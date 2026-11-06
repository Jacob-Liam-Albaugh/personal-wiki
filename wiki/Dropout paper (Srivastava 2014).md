---
type: paper
area: ml
areas: [ml]
source-ref: "Srivastava et al. 2014, JMLR 15:1929-1958, §4-5, §9"
tags: [ml, optimization, bayesian]
authors: ["[[Nitish Srivastava]]", "[[Geoffrey Hinton]]", "[[Alex Krizhevsky]]", "[[Ilya Sutskever]]", "[[Ruslan Salakhutdinov]]"]
year: 2014
venue: "JMLR 15 (2014) 1929-1958"
file: "papers/ML/Hinton, Srivastava, Krizhevsky, Sutskever, Salakhutdinov - Dropout.pdf"
---

# Dropout paper (Srivastava 2014)

**Summary**: Randomly removes units (with their connections) during training, so each step trains a different "thinned" network. At test time one unthinned network with weights scaled by the retention probability $p$ approximates the average over all thinned nets. This cuts overfitting and set records on SVHN, ImageNet, CIFAR-100 and MNIST at the time.

**Authors**: Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, Ruslan Salakhutdinov · **Year**: 2014 · **File**: `papers/ML/Hinton, Srivastava, Krizhevsky, Sutskever, Salakhutdinov - Dropout.pdf` (the file name lists Hinton first; the first author is Srivastava)

---

## Problem

Large networks overfit small data. The ideal regularizer for a fixed-size model is to average the predictions of all parameter settings, weighted by posterior (p. 1-2). That is too costly for big nets, and ensembles of large nets are slow at test time. Dropout is a cheap stand-in (source: Dropout, §1).

## Method

> [!definition] Dropout layer
> Let $y$ be a layer's activations and $p$ the probability of *retaining* a unit. Training samples a mask and thins the layer:
> $$r_j \sim \mathrm{Bernoulli}(p)$$
> $$\tilde y = r * y$$
> The thinned $\tilde y$ feeds the next layer. A new mask is drawn for each training case in each minibatch. (source: Dropout, §4, p. 5)

> [!algorithm] Test-time rule
> Use all units and multiply the outgoing weights by $p$:
> $$W_{\text{test}} = p\,W$$
> so the expected input to each unit at test time equals its expected input during training (source: Dropout, §1, §5).

- A net with $n$ units has $2^n$ possible thinned nets, all sharing weights; training samples from this family and the scaled net approximates their geometric-style average (§2, §4).
- Typical values: $p=0.5$ for hidden units, closer to $1$ (for example $0.8$) for real-valued inputs (App. A.4).
- Equivalent "inverted" form: scale retained activations by $1/p$ during training and leave weights alone at test time (§10).
- Max-norm constraint $\|w\|_2\le c$ on each unit's incoming weights, with $c$ about 3 to 4, keeps weights bounded when the high learning rate and momentum that dropout needs would blow them up (App. A.3).
- Motivation: sexual reproduction forces genes to work with random partners, so dropout forces units to work in many contexts and prevents co-adaptation (§2).

### Practical guide (App. A)

- Size: a good dropout layer has at least $n/p$ units if $n$ is best without dropout (A.1).
- Learning rate: 10 to 100 times the no-dropout value, momentum 0.95 to 0.99 instead of 0.9, because the gradients are noisy (A.2). See [[Momentum]] and [[Init and momentum (Sutskever 2013)]].
- Training takes 2 to 3 times longer than a standard net of the same architecture (§11).

## Results

- MNIST (permutation invariant): standard net about 1.60%; dropout 1.35%; ReLU units 1.25%; plus max-norm 1.06%; a $2\times 8192$ net (over 65 million parameters, 60,000 training images) 0.95%. DBM-pretrained dropout net 0.79% (source: Dropout, §6.1.1, Table 2).
- The gain holds across 2 to 4 layer, 1024 or 2048 unit architectures with fixed hyperparameters (Fig. 4).
- SVHN: best convnet without dropout 3.95%; dropout in fully connected layers 3.02%; in all layers 2.55% (§6.1.2, Table 3).
- CIFAR-10: 14.98% (Snoek et al.) to 14.32% (fully connected dropout) to 12.61% (all layers). CIFAR-100: 43.48% to 37.20% (§6.1.3, Table 4).
- ImageNet: a dropout convnet won ILSVRC-2012 with about 16% top-5 test error, against about 26% for methods on standard vision features (§6.1.4).
- TIMIT phone error: 23.4% to 21.8% for a 6-layer net; pretrained 4-layer net 22.7% to 19.7% (Table 7). Reuters-RCV1: 31.05% to 29.62%, a smaller gain (§6.3).
- Versus a Bayesian neural net on alternative splicing data: [[Bayesian neural networks]] still win, but dropout beats early-stopped nets, SVMs and PCA-regression (§6.4, Table 8).
- Versus other regularizers on MNIST: dropout plus max-norm gives the lowest error (§6.5, Table 9).

### Analysis (§7)

- Features: autoencoder units trained with dropout detect edges, strokes and spots; without it they look co-adapted and not individually meaningful (Fig. 7).
- Sparsity appears without any sparsity penalty: mean hidden activation falls from about 2.0 to about 0.7 (Fig. 8).
- Retention rate: test error is flat for $0.4\le p\le 0.8$ at fixed $n$; holding $pn$ fixed, $p\approx 0.6$ is best (Fig. 9).
- Data size: no gain at 100 or 500 examples, the gain rises then declines as data grows (Fig. 10).
- Weight scaling versus Monte-Carlo averaging: about $k=50$ sampled thinned nets match the weight-scaled net (Fig. 11).

### Extensions

- Dropout RBM: a mask $r\in\{0,1\}^F$ on hidden units, trained by CD-1; a mixture of exponentially many RBMs with shared weights (§8).
- Marginalizing the noise gives a deterministic regularizer (§9.1). For linear regression:
$$\min_w\ \|y-pXw\|^2+p(1-p)\|\Gamma w\|^2$$
$$\Gamma=\mathrm{diag}(X^\top X)^{1/2}$$
  This is ridge regression with a data-scaled penalty. Absorbing $p$ into $w$ makes the penalty weight $(1-p)/p$.
- Gaussian dropout (§10): multiply activations by $r'\sim N(1,\sigma^2)$. With $\sigma^2=(1-p)/p$ it matches the mean $1$ and variance $(1-p)/p$ of the scaled Bernoulli mask, and needs no test-time scaling. MNIST: 0.95 against 1.08 (Table 10).

## Limitations

- Longer training because of noisy updates (§11).
- The weight-scaling average is an approximation, not the true model average (§7.5).
- Marginalized forms are only closed-form for linear models; the approximations weaken with depth (§9.2).
- Little help on very small data sets (§7.4) and a smaller gain on text (§6.3).

## Connections

- Compared with Bayesian averaging in §6.4: dropout weights all submodels equally, a Bayesian net weights them by prior and fit. See [[Bayesian neural networks]] and [[Variational dropout]].
- Noise injection as regularization: compare [[SGLD]], where noise in the update is the sampler itself.
- Used with [[Adam]] in practice; [[Adam paper (Kingma 2015)]] lists dropout as a use case.
- Residual nets drop dropout in favor of batch normalization: [[ResNet paper (He 2016)]].
- Concept page: [[Dropout]].

%% refs:start %%
**Cited by in this wiki**: [[Attention is all you need (Vaswani 2017)]], [[Priors in Bayesian deep learning (Fortuin 2022)]], [[Variational dropout (Kingma 2015)]]
%% refs:end %%

**Sources**: `papers/ML/Hinton, Srivastava, Krizhevsky, Sutskever, Salakhutdinov - Dropout.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dropout]]
- [[Adam paper (Kingma 2015)]]
- [[Init and momentum (Sutskever 2013)]]
- [[Bayesian neural networks]]
- [[Variational dropout]]
- [[ResNet paper (He 2016)]]
- [[Momentum]]
