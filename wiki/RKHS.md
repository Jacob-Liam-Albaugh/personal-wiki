---
type: definition
area: gp
areas: [gp, math]
source-ref: "Kanagawa et al. 2018 §2-4 (Thms 4.1-4.12, Cor 4.10, Prop 3.10); Greengard-O'Neil 2022 Thm 1"
tags: [gp, ml]
---

# RKHS

**Summary**: The reproducing kernel Hilbert space $H_k$ of a positive definite kernel $k$: the Hilbert space of functions in which evaluation is a bounded linear map and $k$ is its representer. It is the "smoothness class" attached to a [[Gaussian process]] prior, though GP samples fall just outside it.

---

> [!definition] Reproducing kernel Hilbert space
> A Hilbert space $H_k$ of functions on $\mathcal X$ with a kernel $k$ such that for all $x$ and all $f\in H_k$:
> 1. $k(\cdot,x)\in H_k$,
> 2. $\langle f,k(\cdot,x)\rangle_{H_k}=f(x)$ (reproducing property).
>
> Each PD kernel determines a unique such space (Moore-Aronszajn).
>
> (source: Kanagawa 2018, §2)

## Mercer picture

On a compact space with a measure $\nu$, the [[Kernel integral operator]] has eigenpairs $(\lambda_i,\phi_i)$ and
$$k(x,x')=\sum_i\lambda_i\phi_i(x)\phi_i(x').$$
Then $\{\lambda_i^{1/2}\phi_i\}$ is an orthonormal basis of $H_k$, and
$$\|f\|_{H_k}^2=\sum_i\frac{c_i^2}{\lambda_i}\quad\text{for } f=\sum_ic_i\phi_i.$$
Fast eigenvalue decay means $H_k$ contains only very smooth functions (source: Kanagawa 2018, Thms 4.1-4.2, p. 30; Greengard-O'Neil 2022, Thm 1, p. 4).

## Relation to GP samples

The [[Karhunen-Loève expansion]] writes a GP draw as
$$f=\sum_iz_i\lambda_i^{1/2}\phi_i,\quad z_i\sim N(0,1).$$
Same basis as $H_k$ but unit-variance coefficients, so $\|f\|^2_{H_k}=\sum z_i^2=\infty$: draws are almost surely not in $H_k$ when it is infinite dimensional (source: Kanagawa 2018, Cor 4.10, p. 33). They lie in the larger power space $H_k^\theta$ iff $\sum_i\lambda_i^{1-\theta}<\infty$; for the squared exponential, every $\theta<1$ works (source: Kanagawa 2018, Thm 4.12, Cor 4.13, pp. 36-37).

## Uses

- Regression: the posterior mean is the minimum-norm interpolant (noise free) or the kernel ridge solution, so it lies in $H_k$ ([[Kernel methods]]).
- Error bar: for $\|f\|_{H_k}\le1$, the pointwise error is bounded by the posterior standard deviation (source: Kanagawa 2018, Prop 3.10, p. 26). With noise the bound uses $k^\sigma=k+\sigma^2\delta$ (Prop 3.8, p. 24).
- Examples: Brownian motion has the first-order Sobolev space as RKHS (source: Kanagawa 2018, Ex. 4.1, p. 35).

## Convexity link

A positive definite kernel has PSD Gram matrices; a symmetric matrix is PSD iff its eigenvalues are nonnegative iff $A=B^\top B$ iff $u^\top Au\ge0$ for all $u$ (Basu 2018, Thm 1.18, p. 7), and $\sqrt{x^\top Ax}$ is a norm for PD $A$. Background on convexity: [[Convex function]], [[Convex set]].

**Covered in**: Basu, Introduction to Convexity ch. 1 and 3 (PSD facts, pp. 7, 52)
**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (ch. 1, 3); `papers/Guassian Processes/Kanagawa, Hennig, Sejdinovic, Sriperumbudur - GPs & Kernel Methods.pdf`; `papers/Guassian Processes/Greengard, O'Neil - Efficient reduced-rank methods for Gaussian processes with eigenfunction expansions.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Kernel methods]] · [[Kernel integral operator]] · [[Karhunen-Loève expansion]] · [[Gaussian process]]
- [[Kernel composition]] · [[Random features model]]
- [[Gaussian processes and kernel methods (Kanagawa 2018)]] · [[Reduced-rank GPs (Greengard 2022)]]
