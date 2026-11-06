---
type: method
area: ml
areas: [ml, stochastic]
source-ref: "Wang 2026, eq. 6; Nakkiran et al. 2025, §4, eqs. 4.6-4.15, Pseudocodes 4-5"
tags: [generative, diffusion, ml]
---

# Flow matching

> [!algorithm] (Wang 2026, eq. 6)
> Learn $v_\theta$ so that $\frac{dx}{d\tau}=v_\theta(x,\tau)$ transports $x_0\sim p_0$ to $x_1\sim p_{\text{data}}$.

## Pointwise and marginal flows (Nakkiran et al. 2025, §4)
Nakkiran et al. run flows from noise at $t=1$ to data at $t=0$. This is reversed relative to Lipman et al. and Wang.
- A pointwise flow $v^{[x_1,x_0]}$ joins one noise point $x_1$ to one data point $x_0$ (p. 36).
- For a coupling $(x_1,x_0)\sim\Pi_{q,p}$, the marginal flow averages them (eq. 4.6, p. 38):
```
v*_t(x_t) = E[ v^{[x1,x0]}_t(x_t) | x_t ]
```
It transports $q$ to $p$ (Flow Combining Lemma, Lemma B.2, pp. 62-63).

## Linear flows: training and sampling
Linear pointwise flow (eqs. 4.7-4.8, p. 39):
```
x_t = t x_1 + (1-t) x_0
v   = x_0 - x_1
```
Since $v^*$ is a conditional expectation, it solves a regression (eqs. 4.9-4.10):
- Train (Pseudocode 4, p. 42): draw $(x_1,x_0)$ and $t\sim U[0,1]$, minimize $\|f_\theta(x_t,t)-(x_0-x_1)\|^2$.
- Sample (Pseudocode 5, p. 43): $x_1\sim q$, then $x_{t-\Delta t}=x_t+f_\theta(x_t,t)\Delta t$ down to $t=0$.

The usual choice is the independent coupling with a Gaussian base.

## DDIM as a linear flow (Claim 4.1, p. 44)
Under the diffusion coupling $x_1=x_0+\mathcal N(0,\sigma_q^2)$, [[DDIM]] follows the linear flow's trajectories at time $\sqrt t$. The claim is informal and holds for the VE form only; it is false for VP-DDIM (footnote 16).

## In Wang 2026
Examples cited by Wang: conditional flow matching for near-wall turbulence (ref. 27), patch-additive flow matching (ref. 56). Neither read.

Wiki note: the deterministic [[Diffusion models#Probability-flow ODE|probability-flow ODE]] of Song et al. 2021 is also a velocity field that transports noise to data. There the velocity is built from the score; flow matching learns it directly.

## Where it appears
- [[Generative priors for turbulence (Wang 2026)]].
- [[Step-by-step diffusion (Nakkiran 2025)]]: Chapter 4.

**Sources**: `papers/IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`, `papers/Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]] · [[Diffusion posterior sampling]] · [[DDIM]] · [[Normalizing flows]]
