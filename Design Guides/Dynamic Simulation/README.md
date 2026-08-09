# ⏱️ Dynamic Simulation — Practical Study Guide

> A field-oriented reference covering the core engineering topics in dynamic (transient) process simulation — combining Aspen HYSYS Dynamics/UniSim Dynamics/OLGA methodology with worked sample calculations, sample documents, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design**, **Depressurization Calculation**, **Compressor Settle-Out Calculations**, **Flow Assurance**, and **Steady-State Simulation** study guides — dynamic simulation is where those studies' steady-state/static results are tested against the actual time-dependent behavior of a real upset, trip, or startup.

**Illustrative project used throughout this guide:** the same gas processing train (V-100, K-101, E-101, BDV-101/PSV-101) and subsea tieback used across this guide series — used to work through PID controller tuning, a blowdown time-constant screening check against the companion Depressurization Calculation guide's static result, an anti-surge valve response-time check, a terrain-slugging volume estimate, and a dynamic model validation against plant data. All numbers below are worked sample calculations for study purposes — always replace with project-specific data and a properly configured dynamic simulation.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Fundamentals](#2-fundamentals)
3. [Transient Operations](#3-transient-operations)
4. [Control System Integration](#4-control-system-integration)
5. [Safety Studies](#5-safety-studies)
6. [Multiphase Flow Dynamics](#6-multiphase-flow-dynamics)
7. [Validation & QA/QC](#7-validation--qaqc)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Documents & Datasheets](#9-sample-documents--datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Anti-Surge Valve Too Slow to Prevent Surge During ESD Trip](#12-case-study--anti-surge-valve-too-slow-to-prevent-surge-during-esd-trip)
13. [Reference Standards & Tools](#13-reference-standards--tools)

---

## 1. Design Basis & Assumptions

Dynamic simulation work is normally governed by a **"Dynamic Simulation Basis Document"** — the transient scenarios to be modeled, the equipment/control system detail level required, and validation criteria — issued before detailed dynamic modeling begins. Unlike a steady-state case (companion guide), a dynamic model's credibility depends heavily on getting valve stroke times, controller tuning, and equipment inventory/geometry right, since these govern the *timing* of the response, not just its end state.

### 1.1 Process & Model Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Unit | Gas processing train: V-100 → K-101 → E-101, plus subsea tieback | Same equipment tags used throughout this guide series |
| V-100 / BDV-101 depressurization case | Per companion Depressurization Calculation guide: P1 = 500 psig, target 100 psig/15 min | Used in Calc Sheet 8.2 |
| K-101 compressor | Surge flow 8,000 ACFM; normal operating flow 9,500 ACFM | Used in Calc Sheet 8.3 |
| FIC-1042 flow control loop | Process reaction curve: K = 2.5, θ = 8 s, τ = 40 s (FOPDT) | Used in Calc Sheet 8.1 |
| Subsea tieback riser | Height 1,200 m, 8-in ID, per companion Flow Assurance guide | Used in Calc Sheet 8.4 |
| Software | Aspen HYSYS Dynamics (illustrative — methodology applies equally to UniSim Dynamics, Dynsim; OLGA for the pipeline/multiphase sections) | — |

### 1.2 Codes & Standards / Methodology Basis
- Vendor software documentation (Aspen HYSYS Dynamics, UniSim Dynamics, OLGA, Dynsim) for numerical integration methods and equipment/controller modeling detail
- **API RP 521** — depressurization/flare dynamics referenced from the companion Flare Network Design and Depressurization Calculation guides
- **API 617** — compressor surge/anti-surge referenced from the companion Compressor Settle-Out guide
- Company/project **Dynamic Simulation Basis Document and Scope** — governs which scenarios require dynamic modeling, required model fidelity, and sign-off/validation criteria

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Valve stroke time source | Actual vendor-confirmed actuator response, not a generic catalog default | Section 5.2; a common and consequential source of error — see Case Study, Section 12 |
| Controller tuning basis | Derived from an actual (or representative) process reaction curve, not assumed generic defaults | Calc Sheet 8.1 |
| Anti-surge control margin | 10% (typical, confirm against project/vendor surge control line definition) | Calc Sheet 8.3 |
| Model validation tolerance | ≤10% of step/transient magnitude against plant historical data, or per project standard | Section 7.1, Calc Sheet 8.5 |
| Vessel/equipment geometry detail | Actual internal volumes, elevations, and nozzle locations from the mechanical datasheet (companion guide), not simplified lumped estimates for final design confirmation | Simplified lumped models (Section 8.2) are for first-pass screening only |
| Scope of dynamic modeling | Determined by risk/consequence screening (safety-critical trips, novel configurations) rather than modeling everything to the same level of detail | Confirm project's dynamic simulation scope-setting philosophy |

> ⚠️ **Practical note:** A dynamic simulation is only as good as its time-dependent inputs (valve stroke times, controller tuning, trip logic timing) — a model built with accurate steady-state properties but generic/default dynamic parameters can produce a plausible-looking but materially wrong transient response, exactly the risk explored in the Case Study (Section 12).

---

## 2. Fundamentals

### 2.1 Difference from Steady-State
Where the companion Steady-State Simulation guide models a system at a single, unchanging operating point, dynamic simulation models **transient behavior** — how the system evolves through time during startup, shutdown, or an upset — capturing equipment inventory (mass/energy holdup), valve stroke timing, and controller response, none of which exist in a steady-state model.

### 2.2 Applications
- **Safety studies** — flare load prediction during a real trip transient, compressor surge analysis, depressurization/blowdown timing (Section 5)
- **Control loop tuning** — validating and tuning PID/advanced control strategies before commissioning (Section 4)
- **Operator training** — dynamic models linked to a DCS/PLC mimic for operator training simulators (OTS, Section 5.4)

### 2.3 Software Tools
| Tool | Typical Use |
|---|---|
| **Aspen HYSYS Dynamics** | Extension of the steady-state HYSYS platform into transient mode — common for process/utility system dynamics |
| **UniSim Dynamics** | Functionally similar (Honeywell platform) |
| **OLGA** | Transient multiphase pipeline/wellbore simulation — the standard tool for subsea tieback slugging, restart, and hydrate management dynamics (companion Flow Assurance guide) |
| **Dynsim** (AVEVA/SimSci) | Full-plant dynamic simulation, commonly used for OTS applications |

---

## 3. Transient Operations

### 3.1 Startup/Shutdown Sequences
Heating, pressurization, and depressurization sequences are modeled step-by-step, confirming that equipment stays within its design temperature/pressure envelope and that the sequence timing is operationally realistic — this is where a vessel's MDMT screening (companion Mechanical Datasheet guide) gets its real transient temperature profile, rather than the bounding hand-calc estimate.

### 3.2 Emergency Scenarios
- **Compressor trip** — the transient path from normal operation through the trip event to the final settle-out condition (companion Compressor Settle-Out guide provides the steady-state end point; dynamic simulation shows the path and timing to get there, including any surge risk along the way — Section 5.2).
- **Power failure** — loss of all active control and rotating equipment simultaneously; dynamic simulation shows whether passive protection (relief valves, gravity drainage) is adequate without operator or control system intervention.
- **Valve closure** — rapid valve closure transients (water hammer/surge analysis for liquid systems) that a steady-state model cannot represent at all.

### 3.3 Pipeline Transients
Slugging and hydrate formation during restart (companion Flow Assurance guide) are inherently transient phenomena — a steady-state model can predict whether hydrate risk *exists* at a given condition, but only a dynamic (transient multiphase) model can predict *when* a cooling pipeline crosses into the hydrate region during a specific shut-in duration, which is exactly the information needed for restart procedure timing (Section 6).

---

## 4. Control System Integration

### 4.1 PID Tuning
Proportional, integral, and derivative settings are derived from the process's actual dynamic response (a process reaction curve from a step test, or a model-based tuning method) — see Calc Sheet 8.1 for a worked Ziegler-Nichols reaction-curve tuning example.

### 4.2 Interlocks & ESD Logic
Dynamic simulation can directly simulate the cause & effect (C&E) matrix's logic (companion P&ID/PEFS guide, Section 7.4/9.5) — confirming not just that the *correct* valve closes on a given trip, but that it closes **fast enough**, and that the resulting transient doesn't create a secondary problem (e.g., a valve that closes correctly but too quickly causes a pressure surge elsewhere).

### 4.3 Advanced Control
- **Cascade control** — an outer loop's output becomes an inner loop's setpoint (e.g., a level controller setting a flow controller's setpoint) — dynamic simulation confirms the cascade's inner loop is fast enough relative to the outer loop for stable operation.
- **Ratio control** — maintaining a fixed ratio between two flows (e.g., steam-to-gas ratio on a flare tip, companion Flare Network Design guide, Section 5.1 practical tip about over-steaming).
- **Feed-forward control** — using a measured disturbance to pre-emptively adjust a manipulated variable, reducing the feedback loop's burden — dynamic simulation is the primary tool for validating feed-forward gain/timing before commissioning.
- **Model predictive control (MPC)** — dynamic simulation provides the step-response data MPC controllers are built from, and is used to validate the MPC's predictive model against the real (or simulated) plant dynamics before cutover.

---

## 5. Safety Studies

### 5.1 Flare System Dynamics
Simultaneous relief events and blowdown sequencing are best confirmed with dynamic simulation, since the companion Flare Network Design guide's simultaneous relief methodology (that guide's Section 3.3) assumes a scenario grouping *without* necessarily capturing the actual time-dependent overlap — a dynamic simulation can show whether two relief events' peak flows genuinely coincide in time, or merely occur within the same broad scenario grouping.

### 5.2 Compressor Surge Analysis
Anti-surge valve performance must be checked not just for its steady-state open position (companion Compressor Settle-Out guide's fail-safe logic) but for whether it **opens fast enough** relative to how quickly the operating point can cross into surge during a real trip transient — see Calc Sheet 8.3 for a worked response-time margin check, and the Case Study (Section 12) for a real consequence of getting this wrong.

### 5.3 Depressurization Studies
Vessel cooldown and brittle fracture risk (companion Depressurization Calculation guide's MDMT screening) can be checked against the dynamic simulation's actual transient temperature profile, not just the bounding hand-calc estimate — see Calc Sheet 8.2 for a worked comparison between a simplified time-constant screening method and the companion guide's static sizing approach.

### 5.4 Operator Training Simulators (OTS)
A full-fidelity dynamic model, linked to an actual (or emulated) DCS/PLC interface, lets operators practice startup, shutdown, and emergency response procedures in a realistic, consequence-free environment — the same underlying dynamic model used for safety studies is often extended (with additional fidelity in operator-facing areas) to build the OTS.

---

## 6. Multiphase Flow Dynamics

### 6.1 Slugging in Pipelines
Terrain-induced, riser-induced, and hydrodynamic slugging (companion Flow Assurance guide, Section 7.1) produce genuinely time-varying pressure and liquid flow at the receiving facility — dynamic multiphase simulation predicts the slug volume and frequency needed to size a slug catcher, worked through in Calc Sheet 8.4.

### 6.2 Hydrate Plug Formation/Removal
Restart procedures (companion Flow Assurance guide, Section 7.2) depend on knowing how a shut-in pipeline's temperature profile evolves over the actual shut-in duration — a fundamentally transient question that only a dynamic (or transient multiphase) model can answer with the needed time resolution.

### 6.3 Transient Multiphase Simulators
**OLGA** is the industry-standard tool for subsea tieback transient multiphase modeling — slugging, restart, pigging, and blowdown — providing the pressure/temperature/liquid-holdup time history that purely steady-state flow assurance screening (companion guide) cannot produce.

---

## 7. Validation & QA/QC

### 7.1 Compare Dynamic Simulation Results with Plant Historical Data
Wherever plant historical trend data exists (from a predecessor unit, a similar facility, or the same unit's commissioning data), the dynamic model's predicted transient response should be checked against it — see Calc Sheet 8.5 for a worked example using a simple error-metric comparison.

### 7.2 Sensitivity Analysis
Valve response times and compressor trip scenario assumptions are exactly the kind of input a dynamic model is highly sensitive to — running the model across a credible range of these inputs (rather than a single assumed value) reveals how much margin (or lack of it) exists in the design, consistent with the companion Steady-State Simulation guide's sensitivity analysis principle (that guide's Section 7.2), but now applied to time-dependent inputs.

### 7.3 Documentation
Every dynamic simulation case should record its basis (scenarios modeled, equipment/controller detail level), assumptions (Section 1.3), and limitations (e.g., "valve stroke times per vendor catalog, not yet field-confirmed") — exactly the same documentation discipline as the companion Steady-State Simulation guide's Section 7.3, applied to the additional time-dependent inputs unique to dynamic modeling.

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific dynamic simulation output and vendor-confirmed equipment response data.

### 8.1 Calc Sheet 1 — PID Controller Tuning (Ziegler-Nichols Reaction Curve)

**Given:** FIC-1042 step test (companion Instrumentation guide): process gain K = 2.5, dead time θ = 8 s, time constant τ = 40 s (first-order-plus-dead-time model identified from the step response).

**Step 1 — Ziegler-Nichols PI tuning rules:**
```
Kc = (0.9/K) × (τ/θ)
Ti = 3.33 × θ
```

**Step 2 — Substitute values:**
```
Kc = (0.9/2.5) × (40/8) = 0.36 × 5.0 = 1.8
Ti = 3.33 × 8 = 26.6 s
```

**Result:** Recommended initial PI tuning: **Kc ≈ 1.8, Ti ≈ 26.6 s** (reset rate ≈ 2.25 repeats/min). This is a starting point for controller commissioning, not a final field-tuned value — always fine-tune against actual closed-loop performance, since Ziegler-Nichols reaction-curve tuning is known to produce a somewhat aggressive (oscillatory) response for some processes.

> 📌 **Assumption check:** This assumes a clean first-order-plus-dead-time (FOPDT) fit to the step response — a process with significant higher-order dynamics or strong non-linearity across its operating range may need a more sophisticated tuning method or gain-scheduled tuning rather than a single fixed Kc/Ti pair.

---

### 8.2 Calc Sheet 2 — Blowdown Time-Constant Screening vs. Static Sizing Method

**Given (from the companion Depressurization Calculation guide's worked example):** V = 50 m³, P1 = 3,652 kPa(abs), initial mass m1 = 1,578.4 kg, peak BDV mass flow W_peak = 1.878 kg/s, target P2 = 791 kPa(abs) (100 psig) at t = 900 s.

**Step 1 — Estimate a first-order (isothermal) blowdown time constant:**
```
τ = m1 / W_peak = 1,578.4 / 1.878 ≈ 840 s (≈14.0 min)
```

**Step 2 — Estimate pressure at t = 900 s using a simple exponential decay (isothermal assumption):**
```
P(t)/P1 = exp(−t/τ)
P(900)/P1 = exp(−900/840) = exp(−1.071) ≈ 0.343

P(900) = 0.343 × 3,652 ≈ 1,253 kPa(abs) ≈ 167 psig
```

**Step 3 — Compare to the target (100 psig):**
```
167 psig (simplified screening estimate) > 100 psig (target)  →  Apparent shortfall
```

**Result:** This simplified isothermal time-constant screening estimate suggests the vessel would **not** reach the 100 psig target within 15 minutes — apparently conflicting with the companion Depressurization Calculation guide's static sizing method (which explicitly sized the BDV to meet the target using a peak/average flow approach).

**Why the discrepancy — and why dynamic simulation resolves it:** Real blowdown is **not** isothermal — as the gas expands, its temperature drops (Joule-Thomson/isentropic cooling, per the companion Depressurization guide's Calc Sheet 8.2). Since `P = nZRT/V`, a falling temperature at a given remaining mass produces a **lower** actual pressure than the isothermal model predicts — meaning the true depressurization is **faster** than this simplified screening estimate suggests, not slower. A full dynamic simulation, which properly integrates the coupled mass/energy balance with a real equation of state (exactly as the companion guides caution is needed for final design), captures this cooling-accelerated depressurization and would be expected to show the target reached on schedule, consistent with the static method's design intent.

> 📌 **Assumption check:** This calc sheet's real teaching point is methodological: a simplified screening calculation (like this isothermal time-constant estimate) can give a *pessimistic and misleading* answer if it omits real physics (here, cooling) that dynamic simulation captures — always treat a screening-level hand calc as a bound or sanity check, not a substitute for the rigorous dynamic result, especially when the two disagree.

---

### 8.3 Calc Sheet 3 — Anti-Surge Valve Response Time Margin Check

**Given:** K-101 surge flow = 8,000 ACFM; normal operating flow = 9,500 ACFM; anti-surge control margin, b = 10% (Section 1.3); worst-case flow decay rate during an ESD trip transient (from a prior dynamic simulation run) = −2,000 ACFM/s; anti-surge valve full-stroke opening time (vendor catalog spec) = 2.5 s.

**Step 1 — Surge control line (SCL) flow:**
```
Q_SCL = Q_surge × (1 + b) = 8,000 × 1.10 = 8,800 ACFM
```

**Step 2 — Available flow margin from normal operation to the control line:**
```
ΔQ = Q_normal − Q_SCL = 9,500 − 8,800 = 700 ACFM
```

**Step 3 — Time available before the operating point crosses the surge control line:**
```
t_available = ΔQ / |dQ/dt| = 700 / 2,000 = 0.35 s (350 ms)
```

**Step 4 — Compare to the anti-surge valve's actual response time:**
```
t_available (350 ms) ≪ Valve full-stroke time (2,500 ms)  →  FAIL
```

**Result:** The anti-surge valve, even assuming it fails to the correct open position (companion Compressor Settle-Out guide's fail-safe logic), **cannot physically stroke open fast enough** to prevent the compressor from crossing into surge during this trip transient — the flow decays past the surge control line roughly **7× faster** than the valve can respond.

**Typical mitigation options:** a dedicated fast-acting hot-gas bypass/trip valve (sub-second response, distinct from the normal modulating anti-surge valve), a faster actuator specification, or a revised trip logic that pre-opens the anti-surge valve earlier in the trip sequence (before the flow decay actually begins) rather than reacting to it.

> 📌 **Assumption check:** The flow decay rate used here must come from an actual dynamic simulation of the specific trip scenario, not assumed — different trip causes (power failure vs. a controlled shutdown vs. a downstream block valve closure) can produce very different decay rates, and the anti-surge system must be checked against the fastest credible one. See the Case Study (Section 12) for exactly this finding in a real project context.

---

### 8.4 Calc Sheet 4 — Terrain/Severe Slugging Volume Estimate

**Given:** Subsea tieback riser (companion Flow Assurance guide basis): height H = 1,200 m, ID = 8 in (0.2032 m); severe (Type 1) slugging regime at low flow, where slug length is commonly approximated as the full riser height.

**Step 1 — Riser cross-sectional area:**
```
A = (π/4) × (0.2032)² ≈ 0.0324 m²
```

**Step 2 — Estimated severe-slug volume (slug length ≈ riser height):**
```
V_slug = A × H = 0.0324 × 1,200 ≈ 38.9 m³ (≈ 245 bbl)
```

**Step 3 — Compare to existing slug catcher design capacity (illustrative, 200 bbl):**
```
245 bbl (estimated slug volume) > 200 bbl (slug catcher capacity)  →  FAIL
```

**Result:** The estimated severe-slug volume **exceeds** the assumed slug catcher capacity — the slug catcher would be undersized for a full riser-content slug under severe slugging conditions.

**Typical mitigation options:** increase slug catcher capacity, install riser-base gas lift or a choke management strategy to suppress severe slugging before it develops, or confirm (via a full OLGA transient study, Section 6.3) whether the severe-slugging regime is actually credible across the field's real operating envelope — this simplified riser-height approximation is a conservative bounding estimate, not a substitute for the rigorous transient multiphase simulation result.

> 📌 **Assumption check:** "Slug length ≈ riser height" is a widely used rule-of-thumb bound for severe slugging specifically — it does not apply to terrain-induced or hydrodynamic slugging in the same way, and even for severe slugging it can be conservative or non-conservative depending on the specific flow conditions. Always confirm the governing slugging mechanism (Section 6.1) before applying this shortcut, and use a full OLGA study for final slug catcher sizing.

---

### 8.5 Calc Sheet 5 — Dynamic Model Validation Against Plant Historical Data

**Given:** A 10% step test on the FIC-1042 loop. Actual plant historical trend and the dynamic simulation's predicted response at matching time points (gpm, base flow 100 gpm):

| Time (s) | Actual (plant) | Simulated (model) | Deviation |
|---|---|---|---|
| 0 | 100 | 100 | 0 |
| 10 | 105 | 103 | 2 |
| 20 | 118 | 115 | 3 |
| 30 | 124 | 122 | 2 |
| 40 | 127 | 126 | 1 |

**Step 1 — Root-mean-square error (RMSE) of the deviations:**
```
RMSE = √[(0² + 2² + 3² + 2² + 1²) / 5]
RMSE = √[(0+4+9+4+1)/5] = √(18/5) = √3.6 ≈ 1.90 gpm
```

**Step 2 — Express as a percentage of the total step change magnitude:**
```
Step magnitude = 127 − 100 = 27 gpm
RMSE (%) = 1.90 / 27 × 100% ≈ 7.0%
```

**Step 3 — Compare to the project's validation tolerance (≤10% of step magnitude, Section 1.3):**
```
7.0% < 10%  →  PASS
```

**Result:** The dynamic model's predicted response matches the actual plant data within **≈7.0%** of the step magnitude, inside the project's ≤10% validation tolerance — the model is validated as an adequate representation of this loop's real dynamic behavior and can be relied upon for the tuning/control-system-integration work in Section 4.

> 📌 **Assumption check:** This simple RMSE-against-step-magnitude check is a fast, useful screening validation — for safety-critical dynamic studies (Section 5), a more rigorous validation (comparing multiple scenarios, checking peak values and timing specifically, not just overall RMSE) is warranted before the model is relied upon for a safety case.

---

## 9. Sample Documents & Datasheets

### 9.1 Dynamic Simulation Basis Document Excerpt

| Field | Value |
|---|---|
| **Case name** | GasProc-Dynamic-TripStudy-Rev2 |
| **Software / version** | Aspen HYSYS Dynamics V12 (process); OLGA 2023.1 (subsea tieback) |
| **Scenarios modeled** | K-101 ESD trip, V-100/BDV-101 fire-case depressurization, subsea tieback 8-hr shut-in restart |
| **Valve stroke time source** | Vendor-confirmed actuator data (K-101 anti-surge, BDV-101); catalog default (all other block valves, non-safety-critical) |
| **Controller tuning basis** | Field step-test data (FIC-1042, per Calc Sheet 8.1); design-stage estimate (all other loops, to be field-tuned at commissioning) |
| **Validation status** | FIC-1042 loop validated against plant data (Calc Sheet 8.5) — PASS; K-101 anti-surge response time check — FAIL, mitigation required (Calc Sheet 8.3) |
| **Known limitations** | Subsea tieback modeled as a simplified single-riser case; full multi-well network transient study pending |
| **Prepared by / Date / Revision** | — |

---

### 9.2 Sample Transient Event Summary Table

| Event | Trigger | Key Result | Status |
|---|---|---|---|
| K-101 ESD trip | Loss of power / manual ESD | Anti-surge valve response time 350 ms available vs. 2.5 s actuator — surge not prevented | FAIL — mitigation in progress (Calc Sheet 8.3) |
| V-100/BDV-101 fire-case depressurization | Confirmed fire detection | Target 100 psig within 15 min — dynamic simulation confirms static sizing basis (Calc Sheet 8.2 discussion) | PASS (pending final dynamic confirmation) |
| Subsea tieback 8-hr shut-in restart | Planned/unplanned shutdown | Hydrate subcooling margin maintained through 6-hr passive protection window; extended-shutdown procedure required beyond that (companion Flow Assurance guide) | PASS with procedural mitigation |

---

### 9.3 Sample Control Loop Tuning Summary

| Loop | Type | Kc | Ti (s) | Td (s) | Tuning Basis |
|---|---|---|---|---|---|
| FIC-1042 | PI (flow) | 1.8 | 26.6 | — | Ziegler-Nichols reaction curve (Calc Sheet 8.1) |
| LIC-3005 | PI (level, cascade outer) | (per project) | (per project) | — | To be field-tuned; cascade to FIC-1042 |
| PIC-3001 (anti-surge) | PID | (per vendor package) | (per vendor package) | (per vendor package) | Vendor-supplied anti-surge controller, validated per Calc Sheet 8.3 response-time check |

---

## 10. Practical Design Checklist

- [ ] Dynamic simulation basis document issued and approved (Section 1) before detailed transient modeling begins
- [ ] Valve stroke times and controller tuning sourced from vendor-confirmed data (not generic catalog defaults) for every safety-critical loop/valve
- [ ] PID tuning derived from an actual or representative process reaction curve — see Calc Sheet 8.1
- [ ] Depressurization/blowdown dynamic results cross-checked against the companion Depressurization Calculation guide's static sizing basis, with any discrepancy explained (not just noted) — see Calc Sheet 8.2
- [ ] Anti-surge valve response time explicitly checked against the fastest credible trip transient's flow decay rate, not just its fail-safe position — see Calc Sheet 8.3
- [ ] Slug catcher sizing checked against a transient multiphase (OLGA) severe-slugging estimate, not steady-state flow assurance screening alone — see Calc Sheet 8.4
- [ ] Dynamic model validated against available plant historical data before being relied upon for safety-critical conclusions — see Calc Sheet 8.5
- [ ] Sensitivity analysis performed on valve response times and trip scenario assumptions (Section 7.2)
- [ ] Every dynamic simulation case documented with basis, assumptions, and explicitly stated limitations (Section 7.3)
- [ ] Cause & effect matrix logic (companion P&ID/PEFS guide) directly simulated, not just assumed adequate from the static logic table alone
- [ ] OTS scope (if applicable) explicitly defined and coordinated with the underlying safety-study dynamic model, to avoid duplicated/divergent model development

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Compressor surged during an actual ESD trip despite a "correctly" fail-open anti-surge valve | Valve's actual response time never checked against the trip's real flow decay rate | Explicitly calculate available response time vs. actuator speed for every credible trip scenario — see Calc Sheet 8.3 and Case Study, Section 12 |
| Dynamic simulation results distrusted by operations after commissioning | Model never validated against any plant/commissioning data before being used to justify design decisions | Perform Section 7.1/Calc Sheet 8.5-style validation as a standard step, not an afterthought |
| Simplified screening hand-calc appeared to contradict a static design guide's sizing result | Screening calc omitted real physics (e.g., cooling effects) captured by the rigorous method | Understand and document *why* a screening calc might reasonably disagree with a more rigorous result, rather than treating disagreement as an automatic red flag — see Calc Sheet 8.2 |
| Slug catcher overflowed shortly after startup | Sizing based on steady-state flow assurance screening only, without a transient severe-slugging volume check | Always cross-check slug catcher sizing against a transient multiphase (OLGA) severe-slugging estimate — see Calc Sheet 8.4 |
| PID loop oscillated badly after commissioning despite "passing" simulation | Tuning derived from a generic default rather than an actual process reaction curve for that specific loop | Derive tuning from real step-test/reaction-curve data wherever possible — see Calc Sheet 8.1 |

---

## 12. Case Study — Anti-Surge Valve Too Slow to Prevent Surge During ESD Trip

> A composite, illustrative case study based on the type of finding commonly encountered during dynamic simulation studies of compressor trip scenarios. Names, tag numbers, and figures are representative, not project-specific, and is a companion finding to (but distinct from) the anti-surge case study in the companion Compressor Settle-Out Calculations guide.

### 12.1 Background

Following the events described in the companion Compressor Settle-Out Calculations guide's case study (where an anti-surge valve was found to have the wrong fail-safe position), the project team commissioned a full dynamic simulation study of K-101's ESD trip scenario as an additional verification step — specifically to confirm that, with the fail-safe position now corrected to fail-open, the anti-surge system would actually protect the machine during a real trip transient.

### 12.2 Problem Identified

The dynamic simulation (Aspen HYSYS Dynamics, modeling the actual trip logic, valve actuator dynamics, and compressor performance map) revealed that even with the anti-surge valve correctly failing open, its **stroke time** — 2.5 seconds to full open, per the vendor's standard catalog actuator — was far too slow relative to how quickly the compressor's operating point crossed the surge control line during the modeled trip transient. This is exactly the finding worked through in this guide's Calc Sheet 8.3: only 350 ms of margin was available against a 2.5-second valve response.

This finding could **not** have been produced by the companion Compressor Settle-Out guide's steady-state methodology alone — that guide's methodology correctly determines the *end-state* settle-out pressure and confirms the *fail-safe position* is correct, but has no mechanism to evaluate whether the valve responds *fast enough* during the transient path to that end state. Only a dynamic simulation, modeling the actual time-dependent flow decay and valve stroke dynamics together, could reveal this gap.

### 12.3 Investigation & Recalculation

The team reran the Calc Sheet 8.3 methodology with the actual dynamic simulation's flow decay rate (−2,000 ACFM/s, consistent with this guide's worked example) and confirmed the valve's vendor-catalog 2.5-second stroke time provided a **7× shortfall** against the available 350 ms response window — the compressor's operating point would cross into surge before the anti-surge valve could meaningfully open, risking mechanical damage (thrust bearing loading, potential impeller damage) from even a brief surge event.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **Valve actuator selection based on generic catalog response time**, appropriate for a standard modulating control application, but never independently checked against the specific, scenario-derived response-time requirement this safety-critical anti-surge application actually demanded.
2. **No dynamic simulation performed at the original valve specification stage** — the anti-surge valve had been specified and procured based on steady-state settle-out and standard vendor sizing practice alone; the dynamic transient check was only added later, as a supplementary verification step, rather than being built into the original specification workflow.

### 12.5 Resolution

- A dedicated, faster-acting **hot-gas bypass/trip valve** was added in parallel with the standard modulating anti-surge valve — sized and actuated specifically for sub-second response, intended to open immediately upon ESD trip initiation (pre-emptively, per the trip logic, rather than reactively based on a measured approach to the surge control line) rather than relying on the standard anti-surge controller's normal modulating response.
- The dynamic simulation was rerun with the new trip valve included, confirming the compressor's operating point now stayed clear of the surge control line throughout the modeled trip transient.
- The project's valve specification procedure was updated to require: for any valve identified as safety-critical during a dynamic simulation scope-setting exercise (Section 1.3), the **response-time requirement must be derived from an actual dynamic simulation of the credible trip scenario**, and the vendor's actuator must be selected/confirmed against that specific requirement — not a generic modulating-control response time.

### 12.6 Outcome

- The gap was caught during a dedicated dynamic simulation study, before commissioning — avoiding a real surge event and potential compressor damage, but requiring an additional procurement cycle (the hot-gas bypass trip valve) with an associated cost and schedule impact.
- The finding reinforced the value of dynamic simulation as a **distinct and necessary** check beyond steady-state settle-out analysis for any compressor with an anti-surge protection scheme — the project's engineering standard was updated to require a dynamic trip-transient simulation as a mandatory step for all new compressor installations, not an optional supplementary study.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A correctly fail-safe anti-surge valve is not the same as a fast-enough anti-surge valve | Explicitly calculate the available response-time margin against the valve's actual stroke time for every credible trip scenario — Calc Sheet 8.3 |
| Steady-state settle-out analysis and dynamic transient analysis answer genuinely different questions | Treat dynamic simulation as a distinct, necessary check for safety-critical rotating equipment protection schemes, not an optional add-on to the steady-state study |
| Generic vendor catalog response times are appropriate for standard modulating control, not necessarily for safety-critical trip response | Derive response-time requirements from actual dynamic simulation before specifying/procuring a safety-critical valve actuator |
| Catching a dynamic response gap before commissioning avoids the much higher cost of a real surge event or in-service failure | Build dynamic trip-transient simulation into the standard specification workflow for compressor protection schemes, not as an after-the-fact supplementary study |

---

## 13. Reference Standards & Tools

- **API RP 521** — Pressure-relieving and Depressuring Systems (referenced for depressurization/flare dynamics basis)
- **API STD 617** — Axial and Centrifugal Compressors (referenced for surge/anti-surge basis)
- Aspen Technology — **Aspen HYSYS Dynamics** documentation
- Honeywell — **UniSim Dynamics** documentation
- Schlumberger (SLB) — **OLGA** transient multiphase simulator documentation
- AVEVA (formerly SimSci) — **Dynsim** documentation
- Ziegler, J.G. & Nichols, N.B. (1942) — original process reaction curve controller tuning method

---

*This guide is a practical study reference combining standard dynamic simulation methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific dynamic simulation output, vendor-confirmed equipment response data, and current regulatory/code requirements. This guide should be read alongside the companion Flare Network Design, Depressurization Calculation, Compressor Settle-Out Calculations, Flow Assurance, and Steady-State Simulation study guides, since dynamic simulation is where those studies' steady-state and static results are tested against real time-dependent behavior.*
