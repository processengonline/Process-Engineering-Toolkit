# Troubleshooting Guide: Electrostatic Coalescer — Declining Water Separation Efficiency

> **Category:** Separation Equipment / Oil Treating
> **Unit:** Electrostatic Coalescer (Free-Water Knockout / Desalter-Adjacent Treating), Crude/Oil Dehydration Service
> **Tools:** Electrical grid current/voltage trending, water-in-oil (BS&W) outlet trending, field inspection
> **Fluid Package:** Not applicable to the electrostatic separation mechanism itself — this is an electrical/physical separation performance issue, though upstream emulsion chemistry can be assessed as in Case Study 7
> **Symptom:** Outlet water-in-oil (BS&W) content gradually rising despite normal inlet water cut and normal chemical (demulsifier) dosing

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Outlet BS&W (water-in-oil) content trending up despite stable inlet water cut and unchanged demulsifier dosing |
| Initially unclear | Whether this was a chemistry-driven emulsion issue (as in Case Study 7) or a mechanical/electrical issue with the coalescer's separation mechanism itself |
| Actual root cause | A degraded electrical grid insulator was causing intermittent grid short-circuiting/arcing, reducing the effective electrostatic field strength available for water droplet coalescence |
| Fix | Replaced the degraded insulator; verified grid current/voltage returned to normal operating range |
| Diagnostic signal | Grid electrical current showed intermittent spikes/dropouts inconsistent with stable operation, while inlet water cut and demulsifier dosing both remained unchanged over the same period |
| Prevention | Routine grid electrical trending (current/voltage stability, not just average values); periodic insulator inspection |

---

## 2. Symptom

- **Outlet water-in-oil (BS&W) content gradually rose** at the coalescer outlet.
- **Inlet water cut remained stable**, and **demulsifier dosing was unchanged** — the parameters most associated with emulsion-driven separation problems (see Case Study 7) were both normal.

## 3. Why This Wasn't Assumed to Be an Emulsion/Chemistry Issue

Given the similarity to the three-phase separator emulsion case (Case Study 7), a chemistry-driven explanation (demulsifier dosing, emulsion stability) would be a reasonable first hypothesis for declining water separation performance. But here, both of the parameters that drove that earlier case — inlet water cut and demulsifier dosing — were confirmed stable, which meant the mechanism had to be different. An electrostatic coalescer's separation performance depends not just on chemistry but on its **electrical field strength**, a factor with no equivalent in a purely gravity/chemistry-based separator.

## 4. Diagnostic Approach

### Step 1 — Confirm inlet conditions and chemical dosing are unchanged
Inlet water cut and demulsifier dosing rate were reviewed and confirmed stable over the period the outlet BS&W had been rising — ruling out the chemistry-driven mechanism seen in Case Study 7.

### Step 2 — Review the coalescer's electrical grid performance
With chemistry ruled out, attention turned to the coalescer's **electrostatic grid** — its current and voltage were trended at high resolution (not just checked as instantaneous readings).

**Finding:** Grid current showed **intermittent spikes and dropouts** — inconsistent with the stable, steady electrical field the coalescer needs to maintain for effective droplet coalescence.

### Step 3 — Investigate the source of the electrical instability
The intermittent electrical behavior pointed toward a **grid insulator issue** — insulators are critical to maintaining the electrostatic field without short-circuiting to the vessel/ground. Field inspection confirmed a **degraded insulator**, causing intermittent short-circuiting/arcing.

### Step 4 — Connect reduced field strength to reduced separation performance
An intermittently short-circuiting grid does not maintain the **consistent electrostatic field strength** needed to promote water droplet coalescence and growth to a settleable size — directly explaining why more water droplets were passing through with the oil despite unchanged inlet conditions and chemistry.

### Quantitative Basis

- Design grid operation: 15 kV AC, steady current draw ~2.5 A. High-resolution trend showed current **spiking to 4.8 A and dropping to 0.3 A on an irregular ~90-second cycle** — but the *averaged* reading masked this, sitting at a normal-looking 2.3 A, which is why the fault wasn't caught by routine average-value monitoring.
- Outlet BS&W spec: ≤0.5 vol%. Baseline 0.3 vol%, rose to **1.4 vol%.**
- Inlet water cut held steady at **12%**, demulsifier dosing held steady at **20 ppm** — both independently confirmed unchanged over the same period, ruling out the Case Study 7-style chemistry mechanism.

## 5. Root Cause

**A degraded electrical grid insulator was causing intermittent short-circuiting/arcing within the coalescer**, reducing the effective, consistent electrostatic field strength available for water droplet coalescence. This reduced separation performance even though inlet water cut and demulsifier dosing — the parameters typically associated with emulsion-driven separation issues — remained unchanged.

## 6. Corrective Action

1. **Replaced the degraded insulator.**
2. **Verified grid current/voltage** returned to a stable operating range consistent with normal, uninterrupted electrostatic field generation.

## 7. Verification

- Post-repair grid current held steady at **2.4–2.6 A with no spikes or dropouts** over continuous high-resolution monitoring.
- Outlet BS&W returned to **0.28 vol%**, below the 0.5 vol% spec, and held there over the following **21 days.**

## 8. Prevention / Long-Term Fix

- Established **routine grid electrical trending focused on stability** (variance/intermittency), not just average current/voltage values, since an intermittent fault can hide within an acceptable-looking average reading.
- Added **periodic insulator inspection** to the maintenance plan.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Confirm inlet water cut and chemical (demulsifier) dosing are stable before assuming a chemistry-driven cause
- [ ] If chemistry/inlet conditions are ruled out, review the coalescer's **electrical grid current/voltage at high time resolution**, not just instantaneous or averaged readings
- [ ] Look specifically for intermittent spikes/dropouts, which can hide within a normal-looking average
- [ ] If electrical instability is found, inspect grid insulators for degradation, fouling, or damage causing intermittent short-circuiting
- [ ] Replace/repair the affected insulator(s)
- [ ] Confirm both electrical stability AND outlet BS&W recovery, since electrical stability alone doesn't guarantee separation performance has actually recovered
- [ ] Establish routine electrical stability trending (not just average value monitoring) and periodic insulator inspection

## 10. Key Takeaway

> Electrostatic coalescer performance depends on maintaining a stable electric field, not just on emulsion chemistry — declining water separation with stable inlet water cut and unchanged demulsifier dosing should point you toward the grid's electrical performance, not toward chemistry. And when checking that electrical performance, look at stability (intermittent spikes/dropouts) rather than just average current/voltage, since an intermittent short-circuit can easily hide inside an average reading that looks perfectly normal.

---

## Related Concepts / Tags

`electrostatic-coalescer` `water-in-oil` `BS&W` `electrostatic-grid` `insulator-degradation` `crude-dehydration` `desalter-adjacent` `oil-treating`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
