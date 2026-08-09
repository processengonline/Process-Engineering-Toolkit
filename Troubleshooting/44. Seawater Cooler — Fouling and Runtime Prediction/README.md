# Troubleshooting Guide: Seawater Cooler — Fouling and Runtime Prediction

> **Category:** Heat Transfer Equipment / Predictive Maintenance
> **Unit:** Seawater-Cooled Shell-and-Tube Heat Exchanger (process gas/liquid cooling service)
> **Tools:** HTRI Xchanger Suite (thermal-hydraulic rating with fouling-resistance trending)
> **Fluid Package:** Not applicable in the traditional VLE sense — see Section 4, Step 1
> **Symptom:** Gradual multi-month performance decline — not a single failure event

---

> **Note on case type:** Unlike Case Studies 1–5, this is primarily a **predictive/quantitative trending exercise** rather than a single-root-cause diagnosis. The underlying cause (biological fouling) was reasonably suspected from the start given seawater service; the real engineering task was **quantifying** the degradation and **predicting remaining runtime**, not distinguishing between competing hypotheses. It's included here because the same "model vs. actual" discipline used elsewhere in this series applies directly to predictive maintenance, not just fault diagnosis.

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Gradually worsening performance over months: rising process outlet temperature, higher compressor discharge temperature, increasing seawater-side pressure drop, climbing energy use |
| Task | Quantify the degradation and predict remaining runtime before the exchanger could no longer meet cooling duty |
| Actual root cause | Biological fouling (algae and marine growth) on the seawater side, confirmed by inspection |
| Fix | Mechanical cleaning; optimized chlorination/biocide dosing |
| Diagnostic tool | HTRI Xchanger Suite model; overall U (measured) vs. clean design U; historical fouling-rate trend extrapolated forward |
| Prevention | Established an ongoing HTRI-based fouling monitoring program — cleaning now scheduled by **predicted remaining runtime**, not a fixed calendar interval |

---

## 2. Symptom

A **gradual, multi-month decline** across several related indicators — the pattern itself (slow, compounding, multi-parameter) is the first diagnostic clue:

- **Rising outlet process temperature** (cooling duty not being fully met)
- **Higher compressor discharge temperature** (downstream consequence of reduced cooling)
- **Increasing seawater-side pressure drop** (physical restriction developing)
- **Climbing energy use** (system working harder to compensate)

## 3. Why This Called for Quantification, Not Just a Cleaning Call

With seawater cooling service, **biological fouling** (algae, marine growth, scaling) is a well-known and expected long-term degradation mechanism — this isn't really a "which of several unrelated causes is it" situation like Cases 1–5. The actual engineering question was different:

1. **How much has performance actually degraded**, in quantitative terms (not just "temperatures are creeping up")?
2. **How much runtime is left** before the exchanger can no longer meet cooling duty?
3. Should cleaning happen **now**, or can it be scheduled to align with a planned outage?

Reacting to each symptom individually (temperature creeping up → schedule a clean) doesn't answer these questions — it requires a **model-based quantitative trend**, not just a qualitative "it's fouling" observation.

## 4. Diagnostic Approach

### Step 1 — Model the exchanger using design geometry and operating data
The exchanger was modeled in **HTRI Xchanger Suite**, using:
- Design tube/shell geometry
- Actual operating data (flows, temperatures)

> **Why there's no "fluid package" here in the usual sense:** Unlike Cases 1–5, which all involve phase-equilibrium (VLE/electrolyte/hydrate) modeling requiring a specific thermodynamic package, this is a **thermal-hydraulic rating exercise**. HTRI uses its own built-in physical property correlations and databanks (seawater properties, process-side fluid properties as input) rather than a cubic-EOS flash calculation — there's no vapor-liquid equilibrium being solved. This is a useful distinction to keep in mind: not every simulation-based diagnosis is a VLE problem, and picking the right *type* of tool (rating software vs. flash-based process simulator) matters as much as picking the right fluid package within a simulator.

### Step 2 — Calculate actual overall heat transfer coefficient (U) and compare to clean design value

```
U_actual (from measured temperatures and flows)  vs.  U_clean (design/clean condition)
```

The gap between these two values is a **direct, quantitative measure of fouling resistance** — not just an inference from temperature trends, but a calculated number tied to the underlying heat transfer physics.

### Step 3 — Trend the fouling rate historically and extrapolate forward
Using **historical trend data** (not just the current snapshot), the **fouling rate** was estimated — i.e., how quickly U is degrading over time. This rate was then **extrapolated forward** to predict when U would fall below the value required to meet cooling duty.

**Interpretation:** This converts a reactive question ("performance is bad, should we clean now?") into a proactive one ("at the current fouling rate, we have approximately N weeks/months of acceptable performance left — plan the clean accordingly").

### Step 4 — Validate against inspection
The HTRI-based prediction was checked against physical inspection findings to confirm the model's fouling-rate estimate and mechanism assumption were correct, not just numerically self-consistent.

### Quantitative Basis

- Clean design U: 210 Btu/hr·ft²·°F. Trended actual U fell from 205 (month 1) to **118 Btu/hr·ft²·°F by month 7 — a 44% loss.**
- Average fouling rate over the trend: approximately 0.00031 hr·ft²·°F/Btu per week.
- Extrapolating the trend forward predicted U would fall below the 140 Btu/hr·ft²·°F minimum-duty threshold within **approximately 3 weeks** of the assessment — the basis for the runtime prediction communicated to operations.

## 5. Root Cause

**Biological fouling — algae and marine growth — on the seawater side**, confirmed by inspection and consistent with the fouling-resistance trend calculated from the HTRI model.

## 6. Corrective Action

1. **Mechanical cleaning** of the exchanger to remove accumulated biological fouling.
2. **Optimized chlorination/biocide dosing** on the seawater side to slow future biological growth.

## 7. Verification

- Post-cleaning U measured at **208 Btu/hr·ft²·°F — 99% of the 210 clean design value**, confirming fouling (not tube degradation) was the sole driver of the decline.
- Chlorination free residual dosing increased from 0.3 to **0.6 ppm.**
- Re-trended fouling rate over the following 3 months showed a much slower decline; extrapolated runtime at the new dosing rate extended from **3 weeks to over 6 months.**

## 8. Prevention / Long-Term Fix

- **Established an ongoing HTRI-based fouling monitoring program.**
- Cleaning is now **scheduled based on predicted remaining runtime** (from the U-trend extrapolation), rather than a **fixed calendar interval**.
- This shift — from calendar-based to condition/prediction-based maintenance — improves reliability (catching degradation before it becomes duty-limiting) while also **cutting unnecessary maintenance cost** (not cleaning exchangers that don't yet need it).

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for seawater-cooled (or similarly fouling-prone) heat exchanger gradual performance decline:

- [ ] Confirm the decline is gradual/multi-parameter (temperature, dP, energy use) rather than a sudden step change (which would point to a different cause, e.g., tube leak, blockage, instrument fault)
- [ ] Gather design geometry and current operating data (flows, inlet/outlet temperatures both sides)
- [ ] Build/update a thermal-hydraulic rating model (e.g., HTRI Xchanger Suite) for the exchanger
- [ ] Calculate **actual overall U** from measured data and compare to **clean/design U**
- [ ] Pull **historical trend data**, not just a current snapshot, to estimate the fouling rate
- [ ] **Extrapolate forward** to predict remaining runtime before U drops below the value needed for required duty
- [ ] Cross-check the predicted fouling mechanism against physical inspection when the unit is next opened
- [ ] Use the runtime prediction to **schedule** cleaning (aligned with planned outages where possible) rather than reacting to symptoms or defaulting to a fixed calendar interval
- [ ] Review chemical treatment (chlorination/biocide dosing) as a complement to mechanical cleaning, not a replacement for it
- [ ] Set up an **ongoing** monitoring cadence (not a one-time study) so future runtime predictions stay current as conditions change

## 10. Key Takeaway

> When degradation is gradual and expected (like biofouling in seawater service), the value of simulation isn't in *discovering* the cause — it's in **quantifying** it and **predicting** how much time you have left. Calculating actual U against clean design U, then trending and extrapolating that gap, turns "temperatures are creeping up, better clean it soon" into a defensible runtime number you can plan an outage around. That shift — from calendar-based to prediction-based maintenance — is often where the real cost savings and reliability gains come from, not just the cleaning itself.

---

## Related Concepts / Tags

`seawater-cooler` `shell-and-tube` `fouling` `biofouling` `HTRI` `Xchanger-Suite` `overall-heat-transfer-coefficient` `U-value-trending` `runtime-prediction` `predictive-maintenance` `chlorination` `biocide-dosing` `thermal-hydraulic-rating`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying.*
