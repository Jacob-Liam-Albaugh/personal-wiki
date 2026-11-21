---
type: concept
area: gp
areas: [gp, bayesian]
source-ref: "Fortuin 2022, eqs. 4, 6, 8-11, 35"
tags: [gp, bayesian]
---

# Gaussian process

**Summary**: a prior over functions, $f\sim\mathcal{GP}(m,k)$, under which any finite set of values is jointly Gaussian; with Gaussian noise the posterior predictive is closed form.

## Connections
- GP posterior mean equals kernel ridge regression when the noise variance equals n times the ridge parameter; the posterior standard deviation equals the worst-case error over the RKHS unit ball (source: Kanagawa 2018, Props 3.6 and 3.10, pp. 21, 26). See [[Gaussian processes and kernel methods (Kanagawa 2018)]].
- GP draws are almost surely not in the RKHS of their own kernel when it is infinite dimensional, but lie in a slightly larger power space (source: Kanagawa 2018, Cor 4.10, Thm 4.12, pp. 33-36).
- kernels are built from sums, products and changepoints, and the structure can be searched automatically (source: Duvenaud 2014, chs. 2-3). See [[Kernel composition]], [[Duvenaud thesis (Duvenaud 2014)]].
- GP regression on a bounded domain can be run at O(N m^2) with a truncated KL basis computed once by Nystrom quadrature (source: Greengard-O'Neil 2022, Alg. 1, p. 6). See [[Reduced-rank GPs (Greengard 2022)]].
- a two-fidelity GP surrogate for a tissue model is in [[Multi-fidelity GP for tissue expansion (Lee 2020)]].

**Examples**: [[A to B to C reaction]] · [[Active learning test functions]] · [[Autoinjector FE surrogate]] · [[Bayesian optimisation 1D test function]] · [[Branin function]] · [[Chwirut1 ultrasonic calibration]] · [[Darcy flow FNO]] · [[Duffing oscillator examples]] · [[KLE of Gaussian processes]] · [[Motorcycle crash (mcycle)]] · [[Multi-fidelity 2D synthetic function]] · [[SPE10 permeability field]] · [[Stochastic 1D heat equation]] · [[Stochastic cylinder flow (multi-fidelity)]] (see [[Examples catalogue]])
## Gaussian fields and Wiener filtering (Enßlin)
Page numbers here are PDF pages of the lecture notes (printed page = PDF page minus 6).

- **Gaussian field** (source: Ensslin - Information Theory & Information Field Theory.pdf, §7, pp. 95-96): a field $\phi:\mathbb R^u\to\mathbb R$ is Gaussian if every finite set of pixel values is multivariate Gaussian with $\Phi_{ij}=\langle\phi(x_i)\phi(x_j)\rangle$. The density $\mathcal G(\phi,\Phi)$ is the $n\to\infty$ limit; the field is a vector in a Hilbert space with delta-function basis and scalar product $\psi^\dagger\phi=\int dx\,\psi(x)\phi(x)$. This is a GP in the notes' vocabulary, with covariance $\Phi$ as the kernel.
- **Wick theorem** for the fourth moment (§7.1, p. 96), with $\Phi_{xy}$ the covariance of $\phi_x,\phi_y$:

$$\langle\phi_x\phi_y\phi_z\phi_w\rangle=\Phi_{xy}\Phi_{zw}+\Phi_{xz}\Phi_{yw}+\Phi_{xw}\Phi_{yz}.$$

  The printed text ends with $\Phi_{yw}\Phi_{yz}$, which looks like a typo for $\Phi_{xw}\Phi_{yz}$.
- **Field calculus** (§7.1, p. 96; eqs. 300-301): the discrete rules carry over to fields.
  - Scalar product: $j^\dagger\phi=j_i\phi^i$ becomes $\int dx\,j(x)\phi(x)$.
  - Derivative: $\partial_\phi\,j^\dagger\phi=j$ in both cases (functional derivative for fields).
  - Determinant: $|\Phi|=\prod_i\lambda_i$, and its $n\to\infty$ limit may be undetermined.
  - Inverse covariance: $\int dy\,(\Phi^{-1})^x{}_y\Phi^y{}_z=\delta(x-z)$.
  - Expectations are path integrals defined as the pixel limit:

$$\langle f(\phi)\rangle=\int\mathcal D\phi\,P(\phi|\Phi)f(\phi)=\lim_{n\to\infty}\Big[\prod_{i=1}^n\int d\phi^i_{(n)}\Big]\mathcal G(\phi_{(n)},\Phi_{(n)})f_n(\phi_{(n)}).$$

  - Field components are contravariant: rescaling the basis by $A$ changes the components by $A^{-1}$, so $\phi$ itself is unchanged (p. 95).
- **Regression is Wiener filtering** (§5.1, p. 81): the posterior mean $m=(S^{-1}+R^\dagger N^{-1}R)^{-1}R^\dagger N^{-1}d$ is GP regression when $R$ samples the field; see [[Wiener filter]] and [[Information Hamiltonian]]. The notes call $S$ a covariance; [[Information field theory]] uses $S$ for a precision.
- **Stationary GPs** are diagonal in Fourier space by the [[Wiener-Khinchin theorem]].
- **Markov GPs**: the Wiener process and Ornstein-Uhlenbeck process are Gaussian Markov processes whose covariance obeys $S^{fp}=S^{ft}S^{tp}/S^{tt}$ (§10.1.3, p. 116); linear SDEs give GPs with spectrum $P_\xi/|\sum a_n(-i\omega)^n|^2$ (§10.3, p. 121). See [[Wiener process]], [[Stochastic differential equation]].
- **Sampling** a zero-mean Gaussian with covariance $S$: $s=S^{1/2}\xi$, $\xi\sim\mathcal G(\xi,\mathbb 1)$ (§9, p. 112).

**Covered in**: Enßlin IT & IFT chs. 7, 9, 10 (pp. 95-96, 111-123); Enßlin IT & IFT ch. 4 (pp. 71-76)
**Sources**: `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Posterior predictive (Fortuin eq. 6)
With training inputs $X$, outputs $y$, noise $\sigma^2$, $K=k(X,X)$, $k_*=k(X,x_*)$:
$$\mu_*=k_*^\top(K+\sigma^2I)^{-1}y$$
$$\sigma_*^2=k(x_*,x_*)-k_*^\top(K+\sigma^2I)^{-1}k_*$$
Hyperparameters fit by maximising the marginal likelihood (eq. 35).

## Links to neural networks
- Infinite-width networks are GPs with the NNGP kernel (eqs. 8-9; proved for deep networks by [[Wide networks as GPs (Matthews 2018)]], see [[Neural network Gaussian process]]):
  $$k^\ell=\sigma_w^2\,\mathbb E_{z\sim N(0,K^{\ell-1})}[\varphi(z_1)\varphi(z_2)]+\sigma_b^2$$
- Gradient-descent training in that limit follows the neural tangent kernel $k=JJ^\top$ (eqs. 10-11); the recursion is verified in [[NTK (Jacot 2018)]], Thm 1.

## Where it appears
- [[Diesel PM as OU process (Bolt 2026)]]: sparse and deep-kernel GPs as benchmarks for engine PM; the 35-parameter OU model beats both on calibration.
- [[Priors in Bayesian deep learning (Fortuin 2022)]] (GP priors and infinite-width limits).
- [[Bayesian DenseED surrogate (Zhu 2018)]]: GPs as the surrogate baseline that scales badly in input dimension; the input field itself is a GP sampled by [[Karhunen-Loève expansion]].
- [[Physics-informed ML review (Karniadakis 2021)]] — GP kernels as inductive bias and GP uncertainty for active learning (pp. 4, 9).
- [[Wide networks as GPs (Matthews 2018)]] — deep wide networks converge to GPs; finite Bayesian nets vs exact GP.
- [[Neural tangent kernel]] — infinite-width networks behave as kernel regression.
- [[Wiener process]] is the GP with kernel $s\wedge t$; KL expansion samples GPs ([[Karhunen-Loève expansion]], [[Mercer's theorem]]).
- First-order propagation of Gaussian parameter uncertainty through an ODE gives a vector-valued GP with covariance $\nabla_\theta x\,\Sigma\,\nabla_\theta x^T$: [[Local sensitivity analysis of ODEs]] (source: `up/sensitivity_analysis/01_theory.md`).
- GP surrogates, exact versus sparse variational: [[Surrogate model]].
- Multi-fidelity GPs (Kennedy-O'Hagan and nonlinear): [[Multi-fidelity modeling]].
- GP with uncertainty sampling for active learning: [[Active learning]].
- GP baselines and smoothing around PINNs: periodic-kernel GP smoothing of MRI waveforms ([[Cardiovascular flow PINNs (Kissas 2020)]]); GP regression as a baseline that fails at wavefront collisions ([[Cardiac activation PINN (Sahli Costabal 2020)]]).
- GP as random-field input to a PDE, expanded by KLE: [[Karhunen-Loève expansion]].

## Related pages
- [[Random features model]] (kernel link, Kovachki et al. 2024 p. 11) · [[Bayesian neural networks]] · [[Information field theory]]
- Fourier-feature networks in the NTK regime behave like kernel regression with a stationary kernel set by B (Tancik 2020). Link [[Fourier features]].
- [[Kernel methods]], [[RKHS]], [[Kernel composition]], [[Multi-fidelity Gaussian process]].
- Field-valued unknowns in the planned PDE inverse problems (empty in the book): [[Bayesian inverse problems]].
- [[IFT for UQ of differential equations (Hao 2024)]]
- [[Wiener filter]] · [[Information Hamiltonian]] · [[Wiener-Khinchin theorem]] · [[Lognormal Poisson model]]
- [[Multivariate Gaussian]]
