---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho et al. 2020, eqs. 1-7, 11-14, Alg. 1-2; Nakkiran et al. 2025, Alg. 2.1, Claim 2.1"
tags: [diffusion, generative]
---

# DDPM (denoising diffusion probabilistic model)

> [!algorithm] Forward chain, marginal and sampler (Ho et al. 2020, eqs. 2, 4; Alg. 2, pp. 2-4)
> Forward:
> ```
> q(x_t|x_{t-1}) = N(√(1-β_t) x_{t-1}, β_t I)
> q(x_t|x_0) = N(√ᾱ_t x_0, (1-ᾱ_t) I)
> α_t = 1-β_t,  ᾱ_t = ∏_{s≤t} α_s
> ```
> Sampling, from $x_T\sim\mathcal N(0,I)$ down to $t=1$:
> $$x_{t-1}=\tfrac{1}{\sqrt{\alpha_t}}\Big(x_t-\tfrac{1-\alpha_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta(x_t,t)\Big)+\sigma_tz$$
> with $\sigma_t^2=\beta_t$ or $\tilde\beta_t$, and $z=0$ at the last step.
>
> (source: `Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, pp. 2-4)

**Intuition**: noise the data in $T$ small Gaussian steps. Each reverse step is then close to Gaussian too, so a network only has to learn its mean. It does this by predicting the noise that was added.

## Training objective
The variational bound on $-\log p_\theta(x_0)$ splits into KLs between Gaussians (Ho eq. 5, p. 3):
```
L = L_T + Σ_{t>1} L_{t-1} + L_0
L_{t-1} = KL(q(x_{t-1}|x_t,x_0) ‖ p_θ(x_{t-1}|x_t))
```
The forward posterior is Gaussian in closed form (eqs. 6-7):
```
μ̃_t = √ᾱ_{t-1} β_t/(1-ᾱ_t) · x_0
     + √α_t (1-ᾱ_{t-1})/(1-ᾱ_t) · x_t
β̃_t = (1-ᾱ_{t-1})/(1-ᾱ_t) · β_t
```
With the [[Noise prediction|ε-parameterization]], dropping the per-$t$ weight gives $L_{\text{simple}}$ (eq. 14, p. 5). That weightless loss is the one that trains well: FID 3.17 against 13.51 for the true bound (Table 2). See [[ELBO]].

## Link to score matching and Langevin
Ho et al. note that the ε-objective "resembles" [[Score matching#Denoising score matching|denoising score matching]] over many noise levels, and Alg. 2 resembles [[Langevin dynamics]] with $\epsilon_\theta$ as a learned gradient (p. 4). [[Score SDE (Song 2021)|Song et al.]] make this exact: DDPM is a discretization of the VP SDE ([[Diffusion models#SMLD and DDPM|hub]]).

## The tutorial's "pointwise" view
[[Step-by-step diffusion (Nakkiran 2025)|Nakkiran et al.]] derive the same sampler without the bound:
- Claim 2.1 (p. 11): for small steps, $p(x_{t-\Delta t}\mid x_t=z)\approx\mathcal N(\mu_z,\sigma_q^2\Delta t)$, with $\mu_z=z+\sigma_q^2\Delta t\,\nabla\log p_t(z)$.
- Lemma 2.1 (p. 14, 1-d): the KL error per step is $O(\sigma^4)$, so the total error vanishes.
- The sampler is Euler-Maruyama on the reverse SDE (eqs. 2.17-2.20, p. 20).

Nakkiran write a VE chain with $t\in[0,1]$ and $\sigma_t=\sigma_q\sqrt t$. This page uses Ho's VP notation with integer $t$ and $\bar\alpha_t$.

## Variants
- [[DDIM]] reuses the same trained $\epsilon_\theta$. Its parameter η=1 recovers DDPM (Song, Meng, Ermon eq. 16).
- [[Classifier-free guidance]] replaces $\epsilon_\theta$ by a mix of a conditional and an unconditional prediction.

## Where it appears
- [[DDPM (Ho 2020)]]: defines it. CIFAR-10 FID 3.17, IS 9.46, NLL ≤ 3.75 bits/dim (Table 1).
- [[DDIM (Song 2021)]]: the baseline that DDIM accelerates.
- [[Step-by-step diffusion (Nakkiran 2025)]]: Chapter 2.
- [[Score SDE (Song 2021)]]: shows it is the VP-SDE discretization.

**Sources**: `Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, `Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`, `Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]] · [[DDIM]] · [[Noise schedule]] · [[Noise prediction]] · [[Score matching]]
