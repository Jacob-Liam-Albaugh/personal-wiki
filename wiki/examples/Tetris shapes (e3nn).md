---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [synthetic]
tasks: [classification]
uses: 1
---

# Tetris shapes (e3nn)

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: classification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/symmetries/02_e3nn.ipynb`.
**Last updated**: 2026-11-18

---

## Tetris 3D shape classification (E(3)-equivariant)

`text_books/advanced-scientific-machine-learning/book/up/symmetries/02_e3nn.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: classification
- **Technique**: E(3)-equivariant message passing; Adam lr 0.01, 100 steps with early stop at accuracy 1.0
- **Data**: 8 Tetris-like shapes of 4 points in 3D (chiral_shape_1, chiral_shape_2, square, line, corner, L, T, zigzag); training set is the 8 graphs in one orientation. Also covers spherical harmonic irreps.
- **Data origin**: synthetic
- **Data file**: none
- **Forward model**: Radius graph (radius 1.1), jraph GraphNetwork with 4 e3nn-jax layers (3 x 32x0e+32x0o+8x1e+8x1o+8x2e+8x2o, output 0o+7x0e), sh_lmax 3, parity-aware logit readout separating the chiral pair.
- **Unknown dimension**: network weights
- **Data dimension**: 8 samples, 4 points each
- **Ground truth**: known labels; test = 90 degree rotation plus translation [2,-1,3] of shape 1, notebook claims correct prediction
- **What makes it hard**: must distinguish a mirror-image (chiral) pair
- **Libraries**: e3nn-jax, jraph, flax, jax==0.4.33
- **References**: adapted from e3nn-jax tetris_point.py; Batzner et al., Nat. Commun. 2022, https://www.nature.com/articles/s41467-022-29939-5
- **Notes**: test_transform helper hard-codes label 5.

## Related pages
- [[Examples catalogue]]
- [[e3nn]] · [[Adam]]
