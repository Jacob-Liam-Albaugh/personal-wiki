---
type: method
area: operators
areas: [operators, ml]
source-ref: "Li et al. 2021, eqs. 2, 4-5, Def. 3, p. 5"
tags: [operators, ml]
---

# Fourier neural operator (FNO)

> [!algorithm] Fourier layer (Li et al. 2021, eqs. 2, 4-5, p. 5)
> $$v_{t+1}(x)=\sigma\big(Wv_t(x)+(\mathcal K(\phi)v_t)(x)\big)$$
> $$(\mathcal K(\phi)v_t)(x)=\mathcal F^{-1}\big(R_\phi\cdot(\mathcal Fv_t)\big)(x)$$
> $$(R\cdot\mathcal Fv_t)_{k,l}=\sum_jR_{k,l,j}\,(\mathcal Fv_t)_{k,j}$$
> Only the lowest $k_{\max}$ modes are kept. $R\in\mathbb C^{k_{\max}\times d_v\times d_v}$, with $R(-k)=R^*(k)$ so outputs are real.
>
> (source: `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, p. 5)

**Intuition**: a [[Kernel integral operator]] with a translation-invariant kernel $\kappa(x-y)$ is a convolution, which is diagonal in Fourier space. Learn the diagonal directly and truncate it. The local term $W$ restores high frequencies and non-periodic boundary behaviour (p. 9).

## Practicalities
- With the FFT the cost is $O(n\log n)$; the FFT needs a uniform grid.
- Defaults: $k_{\max}=16$ in 1-D, $12$ in 2-D; 4 Fourier layers.
- Hyperparameters in the review's notation: width $d_c$, cutoff $k_{\max}$, depth $L$ (source: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, §3.3, pp. 8-9).
- Universality follows from the averaging-operator result, because the zero mode makes a constant kernel available (review Cor. 4.6, p. 15). See [[Universal approximation for operators]].

## Benchmarks (relative $L^2$ error)
| Problem | FNO | Next best | Source |
|---|---|---|---|
| [[Burgers equation]], $\nu=0.1$, $s=256$-$8192$ | 0.0139-0.0160 | low-rank NO 0.0189-0.0221 | Li et al. 2021, Table 3, p. 15 |
| [[Burgers equation]] (JMLR retune) | 0.0018-0.0020 | | Kovachki et al. 2022 |
| [[Darcy flow]] | 0.0098-0.0109 | DeepONet 0.046-0.049 | Kovachki et al. 2022, Table 2 |
| [[Navier-Stokes equations]], $\nu=10^{-3}$, $N=200$ | 0.0098 (FNO-3D, $s=64$) | | Kovachki et al. 2022, Table 5 |

> [!warning] Name clash
> In the FNO and Neural Operator papers "LNO" means the **low-rank** neural operator, not the [[LNO]].

The JMLR Burgers numbers are about 8× lower than the ICLR ones. The JMLR run drops batch norm and is retuned; the paper gives no other reason (Wiki note). Train-coarse, test-fine results are on [[Discretization invariance#Zero-shot super-resolution|zero-shot super-resolution]].

## Where it appears
- [[FNO (Li 2021)]]: introduces it.
- [[Neural operator (Kovachki 2022)]]: one of four [[Neural operator]] parametrizations, the best in nearly all tests.
- [[LNO (Cao 2023)]]: the 4-layer baseline that LNO beats with one Laplace layer.
- [[Operator learning review (Kovachki 2024)]]: a nonlinear-manifold architecture.
- Assigned reading and Burgers JAX tutorial link in [[ME697 3.2 - Operator learning]] (source: `hup/op/01_reading.md`, `03_fno.ipynb`). Translation-equivariant convolution in Fourier space, compared with group symmetries in [[ME697 2.6 - Symmetries]].

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural operator]] · [[LNO]] · [[DeepONet]] · [[Operator learning]]
