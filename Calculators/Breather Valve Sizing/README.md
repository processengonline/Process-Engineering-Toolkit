# Breather Valve (Pressure–Vacuum Relief Valve) Sizing Tool

**Script:** [`breather_valve.py`](./breather_valve.py) · **Sample output:** [`sample_report_output.txt`](./sample_report_output.txt)

```bash
python breather_valve.py --help
```

## Overview

This repository contains a comprehensive **Breather Valve (Pressure–Vacuum Relief Valve) Sizing Tool** developed for the sizing and selection of conservation vents used on **atmospheric** and **low-pressure storage tanks** in oil & gas, LNG, petrochemical, refinery, chemical, and terminal facilities.

The tool automates the engineering calculations traditionally performed using spreadsheets and follows the methodology outlined in **API Standard 2000** and **ISO 28300** for determining the required **pressure relief (out-breathing)** and **vacuum relief (in-breathing)** capacities.

It evaluates operational venting caused by **liquid transfer**, **thermal breathing**, and **vapor generation**, and assists engineers in selecting appropriately sized breather valves to protect storage tanks from excessive internal pressure or vacuum.

The project is available as both an **Excel-based engineering calculator** and a **Python implementation**, enabling transparent engineering calculations and workflow automation.

---

# Engineering Objectives

The primary objectives of this project are to:

- Calculate pressure relief (out-breathing) requirements.
- Calculate vacuum relief (in-breathing) requirements.
- Evaluate venting requirements during filling and emptying operations.
- Calculate thermal breathing due to ambient temperature variations.
- Estimate vapor generation where applicable.
- Convert venting requirements into standard air capacities.
- Select suitable pressure-vacuum relief valves based on manufacturer capacity data.
- Verify compliance with API 2000 and ISO 28300 requirements.
- Support preliminary engineering, FEED, Detailed Engineering, and tank revamp projects.

---

# Applicable Standards & References

The sizing methodology follows internationally recognized engineering standards and references, including:

- API Standard 2000 – Venting Atmospheric and Low-Pressure Storage Tanks
- ISO 28300 – Petroleum and Petrochemical Industries – Venting of Atmospheric and Low-Pressure Storage Tanks
- API 650 – Welded Tanks for Oil Storage
- API 620 – Design and Construction of Large Welded Low-Pressure Storage Tanks
- NFPA 30 – Flammable and Combustible Liquids Code
- Perry's Chemical Engineers' Handbook
- GPSA Engineering Data Book
- Manufacturer Capacity Charts (Protectoseal, Groth, Shand & Jurs, Emerson, etc.)
- Company Engineering Standards (where applicable)

---

# Features

## Pressure Relief (Out-Breathing)

- Liquid filling calculations
- Thermal expansion breathing
- Vapor generation allowance
- Emergency pressure vent verification
- Total pressure relief capacity

---

## Vacuum Relief (In-Breathing)

- Liquid withdrawal calculations
- Thermal contraction breathing
- Air replacement requirements
- Total vacuum relief capacity

---

## Vent Capacity Calculations

- API 2000 methodology
- Standard air flow conversion
- SCFH calculations
- Nm³/h calculations
- Combined operational and thermal venting

---

## Valve Selection

- Pressure relief valve sizing
- Vacuum relief valve sizing
- Combined P/V valve selection
- Capacity margin verification
- Multiple valve configuration support

---

## Engineering Verification

- Tank design pressure verification
- Tank design vacuum verification
- Venting capacity compliance
- Pressure and vacuum margin assessment
- Manufacturer capacity comparison

---

# Required Inputs

## Tank Information

- Tank diameter
- Tank height
- Gross storage volume
- Working capacity
- Tank type
- Roof type
- Design pressure
- Design vacuum

---

## Product Properties

- Product type
- Flash point
- Vapor pressure
- Storage temperature
- Molecular weight
- Product classification

---

## Operating Conditions

### Filling

- Maximum filling rate
- Filling duration
- Pump capacity

### Emptying

- Maximum withdrawal rate
- Pump-out rate
- Gravity drain (if applicable)

---

## Environmental Conditions

- Maximum ambient temperature
- Minimum ambient temperature
- Daily temperature variation
- Solar radiation
- Wind conditions (optional)

---

## Design Parameters

- Vent set pressure
- Vent set vacuum
- Required design margin
- Standard flow units
- Safety factors

---

# Engineering Methodology

The sizing calculations follow the engineering workflow below:

1. Define tank geometry and operating conditions.
2. Calculate operational out-breathing due to filling.
3. Calculate operational in-breathing due to emptying.
4. Calculate thermal expansion breathing.
5. Calculate thermal contraction breathing.
6. Estimate vapor generation (where applicable).
7. Convert all venting requirements to standard air flow.
8. Determine governing pressure relief case.
9. Determine governing vacuum relief case.
10. Compare required capacity with manufacturer valve capacities.
11. Select the optimum pressure-vacuum relief valve.
12. Generate engineering sizing report.

---

# Governing Calculations

API 2000 provides standardized procedures for determining venting requirements based on operational and thermal breathing. The calculator implements these methodologies using modular engineering calculations.

---

## 1. Operational Out-Breathing

Occurs during tank filling.

```text
Qout,operational = Maximum Liquid Filling Rate
```

---

## 2. Operational In-Breathing

Occurs during liquid withdrawal.

```text
Qin,operational = Maximum Liquid Withdrawal Rate
```

---

## 3. Thermal Out-Breathing

Occurs when ambient temperature increases, causing vapor expansion.

```text
Qthermal,out = f(Tank Volume,
                 Vapor Space,
                 Temperature Rise,
                 Product Properties)
```

Calculated using API 2000 thermal venting methodology.

---

## 4. Thermal In-Breathing

Occurs during cooling of the vapor space.

```text
Qthermal,in = f(Tank Volume,
                Vapor Space,
                Temperature Drop,
                Product Properties)
```

---

## 5. Vapor Generation

For volatile liquids:

```text
Qvapor = f(Vapor Pressure,
           Product Temperature,
           Filling Rate,
           Product Characteristics)
```

---

## 6. Total Pressure Relief Requirement

```text
Qout,total =
      Operational Filling
    + Thermal Expansion
    + Vapor Generation
```

---

## 7. Total Vacuum Relief Requirement

```text
Qin,total =
      Operational Emptying
    + Thermal Contraction
```

---

## 8. Standard Air Flow Conversion

Required venting capacities are converted into:

- SCFH (Standard Cubic Feet per Hour)
- Nm³/h (Normal Cubic Metres per Hour)

using API 2000 standard conversion procedures.

---

## 9. Valve Capacity Verification

```text
Selected Valve Capacity ≥ Required Venting Capacity
```

For multiple valves:

```text
Combined Valve Capacity ≥ Required Capacity
```

---

# Spreadsheet Structure

| Worksheet | Description |
|------------|-------------|
| **Inputs** | Tank geometry, operating conditions, product properties, environmental data |
| **Operational_Venting** | Filling and emptying venting calculations |
| **Thermal_Breathing** | Thermal expansion and contraction calculations |
| **Conversions** | Standard air flow conversions (SCFH / Nm³/h) |
| **Valve_Selection** | Valve sizing, capacity verification, manufacturer comparison |
| **Summary** | Final pressure and vacuum relief requirements, selected valve, engineering recommendations |

---

# Repository Structure

```text
Breather-Valve-Sizing/
│
├── README.md
├── breather_valve_sizing.py
├── inputs.yaml
│
├── spreadsheets/
│   └── breather_valve_sizing.xlsx
│
├── examples/
│   ├── crude_oil_storage.yaml
│   ├── diesel_storage.yaml
│   ├── methanol_storage.yaml
│   ├── condensate_storage.yaml
│   ├── chemical_storage.yaml
│   └── sample_results.md
│
├── results/
│   ├── sizing_report.pdf
│   ├── valve_selection.xlsx
│   └── venting_summary.csv
│
├── utils/
│   ├── operational.py
│   ├── thermal.py
│   ├── conversions.py
│   ├── valve_selection.py
│   ├── validation.py
│   └── reporting.py
│
└── docs/
    ├── methodology.md
    ├── api2000_notes.md
    ├── equations.md
    ├── assumptions.md
    └── references.md
```

---

# Typical Applications

The calculator can be used for:

- Atmospheric Storage Tanks
- Low-Pressure Storage Tanks
- Crude Oil Tanks
- Diesel Storage Tanks
- Condensate Tanks
- Chemical Storage Tanks
- Methanol Tanks
- Glycol Storage Tanks
- Fire Water Tanks
- Utility Tanks
- Product Loading Facilities
- Tank Farms
- LNG Auxiliary Storage Systems

---

# Engineering Skills Demonstrated

- API 2000 Vent Sizing
- Storage Tank Engineering
- Pressure–Vacuum Relief Design
- Process Equipment Design
- Tank Venting Calculations
- Oil & Gas Process Engineering
- Process Safety Engineering
- FEED & Detailed Engineering
- Engineering Calculations
- Python for Engineering
- Engineering Automation

---

# Project Value

This project demonstrates how conventional breather valve sizing spreadsheets can be transformed into a structured engineering software application that improves calculation accuracy, consistency, traceability, and engineering productivity.

It showcases the integration of:

- Process Engineering
- Process Safety
- Storage Tank Design
- API 2000 Venting Calculations
- Equipment Sizing
- Digital Engineering
- Python Programming
- Engineering Automation

---

# Future Enhancements

Planned improvements include:

- Emergency fire vent sizing
- Flame arrester pressure drop calculations
- Combined breather valve and flame arrester sizing
- Floating roof vent calculations
- API 2000 Annex calculations
- Multi-compartment tank analysis
- Vendor-specific valve selection database
- Automatic manufacturer datasheet generation
- Excel and PDF report generation
- Interactive Streamlit dashboard
- 3D tank venting visualization

---

# Disclaimer

This tool is intended for educational, portfolio, and preliminary engineering purposes only. Final breather valve selection should always be verified using the latest edition of API 2000, applicable project specifications, manufacturer performance data, and sound engineering judgment.

---

# Author

**Shubham**

**Process Engineer**

Specializations:

- Storage Tank Engineering
- Pressure–Vacuum Relief System Design
- Process Safety Engineering
- Aspen HYSYS & Honeywell UniSim
- LNG, GTL & Gas Processing
- EPC Detailed Engineering
- Python-Based Engineering Automation
