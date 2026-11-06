---
type: method
area: ml
areas: [ml, me697, bayesian]
source-ref: "ME 697 book, inverse/data 01"
tags: [optimization, ml, bayesian]
---

# LASSO

> [!definition] LASSO
> Least squares with an L1 penalty on the weights:
> $$\min_{w_0,w}\ \frac1N\sum_n\big(y_n-w_0-w^T\phi_n\big)^2+\lambda\|w\|_1.$$
> The bias $w_0$ is not penalized.
>
> (source: `inverse/data/01_lasso.ipynb`)

**Intuition**: The penalty pushes small weights to exactly zero, so the model selects features. Ridge (squared L2) shrinks weights but leaves them nonzero.

## Geometry
The constrained form is
$$\min\ \text{loss}\quad\text{s.t.}\quad\|w\|_1\le t.$$
The level sets of $\|w\|_1$ are diamonds. The loss contours first touch a diamond at a corner, where some components are zero (source: data/01).

## Bayesian view
Put a Laplace prior $w_j\sim\mathrm{Laplace}(0,b)$ on every weight:
$$p(w_j)=\frac1{2b}\exp\Big(-\frac{|w_j|}{b}\Big).$$
Then $\log p(w_j)=-|w_j|/b+\text{const}$, and with a Gaussian likelihood the L1 objective equals the negative log posterior up to a constant, with $\lambda$ set by $b$ and the noise level. Ridge corresponds to a Gaussian prior; the Laplace density has a sharper peak at zero and heavier tails. This is MAP estimation, see [[Bayesian inverse problems]].

> [!example] Sparse fit
> Data from $0.2x+0.3x^2+0.4x^3$, noise 0.01, 100 points; 20 features (monomials $x^0..x^9$, $\sin(2\pi ix)$ for $i=0..9$). `LassoCV` is compared with Ridge using cross-validated strength; the book reports that LASSO is sparser (source: data/01).

## Where it appears
- Fitted per state in [[SINDy]] with `LassoCV`; on the Lorenz system `LassoCV` failed and sequentially thresholded least squares was used instead.

**Covered in**: ASML book inverse/data (ME 697 4.7)
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/inverse/data/01_lasso.ipynb`, `02_sindy_1.ipynb`, `03_sindy_2.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[Weight initialization]]
- [[SINDy]] · [[Neural ODE]]
- The absolute-value trick turning $\min\sum c_i|x_i|$ into an LP is the LP form of $\ell_1$ penalties: [[BT ch1 - Introduction]] (p. 18, 1.3), [[Linear programming]].
