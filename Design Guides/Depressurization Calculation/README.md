# 🌡️ Depressurization Calculation — Practical Study Guide

> A field-oriented reference covering the core engineering topics in fire-case and emergency depressurization system design — combining API 521 §5.15 theory with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution.

**Illustrative project used throughout this guide:** a single pressure vessel exposed to an external pool-fire scenario, protected by a full-bore Blowdown Valve (BDV) that vents to the flare header, sized to bring the vessel from MAWP down to the API 521 target pressure within 15 minutes. All numbers below are worked sample calculations for study purposes — always replace with project-specific data and verify with dynamic simulation.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Standards & Guidelines](#2-standards--guidelines)
3. [Blowdown Valve (BDV) Sizing](#3-blowdown-valve-bdv-sizing)
4. [Transient Thermodynamics](#4-transient-thermodynamics)
5. [Two-Phase Blowdown](#5-two-phase-blowdown)
6. [Fire Case Analysis](#6-fire-case-analysis)
7. [Operational Scenarios](#7-operational-scenarios)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Datasheets](#9-sample-datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Offshore Gas Compression Module](#12-case-study--offshore-gas-compression-module)
13. [Reference Standards](#13-reference-standards)

---

## 1. Design Basis & Assumptions

This section is normally issued as a standalone **"Depressurization System Design Basis"** and frozen before BDV sizing and dynamic simulation begin — revisiting the target pressure/time or wall-temperature basis mid-project is a major source of rework (it changes valve trim size, actuator selection, and sometimes vessel/piping metallurgy).

### 1.1 Vessel & Process Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Vessel service | Gas/condensate separator | — |
| MAWP | 500 psig (34.5 barg) | From vessel mechanical datasheet |
| Design temperature (max) | 150 °F (65.5 °C) | — |
| MDMT (as designed) | −20 °F (−29 °C) | Governs low-temperature material check |
| Operating pressure (normal) | 450 psig (31 barg) | — |
| Operating temperature (normal) | 100 °F (37.8 °C) | Taken as T1 for blowdown calc |
| Vessel internal volume | 50 m³ (1,766 ft³) | Including vapor + liquid space |
| Fluid | Lean natural gas, MW ≈ 20 | k ≈ 1.3, Z ≈ 0.9 (initial), 0.85 (post-expansion) |

### 1.2 Codes & Standards Basis
- **API RP 521 §5.15** — depressurization target pressure/time, heat input methodology
- **ASME Section VIII Div. 1/2** — MAWP, MDMT, impact-testing exemption curves
- **ISO 23251** — used where contractually required in lieu of/alongside API 521
- Company/client engineering specification — governs where stricter (e.g., house Cd values, minimum BDV redundancy, target time <15 min for specific services like reactors)

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Target pressure | Lower of 50% MAWP or 100 psig | API 521 §5.15 |
| Target time | 15 minutes from initiation | API 521 §5.15 (some client specs use fixed 100 psig target regardless of MAWP) |
| Depressurization initiation point | Coincident with fire detection / PSV lift, whichever governs | Confirm trigger philosophy with SIL/ESD design |
| BDV discharge coefficient, Cd | 0.8 (typical for full-bore ball/trim valve) | Vendor Cv data preferred once valve selected |
| Isentropic expansion assumption for T2 | Adiabatic, ideal-gas approximation (first pass) | Real project: dynamic simulation (HYSYS/Flarenet/PIPENET) with real EOS |
| Fire heat input environmental factor, F | 1.0 (bare vessel) / 0.3 (fireproofed) | API 521 |
| Liquid level assumption at fire initiation | Normal operating level (not full/empty) | Confirm worst-case level with Operations |
| Minimum design metal temperature check | Required at all wetted/unwetted surfaces exposed to blowdown-cooled fluid, including downstream piping/valve body | Frequently missed for BDV downstream piping, not just the vessel |
| BDV redundancy | Single valve typically acceptable if reliability meets SIL target; dual valves common for critical/large inventories | Per SIL/LOPA study |

> ⚠️ **Practical note:** Always confirm whether the client's target is literally "15 minutes" or a stricter internal standard (some LNG/reactor specs require 10 minutes or less) — this single number drives BDV trim size and can materially change valve cost and actuator torque/response requirements.

---

## 2. Standards & Guidelines

### 2.1 API 521 §5.15 — Fire Case Depressurization Requirements
- Target: reduce vessel pressure to **the lower of 50% of MAWP or 100 psig (690 kPag)** within **15 minutes** of depressurization initiation.
- Applies to vessels where fire exposure could otherwise heat the vapor space wall above its strength-reduction/rupture threshold before the PSV alone can adequately protect it — depressurization is a *risk-reduction* measure that works alongside (not instead of) the PSV.
- The 15-minute clock typically starts at **detection/initiation of depressurization**, not at the moment of fire ignition — confirm the project's philosophy, since fire detection + ESD logic delay can consume part of the available margin.

### 2.2 ASME Code Links — MAWP & MDMT
- **MAWP** sets the starting pressure basis and the 50% target.
- **MDMT** is the critical downstream constraint: as the vessel/piping depressurizes, metal temperature can fall well below MDMT, risking **brittle fracture** in carbon steel not rated for the resulting temperature. This is the single most common finding in depressurization studies — see Calc Sheet 8.3.
- Impact-testing exemption curves (ASME VIII Div.1 UCS-66) are used to check whether the *existing* material is exempt at the *calculated* minimum metal temperature, or whether low-temperature material (LTCS, SS, or impact-tested CS) is required for the vessel, BDV body, and downstream piping.

### 2.3 ISO 23251
Internationally harmonized equivalent of API 521 — used where contractually specified (common on European/Middle East/multinational projects); depressurization methodology is functionally aligned with API 521 §5.15.

---

## 3. Blowdown Valve (BDV) Sizing

### 3.1 Blowdown Valves (BDVs)
- Typically **full-bore ball or gate valves** (minimal pressure drop when fully open) with a fail-open (fail-safe) actuator, fast stroke time (commonly ≤ 30–60 seconds full-stroke, sometimes faster for critical services).
- Located as close as practical to the vessel nozzle to minimize trapped inventory between the vessel and the valve.

### 3.2 Sizing Criteria
- Must simultaneously satisfy:
  1. **Depressurization target** (pressure/time per Section 2.1)
  2. **Flare system capacity** — the BDV's peak flow adds to (or shares timing with) other simultaneous relief/blowdown sources; oversizing the BDV can overload the flare header even though it helps the vessel individually.
- **Practical tip:** BDV peak flow occurs at t=0 (highest driving ΔP) and decays as vessel pressure falls — this peak, not the average flow, governs both the valve trim size and the flare header's instantaneous capacity check.

### 3.3 Choked Flow Analysis
- Flow through the BDV orifice/trim is **choked (sonic)** whenever the downstream-to-upstream pressure ratio is below the critical pressure ratio:
```
(P2/P1)_critical = [2/(k+1)]^(k/(k-1))
```
- For typical hydrocarbon gas (k ≈ 1.2–1.3), the critical ratio is roughly 0.55–0.58 — since flare header pressure is almost always far below vessel pressure during a fire-case blowdown, **flow is choked for nearly the entire depressurization event** until the vessel pressure approaches the header pressure late in the transient.
- Choked flow means mass flow depends only on **upstream** conditions (P1, T1) — this simplifies sizing but also means the flow rate tracks vessel pressure directly as it decays.

---

## 4. Transient Thermodynamics

### 4.1 Pressure–Temperature Coupling
- Rapid depressurization is close to an **adiabatic expansion** (too fast for significant heat transfer from the fire or surroundings to fully offset the cooling) — gas temperature drops as pressure drops.
- Typical drops of **50–100 °F (28–56 °C)** are common for moderate pressure ratios; higher pressure ratios (e.g., high-pressure gas systems blown down to near-atmospheric) can produce considerably larger drops — see Calc Sheet 8.3 for a worked example showing a larger drop at a high pressure ratio.

### 4.2 Joule-Thomson Cooling
- Expansion through the BDV restriction itself causes **additional local cooling** beyond the bulk vessel gas-phase cooling — this is most severe immediately downstream of the valve trim and in the downstream piping/spool, not just inside the vessel.
- **Practical experience:** The coldest metal temperature in the system is very often **downstream of the BDV**, not in the vessel itself — this piping/valve body is frequently overlooked in MDMT checks that focus only on the vessel.

### 4.3 Energy Balance Equations
- A rigorous transient model accounts for:
  - Heat input from the fire (API 521 heat absorption equation, Section 6.2)
  - Cooling from gas expansion leaving through the BDV
  - Vessel wall thermal mass/heat transfer (wall lags behind bulk gas temperature — wall temperature drop is usually less severe and slower than the gas temperature drop)
- **Practical tip:** Hand calculations (Section 8) are useful for first-pass valve sizing and MDMT screening, but final designs are verified with **dynamic simulation** (e.g., Aspen Flare System Analyzer, PIPENET Transient, or HYSYS Dynamics) that solves the coupled mass/energy balance with a real equation of state — hand calcs using ideal-gas/isentropic shortcuts can be non-conservative for real gases near their critical point.

---

## 5. Two-Phase Blowdown

### 5.1 Gas–Liquid Separation
- If the vessel contains liquid (or if gas condenses out during the pressure/temperature drop), **liquid presence reduces the effective venting rate** through the BDV, since the valve now passes a lower-density, lower-sonic-velocity two-phase mixture instead of pure vapor.
- Vessels with a liquid inventory (separators, knockout drums, reflux drums) need the two-phase case checked explicitly — sizing on vapor-only choked flow can be non-conservative (the target time may not actually be met).

### 5.2 API 521 Two-Phase Correlations
- API 521 provides guidance for two-phase blowdown estimation, but in practice most projects go directly to **rigorous dynamic simulation with a process EOS (Peng-Robinson/SRK)** for two-phase and retrograde-condensation systems, since hand correlations are approximate for compositionally complex streams (rich gas, gas-condensate).

### 5.3 Phase Behavior — Retrograde Condensation
- **Gas-condensate systems can drop liquid out during depressurization** even though they start as a single vapor phase — this is a retrograde condensation effect as the system crosses into the two-phase envelope on the way down in pressure/temperature.
- **Practical tip:** Always run a flash/phase envelope check (not just a bulk P/T trace) for rich-gas or condensate systems — a system that "looks like dry gas" at operating conditions can generate a meaningful liquid fraction partway through blowdown, which then affects both BDV two-phase flow capacity and KOD/flare liquid loading downstream.

---

## 6. Fire Case Analysis

### 6.1 Target Pressure Reduction
- **50% of MAWP, or 100 psig (690 kPag), whichever is lower**, within **15 minutes**.
- Example: MAWP = 500 psig → 50% MAWP = 250 psig; since 100 psig < 250 psig, the **governing target is 100 psig** (see Calc Sheet 8.1–8.3, which use this exact case).

### 6.2 Heat Input Calculation (API 521)
- Uses the same wetted-area fire-heat-absorption equation applied for PSV fire-case sizing:
```
Q = 21,000 × F × A^0.82   (Btu/hr, A in ft², A ≤ 2,800 ft²)
```
- For depressurization wall-temperature checks, the **unwetted (vapor space) surface area** is often the governing region of interest, since it heats faster (no liquid heat sink) and is the area most likely to see combined fire-heating + blowdown-cooling stress.

### 6.3 Wall Temperature Limits
- The vessel wall must stay **below the temperature at which the material's allowable stress drops enough to risk rupture** under fire exposure (API 521 provides a wall-temperature-vs-time strength-reduction check), while the **downstream/expansion-side metal must stay above its MDMT** during blowdown cooling.
- These are two *different* failure modes at two different locations and times in the same event — fire-side rupture (too hot, vapor-space wall) vs. brittle fracture (too cold, BDV/downstream piping) — both must be checked, not just one.

---

## 7. Operational Scenarios

### 7.1 Emergency Shutdown (ESD) — Fire or Runaway Reaction
- Automatic, ESD-initiated depressurization on confirmed fire detection (or high-high pressure/temperature for a runaway reaction case) — BDV opens automatically per the safety instrumented function (SIF) logic; this is the scenario Sections 2–6 and the calc sheets are built around.

### 7.2 Pipeline Isolation — Blowdown Between Block Valves
- Depressurizing an isolated pipeline segment (between two block valves) for maintenance — typically much smaller inventory than a process vessel, but long, cold pipeline sections can still see significant temperature drop; check pipeline MDMT and any buried/insulated sections for frost heave or condensation risk.

### 7.3 Maintenance Depressurization — Controlled Reduction
- Slower, operator-controlled reduction (not the fast ESD case) for inspection/repair — governed by operating procedures rather than the 15-minute API 521 target, but still needs a temperature-drop check (slow controlled blowdown can still produce meaningful cooling if the total pressure ratio is large) and a venting/flaring plan for the vented inventory.

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific vessel data, dynamic simulation, and vendor valve Cv curves.

### 8.1 Calc Sheet 1 — Governing Target Pressure & Time

**Given:**
- MAWP = 500 psig
- 15-minute target time per API 521 §5.15

**Step 1 — Compare 50% MAWP vs. 100 psig:**
```
50% × MAWP = 0.50 × 500 = 250 psig
100 psig (fixed) < 250 psig
```

**Result:** Governing target pressure = **100 psig**, to be reached within **15 minutes (900 seconds)** of depressurization initiation. This is the target used in Calc Sheets 8.2–8.3.

> 📌 **Assumption check:** If the client spec uses a fixed 690 kPag target rather than "lower of 50%/100 psig," confirm which governs — for lower-MAWP vessels (e.g., MAWP < 200 psig), 50% MAWP can become the governing (lower) target instead of 100 psig.

---

### 8.2 Calc Sheet 2 — Mass Inventory & Isentropic Temperature Drop

**Given (from Section 1 basis):**
- V = 50 m³, MW = 20 kg/kmol, k = 1.3
- P1 = 500 psig = 3,551 kPag → **P1(abs) = 3,652 kPa**, T1 = 100 °F = 37.8 °C = **311 K**, Z1 = 0.9
- P2 = 100 psig = 690 kPag → **P2(abs) = 791 kPa**, Z2 = 0.85 (post-expansion, lower T)

**Step 1 — Initial mass in vessel (real gas):**
```
m1 = (P1 × V × MW) / (Z1 × R × T1),   R = 8.314 kJ/kmol·K
m1 = (3,652 × 50 × 20) / (0.9 × 8.314 × 311)
m1 = 3,652,000 / 2,327.8
m1 ≈ 1,569 kg
```

**Step 2 — Isentropic (adiabatic, ideal-gas approx.) final temperature:**
```
T2 = T1 × (P2/P1)^[(k−1)/k]
(k−1)/k = 0.3/1.3 = 0.2308
P2/P1 = 791/3,652 = 0.2166
T2 = 311 × (0.2166)^0.2308
T2 = 311 × 0.7027
T2 ≈ 218.6 K = −54.5 °C = −66 °F
```

**Step 3 — Final mass in vessel at target state:**
```
m2 = (P2 × V × MW) / (Z2 × R × T2)
m2 = (791 × 50 × 20) / (0.85 × 8.314 × 218.6)
m2 = 791,000 / 1,544.9
m2 ≈ 512 kg
```

**Step 4 — Mass to be vented:**
```
Δm = m1 − m2 = 1,569 − 512 ≈ 1,057 kg
```

**Result:** Calculated bulk gas-temperature drop ≈ **111 °F (62 °C)**, and **≈1,057 kg** must be vented through the BDV within 900 seconds.

> 📌 **Assumption check:** This 111 °F drop is on the higher end of the "typical 50–100 °F" range quoted in industry guidance because this example uses a large pressure ratio (P1/P2 ≈ 4.6). Systems with a smaller pressure ratio, or where fire heat input partially offsets the expansion cooling, will show a smaller drop — this is exactly why a **case-specific** calculation (not a rule-of-thumb 50–100 °F assumption) is required for MDMT verification. Also note: this ideal-gas isentropic shortcut is a first-pass estimate — real gas behavior near the critical point can produce a *larger* actual drop than the ideal-gas estimate, which is why dynamic simulation with a real EOS is required for final MDMT design.

---

### 8.3 Calc Sheet 3 — MDMT Screening Check

**Given (from Calc Sheet 2):**
- Calculated minimum bulk gas temperature, T2 = −54.5 °C
- Vessel MDMT (as designed) = −29 °C
- BDV body / downstream piping: assume carbon steel, standard MDMT rating ≈ −29 °C (same as vessel, typical default) unless otherwise specified

**Step 1 — Compare calculated minimum temperature to MDMT:**
```
T2 (calculated) = −54.5 °C
MDMT (as designed) = −29 °C
T2 < MDMT  →  FAIL
```

**Result:** The calculated blowdown gas temperature (−54.5 °C) is **well below** the vessel's design MDMT (−29 °C) — the as-designed carbon steel is **not adequate** for this depressurization event without mitigation.

**Typical mitigation options (in order commonly evaluated):**
1. **Re-rate MDMT** — check ASME UCS-66 impact-test exemption curve at the actual calculated metal temperature (wall temperature typically lags bulk gas temperature — a full transient wall-temperature model, not just bulk gas T2, is used for the final code check).
2. **Slow down / restrict the BDV** (reduce peak flow / extend time) — trades off against meeting the 15-minute target; usually not preferred if it violates API 521 timing.
3. **Upgrade material** — low-temperature carbon steel (LTCS) or stainless steel for the vessel (if wall temperature governs) and/or the BDV body + downstream piping spool (very common outcome — the BDV downstream spool is upgraded to LTCS even when the vessel itself is unaffected, since the *local* J-T cooling at the valve is more severe than the bulk vessel gas temperature).
4. **Install additional insulation / heat tracing** on affected piping — less common for a fast ESD event, more relevant for slow maintenance blowdown.

> 📌 **Practical note:** This exact "fails the bulk vessel MDMT but especially fails at the BDV downstream spool" outcome is one of the most common findings in real depressurization studies — always explicitly model/check the piping immediately downstream of the BDV as a separate node, not just the vessel.

---

### 8.4 Calc Sheet 4 — BDV Orifice Sizing (Choked Flow)

**Given:**
- Required average mass flow: `W_avg = Δm / t = 1,057 kg / 900 s ≈ 1.174 kg/s`
- Peak/average flow ratio (typical for an exponential-decay blowdown profile): **1.6** (rule-of-thumb for first-pass sizing; confirm with dynamic simulation)
- Discharge coefficient, Cd = 0.8
- P1(abs) = 3,652 kPa = 3,652,000 Pa, T1 = 311 K, k = 1.3, Z1 = 0.9, MW = 20 kg/kmol

**Step 1 — Peak (design) mass flow:**
```
W_peak = W_avg × 1.6 = 1.174 × 1.6 ≈ 1.878 kg/s
```

**Step 2 — Choked (critical) flow equation:**
```
W = Cd × A × P1 × √[ (k × MW)/(Z × R × T1) × (2/(k+1))^((k+1)/(k−1)) ]
```

**Step 3 — Evaluate the bracketed term:**
```
(k × MW)/(Z × R × T1) = (1.3 × 20) / (0.9 × 8,314 × 311) = 26 / 2,327,089 = 1.117 × 10⁻⁵

(2/(k+1))^[(k+1)/(k−1)]:
  (k+1)/(k−1) = 2.3/0.3 = 7.667
  (2/2.3)^7.667 = (0.8696)^7.667 ≈ 0.342

Combined: 1.117×10⁻⁵ × 0.342 = 3.82 × 10⁻⁶
√(3.82 × 10⁻⁶) = 1.956 × 10⁻³
```

**Step 4 — Solve for required flow area, A:**
```
A = W_peak / (Cd × P1 × 1.956×10⁻³)
A = 1.878 / (0.8 × 3,652,000 × 1.956×10⁻³)
A = 1.878 / 5,714.5
A ≈ 3.286 × 10⁻⁴ m² = 328.6 mm²
```

**Step 5 — Equivalent orifice diameter:**
```
d = √(4A/π) = √(4 × 3.286×10⁻⁴ / 3.1416) = √(4.184×10⁻⁴)
d ≈ 0.0205 m ≈ 20.5 mm ≈ 0.81 in
```

**Result:** Required minimum flow-passing diameter ≈ **20–21 mm (≈0.8 in)**. In practice this is rounded up and cross-checked against a vendor's actual valve Cv/flow coefficient curve — a **1-inch reduced-trim** or **1.5-inch full-bore** BDV would typically be selected here (full-bore valves are sized on standard line sizes, so the calculated minimum diameter is a *check*, not a direct valve-size selection).

> 📌 **Assumption check:** The 1.6 peak/average ratio is a simplified first-pass rule of thumb; the actual peak-to-average ratio depends on the vessel's real P-t decay curve (which itself depends on the valve's flow characteristic and vessel volume/inventory). **Always confirm final trim size with a full transient (dynamic) simulation** that integrates the choked-flow equation against the actual decaying vessel pressure, rather than relying on the average-flow shortcut alone for the final valve selection.

---

### 8.5 Calc Sheet 5 — Two-Phase Dropout Screening (Qualitative/Illustrative)

**Given:**
- Feed composition: lean gas with trace C5+ (gas-condensate tendency)
- Initial state: 500 psig / 100 °F (single-phase vapor, confirmed by phase envelope at operating conditions)
- Final state: 100 psig / −66 °F (from Calc Sheet 2)

**Approach (illustrative — real projects use a process simulator with Peng-Robinson/SRK EOS):**
1. Plot the fluid's phase envelope (P vs. T) using compositional data.
2. Overlay the calculated blowdown P–T trace (500 psig/100 °F → 100 psig/−66 °F) on the envelope.
3. Identify whether/where the trace crosses into the two-phase region.

**Illustrative result:** For a gas-condensate composition of this type, the P–T trace commonly **crosses into the two-phase envelope** somewhere in the mid-blowdown range (e.g., roughly 250–150 psig, well above the final 100 psig target) — meaning liquid dropout should be **expected**, even though the fluid started and often ends up predominantly vapor.

**Practical implications:**
- BDV two-phase flow capacity must be checked (vapor-only choked-flow sizing per Calc Sheet 4 can be non-conservative).
- Downstream KOD must be checked for the additional transient liquid load from blowdown events, not just steady-state PSV liquid carryover.
- The coldest metal temperature may occur **at or near the flash point** in the piping, not necessarily at the final target pressure — the MDMT check (Calc Sheet 3) should scan the **entire** P-T trace, not just the initial and final states.

> 📌 **Practical note:** This is exactly the kind of result that a quick "start and end point" hand calculation misses — always run (or request from process simulation) the full transient P-T-composition trace for gas-condensate systems, not just bookend calculations.

---

## 9. Sample Datasheets

### 9.1 Blowdown Valve (BDV) Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | BDV-101 | — |
| **Service** | Emergency Depressurization | — |
| **Valve Type** | Full-bore Ball Valve | — |
| **Nominal Size** | 1½ | in |
| **Trim/Bore Diameter (confirmed ≥ required)** | 25 (1-in min. per Calc Sheet 4) | mm |
| **End Connections** | Flanged, RF | — |
| **Body Rating** | ASME Class 600 | — |
| **Body Material** | LTCS (A350 LF2) — upgraded per MDMT check (Calc Sheet 3) | — |
| **Actuator Type** | Spring-return pneumatic, fail-open | — |
| **Full Stroke Time** | ≤ 15 | seconds |
| **Fail Position on Air/Signal Loss** | Open (FO) | — |
| **SIL Rating** | SIL 2 (per LOPA) | — |
| **Design Pressure (valve)** | 500 | psig |
| **Design Temperature Range** | −54 to 150 (per Calc Sheet 2/3) | °C |
| **Downstream Piping Material** | LTCS spool, min. 3 m from valve outlet | — |
| **Cv (vendor confirmed)** | 185 (example) | — |
| **Position Indication** | Open/Close limit switches to DCS/ESD | — |
| **Applicable Code** | API 6D / ASME B16.34 | — |

---

### 9.2 Vessel Depressurization Summary Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Vessel Tag** | V-101 | — |
| **MAWP** | 500 (34.5) | psig (barg) |
| **Design Temperature** | 150 (65.5) | °F (°C) |
| **MDMT (as-designed)** | −20 (−29) | °F (°C) |
| **Internal Volume** | 50 (1,766) | m³ (ft³) |
| **Governing Target Pressure** | 100 (6.9) | psig (barg) |
| **Target Time** | 15 | min |
| **Initial Bulk Temperature (T1)** | 100 (37.8) | °F (°C) |
| **Calculated Final Bulk Temperature (T2)** | −66 (−54.5) | °F (°C) |
| **Mass Vented (Δm)** | 1,057 (2,330) | kg (lb) |
| **Peak Mass Flow Rate** | 1.88 (6,764) | kg/s (kg/hr) |
| **MDMT Check Result** | FAIL as-designed → LTCS upgrade required (BDV + 3 m downstream spool) | — |
| **Two-Phase Dropout Expected?** | Yes — screening indicates dropout ~250–150 psig range | — |
| **Associated BDV Tag** | BDV-101 | — |
| **Initiation Logic** | Fire & Gas detection (2oo3) → ESD Level 1 | — |

---

### 9.3 Fire Case / Depressurization Cause-and-Effect Summary

| Initiating Event | Trigger | Action | Target |
|---|---|---|---|
| Confirmed fire (2oo3 F&G detectors) in Zone A | High confidence fire signal | Open BDV-101, close inlet/outlet ESDVs on V-101 | 100 psig within 15 min |
| High-High Pressure, V-101 (PSHH) | Independent of fire detection | PSV-101 lifts (mechanical protection, always available) | Per PSV set pressure — protects MAWP regardless of BDV action |
| Manual ESD pushbutton | Operator-initiated | Same as confirmed fire logic | Same target |
| Loss of cooling water (upstream unit) | Process trip | Evaluate separately — may not require depressurization if PSV alone is adequate | Per unit-specific relief study |

---

## 10. Practical Design Checklist

- [ ] Design basis issued and approved (Section 1) before BDV sizing begins
- [ ] Governing target pressure identified (lower of 50% MAWP or 100 psig) — see Calc Sheet 8.1
- [ ] Initiation logic and timing basis confirmed with SIL/ESD philosophy (does the 15-min clock include detection delay?)
- [ ] Mass inventory and isentropic temperature drop calculated for the governing case — see Calc Sheet 8.2
- [ ] MDMT check performed for **vessel wall**, **BDV body**, and **downstream piping spool** separately — see Calc Sheet 8.3
- [ ] BDV choked-flow orifice sizing completed and cross-checked against vendor Cv curve — see Calc Sheet 8.4
- [ ] Peak (not just average) BDV flow checked against flare header simultaneous-load capacity
- [ ] Two-phase / retrograde condensation screening performed for gas-condensate or rich-gas systems — see Calc Sheet 8.5
- [ ] Full P-T transient trace (not just start/end points) reviewed against the phase envelope for two-phase systems
- [ ] Fire-side wall temperature (rupture) check performed separately from cold-side MDMT (brittle fracture) check
- [ ] Dynamic simulation performed to verify hand-calc sizing before finalizing valve trim/actuator
- [ ] BDV fail-safe position, stroke time, and SIL rating confirmed against LOPA/SIL study
- [ ] Datasheets (BDV, vessel depressurization summary, cause-and-effect) issued for vendor/EPC use

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| BDV downstream piping found to be under-rated for MDMT during detailed engineering | Only the vessel MDMT was checked, not the local J-T cooling at the valve outlet | Model the BDV outlet spool as a separate node; upgrade to LTCS/SS as needed (Calc Sheet 8.3) |
| Flare header overloaded during simultaneous fire + BDV event | BDV peak flow not included in the simultaneous relief cause-and-effect matrix | Add BDV peak flow explicitly to the flare hydraulic simultaneous-case model |
| Depressurization target not met in dynamic simulation despite hand-calc "passing" | Hand calc used average flow / ideal-gas shortcuts; real transient decay is slower initially | Always verify final trim size with dynamic (transient) simulation, not the average-flow hand calc alone |
| Unexpected liquid slug at flare KOD during a blowdown event | Two-phase dropout not screened for a nominally "dry gas" system | Run full P-T trace against phase envelope for any gas-condensate composition, however lean it appears at operating conditions |
| BDV actuator too slow to meet target stroke assumptions | Actuator sizing done generically, not against the project's specific stroke-time requirement feeding the transient model | Confirm actual vendor stroke time and re-run transient sizing with the real (not assumed) valve opening profile |
| MDMT re-rate disputed during code compliance review | Screening used bulk gas T2 only, not a proper transient wall-temperature/UCS-66 exemption curve check | Perform the full ASME UCS-66 exemption-curve check using calculated *metal* temperature (which lags gas temperature), not just the bulk fluid T2 |

---

## 12. Case Study — Offshore Gas Compression Module

> A composite, illustrative case study based on the type of finding commonly encountered during detailed engineering / HAZOP close-out on offshore gas compression modules. Names, tag numbers, and figures are representative, not project-specific.

### 12.1 Background

An offshore platform's gas compression module included a high-pressure (HP) suction scrubber (V-201) feeding a two-stage compressor train. The scrubber operated at 950 psig / 90 °F, with an MAWP of 1,000 psig, MDMT of −20 °F (−29 °C), and an internal volume of 12 m³. A single BDV (BDV-201, 2-inch full-bore ball valve, CS body) had been specified at FEED stage based on a generic "similar service" sizing philosophy carried over from a previous project, rather than a project-specific calculation.

### 12.2 Problem Identified

During detailed engineering, the process safety team re-ran the depressurization study for V-201 as part of routine HAZOP close-out. Two issues surfaced:

1. **Timing:** Using the as-specified 2-inch BDV, dynamic simulation showed the vessel reached only ~145 psig at 15 minutes — **missing the 100 psig target** (the governing target here, since 50% MAWP = 500 psig > 100 psig).
2. **MDMT:** The simulation's minimum predicted metal temperature at the BDV outlet spool was **−61 °C**, far below the vessel and downstream piping's as-built MDMT of −29 °C — indicating a **brittle fracture risk** during a real fire-case blowdown event.

Both findings had been missed at FEED because the BDV had been "sized by analogy" rather than calculated from this vessel's actual MAWP, volume, and target time/pressure.

### 12.3 Investigation & Recalculation

The engineering team reran the sizing using the same method shown in Calc Sheets 8.1–8.4 of this guide:

- **Governing target (Calc Sheet 8.1 method):** 50% MAWP (500 psig) vs. 100 psig fixed → **100 psig governs**.
- **Mass/temperature calc (Calc Sheet 8.2 method):** Using V-201's actual P1 = 950 psig, T1 = 90 °F, V = 12 m³, MW = 22 (richer gas than the illustrative example in this guide) — recalculated ΔT ≈ 130 °F drop, confirming the large predicted cooling was realistic, not a simulation artifact.
- **BDV resizing (Calc Sheet 8.4 method):** Recomputing required orifice area for the *actual* 100 psig/15 min target (not the previously assumed generic sizing) showed the required minimum flow diameter was closer to **34 mm (~1.3 in)** — meaning the as-specified 2-inch valve's *actual installed trim* (which had a restricted internal bore due to a non-full-bore ball originally selected) was undersized relative to what the nameplate size implied. The nominal "2-inch" valve did not deliver 2-inch full-bore flow area.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **Sizing-by-analogy at FEED** instead of a vessel-specific calculation — the "similar service" BDV from a prior project had a different MAWP/volume/target combination and was not re-verified for this vessel.
2. **Valve procurement specification gap** — "2-inch full-bore ball valve" was specified without explicitly calling out minimum bore diameter/Cv, allowing a vendor-standard reduced-bore trim to be quoted and initially accepted.

### 12.5 Resolution

- BDV-201 was re-specified as a true full-bore 2-inch valve with a **minimum guaranteed bore of 50 mm**, confirmed against vendor Cv data before purchase order issue.
- The 3 m of piping immediately downstream of BDV-201 was upgraded from standard CS to **LTCS**, consistent with the MDMT screening outcome shown in Calc Sheet 8.3 of this guide.
- The vessel body MDMT itself was confirmed adequate (bulk wall temperature, accounting for thermal mass/lag, stayed within the exemption curve) — only the **local downstream spool and valve body** required the material upgrade, avoiding a costlier vessel re-rate.
- Dynamic simulation was re-run with the corrected valve Cv and upgraded spool, confirming the target (100 psig within 15 minutes) was met with margin.

### 12.6 Outcome

- Valve and piping spool changes were implemented during the procurement/fabrication window, avoiding offshore rework — but the finding surfaced late enough (post-FEED) that it required an engineering change notice (ECN) and a schedule float of approximately three weeks to re-issue the affected isometrics and valve datasheet.
- The finding was flagged as a **lessons-learned item** for the company's engineering standard: BDV sizing-by-analogy was prohibited going forward; every BDV now requires a vessel-specific calculation sheet (per Section 8 of this guide) and an explicit minimum-bore call-out in the valve requisition.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| "Similar service" BDV sizing from a prior project is not a substitute for a vessel-specific calculation | Mandate Calc Sheets 8.1–8.4 methodology (or equivalent dynamic simulation) for every BDV, every project |
| Nominal valve size does not guarantee full-bore flow area | Always specify minimum bore diameter/Cv explicitly in the valve requisition, not just "full-bore" as a description |
| MDMT findings can apply to downstream piping even when the vessel itself is fine | Always model the BDV outlet spool as its own node (Calc Sheet 8.3) |
| Late-stage (post-FEED) discovery of sizing gaps causes schedule impact | Run the depressurization calc sheet during FEED, not just at detailed engineering/HAZOP close-out, so any BDV or MDMT gap is caught before procurement commitments are made |

---

## 13. Reference Standards

- **API RP 521** — Pressure-relieving and Depressuring Systems (§5.15 — Depressurization)
- **API STD 520** (Parts I & II) — Sizing, Selection, and Installation of Pressure-relieving Devices
- **ASME BPVC Section VIII, Div. 1** — Rules for Construction of Pressure Vessels (MAWP, UCS-66 MDMT exemption curves)
- **ISO 23251** — Petroleum, petrochemical and natural gas industries — Pressure-relieving and depressuring systems
- **API 6D / ASME B16.34** — Valve design/rating standards commonly referenced for BDV specification

---

*This guide is a practical study reference combining standard depressurization design theory with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific design basis, vendor data, dynamic simulation results, and current regulatory/code requirements.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
