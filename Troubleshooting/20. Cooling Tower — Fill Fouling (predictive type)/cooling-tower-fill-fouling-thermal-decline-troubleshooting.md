# Troubleshooting Guide: Cooling Tower — Gradual Thermal Performance Decline from Fill Fouling

> **Category:** Utilities / Heat Rejection / Predictive Maintenance
> **Unit:** Mechanical-Draft Cooling Tower, Process Cooling Water Loop
> **Tools:** Cooling tower thermal performance rating (approach/range vs. wet-bulb temperature) with historical trending
> **Fluid Package:** Not applicable in the VLE sense — cooling tower performance uses psychrometric/wet-bulb correlations, not a phase-equilibrium flash
> **Symptom:** Cooling water supply temperature gradually rising relative to ambient wet-bulb temperature over several months

---

> **Note on case type:** Like the seawater cooler (Case Study 6) and crude preheat train (Case Study 15), this is a **predictive/quantitative trending** exercise, not a competing-hypothesis diagnosis.

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Cooling water supply temperature gradually rising relative to ambient wet-bulb temperature (approach widening) over several months |
| Task | Quantify the degradation and determine whether it was fill fouling, mechanical (fan/drift), or water treatment related |
| Actual root cause | Biological/scale fouling of the fill media, reducing air-water contact surface area and evaporative cooling effectiveness |
| Fix | Fill cleaning; water treatment program review (biocide/scale inhibitor dosing) |
| Diagnostic signal | Approach temperature (cold water temp minus wet-bulb) trending up steadily while fan performance and water flow remained normal |
| Prevention | Routine approach-temperature trending against wet-bulb; periodic fill inspection; water treatment program audits |

---

## 2. Symptom

- **Cooling water supply (cold water basin) temperature gradually rose relative to ambient wet-bulb temperature** over several months — i.e., the **approach temperature** (cold water temp − wet-bulb temp) widened steadily.
- This directly reduced cooling capacity available to downstream process exchangers.

## 3. Why This Needed Quantification, Not Just "Clean the Tower"

Cooling tower performance decline can come from several distinct causes — fan/mechanical issues, water treatment chemistry problems, or fill fouling — each requiring a different fix. Approach temperature alone doesn't say *which* of these is responsible; it just says performance has degraded. The task was to isolate the mechanism using proper thermal performance rating rather than defaulting to a general "clean everything" response.

## 4. Diagnostic Approach

### Step 1 — Confirm the trend using approach temperature, not raw cold water temperature alone
Raw cold water temperature naturally varies with ambient wet-bulb temperature day to day, so it isn't a reliable standalone indicator. **Approach temperature** (cold water temp minus wet-bulb temp) normalizes for weather and isolates tower performance specifically.

```
Approach = T(cold water)  −  T(wet-bulb, ambient)
```

Approach was trended over several months and confirmed a **steady, sustained widening** — not weather noise.

### Step 2 — Rule out mechanical/fan-side causes
Fan speed, motor amperage, and water circulation flow rate were reviewed and found to be at their normal/design values — ruling out a fan or water distribution mechanical issue as the primary driver.

### Step 3 — Inspect fill media condition
With mechanical parameters normal, attention turned to the **fill media** — the surface area that drives evaporative heat/mass transfer. Physical inspection found **biological growth and scale fouling** on the fill surfaces, reducing effective air-water contact area.

### Step 4 — Cross-check water treatment program history
Reviewing water treatment logs (biocide dosing, scale inhibitor dosing, cycles of concentration) helped confirm *why* fouling had developed — providing the basis for a longer-term fix rather than a one-time cleaning.

### Quantitative Basis

- Design approach: 5°F (78°F design wet-bulb, 83°F design cold water). Trended actual approach widened from a baseline **5.5°F to 11.2°F over 4 months** — more than double, at comparable wet-bulb conditions.
- Range (hot water minus cold water temperature) stayed within 1°F of its design 15°F value throughout, confirming the heat load/water flow split across the tower wasn't the driver — isolating the problem to the fill's air-water contact effectiveness specifically.
- Water treatment log review: cycles of concentration had drifted from a target of 4.0 to **6.5 cycles** (blowdown under-dosed), and free chlorine residual had fallen below the 0.3–0.5 ppm target to **<0.1 ppm on 60% of daily logs** over the same period.
- Fill inspection: biological slime layer and CaCO₃ scale were estimated (via wetted-surface visual assessment) to have reduced effective fill contact area by **roughly 30%.**

## 5. Root Cause

**Biological and scale fouling on the cooling tower fill media** reduced the effective air-water contact surface area, degrading evaporative cooling effectiveness and widening the approach temperature — even though fan and water circulation systems remained mechanically normal.

## 6. Corrective Action

1. **Cleaned the fill media** to remove biological growth and scale.
2. **Reviewed and adjusted the water treatment program** (biocide/scale inhibitor dosing, cycles of concentration) to address the underlying conditions that allowed fouling to develop.

## 7. Verification

- Approach temperature returned to **5.8°F within one week** of fill cleaning — close to the 5.5°F baseline.
- Cycles of concentration corrected back to **4.2** and chlorine residual restored to the **0.3–0.5 ppm** target range.
- Approach held in the **5.3–6.1°F band over the following 60 days**, confirming a durable fix rather than a temporary post-cleaning improvement.

## 8. Prevention / Long-Term Fix

- Established **routine approach-temperature trending against wet-bulb temperature** as the standard performance monitoring parameter, rather than relying on raw cold water temperature.
- Added **periodic fill inspection** to the maintenance plan.
- Instituted **water treatment program audits** to catch dosing or cycles-of-concentration drift before it allows fouling to redevelop.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Trend **approach temperature** (cold water temp minus wet-bulb), not raw cold water temperature, to isolate tower performance from weather variation
- [ ] Confirm fan speed, motor performance, and water circulation flow are at normal/design values before suspecting fill fouling
- [ ] Physically inspect fill media condition for biological growth, scale, or debris
- [ ] Review water treatment program history (biocide, scale inhibitor dosing, cycles of concentration) to identify why fouling developed
- [ ] Clean fill media and confirm approach temperature recovery
- [ ] Adjust the water treatment program to address the underlying cause, not just clean reactively
- [ ] Establish standing approach-temperature trending and periodic fill inspection to catch future degradation early

## 10. Key Takeaway

> Cooling tower performance should always be judged against **approach temperature**, not raw outlet temperature, since ambient wet-bulb conditions vary independently of tower health. When approach widens steadily, rule out mechanical/fan causes first (they're usually easy to confirm from existing instrumentation), then inspect the fill directly — biological and scale fouling on fill media is a common, often overlooked driver of gradual performance loss, and fixing it durably means also fixing the water treatment program that allowed it to happen.

---

## Related Concepts / Tags

`cooling-tower` `fill-fouling` `approach-temperature` `wet-bulb-temperature` `biofouling` `scale` `water-treatment` `evaporative-cooling` `predictive-maintenance`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
