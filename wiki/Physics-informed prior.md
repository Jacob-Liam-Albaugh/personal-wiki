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

## Model-trust parameter β
- Can be inferred: Jeffreys prior in log-space (paper 1, Ex. 2), where it tracked model-form error.
- Fixed values used: $\beta=10^5$ (paper 1 Ex. 3), 50 (Ex. 4), 1000 (paper 2).
- Klein-Gordon case: prior $\phi\sim\mathcal N(S^{-1}q,\beta^{-1}S^{-1})$, with $S^{-1}$ the Green's function of $-\nabla^2+\alpha^2$ (eq. 20); posterior covariance → 0 as $\beta\to\infty$ (eq. 21).
- B-PINNs: $\sigma_r^2=n/(2\beta)$ (eq. 32); see [[PINN]].
- Choosing β: Alberts & Bilionis 2024 (arXiv:2401.14224) — cited, not read.

## Energies used
- 1D heat / Dirichlet energy (paper 1, eq. 34); $E(u;k)=\int\frac{k(u)}2u_y^2\,dy$ for $\partial_y(k(u)\partial_yu)=0$ (paper 2, eq. 2).
- Klein-Gordon: $U=\frac12[(\nabla\phi)^\dagger\nabla\phi+\alpha^2\phi^\dagger\phi]-q^\dagger\phi$.
- Wiki note: using the energy whose minimiser is the PDE solution is the Dirichlet principle; neither paper names it.
- The Dirichlet energy $E[u]=\int[\tfrac k2|\nabla u|^2-fu]$ with its first-variation proof appears in [[Energy functional]] (source: pinns/basics/energy.ipynb). This is the link the earlier note on the book's energy notebook asked for.

## Where it appears
- [[PIFT (Alberts 2023)]] — defines it.
- [[IFT thermal conductivity (Alberts 2026)]] — Dirichlet energy of steady heat conduction.
- [[Physics-informed machine learning]] — the same physics-as-prior idea at the level of loss functions; [[Physics-informed ML review (Karniadakis 2021)]], p. 7: soft-penalty PINN equals MAP with a physics-based likelihood.
- [[ME697 5.1 - PINN basics]], [[ME697 IFT.3 - Physics-informed information field theory]].

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`, `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]] · [[Nested SGLD]]
