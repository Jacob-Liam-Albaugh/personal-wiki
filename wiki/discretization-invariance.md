---
type: definition
area: operators
source-ref: "Kovachki et al. 2022, Defs. 1-4, pp. 8-9; Thm 8, p. 48"
---

# Discretization invariance

> [!definition] Discretization invariance (Kovachki et al. 2022, Defs. 1-4, pp. 8-9)
> A discrete refinement of $D$ is a nested sequence $D_1\subset D_2\subset\dots\subset D$ with $|D_L|=L$, such that for every $\varepsilon>0$ some $D_L$ is an $\varepsilon$-net of $D$. For a compact $K\subset\mathcal A$ define the discretized uniform risk
> $$R_K(\mathcal G,\hat{\mathcal G},D_L)=\sup_{a\in K}\big\|\hat{\mathcal G}(D_L,a|_{D_L})-\mathcal G(a)\big\|_{\mathcal U}$$
> $\mathcal G(\cdot,\theta)$ is discretization invariant if there are maps $\hat{\mathcal G}_L$ on $L$-point data with
> $$\lim_{L\to\infty}R_K\big(\mathcal G(\cdot,\theta),\hat{\mathcal G}_L(\cdot,\cdot,\theta),D_L\big)=0$$
> for every $\theta$ and every compact $K$.
>
> (source: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, pp. 8-9)

**Intuition**: one set of weights, any mesh. The model takes a point cloud of any size, can be queried anywhere, and its output converges as the mesh is refined. The total error then splits into a discretization part and an approximation part (p. 12).

> [!theorem] Theorem 8 (Kovachki et al. 2022, p. 48)
> The neural operator class $\mathsf{NO}_n(\sigma_1,\sigma_2,\sigma_3)$ with continuous activations is discretization invariant.

Sensor-based [[deeponet]] is not: its branch net is tied to fixed sensors (Prop. 5). The review lists BelNet and VIDON as discretization-invariant DeepONet encoders (source: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, p. 13). Cao et al. assert the property for LNO but do not test it (LNO §2, p. 3).

## Zero-shot super-resolution
Train on a coarse grid and evaluate the same weights on a finer one.
- FNO-3D trained at 64×64×20 and evaluated at 256×256×80 on Navier-Stokes with $\nu=10^{-4}$ (source: `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, Fig. 1, p. 9).
- In Table 5 of the JMLR paper ($\nu=10^{-3}$, $N=200$), FNO-3D errors are 0.0098, 0.0101 and 0.0106 at $s=64,128,256$.
- GNO trained on 16×16 Darcy and tested on 241×241 (§7.2.3).

The error stays roughly flat with resolution. That is evidence of invariance, not a proof that fine-scale features absent from training are recovered (Wiki note).

## Where it appears
- [[kovachki-2022-neural-operator]]: the definition and Thm 8.
- [[li-2021-fno]]: flat error across resolutions (Tables 3-4) and super-resolution.
- [[cao-2023-lno]], [[kovachki-2024-operator-learning-review]] (Figs. 1-2).

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[neural-operator]] · [[fourier-neural-operator]] · [[operator-learning]]
