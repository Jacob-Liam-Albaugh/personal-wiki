---
type: method
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 4 §4.4, Lemma 4.38, Thms 4.39-4.48 (pp. 85-93)"
tags: [optimization]
---

# Cutting-plane methods

**Summary**: Minimise a convex function over a convex set by repeatedly cutting away half of a localising set with a hyperplane obtained from a separation oracle or a subgradient. Progress is measured by volume shrinkage, which gives $\log(1/\epsilon)$ convergence at a cost polynomial in dimension.

---

> [!algorithm] Cutting-plane scheme (Basu pp. 85-86)
> Keep a localising convex set $S_t\supseteq$ the optimal set. Query its center $c_t$.
> - If $c_t$ is infeasible, a separation oracle ([[Convex set]]) returns a halfspace containing the feasible set.
> - If $c_t$ is feasible, a subgradient ([[Convex function]]) gives a halfspace through $c_t$ containing all better points.
>
> Intersect $S_t$ with that halfspace and repeat. Convergence follows from volume shrinkage (Lemma 4.38, Thm 4.39).

## Center of gravity (Thm 4.41, pp. 87-89)

Cutting a convex body through its centroid keeps between $1/e$ and $1-1/e$ of the volume (Grunbaum). So the volume falls geometrically and the error after $N$ steps decays like $(1-1/e)^{N/d}$ (Thm 4.42, p. 89). Computing the centroid is itself hard.

## Ellipsoid method (pp. 90-93)

Enclose the half-ellipsoid in the minimum-volume ellipsoid, with explicit update formulas. Volume falls by
$$\mathrm{vol}(E_{t+1})\le\Big(1-\tfrac1{(d+1)^2}\Big)^{d/2}\mathrm{vol}(E_t)\quad(\text{Thm 4.46}).$$
The guarantee is polynomial in $d$ and $\log(1/\epsilon)$ (Thm 4.47, Cor 4.48). Basu notes it is the first polynomial-time method for LP (p. 93). The LP-specific development, with the update formulas, is on [[Ellipsoid method]].

## Cutting planes for linear and integer programs

**Separation and optimization.** The [[Ellipsoid method]] needs only a point and, if it is infeasible, a separating hyperplane (the separation problem, BT Def. 8.8, p. 382). If separation is polynomial for a family of polyhedra, so is optimization over them (BT Thm 8.5, p. 382). Applications: the single-machine scheduling LP with exponentially many constraints and a polynomial separation (BT Thm 12.2, p. 555, see [[LP in practice]]) and the TSP cut LP of BT Example 8.2 (separation by minimum cut).

**Integer programs** (BT §11.1, pp. 480-484). Solve the LP relaxation; if the optimum $\mathbf x^*$ is not integer, add a linear inequality satisfied by every integer feasible point but violated by $\mathbf x^*$ (a cut), and re-solve. Repeat until the LP optimum is integer.

**Gomory cut.** From an optimal basis take a tableau row with fractional right side, $N$ the nonbasic indices:
$$x_i+\sum_{j\in N}\bar a_{ij}x_j=\bar a_{i0}$$
Since $x_j\ge0$, rounding the coefficients down weakens the left side, and for integer $\mathbf x$ it is an integer, so
$$x_i+\sum_{j\in N}\lfloor\bar a_{ij}\rfloor x_j\le\lfloor\bar a_{i0}\rfloor$$
It cuts off $\mathbf x^*$ because $x_i^*=\bar a_{i0}$ and $x_j^*=0$ on $N$. Re-solving with the [[Dual simplex method]] and anticycling rules terminates finitely (Gomory 1958), but pure Gomory cuts have not worked well in practice (BT p. 482).

> [!example] Example 11.2 (BT pp. 482-484)
> Minimize $x_1-2x_2$ s.t. $-4x_1+6x_2\le9$, $x_1+x_2\le4$, $\mathbf x\ge\mathbf0$ integer. The LP optimum is $(1.5,2.5)$; the cut $x_2\le2$, then $-3x_1+5x_2\le7$, reaches the integer optimum $(1,2)$.

**Problem-specific cuts** (BT Example 11.3, p. 484): for weighted independent set, clique inequalities $\sum_{i\in K}x_i\le1$ for each clique $K$ are far stronger than edge inequalities. See [[Integer programming]] and [[Branch and bound]] (branch and cut).

**Dual view** (BT §6.3, pp. 236-239). [[Column generation]] on a primal LP is the cutting-plane method on its dual: a missing column is a violated dual constraint, and pricing is separation. The dual is solved over the constraints generated so far; the pricing problem either returns a most violated constraint or certifies dual feasibility (see [[Dantzig-Wolfe decomposition]]).

## Key facts
- Cutting planes are dimension-dependent but converge in $\log(1/\epsilon)$, against $1/\epsilon^2$ for the [[Subgradient method]].
- The only access to the problem is through oracles, so the method applies to convex sets with exponentially many constraints.

**Covered in**: Basu, Introduction to Convexity ch. 4 §4.4 (pp. 85-93); Bertsimas-Tsitsiklis §6.3 (pp. 236-239), §8.5 (p. 382), §11.1 (pp. 480-484)
**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (pp. 85-93; proofs skimmed, statements of Thm 4.46-4.48 taken from the summary lines, update formulas not read); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 6, 8, 11).
**Last updated**: 2026-11-06

---

## Related pages
- [[Ellipsoid method]] · [[Subgradient method]] · [[Convex set]] · [[Convex function]] · [[Linear programming]]
- [[Column generation]] · [[Integer programming]] · [[Branch and bound]] · [[Dual simplex method]] · [[Dantzig-Wolfe decomposition]] · [[LP in practice]]
