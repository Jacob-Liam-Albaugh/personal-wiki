---
type: paper
area: math
areas: [math, optimization]
source-ref: "Basu, Introduction to Convexity (lecture notes, 6 Dec 2018), ch. 3, Defs 3.1-3.17, Thms 3.12, 3.15, 3.27, 3.30, 3.39, 3.51, 3.55, 3.60, 3.61 (pp. 41-67)"
tags: [optimization]
authors: ["[[Amitabh Basu]]"]
year: 2018
venue: "Lecture notes, Johns Hopkins University, compiled 6 Dec 2018"
file: "Math/Convexity/Basu - Intro to Convexity.pdf"
---

# Basu ch3 - Convex functions

**Summary**: Chapter 3 of Basu's notes. A [[Convex function]] is one whose epigraph is a [[Convex set]], so the set theory of [[Basu ch2 - Convex sets]] transfers. The chapter covers closure operations, continuity, gradient and Hessian tests, sublinear functions (gauges and support functions) as the function-side of closed convex sets, and subgradients with directional derivatives.

**Authors**: Amitabh Basu · **Year**: 2018 · **File**: `Math/Convexity/Basu - Intro to Convexity.pdf` · Previous: [[Basu ch2 - Convex sets]] · Next: [[Basu ch4 - Convex optimization]]

---

## 3.1 Definitions, epigraphs, subgradients (pp. 41-47)

> [!definition] Convex function
> $f:\mathbb R^d\to\mathbb R\cup\{\infty\}$ is convex if
> $$f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y),\quad\lambda\in(0,1).$$
> Strict if the inequality is strict for $x\ne y$. Strongly convex with modulus $c>0$ if an extra term $-\tfrac12c\lambda(1-\lambda)\|x-y\|^2$ is subtracted on the right; equivalently $f-\tfrac c2\|x\|^2$ is convex.
>
> (source: Defs 3.1, 3.3, Prop 3.4, pp. 41-42)

- Epigraph $\mathrm{epi}(f)=\{(x,t):f(x)\le t\}$. Then $f$ is convex iff $\mathrm{epi}(f)$ is convex (Prop 3.6, p. 42). "Closed convex function" means closed epigraph (Def 3.7). Sublevel sets of a convex function are convex; the converse fails (quasi-convex, Prop 3.9).
- Examples (Ex. 3.10, p. 43): indicator of a convex set, affine functions, norms, the max of finitely many affine functions.
- Jensen (Thm 3.11, p. 44): $f$ convex iff $f(\sum\lambda_ix_i)\le\sum\lambda_if(x_i)$.
- Preserved by (Thm 3.12, p. 44-45): nonnegative combinations, pointwise supremum, composition with an affine map, post-composition with an increasing convex function. Examples: the sup of any family of affine functions is closed convex (Ex. 3.13); the sum of the $k$ largest eigenvalues of a symmetric matrix is convex (a sup of linear functions over orthonormal frames).
- Affine support at $x$: $f(y)\ge f(x)+\langle a,y-x\rangle$ for all $y$ (Def 3.14).

> [!theorem] Closed convex means supremum of affine functions (Thm 3.15)
> A real-valued $f$ is closed convex iff it has an affine support at every point. The analogue of "closed convex sets are intersections of halfspaces".
>
> (source: p. 46; proof applies the supporting hyperplane theorem to the epigraph)

A subgradient at $x$ is an affine support; $\partial f(x)$ is the subdifferential, a closed convex set (Def 3.17, Thm 3.18, p. 47).

## 3.2 Continuity (pp. 47-49)

On a compact convex $S\subseteq\mathrm{dom}(f)$, a convex $f$ is bounded near each relative interior point (Prop 3.20), locally Lipschitz (Prop 3.19), and Lipschitz over $S$ (Thm 3.21, p. 49). So convex functions are continuous on the relative interior of their domain.

## 3.3-3.4 Derivative tests (pp. 49-52)

- One variable: slopes of chords increase (Prop 3.24). $f$ differentiable is convex iff $f'$ is increasing (Prop 3.25). Convexity in $\mathbb R^d$ reduces to every line slice $t\mapsto f(x+tr)$ being convex (Prop 3.26).

> [!theorem] First-order test (Thm 3.27)
> For differentiable $f$ these are equivalent:
> 1. $f$ is convex.
> 2. $f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle$.
> 3. $\langle\nabla f(y)-\nabla f(x),\,y-x\rangle\ge0$.
>
> Strong convexity with modulus $c$ adds $\tfrac12c\|y-x\|^2$ to 2 and $c\|y-x\|^2$ to 3.
>
> (source: p. 51)

> [!theorem] Second-order test (Thm 3.30)
> For twice differentiable $f$:
> 1. convex iff $\nabla^2f(x)$ is PSD everywhere.
> 2. $\nabla^2f\succ0$ everywhere implies strictly convex (the converse fails: $x^4$, Remark 3.29).
> 3. strongly convex with modulus $c$ iff $\nabla^2f-cI$ is PSD.
>
> (source: p. 52)

## 3.5 Sublinear functions, gauges, support functions (pp. 52-63)

- Sublinear: positively homogeneous and subadditive; equivalently convex and positively homogeneous (Prop 3.32). $f(0)=0$ and $\mathrm{epi}(f)$ a convex cone is the same as sublinear (Prop 3.33, p. 53).
- Gauge (Minkowski functional) of a closed convex $C\ni0$:
$$\gamma_C(r)=\inf\{\lambda>0:\ r\in\lambda C\}.$$
It is sublinear, $C=\{\gamma_C\le1\}$, and $\mathrm{rec}(C)=\{\gamma_C=0\}$ (Def 3.36, Thm 3.39, p. 54-55). Norms are exactly the gauges of compact convex centrally symmetric sets with $0$ in the interior (Cor 3.40-3.45, pp. 55-57). For a polyhedron $\{\langle a_i,x\rangle\le1\}$: $\gamma_P(r)=\max\{0,\langle a_i,r\rangle\}$ (Cor 3.47, p. 58).
- Support function of any set: 
$$\sigma_S(r)=\sup_{x\in S}\langle r,x\rangle.$$
Always closed and sublinear (Def 3.48, p. 58-59). Gauge and support function are linked by polarity:
$$\gamma_C=\sigma_{C^\circ}.\quad(\text{Thm 3.51})$$
- Generalised Holder (Thm 3.53, Cor 3.54, p. 60):
$$\langle x,y\rangle\le\gamma_C(x)\,\gamma_{C^\circ}(y).$$
Holder and Cauchy-Schwarz are the $\ell_p$/$\ell_q$ and Euclidean cases.

> [!theorem] One-to-one correspondence (Thm 3.55)
> $C\mapsto\sigma_C$ is a bijection from closed convex sets onto closed sublinear functions. The inverse is $f\mapsto\{x:\langle r,x\rangle\le f(r)\ \forall r\}$.
>
> (source: p. 61; Fig. 1, p. 62; nonnegative $f$ is the gauge of the polar, Prop 3.57)

## 3.6 Directional derivatives and subdifferential calculus (pp. 63-67)

- Directional derivative $f'(x;r)=\lim_{t\downarrow0}(f(x+tr)-f(x))/t$ exists for convex $f$ and is sublinear in $r$ (Lemma 3.58, Prop 3.59, p. 63).
- $f'(x;\cdot)$ is the support function of the subdifferential: $\partial f(x)=\{s:\langle s,r\rangle\le f'(x;r)\ \forall r\}$ (Thm 3.60, p. 64; Fig. 2, p. 65).
- Differentiability test (Thm 3.61, p. 64): $f$ is differentiable at $x$ iff $f'(x;\cdot)$ is linear iff $\partial f(x)$ is a single point, and then it is $\{\nabla f(x)\}$.
- Calculus (Thm 3.62, p. 66-67): sums and compositions with affine maps behave as expected; for a supremum $f=\sup_jf_j$, the closed hull of the subgradients of the active pieces lies in $\partial f(x)$, with equality when the active index set is compact. **[unverified]** items 1-2 of Thm 3.62 were not read; only item 3 was.

## Connections

- Wiki note: a PSD kernel matrix is the Hessian-style convexity condition for quadratic forms; see [[RKHS]], [[Kernel methods]].
- Subgradients feed the subgradient algorithm in [[Basu ch4 - Convex optimization]].

**Sources**: `Math/Convexity/Basu - Intro to Convexity.pdf` (pp. 41-67; proofs skimmed, Thm 3.62 only partly read).
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex function]] · [[Convex set]] · [[Polyhedron]] · [[Linear programming]]
- [[Basu ch2 - Convex sets]] · [[Basu ch4 - Convex optimization]] · [[Kernel methods]]
