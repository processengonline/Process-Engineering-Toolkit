# Troubleshooting Guide: Custody Transfer Prover — Meter Factor Drift from Prover Calibration Error

> **Category:** Custody Transfer / Metering Metrology
> **Unit:** Pipe/Ball Prover, Custody Transfer Meter Proving Station
> **Tools:** Meter factor trend review, prover base volume certification (waterdraw) history, RTD/CTS (correction for temperature of steel) calibration check
> **Fluid Package:** Not applicable — this is a volumetric metrology investigation, not a phase-equilibrium calculation
> **Symptom:** Meter factor obtained from routine proving trending steadily in one direction over successive provings, with no known change to the meter itself

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Meter factor trending steadily in one direction across successive proving runs, with no known meter hardware or configuration change |
| Initially unclear | Whether the meter itself was genuinely drifting (as in the LACT/ultrasonic meter cases, Case Studies 23 and 36) or the reference instrument used to prove it — the prover — was the actual source of error |
| Actual root cause | A drifted RTD on the prover shell was feeding an incorrect steel temperature into the CTS (correction for temperature of steel) calculation, causing the prover's certified base volume to be calculated incorrectly, which propagated into every meter factor derived from it |
| Fix | Recalibrated/replaced the prover RTD; performed a fresh waterdraw certification of the prover base volume |
| Diagnostic signal | The meter factor drift was smooth and steady (not a step change), and cross-checking prover certification records found the last waterdraw was overdue — prompting a check of the prover itself rather than continuing to investigate the meter |
| Prevention | RTD calibration verification tied into the prover certification schedule; periodic cross-check of meter factor trend against an independent secondary/master meter to distinguish meter-side drift from prover-side drift |

---

## 2. Symptom

- **Meter factor obtained from routine proving trended steadily in one direction** across several successive proving events — with **no known change** to the meter's hardware, configuration, or service conditions that would explain a genuine meter drift.

## 3. Why This Wasn't Assumed to Be a Meter Problem

A drifting meter factor is naturally investigated as a **meter-side** issue first — mechanical wear (for a turbine/PD meter) or a physical condition affecting measurement (as in the ultrasonic meter liquid carryover case, Case Study 36). But **proving** is a *relative* measurement: the meter factor is calculated by comparing the meter's reading against the prover's **certified base volume**, which is itself a physical quantity that must be periodically re-verified. If the prover's certified volume itself were wrong, every meter factor calculated using it would show a **consistent, systematic bias** — which would look exactly like a genuinely drifting meter, even though the meter itself was accurate the entire time.

## 4. Diagnostic Approach

### Step 1 — Confirm the drift is smooth/systematic, not a step change
The meter factor trend was reviewed and confirmed to be a **smooth, steady drift** across successive provings, rather than a sudden step change (which would more directly implicate a specific meter event, like a mechanical failure or a configuration change).

### Step 2 — Check for meter-side explanations
The meter itself was inspected/reviewed for wear, configuration changes, or process condition changes (e.g., a check for liquid/gas presence disturbing measurement, as in Case Study 36) — none were found.

### Step 3 — Review the prover's certification history
With no meter-side explanation found, attention turned to the **prover** itself. Reviewing certification records found that the prover's **last waterdraw certification was overdue** — its certified base volume had not been independently re-verified in longer than the standard interval.

### Step 4 — Check the prover's temperature correction instrumentation
Since a pipe prover's certified base volume must be corrected for the **current steel temperature** (CTS — correction for temperature of steel, since the prover barrel itself expands/contracts with temperature, changing its true internal volume), the prover's **RTD** (measuring shell temperature for this correction) was checked directly against a reference thermometer.

**Finding:** The prover's RTD was reading **low**, consistently biasing the CTS calculation and therefore the **certified base volume** used in every proving run performed since the RTD drifted.

### Quantitative Basis

- Meter factor trended from a baseline **0.9994 to 0.9971** over 8 successive monthly provings — a smooth, steady drift of roughly 0.0003 per proving, rather than any single-event step change.
- Prover's last waterdraw certification was **14 months overdue** against the standard 12-month recertification interval.
- Prover RTD, checked against a certified reference thermometer at the same location, read **4.2°F low** (68.1°F indicated vs. 72.3°F reference).
- This RTD bias translated to a CTS correction error of approximately **0.03%** in the prover's calculated base volume — small on its own, but applied consistently across every proving run, it produced the smooth, systematic meter factor drift observed.

## 5. Root Cause

**A drifted RTD on the prover shell was feeding an artificially low steel temperature into the CTS calculation**, causing the prover's certified base volume — the reference value every meter factor is calculated against — to be systematically miscalculated. Because this error applied consistently to every proving run using this prover, it produced a smooth, steady apparent "meter drift" in the meter factor trend, even though the meter itself had not changed at all.

## 6. Corrective Action

1. **Recalibrated/replaced the prover RTD.**
2. **Performed a fresh waterdraw certification** of the prover's base volume, using the corrected temperature instrumentation.

## 7. Verification

- Post-recalibration, the RTD read **72.4°F**, within 0.1°F of the 72.3°F reference thermometer.
- The fresh waterdraw certification established a corrected base volume, differing from the previously (incorrectly) certified value by **0.03%** — consistent with the RTD bias identified.
- Meter factor, recalculated using the corrected prover base volume across subsequent provings, returned to **0.9993-0.9996**, matching the original baseline range and confirming the meter itself had been accurate throughout.

## 8. Prevention / Long-Term Fix

- **RTD calibration verification is now tied directly into the prover certification schedule**, so temperature instrumentation drift is caught at the same cadence as the base volume recertification itself.
- Established **periodic cross-checking of the meter factor trend against an independent secondary or master meter**, so a future smooth, systematic drift can be quickly attributed to the prover or the meter, rather than defaulting to a meter-side investigation every time.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm whether a meter factor drift is smooth/systematic (favors an instrumentation or reference-standard bias) or a step change (favors a specific meter event)
- [ ] Check for meter-side explanations first (mechanical wear, configuration change, process condition disturbance) since these are more common
- [ ] If no meter-side cause is found, review the prover's own certification history — is a waterdraw recertification overdue?
- [ ] Check the prover's temperature correction (CTS) instrumentation (RTD) against an independent reference thermometer
- [ ] If the RTD is biased, recognize this as a systematic error applied to every proving run, not a random or intermittent fault
- [ ] Recalibrate/replace the RTD and perform a fresh waterdraw certification using corrected instrumentation
- [ ] Confirm recovery by recalculating meter factor using the corrected prover base volume and comparing against the original baseline range
- [ ] Tie RTD/temperature instrumentation calibration into the prover certification schedule going forward, and periodically cross-check against an independent secondary meter to catch future prover-side drift specifically

## 10. Key Takeaway

> A drifting meter factor doesn't automatically mean the meter is drifting — proving is a relative measurement against the prover's certified base volume, and if that reference itself has an error (commonly from an overdue waterdraw certification or a biased temperature correction instrument), every meter factor calculated from it will show the same smooth, systematic bias, perfectly mimicking a genuine meter drift. Before extensively troubleshooting the meter, check whether the prover's own certification is current and its temperature correction instrumentation is accurate.

---

## Related Concepts / Tags

`custody-transfer` `meter-proving` `prover` `meter-factor` `waterdraw-certification` `CTS` `correction-for-temperature-of-steel` `RTD-calibration` `metrology`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
