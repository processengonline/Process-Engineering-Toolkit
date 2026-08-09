"""breather_valve.py

Simple utilities to help size a breather (relief/breather) valve orifice.

This file includes:
- orifice_area_liquid: For incompressible (liquid) flow using standard orifice equation.
- diameter_from_area: Convert area to diameter (assumes circular orifice).
- area_for_choked_gas_mass_flow: Approximate choked (sonic) flow area for ideal gases.

Notes / limitations:
- The liquid function uses A = Q / (C_d * sqrt(2*DeltaP/rho)). This is valid for incompressible flow through an orifice.
- The gas function uses the choked-flow (sonic) ideal-gas formula. It only applies when the downstream-to-upstream pressure ratio is at or below the critical ratio (i.e., flow is choked). If your case is not choked, a more detailed isentropic/subsonic calculation is required.

Author: GitHub Copilot (on user request)
"""

from __future__ import annotations

import math
from typing import Optional

R_UNIVERSAL = 8.314462618  # J/(mol K)


def orifice_area_liquid(Q_m3_s: float, rho_kg_m3: float, deltaP_Pa: float, Cd: float = 0.62) -> float:
    """Calculate required orifice area (m^2) for an incompressible fluid.

    Formula: Q = C_d * A * sqrt(2*DeltaP / rho) -> A = Q / (C_d * sqrt(2*DeltaP / rho))

    Args:
        Q_m3_s: volumetric flow rate in m^3/s
        rho_kg_m3: fluid density in kg/m^3
        deltaP_Pa: pressure drop across orifice in Pascal (Pa)
        Cd: discharge coefficient (typical 0.6-0.8)

    Returns:
        Required orifice area in m^2
    """
    if Q_m3_s <= 0:
        raise ValueError("Q_m3_s must be > 0")
    if rho_kg_m3 <= 0:
        raise ValueError("rho_kg_m3 must be > 0")
    if deltaP_Pa <= 0:
        raise ValueError("deltaP_Pa must be > 0")
    if not (0 < Cd <= 1.5):
        raise ValueError("Cd should be a reasonable positive value (e.g., 0.6)")

    denominator = Cd * math.sqrt(2.0 * deltaP_Pa / rho_kg_m3)
    area_m2 = Q_m3_s / denominator
    return area_m2


def diameter_from_area(area_m2: float) -> float:
    """Convert circular area to diameter in meters.

    Args:
        area_m2: area in square meters
    Returns:
        diameter in meters
    """
    if area_m2 <= 0:
        raise ValueError("area_m2 must be > 0")
    return math.sqrt(4.0 * area_m2 / math.pi)


def area_for_choked_gas_mass_flow(
    m_dot_kg_s: float,
    P0_Pa: float,
    T0_K: float,
    M_kg_per_mol: float = 0.02897,
    gamma: float = 1.4,
    Cd: float = 0.8,
) -> float:
    """Estimate required orifice area (m^2) for a choked (sonic) ideal-gas flow.

    Uses the choked-flow mass flow equation for an ideal gas:
      m_dot = C_d * A * P0 / sqrt(R_specific * T0) * sqrt(gamma) * K
    where K = (2/(gamma+1))^{(gamma+1)/(2*(gamma-1))}

    This formula applies only when the downstream/upstream pressure ratio is <= the critical value
    (i.e., the flow is choked). If your case is not choked, this function is not valid.

    Args:
        m_dot_kg_s: required mass flow rate through the valve (kg/s)
        P0_Pa: upstream total/stagnation pressure in Pa
        T0_K: upstream absolute temperature in K
        M_kg_per_mol: molar mass (kg/mol), default = 0.02897 (air)
        gamma: ratio of specific heats (default air = 1.4)
        Cd: discharge coefficient (typical 0.7-0.95 for sharp-edged orifices)

    Returns:
        area in m^2
    """
    if m_dot_kg_s <= 0:
        raise ValueError("m_dot_kg_s must be > 0")
    if P0_Pa <= 0 or T0_K <= 0:
        raise ValueError("P0_Pa and T0_K must be > 0")

    R_specific = R_UNIVERSAL / M_kg_per_mol  # J/(kg K)
    # Choked flow constant
    K = (2.0 / (gamma + 1.0)) ** ((gamma + 1.0) / (2.0 * (gamma - 1.0)))

    numerator = m_dot_kg_s * math.sqrt(R_specific * T0_K)
    denominator = Cd * P0_Pa * math.sqrt(gamma) * K
    area_m2 = numerator / denominator
    return area_m2


if __name__ == "__main__":
    # Simple demonstration / quick CLI-like usage with example numbers
    print("Breather valve sizing examples:\n")

    # Example 1: Liquid (water) — volumetric flow 0.01 m3/s, density 1000 kg/m3, ΔP = 1000 Pa
    Q = 0.01  # m3/s
    rho = 1000.0  # kg/m3 (water)
    deltaP = 1000.0  # Pa (~0.01 bar)
    Cd_example = 0.62
    area_liq = orifice_area_liquid(Q, rho, deltaP, Cd=Cd_example)
    diam_liq = diameter_from_area(area_liq)
    print(f"Liquid example: Q={Q} m3/s, rho={rho} kg/m3, ΔP={deltaP} Pa, Cd={Cd_example}")
    print(f"  -> area = {area_liq:.6e} m^2 (dia = {diam_liq*1000:.2f} mm)\n")

    # Example 2: Gas (air) choked flow — mass flow 0.5 kg/s, P0=5e5 Pa, T0=293 K
    m_dot = 0.5  # kg/s
    P0 = 5e5  # Pa
    T0 = 293.0  # K
    area_gas = area_for_choked_gas_mass_flow(m_dot, P0, T0, M_kg_per_mol=0.02897, gamma=1.4, Cd=0.8)
    diam_gas = diameter_from_area(area_gas)
    print(f"Gas (choked) example: m_dot={m_dot} kg/s, P0={P0} Pa, T0={T0} K, Cd=0.8")
    print(f"  -> area = {area_gas:.6e} m^2 (dia = {diam_gas*1000:.2f} mm)\n")

    print("Notes:\n - Liquid formula is for incompressible flow through an orifice.\n - Gas formula assumes choked/sonic flow (downstream pressure sufficiently low).")
