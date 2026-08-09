# PSV Sizing Calculator (API 520 / API 521 / API 526)

## Overview

This repository contains a Python-based **Pressure Safety Valve (PSV) Sizing Calculator** developed to automate preliminary relief valve sizing calculations in accordance with **API 520**, **API 521**, and **API 526**.

The tool evaluates various relief scenarios, calculates the required relief area, and recommends an appropriate API 526 standard orifice size. It is intended for process engineers involved in pressure relief studies, equipment design, debottlenecking, and process safety reviews.

The calculator serves as a transparent and auditable alternative to traditional spreadsheet-based PSV sizing workflows while maintaining engineering traceability and modularity.

---

# Engineering Objectives

The tool enables engineers to:

- Calculate required PSV relief area for gas, vapor, and liquid services
- Evaluate relief requirements for common overpressure scenarios
- Select the appropriate API 526 standard orifice size
- Verify sizing against allowable overpressure criteria
- Assess the impact of backpressure and correction factors
- Generate consistent and reproducible PSV sizing calculations

---

# Applicable Standards

The methodology follows the requirements and recommendations of:

- API 520 Part I – Sizing and Selection
- API 520 Part II – Installation
- API 521 – Pressure Relieving and Depressuring Systems
- API 526 – Flanged Steel Pressure Relief Valves
- ASME Section VIII (Pressure Vessel Protection Requirements)

---

# Typical Relief Scenarios

The calculator can be applied to:

### Vessel Protection

- Blocked outlet
- Gas blow-by
- Control valve failure
- Utility failure
- Thermal expansion
- External fire exposure

### Process Equipment

- Separators
- Heat exchangers
- Pressure vessels
- Pipelines
- Storage systems
- Process columns

---

# Features

### Gas & Vapor Relief Sizing

- Critical flow calculations
- API 520 vapor sizing methodology
- Compressibility factor correction
- Molecular weight adjustment
- Backpressure correction

### Liquid Relief Sizing

- API liquid sizing equations
- Capacity correction factors
- Viscosity correction options
- Backpressure considerations

### PSV Selection

- Required relief area calculation
- API 526 standard orifice selection
- Overpressure verification
- Discharge coefficient application

### Reporting

- Detailed sizing summary
- Calculation transparency
- Input validation
- Engineering assumptions log

---

# Repository Structure

```text
PSV-Sizing-Calculator/
│
├── README.md
├── psv_sizing.py
├── inputs.yaml
│
├── examples/
│   ├── gas_relief_case.yaml
│   ├── liquid_relief_case.yaml
│   └── fire_case.yaml
│
├── results/
│   ├── sizing_report.txt
│   └── sizing_summary.csv
│
├── utils/
│   ├── gas_sizing.py
│   ├── liquid_sizing.py
│   ├── api526.py
│   ├── correction_factors.py
│   └── validation.py
│
└── docs/
    ├── methodology.md
    ├── equations.md
    ├── api_references.md
    └── assumptions.md
```

---

# Required Inputs

## Protected Equipment

- Equipment type
- Design pressure
- MAWP
- Set pressure
- Accumulation / allowable overpressure

## Relief Scenario

- Blocked outlet
- Fire case
- Thermal expansion
- Gas blow-by
- Control valve failure
- Utility failure

## Relief Conditions

- Relieving pressure (P₁)
- Relieving temperature (T₁)
- Backpressure (P₂)
- Relief rate

## Fluid Properties

### Gas/Vapor Service

- Molecular weight
- Compressibility factor (Z)
- Specific heat ratio (k)
- Density

### Liquid Service

- Density
- Viscosity
- Vapor pressure

---

# Engineering Methodology

The sizing workflow follows a standard pressure relief design process:

### Step 1

Define the governing relief scenario and determine the required relief load.

### Step 2

Calculate relieving conditions in accordance with API 521.

### Step 3

Determine required PSV flow area using API 520 sizing equations.

### Step 4

Apply correction factors:

- Kd – Discharge coefficient
- Kb – Backpressure correction
- Kc – Combination correction
- Kv – Viscosity correction
- Kw – Liquid capacity correction

### Step 5

Select the smallest API 526 standard orifice that satisfies the required area.

### Step 6

Generate a detailed sizing report for engineering review.

---

# Core Sizing Equations

## Gas / Vapor Service

The required relief area is calculated using the API 520 critical-flow methodology.

Inputs include:

- Relief load
- Relieving pressure
- Molecular weight
- Compressibility factor
- Specific heat ratio
- Correction factors

Outputs:

- Required relief area
- Selected API 526 orifice size
- Capacity margin

---

## Liquid Service

The required relief area is calculated using API liquid sizing methodology considering:

- Flow rate
- Density
- Differential pressure
- Viscosity effects
- Capacity correction factors

Outputs:

- Required relief area
- Selected API 526 orifice size
- Hydraulic verification

---

# Example Output

```text
---------------------------------------
PSV SIZING REPORT
---------------------------------------

Relief Scenario      : Blocked Outlet

Fluid Phase          : Gas

Set Pressure         : 15.0 barg

Relieving Pressure   : 16.5 barg

Relief Load          : 12,500 kg/hr

Required Area        : 1.42 in²

Selected Orifice     : J

API 526 Area         : 1.287 in²

Next Available Size  : K

Installed Area       : 1.838 in²

Capacity Margin      : 29%

Backpressure Check   : PASS

Overpressure Check   : PASS

Overall Status       : ACCEPTABLE
```

---

# Future Enhancements

Planned improvements include:

- Two-phase PSV sizing methodologies
- Fire-case wetted area calculations
- API 521 heat input calculations
- Depressuring valve sizing
- Flare system hydraulics
- Tailpipe pressure drop calculations
- Built-in fluid property package
- HYSYS export/import compatibility
- Excel report generation
- Interactive web application (Streamlit)

---

# Engineering Skills Demonstrated

- Pressure Relief System Design
- PSV Sizing
- API 520 / API 521 / API 526
- Process Safety Engineering
- Loss of Containment Prevention
- Flare and Relief System Design
- Python for Process Engineering
- Engineering Automation
- Equipment Design Verification
- Process Risk Management

---

# Project Value

This project demonstrates how traditional process engineering calculations can be transformed into reliable, reusable software tools that improve consistency, reduce manual effort, and enhance engineering productivity.

It showcases the intersection of:

- Process Engineering
- Process Safety
- Digital Engineering
- Python Programming
- Engineering Automation

---

# Disclaimer

This tool is intended for educational, portfolio, and preliminary engineering purposes only. Final PSV sizing must always be verified using approved engineering procedures, applicable codes and standards, project specifications, and qualified engineering judgment.

---

- # Author

**Shubham**

**Process Engineer**

Specializations:

- Process Safety & Relief Systems
- Aspen HYSYS & Honeywell UniSim
- LNG, GTL & Gas Processing Facilities
- EPC Detailed Engineering
- Dynamic Process Troubleshooting
- Python-Based Engineering Automation
- Process Design & Optimization
