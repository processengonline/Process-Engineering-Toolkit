# Troubleshooting Guide: Ammonia Refrigeration System — Oil Fouling Reducing Evaporator Capacity

> **Category:** Utilities / Industrial Refrigeration
> **Unit:** Ammonia Refrigeration Package, Flooded Evaporator
> **Tools:** Refrigerant-side heat transfer performance trending, compressor oil separator efficiency check, oil sample analysis
> **Fluid Package:** Not applicable in the VLE sense — ammonia refrigeration cycle performance uses standard refrigerant property tables, not a hydrocarbon cubic EOS
> **Symptom:** Process outlet temperature gradually rising, compressor amperage climbing, suction pressure trending down slightly, at unchanged load

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Process outlet temperature creeping up; compressor amps rising; suction pressure trending down slightly — all at unchanged process load |
| Initially unclear | Whether this was a refrigerant charge/leak issue, a compressor mechanical issue, or a heat transfer degradation inside the evaporator |
| Actual root cause | Compressor oil separator demister pad had degraded, allowing increased oil carryover into the evaporator, where it formed an insulating film on the tube surface and reduced heat transfer |
| Fix | Replaced oil separator demister pad; drained accumulated oil from the evaporator low point |
| Diagnostic signal | Refrigerant-side U calculated from actual data had dropped well below clean design value, while refrigerant charge and compressor mechanical checks came back normal |
| Prevention | Periodic oil level trending at the evaporator low point; scheduled oil separator efficiency testing |

---

## 2. Symptom

- **Process outlet temperature gradually rose** at unchanged process load — the evaporator wasn't removing as much heat as before.
- **Compressor amperage climbed** and **suction pressure trended down slightly**, both consistent with the compressor working harder to maintain the same duty.

## 3. Why This Wasn't Assumed to Be a Simple Charge or Compressor Issue

A slowly declining refrigeration performance is often first attributed to a **slow refrigerant leak** (reducing charge) or a **compressor mechanical issue** (reduced volumetric efficiency, similar in principle to the reciprocating compressor case). Both are common and both were worth ruling out before considering a heat-transfer-side cause, since a heat-transfer degradation points toward a completely different fix — cleaning the evaporator, not chasing a leak or overhauling the compressor.

## 4. Diagnostic Approach

### Step 1 — Confirm refrigerant charge
Refrigerant charge level was checked via standard system indicators (receiver level, sight glass) and found within normal range — ruling out a leak as the primary driver.

### Step 2 — Confirm compressor mechanical performance
Compressor discharge pressure, suction pressure, and amperage were reviewed against the compressor's performance curve for current conditions; the compressor itself was found to be operating consistently with its curve — not showing a mechanical efficiency loss of its own.

### Step 3 — Calculate actual evaporator heat transfer performance
With charge and compressor both ruled out, the evaporator's **actual overall heat transfer coefficient** was calculated from measured refrigerant and process-side temperatures and flows, and compared against the clean/design value — the same core technique used for the seawater cooler and crude preheat train cases.

**Finding:** Actual U had dropped **well below clean design**, confirming a heat-transfer-side degradation specifically at the evaporator.

### Step 4 — Investigate the fouling mechanism
With reduced U confirmed, the compressor's **oil separator** was inspected, since oil carryover into a flooded evaporator is a well-known cause of reduced heat transfer (oil forms an insulating film on the tube/shell surface, since oil has much lower thermal conductivity than ammonia liquid).

**Finding:** The oil separator's **demister pad had degraded**, reducing its oil removal efficiency and allowing more oil to carry over into the evaporator.

### Quantitative Basis

- Evaporator clean design U: 165 Btu/hr·ft²·°F. Trended actual U dropped to **98 Btu/hr·ft²·°F — a 41% loss.**
- Process outlet temperature rose from a design 20°F to **28°F** at unchanged load; compressor amperage rose from a baseline 145 A to **172 A.**
- Oil separator efficiency (rated to limit carryover to <5 ppm at the compressor discharge) was measured at the degraded demister pad passing **340 ppm** — a 68x exceedance.
- Oil drained from the evaporator low point measured **11 gallons**, versus a normal trace/negligible accumulation for a properly functioning oil separator.

## 5. Root Cause

**The compressor's oil separator demister pad had degraded, significantly increasing oil carryover into the evaporator.** The carried-over oil accumulated on the evaporator's heat transfer surface, forming an insulating film that reduced the effective overall heat transfer coefficient — reducing cooling capacity at unchanged process load and forcing the compressor to work harder (higher amps, lower suction pressure) to try to compensate.

## 6. Corrective Action

1. **Replaced the oil separator demister pad**, restoring its oil removal efficiency.
2. **Drained the accumulated oil from the evaporator low point.**

## 7. Verification

- Oil separator efficiency, re-tested post-repair, measured **3 ppm carryover**, within the <5 ppm design target.
- Evaporator U recovered to **158 Btu/hr·ft²·°F — 96% of clean design.**
- Process outlet temperature returned to **21°F**, and compressor amperage dropped to **148 A**, both close to baseline, and held stable over the following **30 days.**

## 8. Prevention / Long-Term Fix

- Established **periodic oil level trending at the evaporator low point**, so future oil accumulation is caught early rather than discovered only through a broader performance decline.
- Implemented **scheduled oil separator efficiency testing**, since a demister pad can degrade gradually without triggering any single obvious alarm.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm refrigerant charge level before assuming a heat-transfer-side cause
- [ ] Confirm compressor performance against its rated curve for current suction/discharge conditions
- [ ] If both check out normal, calculate actual evaporator U from measured data and compare to clean design U
- [ ] If U has dropped, inspect the compressor's oil separator (demister condition, measured carryover ppm)
- [ ] Drain and measure any accumulated oil at the evaporator low point as direct physical confirmation
- [ ] Replace/repair the oil separator and drain accumulated oil
- [ ] Confirm recovery via BOTH oil separator carryover test AND evaporator U, not just a general temperature improvement
- [ ] Establish routine oil level trending at evaporator low points and scheduled oil separator efficiency testing

## 10. Key Takeaway

> In flooded ammonia (or other oil-lubricated refrigerant) systems, a gradually declining evaporator performance with normal charge and normal compressor mechanicals should point straight at oil carryover — oil is an effective insulator on a heat transfer surface, and a degrading oil separator can quietly rob capacity long before any single alarm fires. Calculate actual U against clean design, and if it's degraded, check the oil separator before assuming a leak or a compressor problem.

---

## Related Concepts / Tags

`ammonia-refrigeration` `flooded-evaporator` `oil-carryover` `oil-separator` `demister-pad` `heat-transfer-coefficient` `industrial-refrigeration` `U-value-trending`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
