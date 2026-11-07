---
type: definition
area: ift
areas: [ift, physics-informed]
tags: [ift, physics-informed, bayesian]
source-ref: "Alberts & Bilionis 2023, eqs. 12-15, 20-21, pp. 6-10"
---

# Physics-informed functional prior

> [!definition] Boltzmann prior over fields (Alberts & Bilionis 2023, eqs. 12-15)
> For a PDE $D[\phi]=f$, take an energy $U[\phi]=\int u(x,\phi,\nabla\phi,\dots)\,dx$ (a variational energy), or the residual energy $U[\phi]=\int(D[\phi]-f)^2dx$ (eq. 14), and set
> $$p(\phi)\propto e^{-\beta U[\phi]}$$
> optionally times $e^{-\frac12\phi^\dagger S\phi}$.

**Intuition**: $\beta$ is how much you trust the model. $\beta\to\infty$ pins the field to a PDE solution; small $\beta$ gives a broad prior that lets data correct model-form error.

The book's ift/physics takeaway is that the smoothing problem can be posed by a prior over the space of state functions biased by the physics; this is the field-level version of smoothing in [[Stochastic state-space model]]. For a residual $r[u]$ and weight $\lambda$ the squared-residual choice penalizes violation of the governing equation:

$$
p[u] \propto \exp\Big(-\tfrac{\lambda}{2}\,\|r[u]\|^2\Big).
$$

A [[PINN]] is the MAP estimate under this prior (Wiki note).

## Model-trust parameter β
- Uniqueness of the inferred β: with a flat prior and enough data the MAP is unique; for Poisson, $\beta^*=\infty$ iff the model is exact, otherwise finite and larger for better models ([[MAP uniqueness in IFT (Alberts 2025)]], Thm. 3.3, eq. 4.4).
- Can be inferred: Jeffreys prior in log-space (paper 1, Ex. 2), where it tracked model-form error.
- Fixed values used: $\beta=10^5$ (paper 1 Ex. 3), 50 (Ex. 4), 1000 (paper 2).
- Klein-Gordon case: prior $\phi\sim\mathcal N(S^{-1}q,\beta^{-1}S^{-1})$, with $S^{-1}$ the Green's function of $-\nabla^2+\alpha^2$ (eq. 20); posterior covariance → 0 as $\beta\to\infty$ (eq. 21).
- B-PINNs: $\sigma_r^2=n/(2\beta)$ (eq. 32); see [[PINN]].
- Choosing β: Alberts & Bilionis 2024 (arXiv:2401.14224); treated in [[MAP uniqueness in IFT (Alberts 2025)]] and [[Model-form error detection]]. The dissertation calls $\beta$ the "trust", proves $U=\tfrac12\phi^\dagger S\phi-q^\dagger\phi$ for Klein-Gordon step by step (p. 53), and notes the partition function diverges unless the field is truncated at the smallest physical scale (p. 55) (source: dissertation).

## Energies used
- 1D heat / Dirichlet energy (paper 1, eq. 34); $E(u;k)=\int\frac{k(u)}2u_y^2\,dy$ for $\partial_y(k(u)\partial_yu)=0$ (paper 2, eq. 2).
- Klein-Gordon: $U=\frac12[(\nabla\phi)^\dagger\nabla\phi+\alpha^2\phi^\dagger\phi]-q^\dagger\phi$.
- Wiki note: using the energy whose minimiser is the PDE solution is the Dirichlet principle; neither paper names it.
- The Dirichlet energy $E[u]=\int[\tfrac k2|\nabla u|^2-fu]$ with its first-variation proof appears in [[Energy functional]] (source: pinns/basics/energy.ipynb). This is the link the earlier note on the book's energy notebook asked for.

## Where it appears
- [[PIFT (Alberts 2023)]] — defines it.
- [[IFT thermal conductivity (Alberts 2026)]] — Dirichlet energy of steady heat conduction.
- [[IFT for engineering inverse problems (Alberts 2024)]] — Ch. 3 construction and Example 2 energies (cubic nonlinear ODE, pp. 105-107; Allen-Cahn, p. 114).
- [[Physics-informed machine learning]] — the same physics-as-prior idea at the level of loss functions; [[Physics-informed ML review (Karniadakis 2021)]], p. 7: soft-penalty PINN equals MAP with a physics-based likelihood.
- [[PINN]].

**Covered in**: ASML book ift/physics (ME 697 IFT.3)
**Sources**: `papers/IFT/Bilionis, Alberts - IFT.pdf`, `papers/IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`, `text_books/advanced-scientific-machine-learning/book/ift/intro.md`, `ift/physics/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[MAP uniqueness in IFT (Alberts 2025)]]
- [[IFT for engineering inverse problems (Alberts 2024)]] · [[Model-form error detection]]
- [[Information field theory]] · [[Nested SGLD]]
