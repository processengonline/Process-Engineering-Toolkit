# Troubleshooting Guide: Amine Circulation Pump — Cavitation from Foam Ingestion

> **Category:** Rotating Equipment / Gas Treating / Pump Hydraulics
> **Unit:** Lean Amine Circulation Pump, Downstream of Flash Tank
> **Tools:** NPSHa hydraulic calculation, flash tank foam/froth height assessment, foam tendency testing
> **Fluid Package:** Amine/Acid Gas package for vapor pressure (as in the absorber foaming case, Case Study 9), combined with standard NPSH hydraulics
> **Symptom:** Pump cavitation noise/vibration despite a standard NPSH calculation using bulk liquid level showing adequate margin

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Pump cavitation noise and vibration, despite NPSHa (calculated from bulk liquid level) showing adequate margin over NPSHr |
| Initially unclear | Whether the standard NPSH calculation itself was wrong, or a different mechanism entirely was reducing the effective NPSH the pump actually experienced |
| Actual root cause | Amine foaming in the upstream flash tank raised the froth/foam layer height above the pump suction nozzle, causing the pump to draw a two-phase foam mixture rather than clear liquid, effectively starving it of usable NPSH regardless of the bulk liquid level |
| Fix | Addressed amine foaming (antifoam, filtration) to reduce foam tendency; adjusted flash tank level control to keep froth height below the suction nozzle |
| Diagnostic signal | Standard NPSHa calculation using bulk liquid level and temperature showed adequate margin, which didn't match the observed cavitation — prompting investigation of what the pump was actually drawing in, not just what the level instrument reported |
| Prevention | Foam-tendency testing tied into the pump reliability program specifically, not treated only as an absorber/stripper concern |

---

## 2. Symptom

- **Pump cavitation noise and vibration**, the classic hydraulic signature seen in the earlier centrifugal pump NPSH case — but here, a standard **NPSHa calculation using bulk liquid level showed adequate margin** over the pump's NPSHr, which didn't match the observed symptoms.

## 3. Why This Wasn't Explained by the Standard NPSH Calculation

Normally, cavitation with a healthy NPSHa margin (by calculation) would prompt re-checking the calculation inputs for an error. But here, the calculation itself — bulk liquid level, temperature, vapor pressure — was confirmed correct and consistent with what the level instrument reported. This meant the discrepancy wasn't in the *calculation*; it was in the **assumption that the pump suction was drawing clear liquid at all**, which is the implicit basis of any bulk-level NPSH calculation.

## 4. Diagnostic Approach

### Step 1 — Re-verify the standard NPSHa calculation
Suction vessel (flash tank) bulk liquid level, line losses, and fluid vapor pressure (via the amine package) were re-checked and confirmed consistent with the level instrument and process conditions — the calculation itself was not wrong given its inputs.

### Step 2 — Question the calculation's underlying assumption
A standard NPSHa calculation assumes the pump suction draws **clear liquid** from below the liquid surface. This assumption was reconsidered given the persistent, unexplained cavitation.

### Step 3 — Assess the flash tank for foaming/froth
The flash tank — a vessel upstream of a pump handling amine, a fluid class with a well-documented foaming tendency (as established in the absorber foaming case, Case Study 9) — was inspected for foam/froth conditions, and its **froth height relative to the pump suction nozzle elevation** was assessed.

**Finding:** The flash tank was carrying a **substantial froth/foam layer**, and the froth height was **above the pump suction nozzle centerline** — meaning the pump was drawing from within the foam layer, not from clear liquid below it, regardless of what the bulk liquid level instrument (which measures overall level, not distinguishing froth from clear liquid) reported.

### Step 4 — Confirm the amine's foam tendency directly
A foam tendency test was run on the amine sample, confirming an elevated foam tendency consistent with contamination — the same class of mechanism (contamination-driven foaming) identified in the absorber case, but here manifesting downstream at the pump suction rather than as absorber dP/H2S slip.

### Quantitative Basis

- Standard NPSHa (bulk level basis): calculated at **16.8 ft**, against a pump NPSHr of **11.5 ft** — a nominally healthy 5.3 ft margin.
- Flash tank froth height, measured via a differential level check (comparing a density-compensated level reading against a simple hydrostatic level reading — the gap between the two indicates froth), was estimated at **22 in above the pump suction nozzle centerline.**
- Foam tendency test: foam persisted **41 seconds** after air sparge stopped, against a <10 second pass/fail criterion — consistent with the contamination-driven foaming mechanism.

## 5. Root Cause

**Amine foaming in the flash tank raised the froth/foam layer above the pump suction nozzle elevation**, causing the pump to ingest a two-phase (vapor-entrained) mixture rather than clear liquid. This effectively starved the pump of usable NPSH regardless of what the bulk liquid level instrument and a standard clear-liquid NPSHa calculation indicated, since that calculation's foundational assumption — clear liquid at the suction — was not actually being met.

## 6. Corrective Action

1. **Addressed the amine contamination** driving the foam tendency (antifoam dosing, filtration), the same class of fix used in the absorber foaming case.
2. **Adjusted flash tank level control** to maintain a lower operating level, keeping the froth layer's top surface below the pump suction nozzle elevation with margin.

## 7. Verification

- Foam tendency test on the treated amine measured **9 seconds**, within the <10 second pass criterion.
- Froth height, re-assessed via the differential level check, dropped to an estimated **4 in above the (now-lower) liquid level** — comfortably below the suction nozzle elevation under the adjusted level control setpoint.
- Pump cavitation noise and vibration stopped, confirmed via vibration monitoring showing levels return to **baseline (0.09 in/s)** and held there over the following **30 days.**

## 8. Prevention / Long-Term Fix

- **Foam-tendency testing has been added to the pump reliability program specifically**, not treated as only an absorber/stripper concern, since foam anywhere in the amine circuit can starve downstream equipment of usable NPSH even when a standard bulk-level calculation looks fine.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Re-verify the standard NPSHa calculation inputs (level, temperature, vapor pressure) before assuming the calculation itself is flawed
- [ ] If cavitation persists despite a calculated healthy margin, question whether the pump suction is actually drawing clear liquid
- [ ] For foam-prone fluids (amine, and similar), assess the upstream vessel for froth/foam layer height relative to the suction nozzle elevation
- [ ] Use a differential level technique (density-compensated vs. simple hydrostatic level) to estimate froth height where a direct visual check isn't possible
- [ ] Run a foam tendency test on the fluid to confirm/quantify the foaming mechanism
- [ ] Address the foam-causing contamination (the same fix category as absorber/stripper foaming cases) rather than only adjusting level control
- [ ] Adjust vessel level control to keep froth height below the suction nozzle with margin as a complementary, not standalone, fix
- [ ] Extend foam-tendency testing to any pump reliability program handling a foam-prone fluid, not just the absorption/stripping equipment it's traditionally associated with

## 10. Key Takeaway

> A healthy NPSHa margin by calculation doesn't guarantee a pump is actually receiving clear liquid — that calculation implicitly assumes it is. For foam-prone fluids like amine, check whether a froth layer upstream has risen above the suction nozzle elevation before concluding the NPSH calculation itself must be wrong; foaming can starve a pump of usable NPSH completely independent of what the bulk liquid level instrument reports.

---

## Related Concepts / Tags

`amine-pump` `cavitation` `NPSH` `foam-ingestion` `flash-tank` `froth-height` `foam-tendency-test` `amine-foaming` `gas-treating` `pump-hydraulics`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
