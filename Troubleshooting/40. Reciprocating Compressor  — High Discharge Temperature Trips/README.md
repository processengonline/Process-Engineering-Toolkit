# Troubleshooting Guide: Reciprocating Compressor — High Discharge Temperature Trips

> **Category:** Rotating/Reciprocating Equipment / Gas Compression
> **Unit:** Reciprocating Gas Compressor (single/multi-stage, gas transmission/export service)
> **Tools:** UniSim compressor performance model (thermodynamic staging)
> **Fluid Package:** Peng-Robinson (PR)
> **Symptom:** Repeated high discharge temperature trips despite normal cooling, lube oil, and loading conditions

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Repeated compressor trips on high discharge temperature; production interruptions |
| Initially suspected causes | Cooling water flow, lube oil temperature, intercooler performance, loading |
| Actual root cause | Deteriorated piston O-ring causing internal gas leakage (discharge → suction), forcing extra recompression work and excess heat generation |
| Fix | Replace piston O-ring; verify efficiency via performance testing |
| Diagnostic signal | Simulated discharge temp (145°C) vs. actual (175°C+) — a 30°C+ gap pointed away from process causes |
| Prevention | Updated preventive maintenance intervals for seal inspection |

---

## 2. Symptom

- Reciprocating gas compressor **tripping repeatedly on high discharge temperature**.
- Trips were causing **production interruptions**.
- No alarms or abnormal readings elsewhere in the cooling/lubrication systems.

## 3. Why the Obvious Causes Didn't Explain It

Before escalating, the following standard checks were performed and all came back **within design/normal**:

- [x] Cooling water flow
- [x] Lube oil temperature
- [x] Intercooler performance
- [x] Compressor loading

**Conclusion at this stage:** every parameter typically associated with discharge temperature excursions was normal. This ruled out cooling-side and loading-side causes and raised the question of whether the problem was **process-related or mechanical** — a distinction that determines whether the fix is an operating adjustment or a maintenance action.

## 4. Diagnostic Approach

### Step 1 — Build a performance model
A compressor performance model was developed in **UniSim**, based on:
- Suction and discharge pressure
- Gas composition
- Design (polytropic) efficiency

> **Why Peng-Robinson here:** PR is the standard EOS choice for **light-to-medium hydrocarbon gas compression**, giving reliable density and enthalpy predictions across the suction/discharge pressure range needed for **polytropic head and discharge temperature calculations**. Unlike glycol/water systems (see TEG dehydration case study), compression duty on hydrocarbon gas is exactly the regime PR was built for — no specialty package needed here.

### Step 2 — Compare simulated vs. actual performance

```
Simulated discharge temperature (design efficiency):   145°C
Actual plant discharge temperature:                    175°C+
Gap:                                                    30°C+
```

**Interpretation:** A properly built model running on actual suction/discharge conditions and gas composition should track real plant performance reasonably closely if the compressor is operating as designed. A **30°C+ gap** between predicted and actual discharge temperature is far outside normal model uncertainty and indicates the **machine itself is not performing at its design efficiency** — this is the compression equivalent of the "simulation outperforms plant" signal used in the TEG dehydration case, and it points the same way: toward an unmodeled physical degradation rather than a process setpoint issue.

### Step 3 — Sensitivity analysis
Running sensitivity analysis on the performance model against the observed temperature gap pointed to **reduced volumetric efficiency** as the most likely explanation.

**Why this matters operationally:** Volumetric efficiency loss is a classic signature of **internal mechanical leakage** (valves, rings, packing) rather than anything adjustable from the control room. This is the point where the investigation shifted from process troubleshooting to requesting a mechanical inspection.

### Step 4 — Request a mechanical leak test
Based on the volumetric efficiency finding, a mechanical leak test was requested rather than continuing to chase process variables that had already been ruled out.

### Quantitative Basis

- UniSim-simulated discharge temperature at actual suction/discharge pressure (185/720 psig) and design volumetric efficiency (91%): **145°C.** Actual measured discharge temperature: **175°C+.**
- Sensitivity analysis: matching the observed 175°C+ discharge temperature required a volumetric efficiency of **74% — a 17-point drop** from the 91% design value.
- Post-repair inspection of the piston O-ring found wear consistent with an estimated **8-10% internal recirculation** (discharge-to-suction leakage) flow.

## 5. Root Cause

A **deteriorated piston O-ring** was allowing **internal gas leakage from the discharge side back to the suction side**. This meant the compressor was:
- Recompressing gas that had already been compressed (extra work per unit of net throughput)
- Generating excess heat as a direct result of this recirculating/re-compression load
- Showing degraded volumetric efficiency in the performance model even though suction/discharge pressures and loading looked normal externally

## 6. Corrective Action

1. Replaced the deteriorated piston O-ring.
2. Verified restored efficiency through **performance testing** (comparing post-repair actual discharge temperature against the UniSim model prediction).
3. Confirmed discharge temperature returned in line with expected values and trips stopped.

## 7. Verification

- Post-repair discharge temperature measured at **148°C**, within normal tolerance of the 145°C model prediction (91% design volumetric efficiency).
- Follow-up performance test measured volumetric efficiency at **89-90%**, close to the 91% design value, confirming the leak path was closed rather than just masked.
- No further high-discharge-temperature trips observed over the following **60 days.**

## 8. Prevention / Long-Term Fix

- **Updated preventive maintenance intervals for seal/O-ring inspection** to catch this class of degradation earlier, before it manifests as a trip-causing temperature excursion.

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for future reciprocating compressor high-discharge-temperature events:

- [ ] Confirm cooling water flow to intercoolers/aftercoolers
- [ ] Confirm lube oil temperature and flow
- [ ] Confirm intercooler performance (approach temperature, fouling)
- [ ] Confirm compressor loading/staging is as expected
- [ ] **Build or update a performance model** using actual suction/discharge pressure, gas composition, and design efficiency
- [ ] Compare **simulated vs. actual discharge temperature** — flag any gap significantly beyond normal model uncertainty
- [ ] If a gap exists, run **sensitivity analysis** to identify which efficiency parameter (volumetric, polytropic) best explains it
- [ ] Reduced volumetric efficiency with normal external conditions → **request a mechanical leak/inspection test** (valves, rings, packing) rather than continuing to adjust process variables
- [ ] After repair, confirm fix via **performance testing**, not just a single temperature reading
- [ ] Review/update PM intervals for the failed component class

## 10. Key Takeaway

> When cooling, lubrication, and loading all check out but discharge temperature stays high, don't keep tuning process variables — **let the performance model tell you where to look**. A large, sustained gap between predicted and actual discharge temperature is a mechanical-condition signal, not a process-tuning problem. Volumetric efficiency loss specifically points toward internal leakage (rings, valves, packing) and should trigger a mechanical inspection, not another round of process checks.

---

## Related Concepts / Tags

`reciprocating-compressor` `discharge-temperature` `volumetric-efficiency` `polytropic-efficiency` `internal-gas-leakage` `piston-o-ring` `UniSim` `Peng-Robinson` `performance-testing` `preventive-maintenance` `gas-compression`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
