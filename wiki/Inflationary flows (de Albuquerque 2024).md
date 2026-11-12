---
type: paper
area: stochastic
areas: [stochastic, bayesian, ml]
source-ref: "de Albuquerque, Pearson 2024, NeurIPS, eqs. 4-11, 31, 37, 40, 44-50, 67-80; Tables 1-3, 11, 15"
tags: [diffusion, generative, bayesian, uq]
authors: ["[[Daniela de Albuquerque]]", "[[John Pearson]]"]
year: 2024
venue: "NeurIPS 2024 (DOI 10.52202/079017-3070)"
file: "papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models.pdf"
---

# Inflationary Flows: Calibrated Bayesian Inference with Diffusion-Based Models (de Albuquerque 2024)

**Summary**: Builds a deterministic, invertible map between data and a Gaussian latent space out of a diffusion model's probability-flow ODE, so that uncertainty in data space can be carried to the latent space (and back) by integrating an ODE. The noise is a Gaussian kernel with a full covariance $C(t)$, chosen in the eigenbasis of the data covariance so that a measure of intrinsic dimension, the [[Participation ratio]], is either kept or reduced. On CIFAR-10 and AFHQv2 the flows compress to as little as one nominal dimension with FID 12-28, far below injective-flow baselines (FID 280-544).

**Authors**: Daniela de Albuquerque, John Pearson (Duke University) · **Year**: 2024 · **File**: `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models.pdf`

Companion: the authors' 7-slide NeurIPS deck, `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models - Slides.pdf`. It restates the motivation, the three views of diffusion (SDE, Fokker-Planck, pfODE), eq. 6 in words and the participation ratio, and adds nothing beyond the paper.

Wiki note on coverage: read the main text (pp. 1-10) and Appendices A, B.1-B.3, B.5-B.6 and C.1-C.4. Not read: references (pp. 11-17), training hyperparameter tables (pp. 26-29), NeurIPS checklist (pp. 39-45). Equations were read from extracted text, not from rendered pages.

---

## Problem

Diffusion models generate well but do not give a calibrated posterior over latents, and do not compress. Variational methods (VAEs) give posteriors $q(z\mid x)$ that are overconfident and non-identifiable; normalizing flows are exact but keep the full dimension; injective flows reduce dimension only with substantial extra machinery (pp. 1-2). The goal is *posterior* calibration ($q(z\mid x)$ against $p(z\mid x)$), not predictive calibration.

## Method

### Three views of a diffusion (eqs. 1-4, pp. 3-4)

The paper writes the forward SDE as $dx=f(x,t)\,dt+G(x,t)\cdot dW$ (eq. 1), its [[Fokker-Planck equation]] as eq. 3, and the [[Diffusion models#Probability-flow ODE|probability-flow ODE]] (pfODE) with a matrix diffusion coefficient:
$$\frac{dx}{dt}=f-\tfrac12\nabla\cdot[GG^\top]-\tfrac12GG^\top\nabla_x\log p_t(x)\qquad(4)$$

### Inflation and rescaling (eqs. 5-6, p. 4; App. A.1-A.3)

> [!algorithm] Inflationary pfODE
> Smooth the data with a growing Gaussian kernel:
> $$p_t(x)=p_0(x)*\mathcal N(x;0,C(t))\qquad(5)$$
> This solves the Fokker-Planck equation with $f=0$, $GG^\top=\dot C$ (App. A.1). Rescale coordinates $\tilde x=A(t)\,x$ so the limit is a fixed Gaussian. The flow in rescaled coordinates is
> $$\frac{d\tilde x}{dt}=A(t)\Big(-\tfrac12\dot C(t)\,\nabla_x\log p_t(x)\Big)+\big(\dot A(t)A^{-1}(t)\big)\tilde x\qquad(6)$$
> with the score evaluated at $x=A^{-1}\tilde x$ (App. A.3, eq. 37).
>
> (source: de Albuquerque PDF, eqs. 5-6, p. 4)

- If the data were Gaussian with covariance $\Sigma(t)$, the rescaled density $\mathcal N(0,A\Sigma A^\top)$ is stationary when $\dot\Sigma=\dot C$ and $\dot A\Sigma A^\top+A\Sigma\dot A^\top=0$ (eq. 31, App. A.2).
- For isotropic $C=c^2I$, $A=\alpha I$, eq. 6 is the pfODE of Karras et al. 2022 (their eq. 4) (App. A.4, eq. 40). Karras et al. not read.
- The map is deterministic and invertible, so it is identifiable given $C$, $A$ and the score (p. 4, §5).

### Dimension-preserving flows (§3.1, pp. 4-5)

Dimension is measured by the [[Participation ratio]] $\mathrm{PR}(\Sigma)=\mathrm{tr}(\Sigma)^2/\mathrm{tr}(\Sigma^2)$ (eq. 7, p. 5). Take $C(t)$ diagonal in the eigenbasis of the initial data covariance $\Sigma_0$, so $\Sigma(t)=\mathrm{diag}(\sigma^2(t))=C(t)+\Sigma_0$. Then
$$d\,\mathrm{PR}=0\iff\Big(\mathbf 1-\mathrm{PR}(\sigma^2)\frac{\sigma^2}{\sum_k\sigma_k^2}\Big)\cdot d\sigma^2=0\qquad(8)$$
The simplest solution is proportional inflation, $d(\sigma^2)/dt=\rho\,\sigma^2$, which gives
$$C_{jj}(t)=\sigma_j^2(t)-\sigma_{0j}^2=\sigma_{0j}^2\,(e^{\rho t}-1),\qquad A_{jj}(t)=\frac{A_{0j}}{\sigma_j(t)}=\frac{A_{0j}}{\sigma_{0j}}\,e^{-\rho t/2}\qquad(9)$$
The rescaled covariance $\tilde\Sigma=A\Sigma A^\top=\mathrm{diag}(A_{0j}^2)$ is constant in time.

Wiki note: eq. 9 adds noise along each principal direction with variance proportional to that direction's data variance. In whitened coordinates $y_j=x_j/\sigma_{0j}$ the noise variance is $e^{\rho t}-1$ for every $j$, so the PR-preserving schedule is isotropic (VE-type) noise on [[Principal component analysis|PCA]]-whitened data. The paper never uses the word "whiten"; this reading is the wiki's. It is consistent with the network input preconditioner $C_\text{in}=\Sigma^{-1/2}(t)$ (eqs. 67-68), which whitens the noisy input.

### Dimension-reducing flows (§3.2, pp. 5-6; App. A.6)

Let directions inflate at different rates, $d(\sigma^2)/dt=\rho\,g\odot\sigma^2$, with $g_*=\max_i g_i$. Then
$$\mathrm{PR}(\Sigma(t))=\frac{\big(\sum_i\sigma_{0i}^2e^{(g_i-g_*)\rho t}\big)^2}{\sum_i\big(\sigma_{0i}^2e^{(g_i-g_*)\rho t}\big)^2}\;\longrightarrow\;\frac{\big(\sum_{k\le K}\sigma_{0i_k}^2\big)^2}{\sum_{k\le K}\sigma_{0i_k}^4}\qquad(10)$$
the PR of the covariance truncated to the $K$ directions with $g_i=g_*$. A single global rescaling $\alpha(t)\propto A_0e^{-\rho g_*t/2}$ is used, so slower directions shrink relative to the fastest.

- The "inflation gap" $\mathrm{IG}=g_*-g_i$ (p. 8, App. B.2) sets the compression: the variance ratio between kept and compressed directions is $e^{\rho(g_*-g_i)T}$ at the end time $T$.
- The flow is not a linear projection onto the top $K$ principal components: the score term in eq. 6 couples dimensions even when $C$ and $A$ are diagonal, so a particle's final position in the kept dimensions depends on its initial position in the full space (p. 6, Fig. 3).
- Compression is limited by the range of noise levels over which the score is accurate (p. 6).

### Training and integration (§4; App. B.1-B.3)

- Denoiser loss with full-covariance noise (eq. 11): $\mathbb E_y\,\mathbb E_{n\sim\mathcal N(0,C(t))}\|D(y+n;C(t))-y\|^2$; the score is $C^{-1}(t)\,(D(x;C(t))-x)$ (eq. 80). See [[Score matching]].
- Matrix versions of the Karras et al. preconditioners, with $W,\sigma_0^2$ from an SVD of the data and $\gamma(t)$ the diagonal of $C(t)$ in that basis: $C_\text{in}=\Sigma^{-1/2}(t)=W\,\mathrm{diag}\big(1/\sqrt{\sigma_0^2+\gamma(t)}\big)W^\top$ (eqs. 67-68), $C_\text{skip}=\Sigma_0\Sigma^{-1}(t)$ (eq. 73), $C_\text{out}=W\,\mathrm{diag}\big(\sqrt{\sigma_0^2\odot\gamma/(\sigma_0^2+\gamma)}\big)W^\top$ (eq. 78), loss weight $\Lambda(t)=C_\text{out}^{-1}$ (eq. 79).
- Schedules (App. B.2): PR-preserving $g=1$, $\rho=2$; PR-reducing $\rho=1$, $g=2$ on kept directions and $g=2-\mathrm{IG}$ on compressed ones.
- Integration (App. B.3): Euler for toy data (step $10^{-2}$), Heun for images (Algorithm 1, p. 26), $t_\text{max}=15.01$; 118 network evaluations for round trips, 256 for FID.

### Calibration (§5, pp. 6-7; App. B.6, C.2-C.3)

Uncertainty in data space is carried to the latent space by integrating eq. 6 forward on a set of points (and the reverse for a latent prior). Toy experiments check coverage of mapped regions with alpha-shapes and meshes (App. C.2.1, Fig. 10). Denoiser residuals along integration trajectories show negligible autocorrelation on toy data and some at small time lags on CIFAR-10; the authors report that this does not seem to affect round-trip accuracy or sample quality (App. C.3, Fig. 13, pp. 37-38).

> [!example] Sampling a latent posterior with HMC (Fig. 4, App. B.6)
> 2D circles data, latent prior a 3-component Gaussian mixture with weights (0.5, 0.25, 0.25), 2000 noisy observations. [[Hamiltonian Monte Carlo]] (hamiltorch, $L=15$ leapfrog steps, burn-in 500, thinning 5) through the flow gives posteriors that cover the truth. Each sample costs about 40 minutes and burn-in took 2-4 weeks, yielding 1872 and 1635 samples; the authors conclude sampling-based inference through the flow is impractical.

## Results

FID / round-trip MSE at inflation gap 1.02, by number of kept dimensions $d$ out of 3072 (Table 1, p. 8):

| $d$ | AFHQv2 | CIFAR-10 |
|---|---|---|
| 1 | 12.65 / 1.47 | 20.76 / 1.07 |
| 2 | 11.95 / 1.55 | 21.29 / 0.81 |
| 30 | 13.64 / 3.79 | 23.36 / 2.21 |
| 62 | 14.05 / 5.32 | 23.30 / 2.27 |
| 307 | 15.64 / 3.33 | 28.07 / 0.71 |
| 615 | 14.63 / 2.42 | 24.49 / 0.29 |
| 1536 | 13.36 / 0.14 | 17.44 / 0.16 |
| 3041 | 13.97 / 0.28 | 16.60 / 0.30 |
| 3072 (PR-preserving) | 11.90 / 0.38 | 17.01 / 0.22 |

- Larger gaps hurt: AFHQv2, $d=2$, FID 11.95, 13.98, 17.84, 34.68, 107.64 at IG 1.02, 1.10, 1.25, 1.35, 1.50 (Table 2).
- Against injective flows on CIFAR-10 (Table 3, FID): $d=30$: 23.3 vs M-Flow 541.2, Rectangular Flow 544.0, Canonical Manifold Flow 532.6; $d=40$: 24.3 vs 535.7, 481.3, 444.6; $d=62$: 23.2 vs 280.9, 280.8, 287.9.
- Compressed-direction latent variance falls from $2.15\times10^{-7}$ (IG 1.02) to $1.76\times10^{-10}$ (IG 1.50) (Table 11).
- Dataset PR (Table 15): MNIST 30.69, Fashion MNIST 7.90, SVHN 2.90, CIFAR-10 9.24.

## Limitations

Stated by the authors (p. 9; App. C.2.3):

> [!failure]
> - PR uses only second-order statistics and favours the top principal components; the kept subspace is chosen by variance, and rescaling the input dimensions changes what gets compressed.
> - The network must be trained over a much larger range of noise levels than a standard diffusion model.
> - Generation quality trades off against the inflation gap and the number of kept dimensions.
> - Posterior sampling through the flow (HMC) is very slow.

Wiki note: "nominal dimension 1" does not mean the image is stored in one number to working precision. The compressed directions have small but nonzero latent variance (Table 11), and the round-trip MSE is largest at intermediate $d$ (Table 1).

## Connections

- Builds on [[Score SDE (Song 2021)]] (pfODE) and the EDM preconditioning of Karras et al. 2022; reduces to the latter for isotropic noise (App. A.4).
- Equivalent to [[Flow matching]] with Gaussian conditional paths generalized to full covariance (§7, App. A.5): with $x_t=\Sigma_t^{1/2}(x_1)\,x_0+\mu_t(x_1)$ (eq. 44) the conditional velocity is $\dot\Sigma_t^{1/2}\Sigma_t^{-1/2}(x-\mu_t)+\dot\mu_t$ (eq. 45), and $\mu_t=A_tx_1$, $\Sigma_t=A_tC_tA_t^\top$ (eq. 46) recovers eq. 6 (eqs. 47-50). So the flow could be trained by flow matching instead of denoising.
- [[Spectral diffusion]] ([[PISD (Gallon 2026)]]) also rescales each mode by a data statistic before diffusing; there the modes are a fixed spectral basis, here they are the data's principal components (Wiki note).
- [[Normalizing flows]]: same goal of an invertible map with a tractable latent, reached without restricting the architecture.
- [[Diffusion posterior sampling]] conditions a diffusion prior on data by guidance; here the posterior over latents is obtained by pushing uncertainty through the flow, or by MCMC in the latent space.

%% refs:start %%
**Cites in this wiki**: [[DDIM (Song 2021)]], [[DDPM (Ho 2020)]], [[Score SDE (Song 2021)]], [[VAE paper (Kingma 2014)]]
**Software cited**: [[software#scikit-learn|scikit-learn]]
%% refs:end %%

**Sources**: `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models.pdf`, `papers/Diffusion/de Albuquerque, Pearson - Inflationary Flows Calibrated Bayesian Inference with Diffusion-Based Models - Slides.pdf`.
**Last updated**: 2026-11-11

---

## Related pages
- [[Participation ratio]] · [[Diffusion models]] · [[Flow matching]] · [[Score matching]] · [[Fokker-Planck equation]]
- [[Principal component analysis]] · [[Normalizing flows]] · [[Hamiltonian Monte Carlo]] · [[Spectral diffusion]] · [[Noise schedule]]
- [[Flow matching tutorial (Chen 2024)]]
