# Troubleshooting Guide: Molecular Sieve Dehydration — Early Water Breakthrough

> **Category:** Gas Processing / Solid Adsorption
> **Unit:** Molecular Sieve Dryer Beds (TSA cycle), upstream of NGL/cryogenic processing
> **Tools:** Cyclic adsorption performance/breakthrough-curve analysis, regeneration temperature trending
> **Fluid Package:** Not applicable in the VLE sense — performance is governed by adsorption isotherms and regeneration thermal profiles, not a phase-equilibrium flash
> **Symptom:** Outlet gas dew point creeping up before the normal end of the adsorption cycle — beds "breaking through" early

---

> **Note on case type:** Like the seawater cooler case (Case Study 6), this is fundamentally about **cyclic performance trending**, not phase-equilibrium simulation. Adsorption capacity, not VLE, is the governing physics — the diagnostic approach centers on regeneration effectiveness, not a fluid package choice.

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Outlet gas dew point rising noticeably before scheduled bed switchover |
| Initially unclear | Whether beds were simply reaching end-of-life, or something in the cycle itself had degraded |
| Actual root cause | Regeneration gas heater underperforming — regen gas not reaching design temperature, leaving residual moisture on the sieve each cycle and progressively reducing dynamic capacity |
| Fix | Corrected heater duty/instrumentation issue; verified regen outlet temperature reached design target |
| Diagnostic signal | Bed differential temperature profile during regeneration not reaching expected peak; lab analysis of pulled sieve confirmed retained moisture |
| Prevention | Trend regeneration outlet temperature every cycle; alarm if target not reached |

---

## 2. Symptom

- **Outlet gas dew point began rising before the normal end of the adsorption cycle**, i.e., beds appeared to be breaking through earlier than their design cycle time.
- No obvious upstream process change (feed rate, inlet moisture loading) was reported.

## 3. Why This Wasn't Simply "Beds Need Replacing"

Early breakthrough is often assumed to mean the sieve has reached end-of-life and needs replacement — an expensive assumption to act on without confirmation. But early breakthrough can equally be caused by **incomplete regeneration** each cycle: if a bed isn't fully dried out before being put back into adsorption service, its *effective* capacity shrinks even though the sieve material itself may still be perfectly good. Distinguishing these two requires looking at the **regeneration side** of the cycle, not just the adsorption-side symptom.

## 4. Diagnostic Approach

### Step 1 — Review the adsorption-side breakthrough trend
Outlet dew point trends confirmed breakthrough was occurring measurably earlier than the design cycle time, and that this had developed progressively (not a single-cycle anomaly).

### Step 2 — Check the regeneration-side temperature profile
Bed differential temperature during regeneration was reviewed cycle-by-cycle. **The regeneration outlet temperature was not reaching its design target** — the bed was being taken off regeneration and put back into service before it was fully dried.

### Step 3 — Confirm physically with a sieve sample
A sieve sample pulled from an affected bed was analyzed in the lab and **confirmed retained moisture** consistent with incomplete regeneration — not sieve degradation (attrition, crushing, contamination) that would indicate genuine end-of-life.

### Step 4 — Trace back to the regeneration heater
With incomplete regeneration confirmed as the mechanism, the investigation moved to *why* — the regeneration gas heater was underperforming, not delivering enough duty to reach design regen temperature within the allotted cycle time.

### Quantitative Basis

- Design adsorption cycle time: 8 hr, with an outlet dew point spec of ≤ −40°F. Breakthrough was occurring at **6.1 hr — 24% early.**
- Design regeneration outlet temperature target: 550°F. Trended actual regen outlet averaged **495°F — 55°F below target**, meaning beds were returned to service before reaching design dryness.
- Lab analysis of a pulled sieve sample measured **4.8 wt% retained moisture, versus <0.5 wt% for a properly regenerated bed** — direct confirmation of incomplete drying rather than sieve attrition or contamination.

## 5. Root Cause

**The regeneration gas heater was underperforming**, so regeneration gas did not reach the design outlet temperature within the cycle time. This left **residual moisture on the sieve** at the start of each new adsorption cycle, **progressively reducing dynamic capacity** and causing water to break through earlier and earlier as the effect compounded cycle over cycle.

## 6. Corrective Action

1. Corrected the heater duty/instrumentation issue causing underperformance.
2. Verified regeneration outlet temperature reached its design target on subsequent cycles.

## 7. Verification

- Regeneration outlet temperature restored to an average of **552°F**, at/above the 550°F design target.
- Breakthrough timing returned to **7.9 hr**, close to the 8 hr design cycle time.
- Outlet dew point held below **−42°F over 30 days (≈90 cycles)** of continued monitoring.

## 8. Prevention / Long-Term Fix

- **Regeneration outlet temperature is now trended every cycle**, with an alarm if the design target is not reached — catching incomplete regeneration immediately rather than after several cycles of cumulative capacity loss.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm breakthrough timing against the design cycle time using outlet dew point trend
- [ ] Before assuming end-of-life, review the **regeneration-side** temperature profile for each affected bed
- [ ] Confirm regeneration outlet temperature is reaching its design target, not just that the heater "ran"
- [ ] Pull and lab-analyze a sieve sample to distinguish incomplete regeneration (retained moisture) from genuine sieve degradation (attrition, crushing, coking, heavy hydrocarbon contamination)
- [ ] If regeneration is incomplete, trace back to the heater (duty, instrumentation, fouling) or cycle timing logic
- [ ] After correction, confirm both regeneration temperature profile AND adsorption-side breakthrough timing return to design
- [ ] Add per-cycle regeneration temperature trending/alarming to standing operations monitoring

## 10. Key Takeaway

> Early breakthrough on a cyclic adsorption system isn't automatically an end-of-life sieve problem — it can just as easily be an **incomplete regeneration** problem that silently compounds cycle after cycle. Before replacing expensive sieve material, confirm the regeneration side is actually delivering its design temperature and duration; a lab sample of the pulled sieve is the cheapest way to tell "needs replacing" from "isn't being dried properly" apart.

---

## Related Concepts / Tags

`molecular-sieve` `TSA` `dehydration` `breakthrough-curve` `regeneration-temperature` `adsorption-capacity` `dew-point` `cyclic-process` `gas-processing`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
