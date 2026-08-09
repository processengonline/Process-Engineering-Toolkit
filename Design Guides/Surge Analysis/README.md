# 🌀 Surge Analysis — Practical Study Guide

> A field-oriented reference covering the core engineering topics in centrifugal compressor surge analysis and anti-surge system design — combining API 617/614 methodology with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Compressor Settle-Out Calculations**, **Dynamic Simulation**, and **Separator Design** study guides — it develops the surge/anti-surge protection scheme for K-101 (the same compressor used throughout this guide series) in full depth, building on the settle-out and dynamic response findings those guides already established.

**Illustrative project used throughout this guide:** K-101, a variable-speed (steam turbine driven) centrifugal compressor — used to work through surge line tracking across operating speed via the affinity laws, anti-surge recycle valve sizing, a fast-trip valve response-time check, a gas inventory "cushion" calculation, and a comparison between gradual load-change and sudden-trip anti-surge response requirements. All numbers below are worked sample calculations for study purposes — always replace with project-specific compressor performance map data and vendor-confirmed valve/actuator response.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Fundamentals of Surge](#2-fundamentals-of-surge)
3. [Compressor Performance Maps](#3-compressor-performance-maps)
4. [Surge Analysis Methods](#4-surge-analysis-methods)
5. [Anti-Surge System Design](#5-anti-surge-system-design)
6. [Surge Scenarios](#6-surge-scenarios)
7. [Pipeline & System Integration](#7-pipeline--system-integration)
8. [Standards & Guidelines](#8-standards--guidelines)
9. [Sample Calculation Sheets](#9-sample-calculation-sheets)
10. [Sample Datasheets](#10-sample-datasheets)
11. [Practical Design Checklist](#11-practical-design-checklist)
12. [Common Field Issues & Lessons Learned](#12-common-field-issues--lessons-learned)
13. [Case Study — Static Surge Control Line Caused Both Nuisance Recycling and a Near-Miss](#13-case-study--static-surge-control-line-caused-both-nuisance-recycling-and-a-near-miss)
14. [Reference Standards](#14-reference-standards)

---

## 1. Design Basis & Assumptions

Surge analysis sits at the intersection of the compressor's own mechanical performance envelope (the manufacturer's performance map) and the plant's process dynamics (how quickly and how far the operating point can move during a disturbance) — a correct anti-surge design requires both a genuinely accurate surge line (Section 3, tracked properly across the full speed range) and a control/protection system fast enough for the plant's actual transient behavior (Sections 5–6).

### 1.1 Compressor & System Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Compressor | K-101, centrifugal, steam turbine driven (variable speed) | Same tag used throughout this guide series |
| Rated (100%) speed surge point | Q = 8,000 ACFM, H = 45,000 ft·lbf/lbm | Used in Calc Sheet 9.1 |
| Rated (100%) speed choke point | Q = 15,000 ACFM | — |
| Suction/discharge volumes | 15 m³ / 8 m³ | Consistent with companion Compressor Settle-Out guide |
| Suction/discharge pressure | 800 psia / 2,500 psia | Consistent with companion Compressor Settle-Out and Separator Design guides |
| Gas properties | MW = 18, k = 1.3 | Consistent with companion guides |

### 1.2 Codes & Standards / Methodology Basis
- **API 617** — Axial and Centrifugal Compressors and Expander-compressors, the primary mechanical design standard, including surge margin expectations
- **API 614** — Lubrication, Shaft-Sealing, and Oil-Control Systems and Auxiliaries, covering auxiliary systems including surge control system components
- **OEM guidelines** — compressor and anti-surge controller vendors frequently specify their own surge control philosophy details (control line algorithm, minimum margin) beyond the generic API baseline — always confirm the actual vendor's recommended approach for the specific machine

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Anti-surge control margin (b-parameter) | 10% beyond the surge line | Consistent with companion Dynamic Simulation and Process Philosophies guides |
| Surge line speed correction method | Affinity laws (Q ∝ N, H ∝ N²) | Section 3.3, Calc Sheet 9.1; confirm against actual compressor performance map data rather than assuming pure affinity-law behavior for all machines |
| Fast-trip valve target response | Full open within the available margin time for the fastest credible trip scenario | Section 6.1, Calc Sheet 9.3 |
| Modulating (PID) anti-surge valve response | Adequate for gradual load-change scenarios, not necessarily for a sudden trip | Section 6.2, Calc Sheet 9.5 |
| Gas inventory "cushion" | Larger suction/discharge volume slows the transient, providing more response-time margin | Section 7.1, Calc Sheet 9.4 |

> ⚠️ **Practical note:** A surge line calibrated only at one operating speed (typically 100%, the easiest point to test/verify) and then applied as a fixed control line across the compressor's entire variable-speed range is one of the most consequential and easy-to-miss errors in anti-surge system configuration — Section 3.3's affinity-law tracking exists specifically to avoid this, and the Case Study (Section 13) shows the real consequence of skipping it.

---

## 2. Fundamentals of Surge

### 2.1 Definition
Surge is a **dynamic flow instability** that occurs when a centrifugal (or axial) compressor's flow falls below a critical limit for the current operating speed and discharge pressure — the compressor can no longer sustain forward flow against the downstream pressure, causing a rapid flow reversal, followed by re-establishment of forward flow, repeating in a violent oscillating cycle. Surge cycles impose severe thrust bearing loads and can cause serious mechanical damage (impeller, seal, and bearing damage) within seconds if not stopped.

### 2.2 Difference from Choke
| | Surge | Choke |
|---|---|---|
| Flow condition | Too **low** | Too **high** |
| Mechanism | Flow reversal instability at the compressor's low-flow stability limit | Flow limited by sonic velocity somewhere in the flow path (typically at the impeller eye or a diffuser throat) |
| Consequence | Severe, damaging oscillation | Reduced head/efficiency, generally not immediately damaging |
| Protection approach | Anti-surge recycle/trip system (Section 5) | Generally avoided by not operating the compressor beyond its rated flow, not a dedicated protection system |

### 2.3 Surge Line
The **surge line** is the boundary on the compressor's performance map (Section 3) separating stable operation (to the right, higher flow) from the unstable surge region (to the left, lower flow) — it is not a single fixed point but a curve that varies with operating speed (Section 3.3), which is the central complication most of this guide's calc sheets address.

---

## 3. Compressor Performance Maps

### 3.1 Head vs. Flow Curves
The compressor's performance map plots polytropic (or isentropic) head against inlet volumetric flow, typically as a family of curves — one per operating speed — showing the achievable head at each flow rate for that speed; this defines the **operating envelope** the process system must stay within.

### 3.2 Surge Line and Choke Line
The surge line connects the low-flow instability limit across each speed curve; the choke line (Section 2.2) connects the high-flow sonic limit — together they bound the compressor's entire safe/achievable operating region on the performance map.

### 3.3 Operating Point Tracking
As process conditions change (a valve opening/closing, a downstream demand change, a speed change from the turbine governor), the operating point moves across the performance map — and critically, **the surge line itself moves** as speed changes, following (approximately) the compressor affinity laws:
```
Q ∝ N        (flow scales with speed)
H ∝ N²       (head scales with speed squared)
```
A control system that doesn't track this speed-dependent surge line movement — instead using a single fixed control line calibrated at one speed — will be either overly conservative (nuisance recycling) or non-conservative (inadequate real margin) at other speeds; see Calc Sheet 9.1 for a worked example and the Case Study (Section 13) for a real consequence.

---

## 4. Surge Analysis Methods

### 4.1 Steady-State Checks
Confirming the operating point sits an adequate margin away from the (correctly speed-corrected) surge line at every credible steady operating condition — the baseline check, worked through in Calc Sheet 9.1.

### 4.2 Dynamic Simulation
Modeling transient events (trip, recycle valve response, downstream valve closure) — companion Dynamic Simulation guide's Section 5.2 methodology, essential because a steady-state check alone cannot reveal whether the operating point crosses the surge line *during* a transient even if both the initial and final states are individually safe.

### 4.3 Anti-Surge Control
PID control loops driving a recycle valve to hold the operating point at (or right of) a defined control line — detailed in Section 5.

---

## 5. Anti-Surge System Design

### 5.1 Recycle Valve Sizing
The anti-surge recycle valve must be sized with adequate **capacity** (Cv, Calc Sheet 9.2) to actually restore flow above the surge line when opened, and must **open fast enough** (Calc Sheet 9.3) relative to how quickly the operating point can approach the surge line during the fastest credible disturbance.

### 5.2 Control Logic
- **Surge detection** — continuously computing the operating point's position relative to the (speed-corrected) surge/control line from real-time flow, pressure, and temperature measurements (Section 5.3).
- **Valve actuation** — the anti-surge controller drives the recycle valve open as the operating point approaches the control line, and closes it again as margin is restored, in a continuous modulating fashion for gradual disturbances (Calc Sheet 9.5).
- **Compressor trip interlocks** — for the most severe, fastest disturbances (a sudden driver trip), a dedicated fast-opening trip/dump valve — distinct from the normal modulating anti-surge valve — is often required, consistent with the companion Compressor Settle-Out and Dynamic Simulation guides' case study findings.

### 5.3 Instrumentation
Flow, pressure, and temperature transmitters at the compressor suction and discharge feed the surge controller's real-time calculation of the operating point's position on the (speed-corrected) performance map — consistent with the companion Instrumentation Process Datasheet guide's transmitter range/turndown methodology (that guide's Section 4.2), applied here to the specific, safety-critical demands of a surge control loop.

---

## 6. Surge Scenarios

### 6.1 Compressor Trip
Sudden loss of driver power (or an ESD trip) — the fastest-developing, most severe surge scenario, since flow can decay very rapidly with no compressor head to sustain it — worked in Calc Sheet 9.3, requiring the fast-acting dedicated trip valve discussed in Section 5.2.

### 6.2 Rapid Load Changes
Process demand fluctuations (a downstream user's flow requirement dropping) — typically slower-developing than a full trip, and usually adequately handled by the normal modulating PID anti-surge control loop — worked in Calc Sheet 9.5, contrasted directly against the trip scenario's much faster requirement.

### 6.3 Startup/Shutdown
Transient conditions during startup (before the compressor reaches a stable operating speed/flow) and shutdown (as speed/flow are deliberately reduced) can pass close to the surge line even under controlled, intentional conditions — anti-surge protection must remain active and correctly configured throughout these transients, not just during normal running operation.

### 6.4 Blocked Discharge or Suction Disturbances
A blocked discharge (companion PSV Sizing & Design guide's Section 3.1 blocked-outlet scenario, applied here to a compressor rather than a pump) or a suction-side disturbance (e.g., a sudden suction pressure drop) can each independently drive the operating point toward the surge line, and should be evaluated as distinct scenarios alongside the trip and load-change cases above.

---

## 7. Pipeline & System Integration

### 7.1 Gas Inventory Effects
The suction and discharge piping/vessel volumes (companion Compressor Settle-Out guide's Section 3 methodology) act as a "cushion" — larger volumes slow the rate at which a disturbance propagates into a flow/pressure swing at the compressor, providing more time for the anti-surge system to respond; smaller volumes (e.g., a compact skid-mounted package, companion Separator Design guide's Session 13) provide less cushion, making fast valve response even more critical — worked in Calc Sheet 9.4.

### 7.2 Settle-Out Pressure Interaction
During a compressor trip, the same mass/energy balance that determines settle-out pressure (companion Compressor Settle-Out guide, that guide's Calc Sheet 8.1) also determines the flow/pressure trajectory the anti-surge system must manage during the transient leading up to that settle-out state — the two analyses (settle-out and surge) are complementary views of the same trip event, not independent studies.

### 7.3 Flare System Impact
A surge event (or the anti-surge/trip valve's own recycle or dump flow) can create a sudden gas release/load on the flare system — consistent with the companion Flare Network Design and PSV Sizing & Design guides' simultaneous relief and blowdown load methodology, which should explicitly include any credible surge-related flare load, not just the compressor's normal relief/blowdown cases.

---

## 8. Standards & Guidelines

- **API 617** — Axial and Centrifugal Compressors and Expander-compressors for Petroleum, Chemical and Gas Industry Services (mechanical design, including surge margin basis)
- **API 614** — Lubrication, Shaft-Sealing, and Oil-Control Systems and Auxiliaries (auxiliary systems, including surge control components)
- **OEM guidelines** — vendor-specific surge control philosophy, control line algorithm, and minimum margin recommendations, which should always be confirmed and reconciled with the project's own philosophy (companion Process Philosophies guide)

---

## 9. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific compressor performance map data and vendor-confirmed valve/actuator response.

### 9.1 Calc Sheet 1 — Surge Line Tracking via Affinity Laws & Operating Point Margin

**Given:** 100% speed surge point: Q = 8,000 ACFM, H = 45,000 ft·lbf/lbm (Section 1.1). Reduced-speed operating case: 80% speed, actual process operating point Q = 7,200 ACFM, H = 27,500 ft·lbf/lbm.

**Step 1 — Predict the surge point at 80% speed using the affinity laws:**
```
Q_surge,80% = Q_surge,100% × (N%/100) = 8,000 × 0.80 = 6,400 ACFM
H_surge,80% = H_surge,100% × (N%/100)² = 45,000 × (0.80)² = 45,000 × 0.64 = 28,800 ft·lbf/lbm
```

**Step 2 — Flow-basis surge margin at 80% speed:**
```
Margin = (Q_op − Q_surge,80%) / Q_surge,80% = (7,200 − 6,400)/6,400 ≈ 12.5%
```

**Step 3 — Compare to the 100%-speed case (for context, using Section 1.1's rated-speed operating point of Q=9,500 ACFM):**
```
Margin(100%) = (9,500−8,000)/8,000 = 18.75%
Margin(80%) = 12.5%  →  reduced margin at lower speed
```

**Result:** The surge margin **shrinks from 18.75% at rated speed to 12.5% at 80% speed** for this operating case — confirming the common finding that **turndown (reduced-speed) operation is often the higher-risk surge condition**, not full-speed operation, precisely because the surge line itself moves with speed per the affinity laws while the process's actual operating margin doesn't necessarily shrink proportionally.

> 📌 **Assumption check:** Pure affinity-law scaling is an approximation — real compressor performance maps deviate from ideal affinity-law behavior, particularly at the extremes of the speed range, due to Reynolds number and Mach number effects that don't scale perfectly with speed. Always validate the affinity-law prediction against the vendor's actual multi-speed performance map data rather than relying on a single-speed data point extrapolated across the full range, exactly the gap explored in the Case Study (Section 13).

---

### 9.2 Calc Sheet 2 — Anti-Surge Recycle Valve Cv Sizing

**Given:** Required recycle mass flow to restore adequate margin during a disturbance, W = 239,670 lb/hr (derived from a required ≈1,500 ACFM equivalent recycle flow at suction density, consistent with the companion Separator Design guide's suction density basis, ρs = 2.663 lb/ft³). Recycle source (discharge) conditions: P1 = 2,500 psia, T1 = 710°R, Z = 0.82, MW = 18, k = 1.3, discharge coefficient Kd = 0.8 (typical valve).

**Step 1 — Gas sizing coefficient, C (API 520-style choked-flow approach, per companion PSV Sizing & Design guide methodology):**
```
C = 520 × √[k × (2/(k+1))^((k+1)/(k−1))]
(k+1)/(k−1) = 2.3/0.3 = 7.667
(2/2.3)^7.667 ≈ 0.342
k × 0.342 = 1.3 × 0.342 = 0.4446
√0.4446 ≈ 0.6668
C = 520 × 0.6668 ≈ 346.7
```

**Step 2 — Required effective flow area (choked flow through the recycle valve):**
```
A = W×√(T×Z/MW) / (C×Kd×P1)
√(710×0.82/18) = √32.34 ≈ 5.687

A = 239,670 × 5.687 / (346.7 × 0.8 × 2,500)
A = 1,362,924 / 693,400 ≈ 1.966 in²
```

**Step 3 — Convert to an approximate valve Cv:**
```
Cv ≈ 29.9 × A(in²)  [typical rule-of-thumb area-to-Cv conversion]
Cv ≈ 29.9 × 1.966 ≈ 58.8 → Cv ≈ 59
```

**Result:** The anti-surge recycle valve requires **Cv ≈ 59** — consistent with a **4-inch** reduced-trim ball valve or an equivalent-capacity control valve. This Cv requirement, together with the response-time requirement (Calc Sheet 9.3), together define the valve's full specification — sizing for capacity alone, without also checking response time, is not sufficient.

> 📌 **Assumption check:** The Cv-to-area conversion factor used here is a rough rule of thumb, valid for an initial sizing estimate — the final valve selection should be confirmed against the specific vendor's actual Cv-vs-travel curve for the selected valve type and trim, consistent with the companion Instrumentation guide's Calc Sheet 10.1 practical tip about always using vendor-confirmed Cv data for final sizing.

---

### 9.3 Calc Sheet 3 — Fast-Trip Valve Response Time Check

**Given:** Compressor trip scenario, available flow margin at time of trip = 1,200 ACFM (Q_op = 9,200 ACFM, Q_surge = 8,000 ACFM at the operating speed). Flow decay rate during this trip (from dynamic simulation, companion Dynamic Simulation guide methodology) = −1,500 ACFM/s. Selected fast-trip valve (a dedicated dump valve, distinct from the normal modulating recycle valve sized in Calc Sheet 9.2) full-stroke response time = 0.6 s.

**Step 1 — Time available before the operating point crosses the surge line:**
```
t_available = ΔQ/|dQ/dt| = 1,200/1,500 = 0.8 s
```

**Step 2 — Compare to the fast-trip valve's response time:**
```
t_available (0.8 s) > Valve response (0.6 s)  →  PASS
```

**Result:** The dedicated fast-trip valve, at 0.6 s full-stroke response, is **fast enough** to open before the operating point crosses the surge line (0.8 s available) — this is a well-designed protection scheme for this specific trip scenario, in contrast to the companion Dynamic Simulation guide's case study, where a standard modulating valve's slower response was found inadequate for a similarly fast trip transient.

> 📌 **Assumption check:** This result is only as good as the assumed flow decay rate — always derive this rate from an actual dynamic simulation of the specific trip scenario (companion Dynamic Simulation guide, Section 3.2), not an assumed generic value, since different trip causes (driver power loss vs. a downstream block valve closure) can produce meaningfully different decay rates requiring re-verification of this same check.

---

### 9.4 Calc Sheet 4 — Gas Inventory "Cushion" vs. Required Response Time

**Given:** Suction volume Vs = 15 m³ (529.7 ft³), discharge volume Vd = 8 m³ (282.5 ft³) (companion Compressor Settle-Out guide basis). Normal operating flow ≈9,500 ACFM (158.3 ACFS) on both sides (simplified — ignoring the density change between suction and discharge for this approximate index).

**Step 1 — Suction-side inventory time constant (volume ÷ normal flow, a residence-time-style index):**
```
τs = Vs/Q = 529.7/158.3 ≈ 3.35 s
```

**Step 2 — Discharge-side inventory time constant:**
```
τd = Vd/Q = 282.5/158.3 ≈ 1.78 s
```

**Step 3 — Total system inventory time constant:**
```
τ_total = τs + τd ≈ 3.35 + 1.78 ≈ 5.13 s
```

**Step 4 — Compare to the required fast-trip valve response time (Calc Sheet 9.3, 0.6 s):**
```
τ_total (5.13 s) ≫ Required valve response (0.6 s)
```

**Result:** The system's gas inventory provides a substantial "cushion" (≈5.13 s characteristic time) relative to the fast-trip valve's required 0.6 s response — confirming that **the valve response time (Calc Sheet 9.3), not the inventory cushion, is the limiting/design-driving factor** for this configuration. This relationship inverts for a **compact, skid-mounted package** (companion Separator Design guide's Session 13) with much smaller suction/discharge volumes — a smaller τ_total shrinks the available margin further, making fast valve response even more critical, and potentially requiring an even faster-responding trip valve than this example's 0.6 s.

> 📌 **Assumption check:** This simplified time-constant index uses the same volumetric flow on both suction and discharge for simplicity — a more rigorous analysis would account for the actual density difference (discharge gas is denser at higher pressure, meaning the discharge volume represents a different residence time in mass terms than in simple ACFM terms) — treat this as a useful comparative/order-of-magnitude index, not a precise transient prediction (which requires the full dynamic simulation referenced in Calc Sheet 9.3).

---

### 9.5 Calc Sheet 5 — Rapid Load Change vs. Trip: Anti-Surge Response Comparison

**Given:** Same available margin as Calc Sheet 9.3 (1,200 ACFM), but for a **gradual load change** scenario (downstream demand reduction) rather than a sudden trip: flow decay rate = −100 ACFM/s (much slower than the trip's −1,500 ACFM/s). Standard modulating anti-surge valve (PID-controlled, the Cv=59 valve sized in Calc Sheet 9.2) full-stroke response time = 4 s (typical for a standard control valve actuator, not the specialized fast-trip valve).

**Step 1 — Time available before the operating point crosses the surge line:**
```
t_available = 1,200/100 = 12 s
```

**Step 2 — Compare to the standard modulating valve's response time:**
```
t_available (12 s) ≫ Standard valve response (4 s)  →  PASS, with substantial margin
```

**Result:** For this gradual load-change scenario, the **standard modulating anti-surge valve** (the same physical valve sized for capacity in Calc Sheet 9.2, but here evaluated at its normal PID-controlled response speed rather than a specialized fast-trip actuator) is comfortably adequate — 12 s available against only 4 s required.

**Contrast with Calc Sheet 9.3's trip scenario:** The trip scenario required a response within 0.8 s — far faster than this standard valve's 4 s response could achieve. This is exactly **why** a well-designed anti-surge protection scheme typically uses **two distinct elements**: the normal modulating recycle valve (PID-controlled, adequate for gradual disturbances like this one) and a separate, faster-acting dedicated trip/dump valve (Calc Sheet 9.3) reserved specifically for sudden trip events — the same architecture the companion Compressor Settle-Out and Dynamic Simulation guides' case studies arrived at after their own anti-surge findings.

> 📌 **Assumption check:** The specific decay rates used here (−100 ACFM/s for gradual load change vs. −1,500 ACFM/s for a trip) are illustrative — always derive the actual credible range of decay rates for the specific plant and disturbance types from dynamic simulation, since the appropriate valve architecture (single valve vs. dual valve/trip-plus-modulating) depends on how wide a gap exists between the fastest and slowest credible scenarios.

---

## 10. Sample Datasheets

### 10.1 Compressor Performance Map Summary — K-101

| Speed (%) | Surge Flow (ACFM) | Surge Head (ft·lbf/lbm) | Choke Flow (ACFM) |
|---|---|---|---|
| 100% | 8,000 | 45,000 | 15,000 |
| 90% | 7,200 (per affinity law) | 36,450 | 13,500 |
| 80% | 6,400 (per affinity law) | 28,800 | 12,000 |
| 70% | 5,600 (per affinity law) | 22,050 | 10,500 |

*(Illustrative — affinity-law-derived values per Calc Sheet 9.1 methodology; a real performance map should be validated against actual multi-speed vendor test data, not affinity-law extrapolation alone, especially near the ends of the speed range.)*

---

### 10.2 Anti-Surge Valve Datasheet

| Parameter | Modulating Recycle Valve | Fast-Trip (Dump) Valve |
|---|---|---|
| Tag No. | ASV-101 | HGBV-101 |
| Cv | 59 (per Calc Sheet 9.2) | 59 (same capacity requirement) |
| Size | 4-in reduced trim | 4-in full-bore |
| Actuator type | Pneumatic, PID-modulated | Pneumatic, fast-dump/quick-exhaust |
| Response time (full stroke) | 4 s (Calc Sheet 9.5) | 0.6 s (Calc Sheet 9.3) |
| Trigger | Continuous PID control line tracking | Compressor trip signal (direct, bypassing normal PID loop) |
| Fail-safe position | Open | Open |

---

### 10.3 Surge Control Instrumentation Summary

| Tag | Service | Location |
|---|---|---|
| FT-101S | Suction flow | K-101 suction |
| PT-101S / TT-101S | Suction pressure/temperature | K-101 suction |
| PT-101D / TT-101D | Discharge pressure/temperature | K-101 discharge |
| SIC-101 | Surge controller (speed-corrected control line) | DCS/dedicated anti-surge controller |

---

## 11. Practical Design Checklist

- [ ] Compressor performance map obtained across the full operating speed range, not just a single (typically 100%) speed point
- [ ] Surge line tracked across speed using affinity laws as a first-pass estimate, then validated against actual vendor multi-speed data — see Calc Sheet 9.1
- [ ] Surge margin (control line) explicitly checked at reduced-speed/turndown conditions, not assumed adequate because it's adequate at rated speed
- [ ] Anti-surge recycle valve sized for both capacity (Cv) and response time — see Calc Sheets 9.2–9.3
- [ ] Fast-trip valve response time explicitly checked against the fastest credible trip scenario's flow decay rate, derived from dynamic simulation — see Calc Sheet 9.3
- [ ] Gradual load-change scenarios checked against the standard modulating valve's normal response time, confirming a dedicated fast-trip valve isn't over-specified for every scenario — see Calc Sheet 9.5
- [ ] Gas inventory "cushion" assessed, with particular attention for compact/skid-mounted packages with reduced suction/discharge volumes — see Calc Sheet 9.4
- [ ] Anti-surge controller configured with a genuinely speed-corrected control line, not a single fixed line calibrated at one speed
- [ ] Surge-related flare loads (recycle/dump valve flow) included in the companion Flare Network Design and PSV Sizing & Design guides' simultaneous relief load methodology
- [ ] Startup/shutdown transients explicitly confirmed to remain adequately clear of the surge line, not just normal running operation

---

## 12. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Excessive nuisance recycling at high speed, reducing net capacity | Fixed (non-speed-corrected) control line, overly conservative at high speed | Configure the anti-surge controller with a genuine speed-corrected control line — see Calc Sheet 9.1 and Case Study, Section 13 |
| Near-miss surge event during turndown operation | Fixed control line non-conservative at reduced speed, real margin smaller than the fixed line implied | Same fix — verify margin explicitly at every operating speed, not just rated speed |
| Compressor surged during an ESD trip despite an apparently adequate anti-surge valve | Valve response time never checked against the specific trip scenario's flow decay rate | Explicitly calculate available response time vs. actual valve response for the fastest credible trip — see Calc Sheet 9.3 |
| Over-specified, unnecessarily expensive fast-trip valve installed for a service that only ever sees gradual load changes | Fast-trip valve response requirement applied uniformly without checking whether a genuine fast-trip scenario is actually credible for that specific compressor/service | Explicitly compare trip vs. gradual load-change response requirements before defaulting to the more expensive fast-trip architecture — see Calc Sheet 9.5 |
| Compact package compressor surged faster than a similar larger-inventory installation | Smaller suction/discharge volumes provide less inventory cushion, requiring faster valve response than a "typical" installation | Explicitly recalculate the inventory cushion for compact/skid packages rather than assuming a standard response-time spec is adequate — see Calc Sheet 9.4 |

---

## 13. Case Study — Static Surge Control Line Caused Both Nuisance Recycling and a Near-Miss

> A composite, illustrative case study based on the type of finding commonly encountered during commissioning of variable-speed compressor anti-surge systems. Names, tag numbers, and figures are representative, not project-specific.

### 13.1 Background

K-101 (this guide's running example) is steam turbine driven and operates across a wide speed range (roughly 70–100% of rated speed) to match varying process demand. During commissioning, the anti-surge controller was configured using a **single, fixed control line**, calibrated against surge testing performed at 100% (rated) speed only — the commissioning team's rationale was that 100% speed testing represented the "worst case" and that a control line calibrated there, with the standard 10% margin (Section 1.3), would be conservative across the full speed range.

### 13.2 Problem Identified

Two distinct problems emerged once the compressor began operating across its full speed range in normal service:

1. **At high speed (90–100%)**, operators reported the anti-surge valve recycling far more frequently than expected, even during apparently stable operation — reducing net compressor capacity and wasting the energy/gas value of the recycled flow. Investigation confirmed the fixed control line, calibrated conservatively at 100% speed, was being applied essentially unchanged at 90–95% speed as well, where the true (affinity-law-corrected) surge line — per this guide's Calc Sheet 9.1 methodology — sits at meaningfully lower flow, meaning the fixed line was **overly conservative** at these speeds, triggering recycling well before it was actually necessary.

2. **At reduced speed (70–80%, turndown operation)**, a near-miss event occurred: a rapid downstream demand change pushed the operating point close enough to the *actual* surge line that an audible surge cycle began before the anti-surge valve responded — post-event data review found that the fixed control line, extrapolated from the 100% speed calibration, was **not conservative enough** at this lower speed; consistent with this guide's Calc Sheet 9.1 finding that surge margin shrinks disproportionately at reduced speed, the fixed line had significantly overstated the actual available margin at 75% speed specifically.

### 13.3 Investigation & Recalculation

The process control and process safety teams reran the Calc Sheet 9.1 affinity-law methodology across the compressor's full speed range and compared it against the fixed control line that had actually been configured in the anti-surge controller — confirming the fixed line diverged meaningfully from the true, speed-corrected surge line in **both directions**: too conservative at high speed, not conservative enough at low speed, exactly as this guide's Section 3.3 describes as the generic risk of a fixed control line.

### 13.4 Root Cause

Two compounding root causes were identified:
1. **A single-speed calibration was assumed to be conservative across the full speed range without actually verifying that assumption against the affinity-law-predicted surge line at other speeds** — the commissioning team's reasoning (100% speed as "worst case") conflated *absolute* surge flow (highest at 100% speed) with *margin adequacy relative to actual operating conditions at each speed*, which are not the same thing once the operating point's own position is also considered.
2. **The anti-surge controller's actual configured algorithm was not confirmed to include a proper speed-correction function** before commissioning — modern anti-surge controllers are capable of continuously computing a speed-corrected control line in real time (using live speed, or a corrected-flow/corrected-head parameter set), but this capability must be explicitly configured and commissioned, not assumed to be active by default.

### 13.5 Resolution

- The anti-surge controller was reconfigured to use a properly speed-corrected control line, computed continuously from real-time compressor speed using the affinity-law relationship (validated against actual multi-speed vendor performance data, not affinity-law extrapolation alone, per this guide's Calc Sheet 9.1 assumption note) rather than the original single-speed fixed line.
- Post-reconfiguration testing across the full speed range confirmed both problems resolved: nuisance recycling at high speed dropped essentially to zero during stable operation, and the calculated margin at low speed now correctly reflected the actual (smaller) available margin, triggering appropriately earlier recycle valve response during a repeat of a similar downstream demand transient.
- The company's anti-surge commissioning procedure was updated to require: **every anti-surge controller commissioning must explicitly verify speed-corrected control line behavior across at least three representative speeds spanning the compressor's full operating range**, not just confirm correct behavior at a single calibration speed.

### 13.6 Outcome

- No actual surge-related mechanical damage occurred, but the near-miss event was treated with the same seriousness as a genuine loss-of-containment near-miss, given how close the actual surge cycle came to developing before the (too-slow-to-respond-at-this-speed) protection system intervened.
- The finding was documented and disseminated across the company's other variable-speed compressor installations, prompting a proactive review that found at least one other machine with a similarly mis-configured fixed control line, corrected before it produced its own near-miss event.

### 13.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A control line calibrated conservatively at one speed is not automatically conservative at every other speed — it can be simultaneously too conservative at some speeds and not conservative enough at others | Explicitly verify speed-corrected control line behavior across the full operating speed range, not just the calibration speed — Calc Sheet 9.1 |
| "Worst case" reasoning about absolute surge flow doesn't automatically translate into "worst case" reasoning about margin adequacy at other operating points | Separate the two concepts explicitly: highest absolute surge flow (likely at rated speed) vs. smallest actual operating margin (often at reduced speed) |
| A modern anti-surge controller's speed-correction capability must be explicitly configured and commissioned, not assumed active by default | Make explicit speed-corrected control line verification a mandatory commissioning test step, across multiple speeds |
| Nuisance recycling and inadequate protection can both stem from the same underlying root cause (a non-speed-corrected control line), just manifesting in opposite directions at different operating speeds | When investigating a nuisance-trip/recycle complaint, also check whether the same root cause could be creating a non-conservative gap elsewhere in the operating range, not just treat it as a pure "too sensitive" tuning problem |

---

## 14. Reference Standards

- **API 617** — Axial and Centrifugal Compressors and Expander-compressors for Petroleum, Chemical and Gas Industry Services
- **API 614** — Lubrication, Shaft-Sealing, and Oil-Control Systems and Auxiliaries for Petroleum, Chemical and Gas Industry Services

---

*This guide is a practical study reference combining standard surge analysis and anti-surge system design methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific compressor performance map data, vendor-confirmed valve/actuator response, and dynamic simulation results. This guide should be read alongside the companion Compressor Settle-Out Calculations, Dynamic Simulation, Separator Design, PSV Sizing & Design, and Flare Network Design study guides, since surge protection sits at the intersection of the mechanical compressor design, the dynamic process response, and the broader relief/flare system those guides each address in their own detail.*
