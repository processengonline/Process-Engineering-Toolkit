# 🧯 PSV Sizing & Design — Practical Study Guide

> A field-oriented reference covering the core engineering topics in pressure safety valve (PSV) sizing and design — combining API 520/521, ASME Section VIII, and ISO 4126 methodology with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design**, **Depressurization Calculation**, **Instrumentation Process Datasheet Preparation**, **Mechanical Datasheet Preparation**, **Process Philosophies**, and **Process Safety** study guides — PSV-101 (the fire-case relief valve on V-100 used throughout this series) is developed here into a full, multi-scenario sizing and mechanical design exercise.

**Illustrative project used throughout this guide:** PSV-101 on vessel V-100, evaluated against multiple credible relief scenarios (blocked outlet, thermal expansion, and a two-phase case) in addition to the fire case already sized in the companion Flare Network Design guide — used to work through liquid orifice sizing, thermal relief sizing, the omega method for two-phase relief, a critical pressure ratio check, an inlet piping pressure drop check, and a backpressure/balanced-bellows selection decision. All numbers below are worked sample calculations for study purposes — always replace with project-specific process data and the current edition of API 520/521.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Standards & Guidelines](#2-standards--guidelines)
3. [Relief Scenarios](#3-relief-scenarios)
4. [Sizing Calculations](#4-sizing-calculations)
5. [Design Considerations](#5-design-considerations)
6. [Mechanical & Installation Aspects](#6-mechanical--installation-aspects)
7. [Integration with Flare System](#7-integration-with-flare-system)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Datasheets](#9-sample-datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Conventional Trim Selected Without Checking for Variable Superimposed Backpressure](#12-case-study--conventional-trim-selected-without-checking-for-variable-superimposed-backpressure)
13. [Reference Standards](#13-reference-standards)

---

## 1. Design Basis & Assumptions

PSV sizing is never a single calculation — it is the process of evaluating **every credible relief scenario** for a piece of equipment, sizing for each one, and selecting the **governing** (largest required orifice) case, while separately confirming installation details (backpressure, inlet piping) don't invalidate the sizing basis. This guide works through that full process for PSV-101, building directly on the fire-case sizing already established in the companion Flare Network Design guide.

### 1.1 Equipment & Scenario Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Protected equipment | V-100 | Same vessel used throughout this guide series |
| PSV | PSV-101 | Set pressure 250 psig, per companion Flare Network Design and Instrumentation guides |
| Fire case (already sized) | W = 40,373 lb/hr, orifice "L" (1.838 in²) | Companion Flare Network Design guide, Calc Sheet 8.1/8.4; companion Instrumentation guide, Calc Sheet 10.4 |
| Blocked outlet (liquid) case | Pump P-101 rated flow, 150 gpm | Used in Calc Sheet 8.1 |
| Thermal expansion case | Isolated liquid-filled line segment, 50 ft² exposed area | Used in Calc Sheet 8.2 |
| Two-phase (flashing) case | Illustrative fire-exposed two-phase relief, W = 20,000 lb/hr | Used in Calc Sheet 8.3 |
| Flare header (shared) | Design pressure basis per companion Flare Network Design guide | Used in Calc Sheets 8.4–8.6 |

### 1.2 Codes & Standards / Methodology Basis
- **API 520 Part I & II** — sizing (Part I) and installation (Part II) of pressure-relieving devices
- **API 521** — relief system design philosophy, flare integration, fire-case depressurization
- **ASME Section VIII** — pressure vessel code requirements the PSV protects
- **ISO 4126** — international standard for safety devices, used where a project's contractual basis specifies ISO in lieu of/alongside API

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Discharge coefficient, Kd (gas/vapor, certified) | 0.975 (typical certified valve) | Confirm actual vendor-certified value; the commonly cited "0.9" figure is a general efficiency-factor approximation, not the certified Kd used in final sizing |
| Discharge coefficient, Kd (liquid) | 0.65 (uncertified/conservative default) | Confirm against actual certified liquid Kd once a valve is selected; certified values are sometimes higher |
| Allowed overpressure/accumulation | 10% (fire case, single valve); 16% (multiple valves); 25% (liquid thermal/non-fire, per API 521) | Confirm actual project-specific accumulation basis for each scenario type |
| Backpressure limit, conventional PSV (built-up only) | ≤10% of set pressure | Section 5.3; balanced bellows required if this is exceeded, or if superimposed backpressure is variable regardless of magnitude |
| Inlet pressure drop limit | ≤3% of set pressure (API 520) | Section 5.5, Calc Sheet 8.5 |
| Two-phase omega parameter and critical pressure ratio | Illustrative values, per Leung's correlation | Real design requires either DIERS-methodology software or lab flash data — see Calc Sheet 8.3 assumption note |

> ⚠️ **Practical note:** A PSV sized correctly for its governing relief scenario can still fail to perform as intended if the *installation* details — backpressure, inlet piping pressure drop — aren't independently checked against the same rigor as the sizing calculation itself. Sections 5 and 8's Calc Sheets 8.4–8.6 exist specifically because "sized correctly" and "installed correctly" are two different, both-necessary conditions.

---

## 2. Standards & Guidelines

### 2.1 API 520 Part I & II
Part I covers **sizing and selection** (the orifice area equations worked through in Section 4 and Calc Sheets 8.1–8.3); Part II covers **installation** (inlet/outlet piping, backpressure considerations — Section 5 and Calc Sheets 8.4–8.6).

### 2.2 API 521
Governs the broader relief system design philosophy — which scenarios must be evaluated (Section 3), fire-case depressurization methodology (companion Depressurization Calculation guide), and flare system integration (Section 7, companion Flare Network Design guide).

### 2.3 ASME Section VIII
The pressure vessel code that establishes the MAWP the PSV protects, and the allowable accumulation (how far above MAWP the vessel may be pressurized during a relief event) that in turn sets the PSV's allowed overpressure basis (Section 5.1).

### 2.4 ISO 4126
The international standard for safety devices against excessive pressure, broadly analogous to the API 520/521 framework but used where a project's governing contractual basis specifies ISO — the underlying sizing physics (Section 4) is the same; the standard's presentation and some coefficient conventions differ.

---

## 3. Relief Scenarios

Every PSV must be sized against **every credible relief scenario**, with the largest resulting required orifice area governing the final selection — this guide works through four distinct scenario types for PSV-101/V-100 (Calc Sheets 8.1–8.3, plus the fire case already sized in the companion Flare Network Design guide).

### 3.1 Blocked Outlet
A pump or compressor continuing to run against a closed downstream valve — the relief load is the pump/compressor's maximum credible flow at that condition (often close to its rated or shutoff capacity) — worked in Calc Sheet 8.1.

### 3.2 Fire Case
External fire exposure, sized per the API 521 methodology detailed in the companion Flare Network Design guide (that guide's Calc Sheet 8.1) and often paired with a depressurization requirement (companion Depressurization Calculation guide) to reduce the duration/severity of fire exposure the PSV alone must handle.

### 3.3 Utility Failure
Loss of cooling water, power, or instrument air can each independently create an overpressure scenario — e.g., loss of cooling water stopping condensation in a column overhead, causing vapor to back up and overpressure the system; each utility failure mode should be evaluated as its own distinct scenario, not assumed bounded by another case.

### 3.4 Control Valve Failure
A control valve failing to a position that creates runaway flow or pressure (e.g., a feed control valve failing open, overwhelming downstream capacity) — sized against the valve's maximum flow capacity at the upstream pressure, consistent with the companion Instrumentation Process Datasheet guide's control valve Cv sizing methodology (that guide's Calc Sheet 10.1) applied in reverse (maximum credible flow through a fully-open valve, rather than normal control flow).

### 3.5 Thermal Expansion
Liquid-filled lines or equipment isolated between block valves, exposed to ambient heating (solar radiation, or heat from an adjacent hot line/equipment) — liquid has very limited compressibility, so even a modest temperature rise in a fully liquid-filled, blocked-in system can generate very high pressure; worked in Calc Sheet 8.2.

---

## 4. Sizing Calculations

### 4.1 Gas Relief — Isentropic/Choked Flow Equations
The API 520 gas/vapor sizing equation (used for the fire case in the companion Flare Network Design guide, that guide's Calc Sheet 8.4) applies when flow through the PSV orifice is **choked** (sonic) — confirmed by the critical pressure ratio check in Section 4.4/Calc Sheet 8.4.

### 4.2 Liquid Relief — Orifice Equation
```
A = Q / [38 × Kd × Kw × Kc × Kv × √(ΔP/SG)]
```
where Q = flow (gpm), A = required area (in²), Kd = discharge coefficient, Kw = backpressure correction, Kc = combination (rupture disk) factor, Kv = viscosity correction, ΔP = relieving pressure minus backpressure (psi), SG = specific gravity — worked in Calc Sheets 8.1 and 8.2.

### 4.3 Two-Phase Relief — HEM and Omega Method
For a flashing (two-phase) relief stream, the Homogeneous Equilibrium Model (HEM) and Leung's Omega (ω) method are the standard approaches — see Calc Sheet 8.3 for a worked (simplified) example. The omega parameter characterizes the fluid's compressibility/flashing behavior and is either derived from a laboratory flash test or estimated from thermodynamic correlations; the resulting critical pressure ratio and mass flux are then used analogously to the single-phase gas sizing approach.

### 4.4 Critical Pressure Ratio
```
rc = [2/(k+1)]^[k/(k−1)]
```
Determines whether flow through the orifice is choked (P2/P1 < rc, sonic — the simpler choked-flow sizing equation applies) or subcritical (P2/P1 > rc — a more complex non-choked sizing equation is required instead) — worked in Calc Sheet 8.4.

### 4.5 Discharge Coefficient (Kd)
An efficiency factor accounting for the real orifice's flow behavior versus the ideal (frictionless, fully-expanded) theoretical flow — certified values (from the valve manufacturer's ASME/national board certification testing) are typically used for final sizing (commonly ≈0.90–0.975 for vapor service, lower for liquid service, per Section 1.3), rather than a single universal value.

---

## 5. Design Considerations

### 5.1 Set Pressure & Overpressure
The PSV lifts at its set pressure; API 520/521 allows the vessel to accumulate **10% above set pressure** for a single-valve fire case (higher percentages are allowed for other scenarios or multiple-valve installations, per Section 1.3) before reaching its allowable accumulated pressure — this accumulation margin is what the relieving pressure (P1) used throughout Section 4's equations is built from.

### 5.2 Blowdown
The pressure drop **below** the set point required before the valve reseats — typically 4–7% of set pressure for a spring-loaded valve, and a design parameter that affects both valve stability (too little blowdown risks chattering) and how much inventory is actually released per relief cycle.

### 5.3 Backpressure
Must be explicitly accounted for in sizing, since it reduces the effective driving pressure differential across the orifice (Section 4.2's ΔP term) and, for a conventional (non-balanced) valve, can affect the valve's actual set pressure and capacity if it exceeds the allowable limit — see Section 5.4 and Calc Sheet 8.6.

### 5.4 Built-Up vs. Superimposed Backpressure
- **Superimposed backpressure** — the pressure already present in the discharge system (e.g., the flare header) *before* the valve lifts, from other sources.
- **Built-up backpressure** — the *additional* pressure rise in the discharge system caused specifically by this valve's own relieving flow.
- A **conventional** PSV's allowable *built-up* backpressure is limited to 10% of set pressure; but if the *superimposed* component is variable (common on a shared flare header where other PSVs may or may not be relieving simultaneously, per the companion Process Philosophies guide's blowdown sequencing discussion), a **balanced bellows** design is typically required regardless of whether the built-up component alone would pass the 10% test — worked in Calc Sheet 8.6.

### 5.5 Inlet Pressure Drop
API 520 limits inlet piping pressure drop (from the protected equipment's nozzle to the PSV inlet flange) to **≤3% of set pressure** — excessive inlet pressure drop can cause valve chatter and reduced capacity; worked in Calc Sheet 8.5.

### 5.6 Outlet Pressure Drop
Outlet (discharge) piping pressure drop must stay within limits that avoid instability — related to, but a distinct check from, the backpressure limits in Section 5.3/5.4, and directly connected to the companion Flare Network Design guide's header hydraulics methodology (that guide's Calc Sheet 8.2).

---

## 6. Mechanical & Installation Aspects

### 6.1 Orifice Sizes
Standardized **API letter designations** (D, E, F, G, H, J, K, L, M, N, P, Q, R, T — increasing area) — Calc Sheets 8.1–8.3 each select a standard letter designation for their respective scenario, and the largest orifice among all governing scenarios (including the fire case) determines the final valve selection.

### 6.2 Spring-Loaded vs. Pilot-Operated PSVs
| Type | Characteristics |
|---|---|
| **Spring-loaded (direct-acting)** | Simple, robust, the default choice for most services; mechanical spring directly opposes process pressure |
| **Pilot-operated** | Uses a small pilot valve to control a larger main valve; offers tighter set-pressure control near operating pressure, full lift at set pressure (no proportional "simmer" as with some spring valves), and can more easily tolerate higher backpressure — often preferred for high-backpressure or where operating pressure is close to set pressure |

### 6.3 Bellows Design
A bellows (in a balanced bellows PSV) isolates the valve's spring side from backpressure, so the valve's set pressure and capacity remain accurate even with variable or high built-up/superimposed backpressure (Section 5.4) — the standard solution when a conventional trim's backpressure limits are exceeded.

### 6.4 Connections — Nozzle Orientation, Inlet Piping Length
Inlet piping should be as short and direct as practical (minimizing the pressure drop checked in Calc Sheet 8.5), with the PSV mounted directly on (or very close to) the protected equipment's nozzle wherever feasible — consistent with the companion Mechanical Datasheet guide's nozzle schedule and reinforcement methodology (that guide's Section 5.3–5.4) for the PSV nozzle itself.

### 6.5 Maintenance & Testing
- **Bench testing** — removing the valve and testing its set pressure/capacity on a test stand, the traditional and most rigorous verification method.
- **In-situ testing** — testing the valve in place (e.g., using a portable test rig that applies pressure without full removal) — increasingly common where it reduces downtime/exposure, but must be validated as equivalent to bench testing for the specific valve type and service.

---

## 7. Integration with Flare System

### 7.1 PSV Discharge Contributes to Flare Load
Every PSV's sized relief flow (Section 4) becomes an input to the companion Flare Network Design guide's simultaneous relief load methodology (that guide's Section 3.3) — PSV-101's fire case and this guide's additional scenarios must all be checked against the shared header's capacity, individually and in credible simultaneous combinations.

### 7.2 Knock-Out Drum Sizing for Liquid Carryover
Where a PSV's relief stream carries liquid (the two-phase case in Calc Sheet 8.3, or any scenario with entrained liquid), the flare KOD (companion Flare Network Design guide, Section 4 and Calc Sheet 8.3 of that guide) must be sized to handle it — a PSV sizing study should explicitly flag any scenario with two-phase or liquid-carryover potential for the KOD design team, not leave it to be discovered independently.

### 7.3 Flare Tip Selection Based on Relief Gas Composition
The relief gas composition and heating value (varying scenario-to-scenario — the fire case, blocked outlet, and two-phase cases in this guide can each have different compositions) feed into the companion Flare Network Design guide's flare tip selection and combustion efficiency compliance methodology (that guide's Sections 4 and 6.3).

### 7.4 Dynamic Simulation for Simultaneous Relief Events
Where multiple PSVs could credibly relieve simultaneously, dynamic simulation (companion Dynamic Simulation guide, that guide's Section 5.1) provides a more rigorous check than the steady-state simultaneous-case grouping alone — confirming not just whether the header has enough *capacity*, but whether the *timing* of multiple relief events' peaks genuinely coincide, consistent with the companion Process Philosophies guide's blowdown sequencing analysis (that guide's Calc Sheet 8.3).

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific process data and the current edition of API 520/521.

### 8.1 Calc Sheet 1 — Blocked Outlet, Liquid Relief Sizing

**Given:** Pump P-101 rated flow (blocked-outlet relief load) = 150 gpm, PSV-101 set pressure = 310 psig (companion Line List guide basis), allowed overpressure (liquid, non-fire) = 25%, backpressure P2 = 10 psig, SG = 0.85, Kd = 0.65 (Section 1.3), Kw = Kc = Kv = 1.0.

**Step 1 — Relieving pressure:**
```
P1 = 310 × 1.25 = 387.5 psig
```

**Step 2 — Driving pressure differential:**
```
ΔP = P1 − P2 = 387.5 − 10 = 377.5 psi
```

**Step 3 — Required orifice area (API 520 liquid equation):**
```
A = Q / [38 × Kd × Kw × Kc × Kv × √(ΔP/SG)]
√(377.5/0.85) = √444.1 ≈ 21.07

A = 150 / (38 × 0.65 × 21.07) = 150 / 520.6 ≈ 0.288 in²
```

**Step 4 — Select standard orifice:**
```
"E" = 0.196 in² → too small
"F" = 0.307 in² → adequate
```

**Result:** Blocked outlet case requires **≈0.288 in²** → orifice **"F"**, smaller than the fire case's already-selected **"L"** orifice (1.838 in², companion Flare Network Design guide) — the fire case remains governing for this scenario pair.

---

### 8.2 Calc Sheet 2 — Thermal Expansion Relief Sizing

**Given:** Isolated liquid-filled line segment, exposed surface area A_exp = 50 ft², solar heat input H ≈ 2,000 Btu/(hr·ft²), liquid cubical thermal expansion coefficient β = 0.0007/°F, SG (G) = 0.85, Cp (C) = 0.55 Btu/(lb·°F), thermal relief set pressure = 150 psig (line class rating), overpressure 25%, backpressure ≈0.

**Step 1 — Required relief flow (simplified API 521 thermal relief formula):**
```
GPM = (β × H × A_exp) / (500 × G × C)
GPM = (0.0007 × 2,000 × 50) / (500 × 0.85 × 0.55)
GPM = 70 / 233.75 ≈ 0.30 gpm
```

**Step 2 — Relieving pressure and required orifice area:**
```
P1 = 150 × 1.25 = 187.5 psig
√(187.5/0.85) = √220.6 ≈ 14.85

A = 0.30 / (38 × 0.65 × 14.85) = 0.30 / 366.8 ≈ 0.00082 in²
```

**Result:** The calculated required area (≈0.0008 in²) is far smaller than even the smallest standard orifice, **"D" (0.110 in²)** — select orifice **"D"**, the smallest standard size. This is typical: thermal relief valves are almost always governed by the smallest available standard orifice rather than by the (tiny) calculated flow requirement.

> 📌 **Assumption check:** The simplified thermal relief formula used here is a widely-used API 521 rule-of-thumb screening approach — some companies instead default directly to the smallest standard orifice (or a dedicated small thermal relief valve/pin) for any blocked-in liquid segment without running this calculation at all, given how consistently it produces a negligible required flow; either approach is acceptable, but the calculation is useful confirmation for an unusual case (e.g., an unusually large exposed area or an unusually high-expansion-coefficient fluid).

---

### 8.3 Calc Sheet 3 — Two-Phase Relief Sizing (Omega Method, Simplified)

**Given:** Illustrative flashing two-phase fire-case relief, required mass flow W = 20,000 lb/hr, relieving pressure P1 = 300 psia, saturated liquid density at P1, ρ1 = 30 lb/ft³, omega parameter ω = 1.5 (illustrative — see assumption note), critical pressure ratio ηc ≈ 0.58 (illustrative, per Leung's correlation for this ω), discharge coefficient Cd = 0.85 (typical for two-phase omega-method sizing).

**Step 1 — Convert relieving pressure to consistent units:**
```
P1 = 300 psia × 144 = 43,200 lbf/ft²
```

**Step 2 — Leung's critical mass flux equation:**
```
G = Cd × ηc × √(gc × P1 × ρ1 / ω)

Inside the root: 32.2 × 43,200 × 30 / 1.5 = 27,820,800
√27,820,800 ≈ 5,274.5

G = 0.85 × 0.58 × 5,274.5 ≈ 2,600 lbm/(s·ft²)
```

**Step 3 — Convert required flow to consistent units:**
```
W = 20,000 lb/hr = 5.556 lb/s
```

**Step 4 — Required orifice area:**
```
A = W/G = 5.556/2,600 ≈ 0.002137 ft² ≈ 0.308 in²
```

**Step 5 — Select standard orifice:**
```
"F" = 0.307 in² → essentially exact match, no margin
"G" = 0.503 in² → provides adequate margin
```

**Result:** Required area ≈**0.308 in²** — select orifice **"G"** (0.503 in²) to provide reasonable sizing margin above the razor-thin "F" match.

> 📌 **Assumption check:** This is a deliberately simplified illustration of the omega method's structure — the omega parameter (ω) and critical pressure ratio (ηc) used here are illustrative inputs, not derived from first principles in this hand calc. Real two-phase relief sizing requires either laboratory flash test data (a small-scale blowdown test measuring the fluid's actual flashing behavior) or validated DIERS-methodology software — treat this calc sheet as illustrating the *method's structure*, not a substitute for a proper two-phase sizing study.

---

### 8.4 Calc Sheet 4 — Critical Pressure Ratio Check (Choked vs. Subcritical)

**Given:** PSV-101 fire case, k = 1.13 (propane vapor), relieving pressure P1 = 289.7 psia (companion Flare Network Design guide basis), two illustrative backpressure cases to compare: (a) P2 = 40 psia, (b) P2 = 200 psia.

**Step 1 — Critical pressure ratio:**
```
rc = [2/(k+1)]^[k/(k−1)]
k/(k−1) = 1.13/0.13 = 8.692
2/(k+1) = 2/2.13 = 0.9390
rc = (0.9390)^8.692 ≈ 0.579
```

**Step 2 — Case (a): low backpressure:**
```
P2/P1 = 40/289.7 ≈ 0.138
0.138 < 0.579  →  CHOKED (critical) flow — the simpler choked-flow API 520 gas equation applies
```

**Step 3 — Case (b): high backpressure:**
```
P2/P1 = 200/289.7 ≈ 0.690
0.690 > 0.579  →  SUBCRITICAL (non-choked) flow — a different, more complex non-choked sizing equation is required
```

**Result:** At the actual (low, choked-flow-consistent) backpressure used in the companion Flare Network Design guide's fire-case sizing, flow is confirmed **choked** — validating that guide's use of the simpler critical-flow sizing equation. Case (b) illustrates why this check matters: at a sufficiently high backpressure, the same PSV would require an entirely different (subcritical) sizing approach, not just a backpressure-correction factor applied to the choked-flow result.

---

### 8.5 Calc Sheet 5 — Inlet Piping Pressure Drop Check

**Given:** PSV-101 fire case, W = 40,373 lb/hr, set pressure = 250 psig, relieving conditions T = 760°R, P ≈ 264.7 psia, MW = 44, Z = 0.9; inlet piping: 4-in Sch 40 (ID 4.026 in), length ≈ 3 m (10 ft), 2 elbows (K = 0.75 each) + entrance (K = 0.5), friction factor f ≈ 0.02.

**Step 1 — Gas density at relieving conditions:**
```
ρ = (P×MW)/(Z×R×T) = (264.7×44)/(0.9×10.73×760) = 11,646.8/7,339.3 ≈ 1.587 lb/ft³
```

**Step 2 — Velocity in 4-in inlet piping:**
```
Area = (π/4)×(0.3355)² ≈ 0.0884 ft²
Volumetric flow = 40,373/1.587 ≈ 25,441 ft³/hr ≈ 7.067 ft³/s
V = 7.067/0.0884 ≈ 79.9 ft/s
```

**Step 3 — Total resistance coefficient, K:**
```
Fittings: 2×0.75 + 0.5 (entrance) = 2.0
Friction: f×(L/D) = 0.02×(10/0.3355) = 0.02×29.8 ≈ 0.596
Total K = 2.0 + 0.596 ≈ 2.596
```

**Step 4 — Pressure drop:**
```
ΔP = K×ρ×V²/(2×gc)
ΔP = 2.596×1.587×(79.9)²/(2×32.2)
ΔP = 2.596×1.587×6,384/64.4 ≈ 408.4 lbf/ft² ≈ 2.84 psi
```

**Step 5 — Compare to API 520 limit (≤3% of set pressure):**
```
Limit = 0.03 × 250 = 7.5 psi
2.84 psi < 7.5 psi  →  PASS
```

**Result:** The inlet piping pressure drop (**≈2.84 psi**) is well within the API 520 3% limit (7.5 psi) — the short, direct inlet piping run is adequate and does not risk valve chatter or capacity reduction.

---

### 8.6 Calc Sheet 6 — Backpressure Determination & Balanced Bellows Selection

**Given:** PSV-101 set pressure = 250 psig, superimposed backpressure (from normal flare header operating pressure) = 15 psig — **variable**, since it depends on whether other PSVs on the shared header are relieving simultaneously (companion Process Philosophies guide's blowdown/simultaneous relief discussion) — built-up backpressure (from this valve's own relief flow through the header, per companion Flare Network Design guide hydraulics) = 22 psig.

**Step 1 — Built-up backpressure as % of set pressure:**
```
22/250 × 100% ≈ 8.8%
8.8% < 10% (conventional PSV built-up limit)  →  Would PASS on built-up alone
```

**Step 2 — Total backpressure during relief:**
```
Total = Superimposed + Built-up = 15 + 22 = 37 psig
37/250 × 100% ≈ 14.8%
```

**Step 3 — Check the variability of the superimposed component:**
```
Superimposed backpressure is NOT constant — it depends on whether other PSVs on the
shared header are relieving at the same time, per the shared flare header's operating
philosophy (companion Process Philosophies guide, Section 4.3 of that guide).
```

**Result:** Although the **built-up** backpressure alone (8.8%) would technically satisfy the conventional PSV's 10% limit, the **superimposed** backpressure is variable — and per API 520, a conventional (non-balanced) trim's set pressure and capacity are only reliable when backpressure is constant. **Select a balanced bellows PSV**, not a conventional trim, specifically because of this variability — not because the magnitude of either backpressure component alone exceeds a numeric limit.

> 📌 **Assumption check:** This is exactly the kind of finding that is easy to miss if only the numeric 10%-built-up-backpressure check is performed without separately asking whether the superimposed component is genuinely constant — see the Case Study (Section 12) for a real consequence of exactly this gap.

---

## 9. Sample Datasheets

### 9.1 PSV Relief Scenario Summary — PSV-101

| Scenario | Required Flow | Required Area | Standard Orifice | Governing? |
|---|---|---|---|---|
| Fire case (API 521) | 40,373 lb/hr | 1.708 in² | L (1.838 in²) | ✅ Yes |
| Blocked outlet (liquid) | 150 gpm | 0.288 in² | F (0.307 in²) | No |
| Thermal expansion | 0.30 gpm | 0.0008 in² | D (0.110 in²) | No |
| Two-phase (illustrative) | 20,000 lb/hr | 0.308 in² | G (0.503 in²) | No |

*(Illustrative — the fire case governs for this vessel; a real study would also evaluate utility failure and control valve failure scenarios per Section 3.)*

---

### 9.2 PSV Mechanical & Installation Datasheet — PSV-101

| Parameter | Value |
|---|---|
| Tag No. | PSV-101 |
| Service | V-100 overpressure protection |
| Governing scenario | Fire case |
| Set pressure | 250 psig |
| Selected orifice | L (1.838 in²) |
| Type | Spring-loaded, balanced bellows |
| Reason for balanced bellows | Variable superimposed backpressure — see Calc Sheet 8.6 |
| Total backpressure (superimposed + built-up) | 37 psig (14.8% of set) |
| Inlet piping | 4-in, ≈3 m, 2 elbows + entrance; ΔP ≈ 2.84 psi (PASS, Calc Sheet 8.5) |
| Body/bonnet material | WCC carbon steel |
| Applicable standard | API 520/521, ASME Section VIII |
| Testing | Bench test at commissioning; in-situ test method to be confirmed against site program |

---

## 10. Practical Design Checklist

- [ ] Every credible relief scenario evaluated (fire, blocked outlet, utility failure, control valve failure, thermal expansion, two-phase where applicable) — not just the scenario that "looks" governing by inspection
- [ ] Governing scenario (largest required orifice) explicitly identified and documented — see Section 9.1
- [ ] Gas/vapor sizing confirmed choked (or the correct subcritical equation used instead) via the critical pressure ratio check — see Calc Sheet 8.4
- [ ] Liquid and two-phase scenarios sized with the correct equation/method, not defaulted to the gas equation — see Calc Sheets 8.1–8.3
- [ ] Inlet piping pressure drop checked against the 3% API 520 limit — see Calc Sheet 8.5
- [ ] Backpressure (both built-up and superimposed) determined, with the superimposed component's **variability** explicitly assessed, not just its magnitude — see Calc Sheet 8.6
- [ ] Balanced bellows vs. conventional trim decision documented with its actual justification (magnitude limit exceeded, or variability, or both)
- [ ] Two-phase/liquid-carryover scenarios flagged explicitly for the flare KOD design team (companion Flare Network Design guide)
- [ ] Relief gas composition/heating value for each scenario provided to the flare tip selection team
- [ ] Simultaneous relief combinations checked against the shared flare header, including a dynamic simulation check where warranted (companion Dynamic Simulation and Process Philosophies guides)
- [ ] Maintenance/testing method (bench vs. in-situ) specified and validated as appropriate for the selected valve type and service

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| PSV chattered in service | Excessive inlet piping pressure drop, never checked against the 3% limit | Explicitly calculate inlet pressure drop for every PSV, not just the ones with an obviously long inlet run — see Calc Sheet 8.5 |
| PSV failed to reliably reseat/maintain set pressure | Conventional trim selected despite variable superimposed backpressure | Assess backpressure variability explicitly, not just magnitude against the 10% limit — see Calc Sheet 8.6 and Case Study, Section 12 |
| Thermal relief case skipped entirely for an isolable liquid-filled segment | Assumed "too small to matter" without running even the simplified screening calculation | Run the simplified thermal relief check (Calc Sheet 8.2) for every isolable liquid-filled segment, even though it usually confirms only the smallest standard orifice is needed |
| Flare KOD undersized for an unexpected liquid carryover event | Two-phase/liquid-carryover PSV scenario not flagged to the KOD design team | Explicitly flag every two-phase or liquid-carryover scenario across the relief scenario summary (Section 9.1) for the flare/KOD design team |
| Wrong sizing equation applied (choked assumed without checking) | Critical pressure ratio check skipped, defaulting to the simpler choked-flow equation regardless of actual backpressure | Always calculate and check the critical pressure ratio before applying the choked-flow gas sizing equation — see Calc Sheet 8.4 |

---

## 12. Case Study — Conventional Trim Selected Without Checking for Variable Superimposed Backpressure

> A composite, illustrative case study based on the type of finding commonly encountered during flare system audits following the addition of new relief sources to a shared header — directly related to the companion Process Philosophies guide's blowdown sequencing case study (that guide's Section 12), but focused specifically on PSV trim selection rather than BDV sequencing. Names, tag numbers, and figures are representative, not project-specific.

### 12.1 Background

PSV-101 was originally specified during the plant's single-train design phase (consistent with the companion Process Philosophies guide's case study background) with a **conventional (non-balanced)** spring-loaded trim. At that time, the flare header's superimposed backpressure was effectively constant — with only one train, no scenario existed where a second, independent relief source could vary the header's pressure while PSV-101 was lifting. The built-up backpressure calculation (per this guide's Calc Sheet 8.6 methodology) showed 8.8% of set pressure — comfortably within the 10% conventional-trim limit — and the specification was finalized on that basis, without a formal check of whether the superimposed component might later become variable.

### 12.2 Problem Identified

When the plant's scope grew to include a second processing train (the same scope change described in the companion Process Philosophies guide's case study), the flare header's superimposed backpressure became genuinely **variable** — PSV-101 could now lift while the second train's BDV-201 or its own PSVs were independently relieving into the same header, changing the superimposed pressure PSV-101 saw at the moment of its own lift, in a way the original single-train design basis never considered.

During the flare system audit that accompanied the broader Blowdown Philosophy re-verification (companion Process Philosophies guide, Section 12.3), the review team specifically checked PSV-101's original backpressure basis against this guide's Calc Sheet 8.6 methodology and found that, while the built-up component alone remained within the 10% limit, the now-variable superimposed component meant a **conventional trim was no longer an appropriate selection** — the valve's actual set-pressure accuracy and capacity could not be reliably guaranteed across the full range of credible superimposed backpressure conditions the two-train configuration now created.

### 12.3 Investigation & Recalculation

The team reran the Calc Sheet 8.6 analysis with the two-train configuration's actual backpressure range and confirmed: superimposed backpressure could now vary from roughly 10 psig (only PSV-101's own train's normal operation) up to 25 psig (during a scenario where the second train was simultaneously relieving) — a variation that a conventional trim's spring, referenced only to atmospheric pressure on its bonnet side, cannot compensate for, unlike a balanced bellows design.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **The original PSV specification checked backpressure magnitude only, not variability** — a check that was actually correct and complete for the single-train scope it was performed against, but was never revisited when the scope grew, mirroring the same "scope grew but the governing document wasn't reopened" root cause identified in the companion Process Philosophies guide's parallel case study.
2. **No explicit link between the Blowdown Philosophy re-verification trigger (Section 1.3 of the Process Philosophies guide) and individual PSV trim selection** — the philosophy-level fix (mandatory Blowdown Philosophy reopening on new relief source additions) addressed the flare header capacity question, but didn't automatically extend to re-checking every existing PSV's backpressure-variability-driven trim selection.

### 12.5 Resolution

- PSV-101 (and, upon review, two other conventional-trim PSVs found to share the same now-variable-superimposed-backpressure exposure) were changed out for balanced bellows trim.
- The company's scope-change management procedure (already updated per the companion Process Philosophies guide's case study to require Blowdown Philosophy re-verification) was further expanded to explicitly require: **any addition of a new relief source to a shared flare header must also trigger a re-check of every existing PSV on that header for backpressure-variability-driven trim adequacy**, not just a header capacity check.

### 12.6 Outcome

- The trim changeouts were completed during a planned turnaround, avoiding an unplanned shutdown, but represented an avoidable cost that correct scope-change practice from the outset would have prevented.
- The finding reinforced, from a second independent angle within the same underlying scope-growth event, the same core lesson as the companion Process Philosophies guide's case study: a system-level change (adding a relief source to a shared header) has consequences for **multiple** downstream engineering decisions (header capacity **and** individual PSV trim selection), and a single-point fix that addresses only the most obvious consequence can still leave a related gap unaddressed.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A backpressure check that was correct for the original single-train scope became incorrect once the scope grew, without the check itself ever being wrong | Re-verify backpressure variability assessment (not just magnitude) whenever the shared header's configuration changes, not just the header's total capacity |
| A scope-change fix aimed at one consequence (flare header capacity) doesn't automatically catch a related but distinct consequence (PSV trim adequacy) | Explicitly enumerate every downstream engineering decision a shared-header scope change could affect, not just the most obvious one |
| The same root cause (scope grew, governing document/decision wasn't reopened) can manifest in more than one place from a single underlying event | When a scope-change gap is found in one discipline, proactively check for the same root cause's fingerprint in adjacent disciplines, not just the one where it was first discovered |

---

## 13. Reference Standards

- **API STD 520 Part I & II** — Sizing, Selection, and Installation of Pressure-relieving Devices
- **API RP 521** — Pressure-relieving and Depressuring Systems
- **ASME BPVC Section VIII** — Rules for Construction of Pressure Vessels
- **ISO 4126** (all parts) — Safety devices for protection against excessive pressure
- Leung, J.C. (1986) — original omega-method correlation for two-phase relief sizing (referenced in Calc Sheet 8.3)

---

*This guide is a practical study reference combining standard PSV sizing and design methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific process data, vendor-certified discharge coefficients, and the current edition of API 520/521. This guide should be read alongside the companion Flare Network Design, Depressurization Calculation, Instrumentation Process Datasheet Preparation, Mechanical Datasheet Preparation, Process Philosophies, and Process Safety study guides, since PSV sizing sits at the intersection of relief scenario analysis, mechanical design, and flare system integration those guides each cover in their own detail.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
