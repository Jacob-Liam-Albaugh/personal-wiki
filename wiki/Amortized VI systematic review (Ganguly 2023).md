---
type: paper
area: bayesian
areas: [ml]
source-ref: "Ganguly, Jain, Watchareeruetai 2023, JAIR 78:167-215"
tags: [bayesian, vi, ml, generative]
authors: ["[[Ankush Ganguly]]", "[[Sanjana Jain]]", "[[Ukrit Watchareeruetai]]"]
year: 2023
venue: "Journal of Artificial Intelligence Research 78 (2023) 167-215"
file: "[[papers/Bayesian/Ganguly, Jain, Watchareeruetai - Amortized Variational Inference A Systematic Review.pdf]]"
---

# Amortized VI systematic review (Ganguly 2023)

**Summary**: Review that builds amortized VI from traditional (CAVI), stochastic (natural-gradient) and black-box VI, then covers four known problems of amortization (amortization gap, inconsistent representations, generalization gap, posterior collapse) and alternatives to reverse KL (chi, Renyi alpha, Stein). Mostly VAE-centred; it is a survey, with no experiments of its own.

**Authors**: Ankush Ganguly, Sanjana Jain, Ukrit Watchareeruetai (Sertis Vision Lab, Bangkok) · **Year**: 2023 · **File**: [[papers/Bayesian/Ganguly, Jain, Watchareeruetai - Amortized Variational Inference A Systematic Review.pdf]]

---

## Problem

Exact posteriors $p(z\mid x;\theta)=p(x\mid z;\theta)p(z;\theta)/p(x;\theta)$ are intractable (eq. 1); MCMC is slow. VI turns inference into optimisation and also yields a bound on the evidence (§2.1-2.2). Traditional VI adds local parameters $\xi_i$ per datum, so cost grows with $N$ and new points need a fresh optimisation.

## Method

> [!definition] Traditional VI objective and ELBO (source: file, eqs. 2-7)
> $$D=\sum_{i=1}^N D_{KL}\big(q(z|x_i;\xi_i)\,\|\,p(z|x_i;\theta)\big),\qquad \log p(x;\theta)=\mathcal L(x;\xi_{1:N},\theta)+D$$
> $$\mathcal L=\sum_i\mathbb E_q\big[\log p(x_i,z;\theta)-\log q(z|x_i;\xi_i)\big]\le\log p(x;\theta).$$
> See [[ELBO]], [[KL divergence]], [[Variational inference]].

- **Mean field and CAVI** (§2.4-2.5, eqs. 8-9, Alg. 1): factorised $q$, coordinate ascent finds a local optimum, sensitive to initialisation, one full pass per iteration.
- **SVI** (§3, Alg. 2): minibatch estimate $\mathcal L\simeq\frac NM\hat{\mathcal L}(x_M)$ (eq. 10), natural gradients $\bar\nabla=I(\xi)^{-1}\nabla$ via the Fisher matrix (eqs. 11-12); variance control by batch size, adaptive rates ([[Adam]]), control variates.
- **Black-box VI** (§4): score-function gradient (eqs. 13-14), high variance; the [[Reparameterization trick]] $z=g_\phi(\epsilon,x_i)$ gives the lower-variance estimator $\tilde{\mathcal L}$ (eqs. 15-16) but does not extend to discrete $z$.

> [!definition] Amortized ELBO (source: file, eq. 17, §5)
> $$\mathcal L(x;\phi,\theta)=\sum_{i=1}^N\mathbb E_{q_\phi}\big[\log p(x_i,z;\theta)-\log q(z|x_i;\phi)\big],$$
> with one shared encoder $\phi$ for all data, minibatch form eq. 18, Alg. 3. See [[Amortized VI]]; Fisher inversion costs $O(d^3)$ so diagonal or Adam-style second moments are used.

> [!definition] VAE ELBO and SGVB estimator (source: file, eqs. 19-21, §5.1)
> $$\mathcal L=\sum_i\Big[\mathbb E_{q_\phi}\log p(x_i|z;\theta)-D_{KL}\big(q(z|x_i;\phi)\|p(z;\theta)\big)\Big].$$
> Gaussian encoder $q=N(\mu_i,\sigma_i^2I)$ gives the closed-form KL $\tfrac12\sum_j(1+\log\sigma_{ij}^2-\mu_{ij}^2-\sigma_{ij}^2)$ (eq. 21). See [[VAE]], [[VAE paper (Kingma 2014)]].

- **IWAE** (eq. 22): $K$-sample importance-weighted bound; biased for $\log p$ with bias $O(1/K)$ (Nowozin); L-MCVAE gives an unbiased evidence estimate; PIWAE/MIWAE/CIWAE (Rainforth) use different tightness for encoder and decoder.

### Caveats of amortization (§5.2)

> [!failure] Amortization gap and inference gap (source: file, §5.2.1)
> Inference gap $=\log p(x)-\mathcal L$ = approximation gap (family too small, e.g. mean field) + amortization gap (encoder capacity: one function for all $x_i$). Cremer et al.: on complex data the amortization gap is a large part of the inference gap. Remedies: [[Normalizing flows]] (eq. 23) and hierarchical auxiliary variables for the family; iterative refinement (Hjelm EM refinement, Marino iterative encoding of gradients, Kim semi-amortized SA-VAE with extra SVI steps, Kim-Pavlovic single-pass noise model).

- **Inconsistent representations** (§5.2.2): fitted encoders map an input and its semantics-preserving transform to different codes. CR-VAE adds $\mathbb E_t[\mathcal L(\tilde x)-\lambda R]$ with $R=\mathbb E_t D_{KL}(q(z|\tilde x_i)\|q(z|x_i))$ (eq. 24); AVAE makes encoder and decoder consistent on generated samples.
- **Generalization gap** (§5.2.3): over-expressive encoder overfits, low capacity raises the amortization gap. Shu et al. amortized inference regularization (DVAE noise injection, weight-normalized inference) lowers the test inference gap; Zhang et al. self-consistent training mixes generated samples into encoder training.
- **Posterior collapse** (§5.2.4): $q\to p(z)$, KL term $\to0$, decoder ignores $z$. Fixes: weaker decoder, adapted ELBO (Takida), delta-VAE minimum KL, Batch-Normalized VAE.

### Beyond reverse KL (§6)
- Reverse KL is zero-forcing, underestimates variance, can prune units.
- **CHIVI** (eqs. 26-27): $D_{\chi^r}=\mathbb E_q[(p/q)^r-1]$, $\text{CUBO}_r=\frac1r\sum\log\mathbb E_q[(p(z,x_i)/q)^r]\ge\log p(x)$, an evidence upper bound; $r\to0$ recovers the ELBO.
- **Renyi alpha** (eqs. 28-29): $D_\alpha=\frac1{\alpha-1}\log\int q^\alpha p^{1-\alpha}$, variational Renyi bound $\mathcal L_\alpha$; for $\alpha_+\in(0,1)$, $\alpha_-<0$: $\mathcal L<\mathcal L_{\alpha_+}<\log p<\mathcal L_{\alpha_-}$, sandwiching the evidence. f-divergences eq. 30.
- **Stein discrepancy** (eq. 31) with Stein operator $\mathcal Ag=g\nabla\log p+\nabla g$ (no normaliser needed); kernelised version underlies [[SVGD]]; also a goodness-of-fit test.

## Results

A review; no new experiments. It reports evaluation outcomes of cited work only. Evaluation quantities named: the ELBO, the log marginal likelihood or its bounds, the inference/approximation/amortization gaps, test-set log-likelihood, negative ELBO on MNIST, adversarial accuracy and latent-space consistency (§2.3, §5.2, §6).

## Limitations

As stated (§7): VAEs do not treat posterior uncertainty in a principled way (Bayesian NN encoders/decoders proposed); latent geometry is poorly understood; the ELBO is non-convex (Variational Holder bound, a convex upper bound, is proposed as an alternative); probabilistic programming tools are still hard for newcomers. Wiki note: emphasis is VAE image modelling; inverse-problem uses and theory of when amortization costs nothing are not covered (see [[Amortized VI when and why (Margossian 2024)]]), and Section 5.1 states eq. 19 sums per-datum ELBOs under an i.i.d. assumption only.

## Connections

- Survey companion to [[Amortized VI when and why (Margossian 2024)]] (theory of the amortization gap) and [[Amortized VI for inverse problems (Karumuri 2024)]] (amortization over simulated datasets with Gaussian and flow guides; Karumuri's "no amortization gap" assumption is this review's amortization gap closing).
- VAE background: [[VAE paper (Kingma 2014)]], [[Intro to VAEs (Kingma 2019)]], [[VAE]].
- Gradient estimators: [[Reparameterization trick]], [[Local reparameterization trick]]; richer guides: [[Normalizing flows]]; particle alternative: [[SVGD]]; sampling alternative: [[Markov chain Monte Carlo]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Cyclical SG-MCMC (Zhang 2020)]], [[GAN paper (Goodfellow 2014)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[Amortized VI for inverse problems (Karumuri 2024)]], [[Amortized VI when and why (Margossian 2024)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Ganguly, Jain, Watchareeruetai - Amortized Variational Inference A Systematic Review.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[Amortized VI]]
- [[Variational inference]]
- [[ELBO]]
- [[KL divergence]]
- [[VAE]]
- [[Reparameterization trick]]
- [[Normalizing flows]]
- [[SVGD]]
- [[Adam]]
