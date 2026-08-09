"""
Tank Heat Loss Calculator (tank_heat_loss.py)

Provides functions to compute steady-state heat losses for a vertical cylindrical storage tank
(shell, roof, bottom) and a small CLI to run the calculation from the command line.

Units: SI (meters, degrees C, W/m·K)

Usage examples:

# Quick run from CLI:
python tank_heat_loss.py --diameter 10 --height 8 --product-temp 60 --ambient-temp 20 \
    --ins-thickness 0.05 --ins-k 0.04 --hi 10 --ho 10

# Load inputs from JSON (example config.json):
python tank_heat_loss.py --inputs config.json

If you want to use YAML inputs, install PyYAML (pip install pyyaml) and pass a .yaml file to --inputs.

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


@dataclass
class TankInputs:
    diameter: float  # m
    height: float  # m (liquid height)
    product_temp: float  # °C
    ambient_temp: float  # °C
    insulation_thickness: float = 0.0  # m
    insulation_k: float = 0.04  # W/m·K (typical)
    hi: float = 10.0  # internal convective HT coeff, W/m²·K
    ho: float = 10.0  # external convective HT coeff, W/m²·K
    roof_type: str = "flat"  # currently only affects area formula
    bottom_present: bool = True
    safety_factor: float = 1.15  # design safety factor for heating duty


def area_shell(diameter: float, height: float) -> float:
    """Shell lateral surface area: A = π D H"""
    return math.pi * diameter * height


def area_roof(diameter: float, roof_type: str = "flat") -> float:
    """Roof area. For flat roofs, area = π D² / 4. For conical/domed roofs this can be extended."""
    return math.pi * diameter * diameter / 4.0


def area_bottom(diameter: float, bottom_present: bool = True) -> float:
    """Bottom area for flat-bottom tanks. If no bottom, returns 0."""
    if not bottom_present:
        return 0.0
    return math.pi * diameter * diameter / 4.0


def overall_u_value(ins_thickness: float, ins_k: float, hi: float, ho: float) -> float:
    """Compute overall heat transfer coefficient U (W/m²·K).

    1/U = 1/hi + tins/kins + 1/ho
    If no insulation (tins == 0) the conduction term is zero.
    """
    if ins_thickness <= 0.0:
        # conduction term is negligible
        r_total = (1.0 / hi) + (1.0 / ho)
    else:
        r_total = (1.0 / hi) + (ins_thickness / ins_k) + (1.0 / ho)
    U = 1.0 / r_total
    return U


def heat_loss(U: float, area: float, tf: float, ta: float) -> float:
    """Heat loss (W) for a surface: Q = U * A * (Tf - Ta)"""
    return U * area * (tf - ta)


def energy_loss_per_day(q_total_watts: float) -> float:
    """Energy loss in kWh per day: Q (W) * 24 / 1000"""
    return q_total_watts * 24.0 / 1000.0


def heating_duty(q_total_watts: float, safety_factor: float = 1.15) -> float:
    """Heating duty (W) with a design safety factor applied."""
    return q_total_watts * safety_factor


def calculate(inputs: TankInputs) -> Dict[str, float]:
    """Run full calculation and return a dictionary of results (W and derived units)."""
    Ashell = area_shell(inputs.diameter, inputs.height)
    Aroof = area_roof(inputs.diameter, inputs.roof_type)
    Abottom = area_bottom(inputs.diameter, inputs.bottom_present)
    Atotal = Ashell + Aroof + Abottom

    U_shell = overall_u_value(inputs.insulation_thickness, inputs.insulation_k, inputs.hi, inputs.ho)
    # For simplicity we assume same U for roof and bottom; this can be extended.
    U_roof = U_shell
    U_bottom = U_shell

    Q_shell = heat_loss(U_shell, Ashell, inputs.product_temp, inputs.ambient_temp)
    Q_roof = heat_loss(U_roof, Aroof, inputs.product_temp, inputs.ambient_temp)
    Q_bottom = heat_loss(U_bottom, Abottom, inputs.product_temp, inputs.ambient_temp)

    Q_total = Q_shell + Q_roof + Q_bottom
    energy_kwh_day = energy_loss_per_day(Q_total)
    duty_w = heating_duty(Q_total, inputs.safety_factor)

    results = {
        "Ashell_m2": Ashell,
        "Aroof_m2": Aroof,
        "Abottom_m2": Abottom,
        "Atotal_m2": Atotal,
        "U_shell_W_m2K": U_shell,
        "U_roof_W_m2K": U_roof,
        "U_bottom_W_m2K": U_bottom,
        "Q_shell_W": Q_shell,
        "Q_roof_W": Q_roof,
        "Q_bottom_W": Q_bottom,
        "Q_total_W": Q_total,
        "Energy_kWh_per_day": energy_kwh_day,
        "Heating_duty_W (with safety factor)": duty_w,
    }
    return results


def _print_results(results: Dict[str, float]):
    print("Calculation results:")
    for k, v in results.items():
        print(f" - {k}: {v:.3f}")


def _parse_inputs_from_file(path: str) -> Dict:
    if path.lower().endswith(('.yml', '.yaml')):
        if not _HAS_YAML:
            raise RuntimeError("PyYAML not installed. Install with: pip install pyyaml")
        with open(path, 'r', encoding='utf-8') as fh:
            return yaml.safe_load(fh)
    else:
        # assume JSON
        with open(path, 'r', encoding='utf-8') as fh:
            return json.load(fh)


def _args_to_inputs(args: argparse.Namespace) -> TankInputs:
    # If inputs file provided, load and overlay with cli args
    data = {}
    if getattr(args, 'inputs', None):
        data = _parse_inputs_from_file(args.inputs) or {}
    # overlay CLI args (if set)
    def _set_if_provided(name):
        val = getattr(args, name, None)
        if val is not None:
            data[name] = val

    for name in ('diameter', 'height', 'product_temp', 'ambient_temp', 'insulation_thickness', 'insulation_k', 'hi', 'ho', 'roof_type', 'bottom_present', 'safety_factor'):
        _set_if_provided(name)

    # Apply defaults and create TankInputs
    try:
        ti = TankInputs(
            diameter=float(data.get('diameter')),
            height=float(data.get('height')),
            product_temp=float(data.get('product_temp')),
            ambient_temp=float(data.get('ambient_temp')),
            insulation_thickness=float(data.get('insulation_thickness', 0.0)),
            insulation_k=float(data.get('insulation_k', 0.04)),
            hi=float(data.get('hi', 10.0)),
            ho=float(data.get('ho', 10.0)),
            roof_type=str(data.get('roof_type', 'flat')),
            bottom_present=bool(data.get('bottom_present', True)),
            safety_factor=float(data.get('safety_factor', 1.15)),
        )
    except Exception as exc:
        raise ValueError(f"Invalid or missing inputs: {exc}")
    return ti


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(description="Tank Heat Loss Calculator")
    parser.add_argument('--inputs', help='Path to JSON or YAML inputs file', default=None)
    parser.add_argument('--diameter', type=float, help='Tank diameter (m)')
    parser.add_argument('--height', type=float, help='Liquid height / shell height (m)')
    parser.add_argument('--product-temp', dest='product_temp', type=float, help='Product temperature (°C)')
    parser.add_argument('--ambient-temp', dest='ambient_temp', type=float, help='Ambient temperature (°C)')
    parser.add_argument('--ins-thickness', dest='insulation_thickness', type=float, help='Insulation thickness (m)')
    parser.add_argument('--ins-k', dest='insulation_k', type=float, help='Insulation thermal conductivity (W/m·K)')
    parser.add_argument('--hi', type=float, help='Internal heat transfer coefficient (W/m²·K)')
    parser.add_argument('--ho', type=float, help='External heat transfer coefficient (W/m²·K)')
    parser.add_argument('--roof-type', dest='roof_type', type=str, help='Roof type (flat)'),
    parser.add_argument('--bottom-present', dest='bottom_present', type=lambda s: s.lower() in ('1','true','yes'), help='Bottom present: true/false')
    parser.add_argument('--safety-factor', dest='safety_factor', type=float, help='Design safety factor for heating duty')

    args = parser.parse_args(argv)

    try:
        inputs = _args_to_inputs(args)
    except Exception as exc:
        print(f"Error creating inputs: {exc}", file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    results = calculate(inputs)
    _print_results(results)


if __name__ == '__main__':
    main()
