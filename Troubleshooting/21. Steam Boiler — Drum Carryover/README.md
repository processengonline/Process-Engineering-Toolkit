# Troubleshooting Guide: Steam Boiler — Drum Carryover Causing Turbine Trip Risk

> **Category:** Utilities / Steam Generation
> **Unit:** Package/Utility Steam Boiler — Steam Drum
> **Tools:** Steam purity monitoring (silica/conductivity trend), drum level trend review, boiler water chemistry review
> **Fluid Package:** Not applicable in the VLE sense — steam drum carryover is governed by boiler water chemistry and drum internals hydraulics, not a hydrocarbon phase-equilibrium calculation
> **Symptom:** Rising steam conductivity/silica downstream of the drum, with the risk of solids carryover into the turbine

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Steam conductivity and silica content trending up at the drum outlet; concern over carryover into the downstream steam turbine |
| Initially unclear | Whether this was a water chemistry (dissolved solids concentration) issue or a mechanical/hydraulic carryover issue inside the drum |
| Actual root cause | Boiler was operating at a higher-than-recommended drum level combined with elevated total dissolved solids (TDS) from insufficient blowdown, causing mechanical (foam/mist) carryover through the drum internals |
| Fix | Corrected drum level to design operating band; increased blowdown rate to restore TDS within limits |
| Diagnostic signal | Steam purity degradation correlated with periods of elevated drum level, not simply with boiler load |
| Prevention | Continuous blowdown control tied to TDS monitoring; drum level alarm/monitoring against the carryover-risk band, not just the trip band |

---

## 2. Symptom

- **Steam conductivity and silica content downstream of the drum trended upward** — both are standard indicators of solids being carried over from boiler water into the steam.
- Risk of **carryover into the downstream steam turbine**, where solids deposition can damage turbine blades and reduce efficiency — a serious reliability concern.

## 3. Why This Wasn't Assumed to Be Purely a Water Chemistry Problem

Elevated steam impurities are often first attributed to boiler water chemistry alone (high TDS from insufficient blowdown, poor feedwater quality). But **drum internals hydraulics** — particularly drum water level — also directly govern how much liquid (and the solids dissolved in it) gets entrained into the steam space. High TDS water alone doesn't necessarily cause high carryover if the drum's steam-water separation is working correctly; but even moderately elevated TDS combined with a **high drum level** can overwhelm the separation internals and cause carryover. Both factors needed to be checked together, not treated as alternative explanations.

## 4. Diagnostic Approach

### Step 1 — Confirm the steam purity trend and correlate with load
Steam conductivity/silica trends were reviewed, and initially checked against boiler load to rule out a simple load-related explanation (some carryover mechanisms are load-dependent).

### Step 2 — Review boiler water TDS trend
Boiler water total dissolved solids were reviewed against blowdown records, identifying **TDS running above the recommended operating limit** — indicating blowdown had not been keeping pace with makeup/feedwater solids input.

### Step 3 — Review drum level trend alongside the steam purity trend
Rather than treating TDS alone as the explanation, **drum water level** was reviewed over the same time period.

**Finding:** Periods of elevated steam impurity **correlated closely with periods of higher-than-recommended drum level** — not simply with load — indicating the drum internals' steam-water separation capability was being compromised by operating level, on top of the elevated TDS.

### Step 4 — Confirm the compounding mechanism
The combination of **elevated TDS and elevated drum level together** was identified as the driver: higher drum level reduces the vapor disengagement space above the water surface, allowing more mechanical carryover (foam, mist, water droplets) into the steam outlet, and each entrained droplet carries a higher solids load because TDS was also elevated.

### Quantitative Basis

- Steam silica: baseline 0.015 ppm, rose to **0.09 ppm** against a 0.02 ppm turbine-protection limit at this drum pressure (600 psig).
- Steam conductivity (cation): baseline 0.2 µS/cm, rose to **1.4 µS/cm.**
- Boiler water TDS: recommended ABMA guideline limit for this drum pressure is 3,000 ppm; logged values ran **4,200–4,600 ppm** over the affected period.
- Drum level: normal operating band is NWL ± 2 in; trend showed the drum running **NWL + 4 to + 6 in** during the same periods steam purity degraded — well inside the alarm band but above the carryover-risk threshold.

## 5. Root Cause

**The boiler was operating with drum level above its recommended band while also running with elevated total dissolved solids due to insufficient blowdown.** The combination reduced the drum's effective vapor-liquid disengagement capability and increased the solids content of any carried-over liquid, together driving steam impurity levels above the acceptable range for the downstream turbine.

## 6. Corrective Action

1. **Corrected drum water level** back to its design operating band.
2. **Increased blowdown rate** to bring boiler water TDS back within limits.

## 7. Verification

- Drum level restored to **NWL ± 1 in**; boiler water TDS reduced to **2,600 ppm**, within the 3,000 ppm guideline.
- Steam silica returned to **0.012 ppm** and conductivity to **0.18 µS/cm** — both back at baseline.
- Values held stable over **30 days of continued monitoring**, including across the full range of normal boiler loads, confirming the fix wasn't load-condition-specific.

## 8. Prevention / Long-Term Fix

- Implemented **continuous blowdown control tied to TDS monitoring**, rather than periodic/manual blowdown adjustments alone.
- Added **drum level alarm/monitoring against the carryover-risk band** — a tighter threshold than the emergency high-level trip point — so operators can correct drum level before it contributes to carryover, not just before it risks a trip.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Trend steam conductivity/silica against boiler load to rule out a simple load-correlated cause
- [ ] Review boiler water TDS against blowdown records and recommended operating limits
- [ ] Independently review **drum water level trend** over the same period — don't assume TDS alone explains carryover
- [ ] Look for correlation between elevated steam impurity periods and elevated drum level periods specifically
- [ ] If both TDS and drum level are elevated, treat them as a compounding pair, not alternative single causes
- [ ] Correct drum level to its design operating band
- [ ] Increase blowdown (or otherwise correct feedwater/makeup treatment) to bring TDS within limits
- [ ] Verify steam purity recovery is stable across the full range of normal boiler loads, not just at the load where the correction was made
- [ ] Implement continuous blowdown control tied to TDS monitoring and a carryover-risk-specific drum level alarm (tighter than the emergency trip threshold)

## 10. Key Takeaway

> Steam purity carryover is rarely a single-cause problem — it's usually the **combination** of water chemistry (TDS) and drum hydraulics (level) that overwhelms the drum's steam-water separation capability. Correcting TDS alone, or level alone, may not fully resolve carryover if both were contributing; check drum level trends alongside water chemistry trends, and set a separate, tighter operational alarm for level that protects against carryover — not just the emergency high-level trip that protects against overfill.

---

## Related Concepts / Tags

`steam-boiler` `drum-carryover` `steam-purity` `total-dissolved-solids` `TDS` `blowdown` `drum-level` `steam-turbine-protection` `boiler-water-chemistry`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
