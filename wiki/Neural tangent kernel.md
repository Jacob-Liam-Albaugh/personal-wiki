---
type: concept
area: physics-informed
areas: [physics-informed, ml, optimization]
source-ref: "Wang, Yu, Perdikaris (arXiv:2007.14527), §2-§5; Jacot et al. via that paper"
tags: [ml, optimization, physics-informed, gp]
---

# Neural tangent kernel

**Summary**: The kernel of parameter gradients of a network. In the infinite-width limit it is deterministic and constant during gradient-descent training, so training reduces to kernel regression and its spectrum sets how fast each error mode decays.

## Definition

For a network $f(x,\theta)$ trained at time $t$ (source: NTK.pdf, eq. 2.6, p. 3):
$$\mathrm{Ker}_t(x,x')=\Big\langle\tfrac{\partial f(x,\theta(t))}{\partial\theta},\tfrac{\partial f(x',\theta(t))}{\partial\theta}\Big\rangle.$$
With NTK parameterization (weights $N(0,1)$, layers scaled by $1/\sqrt{d_h}$) and width $\to\infty$, $\mathrm{Ker}_0\to\Theta^{(L)}$, a deterministic kernel defined recursively from the Gaussian-process covariances $\Sigma^{(h)}$ (eqs. 2.4-2.8, p. 3). Jacot et al. show the kernel stays $\Theta^{(L)}$ for $0\le t\le T$, so a wide network trained by gradient descent equals kernel regression with a fixed kernel (p. 3). The original paper is now ingested: [[NTK (Jacot 2018)]] (Prop. 1, Thms 1-2, §5), which gives the recursion $\Theta^{(L+1)}_\infty=\Theta^{(L)}_\infty\dot\Sigma^{(L+1)}+\Sigma^{(L+1)}$ and the function-space dynamics $f_t=f^*+e^{-t\Pi}(f_0-f^*)$ (pp. 5-7). Its $\Sigma^{(L)}$ is the [[Neural network Gaussian process]] kernel.

## Why the spectrum matters

Under gradient flow with a constant kernel $K=Q^T\Lambda Q$ (eq. 5.3, p. 7):
$$Q\,(\text{error}(t))\approx -e^{-\Lambda t}\,Q\,(\text{target}).$$
Mode $i$ decays like $e^{-\lambda_i t}$. Eigenvectors with large eigenvalues are low frequency, so high frequencies are learned slowly: the [[Spectral bias]] mechanism (p. 8). Stable step size needs $\eta\le 2/\lambda_{\max}$ (p. 9).

## NTK of a PINN

For a [[PINN]] the Jacobian stacks rows for the solution at boundary points and for the PDE residual $\mathcal Lu$ at collocation points. The kernel becomes a block matrix
$$K=\begin{bmatrix}K_{uu}&K_{ur}\\K_{ru}&K_{rr}\end{bmatrix}=JJ^T.$$
Each block has its own spectrum, and an unbalanced pair gives different convergence rates for boundary and residual terms (eqs. 3.8-3.9, Def. 5.1). The average rate is $\mathrm{Tr}(K)/n$. Weighting each loss term by $\mathrm{Tr}(K)/\mathrm{Tr}(K_{\text{block}})$ equalizes them (eqs. 6.5-6.6, p. 10). Details: [[When and why PINNs fail (Wang 2022)]].

## Caveats

- Proofs cover one hidden layer and linear model problems; the kernel visibly moves for the wave equation (pp. 6, 14).
- The PINN NTK is reported as degenerate, with most eigenvalues near zero (Fig. 2c, p. 7).
- Wiki note: the constant-kernel regime is the "lazy" regime; feature learning is outside it. This is general background, **[unverified]** against these sources.

**Sources**: `papers/ML/Jacot, Gabriel, Hongler - Neural Tangent Kernel Convergence and Generalization in Neural Networks.pdf`, `papers/Physics Informed Architectures/Wang, Yu, Perdikaris - When and Why PINNs Fail to Train - A Neural Tangent Kernel Perspective.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[NTK (Jacot 2018)]] · [[Neural network Gaussian process]] · [[When and why PINNs fail (Wang 2022)]] · [[PINN]] · [[Spectral bias]] · [[Kernel methods]] · [[RKHS]]
- [[Gaussian process]] · [[Gradient descent]] · [[Weight initialization]] · [[Physics-informed machine learning]]
- [[Fourier features]] (eigenmode convergence e^{-eta lambda t}, Tancik 2020) and [[Spectral bias]].
