---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Song et al. 2021, eqs. 7, 19, pp. 4-5, 13"
---

# Score matching

> [!definition] Score
> The score of a density $p$ is $\nabla_x\log p(x)$. It does not depend on the normalizing constant, so it can be learned for unnormalized models.

**Intuition**: fit a vector field that points uphill in log-density. With it, [[langevin-dynamics]] or a reverse SDE can sample.

## Denoising score matching
> [!algorithm] Time-dependent DSM (Song et al. 2021, eq. 7, p. 4)
> $$\theta^*=\arg\min_\theta\ \mathbb E_t\,\lambda(t)\,\mathbb E\big\|s_\theta(x(t),t)-\nabla\log p_{0t}(x(t)\mid x(0))\big\|^2$$
> $t\sim U[0,T]$, $x(0)\sim p_0$, $x(t)\sim p_{0t}(\cdot\mid x(0))$.
> The usual weighting is $\lambda\propto1/\mathbb E\|\nabla\log p_{0t}\|^2$.
>
> (source: `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, p. 4)

The target is the score of the known noising kernel, not of the unknown data density. With enough data and capacity the minimizer equals $\nabla_x\log p_t$ almost everywhere (p. 4). For Gaussian kernels the target is $-(x(t)-\mu)/\sigma^2$.

## Sliced score matching
When the kernel is not available in closed form, eq. 19 (p. 13) replaces the target with random projections:
$$\mathbb E\big[\tfrac12\|s_\theta\|^2+v^\top\nabla s_\theta\,v\big]$$
with $\mathbb E v=0$, $\mathrm{Cov}\,v=I$.

## Where it appears
- [[song-2021-score-sde]], [[diffusion-models]].

**Sources**: `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[diffusion-models]] · [[langevin-dynamics]] · [[flow-matching]]
