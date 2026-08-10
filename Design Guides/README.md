# [/Design Guides](./Design%20Guides)

Reference study guides covering core process design and engineering topics. Each guide is a self-contained Markdown document with theory, standard industry practice, and worked examples.

## Index

| Guide | Folder | Scope |
|---|---|---|
| Compressor Settle-Out Calculations | [`Compressor Settle-Out Calculations/`](./Compressor%20Settle-Out%20Calculations) | Settle-out pressure and temperature calculations for compressor trip/blowdown scenarios. |
| Depressurization Calculation | [`Depressurization Calculation/`](./Depressurization%20Calculation) | Blowdown/depressurization rate and time calculations for vessels and systems per API 521. |
| Dynamic Simulation | [`Dynamic Simulation/`](./Dynamic%20Simulation) | Time-dependent process simulation methodology for transient and relief scenarios. |
| Flare Network Design | [`Flare Network Design/`](./Flare%20Network%20Design) | Flare header sizing, backpressure analysis, and network hydraulics. |
| Flow Assurance | [`Flow Assurance/`](./Flow%20Assurance) | Hydrate, wax, and slugging management strategy for multiphase flowlines. |
| Heat Exchanger Design | [`Heat Exchanger Design/`](./Heat%20Exchanger%20Design) | Shell & tube / plate exchanger thermal design and rating fundamentals. |
| IPDS | [`IPDS/`](./IPDS) | Instrument Protective Device Summary — logic, cause & effect, and SIS documentation practice. |
| Line List Preparation | [`Line List Preparation/`](./Line%20List%20Preparation) | Standard practice for compiling and maintaining a piping line list. |
| MDS | [`MDS/`](./MDS) | Material Data/Design Sheet preparation for equipment specification. |
| P&ID | [`P&ID/`](./P%26ID) | P&ID symbology, development conventions, and review checklist. |
| Process Philosophies | [`Process Philosophies/`](./Process%20Philosophies) | Control, operating, and shutdown philosophy documentation practice. |
| Process Safety | [`Process Safety/`](./Process%20Safety) | Process safety fundamentals — HAZOP inputs, safeguards, layers of protection. |
| PSV Sizing & Design | [`PSV Sizing & Design/`](./PSV%20Sizing%20%26%20Design) | Relief system design basis, scenario identification, and PSV selection per API 520/521. |
| Separator Design | [`Separator Design/`](./Separator%20Design) | Two/three-phase separator internals, sizing basis, and mechanical design considerations. |
| Steady-State Simulation | [`Steady-State Simulation/`](./Steady-State%20Simulation) | Steady-state process simulation setup, convergence, and validation practice. |
| Surge Analysis | [`Surge Analysis/`](./Surge%20Analysis) | Waterhammer/surge analysis methodology for liquid pipeline systems. |

## Folder Structure (per guide)

```
<guide-name>/
├── README.md                       # study guide (Markdown, source of truth)
└── <Guide-Name>-Study-Guide.pdf    # generated PDF export
```

## Notes

- Each guide's `README.md` is the Markdown source of truth; the accompanying PDF is a generated export for distribution, tracked in version control alongside it.
- Each guide references the relevant industry standards (API, ASME, ISA, etc.) at the point of use rather than in a separate bibliography.
