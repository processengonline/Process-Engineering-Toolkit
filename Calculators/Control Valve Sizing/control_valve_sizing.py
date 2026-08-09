"""
Control Valve Sizing Utility (control_valve_sizing.py)

Provides basic control valve sizing helpers for liquid (incompressible) flows
using metric (Kv) and imperial (Cv) sizing conventions. Includes:
 - Kv (m³/h · bar^-0.5) and Cv (US gpm · psi^-0.5) conversions
 - Compute Kv/Cv from flow and pressure drop, and vice versa
 - Unit conversion helpers (m3/h <-> GPM, bar <-> psi)
 - Simple CLI and optional JSON/YAML input file support

Notes:
 - This module focuses on liquid (incompressible) valve sizing. Gas/compressible
   flow sizing requires additional equations (isentropic/choked flow) and vendor
   data and is intentionally left out as a placeholder.
 - Kv definition used: Kv = Q(m3/h) / sqrt(deltaP(bar))
 - Cv and Kv conversion: Cv ≈ 1.156 * Kv (approximation used in industry)

Usage examples:
  python control_valve_sizing.py --flow-m3h 50 --deltaP-bar 0.2
  python control_valve_sizing.py --kv 40 --deltaP-bar 0.5
  python control_valve_sizing.py --inputs valve_inputs.json

If you want YAML inputs, install PyYAML (pip install pyyaml) and pass a .yaml file to --inputs.
"""
from dataclasses import dataclass
import math
import argparse
import json
import sys
from typing import Optional, Dict

try:
    import yaml  # type: ignore
    _HAS_YAML = True
except Exception:
    _HAS_YAML = False


# Conversion constants and helpers
CV_KV_FACTOR = 1.156  # Cv ≈ 1.156 * Kv


def kv_from_flow_and_dP(flow_m3_h: float, deltaP_bar: float) -> float:
    """Compute Kv (m3/h / sqrt(bar)) from flow (m3/h) and pressure drop (bar)."""
    if deltaP_bar <= 0:
        raise ValueError("deltaP must be > 0 bar")
    return flow_m3_h / math.sqrt(deltaP_bar)


def cv_from_flow_and_dP_gpm_psi(flow_gpm: float, deltaP_psi: float, sg: float = 1.0) -> float:
    """Compute Cv from flow (US gpm), pressure drop (psi) and specific gravity.
    Standard incompressible liquid formula: Q(gpm) = Cv * sqrt(ΔP(psi) / SG)
    Rearranged: Cv = Q / sqrt(ΔP / SG)
    """
    if deltaP_psi <= 0:
        raise ValueError("deltaP must be > 0 psi")
    if sg <= 0:
        raise ValueError("specific gravity (sg) must be > 0")
    return flow_gpm / math.sqrt(deltaP_psi / sg)


def cv_from_kv(kv: float) -> float:
    return CV_KV_FACTOR * kv


def kv_from_cv(cv: float) -> float:
    return cv / CV_KV_FACTOR


def flow_from_kv(kv: float, deltaP_bar: float) -> float:
    """Compute flow (m3/h) from Kv and pressure drop (bar)."""
    return kv * math.sqrt(deltaP_bar)


def flow_from_cv(cv: float, deltaP_psi: float, sg: float = 1.0) -> float:
    """Compute flow (US gpm) from Cv, ΔP (psi) and specific gravity."""
    return cv * math.sqrt(deltaP_psi / sg)

# Unit conversions

def m3h_to_gpm_us(q_m3h: float) -> float:
    # 1 m3/h = 4.4028675 US gpm
    return q_m3h * 4.4028675


def gpm_us_to_m3h(q_gpm: float) -> float:
    return q_gpm / 4.4028675


def bar_to_psi(p_bar: float) -> float:
    return p_bar * 14.5037738


def psi_to_bar(p_psi: float) -> float:
    return p_psi / 14.5037738


@dataclass
class ValveInputs:
    flow_m3_h: Optional[float] = None
    flow_gpm: Optional[float] = None
    deltaP_bar: Optional[float] = None
    deltaP_psi: Optional[float] = None
    kv: Optional[float] = None
    cv: Optional[float] = None
    specific_gravity: float = 1.0


def parse_inputs_file(path: str) -> Dict:
    if path.lower().endswith(('.yml', '.yaml')):
        if not _HAS_YAML:
            raise RuntimeError("PyYAML not installed. Install with: pip install pyyaml")
        with open(path, 'r', encoding='utf-8') as fh:
            return yaml.safe_load(fh) or {}
    else:
        with open(path, 'r', encoding='utf-8') as fh:
            return json.load(fh) or {}


def compute_from_args(args: argparse.Namespace) -> Dict[str, float]:
    data: Dict = {}
    if getattr(args, 'inputs', None):
        data = parse_inputs_file(args.inputs) or {}

    # overlay CLI args
    def set_if(name, arg=None):
        if arg is None:
            arg = name
        val = getattr(args, arg, None)
        if val is not None:
            data[name] = val

    for name in ('flow_m3_h', 'flow_gpm', 'deltaP_bar', 'deltaP_psi', 'kv', 'cv', 'specific_gravity'):
        set_if(name)

    inputs = ValveInputs(
        flow_m3_h=data.get('flow_m3_h'),
        flow_gpm=data.get('flow_gpm'),
        deltaP_bar=data.get('deltaP_bar'),
        deltaP_psi=data.get('deltaP_psi'),
        kv=data.get('kv'),
        cv=data.get('cv'),
        specific_gravity=float(data.get('specific_gravity', 1.0)),
    )

    results: Dict[str, float] = {}

    # Normalize pressures and flows
    if inputs.deltaP_psi is None and inputs.deltaP_bar is not None:
        inputs.deltaP_psi = bar_to_psi(inputs.deltaP_bar)
    if inputs.deltaP_bar is None and inputs.deltaP_psi is not None:
        inputs.deltaP_bar = psi_to_bar(inputs.deltaP_psi)

    if inputs.flow_gpm is None and inputs.flow_m3_h is not None:
        inputs.flow_gpm = m3h_to_gpm_us(inputs.flow_m3_h)
    if inputs.flow_m3_h is None and inputs.flow_gpm is not None:
        inputs.flow_m3_h = gpm_us_to_m3h(inputs.flow_gpm)

    # If flow and deltaP provided -> compute Kv and Cv
    if inputs.flow_m3_h is not None and inputs.deltaP_bar is not None:
        kv = kv_from_flow_and_dP(inputs.flow_m3_h, inputs.deltaP_bar)
        cv = cv_from_kv(kv)
        results['kv_m3h_per_sqrt_bar'] = kv
        results['cv_usgpm_per_sqrt_psi'] = cv
        results['flow_m3_h'] = inputs.flow_m3_h
        results['flow_gpm_us'] = inputs.flow_gpm
        results['deltaP_bar'] = inputs.deltaP_bar
        results['deltaP_psi'] = inputs.deltaP_psi
        return results

    # If Kv provided -> compute flow for given deltaP
    if inputs.kv is not None and inputs.deltaP_bar is not None:
        q_m3h = flow_from_kv(inputs.kv, inputs.deltaP_bar)
        results['flow_m3_h'] = q_m3h
        results['flow_gpm_us'] = m3h_to_gpm_us(q_m3h)
        results['kv_m3h_per_sqrt_bar'] = inputs.kv
        results['deltaP_bar'] = inputs.deltaP_bar
        results['deltaP_psi'] = inputs.deltaP_psi
        results['cv_usgpm_per_sqrt_psi'] = cv_from_kv(inputs.kv)
        return results

    # If Cv provided -> compute flow for given deltaP (psi)
    if inputs.cv is not None and inputs.deltaP_psi is not None:
        q_gpm = flow_from_cv(inputs.cv, inputs.deltaP_psi, inputs.specific_gravity)
        results['flow_gpm_us'] = q_gpm
        results['flow_m3_h'] = gpm_us_to_m3h(q_gpm)
        results['cv_usgpm_per_sqrt_psi'] = inputs.cv
        results['deltaP_psi'] = inputs.deltaP_psi
        results['deltaP_bar'] = inputs.deltaP_bar
        results['kv_m3h_per_sqrt_bar'] = kv_from_cv(inputs.cv)
        return results

    raise ValueError('Insufficient inputs: provide (flow + deltaP) OR (kv + deltaP) OR (cv + deltaP)')


def _print_results(results: Dict[str, float]):
    print('Control valve sizing results:')
    for k, v in results.items():
        try:
            print(f" - {k}: {v:.6g}")
        except Exception:
            print(f" - {k}: {v}")


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(description='Control Valve Sizing (liquid Kv/Cv)')
    parser.add_argument('--inputs', help='Path to JSON or YAML inputs file', default=None)
    parser.add_argument('--flow-m3h', dest='flow_m3_h', type=float, help='Flow (m³/h)')
    parser.add_argument('--flow-gpm', dest='flow_gpm', type=float, help='Flow (US gpm)')
    parser.add_argument('--deltaP-bar', dest='deltaP_bar', type=float, help='Pressure drop (bar)')
    parser.add_argument('--deltaP-psi', dest='deltaP_psi', type=float, help='Pressure drop (psi)')
    parser.add_argument('--kv', type=float, help='Kv (m³/h per sqrt(bar))')
    parser.add_argument('--cv', type=float, help='Cv (US gpm per sqrt(psi))')
    parser.add_argument('--specific-gravity', type=float, help='Specific gravity for liquid (default 1.0)')

    args = parser.parse_args(argv)

    try:
        results = compute_from_args(args)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    _print_results(results)


if __name__ == '__main__':
    main()
