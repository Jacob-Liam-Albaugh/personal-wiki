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

# SIR epidemic (boarding school influenza)

**Summary**: Planned example, not built yet. Fills the gap "Canonical" in the [[Dynamical systems table]]. Data: real. Tasks: inverse problem and calibration.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## SIR epidemic (boarding school influenza)

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Canonical
- **Class**: ODE
- **Forward model**: S' = -beta S I / N; I' = beta S I / N - gamma I; R' = gamma I.
- **Data**: 14 daily counts of boys in bed and convalescent, 1978, from the R outbreaks package.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [Boarding-school influenza data](https://r-packages.io/datasets/influenza_england_1978_school): resolved
  - [Eyam plague 1666 (8 rows)](https://rdrr.io/cran/MultiBD/man/Eyam.html): resolved
- **Notes**: The textbook SIR dataset.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Bayesian inverse problems]] · [[PK two-compartment IV bolus]]
