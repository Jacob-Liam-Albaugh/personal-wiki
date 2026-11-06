---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 1 (printed pp. 1-40)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch1 - Introduction

**Summary**: Chapter 1 of *Introduction to Linear Optimization* defines the [[Linear programming]] problem in general and standard form, shows how to convert between them, models real problems as LPs, extends LP to piecewise linear convex costs, gives the graphical picture, and reviews linear algebra and operation counts.

**Authors**: Dimitris Bertsimas, John N. Tsitsiklis (MIT) · **Year**: 1997 · **File**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf p. 17-56; pdf page = printed page + 16)

---

## Problem
Minimize a linear cost over a set cut out by linear equalities and inequalities. Page cites below use printed page numbers.

## Method

> [!definition] General form (source: MIT (ch 1-5).pdf, p. 3, eq. 1.1)
> Minimize $\mathbf c'\mathbf x$ subject to
> $$\mathbf a_i'\mathbf x\ge b_i,\quad i\in M_1$$
> $$\mathbf a_i'\mathbf x\le b_i,\quad i\in M_2$$
> $$\mathbf a_i'\mathbf x= b_i,\quad i\in M_3$$
> $$x_j\ge 0\ (j\in N_1),\qquad x_j\le 0\ (j\in N_2)$$

A $\mathbf x$ meeting all constraints is a feasible solution; the set of them is the feasible set. A variable in neither $N_1$ nor $N_2$ is free. If for every real $K$ some feasible $\mathbf x$ has cost below $K$, the cost is $-\infty$ (unbounded). Maximizing $\mathbf c'\mathbf x$ is minimizing $-\mathbf c'\mathbf x$ (p. 3).

An equality is two inequalities, and $\mathbf a_i'\mathbf x\le b_i$ is $(-\mathbf a_i)'\mathbf x\ge -b_i$. So every LP can be written (eq. 1.2, p. 4) as
$$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\quad \mathbf A\mathbf x\ge\mathbf b .$$

> [!definition] Standard form (source: p. 4, eq. 1.3)
> $$\min\ \mathbf c'\mathbf x\quad\text{s.t.}\quad \mathbf A\mathbf x=\mathbf b,\ \ \mathbf x\ge\mathbf 0 .$$
> Reading: $\sum_i \mathbf A_i x_i=\mathbf b$ synthesizes the target $\mathbf b$ from nonnegative amounts of the $n$ column "resources" $\mathbf A_i$, at unit cost $c_i$.

**Reduction to standard form** (p. 5-6). Two steps:
- Free variable: replace $x_j$ by $x_j^+-x_j^-$ with $x_j^\pm\ge0$.
- Inequality: $\sum_j a_{ij}x_j\le b_i$ becomes $\sum_j a_{ij}x_j+s_i=b_i$, $s_i\ge0$ (slack); a $\ge$ gets $-s_i$ (surplus).

Equivalent means a feasible point of one maps to a feasible point of the other with the same cost, so optimal costs agree. The book uses $\mathbf A\mathbf x\ge\mathbf b$ for theory and standard form for the [[Simplex method]] and interior point methods (p. 6).

**Examples of LP models** (§1.2, pp. 6-20): diet problem (Example 1.3), production planning, multiperiod planning, scheduling, network flow and path choice in communication networks, pattern classification.

> [!definition] Convex / concave function (source: p. 15, Def. 1.1)
> $f$ is convex if for all $\mathbf x,\mathbf y$ and $\lambda\in[0,1]$:
> $$f(\lambda\mathbf x+(1-\lambda)\mathbf y)\le\lambda f(\mathbf x)+(1-\lambda)f(\mathbf y)$$
> Concave: reverse inequality. See [[Convex function]].

> [!theorem] Max of convex functions (source: p. 16, Thm 1.1)
> If $f_1,\dots,f_m$ are convex, then $f(\mathbf x)=\max_i f_i(\mathbf x)$ is convex.

A function $\max_i(\mathbf c_i'\mathbf x+d_i)$ is piecewise linear convex, e.g. $|x|=\max\{x,-x\}$. Minimizing it over $\mathbf A\mathbf x\ge\mathbf b$ is an LP: add a variable $z$ with
$$\min\ z\quad\text{s.t.}\quad z\ge \mathbf c_i'\mathbf x+d_i\ \ \forall i,\ \ \mathbf A\mathbf x\ge\mathbf b .$$
(source: p. 17.) Also $f(\mathbf x)\le h$ with $f$ piecewise linear convex becomes the linear constraints $\mathbf f_i'\mathbf x+g_i\le h$. A piecewise linear approximation can turn a smooth function into a nonsmooth one (p. 17).

**Absolute values** (p. 18, 1.3). For $c_i\ge0$, $\min\sum c_i|x_i|$ s.t. $\mathbf A\mathbf x\ge\mathbf b$ becomes:
$$\min\ \sum_i c_iz_i\quad\text{s.t.}\ \ \mathbf A\mathbf x\ge\mathbf b,\ \ x_i\le z_i,\ -x_i\le z_i$$
Alternative: $x_i=x_i^+-x_i^-$, cost $\sum c_i(x_i^++x_i^-)$. At an optimum one of $x_i^\pm$ is zero if $c_i>0$. Nonnegative $c_i$ is essential, otherwise the cost is nonconvex. Applications: data fitting ($\ell_1$ and $\ell_\infty$ fits), optimal control of linear systems, a rocket soft-landing problem (min fuel $\sum|a_t|$ or min peak thrust $\max_t|a_t|$) (pp. 18-21).

**Graphical solution** (§1.4, pp. 21-25). Level sets $\mathbf c'\mathbf x=z$ are lines (planes) orthogonal to $\mathbf c$; slide them in direction $-\mathbf c$ until leaving the feasible set. Example 1.6: minimize $-x_1-x_2$ s.t. $x_1+2x_2\le3$, $2x_1+x_2\le3$, $\mathbf x\ge0$; optimum $(1,1)$ with cost $-2$, a corner (p. 21). Example 1.8 lists the cases (p. 23-24):
- unique optimum;
- multiple optima (bounded or unbounded optimal set);
- cost $-\infty$ with no optimal solution;
- empty feasible set.

The book notes that "feasible, finite cost, but no optimum" (e.g. $\min 1/x$, $x>0$) never happens for LP (p. 24). If an optimum exists, one is usually at a corner, made precise in ch. 2 ([[BT ch2 - Geometry of linear programming]]).

**Linear algebra and operation counts** (§1.5-1.6, pp. 26-33). Span, basis, rank, invertibility (Thm 1.2 lists equivalent conditions for a square matrix). Operation counts: inner product $2n-1$, matrix product $(2n-1)n^2$ (Example 1.9, p. 32). $O$, $\Omega$, $\Theta$ defined in Def. 1.2. Gaussian elimination and matrix inversion cost $O(n^3)$ (Example 1.10, p. 33). Polynomial time $O(n^k)$ versus exponential $O(2^{cn})$; worst-case analysis is the convention.

## Results
No theorems on LP itself; the chapter sets up forms, reformulations and geometric intuition.

## Limitations
Wiki note: the $1/x$ example is the only warning that "bounded below" does not imply "attained" in general convex optimization; the guarantee for LP comes from [[Simplex method]] / [[Polyhedron]] theory.

## Connections
- Same material in [[BJS ch1 - Introduction]] (their form: min $\mathbf c\mathbf x$, $\mathbf A\mathbf x\le\mathbf b$ etc.).
- Piecewise linear convex costs use [[Convex function]]; the $\ell_1$ trick is the LP form of [[LASSO]]-type absolute-value penalties.
- Next: [[BT ch2 - Geometry of linear programming]].

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (also contained in `MIT (ch 1-2).pdf`, pp. 2-80 = pdf 17-95 of the larger file).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[LP duality]] · [[Polyhedron]] · [[Convex function]] · [[Convex set]]
- [[BT ch2 - Geometry of linear programming]] · [[BJS ch1 - Introduction]]
