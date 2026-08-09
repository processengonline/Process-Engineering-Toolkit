# Troubleshooting Guide: Crude Preheat Train — Progressive Exchanger Fouling Reducing Furnace Inlet Temperature

> **Category:** Heat Transfer Equipment / Predictive Maintenance
> **Unit:** Crude Preheat Train (series of shell-and-tube exchangers upstream of the atmospheric heater)
> **Tools:** HTRI/EDR-based exchanger performance monitoring, network-level U-value trending
> **Fluid Package:** Not applicable in the VLE sense — HTRI/EDR use built-in crude/hydrocarbon property correlations for thermal-hydraulic rating, similar to Case Study 6
> **Symptom:** Furnace inlet (crude preheat) temperature gradually declining, forcing higher furnace duty and fuel consumption

---

> **Note on case type:** Like the seawater cooler case (Case Study 6), this is a **predictive/quantitative trending** exercise focused on identifying *which* exchanger in a train is degrading and *why*, rather than distinguishing between unrelated root-cause hypotheses.

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Furnace inlet (crude preheat) temperature gradually dropping over time; furnace duty and fuel use rising to compensate |
| Task | Identify which exchanger(s) in the train were fouling and why, to target corrective action instead of blanket cleaning the whole train |
| Actual root cause | Asphaltene precipitation in a specific crude/VGO exchanger, caused by incompatibility between blended crude sources |
| Fix | Mechanical cleaning of the affected exchanger during a turnaround; review of crude blending compatibility |
| Diagnostic signal | HTRI-based U-value trending isolated the fouling to one specific exchanger in the train, rather than the whole network degrading uniformly |
| Prevention | Periodic U-value trending per exchanger; asphaltene/blending compatibility screening before crude source changes |

---

## 2. Symptom

- **Furnace inlet temperature (crude preheat outlet) gradually declined over time.**
- **Furnace duty and fuel consumption increased** to compensate and hold the same furnace outlet/process target temperature.

## 3. Why This Needed Per-Exchanger Analysis, Not a Blanket Response

A preheat train is a series of multiple exchangers. A declining overall preheat temperature could result from **one badly fouled exchanger**, or from **several exchangers fouling moderately** — these call for very different responses (targeted cleaning of one unit vs. a broader train-wide cleaning campaign). Cleaning the wrong exchanger, or the whole train unnecessarily, wastes turnaround time and cost. The goal was to isolate **which** exchanger(s) were responsible before committing cleaning resources.

## 4. Diagnostic Approach

### Step 1 — Model the preheat train and calculate actual U-values per exchanger
Each exchanger in the train was modeled/monitored in HTRI (or equivalent EDR tool), using actual operating data to calculate the **actual overall heat transfer coefficient (U)** for each unit individually, not just the train's aggregate performance.

> **Same core technique as Case Study 6:** compare actual U to clean/design U, per exchanger, and trend it over time — this is a thermal-hydraulic rating exercise using built-in property correlations, not a VLE flash calculation.

### Step 2 — Trend U-value per exchanger over time
Historical trending of U for each individual exchanger identified that the **decline was concentrated in one specific crude/VGO exchanger**, while the other exchangers in the train remained close to their clean/design U values.

### Step 3 — Investigate the specific fouling mechanism at that exchanger
With the fouling isolated to one unit, the investigation turned to *why that specific exchanger*. Reviewing recent operating history alongside the crude supply record identified a period of **crude blending from multiple sources**.

### Step 4 — Confirm asphaltene incompatibility as the mechanism
Crude compatibility (asphaltene stability) analysis confirmed that the **blended crude sources were incompatible**, causing asphaltenes to destabilize and precipitate — depositing preferentially in the exchanger(s) operating in the temperature/velocity range where that particular crude blend's asphaltenes were least stable.

### Quantitative Basis

- Train of 6 exchangers; clean/design U values range 85–130 Btu/hr·ft²·°F depending on service.
- Furnace inlet temperature: normal baseline 546°F, dropped to **498°F over 5 months — a 48°F loss.**
- U-trending isolated the decline: **5 of 6 exchangers held within 8% of clean design U**; the crude/VGO exchanger (E-104) dropped from a clean 105 to **61 Btu/hr·ft²·°F — a 42% loss.**
- Crude compatibility screening (ASTM D7157-style P-value) on the blended crude measured a **P-value of 1.02**, below the 1.1 minimum threshold for asphaltene stability — confirming incompatibility following introduction of a new crude source.

## 5. Root Cause

**Blending of incompatible crude sources caused asphaltene destabilization and precipitation**, which deposited and fouled a specific crude/VGO exchanger in the preheat train — reducing that exchanger's heat transfer performance and, cumulatively, the overall furnace inlet temperature, even though the rest of the train remained close to design performance.

## 6. Corrective Action

1. **Mechanically cleaned the affected exchanger** during a scheduled turnaround.
2. **Reviewed crude blending compatibility practices**, incorporating asphaltene stability screening before future crude source changes/blends.

## 7. Verification

- E-104 U-value returned to **98 Btu/hr·ft²·°F — 93% of clean design**, following mechanical cleaning.
- Furnace inlet temperature recovered to **542°F**, and furnace fuel gas consumption dropped **~9%** back to its pre-fouling baseline.
- Held stable over the following **30 days.**

## 8. Prevention / Long-Term Fix

- Established **periodic U-value trending per exchanger** across the preheat train, so future fouling can be isolated to a specific unit early, rather than discovered only as an aggregate furnace-duty symptom.
- Added **asphaltene/blending compatibility screening** as a standard check before introducing a new crude blend, addressing the trigger mechanism rather than only the resulting fouling.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm the symptom (declining preheat temperature, rising furnace duty/fuel use) with trend data over time, not a single reading
- [ ] Model/monitor **each exchanger in the train individually**, not just the train's aggregate outlet temperature
- [ ] Calculate and trend **actual U vs. clean/design U per exchanger** to isolate which unit(s) are fouling
- [ ] Once isolated, review recent operating and feed history specific to that exchanger's service (crude source, blend changes, temperature/velocity regime)
- [ ] If crude blending is involved, check **asphaltene stability/compatibility** between the blended sources
- [ ] Target cleaning to the specific exchanger(s) identified, rather than cleaning the whole train by default
- [ ] After cleaning, confirm U recovery at the specific exchanger AND overall furnace inlet temperature/duty recovery
- [ ] Add compatibility screening to the crude blending change-management process to prevent recurrence

## 10. Key Takeaway

> A declining preheat train is a network problem, but the fix is almost always at a **specific exchanger**, not the whole train. Trend U-value per exchanger, not just the aggregate outlet temperature, to isolate where fouling is actually occurring — then investigate what changed *for that unit specifically* (often a feed/blend change) rather than assuming generic fouling. When crude blending is involved, treat asphaltene compatibility as something to check proactively before blending, not something to diagnose after a preheat train has already fouled.

---

## Related Concepts / Tags

`crude-preheat-train` `exchanger-fouling` `asphaltene-precipitation` `crude-compatibility` `HTRI` `U-value-trending` `furnace-inlet-temperature` `predictive-maintenance` `shell-and-tube`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
