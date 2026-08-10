# Troubleshooting Guide: Sulfur Recovery Unit (Claus) — Catalyst Deactivation and Conversion Decline

> **Category:** Sulfur Recovery / Catalytic Process
> **Unit:** Claus Sulfur Recovery Unit (SRU) — Catalytic Reactor Beds
> **Tools:** Claus process/reaction equilibrium simulation using actual feed composition and reactor bed temperature profiles
> **Fluid Package:** A specialized Claus/sulfur thermodynamic package — not a generic PR/SRK — due to sulfur allotrope behavior and Claus reaction equilibrium requirements
> **Symptom:** Tail gas SO2/H2S ratio drifting off target, with overall sulfur recovery efficiency gradually declining

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Tail gas SO2/H2S ratio drifting off its target value; overall sulfur recovery efficiency declining gradually |
| Initially unclear | Whether the shift was driven by air demand control tuning (a process/control issue) or a genuine loss of catalyst activity (a mechanical/catalyst issue) |
| Actual root cause | Catalyst deactivation in the first reactor bed due to sulfation, caused by an oxygen excess/upset event, reducing Claus reaction conversion |
| Fix | Catalyst bed replaced/regenerated during a planned outage; review of air demand control tuning |
| Diagnostic signal | Reactor bed temperature rise (exotherm) profile not matching the expected conversion-driven rise; catalyst sample analysis confirmed sulfation |
| Prevention | Air demand analyzer calibration checks; scheduled catalyst activity sampling |

---

## 2. Symptom

- **Tail gas SO2/H2S ratio drifted off its target value** — normally maintained near stoichiometric balance for optimal Claus conversion.
- **Overall sulfur recovery efficiency declined gradually** over time, rather than as a sudden step change.

## 3. Why This Wasn't Immediately Treated as a Simple Air Demand Tuning Issue

An off-target SO2/H2S ratio is most commonly a control/tuning problem — the air demand controller isn't dosing combustion air correctly relative to acid gas feed, and adjusting the controller typically resolves it quickly. But a **gradual decline in overall conversion efficiency**, on top of the ratio drift, raised the possibility that something more fundamental — **catalyst activity itself** — had degraded. These require very different responses: a control tuning adjustment vs. a catalyst bed replacement during a planned outage, which has significant scheduling and cost implications.

## 4. Diagnostic Approach

### Step 1 — Review the SO2/H2S ratio trend alongside air demand control performance
The ratio drift was reviewed together with air demand controller performance to see whether simple retuning would explain the full picture.

### Step 2 — Compare actual reactor bed temperature profiles to expected exotherm
Using a **Claus reaction equilibrium model** with actual feed H2S/acid gas composition, expected reactor bed temperature rise (from the exothermic Claus reaction) was calculated and compared against actual bed temperature data.

> **Why a specialized Claus package matters here:** Claus reaction equilibrium and sulfur allotrope behavior are not captured by a generic cubic EOS — accurately modeling expected conversion and the resulting exotherm requires a package built specifically for sulfur/Claus chemistry, similar in principle to needing amine-specific packages (Case Study 9) or wax/hydrate add-ons (Case Studies 5 and 8) for their respective specialized chemistries.

**Finding:** The **actual temperature rise across the first reactor bed did not match the exotherm expected** for the actual feed composition at design conversion — indicating **less reaction (lower conversion) was occurring than the feed composition alone would predict.**

### Step 3 — Confirm catalyst condition directly
A **catalyst sample was pulled from the first reactor bed and analyzed**, confirming **sulfation** — a known catalyst deactivation mechanism where catalytically active sites are converted to inactive sulfate species.

### Step 4 — Identify the trigger for sulfation
Sulfation is commonly triggered by **oxygen excess** reaching the catalyst bed (e.g., from an air demand upset or control excursion), which was reviewed against operating history to identify a prior upset consistent with the timing of the observed decline.

### Quantitative Basis

- Tail gas SO2/H2S ratio target: 2:1 (stoichiometric Claus balance), acceptable band 1.8–2.2:1. Drifted to **3.4:1.**
- Overall sulfur recovery: baseline 96.5%, declined to **91.2% — a 5.3-point drop.**
- Claus equilibrium model, at actual feed H2S concentration and design conversion, predicted a bed 1 exotherm of **62°F. Actual measured ΔT: 34°F — 45% below expected**, indicating reduced conversion.
- Catalyst sample XRF analysis measured **8.2 wt% sulfate loading, versus <2 wt% for fresh/healthy catalyst.**
- Air demand analyzer logs showed a **6-hour period of O2 breakthrough to 0.8 vol%** in the tail gas (against a <0.1% normal target) roughly **3 weeks prior** to the onset of the decline — the likely sulfation trigger.

## 5. Root Cause

**Catalyst in the first reactor bed was deactivated by sulfation**, triggered by a prior **oxygen excess/upset event** in air demand control. The sulfated catalyst had reduced active sites for the Claus reaction, lowering conversion — which manifested as both the declining overall sulfur recovery efficiency and the drifting tail gas SO2/H2S ratio (since reduced conversion in the catalytic stage also affects the downstream mass balance the ratio depends on).

## 6. Corrective Action

1. **Replaced/regenerated the affected catalyst bed** during a planned outage.
2. **Reviewed air demand control tuning** to reduce the likelihood of a repeat oxygen excess upset.

## 7. Verification

- Bed 1 exotherm restored to **60°F**, close to the 62°F expected value.
- Tail gas SO2/H2S ratio returned to **2.05:1**, within the 1.8–2.2:1 target band.
- Overall sulfur recovery efficiency restored to **96.1%**, and held stable over the following **30 days.**

## 8. Prevention / Long-Term Fix

- Established **air demand analyzer calibration checks** to catch drift before it causes an oxygen excess event.
- Implemented **scheduled catalyst activity sampling**, so gradual deactivation can be detected and planned for before it manifests as a conversion/ratio problem.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review the SO2/H2S ratio trend alongside air demand controller performance — confirm whether simple retuning explains the full picture
- [ ] If overall conversion efficiency is also declining (not just the ratio), suspect catalyst activity rather than control tuning alone
- [ ] Model expected reactor bed exotherm from actual feed composition using a Claus-specific reaction/equilibrium model
- [ ] Compare actual bed temperature rise to the expected exotherm — a mismatch indicates reduced conversion, i.e., a catalyst issue, not just an air/acid-gas ratio issue
- [ ] Pull and lab-analyze a catalyst sample to confirm deactivation mechanism (sulfation, coking, poisoning) directly
- [ ] Review operating history for events (oxygen excess, temperature excursions, liquid sulfur carryover) consistent with the timing of the decline
- [ ] Plan catalyst replacement/regeneration around a scheduled outage where possible, informed by the confirmed diagnosis rather than reacting immediately
- [ ] Add air demand analyzer calibration checks and scheduled catalyst activity sampling to standing operations monitoring

## 10. Key Takeaway

> A drifting SO2/H2S ratio isn't always a control tuning problem — if overall conversion efficiency is also declining, compare actual reactor bed exotherm to what the feed composition should produce at design conversion. A mismatch there points to the catalyst itself, not the air demand controller, and a catalyst sample analysis will tell you the specific deactivation mechanism (sulfation, coking, poisoning) so the fix — and the prevention program — targets the right root cause.

---

## Related Concepts / Tags

`sulfur-recovery-unit` `SRU` `claus-process` `catalyst-deactivation` `sulfation` `air-demand-control` `tail-gas` `SO2-H2S-ratio` `catalyst-sampling` `reactor-exotherm`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
