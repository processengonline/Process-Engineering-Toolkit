# Troubleshooting Guide: Gas Engine Generator — Detonation from Fuel Gas Wobbe Index Shift

> **Category:** Rotating Equipment / Combustion & Fuel Gas Quality
> **Unit:** Gas-Fueled Reciprocating Engine-Generator (Genset), Field Gas Fuel
> **Tools:** Fuel gas composition trending, Methane Number (MN) / Wobbe Index calculation
> **Fluid Package:** PR for fuel gas bulk properties, combined with a Methane Number correlation (AVL/CARB-style) — a plain PR flash does not itself output a knock-resistance metric
> **Symptom:** Increasing knock sensor trips and engine power derating, with ignition timing and spark plugs confirmed normal

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Knock sensor trips increasing in frequency; engine automatically derating load to avoid detonation |
| Initially unclear | Ignition system fault (timing, plugs) vs. a fuel gas quality change reducing knock resistance |
| Actual root cause | Upstream fuel gas conditioning skid separator temperature had drifted warmer, allowing heavier C3+ components to remain in the vapor fuel stream and lowering Methane Number below the engine's minimum requirement |
| Fix | Corrected separator temperature; added fuel gas coalescing filtration ahead of the engine |
| Diagnostic signal | Fuel gas composition trend showed Methane Number dropping from a 80 design value to as low as 62 during specific periods, correlating with knock trip events |
| Prevention | Continuous online Wobbe Index/Methane Number analyzer with alarm, tied directly into the engine's automatic derate logic |

---

## 2. Symptom

- **Knock sensor trips increased in frequency**, forcing the engine control system to **automatically derate load** to stay clear of detonation.
- No obvious mechanical trigger — this wasn't correlated with a specific load step or ambient condition on its own.

## 3. Why This Wasn't Assumed to Be an Ignition System Problem

Detonation/knock in a gas engine is most commonly traced to ignition timing drift, worn spark plugs, or excessive compression from carbon buildup — all mechanical/ignition-side explanations. But engine knock resistance also depends entirely on **fuel gas quality**, specifically its Methane Number (an octane-equivalent metric for gaseous fuels). Before assuming an ignition fault, it was necessary to check whether the fuel itself had changed, since field/associated gas composition can vary significantly with upstream separation performance.

## 4. Diagnostic Approach

### Step 1 — Check ignition system parameters
Ignition timing, spark plug condition, and compression were checked and found within normal spec — ruling out the most common mechanical explanation.

### Step 2 — Review fuel gas composition trend
Fuel gas composition data (from the engine skid's gas chromatograph) was reviewed over the period knock events occurred.

**Finding:** Heavier hydrocarbon content (C3+) in the fuel gas had **increased periodically**, correlating with the timing of knock events.

### Step 3 — Calculate Methane Number from actual composition
Using the actual composition trend, **Methane Number** was calculated via the standard AVL/CARB-style correlation for each period.

### Step 4 — Trace the compositional shift upstream
With MN confirmed as the driver, the investigation moved to the **fuel gas conditioning skid**, specifically the separator responsible for knocking heavier components out of the vapor fuel stream before it reaches the engine.

### Quantitative Basis

- Engine minimum Methane Number requirement: 75. Design/baseline fuel gas MN: **80.**
- During knock-event periods, calculated MN dropped as low as **62 — 18 points below the minimum requirement.**
- Fuel gas C3+ content rose from a baseline **2.1 mol% to 9.4 mol%** during these periods.
- Separator operating temperature, reviewed against the compositional shift, had drifted from a design 95°F to **118°F** — warm enough to leave significantly more C3+ in the vapor phase rather than knocking it out to the liquid phase.

## 5. Root Cause

**The fuel gas conditioning skid separator had drifted to a warmer-than-design operating temperature**, allowing more C3+ hydrocarbons to remain in the vapor fuel gas stream rather than being separated to liquid. This lowered the fuel's Methane Number below the engine's minimum requirement during affected periods, reducing knock resistance and triggering the knock sensor's protective derate response.

## 6. Corrective Action

1. **Corrected the fuel gas conditioning skid separator temperature** back to its design value.
2. **Added fuel gas coalescing filtration** ahead of the engine as an additional layer of protection against heavy-end carryover.
3. Adjusted ignition timing conservatively as a temporary compensation during the investigation period.

## 7. Verification

- Separator temperature restored to **96°F**, within 1°F of the 95°F design value.
- Fuel gas Methane Number held at **79-81** over the following **30 days**, consistently above the 75 minimum requirement.
- Knock sensor trips dropped to **zero over the same 30-day period**, and the engine returned to full rated load without derating.

## 8. Prevention / Long-Term Fix

- Installed a **continuous online Wobbe Index/Methane Number analyzer**, with an alarm set at MN 78 (a margin above the 75 engine minimum) tied directly into the engine control system's automatic derate logic — allowing the engine to respond to fuel quality changes proactively rather than only after a knock event.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Check ignition system parameters (timing, spark plugs, compression) first — rule out the most common mechanical cause
- [ ] Review fuel gas composition trend over the period of knock events, specifically C3+ content
- [ ] Calculate Methane Number from actual composition and compare against the engine's minimum requirement
- [ ] If MN has dropped, trace the compositional shift upstream to the fuel gas conditioning system (separator temperature/pressure)
- [ ] Correct the upstream conditioning issue rather than only adjusting ignition timing as a permanent fix
- [ ] Verify both separator temperature recovery AND fuel gas MN recovery, not just that knock trips have stopped
- [ ] Install continuous online Wobbe/MN monitoring tied to engine protection logic for ongoing fuel quality assurance

## 10. Key Takeaway

> Engine knock isn't always an ignition-side problem — fuel gas quality, specifically Methane Number, is just as often the actual driver, especially on field/associated gas where upstream separator performance can shift the fuel composition significantly. Before adjusting ignition timing or replacing plugs, check whether the fuel itself has gotten heavier; a warm upstream separator can quietly rob knock resistance well before anyone thinks to check fuel gas composition.

---

## Related Concepts / Tags

`gas-engine` `genset` `detonation` `knock` `methane-number` `wobbe-index` `fuel-gas-quality` `fuel-gas-conditioning` `Peng-Robinson` `combustion`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
