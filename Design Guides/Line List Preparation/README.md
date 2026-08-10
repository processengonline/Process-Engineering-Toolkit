# 📋 Line List Preparation — Practical Study Guide

> A field-oriented reference covering the core engineering topics in piping line list preparation — combining ASME B31.3 and standard piping engineering practice with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design**, **Depressurization Calculation**, and **Compressor Settle-Out Calculations** study guides — the line list is the document that ultimately records and carries forward the design pressures/temperatures those other studies establish.

**Illustrative project used throughout this guide:** a 6-inch carbon steel pump discharge line from a suction vessel to a downstream vessel, used to work through design pressure/temperature determination, piping class assignment, wall thickness calculation, and personnel-protection insulation sizing. All numbers below are worked sample calculations for study purposes — always replace with project-specific equipment data and the project piping material specification (PMS).

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Fundamentals & Purpose of the Line List](#2-fundamentals--purpose-of-the-line-list)
3. [Line Numbering & Designation Philosophy](#3-line-numbering--designation-philosophy)
4. [Line List Data Fields & Content](#4-line-list-data-fields--content)
5. [Piping Class / Material Selection Basis](#5-piping-class--material-selection-basis)
6. [Design Pressure & Temperature Determination](#6-design-pressure--temperature-determination)
7. [Insulation, Heat Tracing & PWHT Requirements](#7-insulation-heat-tracing--pwht-requirements)
8. [Line List Development Workflow & Interdisciplinary Coordination](#8-line-list-development-workflow--interdisciplinary-coordination)
9. [Sample Calculation Sheets](#9-sample-calculation-sheets)
10. [Sample Datasheets](#10-sample-datasheets)
11. [Practical Design Checklist](#11-practical-design-checklist)
12. [Common Field Issues & Lessons Learned](#12-common-field-issues--lessons-learned)
13. [Case Study — Stale Design Pressure Basis Causing a Flange Rating Mismatch](#13-case-study--stale-design-pressure-basis-causing-a-flange-rating-mismatch)
14. [Reference Standards](#14-reference-standards)

---

## 1. Design Basis & Assumptions

Line list preparation is normally governed by a **"Piping Material Specification (PMS)"** and a **"Line Designation / Numbering Philosophy"**, both issued and frozen early — the line list itself is a living document (revised through the project), but the *rules* it's built on should not change mid-project without a controlled revision, since every downstream discipline (stress, materials, procurement, construction) works directly off the line list.

### 1.1 Project & Equipment Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Line | 6"-P-1042-A1A-H | Pump discharge, V-100 to V-200 |
| Fluid | Light hydrocarbon liquid, ρ ≈ 850 kg/m³ | — |
| Source equipment | Pump P-101 A/B (centrifugal) | Suction from V-100 |
| Pump rated differential | 250 psi at rated flow | From pump datasheet |
| Pump shutoff (dead-head) differential | 1.15 × rated (typical centrifugal) | Confirm actual curve — do not assume a generic factor without vendor data |
| Normal suction pressure | 20 psig | — |
| Downstream PSV set pressure | 275 psig | On V-200 inlet piping |
| Destination equipment | V-200, MAWP 300 psig | — |
| Normal operating temperature | 150 °F (65.6 °C) | — |
| Site minimum design ambient temperature | −20 °F (−28.9 °C) | Governs MDMT/impact-test screening |
| Elevation change, pump discharge to V-200 inlet | +25 m (line runs uphill) | Governs static head correction |
| Pipe size (assumed) | 6-inch, Schedule 40 | To be confirmed by wall thickness calc |
| Material | ASTM A106 Grade B, seamless, CS | Standard PMS default for this service class |

### 1.2 Codes & Standards / Methodology Basis
- **ASME B31.3** — Process Piping (design pressure/temperature, wall thickness, MDMT/impact-test exemption methodology)
- **ASME B16.5 / B16.34** — flange and valve pressure-temperature ratings
- **ASME B36.10M** — standard pipe wall thickness/schedule designations
- Project **Piping Material Specification (PMS)** — governs where stricter than code minimums (e.g., house corrosion allowance, minimum wall thickness by size, mandatory PWHT thresholds)
- Company/client line designation and line list procedure — governs field naming/numbering conventions

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Design pressure margin over normal operating pressure | Greater of +10% or +25 psi (client-specific, confirm actual rule) | Common industry default; some clients use different margins by service |
| Design temperature margin over normal operating temperature | +25 °F (or per client PMS) | Accounts for upset/startup excursions |
| Corrosion allowance (CS, general hydrocarbon service) | 1/16 in (1.5 mm) | Project PMS; can be higher for sour/erosive service |
| Mill under-tolerance (seamless pipe) | 12.5% | ASME B36.10M / API 5L manufacturing tolerance |
| Static head correction | Applied per elevation difference between reference point and connected equipment | Frequently missed on lines with significant elevation change — see Calc Sheet 9.1 |
| Personnel-protection insulation touch-temperature limit | 140 °F (60 °C) surface temperature | Common industry/OSHA-referenced touch-safety threshold; confirm project HSE standard |
| MDMT impact-test exemption methodology | ASME B31.3 Fig. 323.2.2A/B (basic curve + stress-ratio reduction) | See Calc Sheet 9.2 |

> ⚠️ **Practical note:** The design pressure/temperature margin rules (Section 1.3) are exactly the kind of assumption that varies by client and is easy to get wrong by defaulting to "whatever the last project used" — always confirm the actual project basis of design (BOD) or piping design philosophy document before populating the line list, since this single rule affects every line on the list.

---

## 2. Fundamentals & Purpose of the Line List

### 2.1 What the Line List Is
The line list is the **master register of every piping line** in a project, uniquely identifying each line and recording the data needed to design, procure, fabricate, inspect, and operate it — size, material/piping class, design conditions, insulation, tracing, corrosion allowance, test pressure, and more.

### 2.2 Why It Matters
- It is the **single source of truth** that piping stress engineers, materials engineers, procurement, fabrication, and construction all work from — an error or omission on the line list propagates directly into isometrics, material take-offs, and ultimately the as-built plant.
- It is the document where the design pressures/temperatures established by process, relief, and settle-out studies (see the companion guides in this series) are **formally recorded and carried forward** into piping design — the line list is where those upstream calculations become an actionable, traceable engineering record.
- It supports **Management of Change (MOC)** — any change to a line's service, size, or design condition should be traceable through a controlled line list revision, not an informal note on an isometric.

---

## 3. Line Numbering & Designation Philosophy

### 3.1 Typical Line Number Structure
A common format (project-specific — always confirm the actual convention):
```
6"  -  P  -  1042  -  A1A  -  H
|      |      |        |      |
Size   Fluid  Sequential  Piping  Insulation/
       Code   Number      Class   Tracing Code
```
- **Size:** Nominal pipe size (NPS)
- **Fluid/service code:** e.g., P = process, U = utility, ST = steam, CW = cooling water — project-specific legend
- **Sequential number:** Unique identifier, often area/unit-coded (e.g., 1000s block for Unit 100)
- **Piping class:** Ties directly to the PMS (material, rating, corrosion allowance — see Section 5)
- **Insulation/tracing suffix:** e.g., H = hot insulation, C = cold/personnel protection, T = heat traced

### 3.2 Practical Considerations
- **Sequential number blocks** should be pre-allocated by area/unit/discipline at project start to avoid renumbering conflicts as the design develops — renumbering an active line mid-project cascades into isometrics, stress models, and the material take-off, and is a common source of late-project rework.
- **Line breaks** (where the line number changes) should occur at a piping class break, a major branch, or an equipment nozzle — not arbitrarily mid-run — since the piping class boundary is what actually matters for material procurement and stress analysis.

---

## 4. Line List Data Fields & Content

A typical line list carries (at minimum) the following fields per line — see Section 10.1 for a worked sample table:

| Field Category | Typical Fields |
|---|---|
| Identification | Line number, P&ID reference, from/to (equipment or line), area/unit |
| Sizing | Nominal size, schedule/wall thickness |
| Service | Fluid service, phase, hazardous service flag (toxic/flammable/sour) |
| Piping class | Class code, material, rating (e.g., ASME Class 150/300/600) |
| Design conditions | Design pressure, design temperature, MDMT |
| Operating conditions | Normal operating pressure/temperature (min and max if variable) |
| Test requirements | Hydrotest pressure, test medium, PWHT requirement |
| Corrosion | Corrosion allowance, corrosion loop/CML reference |
| Insulation/tracing | Insulation type & thickness, personnel protection flag, heat tracing type |
| Special requirements | X-ray/NDE percentage, PMI requirement, stress-critical flag, sour service flag |

**Practical tip:** The **stress-critical flag** and **hazardous service flag** fields are small but high-value — they tell the stress engineering team and the QA/QC team which lines need the most rigorous review, and missing or incorrect flags are a recurring source of scope gaps discovered late (see Section 12).

---

## 5. Piping Class / Material Selection Basis

### 5.1 What a Piping Class Defines
A piping class (per the project PMS) bundles together, for a given pressure/temperature/service combination: base material, pressure rating (ASME B16.5 class), corrosion allowance, valve types/trim, gasket/bolting, and any special requirements (PWHT, NDE, PMI) — assigning a line to a class is a shorthand that carries all of this information at once.

### 5.2 Selection Logic
1. Determine the line's **design pressure and temperature** (Section 6).
2. Determine the required **material** based on service (sweet/sour, temperature range, corrosion/erosion considerations — see the companion Flow Assurance guide for corrosion/erosion screening methodology).
3. Select the **lowest-rated class** (e.g., ASME Class 150 before considering Class 300) that satisfies the design pressure/temperature at the selected material's B16.5 rating table — going to a higher class than necessary adds unnecessary cost.
4. Confirm any **service-specific overrides** in the PMS (e.g., a class might be upgraded regardless of pressure/temperature for sour service, cyclic service, or a company minimum-class policy).

### 5.3 Practical Tip
Piping class boundaries (e.g., ASME Class 150 vs. 300) are **temperature-dependent**, not just pressure-dependent — a line that would be Class 150 at 100°F can require Class 300 at 400°F even at the same design pressure, because B16.5 allowable pressure *decreases* with increasing temperature for a given class. Always check the class rating table at the line's actual design temperature, not just at ambient.

---

## 6. Design Pressure & Temperature Determination

### 6.1 Design Pressure — General Approach
Design pressure is the **highest** of several candidate values, not simply the normal operating pressure plus a flat margin:
- Upstream/downstream equipment MAWP (if directly connected without an intervening relief device)
- Pump shutoff (dead-head) pressure, for pump discharge lines
- Relief/PSV set pressure plus the code-allowed accumulation margin (commonly +10%)
- Normal operating pressure plus the project's standard margin (Section 1.3)
- **Static head correction** for elevation differences between the line's reference point and connected equipment (Calc Sheet 9.1)

### 6.2 Design Temperature — General Approach
- Normal operating temperature plus the project's standard margin (Section 1.3), covering credible startup/upset excursions.
- For lines exposed to solar radiation or with no active cooling at low/no-flow conditions, check whether a stagnant/no-flow case could exceed the flowing design temperature.
- **Minimum design metal temperature (MDMT)** is checked separately, against the site's minimum ambient/process temperature, using the ASME B31.3 impact-test exemption methodology (Calc Sheet 9.2) — this determines whether the selected material requires impact (Charpy) testing.

---

## 7. Insulation, Heat Tracing & PWHT Requirements

### 7.1 Insulation Types & Purpose
| Type | Purpose |
|---|---|
| **Hot insulation (process/energy conservation)** | Reduce heat loss from hot lines, maintain process temperature |
| **Personnel protection insulation** | Reduce accessible surface temperature below a touch-safety threshold (commonly 140 °F/60 °C) — see Calc Sheet 9.4 |
| **Cold/anti-sweat insulation** | Prevent condensation on cold lines below ambient dew point |
| **Acoustic insulation** | Reduce noise from high-velocity/pressure-drop lines (e.g., control valve stations) |

### 7.2 Heat Tracing
- **Electrical trace heating** or **steam tracing** maintains line temperature above a minimum (freeze protection, wax/hydrate avoidance — see the companion Flow Assurance guide, viscosity maintenance for heavy fluids, or process temperature maintenance during low/no-flow periods).
- Line list should flag tracing requirement, type, and — where available — the target maintain temperature, so the tracing design package can size cable/steam trace spacing without re-deriving the requirement from scratch.

### 7.3 PWHT (Post-Weld Heat Treatment)
- Required based on material, thickness, and service per ASME B31.3 (and any project PMS overrides, which are often more conservative than the code minimum — e.g., mandatory PWHT for all sour service welds regardless of thickness).
- Line list should carry a clear PWHT flag per line so fabrication planning and NDE scope are established before shop drawings are issued, not discovered during fabrication.

---

## 8. Line List Development Workflow & Interdisciplinary Coordination

### 8.1 Typical Workflow
1. **Process** issues P&IDs with line numbers, normal operating conditions, and preliminary line sizes.
2. **Process/Relief/Settle-Out studies** (see companion guides) establish governing design pressures/temperatures for each system.
3. **Piping/Materials** assigns piping class per the PMS logic (Section 5) and populates the line list.
4. **Stress engineering** reviews stress-critical lines (large diameter, high temperature, connected to rotating equipment) and may request line routing or support changes that feed back into the line list (e.g., a design temperature revision after a more detailed thermal analysis).
5. **Insulation/tracing/PWHT** requirements are added once process and mechanical requirements are finalized.
6. **QA/QC** issues the line list for construction, links it to the NDE/inspection plan, and manages revision control through project close-out.

### 8.2 Practical Coordination Tips
- The line list should be treated as **the** controlled interface document between disciplines — informal verbal agreements to change a design condition ("just make it Class 300, we'll fix the line list later") are a common source of the exact kind of mismatch described in the Case Study (Section 13).
- Any revision to a line's design pressure/temperature (e.g., following a settle-out study update, per the companion Compressor Settle-Out guide) must trigger a **line list revision with change tracking**, not a standalone email or marked-up isometric that never makes it back into the controlled document.

---

## 9. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific equipment datasheets and the project PMS.

### 9.1 Calc Sheet 1 — Design Pressure Determination (with Static Head Correction)

**Given (from Section 1 basis):**
- Normal suction pressure = 20 psig
- Pump rated differential = 250 psi; shutoff (dead-head) factor = 1.15
- Downstream PSV set pressure = 275 psig
- Fluid density, ρ = 850 kg/m³
- Elevation rise, pump discharge to V-200 = 25 m
- V-200 MAWP = 300 psig

**Step 1 — Pump shutoff (dead-head) pressure:**
```
Shutoff differential = 250 × 1.15 = 287.5 psi
Dead-head pressure = suction pressure + shutoff differential
Dead-head pressure = 20 + 287.5 = 307.5 psig
```

**Step 2 — PSV set pressure plus accumulation margin (+10%):**
```
PSV set + 10% = 275 × 1.10 = 302.5 psig
```

**Step 3 — Governing design pressure at the reference point (pump discharge nozzle):**
```
Design pressure = max(dead-head, PSV set + 10%) = max(307.5, 302.5) = 307.5 psig
```

**Step 4 — Static head correction (checking the elevated destination equipment, V-200):**
```
ΔP_static = ρ × g × h
ΔP_static = 850 × 9.81 × 25 = 208,463 Pa = 208.5 kPa ≈ 30.2 psi

Static pressure at V-200 (top of rise) under the dead-head (static, no-flow) condition:
P_at_V200 = Dead-head pressure − ΔP_static = 307.5 − 30.2 ≈ 277.3 psig
```

**Step 5 — Check against V-200 MAWP:**
```
P_at_V200 (277.3 psig) < V-200 MAWP (300 psig)  →  PASS
```

**Result:** Line design pressure (at the pump discharge reference point) = **307.5 psig**, rounded to **310 psig** per standard line list rounding practice (or the project's specific rounding convention). The static head correction confirms V-200 is adequately protected under the dead-head condition without requiring a lower line design pressure or additional relief device — but the **line itself** must still be rated for 307.5 psig along its full length, since that is the maximum pressure it will see at the low (pump discharge) end.

> 📌 **Assumption check:** This example credited static head to *relieve* pressure at the elevated destination — the opposite direction (checking a line that runs *downhill* from source to destination) would instead require *adding* static head to the design pressure at the low point. Always work out the actual direction of elevation change for each line rather than applying a memorized "add" or "subtract" rule.

---

### 9.2 Calc Sheet 2 — MDMT / Impact-Test Exemption Screening (ASME B31.3)

**Given:**
- Material: ASTM A106 Grade B, seamless (Curve B per B31.3 Fig. 323.2.2A)
- Nominal wall thickness (Schedule 40, 6-in): t = 0.280 in
- Design pressure, P = 310 psig (from Calc Sheet 9.1, rounded)
- Pipe OD, D = 6.625 in
- Allowable stress at design temperature, S = 20,000 psi (illustrative — confirm actual value from B31.3 Table A-1 at the line's design temperature)
- Site minimum design metal temperature = −20 °F (Section 1.1 basis)

**Step 1 — Calculate the design hoop stress:**
```
σ = P × D / (2 × t)
σ = 310 × 6.625 / (2 × 0.280)
σ = 2,053.8 / 0.560
σ ≈ 3,668 psi
```

**Step 2 — Calculate the stress ratio, Rs (design stress ÷ allowable stress):**
```
Rs = σ / S = 3,668 / 20,000 ≈ 0.183
```

**Step 3 — Basic minimum temperature from Curve B (illustrative chart read, B31.3 Fig. 323.2.2A):**
```
For 0.280 in wall thickness, Curve B basic minimum temperature ≈ −20 °F
```

**Step 4 — Apply the stress-ratio-based temperature reduction (illustrative chart read, Fig. 323.2.2B):**
```
For Rs ≈ 0.18–0.20, allowable temperature reduction ≈ 50 °F (read from chart)
Reduced exemption temperature = −20 °F − 50 °F = −70 °F
```

**Step 5 — Compare to site minimum design metal temperature:**
```
Site MDMT (−20 °F) > Reduced exemption temperature (−70 °F)  →  PASS
```

**Result:** Because the line operates at a low stress ratio (design stress is only ~18% of allowable), the B31.3 stress-ratio reduction credit lowers the impact-test exemption temperature to **−70 °F**, comfortably below the site's −20 °F minimum design metal temperature — **impact (Charpy) testing is not required** for this line's material at this thickness.

> 📌 **Assumption check:** This calc sheet illustrates the *method* — the actual Curve A/B/C/D basic temperature and the stress-ratio reduction value must be read from the current edition of ASME B31.3 Fig. 323.2.2A/B (or an equivalent validated software tool) using the line's actual wall thickness and stress ratio, not assumed from this example. This exemption credit is one of the most valuable (and most often under-utilized) tools in piping material selection for cold-climate projects — a line that appears to require impact-tested material at first glance can often be exempted once the actual stress ratio is calculated, avoiding unnecessary cost.

---

### 9.3 Calc Sheet 3 — Pressure Design (Wall) Thickness (ASME B31.3)

**Given (carried from Calc Sheets 9.1–9.2):**
- Design pressure, P = 310 psig
- Pipe OD, D = 6.625 in
- Allowable stress, S = 20,000 psi
- Weld joint efficiency, E = 1.0 (seamless)
- Coefficient, Y = 0.4 (ferritic steel, t < D/6, temperature < 900 °F)
- Corrosion allowance, CA = 0.0625 in (Section 1.3 basis)
- Mill under-tolerance = 12.5% (seamless pipe)

**Step 1 — Pressure design thickness (B31.3 straight pipe formula):**
```
t = (P × D) / [2 × (S × E + P × Y)]
t = (310 × 6.625) / [2 × (20,000 × 1.0 + 310 × 0.4)]
t = 2,053.8 / [2 × (20,000 + 124)]
t = 2,053.8 / 40,248
t ≈ 0.0510 in
```

**Step 2 — Add corrosion allowance:**
```
t + CA = 0.0510 + 0.0625 = 0.1135 in
```

**Step 3 — Apply mill under-tolerance to determine minimum nominal (purchase) thickness:**
```
t_nominal = (t + CA) / (1 − 0.125)
t_nominal = 0.1135 / 0.875
t_nominal ≈ 0.1297 in
```

**Step 4 — Compare to standard Schedule 40 wall thickness (6-in NPS):**
```
Schedule 40 nominal wall = 0.280 in
Required minimum (calculated) = 0.130 in
Schedule 40 (0.280 in) >> Required minimum (0.130 in)  →  PASS with significant margin
```

**Result:** Schedule 40 is **more than adequate** for pure pressure-containment purposes on this line — the calculated minimum required thickness (≈0.130 in) is less than half of Schedule 40's actual wall (0.280 in). In practice, Schedule 40 (or the project PMS's standard minimum wall for this size) is still selected, because piping class minimum-thickness rules are very often governed by **mechanical robustness, erosion allowance, and standardization practice**, not by the pressure design calculation alone.

> 📌 **Practical note:** This is a common and useful finding to document explicitly on a line list review — it confirms the selected schedule is not marginal, and it also flags that a lighter (and cheaper) schedule *could* be justified by pressure alone if the project's minimum-wall policy allowed it, which is sometimes worth raising during a cost-optimization value-engineering pass on high-quantity bulk piping.

---

### 9.4 Calc Sheet 4 — Personnel Protection Insulation Thickness

**Given:**
- Pipe OD, D = 6.625 in → outer radius, r1 = 3.3125 in = 0.2760 ft
- Process (pipe) temperature, T_pipe = 250 °F
- Ambient (design, summer) temperature, T_amb = 80 °F
- Touch-safety target surface temperature, T_surface = 140 °F (Section 1.3 basis)
- Insulation thermal conductivity, k = 0.032 Btu/(hr·ft·°F) (mineral wool, typical)
- Ambient natural convection coefficient, h = 1.5 Btu/(hr·ft²·°F) (typical outdoor, still air)

**Step 1 — Set up the steady-state radial conduction/convection energy balance (per unit length):**
```
Conduction through insulation = Convection from surface to ambient

2π k (T_pipe − T_surface) / ln(r2/r1)  =  h × 2π r2 (T_surface − T_amb)

Simplifies to:
k (T_pipe − T_surface) / ln(r2/r1) = h × r2 × (T_surface − T_amb)
```

**Step 2 — Substitute known values:**
```
k (T_pipe − T_surface) = 0.032 × (250 − 140) = 0.032 × 110 = 3.52
h × (T_surface − T_amb) = 1.5 × (140 − 80) = 1.5 × 60 = 90

3.52 / ln(r2/r1) = 90 × r2
```

**Step 3 — Solve iteratively for r2 (with r1 = 0.276 ft):**

| Trial r2 (ft) | ln(r2/r1) | LHS = 3.52/ln(r2/r1) | RHS = 90 × r2 | Compare |
|---|---|---|---|---|
| 0.30 | 0.0834 | 42.2 | 27.0 | LHS > RHS |
| 0.32 | 0.1479 | 23.8 | 28.8 | LHS < RHS |
| 0.313 | 0.1258 | 27.98 | 28.17 | LHS ≈ RHS (converged) |

```
r2 ≈ 0.313 ft = 3.756 in
```

**Step 4 — Required insulation thickness:**
```
Insulation thickness = r2 − r1 = 3.756 − 3.3125 ≈ 0.443 in
```

**Result:** The calculated minimum insulation thickness to bring the surface temperature down to the 140 °F touch-safety target is only **≈0.44 in** — however, standard insulation product thicknesses and mechanical/jacketing durability requirements typically mean a **practical minimum of 1 inch** is specified on the line list regardless of the thinner calculated requirement.

> 📌 **Assumption check:** This lumped, steady-state radial model ignores jacketing emissivity/radiation effects and assumes still-air convection — for outdoor, windy locations the effective h can be considerably higher (reducing required insulation thickness further) or the analysis may need a wind-speed-adjusted convection coefficient per the project's insulation design standard. Also confirm the project's touch-safety standard: some specify a shorter contact-duration basis (e.g., a 5-second momentary contact limit allows a higher surface temperature than the 140°F "any duration" basis used here).

---

## 10. Sample Datasheets

### 10.1 Sample Line List Table

| Line No. | From → To | Size (NPS) | Piping Class | Fluid Service | Design P (psig) | Design T (°F) | Normal P/T | Insulation | PWHT | Test Pressure (psig) | Corr. Allow. (in) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 6"-P-1042-A1A-H | P-101 A → V-200 | 6 | A1A (CS, Cl.300) | Light HC liquid | 310 | 200 | 100 psig / 150 °F | Personnel protection, 1" | No | 465 | 0.0625 |
| 8"-P-1015-A1A | V-100 → P-101 A/B | 8 | A1A (CS, Cl.150) | Light HC liquid | 165 | 175 | 20 psig / 100 °F | None | No | 248 | 0.0625 |
| 4"-U-2031-B2B-T | Utility Header → K-101 Seal Pot | 4 | B2B (CS, Cl.150, sour) | Sweet fuel gas | 285 | 250 | 250 psig / 150 °F | Hot, 1.5" | Yes | 428 | 0.125 |
| 2"-P-1042-01-A1A | 6"-P-1042 branch → PSV-115 | 2 | A1A (CS, Cl.300) | Light HC liquid | 310 | 200 | 100 psig / 150 °F | None | No | 465 | 0.0625 |

*(Illustrative — a real line list carries every line in the unit, with additional fields per the project's line list procedure: P&ID reference, stress-critical flag, sour service flag, PMI requirement, NDE percentage, etc.)*

---

### 10.2 Piping Class Summary Datasheet

| Piping Class | A1A | B2B |
|---|---|---|
| **Base Material** | ASTM A106 Gr. B, seamless (CS) | ASTM A106 Gr. B, seamless (CS), sour service qualified |
| **Rating** | ASME B16.5 Class 300 | ASME B16.5 Class 150 |
| **Corrosion Allowance** | 0.0625 in (1.5 mm) | 0.125 in (3 mm) — higher for sour/erosive service |
| **Design Temperature Range** | −20 °F to 400 °F | −20 °F to 400 °F |
| **Gasket** | Spiral wound, CS winding, graphite filler | Spiral wound, 316SS winding, graphite filler |
| **Bolting** | ASTM A193 B7 / A194 2H | ASTM A193 B7M / A194 2HM (sour service, NACE MR0175) |
| **Valve Trim** | Standard CS trim | Sour-service-qualified trim per NACE MR0175/ISO 15156 |
| **PWHT Requirement** | Per B31.3 thickness/material thresholds | Mandatory for all welds (PMS override, sour service) |
| **NDE Requirement** | Per B31.3 category (normal fluid service) | 100% RT (PMS override, sour service) |
| **Impact Test Requirement** | Per Calc Sheet 9.2 methodology, case-by-case | Per Calc Sheet 9.2 methodology, case-by-case |

---

### 10.3 Line Designation / Numbering Legend

| Code Position | Example | Meaning |
|---|---|---|
| Size prefix | 6" | Nominal pipe size |
| Fluid code | P | Process |
| | U | Utility |
| | ST | Steam |
| | CW | Cooling water |
| Sequential number | 1042 | Unique within area/unit block (e.g., 1000–1999 = Unit 100) |
| Piping class | A1A | Ties to PMS (Section 10.2) |
| Suffix | H | Hot insulation |
| | C | Cold/personnel protection insulation |
| | T | Heat traced |
| | (none) | No insulation/tracing |

---

## 11. Practical Design Checklist

- [ ] Line designation/numbering philosophy and PMS issued and approved (Section 1) before line list population begins
- [ ] Design pressure determined per the governing-case logic (equipment MAWP, dead-head, PSV set + margin, operating + margin) — see Calc Sheet 9.1
- [ ] Static head correction applied for any line with meaningful elevation change between its reference point and connected equipment
- [ ] Design temperature determined including startup/upset margin and any stagnant/no-flow solar-exposure case
- [ ] MDMT / impact-test exemption screened per ASME B31.3 methodology, using actual stress ratio, not skipped or assumed — see Calc Sheet 9.2
- [ ] Piping class assigned per the lowest-rated class that satisfies design P/T at the line's actual design temperature (not ambient)
- [ ] Wall thickness verified against the pressure design formula plus corrosion allowance and mill tolerance — see Calc Sheet 9.3
- [ ] Insulation type and thickness specified per actual requirement (process, personnel protection, or anti-sweat) — see Calc Sheet 9.4
- [ ] Heat tracing requirement and target maintain temperature flagged where applicable
- [ ] PWHT and NDE requirements flagged per material/thickness/service (including any PMS override for sour/critical service)
- [ ] Stress-critical and hazardous-service flags populated for every line, not just the obviously large-bore ones
- [ ] Line list formally linked to the source design-basis documents (process, relief, settle-out studies) so revisions to those studies trigger a controlled line list revision
- [ ] Line list issued under change/revision control, with a clear audit trail from design basis to final as-built record

---

## 12. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Wrong flange rating installed in the field (Class 150 where Class 300 required) | Line list design pressure was not updated after a pump curve/dead-head revision | Formally link line list design pressure fields to the source equipment datasheet revision, and trigger a line list re-check on any equipment datasheet revision |
| Unnecessary impact testing specified, adding cost/schedule | MDMT screening skipped or done without the stress-ratio reduction credit | Always apply the full B31.3 Fig. 323.2.2A/B methodology (Calc Sheet 9.2), not just the basic curve, before defaulting to impact-tested material |
| Personnel protection insulation omitted on an accessible hot line | Insulation requirement field left blank/defaulted rather than explicitly calculated per line | Require an explicit insulation calc or standard-detail reference for every accessible hot line above the touch-safety threshold, not a blanket assumption |
| Sour service PMS overrides missed on a branch line | Branch line inherited the parent line's class code without independent re-verification of service | Independently verify the fluid service and PMS class logic for every line, including small branches, rather than assuming inheritance is always correct |
| Line list and isometrics diverged during detailed engineering | Isometric revisions made informally without a corresponding controlled line list update | Enforce the line list as the master document — any isometric change affecting a line list field must trigger a line list revision, not the reverse |
| Static head effects on a long elevation-change line missed at FEED | Design pressure calculated only at a single nominal reference point without checking the full elevation profile | Explicitly check static head correction for any line with significant elevation change, in both directions of possible governing case (Calc Sheet 9.1 note) |

---

## 13. Case Study — Stale Design Pressure Basis Causing a Flange Rating Mismatch

> A composite, illustrative case study based on the type of finding commonly encountered during piping QA/QC review and hydrotest preparation. Names, tag numbers, and figures are representative, not project-specific.

### 13.1 Background

The illustrative pump discharge line from this guide (6"-P-1042-A1A-H, P-101 A/B to V-200) was originally line-listed at FEED using an early pump vendor's preliminary curve, which showed a rated differential of 220 psi and an assumed shutoff factor of 1.10 — giving an early dead-head estimate of 20 + (220×1.10) = 262 psig. Combined with the PSV set + 10% case (302.5 psig), the **PSV case governed** at that time, and the line was assigned Class 150 piping class (rated adequately for ~285 psig at the line's design temperature per B16.5).

### 13.2 Problem Identified

During detailed engineering, the pump vendor issued a final certified performance curve showing a higher rated differential (250 psi) and a confirmed shutoff factor of 1.15 — consistent with the Calc Sheet 9.1 example in this guide, giving a revised dead-head pressure of 307.5 psig, now **exceeding** the PSV case and governing the line design pressure. This revision was correctly captured in the process design basis and the pump datasheet, but the **line list was never updated** — the piping class remained listed as Class 150 (A1A rated to ~285 psig) through issue-for-construction.

The discrepancy was caught during **pre-hydrotest QA/QC review**, when the inspector cross-checked the installed Class 150 flanges against the (by-then-corrected) process design basis summary and found the installed rating did not cover the documented 307.5 psig design pressure.

### 13.3 Investigation & Recalculation

The piping engineering team reran the Calc Sheet 9.1 methodology using the final, certified pump curve data (the same numbers used in this guide's worked example) and confirmed: dead-head pressure = 307.5 psig, governing over the PSV + 10% case (302.5 psig) — meaning **Class 300** piping class was required, not the as-installed Class 150.

### 13.4 Root Cause

Two compounding root causes were identified:
1. **No formal trigger linking equipment datasheet revisions to line list re-verification** — the pump vendor's final curve revision was correctly routed to process engineering and the pump datasheet, but there was no procedural step requiring a corresponding line list check for any line whose design pressure basis depended on that equipment.
2. **Line list revision control gap** — the line list had been "frozen" for issue-for-construction based on the FEED-stage pump data, and the subsequent vendor data revision was treated as a pump-package-only update rather than triggering a piping design basis review.

### 13.5 Resolution

- The as-installed Class 150 flanges, valves, and fittings on the affected line segment (pump discharge to the first isolation point) were replaced with Class 300 components before hydrotest proceeded — caught before the line was put into service, avoiding a safety-critical in-service failure, but still requiring field rework, re-procurement, and a schedule delay for the affected tie-in.
- The line list was formally revised, and a **design-basis traceability check** was added retroactively across the rest of the unit's line list to confirm no other lines had a similar stale-basis gap — none were found, but the check itself became a standard QA/QC step.
- The company's line list procedure was updated to require: any equipment datasheet revision affecting a connected line's design pressure/temperature basis **must** trigger an explicit line list re-verification, logged as a discrete checklist item in the MOC/revision record — not left to informal cross-discipline awareness.

### 13.6 Outcome

- The rework was contained to a single line segment and caught before commissioning, limiting the cost/schedule impact to several weeks rather than a post-startup failure — but the near-miss (a Class 150 flange rated below the actual required design pressure, discovered only at pre-hydrotest QA) was treated seriously as a process gap, not just a one-off paperwork error.
- The finding was documented as a corporate lessons-learned item: line list design conditions must be **formally, traceably linked** to their source equipment/process documents, with revision-triggered re-verification, rather than relying on the line list team's own tracking discipline alone.

### 13.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A line list "frozen" for construction can silently go stale if its source design-basis documents are later revised | Require every equipment datasheet or process design-basis revision to trigger an explicit, logged line list re-verification for all dependent lines |
| The PSV-set-plus-margin case and the pump dead-head case can swap which one governs as vendor data firms up | Recalculate the governing design pressure case (Calc Sheet 9.1 method) whenever any input to it changes, not just at FEED |
| A rating mismatch can go undetected through fabrication and installation and only surface at hydrotest/QA review | Build a design-basis cross-check into the QA/QC pre-hydrotest procedure as a standard, not an ad hoc catch |
| Field rework after installation is far costlier than catching the same gap during detailed engineering | Treat the line list as a live, traceable document throughout detailed engineering, not a document that is finalized once and then only checked again at the very end |

---

## 14. Reference Standards

- **ASME B31.3** — Process Piping (design pressure/temperature, wall thickness, MDMT/impact-test exemption methodology — Section 323 and Fig. 323.2.2A/B)
- **ASME B16.5** — Pipe Flanges and Flanged Fittings (pressure-temperature ratings by class)
- **ASME B16.34** — Valves — Flanged, Threaded, and Welding End
- **ASME B36.10M** — Welded and Seamless Wrought Steel Pipe (standard schedule/wall thickness)
- **API 5L** — Specification for Line Pipe
- **NACE MR0175 / ISO 15156** — Materials for use in H₂S-containing environments (sour service piping class overrides)

---

*This guide is a practical study reference combining standard line list preparation methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against the project-specific Piping Material Specification (PMS), equipment vendor data, and the current edition of the referenced codes. This guide should be read alongside the companion Flare Network Design, Depressurization Calculation, and Compressor Settle-Out Calculations study guides, since the design pressures/temperatures those studies establish are exactly what the line list is built to carry forward.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
