---
type: method
area: ml
areas: [me697, ml]
source-ref: "ME 697 book, ml-software/optimization/06_adaptive (Kingma & Ba 2014)"
tags: [optimization, ml]
---

# Adam

> [!algorithm] Adam (Kingma & Ba 2014, as in the book)
> With gradient $g_t$:
> $$v_t=\beta_1v_{t-1}+(1-\beta_1)g_t$$
> $$r_t=\beta_2r_{t-1}+(1-\beta_2)g_t^2$$
> Bias correction:
> $$\hat v_t=v_t/(1-\beta_1^t)$$
> $$\hat r_t=r_t/(1-\beta_2^t)$$
> Step:
> $$x_{t+1}=x_t-\alpha\,\hat v_t/\sqrt{\hat r_t+\epsilon}$$
> Defaults: $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$, $\alpha$ between 0.001 and 0.1.

> [!failure] Where ε goes
> Wiki note: the paper and optax put $\epsilon$ outside the root, $\hat v_t/(\sqrt{\hat r_t}+\epsilon)$. The book writes it inside. The difference only matters when $\hat r_t$ is near zero.

**Lineage** (book, 06)
- delta-bar-delta (Jacobs 1988): per-parameter rates from sign agreement.
- AdaGrad (Duchi et al. 2011): $r_t=r_{t-1}+g_t^2$. The rate only decays, so the book advises against it.
- RMSProp (Hinton): exponential average $r_t=\beta r_{t-1}+(1-\beta)g_t^2$.
- Adam: RMSProp plus [[Momentum]] on the gradient plus bias correction.
- Nadam: Adam with Nesterov momentum.
- AdamW: decoupled weight decay. Weight decay acts like an L2 penalty, so do not use both.

**Wiki note**: the RMSProp denominator is the same diagonal preconditioner idea as preconditioned [[SGLD]] (Welling-Teh §3.2).

## Where it appears
- Adam followed by L-BFGS is the standard PINN optimizer pair ([[Physics-informed ML review (Karniadakis 2021)]], Box 3).
- Used to fit surrogate MLPs (lr $10^{-3}$, 5000 iterations) and GP hyperparameters (lr 0.01), and the e3nn classifier (lr 0.01): [[Surrogate model]], [[Equivariance]], [[Karhunen-Loève expansion]].
- [[PISD (Gallon 2026)]]: Adam as the guidance step inside diffusion sampling, moments kept across steps, per-frequency learning rates.

## In the paper
- Defaults: $\alpha=0.001$, $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$ (Alg. 1, p. 2).
- Wiki note: Algorithm 1 puts $\epsilon$ outside the root, $\hat m_t/(\sqrt{\hat v_t}+\epsilon)$, and so does the efficient variant (p. 2). The book's inside-the-root form is wrong.
- [[Adam paper (Kingma 2015)]]. The regret proof (§4) is questioned in later literature **[unverified]**.

> [!example] Homework 1, problem 5: autoencoder (source: homework/01_homework.ipynb)
> MNIST autoencoder, latent dimension 2, two hidden layers of 128 ReLU units, Equinox and Optax, Adam at $10^{-3}$, batch 32; then fit a 10-component Gaussian mixture to the latent space and sample from it.

**Covered in**: ASML book ml-software/optimization (ME 697 1.4); homework 1
**Sources**: `text_books/advanced-scientific-machine-learning/book/ml-software/optimization/06_adaptive.ipynb`, `text_books/advanced-scientific-machine-learning/book/ml-software/optimization/01_optimization_problems.md`, `09_gpu_training.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gradient descent]] · [[SGD]] · [[Momentum]] · [[Variational inference]] (ELBO usually trained with Adam)
- [[DeepSeek-V2 (DeepSeek-AI 2024)]]: AdamW with $\beta_1=0.9$, $\beta_2=0.95$, weight decay 0.1 (source: §3.1.2).
