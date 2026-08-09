# Pump Hydraulics Calculation

**Script:** [`pump_hydraulics.py`](./pump_hydraulics.py) · **Sample output:** [`sample_report_output.txt`](./sample_report_output.txt)

```bash
python pump_hydraulics.py --help
```

## Overview

This repository contains a comprehensive **Pump Hydraulics Calculation Tool** developed for the hydraulic design, analysis, and selection of centrifugal pumps used in **oil & gas**, **LNG**, **petrochemical**, **refining**, **chemical**, and **water treatment** facilities.

The tool automates the hydraulic calculations traditionally performed using engineering spreadsheets and provides a structured methodology for evaluating pumping systems during **Conceptual Design**, **FEED**, **Detailed Engineering**, **Plant Revamps**, and **Troubleshooting Studies**.

It calculates the **Total Dynamic Head (TDH)**, determines the **Net Positive Suction Head Available (NPSHa)**, evaluates friction losses in suction and discharge piping, estimates hydraulic and shaft power requirements, and assists in selecting a suitable pump operating near its **Best Efficiency Point (BEP)**.

The project is available as both an **Excel-based engineering calculator** and a **Python implementation**, allowing engineers to automate repetitive calculations while maintaining complete engineering transparency.

---

# Engineering Objectives

The primary objectives of this project are to:

- Calculate the Total Dynamic Head (TDH) required by the pumping system.
- Evaluate suction and discharge piping hydraulics.
- Determine Net Positive Suction Head Available (NPSHa).
- Compare NPSHa against manufacturer NPSH Required (NPSHr).
- Estimate hydraulic, shaft, and motor power.
- Generate system head curves for pump selection.
- Verify operating conditions against hydraulic design criteria.
- Support preliminary pump sizing and equipment selection.

---

# Applicable Standards & References

The calculation methodology is based on internationally recognized engineering standards and design references, including:

- Hydraulic Institute (HI) Standards
- ANSI/HI Pump Standards
- Crane Technical Paper No. 410 – Flow of Fluids
- Perry's Chemical Engineers' Handbook
- GPSA Engineering Data Book
- API 610 – Centrifugal Pumps for Petroleum, Petrochemical and Natural Gas Industries
- Company Engineering Standards (where applicable)

---

# Features

## Hydraulic Calculations

- Total Dynamic Head (TDH)
- Static Head
- Friction Head Loss
- Minor Losses
- Suction Line Analysis
- Discharge Line Analysis
- Velocity Calculations
- Reynolds Number
- Darcy Friction Factor

---

## NPSH Analysis

- NPSH Available (NPSHa)
- NPSH Margin Verification
- Vapor Pressure Correction
- Suction Pressure Analysis
- Cavitation Risk Assessment

---

## Pump Performance

- Hydraulic Power
- Shaft Power
- Motor Power
- Pump Efficiency
- Best Efficiency Point (BEP) Evaluation
- System Curve Generation
- Operating Point Verification

---

## Engineering Verification

- Velocity checks
- Suction velocity verification
- Discharge velocity verification
- Pressure drop verification
- Cavitation assessment
- Pump operating range verification

---

# Required Inputs

## Process Conditions

- Flow rate
- Operating temperature
- Fluid phase
- Required discharge pressure
- Suction source conditions

---

## Fluid Properties

- Density (ρ)
- Dynamic viscosity (μ)
- Vapor pressure
- Specific gravity

---

## Suction System

- Vessel or tank pressure
- Liquid level
- Pump centerline elevation
- Suction pipe diameter
- Pipe length
- Pipe roughness
- Fittings and valves

---

## Discharge System

- Destination pressure
- Elevation
- Pipe diameter
- Pipe length
- Pipe roughness
- Fittings
- Control valves

---

## Pump Data

- Pump efficiency
- Motor efficiency
- Manufacturer pump curve
- NPSH Required (NPSHr)

---

# Engineering Methodology

The calculation follows the standard hydraulic design workflow:

1. Read process operating conditions.
2. Calculate flow velocity.
3. Determine Reynolds number.
4. Calculate Darcy friction factor.
5. Calculate suction-side pressure losses.
6. Calculate discharge-side pressure losses.
7. Calculate static head.
8. Determine Total Dynamic Head (TDH).
9. Calculate Net Positive Suction Head Available (NPSHa).
10. Verify NPSHa against manufacturer NPSHr.
11. Estimate hydraulic, shaft, and motor power.
12. Generate the system curve.
13. Select the appropriate pump based on the operating point and efficiency.

---

# Governing Equations

## 1. Flow Velocity

### Mathematical Expression

\[
v=\frac{4Q}{\pi D^2}
\]

### GitHub Format

```text
v = 4Q / (πD²)
```

| Parameter | Description | Units |
|-----------|-------------|-------|
| v | Fluid velocity | m/s |
| Q | Volumetric flow rate | m³/s |
| D | Pipe internal diameter | m |

---

## 2. Reynolds Number

### Mathematical Expression

\[
Re=\frac{\rho vD}{\mu}
\]

### GitHub Format

```text
Re = (ρ × v × D) / μ
```

---

## 3. Darcy Friction Factor

Using the Swamee–Jain correlation:

### Mathematical Expression

\[
f=\frac{0.25}
{\left[\log_{10}\left(\frac{\varepsilon}{3.7D}+\frac{5.74}{Re^{0.9}}\right)\right]^2}
\]

### GitHub Format

```text
f = 0.25 / [log10((ε / 3.7D) + (5.74 / Re^0.9))]²
```

---

## 4. Friction Head Loss

### Mathematical Expression

\[
h_f=f\frac{L}{D}\frac{v^2}{2g}
\]

### GitHub Format

```text
hf = f × (L / D) × (v² / 2g)
```

---

## 5. Minor Head Losses

### Mathematical Expression

\[
h_m=\sum K\frac{v^2}{2g}
\]

### GitHub Format

```text
hm = ΣK × (v² / 2g)
```

---

## 6. Total Dynamic Head (TDH)

The total head developed by the pump is calculated as:

### Mathematical Expression

\[
TDH=\frac{P_d-P_s}{\rho g}+(z_d-z_s)+h_{f,s}+h_{f,d}+h_m
\]

### GitHub Format

```text
TDH = (Pd − Ps)/(ρg)
    + (Zd − Zs)
    + hf,suction
    + hf,discharge
    + hm
```

---

## 7. Net Positive Suction Head Available (NPSHa)

### Mathematical Expression

\[
NPSH_a=\frac{P_{source}-P_v}{\rho g}+(z_{source}-z_{pump})-h_{f,suction}
\]

### GitHub Format

```text
NPSHa = (Psource − Pv)/(ρg)
       + (Zsource − Zpump)
       − hf,suction
```

### Design Requirement

```text
NPSHa ≥ NPSHr + Safety Margin
```

---

## 8. Hydraulic Power

### Mathematical Expression

\[
P_h=\rho gQH
\]

### GitHub Format

```text
Ph = ρ × g × Q × TDH
```

---

## 9. Shaft Power

### Mathematical Expression

\[
P_{shaft}=\frac{P_h}{\eta_p}
\]

### GitHub Format

```text
Pshaft = Ph / ηpump
```

---

## 10. Motor Power

### Mathematical Expression

\[
P_{motor}=\frac{P_{shaft}}{\eta_m}
\]

### GitHub Format

```text
Pmotor = Pshaft / ηmotor
```

---

# Spreadsheet Structure

| Worksheet | Description |
|------------|-------------|
| **Inputs** | Process conditions, fluid properties, piping data, pump information |
| **Suction_Losses** | Velocity, Reynolds number, friction losses, suction-side pressure drop, NPSHa |
| **Discharge_Losses** | Discharge-side friction losses and static head calculations |
| **System_Curve** | System head calculations over varying flow rates with graphical representation |
| **Pump_Selection** | Pump curve comparison, BEP verification, efficiency evaluation, power calculations |
| **Summary** | Selected pump, operating point, TDH, NPSH margin, hydraulic power, shaft power, motor recommendation |

---

# Repository Structure

```text
Pump-Hydraulics-Calculation/
│
├── README.md
├── pump_hydraulics.py
├── inputs.yaml
│
├── spreadsheets/
│   └── pump_hydraulics.xlsx
│
├── examples/
│   ├── cooling_water.yaml
│   ├── condensate_transfer.yaml
│   ├── crude_oil_transfer.yaml
│   ├── boiler_feed_water.yaml
│   └── sample_results.md
│
├── results/
│   ├── hydraulic_report.pdf
│   ├── pump_selection.xlsx
│   └── system_curve.csv
│
├── utils/
│   ├── hydraulics.py
│   ├── friction.py
│   ├── npsh.py
│   ├── pump_selection.py
│   ├── power.py
│   └── validation.py
│
└── docs/
    ├── methodology.md
    ├── equations.md
    ├── assumptions.md
    └── references.md
```

---

# Typical Applications

The tool can be used for hydraulic analysis and pump selection in:

- Crude Oil Transfer Systems
- Condensate Transfer Pumps
- Cooling Water Networks
- Fire Water Systems
- Boiler Feed Water Systems
- Process Water Distribution
- Chemical Transfer Systems
- LNG and Gas Processing Facilities
- Utility Services
- Tank Loading and Unloading Systems

---

# Engineering Skills Demonstrated

- Pump Hydraulic Design
- Pump Selection
- NPSH Analysis
- Process Hydraulics
- Fluid Mechanics
- Pipeline Design
- API 610
- Hydraulic Institute Standards
- Engineering Calculations
- Python for Process Engineering
- Engineering Automation
- EPC Detailed Engineering

---

# Project Value

This project demonstrates how traditional hydraulic design spreadsheets can be transformed into a modular engineering software application, improving calculation accuracy, consistency, traceability, and engineering productivity.

It showcases the integration of:

- Process Engineering
- Pump Hydraulics
- Fluid Mechanics
- Pipeline Design
- Equipment Selection
- Digital Engineering
- Python Programming
- Engineering Automation

---

# Future Enhancements

Planned improvements include:

- Pump affinity law calculations
- Variable Speed Drive (VSD) analysis
- Parallel and series pump configurations
- Pump curve digitization
- Automatic BEP identification
- Pipe sizing recommendations
- Energy consumption estimation
- Life Cycle Cost (LCC) analysis
- Excel and PDF report generation
- Interactive Streamlit dashboard

---

# Disclaimer

This tool is intended for educational, portfolio, and preliminary engineering purposes only. Final pump selection and hydraulic design should always be verified using manufacturer pump curves, project specifications, applicable engineering standards, and sound engineering judgment.

---

# Author

**Shubham**

**Process Engineer**

Specializations:

- Pump Hydraulics & Equipment Design
- Process Hydraulics
- Aspen HYSYS & Honeywell UniSim
- LNG, GTL & Gas Processing
- EPC Detailed Engineering
- Process Optimization
- Python-Based Engineering Automation
```
