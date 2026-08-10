# 🛢️ Flow Assurance — Practical Study Guide

> A field-oriented reference covering the core engineering topics in flow assurance for subsea and long-distance pipeline systems — combining industry-standard theory with worked sample calculations, sample datasheets, and design-basis assumptions drawn from real project execution.

**Illustrative project used throughout this guide:** a subsea gas-condensate tieback (wellhead to host platform), with produced water, sand potential, and a compositionally rich fluid prone to hydrate, wax, and CO₂ corrosion risk. All numbers below are worked sample calculations for study purposes — always replace with project-specific PVT, water chemistry, and flow simulation data.

---

## 📑 Table of Contents

1. [Design Basis & Assumptions](#1-design-basis--assumptions)
2. [Hydrate Formation](#2-hydrate-formation)
3. [Wax Deposition](#3-wax-deposition)
4. [Asphaltene Precipitation](#4-asphaltene-precipitation)
5. [Scale Formation](#5-scale-formation)
6. [Corrosion & Erosion](#6-corrosion--erosion)
7. [Multiphase Flow & Transient Operations](#7-multiphase-flow--transient-operations)
8. [Sample Calculation Sheets](#8-sample-calculation-sheets)
9. [Sample Datasheets](#9-sample-datasheets)
10. [Practical Design Checklist](#10-practical-design-checklist)
11. [Common Field Issues & Lessons Learned](#11-common-field-issues--lessons-learned)
12. [Case Study — Subsea Tieback Hydrate Blockage on Emergency Shutdown](#12-case-study--subsea-tieback-hydrate-blockage-on-emergency-shutdown)
13. [Reference Standards](#13-reference-standards)

---

## 1. Design Basis & Assumptions

Flow assurance basis is normally issued as a **"Flow Assurance Design Basis & Philosophy"** document, frozen before pipeline thermal design, chemical injection sizing, and dynamic (OLGA/PIPESIM) simulation begin. Revisiting fluid composition, water cut, or thermal targets mid-project is a major source of rework — it changes insulation thickness, chemical injection tie-in sizing, and sometimes pipeline metallurgy.

### 1.1 Field & Fluid Basis (illustrative project)
| Parameter | Value | Notes |
|---|---|---|
| Tieback length | 25 km | Wellhead to host platform |
| Water depth | 1,200 m | Seabed ambient ≈ 4 °C (39 °F) year-round |
| Reservoir fluid type | Gas-condensate, rich in C2–C5 | GOR ≈ 15,000 scf/bbl |
| Flowing wellhead pressure/temperature | 3,500 psia / 160 °F (71 °C) | Declines with reservoir depletion — check end-of-field-life case too |
| Arrival pressure/temperature at host (normal flow) | 1,500 psia / 140 °F (60 °C) | — |
| Produced water cut (initial → late life) | 5% → 40% | Late-life case often governs hydrate/scale/corrosion risk |
| CO₂ content | 5 mol% | Governs corrosion basis |
| H₂S content | 50 ppm | Sour service screening required (NACE MR0175/ISO 15156) |
| Sand production potential | Trace, screened wells | Erosion basis uses a low but non-zero sand rate |
| Wax Appearance Temperature (WAT) | 100 °F (37.8 °C) | From lab (cold-finger/DSC) testing on live/dead oil |
| Asphaltene onset pressure (AOP) | ~2,800 psia at reservoir temp | From lab PVT/gravimetric titration |

### 1.2 Codes & Standards / Methodology Basis
- **Hydrate:** Multiflash/PVTsim or CSMHyd-type thermodynamic hydrate modeling for the equilibrium curve; **Hammerschmidt equation** for quick-check inhibitor dosage (Section 8.2)
- **Wax:** Lab WAT/pour point testing; steady-state and transient thermal simulation (OLGA/PIPESIM) for cooldown; **lumped-capacitance screening calc** for first-pass insulation sizing (Section 8.3)
- **Asphaltene:** Lab asphaltene onset pressure (AOP) envelope; compositional simulation for pressure-depletion trajectory
- **Scale:** Produced/injection water compatibility studies; saturation ratio / scaling indices (Stiff-Davis, Langelier, or direct ion-product-vs-Ksp screening, Section 8.6)
- **Corrosion:** NORSOK M-506 or de Waard-Milliams CO₂ corrosion prediction models; NACE MR0175/ISO 15156 for sour service material selection
- **Erosion:** **API RP 14E** erosional velocity guideline (screening); DNV RP O501 for detailed sand-erosion rate prediction
- **Multiphase/transient:** OLGA, PIPESIM, LedaFlow, or CFD for slugging, restart, and blowdown transient prediction

### 1.3 Key Design Assumptions (typical, to be confirmed per project)
| Assumption | Typical Value | Basis / Justification |
|---|---|---|
| Hydrate subcooling safety margin | 3–5 °F (1.5–3 °C) additional beyond the calculated suppression requirement | Company philosophy; accounts for model/measurement uncertainty |
| Methanol density | 0.792 kg/L | Standard reference value |
| Required no-flow (shut-in) protection time before wax/hydrate risk | 6 hours (planned), longer for unplanned per project philosophy | Confirm with Operations — drives insulation/active heating basis |
| API RP 14E erosional velocity constant, C | 100 (continuous service, solids present) | API RP 14E; C=125–150 sometimes used for solids-free/intermittent service — confirm basis |
| CO₂ corrosion inhibitor efficiency (design) | 90–95% | Vendor qualification testing required; do not assume without data |
| Corrosion allowance | 3 mm | Project material spec |
| Design life | 25 years | Project spec |
| Scale inhibitor squeeze lifetime (design) | 6–12 months between treatments | Confirm with produced water forecast and well intervention plan |

> ⚠️ **Practical note:** Every flow assurance discipline above interacts with the others — insulation added for wax control also slows the hydrate cooldown clock (helps), but a corrosion-inhibitor film can be stripped by high-velocity erosive flow (hurts). Always review the design basis as an integrated package, not as six independent checklists.

---

## 2. Hydrate Formation

### 2.1 Cause
Water + light hydrocarbon gas at **high pressure and low temperature** forms ice-like crystalline structures (clathrates) that can plug pipelines, chokes, and subsea equipment — even at temperatures well above 0 °C, since hydrate formation is pressure-dependent, not just temperature-dependent.

### 2.2 Prevention Methods
| Method | Mechanism | Typical Use |
|---|---|---|
| **Thermodynamic inhibitors** (methanol, MEG) | Shift the hydrate equilibrium curve to lower temperature/higher pressure (freezing-point-depression-like effect) | Continuous injection or batch dosing for shut-in/restart protection |
| **Low-dosage hydrate inhibitors (LDHI)** | Kinetic inhibitors (delay nucleation) or anti-agglomerants (prevent crystal bonding) — effective at much lower dose than thermodynamic inhibitors | Systems with moderate subcooling where full thermodynamic inhibition is uneconomical |
| **Insulation and heating** | Keep fluid temperature above the hydrate curve for as long as practical (passive insulation) or indefinitely (active heating/electrical trace heating, hot-water circulation) | Standard for subsea tiebacks; often combined with chemical injection for shut-in events beyond insulation's no-flow protection time |

### 2.3 Key Calculations
- **Hammerschmidt equation** — quick-check inhibitor dosage for a required hydrate suppression temperature (Section 8.2).
- **Subcooling margin analysis** — the difference between the hydrate equilibrium temperature (at operating pressure) and the actual fluid temperature; a positive subcooling margin (fluid colder than the hydrate curve) indicates the system is inside the hydrate-risk region (Section 8.1).

---

## 3. Wax Deposition

### 3.1 Cause
Crude oil cools below its **Wax Appearance Temperature (WAT)** — the temperature at which dissolved paraffins begin crystallizing out of solution — leading to wax deposition on cold pipe walls, progressively restricting flow area.

### 3.2 Controls
| Method | Notes |
|---|---|
| **Pour-point depressants (PPD)** | Modify wax crystal structure to reduce pour point / improve low-temperature flowability; do not eliminate deposition risk on their own |
| **Wax inhibitors** | Reduce deposition rate/adhesion; efficacy is fluid-specific — always lab-test with the actual (or representative) crude |
| **Pigging** | Mechanical removal of accumulated wax; pigging frequency is a key operating parameter derived from deposition-rate modeling |
| **Insulation** | Keeps fluid temperature above WAT for longer, both during normal flow (steady-state heat loss) and during shut-in (transient cooldown) — see Calc Sheet 8.3 |

### 3.3 Design Focus
Thermal management is the primary design lever for subsea tiebacks and long pipelines — insulation thickness/type (wet insulation, pipe-in-pipe, or active heating) is sized against both the **steady-state** arrival temperature target and the **transient no-flow cooldown time** requirement (Calc Sheet 8.3 works through both).

---

## 4. Asphaltene Precipitation

### 4.1 Cause
Asphaltenes are colloidally stabilized heavy fractions in crude oil; they precipitate when that stability is disrupted by:
- **Pressure drop** — most commonly, crossing below the **Asphaltene Onset Pressure (AOP)** during production (pressure depletion can move the operating point through the unstable region before eventually re-stabilizing at very low pressure)
- **Blending** — mixing crudes of different asphaltene stability (common risk when commingling production streams or during tanker blending)
- **Composition changes** — gas injection (miscible EOR), CO₂ breakthrough, or changing GOR over field life

### 4.2 Controls
| Method | Notes |
|---|---|
| **Asphaltene inhibitors** | Chemical dispersants/stabilizers, typically continuously injected downhole or at the wellhead; must be lab-qualified against the specific crude — poor inhibitor selection can *promote* rather than prevent precipitation |
| **Dispersants** | Keep precipitated particles suspended/small rather than allowing agglomeration and deposition |
| **Pressure management** | Choke/wellhead pressure management to avoid dwelling in the unstable pressure window where practical |

### 4.3 Difference from Wax
| | Wax | Asphaltenes |
|---|---|---|
| Primary driver | **Temperature** (crosses WAT) | **Pressure/chemistry** (crosses AOP, or composition/blending shift) |
| Typical deposit location | Cold spots — seabed sections, risers near mudline | Near-wellbore, tubing, chokes — often where the *largest pressure drop* occurs, not necessarily the coldest point |
| Reversibility | Can partially re-dissolve on reheating | Precipitation is not simply temperature-reversible; requires pressure/composition to return toward the stable region |

---

## 5. Scale Formation

### 5.1 Cause
- **Produced water supersaturation** — as pressure/temperature change along the production path, dissolved mineral salts (commonly CaCO₃, CaSO₄, BaSO₄, SrSO₄) can exceed their solubility limit and precipitate.
- **Mixing of incompatible brines** — most notably seawater (rich in sulfate) mixing with formation water (rich in barium/strontium) during seawater injection for pressure support, producing highly insoluble BaSO₄/SrSO₄ scale.

### 5.2 Controls
- **Scale inhibitors** — continuous downhole/topside injection, or **squeeze treatments** (inhibitor is bullheaded into the near-wellbore formation and slowly produced back over weeks-to-months, providing extended protection without continuous topside injection infrastructure).
- Compatibility testing (mixing produced and injection water at reservoir conditions) is essential before committing to a waterflood scheme — see Calc Sheet 8.6 for a simplified saturation-ratio screening approach.

### 5.3 Risk
Scale plugs valves, chokes, and subsea equipment — often at the point of maximum pressure drop (chokes, safety valves) where flashing/temperature change most rapidly triggers precipitation, similar in that respect to asphaltenes.

---

## 6. Corrosion & Erosion

### 6.1 Corrosion
- **Sweet corrosion (CO₂):** Carbonic acid formed from dissolved CO₂ attacks carbon steel; rate is a strong function of CO₂ partial pressure, temperature, pH, and flow regime (Calc Sheet 8.5 works a simplified de Waard-Milliams example).
- **Sour corrosion (H₂S):** Forms iron sulfide scale (can be locally protective or locally aggressive depending on conditions) and introduces **sulfide stress cracking (SSC)** risk for susceptible materials — governed by NACE MR0175/ISO 15156 material selection rules, not just a corrosion-rate calculation.
- **Controls:** Material selection (carbon steel + inhibitor vs. corrosion-resistant alloy (CRA) cladding/lining), continuous corrosion inhibitor injection, and corrosion monitoring (coupons, ER/LPR probes, intelligent pigging).

### 6.2 Erosion
- High-velocity fluid carrying **sand or other solids** causes wall thinning, particularly at flow-direction changes (elbows, tees, chokes) where particle impingement is highest.
- **Controls:** Velocity limits (API RP 14E erosional velocity screening, Calc Sheet 8.4), pipe sizing (larger ID reduces velocity for the same volumetric flow), erosion-resistant materials/coatings, and blind-tee or long-radius-bend geometry at high-risk locations to reduce direct impingement.

> ⚠️ **Practical note:** Corrosion inhibitor film integrity and erosion are linked — flow velocities high enough to be erosion-risk are often also high enough to mechanically strip a corrosion inhibitor film, so an erosion check that "passes" on its own is not sufficient evidence that corrosion is also under control at the same location.

---

## 7. Multiphase Flow & Transient Operations

### 7.1 Slugging
Severe pressure/flow fluctuations caused by intermittent liquid accumulation and sweep-out along a pipeline — commonly **terrain-induced** (low points in an undulating seabed profile), **riser-induced** (severe slugging at the base of a riser), or **hydrodynamic** (Kelvin-Helmholtz instability at gas-liquid interfaces in near-horizontal flow). Slug catchers at the receiving facility are sized against the predicted slug volume/frequency from dynamic multiphase simulation.

### 7.2 Restart/Shut-in Risks
- **Hydrate plugs during cold restart** are one of the highest-consequence flow assurance risks — a shut-in pipeline cools toward seabed ambient temperature over time (Calc Sheet 8.3 methodology), and if the no-flow duration exceeds the calculated/inhibited protection time, restart must proceed with a hydrate-management plan (e.g., depressurization before restart, or confirmed inhibitor coverage) rather than simply reopening the well.
- **Practical experience:** Depressurizing a shut-in subsea pipeline (rather than restarting under full pressure) is a common hydrate-avoidance strategy — but depressurization itself causes further Joule-Thomson cooling, so the depressurization rate/target must be checked against the hydrate curve too, not assumed to be automatically safe.

### 7.3 Modeling Tools
| Tool | Typical Use |
|---|---|
| **OLGA** | Industry-standard transient multiphase flow simulator — slugging, cooldown, restart, pigging |
| **PIPESIM** | Steady-state and transient multiphase network simulation, well-to-facility |
| **CFD** | Detailed local flow prediction (e.g., erosion at a specific fitting, slug impact loading) where 1D network tools are insufficient |

---

## 8. Sample Calculation Sheets

> All calculations below use the illustrative project basis in Section 1. Values are for study purposes — verify against project-specific PVT/water-chemistry data and dynamic simulation.

### 8.1 Calc Sheet 1 — Hydrate Subcooling Margin

**Given:**
- Operating pressure at seabed cold spot, P = 1,500 psia
- Hydrate equilibrium temperature at this pressure (from thermodynamic hydrate model), T_hyd = 65 °F
- Actual flowing fluid temperature at this location, T_actual = 40 °F
- Required additional safety margin = 5 °F (Section 1.3 basis)

**Step 1 — Calculate subcooling (how far into the hydrate region the system currently sits):**
```
ΔT_subcool = T_hyd − T_actual = 65 − 40 = 25 °F
```
A positive value means the fluid is **25 °F colder** than the hydrate formation temperature at this pressure — the system is well inside the hydrate-risk region without inhibition.

**Step 2 — Determine target hydrate-curve temperature (with safety margin):**
```
T_hyd,target = T_actual − safety margin = 40 − 5 = 35 °F
```

**Step 3 — Required hydrate suppression (how far the inhibitor must shift the curve):**
```
ΔT_required = T_hyd − T_hyd,target = 65 − 35 = 30 °F
```

**Result:** The inhibitor system must be capable of suppressing the hydrate formation temperature by **30 °F** at this location. This value feeds directly into the Hammerschmidt dosage calculation (Calc Sheet 8.2).

> 📌 **Assumption check:** T_hyd should come from a compositional thermodynamic hydrate model (e.g., Multiflash), not a generic chart — hydrate curves are sensitive to gas composition (CO₂/H₂S content shifts the curve), and using a generic "sales gas" hydrate curve for a CO₂-rich stream can significantly under- or over-state the real risk.

---

### 8.2 Calc Sheet 2 — Methanol Dosage (Hammerschmidt Equation)

**Given (from Calc Sheet 8.1):**
- Required hydrate suppression, ΔT = 30 °F
- Hammerschmidt constant for methanol, K = 2,335 (°F basis)
- Methanol molecular weight, M = 32.04 g/mol
- Produced water rate = 50 bbl/day (late-life case per Section 1.3 is higher — this is an early-life illustrative case; repeat for the late-life 40% water-cut case in a real design)
- Methanol density = 0.792 kg/L

**Step 1 — Hammerschmidt equation, solved for required methanol wt% (W) in the free water phase:**
```
ΔT = (K × W) / [M × (100 − W)]

30 = (2,335 × W) / [32.04 × (100 − W)]
30 × 32.04 × (100 − W) = 2,335 × W
961.2 × (100 − W) = 2,335 W
96,120 − 961.2 W = 2,335 W
96,120 = 3,296.2 W
W ≈ 29.16 wt%
```

**Result:** The water phase must contain **≈29.2 wt% methanol** to achieve the required 30 °F suppression.

**Step 2 — Convert to mass injection rate:**
```
Water rate = 50 bbl/day × 0.159 m³/bbl × 1,000 kg/m³ ≈ 7,950 kg/day

W = M_methanol / (M_methanol + M_water) × 100
0.2916 = M_methanol / (M_methanol + 7,950)
M_methanol = 0.2916 × (M_methanol + 7,950)
M_methanol = 2,318.5 + 0.2916 M_methanol
0.7084 M_methanol = 2,318.5
M_methanol ≈ 3,273 kg/day
```

**Step 3 — Convert to volumetric injection rate:**
```
Volume = 3,273 kg/day ÷ 0.792 kg/L ≈ 4,133 L/day ≈ 26 bbl/day
```

**Result:** Required methanol injection rate ≈ **3.27 tonnes/day (≈26 bbl/day)** for this early-life water cut. This sizes the methanol storage, injection pump, and topside/umbilical tie-in capacity.

> 📌 **Assumption check:** This must be re-run for the **late-life water cut (40%)** per the design basis — at higher water cut, the same wt% target requires proportionally more methanol mass, and this late-life case is very often the one that actually governs storage/pump/umbilical sizing, not the early-life case shown here. Also confirm whether MEG (regenerable, lower OPEX for high water-cut systems) is more economical than once-through methanol for the late-life case — this is a common flow assurance economic trade-off study.

---

### 8.3 Calc Sheet 3 — Wax Cooldown / Insulation Screening (Lumped Capacitance Method)

**Given:**
- Fluid arrival temperature (start of shut-in), T_initial = 140 °F
- Seabed ambient temperature, T_amb = 40 °F
- Wax Appearance Temperature, WAT = 100 °F (Section 1.1 basis)
- Required no-flow protection time (Section 1.3 basis) = 6 hours
- Pipe: 8-in OD, 7.625-in ID; fluid density ρ = 50 lb/ft³, specific heat Cp = 0.5 Btu/(lb·°F)
- Base-case insulation overall heat transfer coefficient, U = 1.5 Btu/(hr·ft²·°F)

**Step 1 — Fluid heat capacity per unit pipe length:**
```
A_cross = (π/4) × (7.625/12)² = (π/4) × (0.6354)² ≈ 0.317 ft²
Mass per ft = ρ × A_cross = 50 × 0.317 ≈ 15.85 lb/ft
Heat capacity per ft, mCp = 15.85 × 0.5 ≈ 7.92 Btu/(ft·°F)
```

**Step 2 — Heat transfer area per unit length (based on OD):**
```
A_area = π × (8.625/12) ≈ 2.259 ft²/ft
```

**Step 3 — Overall UA per unit length and thermal time constant:**
```
UA = U × A_area = 1.5 × 2.259 ≈ 3.39 Btu/(hr·ft·°F)
τ = mCp / UA = 7.92 / 3.39 ≈ 2.34 hr
```

**Step 4 — Time to cool from T_initial to WAT (lumped-capacitance exponential decay):**
```
(T(t) − T_amb) / (T_initial − T_amb) = exp(−t/τ)
(100 − 40) / (140 − 40) = 60/100 = 0.6
t = −τ × ln(0.6) = 2.34 × 0.5108 ≈ 1.20 hours
```

**Result:** With the base-case insulation (U = 1.5), the fluid cools to WAT in only **≈1.2 hours** — far short of the **6-hour** required no-flow protection time. **FAIL.**

**Step 5 — Back-calculate the required U to meet the 6-hour target:**
```
τ_required = t_target / (−ln 0.6) = 6 / 0.5108 ≈ 11.75 hr
UA_required = mCp / τ_required = 7.92 / 11.75 ≈ 0.674 Btu/(hr·ft·°F)
U_required = UA_required / A_area = 0.674 / 2.259 ≈ 0.30 Btu/(hr·ft²·°F)
```

**Result:** Insulation must be upgraded to achieve **U ≈ 0.30 Btu/(hr·ft²·°F)** — roughly **5× better** than the base case — to meet the 6-hour no-flow protection target. This is consistent with the thicker syntactic-foam or pipe-in-pipe insulation systems commonly used on real subsea tiebacks, and confirms why insulation selection is a first-order cost/schedule driver rather than a minor detail.

> 📌 **Assumption check:** This lumped-capacitance method ignores pipe wall thermal mass and axial conduction/burial effects — it is a valid **first-pass screening** calc, but final insulation selection should be verified with a full transient thermal simulation (OLGA or equivalent) that also captures the temperature profile along the full pipeline length, not just a single representative point.

---

### 8.4 Calc Sheet 4 — Erosional Velocity Screening (API RP 14E)

**Given:**
- API RP 14E constant, C = 100 (continuous service, sand present, per Section 1.3 basis)
- Mixture density at flowing conditions, ρ_m = 25 lb/ft³
- Pipe: 6-in ID (0.5 ft)
- Volumetric flow at flowing conditions, Q = 25,000 ft³/hr = 6.94 ft³/s

**Step 1 — Erosional velocity limit:**
```
V_e = C / √ρ_m = 100 / √25 = 100 / 5 = 20 ft/s
```

**Step 2 — Actual velocity in the 6-in line:**
```
A = (π/4) × (0.5)² = 0.1963 ft²
V_actual = Q / A = 6.94 / 0.1963 ≈ 35.4 ft/s
```

**Step 3 — Compare:**
```
V_actual (35.4 ft/s) > V_e (20 ft/s)  →  FAIL — erosion risk
```

**Step 4 — Required pipe area/diameter to meet the erosional limit:**
```
A_required = Q / V_e = 6.94 / 20 = 0.347 ft²
D_required = √(4 × A_required / π) = √(0.4415) ≈ 0.664 ft ≈ 7.97 in
```

**Result:** The 6-inch line exceeds the API RP 14E erosional velocity limit; upsizing to **≈8-inch ID** brings velocity within the guideline.

> 📌 **Assumption check:** API RP 14E is a **screening** guideline, not a rate-of-metal-loss prediction — a line that "passes" the C-factor check can still erode over time if sand production is higher than assumed. For any non-trivial sand rate, follow up with a quantitative erosion model (e.g., DNV RP O501) at the specific fittings/bends of concern, not just the straight-run check shown here.

---

### 8.5 Calc Sheet 5 — CO₂ Corrosion Rate Screening (de Waard-Milliams)

**Given:**
- Flowing temperature, T = 60 °C = 333 K
- Total pressure = 50 bar, CO₂ content = 5 mol% → partial pressure of CO₂, p(CO₂) = 0.05 × 50 = 2.5 bar
- Simplified de Waard-Milliams correlation (screening only — does not include pH, flow-regime, or glycol/corrosion-inhibitor correction factors used in the full model)

**Step 1 — Apply the correlation:**
```
log(CR) = 5.8 − 1,710/T − 0.67 × log[p(CO₂)]

1,710 / 333 = 5.135
log(2.5) = 0.398
0.67 × 0.398 = 0.267

log(CR) = 5.8 − 5.135 − 0.267 = 0.398
CR = 10^0.398 ≈ 2.50 mm/year
```

**Result:** Uninhibited CO₂ corrosion rate ≈ **2.5 mm/year** — high, and unacceptable against a 3 mm total corrosion allowance over a 25-year design life without mitigation.

**Step 2 — Apply design corrosion inhibitor efficiency (90%, Section 1.3 basis):**
```
CR_inhibited = CR × (1 − 0.90) = 2.5 × 0.10 = 0.25 mm/year
```

**Step 3 — Compare cumulative loss against corrosion allowance:**
```
Cumulative loss over 25 years = 0.25 × 25 = 6.25 mm
Corrosion allowance = 3 mm
6.25 mm > 3 mm  →  FAIL, even with a 90% efficient inhibitor
```

**Result:** Even with a 90%-efficient corrosion inhibitor, the projected cumulative loss (6.25 mm) **exceeds** the 3 mm corrosion allowance over the design life. Mitigation options: qualify a higher-efficiency inhibitor (≥95%, giving 3.13 mm — still marginal), use corrosion-resistant alloy (CRA) cladding/lining for at least the highest-risk sections (e.g., near the choke where the largest pressure/temperature change occurs), or increase the base wall thickness/corrosion allowance.

> 📌 **Assumption check:** This screening correlation is uncorrected for pH, flow regime, and protective scale formation, all of which the full de Waard-Milliams/NORSOK M-506 models account for — treat this as a **first-pass red-flag screening tool**, not a final material-selection basis. A rich CO₂/temperature combination that screens this poorly should always trigger a full corrosion study before finalizing material selection.

---

### 8.6 Calc Sheet 6 — Scale Formation Screening (Saturation Ratio)

**Given:**
- Produced water Ca²⁺ concentration = 0.01 mol/L
- Produced water CO₃²⁻ concentration (from alkalinity/pH) = 2 × 10⁻⁵ mol/L
- Solubility product of CaCO₃ at reservoir/flowline temperature, Ksp ≈ 3.3 × 10⁻⁹

**Step 1 — Calculate the ion product (IP):**
```
IP = [Ca²⁺] × [CO₃²⁻] = 0.01 × 2×10⁻⁵ = 2×10⁻⁷
```

**Step 2 — Calculate the saturation ratio (SR):**
```
SR = IP / Ksp = (2×10⁻⁷) / (3.3×10⁻⁹) ≈ 60.6
```

**Result:** SR ≈ **60.6** — since SR ≫ 1, the water is **severely supersaturated** with respect to CaCO₃, confirming a strong scaling tendency and the need for continuous scale inhibitor injection (or squeeze treatment) at the predicted precipitation location (commonly the choke or other high pressure-drop point where CO₂ flashing raises pH and drives CaCO₃ precipitation).

> 📌 **Assumption check:** This simplified ion-product screening ignores activity coefficients/ionic strength effects, which matter more at high total dissolved solids (TDS) — for produced/seawater-mixing systems with high TDS, use a full geochemical model (Stiff-Davis Index for high-salinity brines, or software such as ScaleChem/PHREEQC) rather than this simplified check for the final inhibitor-selection basis. This calc is a good, fast **red-flag screening tool**, not a design-basis-grade result.

---

## 9. Sample Datasheets

### 9.1 Chemical Injection (Methanol / LDHI) Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Tag No.** | CIP-301 (Methanol Injection Package) | — |
| **Service** | Hydrate Inhibition — Continuous & Batch | — |
| **Chemical** | Methanol (MeOH), 99.9% | — |
| **Design Injection Rate (early-life)** | 26 (per Calc Sheet 8.2) | bbl/day |
| **Design Injection Rate (late-life, 40% WC)** | To be recalculated per Calc Sheet 8.2 method | bbl/day |
| **Storage Capacity** | 14 days at late-life rate | — |
| **Injection Pressure** | 3,800 (above max wellhead pressure + margin) | psig |
| **Injection Points** | Subsea tree (downhole/wellhead), umbilical-fed | — |
| **Pump Type** | Triplex positive displacement, duty/standby | — |
| **Turndown** | 10:1 | — |
| **Materials of Construction** | 316L SS (methanol-compatible wetted parts) | — |
| **LDHI Backup System** | Yes — anti-agglomerant, for moderate-subcooling normal operation | — |
| **Applicable Standard** | API RP 14E (piping), project chemical injection philosophy | — |

---

### 9.2 Pipeline Thermal Insulation Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **Line No.** | FL-201 (Wellhead to Riser Base) | — |
| **Nominal Size** | 8 | in |
| **Insulation Type** | Multi-layer syntactic polyurethane foam, pipe-in-pipe | — |
| **Design Overall U-value** | 0.30 (per Calc Sheet 8.3) | Btu/(hr·ft²·°F) |
| **Required No-Flow Protection Time** | 6 | hours |
| **Arrival Temperature (steady-state, design flow)** | 140 | °F |
| **Ambient (Seabed) Temperature** | 40 | °F |
| **WAT** | 100 | °F |
| **Hydrate-Curve Temperature (at line pressure)** | 65 | °F |
| **Active Heating System** | Electrical trace heating, standby (beyond 6-hr passive protection) | — |
| **Insulation Design Life** | 25 | years |
| **Applicable Standard** | Project thermal design philosophy, DNV-RP-F113 (deepwater pipeline insulation) | — |

---

### 9.3 Corrosion & Erosion Monitoring Datasheet

| Parameter | Value | Unit |
|---|---|---|
| **System** | Flowline FL-201, Wellhead to Host | — |
| **CO₂ Partial Pressure (design)** | 2.5 (per Calc Sheet 8.5) | bar |
| **Uninhibited Corrosion Rate (screening)** | 2.5 | mm/year |
| **Design Inhibitor Efficiency (required)** | ≥ 95% (per Calc Sheet 8.5 result) | % |
| **Corrosion Allowance** | 3 | mm |
| **Material — General Flowline** | Carbon steel + corrosion inhibitor | — |
| **Material — High-Risk Sections (choke, near-wellhead)** | CRA-clad (e.g., 316L or Alloy 825 liner) | — |
| **Erosional Velocity Limit (C=100 basis)** | 20 (per Calc Sheet 8.4) | ft/s |
| **Governing Line Size (post-erosion check)** | 8 (upsized from 6-in) | in |
| **Monitoring Method** | ER probes + intelligent pigging (every 3 years) | — |
| **Sour Service Screening** | Required — H₂S = 50 ppm, per NACE MR0175/ISO 15156 | — |

---

## 10. Practical Design Checklist

- [ ] Flow assurance design basis issued and approved (Section 1) before thermal/chemical injection sizing begins
- [ ] Hydrate equilibrium curve generated from compositional thermodynamic model (not a generic chart) — see Calc Sheet 8.1
- [ ] Subcooling margin calculated at all cold-spot locations, including late-field-life water-cut case
- [ ] Methanol/MEG or LDHI dosage sized for both early-life and late-life water cut — see Calc Sheet 8.2
- [ ] WAT and pour point confirmed by lab testing on representative fluid, not assumed from analog fields
- [ ] Steady-state AND transient (no-flow cooldown) insulation performance checked — see Calc Sheet 8.3
- [ ] Asphaltene onset pressure (AOP) envelope checked against the full pressure-depletion production trajectory, not just initial conditions
- [ ] Produced/injection water compatibility and scale saturation ratio screened — see Calc Sheet 8.6
- [ ] CO₂/H₂S corrosion basis established; sour service material screening (NACE MR0175/ISO 15156) completed if H₂S present
- [ ] Corrosion inhibitor efficiency requirement checked against corrosion allowance and design life — see Calc Sheet 8.5
- [ ] Erosional velocity checked at all line sizes and high-risk fittings (bends, chokes) — see Calc Sheet 8.4
- [ ] Slugging behavior modeled (OLGA/PIPESIM) and slug catcher sized against predicted volume/frequency
- [ ] Restart/shut-in hydrate management plan developed (depressurization philosophy, inhibitor pre-treatment, or both)
- [ ] Datasheets (chemical injection, insulation, corrosion/erosion monitoring) issued for vendor/EPC use

---

## 11. Common Field Issues & Lessons Learned

| Issue | Root Cause | Practical Fix |
|---|---|---|
| Hydrate plug formed during unplanned shutdown, despite "adequate" insulation on paper | Insulation was sized against steady-state arrival temperature only, not the transient no-flow cooldown time | Always run the transient cooldown check (Calc Sheet 8.3) against the actual required no-flow protection time, not just steady-state |
| Methanol storage/pump undersized within a few years of startup | Dosage sized only for early-life water cut | Size chemical injection systems for the late-life (highest water cut) case, per Calc Sheet 8.2 note |
| Unexpected wax buildup at a riser base rather than at the coldest seabed point | Deposition assumed to track ambient temperature alone; local flow regime/shear and cooling rate also matter | Use full thermal + deposition-rate simulation along the entire profile, not just the single coldest point |
| Asphaltene deposition found in tubing/choke despite "wax control" measures in place | Asphaltene and wax were treated as the same problem with the same controls | Recognize AOP is pressure/chemistry driven, not temperature driven — chase the pressure-depletion trajectory against the AOP envelope, not the temperature profile |
| Scale-related choke plugging shortly after seawater injection started | Produced/injection water compatibility not tested before commissioning | Run compatibility and saturation-ratio screening (Calc Sheet 8.6) before committing to any water injection scheme |
| Corrosion-related leak at a bend well before design life | Screening corrosion rate used but inhibitor efficiency assumed rather than lab-qualified, and erosion at the bend was stripping the inhibitor film | Lab-qualify actual inhibitor efficiency; check erosion and corrosion together at high-risk fittings, not independently |

---

## 12. Case Study — Subsea Tieback Hydrate Blockage on Emergency Shutdown

> A composite, illustrative case study based on the type of finding commonly encountered on subsea gas-condensate tiebacks following an unplanned shutdown. Names, tag numbers, and figures are representative, not project-specific.

### 12.1 Background

A subsea gas-condensate tieback (the illustrative project used throughout this guide) had been in operation for approximately 4 years. The original flow assurance design basis sized pipeline insulation and methanol injection using the early-life water cut (5%) and a 6-hour no-flow protection time, consistent with the project's original planned-shutdown philosophy. Methanol injection had never been required in normal operation, since steady-state arrival temperature stayed comfortably above WAT and the hydrate curve.

### 12.2 Problem Identified

An unplanned host platform trip caused an **8-hour** unplanned shutdown of flowline FL-201 — exceeding the original 6-hour design basis. By this point in field life, water cut had risen to approximately 35%, close to the late-life design case (40%), though the methanol system had never been re-verified against this updated water cut.

On restart, operations identified a **partial hydrate blockage** at the riser base, evidenced by an abnormal pressure differential across that section and a failed pigging attempt. Production was shut in for approximately 9 days while the blockage was managed (a combination of controlled depressurization from both ends and extended methanol circulation) before flow was safely re-established.

### 12.3 Investigation & Recalculation

The flow assurance team reran the cooldown and subcooling analysis using this guide's Calc Sheet 8.1 and 8.3 methodology:

- **Cooldown check (Calc Sheet 8.3 method):** Using the as-built insulation U-value against an 8-hour (not 6-hour) shut-in duration confirmed that fluid temperature at the riser base had fallen below the hydrate equilibrium temperature at the shut-in (static) pressure roughly **1.5 hours before** the platform trip was cleared and restart was attempted — the fluid had been in the hydrate-risk region for over 6 hours before restart procedures began.
- **Subcooling check (Calc Sheet 8.1 method):** At the actual shut-in pressure and the calculated riser-base temperature, subcooling was approximately **22 °F** — well beyond the small margin the original methanol philosophy assumed would be available "if needed," since the design basis had never actually required active methanol dosing during a credible shutdown scenario.
- **Root finding:** The design basis's 6-hour no-flow protection assumption had never been stress-tested against a realistic unplanned-shutdown duration distribution — 6 hours was the *planned* maintenance shutdown target, not a validated bound on all credible unplanned trips.

### 12.4 Root Cause

Two compounding root causes were identified:
1. **Design basis scope gap** — the 6-hour no-flow protection target was carried over from the planned-maintenance philosophy without a separate check against unplanned/emergency shutdown duration statistics (which, per the host platform's own trip history, included multiple prior events exceeding 6 hours).
2. **No active hydrate management procedure for shutdowns beyond 6 hours** — the operations team had a restart procedure for routine cases but no pre-established, pressure-tested depressurization/methanol-circulation procedure for an extended unplanned shutdown, costing valuable time during the actual event.

### 12.5 Resolution

- The flow assurance design basis was revised to size passive insulation (or add active heating) against the **credible unplanned shutdown duration** (revised to a 24-hour basis, based on the host platform's trip history) rather than only the 6-hour planned-maintenance target.
- A pre-approved **extended shutdown hydrate management procedure** was developed and drilled with operations, covering controlled depressurization targets and methanol circulation rates, so a future event would not require real-time engineering analysis under time pressure.
- The methanol system's dosage basis (Calc Sheet 8.2 methodology) was re-run against the current 35% water cut and confirmed adequate for pre-emptive dosing ahead of a planned/forecasted extended shutdown, but was flagged as **not** sized for continuous protection through an unlimited-duration unplanned event — reinforcing that depressurization, not indefinite methanol dosing, is the primary strategy for long unplanned shutdowns.

### 12.6 Outcome

- The 9-day production deferral had a significant, quantifiable revenue impact and prompted a company-wide review of flow assurance design-basis assumptions across other subsea assets with similar "planned-maintenance-only" no-flow protection targets.
- The finding was documented as a corporate lessons-learned item: no-flow protection time targets must be validated against **actual credible shutdown duration statistics** for the specific host facility, not adopted as a generic industry rule of thumb.

### 12.7 Case-Specific Lessons Learned

| Lesson | Applied Fix |
|---|---|
| A "planned maintenance" no-flow protection time target is not automatically valid for unplanned shutdown scenarios | Size insulation/heating against the host facility's actual credible unplanned-shutdown duration statistics, not just the planned-maintenance case |
| Methanol dosage basis must be re-verified as water cut rises through field life | Schedule periodic (e.g., annual) re-verification of Calc Sheet 8.2-style dosage checks against current water cut, not just at initial design |
| Time pressure during a real event leads to worse outcomes than a pre-drilled procedure | Develop and drill an extended-shutdown hydrate management procedure (depressurization targets, circulation rates) before it is needed |
| Depressurization, not indefinite chemical dosing, is the practical strategy for long unplanned shutdowns | State this explicitly in the design basis and operating philosophy so operations does not default to "just inject more methanol" as an open-ended strategy |

---

## 13. Reference Standards

- **API RP 14E** — Recommended Practice for Design and Installation of Offshore Production Platform Piping Systems (erosional velocity guideline)
- **NORSOK M-506** — CO₂ Corrosion Rate Calculation Model
- **NACE MR0175 / ISO 15156** — Petroleum and natural gas industries — Materials for use in H₂S-containing environments in oil and gas production (sour service)
- **DNV-RP-F113** — Pipeline Subsea Repair (referenced alongside general deepwater pipeline insulation/thermal design practice)
- **DNV RP O501** — Erosive Wear in Piping Systems
- Hammerschmidt, E.G. (1934) — original correlation for hydrate suppression by inhibitor concentration
- de Waard, C. & Milliams, D.E. (1975) — Prediction of Carbonic Acid Corrosion in Natural Gas Pipelines

---

*This guide is a practical study reference combining standard flow assurance design theory with worked sample calculations and lessons learned from real project experience. All numeric examples are illustrative — always validate against project-specific PVT/water-chemistry data, dynamic simulation results (OLGA/PIPESIM), and current regulatory/code requirements.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
