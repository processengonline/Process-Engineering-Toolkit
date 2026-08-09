# Design Guides

Reference study guides covering core process design and engineering topics. Each guide is a self-contained Markdown document with theory, standard industry practice, and worked examples.

## Index

| Guide | Folder | Scope |
|---|---|---|
| Compressor Settle-Out Calculations | [`compressor-settle-out-calculations/`](./compressor-settle-out-calculations) | Settle-out pressure and temperature calculations for compressor trip/blowdown scenarios. |
| Depressurization Calculation | [`depressurization-calculation/`](./depressurization-calculation) | Blowdown/depressurization rate and time calculations for vessels and systems per API 521. |
| Dynamic Simulation | [`dynamic-simulation/`](./dynamic-simulation) | Time-dependent process simulation methodology for transient and relief scenarios. |
| Flare Network Design | [`flare-network-design/`](./flare-network-design) | Flare header sizing, backpressure analysis, and network hydraulics. |
| Flow Assurance | [`flow-assurance/`](./flow-assurance) | Hydrate, wax, and slugging management strategy for multiphase flowlines. |
| Heat Exchanger Design | [`heat-exchanger-design/`](./heat-exchanger-design) | Shell & tube / plate exchanger thermal design and rating fundamentals. |
| IPDS | [`ipds/`](./ipds) | Instrument Protective Device Summary — logic, cause & effect, and SIS documentation practice. |
| Line List Preparation | [`line-list-preparation/`](./line-list-preparation) | Standard practice for compiling and maintaining a piping line list. |
| MDS | [`mds/`](./mds) | Material Data/Design Sheet preparation for equipment specification. |
| P&ID | [`p-and-id/`](./p-and-id) | P&ID symbology, development conventions, and review checklist. |
| Process Philosophies | [`process-philosophies/`](./process-philosophies) | Control, operating, and shutdown philosophy documentation practice. |
| Process Safety | [`process-safety/`](./process-safety) | Process safety fundamentals — HAZOP inputs, safeguards, layers of protection. |
| PSV Sizing & Design | [`psv-sizing-and-design/`](./psv-sizing-and-design) | Relief system design basis, scenario identification, and PSV selection per API 520/521. |
| Separator Design | [`separator-design/`](./separator-design) | Two/three-phase separator internals, sizing basis, and mechanical design considerations. |
| Steady-State Simulation | [`steady-state-simulation/`](./steady-state-simulation) | Steady-state process simulation setup, convergence, and validation practice. |
| Surge Analysis | [`surge-analysis/`](./surge-analysis) | Waterhammer/surge analysis methodology for liquid pipeline systems. |

## Folder Structure (per guide)

```
<guide-name>/
└── <Guide-Name>-Study-Guide.md
```

## Notes

- Guides are maintained as Markdown only (source of truth). PDF exports are generated for distribution/release purposes rather than tracked in version control.
- Each guide references the relevant industry standards (API, ASME, ISA, etc.) at the point of use rather than in a separate bibliography.
