---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho, Jain, Abbeel 2020, NeurIPS, eqs. 1-7, 11-14; Alg. 1-2; Tables 1-2"
tags: [diffusion, generative, ml]
authors: ["[[Jonathan Ho]]", "[[Ajay Jain]]", "[[Pieter Abbeel]]"]
year: 2020
venue: "NeurIPS 2020 (arXiv:2006.11239v2)"
file: "papers/Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf"
---

# Denoising Diffusion Probabilistic Models (Ho 2020)

**Summary**: Shows that diffusion probabilistic models (a fixed Gaussian noising Markov chain plus a learned Gaussian reverse chain, trained on a variational bound) can produce high quality images. Predicting the noise $\epsilon$ instead of the posterior mean gives a simplified, reweighted bound $L_\text{simple}$ that equals denoising score matching over many noise levels, with a sampler that resembles Langevin dynamics. On unconditional CIFAR-10 it reaches IS 9.46 and FID 3.17 (p. 5, Table 1); log likelihood is not competitive (NLL $\le$ 3.75 bits/dim).

**Authors**: Jonathan Ho, Ajay Jain, Pieter Abbeel (UC Berkeley) · **Year**: 2020 · **File**: `papers/Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`

---

## Problem

Diffusion models (Sohl-Dickstein 2015) are easy to define and train, but "to the best of our knowledge" had not been shown to generate high quality samples (p. 2). The paper asks which parameterization and objective make them work, and how they relate to score-matching generative models (NCSN) and to autoregressive models. Part of [[Diffusion models]].

## Method

Latent variable model $p_\theta(x_0)=\int p_\theta(x_{0:T})\,dx_{1:T}$ with latents the same size as the data. Notation here follows the paper: $\alpha_t:=1-\beta_t$, $\bar\alpha_t:=\prod_{s\le t}\alpha_s$. (Wiki note: [[DDIM (Song 2021)]] writes $\alpha_t$ for this paper's $\bar\alpha_t$.)

> [!definition] Reverse process (generative model)
> $$p_\theta(x_{0:T}) = p(x_T)\prod_{t=1}^T p_\theta(x_{t-1}\mid x_t),\quad p_\theta(x_{t-1}\mid x_t)=\mathcal N\big(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)\big),\quad p(x_T)=\mathcal N(0,I)$$
> (source: Ho, Jain, Abbeel - DDPM, eq. 1, p. 2)

> [!definition] Forward (diffusion) process
> $$q(x_{1:T}\mid x_0)=\prod_{t=1}^T q(x_t\mid x_{t-1}),\qquad q(x_t\mid x_{t-1})=\mathcal N\big(x_t;\sqrt{1-\beta_t}\,x_{t-1},\beta_t I\big)$$
> Fixed Markov chain with variance schedule $\beta_1,\dots,\beta_T$ (see [[Noise schedule]]); it has no learnable parameters. (source: eq. 2, p. 2)

> [!theorem] Closed-form forward marginal
> $$q(x_t\mid x_0)=\mathcal N\big(x_t;\sqrt{\bar\alpha_t}\,x_0,(1-\bar\alpha_t)I\big)$$
> equivalently $x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon$, $\epsilon\sim\mathcal N(0,I)$ (a [[Reparameterization trick]] step, p. 3). (source: eq. 4, p. 2)

Training minimises the variational bound on negative log likelihood ([[ELBO]]):

> [!definition] Variational bound
> $$\mathbb E[-\log p_\theta(x_0)]\le \mathbb E_q\Big[-\log\frac{p_\theta(x_{0:T})}{q(x_{1:T}\mid x_0)}\Big]=:L\quad\text{(eq. 3, p. 2)}$$
> Rewritten with the forward posteriors (Rao-Blackwellised, all terms are [[KL divergence]]s between Gaussians):
> $$L=\mathbb E_q\Big[\underbrace{D_{KL}(q(x_T\mid x_0)\,\|\,p(x_T))}_{L_T}+\sum_{t>1}\underbrace{D_{KL}(q(x_{t-1}\mid x_t,x_0)\,\|\,p_\theta(x_{t-1}\mid x_t))}_{L_{t-1}}\underbrace{-\log p_\theta(x_0\mid x_1)}_{L_0}\Big]$$
> (source: eq. 5, p. 3; derivation eqs. 17-22, App. A, pp. 13-14)

> [!theorem] Forward-process posterior
> $$q(x_{t-1}\mid x_t,x_0)=\mathcal N\big(x_{t-1};\tilde\mu_t(x_t,x_0),\tilde\beta_t I\big)$$
> $$\tilde\mu_t(x_t,x_0)=\frac{\sqrt{\bar\alpha_{t-1}}\,\beta_t}{1-\bar\alpha_t}x_0+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}x_t,\qquad \tilde\beta_t=\frac{1-\bar\alpha_{t-1}}{1-\bar\alpha_t}\beta_t$$
> (source: eqs. 6-7, p. 3)

### Design choices (Section 3)

- **$L_T$** is constant because $\beta_t$ is fixed, so it is dropped (3.1, p. 3).
- **Reverse variances** fixed to $\Sigma_\theta=\sigma_t^2 I$ with $\sigma_t^2=\beta_t$ or $\sigma_t^2=\tilde\beta_t$; both gave similar results. The first is optimal for $x_0\sim\mathcal N(0,I)$, the second for $x_0$ a single point (3.2, p. 3). Learning the variances was unstable (Table 2).
- **Mean parameterization.** With fixed $\sigma_t$:

> [!definition] $L_{t-1}$ as mean regression
> $$L_{t-1}=\mathbb E_q\Big[\frac1{2\sigma_t^2}\|\tilde\mu_t(x_t,x_0)-\mu_\theta(x_t,t)\|^2\Big]+C\quad\text{(eq. 8, p. 3)}$$
> Substituting $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon$ and eq. 7 gives (eqs. 9-10, p. 3) a target $\frac1{\sqrt{\alpha_t}}\big(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\epsilon\big)$.

> [!definition] $\epsilon$-prediction parameterization ([[Noise prediction]])
> $$\mu_\theta(x_t,t)=\frac1{\sqrt{\alpha_t}}\Big(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\epsilon_\theta(x_t,t)\Big)\quad\text{(eq. 11, p. 4)}$$
> Then
> $$L_{t-1}-C=\mathbb E_{x_0,\epsilon}\Big[\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar\alpha_t)}\big\|\epsilon-\epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,t)\big\|^2\Big]\quad\text{(eq. 12, p. 4)}$$

The paper also notes $x_0$-prediction is possible but "led to worse sample quality early in our experiments" (p. 4).

> [!definition] Simplified objective $L_\text{simple}$
> $$L_\text{simple}(\theta)=\mathbb E_{t,x_0,\epsilon}\Big[\big\|\epsilon-\epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,t)\big\|^2\Big],\quad t\sim\text{Unif}\{1..T\}\quad\text{(eq. 14, p. 5)}$$
> Drops the weight in eq. 12. $t=1$ corresponds to $L_0$ with the decoder integral approximated by density times bin width. It is a *weighted* variational bound that down-weights small $t$ (very-low-noise denoising) so the network focuses on harder, larger-$t$ terms (p. 5).

> [!algorithm] Algorithm 1 (training) and Algorithm 2 (sampling) (source: p. 4)
> **Training**: repeat: $x_0\sim q(x_0)$; $t\sim\text{Unif}\{1,\dots,T\}$; $\epsilon\sim\mathcal N(0,I)$; gradient step on $\nabla_\theta\|\epsilon-\epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,t)\|^2$; until converged.
>
> **Sampling**: $x_T\sim\mathcal N(0,I)$; for $t=T,\dots,1$: $z\sim\mathcal N(0,I)$ if $t>1$ else $z=0$;
> $$x_{t-1}=\frac1{\sqrt{\alpha_t}}\Big(x_t-\frac{1-\alpha_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta(x_t,t)\Big)+\sigma_t z;$$
> return $x_0$.

### Link to denoising score matching and Langevin dynamics

Algorithm 2 "resembles Langevin dynamics with $\epsilon_\theta$ as a learned gradient of the data density" ([[Langevin dynamics]]), and eq. 12 "resembles denoising score matching over multiple noise scales indexed by $t$" ([[Score matching]], section "Denoising score matching"; [[Score matching#Denoising score matching|denoising score matching]]). The paper's conclusion: optimising an objective resembling denoising score matching is equivalent to variational inference fitting the finite-time marginal of a Langevin-like sampling chain (p. 4). Appendix C (p. 15) lists how this differs from NCSN: U-Net with attention and sinusoidal time embedding in every layer; data scaled by $\sqrt{1-\beta_t}$ per step so variance does not grow; forward process destroys signal ($D_{KL}(q(x_T|x_0)\|\mathcal N(0,I))\approx0$) and $\beta_t$ is small so the reverse is Gaussian; sampler coefficients are derived from $\beta_t$, not hand-set post hoc, and the sampler is trained directly as a latent variable model. Wiki note: [[Score SDE (Song 2021)]] later formalises this as DDPM being a discretisation of the VP SDE (see [[Diffusion models]], sections "SMLD and DDPM" and "VE, VP and sub-VP SDEs").

### Decoder and data scaling (3.3, p. 4)

Data are integers $\{0..255\}$ scaled to $[-1,1]$. $L_0$ uses an independent discrete decoder $p_\theta(x_0|x_1)=\prod_i\int_{\delta_-(x_0^i)}^{\delta_+(x_0^i)}\mathcal N(x;\mu^i_\theta(x_1,1),\sigma_1^2)\,dx$ with $\delta_\pm(x)=x\pm\frac1{255}$ and $\pm\infty$ at the edges (eq. 13), so the bound is a lossless codelength. The final sample displays $\mu_\theta(x_1,1)$ noiselessly.

### Noise schedule and architecture (4, App. B)

$T=1000$; $\beta_t$ linear from $\beta_1=10^{-4}$ to $\beta_T=0.02$, small relative to data in $[-1,1]$ so that $L_T\approx10^{-5}$ bits/dim (p. 5). Chosen from constant, linear, quadratic schedules, all with $L_T\approx0$ (App. B, p. 14). See [[Noise schedule]]. U-Net backbone (PixelCNN++ style, Wide ResNet, group norm), sinusoidal time embedding, self-attention at 16x16; 35.7M parameters on CIFAR-10, 114M on CelebA-HQ/LSUN, 256M for the large Bedroom model. Adam, lr $2\times10^{-4}$ ($2\times10^{-5}$ at 256x256), batch 128 (64 for large images), EMA 0.9999, dropout 0.1 on CIFAR-10 (App. B, pp. 14-15).

### Other analyses

- **Rate-distortion.** Treating $L_1+\dots+L_T$ as rate and $L_0$ as distortion; Algorithms 3-4 (p. 6) give a progressive lossy code (needs minimal random coding, intractable in high dimension, so a proof of concept, p. 13). Progressive estimate $\hat x_0=(x_t-\sqrt{1-\bar\alpha_t}\epsilon_\theta(x_t))/\sqrt{\bar\alpha_t}$ (eq. 15, p. 7).
- **Autoregressive link.** $L=D_{KL}(q(x_T)\|p(x_T))+\mathbb E_q\sum_t D_{KL}(q(x_{t-1}|x_t)\|p_\theta(x_{t-1}|x_t))+H(x_0)$ (eq. 16, p. 7; derivation eqs. 23-26, p. 14). With $T=D$ and a masking forward process this is an autoregressive model, so Gaussian diffusion is read as an autoregressive model with a generalised bit ordering (pp. 7-8).
- **Interpolation.** Encode with $q$ at step $t$, linearly interpolate the noisy latents $\bar x_t=(1-\lambda)x_t+\lambda x_t'$ (the text writes $x_0,x_0'$), decode with the reverse process; $t=500$ on CelebA-HQ gives smooth attribute interpolation, $t=1000$ gives novel samples (4.4, p. 8; Fig. 9, p. 16).

## Results

All numbers from the paper.

> [!example] Table 1: CIFAR-10 (p. 5); NLL in bits/dim, test (train)
> | Model | IS | FID | NLL |
> |---|---|---|---|
> | Ours, $L$, fixed isotropic $\Sigma$ | 7.67 $\pm$ 0.13 | 13.51 | $\le$ 3.70 (3.69) |
> | Ours, $L_\text{simple}$ | 9.46 $\pm$ 0.11 | 3.17 | $\le$ 3.75 (3.72) |
> | StyleGAN2 + ADA (v1), uncond. | 9.74 $\pm$ 0.05 | 3.26 | |
> | NCSN | 8.87 $\pm$ 0.12 | 25.32 | |
> | NCSNv2 | | 31.75 | |
> | SNGAN-DDLS | 9.09 $\pm$ 0.10 | 15.42 | |
> | SNGAN | 8.22 $\pm$ 0.05 | 21.7 | |
> | EBM (Du & Mordatch), uncond. | 6.78 | 38.2 | |
> | PixelIQN | 5.29 | 49.46 | |
> | Gated PixelCNN | 4.60 | 65.93 | 3.03 (2.90) |
> | Sparse Transformer | | | 2.80 |
> | Diffusion (original, Sohl-Dickstein 2015) | | | $\le$ 5.40 |
> | Conditional: StyleGAN2+ADA (v1) / BigGAN / JEM / EBM | 10.06 / 9.22 / 8.76 / 8.30 | 2.67 / 14.73 / 38.4 / 37.9 | |

- FID 3.17 is against the training set; against the test set it is 5.24 (p. 5). Lowest FID among the unconditional rows (StyleGAN2+ADA v1 is 3.26); the paper says it beats "most models in the literature, including class conditional models" (p. 5).
- Training on the true bound gives better codelength than $L_\text{simple}$ (3.70 vs 3.75), but $L_\text{simple}$ gives the best samples (p. 6).

> [!example] Table 2: reverse-process parameterization ablation, CIFAR-10 (p. 5)
> | Prediction / objective | IS | FID |
> |---|---|---|
> | $\tilde\mu$, $L$, learned diagonal $\Sigma$ | 7.28 $\pm$ 0.10 | 23.69 |
> | $\tilde\mu$, $L$, fixed isotropic $\Sigma$ | 8.06 $\pm$ 0.09 | 13.22 |
> | $\tilde\mu$, $\|\tilde\mu-\tilde\mu_\theta\|^2$ | unstable | unstable |
> | $\epsilon$, $L$, learned diagonal $\Sigma$ | unstable | unstable |
> | $\epsilon$, $L$, fixed isotropic $\Sigma$ | 7.67 $\pm$ 0.13 | 13.51 |
> | $\epsilon$, $\|\epsilon-\epsilon_\theta\|^2$ ($L_\text{simple}$) | 9.46 $\pm$ 0.11 | 3.17 |
>
> $\epsilon$-prediction matches $\tilde\mu$-prediction under the true bound with fixed variances and is much better with the simplified objective; learned variances were unstable (4.2, p. 6).

- **LSUN 256x256 FID** (Table 3, p. 13): Bedroom 6.36 ($L_\text{simple}$), 4.90 (large model); Church 7.89; Cat 19.75. Comparators: ProgressiveGAN 8.34 / 6.42 / 37.52; StyleGAN 2.65 / 4.21 / 8.53; StyleGAN2 - / 3.86 / 6.93. Abstract: "similar to ProgressiveGAN".
- **Likelihood and overfitting.** Train-test NLL gap at most 0.03 bits/dim (p. 6). Codelengths beat the large AIS-based estimates for EBMs/score matching but not other likelihood models.
- **Rate-distortion** (p. 6, Table 4 p. 13): best-sample CIFAR-10 model has rate 1.78 bits/dim and distortion 1.97 bits/dim (RMSE 0.95 on 0-255). More than half the lossless codelength describes imperceptible detail. Distortion falls steeply at low rate.
- **Progressive generation** (Fig. 6, p. 7): coarse features appear first, details last.
- **Compute** (App. B, p. 14): CIFAR-10 trains at 21 steps/s (batch 128), 10.6 h to 800k steps on TPU v3-8; sampling 256 images takes 17 s. 256x256 models: 300 s for 128 images.
- FID/IS on 50k samples; reported at minimum FID over training (App. B, p. 15).

## Limitations

As stated by the authors:
- Log likelihoods are not competitive with other likelihood-based models; most of the codelength goes to imperceptible detail (pp. 2, 6).
- The compression scheme is a proof of concept; minimal random coding is intractable for high-dimensional data (p. 13).
- $T=1000$ sequential network evaluations per sample matches earlier work (p. 5), sampling is slow (17 s per 256 CIFAR images, 300 s per 128 256x256 images, p. 14).
- Broader-impact section flags misuse (fake imagery) and dataset bias (p. 9).

Wiki notes:
- Learned variances and $x_0$-prediction were dropped for stability or early quality, with no further analysis in this paper.
- The "equivalence" with denoising score matching holds for the weighted objective eq. 12; the deployed $L_\text{simple}$ uses a different weighting (the paper says "analogous to" NCSN's, p. 5). **[unverified]**: how far this matters in practice is not tested here.
- Acceleration is addressed by [[DDIM (Song 2021)]]; the continuous-time view by [[Score SDE (Song 2021)]].

## Connections

- Builds on Sohl-Dickstein et al. 2015 (original diffusion model; cited, not in the wiki) and on SMLD/NCSN (Song & Ermon 2019) via denoising score matching (Vincent 2011); see [[Score matching]], [[Langevin dynamics]].
- Latent-variable framing: ELBO ([[ELBO]], [[KL divergence]]) with a fixed encoder, unlike a [[VAE]]; the paper contrasts itself with [[Normalizing flows]] and VAEs (Related Work, p. 8: $q$ has no parameters, $x_T$ has nearly zero mutual information with $x_0$).
- Samples are competitive with GANs without adversarial training ([[GAN]]).
- Generalised by [[DDIM (Song 2021)]] (non-Markovian forward family, same $L_\text{simple}$, deterministic fast sampling) and by [[Score SDE (Song 2021)]] (SDE view; DDPM = VP SDE discretisation).
- Wiki note: later [[Flow matching]] methods regress a velocity field with a similar simple squared-error objective along a prescribed interpolation path.
- Method pages: [[DDPM]], [[Noise prediction]], [[Noise schedule]], [[Diffusion models]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Attention is all you need (Vaswani 2017)]], [[GAN paper (Goodfellow 2014)]], [[Neural ODEs (Chen 2018)]], [[U-Net paper (Ronneberger 2015)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[Classifier-free guidance (Ho 2022)]], [[DDIM (Song 2021)]], [[PISD (Gallon 2026)]]
%% refs:end %%

**Sources**: `papers/Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Diffusion models]]
- [[DDPM]]
- [[Noise prediction]]
- [[Noise schedule]]
- [[Score matching]]
- [[Langevin dynamics]]
- [[ELBO]]
- [[KL divergence]]
- [[DDIM (Song 2021)]]
- [[Score SDE (Song 2021)]]
- [[U-Net]] · [[U-Net paper (Ronneberger 2015)]]: the denoiser backbone
