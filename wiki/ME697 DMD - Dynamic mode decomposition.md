---
type: lecture
area: me697
areas: [me697, physics-informed]
course: me697
lecture: dynamics
source-ref: "ME 697 book, dynamics 00_intro, 04_dmd, 05_dmd_example (follows Brunton and Kutz, Data-Driven Science and Engineering, ch. 7.2)"
tags: [signals, ml, physics-informed, pde]
---

# ME697 DMD - Dynamic mode decomposition

**Summary**: DMD fits a best-fit linear operator to snapshot pairs, then diagonalizes it in the POD basis to get spatial modes, growth rates and frequencies. The notebook derives the algorithm in four steps and reproduces flow past a cylinder at Reynolds number 100.
**File**: `advanced-scientific-machine-learning/book/dynamics/` (`00_intro.md`, `04_dmd.ipynb`, `05_dmd_example.ipynb`). Not in `_toc.yml`.

---

## Topics
- `00_intro.md` lists the folder objectives: sparse regression (LASSO) and SINDy. The folder has only the DMD notebooks; see [[SINDy]] for the other objective.
- DMD combines POD in space with Fourier analysis in time. Pros: data-driven, only linear algebra, interpretable, predictive, handles control, backbone of Koopman methods. Cons: linear, trouble with traveling waves and transients, noise-sensitive, needs much data (source: 04_dmd.ipynb).
- Uses [[Singular value decomposition]] and [[ME697 ROM - SVD, PCA and POD]].

## Key results
Snapshots $x_k\in\mathbb R^n$ at equal steps $\Delta t$. Stack

$$
X = [x_1,\dots,x_m],
\qquad
X' = [x_2,\dots,x_{m+1}].
$$

Find $A$ with $X'=AX$ by least squares in the Frobenius norm:

$$
A = X' X^{\dagger}.
$$

See [[Dynamic mode decomposition]] for the algorithm. In brief:

1. Truncated SVD $X\approx \tilde U\tilde\Sigma\tilde V^T$ (rank $r$).
2. Reduced operator, size $r\times r$:

$$
\tilde A = \tilde U^T X'\tilde V\tilde\Sigma^{-1}.
$$

3. Eigenproblem $\tilde A W = W\Lambda$.
4. DMD modes (never forming the $n\times n$ matrix $A$):

$$
\Phi = X'\tilde V\tilde\Sigma^{-1}W.
$$

Then $A\Phi=\Phi\Lambda$. Prediction:

$$
x_k = \Phi\Lambda^k b,
\qquad
b = (W\Lambda)^{-1}\tilde x_1,
$$

where $\tilde x_1=\tilde U^T x_1$. In continuous time, $\lambda_j=e^{\omega_j\Delta t}$:

$$
x(t) = \sum_{j=1}^{r}\phi_j\,e^{\omega_j t}\,b_j.
$$

## Examples
> [!example] Cylinder wake, Re = 100 (05_dmd_example.ipynb)
> Replicates Fig. 7.3 of Brunton and Kutz, data from dmdbook.com (`CYLINDER_ALL.mat`). 151 snapshots of size $449\times199$; the vorticity $\omega=\partial_x v-\partial_y u$ is used, which satisfies incompressibility automatically. Vorticity clipped at $\pm10$, cylinder masked.
> - $X$ uses 140 snapshots, rank $r=50$.
> - Modes are complex; real and imaginary parts are plotted.
> - Eigenvalues on the unit circle are oscillatory, inside the circle decaying.
> - Amplitudes evolve as $b_j(t)=e^{\omega_j t}b_j$ with $\omega_j=\log\lambda_j/\Delta t$.
> - Reconstruction and extrapolation are compared with held-out snapshots.

> [!example] Homework 7
> The Hankel-matrix problem (partially observed Lorenz) uses SVD and then SINDy on the principal components, see [[ME697 7 - Homework]]. The Hankel matrix is also the input of time-delay DMD.

## Connections
- [[Proper orthogonal decomposition]] supplies the spatial basis; DMD adds the time dynamics.
- [[SINDy]] fits nonlinear dynamics; DMD is its linear counterpart. See also [[SINDy delay autoencoders (Bakarji 2022)]] for Hankel embeddings.
- Neural alternatives: [[Neural ODE]].

**Wiki note (book errors)**:
- 04_dmd: the amplitude formula is written $b=(\Lambda W)^{-1}\tilde x_1$. From $\tilde x_1=W\Lambda b$ it should be $(W\Lambda)^{-1}$, which is what the code in 05 uses.
- 05: the text says data after step 100 were not used, but the code builds $X$ from 140 snapshots, so only the last ten or so are held out **[unverified: read from source cells]**.

**Sources**: `advanced-scientific-machine-learning/book/dynamics/00_intro.md`, `dynamics/04_dmd.ipynb`, `dynamics/05_dmd_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dynamic mode decomposition]] · [[Proper orthogonal decomposition]] · [[Singular value decomposition]] · [[Principal component analysis]] · [[SINDy]]
- [[ME697 ROM - SVD, PCA and POD]] · [[ME697 7 - Homework]]
