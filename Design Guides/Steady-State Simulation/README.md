# 🖥️ Steady-State Simulation — Practical Study Guide

> A field-oriented reference covering the core engineering topics in steady-state process simulation — combining Aspen HYSYS/UniSim/PRO-II methodology with worked sample calculations, sample documents, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design**, **Depressurization Calculation**, **Compressor Settle-Out Calculations**, **Line List Preparation**, **Instrumentation Process Datasheet Preparation**, **Mechanical Datasheet Preparation**, and **P&ID / PEFS Development** study guides — the steady-state simulation is the model every one of those disciplines' design conditions is ultimately extracted from.

**Illustrative project used throughout this guide:** the same gas processing system used across this guide series — vessel V-100 (flash/suction drum), heat exchanger E-101, compressor K-101, and a new depropanizer column C-101 — used to work through a manual flash validation, a heat exchanger duty cross-check, a compressor power cross-check, a shortcut distillation check, and a recycle-loop convergence acceleration example. All numbers below are worked sample calculations for study purposes — always replace with project-specific PVT data and the current version of the simulation software's property packages.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Simulation Fundamentals](#2-simulation-fundamentals)
3. [Thermodynamic Models](#3-thermodynamic-models)
4. [Unit Operations Modeling](#4-unit-operations-modeling)
5. [Convergence & Solver Techniques](#5-convergence--solver-techniques)
6. [Case Studies & Applications by Industry Segment](#6-case-studies--applications-by-industry-segment)
7. [Validation & QA/QC](#7-validation--qaqc)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Documents & Datasheets](#9-sample-documents--datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Wrong Thermodynamic Package Selected for TEG Dehydration](#12-case-study--wrong-thermodynamic-package-selected-for-teg-dehydration)
13. [Reference Standards & Tools](#13-reference-standards--tools)

---

## 1. Design Basis & Assumptions

Steady-state simulation work is normally governed by a **"Simulation Basis Document"** — fluid composition, thermodynamic package selection, boundary conditions, and key assumptions — issued and frozen before detailed modeling begins. Every downstream discipline in this guide series (line list, instrumentation, mechanical, flare) ultimately traces its design conditions back to this document, so its assumptions carry consequences far beyond the simulation file itself.

### 1.1 Process & Model Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Unit | Gas processing train: V-100 (flash) → K-101 (compression) → E-101 (cooling) → C-101 (depropanizer) | Same equipment tags used throughout this guide series |
| Feed composition (simplified, mol%) | C1: 40%, C3: 35%, nC4: 25% | Used in Calc Sheet 8.1 flash validation |
| Flash conditions (V-100) | 300 psia / 100 °F | — |
| Compressor K-101 duty case | 800 → 2,500 psia, MW 18, k = 1.13 | Consistent with companion Compressor Settle-Out guide |
| Exchanger E-101 duty case | 50,000 lb/hr, cooled 300 °F → 200 °F | Consistent with companion Mechanical Datasheet guide |
| Depropanizer C-101 | Relative volatility (C3/nC4) ≈ 2.5, xD = 0.98, xB(HK) recovery = 97% | Used in Calc Sheet 8.4 shortcut check |
| Software | Aspen HYSYS (illustrative — methodology applies equally to UniSim, Aspen Plus, PRO/II) | — |
| Thermodynamic package | Peng-Robinson (hydrocarbon sections); NRTL (glycol dehydration section, per Section 3 and Case Study) | — |

### 1.2 Codes & Standards / Methodology Basis
- Vendor software documentation (Aspen HYSYS/Plus, UniSim, PRO/II) for property package theory and numerical methods
- GPSA Engineering Data Book — widely used reference for gas processing K-values, equilibrium data, and rule-of-thumb cross-checks
- Company/project **Simulation Basis Document** and **modeling standards** — governs required documentation, validation, and sign-off before a simulation is used as a design basis

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Thermodynamic package selection | Matched to fluid polarity/system type (Section 3) | Never defaulted to "whatever the last model used," per the Case Study (Section 12) |
| Hand-calc vs. simulation agreement tolerance | ±2–5% for duty/power cross-checks; wider for shortcut column methods | Confirm project QA/QC philosophy — see Section 7 |
| Recycle convergence tolerance | ±0.1–1% on tear-stream flow/composition, per project standard | Tighter tolerances increase iteration count/runtime |
| Tray/packing efficiency (columns) | Confirmed against a licensor/vendor value or a validated correlation, not assumed at 100% (theoretical stage) efficiency | A common overly-optimistic default that understates actual column height/stage requirements |
| Equipment sizing margin from simulation output | Simulation gives the process duty/rate; mechanical/instrument datasheets (companion guides) apply their own design margins on top, not duplicated within the simulation itself | Avoids "margin stacking" that oversizes equipment |
| Simulation documentation | Basis, assumptions, and limitations recorded alongside every issued case | Section 7.3; a simulation file without this record is not a usable design basis |

> ⚠️ **Practical note:** The thermodynamic package selection (Section 1.3, Section 3) is the single assumption most likely to silently produce plausible-looking but wrong results — a converged, good-looking simulation run provides no self-evident warning that the underlying property model doesn't fit the fluid system. This is exactly the failure mode explored in the Case Study (Section 12).

---

## 2. Simulation Fundamentals

### 2.1 Purpose
Steady-state simulation serves several distinct purposes across a project's life cycle:
- **Mass & energy balance** — the foundational output feeding the companion PEFS/P&ID guide's stream summary tables and every downstream sizing calculation in this guide series.
- **Equipment sizing** — duty, flow, and composition data that becomes the input to the companion Mechanical Datasheet and Instrumentation guides' calc sheets.
- **Utility demand** — steam, cooling water, fuel gas, and power consumption, feeding the companion P&ID/PEFS guide's utility connection sizing (Calc Sheets 8.3–8.4 of that guide).
- **Design validation** — confirming a proposed process configuration actually achieves its target specifications before committing to detailed engineering.

### 2.2 Software Tools
| Tool | Typical Use |
|---|---|
| **Aspen HYSYS** | Oil & gas, gas processing, refining — strong in hydrocarbon systems and dynamic extension |
| **Aspen Plus** | Chemicals, petrochemicals — strong in complex reaction systems and rigorous distillation |
| **UniSim** | Functionally similar to HYSYS (Honeywell platform) — common in EPC contractor environments |
| **PRO/II** | Widely used in refining and gas processing, strong unit operation library |

### 2.3 Model Setup
- **Fluid properties** — component list, characterization of undefined/pseudo-components (e.g., crude oil assays), and binary interaction parameters.
- **Thermodynamic package** — selected per Section 3, matched to the actual fluid system, not defaulted from habit.
- **Boundary conditions** — feed composition/flow/conditions, and either specified product/utility flows or design specifications the solver iterates to meet (e.g., "adjust reflux ratio until distillate purity = 98%").

---

## 3. Thermodynamic Models

### 3.1 Equations of State (EOS)
- **Peng-Robinson (PR)** and **Soave-Redlich-Kwong (SRK)** — the standard choice for hydrocarbon systems (natural gas, NGLs, crude fractions, LNG) where the mixture is predominantly non-polar; consistent with the EOS basis used throughout the companion Compressor Settle-Out and Flow Assurance guides.

### 3.2 Activity Coefficient Models
- **NRTL** and **UNIQUAC** — required for polar or strongly non-ideal mixtures where a simple EOS mixing rule breaks down — classic examples include glycol dehydration (TEG/water), amine sweetening (MDEA/water/acid gas), and methanol/water systems (consistent with the companion Flow Assurance guide's hydrate inhibition chemistry).

### 3.3 Selection Criteria
| Fluid Type | Typical Package |
|---|---|
| Dry/wet natural gas, NGLs | Peng-Robinson or SRK |
| Crude oil, refinery hydrocarbon streams | Peng-Robinson (with characterized pseudo-components) |
| LNG / cryogenic hydrocarbon systems | Peng-Robinson (validated against cryogenic VLE data — see Section 6) |
| Glycol dehydration (TEG/water) | NRTL or a glycol-specific package (e.g., "Glycol Package" in HYSYS) — **not** a plain hydrocarbon EOS |
| Amine sweetening (MDEA, MEA) | Acid-gas-specific package (e.g., Amine Property Package) — electrolyte/activity-coefficient based, not a plain EOS |
| Petrochemicals with polar components | NRTL/UNIQUAC, or an EOS with an appropriate mixing rule for the specific polar pair |

**Practical tip:** The selection criterion is not "what package do I usually use" — it's "does this package's underlying theory match this specific fluid system's non-ideality." See the Case Study (Section 12) for the consequence of getting this wrong.

---

## 4. Unit Operations Modeling

### 4.1 Separators
Flash drums, knockout drums, and phase splitters are modeled as equilibrium stages (or, for a three-phase system, equilibrium among vapor/hydrocarbon-liquid/aqueous phases) — the resulting vapor/liquid split and composition is exactly what a manual Rachford-Rice flash calculation (Calc Sheet 8.1) can independently verify, and is the process basis the companion Flare Network Design guide's KOD sizing methodology depends on.

### 4.2 Heat Exchangers
Modeled via an energy balance (`Q = m × Δh`, using rigorous enthalpy from the property package, not a constant-Cp shortcut) plus a specified approach temperature or duty — the simulator's rigorous duty can be independently sanity-checked with a simplified `Q = m × Cp × ΔT` hand calc (Calc Sheet 8.2), which is exactly the kind of cross-check the companion Mechanical Datasheet guide's exchanger datasheet depends on being correct.

### 4.3 Compressors & Pumps
- Modeled against a **performance curve** (vendor data, once available) or an idealized polytropic/isentropic efficiency assumption for early design — the resulting power/head can be independently checked with a hand calc (Calc Sheet 8.3), and the discharge conditions feed directly into the companion Compressor Settle-Out guide's settle-out pressure methodology.
- **Settle-out checks** — confirming the simulation's suction/discharge conditions are consistent with the inputs used in the companion Compressor Settle-Out guide's mass/energy balance (that guide's Calc Sheet 8.1 methodology).

### 4.4 Reactors
- **Stoichiometric models** — fixed conversion or extent of reaction, used for early-stage mass balance work before kinetic data is available.
- **Kinetic models** — rate-based, requiring reaction rate constants and residence time; used for detailed reactor sizing once kinetic data (lab or licensor-supplied) is available.

### 4.5 Columns
Distillation, absorption, and stripping columns are modeled either **rigorously** (tray-by-tray or packed-section equilibrium/mass-transfer calculations, converged simultaneously with the rest of the flowsheet) or via a **shortcut method** (Fenske-Underwood-Gilliland, Calc Sheet 8.4) for early screening — tray or packing efficiency must be applied to convert theoretical stages to actual trays/packing height, since 100% efficiency is rarely realistic (Section 1.3).

---

## 5. Convergence & Solver Techniques

### 5.1 Tear Streams and Recycle Loops
A recycle loop (e.g., unconverted gas returned to a compressor suction, or a distillation column's internal reflux) creates a circular dependency the solver must break by "tearing" the loop at a chosen stream, guessing its value, running the flowsheet, and comparing the calculated value against the guess — repeating until convergence.

### 5.2 Convergence Methods
| Method | Characteristics |
|---|---|
| **Direct substitution** | Simplest — next guess = previous calculated value; can be slow or divergent for sensitive loops |
| **Wegstein** | Acceleration method using a weighted extrapolation between the last two iterations — faster convergence for many recycle loops; worked example in Calc Sheet 8.5 |
| **Newton (Newton-Raphson)** | Uses derivative (Jacobian) information — fast convergence near the solution, but requires derivative estimation and can be unstable far from the solution |
| **Broyden** | A quasi-Newton method — approximates the Jacobian from successive iterations rather than computing it directly, balancing robustness and speed |

### 5.3 Handling Difficult Convergence in Large Networks
- Choose tear streams thoughtfully — tearing a loop at a stream with strongly non-linear sensitivity (e.g., near a phase boundary) tends to converge poorly; a different tear point in the same loop can converge far more reliably.
- Provide good initial estimates wherever possible (from a prior converged case, an analogous unit, or a hand estimate) rather than letting the solver start from a default guess.
- For large, multiply-recycled networks, converge sub-sections sequentially before attempting to converge the whole flowsheet simultaneously — isolating a problem loop is far easier in a small sub-flowsheet than in the full model.

---

## 6. Case Studies & Applications by Industry Segment

### 6.1 Gas Processing
Dehydration (TEG, per Section 3.3 and the Case Study), sweetening (amine treating), and NGL recovery (turboexpander/refrigeration cycles) — each requires its own matched thermodynamic package and unit operation modeling approach.

### 6.2 Refinery Units
Hydroprocessing (reaction + separation, often kinetic-model-based), FCC (complex reaction network, typically licensor-proprietary kinetics), and crude distillation (pseudo-component characterization from an assay, rigorous multi-draw column modeling).

### 6.3 LNG & Cryogenic Systems
Refrigeration cycle modeling (mixed refrigerant or cascade cycles) and liquefaction — demands an EOS validated specifically against cryogenic VLE data, since standard PR/SRK parameter fits are usually tuned against more moderate-temperature data and can extrapolate poorly to LNG temperatures without validation.

### 6.4 Utility Systems
Steam balance, cooling water networks, and flare load estimation — the simulation's utility consumption output is exactly the input the companion P&ID/PEFS guide's utility sizing calc sheets and the companion Flare Network Design guide's relief load studies depend on.

---

## 7. Validation & QA/QC

### 7.1 Compare Simulation Results with Design Basis or Plant Data
Every simulation case should be checked against **something independent** — a hand calculation (Section 8), a licensor/vendor guarantee, or actual plant data from a similar or predecessor unit — before being relied upon as a design basis. A simulation that converges without error is not the same as a simulation that is correct.

### 7.2 Sensitivity Analysis
Running the simulation across a range of pressure, temperature, or composition inputs reveals how sensitive the design is to uncertainty in the design basis — critical for identifying which assumptions most need firming up (e.g., via additional lab PVT work) before detailed engineering, and for building the "operating envelope" data other companion guides in this series rely on (e.g., the companion Instrumentation guide's full-operating-envelope sizing principle).

### 7.3 Documentation
Every issued simulation case should be accompanied by a record of: the simulation basis (composition, conditions), the assumptions made (Section 1.3), and the model's known limitations (e.g., "not validated below −40°F," "shortcut column method only, not yet rigorously converged") — so anyone using the simulation's output downstream understands what it does and does not confidently represent.

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific PVT data and simulation output.

### 8.1 Calc Sheet 1 — Manual Flash Validation (Rachford-Rice)

**Given:** Feed to V-100 at 300 psia / 100 °F, composition z(C1) = 0.40, z(C3) = 0.35, z(nC4) = 0.25; K-values at flash conditions (illustrative): K(C1) = 3.5, K(C3) = 0.85, K(nC4) = 0.35.

**Step 1 — Rachford-Rice objective function:**
```
f(V/F) = Σ [zi(Ki − 1)] / [1 + (V/F)(Ki − 1)] = 0
```

**Step 2 — Solve iteratively (trial values shown):**
| V/F | f(V/F) |
|---|---|
| 0.50 | +0.147 |
| 0.65 | +0.041 |
| 0.75 | −0.029 |
| 0.71 | ≈ 0.000 |

```
Converged: V/F ≈ 0.71
```

**Step 3 — Liquid and vapor compositions:**
```
xi = zi / [1 + (V/F)(Ki − 1)];  yi = Ki × xi

x(C1) = 0.40/2.775 = 0.144   y(C1) = 0.504
x(C3) = 0.35/0.894 = 0.392   y(C3) = 0.333
x(nC4)= 0.25/0.539 = 0.464   y(nC4)= 0.163
(Σx ≈ 1.00, Σy ≈ 1.00 — checks out)
```

**Result:** Hand-calculated vapor fraction ≈ **0.71**. If the simulator (HYSYS/UniSim) reports V/F = 0.706 for the same feed and K-values, the agreement (within ~0.5%) **validates** the simulation's flash result for this stream — exactly the kind of independent check described in Section 7.1.

> 📌 **Assumption check:** This example used constant, pre-determined K-values for clarity — the simulator instead calculates K-values rigorously from the selected EOS (Section 3) at actual flash conditions, iterating them together with the flash calculation itself. A hand-calc validation like this is most useful as an order-of-magnitude/sanity check, not an exact-match requirement.

---

### 8.2 Calc Sheet 2 — Heat Exchanger Duty Cross-Check

**Given:** E-101 process-side flow = 50,000 lb/hr, cooled from 300 °F to 200 °F, Cp ≈ 0.55 Btu/(lb·°F) (constant-Cp approximation).

**Step 1 — Simplified energy balance:**
```
Q = m × Cp × ΔT
Q = 50,000 × 0.55 × (300 − 200)
Q = 50,000 × 0.55 × 100
Q = 2,750,000 Btu/hr ≈ 2.75 MMBtu/hr (≈ 806 kW)
```

**Step 2 — Compare to simulator-reported duty:**
```
Simulator duty (rigorous enthalpy, real EOS) = 2.80 MMBtu/hr
Difference = (2.80 − 2.75)/2.80 × 100% ≈ 1.8%
```

**Result:** The hand-calc duty (2.75 MMBtu/hr) agrees with the simulator's rigorous duty (2.80 MMBtu/hr) within **≈1.8%** — well within the project's typical ±2–5% cross-check tolerance (Section 1.3). **PASS** — the simulator's exchanger duty is validated as reasonable for this stream.

> 📌 **Assumption check:** A larger discrepancy here would point to either a bad constant-Cp assumption (common near a phase change or for a stream with strongly temperature-dependent Cp) or a genuine simulation setup error — always investigate a mismatch beyond tolerance rather than assuming the hand calc is simply "less accurate" by default.

---

### 8.3 Calc Sheet 3 — Compressor Power Cross-Check

**Given:** K-101, W = 50,000 lb/hr, P1 = 800 psia, P2 = 2,500 psia, T1 = 560 °R, Z_avg = 0.85, MW = 18, k = 1.13, isentropic efficiency η = 75%.

**Step 1 — Isentropic work per unit mass:**
```
Ws = [Z×R×T1/MW] × [k/(k−1)] × [(P2/P1)^((k−1)/k) − 1]

(k−1)/k = 0.13/1.13 = 0.1150
(P2/P1)^0.1150 = 3.125^0.1150 ≈ 1.140

Z×R×T1/MW = (0.85 × 1.986 × 560)/18 ≈ 52.52 Btu/lb

Ws = 52.52 × (1.13/0.13) × (1.140 − 1)
Ws = 52.52 × 8.692 × 0.140
Ws ≈ 639 Btu/lb
```

**Step 2 — Apply isentropic efficiency:**
```
Actual work = 639 / 0.75 ≈ 852 Btu/lb
```

**Step 3 — Total power:**
```
Total power = 50,000 lb/hr × 852 Btu/lb = 42,600,000 Btu/hr
In kW: 42,600,000 / 3,412.14 ≈ 12,486 kW
```

**Step 4 — Compare to simulator-reported power:**
```
Simulator power (rigorous EOS, real-gas isentropic path) = 12,700 kW
Difference = (12,700 − 12,486)/12,700 × 100% ≈ 1.7%
```

**Result:** Hand-calc power (≈12,486 kW) agrees with the simulator's rigorous result (12,700 kW) within **≈1.7%**. **PASS** — the constant-Z shortcut method reasonably validates the simulator's compressor power for this duty.

---

### 8.4 Calc Sheet 4 — Shortcut Distillation Check (Fenske-Underwood-Gilliland)

**Given:** C-101 depropanizer, relative volatility α (C3/nC4) ≈ 2.5, light key (C3) recovery to distillate = 98%, heavy key (nC4) recovery to bottoms = 97%, feed roughly equimolar in light/heavy key, xD = 0.98.

**Step 1 — Fenske minimum stages:**
```
Nmin = ln[(0.98/0.02) × (0.97/0.03)] / ln(2.5)
Nmin = ln[49 × 32.33] / ln(2.5)
Nmin = ln(1,584) / 0.9163
Nmin = 7.368 / 0.9163 ≈ 8.0 stages
```

**Step 2 — Underwood minimum reflux (simplified binary approximation):**
```
Rmin = [xD/zF − α(1−xD)/(1−zF)] / (α−1)
Rmin = [0.98/0.50 − 2.5×0.02/0.50] / 1.5
Rmin = [1.96 − 0.10] / 1.5 ≈ 1.24
```

**Step 3 — Select operating reflux (typically 1.2–1.5 × Rmin):**
```
R = 1.4 × 1.24 ≈ 1.74
```

**Step 4 — Gilliland correlation (Eduljee approximation) for actual stages:**
```
X = (R − Rmin)/(R + 1) = (1.74 − 1.24)/2.74 ≈ 0.183

Y = 1 − exp{ [(1+54.4X)/(11+117.2X)] × [(X−1)/√X] }
  = 1 − exp{ [10.93/32.39] × [−0.818/0.427] }
  = 1 − exp{ 0.337 × (−1.914) }
  = 1 − exp(−0.646)
  = 1 − 0.524 ≈ 0.476

Y = (N − Nmin)/(N + 1)
0.476 = (N − 8.0)/(N + 1)
N ≈ 16–17 theoretical stages
```

**Result:** The shortcut method predicts **≈16–17 theoretical stages** at R ≈ 1.74. If the rigorous column simulation converges to **18 stages** at the same reflux, the shortcut result is in reasonable range (**~10% low**, a typical and expected shortcut-vs-rigorous gap) — this is a **plausibility check**, not an exact-match validation.

> 📌 **Assumption check:** Shortcut methods assume constant relative volatility and a binary-like key-component treatment — a rigorous simulation captures the actual composition-dependent volatility profile up and down the column, which is why some gap between the two methods is normal and expected, not a red flag on its own. Use the shortcut method for early screening and sanity-checking order of magnitude, not as a substitute for the rigorous result in detailed design.

---

### 8.5 Calc Sheet 5 — Wegstein Convergence Acceleration (Recycle Loop)

**Given:** A recycle stream's flow is being converged by iteration. Direct-substitution history: x₀ = 1,000 kg/hr → simulated f(x₀) = 1,050 kg/hr; next guess by direct substitution x₁ = f(x₀) = 1,050 kg/hr → simulated f(x₁) = 1,072 kg/hr.

**Step 1 — Estimate local slope between the last two iterations:**
```
s = [f(x1) − f(x0)] / (x1 − x0)
s = (1,072 − 1,050) / (1,050 − 1,000)
s = 22 / 50 = 0.44
```

**Step 2 — Wegstein acceleration factor:**
```
q = s / (s − 1)
q = 0.44 / (0.44 − 1) = 0.44 / (−0.56) ≈ −0.786
```

**Step 3 — Wegstein-accelerated next guess:**
```
x2 = q×x1 + (1−q)×f(x1)
x2 = (−0.786)(1,050) + (1.786)(1,072)
x2 = −825.3 + 1,914.6
x2 ≈ 1,089.3 kg/hr
```

**Result:** Direct substitution would simply try x2 = f(x1) = 1,072 kg/hr next; Wegstein instead extrapolates to **x2 ≈ 1,089.3 kg/hr**, anticipating the sequence's convergence trend and typically reaching the converged value in fewer iterations — especially valuable for a slowly-converging or gently oscillating recycle loop, which direct substitution alone can take many iterations (or fail) to resolve.

> 📌 **Assumption check:** Wegstein's benefit depends on the loop's local behavior being reasonably well-approximated by a linear extrapolation between the last two points — for strongly non-linear loops (e.g., near a phase boundary or an azeotrope), even Wegstein can converge poorly, and switching tear-stream choice or using a more robust method (Broyden, or a bounded/damped update) may be necessary (Section 5.3).

---

## 9. Sample Documents & Datasheets

### 9.1 Simulation Basis Document Excerpt

| Field | Value |
|---|---|
| **Case name** | GasProc-Base-Rev3 |
| **Software / version** | Aspen HYSYS V12 |
| **Thermodynamic package(s)** | Peng-Robinson (hydrocarbon sections); NRTL (TEG dehydration section) |
| **Feed basis** | Per Section 1.1 composition table |
| **Key design specifications** | C-101 distillate C3 purity ≥ 98 mol%; K-101 discharge 2,500 psia |
| **Known limitations** | Shortcut column check only for C-101 pre-FEED; rigorous convergence pending final tray count study |
| **Validation status** | Flash (V-100), duty (E-101), and power (K-101) cross-checked per Calc Sheets 8.1–8.3 — PASS |
| **Prepared by / Date / Revision** | — |

---

### 9.2 Sample Stream Summary Table

| Stream | Description | Phase | Flow (lb/hr) | Pressure (psia) | Temperature (°F) |
|---|---|---|---|---|---|
| 1 | Feed to V-100 | Mixed | 71,000 | 300 | 100 |
| 2 | V-100 vapor outlet (to K-101) | Vapor | 50,410 (V/F ≈ 0.71) | 300 | 100 |
| 3 | V-100 liquid outlet | Liquid | 20,590 | 300 | 100 |
| 4 | K-101 discharge (to E-101) | Vapor | 50,410 | 2,500 | ~300 (calc.) |
| 5 | E-101 outlet (to C-101) | Vapor/Liquid | 50,410 | 2,480 | 200 |

*(Illustrative — a real stream summary is generated directly from the simulation and cross-referenced to the companion PEFS/P&ID guide's Section 9.1 sample table format.)*

---

### 9.3 Sample Sensitivity Analysis Summary

| Case | Feed Pressure (psia) | K-101 Power (kW) | C-101 Reflux Ratio | Notes |
|---|---|---|---|---|
| Base case | 300 | 12,700 | 1.74 | Design basis |
| Low feed pressure (−10%) | 270 | 13,450 | 1.81 | Increased compression ratio drives higher power |
| High feed pressure (+10%) | 330 | 12,050 | 1.68 | — |
| Low feed C3 content (−5 mol%) | 300 | 12,650 | 1.95 | Lower LK concentration increases required reflux for same purity |

*(Illustrative — sensitivity studies like this identify which design basis inputs most need firming up before detailed engineering, per Section 7.2.)*

---

### 9.4 Sample Model Validation Summary

| Check | Hand-Calc Method | Simulator Result | Hand-Calc Result | Agreement | Status |
|---|---|---|---|---|---|
| V-100 flash | Rachford-Rice (Calc Sheet 8.1) | V/F = 0.706 | V/F = 0.71 | 0.6% | PASS |
| E-101 duty | m·Cp·ΔT (Calc Sheet 8.2) | 2.80 MMBtu/hr | 2.75 MMBtu/hr | 1.8% | PASS |
| K-101 power | Isentropic shortcut (Calc Sheet 8.3) | 12,700 kW | 12,486 kW | 1.7% | PASS |
| C-101 stages | Fenske-Underwood-Gilliland (Calc Sheet 8.4) | 18 stages (rigorous) | 16–17 stages | ~10% | PASS (expected shortcut gap) |

---

## 10. Practical Design Checklist

- [ ] Simulation basis document issued and approved (Section 1) before detailed modeling begins
- [ ] Thermodynamic package selected explicitly against the actual fluid system's polarity/non-ideality (Section 3), not defaulted from a prior project
- [ ] Every major unit operation's result independently cross-checked with a hand calculation before being relied upon — see Calc Sheets 8.1–8.4
- [ ] Recycle loop convergence method and tolerance appropriate for the loop's sensitivity (Section 5); Wegstein/Broyden considered for slow-converging loops — see Calc Sheet 8.5
- [ ] Tray/packing efficiency applied explicitly for columns, not left at 100% theoretical-stage default
- [ ] Sensitivity analysis performed across credible design-basis uncertainty ranges (Section 7.2)
- [ ] Simulation documentation includes basis, assumptions, and explicitly stated limitations (Section 7.3)
- [ ] Simulation output cross-checked against the companion Line List, Instrumentation, and Mechanical Datasheet guides' downstream design conditions for consistency
- [ ] For polar/non-ideal systems (glycol, amine, methanol/water), package validated against known VLE or plant data, not assumed adequate by default — see Case Study, Section 12
- [ ] For LNG/cryogenic systems, EOS parameters validated against cryogenic-temperature VLE data specifically, not just moderate-temperature default parameters

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Dehydration column underperformed against design water dew point spec | Wrong thermodynamic package (hydrocarbon EOS instead of glycol-specific/NRTL) used for a polar system | Match the package to the fluid system explicitly (Section 3) — see Case Study, Section 12 |
| Recycle loop simulation took excessive iterations or failed to converge | Direct substitution used on a sensitive loop without considering Wegstein/Broyden acceleration | Apply Wegstein (Calc Sheet 8.5) or reconsider the tear-stream location for difficult loops |
| Equipment oversized after "margin stacking" | Design margins applied both within the simulation case and again independently on the mechanical/instrument datasheets | Keep the simulation output as the process basis; apply design margins once, at the datasheet stage (companion Mechanical/Instrumentation guides) |
| Simulation results silently became invalid after a feed composition update | No process in place requiring re-validation of the thermodynamic package or a hand-calc cross-check after a significant input change | Re-run the Section 7.1 validation checks whenever a material change is made to feed composition or operating conditions |
| Shortcut column result taken as final design basis without a rigorous run | Shortcut methods (Calc Sheet 8.4) used past the appropriate screening stage due to schedule pressure | Treat shortcut results explicitly as a screening/plausibility tool; commit rigorous simulation before issuing for detailed design |

---

## 12. Case Study — Wrong Thermodynamic Package Selected for TEG Dehydration

> A composite, illustrative case study based on the type of finding commonly encountered during design review of gas dehydration units. Names, tag numbers, and figures are representative, not project-specific.

### 12.1 Background

A gas processing project (the illustrative train used throughout this guide) included a TEG (triethylene glycol) dehydration unit downstream of the compression and cooling train (K-101/E-101), designed to bring the sales gas water dew point down to meet a pipeline specification. The simulation engineer building out the flowsheet, working under schedule pressure, extended the same **Peng-Robinson** property package used successfully for the upstream hydrocarbon-only sections (V-100, K-101, E-101, C-101 — all appropriately modeled with PR, consistent with Section 3.3 of this guide) into the TEG contactor and regeneration section as well, rather than switching to a glycol-appropriate activity-coefficient package.

### 12.2 Problem Identified

During a routine design review (Section 7.1's "compare against something independent" principle, applied here as a peer review rather than a hand calculation), a senior process engineer familiar with dehydration unit design flagged that the contactor's predicted water dew point suppression looked **too optimistic** relative to typical TEG contactor performance for the stated lean TEG concentration and number of trays — Peng-Robinson, built and tuned for hydrocarbon-hydrocarbon and hydrocarbon-light-polar interactions, does not adequately capture the strongly non-ideal water-TEG liquid-phase behavior that governs how effectively the contactor actually dries the gas.

### 12.3 Investigation & Recalculation

The simulation was rerun using an appropriate glycol-specific package (an NRTL-based activity coefficient model with glycol-water interaction parameters, consistent with Section 3.3's guidance) for the dehydration section, while retaining Peng-Robinson for the upstream hydrocarbon-only sections — a mixed-package flowsheet, which most modern simulation platforms support via a "fluid package" boundary between sections.

The corrected simulation predicted a **meaningfully less favorable** water dew point suppression than the original Peng-Robinson-based run for the same contactor tray count and lean TEG circulation rate — the original design would not have met the pipeline water dew point specification as configured.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **Thermodynamic package selection treated as a flowsheet-wide, one-time decision** rather than a section-by-section decision matched to each part of the process's actual fluid chemistry — the engineer selected PR appropriately for the hydrocarbon sections but never revisited that choice specifically for the polar TEG/water system added later in the flowsheet build-out.
2. **No formal package-selection sign-off step** in the project's simulation basis document process — the Simulation Basis Document (Section 9.1) was drafted for the hydrocarbon sections early in the project and never formally revisited/re-approved when the dehydration section was added.

### 12.5 Resolution

- The dehydration section was rebuilt with the appropriate glycol package, and the contactor was re-sized (additional trays and/or increased lean TEG circulation rate) to meet the pipeline water dew point specification under the corrected thermodynamics.
- Because the finding was caught during design review — **before** the mechanical datasheet (companion Mechanical Datasheet guide) and line list (companion Line List guide) were finalized for the contactor — the correction was contained to the simulation and early mechanical sizing, avoiding a much costlier late-stage or post-fabrication correction.
- The project's Simulation Basis Document procedure was updated to require an **explicit, documented thermodynamic package justification for every distinct fluid system/section** in the flowsheet, not a single flowsheet-wide package statement — with a specific sign-off checkbox for any section involving glycols, amines, or other strongly polar/non-ideal chemistry.

### 12.6 Outcome

- The correction was caught early enough to avoid major schedule impact, but the finding prompted a broader review of other units in the company's portfolio using a single hydrocarbon EOS across flowsheets that also included a dehydration or sweetening section — several similar (though smaller) discrepancies were found and corrected proactively.
- The finding was documented as a corporate lessons-learned item: **thermodynamic package selection is a per-section engineering decision requiring explicit justification, not a flowsheet-wide default** — directly reinforcing this guide's Section 3.3 selection criteria and Section 7 validation principles.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A single thermodynamic package appropriate for most of a flowsheet is not automatically appropriate for every section | Require an explicit, documented package justification per distinct fluid system/section, not one flowsheet-wide statement |
| A converged, plausible-looking simulation result provides no built-in warning that the underlying property model doesn't fit the fluid system | Build independent validation (peer review by someone experienced with the specific unit type, or a hand-calc/literature cross-check) into the workflow for every new section type added to a flowsheet |
| Schedule pressure can lead to reusing a "good enough" prior setup rather than re-evaluating a decision that should be section-specific | Add a formal package-selection sign-off step to the Simulation Basis Document process, specifically flagged for polar/non-ideal sections |
| Catching a thermodynamic modeling error early (design review) vs. late (post-fabrication) has a dramatically different cost impact | Treat thermodynamic package selection with the same rigor and early-stage review attention as a relief or settle-out study, not as a background software setting |

---

## 13. Reference Standards & Tools

- **GPSA Engineering Data Book** — widely used reference for gas processing equilibrium data, K-value correlations, and rule-of-thumb cross-checks
- Aspen Technology — **Aspen HYSYS** and **Aspen Plus** documentation (property package theory, unit operation modeling guides)
- Honeywell — **UniSim Design** documentation
- AVEVA (formerly SimSci) — **PRO/II** documentation
- Fenske, M.R. (1932); Underwood, A.J.V. (1948); Gilliland, E.R. (1940) — original shortcut distillation correlations; Eduljee, H.E. (1975) — widely used Gilliland correlation approximation
- Wegstein, J.H. (1958) — original convergence acceleration method for recycle calculations

---

*This guide is a practical study reference combining standard steady-state simulation methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific PVT/composition data, the current version of the simulation software's property packages, and vendor/licensor guarantees. This guide should be read alongside the companion Flare Network Design, Depressurization Calculation, Compressor Settle-Out Calculations, Line List Preparation, Instrumentation Process Datasheet Preparation, Mechanical Datasheet Preparation, and P&ID/PEFS Development study guides, since the steady-state simulation is the source every one of those disciplines' design conditions is ultimately extracted from.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
