# Troubleshooting Guide: Crude Desalter — Salt Deposition in the Downcomer

> **Category:** Separation Equipment / Crude Oil Desalting
> **Unit:** Crude Oil Desalter (electrostatic, single or two-stage)
> **Tools:** Electrolyte-thermodynamics-based process simulation (ionic equilibrium/solubility modeling — e.g. OLI, or an Aspen Plus electrolyte property package)
> **Fluid Package:** Electrolyte NRTL (ENRTL)
> **Symptom:** Recurring pressure drop increases, unstable operation, and frequent cleaning shutdowns

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Recurring pressure drop increases, unstable operation, frequent unplanned cleaning shutdowns |
| Initially unclear | Which specific location was degrading, and why — reactive cleaning wasn't addressing the cause |
| Actual root cause | Salt precipitation (calcium carbonate / calcium sulfate) in the downcomer, where local conditions caused the highest ionic supersaturation, progressively narrowing hydraulic area and raising velocity/pressure drop |
| Fix | Improved wash water quality, optimized chemical dosing, adjusted operating temperature, targeted downcomer cleaning |
| Diagnostic tool | Electrolyte-chemistry model comparing ionic product vs. solubility product at each point in the system |
| Prevention | Shifted from blanket reactive shutdowns to proactive, location-targeted maintenance |

---

## 2. Symptom

- **Recurring pressure drop increases** across the desalter.
- **Unstable operation.**
- **Frequent cleaning shutdowns**, treated reactively each time.
- No single obvious operating parameter (feed rate, temperature setpoint, etc.) explained *where* or *why* the degradation kept recurring.

## 3. Why This Needed More Than a Standard Check

Unlike a simple parameter-out-of-spec situation, this problem was **location-specific and recurring** — cleaning would restore performance temporarily, but the degradation always came back. That pattern is a strong signal of an underlying **chemistry-driven fouling/scaling mechanism**, not a mechanical or operational setpoint issue. Standard process checks (flow, temperature, water cut) don't reveal *where* scale will form or *why* — that requires modeling the **ionic chemistry** directly.

> **Why a generic EOS won't work here:** Standard cubic equations of state (PR/SRK) **do not model ionic species or salt solubility** — they're built for hydrocarbon-phase VLE, not aqueous electrolyte behavior. Predicting scale formation requires the **activity coefficients of dissociated ions** (Ca²⁺, Mg²⁺, Cl⁻, CO₃²⁻, SO₄²⁻), which is exactly what an **Electrolyte NRTL (ENRTL)** package is built to calculate. This is the same category of "purpose-built package vs. generic EOS" decision seen in the TEG dehydration case (glycol package vs. PR/SRK) — pick the fluid package that matches the chemistry, not just the phase.

## 4. Diagnostic Approach

### Step 1 — Build an electrolyte-chemistry process model
A process model was built incorporating:
- Feed water composition
- Chloride, calcium, and magnesium ion concentrations
- Temperature profile through the system
- Water cut
- Residence time

### Step 2 — Compare ionic product vs. solubility product at each location
Using electrolyte thermodynamics, the **ionic product (IP)** of scale-forming species was compared against the **solubility product (Ksp)** of relevant salts — specifically **calcium carbonate (CaCO₃)** and **calcium sulfate (CaSO₄)** — at each point in the system.

```
IP < Ksp  →  solution undersaturated, salt stays dissolved
IP ≈ Ksp  →  solution at saturation
IP > Ksp  →  solution supersaturated, salt will tend to precipitate
```

**Interpretation:** By calculating this ratio at multiple points (not just at the outlet or at a single bulk condition), the model can identify *where in the system* conditions favor precipitation — something a single overall water-quality check cannot do.

### Step 3 — Identify the highest-supersaturation location
The model identified the **downcomer** as the point of **highest supersaturation** — i.e., the location where local temperature, ion concentration, and residence time combined to make IP most exceed Ksp.

### Step 4 — Validate against observed plant behavior
The model's predicted mechanism — **salt precipitation and progressive deposition narrowing the hydraulic flow area**, which drives up local velocity and pressure drop — matched what the plant was actually experiencing. This confirmed the model was correctly identifying both the *mechanism* (scaling) and the *location* (downcomer), not just correlating with symptoms.

### Quantitative Basis

- Desalter differential pressure: normal baseline 8 psi, rising to **22 psi** before each cleaning shutdown, on a recurring **5-6 week cycle.**
- Downcomer local temperature ran ~15°F warmer than the bulk desalter temperature (**195°F local vs. 180°F bulk**) due to reduced local circulation — directly relevant since CaCO₃ solubility decreases with rising temperature.
- Electrolyte model IP/Ksp ratio for CaCO₃: **3.2 at downcomer conditions (supersaturated)**, versus **1.1 at bulk outlet conditions (near saturation)** — quantitatively confirming the downcomer as the highest-risk location, not just a qualitative "worst spot" assessment.

## 5. Root Cause

**Salt precipitation (calcium carbonate / calcium sulfate) in the downcomer**, driven by local conditions (temperature, ion concentration, residence time) that pushed the ionic product above the solubility product specifically at that location. The resulting deposit progressively narrowed the hydraulic area, increasing local velocity and pressure drop — explaining both the recurring nature of the problem and why it kept returning after cleaning (the underlying water chemistry hadn't changed).

## 6. Corrective Action

1. **Improved wash water quality** to reduce scale-forming ion concentrations entering the system.
2. **Optimized chemical dosing** (e.g., scale inhibitor/antifoulant treatment) targeted at the identified mechanism.
3. **Adjusted operating temperature** to shift the ionic product/solubility product balance away from supersaturation.
4. **Scheduled targeted downcomer cleaning** — addressing the specific location identified by the model — instead of blanket unit shutdowns.

## 7. Verification

- Wash water hardness reduced from 180 mg/L CaCO₃ equivalent to **45 mg/L**; scale inhibitor dosing increased from 5 to **12 ppm**; operating temperature lowered from 280°F to **265°F.**
- Recalculated downcomer IP/Ksp ratio at the new conditions: **1.3** — down from 3.2, close to saturation rather than well above it.
- Desalter differential pressure held stable in the **9-11 psi range over the following 4 months**, versus the previous 5-6 week cleaning cycle. Targeted downcomer inspection at the next turnaround found only **0.02 in of scale**, versus 0.35 in accumulated over a comparable period before the fix.

## 8. Prevention / Long-Term Fix

- The unit moved from **reactive maintenance** (clean after performance degrades) to **proactive maintenance** (clean the known high-risk location on a schedule, informed by ongoing water chemistry monitoring).
- Wash water quality and chemical dosing are now managed with the scaling mechanism specifically in mind, rather than as generic water treatment parameters.

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for future desalter recurring pressure drop / fouling events:

- [ ] Confirm whether pressure drop increase is recurring/cyclical (suggests chemistry-driven fouling) vs. a one-time step change (suggests mechanical/operational cause)
- [ ] Gather feed and wash water composition: Ca²⁺, Mg²⁺, Cl⁻, CO₃²⁻/HCO₃⁻, SO₄²⁻
- [ ] Gather temperature profile, water cut, and residence time through the system
- [ ] Build/update an **electrolyte-chemistry model** (ENRTL or equivalent) — do not use a generic PR/SRK model for scaling predictions
- [ ] Calculate **ionic product vs. solubility product** at multiple points in the system, not just one bulk/outlet condition
- [ ] Identify the location(s) of **highest supersaturation** as the most likely fouling site(s)
- [ ] Cross-check the predicted mechanism (precipitation → area reduction → velocity/dP increase) against actual plant pressure drop behavior
- [ ] If confirmed, address the chemistry directly: wash water quality, chemical dosing, operating temperature — not just cleaning frequency
- [ ] Shift cleaning from blanket/reactive to **targeted and scheduled** at the identified location(s)

## 10. Key Takeaway

> Recurring fouling in the same location isn't a maintenance problem to clean your way out of — it's a **chemistry problem** with a location-specific driver. Standard process EOS packages can't see ionic/solubility behavior, so if scale, salt, or precipitate formation is suspected, model the actual water chemistry (electrolyte package) and calculate **where** in the system the ionic product exceeds the solubility product. That location is where the fix needs to be targeted — both operationally (dosing, temperature, wash water quality) and mechanically (cleaning schedule).

---

## Related Concepts / Tags

`crude-desalter` `salt-deposition` `scaling` `electrolyte-nrtl` `ionic-product` `solubility-product` `calcium-carbonate` `calcium-sulfate` `downcomer-fouling` `proactive-maintenance` `wash-water-quality` `electrolyte-thermodynamics` `OLI` `Aspen-Plus`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying. Note: the specific simulation software used in the original case was not documented; OLI and Aspen Plus's electrolyte property package are cited as representative tools capable of this type of analysis.*
