---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Song, Sohl-Dickstein, Kingma, Kumar, Ermon, Poole 2021, ICLR, eqs. 5-7, 11-13, 29; Alg. 1-5"
tags: [diffusion, generative, sampling]
authors: ["[[Yang Song]]", "[[Jascha Sohl-Dickstein]]", "[[Diederik P. Kingma]]", "[[Abhishek Kumar]]", "[[Stefano Ermon]]", "[[Ben Poole]]"]
year: 2021
venue: "ICLR 2021 (arXiv:2011.13456v2, 10 Feb 2021)"
file: "papers/Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf"
---

# Score-Based Generative Modeling Through SDEs (Song 2021)

**Summary**: Perturbs data to a known prior with a continuous-time forward SDE, and generates by solving the reverse-time SDE (Anderson 1982), which needs only the time-dependent score $\nabla_x\log p_t(x)$, estimated by a neural network trained with denoising score matching. SMLD and DDPM are shown to be discretizations of the VE and VP SDEs; the framework adds Predictor-Corrector samplers, a probability-flow ODE (exact likelihoods, latent encoding), and conditional sampling for inpainting/colorization. Reported CIFAR-10 results: FID 2.20, IS 9.89 (NCSN++ cont. deep, VE), and 2.99 bits/dim (DDPM++ cont. deep, sub-VP) (p. 7, Tables 2-3).

**Authors**: Yang Song (Stanford), Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon (Stanford), Ben Poole · **Year**: 2021 · **File**: `papers/Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`

Wiki note: the PDF's author order is Song, Sohl-Dickstein, Kingma, Kumar, Ermon, Poole (p. 1); the filename lists Kingma first. First author is Yang Song, hence the slug. The paper is "Published as a conference paper at ICLR 2021" (p. 1 header). The first author's work was partly done during an internship at Google Brain (p. 1 footnote).

---

## Problem

Two earlier families corrupt data with a finite ladder of noise levels and learn to reverse it (p. 1):

- SMLD (score matching with Langevin dynamics, Song & Ermon 2019): learn the score at each noise scale, sample by annealed Langevin MCMC.
- DDPM (Sohl-Dickstein 2015; Ho 2020): learn reverse Markov transitions of a noising chain; for continuous state its objective implicitly computes scores.

The paper unifies them as "score-based generative models" by letting the number of noise scales go to infinity, so that perturbed distributions evolve under an SDE (p. 2-3). Goals: flexible samplers, exact likelihood, controllable generation, and a way to explore and tune the SDE itself.

## Method

### Discrete predecessors (§2)

> [!definition] SMLD objective and sampler ([[Diffusion models#SMLD and DDPM|smld]])
> $p_\sigma(\tilde x\mid x)=\mathcal N(\tilde x;x,\sigma^2 I)$, scales $\sigma_{\min}=\sigma_1<\dots<\sigma_N=\sigma_{\max}$.
> $$\theta^*=\arg\min_\theta\sum_{i=1}^N\sigma_i^2\,\mathbb E_{p_{data}(x)}\mathbb E_{p_{\sigma_i}(\tilde x|x)}\big[\|s_\theta(\tilde x,\sigma_i)-\nabla_{\tilde x}\log p_{\sigma_i}(\tilde x\mid x)\|_2^2\big]$$
> Langevin sampling at scale $i$, $m=1..M$, run for $i=N,\dots,1$:
> $$x_i^m=x_i^{m-1}+\epsilon_i s_{\theta^*}(x_i^{m-1},\sigma_i)+\sqrt{2\epsilon_i}\,z_i^m$$
>
> (source: Score-SDE PDF, eqs. 1-2, p. 3)

> [!definition] DDPM objective and ancestral sampler ([[Diffusion models#SMLD and DDPM|ddpm]])
> Chain $p(x_i\mid x_{i-1})=\mathcal N(x_i;\sqrt{1-\beta_i}\,x_{i-1},\beta_i I)$, so $p_{\alpha_i}(x_i\mid x_0)=\mathcal N(x_i;\sqrt{\alpha_i}x_0,(1-\alpha_i)I)$ with $\alpha_i=\prod_{j\le i}(1-\beta_j)$.
> $$\theta^*=\arg\min_\theta\sum_{i=1}^N(1-\alpha_i)\,\mathbb E_{p_{data}}\mathbb E_{p_{\alpha_i}(\tilde x|x)}\big[\|s_\theta(\tilde x,i)-\nabla_{\tilde x}\log p_{\alpha_i}(\tilde x\mid x)\|_2^2\big]$$
> $$x_{i-1}=\tfrac1{\sqrt{1-\beta_i}}\big(x_i+\beta_i s_{\theta^*}(x_i,i)\big)+\sqrt{\beta_i}\,z_i$$
>
> (source: Score-SDE PDF, eqs. 3-4, p. 3; eq. 3 is $L_{simple}$ of Ho et al. 2020 rewritten)

The weights $\sigma_i^2$ and $1-\alpha_i$ are both proportional to $1/\mathbb E\|\nabla\log p(\tilde x\mid x)\|_2^2$ (p. 3).

### Forward SDE and reverse-time SDE (§3.1-3.2)

> [!definition] Forward SDE (Itô)
> $$dx=f(x,t)\,dt+g(t)\,dw \qquad (5)$$
> $t\in[0,T]$, $x(0)\sim p_0$ (data), $x(T)\sim p_T$ (tractable prior); $w$ standard Wiener process, $f(\cdot,t):\mathbb R^d\to\mathbb R^d$ the drift, $g:\mathbb R\to\mathbb R$ the scalar diffusion coefficient. Unique strong solution if coefficients are globally Lipschitz in state and time.
>
> (source: Score-SDE PDF, eq. 5, p. 3-4)

> [!theorem] Reverse-time SDE (Anderson 1982) ([[Diffusion models#Reverse-time SDE|reverse time sde]])
> $$dx=\big[f(x,t)-g(t)^2\nabla_x\log p_t(x)\big]dt+g(t)\,d\bar w \qquad (6)$$
> $\bar w$ is a Wiener process when time flows from $T$ to $0$ and $dt$ is an infinitesimal negative step. Starting from $x(T)\sim p_T$ and integrating backwards gives $x(0)\sim p_0$.
>
> (source: Score-SDE PDF, eq. 6, p. 4; general matrix-valued form eq. 16, p. 13)

General form with $dx=f\,dt+G(x,t)\,dw$ (eq. 15): reverse drift is $f-\nabla\!\cdot[GG^\top]-GG^\top\nabla_x\log p_t(x)$ and diffusion $G\,d\bar w$ (eq. 16, p. 13), where $\nabla\!\cdot F$ is the row-wise divergence of a matrix function.

### Score estimation (§3.3)

> [!definition] Time-dependent denoising score matching ([[Score matching#Denoising score matching|denoising score matching]], [[Score matching]])
> $$\theta^*=\arg\min_\theta\ \mathbb E_t\Big\{\lambda(t)\,\mathbb E_{x(0)}\mathbb E_{x(t)\mid x(0)}\big[\|s_\theta(x(t),t)-\nabla_{x(t)}\log p_{0t}(x(t)\mid x(0))\|_2^2\big]\Big\} \qquad (7)$$
> $\lambda:[0,T]\to\mathbb R_{>0}$ positive weighting, $t\sim\mathcal U[0,T]$, $x(0)\sim p_0$, $x(t)\sim p_{0t}(x(t)\mid x(0))$. With enough data and capacity $s_{\theta^*}(x,t)=\nabla_x\log p_t(x)$ a.e. Typical choice $\lambda\propto 1/\mathbb E\|\nabla\log p_{0t}(x(t)\mid x(0))\|_2^2$.
>
> (source: Score-SDE PDF, eq. 7, p. 4)

Needs the transition kernel $p_{0t}$: Gaussian in closed form when $f$ is affine; otherwise solve Kolmogorov's forward equation, or simulate the SDE and use sliced score matching, eq. 19 (p. 5, p. 13):

$$\mathbb E_t\Big\{\lambda(t)\mathbb E_{x(0)}\mathbb E_{x(t)}\mathbb E_{v\sim p_v}\big[\tfrac12\|s_\theta(x(t),t)\|_2^2+v^\top s_\theta(x(t),t)\,v\big]\Big\},\quad \mathbb E[v]=0,\ \mathrm{Cov}[v]=I.$$

### VE, VP, sub-VP SDEs (§3.4, App. B)

Limits of the discrete chains (eq. 8, 10 / 20, 22, p. 5, 14):

- SMLD chain $x_i=x_{i-1}+\sqrt{\sigma_i^2-\sigma_{i-1}^2}\,z_{i-1}$ ($\sigma_0=0$).
- DDPM chain $x_i=\sqrt{1-\beta_i}\,x_{i-1}+\sqrt{\beta_i}\,z_{i-1}$; with $\bar\beta_i=N\beta_i$, $\beta(i/N)=\bar\beta_i$, $\Delta t=1/N$ (eqs. 23-24).

> [!definition] Variance Exploding SDE ([[Diffusion models#VE, VP and sub-VP SDEs|variance exploding sde]])
> $$dx=\sqrt{\tfrac{d[\sigma^2(t)]}{dt}}\,dw \qquad (9)$$
> Variance explodes as $t\to\infty$. Kernel (eq. 29): $p_{0t}(x(t)\mid x(0))=\mathcal N\big(x(t);x(0),[\sigma^2(t)-\sigma^2(0)]I\big)$.
>
> (source: Score-SDE PDF, eq. 9, p. 5; eqs. 21, 29, pp. 14-15)

> [!definition] Variance Preserving SDE ([[Diffusion models#VE, VP and sub-VP SDEs|variance preserving sde]])
> $$dx=-\tfrac12\beta(t)\,x\,dt+\sqrt{\beta(t)}\,dw \qquad (11)$$
> Covariance obeys $\dot\Sigma_{VP}=\beta(t)(I-\Sigma_{VP})$, so $\Sigma_{VP}(t)=I+e^{-\int_0^t\beta(s)ds}(\Sigma_{VP}(0)-I)$ (eq. 26); constant $=I$ if $\Sigma(0)=I$. Kernel (eq. 29): $\mathcal N\big(x(t);x(0)e^{-\frac12\int_0^t\beta(s)ds},\ I-Ie^{-\int_0^t\beta(s)ds}\big)$.
>
> (source: Score-SDE PDF, eq. 11, p. 5; eqs. 25-26, 29, pp. 14-15)

> [!definition] sub-VP SDE
> $$dx=-\tfrac12\beta(t)\,x\,dt+\sqrt{\beta(t)\big(1-e^{-2\int_0^t\beta(s)ds}\big)}\,dw \qquad (12)$$
> Same mean as VP; variance $\Sigma_{\text{sub-VP}}(t)=I+e^{-2\int_0^t\beta}I+e^{-\int_0^t\beta}(\Sigma(0)-2I)$ (eq. 28), always $\le\Sigma_{VP}(t)$ for the same $\beta$ and initial law, and both $\to I$ if $\int_0^\infty\beta=\infty$. Kernel (eq. 29): $\mathcal N\big(x(t);x(0)e^{-\frac12\int_0^t\beta},\ [1-e^{-\int_0^t\beta}]^2 I\big)$.
>
> (source: Score-SDE PDF, eq. 12, p. 5; eqs. 27-29, p. 15)

Concrete instantiations (App. C, pp. 15-16):

- SMLD, geometric $\sigma_i$: $\sigma(t)=\sigma_{\min}(\sigma_{\max}/\sigma_{\min})^t$, giving $dx=\sigma_{\min}(\sigma_{\max}/\sigma_{\min})^t\sqrt{2\log(\sigma_{\max}/\sigma_{\min})}\,dw$, $t\in(0,1]$ (eq. 30); kernel variance $\sigma_{\min}^2(\sigma_{\max}/\sigma_{\min})^{2t}$ (eq. 31). $\sigma_{\min}=0.01$; $\sigma(0)=0\neq\sigma(0^+)=\sigma_{\min}$, so solve on $t\in[\epsilon,1]$, $\epsilon=10^{-5}$.
- DDPM, arithmetic $\beta_i$: $\beta(t)=\bar\beta_{\min}+t(\bar\beta_{\max}-\bar\beta_{\min})$ with $\bar\beta_{\min}=0.1$, $\bar\beta_{\max}=20$ (eq. 32). Kernel mean scale $e^{-\frac14t^2(\bar\beta_{\max}-\bar\beta_{\min})-\frac12t\bar\beta_{\min}}$ (eq. 33). $\epsilon=10^{-3}$ for sampling, $10^{-5}$ for training and likelihood.
- sub-VP uses the same $\beta(t)$ (eq. 34).

### Probability flow ODE (§4.3, App. D)

> [!theorem] Probability flow ODE ([[Diffusion models#Probability-flow ODE|probability flow ode]])
> For every diffusion process there is a deterministic process with the same marginals $\{p_t(x)\}_{t=0}^T$:
> $$dx=\Big[f(x,t)-\tfrac12 g(t)^2\nabla_x\log p_t(x)\Big]dt \qquad (13)$$
> General form (eq. 17): $dx=\{f-\tfrac12\nabla\!\cdot[GG^\top]-\tfrac12GG^\top\nabla_x\log p_t(x)\}dt$.
>
> (source: Score-SDE PDF, eq. 13, p. 7; eq. 17, p. 13)

> [!proof] Sketch (App. D.1, pp. 16-17)
> The marginal obeys the Fokker-Planck / Kolmogorov forward equation (eq. 35). Using $\sum_j\partial_{x_j}[\sum_kG_{ik}G_{jk}p_t]=p_t\nabla\!\cdot[GG^\top]_i+p_tGG^\top\nabla\log p_t$ it rewrites as the continuity (Liouville) equation $\partial_tp_t=-\sum_i\partial_{x_i}[\tilde f_i p_t]$ with $\tilde f=f-\tfrac12\nabla\!\cdot[GG^\top]-\tfrac12GG^\top\nabla\log p_t$ (eq. 37), i.e. the SDE with zero diffusion, an ODE. Idea credited to Maoutsa et al. 2020. See [[Fokker-Planck equation]].

Exact likelihood (App. D.2, p. 18), with $\tilde f_\theta$ the drift of eq. 38 with $s_\theta$ in place of the score:

$$\log p_0(x(0))=\log p_T(x(T))+\int_0^T\nabla\!\cdot\tilde f_\theta(x(t),t)\,dt \qquad (39)$$

divergence estimated by Skilling-Hutchinson, $\nabla\!\cdot\tilde f_\theta=\mathbb E_{p(\epsilon)}[\epsilon^\top\nabla\tilde f_\theta\,\epsilon]$ with $\mathbb E\epsilon=0$, $\mathrm{Cov}\,\epsilon=I$ (eq. 40). This is the instantaneous change of variables of neural ODEs (Chen 2018), as in FFJORD. RK45 via `scipy.integrate.solve_ivp`, atol=rtol=1e-5.

Further consequences listed on p. 7-8: latent-space interpolation and temperature scaling; a uniquely identifiable encoding (the forward SDE has no trainable parameters; checked in App. D.5 by training two architectures on CIFAR-10 VE and comparing latents, correlation $r=0.96$ in Fig. 8); adaptive-step sampling with a black-box ODE solver, where a larger tolerance cuts function evaluations by over 90% with no visible loss of quality (Fig. 3).

### Samplers (§4.1-4.2, App. E-G)

Given a forward discretization $x_{i+1}=x_i+f_i(x_i)+G_iz_i$ (eq. 45), the *reverse diffusion sampler* mirrors it (App. E):

$$x_i=x_{i+1}-f_{i+1}(x_{i+1})+G_{i+1}G_{i+1}^\top s_{\theta^*}(x_{i+1},i+1)+G_{i+1}z_{i+1} \qquad (46)$$

DDPM ancestral sampling (eq. 4) is shown to be a different discretization of the same reverse VP SDE: it equals the eq. 46 form up to $o(\beta_{i+1})$, i.e. $x_i\approx(2-\sqrt{1-\beta_{i+1}})x_{i+1}+\beta_{i+1}s_{\theta^*}+\sqrt{\beta_{i+1}}z_{i+1}$ (p. 19-21). Ancestral sampling for SMLD (eq. 47, p. 22):

$$x_{i-1}=x_i+(\sigma_i^2-\sigma_{i-1}^2)s_{\theta^*}(x_i,i)+\sqrt{\tfrac{\sigma_{i-1}^2(\sigma_i^2-\sigma_{i-1}^2)}{\sigma_i^2}}\,z_i$$

Deterministic probability-flow discretizations (App. D.3, p. 18): SMLD $x_i=x_{i+1}+\tfrac12(\sigma_{i+1}^2-\sigma_i^2)s_{\theta^*}(x_{i+1},\sigma_{i+1})$ (eq. 43); DDPM $x_i=(2-\sqrt{1-\beta_{i+1}})x_{i+1}+\tfrac12\beta_{i+1}s_{\theta^*}(x_{i+1},i+1)$ (eq. 44).

> [!algorithm] Predictor-Corrector (PC) sampling ([[Diffusion models#Predictor-corrector sampler|predictor corrector sampler]])
> Require: $N$ (discretization steps of the reverse-time SDE), $M$ (corrector steps).
> ```
> 1: x_N ~ p_T(x)
> 2: for i = N-1 down to 0:
> 3:     x_i <- Predictor(x_{i+1})
> 4:     for j = 1 to M:
> 5:         x_i <- Corrector(x_i)
> 6: return x_0
> ```
> The predictor is any numerical reverse-SDE solver (fixed discretization); the corrector is any score-based MCMC (Langevin, HMC) targeting $p_t$. SMLD = identity predictor + annealed Langevin corrector; DDPM = ancestral predictor + identity corrector (p. 6).
>
> (source: Score-SDE PDF, Algorithm 1, p. 22; §4.2, p. 6)

> [!algorithm] PC sampling, VE SDE (Alg. 2) and VP SDE (Alg. 3)
> VE: $x_N\sim\mathcal N(0,\sigma_{\max}^2I)$; for $i=N-1..0$:
> ```
> x'_i = x_{i+1} + (s_{i+1}^2 - s_i^2) * s_theta(x_{i+1}, s_{i+1})
> x_i  = x'_i + sqrt(s_{i+1}^2 - s_i^2) * z
> repeat M times:
>     x_i = x_i + eps_i * s_theta(x_i, s_i) + sqrt(2 eps_i) * z
> ```
> (s = sigma.) VP: $x_N\sim\mathcal N(0,I)$; for $i=N-1..0$:
> ```
> x'_i = (2 - sqrt(1-b_{i+1})) x_{i+1} + b_{i+1} s_theta(x_{i+1}, i+1)
> x_i  = x'_i + sqrt(b_{i+1}) * z
> repeat M times:
>     x_i = x_i + eps_i * s_theta(x_i, i) + sqrt(2 eps_i) * z
> ```
> (b = beta.)
>
> (source: Score-SDE PDF, Algorithms 2-3, p. 23)

> [!algorithm] Corrector with signal-to-noise ratio $r$ (Alg. 4 VE, Alg. 5 VP)
> For each $i=N..1$, $j=1..M$: draw $z\sim\mathcal N(0,I)$, $g\leftarrow s_{\theta^*}(x_i^{j-1},\sigma_i)$ (VE) or $s_{\theta^*}(x_i^{j-1},i)$ (VP);
> $$\epsilon\leftarrow 2\,(r\|z\|_2/\|g\|_2)^2\ \ (\text{VE}),\qquad \epsilon\leftarrow 2\alpha_i\,(r\|z\|_2/\|g\|_2)^2\ \ (\text{VP});\qquad x_i^j\leftarrow x_i^{j-1}+\epsilon g+\sqrt{2\epsilon}\,z.$$
> Norms are averaged over the mini-batch; for small batches replace $\|z\|_2$ by $\sqrt d$. A final denoising step with Tweedie's formula is used in all experiments (p. 22-23).
>
> (source: Score-SDE PDF, Algorithms 4-5, p. 23)

### Controllable generation (§5, App. I)

> [!definition] Conditional reverse-time SDE
> $$dx=\{f(x,t)-g(t)^2[\nabla_x\log p_t(x)+\nabla_x\log p_t(y\mid x)]\}dt+g(t)\,d\bar w \qquad (14)$$
> from $p_t(x(t)\mid y)\propto p_t(x(t))\,p(y\mid x(t))$, so $\nabla\log p_t(x\mid y)=\nabla\log p_t(x)+\nabla\log p(y\mid x)$ (eq. 49). General form eq. 18/48 (pp. 13, 29).
>
> (source: Score-SDE PDF, eq. 14, p. 9)

- Class-conditional: train a time-dependent classifier $p_t(y\mid x(t))$ on noised data with a mixture of cross-entropy losses across $t$ (Wide-ResNet-28-10, CIFAR-10, VE; p. 29).
- Imputation: with $\Omega(x)$ the known and $\bar\Omega(x)$ the unknown coordinates, run the SDE for $z(t)=\bar\Omega(x(t))$ and approximate $p_t(z(t)\mid\Omega(x(0))=y)\approx p_t(z(t)\mid\hat\Omega(x(t)))$, $\hat\Omega(x(t))$ a noised sample of the known part (App. I.2, p. 31).
- Colorization: orthogonal change of basis decouples gray from colour channels, then imputation (App. I.3). Wiener process is invariant under orthogonal maps.
- General inverse problems: $\nabla_x\log p_t(x(t)\mid y)\approx s_{\theta^*}(x(t),t)+\nabla_x\log p_t(\hat y(t)\mid x(t))$ with $\hat y(t)\sim p(y(t)\mid y)$ (eq. 50, p. 32). Relevant to [[Diffusion posterior sampling]].

### Architecture (§4.4, App. H)

NCSN++ (VE) and DDPM++ (VP/sub-VP): FIR anti-aliased up/downsampling, skip connections rescaled by $1/\sqrt2$, BigGAN residual blocks, 4 blocks per resolution instead of 2, optional progressive-growing input/output. "Cont." variants train with eq. 7 and random Fourier feature time embeddings (scale 16); "deep" doubles depth. EMA 0.999 (VE) vs 0.9999 (VP).

## Results

**Table 1: sampler comparison, CIFAR-10, FID (lower better), mean $\pm$ s.d. over 5 runs (p. 6; layout read from the PDF page).** P1000/P2000 predictor-only, C2000 corrector-only, PC1000 = 1000 predictor + 1000 corrector steps. P2000 uses linear interpolation of noise scales (App. G).

| Predictor | VE P1000 | VE P2000 | VE C2000 | VE PC1000 | VP P1000 | VP P2000 | VP C2000 | VP PC1000 |
|---|---|---|---|---|---|---|---|---|
| ancestral | 4.98 | 4.88 | - | 3.62 | 3.24 | 3.24 | - | 3.21 |
| reverse diffusion | 4.79 | 4.74 | 20.43 | 3.60 | 3.21 | 3.19 | 19.06 | 3.18 |
| probability flow | 15.41 | 10.54 | (20.43) | 3.51 | 3.59 | 3.23 | (19.06) | 3.06 |

C2000 is shared across predictors (one value per SDE: 20.43 VE, 19.06 VP). Standard deviations are $\le$ .15 (e.g. 4.98 $\pm$ .06, 15.41 $\pm$ .15, PC1000 prob. flow VP 3.06 $\pm$ .03). Findings (p. 6): reverse diffusion always beats ancestral sampling; corrector-only is worst at equal compute; adding one corrector step doubles compute but always beats P1000 and is typically better than P2000. Table 4 (p. 24) repeats with rounding interpolation (e.g. VE P2000 4.92 ancestral, 4.72 reverse diffusion, 12.87 prob. flow) with the same trend. Optimal $r$ (Table 5, p. 24): e.g. VE C2000 0.17 / 0.16 / 0.22, VP C2000 0.01 / 0.01 / 0.27; PC1000 prob. flow 0.17 (VE), 0.04 (VP). LSUN uses $r=0.075$.

**Table 2: NLL (bits/dim, uniformly dequantized) and FID (ODE sampling), CIFAR-10 (p. 7).**

| Model | NLL test | FID |
|---|---|---|
| RealNVP | 3.49 | - |
| iResNet | 3.45 | - |
| Glow | 3.35 | - |
| MintNet | 3.32 | - |
| Residual Flow | 3.28 | 46.37 |
| FFJORD | 3.40 | - |
| Flow++ | 3.29 | - |
| DDPM (L) | $\le$ 3.70* | 13.51 |
| DDPM ($L_{simple}$) | $\le$ 3.75* | 3.17 |
| DDPM (same model, exact likelihood) | 3.28 | 3.37 |
| DDPM cont. (VP) | 3.21 | 3.69 |
| DDPM cont. (sub-VP) | 3.05 | 3.56 |
| DDPM++ cont. (VP) | 3.16 | 3.93 |
| DDPM++ cont. (sub-VP) | 3.02 | 3.16 |
| DDPM++ cont. (deep, VP) | 3.13 | 3.08 |
| DDPM++ cont. (deep, sub-VP) | **2.99** | 2.92 |

\* ELBO on discrete data (not exact); other rows are exact likelihoods of the probability-flow ODE on uniformly dequantized data. Table 2 reports the last checkpoint.

**Table 3: CIFAR-10 sample quality, PC samplers, best-FID checkpoint (p. 7).**

| Model | FID | IS |
|---|---|---|
| BigGAN (cond.) | 14.73 | 9.22 |
| StyleGAN2-ADA (cond.) | 2.42 | 10.14 |
| StyleGAN2-ADA (uncond.) | 2.92 | 9.83 |
| NCSN | 25.32 | 8.87 $\pm$ .12 |
| NCSNv2 | 10.87 | 8.40 $\pm$ .07 |
| DDPM | 3.17 | 9.46 $\pm$ .11 |
| DDPM++ | 2.78 | 9.64 |
| DDPM++ cont. (VP) | 2.55 | 9.58 |
| DDPM++ cont. (sub-VP) | 2.61 | 9.56 |
| DDPM++ cont. (deep, VP) | 2.41 | 9.68 |
| DDPM++ cont. (deep, sub-VP) | 2.41 | 9.57 |
| NCSN++ | 2.45 | 9.73 |
| NCSN++ cont. (VE) | 2.38 | 9.83 |
| NCSN++ cont. (deep, VE) | **2.20** | **9.89** |

Other findings:

- VE SDEs give better sample quality than VP/sub-VP, but worse likelihood; the authors conclude practitioners need to try different SDEs per domain and architecture (p. 8).
- With the continuous objective, the predictor for continuously trained models is Euler-Maruyama, because DDPM's discretization does not match the continuous variance as $t\to0$ and hurts FID (p. 26).
- Probability-flow samplers without a corrector have worse FID than SDE solvers, and the gap is larger for VE than VP, especially in high dimension (App. D.4, p. 19).
- Smaller $\epsilon$ generally gives better likelihood; for sampling a suitable $\epsilon$ is needed for good IS/FID (p. 16).
- First high-fidelity 1024x1024 CelebA-HQ samples from a score-based model (PC, 2000 steps, $r=0.15$, about 2.4M iterations, batch 8; Fig. 12, p. 29). The authors note visible flaws, e.g. facial symmetry.
- Class-conditional CIFAR-10, and inpainting and colorization on 256x256 LSUN bedroom/church from one unconditional model (Fig. 4, pp. 9, 33-36). Qualitative only.
- PC samplers on LSUN 256x256 (Fig. 9, p. 23): best samples when compute is split between predictor and corrector.

## Limitations

As stated by the authors (p. 9): sampling is still slower than GANs on the same datasets; the many sampler choices bring many hyperparameters ($r$, $M$, $N$, predictor, $\epsilon$) needing automatic selection and more study. Samples at 1024x1024 are imperfect.

Wiki note (not in paper): FID/NLL comparisons depend on dequantization and checkpoint-selection conventions the paper itself flags (Table 2 last checkpoint, Table 3 best-FID checkpoint, uniform dequantization only); the paper's SDE derivations assume a scalar state-independent $g(t)$ for the main text, with the general case in App. A. Score-estimation error and the $p_T\approx$ prior approximation are not analysed theoretically.

## Connections

- Unifies [[Diffusion models#SMLD and DDPM|smld]] (Song & Ermon 2019) and [[Diffusion models#SMLD and DDPM|ddpm]] (Ho et al. 2020) as discretizations of [[Diffusion models#VE, VP and sub-VP SDEs|variance exploding sde]] and [[Diffusion models#VE, VP and sub-VP SDEs|variance preserving sde]]; see [[Diffusion models]] for the broader family, [[Langevin dynamics]] for the corrector, and [[SGLD (Welling 2011)]] for the related Langevin-with-gradient-noise sampler.
- The VP SDE is an [[SDE-BNN (Xu 2022)|ornstein uhlenbeck process]] with time-varying rate; $f$ affine gives Gaussian kernels.
- The probability flow ODE is a neural ODE / continuous [[Normalizing flows]] model, used for exact likelihood and compared against flow baselines in Table 2. Later [[Flow matching]] works with the same ODE view (Wiki note).
- Conditional SDE, eq. 14, and the inverse-problem recipe, eq. 50, anticipate [[Diffusion posterior sampling]] (Wiki note: that method is a later development) and fit the application in [[Generative priors for turbulence (Wang 2026)]] (Wiki note, check that page).
- Wiki note: [[Intro to VAEs (Kingma 2019)]] is the VAE counterpart (a likelihood-based latent model); the 1024x1024 CelebA-HQ experiment follows the VQ-VAE-2 setup (batch 8, EMA 0.9999; App. H.3). The DDPM ELBO rows in Table 2 relate to [[ELBO]], and the reverse-time SDE with learned $s_\theta$ is a [[SDE-BNN (Xu 2022)|neural sde]]-style object. See [[KL divergence]] for the ELBO terms in App. F.
- Architecture borrows from GANs (BigGAN blocks, StyleGAN2 FIR, skip rescaling); see [[GAN]] and [[Group equivariant GANs (Dey 2021)]] for another GAN-based paper in this wiki.

%% refs:start %%
**Cited by in this wiki**: [[Classifier-free guidance (Ho 2022)]], [[DDIM (Song 2021)]]
%% refs:end %%

**Sources**: `papers/Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]]
- [[Score matching]]
- [[Fokker-Planck equation]]
- [[Langevin dynamics]]
- [[Normalizing flows]]
- [[Flow matching]]
- [[Diffusion posterior sampling]]
- [[SDE-BNN (Xu 2022)|ornstein uhlenbeck process]]
- [[ELBO]]
- [[KL divergence]]
- [[Generative priors for turbulence (Wang 2026)]]
- [[Intro to VAEs (Kingma 2019)]]
- [[SGLD (Welling 2011)]]
- [[GAN]]
- [[Group equivariant GANs (Dey 2021)]]
- [[DDPM (Ho 2020)]]
- [[DDIM (Song 2021)]]
- [[Step-by-step diffusion (Nakkiran 2025)]]
