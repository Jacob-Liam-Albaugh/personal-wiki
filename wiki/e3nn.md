---
type: concept
area: symmetry
areas: [symmetry, ml]
source-ref: "Geiger & Smidt 2022, §4-7"
tags: [symmetry, ml, software]
---

# e3nn

**Summary**: A PyTorch library for neural networks equivariant to E(3), the Euclidean group of rotations, translations and inversion. Features are typed by irreducible representations and combined by tensor products.

---

## Ingredients

- Irreps of SO(3) are indexed by $l=0,1,2,\dots$ with dimension $2l+1$; parity $p=\pm1$ extends them to O(3) (source: Geiger & Smidt 2022, p. 5-6).
- Spherical harmonics $Y^l$ transform by the irrep $D^l$ (Def. 6.1).
- Tensor product paths obey

$$|l_1-l_2|\le l_3\le l_1+l_2,\qquad p_1p_2=p_3$$

(source: eq. 16), with Clebsch-Gordan coefficients as the change of basis (eq. 18).
- Learned weights are scalars, so equivariance is preserved through composition.

Wiki note: an ordinary network is the special case with only $l=0$ features; higher $l$ carry directional information that invariant models drop.

Details: [[e3nn Euclidean networks (Geiger 2022)]]. General principle: [[Equivariance]]; discrete-group counterpart: [[Group equivariant CNN]].

> [!algorithm] Tetris classifier (book, up/symmetries/02_e3nn.ipynb)
> 1. Each piece is four points in $\mathbb R^3$; edges connect points within radius 1.1 (`e3nn.radius_graph`); graphs built with `jraph`. Eight classes, including a chiral pair, square, line, corner, L, T, zigzag.
> 2. Edge features: spherical harmonics $Y_\ell^m$ of the relative position, $\ell\le3$, tensor-multiplied with sender features. The continuous filter is
> $$W(\vec r)=R(r)\,Y_\ell^m(\hat r)$$
> with learned radial function $R$.
> 3. Features are typed by irreps (`1e`, `2o`, ...: degree $\ell$ and parity even/odd); `e3nn.flax.Linear` mixes only irreps of equal type.
> 4. Three hidden layers `32x0e + 32x0o + 8x1e + 8x1o + 8x2e + 8x2o`, output `0o + 7x0e`, scatter-sum over nodes, softmax cross-entropy, [[Adam]] at 0.01 for up to 100 steps.
> 5. Trained on one orientation of each piece. A test piece rotated 90 degrees about $z$ and translated is classified correctly.

Wiki notes:
- The text calls the network "invariant to rotations, reflections and translations", yet the classes include a mirror-image pair. The readout multiplies an odd scalar (`0o`) by an even scalar, so the logits flip sign under reflection and separate the chiral pair; a reflection-invariant network could not.
- Only one transformed piece is tested, and `test_transform` hard-codes the label 5 (unused in the prediction). The "reflection across the $y$ axis" example flips $y\to-y$, a reflection across the $xz$ plane.
- Symmetry background (groups, $E(n)=T(n)\rtimes O(n)$) is on [[Equivariance]].

**Covered in**: ASML book up/symmetries (ME 697 2.6)
**Sources**: Geiger & Smidt 2022, `courses/ME 697/advanced-scientific-machine-learning/book/up/symmetries/intro.md`, `01_symmetries.md`, `02_e3nn.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[e3nn Euclidean networks (Geiger 2022)]]
- [[Equivariance]]
- [[Group equivariant CNN]]
- [[Tensor basis NN turbulence (Ling 2016)]]
