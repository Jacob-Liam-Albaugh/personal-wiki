---
type: paper
area: ml
areas: [ml]
source-ref: "Kingma, Ba 2015, ICLR, Algorithm 1"
tags: [optimization, ml]
authors: ["[[Diederik P. Kingma]]", "[[Jimmy Lei Ba]]"]
year: 2015
venue: "ICLR 2015 (arXiv 1412.6980v9)"
file: "papers/ML/Kingma, Lei Ba - Adam.pdf"
---

# Adam paper (Kingma 2015)

**Summary**: Adam keeps exponential moving averages of the gradient and of the squared gradient, corrects both for their zero initialization, and divides one by the root of the other. It gives per-parameter step sizes bounded by the step-size hyperparameter, comes with an $O(\sqrt T)$ regret bound for online convex problems, and works well on logistic regression, MLPs and CNNs.

**Authors**: Diederik P. Kingma, Jimmy Lei Ba · **Year**: 2015 · **File**: `papers/ML/Kingma, Lei Ba - Adam.pdf`

---

## Problem

Stochastic objectives (minibatch sampling, [[Dropout]] noise) in high dimensions need first-order methods with little memory. The paper wants to combine AdaGrad's strength on sparse gradients with RMSProp's strength on non-stationary objectives (p. 1).

## Method

> [!algorithm] Adam (Algorithm 1)
> Require step size $\alpha$, decay rates $\beta_1,\beta_2\in[0,1)$, objective $f$, start $\theta_0$. Set $m_0=0$, $v_0=0$, $t=0$. Repeat:
> $$g_t=\nabla_\theta f_t(\theta_{t-1})$$
> $$m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$$
> $$v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$$
> $$\hat m_t=m_t/(1-\beta_1^t)$$
> $$\hat v_t=v_t/(1-\beta_2^t)$$
> $$\theta_t=\theta_{t-1}-\alpha\,\hat m_t/(\sqrt{\hat v_t}+\epsilon)$$
> All operations are element-wise; $g_t^2=g_t\odot g_t$. Defaults: $\alpha=0.001$, $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$.
>
> (source: `Kingma, Lei Ba - Adam.pdf`, Algorithm 1, p. 2)

**Where $\epsilon$ sits.** In Algorithm 1 the update is $\hat m_t/(\sqrt{\hat v_t}+\epsilon)$: $\epsilon$ is added **outside** the square root (p. 2). The efficient variant on p. 2 uses $\alpha_t=\alpha\sqrt{1-\beta_2^t}/(1-\beta_1^t)$ and $\theta_t=\theta_{t-1}-\alpha_t m_t/(\sqrt{v_t}+\hat\epsilon)$, again outside. The ME 697 book writes it inside the root; see [[Adam]].

**Moment estimates.** $m_t$ estimates the mean of the gradient, $v_t$ its uncentered second moment (p. 2).

**Step size** (§2.1, pp. 2-3). With $\epsilon=0$ the effective step is $\Delta_t=\alpha\hat m_t/\sqrt{\hat v_t}$.
- Upper bounds: $|\Delta_t|\le\alpha(1-\beta_1)/\sqrt{1-\beta_2}$ when $(1-\beta_1)>\sqrt{1-\beta_2}$ (most severe sparsity: gradient zero except now), and $|\Delta_t|\le\alpha$ otherwise.
- In common cases $|\hat m_t/\sqrt{\hat v_t}|\approx1$, so steps are roughly bounded by $\alpha$, a trust region around the current point.
- The ratio $\hat m_t/\sqrt{\hat v_t}$ is called a signal-to-noise ratio; it shrinks near an optimum, an automatic annealing.
- Rescaling gradients by $c$ cancels: $(c\hat m_t)/\sqrt{c^2\hat v_t}=\hat m_t/\sqrt{\hat v_t}$ (invariance to diagonal rescaling).

**Bias correction** (§3, p. 3). Unrolling gives
$$v_t=(1-\beta_2)\sum_{i=1}^t\beta_2^{t-i}g_i^2$$
so for stationary second moment
$$\mathbb E[v_t]=\mathbb E[g_t^2]\,(1-\beta_2^t)$$
and dividing by $1-\beta_2^t$ removes the bias from starting at zero. The first moment is analogous. Needed most when $\beta_2$ is near 1 (sparse gradients).

**Convergence** (§4, p. 4). Regret $R(T)=\sum_{t=1}^T[f_t(\theta_t)-f_t(\theta^*)]$.

> [!theorem] Theorem 4.1 (regret bound)
> Bounded gradients $\|\nabla f_t\|_2\le G$, $\|\nabla f_t\|_\infty\le G_\infty$, bounded iterate distances $D,D_\infty$, and $\beta_1^2/\sqrt{\beta_2}<1$. With $\alpha_t=\alpha/\sqrt t$ and $\beta_{1,t}=\beta_1\lambda^{t-1}$, $\lambda\in(0,1)$, Adam satisfies a bound with leading terms
> $$\sum_{i}\sqrt{T\hat v_{T,i}}\quad\text{and}\quad\sum_i\|g_{1:T,i}\|_2.$$
>
> (source: ibid., Thm 4.1, p. 4; the full three-term bound is on p. 4 and the proof in the appendix)

Corollary 4.2: $R(T)/T=O(1/\sqrt T)$, so average regret goes to 0. Decaying $\beta_{1,t}$ matches Sutskever et al. 2013, who suggest reducing momentum late in training ([[Init and momentum (Sutskever 2013)]]).

**Relations** (§5, pp. 4-5).
- Adam's $\hat v_t$ approximates the diagonal of the Fisher information (citing Pascanu and Bengio); the preconditioner is the inverse square root, so more conservative than natural gradient.
- RMSProp with momentum applies momentum to the rescaled gradient and has no bias correction; without correction and with $\beta_2$ near 1, steps are very large and often diverge (§6.4).
- AdaGrad is recovered with $\beta_1=0$, $\beta_2\to1$ and $\alpha_t=\alpha t^{-1/2}$ (derivation p. 5); this equivalence needs the bias correction.

**AdaMax** (§7.1, Algorithm 2, pp. 8-9): the $L_p$ generalization with $p\to\infty$.
$$u_t=\max(\beta_2u_{t-1},|g_t|)$$
$$\theta_t=\theta_{t-1}-\frac{\alpha}{1-\beta_1^t}\frac{m_t}{u_t}$$
Defaults $\alpha=0.002$, $\beta_1=0.9$, $\beta_2=0.999$. A temporal-averaging variant is in §7.2 [not read in detail].

## Results

- **Logistic regression** (§6.1): MNIST, minibatch 128, $\alpha_t=\alpha/\sqrt t$. Adam is similar to SGD with Nesterov momentum, both faster than AdaGrad. On IMDB bag-of-words (10,000 features, 50% dropout on inputs) Adam converges as fast as AdaGrad, ahead of SGD with Nesterov (Fig. 1).
- **MLP** (§6.2): two hidden layers of 1000 ReLU units, MNIST. Against the quasi-Newton SFO, Adam progresses faster per iteration and per second; SFO is 5-10x slower per iteration and fails with dropout noise. With dropout Adam beats AdaGrad, RMSProp, SGD-Nesterov, AdaDelta (Fig. 2).
- **CNN** (§6.3): CIFAR-10, three 5x5 conv + 3x3 max-pool stages, then 1000 ReLU units. AdaGrad is much slower than Adam and SGD in the long run. The authors note $\hat v_t$ shrinks to near zero after a few epochs and is dominated by $\epsilon$, so the first-moment variance reduction matters more here (Fig. 3).
- **Bias correction** (§6.4, Fig. 4): on a VAE (one hidden layer of 500 softplus units, 50-d latent) without correction and with $\beta_2$ near 1, training is unstable early. Best results use small $1-\beta_2$ with correction.

## Limitations

As stated: the convergence proof is for convex online learning and does not cover the non-convex neural network experiments, where Adam is only shown empirically to work (§6.2, p. 6). Hyperparameters were grid-searched and the best setting reported for every method (p. 5).

Wiki note: the regret proof is the paper's only theory; this page has not checked it. Later literature has questioned that proof, not covered by any source here **[unverified]**.

## Connections

- Builds on SGD and [[Momentum]] (compared against Nesterov SGD); the stochastic setting is that of [[SGD]].
- Used as the standard optimizer for the VAE and normalizing flow papers ([[VAE paper (Kingma 2014)]]).
- The diagonal preconditioner idea is shared with preconditioned [[SGLD]] and Riemannian samplers ([[Riemannian manifold HMC]]).

%% refs:start %%
**Cites in this wiki**: [[AlexNet (Krizhevsky 2012)]], [[Init and momentum (Sutskever 2013)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[Amortized VI for inverse problems (Karumuri 2024)]], [[Amortized VI when and why (Margossian 2024)]], [[Attention is all you need (Vaswani 2017)]], [[Bayesian DenseED surrogate (Zhu 2018)]], [[Cardiac activation PINN (Sahli Costabal 2020)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[DDPM (Ho 2020)]], [[Deep Koopman (Lusch 2018)]], [[Deep Sets paper (Zaheer 2017)]], [[Expert's guide to PINNs (Wang 2023)]], [[Fourier features (Tancik 2020)]], [[HNNs (Greydanus 2019)]], [[IFT for engineering inverse problems (Alberts 2024)]], [[IFT thermal conductivity (Alberts 2026)]], [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[Respecting causality (Wang 2022)]], [[SINDy autoencoders (Champion 2019)]], [[Spectral bias (Rahaman 2019)]], [[Symbolic models from deep learning (Cranmer 2020)]], [[Variational dropout (Kingma 2015)]], [[Variational graph auto-encoder (Kipf 2016)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `papers/ML/Kingma, Lei Ba - Adam.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adam]]
- [[Momentum]]
- [[SGD]]
- [[Gradient descent]]
- [[Dropout]]
- [[Init and momentum (Sutskever 2013)]]
- [[VAE paper (Kingma 2014)]]
- [[SGLD]]
- [[Riemannian manifold HMC]]
