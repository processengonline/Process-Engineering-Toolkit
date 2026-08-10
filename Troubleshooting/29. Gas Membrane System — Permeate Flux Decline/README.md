# Troubleshooting Guide: Gas Separation Membrane System — Declining Permeate Flux and CO2 Removal Performance

> **Category:** Gas Processing / Membrane Separation
> **Unit:** Hollow-Fiber Membrane System, CO2 Removal Service
> **Tools:** Membrane performance model (permeance/selectivity vs. operating conditions), stage-by-stage pressure and composition trend review
> **Fluid Package:** PR for the bulk gas-phase properties feeding the membrane performance model; membrane permeance/selectivity itself is characterized empirically per membrane type, not through a cubic EOS
> **Symptom:** CO2 content in the residue (treated) gas stream gradually rising, requiring increasingly high recycle/permeate rates to maintain spec

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Residue gas CO2 content gradually rising; more permeate recycle needed to hold spec, increasing compression load and operating cost |
| Initially unclear | Whether membrane elements had degraded (fouling/plasticization) or feed gas composition/conditions had shifted the required membrane area for the same performance |
| Actual root cause | A combination of heavy hydrocarbon condensation on the membrane surface (from operating closer to the hydrocarbon dew point than the original design case) and resulting membrane plasticization, both of which reduced effective selectivity |
| Fix | Adjusted upstream feed gas conditioning (temperature/pressure) to restore adequate margin above the hydrocarbon dew point ahead of the membrane; replaced the most affected membrane elements |
| Diagnostic signal | Performance decline correlated with periods of reduced feed gas margin above its hydrocarbon dew point, not simply with membrane run-time/age alone |
| Prevention | Dew point margin monitoring ahead of the membrane skid; periodic selectivity testing on membrane elements independent of overall system performance |

---

## 2. Symptom

- **Residue (treated) gas CO2 content gradually rose** over time.
- Operators had to use **increasingly high permeate recycle rates** to maintain the CO2 spec, driving up compression load and operating cost.

## 3. Why This Wasn't Simply Attributed to Membrane Aging

Membrane performance naturally declines somewhat over its service life, so a gradual CO2 spec creep might be dismissed as normal aging, with the response being simply "replace elements on schedule." But before accepting that conclusion (and its associated capital cost), it was worth checking whether the decline was tracking normal run-time-based aging, or whether it correlated with a **specific operating condition** — which would point to a correctable process cause rather than unavoidable membrane wear.

## 4. Diagnostic Approach

### Step 1 — Review performance decline against membrane run-time/age
CO2 slip was plotted against cumulative membrane operating hours to check for a smooth, run-time-correlated aging curve.

**Finding:** The decline was **not smoothly correlated with run-time alone** — there were periods of faster and slower decline that didn't match a simple aging pattern.

### Step 2 — Review feed gas conditions against the membrane's hydrocarbon dew point margin
Feed gas temperature and pressure were reviewed relative to the **hydrocarbon dew point** of the actual gas composition (using PR to establish dew point behavior), specifically looking at the margin between feed conditions and dew point ahead of the membrane skid.

**Finding:** Periods of **faster performance decline correlated with periods of reduced dew point margin** — i.e., times when feed gas was operating closer to its hydrocarbon dew point than the original design case assumed.

### Step 3 — Connect reduced margin to a physical mechanism
Operating close to the hydrocarbon dew point risks **condensation of heavy hydrocarbons on the membrane fiber surface**. This can both directly foul the membrane surface (blocking permeation sites) and, for polymeric membranes, cause **plasticization** — a swelling effect from hydrocarbon absorption into the polymer matrix that reduces the membrane's inherent CO2/hydrocarbon selectivity.

### Step 4 — Confirm via inspection/testing of affected elements
The most affected membrane elements (from the sections/skids experiencing the lowest dew point margin) were inspected and selectivity-tested, confirming **reduced selectivity consistent with plasticization/fouling**, beyond what would be expected from run-time-based aging alone.

### Quantitative Basis

- Residue CO2 spec: 2.0 mol%. Baseline actual ~1.6 mol%, drifted to **3.4 mol%** at the original design permeate recycle rate.
- Permeate recycle required to hold spec climbed from a design **8% of feed to 19% of feed** — more than doubling the recompression load.
- Design dew point margin was 15°F above the hydrocarbon dew point at feed conditions; during warm-weather periods with reduced feed gas cooling capacity, margin shrank to as little as **3°F.**
- Bench selectivity testing: elements from the lowest-margin skid measured **CO2/CH4 selectivity of 11**, versus a design value of 18 and **16–17 on elements from skids that saw normal dew point margin throughout** — isolating the degradation to the specific low-margin sections rather than uniform fleet-wide aging.

## 5. Root Cause

**Feed gas periodically operated with insufficient margin above its hydrocarbon dew point ahead of the membrane system**, allowing heavy hydrocarbon condensation on the membrane fiber surface. This caused both surface fouling and membrane plasticization, reducing effective CO2/hydrocarbon selectivity beyond normal aging — driving the observed rise in residue gas CO2 content and the need for increasing permeate recycle.

## 6. Corrective Action

1. **Adjusted upstream feed gas conditioning** (temperature/pressure) to restore adequate margin above the hydrocarbon dew point ahead of the membrane skid.
2. **Replaced the most affected membrane elements** in the sections that had experienced the lowest dew point margin.

## 7. Verification

- Dew point margin restored to **14–16°F** following feed conditioning adjustment.
- Replaced elements measured selectivity of **17.5**, close to the 18 design value.
- Residue CO2 returned to **1.7 mol%** at the design **8% permeate recycle rate**, held over the following 60 days.

## 8. Prevention / Long-Term Fix

- Established **dew point margin monitoring ahead of the membrane skid**, so operations can proactively maintain adequate margin rather than discovering insufficient margin only through membrane performance decline.
- Implemented **periodic selectivity testing on membrane elements**, independent of overall system performance, to distinguish normal aging from an accelerated, condition-driven degradation pattern going forward.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Plot performance decline against membrane run-time/age to check for a normal aging pattern
- [ ] If the decline doesn't smoothly track run-time, review feed gas conditions against the membrane's hydrocarbon dew point margin
- [ ] Look for correlation between accelerated decline periods and periods of reduced dew point margin specifically
- [ ] If margin has been insufficient, consider both surface fouling and (for polymeric membranes) plasticization as mechanisms
- [ ] Inspect and selectivity-test the most affected elements to confirm the mechanism directly
- [ ] Correct upstream feed conditioning to restore adequate dew point margin
- [ ] Replace only the most affected elements initially, rather than assuming the whole membrane inventory needs replacement, if the cause was condition-specific rather than uniform aging
- [ ] Establish ongoing dew point margin monitoring ahead of the membrane skid as a standing operational check

## 10. Key Takeaway

> Not all membrane performance decline is simple aging — check whether the decline correlates with a specific operating condition, particularly feed gas margin above its hydrocarbon dew point, before assuming elements just need scheduled replacement. Operating too close to the dew point can accelerate degradation through condensation-driven fouling and plasticization, and correcting the upstream condition can protect the remaining membrane inventory rather than just replacing the damage after the fact.

---

## Related Concepts / Tags

`membrane-separation` `CO2-removal` `permeate-flux` `membrane-plasticization` `hydrocarbon-dew-point` `hollow-fiber-membrane` `selectivity` `gas-processing` `Peng-Robinson`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
