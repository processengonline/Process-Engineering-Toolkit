# Calculators
Python-based sizing and hydraulic calculation tools for common process engineering equipment. Each tool lives in its own folder with the script, a README describing methodology/inputs/outputs, and examples.

## Index

| Tool | Purpose | Live Calculator |
|---|---|---|
| BDV (Blowdown Valve) Sizing | Sizes emergency blowdown/depressuring orifices to the API 521 fire-case pressure and time targets via time-marching vessel blowdown simulation. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Blowdown%20Valve%20(BDV)%20Sizing/) |
| Breather Valve Sizing | Sizes tank conservation vents (breather valves) for thermal in/out-breathing and pump-in/pump-out venting per API 2000. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Breather%20Valve%20Sizing/) |
| Compressor Power | Calculates centrifugal compressor polytropic head, discharge temperature, and shaft power per the GPSA/API 617 polytropic method. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Centrifugal%20Compressor%20Power/) |
| Compressor Settle-Out | Calculates equalized settle-out pressure and temperature across isolated suction/discharge volumes after a compressor trip, via real-gas mass and energy balance. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Compressor%20Settle-Out%20Calculation/) |
| Control Valve Sizing | Calculates Cv/Kv, valve trim selection, and cavitation/choked-flow checks per ISA/IEC 60534. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Control%20Valve%20Sizing/) |
| Flare Header Backpressure | Calculates superimposed and built-up backpressure at a relief valve outlet via isothermal compressible flare tailpipe hydraulics per API 521. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Flare%20Header%20Backpressure%20Calculation/) |
| Flare Knockout Drum | Sizes a flare knockout drum for a governing transient relief case via Souders-Brown gas capacity and drainage-time liquid holdup, per API 521. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Flare%20Knockout%20Drum%20Sizing/) |
| Heat Exchanger Sizing | Rough first-pass shell-and-tube and air-cooler duty/LMTD sizing with the Bowman TEMA F-correction factor. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Heat%20Exchanger%20Calculation/) |
| Heat Tracing Sizing | Sizes electrical or steam heat tracing load for insulated piping from radial conduction heat loss against a design minimum ambient temperature. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Heat%20Tracing%20calculation/) |
| Instrument Air Receiver | Sizes the instrument air receiver volume needed to hold header pressure for a specified backup ride-through time after loss of the air compressors. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Instrument%20Air%20Receiver%20Sizing/) |
| Line Hydraulics | Pressure drop, velocity, and erosional velocity checks for single- and two-phase pipe segments. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Line%20Hydraulics/) |
| Line Sizing | Sizes pipe diameter for a target velocity/pressure-drop via Darcy-Weisbach, with an API RP 14E erosional-velocity check. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Line%20Sizing%20Calculation/) |
| Nitrogen Air Receiver | Sizes a high-pressure nitrogen bottle bank and regulator backup for critical/ESD instrument air on loss of the plant air compressors. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Nitrogen%20Backup%20Air%20Receiver%20Sizing/) |
| Nitrogen Blanketing | Sizes storage tank nitrogen blanketing gas demand and blanketing valve flow area per API 2000 breathing duty. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Nitrogen%20Blanketing%20Gas%20Demand%20%26%20Valve%20Sizing/) |
| Noise Screening (Control Valve / RO) | Screens control valve and restriction-orifice aerodynamic/hydrodynamic noise risk via Mach number, pressure ratio, and cavitation-index banding. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Noise%20Screening%20-%20Control%20Valve%20%20RO/) |
| Pipe Wall Thickness | Calculates required pipe wall thickness, or checks MAWP for a given wall, per the ASME B31.3 straight-pipe pressure design equation. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Pipe%20Wall%20Thickness%20Calculation/) |
| PSV Sizing | Relief valve orifice sizing for vapor, liquid, two-phase, and fire relief scenarios per API 520/521. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/PSV%20Sizing/) |
| Pump Hydraulics | System curve generation, head↔power conversion, and duty point verification. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Pump%20Hydraulics/) |
| Pump NPSH Available | Calculates NPSH available from source elevation, pressure, friction losses, and vapor pressure, checked against a required margin. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Pump%20NPSH%20Available%20Calculation/) |
| PVRV / Tank Breather Valve Sizing | Sizes tank pressure/vacuum relief valve (PVRV) mechanical venting capacity — normal venting demand, PVRV mechanical sizing, and emergency venting via subcritical compressible orifice flow per API 2000 — a companion tool to Breather Valve Sizing above. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/PVRV%20-%20Tank%20Breather%20Valve%20Sizing/) |
| Restriction Orifice Sizing | Sizes thin sharp-edged restriction-orifice plates for liquid (ISO 5167) and gas letdown (choked/subcritical) flow-limiting service. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Restriction%20Orifice%20Sizing/) |
| Rupture Disk Sizing | Sizes rupture disks alone or in combination with a PSV, including combination capacity factors and burst-tolerance margin checks, per API 520. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Rupture%20Disk%20Sizing/) |
| Separator Sizing | Vertical/horizontal two- and three-phase separator sizing per droplet settling theory (Souders-Brown). | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Separator%20Sizing/) |
| Surge Margin | Screens centrifugal compressor surge margin against a vendor-supplied surge point, with speed-affinity correction and required recycle-flow estimate. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Surge%20Margin%20Calculation/) |
| Tank Heat Loss | Storage tank heat loss estimation for insulation design and heat tracing load calculations. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Tank%20Heat%20Loss/) |
| Tank Sizing | Atmospheric/low-pressure storage tank sizing — solves diameter/height/volume with HHLL/HLL/LLL/LLLL working-volume levels. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Tank%20Sizing/) |
| Thermal Relief Sizing | Sizes thermal relief valves for blocked-in liquid-full lines and exchangers from first-principles thermal expansion rate. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Thermal%20Relief%20Valve%20Sizing/) |
| Two/Three-Phase Separator Sizing | Vertical/horizontal two- and three-phase separator sizing via Souders-Brown gas capacity and retention-time liquid holdup — a dedicated companion tool to Separator Sizing above. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Two%20or%20Three-Phase%20Separator%20Sizing/) |

## Running a Tool
```bash
cd <tool-name>
python <tool_name>.py --help
```

Some tools also ship an interactive browser-based calculator (see the **Live Calculator** column above) — open it directly in-browser, no Python install required.

---
**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
