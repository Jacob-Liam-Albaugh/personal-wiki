---
type: paper
area: ml
areas: [ml]
source-ref: "Sutskever, Martens, Dahl, Hinton 2013, ICML, eq. 1-5"
tags: [optimization, ml]
authors: ["[[Ilya Sutskever]]", "[[James Martens]]", "[[George Dahl]]", "[[Geoffrey Hinton]]"]
year: 2013
venue: "ICML 2013 (PMLR 28)"
file: "papers/ML/Hinton, Sutskever, Martens, Dahl - On the Importance of Initialization and Momentum in DL.pdf"
---

# Init and momentum (Sutskever 2013)

**Summary**: Shows that plain minibatch SGD with classical or Nesterov momentum, a well-chosen random initialization and a slowly increasing momentum schedule can train deep autoencoders and RNNs with long-range dependencies to errors close to or better than Hessian-free optimization. Also analyzes how Nesterov's method differs from classical momentum on quadratics.

**Authors**: Ilya Sutskever, James Martens, George Dahl, Geoffrey Hinton · **Year**: 2013 · **File**: `papers/ML/Hinton, Sutskever, Martens, Dahl - On the Importance of Initialization and Momentum in DL.pdf` (the file name lists Hinton first; the paper's first author is Sutskever)

---

## Problem

Deep and recurrent nets were thought nearly impossible to train with first-order methods from random starts, so people used greedy layerwise pretraining or Hessian-free (HF) truncated Newton (p. 1). The paper asks how far SGD with momentum gets when initialization and the momentum schedule are done carefully.

## Method

> [!algorithm] Classical momentum (CM)
> $$v_{t+1}=\mu v_t-\epsilon\nabla f(\theta_t)$$
> $$\theta_{t+1}=\theta_t+v_{t+1}$$
> Learning rate $\epsilon>0$, momentum coefficient $\mu\in[0,1]$.
>
> (source: `Hinton, Sutskever, ... Init and Momentum.pdf`, eq. 1-2, p. 2)

> [!algorithm] Nesterov accelerated gradient (NAG)
> $$v_{t+1}=\mu v_t-\epsilon\nabla f(\theta_t+\mu v_t)$$
> $$\theta_{t+1}=\theta_t+v_{t+1}$$
> The only change is that the gradient is taken at the look-ahead point $\theta_t+\mu v_t$. The paper rewrites the original NAG into this form in its appendix (eq. 3-4, p. 3).

Facts from §2 (pp. 2-4):
- Polyak (1964): CM needs a factor $\sqrt R$ fewer iterations than steepest descent, $R$ the condition number at the minimum, with $\mu=(\sqrt R-1)/(\sqrt R+1)$.
- NAG gets $O(1/T^2)$ on smooth convex functions with exact gradients, versus $O(1/T)$ for gradient descent.
- Stochastic setting: asymptotic local advantages are lost, but momentum helps in the early "transient phase". SGD rate $O(L/T+\sigma/\sqrt T)$ versus an accelerated method $O(L/T^2+\sigma/\sqrt T)$.

> [!theorem] Theorem 2.1 (CM versus NAG on a quadratic)
> For $q(x)=\tfrac12x^\top Ax+b^\top x$, both methods act independently on each eigendirection of $A$. NAG along an eigenvalue $\lambda$ equals CM with momentum
> $$\mu_{\rm eff}=\mu\,(1-\lambda\epsilon).$$
> So they coincide when $\epsilon\lambda\ll1$, and NAG uses smaller effective momentum on high-curvature directions, which damps oscillation and tolerates larger $\mu$.
>
> (source: ibid., Thm 2.1, p. 4)

Momentum schedule for the autoencoder experiments (eq. 5, p. 4):
$$\mu_t=\min\!\big(1-2^{-1-\log_2(\lfloor t/250\rfloor+1)},\ \mu_{\max}\big)$$
with $\mu_{\max}\in\{0.999,0.995,0.99,0.9,0\}$, motivated by Nesterov's $\mu_t=1-3/(t+5)$. In the last 1000 updates, $\mu$ is dropped to 0.9 with the learning rate unchanged.

**Initialization.**
- Feed-forward nets use Martens' sparse initialization (SI): each unit gets 15 randomly chosen inputs from the previous layer with unit Gaussian weights, biases zero (§3.1, p. 6). Rationale: total input to a unit does not grow with layer width, so units saturate less. Tanh nets simulate sigmoids with bias 0.5 and weights scaled by 0.25.
- RNNs use an echo-state-style init: hidden-to-hidden weights with 15 non-zeros per row and spectral radius 1.1, input-to-hidden $0.001\cdot\mathcal N(0,1)$ (0.1 for memory tasks), hidden-to-output $0.1\cdot\mathcal N(0,1)$ (Table 4, §4.1, p. 6). Spectral radius slightly above 1 keeps dynamics rich without severely exploding gradients. Inputs and outputs are centered.

The paper does not use the Glorot rule ([[Glorot init (Glorot 2010)]]); it cites it as evidence that depth up to 8 can train from good inits (p. 1).

## Results

- **Deep autoencoders** (§3, Table 1, p. 5): Curves, MNIST and Faces autoencoders (7 to 11 layers, sigmoid), 750,000 updates of minibatch 200, no regularization, training squared error reported. Plain SGD ($\mu=0$): Curves 0.48, MNIST 2.1, Faces 36.4. NAG with $\mu_{\max}=0.999$: Curves 0.074, MNIST 0.80, Faces 7.7. NAG at 0.995 gives MNIST 0.75. HF (Martens 2010): 0.11, 1.40, 12.0. Larger $\mu_{\max}$ is better and NAG usually beats CM, especially at 0.995 and 0.999.
- **Low-momentum fine-tuning** (Table 2): for NAG, dropping $\mu$ at the end improves Curves from 0.096 to 0.074, MNIST from 1.20 to 0.73, Faces from 10.83 to 7.7.
- **Init scale** (Table 3): for Curves, SI scale multipliers of 0.25 and 0.5 give error 16, scale 1 gives 0.074, 2 gives 0.083, 4 gives 0.35.
- **RNNs** (§4.2, Table 5, p. 8): 100 tanh units on the Hochreiter-Schmidhuber problems (add, multiply, memorization), 50,000 updates. NAG with large $\mu_0$ and a small learning rate solves them (e.g. add T=80 at $\mu_0=0.9$: 0.00025 zero-one loss for NAG; mem-20 at 0.98: 0.00005 for NAG). The authors say Martens and Sutskever 2011 (HF) are moderately better and more robust.
- **HF as momentum** (§5): one CG step is a gradient step plus the previous update reapplied, so HF with one CG iteration is NAG with a curvature-based learning rate. A more momentum-like HF variant gave improved results (Table 1, HF$^\dagger$).

## Limitations

Authors: only training error is reported, because test error depends on regularization (p. 4); the RNN results are moderately worse than HF (p. 7); good input-to-hidden init scale is task dependent (p. 6).

Wiki note: the analysis is for a quadratic with exact gradients. The stochastic case rests on experiments and the transient-phase argument.

## Connections

- Corrects nothing in [[Momentum]], which matches eq. 1-4 here; see the cites added there.
- [[Adam paper (Kingma 2015)]] cites the idea of reducing momentum late in training (Thm 4.1 discussion).
- Compare init in [[Weight initialization]] and [[Glorot init (Glorot 2010)]].
- Momentum plus noise gives [[SGHMC]].

%% refs:start %%
**Cites in this wiki**: [[Glorot init (Glorot 2010)]]
**Cited by in this wiki**: [[Adam paper (Kingma 2015)]]
%% refs:end %%

**Sources**: `papers/ML/Hinton, Sutskever, Martens, Dahl - On the Importance of Initialization and Momentum in DL.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Momentum]]
- [[Weight initialization]]
- [[Glorot init (Glorot 2010)]]
- [[Adam paper (Kingma 2015)]]
- [[Adam]]
- [[SGD]]
- [[Gradient descent]]
- [[SGHMC]]
