---
type: paper
area: bayesian
areas: [bayesian, gp, ml]
source-ref: "Fortuin 2022 (arXiv:2105.06868v3), eqs. 8-11, 24, 30-34, 36"
tags: [bayesian, ml]
authors: ["[[Vincent Fortuin]]"]
year: 2022
venue: "arXiv preprint (stat.ML), v3 18 Mar 2022"
file: "papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf"
---

# Priors in Bayesian Deep Learning (Fortuin 2022)

**Summary**: A review of how priors are chosen, designed and learned for Gaussian processes, deep generative models (VAEs) and Bayesian neural networks. It argues that the prior is the least examined part of Bayesian deep learning, that the default isotropic Gaussian is not uninformative and can be actively harmful, and surveys structured, function-space and learned alternatives. It is a review with no experiments.

**Authors**: Vincent Fortuin (ETH Zurich) · **Year**: 2022 · **File**: `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`

---

## Problem

Bayesian deep learning rests on Bayes' rule and the posterior predictive (eqs. 1-2, p. 1), which is a form of [[Bayesian model averaging]]. Most work targets approximate inference; the prior receives little thought and is usually an isotropic Gaussian on weights (§1). The review argues:

- Gaussian weight priors are not uninformative in function space, and Bernstein-von-Mises-type guarantees can fail for neural nets (§1).
- Marginal-likelihood and decision-theoretic justifications (Dutch book, Savage) degrade under prior misspecification (§1).
- Misspecification is a candidate explanation of the cold posterior effect, where tempered posteriors $p(\theta|D)^{1/T}$ with $T<1$ outperform the Bayes posterior (§1, §4).

The paper's scope: GPs (§2), VAEs (§3), BNNs (§4), and learning priors from data (§5).

## Method

This is a survey; the "method" is its taxonomy. Equation numbers follow the paper.

**§2 Gaussian processes.** A GP prior (eq. 4) gives a closed-form posterior predictive (eq. 6, p. 3). Prior design is through the kernel: standard kernels, kernel composition, spectral kernels, and deep kernels $k(x,x')=k_{base}(\phi(x),\phi(x'))$ (eq. 7). Infinite-width neural networks give GPs:

> [!definition] NNGP kernel
> For one hidden layer, $k_{NN}(x,x')=\sigma_w^2\,\mathbb{E}\big[\varphi(w^\top x+b)\varphi(w^\top x'+b)\big]+\sigma_b^2$, and recursively for depth,
> $$k^{\ell}(x,x')=\sigma_w^2\,\mathbb{E}_{z\sim\mathcal{N}(0,K^{\ell-1})}\big[\varphi(z_1)\varphi(z_2)\big]+\sigma_b^2$$
> (source: `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`, eqs. 8-9, pp. 4-5)

> [!definition] Neural tangent kernel
> The NTK is $k=JJ^\top$ with $J$ the parameter Jacobian of the network output, with the layerwise recursion $k^{\ell}=k^{\ell-1}\dot\Sigma+\Sigma$ (source: eqs. 10-11, p. 5; the recursion form as I recorded it, check against the PDF before relying on the exact $\dot\Sigma$ convention **[unverified]**).

Deep GPs and their priors are also covered (§2).

**§3 VAE priors.** The VAE objective is the [[ELBO]] (eq. 12, p. 6). Priors are split into distributional alternatives to $\mathcal{N}(0,I)$ and structural ones:

- von Mises-Fisher (eq. 13) and power-spherical (eq. 14), Gaussian mixture (eq. 15);
- GP prior across the latent matrix (eq. 16), hierarchical priors (eqs. 17-18), discrete VQ-VAE codes (eq. 19), neural-process priors (eq. 20).

The vMF prior helps mostly at latent dimension $d\lesssim 20$ (§3).

**§4 BNN priors.**

*Weight-space priors* (§4.1): matrix-normal (eq. 21), scale-mixture hyperpriors (eq. 22), inverse-Wishart (eq. 23), giving heavy-tailed marginals:

> [!definition] Student-t weight prior from a Gamma precision
> A Gaussian prior with a Gamma hyperprior on the precision integrates to a Student-t marginal on the weights (source: eqs. 22-24, p. 9). Zhu and Zabaras use this construction in [[Bayesian DenseED surrogate (Zhu 2018)]].

Other weight-space designs: horseshoe (eqs. 25-26), radial-directional (eq. 27), unit-based implicit priors (eq. 28), and implicit priors $p(\theta)=g(z,\varepsilon)$ (eq. 29). Heavy-tailed or correlated priors reduce the cold posterior effect (p. 9).

*Function-space priors* (§4.2): place the prior on the output function, for example a GP, with a KL objective in function space (eq. 30), output-constraint priors (eq. 31) and noise-contrastive priors (eq. 32). Function-space KL between a GP and a BNN is infinite or undefined because the supports differ, so Wasserstein distance is proposed instead (p. 11). Related to [[Physics-informed prior]] (Wiki note).

*Ensembles* (§4.3): deep ensembles as an approximation to the posterior predictive (eq. 33):

> [!algorithm] SVGD update
> $$\theta_i\leftarrow\theta_i+\eta\,\phi(\theta_i),\qquad
> \phi(\theta_i)=\sum_{j}\Big[k(\theta_i,\theta_j)\nabla_{\theta_j}\log p(\theta_j|D)-\nabla_{\theta_i}k(\theta_i,\theta_j)\Big]$$
> (source: eq. 34, p. 12). The kernel term gives a repulsive force between ensemble members. See [[SVGD]].

Gradient-guided MCMC for BNNs is cited at p. 10 ([[SG-MCMC]]).

**§5 Learning priors.**

- Empirical Bayes: optimise the GP marginal likelihood over prior hyperparameters (eq. 35).
- Meta-learning a prior over tasks (eq. 36).
- For VAEs, the ELBO decomposes as $\mathbb{E}\log p(x|z)-I(z;x)-KL(\bar q\|p)$ (eq. 37), which motivates learned priors: VampPrior (eq. 38), flow priors (eq. 39, see [[Normalizing flows]]) and learned acceptance priors (eq. 40).
- For BNNs, a Laplace-GGN estimate of the marginal likelihood (eq. 41, p. 14) and augmentation-invariance-based prior learning (eq. 42, p. 15).
- Learned mixture priors can overfit; the VampPrior is reported to avoid this (§5).

## Results

There are no experiments. Claims the review reports from the literature, with pages:

- Heavy-tailed or correlated weight priors reduce the cold posterior effect (p. 9).
- vMF latent priors help mostly when the latent dimension is $\lesssim 20$ (§3).
- GP-to-BNN function-space KL is infinite or undefined (support mismatch); Wasserstein is proposed instead (§4.2, p. 11).
- Learned mixture priors can overfit; the VampPrior avoids this (§5).

Wiki note: the review gives no quantitative comparison across prior families, so it cannot say which prior to pick for a given problem.

## Limitations

- The author notes the survey is necessarily incomplete.
- Review only: no new method, no benchmark.
- Venue of final publication is not stated in the PDF; a later journal version is **[unverified]**. The text speaks of "this thesis", so it appears to be a chapter extract (Wiki note).

## Connections

- Weight-space process prior in [[SDE-BNN (Xu 2022)]]: an OU process over depth is a stochastic-process prior on weights, not one of the families surveyed here (Wiki note).
- [[Bayesian DenseED surrogate (Zhu 2018)]] uses a Gamma-Gaussian (Student-t) weight prior (eq. 24 here) and SVGD (eq. 34 here), and lists other priors as future work.
- General background: [[Bayesian neural networks]], [[Variational inference]], [[KL divergence]], [[Gaussian process]], [[Normalizing flows]], [[Bayesian model averaging]], [[SG-MCMC]].
- Function-space prior ideas connect to [[Physics-informed prior]] (Wiki note).

%% refs:start %%
**Cites in this wiki**: [[Cyclical SG-MCMC (Zhang 2020)]], [[Dropout paper (Srivastava 2014)]], [[VAE paper (Kingma 2014)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Bayesian neural networks]]
- [[Gaussian process]]
- [[ELBO]]
- [[Variational inference]]
- [[KL divergence]]
- [[Normalizing flows]]
- [[SVGD]]
- [[SG-MCMC]]
- [[Bayesian model averaging]]
- [[Physics-informed prior]]
- cold posterior effect
- function space prior
- [[SDE-BNN (Xu 2022)]]
- [[Bayesian DenseED surrogate (Zhu 2018)]]
