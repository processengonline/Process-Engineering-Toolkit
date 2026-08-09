# Troubleshooting Guide: Produced Water Disposal Well — Injectivity Decline from Fines Migration

> **Category:** Reservoir Engineering / Produced Water Disposal
> **Unit:** Produced Water Disposal (SWD) Well
> **Tools:** Hall plot analysis, total suspended solids (TSS) trending of injected water, filter integrity verification
> **Fluid Package:** Not applicable — this is a mechanical/particulate plugging investigation, not a phase-equilibrium problem
> **Symptom:** Wellhead injection pressure climbing steadily at constant rate — declining injectivity

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Wellhead injection pressure climbing steadily to maintain constant injection rate |
| Initially unclear | Whether this was chemistry-driven scaling (as in the water injection well case, Case Study 42) or mechanical fines-plugging from suspended solids in the injected water |
| Actual root cause | An upstream produced water filtration system had a failed/bypassed filter housing, allowing elevated total suspended solids (fine particulates) into the injection stream, which plugged pore throats in the near-wellbore formation |
| Fix | Repaired the filtration bypass; performed acid/mechanical stimulation to remove near-wellbore fines damage |
| Diagnostic signal | Hall plot slope increase correlated with a rise in TSS content of the injected water, and the filter bypass had NOT shown an abnormal differential pressure — the standard filter health indicator gave a false-normal reading |
| Prevention | Continuous TSS monitoring on injection water tied to Hall plot trending as a combined check; filter integrity verification beyond just differential pressure, since a bypass can look normal on dP alone |

---

## 2. Symptom

- **Wellhead injection pressure climbed steadily** at a constant target injection rate — a declining **injectivity index**, the same general symptom pattern as the water injection well scaling case (Case Study 42), but here with a different underlying mechanism.

## 3. Why This Wasn't Assumed to Be the Same Scaling Mechanism as Case Study 42

Given the similarity to the earlier water injection well case, a chemistry-driven scaling explanation was a reasonable starting hypothesis. But injectivity decline has (at least) two well-known distinct mechanisms — chemical scaling (incompatible water mixing) and **mechanical fines plugging** (suspended solids physically lodging in formation pore throats) — and these require different diagnostic paths and different fixes. It was necessary to determine which mechanism, or combination, was actually occurring here rather than assuming the same cause as a previous, superficially similar case.

## 4. Diagnostic Approach

### Step 1 — Run a Hall plot analysis
Cumulative injection pressure was plotted against cumulative injected volume, confirming a **slope increase** — the general near-wellbore skin damage signature, consistent with either scaling or fines plugging at this stage.

### Step 2 — Check water compatibility for a scaling mechanism
Following the same approach as Case Study 42, the injection water's ionic composition was checked for compatibility/scaling risk using an electrolyte-chemistry assessment.

**Finding:** The water chemistry showed **no significant scaling risk** — IP/Ksp ratios for common scale-forming salts remained well below 1, ruling out the chemistry-driven mechanism seen in the earlier case.

### Step 3 — Review injected water solids content
With scaling ruled out, **total suspended solids (TSS)** content of the injected water was reviewed over the period the Hall plot slope began increasing.

**Finding:** TSS content showed a **clear upward trend**, correlating closely with the onset of the Hall plot slope change — pointing toward mechanical fines plugging rather than chemical scaling.

### Step 4 — Investigate the upstream filtration system
With elevated TSS confirmed as the likely mechanism, the upstream produced water filtration system (responsible for removing suspended solids before injection) was investigated.

**Finding:** A **filter housing was found bypassed/failed**, but critically, its **differential pressure reading had remained normal** throughout — because a bypass allows flow to avoid the filter media entirely, it does not register as the differential pressure increase that a *plugged* (rather than bypassed) filter would show, making this failure mode invisible to the standard dP-based filter health check.

### Quantitative Basis

- Hall plot slope increased from a baseline **0.6 psi/bbl to 2.4 psi/bbl.**
- Injection water TSS content rose from a baseline **3 mg/L to 42 mg/L** over the same period — a 14x increase, well above the typical <10 mg/L target for this service.
- The bypassed filter housing's differential pressure reading remained at a **normal 4-6 psi** throughout, indistinguishable from a properly functioning filter on that indicator alone — confirmed only via a direct upstream/downstream TSS sample comparison across that specific housing, which showed **no TSS reduction across it (41 mg/L in, 42 mg/L out)**, versus an expected >90% reduction for a functioning filter.

## 5. Root Cause

**A filter housing in the upstream produced water filtration train had failed/bypassed**, allowing water to pass around the filter media entirely rather than through it. Because a bypass doesn't restrict flow the way a plugged filter does, it produced **no abnormal differential pressure reading**, allowing elevated total suspended solids to pass through undetected and migrate into the near-wellbore formation, where they plugged pore throats and progressively reduced injectivity.

## 6. Corrective Action

1. **Repaired the bypassed filter housing**, restoring proper flow through the filter media.
2. **Performed acid/mechanical stimulation** to remove the near-wellbore fines damage that had already accumulated.

## 7. Verification

- Post-repair, direct TSS sampling across the previously-bypassed housing showed **41 mg/L in, 3 mg/L out — a 93% reduction**, confirming the filter was now functioning as designed.
- Injection water TSS at the wellhead returned to **4 mg/L**, within the <10 mg/L target.
- Following stimulation, wellhead injection pressure at the constant target rate dropped to near baseline, and the Hall plot slope, recalculated over the following injection period, returned to **0.7 psi/bbl**, close to the 0.6 psi/bbl original baseline.

## 8. Prevention / Long-Term Fix

- Established **continuous TSS monitoring on the injection water, tied to Hall plot trending** as a combined standing check, so either a chemistry-driven or fines-driven mechanism is caught early and can be distinguished quickly.
- Implemented **filter integrity verification beyond differential pressure alone** (periodic direct upstream/downstream TSS sampling across each filter housing), since this incident demonstrated that a bypass failure mode is invisible to dP monitoring specifically.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Run a Hall plot analysis to confirm and characterize an injectivity decline
- [ ] Check water compatibility/scaling risk (electrolyte IP/Ksp assessment) to rule in/out a chemistry-driven mechanism, as in Case Study 42 — don't assume the same mechanism as a similar prior case without checking
- [ ] If scaling is ruled out, review injected water TSS trend for correlation with the onset of the Hall plot change
- [ ] If TSS has risen, investigate the upstream filtration system directly — including a check for a BYPASSED (not just plugged) filter, since a bypass will show normal, not elevated, differential pressure
- [ ] Confirm any suspected filter bypass via direct upstream/downstream TSS sampling across that specific housing, not differential pressure alone
- [ ] Repair the filtration issue and perform stimulation to address existing near-wellbore fines damage
- [ ] Confirm recovery via BOTH filter TSS reduction performance AND the Hall plot slope returning toward baseline
- [ ] Add TSS monitoring and periodic direct filter integrity verification (not just dP) to the standing water injection monitoring program

## 10. Key Takeaway

> Two different injectivity-decline mechanisms — chemical scaling and mechanical fines plugging — produce the identical symptom (a Hall plot slope increase), so don't assume a new case matches a previous similar-looking one without checking both. And when investigating a filtration system as a possible fines source, remember that a **bypassed** filter shows *normal*, not elevated, differential pressure — the standard filter health indicator can give a false-normal reading in exactly the failure mode you're trying to catch, so a direct TSS check across the filter is the only way to confirm it's actually working.

---

## Related Concepts / Tags

`produced-water-disposal` `SWD-well` `injectivity-decline` `hall-plot` `fines-migration` `total-suspended-solids` `TSS` `filter-bypass` `near-wellbore-damage`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
