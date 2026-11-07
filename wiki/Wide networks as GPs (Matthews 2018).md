---
type: paper
area: gp
areas: [gp, bayesian, ml]
source-ref: "Matthews, Rowland, Hron, Turner, Ghahramani 2018, arXiv:1804.11271v2, eqs. 1-9, Lemma 2, Thm 4, Cor. 5"
tags: [gp, bayesian, ml]
authors: ["[[Alexander G. de G. Matthews]]", "[[Mark Rowland]]", "[[Jiri Hron]]", "[[Richard E. Turner]]", "[[Zoubin Ghahramani]]"]
year: 2018
venue: "ICLR 2018 (this PDF: extended arXiv v2)"
file: "papers/Guassian Processes/Matthews et al - Gaussian Process Behaviour in Wide Deep Neural Networks.pdf"
---

# Wide networks as GPs (Matthews 2018)

**Summary**: Proves that a randomly initialized, fully connected network with any fixed number of hidden layers and independent Gaussian weights converges in distribution to a Gaussian process as all hidden widths grow together, extending Neal's one-hidden-layer result. The proof uses exchangeability and a central limit theorem for exchangeable arrays. Experiments measure the distance to the GP by maximum mean discrepancy (MMD) and compare finite Bayesian networks (gold-standard MCMC) with exact GP inference: close on five of six datasets.

**Authors**: Alexander G. de G. Matthews, Mark Rowland, Jiri Hron, Richard E. Turner, Zoubin Ghahramani · **Year**: 2018 · **File**: `papers/Guassian Processes/Matthews et al - Gaussian Process Behaviour in Wide Deep Neural Networks.pdf`

---

Page numbers are PDF pages (36 pages; pp. 26-36 are references and appendices, which I only skimmed).

## Problem

Neal (1996) showed that one-hidden-layer random networks tend to a GP, but the type of convergence was left loose and no rigorous result existed for several hidden layers. Cho and Saul's recursive kernel reached the right recursion by an argument the authors call erroneous (composing feature maps is a type error, p. 9). Lee et al. (2018) argued for the GP limit by taking the layer widths to infinity sequentially; this paper treats simultaneous growth (pp. 3-4).

## Method

**Network** (eqs. 1-6, p. 5). Activation $f^{(\mu)}$, activity $g^{(\mu)}=\phi(f^{(\mu)})$, input $x\in\mathbb R^M$:
$$f_i^{(1)}(x)=\sum_jw^{(1)}_{ij}x_j+b_i^{(1)},\qquad
f_i^{(\mu+1)}(x)=\sum_{j=1}^{H_\mu}w^{(\mu+1)}_{ij}g^{(\mu)}_j(x)+b_i^{(\mu+1)},$$
with $w\sim N(0,C_w^{(\mu)})$, $b\sim N(0,C_b^{(\mu)})$ iid and Neal's scaling
$$C_w^{(\mu)}=\hat C_w^{(\mu)}/H_{\mu-1},\qquad\mu\ge2.$$

**One hidden layer.** $F^{(2)}$ is a sum of $H_1$ iid vectors given the inputs, so the multivariate CLT applies; the limit is a zero-mean GP with covariance (eq. 9, p. 6)
$$\mathbb E[f_i^{(2)}(x)f_j^{(2)}(x')]=\delta_{ij}\Big[\hat C_w^{(2)}\,\mathbb E_{\epsilon,\gamma}\big[\phi(\epsilon^\top x+\gamma)\phi(\epsilon^\top x'+\gamma)\big]+C_b^{(2)}\Big].$$
Consistency under marginalization gives a GP by the Kolmogorov extension theorem.

**Mode of convergence** (§2.2, pp. 6-7). Convergence is in distribution, with respect to the metric $\rho(v,v')=\sum_i2^{-i}\min(1,|v_i-v_i'|)$ on $\mathbb R^{\mathbb N}$ for a countable input set; then it suffices to prove convergence of every finite-dimensional marginal. Properties needing uncountably many indices (continuity, differentiability) are not covered.

> [!definition] Linear envelope property
> A nonlinearity $\phi$ obeys it if $|\phi(u)|\le c+m|u|$ for some $c,m\ge0$. This holds for sigmoid, ReLU, ELU and SeLU, and stops $\phi$ from creating heavy tails; it is the only assumption on $\phi$ (besides continuity).
>
> (source: Def. 1, p. 7)

> [!theorem] Lemma 2 (normal recursion, attributed to Hazan and Jaakkola)
> If the layer-$(\mu-1)$ activations are Gaussian with covariance $\delta_{ij}K(x,x')$, then as $H\to\infty$ layer $\mu$ is Gaussian with
> $$\mathbb E[f^{(\mu)}_i(x)f^{(\mu)}_j(x')]=\delta_{ij}\Big[\hat C_w^{(\mu)}\,\mathbb E_{(\epsilon_1,\epsilon_2)\sim N(0,K)}[\phi(\epsilon_1)\phi(\epsilon_2)]+C_b^{(\mu)}\Big].$$
>
> (source: eqs. 12-15, p. 8)

The lemma alone is not enough, because for finite $H$ the layer inputs are only approximately Gaussian, and the rate of that approximation could matter downstream (p. 8).

> [!theorem] Theorem 4 (deep wide limit)
> For a random network with continuous $\phi$ obeying the linear envelope property, every set of strictly increasing width functions $h_\mu(n)$, and every countable input set, the network output converges in distribution to a GP with mean zero and covariance given by the recursion of Lemma 2. Corollary 5: the special case $H_\mu=H$ for all layers, $H\to\infty$.
>
> (source: pp. 8-9)

The layers may grow at different rates (e.g. $h_\mu(n)=n^\mu$).

**Closed-form kernels** (§3, p. 9). For $\phi(u)=\Theta(u)u^r$, $r=0,1,2,3$, Cho and Saul's closed forms solve the recursion; $r=1$ is ReLU and is used in all experiments. See [[Neural network Gaussian process]].

### Proof structure (§6, pp. 19-23)

1. Cramér-Wold plus the metric $\rho$ reduce the problem to real-valued finite linear projections $T^{(\mu)}(L,\alpha)$ (Lemma 6).
2. Write $T^{(\mu)}=h_{\mu-1}^{-1/2}\sum_j\gamma_j^{(\mu)}$; the summands $\gamma_j$ are exchangeable for fixed $n$ (Lemma 8, via de Finetti: iid given the previous layer's activities).
3. A CLT for exchangeable sequences (Blum et al. 1958, Thm 9; adapted as Lemma 10) needs: zero correlation of two summands, $\mathbb E[X_1^2X_2^2]\to\sigma_*^4$, and $\mathbb E|X_1|^3=o(\sqrt{h(n)})$.
4. The limiting variance is $\alpha^\top K\alpha$ (Lemma 11); the moment conditions are shown by induction through the layers, starting at the input (Lemma 12; details in Appendix B, not read).

## Results

- **MMD vs width** (§4, Fig. 2, pp. 10-12): 10 standard-normal inputs in 4 dimensions, 2000 networks vs 2000 GP samples, $\hat C_w=0.8$, $C_b=0.2$, RBF kernel for the MMD (lengthscale 1/2), 20 repeats. Squared MMD falls as width grows for 1, 2, 3 hidden layers; convergence is slower for more layers; the "largest first", "largest last" and identity width functions behave consistently with the theory (which predicts independence of the width function). A calibration line gives the MMD between two RBF GPs with lengthscales $\ell$ and $2\ell$, $\ell=\sqrt8$.
- **Posterior comparison** (§5, pp. 11-19): 3 hidden layers of 50 ReLU units, HMC interleaved with elliptical slice sampling vs exact GP inference. Close agreement on small 1D regression, small XOR (mean absolute difference between posterior mean grids 0.064; annealed-importance-sampling marginal likelihood within one nat), a random-network test, the Snelson data (100 points) and smooth XOR (100 points). On the yacht dataset (6 inputs, 100 training points) the two disagree and the finite network has clearly better log-likelihood. For Snelson the MCMC took 44 hours on ten cores while the GP took seconds.

## Limitations

Stated by the authors:
- Independent Gaussian weights only; Blundell et al. (up to 1200 units, scale-mixture priors) would need a non-Gaussian extension (p. 13).
- Only countable index sets; continuity and differentiability are not covered (p. 7).
- The empirical comparison is limited to small, low-dimensional problems because the gold-standard MCMC is expensive, and the yacht mismatch may reflect higher dimension (pp. 11, 18). They predict larger differences for much deeper networks (p. 18).
- Desirability (§7, pp. 23-24): a GP with fixed kernel has a flat representation and does not learn hierarchical features, as MacKay and Neal noted. Ways to avoid the GP behaviour: narrow layers as in deep GPs, infinite-variance weights (alpha-stable limits), or coupling weights.

## Connections

- The GP limit at initialization is Prop. 1 of [[NTK (Jacot 2018)]]; Jacot adds the NTK that describes training, using the same $\Sigma^{(L)}$ recursion (with $\sigma_w^2=1$ and a $\beta^2$ bias term).
- The limit is the "NNGP" prior used in [[Priors in Bayesian deep learning (Fortuin 2022)]]; see [[Neural network Gaussian process]], [[Bayesian neural networks]] and [[Gaussian process]].
- The practical recommendation, that Bayesian deep learning papers routinely compare against the matching GP, bears on every [[Bayesian neural networks]] result.

%% refs:start %%
**Cited by in this wiki**: [[Neural operator (Kovachki 2022)]], [[Priors in Bayesian deep learning (Fortuin 2022)]], [[When and why PINNs fail (Wang 2022)]]
**Software cited**: [[software#GPflow|GPflow]]
%% refs:end %%

**Sources**: `papers/Guassian Processes/Matthews et al - Gaussian Process Behaviour in Wide Deep Neural Networks.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Neural network Gaussian process]] · [[Gaussian process]] · [[Bayesian neural networks]] · [[Kernel methods]]
- [[NTK (Jacot 2018)]] · [[Neural tangent kernel]] · [[Priors in Bayesian deep learning (Fortuin 2022)]] · [[Hamiltonian Monte Carlo]]
- [[Weight initialization]]
