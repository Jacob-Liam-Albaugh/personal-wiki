---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 8 (printed pp. 359-392)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "text_books/Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch8 - Complexity of LP and the ellipsoid method

**Summary**: Shows that [[Linear programming]] with integer data is solvable in polynomial time, although the [[Simplex method]] is exponential in the worst case. The ellipsoid method decides feasibility by shrinking a sequence of ellipsoids, each at least a fixed factor smaller in volume, around the polyhedron. It also handles problems with exponentially many constraints, provided a separation oracle exists. The method is not practical; the next chapter gives [[BT ch9 - Interior point methods]], which are both efficient in theory and in practice (p. 360).

## Efficiency and complexity (§8.1, p. 360-363)
- The simplex method needs $2^n-1$ iterations on a particular $n$-variable, $2n$-constraint problem (§3.7), yet empirically "typically" about $O(m)$ iterations for $m$ equality constraints (p. 360). See [[BT ch3 - The simplex method]].
- Arithmetic model: every operation takes unit time. Bit model: each operation is decomposed into single-bit steps, which accounts for the cost of large numbers (p. 362).
- $T(n)$ is the worst-case running time over instances of size $n$ in the bit model.

> [!definition] Definition 8.3 (p. 362)
> An algorithm runs in polynomial time if there is an integer $k$ with $T(n)=O(n^k)$.

- A polynomial algorithm must also keep the numbers it produces polynomially bounded in size. Gaussian elimination is the example: $O(n^3)$ arithmetic operations, and the intermediate numbers stay polynomial, so inversion is polynomial in the bit model (p. 363).
- Polynomiality is a stable property across reasonable computation models. Worst-case efficiency can mislead: the simplex method routinely solves large problems fast (p. 363).

## The key geometric result (§8.2, p. 363-367)
An ellipsoid $E(\mathbf z,\mathbf D)$ has center $\mathbf z$ and a symmetric positive definite matrix $\mathbf D$. A ball is $E(\mathbf z,r^2\mathbf I)$.

> [!theorem] Theorem 8.1 (p. 366)
> Let $E=E(\mathbf z,\mathbf D)$ be an ellipsoid in $\mathbb R^n$, $\mathbf a\ne\mathbf0$, and $H=\{\mathbf x\mid\mathbf a'\mathbf x\ge\mathbf a'\mathbf z\}$. Define
> $$\mathbf z'=\mathbf z+\frac1{n+1}\frac{\mathbf D\mathbf a}{\sqrt{\mathbf a'\mathbf D\mathbf a}}$$
> $$\mathbf D'=\frac{n^2}{n^2-1}\Big(\mathbf D-\frac2{n+1}\frac{\mathbf D\mathbf a\mathbf a'\mathbf D}{\mathbf a'\mathbf D\mathbf a}\Big)$$
> Then $\mathbf D'$ is symmetric positive definite and $E'=E(\mathbf z',\mathbf D')$ satisfies (a) $E\cap H\subset E'$ and (b) $\mathrm{Vol}(E')<e^{-1/(2(n+1))}\,\mathrm{Vol}(E)$.

(The book writes the new center and matrix with bar notation; here the primes are used instead.) The proof first treats $E$ = unit ball, $H=\{x_1\ge0\}$ (Figure 8.2, p. 367) and then reduces the general case by a coordinate transformation. Figure 8.1 (p. 366) shows the half-ellipsoid $E_t\cap H$ covered by the smaller $E_{t+1}$.

## The ellipsoid method for feasibility (§8.3, p. 367-378)
Goal: decide whether $P=\{\mathbf x\mid\mathbf a_i'\mathbf x\ge b_i,\ i=1,\dots,m\}$ is empty. Assumptions (p. 371):
- (a) $P$ is bounded and either empty or full-dimensional. A ball $E_0=E(\mathbf x_0,r^2\mathbf I)$ of volume at most $V$ contains $P$, and $\mathrm{Vol}(P)>v$ if $P\ne\emptyset$.
- (b) Exact arithmetic including square roots (relaxed later).

**Algorithm** (box, p. 371):
1. Set $t^*=\lceil2(n+1)\log(V/v)\rceil$, $E_0=E(\mathbf x_0,r^2\mathbf I)$, $\mathbf D_0=r^2\mathbf I$, $t=0$.
2. (a) If $t=t^*$ stop: $P$ is empty. (b) If $\mathbf x_t\in P$ stop: $P$ is nonempty. (c) Otherwise find a violated constraint $\mathbf a_i'\mathbf x_t<b_i$. (d) Let $H_t=\{\mathbf x\mid\mathbf a_i'\mathbf x\ge\mathbf a_i'\mathbf x_t\}$ and set $E_{t+1}$ to the ellipsoid of Theorem 8.1 containing $E_t\cap H_t$:
$$\mathbf x_{t+1}=\mathbf x_t+\frac1{n+1}\frac{\mathbf D_t\mathbf a_i}{\sqrt{\mathbf a_i'\mathbf D_t\mathbf a_i}}$$
$$\mathbf D_{t+1}=\frac{n^2}{n^2-1}\Big(\mathbf D_t-\frac2{n+1}\frac{\mathbf D_t\mathbf a_i\mathbf a_i'\mathbf D_t}{\mathbf a_i'\mathbf D_t\mathbf a_i}\Big)$$
(e) Set $t:=t+1$.

> [!theorem] Theorem 8.2 (p. 372)
> If $P$ is bounded and either empty or full-dimensional, with prior information $\mathbf x_0,r,v,V$, the method decides correctly whether $P$ is nonempty.

Proof idea: by induction $P\subset E_k$, because a violated inequality gives $P\subset E_k\cap H_k\subset E_{k+1}$ (Thm 8.1(a)). Volumes shrink as $\mathrm{Vol}(E_{t+1})/\mathrm{Vol}(E_t)<e^{-1/(2(n+1))}$, so after $t^*$ steps $\mathrm{Vol}(E_{t^*})<v$, and then $\mathrm{Vol}(P)<v$ forces $P=\emptyset$.

Example 8.1 (p. 372): in dimension $n=1$ ellipsoids are intervals and the method is binary search on the intersection of intervals.

**Removing the assumptions** (p. 373-378). Perturbing the polyhedron to a full-dimensional $P_\varepsilon$ and bounding it (Lemma 8.3) handles degeneracy and unboundedness. Finite precision with $O(n^3\log U)$ bits keeps the numbers polynomial, and the method then needs $O(n^6\log(nU))$ iterations (p. 378). These details are technical and were not worked through here.

> [!theorem] Theorem 8.3 (p. 378)
> The linear programming feasibility problem with integer data can be solved in polynomial time.

## The ellipsoid method for optimization (§8.4, p. 378-381)
Given the primal and dual
$$\min\ \mathbf c'\mathbf x\ \ \text{s.t. }\mathbf A\mathbf x\ge\mathbf b$$
$$\max\ \mathbf b'\mathbf p\ \ \text{s.t. }\mathbf A'\mathbf p=\mathbf c,\ \mathbf p\ge\mathbf0$$
strong duality ([[BT ch4 - Duality theory]]) says both have optimal solutions exactly when this system is feasible:
$$\mathbf b'\mathbf p=\mathbf c'\mathbf x,\quad\mathbf A\mathbf x\ge\mathbf b,\quad\mathbf A'\mathbf p=\mathbf c,\quad\mathbf p\ge\mathbf0$$
Apply the feasibility method to the set $Q$ of solutions of this system. If $Q$ is not full-dimensional it is perturbed to $Q_\varepsilon$, and for small $\varepsilon$ a point of $Q$ is recovered by rounding (p. 378).

> [!theorem] Theorem 8.4 (p. 379)
> The linear programming problem with integer data can be solved in polynomial time.

**Sliding objective ellipsoid method** (p. 379). First find a feasible $\mathbf x_0$ in $F=\{\mathbf x\mid\mathbf A\mathbf x\ge\mathbf b\}$. Then test whether
$$P=F\cap\{\mathbf x\mid\mathbf c'\mathbf x<\mathbf c'\mathbf x_0\}$$
is empty. If empty, $\mathbf x_0$ is optimal. Otherwise take a better point $\mathbf x_1$ in $P$ and repeat with $\mathbf c'\mathbf x<\mathbf c'\mathbf x_1$. The added constraints are all parallel, which gives the method its name (Figure 8.4). The method also works with strict inequalities.

**In practice** (p. 380). The bound is $O(n^6\log(nU))$ iterations with polynomial work per iteration, which beats the exponential worst case of the simplex method. Yet the ellipsoid method needs a very large number of iterations even on moderate problems and has not been practically successful. The lesson is that polynomial time for all instances is not the same as efficient in practice. Deep cuts (Exercise 8.3) accelerate it but do not change this. Its lasting value is the theoretical proof that LP is efficiently solvable.

## Problems with exponentially many constraints (§8.5, p. 381-386)
Each iteration only needs a point $\mathbf x_t$ and, if $\mathbf x_t\notin P$, a violated constraint. When $m$ is exponential in $n$, scanning all constraints is too slow, so the cost hinges on Steps 2(b)-(c) (p. 381-382).

> [!definition] Definition 8.8 (p. 382)
> Given a polyhedron $P\subset\mathbb R^n$ and $\mathbf x\in\mathbb R^n$, the separation problem is to either (a) decide that $\mathbf x\in P$, or (b) find $\mathbf d$ with $\mathbf d'\mathbf x<\mathbf d'\mathbf y$ for all $\mathbf y\in P$.

This is the separating hyperplane problem of [[BT ch4 - Duality theory]] and the step met in the cutting plane method of [[BT ch6 - Large scale optimization]]. Any separating hyperplane is acceptable, not only one of the original constraints; the method's properties stay valid (p. 382).

> [!theorem] Theorem 8.5 (p. 382)
> If separation can be solved (for a family of polyhedra) in time polynomial in $n$ and $\log U$, then linear optimization over those polyhedra can also be solved in time polynomial in $n$ and $\log U$.

Under technical conditions the converse holds as well (p. 382-383, Exercise 8.10).

**Example 8.2, traveling salesman lower bound** (p. 383). For an undirected graph with edge variables $x_e$ and cut sets $\delta(S)$, the LP relaxation is
$$\min\ \sum_ec_ex_e$$
$$\sum_{e\in\delta(\{i\})}x_e=2\quad\forall i$$
$$\sum_{e\in\delta(S)}x_e\ge2\quad\forall S\ne\emptyset,N$$
$$0\le x_e\le1$$
It has exponentially many constraints. Separation: assign capacity $x_e$ to each edge and compute a minimum cut over all source/sink choices, by [[BT ch7 - Network flows]] maximum flow. If the capacity is at least $2$, $\mathbf x$ is feasible; otherwise the minimum cut $S_0$ gives a violated constraint (p. 384). So the bound is computable in polynomial time by Theorem 8.5.

**Example 8.3, probability consistency** (p. 384). Events $A_1,\dots,A_n$ with bounds $P(A_i)\le p_i$ and $P(A_i\cap A_j)\ge p_{ij}$; the question is whether a consistent probability measure exists, which is again an LP with exponentially many variables or constraints. The details were not read from a page image. **[unverified]**

## Notes
- Wiki note: the ellipsoid method is the ancestor of the cutting plane idea in [[BT ch6 - Large scale optimization]] with a volume-based termination rule. For ellipsoid cut theory, compare convex feasibility via a separation oracle ([[Convex set]]).
- Wiki note: the ellipsoid and interior point methods are polynomial; the simplex method is not known to be, but is faster in practice (pp. 360, 380).

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (pdf 375-408, printed pp. 359-392). Pages viewed as images: pdf 382, 383, 387, 394; the rest read from the text layer.
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[LP duality]] · [[Polyhedron]] · [[Convex set]]
- [[BT ch3 - The simplex method]] · [[BT ch4 - Duality theory]] · [[BT ch6 - Large scale optimization]] · [[BT ch7 - Network flows]] · [[BT ch9 - Interior point methods]] · [[BT ch11 - Integer programming]]
- [[Ellipsoid method]]
