---
type: concept
area: me697
areas: [me697, gp]
tags: [uq, gp, ml, bayesian]
---

# Active learning

**Summary**: Training a model on data it chooses itself. Start from a few labeled points, score every candidate input with an acquisition function, evaluate the best one, update, repeat. In surrogate modeling it cuts the number of expensive simulations or experiments.

---

## Definition
> [!definition] Acquisition-driven loop
> Given the posterior $p(f\mid\mathcal D_t)$, choose
> $$\mathbf x_{t+1}=\arg\max_{\mathbf x}\alpha_t(\mathbf x)$$
> query the true function, add the pair to $\mathcal D_t$, re-condition. Stop when the best $\alpha_t$ falls below a threshold or the budget runs out.
> (source: ME 697 book, `up/al/01_al_basics.md`)

## Acquisition functions
- **Uncertainty sampling**: expected information gain (MacKay 1992), approximately proportional to the predictive variance $\sigma_t^2(\mathbf x)$ over the noise variance. Pushes samples to the domain boundary.
- **Value of information**: expected utility $\mathbb E[v_t(y)-c_t(\mathbf x)]$; expected improvement is a special case.
- **Multi-fidelity**: acquisition $\alpha_t(s,\mathbf x)$ also picks a fidelity $s$ and balances information against cost.
- **Multi-objective**: hypervolume improvement.

## Notes
- Needs a model with a usable predictive uncertainty: [[Gaussian process]] (closed form), generalized linear models, or neural networks with a Laplace approximation or samples.
- Candidate points are found by random or space-filling search ([[Latin hypercube sampling]]) when the argmax is not analytic.
- Wiki note: the information gain in the book is the small-variance form of $\tfrac12\log(1+\sigma_t^2/\sigma^2)$; the argmax is the same.

## Setting and loop
> [!definition] Bayesian regression setting
> Regression $f:\mathcal X\to\mathbb R$ with prior $p(f)$ and likelihood $p(y\mid\mathbf x,f)$. Data $\mathcal D=\{(\mathbf x_i,y_i)\}$, conditionally independent given $f$. Posterior predictive:
> $$p(y\mid\mathbf x,\mathcal D)=\int p(y\mid\mathbf x,f)\,p(f\mid\mathcal D)\,Df$$
> with mean $\mu(\mathbf x\mid\mathcal D)$ and variance $\sigma^2(\mathbf x\mid\mathcal D)$.

> [!algorithm] Active learning loop
> 1. Start with a small, space-filling $\mathcal D_{n_0}$ and condition the model.
> 2. Find $\mathbf x_{t+1}=\arg\max_{\mathbf x}\alpha_t(\mathbf x)$.
> 3. If $\alpha_t(\mathbf x_{t+1})$ is below a threshold, stop.
> 4. Query $y_{t+1}=f_{\text{true}}(\mathbf x_{t+1})$, append, re-condition.

> [!theorem] Expected information gain (after MacKay 1992)
> The information gain of a hypothetical observation $(\mathbf x,y)$ is the KL divergence from old to new posterior. Averaged over the unknown $y$, it equals the drop in posterior entropy:
> $$\alpha_t(\mathbf x)=S_t-\mathbb E\big[S_{t+1}(\mathbf x,y)\mid\mathbf x\big]$$
> The reference measure $m(f)$ in the entropy cancels. With a Gaussian approximation of the posterior,
> $$\alpha_t(\mathbf x)\approx\frac12\,\frac{\sigma_t^2(\mathbf x)}{\sigma^2}$$
> which is uncertainty sampling. With input-dependent noise divide by $\sigma^2(\mathbf x)$, so equal epistemic uncertainty favors the less noisy region. (source: `01_al_basics.md`)

Further acquisition details:
- **Value of information**: utility $u_t(\mathbf x,y)=v_t(y)-c_t(\mathbf x)$ (value of output minus cost), acquisition $\alpha_t(\mathbf x)=\mathbb E[u_t(\mathbf x,y)\mid\mathbf x]$.
- **Multi-fidelity example** from the book, with $\lambda$ trading information against cost $c_s$:
$$\alpha_t(s,\mathbf x)=\lambda\frac{\sigma_{t,s}^2(\mathbf x)}{\sigma_s^2}-(1-\lambda)\,c_s(\mathbf x)$$
  See [[Multi-fidelity modeling]].
- **Multi-objective**: hypervolume improvement for a Pareto front (Beume et al. 2007; Pandita et al. 2018).

## Examples
> [!example] 1D uncertainty sampling (02)
> Data from $\sin(10x^2)+x$ plus noise ($0.1$). Fixed GP hyperparameters (RBF, amplitude 4, length scale 0.15, noise sd 0.1) because one point cannot train a model. The next point maximizes the predictive variance, found by random search over 1000 [[Latin hypercube sampling]] points. The first pick is near the boundary; nine more points are added, one per step.

> [!example] 2D uncertainty sampling (02)
> A smooth blend of two functions (a sigmoid in $x_2-x_1$ mixes a sine/cosine term with a polynomial bump). Start from 5 LHS points, then 21 more steps with an RBF GP (length scales 0.3, noise sd 0.01). The variance map is highest at the domain edge, so new points land there first.

> [!example] Homework 4, active learning part (source: homework/04_homework.ipynb)
> Random versus actively chosen training points for the Branin surrogate ([[Surrogate model]]).

Wiki notes:
- Typo in the book: `mu(\mathbf{x}|\mathcal{D}_{n_0})` is missing a backslash.
- The notebook's `get_next_x` takes the best of 1000 random LHS points, so the pick is approximate, not a true argmax.
- The "optimally efficient" claim holds for the hand-set hyperparameters; refitting them as data arrives would change the variances.
- The multi-fidelity example subtracts a cost from a dimensionless variance ratio, so $\lambda$ also sets the exchange rate between them.

**Covered in**: ASML book up/al (ME 697 2.5); homework 4
**Sources**: ME 697 book `up/al/`, `advanced-scientific-machine-learning/book/up/al/intro.md`, `01_al_basics.md`, `02_al.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Multi-fidelity modeling]]
- [[Surrogate model]] · [[Gaussian process]] · [[KL divergence]]
