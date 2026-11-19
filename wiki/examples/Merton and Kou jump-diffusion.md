---
type: example
area: me697
areas: [me697, me539]
source-ref: "Planned example; not from an ingested source"
tags: [bayesian, inverse-problems]
status: lead
data-origin: [real]
tasks: [inverse problem and calibration, stochastic simulation]
uses: 0
---

# Merton and Kou jump-diffusion

**Summary**: Planned example, not built yet. Fills the gap "Jump noise" in the [[Dynamical systems table]]. Data: real. Tasks: inverse problem and calibration, stochastic simulation.

Lead page written from web search and background knowledge, not from an ingested source. The model and the papers named are **[unverified]**.

**Sources**: the links below.
**Last updated**: 2026-11-19

---

## Merton and Kou jump-diffusion

- **Source**: planned, not in the books or lab papers
- **Gap filled**: Jump noise
- **Class**: SDE with jumps
- **Forward model**: dS/S = mu dt + sigma dW + (J - 1) dN, with N a Poisson process and J a random jump size (lognormal for Merton, double exponential for Kou).
- **Data**: Daily index returns.
- **Data origin**: real
- **Links** (each opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read):
  - [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip): resolved
  - [FRED SP500 (last 10 years)](https://fred.stlouisfed.org/series/SP500): timed out for a script; open in a browser
- **Notes**: FRED's S&P 500 series is copyrighted by S&P and may not be redistributed; the French series is the safer choice.

## Related pages
- [[Examples catalogue]]
- [[Dynamical systems table]]
- [[Stochastic differential equation]] · [[Tumour growth (GBM)]]
