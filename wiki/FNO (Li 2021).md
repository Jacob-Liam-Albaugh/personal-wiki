---
type: paper
area: operators
areas: [operators, ml, pde]
source-ref: "Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart, Anandkumar 2021, ICLR 2021; arXiv:2010.08895v3"
tags: [operators, ml, pde]
authors: ["[[Zongyi Li]]", "[[Nikola B. Kovachki]]", "[[Kamyar Azizzadenesheli]]", "[[Burigede Liu]]", "[[Kaushik Bhattacharya]]", "[[Andrew M. Stuart]]", "[[Anima Anandkumar]]"]
year: 2021
venue: "ICLR 2021; arXiv:2010.08895v3"
file: "papers/Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf"
---

# Fourier Neural Operator for parametric PDEs (Li 2021)

**Summary**: Parametrizes the kernel of an integral operator directly in Fourier space: FFT the features, multiply the lowest modes by a learned complex tensor, inverse FFT, add a pointwise linear term. The resulting [[FNO]] is mesh-independent, costs $O(n\log n)$ on a uniform grid, and beats the baselines on Burgers, Darcy and Navier-Stokes, with zero-shot super-resolution and a roughly 4-orders-of-magnitude cheaper forward pass than a pseudo-spectral solver.

**Authors**: Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart, Anima Anandkumar · **Year**: 2021 (ICLR) · **File**: `papers/Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`

---

## Problem

Learn a parametric PDE solution operator $\mathcal G^\dagger:\mathcal A\to\mathcal U$, with $D\subset\mathbb R^d$ bounded and open and $\mathcal A,\mathcal U$ separable Banach spaces of functions on $D$. Data: pairs $\{a_j,u_j\}$ with $a_j\sim\mu$ i.i.d. Fit a parametric map $\mathcal G(\cdot,\theta)\approx\mathcal G^\dagger$ by
$$\min_\theta\ \mathbb E_{a\sim\mu}\big[C(\mathcal G(a,\theta),\mathcal G^\dagger(a))\big]$$
(source: FNO.pdf, §2, eq. 1 and following display, p.3). Complaints about prior work (pp.1-3): finite-dimensional CNN-style maps are mesh-dependent; PINN-type methods solve one instance; earlier neural operators (GNO, MGNO) rely on kernel networks and are slow, and DeepONet-style low-rank maps are limited in expressivity. Headline claims (p.3): 30% lower error on Burgers, 60% on Darcy, 30% on NS ($\nu=10^{-4}$) than the best baselines; 0.005 s per inference vs 2.2 s for the pseudo-spectral solver at $256\times256$.

## Method

### Iterative architecture

Lift $v_0(x)=P(a(x))$, apply $T$ updates, project $u(x)=Q(v_T(x))$ (p.4).

> [!definition] Iterative update (Definitions 1-2)
> $$v_{t+1}(x):=\sigma\big(Wv_t(x)+(\mathcal K(a;\phi)v_t)(x)\big),\quad\forall x\in D$$
> $W\in\mathbb R^{d_v\times d_v}$, $\sigma$ componentwise, $\mathcal K:\mathcal A\times\Theta_{\mathcal K}\to\mathcal L(\mathcal U(D;\mathbb R^{d_v}),\mathcal U(D;\mathbb R^{d_v}))$. The kernel integral operator:
> $$(\mathcal K(a;\phi)v_t)(x):=\int_D\kappa_\phi(x,y,a(x),a(y))\,v_t(y)\,dy$$
> with $\kappa_\phi:\mathbb R^{2(d+d_a)}\to\mathbb R^{d_v\times d_v}$.
>
> (source: FNO.pdf, eqs. 2-3, Defs. 1-2, p.4)

If $\kappa(x,y)=\kappa(x-y)$ the integral is a convolution. See [[Kernel integral operator]], [[Neural operator]].

### Fourier layer

> [!definition] Fourier transform pair
> $$(\mathcal Ff)_j(k)=\int_Df_j(x)\,e^{-2i\pi\langle x,k\rangle}dx$$
> $$(\mathcal F^{-1}f)_j(x)=\int f_j(k)\,e^{2i\pi\langle x,k\rangle}dk$$
> Convolution theorem: $(\mathcal Kv_t)(x)=\mathcal F^{-1}\big(\mathcal F(\kappa_\phi)\cdot\mathcal F(v_t)\big)(x)$.
>
> (source: FNO.pdf, §4, p.5)

> [!definition] Fourier integral operator (Definition 3)
> $$(\mathcal K(\phi)v_t)(x)=\mathcal F^{-1}\big(R_\phi\cdot(\mathcal Fv_t)\big)(x)$$
> $R_\phi$ is the Fourier transform of a periodic $\kappa:\bar D\to\mathbb R^{d_v\times d_v}$. Truncating to $k_{\max}=|\{k\in\mathbb Z^d:|k_j|\le k_{\max,j}\}|$ modes makes $R_\phi$ a complex $k_{\max}\times d_v\times d_v$ tensor with conjugate symmetry. Mode-wise product:
> $$\big(R\cdot(\mathcal Fv_t)\big)_{k,l}=\sum_{j=1}^{d_v}R_{k,l,j}(\mathcal Fv_t)_{k,j}$$
>
> (source: FNO.pdf, eqs. 4-5, Def. 3, pp.5-6)

> [!algorithm] Fourier layer on a uniform grid
> ```
> input  v_t on n-point grid, shape (n, d_v)
> 1. V = FFT(v_t)
> 2. keep modes k_j <= kmax_j
>    or s_j - k_j <= kmax_j (corners)
> 3. V_k <- R_k V_k   (R_k in C^{dv x dv})
> 4. zero the other modes
> 5. y = IFFT(V)
> 6. v_{t+1} = sigma(W v_t + y)
> ```
> $k_{\max,j}=12$ per dimension gives $12^d$ parameters per channel pair block. Cost: truncated DFT $O(nk_{\max})$; with FFT $O(n\log n)$. A uniform grid is required.
>
> (source: FNO.pdf, §4, pp.5-6)

Notes (p.6): $R$ may depend on $\mathcal Fa$; a linear parametrization in $\mathcal Fa$ performs similarly to the direct one, a neural-net parametrization is worse. The pointwise $W$ term lets the model handle non-periodic boundary conditions despite the periodic Fourier basis (p.9). Because only the lowest modes are learned, the weights are independent of the grid, which gives [[Discretization invariance]] and [[Discretization invariance#Zero-shot super-resolution|zero shot super resolution]].

### Experimental setup (p.6)

4 Fourier layers, ReLU, batch norm. $N=1000$ train / 200 test. Adam, 500 epochs, lr 0.001 halved every 100 epochs. $k_{\max,j}=16$, $d_v=64$ in 1-D; $k_{\max,j}=12$, $d_v=32$ in 2-D. One V100 16 GB. Baselines: time-independent NN, RBM, FCN (Zhu-Zabaras), PCANN, GNO, MGNO, LNO (low-rank, similar to unstacked DeepONet); time-dependent ResNet, U-Net, TF-Net, FNO-2D (RNN in time) and FNO-3D (space-time convolution). See [[Neural operator#Graph neural operator|graph neural operator]], [[Neural operator#Multipole graph neural operator|multipole graph neural operator]], [[Neural operator#Low-rank neural operator|low rank neural operator]], [[DeepONet]].

### Problems

> [!definition] Burgers (eq. 6)
> $$\partial_tu+\partial_x(u^2/2)=\nu\,\partial_{xx}u,\quad x\in(0,1),\ t\in(0,1]$$
> periodic BC, $\mathcal G^\dagger:u_0\mapsto u(\cdot,1)$. Data: $u_0\sim N(0,625(-\Delta+25I)^{-2})$, $\nu=0.1$, split-step solver on $2^{13}=8192$ points.
>
> (source: FNO.pdf, eq. 6, §5.1, p.6)

> [!definition] Darcy flow (eq. 7)
> $$-\nabla\cdot(a\nabla u)=f\ \text{on }(0,1)^2,\quad u=0\ \text{on }\partial(0,1)^2,\ f\equiv1$$
> $\mathcal G^\dagger:a\mapsto u$ (nonlinear although the PDE is linear). Data: $a\sim\psi_\#N(0,(-\Delta+9I)^{-2})$, $\psi=12$ on positive and $3$ on negative values; second-order finite differences on $421\times421$, downsampled.
>
> (source: FNO.pdf, eq. 7, §5.2, pp.6-7)

> [!definition] Navier-Stokes, vorticity form (eq. 8)
> $$\partial_tw+u\cdot\nabla w=\nu\Delta w+f,\quad\nabla\cdot u=0$$
> unit torus, $\mathcal G^\dagger:w|_{[0,10]}\mapsto w|_{(10,T]}$. Data: $w_0\sim N(0,7^{3/2}(-\Delta+49I)^{-2.5})$, $f=0.1(\sin(2\pi(x_1+x_2))+\cos(2\pi(x_1+x_2)))$, pseudo-spectral Crank-Nicolson at $256\times256$, downsampled to $64\times64$.
>
> (source: FNO.pdf, eq. 8, §5.3, p.7)

See [[Burgers equation]], [[Darcy flow]], [[Navier-Stokes equations]]. The Gaussian input measures are $N(0,C)$ with $C=(-\Delta+\tau^2I)^{-\alpha}$ ([[Gaussian process]] / [[Karhunen-Loève expansion]] type priors; Wiki note: the paper does not develop either).

## Results

All errors are relative $L^2$.

**Burgers** (Table 3, p.15), $s=256,512,1024,2048,4096,8192$:

| Model | 256 | 512 | 1024 | 2048 | 4096 | 8192 |
|---|---|---|---|---|---|---|
| NN | 0.4714 | 0.4561 | 0.4803 | 0.4645 | 0.4779 | 0.4452 |
| GCN | 0.3999 | 0.4138 | 0.4176 | 0.4157 | 0.4191 | 0.4198 |
| FCN | 0.0958 | 0.1407 | 0.1877 | 0.2313 | 0.2855 | 0.3238 |
| PCANN | 0.0398 | 0.0395 | 0.0391 | 0.0383 | 0.0392 | 0.0393 |
| GNO | 0.0555 | 0.0594 | 0.0651 | 0.0663 | 0.0666 | 0.0699 |
| LNO | 0.0212 | 0.0221 | 0.0217 | 0.0219 | 0.0200 | 0.0189 |
| MGNO | 0.0243 | 0.0355 | 0.0374 | 0.0360 | 0.0364 | 0.0364 |
| FNO | 0.0149 | 0.0158 | 0.0160 | 0.0146 | 0.0142 | 0.0139 |

FNO error is flat in $s$; FCN degrades with resolution; the mesh-dependent NN/GCN are worst.

**Darcy** (Table 4, p.15), $s=85,141,211,421$:

| Model | 85 | 141 | 211 | 421 |
|---|---|---|---|---|
| NN | 0.1716 | 0.1716 | 0.1716 | 0.1716 |
| FCN | 0.0253 | 0.0493 | 0.0727 | 0.1097 |
| PCANN | 0.0299 | 0.0298 | 0.0298 | 0.0299 |
| RBM | 0.0244 | 0.0251 | 0.0255 | 0.0259 |
| GNO | 0.0346 | 0.0332 | 0.0342 | 0.0369 |
| LNO | 0.0520 | 0.0461 | 0.0445 | - |
| MGNO | 0.0416 | 0.0428 | 0.0428 | 0.0420 |
| FNO | 0.0108 | 0.0109 | 0.0109 | 0.0098 |

There is no DeepONet row in this paper (the JMLR version [[Neural operator (Kovachki 2022)]] adds one, 0.0476-0.0487).

**Navier-Stokes** (Table 1, p.8), $64\times64$; columns are $(\nu,T,N)$ = (1e-3, 50, 1000), (1e-4, 30, 1000), (1e-4, 30, 10000), (1e-5, 20, 1000):

| Model | Params | s/epoch | 1e-3 | 1e-4 | 1e-4 (N=1e4) | 1e-5 |
|---|---|---|---|---|---|---|
| FNO-3D | 6,558,537 | 38.99 | 0.0086 | 0.1918 | 0.0820 | 0.1893 |
| FNO-2D | 414,517 | 127.80 | 0.0128 | 0.1559 | 0.0834 | 0.1556 |
| U-Net | 24,950,491 | 48.67 | 0.0245 | 0.2051 | 0.1190 | 0.1982 |
| TF-Net | 7,451,724 | 47.21 | 0.0225 | 0.2253 | 0.1168 | 0.2268 |
| ResNet | 266,641 | 78.47 | 0.0701 | 0.2871 | 0.2311 | 0.2753 |

FNO-3D is best with enough data; with insufficient data all methods exceed 15% error, and FNO-2D is lowest there. The full time series is predicted with under 1% error at $\nu=10^{-3}$ and 8% at $\nu=10^{-4}$ (p.3).

**Zero-shot super-resolution** (p.9, Fig. 1): FNO-3D trained on $64\times64\times20$ ($\nu=10^{-4}$, $N=10000$) evaluated at $256\times256\times80$ in space and time; FNO is the only benchmark that can do this.

**Bayesian inverse problem** (p.9): function-space MCMC (Cotter et al. 2013), 25,000 posterior samples plus 5,000 burn-in, i.e. 30,000 forward evaluations. FNO at 0.005 s per evaluation: about 2.5 minutes. Solver at 2.2 s per evaluation: over 18 hours. Offline data generation plus training: 12 hours. Posterior means nearly identical.

**Spectral analysis** (p.9): truncating at 20 modes gives about 2% error at $\nu=10^{-3}$, while FNO with $k_{\max}=12$ achieves 1% or less. The NS data spectrum decays like $k^{-5/3}$ (A.2, p.13).

## Limitations

As stated by the authors (pp.6, 9):
- Data hungry: $N=10000$ pairs are needed to reach a useful error at $\nu=10^{-4}$.
- A uniform grid is required for the FFT (p.6).
- Suggested future work: combine with numerical solvers, recurrent weight sharing, computer-vision applications.

Wiki note: the truncation to a few modes presupposes a smooth solution; the benchmark solutions are smooth or periodic, and the 20-mode ablation (p.9) is the only evidence on this. The paper has no approximation theorem; the JMLR version [[Neural operator (Kovachki 2022)]] notes its universal approximation theory excludes FNO and cites separate Hilbert-space FNO results (Kovachki, Lanthaler, Mishra 2021). Baseline hyperparameters appear not to be tuned as heavily as FNO's: **[unverified]**, inferred from the later JMLR retuning (Burgers FNO 0.0139-0.0160 here vs 0.0018 there).

## Connections

- Instance of the [[Neural operator]] framework with the kernel parametrized in Fourier space; contrasts with [[Neural operator#Graph neural operator|graph neural operator]] (Nystrom/message passing), [[Neural operator#Multipole graph neural operator|multipole graph neural operator]] and [[Neural operator#Low-rank neural operator|low rank neural operator]] (its LNO baseline, "similar to unstacked DeepONet").
- Extended and retuned in [[Neural operator (Kovachki 2022)]] (JMLR), which also proves DeepONet is a special case of a neural operator ([[DeepONet]], [[DeepONet (Lu 2021)]]).
- [[LNO (Cao 2023)]] replaces the Fourier basis with Laplace-domain poles and residues ([[LNO]]); Wiki note: neither is discussed in this paper.
- Surveyed in [[Operator learning review (Kovachki 2024)]].
- General setting: [[Operator learning]], [[Kernel integral operator]].

%% refs:start %%
**Cites in this wiki**: [[Bayesian DenseED surrogate (Zhu 2018)]], [[DeepONet (Lu 2021)]], [[PINNs (Raissi 2019)]], [[SIREN paper (Sitzmann 2020)]]
**Cited by in this wiki**: [[LNO (Cao 2023)]], [[NIF (Pan 2023)]], [[Neural operator (Kovachki 2022)]], [[Operator learning review (Kovachki 2024)]]
%% refs:end %%

**Sources**: `papers/Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[FNO]]
- [[Neural operator]]
- [[Operator learning]]
- [[Kernel integral operator]]
- [[Discretization invariance]]
- [[DeepONet]]
- [[Darcy flow]]
- [[Burgers equation]]
- [[Navier-Stokes equations]]
- [[Gaussian process]]
- [[Karhunen-Loève expansion]]
- [[LNO]]
- [[Neural operator (Kovachki 2022)]]
- [[DeepONet (Lu 2021)]]
- [[LNO (Cao 2023)]]
- [[Operator learning review (Kovachki 2024)]]
