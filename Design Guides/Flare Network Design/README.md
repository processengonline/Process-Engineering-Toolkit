# 🔥 Flare Network Design — Practical Study Guide

> A field-oriented reference covering the core engineering topics in flare network design — combining API/EPA theory with worked sample calculations, sample process datasheets, and design-basis assumptions drawn from real project execution (process design, hydraulic sizing, mechanical/safety review, and commissioning).

**Illustrative project used throughout this guide:** a single PSV protecting a propane storage/process vessel, exposed to an external pool-fire scenario, relieving through a horizontal knock-out drum to an elevated steam-assisted flare tip. All numbers below are worked sample calculations for study purposes — always replace with project-specific data.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Gas Characterization](#2-gas-characterization)
3. [Flare System Hydraulics](#3-flare-system-hydraulics)
4. [Knock-Out Drum (KOD) Design](#4-knock-out-drum-kod-design)
5. [Flare Tip & Pilot Design](#5-flare-tip--pilot-design)
6. [Radiation & Safety Analysis](#6-radiation--safety-analysis)
7. [Environmental & Regulatory Compliance](#7-environmental--regulatory-compliance)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Datasheets](#9-sample-datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Brownfield LPG Sphere Relief Tie-In](#12-case-study--brownfield-lpg-sphere-relief-tie-in)
13. [Reference Standards](#13-reference-standards)

---

## 1. Design Basis & Assumptions

Every calculation sheet in Section 8 traces back to this basis. In real projects, this section is issued as a standalone **"Flare System Design Basis"** document and frozen before detailed engineering starts — changing it mid-project is one of the biggest sources of rework.

### 1.1 Site & Ambient Conditions
| Parameter | Value | Notes |
|---|---|---|
| Ambient temperature (design max) | 45 °C (113 °F) | Governs relieving temperature credit, dispersion modeling |
| Ambient temperature (min) | 5 °C (41 °F) | Governs low-temperature material selection, viscosity checks |
| Design wind speed | 5 m/s (base case) & 10 m/s (sensitivity) | Used in flame tilt / radiation footprint runs |
| Elevation / atmospheric pressure | Sea level, 101.325 kPa | Adjust for inland/high-altitude sites |
| Solar radiation background | 1.0 kW/m² (per API 521) | Added to flare-only radiation total |

### 1.2 Codes & Standards Basis
- API RP 521 (7th Ed.) — relief load, hydraulics, radiation methodology
- API STD 537 — flare tip & assist system design
- API STD 520 Parts I & II — PSV sizing
- ISO 23251 — used where contractually required in lieu of/alongside API 521
- 40 CFR 60.18 — combustion efficiency, minimum heating value, exit velocity
- Energy Institute AIV Guidelines (2nd Ed.) — vibration screening
- Company/client engineering specification (governs where stricter than the above, e.g., house K-factors, minimum pilot count)

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| PSV backpressure allowable | 10% of set pressure (conventional PSV) | API 520 Part I |
| Fire case environmental factor, F | 1.0 (bare vessel) / 0.3 (with fireproofing) | API 521 Table on environmental factors |
| Adequate drainage & firefighting credit | Assumed available unless stated otherwise | Reduces fire case factor — confirm with site HSE |
| KOD droplet removal size | 300–600 µm | Flare service; finer cut not justified for flare KODs |
| KOD liquid residence time | 20–30 min (min. to alarm response) | Company philosophy; confirm with Ops |
| Minimum LHV for flare gas | 300 Btu/scf (unassisted) / 200 Btu/scf (assisted) | 40 CFR 60.18 |
| Maximum allowable radiation at grade (personnel, escape route) | 4.73 kW/m² (1500 Btu/hr·ft²) | API 521 |
| Maximum radiation at equipment (no personnel) | 9.46 kW/m² | API 521 |
| Simultaneous relief grouping | By common initiating cause only | API 521 Section 4 |
| Corrosion allowance (KOD, CS) | 3 mm | Project material spec |
| Design life | 25 years | Project spec |

> ⚠️ **Practical note:** Always issue the design basis for client/PMC approval *before* running detailed hydraulics — changing K-factors or the fire-case environmental factor after headers are sized is one of the most common (and expensive) causes of rework on brownfield flare projects.

---

## 2. Gas Characterization

### 2.1 Flow Rate & Variability
- **Normal relief** — routine venting/blowdown; sizes minimum sustained tip turndown.
- **Maximum relief (design case)** — fire, power failure, blocked outlet, control valve failure; governs header/sub-header diameter.
- **Staged/rundown relief** — sequential PSV lifting during upset; needs dynamic simulation for complex multi-source headers.

**Practical experience:** Build a PSV relief load summary (Section 9.1) as the single source of truth before touching hydraulics. Identify the governing scenario **per header segment**, not globally — a common error is applying one global governing case across the whole network.

### 2.2 Composition & Heating Value
- MW, specific gravity, and LHV drive flare tip selection, combustion efficiency compliance, and smoke potential.
- Use a *flow-weighted average composition* across scenarios, not just the largest-flow case — a small hydrogen-rich stream can dominate combustion behavior.

### 2.3 Two-Phase Relief Scenarios
- Use the **Omega method (API 520 Appendix)** or **HEM** for two-phase PSV sizing — don't default to vapor-only sizing for flashing streams.
- Two-phase lines carry much higher density than vapor-only lines — this changes header sizing significantly and often justifies a dedicated sub-header to the KOD.

---

## 3. Flare System Hydraulics

### 3.1 Header & Sub-Header Sizing
Sizing sequence used in practice:
1. Build routing sketch (tie-ins, lengths, elevations).
2. Run hydraulic calc (friction + elevation loss, Mach check) from each PSV to the tip.
3. Check simultaneous relief cases per the cause-and-effect matrix — not just the single largest contributor.
4. Iterate pipe size until **every** PSV tie-in backpressure is within its allowable limit — the tightest constraint is often a low-set-pressure PSV far from the tip, not the largest PSV.

### 3.2 Mach Number & Velocity Limits
| Parameter | Typical Limit | Why |
|---|---|---|
| Mach number, header (design) | ≤ 0.7, ≤ 0.5 preferred | Avoid choking, excess ΔP |
| Mach number, short PSV tailpipe | up to 1.0 (sonic) acceptable | Short-duration transient only |
| Velocity (AIV screening) | Per Energy Institute likelihood ranking | Prevent acoustic-induced vibration fatigue |

### 3.3 Simultaneous Relief Events
- Group by **common initiating cause** (power failure, cooling water failure, fire zone) — only sources triggered by the same event are summed.
- Fire zone cases: only PSVs on equipment within the same fire zone (commonly a 232 m² / 2,500 ft² radius per API 521) are counted together.
- Build a cause-and-effect matrix first — treating every PSV's individual worst case as simultaneous massively over-sizes the header.

---

## 4. Knock-Out Drum (KOD) Design

### 4.1 Liquid Separation — Souders-Brown Equation
```
V_max = K_SB × √[(ρ_L − ρ_V) / ρ_V]
```
`K_SB` depends on target droplet size (300–600 µm typical for flare KODs — coarser than process separators, since over-designing to a fine cut like 150 µm gives an oversized drum with little real benefit in flare service).

### 4.2 Residence Time & Settling Velocity
- Liquid space sized on residence time (20–30 min typical, per site philosophy) for operator response before carryover.
- Always cross-check against the **maximum liquid inventory/slug scenario** — residence time alone can under-size the drum if a slug governs rather than continuous flow.

### 4.3 Horizontal vs. Vertical KODs
| Type | Pros | Cons | Typical Use |
|---|---|---|---|
| Horizontal | Better for high liquid loading, longer settling length, easier debottlenecking | Larger footprint | Refineries, high carryover risk |
| Vertical | Smaller footprint | Limited holdup, less efficient at high flow | Offshore/FPSO, space-constrained sites |

---

## 5. Flare Tip & Pilot Design

### 5.1 Types of Flare Tips
| Type | Mechanism | Best For | Trade-off |
|---|---|---|---|
| Utility (basic) | No assist | Low-value, intermittent, remote flares | Poor smoke control at high loads |
| Steam-assist | Steam-induced air entrainment | Refineries/petrochemical (steam available) | Over-steaming quenches flame/steam plume |
| Air-assist | Forced-draft blower | Sites without reliable steam | Blower power & maintenance |
| Gas-assist | Sonic gas jets induce air entrainment | Remote/unmanned sites | Continuous fuel gas consumption |

**Practical tip:** Steam ratio should be tuned during commissioning against real (not just design-case) relief loads — over-injection is one of the most common field operability complaints.

### 5.2 Pilot Systems
- Continuously lit, monitored per **EPA 40 CFR 60.18**; requires reliable ignition (flame-front generator or high-energy igniter) and flame detection (thermocouple or UV/IR) alarmed to the control room.
- Minimum 2 (commonly 3) redundant pilots is standard; single-pilot designs are a frequent HAZOP/PHA finding. Pilot gas supply should be independently regulated from the main flare gas supply to avoid common-mode failure.

---

## 6. Radiation & Safety Analysis

### 6.1 Thermal Radiation Limits (API RP 521)
| Radiation Level (kW/m²) | Exposure Condition |
|---|---|
| 1.6 | No shielding, indefinite exposure |
| 4.73 | Emergency actions, several minutes exposure, escape route available |
| 6.31 | Emergency actions lasting only seconds |
| 9.46 | Equipment area, personnel excluded during flaring |

**Practical experience:** Run radiation contours for multiple flow cases (normal, intermediate, max) and multiple wind directions/speeds — flame lift/tilt due to wind materially shifts the footprint. Always add the 1.0 kW/m² solar background allowance — a commonly missed detail.

### 6.2 Stack Height & Dispersion Modeling
- Governed by the larger of: radiation limits at grade/nearest equipment, or ground-level concentration limits for **unignited** release (e.g., pilot failure during a relief event).
- Run dispersion modeling (e.g., AERMOD) for the unignited case in addition to the ignited radiation case, especially for H₂S-bearing streams — this can govern stack height.

---

## 7. Environmental & Regulatory Compliance

### 7.1 API Standards
- **API 521** — relief load determination, header sizing philosophy, radiation/dispersion methodology.
- **API 537** — flare tip mechanical/combustion design, assist systems, pilot requirements.

### 7.2 ISO 23251
Internationally harmonized equivalent of API 521, used where contractually specified (common on European/Middle East/multinational projects).

### 7.3 EPA Requirements (40 CFR 60.18)
- ≥98% combustion efficiency, demonstrated via: LHV ≥ 300 Btu/scf (or ≥200 Btu/scf assisted), exit velocity limits per the regulation's Btu/scf-vs-velocity chart, and no visible emissions >5 min in any 2 consecutive hours.
- **Practical note:** Continuous flare gas flow/composition monitoring (GC or NIR analyzer on the header) is increasingly required under site-specific consent decrees — always check current permit conditions, which often exceed the 40 CFR 60.18 baseline.

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific PSV datasheets and simulation results.

### 8.1 Calc Sheet 1 — Fire Case Relief Load (API 521 Wetted Area Method)

**Given:**
- Vessel wetted surface area (fire exposure), `A` = 1,000 ft²
- Environmental factor, `F` = 1.0 (bare vessel, adequate drainage assumed)
- Latent heat of vaporization at relieving conditions, `L` = 150 Btu/lb (propane, approx.)

**Step 1 — Total absorbed heat (API 521 Eq., A ≤ 2,800 ft²):**
```
Q = 21,000 × F × A^0.82
Q = 21,000 × 1.0 × (1,000)^0.82
Q = 21,000 × 288.4
Q ≈ 6,056,000 Btu/hr  (≈ 6.06 MMBtu/hr)
```

**Step 2 — Relieving mass flow:**
```
W = Q / L
W = 6,056,000 / 150
W ≈ 40,373 lb/hr   (≈ 18.3 t/hr, ≈ 18,300 kg/hr)
```

**Result:** Governing fire-case relief load ≈ **40,373 lb/hr** of propane vapor. This becomes the design flow for the PSV, header segment, and downstream KOD/tip sizing below.

> 📌 **Assumption check:** If fireproofing is credited, F drops to ~0.3 and Q/W drop proportionally — confirm fireproofing coverage and rating with the mechanical/piping team before applying a reduced F.

---

### 8.2 Calc Sheet 2 — Header Hydraulics & Mach Number Check

**Given (carried from Calc Sheet 1):**
- Mass flow, `W` = 40,373 lb/hr
- Relieving temperature, `T` = 760 °R (300 °F)
- Header pressure at this point, `P` = 29.7 psia (15 psig)
- MW = 44 (propane), k = 1.13
- Trial pipe size: 10-inch, Schedule 40 (ID = 10.02 in)

**Step 1 — Gas density at relieving conditions (ideal gas):**
```
ρ = (P × MW) / (R × T),   R = 10.73 psia·ft³/(lbmol·°R)
ρ = (29.7 × 44) / (10.73 × 760)
ρ = 1,306.8 / 8,154.8
ρ ≈ 0.160 lb/ft³
```

**Step 2 — Volumetric flow:**
```
Q_v = W / ρ = 40,373 / 0.160 ≈ 252,300 ft³/hr ≈ 70.1 ft³/s
```

**Step 3 — Pipe flow area (10-in Sch 40):**
```
ID = 10.02 in = 0.835 ft
A = (π/4) × (0.835)² = 0.548 ft²
```

**Step 4 — Actual velocity:**
```
V = Q_v / A = 70.1 / 0.548 ≈ 127.9 ft/s
```

**Step 5 — Speed of sound:**
```
c = √[k × (1,545/MW) × T × 32.2]
c = √[1.13 × (1,545/44) × 760 × 32.2]
c = √[1.13 × 35.11 × 760 × 32.2]
c ≈ 985.5 ft/s
```

**Step 6 — Mach number:**
```
M = V / c = 127.9 / 985.5 ≈ 0.13
```

**Result:** M = 0.13, well under the 0.5–0.7 design limit. **10-inch header is acceptable** for this segment on velocity/Mach grounds — backpressure at each upstream PSV tie-in must still be separately verified (Calc Sheet not shown here; use standard Darcy-Weisbach/isothermal compressible flow with header fittings K-values).

> 📌 **Practical note:** This low Mach number leaves margin — on a real project, check whether a smaller (e.g., 8-inch) header still meets Mach/backpressure limits before locking in 10-inch, since header size is a major cost driver.

---

### 8.3 Calc Sheet 3 — Knock-Out Drum Sizing (Horizontal, Souders-Brown)

**Given (carried from Calc Sheets 1–2):**
- Vapor mass flow, `W_v` = 40,373 lb/hr
- Vapor density, `ρ_V` = 0.160 lb/ft³
- Liquid density, `ρ_L` = 30 lb/ft³ (light HC liquid at relieving conditions)
- Droplet cut / `K_SB` = 0.20 ft/s (flare service, coarse cut, no mist eliminator — plugging risk)
- Assumed liquid carryover rate for holdup case = 5,000 lb/hr
- Required liquid residence time = 20 min

**Step 1 — Maximum allowable vapor velocity (Souders-Brown):**
```
V_max = K_SB × √[(ρ_L − ρ_V) / ρ_V]
V_max = 0.20 × √[(30 − 0.16) / 0.16]
V_max = 0.20 × √(186.5)
V_max = 0.20 × 13.66
V_max ≈ 2.73 ft/s
```

**Step 2 — Vapor volumetric flow:**
```
Q_v = W_v / ρ_V = 40,373 / 0.160 = 252,300 ft³/hr = 70.1 ft³/s
```

**Step 3 — Required vapor flow area (horizontal drum, ~50% cross-section available above liquid level):**
```
A_vapor = Q_v / V_max = 70.1 / 2.73 ≈ 25.7 ft²
A_vapor ≈ 0.5 × (π/4) × D²
25.7 = 0.5 × 0.785 × D²
D² = 25.7 / 0.3925 = 65.5
D ≈ 8.09 ft  →  select D = 8 ft-0 in ID
```

**Step 4 — Drum length (L/D = 4, typical for flare KOD):**
```
L = 4 × D = 4 × 8 = 32 ft (tan-to-tan, to be confirmed with heads/nozzle layout)
```

**Step 5 — Liquid holdup volume check (20-min residence, slug scenario):**
```
Q_liquid = 5,000 lb/hr / 30 lb/ft³ = 166.7 ft³/hr = 2.78 ft³/min
V_holdup = 2.78 × 20 = 55.6 ft³
```
Cross-check: available shallow-layer volume in an 8 ft × 32 ft drum (e.g., 6-in liquid layer) ≈ 8 × 32 × 0.5 = 128 ft³ ≫ 55.6 ft³ required → **liquid holdup is not governing**; vapor/droplet removal governs the drum diameter.

**Result:** Horizontal KOD, **8'-0" ID × 32'-0" T/T**, confirmed adequate for both droplet removal and liquid holdup for this case.

> 📌 **Assumption check:** K_SB of 0.20 ft/s is a common flare-service value but varies by company philosophy (0.15–0.35 ft/s range seen in practice) — confirm against project specification before finalizing drum diameter, since D scales with √(1/K_SB).

---

### 8.4 Calc Sheet 4 — Radiation Distance Check (API 521 Point-Source Method)

**Given:**
- Total heat release at flare tip, `Q` = 100 MMBtu/hr (illustrative combined/governing case, larger than the single fire case above)
- Fraction of heat radiated, `τ` (tau) = 0.30 (typical for hydrocarbon flares, range 0.2–0.4 depending on assist type/smokeless performance)
- Target radiation level at grade, `K` = 1,500 Btu/hr·ft² (≈ 4.73 kW/m², personnel with escape route)

**Step 1 — Rearranged point-source equation:**
```
K = (τ × Q) / (4π D²)
→ D = √[τ × Q / (4π × K)]
```

**Step 2 — Substitute values:**
```
D = √[(0.30 × 100,000,000) / (4 × 3.1416 × 1,500)]
D = √[30,000,000 / 18,850]
D = √1,591.5
D ≈ 39.9 ft ≈ 12.2 m
```

**Result:** Minimum slant distance from flame center to any point where personnel may need to take emergency action (with escape route) ≈ **12.2 m**. Repeat with K = 9.46 kW/m² (3,000 Btu/hr·ft²) for equipment-only zones, and re-run with flame tilt geometry (wind-adjusted flame center offset) for the actual stack-height/plot-plan check — the simple point-source method above ignores flame tilt and is typically only a first-pass screening calc; detailed radiation studies use multi-point source or API 521 Annex flame-tilt methodology.

> 📌 **Assumption check:** τ (fraction radiated) is highly sensitive to flare type — steam-assisted smokeless flares are often modeled nearer 0.2, while unassisted/sooty flames can approach 0.4. Confirm the project's basis value; it materially changes the required safe distance / stack height.

---

## 9. Sample Datasheets

### 9.1 PSV / Relief Load Summary Datasheet

| Tag No. | Service | Set Pressure (barg) | Relieving Scenario | Relieving Temp (°C) | Mass Flow (kg/hr) | MW | Phase | k | Governing? |
|---|---|---|---|---|---|---|---|---|---|
| PSV-101 | Propane Storage Vessel | 17.5 | External Fire | 149 | 18,300 | 44.1 | Vapor | 1.13 | ✅ Yes |
| PSV-102 | Propane Storage Vessel | 17.5 | Blocked Outlet | 65 | 9,100 | 44.1 | Vapor | 1.13 | No |
| PSV-201 | Deethanizer OVHD | 24.0 | Power Failure | 55 | 12,400 | 32.6 | Vapor | 1.20 | ✅ Yes (segment 2) |
| PSV-301 | Reflux Drum | 8.5 | Control Valve Failure | 40 | 6,700 | 38.2 | Two-Phase | 1.18 | No |

*(Illustrative — a real relief load summary carries every PSV in the unit, cross-referenced to the cause-and-effect matrix and P&ID tag.)*

---

### 9.2 Knock-Out Drum (KOD) Process Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | V-501 | — |
| **Service** | Flare Knock-Out Drum | — |
| **Orientation** | Horizontal | — |
| **Inside Diameter** | 2,438 (8'-0") | mm |
| **Tangent-to-Tangent Length** | 9,754 (32'-0") | mm |
| **Design Pressure** | 3.5 (full vacuum to +3.5) | barg |
| **Design Temperature** | −29 to 150 | °C |
| **Operating Pressure (normal)** | 0.15 | barg |
| **Governing Relief Case** | Fire Case (Vessel PSV-101) | — |
| **Vapor Inlet Flow (governing case)** | 18,300 | kg/hr |
| **Vapor Density (relieving cond.)** | 2.56 | kg/m³ |
| **Liquid Density (relieving cond.)** | 480 | kg/m³ |
| **Droplet Removal Size (design)** | 400 | µm |
| **K_SB (Souders-Brown constant)** | 0.061 | m/s (≈0.20 ft/s) |
| **Max. Allowable Vapor Velocity** | 0.83 | m/s |
| **Liquid Residence Time (design)** | 20 | min |
| **High Level Alarm** | 50% | % of ID |
| **High-High Level Trip (ESD)** | 65% | % of ID |
| **Corrosion Allowance** | 3 | mm |
| **Material of Construction (shell)** | SA-516 Gr.70 | — |
| **Internals** | Inlet deflector/vane, no mist eliminator (plugging risk) | — |
| **Nozzles** | Inlet (1), Vapor outlet to flare (1), Liquid outlet/pump-out (1), Drain, Level instruments (LG/LT), PSV (thermal relief), Manway | — |
| **Applicable Code** | ASME Section VIII Div. 1 | — |

---

### 9.3 Flare Tip Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | FT-701 | — |
| **Type** | Steam-Assisted, Smokeless | — |
| **Tip Diameter** | 610 (24-in) | mm |
| **Riser Height (grade to tip)** | 45 | m |
| **Design (Max.) Relief Flow** | 45,000 | kg/hr |
| **Normal/Continuous Purge Flow** | 150 | kg/hr |
| **Minimum LHV for Smokeless Operation** | 300 (unassisted basis) | Btu/scf |
| **Exit Velocity at Max. Flow** | 0.5 Mach (≈170) | m/s |
| **Steam-to-Gas Ratio (design)** | 0.3 : 1 (mass basis) | — |
| **Steam Supply Pressure** | 10 | barg |
| **Turndown Ratio** | 20:1 | — |
| **Pilot Burners** | 3 (2 required + 1 standby) | — |
| **Pilot Ignition System** | Flame Front Generator (FFG) | — |
| **Pilot Monitoring** | Thermocouple + UV/IR scanner, alarmed to DCS | — |
| **Molecular Seal / Purge Gas** | N₂, velocity seal, 0.05 m/s min. purge | — |
| **Design Combustion Efficiency** | ≥ 98% | — |
| **Applicable Standard** | API STD 537, 40 CFR 60.18 | — |
| **Radiation at Grade (design case, 12.2 m)** | 4.73 | kW/m² |

---

## 10. Practical Design Checklist

- [ ] Design basis issued and approved (Section 1) before hydraulics begin
- [ ] PSV relief load summary complete (all scenarios, phases, compositions)
- [ ] Governing case identified **per header segment**, not just globally
- [ ] Two-phase relief cases flagged and sized separately (Omega/HEM method)
- [ ] Simultaneous relief cause-and-effect matrix built
- [ ] Backpressure verified at every PSV tie-in (including existing PSVs on brownfield tie-ins)
- [ ] Mach number and AIV screening performed on all high-velocity segments
- [ ] KOD droplet size / K_SB basis agreed with client/site philosophy
- [ ] KOD liquid residence time checked against worst-case slug/dump scenario (see Calc Sheet 3)
- [ ] Flare tip assist type selected based on utility availability (steam/air/fuel gas)
- [ ] Pilot redundancy and independent gas supply confirmed
- [ ] Radiation contours run for multiple flow cases and wind conditions (see Calc Sheet 4)
- [ ] Solar radiation background included in radiation totals
- [ ] Unignited dispersion case modeled for stack height determination
- [ ] Combustion efficiency basis (LHV, exit velocity) checked against 40 CFR 60.18 / local regulation
- [ ] Site-specific consent decree/permit conditions cross-checked
- [ ] All datasheets (PSV summary, KOD, flare tip) issued for vendor/EPC use

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Excessive visible smoke at partial loads | Steam ratio not tuned for real (vs. design) flow | Re-tune steam-to-gas ratio during commissioning across turndown range |
| AIV fatigue cracking at small-bore branches | Under-screened high-velocity segments | Retrofit reinforced branches or reroute instrument connections away from high-Mach zones |
| Liquid carryover to flare tip | KOD undersized for slug/dump scenario, or ESD trip untested | Revisit liquid residence time basis + verify trip testing frequency |
| Nuisance pilot-out trips | Poor flame detector line-of-sight or wind-affected pilot design | Reposition scanners, consider wind-shielded pilot tip |
| Backpressure exceedance after brownfield tie-in | New PSV added without re-verifying network-wide hydraulics | Re-run full hydraulic model network-wide for any new tie-in |
| Radiation exceedance during unexpected high flaring | Radiation study only covered single "worst case" | Model radiation across a range of flows; publish safe-distance curves for Ops |
| KOD oversized/costly | Over-conservative K_SB (fine droplet cut applied unnecessarily) | Confirm K_SB basis against company philosophy before sizing (see Calc Sheet 3 note) |

---

## 12. Case Study — Brownfield LPG Sphere Relief Tie-In

> A composite, illustrative case study based on the type of finding commonly encountered during brownfield flare network debottlenecking at refineries/terminals. Names, tag numbers, and figures are representative, not project-specific.

### 12.1 Background

A terminal was adding a new LPG storage sphere (V-410, MAWP 250 psig) with its own PSV (PSV-410) tied into an existing plant flare header that already served four other PSVs, including an older low-set-pressure PSV (PSV-115, set at 15 psig) on a distillation column overhead drum located far downstream on the same sub-header. The tie-in was engineered as a "local" addition: the new PSV-410 line was sized and hydraulically checked against the *nearest* header segment only, on the assumption that the existing network had adequate spare capacity.

### 12.2 Problem Identified

During detailed engineering hydraulic re-verification (triggered by the project's MOC/PSSR process, not the original tie-in design), the engineer re-ran the **network-wide** backpressure model with PSV-410 relieving simultaneously with the governing fire-zone group that included PSV-115. Two issues surfaced:

1. **Backpressure exceedance at PSV-115:** With the new PSV-410 flow added to the shared header, calculated backpressure at PSV-115's outlet rose to **14% of its set pressure**, exceeding the 10% allowable limit for its conventional (non-balanced) trim — even though PSV-410's own local tie-in point was well within limits. The governing constraint was **not** at the new equipment at all, but at an existing, unrelated PSV far downstream — exactly the brownfield pitfall flagged in this guide's Section 3.1 practical note.
2. **KOD liquid loading:** The existing KOD (V-405) had originally been sized years earlier using a fine droplet-cut basis (K_SB ≈ 0.10 ft/s) inherited from an old company standard. When the current project's engineer re-ran the Souders-Brown check (per the Calc Sheet 8.3 method in this guide) using the current corporate K_SB of 0.20 ft/s, the drum was confirmed to have **more real margin** than the original design assumed — but this had never been checked, so the project team had initially budgeted for a costly KOD replacement that turned out to be unnecessary.

### 12.3 Investigation & Recalculation

- **Network hydraulics:** The team rebuilt the full hydraulic model (not just the local tie-in segment) using the Calc Sheet 8.2 methodology of this guide, applied at every PSV tie-in point rather than only the new one. This confirmed PSV-115 as the governing constraint and identified two viable fixes: (a) upsize ~120 m of the shared sub-header from 8-inch to 10-inch, or (b) reroute PSV-410 into a separate sub-header joining the main header downstream of PSV-115's tie-in point.
- **KOD re-verification:** Using the current K_SB = 0.20 ft/s basis (Calc Sheet 8.3 method) against V-405's actual as-built diameter and the updated combined relief load (including PSV-410), the drum was confirmed adequate without modification — avoiding an unnecessary replacement.
- **Radiation re-check:** Because the combined relief load changed, radiation at the two nearest occupied work areas was re-run (Calc Sheet 8.4 method) for the new simultaneous case. The result remained within the 4.73 kW/m² limit with margin, so no stack height change was required.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **Local-only hydraulic verification at tie-in design** — the new PSV-410 line was checked against its immediate connection point but the shared network was never re-run end-to-end for the new simultaneous relief case, so the impact on PSV-115 (a completely different, older PSV) was missed until the MOC review.
2. **Undocumented legacy design margin at the KOD** — the original K_SB basis used for V-405 was never recorded in a retrievable design basis document, so the project defaulted to assuming the drum needed replacement rather than re-verifying it against the current, less conservative, corporate standard.

### 12.5 Resolution

- **Hydraulics:** Option (b) was selected — PSV-410 was rerouted into a new, independent sub-header tying into the main header downstream of PSV-115, avoiding both the sub-header upsize cost and any backpressure impact on the existing PSV. This is generally the lower-cost fix on brownfield headers when a downstream tie-in point is geometrically available.
- **KOD:** No hardware change required; the re-verified Souders-Brown calculation was issued as an updated design basis record for V-405 so future tie-in projects would not repeat the "assume replacement needed" default.
- **Radiation:** No change required; updated contour issued for records.
- **Process safety management:** The terminal's MOC procedure was updated to require a network-wide hydraulic re-run (all existing PSV tie-ins, not just the new one) as a mandatory checklist item for any new flare header tie-in, however small the new load appears relative to total header capacity.

### 12.6 Outcome

- The rerouted sub-header addition was implemented during the original construction window with a minor (2-week) engineering schedule impact, avoiding a much larger cost and schedule hit that a full 120 m sub-header upsize (or unnecessary KOD replacement) would have caused.
- The finding was documented as a corporate lessons-learned item: "small" brownfield tie-ins require the same network-wide verification rigor as new grassroots headers, since the governing constraint is frequently at an unrelated, pre-existing PSV rather than at the new connection itself.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A "local" tie-in check is not sufficient — the governing backpressure constraint is often at an unrelated, pre-existing PSV elsewhere on the shared header | Mandate network-wide (all PSV tie-ins) hydraulic re-verification for every new flare header connection, regardless of how small the added load seems |
| Undocumented legacy design margins (e.g., K_SB basis) lead to costly default assumptions | Record and retain the design basis (K_SB, residence time, etc.) for every KOD so future projects can re-verify rather than assume replacement is needed |
| Rerouting into a downstream tie-in point can be a lower-cost fix than upsizing a shared sub-header | Evaluate routing alternatives before defaulting to pipe upsizing when a backpressure exceedance is found |
| Radiation and KOD checks should be re-run whenever the combined relief load changes, even if the new PSV's own load is small | Include radiation and KOD re-verification explicitly in the brownfield tie-in MOC checklist, not just hydraulics |

---

## 13. Reference Standards

- **API RP 521** — Pressure-relieving and Depressuring Systems
- **API STD 537** — Flare Details for Petroleum, Petrochemical, and Natural Gas Industries
- **API STD 520** (Parts I & II) — Sizing, Selection, and Installation of Pressure-relieving Devices
- **ISO 23251** — Petroleum, petrochemical and natural gas industries — Pressure-relieving and depressuring systems
- **40 CFR 60.18** — General Control Device and Work Practice Requirements (US EPA)
- **Energy Institute Guidelines for the Avoidance of Vibration Induced Fatigue Failure** — AIV screening methodology

---

*This guide is a practical study reference combining standard design theory with worked sample calculations and lessons learned from flare network design/review experience. All numeric examples are illustrative — always validate against project-specific design basis, vendor data, simulation results, and current regulatory requirements.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
