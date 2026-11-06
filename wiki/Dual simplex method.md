---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §4.5; Bazaraa, Jarvis, Sherali 2010, §6.4"
tags: [optimization]
---

# Dual simplex method

> [!algorithm] Dual simplex iteration (source: MIT (ch 1-5).pdf, pp. 157-158)
> Start from a tableau with all reduced costs $r_j\ge0$ (dual feasible) but possibly $\mathbf B^{-1}\mathbf b\not\ge\mathbf 0$.
> 1. If $\mathbf B^{-1}\mathbf b\ge\mathbf0$, stop: optimal for both.
> 2. Pick a row $\ell$ with $x_{B(\ell)}<0$, entries $v_i$.
> 3. If no $v_i<0$, the dual is unbounded and the primal infeasible.
> 4. Else the entering column $j$ minimizes (eq. 4.2)
> $$\frac{r_j}{|v_j|}=\min_{\{i:\,v_i<0\}}\frac{r_i}{|v_i|}.$$
> 5. Pivot; the new reduced costs stay nonnegative.

**Intuition**: the [[Simplex method]] keeps the primal feasible and works toward dual feasibility; this method does the reverse (BT p. 157). It is the simplex method run on the dual problem, in primal tableau form.

## Key facts
- BJS version: with the minimization sign convention a basis is dual feasible when $z_j-c_j\le0$ for all $j$; pivot row $r$ has $\hat b_r<0$; if $y_{rj}\ge0$ for all $j$ the primal is infeasible; the entering column attains $\min_j\{(z_j-c_j)/y_{rj}:y_{rj}<0\}$ (BJS p. 279-280).
- The dual objective does not decrease, and strictly increases without dual degeneracy, so no basis repeats (BJS p. 285).
- Primal and dual bases are paired: a basis $\mathbf B$ is primal feasible iff $\mathbf B^{-1}\mathbf b\ge\mathbf0$ and dual feasible iff $\mathbf c_N-\mathbf c_B\mathbf B^{-1}\mathbf N\ge\mathbf0$ (BJS eq. 6.11, "complementary bases").
- Natural for re-optimizing after adding a constraint or changing the right-hand side (BT ch5, [[BT ch5 - Sensitivity analysis]]) and for warm-starting in cutting plane and branch and bound methods ([[Integer programming]]).
- BJS's primal-dual method is a related algorithm that holds dual feasibility and builds primal feasibility through a restricted primal (BJS §6.5).

## Where it appears
- [[BT ch4 - Duality theory]]: §4.5.
- [[BJS ch6 - Duality and sensitivity analysis]]: §6.4-6.6.
- [[BT ch5 - Sensitivity analysis]]: re-solving after data changes.
- [[BT ch11 - Integer programming]]: Gomory cuts and branch and bound reuse the dual simplex.

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 4, 5, 11); `text_books/Linear Optimization/BJS full book.pdf` (ch. 6).
**Last updated**: 2026-11-06

---

## Related pages
- [[LP duality]] · [[Simplex method]] · [[Linear programming]] · [[Basic feasible solution]] · [[Integer programming]]
