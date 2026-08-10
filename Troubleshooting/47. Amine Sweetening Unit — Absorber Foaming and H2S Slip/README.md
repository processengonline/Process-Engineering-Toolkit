# Troubleshooting Guide: Amine Sweetening Unit — Absorber Foaming and H2S Slip

> **Category:** Gas Treating / Chemical Absorption
> **Unit:** Amine (MDEA/aMDEA) Sweetening Unit — Absorber Column
> **Tools:** HYSYS/UniSim Amine Property Package, absorber dP trending, foam tendency testing
> **Fluid Package:** Amine/Acid Gas package (Kent-Eisenberg or Li-Mather based electrolyte chemistry) — a generic PR/SRK cannot model chemical (reactive) absorption of CO2/H2S into amine
> **Symptom:** Sweet gas H2S content drifting above pipeline spec despite normal lean amine circulation and concentration

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Sweet gas H2S rising above the 4 ppm pipeline spec |
| Initially unclear | Amine quality issue vs. hydraulic/mass-transfer issue inside the absorber |
| Actual root cause | Absorber foaming caused by hydrocarbon condensate carryover and iron sulfide fines contaminating the amine, degrading tray/packing vapor-liquid contact |
| Fix | Improved inlet gas separation, added antifoam, installed amine filtration (particulate + carbon) |
| Diagnostic signal | Rising absorber differential pressure with normal lean amine concentration and circulation rate; foam confirmed at sample points |
| Prevention | Routine amine dP trending, scheduled foam-tendency testing, review of inlet separator performance |

---

## 2. Symptom

- **Sweet gas H2S content exceeded the 4 ppm pipeline specification.**
- **Lean amine circulation rate and concentration were both normal** — the parameters operators check first were not the cause.
- No equipment alarms had triggered yet, but gas quality was trending the wrong way.

## 3. Why This Wasn't an Obvious Amine-Quality Problem

H2S slip is most often blamed on lean amine quality (low concentration, high heat-stable salts, degraded amine). Here, amine concentration and circulation checked out normal, which meant the absorption *chemistry* driving force was intact — so the investigation had to shift toward **mass transfer/hydraulics inside the column**, a different failure mode entirely (loss of effective vapor-liquid contact, not insufficient absorbent).

## 4. Diagnostic Approach

### Step 1 — Confirm amine quality is not the driver
Lean amine concentration and circulation rate were checked against design and found normal, ruling out the most common cause.

### Step 2 — Review absorber hydraulic trends
Absorber **differential pressure was rising** — a classic signature of reduced vapor space and increased liquid holdup on the trays, consistent with **foaming** rather than a chemistry deficiency.

> **Why the amine fluid package matters here:** absorption of H2S/CO2 into amine is a **reactive** (chemical) absorption process, not simple physical VLE. Modeling or interpreting absorber performance correctly requires an amine-specific package (Kent-Eisenberg, Li-Mather, or equivalent) — a generic PR/SRK model would not correctly predict acid gas loading or column behavior for this system.

### Step 3 — Confirm foaming directly
Foam was observed at sample/sight points on the column, and **foam tendency testing** on the amine sample confirmed a stable foam — physical evidence, not just an inference from dP trends.

### Step 4 — Identify the foam-causing contaminant
Analysis of the amine identified **hydrocarbon condensate liquid carryover and iron sulfide (FeS) fines** as the foam stabilizers — both classic amine foaming culprits.

### Quantitative Basis

- Sweet gas H2S: baseline 2.1 ppm, rose to **9.8 ppm** against the 4 ppm pipeline spec.
- Absorber differential pressure: normal design range 0.30–0.45 bar; trended actual rose to **0.68 bar** — well above the design band despite unchanged gas/liquid loading.
- Lean amine held at **44.7 wt% MDEA** (design 45.0 wt%) and circulation held at design **850 gpm** throughout — both independently confirmed normal.
- Foam tendency test (ASTM D892-style): foam persisted **38 seconds** after air sparge stopped, versus a <10 second pass/fail criterion.
- Filtered-solids analysis: iron sulfide (FeS) content of **620 mg/L versus a <100 mg/L baseline**, confirming particulate-stabilized foam.

## 5. Root Cause

**Hydrocarbon liquid carryover from the upstream inlet separator, combined with iron sulfide particulates, contaminated the amine and caused stable foaming in the absorber.** The foam reduced effective vapor-liquid contact area and caused gas channeling, cutting mass transfer efficiency and allowing H2S to slip into the sweet gas — even though the amine's underlying chemistry (concentration, circulation) remained healthy.

## 6. Corrective Action

1. Improved/verified inlet gas separator performance to reduce hydrocarbon carryover into the amine system.
2. Added antifoam to break the existing foam.
3. Installed particulate and activated-carbon filtration on the amine circuit to remove FeS fines and residual hydrocarbon.

## 7. Verification

- Absorber differential pressure returned to **0.38 bar**, within the 0.30–0.45 bar design band.
- Sweet gas H2S content returned to **2.4 ppm**, within the 4 ppm spec, and held in the **2.0–2.8 ppm range over the following 30 days.**

## 8. Prevention / Long-Term Fix

- Established **routine absorber dP trending** as an early foaming indicator, independent of amine concentration checks.
- Scheduled **periodic foam tendency testing** on the amine.
- Reviewed inlet separator performance/maintenance to reduce the chance of repeat hydrocarbon carryover.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm lean amine concentration and circulation rate first (rules in/out the most common cause)
- [ ] If amine quality is normal, check absorber differential pressure trend for a foaming signature
- [ ] Physically confirm foam at sample/sight points before committing to an antifoam or filtration fix
- [ ] Run a foam tendency test on the amine sample
- [ ] Identify the specific contaminant (hydrocarbon carryover, FeS, degradation products, surfactants) rather than just treating with antifoam alone
- [ ] Trace contamination back to its source (inlet separator performance, corrosion products, upstream chemical injection)
- [ ] Add filtration appropriate to the contaminant identified
- [ ] Build absorber dP and foam-testing into routine monitoring, not just incident response

## 10. Key Takeaway

> Amine quality (concentration, circulation) tells you about absorption **capacity**; absorber differential pressure tells you about absorption **hydraulics**. H2S slip with healthy amine chemistry means the column isn't achieving proper vapor-liquid contact — check for foaming before assuming a chemistry problem, and always identify the specific contaminant driving the foam rather than treating symptoms with antifoam alone.

---

## Related Concepts / Tags

`amine-sweetening` `absorber-foaming` `h2s-slip` `kent-eisenberg` `foam-tendency-test` `hydrocarbon-carryover` `iron-sulfide` `gas-treating` `HYSYS` `UniSim`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
