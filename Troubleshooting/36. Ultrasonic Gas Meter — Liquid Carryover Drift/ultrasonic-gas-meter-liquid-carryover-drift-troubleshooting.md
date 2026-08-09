# Troubleshooting Guide: Ultrasonic Gas Meter — Custody Transfer Measurement Drift from Liquid Carryover

> **Category:** Custody Transfer / Gas Metering
> **Unit:** Ultrasonic Gas Flow Meter, Custody Transfer Station
> **Tools:** Meter diagnostic data review (speed of sound comparison, signal quality/gain trending), upstream separation performance review
> **Fluid Package:** PR, used to calculate the expected theoretical speed of sound for the actual gas composition, for comparison against the meter's measured speed of sound
> **Symptom:** Ultrasonic meter's internally measured speed of sound deviating from the value calculated from gas composition/AGA10, alongside a small but persistent metered volume discrepancy against the receiving party

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | A persistent, small volumetric discrepancy in custody-transfer gas metering vs. the receiving party's measurement |
| Initially unclear | Whether this was a meter electronics/calibration issue or a physical condition (e.g., liquid presence) affecting the meter's measurement |
| Actual root cause | Intermittent liquid carryover from an underperforming upstream separator was periodically wetting the meter's ultrasonic transducer paths, distorting signal transit time measurements and skewing the calculated flow rate |
| Fix | Corrected upstream separator performance (addressed a mist-eliminator degradation issue) to eliminate liquid carryover to the meter; verified meter diagnostics returned to normal |
| Diagnostic signal | The meter's internally measured speed of sound deviated from the AGA10/PR-calculated theoretical value for the actual gas composition, and this deviation correlated with periods of degraded upstream separator performance, not with meter age or calibration history |
| Prevention | Routine speed-of-sound comparison (measured vs. calculated) as a standing meter health check; upstream separator performance monitoring tied into the metering station's data quality program |

---

## 2. Symptom

- A **small but persistent volumetric discrepancy** existed between the ultrasonic meter's custody-transfer measurement and the receiving party's independently measured volume — within a range that raised concern but wasn't dramatic enough to obviously implicate one specific cause.

## 3. Why This Wasn't Assumed to Be a Meter Calibration Issue

Ultrasonic meters are generally very stable and don't drift the way mechanical meters can, so a volumetric discrepancy is often first suspected to be a **calibration or electronics issue** requiring recalibration or replacement. But modern ultrasonic meters provide rich internal diagnostics — including a **measured speed of sound**, which can be independently cross-checked against a **theoretically calculated** speed of sound from the actual gas composition (via AGA10, using an equation of state like PR). This diagnostic exists specifically to catch physical measurement problems (like liquid presence) that look like "meter drift" but aren't actually a calibration issue at all.

## 4. Diagnostic Approach

### Step 1 — Pull ultrasonic meter internal diagnostics
The meter's internal diagnostic data was reviewed, focusing on its **measured speed of sound** and per-path signal quality/gain values, rather than just the reported flow rate.

### Step 2 — Calculate the theoretical (expected) speed of sound from gas composition
Using **PR** and AGA10 methodology with the actual current gas composition, the **theoretically expected speed of sound** was calculated for comparison against the meter's measured value.

### Step 3 — Compare measured vs. calculated speed of sound and correlate with time
**Finding:** The meter's measured speed of sound periodically **deviated from the calculated theoretical value**, and this deviation was **not constant** — it appeared intermittently rather than as a fixed calibration offset (which would show a consistent, steady bias instead).

### Step 4 — Investigate the physical cause of intermittent deviation
An intermittent (rather than constant) speed-of-sound deviation, together with degraded signal quality/gain on certain ultrasonic paths during the same periods, is a recognized signature of **liquid presence at the meter** (wetting the transducer faces or path, which distorts acoustic transit time). This pointed the investigation upstream, toward the **separator** feeding this metering station, which was found to have **degraded mist eliminator performance**, allowing intermittent liquid carryover downstream to the meter run.

### Quantitative Basis

- AGA10-calculated (PR) theoretical speed of sound for the actual gas composition: **1,382 ft/s.** Meter-measured speed of sound tracked this within 0.1% on normal days, but deviated as low as **1,355 ft/s (1.9% low) on affected days** — liquid wetting the acoustic path slows and distorts transit time.
- On affected days, **2 of the meter's 4 acoustic paths (the lower chords, closest to any liquid film)** showed signal quality/gain dropping from a normal 85–95% to **40–55%**, while the upper paths stayed normal — a spatial pattern consistent with liquid sitting low in the meter run rather than a uniform electronic fault.
- Volumetric discrepancy against the receiving party: baseline 0.15%, grew to **0.9% on affected days** — well outside the ±0.25% AGA custody transfer tolerance.
- Deviation events occurred on **14 of 60 days reviewed**, and all 14 correlated with logged high-level alarms on the upstream separator.

## 5. Root Cause

**An underperforming upstream separator (degraded mist eliminator) allowed intermittent liquid carryover into the gas stream reaching the ultrasonic meter.** Liquid periodically wetting the meter's transducer paths distorted the acoustic transit time measurements, causing the meter's calculated flow rate to deviate from the true gas flow rate — producing the observed custody transfer volumetric discrepancy. This was a physical measurement disturbance, not a meter calibration or electronics fault.

## 6. Corrective Action

1. **Corrected upstream separator performance**, addressing the mist eliminator degradation to eliminate liquid carryover to the meter run.
2. **Verified meter diagnostics** (measured vs. calculated speed of sound, signal quality/gain) returned to normal, stable values.

## 7. Verification

- Post-repair, measured speed of sound tracked the AGA10/PR-calculated value **within 0.15% on every subsequent day** reviewed, with no further intermittent deviations.
- All 4 acoustic path signal quality/gain values returned to and held the normal **85–95% range.**
- Volumetric discrepancy dropped to **0.12%**, within the ±0.25% tolerance, sustained over the following **45 days.**

## 8. Prevention / Long-Term Fix

- Established **routine speed-of-sound comparison (measured vs. calculated) as a standing meter health check**, independent of the reported flow rate itself, since this diagnostic can catch physical measurement problems that a simple volume-discrepancy review would miss.
- Added **upstream separator performance monitoring** into the metering station's overall data quality program, recognizing that meter accuracy depends on gas quality delivered to it, not just the meter's own internal health.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Pull ultrasonic meter internal diagnostics (measured speed of sound, per-path signal quality/gain) rather than relying on reported flow rate alone
- [ ] Calculate the theoretical speed of sound from actual gas composition (AGA10/EOS-based) for comparison
- [ ] Check whether any measured-vs-calculated deviation is constant (favors calibration/electronics) or intermittent (favors a physical condition like liquid presence)
- [ ] If intermittent, review signal quality/gain on individual ultrasonic paths for correlated degradation
- [ ] Investigate upstream separation performance (mist eliminator condition, liquid carryover history) as a likely source
- [ ] Correct the upstream separation issue rather than replacing/recalibrating the meter if the meter's own diagnostics point to a physical (not electronic) cause
- [ ] Confirm resolution via BOTH meter diagnostic recovery AND reduced discrepancy against the receiving party's independent measurement
- [ ] Establish routine speed-of-sound comparison as a standing custody transfer meter health check

## 10. Key Takeaway

> Ultrasonic meters carry rich internal diagnostics specifically so a "meter problem" doesn't have to mean a calibration or electronics fault — comparing measured speed of sound against the value calculated from actual gas composition can distinguish a genuine meter issue from a physical disturbance like liquid carryover. An intermittent deviation, especially alongside degraded per-path signal quality, points upstream to gas quality (separator performance) rather than to the meter itself; fixing the separator can resolve a metering discrepancy that recalibrating or replacing the meter never would.

---

## Related Concepts / Tags

`ultrasonic-gas-meter` `custody-transfer` `speed-of-sound` `AGA10` `liquid-carryover` `mist-eliminator` `meter-diagnostics` `Peng-Robinson` `gas-metering`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
