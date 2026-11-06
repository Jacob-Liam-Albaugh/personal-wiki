---
type: concept
area: operators
areas: [operators, physics-informed]
source-ref: "Li et al. 2021, eq. 6, p. 6"
---

# Burgers' equation (benchmark)

**Summary**: 1-D viscous Burgers, the simplest nonlinear advection-diffusion PDE. In operator learning the benchmark map is $u_0\mapsto u(\cdot,1)$.

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

> [!definition] Benchmark setup (Li et al. 2021, eq. 6, p. 6)
> $$\partial_tu+\partial_x(u^2/2)=\nu\,\partial_{xx}u,\quad x\in(0,1),\ t\in(0,1]$$
> Periodic boundary, $\nu=0.1$.
> $$u_0\sim\mathcal N\big(0,625(-\Delta+25I)^{-2}\big)$$
> The data come from a solve on an 8192-point grid. Kovachki et al. use the domain $(0,2\pi)$.

## Results (relative $L^2$, $s=256$ to $8192$)
| Model | Error | Source |
|---|---|---|
| [[fourier-neural-operator]] | 0.0139-0.0160 | Li et al. 2021, Table 3, p. 15 |
| low-rank NO | 0.0189-0.0221 | same |
| PCANN ([[pca-net]]) | 0.0383-0.0398 | same |
| FNO, JMLR retune | 0.0018-0.0020 | Kovachki et al. 2022 |
| [[deeponet]] | 0.0569-0.0857 | Kovachki et al. 2022 |

The FNO error is flat in $s$, which is evidence of [[discretization-invariance]].

## Where it appears
- [[li-2021-fno]], [[kovachki-2022-neural-operator]].

## Related pages
- [[darcy-flow]] · [[navier-stokes-equations]] · [[operator-learning]]
