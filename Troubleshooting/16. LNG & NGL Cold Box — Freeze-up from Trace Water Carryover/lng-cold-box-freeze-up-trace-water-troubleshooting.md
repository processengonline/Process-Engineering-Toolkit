# Troubleshooting Guide: LNG/NGL Cold Box — Freeze-up from Trace Water Carryover

> **Category:** Cryogenic Processing / Flow Assurance
> **Unit:** Cryogenic Cold Box / Brazed Aluminum Heat Exchanger (BAHX), NGL Recovery Section
> **Tools:** Cryogenic process simulation (low-temperature VLE) plus moisture/freeze-out risk review
> **Fluid Package:** Peng-Robinson (PR) with appropriate low-temperature binary interaction parameters, combined with a moisture/freeze-point check since PR alone does not predict solid ice/hydrate-like freeze-out of trace water
> **Symptom:** Increasing pressure drop across a cold box passage with a localized outlet temperature deviation, progressing toward partial flow restriction

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Rising differential pressure across a specific cold box passage; localized low outlet temperature deviation; developing partial flow restriction |
| Initially unclear | Whether this was a process condition change, an instrumentation issue, or physical blockage inside the BAHX |
| Actual root cause | A brief upstream molecular sieve breakthrough allowed trace water to slip past the dryer beds and freeze out inside the cryogenic exchanger passages, building an ice/hydrate-like blockage |
| Fix | Controlled warm-up/deicing of the cold box; confirmed upstream mol sieve moisture performance was corrected before resuming |
| Diagnostic signal | dP rise and localized temperature deviation consistent with a developing internal restriction, cross-referenced against upstream dehydration performance history |
| Prevention | Installed/verified online moisture analyzer downstream of the mol sieve beds, closing the detection gap that allowed the breakthrough to go unnoticed |

---

## 2. Symptom

- **Rising differential pressure across a specific cold box passage.**
- **A localized low outlet temperature deviation** on that passage.
- Progressing over time toward a **partial flow restriction**.

## 3. Why This Wasn't Assumed to Be a Simple Process Upset

Rising dP and a localized temperature deviation in a cryogenic exchanger can result from several distinct causes: a genuine process rate/composition change, an instrumentation fault, or physical blockage inside the exchanger passages. Given the safety and reliability stakes of a cryogenic cold box, it was necessary to determine the actual mechanism — particularly whether **trace water** (which is catastrophic in cryogenic service, since it freezes solid) had made it past the upstream dehydration system.

## 4. Diagnostic Approach

### Step 1 — Confirm the symptom pattern is consistent with an internal restriction
The combination of rising dP and a localized (not uniform) outlet temperature deviation pointed toward a developing **physical restriction inside a specific passage**, rather than a broad process condition change that would typically affect multiple passages more uniformly.

### Step 2 — Cross-reference against upstream dehydration performance
Given that cold box freeze-up is a well-known consequence of trace water carryover, upstream **molecular sieve dehydration performance history** was reviewed for any recent anomaly.

> **This connects directly to the molecular sieve case (Case Study 10):** a brief regeneration or cycle-timing issue on the mol sieve beds can allow a short window of water breakthrough that wouldn't necessarily register as an obvious upset at the time, but has serious downstream consequences once that moisture reaches cryogenic temperatures.

**Finding:** A **brief mol sieve breakthrough event** was identified in the historical record — a short-duration water slip that had not been caught by the process at the time.

### Step 3 — Confirm the freeze-out mechanism
With bulk gas confirmed to be well below the freezing point of water in this section of the cold box, even a small amount of carried-over moisture would be expected to **freeze out and accumulate** on the exchanger's internal passages, consistent with the observed localized dP rise and temperature deviation.

### Step 4 — Plan a controlled resolution
Given the safety-critical nature of cryogenic equipment, resolution required a **controlled warm-up/deicing procedure** rather than an abrupt intervention, to safely melt and clear the ice without risking mechanical damage to the aluminum exchanger.

### Quantitative Basis

- Passage design dP at rated flow: 8 psi. Trended actual dP rose from **8.2 psi to 34 psi over 9 days.**
- Passage design outlet temperature: −152°F. Localized readings drifted to **−139°F — 13°F warmer**, while neighboring passages held steady at **−150°F to −154°F.**
- Retrospective review of the upstream mol sieve moisture analyzer found a **40-minute window where outlet dew point spiked to −35°F** against a −100°F spec, **5 days prior to the cold box symptom onset** — the undetected breakthrough event responsible for the freeze-out.

## 5. Root Cause

**A brief upstream molecular sieve breakthrough allowed a small amount of water to slip into the cryogenic section**, where it **froze out inside the brazed aluminum exchanger passages**, progressively restricting flow and producing the observed rising differential pressure and localized temperature deviation.

## 6. Corrective Action

1. Performed a **controlled warm-up/deicing** of the affected cold box passage.
2. **Verified upstream mol sieve moisture performance had been corrected** (see Case Study 10-style investigation) before resuming cryogenic operation.
3. Resumed normal operation once ice was cleared and upstream dehydration was confirmed sound.

## 7. Verification

- Passage differential pressure returned to **8.4 psi**, close to the 8 psi design value.
- Outlet temperature deviation resolved, reading **−151°F** — within 1°F of the −152°F design value.
- No recurrence over the following **30 days**, with continuous online moisture monitoring confirming outlet dew point held below −100°F throughout.

## 8. Prevention / Long-Term Fix

- **Installed/verified an online moisture analyzer downstream of the mol sieve beds**, closing the detection gap that had allowed the earlier breakthrough to go unnoticed until it manifested as a cold box symptom well downstream.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm whether rising cold box dP and temperature deviation are localized to a specific passage (favors internal restriction) or broad/uniform (favors a process rate/composition change)
- [ ] Review upstream dehydration (mol sieve or equivalent) performance history for any recent breakthrough, regeneration anomaly, or cycle-timing issue
- [ ] Recognize that even a brief, short-duration moisture slip can cause a lasting cryogenic freeze-out problem — don't dismiss a past minor upstream anomaly as irrelevant just because it was brief
- [ ] Confirm bulk gas temperature in the affected section is below water's freeze point, supporting the freeze-out hypothesis
- [ ] Plan resolution as a **controlled** warm-up/deicing procedure appropriate to cryogenic/BAHX equipment — do not attempt abrupt thermal intervention
- [ ] Before resuming cryogenic operation, confirm upstream dehydration performance has been corrected and verified, not just that the ice has cleared
- [ ] Install or verify continuous moisture monitoring downstream of the dehydration system as an early-warning layer specifically protecting the cryogenic section

## 10. Key Takeaway

> Cryogenic cold box problems are very often **upstream** problems that took time to manifest — a brief mol sieve breakthrough that seemed inconsequential at the time can show up much later as a localized freeze-up deep inside a BAHX passage. When you see a developing internal restriction in cryogenic service, check upstream dehydration history before assuming a cold-box-specific mechanical cause, and treat online moisture monitoring downstream of the dryers as a safety-critical detection layer, not an optional nicety.

---

## Related Concepts / Tags

`cold-box` `BAHX` `freeze-up` `cryogenic-processing` `trace-water` `molecular-sieve-breakthrough` `NGL-recovery` `moisture-analyzer` `flow-assurance` `Peng-Robinson`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
