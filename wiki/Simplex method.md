---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 3; Bazaraa, Jarvis, Sherali 2010, ch. 3-5"
tags: [optimization]
---

# Simplex method

> [!algorithm] An iteration of the simplex method (source: MIT (ch 1-5).pdf, pp. 90-91)
> 1. Start with basis columns $\mathbf A_{B(1)},\dots,\mathbf A_{B(m)}$ and a [[Basic feasible solution]] $\mathbf x$.
> 2. Compute reduced costs $r_j=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$. If all are $\ge0$, stop: optimal. Else pick $j$ with $r_j<0$.
> 3. Compute $\mathbf u=\mathbf B^{-1}\mathbf A_j$. If no component is positive, the cost is $-\infty$.
> 4. Otherwise
> $$\theta^*=\min_{\{i\mid u_i>0\}}\frac{x_{B(i)}}{u_i}.$$
> 5. Let $\ell$ attain the minimum. Replace $\mathbf A_{B(\ell)}$ by $\mathbf A_j$.

**Intuition**: walk along edges of the [[Polyhedron]] from corner to adjacent corner, each time to a cheaper one, until no edge improves the cost. BJS write the reduced cost as $z_j-c_j$ with the opposite sign convention (enter when $z_j-c_j>0$ in a minimization), and BT write $r_j$.

## Key facts
- Optimality: $\mathbf r\ge\mathbf 0$ at a BFS implies optimal; the converse holds if the BFS is nondegenerate (BT Thm 3.1, p. 86).
- Without degeneracy the method stops finitely at an optimal basis or a ray of unbounded cost (BT Thm 3.3, p. 91).
- With degeneracy it can cycle (BT Example 3.6, p. 104; BJS Beale's example, ch4). Fixes: lexicographic rule (BT Thm 3.4) and Bland's smallest-index rule (BT p. 111; BJS ch4, p. 180).
- Implementations: full tableau, revised simplex keeping $\mathbf B^{-1}$, bounded-variable simplex ([[BJS ch5 - Special simplex implementations and optimality conditions]]).
- Initialization: Phase I with artificial variables, big-M, single artificial variable.
- Worst case is exponential: BT cite $2^n-1$ iterations on a particular problem (ch8, §8.1); BJS give a construction taking $2^{n-1}$ pivots (ch8, §8.2). Empirically about $O(m)$ iterations are typical (BT ch8, p. 360).
- At an optimal basis, $\mathbf p'=\mathbf c_B'\mathbf B^{-1}$ is dual optimal; this proves strong duality ([[LP duality]]). The [[Dual simplex method]] runs the same tableau with the roles of feasibility swapped.
- Specializations: network simplex on spanning trees ([[Network flow problem]]), column generation and [[Dantzig-Wolfe decomposition]].

## Where it appears
- [[BT ch3 - The simplex method]]: derivation, tableau and revised forms, anticycling, initialization.
- [[BJS ch3 - The simplex method]], [[BJS ch4 - Starting solution and convergence]], [[BJS ch5 - Special simplex implementations and optimality conditions]].
- [[BT ch5 - Sensitivity analysis]], [[BJS ch6 - Duality and sensitivity analysis]]: re-optimizing after data changes.
- [[BT ch8 - Complexity of LP and the ellipsoid method]], [[BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms]]: running time.
- [[BJS ch9 - Minimal cost network flows]], [[BT ch7 - Network flows]]: tree-based version.

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (ch. 3, 8); `Linear Optimization/BJS full book.pdf` (ch. 3-5, 8-9).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Basic feasible solution]] · [[Dual simplex method]] · [[LP duality]] · [[Interior point method]] · [[Ellipsoid method]] · [[Polyhedron]]
