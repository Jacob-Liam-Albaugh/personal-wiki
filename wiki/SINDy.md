---
type: method
area: physics-informed
areas: [physics-informed, ml]
source-ref: "Champion et al. 2019, §2.1; Bakarji et al. 2022, §2"
tags: [physics-informed, optimization, ml]
---

# SINDy

> [!definition] Sparse identification of nonlinear dynamics (SINDy)
> From snapshots $X$ and derivatives $\dot X$, pick a library $\Theta(X)=[\theta_1(X)\cdots\theta_p(X)]$ of candidate functions and solve
> $$\dot X=\Theta(X)\,\Xi$$
> for a sparse coefficient matrix $\Xi$. Typically solved by sequentially thresholded least squares, a proxy for
> $$\min_\Xi\ \|\dot X-\Theta\,\Xi\|_2^2+\lambda\|\Xi\|_0.$$
>
> (source: SINDy autoencoders.pdf, §2.1, p. 3; delay autoencoders.pdf, eq. 6)

**Intuition**: most physical equations have few terms. Regress the time derivative on a large dictionary (polynomials, trig terms) and keep only the terms that matter. Because the problem is a linear regression it is cheap and gives a closed-form, interpretable model, unlike the weights of a [[Neural ODE]]. The original method is Brunton, Proctor, Kutz 2016 (PNAS), cited in both papers but not in this folder.

## Practical points
- Needs $m\gg p$ samples and good conditioning (sample transients and several initial conditions) (source: [[SINDy autoencoders (Champion 2019)]], p. 3).
- Needs derivative estimates; noisy data is a weakness. Remedies cited: total-variation regularized derivatives, integral/weak SINDy, discrete-time fits.
- Can include partial physics: symmetries, constraints, conservation laws; extends to PDEs, parametric, switching and rational-function models (p. 4).
- $\ell_1$ ([[LASSO]]) is the convex relaxation of $\ell_0$.
- Works only if the measured coordinates make the dynamics sparse; this motivates learned coordinates.

## Variants in this wiki
- **SINDy autoencoder**: learns coordinates $z=\phi(x)$ and $\Xi$ jointly ([[SINDy autoencoders (Champion 2019)]]).
- **Delay SINDy autoencoder**: coordinates learned from a time-delay (Hankel) embedding of a partial measurement ([[SINDy delay autoencoders (Bakarji 2022)]]).
- Second-order version for mechanical systems: library in $z,\dot z$ predicts $\ddot z$.

## Failure modes
- Library misspecification: no sparse model exists if needed terms are absent (e.g. non-local closures need extra terms).
- Chaotic systems: long forecasts diverge even for a correct model.
- Non-unique coordinates: discovered equations can differ from the textbook ones by a transformation.

## Where it appears
- Both SINDy papers above; also as the "parsimonious model discovery" branch of [[Physics-informed machine learning]] (alongside [[Symbolic regression]]).
- ME 697 `inverse/data` replicates Brunton et al. (2016): fifth-degree polynomial library with `LassoCV` for 2D linear, 2D cubic and 3D linear systems (`02_sindy_1.ipynb`), and the Lorenz system with sequentially thresholded least squares, threshold 0.025, because `LassoCV` failed even after scaling (`03_sindy_2.ipynb`). The learned Lorenz trajectories diverge (chaos) but the attractor matches, also with noise $\eta=10$ on the derivatives. See SINDy and [[LASSO]].

## Examples

> [!example] Homework 7, problems 1-2 (source: homework/07_homework.ipynb)
> Partially observed Lorenz: SINDy fails on the observed coordinate alone; build a Hankel matrix, take its SVD to three dimensions, run degree-5 SINDy on the principal components. Then SINDy on noisy data with derivatives from the `derivative` package.

**Covered in**: ASML book inverse/data (ME 697 4.7); homework 7
**Sources**: `papers/Physics Informed Architectures/Brunton, Champion, Lusch, Kutz - SINDy - Data-Driven Discovery of Coordinates and Governing Equations.pdf`, `Brunton, Bakarji, Champion, Kutz -SINDy - Discovering Governing Equations Deep Delay Autoencoders.pdf`, `text_books/advanced-scientific-machine-learning/book/inverse/data/intro.md`, `01_lasso.ipynb`, `02_sindy_1.ipynb`, `03_sindy_2.ipynb`, `04_nodes.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SINDy autoencoders (Champion 2019)]] · [[SINDy delay autoencoders (Bakarji 2022)]] · [[Neural ODE]] · [[LASSO]]
- [[Symbolic regression]] · [[Dynamic mode decomposition]] · [[Singular value decomposition]] · [[Physics-informed machine learning]]
- [[Dynamic mode decomposition]] (linear least-squares counterpart).
