---
type: definition
area: operators
source-ref: "Kovachki et al. 2022, eqs. 7-9, pp. 10-11; Li et al. 2021, eq. 3, p. 4"
tags: [operators]
---

# Kernel integral operator

> [!definition] Kernel integral operator (Kovachki et al. 2022, eqs. 7-9, pp. 10-11)
> $$(\mathcal K v)(x)=\int_D\kappa(x,y)\,v(y)\,dy,\qquad \kappa:D\times D\to\mathbb R^{d_v\times d_v}$$
> Variants let the kernel see the input $a$ or the current state $v_t$:
> $$\kappa(x,y,a(x),a(y))\quad\text{or}\quad\kappa(x,y,v_t(x),v_t(y))$$
> The second makes the layer nonlinear in $v_t$.
>
> (source: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, pp. 10-11)

**Intuition**: the nonlocal half of a [[Neural operator]] layer. It is the operator analogue of a dense weight matrix, and like a Green's function it lets every point see the whole domain.

## Special cases
| Kernel | Gives |
|---|---|
| $\kappa(x-y)$ | convolution, evaluated by FFT in [[FNO]] |
| $\kappa(t-\tau)$ with rational transfer function | [[LNO]] (LNO eqs. 6-7, p. 4) |
| $\sum_j\varphi_j(x)\psi_j(y)$ | low rank; see [[Neural operator#Low-rank neural operator\|low-rank neural operator]] |
| constant matrix | averaging neural operator, already universal |

Kovachki et al. report that the $a$-dependent kernel (eq. 8) beats the plain kernel (eq. 7) on Darcy (p. 11).

## Where it appears
- [[Neural operator (Kovachki 2022)]], [[FNO (Li 2021)]], [[LNO (Cao 2023)]], [[Operator learning review (Kovachki 2024)]] (eq. 4.2, p. 14).

## Spectral properties
- for a continuous symmetric PSD kernel on a compact interval, the integral operator has real nonnegative eigenvalues and the kernel expands as a uniformly convergent sum of eigenvalue times eigenfunction products (Mercer; source: Greengard-O'Neil 2022, Thm 1, p. 4; Kanagawa 2018, Thm 4.1, p. 30). The eigenfunctions depend on the measure, the kernel does not (Kanagawa 2018, Remark 4.1).
- Nystrom quadrature on Gauss-Legendre nodes turns the operator into a matrix with entries sqrt(w_i w_j) k(x_i, x_j) (source: Greengard-O'Neil 2022, Alg. 1, p. 6).

**Sources**: `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural operator]] · [[Operator learning]]
- [[Neural tangent kernel]]
- [[RKHS]], [[Kernel methods]], [[Gaussian processes and kernel methods (Kanagawa 2018)]], [[Reduced-rank GPs (Greengard 2022)]].
