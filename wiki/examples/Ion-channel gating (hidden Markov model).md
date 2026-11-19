---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [bayesian]
status: lead
data-origin: [real]
tasks: [state estimation, inverse problem and calibration]
uses: 0
---

# Ion-channel gating (hidden Markov model)

**Summary**: Planned example, not built yet. Fills the gap "Markov chain" in the [[Dynamical systems table]]. Data: real. Tasks: state estimation, inverse problem and calibration.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## Ion-channel gating (hidden Markov model)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Markov chain
- **Class**: hidden Markov model
- **Forward model**: Channel switches between closed and open states as a Markov chain; the current is the state level plus Gaussian noise.
- **Data**: Patch-clamp currents from single channels, about 200,000 points per series.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [R ionChannelData](https://rolfturner.r-universe.dev/ionChannelData): page refuses scripts (403); the r-universe API confirms the package, version 0.0-3
- **Notes**: A hidden discrete state with a clean inference target. Not on CRAN; licence file not read.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Particle filter]] · [[Stochastic state-space model]]
