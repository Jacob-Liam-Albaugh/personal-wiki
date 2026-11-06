---
type: definition
area: stochastic
areas: [stochastic, math]
source-ref: "Song et al. 2021, App. D.1, eqs. 35-37, pp. 16-17"
tags: [sampling, pde]
---

# Fokker-Planck equation

> [!definition] Kolmogorov forward equation (Song et al. 2021, eq. 35, p. 16)
> For $dx=f(x,t)\,dt+G(x,t)\,dw$ the marginal density $p_t$ obeys
> $$\partial_tp_t=-\sum_i\partial_i[f_ip_t]+\tfrac12\sum_{i,j}\partial_i\partial_j\Big[\textstyle\sum_kG_{ik}G_{jk}\,p_t\Big]$$
>
> (source: `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, p. 16)

**Intuition**: the SDE moves particles; Fokker-Planck moves the density. Drift transports it and diffusion spreads it.

## As a continuity equation
Song et al. pull the diffusion term into the drift (eqs. 36-37):
$$\partial_tp_t=-\nabla\cdot(\tilde f\,p_t)$$
$$\tilde f=f-\tfrac12\nabla\cdot[GG^\top]-\tfrac12GG^\top\nabla\log p_t$$
This is a Liouville equation with no diffusion, so the ODE $\dot x=\tilde f$ has the same marginals. That ODE is the [[Diffusion models#Probability-flow ODE|probability-flow ODE]]. Song et al. credit the idea to Maoutsa et al. 2020.

Song et al. also note that for non-affine drift, the DSM transition kernel can be got by solving this equation (p. 5).

## Where it appears
- [[Score SDE (Song 2021)]].

**Sources**: `Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]] · [[Langevin dynamics]] · [[SDE-BNN (Xu 2022)]]
