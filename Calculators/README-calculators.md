# Calculators

Python-based sizing and hydraulic calculation tools for common process engineering equipment. Each tool lives in its own folder with the script, a README describing methodology/inputs/outputs, and examples.

## Index

| Tool | Folder | Purpose |
|---|---|---|
| Breather Valve Sizing | [`Breather Valve Sizing/`](./Breather%20Valve%20Sizing) | Sizes tank conservation vents (breather valves) for thermal in/out-breathing and pump-in/pump-out venting per API 2000. |
| Control Valve Sizing | [`Control Valve Sizing/`](./Control%20Valve%20Sizing) | Calculates Cv/Kv, valve trim selection, and cavitation/choked-flow checks per ISA/IEC 60534. |
| Line Hydraulics | [`Line Hydraulics/`](./Line%20Hydraulics) | Pressure drop, velocity, and erosional velocity checks for single- and two-phase pipe segments. |
| PSV Sizing | [`PSV Sizing/`](./PSV%20Sizing) | Relief valve orifice sizing for vapor, liquid, two-phase, and fire relief scenarios per API 520/521. |
| Pump Hydraulics | [`Pump Hydraulics/`](./Pump%20Hydraulics) | System curve generation, NPSH available calculation, and duty point verification. |
| Separator Sizing | [`Separator Sizing/`](./Separator%20Sizing) | Vertical/horizontal two- and three-phase separator sizing per droplet settling theory (Souders-Brown). |
| Tank Heat Loss | [`Tank Heat Loss/`](./Tank%20Heat%20Loss) | Storage tank heat loss estimation for insulation design and heat tracing load calcs. |
| Tank Sizing | [`Tank Sizing/`](./Tank%20Sizing) | Atmospheric/low-pressure storage tank sizing including working, minimum, and vapor space volumes. |

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

## Requirements

These scripts are written in standard Python 3 with minimal dependencies. If a `requirements.txt` is added at the repo root, install with:

```bash
pip install -r requirements.txt
```
