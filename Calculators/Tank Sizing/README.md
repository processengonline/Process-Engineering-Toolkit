# Tank Sizing Tool (Atmospheric & Low-Pressure Storage Tanks)

**Script:** [`tank_sizing.py`](./tank_sizing.py) · **Sample output:** [`sample_report_output.txt`](./sample_report_output.txt)

```bash
python tank_sizing.py --help
```

## Overview

This repository contains a comprehensive **Tank Sizing Tool** developed for the preliminary design and sizing of **atmospheric** and **low-pressure storage tanks** used in oil & gas, LNG, petrochemical, refinery, chemical, and utility facilities.

The tool automates the engineering calculations traditionally performed using spreadsheets and provides a systematic methodology for determining storage tank dimensions based on **storage capacity**, **operating philosophy**, **site constraints**, and **industry design practices**.

It calculates the required **working volume**, **gross storage capacity**, and evaluates multiple diameter-height combinations to identify an optimum tank geometry while satisfying operational and layout requirements.

The project is available as both an **Excel-based engineering calculator** and a **Python implementation**, enabling engineers to automate repetitive sizing calculations while maintaining complete engineering transparency.

---

# Engineering Objectives

The primary objectives of this project are to:

- Calculate the required storage capacity based on plant throughput and storage duration.
- Determine the required gross tank volume considering operating levels and freeboard.
- Size vertical cylindrical storage tanks in accordance with industry design practices.
- Generate multiple diameter-height combinations for engineering evaluation.
- Verify acceptable Height-to-Diameter (H/D) ratios.
- Evaluate tank operating levels including minimum, normal, and maximum liquid levels.
- Support preliminary equipment sizing during Conceptual Design, FEED, and Detailed Engineering.
- Provide engineering documentation suitable for equipment datasheets and layout development.

---

# Applicable Standards & References

The sizing methodology follows internationally recognized engineering standards and design references, including:

- API 650 – Welded Tanks for Oil Storage
- API 620 – Design and Construction of Large Welded Low-Pressure Storage Tanks
- IS 803 – Design of Steel Storage Tanks
- NFPA 30 – Flammable and Combustible Liquids Code
- Shell Design Engineering Practices (DEP) *(where applicable)*
- Company Engineering Standards
- Perry's Chemical Engineers' Handbook
- GPSA Engineering Data Book

---

# Features

## Storage Capacity Calculations

- Working Storage Volume
- Gross Tank Volume
- Effective Storage Volume
- Dead Storage Volume
- Freeboard Allowance
- Operating Inventory
- Surge Capacity

---

## Tank Geometry

- Vertical Cylindrical Tank Sizing
- Diameter Selection
- Shell Height Calculation
- H/D Ratio Verification
- Standard Diameter Evaluation
- Standard Height Selection

---

## Operational Checks

- Maximum Filling Level
- Normal Operating Level
- Minimum Operating Level
- Pump Suction Level
- Freeboard Verification
- Overflow Margin

---

## Engineering Verification

- Site Height Restrictions
- Maximum Diameter Constraints
- H/D Ratio Validation
- Working Volume Compliance
- Operating Volume Verification
- Layout Feasibility

---

# Required Inputs

## Process Requirements

- Storage duty
- Product throughput
- Storage duration (days)
- Design capacity
- Future expansion allowance

---

## Fluid Properties

- Fluid density
- Specific gravity
- Vapor pressure
- Operating temperature
- Product classification

---

## Operating Constraints

- Maximum filling percentage
- Minimum operating level
- Dead storage volume
- Freeboard allowance
- Roof type
- Fire-fighting allowance (if applicable)

---

## Site Constraints

- Maximum allowable diameter
- Maximum allowable height
- Plot limitations
- Transportation restrictions
- Foundation limitations

---

## Design Preferences

- Fixed roof
- Cone roof
- Dome roof
- Internal floating roof
- External floating roof

---

# Engineering Methodology

The sizing workflow follows a standard process engineering approach:

1. Determine required storage based on plant throughput and storage philosophy.
2. Calculate the required working volume.
3. Apply filling limitations to determine gross tank volume.
4. Select a trial tank diameter.
5. Calculate the corresponding shell height.
6. Verify Height-to-Diameter ratio.
7. Check against site and layout constraints.
8. Generate multiple geometry options.
9. Compare feasible designs.
10. Select the optimum storage tank configuration.

---

# Governing Equations

## 1. Working Storage Volume

### Mathematical Expression

\[
V_{work}=Q\times t
\]

### GitHub Format

```text
Vwork = Throughput × Storage Time
```

Where:

| Parameter | Description | Units |
|-----------|-------------|-------|
| Vwork | Working storage volume | m³ |
| Q | Throughput | m³/day |
| t | Storage duration | days |

---

## 2. Gross Tank Volume

### Mathematical Expression

\[
V_{gross}=\frac{V_{work}}{f_{fill}}
\]

### GitHub Format

```text
Vgross = Vwork / Fill Fraction
```

Where:

| Parameter | Description |
|-----------|-------------|
| Vgross | Gross tank volume |
| Fill Fraction | Maximum allowable filling percentage |

---

## 3. Cylindrical Tank Volume

### Mathematical Expression

\[
V=\frac{\pi D^2}{4}\times H
\]

### GitHub Format

```text
V = (π × D² × H) / 4
```

Where:

| Parameter | Description | Units |
|-----------|-------------|-------|
| D | Tank diameter | m |
| H | Shell height | m |

---

## 4. Required Tank Height

For a selected tank diameter:

### GitHub Format

```text
H = (4 × Vgross) / (π × D²)
```

---

## 5. Height-to-Diameter Ratio

```text
H/D = Tank Height ÷ Tank Diameter
```

Typical engineering practice:

| H/D Ratio | Evaluation |
|-----------|------------|
| < 0.5 | Very wide tank |
| 0.5 – 1.5 | Preferred design range |
| > 1.5 | Tall, less economical |

---

## 6. Working Capacity Verification

```text
Working Volume ≤ Fill Fraction × Gross Volume
```

---

## 7. Freeboard Requirement

```text
Freeboard = Tank Height − Maximum Liquid Level
```

---

# Spreadsheet Structure

| Worksheet | Description |
|------------|-------------|
| **Inputs** | Product throughput, storage philosophy, operating levels, fluid properties, design constraints |
| **Volume_Calculations** | Working volume, gross volume, dead storage, freeboard calculations |
| **Geometry_Options** | Standard diameter-height combinations with feasibility checks |
| **Tank_Checks** | H/D ratio, fill levels, freeboard, operating limits, layout verification |
| **Summary** | Final tank dimensions, storage capacities, operating levels, engineering recommendations |

---

# Repository Structure

```text
Tank-Sizing-Tool/
│
├── README.md
├── tank_sizing.py
├── inputs.yaml
│
├── spreadsheets/
│   └── tank_sizing.xlsx
│
├── examples/
│   ├── crude_oil_storage.yaml
│   ├── diesel_storage.yaml
│   ├── condensate_storage.yaml
│   ├── fire_water_tank.yaml
│   ├── chemical_storage.yaml
│   └── sample_results.md
│
├── results/
│   ├── sizing_report.pdf
│   ├── tank_dimensions.xlsx
│   └── geometry_options.csv
│
├── utils/
│   ├── volume.py
│   ├── geometry.py
│   ├── operating_levels.py
│   ├── validation.py
│   └── reporting.py
│
└── docs/
    ├── methodology.md
    ├── equations.md
    ├── assumptions.md
    ├── design_guidelines.md
    └── references.md
```

---

# Typical Applications

The tool can be used for preliminary sizing of:

- Crude Oil Storage Tanks
- Diesel Storage Tanks
- Condensate Storage Tanks
- Produced Water Tanks
- Fire Water Tanks
- Utility Water Tanks
- Chemical Storage Tanks
- Methanol Storage Tanks
- Glycol Storage Tanks
- LNG Auxiliary Storage
- Product Loading Tanks
- Intermediate Process Tanks

---

# Engineering Skills Demonstrated

- Storage Tank Design
- Tank Sizing Calculations
- API 650 & API 620
- Process Equipment Design
- Process Engineering
- Oil & Gas Facilities
- FEED & Detailed Engineering
- Engineering Calculations
- Python for Engineering
- Engineering Automation
- Equipment Layout Studies

---

# Project Value

This project demonstrates how conventional storage tank sizing spreadsheets can be transformed into a structured engineering software application that improves calculation consistency, engineering transparency, and design efficiency.

It showcases the integration of:

- Process Engineering
- Equipment Design
- Storage Tank Design
- Engineering Calculations
- Digital Engineering
- Python Programming
- Engineering Automation

---

# Future Enhancements

Planned improvements include:

- Horizontal storage tank sizing
- Floating roof calculations
- Roof volume estimation
- Wind girder recommendations
- Shell course estimation
- Nozzle sizing
- Tank foundation load estimation
- Hydrotest volume calculations
- Roof drain calculations
- Automatic API 650 design checks
- Excel and PDF report generation
- Interactive Streamlit web application

---

# Disclaimer

This tool is intended for educational, portfolio, and preliminary engineering purposes only. Final storage tank design should always be verified in accordance with applicable design codes, project specifications, client standards, and detailed mechanical design calculations.

---

# Author

**Shubham**

**Process Engineer**

Specializations:

- Storage Tank Design
- Process Equipment Design
- Process Hydraulics
- Aspen HYSYS & Honeywell UniSim
- LNG, GTL & Gas Processing
- EPC Detailed Engineering
- Python-Based Engineering Automation
