# Troubleshooting Guide: Centrifugal Compressor — Anti-Surge Control Nuisance Surge Events

> **Category:** Rotating Equipment / Compressor Control
> **Unit:** Centrifugal Gas Compressor with Anti-Surge Control System
> **Tools:** Compressor performance map overlay against actual operating trend data
> **Fluid Package:** Peng-Robinson (PR), used to calculate actual gas molecular weight/compressibility for accurate surge line positioning on the compressor map
> **Symptom:** Compressor experiencing surge events (audible banging, flow/pressure reversal) at flow rates that should be well clear of the surge line

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Repeated surge events at flow conditions that appeared, per the control system, to be within the safe operating envelope |
| Initially unclear | Whether the anti-surge valve/controller was malfunctioning, or the surge line itself was positioned incorrectly for current conditions |
| Actual root cause | Gas composition had drifted from the original design basis (lighter average molecular weight), shifting the true surge line without the anti-surge controller's reference curve being updated |
| Fix | Recalculated and updated the surge control line/margin in the anti-surge controller using current gas composition |
| Diagnostic signal | Actual compressor operating points, when re-plotted using current gas properties (via PR), fell much closer to the true surge line than the controller's stored reference indicated |
| Prevention | Periodic gas composition review triggering surge line reverification; alarm on molecular weight deviation from the surge-map design basis |

---

## 2. Symptom

- **Repeated surge events** — audible banging/flow reversal — occurring at flow rates the anti-surge control system indicated were within the safe operating region.
- No obvious anti-surge valve mechanical fault (stroke tests normal).

## 3. Why This Wasn't Assumed to Be a Simple Valve/Controller Malfunction

Surge events with an active anti-surge system in place are most often blamed on the anti-surge valve or controller itself (slow response, calibration drift, valve sticking). But if the valve and controller were both confirmed to be functioning and responding correctly according to their programmed surge line, the real question became: **is the programmed surge line itself still correct for current operating conditions?** A surge line is only valid for the gas composition/molecular weight it was calculated against — if that has changed, the controller can be working perfectly and still let the compressor surge.

## 4. Diagnostic Approach

### Step 1 — Verify anti-surge valve and controller function
Stroke tests and response checks on the anti-surge valve and controller confirmed both were operating and responding as programmed — ruling out a straightforward mechanical/controller fault.

### Step 2 — Review current gas composition against the original surge map design basis
Current gas composition data was compared against the composition/molecular weight assumed when the compressor's surge control line was originally calculated and programmed.

**Finding:** Gas molecular weight had drifted **lighter** than the original design basis (a common consequence of upstream production mix changes over the life of a field/facility).

### Step 3 — Recalculate the true surge line using current gas properties
Using **PR** to establish accurate current gas compressibility and molecular weight, the compressor performance map and surge line were recalculated for the actual current gas composition.

### Step 4 — Compare actual operating points to the recalculated surge line
When actual compressor operating points were re-plotted against the **recalculated** surge line (rather than the outdated stored reference), they fell **much closer to the true surge boundary** than the controller's existing programmed margin reflected — explaining why surge was occurring at flows the outdated reference considered safe.

### Quantitative Basis

- Original design gas: MW = 19.6 lb/lbmol (basis for the programmed surge line). Current GC sample: **MW = 16.4 lb/lbmol — 16.3% lighter.**
- At current operating conditions (suction 410 psig, discharge 780 psig, 9,800 rpm), the controller's stored surge line (10% margin) placed the recycle trip point at **12,300 ACFM**.
- Recalculating the surge line with PR using the actual MW = 16.4 gas raised the true minimum stable flow to **13,650 ACFM** at the same head — lighter gas requires higher volumetric flow to avoid stall for the same polytropic head.
- Logged surge events occurred at **12,800–13,100 ACFM** — above the controller's outdated 12,300 ACFM trip point (so the control system saw no reason to act) but still below the true 13,650 ACFM surge boundary for the actual gas.

## 5. Root Cause

**Gas composition had drifted to a lighter average molecular weight than the original design basis**, which shifted the compressor's true surge line. The anti-surge controller was still operating against its **original, now-outdated** surge reference curve, so it was allowing operation at flow/head combinations that were actually inside the true (shifted) surge region for the current gas.

## 6. Corrective Action

1. Recalculated the surge control line and appropriate surge margin using current gas composition.
2. Updated the anti-surge controller's reference curve/setpoints accordingly.

## 7. Verification

- New trip setpoint (10% margin over the recalculated 13,650 ACFM true surge line) reprogrammed to **15,000 ACFM**.
- Sustained operation confirmed at **16,200 ACFM average**, restoring an effective surge margin of ~11% — consistent with the original design intent.
- **No surge events logged over the following 45 days**, spanning the same range of loads and suction/discharge pressures at which the original events occurred.

## 8. Prevention / Long-Term Fix

- Established **periodic gas composition review** specifically tied to surge line validity, not just general process monitoring.
- Added an **alarm on molecular weight deviation** from the surge-map design basis, prompting proactive surge line reverification before a surge event occurs rather than after.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Verify anti-surge valve and controller function via stroke test/response check before suspecting the surge line itself
- [ ] Compare current gas composition/molecular weight against the design basis used for the original surge map
- [ ] If composition has drifted, recalculate the compressor performance map and surge line using current gas properties
- [ ] Re-plot actual operating history against the recalculated (not the original) surge line to confirm the mismatch
- [ ] Update the anti-surge controller's reference curve/margin to reflect current gas composition
- [ ] Add a standing check (e.g., molecular weight deviation alarm) to catch future composition drift before it causes a surge event
- [ ] Recognize that a functioning anti-surge system is only as accurate as the surge line it was programmed against — it does not self-correct for composition changes

## 10. Key Takeaway

> An anti-surge controller doesn't know when the gas composition has changed — it only knows the surge line it was originally programmed with. If a compressor with a working, correctly-responding anti-surge system is still surging, check whether the gas itself has drifted from the design basis before troubleshooting the control hardware. A surge line calculated years ago for a different gas composition can quietly become unsafe long before anyone notices, unless composition is actively tracked against it.

---

## Related Concepts / Tags

`centrifugal-compressor` `anti-surge-control` `surge-line` `molecular-weight-drift` `compressor-map` `Peng-Robinson` `gas-composition` `surge-margin`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
