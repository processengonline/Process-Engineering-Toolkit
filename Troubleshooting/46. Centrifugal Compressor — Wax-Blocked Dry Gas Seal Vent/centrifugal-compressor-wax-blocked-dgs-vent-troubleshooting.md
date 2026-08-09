# Troubleshooting Guide: Centrifugal Compressor — Wax-Blocked Dry Gas Seal Vent Causing Temperature Trip

> **Category:** Rotating Equipment / Dry Gas Seal Systems / Flow Assurance
> **Unit:** Centrifugal Gas Compressor — Dry Gas Seal (DGS) system, Non-Drive-End (NDE) primary vent line
> **Tools:** Compressor performance trending (suction/discharge pressure, load) + PVT-based Wax Appearance Temperature (WAT) analysis
> **Fluid Package:** Peng-Robinson (PR) for compressor gas-phase performance; a dedicated wax-modeling package (e.g., Multiflash Wax model or similar solid-liquid-equilibrium add-on) for WAT/wax precipitation prediction
> **Symptom:** Gradual NDE dry gas seal housing temperature rise, culminating in a high-temperature trip, with all other machine parameters normal

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Compressor tripped on high NDE dry gas seal housing temperature; temperature had crept up gradually beforehand |
| Initially unclear | Whether the rising seal temperature originated from the compressor itself or from the auxiliary seal gas system |
| Actual root cause | Wax (paraffin) deposits partially blocking the primary vent line — pipe wall temperature dropped below the Wax Appearance Temperature (WAT) due to ambient cooling, even though bulk gas stayed above WAT |
| Fix | Isolate compressor, mechanically clean the vent line, restart |
| Diagnostic signal | Compressor performance stayed at design point (ruling out internal cause); primary vent pressure showed a slow, steady increase correlating with the temperature rise |
| Prevention | Periodic vent-line inspections; improved heat tracing and insulation; WAT assessments added to seasonal operating reviews |

---

## 2. Symptom

- Compressor **tripped on a high NDE dry gas seal housing temperature alarm**.
- In the hours before the trip, **seal housing temperature crept up gradually** — not a sudden spike, which is diagnostically significant (see Section 3).
- **Suction pressure, discharge pressure, and bearing temperatures all stayed within normal limits.**
- **No notable vibration or lubrication issues.**

## 3. Why This Wasn't an Obvious Mechanical Call

A gradual seal temperature rise with every other compressor parameter normal creates a genuine fork in the investigation:

1. **The compressor itself** — e.g., an internal mechanical or performance issue generating extra heat near the seal.
2. **The auxiliary seal gas system** — e.g., the dry gas seal's own support system (seal gas supply, vent path) failing to remove heat properly, independent of anything wrong with the compressor's core performance.

These point to completely different response teams and repair scopes, so the first priority was determining **which side of that boundary** the problem was on — using trend data to test the "compressor itself" hypothesis before escalating further.

## 4. Diagnostic Approach

### Step 1 — Review compressor performance trends
Trends reviewed included:
- Suction/discharge pressure
- Load
- Seal gas differential pressure
- Dry gas seal vent pressure
- NDE housing temperature

**Finding:** **Compressor performance stayed close to its design point** — suction/discharge pressure and load showed nothing abnormal. This **ruled out an internal compressor problem** as the driver and shifted focus toward the auxiliary seal gas/vent system.

> **This is the same core move used in the reciprocating compressor case (Case Study 2):** build/consult a performance reference, confirm the machine is behaving as designed, and let that result redirect the investigation — here, toward the seal support system rather than toward a mechanical inspection of the compressor itself.

### Step 2 — Correlate the temperature rise with vent pressure trend
The gradual seal housing temperature rise was correlated against the vent-side data and found to track a **slow but steady increase in primary vent pressure** — a strong indicator of a developing **restriction in the vent line** rather than an upstream process condition.

### Step 3 — Confirm physically
**Field inspection confirmed wax deposits partially blocking the primary vent.**

### Step 4 — Explain the wax formation using PVT/WAT analysis
To understand *why* wax was forming here specifically, gas composition was checked against **laboratory PVT data**:

```
Gas composition:        rich in paraffinic hydrocarbons
Bulk gas temperature:   above Wax Appearance Temperature (WAT)  →  no wax expected in bulk flow
Vent pipe wall temp:    exposed to cooler ambient conditions  →  dropped BELOW WAT
```

> **Why a plain cubic EOS wasn't enough here either:** As in the hydrate case (Case Study 5), **Peng-Robinson handles the bulk gas-phase performance correctly, but wax/paraffin crystallization is a solid-liquid equilibrium phenomenon that a standard cubic EOS does not predict on its own.** A dedicated wax-modeling package (e.g., a Multiflash Wax model or equivalent solid-phase add-on) is needed to calculate the Wax Appearance Temperature and confirm where in the system conditions cross below it.

**Interpretation:** Even though the **bulk gas** was warm enough to stay above WAT, the **vent piping itself** was locally cooled by ambient exposure, dropping the **pipe wall temperature** — not the bulk gas temperature — below WAT. This is a **localized, wall-temperature-driven** phenomenon, which is why it wasn't visible in the bulk process temperature trends and only showed up as a slowly developing restriction.

### Quantitative Basis

- Gas: paraffinic condensate-associated gas, average MW ≈ 22; WAT (Multiflash-type wax model) calculated at **46°F** at the vent's operating pressure (145 psig).
- Bulk gas temperature: 95°F — well above WAT, confirming no bulk-flow wax risk.
- Vent pipe wall temperature estimate (ambient heat-loss calc, h_amb ≈ 3 Btu/hr·ft²·°F, ambient air 28°F): **41°F — 5°F below WAT**, despite the bulk gas remaining warm.
- Primary vent pressure rose from a 12 psig baseline to 34 psig over the 11 hours preceding the trip.
- NDE seal housing temperature rose from 148°F to 231°F against a 225°F trip setpoint.

## 5. Root Cause

**Paraffin wax crystallized on the internal wall of the primary DGS vent line** because the **pipe wall temperature** (cooled by ambient exposure) dropped below the gas's **Wax Appearance Temperature**, even though the bulk gas itself remained above WAT. The resulting wax buildup **progressively restricted the vent**, allowing heat to accumulate around the seal housing until the protection system tripped the machine on high temperature.

## 6. Corrective Action

1. **Isolated the compressor.**
2. **Mechanically cleaned the vent line** to remove wax deposits.
3. **Restarted** the machine.

## 7. Verification

- Vent pressure returned to **12-14 psig**, close to the pre-event baseline.
- NDE seal housing temperature held at **145-152°F**, versus the 231°F peak reached at the trip event and the 225°F setpoint.
- **No further trips over the following 60 days**, including across two subsequent cold snaps that tested the improved heat tracing.

## 8. Prevention / Long-Term Fix

- **Periodic vent-line inspections** implemented.
- **Improved heat tracing and insulation** added to the exposed piping, directly targeting the mechanism (pipe wall cooling below WAT) rather than just the symptom.
- **WAT assessments added to seasonal operating reviews**, so wax risk is **reassessed as ambient conditions change** — recognizing that this is a seasonally variable risk, not a one-time design check.

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for future dry gas seal housing temperature excursions/trips:

- [ ] Confirm whether the temperature rise was gradual (favors a developing restriction/fouling mechanism) or sudden (favors an instrumentation fault or abrupt mechanical event)
- [ ] Review core compressor performance trends (suction/discharge pressure, load) — confirm whether the machine is at its design point before suspecting an internal compressor issue
- [ ] If compressor performance is normal, shift focus to the **seal gas/vent auxiliary system** specifically
- [ ] Review seal gas differential pressure and **vent pressure trends** for a slow, steady change that could indicate a developing restriction
- [ ] If vent pressure is trending up, request a **field inspection of the vent line** for physical blockage
- [ ] If a wax/deposit blockage is found (or suspected) in gas service, check gas composition against **laboratory PVT data** and calculate the **Wax Appearance Temperature (WAT)**
- [ ] Don't rely on bulk gas temperature alone — check whether **pipe wall temperature** (influenced by ambient exposure, insulation, heat tracing) could be locally below WAT even when the bulk gas is not
- [ ] After clearing a blockage, verify both **vent pressure and seal housing temperature** return to normal, not just that the trip alarm has cleared
- [ ] Add heat tracing/insulation review and periodic vent-line inspection to the maintenance plan for any vent/drain piping exposed to ambient cooling in waxy/paraffinic gas service
- [ ] Reassess WAT risk **seasonally**, since ambient temperature — not just gas composition — determines whether wax risk exists at a given point in the piping

## 10. Key Takeaway

> When a machine's core performance stays at design point but a localized temperature keeps climbing, look at the **support/auxiliary system**, not the machine internals — and remember that solid-phase phenomena like wax (or hydrates, see Case Study 5) can form based on **local wall temperature**, not bulk process temperature. A vent line can sit well below the bulk gas's wax appearance temperature simply because it's exposed to ambient air, even when every other process indicator looks completely normal. If your gas is paraffinic, treat exposed, poorly-insulated piping as a standing wax risk that changes with the seasons — not a one-time design check.

---

## Related Concepts / Tags

`centrifugal-compressor` `dry-gas-seal` `DGS-vent` `wax-deposition` `paraffin` `wax-appearance-temperature` `WAT` `PVT-analysis` `Peng-Robinson` `Multiflash` `heat-tracing` `flow-assurance` `seasonal-operating-review` `compressor-performance-trending`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying.*
