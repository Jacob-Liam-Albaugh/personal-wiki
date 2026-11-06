---
type: paper
area: symmetry
areas: [symmetry, ml]
source-ref: "Geiger & Smidt 2022, arXiv:2207.09453, §4-8"
tags: [symmetry, ml, software]
authors: ["[[Mario Geiger]]", "[[Tess Smidt]]"]
year: 2022
venue: "arXiv:2207.09453 (cs.LG); draft dated January 2021"
file: "Symmetries/Geiger, Smidt - e3nn Euclidean Neural Networks.pdf"
---

# e3nn Euclidean networks (Geiger 2022)

**Summary**: Describes [[e3nn]], a PyTorch library for networks that are equivariant to the Euclidean group E(3) (rotations, translations, inversion). Data are typed by irreducible representations. The central operation is a general `TensorProduct` built from Clebsch-Gordan coefficients.

**Authors**: Mario Geiger, Tess Smidt · **Year**: 2022 · **File**: `Symmetries/Geiger, Smidt - e3nn Euclidean Neural Networks.pdf`

---

## Problem

3D data (points, meshes, vector and strain fields) depend on the coordinate frame. Data augmentation over orientations costs a very large increase in training, quoted as about 500-fold (source: e3nn PDF, p. 2). Invariant models act only on scalars ($l=0$) and so cannot output a quantity that rotates with the input. Models using only $l\le1$ internal features are universal, but models with $l=2$ internal features show better learning curves (source: p. 2-3).

## Group and representation vocabulary

- A group has identity, associativity and inverses (Def. 4.1). Rotations, translations and inversion generate the Euclidean group.
- A representation maps each group element to a matrix $D(g)$ with $D(ab)=D(a)D(b)$ (Def. 4.2). An irreducible representation contains no smaller one (Def. 4.3).
- The irreps of SO(3) are indexed by $l=0,1,2,\dots$ and have dimension $2l+1$. $l=0$ is a scalar, $l=1$ a vector (source: p. 5).
- Parity is the inversion $\vec x\to-\vec x$. Irreps of O(3) factor into an SO(3) irrep and a parity $p=\pm1$. The velocity is odd. The cross product of two vectors is even (a pseudovector) (source: p. 6).
- Example: a symmetric $3\times3$ tensor has 6 degrees of freedom. It splits into one $l=0$ (the trace) and one $l=2$ (5 traceless components). In e3nn notation, `1x0e + 1x2e` (source: p. 5-6).

Equivariance of $f$ under $G$:

$$f(D_X(g)\,x)=D_Y(g)\,f(x)$$

(source: p. 6). Composition of equivariant maps is equivariant. Learned weights must be scalars, so they do not transform.

e3nn uses real-valued irreps, obtained from the standard complex basis by a fixed change of basis (source: p. 7).

## Spherical harmonics

$Y^l$ is a vector of $2l+1$ functions on the sphere that transforms by the irrep $D^l$:

$$Y^l_m(R\vec x)=\sum_n D^l(R)_{mn}\,Y^l_n(\vec x)$$

(source: Def. 6.1, p. 7).

- Once the basis is fixed, $Y^l$ is unique up to sign (Lemma 6.1).
- Extended to $\mathbb R^3$ it can be chosen as polynomials of $\vec x$ (Lemma 6.2). The sign is fixed by $Y^{l+1}\propto C_{l+1,l,1}\,Y^l Y^1$.
- Frequency grows with $l$, and they are orthogonal under the sphere inner product (source: p. 8).
- A scalar function on the sphere is $f(\vec x)=\sum_l v^l\cdot Y^l(\vec x)$. Under rotation the coefficients $v^l$ transform as irreps (source: eq. 10-14, p. 9-10). Truncating at $L$ removes high frequencies.

## Tensor product and paths

The tensor product is any bilinear equivariant map between irreps. Two vectors give $\mathbb R^9$, which splits into a scalar (dot product), a pseudovector (cross product) and a 5-component $l=2$ part (source: p. 10-11).

Selection rule for the output of irreps $(l_1,p_1)$ and $(l_2,p_2)$:

$$|l_1-l_2|\le l_3\le l_1+l_2,\qquad p_1p_2=p_3$$

(source: eq. 16). Each allowed $l_3$ is a "path". A `TensorProduct` is defined by input irreps, output irreps, and a list of weighted paths. `FullyConnectedTensorProduct` connects all allowed paths.

Clebsch-Gordan coefficients (Wigner 3j symbols) are the change of basis that decomposes the product into irreps (eq. 18). A path with weights $w_{uvw}$ is

$$\text{path}_{wk}\propto\sum w_{uvw}\,C_{ijk}\,(\text{in}_1)_{ui}\,(\text{in}_2)_{vj}$$

(source: eq. 20, normalisation constants omitted). Connection modes include `uvw` (fully connected) and `uvu` (eq. 21), the latter matching the Tensor Field Network pattern.

Lemma 7.1: `TensorProduct` can represent every bilinear equivariant operation from two sets of irreps to irreps (source: p. 13).

`ReducedTensorProduct` decomposes tensors with index symmetries into irreps. Example in the paper: a rank-4 symmetric Cartesian tensor has 21 degrees of freedom, and its decomposition is `2x0e + 2x2e + 1x4e` (source: p. 14).

## Initialisation and data efficiency

- Weights are drawn from $N(0,1)$ with a multiplicative constant (such as $1/\sqrt{n}$ for a fully connected layer) so that pre-activations have variance 1.
- "Component normalisation": for $x\in\mathbb R^d$, $\|x\|^2=d$.
- The scheme follows the maximal update parametrisation shifted by $\theta=1/2$, with learning rate proportional to the number of features (source: p. 17). See [[Weight initialization]].
- The authors cite an observation that equivariant networks change the exponent of the learning curve, not just a constant shift, and state they have no theoretical explanation (source: p. 18, Fig. 4).

## Other architectures expressed in e3nn

Tensor Field Networks, 3D Steerable CNNs, Spherical CNNs (convolution maps to linear layers in irrep space, activations need a Fourier-type transform), Clebsch-Gordan Networks, and the SE(3) transformer (source: p. 18-19).

## Wiki note

- Section 8 of the paper (equivariant modules such as linear layers, gates and norms) and the code listing on pp. 15-17 were read only in outline, not summarised.
- [[Group equivariant CNN]] is the discrete-group (p4, p4m) ancestor of this continuous-group construction. [[Equivariance]] is the general idea.

**Sources**: e3nn PDF, pp. 1-19.

**Last updated**: 2026-11-06

---

## Related pages
- [[e3nn]]
- [[Equivariance]]
- [[Group equivariant CNN]]
- [[Group equivariant GANs (Dey 2021)]]
- [[Weight initialization]]
- [[Rotation augmentation for CNNs (Quiroga 2018)]]
