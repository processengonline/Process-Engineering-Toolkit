# Troubleshooting Guide: Vapor Recovery Unit Compressor — Nuisance Trips from Tank Blanket Gas Composition Swings

> **Category:** Vapor Recovery / Rotating Equipment
> **Unit:** Vapor Recovery Unit (VRU) Compressor, Storage Tank Vapor Collection System
> **Tools:** VRU compressor performance trending, tank vapor composition sampling
> **Fluid Package:** Peng-Robinson (PR), used to assess compressibility and dew point behavior of the variable tank vapor stream
> **Symptom:** VRU compressor tripping intermittently on high discharge temperature or low suction pressure, with no consistent pattern tied to tank level or throughput

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Intermittent VRU compressor trips (high discharge temperature, low suction pressure) with no clear correlation to tank level or vapor throughput |
| Initially unclear | Mechanical/control issue on the compressor vs. a variable feed-composition issue from the tanks it serves |
| Actual root cause | Tank vapor composition swung significantly depending on which crude/product was being loaded/received at a given time, periodically producing a much lighter or heavier vapor than the compressor's control logic assumed, pushing operation outside its stable range |
| Fix | Widened/adjusted compressor control setpoints to accommodate the actual composition range; added vapor composition monitoring to correlate trips with specific tank service |
| Diagnostic signal | Trip events correlated with specific tank-receiving activities rather than with throughput rate or tank level alone |
| Prevention | Real-time or periodic vapor composition sampling correlated to tank service; control logic reviewed against the full expected composition range, not a single design case |

---

## 2. Symptom

- **VRU compressor tripping intermittently** on **high discharge temperature** or **low suction pressure** alarms.
- **No consistent pattern** with tank level or overall vapor throughput rate — ruling out the most intuitive explanations first.

## 3. Why This Wasn't Assumed to Be a Straightforward Mechanical Problem

Intermittent compressor trips are often first investigated as a mechanical or control tuning issue specific to the machine. But a VRU compressor's feed — vapor displaced from multiple storage tanks — is inherently **variable in composition**, since different tanks may hold different products or crude grades at different times. Before focusing on the compressor itself, it was worth checking whether the trips correlated with **what was happening on the tank farm side**, not just the compressor's own operating parameters.

## 4. Diagnostic Approach

### Step 1 — Review trip events against throughput and tank level
Trip timing was checked against vapor throughput rate and tank levels — no clear, consistent correlation was found, ruling out the most obvious rate/level-driven explanations.

### Step 2 — Review trip events against tank-receiving activity
Trip timestamps were cross-referenced against records of **which tank was actively receiving/loading** at the time of each trip.

**Finding:** Trips correlated much more closely with periods when **specific tanks (holding lighter or heavier products/crude grades) were actively being filled**, generating a surge of vapor with significantly different composition than the compressor's control logic was tuned for.

### Step 3 — Sample and analyze vapor composition during a trip-correlated event
Vapor composition samples taken during a period correlated with trips confirmed a **significant compositional swing** (much lighter or heavier than the baseline/design case) coinciding with the specific tank's receiving activity.

### Step 4 — Assess compressibility/dew point behavior for the swung composition
Using **PR**, the compressibility and dew point behavior of the swung composition was checked against the compressor's operating envelope, confirming that this composition would push discharge temperature and/or suction pressure outside the compressor's stable control range under the existing setpoints.

### Quantitative Basis

- Design/baseline tank vapor: MW ≈ 50 (propane/butane-rich flashed vapor).
- During **condensate tank filling**, sampled vapor MW dropped to **34** — significantly lighter. At the same mass throughput, this raises volumetric flow enough that suction pressure sagged from a normal 2.0 psig to **1.1 psig, tripping the 1.5 psig low-suction alarm.**
- During **crude tank filling**, sampled vapor MW rose to **65** — heavier, higher effective compression ratio for the same suction/discharge pressures. Discharge temperature rose from a normal ~270°F to **315°F, tripping the 300°F high-discharge-temperature alarm.**
- Both trip types correlated to within ±10 minutes of the respective tank's receiving activity start time across the 6 trip events reviewed.

## 5. Root Cause

**Tank vapor composition varied significantly depending on which tank was actively receiving product**, periodically sending the VRU compressor a vapor stream much lighter or heavier than its control logic's design assumption. This pushed the compressor outside its stable operating envelope during those periods, triggering high discharge temperature or low suction pressure trips — independent of overall throughput rate or tank level.

## 6. Corrective Action

1. **Widened/adjusted compressor control setpoints** to accommodate the actual range of vapor compositions the unit sees in practice, rather than a single design-case composition.
2. **Added vapor composition monitoring** correlated to which tank/service is active, to support both operations and future control tuning.

## 7. Verification

- Low-suction trip setpoint widened from 1.5 psig to **0.8 psig**; high-discharge-temperature trip widened from 300°F to **325°F**, both re-verified against API 618/machine mechanical limits before implementation.
- Trip frequency dropped from **3–4 events/week to zero over the following 60 days**, spanning multiple condensate and crude tank receiving cycles.

## 7a. Note on Comparison to Case Study 19

This case and the anti-surge case (Case Study 19) both involve a control system trip line calculated for one gas composition failing to track a different, actual composition — but the fixes point opposite directions operationally: in the anti-surge case the *true* stability boundary had moved further from normal operation than the old line assumed (undetected risk), while here the compressor's normal, safe operation was being falsely flagged as unsafe by trip setpoints that hadn't been evaluated against the full range of compositions the unit actually sees (nuisance trips). Confirming which situation applies — via the same "recalculate against actual current composition" step — determines whether the fix is tightening a margin or widening one.

## 8. Prevention / Long-Term Fix

- Established **vapor composition sampling correlated to tank service**, so composition swings are visible and can inform operations planning, not just discovered after a trip.
- Reviewed compressor control logic against the **full expected range of tank vapor compositions**, not a single nominal design case.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review trip timing against throughput rate and tank level first, to rule out the most obvious correlations
- [ ] If no clear pattern emerges, cross-reference trip timing against **which specific tank/service was active** at the time
- [ ] Sample and analyze vapor composition during a trip-correlated period to confirm a compositional swing
- [ ] Check compressibility/dew point behavior of the swung composition against the compressor's control envelope
- [ ] If confirmed, adjust control setpoints to accommodate the actual composition range, not just the original design case
- [ ] Add composition monitoring correlated to tank service to support ongoing operational awareness
- [ ] Recognize that shared/multi-source vapor recovery systems inherit the compositional variability of everything feeding them — a single design-case control tuning may not cover all real operating scenarios

## 10. Key Takeaway

> A vapor recovery compressor's feed isn't one consistent stream — it's whatever composition happens to be coming off whichever tank is active at the time. When trips don't correlate with throughput or level, check what's actually being loaded/received on the tank farm; a compressor tuned for a single "typical" vapor composition can trip reliably every time a much lighter or heavier product is handled, even though nothing is mechanically wrong with the machine itself.

---

## Related Concepts / Tags

`vapor-recovery-unit` `VRU` `compressor-trip` `tank-vapor-composition` `storage-tank` `Peng-Robinson` `compressibility` `control-setpoint` `variable-feed-composition`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
