---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 8; Bazaraa, Jarvis, Sherali 2010, §8.3"
tags: [optimization]
---

# Ellipsoid method

> [!theorem] Key geometric step (source: MIT (ch 1-5).pdf, p. 366, Thm 8.1)
> Let $E=E(\mathbf z,\mathbf D)$ be an ellipsoid in $\mathbb R^n$, $\mathbf a\ne\mathbf0$, $H=\{\mathbf x\mid\mathbf a'\mathbf x\ge\mathbf a'\mathbf z\}$. With
> $$\mathbf z'=\mathbf z+\frac1{n+1}\frac{\mathbf D\mathbf a}{\sqrt{\mathbf a'\mathbf D\mathbf a}}$$
> $$\mathbf D'=\frac{n^2}{n^2-1}\Big(\mathbf D-\frac2{n+1}\frac{\mathbf D\mathbf a\mathbf a'\mathbf D}{\mathbf a'\mathbf D\mathbf a}\Big)$$
> the ellipsoid $E'=E(\mathbf z',\mathbf D')$ contains $E\cap H$ and $\mathrm{Vol}(E')<e^{-1/(2(n+1))}\mathrm{Vol}(E)$.

**Intuition**: to decide whether a [[Polyhedron]] $P$ is empty, enclose it in an ellipsoid, test the center, and if it violates a constraint replace the ellipsoid by a smaller one containing the half that can still hold $P$. The volume shrinks by a fixed factor each step, so the loop ends after polynomially many steps. The method proves that [[Linear programming]] with integer data is solvable in polynomial time although the [[Simplex method]] is exponential in the worst case; the efficiency notions are in [[Complexity of linear programming]].

## The key geometric result

An ellipsoid $E(\mathbf z,\mathbf D)$ has center $\mathbf z$ and a symmetric positive definite matrix $\mathbf D$. A ball is $E(\mathbf z,r^2\mathbf I)$ (BT §8.2, p. 363-367).

> [!theorem] Theorem 8.1 (p. 366)
> Let $E=E(\mathbf z,\mathbf D)$ be an ellipsoid in $\mathbb R^n$, $\mathbf a\ne\mathbf0$, and $H=\{\mathbf x\mid\mathbf a'\mathbf x\ge\mathbf a'\mathbf z\}$. Define
> $$\mathbf z'=\mathbf z+\frac1{n+1}\frac{\mathbf D\mathbf a}{\sqrt{\mathbf a'\mathbf D\mathbf a}}$$
> $$\mathbf D'=\frac{n^2}{n^2-1}\Big(\mathbf D-\frac2{n+1}\frac{\mathbf D\mathbf a\mathbf a'\mathbf D}{\mathbf a'\mathbf D\mathbf a}\Big)$$
> Then $\mathbf D'$ is symmetric positive definite and $E'=E(\mathbf z',\mathbf D')$ satisfies (a) $E\cap H\subset E'$ and (b) $\mathrm{Vol}(E')<e^{-1/(2(n+1))}\,\mathrm{Vol}(E)$.

(BT write the new center and matrix with bar notation; primes are used here instead.) The proof first treats $E$ = unit ball, $H=\{x_1\ge0\}$ (Figure 8.2, p. 367) and then reduces the general case by a coordinate transformation. Figure 8.1 (p. 366) shows the half-ellipsoid $E_t\cap H$ covered by the smaller $E_{t+1}$.

## The method for feasibility

Goal: decide whether $P=\{\mathbf x\mid\mathbf a_i'\mathbf x\ge b_i,\ i=1,\dots,m\}$ is empty (BT §8.3, p. 367-378). Assumptions (p. 371):
- (a) $P$ is bounded and either empty or full-dimensional. A ball $E_0=E(\mathbf x_0,r^2\mathbf I)$ of volume at most $V$ contains $P$, and $\mathrm{Vol}(P)>v$ if $P\ne\emptyset$.
- (b) Exact arithmetic including square roots (relaxed later).

> [!algorithm] Ellipsoid method for feasibility (BT p. 371)
> 1. Set $t^*=\lceil2(n+1)\log(V/v)\rceil$, $E_0=E(\mathbf x_0,r^2\mathbf I)$, $\mathbf D_0=r^2\mathbf I$, $t=0$.
> 2. (a) If $t=t^*$ stop: $P$ is empty. (b) If $\mathbf x_t\in P$ stop: $P$ is nonempty. (c) Otherwise find a violated constraint $\mathbf a_i'\mathbf x_t<b_i$. (d) Let $H_t=\{\mathbf x\mid\mathbf a_i'\mathbf x\ge\mathbf a_i'\mathbf x_t\}$ and set $E_{t+1}$ to the ellipsoid of Theorem 8.1 containing $E_t\cap H_t$:
> $$\mathbf x_{t+1}=\mathbf x_t+\frac1{n+1}\frac{\mathbf D_t\mathbf a_i}{\sqrt{\mathbf a_i'\mathbf D_t\mathbf a_i}}$$
> $$\mathbf D_{t+1}=\frac{n^2}{n^2-1}\Big(\mathbf D_t-\frac2{n+1}\frac{\mathbf D_t\mathbf a_i\mathbf a_i'\mathbf D_t}{\mathbf a_i'\mathbf D_t\mathbf a_i}\Big)$$
> (e) Set $t:=t+1$.

> [!theorem] Theorem 8.2 (p. 372)
> If $P$ is bounded and either empty or full-dimensional, with prior information $\mathbf x_0,r,v,V$, the method decides correctly whether $P$ is nonempty.

Proof idea: by induction $P\subset E_k$, because a violated inequality gives $P\subset E_k\cap H_k\subset E_{k+1}$ (Thm 8.1(a)). Volumes shrink as $\mathrm{Vol}(E_{t+1})/\mathrm{Vol}(E_t)<e^{-1/(2(n+1))}$, so after $t^*$ steps $\mathrm{Vol}(E_{t^*})<v$, and then $\mathrm{Vol}(P)<v$ forces $P=\emptyset$.

Example 8.1 (p. 372): in dimension $n=1$ ellipsoids are intervals and the method is binary search on the intersection of intervals.

**Removing the assumptions** (p. 373-378). Perturbing the polyhedron to a full-dimensional $P_\varepsilon$ and bounding it (Lemma 8.3) handles degeneracy and unboundedness. Finite precision with $O(n^3\log U)$ bits keeps the numbers polynomial, and the method then needs $O(n^6\log(nU))$ iterations (p. 378). These details are technical and were not worked through.

> [!theorem] Theorem 8.3 (p. 378)
> The linear programming feasibility problem with integer data can be solved in polynomial time.

**Khachian's formulation** (BJS §8.3, p. 401-402). Proposed in 1979 by L. G. Khachian, answering whether a polynomial-time LP algorithm exists. It finds a solution of the open system $S=\{\mathbf x:\mathbf G\mathbf x<\mathbf g\}$ with $\mathbf G$ of size $r\times q$, $r,q\ge2$, integer data, or concludes that $S$ is empty. BJS describe it as: start with a ball centered at the origin containing enough of $S$; if the center is in $S$ stop; otherwise build a monotonically volume-shrinking sequence of ellipsoids all containing the part of $S$ caught by the initial ball. If $S$ is nonempty some center lies in $S$ within a number of iterations polynomial in the problem size; if the bound is exceeded the algorithm asserts $S$ is empty. BJS leave the details to Exercises 8.12-8.17.

## The method for optimization

Given the primal and dual (BT §8.4, p. 378-381)
$$\min\ \mathbf c'\mathbf x\ \ \text{s.t. }\mathbf A\mathbf x\ge\mathbf b$$
$$\max\ \mathbf b'\mathbf p\ \ \text{s.t. }\mathbf A'\mathbf p=\mathbf c,\ \mathbf p\ge\mathbf0$$
strong duality ([[LP duality]]) says both have optimal solutions exactly when this system is feasible:
$$\mathbf b'\mathbf p=\mathbf c'\mathbf x,\quad\mathbf A\mathbf x\ge\mathbf b,\quad\mathbf A'\mathbf p=\mathbf c,\quad\mathbf p\ge\mathbf0$$
Apply the feasibility method to the set $Q$ of solutions of this system. If $Q$ is not full-dimensional it is perturbed to $Q_\varepsilon$, and for small $\varepsilon$ a point of $Q$ is recovered by rounding (p. 378).

> [!theorem] Theorem 8.4 (p. 379)
> The linear programming problem with integer data can be solved in polynomial time.

**Sliding objective ellipsoid method** (p. 379). First find a feasible $\mathbf x_0$ in $F=\{\mathbf x\mid\mathbf A\mathbf x\ge\mathbf b\}$. Then test whether
$$P=F\cap\{\mathbf x\mid\mathbf c'\mathbf x<\mathbf c'\mathbf x_0\}$$
is empty. If empty, $\mathbf x_0$ is optimal. Otherwise take a better point $\mathbf x_1$ in $P$ and repeat with $\mathbf c'\mathbf x<\mathbf c'\mathbf x_1$. The added constraints are all parallel, which gives the method its name (Figure 8.4). The method also works with strict inequalities.

**Bisection** (BJS §8.1, p. 393-397). An LP optimization can also be solved through the decision problem by bisection on the interval of uncertainty of the optimal value. After $3L+2$ calls to a polynomial decision algorithm the optimal value is localized to an interval short enough that a polynomial rounding scheme recovers an exact solution (p. 397; the interval endpoints involve powers of 2 that were garbled in the text layer).

## In practice

The bound is $O(n^6\log(nU))$ iterations with polynomial work per iteration (BT p. 380); BJS give $O[(m+n)^6L]$ for $\min\{\mathbf c\mathbf x:\mathbf A\mathbf x\ge\mathbf b,\mathbf x\ge\mathbf0\}$ (p. 402). That beats the exponential worst case of the simplex method, yet the ellipsoid method needs a very large number of iterations even on moderate problems (BJS: about 100 variables can need enormous effort, with practical performance following the worst-case bound) and has not been practically successful. The lesson is that polynomial time for all instances is not the same as efficient in practice. Deep cuts (BT Exercise 8.3) accelerate it but do not change this. Its lasting value is the theoretical proof that LP is efficiently solvable and its use as a tool for row generation in combinatorial optimization (BJS p. 402).

## Problems with exponentially many constraints

Each iteration only needs a point $\mathbf x_t$ and, if $\mathbf x_t\notin P$, a violated constraint. When $m$ is exponential in $n$, scanning all constraints is too slow, so the cost hinges on Steps 2(b)-(c) (BT §8.5, p. 381-386).

> [!definition] Definition 8.8 (p. 382)
> Given a polyhedron $P\subset\mathbb R^n$ and $\mathbf x\in\mathbb R^n$, the separation problem is to either (a) decide that $\mathbf x\in P$, or (b) find $\mathbf d$ with $\mathbf d'\mathbf x<\mathbf d'\mathbf y$ for all $\mathbf y\in P$.

This is the separating hyperplane problem of [[Farkas lemma]] and the step met in [[Cutting-plane methods]]. Any separating hyperplane is acceptable, not only one of the original constraints; the method's properties stay valid (p. 382).

> [!theorem] Theorem 8.5 (p. 382)
> If separation can be solved (for a family of polyhedra) in time polynomial in $n$ and $\log U$, then linear optimization over those polyhedra can also be solved in time polynomial in $n$ and $\log U$.

Under technical conditions the converse holds as well (p. 382-383, BT Exercise 8.10).

> [!example] Example 8.2, traveling salesman lower bound (p. 383)
> For an undirected graph with edge variables $x_e$ and cut sets $\delta(S)$, the LP relaxation is
> $$\min\ \sum_ec_ex_e$$
> $$\sum_{e\in\delta(\{i\})}x_e=2\quad\forall i$$
> $$\sum_{e\in\delta(S)}x_e\ge2\quad\forall S\ne\emptyset,N$$
> $$0\le x_e\le1$$

It has exponentially many constraints. Separation: assign capacity $x_e$ to each edge and compute a minimum cut over all source/sink choices, by maximum flow ([[Network flow problem]]). If the capacity is at least $2$, $\mathbf x$ is feasible; otherwise the minimum cut $S_0$ gives a violated constraint (p. 384). So the bound is computable in polynomial time by Theorem 8.5. The same pattern drives the scheduling LP of [[LP in practice]].

Example 8.3, probability consistency (p. 384): events $A_1,\dots,A_n$ with bounds $P(A_i)\le p_i$ and $P(A_i\cap A_j)\ge p_{ij}$; the question is whether a consistent probability measure exists, which is again an LP with exponentially many variables or constraints. The details were not read from a page image **[unverified]**.

## General convex version

For a general convex body the method is a [[Cutting-plane methods|cutting-plane method]] (Basu §4.4, pp. 90-93). Volume shrinks as $\mathrm{vol}(E_{t+1})\le(1-1/(d+1)^2)^{d/2}\mathrm{vol}(E_t)$ (Basu Thm 4.46), giving an iteration count polynomial in $d$ and $\log(1/\epsilon)$ (Thm 4.47, Cor 4.48).

## Key facts
- Feasibility loop: if the center $\mathbf x_t\in P$ stop (nonempty); else take a violated constraint, cut with its halfspace, and update; if $t=t^*$ stop (empty) (BT §8.3, p. 371-372).
- Assumptions: $P$ bounded, and empty or full-dimensional; removed by perturbation and bounding, with finite precision using $O(n^3\log U)$ bits (BT p. 373-378).
- Bound $O(n^6\log(nU))$ iterations with polynomial work each (BT p. 380); BJS give $O[(m+n)^6L]$ (p. 402).
- Optimization reduces to feasibility by bisection on the optimal value (BJS: $3L+2$ calls suffice for exact recovery, p. 397) or by the sliding objective (BT p. 379).
- It proves [[Linear programming]] is polynomial but needs very many iterations even on moderate problems, so it is not used in practice (BT p. 380; BJS p. 402).
- Contrast with [[Interior point method]]s: the ellipsoid contains the feasible set, the affine scaling ellipsoid lies inside it ([[Affine scaling method]], BT p. 393).
- The ellipsoid method is the ancestor of the cutting plane idea with a volume-based termination rule; convex feasibility via a separation oracle ([[Convex set]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 8 §8.2-8.5 (pp. 363-386); Bazaraa-Jarvis-Sherali ch. 8 §8.1 and §8.3 (pp. 393-397, 401-402); Basu ch. 4 §4.4 (pp. 90-93)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 8-10; printed pp. 359-392, pdf pages 382, 383, 387, 394 viewed as images); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8; printed pp. 393-402, pdf 417-418 viewed as images); `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (§4.4).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Interior point method]] · [[Simplex method]] · [[Polyhedron]] · [[Convex set]] · [[Complexity of linear programming]] · [[Cutting-plane methods]] · [[LP duality]] · [[LP in practice]] · [[Integer programming]]
