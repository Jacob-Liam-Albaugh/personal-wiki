---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, §6.1-6.2"
tags: [optimization]
---

# Column generation

> [!algorithm] Delayed column generation (source: MIT (ch 1-5).pdf, pp. 232-234)
> For a standard form LP with too many columns to store, run the revised [[Simplex method]] keeping only the basic columns and the entering one. To find an entering variable without listing every column, solve the pricing problem (eq. 6.1)
> $$\min_i\ r_i$$
> over all columns $i$, often easy by problem structure. If the minimum is $\ge0$ the current solution is optimal; otherwise the minimizing column enters (p. 233).

**Intuition**: revised simplex only ever needs $\mathbf B^{-1}$ and one entering column, so generate columns on demand. It is the primal side of the [[Cutting-plane methods]] applied to the dual, and the engine of [[Dantzig-Wolfe decomposition]], whose subproblem is the pricing problem.

## Key facts
- Variants differ in which columns the restricted problem keeps (p. 234): (a) only the basic columns plus the entering one; (b) every column that ever became basic; (c) a moderate set, dropping old ones. All are special cases of revised simplex, so they terminate without degeneracy, and the lexicographic rule prevents cycling.
- Dual view (BT §6.3, p. 236-239): maximize $\mathbf p'\mathbf b$ s.t. $\mathbf p'\mathbf A_i\le c_i$ for huge numbers of $i$ (eq. 6.7); solve the dual over a subset $I$ of constraints (eq. 6.8) to get $\mathbf p^*$. If $\mathbf p^*$ satisfies all constraints it is optimal, since the relaxed problem has fewer constraints. Else find a violated one by the separation problem, e.g. minimize $c_i-(\mathbf p^*)'\mathbf A_i$ over $i$ (eq. 6.9); a negative minimum gives a violated constraint, which is added. Constraints that become inactive may be dropped (Fig. 6.1, pp. 238-239). The computation is revised simplex on the primal, so column generation and cutting planes are the same algorithm.
- The pricing step of the [[Network simplex method]] is the same idea.

## Cutting stock problem (BT §6.2, pp. 234-236)
Large rolls of width $W$ are cut into $b_i$ rolls of width $w_i$ ($w_i<W$, integers). A pattern $j$ is a column $\mathbf A_j$ of nonnegative integers $a_{ij}$ with $\sum_iw_ia_{ij}\le W$ (p. 234). The LP over all patterns has exponentially many columns. Pricing a pattern with dual prices $p_i$ is an integer knapsack problem (eq. 6.5, p. 236):
$$\max\ \sum_ip_ia_i\quad\text{s.t. }\sum_iw_ia_i\le W,\ a_i\ge0\text{ integer}$$
solved by dynamic programming in $O(mW)$ time. With $F(v)=0$ for $v<w_{\min}$, for larger $v$
$$F(v)=\max_i\{F(v-w_i)+p_i\}$$
(eq. 6.6, p. 236; the OCR of the displayed recursion is garbled, so the form is taken from the surrounding text). Dynamic programming for knapsack reappears in [[Integer programming]]; multicommodity flows are another standard source of column generation ([[Multicommodity flow]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 6 §6.1-6.3 (pp. 232-239)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 6).
**Last updated**: 2026-11-06

---

## Related pages
- [[Dantzig-Wolfe decomposition]] · [[Cutting-plane methods]] · [[Benders decomposition]] · [[Simplex method]] · [[LP duality]]
- [[Integer programming]] · [[Network simplex method]] · [[Linear programming]]
