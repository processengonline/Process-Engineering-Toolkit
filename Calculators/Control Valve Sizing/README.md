# Control Valve Sizing Tool (ISA 75.01 / IEC 60534)

## Overview

This repository contains a comprehensive **Control Valve Sizing Tool** developed for the preliminary sizing, selection, and performance evaluation of control valves used in oil & gas, LNG, petrochemical, refining, and chemical processing facilities.

The tool automates the engineering calculations typically performed during **FEED**, **Detailed Engineering**, revamp studies, and plant troubleshooting by implementing internationally recognized sizing methodologies from **ISA 75.01** and **IEC 60534**.

It calculates the required valve flow coefficient (**Cv/Kv**), evaluates valve operating conditions, verifies hydraulic performance, and assists in selecting an appropriate valve size and trim configuration.

The project is available as both a **spreadsheet-based engineering calculator** and a **Python implementation** for engineering automation.

---

# Engineering Objectives

The primary objectives of this tool are to:

- Calculate the required **Cv** or **Kv** for liquid, gas, and steam applications.
- Size control valves in accordance with ISA and IEC standards.
- Evaluate valve performance under minimum, normal, and maximum operating conditions.
- Verify valve operation within the recommended travel range.
- Assess cavitation, flashing, choked flow, and aerodynamic noise.
- Assist engineers in selecting the optimum valve body and trim size.
- Improve consistency, transparency, and repeatability of engineering calculations.

---

# Applicable Standards & References

The sizing methodology follows internationally accepted engineering standards:

- ISA 75.01 – Flow Equations for Sizing Control Valves
- IEC 60534 Series – Industrial Process Control Valves
- Fisher Control Valve Handbook
- Masoneilan Control Valve Handbook
- Crane Technical Paper No. 410
- Perry's Chemical Engineers' Handbook
- GPSA Engineering Data Book
- Project and Company Engineering Standards (where applicable)

---

# Features

## Liquid Valve Sizing

- Liquid Cv calculation
- Pressure recovery factor (FL)
- Reynolds number correction
- Viscosity correction
- Choked flow verification
- Cavitation assessment
- Flashing evaluation

---

## Gas & Steam Valve Sizing

- Compressible flow sizing
- Expansion factor (Y)
- Pressure drop ratio (x)
- Critical pressure ratio (xT)
- Choked flow verification
- Compressibility correction
- Gas velocity evaluation

---

## Valve Selection

- Required Cv/Kv determination
- Valve body sizing
- Trim selection
- Valve travel estimation
- Installed versus required Cv comparison
- Capacity margin calculation

---

## Performance Verification

- Velocity checks
- Cavitation index
- Flashing verification
- Noise prediction
- Operating range evaluation
- Valve authority assessment

---

# Required Inputs

## Process Conditions

- Fluid type (Liquid / Gas / Steam)
- Operating pressure
- Operating temperature
- Minimum flow rate
- Normal flow rate
- Maximum flow rate

---

## Fluid Properties

### Liquids

- Density
- Specific gravity
- Dynamic viscosity
- Vapor pressure

### Gas / Steam

- Molecular weight
- Density
- Compressibility factor (Z)
- Ratio of specific heats (k)

---

## Valve Data

- Valve type
- Flow characteristic
- Valve style
- Trim type
- Pressure class
- Line size
- Pipe schedule

---

## Design Constraints

- Maximum allowable velocity
- Maximum allowable noise level
- Cavitation limit
- Flashing limit
- Required valve travel
- Pressure recovery factor
- Pipe geometry correction factors

---

# Engineering Methodology

The sizing calculation follows the engineering workflow below:

1. Define the process operating conditions.
2. Calculate the required pressure drop across the valve.
3. Select the appropriate ISA/IEC sizing equation.
4. Calculate the required valve coefficient (Cv/Kv).
5. Apply correction factors:
   - Reynolds number correction
   - Pipe geometry factor
   - Pressure recovery factor
   - Expansion factor
6. Verify choked flow conditions.
7. Evaluate cavitation and flashing potential.
8. Estimate valve operating travel.
9. Select the smallest valve satisfying all design criteria.
10. Generate a valve sizing report.

---

# Governing Equations

## Liquid Service

### Standard Equation

```text
Cv = Q × √(SG / ΔP)
```

Where:

| Symbol | Description | Units |
|---------|-------------|------|
| Cv | Valve flow coefficient | — |
| Q | Liquid flow rate | gpm |
| SG | Specific gravity | — |
| ΔP | Pressure drop | psi |

---

## Gas & Steam Service

### ISA Compressible Flow Equation

```text
Cv = Q / [N9 × FP × Y × √((x × P1 × ρ1) / SG)]
```

Where:

| Symbol | Description |
|---------|-------------|
| Cv | Valve flow coefficient |
| FP | Pipe geometry factor |
| Y | Expansion factor |
| x | Pressure drop ratio |
| P₁ | Upstream pressure |
| ρ₁ | Upstream density |
| SG | Specific gravity |

---

## Additional Engineering Corrections

The sizing methodology incorporates the following correction factors where applicable:

- Pipe Geometry Factor (FP)
- Reynolds Number Factor (FR)
- Pressure Recovery Factor (FL)
- Expansion Factor (Y)
- Critical Pressure Ratio (xT)
- Choked Flow Correction
- Compressibility Factor (Z)

---

# Spreadsheet Structure

| Worksheet | Description |
|------------|-------------|
| **Inputs** | Operating conditions, fluid properties, valve data |
| **Liquid_Cv** | Liquid valve sizing calculations |
| **Gas_Steam_Cv** | Gas and steam sizing calculations |
| **Checks** | Cavitation, flashing, velocity, and noise evaluation |
| **Summary** | Final valve selection and engineering recommendations |

---

# Repository Structure

```text
Control-Valve-Sizing/
│
├── README.md
├── valve_sizing.xlsx
├── control_valve_sizing.py
├── inputs.yaml
│
├── spreadsheets/
│   └── control_valve_sizing.xlsx
│
├── examples/
│   ├── liquid_case.yaml
│   ├── gas_case.yaml
│   ├── steam_case.yaml
│   └── sample_results.md
│
├── results/
│   ├── sizing_report.pdf
│   ├── sizing_summary.xlsx
│   └── valve_selection.csv
│
├── utils/
│   ├── liquid.py
│   ├── gas.py
│   ├── corrections.py
│   ├── valve_selection.py
│   └── validation.py
│
└── docs/
    ├── methodology.md
    ├── equations.md
    ├── assumptions.md
    └── references.md
```

---

# Engineering Skills Demonstrated

- Control Valve Sizing
- Process Hydraulics
- Process Engineering
- Instrumentation Engineering
- ISA 75.01
- IEC 60534
- Engineering Calculations
- Process Design
- Python for Engineering
- Engineering Automation
- Oil & Gas Process Design
- EPC Detailed Engineering

---

# Project Value

This project demonstrates how conventional control valve sizing spreadsheets can be transformed into a structured engineering software tool that improves calculation accuracy, standardization, transparency, and engineering productivity.

It showcases the integration of:

- Process Engineering
- Fluid Mechanics
- Instrumentation Engineering
- Digital Engineering
- Python Programming
- Engineering Automation
- Engineering Best Practices

---

# Disclaimer

This tool is intended for educational, portfolio, and preliminary engineering purposes only. Final control valve sizing should always be verified using approved vendor sizing software, project specifications, applicable standards, and sound engineering judgment.
