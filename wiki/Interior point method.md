---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 9; Bazaraa, Jarvis, Sherali 2010, §8.4-8.6"
tags: [optimization]
---

# Interior point method

> [!definition] Barrier problem and central path (source: MIT (ch 1-5).pdf, pp. 419-421)
> For $\mu>0$,
> $$B_\mu(\mathbf x)=\mathbf c'\mathbf x-\mu\sum_j\log x_j$$
> $$\min\ B_\mu(\mathbf x)\ \ \text{s.t. }\mathbf A\mathbf x=\mathbf b$$
> Its minimizers $\mathbf x(\mu)$ form the central path, characterized by
> $$\mathbf A\mathbf x=\mathbf b,\ \ \mathbf x>\mathbf0$$
> $$\mathbf A'\mathbf p+\mathbf s=\mathbf c,\ \ \mathbf s>\mathbf0$$
> $$\mathbf X\mathbf S\mathbf e=\mu\mathbf e$$

**Intuition**: instead of walking along vertices like the [[Simplex method]], move through the interior of the feasible set. At $\mu\to0$ the last equation becomes complementary slackness ([[LP duality]]), and the limit of $\mathbf x(\mu)$ is an LP optimum.

## Three families

- In practice these methods are competitive with the simplex method and often beat it on large sparse problems (BT p. 393).
- Affine scaling ([[Affine scaling method]]): the approximating ellipsoid lies inside the polyhedron, whereas in the [[Ellipsoid method]] it contains it.
- Potential reduction (below): progress is measured by a nonlinear potential, not by the cost.
- Path following ([[Path-following interior point methods]]): solve a log-barrier problem approximately with Newton's method ([[Newton's method]]) and let the barrier weight fall; the optimum traces a path to the LP optimum.

All work on the standard-form pair and need a strictly positive start, obtained with an artificial variable and large cost $M$. Setting: the standard form problem and its dual
$$\min\ \mathbf c'\mathbf x\ \ \text{s.t. }\mathbf A\mathbf x=\mathbf b,\ \mathbf x\ge\mathbf0$$
$$\max\ \mathbf p'\mathbf b\ \ \text{s.t. }\mathbf p'\mathbf A\le\mathbf c'$$
with $\mathbf A$ of size $m\times n$ (BT p. 395). The interior of the feasible set $P$ is $\{\mathbf x\in P\mid\mathbf x>\mathbf0\}$.

## Potential reduction

(BT §9.3, p. 409-419) Assumption 9.3 (p. 409): $\mathbf A$ has independent rows, and strictly feasible $\mathbf x>\mathbf0$ and $(\mathbf p,\mathbf s)$ with $\mathbf s>\mathbf0$ exist for the primal and the dual
$$\max\ \mathbf p'\mathbf b\ \ \text{s.t. }\mathbf p'\mathbf A+\mathbf s'=\mathbf c',\ \mathbf s\ge\mathbf0$$
Affine scaling pushes toward the boundary and then takes tiny steps. The cure is the potential function with $q>n$ (p. 409):
$$G(\mathbf x,\mathbf s)=q\log\mathbf s'\mathbf x-\sum_{j}\log x_j-\sum_j\log s_j$$
The first term measures the duality gap, since $\mathbf c'\mathbf x-\mathbf b'\mathbf p=\mathbf s'\mathbf x$; the others penalize closeness to the boundary of the primal and the dual.

> [!theorem] Theorem 9.4 (p. 410)
> Any algorithm that keeps primal and dual feasibility and lowers $G$ by at least $\delta>0$ per iteration reaches duality gap $(\mathbf s^K)'\mathbf x^K\le\epsilon$ after $K=\big\lceil\frac{G(\mathbf x^0,\mathbf s^0)+(q-n)\log(1/\epsilon)-n\log n}{\delta}\big\rceil$ iterations.

The proof uses $G\ge n\log n+(q-n)\log\mathbf s'\mathbf x$ (Eq. 9.7), with equality when $x_js_j=\mathbf s'\mathbf x/n$.

**Direction** (p. 411-412). Linearize $G(\mathbf x+\mathbf d,\mathbf s)$ in $\mathbf d$ subject to $\mathbf A\mathbf d=\mathbf0$ and $\|\mathbf X^{-1}\mathbf d\|\le\beta$. This is the affine scaling problem with cost vector $\nabla_xG$, whose components are $\frac{q s_i}{\mathbf s'\mathbf x}-\frac1{x_i}$. Define
$$\mathbf u^k=\Big(\mathbf I-\mathbf X_k\mathbf A'(\mathbf A\mathbf X_k^2\mathbf A')^{-1}\mathbf A\mathbf X_k\Big)\Big(\frac q{(\mathbf s^k)'\mathbf x^k}\mathbf X_k\mathbf s^k-\mathbf e\Big)$$
and $\mathbf d^k=-\beta\mathbf X_k\mathbf u^k/\|\mathbf u^k\|$. The algorithm (p. 412-413) with parameters $\beta,\gamma,q$:
- If $\|\mathbf u^k\|\ge\gamma$ (primal step): $\mathbf x^{k+1}=\mathbf x^k+\mathbf d^k$, dual unchanged.
- If $\|\mathbf u^k\|<\gamma$ (dual step): $\mathbf x$ unchanged and $\mathbf p,\mathbf s$ updated so that $\mathbf A'\mathbf p+\mathbf s=\mathbf c$ and $\mathbf s>\mathbf0$ stay true.

> [!theorem] Theorem 9.5 (p. 413)
> For $0<\beta<1$, $0<\gamma<1$: (a) a primal step lowers $G$ by at least a quantity of order $\beta\gamma-\frac{\beta^2}{2(1-\beta)}$; (b) a dual step lowers it by a bounded amount depending on $q$, $n$ and $\gamma$; (c) for $q=n+\sqrt n$, $\beta\approx0.285$, $\gamma\approx0.479$, $G$ falls by at least $\delta=0.079$ per iteration.

Only the text layer was read for the exact bounds in (a)-(b). **[unverified]**

**Initialization** (Theorem 9.6, p. 417-418): artificial variables with big-$M$ costs make a strictly feasible start; the artificial problem's optima are those of the original provided $M_1,M_2$ are large enough.

**Complexity** (p. 418). With integer data bounded by $U$, $K=O(\sqrt n\log\frac1\epsilon+n^2\log(nU))$ iterations at $O(n^3)$ work each, so $O(n^{3.5}\log\frac1\epsilon+n^5\log(nU))$ arithmetic operations: polynomial. A matching lower bound of order $\sqrt n\log(1/\epsilon)$ iterations exists (Exercise 9.6). Line searches on $G$ help in practice without improving the worst case (p. 419).


## Karmarkar's projective algorithm

Proposed by N. Karmarkar at AT&T Bell Laboratories in 1984, the method that started the area (BJS §8.4, p. 402-417, image seen at p. 402; BT notes p. 448). BJS's problem form (8.4), with $\mathbf A$ of rank $m$, $m,n\ge2$, integer data and $\mathbf 1$ a row of ones:
$$\min\ \mathbf c\mathbf x$$
$$\mathbf A\mathbf x=\mathbf0,\quad\mathbf 1\mathbf x=1,\quad\mathbf x\ge\mathbf0$$
Assumption (A1): $\mathbf x_0=(1/n,\dots,1/n)'$ is feasible. Assumption (A2) and the algorithm itself (projective transformations, a potential function, steps $\mathbf x_k$ and a rounding step) were read only as headings and numeric examples (Examples 8.1-8.3, p. 410-417, where a table lists iterates such as $\mathbf x_6=(0.606509,0.060158,\dots)$, not verified). Convergence analysis (§8.5, p. 417-428, Examples 8.4-8.5) not read. The potential-reduction method above is the version analysed in detail by BT (Ye 1991).

## Directions compared
Directions at a feasible $\mathbf x$ are linear combinations of the affine scaling and centering directions:
$$\mathbf d_{\text{affine}}=-\mathbf X^2(\mathbf I-\mathbf A'(\mathbf A\mathbf X^2\mathbf A')^{-1}\mathbf A\mathbf X^2)\mathbf c$$
$$\mathbf d_{\text{centering}}=(\mathbf I-\mathbf X^2\mathbf A'(\mathbf A\mathbf X^2\mathbf A')^{-1}\mathbf A)\mathbf X\mathbf e$$
The book states the path-following direction (p. 438) is a linear combination of these two; the exact coefficients were not read from an image. **[unverified]** Centering dominates early (large $\mu$), affine scaling late. Potential reduction behaves likewise. Since path following and potential reduction are polynomial and affine scaling has no polynomial bound, centering seems responsible for polynomiality (p. 439). Guideline: the simplex method does poorly on large, massively degenerate problems, which hardly hurt interior point methods (p. 439).


## Key facts
- Three families in BT: affine scaling, potential reduction, path following (BT p. 393-395). All start from a strictly positive point.
- Affine scaling: best point of the ellipsoid $\|\mathbf Y^{-1}\mathbf d\|\le\beta$ inside the positive orthant (BT Lemma 9.2, p. 397); dual estimates $\mathbf p$ come for free.
- Path following applies Newton's method to the barrier problem (primal) or to the perturbed optimality system (primal-dual), with the barrier weight decreasing (BT §9.4-9.5; BJS §8.6). Because the system is the perturbed [[KKT conditions]], the Newton step is the core computation.
- Complexity: potential reduction takes $O(\sqrt n\log\frac1\epsilon+n^2\log(nU))$ iterations at $O(n^3)$ work each (BT p. 418); see [[Complexity of linear programming]].
- The term "Karush-Kuhn-Tucker" appears in BT for the central path system (9.17).
- Interior point codes against simplex codes in large applications: [[LP in practice]].
- Ye (1991) potential reduction; Dikin (1974) short-step affine scaling (BT p. 448) **[unverified]** beyond the names.

**Covered in**: Bertsimas-Tsitsiklis ch. 9 §9.3 and §9.6 (pp. 393-395, 409-419, 438-440), §9.1-9.5 summarised with [[Affine scaling method]] and [[Path-following interior point methods]]; Bazaraa-Jarvis-Sherali ch. 8 §8.4-8.6 (pp. 402-440); Bertsimas-Tsitsiklis ch. 12 (simplex versus interior point codes, pp. 534-562)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 9, 12; printed pp. 393-450, pdf 412, 413, 416, 425, 442 viewed as images); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8, printed pp. 402-440, pdf 417-418 viewed as images).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Ellipsoid method]] · [[Simplex method]] · [[KKT conditions]] · [[Newton's method]] · [[Affine scaling method]] · [[Path-following interior point methods]] · [[Complexity of linear programming]] · [[LP duality]] · [[LP in practice]]
