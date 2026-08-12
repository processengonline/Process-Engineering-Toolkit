# Calculators
Python-based sizing and hydraulic calculation tools for common process engineering equipment. Each tool lives in its own folder with the script, a README describing methodology/inputs/outputs, and examples.

## Index

| Tool | Folder | Purpose | Live Calculator |
|---|---|---|---|
| Breather Valve Sizing | [`Breather Valve Sizing/`](./Breather%20Valve%20Sizing) | Sizes tank conservation vents (breather valves) for thermal in/out-breathing and pump-in/pump-out venting per API 2000. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Breather%20Valve%20Sizing/) |
| Control Valve Sizing | [`Control Valve Sizing/`](./Control%20Valve%20Sizing) | Calculates Cv/Kv, valve trim selection, and cavitation/choked-flow checks per ISA/IEC 60534. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Control%20Valve%20Sizing/) |
| Line Hydraulics | [`Line Hydraulics/`](./Line%20Hydraulics) | Pressure drop, velocity, and erosional velocity checks for single- and two-phase pipe segments. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Line%20Hydraulics/) |
| PSV Sizing | [`PSV Sizing/`](./PSV%20Sizing) | Relief valve orifice sizing for vapor, liquid, two-phase, and fire relief scenarios per API 520/521. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/PSV%20Sizing/) |
| Pump Hydraulics | [`Pump Hydraulics/`](./Pump%20Hydraulics) | System curve generation, NPSH available calculation, and duty point verification. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Pump%20Hydraulics/) |
| Separator Sizing | [`Separator Sizing/`](./Separator%20Sizing) | Vertical/horizontal two- and three-phase separator sizing per droplet settling theory (Souders-Brown). | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Separator%20Sizing/) |
| Tank Heat Loss | [`Tank Heat Loss/`](./Tank%20Heat%20Loss) | Storage tank heat loss estimation for insulation design and heat tracing load calcs. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Tank%20Heat%20Loss/) |
| Tank Sizing | [`Tank Sizing/`](./Tank%20Sizing) | Atmospheric/low-pressure storage tank sizing including working, minimum, and vapor space volumes. | [Open ↗](https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Tank%20Sizing/) |


## Folder Structure (per tool)
```
<tool-name>/
├── <tool_name>.py           # main script
├── README.md                 # methodology, standards referenced, inputs, outputs
└── examples/
    └── sample_report_output.txt
```

## Running a Tool
```bash
cd <tool-name>
python <tool_name>.py --help
```
Refer to each tool's individual README for required input parameters, units convention, and applicable design codes/standards.

Some tools also ship an interactive browser-based calculator (see the **Live Calculator** column above) — open it directly in-browser, no Python install required.

## Requirements
These scripts are written in standard Python 3 with minimal dependencies. If a `requirements.txt` is added at the repo root, install with:

```bash
pip install -r requirements.txt
```

---
**Shubham Chatterjee** · Process Engineer
[processengonline.github.io](https://processengonline.github.io/) · [GitHub](https://github.com/processengonline)
