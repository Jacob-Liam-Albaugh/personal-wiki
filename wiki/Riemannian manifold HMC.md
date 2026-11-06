---
type: method
area: stochastic
areas: [stochastic]
source-ref: "Girolami & Calderhead 2011, §3-4"
tags: [sampling, mcmc, bayesian]
---

# Riemannian manifold HMC

**Summary**: Hamiltonian Monte Carlo with a position-dependent mass matrix $G(\theta)$, usually the Fisher metric. The kinetic energy becomes non-separable, so the integrator must be the implicit generalized leapfrog. The metric adapts steps to local posterior curvature.

> [!definition] Hamiltonian
> $$H = -L(\theta) + \tfrac12 \log\left\{(2\pi)^D |G(\theta)|\right\} + \tfrac12 p^{\top} G(\theta)^{-1} p$$
> with $p \mid \theta \sim N(0, G(\theta))$ (source: Girolami 2011, eq. 13).

## Key points

- Standard [[Hamiltonian Monte Carlo]] is the special case $G = M$ constant.
- The simpler relative is MMALA: one Langevin step preconditioned by $G^{-1}$, Metropolis-corrected.
- Generalized leapfrog (eq. 16-18) is implicit, solved by fixed-point iteration; it is symmetric and symplectic, so the Metropolis accept step $\min[1,e^{-H^*+H}]$ is valid.
- Any positive definite $G$ gives a correct sampler; Fisher-based $G$ gives good mixing.
- Cost: metric solve $O(N^3)$ worst case, plus derivatives of $G$. MMALA wins when the metric is expensive (FitzHugh-Nagumo example).

Wiki note: in large neural networks the full metric is infeasible, which is why stochastic-gradient samplers ([[SGLD]], [[SGHMC]]) and diagonal preconditioners ([[Adam]]) dominate.

**Sources**: `papers/ML/Girolami, Calderhead - Riemann Manifold Langevin & Hamiltonian Monte Carlo Methods.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[RMHMC (Girolami 2011)]]
- [[Hamiltonian Monte Carlo]]
- [[Markov chain Monte Carlo]]
- [[SGLD]]
- [[SGHMC]]
- [[Langevin dynamics]]
- [[Metropolis-Hastings correction]]
- [[Riemannian convergence (Sormani 2011)]]
