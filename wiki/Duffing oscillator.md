---
type: concept
area: me697
areas: [me697, bayesian]
source-ref: "ME 697 book, inverse/odes 03"
tags: [inverse-problems, bayesian, vi, mechanics]
---

# Duffing oscillator

**Summary**: A damped, driven oscillator with a cubic restoring term, used in the book as a test bed for VI versus [[Amortized VI]] with many observed trajectories.

**Covered in**: ASML book up/sensitivity_analysis (ME 697 2.1); homework 2
**Sources**: `advanced-scientific-machine-learning/book/inverse/odes/03_dyn_system_multiple_traj.ipynb`.
**Last updated**: 2026-11-06

---

## Model (source: odes/03)
$$\dot x=v,$$
$$\dot v=-2\xi\omega_nv-\omega_n^2x-\beta x^3+\gamma\sin\omega t.$$
The data are noisy accelerations with known noise. The unknowns are
$$\theta=(x_0,v_0,\omega_n,\xi,\beta).$$

## Priors
- $x_0,v_0\sim N(0,1)$
- $\beta\sim N(0,0.5^2)$
- $\omega_n\sim\mathrm{LogNormal}(1.2,0.3^2)$
- $\xi\sim\mathrm{LogNormal}(-1.9,0.6^2)$

## Result
A full-covariance Gaussian guide on a transformed space (with the Jacobian $|\det J_T|$) is trained per dataset (VI) and over many datasets (AVI, expected [[ELBO]] over $p(y)$, 1000 steps on a GPU, diverging trajectories filtered). VI reconstructs better; AVI is much faster at inference; AVI's solution space is a subset of VI's.

## Related pages
- [[Identifiability]] · [[Variational inference]] · [[Neural ODE]]
