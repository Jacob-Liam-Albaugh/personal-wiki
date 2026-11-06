---
type: definition
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 3, Defs 3.1-3.17, Thms 3.11, 3.12, 3.15, 3.27, 3.30, 3.39, 3.51, 3.55, 3.60, 3.61 (pp. 41-67)"
tags: [optimization]
---

# Convex function

**Summary**: A function lying below its chords, equivalently with a convex epigraph. Every local minimiser is global, and first- and second-order tests are simple.

---

> [!definition] Convex function
> $f:\mathbb R^d\to\mathbb R\cup\{\infty\}$ is convex if for $\lambda\in(0,1)$:
> $$f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y).$$
> Strongly convex with modulus $c$: $f-\tfrac c2\|x\|^2$ is convex.
>
> (source: Basu 2018, Defs 3.1, 3.3, pp. 41-42)

## Equivalent forms

- The epigraph $\{(x,t):f(x)\le t\}$ is a [[Convex set]] (Prop 3.6, p. 42).
- Jensen: $f(\sum\lambda_ix_i)\le\sum\lambda_if(x_i)$ (Thm 3.11).
- First order, for differentiable $f$ (Thm 3.27, p. 51):
$$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle.$$
- Second order (Thm 3.30, p. 52): convex iff $\nabla^2f\succeq0$ everywhere; $\nabla^2f\succ0$ implies strictly convex (not conversely, $x^4$); strongly convex with modulus $c$ iff $\nabla^2f-cI\succeq0$.
- A closed convex function is the supremum of its affine supports (Thm 3.15, p. 46).

## Building convex functions (Thm 3.12, p. 44-45)

Nonnegative combinations, pointwise supremum, composition with an affine map, post-composition with an increasing convex function. Examples (Ex. 3.10, 3.13, p. 43-44): indicators of convex sets, affine functions, norms, maxima of finitely many affine functions, the supremum of any family of affine functions (closed convex), and the sum of the $k$ largest eigenvalues of a symmetric matrix (a sup of linear functions over orthonormal frames). Sublevel sets of a convex function are convex; the converse fails (quasi-convex, Prop 3.9). "Closed convex function" means closed epigraph (Def 3.7).

## Continuity (pp. 47-49)

On a compact convex $S\subseteq\mathrm{dom}(f)$, a convex $f$ is bounded near each relative interior point (Prop 3.20), locally Lipschitz (Prop 3.19), and Lipschitz over $S$ (Thm 3.21, p. 49). So convex functions are continuous on the relative interior of their domain.

## One-variable and slice tests (pp. 49-51)

Slopes of chords increase (Prop 3.24). A differentiable $f$ is convex iff $f'$ is increasing (Prop 3.25). Convexity in $\mathbb R^d$ reduces to every line slice $t\mapsto f(x+tr)$ being convex (Prop 3.26). The first-order test also has a monotone-gradient form (Thm 3.27, p. 51): $\langle\nabla f(y)-\nabla f(x),y-x\rangle\ge0$; strong convexity with modulus $c$ adds $\tfrac12c\|y-x\|^2$ to the gradient inequality and $c\|y-x\|^2$ to the monotone form.

## Sublinear functions, gauges, support functions (pp. 52-63)

These are the function-side of closed convex sets.

- Sublinear: positively homogeneous and subadditive; equivalently convex and positively homogeneous (Prop 3.32). Equivalently $f(0)=0$ and $\mathrm{epi}(f)$ a convex cone (Prop 3.33, p. 53).
- Gauge (Minkowski functional) of a closed convex $C\ni0$:
$$\gamma_C(r)=\inf\{\lambda>0:\ r\in\lambda C\}.$$
It is sublinear, $C=\{\gamma_C\le1\}$, and $\mathrm{rec}(C)=\{\gamma_C=0\}$ (Def 3.36, Thm 3.39, p. 54-55). Norms are exactly the gauges of compact convex centrally symmetric sets with $0$ in the interior (Cor 3.40-3.45, pp. 55-57). For a polyhedron $\{\langle a_i,x\rangle\le1\}$: $\gamma_P(r)=\max\{0,\langle a_i,r\rangle\}$ (Cor 3.47, p. 58).
- Support function of any set:
$$\sigma_S(r)=\sup_{x\in S}\langle r,x\rangle.$$
Always closed and sublinear (Def 3.48, p. 58-59). Gauge and support function are linked by polarity ([[Convex set]]):
$$\gamma_C=\sigma_{C^\circ}.\quad(\text{Thm 3.51})$$
- Generalised Holder (Thm 3.53, Cor 3.54, p. 60):
$$\langle x,y\rangle\le\gamma_C(x)\,\gamma_{C^\circ}(y).$$
Holder and Cauchy-Schwarz are the $\ell_p$/$\ell_q$ and Euclidean cases.

> [!theorem] One-to-one correspondence (Thm 3.55)
> $C\mapsto\sigma_C$ is a bijection from closed convex sets onto closed sublinear functions. The inverse is $f\mapsto\{x:\langle r,x\rangle\le f(r)\ \forall r\}$.
>
> (source: p. 61; Fig. 1, p. 62; nonnegative $f$ is the gauge of the polar, Prop 3.57)

## Subgradients and directional derivatives (pp. 46-47, 63-67)

$s$ is a subgradient at $x$ if $f(y)\ge f(x)+\langle s,y-x\rangle$ for all $y$ (an affine support, Def 3.14); the set $\partial f(x)$ is closed convex (Def 3.17, Thm 3.18, p. 47).

- Directional derivative $f'(x;r)=\lim_{t\downarrow0}(f(x+tr)-f(x))/t$ exists for convex $f$ and is sublinear in $r$ (Lemma 3.58, Prop 3.59, p. 63).
- $f'(x;\cdot)$ is the support function of the subdifferential: $\partial f(x)=\{s:\langle s,r\rangle\le f'(x;r)\ \forall r\}$ (Thm 3.60, p. 64; Fig. 2, p. 65).
- Differentiability test (Thm 3.61, p. 64): $f$ is differentiable at $x$ iff $f'(x;\cdot)$ is linear iff $\partial f(x)$ is a single point, and then it is $\{\nabla f(x)\}$.
- Calculus (Thm 3.62, p. 66-67): sums and compositions with affine maps behave as expected; for a supremum $f=\sup_jf_j$, the closed hull of the subgradients of the active pieces lies in $\partial f(x)$, with equality when the active index set is compact. **[unverified]** items 1-2 of Thm 3.62 were not read; only item 3 was.

## Convexity in linear programming

BT's definition (Def. 1.1, p. 15) and the fact that a maximum of convex functions is convex (Thm 1.1, p. 16) underlie piecewise-linear LP models (see [[LP modelling]]). LP value functions: the optimal cost $F(\mathbf b)$ of $\min\{\mathbf c'\mathbf x:\mathbf A\mathbf x=\mathbf b,\mathbf x\ge\mathbf0\}$ is convex piecewise linear in $\mathbf b$, and the optimal cost $G(\mathbf c)$ is concave piecewise linear in $\mathbf c$ (BT Thms 5.1, 5.3; see [[LP sensitivity analysis]]).

## Why it matters

A point $x^*$ minimises $f$ iff $0\in\partial f(x^*)$ (and $0\in\partial f+N_C$ with constraints, see [[KKT conditions]]), and the [[Subgradient method]] converges at rate $MR/\sqrt N$ regardless of dimension. The Lagrangian dual function of a convex program is concave ([[Lagrangian duality]]). A PSD kernel matrix is the Hessian-style convexity condition for quadratic forms ([[RKHS]], [[Kernel methods]]).

## Where it appears
- Piecewise linear convex costs reduce to LPs, and the optimal value as a function of $\mathbf b$ is piecewise linear and convex: [[Linear programming]] (Bertsimas-Tsitsiklis §1.3), [[Sensitivity analysis]] (pp. 213-214).
- The Lagrangean dual function of an integer program is concave and piecewise linear: [[Integer programming]] (Bertsimas-Tsitsiklis p. 495, Fig. 11.6).
- Convex functions and parametric LP value functions: [[Polyhedron]] (Bazaraa-Jarvis-Sherali ch. 2), [[LP duality]] (§6.8).

**Covered in**: Basu, Introduction to Convexity ch. 3 (pp. 41-67); Bertsimas-Tsitsiklis ch. 1, 5, 11 and Bazaraa-Jarvis-Sherali ch. 2, 6 (LP appearances)
**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (pp. 41-67; proofs skimmed, Thm 3.62 only partly read); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 1, 5).
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex set]] · [[Linear programming]] · [[LP duality]] · [[Polyhedron]]
- [[KKT conditions]] · [[Subgradient method]] · [[Lagrangian duality]] · [[RKHS]] · [[Kernel methods]]
- [[LP modelling]] · [[LP sensitivity analysis]]
