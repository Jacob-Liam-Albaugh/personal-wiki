---
type: method
area: operators
areas: [operators, gp]
source-ref: "Kovachki, Lanthaler, Stuart 2024, §3.4, pp. 9-10"
tags: [operators, ml]
---

# Random features model (operator)

> [!algorithm] Random features model (Kovachki et al. 2024, §3.4, pp. 9-10)
> $$\Psi_{RFM}(u;\theta)(y)=\sum_{j=1}^M\theta_j\,\psi(u;\gamma_j)(y),\qquad\gamma_j\overset{iid}\sim\nu$$
> The features $\gamma_j$ are drawn once and frozen. Only the linear weights $\theta$ are trained, so the fit is convex with a unique minimizer.
> Fourier example: $\psi(u;\gamma)=\sigma\big(\mathcal F^{-1}(\chi\,\mathcal F_\gamma\,\mathcal Fu)\big)$, with $\gamma$ a Gaussian random field.
>
> (source: `papers/Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, pp. 9-10)

**Intuition**: a kernel method in disguise. The review relates it to kernel methods (p. 11). Wiki note: as $M\to\infty$ it tends to kernel regression with the induced kernel, which links it to [[Gaussian process]] regression. The outputs still lie on a nonlinear manifold, because $\psi$ is nonlinear in $u$.

The review says its analysis can account for finite samples, finite parameters and optimization together (citing its ref. [76]).

## Where it appears
- [[Operator learning review (Kovachki 2024)]].
- Wiki note: the course surrogates chapter does not use random features; they appear in part 1. For approximating a GP kernel with finite features compare the GLM surrogate $\hat f=\sum_iw_i\phi_i(x)$ in [[Surrogate model]] (source: `up/surrogates/01_basics_of_surrogate_models.md`). **[unverified]** whether the existing page needs more than this link.

## Connections
- a one-hidden-layer network with infinitely many iid-weight features is a GP by the central limit theorem (source: Duvenaud 2014, eqs. 5.4-5.5, p. 61).
- Greengard and O'Neil note that random Fourier features are cheap but not L2-optimal compared with the KL basis (source: Greengard-O'Neil 2022, p. 3).

**Sources**: `papers/Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Operator learning]] · [[Gaussian process]] · [[FNO]]
- Fourier-feature maps gamma(v) = [cos(2 pi B v), sin(2 pi B v)] with Gaussian B approximate stationary kernels (source: Tancik 2020, eq. 5-6). Link [[Fourier features]].
- [[Kernel methods]], [[RKHS]], [[Reduced-rank GPs (Greengard 2022)]].
