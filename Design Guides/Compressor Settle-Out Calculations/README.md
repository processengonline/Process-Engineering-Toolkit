# ⚙️ Compressor Settle-Out Calculations — Practical Study Guide

> A field-oriented reference covering the core engineering topics in compressor settle-out pressure analysis — combining mass/energy balance theory with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design** and **Depressurization Calculation** study guides — settle-out pressure is frequently the governing initial condition for both.

**Illustrative project used throughout this guide:** a single-stage centrifugal compressor on natural gas service, tripping from normal operation with both suction- and discharge-side isolation valves closing (or check valves preventing backflow), leaving the suction and discharge inventories to mix and equalize within the trapped volume. All numbers below are worked sample calculations for study purposes — always replace with project-specific PVT and mechanical data.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Fundamentals of Settle-Out Pressure](#2-fundamentals-of-settle-out-pressure)
3. [Volume & Inventory Considerations](#3-volume--inventory-considerations)
4. [Thermodynamics of Mixing](#4-thermodynamics-of-mixing)
5. [Dynamic vs. Static Methods](#5-dynamic-vs-static-methods)
6. [Impact on Flare System Design](#6-impact-on-flare-system-design)
7. [Special Scenarios](#7-special-scenarios)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Datasheets](#9-sample-datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Multi-Stage Compressor Trip Exceeding Downstream MAWP](#12-case-study--multi-stage-compressor-trip-exceeding-downstream-mawp)
13. [Reference Standards](#13-reference-standards)

---

## 1. Design Basis & Assumptions

Settle-out calculations are normally issued as part of the **"Compressor System Design Basis"** or a standalone **"Settle-Out Pressure Study"**, and must be frozen (or at least bounded) before compressor casing, piping class, and downstream vessel MAWP are finalized — settle-out pressure is very often the **governing design pressure case**, higher than either the normal suction or normal discharge operating pressure alone would suggest at first glance for shared/interconnected piping.

### 1.1 Compressor & System Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Compressor type | Single-stage centrifugal | Multi-stage extension covered in Section 7.1 / Calc Sheet 8.2 |
| Gas | Natural gas, MW ≈ 18 | k ≈ 1.27 |
| Suction volume (drum + piping + compressor internals) | 15 m³ | See Section 3.1 for what to include |
| Suction pressure (normal) | 800 psia (55.2 bara) | Taken as P_s for the trip case |
| Suction temperature (normal) | 100 °F (37.8 °C, 311 K) | — |
| Suction gas compressibility, Z_s | 0.88 | At suction conditions |
| Discharge volume (piping + cooler + downstream vessel up to first isolation) | 8 m³ | See Section 3.1 |
| Discharge pressure (normal) | 2,500 psia (172.4 bara) | Taken as P_d for the trip case |
| Discharge temperature (normal) | 250 °F (121.1 °C, 394 K) | — |
| Discharge gas compressibility, Z_d | 0.82 | At discharge conditions |
| Downstream vessel MAWP (governing) | 1,500 psig | Confirm against actual mechanical datasheet |

### 1.2 Codes & Standards / Methodology Basis
- **API 521** — general guidance referencing settle-out pressure as a design-pressure-basis input for casings/piping/flare systems
- **API 617 / API 618** — compressor mechanical design standards (casing MAWP must accommodate settle-out, not just normal operating pressure)
- Equation of state: **Peng-Robinson** or **Soave-Redlich-Kwong (SRK)** for accurate Z-factor and phase behavior, especially for rich-gas or near-critical streams
- Static (hand-calc) mass/energy balance for screening; **dynamic simulation** (HYSYS, Aspen Plus/HYSYS Dynamics, or equivalent) for detailed design and flare load prediction

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Trip scenario | Both suction and discharge isolation valves close (or check valve prevents backflow), trapping suction + discharge inventory together | Confirm actual isolation valve/check valve philosophy — some designs trap additional volume (e.g., recycle loop) |
| Mixing process | Adiabatic, constant-volume (no heat transfer during the short mixing transient, no shaft work after trip) | Standard first-pass assumption; real systems have some heat loss over longer timeframes |
| Z-factor for settle-out state | Estimated first pass as inventory-weighted average of Z_s and Z_d, then iterated with EOS at calculated (P_so, T_so) | Iteration is important — a single-pass average Z can introduce meaningful error near the phase envelope |
| Anti-surge/recycle valve response | Confirm whether recycle valve opens or closes on trip, and whether recycle loop volume is included in the trapped inventory | This materially changes the effective mixing volume — see Section 7.3 |
| Downstream isolation point | First ESDV or check valve downstream of the compressor discharge that would actually trap the inventory | Confirm actual P&ID isolation philosophy, not just "the cooler" or "the next vessel" by default |
| Multi-stage case | Each stage settle-out calculated independently unless interstage piping allows cross-communication | Confirm interstage block valve philosophy — see Section 7.1 |

> ⚠️ **Practical note:** Settle-out pressure studies are frequently revisited late in a project (or even post-startup) when the actual as-built isolation valve philosophy differs from the original P&ID assumption used at FEED — always re-verify the trapped-volume boundary against the as-built P&ID before finalizing casing/piping MAWP, not just the design-stage P&ID.

---

## 2. Fundamentals of Settle-Out Pressure

### 2.1 Definition
Settle-out pressure is the **single, uniform pressure** reached once gas trapped in the compressor's suction-side and discharge-side volumes mixes and equalizes following a trip — the compressor is no longer adding energy, isolation valves (or check valves) have trapped the inventory, and pressure/temperature gradients dissipate over a short transient until the whole trapped volume reaches one common condition.

### 2.2 Importance
- **Compressor casing design pressure:** The casing must be rated for settle-out pressure, not just normal discharge pressure — settle-out is frequently the **governing MAWP case** for the casing.
- **Piping design pressure:** Suction-side piping, valves, and instrumentation must also be rated for settle-out pressure if they remain in the trapped volume, even though their *normal* operating pressure is much lower (the suction side, in particular, sees a pressure rise well above its normal operating range).
- **Flare system design:** If a relief/blowdown path exists, the settle-out condition becomes the **initial state (P1, T1)** for the subsequent depressurization/relief calculation (see Section 6 and Calc Sheet 8.3, and the companion Depressurization Calculation guide).

### 2.3 Key Equation
Settle-out pressure is found from a **combined mass and energy balance** across the suction and discharge volumes:
- **Mass balance:** total moles (or mass) trapped = moles initially in the suction volume + moles initially in the discharge volume (conserved — nothing enters or leaves the trapped boundary).
- **Energy balance:** internal energy is conserved during the adiabatic mixing process, which (for an ideal-gas-like approximation with a single Cv) reduces to a mole-weighted average temperature; a real-gas calculation instead solves the coupled energy balance with an EOS.
- **Equation of state:** the mixed inventory's final pressure at the combined volume and settle-out temperature is then found from the real-gas law (or full EOS), not the ideal gas law, for any meaningfully non-ideal system.

---

## 3. Volume & Inventory Considerations

### 3.1 Suction Volume
Includes everything on the suction side that will be trapped by the isolation philosophy at trip:
- Suction scrubber/drum
- Suction piping up to the isolation valve (or check valve boundary)
- Compressor internals on the suction side (impeller eye through to the diffuser, for centrifugal machines)

### 3.2 Discharge Volume
Includes everything on the discharge side similarly trapped:
- Discharge piping
- Aftercooler(s)
- Downstream vessel(s) up to the first isolation point

**Practical tip:** The discharge volume boundary is the single most common source of error in settle-out studies — teams sometimes stop the discharge volume at the cooler outlet when the actual downstream ESDV is much further downstream (e.g., after a knockout drum), which under-states both the trapped inventory and the resulting settle-out pressure's true governing scope.

### 3.3 Gas Inventory
- **Composition** matters directly (through MW and k) and indirectly (through the EOS-predicted Z-factor and any phase behavior near the settle-out condition).
- **Compressibility factor (Z)** for both the suction-side and discharge-side gas, and for the final settle-out condition, should be calculated (or at minimum, checked) with a real EOS rather than assumed as 1.0 — for high-pressure gas systems, ideal-gas assumptions can meaningfully under- or over-predict the resulting pressure.

---

## 4. Thermodynamics of Mixing

### 4.1 Energy Balance — Adiabatic vs. Isothermal
- **Adiabatic mixing** (no heat transfer during the short mixing transient) is the standard first-pass assumption — internal energy is conserved, and for a constant-volume, no-work process this reduces (for near-ideal gas behavior) to a mole-weighted average temperature.
- **Isothermal approximation** (assuming settle-out temperature equals some fixed reference, e.g., ambient) is sometimes used as an additional conservative bound, but is not physically representative of the near-term post-trip transient — use it only as a sensitivity case, not the primary design basis.

### 4.2 Temperature Effects
- Settle-out temperature can be **higher or lower** than either the original suction or discharge temperature, depending on the relative inventory (moles) and temperature of each side — a large, hot discharge inventory mixing with a smaller, cooler suction inventory pulls the blended temperature toward the discharge condition, and vice versa (see Calc Sheet 8.1 for a worked example).
- High compression ratio machines (large T_d − T_s) show the largest sensitivity to this effect — always calculate rather than assume settle-out temperature is simply "somewhere in the middle."

### 4.3 Equation of State (EOS)
- **Peng-Robinson (PR)** or **Soave-Redlich-Kwong (SRK)** EOS are standard for real-gas Z-factor and phase behavior prediction in settle-out studies, particularly important for:
  - Rich/high-MW gas streams
  - Systems operating near their phase envelope (risk of partial condensation during cooling/mixing)
  - High-pressure systems where ideal-gas assumptions break down significantly

---

## 5. Dynamic vs. Static Methods

### 5.1 Static Calculation
A simple mass balance (and mole-weighted energy balance) between the suction and discharge volumes, solved as a single equilibrium state with no time dependency — this is the method worked through in Section 8 of this guide.
- **Advantages:** Fast, transparent, good for screening and early design-pressure-basis decisions.
- **Limitations:** Does not capture the actual transient path (how quickly settle-out is reached, whether check valves actually close in time, whether recycle valve response changes the trapped volume mid-transient).

### 5.2 Dynamic Simulation
Time-dependent modeling (HYSYS Dynamics, Aspen Plus Dynamics, or similar; OLGA is more commonly used for pipeline/multiphase transient work rather than compressor settle-out specifically, though it may appear in an integrated flow assurance + compressor system model) that solves the coupled mass/momentum/energy equations through the actual trip transient.
- **Advantages:** Captures valve stroke timing, check valve response, recycle/anti-surge valve behavior, and any partial condensation during the transient — often reveals a different (sometimes higher) peak pressure than the static equilibrium calculation, especially if a check valve is slow to seat.
- **Limitations:** Requires more engineering effort/time and detailed valve/actuator data; not justified for early screening.

### 5.3 When to Use Which
| Method | Use Case |
|---|---|
| Static | Early screening, design-pressure-basis first pass, simple single-stage systems with well-defined trapped volumes |
| Dynamic | Detailed design, final casing/piping MAWP confirmation, flare load prediction, any system with recycle/anti-surge interaction or check-valve timing sensitivity (see Section 7.3 and the Case Study in Section 12) |

---

## 6. Impact on Flare System Design

### 6.1 Flare Load
If the settle-out pressure exceeds the downstream system's allowable operating pressure (or if a planned blowdown is initiated after a trip to protect equipment or enable maintenance), the settle-out condition becomes the **initial state (P1, T1)** for the subsequent blowdown valve (BDV) sizing calculation — see Calc Sheet 8.3, which follows the same choked-flow methodology as the companion **Depressurization Calculation** guide, but starting from the settle-out condition rather than normal operating pressure.

### 6.2 Knock-Out Drum Sizing
The flare KOD downstream of any settle-out-driven blowdown must be checked against the settle-out gas volume/composition, which can differ meaningfully from the normal-operation relief case (different temperature, potentially different phase behavior if the settle-out condition is near the phase envelope) — do not assume the KOD design basis from a normal PSV relief case automatically covers the settle-out blowdown case.

### 6.3 Radiation & Dispersion
A higher settle-out pressure directly increases the resulting flare load (mass/energy released) if a blowdown is triggered, which increases radiation intensity at a given distance — settle-out-driven blowdown scenarios should be explicitly checked against the flare system's radiation study (see the companion **Flare Network Design** guide, Calc Sheet 8.4 methodology) rather than assumed to be bounded by the normal fire-case relief scenario.

---

## 7. Special Scenarios

### 7.1 Multi-Stage Compressors
Each stage has its **own** settle-out pressure, calculated independently between that stage's suction and discharge volumes — unless interstage piping/valve philosophy allows cross-communication between stages (e.g., an open interstage bypass), in which case the trapped-volume boundary must be redefined to include the connected stages together. See Calc Sheet 8.2 for a worked two-stage example.

### 7.2 Intercoolers/Aftercoolers
Coolers add thermal mass and heat transfer surface area to the trapped volume — over a longer post-trip timeframe (minutes, not seconds), a cooler can meaningfully reduce the settle-out temperature (and therefore pressure) below the adiabatic first-pass estimate, since the adiabatic assumption becomes less accurate as elapsed time increases. For fast/immediate settle-out (the design-basis case, since maximum pressure is usually reached quickly), the adiabatic assumption remains standard and conservative.

### 7.3 Recycles & Anti-Surge Systems
- Whether the anti-surge/recycle valve **opens or closes** on trip materially changes the effective trapped volume and gas distribution — an anti-surge valve that opens on trip connects the discharge volume back to the suction volume through the recycle loop *during* the transient, which can change both the final settle-out pressure and how quickly it is reached, compared to a scenario where the valve fails closed.
- **Practical experience:** This interaction is one of the most commonly mis-modeled aspects of settle-out studies — always confirm actual anti-surge valve fail-safe position and response time with the compressor control system vendor, rather than assuming a generic behavior. See the Case Study (Section 12) for a real-world example of this exact issue.

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific PVT data, EOS modeling, and dynamic simulation.

### 8.1 Calc Sheet 1 — Single-Stage Settle-Out Pressure (Static Mass/Energy Balance)

**Given (from Section 1 basis):**
- Suction: V_s = 15 m³, P_s = 800 psia = 5,515 kPa(abs), T_s = 311 K, Z_s = 0.88
- Discharge: V_d = 8 m³, P_d = 2,500 psia = 17,237 kPa(abs), T_d = 394 K, Z_d = 0.82
- R = 8.314 kJ/(kmol·K), MW = 18 kg/kmol

**Step 1 — Moles of gas in the suction volume:**
```
n_s = (P_s × V_s) / (Z_s × R × T_s)
n_s = (5,515 × 15) / (0.88 × 8.314 × 311)
n_s = 82,725 / 2,276.4
n_s ≈ 36.35 kmol
```

**Step 2 — Moles of gas in the discharge volume:**
```
n_d = (P_d × V_d) / (Z_d × R × T_d)
n_d = (17,237 × 8) / (0.82 × 8.314 × 394)
n_d = 137,896 / 2,686.4
n_d ≈ 51.34 kmol
```

**Step 3 — Total trapped moles and total trapped volume:**
```
n_total = n_s + n_d = 36.35 + 51.34 = 87.69 kmol
V_total = V_s + V_d = 15 + 8 = 23 m³
```

**Step 4 — Settle-out temperature (mole-weighted energy balance, equal Cv approximation):**
```
T_so = (n_s × T_s + n_d × T_d) / n_total
T_so = (36.35 × 311 + 51.34 × 394) / 87.69
T_so = (11,304.9 + 20,228.0) / 87.69
T_so = 31,532.8 / 87.69
T_so ≈ 359.6 K = 86.5 °C = 187.8 °F
```

**Step 5 — Settle-out pressure (real gas law, first-pass average Z):**
```
Z_so (first pass) ≈ inventory-weighted average of Z_s, Z_d ≈ 0.85

P_so = (n_total × Z_so × R × T_so) / V_total
P_so = (87.69 × 0.85 × 8.314 × 359.6) / 23
P_so = 222,806 / 23
P_so ≈ 9,687 kPa(abs) ≈ 1,405 psia ≈ 1,390 psig
```

**Result:** Settle-out pressure ≈ **1,390 psig**, settle-out temperature ≈ **187.8 °F** — well above the suction operating pressure (800 psia) and, in this case, below the downstream vessel MAWP (1,500 psig per Section 1.1), so this particular result **passes** the casing/piping design-pressure check. (See Calc Sheet 8.3 and the Case Study in Section 12 for scenarios where it does not.)

> 📌 **Assumption check:** Step 5 used a first-pass average Z-factor (0.85). For a rigorous design-basis calculation, iterate: use P_so and T_so from this first pass to look up (or calculate via PR/SRK EOS) a refined Z_so at the *actual* settle-out condition, then recompute P_so with that refined value, repeating until convergence — for this example the correction is typically small (a percent or two), but for gas mixtures closer to their critical point the correction can be significant.

---

### 8.2 Calc Sheet 2 — Two-Stage Compressor Settle-Out (Independent Stages)

**Given:**
- Stage 1: suction V=10 m³/800 kPa(abs)/300K/Z=0.95; discharge V=5 m³/2,400 kPa(abs)/340K/Z=0.90
- Stage 2: suction V=6 m³/2,300 kPa(abs)/305K/Z=0.88; discharge V=4 m³/6,500 kPa(abs)/365K/Z=0.80
- MW = 18 kg/kmol for both stages (same gas, illustrative)
- Assume interstage block valves isolate the stages independently at trip (Section 7.1 basis)

**Stage 1 (following the Calc Sheet 8.1 method):**
```
n_s1 = (800 × 10)/(0.95 × 8.314 × 300) = 8,000/2,369.5 ≈ 3.376 kmol
n_d1 = (2,400 × 5)/(0.90 × 8.314 × 340) = 12,000/2,544.1 ≈ 4.717 kmol
n_total,1 = 8.093 kmol,  V_total,1 = 15 m³

T_so,1 = (3.376×300 + 4.717×340)/8.093 = (1,012.8+1,603.8)/8.093 ≈ 323.3 K (50.2 °C)

Z_so,1 (avg) ≈ 0.925
P_so,1 = (8.093 × 0.925 × 8.314 × 323.3)/15 ≈ 20,105/15 ≈ 1,340 kPa(abs) ≈ 179 psig
```

**Stage 2 (same method):**
```
n_s2 = (2,300 × 6)/(0.88 × 8.314 × 305) = 13,800/2,230.5 ≈ 6.187 kmol
n_d2 = (6,500 × 4)/(0.80 × 8.314 × 365) = 26,000/2,427.7 ≈ 10.71 kmol
n_total,2 = 16.90 kmol,  V_total,2 = 10 m³

T_so,2 = (6.187×305 + 10.71×365)/16.90 = (1,887.0+3,909.2)/16.90 ≈ 342.9 K (69.7 °C)

Z_so,2 (avg) ≈ 0.84
P_so,2 = (16.90 × 0.84 × 8.314 × 342.9)/10 ≈ 40,528/10 ≈ 4,053 kPa(abs) ≈ 573 psig
```

**Result:** Stage 1 settle-out ≈ **179 psig**; Stage 2 settle-out ≈ **573 psig** — each stage's casing and interstage piping must be rated for its **own** settle-out pressure, not a single blended value across the whole train.

> 📌 **Assumption check:** This example assumed the interstage block valve fully isolates Stage 1's discharge from Stage 2's suction at trip. If the project's actual philosophy uses a common interstage vessel without an isolation valve between the stages (or an open bypass), the two stages' volumes/inventories must be combined into a single settle-out calculation instead — confirm the as-built P&ID isolation philosophy before finalizing which case applies (see Section 1.3 note).

---

### 8.3 Calc Sheet 3 — Settle-Out as Initial Condition for BDV Sizing

**Given (carried from Calc Sheet 8.1):**
- Settle-out condition (now treated as P1, T1 for a subsequent blowdown): P1 = 9,687 kPa(abs), T1 = 359.6 K
- Combined volume, V = 23 m³, MW = 18 kg/kmol, k = 1.27, Z1 ≈ 0.85
- Target pressure per API 521 §5.15-style logic (lower of 50% of a hypothetical 1,500 psig MAWP = 750 psig, or 100 psig) → **100 psig governs**, P2 = 791 kPa(abs)
- Target time = 15 minutes (900 s)

**Step 1 — Initial trapped mass (from Calc Sheet 8.1 moles):**
```
m1 = n_total × MW = 87.69 × 18 ≈ 1,578.4 kg
```

**Step 2 — Isentropic (first-pass) final temperature:**
```
T2 = T1 × (P2/P1)^[(k−1)/k]
(k−1)/k = 0.27/1.27 = 0.2126
P2/P1 = 791/9,687 = 0.0817
T2 = 359.6 × (0.0817)^0.2126 = 359.6 × 0.587
T2 ≈ 211.1 K = −62.1 °C = −79.7 °F
```

**Step 3 — Final mass at target state (Z2 ≈ 0.90 near low pressure/temperature):**
```
m2 = (P2 × V × MW)/(Z2 × R × T2)
m2 = (791 × 23 × 18)/(0.90 × 8.314 × 211.1)
m2 = 327,474/1,579.5
m2 ≈ 207.3 kg
```

**Step 4 — Mass to be vented:**
```
Δm = m1 − m2 = 1,578.4 − 207.3 ≈ 1,371.1 kg
```

**Step 5 — Average required BDV mass flow:**
```
W_avg = Δm / t = 1,371.1 / 900 ≈ 1.524 kg/s
```

**Result:** Starting from the settle-out condition (not normal operating pressure), the BDV must remove **≈1,371 kg** within 15 minutes, an average flow of **≈1.52 kg/s**. This mass and average flow (with an appropriate peak/average multiplier, per the companion Depressurization Calculation guide's Calc Sheet 8.4 methodology) sizes the BDV orifice for this trip scenario.

> 📌 **Assumption check:** Using settle-out (rather than normal discharge pressure) as the BDV sizing basis is essential whenever settle-out pressure exceeds normal discharge pressure by a meaningful margin — sizing the BDV against normal operating pressure alone would understate the actual post-trip inventory and pressure the valve must handle.

---

## 9. Sample Datasheets

### 9.1 Compressor Settle-Out Summary Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Compressor Tag** | K-101 | — |
| **Type** | Single-stage centrifugal | — |
| **Gas / MW** | Natural gas / 18 | kg/kmol |
| **k (Cp/Cv)** | 1.27 | — |
| **Suction Volume** | 15 | m³ |
| **Suction Pressure (normal)** | 800 (55.2) | psia (bara) |
| **Suction Temperature (normal)** | 100 (37.8) | °F (°C) |
| **Discharge Volume** | 8 | m³ |
| **Discharge Pressure (normal)** | 2,500 (172.4) | psia (bara) |
| **Discharge Temperature (normal)** | 250 (121.1) | °F (°C) |
| **Calculated Settle-Out Pressure** | 1,390 (95.8) | psig (barg) |
| **Calculated Settle-Out Temperature** | 187.8 (86.5) | °F (°C) |
| **Downstream Vessel MAWP** | 1,500 (103.4) | psig (barg) |
| **Settle-Out vs. MAWP Check** | PASS (margin ≈ 110 psig) | — |
| **EOS Used** | Peng-Robinson (final), average-Z hand calc (screening) | — |
| **Recycle/Anti-Surge Valve Trip Position** | Fail-open to recycle loop | — |
| **Method** | Static (screening) — dynamic simulation recommended for final design | — |

---

### 9.2 Multi-Stage Settle-Out Summary Datasheet

| Stage | Suction P/T (normal) | Discharge P/T (normal) | Settle-Out Pressure | Settle-Out Temperature | Casing MAWP Check |
|---|---|---|---|---|---|
| Stage 1 | 800 kPa(a) / 300 K | 2,400 kPa(a) / 340 K | 179 psig | 50.2 °C | Confirm casing MAWP ≥ 179 psig + margin |
| Stage 2 | 2,300 kPa(a) / 305 K | 6,500 kPa(a) / 365 K | 573 psig | 69.7 °C | Confirm casing MAWP ≥ 573 psig + margin |

*(Per Calc Sheet 8.2 — each stage's casing and interstage piping design pressure must independently accommodate its own settle-out result.)*

---

### 9.3 Compressor Trip Cause-and-Effect Summary

| Initiating Event | Isolation Response | Trapped Volume | Governing Design Case |
|---|---|---|---|
| High-High discharge pressure trip | Suction & discharge ESDVs close | Suction + discharge volumes (Calc Sheet 8.1) | Settle-out pressure vs. casing/piping MAWP |
| Anti-surge valve fails to open on trip | Suction & discharge ESDVs close, recycle valve fails closed | Same as above — no recycle relief path | Settle-out pressure (higher, no recycle dilution) — see Case Study, Section 12 |
| Anti-surge valve fails open on trip | Suction & discharge ESDVs close, recycle valve opens | Suction + discharge + recycle loop volume | Settle-out pressure (typically lower/more evenly distributed) |
| Total power failure | All ESDVs close (fail-safe), no active BDV response unless independently powered/pneumatic | Suction + discharge volumes | Settle-out pressure vs. casing/piping MAWP; confirm BDV fail-safe power source independent of plant electrical supply |

---

## 10. Practical Design Checklist

- [ ] Settle-out design basis issued and approved (Section 1) before casing/piping MAWP finalized
- [ ] Trapped-volume boundary (suction + discharge, and recycle loop if applicable) confirmed against the **as-built** P&ID isolation philosophy, not just the design-stage assumption
- [ ] Settle-out pressure and temperature calculated via mass/energy balance — see Calc Sheet 8.1
- [ ] Z-factor iterated using PR/SRK EOS at the calculated settle-out condition, not left at the first-pass average
- [ ] Multi-stage machines checked stage-by-stage (or combined, if interstage isolation allows cross-communication) — see Calc Sheet 8.2
- [ ] Settle-out pressure checked against compressor casing MAWP, piping class, and downstream vessel MAWP
- [ ] Anti-surge/recycle valve fail-safe position and response time confirmed with the compressor control vendor, not assumed generically
- [ ] If settle-out exceeds allowable pressure, BDV/blowdown sizing performed using settle-out (not normal operating pressure) as the initial condition — see Calc Sheet 8.3
- [ ] Flare KOD and radiation study explicitly checked against the settle-out-driven blowdown case, not assumed to be bounded by the normal fire-case relief scenario
- [ ] Static calculation used for screening; dynamic simulation performed for final design-pressure confirmation and flare load prediction
- [ ] Datasheets (settle-out summary, multi-stage summary, cause-and-effect) issued for vendor/EPC use

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Downstream vessel found under-rated for settle-out pressure during detailed engineering | Discharge volume boundary for the settle-out calc stopped at the cooler outlet instead of the actual downstream ESDV | Confirm the true trapped-volume boundary against the as-built isolation philosophy (Section 3.2 practical tip) |
| Settle-out pressure higher than expected after a real trip event | Anti-surge valve failed closed instead of the assumed fail-open behavior | Confirm actual fail-safe position and response time with the compressor control vendor before finalizing the design basis (Section 7.3); see Case Study, Section 12 |
| Multi-stage casing MAWP dispute during code compliance review | Single blended settle-out value was calculated across the whole train instead of stage-by-stage | Calculate settle-out independently per stage unless interstage cross-communication is confirmed (Calc Sheet 8.2) |
| BDV found undersized for the post-trip depressurization case | BDV sized against normal discharge pressure, not the (higher) settle-out pressure | Always use settle-out as the initial condition (P1, T1) for BDV sizing when it governs (Calc Sheet 8.3) |
| Static hand-calc settle-out pressure under-predicted the dynamic simulation result | Check valve took longer to seat than assumed, allowing additional backflow/mixing before full isolation | Use dynamic simulation for final design confirmation on any system with meaningful check-valve response time uncertainty |

---

## 12. Case Study — Multi-Stage Compressor Trip Exceeding Downstream MAWP

> A composite, illustrative case study based on the type of finding commonly encountered on multi-stage gas compression trains following a real trip event. Names, tag numbers, and figures are representative, not project-specific.

### 12.1 Background

A two-stage gas injection compressor train (K-201 A/B) had been designed with a settle-out study performed at FEED, assuming the anti-surge/recycle valve on each stage would **fail open** on trip — a standard assumption for many centrifugal compressor control philosophies, intended to protect the machine from surge during shutdown and to relieve discharge pressure back toward suction. Based on this assumption, Stage 2's settle-out pressure was calculated at approximately 573 psig (consistent with the Calc Sheet 8.2 example in this guide), comfortably within the downstream vessel's 1,000 psig MAWP.

### 12.2 Problem Identified

During a real unplanned trip (triggered by a high vibration signal), the Stage 2 anti-surge valve's positioner lost instrument air pressure due to a common-mode failure in the local air supply header — rather than failing to its intended open position, the valve's actual as-installed fail-safe behavior (a spring-return actuator configured for fail-closed, inconsistent with the original control philosophy assumption) left it **closed** during the trip.

With no recycle relief path available, the full Stage 2 suction and discharge inventories mixed and equalized without any recycle-loop dilution. Post-event data review (pressure transmitter trend) showed peak pressure reached approximately **1,050 psig** — **exceeding the downstream vessel's 1,000 psig MAWP** by a meaningful margin, though (fortunately) still within the vessel's actual hydrotest/burst margin, so no failure occurred. The vessel's PSV also lifted briefly, confirming the pressure excursion was real and not an instrumentation artifact.

### 12.3 Investigation & Recalculation

The process safety team reran the Stage 2 settle-out calculation using the Calc Sheet 8.1/8.2 methodology in this guide, but with the recycle loop **excluded** (fail-closed case) rather than included (the original fail-open assumption):

- **Original (fail-open) assumption:** Stage 2 settle-out ≈ 573 psig (recycle loop volume included, diluting the discharge inventory back toward suction conditions).
- **Actual (fail-closed) case:** Recalculating without recycle dilution — using only the Stage 2 suction and discharge volumes as the trapped boundary — gave a settle-out pressure of approximately **1,070 psig**, closely matching the ≈1,050 psig actually observed in the field data (the small difference attributable to real check-valve response time and non-ideal mixing not captured in the static calculation).
- **Root finding:** The original design basis had used the compressor control philosophy's *intended* fail-safe behavior without independently verifying it against the *as-installed* actuator configuration and the local instrument air supply's actual reliability.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **Design-basis/as-built mismatch** — the settle-out study assumed fail-open recycle valve behavior based on the control philosophy document, but the actuator was procured and commissioned with a fail-closed spring return, and this discrepancy was never caught by a design-basis cross-check against the actual valve datasheet.
2. **Single point of failure in instrument air supply** — the local air header serving the anti-surge valve positioner had no redundant supply path, so a single air-supply fault removed the valve's normal control response entirely, defaulting it to its true (fail-closed) mechanical failure position.

### 12.5 Resolution

- The Stage 2 settle-out design basis was corrected to reflect the **actual fail-closed** behavior, and both stages' casing/piping and the downstream vessel MAWP were re-verified against this bounding (higher) case. In this instance, the existing downstream vessel MAWP (1,000 psig) was found **inadequate** against the corrected 1,070 psig bounding case, and required either a vessel re-rate review or a compensating measure.
- Given the cost/schedule impact of a full vessel re-rate, the selected compensating measure was to add an **independent, dedicated instrument air receiver with check valve isolation** for the anti-surge valve positioner, specifically to protect against the common-mode air-supply failure mode that caused the event — restoring confidence in the fail-open recycle path that the original (lower, 573 psig) settle-out case depended on.
- A formal cross-check step was added to the settle-out calculation procedure: **every settle-out study must be reconciled against the actual as-procured valve actuator fail-safe datasheet**, not just the control philosophy document, before the study is considered final.

### 12.6 Outcome

- No equipment failure occurred, but the event prompted an immediate review of settle-out studies across the company's other multi-stage compression assets with similar recycle-valve-dependent design bases.
- The finding was documented as a corporate lessons-learned item: any settle-out (or other safety) calculation that credits a control valve's *assumed* fail-safe behavior must be independently verified against the *as-procured* actuator configuration, not just the control philosophy narrative.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A settle-out study that credits recycle-valve dilution is only as reliable as the valve's actual fail-safe behavior | Cross-check every settle-out study against the as-procured actuator fail-safe datasheet, not just the control philosophy document |
| Single points of failure in supporting utilities (instrument air) can silently invalidate a safety-relevant design assumption | Identify and protect (redundancy or dedicated local supply) any utility that a credited safety behavior depends on |
| The "worse case" (fail-closed, no recycle) settle-out result should be calculated and checked even when the design intends fail-open behavior | Always calculate and document the settle-out result for both the intended AND the worst-case credible valve failure mode, not just the intended one |
| Static hand-calc results, once corrected for the actual failure mode, matched field data closely | Confirms the static method (Calc Sheet 8.1/8.2) is a valid, fast tool for both design screening and post-event root-cause verification, provided the trapped-volume assumptions are correct |

---

## 13. Reference Standards

- **API RP 521** — Pressure-relieving and Depressuring Systems (settle-out referenced as a design-pressure-basis input)
- **API STD 617** — Axial and Centrifugal Compressors and Expander-compressors for Petroleum, Chemical and Gas Industry Services
- **API STD 618** — Reciprocating Compressors for Petroleum, Chemical, and Gas Industry Services
- **ASME BPVC Section VIII, Div. 1** — Rules for Construction of Pressure Vessels (MAWP basis for downstream vessels)
- Peng, D.Y. & Robinson, D.B. (1976) — A New Two-Constant Equation of State
- Soave, G. (1972) — Equilibrium Constants from a Modified Redlich-Kwong Equation of State

---

*This guide is a practical study reference combining standard settle-out calculation theory with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific PVT data, EOS modeling, dynamic simulation results, and current regulatory/code requirements. This guide should be read alongside the companion Flare Network Design and Depressurization Calculation study guides, since settle-out pressure frequently governs the initial conditions for both.*
