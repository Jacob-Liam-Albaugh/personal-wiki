---
type: method
area: ml
areas: [me697, ml, stochastic]
source-ref: "ME 697 book, ml-software/optimization/05_sgd"
tags: [optimization, ml]
---

# Stochastic gradient descent (SGD)

> [!algorithm] Minibatch SGD
> For a loss $L(\theta)=\frac1N\sum_{i=1}^N\ell(\theta;x_i)$, draw a minibatch of size $M$ and step
> $$\theta_{t+1}=\theta_t-\alpha_t\frac1M\sum_{j=1}^M\nabla\ell(\theta_t;x_{i_j})$$
> $M=1$ is online SGD. One pass through the data is an epoch.

**Robbins-Monro steps**: convergence needs
$$\sum_t\alpha_t=\infty,\quad \sum_t\alpha_t^2<\infty$$
With a constant $\alpha$ the iterates keep wandering around the optimum (book, 05, quadratic regression in Equinox).

**Saddles**: the gradient noise helps SGD leave saddle points (book, 01).

**Relatives**
- [[SGLD]]: the same step plus Gaussian noise of variance $\alpha_t$ (Welling-Teh scaling), turning the optimizer into a sampler. See [[SG-MCMC]].
- [[Momentum]], [[Adam]]: use the same minibatch gradient with extra state.
- Stochastic L-BFGS-B exists (named in the book, 07) for second-order methods; see [[Newton's method]].

> [!example] Quadratic regression (05)
> Equinox model $\theta_0+\theta_1x+\theta_2x^2$ trained by minibatch SGD; constant-rate iterates wiggle around the least-squares fit.

**Covered in**: ASML book ml-software/optimization (ME 697 1.4)
**Sources**: `text_books/advanced-scientific-machine-learning/book/ml-software/optimization/05_sgd.ipynb`, `01_optimization_problems.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[vmap]] (per-example gradients)
- [[Init and momentum (Sutskever 2013)]], [[Dropout]] (SGD with a stochastic mask; Srivastava 2014, §5).
- [[Attention is all you need (Vaswani 2017)]]: Adam with warmup for the Transformer.
