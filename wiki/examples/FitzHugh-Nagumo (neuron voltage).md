---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [bayesian, inverse-problems]
status: lead
data-origin: [real]
tasks: [inverse problem and calibration, system identification]
uses: 0
---

# FitzHugh-Nagumo (neuron voltage)

**Summary**: Planned example, not built yet. Fills the gap "Multiscale / stiff" in the [[Dynamical systems table]]. Data: real. Tasks: inverse problem and calibration, system identification.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## FitzHugh-Nagumo (neuron voltage)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Multiscale / stiff
- **Class**: fast-slow ODE
- **Forward model**: v' = v - v^3/3 - w + I; w' = eps (v + a - b w), with eps small.
- **Data**: Patch-clamp membrane-voltage recordings under step, ramp and noise currents.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [Allen Cell Types database](https://celltypes.brain-map.org/): resolved
- **Notes**: Real fast-slow voltage traces. No raw squid-axon data was found.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Stiff ODE test problems]]
