---
type: method
area: me697
areas: [me697, mechanics]
source-ref: "ME 697 book, dynamics/ (DMD notebook and text)"
tags: [ml, signals, optimization]
---

# Dynamic mode decomposition

Data-driven fit of a linear operator $A$ to snapshot pairs, then an eigen-decomposition that gives spatial modes with a growth rate and frequency each.

> [!definition] Snapshot matrices
> Columns are states at consecutive times, $x_{k+1}\approx A x_k$:

$$
X = [x_1,\dots,x_{m-1}],
\qquad
X' = [x_2,\dots,x_m].
$$

$$
A = X' X^{+}.
$$

> [!algorithm] Reduced-rank DMD (source: dynamics/)
> 1. Truncated [[Singular value decomposition]] of $X$ at rank $r$: $X\approx \tilde U\tilde\Sigma\tilde V^T$.
> 2. Reduced operator:

$$
\tilde A = \tilde U^T X' \tilde V \tilde\Sigma^{-1}.
$$

> 3. Eigen-decomposition $\tilde A W = W\Lambda$.
> 4. Modes (exact DMD) and amplitudes:

$$
\Phi = X' \tilde V \tilde\Sigma^{-1} W,
\qquad
b = (W\Lambda)^{-1}\tilde x_1.
$$

> Prediction in discrete time:

$$
x_k = \Phi\Lambda^k b,
\qquad
b = (W\Lambda)^{-1}\tilde x_1,
$$

> Prediction with continuous-time frequencies $\omega_j=\log(\lambda_j)/\Delta t$:

$$
x(t) = \sum_j \phi_j\, e^{\omega_j t}\, b_j.
$$

> [!example] Cylinder wake, Re = 100 (05_dmd_example.ipynb)
> Replicates Fig. 7.3 of Brunton and Kutz, data from dmdbook.com (`CYLINDER_ALL.mat`). 151 snapshots of size $449\times199$; the vorticity $\omega=\partial_x v-\partial_y u$ is used, which satisfies incompressibility automatically. Vorticity clipped at $\pm10$, cylinder masked.
> - $X$ uses 140 snapshots, rank $r=50$; the remaining ones test the forecast.
> - Modes are complex; real and imaginary parts are plotted.
> - Eigenvalues on the unit circle are oscillatory, inside the circle decaying.
> - Amplitudes evolve as $b_j(t)=e^{\omega_j t}b_j$ with $\omega_j=\log\lambda_j/\Delta t$.
> - Reconstruction and extrapolation are compared with held-out snapshots.

## Notes
- DMD is an SVD/[[Proper orthogonal decomposition]] projection followed by a least-squares linear fit; the modes are not orthogonal, unlike POD modes.
- For nonlinear dynamics a linear fit is a Koopman-style approximation **[unverified]**; compare [[SINDy]], which fits a sparse nonlinear model instead.

**Wiki note**: the text writes $b=(\Lambda W)^{-1}\tilde x_1$; dimensionally and by the eigen-relation it should be $(W\Lambda)^{-1}\tilde x_1$ as in the algorithm list. The text also says data after step 100 are unused, but the notebook uses 140 snapshots.

**Covered in**: ASML book dynamics (ME 697 DMD); homework 7
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/dynamics/`, `courses/ME 697/advanced-scientific-machine-learning/book/dynamics/00_intro.md`, `dynamics/04_dmd.ipynb`, `dynamics/05_dmd_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Proper orthogonal decomposition]] · [[Singular value decomposition]] · [[Principal component analysis]]
- [[SINDy]] · [[Neural ODE]]
