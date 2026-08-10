# Troubleshooting Guide: Gas Compressor Surge from Liquid Slugs Carried into Suction

> **Category:** Rotating Equipment / Multiphase Flow Interaction
> **Unit:** Centrifugal Gas Compressor, Suction Scrubber Upstream
> **Tools:** Suction scrubber level/carryover trend review, compressor surge event correlation, transient multiphase flow review (upstream pipeline)
> **Fluid Package:** PR, used for gas-phase compressor performance calculations; upstream multiphase behavior assessed via transient pipeline flow tools as needed (see Case Study 18)
> **Symptom:** Compressor surging intermittently, with surge events correlating to brief suction scrubber high-level excursions rather than any compressor-side parameter

---

## 1. Quick Reference

| Item | Detail |
|---|---|
| Reported symptom | Intermittent compressor surge events with no clear correlation to compressor suction/discharge pressure or load alone |
| Initially unclear | Whether surges originated from the compressor/anti-surge system itself or from an upstream liquid-handling issue |
| Actual root cause | Brief liquid slugs from the upstream pipeline periodically overwhelmed the suction scrubber's liquid handling capacity, causing momentary liquid carryover into the compressor suction, which disrupted gas density/molecular weight momentarily and triggered surge |
| Fix | Increased suction scrubber liquid handling margin (level control tuning and, where needed, mechanical modification); coordinated with pipeline operations on slug-prone flow regimes |
| Diagnostic signal | Surge event timestamps correlated precisely with brief suction scrubber high-level excursions, not with any compressor performance parameter in isolation |
| Prevention | Suction scrubber level trending tied to surge event log; use of transient pipeline slug prediction (as in Case Study 18) to anticipate high-liquid-carryover periods |

---

## 2. Symptom

- **Compressor surging intermittently**, without a clear correlation to compressor suction pressure, discharge pressure, or load individually.

## 3. Why This Wasn't Assumed to Be an Anti-Surge Control Issue

Compressor surge naturally draws attention to the compressor and its anti-surge control system first (see Case Study 19 for a case where that assumption was correct). Here, though, it was worth checking a different possibility: **surge can also be triggered by a sudden, brief disruption to the suction gas itself** — such as liquid carryover momentarily changing gas density/molecular weight at the compressor inlet — rather than by the compressor's control system misjudging its own operating point on a stable gas.

## 4. Diagnostic Approach

### Step 1 — Review compressor-side parameters at the moment of each surge event
Suction pressure, discharge pressure, and load were reviewed at each surge event and found to not, by themselves, explain the timing — surges occurred at a range of different load conditions, not a consistent operating point.

### Step 2 — Review upstream suction scrubber level trend
Suction scrubber liquid level was reviewed at high time resolution around each surge event.

**Finding:** Each surge event correlated precisely with a **brief suction scrubber high-level excursion** — a short-duration liquid level spike, not a sustained high-level condition.

### Step 3 — Investigate the source of the brief liquid level spikes
With the scrubber implicated, the upstream pipeline was reviewed for a source of intermittent liquid surges — consistent with the multiphase slugging mechanism described in the slug catcher case (Case Study 18), but here arriving in smaller volumes at a scrubber further downstream in the gas gathering system.

### Step 4 — Confirm the carryover mechanism
The brief high-level excursions were confirmed to be large/fast enough to periodically **exceed the scrubber's vapor-liquid disengagement capacity for that instant**, allowing a small amount of liquid to carry over into the compressor suction line. Even a small liquid carryover event can momentarily and significantly change the effective gas density/molecular weight the compressor sees, which can be enough to push the compressor's instantaneous operating point across its surge line.

### Quantitative Basis

- **9 surge events over 6 weeks**, each lasting only **15–40 seconds** — too brief to be explained by a sustained operating point shift.
- Scrubber level normally runs 30–50%; during each surge event, level spiked to **88–95% for 20–45 seconds** before receding, tracking the surge event timing to within the trend logger's resolution.
- Scrubber liquid handling was sized for 15 gpm continuous; the brief spikes were back-calculated (from level rate-of-rise) at an estimated **60–90 gpm instantaneous slug rate** — 4–6x design.
- Normal suction gas MW is 19.2. The estimated momentary liquid carryover (droplet entrainment equivalent to an ~8% liquid volume fraction) was sufficient to shift the compressor's effective inlet flow reading by an estimated **12%**, enough to cross the programmed surge control line.

## 5. Root Cause

**Brief liquid slugs arriving from the upstream pipeline periodically exceeded the suction scrubber's liquid handling/disengagement capacity for short durations**, causing momentary liquid carryover into the compressor suction. This transient change in suction gas properties was sufficient to trigger compressor surge, even though sustained suction/discharge pressure and load conditions looked normal.

## 6. Corrective Action

1. **Increased suction scrubber liquid handling margin** — through level control tuning improvements and, where necessary, mechanical modification to improve disengagement capacity for brief high-liquid-rate events.
2. **Coordinated with pipeline operations** regarding flow regimes/rates known to be more prone to generating these liquid slugs, informing operational awareness even where the pipeline hydraulics themselves weren't immediately changed.

## 7. Verification

- Scrubber mesh pad upgrade increased design liquid handling capacity from **15 to 35 gpm**; level control response was also tuned tighter.
- Surge events dropped from **9 in 6 weeks to 1 in the following 12 weeks.**
- The single remaining event correlated with a slug **roughly twice the size of any previously recorded event**, confirming the mechanism and setting the basis for a follow-up review of the upstream pipeline's slugging behavior at high flow.

## 8. Prevention / Long-Term Fix

- Established **suction scrubber level trending tied to the surge event log**, so any future surge can be immediately checked against scrubber behavior as a first diagnostic step.
- Where applicable, used **transient pipeline slug prediction** (the same technique as Case Study 18) to anticipate periods of higher liquid carryover risk and inform operational planning.

---

## 9. General Troubleshooting Checklist (Reusable)

- [ ] Review compressor suction pressure, discharge pressure, and load at each surge event — check whether they explain the timing on their own
- [ ] If compressor-side parameters don't explain the pattern, review upstream suction scrubber level at high time resolution around each surge event
- [ ] Look specifically for brief, short-duration level excursions, not just sustained high-level conditions
- [ ] If found, investigate the upstream source (pipeline slugging, a sudden rate change, etc.) of the brief liquid surges
- [ ] Confirm the carryover mechanism: could a brief liquid carryover event plausibly change suction gas density/molecular weight enough to cross the surge line?
- [ ] Improve scrubber liquid handling margin (level control tuning, mechanical modification) rather than only adjusting the compressor's anti-surge control
- [ ] Coordinate with upstream operations on flow regimes that generate slugging, where relevant
- [ ] Tie ongoing scrubber level trending to the surge event log so future events can be quickly checked against this mechanism

## 10. Key Takeaway

> Not every compressor surge originates at the compressor — a brief liquid carryover event from an overwhelmed upstream scrubber can trigger surge just as effectively as a genuine compressor operating point excursion, and it won't show up if you only look at sustained suction/discharge pressure and load. Check high-time-resolution scrubber level data around each surge event before assuming the anti-surge control system itself is at fault; sometimes the compressor's control system is working perfectly and reacting correctly to a genuinely disrupted suction gas.

---

## Related Concepts / Tags

`centrifugal-compressor` `surge` `liquid-carryover` `suction-scrubber` `pipeline-slugging` `anti-surge-control` `multiphase-flow` `Peng-Robinson`

---

*This guide is derived from a representative field troubleshooting scenario. Values and thresholds shown are illustrative and should be validated against your own unit's design basis before applying.*

---

**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
