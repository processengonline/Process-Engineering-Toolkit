# Troubleshooting Guide: Three-Phase Inlet Separator — Emulsion-Driven Level Instability and Gas Valve Creep

> **Category:** Separation Equipment / Process Chemistry & Control Interaction
> **Unit:** Three-Phase Inlet Separator (oil/water/gas, upstream gas processing facility)
> **Tools:** DCS trend/historian analysis with field lab (bottle test) verification — no steady-state process simulator required
> **Fluid Package:** Not applicable — no thermodynamic simulation was run (see Section 4, Step 1)
> **Symptom:** Liquid level swinging ±10–20% around normal, coupled with an unexplained gas outlet valve creeping open

---

> **Note on case type:** Unlike Case Studies 1–5 (simulation-based diagnosis) and Case Study 6 (simulation-based predictive trending), this case was resolved entirely through **DCS historian analysis, instrumentation verification, and physical lab testing** — no process simulator or fluid package was involved. It's included to show that not every root-cause investigation requires a simulation model; sometimes the fastest and most defensible path is systematic data review + physical confirmation. This is also a good example of **cascading symptoms**: two seemingly separate control loops (liquid level, gas pressure) were actually both downstream effects of a single upstream cause.

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Liquid level swinging 40–70% (normally steady at 50%); gas outlet valve creeping open 3–7% (normally fully closed) |
| Initially unclear | Faulty instrumentation vs. poor control tuning vs. an actual process phenomenon inside the vessel |
| Actual root cause | A stable, slow-settling emulsion (rag layer) reduced effective separation volume; demulsifier dosing had recently been cut during a chemical optimization trial and was no longer sufficient for current crude properties |
| Fix | Restored demulsifier injection rate to its previous optimized value |
| Diagnostic tools | DCS historian trends; transmitter calibration checks; control valve stroke tests; field confirmation of rag layer; lab bottle test of emulsion stability |
| Prevention | New guideline requiring lab bottle tests before any future reduction in demulsifier dosage |

---

## 2. Symptom

Two related but distinct symptoms appeared together:

- **Liquid level instability:** separator level, normally steady at **50%**, began **swinging between 40% and 70%**.
- **Gas outlet valve creep:** the gas outlet pressure control valve, which normally stayed **fully closed** (upstream pressure alone maintained separator pressure), started **creeping open 3–7%** as the controller hunted for a setpoint.
- **No alarms had fired yet** — but the correlated pattern across two different control loops signaled a genuine process upset rather than a nuisance/noise issue.

## 3. Why This Wasn't Immediately Obvious

Two separate control loops misbehaving at the same time could plausibly be explained by several very different fault classes, each requiring a different response:

1. **Faulty instrumentation** — a bad transmitter or valve, which would be a straightforward maintenance fix.
2. **Poor control tuning** — a controller retuning exercise, no physical vessel issue at all.
3. **An actual process phenomenon inside the vessel** — something changing the vessel's real separation behavior, which neither retuning nor instrument replacement would fix.

The task was explicit: figure out which of these it was, **and resolve it without taking the plant down** — ruling things out efficiently mattered as much as finding the answer.

## 4. Diagnostic Approach

### Step 1 — Start with DCS historian trends
Historian trends were pulled for:
- Separator level
- Level control valve position
- Gas outlet pressure and valve position
- Inlet/outlet flows

> **No simulator needed for this step:** this is a case where the fastest path to an answer is systematic trend review, not a process model. Simulation is a tool for testing a hypothesis quantitatively (as in Cases 1–5) or for predicting future behavior (Case 6) — it isn't always the first or best step. Here, the historian data itself was rich enough to start ruling out causes immediately.

**Finding:** **Inlet flow was steady** — this ruled out a **production-driven cause** (e.g., a slug of liquid or a rate change from upstream) as the trigger.

### Step 2 — Verify instrumentation before suspecting process chemistry
Rather than jumping straight to "something's wrong inside the vessel," the more easily-fixed and more common causes were checked first:
- **Level transmitter calibration**
- **Pressure transmitter health**
- **Both control valves** — verified through **stroke tests**

**Finding:** **All instrumentation checked out normal.** This systematically eliminated fault classes 1 and 2 (faulty instrumentation, and by extension made poor tuning alone an unlikely explanation for two independent loops drifting together), and shifted the investigation **inside the vessel** — toward an actual process phenomenon.

### Step 3 — Get field and lab confirmation
With instrumentation cleared, physical evidence was gathered directly:
- **Field operators confirmed a persistent rag layer on the sight glass** — direct visual evidence of an oil/water interface problem.
- **Lab analysis (bottle test) confirmed a stable emulsion settling far slower than normal.**

**Interpretation:** This connected the two original symptoms into one mechanism:
1. The emulsion/rag layer **shrinks the effective separation volume** inside the vessel.
2. As the oil/water interface became unstable, the **level controller kept over-correcting the liquid outlet valve**.
3. Those liquid-side corrections **disturbed separator pressure**, which made the **gas outlet valve creep** in response.

What looked like two unrelated control loop problems was actually **one upstream cause propagating through two downstream control loops**.

### Step 4 — Trace the emulsion back to a process chemistry change
Reviewing **chemical injection logs** revealed that **demulsifier dosing had recently been cut** as part of a chemical optimization trial. The new, lower dosing rate **wasn't sufficient to break the emulsion at current crude properties** — directly explaining why a stable emulsion had started forming when it hadn't before.

### Quantitative Basis

- Separator level swung 40-70% against a normal steady 50% (alarm band 25-85%); gas outlet valve crept from fully closed (0%) to 3-7% open, hunting on a roughly 4-minute cycle.
- Bottle test at the reduced demulsifier rate (9 ppm): emulsion resolved to only 95% water-oil separation after 30 minutes.
- Bottle test at the previous rate (15 ppm): **>99% separation within 10 minutes** — confirming the dosing reduction, not the crude itself, was the driver.

## 5. Root Cause

A recent **reduction in demulsifier injection rate** (part of a chemical optimization trial) was insufficient to break the emulsion at the crude's current properties. The resulting **stable, slow-settling emulsion (rag layer)** reduced effective separation volume and destabilized the oil/water interface, which in turn caused the **level controller to over-correct**, which then **disturbed separator pressure and caused the gas outlet valve to creep open**.

## 6. Corrective Action

1. **Restored demulsifier injection rate to its previous optimized value.**
2. Allowed the emulsion to clear — resolved within a few hours.

## 7. Verification

- **Separator level held at 48-52% over the following 45 days**, versus the previous 40-70% swings.
- **Gas outlet valve remained fully closed (0-1%) throughout**, versus the previous 3-7% creep.
- **No further pressure fluctuations recorded.**
- All achieved **without a shutdown**, meeting the original task constraint.

## 8. Prevention / Long-Term Fix

- Established a **new chemical optimization guideline requiring lab bottle tests before any future reduction in demulsifier dosage**, so process chemistry changes are validated against actual crude behavior before being rolled out plant-wide.

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist when multiple, seemingly unrelated control loops on a three-phase separator start misbehaving together:

- [ ] Pull DCS historian trends for level, valve positions, pressures, and inlet/outlet flows — before assuming any single cause
- [ ] Check inlet flow stability first — rules production changes in or out quickly
- [ ] Verify transmitter calibration (level, pressure) and run control valve stroke tests before suspecting a process/chemistry cause
- [ ] If instrumentation checks out clean, look for a **shared upstream cause** connecting multiple misbehaving loops, rather than tuning each loop independently
- [ ] Get field confirmation (visual: sight glass, rag layer, interface appearance) — don't rely on instrumentation data alone for interface-related issues
- [ ] Run a **lab bottle test** to confirm emulsion stability/settling behavior quantitatively rather than relying on visual impression alone
- [ ] Review **chemical injection logs and recent dosing changes** — a chemistry change is easy to overlook if it happened as part of an unrelated "optimization" initiative
- [ ] Correct the chemistry (restore/adjust demulsifier rate) and confirm resolution against the ORIGINAL symptoms (level stability, valve position, pressure), not just visual clearing of the rag layer
- [ ] Add a validation step (e.g., bottle testing) to the change-management process for any future dosing reduction, so optimization trials don't silently reintroduce the same failure mode

## 10. Key Takeaway

> When two different control loops start misbehaving at the same time, don't tune them separately — look for a **single upstream cause** creating both symptoms. Rule out instrumentation first (it's the fastest, most common, and most fixable explanation), but if everything checks out clean, be willing to go physical: a sight glass observation and a lab bottle test can find what historian trends and stroke tests can't. And when the root cause turns out to be a recent "optimization" change, remember that any dosing/setpoint change to process chemistry should be validated against current feed properties before rollout — not assumed safe because it worked historically.

---

## Related Concepts / Tags

`three-phase-separator` `emulsion` `rag-layer` `demulsifier` `level-instability` `valve-creep` `DCS-historian` `bottle-test` `control-loop-interaction` `chemical-optimization` `process-chemistry` `instrumentation-verification`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying.*
