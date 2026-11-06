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

**Sources**: `advanced-scientific-machine-learning/book/ml-software/optimization/08_initialization.ipynb`, `01_optimization_problems.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 1.4 - Optimization]] · [[Gradient descent]] · [[Adam]]
