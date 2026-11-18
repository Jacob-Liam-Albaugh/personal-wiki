---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [gp, optimization]
data-origin: [synthetic]
tasks: [active learning]
uses: 2
---

# Active learning test functions

**Summary**: 2 uses in ASML (ME 697). Data: synthetic. Tasks: active learning.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/al/02_al.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Active learning 1D noisy function

`text_books/advanced-scientific-machine-learning/book/up/al/02_al.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: active learning
- **Technique**: uncertainty sampling (max predictive variance), maximized by random Latin-hypercube search of 1000 points; GP with fixed hyperparameters (mean 0, amplitude 4, lengthscale 0.15, noise sd 0.1)
- **Data**: f(x) = sin(10 x^2) + x + 0.1 N(0,1); 1 initial point then 9 more acquired.
- **Data origin**: synthetic
- **Data file**: none
- **Forward model**: Analytic f above.
- **Unknown dimension**: 1 input
- **Data dimension**: 10 points
- **Ground truth**: analytic function
- **What makes it hard**: chirp-like nonstationary function
- **Libraries**: jax, tinygp
- **Notes**: Hyperparameters not learned.

## Active learning 2D piecewise-blended function

`text_books/advanced-scientific-machine-learning/book/up/al/02_al.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: active learning
- **Technique**: uncertainty sampling, GP with fixed hyperparameters (amplitude 4, lengthscales [0.3,0.3], noise 0.01)
- **Data**: 5 initial Latin-hypercube points, 21 iterations (plotted 0 to 20).
- **Data origin**: synthetic
- **Data file**: none
- **Forward model**: f1 = f_h from the MF 2D example; f2 = 10 x1(1-x1) x2(1-x2); alpha = sigmoid(10 (x2 - x1)); f = alpha f1 + (1-alpha) f2.
- **Unknown dimension**: 2 inputs
- **Data dimension**: about 26 points
- **Ground truth**: analytic function
- **What makes it hard**: regime change across the diagonal x1 = x2
- **Libraries**: jax, tinygp

## Related pages
- [[Examples catalogue]]
- [[Active learning]] · [[Gaussian process]]
