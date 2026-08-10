# 📟 Instrumentation Process Datasheet Preparation — Practical Study Guide

> A field-oriented reference covering the core engineering topics in preparing instrument process datasheets — combining ISA/IEC/API standard methodology with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design**, **Depressurization Calculation**, **Compressor Settle-Out Calculations**, and **Line List Preparation** study guides — the instrument process datasheet is where those studies' process conditions become the sizing basis for the field instruments that measure and protect the system.

**Illustrative project used throughout this guide:** a control valve on a pump discharge line, an orifice flow meter on a liquid transfer line, a DP level transmitter on a closed vessel, and a PSV protecting the same vessel used in the companion Flare Network Design guide — used to work through control valve Cv sizing, flow meter beta ratio selection, transmitter range/turndown calculation, and PSV orifice sizing. All numbers below are worked sample calculations for study purposes — always replace with project-specific process data and vendor-confirmed performance data.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Purpose & Role of the Instrument Process Datasheet](#2-purpose--role-of-the-instrument-process-datasheet)
3. [Process Conditions & Fluid Properties](#3-process-conditions--fluid-properties)
4. [Instrument Type, Range & Turndown Selection](#4-instrument-type-range--turndown-selection)
5. [Accuracy & Performance Requirements](#5-accuracy--performance-requirements)
6. [Materials of Construction](#6-materials-of-construction)
7. [Connections, Signal Types & Standards](#7-connections-signal-types--standards)
8. [Safety & Compliance (SIL, Hazardous Area Certification)](#8-safety--compliance-sil-hazardous-area-certification)
9. [Integration with P&IDs, Line List, and Equipment Datasheets](#9-integration-with-pids-line-list-and-equipment-datasheets)
10. [Sample Calculation Sheets](#10-sample-calculation-sheets)
11. [Sample Datasheets](#11-sample-datasheets)
12. [Practical Design Checklist](#12-practical-design-checklist)
13. [Common Field Issues & Lessons Learned](#13-common-field-issues--lessons-learned)
14. [Case Study — Custody Transfer Flow Meter Rangeability Shortfall](#14-case-study--custody-transfer-flow-meter-rangeability-shortfall)
15. [Reference Standards](#15-reference-standards)

---

## 1. Design Basis & Assumptions

Instrument process datasheets are normally developed under a **"Instrument Design Basis / Philosophy"** document and populated field-by-field as process data matures — the datasheet is the handoff point between process engineering and instrument/vendor engineering, so its inputs must be traceable back to a controlled source (P&ID, line list, process simulation), not entered from memory or a "similar service" assumption.

### 1.1 Process & Instrument Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Service | Pump discharge control valve, flow metering, and vessel level control | Same pump/vessel system used in the companion Line List guide |
| Fluid | Light hydrocarbon liquid, ρ = 850 kg/m³ | SG = 0.85 |
| Normal flow (control valve) | 150 gpm | Design case for Cv sizing |
| Minimum flow (control valve) | 30 gpm | Turndown check case |
| Available pressure drop across control valve | 40 psi | At normal flow, from hydraulic model |
| Flow meter line size | 4-inch, Schedule 40 (ID = 4.026 in / 0.1023 m) | Orifice flow meter |
| Flow meter design flow | 200 m³/hr | Max flow case |
| Vessel level span (0–100%) | 2 m | Tap-to-tap distance |
| Level transmitter mounting offset below low tap | 0.8 m | Remote-mounted transmitter, wet leg |
| Fill fluid density (wet leg) | 900 kg/m³ | Silicone oil, typical |
| PSV design case | Fire case, same vessel as companion Flare Network Design guide | W = 40,373 lb/hr, T = 760 °R, MW = 44, k = 1.13 |
| PSV set pressure | 250 psig | — |

### 1.2 Codes & Standards / Methodology Basis
- **ISA-75.01.01 / IEC 60534** — control valve sizing
- **ISO 5167** — orifice plate flow measurement
- **ISA-RP31.1 / general DP level instrumentation practice** — level transmitter range calculation
- **API STD 520 Part I** — PSV orifice sizing
- **IEC 61508 / IEC 61511** — functional safety (SIL) for safety instrumented functions
- **IEC 60079 series / ATEX / IECEx / NEC (North America)** — hazardous area electrical certification
- Project **Instrument Design Basis** and **Instrument Index** — governs where stricter than generic code practice (e.g., house minimum turndown, mandatory HART, minimum SIL verification requirements)

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Control valve installed sizing margin | Select valve so design flow falls at 60–80% travel, not at (or near) 100% | Leaves margin for future capacity/turndown; confirm project philosophy |
| Control valve rangeability required | Design flow ÷ minimum flow, checked against valve's inherent rangeability (typically 30:1–50:1 for globe valves) | Section 10.1 |
| Orifice plate beta ratio (ISO 5167 recommended range) | 0.2–0.75 (corner taps) | Outside this range, accuracy/uncertainty degrades and standard discharge coefficient correlations may not apply |
| Orifice discharge coefficient, C | ≈0.61 (typical, corner taps, mid-beta range) — treat as illustrative; final value must come from ISO 5167 iterative calculation | Full ISO 5167 calc iterates C as a function of β, Reynolds number, and tap type |
| DP transmitter range basis | Zero-based unless elevation/suppression requires an elevated or suppressed zero | See Calc Sheet 10.3 |
| PSV accumulation | 10% (conventional PSV) | API 520 |
| SIL verification | Required for all safety instrumented functions (SIFs) identified in the project's SIL/LOPA study | Not just "high-consequence-looking" loops — must trace to the formal SIL study |
| Hazardous area classification | To be confirmed per project area classification drawing, not assumed generically | Governs certification requirement (ATEX/IECEx/NEC, zone/division, gas group, temperature class) |

> ⚠️ **Practical note:** Every field on an instrument process datasheet should be traceable to a specific source document (P&ID revision, line list entry, process simulation case, SIL study) — a datasheet field populated from "typical practice" without a traceable source is exactly the kind of gap that surfaces late, as illustrated in the Case Study (Section 14).

---

## 2. Purpose & Role of the Instrument Process Datasheet

### 2.1 What It Captures
The instrument process datasheet captures the **process requirements** for a specific instrument — control valves, flow meters, pressure/level/temperature transmitters, PSVs, and similar field devices — separating *what the process needs* (this datasheet) from *how a specific vendor's product delivers it* (the vendor's own mechanical/model-specific datasheet, developed later in procurement).

### 2.2 Why It Matters
- It is the **basis for vendor datasheets and procurement** — the process datasheet is issued as part of the inquiry package, and vendors respond with their specific model, trim, and construction details against the stated process requirements.
- It is the document where the design conditions established by process, relief, settle-out, and line list work (see the companion guides in this series) are **translated into an actionable instrument sizing requirement** — the same discipline of traceability that applies to the line list applies here.
- Errors or stale data on this datasheet propagate directly into an undersized/oversized valve, an inaccurate flow meter, or a PSV that doesn't actually protect the vessel it's attached to — see Section 13 and the Case Study for real consequences of this.

---

## 3. Process Conditions & Fluid Properties

### 3.1 Required Fields
- **Operating and design pressure/temperature** — normal, minimum, and maximum, sourced directly from the line list (companion guide) or the relevant process simulation case, not re-derived independently.
- **Flow rate** — normal, minimum, and maximum (or design) flow, since instrument sizing depends on the *range* of flow, not just a single design point (see Section 4.2 and the Case Study).
- **Density, viscosity, compressibility (Z-factor)** — at actual operating conditions, not standard conditions, unless the instrument specifically requires standard-condition data (e.g., some flow computers reference standard volume).

### 3.2 Practical Tip
Process conditions on an instrument datasheet should reflect the **full credible operating envelope**, not just the single normal/design point — a control valve or flow meter sized only against one flow rate can fail to perform adequately at the actual minimum or maximum flow the process will see, which is precisely the failure mode worked through in Calc Sheets 10.1–10.2 and the Case Study (Section 14).

---

## 4. Instrument Type, Range & Turndown Selection

### 4.1 Instrument Type Selection
Instrument type follows from the service and the required measurement/control function — e.g., globe control valve vs. ball control valve, orifice plate vs. Coriolis vs. ultrasonic flow meter, DP transmitter vs. radar level gauge — driven by fluid properties (viscosity, solids content, phase), required accuracy, and the range/turndown the service actually demands.

### 4.2 Range & Turndown
- **Range** is the span between the instrument's minimum and maximum reading (e.g., a pressure transmitter ranged 0–50 bar, a flow meter ranged 100–500 m³/h).
- **Turndown** (or rangeability) is the ratio between the maximum and minimum flow/measurement the instrument must accurately handle at its **required accuracy** — not just the ratio between its absolute physical limits.
- **Practical tip:** Always range the instrument against the full normal operating envelope (minimum to maximum credible flow/pressure), not just the single design point — an instrument that only "passes" at the design flow can still fail to deliver adequate accuracy/turndown at the process's actual minimum flow, exactly the gap worked through in Calc Sheet 10.2 and the Case Study.

---

## 5. Accuracy & Performance Requirements

### 5.1 Required Measurement Precision
- Accuracy requirements are service-driven — custody transfer or fiscal metering demands a much tighter accuracy specification (often ±0.5% or better) than a general process control loop (±1–2% is often adequate).
- Accuracy must be stated **at the actual required turndown**, since most instruments' accuracy specification degrades toward the low end of their range — a flow meter quoted at "±0.5% of rate" typically only holds that figure across a limited turndown band, with accuracy degrading (or specification shifting to "% of full scale") outside it.

### 5.2 Practical Tip
Always confirm whether a quoted accuracy is **"% of rate"** or **"% of full scale/span"** — these produce very different real-world uncertainty at low-flow conditions, and conflating the two is a common specification error that only becomes apparent once the vendor's actual performance curve is reviewed.

---

## 6. Materials of Construction

### 6.1 Wetted Parts, Body & Trim
Materials selection is linked directly to fluid corrosivity, temperature, and any sour service requirement — the same corrosion/erosion screening methodology covered in the companion Flow Assurance guide applies here (e.g., a CO₂/H₂S-rich stream that screens poorly for corrosion in a pipeline corrosion study should drive the same corrosion-resistant alloy or coating decision for wetted instrument parts).

### 6.2 Practical Tip
Instrument wetted-parts material selection is frequently specified generically ("316SS wetted parts" as a default) without cross-checking against the *specific* line's corrosion/sour-service basis on the line list — always pull the governing corrosion allowance/material class directly from the line list entry for the tapped line, not from a generic instrument standard default.

---

## 7. Connections, Signal Types & Standards

### 7.1 Process Connections
- **Flange rating** must match the piping class of the line the instrument is tapped into (per ASME B16.5, consistent with the companion Line List Preparation guide's piping class logic) — a mismatch here is the instrumentation-side equivalent of the flange rating case study in that guide.
- Root/manifold valve and impulse tubing material/rating must also match the line's piping class and service, not just the transmitter body itself.

### 7.2 Electrical Signal Types
| Signal Type | Typical Use |
|---|---|
| **4–20 mA (analog)** | Standard process variable transmission |
| **4–20 mA with HART** | Analog signal plus digital diagnostic/configuration overlay — now the default for most new transmitters |
| **Fieldbus (FOUNDATION Fieldbus, Profibus PA)** | Digital multi-variable/multi-device networks, used on some modern DCS architectures |
| **Discrete (dry contact / digital)** | On/off status, switches, some SIF final elements |

### 7.3 Practical Tip
Confirm the host DCS/SIS system's actual signal-type support and the project's standardization policy before defaulting to "4–20 mA HART" on every datasheet — some projects standardize on fieldbus for non-safety loops, and mixing signal types unnecessarily adds procurement and maintenance complexity.

---

## 8. Safety & Compliance (SIL, Hazardous Area Certification)

### 8.1 SIL Rating
- Instruments performing a **safety instrumented function (SIF)** — identified through the project's SIL/LOPA study — must be selected and verified against the required SIL level (SIL 1, 2, or 3, per IEC 61508/61511), including confirming the vendor's certified failure data (PFD, SFF) supports the target SIL when combined with the rest of the safety loop (sensor + logic solver + final element).
- **Practical tip:** A SIL rating on the datasheet must trace back to the formal SIL/LOPA study — do not assign SIL ratings by analogy to "similar" loops on a prior project without independent verification, since SIL requirements are scenario-specific.

### 8.2 Explosion-Proof / Hazardous Area Certification
- Certification (ATEX, IECEx, or NEC/CSA for North America) must match the **actual** area classification (zone/division, gas group, temperature class) from the project's area classification drawing — not a generic "explosion-proof" specification applied uniformly across the whole plant regardless of the specific area's classification.

---

## 9. Integration with P&IDs, Line List, and Equipment Datasheets

### 9.1 Source Documents
- **P&IDs** — establish the instrument's existence, tag number, and basic control/safety function.
- **Process simulations** — provide the flow/pressure/temperature envelope (normal, minimum, maximum) needed for sizing.
- **Line list** (companion guide) — confirms the design pressure/temperature, piping class, and corrosion allowance of the line the instrument is tapped into, which the instrument's connection rating and wetted-parts material must match.
- **Equipment datasheets** — confirm any equipment-side design basis the instrument depends on (e.g., a level transmitter's range depends on the vessel's actual tap locations from the vessel datasheet, not an assumed generic span).

### 9.2 Downstream Documents
- **Instrument index** — the master register of every instrument in the project (analogous to the line list for piping), tracking tag number, service, type, range, and status through procurement and construction.
- **Vendor inquiry / requisition package** — the process datasheet, once complete, is issued to vendors as the technical basis for their quotation and their own model-specific datasheet response.

> ⚠️ **Practical note:** Just as the companion Line List guide's Case Study showed a stale equipment datasheet revision failing to propagate into the line list, the same revision-control discipline applies here — any change to a P&ID, process simulation case, or line list entry that affects an instrument's process basis must trigger a controlled instrument datasheet revision, not an informal note.

---

## 10. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific process data and vendor-confirmed performance curves.

### 10.1 Calc Sheet 1 — Control Valve Cv Sizing & Turndown Check

**Given (from Section 1 basis):**
- Normal (design) flow, Q = 150 gpm
- Minimum flow, Q_min = 30 gpm
- Specific gravity, SG = 0.85
- Available pressure drop at design flow, ΔP = 40 psi (assume constant ΔP across the flow range for this simplified screening calc)

**Step 1 — Required Cv at design flow (ISA liquid sizing, non-choked, simplified):**
```
Cv = Q × √(SG / ΔP)
Cv = 150 × √(0.85 / 40)
Cv = 150 × √(0.02125)
Cv = 150 × 0.1458
Cv ≈ 21.9
```

**Step 2 — Required Cv at minimum flow:**
```
Cv_min = 30 × √(0.85 / 40) = 30 × 0.1458 ≈ 4.4
```

**Step 3 — Select a valve size (illustrative Cv table, equal-percentage globe valve):**
```
3-inch valve, full-open Cv ≈ 40 (typical, vendor-specific — confirm actual Cv curve)
At design flow: required Cv (21.9) / full-open Cv (40) ≈ 55% valve travel — within the preferred 60–80% band (Section 1.3), slightly low but acceptable; a 2.5-inch valve could also be evaluated for a better fit at design flow.
```

**Step 4 — Turndown / rangeability check:**
```
Required rangeability = Cv (design) / Cv (minimum) = 21.9 / 4.4 ≈ 5.0 : 1
Typical equal-percentage globe valve inherent rangeability ≈ 30:1–50:1
Required (5:1) ≪ Available (30:1–50:1)  →  PASS, with significant margin
```

**Result:** A 3-inch equal-percentage globe control valve is adequate for both the design flow (≈55% travel) and the minimum flow turndown requirement (5:1 required vs. 30:1+ available). 

> 📌 **Assumption check:** This simplified calc holds ΔP constant across the flow range — in a real system, ΔP available across the valve typically *increases* as flow decreases (since friction losses elsewhere in the line drop faster than the pump/system curve), which usually makes the low-flow case even less limiting than shown here. Always use the actual system curve (ΔP vs. flow) from the hydraulic model for the final sizing calculation, and always obtain the vendor's actual Cv-vs-travel curve rather than assuming a generic full-open Cv.

---

### 10.2 Calc Sheet 2 — Orifice Flow Meter Beta Ratio Selection (ISO 5167, Simplified)

**Given:**
- Pipe ID, D = 4.026 in = 0.1023 m
- Design (max) flow, Q = 200 m³/hr = 0.05556 m³/s
- Fluid density, ρ = 850 kg/m³
- Discharge coefficient, C ≈ 0.61 (illustrative, mid-beta-range approximation — see assumption note)
- Expansion factor, ε = 1 (incompressible liquid)

**Step 1 — First attempt: target a common "low-range" transmitter span, ΔP = 25 kPa (250 mbar):**
```
Q = C × (π/4) × (βD)² × √[2ΔP / (ρ(1−β⁴))]

Let K = C × (π/4) × D² = 0.61 × 0.7854 × (0.1023)² ≈ 0.00501
√(2ΔP/ρ) = √(2 × 25,000 / 850) = √58.82 ≈ 7.670

Q = K × β² × 7.670 / √(1−β⁴)
0.05556 = 0.00501 × 7.670 × β² / √(1−β⁴)
0.05556 = 0.03842 × β² / √(1−β⁴)
β² / √(1−β⁴) = 1.446
```
Solving iteratively: **β ≈ 0.907**

**Result (Step 1):** β ≈ 0.91 — this **exceeds** the ISO 5167 recommended maximum of 0.75 (Section 1.3). **FAIL** — an orifice plate at this beta ratio falls outside the standard's validated discharge coefficient correlation range and would produce unreliable, poorly-characterized flow measurement.

**Step 2 — Revise: increase the target transmitter span to ΔP = 150 kPa (1.5 bar) and re-solve:**
```
√(2ΔP/ρ) = √(2 × 150,000 / 850) = √352.9 ≈ 18.79
Q = 0.00501 × 18.79 × β² / √(1−β⁴)
0.05556 = 0.09414 × β² / √(1−β⁴)
β² / √(1−β⁴) = 0.590
```
Solving iteratively: **β ≈ 0.713**

**Result (Step 2):** β ≈ 0.71 — within the ISO 5167 recommended range (0.2–0.75). **PASS.**

**Step 3 — Orifice bore diameter:**
```
d = β × D = 0.713 × 0.1023 m ≈ 0.0729 m ≈ 72.9 mm (2.87 in)
```

**Result:** Specify the orifice plate with a bore diameter of **≈73 mm**, paired with a DP transmitter ranged to a full-scale differential pressure of **150 kPa (1.5 bar)** — the higher DP range was required to bring the beta ratio back within the standard's valid range at this flow rate and pipe size.

> 📌 **Assumption check:** This is a simplified screening calculation using a fixed discharge coefficient — the full ISO 5167 method iterates the discharge coefficient (C) as a function of β, Reynolds number, and tap type (corner, flange, or D–D/2 taps) simultaneously with the beta ratio itself. Always perform (or have the vendor/flow calculation software perform) the full iterative ISO 5167 calculation before finalizing bore diameter — this hand calc is a fast way to catch a beta-ratio-out-of-range problem early, exactly as shown here, not a substitute for the final certified calculation.

---

### 10.3 Calc Sheet 3 — DP Level Transmitter Range Calculation (Elevated Zero)

**Given (from Section 1 basis):**
- Vessel level span (0–100%), tap-to-tap distance = 2 m
- Transmitter mounted 0.8 m below the low tap
- Configuration: open/simple case — wet leg (or process fluid-filled impulse line) with fluid density ρ = 900 kg/m³ (fill fluid; illustrative — for a live process-fluid wet leg use the process density instead)

**Step 1 — Lower Range Value (LRV) — pressure at the transmitter when level = 0%:**
```
LRV = ρ × g × h_offset
LRV = 900 × 9.81 × 0.8
LRV = 7,063 Pa ≈ 7.06 kPa ≈ 0.0706 bar
```

**Step 2 — Upper Range Value (URV) — pressure at the transmitter when level = 100%:**
```
URV = ρ × g × (h_offset + span)
URV = 900 × 9.81 × (0.8 + 2.0)
URV = 900 × 9.81 × 2.8
URV = 24,721 Pa ≈ 24.72 kPa ≈ 0.247 bar
```

**Step 3 — Transmitter span:**
```
Span = URV − LRV = 0.247 − 0.0706 ≈ 0.176 bar (17.6 kPa)
```

**Result:** The transmitter must be configured with an **elevated zero** — ranged from **0.0706 bar (4 mA, 0% level) to 0.247 bar (20 mA, 100% level)** — not a naive 0-to-(ρgh) range starting at zero pressure, because the remote-mounted transmitter's own elevation below the low tap adds a constant offset pressure at every level.

> 📌 **Assumption check:** This example used a single fluid density throughout for simplicity (illustrating the elevated-zero *method*). A real closed-tank installation with a wet reference leg on the high side (vapor space) and a different fluid (or vapor) on the process side requires the full differential calculation: `DP = ρ_process × g × L − ρ_fill × g × H_reference`, accounting for both legs' densities independently — always confirm the actual leg configuration (wet/dry, fill fluid identity) before finalizing the range calculation, since getting the configuration wrong (e.g., assuming dry leg when the installation is actually wet) is a common and consequential specification error.

---

### 10.4 Calc Sheet 4 — PSV Orifice Sizing (API 520, Vapor Service)

**Given (from Section 1 basis, consistent with the companion Flare Network Design guide's fire-case example):**
- Required relieving mass flow, W = 40,373 lb/hr
- Relieving temperature, T = 760 °R
- Compressibility factor, Z = 0.9
- Molecular weight, M = 44
- Specific heat ratio, k = 1.13
- Set pressure = 250 psig; accumulation = 10% (Section 1.3)
- Discharge coefficient, Kd = 0.975 (typical certified vapor-service PSV)
- Backpressure correction, Kb = 1.0 (conventional valve, backpressure within allowable limits)
- Combination correction factor, Kc = 1.0 (no rupture disk installed)

**Step 1 — Relieving pressure (P1):**
```
P1 = (Set pressure × 1.10) + 14.7 = (250 × 1.10) + 14.7 = 275 + 14.7 = 289.7 psia
```

**Step 2 — Gas constant coefficient, C (API 520 formula, function of k):**
```
C = 520 × √[ k × (2/(k+1))^((k+1)/(k−1)) ]

(k+1)/(k−1) = 2.13/0.13 = 16.38
2/(k+1) = 2/2.13 = 0.9390
(0.9390)^16.38 ≈ 0.357
k × 0.357 = 1.13 × 0.357 = 0.4034
√0.4034 ≈ 0.635

C = 520 × 0.635 ≈ 330
```

**Step 3 — Required effective orifice area (API 520 critical/sonic flow formula):**
```
A = W × √(T×Z/M) / (C × Kd × P1 × Kb × Kc)

√(T×Z/M) = √(760 × 0.9 / 44) = √(15.545) ≈ 3.943

A = (40,373 × 3.943) / (330 × 0.975 × 289.7 × 1.0 × 1.0)
A = 159,231 / 93,212
A ≈ 1.708 in²
```

**Step 4 — Select standard API orifice designation:**
```
Standard orifice "K" = 1.287 in²  →  too small (< 1.708 in² required)
Standard orifice "L" = 1.838 in²  →  adequate (≥ 1.708 in² required)
```

**Result:** Required effective orifice area ≈ **1.708 in²** → select standard **API orifice "L" (1.838 in²)**. This value, along with the relieving conditions used to derive it, should be recorded on the PSV's instrument process datasheet as the basis for the vendor's mechanical selection and certified capacity confirmation.

> 📌 **Assumption check:** This is the same fire-case relief load used in the companion Flare Network Design guide (Calc Sheet 8.1) — the instrument process datasheet for a PSV should always cite its relieving flow/pressure basis back to that governing relief scenario calculation, not restate an independently-derived number, to keep the two documents consistent through revisions.

---

## 11. Sample Datasheets

### 11.1 Control Valve Process Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | FCV-1042 | — |
| **Service** | Pump discharge flow control, P-101 to V-200 | — |
| **Line No.** | 6"-P-1042-A1A-H | — (per companion Line List guide) |
| **Fluid** | Light hydrocarbon liquid, SG 0.85 | — |
| **Normal Flow** | 150 | gpm |
| **Minimum Flow** | 30 | gpm |
| **Maximum Flow** | 180 | gpm |
| **ΔP at Normal Flow** | 40 | psi |
| **Required Cv (normal flow)** | 21.9 (per Calc Sheet 10.1) | — |
| **Selected Valve Size / Type** | 3-in, equal-percentage globe | — |
| **Body Rating** | ASME Class 300 (per line piping class) | — |
| **Trim Material** | 316 SST, hardened | — |
| **Body Material** | WCC carbon steel | — |
| **Actuator Type** | Pneumatic spring-diaphragm, fail-closed | — |
| **Signal Type** | 4–20 mA HART | — |
| **Required Rangeability** | 5:1 (per Calc Sheet 10.1) | — |
| **SIL Requirement** | Not a SIF (BPCS control loop only) | — |

---

### 11.2 Flow Meter (Orifice) Process Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | FE/FT-2031 | — |
| **Service** | Liquid transfer metering | — |
| **Line Size** | 4-in, Sch 40 (ID 4.026 in) | — |
| **Design Flow (max)** | 200 | m³/hr |
| **Fluid Density** | 850 | kg/m³ |
| **Meter Type** | Orifice plate, corner taps | — |
| **Beta Ratio** | 0.713 (per Calc Sheet 10.2) | — |
| **Orifice Bore Diameter** | 72.9 | mm |
| **DP Transmitter Range** | 0–150 | kPa |
| **Discharge Coefficient (final, per ISO 5167 iteration)** | To be confirmed by vendor/flow calc software | — |
| **Accuracy Requirement** | ±1.0% of rate (process control; confirm if custody transfer applies) | — |
| **Material — Orifice Plate** | 316 SST | — |
| **Flange Rating** | ASME Class 300 (per line piping class) | — |
| **Signal Type** | 4–20 mA HART | — |

---

### 11.3 DP Level Transmitter Process Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | LT-3005 | — |
| **Service** | Vessel V-200 level | — |
| **Vessel Tap Span (0–100%)** | 2.0 | m |
| **Transmitter Mounting Offset** | 0.8 (below low tap) | m |
| **Leg Configuration** | Wet leg, fill fluid density 900 kg/m³ | — |
| **Lower Range Value (LRV)** | 0.0706 (per Calc Sheet 10.3) | bar |
| **Upper Range Value (URV)** | 0.247 (per Calc Sheet 10.3) | bar |
| **Span** | 0.176 | bar |
| **Accuracy** | ±0.075% of span | — |
| **Wetted Parts Material** | 316L SST (per line corrosion basis) | — |
| **Process Connection** | ½-in NPT, via 3-valve manifold | — |
| **Flange Rating (manifold/root valve)** | ASME Class 300 (per line piping class) | — |
| **SIL Requirement** | SIL 2 (per SIL/LOPA study — high level SIF) | — |
| **Hazardous Area Certification** | ATEX/IECEx, Zone 1, Gas Group IIA, T3 | — |
| **Signal Type** | 4–20 mA HART | — |

---

### 11.4 PSV Instrument Process Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | PSV-101 | — |
| **Service** | Vessel V-100 overpressure protection, fire case | — |
| **Set Pressure** | 250 | psig |
| **Accumulation** | 10 | % |
| **Relieving Pressure (P1)** | 289.7 (per Calc Sheet 10.4) | psia |
| **Relieving Temperature** | 760 (300) | °R (°F) |
| **Relieving Flow, W** | 40,373 | lb/hr |
| **Fluid** | Propane vapor, MW 44 | — |
| **Required Orifice Area** | 1.708 (per Calc Sheet 10.4) | in² |
| **Selected Orifice Designation** | L (1.838 in²) | — |
| **Backpressure (built-up)** | Confirm ≤10% of set pressure per header hydraulics (companion Flare Network guide) | — |
| **Body/Bonnet Material** | WCC carbon steel | — |
| **Applicable Standard** | API STD 520 Part I, ASME Section VIII | — |

---

## 12. Practical Design Checklist

- [ ] Instrument design basis and instrument index issued and approved (Section 1) before datasheet population begins
- [ ] Every process condition field traceable to a specific source document (P&ID revision, line list entry, process simulation case) — not entered generically
- [ ] Full operating envelope (minimum, normal, maximum) used for sizing, not just the single design point — see Calc Sheets 10.1–10.2
- [ ] Control valve Cv and rangeability checked at both design and minimum flow — see Calc Sheet 10.1
- [ ] Flow meter beta ratio (or equivalent sizing parameter) checked against the applicable standard's valid range — see Calc Sheet 10.2
- [ ] DP transmitter range calculated with correct elevated/suppressed zero logic for the actual leg configuration — see Calc Sheet 10.3
- [ ] PSV orifice sizing cross-referenced to the governing relief scenario calculation (not independently re-derived) — see Calc Sheet 10.4
- [ ] Materials of construction pulled from the actual line list corrosion/service basis for the tapped line, not a generic instrument standard default
- [ ] Flange rating and connection class matched to the tapped line's piping class (per companion Line List guide)
- [ ] SIL rating traced to the formal SIL/LOPA study for any safety instrumented function, not assigned by analogy
- [ ] Hazardous area certification matched to the actual area classification drawing for the instrument's installed location
- [ ] Signal type confirmed against host DCS/SIS support and project standardization policy
- [ ] Datasheets issued for vendor inquiry, and the instrument index updated to reflect issued status

---

## 13. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Flow meter accuracy poor at low flow / failed a custody transfer audit | Beta ratio sized only against the single design flow point, not checked against the actual full operating range | Check beta ratio (or equivalent) across the full expected flow range, not just the design point — see Calc Sheet 10.2 and Case Study, Section 14 |
| Control valve hunts/oscillates at low flow | Valve selected for adequate Cv at design flow without checking rangeability at minimum flow | Explicitly check rangeability (Cv_design/Cv_min vs. valve inherent rangeability) — Calc Sheet 10.1 |
| Level transmitter reading incorrect from day one of commissioning | Elevated/suppressed zero calculation omitted or leg configuration (wet/dry) assumed incorrectly | Always explicitly calculate LRV/URV for the actual as-built leg configuration — Calc Sheet 10.3 |
| Instrument wetted parts corroded faster than expected | Generic "316SS wetted parts" default applied without cross-checking the actual line's corrosion/sour-service basis | Pull materials basis directly from the line list entry for the tapped line, not a generic instrument standard |
| SIL-rated loop found non-compliant during functional safety audit | SIL rating assigned by analogy to a "similar" loop on a prior project rather than traced to this project's SIL/LOPA study | Trace every SIL rating to the formal, project-specific SIL/LOPA study before issuing the datasheet |
| PSV orifice size inconsistent between the flare system study and the instrument datasheet | Relieving flow re-derived independently on the instrument datasheet rather than cited from the governing relief study | Cross-reference PSV sizing inputs directly to the governing relief calculation (companion Flare Network Design guide) — Calc Sheet 10.4 |

---

## 14. Case Study — Custody Transfer Flow Meter Rangeability Shortfall

> A composite, illustrative case study based on the type of finding commonly encountered during commissioning and early operation of custody transfer / fiscal metering skids. Names, tag numbers, and figures are representative, not project-specific.

### 14.1 Background

A liquid transfer skid included an orifice-type custody transfer flow meter (FE/FT-2031, the same tag used in this guide's illustrative datasheet) sized during detailed engineering against the process design basis's single stated "design flow" of 200 m³/hr — the same value used in Calc Sheet 10.2 of this guide. The datasheet and subsequent orifice bore calculation used this single flow point, resulting in a beta ratio of 0.71 at a 150 kPa transmitter span, which passed the ISO 5167 range check comfortably at the time.

### 14.2 Problem Identified

Once the facility began commercial operation, actual transfer rates varied far more widely than the single design-flow point had implied — the terminal's actual operating envelope ranged from approximately 40 m³/hr (low-demand periods) up to the 200 m³/hr design maximum. At the low end of this actual range, the orifice's differential pressure output fell to a small fraction of the transmitter's 150 kPa span, well below the meter run's effective accurate turndown (a standard orifice meter's usable accurate turndown against a single fixed DP range is typically only about 3:1–5:1, since DP falls with the *square* of flow).

The custody transfer accuracy audit (required periodically for fiscal metering) found the meter's demonstrated uncertainty at low flow rates **exceeded the ±0.5% custody transfer requirement by a significant margin** — the meter was accurate at high flow but effectively unusable for billing purposes during low-demand periods, forcing the terminal to fall back on a less accurate secondary estimation method for a portion of transferred volume.

### 14.3 Investigation & Recalculation

The instrumentation team reviewed the original process datasheet and found it had captured only the single 200 m³/hr design flow — the actual commercial operating envelope (40–200 m³/hr) had never been incorporated, despite being available in the terminal's commercial operations plan at the time the datasheet was prepared.

Reapplying the Calc Sheet 10.2 methodology at the low end of the actual range (40 m³/hr) against the existing fixed 150 kPa transmitter span confirmed the DP at 40 m³/hr fell to only about 4% of full span — far below the level at which the orifice meter's standard uncertainty specification remains valid, consistent with the poor field-observed accuracy.

### 14.4 Root Cause

Two compounding root causes were identified:
1. **Process datasheet captured only a single design flow point**, not the full commercial operating envelope, even though that envelope was available from the commercial/operations planning documentation at the time of instrument sizing — a scope gap between process engineering (who provided the single design case) and the commercial/operations team (who held the actual expected range).
2. **No turndown/rangeability check was performed against a fixed-orifice, single-range meter design** — the datasheet preparer sized the beta ratio correctly against ISO 5167 for the stated design flow (Calc Sheet 10.2 "PASS" result) but did not separately check whether a single fixed-bore orifice could deliver adequate *accuracy* across the actual full flow range, which is a materially different question from whether the beta ratio itself is within the standard's valid geometric range.

### 14.5 Resolution

- The single orifice meter run was **replaced with a dual-run configuration** (a smaller-bore orifice run for low flows, a larger-bore run for high flows, with automatic run-switching logic) — a common solution for custody transfer applications with a wide flow turndown requirement, since it is often more cost-effective than a single high-turndown meter technology (e.g., Coriolis) for this line size and service.
- The instrument design basis document was updated to require the **full commercial/operating flow envelope** (not just a single design point) be explicitly requested from operations/commercial planning for any custody transfer or fiscal metering application, before sizing begins.
- A rangeability/turndown check step (distinct from the beta-ratio range check) was added to the instrument datasheet preparation checklist specifically for fixed-geometry meter types (orifice, Venturi) — confirming the *accuracy* turndown, not just the geometric beta-ratio validity, is checked against the actual full operating range.

### 14.6 Outcome

- The dual-run meter replacement required a capital expenditure and a scheduled tie-in outage, but restored full custody transfer accuracy compliance across the actual operating range.
- The finding was documented as a corporate lessons-learned item: for any custody transfer or fiscal metering application, the instrument process datasheet must capture the **full actual operating envelope**, sourced explicitly from commercial/operations planning, not just the process design case — and fixed-geometry meter technologies must be explicitly checked for *accuracy* turndown across that envelope, separate from the standard's geometric validity check.

### 14.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A single "design flow" data point is not sufficient for sizing a custody transfer / fiscal metering instrument | Explicitly request and document the full actual operating envelope from commercial/operations planning for any fiscal metering application |
| Passing the ISO 5167 beta-ratio range check confirms geometric validity, not accuracy across the full flow range | Add a distinct accuracy/turndown check for fixed-geometry meter types, separate from the beta-ratio range check — Calc Sheet 10.2 |
| Standard orifice meters have inherently limited accurate turndown (DP falls with the square of flow) | For services with wide flow turndown requirements, evaluate dual-run configurations or alternative meter technologies (Coriolis, ultrasonic) at the datasheet preparation stage, not after a field accuracy failure |
| Commercial/operations data availability gaps between departments can silently limit engineering scope | Formalize the data request for full operating envelope as a mandatory input to the instrument design basis, not an informal or assumed data source |

---

## 15. Reference Standards

- **ISA-75.01.01 / IEC 60534** — Control valve sizing equations
- **ISO 5167** (Parts 1–4) — Measurement of fluid flow by means of pressure differential devices (orifice plates, nozzles, Venturi tubes)
- **API STD 520 Part I** — Sizing, Selection, and Installation of Pressure-relieving Devices
- **IEC 61508** — Functional safety of electrical/electronic/programmable electronic safety-related systems
- **IEC 61511** — Functional safety — Safety instrumented systems for the process industry sector
- **IEC 60079 series / ATEX Directive / IECEx** — Explosive atmospheres — equipment certification
- **ASME B16.5** — Pipe Flanges and Flanged Fittings (instrument connection/flange rating basis)

---

*This guide is a practical study reference combining standard instrument process datasheet preparation methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific process data, the current edition of the referenced standards, and vendor-confirmed performance data. This guide should be read alongside the companion Flare Network Design, Depressurization Calculation, Compressor Settle-Out Calculations, and Line List Preparation study guides, since the process conditions those studies establish are exactly what this datasheet is built to carry forward into instrument sizing and procurement.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
