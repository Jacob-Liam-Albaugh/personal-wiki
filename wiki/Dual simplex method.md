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

**Intuition**: the [[Simplex method]] keeps the primal feasible and works toward dual feasibility; this method does the reverse (BT p. 157). It is the simplex method run on the dual problem, in primal tableau form. BJS motivate it (§6.4, p. 279): when no feasible starting basis is available without artificials, a basis that is dual feasible ($z_j-c_j\le0$ for all $j$, minimization) may be easy to find.

Worked example: BT Example 4.7 (p. 158) works one pivot. The method moves between basic feasible solutions of the dual; dual degeneracy and the relation between primal and dual bases are discussed in BT pp. 160-164 (Examples 4.8-4.9). A revised version is BT Exercise 4.23.

## BJS version

With the minimization sign convention a basis is dual feasible when $z_j-c_j\le0$ for all $j$. If $\hat b_r<0$, pick row $r$ as pivot row. If $y_{rj}\ge0$ for all $j$ in that row the primal is infeasible (BJS pp. 279-280, text). Otherwise the pivot column $k$ comes from the minimum ratio test (eq. 6.7, p. 280, text):
$$\frac{z_k-c_k}{y_{rk}}=\min_j\Big\{\frac{z_j-c_j}{y_{rj}}:\ y_{rj}<0\Big\}$$
The new row-0 entries are $(z_j-c_j)'=(z_j-c_j)-\frac{y_{rj}}{y_{rk}}(z_k-c_k)$ and are shown to remain $\le0$ in both cases $y_{rj}\ge0$ and $y_{rj}<0$ (p. 280, text). The dual objective changes by $-(z_k-c_k)\hat b_r/y_{rk}\ge0$ per iteration, strictly increasing without dual degeneracy, so no basis repeats (p. 285, text). Dual degeneracy needs a cycling rule, obtained by applying the ordinary rules of [[Simplex initialization and anticycling]] to the dual (p. 285, text). BJS Example 6.7 (pp. 281-284).

**Complementary bases** (BJS pp. 283-284, images seen). For a primal basis $\mathbf B$ the matrix pairing it is the dual basis
$$\begin{pmatrix}\mathbf B'&\mathbf0\\\mathbf N'&\mathbf I_{n-m}\end{pmatrix}$$
of rank $n$. The dual slack vector is $\mathbf w_s'=\mathbf c'-\mathbf A'\mathbf w'$, which equals $(\mathbf 0,\ \mathbf c_N-\mathbf c_B\mathbf B^{-1}\mathbf N)$ at $\mathbf w=\mathbf c_B\mathbf B^{-1}$ (eq. 6.11). The primal basis is feasible iff $\mathbf B^{-1}\mathbf b\ge\mathbf0$ and the dual basis is feasible iff $\mathbf c_N-\mathbf c_B\mathbf B^{-1}\mathbf N\ge\mathbf0$. Complementary slackness holds for the pair, since $(\mathbf w\mathbf A-\mathbf c)\mathbf x=\mathbf w_s\mathbf x=0$. In every dual simplex iteration the primal basis is not necessarily feasible and the dual basis is feasible, and at termination all KKT conditions hold.

## Primal-dual method

BJS's primal-dual method maintains dual feasibility and builds primal feasibility through a restricted primal problem solved with artificial variables (§6.5, pp. 285-293, Example 6.8 on pp. 289-293, headings and text only, not read). §6.6 (pp. 293-295) finds an initial dual feasible solution (Example 6.9).

## Key facts
- BJS version: with the minimization sign convention a basis is dual feasible when $z_j-c_j\le0$ for all $j$; pivot row $r$ has $\hat b_r<0$; if $y_{rj}\ge0$ for all $j$ the primal is infeasible; the entering column attains $\min_j\{(z_j-c_j)/y_{rj}:y_{rj}<0\}$ (BJS pp. 279-280).
- The dual objective does not decrease, and strictly increases without dual degeneracy, so no basis repeats (BJS p. 285).
- Primal and dual bases are paired: a basis $\mathbf B$ is primal feasible iff $\mathbf B^{-1}\mathbf b\ge\mathbf0$ and dual feasible iff $\mathbf c_N-\mathbf c_B\mathbf B^{-1}\mathbf N\ge\mathbf0$ (BJS eq. 6.11, "complementary bases").
- Natural for re-optimizing after adding a constraint or changing the right-hand side ([[LP sensitivity analysis]]) and for warm-starting in cutting plane and branch and bound methods ([[Integer programming]]).
- BJS's primal-dual method is a related algorithm that holds dual feasibility and builds primal feasibility through a restricted primal (BJS §6.5).

- Branch and bound and Gomory cuts reuse the dual simplex ([[Integer programming]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 4 §4.5 (pp. 156-164); Bazaraa-Jarvis-Sherali ch. 6 §6.4-6.6 (pp. 277-295)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 4, 5, 11); `text_books/Linear Optimization/BJS full book.pdf` (ch. 6; printed pages 283-284 seen as images, the rest from the text layer).
**Last updated**: 2026-11-06

---

## Related pages
- [[LP duality]] · [[Simplex method]] · [[Linear programming]] · [[Basic feasible solution]] · [[Integer programming]] · [[LP sensitivity analysis]]
