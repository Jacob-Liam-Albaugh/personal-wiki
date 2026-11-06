---
type: paper
area: bayesian
areas: [bayesian, ml]
source-ref: "Kingma, Welling 2019, Found. Trends Mach. Learn. 12(4), ch. 1 and appendix A"
tags: [paper, bayesian, vi, generative, ml]
authors: [Kingma, Welling]
year: 2019
venue: "Foundations and Trends in Machine Learning, vol. 12, no. 4, pp. 307-392"
file: "Bayesian/Kingma, Welling - Intro to Variational Autoencoders.pdf"
---

# An Introduction to Variational Autoencoders (Kingma, Welling 2019)

**Summary**: A monograph that expands [[VAE paper (Kingma 2014)]] into a tutorial on variational autoencoders and deep latent-variable models. The PDF in this folder contains only the front matter, the motivation and background chapter (ch. 1) and the appendix (notation, MAP, variational EM, MCMC-EM, SGD). Chapters 2-5 (VAE/ELBO/reparameterization, flexible posteriors and IAF, deeper generative models, conclusion) listed in its table of contents are not in the file.

**Authors**: Diederik P. Kingma (Google), Max Welling (University of Amsterdam; Qualcomm) · **Year**: 2019 · **File**: `Bayesian/Kingma, Welling - Intro to Variational Autoencoders.pdf`

Page cites below use the monograph's own printed page numbers (ch. 1 on pp. 2-14, appendix pp. 67-73). The PDF is 44 pages; the text jumps from printed p. 14 straight to Acknowledgements (p. 65).

---

## Problem

Framing (§1.1, pp. 2-5): generative modeling is how science models the world; it encodes causal structure and physical constraints and treats unknowns as noise. The VAE couples two independently parameterized models, an encoder (recognition model) and a decoder (generative model), that "support each other" (p. 4). The recognition model is a stochastic function of the input, with one set of parameters shared by all datapoints; the authors call this amortized inference ([[Amortized VI]]). Classical VI uses a separate variational distribution per datapoint, which is inefficient for large data (p. 4). The cost of amortizing is sampling noise in the learning gradients, which the [[Reparameterization trick]] counteracts (p. 4). The VAE is positioned as inspired by the Helmholtz machine, whose wake-sleep algorithm did not optimize a single objective (p. 5). Versus GANs: GANs give sharper samples but lack full support; likelihood-based VAEs give more dispersed samples but better likelihoods (p. 5).

## Method

Everything the PDF contains is background for the VAE; the VAE objective itself is in the missing ch. 2.

**Models.** Unconditional $p_\theta(x)\approx p^*(x)$ (eqs. 1.1-1.2) or conditional $p_\theta(y|x)\approx p^*(y|x)$ (eq. 1.3). Neural networks parameterize conditional distributions: $\eta=\mathrm{NeuralNet}(\mathrm{Pa}(x))$, $p_\theta(x|\mathrm{Pa}(x))=p_\theta(x|\eta)$ (eqs. 1.7-1.8, p. 10); classification is a categorical on a softmax output (eqs. 1.4-1.5).

> [!definition] Directed graphical model
> $$p_\theta(x_1,\dots,x_M)=\prod_{j=1}^M p_\theta\big(x_j\,|\,\mathrm{Pa}(x_j)\big)$$
>
> (source: Kingma Welling Intro VAE, eq. 1.6, p. 9)

**Fully observed models.** For i.i.d. $D=\{x^{(i)}\}_{i=1}^N$, $\log p_\theta(D)=\sum_{x\in D}\log p_\theta(x)$ (eq. 1.10). Maximum likelihood by minibatch SGD uses the unbiased estimator
$$\tfrac1{N_D}\log p_\theta(D)\simeq\tfrac1{N_M}\sum_{x\in\mathcal M}\log p_\theta(x)$$
(eqs. 1.11-1.12, p. 11); "$\simeq$" means one side is an unbiased estimator of the other. ML is equivalent to minimizing a KL divergence between data and model distributions ([[KL divergence]], p. 10).

> [!definition] Deep latent variable model (DLVM)
> A latent-variable model $p_\theta(x,z)$ whose distributions are parameterized by neural networks. The simplest form is
> $$p_\theta(x,z)=p_\theta(z)\,p_\theta(x|z),\qquad p_\theta(x)=\int p_\theta(x,z)\,dz$$
> The marginal $p_\theta(x)$ is the model evidence. For discrete $z$ and Gaussian $p(x|z)$ it is a mixture of Gaussians, for continuous $z$ an infinite mixture; simple factors can give a very complex marginal.
>
> (source: eqs. 1.13-1.14, pp. 12-13)

> [!example] Binary-data DLVM used in the original VAE
> $$p(z)=N(z;0,I),\quad p=\mathrm{DecoderNeuralNet}_\theta(z)$$
> $$\log p(x|z)=\sum_{j=1}^D x_j\log p_j+(1-x_j)\log(1-p_j)$$
> with $p_j\in[0,1]$ from a sigmoid output (eqs. 1.15-1.18, p. 13; compare [[VAE paper (Kingma 2014)]] eq. 11).

**The intractability** (§1.8, pp. 13-14): $p_\theta(x)$ has no analytic form or efficient estimator, so it cannot be differentiated. Since $p_\theta(z|x)=p_\theta(x,z)/p_\theta(x)$ (eq. 1.19) and the joint is tractable, an intractable evidence means an intractable posterior and vice versa. Traditional approximate inference needs a per-datapoint optimization loop or gives poor approximations. The weight posterior $p(\theta|D)$ is also intractable (see [[Variational inference]]).

### Appendix methods

> [!algorithm] Variational EM with local variational parameters
> Per-datapoint parameters $\phi^{(i)}$:
> $$\phi^{(i)}\leftarrow\arg\max_\phi \mathcal L(x^{(i)};\theta,\phi)\quad\text{(E-step)}$$
> $$\theta\leftarrow\arg\max_\theta\sum_{i=1}^N \mathcal L(x^{(i)};\theta,\phi)\quad\text{(M-step)}$$
> The E-step equals $\arg\min_\phi D_{KL}(q_\phi(z|x)\|p_\theta(z|x))$ because $\mathcal L=\log p_\theta(x)-D_{KL}(\cdot)$. The M-step always optimizes a bound on the marginal likelihood, tight when $q_\phi=p_\theta(z|x)$. VAEs instead use global variational parameters.
>
> (source: eqs. A.6-A.10, p. 71; Neal and Hinton 1998 view of EM as coordinate ascent on the [[ELBO]])

> [!algorithm] MAP estimation
> $$\mathcal L_{MAP}(\theta)=\log p(\theta|D)=\log p(\theta)+\mathcal L_{ML}(\theta)+\text{const}$$
> The prior's effect diminishes with $N$, so for large data it is often dropped (equivalently $p(\theta)=$ const).
>
> (source: eqs. A.4-A.5, pp. 70-71)

MCMC-EM (§A.2.3, p. 72): approximate the posterior by samples from a Markov chain; posterior gradients are cheap in a DLVM because the evidence term drops out,
$$\nabla_z\log p_\theta(z|x)=\nabla_z\log p_\theta(x,z)$$
(eqs. A.11-A.14). Hamiltonian MCMC (Neal 2011) converges relatively fast but needs a chain per datapoint.

> [!algorithm] Stochastic gradient descent
> $$\theta_{t+1}\leftarrow\theta_t+\alpha_t\nabla_\theta\tilde{\mathcal L}(\theta,\xi),\qquad E_{\xi\sim p(\xi)}[\tilde{\mathcal L}(\theta,\xi)]=\mathcal L(\theta)$$
> $\xi$ may be a datapoint index or noise such as posterior-sampling noise in VAEs. The authors typically use Adam or Adamax (invariant to constant rescalings, so $\tilde{\mathcal L}$ need only be unbiased up to proportionality) and early stopping on held-out probability.
>
> (source: eq. A.15, pp. 72-73)

Bayesian inference reminder (§A.1.4, p. 70): $p(\theta|D)=p(D|\theta)p(\theta)/p(D)\propto p(D|\theta)p(\theta)$ (eq. A.3), with predictive $p(x'|D)=\int p_\theta(x')p(\theta|D)d\theta$.

## Results

None: this is an expository monograph. The only quantitative statements in the PDF are definitional (e.g. the ELBO as a KL gap, eq. A.9-A.10). Claims made in prose without data: GANs vs VAEs trade-off (p. 5); purely discriminative models usually win with enough data when the generative model is misspecified, but generative models help in semi-supervised settings (pp. 3, citing Kingma et al. 2014; Sønderby et al. 2016a).

## Limitations

- Stated: "not aimed to be a comprehensive review of all related work"; assumes basic algebra, calculus, probability (p. 6).
- Wiki note: the PDF here is incomplete. The ELBO derivation (§2.2), reparameterization (§2.4), factorized Gaussian posteriors (§2.5), the ELBO/marginal likelihood as KL divergences (§2.7), challenges (§2.8), normalizing flows and inverse autoregressive flow (ch. 3, §3.4), multi-latent models and follow-up work (ch. 4) are in the table of contents (pp. v-vi) but have no text here. Concept pages should cite [[VAE paper (Kingma 2014)]] for those, and not attribute chapter content to this file. Re-obtain a full copy before ingesting chapters 2-4 (**[unverified]** whether a complete PDF exists elsewhere in the folder).

## Connections

- Expanded version of [[VAE paper (Kingma 2014)]] (p. 6). Reference list also cites [[Variational dropout (Kingma 2015)]] (NIPS 2015, pp. 2575-2583) and Molchanov et al. 2017 on sparsifying variational dropout.
- Contents list (not text) shows the book covers [[Normalizing flows]] for posteriors beyond Gaussians (IAF, Sylvester flows cited in the references), the thread to [[Amortized VI]] work for inverse problems.
- The MCMC-EM discussion relates the VAE to MCMC-based alternatives; see [[SGLD]], [[SGLD (Welling 2011)]] for SG-MCMC over network weights.
- Wiki note: the references include Sohl-Dickstein et al. 2015 (nonequilibrium thermodynamics), the diffusion-model precursor; see [[Diffusion models]]. Mentioned only as a reference-list entry in this PDF.

**Sources**: `Bayesian/Kingma, Welling - Intro to Variational Autoencoders.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[VAE]]
- [[Amortized VI]]
- [[ELBO]]
- [[Reparameterization trick]]
- [[Variational inference]]
- [[KL divergence]]
- [[Normalizing flows]]
- [[VAE paper (Kingma 2014)]]
- [[Variational dropout (Kingma 2015)]]
- [[Diffusion models]]
- [[SGLD]]
