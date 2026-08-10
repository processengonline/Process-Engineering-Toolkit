# Troubleshooting Guide: Corrosion Under Insulation — Pipeline Leak at a Previously Unmonitored Location

> **Category:** Integrity Management / Corrosion
> **Unit:** Insulated Process Pipeline, Intermittent Service
> **Tools:** Risk-based inspection (RBI) review, corrosion-under-insulation (CUI) susceptibility screening, non-intrusive inspection (guided wave/pulsed eddy current)
> **Fluid Package:** Not applicable — this is a mechanical integrity/corrosion investigation, not a process simulation exercise
> **Symptom:** A small process leak detected at an insulated pipeline location with no history of inspection findings or known corrosion concerns

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Small leak discovered at an insulated pipeline section previously considered low-risk with no inspection findings |
| Initially unclear | Whether this was an isolated, unpredictable failure or a symptom of a broader CUI risk that had gone undetected by the existing inspection program |
| Actual root cause | Corrosion under insulation (CUI) had developed at this location due to a specific combination of intermittent wet/dry cycling (from a nearby deluge/wash-down area) and a temperature range known to promote CUI, which fell outside the criteria the existing risk-based inspection program used to prioritize inspection locations |
| Fix | Repaired the leaking section; expanded RBI screening criteria to capture this combination of conditions |
| Diagnostic signal | Once the specific local conditions (wet/dry cycling, temperature band) were reviewed, this location matched known CUI risk factors closely, despite not having been flagged by the existing program |
| Prevention | Revised RBI/CUI screening criteria to include the newly recognized risk combination; added non-intrusive inspection at similarly-situated locations plant-wide |

---

## 2. Symptom

- **A small process leak was discovered at an insulated pipeline section** during routine walkdown/inspection.
- This location had **no history of inspection findings** and was not flagged as high-risk by the existing risk-based inspection (RBI) program.

## 3. Why This Wasn't Treated as a One-Off, Unpredictable Failure

It's tempting to treat an unexpected leak at a "clean" location as a rare, essentially random event — repair it and move on. But corrosion under insulation is a well-understood, mechanistically predictable phenomenon: it requires water ingress under insulation combined with a specific temperature range (generally intermittent or cyclic operating temperatures are higher risk than continuously hot or continuously cold service). Before treating this as an isolated anomaly, it was worth asking whether the **existing risk screening had actually captured the true risk factors present at this specific location**, or whether there was a gap in the program itself.

## 4. Diagnostic Approach

### Step 1 — Confirm the failure mechanism at the leak location
Inspection of the leak location (after insulation removal) confirmed **corrosion under insulation** as the failure mechanism — pitting/wall loss consistent with CUI, not another mechanism like erosion or a weld defect.

### Step 2 — Review local environmental/operating conditions specific to this location
Rather than treating the location generically, the **specific local conditions** were reviewed: proximity to a nearby deluge/wash-down system (a source of intermittent water ingress under insulation) and the pipeline's actual operating temperature range at this point (intermittent service, cycling through a temperature band known to be high-risk for CUI).

### Step 3 — Compare against the existing RBI screening criteria
The existing RBI program's screening criteria for CUI risk were reviewed against these specific local conditions.

**Finding:** The **combination** of intermittent wet/dry cycling from the nearby deluge system and the specific cyclic temperature range **fell outside the criteria the RBI program used to flag locations for CUI-focused inspection** — the program had been screening for more commonly recognized CUI risk combinations, but hadn't specifically captured this particular local wet/dry cycling source.

### Step 4 — Assess for similarly-situated locations plant-wide
With the gap identified, other pipeline/equipment locations sharing the same combination (proximity to deluge/wash-down systems, similar intermittent temperature service) were identified for non-intrusive inspection, since the same undetected risk factor could plausibly exist elsewhere.

### Quantitative Basis

- 6-in carbon steel line, nominal wall 0.280 in (Sch 40). At the leak, remaining wall measured **0.045 in — 84% wall loss**, pit depth 0.235 in.
- Line operates intermittently through 140–180°F, spending an estimated **~40% of operating hours within the 25–250°F band** API 583 identifies as highest CUI risk (the temperature range where water neither stays liquid-free nor boils off insulation before it can corrode).
- The nearby deluge system, tested monthly, sits **8 ft from the leak location** — outside the existing RBI program's **3 ft screening radius** for deluge/wash-down proximity, so the location was never flagged despite realistic wetting exposure.
- Following criteria revision (radius widened to 15 ft, temperature-cycling logic added), **22 additional locations plant-wide** matched the expanded criteria; non-intrusive screening found **3 of the 22** already showing early-stage wall loss (10–15% by pulsed eddy current), caught before a leak.

## 5. Root Cause

**Corrosion under insulation developed due to a specific combination of intermittent water ingress (from a nearby deluge/wash-down system) and a cyclic operating temperature range known to promote CUI.** This particular combination of risk factors was not captured by the existing risk-based inspection program's screening criteria, so the location had never been flagged or prioritized for inspection despite genuinely being at elevated CUI risk.

## 6. Corrective Action

1. **Repaired the leaking pipeline section.**
2. **Expanded RBI/CUI screening criteria** to explicitly include this combination of local wet/dry cycling source and temperature range.

## 7. Verification

- Repaired section confirmed sound (wall thickness restored to nominal 0.280 in) via post-repair UT inspection.
- All **22 newly-flagged locations** were screened via guided wave/pulsed eddy current within 90 days; the **3 locations with early-stage wall loss** were scheduled for repair/re-insulation before reaching leak condition.

## 8. Prevention / Long-Term Fix

- **Revised RBI/CUI screening criteria** to capture the specific risk combination identified (proximity to intermittent water sources like deluge/wash-down systems, combined with cyclic operating temperature), closing the gap that had allowed this location to go unflagged.
- Added **non-intrusive inspection (guided wave/pulsed eddy current) at similarly-situated locations** plant-wide, rather than waiting for further leaks to identify them.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm the failure mechanism directly (insulation removal and inspection) rather than assuming based on service type alone
- [ ] Review the specific **local** environmental and operating conditions at the failure location — not just generic service classification
- [ ] Check for intermittent water ingress sources near the location (deluge systems, wash-down areas, roof drainage, steam tracing leaks)
- [ ] Check the actual operating temperature range/cycling pattern at that specific point, not just the nominal process design temperature
- [ ] Compare these specific local conditions against the existing RBI/CUI screening criteria — look for a genuine gap, not just a missed inspection
- [ ] If a screening gap is found, treat it as systemic: identify other locations plant-wide sharing the same combination of risk factors
- [ ] Expand screening criteria and inspection scope accordingly, rather than treating the finding as an isolated repair
- [ ] Recognize that CUI risk is driven by **local** conditions (nearby water sources, actual temperature cycling) that can differ significantly from a line's nominal service classification

## 10. Key Takeaway

> An unexpected leak at a location with a clean inspection history isn't necessarily bad luck — it can mean the risk screening program has a genuine gap for a specific combination of local conditions. CUI risk is driven by local water ingress sources and actual (not nominal) temperature cycling, which can vary significantly even within the same nominal service classification. When a "low-risk" location fails, treat the RBI criteria itself as a hypothesis to test, and look for other locations sharing the same overlooked risk combination before the next leak finds them for you.

---

## Related Concepts / Tags

`corrosion-under-insulation` `CUI` `risk-based-inspection` `RBI` `mechanical-integrity` `non-intrusive-inspection` `pulsed-eddy-current` `guided-wave-inspection` `pipeline-integrity`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
