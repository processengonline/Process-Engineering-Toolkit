"""
PSV Sizing Calculator (psv_sizing.py)

Provides simplified pressure safety valve (PSV) sizing calculations for
screening-level engineering. Supports both gas (compressible) and liquid
(incompressible) relieving conditions with simple isentropic/choked flow
estimates for gases and orifice flow for liquids.

Features
- Compute required orifice area for a target mass flow (kg/s) or volumetric
  flow (m^3/s).
- Gas relief: determines if flow is choked and uses appropriate isentropic
  formula. Assumes ideal gas behavior and steady isentropic expansion.
- Liquid relief: uses incompressible orifice equation Q = Cd*A*sqrt(2*ΔP/ρ).
- Simple CLI and JSON/YAML input file support (YAML optional if PyYAML installed).
- Returns required area (m^2) and equivalent diameter (mm) and notes.

Caveats
- This is a screening tool. Final PSV selection must use vendor-certified
  methods (API 520/521), two-phase relief correlations, and account for
  inlet/outlet conditions, backpressure, blowdown, and alpha factors.
- Units: SI (Pa, K, m, kg, s). User may provide pressures in bar or barg; the
  CLI supports Pa or bar via input file or flags.
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

# Universal gas constant J/(kmol*K)
R_UNIVERSAL = 8314.462618


@dataclass
class PSVInputs:
    phase: str  # 'gas' or 'liquid'
    mass_flow_kg_s: Optional[float] = None  # kg/s (preferred for gas)
    vol_flow_m3_s: Optional[float] = None  # m3/s (alternative; needs density)
    rho: Optional[float] = None  # kg/m3 (required for liquid or to convert vol->mass)
    inlet_pressure_Pa: Optional[float] = None  # Pa (upstream relieving absolute pressure)
    outlet_pressure_Pa: Optional[float] = None  # Pa (downstream / backpressure absolute)
    temperature_K: Optional[float] = None  # K (gas temperature at inlet)
    molecular_weight_gpmol: Optional[float] = None  # g/mol (kg/kmol) for gas
    gamma: float = 1.4  # specific heat ratio for gas (default air)
    Cd: float = 0.9  # discharge coefficient / efficiency


def bar_to_Pa(p_bar: float) -> float:
    return p_bar * 1e5


def Pa_to_bar(p_pa: float) -> float:
    return p_pa / 1e5


def mass_from_vol(vol_m3_s: float, rho: float) -> float:
    return vol_m3_s * rho


def equivalent_diameter(area_m2: float) -> float:
    """Return equivalent circular diameter in meters and millimeters."""
    if area_m2 <= 0:
        return 0.0
    d_m = math.sqrt(4.0 * area_m2 / math.pi)
    return d_m


# --- Gas (compressible) flow formulas ---

def critical_pressure_ratio(gamma: float) -> float:
    """Critical (choke) downstream-to-upstream pressure ratio: (2/(gamma+1))^(gamma/(gamma-1))"""
    return (2.0 / (gamma + 1.0)) ** (gamma / (gamma - 1.0))


def choked_mass_flux(P0: float, T0: float, M: float, gamma: float) -> float:
    """Return mass flux (kg/s·m2) for choked (critical) isentropic flow.

    Formula (ideal gas, isentropic):
      G_crit = P0 * sqrt(gamma / (R_specific * T0)) * (2/(gamma+1))^{(gamma+1)/(2*(gamma-1))}
    where R_specific = R_universal / M (M in kg/kmol).
    P0 in Pa, T0 in K -> G in kg/(s·m2)
    """
    if T0 is None or M is None:
        raise ValueError("Temperature and molecular weight required for gas calculation")
    R_spec = R_UNIVERSAL / M
    factor = (2.0 / (gamma + 1.0)) ** ((gamma + 1.0) / (2.0 * (gamma - 1.0)))
    G = P0 * math.sqrt(gamma / (R_spec * T0)) * factor
    return G


def isentropic_mass_flow(P0: float, P2: float, T0: float, M: float, gamma: float, A: float, Cd: float) -> float:
    """Compute mass flow rate (kg/s) for isentropic nozzle/orifice given area A (m2).
    Handles both choked and sub-critical cases.

    Equations from isentropic relations for ideal gas.
    """
    if P2 <= 0 or P0 <= 0:
        raise ValueError("Pressures must be > 0")
    Pratio = P2 / P0
    Pc = critical_pressure_ratio(gamma)
    R_spec = R_UNIVERSAL / M
    if Pratio <= Pc:
        # Choked flow
        G = choked_mass_flux(P0, T0, M, gamma)
        m_dot = Cd * A * G
        return m_dot
    else:
        # Sub-critical isentropic mass flow formula
        # m_dot = Cd * A * P0 * sqrt( (2*gamma/(R*T*(gamma-1))) * (Pratio^(2/gamma) * (1 - Pratio^((gamma-1)/gamma))) )
        term = (2.0 * gamma) / (R_spec * T0 * (gamma - 1.0))
        part = (Pratio ** (2.0 / gamma)) * (1.0 - Pratio ** ((gamma - 1.0) / gamma))
        m_dot = Cd * A * P0 * math.sqrt(term * part)
        return m_dot


def required_area_for_gas_massflow(m_dot: float, P0: float, P2: float, T0: float, M: float, gamma: float, Cd: float) -> Dict[str, float]:
    """Compute required orifice area (m2) and diameter (mm) for a target mass flow m_dot (kg/s).
    Determines if flow is choked; if choked, uses mass flux inversion; otherwise numerically solve for A using isentropic formula.
    Returns dict with area, diameter_mm, choked (bool) and notes.
    """
    if m_dot <= 0:
        raise ValueError("Mass flow must be > 0")
    Pratio = P2 / P0
    Pc = critical_pressure_ratio(gamma)
    notes = []
    if Pratio <= Pc:
        # choked; use mass flux G and invert
        G = choked_mass_flux(P0, T0, M, gamma)
        A = m_dot / (Cd * G)
        choked = True
        notes.append('Choked flow (critical) assumed')
    else:
        # Not choked; need to solve for A from isentropic_mass_flow -> A = m_dot / (Cd * P0 * sqrt(term*part))
        R_spec = R_UNIVERSAL / M
        term = (2.0 * gamma) / (R_spec * T0 * (gamma - 1.0))
        part = (Pratio ** (2.0 / gamma)) * (1.0 - Pratio ** ((gamma - 1.0) / gamma))
        denom = Cd * P0 * math.sqrt(term * part)
        if denom <= 0:
            raise ValueError('Denominator non-positive, check inputs')
        A = m_dot / denom
        choked = False
        notes.append('Sub-critical isentropic flow assumed')

    d_m = equivalent_diameter(A)
    return {'area_m2': A, 'diameter_m': d_m, 'diameter_mm': d_m * 1000.0, 'choked': choked, 'notes': '; '.join(notes)}


# --- Liquid (incompressible) orifice equation ---

def required_area_for_liquid_volflow(Q: float, deltaP: float, rho: float, Cd: float) -> Dict[str, float]:
    """Compute orifice area for volumetric flow Q (m3/s) through an orifice with pressure drop deltaP (Pa).

    Q = Cd * A * sqrt(2*deltaP/rho)  =>  A = Q / (Cd * sqrt(2*deltaP/rho))
    """
    if Q <= 0:
        raise ValueError('Volumetric flow must be > 0')
    if deltaP <= 0:
        raise ValueError('Pressure drop must be > 0')
    denom = Cd * math.sqrt(2.0 * deltaP / rho)
    if denom <= 0:
        raise ValueError('Invalid denominator in liquid area calculation')
    A = Q / denom
    d_m = equivalent_diameter(A)
    return {'area_m2': A, 'diameter_m': d_m, 'diameter_mm': d_m * 1000.0}


# --- Input parsing and CLI glue ---

def parse_inputs_file(path: str) -> Dict:
    if path.lower().endswith(('.yml', '.yaml')):
        if not _HAS_YAML:
            raise RuntimeError('PyYAML not installed. Install with: pip install pyyaml')
        with open(path, 'r', encoding='utf-8') as fh:
            return yaml.safe_load(fh) or {}
    else:
        with open(path, 'r', encoding='utf-8') as fh:
            return json.load(fh) or {}


def build_inputs_from_args(args: argparse.Namespace) -> PSVInputs:
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

    for name in ('phase', 'mass_flow_kg_s', 'vol_flow_m3_s', 'rho', 'inlet_pressure_Pa', 'outlet_pressure_Pa', 'temperature_K', 'molecular_weight_gpmol', 'gamma', 'Cd'):
        _set(name)

    # If pressures provided in bar via CLI, allow user to pass inlet_pressure_bar/outlet_pressure_bar
    if getattr(args, 'inlet_pressure_bar', None) is not None and 'inlet_pressure_Pa' not in data:
        data['inlet_pressure_Pa'] = bar_to_Pa(float(args.inlet_pressure_bar))
    if getattr(args, 'outlet_pressure_bar', None) is not None and 'outlet_pressure_Pa' not in data:
        data['outlet_pressure_Pa'] = bar_to_Pa(float(args.outlet_pressure_bar))

    # Build PSVInputs with validation/defaults
    phase = str(data.get('phase', 'gas')).lower()
    if phase not in ('gas', 'liquid'):
        raise ValueError('phase must be "gas" or "liquid"')

    try:
        inputs = PSVInputs(
            phase=phase,
            mass_flow_kg_s=float(data.get('mass_flow_kg_s')) if data.get('mass_flow_kg_s') is not None else None,
            vol_flow_m3_s=float(data.get('vol_flow_m3_s')) if data.get('vol_flow_m3_s') is not None else None,
            rho=float(data.get('rho')) if data.get('rho') is not None else None,
            inlet_pressure_Pa=float(data.get('inlet_pressure_Pa')) if data.get('inlet_pressure_Pa') is not None else None,
            outlet_pressure_Pa=float(data.get('outlet_pressure_Pa')) if data.get('outlet_pressure_Pa') is not None else None,
            temperature_K=float(data.get('temperature_K')) if data.get('temperature_K') is not None else None,
            molecular_weight_gpmol=float(data.get('molecular_weight_gpmol')) if data.get('molecular_weight_gpmol') is not None else None,
            gamma=float(data.get('gamma', 1.4)),
            Cd=float(data.get('Cd', 0.9)),
        )
    except Exception as exc:
        raise ValueError(f'Invalid inputs: {exc}')

    return inputs


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(description='PSV Sizing (simplified screening tool)')
    parser.add_argument('--inputs', help='Path to JSON or YAML inputs file', default=None)
    parser.add_argument('--phase', help='gas or liquid')
    parser.add_argument('--mass-flow-kg-s', dest='mass_flow_kg_s', type=float, help='Mass flow (kg/s)')
    parser.add_argument('--vol-flow-m3-s', dest='vol_flow_m3_s', type=float, help='Volumetric flow (m3/s)')
    parser.add_argument('--rho', type=float, help='Fluid density (kg/m3)')
    parser.add_argument('--inlet-pressure-Pa', dest='inlet_pressure_Pa', type=float, help='Inlet absolute pressure (Pa)')
    parser.add_argument('--outlet-pressure-Pa', dest='outlet_pressure_Pa', type=float, help='Outlet/backpressure absolute (Pa)')
    parser.add_argument('--inlet-pressure-bar', dest='inlet_pressure_bar', type=float, help='Inlet pressure (bar) — convenience')
    parser.add_argument('--outlet-pressure-bar', dest='outlet_pressure_bar', type=float, help='Outlet pressure (bar) — convenience')
    parser.add_argument('--temperature-K', dest='temperature_K', type=float, help='Gas temperature (K)')
    parser.add_argument('--molecular-weight', dest='molecular_weight_gpmol', type=float, help='Molecular weight (g/mol == kg/kmol)')
    parser.add_argument('--gamma', type=float, help='Specific heat ratio for gas (default 1.4)')
    parser.add_argument('--Cd', type=float, help='Discharge coefficient (default 0.9)')

    args = parser.parse_args(argv)

    try:
        inputs = build_inputs_from_args(args)
    except Exception as exc:
        print(f'Input error: {exc}', file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    try:
        # Normalize mass flow from vol flow if provided
        if inputs.mass_flow_kg_s is None and inputs.vol_flow_m3_s is not None:
            if inputs.rho is None:
                raise ValueError('rho required to convert vol_flow to mass_flow')
            inputs.mass_flow_kg_s = mass_from_vol(inputs.vol_flow_m3_s, inputs.rho)

        if inputs.phase == 'gas':
            # Required inputs for gas: mass_flow_kg_s, inlet_pressure_Pa, outlet_pressure_Pa, temperature_K, molecular_weight_gpmol
            missing = []
            for field in ('mass_flow_kg_s', 'inlet_pressure_Pa', 'outlet_pressure_Pa', 'temperature_K', 'molecular_weight_gpmol'):
                if getattr(inputs, field) is None:
                    missing.append(field)
            if missing:
                raise ValueError(f'Missing required gas inputs: {missing}')
            res = required_area_for_gas_massflow(
                m_dot=inputs.mass_flow_kg_s,
                P0=inputs.inlet_pressure_Pa,
                P2=inputs.outlet_pressure_Pa,
                T0=inputs.temperature_K,
                M=inputs.molecular_weight_gpmol,
                gamma=inputs.gamma,
                Cd=inputs.Cd,
            )
        else:
            # liquid path: need vol_flow or mass_flow+rho, and pressure drop (inlet - outlet)
            if inputs.rho is None:
                raise ValueError('rho required for liquid calculation')
            if inputs.vol_flow_m3_s is None and inputs.mass_flow_kg_s is None:
                raise ValueError('Provide vol_flow_m3_s or mass_flow_kg_s for liquid')
            Q = inputs.vol_flow_m3_s if inputs.vol_flow_m3_s is not None else inputs.mass_flow_kg_s / inputs.rho
            if inputs.inlet_pressure_Pa is None or inputs.outlet_pressure_Pa is None:
                raise ValueError('Provide inlet and outlet pressures to compute deltaP for liquid path')
            deltaP = inputs.inlet_pressure_Pa - inputs.outlet_pressure_Pa
            if deltaP <= 0:
                raise ValueError('inlet_pressure must be greater than outlet_pressure for liquid flow')
            res = required_area_for_liquid_volflow(Q=Q, deltaP=deltaP, rho=inputs.rho, Cd=inputs.Cd)

    except Exception as exc:
        print(f'Calculation error: {exc}', file=sys.stderr)
        sys.exit(3)

    # Print results
    print('PSV sizing results (screening):')
    for k, v in res.items():
        try:
            if isinstance(v, float):
                print(f' - {k}: {v:.6g}')
            else:
                print(f' - {k}: {v}')
        except Exception:
            print(f' - {k}: {v}')


if __name__ == '__main__':
    main()
