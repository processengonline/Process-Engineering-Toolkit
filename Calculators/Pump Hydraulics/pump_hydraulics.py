"""
Pump Hydraulics Calculator (pump_hydraulics.py)

Provides basic hydraulic calculations for centrifugal pumps:
 - Compute hydraulic power and shaft power requirement
 - Compute pump head for a given flow and power
 - Unit conversions for flow (m3/s, m3/h, L/s, US gpm) and power (W, kW, HP)
 - Estimate Net Positive Suction Head Required (NPSHr) using a simple correlation placeholder

Includes a small CLI to run calculations from command line or from a JSON/YAML inputs file.

Units: SI by default (m, m³/s, W). Gravity constant g = 9.80665 m/s².

Usage examples:
  python pump_hydraulics.py --flow 0.05 --head 30 --efficiency 0.75
  python pump_hydraulics.py --power 5000 --flow 0.1 --efficiency 0.8
  python pump_hydraulics.py --inputs pump_inputs.json

If you want YAML inputs, install PyYAML (pip install pyyaml) and pass a .yaml file to --inputs.

Changelog:
 - Fixed: --flow-gpm was accepted by the CLI but never converted to flow_m3_s,
   silently producing a "Flow is required" error. Now wired up the same way
   as --flow-m3h and --flow-Ls (US gpm -> m3/s via /15850.3231).
 - Fixed: calculate() now validates flow_m3_s > 0 consistently for both the
   head->power and power->head branches. Previously a flow of 0 on the
   head->power path silently returned an all-zero result instead of raising
   a validation error, unlike the power->head path which already rejected it.
 - Removed: the NPSH available / NPSH margin check (npsh_available_m input,
   --npsh-available CLI flag, npsh_margin_m output). The NPSHr estimate
   itself (npshr_estimated_m) is unchanged and still always returned by
   calculate() — only the available-vs-required margin comparison was
   removed.
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

G = 9.80665  # m/s²


@dataclass
class PumpInputs:
    flow_m3_s: Optional[float] = None  # m³/s
    head_m: Optional[float] = None  # m
    efficiency: float = 0.75  # decimal (0-1)
    power_W: Optional[float] = None  # W (shaft input power)
    density: float = 1000.0  # kg/m³ (water)
    viscosity_cp: Optional[float] = None  # cP (optional, for notes)


def hydraulic_power_W(rho: float, g: float, Q_m3_s: float, H_m: float) -> float:
    """Hydraulic power delivered to fluid (W): P = rho * g * Q * H"""
    return rho * g * Q_m3_s * H_m


def shaft_power_W(hydraulic_power_w: float, efficiency: float) -> float:
    """Shaft input power required (W) considering pump efficiency."""
    if efficiency <= 0 or efficiency > 1:
        raise ValueError("Efficiency should be in (0,1]")
    return hydraulic_power_w / efficiency


def head_from_power_and_flow(power_W: float, rho: float, g: float, Q_m3_s: float, efficiency: float) -> float:
    """Compute pump head (m) from input shaft power (W) and flow (m³/s):
    hydraulic_power = power * efficiency -> H = P_hyd / (rho*g*Q)
    """
    if Q_m3_s <= 0:
        raise ValueError("Flow must be > 0")
    P_hyd = power_W * efficiency
    return P_hyd / (rho * g * Q_m3_s)


def estimate_npshr(flow_m3_s: float, diameter_m: Optional[float] = None) -> float:
    """Estimate NPSHr (m) using a simple empirical placeholder.

    NOTE: This is a rough placeholder for demonstration. For real designs use vendor data or detailed pump curves.
    Here we use a simple scaling: NPSHr ≈ 0.5 + 5 * (Q_norm)**0.6 where Q_norm is in m3/s scaled by 0.01.
    """
    Q_norm = flow_m3_s / 0.01 if flow_m3_s is not None else 0.0
    if Q_norm <= 0:
        return 0.0
    return 0.5 + 5.0 * (Q_norm ** 0.6)


# Unit conversions

def m3s_to_m3h(q: float) -> float:
    return q * 3600.0


def m3s_to_Ls(q: float) -> float:
    return q * 1000.0


def m3s_to_gpm_us(q: float) -> float:
    return q * 15850.3231  # approx conversion m3/s -> US gpm


def W_to_kW(p: float) -> float:
    return p / 1000.0


def W_to_hp(p: float) -> float:
    return p / 745.699872


def parse_inputs_file(path: str) -> Dict:
    if path.lower().endswith(('.yml', '.yaml')):
        if not _HAS_YAML:
            raise RuntimeError("PyYAML not installed. Install with: pip install pyyaml")
        with open(path, 'r', encoding='utf-8') as fh:
            return yaml.safe_load(fh) or {}
    else:
        with open(path, 'r', encoding='utf-8') as fh:
            return json.load(fh) or {}


def _args_to_inputs(args: argparse.Namespace) -> PumpInputs:
    data: Dict = {}
    if getattr(args, 'inputs', None):
        data = parse_inputs_file(args.inputs) or {}

    # overlay CLI args
    def _set_if_provided(field, argname=None):
        if argname is None:
            argname = field
        val = getattr(args, argname, None)
        if val is not None:
            data[field] = val

    for name in ('flow_m3_s', 'head_m', 'efficiency', 'power_W', 'density', 'viscosity_cp'):
        _set_if_provided(name)

    # support alternative CLI names
    if getattr(args, 'flow_m3h', None) is not None and 'flow_m3_s' not in data:
        data['flow_m3_s'] = float(args.flow_m3h) / 3600.0

    if getattr(args, 'flow_l_s', None) is not None and 'flow_m3_s' not in data:
        data['flow_m3_s'] = float(args.flow_l_s) / 1000.0

    if getattr(args, 'flow_gpm', None) is not None and 'flow_m3_s' not in data:
        data['flow_m3_s'] = float(args.flow_gpm) / 15850.3231

    # Build dataclass with defaults
    return PumpInputs(
        flow_m3_s=float(data.get('flow_m3_s')) if data.get('flow_m3_s') is not None else None,
        head_m=float(data.get('head_m')) if data.get('head_m') is not None else None,
        efficiency=float(data.get('efficiency', 0.75)),
        power_W=float(data.get('power_W')) if data.get('power_W') is not None else None,
        density=float(data.get('density', 1000.0)),
        viscosity_cp=data.get('viscosity_cp'),
    )


def calculate(inputs: PumpInputs) -> Dict[str, float]:
    """Perform calculations and return a results dict."""
    if inputs.flow_m3_s is None:
        raise ValueError('Flow (flow_m3_s) is required')
    if inputs.flow_m3_s <= 0:
        raise ValueError('Flow must be > 0')

    results: Dict[str, float] = {}
    Q = inputs.flow_m3_s

    # If head provided, compute hydraulic and shaft power
    if inputs.head_m is not None:
        P_hyd = hydraulic_power_W(inputs.density, G, Q, inputs.head_m)
        P_shaft = shaft_power_W(P_hyd, inputs.efficiency)
        results['hydraulic_power_W'] = P_hyd
        results['shaft_power_W'] = P_shaft
        results['shaft_power_kW'] = W_to_kW(P_shaft)
        results['shaft_power_HP'] = W_to_hp(P_shaft)

    # If power provided but head not, compute head from power
    if inputs.power_W is not None and inputs.head_m is None:
        H = head_from_power_and_flow(inputs.power_W, inputs.density, G, Q, inputs.efficiency)
        results['computed_head_m'] = H

    # Always provide flow unit conversions
    results['flow_m3_s'] = Q
    results['flow_m3_h'] = m3s_to_m3h(Q)
    results['flow_L_s'] = m3s_to_Ls(Q)
    results['flow_gpm_us'] = m3s_to_gpm_us(Q)

    # NPSHr estimate (placeholder, screening only)
    results['npshr_estimated_m'] = estimate_npshr(Q)

    return results


def _print_results(results: Dict[str, float]):
    print('Pump hydraulics results:')
    for k, v in results.items():
        try:
            print(f" - {k}: {v:.6g}")
        except Exception:
            print(f" - {k}: {v}")


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(description='Pump Hydraulics Calculator')
    parser.add_argument('--inputs', help='Path to JSON or YAML inputs file', default=None)
    parser.add_argument('--flow-m3s', dest='flow_m3_s', type=float, help='Flow (m³/s)')
    parser.add_argument('--flow-m3h', dest='flow_m3h', type=float, help='Flow (m³/h)')
    parser.add_argument('--flow-Ls', dest='flow_l_s', type=float, help='Flow (L/s)')
    parser.add_argument('--flow-gpm', dest='flow_gpm', type=float, help='Flow (US gpm)')
    parser.add_argument('--head', dest='head_m', type=float, help='Pump head (m)')
    parser.add_argument('--efficiency', type=float, help='Pump efficiency (decimal, 0-1)')
    parser.add_argument('--power-W', dest='power_W', type=float, help='Shaft input power (W)')
    parser.add_argument('--density', type=float, help='Fluid density (kg/m³)')
    parser.add_argument('--viscosity-cp', dest='viscosity_cp', type=float, help='Fluid viscosity (cP)')

    args = parser.parse_args(argv)

    try:
        inputs = _args_to_inputs(args)
    except Exception as exc:
        print(f"Error creating inputs: {exc}", file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    try:
        results = calculate(inputs)
    except Exception as exc:
        print(f"Calculation error: {exc}", file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    _print_results(results)


if __name__ == '__main__':
    main()
