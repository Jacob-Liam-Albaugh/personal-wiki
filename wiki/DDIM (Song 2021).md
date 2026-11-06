---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Song, Meng, Ermon 2021, ICLR, eqs. 5-7, 9-16; Thm. 1; Prop. 1; Tables 1-3"
tags: [diffusion, generative, sampling]
authors: [Song, Meng, Ermon]
year: 2021
venue: "ICLR 2021 (arXiv:2010.02502v4)"
file: "Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf"
---

# Denoising Diffusion Implicit Models (Song 2021)

**Summary**: Generalises DDPM's Markovian forward process to a family of non-Markovian processes with the same marginals $q(x_t|x_0)$, indexed by a variance vector $\sigma$. All members share the DDPM training objective up to weights (Theorem 1), so a pretrained DDPM can be reused with a different sampler. The $\sigma=0$ member (DDIM) is deterministic, can skip steps via a sub-sequence $\tau$, and gives 10x to 50x faster sampling at modest quality loss, plus latent interpolation and near-exact reconstruction.

**Authors**: Jiaming Song, Chenlin Meng, Stefano Ermon (Stanford) · **Year**: 2021 · **File**: `Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`

---

## Problem

DDPMs ([[DDPM (Ho 2020)]]) need many sequential steps per sample because the generative chain approximates the reverse of a forward chain with up to thousands of steps. The paper's numbers: about 20 hours to sample 50k 32x32 images from a DDPM versus under a minute from a GAN on an Nvidia 2080 Ti, and nearly 1000 hours for 50k 256x256 images (p. 1). Goal: fewer steps without retraining, in the [[Diffusion models]] family.

## Method

**Notation.** This paper writes $\alpha_t$ for what [[DDPM (Ho 2020)]] calls $\bar\alpha_t=\prod_s(1-\beta_s)$, and $\alpha_t/\alpha_{t-1}$ for DDPM's $\alpha_t$ (App. C.2, p. 17, eqs. 60-61). Convention $\alpha_0:=1$. Below, "DDPM $\alpha$" means $\bar\alpha$ in Ho's notation.

> [!definition] DDPM forward process, reparameterised
> $$q(x_t\mid x_{t-1})=\mathcal N\Big(\sqrt{\tfrac{\alpha_t}{\alpha_{t-1}}}\,x_{t-1},\Big(1-\tfrac{\alpha_t}{\alpha_{t-1}}\Big)I\Big),\quad q(x_t\mid x_0)=\mathcal N(\sqrt{\alpha_t}x_0,(1-\alpha_t)I)$$
> $$x_t=\sqrt{\alpha_t}\,x_0+\sqrt{1-\alpha_t}\,\epsilon,\ \epsilon\sim\mathcal N(0,I)$$
> (source: Song, Meng, Ermon - DDIM, eqs. 3-4, pp. 2-3)

> [!definition] Weighted denoising objective $L_\gamma$
> $$L_\gamma(\epsilon_\theta)=\sum_{t=1}^T\gamma_t\,\mathbb E_{x_0,\epsilon_t}\big[\|\epsilon^{(t)}_\theta(\sqrt{\alpha_t}x_0+\sqrt{1-\alpha_t}\epsilon_t)-\epsilon_t\|_2^2\big]$$
> with $T$ separate functions $\epsilon_\theta^{(t)}$ and positive weights $\gamma$ depending on $\alpha_{1:T}$. Ho et al. use $\gamma=\mathbf 1$ (this is $L_\text{simple}$, see [[Noise prediction]]; also the NCSN objective). (source: eq. 5, p. 3)

The key observation (p. 3): $L_\gamma$ depends on the joint $q(x_{1:T}|x_0)$ only through the marginals $q(x_t|x_0)$, and many joints share those marginals.

> [!definition] Non-Markovian inference family $Q_\sigma$
> For $\sigma\in\mathbb R^T_{\ge0}$:
> $$q_\sigma(x_{1:T}\mid x_0)=q_\sigma(x_T\mid x_0)\prod_{t=2}^T q_\sigma(x_{t-1}\mid x_t,x_0),\quad q_\sigma(x_T|x_0)=\mathcal N(\sqrt{\alpha_T}x_0,(1-\alpha_T)I)$$
> $$q_\sigma(x_{t-1}\mid x_t,x_0)=\mathcal N\Big(\sqrt{\alpha_{t-1}}\,x_0+\sqrt{1-\alpha_{t-1}-\sigma_t^2}\cdot\frac{x_t-\sqrt{\alpha_t}x_0}{\sqrt{1-\alpha_t}},\ \sigma_t^2 I\Big)$$
> (source: eqs. 6-7, p. 3)

> [!theorem] Lemma 1 (marginals preserved)
> $q_\sigma(x_t|x_0)=\mathcal N(\sqrt{\alpha_t}x_0,(1-\alpha_t)I)$ for all $t$. Proof by backward induction using the Gaussian marginalisation formula (Bishop 2.115): mean $\sqrt{\alpha_{t-1}}x_0$, covariance $\sigma_t^2I+\frac{1-\alpha_{t-1}-\sigma_t^2}{1-\alpha_t}(1-\alpha_t)I=(1-\alpha_{t-1})I$. (source: eq. 22, App. B, pp. 13-14)

The forward step follows from Bayes (eq. 8, p. 3) and is no longer Markovian: $x_t$ depends on both $x_{t-1}$ and $x_0$. As $\sigma\to0$, observing $x_0$ and $x_t$ fixes $x_{t-1}$ (p. 4).

**Generative process.** Predict $x_0$ from $x_t$, then use $q_\sigma(x_{t-1}|x_t,\cdot)$:

> [!definition] Predicted $x_0$ and generative kernel
> $$f_\theta^{(t)}(x_t)=\big(x_t-\sqrt{1-\alpha_t}\,\epsilon^{(t)}_\theta(x_t)\big)/\sqrt{\alpha_t}\quad\text{(eq. 9)}$$
> $$p^{(t)}_\theta(x_{t-1}|x_t)=\begin{cases}\mathcal N(f^{(1)}_\theta(x_1),\sigma_1^2I)&t=1\\ q_\sigma(x_{t-1}|x_t,f^{(t)}_\theta(x_t))&t>1\end{cases}\quad\text{(eq. 10)}$$
> with $p_\theta(x_T)=\mathcal N(0,I)$. The $t=1$ noise keeps the process supported everywhere. (source: pp. 4)

> [!theorem] Theorem 1 (same training objective)
> The variational objective $J_\sigma(\epsilon_\theta)=\mathbb E_{q_\sigma}[\log q_\sigma(x_{1:T}|x_0)-\log p_\theta(x_{0:T})]$ (eq. 11) satisfies: for all $\sigma>0$ there exist $\gamma\in\mathbb R^T_{>0}$ and $C\in\mathbb R$ with $J_\sigma=L_\gamma+C$.
> (source: Thm. 1, p. 4; proof eqs. 29-35, App. B, p. 14)

> [!proof] Sketch
> Up to terms independent of $\epsilon_\theta$, $J_\sigma\equiv\sum_{t>1}\mathbb E[D_{KL}(q_\sigma(x_{t-1}|x_t,x_0)\|p^{(t)}_\theta)]-\mathbb E\log p^{(1)}_\theta(x_0|x_1)$ ([[KL divergence]]). Both kernels in the KL are Gaussians with the same variance $\sigma_t^2I$, so the KL equals $\|x_0-f^{(t)}_\theta(x_t)\|^2/(2\sigma_t^2)$ (eq. 30), which with $x_t=\sqrt{\alpha_t}x_0+\sqrt{1-\alpha_t}\epsilon$ becomes $\|\epsilon-\epsilon_\theta^{(t)}(x_t)\|^2/(2d\sigma_t^2\alpha_t)$ (eq. 32; $d$ = dimension of $x_0$, as printed in the paper). Hence $\gamma_t=1/(2d\sigma_t^2\alpha_t)$ (eq. 35).

Consequence (p. 4): if parameters are not shared across $t$, the optimum of $L_\gamma$ does not depend on $\gamma$ (each term is minimised separately), so the DDPM objective $L_1$ is also a valid surrogate for $J_\sigma$ for every $\sigma$, and a pretrained DDPM can be used with any $\sigma$. The theorem does not cover $\sigma=0$ (needs $\sigma>0$); footnote 5 (p. 5): approximate it with tiny $\sigma_t$. Wiki note: in practice $\epsilon_\theta$ shares parameters across $t$, so this is an argument, not an exact guarantee; the paper accepts it empirically.

> [!algorithm] DDIM / generalised update (eq. 12, p. 5)
> $$x_{t-1}=\sqrt{\alpha_{t-1}}\underbrace{\Big(\frac{x_t-\sqrt{1-\alpha_t}\,\epsilon^{(t)}_\theta(x_t)}{\sqrt{\alpha_t}}\Big)}_{\text{predicted }x_0}+\underbrace{\sqrt{1-\alpha_{t-1}-\sigma_t^2}\;\epsilon^{(t)}_\theta(x_t)}_{\text{direction pointing to }x_t}+\underbrace{\sigma_t\epsilon_t}_{\text{random noise}}$$
> with $\epsilon_t\sim\mathcal N(0,I)$ independent of $x_t$, $\alpha_0:=1$.

Special cases:
- $\sigma_t=\sqrt{(1-\alpha_{t-1})/(1-\alpha_t)}\sqrt{1-\alpha_t/\alpha_{t-1}}$: forward process becomes Markovian and the generative process is a DDPM (the posterior std $\tilde\beta_t^{1/2}$ of [[DDPM (Ho 2020)]]) (p. 5).
- $\sigma_t=0$ for all $t$: the noise term vanishes, sampling is a fixed map from $x_T$ to $x_0$, an implicit probabilistic model (Mohamed & Lakshminarayanan 2016). Named **DDIM** "because it is an implicit probabilistic model trained with the DDPM objective (despite the forward process no longer being a diffusion)" (p. 5).

> [!definition] Interpolation parameter $\eta$ (eq. 16, p. 6)
> $$\sigma_{\tau_i}(\eta)=\eta\sqrt{\frac{1-\alpha_{\tau_{i-1}}}{1-\alpha_{\tau_i}}}\sqrt{1-\frac{\alpha_{\tau_i}}{\alpha_{\tau_{i-1}}}}$$
> $\eta=1$ is DDPM, $\eta=0$ is DDIM. Also $\hat\sigma_{\tau_i}=\sqrt{1-\alpha_{\tau_i}/\alpha_{\tau_{i-1}}}$ ("DDPM with larger variance"), the choice in Ho et al.'s released code for CIFAR-10 samples only; more stochastic than $\eta=1$ (pp. 6, 19). Closed-form step (App. D.3, pp. 18-19): eq. 12 with $\tau_i,\tau_{i-1}$ in place of $t,t-1$ and $\sigma_{\tau_i}(\eta)$.

### Accelerated generation (4.2, App. C.1)

Define the inference process only on an increasing sub-sequence $\tau=[\tau_1,\dots,\tau_S]\subset[1,\dots,T]$, $\tau_S=T$, with $q(x_{\tau_i}|x_0)=\mathcal N(\sqrt{\alpha_{\tau_i}}x_0,(1-\alpha_{\tau_i})I)$ (marginals matched). Steps outside $\tau$ form a star graph around $x_0$ (eq. 52). The kernel is eq. 7 with $(t,t-1)\to(\tau_i,\tau_{i-1})$ (eq. 53). The generative process only uses the $\tau$ steps (eq. 55-57); the objective $J$ again reduces to the $L_\gamma$ form (eqs. 58-59), so no retraining is needed (pp. 5, 16-17). Applies to DDPM, DDIM and all kernels in eq. 10. Sub-sequence choices (App. D.2, p. 18): linear $\tau_i=\lfloor ci\rfloor$ or quadratic $\tau_i=\lfloor ci^2\rfloor$, with $c$ chosen so $\tau_{-1}$ is near $T$; quadratic for CIFAR-10, linear for the rest.

### Relation to neural ODEs and the probability-flow ODE (4.3)

Rewriting eq. 12 with $\sigma=0$:

> [!definition] Euler form and ODE
> $$\frac{x_{t-\Delta t}}{\sqrt{\alpha_{t-\Delta t}}}=\frac{x_t}{\sqrt{\alpha_t}}+\Big(\sqrt{\tfrac{1-\alpha_{t-\Delta t}}{\alpha_{t-\Delta t}}}-\sqrt{\tfrac{1-\alpha_t}{\alpha_t}}\Big)\epsilon^{(t)}_\theta(x_t)\quad\text{(eq. 13)}$$
> With $\bar x=x/\sqrt\alpha$ and $\sigma=\sqrt{1-\alpha}/\sqrt\alpha$ (so $x=\bar x/\sqrt{\sigma^2+1}$, $\alpha=1/(1+\sigma^2)$, eqs. 37-40), eq. 13 is an Euler step for
> $$d\bar x(t)=\epsilon^{(t)}_\theta\Big(\frac{\bar x(t)}{\sqrt{\sigma^2+1}}\Big)d\sigma(t)\quad\text{(eq. 14, p. 6)}$$
> with $\bar x(T)\sim\mathcal N(0,\sigma(T)^2 I)$ for very large $\sigma(T)$ (the paper prints $\mathcal N(0,\sigma(T))$; App. B writes $\sigma^2(T)I$, p. 16).

Reading this ODE backwards ($t:0\to T$) encodes $x_0$ to $x_T$, which a DDPM cannot do (p. 6).

> [!theorem] Proposition 1 (equivalence to the VE probability-flow ODE)
> The ODE in eq. 14 with the optimal $\epsilon_\theta$ is equivalent to the probability-flow ODE of the Variance-Exploding SDE of [[Score SDE (Song 2021)]].
> (source: Prop. 1, p. 6; proof eqs. 36-51, App. B, pp. 15-16)

> [!proof] Sketch
> Set $\bar x(t)=\bar x(0)+\sigma(t)\epsilon$ (VE form, eq. 42). The VE probability-flow ODE is $d\bar x=-\tfrac12g(t)^2\nabla\log p_t(\bar x)\,dt$ with $g^2=d\sigma^2/dt$ (eq. 47). The optimal noise predictor and denoising score matching ([[Score matching#Denoising score matching|denoising score matching]]) give $\nabla\log p_t(\bar x)=-\epsilon_\theta(\bar x/\sqrt{\sigma^2+1})/\sigma$ (eq. 49). Substituting yields $d\bar x/dt=(d\sigma/dt)\,\epsilon_\theta(\cdot)$ (eq. 51), identical to eq. 45/14. See [[Diffusion models]], section "Probability-flow ODE".

The ODEs match but the sampling procedures differ. The Euler step on the probability-flow ODE is

> $$\frac{x_{t-\Delta t}}{\sqrt{\alpha_{t-\Delta t}}}=\frac{x_t}{\sqrt{\alpha_t}}+\frac12\Big(\frac{1-\alpha_{t-\Delta t}}{\alpha_{t-\Delta t}}-\frac{1-\alpha_t}{\alpha_t}\Big)\sqrt{\frac{\alpha_t}{1-\alpha_t}}\;\epsilon^{(t)}_\theta(x_t)\quad\text{(eq. 15, p. 6)}$$

which agrees with eq. 13 only when $\alpha_t,\alpha_{t-\Delta t}$ are close. DDIM takes Euler steps in $d\sigma(t)$, the probability-flow sampler in $dt$; the two differ with few steps (p. 6).

## Results

Setup (p. 6, App. D.1): one trained model per dataset, $T=1000$, $\gamma=\mathbf 1$; checkpoints from the DDPM release for CIFAR-10, LSUN Bedroom and Church, own model for CelebA 64x64 (trained with the $L_1$ objective); only the sampler changes ($\tau$, $\sigma$/$\eta$). Metric: FID.

> [!example] Table 1: FID vs. steps $S=\dim(\tau)$ and $\eta$ (p. 7)
> | | CIFAR-10 S=10 | 20 | 50 | 100 | 1000 | CelebA S=10 | 20 | 50 | 100 | 1000 |
> |---|---|---|---|---|---|---|---|---|---|---|
> | $\eta=0.0$ (DDIM) | 13.36 | 6.84 | 4.67 | 4.16 | 4.04 | 17.33 | 13.73 | 9.17 | 6.53 | 3.51 |
> | $\eta=0.2$ | 14.04 | 7.11 | 4.77 | 4.25 | 4.09 | 17.66 | 14.11 | 9.51 | 6.79 | 3.64 |
> | $\eta=0.5$ | 16.66 | 8.35 | 5.25 | 4.46 | 4.29 | 19.86 | 16.06 | 11.01 | 8.09 | 4.28 |
> | $\eta=1.0$ (DDPM) | 41.07 | 18.36 | 8.01 | 5.78 | 4.73 | 33.12 | 26.03 | 18.48 | 13.93 | 5.98 |
> | $\hat\sigma$ | 367.43 | 133.37 | 32.72 | 9.99 | 3.17 | 299.71 | 183.83 | 71.71 | 45.20 | 3.26 |

> [!example] Table 3: LSUN FID (App. D.1, p. 18)
> | $\dim(\tau)$ | Bedroom 10 | 20 | 50 | 100 | Church 10 | 20 | 50 | 100 |
> |---|---|---|---|---|---|---|---|---|
> | DDIM $\eta=0$ | 16.95 | 8.89 | 6.75 | 6.62 | 19.45 | 12.47 | 10.84 | 10.58 |
> | DDPM $\eta=1$ | 42.78 | 22.77 | 10.81 | 6.81 | 51.56 | 23.37 | 11.16 | 8.27 |
>
> 1000-step DDPM FIDs: 6.36 (Bedroom), 7.89 (Church).

Findings:
- Quality improves with $S$, trading compute for quality. DDIM ($\eta=0$) is best at small $S$; DDPM ($\eta=1$ and $\hat\sigma$) is worse at the same $S$, and $\hat\sigma$ collapses at short trajectories (FID 367 at $S=10$) because FID is very sensitive to residual noise (5.1, p. 7). The exceptions: at $S=1000$ the $\hat\sigma$ DDPM of Ho et al. is marginally better (3.17 vs 4.04 on CIFAR-10; 3.26 vs 3.51 on CelebA).
- Wall-clock time is linear in the number of steps (Fig. 4, p. 8). DDIM reaches quality comparable to 1000 steps in 20 to 100 steps, "10x to 50x" faster; abstract says 10x to 50x, the Introduction says 10x to 100x (pp. 1-2). On CelebA a 100-step DDPM ($\eta=1$, FID 13.93) is similar to a 20-step DDIM (13.73) (p. 7).
- **Consistency** (5.2, Fig. 5, p. 7-8): with the same $x_T$, DDIM samples from different $\tau$ share high-level features; 20 steps already resemble 1000 steps. Wiki reading: $x_T$ acts as an informative latent code. The authors' phrasing is that minor detail "is encoded in the parameters" (p. 8).
- **Interpolation** (5.3, Fig. 6, p. 8; App. D.5, p. 19): interpolate two Gaussian $x_T$ by spherical linear interpolation, $x_T^{(\alpha)}=\frac{\sin((1-\alpha)\theta)}{\sin\theta}x_T^{(0)}+\frac{\sin(\alpha\theta)}{\sin\theta}x_T^{(1)}$ with $\theta=\arccos\big(\frac{(x_T^{(0)})^\top x_T^{(1)}}{\|x_T^{(0)}\|\|x_T^{(1)}\|}\big)$ (eq. 67), then decode with DDIM. This gives semantically meaningful interpolations (shown with $\dim\tau=50$). In DDPM the same $x_T$ yields diverse $x_0$.

> [!example] Table 2: DDIM reconstruction error, CIFAR-10 test set (5.4, p. 9)
> Encode $x_0\to x_T$ by running eq. 14 forward, decode back, with $S$ steps for both; per-dimension MSE on $[0,1]$ scale:
> | S | 10 | 20 | 50 | 100 | 200 | 500 | 1000 |
> |---|---|---|---|---|---|---|---|
> | Error | 0.014 | 0.0065 | 0.0023 | 0.0009 | 0.0004 | 0.0001 | 0.0001 |
>
> Error falls with $S$, "similar to Neural ODEs and normalizing flows"; not possible for DDPM because of stochastic sampling (p. 9).

## Limitations

As stated by the authors:
- Theorem 1 excludes $\sigma=0$; footnote 5 approximates it by very small $\sigma_t$ (p. 5).
- Encoding quality was not a goal: $x_T$ and $x_0$ have the same dimension, so "compression qualities are not our immediate concern" (footnote 7, p. 9).
- Empirical study uses the DDPM training procedure unchanged; training with many more steps or continuous $t$ is left to future work (p. 5). Higher-order ODE solvers (e.g. Adams-Bashforth) are proposed as future improvements (p. 10).
- The discrete-case non-Markovian process (App. A, pp. 13) is derived but not evaluated.

Wiki notes:
- Quality gap versus 1000-step DDPM at $S=1000$ is small but real for $\eta=0$ on CIFAR-10 (4.04 vs 3.17 for $\hat\sigma$; Table 1); quality at very small $S$ (10 steps FID 13.36) is still far from 1000 steps.
- The ODE-solver framing implies multistep and adaptive solvers could help; later work does this (e.g. predictor-corrector and ODE solvers in [[Score SDE (Song 2021)]]). The "unified DDIM = Euler" statement is for the specific parameterization in $\bar x,\sigma$ coordinates.
- Sub-sequence $\tau$ selection is a hand-chosen heuristic (linear vs quadratic), picked by FID on each dataset.

## Connections

- Directly generalises [[DDPM (Ho 2020)]]: same $\epsilon_\theta$, same $L_\text{simple}$, new samplers; $\eta=1$ recovers the DDPM ancestral sampler. Method pages: [[DDIM]], [[DDPM]], [[Noise prediction]].
- Proposition 1 ties it to [[Score SDE (Song 2021)]]: DDIM is Euler's method on the (VE) probability-flow ODE in different time coordinates; see [[Diffusion models]], sections "Probability-flow ODE" and "VE, VP and sub-VP SDEs".
- Deterministic invertible sampling gives latent encodings like [[Normalizing flows]] and neural ODEs, and GAN-like latent interpolation ([[GAN]]); in the paper's words, "properties that resemble GANs and invertible flows" (p. 9). Compared with [[VAE]]: DDIM latents have the same dimension as the data.
- Derived "from a purely variational perspective", where the restrictions of [[Langevin dynamics]] are not relevant (p. 9); this is offered as a partial explanation for better few-step quality (the paper's speculation).
- Wiki note: the ODE view foreshadows [[Flow matching]]-style deterministic transport maps.

**Sources**: `Diffusion/Song, Meng, Ermon - Denoising Diffusion Implicit Models.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]]
- [[DDIM]]
- [[DDPM]]
- [[Noise prediction]]
- [[Noise schedule]]
- [[DDPM (Ho 2020)]]
- [[Score SDE (Song 2021)]]
- [[ELBO]]
- [[KL divergence]]
- [[Score matching#Denoising score matching|denoising score matching]]
