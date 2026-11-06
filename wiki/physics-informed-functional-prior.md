---
type: definition
area: ift
areas: [ift, physics-informed]
tags: [lab]
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
- Link to B-PINNs: $\sigma_r^2=n/(2\beta)$ (eq. 32); see [[pinn]].
- Choosing β: Alberts & Bilionis 2024 (arXiv:2401.14224) — cited, not read.

## Energies used
- 1D heat / Dirichlet energy (paper 1, eq. 34); $E(u;k)=\int\frac{k(u)}2u_y^2\,dy$ for $\partial_y(k(u)\partial_yu)=0$ (paper 2, eq. 2).
- Klein-Gordon: $U=\frac12[(\nabla\phi)^\dagger\nabla\phi+\alpha^2\phi^\dagger\phi]-q^\dagger\phi$.
- Wiki note: using the energy whose minimiser is the PDE solution is the Dirichlet principle; neither paper names it.

## Where it appears
- [[alberts-2023-pift]] — defines it.
- [[alberts-2026-ift-thermal-conductivity]] — Dirichlet energy of steady heat conduction.

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`, `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[information-field-theory]] · [[nested-sgld]]
