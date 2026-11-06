---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho et al. 2020, eqs. 11-14, Table 2; Nakkiran et al. 2025, §5 and App. B.10"
tags: [diffusion, generative]
---

# Noise prediction (ε-parameterization)

> [!definition] ε-parameterization (Ho et al. 2020, eqs. 11, 14, pp. 4-5)
> Write the reverse mean through a noise predictor:
> $$\mu_\theta(x_t,t)=\tfrac{1}{\sqrt{\alpha_t}}\Big(x_t-\tfrac{\beta_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta(x_t,t)\Big)$$
> and train on
> ```
> L_simple = E_{t,x_0,ε} ‖ε - ε_θ(x_t, t)‖²
> x_t = √ᾱ_t x_0 + √(1-ᾱ_t) ε
> ```
> with $t$ uniform on $\{1,\dots,T\}$.
>
> (source: `Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, pp. 4-5)

**Intuition**: the network sees a noisy image and says what noise was added. Given $x_t$, predicting $\epsilon$, $x_0$ or the score are the same task up to known affine maps.

## Equivalent targets
| Target | Optimum |
|---|---|
| x₀-prediction | $\mathbb E[x_0\mid x_t]$ |
| ε-prediction | $\mathbb E[\epsilon\mid x_t]$ |
| v-prediction | $v=\alpha_t\epsilon-\sigma_tx_0$ (Salimans-Ho) |
| score | $\nabla\log p_t=-\epsilon_\theta/\sqrt{1-\bar\alpha_t}$ |

[[Step-by-step diffusion (Nakkiran 2025)|Nakkiran et al.]] (§5, p. 49) state the first three differ only by time weightings. The weightings leave the optimum unchanged but change training. Their example: x₀-prediction with much weight on low noise can settle near the identity map.

DDIM's predicted clean image is $\hat x_0=(x_t-\sqrt{1-\alpha_t}\epsilon_\theta)/\sqrt{\alpha_t}$ (Song, Meng, Ermon eq. 9). Wiki note: the score row is the DSM optimum written in DDPM coordinates. DDIM eq. 49 (p. 16) states the VE version, $\nabla\log p_t(\bar x)=-\epsilon_\theta/\sigma(t)$. See [[Score matching#Tweedie's formula|Tweedie's formula]].

> [!warning] Sign as printed in Nakkiran
> Nakkiran p. 49 prints $\epsilon_t=\frac1{\sigma_t}\mathbb E[x_0-x_t\mid x_t]$. With their $x_t=x_0+\sigma_t\epsilon$, $\epsilon=(x_t-x_0)/\sigma_t$. Wiki note: the printed sign looks flipped; App. B.10 repeats the pattern. Optima are unaffected up to sign.

## Weighting matters (Ho Table 2, p. 5)
| Target and loss | IS | FID |
|---|---|---|
| μ̃, true bound | 8.06 | 13.22 |
| ε, true bound | 7.67 | 13.51 |
| ε, L_simple | 9.46 | 3.17 |

$L_{\text{simple}}$ drops the weight $\beta_t^2/(2\sigma_t^2\alpha_t(1-\bar\alpha_t))$ of eq. 12. This down-weights small $t$, which Ho et al. credit for the better samples (p. 5). Predicting $x_0$ was worse in their early tests (p. 4).

## Where it appears
- [[DDPM (Ho 2020)]], [[DDPM]].
- [[DDIM (Song 2021)]]: one ε-network shared by every σ (Thm. 1).
- [[Classifier-free guidance (Ho 2022)]]: guidance mixes two ε-predictions.
- [[Step-by-step diffusion (Nakkiran 2025)]]: §5 and App. B.10.

**Sources**: `Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, `Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`, `Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DDPM]] · [[Score matching]] · [[Noise schedule]] · [[Classifier-free guidance]]
