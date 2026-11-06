---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Song et al. 2021, eqs. 7, 19, pp. 4-5, 13; Nakkiran et al. 2025, eq. 2.16; Ho et al. 2020, §3.2"
tags: [diffusion, generative, ml]
---

# Score matching

> [!definition] Score
> The score of a density $p$ is $\nabla_x\log p(x)$. It does not depend on the normalizing constant, so it can be learned for unnormalized models.

**Intuition**: fit a vector field that points uphill in log-density. With it, [[Langevin dynamics]] or a reverse SDE can sample.

## Denoising score matching
> [!algorithm] Time-dependent DSM (Song et al. 2021, eq. 7, p. 4)
> $$\theta^*=\arg\min_\theta\ \mathbb E_t\,\lambda(t)\,\mathbb E\big\|s_\theta(x(t),t)-\nabla\log p_{0t}(x(t)\mid x(0))\big\|^2$$
> $t\sim U[0,T]$, $x(0)\sim p_0$, $x(t)\sim p_{0t}(\cdot\mid x(0))$.
> The usual weighting is $\lambda\propto1/\mathbb E\|\nabla\log p_{0t}\|^2$.
>
> (source: `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, p. 4)

The target is the score of the known noising kernel, not of the unknown data density. With enough data and capacity the minimizer equals $\nabla_x\log p_t$ almost everywhere (p. 4). For Gaussian kernels the target is $-(x(t)-\mu)/\sigma^2$.

## Tweedie's formula
For Gaussian noising, the score is a denoiser. In Nakkiran et al.'s VE setup, $x_t=x_0+\mathcal N(0,\sigma_q^2t)$, and (eq. 2.16, p. 20):
```
σ_q² ∇log p_t(x_t)
  = (1/t) E[x_0 - x_t | x_t]
```
So learning $\mathbb E[x_0\mid x_t]$ by regression gives the score. Nakkiran footnote 3 (p. 12) notes this makes the reverse-step mean exact for any step size.

[[DDPM]] reaches the same link from the other side. Its $\epsilon$-loss "resembles denoising score matching over multiple noise scales" (Ho et al., §3.2, p. 4). See [[Noise prediction]].

## Sliced score matching
When the kernel is not available in closed form, eq. 19 (p. 13) replaces the target with random projections:
$$\mathbb E\big[\tfrac12\|s_\theta\|^2+v^\top\nabla s_\theta\,v\big]$$
with $\mathbb E v=0$, $\mathrm{Cov}\,v=I$.

## Where it appears
- [[Score SDE (Song 2021)]], [[Diffusion models]].
- [[DDPM (Ho 2020)]], [[Step-by-step diffusion (Nakkiran 2025)]].

**Sources**: `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, `Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, `Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]] · [[Langevin dynamics]] · [[Flow matching]]
