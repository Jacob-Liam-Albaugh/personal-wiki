---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 8 (printed pp. 393-452)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "Linear Optimization/BJS full book.pdf"
---

# BJS ch8 - Complexity of the simplex algorithm and polynomial-time algorithms

**Summary**: Worst-case versus average-case complexity of the simplex method (an exponential-time example), polynomial complexity classes, Khachian's ellipsoid algorithm (outlined), Karmarkar's projective algorithm in detail, and the affine scaling and primal-dual path-following variants including a predictor-corrector scheme. See [[Ellipsoid method]], [[Interior point method]], [[BT ch8 - Complexity of LP and the ellipsoid method]], [[BT ch9 - Interior point methods]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `Linear Optimization/BJS full book.pdf` (printed pp. 393-452). Cites use printed pages; pdf = printed + 16.

## Overview (p. 393)
The simplex algorithm is "bad" by worst-case analysis because effort grows exponentially on certain problem classes, while average-case results help explain its practical efficiency. Polynomial-time algorithms exist. Khachian's has failed to be of practical value, so it is relegated to exercises (8.12-8.17), while Karmarkar's concept "is far more promising" and is treated in detail (p. 393, text).

## Polynomial complexity issues (§8.1-8.2, p. 393-401)
Section 8.1 (p. 393-397) discusses exponential versus polynomial time in the input size $L$ (Equation 8.1). An LP optimization can be solved through the decision problem by bisection on the interval of uncertainty of the optimal value. After $3L+2$ calls to a polynomial decision algorithm the optimal value is localized to an interval short enough that a polynomial rounding scheme recovers an exact solution, so the whole process is polynomial (p. 397, text, the interval endpoints involve powers of 2 that were garbled).

**Computational complexity of the simplex algorithm** (§8.2, p. 397-401). A problem with $n$ constraints and $2n$ nonnegative variables forces the simplex method, under the stated entering rule, through an exponentially long sequence of pivots (p. 400-401, the construction is in Figure 8.1, not read). At the end of $2^{n-1}$ pivots the basic variables are $(s_1,\dots,s_{n-2},y_{n-1},y_n)$, and entering $s_{n-1}$ gives the optimum, but ties $z_j-c_j=-1$ for $y_1$ and $s_{n-1}$ lead through the reverse sequence (p. 401, image seen). With $0.25n^2$ operations per pivot at one nanosecond each, the effort is 22.3 years for $n=50$ and over 328 centuries for $n=60$ (p. 401, image seen). The book notes the problem is solved in one iteration after scaling columns by $y_i=2^{-i}y_i'$ or under the largest-improvement rule, but Jeroslow (1973) exhibited problem classes with exponential effort for the maximum-improvement rule too, even for $r$-pivot lookahead with $r\ge1$ fixed. The root cause is the "myopic or local viewpoint" and the restriction to an edge path (p. 401, image seen).

## Khachian's ellipsoid algorithm (§8.3, p. 401-402)
Proposed in 1979 by L. G. Khachian, answering whether a polynomial-time LP algorithm exists. It finds a solution of the open system $S=\{\mathbf x:\mathbf G\mathbf x<\mathbf g\}$ with $\mathbf G$ of size $r\times q$, $r,q\ge2$, integer data, or concludes that $S$ is empty (p. 401, image seen). Mode of operation: start with a ball centered at the origin containing enough of $S$; if the center is in $S$ stop; otherwise build a monotonically volume-shrinking sequence of ellipsoids all containing the part of $S$ caught by the initial ball. If $S$ is nonempty some center lies in $S$ within a number of iterations polynomial in the problem size; if the bound is exceeded the algorithm asserts $S$ is empty (p. 401-402). Solving $\min\{\mathbf c\mathbf x:\mathbf A\mathbf x\ge\mathbf b,\mathbf x\ge\mathbf0\}$ costs $O[(m+n)^6L]$ (p. 402, image seen). Computational experience was disappointing: problems with about 100 variables can need enormous effort, and the practical performance follows the worst-case bound, so today it serves as a theoretical tool for row generation in combinatorial optimization (p. 402, image seen). See [[BT ch8 - Complexity of LP and the ellipsoid method]] for BT's treatment.

## Karmarkar's projective algorithm (§8.4, p. 402-417)
Proposed by N. Karmarkar at AT&T Bell Laboratories in 1984 (p. 402, image seen). The problem form (8.4) with $\mathbf A$ of rank $m$, $m,n\ge2$, integer data, $\mathbf 1$ a row of ones:
$$\min\ \mathbf c\mathbf x$$
$$\mathbf A\mathbf x=\mathbf0,\quad\mathbf 1\mathbf x=1,\quad\mathbf x\ge\mathbf0$$
Assumption (A1): $\mathbf x_0=(1/n,\dots,1/n)'$ is feasible (p. 402, image seen). Assumption (A2) and the algorithm itself (projective transformations, a potential function, steps $\mathbf x_k$ and a rounding step) were read only as headings and numeric examples (Examples 8.1-8.3, p. 410-417, where a table lists iterates such as $\mathbf x_6=(0.606509,0.060158,\dots)$, not verified). Convergence analysis (§8.5, p. 417-428, Examples 8.4-8.5) not read.

## Affine scaling, primal-dual path following (§8.6, p. 428-440)
Text read (p. 433-434, images not seen). The primal-dual path-following method applies one Newton step to the perturbed KKT system, neglecting a second-order product term $d_{v_j}d_{x_j}$ in system (8.41c) so that the direction is the unique solution of a linear system. A unit step gives the new iterate (8.42). With the step parameter chosen as $\beta=1-\delta/\sqrt n$ with $\delta=0.35$ (eq. 8.43, text, the formula garbled, **[unverified]**), the new iterate stays near the central path and the optimality gap shrinks geometrically as $\beta^k$ (eq. 8.44), so after $k>4L\ln2/[-\ln\beta]$ iterations the gap is below $2^{-2L}$ and an optimal rounding is possible. The barrier parameter is reduced by $\mu_{k+1}=\mu_k/n$ for $n\le5000$ and $\mu_k/\sqrt n$ otherwise (eq. 8.45, text, **[unverified]**). Applying affine scaling to the barrier problem and letting $\mu\to0$ recovers the standard affine scaling method, convergent for all step lengths $0<\alpha<1$ regardless of degeneracy (p. 434). A **predictor-corrector** variant (p. 434) first takes a predictor step in the direction of the system with $\mu_{k+1}=0$ and the second-order term neglected, then a corrector, and is described as one of the most computationally effective interior point variants. See [[BT ch9 - Interior point methods]].

## Notes
- Wiki note: BT cover the same history in [[BT ch8 - Complexity of LP and the ellipsoid method]] and [[BT ch9 - Interior point methods]]; BJS treat Karmarkar's projective algorithm in detail (§8.4-8.5).
- Wiki note: these methods are the polynomial-time alternatives to [[Simplex method]]; the Newton step above is that of [[Newton's method]] applied to perturbed KKT conditions ([[KKT conditions]]).

**Sources**: `Linear Optimization/BJS full book.pdf` (pdf 409-466, printed pp. 393-452). Pages viewed as images: pdf 417 (printed 401) and 418 (402). The rest read from the text layer, whose math is garbled. Karmarkar's algorithm steps were not read.
**Last updated**: 2026-11-06

---

## Related pages
- [[Ellipsoid method]] · [[Interior point method]] · [[Linear programming]] · [[Simplex method]] · [[KKT conditions]]
- [[BT ch8 - Complexity of LP and the ellipsoid method]] · [[BT ch9 - Interior point methods]] · [[BJS ch6 - Duality and sensitivity analysis]]
