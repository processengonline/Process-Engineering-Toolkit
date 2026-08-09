# Troubleshooting Guide: Water Injection Well — Injectivity Decline from Incompatible Water Scaling

> **Category:** Reservoir Engineering / Water Injection / Scale Chemistry
> **Unit:** Water Injection Well, Waterflood System
> **Tools:** Hall plot analysis, injection water compatibility/scale prediction (electrolyte chemistry)
> **Fluid Package:** Electrolyte NRTL (ENRTL) or equivalent — the same category of tool used in the crude desalter case, since this is a mixing-induced scale prediction problem, not a hydrocarbon phase-equilibrium problem
> **Symptom:** Wellhead injection pressure climbing steadily to maintain target injection rate

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Injection pressure required to maintain target rate climbing steadily — injectivity index declining |
| Initially unclear | Whether this was near-wellbore formation damage from fines, a mechanical wellbore restriction, or a chemistry-driven scaling mechanism |
| Actual root cause | A sulfate-rich injection water source had recently been blended in without compatibility screening; mixing with calcium-rich formation water precipitated barium/calcium sulfate scale in the near-wellbore region |
| Fix | Acid/scale-dissolver stimulation treatment; corrected the blend ratio to use compatible water sources |
| Diagnostic signal | Hall plot slope increase (classic near-wellbore skin damage signature) correlated with the timing of a new water source being blended into the injection stream |
| Prevention | Water compatibility screening (mixing IP/Ksp calculation) required before blending any new water source; ongoing Hall plot trending as a standing check |

---

## 2. Symptom

- **Wellhead injection pressure climbed steadily** to maintain the target injection rate — a declining **injectivity index.**

## 3. Why This Wasn't Assumed to Be Simple Fines Plugging

Injectivity decline in a water injection well is very commonly caused by fines migration/plugging from suspended solids in the injected water — a mechanical filtration issue. But injectivity decline can equally be caused by **chemistry**: if two incompatible waters mix (e.g., a sulfate-rich source and a calcium/barium-rich formation water), scale can precipitate directly in the near-wellbore formation, producing the identical symptom (rising injection pressure, declining injectivity) through a completely different mechanism requiring a completely different fix.

## 4. Diagnostic Approach

### Step 1 — Run a Hall plot analysis
Cumulative injection pressure was plotted against cumulative injected volume (Hall plot) to characterize the nature of the decline.

**Finding:** The Hall plot showed a **slope increase** — the classic signature of developing **near-wellbore skin damage**, rather than a wellbore-mechanical restriction (which would typically show a different pattern).

### Step 2 — Review recent changes to the injection water source
With skin damage confirmed as the general mechanism, recent operational history was reviewed for anything that could explain a new damage mechanism starting.

**Finding:** A **new water source had recently been blended into the injection stream**, timing consistent with the onset of the Hall plot slope change.

### Step 3 — Check water compatibility between the blended sources
Using an electrolyte-chemistry model (the same category of tool used in the crude desalter salt deposition case), the **ionic product** of the mixed water (combining the new source with the existing formation/injection water) was calculated against the **solubility product** of common scale-forming salts.

**Finding:** The mixed water showed a **significant supersaturation** with respect to barium sulfate and calcium sulfate, meaning scale precipitation was thermodynamically favorable specifically as a result of this blend.

### Step 4 — Confirm via water analysis
Water analysis of both sources confirmed the new source was **sulfate-rich**, while the existing formation/injection water was **calcium/barium-rich** — the classic ion pairing that produces highly insoluble sulfate scales when mixed.

### Quantitative Basis

- Hall plot slope increased from a baseline **0.8 psi/bbl to 3.1 psi/bbl** — a nearly 4x increase, consistent with developing near-wellbore skin.
- Wellhead injection pressure required to hold a constant 4,500 bwpd rate rose from a baseline **1,450 psig to 2,380 psig** over 10 weeks.
- New water source sulfate content: **1,850 mg/L.** Existing formation/injection water barium content: **95 mg/L**, calcium: **620 mg/L.**
- Electrolyte model IP/Ksp ratio for BaSO₄ in the blended water: **6.4** (strongly supersaturated), versus **0.3** for either source water individually (undersaturated) — confirming the scale risk was specifically a mixing effect, not a property of either water alone.

## 5. Root Cause

**A new, sulfate-rich water source was blended into the injection stream without compatibility screening.** Mixing with the existing calcium/barium-rich water created strong supersaturation with respect to barium and calcium sulfate, precipitating scale in the near-wellbore formation and progressively reducing injectivity — even though neither water source alone would have caused scaling.

## 6. Corrective Action

1. **Performed an acid/scale-dissolver stimulation treatment** to remove the near-wellbore scale damage.
2. **Corrected the blend ratio**, reducing the sulfate-rich source's contribution to a level the electrolyte model confirmed as compatible (IP/Ksp < 1) with the existing water.

## 7. Verification

- Post-stimulation, wellhead injection pressure at the 4,500 bwpd target rate dropped to **1,610 psig**, close to the 1,450 psig baseline.
- Hall plot slope, re-calculated over the following injection period, returned to **0.9 psi/bbl**, near the original 0.8 psi/bbl baseline.
- Recalculated IP/Ksp ratio for BaSO₄ at the corrected blend ratio: **0.6** — undersaturated, confirming the scaling risk had been eliminated, not just the existing scale removed.

## 8. Prevention / Long-Term Fix

- Established **mandatory water compatibility screening** (mixing IP/Ksp calculation) before blending any new water source into the injection stream, closing the gap that allowed this blend to go unchecked.
- **Ongoing Hall plot trending** established as a standing check, so any future skin damage — chemical or mechanical — is caught early.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Run a Hall plot analysis to characterize the nature of an injectivity decline (skin damage signature vs. other patterns)
- [ ] Review recent changes to the injection water source(s) or blend ratios for timing correlation with the decline
- [ ] If a new source or blend change correlates, run a water compatibility (mixing IP/Ksp) calculation using an electrolyte-chemistry model — checking the MIXED water, not each source individually
- [ ] Confirm via direct water analysis (sulfate, calcium, barium, etc.) of both sources
- [ ] If chemistry-driven scaling is confirmed, treat with acid/scale-dissolver stimulation, and correct the blend ratio to a compatible level
- [ ] Verify recovery via BOTH injection pressure/Hall plot AND recalculated IP/Ksp at the corrected blend, since removing existing scale doesn't guarantee the underlying incompatibility has been fixed
- [ ] Require compatibility screening as a standard step before blending any new water source going forward

## 10. Key Takeaway

> Declining injectivity looks the same on a pressure trend whether it's caused by fines plugging or by chemistry — a Hall plot alone can't tell them apart. When a new water source has recently been introduced, check compatibility of the **mixed** water, not just each source's individual quality; two waters that are each perfectly fine on their own can precipitate scale the moment they're blended, and that's a chemistry problem no amount of filtration will fix.

---

## Related Concepts / Tags

`water-injection` `injectivity-decline` `hall-plot` `scale-prediction` `barium-sulfate` `calcium-sulfate` `water-compatibility` `electrolyte-nrtl` `waterflood` `near-wellbore-damage`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
