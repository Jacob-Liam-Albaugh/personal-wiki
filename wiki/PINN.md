---
type: method
area: physics-informed
areas: [physics-informed, ift]
source-ref: "Alberts & Bilionis 2023, eqs. 28-32, pp. 15-17"
tags: [physics-informed, ml, pde]
---

# Physics-informed neural networks (PINN) and B-PINN

> [!theorem] PINN as a PIFT MAP estimate (Alberts & Bilionis 2023, eqs. 28-30)
> With a flat prior on network weights $\theta$ and constant partition function, the PINN loss equals the parameter information Hamiltonian when $r_d=s/(2\sigma^2)$ and $r_p=\beta$. With physics parameters $\lambda$, $-\log p(\theta,\lambda|d)$ also has $\log Z(\lambda)+H(\lambda)$, which the PINN loss drops.

> [!theorem] When a B-PINN matches PIFT (eqs. 31-32)
> A B-PINN uses a fictitious zero-residual likelihood with noise $\sigma_r$ and a Gaussian weight prior. Its posterior equals PIFT's iff collocation points are shared, $\sigma_\theta=\infty$, and
> $$\sigma_r^2=n/(2\beta).$$

**Intuition**: B-PINN posteriors collapse as collocation points $n\to\infty$ (Bayesian asymptotics); PIFT's spread is set by $\beta$ and stays.

## Where it appears
- [[PIFT (Alberts 2023)]] — derivations.
- [[IFT thermal conductivity (Alberts 2026)]] — contrast; cites Hao & Bilionis (neural information field filter, not read) for B-PINN's poor extrapolation.
- [[PINNs (Raissi 2019)]] — original continuous-time and discrete-time (implicit Runge-Kutta) formulations (source: Physics Informed Architectures/Karniadakis, Raissi, Perdikaris - PINNs - Physics-Informed Neural Networks.pdf).
- [[When and why PINNs fail (Wang 2022)]] — NTK analysis: boundary and residual loss blocks converge at different rates; adaptive weights from Tr(K) ratios; see [[Neural tangent kernel]].
- [[Respecting causality (Wang 2022)]] — causal weights along time; temporal convergence rate as a stopping criterion.
- [[Expert's guide to PINNs (Wang 2023)]] — training pipeline: non-dimensionalization, Fourier features, random weight factorization, loss balancing, curriculum.
- [[Physics-informed ML review (Karniadakis 2021)]] — PINN as a learning bias; soft penalty equals MAP under a physics likelihood (review, p. 7).
- [[ME697 5.1 - PINN basics]]: residual loss, hard boundary conditions, [[Non-dimensionalization]] with Glorot init, Fourier features against [[Spectral bias]], and the [[Energy functional]] alternative (source: pinns/basics/forward.ipynb, energy.ipynb).
- [[ME697 5.2 - Parametric PINNs]] / [[Parametric PINN]]: branch-trunk ansatz $N=\sum_i b_i(\xi)\phi_i(x)$ with loss averaged over $p(\xi)$ (source: pinns/parametric).
- [[ME697 5.3 - PINNs for inverse problems]]: stub notebooks only (source: pinns/inverse).

## PINN literature
The PINN literature is ingested under [[Physics-informed machine learning]] (five PINN pages plus the review).
- Book chapters pinns/basics, parametric, inverse are now ingested; remove from the queue.

## Examples

> [!example] Homework 7, neo-Hookean PINN (source: homework/07_homework.ipynb)
> Train a PINN on $[0,1]^2$ minimizing a hyperelastic stored energy: $\delta=0.1$ first, then $\delta=0.5$ by continuation (transfer learning), then a parametric PINN over $\delta\in[0,0.5]$ with the loss integrated over $\delta$. See [[Energy functional]], [[Parametric PINN]], [[ME697 7 - Homework]].

- Wiki note: the energy loss was less accurate than the residual loss in the book's Poisson example (source: pinns/basics/energy.ipynb).

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Physics-informed prior]] · [[Information field theory]]
- [[Physics-informed machine learning]] · [[PINNs (Raissi 2019)]] · [[When and why PINNs fail (Wang 2022)]] · [[Respecting causality (Wang 2022)]] · [[Expert's guide to PINNs (Wang 2023)]] · [[Neural tangent kernel]] · [[Physics-informed ML review (Karniadakis 2021)]]
- [[SIREN]] (smooth derivatives for PDE losses, Sitzmann 2020 §4), [[Spectral bias]], [[Fourier features]].
- [[Poisson and Laplace equations]], [[Maxwell's equations]]: classical PDEs of electrostatics and electromagnetics that PINNs can solve (source: Electromagnetics/Lectures Slides/lect_12.pdf).
