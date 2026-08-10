# Troubleshooting Guide: PSV Bench Testing — Set Pressure Drift from Spring Corrosion

> **Category:** Relief Systems / Mechanical Integrity
> **Unit:** Process Pressure Safety Valve (PSV), Corrosive Service
> **Tools:** PSV bench test history trending, spring/internals metallurgical inspection
> **Fluid Package:** Not applicable — this is a mechanical/metallurgical investigation, not a process simulation exercise
> **Symptom:** A PSV found lifting below its stamped set pressure during a routine bench test ("as-found" test failure)

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | PSV as-found bench test result showed the valve lifting below its stamped set pressure |
| Initially unclear | Whether this was a single test anomaly/test equipment issue, or a genuine, developing valve condition |
| Actual root cause | A corrosive service atmosphere was reaching the valve's spring bonnet (via a vent path/bellows issue), progressively corroding the spring and reducing its force output over time |
| Fix | Replaced the valve's internals/spring; corrected the bonnet vent/bellows issue causing corrosive exposure |
| Diagnostic signal | Reviewing as-found set pressure across successive bench tests (not just the latest one) showed a steady downward trend, not a single-event failure |
| Prevention | Trend as-found test results across test cycles for every valve, not just pass/fail; shorten test interval specifically for valves showing a trend rather than applying a uniform interval to all valves |

---

## 2. Symptom

- A PSV in corrosive service was found, during **routine bench testing**, to **lift below its stamped set pressure** — an as-found test failure requiring investigation before the valve could be returned to service or re-certified.

## 3. Why This Wasn't Treated as a One-Off Test Anomaly

A single as-found failure could plausibly be a test equipment calibration issue, a test procedure error, or a genuine but isolated valve condition. Before concluding the valve itself had a developing problem, it was worth checking the **broader test history** for this specific valve — a single low reading is ambiguous, but a *trend* of successively lower as-found set pressures across multiple test cycles is a much stronger and more specific signal of genuine, progressive degradation.

## 4. Diagnostic Approach

### Step 1 — Confirm the test result was not equipment/procedure error
The bench test equipment was cross-checked against a reference standard and the test procedure reviewed — both confirmed valid, ruling out a test-side artifact.

### Step 2 — Review this valve's as-found test history across multiple cycles
Rather than treating the current result in isolation, **historical as-found set pressure data for this specific valve** was pulled across its last several test cycles.

**Finding:** As-found set pressure had been **trending steadily downward** over successive tests — not a single-event failure, but a **progressive, developing condition.**

### Step 3 — Inspect the valve internals
With a genuine progressive trend confirmed, the valve was disassembled and the **spring and internals inspected**.

**Finding:** The spring showed **corrosion pitting**, consistent with a mechanism that would progressively reduce spring force (and therefore set pressure) over time.

### Step 4 — Identify the corrosion exposure pathway
With spring corrosion confirmed as the mechanism, the investigation turned to *why* a spring — normally isolated from the corrosive process fluid by the valve's disc/seat — was being exposed. Inspection found a **bonnet vent/bellows issue** allowing the corrosive service atmosphere to reach the spring compartment.

### Quantitative Basis

- Valve stamped set pressure: 250 psig. As-found result on the failing test: **228 psig — 8.8% below set.**
- Reviewing the prior 3 test cycles (roughly annual): as-found results were **249 psig → 244 psig → 236 psig → 228 psig** — a clear, steady downward trend rather than a single-event drop.
- Spring force measured on the bench: rated **142 lbf** at set condition; measured **126 lbf — an 11% loss**, consistent with the observed set pressure shortfall.
- Visual/metallurgical inspection found corrosion pitting covering an estimated **30% of the spring coil surface area.**

## 5. Root Cause

**A bonnet vent/bellows issue allowed the corrosive service atmosphere to reach the valve's spring compartment**, progressively corroding the spring over multiple years of service. The resulting pitting reduced the spring's effective force output, which directly and predictably lowered the valve's actual set pressure below its stamped value — a slow, cumulative degradation that only became visible as a trend across successive bench tests, not from any single test result alone.

## 6. Corrective Action

1. **Replaced the valve's spring and internals.**
2. **Corrected the bonnet vent/bellows issue** that had been allowing corrosive exposure to the spring compartment.

## 7. Verification

- Post-repair bench test measured set pressure at **251 psig**, within normal test tolerance of the 250 psig stamped value.
- Spring force measured at **141 lbf**, within 1 lbf of the 142 lbf rated value.
- The valve was returned to service and flagged for **closer-interval retesting (annual instead of the standard interval)** to confirm the corrected bonnet vent has stopped the corrosion mechanism going forward.

## 8. Prevention / Long-Term Fix

- Implemented **trending of as-found test results across cycles for every PSV in corrosive service**, not just a pass/fail check on the most recent test — since a trend is visible well before an actual failure occurs.
- Established that valves **showing a developing trend** get a **shortened test interval** specifically, rather than applying the same fixed interval uniformly to every valve regardless of its individual condition history.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm test equipment and procedure are valid before concluding a genuine valve condition
- [ ] Pull as-found test history across multiple prior cycles for the specific valve — don't evaluate a single result in isolation
- [ ] Look for a steady trend (progressive degradation) versus a single-event anomaly
- [ ] If a trend is confirmed, disassemble and inspect the spring/internals for a physical mechanism (corrosion, fatigue, wear)
- [ ] If spring corrosion is found, investigate how the corrosive process atmosphere is reaching a component normally isolated from process fluid (bonnet vent, bellows, seat leakage)
- [ ] Replace internals AND correct the exposure pathway — replacing the spring alone without fixing the exposure just resets the same degradation clock
- [ ] Flag repaired valves for a shortened retest interval to confirm the exposure pathway fix was effective
- [ ] Build as-found trend review (not just pass/fail) into the standing PSV test program for all valves in corrosive or otherwise aggressive service

## 10. Key Takeaway

> A single PSV as-found test failure is ambiguous — but pulling that valve's test history across several cycles turns ambiguity into a clear signal. A steadily declining set pressure trend points to a genuine, progressive mechanical cause (very often spring corrosion from an exposure pathway that shouldn't exist), and fixing only the symptom — replacing the spring — without finding and correcting how corrosive atmosphere reached it in the first place just restarts the same clock.

---

## Related Concepts / Tags

`PSV` `pressure-safety-valve` `set-pressure-drift` `spring-corrosion` `bench-test` `as-found-testing` `bonnet-vent` `bellows` `relief-valve` `mechanical-integrity`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
