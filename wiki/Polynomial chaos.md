---
type: method
area: me697
areas: [me697, uq]
tags: [uq, pde, ml]
---

# Polynomial chaos

**Summary**: Expands a model output as a series in polynomials that are orthonormal under the distribution of the random inputs. Mean and variance come from the coefficients, and for ODEs a Galerkin projection gives a deterministic ODE for the coefficients. The name has nothing to do with chaos theory.

---

## Expansion
$\mathcal L^2(\Xi)$ with $\langle f,g\rangle=\mathbb E[f(\Xi)g(\Xi)]$ has an orthonormal basis $\{\phi_n\}$:
$$f=\sum_n c_n\phi_n,\qquad c_n=\mathbb E[f(\Xi)\phi_n(\Xi)]$$
$$\mathbb E[f]=c_0,\qquad \mathbb V[f]=\sum_{n\ge1}c_n^2$$
The space is a separable Hilbert space for the standard distributions, which is why a basis exists. Parseval's identity gives the variance formula:
$$\|f\|^2=\sum_n c_n^2\quad\text{(Parseval)}$$
(source: `up/polynomial_chaos/01_functional_analysis.md`, `05_pc_ode_1d.ipynb`).

## Basis by input law
| Input | Polynomials |
|---|---|
| uniform | Legendre (shifted on $[0,1]$) |
| Gaussian | Hermite |
| any weight | numerical, three-term recurrence (orthojax, Gautschi) |

The book builds them by Gram-Schmidt on $\{1,\xi,\dots,\xi^9\}$ in sympy, with $\langle f,g\rangle=\int_0^1fg\,d\xi$ for uniform inputs (high orders show numerical noise) and the weight $e^{-\xi^2/2}/\sqrt{2\pi}$ for Gaussian ones. Gautschi's ORTHPOL idea via `orthojax` handles other weights (uniform on $[0,2]$, a two-component Gaussian mixture, $\mathrm{Exp}(1)$). Background reading on Hilbert spaces: Kreyszig, *Introductory Functional Analysis*, sections 1.1-3.7.

Recurrence for monic polynomials:
$$\pi_{k+1}=(\xi-\alpha_k)\pi_k-\beta_k\pi_{k-1}$$
$$\alpha_k=\frac{\langle\xi\pi_k,\pi_k\rangle}{\langle\pi_k,\pi_k\rangle},\qquad \beta_k=\frac{\langle\pi_k,\pi_k\rangle}{\langle\pi_{k-1},\pi_{k-1}\rangle}$$
with $\pi_{-1}=0$, $\pi_0=1$. For any weight there is a unique monic family $\pi_k=\xi^k+\dots$ with $\langle\pi_k,\pi_l\rangle=0$ for $k\ne l$; the orthonormalized family is the "polynomial chaos".

## ODEs
Write $X_t=\sum_i\alpha_i(t)e_i(\Xi)$ and project:
$$\dot\alpha_i=\big\langle f(t,\textstyle\sum_j\alpha_je_j;\cdot),e_i\big\rangle$$
$$\alpha_i(0)=\langle x_0,e_i\rangle$$
Truncate at $N$ and raise $N$ until converged. This is a Galerkin projection; the inner products are done by quadrature. Statistics come free: $\mathbb E[X_t]=\alpha_0(t)$ and $\mathbb V[X_t]=\sum_{i\ge1}\alpha_i(t)^2$. The PC solution is also a surrogate: evaluate $\sum\alpha(t)\phi_\alpha(\xi)$ at any $\xi$ with no ODE solve.

> [!example] Exponential decay (05)
> $\dot x=-(0.5+0.1\Xi)x$, $x_0=1$, $\Xi\sim\mathcal U[-1,1]$, Legendre degree 5, Tsit5 on the coefficient system, compared with Monte Carlo.

> [!example] Duffing with random initial state (07)
> $x(0),v(0)$ Gaussian, written as $\mu+\sigma\Phi^{-1}((\Xi+1)/2)$ with $\Xi_i\sim\mathcal U[-1,1]$. Degree 5, sparse-grid level 5. PC mean and variance match Monte Carlo and are much faster; accuracy degrades as the initial variance grows.

> [!example] Mean and variance of $\sin(2\Xi)/(2\Xi)$ (04)
> $\Xi\sim\mathcal N(0,1)$: project on Hermite, $\mathbb E[Z]=f_0$, $\mathbb V[Z]=\sum_{k\ge1}f_k^2$, compare Monte Carlo.

## Many inputs
- $\mathcal L^2(\Xi)=\mathcal L^2(\Xi_1)\otimes\dots\otimes\mathcal L^2(\Xi_d)$, so the tensor basis is
$$\phi_\alpha(\xi)=\prod_{i=1}^d\phi_{\alpha_i}(\xi_i),\qquad|\alpha|\le\rho$$
truncated at total degree $\rho$. For a vector state, $\psi_{i,\alpha}=\mathbf e_i\phi_\alpha$ is an orthonormal basis of $\mathcal L^2(\Xi,\mathbb R^n)$.
- Quadrature on Smolyak sparse grids, since full tensor grids explode (Clenshaw-Curtis/Fejer nested rules for Legendre, Gauss-Hermite for Hermite); chaospy has sparse grids but not in JAX.
- Mixed inputs: map each to uniform by $\Xi_i=F_i^{-1}(U_i)$ and use Legendre. Correlated Gaussians: $\Xi=\mu+LZ$ with $\Sigma=LL^T$; the general case is the Rosenblatt transformation.

## Limits (08)
Term count grows quickly with input dimension; poor for discontinuities, singularities, high frequency, and chaos.

## Wiki notes
- Term count is $\binom{d+\rho}{\rho}$, polynomial in $d$ for fixed $\rho$; the book's "exponential in the number of variables" is loose.
- The book defines $\mathcal L^2$ without the condition $\mathbb E[f^2]<\infty$, and its later inner product $\int g\cdot h\,d\Xi$ must carry the density of $\Xi$ for orthonormality to hold.
- The dependent-Gaussian recipe says $U$ is uniform on $[-1,1]$, but $\Phi^{-1}(U)$ needs $U\in[0,1]$; the notebook uses $(\Xi+1)/2$.
- A PCE is a [[Surrogate model]] with closed-form moments and [[Sobol indices]].

## Where it appears
- [[Wiener-Askey chaos (Xiu 2002)]]: generalises Wiener's Hermite chaos to the Askey scheme, matching the polynomial family to the input distribution.
- KL coefficients of a Gaussian field are the random inputs of the chaos expansion ([[KL expansion note (Alexanderian 2015)]]).

> [!example] Homework 3 (source: homework/03_homework.ipynb)
> Pythagoras $\|x+y\|^2=\|x\|^2+\|y\|^2$ for orthogonal $x,y$ and its $n$-term form; the map $T:H\to\ell^2$ from an orthonormal basis is linear, onto, one-to-one and preserves the inner product. Orthogonal polynomials for $\Xi\sim\exp(1)$ with `orthojax`, projection of $\sin$, mean and variance of $\sin(\Xi)$. Lorenz system ($\sigma=10$, $\beta=8/3$, $\rho=28$) with $x(0)\sim N(0,0.1)$, $y(0)\sim N(5,0.1)$, $z(0)\sim N(20,0.1)$: build a PCE surrogate, compare mean and variance with Monte Carlo, make three predictions, and plot densities at $t=1,2,5,10$ from 100,000 samples.

**Covered in**: ASML book up/polynomial_chaos (ME 697 2.2); homework 3
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/up/polynomial_chaos/00_intro.md` through `08_limitations.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sensitivity analysis]] · [[Local sensitivity analysis of ODEs]] · [[Sobol indices]] · [[Surrogate model]]
- [[Karhunen-Loève expansion]] · [[Gaussian process]]
