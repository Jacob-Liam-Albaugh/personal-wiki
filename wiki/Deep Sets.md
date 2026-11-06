---
type: method
area: ml
areas: [ml]
source-ref: "Zaheer et al. 2017, §2-3"
tags: [ml, symmetry]
---

# Deep Sets

**Summary**: An architecture for functions of unordered sets of variable size. Encode each element, sum, then decode.

> [!definition] Sum-decomposition
> $$f(X) = \rho\Big(\sum_{x\in X}\phi(x)\Big)$$
> This is permutation-invariant by construction, and (countable universe) every invariant function has this form (source: Zaheer 2017, Thm 2).

## Key points

- Equivariant version: use $\Theta=\lambda I+\gamma\mathbf{1}\mathbf{1}^{\top}$ in each layer (Lemma 3). This is the unique weight sharing that commutes with permutations.
- Sum can be replaced by max or mean pooling; max helped in some tasks.
- Generalizes across set sizes, unlike recurrent models (digit-sum test, Fig. 2).
- Same structure as aggregation in a [[Graph neural network]] (a node's neighbours form a set) and as sum-over-edges messages in [[Symbolic models from deep learning (Cranmer 2020)]].
- A symmetry-by-construction model, like those in [[Equivariance]]: build the group into the layers rather than learn it.

**Sources**: `ML/Zaheer, Kottur, Ravanbhakhsh, Poczos, Salakhutdinov, Smola - Deep Sets.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Deep Sets paper (Zaheer 2017)]]
- [[Graph neural network]]
- [[Equivariance]]
- [[Kernel methods]]
