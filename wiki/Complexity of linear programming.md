---
type: concept
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 1, 3, 8; Bazaraa, Jarvis, Sherali 2010, ch. 8"
tags: [optimization]
---

# Complexity of linear programming

**Intuition**: the [[Simplex method]] is exponential in the worst case yet typically needs about $O(m)$ iterations for $m$ equality constraints (BT p. 360). The [[Ellipsoid method]] and [[Interior point method]]s are polynomial in the bit model, but only the interior point family is also fast in practice. Worst-case efficiency can mislead (BT p. 363).

## Operation counts and polynomial time

Basic counts (BT §1.5-1.6, pp. 26-33): inner product $2n-1$ operations, matrix product $(2n-1)n^2$ (Example 1.9, p. 32). $O$, $\Omega$, $\Theta$ are defined in Def. 1.2. Gaussian elimination and matrix inversion cost $O(n^3)$ (Example 1.10, p. 33). Polynomial time $O(n^k)$ versus exponential $O(2^{cn})$; worst-case analysis is the convention.

Models of computation (BT §8.1, p. 360-363):
- Arithmetic model: every operation takes unit time.
- Bit model: each operation is decomposed into single-bit steps, which accounts for the cost of large numbers (p. 362).
- $T(n)$ is the worst-case running time over instances of size $n$ in the bit model.

> [!definition] Definition 8.3 (p. 362)
> An algorithm runs in polynomial time if there is an integer $k$ with $T(n)=O(n^k)$.

A polynomial algorithm must also keep the numbers it produces polynomially bounded in size. Gaussian elimination is the example: $O(n^3)$ arithmetic operations, and the intermediate numbers stay polynomial, so inversion is polynomial in the bit model (p. 363). Polynomiality is a stable property across reasonable computation models.

BJS (§8.1, p. 393-397) discuss exponential versus polynomial time in the input size $L$ (Equation 8.1). An LP optimization can be solved through the decision problem by bisection on the interval of uncertainty of the optimal value: after $3L+2$ calls to a polynomial decision algorithm the optimal value is localized well enough for a polynomial rounding scheme to recover an exact solution (p. 397).

## Simplex worst case

BT (§3.7, pp. 124-128): the diameter $\Delta(n,m)$ of a polyhedron with $m$ constraints in $n$ dimensions lower-bounds the iterations of any vertex-to-adjacent-vertex method.
- Hirsch conjecture: $\Delta(n,m)\le m-n$ (p. 127). False for unbounded polyhedra: $\Delta_u(n,m)\ge m-n+\lfloor n/5\rfloor$ (Klee-Walkup).
- Best known upper bound (Kalai-Kleitman): $\Delta\le\Delta_u<m^{1+\log_2n}=(2n)^{\log_2m}$.
- Diameter examples: $\Delta(2,m)=\lfloor m/2\rfloor$, $\Delta_u(2,m)=m-2$ (Fig. 3.9).
- Exponential-iteration examples have been constructed for several popular pivoting rules, but that does not exclude a better rule, an important open problem (p. 126). Average-case analysis is hard because "average" needs a probability model (p. 127-128).
- The simplex method needs $2^n-1$ iterations on a particular $n$-variable, $2n$-constraint problem (§3.7), yet empirically about $O(m)$ iterations are typical (BT p. 360).

BJS (§8.2, p. 397-401): a problem with $n$ constraints and $2n$ nonnegative variables forces the simplex method, under the stated entering rule, through an exponentially long sequence of pivots (the construction is in BJS Figure 8.1, not read). At the end of $2^{n-1}$ pivots the basic variables are $(s_1,\dots,s_{n-2},y_{n-1},y_n)$, and entering $s_{n-1}$ gives the optimum, but ties $z_j-c_j=-1$ for $y_1$ and $s_{n-1}$ lead through the reverse sequence (p. 401). With $0.25n^2$ operations per pivot at one nanosecond each, the effort is 22.3 years for $n=50$ and over 328 centuries for $n=60$. The problem is solved in one iteration after scaling columns by $y_i=2^{-i}y_i'$ or under the largest-improvement rule, but Jeroslow (1973) exhibited problem classes with exponential effort for the maximum-improvement rule too, even for $r$-pivot lookahead with $r\ge1$ fixed. The root cause is the "myopic or local viewpoint" and the restriction to an edge path (p. 401). BJS stress that average-case results help explain the practical efficiency of the simplex method (p. 393).

## Polynomial-time algorithms

- Ellipsoid: Khachian, 1979. Polynomial but not practical; $O(n^6\log(nU))$ iterations (BT) or $O[(m+n)^6L]$ (BJS). See [[Ellipsoid method]].
- Interior point: Karmarkar's 1984 projective algorithm started the field (BJS §8.4, p. 402-417; BT notes p. 448). Affine scaling ([[Affine scaling method]]) has no polynomial bound; potential reduction ([[Interior point method]]) and path following ([[Path-following interior point methods]]) are polynomial, with $O(\sqrt n\log(1/\epsilon))$ iterations and $O(n^3)$ work each, giving the practical methods.
- BJS call Karmarkar's concept "far more promising" than Khachian's, which they relegate to exercises 8.12-8.17 (p. 393).
- Guideline (BT p. 439): the simplex method does poorly on large, massively degenerate problems, which hardly hurt interior point methods. The simplex method is not known to be polynomial but is often faster in practice.

## Key facts
- Simplex: exponential worst case for known pivoting rules, about $O(m)$ iterations typically; polynomial pivoting rule is open.
- Ellipsoid and interior point methods are polynomial in the bit model; the ellipsoid method also proves that optimization reduces to separation (Thm 8.5, see [[Ellipsoid method]]).
- Simplex and polynomial methods are complementary: crossover from interior point to a basis allows reoptimization ([[LP in practice]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 1 §1.5-1.6 (pp. 26-33), ch. 3 §3.7 (pp. 124-128), ch. 8 §8.1 (pp. 360-363); Bazaraa-Jarvis-Sherali ch. 8 §8.1-8.2, overview (pp. 393-401)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 1, 3, 8, 9); `text_books/Linear Optimization/BJS full book.pdf` (ch. 8, printed pp. 393-401, pdf 417 viewed as image).
**Last updated**: 2026-11-06

---

## Related pages
- [[Linear programming]] · [[Simplex method]] · [[Ellipsoid method]] · [[Interior point method]] · [[Affine scaling method]] · [[Path-following interior point methods]] · [[LP in practice]] · [[Basic feasible solution]]
