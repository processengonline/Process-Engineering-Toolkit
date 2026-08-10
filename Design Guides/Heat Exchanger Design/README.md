# 🌡️ Heat Exchanger Design — Practical Study Guide

> A field-oriented reference covering the core engineering topics in heat exchanger design — combining TEMA/API 660/ASME Section VIII methodology with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Mechanical Datasheet Preparation**, **Steady-State Simulation**, **Flow Assurance**, and **Flare Network Design** study guides — the shell-and-tube cooler E-101 used as this guide's worked example is the same equipment tag referenced (at a summary level) in those companion guides; this guide develops its actual thermal, mechanical, and hydraulic design in full detail.

**Illustrative project used throughout this guide:** E-101, a shell-and-tube cooler using cooling water to cool a light hydrocarbon process stream from 300 °F to 200 °F (the same duty case used in the companion Steady-State Simulation guide's Calc Sheet 8.2) — used to work through the LMTD method, an overall heat transfer coefficient build-up (which reveals that an initially assumed coefficient was too optimistic), a tube-side velocity/hydraulics check, a tube rupture relief scenario, and an air-cooled exchanger fan power example. All numbers below are worked sample calculations for study purposes — always replace with project-specific process data and vendor-confirmed performance.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Fundamentals](#2-fundamentals)
3. [Thermal Design](#3-thermal-design)
4. [Mechanical Design](#4-mechanical-design)
5. [Hydraulic Considerations](#5-hydraulic-considerations)
6. [Special Design Topics](#6-special-design-topics)
7. [Safety & Operability](#7-safety--operability)
8. [Standards & References (Applicable Codes)](#8-standards--references-applicable-codes)
9. [Sample Calculation Sheets](#9-sample-calculation-sheets)
10. [Sample Datasheets](#10-sample-datasheets)
11. [Practical Design Checklist](#11-practical-design-checklist)
12. [Common Field Issues & Lessons Learned](#12-common-field-issues--lessons-learned)
13. [Case Study — E-101 Underperforms After Startup Because U Was Assumed, Not Verified](#13-case-study--e-101-underperforms-after-startup-because-u-was-assumed-not-verified)
14. [Reference Standards](#14-reference-standards)

---

## 1. Design Basis & Assumptions

Heat exchanger design translates a process duty requirement (from the companion Steady-State Simulation guide's heat & mass balance) into an actual piece of mechanical equipment — the point where a simple `Q = m·Cp·ΔT` line item becomes a specific tube count, shell diameter, and TEMA type. Every assumption made along the way (especially the overall heat transfer coefficient) should be treated as provisional until independently verified, which is exactly the theme this guide's Case Study (Section 13) explores.

### 1.1 Process & Equipment Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Equipment | E-101, shell-and-tube cooler | Consistent tag with companion Mechanical Datasheet and Steady-State Simulation guides |
| Service | Process HC cooler, cooling water utility | Shell side: process (hot); Tube side: cooling water (cold) |
| Process (shell side) flow | 50,000 lb/hr | Cp ≈ 0.55 Btu/(lb·°F) |
| Process inlet/outlet temperature | 300 °F → 200 °F | Duty ≈ 2,750,000 Btu/hr (2.75 MMBtu/hr), per companion Steady-State Simulation guide |
| Cooling water (tube side) inlet temperature | 90 °F | Typical CW supply temperature |
| Cooling water flow (design) | 275,000 lb/hr | Cp = 1.0 Btu/(lb·°F); outlet temperature derived in Calc Sheet 9.1 |
| Tube specification | 0.75-in OD, 14 BWG, carbon steel | Consistent with companion Mechanical Datasheet guide's illustrative E-101 datasheet |
| Tube length | 16 ft | Standard tube length |
| TEMA type (initial) | AES (2 tube passes) | Reassessed in Calc Sheet 9.3 |
| Tube-side design pressure | 150 psig | Used in Calc Sheet 9.4 |
| Shell-side design pressure | 75 psig | Used in Calc Sheet 9.4 |

### 1.2 Codes & Standards / Methodology Basis
- **TEMA** (Tubular Exchanger Manufacturers Association) — mechanical design standards, shell type designations (E, F, K, etc.), tube layout and pitch conventions
- **API 660** — shell-and-tube heat exchangers for general refinery service, supplementing TEMA with additional refinery-specific requirements
- **ASME BPVC Section VIII, Division 1** — pressure vessel code governing the exchanger's pressure boundary (shell and channel), consistent with the companion Mechanical Datasheet guide's methodology
- **HEI Standards** (Heat Exchange Institute) — air-cooled heat exchangers and other specialized equipment
- **API 521** — tube rupture relief scenario guidance (companion Flare Network Design and Depressurization Calculation guides' relief methodology, applied here to the tube rupture case specifically)

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Overall heat transfer coefficient, first-pass estimate | Rule-of-thumb/prior-project value (e.g., 100 Btu/hr·ft²·°F for this service) | Must always be independently verified via a film-coefficient build-up — see Calc Sheet 9.2 and Case Study, Section 13 |
| Design area margin over the rigorously calculated requirement | 10–15% | Confirm project-specific margin philosophy; too little margin risks underperformance, too much adds unnecessary cost |
| Fouling resistance (process HC, shell side) | 0.002 hr·ft²·°F/Btu | TEMA-typical value for a moderately fouling hydrocarbon; confirm against actual fluid fouling tendency (companion Flow Assurance guide's wax/asphaltene deposition discussion is relevant for heavier or waxy crudes) |
| Fouling resistance (cooling water, tube side) | 0.002 hr·ft²·°F/Btu | TEMA-typical value; brackish or seawater cooling requires a higher allowance |
| Tube-side velocity limit (carbon steel tubes, cooling water) | ≤8 ft/s (erosion/corrosion guideline) | HEI/TEMA-typical; confirm against project material and water quality specifics |
| Tube rupture relief basis | Flow through 2× a single tube's cross-sectional area, per API 521 | Section 7.2, Calc Sheet 9.4 |

> ⚠️ **Practical note:** The single most consequential assumption in this entire guide is the overall heat transfer coefficient used for the first-pass area estimate — a value borrowed from a "similar" prior project without independently verifying it against this specific service's actual film coefficients and fouling resistances is one of the most common and costly sources of an underperforming exchanger, exactly the finding worked through in Calc Sheet 9.2 and the Case Study (Section 13).

---

## 2. Fundamentals

### 2.1 Types of Exchangers
| Type | Characteristics |
|---|---|
| **Shell-and-tube** | Most common in process industry; robust, widely understood, TEMA-standardized; this guide's primary worked example (E-101) |
| **Plate** | Compact, high heat transfer coefficient, easily expandable by adding plates; limited by gasket temperature/pressure and fluid compatibility (Section 6.2) |
| **Air-cooled** | No cooling water required; used where water is scarce/expensive or to reduce cooling water system load; worked example in Calc Sheet 9.5 |
| **Spiral** | Self-cleaning (single continuous flow channel), good for fouling/viscous/slurry services |
| **Double-pipe** | Simple, small duty, good for high-pressure service or where only a small area is needed (Section 6.4) |

### 2.2 Applications
Process heating/cooling (E-101's service), condensing (Section 3.5), reboiling (companion Steady-State Simulation guide's column modeling, Section 4.2 of that guide), and economizers (heat recovery, preheating a cold stream against a hot stream that would otherwise be cooled by utility alone).

### 2.3 Design Basis
- **Duty (Q)** — from the process heat & mass balance (companion Steady-State Simulation guide)
- **Temperature approach** — the minimum temperature difference between hot and cold streams, a key economic/area trade-off (a tighter approach requires more area for the same duty)
- **Allowable pressure drop** — process-side and utility-side limits (Section 5.1), which directly constrain the mechanical configuration (tube passes, baffle spacing)

---

## 3. Thermal Design

### 3.1 Heat Transfer Equation
The fundamental relationship linking duty, area, and driving temperature difference:
```
Q = U × A × ΔT_lm × F
```
where U = overall heat transfer coefficient, A = heat transfer area, ΔT_lm = log mean temperature difference, and F = a correction factor accounting for the actual flow arrangement (not pure countercurrent) — see Calc Sheet 9.1.

### 3.2 Log Mean Temperature Difference (LMTD) Method
The standard method for sizing simple exchangers with known inlet/outlet temperatures on both sides — worked through in full in Calc Sheet 9.1, including the correction factor for a real (not purely countercurrent) shell-and-tube flow arrangement.

### 3.3 Effectiveness-NTU Method
Preferred over LMTD for cases where outlet temperatures aren't known in advance (e.g., rating an existing exchanger against a new duty, or where one stream's outlet temperature is itself the unknown being solved for) — expresses performance in terms of effectiveness (ε) and Number of Transfer Units (NTU) rather than requiring iterative LMTD solving. Not worked in detail in this guide's calc sheets (LMTD is used throughout, since E-101's example has known inlet/outlet temperatures), but essential for rating/simulation-embedded exchanger models (companion Steady-State Simulation guide's Section 4.2).

### 3.4 Fouling Factors
Allowances added to the clean heat transfer resistance to account for the inevitable buildup of deposits over the exchanger's service life — service-specific (Section 1.3 table gives typical values for this guide's HC/cooling-water service); heavier or dirtier services (crude oil, untreated seawater, glycol-rich streams) require substantially higher fouling allowances than the values used in this guide's clean liquid/water example.

### 3.5 Phase Change Considerations
Condensation and boiling (reboiling) introduce latent heat effects that dominate the duty calculation (`Q = m × λ` for the phase-change portion, vs. `Q = m × Cp × ΔT` for sensible heat) and require different film-coefficient correlations than single-phase liquid or vapor flow — not worked in detail in this guide's calc sheets (E-101's example is single-phase sensible cooling on both sides), but essential for condensers/reboilers, which also introduce the two-phase hydraulic considerations discussed in Section 5.4.

---

## 4. Mechanical Design

### 4.1 Shell-and-Tube Geometry — TEMA Standards
TEMA designates shell types by letter (E = one-pass shell, the most common; F = two-pass shell with a longitudinal baffle; K = kettle reboiler, with an enlarged vapor disengagement space) and front/rear head types, combining into a three-letter TEMA type designation (e.g., AES). Tube layout (triangular, square, rotated square) and pitch affect both thermal performance (turbulence, fouling accessibility) and shell diameter for a given tube count — see Calc Sheet 9.2 for a worked shell diameter estimate.

### 4.2 Pressure Vessel Codes — ASME Section VIII
The exchanger's shell and channel pressure boundary is designed per ASME Section VIII Division 1, using the same methodology (shell/head thickness, nozzle reinforcement, MAWP, hydrotest) detailed in the companion Mechanical Datasheet guide (that guide's Calc Sheets 10.1–10.6), applied here to the exchanger's shell and channel components specifically rather than a simple vessel.

### 4.3 Nozzle Sizing and Orientation
Shell and tube-side nozzles are sized against an acceptable inlet/outlet velocity (avoiding both excessive pressure drop and impingement erosion at the nozzle) and oriented per the plot plan and piping routing (companion Line List Preparation and P&ID/PEFS Development guides).

### 4.4 Tube Material Selection
| Material | Typical Use |
|---|---|
| Carbon steel | Non-corrosive service, moderate cost — this guide's E-101 example |
| Stainless steel | Corrosive or sour service (companion Flow Assurance guide's corrosion screening), or where product purity matters |
| Cu-Ni (copper-nickel) | Seawater cooling — good biofouling and corrosion resistance |
| Titanium | Aggressive seawater/brine service, or where CU-Ni is inadequate — higher cost, excellent corrosion resistance |

### 4.5 Thermal Expansion and Tube Stress Analysis
A significant temperature difference between the shell and tubes (e.g., a large ΔT service, or startup/shutdown transients) induces differential thermal expansion between the shell and tube bundle — for a fixed-tubesheet design (no provision for differential movement), this must be checked against allowable stress; where the differential is too large, an expansion joint (in the shell) or a floating-head/U-tube design (allowing the bundle to move independently of the shell) is required instead.

---

## 5. Hydraulic Considerations

### 5.1 Pressure Drop Limits
Both the process side and the utility side typically have an allowable pressure drop limit — process-side ΔP is often constrained by the upstream pump/compressor's available head (companion Line List Preparation guide's Calc Sheet 9.1 pump dead-head logic is directly relevant here), while utility-side (cooling water) ΔP is constrained by the cooling water system's available supply pressure and the broader utility philosophy (companion Process Philosophies guide, Section 3).

### 5.2 Flow Distribution
Baffle spacing/type (shell side) and tube pass/channel design (tube side) govern how evenly flow is distributed across the exchanger — poor distribution creates dead zones (accelerating fouling) and reduces effective heat transfer area below the nominal geometric area.

### 5.3 Velocity Limits
Both shell-side and tube-side velocities must stay within limits that avoid excessive erosion/corrosion (too high) or excessive fouling/poor heat transfer (too low) — see Calc Sheet 9.3 for a worked tube-side velocity check that finds an initial configuration exceeds the erosion guideline.

### 5.4 Two-Phase Hydraulics
Condensers and reboilers (Section 3.5) require careful vapor-liquid flow distribution design — maldistribution in a condenser can create localized flooding or vapor blow-through, and in a reboiler can create localized dryout (loss of nucleate boiling, risking tube wall overheating) — a more specialized topic requiring dedicated two-phase flow correlations beyond this guide's single-phase worked examples.

---

## 6. Special Design Topics

### 6.1 Air-Cooled Exchangers
Fan sizing (Calc Sheet 9.5), noise (a real siting/community consideration, especially for large installations), and plot space (air-cooled exchangers require substantially more plot area than an equivalent-duty shell-and-tube water-cooled exchanger) are the key differentiating design considerations versus a water-cooled exchanger.

### 6.2 Plate Exchangers
Compact design (much higher area density than shell-and-tube) comes with a key constraint: **gasket compatibility** — the elastomer gasket sealing each plate must be chemically compatible with the process fluid and rated for the service temperature/pressure, which can rule out plate exchangers for aggressive or high-temperature services where a shell-and-tube design (with no gasket exposed to the process, for a welded/fixed design) would be unaffected.

### 6.3 Cryogenic Exchangers
Brazed aluminum plate-fin exchangers are the standard for LNG and other cryogenic services — offering very high area density and good low-temperature performance, but requiring careful attention to differential thermal contraction during cooldown (consistent with the companion Flow Assurance guide's Joule-Thomson cooling discussion, Section 4.2 of that guide, for the magnitude of temperature change involved) and MDMT-equivalent material qualification for aluminum at cryogenic temperatures.

### 6.4 Double-Pipe Exchangers
Simple, robust, well-suited to small duty or high-pressure service (the annular/inner-pipe construction handles high pressure more naturally than a large-diameter shell) — often used for a single, small, high-pressure duty where a full shell-and-tube exchanger would be disproportionately complex.

---

## 7. Safety & Operability

### 7.1 Relief Scenarios
- **Blocked outlet** — a downstream block valve inadvertently closed while the exchanger continues to receive flow (or is exposed to fire/thermal expansion of a trapped liquid), requiring PSV protection sized per the companion Flare Network Design guide's methodology.
- **Tube rupture** — a failed tube creates a direct path between the (typically higher-pressure) tube side and the (typically lower-pressure) shell side, potentially overpressuring the shell beyond its design rating — see Calc Sheet 9.4 for a worked example.

### 7.2 Tube Rupture Analysis — API 521 Guidance
API 521 provides a standard rule-of-thumb basis for tube rupture relief sizing: assume flow through an effective area equal to **twice** a single tube's cross-sectional flow area (accounting for both the direct rupture opening and the potential for flow reversal/additional tube damage), discharging from the high-pressure side into the low-pressure side — this flow becomes an additional relief case the shell-side (or tube-side, whichever is lower-rated) PSV must be checked against, potentially governing over other relief cases. Worked in full in Calc Sheet 9.4.

### 7.3 Maintenance Considerations
Fouling accumulation drives cleaning frequency — removable bundle designs (floating head, U-tube) allow mechanical cleaning of the shell side; fixed-tubesheet designs are limited to chemical cleaning or tube-side mechanical cleaning (pigging/rodding) only, which should be considered explicitly when the shell-side fluid has meaningful fouling tendency (Section 3.4).

### 7.4 Isolation and Bypass Arrangements
Block valves and (where operationally justified) a bypass line around the exchanger allow maintenance/cleaning without a full process shutdown — consistent with the companion Process Philosophies guide's isolation philosophy (Section 6 of that guide), and the companion P&ID/PEFS Development guide's three-valve control-station bypass concept (that guide's Section 9.4 detailed example) applied here to exchanger isolation rather than a control valve.

---

## 8. Standards & References (Applicable Codes)

- **TEMA** — mechanical design standard for shell-and-tube exchangers (shell type designation, tube layout/pitch, baffle design)
- **API 660** — supplements TEMA with additional refinery/process-industry-specific requirements for shell-and-tube exchangers
- **ASME Section VIII** — pressure vessel code governing the exchanger's pressure boundary (Section 4.2 above)
- **HEI Standards** — air-cooled heat exchanger design standards (Section 6.1)

---

## 9. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific process data and vendor-confirmed performance.

### 9.1 Calc Sheet 1 — LMTD Method & First-Pass Required Area

**Given:** Shell side (hot, process): W = 50,000 lb/hr, Cp = 0.55 Btu/(lb·°F), Thi = 300°F, Tho = 200°F, Q = 2,750,000 Btu/hr. Tube side (cold, cooling water): W = 275,000 lb/hr, Cp = 1.0 Btu/(lb·°F), Tci = 90°F. First-pass assumed overall coefficient, U = 100 Btu/(hr·ft²·°F) (Section 1.3).

**Step 1 — Cooling water outlet temperature (energy balance):**
```
Tco = Tci + Q/(W×Cp) = 90 + 2,750,000/(275,000×1.0) = 90 + 10 = 100°F
```

**Step 2 — Countercurrent LMTD:**
```
ΔT1 = Thi − Tco = 300 − 100 = 200°F
ΔT2 = Tho − Tci = 200 − 90 = 110°F
LMTD = (ΔT1 − ΔT2)/ln(ΔT1/ΔT2) = (200−110)/ln(200/110) = 90/0.598 ≈ 150.5°F
```

**Step 3 — Correction factor, F (1 shell pass, 2 tube passes):**
```
R = (Thi−Tho)/(Tco−Tci) = 100/10 = 10.0
P = (Tco−Tci)/(Thi−Tci) = 10/210 ≈ 0.0476

For R=10, P=0.0476 (small P), F ≈ 0.97 (read from standard 1-2 TEMA correction chart)
```

**Step 4 — Corrected LMTD and required area:**
```
ΔT_corrected = F × LMTD = 0.97 × 150.5 ≈ 146.0°F
A_required = Q/(U × ΔT_corrected) = 2,750,000/(100 × 146.0) ≈ 188.4 ft²
```

**Result:** First-pass required area ≈ **188.4 ft²**, using the assumed U = 100. This suggests a tentative layout of roughly 60 tubes (0.75-in OD × 16 ft) — but this result should **not** be finalized until U is independently verified (Calc Sheet 9.2), since it depends entirely on the assumed coefficient.

> 📌 **Assumption check:** This first-pass estimate is only as good as the assumed U — treat it as a starting point for the mechanical layout, not a final answer, consistent with this guide's Section 1.3 practical note.

---

### 9.2 Calc Sheet 2 — Overall U Verification, Final Tube Count & Shell Sizing

**Given:** Film coefficients (from correlations or vendor software, illustrative): shell-side process HC, ho = 150 Btu/(hr·ft²·°F); tube-side cooling water, hi = 800 Btu/(hr·ft²·°F). Fouling resistances: shell side Rfo = 0.002, tube side Rfi = 0.002 hr·ft²·°F/Btu (Section 1.3). Tube: OD = 0.75 in (0.0625 ft), 14 BWG wall (0.083 in), ID = 0.584 in (0.04867 ft), kwall (carbon steel) ≈ 26 Btu/(hr·ft·°F).

**Step 1 — Tube wall resistance (outside-area basis):**
```
Rwall = [do × ln(do/di)] / (2 × kwall)
do/di = 0.75/0.584 = 1.284
Rwall = [0.0625 × ln(1.284)] / (2×26) = [0.0625 × 0.250] / 52 ≈ 0.0003 hr·ft²·°F/Btu
```

**Step 2 — Build up 1/Uo (outside-area basis), converting tube-side terms by (do/di):**
```
1/Uo = 1/ho + Rfo + Rwall + Rfi×(do/di) + (1/hi)×(do/di)

1/ho = 1/150 = 0.006667
Rfo = 0.002000
Rwall = 0.000300
Rfi×(do/di) = 0.002×1.284 = 0.002568
(1/hi)×(do/di) = (1/800)×1.284 = 0.001605

1/Uo = 0.006667+0.002000+0.000300+0.002568+0.001605 = 0.013140
```

**Step 3 — Overall coefficient:**
```
Uo = 1/0.013140 ≈ 76.1 Btu/(hr·ft²·°F)
```

**Step 4 — Compare to the Calc Sheet 9.1 assumed value:**
```
Assumed U (100) vs. Verified U (76.1)  →  Assumed value was ~31% too optimistic
```

**Step 5 — Recalculate required area with the verified U:**
```
A_required = Q/(U×ΔT_corrected) = 2,750,000/(76.1×146.0) ≈ 247.5 ft²
```

**Step 6 — Compare to the tentative 60-tube layout from Calc Sheet 9.1:**
```
Tentative area (60 tubes × π × 0.0625 ft × 16 ft ≈ 188.5 ft²) < 247.5 ft² required  →  FAIL
```

**Step 7 — Resize: select tube count for adequate margin:**
```
Trial: 88 tubes → A = 88 × π × 0.0625 × 16 ≈ 276.5 ft²
Margin = (276.5 − 247.5)/247.5 ≈ 11.7%  →  Acceptable (Section 1.3 target 10–15%)
```

**Step 8 — Estimate shell diameter for 88 tubes (Kern's method approximation, triangular pitch, 2 passes):**
```
Db = do × (Nt/K1)^(1/n1),  K1=0.249, n1=2.207 (typical constants, 2-pass triangular)
Db = 0.75 × (88/0.249)^(1/2.207) = 0.75 × (353.4)^0.4531 ≈ 0.75 × 14.28 ≈ 10.71 in

Shell ID = Db + clearance (≈0.5 in, fixed tubesheet) ≈ 11.2 in → round to standard 12-in shell
```

**Result:** The rigorously verified U (76.1, not the initially assumed 100) requires **88 tubes** (not 60) for adequate margin, housed in a **≈12-inch shell**. This is a direct, worked illustration of why the overall coefficient must be independently built up from film coefficients and fouling resistances, not assumed from a rule of thumb, before finalizing tube count.

> 📌 **Assumption check:** Film coefficients (ho, hi) here are illustrative — in practice these come from validated correlations (e.g., Kern or Bell-Delaware methods for shell-side, Dittus-Boelter or similar for tube-side turbulent flow) or vendor thermal-rating software, which also account for baffle geometry and tube layout effects this simplified hand calc does not capture.

---

### 9.3 Calc Sheet 3 — Tube-Side Velocity Check

**Given:** Cooling water flow = 275,000 lb/hr, ρ_water ≈ 62 lb/ft³, tube ID = 0.04867 ft, 88 tubes (Calc Sheet 9.2), 2 tube passes (44 tubes per pass). Velocity limit ≤8 ft/s (Section 1.3).

**Step 1 — Volumetric flow:**
```
Q_v = 275,000/62 ≈ 4,435 ft³/hr ≈ 1.232 ft³/s
```

**Step 2 — Flow area per pass (2-pass configuration, 44 tubes/pass):**
```
A_per_pass = 44 × (π/4) × (0.04867)² = 44 × 0.001860 ≈ 0.0818 ft²
```

**Step 3 — Velocity (2-pass configuration):**
```
V = Q_v/A_per_pass = 1.232/0.0818 ≈ 15.1 ft/s
```

**Step 4 — Compare to limit:**
```
15.1 ft/s > 8 ft/s limit  →  FAIL
```

**Step 5 — Evaluate a single-pass configuration instead (all 88 tubes carrying flow simultaneously):**
```
A_single_pass = 88 × 0.001860 ≈ 0.1637 ft²
V = 1.232/0.1637 ≈ 7.5 ft/s  →  PASS (within 8 ft/s limit)
```

**Result:** The initially assumed **2-tube-pass** configuration produces an excessive tube-side velocity (15.1 ft/s), risking erosion/corrosion in the carbon steel tubes. Reconfiguring to a **single tube pass** (requiring a different TEMA head type — e.g., a U-tube or single-pass floating head arrangement, rather than the initially assumed 2-pass AES) brings velocity down to an acceptable 7.5 ft/s.

> 📌 **Assumption check:** Switching pass configuration also changes the exchanger's true LMTD correction factor and flow arrangement — Calc Sheet 9.1's F-factor and area calculation should, strictly, be revisited for the final single-pass configuration; for this near-countercurrent, small-P case the impact is expected to be minor, but should be confirmed rather than assumed.

---

### 9.4 Calc Sheet 4 — Tube Rupture Relief Scenario (API 521)

**Given:** Tube-side (cooling water) design pressure = 150 psig; shell-side (process) design pressure = 75 psig (Section 1.1) — a credible tube rupture would drive high-pressure water into the lower-rated shell side. Tube ID = 0.04867 ft (0.584 in). Discharge coefficient Cd = 0.65 (sharp-edged orifice approximation). ρ_water ≈ 62 lb/ft³.

**Step 1 — Tube cross-sectional flow area:**
```
A_tube = (π/4) × (0.04867)² ≈ 0.001860 ft²
```

**Step 2 — API 521 rupture relief area (2× single tube area):**
```
A_rupture = 2 × 0.001860 = 0.003720 ft² (≈0.536 in²)
```

**Step 3 — Driving pressure differential:**
```
ΔP = 150 − 75 = 75 psi = 75 × 144 = 10,800 lb/ft²
```

**Step 4 — Liquid orifice flow rate:**
```
Q(ft³/s) = Cd × A × √(2×ΔP×gc/ρ)
√(2×10,800×32.2/62) = √(695,520/62) = √11,218 ≈ 105.9 ft/s

Q = 0.65 × 0.003720 × 105.9 ≈ 0.2558 ft³/s ≈ 920.9 ft³/hr
```

**Step 5 — Convert to mass flow:**
```
W = 920.9 × 62 ≈ 57,100 lb/hr
```

**Step 6 — Compare to the shell side's other governing relief case (illustrative, blocked outlet = 40,000 lb/hr):**
```
Tube rupture case (57,100 lb/hr) > Blocked outlet case (40,000 lb/hr)  →  Tube rupture GOVERNS
```

**Result:** The tube rupture scenario produces a relief load (**≈57,100 lb/hr**) that **exceeds** the previously-governing blocked outlet case — the shell-side PSV must be sized (or re-verified, per the companion Flare Network Design guide's API 520 orifice sizing methodology, that guide's Calc Sheet 8.4) against this larger tube rupture flow, not the smaller blocked outlet case alone.

> 📌 **Assumption check:** This is a screening-level liquid orifice flow estimate — a rigorous tube rupture study should also confirm whether flashing occurs as the high-pressure water discharges into the lower-pressure shell side (which would change the relief flow calculation to a two-phase basis) and should check the shell side's transient pressure response, not just the steady relief flow rate.

---

### 9.5 Calc Sheet 5 — Air-Cooled Exchanger Fan Power (Special Design Topics)

**Given:** A separate air-cooled exchanger (illustrative, different service), duty Q = 5,000,000 Btu/hr, air inlet 95°F, air outlet 130°F (ΔT = 35°F), air density ρ = 0.071 lb/ft³, Cp_air = 0.24 Btu/(lb·°F), fan static pressure requirement = 0.5 in H₂O, fan mechanical efficiency = 70%, 2 fans per bay.

**Step 1 — Required air mass flow:**
```
W_air = Q/(Cp×ΔT) = 5,000,000/(0.24×35) = 5,000,000/8.4 ≈ 595,238 lb/hr
```

**Step 2 — Air volumetric flow:**
```
Q_v = 595,238/0.071 ≈ 8,383,634 ft³/hr ≈ 139,727 ACFM
```

**Step 3 — Theoretical (air) fan power:**
```
Air power (HP) = ACFM × ΔP(in H₂O) / 6,356
Air power = 139,727 × 0.5 / 6,356 ≈ 11.0 HP
```

**Step 4 — Actual brake power (apply fan efficiency):**
```
Brake power = 11.0/0.70 ≈ 15.7 HP total
```

**Step 5 — Per-fan power (2 fans per bay):**
```
Per fan ≈ 15.7/2 ≈ 7.85 HP → select a standard 10 HP motor per fan
```

**Result:** This air-cooled exchanger requires **≈15.7 HP** total fan brake power, split across 2 fans at **≈7.85 HP each** — round up to standard **10 HP motors**. This figure feeds directly into the electrical/utility load summary (companion Process Philosophies guide's utility balance methodology, that guide's Calc Sheet 8.5 approach, applied to electrical load rather than steam).

> 📌 **Assumption check:** This simplified calc uses a single average static pressure requirement — a full ACHE design also accounts for the fan's actual performance curve (static pressure vs. airflow, not a single point), air density variation with elevation/temperature, and noise constraints (Section 6.1), which can all affect the final fan/motor selection.

---

## 10. Sample Datasheets

### 10.1 TEMA-Style Heat Exchanger Data Sheet — E-101

| Field | Shell Side (Process) | Tube Side (Cooling Water) |
|---|---|---|
| **Fluid** | Light hydrocarbon liquid | Cooling water |
| **Flow Rate** | 50,000 lb/hr | 275,000 lb/hr |
| **Temperature In / Out** | 300 °F / 200 °F | 90 °F / 100 °F |
| **Operating Pressure** | 60 psig | 120 psig |
| **Design Pressure** | 75 psig | 150 psig |
| **Design Temperature** | 350 °F | 150 °F |
| **Allowable Pressure Drop** | 10 psi | 8 psi |
| **Fouling Resistance** | 0.002 hr·ft²·°F/Btu | 0.002 hr·ft²·°F/Btu |
| **Heat Exchanged, Q** | 2,750,000 Btu/hr | — |
| **MTD (Corrected)** | 146.0 °F | — |
| **Transfer Rate, Service (Uo)** | 76.1 Btu/(hr·ft²·°F) | — |
| **Surface Area (installed)** | 276.5 ft² | — |
| **Design Margin** | 11.7% | — |
| **TEMA Type** | BEU (single tube pass, U-tube, per Calc Sheet 9.3 resolution) | — |
| **Shell ID** | 12 in | — |
| **Tube: No. / OD / BWG / Length / Pitch** | 88 / 0.75 in / 14 / 16 ft / 1-in triangular | — |
| **Material — Shell / Tube** | SA-516 Gr. 70 / Carbon steel | — |
| **Applicable Codes** | ASME Section VIII Div. 1, TEMA, API 660 | — |

---

### 10.2 Tube Rupture Relief Summary

| Parameter | Value |
|---|---|
| Rupture relief area (2× tube CSA) | 0.536 in² |
| Driving ΔP (tube side − shell side design) | 75 psi |
| Calculated relief flow | 57,100 lb/hr |
| Governing case vs. blocked outlet (40,000 lb/hr) | Tube rupture governs |
| Action | Re-verify/resize shell-side PSV per companion Flare Network Design guide methodology |

---

### 10.3 Air-Cooled Exchanger Datasheet (Secondary Example)

| Parameter | Value |
|---|---|
| Duty | 5,000,000 Btu/hr |
| Air inlet / outlet temperature | 95 °F / 130 °F |
| Air mass flow | 595,238 lb/hr |
| Fan airflow (ACFM) | 139,727 |
| Fan static pressure | 0.5 in H₂O |
| Fan efficiency | 70% |
| Total brake power | 15.7 HP |
| Fans per bay / motor size each | 2 / 10 HP |
| Applicable standard | HEI Standards for Air-Cooled Heat Exchangers |

---

## 11. Practical Design Checklist

- [ ] Process duty, temperatures, and flow rates confirmed against the current heat & mass balance (companion Steady-State Simulation guide), not an outdated case
- [ ] LMTD (or effectiveness-NTU) method applied correctly, including the flow-arrangement correction factor F — see Calc Sheet 9.1
- [ ] Overall heat transfer coefficient independently built up from film coefficients and fouling resistances — never left at an assumed/rule-of-thumb value for final design — see Calc Sheet 9.2
- [ ] Design area margin (10–15%, Section 1.3) applied against the verified (not assumed) required area
- [ ] Tube-side and shell-side velocities checked against erosion/corrosion limits — see Calc Sheet 9.3
- [ ] TEMA type and tube pass configuration finalized only after the velocity check, not fixed early and left unverified
- [ ] Nozzle sizing checked against acceptable inlet/outlet velocity and impingement risk
- [ ] Tube material selected against actual service corrosivity (companion Flow Assurance guide's screening methodology)
- [ ] Thermal expansion/differential movement checked, with expansion joint or floating-head/U-tube design specified where required
- [ ] Tube rupture relief scenario explicitly evaluated and compared against other governing relief cases — see Calc Sheet 9.4
- [ ] Isolation and bypass arrangement specified consistent with the project's isolation philosophy (companion Process Philosophies guide)
- [ ] For air-cooled exchangers: fan power, noise, and plot space explicitly checked — see Calc Sheet 9.5

---

## 12. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Exchanger fails to achieve design outlet temperature after startup | Overall U assumed from a rule of thumb, never independently verified against actual film coefficients/fouling | Always build up U from first principles or vendor software — see Calc Sheet 9.2 and Case Study, Section 13 |
| Tube erosion/thinning found during inspection well before expected | Tube-side velocity exceeded the erosion guideline in the as-built configuration | Explicitly check velocity for the actual final pass configuration — see Calc Sheet 9.3 |
| Shell-side PSV found undersized during a later relief study | Tube rupture scenario never evaluated as a distinct relief case | Explicitly calculate and compare the tube rupture case against other relief scenarios — see Calc Sheet 9.4 |
| Excessive fouling/short run length between cleanings | Fouling resistance assumption too low for the actual fluid's real fouling tendency | Confirm fouling factors against actual fluid characterization (companion Flow Assurance guide), not a generic TEMA table value alone for unusually fouling services |
| Air-cooled exchanger noise complaint after startup | Fan noise not explicitly evaluated against site/community limits during design | Include noise as an explicit design check for air-cooled equipment, not just fan power/plot space |

---

## 13. Case Study — E-101 Underperforms After Startup Because U Was Assumed, Not Verified

> A composite, illustrative case study based on the type of finding commonly encountered during heat exchanger commissioning. Names, tag numbers, and figures are representative, not project-specific.

### 13.1 Background

E-101 (this guide's running example) was specified during an early design phase using a first-pass required-area estimate based on an assumed overall coefficient, U = 100 Btu/(hr·ft²·°F) — a value the process engineer carried over from a "similar" cooler on a prior project, without independently building it up from film coefficients and fouling resistances for this specific service (exactly the Calc Sheet 9.1 result in this guide). The resulting tentative 60-tube layout was passed to the exchanger vendor as a target, and — under schedule pressure, and without a formal thermal rating cross-check by the buyer's own engineering team — the vendor's quoted design was accepted close to this tentative tube count.

### 13.2 Problem Identified

After startup, E-101 was unable to cool the process stream to its 200°F target — operating data showed the process outlet stabilizing around 215–220°F, several degrees above the design target, with the cooling water side operating essentially as expected. This directly reduced downstream unit performance (the warmer stream fed forward into equipment sized for the original 200°F target).

### 13.3 Investigation & Recalculation

The process engineering team reran the thermal design from first principles, using this guide's Calc Sheet 9.2 methodology — building up the overall coefficient from actual film coefficients (shell-side process HC, tube-side cooling water) and TEMA-typical fouling resistances for this specific service, rather than the originally assumed rule-of-thumb value. The rigorous build-up gave **U ≈ 76.1 Btu/(hr·ft²·°F)** — roughly 24% lower than the originally assumed 100 — confirming that the as-built 60-tube exchanger had materially less area than the service actually required (consistent with this guide's Calc Sheet 9.2 finding that 88 tubes, not 60, would have been needed for adequate margin).

### 13.4 Root Cause

Two compounding root causes were identified:
1. **An assumed, unverified overall coefficient was used for the actual procurement specification**, not just an early conceptual screening estimate — the "prior project" value was reasonable as a very early rough-cut, but was never revisited with a proper film-coefficient build-up before being sent to the vendor as the design target.
2. **No independent thermal rating cross-check was performed on the vendor's quoted design** before order placement — a standard buyer-side practice (rating the vendor's proposed tube count/geometry against the buyer's own independently-calculated required area) that, had it been performed, would have caught the area shortfall before fabrication, not after startup.

### 13.5 Resolution

- Given the exchanger was already fabricated and installed, a full area increase (more tubes) was not practical without a shell replacement; the resolution instead focused on maximizing achievable performance within the existing shell: confirming cooling water flow was at its design maximum (verified acceptable, per Calc Sheet 9.3's velocity check headroom), and evaluating whether a modest cooling water supply temperature reduction (via the broader utility system, companion Process Philosophies guide's utility philosophy) could partially compensate for the area shortfall.
- A supplementary trim cooler was ultimately added downstream to recover the remaining temperature gap to the original 200°F target, at additional capital cost that a correctly-sized original E-101 would have avoided entirely.
- The company's exchanger specification procedure was updated to require: **every overall heat transfer coefficient used in a procurement specification must be independently built up from film coefficients and fouling resistances (or validated vendor software output) and documented**, and **every vendor-quoted thermal design must be independently rated by the buyer's own engineering team before order placement** — both as mandatory, logged steps, not assumed to be redundant with the vendor's own design responsibility.

### 13.6 Outcome

- The supplementary trim cooler resolved the immediate performance gap, but at a real, avoidable capital cost and schedule delay compared to specifying E-101 correctly the first time.
- The finding was documented as a corporate lessons-learned item, reinforcing this guide's Section 1.3 opening practical note: an assumed overall coefficient is the single most consequential unverified assumption in heat exchanger design, and it deserves the same rigor as any other safety- or performance-critical calculation in this guide series, not the informal "rule of thumb, revisit later" treatment it received here.

### 13.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| An assumed overall coefficient, adequate for very early conceptual screening, is not adequate for a procurement specification | Require an independently built-up U (Calc Sheet 9.2 methodology) before issuing any exchanger for vendor quotation |
| A vendor's quoted thermal design should not be accepted without an independent buyer-side rating check | Make independent thermal rating verification a mandatory, logged step before order placement, not an assumed redundancy |
| Correcting an undersized exchanger after fabrication is far costlier than specifying it correctly the first time | Treat the thermal design calculation with the same rigor and review discipline as a safety-critical calculation, given the real downstream cost of getting it wrong |
| A "similar" prior-project value is a reasonable starting point but not a substitute for a service-specific verification | Apply the same "don't assume, verify" discipline seen in the nozzle reinforcement, line list, and process philosophy case studies elsewhere in this guide series |

---

## 14. Reference Standards

- **TEMA** — Standards of the Tubular Exchanger Manufacturers Association
- **API 660** — Shell-and-Tube Heat Exchangers for General Refinery Service
- **ASME BPVC Section VIII, Division 1** — Rules for Construction of Pressure Vessels
- **HEI Standards** — Standards for Air Cooled Heat Exchangers (Heat Exchange Institute)
- **API RP 521** — Pressure-relieving and Depressuring Systems (tube rupture relief basis)

---

*This guide is a practical study reference combining standard heat exchanger design methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific process data, the current edition of the referenced codes, and vendor-confirmed thermal/mechanical performance. This guide should be read alongside the companion Mechanical Datasheet Preparation, Steady-State Simulation, Flow Assurance, Flare Network Design, and Process Philosophies study guides, since heat exchanger design draws directly on the process duty, mechanical code, corrosion/fouling, and relief methodology those guides establish in detail.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
