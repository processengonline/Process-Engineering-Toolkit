# Pipeline Hydraulic Calculator (Single-Phase & Two-Phase Flow)

**Script:** [`line_hydraulics.py`](./line_hydraulics.py) · **Sample output:** [`sample_report_output.txt`](./sample_report_output.txt)

```bash
python line_hydraulics.py --help
```

## Overview

This repository contains a Python-based **Pipeline Hydraulic Calculator** developed for preliminary hydraulic analysis and pressure drop calculations in process piping systems. The tool automates calculations commonly performed during FEED, Detailed Engineering, debottlenecking studies, and plant troubleshooting.

The calculator evaluates pressure losses due to friction, elevation changes, and piping components while verifying flow velocity and hydraulic performance against engineering design criteria.

The current version supports **single-phase liquid flow** with a modular framework for future implementation of **gas** and **two-phase flow** models.

---

# Engineering Objectives

The calculator enables process engineers to:

- Calculate pressure drop in process pipelines
- Determine fluid velocity and Reynolds number
- Calculate friction factor using the Swamee–Jain correlation
- Evaluate pressure losses due to fittings and valves
- Account for static head caused by elevation changes
- Verify compliance with allowable pressure drop limits
- Assist in pipeline sizing and hydraulic verification

---

# Applicable Standards & References

The hydraulic methodology is based on industry-recognized references, including:

- Darcy–Weisbach Equation
- Swamee–Jain Friction Factor Correlation
- Crane Technical Paper No. 410
- GPSA Engineering Data Book
- Perry's Chemical Engineers' Handbook
- ASME B31.3 Process Piping
- Company Engineering Standards (where applicable)

---

# Features

### Single-Phase Liquid Flow

- Velocity calculation
- Reynolds number determination
- Laminar and turbulent flow identification
- Darcy friction factor calculation
- Frictional pressure loss
- Static head calculation
- Minor loss calculation (fittings, valves, bends)
- Total pressure drop calculation

### Future Gas Flow Module

- Compressible gas hydraulics
- Isothermal pressure drop
- Weymouth equation
- Panhandle A/B equations
- Darcy-Weisbach for gases

### Future Two-Phase Module

- Lockhart-Martinelli Method
- Beggs & Brill Correlation
- Homogeneous Flow Model
- Flow regime estimation
- Two-phase pressure drop

---

# Repository Structure

```text
Pipeline-Hydraulic-Calculator/
│
├── README.md
├── hydraulic_calculator.py
├── inputs.yaml
│
├── examples/
│   ├── liquid_pipeline.yaml
│   ├── gas_pipeline.yaml
│   ├── two_phase_pipeline.yaml
│   └── sample_results.md
│
├── results/
│   ├── hydraulic_report.txt
│   └── pressure_drop_summary.csv
│
├── utils/
│   ├── fluid_properties.py
│   ├── friction.py
│   ├── fittings.py
│   ├── hydraulics.py
│   └── validation.py
│
└── docs/
    ├── methodology.md
    ├── equations.md
    ├── assumptions.md
    └── references.md
```

---

# Required Inputs

## Process Conditions

- Fluid phase
- Flow rate
- Operating pressure
- Operating temperature

## Fluid Properties

- Density (ρ)
- Dynamic viscosity (μ)
- Compressibility factor (gas)
- Molecular weight (gas)

## Pipeline Data

- Internal diameter
- Pipe length
- Pipe roughness
- Elevation difference
- Pipe material

## Hydraulic Components

- Valves
- Elbows
- Reducers
- Tees
- Control valves
- Equipment nozzles

## Design Constraints

- Maximum allowable velocity
- Maximum allowable pressure drop
- Design flow rate

---

# Engineering Methodology

The hydraulic calculation follows the workflow below:

1. Read operating conditions and pipeline geometry.
2. Calculate fluid velocity.
3. Determine Reynolds number.
4. Calculate Darcy friction factor.
5. Compute frictional pressure loss.
6. Calculate static head due to elevation.
7. Calculate minor losses from fittings and valves.
8. Sum all pressure losses.
9. Verify hydraulic performance against design criteria.
10. Generate an engineering report.

---

# Governing Equations

## 1. Fluid Velocity

The average fluid velocity is calculated as:

\[
v = \frac{4Q}{\pi D^{2}}
\]

where:

- **v** = Fluid velocity (m/s)
- **Q** = Volumetric flow rate (m³/s)
- **D** = Internal pipe diameter (m)

---

## 2. Reynolds Number

\[
Re = \frac{\rho v D}{\mu}
\]

where:

- **ρ** = Fluid density (kg/m³)
- **μ** = Dynamic viscosity (Pa·s)

Flow regime:

- Laminar: Re < 2,300
- Transitional: 2,300–4,000
- Turbulent: Re > 4,000

---

## 3. Darcy Friction Factor (Swamee–Jain)

For turbulent flow:

\[
f =
\frac{0.25}
{\left[
\log_{10}
\left(
\frac{\varepsilon}{3.7D}
+
\frac{5.74}{Re^{0.9}}
\right)
\right]^2}
\]

where:

- **ε** = Pipe roughness
- **D** = Pipe diameter

---

## 4. Frictional Pressure Drop

Using the Darcy–Weisbach equation:

\[
\Delta P_f
=
f
\frac{L}{D}
\left(
\frac{\rho v^2}{2}
\right)
\]

where:

- **L** = Pipe length

---

## 5. Static Pressure Loss

\[
\Delta P_{static}
=
\rho g \Delta z
\]

where:

- **g** = Gravitational acceleration
- **Δz** = Elevation difference

---

## 6. Minor Losses

Pressure losses across fittings are calculated using:

\[
\Delta P_{minor}
=
\sum K
\left(
\frac{\rho v^2}{2}
\right)
\]

where:

- **K** = Loss coefficient

---

## 7. Total Pressure Drop

\[
\Delta P_{total}
=
\Delta P_f
+
\Delta P_{static}
+
\Delta P_{minor}
\]

---

# Example Output

```text
-----------------------------------------
PIPELINE HYDRAULIC REPORT
-----------------------------------------

Fluid                 : Water

Flow Rate             : 120 m³/hr

Pipe Diameter         : 150 mm

Pipe Length           : 850 m

Velocity              : 1.89 m/s

Reynolds Number       : 3.9 × 10⁵

Flow Regime           : Turbulent

Friction Factor       : 0.018

Friction Loss         : 58.2 kPa

Static Head           : 21.5 kPa

Minor Losses          : 8.3 kPa

-----------------------------------------

Total Pressure Drop   : 88.0 kPa

Hydraulic Status      : PASS
```

---

# Future Enhancements

Future versions will include:

- Compressible gas hydraulics
- Two-phase pressure drop models
- Pump system calculations
- NPSH available calculations
- Pipeline sizing optimization
- Line sizing recommendations
- Pipe schedule selection
- Heat transfer calculations
- Erosion velocity verification (API RP 14E)
- Excel report generation
- PDF calculation reports
- Interactive Streamlit dashboard

---

# Engineering Skills Demonstrated

- Process Hydraulics
- Pipeline Design
- Pressure Drop Calculations
- Process Engineering
- Oil & Gas Facilities
- Python for Engineering
- Hydraulic Modeling
- Engineering Automation
- FEED & Detailed Engineering
- Plant Troubleshooting

---

# Project Value

This project demonstrates how traditional hydraulic design spreadsheets can be transformed into a modular Python application that improves calculation consistency, engineering transparency, and workflow automation.

It highlights the integration of:

- Process Engineering
- Fluid Mechanics
- Pipeline Design
- Digital Engineering
- Python Programming
- Engineering Automation

---

# Disclaimer

This calculator is intended for educational, portfolio, and preliminary engineering purposes only. Final hydraulic design should be verified against project specifications, applicable design codes, client standards, and detailed engineering calculations.

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
