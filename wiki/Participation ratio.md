---
type: definition
area: stochastic
areas: [stochastic, ml]
source-ref: "de Albuquerque, Pearson 2024, eq. 7 (after Gao et al. 2017)"
tags: [diffusion, generative, ml]
---

# Participation ratio

> [!definition] Participation ratio (PR)
> For a covariance matrix $\Sigma$ with eigenvalues $\sigma_i^2$,
> $$\mathrm{PR}(\Sigma)=\frac{\mathrm{tr}(\Sigma)^2}{\mathrm{tr}(\Sigma^2)}=\frac{\big(\sum_i\sigma_i^2\big)^2}{\sum_i\sigma_i^4}$$
>
> (source: de Albuquerque, Pearson - Inflationary Flows PDF, eq. 7, p. 5, citing Gao et al. 2017; Gao et al. not read)

**Intuition**: a soft count of how many directions carry the variance. It needs only second-order statistics, so it is cheap, and blind to any structure that the covariance does not see.

## Basic consequences
- $\mathrm{PR}=1$ when $\Sigma$ has rank 1; $\mathrm{PR}=d$ when $\Sigma\propto I_d$ (p. 5).
- Invariant to linear transforms of the data, as stated by the paper (p. 5). Wiki note: the formula is invariant to rotations and to a global scale; a general invertible linear map changes the eigenvalues and so the PR. The paper's own App. C.2.3 notes that rescaling dimensions changes what is compressed.
- Proportional inflation of all eigenvalues, $d\sigma^2/dt=\rho\sigma^2$, leaves PR unchanged; inflating some directions faster drives PR to that of the fastest-growing subspace (eqs. 8-10).

## Examples
Dataset PR (Table 15): MNIST 30.69, Fashion MNIST 7.90, SVHN 2.90, CIFAR-10 9.24.

## Where it appears
- [[Inflationary flows (de Albuquerque 2024)]]: the quantity the noise schedule is designed to preserve or reduce.

**Sources**: `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models.pdf`.
**Last updated**: 2026-11-11

---

## Related pages
- [[Principal component analysis]] · [[Karhunen-Loève expansion]] · [[Diffusion models]]
