---
type: paper
area: physics-informed
areas: [physics-informed, pde, inverse-problems]
source-ref: "Raissi, Yazdani, Karniadakis 2020, Science 367, eq. 1, pp. 2-3"
tags: [physics-informed, pde, inverse-problems, ml]
authors: ["[[Maziar Raissi]]", "[[Alireza Yazdani]]", "[[George Em Karniadakis]]"]
year: 2020
venue: "Science 367(6481), 1026-1030"
file: "papers/Physics Informed Architectures/Raissi, Yazdani, Karniadakis - Hidden fluid mechanics Learning velocity and pressure fields from flow visualizations.pdf"
---

# Hidden fluid mechanics (Raissi 2020)

**Summary**: Hidden fluid mechanics (HFM) is a [[PINN]] that takes only scattered space-time data on a passive scalar (dye, smoke, contrast agent) and infers the hidden velocity and pressure fields by enforcing the transport and incompressible [[Navier-Stokes equations]] through [[Automatic differentiation]]. No boundary or initial conditions are supplied. Demonstrated on a cylinder wake, a stenosed channel and a patient-specific 3D intracranial aneurysm.

**Authors**: Maziar Raissi, Alireza Yazdani, George Em Karniadakis · **Year**: 2020 · **File**: `papers/Physics Informed Architectures/Raissi, Yazdani, Karniadakis - Hidden fluid mechanics Learning velocity and pressure fields from flow visualizations.pdf`

---

## Problem

Flow visualization (PIV, MRI, dye) gives images, not velocity and pressure; internal flows such as blood in the vasculature are hard to measure at all (p. 1). The only observable is noisy data $\{t^n,x^n,y^n,z^n,c^n\}_{n=1}^N$ on the concentration $c$ of a passive scalar, a single point cloud scattered in space and time. The goal is the latent $u,v,w$ and pressure $p$ (p. 2). The passive scalar is advected and diffused but does not act on the flow (p. 2). The NS prior is described as a regulariser of an otherwise ill-posed inverse problem (p. 1).

## Method

A network $(t,x,y,z)\mapsto(c,u,v,w,p)$ is "physics-uninformed"; applying automatic differentiation to its outputs gives a physics-informed network $(t,x,y,z)\mapsto(e_1,\dots,e_5)$ (p. 2):
- $e_1$: residual of the scalar transport (advection-diffusion) equation;
- $e_2,e_3,e_4$: momentum residuals in $x,y,z$;
- $e_5$: continuity (divergence-free) residual.

Both networks share parameters and are trained on one loss (source: HFM.pdf, eq. 1, p. 2):
$$\mathrm{MSE}=\frac1N\sum_{n=1}^N|c(t^n,x^n,y^n,z^n)-c^n|^2+\sum_{i=1}^5\frac1M\sum_{m=1}^M|e_i(t^m,x^m,y^m,z^m)|^2.$$
The first term fits concentration data; the second enforces the PDEs at $M$ residual points whose number and location need not match the data. Minimization uses mini-batch Adam-type optimizers, so the equations can be penalized at "virtually infinitely many points" (pp. 2-3). Reynolds and Peclet numbers can also be treated as unknowns and discovered from concentration data alone (tables S2, S3; cited p. 3). The framework is agnostic to geometry and to initial and boundary conditions (p. 4).

Two conditions on the training domain (p. 3): the concentration field must be present in it, and there must be a nonzero normal concentration gradient $\partial c/\partial n\neq0$ at the boundaries so that a single velocity field is identifiable without velocity boundary conditions. Where concentration alone does not pin down the velocity, extra velocity or pressure data can be added (p. 3).

## Results

- **2D cylinder wake**, $Re=100$, $Pe=100$ (Fig. 2): training data from spectral-element DNS on an arbitrary "flower"-shaped domain in the wake; HFM recovers $u,v,p$ with good agreement to reference. The method breaks down with fewer than 5 time snapshots per vortex-shedding cycle or fewer than 250 spatial points (p. 3). Robust to noise and low resolution (supplement, cited p. 3).
- **2D stenosed channel**: wall shear stress inferred (supplement figs. S15-S18, cited p. 4).
- **3D intracranial aneurysm** (Fig. 3): concentration data only inside the aneurysm sac, no boundary information; reference and regressed concentration, velocity and pressure agree "very good, given the complexity" (p. 4). Wall shear stress is obtained at no extra cost (p. 4).
- Only one example (figs. S8, S9) uses velocity data; all others use concentration alone (p. 3).

## Limitations

- As stated: the concentration must carry enough gradient information at the boundary; otherwise extra velocity or pressure data is needed (p. 3).
- Wiki note: all data are DNS-generated and the passive-scalar field is assumed noise-corrupted but otherwise exact in the main text; the paper reports no real clinical images. Compare [[Cardiovascular flow PINNs (Kissas 2020)]], which uses real 4D flow MRI.
- Wiki note: training pathologies of the residual loss (loss balancing, causality) are not discussed here; see [[When and why PINNs fail (Wang 2022)]].

## Connections

- Builds on the PINN of [[PINNs (Raissi 2019)]], whose Navier-Stokes cylinder example inferred $\lambda$ from velocity data; HFM instead observes a scalar and infers velocity and pressure themselves.
- The "hidden state recovery from a different observable" idea is an [[Bayesian inverse problems]] setting solved by a [[Physics-informed prior]] in the Bayesian reading.
- Biomedical follow-ups from the same group: [[Cardiovascular flow PINNs (Kissas 2020)]], [[Cardiac activation PINN (Sahli Costabal 2020)]].

%% refs:start %%
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[NIF (Pan 2023)]], [[Respecting causality (Wang 2022)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Raissi, Yazdani, Karniadakis - Hidden fluid mechanics Learning velocity and pressure fields from flow visualizations.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[PINN]] · [[PINNs (Raissi 2019)]] · [[Navier-Stokes equations]] · [[Automatic differentiation]] · [[Physics-informed machine learning]]
- [[Cardiovascular flow PINNs (Kissas 2020)]] · [[Cardiac activation PINN (Sahli Costabal 2020)]] · [[Bayesian inverse problems]]
