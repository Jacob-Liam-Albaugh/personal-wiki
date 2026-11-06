---
type: paper
area: operators
areas: [operators, ml, math]
source-ref: "Kovachki, Lanthaler, Stuart 2024, arXiv:2402.15715v1, §3-5"
tags: [paper, operators, ml]
authors: [Kovachki, Lanthaler, Stuart]
year: 2024
venue: "arXiv:2402.15715v1 [cs.LG], 24 Feb 2024 (dated 27 Feb 2024); review article"
file: "Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf"
---

# Operator Learning: Algorithms and Analysis (Kovachki 2024)

**Summary**: A review of [[Operator learning]] (supervised learning of maps between Banach spaces) that defines four architecture families (PCA-Net, DeepONet, FNO / neural operators, random features), states the universal approximation theorems, and then surveys quantitative error and sample complexity for linear, holomorphic and general Lipschitz operators. Its central negative result is the [[Curse of parametric complexity]]: for general Lipschitz or Frechet-differentiable operators, standard architectures need model size exponential in $\varepsilon^{-1}$.

**Authors**: Nikola B. Kovachki, Samuel Lanthaler, Andrew M. Stuart · **Year**: 2024 · **File**: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`

Wiki note: the file name lists only Stuart (and misspells "Learning"); the PDF's first author is Kovachki, so the slug is kovachki-2024-operator-learning-review. The paper gives no published venue, only the arXiv stamp. Pages cited below are the PDF's own page numbers.

---

## Problem

(source: Stuart - Operator Leraning - Algorithms and Analysis.pdf, §1-2, pp. 1-6)

- View high-dimensional tensors (pixellated images, discretized fields) as functions $u:D\to\mathbb{R}^c$, design the algorithm in the continuum limit $N\to\infty$, then discretize. Models then transfer between resolutions (p. 1-2, Figs. 1-2); this is the motivation for [[Discretization invariance]].
- Supervised learning of an operator $\Psi^\dagger:U\to V$ from samples $\{u_n,\Psi^\dagger(u_n)\}_{n=1}^N$, $u_n\sim\mu$, with $U,V$ separable Banach spaces of vector-valued functions (eq. 2.1, p. 4).
- Goal of the review: the approximation-theoretic state of the art. How many parameters, and how many samples, give accuracy $\varepsilon$, and what structure reduces the cost (p. 4).

> [!definition] Training and testing
> Given a parametrized family $\Psi:U\times\Theta\to V$, $\Theta\subseteq\mathbb{R}^p$, and an error or relative-error measure $r$ (e.g. $r(v_1,v_2)=\|v_1-v_2\|_{V'}/(\varepsilon+\|v_1\|_{V'})$):
> $$\theta^\ast=\arg\min_\theta R_N(\theta),\quad R_N(\theta)=\mathbb{E}_{u\sim\mu_N}\big[r(\Psi^\dagger(u),\Psi(u;\theta))^q\big],\quad \mu_N=\tfrac1N\sum_n\delta_{u_n},$$
> population risk $R_\infty(\theta)=\mathbb{E}_{u\sim\mu}[r(\Psi^\dagger(u),\Psi(u;\theta))^q]$, typically $q=1$. Test error uses an independent measure $\mu'$ on the support of $\mu$.
>
> (source: Stuart - Operator Leraning - Algorithms and Analysis.pdf, §2.3, pp. 4-5)

> [!definition] Latent structure (encoder-decoder pairs)
> Encoder/decoder pairs $G_U\circ F_U\approx I_U$ and $G_V\circ F_V\approx I_V$, with a finite-dimensional map $\varphi$ chosen so that $G_V\circ\varphi\circ F_U\approx\Psi^\dagger$ (Fig. 3). Equivalently $\varphi=F_V\circ\Psi^\dagger\circ G_U:\mathbb{R}^{d_U}\to\mathbb{R}^{d_V}$ (p. 20). See [[Encoder-decoder operators]].
>
> (source: same file, §2.4, p. 5; §5.3.1, p. 20)

Running example (p. 6): Darcy flow $-\nabla\cdot(a\nabla v)=f$ on $D\subset\mathbb{R}^2$, $v=0$ on $\partial D$, operator $a\mapsto v$ from a subset of $L^\infty(D)$ into $H^1_0(D)$. For separability the input space is taken as $L^2(D)$ with the measure supported on $a$ with a positive lower bound and a finite upper bound.

## Method: taxonomy of architectures (§3, pp. 7-11)

The review sorts architectures along two axes: (i) encoder-decoder-net vs neural operator layer-structure, and (ii) linear vs nonlinear approximation of the output.

### Encoder-decoder-nets: [[PCA-Net]] and [[DeepONet]]

> [!definition] PCA-Net
> $U,V$ Hilbert spaces, $\mu$ on $U$. Encoder: projection onto the first $d_U$ PCA basis functions $\{\phi_j\}$ of the input covariance, $F_U(u)=Lu=\{\langle\phi_j,u\rangle\}_{j=1}^{d_U}$. Decoder: expansion in the first $d_V$ PCA functions $\{\psi_j\}$ of the pushforward $\Psi^\dagger_\#\mu$, $G_V(\alpha)=\sum_{j=1}^{d_V}\alpha_j\psi_j$. With a neural network $\alpha(\cdot;\theta):\mathbb{R}^{d_U}\to\mathbb{R}^{d_V}$,
> $$\Psi_{PCA}(u;\theta)(y)=\sum_{j=1}^{d_V}\alpha_j(Lu;\theta)\,\psi_j(y).$$
> PCA bases are computed from the empirical measure $\mu_N$ and its pushforward.
>
> (source: Stuart - Operator Leraning - Algorithms and Analysis.pdf, §3.1, p. 7)

> [!definition] DeepONet
> Encoder: a general linear map $F_U(u)=Lu$ (PCA coefficients, or point values $u(x_\ell)$ at sensor points; active subspaces are another option). Decoder: expansion in a neural-network basis $\psi:D_y\times\Theta_\psi\to\mathbb{R}^{d_V}$. With branch net $\alpha$ and trunk net $\psi$ (real-valued case):
> $$\Psi_{DEEP}(u;\theta)(y)=\sum_{j=1}^{d_V}\alpha_j(Lu;\theta_\alpha)\,\psi_j(y;\theta_\psi),\quad \theta=\{\theta_\alpha,\theta_\psi\}.$$
>
> (source: same file, §3.2, pp. 7-8)

### Neural operators: [[FNO]] and general [[Neural operator]]

> [!definition] FNO
> Domain $D_x=[0,2\pi]^d$ identified with the torus.
> $$\Psi_{FNO}(u;\theta)=Q\circ L_L\circ\cdots\circ L_1\circ R(u),\quad L_\ell(v)(x)=\sigma\big(W_\ell v(x)+b_\ell+K(v)(x;\gamma_\ell)\big),$$
> $R,Q$ pointwise shallow nets or linear maps. $K$ is a convolution, evaluated as a Fourier multiplier:
> $$K(v)(x;\gamma_\ell)=\int_{D_x}\kappa(x-y;\gamma_\ell)v(y)\,dy=\mathcal{F}^{-1}\big(\mathcal{F}(\kappa)\,\mathcal{F}(v)\big),$$
> $$[K(v)_i](x)=\frac{1}{(2\pi)^d}\sum_{k\in\mathbb{Z}^d}\Big(\sum_{j=1}^{d_c}\hat\kappa_{k,ij}\mathcal{F}(v_j)(k)\Big)e^{ik\cdot x}.$$
> Truncation $|k|_{\ell^\infty}\le k_{\max}$ leaves finitely many parameters $\gamma_\ell=\{\hat\kappa_{k,ij}\}$. Hyperparameters: width $d_c$, cutoff $k_{\max}$, depth $L$, and $R,Q$.
>
> (source: same file, §3.3, pp. 8-9)

> [!definition] General neural operator (eq. 4.2)
> Same layer form as FNO, but the convolution is replaced by a general [[Kernel integral operator]] $K(v)(x;\gamma)=\int_D\kappa(x,y;\gamma)v(y)\,dy$ with matrix-valued kernel; nonlinear dependence $\kappa(x,y,u(x),u(y);\gamma)$ is allowed (transformer-like). Implementations differ mainly in the kernel: Fourier basis [FNO], wavelets, spherical harmonics, restricted support, or fast-decaying kernels (p. 14).
>
> (source: same file, eq. 4.2, p. 14)

### Random features: [[Random features model]]

> [!definition] Random feature model (RFM)
> Parametrized operator $\psi:U\times\Gamma\to V$ and a measure $\nu$ on $\Gamma$. Draw $\gamma_1,\dots,\gamma_M\sim\nu$ i.i.d. and keep them fixed:
> $$\Psi_{RFM}(u;\theta)(y)=\sum_{j=1}^M\theta_j\,\psi(u;\gamma_j)(y).$$
> Only $\theta\in\mathbb{R}^M$ is trained, so with conventional losses the problem is convex with a unique minimizer. Original work uses Fourier-space features $\psi(u;\gamma)=\sigma(\mathcal{F}^{-1}(\chi F_\gamma\mathcal{F}u))$ with $\gamma$ drawn from a Gaussian random field.
>
> (source: same file, §3.4, pp. 9-10)

### The paper's own taxonomy (§3.5, pp. 10-11)

- **Encoder-decoder-net** (PCA-Net, DeepONet): encode to a finite-dimensional vector, apply an ordinary network, decode. Mirrors FEM/FVM/FD structure (Table 1: encoding / finite-dim map / reconstruction). Output always lies in a fixed finite-dimensional *linear* subspace of $V$, so it is *linear approximation*. FNO and random features have outputs on a *nonlinear manifold*.
- **Neural operators generalizing network structure** (FNO): keep alternating affine / nonlinear layers on function space; the integral-kernel affine layer supplies the nonlocality needed for universality.
- **Optimization and randomization**: the RFM can be combined with any architecture and permits error analysis that accounts for finite samples, finite parameters and optimization [ref. 76]; designing efficient random features is called largely open. Related: kernel methods in the encoder-decoder paradigm [ref. 12, Batlle et al.].
- Other approaches mentioned, not analysed: nonlinear reduced-order models, Koopman, solver augmentation, closure modeling (p. 11).

| Family | Encoder | Finite-dim map | Output space | Approximation type |
|---|---|---|---|---|
| PCA-Net | PCA projection (data-driven) | NN | PCA basis | linear |
| DeepONet | general linear $L$ (sensors, PCA, ...) | branch NN | NN trunk basis | linear (for fixed trunk) |
| FNO / neural operator | pointwise lift $R$ | none (layers act on functions) | nonlinear manifold | nonlinear |
| RFM | any | convex least squares in $\theta$ | span of random features | nonlinear in $u$ |

## Results: approximation theorems (§4-5)

### Universality (§4, pp. 11-16)

Universality is "the ability to approximate a wide class of operators to any given accuracy in the absence of any constraints on model size, data, or optimization" (p. 11). See [[Universal approximation for operators]].

> [!theorem] Thm 4.1: encoder-decoder-nets are universal
> Let $U,V$ be separable Banach spaces *with the approximation property*, $\Psi^\dagger:U\to V$ continuous, $K\subset U$ compact. For every $\epsilon>0$ there exist $d_U,d_V\in\mathbb{N}$, bounded linear maps $F_U:U\to\mathbb{R}^{d_U}$, $G_V:\mathbb{R}^{d_V}\to V$, and $\alpha\in C(\mathbb{R}^{d_U};\mathbb{R}^{d_V})$ with
> $$\sup_{u\in K}\|\Psi^\dagger(u)-(F_U\circ\alpha\circ G_V)(u)\|_V\le\epsilon.$$
> (The paper prints the composition in this order; read as $G_V\circ\alpha\circ F_U$.) The approximation property holds for Lebesgue, Sobolev, Besov and $C^k$ spaces.
>
> (source: same file, Thm 4.1, p. 12; the PDF cites [68, Lemma 22])

> [!theorem] Thm 4.2: Chen-Chen operator network (basis of DeepONet)
> $\sigma\in C(\mathbb{R})$ non-polynomial, $D\subset\mathbb{R}^d$ compact with Lipschitz boundary, $\Psi^\dagger:C(D)\to C(D)$ continuous, $K\subset C(D)$ compact. For every $\varepsilon>0$ there are $d_U,d_V,N$, sensor points $x_1..x_{d_U}\in D$ and coefficients such that
> $$\sup_{u\in K}\sup_{x\in D}\Big|\Psi^\dagger(u)(x)-\sum_{k=1}^{d_V}\sum_{i=1}^{N}c_i^k\,\sigma\Big(\sum_{j=1}^{d_U}\xi_{ij}^k u(x_j)+b_i\Big)\sigma(\omega_k x+\zeta_k)\Big|\le\varepsilon.$$
> Identification: linear encoder $Lu=(u(x_j))_j$, shallow branch net $\alpha_k$, trunk $\psi_k(y)=\sigma(\omega_k y+\zeta_k)$. (Remark 4.3: also valid for $C(V)\to C(D)$ with $V$ a compact subset of a Banach space.)
>
> (source: same file, Thm 4.2, p. 13; Chen & Chen 1995, Thm 5)

Extensions listed (pp. 13-14): input measure $\mu$ with possibly unbounded support, error in Bochner $L^2(\mu)$ [ref. 74 in the PDF]; discretization-invariant encoders (BelNet, VIDON); Basis Operator Network; MIO-Net for multiple inputs; DeepONets on abstract Hilbert spaces.

> [!theorem] Thm 4.4: PCA-Net universality
> $U,V$ separable Hilbert spaces, $\mu\in\mathcal{P}(U)$, $\Psi^\dagger$ $\mu$-measurable with $\mathbb{E}_\mu\|u\|_U^2<\infty$ and $\mathbb{E}_\mu\|\Psi^\dagger(u)\|_V^2<\infty$. For every $\varepsilon>0$ there are $d_U,d_V$, an amount of data $N$ and a network $\psi$ (depending on the data) such that
> $$\mathbb{E}_{\{u_j\}\sim\mu^{\otimes N}}\Big[\mathbb{E}_{u\sim\mu}\|\Psi^\dagger(u)-\Psi(u;\{u_j\})\|_V^2\Big]<\varepsilon,$$
> where the outer expectation is over the i.i.d. samples that determine the empirical PCA encoder and decoder.
>
> (source: same file, Thm 4.4, p. 14; the PDF cites [72, Prop. 31])

> [!definition] Averaging neural operator (ANO)
> $$L(v;\gamma_\ell)(x)=\sigma\Big(W_\ell v(x)+A_\ell x+c_\ell+V_\ell\int_D v(y)\,dy\Big),$$
> with $W_\ell,V_\ell\in\mathbb{R}^{d_c\times d_c}$, bias $b_\ell(x)=A_\ell x+c_\ell$; input/output layers are matrices $R\in\mathbb{R}^{d_c\times d_i}$, $Q\in\mathbb{R}^{d_o\times d_c}$. It is FNO with a *constant* kernel.
>
> (source: same file, §4.2.1, p. 15)

> [!theorem] Thm 4.5 and Cor. 4.6: universality of neural operators
> Thm 4.5: $\sigma\in C(\mathbb{R})$ non-polynomial, $D\subset\mathbb{R}^d$ compact with Lipschitz boundary, $\Psi^\dagger:C(D)\to C(D)$ continuous, $K\subset C(D)$ compact. For every $\varepsilon>0$ there is an ANO $\Psi$ with $\sup_{u\in K}\|\Psi^\dagger(u)-\Psi(u)\|_{C(D)}<\varepsilon$.
> Cor. 4.6: any neural operator of form (4.2) is universal in this sense if, for every channel dimension $d_c$ and matrix $V\in\mathbb{R}^{d_c\times d_c}$, some parameter $\gamma_V$ gives $\kappa(x,y;\gamma_V)\equiv V$. This covers FNO.
>
> (source: same file, Thm 4.5, Cor. 4.6, p. 15; the PDF credits [73])

Intuition (p. 16, Fig. 5): a two-layer ANO is a *nonlinear* encoder $\alpha(u)=\int_D\phi(u(y),y)\,dy$ followed by a nonlinear decoder $\Psi(u)(x)=\psi(\alpha(u),x)$, which gives a route to universality for any architecture containing an ANO.

### Linear operators (§5.1, pp. 17-18)

> [!theorem] Thm 5.1: rate for learning a linear operator from noisy data
> Setting: $\Psi^\dagger=L^\dagger$ linear on a separable Hilbert space $U=V$, diagonal in a known Schauder basis $\{\varphi_j\}$ with eigenvalues $l^\dagger_j$; data $v_n=L^\dagger u_n+\gamma\xi_n$, $u_n\sim\mathcal{N}(0,\Gamma)$ i.i.d., $\xi_n\sim\mathcal{N}(0,I_U)$ white noise independent of the inputs, $\Gamma$ strictly positive and diagonal in $\{\varphi_j\}$; Gaussian prior $l_j\sim\mathcal{N}(0,\sigma_j^2)$; estimator = posterior mean
> $$l_j=\frac{\gamma^{-2}\sigma_j^2\sum_{n}v_{jn}\langle\varphi_j,u_n\rangle}{1+\gamma^{-2}\sigma_j^2\sum_n\langle\varphi_j,u_n\rangle^2},$$
> truth in a weighted space $\sum_j j^{2s}|l^\dagger_j|^2<\infty$. Assume $\langle\varphi_j,\Gamma\varphi_j\rangle\asymp j^{-2\alpha}$ with $\alpha>1/2$, $\sigma_j^2\asymp j^{-2p}$, $\alpha'\in[0,\alpha+1/2)$ and $\min\{\alpha,\alpha'\}+\min\{p-1/2,s\}>0$. Then as $N\to\infty$
> $$\mathbb{E}\sum_{j=1}^\infty j^{-2\alpha'}|l_j-l^\dagger_j|^2\lesssim N^{-\frac{\alpha'+\min\{p-1/2,\,s\}}{\alpha+p}},$$
> i.e. $N\sim\epsilon^{-\frac{\alpha+p}{\alpha'+\min\{p-1/2,s\}}}$ samples for squared-weighted-$\ell^2$ error $\epsilon$.
>
> (source: same file, Thm 5.1, pp. 17-18; the PDF cites [36, Thm 1.3], de Hoop-Kovachki-Nelsen-Stuart)

Noise is essential: without it all eigenvalues follow from one sample via $l_j^\dagger=v_{j1}/\langle\varphi_j,u_1\rangle$ (p. 17). The cited source also treats the case without simultaneous diagonalizability of $L^\dagger$ and $\Gamma$.

### Holomorphic operators (§5.2, pp. 18-20)

> [!definition] $(b,\varepsilon)$-holomorphic parametrized operator
> For $b\in[0,\infty)^{\mathbb{N}}$ and $\varepsilon>0$, a map $F:[-1,1]^{\mathbb{N}}\to V$ (e.g. $F(y)=\Psi^\dagger(a(\cdot;y))$ with $a(x;y)=\bar a(x)+\sum_j y_j\varphi_j(x)$) is $(b,\varepsilon)$-holomorphic if it has a holomorphic extension $F:\prod_j\mathcal{E}_{\rho_j}\to V_{\mathbb{C}}$ (Bernstein ellipses $\mathcal{E}_{\rho_j}=\{\tfrac12(z+z^{-1}):1\le|z|\le\rho_j\}$) for every $\rho\in[1,\infty)^{\mathbb{N}}$ with
> $$\sum_{j=1}^\infty\Big(\frac{\rho_j+\rho_j^{-1}}{2}-1\Big)b_j\le\varepsilon.$$
>
> (source: same file, eqs. 5.1-5.2, p. 19)

Results stated (pp. 19-20):
- For $b\in\ell^p(\mathbb{N})$, $0<p<1$ (e.g. $b_j\sim j^{-s}$ with $s>p^{-1}>1$): best $n$-term polynomial approximation converges at rate $n^{1-1/p}$ in sup norm and $n^{1/2-1/p}$ in Bochner $L^2(\mu)$ (Cohen-DeVore Cor. 3.11). These rates are dimension-independent for finitely many inputs, so they beat the curse of dimensionality.
- ReLU DeepONets (Riesz-frame encoders/decoders) reach rates arbitrarily close to $n^{1-s}$ (sup norm) and $n^{1/2-s}$ ($L^2(\mu)$), $n$ = number of parameters, $s$ the frame-coefficient decay [ref. 52 in the PDF]; with $s\sim 1/p$ this recovers the $n$-term rates.
- Sample complexity: on $(b,\varepsilon)$-holomorphic operators in a Bochner $L^2$ setting, no method using $N$ samples can beat $N^{1/2-1/p}$; the optimal rate is attainable up to logarithmic factors ([6,7] in the PDF, Adcock-Dexter-Moraga).
- Wiki note: non-holomorphic examples named by the authors include solution operators of nonlinear hyperbolic conservation laws (compressible Euler, shocks) (p. 20).

### General Lipschitz operators: error decomposition and the curse (§5.3, pp. 20-27)

> [!theorem] Error decomposition for encoder-decoder-nets
> With pairs $(F_U,G_U)$ on $U$ and $(F_V,G_V)$ on $V$ and $\varphi=F_V\circ\Psi^\dagger\circ G_U$, the network $\psi\approx\varphi$:
> $$\mathcal{E}\lesssim\mathcal{E}_U+\mathcal{E}_\psi+\mathcal{E}_V,$$
> $$\mathcal{E}_U=\sup_u\|u-G_U\circ F_U(u)\|_U,\quad \mathcal{E}_V=\sup_v\|v-G_V\circ F_V(v)\|_V,$$
> $$\mathcal{E}_\psi=\sup_\alpha\|F_V\circ\Psi^\dagger\circ G_U(\alpha)-\psi(\alpha)\|\quad(5.3).$$
> Encoding/reconstruction errors for linear pairs amount to PCA (Bochner $L^2_\mu$ norm) or Kolmogorov $n$-widths (sup norm over a compact set).
>
> (source: same file, §5.3.1, pp. 20-21; error splitting credited to [14] and [74] in the PDF)

> [!theorem] Thm 5.2 (Yarotsky): ReLU approximation of smooth functions
> $f\in W^{k,\infty}([0,1]^d)$ can be approximated to uniform accuracy $\varepsilon$ by a ReLU network with at most $O(\varepsilon^{-d/k}\log(\varepsilon^{-1}))$ parameters. Remark 5.3: the relevant dimension is the latent one $d_U$, so each component of $G:\mathbb{R}^{d_U}\to\mathbb{R}^{d_V}$ costs $O(\varepsilon^{-d_U/k})$ and $\psi$ has size $O(d_V\varepsilon^{-d_U/k})$.
>
> (source: same file, Thm 5.2, Rem. 5.3, p. 22)

Back-of-envelope chain behind the curse (pp. 23-24). Assume algebraic decay of encoding and reconstruction errors,
```
E_U <~ d_U^(-alpha)   (5.4)
E_V <~ d_V^(-beta)    (5.5)
size(psi) ~ d_V eps^(-d_U/k)   (5.6)
```
Requiring each error $\le\varepsilon$ forces $d_U\sim\varepsilon^{-1/\alpha}$, $d_V\sim\varepsilon^{-1/\beta}$. Substituting,
```
size(psi) ~ eps^(-1/beta) * eps^(-c eps^(-1/alpha) / k)
size(psi) >~ exp( c eps^(-1/alpha) / k )        (5.7)
```
and for inputs on a $d$-dimensional domain with $s$ bounded derivatives, $\alpha=s/d$, giving $\text{size}(\psi)\gtrsim\exp(c\,\varepsilon^{-d/s}/k)$ (5.8). The authors say that for operator learning this super-algebraic dependence has been called the "curse of dimensionality" [67, 74 in the PDF] and, more recently, the "curse of parametric complexity" [72 in the PDF], the later name chosen because there is no fixed dimension to speak of. It is an infinite-dimensional scaling limit of the finite-dimensional curse: the latent dimension $d_U$ itself grows as $\varepsilon^{-1/\alpha}$. Even $d_U\sim\log(\varepsilon^{-1})$ would still give super-algebraic size.

> [!theorem] Nonlinear $n$-width lower bound (Mhaskar-Hahm [97], simplified)
> Continuous nonlinear $n$-width $d_n(K;\|\cdot\|_X)=\inf_{(a,M)}\sup_{f\in K}\|f-M(a(f))\|_X$ over continuous $a:K\to\mathbb{R}^n$ and general $M:\mathbb{R}^n\to X$. Let $\mathcal{F}_d=\{\Psi^\dagger:L^2([-1,1]^d)\to\mathbb{R}:\|\Psi^\dagger\|_{Lip}\le1\}$ with $\|\Psi^\dagger\|_{Lip}=\sup_u|\Psi^\dagger(u)|+\sup_{u\ne v}|\Psi^\dagger(u)-\Psi^\dagger(v)|/\|u-v\|_{L^2}$, and $K_s=\{f:\sum_{k\in\mathbb{N}^d}|k|^{2s}|\hat f_k|^2\le1\}$ (Legendre coefficients $\hat f_k$). Then in $C(K_s)$
> $$d_n(\mathcal{F}_d)\sim\log(n)^{-s/d},$$
> so uniform accuracy $\varepsilon$ with a continuous encoder/decoder pair needs
> $$n\gtrsim\exp\big(c\,\varepsilon^{-d/s}\big)\quad(5.9).$$
>
> (source: same file, §5.3.3, pp. 24-25; Mhaskar & Hahm 1997)

This matches (5.8) for $k=1$ only if the architecture is fixed and the map $\Psi^\dagger\mapsto\theta_{\Psi^\dagger}$ is continuous; the authors note this continuity may fail when parameters are fit by gradient descent (p. 25).

> [!theorem] Prop. 5.4: curse of parametric complexity for DeepONet
> $D\subset\mathbb{R}^d$ a domain, $k\in\mathbb{N}$, $K=\{u\in C^k(D):\|u\|_{C^k}\le1\}\subset U:=C(D)$, $\alpha>2+k/d$. For every $r\in\mathbb{N}$ there is an $r$-times Frechet-differentiable functional $\Psi^\dagger:U\to\mathbb{R}$ and constants $c,\bar\varepsilon>0$ (depending only on $k,\alpha,r$) such that, for $\varepsilon\le\bar\varepsilon$, any ReLU DeepONet $\Psi:U\to\mathbb{R}$ with linear encoder $E$ and network $\psi$ satisfying
> $$\sup_{u\in K}|\Psi^\dagger(u)-\Psi(u)|\le\varepsilon\quad(5.10)$$
> must have
> $$\text{size}(\psi)\ge\exp\big(c\,\varepsilon^{-1/\alpha r}\big)\quad(5.11).$$
>
> (source: same file, Prop. 5.4, pp. 25-26; the PDF says it follows from [78, Example 2.17])

Notes from the text (p. 26): this rules out escaping the curse by (a) a discontinuous weight assignment or (b) an adaptively chosen architecture, for standard architectures on the full class of Lipschitz or Frechet-differentiable operators; analogous bounds are stated for PCA-Net, FNO and others (details in [78]); the more general version covers Sobolev inputs. Remark 5.5: the exponent was not optimized; the appearance of $r$ may be an artifact, and the heuristic (5.7) suggests $\alpha=k/d+2+\delta$ could be $k/d+\delta$.

Escape routes noted (pp. 22, 26): networks with hyperexpressive (non-standard) activations or "three-dimensional" connectivity can break the curse in parameter *count*, but necessarily at the cost of parameter bit-precision (total bits are lower-bounded by the Kolmogorov $\varepsilon$-entropy, $\sim\varepsilon^{-d/k}$ for $W^{k,\infty}([0,1]^d)$), and the architectures are very sensitive to parameter perturbations. With such architectures, DeepONets achieve algebraic expression rates for general Lipschitz and Holder operators [ref. 123 in the PDF].

### Sample complexity for Lipschitz operators (§5.3.4, pp. 26-28)

> [!theorem] Generalization bound, fixed trigonometric encoder/decoder (simplified [90, Cor. 3])
> $\Psi^\dagger:U\to V$ Lipschitz, $U=V=L^2([-1,1]^d)$; $\mu$ and $\Psi^\dagger_\#\mu$ supported on periodic functions in $K=\{u:\|u\|_{C^{k,\alpha}}\le C\}$. With $N$ samples, $s=k+\alpha$, $\mathcal{E}^2:=\mathbb{E}_{data}\mathbb{E}_{u\sim\mu}\|D_Y\circ\psi\circ E_X(u)-\Psi^\dagger(u)\|^2_{L^2}$,
> $$\mathcal{E}^2\lesssim d_V^{\frac{4+d_U}{2+d_U}}\,N^{-\frac{2}{2+d_U}}\log^6(n)+d_U^{-2s/d}+d_V^{-2s/d}\quad(5.12),$$
> for a ReLU network $\psi$ of depth $L$ and width $p$ with, up to log terms, $Lp\sim (d_V/d_U)^{\cdot}N^{\frac{d_U}{4+2d_U}}$ (the extraction of this display is garbled; the $N$ exponent $d_U/(4+2d_U)$ is clear, the $d_V,d_U$ prefactor exponent is **[unverified]**, see p. 27). The last two terms are encoding/reconstruction error; the first combines network approximation and generalization error.
>
> (source: same file, eq. 5.12, p. 27; the PDF cites [90, Corollary 3])

Consequence (p. 27): to get $\mathcal{E}\le\varepsilon$ choose $d_U,d_V\sim\varepsilon^{-d/s}$ and then $N\sim\varepsilon^{-(2+d_U)/2}$, hence
$$N\gtrsim\exp\big(c\,\varepsilon^{-d/s}\big),\qquad Lp\gtrsim\exp\big(c\,\varepsilon^{-d/s}\big),$$
so the curse shows up as an exponential *sample* complexity, consistent with (5.7). The authors think [90] likely cannot be substantially improved for Lipschitz operators. Also cited (pp. 27-28): Rademacher complexity and generalization bounds for FNO [ref. 62 in the PDF]; out-of-distribution risk bounds for the Helmholtz equation [ref. 13, Benitez et al.]; noisy data need $d_V\gtrsim\sqrt n$ trunk functions [ref. 100].

### Structure beyond smoothness (§5.4, pp. 28-29)

- Operator Barron spaces (Barron 1993, generalized to infinite dimensions in [64]): Monte-Carlo rate $O(1/\sqrt n)$ by shallow neural operators, but it is unclear which practical operators lie in the class. Operator RKHS in the random feature model has analogous rates [ref. 76].
- Explicit representation (e.g. Cole-Hopf for viscous Burgers) and emulation of numerical methods give $\text{size}(\psi)=O(\varepsilon^{-\gamma})$ or $O(|\log\varepsilon|^\gamma)$ for specific PDEs: Darcy, Navier-Stokes, reaction-diffusion, inviscid Burgers, for DeepONet/FNO/PCA-Net.
- Discussion (p. 29): conjecture that, for a suitable definition of numerical algorithm, networks can efficiently emulate any numerical algorithm, so only operators with no efficient numerical algorithm are excluded. This is stated as a conjecture, not a result.

## Limitations

As stated by the authors (pp. 29-30):
- Theoretical understanding of neural operators remains incomplete; universality is qualitative and necessary but not sufficient.
- Results beating the curse are case-by-case and often rely on emulating numerical schemes; a general characterization of exploitable structure is "one of the great challenges".
- The Lipschitz lower bound (Prop. 5.4) leaves open whether $r$ in the exponent is an artifact (Rem. 5.5); the practical efficiency of operator Barron spaces is unclear; how to design efficient random features is open.
- Whether smoothness alone decides practical success is left open (p. 28).

Wiki notes (labelled): the review's scope is approximation and sample complexity, so optimization error is out of scope except via the RFM; it does not cover the Laplace/wavelet/graph variants beyond a one-line mention, so [[LNO]] is not discussed; expected sizes in (5.7)-(5.8) are heuristic upper-bound arguments, while the rigorous lower bounds are (5.9) and Prop. 5.4.

## Connections

- Survey companion to [[Neural operator (Kovachki 2022)]] (the long neural-operator paper it cites as [68]; its Lemma 22 gives Thm 4.1) and to [[FNO (Li 2021)]] (the FNO definition in §3.3). Basic DeepONet architecture and universality background in [[DeepONet (Lu 2021)]].
- Explains why many architectures in this wiki (e.g. [[LNO (Cao 2023)]]) work empirically on PDE operators even though general Lipschitz operators suffer the curse: those PDE operators carry structure (holomorphy, explicit formulas).
- Defines the linear-vs-nonlinear approximation distinction that separates DeepONet/PCA-Net from FNO/[[Random features model]].
- [[Gaussian process]] link: Thm 5.1 uses a Gaussian prior over eigenvalues and Gaussian input measure, so the estimator is a Gaussian posterior mean; the review also relates the RFM to kernel methods (p. 11).

**Sources**: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Operator learning]]
- [[Neural operator]]
- [[FNO]]
- [[DeepONet]]
- [[PCA-Net]]
- [[Random features model]]
- [[Kernel integral operator]]
- [[Discretization invariance]]
- [[Encoder-decoder operators]]
- [[Universal approximation for operators]]
- [[Curse of parametric complexity]]
- [[Gaussian process]]
- [[FNO (Li 2021)]]
- [[Neural operator (Kovachki 2022)]]
- [[DeepONet (Lu 2021)]]
- [[LNO (Cao 2023)]]
