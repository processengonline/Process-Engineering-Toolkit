# Troubleshooting Guide: Distillation Column — Overhead Product Off-Spec

> **Category:** Separation Equipment / Distillation
> **Unit:** Distillation Column (tray or packed, electrically heated reboiler)
> **Tools:** UniSim rigorous column model with reboiler duty sensitivity analysis
> **Fluid Package:** Peng-Robinson (PR) or SRK, depending on the hydrocarbon system (specific package not stated in original case notes)
> **Symptom:** Overhead product gradually drifting off spec despite stable feed and normal-looking steam pressure

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Overhead product gradually drifted off specification |
| Initially unclear | Whether this was a process deficiency (insufficient reboiler duty) or an instrumentation/equipment fault hiding behind a normal-looking reading |
| Actual root cause | Malfunctioning thyristor (SCR power controller) delivering only ~70% of required power to the electric reboiler heater — while the operator display showed the correct setpoint |
| Fix | Replace the thyristor |
| Diagnostic signal | Simulated overhead composition (using actual feed data + reboiler duty sensitivity) matched plant data only when duty was reduced — pointing at duty, not feed or trays |
| Prevention | Periodic checks that verify **actual heater duty** against controller output, not just the setpoint display |

---

## 2. Symptom

- Overhead product **gradually drifted off specification** — not a sudden step change, which matters diagnostically (see Section 3).
- **Feed conditions were stable.**
- **Steam pressure looked normal** — except this unit uses an **electrically heated reboiler**, so "steam pressure" here refers to a related utility/indicator that was not, in the end, the limiting factor (see Root Cause).

## 3. Why This Wasn't a Simple Feed or Tray Problem

A **gradual** drift with **stable feed** and a **normal-looking heat source indicator** creates ambiguity between two very different fix paths:

1. **Process deficiency** — insufficient reboiler duty, genuinely not enough heat being delivered to generate the vapor traffic needed for separation.
2. **Instrumentation/equipment problem** — the heat source indicator is telling the operator everything is fine, while the actual delivered energy is not what the display shows.

These require completely different troubleshooting paths (steam/heater-side vs. electrical/controller-side), so before dispatching a field team, the priority was determining **which one** was actually happening — using simulation to test the "insufficient duty" hypothesis quantitatively rather than guessing.

## 4. Diagnostic Approach

### Step 1 — Build a rigorous column model with actual operating data
The column was modeled in **UniSim**, using:
- Actual feed composition
- Actual operating data (pressures, temperatures, flows)

> **Fluid package note:** PR and SRK are both standard choices for hydrocarbon distillation VLE. PR is generally preferred for systems with **lighter components or higher pressure**; SRK tends to be preferred for **closer boiling-point separations at moderate pressure**. The specific package used in this case wasn't recorded in the original notes — when reproducing this type of analysis, choose based on your system's component slate and operating pressure rather than defaulting to one package by habit.

### Step 2 — Run reboiler duty sensitivity analysis
Rather than assuming the reboiler duty shown/implied by the steam-side reading was correct, a **sensitivity study on reboiler duty** was run against overhead composition.

```
Hypothesis tested: Is reduced vapor generation (lower effective reboiler duty)
                    sufficient to explain the observed loss of overhead purity?
```

### Step 3 — Compare simulated composition to plant measurements
The simulation showed that **reduced vapor generation from lower reboiler duty directly explained the loss of overhead purity**, and the predicted composition **matched plant measurements closely** at a reduced-duty case.

**Interpretation:** This is the same core diagnostic pattern used in the TEG dehydration and reciprocating compressor cases — build a model on actual data, then see what condition makes the model agree with reality. Here, the model only matched plant behavior when duty was reduced below its nominal/expected value — which meant duty (not feed composition, not tray/packing performance) was confirmed as the actual driver.

### Step 4 — Redirect the investigation based on the model's conclusion
Because the model confirmed duty was insufficient — not feed or separation efficiency — the field team was directed toward an **electrical inspection of the reboiler**, rather than continuing to troubleshoot the steam side, which had already looked normal and would likely have been a dead end.

### Quantitative Basis

- Overhead purity spec: ≥95 mol%. Baseline held near 96 mol%, drifted to **89 mol% over 3 weeks.**
- Reboiler design duty: 4.2 MMBtu/hr. UniSim sensitivity analysis found that matching the observed 89 mol% overhead composition required a reboiler duty of **2.9-3.0 MMBtu/hr — roughly 70% of design.**
- Following the sensitivity result, direct electrical measurement at the heater element found current of **145 A, against a rated/commanded 205 A (71% of rated)** — despite the controller display showing 100% commanded output. This closely matched the ~70% duty shortfall the model had already identified.

## 5. Root Cause

A **malfunctioning thyristor (SCR power controller)** was delivering only **~70% of required power** to the electric heater. Critically, **the operator display showed the correct setpoint** — the instrumentation the operators were trusting was not reflecting the actual power being delivered. This is a case of the *commanded* value and the *actual delivered* value diverging without any alarm or visible discrepancy at the operator interface.

## 6. Corrective Action

1. Replaced the faulty thyristor.
2. Verified restored reboiler duty.
3. Confirmed overhead product purity returned to specification.

## 7. Verification

- Post-replacement, heater current measured **203 A — 99% of the 205 A rated value.**
- Reboiler duty restored to **4.15 MMBtu/hr**, close to the 4.2 MMBtu/hr design value.
- Overhead purity recovered to **96.2 mol%**, within spec, and held there over the following **30 days.**

## 8. Prevention / Long-Term Fix

- Recommended **periodic checks that verify actual heater duty against controller output**, rather than relying on the setpoint display alone.
- This closes the specific gap that caused the extended drift: a setpoint display that looked correct while the actual delivered energy silently degraded.

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for future distillation column gradual off-spec product events:

- [ ] Confirm feed composition and flow are stable (rules in/out a feed-driven cause)
- [ ] Note whether the drift is **gradual** (favors equipment degradation) or a **step change** (favors an operational/setpoint change)
- [ ] Do not treat a normal-looking utility-side indicator (steam pressure, setpoint display) as proof that duty is actually being delivered — indicators can be correct on the command side and wrong on the delivery side
- [ ] Build/update a rigorous column model using actual feed composition and operating data
- [ ] Run a **reboiler duty sensitivity analysis** against the off-spec product composition
- [ ] If a reduced-duty case matches plant data closely, treat **duty delivery** as confirmed — not feed, not tray/packing efficiency
- [ ] For electrically heated reboilers, direct inspection toward the **power controller/SCR/thyristor**, not just the heater element itself
- [ ] For steam-heated reboilers, the equivalent check is control valve position vs. actual steam flow, not just steam header pressure
- [ ] After repair, verify fix by confirming **actual duty delivered**, not just that the setpoint display reads correctly
- [ ] Add a standing check that periodically cross-verifies actual delivered duty against commanded/setpoint duty

## 10. Key Takeaway

> A setpoint display shows what the system was **told** to do, not necessarily what it's **actually doing**. When a gradual off-spec trend shows up despite everything upstream looking stable, use a duty (or equivalent) sensitivity analysis to test whether reduced delivered energy — not feed, not separation efficiency — explains the data. If it does, inspect the delivery path (controller, thyristor, valve actuator) directly, because the indicator that looks "normal" may only be reporting the command, not the result.

---

## Related Concepts / Tags

`distillation-column` `overhead-product` `off-spec` `reboiler-duty` `sensitivity-analysis` `thyristor` `SCR-controller` `electric-reboiler` `UniSim` `Peng-Robinson` `SRK` `instrumentation-fault` `setpoint-vs-actual`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying. Note: the specific fluid package used in the original case was not documented; PR and SRK are cited as the standard candidates for this service.*
