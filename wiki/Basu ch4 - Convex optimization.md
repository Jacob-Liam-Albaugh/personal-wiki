---
type: paper
area: math
areas: [math, optimization]
source-ref: "Basu, Introduction to Convexity (lecture notes, 6 Dec 2018), ch. 4, Thms 4.9-4.12, 4.25, 4.31-4.33, 4.39-4.48 (pp. 67-93)"
tags: [optimization]
authors: ["[[Amitabh Basu]]"]
year: 2018
venue: "Lecture notes, Johns Hopkins University, compiled 6 Dec 2018"
file: "text_books/Mathmatics/Basu - Intro to Convexity.pdf"
---

# Basu ch4 - Convex optimization

**Summary**: Chapter 4 of Basu's notes. Minimising a [[Convex function]] over a [[Convex set]]: optimality conditions through tangent and normal cones, the projected subgradient method and its dimension-free rate, conic duality (weak duality, Slater, complementary slackness, saddle points), and cutting-plane methods (center of gravity, ellipsoid).

**Authors**: Amitabh Basu · **Year**: 2018 · **File**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` · Previous: [[Basu ch3 - Convex functions]]

---

## 4.1 The problem and optimality (pp. 67-69)

Problem: $\inf_{x\in C}f(x)$ with $C$ closed convex and $f$ convex (eq. 4.1). A local minimiser is a global one (p. 67). Tangent and normal cones at $x\in C$:
$$T_C(x)=\mathrm{cl}\,\mathrm{cone}(C-x),\qquad N_C(x)=\{s:\langle s,y-x\rangle\le0\ \forall y\in C\}.$$
(Defs 4.4-4.5, Prop 4.6, p. 68; normal cone is the polar of the tangent cone.)

> [!theorem] Optimality conditions (pp. 68-69)
> $x^*$ minimises $f$ over $C$ iff either of these holds:
> 1. $f'(x^*;r)\ge0$ for all $r\in T_C(x^*)$.
> 2. $0\in\partial f(x^*)+N_C(x^*)$.
>
> Condition 2 needs a constraint qualification (a relative-interior point of both domains).
>
> (source: pp. 68-69; unconstrained case: $0\in\partial f(x^*)$)

## 4.2 Projected subgradient method (pp. 69-72)

> [!algorithm] Projected subgradient (Def 4.9, p. 70)
> Start at $x_0\in C$. At step $i$ take $g_i\in\partial f(x_i)$ and
> $$x_{i+1}=\Pi_C\big(x_i-h_i\,g_i\big),$$
> where $\Pi_C$ is Euclidean projection onto $C$ and $h_i>0$ is the step.
>
> (source: p. 70)

> [!theorem] Rate (pp. 71-72)
> Let $\|g\|\le M$ for all subgradients and $\|x_0-x^*\|\le R$. Then
> $$\min_{i\le N}f(x_i)-f^*\le\frac{M(R^2+\sum_i h_i^2)}{2\sum_i h_i}.$$
> With the constant step $h_i=R/\sqrt{N+1}$ (Cor 4.12) the error is at most $MR/\sqrt{N+1}$. Convergence also holds for $h_i\to0$ with $\sum h_i=\infty$ (Cor 4.13).
>
> (source: Thm p. 71, Cors 4.12-4.13)

So $O(M^2R^2/\epsilon^2)$ steps reach accuracy $\epsilon$, with no dependence on dimension (Remark 4.14). The method needs only a subgradient oracle and a projection oracle.

## 4.3 Conic problems and duality (pp. 72-84)

- A pointed closed convex cone $K$ defines $x\preceq_Ky$ iff $y-x\in K$ (Prop 4.17). Examples: the orthant, the Lorentz cone, the PSD cone (Ex. 4.18). A $K$-convex map $G$ has convex $\{x:G(x)\preceq_K0\}$.
- Problem (Def 4.21, eq. 4.4):
$$\inf\{f(x):\ G(x)\preceq_K0,\ x\in C\}.$$
Ex. 4.22 shows LP and QP as cases. See [[Linear programming]].
- Dual cone $K^*=-K^\circ$ (Def 4.24). Lagrangian dual function (eq. 4.9):
$$L(y)=\inf_{x\in C}\ f(x)+\langle y,G(x)\rangle,\qquad y\in K^*.$$

> [!theorem] Weak duality (Prop 4.25) and concavity (Prop 4.27)
> $L$ is concave and $L(y)\le f(x)$ for every feasible $x$ and $y\in K^*$. The dual problem (eq. 4.10) is $\sup_{y\in K^*}L(y)$. Strong duality (Def 4.26) means the two optimal values agree and the dual is attained.
>
> (source: pp. 74-76)

- Conic programs (eq. 4.12). LP dual with a worked example (p. 81) and the SDP dual (p. 80) follow by computing $L$. See [[LP duality]].

> [!theorem] Strong duality (Slater and closed cone, Thm 4.31)
> Strong duality holds if the problem is bounded and there is a strictly feasible point (Slater: $G(\bar x)\prec_K0$ with the interior of $K$). For LP it holds without Slater, by the valid-inequality theorem of ch. 2 (Thm 2.85, p. 84), as in [[Basu ch2 - Convex sets]].
>
> (source: pp. 81-84)

- Complementary slackness (Thm 4.32): at optimal $x^*,y^*$ with zero gap, $\langle y^*,G(x^*)\rangle=0$ and $x^*$ minimises the Lagrangian.
- Saddle point (Thm 4.33): $(x^*,y^*)$ is a saddle point of $f(x)+\langle y,G(x)\rangle$ iff $x^*$ is primal-optimal, $y^*$ is dual-optimal and there is no gap.

## 4.4 Cutting-plane methods (pp. 85-93)

Scheme (pp. 85-86): keep a localising convex set $S_t\supseteq$ the optimal set. Query the center $c_t$. If infeasible, a separation oracle returns a halfspace; if feasible, a subgradient gives a halfspace through $c_t$. Intersect and repeat. Convergence follows from volume shrinkage (Lemma 4.38, Thm 4.39).

- Center of gravity (Thm 4.41, p. 87-89): cutting a convex body through its centroid keeps between $1/e$ and $1-1/e$ of the volume (Grunbaum). So the volume falls geometrically, and the error after $N$ steps decays like $(1-1/e)^{N/d}$ (Thm 4.42, p. 89). Computing the centroid is itself hard.
- Ellipsoid method (pp. 90-93): enclose the half-ellipsoid in the minimum-volume ellipsoid, with explicit update formulas. Volume falls by
$$\mathrm{vol}(E_{t+1})\le\Big(1-\tfrac1{(d+1)^2}\Big)^{d/2}\mathrm{vol}(E_t)\quad(\text{Thm 4.46}).$$
The guarantee is polynomial in $d$ and $\log(1/\epsilon)$ (Thm 4.47, Cor 4.48). The text follows with a note that it is the first polynomial-time method for LP (p. 93).

Comparison to subgradient: cutting planes are dimension-dependent but converge in $\log(1/\epsilon)$ rather than $1/\epsilon^2$.

## Connections

- Wiki note: the LP dual and complementary slackness here are the continuous-optimisation view of the pages [[LP duality]] and [[Simplex method]].
- Wiki note: the projected subgradient method is the non-smooth ancestor of stochastic gradient training; the $MR/\sqrt N$ bound is the classical non-smooth rate.
- Convexity of the objective rests on [[Convex function]]; feasible sets on [[Convex set]] and [[Polyhedron]].

**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (pp. 67-93; proofs skimmed, statements of Thm 4.46-4.48 taken from the summary lines, update formulas not read).
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex function]] · [[Convex set]] · [[Polyhedron]] · [[Linear programming]] · [[LP duality]] · [[Simplex method]]
- [[Basu ch2 - Convex sets]] · [[Basu ch3 - Convex functions]]
