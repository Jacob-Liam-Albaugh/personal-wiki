---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [synthetic]
tasks: [regression]
uses: 1
---

# Sparse regression (lasso and ridge)

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: regression.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/data/01_lasso.ipynb`.
**Last updated**: 2026-11-18

---

## Lasso/ridge sparse regression

`text_books/advanced-scientific-machine-learning/book/inverse/data/01_lasso.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Sparse regression
- **Technique**: sklearn LassoCV(fit_intercept=False) vs ridge CV; 2D L1-diamond illustration (w\*=(0.5,0.2), A=[ [1,-0.4],[-0.4,1]]); Laplace-prior Bayesian interpretation
- **Data**: 100 points x~U(-1,1), y=0.2x+0.3x^2+0.4x^3+N(0,0.01^2), unseeded np.random
- **Data origin**: synthetic
- **Forward model**: Linear in 20 features: monomials x^0..x^9 and sin(2 pi i x), i=0..9
- **Unknown dimension**: 20 coefficients (3 nonzero)
- **Data dimension**: 100
- **Ground truth**: true coefficients known
- **Libraries**: numpy, sklearn

## Related pages
- [[Examples catalogue]]
- [[LASSO]]
