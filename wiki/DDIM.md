---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Song, Meng, Ermon 2021, eqs. 7, 12, 14-16, Thm. 1, Prop. 1; Nakkiran et al. 2025, Alg. 3.1, Claim 4.1"
tags: [diffusion, generative, sampling]
---

# DDIM (denoising diffusion implicit model)

> [!algorithm] Generalised update (Song, Meng, Ermon 2021, eq. 12, p. 5)
> In DDIM notation, where $\alpha_t$ means DDPM's $\bar\alpha_t$:
> $$x_{t-1}=\sqrt{\alpha_{t-1}}\,\hat x_0+\sqrt{1-\alpha_{t-1}-\sigma_t^2}\;\epsilon_\theta(x_t)+\sigma_t\epsilon_t$$
> $$\hat x_0=\frac{x_t-\sqrt{1-\alpha_t}\,\epsilon_\theta(x_t)}{\sqrt{\alpha_t}}$$
> $\sigma_t=0$ is DDIM, a deterministic map. The DDPM value of $\sigma_t$ recovers [[DDPM]].
>
> (source: `papers/Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`, p. 5)

**Intuition**: many forward processes have the same one-step marginals $q(x_t\mid x_0)$ as DDPM. The DDPM loss sees only those marginals, so one trained network serves all of them. Pick the noise-free one, and you can also skip steps.

> [!warning] Notation
> DDIM writes $\alpha_t$ for DDPM's $\bar\alpha_t$, and $\alpha_t/\alpha_{t-1}$ for DDPM's $\alpha_t$ (App. C.2, eqs. 60-61). This page follows DDIM's notation inside the callouts only.

## Why no retraining is needed
- The non-Markovian family $q_\sigma$ (eqs. 6-7, p. 3) keeps the DDPM marginals (Lemma 1, p. 13).
- Theorem 1 (p. 4): for every $\sigma>0$, $J_\sigma=L_\gamma+C$, a weighted DDPM ε-loss plus a constant. So a model trained on $L_{\text{simple}}$ ([[Noise prediction]]) is used for all σ.
- The optimum is independent of γ only if $\epsilon_\theta$ does not share parameters across $t$ (p. 4). Theorem 1 itself is stated for $\sigma>0$.

## The η family and acceleration
```
σ_τi(η) = η √((1-α_τ{i-1})/(1-α_τi))
            · √(1 - α_τi/α_τ{i-1})
```
(eq. 16, p. 6). η=0 is DDIM and η=1 is DDPM. Sampling on a sub-sequence τ of length $S\ll T$ uses the same update (App. C.1).

CIFAR-10 FID (Table 1, p. 7):

| η | S=10 | S=100 | S=1000 |
|---|---|---|---|
| 0 (DDIM) | 13.36 | 4.16 | 4.04 |
| 1 (DDPM) | 41.07 | 5.78 | 4.73 |

At $S=1000$ the larger-variance DDPM $\hat\sigma$ gives 3.17, but it gives 367.43 at $S=10$.

## ODE view
Eq. 14 (p. 6) writes DDIM as Euler steps of
$$d\bar x=\epsilon_\theta\big(\bar x/\sqrt{\sigma^2+1}\big)\,d\sigma$$
with $\bar x=x/\sqrt\alpha$ and $\sigma=\sqrt{(1-\alpha)/\alpha}$.
- Prop. 1 (p. 6): with the optimal $\epsilon_\theta$ this is the [[Diffusion models#Probability-flow ODE|probability-flow ODE]] of the VE SDE.
- The discretizations differ: DDIM steps in $d\sigma$ and Song et al.'s sampler steps in $dt$. They agree only for close $\alpha_t,\alpha_{t-\Delta t}$ (eq. 15).
- Consequences: an invertible encoding $x_0\mapsto x_T$, a reconstruction error from 0.014 at S=10 to 0.0001 at S=1000 (Table 2, p. 9), and meaningful interpolation in $x_T$.

## The tutorial's view
[[Step-by-step diffusion (Nakkiran 2025)|Nakkiran et al.]] (Alg. 3.1, p. 21) write the deterministic step as
```
x_{t-Δt} = x_t + λ (μ_{t-Δt}(x_t) - x_t)
λ = σ_t / (σ_{t-Δt} + σ_t)
```
- λ → ½ as Δt → 0, which matches the probability-flow ODE (p. 29).
- Claim 4.1 (p. 44): DDIM is linear [[Flow matching]] under the "diffusion coupling", with time reparametrized by √t. It holds for VE only.

## Where it appears
- [[DDIM (Song 2021)]]: defines it.
- [[Step-by-step diffusion (Nakkiran 2025)]]: Chapters 3-4.
- [[Classifier-free guidance (Ho 2022)]]: named as a drop-in sampler for Alg. 2.

**Sources**: `papers/Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`, `papers/Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DDPM]] · [[Diffusion models]] · [[Flow matching]] · [[Normalizing flows]] · [[Noise schedule]]
