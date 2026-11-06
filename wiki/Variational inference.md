---
type: method
area: bayesian
areas: [bayesian, ml]
source-ref: "Margossian & Blei 2024, eq. 1; Tsilifis et al. 2014, eq. 14; Kingma et al. 2015, eqs. 1-2"
tags: [bayesian, vi]
---

# Variational inference

> [!algorithm] Variational inference
> Pick a tractable family $\mathcal Q$ and solve
> $$q^*=\arg\min_{q\in\mathcal Q}\mathrm{KL}\big(q(\theta,z)\,\|\,p(\theta,z\mid x)\big),$$
> equivalently maximise the [[ELBO]] $\mathcal F[q]$.
>
> (source: `papers/Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`, eq. 1)

**Intuition**: replace sampling from the posterior with optimisation over a family of simple distributions. The answer is only as good as the family, and the reverse-KL objective is mode-seeking, so a unimodal family locks onto one mode of a multimodal posterior.

## Variants
- **Factorized (F-VI)**: one set of parameters $\nu_n$ per latent (Margossian & Blei).
- **Amortized**: a learned map from data to variational parameters, see [[Amortized VI]].
- **Global weights**: $q_\phi(w)$ over network weights, gradients via the [[Reparameterization trick]] (Kingma et al. 2015, eqs. 1-3), the basis of [[Variational dropout]].
- **Particle**: [[SVGD]] transports a particle set by the KL steepest-descent direction.
- **Path space**: ELBO over SDE path measures (Xu et al. 2022, eq. 1).

## Failure modes
- Mode-seeking reverse KL: Karumuri et al.'s Gaussian guide misses the second mode of the inverse-kinematics posterior; a [[Normalizing flows]] guide recovers it (p. 30).

## Where it appears
- [[Variational inverse problems (Tsilifis 2014)]]: Gaussian-mixture family, analytic ELBO, one run per dataset.
- [[Amortized VI for inverse problems (Karumuri 2024)]]: amortized Gaussian and flow guides.
- [[Amortized VI when and why (Margossian 2024)]]: when amortized matches factorized.
- [[VAE paper (Kingma 2014)]] · [[Variational dropout (Kingma 2015)]] · [[Intro to VAEs (Kingma 2019)]] (variational EM, App. A).
- [[SDE-BNN (Xu 2022)]] (path-space VI) · [[Bayesian DenseED surrogate (Zhu 2018)]] (SVGD as VI).
- Sparse variational GPs for large-data surrogates: [[Surrogate model]].
- Book chapter on guide families (diagonal, low-rank, full-rank Cholesky, transformed, Gamma/Beta, composite), KL non-negativity by Jensen, ELBO derivation and reparameterized gradients. (source: `inverse/vi/01_basics.md`)
- Full-rank Gaussian guide on [[Catalysis problem]] with 27 parameters, fitted with minibatch ELBO estimates and compared with the [[Laplace approximation]] result. (source: `inverse/vi/02_catalysis.ipynb`)
- Wiki note: the book's low-rank covariance $\sum_{i\le k}e^{\lambda_i}u_iu_i^T$ with $k<d$ is singular, so it has no density unless a diagonal term is added. (source: `inverse/vi/01_basics.md`)
- Wiki note, vi/01: "Example 1 ... univariate Gaussian" shows a multivariate Gaussian, and "Example 2 multivariate" shows the transformed guide (titles swapped).
- Wiki note, vi/02: the text says $\lambda=1/0.1$ but the code uses `lambda_=1/0.005`; the text says $\mu_\phi\in\mathbb R_+^5$ although it is six real numbers; `k_transformation` is defined but `T` uses `exp(gamma*x)`; the text's $\tilde k=180k/500$ is only a time rescaling for a linear system.

## Examples

> [!example] Homework 6, problems 2-3 (source: homework/06_homework.ipynb)
> Rank-$k$ covariance parameterization is positive semi-definite, multi-point convexity, Jensen's inequality. Then mean-field and full-rank Gaussian VI for the acetaminophen model.

**Covered in**: ASML book inverse/vi (ME 697 4.3); homework 6
**Sources**: `papers/Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`, `papers/Bayesian/Bilionis, Tsilifis - Variational Reformulation of Bayesian Inverse Problems.pdf`, `papers/Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`, `courses/ME 697/advanced-scientific-machine-learning/book/inverse/vi/intro.md`, `01_basics.md`, `02_catalysis.ipynb`, `03_3d_reconstruction.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ELBO]] · [[KL divergence]] · [[SG-MCMC]] · [[Bayesian inverse problems]]
