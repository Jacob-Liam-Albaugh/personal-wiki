---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Nakkiran, Bradley, Zhou, Advani 2025, FnT Computer Graphics and Vision 17(1), Alg. 2.1, 3.1, Claims 2.1/2.2/3.1/4.1, eqs. 1.11, 2.6, 2.11, 2.15, 3.1, 3.25, 4.6, 4.10"
tags: [diffusion, generative]
authors: [Nakkiran, Bradley, Zhou, Advani]
year: 2025
venue: "Foundations and Trends in Computer Graphics and Vision, Vol. 17, No. 1, pp. 1-75 (DOI 10.1561/0600000114)"
file: "Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf"
---

# Step-by-Step Diffusion: An Elementary Tutorial (Nakkiran 2025)

**Summary**: A 77-page tutorial that derives diffusion samplers and flow matching with no SDEs, ELBOs, Langevin dynamics or scores in the core argument. A Gaussian forward process reduces generative modelling to per-step regression of conditional means; the stochastic (DDPM-like) sampler is justified by a Bayes-rule/Taylor argument, the deterministic (DDIM-like) sampler by a "pointwise, then average" transport argument, and both are then subsumed by flow matching with pointwise flows. SDE/ODE views, noise schedules, parametrizations and error sources are covered as optional or practical material (Sections 2.4, 3.5, 5). No new experiments beyond one toy spiral figure.

**Authors**: Preetum Nakkiran, Arwen Bradley, Hattie Zhou, Madhu Advani (Apple; Zhou also Mila) · **Year**: 2025 · **File**: `Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`

Wiki note: year is 2025 because the PDF's own citation line reads "Foundations and Trends in Computer Graphics and Vision: Vol. 17, No. 1, pp 1-75 ... (2025)" (PDF p. 1) and "(c)2025 P. Nakkiran et al." (PDF p. 3). The tutorial circulated earlier as a preprint (arXiv, 2024) **[unverified]**; the wiki slug follows the published year. Page cites below are the tutorial's printed page numbers (PDF page = printed + 2; the PDF has 77 pages, body ends printed p. 51, appendices pp. 53-68, references pp. 70-74).

---

## Problem

Given i.i.d. samples from an unknown $p^*(x)$, build a sampler for (approximately) the same distribution (p. 3). Diffusion reduces this to a sequence of easier sampling problems: noise the data into an easy distribution, then learn to undo each small noising step. The tutorial's aim is to teach this with minimal prerequisites yet enough detail to reason about *correctness* of the samplers (Abstract, p. 1). Unlike most treatments it takes neither the VAE nor the SDE route (p. 1; SDEs appear only in optional Sections 2.4 and 3.5).

## Method

The Method section follows the tutorial's chapters.

### Notation used by this tutorial

- Time is continuous, $t\in[0,1]$, with $t=0$ the **data** $p_0=p^*$ and $t=1$ the noisy end, on the grid $0,\Delta t,\dots,1$ with $\Delta t=1/T$ ($T$ = number of steps, not a horizon) (eq. 1.9-1.10, p. 8). After Section 1.3 subscripts denote time, not index (p. 8).
- $p_t$ is the marginal of $x_t$; $\sigma_q$ is the terminal std-dev scale; per-step noise is $\mathcal N(0,\sigma_q^2\Delta t)$ and $\sigma_t:=\sigma_q\sqrt t$ (eq. 1.11-1.12, p. 9).
- $\mu_t(z):=\mathbb E[x_t\mid x_{t+\Delta t}=z]$ (eq. 2.1, p. 10), so the reverse step uses $\mu_{t-\Delta t}(x_t)=\mathbb E[x_{t-\Delta t}\mid x_t]$.
- Flows: $v_t$ is a velocity field with $dx_t/dt=-v_t(x_t)$ run from $t=1$ down to $t=0$ (eq. 4.1, p. 35); $\mathrm{RunFlow}(v,x_1,t)$ is its solution; this is the opposite time convention to most flow-matching papers, which put the target at $t=1$ (footnote 2, p. 35).
- The forward process is "variance exploding" (VE) with $f=0$, $g=\sigma_q$ (p. 18, footnote 1 p. 10); a variance-preserving (VP) version appears only as eq. 5.1 (p. 47).

### Chapter 1: Gaussian diffusion setup (Section 1, pp. 3-9)

> [!definition] Gaussian diffusion forward process ([[Diffusion models]], [[Noise schedule]])
> $$x_{t+\Delta t}=x_t+\eta_t,\qquad \eta_t\sim\mathcal N(0,\sigma_q^2\Delta t)\qquad(1.11)$$
> $$x_t\sim\mathcal N(x_0,\sigma_t^2),\qquad \sigma_t=\sigma_q\sqrt t\qquad(1.12)$$
> The $\sqrt{\Delta t}$ scaling (eq. 1.10, $\sigma=\sigma_q\sqrt{\Delta t}$) makes the terminal variance independent of the step count.
>
> (source: Nakkiran PDF, eqs. 1.10-1.12, pp. 8-9)

> [!definition] Reverse sampler
> A reverse sampler for step $t$ is a (possibly stochastic) map $F_t$ with $\{F_t(z):z\sim p_t\}\equiv p_{t-\Delta t}$, i.e. $F_t$ pushes $p_t$ to $p_{t-\Delta t}$. The tutorial's abstract diffusion model is any chain $p_0=p^*,\dots,p_T=q$ plus learned reverse samplers; nothing requires Gaussian noise or even "adding noise" (p. 7, Definition 1.1, eq. 1.8, and footnote 10).
>
> (source: Nakkiran PDF, Def. 1.1, p. 7)

Key moves:

- **Fact 1.1** (p. 5): for small $\sigma$, $p(x_{t-1}\mid x_t=z)\approx\mathcal N(\mu,\sigma^2)$ for some mean $\mu$, so only the mean must be learned.
- Learning that mean is regression: $\mu_{t-1}(z)=\mathbb E[x_{t-1}\mid x_t=z]=\arg\min_f\mathbb E\|f(x_t)-x_{t-1}\|^2$ (eqs. 1.4-1.6, p. 6). For images this is a denoising objective.
- Couplings: given marginals $\{p_t\}$ there are many joint laws, so there is no canonical reverse sampler (footnote 11, p. 8).

### Chapter 2: DDPM, the stochastic reverse sampler (Section 2, pp. 10-20)

> [!algorithm] Stochastic reverse sampler, DDPM-like ([[DDPM]])
> $$x_{t-\Delta t}=\mu_{t-\Delta t}(x_t)+\mathcal N(0,\sigma_q^2\Delta t)\qquad(2.3)$$
> Start from $x_1\sim\mathcal N(0,\sigma_q^2)$ and iterate to $t=0$. Training: $\mu_t=\arg\min_f\mathbb E\|f(x_{t+\Delta t})-x_t\|^2$ (eq. 2.2), with $t\sim\mathrm{Unif}[0,1]$ and a shared network $f_\theta(x,t)$ (Pseudocodes 1-2, p. 15; footnote 2, p. 11).
>
> (source: Nakkiran PDF, Alg. 2.1, eqs. 2.2-2.3, pp. 10-11)

> [!theorem] Claim 2.1 (informal): Gaussian reverse step, "pointwise" correctness
> Let $p_{t-\Delta t}$ be a sufficiently smooth density, $x_t\sim x_{t-\Delta t}+\mathcal N(0,\sigma_q^2\Delta t)$. For small $\Delta t$ and every conditioning $z$,
> $$p(x_{t-\Delta t}\mid x_t=z)\approx\mathcal N(x_{t-\Delta t};\mu_z,\sigma_q^2\Delta t)\qquad(2.4)$$
> and it suffices to take
> $$\mu_z=\mathbb E[x_{t-\Delta t}\mid x_t=z]=z+(\sigma_q^2\Delta t)\nabla\log p_t(z)\qquad(2.5)\text{-}(2.6)$$
>
> (source: Nakkiran PDF, Claim 2.1, pp. 11-12)

> [!proof] Sketch (pp. 12-13, eqs. 2.7-2.8)
> Bayes: $p(x_{t-\Delta t}\mid x_t)=p(x_t\mid x_{t-\Delta t})\,p_{t-\Delta t}(x_{t-\Delta t})/p_t(x_t)$. Take logs, treat $x_t$ as constant, drop $O(\Delta t)$ terms (the quadratic $\tfrac1{2\sigma_q^2\Delta t}\|x_{t-\Delta t}-x_t\|^2$ is $O(1)$ and is kept). Replace $p_{t-\Delta t}$ by $p_t$ (error $\Delta t\,\partial_tp_t$), Taylor-expand $\log p_t$ about $x_t$ to first order, and complete the square. The result is a Gaussian centred at $x_t+\sigma_q^2\Delta t\,\nabla\log p_t(x_t)$ with variance $\sigma_q^2\Delta t$. The forward likelihood dominates, which is why forward and reverse steps have the same Gaussian form.

> [!theorem] Lemma 2.1 (per-step KL error; proof in Appendix B.1, pp. 57-60)
> For a density $p$ on $\mathbb R$ with bounded 1st-4th derivatives, $x_0\sim p$, $x_1\sim x_0+\mathcal N(0,\sigma^2)$:
> $$\mathrm{KL}\big(\mathcal N(\mu_z,\sigma^2)\,\|\,p_{x_0\mid x_1}(\cdot\mid x_1=z)\big)\le O(\sigma^4),\quad \mu_z=z+\sigma^2\nabla\log p(z)\quad(2.9)\text{-}(2.10)$$
> Since the number of steps grows only as $\Omega(1/\sigma^2)$ and KL chain-rules additively, per-step errors sum to a vanishing total (p. 14, footnote 6). The proof Taylor-expands $F=\log p$ at $z=0$ and shows the $O(\sigma^2)$ terms cancel only for $\mu^*=F'(0)\sigma^2$ (eqs. B.36-B.40, p. 60). The paper states the lemma only for $d=1$.
>
> (source: Nakkiran PDF, Lemma 2.1, p. 14; Lemma B.1, p. 57)

Remarks on the chapter:

- Footnote 3 (p. 12): Tweedie's formula makes the mean $z+\sigma_q^2\Delta t\nabla\log p_t(z)$ exactly correct for any $\Delta t$; only the *Gaussian shape* of the conditional degrades for large $\Delta t$.
- **Predicting $x_0$ (variance reduction)** (Section 2.3, pp. 16-17):

> [!theorem] Claim 2.2
> $$\mathbb E[x_{t-\Delta t}-x_t\mid x_t]=\frac{\Delta t}{t}\,\mathbb E[x_0-x_t\mid x_t]\qquad(2.11)$$
> $$\mathbb E[x_{t-\Delta t}\mid x_t]=\frac{\Delta t}{t}\,\mathbb E[x_0\mid x_t]+\Big(1-\frac{\Delta t}{t}\Big)x_t\qquad(2.12)$$
> Reason: given $x_t$ the $t/\Delta t$ past noise steps are exchangeable, so each has conditional mean equal to the average (proof sketch, Appendix B.8, p. 66). Variance-reduced training/sampling: Pseudocodes 6-7, Appendix B.9, p. 67, using $f_\theta(x,t)=(\Delta t/t)g_\theta(x,t)+(1-\Delta t/t)x$ (B.63).
>
> (source: Nakkiran PDF, Claim 2.2, p. 16; Appendix B.8-B.9, pp. 66-67)

The tutorial warns that a network trained to output $\mathbb E[x_0\mid x_t]$ is not "sampling $p(x_0\mid x_t)$"; for images it outputs a blurry mean (p. 17).

- **Diffusions as SDEs [optional]** (Section 2.4, pp. 17-20; see [[Diffusion models#Reverse-time SDE]] and [[Score SDE (Song 2021)]]):

> [!definition] Limiting SDE and reverse SDE
> Limit of (1.11): $dx=\sigma_q\,dw$ (eq. 2.13). General form $dx=f(x,t)\,dt+g(t)\,dw$ (eq. 2.14, p. 18). Anderson's time reversal (cited to Anderson 1982, re-derived in Winkler):
> $$dx=\big(f(x,t)-g(t)^2\nabla_x\log p_t(x)\big)\,dt+g(t)\,dw\qquad(2.15)$$
> For the simple diffusion, with $\sigma_q^2\nabla\log p_t(x_t)=\tfrac1t\mathbb E[x_0-x_t\mid x_t]$ (eq. 2.16, p. 20, from Tweedie):
> $$dx=-\sigma_q^2\nabla_x\log p_t\,dt+\sigma_q\,dw=-\tfrac1t\mathbb E[x_0-x_t\mid x_t]\,dt+\sigma_q\,dw\qquad(2.17)\text{-}(2.18)$$
> Its discretization gives $x_{t-\Delta t}=\mathbb E[x_{t-\Delta t}\mid x_t]+\mathcal N(0,\sigma_q^2\Delta t)$ (eqs. 2.19-2.20), i.e. Algorithm 2.1 is Euler-Maruyama on (2.17).
>
> (source: Nakkiran PDF, eqs. 2.13-2.20, pp. 18-20)

Noise schedules as SDEs (p. 19): $x_t\sim\mathcal N(x_0,\sigma_t^2)$ for a general schedule $\sigma(t)$ corresponds to $dx=\sqrt{\tfrac{d}{dt}\sigma^2(t)}\,dw$; adding a scaling $s(t)$ (Karras et al.) gives $f(x)=\tfrac{\dot s}{s}x$, $g(t)=s\sqrt{2\dot\sigma\sigma}$ (footnote 10 derives $f$). In the printed text the Karras formula is partly garbled in the extraction; the form above is read from the page and is consistent with $x_t\sim\mathcal N(s x_0,s^2\sigma^2)$ **[verify against PDF p. 19 before relying on it]**.

### Chapter 3: DDIM, the deterministic sampler (Section 3, pp. 21-32)

> [!algorithm] Deterministic reverse sampler, DDIM-like ([[DDIM]], [[DDIM (Song 2021)]])
> $$x_{t-\Delta t}=x_t+\lambda\big(\mu_{t-\Delta t}(x_t)-x_t\big),\qquad \lambda:=\frac{\sigma_t}{\sigma_{t-\Delta t}+\sigma_t}\qquad(3.1)$$
> with $\sigma_t=\sigma_q\sqrt t$. Same network and training as DDPM; only the step differs (Pseudocode 3, p. 15; its loop ends at $t=0$ where $\lambda=1$). Since the sampler is deterministic it cannot sample $p(x_{t-\Delta t}\mid x_t)$; correctness means it is a *transport map*: with $F_t(z)=z+\lambda(\mathbb E[x_{t-\Delta t}\mid x_t=z]-z)$, show $F_{t\#}p_t\approx p_{t-\Delta t}$ (eqs. 3.2-3.4, p. 22).
>
> (source: Nakkiran PDF, Alg. 3.1, eq. 3.1, p. 21)

Proof strategy (p. 22): prove it for a single point mass, lift to mixtures by averaging velocity fields, then to arbitrary $p_0$ (the last step is deferred to Chapter 4).

> [!theorem] Claim 3.1: point-mass target (pp. 22-24; Claim B.1, p. 61)
> If $p_0=\delta_0$ then $p_t=\mathcal N(0,\sigma_t^2)$, $\mathbb E[x_{t-\Delta t}\mid x_t]=\tfrac{\sigma_{t-\Delta t}^2}{\sigma_t^2}x_t$ (eq. 3.7), and $F_t\equiv G_t$ where
> $$G_t(z)=\frac{\sigma_{t-\Delta t}}{\sigma_t}\,z\qquad(3.5)$$
> simply rescales the Gaussian $\mathcal N(0,\sigma_t^2)$ to $\mathcal N(0,\sigma_{t-\Delta t}^2)$. For a general point $x_0$: $G_t[x_0](x_t)=\tfrac{\sigma_{t-\Delta t}}{\sigma_t}(x_t-x_0)+x_0$ (B.41), and $G_t[x_0]=F_t$ (B.42).
>
> (source: Nakkiran PDF, Claim 3.1, p. 23; Claim B.1, p. 61)

> [!definition] DDIM velocity field and the "gas" picture
> $$v_t(x_t):=\frac{\lambda}{\Delta t}\big(\mathbb E[x_{t-\Delta t}\mid x_t]-x_t\big),\qquad x_{t-\Delta t}=x_t+v_t(x_t)\Delta t\qquad(3.8)\text{-}(3.10)$$
> Non-interacting particles with density $p_t$ moving with velocity $v_t$ produce density $p_{t-\Delta t}$, written $p_t\xrightarrow{v_t}p_{t-\Delta t}$ (3.11). For $p_0=\delta_{x_0}$: $v_t(x_t)=\frac{\sigma_t-\sigma_{t-\Delta t}}{\sigma_t}\,\frac{x_0-x_t}{\Delta t}$, pointing at $x_0$ (p. 24, Fig. 3.1).
>
> (source: Nakkiran PDF, eqs. 3.8-3.11, p. 24)

> [!theorem] Two-point (mixture) case: density-weighted velocities (pp. 25-28)
> For $p_0=\tfrac12\delta_a+\tfrac12\delta_b$, $p_t=\tfrac12\mathcal N(a,\sigma_t^2)+\tfrac12\mathcal N(b,\sigma_t^2)$ (3.12-3.13). The correct combined field is the posterior-weighted average, **not** the plain average:
> $$v_t^*(x_t)=v_t^{[a]}(x_t)\,p(x_0{=}a\mid x_t)+v_t^{[b]}(x_t)\,p(x_0{=}b\mid x_t)\qquad(3.17)\text{-}(3.18)$$
> and rewriting each term as a conditional expectation gives $v_t^*=\lambda\,\mathbb E[x_{t-\Delta t}-x_t\mid x_t]=v_t$ (eqs. 3.19-3.24). So (3.1) is correct for two points; the same argument gives arbitrary $p_0$ (Section 3.4, p. 28, via Chapter 4). A caveat (footnote 11, p. 26): the "combine locally" argument needs infinitesimal steps.
>
> (source: Nakkiran PDF, eqs. 3.12-3.24, pp. 25-28)

> [!definition] Probability-flow ODE, optional (Section 3.5, pp. 28-29; see [[Diffusion models#Probability-flow ODE]], [[Fokker-Planck equation]])
> For the SDE (2.14), Song et al. show the deterministic ODE with the same marginals
> $$\frac{dx}{dt}=\tilde f(x,t),\qquad \tilde f(x,t)=f(x,t)-\tfrac12g(t)^2\nabla_x\log p_t(x)\qquad(3.25)$$
> Sketch (Appendix B.2, p. 60): rewrite Fokker-Planck $\partial_tp_t=-\nabla\!\cdot(fp_t)+\tfrac12g^2\nabla^2p_t$ using $\nabla^2p_t=\nabla\!\cdot(p_t\nabla\log p_t)$, so the diffusion term is absorbed into a drift and $\partial_tp_t=-\nabla\!\cdot(\tilde fp_t)$. The SDE-to-Fokker-Planck step is outlined via Itô's formula in 1-d with constant $g$ (p. 61).
> For the simple diffusion ($f=0,g=\sigma_q$):
> $$\frac{dx}{dt}=-\tfrac12\sigma_q^2\nabla_x\log p_t(x)=-\frac1{2t}\mathbb E[x_0-x_t\mid x_t]\qquad(3.26)\text{-}(3.27)$$
> Reversing and discretizing gives $x_{t-\Delta t}=x_t+\tfrac12(\mathbb E[x_{t-\Delta t}\mid x_t]-x_t)$, and since $\lim_{\Delta t\to0}\lambda=\tfrac12$ this is DDIM (3.1).
>
> (source: Nakkiran PDF, eqs. 3.25-3.27, pp. 28-29; App. B.2, p. 60)

DDPM vs DDIM (Section 3.6, pp. 30-31): both step in the same direction ($\propto\mu_{t-\Delta t}(x_t)-x_t$, footnote 15) but behave differently. Ideal DDPM outputs a sample of $p(x_0\mid x_1)\approx p(x_0)$ regardless of $x_1$ when the forward process mixes; ideal DDIM is a fixed deterministic map $\mathbb R^d\to\mathbb R^d$ determined by $p^*$ (unlike GANs or normalizing flows, whose noise-to-data map is free; see [[Normalizing flows]]). Generalization and memorization (Section 3.7, pp. 31-32): exact ERM reproduces training points; Figure 3.3 (3-layer ReLU net, 128 units) shows DDIM trajectories on a spiral collapsing to training points at $N=10$ and converging to the spiral manifold, increasingly perpendicular to it, as $N$ grows to 20 and 40.

### Chapter 4: Flow matching and pointwise flows (Section 4, pp. 33-45; see [[Flow matching]])

> [!definition] Flow and RunFlow
> A flow is a family of time-indexed vector fields $v=\{v_t\}_{t\in[0,1]}$, run from $x_1$ by $\frac{dx_t}{dt}=-v_t(x_t)$ (4.1), $x_t=\mathrm{RunFlow}(v,x_1,t)$ (4.2). Pushing $p_1$ forward gives $p_0=\{\mathrm{RunFlow}(v,x_1,0)\}_{x_1\sim p_1}$ (4.3), written $p_1\xrightarrow{v}p_0$. Goal: learn $v^*$ with $q\xrightarrow{v^*}p$ for an easy base $q$. Discrete analogue: $x_{t-\Delta t}=x_t+v_t(x_t)\Delta t$ (footnote 1, p. 35).
>
> (source: Nakkiran PDF, eqs. 4.1-4.3, pp. 35-36)

> [!definition] Pointwise flow and marginal flow
> A pointwise flow $v^{[x_1,x_0]}$ is any flow whose trajectory joins $x_1$ at $t=1$ to $x_0$ at $t=0$; it transports $\delta_{x_1}\to\delta_{x_0}$ and is not unique (p. 36). Given a coupling $\Pi_{q,p}$ of base and target, the **marginal flow** averages pointwise velocities over the posterior:
> $$v_t^*(x_t):=\mathbb E_{x_0,x_1\mid x_t}\big[v_t^{[x_1,x_0]}(x_t)\mid x_t\big]\qquad(4.6)$$
> where $(x_1,x_0)\sim\Pi_{q,p}$ and $x_t=\mathrm{RunFlow}(v^{[x_1,x_0]},x_1,t)$. It transports $q\to p$ (footnote 9, eqs. 4.4-4.5). Formal version, the Flow Combining Lemma: for any distribution $\Gamma$ over (flow, initial distribution) pairs, $v_t^*(x_t)=\mathbb E[v_t(x_t)\mid x_t]$ transports $\mathbb E[q_v]\to\mathbb E[v(q_v)]$ (Lemma B.2, eqs. B.44-B.46, pp. 62-63).
>
> (source: Nakkiran PDF, eq. 4.6, p. 38; Lemma B.2, pp. 62-63)

> [!algorithm] Flow matching with linear pointwise flows ([[Flow matching]])
> Linear pointwise flow: $v_t^{[x_1,x_0]}(x_t)=x_0-x_1$ (4.7), with trajectory $x_t=tx_1+(1-t)x_0$ (4.8), the rectified-flow choice of Liu et al. Because $v^*$ is a conditional expectation it is the minimizer of a regression:
> $$v_t^*=\arg\min_f\ \mathbb E_{(x_0,x_1,x_t)}\big\|f(x_t)-v_t^{[x_1,x_0]}(x_t)\big\|_2^2\qquad(4.9)\text{-}(4.10)$$
> Train (Pseudocode 4, p. 42): sample $(x_1,x_0)\sim\Pi_{q,p}$, $t\sim\mathrm{Unif}[0,1]$, set $x_t=tx_1+(1-t)x_0$, loss $\|f_\theta(x_t,t)-(x_0-x_1)\|^2$. Sample (Pseudocode 5, p. 43): $x_1\sim q$, iterate $x_{t-\Delta t}=x_t+f_\theta(x_t,t)\Delta t$ down to $t=0$. The ingredients checklist (source $q$, coupling $\Pi$, pointwise flow) is on pp. 41-42, eq. 4.11. The independent coupling is the standard choice. Footnote 12 (p. 40) compares eq. 4.10 to Theorem 2 of Lipman et al., which is one-sided; this is the two-sided version.
>
> (source: Nakkiran PDF, eqs. 4.7-4.11, pp. 39-42; Pseudocodes 4-5)

> [!theorem] Claim 4.1 (informal): DDIM is a linear flow, reparametrized in time
> DDIM (Alg. 3.1) is flow matching with the "diffusion coupling" $x_0\sim p$, $x_1\leftarrow x_0+\mathcal N(0,\sigma_q^2)$ (4.15) and either pointwise flow
> $$v_t^{[x_1,x_0]}(x_t)=\frac1{2t}(x_t-x_0)\ (4.12)\quad\text{or}\quad\frac1{2\sqrt t}(x_0-x_1)\ (4.13),$$
> both generating $x_t=x_0+(x_1-x_0)\sqrt t$ (4.14). Hence DDIM trajectories equal those of the linear flow (4.7) with the diffusion coupling at time $\sqrt t$ (footnote 15, p. 44). Formal statement: Lemma B.3, $y_t=z_{\sqrt t}$ (eq. B.52, p. 66). Derivations: DDIM from flows, Appendix B.5 (pp. 63-64); equivalence of (4.12) and (4.13), Appendix B.6 (pp. 64-65).
>
> (source: Nakkiran PDF, eqs. 4.12-4.15, p. 43; Claim 4.1, p. 44)

Remarks (pp. 44-45): the independent coupling is close to the diffusion coupling for large $\sigma_q^2$, so the common practice (linear flows, Gaussian base, independent coupling) is nearly DDIM with a different time schedule (footnote 16). This holds only for the VE form; the paper states Claim 4.1 is false for VP-DDIM. No explicit forward process is needed for flow matching. Related: stochastic interpolants (Albergo et al.) use stochastic pointwise flows and generalize DDPM and DDIM; "pointwise flows" are called two-sided conditional flows elsewhere.

### Chapter 5: SDE vs ODE samplers, discretization, practical guidance (Section 5, pp. 46-51)

Figure 5.1 (p. 50) is a commutative diagram: DDPM (Section 2) and DDIM (Section 3) on the discrete row; Reverse-SDE (Section 2.4) and PF-ODE (Section 3.5, a flow of Section 4) on the continuous row. Vertical arrows are $\Delta t\to0$ limits; horizontal arrows turn a stochastic sampler into its deterministic counterpart with identical marginals.

- **Samplers** (p. 46-47): DDPM and DDIM correspond to Ho et al. and Song et al. up to schedule and parametrization (see [[DDPM (Ho 2020)]], [[DDIM (Song 2021)]]). Because DDPM/DDIM are discretizations of the reverse SDE/PF-ODE, any black-box SDE or ODE solver (Euler, Heun, Runge-Kutta) gives a sampler, and exponential-integrator-type solvers exploiting the diffusion ODE's structure (DPM-Solver, DPM-Solver++) do better. Footnote 1: even the best samplers still need around 10 steps; distillation (consistency models, adversarial distillation) yields one-step students that are no longer diffusion samplers.
- **Noise schedules** (p. 47): the simple diffusion has $\mathrm{Var}(x_t)\propto t$, which grows. Ho et al.'s VP update is
  $$x_t=\sqrt{1-\beta(t)}\,x_{t-1}+\sqrt{\beta(t)}\,\varepsilon_t,\quad\varepsilon_t\sim\mathcal N(0,1)\qquad(5.1)$$
  with $f=-\tfrac12\beta(t)x$. Karras et al. parametrize by scaling $s(t)$ and std-dev $\sigma(t)$ and suggest $s=1$, $\sigma(t)=t$ (i.e. $f=0$, $g=\sqrt{2t}$). VE vs VP naming follows Song et al.
- **ELBO / VAE view** (pp. 47-48): the diffusion chain is a deep hierarchical VAE with a fixed encoder; the ELBO reduces to the same $L_2$ regression with a time-weighting. The "principled" ELBO weighting does not always give the best samples; Ho et al. drop the weights (footnote 5).
- **Parametrizations** (pp. 48-49, Appendix B.10 p. 68): $x_0$-prediction ($\min\|f_\theta-x_0\|^2\Rightarrow f^*=\mathbb E[x_0\mid x_t]$), $\varepsilon$-prediction ($f^*=\mathbb E[\varepsilon_t\mid x_t]$) and $v$-prediction ($v=\alpha_t\varepsilon-\sigma_tx_0$, Salimans-Ho) are equivalent up to time-weightings: $1/t$ for $x_0$, $1/(t\sigma_t)$ for $\varepsilon$ relative to the base objective (B.10 p. 68, as printed). They share the optimum but differ in training behaviour; e.g. $x_0$-prediction with weight concentrated at low noise can fail because the identity map already scores well there.
- **Sources of error** (pp. 49-51): (1) train-time regression error (approximation plus estimation); (2) sampling-time discretization error, which for DDPM is the failure of the Gaussian approximation (Fact 1.1 breaks for large $\sigma$) and for DDIM/flow matching the error of simulating a flow in discrete time. How they compound is "not yet fully understood", and they can act as beneficial regularization against memorization (pp. 50-51).

## Results

This is a tutorial; it reports no benchmark numbers. Concrete findings:

- Per-step KL error of the Gaussian reverse approximation is $O(\sigma^4)$ for smooth 1-d densities (Lemma 2.1, p. 14), enough to sum over $\Omega(1/\sigma^2)$ steps.
- The DDIM update equals a rescaling for a point-mass target (Claim 3.1, p. 23) and extends by density-weighted velocity averaging (eq. 3.18, p. 26) to mixtures and, via flow matching, to arbitrary $p_0$.
- The limit $\lambda\to\tfrac12$ links DDIM to the PF-ODE (p. 29), and DDIM equals the linear flow under $t\mapsto\sqrt t$ (Claim 4.1, p. 44).
- Toy experiment (Figure 3.3, p. 32): a 3-layer, 128-unit ReLU network on a spiral memorizes at $N=10$ training points (all trajectories collapse to training points) and generalizes toward the spiral manifold as $N$ increases to 20 and 40. No quantitative metric is given.

## Limitations

As stated by the authors:

- Key arguments are heuristic: Claim 2.1 and Claim 4.1 are "informal"; the rigorous Lemma 2.1 is proved only in $d=1$ with bounded derivatives (pp. 11, 14, 44).
- Mixture correctness of DDIM relies on infinitesimal steps (footnote 11, p. 26); the discrete-step error is the sampling error of Section 5.
- Learning theory (generalization, memorization, how train-time error maps to distributional error) is out of scope and "not yet fully understood" (pp. 31, 50).
- Uses a VE forward process, constant schedule, and does not treat $x_0/\varepsilon$-parametrization in the main text; Claim 4.1 is false for VP-DDIM (footnotes 1, p. 10; 16, p. 44).
- Guidance, latent diffusion, discrete diffusion beyond a remark, and distillation are only mentioned (Section 5, Appendix A).

Wiki notes (not from the paper):

- Eq. (5.x) text on p. 49 defines $\varepsilon_t=\frac1{\sigma_t}\mathbb E[x_0-x_t\mid x_t]$ and Appendix B.10 (p. 68) writes $\mathbb E[x_0-x_t\mid x_t]\equiv\sigma_t\mathbb E[\varepsilon_t\mid x_t]$ as printed. With the paper's own $x_t=x_0+\sigma_t\varepsilon_t$ (B.10) one has $\varepsilon_t=(x_t-x_0)/\sigma_t$, so the sign appears flipped in print. The $L_2$ losses and time-weights are unaffected. **[unverified: my reading, not an erratum from the authors]**
- Lemma B.3 (p. 65) states $\mathbb E[x_1\mid x_t]=x_t$ under the diffusion coupling to get $v_t^*=\mathbb E[x_0-x_t\mid x_t]$. Computing directly with $x_s=x_0+s(x_1-x_0)$, $x_1-x_0\sim\mathcal N(0,\sigma_q^2)$ I get $\mathbb E[x_0-x_1\mid x_s]=\tfrac1s\mathbb E[x_0-x_s\mid x_s]$, and the extra $1/s$ is exactly what the time change $s=\sqrt t$ in (B.52) needs ($ds=dt/2\sqrt t$ yields $1/(2t)$ in (3.27)). So Claim 4.1 stands; the printed intermediate line looks like a dropped factor. **[unverified]**
- Printed lemma numbering: Lemma 2.1 in the body is restated as Lemma B.1 in the appendix (p. 57); equation numbers (2.9)-(2.10) correspond to (B.1)-(B.2).
- Wiki's folder map in CLAUDE.md has no `Diffusion/` entry; area assigned as `stochastic` with `ml` secondary, matching [[Score SDE (Song 2021)]].

## Connections

- **Original DDPM and DDIM**: this tutorial re-derives [[DDPM (Ho 2020)]] and [[DDIM (Song 2021)]] in a simplified VE setting; details like constants and parametrization differ (footnote 1, p. 10; p. 46). The tutorial gives DDIM as velocity-field transport rather than via non-Markovian forward processes ("implicit" is unimportant, footnote 1, p. 21).
- **[[Score SDE (Song 2021)]]**: reverse SDE (2.15) and PF-ODE (3.25) are Song et al.'s results (eqs. 6 and 13 there); the tutorial presents them as optional continuous-time limits and proves PF-ODE only by sketch via Fokker-Planck ([[Fokker-Planck equation]]). It names Song's VE/VP split and treats its own forward process as VE. The score appears via (2.6) and (2.16), tied to [[Score matching]] only through Tweedie's formula.
- **[[Flow matching]]**: Chapter 4 is a self-contained derivation of flow matching/rectified flow with a time convention reversed relative to Lipman et al. and Liu et al.; pointwise flows = two-sided conditional flows.
- **[[Langevin dynamics]]**: deliberately not used; the paper notes that experts will recognize the mean as the score (p. 12).
- **[[Normalizing flows]]**: DDIM and flow matching define Gaussian-to-data maps like flows and GANs, but the ideal map is fixed by $p^*$ (p. 30).
- **Within the wiki**: [[Diffusion models]] is the hub; this tutorial supplies the elementary correctness arguments.

**Sources**: `Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]] (hubs: [[Diffusion models#SMLD and DDPM]], [[Diffusion models#Reverse-time SDE]], [[Diffusion models#Probability-flow ODE]])
- [[DDPM]], [[DDIM]], [[Noise schedule]]
- [[Flow matching]], [[Score matching]], [[Langevin dynamics]], [[Fokker-Planck equation]], [[Normalizing flows]]
- [[Score SDE (Song 2021)]], [[DDPM (Ho 2020)]], [[DDIM (Song 2021)]]
