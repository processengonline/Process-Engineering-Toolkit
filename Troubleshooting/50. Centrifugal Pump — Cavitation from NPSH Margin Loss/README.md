# Troubleshooting Guide: Centrifugal Pump — Cavitation from NPSH Margin Loss

> **Category:** Rotating Equipment / Pump Hydraulics
> **Unit:** Centrifugal Charge Pump, upstream of a process unit
> **Tools:** NPSH available (NPSHa) hydraulic calculation using suction vessel conditions and fluid vapor pressure
> **Fluid Package:** PR/SRK, used to determine hydrocarbon liquid vapor pressure at suction temperature
> **Symptom:** Increasing pump noise/vibration, discharge pressure oscillation, and early seal leakage

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Pump noise and vibration increasing; discharge pressure oscillating; mechanical seal leakage beginning |
| Initially unclear | Mechanical/seal issue vs. a hydraulic (cavitation) condition |
| Actual root cause | Suction vessel level had drifted below its design operating point (upstream level control drift), and rising feed temperature increased fluid vapor pressure — together reducing NPSH available below NPSH required |
| Fix | Restored suction vessel level to design setpoint; reviewed level control tuning |
| Diagnostic signal | Symptoms (noise, vibration, discharge oscillation) classic for cavitation; NPSHa calculation using actual level and temperature showed margin had collapsed |
| Prevention | NPSH margin monitoring against vapor pressure trend with temperature; low-level alarm on suction vessel |

---

## 2. Symptom

- **Increasing pump noise and vibration** — often described as a "gravel" or crackling sound characteristic of cavitation.
- **Discharge pressure oscillating**, rather than holding steady.
- **Mechanical seal leakage began** — a downstream consequence of sustained vibration and pressure instability.

## 3. Why This Wasn't Immediately Treated as a Seal Failure

Seal leakage alone often triggers a straightforward seal-replacement work order. But here it appeared **alongside** noise, vibration, and discharge oscillation — a symptom cluster more consistent with an underlying **hydraulic** problem (cavitation) than a standalone mechanical seal failure. Replacing the seal without addressing an active cavitation condition would likely just repeat the failure. The priority was determining whether cavitation was occurring, and if so, why.

## 4. Diagnostic Approach

### Step 1 — Recognize the symptom cluster as classic cavitation indicators
Noise, vibration, and discharge pressure oscillation together are a well-known signature of cavitation (vapor bubble formation and collapse at the impeller), not a typical standalone seal or bearing fault pattern.

### Step 2 — Calculate NPSH available (NPSHa) using actual operating conditions
NPSHa was calculated from:
- Actual suction vessel level (affecting static head)
- Actual suction line losses
- **Fluid vapor pressure at current suction temperature**, determined via PR/SRK

```
NPSHa = (static head from level) + (pressure head) − (friction losses) − (vapor pressure head)
```

### Step 3 — Compare NPSHa to NPSH required (NPSHr)
The calculation showed NPSHa had dropped close to, or below, the pump's NPSHr — confirming cavitation was hydraulically expected under current operating conditions, not just suspected from symptoms alone.

### Step 4 — Identify what changed
Two contributing factors were identified together:
- **Suction vessel level had drifted lower than design**, due to upstream level control drift — directly reducing the static head component of NPSHa.
- **Feed temperature had risen**, increasing the fluid's **vapor pressure** — directly increasing the vapor pressure term that subtracts from NPSHa.

Both effects moved in the same direction simultaneously, compounding the NPSH margin loss.

### Quantitative Basis

- Pump NPSHr (vendor curve, current flow): **12.5 ft.**
- Baseline NPSHa (design suction level 65%, design feed temp 180°F): **18.2 ft — a 5.7 ft margin.**
- Suction vessel level had drifted from 65% to **38%**, reducing static head contribution by an estimated **4.1 ft.**
- Feed temperature rose from 180°F to **205°F**; via PR, fluid vapor pressure rose from 7.5 psia to **11.8 psia**, increasing the vapor pressure head deduction by an estimated **3.3 ft.**
- Recalculated NPSHa at degraded conditions: 18.2 − 4.1 − 3.3 = **10.8 ft — below the 12.5 ft NPSHr, a 1.7 ft deficit.**

## 5. Root Cause

**A combination of lower-than-design suction vessel level (from upstream level control drift) and higher feed temperature (increasing fluid vapor pressure) reduced NPSH available below NPSH required**, causing the pump to cavitate — producing the observed noise, vibration, discharge pressure oscillation, and consequent seal leakage.

## 6. Corrective Action

1. Restored suction vessel level to its design operating setpoint.
2. Reviewed and adjusted upstream level control tuning to prevent recurring drift.

## 7. Verification

- Suction level restored to **63%**, feed temperature corrected to **182°F**; recalculated NPSHa returned to **17.6 ft — a 5.1 ft margin** over the 12.5 ft NPSHr.
- Pump vibration dropped from **0.42 in/s to 0.11 in/s**, and discharge pressure stabilized.
- Seal leakage stopped; held with no recurrence over the following **14 days.**

## 8. Prevention / Long-Term Fix

- Established **NPSH margin monitoring** that accounts for vapor pressure changes with temperature, not just a static level check.
- Added a **low-level alarm** on the suction vessel tied to the NPSH-critical range, rather than a generic low-level alarm unrelated to pump protection.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Recognize noise/vibration/discharge oscillation together as a likely cavitation signature before treating seal leakage as an isolated mechanical fault
- [ ] Calculate NPSHa using **actual** current suction level, line losses, and fluid vapor pressure — not design-basis assumptions
- [ ] Determine fluid vapor pressure at the **actual current suction temperature**, since vapor pressure is highly temperature-sensitive
- [ ] Compare calculated NPSHa against the pump's NPSHr (from vendor curve)
- [ ] If margin has collapsed, identify which contributing factor(s) changed: suction level, suction line losses, or temperature/vapor pressure
- [ ] Correct the upstream condition (level control, temperature control) rather than only replacing downstream-damaged components (seals, bearings)
- [ ] Add NPSH margin as a monitored, temperature-aware parameter — not a one-time design check
- [ ] Set low-level alarms based on the level at which NPSH margin becomes critical, not an arbitrary generic threshold

## 10. Key Takeaway

> Seal leakage, vibration, and noisy operation are often treated as separate mechanical issues to fix independently — but together, they're a strong cavitation signature. NPSH margin isn't a one-time design number; it moves with **both** suction level and fluid temperature (via vapor pressure), so a pump that was fine for years can start cavitating purely from a level control drift or a feed temperature creep, with no mechanical change to the pump itself. Recalculate NPSHa with actual current conditions before replacing mechanical components.

---

## Related Concepts / Tags

`centrifugal-pump` `cavitation` `NPSH` `NPSHa` `NPSHr` `vapor-pressure` `mechanical-seal` `suction-vessel-level` `pump-hydraulics` `level-control`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
