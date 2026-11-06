---
type: paper
area: bayesian
areas: [variational-inference]
source-ref: "Margossian, Blei 2024, UAI, arXiv:2307.11018v4"
tags: [bayesian, vi]
authors: [Margossian, Blei]
year: 2024
venue: "UAI 2024 (40th Conference on Uncertainty in Artificial Intelligence)"
file: "Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf"
---

# Amortized variational inference: when and why? (Margossian 2024)

**Summary**: Asks when amortized VI (one shared inference function mapping each observation to its local approximate posterior) can reach the same optimum as factorized (mean-field) VI. Proves that, for exchangeable latent variable models, the gap closes in general exactly for simple hierarchical models; shows how widening the function's input rescues some time-series models and that HMMs and dense hierarchical models cannot be rescued.

**Authors**: Charles C. Margossian (Flatiron Institute), David M. Blei (Columbia) · **Year**: 2024 · **File**: `Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`

---

## Problem

Model $p(\theta,z,x)$ with local latents $z_{1:N}$, observations $x_{1:N}$, global $\theta$. [[Variational inference]] minimises $\mathrm{KL}(q\,\|\,p(\theta,z\mid x))$ ([[KL divergence]]) over a family (source: file, eq. 1).

> [!definition] Two variational families (source: file, eqs. 2-3)
> Factorized (F-VI): $\;\mathcal Q_F=\{q:\ q(\theta,z)=q_0(\theta)\prod_{n=1}^N q_n(z_n)\}$ with a free parameter $\nu_n$ per datum.
> Amortized (A-VI): $\;\mathcal Q_A=\{q:\ q(\theta,z)=q_0(\theta)\prod_{n=1}^N q(z_n;f_\phi(x_n))\}$ with one shared inference function $f_\phi:\mathcal X\to\mathcal U$.

A-VI is the machinery inside the VAE encoder. The "amortization gap" is A-VI's suboptimality relative to F-VI (Cremer et al. 2018; cited). The paper asks for conditions on the model (not on the network) under which that gap can be closed, and treats full Bayesian inference over $\theta$, not a point estimate of $\theta$ as in variational EM (p. 2). See [[Amortized VI]].

## Method (theory)

> [!theorem] Proposition 2.1: A-VI is strictly poorer (source: file, p. 3)
> For any class $\mathcal F$ of inference functions, $\mathcal Q_A(\mathcal F)\subsetneq\mathcal Q_F$.
> Proof idea: if $x_n=x_m$ then $f_\phi(x_n)=f_\phi(x_m)$, but some $q\in\mathcal Q_F$ has $\nu_n\ne\nu_m$.

So A-VI can never beat F-VI; the gap closes only if $f_\phi$ can reproduce F-VI's optimum.

> [!definition] Amortization interpolation problem and ideal inference function (source: file, eq. 5, Def. 2.2)
> $$f_\phi(x_n)=\nu_n^*\quad\forall n$$
> A function $f$ solving this for a dataset $x$ is an *ideal inference function*. Two requirements: (i) the problem is well posed (a property of the model); (ii) the class $\mathcal F$ is expressive enough (a property of the algorithm; studied empirically in §4).

> [!theorem] Lemma 3.1: CAVI rule at the optimum (source: file, eq. 6, App. A.1)
> $$q(z_n;\nu_n^*)\ \propto\ \exp\Big\{\mathbb E_{q(\theta;\nu_0^*)}\,\mathbb E_{q(z_{-n};\nu^*)}\big[\log p(\theta,z,x)\big]\Big\}$$

> [!definition] Exchangeable latent variable model (source: file, Def. 3.2)
> (i) local dependence: edge $x_n\!-\!z_n$ with $p(x_n\mid z,\theta)\ne p(x_n\mid z_{-n},\theta)$; (ii) conditional independence $p(x\mid z,\theta)=\prod_n p(x_n\mid z,\theta)$; (iii) common distributional forms: no density depends on the index.

> [!definition] Simple hierarchical model (source: file, Def. 3.3, eq. 4)
> $$p(\theta,z,x)=p(\theta)\prod_{n=1}^N p(z_n\mid\theta)\,p(x_n\mid z_n,\theta)$$
> (Agrawal and Domke 2021; the intro eq. 4 writes $p(z_n)$ without $\theta$-dependence.)

> [!theorem] Theorem 3.4: existence of an ideal inference function (source: file, p. 4, App. A.2)
> 1. If $p(\theta,z,x)$ is a simple hierarchical model, an ideal inference function $f_x$ with $f_x(x_n)=\nu_n^*$ exists.
> 2. If an ideal inference function exists for *every* $p$ that factorizes according to a graph, that graph is the simple hierarchical one.

Proof sketch (pp. 4-5, 11-12). (1) Apply Lemma 3.1: all terms not involving $z_n$ drop and
$$q(z_n;\nu_n^*)\propto\int g(\theta,x)\,[\,m(\theta,z_n)+h(\theta,z_n,x_n)\,]\,d\theta,$$
where $g=q(\theta;\nu_0^*(x))$ is common to every factor and only $x_n$ is local, hence $x_n=x_m\Rightarrow\nu_n^*=\nu_m^*$. (2) Any dependence of the kernel of $q(z_n)$ on $x_{i\ne n}$ that is not shared across factors must be removed. That forces $p(x_i\mid z_n,z_{-n},\theta)=p(x_i\mid z_i,\theta)$ (eq. 21) and $p(z_n\mid z_{-n},\theta)=p(z_n\mid\theta)$ (eq. 23), i.e. the simple hierarchical factorization. The theorem is stated for a class of models to exclude trivial symmetric edge cases (Remark 3.5, App. A.3: a likelihood depending only on $\sum_n z_n$ has a constant ideal function, but then "local latent" is meaningless).

> [!theorem] Proposition 3.6: linear model has a 3-parameter ideal function (source: file, eqs. 8-10, App. A.4)
> Model $p(\theta)\propto1$, $p(z_n)=N(0,1)$, $p(x_n\mid z_n,\theta)=N(\theta+\tau z_n,\sigma^2)$. The optimal factorized-Gaussian F-VI solution has
> $$\mathbb E_{q^*}[z_n]=\frac{\tau}{\sigma^2+\tau^2}(x_n-\bar x)=\alpha_0(x)+\alpha x_n,\qquad \mathrm{Var}_{q^*}(z_n)=\xi^2\ (\text{constant in }x),$$
> $\alpha=\tau/(\sigma^2+\tau^2)$, $\alpha_0(x)=-\tau\bar x/(\sigma^2+\tau^2)$. A linear function for the mean plus a constant variance closes the gap regardless of $N$. This illustrates *partial pooling*: $p(z_n\mid x)\ne p(z_n\mid x_n)$, yet the global influence $\bar x$ is common to all factors.

**Beyond simple hierarchical models** (§3.2):
- *Saw time series* $p(\theta)\prod_n p(z_n\mid x_{n-1})p(x_n\mid z_n,\theta)$ (eq. 11): CAVI gives $q(z_n;\nu_n^*)\propto p(z_n\mid x_{n-1})\exp\{\mathbb E_{q(\theta)}\log p(x_n\mid z_n,\theta)\}$ (eq. 12). No ideal $f:\mathcal X\to\mathcal U$ exists, but one on $\mathcal X\times\mathcal X$ with input $(x_{n-1},x_n)$ does. The first latent, whose $x_0$ is unobserved, gets its own free parameter (Remark 3.7).
- *Hidden Markov model* $p(\theta)\prod_n p(z_n\mid z_{n-1})p(x_n\mid z_n,\theta)$ (eq. 13).

> [!theorem] Proposition 3.8: HMMs (source: file, p. 5, App. A.5)
> For an HMM and any strict subset $w_n\subset x$ as input, there exist models with no ideal $f_x:\mathcal W\to\mathcal U$.
> Counterexample (eq. 42): $p(z_0)\propto1$, $p(z_n\mid z_{n-1})=N(z_{n-1},1)$, $p(x_n\mid z_n)=N(z_n,1)$, $N=100$, all $x_n=1$. The posterior precision is tridiagonal (eqs. 43-47), $\nu^*=\mu=-2\Psi^{-1}x$, and the optimal means differ across $n$ (Fig. 8). Taking the full dataset as input makes A-VI equal F-VI trivially (Remark 3.9).

Intuition (p. 6): in simple hierarchical and saw models every datum has either a local or a common global influence on $q(z_n)$; in an HMM every $x_m$ influences each $z_n$ differently, and the same holds for dense hierarchical models including Gaussian processes.

## Results

Setup (§4.1): factorized Gaussians, ELBO by Monte Carlo (100 draws), Adam with lr $10^{-3}$, [[Reparameterization trick]] gradients, 10 seeds, wall-time reported. Baselines: F-VI (richest family) and a "constant factor" that gives every $z_n$ the same Gaussian (poorest). A-VI fits $q(\theta)$ as in F-VI and an inference net for $q(z_n)$.

- **Linear model** ($N=10{,}000$, §4.2): a degree-1 polynomial $f_\phi$ matches F-VI's ELBO, as Prop. 3.6 predicts, and converges about an order of magnitude faster. Degree 2 also reaches the optimum but converges more slowly.
- **Nonlinear model** ($N=10{,}000$, eq. 15, §4.3): two-hidden-layer ReLU net matches F-VI for width $k\ge4$; overparameterised nets converge faster in median, but A-VI is more seed-sensitive and sometimes fails to converge in 20,000 iterations. $k=16$ is "fast and reasonably stable".
- **Bayesian neural network** (FashionMNIST, 10,000 images, $x\in\mathbb R^{784}$, $z\in\mathbb R^{64}$, $\theta\in\mathbb R^{57{,}232}$, §4.4): A-VI reaches F-VI's ELBO for width $k\ge64$; to reach MSE below 0.03 it needs 2-3 times fewer iterations but each is costlier, so the wall-time speed-up is about 25%. Test-set reconstruction MSE is close to training MSE (App. B, Fig. 9); F-VI has no way to infer on new images.
- **Saw time series** ($N=1000$, §4.5): with input $x_n$ only, no network (even $k=20$) reaches F-VI's optimum; with $(x_{n-1},x_n)$ and $k\ge4$ it does and is seed-stable.

Across examples the inference network's size need not scale with $N$, whereas F-VI's parameter count does (p. 3).

## Limitations

As stated (§5):
- Existence of an ideal function does not say how rich the function class must be; only an informal diagnostic is offered (run a few F-VI steps after A-VI converges; improvement signals a gap), which may miss gaps in high-dimensional non-convex problems.
- Unclear whether overparameterisation helps or burdens optimisation (it slowed the linear model, sped up the BNN and saw series); A-VI can be seed-sensitive.
- Held-out accuracy, online learning ($f_\phi(x_{N+1})$ vs the exact $p(z\mid x,x_{N+1})$) and complex datasets are left open.
- Analysis excludes inference functions that also take latent variables (these target the inference gap, not the amortization gap).

Wiki note: results are for mean-field Gaussians and small problems; the theorem concerns reaching F-VI's optimum, not the true posterior, so a closed amortization gap still inherits mean-field's variance underestimation (the paper cites this, App. A.4).

## Connections

- Gives the theory missing from [[Amortized VI for inverse problems (Karumuri 2024)]]: that paper trains a data-to-posterior network over *whole datasets*, a different (joint-over-$y$) setting from Margossian and Blei's per-datum latents, but both rest on the same idea of one function replacing per-dataset optimisation. Its "no amortization gap" assumption in Theorem 2 is the practical counterpart of an ideal inference function. Wiki note: the inverse-problem setting has one latent $\xi$ per dataset $y$, so it is the "$N=1$ per dataset, many datasets" regime, not the exchangeable-$N$ regime analysed here; the correspondence is loose.
- The per-dataset optimisation of [[Variational inverse problems (Tsilifis 2014)]] is the F-VI analogue that amortization replaces.
- Uses the [[Reparameterization trick]] and [[ELBO]]; frames the VAE encoder as A-VI. Mentions semi-amortized VI (A-VI then F-VI refinement) as justification when the gap cannot be closed.

**Sources**: `Bayesian/Margossian, Blei - Amortized Variational Inference When & Why.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Amortized VI]]
- [[Variational inference]]
- [[ELBO]]
- [[KL divergence]]
- [[Reparameterization trick]]
- [[Amortized VI for inverse problems (Karumuri 2024)]]
- [[Variational inverse problems (Tsilifis 2014)]]
