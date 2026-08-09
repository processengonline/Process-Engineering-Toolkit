# 🔧 Mechanical Datasheet Preparation — Practical Study Guide

> A field-oriented reference covering the core engineering topics in preparing mechanical equipment datasheets — combining ASME Section VIII, TEMA, and API mechanical equipment standards with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Flare Network Design**, **Depressurization Calculation**, **Compressor Settle-Out Calculations**, **Line List Preparation**, and **Instrumentation Process Datasheet Preparation** study guides — the mechanical datasheet is where the design pressures/temperatures those studies establish become the actual pressure-boundary design (shell thickness, nozzle reinforcement, MAWP) of the equipment itself.

**Illustrative project used throughout this guide:** the same suction vessel (V-100) and pump (P-101) used in the companion Line List and Instrumentation guides — used to work through shell/head thickness calculation, corroded-condition MAWP verification, nozzle reinforcement (area replacement method), and hydrotest pressure determination. All numbers below are worked sample calculations for study purposes — always replace with project-specific process data and the current edition of the referenced codes.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Purpose & Role of the Mechanical Datasheet](#2-purpose--role-of-the-mechanical-datasheet)
3. [Design Conditions — Design Pressure, Temperature, MAWP & MDMT](#3-design-conditions--design-pressure-temperature-mawp--mdmt)
4. [Materials of Construction & Corrosion Allowance](#4-materials-of-construction--corrosion-allowance)
5. [Geometry, Nozzle Schedule & Reinforcement](#5-geometry-nozzle-schedule--reinforcement)
6. [Code & Standard Compliance](#6-code--standard-compliance)
7. [Fabrication, NDE, PWHT & Testing Requirements](#7-fabrication-nde-pwht--testing-requirements)
8. [Rotating Equipment-Specific Considerations](#8-rotating-equipment-specific-considerations)
9. [Integration with Process Datasheets, Line List, and P&IDs](#9-integration-with-process-datasheets-line-list-and-pids)
10. [Sample Calculation Sheets](#10-sample-calculation-sheets)
11. [Sample Datasheets](#11-sample-datasheets)
12. [Practical Design Checklist](#12-practical-design-checklist)
13. [Common Field Issues & Lessons Learned](#13-common-field-issues--lessons-learned)
14. [Case Study — Nozzle Reinforcement Omission Found During Fabrication](#14-case-study--nozzle-reinforcement-omission-found-during-fabrication)
15. [Reference Standards](#15-reference-standards)

---

## 1. Design Basis & Assumptions

Mechanical datasheets are normally developed under a **"Mechanical Design Basis / Equipment Specification"** and populated once process conditions are confirmed on the line list and process datasheets (companion guides) — the mechanical datasheet is the point where those process conditions become an actual pressure-boundary design, so every input must trace back to a controlled source, not an assumed "typical" value.

### 1.1 Equipment & Process Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Equipment | V-100, horizontal suction drum | Same vessel referenced in companion Line List and Instrumentation guides |
| Inside diameter | 1,500 mm (59.06 in) | — |
| Shell length (tan-to-tan) | 4,500 mm | — |
| Design pressure | 150 psig | Consistent with companion Line List guide, Section 1.1 |
| Design temperature | 200 °F (93.3 °C) | — |
| MDMT | −20 °F (−28.9 °C) | Site minimum design ambient, consistent with companion guides |
| Shell/head material | SA-516 Grade 70 | Allowable stress, S ≈ 20,000 psi at design temp (confirm actual value from ASME Section II-D) |
| Corrosion allowance | 0.125 in (3 mm) | Consistent with companion guides' corrosion allowance basis |
| Joint efficiency, E | 1.0 (full radiography) | Confirm actual NDE extent per Section 7 |
| Head type | 2:1 semi-ellipsoidal | — |
| Governing nozzle (example) | 6-in, Schedule 40, shell nozzle | Used for reinforcement calc, Calc Sheet 10.4 |
| Associated pump | P-101 A/B, centrifugal | Same pump referenced in companion Line List/Instrumentation guides |

### 1.2 Codes & Standards / Methodology Basis
- **ASME BPVC Section VIII, Division 1** — pressure vessel design (shell/head thickness, nozzle reinforcement, MAWP, hydrotest)
- **ASME Section II, Part D** — allowable stress values by material and temperature
- **TEMA** (Tubular Exchanger Manufacturers Association) — shell-and-tube heat exchanger mechanical standards, used alongside ASME VIII for the pressure boundary
- **API STD 610** — Centrifugal Pumps for Petroleum, Petrochemical and Natural Gas Industries
- **API STD 617** — Axial and Centrifugal Compressors (referenced from the companion Compressor Settle-Out guide for casing MAWP basis)
- **ASME B16.5** — flange ratings for nozzles (consistent with companion Line List guide's piping class logic)
- Project **Mechanical Design Basis / Equipment Specification** — governs where stricter than code minimums (e.g., house minimum corrosion allowance, mandatory full radiography, minimum nozzle NPS for reinforcement calculation)

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Corrosion allowance basis | Applied to shell, heads, and nozzle necks equally unless service dictates otherwise | Confirm whether internals/nozzles need a different allowance than the shell |
| Joint efficiency | 1.0 (full RT) assumed for this example | Actual value depends on the project's NDE extent decision — see Section 7; full RT is not automatic and has a cost/schedule trade-off against a lower joint efficiency (thicker shell) |
| Allowable stress source | ASME Section II-D, at design temperature | Never assume a stress value from a prior project without confirming the current code edition's value for the actual material/temperature |
| Mill/plate tolerance | Not applied as a percentage (unlike pipe) — plate is typically ordered to nominal or per plate specification minus tolerance | Confirm actual plate procurement tolerance with materials engineering; differs from the pipe mill-tolerance logic used in the companion Line List guide |
| Nozzle reinforcement method | Area replacement method (ASME VIII UG-37) | Alternative: finite element analysis for complex/highly loaded nozzles — confirm project policy for when FEA is required instead of the standard area-replacement hand method |
| Hydrotest pressure basis | 1.3 × MAWP × (Sa/S), per ASME VIII UG-99(b) | Confirm whether pneumatic testing alternative is used instead (different factor, additional precautions) |
| MDMT / impact test exemption | Per ASME VIII Div. 1 UCS-66, analogous methodology to the companion Line List guide's ASME B31.3 approach for piping | Vessel and piping use different code sections (UCS-66 vs. B31.3 Fig. 323.2.2) even though the underlying stress-ratio-credit concept is similar |

> ⚠️ **Practical note:** The joint efficiency assumption (Section 1.3) has a direct, compounding effect on required thickness — a lower joint efficiency (less radiography) increases required thickness, which increases weight, which can cascade into foundation/structural/lifting requirements. This trade-off should be made deliberately at the mechanical design basis stage, not defaulted to "full RT" or "spot RT" without a cost/schedule comparison.

---

## 2. Purpose & Role of the Mechanical Datasheet

### 2.1 What It Captures
The mechanical datasheet captures the **pressure-boundary and mechanical design requirements** for a specific piece of equipment — pressure vessels, heat exchangers, pumps, compressors, and similar — translating the process conditions (from the process datasheet/line list) into the actual physical design: shell/head thickness, nozzle schedule and reinforcement, materials, MAWP, MDMT, and applicable code/testing requirements.

### 2.2 Why It Matters
- It is the **basis for the fabricator's/vendor's detailed mechanical design and fabrication drawings** — for a pressure vessel, the datasheet plus the project's general notes/specification is what the fabricator uses to prepare the U-1 data report package and shop drawings.
- It is the document where **process conditions become a code-compliant physical design** — the same design pressure that governs a line list entry (companion guide) also governs the vessel's shell thickness, and the two must remain consistent through revisions.
- Errors or stale data on this datasheet propagate directly into an under-designed pressure boundary, missed nozzle reinforcement, or an MAWP that doesn't actually match the nameplate — see Section 13 and the Case Study for real consequences of this.

---

## 3. Design Conditions — Design Pressure, Temperature, MAWP & MDMT

### 3.1 Design Pressure & Temperature
- Sourced directly from the process datasheet/line list (companion guides) — the mechanical datasheet should **cite**, not independently re-derive, the governing design pressure/temperature case (e.g., a pump dead-head case, a fire case, or a settle-out case per the companion Compressor Settle-Out guide).
- **MAWP** (Maximum Allowable Working Pressure) is the pressure the vessel is actually designed and rated to — it is often *higher* than the stated design pressure once actual selected plate thickness (rounded up to a standard/available thickness) is applied, as shown in Calc Sheet 10.3.

### 3.2 MDMT
- Minimum Design Metal Temperature is checked against the site's minimum ambient/process temperature using the ASME VIII Div. 1 **UCS-66** impact-test exemption curves and stress-ratio reduction credit — methodologically analogous to (but a distinct code reference from) the companion Line List guide's B31.3 piping approach.
- **Practical tip:** Just as with piping, the stress-ratio reduction credit (UCS-66) is frequently under-utilized — a vessel that appears to need impact-tested material at first glance can often be exempted once the actual design-stress-to-allowable-stress ratio is calculated.

---

## 4. Materials of Construction & Corrosion Allowance

### 4.1 Material Selection
- Driven by fluid corrosivity/sour service (cross-check against the companion Flow Assurance guide's corrosion/erosion screening for the connected process), design temperature range (governs both high-temperature creep considerations and low-temperature MDMT/impact-test needs), and cost.
- Allowable stress values must be pulled from **ASME Section II, Part D** at the actual design temperature — allowable stress decreases with increasing temperature for most materials, so using an ambient-temperature stress value for a hot-service vessel is non-conservative.

### 4.2 Corrosion Allowance
- Applied as extra wall thickness beyond the pressure-design-required minimum, consumed gradually over the equipment's service life; the **corroded-condition MAWP** (thickness minus corrosion allowance) is what should be checked against the design pressure for end-of-life adequacy, not just the new/nominal-thickness MAWP (Calc Sheet 10.3).
- **Practical tip:** Corrosion allowance should be confirmed against the actual expected corrosion mechanism and rate for the specific service (see the companion Flow Assurance guide's CO₂ corrosion rate screening methodology) rather than defaulted to a generic company-standard value for every vessel regardless of service severity.

---

## 5. Geometry, Nozzle Schedule & Reinforcement

### 5.1 Vessel Geometry
- Inside diameter, tan-to-tan length, head type (ellipsoidal, hemispherical, torispherical) — all driven by the process volume/residence-time requirement (see the companion Flare Network Design guide's KOD sizing methodology as an example of how process requirements translate into vessel geometry) and by fabrication/transport practicalities (e.g., maximum shippable diameter).

### 5.2 Nozzle Schedule
- Every nozzle (process connections, instrument connections, manways, drains, vents) must be listed with size, rating, projection, orientation, and service — the nozzle schedule is a direct input to both the vessel's general arrangement drawing and to the instrument/piping tie-in design (companion guides).

### 5.3 Nozzle Reinforcement
- Every opening in the pressure boundary removes load-carrying shell material — the **area replacement method** (ASME VIII UG-37) confirms that the material removed is adequately replaced by excess thickness in the shell, excess thickness in the nozzle neck, and/or a reinforcing pad, within a defined limit of reinforcement around the opening.
- **Practical tip:** Nozzle reinforcement is one of the most common omissions/errors on mechanical datasheets and shop drawings, particularly for nozzles added or resized late in the design (e.g., an instrument nozzle added after the original vessel calc package was issued) — see Calc Sheet 10.4 and the Case Study (Section 14) for a full worked example and a real-world consequence.

---

## 6. Code & Standard Compliance

### 6.1 Pressure Vessels
**ASME BPVC Section VIII, Division 1** (or Division 2 for higher-pressure/optimized designs) governs shell/head design, nozzle reinforcement, MAWP determination, and the U-1 data report/nameplate requirements.

### 6.2 Heat Exchangers
Shell-and-tube exchangers are designed to **ASME Section VIII** for the pressure boundary, with **TEMA** providing mechanical standards for tube bundle construction, baffle spacing, tube-to-tubesheet joints, and classifying service severity (TEMA Class R — severe/refinery service, C — moderate/commercial, B — chemical process service).

### 6.3 Rotating Equipment
- **API STD 610** — centrifugal pumps (mechanical seal, bearing, baseplate, and NPSH margin requirements beyond the basic hydraulic performance)
- **API STD 617** — centrifugal/axial compressors (see the companion Compressor Settle-Out guide for how settle-out pressure feeds directly into this standard's casing MAWP requirement)
- **API STD 674 / 675 / 676** — reciprocating, metering, and rotary pumps, as applicable to the specific equipment type

---

## 7. Fabrication, NDE, PWHT & Testing Requirements

### 7.1 NDE (Non-Destructive Examination) & Joint Efficiency
- The extent of radiography (full RT, spot RT, or none) directly sets the **joint efficiency (E)** used in the thickness calculations (Section 1.3, Calc Sheets 10.1–10.2) — this is a deliberate design/cost trade-off, not just an inspection checkbox, since a lower joint efficiency requires thicker (heavier, costlier) plate to compensate.

### 7.2 PWHT (Post-Weld Heat Treatment)
- Required based on material, thickness, and service per ASME VIII (and any project specification override — e.g., mandatory PWHT for sour service regardless of the code-minimum thickness threshold, consistent with the companion Flow Assurance and Line List guides' sour-service override logic).

### 7.3 Hydrotest / Pneumatic Test
- Hydrotest pressure is calculated per **ASME VIII UG-99(b)**: 1.3 × MAWP × (allowable stress at test temperature ÷ allowable stress at design temperature) — see Calc Sheet 10.5 for a worked example.
- Pneumatic testing (where hydrotest is impractical, e.g., vessels that cannot tolerate the weight/contamination of water) uses a different factor and requires additional safety precautions per code — confirm which method the project specifies before finalizing the datasheet's test requirement field.

---

## 8. Rotating Equipment-Specific Considerations

### 8.1 Pumps (API 610)
- Beyond the process datasheet's flow/head/NPSH requirements (which feed the vendor's hydraulic selection), the **mechanical datasheet** captures casing design pressure/temperature (including the dead-head case, per the companion Line List guide's Calc Sheet 9.1 methodology), materials, seal plan, baseplate, and coupling requirements.
- **NPSH margin** (NPSH available minus NPSH required) is a mechanical/process interface item — confirm the project's minimum margin policy (commonly 3 ft or 1 m minimum, sometimes more for high-energy or high-suction-specific-speed pumps) is reflected on both the process and mechanical datasheets consistently.

### 8.2 Compressors (API 617)
- Casing MAWP must accommodate the **settle-out pressure** (see the companion Compressor Settle-Out Calculations guide), not just normal discharge pressure — this is one of the clearest examples in this whole series of a process/relief-type study result becoming a direct mechanical design input.

---

## 9. Integration with Process Datasheets, Line List, and P&IDs

### 9.1 Source Documents
- **Process datasheets** (companion Instrumentation guide's process-side equivalent for equipment) — provide the design pressure/temperature, flow, and service basis.
- **Line list** (companion guide) — confirms the design pressure/temperature and piping class of connected lines, which nozzle ratings must match.
- **Relief and settle-out studies** (companion Flare Network, Depressurization, and Compressor Settle-Out guides) — establish governing design-pressure cases that the mechanical datasheet must reflect, sometimes overriding a simpler "normal operating pressure plus margin" basis.

### 9.2 Downstream Documents
- **Equipment list / mechanical equipment index** — the master register analogous to the line list and instrument index, tracking every piece of equipment through procurement and construction.
- **Vendor inquiry / requisition package** — the mechanical datasheet, once complete, is issued to fabricators/vendors as the technical basis for their detailed mechanical design, fabrication, and (for pressure vessels) the code data report package.

> ⚠️ **Practical note:** The same revision-control discipline emphasized in the companion Line List and Instrumentation guides applies here — any change to a relief study, settle-out study, or process datasheet that affects a piece of equipment's design pressure/temperature must trigger a controlled mechanical datasheet revision, not an informal note to the vendor.

---

## 10. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against the current edition of ASME Section VIII and project-specific material/process data.

### 10.1 Calc Sheet 1 — Shell Thickness (ASME VIII Div. 1, UG-27, Circumferential/Hoop Stress)

**Given:**
- Design pressure, P = 150 psig
- Inside radius, R = 29.53 in (1,500 mm ID ÷ 2)
- Allowable stress, S = 20,000 psi
- Joint efficiency, E = 1.0
- Corrosion allowance, CA = 0.125 in

**Step 1 — Required thickness (thin cylindrical shell formula):**
```
t = (P × R) / (S × E − 0.6 × P) + CA
t = (150 × 29.53) / (20,000 × 1.0 − 0.6 × 150) + 0.125
t = 4,429.5 / (20,000 − 90) + 0.125
t = 4,429.5 / 19,910 + 0.125
t = 0.2225 + 0.125
t ≈ 0.3475 in
```

**Step 2 — Select standard plate thickness:**
```
Next standard plate thickness ≥ 0.3475 in → 3/8 in (0.375 in)
```

**Result:** Shell plate thickness = **3/8 in (9.5 mm)**, providing margin over the calculated minimum (0.3475 in).

> 📌 **Assumption check:** The joint efficiency (E = 1.0) assumes full radiographic examination of all shell longitudinal and circumferential seams — if the project specification instead calls for spot RT (E = 0.85), the required thickness increases to approximately 0.408 in, which could push the selection to the next standard plate thickness and add cost/weight. Confirm the actual NDE extent (Section 7.1) before finalizing this calculation.

---

### 10.2 Calc Sheet 2 — Head Thickness (2:1 Semi-Ellipsoidal Head, UG-32)

**Given:**
- Design pressure, P = 150 psig
- Inside diameter, D = 59.06 in
- Allowable stress, S = 20,000 psi
- Joint efficiency, E = 1.0
- Corrosion allowance, CA = 0.125 in

**Step 1 — Required thickness (2:1 ellipsoidal head formula):**
```
t = (P × D) / (2 × S × E − 0.2 × P) + CA
t = (150 × 59.06) / (2 × 20,000 × 1.0 − 0.2 × 150) + 0.125
t = 8,859 / (40,000 − 30) + 0.125
t = 8,859 / 39,970 + 0.125
t = 0.2216 + 0.125
t ≈ 0.3466 in
```

**Step 2 — Select standard plate thickness:**
```
Next standard plate thickness ≥ 0.3466 in → 3/8 in (0.375 in), matching the shell plate selection
```

**Result:** Head plate thickness = **3/8 in (9.5 mm)** — conveniently matching the shell thickness from Calc Sheet 10.1, simplifying procurement (single plate thickness for the whole pressure boundary).

---

### 10.3 Calc Sheet 3 — Corroded-Condition MAWP Verification

**Given (from Calc Sheet 10.1):**
- Selected (nominal) shell thickness = 0.375 in
- Corrosion allowance, CA = 0.125 in
- Allowable stress, S = 20,000 psi; Joint efficiency, E = 1.0
- Inside radius, R = 29.53 in

**Step 1 — Corroded (end-of-life) thickness:**
```
t_corroded = t_nominal − CA = 0.375 − 0.125 = 0.250 in
```

**Step 2 — MAWP at corroded thickness (rearranged UG-27 formula):**
```
MAWP = (S × E × t_corroded) / (R + 0.6 × t_corroded)
MAWP = (20,000 × 1.0 × 0.250) / (29.53 + 0.6 × 0.250)
MAWP = 5,000 / (29.53 + 0.150)
MAWP = 5,000 / 29.68
MAWP ≈ 168.5 psig
```

**Step 3 — Compare to design pressure:**
```
Corroded MAWP (168.5 psig) > Design pressure (150 psig)  →  PASS, with ~18.5 psig margin
```

**Result:** Even at fully corroded (end-of-corrosion-allowance) condition, the vessel's MAWP (168.5 psig) remains above the design pressure (150 psig) — the vessel remains adequately rated throughout its intended service life. This corroded-condition MAWP (not the higher new/nominal-thickness value) is the figure that should be used for any future re-rate or fitness-for-service evaluation as the vessel approaches its corrosion allowance limit.

> 📌 **Assumption check:** This calculation assumes uniform, general corrosion consuming the allowance evenly — localized corrosion (pitting, erosion at nozzles) can create a local thin spot well before the general corrosion allowance is nominally consumed. Periodic thickness inspection (UT surveys) at known high-risk locations (nozzles, liquid/vapor interface line, low points) should verify actual condition rather than relying solely on this uniform-corrosion assumption over the vessel's life.

---

### 10.4 Calc Sheet 4 — Nozzle Reinforcement (Area Replacement Method, UG-37)

**Given:**
- Nozzle: 6-in NPS, Schedule 40 (OD = 6.625 in, nominal wall = 0.280 in), corrosion allowance = 0.125 in
- Shell (corroded): t = 0.250 in (from Calc Sheet 10.3)
- Design pressure, P = 150 psig; S = 20,000 psi; E = 1.0

**Step 1 — Nozzle finished opening diameter, d:**
```
d = Nozzle OD − 2 × nominal wall = 6.625 − 2 × 0.280 = 6.065 in
```

**Step 2 — Required shell thickness for pressure alone (no CA), t_r:**
```
t_r = (P × R) / (S × E − 0.6 × P) = 0.2225 in   (from Calc Sheet 10.1, Step 1, before adding CA)
```

**Step 3 — Required reinforcement area:**
```
A_required = d × t_r × F   (F = 1.0 for a radial nozzle, circumferential stress governs)
A_required = 6.065 × 0.2225 × 1.0
A_required ≈ 1.350 in²
```

**Step 4 — Area available in the shell (excess thickness beyond pressure requirement):**
```
A1 = d × (E1×t_shell,corroded − F×t_r)
A1 = 6.065 × (1.0 × 0.250 − 1.0 × 0.2225)
A1 = 6.065 × 0.0275
A1 ≈ 0.167 in²
```

**Step 5 — Area available in the nozzle wall (excess thickness beyond the nozzle's own pressure requirement):**
```
Nozzle corroded wall = 0.280 − 0.125 = 0.155 in
Nozzle required thickness, t_rn = (P × r_nozzle)/(S×E − 0.6×P), r_nozzle = 6.065/2 = 3.0325 in
t_rn = (150 × 3.0325)/19,910 ≈ 0.0229 in

Nozzle excess = 0.155 − 0.0229 = 0.1321 in
Limit of reinforcement (projection) = min(2.5×t_shell,corroded, 2.5×t_nozzle,corroded) = min(0.625, 0.3875) = 0.3875 in

A2 = 2 × (limit of reinforcement) × (nozzle excess)
A2 = 2 × 0.3875 × 0.1321
A2 ≈ 0.102 in²
```

**Step 6 — Total available area vs. required:**
```
A_available = A1 + A2 = 0.167 + 0.102 = 0.269 in²
A_required = 1.350 in²

A_available (0.269 in²) ≪ A_required (1.350 in²)  →  FAIL — reinforcing pad required
```

**Step 7 — Size a reinforcing pad to make up the shortfall:**
```
Additional area needed, A3 = A_required − A_available = 1.350 − 0.269 = 1.081 in²

Select pad thickness, t_pad = 0.375 in (same as shell plate, for procurement simplicity)
Required pad width, w = A3 / t_pad = 1.081 / 0.375 ≈ 2.88 in

Pad outside diameter = Nozzle OD + 2×w = 6.625 + 2×2.88 = 6.625 + 5.76 ≈ 12.39 in
→ Round up to standard pad OD: 13 in
```

**Result:** The 6-inch nozzle **requires a reinforcing pad** — specify a **13-in OD × 3/8-in thick** reinforcing pad, matching the shell material.

> 📌 **Assumption check:** This worked example deliberately shows a FAIL result to illustrate why nozzle reinforcement cannot be assumed adequate "by inspection" for anything but the smallest, lowest-pressure openings — always run the actual UG-37 calculation (or equivalent software) for every nozzle, especially larger-diameter process nozzles on thinner-walled vessels, and see the Case Study (Section 14) for what happens when this step is skipped or performed late.

---

### 10.5 Calc Sheet 5 — Hydrotest Pressure (ASME VIII UG-99(b))

**Given:**
- Nominal shell thickness = 0.375 in (Calc Sheet 10.1); R = 29.53 in; S = 20,000 psi; E = 1.0
- Allowable stress at test temperature (ambient), Sa ≈ 20,000 psi (illustrative — confirm actual value from ASME II-D at the actual test temperature)
- Allowable stress at design temperature, S = 20,000 psi (from Section 1.1)

**Step 1 — MAWP at new, nominal (non-corroded) thickness:**
```
MAWP_new = (S × E × t_nominal) / (R + 0.6 × t_nominal)
MAWP_new = (20,000 × 1.0 × 0.375) / (29.53 + 0.6 × 0.375)
MAWP_new = 7,500 / (29.53 + 0.225)
MAWP_new = 7,500 / 29.755
MAWP_new ≈ 252.0 psig
```

**Step 2 — Hydrotest pressure (UG-99(b)):**
```
P_test = 1.3 × MAWP_new × (Sa / S)
P_test = 1.3 × 252.0 × (20,000/20,000)
P_test = 1.3 × 252.0
P_test ≈ 327.6 psig
```

**Result:** Required hydrotest pressure ≈ **328 psig** (round up per project rounding convention, e.g., to 330 psig). This value, along with the test medium (water) and any test temperature/brittle-fracture precautions, should be recorded on the mechanical datasheet as the fabricator's test requirement.

> 📌 **Assumption check:** This example used equal Sa and S for simplicity — for materials where allowable stress at ambient (test) temperature differs meaningfully from the allowable stress at design temperature, the Sa/S ratio can materially shift the required test pressure. Always pull both values from the current ASME Section II-D table at the actual respective temperatures, not assume they are equal.

---

## 11. Sample Datasheets

### 11.1 Pressure Vessel Mechanical Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Equipment Tag** | V-100 | — |
| **Service** | Pump Suction Drum | — |
| **Orientation** | Horizontal | — |
| **Inside Diameter** | 1,500 (59.06) | mm (in) |
| **Tan-to-Tan Length** | 4,500 | mm |
| **Design Pressure** | 150 (Full vacuum to +150) | psig |
| **Design Temperature** | 200 (−20 min) | °F |
| **MDMT** | −20 (per UCS-66 screening) | °F |
| **Calculated Corroded MAWP** | 168.5 (per Calc Sheet 10.3) | psig |
| **Hydrotest Pressure** | 328 (per Calc Sheet 10.5) | psig |
| **Shell/Head Material** | SA-516 Gr. 70 | — |
| **Shell Thickness (nominal)** | 3/8 (9.5) (per Calc Sheet 10.1) | in (mm) |
| **Head Thickness (nominal)** | 3/8 (9.5) (per Calc Sheet 10.2) | in (mm) |
| **Head Type** | 2:1 Semi-Ellipsoidal | — |
| **Corrosion Allowance** | 0.125 (3) | in (mm) |
| **Joint Efficiency** | 1.0 (Full RT) | — |
| **PWHT** | Not required (confirm per thickness/service) | — |
| **Design Code** | ASME BPVC Section VIII, Div. 1 | — |
| **Nozzles** | See Nozzle Schedule, Section 11.2 | — |
| **Internals** | Inlet deflector, demister pad (if vapor disengagement required) | — |
| **Insulation** | None (process temperature does not require it) | — |
| **Painting/Coating** | Per project coating specification | — |

---

### 11.2 Nozzle Schedule

| Nozzle No. | Service | Size (NPS) | Rating | Projection | Orientation | Reinforcement |
|---|---|---|---|---|---|---|
| N1 | Inlet | 8 | ASME Cl. 150 | 200 mm | Top, 0° | Confirm per UG-37 (larger nozzle than worked example — recalculate) |
| N2 | Outlet (to pump) | 6 | ASME Cl. 150 | 200 mm | Bottom, 180° | **Pad required — 13-in OD × 3/8-in (per Calc Sheet 10.4)** |
| N3 | PSV connection | 3 | ASME Cl. 300 | 250 mm | Top, 90° | Confirm per UG-37 (smaller nozzle — check if self-reinforced) |
| N4 | Level instrument (upper tap) | 2 | ASME Cl. 300 | 150 mm | Side, 270° | Self-reinforced (small bore, typical) |
| N5 | Level instrument (lower tap) | 2 | ASME Cl. 300 | 150 mm | Side, 270° | Self-reinforced (small bore, typical) |
| N6 | Drain | 2 | ASME Cl. 300 | 150 mm | Bottom, 180° | Self-reinforced (small bore, typical) |
| MW1 | Manway | 20 | ASME Cl. 150 | 100 mm | Side, 90° | Confirm per UG-37 (large opening — always calculate, never assume self-reinforced) |

*(Illustrative — every nozzle on a real vessel requires its own UG-37 reinforcement check; only N2 was fully worked in this guide's Calc Sheet 10.4.)*

---

### 11.3 Shell & Tube Heat Exchanger Mechanical Datasheet (Secondary Example)

| Parameter | Value | Unit |
|---|---|---|
| **Equipment Tag** | E-101 | — |
| **Service** | Product Cooler | — |
| **TEMA Type** | AES | — |
| **TEMA Class** | B (chemical process service) | — |
| **Shell Design Pressure / Temperature** | 250 / 300 | psig / °F |
| **Tube Design Pressure / Temperature** | 150 / 250 | psig / °F |
| **Shell Material** | SA-516 Gr. 70 | — |
| **Tube Material** | SA-179 (CS) or 316SS (confirm per corrosion basis) | — |
| **Tube OD / BWG / Length** | 0.75 / 14 / 6,000 | in / — / mm |
| **Number of Tubes** | 210 | — |
| **Corrosion Allowance (Shell / Tube)** | 0.125 / 0.049 | in |
| **Design Code** | ASME BPVC Section VIII, Div. 1 + TEMA | — |

---

### 11.4 Centrifugal Pump Mechanical Datasheet (Secondary Example)

| Parameter | Value | Unit |
|---|---|---|
| **Equipment Tag** | P-101 A/B | — |
| **Service** | V-100 to V-200 transfer | — |
| **Type** | Centrifugal, API 610 (OH2) | — |
| **Casing Design Pressure** | 310 (per companion Line List guide, Calc Sheet 9.1) | psig |
| **Casing Design Temperature** | 200 | °F |
| **Casing Material** | WCC (carbon steel) | — |
| **Rated Flow / Head** | 150 gpm / 650 ft | — |
| **NPSH Required (vendor)** | 12 | ft |
| **NPSH Available (process)** | 18 | ft |
| **NPSH Margin** | 6 (≥ project minimum of 3–5 ft) | ft |
| **Seal Plan** | API Plan 11 | — |
| **Coupling** | Spacer type, per API 610 | — |
| **Baseplate** | Fabricated steel, per API 610 | — |
| **Design Code** | API STD 610 | — |

---

## 12. Practical Design Checklist

- [ ] Mechanical design basis issued and approved (Section 1) before shell/nozzle calculations begin
- [ ] Design pressure/temperature cited directly from the governing process datasheet/line list/relief study — not independently re-derived
- [ ] Shell and head thickness calculated per ASME VIII UG-27/UG-32 — see Calc Sheets 10.1–10.2
- [ ] Joint efficiency confirmed against the actual planned NDE extent (Section 7.1), not assumed
- [ ] Corroded-condition MAWP verified against design pressure for full service-life adequacy — see Calc Sheet 10.3
- [ ] **Every** nozzle (not just the largest) checked for reinforcement adequacy per UG-37, including instrument and small-bore connections that may still require a check — see Calc Sheet 10.4
- [ ] Reinforcing pads sized and specified wherever the area-replacement check fails
- [ ] MDMT / impact-test exemption screened per ASME VIII UCS-66 methodology
- [ ] Hydrotest (or pneumatic test) pressure calculated per UG-99(b) — see Calc Sheet 10.5
- [ ] Materials of construction cross-checked against the connected line's corrosion/sour-service basis (companion Line List and Flow Assurance guides)
- [ ] Nozzle ratings matched to the connected piping class (companion Line List guide)
- [ ] For rotating equipment: casing design pressure confirmed against the governing case (dead-head, settle-out — companion Line List and Compressor Settle-Out guides), not just normal operating pressure
- [ ] Datasheets issued for vendor/fabricator inquiry, and the mechanical equipment index updated to reflect issued status

---

## 13. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Reinforcing pad missing on an as-fabricated vessel, caught at shop inspection | Nozzle reinforcement calc not performed (or performed against outdated nozzle size) for a nozzle added/resized after the original calc package | Recalculate reinforcement for every nozzle change, however late in the design — see Case Study, Section 14 |
| Vessel found under-rated after a downstream process change increased design pressure | Mechanical datasheet not linked to a revision-trigger from the process datasheet/line list | Formally link mechanical datasheet design pressure fields to the source process document revision, per the same discipline established in the companion Line List guide |
| Unnecessary cost from over-conservative joint efficiency/full RT applied without a trade-off study | Joint efficiency defaulted to "full RT" without comparing cost/schedule against a spot-RT, thicker-plate alternative | Perform the joint-efficiency trade-off explicitly at the mechanical design basis stage, not by default |
| Vessel corroded-condition MAWP found inadequate during a life-extension/re-rate study | Original design only checked new/nominal-thickness MAWP against design pressure, not the corroded-condition MAWP | Always calculate and record corroded-condition MAWP (Calc Sheet 10.3) as part of the original design package, not only during a later re-rate study |
| Pump casing found inadequate for an actual trip event | Casing design pressure based on normal discharge pressure only, not the dead-head/settle-out governing case | Cross-reference casing design pressure to the companion Line List guide's dead-head calc and/or the Compressor Settle-Out guide's methodology, as applicable |

---

## 14. Case Study — Nozzle Reinforcement Omission Found During Fabrication

> A composite, illustrative case study based on the type of finding commonly encountered during pressure vessel fabrication and shop inspection. Names, tag numbers, and figures are representative, not project-specific.

### 14.1 Background

The illustrative vessel from this guide (V-100) was originally designed with a 4-inch outlet nozzle (N2) at FEED, which — being a smaller opening relative to the shell thickness — passed the UG-37 area-replacement check without requiring a reinforcing pad, and the original calculation package and datasheet reflected this "no pad required" result.

During detailed engineering, the process team increased the outlet line size from 4-inch to 6-inch (the size used throughout this guide's worked examples) to accommodate a higher revised flow rate identified during hydraulic re-verification — consistent with exactly the kind of line list revision discussed in the companion Line List Preparation guide. The **line list and process datasheet were correctly updated** to reflect the 6-inch nozzle size. However, the **vessel mechanical datasheet's nozzle schedule was updated to show 6-inch**, but the **underlying UG-37 reinforcement calculation was not rerun** — the design team updated the nozzle schedule table entry directly without re-triggering the calculation package that had originally justified "no pad required" for the smaller 4-inch opening.

### 14.2 Problem Identified

The fabricator's shop drawing, prepared from the (visually updated but calculation-unverified) mechanical datasheet, showed the 6-inch nozzle installed **without a reinforcing pad**, consistent with the datasheet's carried-over "no pad required" note. This was caught during the fabricator's **mandatory internal design review** (a standard fabricator QA step, cross-checking shop drawings against the code calculation package) before welding began — the reviewer could not locate a valid UG-37 calculation covering the 6-inch opening and flagged it.

### 14.3 Investigation & Recalculation

The vessel design engineer reran the UG-37 calculation for the 6-inch nozzle using the methodology in this guide's Calc Sheet 10.4, confirming the result shown in that calc sheet: required reinforcement area ≈1.350 in² against only ≈0.269 in² available without a pad — a clear **FAIL**, requiring the 13-in OD × 3/8-in pad calculated in Section 10.4.

### 14.4 Root Cause

Two compounding root causes were identified:
1. **Datasheet field updated without a corresponding calculation update** — the nozzle schedule table (a datasheet field) was changed to reflect the new nozzle size, but there was no procedural trigger requiring the UG-37 calculation package to be reopened and rerun whenever a nozzle size field changed on the datasheet.
2. **No independent cross-check between the datasheet's nozzle schedule and the calculation package's covered nozzle list** prior to issuing the datasheet for fabrication — the mismatch existed for the full duration between the datasheet revision and the fabricator's own internal QA catch.

### 14.5 Resolution

- The nozzle was re-specified with the required 13-in OD × 3/8-in reinforcing pad (per Calc Sheet 10.4), and the calculation package was formally updated and reissued alongside the datasheet.
- Because the finding was caught during the fabricator's design review — **before** welding/fabrication began — no rework of already-fabricated material was required, though the finding did cause a short delay while the calculation and revised drawings were processed.
- The project's document control procedure was updated to require: **any change to a nozzle size, rating, or location on the mechanical datasheet's nozzle schedule must be accompanied by a re-issued (or explicitly re-confirmed) UG-37 calculation for that nozzle**, cross-referenced by revision number, before the datasheet can be issued for fabrication.

### 14.6 Outcome

- The gap was caught at the earliest practical point (fabricator design review, pre-welding) rather than during shop inspection of completed welds or, worse, during service — but it was still treated as a near-miss worth a formal lessons-learned review, since a less rigorous fabricator (or a project without a mandatory independent design review step) might not have caught it before fabrication proceeded.
- The finding was documented as a corporate lessons-learned item, reinforcing the same principle established in the companion Line List and Instrumentation guides' case studies: **a datasheet field change is not the same as a design verification** — every datasheet field that depends on an underlying calculation must have that calculation re-triggered and re-confirmed whenever the field changes, not just the table entry itself.

### 14.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| Updating a datasheet table entry (nozzle size) does not automatically update the underlying engineering calculation that justified the original entry | Require an explicit, cross-referenced calculation re-issue for any nozzle schedule change, before the datasheet can be issued for fabrication |
| Reinforcement conclusions ("no pad required") from an earlier design iteration can silently become invalid after a seemingly minor field change | Treat every "no pad required" or similar qualitative conclusion as tied to a specific input revision — re-verify explicitly whenever any input to it changes |
| An independent design review step (fabricator or third-party) can catch a gap that internal document control missed | Value and preserve independent review steps in the schedule — do not treat them as a formality to be expedited under schedule pressure |
| The same "field changed without re-triggering the underlying calculation" failure mode recurs across disciplines (line list, instrument datasheet, and now mechanical datasheet) | Apply a consistent, company-wide document control principle across all datasheet types: every calculated field must be traceable to a specific, current calculation revision |

---

## 15. Reference Standards

- **ASME BPVC Section VIII, Division 1** — Rules for Construction of Pressure Vessels (UG-27 shell thickness, UG-32 head thickness, UG-37 nozzle reinforcement, UG-99 hydrotest, UCS-66 MDMT)
- **ASME BPVC Section II, Part D** — Properties (allowable stress values by material and temperature)
- **TEMA** — Standards of the Tubular Exchanger Manufacturers Association
- **API STD 610** — Centrifugal Pumps for Petroleum, Petrochemical and Natural Gas Industries
- **API STD 617** — Axial and Centrifugal Compressors and Expander-compressors
- **ASME B16.5** — Pipe Flanges and Flanged Fittings

---

*This guide is a practical study reference combining standard mechanical datasheet preparation methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against the current edition of the referenced codes, project-specific material data, and vendor-confirmed performance data. This guide should be read alongside the companion Flare Network Design, Depressurization Calculation, Compressor Settle-Out Calculations, Line List Preparation, and Instrumentation Process Datasheet Preparation study guides, since the design conditions those studies establish are exactly what this datasheet is built to carry forward into the equipment's actual pressure-boundary design.*
