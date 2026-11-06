---
type: concept
area: ml
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/optimization/08_initialization"
tags: [optimization, ml]
---

# Weight initialization

> [!definition] Xavier/Glorot uniform
> $$W\sim U[-a,a],\quad a=\sqrt{\frac{6}{n_{in}+n_{out}}}$$
> Keeps activation and gradient variance roughly constant across layers for sigmoid and tanh.

**What goes wrong** (book, 08)
- All zeros: with ReLU every unit is dead and gradients are zero.
- Any constant: all units in a layer get the same gradient and stay identical. Initialization must break symmetry.
- Too large or too small: exploding or vanishing gradients. Check histograms of gradients per layer.

> [!failure] "He" initialization in the book
> The book calls $U[-a,a]$ with $a=\sqrt{1/n_{in}}$ He initialization and says it is Equinox's default. Wiki note: that bound is LeCun-style uniform (variance $1/(3n_{in})$). He et al. 2015, for ReLU, is $\mathcal N(0,2/n_{in})$ or $U[-a,a]$ with $a=\sqrt{6/n_{in}}$. **[unverified]** which one current Equinox uses.

**Wiki note**: in a [[Bayesian neural networks|BNN]] the initialization scale and the prior scale play similar roles; see [[Priors in Bayesian deep learning (Fortuin 2022)]].

## Where it appears
- [[Expert's guide to PINNs (Wang 2023)]] — random weight factorization changes the parameterization of weights to speed up PINN training.

## Glorot / Xavier initialization
- Glorot's normalized initialization: W ~ U[-sqrt(6)/sqrt(n_j+n_{j+1}), +sqrt(6)/sqrt(n_j+n_{j+1})], so Var[W] = 2/(n_j+n_{j+1}) (source: Glorot 2010, eq. 16, p. 5; compromise of eq. 10-11). The book's formula matches this.
- Wiki note: the book labels the $n^{-1/2}$ uniform init "He". That is Glorot's baseline, $U[-1/\sqrt n,1/\sqrt n]$ with $n\,\mathrm{Var}[W]=1/3$ (Glorot 2010, eqs. 1 and 15, pp. 3, 5), not He.
- He initialization (Var = 2/n for ReLU) is not in the papers/ML/ folder; ResNet paper (He 2016) mentions it only as prior work **[unverified]**. Do not cite it from these sources.
- SIREN uses its own init U(-sqrt(6/n), sqrt(6/n)) with omega0=30 (source: Sitzmann 2020, §3.2). See [[SIREN]].
- [[Glorot init (Glorot 2010)]].

**Covered in**: ASML book ml-software/optimization (ME 697 1.4)
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/ml-software/optimization/08_initialization.ipynb`, `01_optimization_problems.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[Adam]]
- Initialization scale for attention and state space models: [[Attention is all you need (Vaswani 2017)]], [[Mamba (Gu 2023)]].
