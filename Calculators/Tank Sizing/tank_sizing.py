"""
Tank Sizing Calculator (tank_sizing.py)

Simple utilities to size a vertical cylindrical storage tank (volume, dimensions,
and surface areas). Includes a small CLI to compute:
 - volume from diameter and height
 - required diameter (or height) for a target volume
 - shell, roof and bottom areas for insulation/heat-loss estimation

Units: SI (meters, cubic meters, kg/m³)

Usage examples:
    python tank_sizing.py --diameter 10 --height 8
    python tank_sizing.py --target-volume 500 --assume-height 6
    python tank_sizing.py --target-volume 200 --assume-diameter 4

You can also pass a JSON or YAML inputs file via --inputs (supports YAML when PyYAML is installed).
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
class TankSizingInputs:
    diameter: Optional[float] = None  # m
    height: Optional[float] = None  # m
    target_volume: Optional[float] = None  # m³
    assume_diameter: Optional[float] = None  # m (for sizing height)
    assume_height: Optional[float] = None  # m (for sizing diameter)
    product_density: float = 1000.0  # kg/m³ default (water)


def volume_cylinder(diameter: float, height: float) -> float:
    """Compute cylinder volume (m³) from diameter (m) and height (m)."""
    radius = diameter / 2.0
    return math.pi * radius * radius * height


def diameter_for_volume(volume_m3: float, height_m: float) -> float:
    """Compute required diameter (m) for a given volume (m³) and height (m)."""
    radius_sq = volume_m3 / (math.pi * height_m)
    if radius_sq < 0:
        raise ValueError("Computed negative radius squared")
    return 2.0 * math.sqrt(radius_sq)


def height_for_volume(volume_m3: float, diameter_m: float) -> float:
    """Compute required height (m) for a given volume (m³) and diameter (m)."""
    area = math.pi * (diameter_m / 2.0) ** 2
    return volume_m3 / area


def area_shell(diameter: float, height: float) -> float:
    """Shell lateral surface area: A = π D H"""
    return math.pi * diameter * height


def area_roof(diameter: float) -> float:
    """Flat roof area: π D² / 4"""
    return math.pi * diameter * diameter / 4.0


def area_bottom(diameter: float, bottom_present: bool = True) -> float:
    if not bottom_present:
        return 0.0
    return math.pi * diameter * diameter / 4.0


def liters_from_m3(volume_m3: float) -> float:
    return volume_m3 * 1000.0


def gallons_from_m3(volume_m3: float) -> float:
    return volume_m3 * 264.172052  # US gallons


def barrels_from_m3(volume_m3: float) -> float:
    return volume_m3 * 6.28981077  # oil barrels


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
    # Load inputs file if provided
    data: Dict = {}
    if getattr(args, 'inputs', None):
        data = parse_inputs_file(args.inputs)

    # overlay CLI args
    def _set_if_provided(name: str, argname: Optional[str] = None):
        if argname is None:
            argname = name
        val = getattr(args, argname, None)
        if val is not None:
            data[name] = val

    for name in ('diameter', 'height', 'target_volume', 'assume_diameter', 'assume_height', 'product_density'):
        _set_if_provided(name)

    # Build inputs dataclass
    inputs = TankSizingInputs(
        diameter=data.get('diameter'),
        height=data.get('height'),
        target_volume=data.get('target_volume'),
        assume_diameter=data.get('assume_diameter'),
        assume_height=data.get('assume_height'),
        product_density=float(data.get('product_density', 1000.0)),
    )

    result: Dict[str, float] = {}

    # If diameter and height provided -> compute volume
    if inputs.diameter and inputs.height:
        vol = volume_cylinder(inputs.diameter, inputs.height)
        result['volume_m3'] = vol
        result['volume_liters'] = liters_from_m3(vol)
        result['volume_gal_us'] = gallons_from_m3(vol)
        result['volume_barrels'] = barrels_from_m3(vol)
        result['shell_area_m2'] = area_shell(inputs.diameter, inputs.height)
        result['roof_area_m2'] = area_roof(inputs.diameter)
        result['bottom_area_m2'] = area_bottom(inputs.diameter, True)
        result['mass_kg'] = vol * inputs.product_density
        return result

    # If target_volume provided with an assumed dimension -> compute the missing dimension
    if inputs.target_volume is not None:
        if inputs.assume_height is not None:
            d = diameter_for_volume(inputs.target_volume, inputs.assume_height)
            h = inputs.assume_height
        elif inputs.assume_diameter is not None:
            d = float(inputs.assume_diameter)
            h = height_for_volume(inputs.target_volume, d)
        else:
            raise ValueError("When providing target_volume you must provide either assume_height or assume_diameter to solve for the missing dimension.")
        vol = inputs.target_volume
        result['solution_diameter_m'] = d
        result['solution_height_m'] = h
        result['volume_m3'] = vol
        result['shell_area_m2'] = area_shell(d, h)
        result['roof_area_m2'] = area_roof(d)
        result['bottom_area_m2'] = area_bottom(d, True)
        result['mass_kg'] = vol * inputs.product_density
        return result

    raise ValueError('Insufficient inputs: provide diameter+height OR target_volume+assume_height/assume_diameter')


def print_results(results: Dict[str, float]):
    print("Tank sizing results:")
    for k, v in results.items():
        if isinstance(v, float):
            print(f" - {k}: {v:.6g}")
        else:
            print(f" - {k}: {v}")


def main(argv: Optional[list] = None):
    parser = argparse.ArgumentParser(description='Tank Sizing Calculator')
    parser.add_argument('--inputs', help='JSON or YAML inputs file', default=None)
    parser.add_argument('--diameter', type=float, help='Tank diameter (m)')
    parser.add_argument('--height', type=float, help='Liquid height / shell height (m)')
    parser.add_argument('--target-volume', dest='target_volume', type=float, help='Target volume (m³)')
    parser.add_argument('--assume-diameter', dest='assume_diameter', type=float, help='Assumed diameter (m) when solving for height')
    parser.add_argument('--assume-height', dest='assume_height', type=float, help='Assumed height (m) when solving for diameter')
    parser.add_argument('--product-density', dest='product_density', type=float, help='Product density (kg/m³)')

    args = parser.parse_args(argv)
    try:
        results = compute_from_args(args)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        parser.print_help()
        sys.exit(2)

    print_results(results)


if __name__ == '__main__':
    main()
