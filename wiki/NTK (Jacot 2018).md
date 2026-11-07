---
type: paper
area: ml
areas: [ml, gp, optimization]
source-ref: "Jacot, Gabriel, Hongler 2018, NeurIPS, Prop. 1, Thms 1-2, §5"
tags: [ml, gp, optimization]
authors: ["[[Arthur Jacot]]", "[[Franck Gabriel]]", "[[Clément Hongler]]"]
year: 2018
venue: "NeurIPS 2018"
file: "papers/ML/Jacot, Gabriel, Hongler - Neural Tangent Kernel Convergence and Generalization in Neural Networks.pdf"
---

# NTK (Jacot 2018)

**Summary**: Shows that for fully connected networks in the infinite-width limit, gradient descent on the parameters is kernel gradient descent in function space with respect to the neural tangent kernel (NTK). The NTK is random at initialization and moving during training for finite width, but converges to a deterministic kernel that stays constant. For least-squares loss the network function then follows a linear ODE whose modes decay at rates given by the kernel eigenvalues, which motivates early stopping.

**Authors**: Arthur Jacot, Franck Gabriel, Clément Hongler · **Year**: 2018 · **File**: `papers/ML/Jacot, Gabriel, Hongler - Neural Tangent Kernel Convergence and Generalization in Neural Networks.pdf`

---

Page numbers are PDF pages. The PDF has 10 pages: the proofs are said to be in an appendix that is not included, so Prop. 1 and Thms 1-2 are reported here without proof.

## Problem

Networks can approximate any function with enough hidden units ([[Universal approximation (Hornik 1989)]], p. 1), but it is not known what training converges to: the parameter loss is non-convex. Overparametrized networks also generalize despite fitting random labels. At initialization, infinite-width networks are Gaussian processes ([[Wide networks as GPs (Matthews 2018)]]); the paper asks what describes the training dynamics (pp. 1-2).

## Method

**Setup** (§2, p. 3). Layers $0,\dots,L$ with widths $n_\ell$; parameters iid $N(0,1)$ and an explicit $1/\sqrt{n_\ell}$ scaling:
$$\tilde\alpha^{(\ell+1)}(x)=\tfrac{1}{\sqrt{n_\ell}}W^{(\ell)}\alpha^{(\ell)}(x)+\beta b^{(\ell)},\qquad \alpha^{(\ell)}=\sigma(\tilde\alpha^{(\ell)}).$$
Here $\beta$ balances the bias and weight learning rates. The paper's parametrization differs from the usual LeCun one, where $W_{ij}\sim N(0,1/n_\ell)$ and no $1/\sqrt{n_\ell}$ appears; the same functions are representable but the gradients are scaled (Remark 1). See [[Weight initialization]].

**Kernel gradient** (§3, pp. 3-4). A kernel $K$ defines a bilinear form $\langle f,g\rangle_K=\mathbb E_{x,x'\sim p_{in}}[f(x)^\top K(x,x')g(x')]$. For a cost $C$ depending on $f$ only at the data, the kernel gradient is
$$\nabla_KC|_{f_0}(x)=\frac1N\sum_{j=1}^NK(x,x_j)\,d|_{f_0}(x_j),$$
and $f(t)$ follows kernel gradient descent if $\partial_tf=-\nabla_KC|_{f(t)}$. Then $\partial_tC=-\|d|_{f(t)}\|_K^2$, so the cost decreases whenever $K$ is positive definite.

> [!definition] Neural tangent kernel
> $$\Theta^{(L)}(\theta)=\sum_{p=1}^P\partial_{\theta_p}F^{(L)}(\theta)\otimes\partial_{\theta_p}F^{(L)}(\theta).$$
> Under gradient descent, $\partial_tf_{\theta(t)}=-\nabla_{\Theta^{(L)}}C|_{f_{\theta(t)}}$. See [[Neural tangent kernel]].
>
> (source: §4, p. 5)

For a linear model with $P$ random features $f^{(p)}$, the tangent kernel is $\tilde K=\frac1P\sum_pf^{(p)}\otimes f^{(p)}$, which tends to the feature covariance by the law of large numbers; this is the motivating toy case (§3.1, p. 4). A real network is nonlinear in $\theta$, so $\Theta^{(L)}$ depends on $\theta$.

> [!theorem] Proposition 1 (initialization: GP limit)
> For a Lipschitz $\sigma$ and $n_1,\dots,n_{L-1}\to\infty$, the outputs $f_{\theta,k}$ tend in law to iid centered Gaussian processes with covariance $\Sigma^{(L)}$:
> $$\Sigma^{(1)}(x,x')=\tfrac1{n_0}x^\top x'+\beta^2,\qquad
> \Sigma^{(L+1)}(x,x')=\mathbb E_{f\sim N(0,\Sigma^{(L)})}[\sigma(f(x))\sigma(f(x'))]+\beta^2.$$
>
> (source: p. 5; compare Matthews et al., see [[Neural network Gaussian process]])

> [!theorem] Theorem 1 (NTK converges at initialization)
> In the same limit, $\Theta^{(L)}\to\Theta^{(L)}_\infty\otimes\mathrm{Id}_{n_L}$ in probability, with
> $$\Theta^{(1)}_\infty=\Sigma^{(1)},\qquad
> \Theta^{(L+1)}_\infty(x,x')=\Theta^{(L)}_\infty(x,x')\,\dot\Sigma^{(L+1)}(x,x')+\Sigma^{(L+1)}(x,x'),$$
> $$\dot\Sigma^{(L+1)}(x,x')=\mathbb E_{f\sim N(0,\Sigma^{(L)})}[\dot\sigma(f(x))\dot\sigma(f(x'))].$$
> The limit depends only on $\sigma$, depth and the initialization variance.
>
> (source: p. 5)

> [!theorem] Theorem 2 (the NTK stays constant)
> Assume $\sigma$ Lipschitz, twice differentiable with bounded second derivative, and $\int_0^T\|d_t\|_{p_{in}}dt$ stochastically bounded as the widths grow. Then uniformly for $t\in[0,T]$, $\Theta^{(L)}(t)\to\Theta^{(L)}_\infty\otimes\mathrm{Id}_{n_L}$, and $f_\theta$ follows $\partial_tf=\Phi_{\Theta_\infty\otimes\mathrm{Id}}(\langle d_t,\cdot\rangle_{p_{in}})$.
>
> (source: p. 6)

Remark 4 (p. 6): individual hidden activations move less and less as width grows, but their collective motion still lets lower layers learn. In the recursion, $\Sigma^{(L+1)}$ is the learning of the last layer and $\Theta^{(L)}_\infty\dot\Sigma^{(L+1)}$ that of the lower layers. The limiting NTK is positive definite if last-layer features become dense in function space, which the authors find natural to expect from approximation theorems of the [[Universal approximation theorem]] kind (p. 6).

### Least-squares regression (§5, pp. 6-7)

With $C(f)=\tfrac12\|f-f^*\|^2_{p_{in}}$ the dynamics are linear: $f_t=f^*+e^{-t\Pi}(f_0-f^*)$ where $\Pi f=\Phi_K(\langle f,\cdot\rangle_{p_{in}})$. If $\Pi$ has eigenfunctions $f^{(i)}$ (the kernel principal components of the data) with eigenvalues $\lambda_i$,
$$f_t=f^*+\Delta^0_f+\sum_ie^{-t\lambda_i}\Delta^i_f,$$
with $\Delta^0_f$ in the null space of $\Pi$. Convergence is fastest along the largest-eigenvalue components, which motivates early stopping; for the RBF kernel small eigenvalues are high-frequency functions. This is the mechanism behind [[Spectral bias]].

> [!theorem] Limit $t\to\infty$ (p. 7)
> With positive-definite Gram matrix $\tilde K$,
> $$f_{\infty,k}(x)=\kappa_{x,k}^\top\tilde K^{-1}y^*+\big(f_0(x)-\kappa_{x,k}^\top\tilde K^{-1}y_0\big).$$
> The mean is the MAP estimate under the prior $f_k\sim N(0,\Theta_\infty^{(L)})$ with $f_k(x_i)=f_k^*(x_i)$, equal to kernel ridge regression as the regularization goes to 0; the second term is a centered Gaussian whose variance vanishes on the data.

Since $f_0$ is Gaussian in the limit and $e^{-t\Pi}$ is linear, $f_t$ is Gaussian for all $t$.

## Results

All experiments use ReLU, hidden widths equal to $n$, $\beta=0.1$, learning rate 1.0 (§6, p. 7).
- **NTK convergence** (Fig. 1): depth 4, $n=500$ vs $10000$, 10 initializations each. The wider network's NTK has less variance, a similar mean, and moves less over 200 steps ("inflates" at $n=500$).
- **Kernel regression** (Fig. 2): 4 points on the unit circle, 1000 steps; mean and variance of $f_\theta(T)$ at $n=50$ and $1000$ both close to the $t\to\infty$ Gaussian, with the kernels estimated from an $n=10000$ network.
- **MNIST** ($N=512$, Fig. 3): top NTK eigenvalues $\lambda_1=0.0457$, $\lambda_2=0.00108$, $\lambda_3=0.00078$ (first component is near-constant because the PCA is uncentered). Starting along $f^*=f_{\theta(0)}+0.5f^{(2)}$, wider networks deviate less from the straight-line path and match $\|g_t\|=0.5e^{-\lambda_2t}$ more closely. Smaller networks converge faster in steps, attributed to NTK inflation (multiplying the NTK by $a$ is like multiplying the learning rate by $a$).

## Limitations

Stated by the authors: smoothness assumptions on $\sigma$ simplify the proofs but "do not seem to be strictly needed" (footnote, p. 2); the experiments only show that wide networks are close to the limit, and the step-count comparison across widths is confounded by inflation and learning rate (p. 9).

Wiki notes: the results cover fully connected networks, a finite dataset, and width $\to\infty$ with the hidden layers going to infinity; the limit is the regime where the features do not change, so it does not describe feature learning. The last point is general background, **[unverified]** against this paper. Theorem proofs are not in the PDF.

## Connections

- Source of the NTK used in [[When and why PINNs fail (Wang 2022)]], which cites this paper as ref. 33 and analyses PINN NTK eigenvalues.
- Prop. 1 is the GP limit proved with full rigour for deep nets by [[Wide networks as GPs (Matthews 2018)]]; Jacot cites the earlier Lee et al. and Neal versions.
- Eigenmode decay $e^{-\lambda_it}$ is the mechanism used for [[Spectral bias]] and in [[Fourier features (Tancik 2020)]].
- Classical approximation counterpart: [[Universal approximation (Hornik 1989)]].

%% refs:start %%
**Cites in this wiki**: [[Universal approximation (Hornik 1989)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[Fourier features (Tancik 2020)]], [[Priors in Bayesian deep learning (Fortuin 2022)]], [[Respecting causality (Wang 2022)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `papers/ML/Jacot, Gabriel, Hongler - Neural Tangent Kernel Convergence and Generalization in Neural Networks.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Neural tangent kernel]] · [[Neural network Gaussian process]] · [[Gaussian process]] · [[Kernel methods]]
- [[Spectral bias]] · [[Gradient descent]] · [[Weight initialization]] · [[Universal approximation theorem]]
- [[Wide networks as GPs (Matthews 2018)]] · [[When and why PINNs fail (Wang 2022)]]
