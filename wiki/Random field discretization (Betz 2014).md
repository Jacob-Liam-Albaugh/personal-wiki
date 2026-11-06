---
type: paper
area: stochastic
areas: [stochastic, math]
source-ref: "Betz, Papaioannou, Straub 2014, CMAME 271, §2-3, eq. 5-20"
tags: [uq, gp]
authors: ["[[Wolfgang Betz]]", "[[Iason Papaioannou]]", "[[Daniel Straub]]"]
year: 2014
venue: "Computer Methods in Applied Mechanics and Engineering 271, 109-129"
file: "papers/Stochastic Methods/Betz, Papaioannou, Straub - Karhunen-Loève Expansion for Discretization of RFs.pdf"
---

# Random field discretization (Betz 2014)

**Summary**: Compares numerical ways to solve the Fredholm integral eigenvalue problem behind the [[Karhunen-Loève expansion]] of a random field on an arbitrary domain: Nyström, collocation, and Galerkin (finite element and a proposed finite cell method). Shows that the EOLE method is a special case of Nyström with equal weights, and finds EOLE cheapest to set up while FEM and FCM are cheapest to evaluate.

**Authors**: Wolfgang Betz, Iason Papaioannou, Daniel Straub · **Year**: 2014 · **File**: `papers/Stochastic Methods/Betz, Papaioannou, Straub - Karhunen-Loève Expansion for Discretization of RFs.pdf`

---

## Problem

Engineering models (soil, wind, snow, precipitation) need spatially varying uncertain inputs, which are random fields with infinitely many random variables. For computation the field must be reduced to finitely many ones, "random field discretization" (p. 109). The KL expansion is optimal in global mean square error among series expansions for a given number of terms (p. 110), but it needs eigenpairs of the covariance kernel, available in closed form only for special kernels on simple domains (p. 111). The paper treats arbitrary domains and arbitrary (non-stationary) covariance.

## Method

> [!definition] KL expansion of a random field (eq. 5-6, p. 111)
> $$H(x,\theta)=\mu(x)+\sum_{i=1}^\infty\sqrt{\lambda_i}\,\varphi_i(x)\,\xi_i(\theta)$$
> with $\xi_i$ standard uncorrelated and $(\lambda_i,\varphi_i)$ solving the Fredholm equation
> $$\int_\Omega \mathrm{Cov}(x,x')\,\varphi_i(x')\,dx'=\lambda_i\varphi_i(x).$$
> By [[Mercer's theorem]] the eigenvalues are nonnegative, the eigenfunctions orthonormal and complete in $L^2(\Omega)$, and the kernel expands uniformly. For a Gaussian field the $\xi_i$ are independent standard normals; otherwise their joint law is "almost impossible to obtain" (p. 111).
>
> (source: Betz, Papaioannou, Straub - Karhunen-Loève Expansion for Discretization of RFs.pdf, eq. 5-6)

Truncation to $M$ terms (eq. 7-12, p. 112) gives
$$\mathrm{Var}[\tilde H(x)]=\sum_{i=1}^M\lambda_i\varphi_i(x)^2$$
and global mean square error
$$e_H^2=\int_\Omega\sigma^2(x)\,dx-\sum_{i=1}^M\lambda_i.$$
Consequences stated by the authors: the truncated field always underestimates the variance, and a truncated homogeneous field is only approximately homogeneous.

Non-Gaussian fields (§2.3, 2.5): translation fields $g(H)$ are discretized by applying $g$ to the KL expansion of the underlying Gaussian field, but optimality is not inherited (p. 112). Others combine KL with [[Polynomial chaos]] (Ghanem; Matthies-Keese, p. 112).

Numerical solution (§3, pp. 113-117). Approximate $\varphi_i\approx\sum_j d_j^ih_j(x)$ with basis functions $h_j$. The numerical expansion is no longer optimal, and the error formulas above no longer strictly hold (p. 113).

- **Nyström**: replace the integral by a quadrature with points $x_j$ and weights $w_j$. This gives the matrix problem
$$C W y_i=\hat\lambda_i y_i,\qquad C_{nj}=\mathrm{Cov}(x_n,x_j)$$
(eq. 17), symmetrised as $W^{1/2}CW^{1/2}$.
- **EOLE as Nyström**: with equal weights $w=|\Omega|/N$ the problem reduces to eigenpairs of the covariance matrix $C$, and the expansion
$$\hat H=\mu+\sum_i\hat\xi_i\frac1{\sqrt{\hat\lambda_i'}}\sum_j y_{i,j}\mathrm{Cov}(x,x_j)$$
(eq. 20) is the EOLE expansion of Li and Der Kiureghian 1993.
- **Collocation**: force the residual to zero at $P$ points; $P=N$ gives $A d=\hat\lambda Nd$, $P>N$ a quadratic eigenproblem (eq. 22-24).
- **Galerkin**: make the residual orthogonal to the basis. This gives the generalised problem $Bd=\hat\lambda Md$ with
$$b_{ln}=\iint h_l(x)\mathrm{Cov}(x,x')h_n(x')\,dx'dx,\qquad m_{ln}=\int h_lh_n$$
(eq. 26-28). Building $B$ is a double integral over the domain (six-fold in 3D); H-matrices can speed it up. FEM uses local piecewise polynomial bases on a mesh.
- **Finite cell method (FCM)**: the proposed variant; embed the domain in a simple shape, mesh that, use high-order hierarchic polynomials, and integrate carefully across the discontinuity at the true boundary (§3.5.3-3.5.4).
- Also compared: $H^{1/2}$-projection and discrete projection in place of $L^2$-projection.

## Results

- **Error measures** (§4.1, eq. 43-44): relative variance error $e_{\mathrm{Var}}$ and covariance error $e_{\mathrm{Cov}}$ averaged over the domain. $e_{\mathrm{Var}}=0$ does not imply $e_{\mathrm{Cov}}=0$.
- **Kernels** (§4.2): exponential, squared exponential and sine correlation, with correlation lengths $l_A,l_B,l_C$.
- **1D test** (§4.3): $\Omega=[0,1]$, $\sigma=1$, $M=10$, exponential kernel with $l_A=0.42385$ (chosen so the reference error is about 5%). The exponential kernel is non-differentiable on the diagonal, so quadrature needs care. $L^2$-projection gave errors orders of magnitude below $H^{1/2}$-projection; higher-order bases converged faster than piecewise linear (Fig. 5-6). Convergence in $e_{\mathrm{Cov}}$ is slower than in $e_{\mathrm{Var}}$.
- **2D complex domain** (§4.4): squared exponential and exponential kernels; costs compared for building the approximation and for evaluating realizations (pp. 121-127). Details not extracted here.
- **Conclusions** (§5, p. 127): EOLE is the cheapest to set up, needs no integration, and the authors call it the only truly meshless KL discretization. FEM and FCM evaluate realizations faster, which matters in finite element reliability analysis. Use FEM if a mesh exists, FCM if not. Collocation, $H^{1/2}$ and discrete projection showed no particular advantage.

## Limitations

As stated: the numerical KL loses optimality; error measures are not strictly valid for it; the FCM is involved to implement (discontinuous integrands, special basis). The paper restricts to scalar (univariate) fields and mostly Gaussian ones.

Wiki note: this is the practical companion to the theory in [[KL expansion note (Alexanderian 2015)]]. The Nyström step is what [[PIFT (Alberts 2023)]] uses for its 10-term KLE (see [[Karhunen-Loève expansion]]).

## Connections

- Theory and Mercer: [[KL expansion note (Alexanderian 2015)]]; closed-form Wiener case: [[KL expansions of the Wiener process (Deheuvels 2006)]].
- KL gives the Gaussian inputs of a [[Polynomial chaos]] expansion ([[Wiener-Askey chaos (Xiu 2002)]]).
- A Gaussian field is a [[Gaussian process]]; the covariance kernel is the GP kernel.

**Sources**: `papers/Stochastic Methods/Betz, Papaioannou, Straub - Karhunen-Loève Expansion for Discretization of RFs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Karhunen-Loève expansion]] · [[Mercer's theorem]] · [[Gaussian process]] · [[Polynomial chaos]]
- [[KL expansion note (Alexanderian 2015)]] · [[KL expansions of the Wiener process (Deheuvels 2006)]]
- [[PIFT (Alberts 2023)]] · [[Quantum option pricing KL (Prakash 2025)]]
