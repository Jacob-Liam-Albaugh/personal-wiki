---
type: paper
area: math
areas: [math, optimization]
source-ref: "Polyhedral representation theorem note, pp. 1-3 (Minkowski-Weyl by cone lemma and Fourier-Motzkin)"
tags: [optimization]
authors: []
year: unknown
venue: "Short self-contained note (3 pp.), author and date not stated in the PDF"
file: "papers/Math/Convexity/Polyhedral_Representation_Theorem.pdf"
---

# Polyhedral representation theorem (n.d.)

**Summary**: A three-page explanation of the Minkowski-Weyl theorem. A nonempty set is a [[Polyhedron]] (finite intersection of halfspaces) iff it is the convex hull of finitely many points plus the cone of finitely many directions. The proof lifts to a cone, uses a lemma that cutting a finitely generated cone by one halfspace keeps it finitely generated, and goes back with Fourier-Motzkin elimination. It is an independent write-up of Basu Thms 2.77 and 2.81.

**Authors**: not stated · **File**: `papers/Math/Convexity/Polyhedral_Representation_Theorem.pdf` · Further reading named in the note: Basu §2.5.1, Thms 2.76, 2.80, 2.81 ([[Convex set]])

---

## Statement (p. 1)

> [!theorem] Minkowski-Weyl
> A nonempty $P\subseteq\mathbb R^n$ is a polyhedron iff there are finite sets $V$ (points) and $D$ (directions) with
> $$P=\mathrm{conv}(V)+\mathrm{cone}(D).$$
>
> (source: p. 1)

Reading it: the weights on $V$ sum to one, the weights on $D$ are only nonnegative. Every direction $d$ satisfies $Ad\le0$ for $P=\{Ax\le b\}$. The points of $V$ need not be extreme points. A bounded $P$ has $D=\emptyset$, so $P=\mathrm{conv}(V)$ (p. 3).

## Step 1: cone lemma (p. 1)

> [!theorem] Lemma
> If $C=\mathrm{cone}\{u_1,\dots,u_m\}$ and $H=\{x:a^\top x\ge0\}$, then $C\cap H$ is finitely generated.
>
> (source: p. 1)

Proof idea. Put $s_i=a^\top u_i$ and split indices into $I_+$ ($s_i>0$), $I_0$ ($s_i=0$) and $I_-$ ($s_i<0$). Generators of $C\cap H$:
- $u_i$ for $i\in I_+\cup I_0$,
- $w_{ij}=u_i/s_i+u_j/t_j$ for $i\in I_+$, $j\in I_-$, where $t_j=-s_j$.

Each $w_{ij}$ has $a^\top w_{ij}=0$, so lies on the boundary of $H$. Any point of $C\cap H$ is rebalanced so negative-side mass is paired with positive-side mass (p. 1).

## Step 2: every polyhedral cone is finitely generated (p. 2)

$\mathbb R^N=\mathrm{cone}\{\pm e_i\}$. Intersect with the halfspaces $\{a_k^\top x\ge0\}$ one at a time, applying the lemma once per halfspace. So $\{x:Ax\le0\}$ is finitely generated.

## Step 3: polyhedron to points and directions (p. 2)

Lift $P=\{Ax\le b\}$ to the cone
$$K=\{(z,t):\ Az\le tb,\ t\ge0\}.$$
By step 2 it is finitely generated. Rescale generators with $t>0$ to $(v_i,1)$; those with $t=0$ are $(d_j,0)$. Slice at $t=1$:
$$P\subseteq\mathrm{conv}\{v_i\}+\mathrm{cone}\{d_j\}.$$
Reverse inclusion: $Av_i\le b$ and $Ad_j\le0$, and these are preserved under convex combinations plus conic combinations.

## Step 4: points and directions to polyhedron (p. 3)

$P$ is the projection onto $x$ of the polyhedron in $(x,\lambda,\mu)$:
$$x=V\lambda+D\mu,\quad \mathbf 1^\top\lambda=1,\quad\lambda,\mu\ge0.$$
Projections of polyhedra are polyhedra by Fourier-Motzkin elimination: to remove variable $y$, write the constraints as lower bounds $y\ge L_i(z)$, upper bounds $y\le U_j(z)$ and constraints without $y$. The projection keeps the latter and adds $L_i(z)\le U_j(z)$ for every pair. Repeat per variable. The note states the proof works even when $P$ contains a line (p. 3).

## Connections

- Wiki note: each Fourier-Motzkin step can square the number of constraints, so it is a proof device, not a practical algorithm.
- Wiki note: the V-description is what the [[Simplex method]] walks (vertices and rays); the H-description is the LP constraint matrix in [[Linear programming]].
- General theory of the sets: [[Convex set]].

**Sources**: `papers/Math/Convexity/Polyhedral_Representation_Theorem.pdf` (all 3 pages read). Author and date are not in the file.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Convex set]] · [[Linear programming]] · [[LP duality]] · [[Simplex method]]
