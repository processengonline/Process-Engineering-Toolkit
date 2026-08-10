# Troubleshooting Guide: Nitrogen Generation Package (PSA) — Declining Product Purity

> **Category:** Utilities / Gas Generation / Cyclic Adsorption
> **Unit:** Pressure Swing Adsorption (PSA) Nitrogen Generation Package
> **Tools:** Cycle-by-cycle product purity trending, adsorber bed pressure profile review
> **Fluid Package:** Not applicable in the VLE sense — PSA performance is governed by adsorption kinetics/selectivity, similar in category to the molecular sieve dehydration case (Case Study 10), not phase-equilibrium thermodynamics
> **Symptom:** Product nitrogen purity gradually declining below the required spec for its blanketing/inerting service, despite the PSA package running its normal automated cycle

---

> **Note on case type:** Like Case Study 10 (molecular sieve dehydration), this is a **cyclic adsorption performance** investigation rather than a VLE-based diagnosis.

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Product nitrogen purity gradually declining below spec despite the PSA package running its normal automated cycle |
| Initially unclear | Whether this was carbon molecular sieve (CMS) media degradation (end-of-life) or a cycle-timing/valve performance issue preventing the beds from completing their intended adsorption/regeneration steps properly |
| Actual root cause | A slowly leaking cycle valve was allowing partial cross-flow between beds during what should have been an isolated step, effectively shortening the usable adsorption time and allowing oxygen breakthrough earlier than the cycle timer assumed |
| Fix | Repaired/replaced the leaking cycle valve; verified full isolation between beds during each cycle step |
| Diagnostic signal | Bed pressure profiles during cycle steps that should show a fully isolated bed instead showed a small but consistent pressure interaction with the adjacent bed, inconsistent with a properly sealed cycle valve |
| Prevention | Routine cycle valve leak/seat testing; per-cycle bed pressure profile review as a standing diagnostic, not just overall product purity monitoring |

---

## 2. Symptom

- **Product nitrogen purity gradually declined**, falling below the specification required for its blanketing/inerting service.
- The PSA package continued to **run its normal automated cycle** — no obvious alarm or cycle fault was indicated by the control system.

## 3. Why This Wasn't Assumed to Be Simple CMS Media End-of-Life

Declining PSA product purity is often attributed to **carbon molecular sieve (CMS) media degradation** — a normal end-of-life process for this consumable, addressed by media replacement. Before committing to that (costly) conclusion, it was worth checking whether the **cycle itself** was executing correctly, since a valve or cycle-timing fault can produce the same purity-decline symptom as genuine media degradation, but with a very different (and cheaper) fix.

## 4. Diagnostic Approach

### Step 1 — Review product purity trend for a run-time-correlated pattern
Purity decline was reviewed against cumulative operating time/cycles, checking for a smooth, aging-consistent decline pattern (as would be expected from genuine CMS degradation).

### Step 2 — Review per-cycle bed pressure profiles
Rather than relying on purity trend alone, individual **bed pressure profiles** during each step of the automated cycle were reviewed in detail — specifically checking whether each bed was achieving true pressure isolation during the steps where isolation is required (e.g., during the other bed's regeneration/blowdown).

**Finding:** Bed pressure profiles showed a **small but consistent pressure interaction with the adjacent bed** during steps that should have shown full isolation — inconsistent with a properly sealed cycle valve.

### Step 3 — Investigate the specific cycle valve responsible for that isolation step
The specific valve responsible for isolating the two beds during that cycle step was inspected and found to have a **slow internal leak**, allowing partial cross-flow between beds rather than the clean isolation the cycle design assumes.

### Step 4 — Connect the leak to reduced effective adsorption time
With partial cross-flow occurring during what should be an isolated adsorption step, the **effective, usable adsorption time** for the bed currently producing nitrogen was being shortened — allowing oxygen to break through earlier in the cycle than the fixed cycle timer accounted for, since the timer assumed full isolation and a clean cycle.

### Quantitative Basis

- Product spec for blanketing service: ≥99.5% N₂ (≤500 ppm O₂). Baseline: 99.7% N₂ (300 ppm O₂). Declined to **98.9% N₂ (11,000 ppm O₂)** — well below spec.
- 2-bed PSA, 60-second total cycle, 55 seconds nominal adsorption time per bed. During the adjacent bed's blowdown/purge step, the producing bed's pressure should hold steady at 100 ± 1 psig; trend data showed it dipping to **94 psig** during that step — a cross-flow signature.
- Bench leak test on the isolation valve for that step measured **8 SCFH seat leakage, against a ≤0.5 SCFH allowable spec** — a 16x exceedance.
- Estimated effective usable adsorption time, accounting for the cross-flow loss, was **≈38 seconds instead of the nominal 55 — a 31% reduction**, consistent with oxygen breaking through well before the fixed 55-second cycle timer expected it.

## 5. Root Cause

**A slowly leaking cycle valve was allowing partial cross-flow between adsorber beds during a step that should have been fully isolated**, shortening the effective usable adsorption time for the producing bed and causing oxygen breakthrough earlier than the fixed automated cycle timer assumed — reducing product nitrogen purity even though CMS media itself had not reached genuine end-of-life.

## 6. Corrective Action

1. **Repaired/replaced the leaking cycle valve.**
2. **Verified full isolation between beds** during the relevant cycle step following the repair.

## 7. Verification

- Post-repair, bed pressure held steady at **99–100 psig** through the previously-affected isolation step, with no further dip.
- Product O₂ content dropped to **280 ppm**, giving **99.72% N₂ purity** — better than the original baseline.
- Held stable across **~43,200 cycles (30 days of continuous operation)** with no recurrence of the decline.

## 8. Prevention / Long-Term Fix

- Established **routine cycle valve leak/seat testing**, since a slow internal leak like this can develop gradually and not trigger any cycle-fault alarm on its own.
- Added **per-cycle bed pressure profile review as a standing diagnostic**, rather than relying solely on overall product purity monitoring, which only reveals a problem after it has already affected product quality.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review product purity decline against cumulative run-time/cycles for a pattern consistent with normal media aging
- [ ] Before assuming CMS/adsorbent media end-of-life, review **per-cycle bed pressure profiles** in detail, not just the overall purity trend
- [ ] Check specifically for pressure interaction between beds during steps that should show full isolation
- [ ] If found, identify and inspect the specific cycle valve responsible for isolation during that step
- [ ] Repair/replace a leaking cycle valve and verify full isolation is restored
- [ ] Confirm purity recovery following the valve repair before concluding media replacement is unnecessary
- [ ] Establish routine cycle valve leak/seat testing and per-cycle bed pressure profile review as standing diagnostics, since a slow internal leak can develop without triggering a standard cycle-fault alarm

## 10. Key Takeaway

> Declining PSA product purity doesn't automatically mean the adsorbent media has reached end-of-life — a leaking cycle valve can produce the exact same symptom by quietly shortening the effective adsorption time each cycle, well before the fixed cycle timer would expect oxygen breakthrough. Reviewing per-cycle bed pressure profiles for proper isolation is a much cheaper and more specific diagnostic step than replacing adsorbent media on the assumption of normal aging.

---

## Related Concepts / Tags

`nitrogen-generation` `PSA` `pressure-swing-adsorption` `carbon-molecular-sieve` `cycle-valve` `bed-isolation` `product-purity` `oxygen-breakthrough` `cyclic-process`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
