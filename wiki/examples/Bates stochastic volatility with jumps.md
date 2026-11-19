---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [bayesian, inverse-problems]
status: lead
data-origin: [real]
tasks: [inverse problem and calibration, state estimation]
uses: 0
---

# Bates stochastic volatility with jumps

**Summary**: Planned example, not built yet. Fills the gap "Jump noise" in the [[Dynamical systems table]]. Data: real. Tasks: inverse problem and calibration, state estimation.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## Bates stochastic volatility with jumps

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Jump noise
- **Class**: SDE with jumps
- **Forward model**: Heston stochastic volatility plus Merton jumps in the price.
- **Data**: Daily VIX close from 1990, used as a volatility proxy alongside index returns.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [FRED VIXCLS](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS): timed out for a script; open in a browser
  - [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip): resolved
- **Notes**: Hidden volatility state makes this a filtering problem too. Papers: Bates 1996; Eraker, Johannes and Polson 2003.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Stochastic differential equation]] · [[Particle filter]] · [[Merton and Kou jump-diffusion]]
