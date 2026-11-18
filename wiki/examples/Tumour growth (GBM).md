---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [inverse-problems]
data-origin: [real]
tasks: [system identification]
uses: 1
---

# Tumour growth (GBM)

**Summary**: 1 use in ASML (ME 697). Data: real. Tasks: system identification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/sinverse/sodes/03_stochastic_exponential_growth.ipynb`.
**Last updated**: 2026-11-18

---

## Geometric Brownian motion tumour growth

`text_books/advanced-scientific-machine-learning/book/sinverse/sodes/03_stochastic_exponential_growth.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: system identification / SDE parameter estimation
- **Technique**: Log-space MLE; train t<250 h, test t>=250 h; simulate 1000 paths
- **Data**: Cell-count time series N(t) of glioblastoma-type cells (Johnson et al., PLOS Biol). CSV 96x181 with 'time'/'N' header rows; initial-seeding groups n=2 (59 replicates, 90 time points, to 354.87 h), n=5 (60, 94, to 337.1 h), n=12 (59, 85, to 336 h). Notebook uses the n=12 block (~10 replicates).
- **Data origin**: real
- **Data file**: data/cancer_growth.csv
- **Forward model**: dN = mu N dt + sigma N dW (GBM); log-space Gaussian increments with Ito correction.
- **Unknown dimension**: 2 (mu, sigma)
- **Data dimension**: ~85 time points per replicate
- **Ground truth**: Held-out t>=250 h data
- **What makes it hard**: Replicate variability not captured by GBM
- **Libraries**: jax, pandas, numpy
- **References**: Johnson et al., PLOS Biology, journal.pbio.3000399
- **Notes**: Fit mu=0.010, sigma=0.073. Notebook concludes simulated samples do not resemble replicates.

## Related pages
- [[Examples catalogue]]
- [[Brownian motion]] · [[Geometric Brownian motion]]
