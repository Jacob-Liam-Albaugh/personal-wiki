---
type: definition
area: stochastic
areas: [stochastic, operators]
source-ref: "Lu et al. 2021, p. 9"
tags: [gp]
---

# Karhunen-Loève expansion

> [!definition] Truncated KL expansion (as used in Lu et al. 2021, p. 9)
> $$k(t;\omega)\approx\sum_{i=1}^N\sqrt{\lambda_i}\,e_i(t)\,\xi_i(\omega)$$
> with $(\lambda_i,e_i)$ the eigenpairs of the covariance operator (eigenfunctions normalized) and $\xi_i$ i.i.d. standard Gaussians.
>
> (source: `26.10.22 - DeepONets.pdf`, p. 9)

**Intuition**: the eigenfunctions of the covariance are the optimal basis for a random field in mean square; truncation turns a random function into $N$ independent Gaussian numbers.

## Where it appears
- [[DeepONet (Lu 2021)]] — random coefficients in Problems 5-6.
- [[PIFT (Alberts 2023)]] — Ex. 3b: 10-term KLE of a squared-exponential GP (lengthscale 0.3, >99% variance) via Nyström.
- [[IFT thermal conductivity (Alberts 2026)]] — $k(u)=\exp(a_1+a_2u+\sum_{n=1}^{25}z_n\lambda_n^{1/2}\varphi_n(u))$ with exact Hermite eigenpairs of the SE kernel (eq. 10, App. A).

Wiki note: [[PCA-Net]] uses the empirical version, PCA of sampled input and output functions, as its encoder and decoder.
- KLE of a GP with a Nystrom implementation in JAX, truncation at 95% of $\sum_i\lambda_i$, and use as the input stage of a UQ pipeline (KLE in, PCA out, one GP per coefficient) (source: `hup/funcin/04_kle.ipynb`, `05_up_example.ipynb`, `06_up_hout_example.ipynb`).
- Same orthonormal-expansion device for random variables: [[Polynomial chaos]]. Data-driven counterpart: [[Principal component analysis]].
- Wiki note: the book's KLE display has typos and the Nystrom eigenfunction extension is asymmetric for non-uniform weights.
- [[Proper orthogonal decomposition]]: the POD basis of a random field is its KL basis (Wiki note; the book treats them in separate chapters).

> [!example] Homework 5, problem 3 (source: homework/05_homework.ipynb)
> KL model of oil-reservoir permeability on $[0,356]\times[0,670]$ m, positive and conditioned on a geologist's estimate.

- [[Stochastic differential equation]] uses a KL expansion for the Brownian bridge (source: sinverse/sodes).

## Queued sources
Four KL papers in `papers/Stochastic Methods/` (Alexanderian; Betz-Papaioannou-Straub; Deheuvels; Prakash et al.) should extend this page with the Mercer / convergence statements. Everything beyond the formula above is **[unverified]** until then.

## Properties
- among all order-m expansions with iid N(0,1) coefficients, the truncated KL expansion minimises the L2 error of the effective kernel (source: Greengard-O'Neil 2022, eq. 1.10, p. 3). Error decays exponentially in m for smooth kernels and no slower than O(1/m^(j+1)) for kernels with j continuous derivatives (Thm 3, pp. 4-5).
- the expansion uses the same eigenfunctions as the RKHS basis, but with coefficients of variance one, so the sample has infinite RKHS norm (source: Kanagawa 2018, Thm 4.3, p. 31).

## Related / finite-dimensional analogue
- The best m-term approximation of a vector in an orthogonal basis (keep the m largest coefficients) is the idea that the [[DFT]] page and [[DFT]] develop for fixed Fourier bases; Karhunen-Loève chooses the basis from the data. (source: courses/ECE 438/Topic DSP.3.B DT frequency analysis Part 2 Jan 31, 2025.pdf, pp. 2-4)
- See also [[Image transforms]].

## Gaussian random field expansion (book, hup/funcin/04)
> [!definition] KLE of a GP
> For $f\sim\mathrm{GP}(m,k)$:
> $$f(\mathbf x)=m(\mathbf x)+\sum_{i=1}^{\infty}\xi_i\sqrt{\lambda_i}\,\phi_i(\mathbf x)$$
> with independent $\xi_i\sim\mathcal N(0,1)$ and $(\lambda_i,\phi_i)$ the eigenpairs of the covariance operator,
> $$\int k(\mathbf x,\mathbf x')\phi_i(\mathbf x')\,d\mathbf x'=\lambda_i\phi_i(\mathbf x)$$
> Pointwise variance is $\sum_i\lambda_i\phi_i^2(\mathbf x)$ and the field energy is
> $$\mathcal E[f]=\int\mathbb V[f(\mathbf x)]\,d\mathbf x=\sum_i\lambda_i$$
> Truncate at the smallest $M$ with $\sum_{i\le M}\lambda_i\ge\alpha\sum_i\lambda_i$, typically $\alpha=0.95$. An infinite-dimensional field becomes $M$ standard normals.

> [!algorithm] Nystrom KLE
> 1. Quadrature points $\mathbf x_q$ with weights $w_q$ (uniform grid on $[0,1]$ or $[0,1]^2$).
> 2. Eigendecompose the discretized operator $K_{qq'}w_{q'}$.
> 3. Keep eigenvalues until the cumulative energy exceeds $\alpha$.
> 4. Extend eigenfunctions off the grid by $\phi_i(\mathbf x)=\lambda_i^{-1}\sum_q v_{qi}\sqrt{w_q}\,k(\mathbf x,\mathbf x_q)$.
> For a GP conditioned on data the same code expands the posterior GP, whose eigenfunctions are pinned near zero at observed inputs.

- A larger lengthscale (smoother samples) gives faster eigenvalue decay, because the leading eigenfunctions are the smoothest.
- Rough kernels need many terms: with the exponential kernel and $\alpha=0.8$ the sampled fields look too smooth; the truncation removed the roughness.

> [!example] Stochastic heat equation to one number (05)
> Steady rod $\frac{d}{dx}\big(c\,\frac{du}{dx}\big)=0$, $u(0)=1$, $u(1)=0$. Conductivity $c=\exp\{g\}$, $g\sim\mathrm{GP}(0,\,0.5\,k_{SE})$ with lengthscale 0.1, KLE with $\alpha=0.95$ on 1000 quadrature points; finite-volume solver (FiPy, 500 cells); quantity of interest $u(0.5)$.
> 1. Draw 200 samples of $\boldsymbol\xi$, solve, keep $u(0.5)$; 80/20 train/test split.
> 2. Fit an ARD squared-exponential GP from $\boldsymbol\xi$ to $u(0.5)$ by minibatch marginal likelihood with [[Adam]] (1000 steps, lr 0.01, batch 100).
> 3. The parity plot is good; push 2000 new $\boldsymbol\xi$ through the cheap GP for a histogram of $u(0.5)$.
> The whole-field version is on [[Principal component analysis]].

Wiki notes on the book's section:
- The KLE equation is printed with $\phi_i(\mathbf x')$ on the right (should be $\phi_i(\mathbf x)$) and the orthonormality integral mixes $\mathbf x$ and $\mathbf x'$.
- The matrix $K_{qq'}w_{q'}$ is symmetric only for uniform weights, which the code uses; for general weights symmetrize with $w^{1/2}Kw^{1/2}$ before `eigh`. The default grid with weights $1/n_q$ is a crude rectangle rule.
- In 1D, $c\,u'$ is constant, so $u(x)=1-\int_0^xc^{-1}\big/\int_0^1c^{-1}$ (derived here; handy to check the FiPy solver).
- The text defines $c=c_0\exp\{g\}$ but the code sets $c_0=1$. Minibatches are drawn with replacement and batch 100 nearly equals the 160 training points, so duplicate inputs plus a $10^{-6}$ jitter condition the marginal likelihood poorly.
- A log-Gaussian coefficient is positive but not bounded away from zero, so elliptic theory needs extra conditions **[unverified]**.

**Covered in**: ASML book hup/funcin (ME 697 3.1); homework 5
**Sources**: `26.10.22 - DeepONets.pdf`, `papers/IFT/Bilionis, Alberts - IFT.pdf`, `papers/IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`, `courses/ME 697/advanced-scientific-machine-learning/book/hup/intro.md`, `hup/funcin/intro.md`, `01_functional_inputs.md`, `02_svd.ipynb`, `03_pca.ipynb`, `04_kle.ipynb`, `05_up_example.ipynb`, `06_up_hout_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[DeepONet]] · [[PCA-Net]]
- Optional link to [[Spectral bias]]; Wiki note only, no direct source cite. Skip if the page has no related-section.
- Convergence and Mercer: [[Mercer's theorem]]; full derivation via compact self-adjoint operators in [[KL expansion note (Alexanderian 2015)]] (source: Alexanderian 2015, Thm 3.1, 5.3, Cor 5.5). Truncation error $k(t,t)-\sum_{i\le n}\lambda_ie_i(t)^2$ goes to 0 uniformly.
- Closed-form example: Wiener process eigenpairs $\lambda_k=((k-\frac12)\pi)^{-2}$, $e_k=\sqrt2\sin((k-\frac12)\pi t)$ (source: Li, eq. 1.6); mean-centered version gives cosines (source: Deheuvels 2006, Thm 1.1). See [[Wiener process]], [[KL expansions of the Wiener process (Deheuvels 2006)]].
- Example: exponential kernel $\sigma^2e^{-|s-t|/L_c}$ with 6 terms, covariance error under $8\times10^{-2}$ (source: Alexanderian 2015, §6).
- Discretized random fields: [[Random field discretization (Betz 2014)]]. Application: [[Quantum option pricing KL (Prakash 2025)]].
- [[Reduced-rank GPs (Greengard 2022)]], [[RKHS]], [[Gaussian processes and kernel methods (Kanagawa 2018)]].
