# 🛢️ Separator Design — Practical Study Guide

> A field-oriented reference covering the core engineering topics in gas-liquid and three-phase separator design — combining API 12J/ASME Section VIII methodology with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution. This guide is a companion to the **Steady-State Simulation**, **Compressor Settle-Out Calculations**, and **Flare Network Design** study guides — the separators developed here feed directly into the compressor suction and flare knock-out drum equipment those guides depend on.

**Illustrative project used throughout this guide:** a new three-phase production separator (V-300), validated against Aspen HYSYS sizing output, a high-GOR vertical separator with a mesh pad mist eliminator, a compact compressor suction scrubber protecting K-101 (the same compressor used in the companion Compressor Settle-Out and Steady-State Simulation guides), and a flare knock-out drum with an accompanying liquid seal drum. All numbers below are worked sample calculations for study purposes — always replace with project-specific fluid properties and vendor-confirmed internals performance.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Session 10 — Horizontal Separator Fundamentals](#2-session-10--horizontal-separator-fundamentals)
3. [Session 11 — Separator Sizing in Aspen HYSYS](#3-session-11--separator-sizing-in-aspen-hysys)
4. [Session 12 — Vertical Separator with Mist Eliminator](#4-session-12--vertical-separator-with-mist-eliminator)
5. [Session 13 — Compressor Package Separator](#5-session-13--compressor-package-separator)
6. [Session 14 — Knock-Out Drum Sizing](#6-session-14--knock-out-drum-sizing)
7. [Sample Calculation Sheets](#7-sample-calculation-sheets)
8. [Sample Datasheets](#8-sample-datasheets)
9. [Practical Design Checklist](#9-practical-design-checklist)
10. [Common Field Issues & Lessons Learned](#10-common-field-issues--lessons-learned)
11. [Case Study — Three-Phase Separator Undersized Because Only Gas Capacity Was Checked](#11-case-study--three-phase-separator-undersized-because-only-gas-capacity-was-checked)
12. [Reference Standards](#12-reference-standards)

---

## 1. Design Basis & Assumptions

Separator sizing is governed by **two independent criteria that must both be satisfied** — gas capacity (droplet settling, via the Souders-Brown equation) and liquid retention time (holdup volume for adequate phase separation and downstream surge protection) — and, critically, **either one can govern**, depending on the specific gas/liquid rate ratio. This guide's Calc Sheet 7.1 works through a case where liquid retention time, not gas capacity, turns out to be the governing (and often overlooked) criterion.

### 1.1 Process Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| V-300 (three-phase separator) | Gas 25 MMscfd, oil 3,000 bpd, water 1,500 bpd, 800 psia/100°F | Used in Calc Sheets 7.1–7.2 |
| Vertical separator (high-GOR) | Gas 40 MMscfd, 1,000 psia/80°F, with mesh pad | Used in Calc Sheet 7.3 |
| Compressor suction scrubber | Protects K-101 (companion Compressor Settle-Out and Steady-State Simulation guides), 800 psia/100°F, 50,000 lb/hr | Used in Calc Sheet 7.4 |
| Flare KOD + liquid seal drum | Fire-case flow 40,373 lb/hr (companion Flare Network Design guide basis) | Used in Calc Sheet 7.5 |

### 1.2 Codes & Standards / Methodology Basis
- **API 12J** — specification for oil and gas separators, the primary standard for horizontal/vertical separator sizing criteria
- **ASME BPVC Section VIII** — pressure vessel code governing the separator's pressure boundary (companion Mechanical Datasheet guide's methodology applied to separator shells/heads)
- **API 614** — auxiliary equipment for compressors, including suction scrubber design considerations (Section 5)
- **HEI/Otto York (or equivalent manufacturer) data** — mist eliminator (mesh pad, vane pack) performance data

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Souders-Brown K-value, horizontal separator, no mist eliminator | 0.40 ft/s | Confirm against actual API 12J/vendor guidance for the specific service; varies with pressure and fluid properties |
| Souders-Brown K-value, vertical separator with mesh pad | 0.35 ft/s | Section 4.1; higher than no-mesh-pad cases |
| Souders-Brown K-value, compact scrubber with vane pack | 0.40 ft/s | Section 5.1; vane packs tolerate higher velocity than mesh pads, supporting a more compact design |
| Liquid retention time (oil and water phases) | 5 minutes each (minimum) | Confirm against project-specific philosophy; higher for surge protection ahead of sensitive downstream equipment |
| Vapor space fraction (horizontal separator, normal liquid level) | 50% of cross-section | Typical design assumption; confirm against the specific level control philosophy |
| Target L/D ratio (horizontal separators) | 3:1–5:1 | Practical fabrication/support span guideline; Calc Sheet 7.1 shows what happens outside this range |
| Mist eliminator effective operating range | 30–100% of rated K_SB velocity | Below this range, poor droplet capture (insufficient inertial impaction); above it, re-entrainment risk |

> ⚠️ **Practical note:** The single most common separator sizing error is checking gas capacity (Souders-Brown) carefully while treating liquid retention time as an afterthought, or vice versa — both criteria must be independently calculated and compared, since either one can govern depending on the specific gas-to-liquid ratio, exactly as Calc Sheet 7.1 and the Case Study (Section 11) illustrate.

---

## 2. Session 10 — Horizontal Separator Fundamentals

### 2.1 Applications
Horizontal separators are the standard choice for **gas-liquid** separation with meaningful liquid rates, and for **three-phase** oil/gas/water separation — their geometry naturally provides a long liquid residence path and a large liquid/vapor interface area per unit volume, both favorable for higher-liquid-rate services (unlike a vertical separator, better suited to gas-dominant streams — Section 4).

### 2.2 Design Basis
Operating pressure, temperature, and fluid properties (density, viscosity) come directly from the process design basis (companion Steady-State Simulation guide) — these establish both the gas density (governing Souders-Brown sizing) and the liquid properties (governing retention time and, for three-phase separators, interface/emulsion behavior).

### 2.3 Sizing Criteria
- **Gas capacity (Souders-Brown equation)** — `V_max = K √[(ρL−ρV)/ρV]`, setting the minimum vapor space cross-sectional area for adequate droplet settling (Section 2.4/Calc Sheet 7.1).
- **Liquid retention time (holdup volume)** — the liquid volume needed to provide adequate residence time for phase separation (oil/water) and to buffer against normal flow variability, often the actual governing criterion for higher-liquid-rate services (Calc Sheet 7.1).
- **Interface control for three-phase separation** — a level control system (typically a displacer or capacitance-type interface level transmitter) must actively maintain the oil/water interface within the vessel, since the two liquid phases will otherwise migrate over time; the vessel's internal weir arrangement (Section 2.4) works together with this control system.

### 2.4 Mechanical Aspects
- **Length-to-diameter (L/D) ratio** — a practical fabrication/support and performance guideline (typically 3:1–5:1, Section 1.3); a vessel sized purely to satisfy liquid holdup volume without checking L/D can end up impractically long and slender, as Calc Sheet 7.1 shows.
- **Internals** — weirs (separating the oil and water compartments in a three-phase separator, maintaining independent liquid levels for each), and baffles/inlet diverters (breaking the momentum of the incoming multiphase stream to promote initial gross gas-liquid separation before the stream reaches the settling section).

### 2.5 Standards
**API 12J** (separator sizing/performance criteria) and **ASME Section VIII** (pressure vessel code, companion Mechanical Datasheet guide methodology).

---

## 3. Session 11 — Separator Sizing in Aspen HYSYS

### 3.1 Simulation Setup
Feed composition, pressure, and temperature are defined consistent with the companion Steady-State Simulation guide's model setup methodology (that guide's Section 2.3) — the separator's feed stream is typically an output from an upstream unit operation (a wellhead choke, a compressor discharge, or a simple feed stream for a standalone separator study).

### 3.2 Flash Calculations
HYSYS performs a rigorous vapor-liquid (and, for three-phase-capable property packages, vapor-liquid-liquid) equilibrium flash at the separator's operating conditions — the same underlying physics as the companion Steady-State Simulation guide's manual Rachford-Rice flash validation (that guide's Calc Sheet 8.1), but solved rigorously with the selected thermodynamic package rather than pre-determined K-values.

### 3.3 Separator Block Configuration
The HYSYS separator unit operation is configured with defined gas and liquid outlet streams (and, for a three-phase-capable block, a separate water outlet); **mist carryover** is not automatically modeled by the basic flash equilibrium alone — actual droplet carryover past the separator's internals requires either a dedicated sizing utility (Section 3.4) or an explicit droplet-size/efficiency calculation layered on top of the equilibrium flash result.

### 3.4 Validation — Simulation Sizing vs. Hand Calculations
HYSYS's built-in separator sizing utility (using the same underlying Souders-Brown and retention-time methodology as Section 2.3) should be cross-checked against an independent hand calculation before being relied upon as a final design basis — see Calc Sheet 7.2 for a worked comparison.

### 3.5 Integration with Downstream Equipment
The separator's gas and liquid outlet stream conditions become the feed basis for downstream equipment — gas outlet conditions feed the companion Compressor Settle-Out guide's compressor suction basis, and liquid outlet conditions feed downstream pumps, exchangers (companion Heat Exchanger Design guide), or further separation/treating equipment.

---

## 4. Session 12 — Vertical Separator with Mist Eliminator

### 4.1 Applications
Vertical separators are well-suited to **high gas-to-liquid ratio** streams, where the liquid volume is small relative to the gas flow — the vertical geometry uses plot space efficiently for this service type, unlike a horizontal separator, which is more space-efficient for higher liquid rates (Section 2.1).

### 4.2 Design Criteria
- **Gas velocity limits (Souders-Brown)** — the same underlying equation as Section 2.3, but with a higher allowable K-value when a mist eliminator is installed (Section 1.3), since the mist eliminator itself provides additional droplet capture beyond simple gravity settling.
- **Liquid droplet removal efficiency** — the mist eliminator's actual performance (Section 4.3) at the design gas velocity, not just the bulk Souders-Brown vessel sizing check alone.

### 4.3 Mist Eliminators
| Type | Characteristics |
|---|---|
| **Mesh pad** | Simple, low cost, good efficiency for droplets down to ~10 microns at design velocity; can plug/foul in dirty or waxy/asphaltenic services (companion Flow Assurance guide's deposition discussion is relevant here) |
| **Vane pack** | Tolerates higher velocity (more compact for a given flow), lower fouling tendency than mesh pad, but somewhat lower fine-droplet efficiency; often preferred for compact/skid-mounted designs (Section 5) |
| **Cyclonic** | Highest capacity/most compact for a given flow, good for higher liquid loading, but generally the highest pressure drop and most complex internals |

### 4.4 Efficiency vs. Pressure Drop Trade-offs
A mist eliminator's droplet removal efficiency and pressure drop both increase with velocity — operating within the manufacturer's recommended range (typically 30–100% of the rated K_SB velocity, Section 1.3) balances adequate removal efficiency against excessive pressure drop and re-entrainment risk; see Calc Sheet 7.3 for a worked example checking this operating range.

### 4.5 Mechanical Design
Vessel diameter (from the gas capacity check, Calc Sheet 7.3), height (accounting for liquid holdup at the bottom, disengagement space, mist eliminator thickness, and adequate space above the eliminator for the gas outlet nozzle), and internals arrangement (inlet diverter, mist eliminator support ring, liquid outlet).

### 4.6 Standards
**API 12J** and manufacturer/**TEMA-adjacent** guidelines for internals (mist eliminator vendors typically provide their own detailed sizing/performance data beyond the generic API 12J K-value tables).

---

## 5. Session 13 — Compressor Package Separator

### 5.1 Purpose
Protect the compressor (companion Compressor Settle-Out guide's K-101) from liquid carryover, which can cause serious mechanical damage (impeller/valve damage from liquid slugging, particularly severe for reciprocating compressors, but also a real risk for centrifugal machines).

### 5.2 Design Focus
- **High-efficiency mist elimination** — compressor suction scrubbers typically target a stricter liquid carryover specification than a general process separator (often specified directly by the compressor OEM, e.g., <0.1 gal/MMscf), since even small liquid carryover accumulated over continuous operation poses a real risk.
- **Compact design for skid-mounted packages** — compressor packages are frequently skid-mounted with tight footprint constraints, favoring vane-pack or cyclonic internals (Section 4.3) over a larger mesh-pad vessel — see Calc Sheet 7.4 for a worked compact sizing example.

### 5.3 Sizing Criteria
Gas velocity limits (Section 4.2 methodology, with the vane-pack K-value from Section 1.3) and liquid droplet size distribution (confirming the selected internals actually achieve the OEM's carryover specification at the design velocity, not just passing a generic Souders-Brown check).

### 5.4 Integration
- **Anti-surge systems** — the suction scrubber sits directly in the compressor's suction path, so its liquid level and any potential for liquid carryover during a transient (companion Dynamic Simulation guide's Section 5.2 anti-surge discussion) must be considered alongside the compressor's own protection scheme.
- **Recycle lines** — anti-surge recycle flow often returns to the suction scrubber inlet (or directly to the suction line upstream of it), meaning the scrubber must be sized for the recycle case's flow, not just the normal suction flow alone.

### 5.5 Standards
**API 614** (auxiliary equipment for compressors) and **OEM guidelines** (compressor vendors frequently specify their own suction scrubber requirements beyond the generic API 614 baseline).

---

## 6. Session 14 — Knock-Out Drum Sizing

### 6.1 Purpose
Remove liquids **before** the flare (protecting the flare tip from liquid carryover, companion Flare Network Design guide's Section 4) or before other downstream equipment (e.g., a vent system).

### 6.2 Design Criteria
- **Gas capacity (Souders-Brown)** — detailed in full in the companion Flare Network Design guide's Calc Sheet 8.3, using a coarser droplet-cut K-value than a process separator, since flare service tolerates some liquid carryover risk trade-off against drum size.
- **Liquid holdup time** — typically **5–10 minutes**, sized against the operator's response time to a high-level alarm (companion Flare Network Design guide's Section 4.2).
- **Droplet size removal efficiency** — the target droplet cut (300–600 µm typical for flare KODs, companion Flare Network Design guide's Section 4.1), coarser than a process separator's typical 100–150 µm target, since flare KODs deliberately avoid mist eliminators (plugging risk in intermittent, potentially fouling relief service).

### 6.3 Types
Horizontal vs. vertical KODs — the same fundamental trade-offs as Section 2.1 (horizontal favors higher liquid loading/larger L/D settling length; vertical favors smaller footprint) apply, detailed in the companion Flare Network Design guide's Section 3.3.

### 6.4 Safety Considerations
- **Flare system integration** — the KOD sits directly in the relief path, so its sizing must account for the full range of relief scenarios feeding it (companion PSV Sizing & Design guide's Section 7.2), not just a single governing case.
- **Liquid seal drums** — where required (typically on lower-pressure flare/vent headers), a liquid seal drum provides a water leg that prevents air ingress/flashback into the flare system while still allowing relief gas to bubble through during an actual relief event — sized against both the maximum system pressure the seal must hold back and the maximum credible bubble-through gas flow, worked in Calc Sheet 7.5.

---

## 7. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific fluid properties and vendor-confirmed internals performance.

### 7.1 Calc Sheet 1 — Horizontal Three-Phase Separator Sizing (V-300)

**Given:** Gas 25 MMscfd, oil 3,000 bpd, water 1,500 bpd; operating 800 psia/100°F (560°R); gas MW = 19, Z = 0.88; oil ρ = 53 lb/ft³, water ρ = 62.4 lb/ft³; K_SB = 0.40 ft/s (Section 1.3, no mist eliminator); liquid retention time = 5 min each phase (Section 1.3); target L/D = 3–5.

**Step 1 — Gas density at operating conditions:**
```
ρg = (P×MW)/(Z×R×T) = (800×19)/(0.88×10.73×560) = 15,200/5,287.7 ≈ 2.875 lb/ft³
```

**Step 2 — Actual gas volumetric flow (converting from standard conditions):**
```
Q_actual = 25,000,000 scf/day × (14.7/800) × (560/520) × (0.88/1.0) / 1,440 min/day
Q_actual ≈ 302.3 acfm ≈ 5.038 acfs
```

**Step 3 — Souders-Brown maximum vapor velocity (governed by the lighter liquid phase, oil):**
```
Vmax = K×√[(ρL−ρg)/ρg] = 0.40×√[(53−2.875)/2.875] = 0.40×√17.43 ≈ 1.670 ft/s
```

**Step 4 — Required vapor flow area and diameter (50% vapor space assumption):**
```
A_vapor = 5.038/1.670 ≈ 3.017 ft²
A_vapor = 0.5×(π/4)×D²  →  D² = 3.017/0.3927 ≈ 7.684  →  D ≈ 2.77 ft (≈33 in)
```

**Step 5 — Liquid holdup volume (5 min retention, each phase):**
```
Oil: 3,000 bbl/day × 5.615 ft³/bbl / 1,440 min/day ≈ 11.70 ft³/min → ×5 min = 58.5 ft³
Water: 1,500 bbl/day × 5.615 / 1,440 ≈ 5.85 ft³/min → ×5 min = 29.25 ft³
Total liquid volume = 58.5 + 29.25 = 87.75 ft³
```

**Step 6 — Check required length at the gas-capacity-governed diameter (D ≈ 2.77 ft):**
```
Liquid c/s area (50% of circle) = 0.5×π×(1.385)² ≈ 3.02 ft² (approx., using D≈2.77ft, r≈1.385ft)
L = 87.75/3.02 ≈ 29.1 ft
L/D = 29.1/2.77 ≈ 10.5  →  FAR exceeds the 3–5 target — impractically long/slender vessel
```

**Step 7 — Resolve: resize diameter for a practical L/D (target L/D = 4), governed by liquid holdup instead:**
```
Liquid volume = 0.5×π×(D/2)²×L,  with L = 4D
87.75 = 0.5×π×(D²/4)×4D = 0.5×π×D³
D³ = 87.75/1.5708 ≈ 55.86  →  D ≈ 3.82 ft → round to standard 48-in (4 ft) shell

Check at D=4 ft: A_liquid = 0.5×π×2² ≈ 6.283 ft²; L = 87.75/6.283 ≈ 13.97 ft
L/D = 13.97/4 ≈ 3.49  →  within the 3–5 target
```

**Step 8 — Re-verify gas capacity is still satisfied at the larger diameter:**
```
A_vapor,actual = 0.5×(π/4)×4² ≈ 6.28 ft²
V_actual = 5.038/6.28 ≈ 0.802 ft/s < Vmax (1.670 ft/s)  →  PASS, with significant margin
```

**Result:** **Liquid retention time — not gas capacity — governs** this separator's sizing. The gas-capacity-only diameter (2.77 ft) would have produced an impractically long, slender vessel (L/D ≈ 10.5) once liquid holdup was checked; resizing to **D = 4 ft, L ≈ 14 ft (L/D ≈ 3.5)** satisfies both criteria with margin on gas capacity.

> 📌 **Assumption check:** This is one of the most important lessons in separator sizing — always calculate **both** criteria independently and compare, rather than sizing for gas capacity alone (a common shortcut when gas rate is the parameter most readily available early in a project) and only checking liquid holdup as an afterthought. See the Case Study (Section 11) for a real consequence of skipping this cross-check.

---

### 7.2 Calc Sheet 2 — Validate HYSYS Sizing vs. Hand Calculation

**Given:** HYSYS's built-in separator sizing utility, run against the same V-300 feed/conditions as Calc Sheet 7.1, reports: D = 4.0 ft, L = 14.5 ft.

**Step 1 — Compare diameter:**
```
Hand calc: D = 4.0 ft (rounded); HYSYS: D = 4.0 ft
Difference: 0%  →  Match
```

**Step 2 — Compare length:**
```
Hand calc: L ≈ 13.97 ft; HYSYS: L = 14.5 ft
Difference = (14.5−13.97)/13.97 × 100% ≈ 3.8%
```

**Step 3 — Compare to validation tolerance (companion Steady-State Simulation guide's ≤5–10% cross-check principle):**
```
3.8% < 10%  →  PASS
```

**Result:** HYSYS's sizing utility output agrees with the independent hand calculation within **≈3.8%** — the simulation-based sizing is validated and can be relied upon as the design basis, consistent with the companion Steady-State Simulation guide's Section 7.1 validation principle applied here specifically to separator sizing.

> 📌 **Assumption check:** A validation check like this is most valuable specifically **because** it's fast and simple — always perform it before accepting a simulation tool's sizing utility output for a new or unusual service, since sizing utilities can be configured with defaults (e.g., a different K-value or retention time assumption) that don't match the project's actual design basis unless explicitly set.

---

### 7.3 Calc Sheet 3 — Vertical Separator with Mesh Pad Mist Eliminator

**Given:** Gas 40 MMscfd, 1,000 psia/80°F (540°R), MW = 18, Z = 0.85; condensate ρL = 46.8 lb/ft³; mesh pad K_SB = 0.35 ft/s (Section 1.3).

**Step 1 — Gas density:**
```
ρg = (1,000×18)/(0.85×10.73×540) = 18,000/4,925.1 ≈ 3.655 lb/ft³
```

**Step 2 — Actual gas flow:**
```
Q_actual = 40,000,000 × (14.7/1,000) × (540/520) × (0.85/1.0) / 1,440 ≈ 360.4 acfm ≈ 6.007 acfs
```

**Step 3 — Souders-Brown maximum velocity:**
```
Vmax = 0.35×√[(46.8−3.655)/3.655] = 0.35×√11.805 ≈ 1.203 ft/s
```

**Step 4 — First-pass diameter (30-in trial):**
```
A(30in) = (π/4)×(2.5)² ≈ 4.909 ft²
V = 6.007/4.909 ≈ 1.224 ft/s > Vmax (1.203 ft/s)  →  FAIL (marginal)
```

**Step 5 — Resize to 36-in:**
```
A(36in) = (π/4)×(3)² ≈ 7.069 ft²
V = 6.007/7.069 ≈ 0.850 ft/s < Vmax (1.203 ft/s)  →  PASS
```

**Step 6 — Check the mesh pad's effective operating range (Section 1.3, 30–100% of rated velocity):**
```
V_actual/Vmax = 0.850/1.203 ≈ 0.71 (71%)  →  within the 30–100% effective range  →  Good expected performance
```

**Result:** Select a **36-in ID vertical separator** with a mesh pad mist eliminator — the 30-in trial size failed the gas capacity check; the 36-in size passes with good margin and operates at 71% of the mesh pad's rated velocity, within its effective performance range (neither under-loaded nor at re-entrainment risk).

> 📌 **Assumption check:** Operating well below 30% of rated velocity is also a real concern (not just above 100%) — a mesh pad relies partly on inertial impaction, which becomes less effective at very low velocity; if turndown operation is expected to push velocity below ~30% of rated Vmax for extended periods, confirm the mesh pad's actual low-velocity performance with the vendor rather than assuming the sizing calc alone guarantees adequate removal across the full turndown range.

---

### 7.4 Calc Sheet 4 — Compressor Suction Scrubber Sizing (Compact, Vane Pack)

**Given:** K-101 suction (companion Compressor Settle-Out and Steady-State Simulation guides basis), W = 50,000 lb/hr, 800 psia/100°F (560°R), MW = 18, Z = 0.9; light condensate ρL = 30 lb/ft³; vane pack K_SB = 0.40 ft/s (Section 1.3, compact/skid design).

**Step 1 — Gas density:**
```
ρg = (800×18)/(0.9×10.73×560) = 14,400/5,407.9 ≈ 2.663 lb/ft³
```

**Step 2 — Actual gas flow:**
```
Q_actual = 50,000/2.663 ≈ 18,776 ft³/hr ≈ 5.216 ft³/s
```

**Step 3 — Souders-Brown maximum velocity:**
```
Vmax = 0.40×√[(30−2.663)/2.663] = 0.40×√10.27 ≈ 1.282 ft/s
```

**Step 4 — Required diameter:**
```
A = 5.216/1.282 ≈ 4.068 ft²
D = √(4×4.068/π) ≈ 2.276 ft (≈27.3 in) → round to standard 30-in
```

**Step 5 — Verify at 30-in:**
```
A(30in) ≈ 4.909 ft²
V = 5.216/4.909 ≈ 1.063 ft/s < Vmax (1.282 ft/s)  →  PASS, ≈17% margin
```

**Result:** A **30-in ID compact scrubber with a vane-pack mist eliminator** satisfies the gas capacity requirement with reasonable margin, in a substantially smaller footprint than an equivalent mesh-pad vertical separator (companion Calc Sheet 7.3's higher-flow example needed 36-in even at a comparable per-unit-flow basis, partly reflecting the vane pack's higher allowable K-value) — well-suited to a skid-mounted compressor package's space constraints.

> 📌 **Assumption check:** Always confirm the compressor OEM's specific liquid carryover specification (often stated directly as gal/MMscf, not just a generic Souders-Brown K-value) — a scrubber that "passes" the Souders-Brown check can still fail to meet a stricter OEM carryover limit if the actual droplet size distribution in the incoming stream is finer than the vane pack's effective removal range; confirm against vendor-specific performance data, not the generic K-value alone, for a genuinely compressor-protection-critical scrubber.

---

### 7.5 Calc Sheet 5 — Flare KOD Gas Capacity Reference & Liquid Seal Drum Sizing

**Given (KOD gas capacity, cross-referencing the companion Flare Network Design guide's Calc Sheet 8.3 in full):** That guide's worked example resulted in an **8 ft ID × 32 ft T/T horizontal KOD**, sized against a fire-case flow of 40,373 lb/hr using a coarse-cut K_SB = 0.20 ft/s. This guide does not repeat that calculation — see the companion guide directly.

**New calculation — Liquid Seal Drum:**

**Given:** Maximum flare header pressure the seal must hold back = 2 psig; seal fluid = water (ρ = 62.4 lb/ft³); safety margin for turbulence/splash = 9 in; maximum credible bubble-through gas flow (fire case, per companion Flare Network Design guide) = 40,373 lb/hr; gas conditions at the seal (near-atmospheric) ≈ 16.7 psia/100°F (560°R), MW = 44, Z = 0.98; target bubble velocity limit = 4 ft/s.

**Step 1 — Required seal leg depth:**
```
h(in H2O) = P(psi) × 27.7 in H2O/psi = 2 × 27.7 = 55.4 in H2O
Total seal depth = 55.4 + 9 (margin) ≈ 64.4 in ≈ 65 in (5.4 ft)
```

**Step 2 — Gas density at seal conditions:**
```
ρg = (16.7×44)/(0.98×10.73×560) = 734.8/5,888.6 ≈ 0.1248 lb/ft³
```

**Step 3 — Actual gas volumetric flow through the seal:**
```
Q = 40,373/0.1248 ≈ 323,500 ft³/hr ≈ 89.86 ft³/s
```

**Step 4 — Required seal drum diameter (bubble velocity limit):**
```
A = Q/V = 89.86/4 ≈ 22.47 ft²
D = √(4×22.47/π) ≈ 5.35 ft (≈64 in) → round to standard 72-in (6 ft) shell
```

**Result:** The liquid seal drum requires a **≈65-in (5.4 ft) water seal leg depth** (to hold back the 2 psig maximum header pressure with margin) and a **≈6 ft diameter** drum (to keep bubble-through velocity at the fire-case emergency flow rate within the 4 ft/s guideline, avoiding excessive liquid carryover/seal loss during the actual relief event).

> 📌 **Assumption check:** The seal leg depth calculation is a straightforward hydrostatic check, but the bubble velocity guideline (and resulting diameter) is a more approximate, vendor/experience-based rule of thumb — for a safety-critical liquid seal drum, confirm the diameter against the specific seal design's actual tested performance (some designs use a distributor or multiple smaller seal legs rather than a single large-diameter open seal, changing the sizing approach entirely) rather than relying on this simplified single-orifice bubble velocity model alone.

---

## 8. Sample Datasheets

### 8.1 Horizontal Three-Phase Separator Datasheet — V-300

| Parameter | Value |
|---|---|
| Tag No. | V-300 |
| Service | Three-phase production separator |
| Orientation | Horizontal |
| Design flow (gas/oil/water) | 25 MMscfd / 3,000 bpd / 1,500 bpd |
| Operating pressure/temperature | 800 psia / 100°F |
| Governing sizing criterion | Liquid retention time (Calc Sheet 7.1) |
| Diameter | 4 ft (48 in) |
| Length (T/T) | 14 ft |
| L/D ratio | 3.5 |
| Gas capacity margin | Significant (Vactual ≈ 48% of Vmax) |
| Internals | Inlet diverter, oil/water weir, mesh-free (no mist eliminator) |
| Interface control | Displacer-type interface level transmitter, oil/water weir |
| HYSYS sizing validation | 3.8% deviation — PASS (Calc Sheet 7.2) |
| Applicable codes | API 12J, ASME Section VIII |

---

### 8.2 Vertical Separator with Mist Eliminator Datasheet

| Parameter | Value |
|---|---|
| Service | High-GOR gas/condensate separation |
| Design gas flow | 40 MMscfd |
| Operating pressure/temperature | 1,000 psia / 80°F |
| Diameter | 36 in |
| Mist eliminator type | Mesh pad, 6-in thickness (typical) |
| Design velocity / rated Vmax | 0.850 / 1.203 ft/s (71% of rated) |
| Expected removal efficiency | >99% for droplets >10 microns at design velocity |
| Estimated ΔP across mesh pad | ≈1.5 in H₂O |
| Applicable codes | API 12J, manufacturer mist eliminator data |

---

### 8.3 Compressor Suction Scrubber Datasheet

| Parameter | Value |
|---|---|
| Service | K-101 suction protection |
| Design flow | 50,000 lb/hr |
| Operating pressure/temperature | 800 psia / 100°F |
| Diameter | 30 in |
| Mist eliminator type | Vane pack (compact) |
| Design velocity / rated Vmax | 1.063 / 1.282 ft/s (83% of rated) |
| Target liquid carryover spec | <0.1 gal/MMscf (confirm against K-101 OEM requirement) |
| Anti-surge recycle tie-in | Yes — confirm scrubber sized for recycle case flow, not suction flow alone |
| Applicable standard | API 614, OEM guidelines |

---

### 8.4 Liquid Seal Drum Datasheet

| Parameter | Value |
|---|---|
| Service | Flare header liquid seal (upstream of KOD) |
| Max header pressure to be sealed | 2 psig |
| Seal leg depth | 65 in (5.4 ft), including margin |
| Drum diameter | 6 ft (72 in) |
| Design bubble-through flow | 40,373 lb/hr (fire case, per companion Flare Network Design guide) |
| Target bubble velocity limit | 4 ft/s |
| Seal fluid | Water |
| Applicable codes | API 12J (general vessel practice), project-specific seal drum design standard |

---

## 9. Practical Design Checklist

- [ ] Both gas capacity (Souders-Brown) and liquid retention time calculated independently, with the governing criterion explicitly identified — see Calc Sheet 7.1
- [ ] L/D ratio checked against the practical 3:1–5:1 target once the governing criterion's diameter/length are determined
- [ ] For three-phase separators, interface control philosophy and weir arrangement explicitly specified, not just bulk liquid holdup
- [ ] Simulation tool sizing output (HYSYS or equivalent) independently cross-checked against a hand calculation — see Calc Sheet 7.2
- [ ] Mist eliminator type selected based on the actual service (fouling tendency, compactness requirement, target droplet size), not defaulted to mesh pad for every service
- [ ] Mist eliminator operating point checked against its effective range (30–100% of rated velocity), not just a bare pass/fail on the upper limit — see Calc Sheet 7.3
- [ ] Compressor suction scrubbers checked against the OEM's specific carryover specification, not just a generic Souders-Brown pass — see Calc Sheet 7.4
- [ ] Compressor suction scrubber sized for the anti-surge recycle case flow, not suction flow alone
- [ ] Flare KOD sizing cross-referenced to the companion Flare Network Design guide's full methodology
- [ ] Liquid seal drum (where required) sized for both seal leg depth (hydrostatic) and bubble-through velocity (drum diameter) — see Calc Sheet 7.5
- [ ] All separator datasheets issued with governing criterion explicitly documented, so a later reviewer can see which check drove the final size

---

## 10. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Poor oil/water separation and carryover after startup | Separator sized for gas capacity only; liquid retention time never independently checked | Always calculate both criteria and compare — see Calc Sheet 7.1 and Case Study, Section 11 |
| Impractically long, slender vessel proposed early in a project | Diameter fixed by gas capacity alone, length then driven up by liquid holdup without revisiting diameter | Iterate diameter against L/D target once both criteria are known, as in Calc Sheet 7.1's Step 7 |
| Mesh pad mist eliminator fouled quickly in service | Mesh pad selected by default without checking the fluid's fouling tendency | Evaluate vane pack or cyclonic internals for fouling-prone services (companion Flow Assurance guide) |
| Compressor suffered liquid-related damage despite an "adequately sized" suction scrubber | Scrubber passed a generic Souders-Brown check but didn't meet the compressor OEM's specific carryover spec | Always confirm against OEM-specific carryover requirements, not just the generic K-value check — see Calc Sheet 7.4 |
| Liquid seal lost (blown out) during an actual relief event | Seal drum diameter sized by rule of thumb without checking bubble-through velocity at the actual emergency flow rate | Explicitly calculate bubble-through velocity at the maximum credible flow, not just typical/average flow — see Calc Sheet 7.5 |

---

## 11. Case Study — Three-Phase Separator Undersized Because Only Gas Capacity Was Checked

> A composite, illustrative case study based on the type of finding commonly encountered during separator commissioning. Names, tag numbers, and figures are representative, not project-specific.

### 11.1 Background

V-300 (this guide's running example) was originally sized during an early design phase by an engineer focused primarily on the gas handling capacity of the unit — the project's gas rate was the headline design parameter for the broader facility, and the separator's gas-capacity (Souders-Brown) sizing was performed carefully and correctly. Under schedule pressure, the liquid retention time check — a smaller, seemingly secondary calculation — was performed only as a rough confirmation that "the vessel looked big enough," without the full independent calculation and diameter iteration worked through in this guide's Calc Sheet 7.1.

### 11.2 Problem Identified

During commissioning, operations reported poor oil/water separation performance — the water outlet carried a persistent oil sheen, and the oil outlet showed higher-than-expected water content (basic sediment and water, BS&W) above the sales specification. Level control was also difficult to stabilize, with the interface level transmitter showing erratic behavior.

### 11.3 Investigation & Recalculation

The process engineering team reran the full sizing calculation using this guide's Calc Sheet 7.1 methodology and found that the as-built vessel (sized primarily against gas capacity, with the diameter effectively fixed by that criterion alone) provided **meaningfully less liquid retention time than intended** — the actual installed liquid volume, at the as-built diameter, was smaller than the 87.75 ft³ (5-minute-per-phase) target, since the diameter had never been revisited once the liquid holdup calculation was performed only as an approximate check rather than a full independent sizing pass. The shorter effective retention time was insufficient for the oil/water phases to fully separate before reaching their respective outlets, explaining both the carryover and the difficult-to-control interface level (a shorter, more turbulent liquid section is inherently harder to control stably).

### 11.4 Root Cause

Two compounding root causes were identified:
1. **Liquid retention time was treated as a confirmatory check rather than an independent sizing calculation** — the team's attention was appropriately focused on the gas capacity criterion (given the project's gas-rate-driven framing), but this created a bias toward treating the liquid-side calculation as secondary, rather than recognizing (as this guide's Section 1's opening practical note states) that either criterion can govern.
2. **No standard procedure required both criteria to be calculated to completion and explicitly compared**, with the diameter iterated if needed — the project's separator sizing checklist (where one existed) did not explicitly call out this comparison as a mandatory step with a documented governing-criterion conclusion.

### 11.5 Resolution

- Given the vessel was already fabricated and installed, the immediate resolution focused on operational mitigation: reducing throughput to increase effective retention time (accepting reduced production temporarily) and optimizing the interface level control tuning within the vessel's actual (undersized) liquid capacity.
- A future debottlenecking project was scoped to either replace V-300 with a correctly-sized vessel or add a downstream coalescer/polishing step to compensate for the retention time shortfall — both options representing real, avoidable capital cost compared to correct original sizing.
- The company's separator design procedure was updated to require: **both gas capacity and liquid retention time must be calculated to completion, independently, with the governing criterion explicitly documented on the datasheet** (consistent with this guide's Section 8.1 datasheet field) — and any case where gas capacity alone would produce an L/D ratio outside the practical 3:1–5:1 range must trigger an explicit re-evaluation of whether liquid holdup is actually governing, exactly as Calc Sheet 7.1 works through.

### 11.6 Outcome

- The interim throughput reduction had a real, ongoing production impact until the debottlenecking project could be executed — a direct, quantifiable cost of the original sizing gap.
- The finding was documented as a corporate lessons-learned item, reinforcing that a headline project parameter (here, gas rate) can create an unintentional bias toward treating that criterion's calculation as the "real" sizing exercise and other criteria as secondary confirmation — a bias that separator sizing, with its two genuinely independent and either-can-govern criteria, is particularly exposed to.

### 11.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A project's headline design parameter (e.g., gas rate) can create a bias toward under-investing in the calculation of a secondary-seeming criterion (liquid retention time) that can still govern | Explicitly require both criteria to be calculated to completion and compared, regardless of which one the project's framing emphasizes |
| An L/D ratio outside the practical range, discovered only after fixing diameter by one criterion, is a signal the other criterion may actually govern | Treat an out-of-range L/D as a trigger for re-evaluating and iterating diameter, not just a note to shorten or lengthen the vessel |
| Correcting an undersized separator after fabrication is far costlier than sizing it correctly from both criteria the first time | Apply the same rigor to liquid retention time as to gas capacity, given the real downstream cost of getting either one wrong |
| The governing criterion should be explicitly documented, not left implicit | Add a mandatory "governing criterion" field to every separator datasheet, so future reviewers can see which check actually drove the final size |

---

## 12. Reference Standards

- **API 12J** — Specification for Oil and Gas Separators
- **ASME BPVC Section VIII** — Rules for Construction of Pressure Vessels
- **API 614** — Lubrication, Shaft-Sealing, and Oil-Control Systems and Auxiliaries for Petroleum, Chemical and Gas Industry Services (compressor auxiliaries, including suction scrubbers)
- Manufacturer/vendor data (e.g., Otto York or equivalent) — mist eliminator (mesh pad, vane pack, cyclonic) performance data

---

*This guide is a practical study reference combining standard separator design methodology with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific fluid properties, the current edition of API 12J, and vendor-confirmed internals performance. This guide should be read alongside the companion Steady-State Simulation, Compressor Settle-Out Calculations, Flare Network Design, and Flow Assurance study guides, since the separators developed here directly feed the compressor suction, flare, and downstream equipment those guides depend on.*
