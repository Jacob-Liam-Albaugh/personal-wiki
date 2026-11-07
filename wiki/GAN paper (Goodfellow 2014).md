---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Goodfellow et al. 2014, NeurIPS, eqs. 1-6, Prop. 1-2, Thm 1, Alg. 1, Table 1"
tags: [generative, ml]
authors: ["[[Ian J. Goodfellow]]", "[[Jean Pouget-Abadie]]", "[[Mehdi Mirza]]", "[[Bing Xu]]", "[[David Warde-Farley]]", "[[Sherjil Ozair]]", "[[Aaron Courville]]", "[[Yoshua Bengio]]"]
year: 2014
venue: "NeurIPS 2014"
file: "papers/Generative ML/Goodfellow et al - Generative Adversarial Nets.pdf"
---

# GAN paper (Goodfellow 2014)

**Summary**: Trains a generator $G$ and a discriminator $D$ as a two-player minimax game. In the non-parametric limit the unique solution has $p_g=p_{data}$ and $D=1/2$; the game value equals $-\log4+2\,\mathrm{JSD}(p_{data}\Vert p_g)$. With MLPs the whole system trains by backpropagation, with no Markov chains or inference networks.

**Authors**: Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio · **Year**: 2014 · **File**: `papers/Generative ML/Goodfellow et al - Generative Adversarial Nets.pdf`

---

## Problem

Deep generative models of the time (Boltzmann machines, generative stochastic networks) needed intractable likelihood gradients, approximate inference or Markov chains, and could not exploit piecewise-linear units well. The paper asks for a way to train a sampler without any of these (source: GAN.pdf, p. 1).

## Method

> [!definition] Adversarial game
> Noise prior $p_z(z)$, generator $G(z;\theta_g)$ and discriminator $D(x;\theta_d)\in[0,1]$ (probability that $x$ is real):
> $$\min_G\max_D V(D,G)=\mathbb E_{x\sim p_{data}}[\log D(x)]+\mathbb E_{z\sim p_z}[\log(1-D(G(z)))]$$
>
> (source: eq. 1, p. 3). See [[GAN]].

> [!algorithm] Minibatch training (Algorithm 1, p. 4)
> Repeat: for $k$ steps, sample $m$ noise vectors and $m$ data points and ascend
> $$\nabla_{\theta_d}\frac1m\sum_{i=1}^m\big[\log D(x^{(i)})+\log(1-D(G(z^{(i)})))\big];$$
> then sample $m$ noise vectors and descend
> $$\nabla_{\theta_g}\frac1m\sum_{i=1}^m\log\big(1-D(G(z^{(i)}))\big).$$
> $k=1$ in the experiments; momentum was used. Alternating keeps $D$ near its optimum if $G$ moves slowly.

**Non-saturating generator loss** (p. 3): early on $D$ rejects samples confidently, so $\log(1-D(G(z)))$ saturates. Instead train $G$ to maximize $\log D(G(z))$: same fixed point, stronger early gradients.

### Theory (§4, pp. 3-5)

> [!theorem] Optimal discriminator (Proposition 1)
> For fixed $G$,
> $$D^*_G(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}.$$
>
> (source: eq. 2, p. 4)

> [!proof]
> $V=\int p_{data}\log D+p_g\log(1-D)\,dx$, and $y\mapsto a\log y+b\log(1-y)$ is maximized on $[0,1]$ at $a/(a+b)$ (eq. 3, p. 5).

> [!theorem] Global optimum (Theorem 1)
> $C(G)=\max_D V(G,D)$ is minimized iff $p_g=p_{data}$, with value $-\log4$. In general
> $$C(G)=-\log4+\mathrm{KL}\Big(p_{data}\Big\Vert\frac{p_{data}+p_g}2\Big)+\mathrm{KL}\Big(p_g\Big\Vert\frac{p_{data}+p_g}2\Big)=-\log4+2\,\mathrm{JSD}(p_{data}\Vert p_g).$$
>
> (source: eqs. 4-6, p. 5). Uses [[KL divergence]]; JSD is non-negative and zero iff the distributions agree.

> [!theorem] Convergence (Proposition 2)
> If $G,D$ have enough capacity, $D$ reaches its optimum at each step and $p_g$ is updated to improve $\mathbb E_{p_{data}}[\log D^*_G]+\mathbb E_{p_g}[\log(1-D^*_G)]$, then $p_g\to p_{data}$. Proof: $U(p_g,D)$ is convex in $p_g$, so $\sup_D U$ is convex with a unique optimum and small steps converge (p. 5).

The authors state the guarantees do not apply to the parametric case, where one optimizes $\theta_g$ rather than $p_g$ (p. 5).

## Results

- Generators use ReLU and sigmoid; discriminators use maxout; dropout on the discriminator; noise enters only the bottom generator layer (§5, p. 6).
- **Parzen-window log-likelihood** (Table 1, p. 6), MNIST / TFD: adversarial nets 225 ± 2 / 2057 ± 26; DBN 138 ± 2 / 1909 ± 66; stacked CAE 121 ± 1.6 / 2110 ± 50; deep GSN 214 ± 1.1 / 1890 ± 29. The authors call the estimator high variance and poor in high dimension. No claim that samples beat other methods, only that they are competitive.
- Samples on MNIST, TFD and CIFAR-10 (fully connected and convolutional/"deconvolutional") with nearest training neighbours to show no memorization; linear interpolation in $z$ gives smooth digit morphs (Figs. 2-3, p. 7).

## Limitations

Stated (§6, p. 6): no explicit $p_g(x)$; $D$ must be synchronized with $G$, else $G$ collapses many $z$ to the same $x$ (the "Helvetica scenario"). GANs differentiate through the visible units, so they cannot model discrete data (§2, p. 2). Evaluation of sample-only models is an open problem.

## Connections

- Compared with [[VAE]]s (§2, p. 2): a VAE pairs a generator with a recognition network doing approximate inference and cannot have discrete latents; a GAN has no inference and cannot have discrete visibles. Uses the same stochastic-backprop idea as [[VAE paper (Kingma 2014)]].
- Uses [[Dropout]] and piecewise-linear units, the toolkit popularized by [[AlexNet (Krizhevsky 2012)]].
- Table 2 (p. 8) contrasts adversarial models with directed, undirected and autoencoder models: no Markov chain for sampling, no inference during training.
- Later baseline family against [[Diffusion models]]: see the CIFAR-10 FID comparison on [[GAN]] and [[Score SDE (Song 2021)]]; equivariant variants in [[Group equivariant GANs (Dey 2021)]].
- Proposed extensions (p. 7): conditional $p(x\mid c)$, learned inference, semi-supervised features, faster training.

%% refs:start %%
**Cites in this wiki**: [[AlexNet (Krizhevsky 2012)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[Bayesian DenseED surrogate (Zhu 2018)]], [[DDIM (Song 2021)]], [[DDPM (Ho 2020)]], [[Group equivariant GANs (Dey 2021)]], [[Priors in Bayesian deep learning (Fortuin 2022)]]
**Software cited**: [[software#Theano|Theano]]
%% refs:end %%

**Sources**: `papers/Generative ML/Goodfellow et al - Generative Adversarial Nets.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[GAN]] · [[VAE]] · [[Dropout]] · [[KL divergence]] · [[Diffusion models]] · [[Normalizing flows]]
