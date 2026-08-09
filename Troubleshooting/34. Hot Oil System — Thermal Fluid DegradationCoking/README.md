# Troubleshooting Guide: Hot Oil (Heat Medium) System — Thermal Fluid Degradation and Coking

> **Category:** Utilities / Heat Transfer Fluid Systems
> **Unit:** Hot Oil (Thermal Fluid) Circulation System, Indirect Process Heating
> **Tools:** Thermal fluid lab analysis (viscosity, acid number, flash point, carbon residue) trending; heater tube skin temperature review
> **Fluid Package:** Not applicable in the VLE sense — thermal fluid degradation is assessed via lab analysis against the fluid manufacturer's condition-monitoring guidelines, not a phase-equilibrium calculation
> **Symptom:** Process-side heat exchangers served by the hot oil loop gradually receiving less heat despite stable hot oil circulation rate and heater outlet temperature

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Process-side exchangers on the hot oil loop gradually receiving less heat despite stable circulation rate and heater outlet temperature |
| Initially unclear | Whether this was fouling on individual process-side exchangers (a per-exchanger issue) or a system-wide thermal fluid quality issue |
| Actual root cause | The thermal fluid itself had degraded (oxidation and localized overheating at the fired heater had produced coking/carbon buildup circulating in the fluid and depositing inside heater tubes and exchanger tubes), reducing the fluid's effective heat transfer capability system-wide |
| Fix | Drained and replaced/reconditioned the degraded thermal fluid; mechanically cleaned heater tubes and affected exchangers; corrected the heater firing pattern that had caused localized overheating |
| Diagnostic signal | The performance decline affected multiple exchangers across the loop simultaneously (system-wide), and lab analysis of the circulating fluid showed degraded properties (elevated carbon residue, changed viscosity/acid number) consistent with thermal degradation, not fresh-fluid behavior |
| Prevention | Routine thermal fluid lab sampling on a fixed schedule; heater tube skin temperature monitoring to catch localized overheating before it degrades the fluid inventory |

---

## 2. Symptom

- **Multiple process-side heat exchangers served by the hot oil loop gradually received less heat** — process outlet temperatures on several unrelated services trended down together.
- **Hot oil circulation rate and heater outlet temperature both remained stable** at their normal setpoints.

## 3. Why This Wasn't Treated as Several Separate Exchanger Fouling Problems

Multiple exchangers losing performance at the same time, served by a shared hot oil loop, is analogous to the instrument air case (Case Study 26): when several otherwise-unrelated pieces of equipment degrade together, a **shared system** is a more likely explanation than several coincidental, independent fouling events. Here, the shared system was the thermal fluid itself — if the fluid's heat transfer properties had degraded, every exchanger on the loop would be affected simultaneously, regardless of that exchanger's individual service or fouling history.

## 4. Diagnostic Approach

### Step 1 — Confirm the performance decline is system-wide, not exchanger-specific
Performance trends were reviewed across multiple exchangers on the loop and confirmed to be declining **together**, rather than one specific exchanger degrading in isolation — pointing toward a shared cause rather than independent per-exchanger fouling.

### Step 2 — Confirm hot oil circulation and heater outlet temperature are stable
Circulation rate and heater outlet temperature were confirmed at normal setpoints — ruling out an obvious operational cause like reduced flow or reduced heater duty.

### Step 3 — Sample and lab-analyze the circulating thermal fluid
A sample of the circulating hot oil was sent for lab analysis of standard thermal fluid condition indicators: **viscosity, acid number, flash point, and carbon residue**, compared against the fluid manufacturer's condition-monitoring guidelines and the fluid's baseline (fresh) properties.

**Finding:** Results showed **elevated carbon residue and shifted viscosity/acid number**, consistent with **thermal degradation** — the fluid itself had broken down chemically, rather than remaining in its original, effective condition.

### Step 4 — Identify the degradation trigger
With fluid degradation confirmed, the investigation turned to *why*. Reviewing fired heater operating history identified periods of **localized overheating** (a firing pattern issue, similar in principle to the flame impingement case, Case Study 11, but here affecting the circulating fluid rather than a process gas stream) that would drive **localized fluid temperatures above the fluid's recommended film temperature limit**, promoting oxidation/coking at the tube surface.

### Quantitative Basis

- **4 exchangers on the loop** showed process outlet temperatures **8–14°F below setpoint simultaneously** — a system-wide pattern, not one exchanger degrading in isolation.
- Fresh-fluid baseline: viscosity 32 cSt @ 40°C, acid number 0.05 mg KOH/g, flash point 240°C, Conradson carbon residue 0.1 wt%. Circulating sample: viscosity **24 cSt** (light, cracked fragments lowering bulk viscosity), acid number **0.65 mg KOH/g**, flash point **195°C**, carbon residue **2.8 wt%** — all well outside the manufacturer's acceptable range.
- Fluid's rated maximum film temperature is 343°C (650°F). Heater tube skin thermocouples, reviewed against firing history, showed localized readings reaching **365–380°C** during periods of burner-biased firing — 22–37°C above the fluid's limit.

## 5. Root Cause

**Localized overheating at the fired heater (from a firing pattern issue) drove the thermal fluid's film temperature at the tube surface above its safe operating limit in certain areas, causing oxidation and coking.** This degraded the fluid's heat transfer properties system-wide and generated carbon/coke particulate that circulated through the loop and deposited inside heater tubes and process-side exchanger tubes — reducing heat transfer performance across multiple, otherwise unrelated exchangers simultaneously.

## 6. Corrective Action

1. **Drained and replaced/reconditioned the degraded thermal fluid.**
2. **Mechanically cleaned heater tubes and the affected process-side exchangers** to remove deposited coke/carbon.
3. **Corrected the heater firing pattern** that had caused the localized overheating driving fluid degradation in the first place.

## 7. Verification

- Follow-up lab analysis of the fresh/reconditioned fluid measured **31 cSt viscosity, 0.06 mg KOH/g acid number, 238°C flash point, 0.15 wt% carbon residue** — all within acceptable range of the fresh-fluid baseline.
- Process outlet temperatures recovered to **within 2°F of setpoint across all 4 previously affected exchangers.**
- Following the firing pattern correction, subsequent tube skin monitoring has held **below 345°C**, within the fluid's rated film temperature limit.

## 8. Prevention / Long-Term Fix

- Established **routine thermal fluid lab sampling on a fixed schedule**, rather than only sampling reactively once performance issues appear.
- Added **heater tube skin temperature monitoring**, to catch localized overheating (the actual trigger mechanism) before it has time to meaningfully degrade the entire fluid inventory.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm whether a performance decline is affecting a single exchanger or **multiple exchangers on the same shared system** simultaneously
- [ ] If multiple/unrelated exchangers are affected together, suspect a shared system (fluid quality, utility supply) rather than independent per-exchanger fouling
- [ ] Confirm circulation rate and heater outlet temperature are stable to rule out an obvious operational cause
- [ ] Sample and lab-analyze the circulating thermal fluid against manufacturer condition-monitoring guidelines (viscosity, acid number, flash point, carbon residue)
- [ ] If degradation is confirmed, investigate the fired heater for localized overheating (firing pattern, burner condition) as the likely trigger mechanism
- [ ] Replace/recondition the fluid and mechanically clean both the heater and affected exchangers, since coke/carbon deposits won't clear simply by replacing the fluid alone
- [ ] Correct the underlying overheating cause to prevent re-degradation of the new/reconditioned fluid
- [ ] Establish routine thermal fluid sampling and heater tube skin temperature monitoring as standing checks

## 10. Key Takeaway

> When multiple, otherwise-unrelated exchangers on a shared heat transfer loop lose performance together, look at what they share — the circulating fluid itself — before investigating each exchanger individually. Thermal fluid degradation is often triggered by localized overheating at the fired heater, well upstream of where the symptom (reduced exchanger performance) eventually shows up, so fixing the fluid without correcting the heater firing pattern that degraded it just sets up a repeat failure.

---

## Related Concepts / Tags

`hot-oil-system` `thermal-fluid` `heat-medium` `fluid-degradation` `coking` `carbon-residue` `fired-heater` `film-temperature` `shared-utility-failure`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
