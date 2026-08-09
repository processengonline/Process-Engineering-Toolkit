# Troubleshooting Guide: Produced Water Hydrocyclone — Declining Oil-in-Water Separation Efficiency

> **Category:** Produced Water Treatment / Physical Separation
> **Unit:** Deoiling Hydrocyclone Train, Produced Water Treatment System
> **Tools:** Hydrocyclone performance review — pressure drop ratio (PDR) vs. separation efficiency correlation
> **Fluid Package:** Not applicable — hydrocyclone performance is governed by droplet-size/centrifugal separation correlations, not phase-equilibrium thermodynamics
> **Symptom:** Oil-in-water content at the hydrocyclone outlet trending upward, risking the discharge permit limit

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Oil-in-water (OiW) content at hydrocyclone outlet trending up toward the discharge permit limit |
| Initially unclear | Feed characteristic change (droplet size, oil concentration) vs. an equipment/hydraulic issue within the hydrocyclones |
| Actual root cause | Reduced pressure drop ratio (PDR) across the hydrocyclones caused by a partially plugged underflow orifice and a malfunctioning control valve, disrupting the reject/split ratio and allowing more oil droplets to escape with the treated water |
| Fix | Cleaned/replaced the underflow orifice; corrected the control valve; restored design PDR |
| Diagnostic signal | PDR trending below its design range despite stable inlet feed conditions |
| Prevention | Routine PDR trending with alarm; routine underflow orifice/valve inspection |

---

## 2. Symptom

- **Oil-in-water content at the hydrocyclone outlet trending upward**, approaching or risking exceedance of the environmental discharge permit limit.

## 3. Why This Wasn't Assumed to Be a Feed-Quality Issue

Deoiling hydrocyclone performance is sensitive to inlet oil droplet size distribution and concentration — a genuine feed-quality change (e.g., from upstream process upsets, chemical injection changes, or emulsified oil) is a very plausible first suspect. But hydrocyclones are also **hydraulically tuned devices** — their separation performance depends heavily on maintaining a specific split (reject) ratio, governed by the **pressure drop ratio** across the unit. Before assuming a feed-side cause, it was necessary to check whether the hydrocyclones themselves were still operating at their design hydraulic point.

## 4. Diagnostic Approach

### Step 1 — Check inlet feed conditions
Feed oil concentration and general process conditions upstream were reviewed and found reasonably stable — not pointing to an obvious feed-quality driven cause.

### Step 2 — Review hydrocyclone pressure drop ratio (PDR) trend
The **pressure drop ratio** (a key hydrocyclone operating parameter relating reject-side and overflow-side pressure drops) was trended and found to have **drifted below its design range**.

```
PDR too low  →  insufficient reject flow/split ratio  →  reduced centrifugal separation efficiency
                →  more oil droplets escape with the treated (overflow) water
```

**Interpretation:** A PDR outside the design band directly correlates with reduced separation efficiency in hydrocyclone performance curves — this pointed the investigation toward the reject-side hydraulics rather than the feed.

### Step 3 — Inspect the reject-side hardware
With PDR identified as the deviation, the reject-side flow path was inspected, including the **underflow orifice** and its associated **control valve**.

### Step 4 — Confirm the physical restriction/malfunction
Inspection found the **underflow orifice partially plugged** and the **control valve malfunctioning**, both of which would disrupt the intended reject flow rate and therefore the pressure drop ratio.

### Quantitative Basis

- Discharge permit limit: OiW ≤ 29 mg/L. Baseline 12 mg/L, rose to **41 mg/L** — above the permit limit.
- Design PDR range: 2.5–3.0. Trended actual PDR dropped to **1.6**, well below the design band.
- Underflow orifice: design opening 0.375 in (3/8 in); inspection found it **~60% plugged with scale, reducing effective opening to ≈0.24 in.**
- Reject flow: design target 8% of total feed; actual measured only **3.1% of feed** at the degraded PDR — less than half the intended split.

## 5. Root Cause

**A partially plugged underflow orifice combined with a malfunctioning reject-side control valve disrupted the hydrocyclone's pressure drop ratio**, moving it outside its design operating band. This reduced the effective split/reject ratio and centrifugal separation efficiency, allowing more oil droplets to escape with the treated water and driving up outlet oil-in-water content.

## 6. Corrective Action

1. **Cleaned/replaced the underflow orifice.**
2. **Corrected the malfunctioning control valve.**
3. Restored the pressure drop ratio to its design range.

## 7. Verification

- PDR restored to **2.7**, within the 2.5–3.0 design range.
- Reject flow returned to **7.8% of feed**, close to the 8% design target.
- Outlet OiW content dropped to **14 mg/L**, within the 29 mg/L permit limit, and held there over the following **21 days.**

## 8. Prevention / Long-Term Fix

- Established **routine PDR trending with an alarm** for deviation outside the design band — an early, hydraulics-based indicator rather than waiting for the OiW analyzer to show a problem.
- Added **routine inspection of the underflow orifice and reject control valve** to the maintenance plan.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm feed oil concentration and general upstream process conditions before assuming a feed-quality cause
- [ ] Review the **pressure drop ratio (PDR)** trend against the hydrocyclone's design operating band
- [ ] If PDR has drifted, inspect the reject-side flow path: underflow orifice, reject control valve, and associated instrumentation
- [ ] Correct any physical restriction (plugging, scale, debris) or valve malfunction found
- [ ] After correction, confirm both PDR **and** outlet oil-in-water content return to design/permit-compliant values
- [ ] Add PDR trending and alarming as a standing operational check, since it's a leading indicator that moves before the OiW analyzer shows a permit-risk trend
- [ ] Include the underflow orifice and reject valve in routine preventive maintenance, since these small components have an outsized effect on separation performance

## 10. Key Takeaway

> Hydrocyclone separation efficiency isn't just a function of what's coming in — it depends on maintaining the correct **hydraulic split** across the unit. Before chasing a feed-quality explanation for declining oil-in-water performance, check the pressure drop ratio: if it's out of its design band, look at the reject-side hardware (orifice, control valve) first. A small mechanical restriction on the reject side can silently degrade separation efficiency well before it shows up as an obvious equipment fault.

---

## Related Concepts / Tags

`hydrocyclone` `produced-water` `deoiling` `oil-in-water` `pressure-drop-ratio` `PDR` `underflow-orifice` `discharge-permit` `centrifugal-separation` `water-treatment`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
