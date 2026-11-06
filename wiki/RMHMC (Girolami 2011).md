---
type: paper
area: stochastic
areas: [stochastic]
source-ref: "Girolami & Calderhead 2011, JRSS B 73(2):123-214, §2-4, §6"
tags: [sampling, mcmc, bayesian]
authors: ["[[Mark Girolami]]", "[[Ben Calderhead]]"]
year: 2011
venue: "J. R. Statist. Soc. B 73 (2011) 123-214"
file: "ML/Girolami, Calderhead - Riemann Manifold Langevin & Hamiltonian Monte Carlo Methods.pdf"
---

# RMHMC (Girolami 2011)

**Summary**: Treats the parameter space as a Riemannian manifold whose metric $G(\theta)$ is the expected Fisher information (plus prior curvature). A position-dependent metric rescales and rotates the proposal, so Langevin and Hamiltonian samplers adapt to local correlation. This gives MMALA and Riemannian manifold HMC, which mix far better than plain MALA and HMC on strongly correlated or ill-conditioned posteriors.

**Authors**: Mark Girolami, Ben Calderhead · **Year**: 2011 · **File**: `ML/Girolami, Calderhead - Riemann Manifold Langevin & Hamiltonian Monte Carlo Methods.pdf`

---

## Problem

Plain MALA and HMC use one global step size and a fixed (often identity) mass matrix. Posteriors with strong, location-dependent correlation force tiny steps in the narrow directions (source: Girolami 2011, §1-2). Hand-tuned global preconditioning cannot fix curvature that changes across the space.

## Method

Let $L(\theta)$ be the log joint density. Pick a metric $G(\theta)$.

> [!definition] Metric tensor
> $$G(\theta) = \mathbb{E}\left[ \nabla L \, \nabla L^{\top} \right] - \nabla\nabla^{\top} \log p(\theta)$$
> The expected Fisher information plus the negative Hessian of the log prior. Any positive definite $G$ is admissible (source: Girolami 2011, §3).

Wiki note: correctness never depends on this choice, because every proposal is Metropolis-corrected. The metric only affects efficiency.

**Natural gradient.** The steepest direction under the metric is $G^{-1}\nabla L$ (source: Girolami 2011, §3).

**MMALA** (simplified manifold Langevin). The proposal is a Langevin step preconditioned by $G$ (the full form adds a term from the derivative of $G$):

$$\theta^{*} = \theta + \tfrac{\epsilon^2}{2} G^{-1}\nabla L + \epsilon \sqrt{G^{-1}}\, z$$

with $z \sim N(0, I)$. It is accepted by Metropolis-Hastings. The IWLS sampler for generalized linear models equals this simplified MMALA (source: Girolami 2011, §4).

**RMHMC.** Draw momentum from a position-dependent Gaussian:

$$p \mid \theta \sim N(0, G(\theta))$$

> [!definition] Riemannian Hamiltonian (eq. 13)
> $$H(\theta,p) = -L(\theta) + \tfrac12 \log\left\{(2\pi)^D |G(\theta)|\right\} + \tfrac12 p^{\top} G(\theta)^{-1} p$$
> The log-determinant term makes the marginal over $\theta$ equal to the target. $H$ is not separable, since the kinetic term depends on $\theta$.

Hamilton's equations (eq. 14-15) then have $\theta$-dependence in the $p$ flow. The flows are locally geodesic (source: Girolami 2011, §4).

> [!algorithm] Generalized leapfrog (eq. 16-18)
> 1. Half step in $p$, implicit in $p$ (solve by fixed-point iteration, 5-6 iterations typical).
> 2. Full step in $\theta$, implicit in $\theta$ (also fixed-point).
> 3. Half step in $p$, explicit.
>
> The scheme is symmetric and symplectic, so it is reversible and volume preserving. Accept with probability $\min[1, \exp(-H^{*} + H)]$.

A naive leapfrog fails on a non-separable $H$: it is neither reversible nor volume preserving. Zlochin and Baram's earlier manifold HMC attempt failed for this reason (source: Girolami 2011, §4).

A Gibbs variant (eq. 19-20) alternates momentum resampling with the leapfrog trajectory.

> [!example] Normal model
> For $N$ observations with unknown mean and standard deviation, the Fisher metric is $G = \mathrm{diag}(N/\sigma^2,\ 2N/\sigma^2)$. This is a hyperbolic upper half-plane, so geodesics are curved, and the proposal scale shrinks as $\sigma$ shrinks (source: Girolami 2011, §3).

## Results

- **Bayesian logistic regression**, $G = X^{\top}\Lambda X + \alpha^{-1} I$, five data sets, 5000 burn-in plus 5000 samples, 10 runs, minimum ESS reported. On Australian credit, RMHMC gives min/median/max ESS of (4975, 5000, 5000) from 5000 samples; German credit (4757, 5000, 5000) (source: Girolami 2011, §6.1; other rows garbled in extraction).
- **Stochastic volatility** with a sparse metric structure (§6.2).
- **Log-Gaussian Cox process**: RMHMC samples the latent field directly with no reparameterization (§6.3).
- **FitzHugh-Nagumo ODE**: MMALA is best because the metric (sensitivities) is expensive, so RMHMC's extra metric derivatives cost more than they return (§6.4).

## Limitations

- Needs an analytic metric and its derivatives.
- Worst-case $O(N^3)$ cost for metric inversion each step; impractical beyond roughly 100 covariates for logistic regression (source: Girolami 2011, §7).
- Fixed-point iterations in the generalized leapfrog add cost per step.
- Skilling's discussion remark: rough submanifolds may not suit a smooth metric (discussion section).

## Connections

- The reference method for [[Riemannian manifold HMC]]; builds on [[Hamiltonian Monte Carlo]] and [[Markov chain Monte Carlo]].
- The Langevin step is the Metropolis-corrected cousin of [[SGLD]]; see also [[SGHMC]].
- Metric from the Fisher matrix: the same natural-gradient idea that [[Adam paper (Kingma 2015)]] approximates with a diagonal second-moment estimate (Wiki note).
- Gaussian and Bayesian-neural-network posteriors are the use case at scale: [[Gaussian process]], [[Bayesian neural networks]].

%% refs:start %%
**Cited by in this wiki**: [[SGLD (Welling 2011)]]
%% refs:end %%

**Sources**: `ML/Girolami, Calderhead - Riemann Manifold Langevin & Hamiltonian Monte Carlo Methods.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Riemannian manifold HMC]]
- [[Hamiltonian Monte Carlo]]
- [[Markov chain Monte Carlo]]
- [[SGLD]]
- [[SGHMC]]
- [[Bayesian neural networks]]
