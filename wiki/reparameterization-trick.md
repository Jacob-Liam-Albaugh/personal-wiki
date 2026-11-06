---
type: method
area: bayesian
areas: [bayesian, ml]
source-ref: "Kingma & Welling 2014, eqs. 4-5, p. 5; Karumuri et al. 2024, p. 14"
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
- [[local-reparameterization-trick]]: sample pre-activations instead of weights.
- Pathwise gradients through an SDE solver by sampling $dB_t$ (Xu et al. §4), with the sticking-the-landing estimator dropping the score term.

## Where it appears
- [[kingma-2014-aevb]] (defines it) · [[kingma-2015-variational-dropout]] (weights, eq. 3) · [[kingma-2019-intro-vae]] (motivation only).
- [[karumuri-2024-amortized-vi-inverse-problems]] · [[margossian-2024-amortized-vi-when-why]] (Adam on ELBO gradients) · [[xu-2022-sde-bnn]].

**Sources**: `Bayesian/Kingma Welling - Auto-Encoding Variational Bays - Bayesian Variational Inference & Reparametrization Trick.pdf`, `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[evidence-lower-bound]] · [[variational-autoencoder]] · [[normalizing-flows]]
