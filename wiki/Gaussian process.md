---
type: concept
area: gp
areas: [gp, bayesian]
source-ref: "Fortuin 2022, eqs. 4, 6, 8-11, 35"
tags: [gp, bayesian]
---

# Gaussian process

**Summary**: a prior over functions, $f\sim\mathcal{GP}(m,k)$, under which any finite set of values is jointly Gaussian; with Gaussian noise the posterior predictive is closed form.

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

## Related pages
- [[Random features model]] (kernel link, Kovachki et al. 2024 p. 11) · [[Bayesian neural networks]] · [[Information field theory]]
