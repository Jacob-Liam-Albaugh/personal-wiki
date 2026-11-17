---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Song et al. 2021, eqs. 5-7, 9, 11-13, 39; Alg. 1; Wang 2026, eqs. 3-5; de Albuquerque, Pearson 2024, eqs. 4-6, 9"
tags: [diffusion, generative, sampling]
---

# Diffusion models (score-based SDE view)

> [!algorithm] Forward and reverse SDE (Song et al. 2021, eqs. 5-6, p. 4)
> Forward, data to noise:
> $$dx=f(x,t)\,dt+g(t)\,dw$$
> Reverse, noise to data (Anderson 1982):
> $$dx=\big[f-g^2\nabla_x\log p_t(x)\big]dt+g\,d\bar w$$
> The score $\nabla_x\log p_t$ is replaced by a network $s_\theta(x,t)$ trained by [[Score matching#Denoising score matching|denoising score matching]].
>
> (source: `papers/Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, pp. 3-4)

**Intuition**: noise the data slowly until nothing is left but a Gaussian. Then run the movie backwards. Reversal needs only the score of every intermediate marginal.

## SMLD and DDPM
Both are discretizations of the SDE framework (Song et al., eqs. 8, 10, p. 5):
- SMLD chain: $x_i=x_{i-1}+\sqrt{\sigma_i^2-\sigma_{i-1}^2}\,z_{i-1}$. Its limit is the VE SDE.
- DDPM chain: $x_i=\sqrt{1-\beta_i}\,x_{i-1}+\sqrt{\beta_i}\,z_{i-1}$. Its limit is the VP SDE.
- SMLD samples with annealed [[Langevin dynamics]]; DDPM with ancestral sampling (p. 6).

Discrete-time details: [[DDPM]] (the original model and $L_\text{simple}$), [[DDIM]] (the deterministic sampler), [[Noise schedule]] and [[Noise prediction]].

## VE, VP and sub-VP SDEs
```
VE:     dx = sqrt(d[σ²(t)]/dt) dw
VP:     dx = -½β(t) x dt + sqrt(β(t)) dw
sub-VP: dx = -½β(t) x dt
             + sqrt(β(t)(1-e^{-2∫β})) dw
```
(eqs. 9, 11, 12, p. 5). All have Gaussian transition kernels in closed form (eq. 29), so [[Score matching#Denoising score matching|DSM]] needs no simulation. sub-VP has variance at most VP's and gave the best likelihoods.

Wang 2026 uses the VP form with $f=-\tfrac12\beta x$, $g=\sqrt\beta$ (eqs. 3-4).

## Reverse-time SDE
Eq. 6 above. $\bar w$ is a Wiener process in reversed time. The state-dependent form is eq. 16 (p. 13). Conditioning on $y$ adds $\nabla_x\log p_t(y\mid x)$ to the score (eq. 14, p. 9), which is the basis of [[Diffusion posterior sampling]].

## Probability-flow ODE
$$dx=\big[f-\tfrac12g^2\nabla_x\log p_t(x)\big]dt$$
It has the same marginals as the SDE (eq. 13, p. 7). The proof rewrites the [[Fokker-Planck equation]] as a continuity equation (App. D.1). It gives exact likelihoods by the instantaneous change of variables:
$$\log p_0(x(0))=\log p_T(x(T))+\int_0^T\nabla\cdot\tilde f_\theta\,dt$$
(eq. 39), with the divergence estimated by Hutchinson's trick. This links diffusion to continuous [[Normalizing flows]] and to [[Flow matching]]. Wang 2026 eq. 5 is the same ODE. [[DDIM]] with $\eta=0$ is an Euler discretization of an equivalent ODE (Song, Meng, Ermon, Prop. 1, p. 6).

## Matrix-valued noise (de Albuquerque, Pearson 2024)
With a matrix diffusion coefficient $G$ the ODE becomes $dx=\{f-\tfrac12\nabla\cdot[GG^\top]-\tfrac12GG^\top\nabla_x\log p_t\}dt$ (their eq. 4, p. 4). Taking $f=0$, $GG^\top=\dot C(t)$ smooths the data with $\mathcal N(0,C(t))$, and a rescaling $\tilde x=A(t)x$ gives the "inflationary" ODE (eq. 6). With $C(t)$ diagonal in the eigenbasis of the data covariance and $C_{jj}=\sigma_{0j}^2(e^{\rho t}-1)$ (eq. 9), each principal direction is noised in proportion to its own variance, which keeps the [[Participation ratio]] fixed; unequal rates compress the slower directions. Wiki note: this is the VE SDE applied to PCA-whitened data. Details on [[Inflationary flows (de Albuquerque 2024)]].

## Predictor-corrector sampler
Alg. 1 (p. 22): at each step a predictor (a reverse-SDE solver) moves $x$ to the next time. Then $M$ corrector steps of score-based MCMC (Langevin) fix the marginal. SMLD is identity predictor plus Langevin corrector; DDPM is ancestral predictor plus identity corrector.

CIFAR-10 FID, Table 1 (p. 6): PC1000 gives 3.06-3.62. P2000, the predictor-only run with equal compute, gives 3.19-10.54.

## Guidance
Conditional sampling can be sharpened at the cost of diversity:
- [[Classifier guidance]]: add a noisy-data classifier's gradient to the score.
- [[Classifier-free guidance]]: extrapolate from an unconditional to a conditional ε-prediction, with no classifier.

## Results (CIFAR-10, Song et al. 2021)
- FID 2.20, IS 9.89: NCSN++ cont. deep, VE (Table 3).
- NLL 2.99 bits/dim: DDPM++ cont. deep, sub-VP (Table 2).

## Where it appears
- [[Score SDE (Song 2021)]]: the framework.
- [[Generative priors for turbulence (Wang 2026)]]: a VP prior for turbulent fields.
- [[DDPM (Ho 2020)]], [[DDIM (Song 2021)]], [[Classifier-free guidance (Ho 2022)]].
- [[NCSNv2 (Song 2020)]]: how to set the noise scales and Langevin settings of SMLD.
- [[Step-by-step diffusion (Nakkiran 2025)]]: an elementary derivation, with the reverse SDE and PF-ODE as limits (Fig. 5.1, p. 50).
- [[PISD (Gallon 2026)]]: EDM-style diffusion on data-scaled spectral coefficients with PDE-residual guidance; see [[Spectral diffusion]].
- [[Inflationary flows (de Albuquerque 2024)]]: pfODE with full-covariance noise as an invertible, dimension-preserving or dimension-reducing map for calibrated latent inference.
- [[iDEM (Akhound-Sadegh 2024)]]: a VE diffusion sampler for Boltzmann densities trained from the energy alone, with an MC estimate of the noised score.
- [[Path Integral Sampler (Zhang 2022)]]: a finite-time SDE sampler whose drift is a stochastic-control solution, trained from the energy.
- [[Flow matching tutorial (Chen 2024)]]: diffusion as the Gaussian-path, independent-coupling case of flow matching (slides 31, 33).

**Sources**: `papers/Stochastic Methods/Kingma, Song, Sohl-Dickstein, Kumar, Ermon, Poole - Score-Based Generative Modeling Through Stochastic Differential Equations.pdf`, `papers/IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`, `papers/Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`, `papers/Diffusion/Nakkiran, Bradley, Zhou, Advani - Step-by-Step Diffusion An Elementary Tutorial.pdf`, `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models.pdf`, `papers/Diffusion/Chen, Lipman, Ben-Hamu - Flow Matching Tutorial.pdf`.
**Last updated**: 2026-11-11

---

## Related pages
- [[Score matching]] · [[Fokker-Planck equation]] · [[Langevin dynamics]] · [[Flow matching]] · [[Normalizing flows]] · [[GAN]] · [[DDPM]] · [[DDIM]] · [[Participation ratio]]
- [[U-Net]] · [[GAN paper (Goodfellow 2014)]]
