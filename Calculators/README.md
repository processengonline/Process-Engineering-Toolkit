# Calculators
Python-based sizing and hydraulic calculation tools for common process engineering equipment. Each tool lives in its own folder with the script, a README describing methodology/inputs/outputs, and examples.

## Index

<table>
<thead>
<tr><th>Tool</th><th>Folder</th><th>Purpose</th><th>Live Calculator</th></tr>
</thead>
<tbody>
<tr>
<td>Breather Valve Sizing</td>
<td><a href="./Breather%20Valve%20Sizing"><code>Breather Valve Sizing/</code></a></td>
<td>Sizes tank conservation vents (breather valves) for thermal in/out-breathing and pump-in/pump-out venting per API 2000.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Breather%20Valve%20Sizing/">Open ↗</a></td>
</tr>
<tr>
<td>Control Valve Sizing</td>
<td><a href="./Control%20Valve%20Sizing"><code>Control Valve Sizing/</code></a></td>
<td>Calculates Cv/Kv, valve trim selection, and cavitation/choked-flow checks per ISA/IEC 60534.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Control%20Valve%20Sizing/">Open ↗</a></td>
</tr>
<tr>
<td>Line Hydraulics</td>
<td><a href="./Line%20Hydraulics"><code>Line Hydraulics/</code></a></td>
<td>Pressure drop, velocity, and erosional velocity checks for single- and two-phase pipe segments.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Line%20Hydraulics/">Open ↗</a></td>
</tr>
<tr>
<td>PSV Sizing</td>
<td><a href="./PSV%20Sizing"><code>PSV Sizing/</code></a></td>
<td>Relief valve orifice sizing for vapor, liquid, two-phase, and fire relief scenarios per API 520/521.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/PSV%20Sizing/">Open ↗</a></td>
</tr>
<tr>
<td>Pump Hydraulics</td>
<td><a href="./Pump%20Hydraulics"><code>Pump Hydraulics/</code></a></td>
<td>System curve generation, NPSH available calculation, and duty point verification.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Pump%20Hydraulics/">Open ↗</a></td>
</tr>
<tr>
<td>Separator Sizing</td>
<td><a href="./Separator%20Sizing"><code>Separator Sizing/</code></a></td>
<td>Vertical/horizontal two- and three-phase separator sizing per droplet settling theory (Souders-Brown).</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Separator%20Sizing/">Open ↗</a></td>
</tr>
<tr>
<td>Tank Heat Loss</td>
<td><a href="./Tank%20Heat%20Loss"><code>Tank Heat Loss/</code></a></td>
<td>Storage tank heat loss estimation for insulation design and heat tracing load calcs.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Tank%20Heat%20Loss/">Open ↗</a></td>
</tr>
<tr>
<td>Tank Sizing</td>
<td><a href="./Tank%20Sizing"><code>Tank Sizing/</code></a></td>
<td>Atmospheric/low-pressure storage tank sizing including working, minimum, and vapor space volumes.</td>
<td><a href="https://processengonline.github.io/Process-Engineering-Toolkit/Calculators/Tank%20Sizing/">Open ↗</a></td>
</tr>
</tbody>
</table>
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
