# Troubleshooting Guide: LACT Unit — Custody Transfer Metering Discrepancy

> **Category:** Custody Transfer / Metering
> **Unit:** Lease Automatic Custody Transfer (LACT) Unit — Turbine or Positive Displacement Meter with Prover
> **Tools:** Meter proving data review, BS&W (basic sediment and water) analysis, meter factor trending
> **Fluid Package:** Not applicable in the VLE sense — custody transfer metering accuracy is governed by API MPMS standards and meter proving, not a phase-equilibrium calculation
> **Symptom:** A persistent volumetric discrepancy between LACT-metered delivered volume and receiving-party (pipeline/terminal) measured volume

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Persistent volumetric discrepancy between LACT unit delivered volume and the receiving party's measured volume, beyond normal tolerance |
| Initially unclear | Whether the meter itself had drifted out of calibration, or whether the crude being measured contained more free water/sediment than accounted for |
| Actual root cause | Rising basic sediment and water (BS&W) content in the crude, above the level the sampling/net-oil correction was capturing, meant a portion of measured "gross" volume was actually water rather than oil |
| Fix | Corrected the automatic sampler to capture a representative sample per API MPMS guidance; adjusted upstream dehydration/free-water knockout to reduce BS&W ahead of the LACT unit |
| Diagnostic signal | Meter factor from proving remained within normal tolerance (ruling out meter drift), while BS&W lab results trended up over the same period as the discrepancy |
| Prevention | Routine BS&W trending correlated against metering discrepancy; sampler system verification per API MPMS schedule |

---

## 2. Symptom

- A **persistent volumetric discrepancy** developed between the LACT unit's metered delivered (net) volume and the volume measured by the receiving party (pipeline or terminal) — exceeding the normally accepted tolerance for custody transfer.

## 3. Why This Wasn't Assumed to Be Simple Meter Drift

A custody transfer discrepancy is often first suspected to be a **meter calibration/drift** issue, since that's the most direct explanation for "the numbers don't match." But custody transfer volume isn't just a raw meter reading — it's a **net oil volume**, calculated from gross metered volume corrected for BS&W (water and sediment) content via representative sampling. If the meter itself is accurate but the BS&W correction isn't representative of what's actually flowing, the reported "net oil" volume will be wrong even though the meter is working correctly.

## 4. Diagnostic Approach

### Step 1 — Review meter proving history and meter factor trend
The LACT unit's **meter factor** (from routine proving against a certified prover) was reviewed over the relevant time period.

**Finding:** Meter factor remained **within normal tolerance** — ruling out meter mechanical drift/wear as the explanation for the discrepancy.

### Step 2 — Review BS&W lab analysis trend
With the meter itself cleared, attention turned to the **net oil correction** — specifically, **BS&W (basic sediment and water) content** determined from the automatic sampler.

**Finding:** Lab BS&W results **trended upward** over the same period the volumetric discrepancy developed.

### Step 3 — Assess sampler representativeness
The automatic sampler system was reviewed against **API MPMS (Manual of Petroleum Measurement Standards)** sampling guidance to confirm whether it was still collecting a truly representative sample of the flowing stream, particularly given the rising water content — free water tends to be harder to sample representatively than well-mixed oil, especially if flow conditions or sampler probe positioning aren't ideal for the current water cut.

### Step 4 — Confirm the mechanism connecting BS&W and the discrepancy
With BS&W trending up and the sampler's representativeness in question, the mechanism became clear: **actual water content in the crude was higher than what the sampling system was capturing and correcting for**, meaning a portion of the volume being counted as "net oil" delivered was actually water — explaining the gap against the receiving party's independent measurement.

### Quantitative Basis

- Meter factor across the last 4 provings: 0.9987–0.9993, all within the ±0.25% repeatability tolerance — confirms the meter itself was not drifting.
- Field water cut had risen from **2% to 9% over 3 months** (a nearby well coming online), directly increasing the BS&W load the sampler now had to capture representatively.
- Automatic sampler-reported BS&W: **0.3%**, essentially unchanged from its historical baseline. Independent manual lab draw taken concurrently: **1.1% actual BS&W** — a **0.8 percentage-point under-capture.**
- Custody transfer volumetric discrepancy grew from a baseline 0.3% (within the ±0.5% LACT tolerance) to **1.6%**, tracking the same 3-month period as the rising water cut.

## 5. Root Cause

**Basic sediment and water (BS&W) content in the crude had risen**, and the automatic sampling system was not capturing a fully representative sample of this water at the current flow/water-cut conditions. As a result, the **net oil volume correction understated the true water content**, causing the LACT unit to report a higher net oil volume than was actually being delivered — producing the discrepancy against the receiving party's measurement.

## 6. Corrective Action

1. **Corrected the automatic sampler system** to capture a representative sample per API MPMS guidance (e.g., probe positioning, sample frequency, mixing considerations appropriate to the current water cut).
2. **Adjusted upstream dehydration/free-water knockout** ahead of the LACT unit to reduce BS&W entering the metering system in the first place.

## 7. Verification

- Post-correction, sampler-reported BS&W tracked independent manual lab draws to within **0.1 percentage points** (e.g., 1.0% sampler vs. 1.05% lab), versus the earlier 0.8-point gap.
- Volumetric discrepancy against the receiving party's measurement dropped from 1.6% to **0.4%**, within the ±0.5% custody transfer tolerance.
- Held within tolerance across the **following 3 monthly ticket reconciliation cycles.**

## 8. Prevention / Long-Term Fix

- Established **routine BS&W trending correlated against metering discrepancy**, so a developing gap can be caught and investigated early rather than allowed to accumulate.
- Added **sampler system verification per API MPMS schedule**, ensuring the sampling method remains representative as water cut and flow conditions change over time.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review meter proving history and meter factor trend first — rule in/out mechanical meter drift before looking elsewhere
- [ ] If the meter factor is stable/normal, review BS&W lab trend over the same period as the discrepancy
- [ ] Check automatic sampler representativeness against API MPMS guidance, especially if water cut has changed
- [ ] Confirm the mechanism: is the sampler under-capturing water content relative to what's actually flowing?
- [ ] Correct sampler positioning/operation per API MPMS standards
- [ ] Address the source of rising BS&W upstream (dehydration, free-water knockout) where practical, not just the measurement of it
- [ ] Confirm resolution against the receiving party's independent measurement, not just internal lab consistency
- [ ] Establish routine BS&W trending correlated to metering discrepancy as a standing check

## 10. Key Takeaway

> A custody transfer volumetric discrepancy isn't automatically a meter calibration problem — check the meter factor from proving first, and if that's stable, look at the **net oil correction** itself. Rising BS&W content combined with a sampler that's no longer representative at the current water cut can make an accurate meter report an inaccurate net oil volume. Both the meter and the sampling/correction system need to be verified independently before concluding where a discrepancy is actually coming from.

---

## Related Concepts / Tags

`LACT-unit` `custody-transfer` `metering` `BS&W` `meter-factor` `meter-proving` `API-MPMS` `automatic-sampler` `net-oil-volume`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
