---
type: paper
area: ml
areas: [ml]
source-ref: "Zaheer et al. 2017, NIPS, arXiv:1703.06114v3, §2-4"
tags: [ml, symmetry]
authors: ["[[Manzil Zaheer]]", "[[Satwik Kottur]]", "[[Siamak Ravanbhakhsh]]", "[[Barnabas Poczos]]", "[[Ruslan Salakhutdinov]]", "[[Alexander Smola]]"]
year: 2017
venue: "NIPS 2017 (arXiv:1703.06114v3)"
file: "papers/ML/Zaheer, Kottur, Ravanbhakhsh, Poczos, Salakhutdinov, Smola - Deep Sets.pdf"
---

# Deep Sets paper (Zaheer 2017)

**Summary**: Characterizes functions of sets that ignore element order. Any permutation-invariant function on a countable universe has the form $\rho(\sum_x \phi(x))$. Replacing $\phi,\rho$ by networks gives the DeepSets architecture. A layer is permutation-equivariant exactly when its weight matrix is $\lambda I+\gamma \mathbf{1}\mathbf{1}^{\top}$.

**Authors**: Manzil Zaheer, Satwik Kottur, Siamak Ravanbhakhsh, Barnabas Poczos, Ruslan Salakhutdinov, Alexander Smola · **Year**: 2017 · **File**: `papers/ML/Zaheer, Kottur, Ravanbhakhsh, Poczos, Salakhutdinov, Smola - Deep Sets.pdf`

---

## Problem

Standard models take fixed-size vectors. Inputs that are sets (point clouds, galaxy clusters, tag sets) must give the same answer under any ordering, and may vary in size (source: Zaheer 2017, §1-2).

- Invariance (Property 1): $f(\{x_1,\dots,x_M\}) = f(\{x_{\pi(1)},\dots,x_{\pi(M)}\})$.
- Equivariance: $f([x_{\pi(1)},\dots,x_{\pi(M)}])$ equals the permuted outputs, for per-element labelling tasks.

## Method

> [!theorem] Invariant functions (Thm 2)
> For a countable universe, $f(X)$ is a valid set function iff it decomposes as
> $$f(X) = \rho\Big(\sum_{x\in X}\phi(x)\Big)$$
> for suitable $\phi$ and $\rho$. For uncountable universes the paper proves only the fixed-size case and conjectures the general one (source: Zaheer 2017, §2, App. A).

> [!theorem] Equivariant layer (Lemma 3)
> $f_\Theta(x)=\sigma(\Theta x)$ with $\Theta\in\mathbb{R}^{M\times M}$ is permutation-equivariant iff
> $$\Theta = \lambda I + \gamma\, \mathbf{1}\mathbf{1}^{\top}$$
> All diagonal entries are equal and all off-diagonal entries are tied. The layer applies a nonlinearity to a weighted sum of the input and the sum over the set.

A max-pool variant, $\sigma(\lambda x + \gamma\,\mathrm{maxpool}(x)\mathbf{1})$, works better in some tasks. Equivariant layers compose, so they stack.

> [!algorithm] DeepSets (invariant)
> 1. Map each element: $\phi(x_m)$ (a few layers).
> 2. Sum the representations.
> 3. Apply the $\rho$ network.
> Optional conditioning on side information $z$ gives $\phi(x_m\mid z)$.

**Related results** (§2): de Finetti's theorem for exchangeable models gives the same sum-over-elements form for conjugate exponential families; support distribution machines and low-order spectral methods fit the same $\rho\circ\phi$ structure.

## Results

- **Population statistics**: entropy and mutual information of Gaussians from sample sets. Support distribution machines (SDM) are better for small $N$; DeepSets scales to large $N$ and high dimension, where SDM's $N\times N$ inversion is prohibitive beyond $N>2^{14}$ (Fig. 1).
- **Sum of digits** (text and MNIST8m): trained on sets of at most 10, tested up to 100 (text) and 50 (images); DeepSets generalizes much better than LSTM and GRU (Fig. 2).
- **Point clouds** (ModelNet40): 90 +/- 0.3% with 5000 points, 82 +/- 2% with 100 points (Table 1).
- **Galaxy red-shift**: average scatter 0.023 for DeepSets against 0.025 for the redMaPPer estimate (Table 2).
- **Set expansion** (concept retrieval, image tagging, outlier detection on CelebA): best on LDA-3k and LDA-5k, but below w2v-Near on LDA-1k, which the authors blame on small data (Table 3).

## Limitations

- Uncountable-universe case unproven (conjecture).
- Sum pooling needs $\phi$ and $\rho$ expressive enough; the proof is existential, not about size or learnability. **[unverified]** for practical bounds.
- Evaluation mixes several loosely related tasks; image tagging precision is below the best baseline (Table 4).

## Connections

- Concept page: [[Deep Sets]]. A permutation-symmetry special case of [[Equivariance]].
- Message passing aggregates neighbours by sum, the same pattern: [[Graph neural network]], [[Variational graph auto-encoder (Kipf 2016)]].
- Cranmer's graph networks sum edge messages for the same reason: [[Symbolic models from deep learning (Cranmer 2020)]].
- Kernel mean embeddings and exchangeability link to [[Kernel methods]] and [[Bayesian neural networks]] (Wiki note, via de Finetti).

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Group equivariant CNNs (Cohen 2016)]]
%% refs:end %%

**Sources**: `papers/ML/Zaheer, Kottur, Ravanbhakhsh, Poczos, Salakhutdinov, Smola - Deep Sets.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Deep Sets]]
- [[Equivariance]]
- [[Graph neural network]]
- [[Symbolic models from deep learning (Cranmer 2020)]]
- [[Kernel methods]]
