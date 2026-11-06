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
$$f_h(x)=\rho f_l(x)+\epsilon(x),\qquad\epsilon\sim\mathrm{GP}$$
After the low-fidelity data, $f_h$ is a GP with
$$m=\rho\,\tilde m_l(x)$$
$$c=\rho^2\tilde k_l(x,x')+k_\epsilon(x,x')$$
Fit by maximizing $\log p(\mathbf y_l)+\log p(\mathbf y_h\mid\mathbf y_l)$ (source: `up/mf/01_mf_basics.md`).

## Nonlinear (Karumuri 2023)
Kernel on the input and the low-fidelity output:
$$k_h(x,x')=k\big((x,\tilde m_l(x)),(x',\tilde m_l(x'))\big)$$
A one-hidden-layer deep GP; in `tinygp` a `Transform` appending $\tilde m_l(x)$.

## Examples
Synthetic 2D function, and flow past a cylinder (8 high- and 99 low-fidelity runs); the multi-fidelity GP beats a high-fidelity-only GP.

## Wiki notes
- The notebook's $f_\ell$ differs from the markdown definition (scale 2.5 vs 1.5); see [[ME697 2.4 - Multi-fidelity modeling]].
- Which fidelity to query next is an [[Active learning]] problem.

**Sources**: `advanced-scientific-machine-learning/book/up/mf/intro.md`, `01_mf_basics.md`, `02_mf_gps.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Multi-fidelity Gaussian process]] · [[Kernel composition]] · [[Gaussian process]] · [[Surrogate model]]
- [[Latin hypercube sampling]] · [[ME697 2.4 - Multi-fidelity modeling]]
