---
type: paper
area: operators
areas: [operators, ml, pde]
source-ref: "Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, Anandkumar 2022, JMLR 23 (2022) 1-97"
tags: [operators, ml]
authors: [Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, Anandkumar]
year: 2022
venue: "JMLR 23 (2022) 1-97; arXiv:2108.08481v6"
file: "Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf"
---

# Neural Operator: learning maps between function spaces (Kovachki 2022)

**Summary**: Defines the neural operator, a composition of pointwise lifting, iterated nonlocal kernel-integral layers and pointwise projection, which learns a map between Banach function spaces with a fixed parameter count and is discretization invariant. Four concrete parametrizations are given (graph, low-rank, multipole, Fourier), a universal approximation theorem is proved for the integral-operator class, and the methods are benchmarked on Poisson, Darcy, Burgers and Navier-Stokes. The Fourier version is best in nearly all benchmarks.

**Authors**: Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, Anandkumar · **Year**: 2022 (JMLR 23, submitted 12/21, revised 10/22, published 12/22) · **File**: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`

---

## Problem

Learn the map $\mathcal{G}^\dagger : \mathcal{A} \to \mathcal{U}$ between separable Banach function spaces (typically a PDE solution operator $a \mapsto u$) from pairs $\{a_i, u_i\}$ with $a_i \sim \mu$ i.i.d. (source: Neural Operators.pdf, §2.2, p.7).

> [!definition] Learning problem
> Bochner loss and empirical risk:
> $$\|\mathcal{G}^\dagger - \mathcal{G}_\theta\|^2_{L^2_\mu(\mathcal{A};\mathcal{U})} = \mathbb{E}_{a\sim\mu}\|\mathcal{G}^\dagger(a) - \mathcal{G}_\theta(a)\|_{\mathcal{U}}^2$$
> $$\min_\theta \frac1N \sum_{i=1}^N \|u^{(i)} - \mathcal{G}_\theta(a^{(i)})\|_{\mathcal{U}}^2$$
> Uniform version on compact $K\subset\mathcal{A}$: $\sup_{a\in K}\|\mathcal{G}^\dagger(a)-\mathcal{G}_\theta(a)\|_{\mathcal{U}}$.
>
> (source: Neural Operators.pdf, eqs. 3-5, p.7)

For a generic PDE $(\mathcal{L}_a u)(x) = f(x)$ on $D$ with $u=0$ on $\partial D$, the target is $\mathcal{G}^\dagger := \mathcal{L}_a^{-1} f$ (eq. 1, p.7). The paper's complaints about existing approaches (§1, pp.2-5): finite-dimensional NNs (e.g. CNNs) are tied to one mesh; DeepONet cannot take input at arbitrary points; PINN-type methods fit one PDE instance; hybrid solvers need the PDE.

The central requirement is [[Discretization invariance]]: fixed parameters, any input point set, evaluable at any output point, and convergence to a continuum operator under refinement.

> [!definition] Discretization invariance
> A discrete refinement is nested $D_1\subset D_2\subset\dots\subset D$, $|D_L|=L$, with: for every $\varepsilon>0$ there is $L$ such that $D\subseteq\bigcup_{x\in D_L}\{y:\|y-x\|_2<\varepsilon\}$ (Def. 1). Discretized uniform risk:
> $$R_K(\mathcal{G},\hat{\mathcal{G}},D_L)=\sup_{a\in K}\|\hat{\mathcal{G}}(D_L,a|_{D_L})-\mathcal{G}(a)\|_{\mathcal{U}}$$
> (Def. 3). $\mathcal{G}:\mathcal{A}\times\Theta\to\mathcal{U}$ is discretization invariant if there exist maps $\hat{\mathcal{G}}_L:\mathbb{R}^{Ld}\times\mathbb{R}^{Lm}\times\Theta\to\mathcal{U}$ such that for every $\theta$ and compact $K\subset\mathcal{A}$:
> $$\lim_{L\to\infty}R_K(\mathcal{G}(\cdot,\theta),\hat{\mathcal{G}}_L(\cdot,\cdot,\theta),D_L)=0$$
>
> (source: Neural Operators.pdf, Defs. 1-4, pp.8-9)

Table 1 (p.5) summarises the comparison:

| Property | NNs | DeepONets | Interpolation | Neural operators |
|---|---|---|---|---|
| Discretization invariant | no | no | yes | yes |
| Output is a function | no | yes | yes | yes |
| Query output at any point | no | yes | yes | yes |
| Take input at any point | no | no | yes | yes |
| Universal approximation | no | yes | no | yes |

Error splits as discretization error plus approximation error (p.12):
$\|\hat{\mathcal G}_\theta(D_L,a|_{D_L})-\mathcal G^\dagger(a)\| \le \|\hat{\mathcal G}_\theta(D_L,a|_{D_L})-\mathcal G_\theta(a)\| + \|\mathcal G_\theta(a)-\mathcal G^\dagger(a)\|$.

## Method

### Architecture

> [!definition] Neural operator
> $$\mathcal{G}_\theta := Q\circ\sigma_T(W_{T-1}+\mathcal{K}_{T-1}+b_{T-1})\circ\cdots\circ\sigma_1(W_0+\mathcal{K}_0+b_0)\circ P$$
> $P,Q$: local lifting and projection (Nemytskii operators). $W_t$: local linear matrices. $\mathcal{K}_t$: integral kernel operators. $b_t$: bias functions. Layer update:
> $$v_{t+1}(x)=\sigma_{t+1}\Big(W_t v_t(\Pi_t(x))+\int\kappa^{(t)}(x,y)\,v_t(y)\,d\nu_t(y)+b_t(x)\Big)$$
>
> (source: Neural Operators.pdf, eqs. 6 and 10, pp.9-11)

Three kernel choices (pp.10-11):

> [!definition] Kernel integral operator, three versions
> ```
> (7)  kappa(x, y)
> (8)  kappa(x, y, a(x), a(y))
> (9)  kappa(x, y, v_t(x), v_t(y))
> ```
> (7) is linear in $v_t$. (8) feeds the input $a$ into every layer's kernel. (9) is a nonlinear integral operator.
>
> (source: Neural Operators.pdf, eqs. 7-9, pp.10-11)

Eq. 8 outperforms eq. 7 on Darcy because with (7) the input $a$ enters only through the initial lifting and its influence fades with depth (p.11). Feeding $(x,a(x))$ to $P$ gives the network access to geometry. A two-layer instance (eq. 11, p.11):
$(\mathcal G_\theta(a))(x)=Q\big(\int_D\kappa^{(1)}(x,y)\,\sigma(W_0P(a(y))+\int_D\kappa^{(0)}(y,z)P(a(z))dz+b_0(y))\,dy\big)$.

### Computing the integral

Single layer (eq. 12): $u(x)=\sigma(Wv(x)+\int\kappa(x,y)v(y)d\nu(y)+b(x))$, with constant bias $b\in\mathbb R^m$ working at least as well as a function (p.13). Monte Carlo (eq. 14): $u(x_j)=\frac1J\sum_l\kappa(x_j,x_l)v(x_l)$, cost $O(J^2)$. The four parametrizations differ in how this is made cheaper (§4, pp.12-24).

> [!algorithm] Graph neural operator (GNO), §4.1
> Nystrom: sample $J'\ll J$ points, giving low-rank $K\approx K_{JJ'}K_{J'J'}K_{J'J}$, cost $O(J'^2)$ (eq. 15). Truncation: restrict to a ball,
> $$u(x)=\int_{B(x,r)\cap D}\kappa(x,y)v(y)\,dy$$
> cost $c_sJ^2$ with $c_s\approx r^d$ (eq. 16). Implemented by message passing (Gilmer et al.) with edge features $(x_j,x_k)\in\mathbb R^{2d}$ and mean aggregation. Composing $L\ge2$ truncated layers with $2^{L-1}r\ge1$ covers $D$ at cost $O(Lr^dJ^2)$, so truncation loses no expressivity.
>
> (source: Neural Operators.pdf, §4.1, pp.14-17)

A CNN is the special case $\kappa(x-y)$ with compact support parametrized pointwise (eq. 17); it is not discretization-consistent because the kernel support shrinks to a point under refinement, or the parameters blow up (p.17).

> [!definition] Low-rank neural operator (LNO), §4.2
> $$\kappa(x,y)=\sum_{j=1}^{r}\varphi^{(j)}(x)\psi^{(j)}(y)\ \Rightarrow\ u(x)=\sum_{j=1}^r\langle\psi^{(j)},v\rangle\,\varphi^{(j)}(x)$$
> Cost $O(rJ)$; equivalent to a rank-$r$ operator $K=K_{Jr}K_{rJ}$. Similar to DeepONet.
>
> (source: Neural Operators.pdf, eqs. 18, 29, pp.18, 22)

> [!algorithm] Multipole graph neural operator (MGNO), §4.3
> Range-split $K=K_1+\dots+K_L$ (eq. 19), multi-resolution factorization
> $$K\approx K_{1,1}+K_{1,2}K_{2,2}K_{2,1}+K_{1,2}K_{2,3}K_{3,3}K_{3,2}K_{2,1}+\cdots$$
> (eq. 20), with learned truncated integral operators for $K_{l,l},K_{l+1,l},K_{l,l+1}$ (eqs. 21-23). V-cycle, per layer $t$:
> ```
> down (24): v_check[l+1] = sigma( v_hat[l+1]
>               + K[l+1,l] v_check[l] )
> up   (25): v_hat[l] = sigma( (W_l + K[l,l]) v_check[l]
>               + K[l,l-1] v_hat[l-1] )
> ```
> Complexity $\sum_l O(J_l^2r_l^d)=O(J)$ for suitable $r_l$, $J_l$ (e.g. $d=2$, $r_l=1/\sqrt{J_l}$, $J_l=O(2^{-l}J)$).
>
> (source: Neural Operators.pdf, §4.3, pp.18-22)

> [!algorithm] Fourier neural operator (FNO), §4.4
> On the torus $\mathbb T^d$ with $\psi_k(x)=e^{2\pi i k\cdot x}$:
> $$u(x)=\mathcal F^{-1}\big(R_\phi\cdot\mathcal F(v)\big)(x)$$
> $R_\phi$ is a complex $(k_{\max}\times m\times n)$ tensor with conjugate symmetry $R(-k)_{j,l}=R^*(k)_{j,l}$. Mode-wise product (eq. 27). Cost $O(Jk_{\max})$ for the truncated DFT, $O(J\log J)$ with FFT on a uniform grid. Modes kept: the "corners" of the FFT array, $k_{\max,j}\approx\frac13$ to $\frac23$ of the modes; experiments use $k_{\max,j}=12$, i.e. $12^d$ parameters per channel.
>
> (source: Neural Operators.pdf, eqs. 26-27, pp.22-24)

$R$ can be parametrized directly, linearly in $\mathcal F a$, or by a feed-forward net; linear is similar to direct but less efficient, the NN version is worse (p.23). Non-periodic or non-uniform domains: Fourier continuation, or zero-padding into the torus (p.24). The theory of §8 does not cover FNO; separate Hilbert-space FNO results are cited (Kovachki, Lanthaler, Mishra 2021). Complexities (§4.5): GNO $O(JJ')$, LNO $O(J)$, MGNO $O(J)$, FNO $O(J\log J)$. See [[FNO]], [[Neural operator#Graph neural operator|graph neural operator]], [[Neural operator#Low-rank neural operator|low rank neural operator]], [[Neural operator#Multipole graph neural operator|multipole graph neural operator]].

### Relation to DeepONet and transformers (§5, pp.24-29)

> [!theorem] Proposition 5 (DeepONet as a special case)
> A neural operator with a pointwise-parametrized first kernel and discretized integral operators yields a DeepONet. Proof: eq. 11 with $W_0=0$, $P(x)=(x,\dots,x)$, $Q(x)=x_1+\dots+x_p$, $\kappa_j^{(0)}(y,z)=1(y)w_j(z)$, $\kappa^{(1)}_{jk}(x,y)=\frac{\tilde c_{jk}}{|D|}\varphi_k(x)1(y)$. Result:
> $$(\mathcal G_\theta(a))(x)=\sum_{k=1}^p\Big[\sum_{j=1}^n\tilde c_{jk}\,\sigma(\langle\tilde w_j,\tilde a\rangle+\tilde b_j)\Big]\varphi_k(x)=\sum_k G_k(\tilde a)\varphi_k(x)$$
> $\varphi_k$ is the trunk net, $G$ the branch net.
>
> (source: Neural Operators.pdf, Prop. 5, eq. 32, pp.25-26)

This DeepONet is not discretization invariant: the parameter count depends on $q$, the number of sensors. The "DeepONet-Operator" (eq. 33) replaces $\langle\tilde w_j,\tilde a\rangle_{\mathbb R^q}$ with the function-space inner product $\langle w_j,a\rangle$, which is. DeepONet and LNO live in a linear space $\mathrm{span}\{\varphi_1..\varphi_p\}$ and are limited by Kolmogorov $n$-width; the authors say a general neural operator is a nonlinear approximation (pp.26-27). See [[DeepONet]], [[DeepONet (Lu 2021)]].

> [!theorem] Proposition 6 (attention as a special case)
> Kernel (9) with $\kappa_v(v(x),v(y))=g_v(v(x),v(y))R$, $g_v$ the softmax-normalised $\exp(\langle Av(x),Bv(y)\rangle/\sqrt m)$. A Monte Carlo discretization gives $u_j=\sigma(v_j+R_{out}\sum_qS_j(z_q)R_{val}v_q)$, a single-head attention block. Standard ViTs are not special cases because CNN patch tokenization is not discretization invariant.
>
> (source: Neural Operators.pdf, Prop. 6, eq. 35, pp.28-29)

### Approximation theory (§8, pp.47-53)

Setting: network class $\mathcal N_n(\sigma;\mathbb R^d)$ of depth $n$; $\mathcal A_m$ the activations $\sigma\in C(\mathbb R)$ for which some depth-$n$ net class is dense in $C^m(K)$ for all compact $K$ (Pinkus 1999: non-polynomial $C^m$ functions qualify with $n=1$); $\mathcal A_m^L\subset\mathcal A_m$ adds Borel measurability and $\sup_x|\sigma(x)|/(1+|x|)<\infty$ (ReLU is in $\mathcal A^L_0$, ELU in $\mathcal A^L_1$); $\mathcal B_A$ (Def. 7) is the $\sigma\in\mathcal A_0$ that approximate the identity with bounded range (ReLU qualifies with $n=3$). The theorem class $NO_n(\sigma_1,\sigma_2,\sigma_3;D,D')$ uses affine kernel-integral layers $f\mapsto\int_D\kappa(\cdot,y)f(y)dy+b$ with $\kappa,b$ neural nets; here $P$, $Q$, $\sigma_n$ are identity and $W_t=0$. The authors note learning them helps in practice and explaining this is future work (p.49).

> [!definition] Assumptions 9 and 10
> 9 ($D\subset\mathbb R^d$ Lipschitz): $\mathcal A=L^{p_1}(D)$, $1\le p_1<\infty$; or $W^{m_1,p_1}(D)$, $1\le p_1<\infty$; or $C(\bar D)$.
> 10 ($D'\subset\mathbb R^{d'}$ Lipschitz): $\mathcal U=L^{p_2}(D')$; or $W^{m_2,p_2}(D')$, $1\le p_2<\infty$; or $C^{m_2}(\bar D')$.
>
> (source: Neural Operators.pdf, §8, p.49)

> [!theorem] Theorem 8 (discretization invariance of the class)
> $D\subset\mathbb R^d$, $D'\subset\mathbb R^{d'}$; $\mathcal A,\mathcal U$ real Banach function spaces continuously embedded in $C(\bar D)$, $C(\bar D')$; $\sigma_1,\sigma_2,\sigma_3\in C(\mathbb R)$. Then for any $n$, $NO_n(\sigma_1,\sigma_2,\sigma_3;D,D')$ as maps $\mathcal A\to\mathcal U$ are discretization invariant. Proof by Riemann sums and uniform convergence on compacts (appendix E).
>
> (source: Neural Operators.pdf, Thm 8, p.48)

> [!theorem] Theorem 11 (universal approximation, uniform on compacts)
> Let Assumptions 9, 10 hold and $\mathcal G^\dagger:\mathcal A\to\mathcal U$ be continuous. Let $\sigma_1\in\mathcal A^L_0$, $\sigma_2\in\mathcal A_0$, $\sigma_3\in\mathcal A_{m_2}$. Then for any compact $K\subset\mathcal A$ and $0<\varepsilon\le1$ there exist $N\in\mathbb N$ and $\mathcal G\in NO_N(\sigma_1,\sigma_2,\sigma_3;D,D')$ with
> $$\sup_{a\in K}\|\mathcal G^\dagger(a)-\mathcal G(a)\|_{\mathcal U}\le\varepsilon$$
> Moreover, if $\mathcal U$ is Hilbert, $\sigma_1\in\mathcal B_A$ and $\|\mathcal G^\dagger(a)\|_{\mathcal U}\le M$ for all $a$, then $\mathcal G$ can be chosen with $\|\mathcal G(a)\|_{\mathcal U}\le4M$ for all $a\in\mathcal A$.
>
> (source: Neural Operators.pdf, Thm 11, p.50; proof appendix F)

> [!theorem] Theorem 12 (input in $C^{m_1}$)
> $D$ Lipschitz, $m_1\in\mathbb N$, $\mathcal A:=C^{m_1}(\bar D)$, Assumption 10, $\mathcal G^\dagger$ continuous, same $\sigma$'s. For compact $K$ and $0<\varepsilon\le1$ there is $\mathcal G\in NO^{m_1}_N$ (order-$m_1$ neural operator taking $(\partial^{\alpha_1}f,\dots,\partial^{\alpha_{J_m}}f)$ as input) with $\sup_K\|\mathcal G^\dagger-\mathcal G\|_{\mathcal U}\le\varepsilon$, and the same Hilbert bound $\le4M$.
>
> (source: Neural Operators.pdf, Thm 12, p.50)

> [!theorem] Theorem 13 (universal approximation in $L^2_\mu$)
> $D'$ Lipschitz, $m_2\in\mathbb N_0$, Assumption 9, $\mu$ a probability measure on $\mathcal A$, $\mathcal G^\dagger:\mathcal A\to H^{m_2}(D')$ $\mu$-measurable with $\mathcal G^\dagger\in L^2_\mu(\mathcal A;H^{m_2}(D'))$; $\sigma_1\in\mathcal A_0^L\cap\mathcal B_A$, $\sigma_2\in\mathcal A_0$, $\sigma_3\in\mathcal A_{m_2}$. Then for any $0<\varepsilon\le1$ there are $N$ and $\mathcal G\in NO_N$ with
> $$\|\mathcal G^\dagger-\mathcal G\|_{L^2_\mu(\mathcal A;H^{m_2}(D'))}\le\varepsilon$$
>
> (source: Neural Operators.pdf, Thm 13, p.51; proof appendix G, following Lanthaler et al. via Lusin's theorem)

Theorem 14 is the analogue for $\mathcal A=C^{m_1}(D)$, $\mu$ on $C^{m_1}(D)$, $\mathcal G^\dagger\in L^2_\mu(C^{m_1}(D);\mathcal U)$, with order-$m_1$ neural operators (proof via Thm 12 and the argument of Thm 13). Proof strategy (Fig. 16, p.51): (1) approximate the linear functionals $F:\mathcal A\to\mathbb R^J$ by integration against smooth functions (Lemmas 21, 23, generalizing Chen & Chen 1995) and then by integral-operator layers (Lemma 25), using the Banach approximation property and a Riesz-type representation for $C^m$; (2) approximate a continuous $\psi:\mathbb R^J\to\mathbb R^{J'}$ by a standard NN (Lemma 28); (3) produce coefficients of an expansion in representers of $\mathcal U$ with one layer (Lemma 27). Structure follows Bhattacharya et al. 2020, generalized from Hilbert to Banach spaces. See [[Universal approximation for operators]].

## Results

Common setup (pp.35-36): 4 integral layers, ReLU, no batch norm (the ICLR FNO paper [[FNO (Li 2021)]] uses batch norm), $N=1000$ train and 200 test, Adam 500 epochs, lr $10^{-3}$ halved every 100 epochs, $d_v=64$ (1-D) or 32 (2-D), kernel nets 3-layer width 256. GNO $r=0.25$, $J'=300$; LNO rank 4; MGNO Darcy random graph $J_1=400,J_2=100,J_3=25$; FNO $k_{\max}=16$ (1-D), 12 (2-D). Metric: relative $L^2$ error.

**Poisson, 1-D** (p.36): $-u''=f$, zero BC, $\mu=N(0,(L+I)^{-2})$, 85 collocation points, $N=1000$. A zero-hidden-layer operator reaches relative test error about $10^{-7}$ and the learned kernel matches the Green's function $G(x,y)=\frac12(x+y-|y-x|)-xy$ (Fig. 7), so it generalizes beyond the support of $\mu$.

**Darcy** (Table 2, p.39), relative $L^2$ error, resolution $s=85,141,211,421$:

| Model | 85 | 141 | 211 | 421 |
|---|---|---|---|---|
| NN | 0.1716 | 0.1716 | 0.1716 | 0.1716 |
| FCN | 0.0253 | 0.0493 | 0.0727 | 0.1097 |
| PCANN | 0.0299 | 0.0298 | 0.0298 | 0.0299 |
| RBM | 0.0244 | 0.0251 | 0.0255 | 0.0259 |
| GNO | 0.0346 | 0.0332 | 0.0342 | 0.0369 |
| LNO | 0.0520 | 0.0461 | 0.0445 | - |
| MGNO | 0.0416 | 0.0428 | 0.0428 | 0.0420 |
| DeepONet | 0.0476 | 0.0479 | 0.0462 | 0.0487 |
| FNO | 0.0108 | 0.0109 | 0.0109 | 0.0098 |

The DeepONet baseline is an unstacked net (8 layers, width 200). A CNN-branch/PCA-trunk DeepONet reaches 0.0232 at $s=29$ (Lu et al. 2021b). FCN error grows with resolution; the neural operators stay flat.

**Burgers** (Table 3, p.39), $s=256,512,1024,2048,4096,8192$:

| Model | 256 | 512 | 1024 | 2048 | 4096 | 8192 |
|---|---|---|---|---|---|---|
| NN | 0.4714 | 0.4561 | 0.4803 | 0.4645 | 0.4779 | 0.4452 |
| GCN | 0.3999 | 0.4138 | 0.4176 | 0.4157 | 0.4191 | 0.4198 |
| FCN | 0.0958 | 0.1407 | 0.1877 | 0.2313 | 0.2855 | 0.3238 |
| PCANN | 0.0398 | 0.0395 | 0.0391 | 0.0383 | 0.0392 | 0.0393 |
| GNO | 0.0555 | 0.0594 | 0.0651 | 0.0663 | 0.0666 | 0.0699 |
| LNO | 0.0212 | 0.0221 | 0.0217 | 0.0219 | 0.0200 | 0.0189 |
| MGNO | 0.0243 | 0.0355 | 0.0374 | 0.0360 | 0.0364 | 0.0364 |
| DeepONet | 0.0569 | 0.0617 | 0.0685 | 0.0702 | 0.0833 | 0.0857 |
| FNO | 0.0018 | 0.0018 | 0.0018 | 0.0019 | 0.0020 | 0.0019 |

FNO std 0.0010, mean training error 0.0012; GeLU lowers test error from 0.0018 to 0.0007; PCA-DeepONet reaches 0.0194 at $s=128$. These FNO numbers are about 8x lower than the ICLR paper's (0.0139-0.0160). Wiki note: the differences are no batch norm and tuning, but the text does not say which causes the gap.

**Navier-Stokes** (Table 4, p.41; identical to the ICLR Table 1), $64\times64$, error for $(\nu,T,N)$ = (1e-3, 50, 1000), (1e-4, 30, 1000), (1e-4, 30, 10000), (1e-5, 20, 1000):

| Model | Params | s/epoch | 1e-3 | 1e-4 | 1e-4 (N=1e4) | 1e-5 |
|---|---|---|---|---|---|---|
| FNO-3D | 6,558,537 | 38.99 | 0.0086 | 0.1918 | 0.0820 | 0.1893 |
| FNO-2D | 414,517 | 127.80 | 0.0128 | 0.1559 | 0.0834 | 0.1556 |
| U-Net | 24,950,491 | 48.67 | 0.0245 | 0.2051 | 0.1190 | 0.1982 |
| TF-Net | 7,451,724 | 47.21 | 0.0225 | 0.2253 | 0.1168 | 0.2268 |
| ResNet | 266,641 | 78.47 | 0.0701 | 0.2871 | 0.2311 | 0.2753 |

Resolution study (Table 5, p.42; $\nu=10^{-3}$, $N=200$, $T=20$), $s=64,128,256$: FNO-3D 0.0098, 0.0101, 0.0106; FNO-2D 0.0129, 0.0128, 0.0126; U-Net 0.0253, 0.0289, 0.0344; TF-Net 0.0277, 0.0278, 0.0301. The FNO error is roughly flat in $s$; the convolutional baselines degrade.

**Zero-shot super-resolution** (§7.2.3, pp.40-42, Figs. 9, 11): GNO trained on $16\times16$ Darcy and tested on $241\times241$; FNO-3D trained on $64\times64\times20$ NS ($\nu=10^{-4}$, Re about 200) and evaluated at $256\times256\times80$. See [[Discretization invariance#Zero-shot super-resolution|zero shot super resolution]].

**Bayesian inverse problem** (§6.4.1, §7.3.4, pp.34, 44): observe $y=O(\mathcal G^\dagger(w_0))+\eta$, $\mathcal G^\dagger:w_0\mapsto\Psi(w_0,50)$, $O$ a $7\times7$ interior grid ($\mathbb R^{49}$), $\eta\sim N(0,\Gamma)$, $\Gamma=\gamma^{-2}I$, $\gamma=0.1$. Posterior density w.r.t. the prior $\propto\exp(-\frac12\|y-O(\mathcal G^\dagger(w_0))\|^2_\Gamma)$, sampled with pCN: 5,000 burn-in plus 25,000 samples. FNO costs 0.005 s per evaluation vs 2.2 s for the solver, so about 2.5 minutes vs over 18 hours, plus 12 hours offline data generation and training; posterior means nearly identical.

**Cost** (Table 7, p.46), time per training epoch: GNO 4 s, LNO 20 s, MGNO 8 s, FNO 4 s.

**Refinability** (Table 8, Darcy error vs parameter budget $10^3,10^4,10^5,10^6$, rounded values read from the table):

| Model | 1e3 | 1e4 | 1e5 | 1e6 |
|---|---|---|---|---|
| GNO | 0.075 | 0.065 | 0.060 | 0.035 |
| LNO | 0.080 | 0.070 | 0.060 | 0.040 |
| MGNO | 0.070 | 0.050 | 0.040 | 0.030 |
| FNO | 0.200 | 0.035 | 0.020 | 0.015 |

FNO needs more parameters at small budgets because it has no kernel network.

**Robustness** (Table 9, p.46), input noise $a'=a+0.1\|a\|_\infty\xi$; train / clean test / noisy test error: Burgers 0.002/0.002/0.018; Advection 0.002/0.002/0.094; Darcy 0.006/0.011/0.012; NS 0.024/0.024/0.039. Trained with noise: Burgers 0.011/0.004/0.011; Advection 0.020/0.010/0.019; Darcy 0.007/0.012/0.012; NS 0.026/0.026/0.025. Robust for smoothing operators (Darcy, NS), less so for advection and Burgers.

**Loss choice** (§6.5): training with relative $L^2$ gives about half the test error of MSE.

**Overall ranking** (§7.4): FNO best overall and the only method to capture NS; LNO best of GNO/LNO/MGNO on 1-D Burgers; GNO and MGNO suffer from sampling.

## Limitations

As stated by the authors (§9, §10, pp.53-59):
- Theory covers integral-operator layers with $P$, $Q$, $W$ trivial and reduces to linear approximation; it does not capture nonlinear approximation or the benefit of depth (pp.26, 58-59). FNO itself is outside the theory.
- Parameter growth with accuracy is not studied; it may be super-exponential in general (Kovachki et al. 2021), though some operator classes beat the curse of dimensionality (Lanthaler et al. 2021).
- Data discretization error, finite-data (ERM) error and optimization error are not analysed; only the architecture's approximation error is (pp.53, 57).
- The full $O(J^2)$ integration still beats FNO by about 40% on one comparison, at greater cost (p.58). Wiki note: this sentence is not tied to a specific table in the text I read.
- FNO needs a uniform grid (or padding/continuation); GNO/MGNO are quadratic or sampling-limited.
- Supervised only; combination with solvers and physics constraints is left to future work (p.58).

Wiki note: the benchmark PDEs are all smooth-solution, mostly periodic or simple-domain problems; the authors themselves attribute FNO's lead partly to smoothness and uniform grids (p.57).

## Connections

- Journal version of the ICLR paper [[FNO (Li 2021)]]; reuses its FNO but retunes it (Burgers 0.0018 vs 0.0139-0.0160) and adds DeepONet baselines and the transformer/DeepONet special-case propositions.
- [[DeepONet]] ([[DeepONet (Lu 2021)]]) is shown to be a special case (Prop. 5), and the linear-vs-nonlinear approximation contrast is the authors' main conceptual argument against it.
- Priors $\mu=N(0,(-\Delta+\tau^2I)^{-\alpha})$ are [[Gaussian process]] / [[Karhunen-Loève expansion]] type measures; the review of continuous NNs and infinite-width GPs (§9) contrasts continuity in width/depth with continuity of the data domain. Wiki note: neither concept is developed in the paper.
- Later work: [[LNO (Cao 2023)]] (Laplace transform instead of Fourier basis; [[LNO]] is not discussed here, Wiki note: only related as a later alternative to the FNO basis) and the overview [[Operator learning review (Kovachki 2024)]].
- Benchmark PDEs: [[Darcy flow]], [[Burgers equation]], [[Navier-Stokes equations]]. General setting: [[Operator learning]], [[Neural operator]], [[Kernel integral operator]].

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf` (appendix proofs A-G not read in detail; theorem statements are from §8).
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural operator]]
- [[Operator learning]]
- [[Kernel integral operator]]
- [[Discretization invariance]]
- [[Universal approximation for operators]]
- [[Neural operator#Graph neural operator|graph neural operator]]
- [[Neural operator#Low-rank neural operator|low rank neural operator]]
- [[Neural operator#Multipole graph neural operator|multipole graph neural operator]]
- [[FNO]]
- [[DeepONet]]
- [[Discretization invariance#Zero-shot super-resolution|zero shot super resolution]]
- [[Darcy flow]]
- [[Burgers equation]]
- [[Navier-Stokes equations]]
- [[Gaussian process]]
- [[Karhunen-Loève expansion]]
- [[LNO]]
- [[FNO (Li 2021)]]
- [[DeepONet (Lu 2021)]]
- [[LNO (Cao 2023)]]
- [[Operator learning review (Kovachki 2024)]]
