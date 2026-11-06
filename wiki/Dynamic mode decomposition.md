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

> Prediction with continuous-time frequencies $\omega_j=\log(\lambda_j)/\Delta t$:

$$
x(t) = \sum_j \phi_j\, e^{\omega_j t}\, b_j.
$$

> [!example] Flow past a cylinder
> 151 snapshots of a 449 by 199 field, rank $r=50$, 140 snapshots used for the fit; the remaining ones test the forecast (source: dynamics/ notebook).

## Notes
- DMD is an SVD/[[Proper orthogonal decomposition]] projection followed by a least-squares linear fit; the modes are not orthogonal, unlike POD modes.
- For nonlinear dynamics a linear fit is a Koopman-style approximation **[unverified]**; compare [[SINDy]], which fits a sparse nonlinear model instead.

**Wiki note**: the text writes $b=(\Lambda W)^{-1}\tilde x_1$; dimensionally and by the eigen-relation it should be $(W\Lambda)^{-1}\tilde x_1$ as in the algorithm list. The text also says data after step 100 are unused, but the notebook uses 140 snapshots. See [[ME697 DMD - Dynamic mode decomposition]].

**Sources**: `advanced-scientific-machine-learning/book/dynamics/`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 DMD - Dynamic mode decomposition]] · [[Proper orthogonal decomposition]] · [[Singular value decomposition]] · [[Principal component analysis]]
- [[SINDy]] · [[Neural ODE]]
