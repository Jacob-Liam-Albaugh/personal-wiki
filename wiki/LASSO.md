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

## As a linear program
The absolute-value trick of [[LP modelling]] turns $\min\sum c_i|x_i|$ with $c_i\ge0$ and linear constraints $\mathbf A\mathbf x\ge\mathbf b$ into an LP (BT p. 18, 1.3), which is the LP form of an $\ell_1$ penalty. In the constrained form above with a linear loss or an $\ell_1$ loss the whole problem is a [[Linear programming]] problem; with the squared loss it is a quadratic program.

**Covered in**: ASML book inverse/data (ME 697 4.7); Bertsimas-Tsitsiklis ch. 1 §1.3 (absolute values, p. 18)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/data/01_lasso.ipynb`, `02_sindy_1.ipynb`, `03_sindy_2.ipynb`; `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 1).
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[Weight initialization]]
- [[SINDy]] · [[Neural ODE]]
- [[LP modelling]] · [[Linear programming]]
