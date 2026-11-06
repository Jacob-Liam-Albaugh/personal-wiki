---
type: concept
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 1 §1.2-1.3; Bazaraa, Jarvis, Sherali 2010, ch. 1 §1.2"
tags: [optimization]
---

# LP modelling

**Summary**: How practical problems become [[Linear programming]] models: the standard catalogue of applications, and the reformulations (extra variables) that turn piecewise linear convex costs, absolute values and minimax objectives into linear programs.

## Catalogue of models

- Bertsimas-Tsitsiklis (BT §1.2, pp. 6-20): diet problem (Example 1.3), production planning, multiperiod planning, scheduling, network flow and path choice in communication networks, pattern classification.
- Bazaraa-Jarvis-Sherali (BJS §1.2, pp. 7-18): a feed mix problem, a cutting stock problem, the transportation problem ([[Network flow problem]]), capital budgeting, tanker scheduling and a multiperiod coal blending and distribution problem, with a remark that integrality is handled later ([[Integer programming]]). Headings come from the text layer; the models were not individually verified.
- Large-scale applications (fleet assignment, air traffic flow, scheduling) are in [[LP in practice]].

## Piecewise linear convex costs

> [!definition] Convex / concave function (source: p. 15, Def. 1.1)
> $f$ is convex if for all $\mathbf x,\mathbf y$ and $\lambda\in[0,1]$:
> $$f(\lambda\mathbf x+(1-\lambda)\mathbf y)\le\lambda f(\mathbf x)+(1-\lambda)f(\mathbf y)$$
> Concave: reverse inequality. See [[Convex function]].

> [!theorem] Max of convex functions (source: p. 16, Thm 1.1)
> If $f_1,\dots,f_m$ are convex, then $f(\mathbf x)=\max_i f_i(\mathbf x)$ is convex.

A function $\max_i(\mathbf c_i'\mathbf x+d_i)$ is piecewise linear convex, e.g. $|x|=\max\{x,-x\}$. Minimizing it over $\mathbf A\mathbf x\ge\mathbf b$ is an LP: add a variable $z$ with
$$\min\ z\quad\text{s.t.}\quad z\ge \mathbf c_i'\mathbf x+d_i\ \ \forall i,\ \ \mathbf A\mathbf x\ge\mathbf b .$$
(source: BT p. 17.) Also $f(\mathbf x)\le h$ with $f$ piecewise linear convex becomes the linear constraints $\mathbf f_i'\mathbf x+g_i\le h$. A piecewise linear approximation can turn a smooth function into a nonsmooth one (p. 17). Piecewise linear concave objectives are handled the same way when maximizing; a nonconvex piecewise linear cost is not an LP.

## Absolute values

For $c_i\ge0$, $\min\sum c_i|x_i|$ s.t. $\mathbf A\mathbf x\ge\mathbf b$ becomes (BT p. 18, 1.3):
$$\min\ \sum_i c_iz_i\quad\text{s.t.}\ \ \mathbf A\mathbf x\ge\mathbf b,\ \ x_i\le z_i,\ -x_i\le z_i$$
Alternative: $x_i=x_i^+-x_i^-$, cost $\sum c_i(x_i^++x_i^-)$. At an optimum one of $x_i^\pm$ is zero if $c_i>0$. Nonnegative $c_i$ is essential, otherwise the cost is nonconvex. Applications: data fitting ($\ell_1$ and $\ell_\infty$ fits), optimal control of linear systems, a rocket soft-landing problem (min fuel $\sum|a_t|$ or min peak thrust $\max_t|a_t|$) (BT pp. 18-21). The $\ell_1$ trick is the LP form of absolute-value penalties such as [[LASSO]].

## Key facts
- Piecewise linear convex costs, absolute values and minimax objectives are LPs after adding variables; the added variable is tight at the optimum.
- Models are usually written in general or canonical form and converted to standard form for the [[Simplex method]]; the conversions are in [[Linear programming]].

**Covered in**: Bertsimas-Tsitsiklis ch. 1 §1.2-1.3 (pp. 6-21); Bazaraa-Jarvis-Sherali ch. 1 §1.2 (pp. 7-18)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 1); `text_books/Linear Optimization/BJS full book.pdf` (ch. 1).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Convex function]] · [[LASSO]] · [[Network flow problem]] · [[Integer programming]] · [[LP in practice]]
