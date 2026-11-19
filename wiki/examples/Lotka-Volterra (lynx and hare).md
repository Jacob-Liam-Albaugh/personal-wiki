---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [bayesian, inverse-problems]
status: lead
data-origin: [real]
tasks: [inverse problem and calibration]
uses: 0
---

# Lotka-Volterra (lynx and hare)

**Summary**: Planned example, not built yet. Fills the gap "Canonical" in the [[Dynamical systems table]]. Data: real. Tasks: inverse problem and calibration.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## Lotka-Volterra (lynx and hare)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Canonical
- **Class**: ODE
- **Forward model**: u' = alpha u - beta u v; v' = -gamma v + delta u v.
- **Data**: Hudson Bay Company pelt counts: 21 years (1900 to 1920) in the Stan file, 91 years (1845 to 1935) in R.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [Stan CSV, 1900-1920](https://raw.githubusercontent.com/stan-dev/example-models/master/knitr/lotka-volterra/hudson-bay-lynx-hare.csv): resolved
  - [R pelt, 1845-1935](https://tsibbledata.tidyverts.org/reference/pelt.html): resolved
  - [Stan case study](https://mc-stan.org/learn-stan/case-studies/lotka-volterra-predator-prey.html): resolved
- **Notes**: The canonical small Bayesian calibration. These are fur returns, not census counts.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Bayesian inverse problems]] · [[Catalysis kinetics]]
