---
type: definition
area: gp
areas: [gp, bayesian, ml]
source-ref: "Matthews et al. 2018, eqs. 1-9, 15, Thm 4; Jacot et al. 2018, Prop. 1; Fortuin 2022, eqs. 8-9"
tags: [gp, bayesian, ml]
---

# Neural network Gaussian process

> [!definition] NNGP (infinite-width prior)
> For a fully connected network with iid Gaussian weights scaled by the width, $w^{(\mu)}\sim N(0,\hat C_w/H_{\mu-1})$, $b\sim N(0,C_b)$, the output converges in distribution as all hidden widths $\to\infty$ to a zero-mean Gaussian process, independent across output units, with kernel given by the recursion
> $$K^{(\mu)}(x,x')=\hat C_w\,\mathbb E_{(u,v)\sim N(0,K^{(\mu-1)})}\big[\phi(u)\phi(v)\big]+C_b,$$
> where $K^{(\mu-1)}$ is the $2\times2$ covariance of the previous layer at $(x,x')$ and the first layer is $K^{(1)}(x,x')=C_w^{(1)}\,x^\top x'+C_b^{(1)}$ (its weights have variance $C_w^{(1)}$, not width-scaled).
>
> (source: Matthews et al., eqs. 9 and 15, Lemma 2 and Thm 4, pp. 6-9; Jacot et al., Prop. 1, p. 5)

**Notation**: this page uses Matthews' $\hat C_w,C_b$. [[NTK (Jacot 2018)]] writes $\Sigma^{(L)}$ with unit weight variance and a bias term $\beta^2$ and divides the first layer by $n_0$; [[Priors in Bayesian deep learning (Fortuin 2022)]] writes $\sigma_w^2,\sigma_b^2$ and $k^\ell$.

**Intuition**: each output unit is a sum of many weakly dependent terms, so a central limit theorem makes its value Gaussian. The covariance at the next layer is then an expectation of $\phi\phi$ under the Gaussian of the layer below, which gives a layer-by-layer recursion. Predictions of the infinite network are ordinary GP regression with this kernel.

## What is proved
- One hidden layer: multivariate CLT, Neal 1996 (Matthews §2.1).
- Several hidden layers, widths growing jointly at any strictly increasing rates: Matthews Thm 4 (weak convergence, countable input set, continuous $\phi$ with the linear envelope $|\phi(u)|\le c+m|u|$). The proof uses exchangeability and a CLT for exchangeable arrays (Blum et al.).
- Lee et al. (2018, cited not read) take the widths to infinity one layer after another; Matthews notes this is the weaker form (p. 4).

## Examples
- $\phi(u)=\Theta(u)u^r$, $r=0,\dots,3$ have closed forms (Cho and Saul); ReLU is $r=1$ (Matthews §3, p. 9).
- Empirical closeness for finite widths: squared MMD to the GP falls with width and rises with depth (Matthews Fig. 2); a 3x50 ReLU Bayesian network matches exact GP posteriors on five of six small datasets, but not on the 6-dimensional yacht data (Matthews §5).

## Failure modes / non-examples
- The limit has a fixed kernel and so no learned hierarchical features (MacKay, Neal, Matthews §7). To avoid it: narrow layers, heavy-tailed weights, or coupled weights.
- It describes the prior at initialization only. Training by gradient descent in the same limit is governed by the [[Neural tangent kernel]], a different kernel built from the same recursion; the posterior of the NNGP is Bayesian inference, not SGD (Jacot, Thm 2).
- Not covered: non-Gaussian weights (e.g. scale mixtures), continuity or differentiability of sample paths.

## Where it appears
- [[Wide networks as GPs (Matthews 2018)]] — proof and experiments.
- [[NTK (Jacot 2018)]] — Prop. 1 re-derives the limit and uses $\Sigma^{(L)}$ inside $\Theta_\infty^{(L)}$.
- [[Priors in Bayesian deep learning (Fortuin 2022)]] — survey statement of the NNGP kernel (eqs. 8-9).
- [[Bayesian neural networks]] — infinite-width limit of the weight-space prior.

**Sources**: `papers/Guassian Processes/Matthews et al - Gaussian Process Behaviour in Wide Deep Neural Networks.pdf`, `papers/ML/Jacot, Gabriel, Hongler - Neural Tangent Kernel Convergence and Generalization in Neural Networks.pdf`, `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Gaussian process]] · [[Neural tangent kernel]] · [[Bayesian neural networks]] · [[Kernel methods]]
- [[Wide networks as GPs (Matthews 2018)]] · [[NTK (Jacot 2018)]] · [[Weight initialization]]
