# Troubleshooting Guide: Gas Filter Separator — Hydrate Blockage

> **Category:** Flow Assurance / Gas Gathering & Separation
> **Unit:** Gas Filter Separator (upstream/midstream gas gathering line)
> **Tools:** VLE + hydrate stability modeling (specific software not documented in original case notes — commonly the Hydrate utility in Aspen HYSYS/UniSim, or Multiflash)
> **Fluid Package:** Peng-Robinson (PR) for bulk gas VLE + a hydrate-specific model (e.g., CSMHYD-based Hydrate utility in HYSYS, or CPA in Multiflash)
> **Symptom:** Steadily declining gas flow with stable upstream pressure, rising differential pressure, and occasional vibration

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Gas flow steadily declining; upstream pressure stable; rising differential pressure across the separator; occasional vibration |
| Initially unclear | Mechanical fouling vs. process condition vs. something else entirely restricting flow |
| Actual root cause | Separator operating temperature had moved into the **hydrate stability region**, allowing free water + hydrocarbon gas to form solid hydrate crystals that accumulated on the filter elements |
| Fix | Raised gas temperature above the hydrate formation threshold; cleared accumulated hydrates |
| Diagnostic tool | Combined VLE + hydrate stability study using actual gas composition and operating pressure |
| Prevention | Reviewed methanol/MEG injection strategy for future low-temperature operation |

---

## 2. Symptom

- **Gas flow steadily declining** through the filter separator.
- **Upstream pressure remained stable** — ruling out a supply-side cause.
- **Rising differential pressure (dP)** across the separator — classic signature of something physically restricting flow area.
- **Occasional vibration** — consistent with partial/uneven blockage disturbing flow distribution.

## 3. Why This Wasn't an Obvious Mechanical Call

Rising differential pressure with declining flow is the textbook signature of **filter element fouling/plugging** — the natural first assumption. But before committing to that (and the associated shutdown to inspect/replace elements), it was worth asking: **what could be depositing on the filter, and why now?** Stable upstream pressure meant the driving force hadn't changed, so the restriction had to be developing *inside* the separator itself — which could be:

1. **Mechanical fouling** — solids, scale, or debris progressively plugging the filter elements.
2. **A process condition** — something in the gas/liquid system itself changing state and depositing (e.g., hydrates, wax, salt).
3. Something else entirely.

Given the gas gathering service and the possibility of free water in the stream, **hydrate formation** was a strong candidate worth checking quantitatively before assuming purely mechanical fouling.

## 4. Diagnostic Approach

### Step 1 — Run a combined VLE + hydrate stability study
Using the **actual gas composition** and **actual operating pressure**, a hydrate formation study was performed combining:
- **Vapor–liquid equilibrium (VLE)** analysis of the bulk gas
- **Hydrate stability prediction**

> **Why a plain cubic EOS isn't enough:** Peng-Robinson (or SRK) handles the bulk hydrocarbon gas VLE correctly, but **a plain cubic EOS alone will not predict hydrate formation**. Hydrate prediction requires a dedicated add-on module — e.g., the **CSMHYD-based Hydrate utility in Aspen HYSYS/UniSim**, or a **CPA (Cubic-Plus-Association)** approach in tools like Multiflash — layered on top of the bulk VLE model. This is the same principle seen in the TEG dehydration and desalter cases: match the modeling tool to the specific physics/chemistry in question, not just the general phase behavior.

### Step 2 — Compare operating temperature to the hydrate stability envelope
The study showed that the **separator's actual operating temperature had moved into the hydrate stability region** for the given gas composition and pressure — meaning conditions were thermodynamically favorable for hydrate formation, not just theoretically possible.

```
If:  operating temperature < hydrate formation temperature (at operating pressure)
And: free water is present in the gas stream
Then: solid hydrate crystals can form and accumulate
```

### Step 3 — Connect the mechanism to the physical symptom
With free water and hydrocarbon gas both present under hydrate-favorable conditions, **solid hydrate crystals would form and accumulate on the filter elements** — physically restricting flow area. This directly explains:
- Declining flow (restriction building over time)
- Rising differential pressure (classic response to a narrowing flow path)
- Occasional vibration (uneven/partial blockage disturbing flow)

### Step 4 — Confirm against field symptoms
The hydrate-formation diagnosis **matched the field symptoms exactly**, confirming this was a process/thermodynamic condition — not primarily mechanical fouling from solids or debris — even though the *symptom* (rising dP, declining flow) looked identical to a mechanical fouling case from the outside.

### Quantitative Basis

- Operating pressure: 950 psig. Hydrate formation temperature at this pressure and gas composition (per CSMHYD/Multiflash calc): **68°F.**
- Actual gas temperature at the separator had drifted to **61°F — 7°F below** the hydrate formation temperature, due to a colder ambient period combined with upstream Joule-Thomson cooling.
- Gas flow declined from a baseline **42 MMscfd to 31 MMscfd over 9 days — a 26% decline.**
- Differential pressure across the separator rose from a normal 3-5 psi to **28 psi** before flow loss became severe.

## 5. Root Cause

The separator's operating temperature had drifted into the **hydrate stability region** for the actual gas composition and pressure. With free water present, this allowed **hydrate crystals to form and progressively accumulate on the filter elements**, restricting flow area and driving up differential pressure.

## 6. Corrective Action

1. **Raised gas temperature above the hydrate formation threshold**, moving operating conditions out of the hydrate stability region.
2. **Cleared the accumulated hydrates** from the filter elements.
3. Restored normal flow and differential pressure.

## 7. Verification

- Gas temperature raised to **78°F — a 10°F margin above the 68°F hydrate formation temperature.**
- Following hydrate clearing, differential pressure returned to **4 psi**, and flow recovered to **41 MMscfd**, close to the 42 MMscfd baseline.
- Held stable over the following **21 days**, with no further vibration or flow decline.

## 8. Prevention / Long-Term Fix

- **Reviewed the methanol/MEG injection strategy** for future low-temperature operating scenarios, to provide hydrate inhibition proactively rather than relying solely on temperature management. Methanol injection rate was increased from **0.5 to 1.8 gal/MMscf** as a backup inhibition measure for future cold snaps.
- This addresses the underlying flow-assurance risk rather than just the single blockage event, reducing the chance of a repeat occurrence — and avoiding what could otherwise have escalated into a full flow-assurance failure (e.g., a hard blockage requiring depressurization/thawing).

---

## 9. General Troubleshooting Checklist (Reusable)

Use this checklist for future gas separator/filter declining-flow and rising-dP events:

- [ ] Confirm upstream pressure is stable (rules out a supply-side driving-force change)
- [ ] Note the symptom pattern: declining flow + rising differential pressure + intermittent vibration is consistent with **either** mechanical fouling **or** hydrate/solid deposition — don't assume mechanical by default
- [ ] Check for the presence of free water in the gas stream
- [ ] Gather actual gas composition and actual operating pressure/temperature
- [ ] Run a **VLE + hydrate stability study** (bulk EOS + hydrate-specific add-on module — not a plain cubic EOS alone)
- [ ] Compare actual operating temperature against the **hydrate formation temperature** at operating pressure for the given composition
- [ ] If operating conditions fall inside the hydrate stability region, treat hydrate accumulation as the likely mechanism before assuming mechanical fouling/debris
- [ ] Corrective options: raise temperature above the hydrate formation threshold, and/or review chemical inhibition (methanol/MEG) strategy
- [ ] After clearing, verify flow and dP return to normal, and confirm operating conditions are now outside the hydrate stability region going forward
- [ ] Build hydrate-risk checks into low-temperature/low-flow operating scenarios going forward, not just as a one-time incident response

## 10. Key Takeaway

> Rising differential pressure with declining flow doesn't automatically mean mechanical fouling — it means **something is restricting the flow path**, and process chemistry can produce that restriction just as effectively as solids or debris. Whenever free water and hydrocarbon gas coexist at low temperature and elevated pressure, check the **hydrate stability envelope** before committing to a mechanical-fouling diagnosis. A plain hydrocarbon EOS won't tell you this on its own — you need a hydrate-specific model layered on top.

---

## Related Concepts / Tags

`gas-filter-separator` `hydrate-blockage` `flow-assurance` `hydrate-stability` `VLE` `CSMHYD` `CPA` `cubic-plus-association` `methanol-injection` `MEG-injection` `Peng-Robinson` `HYSYS` `UniSim` `Multiflash` `differential-pressure`

---

*This guide is derived from a real field troubleshooting case. Values and thresholds shown are specific to the reported case and should be validated against your own unit's design basis before applying. Note: the specific simulation software used in the original case was not documented; the Hydrate utility in Aspen HYSYS/UniSim and Multiflash are cited as representative tools capable of this type of analysis.*
