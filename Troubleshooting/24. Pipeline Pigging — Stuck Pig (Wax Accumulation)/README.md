# Troubleshooting Guide: Pipeline Pigging — Stuck Pig from Underestimated Wax/Debris Accumulation

> **Category:** Pipeline Operations / Flow Assurance
> **Unit:** Pipeline Pigging System (Launcher/Receiver), Gathering or Transmission Line
> **Tools:** Pig tracking/differential pressure trending, pipeline deposit (wax) accumulation estimate
> **Fluid Package:** PR, used within a flow assurance/wax deposition model to estimate accumulated deposit thickness between pigging runs
> **Symptom:** A pig run stalls partway through the line — differential pressure across the pig rises sharply and pig tracking signal stops advancing

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Pig stalled partway through the pipeline during a routine pigging run; differential pressure across the pig spiked and tracking signal stopped advancing |
| Initially unclear | Whether this was a pig mechanical failure (damaged cups/discs) or the pipeline itself had accumulated far more deposit than the pigging frequency assumed |
| Actual root cause | The established pigging frequency was based on an outdated deposition-rate estimate; actual wax accumulation between runs had grown well beyond that assumption (due to a colder-than-typical season and reduced flow rate), producing a deposit plug too large and hard for a standard pig to push through |
| Fix | Free the stuck pig (via bidirectional flow/pressure techniques per pipeline-specific procedures); once cleared, ran a more frequent, graduated pigging sequence to safely reduce the deposit backlog |
| Diagnostic signal | Deposition-rate model, updated with actual recent flow rate and temperature history, predicted a much larger accumulated deposit than the pigging interval assumed — consistent with a stuck-pig event rather than pig damage |
| Prevention | Pigging frequency tied to a periodically-updated deposition model rather than a fixed calendar interval; graduated pig sizing during high-deposition seasons |

---

## 2. Symptom

- **A pig stalled partway through the pipeline** during a routine pigging run.
- **Differential pressure across the pig spiked sharply** as it encountered resistance.
- **Pig tracking signal stopped advancing**, confirming the pig had physically stopped moving rather than just slowing down.

## 3. Why This Wasn't Assumed to Be Pig Equipment Failure

A stuck pig event is often first suspected to be a **pig mechanical issue** — damaged cups/discs, incorrect pig sizing for the line, or a mechanical obstruction like a partially closed valve. These are legitimate possibilities, but before mobilizing for a mechanical failure investigation, it was worth checking the other common cause of stuck pigs in waxy crude/gas service: **the pipeline had simply accumulated more deposit than the pig (or the pigging frequency) was designed to handle in one pass.**

## 4. Diagnostic Approach

### Step 1 — Review recent operating history: flow rate and temperature
Flow rate and fluid temperature history since the last successful pigging run were reviewed, since both directly affect wax deposition rate (lower flow and lower temperature both tend to promote greater deposition).

**Finding:** The pipeline had recently experienced a period of **colder-than-typical ambient conditions combined with reduced flow rate**, both of which favor higher wax deposition.

### Step 2 — Update the deposition-rate estimate with actual conditions
Using **PR** within a flow assurance/wax deposition model, the accumulated deposit thickness was re-estimated using the **actual** flow rate and temperature history since the last pig run, rather than the original design-basis assumptions the pigging interval was set from.

**Finding:** The updated estimate predicted a **significantly larger accumulated deposit** than the existing pigging frequency assumed — consistent with a deposit plug large enough to stall a standard pig.

### Step 3 — Cross-check against the stuck-pig symptom pattern
A sharp differential pressure spike followed by a stalled tracking signal is consistent with a pig encountering a **large, hard deposit plug** rather than a mechanical/equipment failure (which more typically shows gradual differential pressure changes or erratic tracking behavior instead of a sudden stall).

### Step 4 — Plan pig recovery appropriately for a deposit-related stall
With the mechanism identified as deposit accumulation (not pig damage), recovery was planned using **bidirectional flow/pressure techniques** appropriate for freeing a pig stuck against a soft/wax deposit plug, rather than techniques suited to a mechanical obstruction.

### Quantitative Basis

- 12-in pipeline; WAT for this crude ≈ 95°F. Normal operating temperature at the affected low point: 105°F (10°F margin). During the cold snap, ground/line temperature at that low point fell to **88°F — 7°F below WAT.**
- Throughput had also dropped from a design 8,000 bpd to **4,200 bpd** (a well shut-in reduced feed), roughly doubling residence time and heat loss per unit length.
- Original pigging interval (21 days) was set assuming a deposition rate of ~15 mil/day. Re-running the deposition model with actual flow and temperature history for the affected period estimated the real rate at **42 mil/day.**
- At day 18 of the 21-day interval, modeled wax thickness had reached **≈0.75 in**, reducing effective ID from 12 in to roughly 10.5 in (a **13% area reduction**) at the worst-affected point — consistent with a plug capable of stalling a standard-diameter pig.
- Differential pressure across the pig during the stall spiked from a normal pigging-run range of 15–25 psi to **180 psi.**

## 5. Root Cause

**The established pigging frequency was based on a deposition-rate assumption that no longer reflected actual conditions.** A recent period of colder temperatures and reduced flow rate significantly increased the real wax deposition rate, so far more deposit had accumulated by the scheduled pigging interval than the pig was sized/expected to push through in one pass — causing it to stall against an oversized deposit plug.

## 6. Corrective Action

1. **Freed the stuck pig** using bidirectional flow/pressure techniques appropriate to the pipeline and the deposit-related stall mechanism.
2. Once cleared, ran a **graduated pigging sequence** (progressively larger/more aggressive pigs over successive runs) to safely reduce the deposit backlog without risking another stall.

## 7. Verification

- Subsequent pigging runs completed successfully with differential pressure back in the **20–30 psi normal range** and consistent pig transit speed.
- After 3 graduated cleaning passes, modeled residual deposit thickness at the affected low point dropped to **<0.15 in**, close to the post-clean baseline.
- Updated deposition model, re-run against the new (colder, lower-flow) actual conditions, revised the pigging interval down to **12 days** for the duration of the reduced-throughput period.

## 8. Prevention / Long-Term Fix

- **Tied pigging frequency to a periodically-updated deposition model** (using actual flow and temperature history) rather than a fixed calendar interval that assumes constant operating conditions.
- Established **graduated pig sizing during known high-deposition seasons** (colder periods, reduced-flow operation), so accumulated deposit is addressed incrementally rather than risking a large single-pass stall.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review differential pressure and tracking signal pattern at the time of the stall — a sharp dP spike with a hard stop is more consistent with a deposit plug than gradual mechanical wear
- [ ] Review flow rate and temperature history since the last successful pigging run for conditions favoring higher deposition (low flow, low temperature)
- [ ] Update the pipeline's deposition-rate estimate using **actual** recent operating conditions, not the original fixed design-basis assumption
- [ ] Compare the updated deposit estimate against what the current pigging frequency/pig sizing assumes it will encounter
- [ ] If deposition is confirmed to have outpaced the pigging schedule, plan pig recovery using techniques appropriate for a soft/wax deposit stall (bidirectional flow/pressure), not a mechanical obstruction
- [ ] After recovery, run a graduated pigging sequence rather than immediately resuming the standard pig size/interval
- [ ] Tie future pigging frequency to a periodically-updated deposition model, especially across seasonal operating condition changes

## 10. Key Takeaway

> A fixed pigging interval assumes a fixed deposition rate — but deposition rate moves with flow rate and temperature, both of which change seasonally and operationally. Before treating a stuck pig as an equipment failure, check whether recent conditions (colder weather, reduced throughput) would have driven deposition well above what the pigging schedule assumed, and recover/clean accordingly. A pigging program that isn't periodically re-checked against actual operating history is really just following last year's assumptions.

---

## Related Concepts / Tags

`pipeline-pigging` `stuck-pig` `wax-deposition` `flow-assurance` `pig-tracking` `differential-pressure` `deposition-rate` `Peng-Robinson` `pipeline-operations`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
