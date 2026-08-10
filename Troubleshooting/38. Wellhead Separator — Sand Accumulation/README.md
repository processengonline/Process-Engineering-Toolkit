# Troubleshooting Guide: Wellhead Test Separator — Sand Accumulation Causing Erosion and Level Control Instability

> **Category:** Separation Equipment / Upstream Production
> **Unit:** Wellhead Test Separator (two- or three-phase), Well Testing Service
> **Tools:** Level control trend review, sand probe/erosion monitoring data, internal inspection
> **Fluid Package:** PR, used for flow/velocity calculations relevant to erosion assessment; separator internals hydraulics reviewed independently
> **Symptom:** Liquid level control becoming erratic and increasingly difficult to tune on a specific well's test separator, coinciding with a gradual rise in measured erosion/sand production

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Liquid level control on a specific wellhead test separator becoming erratic/hard to tune, coinciding with a rising erosion signal on the sand monitoring probe |
| Initially unclear | Whether this was a level control instrumentation/tuning issue or a physical change inside the vessel affecting how liquid actually behaved |
| Actual root cause | Sand accumulation had built up to the point of intermittently burying and dislodging around the level instrument's lower cage process connection, alternately isolating and reconnecting the cage from true vessel level and producing a sawtooth-pattern level signal, even though the level controller itself was undamaged |
| Fix | Vessel isolated and sand accumulation removed (internal cleaning); level instrument's lower cage process connection inspected/cleared |
| Diagnostic signal | Sand probe erosion trend had been rising steadily over the same period level control became erratic, and internal inspection directly confirmed physical sand accumulation around the level instrument |
| Prevention | Routine sand accumulation monitoring (probe trend + periodic internal inspection) tied to level control performance review; sand jetting/cleanout schedule based on sand production rate rather than a fixed calendar interval |

---

## 2. Symptom

- **Liquid level control on a specific well's test separator became erratic** and increasingly **difficult to tune**, despite no changes to the controller configuration.
- This coincided with a **gradual rise in the erosion signal** from the vessel's sand monitoring probe.

## 3. Why This Wasn't Assumed to Be a Level Control Tuning Problem

Erratic level control is often first addressed as a controller tuning issue — adjusting gain, integral, and derivative parameters to smooth out the response. But the level trend itself had a distinctive **sawtooth pattern** — a slow drift followed by a sudden step change, repeating every few minutes — rather than the smooth noise or steady bias that a tuning problem or a simple sensor drift would typically produce. That specific shape, together with the **coincident rise in the sand erosion signal**, pointed toward an intermittent physical obstruction rather than a control loop issue: a controller can't be tuned into stability if the value it's reading is genuinely jumping between two different states.

## 4. Diagnostic Approach

### Step 1 — Review level control trend alongside sand probe erosion trend
Level control variability was plotted alongside the vessel's sand monitoring probe erosion signal over the same time period.

**Finding:** Both trends **developed together** — level control became progressively more erratic as the sand erosion signal rose, rather than the two being independent, coincidental issues.

### Step 2 — Check whether level controller configuration/tuning had changed
Controller configuration history was reviewed and confirmed unchanged — ruling out a simple tuning drift or accidental reconfiguration as the explanation.

### Step 3 — Consider physical mechanisms consistent with the sawtooth pattern
The separator uses an external cage (bridle-type) level instrument, connected to the vessel through lower and upper process taps. A sawtooth pattern — a slow drift followed by a sudden correction — is a recognized signature of an **intermittently blocking and clearing lower process connection**: as sand accumulates near the tap, flow surges from the well stream periodically pack sand against the connection (isolating the cage from true vessel level, so the reading drifts/holds on a stale value), then dislodge it again (letting the cage suddenly re-equilibrate to actual level, producing the sudden step). An instrument reading a genuinely and continuously disturbed liquid surface, or one that's simply drifted out of calibration, would not typically produce this specific alternating block/clear signature.

### Step 4 — Confirm via internal inspection
The vessel was isolated and internally inspected. Approximately **14 inches of sand accumulation** was found on the vessel floor, with the level instrument's **lower cage process connection roughly 60% buried** — directly consistent with the intermittent block/clear mechanism identified in Step 3, rather than a simple, steady obstruction that would produce a fixed offset instead of a sawtooth pattern.

### Quantitative Basis

- Level swung with a distinctive **sawtooth pattern**, ranging ±18% around setpoint (a slow drift over 2-4 minutes followed by a sudden step correction), rather than random noise — a pattern-level clue distinguishing an intermittent blockage from simple sensor drift or turbulence.
- Sand probe erosion rate rose from 0.5 mil/month to **4.2 mil/month over 5 weeks**, tracking the same timeframe as the onset of level instability.
- Internal inspection found **~14 inches of sand accumulation** on the vessel floor, with the level instrument's lower cage connection **approximately 60% buried.**

## 5. Root Cause

**Sand accumulation on the separator floor, driven by rising sand production from the well, progressively buried the level instrument's lower cage process connection.** Flow surges from the well stream intermittently packed and then dislodged sand at this connection, alternately isolating the cage (causing the level reading to drift or hold on a stale value) and suddenly reconnecting it (causing a sharp correction) — producing the characteristic sawtooth level pattern and a control response no amount of retuning could resolve, since the underlying physical measurement itself was being intermittently interrupted.

## 6. Corrective Action

1. **Isolated the vessel and removed the accumulated sand** through internal cleaning (approximately 14 inches of accumulation removed from the vessel floor).
2. **Inspected and cleared the level instrument's lower cage process connection**, confirming full, unobstructed flow between the vessel and the cage before returning to service.

## 7. Verification

- Following sand removal and clearing of the lower cage connection, level control returned to smooth, stable behavior at its **original tuning parameters** — no retuning was required, confirming the physical obstruction (not the control loop) had been the cause.
- Level variance over the following 14 days measured within ±2% of setpoint, versus the ±18% sawtooth swings observed pre-cleanout.
- Sand probe erosion rate was tracked going forward as the basis for scheduling the next cleanout before accumulation could reach a similar level.

## 8. Prevention / Long-Term Fix

- Established **routine sand accumulation monitoring** (probe trend combined with periodic internal inspection), tied explicitly into level control performance review, so a developing correlation like this one is caught early.
- Implemented a **sand jetting/cleanout schedule based on actual sand production rate**, rather than a fixed calendar interval that may not reflect a particular well's actual sand loading.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Before retuning an erratic level controller, check whether its behavior correlates with any other unrelated trend (e.g., sand probe erosion signal, vibration, differential pressure)
- [ ] Confirm controller configuration/tuning history hasn't changed, to rule out a simple reconfiguration explanation
- [ ] If a physical process trend (like rising sand production) correlates with the control instability, consider whether it could be intermittently interfering with the level instrument's process connection (cage, dip tube, bridle) rather than just changing the process — a sawtooth-shaped trend specifically suggests an intermittent block/clear mechanism, not steady fouling or drift
- [ ] Isolate and internally inspect the vessel to confirm any suspected physical accumulation directly
- [ ] Clean the vessel and clear the level instrument's sensing path
- [ ] Confirm level control returns to stable behavior at its ORIGINAL tuning parameters — needing to retune afterward would suggest the physical cause wasn't fully resolved, or was never the full story
- [ ] Establish routine sand accumulation monitoring tied to level control performance, with cleanout scheduling based on actual sand production rather than a fixed calendar interval

## 10. Key Takeaway

> Erratic level control isn't always a tuning problem — if it develops alongside another physical process trend like rising sand production, check the *shape* of the erratic signal before touching the controller settings. A sawtooth pattern (slow drift, sudden correction, repeat) points to an intermittently blocking and clearing process connection, not random noise or steady fouling. No amount of retuning fixes a level instrument whose connection to the vessel is being periodically interrupted — the real fix is a cleanout, not a retune.

---

## Related Concepts / Tags

`wellhead-separator` `sand-accumulation` `sand-erosion` `level-control` `stilling-well` `dip-tube` `well-testing` `internal-inspection` `sand-jetting`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
