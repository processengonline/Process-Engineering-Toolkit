# Tank Heat Loss Calculation Tool

**Script:** [`tank_heat_loss.py`](./tank_heat_loss.py) · **Sample output:** [`sample_report_output.txt`](./sample_report_output.txt)

```bash
python tank_heat_loss.py --help
```

## Overview

This repository contains a comprehensive **Tank Heat Loss Calculation Tool** developed for estimating steady-state heat losses from **atmospheric** and **low-pressure storage tanks** used in oil & gas, LNG, petrochemical, refinery, chemical, and utility facilities.

The tool automates thermal calculations traditionally performed using engineering spreadsheets and provides a systematic methodology for estimating heat losses from the **tank shell**, **roof**, and **bottom**, enabling engineers to evaluate insulation performance, determine heating requirements, and optimize operating costs.

The calculator supports insulated and uninsulated vertical cylindrical storage tanks and assists process engineers during **Conceptual Design**, **FEED**, **Detailed Engineering**, **Brownfield Modifications**, and **Plant Troubleshooting**.

The project is available as both an **Excel-based engineering calculator** and a **Python implementation**, providing transparent engineering calculations and opportunities for workflow automation.

---

# Engineering Objectives

The primary objectives of this project are to:

- Estimate steady-state heat loss from storage tanks.
- Calculate heat losses through the shell, roof, and bottom.
- Determine the overall heat transfer coefficient (U-value).
- Evaluate insulation performance for different insulation materials and thicknesses.
- Estimate required heating duty to maintain product temperature.
- Compare insulation alternatives for energy optimization.
- Support insulation specification during engineering design.
- Generate engineering documentation suitable for thermal design calculations.

---

# Applicable Standards & References

The calculation methodology follows internationally recognized engineering references, including:

- ASHRAE Handbook – Fundamentals
- API 2000 – Venting Atmospheric and Low-Pressure Storage Tanks
- API 650 – Welded Tanks for Oil Storage
- API 620 – Design and Construction of Large Welded Low-Pressure Storage Tanks
- Perry's Chemical Engineers' Handbook
- GPSA Engineering Data Book
- Incropera & DeWitt – Fundamentals of Heat and Mass Transfer
- Company Engineering Standards (where applicable)

---

# Features

## Heat Transfer Calculations

- Overall Heat Transfer Coefficient (U-value)
- Conduction through insulation
- Internal convection resistance
- External convection resistance
- Steady-state heat transfer

---

## Heat Loss Estimation

- Tank shell heat loss
- Roof heat loss
- Bottom heat loss
- Total heat loss
- Heat loss per unit area
- Daily energy loss estimation

---

## Insulation Analysis

- Insulation thickness evaluation
- Thermal conductivity comparison
- U-value optimization
- Surface temperature estimation
- Heat loss reduction analysis

---

## Heating Requirement Assessment

- Heater duty estimation
- Steam tracing assessment
- Electric heat tracing evaluation
- Heating coil sizing support
- Energy consumption estimation

---

## Engineering Verification

- Insulation adequacy check
- Surface temperature verification
- Energy loss assessment
- Operating temperature maintenance
- Thermal performance comparison

---

# Required Inputs

## Tank Geometry

- Tank diameter
- Tank shell height
- Liquid level
- Roof type
- Tank orientation

---

## Process Conditions

- Product temperature
- Ambient temperature
- Wind velocity (optional)
- Design temperature
- Operating temperature

---

## Fluid Properties

- Density
- Specific heat capacity
- Thermal conductivity
- Product classification

---

## Insulation Properties

- Insulation material
- Insulation thickness
- Thermal conductivity
- External cladding thickness
- Cladding material

---

## Heat Transfer Parameters

- Internal heat transfer coefficient
- External heat transfer coefficient
- Surface emissivity (optional)
- Radiation effects (future enhancement)

---

# Engineering Methodology

The calculation follows a standard heat transfer analysis workflow:

1. Define tank geometry and operating conditions.
2. Calculate shell, roof, and bottom surface areas.
3. Determine thermal resistances.
4. Calculate overall heat transfer coefficient (U-value).
5. Calculate shell heat loss.
6. Calculate roof heat loss.
7. Calculate bottom heat loss.
8. Sum all heat losses.
9. Estimate required heating duty.
10. Evaluate insulation performance.
11. Generate a thermal design report.

---

# Governing Equations

## 1. Overall Heat Transfer Coefficient (U-Value)

### Mathematical Expression

\[
\frac{1}{U}=\frac{1}{h_i}+\frac{t_{ins}}{k_{ins}}+\frac{1}{h_o}
\]

### GitHub Format

```text
1/U = (1/hi) + (tins / kins) + (1/ho)
```

Where:

| Parameter | Description | Units |
|-----------|-------------|-------|
| U | Overall heat transfer coefficient | W/m²·K |
| hi | Internal heat transfer coefficient | W/m²·K |
| ho | External heat transfer coefficient | W/m²·K |
| tins | Insulation thickness | m |
| kins | Insulation thermal conductivity | W/m·K |

---

## 2. Shell Surface Area

### Mathematical Expression

\[
A_{shell}=\pi D H
\]

### GitHub Format

```text
Ashell = π × D × H
```

Where:

| Parameter | Description | Units |
|-----------|-------------|-------|
| D | Tank diameter | m |
| H | Liquid height | m |

---

## 3. Roof Surface Area

### Mathematical Expression

\[
A_{roof}=\frac{\pi D^2}{4}
\]

### GitHub Format

```text
Aroof = (π × D²) / 4
```

---

## 4. Bottom Surface Area

For flat-bottom tanks:

### GitHub Format

```text
Abottom = (π × D²) / 4
```

---

## 5. Shell Heat Loss

### Mathematical Expression

\[
Q_{shell}=U\times A_{shell}\times(T_f-T_a)
\]

### GitHub Format

```text
Qshell = U × Ashell × (Tf − Ta)
```

Where:

| Parameter | Description | Units |
|-----------|-------------|-------|
| Qshell | Shell heat loss | W |
| Tf | Product temperature | °C |
| Ta | Ambient temperature | °C |

---

## 6. Roof Heat Loss

### Mathematical Expression

\[
Q_{roof}=U_{roof}\times A_{roof}\times(T_f-T_a)
\]

### GitHub Format

```text
Qroof = Uroof × Aroof × (Tf − Ta)
```

---

## 7. Bottom Heat Loss

### Mathematical Expression

\[
Q_{bottom}=U_{bottom}\times A_{bottom}\times(T_f-T_a)
\]

### GitHub Format

```text
Qbottom = Ubottom × Abottom × (Tf − Ta)
```

---

## 8. Total Heat Loss

### Mathematical Expression

\[
Q_{total}=Q_{shell}+Q_{roof}+Q_{bottom}
\]

### GitHub Format

```text
Qtotal = Qshell + Qroof + Qbottom
```

---

## 9. Specific Heat Loss

```text
Heat Loss per Unit Area = Qtotal / Atotal
```

---

## 10. Heating Duty

When maintaining product temperature:

```text
Heating Duty = Qtotal × Design Safety Factor
```

Typical design safety factor:

- 1.10–1.25

---

## 11. Daily Energy Loss

```text
Energy Loss = Qtotal × 24 hr
```

---

# Spreadsheet Structure

| Worksheet | Description |
|------------|-------------|
| **Inputs** | Tank geometry, operating conditions, insulation properties, heat transfer coefficients |
| **Surface_Areas** | Calculation of shell, roof, and bottom heat transfer areas |
| **U_Value** | Thermal resistance calculations and overall heat transfer coefficients |
| **Heat_Loss** | Shell, roof, bottom, and total heat loss calculations |
| **Heating_Duty** | Heater duty estimation and insulation comparison |
| **Summary** | Total heat loss, U-values, energy consumption, engineering recommendations |

---

# Repository Structure

```text
Tank-Heat-Loss-Calculator/
│
├── README.md
├── tank_heat_loss.py
├── inputs.yaml
│
├── spreadsheets/
│   └── tank_heat_loss.xlsx
│
├── examples/
│   ├── crude_oil_storage.yaml
│   ├── diesel_storage.yaml
│   ├── condensate_storage.yaml
│   ├── bitumen_storage.yaml
│   ├── methanol_storage.yaml
│   └── sample_results.md
│
├── results/
│   ├── thermal_report.pdf
│   ├── heat_loss_summary.xlsx
│   └── insulation_comparison.csv
│
├── utils/
│   ├── heat_transfer.py
│   ├── insulation.py
│   ├── geometry.py
│   ├── heating.py
│   ├── validation.py
│   └── reporting.py
│
└── docs/
    ├── methodology.md
    ├── equations.md
    ├── assumptions.md
    ├── insulation_guidelines.md
    └── references.md
```

---

# Typical Applications

The calculator can be used for:

- Crude Oil Storage Tanks
- Heavy Fuel Oil Tanks
- Bitumen Storage Tanks
- Molten Sulfur Tanks
- Methanol Storage Tanks
- Glycol Storage Tanks
- Chemical Storage Tanks
- Condensate Tanks
- Fire Water Tanks
- LNG Auxiliary Tanks
- Heated Product Storage
- Utility Storage Tanks

---

# Engineering Skills Demonstrated

- Heat Transfer Analysis
- Storage Tank Thermal Design
- Insulation Design
- Energy Efficiency Assessment
- Process Equipment Design
- API 650 & API 620
- Thermal Engineering
- Process Engineering
- Python for Engineering
- Engineering Automation
- FEED & Detailed Engineering

---

# Project Value

This project demonstrates how conventional thermal design spreadsheets can be transformed into a structured engineering software application that improves calculation accuracy, engineering transparency, and design efficiency.

It showcases the integration of:

- Heat Transfer
- Thermal Engineering
- Process Engineering
- Storage Tank Design
- Energy Optimization
- Digital Engineering
- Python Programming
- Engineering Automation

---

# Future Enhancements

Planned improvements include:

- Radiation heat transfer calculations
- Solar heat gain estimation
- Transient cooling analysis
- Heating coil sizing
- Steam tracing calculations
- Electric heat tracing design
- Insulation optimization studies
- Multi-layer insulation analysis
- Annual energy cost estimation
- CO₂ emission calculations
- Excel and PDF report generation
- Interactive Streamlit dashboard

---

# Disclaimer

This tool is intended for educational, portfolio, and preliminary engineering purposes only. Final thermal design should always be verified using project specifications, applicable design standards, detailed heat transfer analysis, and sound engineering judgment.

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
