---
type: method
area: ml
areas: [ml, bayesian]
source-ref: "Kingma & Welling 2014, Alg. 1, eqs. 9-12; Kingma & Welling 2019, pp. 4-5"
---

# Variational autoencoder (VAE)

> [!algorithm] AEVB / VAE (Kingma & Welling 2014, Alg. 1)
> Decoder $p_\theta(x\mid z)p(z)$, encoder $q_\phi(z\mid x)=N(\mu,\sigma^2I)$ given by a network. Per minibatch ($M=100$, $L=1$): sample $\epsilon$, set $z=\mu+\sigma\odot\epsilon$, ascend
> $$\tfrac12\textstyle\sum_j\big(1+\log\sigma_j^2-\mu_j^2-\sigma_j^2\big)+\tfrac1L\sum_l\log p_\theta(x\mid z^{(l)})$$
> in $(\theta,\phi)$ with SGD or Adagrad.
>
> (source: `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, Alg. 1, eq. 10)

**Intuition**: a latent-variable generative model and an inference network trained together on one objective, the [[evidence-lower-bound]], made differentiable by the [[reparameterization-trick]]. The encoder is [[amortized-variational-inference]].

## Variants
- Decoders: Bernoulli MLP (eq. 11) or Gaussian MLP with learned $\log\sigma^2$ (eq. 12).
- Learned priors (VampPrior, flow, neural-process) surveyed in Fortuin §3.
- Ancestor: the Helmholtz machine and wake-sleep (Kingma & Welling 2019, p. 5), which AEVB beats on MNIST and Frey Face (AEVB Fig. 2).

## Where it appears
- [[kingma-2014-aevb]] (defines it) · [[kingma-2019-intro-vae]] (background; VAE chapters missing from the PDF) · [[fortuin-2022-priors-in-bdl]].

**Sources**: `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `Bayesian/Kingma, Welling - Intro to Variational Autoencoders.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[diffusion-models]] · [[normalizing-flows]] · [[kl-divergence]]
