---
type: paper
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Zhang, Wilson, De Sa 2022, ICML (PMLR 162), Alg. 1-2, Thm. 1-3"
tags: [sampling, mcmc]
authors: ["[[Ruqi Zhang]]", "[[Andrew Gordon Wilson]]", "[[Christopher De Sa]]"]
year: 2022
venue: "ICML (PMLR 162)"
file: "IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf"
---

# Low-Precision Stochastic Gradient Langevin Dynamics (Zhang 2022)

**Summary**: Studies [[SGLD]] when weights and gradients are stored in few bits. With a full-precision weight buffer, a 2-Wasserstein bound shows the quantization bias enters as $O(\Delta_W^2)$ for SGLD versus $O(\Delta_W)$ for SGD. With a low-precision buffer, naive SGLD gets the variance wrong and diverges as the step size shrinks; a variance-corrected quantizer $Q_{vc}$ fixes this. Experiments on MNIST, CIFAR, IMDB and ImageNet use simulated 8-bit arithmetic.

**Authors**: Ruqi Zhang, Andrew Gordon Wilson, Christopher De Sa · **Year**: 2022 (ICML, PMLR 162) · **File**: `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`

Not a Bilionis-lab paper (no `lab` tag). Extraction note: several formulas (Theorem 1-3 bounds, Eq. 5) were read from the text layer, which is partially garbled for fractions and square roots; the forms below follow the proofs in Appendix B-D where they could be cross-checked, and a few terms are marked **[unverified]**.

---

## Problem

Low-precision training is standard for optimization (8-bit gives about 4x latency and memory savings, p. 1) but low-precision sampling was unexplored. SG-MCMC is argued to be well suited because it explores weight space rather than converging to a point, already injects noise, and averages predictions over an ensemble ([[Bayesian model averaging]]) (p. 1). Questions: does SGLD still converge to $\pi$ under quantization, and what happens when even the weight accumulator is low precision?

Setup (p. 2): posterior $p(\theta|D)\propto\exp(-U(\theta))$, $U(\theta)=-\sum_{x\in D}\log p(x|\theta)-\log p(\theta)$, unbiased stochastic gradient $\tilde\nabla U$.

## Method

> [!definition] SGLD update
> $$\theta_{k+1}=\theta_k-\alpha\,\tilde\nabla U(\theta_k)+\sqrt{2\alpha}\,\xi_{k+1},\quad \xi\sim\mathcal N(0,I).$$
>
> (source: Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf, eq. 1, p. 2). Same as [[SGLD (Welling 2011)]] with the step-size/noise scaling $\alpha$, $2\alpha$ (the original writes $\epsilon/2$, $\epsilon$; this page uses $\alpha$ as the paper does).

> [!definition] Fixed-point numbers and quantizers
> $W$ total bits, $F$ fractional bits, quantization gap $\Delta=2^{-F}$, range $[l,u]$ with $l=-2^{W-F-1}$, $u=2^{W-F-1}-2^{-F}$. Deterministic rounding $Q_d$ goes to the nearest representable value. Stochastic rounding $Q_s$ rounds up with probability $\theta/\Delta-\lfloor\theta/\Delta\rfloor$ and down otherwise, so $\mathbb E[Q_s(\theta)]=\theta$.
>
> (source: ibid., §3.2, p. 3). Block floating point, used for the deep nets, shares an exponent per block; the gap is recomputed each step (App. G, eq. 7, p. 19).

Two ways to apply the update (p. 3-4). $Q_W$, $Q_G$ are the weight and gradient quantizers with gaps $\Delta_W$, $\Delta_G$.

> [!definition] Full- vs low-precision gradient accumulators
> SGLDLP-F (full-precision buffer, weights quantized only for the forward/backward pass):
> $$\theta_{k+1}=\theta_k-\alpha\,Q_G\big(\tilde\nabla U(Q_W(\theta_k))\big)+\sqrt{2\alpha}\,\xi_{k+1}\quad(3)$$
> Naive SGLDLP-L (weights always low precision):
> $$\theta_{k+1}=Q_W\Big(\theta_k-\alpha\,Q_G\big(\tilde\nabla U(\theta_k)\big)+\sqrt{2\alpha}\,\xi_{k+1}\Big)\quad(4)$$
> The SGD analogues are SGDLP-F and SGDLP-L, eq. 2 (p. 3).
>
> (source: ibid., eq. 2-4, pp. 3-4)

Assumptions (p. 4): $U$ is $m$-strongly convex, $M$-smooth, with $\Psi$-Lipschitz Hessian, and $\mathbb E\|\tilde\nabla U-\nabla U\|_2^2\le\kappa^2$; constant step size; stochastic rounding.

> [!theorem] Theorem 1: SGLDLP-F
> For $\alpha\le2/(m+M)$, with $\pi$ the target and $\mu_K$ the law after $K$ steps,
> $$W_2(\mu_K,\pi)\le(1-\alpha m)^K W_2(\mu_0,\pi)+1.65\frac Mm(\alpha d)^{1/2}$$
> $$\qquad+\min\Big(\frac{\Psi\Delta_W^2 d}{4m},\ \frac{M\Delta_W\sqrt d}{2m}\Big)$$
> $$\qquad+\sqrt{\frac{(\Delta_G^2+M^2\Delta_W^2)\alpha d+4\alpha\kappa^2}{4m}}.$$
>
> (source: ibid., Thm. 1, p. 4; proof App. B, pp. 12-14, via Thm. 4 of Dalalyan & Karagulyan 2019 with gradient-noise bias $\delta$ and variance $\sigma^2$.) The $\min(\cdot)$ is the accuracy floor as $K\to\infty$, $\alpha\to0$. With $\Delta_W=0$ it reduces to the Dalalyan-Karagulyan bound (p. 4). For quadratic $U$ ($\Psi=0$) the floor vanishes. See [[Wasserstein distance]].

Wiki note: the proof shows the floor arises because $\|\mathbb E[\zeta_k|\theta_k]\|\le\min(\Psi\Delta_W^2d/4,\ M\Delta_W\sqrt d/2)$. The $\Psi$ branch uses that the first-order Hessian term vanishes in expectation under unbiased rounding, hence the quadratic dependence on $\Delta_W$.

SGD comparison (p. 4, App. E, p. 18-19): the SGD bound is $O(\Delta_W)$ in distance to the optimum (Yang et al. 2019) against $O(\Delta_W^2)$ here, so "asymptotically, SGLD only needs half the number of bits" (p. 4). The comparison treats point masses and $W_2\le\mathbb E\|\bar\theta_K-\theta^*\|_2$; the footnote on p. 4 notes the SGD bound is stated for the squared norm so a square root was taken.

> [!theorem] Theorem 2: naive SGLDLP-L
> Under the same assumptions,
> $$W_2(\mu_K,\pi)\le(1-\alpha m)^KW_2(\mu_0,\pi)+1.65\frac Mm(\alpha d)^{1/2}+\min\Big(\frac{\Psi\Delta_W^2d}{4m},\frac{M\Delta_W\sqrt d}{2m}\Big)$$
> $$\qquad+A+\big((1-\alpha m)^K+1\big)\frac{\Delta_W\sqrt d}{2},$$
> $$A=\sqrt{\frac{(\alpha\Delta_G^2+\alpha^{-1}\Delta_W^2)d+4\alpha\kappa^2}{4m}}.$$
>
> (source: ibid., Thm. 2, p. 4; proof App. C). The $\alpha^{-1}\Delta_W^2$ inside $A$ grows as $\alpha\to0$, so the bound (and, empirically, the error) gets worse for small step sizes.

Diagnosis (§4.3, p. 5): with unbiased stochastic rounding the mean of $\theta_{k+1,i}$ is right but the variance is not. Ignoring gradient noise and $Q_G$,
$$\mathrm{Var}[\theta_{k+1,i}]=\tfrac{\Delta_W^2}{4}\chi_{k+1,i}+2\alpha,\quad\chi_{k+1,i}\in[0,1],$$
where $\chi$ depends on the distance of the pre-rounding value to its grid neighbour, so the variance exceeds the target $2\alpha$ (as printed, p. 5). Deterministic rounding is biased and is not a fix (App. F).

Idea: instead of rounding a Gaussian sample, sample directly on the grid. A three-point distribution on $\{\Delta_W,-\Delta_W,0\}$ with mean $\mu\ge0$ and variance $v\le\Delta_W^2/4$:

> [!definition] Categorical distribution Cat(mu, v)
> $$\Pr[\Delta_W]=\frac{v+\mu^2+\mu\Delta_W}{2\Delta_W^2},\quad\Pr[-\Delta_W]=\frac{v+\mu^2-\mu\Delta_W}{2\Delta_W^2},$$
> and value $0$ otherwise.
>
> (source: ibid., eq. 5, p. 6)

> [!algorithm] Variance-corrected quantization $Q_{vc}(\mu,v,\Delta)$ (Algorithm 2) and VC SGLDLP-L (Algorithm 1)
> Algorithm 1: $\theta_{k+1}\leftarrow Q_{vc}\big(\theta_k-\alpha Q_G(\tilde\nabla U(\theta_k)),\ 2\alpha,\ \Delta_W\big)$.
>
> Algorithm 2, with $v_0=\Delta^2/4$ (largest variance stochastic rounding can add):
> - if $v>v_0$: $x\leftarrow\mu+\sqrt{v-v_0}\,\xi$; $r\leftarrow x-Q_d(x)$; draw $c_i\sim\mathrm{Cat}(|r_i|,v_0)$; return $Q_d(x)+\mathrm{sign}(r)\odot c$;
> - else: $r\leftarrow\mu-Q_s(\mu)$; per coordinate $v_s\leftarrow(1-|r_i|/\Delta)r_i^2+(|r_i|/\Delta)(-r_i+\mathrm{sign}(r_i)\Delta)^2$; if $v>v_s$ draw $c_i\sim\mathrm{Cat}(0,v-v_s)$ and set $\theta_i\leftarrow Q_s(\mu)_i+c_i$, else $\theta_i\leftarrow Q_s(\mu)_i$;
> - clip to the representable range.
>
> (source: ibid., Alg. 1-2, p. 6). The mean is always $\theta_{k,i}-\alpha\tilde\nabla U(\theta_k)_i$; the variance is $2\alpha$ except when $v=2\alpha<v_s$, which needs an extremely small step size (p. 6). Only the first two moments are matched. Cost is negligible next to the gradient. The block/floating-point version recomputes the gap after adding noise (Alg. 4-5, App. G, pp. 19-20).

> [!theorem] Theorem 3: VC SGLDLP-L
> Additionally assume $\mathbb E\|Q_G(\tilde\nabla U(\theta_k))\|_1\le G$. Let $v_0=\Delta_W^2/4$. Then
> $$W_2(\mu_K,\pi)\le(1-\alpha m)^KW_2(\mu_0,\pi)+1.65\frac Mm(\alpha d)^{1/2}+\min\Big(\frac{\Psi A}{m},\frac{M\sqrt A}{m}\Big)$$
> $$\qquad+\sqrt{\frac{\alpha\Delta_G^2d+4\alpha\kappa^2}{4m}+\frac{A}{\alpha m}}+\big((1-\alpha m)^K+1\big)\sqrt A\quad\textbf{[unverified: grouping of the A/(alpha m) term]}$$
> $$A=\begin{cases}5v_0d,&2\alpha>v_0\\ \max(2\Delta_W\alpha G,\ 4\alpha d),&\text{otherwise.}\end{cases}$$
>
> (source: ibid., Thm. 3, p. 6; proof App. D, pp. 16-18). As $\alpha\to0$ the bound stays finite rather than diverging. The authors state the rate is $O(\sqrt{\Delta_W})$, equal to the SGD bound with low-precision accumulators, and leave a tighter bound open (p. 6).

## Results

All deep-learning runs use QPyTorch simulation (p. 7). Predictions use Bayesian model averaging over collected samples.

- **Gaussian, 8-bit fixed point with 3 fractional bits (Fig. 1, p. 5)**: for $\alpha=10^{-3}$ and $10^{-4}$, naive SGLDLP-L gets the mean right but the variance wrong, worse at smaller $\alpha$; VC SGLDLP-L and SGLDLP-F match the target for both step sizes. No numeric error values are given.
- **MNIST logistic regression, prior $\mathcal N(0,1/6)$, 2 integer bits, vary fractional bits (Fig. 2a, p. 7)**: SGLDLP-F beats SGDLP-F at every bit width and recovers the full-precision test NLL ($-0.567$ for SGLD, $-0.566$ for SGD) with 6 fractional bits, where SGDLP-F needs 10. VC SGLDLP-L is much better than naive SGLDLP-L, beats SGDLP-L at all widths, and beats SGDLP-F at 2 fractional bits.
- **MNIST MLP, 100 hidden units, ReLU (Fig. 2b)**: same pattern; full-precision NLL $-1.17$ (SGLD) and $-1.14$ (SGD). Full-precision test error 1.9% SGLD vs 2.03% SGD (Fig. 3, App. H).
- **CIFAR / IMDB, ResNet-18 / LSTM, 3 runs, test error % ± s.e. (Table 1, p. 8)**:

  | Method | CIFAR-10 | CIFAR-100 | IMDB |
  |---|---|---|---|
  | 32-bit SGLD | 4.65 ± 0.06 | 22.58 ± 0.18 | 13.43 ± 0.21 |
  | 32-bit SGD | 4.71 ± 0.02 | 22.64 ± 0.13 | 13.88 ± 0.29 |
  | 32-bit cSGLD | 4.54 ± 0.05 | 21.63 ± 0.04 | 13.25 ± 0.18 |
  | 8-bit fixed: naive SGLDLP-L | 7.82 ± 0.13 | 27.25 ± 0.13 | 16.63 ± 0.28 |
  | 8-bit fixed: VC SGLDLP-L | 7.13 ± 0.01 | 26.62 ± 0.16 | 15.38 ± 0.27 |
  | 8-bit fixed: SGDLP-L | 8.53 ± 0.08 | 28.86 ± 0.10 | 19.28 ± 0.63 |
  | 8-bit fixed: SGLDLP-F | 5.12 ± 0.06 | 23.30 ± 0.09 | 15.40 ± 0.36 |
  | 8-bit fixed: SGDLP-F | 5.20 ± 0.14 | 23.84 ± 0.12 | 15.74 ± 0.79 |
  | 8-bit BFP: naive SGLDLP-L | 5.85 ± 0.04 | 26.38 ± 0.13 | 14.64 ± 0.08 |
  | 8-bit BFP: VC SGLDLP-L | 5.51 ± 0.01 | 25.22 ± 0.18 | 13.99 ± 0.24 |
  | 8-bit BFP: SGDLP-L | 5.86 ± 0.18 | 26.19 ± 0.11 | 16.06 ± 1.81 |
  | 8-bit BFP: SGLDLP-F | 4.58 ± 0.07 | 22.59 ± 0.18 | 14.05 ± 0.33 |
  | 8-bit BFP: SGDLP-F | 4.75 ± 0.05 | 22.9 ± 0.13 | 14.28 ± 0.17 |
  | 8-bit BFP: VC cSGLDLP-L | 4.97 ± 0.10 | 22.61 ± 0.12 | 13.09 ± 0.27 |
  | 8-bit BFP: cSGLD-F | 4.32 ± 0.07 | 21.50 ± 0.14 | 13.13 ± 0.37 |

  Fixed point uses 8 bits for weights and gradients but full-precision activations, because low-precision activations "significantly harm" performance (p. 8). On CIFAR-100 fixed point, VC SGLDLP-L beats SGDLP-L by 2.24 points, SGLDLP-F beats SGDLP-F by 0.54, full-precision SGLD beats SGD by 0.06 (p. 8). In block floating point SGLDLP-F is within about 0.1 points of 32-bit SGLD on CIFAR (4.58 vs 4.65; 22.59 vs 22.58) and VC cSGLDLP-L matches or beats 32-bit SGD, per the authors (p. 8). The cSGLD runs use the cyclical schedule of [[Cyclical SG-MCMC (Zhang 2020)]] (7 cycles, 5 models per cycle on CIFAR, App. H.3).
- **Calibration, ECE % (Table 2, p. 8)**, CIFAR-10 / CIFAR-100: 32-bit SGLD 1.11 / 3.92, SGD 2.53 / 4.97, cSGLD 0.66 / 1.38. 8-bit fixed: VC SGLDLP-L 0.6 / 3.19, SGLDLP-F 1.12 / 4.42, SGDLP-L 3.4 / 10.38, SGDLP-F 3.05 / 6.80. 8-bit BFP: VC SGLDLP-L 0.6 / 5.82, SGLDLP-F 1.19 / 3.78, SGDLP-L 4.23 / 12.97, SGDLP-F 2.76 / 5.2, VC cSGLDLP-L 0.51 / 1.39, cSGLD-F 0.56 / 1.33. Low-precision SGD becomes more overconfident; SGLD calibration holds (10 bins, App. H.3). Not all cells favour SGLD: BFP VC SGLDLP-L on CIFAR-100 (5.82) is worse than full-precision SGLD (3.92).
- **ImageNet, ResNet-18 (Table 3, p. 9)**: SGD 90 epochs, SGLD 10 further epochs from the SGD solution. Top-1 / top-5 error %: 32-bit SGLD 30.39 / 10.76, SGD 30.56 / 10.97; 8-bit BFP SGLDLP-F 31.47 / 11.77, SGDLP-F 32.23 / 12.09. The SGLD gap is 0.76 points top-1 at 8 bits against 0.17 at 32 bits. Low-precision accumulators did not give reasonable results for either method, possibly hyper-parameter tuning (p. 9). Single run, no error bars.
- **Rounding (App. F, p. 19)**: CIFAR-10, 8-bit BFP: deterministic rounding gives 7.44% (SGDLP-L) and 7.37% (naive SGLDLP-L) against 5.86% and 5.85% with stochastic rounding; VC SGLDLP-L 5.51%.
- **Guidance (p. 9)**: SGLDLP-F is more accurate; VC SGLDLP-L needs less computation, preferable on edge devices.

## Limitations

Stated by the authors: the bounds are for strongly log-concave targets with Lipschitz Hessian, while the deep-net experiments are outside the theory (p. 7); the VC bound is only $O(\sqrt{\Delta_W})$ and they leave improving it open (p. 6); $Q_{vc}$ matches only mean and variance (p. 6); activations stay full precision in fixed-point runs (p. 8); no low-precision accumulator result on ImageNet (p. 9).

Wiki note: low precision is simulated in QPyTorch, so the latency and memory gains are not measured, and the headline "8 bits" claim covers weights, gradients and (in BFP) activations and errors but still uses a full-precision accumulator for the best-performing SGLDLP-F. The "half the bits" claim compares upper bounds, with the SGD bound taken from another paper; it is supported empirically only on MNIST logistic regression (6 vs 10 bits). Table 1 entries differ by amounts comparable to the reported standard errors in several cells (e.g. 32-bit SGLD vs SGD on CIFAR). Bounds are on $W_2$ of the chain's law, as in [[Cyclical SG-MCMC (Zhang 2020)]], not of the time-averaged sample.

## Connections

- Direct application of [[SGLD (Welling 2011)]]; the cited SG-MCMC family is [[SG-MCMC]] ([[SGHMC]], complete recipe of Ma et al. 2015).
- Reuses the cyclical schedule of [[Cyclical SG-MCMC (Zhang 2020)]] (cSGLD) as a variant; diverse cycles are argued to offset quantization error.
- The only prior low-precision MCMC the authors know is Ferianc et al. 2021, post-training quantization of SGHMC-trained BNNs (p. 2).
- Same first author as [[AMAGOLD (Zhang 2020)]]; complementary: AMAGOLD removes discretization bias with a Metropolis correction, whereas here the question is quantization bias. Combining them is not studied (**[unverified]** that it is feasible).
- Proof technique: Theorem 4 of Dalalyan & Karagulyan (2019), Langevin with noisy gradients (App. B, p. 12). See [[Langevin dynamics]], [[Wasserstein distance]], [[Variance-corrected quantization]].





%% refs:start %%
**Cites in this wiki**: [[Cyclical SG-MCMC (Zhang 2020)]], [[SGLD (Welling 2011)]]
%% refs:end %%

**Sources**: `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGLD (Welling 2011)]]
- [[Cyclical SG-MCMC (Zhang 2020)]]
- [[AMAGOLD (Zhang 2020)]]
- [[SGLD]]
- [[SG-MCMC]]
- [[Langevin dynamics]]
- [[Wasserstein distance]]
- [[Bayesian model averaging]]
- [[Variance-corrected quantization]]
