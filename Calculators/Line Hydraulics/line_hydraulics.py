"""
Line Hydraulics Calculator (line_hydraulics.py)

Provides basic single-phase and simplified two-phase hydraulic calculations for
circular pipes. Features:
 - Single-phase pressure drop using Darcy-Weisbach with friction factor via
   the explicit Swamee-Jain approximation (suitable for turbulent/transitional
   flows) and laminar f = 64/Re.
 - Velocity and Reynolds number calculations.
 - Minor losses from fittings (user-provided K factor) and elevation head.
 - Simple homogeneous two-phase pressure drop estimate using homogeneous
   density and single-phase method as a first approximation, and a basic
   Lockhart-Martinelli correlation (two-phase multiplier) for separated flow
   rough estimate.
 - Unit helpers and a small CLI that supports JSON/YAML input files.

Notes:
 - This module is intended for screening-level engineering estimates only.
 - For critical designs, use detailed multiphase models, vendor software or
   validated correlations for your flow regime and fluid properties.

Usage examples:
  python line_hydraulics.py --flow 0.05 --diameter 0.1 --length 50 --rho 1000 --mu 1e-3 --roughness 1.5e-5
  python line_hydraulics.py --inputs example_pipe.json

YAML support requires PyYAML (pip install pyyaml).
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

G = 9.80665  # m/s^2


@dataclass
class PipeInputs:
    flow_m3_s: float  # volumetric flow rate (m^3/s)
    diameter_m: float  # internal pipe diameter (m)
    length_m: float  # pipe length (m)
    rho: float  # fluid density (kg/m^3)
    mu: float  # dynamic viscosity (Pa.s or N.s/m^2)
    roughness: float = 1.5e-5  # pipe absolute roughness (m), default ~ commercial steel
    gage_elevation_diff_m: float = 0.0  # z2 - z1 (m) positive if downstream higher
    fittings_K: float = 0.0  # sum of K values for minor losses
    two_phase: bool = False  # compute simple two-phase estimates
    rho_g: Optional[float] = None  # gas density (kg/m^3) if two-phase
    mu_g: Optional[float] = None  # gas viscosity (Pa.s) if two-phase
    quality: Optional[float] = None  # vapor mass fraction (0-1) for two-phase


def area_from_d(d: float) -> float:
    return math.pi * (d / 2.0) ** 2


def velocity_from_flow(Q: float, d: float) -> float:
    A = area_from_d(d)
    return Q / A


def reynolds_number(rho: float, v: float, d: float, mu: float) -> float:
    return rho * v * d / mu


def friction_factor_swamee_jain(Re: float, rel_roughness: float) -> float:
    """Swamee-Jain explicit approximation for turbulent flow (Re > ~3000).
    f = 0.25 / [log10(eps/(3.7D) + 5.74/Re^0.9)]^2
    Using format with rel_roughness = eps/D
    """
    if Re <= 0:
        raise ValueError("Reynolds number must be > 0")
    if Re < 2300:
        # laminar
        return 64.0 / Re
    # turbulent: use Swamee-Jain
    term = rel_roughness / 3.7 + 5.74 / (Re ** 0.9)
    f = 0.25 / (math.log10(term) ** 2)
    return f


def darcy_weisbach_pressure_drop(f: float, L: float, D: float, rho: float, v: float) -> float:
    # ΔP (Pa) = f * (L/D) * (rho * v^2 / 2)
    return f * (L / D) * (rho * v * v / 2.0)


def minor_loss_pressure(K_total: float, rho: float, v: float) -> float:
    # ΔP (Pa) = K * (rho * v^2 / 2)
    return K_total * (rho * v * v / 2.0)


# --- Two-phase helpers (simplified approximations) ---

def homogeneous_two_phase_properties(rho_l: float, rho_g: float, quality: float) -> float:
    """Compute a homogeneous mixture density (kg/m3) given liquid/gas densities and vapor quality (mass fraction)."""
    # Avoid division by zero
    if quality is None:
        raise ValueError("quality required for two-phase homogeneous estimate")
    if rho_g is None:
        raise ValueError("rho_g (gas density) required for two-phase homogeneous estimate")
    # mass-based mixing: 1/rho_mix = x/rho_g + (1-x)/rho_l
    x = quality
    inv_rho_mix = x / rho_g + (1.0 - x) / rho_l
    rho_mix = 1.0 / inv_rho_mix
    return rho_mix


def lockhart_martinelli_multiplier(rho_l: float, rho_g: float, Re_l: float, Re_g: float, x: float) -> float:
    """Simple Lockhart-Martinelli two-phase multiplier estimate for pressure drop scaling.
    This returns a two-phase multiplier phi^2 to multiply single-phase liquid pressure drop.
    The implementation follows a basic form using the Chisholm parameter C ≈ 20 for turbulent flows.
    This is a rough screening estimate only.
    """
    # Avoid invalid values
    if x is None or rho_g is None or rho_l is None:
        raise ValueError("liquid/gas properties and quality required for LM estimate")
    # Calculate Martinelli parameter X_tt (chi)
    # X_tt = ( (1-x)/x )^0.9 * (rho_g / rho_l)^0.5 * (mu_l / mu_g)^0.1   [one simplified form]
    # Use simplified form with nominal exponents
    # Ensure positive
    if x <= 0:
        return 1.0
    chi = ((1.0 - x) / x) ** 0.9 * math.sqrt(rho_g / rho_l)
    # pick Chisholm C dependent on flow regime; use 20 (liquid turbulent) as conservative
    C = 20.0
    phi2 = 1.0 + C / (chi ** 0.5) + 1.0 / (chi)  # simplified combination
    # ensure >=1
    return max(phi2, 1.0)


def calculate_single_phase(inputs: PipeInputs) -> Dict[str, float]:
    v = velocity_from_flow(inputs.flow_m3_s, inputs.diameter_m)
    Re = reynolds_number(inputs.rho, v, inputs.diameter_m, inputs.mu)
    rel_roughness = inputs.roughness / inputs.diameter_m
    f = friction_factor_swamee_jain(Re, rel_roughness)
    dp_friction = darcy_weisbach_pressure_drop(f, inputs.length_m, inputs.diameter_m, inputs.rho, v)
    dp_minor = minor_loss_pressure(inputs.fittings_K, inputs.rho, v)
    dp_total = dp_friction + dp_minor + inputs.rho * G * inputs.gage_elevation_diff_m

    results = {
        'velocity_m_s': v,
        'Reynolds_number': Re,
        'friction_factor': f,
        'dp_friction_Pa': dp_friction,
        'dp_minor_Pa': dp_minor,
        'dp_elevation_Pa': inputs.rho * G * inputs.gage_elevation_diff_m,
        'dp_total_Pa': dp_total,
    }
    return results


def calculate_two_phase(inputs: PipeInputs) -> Dict[str, float]:
    # Basic homogeneous mixture estimate
    if inputs.quality is None or inputs.rho_g is None or inputs.mu_g is None:
        raise ValueError('Two-phase calculation requires quality, rho_g and mu_g')
    rho_mix = homogeneous_two_phase_properties(inputs.rho, inputs.rho_g, inputs.quality)
    # use mixture viscosity approx (simple harmonic mean by volume fraction not very accurate)
    # approximate: mu_mix ≈ (1-x)*mu_l + x*mu_g (mass fraction used as proxy)
    mu_mix = (1.0 - inputs.quality) * inputs.mu + inputs.quality * inputs.mu_g
    # reuse single-phase formula with mixture properties
    v = velocity_from_flow(inputs.flow_m3_s, inputs.diameter_m)
    Re_mix = reynolds_number(rho_mix, v, inputs.diameter_m, mu_mix)
    rel_roughness = inputs.roughness / inputs.diameter_m
    f_mix = friction_factor_swamee_jain(Re_mix, rel_roughness)
    dp_friction_single = darcy_weisbach_pressure_drop(f_mix, inputs.length_m, inputs.diameter_m, rho_mix, v)

    # Apply Lockhart-Martinelli multiplier phi^2 to account for two-phase effects (separated flow approximation)
    # Compute approximate Re for liquid and gas phases for LM function
    # Assume volumetric quality alpha approximated by mass quality and densities: alpha ≈ x/rho_g / (x/rho_g + (1-x)/rho_l)
    x = inputs.quality
    alpha = (x / inputs.rho_g) / (x / inputs.rho_g + (1.0 - x) / inputs.rho)
    # approximate phase superficial velocities
    v_g = v * alpha
    v_l = v * (1.0 - alpha)
    Re_g = reynolds_number(inputs.rho_g, v_g if v_g>0 else 1e-12, inputs.diameter_m, inputs.mu_g)
    Re_l = reynolds_number(inputs.rho, v_l if v_l>0 else 1e-12, inputs.diameter_m, inputs.mu)
    phi2 = lockhart_martinelli_multiplier(inputs.rho, inputs.rho_g, Re_l, Re_g, x)

    dp_two_phase = dp_friction_single * phi2
    dp_minor = minor_loss_pressure(inputs.fittings_K, rho_mix, v)
    dp_total = dp_two_phase + dp_minor + rho_mix * G * inputs.gage_elevation_diff_m

    results = {
        'velocity_m_s': v,
        'rho_mix_kg_m3': rho_mix,
        'mu_mix_Pa_s': mu_mix,
        'Re_mix': Re_mix,
        'friction_factor_mix': f_mix,
        'dp_friction_single_Pa': dp_friction_single,
        'lockhart_martinelli_phi2': phi2,
        'dp_two_phase_Pa': dp_two_phase,
        'dp_minor_Pa': dp_minor,
        'dp_total_Pa': dp_total,
    }
    return results


def parse_inputs_file(path: str) -> Dict:
    if path.lower().endswith(('.yml', '.yaml')):
        if not _HAS_YAML:
            raise RuntimeError('PyYAML not installed. Install with: pip install pyyaml')
        with open(path, 'r', encoding='utf-8') as fh:
            return yaml.safe_load(fh) or {}
    else:
        with open(path, 'r', encoding='utf-8') as fh:
            return json.load(fh) or {}


def args_to_inputs(args: argparse.Namespace) -> PipeInputs:
    data: Dict = {}
    if getattr(args, 'inputs', None):
        data = parse_inputs_file(args.inputs) or {}

    # overlay CLI args
    def _set(name, arg=None):
        if arg is None:
            arg = name
        val = getattr(args, arg, None)
        if val is not None:
            data[name] = val

    for name in ('flow_m3_s', 'diameter_m', 'length_m', 'rho', 'mu', 'roughness', 'gage_elevation_diff_m', 'fittings_K', 'two_phase', 'rho_g', 'mu_g', 'quality'):
        _set(name)

    try:
        inputs = PipeInputs(
            flow_m3_s=float(data['flow_m3_s']),
            diameter_m=float(data['diameter_m']),
            length_m=float(data['length_m']),
            rho=float(data['rho']),
            mu=float(data['mu']),
            roughness=float(data.get('roughness', 1.5e-5)),
            gage_elevation_diff_m=float(data.get('gage_elevation_diff_m', 0.0)),
            fittings_K=float(data.get('fittings_K', 0.0)),
            two_phase=bool(data.get('two_phase', False)),
            rho_g=float(data.get('rho_g')) if data.get('rho_g') is not None else None,
            mu_g=float(data.get('mu_g')) if data.get('mu_g') is not None else None,
            quality=float(data.get('quality')) if data.get('quality') is not None else None,
        )
    except KeyError as ke:
        raise ValueError(f"Missing required input: {ke}")
    return inputs


def print_results(results: Dict[str, float]):
    print('Line hydraulics results:')
    for k, v in results.items():
        try:
            print(f" - {k}: {v:.6g}")
        except Exception:
            print(f" - {k}: {v}")


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(description='Line Hydraulics (single-phase and simplified two-phase)')
    parser.add_argument('--inputs', help='Path to JSON or YAML inputs file', default=None)
    parser.add_argument('--flow', dest='flow_m3_s', type=float, help='Volumetric flow (m^3/s)')
    parser.add_argument('--diameter', dest='diameter_m', type=float, help='Internal diameter (m)')
    parser.add_argument('--length', dest='length_m', type=float, help='Pipe length (m)')
    parser.add_argument('--rho', type=float, help='Liquid density (kg/m^3)')
    parser.add_argument('--mu', type=float, help='Liquid viscosity (Pa.s)')
    parser.add_argument('--roughness', type=float, help='Pipe absolute roughness (m)')
    parser.add_argument('--elevation-diff', dest='gage_elevation_diff_m', type=float, help='Elevation difference z2 - z1 (m)')
    parser.add_argument('--fittings-K', dest='fittings_K', type=float, help='Sum of minor loss K values')
    parser.add_argument('--two-phase', dest='two_phase', action='store_true', help='Enable simplified two-phase estimate')
    parser.add_argument('--rho-g', dest='rho_g', type=float, help='Gas density (kg/m^3) for two-phase')
    parser.add_argument('--mu-g', dest='mu_g', type=float, help='Gas viscosity (Pa.s) for two-phase')
    parser.add_argument('--quality', type=float, help='Vapor mass quality (0-1) for two-phase')

    args = parser.parse_args(argv)

    try:
        inputs = args_to_inputs(args)
    except Exception as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    try:
        if inputs.two_phase:
            results = calculate_two_phase(inputs)
        else:
            results = calculate_single_phase(inputs)
    except Exception as exc:
        print(f"Calculation error: {exc}", file=sys.stderr)
        sys.exit(3)

    print_results(results)


if __name__ == '__main__':
    main()
