# Troubleshooting Guide: Cathodic Protection System — Rising Pipeline Corrosion Rate Despite Normal Rectifier Output

> **Category:** Integrity Management / Corrosion Control
> **Unit:** Buried Pipeline — Impressed Current Cathodic Protection (ICCP) System
> **Tools:** Pipe-to-soil potential (P/S) survey, rectifier output trending, coating condition assessment (DCVG/CIS survey)
> **Fluid Package:** Not applicable — this is an electrochemical corrosion protection investigation, not a process simulation
> **Symptom:** Corrosion coupon/ER probe data showing an increasing external corrosion rate on a buried pipeline segment, despite the cathodic protection rectifier operating at its normal output

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Increasing external corrosion rate detected on a buried pipeline segment, despite the CP rectifier delivering its normal, unchanged output current/voltage |
| Initially unclear | Whether the CP system itself was underperforming (undersized/failing) or something specific to this segment was preventing adequate protection from reaching the pipe surface, despite normal overall rectifier output |
| Actual root cause | A section of disbonded/damaged pipeline coating was "shielding" that segment of pipe from the impressed current, so even though overall rectifier output was normal and pipe-to-soil potential looked adequate at test stations, the actual steel surface under the disbonded coating was not receiving protective current |
| Fix | Excavated and repaired the coating in the affected section; verified direct-current-voltage-gradient (DCVG) or close-interval survey (CIS) confirmed restored protection at that specific location |
| Diagnostic signal | Overall rectifier output and nearby test station pipe-to-soil potentials looked normal, but a close-interval or DCVG survey specifically over the affected segment identified a localized potential shift consistent with coating shielding |
| Prevention | Periodic DCVG/CIS survey coverage (not just test station point readings) to catch localized shielding; coating condition assessment tied into the CP monitoring program |

---

## 2. Symptom

- **Corrosion coupon/electrical resistance (ER) probe data showed an increasing external corrosion rate** on a specific buried pipeline segment.
- The **cathodic protection rectifier was operating at its normal, unchanged output** current and voltage — the most obvious CP system health indicator looked fine.

## 3. Why This Wasn't Assumed to Be a Rectifier/CP System Capacity Issue

Rising corrosion rate on a cathodically protected pipeline is often first suspected to mean the CP system itself is underperforming — insufficient current output, a failing rectifier, or a system that's become undersized as the pipeline ages or soil conditions change. But here, rectifier output was already confirmed normal, and standard test station pipe-to-soil potential readings (typically taken at fixed intervals) also looked acceptable. This meant the problem, if real, had to be **localized** — something preventing protective current from reaching the steel at this specific segment, invisible to point measurements taken elsewhere along the line.

## 4. Diagnostic Approach

### Step 1 — Confirm rectifier output and nearby test station readings
Rectifier current/voltage output was confirmed normal, and pipe-to-soil potential readings at the **nearest fixed test stations** were reviewed and found within the acceptable protection criteria — consistent with a functioning CP system overall.

### Step 2 — Recognize the limitation of point-based test station data
Fixed test stations only sample pipe-to-soil potential at specific points, often spaced considerable distances apart. A **localized** issue between test stations — such as a section of shielded coating — would not necessarily be visible in that data, even with a functioning CP system.

### Step 3 — Run a close-interval or DCVG survey over the affected segment
A **close-interval survey (CIS)** or **direct-current-voltage-gradient (DCVG) survey** was conducted specifically over the pipeline segment showing the rising corrosion rate, providing continuous (rather than point-sampled) potential/current data along that section.

**Finding:** The survey identified a **localized potential shift** consistent with **coating shielding** — a section of disbonded or damaged coating that was preventing the impressed current from effectively reaching the underlying steel, even though the surrounding soil and pipe-to-soil potential looked adequate.

### Step 4 — Confirm via excavation
The identified section was excavated, confirming **disbonded/damaged coating** at that specific location, consistent with the survey's shielding indication.

### Quantitative Basis

- ER probe corrosion rate: baseline 1.2 mpy, rose to **6.8 mpy** against an acceptable threshold of <3 mpy for CP-protected pipe.
- Rectifier output held steady at **8.2 A / 22 V DC**, well within its 10 A/30 V rating — no change over the period.
- Nearest fixed test stations (spaced ~1,600 ft apart) both read **−0.95 V and −1.02 V CSE**, more negative than the −0.85 V NACE protection criterion — both indicating adequate protection by the standard point-based check.
- A close-interval survey at 2.5 ft spacing identified a localized shift to **−0.72 V CSE over an 18 ft section** roughly midway between the two test stations — less negative than the −0.85 V criterion, indicating inadequate protection at that specific location. Excavation confirmed **18 ft of disbonded/tented coating** matching the survey findings almost exactly.

## 5. Root Cause

**A section of disbonded/damaged pipeline coating was shielding the underlying steel from the impressed cathodic protection current.** Because overall rectifier output was normal and the nearest fixed test stations happened to be positioned outside the affected segment, this localized shielding was not visible through standard point-based CP monitoring — allowing corrosion to progress at this specific location despite an apparently healthy CP system overall.

## 6. Corrective Action

1. **Excavated and repaired the coating** in the affected section.
2. **Verified restored protection** at that specific location via a follow-up DCVG/CIS survey.

## 7. Verification

- Follow-up CIS survey over the repaired 18 ft section measured potential restored to **−0.91 V CSE**, better than the −0.85 V protection criterion.
- ER probe corrosion rate at the affected segment declined from 6.8 mpy to **1.4 mpy over the following 6 months** of monitoring — back within the acceptable <3 mpy range.

## 8. Prevention / Long-Term Fix

- Established **periodic DCVG/CIS survey coverage** along the pipeline route, rather than relying solely on fixed test station point readings, specifically to catch localized shielding issues that point-based monitoring can miss.
- Integrated **coating condition assessment** into the ongoing CP monitoring program, recognizing that coating and CP system performance are interdependent, not separately-managed parameters.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm rectifier output and nearby fixed test station pipe-to-soil potentials before assuming a CP system capacity/failure issue
- [ ] Recognize that normal rectifier output and normal nearby test station readings do NOT rule out a localized problem between test stations
- [ ] Run a close-interval survey (CIS) or DCVG survey specifically over the segment showing the elevated corrosion rate, for continuous rather than point-sampled data
- [ ] Look for localized potential shifts consistent with coating shielding or disbondment
- [ ] Confirm via excavation before committing to a repair scope
- [ ] Repair the identified coating section and verify restored protection with a follow-up survey at that specific location
- [ ] Confirm corrosion rate recovery via coupon/ER probe monitoring, not just the electrical survey result alone
- [ ] Build periodic CIS/DCVG survey coverage and coating condition assessment into the standing CP monitoring program, rather than relying only on fixed test station readings

## 10. Key Takeaway

> A cathodic protection system can be functioning perfectly at the rectifier and still fail to protect a specific pipeline segment, if disbonded coating is shielding that section from the impressed current. Fixed test station readings only sample specific points and can easily miss a localized shielding problem between stations — when corrosion rate rises despite normal rectifier output and normal nearby test station data, run a close-interval or DCVG survey specifically over the affected segment rather than concluding the CP system needs to be resized or upgraded.

---

## Related Concepts / Tags

`cathodic-protection` `impressed-current` `coating-shielding` `disbonded-coating` `pipe-to-soil-potential` `DCVG` `close-interval-survey` `CIS` `pipeline-corrosion` `integrity-management`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
