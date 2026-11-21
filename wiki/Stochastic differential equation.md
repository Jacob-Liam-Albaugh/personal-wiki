---
type: concept
area: stochastic
areas: [stochastic, me697]
source-ref: "ME 697 book, sinverse/intro and sinverse/sodes"
tags: [sampling, uq, inverse-problems, pde]
---

# Stochastic differential equation

An SDE adds random forcing to an ODE (source: sinverse/sodes/intro.md: "SDEs model random external excitations"):

$$
dX_t = a(X_t,t)\,dt + b(X_t,t)\,dW_t.
$$

Here $W$ is a [[Wiener process]] ([[Brownian motion]]), $a$ is the drift and $b$ the diffusion coefficient.

## Where they appear in the book
| SDE | Page | Closed form used |
|---|---|---|
| $dX=\mu X\,dt+\sigma X\,dW$ | [[Geometric Brownian motion]] | Itô log transform, lognormal law |
| $dX=-\lambda(X-\mu)dt+\sigma\,dW$ | [[Ornstein-Uhlenbeck process]] | mean and variance of $X_t$ |
| Duffing oscillator with noise | [[Stochastic state-space model]] | none, particle methods |

## Tools
- Simulation: [[Euler-Maruyama method]].
- Brownian paths from random walks (Donsker) and bridges via the [[Karhunen-Loève expansion]] (source: 02_bm.ipynb).
- Density evolution: [[Fokker-Planck equation]].
- Gradient drift with unit noise: [[Langevin dynamics]], used for sampling in [[SGLD]].

## Inverse problems for SDEs
Observed through noise, an SDE becomes a state-space model. Filtering and smoothing recover the state ([[Particle filter]]), calibration recovers parameters ([[Expectation-maximization]], [[Particle MCMC]]).

Applied example: [[Diesel PM as OU process (Bolt 2026)]] fits an OU SDE with input-dependent coefficients to engine PM by exact transition likelihood.

**Wiki note**: the book does not define the Itô integral or Itô's lemma beyond using the log transform for GBM. For a full treatment see the stochastic-methods pages linked from [[Brownian motion]].

## Linear SDEs in Fourier space and Stratonovich versus Itô (Enßlin)
Page numbers here are PDF pages of the lecture notes (printed page = PDF page minus 6).

> [!theorem] Linear SDE with stationary noise (source: Ensslin - Information Theory & Information Field Theory.pdf, §10.3, p. 121)
> $\sum_{n=0}^Na_n\,d^ns_t/dt^n=\xi_t$ with $P(\xi)=\mathcal G(\xi,\Xi)$, $\Xi^{\omega\omega'}=2\pi\delta(\omega-\omega')P_\xi(\omega)$ becomes algebraic after Fourier transform, $s^\omega=\big[\sum_na_n(-i\omega)^n\big]^{-1}\xi^\omega$. So $s$ is Gaussian with covariance $R\Xi R^\dagger$ and
> $$P_s(\omega)=\frac{P_\xi(\omega)}{\big|\sum_{n=0}^Na_n(-i\omega)^n\big|^2}\equiv P_R(\omega)P_\xi(\omega).$$

$R$ is the transfer function of signal processing. Examples: Wiener process ($a_1=1$, $P_R=\omega^{-2}$), [[Ornstein-Uhlenbeck process]] ($P_R=(\eta^2+\omega^2)^{-1}$), harmonic oscillator (§10.3.1-10.3.3, pp. 121-123). See [[Wiener-Khinchin theorem]].

> [!definition] Stratonovich and Itô pictures (source: §10.2, pp. 119-120)
> Take $\dot s=\xi$ with coloured Gaussian $\xi$ of bounded spectrum (Stratonovich picture, ordinary chain rule: $\dot f=f'(s)\xi$). Expanding $\langle f(s+\Delta s)-f(s)\rangle$ with $\langle\Delta s^2\rangle=\Delta t$, $\langle\Delta s^4\rangle=3\Delta t^2$ and odd moments zero gives the drift rate $\tfrac12f''(s_t)$ (eq. 307 and the text after it). In the Itô picture time is discrete and $\xi$ is white, so the drift is written explicitly: $df=f'(s_t)ds_t+\tfrac12f''(s_t)dt$ (eqs. 308-309).

The book gives the drift $\tfrac12f''$ in both pictures; the difference is where it comes from (automatic from the continuous action of $f$, versus an explicit added term).

Wiki note: standard texts usually state that the Stratonovich chain rule has no extra term and the $\tfrac12f''$ appears when converting to Itô form; the book's drift of $\langle f\rangle$ is the same quantity **[unverified]**. This also fills the gap noted above about Itô's lemma.

**Covered in**: ASML book sinverse/sodes (ME 697 6.1); Enßlin IT & IFT ch. 10.2-10.3 (pp. 119-123)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/sinverse/intro.md`, `sinverse/sodes/intro.md`, `02_bm.ipynb`, `03_stochastic_exponential_growth.ipynb`, `04_ornstein_uhlenbeck.ipynb`, `sinverse/sodes/01_reading.md`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Euler-Maruyama method]] · [[Geometric Brownian motion]] · [[Ornstein-Uhlenbeck process]]
- [[Stochastic state-space model]] · [[Wiener process]] · [[Fokker-Planck equation]] · [[Langevin dynamics]]
- [[Diesel PM as OU process (Bolt 2026)]]
- [[Wiener-Khinchin theorem]] · [[Wiener filter]] · [[Information Hamiltonian]]
