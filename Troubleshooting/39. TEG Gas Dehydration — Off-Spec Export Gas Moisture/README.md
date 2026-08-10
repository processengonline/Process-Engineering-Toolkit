# Troubleshooting Guide: TEG Gas Dehydration — Off-Spec Export Gas Moisture

> **Category:** Gas Processing / Glycol Dehydration
> **Unit:** TEG (Triethylene Glycol) Dehydration — Absorber/Contactor
> **Tools:** Aspen HYSYS / UniSim (steady-state absorber model, DCS data reconciliation)
> **Fluid Package:** Glycol Package (Twu-Sim-Tassone / TEG-specific)
> **Symptom:** Export gas moisture out of spec despite healthy glycol quality

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Export gas moisture rose from 4 → 10 lb/MMscf (spec: ≤ 7 lb/MMscf) |
| Initially suspected cause | Poor lean glycol quality |
| Actual root cause | Tight gas–glycol temperature approach (2°C vs. 3°C minimum) caused by a drifted lean glycol cooler control valve, leading to hydrocarbon condensation on the packing |
| Fix | Recalibrate lean glycol cooler control valve to restore 3–5°C approach above gas temperature |
| Time to resolve (typical) | Diagnosis: simulation + approach-temperature calc; Fix: valve recalibration |
| Prevention | Add temperature-approach monitoring to SOPs — don't rely on glycol concentration alone |

---

## 2. Symptom

- Export gas moisture content increased from **4 lb/MMscf** to **10 lb/MMscf**.
- This breached the **contractual specification of 7 lb/MMscf**.
- No alarms or faults were present on the regeneration system.
- Lean glycol concentration was healthy at **99.6 wt%** — normally the first thing operators check, and normally a good indicator of dehydration health.

## 3. Why the Obvious Causes Didn't Explain It

Before escalating, the following standard checks were performed and all came back **within design**:

- [x] Lean glycol concentration (99.6 wt% — healthy)
- [x] Lean glycol circulation rate
- [x] Reboiler temperature
- [x] Flash tank pressure
- [x] Regeneration system fault status

**Conclusion at this stage:** none of the usual suspects explained the moisture excursion. This ruled out glycol *quality* as the driver and pointed toward something in the *contacting/mass-transfer* side of the process — an unmeasured or overlooked variable.

## 4. Diagnostic Approach

### Step 1 — Build a reconciled process model
A steady-state absorber model was built in **Aspen HYSYS/UniSim**, using actual DCS operating data as inputs, with the **Glycol fluid package** (Twu-Sim-Tassone / TEG-specific).

> **Why the fluid package choice matters:** Generic equations of state such as **Peng-Robinson or SRK do not handle glycol–water non-ideality well**. For TEG dehydration systems, a purpose-built glycol package gives substantially better VLE accuracy for the glycol–water–hydrocarbon system and should be the default choice for this unit type — using a generic EOS here can itself produce misleading simulation results.

### Step 2 — Compare simulated vs. actual performance
The simulation, run on actual plant conditions, **predicted better moisture removal than the plant was actually achieving**.

**Interpretation:** When a properly reconciled model outperforms the real unit under the same nominal conditions, it's a strong signal that an unmeasured, unmodeled, or overlooked physical effect is degrading real-world performance — not a parameter that's simply been mis-set.

### Step 3 — Check the gas–glycol temperature approach
This is the variable that isn't on most operator checklists but is critical to absorber performance:

```
Inlet gas temperature:       38°C
Lean glycol temperature:     40°C
Approach (glycol - gas):     2°C
Recommended minimum approach: 3°C
```

A 2°C approach — below the recommended minimum of 3°C — meant the lean glycol was not sufficiently warmer than the gas.

### Step 4 — Identify the physical consequence
A tight temperature approach at the absorber inlet allows **heavier hydrocarbon components to condense** as the gas contacts glycol close to its own temperature. This condensed hydrocarbon liquid **coats the glycol film on the structured/random packing**, which:

- Reduces glycol-to-gas contact area
- Impairs mass transfer of water into the glycol
- Produces exactly the symptom seen: healthy glycol chemistry, but poor actual dehydration

### Quantitative Basis

- Export gas moisture: baseline 4 lb/MMscf, rose to 10 lb/MMscf against a 7 lb/MMscf contractual spec.
- HYSYS/UniSim absorber model, run at the design 3°C gas-glycol approach with actual lean TEG rate and reboiler temperature, predicted 3.8 lb/MMscf — closely matching the historical baseline and confirming the model was properly reconciled before the approach-temperature deviation was investigated.
- Measured approach at the time of the excursion: inlet gas 38°C, lean glycol 40°C — **only 2°C, against a recommended minimum of 3°C.**

## 5. Root Cause

A **drifted lean glycol cooler control valve** was allowing lean glycol to enter the absorber warmer than intended, collapsing the gas–glycol temperature approach from the recommended 3–5°C down to 2°C.

## 6. Corrective Action

1. Recalibrated the lean glycol cooler control valve.
2. Restored the gas–glycol approach temperature to the recommended **3–5°C above gas temperature**.
3. Verified export gas moisture returned to spec (≤ 7 lb/MMscf).

## 7. Verification

- Post-recalibration, approach restored to 4°C (inlet gas 38°C, lean glycol 42°C).
- Export gas moisture measured at 3.6 lb/MMscf within 24 hours of the valve recalibration.
- Moisture content held in the 3.4-4.1 lb/MMscf range over the following 30 days of monitoring.

## 8. Prevention / Long-Term Fix

- **Added temperature-approach monitoring to standard operating procedures (SOPs).**
- Glycol concentration alone is **no longer treated as the sole health indicator** for the dehydration unit — approach temperature is now tracked alongside it.

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for future TEG dehydration off-spec moisture events:

- [ ] Confirm lean glycol concentration (wt%) is within spec
- [ ] Confirm lean glycol circulation rate
- [ ] Confirm reboiler temperature
- [ ] Confirm flash tank pressure
- [ ] Confirm no regeneration system faults/alarms
- [ ] **Calculate gas–glycol temperature approach at absorber inlet** (target: ≥ 3°C, ideally 3–5°C)
- [ ] Check lean glycol cooler performance / control valve position vs. commanded position
- [ ] If all "standard" parameters check out, build/update a reconciled simulation model using actual DCS data and compare predicted vs. actual moisture removal
- [ ] If simulation outperforms actual plant, suspect an unmodeled physical effect (e.g., hydrocarbon condensation, packing fouling, liquid maldistribution) rather than a setpoint error

## 10. Key Takeaway

> Glycol concentration tells you about **regeneration** performance. Temperature approach tells you about **absorption** performance. A unit can pass every regeneration-side check and still fail on moisture spec if the absorption-side thermal conditions are wrong. When the "obvious" parameters are all in spec, check the ones that aren't on the standard checklist — starting with temperature approach.

---

## Related Concepts / Tags

`glycol-dehydration` `TEG` `moisture-spec` `absorber` `temperature-approach` `hydrocarbon-condensation` `packing-fouling` `HYSYS` `UniSim` `glycol-fluid-package` `control-valve-drift` `gas-processing`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
