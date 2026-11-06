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

**Intuition**: to decide whether a [[Polyhedron]] $P$ is empty, enclose it in an ellipsoid, test the center, and if it violates a constraint replace the ellipsoid by a smaller one containing the half that can still hold $P$. The volume shrinks by a fixed factor each step, so the loop ends after polynomially many steps.

## Key facts
- Feasibility loop: if the center $\mathbf x_t\in P$ stop (nonempty); else take a violated constraint, cut with its halfspace, and update; if $t=t^*$ stop (empty) (BT §8.3, p. 371-372).
- Assumptions: $P$ bounded, and empty or full-dimensional; removed by perturbation and bounding, with finite precision using $O(n^3\log U)$ bits (BT p. 373-378).
- Bound $O(n^6\log(nU))$ iterations with polynomial work each (BT p. 380). BJS give $O[(m+n)^6L]$ for $\min\{\mathbf c\mathbf x:\mathbf A\mathbf x\ge\mathbf b,\mathbf x\ge\mathbf0\}$ (BJS p. 402).
- Optimization reduces to feasibility by bisection on the optimal value; BJS note $3L+2$ calls suffice for exact recovery (BJS p. 397).
- It proves [[Linear programming]] is polynomial but needs very many iterations even on moderate problems, so it is not used in practice (BT p. 380; BJS p. 402). Its remaining use is as a theoretical tool, for instance for separation-based optimization over exponentially many constraints (BJS p. 402; compare [[Integer programming]]).
- Contrast with [[Interior point method]]s: the ellipsoid contains the feasible set, the affine scaling ellipsoid lies inside it (BT ch9, p. 393).

## Where it appears
- [[BT ch8 - Complexity of LP and the ellipsoid method]]: full development.
- [[BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms]]: outline (details left to exercises).
- [[BT ch10 - Integer programming formulations]]: separation and exponentially many constraints.

**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 8-10); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Interior point method]] · [[Simplex method]] · [[Polyhedron]] · [[Convex set]]
