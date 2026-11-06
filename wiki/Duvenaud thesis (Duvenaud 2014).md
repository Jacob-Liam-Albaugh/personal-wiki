---
type: paper
area: gp
areas: [gp, ml]
source-ref: "Duvenaud 2014, PhD thesis, Univ. of Cambridge, chs. 2-8 (page numbers are the thesis's printed pages; PDF page = printed + 13)"
tags: [gp, bayesian, ml]
authors: ["[[David Duvenaud]]"]
year: 2014
venue: "PhD thesis, University of Cambridge, June 2014"
file: "Guassian Processes/Duvenaud - Thesis - Automatic Model Construction with Gaussian Processes.pdf"
---

# Duvenaud thesis (Duvenaud 2014)

**Summary**: Gaussian process models whose structure is chosen by writing sums and products of kernels. The thesis shows what each kernel and each combination means, automates the search over kernel expressions and describes the result in English, then studies deep GPs, additive GPs (and their link to dropout), and a GP-warped clustering model.

**Authors**: David Duvenaud · **Year**: 2014 · **File**: `Guassian Processes/Duvenaud - Thesis - Automatic Model Construction with Gaussian Processes.pdf`

---

## Ch. 1 Introduction (pp. 1-7)

A GP is a distribution over functions whose finite marginals are jointly Gaussian; it is set by a mean $\mu(x)$ and a covariance function (kernel) $k(x,x')$ (eqs. 1.1-1.2, p. 2). See [[Gaussian process]]. The kernel fixes which functions are likely a priori and so how the model generalises (p. 8). Model comparison uses the marginal likelihood.

## Ch. 2 Expressing structure with kernels (pp. 8-30)

The core tutorial; the wiki page is [[Kernel composition]].

- Basic kernels: squared exponential (SE, local variation, infinitely differentiable), periodic (Per), linear (Lin) (Fig. 2.1, p. 9). Stationary versus non-stationary (p. 10).
- Products: product of kernels is a kernel; Lin x Lin gives quadratic functions, SE x Per gives locally periodic, Lin x Per gives growing amplitude (§2.3.2, p. 11). A product of SE kernels per input is SE-ARD (eq. 2.4, p. 12).
- Sums: independent GPs add, $f_a+f_b\sim GP(\mu_a+\mu_b,\,k_a+k_b)$ (eq. 2.7, p. 14). Additive kernels in separate inputs give additive functions and can extrapolate where a product kernel reverts to the mean (Figs. 2.5-2.6, pp. 15-16). Concrete-strength example: 8 one-dimensional components, two switched off by marginal-likelihood ARD (§2.4.4, p. 17). Posterior of each component derived in §2.4.5 (p. 18).
- Changepoints: $CP(k_1,k_2)=\sigma k_1\sigma + \bar\sigma k_2\bar\sigma$ with a sigmoid (eq. 2.19, p. 20). Known multiplier: $a(x)g(x)\sim GP(0,\,a\,k\,a)$ (eq. 2.21).
- Features (§2.6, pp. 21-22): by Mercer, $k(x,x')=h(x)^\top h(x')$. Sum of kernels concatenates features; product takes all pairs of features.
- Symmetries (§2.7, pp. 22-26): to make $f(x)=f(g(x))$ for a group $G$, three recipes: sum over the orbit, project onto a fundamental domain, multiply over the orbit (eqs. 2.36-2.39). Periodic kernel $\mathrm{Per}=SE(\sin x,\sin x')\times SE(\cos x,\cos x')$ (eq. 2.41, MacKay 1998). The sum-over-orbit recipe doubles marginal variance near the symmetry line; the product recipe can give zero variance in regions (pp. 23-25).
- Topology (§2.8, pp. 26-29): a GP prior on maps from $\mathbb R^2$ to $\mathbb R^3$ with periodic kernels gives cylinders ($SE\times Per$), tori ($Per\times Per$) and Mobius strips (Figs. 2.11-2.12).
- Categorical inputs by one-of-k encoding (§2.9); building a kernel in practice, GPML toolbox (§2.11, p. 30).

## Ch. 3 Automatic model construction (pp. 31-47)

> [!algorithm] ABCD: automatic Bayesian covariance discovery
> 1. Language: all sums and products of base kernels (C, Lin, SE, RQ, Per, sigma, WN).
> 2. Search: greedy over kernel expressions with operators replace $k\to k'$, add $k\to k+k'$, multiply $k\to k\times k'$, plus changepoint operators (Fig. 3.2, p. 35; list in appendix C).
> 3. Score each expression by BIC: $\log p(D|M)-\tfrac12|M|\log N$ with optimised parameters (eq. 3.3, p. 37).
> 4. Report the best expression, decomposed into additive components with their posteriors.
>
> (source: pp. 32-38)

Many standard regression models are special cases (Table 3.1, p. 34). Mauna Loa CO2 comes out as long-term trend + yearly periodic + medium-term deviation + noise (Lin x SE + SE x (Per + RQ) + WN, Fig. 3.4, p. 39). Extrapolation test on 13 time series (train on first 90 percent, standardised RMSE): ABCD-accuracy usually beats ABCD-interpretability and the baselines (Fig. 3.6, p. 45). On synthetic data, ABCD recovers the generating structure and backs off to simpler structure as noise rises (§3.8.4, p. 46).

## Ch. 4 Automatic model description (pp. 48-58)

Any kernel expression simplifies to a sum of products; each product is described by one noun kernel plus modifiers: SE removes long-range correlation ("varies smoothly"), Lin makes the standard deviation grow linearly, sigma gives changepoints (pp. 49-50). Output is a report with plots and text (worked example appendix D). Limits: the description rules cover a restricted base set, and uncertainty over structures is not reported (§4.4, p. 58).

## Ch. 5 Deep Gaussian processes (pp. 59-80)

- A deep GP is a composition $f^{(L)}(\dots f^{(1)}(x))$ of GP-distributed functions (eq. 5.1, p. 60). One hidden layer of infinitely many fixed features with iid weights is a GP, by the central limit theorem (Neal 1995; eqs. 5.4-5.5, p. 61). Compare [[Random features model]].
- Pathology (§5.2-5.3, pp. 64-69): the Jacobian of a deep GP with product kernel is a product of independent Gaussian matrices (Thm 5.2.3, p. 67), so with depth one singular value dominates and the representation varies in only one direction (Fig. 5.5, p. 69).
- Fix: connect the input to every layer (§5.4, pp. 69-74).
- Deep kernels: composing fixed feature maps; periodic kernel is a 2-layer deep kernel (§5.5, p. 75). Infinite SE composition converges to the constant kernel; input-connected deep kernels avoid it (§5.5.1, p. 76).
- Stated finding: the spectrum stayed flat for hundreds of layers when hidden dimension exceeded 100, so the pathology is mostly a thin-layer effect (p. 69).

## Ch. 6 Additive Gaussian processes (pp. 81-95)

- Order-$n$ additive kernel: a sum over all $n$-subsets of products of one-dimensional kernels,
$$k_{add_n}(x,x')=\sigma_n^2\sum_{i_1<\dots<i_n}\ \prod_{d=1}^{n}k_{i_d}(x_{i_d},x'_{i_d}).$$
The full model is a weighted sum over orders; evaluated in $O(D)$ per order via Newton-Girard identities for elementary symmetric polynomials (eq. 6.14, p. 85).
- Additive kernels are non-local and can extrapolate; SE, RQ and Matern are local, depend only on scaled distance (§6.3, p. 86).
- Dropout: on infinitely wide hidden layers it has no effect; dropout on the $D$ inputs of a product kernel gives a mixture of $2^D$ GPs, i.e. additive covariance (§6.4, pp. 87-88).
- Results: mean over 10 splits. The additive GP and kernel search beat SE-ARD on most regression sets, e.g. concrete MSE 0.089 (additive) and 0.087 (search) against 0.157 (SE) (Table 6.4, p. 94). Variance often concentrates on one order of interaction (Table 6.1, p. 84).

## Ch. 7 Warped mixture models (pp. 96-110)

GP latent variable model (GP-LVM): latent points through GP-drawn warp give nonparametric densities (§7.1). The infinite warped mixture model (iWMM) puts a Dirichlet-process Gaussian mixture in the latent space, warped by a GP, giving clusters of arbitrary shape; it generalises both GP-LVM and the infinite Gaussian mixture (p. 99). Inference by MCMC over latents, assignments and kernel parameters (§7.3; appendix E). Compared against KDE, iGMM and GP-LVM on four synthetic and four real sets: iWMM usually has higher test likelihood than KDE and iGMM, GP-LVM competitive (Table 7.3, p. 108). Related: [[Markov chain Monte Carlo]].

## Ch. 8 Discussion (pp. 111-114)

Structured kernel models versus unstructured deep GPs: optimisation difficulty, long-range extrapolation, interpretability (§8.2, pp. 112-113). Top-down versus bottom-up routes to automating model building (§8.3). Appendices: Gaussian conditionals (A), kernel definitions (B), search operators (C), example report (D), iWMM inference (E).

## Connections

- Wiki note: for surrogate building ([[Surrogate model]]) this is the toolkit for choosing a kernel by structure; [[Multi-fidelity GP for tissue expansion (Lee 2020)]] uses additive-style composition of kernels across fidelity levels (see [[Multi-fidelity Gaussian process]]).
- Wiki note: additive structure and Sobol-type decompositions look alike: an order-$n$ term is a main effect (n=1) or interaction. Compare [[Sobol indices]]. **[unverified]** link, not drawn in the thesis.
- Kernel versus RKHS theory: [[Gaussian processes and kernel methods (Kanagawa 2018)]], [[RKHS]], [[Kernel methods]].
- Eigenfunction view of the same kernels: [[Reduced-rank GPs (Greengard 2022)]], [[Karhunen-Loève expansion]].
- Symmetric kernels: compare [[Equivariance]].

**Sources**: `Guassian Processes/Duvenaud - Thesis - Automatic Model Construction with Gaussian Processes.pdf` (read contents, chs. 1-3 and 5-8 in the main passages, ch. 4 first and last sections; appendices B-E not read in detail).
**Last updated**: 2026-11-06

---

## Related pages
- [[Gaussian process]] · [[Kernel composition]] · [[Kernel methods]] · [[RKHS]] · [[Random features model]]
- [[Karhunen-Loève expansion]] · [[Surrogate model]] · [[Multi-fidelity Gaussian process]] · [[Equivariance]] · [[Markov chain Monte Carlo]]
- [[Gaussian processes and kernel methods (Kanagawa 2018)]] · [[Reduced-rank GPs (Greengard 2022)]] · [[Multi-fidelity GP for tissue expansion (Lee 2020)]]
