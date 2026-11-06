---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 3 (printed pp. 81-128)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch3 - The simplex method

**Summary**: Derives the [[Simplex method]] from basic directions and reduced costs, proves optimality conditions and finite termination for nondegenerate problems, covers the tableau and revised implementations, anticycling rules (lexicographic, Bland), Phase I / big-M initialization, column geometry and what is known about running time.

**Authors**: Dimitris Bertsimas, John N. Tsitsiklis · **Year**: 1997 · **File**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf pp. 97-154). Cites use printed pages; pdf = printed + 16.

---

## Problem
Given a standard-form LP $\min\mathbf c'\mathbf x$, $\mathbf A\mathbf x=\mathbf b$, $\mathbf x\ge0$ with $\mathbf A$ of full row rank, move from one [[Basic feasible solution]] to an adjacent better one until none exists.

## Method

**Feasible directions** (§3.1, pp. 83-84). A direction $\mathbf d$ is feasible at $\mathbf x\in P$ if $\mathbf x+\theta\mathbf d\in P$ for some $\theta>0$ (Def. 3.1). At a BFS with basis matrix $\mathbf B=[\mathbf A_{B(1)}\cdots\mathbf A_{B(m)}]$, $\mathbf x_B=\mathbf B^{-1}\mathbf b$. Raise one nonbasic $x_j$ to $\theta$ and keep the others nonbasic at zero: $d_j=1$, and $\mathbf A\mathbf d=0$ forces
$$\mathbf d_B=-\mathbf B^{-1}\mathbf A_j .\qquad(3.1)$$
This is the $j$th basic direction. If $\mathbf x$ is nondegenerate it is feasible; if degenerate it may immediately violate $x_{B(i)}\ge0$ (p. 84). The cost changes at rate $\mathbf c'\mathbf d=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$.

Wiki note: the book writes the reduced cost with a bar over $c_j$; this wiki writes $r_j$ (vector $\mathbf r$) throughout.

> [!definition] Reduced cost (p. 84, Def. 3.2)
> $$r_j=c_j-\mathbf c_B'\mathbf B^{-1}\mathbf A_j$$
> The reduced cost of every basic variable is zero (p. 86).

> [!theorem] Optimality conditions (p. 86, Thm 3.1)
> For a BFS $\mathbf x$ with basis $\mathbf B$ and reduced costs $\mathbf r$: (a) if $\mathbf r\ge0$ then $\mathbf x$ is optimal; (b) if $\mathbf x$ is optimal and nondegenerate then $\mathbf r\ge0$.

Proof of (a): for any feasible $\mathbf y$, with $\mathbf d=\mathbf y-\mathbf x$ one has $\mathbf c'\mathbf d=\sum_{i\in N}r_id_i\ge0$ because $d_i\ge0$ on nonbasic indices (p. 86). In the degenerate case an optimal BFS can have negative reduced costs.

> [!definition] Optimal basis (p. 87, Def. 3.3)
> $\mathbf B$ is optimal if (a) $\mathbf B^{-1}\mathbf b\ge0$ and (b) $\mathbf r'=\mathbf c'-\mathbf c_B'\mathbf B^{-1}\mathbf A\ge\mathbf 0'$.

**The iteration** (§3.2, pp. 87-91). Let $\mathbf u=-\mathbf d_B=\mathbf B^{-1}\mathbf A_j$.

> [!algorithm] An iteration of the simplex method (p. 90-91)
> 1. Start with basis columns $\mathbf A_{B(1)},\dots,\mathbf A_{B(m)}$ and BFS $\mathbf x$.
> 2. Compute $r_j$ for all nonbasic $j$. If all $\ge0$, stop: optimal. Else pick $j$ with $r_j<0$.
> 3. Compute $\mathbf u=\mathbf B^{-1}\mathbf A_j$. If no component is positive, $\theta^*=\infty$, optimal cost is $-\infty$, stop.
> 4. Otherwise
> $$\theta^*=\min_{\{i\mid u_i>0\}}\frac{x_{B(i)}}{u_i}.$$
> 5. Let $\ell$ attain the minimum. Replace $\mathbf A_{B(\ell)}$ by $\mathbf A_j$. New BFS: $y_j=\theta^*$ and $y_{B(i)}=x_{B(i)}-\theta^*u_i$ for $i\ne\ell$.

> [!theorem] Basis change is valid (p. 89, Thm 3.2)
> (a) $\mathbf A_{B(i)}$, $i\ne\ell$, and $\mathbf A_j$ are linearly independent, so $\overline{\mathbf B}$ is a basis matrix. (b) $\mathbf y=\mathbf x+\theta^*\mathbf d$ is a BFS for the basis $\overline{\mathbf B}$.

> [!theorem] Termination, nondegenerate case (p. 91, Thm 3.3)
> If the feasible set is nonempty and every BFS is nondegenerate, the method stops after finitely many iterations, with either (a) an optimal basis and BFS, or (b) $\mathbf d$ with $\mathbf A\mathbf d=0$, $\mathbf d\ge0$, $\mathbf c'\mathbf d<0$ (cost $-\infty$).

Finiteness: each step lowers the cost strictly and there are finitely many BFS.

**Pivoting rules** (p. 92-93). Entering variable: most negative $r_j$ (steepest rate), or largest decrease $\theta^*|r_j|$ (costlier per iteration, no clear win in practice). Simpler rules are often used for large problems.

**Degenerate pivots.** With $\theta^*=0$ the basis changes but the point does not (Fig. 3.3, p. 93: after a basis change the basic directions $\mathbf h,-\mathbf g$ can lead to a better vertex).

**Implementations** (§3.3, pp. 94-107).
- Row operations are left multiplication by an invertible $\mathbf Q$ (Def. 3.4, p. 96).
- Full tableau: top row $[-\mathbf c_B'\mathbf B^{-1}\mathbf b\mid\mathbf r']$, body $[\mathbf B^{-1}\mathbf b\mid\mathbf B^{-1}\mathbf A]$ (p. 99). The pivot is a Gauss-Jordan step on the entry $u_\ell>0$ chosen by the ratio $x_{B(i)}/u_i$.
- Revised simplex keeps only $\mathbf B^{-1}$ (updated by elementary row operations). Per iteration: memory $O(mn)$ vs $O(m^2)$, worst-case time $O(mn)$ for both, best case $O(mn)$ vs $O(m^2)$ (Table 3.1, p. 107).
- Practical codes reinvert periodically to control roundoff and store $\mathbf B^{-1}$ in product form (p. 107).

**Cycling and anticycling** (§3.4, pp. 108-111). Example 3.6 (p. 104) cycles through six degenerate pivots (all $\theta^*=0$) back to the starting tableau.
- Lexicographic rule: if all rows except the zeroth are lexicographically positive and the pivot row is chosen as the lexicographically smallest of $(\text{row})/u_i$ over $u_i>0$ then rows stay lexicographically positive, the zeroth row strictly increases lexicographically, and no basis repeats (Thm 3.4, p. 110).
- Bland's (smallest subscript) rule (p. 111): enter the smallest $j$ with $r_j<0$; among tied leaving variables take the smallest index. It prevents cycling and suits revised implementations that compute reduced costs one at a time.

**Initialization** (§3.5, pp. 111-118). Make $\mathbf b\ge0$, add artificial variables:
$$\min\ y_1+\cdots+y_m\quad\text{s.t.}\quad \mathbf A\mathbf x+\mathbf y=\mathbf b,\ \mathbf x,\mathbf y\ge0$$
(p. 112). $\mathbf x=0,\mathbf y=\mathbf b$ is a BFS. Positive optimal cost means the original is infeasible; zero cost gives a feasible $\mathbf x$. If artificials remain in the final basis at level zero, pivot them out using any nonzero entry of $\mathbf B^{-1}\mathbf A_j$; a row of zeros there means $\mathbf A$ has a redundant row, which is deleted (pp. 112-115, Example 3.8). Two-phase summary (p. 117): infeasibility is detected in Phase I, redundancy is repaired at the end of Phase I, unboundedness appears in Phase II, else Phase II ends optimal. The big-$M$ method minimizes $\sum_jc_jx_j+M\sum_iy_i$ with $M$ symbolic and larger than any number it is compared with (p. 117).

**Column geometry** (§3.6, pp. 119-124): an alternative picture of the method, offered to explain why it works well in practice (p. 119). **[unverified]**: details not read.

**Efficiency** (§3.7, pp. 124-128). Diameter $\Delta(n,m)$ of a polyhedron with $m$ constraints in $n$ dimensions lower-bounds iterations of any vertex-to-adjacent-vertex method.
- Hirsch conjecture: $\Delta(n,m)\le m-n$ (p. 127). False for unbounded polyhedra: $\Delta_u(n,m)\ge m-n+\lfloor n/5\rfloor$ (Klee-Walkup).
- Best known upper bound (Kalai-Kleitman): $\Delta\le\Delta_u<m^{1+\log_2n}=(2n)^{\log_2m}$.
- Exponential-iteration examples have been constructed for several popular pivoting rules, but that does not exclude a better rule, an important open problem (p. 126). Diameter examples: $\Delta(2,m)=\lfloor m/2\rfloor$, $\Delta_u(2,m)=m-2$ (Fig. 3.9). Average-case analysis is hard because "average" needs a probability model (p. 127-128).

## Results
For nondegenerate problems the simplex method terminates correctly; with an anticycling rule it always terminates; Phase I makes it complete (detects infeasible, unbounded, optimal).

## Limitations
Worst-case behaviour is exponential for known rules, while practice is much better (p. 129). Whether a polynomial pivoting rule exists is open (Hirsch bounds).

## Connections
- Same method in [[BJS ch3 - The simplex method]] (tableau first), [[BJS ch4 - Starting solution and convergence]] (two-phase, big-M, cycling) and [[BJS ch5 - Special simplex implementations and optimality conditions]] (revised, bounded variables).
- Complexity questions continue in [[BT ch8 - Complexity of LP and the ellipsoid method]] and [[BT ch9 - Interior point methods]].
- The dual simplex method is in [[BT ch4 - Duality theory]] (§4.5).

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 97-154).
**Last updated**: 2026-11-06

---

## Related pages
- [[Simplex method]] · [[Basic feasible solution]] · [[Linear programming]] · [[LP duality]] · [[Polyhedron]]
- [[BT ch2 - Geometry of linear programming]] · [[BT ch4 - Duality theory]] · [[BJS ch3 - The simplex method]]
