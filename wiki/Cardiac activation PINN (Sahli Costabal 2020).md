---
type: paper
area: physics-informed
areas: [physics-informed, pde, inverse-problems, uq]
source-ref: "Sahli Costabal et al. 2020, Front. Phys. 8:42, eqs. 1-10, Alg. 1"
tags: [physics-informed, pde, inverse-problems, uq, ml]
authors: ["[[Francisco Sahli Costabal]]", "[[Yibo Yang]]", "[[Paris Perdikaris]]", "[[Daniel E. Hurtado]]", "[[Ellen Kuhl]]"]
year: 2020
venue: "Frontiers in Physics 8, 42"
file: "papers/Physics Informed Architectures/Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf"
---

# Cardiac activation PINN (Sahli Costabal 2020)

**Summary**: A PINN for electro-anatomic mapping of the atria: two networks give activation time $T(x)$ and conduction velocity $V(x)$, tied by the [[Eikonal equation]] and trained on a few sparse activation-time measurements. An ensemble with [[Randomized prior functions]] gives epistemic uncertainty, whose entropy drives an [[Active learning]] rule choosing the next catheter location. Beats linear interpolation and GP regression on a synthetic benchmark and linear interpolation on a simulated left atrium.

**Authors**: Francisco Sahli Costabal, Yibo Yang, Paris Perdikaris, Daniel E. Hurtado, Ellen Kuhl · **Year**: 2020 · **File**: `papers/Physics Informed Architectures/Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf`

---

## Problem

Atrial fibrillation diagnosis uses activation maps: a catheter records activation times at sparse sites and the values are interpolated (linearly or by radial basis functions). Interpolation ignores the wave physics, yields artificially high conduction velocities, and gives no guidance on where to measure next (pp. 1-2).

## Method

The activation time satisfies the [[Eikonal equation]] (source: Costabal.pdf, eqs. 1-2, p. 2):
$$\|\nabla T(x)\|=\frac1{V(x)},\qquad R(x):=V(x)\|\nabla T\|-1=0.$$
Two networks $T\approx NN_T(x;\theta_T)$ and $V\approx V_{max}\,\sigma(NN_V(x;\theta_V))$ (eqs. 3-5); the sigmoid keeps $V$ positive and bounded. Loss (eq. 6, p. 2):
$$\mathcal L=\tfrac1{N_T}\sum_i(T(x_i)-\hat T_i)^2+\tfrac1{N_R}\sum_iR(x_i)^2+\alpha_{TV}\tfrac1{N_R}\sum_i\|\nabla V(x_i)\|+\alpha_{L2}\sum\theta_{T}^2.$$
The total-variation term lets $V$ jump (slow or fibrotic patches); the L2 term on $\theta_T$ is what makes the prior-ensemble reading valid.

**Surfaces** (§2.4, p. 4): the atrium is a triangulated surface; collocation points are triangle centroids and a normal penalty
$$\mathcal L_N=\alpha_N\tfrac1{N_R}\sum_i|\nabla T(x_i)\cdot N_i|^2\quad(\text{eq. }10)$$
pushes the gradient tangent to the surface (applied weakly, since exact enforcement would force linear interpolation).

**Uncertainty** (§2.2, p. 3): each ensemble member is $NN(x;\theta)+NN(x;\tilde\theta)$ with $\tilde\theta$ a fixed randomly drawn prior network (eqs. 8-9) and data perturbed by $N(0,\sigma_N^2)$; the prediction is the ensemble mean. See [[Randomized prior functions]].

**Active learning** (Alg. 1, pp. 3-4): start from $N_{init}$ random samples; repeatedly compute the entropy $H(x)$ of the predictive $p(T|D)$ over candidate sites (non-parametric estimator, since the posterior is not Gaussian), acquire at $\arg\max H$, retrain briefly with Adam. Training and acquisition can run in parallel.

## Results

- **2D benchmark** (analytic two-wavefront collision with a velocity jump, eqs. 11-12; $N=50$ Latin hypercube samples, 5x20 and 5x5 networks): Table 1 (RMSE of $T$ in ms, MAE of $V$ in m/s), noise-free: PINN $T$ 0.49, $V$ 3.56; plain network 0.48, 9.07; GP 1.56, 57.78; linear 2.05, 17.98. At 1% noise PINN $V$ error is 10.24 against 63.93 (network), 54.08 (GP), 27.37 (linear). PINN wins except $T$ at 5% noise, where GP is marginally better (3.34 vs 3.42). Smooth methods cannot represent the gradient kink at a collision, giving infinite $V$ (p. 5).
- **Ensemble size**: error reduction slows beyond about 30 networks; 30 chosen. Training 30 in parallel costs 1.75x one network (p. 9). Regions of high entropy coincide with high error (Fig. 5).
- **Active vs Latin hypercube** (benchmark): lower error at all budgets, $p<10^{-7}$ for $T$ and $p<0.015$ for $V$ (p. 7).
- **Left atrium** (MICCAI mesh; monodomain + Fenton-Karma simulation; homogeneous and half-reduced conductivity): at 1.05 samples/cm$^2$ PINN median error 1.53 ms vs 3.92 ms linear (homogeneous), 2.23 vs 4.77 ms (heterogeneous), $p<10^{-5}$ (p. 8). Active learning from 10 samples matches linear interpolation's optimal-density error with only about 0.20-0.24 samples/cm$^2$, and beats random selection ($p<0.002$) (p. 8).
- About 1 min of training per sample on an 8-core laptop was enough (p. 9).

## Limitations

As stated (§4, pp. 10-11): isotropic conduction assumed (anisotropic Eikonal possible); electrode noise not modelled; uncertainty uses Euclidean not geodesic distance on the surface; only synthetic data tested; expected to fail for localized re-entry or fibrillation where the Eikonal equation does not hold. Conduction-velocity error stays high, partly from artefacts of the simulated reference where wavefronts collide (p. 8).

## Connections

- Same PINN family as [[PINNs (Raissi 2019)]], here with a first-order nonlinear PDE and two coupled networks; an inverse problem (infer $V$ from $T$) like [[Hidden fluid mechanics (Raissi 2020)]].
- Compared against [[Gaussian process]] regression (squared-exponential ARD kernel).
- Wiki note: the entropy criterion is the posterior-entropy form of the loop in [[Active learning]]; here the posterior comes from an ensemble instead of a GP. The MSE-as-Gaussian-likelihood and L2-as-prior reading matches [[Physics-informed prior]] and [[PINN]].
- Companion: [[Cardiovascular flow PINNs (Kissas 2020)]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Glorot init (Glorot 2010)]], [[PINNs (Raissi 2019)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[PIFT (Alberts 2023)]], [[Respecting causality (Wang 2022)]], [[When and why PINNs fail (Wang 2022)]]
**Software cited**: [[software#NPEET|NPEET]], [[software#TensorFlow|TensorFlow]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[PINN]] · [[PINNs (Raissi 2019)]] · [[Eikonal equation]] · [[Randomized prior functions]] · [[Active learning]] · [[Latin hypercube sampling]]
- [[Gaussian process]] · [[Hidden fluid mechanics (Raissi 2020)]] · [[Cardiovascular flow PINNs (Kissas 2020)]]
