---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [bayesian]
status: lead
data-origin: [real]
tasks: [inverse problem and calibration]
uses: 0
---

# Earthquake aftershocks (Hawkes, ETAS)

**Summary**: Planned example, not built yet. Fills the gap "Point process" in the [[Dynamical systems table]]. Data: real. Tasks: inverse problem and calibration.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## Earthquake aftershocks (Hawkes, ETAS)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Point process
- **Class**: point process
- **Forward model**: Event rate = background + sum over past events of a decaying kernel (Omori law, scaled by magnitude in ETAS).
- **Data**: Any region and time window from the USGS catalogue, up to 20,000 events per query.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [USGS ComCat API](https://earthquake.usgs.gov/fdsnws/event/1/): resolved
  - [R PtProcess catalogues](https://cran.r-project.org/web/packages/PtProcess/index.html): resolved
  - [R ETAS fitter](https://cran.r-project.org/web/packages/ETAS/index.html): resolved
- **Notes**: Self-exciting, so past events raise the rate. A plain Poisson fit is the baseline.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[California earthquakes]] · [[Coal mining disasters]]
