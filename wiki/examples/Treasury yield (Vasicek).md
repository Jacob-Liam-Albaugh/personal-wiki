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

# Treasury yield (Vasicek)

**Summary**: 1 use in ASML (ME 697). Data: real. Tasks: system identification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/sodes/04_ornstein_uhlenbeck.ipynb`.
**Last updated**: 2026-11-18

---

## Vasicek / Ornstein-Uhlenbeck on 2-year Treasury yield

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/sodes/04_ornstein_uhlenbeck.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: system identification / SDE parameter estimation
- **Technique**: Fit OU parameters on the recovery segment after 2020-03-12 / 2021-09-12 with time rescaled to [0,1]
- **Data**: FRED DGS2, 2-year Treasury constant-maturity yield. 1555 rows, columns observation_date, DGS2; 2019-01-02 to 2024-12-17; 63 NaN.
- **Data origin**: real
- **Data file**: data/twoYearTnote.csv
- **Forward model**: dX = lambda (mu - X) dt + sigma dW.
- **Unknown dimension**: 3 (mu, lambda, sigma) plus x0
- **Data dimension**: ~1500 daily values
- **Ground truth**: none (real data)
- **What makes it hard**: Regime change (COVID); non-stationary segment
- **Libraries**: jax, pandas
- **References**: FRED DGS2
- **Notes**: x0=0.21%, mu=4.358%, lambda=5.226, sigma=1.311. Code has a likely bug: sqrt((2\*lam\*var)/1 - exp(-2\*lam\*t)).

## Related pages
- [[Examples catalogue]]
- [[Ornstein-Uhlenbeck process]]
