---
type: concept
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 4 §4.3, Defs 4.17-4.26, Props 4.25, 4.27, Thms 4.31-4.33 (pp. 72-84)"
tags: [optimization]
---

# Lagrangian duality

**Summary**: For a convex program with conic constraints, the Lagrangian dual function is a concave lower bound on the optimal value. Weak duality always holds; strong duality needs a constraint qualification such as Slater's condition, except for LP where it holds automatically.

---

## Conic programs (Basu pp. 72-76)

- A pointed closed convex cone $K$ defines $x\preceq_Ky$ iff $y-x\in K$ (Prop 4.17). Examples: the orthant, the Lorentz cone, the PSD cone (Ex. 4.18). A $K$-convex map $G$ has convex $\{x:G(x)\preceq_K0\}$.
- Problem (Def 4.21, eq. 4.4):
$$\inf\{f(x):\ G(x)\preceq_K0,\ x\in C\}.$$
Ex. 4.22 shows [[Linear programming]] and QP as cases.
- Dual cone $K^*=-K^\circ$ (Def 4.24; polar from [[Convex set]]). Lagrangian dual function (eq. 4.9):
$$L(y)=\inf_{x\in C}\ f(x)+\langle y,G(x)\rangle,\qquad y\in K^*.$$

> [!theorem] Weak duality (Prop 4.25) and concavity (Prop 4.27)
> $L$ is concave and $L(y)\le f(x)$ for every feasible $x$ and $y\in K^*$. The dual problem (eq. 4.10) is $\sup_{y\in K^*}L(y)$. Strong duality (Def 4.26) means the two optimal values agree and the dual is attained.
>
> (source: Basu pp. 74-76)

Conic programs have the form of eq. 4.12. The LP dual (worked example, p. 81) and the SDP dual (p. 80) follow by computing $L$; the LP case is [[LP duality]].

> [!theorem] Strong duality (Slater and closed cone, Thm 4.31)
> Strong duality holds if the problem is bounded and there is a strictly feasible point (Slater: $G(\bar x)\prec_K0$ with the interior of $K$). For LP it holds without Slater, by the valid-inequality theorem for polyhedra (Thm 2.85, p. 84; see [[Convex set]]).
>
> (source: Basu pp. 81-84)

## Optimality through the Lagrangian

- Complementary slackness (Thm 4.32): at optimal $x^*,y^*$ with zero gap, $\langle y^*,G(x^*)\rangle=0$ and $x^*$ minimises the Lagrangian.
- Saddle point (Thm 4.33): $(x^*,y^*)$ is a saddle point of $f(x)+\langle y,G(x)\rangle$ iff $x^*$ is primal-optimal, $y^*$ is dual-optimal and there is no gap.
- For the LP and nonlinear forms of the optimality system see [[KKT conditions]].

## Partial duality for linear programs

General duality for LPs (BT §4.10, p. 184). Primal: minimize $\mathbf c'\mathbf x$ s.t. $\mathbf A\mathbf x\ge\mathbf b$, $\mathbf x\in P$ with $P=\{\mathbf x\mid\mathbf D\mathbf x\ge\mathbf d\}$. Pricing only the constraints $\mathbf A\mathbf x\ge\mathbf b$ gives the dual function
$$g(\mathbf p)=\min_{\mathbf x\in P}\big[\mathbf c'\mathbf x+\mathbf p'(\mathbf b-\mathbf A\mathbf x)\big]$$
and the dual problem: maximize $g(\mathbf p)$ s.t. $\mathbf p\ge\mathbf0$. Weak duality (BT Thm 4.17): $g(\mathbf p)\le\mathbf c'\mathbf x$ for feasible pairs. Strong duality (BT Thm 4.18): if the primal has an optimal solution, so does the dual and the costs are equal. [[LP duality]] is the case $P=\{\mathbf x\ge\mathbf0\}$.

Leaving some constraints un-priced is the idea behind decomposition and [[Lagrangian relaxation]]: for an integer program the dual bound satisfies $Z_{LP}\le Z_D\le Z_{IP}$, it gives the Held-Karp TSP bound, and the convexified master equals the Dantzig-Wolfe master (BT Thm 11.4).

## Key facts
- The Lagrangian dual function of an integer program is concave and piecewise linear, which is the basis of Lagrangean relaxation ([[Integer programming]], [[Convex function]]).
- The dual function is the pointwise infimum of affine functions of $y$, hence concave ([[Convex function]], closure under suprema).

**Covered in**: Basu, Introduction to Convexity ch. 4 §4.3 (pp. 72-84); Bertsimas-Tsitsiklis §4.10 (p. 184), §11.4
**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (pp. 72-84; proofs skimmed); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (§4.10, ch. 11).
**Last updated**: 2026-11-06

---

## Related pages
- [[KKT conditions]] · [[LP duality]] · [[Linear programming]] · [[Convex function]] · [[Convex set]] · [[Farkas lemma]] · [[Integer programming]]
- [[Lagrangian relaxation]] · [[Dantzig-Wolfe decomposition]]
