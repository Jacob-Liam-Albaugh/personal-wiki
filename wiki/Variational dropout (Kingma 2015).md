---
type: paper
area: bayesian
areas: [bayesian, ml]
source-ref: "Kingma, Salimans, Welling 2015, NIPS, §2.3, §3, eqs. 3-12"
tags: [bayesian, vi, ml]
authors: ["[[Diederik P. Kingma]]", "[[Tim Salimans]]", "[[Max Welling]]"]
year: 2015
venue: "NIPS 2015 (Advances in Neural Information Processing Systems 28)"
file: "papers/Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf"
---

# Variational Dropout and the Local Reparameterization Trick (Kingma, Salimans, Welling 2015)

**Summary**: For SGVB over network weights, sampling one weight matrix per minibatch leaves the per-example losses correlated, so gradient variance does not fall with batch size. The local reparameterization trick instead samples each layer's pre-activations directly, giving independent noise per example, variance scaling as $1/M$, and an over 200x speedup versus per-example weight samples. Gaussian dropout is a special case, and learning the dropout rates gives "variational dropout".

**Authors**: Diederik P. Kingma, Tim Salimans, Max Welling (Kingma and Welling: University of Amsterdam; Salimans: Algoritmica; Welling also UC Irvine and CIFAR) · **Year**: 2015 · **File**: `papers/Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`

The PDF has no venue header. NIPS 2015, pp. 2575-2583, comes from the citation in the reference list of [[Intro to VAEs (Kingma 2019)]]. A Finder alias of this PDF also exists at `papers/ML/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick`; it is not a separate source. The PDF is the 9-page main text only: appendices A-F (log-uniform prior derivation, KL approximation, variance analysis) are cited in the text but are not in the file.

---

## Problem

Bayesian inference over network weights $w$ is attractive against overfitting but has not beaten dropout in practice (pp. 1-2). Earlier SGVB for weights ([[VAE paper (Kingma 2014)]] appendix F; Rezende et al. 2014; Blundell et al. 2015) is limited by high gradient variance. Two questions: (1) can that variance be cut while staying parallelizable on GPUs; (2) can dropout be given a Bayesian justification that lets its rates be learned?

## Method

Data $D$ of $N$ i.i.d. pairs $(x,y)$, model $p(y|x,w)$, prior $p(w)$, approximate posterior $q_\phi(w)$.

> [!definition] Variational bound ([[ELBO]])
> $$\mathcal L(\phi) = -D_{KL}\big(q_\phi(w)\,\|\,p(w)\big) + \mathcal L_D(\phi)$$
> $$\mathcal L_D(\phi)=\sum_{(x,y)\in D} E_{q_\phi(w)}\big[\log p(y|x,w)\big]$$
>
> (source: Kingma Salimans Welling VD, eqs. 1-2, p. 2)

> [!definition] SGVB estimator with a shared weight sample
> With $w=f(\epsilon,\phi)$, $\epsilon\sim p(\epsilon)$ and minibatch $(x_i,y_i)_{i=1}^M$:
> $$\mathcal L_D^{SGVB}(\phi)=\tfrac NM\sum_{i=1}^M \log p\big(y_i|x_i,w=f(\epsilon,\phi)\big)$$
> Unbiased and differentiable. (source: eq. 3, p. 2)

> [!theorem] Variance does not shrink with M
> Writing $L_i=\log p(y_i|x_i,w=f(\epsilon_i,\phi))$, 
> $$\mathrm{Var}\big[\mathcal L_D^{SGVB}\big]=N^2\Big(\tfrac1M\mathrm{Var}[L_i]+\tfrac{M-1}{M}\mathrm{Cov}[L_i,L_j]\Big)$$
> The first term falls as $1/M$; the covariance term does not, and can dominate even at moderate $M$.
>
> (source: eqs. 4-5, p. 3; minibatches drawn with replacement, without-replacement case in appendix F, not in this PDF)

> [!algorithm] Local reparameterization trick ([[Local reparameterization trick]])
> Goal: make $\mathrm{Cov}[L_i,L_j]=0$ cheaply. Weights only affect the loss through the pre-activations $B=AW$, so sample $B$ directly. For a factorized Gaussian $q_\phi(w_{i,j})=N(\mu_{i,j},\sigma_{i,j}^2)$ and input $A$ ($M\times K$):
> $$q_\phi(b_{m,j}|A)=N(\gamma_{m,j},\delta_{m,j})$$
> $$\gamma_{m,j}=\sum_i a_{m,i}\mu_{i,j},\quad \delta_{m,j}=\sum_i a_{m,i}^2\sigma_{i,j}^2$$
> $$b_{m,j}=\gamma_{m,j}+\sqrt{\delta_{m,j}}\,\zeta_{m,j},\quad \zeta_{m,j}\sim N(0,1)$$
>
> (source: eq. 6, p. 4 and the text of §2.3)

Cost argument (p. 3-4): a 1000-unit layer with per-example weight matrices needs $M$ million random numbers and $M$ separate vector-matrix products that BLAS or convolution libraries cannot batch. Local reparameterization needs $M\times1000$ numbers, a thousand-fold saving, and keeps one matrix-matrix product.

Why variance is lower than even per-example weight sampling (p. 4): for $M=1$, the gradient wrt $\sigma_{i,j}^2$ is
$$\frac{\partial\mathcal L}{\partial\sigma^2_{i,j}}=\frac{\partial\mathcal L}{\partial b_{m,j}}\frac{\epsilon_{i,j}a_{m,i}}{2\sigma_{i,j}}\ \text{(weights, eq. 7)},\qquad \frac{\partial\mathcal L}{\partial\sigma^2_{i,j}}=\frac{\partial\mathcal L}{\partial b_{m,j}}\frac{\zeta_{m,j}a_{m,i}^2}{2\sqrt{\delta_{m,j}}}\ \text{(local, eq. 8)}$$
Estimating the gradient means estimating the covariance between $\partial\mathcal L/\partial b$ and the noise. With local noise each $b_{m,j}$ has a single $\zeta_{m,j}$; with weight noise, a thousand $\epsilon_{i,j}$ feed each $b$, so individual effects are lost in noise. The rigorous version is in appendix D (not in the PDF).

### Variational dropout

Dropout multiplies layer inputs by noise: $B=(A\circ\xi)\theta$, $\xi_{i,j}\sim p(\xi_{i,j})$ (eq. 9, p. 4). Bernoulli noise with drop rate $p$ (Hinton et al.) can be replaced by Gaussian $N(1,\alpha)$, $\alpha=p/(1-p)$ (Srivastava et al.).

- **Type B, independent weight noise** (§3.1): $\xi\sim N(1,\alpha)$ gives
  $$q_\phi(b_{m,j}|A)=N(\gamma_{m,j},\delta_{m,j}),\ \gamma_{m,j}=\sum_i a_{m,i}\theta_{i,j},\ \delta_{m,j}=\alpha\sum_i a_{m,i}^2\theta_{i,j}^2$$
  (eq. 10, p. 5). Wang and Manning's "fast dropout" ([[Variational dropout|gaussian dropout]]) samples $b$ from this directly; the paper shows it is local reparameterization of $q_\phi(w_{i,j})=N(\theta_{i,j},\alpha\theta_{i,j}^2)$.
- **Type A, correlated weight noise** (§3.2, eq. 11): $b_m=a_mW$ with $w_i=s_i\theta_i$ and $q_\phi(s_i)=N(1,\alpha)$. The $\theta_i$ are point estimates, the scales $s_i$ carry the posterior. Original Gaussian dropout (eq. 9) is a local reparameterization of this.

> [!definition] Dropout posterior and its prior ([[Variational dropout]])
> Any $q(W)$ whose noise enters multiplicatively, via a mean parameter $\theta$ and noise parameters $\alpha$, is a "dropout posterior". For dropout training of $\theta$ to coincide with maximizing a bound
> $$E_{q_\alpha}[\mathcal L_D(\theta)]-D_{KL}\big(q_\alpha(w)\,\|\,p(w)\big)$$
> (eq. 12), $D_{KL}$ must not depend on $\theta$. The only prior with this property is the scale-invariant log-uniform prior ([[Variational dropout|scale invariant log uniform prior]])
> $$p(\log|w_{i,j}|)\propto c$$
>
> (source: §3.3, p. 5; proof in appendix C, not in the PDF)

Interpretation (p. 5): this prior is the one for which the floating-point format is an optimal code (MDL, appendix A); the KL term regularizes the number of significant digits stored per weight.

For $q(w_{i,j})=N(\theta_{i,j},\alpha\theta_{i,j}^2)$ the negative KL is not analytic. The paper gives an approximation, stated as extremely accurate (appendix C derivation not in PDF):
$$-D_{KL}[q_\phi(w_i)\|p(w_i)]\approx \text{const}+0.5\log\alpha+c_1\alpha+c_2\alpha^2+c_3\alpha^3$$
$$c_1=1.16145124,\ c_2=-1.50204118,\ c_3=0.58629921$$
(§3.3, p. 6). The same expression serves the correlated-noise posterior over $s$.

> [!algorithm] Adaptive dropout rates
> Because eq. 12 is a proper objective, maximize it also wrt $\alpha$, giving a rate per layer, per neuron, or per weight. Very large $\alpha$ are poor local optima with large-variance gradients, so training constrains $\alpha\le1$ (posterior std at most the posterior mean, equivalent to dropout rate 0.5).
>
> (source: §3.4, p. 6)

## Results

Setup (p. 7): MNIST, fully connected net with 3 hidden ReLU layers, dropout $p=0.5$ hidden / $0.2$ input as in earlier work, Theano, Adam with default hyperparameters and temporal averaging, early stopping on a validation set. Compared: binary dropout, Gaussian dropout A (pre-linear, Srivastava) and B (post-linear, Wang-Manning), variational dropout A and B.

**Gradient variance** (Table 1, p. 7): empirical variance of minibatch gradient estimates ($M=1000$), variational dropout with independent weight noise.

| estimator | top 10 ep | top 100 ep | bottom 10 ep | bottom 100 ep |
|---|---|---|---|---|
| local reparameterization | 7.8e3 | 1.2e3 | 1.9e2 | 1.1e2 |
| weight sample per data point | 1.4e4 | 2.6e3 | 4.3e2 | 2.5e2 |
| weight sample per minibatch | 4.9e4 | 4.3e3 | 8.5e2 | 3.3e2 |
| no dropout noise | 2.8e3 | 5.9e1 | 1.3e2 | 9.0e0 |

Local reparameterization has the lowest variance among variational estimators in every column, though still above the no-noise baseline. The $1/M$ scaling matters most early in training (compare minibatch vs per-datapoint sampling); drawing fewer random numbers gives a further factor of about 2 that stays stable (local vs per-datapoint).

**Speed** (p. 7): per epoch on a modern GPU, 1635 s for per-datapoint weight samples vs 7.4 s for local reparameterization, "over 200 fold".

**Classification error** (Fig. 1, p. 8): adaptive variational dropout "performs equal or better" than non-adaptive Gaussian dropout and standard dropout in all tested conditions, most visibly for small networks, where fixed-rate dropout underfits and variational dropout learns lower rates. MNIST: 3 hidden layers, average of 5 runs. CIFAR-10: two conv layers (32k and 64k maps, stride 2, softplus) plus two dense layers of 128k units, over sizes $k$. Scaling the KL term down by 3 ("Variational (A2)") prevents underfitting and beats all other dropout variants in the tested models. Fig. 1 reports curves; I did not extract numeric error values.

## Limitations

- Stated: very large $\alpha$ are hard-to-escape local optima, so $\alpha$ is capped at 1 (p. 6). The KL needs down-weighting by 3 in the best variant, which departs from the exact bound (p. 8).
- Stated: variance is still "substantially higher" than training without dropout noise (p. 7). The Gaussian marginal for binary dropout ignores dependencies between elements of $B$ and rests on the CLT (p. 5).
- Wiki note: results are on MNIST and CIFAR-10 with moderate nets; predictive uncertainty is not evaluated here. This PDF omits all appendices, so the derivations of the log-uniform prior, KL approximation and variance proof cannot be checked from this source.

## Connections

- Builds on the global-weight SGVB of [[VAE paper (Kingma 2014)]] (appendix F), and is described in the later [[Intro to VAEs (Kingma 2019)]] reference list; the monograph's text on Bayesian neural networks and local reparameterization in chapters 2-4 is not in the extracted PDF.
- Re-derives Gaussian dropout (Wang and Manning 2013, Srivastava et al. 2014) as variational inference; related Bayesian readings of dropout: Gal and Ghahramani 2015, Maeda 2014 (p. 6). See [[Variational dropout]], [[Variational dropout|gaussian dropout]].
- Alternative to MCMC for network weights: the paper cites Neal 1995 and Welling and Teh 2011 ([[SGLD (Welling 2011)]], [[SGLD]]) for sampling-based Bayesian networks (p. 1). Averaging over samples relates to [[Bayesian model averaging]] (Wiki note).
- Wiki note: any [[Reparameterization trick]] gradient with a shared noise draw per minibatch has this covariance issue; the fix applies when the noise passes through a low-dimensional intermediate (activations).

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Dropout paper (Srivastava 2014)]], [[SGLD (Welling 2011)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[Bayesian DenseED surrogate (Zhu 2018)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick.pdf`; alias `papers/ML/Kingma, Welling, Salimans - Variational Dropout & Local Reparameterizing Trick`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Local reparameterization trick]]
- [[Variational dropout]]
- [[Reparameterization trick]]
- [[ELBO]]
- [[VAE paper (Kingma 2014)]]
- [[Intro to VAEs (Kingma 2019)]]
- [[Bayesian model averaging]]
- [[SGLD]]
- [[Dropout paper (Srivastava 2014)]]. Gaussian dropout noise N(1, p/(1-p)) comes from Srivastava 2014, §10.
