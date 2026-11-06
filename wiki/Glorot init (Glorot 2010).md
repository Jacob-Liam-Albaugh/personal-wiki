---
type: paper
area: ml
areas: [ml]
source-ref: "Glorot, Bengio 2010, AISTATS, eq. 12 and 16"
tags: [optimization, ml]
authors: ["[[Xavier Glorot]]", "[[Yoshua Bengio]]"]
year: 2010
venue: "AISTATS 2010 (JMLR W&CP 9)"
file: "ML/Glorot, Bengio - Understanding the Difficulty of Training DFFNN.pdf"
---

# Glorot init (Glorot 2010)

**Summary**: Studies why plain SGD on deep feedforward nets from random initialization trains badly. Finds that sigmoid saturates the top hidden layer, that softsign saturates more gently, and that keeping layer-to-layer variances of activations and back-propagated gradients equal gives a "normalized initialization" with variance $2/(n_j+n_{j+1})$. This is the rule now called Xavier or Glorot initialization.

**Authors**: Xavier Glorot, Yoshua Bengio · **Year**: 2010 · **File**: `ML/Glorot, Bengio - Understanding the Difficulty of Training DFFNN.pdf`

---

## Problem

Before 2006 deep nets were hard to train; since then unsupervised pretraining and similar schemes worked. The paper asks what is wrong with "good old" deep nets trained from random initialization, by monitoring activations and gradients across layers and training time (pp. 1-2).

## Method

Setup (§2.3, p. 3): 1 to 5 hidden layers of 1000 units, softmax output, negative log-likelihood, minibatch 10, plain SGD $\theta\leftarrow\theta-\epsilon g$, biases 0. Activations compared: sigmoid, tanh, softsign $x/(1+|x|)$. Data: Shapeset-3x2 (synthetic, online), MNIST, CIFAR-10, Small-ImageNet.

**Baseline ("standard") initialization** (eq. 1, p. 3), called a commonly used heuristic:
$$W_{ij}\sim U\!\left[-\tfrac1{\sqrt n},\tfrac1{\sqrt n}\right]$$
with $n$ the size of the previous layer. Its variance satisfies $n\,\mathrm{Var}[W]=1/3$ (eq. 15, p. 5).

**Variance analysis** (§4.2.1, pp. 4-5). Assume a linear regime at initialization, $f'(s)\approx1$, independent weights, equal input variances. With $n_i$ the width of layer $i$ and $d$ layers:
$$\mathrm{Var}[z^i]=\mathrm{Var}[x]\prod_{i'=0}^{i-1}n_{i'}\mathrm{Var}[W^{i'}]$$
$$\mathrm{Var}\Big[\tfrac{\partial\,\mathrm{Cost}}{\partial s^i}\Big]=\mathrm{Var}\Big[\tfrac{\partial\,\mathrm{Cost}}{\partial s^d}\Big]\prod_{i'=i}^{d-1}n_{i'+1}\mathrm{Var}[W^{i'}]$$
(eq. 5 and 6). Keeping activation variance constant across layers requires, forward and backward respectively,
$$n_i\,\mathrm{Var}[W^i]=1\qquad n_{i+1}\mathrm{Var}[W^i]=1$$
(eq. 10-11). As a compromise:

> [!definition] Normalized (Glorot, Xavier) initialization
> $$\mathrm{Var}[W^i]=\frac{2}{n_i+n_{i+1}}$$
> realized as the uniform distribution
> $$W\sim U\!\left[-\frac{\sqrt6}{\sqrt{n_j+n_{j+1}}},\ +\frac{\sqrt6}{\sqrt{n_j+n_{j+1}}}\right]$$
>
> (source: `Glorot, Bengio ... DFFNN.pdf`, eq. 12 and 16, pp. 5-6)

Check: a uniform on $[-a,a]$ has variance $a^2/3$, so $a=\sqrt{6/(n_j+n_{j+1})}$ gives $2/(n_j+n_{j+1})$. This matches the formula on [[Weight initialization]].

Both constraints hold at once when all layers have equal width. The paper does not use the name "Xavier"; it calls the rule "normalized initialization". The paper gives the uniform form only; a Gaussian version with the same variance is a common use but is not stated here **[unverified in this source]**.

The paper also notes the weight-gradient variance is equal across layers even when the back-propagated gradient shrinks (eq. 14, p. 5), and tracks singular values of the layer Jacobian $J_i=\partial z^{i+1}/\partial z^i$ (eq. 17): average about 0.8 under normalized init, about 0.5 under standard (p. 6).

## Results

- **Sigmoid** (§3.1, Fig. 2, p. 3): the top hidden layer is pushed to 0 and saturates quickly because the softmax output first relies on its biases. Depth 5 never escaped within training; depth 4 escaped around epoch 100, slowly. Sigmoid is recommended against (conclusions, p. 8).
- **Tanh** (§3.2, Fig. 3): with the standard init, layers saturate one after another from layer 1 up. The authors say why "remains to be understood".
- **Softsign** (§3.3): layers saturate less and together; activation modes sit near the knees where there is non-linearity and gradients still flow (Fig. 4).
- **Cost** (§4.1, Fig. 5): cross-entropy with softmax has fewer plateaus than the quadratic cost.
- **Test error, 5 hidden layers** (Table 1, p. 7), N = normalized init:

| Activation | Shapeset | MNIST | CIFAR-10 | ImageNet |
|---|---|---|---|---|
| Softsign | 16.27 | 1.64 | 55.78 | 69.14 |
| Softsign N | 16.06 | 1.72 | 53.8 | 68.13 |
| Tanh | 27.15 | 1.76 | 55.9 | 70.58 |
| Tanh N | 15.60 | 1.64 | 52.92 | 68.57 |
| Sigmoid | 82.61 | 2.21 | 57.28 | 70.66 |

  On Shapeset an RBF SVM got 59.47% test error versus 50.47% for depth-5 tanh with normalized init (p. 6).
- Hessian-diagonal or gradient-variance per-parameter rates help with standard init but do less than normalized init; combining both helps more (p. 7).

## Limitations

Authors: many observations remain unexplained, such as the sequential tanh saturation (p. 8). The derivation assumes a linear regime at initialization, and the authors say it cannot be used during learning because weights stop being independent of activations (§4.3, p. 6).

Wiki note: the analysis covers symmetric activations with $f'(0)=1$ (tanh, softsign). ReLU is not treated, and He initialization is not in the `ML/` folder, so this wiki has no source for it. See [[Weight initialization]].

## Connections

- Sutskever et al. 2013 cite this paper as evidence that depth up to 8 trains from good inits, and use sparse init instead ([[Init and momentum (Sutskever 2013)]]).
- [[ResNet paper (He 2016)]] discusses initialization and normalization as the answer to vanishing gradients in deep plain nets.
- The "standard" init here is the rule the ME 697 book labels He ([[Weight initialization]]).

%% refs:start %%
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[LNNs (Cranmer 2020)]], [[ResNet paper (He 2016)]], [[Respecting causality (Wang 2022)]], [[SINDy autoencoders (Champion 2019)]], [[SIREN paper (Sitzmann 2020)]], [[Variational graph auto-encoder (Kipf 2016)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `ML/Glorot, Bengio - Understanding the Difficulty of Training DFFNN.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Weight initialization]]
- [[Init and momentum (Sutskever 2013)]]
- [[ResNet paper (He 2016)]]
- [[SGD]]
- [[Gradient descent]]
- [[Adam]]
