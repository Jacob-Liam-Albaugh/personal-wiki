---
type: paper
area: gp
areas: [gp, stochastic]
source-ref: "Greengard, O'Neil 2022, arXiv:2108.05924v2, Alg. 1-4, eqs. 1.10, 4.7-4.18"
tags: [gp, bayesian, mcmc]
authors: ["[[Philip Greengard]]", "[[Michael O'Neil]]"]
year: 2022
venue: "arXiv:2108.05924v2 [stat.CO], 24 Aug 2022"
file: "papers/Guassian Processes/Greengard, O'Neil - Efficient reduced-rank methods for Gaussian processes with eigenfunction expansions.pdf"
---

# Reduced-rank GPs (Greengard 2022)

**Summary**: Turns a GP on an interval (or rectangle) into its [[Karhunen-Loève expansion]], computed once by Nystrom quadrature of the covariance integral operator. GP regression then becomes ridge regression on $m$ fixed basis functions at cost $O(Nm^2)$ instead of $O(N^3)$. Works for non-translation-invariant kernels, and comes with a fast Bayesian hyperparameter algorithm. Practical in 1-3 dimensions.

**Authors**: Philip Greengard, Michael O'Neil · **Year**: 2022 · **File**: `papers/Guassian Processes/Greengard, O'Neil - Efficient reduced-rank methods for Gaussian processes with eigenfunction expansions.pdf`

---

## Problem

Direct [[Gaussian process]] regression with $N$ points costs $O(N^3)$ (p. 1). Reduced-rank methods replace the covariance $C$ by a rank-$m$ factor,
$$\|C-XX^\top\|<\epsilon,\quad X\in\mathbb R^{N\times m}.$$
Existing ones are rough (random Nystrom subsampling) or need assumptions on the kernel or data layout. Hierarchical solvers (Ambikasaran, Minden) need low-rank off-diagonal structure and are slow when it fails (p. 1-2).

## Method

**Why the KL basis.** Any order-$m$ expansion $f\approx\sum\alpha_i g_i$ with iid $N(0,1)$ coefficients has effective kernel $\sum_i g_i(x)g_i(y)$ (eq. 1.9). Among all such, the truncated KL expansion minimises the $L^2$ kernel error (eq. 1.10, citing Trefethen 2020):
$$k_{KL}=\arg\min_{k'}\iint (k-k')^2\,dx\,dy.$$

> [!theorem] Mercer (Thm 1)
> For continuous symmetric PSD $k$ on $[a,b]^2$, the integral operator $Kf(x)=\int k(x,x')f(x')dx'$ has real non-negative eigenvalues $\lambda_i$ and unit-norm eigenfunctions $u_i$, with
> $$k(x,x')=\sum_{i\ge1}\lambda_i u_i(x)u_i(x'),$$
> absolutely and uniformly convergent.
>
> (source: p. 4, eq. 2.6)

> [!theorem] Karhunen-Loève (Thm 2) and truncation (Thm 3)
> $$f(x)=\sum_i\alpha_iu_i(x),\quad \alpha_i\sim N(0,\lambda_i).$$
> With $\phi_i=\sqrt{\lambda_i}\,u_i$ the coefficients are iid $N(0,1)$. The order-$m$ sum is a GP with kernel $\sum_{i\le m}\lambda_iu_iu_i$. For smooth $k$ the $L^2$ error decays exponentially in $m$; for $k$ with $j$ continuous derivatives, no slower than $O(1/m^{j+1})$.
>
> (source: pp. 4-5, eqs. 2.7-2.15)

> [!algorithm] Algorithm 1: numerical KL expansion on $[-1,1]$
> 1. Gauss-Legendre nodes $x_i$, weights $w_i$; form $A_{ij}=\sqrt{w_iw_j}\,k(x_i,x_j)$.
> 2. Diagonalise $A=UDU^\top$; eigenvalues $\lambda_i$.
> 3. Rescale $\hat U_{ij}=U_{ij}/\sqrt{w_i}$.
> 4. Convert tabulated eigenvectors to Legendre coefficients.
> 5. Evaluate $u_i(x)$ by Legendre sums; set $\phi_i=\sqrt{\lambda_i}u_i$.
> 6. Use $\hat f=\sum_{i\le m}\alpha_i\phi_i$, $\alpha_i\sim N(0,I)$.
>
> Cost $O(n^3)$ in the number of nodes, paid once. A variant of Yarvin-Rokhlin (1998).
>
> (source: p. 6, eqs. 3.2-3.10)

**Error control (§3.1).** Two sources: discretisation, about $O(n^{-(j+1)})$ for $j$ continuous derivatives, and truncation, $\big(\sum_{i>m}\lambda_i^2\big)^{1/2}$. Practical proxy: compare eigenvalues from $n$ and $2n$ nodes, $\delta_{\max}=\max_i|\lambda_i^n-\lambda_i^{2n}|$ (p. 7). Needed terms depend on region size relative to the kernel timescale.

**Regression (§4).** With $X_{ij}=\phi_j(x_i)$ (eq. 4.8):
$$K\approx XX^\top.$$
With the SVD $X=UDV^\top$:
$$(K+\sigma^2I)^{-1}\approx U(D^2+\sigma^2I)^{-1}U^\top.$$
In weight space the model is ridge regression:
$$y\sim N(X\beta,\sigma^2),\quad \beta\sim N(0,I),$$
$$\bar\beta=\arg\min\|X\beta-y\|^2+\sigma^2\|\beta\|^2.$$
Posterior variance at $x$: $\varphi^\top(\sigma^{-2}X^\top X+I)^{-1}\varphi$ with $\varphi=(\phi_1(x),\dots,\phi_m(x))^\top$. Cost $O(Nm^2)$ (pp. 8-10, eqs. 4.7-4.20).

**Hyperparameters (§5).** Maximum likelihood: maximise $q(\beta,\theta,\sigma)$ over $\theta$; the KL basis is recomputed per $\theta$, $O(m^3)$, cheap against $O(Nm^2)$ regression; eigendecompositions can be precomputed over a $\theta$ grid. Fully Bayesian: a normal-normal model for $\beta$, sampled with MCMC (e.g. Stan).

> [!algorithm] Algorithm 2: reduced-rank Bayesian inference
> Squared-exponential kernel with amplitude $\alpha$, noise $\sigma$, timescale $\ell$; priors $\alpha,\sigma\sim N^+(0,3)$, $\ell\sim U(0.02,1)$.
> 1. Gauss nodes $\ell_i$, weights $w_i$ on $(0.02,1)$.
> 2. For each $\ell_i$, KL expansion by Algorithm 1 (amplitude only rescales it).
> 3. Per $\ell_i$, posterior moments of $\beta,\alpha,\sigma$ via Greengard et al. 2021.
> 4. Convert to Legendre coefficients; combine with $E[c]=\sum_iw_iE_{\ell_i}[c]$.
>
> (source: p. 11, eq. 5.7)

**Non-smooth kernels (§6).** For Matern, Algorithm 1 converges slowly. Algorithm 3 splits the integral at $x_i$ (eq. 6.5) and uses an SVD of the Legendre-to-node matrix, super-algebraic convergence for kernels smooth away from the origin. In practice little difference in $\epsilon_n$, since truncation error dominates (p. 12). **Two dimensions (§7, Alg. 4):** tensor-product Gauss nodes, $n^2\times n^2$ matrix, tensor Legendre expansion (pp. 12-13).

## Results

- 1D, $y=\cos(3e^x)+\epsilon$ (§8.1). Squared exponential, $\ell=0.2$: $\|k-k_n\|_2$ falls from $0.40$ at $n=5$ to $1.1\times10^{-14}$ at $n=50$ in 0.54 ms (Table 1). Matern 3/2: only $8.6\times10^{-4}$ at $n=55$ (Table 2).
- Conclusion states: $\ell=0.1$ squared exponential reaches error below $10^{-3}$ with 25 basis functions (p. 17).
- Bayesian fit, Matern 3/2 (Table 3): $N$ from 10 to $10^5$ in 0.21 s to 37.2 s.
- Versus Hilbert-GP (Solin and Sarkka 2020): the paper reports its basis is more accurate at the same number of functions, especially for small timescales; Hilbert-GP bases are free to compute but lose accuracy (Fig. 7, pp. 15-17).
- 2D, squared exponential, $\ell=0.25$ (Table 5): $N=160{,}000$ points in 7.12 s total (KL part 0.05 s) with $n=20^2$.
- Python code of Algorithm 1: github.com/pgree/kl_exps (p. 17).

## Limitations

Stated (p. 18): (i) rough kernels (slowly decaying spectrum) need many terms; (ii) curse of dimensionality: $m^d$ terms, so best in 1-2 D, or 3 D with smooth kernels. Accuracy of the effective kernel is measured, not yet the accuracy of the posterior; the authors defer that to later work (p. 13). They also sketch an extension to stable processes (p. 17-18).

Wiki note: needs a bounded rectangular domain containing all data and test points (p. 5), unlike hierarchical solvers that work on scattered data in any region. Compare [[Random features model]] / random Fourier features, which are cheap but not $L^2$-optimal (the paper makes this point about Lazaro-Gredilla 2010, p. 3).

## Connections

- The [[Karhunen-Loève expansion]] page has the general theory; this paper is its use as a GP regression engine.
- Weight-space view and ridge equivalence: [[Gaussian process]], [[Kernel methods]] (the GP posterior mean is the kernel ridge regression solution, see [[Gaussian processes and kernel methods (Kanagawa 2018)]]).
- Mercer expansion and the integral operator link to [[Kernel integral operator]] and [[RKHS]].
- Kernel choices (squared exponential, Matern): [[Kernel composition]], [[Duvenaud thesis (Duvenaud 2014)]].
- Pairs with [[Markov chain Monte Carlo]] for the fully Bayesian version.

**Sources**: `papers/Guassian Processes/Greengard, O'Neil - Efficient reduced-rank methods for Gaussian processes with eigenfunction expansions.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gaussian process]] · [[Karhunen-Loève expansion]] · [[Kernel methods]] · [[RKHS]] · [[Kernel integral operator]]
- [[Random features model]] · [[Markov chain Monte Carlo]] · [[Principal component analysis]]
- [[Gaussian processes and kernel methods (Kanagawa 2018)]] · [[Duvenaud thesis (Duvenaud 2014)]]
