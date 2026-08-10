# Troubleshooting Guide: Fired Heater — Localized Tube Skin Overheating from Flame Impingement

> **Category:** Fired Equipment / Heat Transfer
> **Unit:** Process Fired Heater (crude/process heater, radiant section)
> **Tools:** Tube skin thermocouple trending, firebox heat flux/combustion review
> **Fluid Package:** Not applicable to the firebox/combustion side; process-side duty calculations typically use PR/SRK for the hydrocarbon process fluid
> **Symptom:** A localized high tube-skin-temperature alarm on specific tubes, while overall heater duty stays within design

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | High tube skin temperature alarm on specific tube-row thermocouples; overall heater duty normal |
| Initially unclear | Whether this was an overall firing/duty issue or a localized problem specific to certain tubes |
| Actual root cause | Burner tip fouling/misalignment causing flame impingement directly onto a tube row, creating asymmetric, locally excessive heat flux |
| Fix | Burner inspection, cleaning, and re-alignment; excess air adjustment |
| Diagnostic signal | Hot spot confined to specific tubes/thermocouples rather than a heater-wide temperature rise, despite normal overall firing rate and process duty |
| Prevention | Periodic burner inspection program; infrared tube skin surveys |

---

## 2. Symptom

- **High tube skin temperature alarm on specific tube-row thermocouples.**
- **Overall heater duty and firing rate remained within design** — this was not a heater-wide overfiring event.

## 3. Why This Wasn't an Overall Firing Problem

If the whole heater were overfired, tube skin temperatures would rise broadly across the radiant section, and process outlet temperature would likely be trending high too. Here, the effect was **localized** — confined to specific tubes — which immediately narrows the search from "the heater is being fired too hard" to "something is happening at a specific burner or tube location." This distinction determines whether the fix is a global combustion adjustment or a targeted mechanical inspection.

## 4. Diagnostic Approach

### Step 1 — Confirm the localized nature of the hot spot
Tube skin thermocouple data across the radiant section was reviewed to confirm the elevated readings were confined to specific tubes/rows, not heater-wide — ruling out a general overfiring or process-side duty issue.

### Step 2 — Review overall combustion parameters
Overall firing rate, excess air, and process fluid duty were checked and found within normal range, further supporting a **localized** rather than global cause.

### Step 3 — Inspect the firebox/burners near the affected tubes
With the hot spot narrowed to a specific location, burners in that vicinity were inspected for **fouling or misalignment** that could cause the flame pattern to deviate from its intended envelope.

### Step 4 — Confirm flame impingement as the mechanism
Inspection identified a burner with **fouling/misalignment causing flame impingement directly onto the adjacent tube row** — an asymmetric, locally excessive heat flux landing on that tube rather than being distributed as designed across the radiant section.

### Quantitative Basis

- Tube skin alarm setpoint: 1,000°F. Localized thermocouples on tube row 14 (2 adjacent tubes) read **1,090°F**, while neighboring rows held **870–910°F** — a 180–220°F spread confined to two tubes.
- Overall firing rate held at **92% of design**; excess O2 held at **3.1%**, within the 2.5–3.5% target band — both confirming no heater-wide overfiring.
- Burner inspection found tip erosion/carbon buildup causing the flame to lean **~12° off-axis** toward tube row 14, consistent with the asymmetric heat flux pattern observed.

## 5. Root Cause

**A fouled/misaligned burner tip caused flame impingement directly onto a specific tube row**, creating localized heat flux well above the design radiant heat flux for that tube, even though overall heater firing and process duty remained within normal limits.

## 6. Corrective Action

1. Inspected and cleaned the affected burner.
2. Re-aligned the burner to restore the intended flame envelope.
3. Adjusted excess air as needed to support stable, properly-shaped combustion.

## 7. Verification

- Tube skin temperature at row 14 dropped from 1,090°F to **895°F**, in line with the 870–910°F range of neighboring rows.
- No further localized high-temperature alarms observed over the following **21 days.**

## 8. Prevention / Long-Term Fix

- Implemented a **periodic burner inspection program** to catch fouling/misalignment before it produces flame impingement.
- Added **infrared tube skin surveys** to detect localized hot spots proactively, rather than relying solely on point thermocouples.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm whether elevated tube skin temperature is localized (specific tubes/rows) or heater-wide (all tubes trending up together)
- [ ] Check overall firing rate, excess air, and process duty against design — rule out general overfiring first
- [ ] If localized, physically inspect the burner(s) nearest the affected tube location for fouling, coking, or misalignment
- [ ] Confirm flame pattern/impingement visually or via infrared survey where possible, not just by inference
- [ ] Clean/re-align the burner and adjust excess air as needed
- [ ] Verify the specific affected thermocouples return to normal, in line with neighboring tubes
- [ ] Add periodic burner inspection and infrared tube skin surveys to the maintenance program, rather than relying only on fixed-point thermocouple alarms

## 10. Key Takeaway

> A localized tube hot spot with normal overall heater duty is a **burner/flame-pattern problem**, not a firing-rate problem — don't cut overall duty in response to a localized alarm, since that both under-treats the fired heater's actual capability and doesn't fix the underlying flame impingement. Confirm whether the issue is localized or heater-wide first; that single distinction points to two completely different fixes.

---

## Related Concepts / Tags

`fired-heater` `flame-impingement` `tube-skin-temperature` `burner-fouling` `burner-alignment` `radiant-section` `infrared-survey` `combustion` `process-furnace`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
