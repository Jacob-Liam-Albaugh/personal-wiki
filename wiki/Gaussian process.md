---
type: concept
area: gp
areas: [gp, bayesian]
source-ref: "Fortuin 2022, eqs. 4, 6, 8-11, 35"
tags: [gp, bayesian]
---

# Gaussian process

**Summary**: a prior over functions, $f\sim\mathcal{GP}(m,k)$, under which any finite set of values is jointly Gaussian; with Gaussian noise the posterior predictive is closed form.

## Connections
- GP posterior mean equals kernel ridge regression when the noise variance equals n times the ridge parameter; the posterior standard deviation equals the worst-case error over the RKHS unit ball (source: Kanagawa 2018, Props 3.6 and 3.10, pp. 21, 26). See [[Gaussian processes and kernel methods (Kanagawa 2018)]].
- GP draws are almost surely not in the RKHS of their own kernel when it is infinite dimensional, but lie in a slightly larger power space (source: Kanagawa 2018, Cor 4.10, Thm 4.12, pp. 33-36).
- kernels are built from sums, products and changepoints, and the structure can be searched automatically (source: Duvenaud 2014, chs. 2-3). See [[Kernel composition]], [[Duvenaud thesis (Duvenaud 2014)]].
- GP regression on a bounded domain can be run at O(N m^2) with a truncated KL basis computed once by Nystrom quadrature (source: Greengard-O'Neil 2022, Alg. 1, p. 6). See [[Reduced-rank GPs (Greengard 2022)]].
- a two-fidelity GP surrogate for a tissue model is in [[Multi-fidelity GP for tissue expansion (Lee 2020)]].

**Sources**: `Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`.
**Last updated**: 2026-11-06

---

## Posterior predictive (Fortuin eq. 6)
With training inputs $X$, outputs $y$, noise $\sigma^2$, $K=k(X,X)$, $k_*=k(X,x_*)$:
$$\mu_*=k_*^\top(K+\sigma^2I)^{-1}y$$
$$\sigma_*^2=k(x_*,x_*)-k_*^\top(K+\sigma^2I)^{-1}k_*$$
Hyperparameters fit by maximising the marginal likelihood (eq. 35).

## Links to neural networks
- Infinite-width networks are GPs with the NNGP kernel (eqs. 8-9):
  $$k^\ell=\sigma_w^2\,\mathbb E_{z\sim N(0,K^{\ell-1})}[\varphi(z_1)\varphi(z_2)]+\sigma_b^2$$
- Gradient-descent training in that limit follows the neural tangent kernel $k=JJ^\top$ (eqs. 10-11; recursion detail **[unverified]**).

## Where it appears
- [[Priors in Bayesian deep learning (Fortuin 2022)]] (GP priors and infinite-width limits).
- [[Bayesian DenseED surrogate (Zhu 2018)]]: GPs as the surrogate baseline that scales badly in input dimension; the input field itself is a GP sampled by [[Karhunen-Loève expansion]].
- [[Physics-informed ML review (Karniadakis 2021)]] — GP kernels as inductive bias and GP uncertainty for active learning (pp. 4, 9).
- [[Neural tangent kernel]] — infinite-width networks behave as kernel regression.
- [[Wiener process]] is the GP with kernel $s\wedge t$; KL expansion samples GPs ([[Karhunen-Loève expansion]], [[Mercer's theorem]]).
- First-order propagation of Gaussian parameter uncertainty through an ODE gives a vector-valued GP with covariance $\nabla_\theta x\,\Sigma\,\nabla_\theta x^T$: [[Local sensitivity analysis of ODEs]] (source: `up/sensitivity_analysis/01_theory.md`).
- GP surrogates, exact versus sparse variational: [[Surrogate model]], [[ME697 2.3 - Surrogates]].
- Multi-fidelity GPs (Kennedy-O'Hagan and nonlinear): [[Multi-fidelity modeling]], [[ME697 2.4 - Multi-fidelity modeling]].
- GP with uncertainty sampling for active learning: [[Active learning]].
- GP as random-field input to a PDE, expanded by KLE: [[ME697 3.1 - Functional inputs]].

## Related pages
- [[Random features model]] (kernel link, Kovachki et al. 2024 p. 11) · [[Bayesian neural networks]] · [[Information field theory]]
- Fourier-feature networks in the NTK regime behave like kernel regression with a stationary kernel set by B (Tancik 2020). Link [[Fourier features]].
- [[Kernel methods]], [[RKHS]], [[Kernel composition]], [[Multi-fidelity Gaussian process]].
- Field-valued unknowns in the planned PDE inverse problems (empty in the book): [[ME697 4.6 - PDE inverse problems]].
