---
type: method
area: ml
areas: [ml, bayesian]
source-ref: "Kingma & Welling 2014, Alg. 1, eqs. 9-12; Kingma & Welling 2019, pp. 4-5"
tags: [generative, vi, ml]
---

# Variational autoencoder (VAE)

> [!algorithm] AEVB / VAE (Kingma & Welling 2014, Alg. 1)
> Decoder $p_\theta(x\mid z)p(z)$, encoder $q_\phi(z\mid x)=N(\mu,\sigma^2I)$ given by a network. Per minibatch ($M=100$, $L=1$): sample $\epsilon$, set $z=\mu+\sigma\odot\epsilon$, ascend
> $$\tfrac12\textstyle\sum_j\big(1+\log\sigma_j^2-\mu_j^2-\sigma_j^2\big)+\tfrac1L\sum_l\log p_\theta(x\mid z^{(l)})$$
> in $(\theta,\phi)$ with SGD or Adagrad.
>
> (source: `papers/Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, Alg. 1, eq. 10)

**Intuition**: a latent-variable generative model and an inference network trained together on one objective, the [[ELBO]], made differentiable by the [[Reparameterization trick]]. The encoder is [[Amortized VI]].

## Variants
- Decoders: Bernoulli MLP (eq. 11) or Gaussian MLP with learned $\log\sigma^2$ (eq. 12).
- Learned priors (VampPrior, flow, neural-process) surveyed in Fortuin §3.
- Ancestor: the Helmholtz machine and wake-sleep (Kingma & Welling 2019, p. 5), which AEVB beats on MNIST and Frey Face (AEVB Fig. 2).

## Where it appears
- [[VAE paper (Kingma 2014)]] (defines it) · [[Intro to VAEs (Kingma 2019)]] (background; VAE chapters missing from the PDF) · [[Priors in Bayesian deep learning (Fortuin 2022)]].
- [[SINDy autoencoders (Champion 2019)]] and [[SINDy delay autoencoders (Bakarji 2022)]] use autoencoders to find latent coordinates where dynamics are sparse; [[Neural ODEs (Chen 2018)]] introduces a latent-ODE generative model.

**Sources**: `papers/Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `papers/Bayesian/Kingma, Welling - Intro to Variational Autoencoders.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]] · [[Normalizing flows]] · [[KL divergence]]
- [[Variational graph auto-encoder (Kipf 2016)]] (graph-structured VAE with GCN encoder and inner-product decoder).
- [[GAN paper (Goodfellow 2014)]]
