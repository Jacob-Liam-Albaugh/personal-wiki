---
type: concept
area: me697
areas: [me697, gp]
tags: [uq, gp, ml]
---

# Multi-fidelity modeling

**Summary**: Builds a surrogate of an expensive high-fidelity model $f_h$ from many runs of a cheap low-fidelity model $f_l$ (coarse mesh, simplified physics) plus few high-fidelity runs. The course uses Gaussian processes.

---

## Target
$$p(f_h\mid\mathbf y_l,\mathbf y_h)=\int p(f_h\mid f_l,\mathbf y_l,\mathbf y_h)\,p(f_l\mid\mathbf y_l)\,df_l$$

## Kennedy-O'Hagan (linear)
> [!algorithm] Kennedy-O'Hagan model (01)
> $$f_h(x)=\rho f_l(x)+\epsilon(x),\qquad \epsilon\sim\mathrm{GP}(m_\epsilon,k_\epsilon)$$
> with $\epsilon$ independent of $f_l$ and $\rho$ a scalar (or a basis expansion $\rho(x)=\sum_iw_i\phi_i(x)$). After seeing the low-fidelity data, $f_h$ is again a GP:
> $$m_{h|y_l}(x)=\rho\,\tilde m_l(x)$$
> $$c_{h|y_l}(x,x')=\rho^2\tilde k_l(x,x')+k_\epsilon(x,x')$$
> For input-dependent $\rho$ replace $\rho^2$ by $\rho(x)\rho(x')$. Condition on $\mathbf y_h$ with the usual GP formulas, using $c_{h|y_l}$ in place of the prior kernel.
> (source: `01_mf_basics.md`)

Fit by maximizing $\log p(\mathbf y_l)+\log p(\mathbf y_h\mid\mathbf y_l)$ (source: `up/mf/01_mf_basics.md`).

## Nonlinear (Karumuri 2023)
$f_h\mid f_l$ is a GP whose kernel acts on the input and the low-fidelity output:
$$k_h(x,x')=k\big((x,f_l(x)),(x',f_l(x'))\big)$$
With plenty of low-fidelity data the posterior of $f_l$ collapses to its mean, so use
$$k_h(x,x')=k\big((x,\tilde m_l(x)),(x',\tilde m_l(x'))\big)$$
A one-hidden-layer deep GP; in `tinygp` a `Transform` appending $\tilde m_l(x)$.

## Examples
Synthetic 2D function, and flow past a cylinder (8 high- and 99 low-fidelity runs); the multi-fidelity GP beats a high-fidelity-only GP.

## Wiki notes
- The notebook's $f_\ell$ differs from the markdown definition (scale 2.5 vs 1.5).
- Which fidelity to query next is an [[Active learning]] problem.

## Details (book, up/mf)
- Sources of fidelity: fine versus coarse mesh, FE model versus analytic model, experiment versus analytic model. The target needs (1) a [[Gaussian process]] regression for $f_l$ with noisy data and (2) a model linking $f_h$ to $f_l$.
- Fitting: both terms of $\log p(\mathbf y_l,\mathbf y_h)=\log p(\mathbf y_l)+\log p(\mathbf y_h\mid\mathbf y_l)$ are analytic. With much more low-fidelity data, fit the low-fidelity parameters on the first term alone, then the rest on the second.
- Nonlinear model: general deep-GP inference is hard (Damianou et al. 2013); the appended $\tilde m_l(x)$ input gets its own length scale.

> [!example] Synthetic 2D function
> $f_h$ is a sum of a squared sine and an exponentially damped squared cosine; $f_\ell$ is a scaled $f_h$ plus extra terms (modified from Perdikaris et al. 2015). Data from [[Latin hypercube sampling]]. The low-fidelity GP fits $f_\ell$ but misses $f_h$; the multi-fidelity GP is clearly the most accurate, better than a GP on the high-fidelity data alone. Exercises: vary the numbers of low and high data, find the $N_h$ where the high-only GP catches up, and how different $f_\ell$ may be.

> [!example] Flow past a cylinder
> Random inflow profile with two Gaussian variables; the quantity of interest is the superquantile risk $\mathcal R_{0.6}[C_{BP}]$ of the base pressure coefficient (mean of the upper 40%). 8 high-fidelity and 99 low-fidelity runs. The multi-fidelity GP has the best parity plot and its response surface almost coincides with the truth.

> [!example] Homework 4, multi-fidelity part (source: homework/04_homework.ipynb)
> Final stage of the Branin exercise, after the surrogate and [[Active learning]] stages ([[Surrogate model]]).

Wiki notes:
- The markdown gives $f_\ell=1.5f_h+\tfrac13\sin(x_1+x_2)+\tfrac12e^{-x_1}\sin(x_1+7x_2)$, but the code uses $2.5f_h+\tfrac13\big(\sin(x_1+x_2)+\tfrac12e^{-x_1}\sin(x_1+7x_2)\big)$: the scale and the factor on the last term differ.
- "$f_h\mid f_l=\mathrm{GP}(\tilde m_h,\tilde k_h)$" with mean $\rho\tilde m_l$ is already the result after integrating out $f_l$ given $\mathbf y_l$. Conditional on $f_l$ itself the mean is $\rho f_l+m_\epsilon$ and the covariance is $k_\epsilon$.
- The Kennedy-O'Hagan reference is cited by the book as 2000 (Biometrika 87).
- The nonlinear kernel on $(x,\tilde m_l(x))$ is a warping of the input, a form of [[Kernel composition]].

**Covered in**: ASML book up/mf (ME 697 2.4); homework 4
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/mf/intro.md`, `01_mf_basics.md`, `02_mf_gps.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Multi-fidelity Gaussian process]] · [[Kernel composition]] · [[Gaussian process]] · [[Surrogate model]]
- [[Latin hypercube sampling]]
