---
type: concept
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho et al. 2020, p. 5, App. B; Song et al. 2021, eqs. 9-12; Nakkiran et al. 2025, eqs. 1.12, 5.1, p. 19; Ho, Salimans 2022, eq. 1"
tags: [diffusion, generative]
---

# Noise schedule

**Summary**: the schedule says how much noise the forward process has added by each time. It fixes the marginals $q(x_t\mid x_0)$, so it fixes the training targets and the sampler's step sizes. The papers here parameterize it four ways.

**Sources**: `papers/Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, `papers/Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, `papers/Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`, `papers/Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`, `papers/Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`.
**Last updated**: 2026-11-06

---

## Four parameterizations
```
Ho (VP, discrete):  β_1..β_T,  ᾱ_t = ∏(1-β_s)
DDIM:               α_t (= Ho's ᾱ_t)
Song (SDE):         β(t) for VP,  σ(t) for VE
Ho-Salimans:        log-SNR λ,
                    α_λ² = 1/(1+e^{-λ})
                    σ_λ² = 1-α_λ²
Nakkiran (VE):      σ_t = σ_q √t,  t∈[0,1]
```
DDIM's $\alpha_{1:T}$ fixes $\beta_t$ uniquely through $\alpha_t/\alpha_{t-1}$ (App. C.2, eqs. 60-61).

## Choices in the papers
- **DDPM**: linear $\beta$ from $10^{-4}$ to $0.02$, $T=1000$ (Ho p. 5). It was picked from constant, linear and quadratic schedules, all kept so that $L_T\approx0$, giving about $10^{-5}$ bits/dim (App. B).
- **Score SDE**: the VE, VP and sub-VP SDEs ([[Diffusion models#VE, VP and sub-VP SDEs|hub]]).
- **Tutorial**: a constant VE schedule in the main text. General $\sigma(t)$ gives $dx=\sqrt{d\sigma^2/dt}\,dw$ (p. 19). §5 adds the VP form (eq. 5.1, p. 47) and Karras et al.'s suggestion $\sigma(t)=t$, $s=1$.
- **DDIM sampling**: a time sub-sequence τ, linear or quadratic, which acts as a sampling-time schedule (App. D.2).

## Where it appears
- [[DDPM]], [[DDIM]], [[Diffusion models]], [[Classifier-free guidance]].

## Related pages
- [[Noise prediction]] · [[DDPM (Ho 2020)]] · [[Step-by-step diffusion (Nakkiran 2025)]]
