---
type: method
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 4, Def 4.9, Cors 4.12-4.13, Remark 4.14 (pp. 69-72)"
tags: [optimization]
---

# Subgradient method

**Summary**: Gradient descent for non-smooth convex functions: step along a negative subgradient and project back onto the feasible set. It needs only a subgradient oracle and a projection oracle, and its rate is independent of dimension.

---

> [!algorithm] Projected subgradient (Basu Def 4.9, p. 70)
> Start at $x_0\in C$. At step $i$ take $g_i\in\partial f(x_i)$ and
> $$x_{i+1}=\Pi_C\big(x_i-h_i\,g_i\big),$$
> where $\Pi_C$ is Euclidean projection onto the closed [[Convex set]] $C$ and $h_i>0$ is the step. The problem is $\inf_{x\in C}f(x)$ with $f$ a [[Convex function]] (Basu eq. 4.1).

> [!theorem] Rate (Basu pp. 71-72)
> Let $\|g\|\le M$ for all subgradients and $\|x_0-x^*\|\le R$. Then
> $$\min_{i\le N}f(x_i)-f^*\le\frac{M(R^2+\sum_i h_i^2)}{2\sum_i h_i}.$$
> With the constant step $h_i=R/\sqrt{N+1}$ (Cor 4.12) the error is at most $MR/\sqrt{N+1}$. Convergence also holds for $h_i\to0$ with $\sum h_i=\infty$ (Cor 4.13).

So $O(M^2R^2/\epsilon^2)$ steps reach accuracy $\epsilon$, with no dependence on dimension (Remark 4.14).

## Subgradients in linear programming

BT define subgradients for LP sensitivity (BT Def. 5.1, p. 215): $\mathbf p$ is a subgradient of a convex $F$ at $\mathbf b^*$ if $F(\mathbf b^*)+\mathbf p'(\mathbf b-\mathbf b^*)\le F(\mathbf b)$ for all $\mathbf b$. For the LP optimal-cost function $F(\mathbf b)$ the dual optimal solutions are exactly the subgradients at $\mathbf b^*$ (BT Thm 5.2, p. 216); at breakpoints of the piecewise linear $F$ there are several (see [[LP sensitivity analysis]]).

The Lagrangean dual of an integer program is concave piecewise linear and is maximized by subgradient steps $\mathbf p^{t+1}=\mathbf p^t+\theta_t\mathbf s^t$ with $\theta_t=\alpha_t(\hat Z_D-Z(\mathbf p^t))/\|\mathbf s^t\|^2$ (BT pp. 502-507, see [[Lagrangian relaxation]]).

## Key facts
- The step is not a descent step: only the best iterate $\min_{i\le N}f(x_i)$ is controlled.
- The stopping point of the method is the optimality condition $0\in\partial f(x^*)+N_C(x^*)$ ([[KKT conditions]]).
- Compared with [[Cutting-plane methods]]: the subgradient method is dimension-free but converges as $1/\epsilon^2$; cutting planes depend on dimension but converge in $\log(1/\epsilon)$.
- It is the non-smooth ancestor of stochastic gradient training ([[Gradient descent]], [[SGD]]); the $MR/\sqrt N$ bound is the classical non-smooth rate.

**Covered in**: Basu, Introduction to Convexity ch. 4 §4.2 (pp. 69-72); Bertsimas-Tsitsiklis §5.2 (pp. 215-216), §11.4 (pp. 502-507)
**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (pp. 69-72; proof skimmed); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 5, 11).
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex function]] · [[Convex set]] · [[KKT conditions]] · [[Cutting-plane methods]] · [[Gradient descent]] · [[SGD]]
- [[LP sensitivity analysis]] · [[Lagrangian relaxation]]
