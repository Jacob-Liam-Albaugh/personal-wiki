---
type: paper
area: physics-informed
areas: [physics-informed, pde, inverse-problems]
source-ref: "Kissas et al. 2020, CMAME 358:112623, eqs. 1-20"
tags: [physics-informed, pde, inverse-problems, ml]
authors: ["[[Georgios Kissas]]", "[[Yibo Yang]]", "[[Eileen Hwuang]]", "[[Walter R. Witschey]]", "[[John A. Detre]]", "[[Paris Perdikaris]]"]
year: 2020
venue: "Computer Methods in Applied Mechanics and Engineering 358, 112623"
file: "papers/Physics Informed Architectures/Kissas et al - Machine learning in cardiovascular flows modeling Predicting arterial blood pressure from non-invasive 4D flow MRI data.pdf"
---

# Cardiovascular flow PINNs (Kissas 2020)

**Summary**: One PINN per vessel of a 1D arterial network, trained on noisy area and velocity time series (no pressure data) and coupled at bifurcations by mass and momentum conservation. The area-pressure wall law makes absolute pressure identifiable. Non-dimensionalization is shown to be essential, and a trained network is used to calibrate [[Windkessel model]] outflow parameters by post-processing. First PINN applied to real noisy clinical data (4D flow MRI).

**Authors**: Georgios Kissas, Yibo Yang, Eileen Hwuang, Walter R. Witschey, John A. Detre, Paris Perdikaris · **Year**: 2020 · **File**: `papers/Physics Informed Architectures/Kissas et al - Machine learning in cardiovascular flows modeling Predicting arterial blood pressure from non-invasive 4D flow MRI data.pdf`

---

## Problem

Arterial pressure is hard to measure non-invasively, while area (2D cine MRI) and velocity (phase-contrast / 4D flow MRI) are measurable. Conventional 1D solvers need tedious geometry, boundary-condition and Windkessel calibration (p. 1). Goal: infer pressure from area and velocity alone.

## Method

**1D reduced model** (source: Kissas.pdf, eq. 1, p. 4): incompressible, Newtonian, thin elastic wall:
$$\partial_tA+\partial_x(Au)=0,$$
$$\partial_tu+\alpha u\,\partial_xu+\tfrac uA\partial_x\big((\alpha-1)uA\big)+\tfrac1\rho\partial_xp-K_R\tfrac uA=0,$$
$$p=p_{ext}+\beta(\sqrt A-\sqrt{A_0}).$$
Neglects tortuosity and curvature (p. 4).

**One network per vessel** $j$: $[x,t]\mapsto[A_j,u_j,p_j]$ with residuals $r_A,r_u,r_p$ (eq. 2, p. 5). Momentum alone gives only $\partial_xp$; the wall law $r_p$ is what makes absolute pressure identifiable (p. 5). Only $A$ and $u$ are measured (p. 5).

Loss terms (pp. 5-8):
- measurements, eq. 3: MSE on $u$ and $A$ at scattered points;
- residuals, eq. 4: mean squared $r_A,r_u,r_p$ at [[Latin hypercube sampling]] collocation points;
- interfaces, eqs. 5-8: at a bifurcation of parent 1 into 2 and 3,
$$A_1u_1=A_2u_2+A_3u_3,\quad p_1+\tfrac12\rho u_1^2=p_i+\tfrac12\rho u_i^2\ (i=2,3).$$
Characteristic-variable (Riemann) constraints were tried and gave no benefit (p. 8).

Total loss (eq. 9, p. 8):
$$\mathcal L=\sum_{j\in D_M}\mathcal L^j_{meas}+\sum_{j=1}^D\mathcal L^j_{res}+\sum_{k=1}^{D_I}\mathcal L^k_{int}.$$
Information from one vessel propagates to neighbours through the interface term (p. 8).

**Non-dimensionalization and normalization** (§2.7, pp. 9-10): raw magnitudes ($P\sim10^6$ Pa, $A\sim10^{-5}$ m$^2$, $u\sim10$ m/s) wreck back-propagated gradients. The paper picks $L=\sqrt{\tfrac1N\sum_jA_0^j}$, $U=10$ and
$$\hat u=u/U,\ \hat A=A/A_0,\ \hat p=p/p_0,\ x^*=x/L,\ t^*=t/T,\quad p_0=\rho U^2,\ T=L/U\quad(\text{eq. 13}),$$
then standardizes $x^*,t^*$ to zero mean, unit variance per vessel (eq. 14), consistent with Glorot init and tanh. See [[Non-dimensionalization]]. The authors prefer this to hand-tuned loss weights (p. 9).

**Windkessel calibration** (§2.8, pp. 11-12): with trained networks giving outlet $p_j(t)$ and $Q_j=A_ju_j$, solve the three-element [[Windkessel model]] ODE (eq. 19) on a grid of $(R,C)$ and minimize $\frac1{N_t}\sum\|\tilde p-p\|^2$ (eq. 20); refine the grid around the best point 5 times (about 10 min per outlet on a laptop).

## Results

Setup: 7 hidden layers x 100 tanh, Xavier init, Adam at $10^{-3}$ then $10^{-4}$, batch 1024, single precision (Table 1, p. 13). Largest case trains about 7 h on one P100 (p. 11).
- **Y-bifurcation** (synthetic, discontinuous-Galerkin data): without non-dimensionalization the prediction collapses (Fig. 5); with it pressure matches the DG reference, though secondary waveform peaks are missed (p. 14). Over 50 seeds the relative $L^2$ pressure error is $5.29\pm2.38\times10^{-2}$ in single and $4.25\pm1.99\times10^{-2}$ in double precision (p. 16). Larger networks do better, read as the residual regularizing against overfitting (p. 17). Mass and momentum are conserved at the junction (Fig. 7).
- **Idealized pelvic network** (7 vessels, 3 bifurcations): data only at vessel midpoints, none at boundaries or in vessels 2 and 3; some discrepancy in the unmeasured vessels (p. 19).
- **Aorta/carotid bifurcation, real 4D flow MRI** of one healthy volunteer: training on Aorta 1, Aorta 4 and carotid, test on Aorta 3. Area and velocity at the test point agree well; predicted pressure is 80-120 mmHg, consistent with healthy values (p. 22). Waveforms were smoothed with a periodic-kernel [[Gaussian process]] (p. 21). A DG solver run with the identified Windkessel parameters captures magnitude and peak timing, with a larger discrepancy and time shift at the carotid (p. 24).

## Limitations

As stated (§4, pp. 24-25): training takes hours and must drop to minutes (transfer learning suggested); the MSE loss assumes isotropic Gaussian noise, unlike real heteroscedastic noise; data fit and physics can conflict under noise; the 1D model ignores 3D effects, non-Newtonian rheology and wall viscoelasticity; uncertainty quantification is absent (ensembles, MCMC, generative models suggested). No ground-truth pressure exists for the clinical case.

## Connections

- Applies [[PINNs (Raissi 2019)]] to a graph of subdomains (a conservation-law form of domain decomposition); same group and venue family as [[Hidden fluid mechanics (Raissi 2020)]].
- The scaling argument anticipates the pipeline in [[Expert's guide to PINNs (Wang 2023)]]; the single-seed fragility fits the failure analysis in [[When and why PINNs fail (Wang 2022)]].
- Wiki note: the authors call it "PDE-constrained filtering of scattered noisy data" (p. 25), close to the [[Physics-informed prior]] reading.
- Companion cardiac paper by two of the same authors: [[Cardiac activation PINN (Sahli Costabal 2020)]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Bayesian DenseED surrogate (Zhu 2018)]], [[Glorot init (Glorot 2010)]], [[PINNs (Raissi 2019)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[PIFT (Alberts 2023)]], [[Respecting causality (Wang 2022)]], [[When and why PINNs fail (Wang 2022)]]
**Software cited**: [[software#PyTorch|PyTorch]], [[software#TensorFlow|TensorFlow]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Kissas et al - Machine learning in cardiovascular flows modeling Predicting arterial blood pressure from non-invasive 4D flow MRI data.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[PINN]] · [[PINNs (Raissi 2019)]] · [[Non-dimensionalization]] · [[Windkessel model]] · [[Latin hypercube sampling]] · [[Gaussian process]]
- [[Hidden fluid mechanics (Raissi 2020)]] · [[Cardiac activation PINN (Sahli Costabal 2020)]] · [[Physics-informed machine learning]]
