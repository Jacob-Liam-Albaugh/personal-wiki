---
type: concept
area: operators
areas: [operators, physics-informed]
source-ref: "Li et al. 2021, eq. 8, p. 7; Kovachki et al. 2022, eqs. 43-46"
tags: [pde, operators]
---

# Navier-Stokes equations (2-D vorticity benchmark)

**Summary**: incompressible Navier-Stokes on the unit torus, in vorticity form. In operator learning the benchmark map is the vorticity on $[0,10]$ to the vorticity on $(10,T]$.

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

> [!definition] Benchmark setup (Li et al. 2021, eq. 8, p. 7)
> $$\partial_tw+u\cdot\nabla w=\nu\Delta w+f,\qquad\nabla\cdot u=0$$
> $$w_0\sim\mathcal N\big(0,7^{3/2}(-\Delta+49I)^{-2.5}\big)$$
> $$f=0.1\big(\sin2\pi(x_1+x_2)+\cos2\pi(x_1+x_2)\big)$$
> Kovachki et al. give $Re=\sqrt{0.1}/(\nu(2\pi)^{3/2})$: about 200 for $\nu=10^{-4}$ and 20 for $\nu=10^{-3}$. The energy spectrum decays as $k^{-5/3}$ (FNO App. A.2).

## Results
- FNO-3D at $\nu=10^{-3}$, $N=200$, $T=20$: errors 0.0098, 0.0101 and 0.0106 at $s=64,128,256$ (Kovachki et al. 2022, Table 5).
- The NS tables are identical in the ICLR and JMLR papers.
- Kovachki et al. also use NS for a Bayesian inverse problem: pCN sampling with an FNO surrogate, 7×7 observations, noise $\gamma=0.1$.

## Where it appears
- [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]].
- Turbulence priors: [[Generative priors for turbulence (Wang 2026)]] (Wiki note: a different flow setting).
- [[PINNs (Raissi 2019)]] — PINN on incompressible flow; [[NIF (Pan 2023)]] — neural implicit flow on flow-field data; [[Energy-based kernels for viscoelastic flow (Otto 2024)]].

## Related pages
- [[Darcy flow]] · [[Burgers equation]] · [[FNO]] · [[Discretization invariance]]
- [[Maxwell's equations]]: another classical PDE system (wiki note).
