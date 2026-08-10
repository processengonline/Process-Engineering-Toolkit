# Troubleshooting Guide: Flare Knockout Drum — Liquid Carryover to Flare Tip

> **Category:** Relief & Flare Systems / Safety-Critical Equipment
> **Unit:** Flare Knockout (KO) Drum
> **Tools:** Relief/blowdown hydraulic review (API 521-based sizing check), KO drum level trend review
> **Fluid Package:** PR, used for the relief stream composition/properties in the hydraulic check
> **Symptom:** Liquid observed falling ("raining") or burning droplets at the flare tip during a relief event

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Liquid carryover (rain/burning droplets) observed at the flare tip during a relief event |
| Initially unclear | Whether the KO drum was undersized for this event, or whether something had reduced its effective performance |
| Actual root cause | KO drum liquid level was already higher than assumed, due to slow inventory buildup from a leaking PSV providing continuous minor relief — reducing available vapor disengagement space when the larger relief event occurred |
| Fix | Drained the KO drum; identified and repaired the leaking valve |
| Diagnostic signal | Level trend showed a slow, sustained rise in KO drum inventory over time prior to the event, inconsistent with a single relief occurrence |
| Prevention | KO drum level monitoring; PSV leak testing program; periodic drum inspection |

---

## 2. Symptom

- **Liquid carryover (rain or burning droplets) observed at the flare tip** during a relief event — a safety and environmental concern, since the KO drum's entire purpose is to prevent this.

## 3. Why This Wasn't Assumed to Be a Sizing Problem

The instinctive explanation for liquid carryover is that the relief event exceeded the KO drum's design liquid handling capacity or vapor disengagement space. But before concluding the drum itself was undersized for this scenario — a conclusion with significant design/capital implications — it was worth checking whether the drum was actually starting the event with its **design-assumed empty/low liquid level**, or whether it was already partially full from an unrelated cause.

## 4. Diagnostic Approach

### Step 1 — Review the relief event against the KO drum's hydraulic design basis
An API 521-based hydraulic check was performed for the specific relief event (flow rate, composition via PR properties) against the KO drum's rated liquid handling and vapor disengagement capacity.

### Step 2 — Review KO drum liquid level trend leading up to the event
Rather than assuming the drum started empty (per typical design basis), the **level trend prior to the event** was reviewed.

**Finding:** Liquid level had been **slowly and steadily rising** over a period of time before the relief event — inconsistent with a single, isolated relief occurrence. This indicated an ongoing, low-rate liquid input to the drum unrelated to the event itself.

### Step 3 — Identify the source of the slow inventory buildup
The gradual buildup was traced to a **leaking PSV providing continuous minor relief** into the flare header — small enough not to trigger any alarm on its own, but sufficient to slowly fill the KO drum over time.

### Step 4 — Connect reduced available volume to the carryover event
With the drum's starting liquid level already elevated from the leaking PSV, the **available vapor disengagement space and liquid holdup capacity for the actual relief event were significantly reduced** compared to the design assumption of a near-empty drum — directly explaining the carryover.

### Quantitative Basis

- KO drum design total volume: 1,200 bbl, with **950 bbl design-assumed available** capacity above a normal 250 bbl operating heel.
- Level trend rose from a baseline **18% to 61% over 11 days** prior to the event — a slow, steady climb inconsistent with the single relief occurrence.
- The leaking PSV was found relieving continuously at an estimated **0.8 gpm**. Over 11 days that totals ≈271 bbl, closely matching the observed level rise.
- API 521 sizing check for the actual relief event required **340 bbl of liquid handling capacity**. At the elevated 61% starting level, only **≈370 bbl of the 950 bbl design-assumed capacity remained** — a margin thin enough that any additional entrainment or surge pushed liquid to the tip.

## 5. Root Cause

**A leaking PSV was continuously relieving a small amount of fluid into the flare header, slowly filling the KO drum over time.** When the larger relief event occurred, the drum's liquid level was already elevated, leaving insufficient disengagement space and liquid handling capacity — causing liquid to carry over to the flare tip.

## 6. Corrective Action

1. **Drained the KO drum** to restore available capacity.
2. **Identified and repaired the leaking PSV** causing the ongoing minor relief.

## 7. Verification

- KO drum level returned to and held its normal **15–20% baseline over the following 45 days**, confirming the slow rise had stopped following PSV repair.
- No further carryover reported on subsequent relief events.

## 8. Prevention / Long-Term Fix

- Established **ongoing KO drum level monitoring** as a standing check, not just an event-response check.
- Implemented a **PSV leak testing program** to catch minor/continuous leakage before it silently consumes KO drum capacity.
- Added **periodic drum inspection** to the maintenance plan.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm the relief event's flow/composition against the KO drum's design hydraulic basis (API 521 check)
- [ ] Before concluding the drum is undersized, review the **liquid level trend leading up to the event** — not just the event itself
- [ ] A slow, sustained level rise prior to the event indicates an ongoing input unrelated to the event — investigate for a leaking relief valve or other continuous minor contributor
- [ ] Trace any identified leak to its source and repair it
- [ ] Drain the KO drum to restore design-assumed available capacity
- [ ] After repair, confirm the drum returns to and holds its normal baseline level (not just a one-time drain)
- [ ] Add standing KO drum level monitoring and a PSV leak testing program, since minor continuous leaks are easy to miss without deliberate checking

## 10. Key Takeaway

> A flare KO drum's protection against liquid carryover assumes it starts each relief event with its design-assumed available capacity — usually near-empty. If the drum is already partially full from an unrelated, easy-to-miss source like a slowly leaking PSV, even a properly-sized drum can carry over liquid on a legitimate relief event. Before concluding equipment is undersized, check whether it was actually starting from where the design basis assumed.

---

## Related Concepts / Tags

`flare-system` `knockout-drum` `liquid-carryover` `API-521` `PSV-leakage` `relief-system` `vapor-disengagement` `flare-tip` `safety-critical-equipment`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
