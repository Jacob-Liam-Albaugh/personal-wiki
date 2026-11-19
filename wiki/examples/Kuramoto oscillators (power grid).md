---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [inverse-problems]
status: lead
data-origin: [real]
tasks: [system identification, inverse problem and calibration]
uses: 0
---

# Kuramoto oscillators (power grid)

**Summary**: Planned example, not built yet. Fills the gap "Interacting particles" in the [[Dynamical systems table]]. Data: real. Tasks: system identification, inverse problem and calibration.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## Kuramoto oscillators (power grid)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Interacting particles
- **Class**: ODE network
- **Forward model**: theta_i' = omega_i + (K/N) sum_j sin(theta_j - theta_i); the grid adds inertia (swing equation).
- **Data**: Mains frequency at 17 sites in 12 synchronous areas, 1 Hz and faster.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [Power grid frequency database](https://osf.io/by5hu/): resolved
  - [Rydin Gorjão et al. 2020](https://arxiv.org/abs/2006.01771): resolved
- **Notes**: No coupled-metronome data deposit was found, so the grid is the real Kuramoto system.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Power-grid swing dynamics]]
