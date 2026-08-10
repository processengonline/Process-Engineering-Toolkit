# Troubleshooting Guide: Condensate Stabilizer — Off-Spec Reid Vapor Pressure (RVP)

> **Category:** Liquids Processing / Distillation
> **Unit:** Condensate Stabilizer Column
> **Tools:** UniSim rigorous column model, RVP correlation check against light-end composition
> **Fluid Package:** Peng-Robinson (PR), standard for light hydrocarbon condensate VLE and RVP-related light-end behavior
> **Symptom:** Stabilized condensate product RVP creeping above the sales/trucking specification despite reboiler temperature holding at its normal setpoint

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Stabilized condensate RVP gradually rising above spec despite reboiler temperature at its normal setpoint |
| Initially unclear | Whether insufficient stripping (a column performance issue) or a feed composition change (more light ends arriving) was driving the RVP rise |
| Actual root cause | Feed condensate light-end (C2/C3) content had increased due to an upstream separator pressure change, exceeding what the column's existing reboiler duty/reflux configuration could strip at the current feed rate — a feed-composition-driven capacity issue, not a column malfunction |
| Fix | Increased reboiler duty and adjusted column pressure to restore adequate stripping for the new feed composition; requested review of upstream separator pressure control |
| Diagnostic signal | UniSim model, run with updated actual feed composition, correctly predicted the observed RVP rise at existing reboiler duty — confirming the column was performing as expected for the new (lighter) feed, not malfunctioning |
| Prevention | Feed composition trending correlated with upstream separator conditions; stabilizer capacity check whenever upstream pressure/composition changes are planned |

---

## 2. Symptom

- **Stabilized condensate RVP gradually rose above the sales/trucking specification.**
- **Reboiler temperature remained at its normal setpoint** — the most obvious lever operators would check first appeared unchanged.

## 3. Why This Wasn't Assumed to Be a Column Malfunction

A normal reboiler temperature with rising product RVP creates the same kind of puzzle seen in the distillation column case (Case Study 4): if the heat input looks right, why is the light-end stripping getting worse? Here, though, the underlying cause turned out to be different — not an equipment fault delivering less heat than commanded, but a **genuine increase in the stripping duty required**, because the feed itself had become richer in light ends. Distinguishing "the column isn't doing its job" from "the column's job just got harder" required checking feed composition, not just reboiler performance.

## 4. Diagnostic Approach

### Step 1 — Confirm reboiler is delivering its commanded duty
Unlike the distillation column case, here the reboiler's actual delivered duty (steam flow/temperature response) was checked and confirmed to be consistent with its setpoint — ruling out an equipment/instrumentation fault as the cause (this is worth explicitly checking, even though it turned out not to be the answer here).

### Step 2 — Review feed condensate composition trend
Feed composition data was reviewed and showed a **noticeable increase in light-end (C2/C3) content** entering the stabilizer over the same period the RVP had been rising.

### Step 3 — Model the column with updated actual feed composition
The stabilizer was modeled in **UniSim** using **PR**, updated with the **actual current feed composition**, at the existing reboiler duty and column pressure.

**Finding:** The model, run with the updated (lighter) feed composition, **correctly predicted RVP rising above spec at the existing reboiler duty** — confirming the column was behaving exactly as expected for its current feed, not malfunctioning. The problem was that the column's existing operating configuration simply didn't have enough stripping capacity for the new, lighter feed.

### Step 4 — Trace the feed composition change upstream
With the column's behavior explained and validated by the model, the investigation moved further upstream to understand *why* feed composition had gotten lighter — tracing it to a **change in upstream separator operating pressure**, which shifted more light ends into the condensate stream feeding the stabilizer rather than staying with the gas phase.

### Quantitative Basis

- Sales/trucking RVP spec: ≤ 10 psi. Baseline product RVP: 8.6 psi, rose to **12.1 psi.**
- Feed condensate C2+C3 content rose from a baseline **3.8 mol% to 7.2 mol%** over the same period.
- Upstream separator operating pressure had crept from **850 psig to 980 psig** (a downstream compression suction pressure increase pushed it up) — higher separator pressure retains more C2/C3 dissolved in the liquid (condensate) phase rather than flashing to the gas phase, directly explaining the richer feed.
- UniSim (PR), run with the updated feed composition at unchanged reboiler duty (3.1 MMBtu/hr) and column pressure, predicted **RVP = 12.4 psi** — closely matching the observed 12.1 psi and confirming the column was behaving exactly as expected for the new feed, not malfunctioning.

## 5. Root Cause

**An upstream separator pressure change increased the light-end (C2/C3) content of the feed condensate entering the stabilizer.** The stabilizer's existing reboiler duty and reflux configuration, while performing exactly as designed, did not have enough stripping capacity to remove the additional light ends at the current feed rate — producing off-spec RVP even though every column-side parameter (reboiler temperature, etc.) looked normal.

## 6. Corrective Action

1. **Increased reboiler duty** and **adjusted column operating pressure** to restore adequate light-end stripping capacity for the new feed composition.
2. **Requested a review of upstream separator pressure control**, since that was the actual source of the compositional shift driving the added stripping load.

## 7. Verification

- Reboiler duty increased from 3.1 to **3.9 MMBtu/hr (26% increase)**, with a modest column pressure reduction to improve relative volatility of the light ends.
- Stabilized condensate RVP returned to **9.4 psi**, within the 10 psi spec, and held in the **9.0–9.6 psi range over the following 30 days.**
- UniSim, re-run with the corrected operating parameters and current (7.2 mol% C2+C3) feed composition, predicted **RVP = 9.3 psi** — matching the recovered plant performance.

## 8. Prevention / Long-Term Fix

- Established **feed composition trending correlated with upstream separator conditions**, so a compositional shift is visible before it manifests as an off-spec product.
- Added a **stabilizer capacity check** as a standard step whenever upstream pressure or composition changes are planned, rather than discovering the capacity shortfall reactively.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm reboiler is actually delivering its commanded duty (steam flow/temperature response), not just that the setpoint looks normal
- [ ] Review feed composition trend, specifically light-end (C2/C3) content, over the period the off-spec condition developed
- [ ] Model the column with the current actual feed composition at existing operating conditions to check whether the observed performance is expected (a capacity/feed issue) or unexpected (a genuine malfunction)
- [ ] If the model confirms the column is performing as expected for a changed feed, don't treat it as an equipment fault — treat it as a capacity/operating-point adjustment need
- [ ] Trace a feed composition change back to its actual upstream source (separator pressure, blending, new well/source coming online, etc.)
- [ ] Adjust reboiler duty/column pressure to restore adequate stripping capacity for the new feed
- [ ] Address the upstream driver where practical, not just the downstream symptom
- [ ] Build feed composition trending and a capacity check into the change-management process for planned upstream changes

## 10. Key Takeaway

> Not every off-spec product with a "normal-looking" reboiler is an equipment problem — sometimes the column is doing exactly what it's designed to do, but the job got harder because the feed changed. Before troubleshooting the column itself, check whether feed composition has shifted, and use a rigorous model with the current actual feed to confirm whether observed performance is expected given that shift. If it is, the fix is adjusting operating conditions (and addressing the upstream driver), not chasing an equipment fault that isn't there.

---

## Related Concepts / Tags

`condensate-stabilizer` `RVP` `reid-vapor-pressure` `light-ends` `stripping-capacity` `feed-composition` `UniSim` `Peng-Robinson` `separator-pressure`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
