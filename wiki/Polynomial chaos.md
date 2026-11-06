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
(source: `up/polynomial_chaos/01_functional_analysis.md`, `05_pc_ode_1d.ipynb`).

## Basis by input law
| Input | Polynomials |
|---|---|
| uniform | Legendre (shifted on $[0,1]$) |
| Gaussian | Hermite |
| any weight | numerical, three-term recurrence (orthojax, Gautschi) |

Recurrence for monic polynomials:
$$\pi_{k+1}=(\xi-\alpha_k)\pi_k-\beta_k\pi_{k-1}$$

## ODEs
Write $X_t=\sum_i\alpha_i(t)e_i(\Xi)$ and project:
$$\dot\alpha_i=\big\langle f(t,\textstyle\sum_j\alpha_je_j;\cdot),e_i\big\rangle$$
$$\alpha_i(0)=\langle x_0,e_i\rangle$$
Raise the degree until converged.

## Many inputs
- Tensor basis $\phi_\alpha=\prod_i\phi_{\alpha_i}(\xi_i)$, truncated at total degree $|\alpha|\le\rho$.
- Quadrature on Smolyak sparse grids; non-uniform or correlated inputs via inverse-CDF maps, Cholesky, or the Rosenblatt transform.

## Limits (08)
Term count grows quickly with input dimension; poor for discontinuities, singularities, high frequency, and chaos.

## Wiki notes
- Term count is $\binom{d+\rho}{\rho}$, polynomial in $d$ for fixed $\rho$; the book's "exponential in the number of variables" is loose.
- A PCE is a [[Surrogate model]] with closed-form moments and [[Sobol indices]].

## Where it appears
- [[Wiener-Askey chaos (Xiu 2002)]]: generalises Wiener's Hermite chaos to the Askey scheme, matching the polynomial family to the input distribution.
- KL coefficients of a Gaussian field are the random inputs of the chaos expansion ([[KL expansion note (Alexanderian 2015)]]).

**Sources**: `advanced-scientific-machine-learning/book/up/polynomial_chaos/00_intro.md` through `08_limitations.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sensitivity analysis]] · [[Local sensitivity analysis of ODEs]] · [[Sobol indices]] · [[Surrogate model]]
- [[Karhunen-Loève expansion]] · [[Gaussian process]]
- [[ME697 2.2 - Polynomial chaos]] · [[ME697 2.1 - Sensitivity analysis]] · [[ME697 2.3 - Surrogates]]
