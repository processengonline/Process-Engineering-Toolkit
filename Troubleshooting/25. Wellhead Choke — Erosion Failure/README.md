# Troubleshooting Guide: Wellhead Choke — Erosion-Driven Choke Failure

> **Category:** Wellhead Equipment / Erosion & Flow Assurance
> **Unit:** Wellhead Production Choke (adjustable or fixed-bean)
> **Tools:** Erosional velocity calculation (API RP 14E-based), sand production trend review
> **Fluid Package:** PR, used to determine gas/liquid density and compressibility for erosional velocity and multiphase choke flow calculations
> **Symptom:** Choke position no longer controlling downstream pressure/rate as expected, with a gradually increasing flow rate at a constant choke setting

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Downstream flow rate at a fixed choke setting gradually increasing over time; choke losing its expected pressure-drop/rate control relationship |
| Initially unclear | Whether this was a choke trim mechanical wear issue, a reservoir/well performance change, or something else |
| Actual root cause | Sand production had increased, and erosional velocity through the choke exceeded the recommended limit, progressively eroding/enlarging the choke bean/trim and reducing its effective restriction |
| Fix | Replaced the eroded choke trim; adjusted operating rate to stay within the erosional velocity limit for current sand production; increased choke inspection frequency |
| Diagnostic signal | Flow rate at constant choke position increased steadily while wellhead/flowline pressure data ruled out a reservoir-driven productivity increase; sand production records showed a coincident rise |
| Prevention | Routine erosional velocity check against current sand production rate; choke trim inspection tied to sand production trend, not just a fixed calendar interval |

---

## 2. Symptom

- **At a fixed/unchanged choke setting, downstream flow rate gradually increased over time** — the choke was providing progressively less restriction than it should for the same nominal position.
- The choke was **no longer controlling pressure/rate as expected**.

## 3. Why This Wasn't Assumed to Be a Reservoir/Well Performance Change

An increasing flow rate at a fixed choke setting could plausibly be explained by a genuine change in well productivity (e.g., a skin reduction, a completion change effect, or reservoir pressure behavior). This is a reasonable first hypothesis, since it doesn't necessarily point to equipment failure. But choke trim erosion produces the **same symptom** — more flow at the same nominal setting, because the physical restriction has been worn away — so it was necessary to distinguish between a genuine well-performance change and a mechanical/erosion-driven change in the choke itself.

## 4. Diagnostic Approach

### Step 1 — Review wellhead and flowline pressure data for a reservoir-driven explanation
Wellhead flowing pressure and flowline pressure data were reviewed against expected well performance behavior (e.g., via a nodal-type comparison) to check whether the increased rate was consistent with a genuine productivity change.

**Finding:** The pressure/rate relationship **did not support a straightforward well productivity increase** — the flow increase at constant choke position was better explained by reduced restriction at the choke itself rather than a change upstream in the reservoir/wellbore.

### Step 2 — Review sand production trend
Sand production monitoring records were reviewed and showed a **coincident increase in sand production** over the same period as the flow rate drift — a strong candidate mechanism for choke erosion.

### Step 3 — Calculate erosional velocity for current conditions
Using **PR** to establish current gas/liquid density and compressibility, an **API RP 14E-based erosional velocity calculation** was performed for the choke at current flow conditions and sand production rate.

**Finding:** Erosional velocity through the choke **exceeded the recommended limit** at current operating conditions, consistent with active, ongoing erosion of the choke trim.

### Step 4 — Confirm physically
Choke trim was inspected and confirmed to show **erosion/enlargement** consistent with the calculated erosional risk — directly explaining the reduced restriction at a nominally unchanged choke position.

### Quantitative Basis

- Flow at the nominal 32/64-in choke setting drifted from a baseline **1,850 Mscf/d and 220 bopd to 2,600 Mscf/d and 310 bopd** over 6 weeks, with wellhead flowing pressure essentially unchanged — inconsistent with a reservoir-driven rate increase, which would be expected to show a corresponding pressure decline.
- Sand production rose from a baseline **2 lb/1,000 bbl to 18 lb/1,000 bbl** over the same period.
- API RP 14E erosional velocity limit for continuous service (C = 100) at the current wellstream mixture density (ρm ≈ 10 lb/ft³ at choke conditions, from PR): **Ve = C/√ρm ≈ 32 ft/s.**
- Back-calculating actual velocity through the choke at the drifted flow rate (using the *current*, now-enlarged effective opening) gave **≈55 ft/s — 72% above the 32 ft/s limit**, confirming active erosion rather than a one-time excursion.
- Trim inspection measured the effective bean diameter had grown from 32/64 in (0.500 in) to **≈38/64 in (0.594 in) — a 19% diameter increase, ~41% area increase.**

## 5. Root Cause

**Increased sand production drove erosional velocity through the choke above the recommended limit, progressively eroding and enlarging the choke bean/trim.** This reduced the choke's effective restriction at any given nominal position, causing flow rate to increase over time even though the choke setting itself was unchanged — mimicking, but not actually being, a well productivity increase.

## 6. Corrective Action

1. **Replaced the eroded choke trim.**
2. **Adjusted operating rate** to stay within the erosional velocity limit for the current (higher) sand production level, reducing the rate of future erosion.

## 7. Verification

- Following trim replacement, flow at the 32/64-in setting returned to **1,900 Mscf/d and 225 bopd** — matching the original baseline within normal well variability.
- Operating rate was adjusted so recalculated erosional velocity at current (elevated) sand production holds at **≈26 ft/s, an 18% margin below the 32 ft/s limit.**
- Choke trim re-inspected after 30 days showed **no measurable diameter change** at the new operating rate, confirming erosion had been arrested.

## 8. Prevention / Long-Term Fix

- Established a **routine erosional velocity check tied to current sand production rate**, rather than a one-time design-case calculation.
- Increased **choke trim inspection frequency**, tied to sand production trend rather than a fixed calendar interval, so erosion is caught and addressed before it significantly affects rate control.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm the choke setting has genuinely remained constant (rule out a setpoint/positioner issue first)
- [ ] Review wellhead/flowline pressure data against expected well performance to check whether a reservoir-driven productivity change could explain the increased rate
- [ ] Review sand production trend over the same period
- [ ] Calculate erosional velocity (API RP 14E or equivalent) using **current** flow conditions and sand production rate, not the original design case
- [ ] If erosional velocity exceeds the recommended limit, physically inspect the choke trim for erosion/enlargement
- [ ] Replace eroded trim and adjust operating rate to bring erosional velocity back within limits for current sand production
- [ ] Tie future choke inspection frequency to sand production trend, not a fixed calendar schedule
- [ ] Recognize that "more flow at the same choke setting" can be either a well-performance change or a choke-erosion effect — pressure/rate analysis and an erosional velocity check are both needed to tell them apart

## 10. Key Takeaway

> A choke providing more flow at an unchanged setting can look exactly like a well productivity increase — but it's just as likely to be the choke trim eroding away under high sand production, which quietly changes the choke's actual restriction without anyone touching the setpoint. Before crediting a flow increase to the reservoir, calculate erosional velocity against current sand production and inspect the trim; erosional velocity limits aren't a one-time design check; they need to be re-evaluated whenever sand production changes.

---

## Related Concepts / Tags

`wellhead-choke` `erosional-velocity` `API-RP-14E` `sand-production` `choke-trim-erosion` `multiphase-flow` `Peng-Robinson` `well-performance`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
