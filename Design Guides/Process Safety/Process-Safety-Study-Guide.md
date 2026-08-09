# 🛡️ Process Safety — Practical Study Guide

> A field-oriented reference covering the core engineering topics in process safety engineering — combining API/OSHA/CCPS methodology with worked sample calculations, sample documents, and design-basis assumptions drawn from real project execution. This guide is the capstone companion to the **Flare Network Design**, **Depressurization Calculation**, **Compressor Settle-Out Calculations**, **Line List Preparation**, **Instrumentation Process Datasheet Preparation**, **Mechanical Datasheet Preparation**, **P&ID/PEFS Development**, **Steady-State Simulation**, **Dynamic Simulation**, and **Process Philosophies** study guides — process safety is the discipline that ties every one of those guides' individual outputs into a coherent, risk-managed whole, from design through operations.

**Illustrative project used throughout this guide:** the same gas processing plant (V-100, K-101, E-101, BDV-101/PSV-101) used across this guide series — used to work through a HAZOP risk-ranking calculation, a vapor cloud explosion blast/siting check, an AIV screening at a pressure let-down point, a firewater demand calculation, and a SIL/PFD verification for a redundant sensor architecture. All numbers below are worked sample calculations for study purposes — always replace with project-specific hazard, reliability, and site data.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Foundations & Standards](#2-foundations--standards)
3. [Hazard Identification & Risk Assessment](#3-hazard-identification--risk-assessment)
4. [Relief & Flare Systems](#4-relief--flare-systems)
5. [Fire & Explosion Safety](#5-fire--explosion-safety)
6. [Process Safety in Design](#6-process-safety-in-design)
7. [Operational Safety](#7-operational-safety)
8. [Specialized Topics](#8-specialized-topics)
9. [Sample Calculation Sheets](#9-sample-calculation-sheets)
10. [Sample Documents & Datasheets](#10-sample-documents--datasheets)
11. [Practical Design Checklist](#11-practical-design-checklist)
12. [Common Field Issues & Lessons Learned](#12-common-field-issues--lessons-learned)
13. [Case Study — Unauthorized Bypass Removes a Safety Interlock Without MOC Review](#13-case-study--unauthorized-bypass-removes-a-safety-interlock-without-moc-review)
14. [Reference Standards](#14-reference-standards)

---

## 1. Design Basis & Assumptions

Process safety spans the full project life cycle — from the earliest HAZID screening through detailed design (where it draws directly on the companion Flare Network, Depressurization, Mechanical Datasheet, and Process Philosophies guides) and into operations (permit-to-work, MOC, incident investigation). Unlike the discipline-specific guides earlier in this series, this guide's "design basis" is really a **risk basis** — the criteria against which every hazard, safeguard, and mitigation decision is judged.

### 1.1 Project & Risk Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Facility | Same gas processing plant used throughout this guide series | V-100, K-101, E-101, BDV-101/PSV-101 |
| Company risk matrix | 5×5 severity × likelihood, action thresholds: Low (1–5), Medium/ALARP (6–11), High (12–25) | Used in Calc Sheet 9.1 |
| VCE ignition scenario (siting check) | 2,000 kg flammable vapor release, delayed ignition | Used in Calc Sheet 9.2 |
| AIV screening location | Pressure let-down tie-in upstream of the flare header | Used in Calc Sheet 9.3 |
| Firewater design fire case | Largest single fire zone, 4-hour minimum duration | Used in Calc Sheet 9.4 |
| SIF sensor architecture | 1oo2 pressure transmitters, high-high pressure trip | Used in Calc Sheet 9.5 |

### 1.2 Codes & Standards / Methodology Basis
- **API 520/521/537** — relief systems and flare design (companion Flare Network Design and Depressurization Calculation guides)
- **OSHA PSM (29 CFR 1910.119)** — the 14-element US regulatory framework for process safety management
- **CCPS Guidelines** (Center for Chemical Process Safety) — industry best-practice guidance underlying much of modern process safety methodology, including LOPA and inherently safer design
- **ISO 45001** — occupational health & safety management systems
- **API RP 752/753** — facility siting for occupied buildings (onshore/offshore respectively)
- **IEC 61508/61511** — functional safety (companion Instrumentation and Process Philosophies guides)

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| VCE explosion yield factor, η | 0.02–0.10 (use 0.03 as a typical mid-range screening value) | Highly scenario- and congestion-dependent; confirm with a proper consequence modeling tool for final siting decisions |
| Blast overpressure threshold for occupied buildings | 0.2 bar (moderate structural damage) as a common screening criterion | Confirm actual company/API 752 criteria — some use multiple thresholds for different building types/occupancy |
| AIV Mach number screening bands | <0.3 typically low risk; 0.3–0.5 requires Level 2 assessment; >0.5 high risk | Illustrative — always use the current Energy Institute AIV guideline's full methodology for final assessment, not a Mach-only proxy |
| Firewater design duration | 4 hours minimum (confirm against API 2030/NFPA and project-specific risk basis) | Calc Sheet 9.4 |
| SIF common cause factor (β) | 2% for a reasonably diverse/separated redundant sensor pair | Confirm against actual installation independence (separate impulse lines, different manufacturers/models where practical) |

> ⚠️ **Practical note:** Every calculation in Section 9 answers a version of the same underlying process safety question: **"is the risk as low as reasonably practicable (ALARP), and can I show my work?"** — a qualitative judgment ("this seems safe enough") is not the same as a documented, defensible calculation against a stated criterion, and only the latter holds up under audit or incident investigation.

---

## 2. Foundations & Standards

### 2.1 API 520/521/537
The core relief-system and flare-design standards implemented in detail by the companion Flare Network Design and Depressurization Calculation guides — PSV sizing (API 520), relief system and depressurization philosophy (API 521), and flare tip design (API 537).

### 2.2 OSHA PSM (29 CFR 1910.119)
The US regulatory framework organizing process safety into 14 elements: Process Safety Information, Process Hazard Analysis, Operating Procedures, Training, Contractor Safety, Pre-Startup Safety Review, Mechanical Integrity, Hot Work Permit, Management of Change, Incident Investigation, Emergency Planning and Response, Compliance Audits, Trade Secrets, and Employee Participation. Most of the topics in Sections 3–8 of this guide map directly onto one or more of these 14 elements.

### 2.3 CCPS Guidelines
The Center for Chemical Process Safety publishes widely adopted industry best-practice guidance underlying much of modern process safety methodology — including the LOPA methodology referenced in the companion Process Philosophies guide (Section 5.3/Calc Sheet 8.2 of that guide) and inherently safer design principles (Section 6.1 of this guide).

### 2.4 ISO 45001
The international standard for occupational health & safety management systems — broader than process safety alone (covering general workplace safety), but establishing the management-system framework (policy, planning, support, operation, performance evaluation, improvement) that a mature process safety program typically integrates with.

---

## 3. Hazard Identification & Risk Assessment

### 3.1 HAZOP (Hazard & Operability Study)
A systematic, node-by-node review of the P&ID (companion P&ID/PEFS Development guide) using guide words (More, Less, No, Reverse, etc.) applied to process parameters (flow, pressure, temperature, level) to identify credible deviations, their causes, consequences, existing safeguards, and any required actions. See Calc Sheet 9.1 for a worked risk-ranking example of a single HAZOP finding.

### 3.2 HAZID (Hazard Identification)
An earlier-stage, broader-brush risk screening — typically performed at concept/FEED stage, before detailed P&IDs exist, to identify major hazards and inform facility siting (Section 6.2), inherently safer design opportunities (Section 6.1), and the overall risk basis that later HAZOP and LOPA studies will build on in detail.

### 3.3 LOPA (Layer of Protection Analysis)
A semi-quantitative method for determining whether existing/proposed independent protection layers adequately reduce an initiating event's frequency to a tolerable level — worked through in detail in the companion Process Philosophies guide (that guide's Calc Sheet 8.2), which derives the required SIL for a new safety instrumented function from a LOPA calculation.

### 3.4 SIL (Safety Integrity Level) Studies
Beyond determining the *required* SIL (LOPA, Section 3.3), a SIL **verification** study confirms that a *specific, as-designed* safety instrumented function architecture actually **achieves** its target SIL, given the real failure rates and redundancy of its sensors, logic solver, and final elements — see Calc Sheet 9.5 for a worked PFD verification example.

---

## 4. Relief & Flare Systems

### 4.1 PSV Sizing and Selection
Detailed in the companion Flare Network Design guide (Section 8.1's fire-case relief load calculation and Section 8.4's orifice sizing) and the companion Instrumentation guide's PSV instrument datasheet (Section 10.4 of that guide).

### 4.2 Flare Header Hydraulics and Radiation Analysis
Detailed in the companion Flare Network Design guide (Sections 3 and 6, and Calc Sheets 8.2 and 8.4 of that guide) — backpressure verification and radiation distance screening.

### 4.3 Blowdown and Depressurization Studies
Detailed in the companion Depressurization Calculation guide, and cross-checked against dynamic simulation (companion Dynamic Simulation guide's Calc Sheet 8.2) and the blowdown sequencing philosophy (companion Process Philosophies guide's Calc Sheet 8.3).

### 4.4 Flare Gas Recovery Systems (FGRS)
Detailed in the companion Flare Network Design guide (Section 4.1) and justified economically in the companion Process Philosophies guide's Calc Sheet 8.4.

---

## 5. Fire & Explosion Safety

### 5.1 Fire Case Depressurization (API 521)
Detailed in the companion Depressurization Calculation guide's Section 6 and Calc Sheets 8.1–8.3 — the target pressure/time basis and wall-temperature/MDMT screening.

### 5.2 Explosion Venting and Blast Load Analysis
Where a vapor cloud explosion (VCE) is a credible scenario, blast overpressure at occupied buildings and critical equipment must be estimated and checked against a siting criterion — see Calc Sheet 9.2 for a worked TNT-equivalency example. Explosion **venting** (for enclosed/indoor process areas or buildings where an internal deflagration is credible) is a related but distinct discipline, sizing vent panels/area to limit internal overpressure per NFPA 68 or equivalent — not worked in detail in this guide, but governed by the same underlying risk basis.

### 5.3 Firewater System Design and Firefighting Philosophies
Fixed fire protection (deluge/spray systems), monitors, and hose stream demand must be sized against the facility's design fire scenario and an adequate supply duration — see Calc Sheet 9.4 for a worked example, and Section 3 of the companion Process Philosophies guide for how firewater fits into the broader utility philosophy.

---

## 6. Process Safety in Design

### 6.1 Inherently Safer Design Principles
The CCPS hierarchy — **Eliminate, Substitute, Moderate, Simplify** — should be applied in that order of preference before relying on added-on protective systems:
- **Eliminate** — remove the hazard entirely (e.g., eliminate an unnecessary intermediate storage inventory)
- **Substitute** — use a less hazardous material or condition (e.g., a lower-toxicity solvent)
- **Moderate** — reduce the hazard's magnitude (e.g., lower inventory, lower pressure/temperature)
- **Simplify** — reduce complexity that creates opportunity for error (e.g., fewer interconnections, clearer operating envelope)

Every added PSV, BDV, or SIF (companion Flare Network, Depressurization, and Instrumentation guides) is, in this hierarchy, a *lower-preference* mitigation compared to genuinely removing or reducing the underlying hazard — a mature process safety review should ask "could this hazard have been designed out?" before defaulting straight to "what protective system do we need?"

### 6.2 Facility Siting and Layout (API RP 752/753)
Occupied buildings, control rooms, and critical equipment must be sited with adequate separation from blast, fire, and toxic release hazards — see Calc Sheet 9.2 for a worked blast-distance example directly applicable to this section.

### 6.3 Material Selection for Corrosive/Toxic Service
Detailed in the companion Flow Assurance guide (corrosion/erosion screening, Section 6 of that guide) and the companion Mechanical Datasheet guide (Section 4.1's material selection basis) and Line List guide's sour-service PMS logic (Section 5 of that guide).

### 6.4 Isolation and ESD Philosophies
Detailed in the companion Process Philosophies guide's Section 6 (ESD levels, DBB vs. spectacle blind, brownfield isolation strategy).

---

## 7. Operational Safety

### 7.1 Permit-to-Work Systems
Formal authorization systems (hot work, confined space entry, line breaking, electrical isolation) that control non-routine work on operating equipment — a critical control, but one that depends entirely on disciplined execution, not just the existence of the procedure (see the Case Study, Section 13, for what happens when a related control — MOC — is bypassed under time pressure).

### 7.2 Management of Change (MOC)
Every technical, procedural, or organizational change to a process facility should pass through a formal MOC review before implementation — confirming the change doesn't inadvertently remove or degrade a safeguard, consistent with the "any change must trigger a controlled revision" principle emphasized throughout this guide series (companion Line List, Mechanical Datasheet, and Process Philosophies guides' case studies all illustrate variations of this same principle at the *design* stage; the Case Study in this guide, Section 13, illustrates the *operational* equivalent).

### 7.3 Incident Investigation and Root Cause Analysis (RCA)
When a process safety event (or near-miss) occurs, a structured RCA — identifying not just the immediate cause but the underlying systemic/organizational root causes — is essential both for correcting the specific issue and for identifying whether the same gap exists elsewhere in the facility or organization (a recurring theme in nearly every case study across this guide series: a design or procedural gap, once found, prompts a broader portfolio review).

### 7.4 Lessons Learned Capture and Dissemination
A finding from one unit, one project, or one incident has value far beyond its original context only if it's captured and actively shared — every case study in this guide series ends with exactly this kind of "lessons learned" table specifically because that discipline (documenting and disseminating findings, not just fixing the immediate issue) is itself a core process safety practice, not just a formatting convention.

---

## 8. Specialized Topics

### 8.1 Acoustic-Induced Vibration (AIV) and Flow-Induced Vibration (FIV)
High-velocity gas flow, particularly downstream of pressure let-down (control valves, PSVs) or at flow discontinuities, can generate acoustic energy strong enough to fatigue-crack small-bore connections and welds — introduced briefly in the companion Flare Network Design guide (Section 3.2) and worked through in more detail here as a dedicated screening calculation (Calc Sheet 9.3). FIV is a related but mechanistically distinct phenomenon (flow-induced mechanical vibration, e.g., vortex shedding) requiring its own screening methodology, not covered in detail in this guide.

### 8.2 Human Factors Engineering
Operator interface design (alarm philosophy, HMI graphics, control room layout) and alarm management (rationalization, prioritization, nuisance-alarm reduction) directly affect an operator's ability to correctly diagnose and respond to an abnormal situation — detailed in the companion Process Philosophies guide's Section 5.2, and directly relevant to why the operator-response IPL credited in a LOPA calculation (companion guide's Calc Sheet 8.2) is only as reliable as the alarm system actually supporting that response.

### 8.3 Emergency Response Planning
Evacuation, firefighting (Section 5.3), and spill containment planning — the operational counterpart to the design-stage mitigations covered elsewhere in this guide series, ensuring that even where a hazard scenario does develop, personnel and the environment are protected through a well-rehearsed response plan.

---

## 9. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific hazard, reliability, and site data.

### 9.1 Calc Sheet 1 — HAZOP Risk Ranking

**Given:** HAZOP node on the V-100 inlet line, deviation "More Pressure," cause: control valve fails open. Unmitigated consequence: potential vessel overpressure, major safety consequence. Company 5×5 risk matrix (Section 1.1): Severity 1–5, Likelihood 1–5, Score = Severity × Likelihood; Low 1–5, Medium/ALARP 6–11, High 12–25.

**Step 1 — Unmitigated risk score:**
```
Severity = 4 (major — potential single fatality / major asset damage)
Likelihood = 4 (likely, no independent protection credited yet)
Risk score = 4 × 4 = 16  →  High risk band
```

**Step 2 — Credit the existing independent safeguard (PSV-101, mechanical protection independent of the control system):**
```
Crediting one genuinely independent protection layer typically reduces the likelihood
score by ~1–2 ordinal categories (company-specific methodology; broadly consistent
with an order-of-magnitude frequency reduction, per LOPA principles).

Likelihood: 4 → 2
```

**Step 3 — Mitigated risk score:**
```
Risk score = Severity (4) × Likelihood (2) = 8  →  Medium/ALARP band
```

**Result:** With PSV-101 credited, the mitigated risk score (**8**) falls within the Medium/ALARP band — **acceptable**, provided PSV-101's ongoing mechanical integrity (inspection/testing per the companion Mechanical Datasheet guide's assumptions and the facility's mechanical integrity program, OSHA PSM element) is maintained. No further HAZOP action item is required beyond confirming this testing assurance.

> 📌 **Assumption check:** This ordinal risk-matrix approach is a fast, useful HAZOP-stage tool, but it is not a substitute for a full LOPA (Section 3.3) when the finding is significant enough to warrant more rigorous, frequency-based justification — many companies' HAZOP procedures explicitly require escalation to LOPA for any finding scoring in the High band, or any finding proposing a new SIF.

---

### 9.2 Calc Sheet 2 — Vapor Cloud Explosion (VCE) Blast Distance (TNT Equivalency)

**Given:** Credible large leak scenario near K-101, releasing W_hc = 2,000 kg of flammable hydrocarbon vapor before delayed ignition. Explosion yield factor η = 0.03 (Section 1.3). Heat of combustion ΔHc ≈ 46,000 kJ/kg; TNT heat of detonation ΔHc,TNT = 4,680 kJ/kg. Blast overpressure threshold for occupied buildings = 0.2 bar (Section 1.3). Existing control room location: 20 m from the release point.

**Step 1 — TNT-equivalent mass:**
```
W_TNT = η × W_hc × (ΔHc/ΔHc,TNT)
W_TNT = 0.03 × 2,000 × (46,000/4,680)
W_TNT = 60 × 9.829
W_TNT ≈ 589.7 kg TNT-equivalent
```

**Step 2 — Cube root of TNT-equivalent mass (for Hopkinson-Cranz scaling):**
```
W_TNT^(1/3) = 589.7^(1/3) ≈ 8.39
```

**Step 3 — Scaled distance for the 0.2 bar (20 kPa) overpressure threshold (from a standard Kingery-Bulmash-type curve, illustrative reading):**
```
Z ≈ 3.3 m/kg^(1/3) at Pso = 0.2 bar
```

**Step 4 — Required actual distance:**
```
R = Z × W_TNT^(1/3) = 3.3 × 8.39 ≈ 27.7 m
```

**Step 5 — Compare to the existing control room distance:**
```
Existing control room distance (20 m) < Required distance (27.7 m)  →  FAIL
```

**Result:** The existing control room, at 20 m, sits **within** the estimated 0.2 bar blast exclusion distance (≈27.7 m) — a facility siting finding requiring mitigation: relocate the control room, provide blast-resistant design for the existing structure, or reduce the credible release scenario's magnitude (e.g., via inventory reduction/inherently safer design, Section 6.1) to shrink the hazard distance.

> 📌 **Assumption check:** This is a simplified screening-level TNT-equivalency estimate — final facility siting decisions per API RP 752/753 should use a validated consequence modeling tool (e.g., a dedicated VCE/blast modeling package) with a site-specific congestion/confinement assessment, since the TNT-equivalency method's yield factor and scaled-distance curve are both significant sources of uncertainty for a real, non-ideal vapor cloud geometry.

---

### 9.3 Calc Sheet 3 — AIV Screening at a Pressure Let-Down Point

**Given:** Flare header tie-in downstream of a pressure let-down point, mass flow ṁ = 25 kg/s, downstream gas density ρ = 3 kg/m³ (low, post-expansion), pipe ID = 254.4 mm (10-in, wall 9.3 mm), gas properties k = 1.3, Z = 0.95, T = 280 K, MW = 19.

**Step 1 — Pipe flow area:**
```
A = (π/4) × (0.2544)² ≈ 0.0508 m²
```

**Step 2 — Actual gas velocity:**
```
V = ṁ / (ρ × A) = 25 / (3 × 0.0508) = 25 / 0.1525 ≈ 163.9 m/s
```

**Step 3 — Speed of sound at these conditions:**
```
c = √(k × Z × R × T / MW)
c = √(1.3 × 0.95 × 8,314 × 280 / 19)
c = √(2,874,981 / 19) ≈ √151,315 ≈ 389.0 m/s
```

**Step 4 — Mach number:**
```
M = V/c = 163.9/389.0 ≈ 0.42
```

**Step 5 — Compare against the Section 1.3 screening bands:**
```
0.3 < M(0.42) < 0.5  →  Medium-risk band — Level 2 detailed AIV assessment required
```

**Result:** At Mach ≈0.42, this pressure let-down tie-in falls in the **medium-risk band**, requiring a **Level 2 Energy Institute AIV assessment** before finalizing the piping design — and, in the interim, avoiding any small-bore branch connections (instrument tees, vents, drains) within this pipe run, since small-bore connections at exactly this kind of high-velocity, high-turbulence location are the classic AIV fatigue-failure point.

> 📌 **Assumption check:** This Mach-number screening is a fast first-pass proxy consistent with the companion Flare Network Design guide's Section 3.2 approach — it is not a substitute for the full Energy Institute AIV methodology (which also considers pipe diameter, wall thickness, weld/fitting geometry, and sound power level), which should be applied for any location screening into the medium-or-higher risk band before finalizing the mechanical design.

---

### 9.4 Calc Sheet 4 — Firewater Demand Calculation

**Given:** Largest single fire zone (design fire case) requires: fixed water spray coverage over a 2,000 ft² wetted equipment area at an application rate of 0.25 gpm/ft²; 2 monitor nozzles at 500 gpm each (minimum practice); 2 hose streams at 250 gpm each (minimum per typical NFPA practice). Design duration = 4 hours (Section 1.3). Existing firewater storage tank capacity = 400,000 gallons.

**Step 1 — Fixed spray system demand:**
```
Fixed spray = 2,000 ft² × 0.25 gpm/ft² = 500 gpm
```

**Step 2 — Monitor nozzle demand:**
```
Monitors = 2 × 500 gpm = 1,000 gpm
```

**Step 3 — Hose stream demand:**
```
Hose streams = 2 × 250 gpm = 500 gpm
```

**Step 4 — Total firewater demand:**
```
Total demand = 500 + 1,000 + 500 = 2,000 gpm
```

**Step 5 — Required storage volume for the design duration:**
```
Required volume = 2,000 gpm × 240 min = 480,000 gallons
```

**Step 6 — Compare to existing tank capacity:**
```
480,000 gal (required) > 400,000 gal (existing capacity)  →  FAIL
```

**Result:** The existing 400,000-gallon firewater storage tank is **undersized** by 80,000 gallons against the design fire case's 4-hour demand — requiring additional storage capacity, a supplemental water source (e.g., a secondary tank, tie-in to a larger raw water source, or — for offshore/coastal facilities — a seawater lift system), or a reassessment of the design fire scenario's basis.

> 📌 **Assumption check:** The individual component demands (application rate, number of monitors/hose streams) used here are simplified, typical values — actual firewater system design must follow the applicable NFPA standards (e.g., NFPA 15 for water spray systems) and the project's specific fire hazard analysis, which may identify a larger or smaller design fire case than this illustrative example.

---

### 9.5 Calc Sheet 5 — SIL Verification: PFD for a 1oo2 Sensor Architecture

**Given:** High-high pressure trip SIF, sensor subsystem = 1oo2 (two pressure transmitters, either alone can initiate the trip — a redundant, fault-tolerant architecture). Dangerous undetected failure rate per transmitter, λDU = 5×10⁻⁷/hr. Proof test interval, T1 = 8,760 hr (1 year). Common cause factor, β = 2% (Section 1.3).

**Step 1 — Single-channel average probability of failure on demand:**
```
PFDavg,single = λDU × T1 / 2 = (5×10⁻⁷ × 8,760) / 2 = 4.38×10⁻³ / 2 = 2.19×10⁻³
```

**Step 2 — 1oo2 architecture, independent-failure contribution (simplified IEC 61508 formula):**
```
PFDavg,independent = (λDU × T1)² / 3 = (4.38×10⁻³)² / 3 = 1.918×10⁻⁵ / 3 ≈ 6.39×10⁻⁶
```

**Step 3 — Common-cause contribution:**
```
PFDavg,CC = β × λDU × T1 / 2 = 0.02 × 2.19×10⁻³ ≈ 4.38×10⁻⁵
```

**Step 4 — Total 1oo2 sensor subsystem PFDavg:**
```
PFDavg,1oo2 ≈ (1−β)² × PFDavg,independent + PFDavg,CC
PFDavg,1oo2 ≈ (0.98)² × 6.39×10⁻⁶ + 4.38×10⁻⁵
PFDavg,1oo2 ≈ 6.14×10⁻⁶ + 4.38×10⁻⁵ ≈ 5.0×10⁻⁵
```

**Result:** The 1oo2 sensor subsystem's PFDavg ≈ **5.0×10⁻⁵** — well within even a SIL 3 sensor-subsystem budget, and **common-cause failure dominates** the redundant architecture's overall PFD (≈4.4×10⁻⁵ of the ≈5.0×10⁻⁵ total), not independent random failures — reinforcing why physically separating the two transmitters' impulse lines, and using different manufacturers/models where practical, matters more than simply adding a second identical unit.

> 📌 **Assumption check:** This is the **sensor subsystem's** contribution only — the overall SIF's PFD is the sum of the sensor, logic solver, and final element (valve) contributions, and the final element is very often the dominant term (a single, non-redundant safety valve's PFD is commonly an order of magnitude or more higher than this sensor result) — see the companion Compressor Settle-Out and Dynamic Simulation guides' anti-surge valve case studies for real examples of the final element being the actual limiting factor in a protection scheme's real-world performance, which a PFD calculation alone (without checking the *dynamic response time*, per that guide's Calc Sheet 8.3) would not have revealed.

---

## 10. Sample Documents & Datasheets

### 10.1 Sample HAZOP Worksheet Excerpt

| Node | Deviation | Cause | Consequence | Safeguard | Risk (Unmitigated → Mitigated) | Action |
|---|---|---|---|---|---|---|
| V-100 inlet | More Pressure | FCV-1042 fails open | Vessel overpressure | PSV-101 | 16 (High) → 8 (Medium/ALARP) | None — confirm PSV testing assurance |
| V-100 inlet | Less Level | LT-3005 fails low, pump runs dry | Pump cavitation/damage | LSL alarm, operator response | 12 (High) → 6 (Medium) | Confirm LSL alarm rationalization per Section 8.2 |

---

### 10.2 Sample Risk Matrix

| Severity ↓ / Likelihood → | 1 (Rare) | 2 (Unlikely) | 3 (Possible) | 4 (Likely) | 5 (Frequent) |
|---|---|---|---|---|---|
| 5 (Catastrophic) | 5 | 10 | 15 | 20 | 25 |
| 4 (Major) | 4 | 8 | 12 | 16 | 20 |
| 3 (Moderate) | 3 | 6 | 9 | 12 | 15 |
| 2 (Minor) | 2 | 4 | 6 | 8 | 10 |
| 1 (Negligible) | 1 | 2 | 3 | 4 | 5 |

*Low (1–5, green) — acceptable. Medium (6–11, yellow) — ALARP, monitor. High (12–25, red) — action required.*

---

### 10.3 Sample OSHA PSM 14-Element Checklist (Excerpt)

| Element | Status | Cross-Reference |
|---|---|---|
| Process Safety Information | Complete | Companion Line List, Mechanical, Instrumentation guides |
| Process Hazard Analysis | HAZOP complete, LOPA in progress | Section 3, Calc Sheet 9.1 |
| Mechanical Integrity | Inspection program established | Companion Mechanical Datasheet guide, Section 4.2 |
| Management of Change | Procedure in place | Section 7.2, Case Study (Section 13) |
| Incident Investigation | Procedure in place | Section 7.3 |
| Emergency Planning and Response | Firewater sized, ERP drafted | Section 5.3/8.3, Calc Sheet 9.4 |

---

### 10.4 Sample MOC Form Excerpt

| Field | Entry |
|---|---|
| MOC No. | MOC-2026-0142 |
| Description of change | Temporary bypass of PSHH interlock during K-101 vibration investigation |
| Technical basis / PHA review | **Required before implementation** — not to be treated as routine |
| Safety review sign-off | Process Safety Engineer, Operations Manager |
| Time limit (if temporary) | 72 hours maximum, with mandatory reversion tracking |
| Reversion confirmed | — |

---

## 11. Practical Design Checklist

- [ ] HAZOP performed against the current P&ID revision, with every finding risk-ranked and safeguards explicitly credited — see Calc Sheet 9.1
- [ ] Any High-risk-band or new-SIF HAZOP finding escalated to a full LOPA (companion Process Philosophies guide)
- [ ] Facility siting (occupied buildings, control room) checked against a blast/fire/toxic consequence distance, not just qualitative judgment — see Calc Sheet 9.2
- [ ] AIV screening performed at every pressure let-down/high-velocity location, with Level 2 assessment triggered per the risk band — see Calc Sheet 9.3
- [ ] Firewater system sized against the actual design fire case and required duration, with storage capacity explicitly verified — see Calc Sheet 9.4
- [ ] Every SIF's achieved PFD verified against its required SIL (companion Process Philosophies guide's LOPA), including sensor, logic solver, AND final element contributions and dynamic response time — see Calc Sheet 9.5
- [ ] Inherently safer design opportunities (eliminate/substitute/moderate/simplify) explicitly considered before finalizing added-on protective systems
- [ ] MOC procedure requires review and sign-off **before** implementation, including for temporary/emergency changes, with a mandatory reversion tracking mechanism
- [ ] Incident investigation procedure defined, including root cause analysis methodology and a lessons-learned dissemination step
- [ ] All 14 OSHA PSM elements (or equivalent international framework) explicitly addressed and cross-referenced to the relevant companion guide/discipline

---

## 12. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Occupied building found within blast exclusion distance during a later siting review | Facility siting check performed qualitatively rather than with an actual consequence distance calculation | Perform an explicit blast/fire/toxic distance check for every occupied building — see Calc Sheet 9.2 |
| Small-bore fitting fatigue failure at a pressure let-down point | AIV risk never screened at that specific location | Screen every high-velocity/pressure let-down location explicitly, not just the locations that "look" high-risk by inspection — see Calc Sheet 9.3 |
| Firewater system found inadequate during an audit or real fire event | Storage/supply sized against an outdated or incomplete design fire case | Explicitly verify firewater demand and storage against the current design fire case — see Calc Sheet 9.4 |
| SIF found non-compliant despite "passing" sensor PFD calculation | Final element (valve) PFD and dynamic response time never checked, only the sensor subsystem | Verify the complete SIF (sensor + logic solver + final element), including dynamic response time, not just one subsystem — see Calc Sheet 9.5 and companion Dynamic Simulation guide |
| Safety interlock inadvertently bypassed and left disabled | Temporary/emergency change made without MOC review under time pressure | Enforce MOC review for all changes, including temporary/emergency ones, with mandatory reversion tracking — see Case Study, Section 13 |

---

## 13. Case Study — Unauthorized Bypass Removes a Safety Interlock Without MOC Review

> A composite, illustrative case study based on the type of finding commonly encountered during PSM compliance audits. Names, tag numbers, and figures are representative, not project-specific.

### 13.1 Background

The illustrative gas processing plant (this guide's running example) experienced an unexpected high-vibration trip on K-101 during operations. The maintenance and operations teams, under pressure to restore production quickly, began an investigation that required repeatedly restarting the compressor to observe the vibration signature under load — but the high-high pressure safety interlock (the same SIF whose sensor subsystem PFD was verified in this guide's Calc Sheet 9.5) was tripping the unit before the team could gather sufficient data at the operating conditions they needed to observe.

A senior operator, experienced but working outside the formal MOC process under the pressure of a production-impacting investigation, instructed the instrument technician to install a temporary jumper across the pressure transmitter signal to prevent the interlock from tripping during the test runs — reasoning (informally, without documented review) that the vibration monitoring system would itself protect the machine, and that the bypass was "obviously temporary" and would be removed once the investigation concluded.

### 13.2 Problem Identified

The bypass was never formally logged, no MOC was raised, and no time-limited reversion tracking (Section 10.4's MOC form field) was established. The vibration investigation concluded within a few days and the immediate mechanical issue was resolved, but the **jumper was never removed** — it was physically difficult to notice during a routine visual panel check, and no one on the following shifts knew it existed, since it had never entered any tracked system.

The gap was discovered **weeks later**, during a routine PSM compliance audit that included physically verifying a sample of safety-critical instrument loops against their as-designed configuration — the auditor found the high-high pressure trip's transmitter signal path did not match the P&ID and traced it to the still-installed jumper.

### 13.3 Investigation & Root Cause Analysis

A formal incident investigation (Section 7.3) was conducted, treating this as a significant near-miss (the plant had been operating for weeks without one of two independent layers of overpressure protection functioning as designed, though PSV-101 — the mechanical relief valve credited in this guide's Calc Sheet 9.1 — remained in place and functional throughout). The RCA identified that the underlying overpressure risk during this window was elevated, though not to an unacceptable level given PSV-101's continued availability — consistent with Calc Sheet 9.1's finding that the mechanical PSV alone still provides meaningful risk reduction, just not the full mitigated risk level the design basis assumed with both layers active.

### 13.4 Root Cause

Two compounding root causes were identified:
1. **Time pressure led to an informal decision to bypass a safety interlock without MOC review** — the operator's reasoning (temporary, and covered by another protection layer) was a genuine safety judgment, but it was made unilaterally, without the cross-functional review (process safety engineering, instrumentation, operations management) that MOC exists specifically to provide, and without the documentation that would have ensured the bypass was tracked and reversed.
2. **No physical or systematic control caught an undocumented bypass** for weeks — there was no independent verification step (e.g., a shift-change checklist item specifically confirming safety-critical bypass status, or a bypass management system logging and time-limiting all interlock overrides) that would have caught the gap before a dedicated compliance audit happened to sample this specific loop.

### 13.5 Resolution

- The jumper was removed and the interlock's normal function was confirmed restored.
- A formal **bypass management system** was implemented, requiring every safety interlock bypass (planned or emergency) to be logged with an automatic maximum duration, a named accountable owner, and an automatic escalation/alarm if the bypass exceeds its authorized duration without a documented extension.
- MOC training was reinforced specifically for the scenario of "temporary" or "emergency" changes, explicitly addressing the false assumption that urgency justifies skipping MOC review — the MOC procedure was clarified to state that expedited (not skipped) MOC review is available for genuine emergencies, with a documented fast-track approval path rather than an informal bypass of the process entirely.

### 13.6 Outcome

- No actual overpressure event occurred during the gap period, and PSV-101 remained available as a mechanical backstop throughout — but the finding was treated with the same seriousness as an actual loss-of-containment near-miss, given the systemic gap it revealed.
- The finding was documented and disseminated (Section 7.4) across the company's other facilities, prompting several to implement similar bypass management system upgrades proactively rather than waiting for their own compliance audit to find a similar gap.

### 13.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| Time pressure is one of the most common and dangerous drivers of informal, undocumented safety-critical changes | Provide a genuine, well-understood expedited MOC path for real emergencies, so urgency is never used as a justification for skipping review entirely |
| An undocumented bypass has no natural expiration and can persist indefinitely without a specific control designed to catch it | Implement a formal bypass management system with automatic time limits, named ownership, and escalation |
| A single remaining protection layer (PSV-101) reduced but did not eliminate the elevated risk during the gap period | Recognize that a documented "acceptable" mitigated risk level often depends on multiple layers being simultaneously available — losing even one layer, even temporarily, is a materially different risk state that deserves the same rigor as a permanent design change |
| A routine compliance audit, not a targeted investigation, is what actually caught this gap | Value routine, sampling-based compliance verification as a genuine safety control in its own right, not just an administrative/regulatory formality |

---

## 14. Reference Standards

- **API 520 / 521 / 537** — Relief device sizing, pressure-relieving and depressuring systems, flare details
- **OSHA 29 CFR 1910.119** — Process Safety Management of Highly Hazardous Chemicals
- **CCPS Guidelines** (AIChE Center for Chemical Process Safety) — LOPA, inherently safer design, and related process safety methodology
- **ISO 45001** — Occupational health and safety management systems
- **API RP 752 / 753** — Management of Hazards Associated with Location of Process Plant Buildings (onshore / portable buildings)
- **IEC 61508 / 61511** — Functional safety
- **NFPA 15 / NFPA 68** — Water spray fixed systems / explosion venting

---

*This guide is a practical study reference combining standard process safety methodology with worked sample calculations and lessons learned from real project and operational experience. All numeric examples are illustrative — always validate against project-specific hazard, reliability, and site data, and the current edition of the referenced codes and standards. This guide is the capstone companion to the Flare Network Design, Depressurization Calculation, Compressor Settle-Out Calculations, Line List Preparation, Instrumentation Process Datasheet Preparation, Mechanical Datasheet Preparation, P&ID/PEFS Development, Steady-State Simulation, Dynamic Simulation, and Process Philosophies study guides — process safety is the discipline that ties every one of those guides' individual outputs into a coherent, risk-managed whole, from design through operations.*
