---
type: paper
area: bayesian
areas: [bayesian, stochastic]
source-ref: "Zhu, Zabaras 2018 (J. Comput. Phys.), Alg. 1, eqs. 11-17"
tags: [bayesian, operators, ml]
authors: ["[[Yinhao Zhu]]", "[[Nicholas Zabaras]]"]
year: 2018
venue: "Journal of Computational Physics (preprint submitted Jan 2018; arXiv:1801.06879v1)"
file: "papers/Bayesian/Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf"
---

# Bayesian DenseED Surrogates (Zhu 2018)

**Summary**: Surrogate modelling of stochastic PDEs is cast as image-to-image regression with a dense convolutional encoder-decoder (DenseED), made Bayesian with a Student-t weight prior and trained by [[SVGD]] using 20 particles. On Darcy flow with log-permeability input dimension up to 4225, it gives accurate means and calibrated predictive variances from as few as 32 to 1024 training runs.

**Authors**: Yinhao Zhu, Nicholas Zabaras (University of Notre Dame) · **Year**: 2018 · **File**: `papers/Bayesian/Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf`

---

## Problem

Uncertainty propagation for SPDE-governed systems needs many solves, but only ~100 simulations are affordable (p. 2). GP and generalised polynomial chaos surrogates do not scale to high stochastic input dimension, as arises from discretising random fields with short correlation length (p. 2). The classical remedy is a two-stage reduce-then-regress pipeline (for example [[Karhunen-Loève expansion]] followed by a GP), which separates the unsupervised reduction from the regression (p. 3).

The task: learn $y=f(x,\theta)$ from $D=\{x_i,y_i\}_{i=1}^N$ with $x\in\mathbb{R}^{d_x\times H\times W}$, $y\in\mathbb{R}^{d_y\times H\times W}$, with calibrated epistemic uncertainty, then propagate input uncertainty through the surrogate (pp. 5-6).

## Method

**Image-to-image regression.** The discretised input field and solution fields are treated as images with $d_x$, $d_y$ channels, so $\eta:\mathbb{R}^{d_x\times H\times W}\to\mathbb{R}^{d_y\times H\times W}$ (p. 6). Input and output share no underlying structure, unlike typical vision encoder-decoder tasks (p. 6).

**DenseED architecture** (pp. 7-10): DenseNet blocks (layer $l$ takes $[x_{l-1},\dots,x_0]$, growth rate $K$, $L$ layers per block), encoding layers (1x1 conv then stride-2 conv), decoding layers (1x1 conv then stride-2 transposed conv), no pooling, no encoder-decoder skip connections, no fully connected layers, a first conv k7s2p2. The selected net, DenseED-c16, has dense blocks (3, 6, 3), $K=16$, 19 conv layers, 241,164 parameters, code resolution 16x16 (Fig. 7, p. 24). It was chosen by architecture search and Hyperband under a 0.25M-parameter cap (App. A).

**Probabilistic model.** $y=f(x,w)+n$ (p. 12).

> [!definition] Weight prior and noise model
> $p(w|\alpha)=\mathcal{N}(w\,|\,0,\alpha^{-1}I)$, $p(\alpha)=\mathrm{Gamma}(\alpha\,|\,a_0,b_0)$, giving a Student-t marginal prior on $w$ (heavy tails, sparsity-promoting). Noise $n=\sigma\epsilon$ with precision $\beta=1/\sigma^2\sim\mathrm{Gamma}(a_1,b_1)$, $a_1=2$, $b_1=2\cdot10^{-6}$ (small nugget) (source: `Zhu ... .pdf`, §3.1-3.2, pp. 12-13). Experiments use homoscedastic output-wise Gaussian noise (p. 26). Non-Bayesian training with L2-regularised MSE equals MAP under an independent normal prior (p. 25).

> [!algorithm] SVGD (Algorithm 1)
> Variational family: smooth transforms $T(\theta)=\theta+\epsilon\phi(\theta)$ of particles $\{\theta^i\}_{i=1}^S$. The optimal direction in the unit ball of an RKHS is
> $$\phi^*(\theta)\propto\mathbb{E}_{\theta'\sim\mu}\big[\nabla_{\theta'}\log p(\theta')\,k(\theta,\theta')+\nabla_{\theta'}k(\theta,\theta')\big],$$
> and the update is
> $$\theta^i_{t+1}\leftarrow\theta^i_t+\epsilon_t\,\phi(\theta^i_t),\qquad
> \phi(\theta^i_t)=\tfrac1S\sum_{j=1}^S\Big[k(\theta^j_t,\theta^i_t)\nabla_{\theta^j_t}\log p(\theta^j_t)+\nabla_{\theta^j_t}k(\theta^j_t,\theta^i_t)\Big].$$
> The first term drives particles to high posterior density; the second is a repulsive force. With one particle it reduces to MAP. (source: pp. 15-16, Alg. 1; the extracted $\phi^*$ and the sum were garbled; the form shown is the standard SVGD statement the text describes.)

Here $\theta=\{w,\beta\}$, $\tilde p(\theta|D)=\prod_i p(y_i|\theta,x_i)p_0(\theta)$, and the target is $\arg\min_q \mathrm{KL}(q\|p(\theta|D))$ (p. 14), with $-\frac{d}{d\epsilon}\mathrm{KL}(T\mu\|\nu_p)|_{\epsilon=0}=\mathbb{E}_\mu[\mathcal{T}_p\phi]$ and Stein operator $\mathcal{T}_p\phi=(\nabla\log p)\cdot\phi+\nabla\cdot\phi$ (p. 15).

**Implementation**: $S=20$ DenseED networks and 20 scalar $\beta$s, one PyTorch module each. Each step: backprop the log joint, vectorise parameters and gradients, form the kernel matrix, compute $\phi$, write $\phi$ back as the gradient and step with Adam (pp. 16-17). RBF kernel $k=\exp(-\|x-x'\|^2/h)$ with median heuristic $h=H^2/\log S$ (p. 26). Mini-batch (16) likelihood approximation, 300 epochs, lr 0.002 for $w$ and 0.01 for $\beta$ (p. 28).

> [!definition] Predictive moments from particles
> $$\mathbb{E}[y^*|x^*,D]\approx\tfrac1S\sum_i f(x^*,w_i),$$
> $$\mathrm{Cov}(y^*|x^*,D)=\mathbb{E}_\beta[\beta^{-1}]I+\mathrm{Cov}_w(f(x^*,w))\approx\tfrac1S\sum_i\big[\beta_i^{-1}I+f f^\top\big]-\bar f\bar f^\top,$$
> via the law of total variance. For propagated uncertainty, with $x_j\sim p(x)$: $\mathbb{E}[y|\theta]\approx\frac1M\sum_j f(x_j,w)$ and $\mathrm{Var}(y|\theta)=\beta^{-1}\mathbf 1+\frac1M\sum_j f^2(x_j,w)-(\frac1M\sum_j f(x_j,w))^2$ (source: eqs. 11-17, pp. 17-19). The statistics $\mathbb{E}_\theta[\mathbb{E}[y|\theta]]$, $\mathrm{Var}_\theta(\cdot)$ are then taken over particles. This is a form of [[Bayesian model averaging]].

**Benchmark.** 2D single-phase Darcy flow on $[0,1]^2$, 65x65 grid, $u=-K\nabla p$, $\nabla\cdot u=f$, with a source and sink at opposite corners. $K=\exp(G)$, $G\sim\mathcal{N}(m,k)$ with $k(s,s')=\exp(-\|s-s'\|_2/l)$, $l=0.1$ (eqs. 18-21, pp. 19-20). Three datasets with $q$ [[Karhunen-Loève expansion]] terms: KLE50, KLE500, KLE4225 (the last has no reduction, intrinsic dimension 4225). The model never sees the KLE coefficients. Training inputs sampled by Latin hypercube; 500 validation, 500 test, 10,000 uncertainty-propagation inputs (p. 22). Solver: FEniCS mixed FEM (p. 21).

**Metrics** (p. 23): $R^2$, RMSE, mean negative log-probability (MNLP), propagated statistics against Monte Carlo, and reliability diagrams.

## Results

- **Non-Bayesian DenseED-c16** (Table A.2, p. 43; test $R^2$):

| N train | KLE50 | KLE500 | KLE4225 |
|---|---|---|---|
| 32 | 0.718 | 0.551 | 0.280 |
| 64 | 0.883 | 0.817 | 0.662 |
| 128 | 0.947 | 0.913 | 0.829 |
| 256 | 0.970 | 0.954 | 0.927 |
| 512 | n/a | 0.976 | 0.963 |

  Error falls with more data and with lower intrinsic dimension; $R^2>0.9$ is reached with reasonably small training sets across 50 to 4225 dimensions (p. 26). One architecture works for all three datasets; DenseED-c8 fails on KLE4225 (code too small) and DenseED-c32 fails on KLE50 (App. A, p. 42).
- **No overfitting with over-parameterisation**: parameters 37,892 to 805,204 with 256 training points, train error does not drop and test error does not rise (App. B, p. 45).
- **Bayesian vs non-Bayesian** (Fig. 13, p. 29; values read off the plot, approximate): Bayesian is better at every size, with the largest gain at small N, for example KLE4225 at 128 points about 0.91 vs 0.85 and KLE50 at 32 points about 0.84 vs 0.78. At the largest sizes the gap closes (KLE4225 at 1024 about 0.987 vs 0.983). The text says "improves the $R^2$-score significantly" (p. 28). MNLP falls with N (Fig. 14).
- **Uncertainty**: predictive std shrinks as N grows (Figs. 15-17). Velocity is predicted better than pressure.
- **Uncertainty propagation**: with 10,000 inputs, output mean and variance match Monte Carlo, closer with more data (Figs. 18-22).
- **Calibration** (Fig. 23, p. 33): close to the diagonal, best at 128 points for all three datasets; over-confident for small N and increasingly conservative for large N.
- **Particles**: train and test error stabilise by 20 particles (Fig. 25, p. 39). Training takes about 2000 to 7000 s for 300 epochs with 32 to 512 points on one GTX 1080 Ti (p. 28). Convergence takes about 50 to 75 epochs for KLE50/500, longer for KLE4225 (Fig. 24).

Note: the abstract claims state-of-the-art versus other BNN methods, GPs and ensembles; the body of this arXiv v1 compares only against the non-Bayesian DenseED, so that claim is not backed by a table here. Wiki note.

## Limitations

As stated (pp. 39-40):
- Inference over millions of weights from hundreds of data points is "genuinely difficult"; other weight priors and newer VI methods are future work.
- No physics is used: no governing equations or constraints between the output fields.
- Pressure is predicted worse than velocity; suggested fixes are encoder-decoder skip connections, a conditional-GAN loss, and group convolution in the last layer.
- Training cost is high (up to about 7000 s).
- Input realisations for testing and propagation are assumed available (a generative model is out of scope, Remark 1, p. 7); the Darcy data are synthetic with a known GRF.

Wiki note: 20 particles is a small ensemble for a posterior over about 240k weights; the validation is by reliability diagrams on one PDE.

## Connections

- Builds on [[SVGD]] (Liu-Wang) and DenseNet; uses [[Karhunen-Loève expansion]] only to generate datasets, not in the model.
- Alternative to the [[Gaussian process]]-after-KLE-reduction pipeline described in the paper's introduction.
- Weight prior: Student-t via Gamma precision, one of the hierarchical-hyperprior priors reviewed in [[Priors in Bayesian deep learning (Fortuin 2022)]] (Sec. 4.1). The conclusion explicitly calls for exploring other priors.
- Particles act as a deep ensemble with a repulsive term, the SVGD-as-Bayesian-ensemble view in [[Priors in Bayesian deep learning (Fortuin 2022)]] (Sec. 4.3).
- Related operator-style surrogates: [[Operator learning]] maps function to function without a fixed grid, whereas this is grid-based image regression (Wiki note).
- Conclusion points to physics information as the next step, which connects to [[Physics-informed prior]] (Wiki note).
- Contrast with [[SDE-BNN (Xu 2022)]]: parametric stochastic-process posterior vs non-parametric particle posterior.
- Wiki note: a GP surrogate is the classical Bayesian alternative to a neural surrogate with uncertainty; see [[Gaussian processes and kernel methods (Kanagawa 2018)]] for the GP and kernel-ridge picture and [[Multi-fidelity GP for tissue expansion (Lee 2020)]] for a GP surrogate in a physical-simulation setting.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[AlexNet (Krizhevsky 2012)]], [[GAN paper (Goodfellow 2014)]], [[U-Net paper (Ronneberger 2015)]], [[VAE paper (Kingma 2014)]], [[Variational dropout (Kingma 2015)]], [[Wiener-Askey chaos (Xiu 2002)]]
**Cited by in this wiki**: [[Amortized VI for inverse problems (Karumuri 2024)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[FNO (Li 2021)]], [[NIF (Pan 2023)]], [[Neural operator (Kovachki 2022)]], [[PINNs (Raissi 2019)]]
**Software cited**: [[software#FEniCS|FEniCS]], [[software#Theano|Theano]]
%% refs:end %%

**Sources**: `papers/Bayesian/Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SVGD]]
- [[Bayesian neural networks]]
- [[Variational inference]]
- [[KL divergence]]
- [[Karhunen-Loève expansion]]
- [[Gaussian process]]
- [[Bayesian model averaging]]
- [[Operator learning]]
- [[Physics-informed prior]]
- densenet encoder decoder
- [[Priors in Bayesian deep learning (Fortuin 2022)]]
- [[SDE-BNN (Xu 2022)]]
- [[Kernel methods]], [[Gaussian process]], [[Surrogate model]].
