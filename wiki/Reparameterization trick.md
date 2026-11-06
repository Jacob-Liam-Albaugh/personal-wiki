---
type: method
area: bayesian
areas: [bayesian, ml]
source-ref: "Kingma & Welling 2014, eqs. 4-5, p. 5; Karumuri et al. 2024, p. 14"
tags: [vi, ml]
---

# Reparameterization trick

> [!algorithm] Reparameterization
> Write $z\sim q_\phi(z\mid x)$ as $z=g_\phi(\epsilon,x)$ with $\epsilon\sim p(\epsilon)$ free of $\phi$. Then
> $$\mathbb E_{q_\phi}[f(z)]=\mathbb E_{p(\epsilon)}[f(g_\phi(\epsilon,x))]\approx\tfrac1L\textstyle\sum_l f(g_\phi(\epsilon^{(l)},x)),$$
> which is differentiable in $\phi$.
>
> (source: `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, eqs. 4-5)

**Intuition**: move the randomness into a fixed noise variable so the gradient passes through the sample. The alternative score-function estimator $\mathbb E_q[f\,\nabla\log q]$ is unbiased but has high variance (AEVB p. 3).

## Recipes (AEVB p. 5)
- Location-scale: $z=\mu+\sigma\epsilon$, $\epsilon\sim N(0,1)$.
- Inverse CDF with $\epsilon\sim U(0,I)$.
- Composition: log-normal, gamma, Dirichlet, beta, $\chi^2$, F.
- Full-covariance Gaussian (Karumuri p. 14): $\Xi=\mu(Y;\phi)+L(Y;\phi)Z_0$; flow guide $\Xi=G(Z_0;Y,\phi)$.

## Variants
- [[Local reparameterization trick]]: sample pre-activations instead of weights.
- Pathwise gradients through an SDE solver by sampling $dB_t$ (Xu et al. §4), with the sticking-the-landing estimator dropping the score term.

## Where it appears
- [[VAE paper (Kingma 2014)]] (defines it) · [[Variational dropout (Kingma 2015)]] (weights, eq. 3) · [[Intro to VAEs (Kingma 2019)]] (motivation only).
- [[Amortized VI for inverse problems (Karumuri 2024)]] · [[Amortized VI when and why (Margossian 2024)]] (Adam on ELBO gradients) · [[SDE-BNN (Xu 2022)]].

**Sources**: `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ELBO]] · [[VAE]] · [[Normalizing flows]]
