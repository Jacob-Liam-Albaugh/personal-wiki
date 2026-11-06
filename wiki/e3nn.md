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

**Sources**: Geiger & Smidt 2022.
**Last updated**: 2026-11-06

---

## Related pages
- [[e3nn Euclidean networks (Geiger 2022)]]
- [[Equivariance]]
- [[Group equivariant CNN]]
- [[Tensor basis NN turbulence (Ling 2016)]]
