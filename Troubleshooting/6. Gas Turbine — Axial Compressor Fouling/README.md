# Troubleshooting Guide: Gas Turbine — Axial Compressor Fouling Reducing Power Output

> **Category:** Rotating Equipment / Gas Turbine Performance
> **Unit:** Gas Turbine Driving Compressor/Generator, Axial Compressor Section
> **Tools:** Corrected-parameter performance trending (compressor efficiency vs. corrected speed/flow), inlet filtration differential pressure review
> **Fluid Package:** Not applicable — turbine/compressor performance is assessed via standard gas turbine corrected-parameter correlations, not a VLE flash
> **Symptom:** Gradual loss of output power at constant fuel flow, with rising compressor discharge temperature for a given load

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Output power gradually declining at constant fuel flow; compressor discharge temperature rising for a given load |
| Initially unclear | Whether the turbine (hot) section or the axial compressor (cold) section was degrading |
| Actual root cause | Inlet air filter media damage allowed fine particulate to pass through and foul the axial compressor blades, reducing compressor efficiency |
| Fix | Performed an online water wash to restore compressor efficiency; replaced the damaged filter media |
| Diagnostic signal | Corrected-parameter trending isolated the efficiency loss specifically to the compressor section, while turbine section corrected efficiency stayed normal |
| Prevention | Differential pressure trending across inlet filters; water wash scheduled from the corrected efficiency trend rather than a fixed calendar interval |

---

## 2. Symptom

- **Output power gradually declined** at constant fuel flow — the machine was producing less for the same energy input.
- **Compressor discharge temperature rose** for a given load, consistent with the compressor doing less useful work per unit of energy consumed compressing the air.

## 3. Why This Needed Corrected-Parameter Analysis, Not Just a Power Trend

Raw output power and raw temperatures are heavily influenced by ambient conditions (temperature, pressure, humidity) — a gas turbine naturally makes less power on a hot day than a cold one. Before concluding real degradation had occurred, it was necessary to normalize the data using standard **corrected-parameter** methodology (correcting for ambient conditions to a reference state), which also allows isolating **which section** — compressor or turbine — is responsible for any genuine efficiency loss.

## 4. Diagnostic Approach

### Step 1 — Correct performance data for ambient conditions
Output power, compressor discharge pressure/temperature, and turbine exhaust temperature were all corrected to a standard reference ambient condition, removing weather-driven variation from the trend.

### Step 2 — Trend corrected compressor efficiency and corrected turbine section efficiency separately
Corrected efficiency was calculated and trended for the **axial compressor section** and the **turbine (expander) section** independently.

**Finding:** **Corrected compressor efficiency had declined measurably**, while **corrected turbine section efficiency remained essentially unchanged** — isolating the degradation specifically to the compressor, not the hot section.

### Step 3 — Review inlet air filtration condition
With the compressor implicated, inlet air filtration — the compressor's first line of defense against particulate fouling — was reviewed, including differential pressure trend across the filter house.

**Finding:** Filter differential pressure showed an unusual pattern inconsistent with normal, gradual filter loading, prompting a physical inspection.

### Step 4 — Confirm the fouling mechanism
Physical inspection found **damaged filter media** (tears/gaps) allowing fine particulate to bypass effective filtration and deposit on the compressor's early blade stages — directly explaining the isolated compressor efficiency loss.

### Quantitative Basis

- Corrected compressor efficiency dropped from a clean-condition baseline of **85% to 76% — a 9-point loss** over 4 months, while corrected turbine section efficiency held at **91-92%** throughout (essentially unchanged from baseline).
- Corrected output power at reference ambient conditions declined from **24.5 MW to 21.8 MW — an 11% loss.**
- Inlet filter differential pressure trend showed a step increase inconsistent with gradual loading, followed by inspection confirming **filter media tears** allowing particulate bypass.

## 5. Root Cause

**Damaged inlet air filter media allowed fine particulate to bypass effective filtration and deposit on the axial compressor's early blade stages**, progressively fouling the airfoils and reducing compressor efficiency. Because the turbine (hot) section remained unaffected, the overall machine efficiency loss and reduced output power were isolated specifically to the compressor fouling mechanism.

## 6. Corrective Action

1. **Performed an online water wash** of the axial compressor to remove fouling deposits without a full shutdown.
2. **Replaced the damaged inlet filter media** to prevent continued particulate bypass.

## 7. Verification

- Following the water wash, corrected compressor efficiency recovered to **82%** — a partial but significant recovery from 76%, consistent with an online wash typically not achieving full offline-wash-level cleaning.
- Corrected output power recovered to **23.6 MW**, close to the 24.5 MW baseline.
- Filter differential pressure returned to a **normal, gradual-loading pattern** following media replacement, with no further step changes over the following **60 days.**

## 8. Prevention / Long-Term Fix

- Established **differential pressure trending across the inlet filters** as a standing check, watching specifically for pattern changes (not just absolute dP level) that could indicate media damage rather than normal loading.
- **Water wash scheduling is now tied to the corrected compressor efficiency trend**, rather than a fixed calendar interval, so cleaning happens when actually needed.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Correct raw performance data (power, temperatures) for ambient conditions before drawing conclusions about degradation
- [ ] Trend corrected compressor efficiency and corrected turbine section efficiency separately to isolate which section is degrading
- [ ] If compressor efficiency specifically has declined, review inlet air filtration differential pressure trend
- [ ] Watch for a filter dP pattern change (step change, unusual trend shape) rather than just absolute dP level, since this can indicate media damage rather than normal loading
- [ ] Physically inspect filter media if the dP pattern is inconsistent with normal gradual loading
- [ ] Perform an online water wash to recover compressor efficiency, recognizing this typically gives partial (not full) recovery compared to an offline wash
- [ ] Replace damaged filter media to prevent recurrence
- [ ] Tie future water wash scheduling to the corrected efficiency trend, not a fixed calendar interval

## 10. Key Takeaway

> Raw power and temperature trends on a gas turbine are dominated by ambient conditions — always correct to a reference state before concluding real degradation has occurred. Once corrected, trending compressor and turbine section efficiency separately tells you which half of the machine is actually degrading, which determines whether the fix is a water wash (compressor fouling) or a hot-section inspection (turbine degradation) — two very different maintenance actions that a raw power trend alone can't distinguish between.

---

## Related Concepts / Tags

`gas-turbine` `axial-compressor` `compressor-fouling` `corrected-parameters` `inlet-air-filtration` `water-wash` `turbine-performance` `power-output-decline`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*
