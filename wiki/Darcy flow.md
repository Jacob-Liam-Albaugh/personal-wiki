---
type: concept
area: operators
areas: [operators, physics-informed]
source-ref: "Li et al. 2021, eq. 7, p. 6; Kovachki et al. 2022, §6.2"
tags: [pde, operators]
---

# Darcy flow (benchmark)

**Summary**: the steady elliptic PDE for flow through porous media. In operator learning the benchmark map is the permeability $a(x)$ to the pressure $u(x)$, which is nonlinear in $a$.

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

> [!definition] Benchmark setup (Li et al. 2021, eq. 7, p. 6)
> $$-\nabla\cdot(a(x)\nabla u(x))=f(x),\quad x\in(0,1)^2$$
> $$u=0\text{ on }\partial(0,1)^2,\qquad f\equiv1$$
> $$a\sim\psi_\#\mathcal N\big(0,(-\Delta+9I)^{-2}\big)$$
> $\psi$ maps positive values to 12 and negative to 3, so $a$ is piecewise constant. The data come from a 421×421 finite-difference solve.

## Results
| Model | Relative $L^2$ error | Source |
|---|---|---|
| [[FNO]] | 0.0098-0.0109 | Kovachki et al. 2022, Table 2 |
| [[DeepONet]] | 0.0462-0.0487 | Kovachki et al. 2022, Table 2 |

## Where it appears
- [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]].

## Related pages
- [[Operator learning]] · [[Burgers equation]] · [[Navier-Stokes equations]]
