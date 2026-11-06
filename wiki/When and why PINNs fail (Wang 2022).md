---
type: paper
area: physics-informed
areas: [physics-informed, pde, optimization]
source-ref: "Wang, Yu, Perdikaris, arXiv:2007.14527 (preprint dated 30 Jul 2020)"
tags: [physics-informed, pde, optimization, ml]
authors: ["[[Sifan Wang]]", "[[Xinling Yu]]", "[[Paris Perdikaris]]"]
year: 2022
venue: "arXiv:2007.14527; journal version Journal of Computational Physics 2022 [unverified]"
file: "Physics Informed Architectures/Wang, Yu, Perdikaris - When and Why PINNs Fail to Train - A Neural Tangent Kernel Perspective.pdf"
---

# When and why PINNs fail to train (Wang 2022)

**Summary**: Derives the [[Neural tangent kernel]] of a [[PINN]], shows that for a one-hidden-layer network it converges to a deterministic kernel that stays constant under gradient flow, and uses its eigenvalues to explain why the boundary and residual loss terms train at very different speeds. The fix is an NTK-based rule for the loss weights (Algorithm 1).

**Authors**: Sifan Wang, Xinling Yu, Paris Perdikaris · **Year**: 2022 (the PDF is the 30 Jul 2020 preprint; the year in the page name follows the later journal version, **[unverified]**)

---

## Setting

PDE on a domain $\Omega$ with Dirichlet data (source: NTK.pdf, eqs. 3.1-3.2, p. 4):
$$\mathcal L[u](x)=f(x),\ x\in\Omega$$
$$u(x)=g(x),\ x\in\partial\Omega$$
Time is treated as one more coordinate; initial conditions count as boundary data. The residual and composite loss (eqs. 3.3-3.6):
$$r(x,\theta)=\mathcal L u(x,\theta)-f(x)$$
$$L(\theta)=L_b(\theta)+L_r(\theta)$$
with $L_b=\tfrac12\sum_{i\le N_b}|u(x_b^i,\theta)-g(x_b^i)|^2$ and $L_r=\tfrac12\sum_{i\le N_r}|r(x_r^i,\theta)|^2$ (p. 4).

## Background: infinite-width networks (§2)

Networks use the NTK parameterization with $1/\sqrt{d_h}$ scaling and i.i.d. $N(0,1)$ weights (eqs. 2.1-2.3). As width grows the pre-activations become a Gaussian process with covariance $\Sigma^{(h)}$ (eq. 2.4), and the kernel of parameter gradients
$$\mathrm{Ker}_t(x,x')=\Big\langle\tfrac{\partial f(x,\theta(t))}{\partial\theta},\tfrac{\partial f(x',\theta(t))}{\partial\theta}\Big\rangle$$
converges to a deterministic $\Theta^{(L)}$ (eqs. 2.6-2.8, p. 3). Training then equals kernel regression (Jacot et al., cited as ref. 33). See [[Gaussian process]] and [[Kernel methods]].

## Results

1. **Training dynamics (Lemma 3.1, eq. 3.8, p. 4).** Under gradient flow $\dot\theta=-\nabla L$, the network outputs obey
$$\frac{d}{dt}\begin{bmatrix}u(x_b)\\ \mathcal Lu(x_r)\end{bmatrix}=-K(t)\begin{bmatrix}u(x_b)-g\\ \mathcal Lu(x_r)-f\end{bmatrix}$$
with blocks $K_{uu},K_{ur},K_{rr}$ built from parameter-gradient inner products (eq. 3.9). $K=JJ^T$ is positive semi-definite (Remark 3.3). The lemma holds for any operator and architecture (Remark 3.4, p. 5).
2. **PINN-GP correspondence (Thm 4.1, p. 5).** For $u_{xx}=f$ and one hidden layer of width $N\to\infty$, both $u$ and $u_{xx}$ converge in distribution to Gaussian processes at initialization. Remark 4.2 extends it to any linear PDE operator (p. 6).
3. **Deterministic kernel (Thm 4.3, p. 6).** $K(0)\to K^*$ in probability as $N\to\infty$; the explicit form is in Appendix C.
4. **Constant kernel (Thm 4.4, p. 6).** Under bounded parameters, bounded loss integrals and a smooth activation with bounded derivatives up to order 4, $\sup_{t\le T}\|K(t)-K(0)\|_2\to0$. Proof idea: parameters move little (Lemma D.2), so gradients barely change (p. 7).
5. **Kernel regression limit (eq. 4.10, p. 7).** If $K^*$ is invertible, the trained network equals a kernel regression. The authors report that in practice the PINN NTK is degenerate (Figs. 2c, 3c), so this is not usable directly.

Only one hidden layer and the Poisson problem $u_{xx}=f$ are proven; deeper networks and nonlinear PDEs are conjectured from experiments (p. 11).

## Spectral bias and the loss imbalance (§5)

With $K$ constant and $K(0)=Q^T\Lambda Q$, the error in eigen-direction $i$ decays as $e^{-\lambda_i t}$ (eq. 5.3, p. 7). Large eigenvalues go with low-frequency eigenvectors, and the PINN NTK spectrum decays fast (Fig. 1), so high-frequency components converge slowly: PINNs show [[Spectral bias]] (p. 8).

The trace splits across blocks:
$$\sum_i\lambda_i(t)=\mathrm{Tr}(K_{uu})+\mathrm{Tr}(K_{rr}).$$
Definition 5.1 (p. 8) gives the average convergence rate
$$c=\mathrm{Tr}(K)/n.$$
$K_1$ dominates $K_2$ if $c_1\gg c_2$. In the 1D Poisson example with $u=\sin(a\pi x)$, $K_{rr}$ dominates $K_{uu}$, so the residual converges much faster than the boundary fit. The authors call this discrepancy a key reason PINNs fail to train; they also note that for some problems $K_{uu}$ can dominate (p. 8).

## Algorithm 1: NTK-adaptive weights (§6, p. 10)

Weighted loss $L=\lambda_bL_b+\lambda_rL_r$. Stable gradient descent needs a learning rate $\le 2/\lambda_{\max}(\tilde K)$ (p. 9). Weights are set to equalize average rates:
$$\lambda_b=\frac{\mathrm{Tr}(K)}{\mathrm{Tr}(K_{uu})}\quad(\text{eq. 6.5})$$
$$\lambda_r=\frac{\mathrm{Tr}(K)}{\mathrm{Tr}(K_{rr})}\quad(\text{eq. 6.6})$$
Only traces are needed, not full eigendecompositions, and the update can run every few steps. Compared with the earlier gradient-statistics annealing rule of the same group (ref. 28), this one is theory-derived (p. 10). Wiki note: the later heuristic family is collected in [[Expert's guide to PINNs (Wang 2023)]].

## Experiments (§7)

| Case | Setup | Result |
|---|---|---|
| NTK convergence, 1D Poisson, $u=\sin\pi x$ | width 10/100/500, $N_b=N_r=100$, lr $10^{-5}$, 10,000 steps | relative change of weights and $K$ shrinks with width (Fig. 2); similar with 3 hidden layers (Fig. 3) (pp. 10-11) |
| 1D Poisson, $u=\sin4\pi x$ | width 100, 40,000 steps | rel. $L^2$ error $2.40\times10^{-1}$ with $\lambda_b=\lambda_r=1$; $1.63\times10^{-3}$ with $\lambda_b\approx100$ (Fig. 4, p. 13) |
| Same, sweep of $\lambda_b\in[1,500]$ | 10 trials | error minimum near $\lambda_b\approx100$, matching theory; larger values oscillate and raise variance (Fig. 5, p. 12) |
| 1D wave, $u_{tt}-4u_{xx}=0$ (eqs. 7.5-7.9) | 5 layers x 500, Adam, 80,000 steps, $N_u=N_{u_t}=N_r=300$ | standard PINN rel. $L^2$ $4.518\times10^{-1}$; Algorithm 1 gives $1.728\times10^{-3}$ (Fig. 6, p. 15) |

For the wave equation the NTK does not stay fixed: eigenvalues first move outward, then settle, with $K_r$ and $K_{u_t}$ dominating $K_u$. Weights update every 1,000 iterations (eqs. 7.13-7.15, p. 14), so the extra cost is negligible; $\lambda_u,\lambda_{u_t}$ grow quickly and $\lambda_r$ stays near 1 (Fig. 8a).

## Connections

- Base method: [[PINNs (Raissi 2019)]]; the failure analysis is complementary to [[Respecting causality (Wang 2022)]].
- High-frequency fixes in the wider literature: [[Fourier features]], [[SIREN]].
- Optimizers used: [[Gradient descent]], [[Adam]]. Matrix analysis is eigenvalue/[[Singular value decomposition]] based.
- Related frameworks: [[Physics-informed machine learning]], [[Physics-informed prior]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[DeepONet (Lu 2021)]], [[Fourier features (Tancik 2020)]], [[Glorot init (Glorot 2010)]], [[PINNs (Raissi 2019)]], [[Spectral bias (Rahaman 2019)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[Respecting causality (Wang 2022)]]
%% refs:end %%

**Sources**: `Physics Informed Architectures/Wang, Yu, Perdikaris - When and Why PINNs Fail to Train - A Neural Tangent Kernel Perspective.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural tangent kernel]] · [[PINN]] · [[PINNs (Raissi 2019)]] · [[Spectral bias]] · [[Gaussian process]]
- [[Respecting causality (Wang 2022)]] · [[Expert's guide to PINNs (Wang 2023)]] · [[Physics-informed machine learning]]
