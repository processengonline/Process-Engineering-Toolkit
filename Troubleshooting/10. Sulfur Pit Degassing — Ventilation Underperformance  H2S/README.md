# Troubleshooting Guide: Sulfur Pit Degassing — Ventilation Underperformance and Rising H2S Levels

> **Category:** Safety Systems / Sulfur Handling
> **Unit:** Liquid Sulfur Pit/Storage, Degassing Ventilation System
> **Tools:** Ventilation airflow trending (anemometer-verified, not just motor amps), off-gas rate estimate from sulfur production and dissolved H2S content
> **Fluid Package:** Not applicable — this is an airflow/ventilation capacity balance problem, not a phase-equilibrium calculation
> **Symptom:** Rising H2S concentration readings at the pit vent and ambient monitors, approaching the site action level

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | H2S concentration at the sulfur pit vent/ambient monitors trending up toward the action level |
| Initially unclear | Whether this was a change in sulfur production rate/dissolved H2S content, or a ventilation system underperforming despite appearing to run normally |
| Actual root cause | The degassing ventilation blower's drive belt had worn and was slipping, reducing actual air delivery well below the rate needed to dilute H2S off-gas, even though the blower motor itself was still drawing normal current |
| Fix | Replaced the worn/slipping belt; verified restored airflow via direct anemometer measurement |
| Diagnostic signal | Motor amperage looked completely normal (masking the fault), but direct airflow measurement showed a significant shortfall from rated capacity |
| Prevention | Periodic direct airflow verification via anemometer (not just motor current) added to the PM program; belt condition inspection tied to the airflow trend |

---

## 2. Symptom

- **H2S concentration readings at the sulfur pit vent and ambient monitors trended upward**, approaching the site's action level — a safety-significant trend requiring prompt investigation.

## 3. Why This Wasn't Assumed to Be a Production-Rate Issue

Rising H2S readings from a sulfur pit are most directly explained by an increase in dissolved H2S content in the incoming liquid sulfur (e.g., from an upstream Claus/degassing process change) or an increase in sulfur throughput — both process-side explanations. But the degassing **ventilation system's** job is specifically to dilute and remove H2S off-gas to keep concentrations below the action level; if that system's actual performance had degraded, the same rising-H2S symptom would appear even with unchanged sulfur production. Both possibilities needed to be checked.

## 4. Diagnostic Approach

### Step 1 — Review sulfur production rate and upstream dissolved H2S content
Sulfur throughput and the upstream Claus/degassing process's dissolved H2S content in the liquid sulfur feed to the pit were reviewed and found essentially unchanged — ruling out a process-side driver for the rising readings.

### Step 2 — Check the ventilation blower's operating status
The degassing ventilation blower's control system status and **motor amperage** were checked and found **normal** — the motor was running and drawing its expected current, giving no indication of a problem from the control room.

### Step 3 — Directly measure actual airflow delivery
Rather than relying on motor amperage as a proxy for airflow (a proxy that only confirms the motor is running, not that it's actually moving the rated volume of air), a **direct anemometer measurement** was taken at the ventilation discharge.

**Finding:** Actual airflow was **significantly below the blower's rated capacity**, despite the motor drawing normal current — a clear "commanded vs. delivered" mismatch, conceptually similar to the distillation column thyristor case (Case Study 4), but here on a mechanical belt-drive rather than an electrical heater.

### Step 4 — Identify the mechanical cause
With a real airflow shortfall confirmed independent of motor status, the blower's **belt drive** was inspected directly.

**Finding:** The drive belt was **worn and slipping**, transmitting less power to the fan than the motor was producing — explaining why the motor could draw normal current while the fan itself moved far less air.

### Quantitative Basis

- Ventilation blower rated airflow: 4,200 CFM. Direct anemometer measurement during the investigation: **2,650 CFM — a 37% shortfall**, despite motor amperage reading within 2% of its normal baseline value throughout.
- H2S concentration at the pit vent monitor: baseline 4-6 ppm, rose to **18 ppm** against a site action level of 20 ppm.
- Estimated H2S off-gas generation rate (from sulfur throughput and dissolved H2S content, essentially unchanged): consistent with the baseline design case — confirming the ventilation shortfall, not a production change, as the driver.

## 5. Root Cause

**The degassing ventilation blower's drive belt had worn and was slipping**, reducing actual air delivery to well below the rate needed to adequately dilute H2S off-gas from the sulfur pit — even though the blower motor itself continued to run and draw normal current, giving no indication of the underlying mechanical shortfall from standard control-room monitoring alone.

## 6. Corrective Action

1. **Replaced the worn/slipping drive belt.**
2. **Verified restored airflow via direct anemometer measurement** rather than relying on motor amperage alone.

## 7. Verification

- Post-repair anemometer measurement confirmed airflow at **4,150 CFM — 99% of the 4,200 CFM rated capacity.**
- H2S concentration at the pit vent monitor returned to **5 ppm**, within the normal 4-6 ppm baseline range, well below the 20 ppm action level.
- Held stable over the following **30 days** of continued monitoring.

## 8. Prevention / Long-Term Fix

- Added **periodic direct airflow verification via anemometer** to the PM program, specifically because motor amperage alone had proven insufficient to detect this failure mode.
- **Belt condition inspection is now tied to the airflow trend** (triggered by any deviation, not just a fixed calendar interval), since belt wear can progress without producing any electrical-side symptom.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review process-side factors (production rate, upstream dissolved H2S content) first to rule in/out a genuine process change
- [ ] Check ventilation/blower control status and motor amperage, but recognize that normal motor current does NOT confirm normal air delivery
- [ ] Take a direct airflow measurement (anemometer) at the ventilation discharge to verify actual delivered performance against rated capacity
- [ ] If a shortfall is confirmed despite normal motor amperage, inspect the mechanical power transmission path (belts, couplings, fan blade condition) rather than the motor/electrical side
- [ ] Repair the mechanical fault and re-verify with a direct airflow measurement, not just a return-to-normal motor amperage reading
- [ ] Confirm H2S/ambient monitoring readings return to baseline and hold stable over an extended monitoring period
- [ ] Add direct airflow verification (not just motor current) to the standing PM program for any ventilation system protecting against a toxic gas exposure risk

## 10. Key Takeaway

> Motor amperage tells you the motor is running — it does not tell you the fan is actually moving its rated volume of air. A slipping belt, damaged fan blade, or other mechanical power-transmission fault can leave a ventilation system silently underperforming for a safety-critical duty while every electrical indicator looks completely normal. For any ventilation system protecting against a toxic gas hazard, periodic direct airflow measurement is not optional — it's the only way to actually confirm delivered performance, not just commanded performance.

---

## Related Concepts / Tags

`sulfur-pit` `degassing` `H2S` `ventilation-system` `blower-belt` `airflow-verification` `anemometer` `safety-critical-ventilation` `toxic-gas-exposure`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
