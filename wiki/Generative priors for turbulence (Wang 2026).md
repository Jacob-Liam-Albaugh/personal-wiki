---
type: paper
area: ift
areas: [ift, stochastic]
source-ref: "Wang 2026, Phys. Rev. Fluids 11, 090502"
tags: [diffusion, generative, inverse-problems, pde]
authors: [Wang]
year: 2026
venue: "Physical Review Fluids 11, 090502 (Invited Article)"
file: "IFT/Wang - Generative priors for spatiotemporal turbulence.pdf"
---

# Generative priors for spatiotemporal turbulence (Wang 2026)

**Summary**: A perspective article arguing that diffusion and flow-matching models should be treated as reusable probabilistic priors $p_\theta(x)$ for turbulence rather than as surrogate architectures. A single pretrained prior can generate stochastic flow realizations, be conditioned on sparse or indirect measurements at inference time without retraining, and be scaled to large domains by local (patchwise) composition. The article also proposes six validation criteria. It is a review of the author's group's work; it contains no new experiments.

**Authors**: J.-X. Wang (Cornell) · **Year**: 2026 · **File**: `IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`

---

## Problem

Direct numerical simulation cost grows as $N\sim Re^{37/14}$ and wall-resolved LES as $Re^{13/7}$ grid points (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, Sec. I). Chaotic sensitivity limits deterministic prediction, and reconstruction from sparse sensors is ill-posed. The article notes that $L_2$ regression returns the posterior mean, which yields smoothed, energy-deficient fields, and that calibrated uncertainty is needed. The proposed remedy is to learn a distribution over plausible turbulent states and treat each task as conditioning that distribution.

## Method

The observation model is $y=\mathcal H(x)+\eta$, $\eta\sim\mathcal N(0,\Sigma)$ (eqs. 2, 13).

### Generative priors

> [!definition] Score-based diffusion (forward and reverse SDE)
> Forward: $dx=f(x,\tau)\,d\tau+g(\tau)\,dW$ (eq. 3); for DDPM $f=-\beta(\tau)x/2$ and $g=\sqrt{\beta}$. Reverse:
> $$dx=[f-g^2 s]\,d\tau+g\,d\bar W,\qquad s=\nabla_x\log p_\tau(x)$$
> (eq. 4), with the score $s$ learned by a network.
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eqs. 3-4)

See [[Diffusion models]] and [[Diffusion models]].

> [!definition] Probability-flow ODE
> $$dx=\big(f-\tfrac12 g^2\nabla_x\log p_\tau\big)\,d\tau$$
> (eq. 5): a deterministic flow with the same marginals as the reverse SDE.
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eq. 5)

See [[Diffusion models]].

> [!definition] Flow matching
> A learned velocity field $dx/d\tau=v_\theta(x,\tau)$ transports $x_0\sim p_0$ to $x_1\sim p_{\rm data}$ (eq. 6).
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eq. 6)

See [[Flow matching]]. The article describes diffusion and flow matching as two closely related parametrisations of probability transport (Sec. VIII).

### Spatiotemporal generation

Short space-time blocks $x^{(m)}=\{u(t_m),\dots,u(t_m+(K-1)\Delta t)\}$ (eq. 8). A Bayesian conditional diffusion model (Gao et al., cited as ref. 17) with 3D convolutions samples $x^{(m)}\sim p_\theta(x^{(m)}|c)$ (eq. 9); longer trajectories are produced autoregressively, $x^{(m+1)}\sim p_\theta(\cdot\,|\,T(x^{(m)}))$ (eq. 10).

> [!definition] CoNFiLD latent neural-field diffusion
> A conditional neural field decodes a latent code, $u(x,t)=D_\phi(x,t,z)$ (eq. 11); a latent diffusion prior is trained over $z$. Demonstrated on turbulent boundary layers over wall-mounted roughness blocks.
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eq. 11; Du et al., ref. 24)

See [[confild-latent-diffusion]]. CoNFiLD-inlet (ref. 39) generates synthetic inflow and is reported to beat digital filtering and deterministic ML baselines on downstream statistics; the text gives this qualitatively.

### Training-free conditioning

> [!theorem] Bayes conditioning of a pretrained prior
> $$p_\theta(x|y)\ \propto\ p_\theta(x)\,p(y|x),\qquad p(y|x)\propto\exp\{-\tfrac12\|y-\mathcal H(x)\|^2_{\Sigma^{-1}}\}$$
> (eqs. 7, 14, 15). The prior is fixed and only $\mathcal H$ changes per task, so sparse reconstruction, data assimilation, super-resolution and inpainting are all the same sampler with different $\mathcal H$.
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eqs. 7, 14-15, Sec. IV)

> [!algorithm] Three conditioning mechanisms
> 1. Diffusion posterior sampling (DPS): $\nabla\log p_\theta(x|y)\approx\nabla\log p_\theta(x)+\nabla\log p(y|x)$ (eq. 16), with the likelihood evaluated at the denoised estimate $\hat x_0$ (eq. 17).
> 2. Guided flow matching: $dx/d\tau=v_\theta+\lambda(\tau)\nabla\log p(y|\hat x)$ (eq. 18).
> 3. Source-space conditioning: with generator $x_1=T_\theta(x_0)$, sample the source posterior $p(x_0|y)\propto p_0(x_0)\,p(y|T_\theta(x_0))$ (eqs. 19-20) and push forward, $x_1^{(i)}=T_\theta(x_0^{(i)})$, $x_0^{(i)}\sim p(x_0|y)$ (eq. 21). The learned transport is unchanged; ref. 29 (Parikh et al., "D-Flow SGLD", arXiv:2602.21469, cited, not read) names SGLD for this source-space sampling.
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eqs. 16-21, pp. 12-14)

See [[Diffusion posterior sampling]].

### Scalable composition

Local, convolutional or coordinate-local priors are applied over larger domains and composed by overlapping patches, domain-decomposed latents or spatial marching (Sec. V, p. 16). Two examples: patchwise latent diffusion for wall pressure (Fan et al., ref. 30) with classifier-free guidance, and patch-additive flow matching (Parikh et al., ref. 56), where the full-domain density is approximated by a product of local patch densities and long sections are generated autoregressively, with sparse sensors and the previous section's boundary column entering as gradient corrections.

### Validation criteria

> [!definition] Nearest-neighbour memorisation test
> $$d_{\rm gen}=\min_{x_i\in\mathcal D_{\rm train}}d(x_{\rm gen},x_i),\qquad d_{\rm test}=\min_{x_i\in\mathcal D_{\rm train}}d(x_{\rm test},x_i)$$
> Evidence of memorisation is $d_{\rm gen}$ systematically much smaller than $d_{\rm test}$. Comparisons should be done in physical and in feature space, and train/test segments must be non-overlapping and separated by a decorrelation time.
>
> (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, eqs. 22-23, p. 18)

Table II (p. 19) lists six criteria: distributional fidelity, nonmemorization, data consistency, posterior calibration, physical admissibility, and scalable coherence, each with diagnostics (profiles, PDFs, spectra; nearest-neighbour search; observation residuals; coverage and spread versus observability; divergence and solver stability; cross-patch continuity and low-wavenumber spectra).

## Results

This is a review; the results below are the article's qualitative reports of prior work, with no tabulated error numbers in the sections read.

- CoNFiLD reconstructs full spatiotemporal trajectories for periodic hills and cube-array boundary layers from limited sensors, recovering the main coherent structures of the DNS reference with posterior ensembles giving uncertainty. More sensors contract the posterior, more noise broadens it. In super-resolution, finer input gives samples closer to the DNS; extremely coarse input approaches unconditional sampling (source: `Wang - Generative priors for spatiotemporal turbulence.pdf`, Fig. 6, pp. 14-15).
- Conditional flow matching for near-wall turbulence from wall pressure and shear (ref. 27): at $y^+=5$ the ensemble mean follows the truth with a narrow band; farther from the wall the spread grows. The author reads this as the correct response to reduced observability and separates aleatoric turbulent variability, measurement noise in the likelihood, and epistemic uncertainty from partial observation (Fig. 7, pp. 15-16).
- Patchwise priors enable long-span wall-pressure generation and reconstruction, with long-range coherence and low-wavenumber spectra flagged as needing explicit validation (pp. 16-17).

## Limitations

As stated by the author (Sec. VII, pp. 19-21):

- Physical structure is learned statistically; incompressibility, boundary conditions and conservation can be violated pointwise. Soft physics losses give no hard guarantee.
- Calibration of diffusion and flow-matching posteriors is established empirically; there is no theory comparable to ensemble or variational data assimilation.
- There is no practitioner rule for choosing among DPS, guided transport, source-space inference and learned observation models; systematic benchmarks are needed.
- Locality versus long-range coherence is an unresolved tension.
- Nonstationary flows require explicit conditioning on context, $p_\theta(x_{t:t+T}|c_{t:t+T})$ (eq. 24).
- Demonstrations rely on curated DNS/LES in canonical geometries; out-of-distribution detection is needed.

Wiki note: the article has no quantitative comparison table, so the claims of advantage over baselines are those of the cited papers, which were not read here.

## Connections

- Wiki note: the structure $p(x|y)\propto p(x)p(y|x)$ with a prior over fields matches [[Information field theory]] and the posterior of [[PIFT (Alberts 2023)]]; the difference is that IFT/PIFT derives the prior from a Hamiltonian ($e^{-\beta U}$, see [[Physics-informed prior]]) whereas here it is learned from data. The article itself does not mention IFT.
- Wiki note: the reverse diffusion SDE with score $\nabla\log p_\tau$ is a Langevin-type sampler, related to [[SGLD]] and [[SG-MCMC]]. The only explicit link in the article is the source-space method of ref. 29, which is named after SGLD.
- Wiki note: the article's call for "physics-as-architecture" and solver-coupled priors (Sec. VII) is the problem [[IFT thermal conductivity (Alberts 2026)]] addresses from the physics-prior side, with a PDE energy as prior.
- Related diffusion/score-based references listed in the article: Ho et al. (DDPM) and Song et al. (score SDE) [refs. 13-14]; Lipman et al. (flow matching) [ref. 26].

**Sources**: `IFT/Wang - Generative priors for spatiotemporal turbulence.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]]
- [[Diffusion models]]
- [[Diffusion models]]
- [[Diffusion models]]
- [[Flow matching]]
- [[Diffusion posterior sampling]]
- [[confild-latent-diffusion]]
- [[SGLD]]
- [[SG-MCMC]]
- [[Physics-informed prior]]
- [[PIFT (Alberts 2023)]]
- [[IFT thermal conductivity (Alberts 2026)]]
