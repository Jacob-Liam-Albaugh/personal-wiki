---
type: paper
area: physics-informed
areas: [physics-informed, bayesian, inverse-problems]
source-ref: "Hans et al. 2026, Med. Image Anal. 114, 104230, eqs. 1-14, §2-3"
tags: [physics-informed, bayesian, inverse-problems, ml, pde]
authors: ["[[Atharva Hans]]", "[[Abhishek Singh]]", "[[Yue-Hin Loke]]", "[[Pavlos P. Vlachos]]", "[[Ilias Bilionis]]"]
year: 2026
venue: "Medical Image Analysis 114, 104230"
file: "[[papers/Physics Informed Architectures/Hans, Singh, Loke, Vlachos, Bilionis - Patient-specific unsupervised neural reconstruction of cardiac blood flow from 4D flow MRI.pdf]]"
---

# SMURF (Hans 2026)

**Summary**: SMURF (Scalable Method for Unsupervised Reconstruction of Flow) fits two coordinate-based neural fields per patient, a probabilistic geometry field and a three-component velocity field, to 4D flow MRI magnitude and phase-derived velocity through one shared likelihood. Segmentation and velocity reconstruction become a single label-free inference problem with no physics loss. On 12 pediatric cases it matches expert segmentations to about 1 voxel (Normal) and 1.3 voxels (Fontan) and cuts RMS divergence and vorticity-transport residuals by about 70-80% against an FDA-cleared pipeline.

**Authors**: Atharva Hans, Abhishek Singh, Yue-Hin Loke, Pavlos P. Vlachos, Ilias Bilionis · **Year**: 2026 · **File**: [[papers/Physics Informed Architectures/Hans, Singh, Loke, Vlachos, Bilionis - Patient-specific unsupervised neural reconstruction of cardiac blood flow from 4D flow MRI.pdf]]

---

## Problem

4D flow MRI gives noisy, low-resolution, time-resolved 3D velocity. Clinical use needs a time-varying cardiac geometry and a clean velocity field inside it. Current workflows segment by hand or semi-automatically (about 40.1 ± 15.7 min post-processing plus about 30 min manual segmentation per patient, p. 1) and filter velocity afterwards, so segmentation errors propagate into velocity and velocity never refines segmentation. Labelled 4D flow data are scarce, and pediatric and congenital anatomies break supervised models (p. 1). Goal: infer geometry and velocity together from one patient's magnitude and phase alone.

## Method

Input is image-space data: magnitude $y^{mag}_{it}$ and velocity $\mathbf y^{vel}_{it}=\text{phase}\cdot\text{venc}/\pi$ at voxel $i$, time $t$ (p. 2). k-space and image reconstruction are out of scope.

**Geometry field** $\mathbf g_\psi:\Omega\times[0,T]\to\mathbb R^M$ with a latent class $z_{it}$ per voxel and time (eq. 1, p. 3):
$$p(z_{it}=m\mid\psi)=\mathrm{sparsemax}(\mathbf g_\psi(\mathbf r_i,t))_m.$$
Sparsemax can give exactly zero probability to unused classes, so $M=6$ is only an upper bound; $M=3$ to $9$ gave no material change (p. 5). Hard segmentation is the arg-max class. Intermediate probabilities near walls represent partial volume (§2.1, §3.3).

**Likelihoods** (pp. 3-4):
- magnitude, class-conditional Gaussian with learnable $\mu_m,\sigma_m^2$ (eq. 2), marginalised over class (eq. 3), product over voxels and time (eq. 4);
- velocity, $\mathbf y^{vel}_{it}\mid z_{it}=m\sim\mathcal N(\mathbf v_\phi(\mathbf r_i,t),\Sigma_m)$ with diagonal class-specific noise $\Sigma_m$ (eq. 5), marginalised (eq. 6), product (eq. 7).

> [!algorithm] SMURF-Coupled
> Minimise the regularised negative log-likelihood over $\theta=\{\psi,\phi,(\mu_m,\sigma_m^2),\{\Sigma_m\}\}$:
> $$\text{Loss}_{data}=-\log p(\mathbf Y^{mag}\mid\psi)-\log p(\mathbf Y^{vel}\mid\psi,\phi)\quad(\text{eqs. 8-9}),$$
> $$\text{Loss}_{l2}=\alpha_{geom}\|\psi\|_2^2+\alpha_{vel}\|\phi\|_2^2\quad(\text{eq. 10}),$$
> $$\text{Loss}_{total}=\text{Loss}_{data}+\text{Loss}_{l2}\quad(\text{eq. 11}).$$
> The shared $p(z_{it}=m\mid\psi)$ sits in both likelihoods, so velocity evidence moves the geometry and geometry gates the velocity fit.
>
> (source: `Hans ... 4D flow MRI.pdf`, §2.4.1, Alg. 1)

**SMURF-Sequential** (§2.4.2, eqs. 12-13): stage 1 minimises the magnitude-only loss for $\psi$, giving a fixed hard mask $\mathcal F$; stage 2 fits $\phi$ and $\Sigma_{flow}$ by masked velocity likelihood with $\mathcal F$ held fixed. Same likelihood and architecture; the only difference is whether geometry is updated by velocity.

**Subsampling** (§2.5, eq. 14): the log-likelihoods are estimated on random time and voxel index sets of sizes $S_t,S_v$, scaled by $N_tN_v/(S_tS_v)$, so a step costs the minibatch, not the scan.

**Architecture** (§2.7): separate modified (gated) MLPs from [[Expert's guide to PINNs (Wang 2023)]] on $(x,y,z,t)$ with [[Fourier features]] to counter [[Spectral bias]], 4 hidden layers of width 256, tanh, and random weight factorization (RWF). One geometry head with $M$ logits and three independent velocity heads, one per component, which performed better than one joint head (p. 4). The authors call these implicit neural representations (INRs) and the same function class as [[PINN]]s, but with a likelihood objective and no PDE residual (p. 5). Compare [[Neural implicit flow]], also a coordinate network.

**Training** (§2.6): JAX and Equinox, [[Adam]] with $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$, constant learning rate $10^{-3}$; 750 epochs; float32; data standardised; $\mu_m$ initialised evenly in $[-1,1]$, variances 1; $S_t$, $S_v$ are 10% of $N_t$, $N_v$; $\alpha_{geom}=250$, $\alpha_{vel}=1000$ chosen to minimise cohort-level expert→SMURF surface distance (p. 5).

**Evaluation definitions** (§2.8-2.10):
- Surface distance: meshes from binarised masks (zero-pad 1 voxel, marching cubes at isovalue 0.5, hole filling, Laplacian 50 iterations at relaxation 0.01, then Taubin 50 iterations). For each expert-surface vertex, the Euclidean distance to the nearest SMURF-surface point, divided by the minimum voxel edge length, in voxel units. One-sided on purpose (expert→SMURF) so SMURF is not penalised for valid flow beyond the expert region of interest (p. 6).
- Overlap: voxelwise Dice (and accuracy, recall) on native-resolution binary masks, restricted to the expert time-union 3D bounding box (p. 7).
- Conservation residuals, with $\nu=3.3\times10^{-6}\,\mathrm{m^2\,s^{-1}}$ (p. 6):
$$r_{div}=\nabla\!\cdot\mathbf v\ \ [\mathrm{s^{-1}}],$$
$$\mathbf R_{mom}=\partial_t\boldsymbol\omega+\nabla\times(\mathbf v\times\boldsymbol\omega)-\nu\nabla^2\boldsymbol\omega\ \ [\mathrm{s^{-2}}],\quad\boldsymbol\omega=\nabla\times\mathbf v.$$
The vorticity form avoids the unknown pressure gradient. Reported as the spatial RMS inside the segmentation at each cardiac phase. SMURF derivatives come from autodiff of the field; Tempus uses second-order central differences inside the expert mask and one-sided stencils at its boundary, with second-order temporal differences.
- Q-criterion $Q=\tfrac12(\|\Omega\|_F^2-\|S\|_F^2)$ isosurfaces at $5Q^+$ for visualisation only (§2.10).

## Results

Data: 12 pediatric studies (4 Normal, 8 Fontan), 1.5 T, ferumoxytol-enhanced, 30 time frames, venc 150-200 cm/s, 2,841,300-7,310,160 space-time points per case (§2.6, §2.11). References: expert iTFlow segmentations by a pediatric cardiologist and Tempus velocities (FDA-cleared).

- **Speed** (§2.6): 4.7-11.4 min per case for 750 epochs on one H100 80 GB, about five- to fifteen-fold shorter than reported semiautomatic workflows; convergence often in about half the epochs.
- **Segmentation vs expert** (§3.2, Fig. 2): both SMURF variants stay about one voxel from the expert surface; SMURF-Coupled has lower surface error than SMURF-Sequential in 9 of 12 subjects. About 1 voxel (Normal) and about 1.3 voxels (Fontan) for SMURF-Coupled. Dice stays close to 75% across the cycle for SMURF-Coupled, SMURF-Sequential slightly lower, MedSAM2-Mag generally near 50%, MedSAM2-Angio more phase-dependent. Discussion reports accuracy about 0.88-0.90 and Dice about 0.70-0.75 (§4). MedSAM2 baselines stay several voxels away; their lower Dice is mostly lower recall (Suppl. Table 1, not in the PDF).
- **Velocity residuals vs Tempus** (§3.4, Fig. 3): RMS divergence residual falls by 75-82% and RMS momentum residual by 69-84%, depending on cohort and phase. Tempus+DFW changes both by typically less than 10%. In Normal cases SMURF-Sequential has the lower momentum residual on average; in Fontan SMURF-Coupled has the lowest, and Sequential shows late-systole excursions. Absolute residuals stay non-zero for all methods; the paper stresses the relative reduction.
- **Qualitative** (§3.5, Figs. 4-6): fewer wall artefacts, a coherent mitral vortex ring in the Normal case, and a thin tricuspid regurgitant jet in the Fontan case where Tempus shows background phase leakage. Fields were evaluated on a grid 2x denser per axis for display (4x in Fig. 1d) without retraining.

## Limitations

As stated (§4): expert labels encode cohort-dependent regions of interest and phase-dependent smoothing; residuals use autodiff for SMURF but finite differences for Tempus, so derivative operators affect magnitudes; constant viscosity and no pressure or energy balance; modest pediatric cohort; no ground-truth velocity, so residuals are a proxy; no vessel-specific labels and closely apposed great vessels can merge near the pulmonary bifurcation; no non-contrast evaluation (all scans used ferumoxytol).

Wiki note: residuals are emergent checks, not optimised, so a PINN would drive them lower by construction; the comparison is against a post-processing pipeline, not against a PINN or other neural baseline. Segmentation uncertainty is available in the probability field but only the arg-max mask is used.

## Connections

- Shares INR ingredients with [[PINN]]-style networks but drops the PDE residual: a probabilistic measurement model replaces physics loss. The authors note a physics term could be added, linking to Bayesian PINN and information-field-theory formulations (cites Alberts and Bilionis 2023; see [[PIFT (Alberts 2023)]], [[Physics-informed prior]]).
- Same data modality as [[Cardiovascular flow PINNs (Kissas 2020)]], which reduces 4D flow MRI to a 1D vessel network with PDE residuals instead of a 3D field.
- Architecture follows [[Expert's guide to PINNs (Wang 2023)]] (modified MLP, RWF) and [[Fourier features (Tancik 2020)]]; compare the INR in [[SIREN]] and [[NIF (Pan 2023)]].
- The residual diagnostic uses the incompressible [[Navier-Stokes equations]] in vorticity form.
- Lab paper (Bilionis is last author).

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Fourier features (Tancik 2020)]], [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[SIREN paper (Sitzmann 2020)]], [[Spectral bias (Rahaman 2019)]]
**Software cited**: [[software#JAX|JAX]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Hans, Singh, Loke, Vlachos, Bilionis - Patient-specific unsupervised neural reconstruction of cardiac blood flow from 4D flow MRI.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[PINN]] · [[Neural implicit flow]] · [[Fourier features]] · [[Spectral bias]] · [[Adam]] · [[Navier-Stokes equations]] · [[Cardiovascular flow PINNs (Kissas 2020)]] · [[Expert's guide to PINNs (Wang 2023)]] · [[Physics-informed prior]]
