# Process Engineering Toolkit

A working reference library for process engineers — sizing calculators, design guides, and real-world troubleshooting case studies covering oil & gas, refining, and gas processing facilities.

This repo is organized into three pillars:

| Pillar | What it contains | Link |
|---|---|---|
| **Calculators** | Python scripts for equipment sizing and hydraulic calculations | [`/calculators`](./calculators) |
| **Design Guides** | Reference study guides on core process design topics | [`/design-guides`](./design-guides) |
| **Troubleshooting** | 50 real-world operational case studies with root-cause analysis | [`/troubleshooting`](./troubleshooting) |

---

## Repository Structure

```
process-engineering-toolkit/
├── calculators/        8 sizing tools (PSV, tank, pump, line, separator, etc.)
├── design-guides/       16 topic guides (surge analysis, flare network, MDS, etc.)
└── troubleshooting/      50 case studies (rotating equipment, separation, dehydration, etc.)
```

## Quickstart — Running a Calculator

Each calculator is a standalone Python script with its own README and a sample report output.

```bash
cd calculators/tank-sizing
python tank_sizing.py --help
```

See [`calculators/README.md`](./calculators/README.md) for the full list of tools and required inputs.

## Using the Design Guides

Each guide is a self-contained Markdown study document covering theory, standard practice, and worked examples for one process design topic. Browse the index at [`design-guides/README.md`](./design-guides/README.md).

## Using the Troubleshooting Library

Each case study documents a real symptom, diagnostic path, root cause, and corrective action for a specific piece of equipment or process unit. Browse the full index — searchable by equipment type or symptom — at [`troubleshooting/README.md`](./troubleshooting/README.md).

## Contributing

New calculators, guides, or case studies are welcome. Please:
1. Follow the existing folder naming convention (`kebab-case`, numbered where applicable).
2. Include a `README.md` in every new sub-folder.
3. Add an entry to the relevant pillar's index table.

## License

See [LICENSE](./LICENSE) for details.
