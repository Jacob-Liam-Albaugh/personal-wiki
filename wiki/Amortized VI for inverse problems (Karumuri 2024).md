---
type: paper
area: bayesian
areas: [inverse-problems, scientific-machine-learning]
source-ref: "Karumuri, Bilionis 2024, arXiv:2305.20004v3"
tags: [bayesian, vi, inverse-problems, ml]
authors: ["[[Sharmila Karumuri]]", "[[Ilias Bilionis]]"]
year: 2024
venue: "arXiv:2305.20004v3 (stat.ML), 28 May 2024 (preprint; no journal given in the PDF)"
file: "Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf"
---

# Learning to solve Bayesian inverse problems with amortized VI (Karumuri 2024)

**Summary**: Learns the *Bayesian inverse map* (data to posterior) once, by maximising the expected ELBO over all datasets the model can generate. The posterior is a full-rank Gaussian or a conditional normalizing flow whose parameters are the output of an amortization network, so a new posterior costs one forward pass. Three benchmarks match NUTS MCMC; the Gaussian guide fails on a multimodal problem, the flow guide largely recovers it.

**Authors**: Sharmila Karumuri, Ilias Bilionis (Purdue) · **Year**: 2024 · **File**: `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`

Wiki note: filename lists Bilionis first; the paper's first author is Karumuri (corresponding author).

---

## Problem

[[Bayesian inverse problems]]: unknown $\xi\in\mathbb R^d$, forward model $f:\mathbb R^d\to\mathbb R^m$, data $y$, Gaussian likelihood $p(y\mid\xi)=N(y\mid f(\xi),\gamma^2 I)$ with only measurement noise modelled (source: file, §2.1). MCMC and per-dataset [[Variational inference]] (e.g. [[Variational inverse problems (Tsilifis 2014)]]) must be rerun from scratch for each new $y$, which blocks real-time uses such as structural health monitoring and medical diagnosis (pp. 1-2). Goal: learn the map $y\mapsto p(\xi\mid y)$ so the posterior for any new observation is available at forward-pass cost.

Prior art on inverse maps (pp. 2-3): invertible networks with noise-free data (ref. 49); conditional flows trained on (parameter, observation) pairs by maximum conditional likelihood, which the authors say is mean-seeking and troublesome for ill-posed problems; an invertible DeepONet ([[DeepONet]], [[Operator learning]]) with a semi-analytic posterior; transport maps via tensor trains, which struggle with many parameters and concentrated densities.

## Method

> [!definition] ELBO for a guide $q_\lambda$ (source: file, eq. 1)
> $$\mathrm{ELBO}(\lambda;y)=\mathbb E_{q_\lambda}\big[\log p(\Xi,y)\big]+H\big[q_\lambda(\Xi)\big]$$
> See [[ELBO]]; maximising it minimises [[KL divergence]] between guide and posterior.

**Amortization**: make the variational parameters a function of data, $\lambda=\lambda(y)$, in a Banach space $A$ of measurable functions with finite $L^2$ norm under the data density $p(y)=\int p(y\mid\xi)p(\xi)\,d\xi$ (data can be sampled by prior draw, forward solve, likelihood draw). See [[Amortized VI]].

> [!definition] Amortized ELBO (AELBO) (source: file, eq. 2)
> $$\mathrm{AELBO}[\lambda]=\mathbb E_{Y\sim p(y)}\Big[\mathrm{ELBO}\big(\lambda(Y);Y\big)\Big]$$

> [!theorem] Theorem 1: upper bound (source: file, p. 6)
> If $H[p(Y)]$ is finite, then $\mathrm{AELBO}[\lambda]\le\mathbb E[\log p(Y)]=-H[p(Y)]$ for every admissible $\lambda$. Proof: ELBO $\le\log p(y)$ pointwise, then take expectations. (Guarantees maximisation cannot increase forever; it does not assert the supremum is attained.)

> [!theorem] Theorem 2: AELBO maxima give ELBO maxima (source: file, pp. 7-8, eqs. 3-5)
> Assume $\mathrm{ELBO}(\lambda,y)$ is $C^2$ in $\lambda$, smoothness as needed, and **no amortization gap** (the admissible class contains the local maxima of the per-$y$ ELBO). If $\lambda$ is a local maximum of the AELBO then $\lambda(y)$ is a local maximum of the ELBO for every $y$ in the support of the data density.
> Proof sketch: the first variation vanishes in every direction $\zeta$. Choosing $\zeta_i(Y)=\delta_{ij}\delta(Y-y)$ gives $\partial_{\lambda_j}\mathrm{ELBO}(\lambda(y),y)=0$. For the second variation use $\zeta_{\epsilon,i}(Y)=x_i\,\delta_\epsilon^{1/2}(Y-y)/\sqrt{p(Y)}$ (a Gaussian bump) and let $\epsilon\to0^+$ to get $\sum_{ij}\partial^2_{\lambda_i\lambda_j}g\,x_ix_j\le-\kappa\|x\|^2<0$, so the Hessian is negative definite.

The authors read this as "optimising the AELBO is equivalent to solving all possible VI problems in one shot".

**Guide 1: amortized full-rank Gaussian** (§2.3.1). Amortization network $\lambda(y;\phi)=(\mu(y;\phi),L(y;\phi))$, with $q=N(\xi\mid\mu,LL^\top)$, built from three feed-forward ReLU nets: mean (linear output), lower-triangular part of $L$ (linear output, $d(d-1)/2$ outputs), diagonal of $L$ (softplus output for positivity).

**Guide 2: conditional normalizing flow** (§2.3.2-2.3.3). A [[Normalizing flows]] guide pushes $z_0\sim N(0,I)$ through invertible maps; density by change of variables (eq. 6 and following). Conditional version $\xi=G(z_0;y,\phi)$, built from conditional coupling blocks (CCB, ref. 54):

> [!definition] Conditional coupling block (source: file, p. 12)
> Split $u=[u_1,u_2]$, then
> $$v_1=u_1\odot\exp(s(u_2,y))+t(u_2,y),\qquad v_2=u_2\odot\exp(a(v_1,y))+b(v_1,y)$$
> $$\log|\det|=\sum_j s(u_2,y)_j+\sum_j a(v_1,y)_j$$
> Inverse: $u_2=(v_2-b(v_1,y))\oslash\exp(a(v_1,y))$, $u_1=(v_1-t(u_2,y))\oslash\exp(s(u_2,y))$. The inner nets $s,t,a,b$ need not be invertible. Each block is followed by a fixed random permutation (determinant modulus 1); none after the last block.

**Stochastic optimisation** (§2.4). Write the objective as $v(\phi)=\mathrm{AELBO}[\lambda(\cdot;\phi)]$ (eq. 7, 8).

> [!definition] Gaussian guide: reparameterized objective (source: file, eq. 9)
> With $\Xi=\mu(Y;\phi)+L(Y;\phi)Z_0$, $Z_0\sim N(0,I)$, and entropy $H=\tfrac d2\log(2\pi e)+\sum_r\log L_{rr}$:
> $$V(\phi)=\tfrac d2\log(2\pi e)+\frac1{N_y}\sum_{i=1}^{N_y}\Big[\frac1{N_z}\sum_{j=1}^{N_z}\log p\big(\mu(Y_i;\phi)+L(Y_i;\phi)Z_{0j},\,Y_i\big)+\sum_{r=1}^d\log L_{rr}(Y_i;\phi)\Big]$$

> [!definition] Flow guide: objective (source: file, eq. 10)
> With $h(Z_0;Y,\phi)=|\det\partial G/\partial Z_0|$:
> $$V(\phi)=\tfrac d2\log(2\pi e)+\frac1{N_yN_z}\sum_{i,j}\Big[\log p\big(G(Z_{0j};Y_i,\phi),Y_i\big)+\log h(Z_{0j};Y_i,\phi)\Big]$$

Both give $v(\phi)=\mathbb E[V(\phi)]$ and $\nabla v=\mathbb E[\nabla V]$ via the [[Reparameterization trick]].

> [!algorithm] Algorithm 1: amortization network training (source: file, p. 16, eq. 11)
> For $k=1..N_{iter}$: (a) draw $N_y$ synthetic datasets by sampling $\xi\sim p(\xi)$, solving the forward model, sampling $y$ from the likelihood; (b) draw $N_z$ base samples per dataset; (c) form $V(\phi_k)$ by eq. 9 or 10 and its gradient; (d) update
> $$\phi_{k+1}=\phi_k+\eta_k\nabla_\phi v_k(\phi_k)$$
> Converges to a local maximum under Robbins-Monro, $\sum\eta_k=\infty$, $\sum\eta_k^2<\infty$. In practice Adam ($\beta_1=0.9,\beta_2=0.999$) with step-decay schedule.

Note that training needs only the prior, forward model and likelihood: no MCMC samples and no posterior pairs. The forward model is used inside the loop, so the examples replace it with a neural surrogate where costly.

## Results

Ground truth: NUTS (Pyro), 3,300 samples, 300 burn-in, thinned by 3 to 1,000 samples (p. 18). Metrics (§3.1): Kolmogorov-Smirnov statistic per parameter against MCMC for $N_y=100$ datasets drawn from the data density, and the re-simulation error
$$E_{\text{re-sim}}=\mathbb E\,\mathbb E_{\Xi\sim q_{\lambda(Y;\phi)}}\|f(\Xi)-f(\Xi_{gt})\|^2,$$
estimated by eq. 12; it needs no MCMC.

| Problem | Guide | Setup (iterations, $N_y,N_z$) | $E_{\text{re-sim}}$ |
|---|---|---|---|
| EIT damage location: $y\in\mathbb R^{600}\to\xi\in\mathbb R^2$ (p. 20-21) | Gaussian | 8,000, (32, 5); nets 20-10 hidden; lr $10^{-2}$ | $1.06\times10^{-2}$ |
| 1D elliptic PDE conductivity: $y\in\mathbb R^9\to\xi\in\mathbb R^5$ (p. 23-24) | Gaussian | 35,000, (64, 5); nets 50-40-30-20 | $4.05\times10^{-2}$ |
| Inverse kinematics: $y\in\mathbb R^2\to\xi\in\mathbb R^4$ (p. 29-30) | Gaussian | 10,000, (32, 5) | $2.32\times10^{-2}$ |
| Inverse kinematics | Cond. flow, $K=15$ CCBs | 200,000, (64, 32); Adam + AMSGrad, lr $10^{-3}$ | $1.79\times10^{-2}$ |

- **EIT damage detection** (circular void of radius 0.1, centre in $[0.2,0.8]^2$, $\gamma=0.005$, forward model replaced by a residual-network surrogate trained on 3,721 FVM solves): posterior pairplots for three test observations match MCMC; KS statistics low (Fig. 10).
- **Elliptic PDE** (random sinusoidal log-conductivity with 5 standard-normal coefficients, $\gamma=0.015$, forward model a physics-informed energy-loss network, cf. [[PINN]]): MCMC posteriors are Gaussian and the Gaussian guide recovers them including parameter correlations "in almost agreement" (Figs. 14-17).
- **Inverse kinematics** (4-DoF arm with slider; non-Gaussian, multimodal posterior): the Gaussian guide finds a valid mode but not all configurations, giving high KS statistics (Fig. 19); the authors attribute this to the mode-seeking nature of KL minimisation. The conditional flow covers the arm configurations and has low, right-skewed KS statistics (Fig. 25), yet pairplots show it misses some modes, "probably" a local optimum (pp. 30, 41).
- Once trained, each posterior costs one network forward pass (abstract, §4). The paper reports no wall-clock comparison against MCMC or training cost. Wiki note: the up-front training cost (up to 200,000 iterations with an inner forward model) is what is "amortized"; no break-even count of test datasets is given.

## Limitations

As stated: amortization gap exists in practice and shrinks with network capacity, but the ideal flow depth and width are unknown (p. 30); Gaussian guides cannot represent non-Gaussian/multimodal posteriors; the flow architecture is harder to choose and training is slow (§4); Theorem 2 assumes no amortization gap and unstated smoothness; the likelihood assumes only Gaussian measurement noise, no model discrepancy (§2.1).

Wiki note (not in paper): Theorem 2 and the "equivalent to all VI problems" claim are local-optimum statements and say nothing about reaching the global optimum; examples are low dimensional (2 to 5 parameters), with surrogates standing in for expensive solvers.

## Connections

- Builds on [[Variational inverse problems (Tsilifis 2014)]] (ref. 41): same group, same Gaussian-likelihood inverse-problem framing and MCMC-as-truth protocol, but the Taylor/mixture machinery is replaced by neural guides and per-dataset optimisation by [[Amortized VI]].
- [[Amortized VI when and why (Margossian 2024)]] supplies the theory of when amortization gaps can close (for exchangeable latent models), and the semi-amortized remedy; the present paper's "no amortization gap" assumption in Theorem 2 corresponds to the existence of an ideal inference function.
- Uses surrogates (residual nets, PINN-style energy loss: [[PINN]]) in place of the forward model; compares conceptually to operator-learning approaches ([[Operator learning]], [[DeepONet]]).
- Complementary samplers: [[SGLD]]; flow/diffusion-style generative alternatives: [[Diffusion models]], [[Flow matching]] (Wiki note: not discussed in this paper).





%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Amortized VI when and why (Margossian 2024)]], [[Bayesian DenseED surrogate (Zhu 2018)]], [[VAE paper (Kingma 2014)]], [[Variational inverse problems (Tsilifis 2014)]], [[Wiener-Askey chaos (Xiu 2002)]]
%% refs:end %%

**Sources**: `Bayesian/Bilionis, Karumuri - Learning to solve Baysian inverse problems An Amortizeed Variational Inferece approach useing Gaussian and Flow guides.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Amortized VI]]
- [[Variational inference]]
- [[ELBO]]
- [[KL divergence]]
- [[Reparameterization trick]]
- [[Normalizing flows]]
- [[Bayesian inverse problems]]
- [[Variational inverse problems (Tsilifis 2014)]]
- [[Amortized VI when and why (Margossian 2024)]]
- [[PINN]]
- [[DeepONet]]
- [[Operator learning]]
- [[SGLD]]
- [[Diffusion models]]
- [[Flow matching]]
- Reproduced in the ME 697 book as the inverse-kinematics example (§3.4 of the paper): [[ME697 4.4 - Hierarchical Bayes]]. (source: `inverse/hbayes/04_amortized_vi.ipynb`)
