---
type: method
area: ml
areas: [ml, stochastic]
source-ref: "Wang 2026, eq. 6; Nakkiran et al. 2025, §4, eqs. 4.6-4.15, Pseudocodes 4-5; Chen, Lipman, Ben-Hamu 2024, slides 19-31, 43, 64, 131-134; de Albuquerque, Pearson 2024, eqs. 44-46"
tags: [generative, diffusion, ml]
---

# Flow matching

> [!algorithm] (Wang 2026, eq. 6)
> Learn $v_\theta$ so that $\frac{dx}{d\tau}=v_\theta(x,\tau)$ transports $x_0\sim p_0$ to $x_1\sim p_{\text{data}}$.

## General recipe (Chen, Lipman, Ben-Hamu 2024)
Notation of the tutorial slides: source $X_0\sim p$ at $t=0$, data $X_1\sim q$ at $t=1$, velocity $u_t$.
- Choose a conditional path $p_{t|1}(x\mid x_1)$ with a known conditional velocity $u_t(x\mid x_1)$. The marginal velocity is $u_t(x)=\mathbb E[u_t(X_t\mid X_1)\mid X_t=x]$, and it generates the marginal path $p_t(x)=\mathbb E_{X_1}p_{t|1}(x\mid X_1)$ ("marginalization trick", slides 21-23).
- Conditional flow matching loss (slide 24): $\mathcal L_\text{CFM}=\mathbb E_{t,X_1,X_t}\,D\big(u_t(X_t\mid X_1),u_t^\theta(X_t)\big)$ has the same gradient as the intractable loss against $u_t(X_t)$, for any Bregman divergence $D$ (slides 25-26).
- Linear path (slide 19): $X_t=(1-t)X_0+tX_1$, target $X_1-X_0$. It is exact OT per data point but the marginal flow is not OT (slide 28).
- Affine paths (slide 30): $X_t=\alpha_tX_1+\sigma_tX_0$, $u_t(x)=\mathbb E[\dot\alpha_tX_1+\dot\sigma_tX_0\mid X_t=x]$. Predicting $X_0$, $X_1$ or the velocity are interchangeable. With a Gaussian source and independent coupling this is a diffusion model's probability-flow ODE (slide 31).
- Coupling (slide 64): any joint law of $(X_0,X_1)$ with the right marginals works; kinetic energy is bounded by $\mathbb E\|X_1-X_0\|^2$, which minibatch OT pairings reduce.
- Guidance for Gaussian paths (slide 43): $\tilde u_t(x\mid y)=(1-w)u_t(x)+w\,u_t(x\mid y)$ ([[Classifier-free guidance]]).
- Inverse problems with a pre-trained model (slides 131-134): $u_t(x\mid y)=u_t(x)+\sigma_t^2\frac{d\log(\alpha_t/\sigma_t)}{dt}\nabla_x\log p_{Y|t}(y\mid x)$, with the likelihood score approximated heuristically; see [[Diffusion posterior sampling]].

Extensions (equivariant and Riemannian flows, shortcut models, discrete flows, Generator Matching) are summarized on [[Flow matching tutorial (Chen 2024)]].

## Full-covariance Gaussian paths (de Albuquerque, Pearson 2024, App. A.5)
The conditional path can use a matrix scale: $x_t=\Sigma_t^{1/2}(x_1)\,x_0+\mu_t(x_1)$ with conditional velocity $\dot\Sigma_t^{1/2}\Sigma_t^{-1/2}(x-\mu_t)+\dot\mu_t$ (eqs. 44-45). Choosing $\mu_t=A_tx_1$, $\Sigma_t=A_tC_tA_t^\top$ (eq. 46) gives the inflationary pfODE of [[Inflationary flows (de Albuquerque 2024)]], whose noise is anisotropic in the data's principal directions. That paper runs time from data ($t=0$) to noise.

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
- [[Flow matching tutorial (Chen 2024)]]: the general recipe, design choices and adaptations.
- [[Inflationary flows (de Albuquerque 2024)]]: its pfODE is a full-covariance Gaussian-path flow (App. A.5), so it could be trained by flow matching.

**Sources**: `papers/IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`, `papers/Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`, `papers/Diffusion/Chen, Lipman, Ben-Hamu - Flow Matching Tutorial.pdf`, `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models.pdf`.
**Last updated**: 2026-11-11

---

## Related pages
- [[Diffusion models]] · [[Diffusion posterior sampling]] · [[DDIM]] · [[Normalizing flows]] · [[Classifier-free guidance]] · [[Equivariance]]
