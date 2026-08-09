# Troubleshooting Guide: Amine Regenerator — Reboiler Fouling and Stripper Foaming Carryover

> **Category:** Gas Treating / Chemical Regeneration
> **Unit:** Amine Regenerator (Stripper) and Reboiler
> **Tools:** HYSYS/UniSim Amine Package regenerator model, reboiler duty/U-value trending, amine degradation product analysis
> **Fluid Package:** Amine/Acid Gas package (reactive absorption chemistry) — the same specialized package family used for the absorber (Case Study 9), needed because regeneration also involves amine-CO2/H2S chemical equilibrium, not simple physical stripping
> **Symptom:** Lean amine concentration gradually declining despite stable reboiler steam/duty input, with occasional foam observed in the stripper overhead

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Lean amine concentration gradually dropping despite stable reboiler duty input; occasional stripper overhead foaming observed |
| Initially unclear | Whether this was a reboiler performance issue (fouling reducing effective duty) or a stripper hydraulic/foaming issue reducing stripping efficiency |
| Actual root cause | Reboiler tube fouling (from amine degradation products/heat-stable salts) reduced the effective heat transfer coefficient, lowering actual stripping steam generation even though duty setpoint/steam flow appeared normal — and the resulting poor stripping performance increased degradation products further, which also promoted stripper foaming |
| Fix | Mechanically cleaned reboiler tubes; implemented amine reclaiming to remove heat-stable salts and degradation products |
| Diagnostic signal | Reboiler duty/steam flow looked normal, but the calculated overall U-value (from actual temperatures and heat duty) had dropped well below clean design value |
| Prevention | Routine reboiler U-value trending; periodic heat-stable salt (HSS) analysis with a reclaiming program tied to HSS concentration |

---

## 2. Symptom

- **Lean amine concentration gradually declined** over time, even though **reboiler steam/duty input appeared stable** at its normal setpoint.
- **Occasional foam was observed in the stripper overhead.**

## 3. Why This Wasn't Assumed to Be a Simple Reboiler Duty Shortfall

A declining lean amine concentration with "stable" reboiler duty seems contradictory at first — if duty is stable, why would stripping performance decline? This apparent contradiction was the key clue: **steam flow/duty setpoint being stable doesn't guarantee the same amount of heat is actually being transferred to the amine**, if the reboiler's heat transfer surface itself has degraded. This needed the same "duty delivered vs. duty commanded" distinction seen in the distillation column case (Case Study 4), but for a reboiler fouling mechanism rather than an electrical fault.

## 4. Diagnostic Approach

### Step 1 — Confirm reboiler duty/steam flow at the utility side
Reboiler steam flow and pressure were reviewed and found to be at their normal, stable values — the utility side appeared to be delivering as commanded.

### Step 2 — Calculate the actual overall heat transfer coefficient (U)
Rather than relying on steam flow alone, the reboiler's **actual overall U-value** was calculated from measured amine-side and steam-side temperatures and the resulting heat duty, then compared to the **clean/design U-value** — the same core technique used in the seawater cooler case (Case Study 6).

**Finding:** Actual U had dropped **well below the clean design value**, meaning the reboiler was transferring significantly less heat to the amine than its steam consumption alone would suggest — a fouling signature, not a utility supply issue.

### Step 3 — Investigate the fouling mechanism
With fouling confirmed via the U-value gap, the reboiler tubes were inspected and amine samples analyzed for **heat-stable salts (HSS) and degradation products**, both known amine reboiler foulants.

**Finding:** Elevated HSS/degradation product levels were confirmed, consistent with fouling deposits found on inspection.

### Step 4 — Connect reduced stripping performance to the observed foaming
With reboiler heat transfer reduced, less stripping steam was actually being generated per unit of amine circulated, reducing acid gas stripping efficiency — which in turn tends to leave more degradation products in circulation (since they aren't being effectively purged), **compounding** the fouling over time and also contributing to the stripper foaming observed, since degradation products and heat-stable salts are well-known foam stabilizers (as in the absorber foaming case, Case Study 9, but here originating from regeneration-side chemistry rather than upstream carryover).

### Quantitative Basis

- Reboiler steam flow held steady at **8,200 lb/hr, 50 psig** throughout — utility side delivering as commanded.
- Calculated actual U-value dropped from a clean design **165 Btu/hr·ft²·°F to 98 Btu/hr·ft²·°F — a 41% loss** — despite the unchanged steam supply.
- Lean amine concentration declined from a design **50.0 wt% MDEA to 46.5 wt%** over the same 4-month period.
- HSS analysis: design/action threshold is 2.0 wt% of total amine inventory; measured concentration reached **4.8 wt%.**

## 5. Root Cause

**Reboiler tube fouling — driven by amine degradation products and heat-stable salts — reduced the reboiler's actual heat transfer coefficient**, so less stripping steam was generated per unit of circulated amine even though commanded steam flow/duty appeared normal. This reduced stripping efficiency, which allowed degradation products to accumulate further (a compounding effect) and also promoted the observed stripper foaming, together driving down lean amine concentration.

## 6. Corrective Action

1. **Mechanically cleaned the reboiler tubes** to remove fouling deposits and restore heat transfer performance.
2. **Implemented amine reclaiming** to remove heat-stable salts and degradation products from the circulating amine inventory.

## 7. Verification

- Reboiler U-value returned to **158 Btu/hr·ft²·°F**, within 5% of clean design, following mechanical cleaning.
- Lean amine concentration recovered to **49.6 wt%**, and HSS dropped to **1.6 wt%**, below the 2.0 wt% action threshold, after the reclaiming program.
- Stripper foaming incidents dropped from **3 events/week to zero over the following 45 days.**

## 8. Prevention / Long-Term Fix

- Established **routine reboiler U-value trending** (not just steam flow monitoring) as the standard performance check, since steam flow alone can look normal while actual heat transfer degrades.
- Implemented **periodic heat-stable salt analysis with a reclaiming program tied to HSS concentration**, addressing the chemistry driving both the fouling and the foaming rather than treating them as separate issues.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Don't treat stable steam flow/duty setpoint as proof the reboiler is delivering its intended heat — calculate actual U-value from measured temperatures and compare to clean/design value
- [ ] If U has dropped, inspect reboiler tubes and sample the amine for heat-stable salts and degradation products
- [ ] Recognize that reduced reboiler performance and stripper foaming are often linked through the same underlying chemistry (HSS/degradation products), not independent problems
- [ ] Mechanically clean fouled reboiler tubes
- [ ] Implement or increase amine reclaiming to remove HSS/degradation products from circulation
- [ ] Verify recovery via BOTH U-value trend AND lean amine concentration — a partial recovery in one without the other suggests the fix is incomplete
- [ ] Establish routine reboiler U-value trending and periodic HSS analysis as standing checks, since this failure mode compounds over time if left unaddressed

## 10. Key Takeaway

> A reboiler delivering its commanded steam flow isn't necessarily delivering its intended heat duty — fouling can quietly reduce actual heat transfer while the utility-side numbers look completely normal. In amine systems specifically, reboiler fouling and stripper foaming are often two symptoms of the same underlying chemistry problem (heat-stable salts and degradation products), and reduced stripping performance from fouling can make that chemistry worse over time. Calculate actual U-value, don't just watch steam flow, and treat reclaiming as the fix for the shared root cause rather than treating fouling and foaming as separate issues.

---

## Related Concepts / Tags

`amine-regenerator` `stripper` `reboiler-fouling` `heat-stable-salts` `HSS` `amine-degradation` `foaming` `U-value-trending` `amine-reclaiming` `gas-treating`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
