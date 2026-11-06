---
type: paper
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Zhang, Li, Zhang, Chen, Wilson 2020, ICLR, eq. 1, Alg. 1, Thm. 1-2"
tags: []
authors: [Zhang, Li, Zhang, Chen, Wilson]
year: 2020
venue: "ICLR"
file: "IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf"
---

# Cyclical Stochastic Gradient MCMC for Bayesian Deep Learning (Zhang 2020)

**Summary**: Replaces the decreasing step-size schedule of SG-MCMC with a cyclical cosine schedule. Each cycle has a large-step exploration stage (zero-temperature, i.e. plain SGD) that jumps to a new mode and a small-step sampling stage that characterizes it, so a single run visits several modes of a neural-network posterior. The paper proves non-asymptotic weak and 2-Wasserstein bounds for cyclical SGLD and reports gains on CIFAR-10/100, ImageNet and out-of-distribution entropy.

**Authors**: Ruqi Zhang, Chunyuan Li, Jianyi Zhang, Changyou Chen, Andrew Gordon Wilson · **Year**: 2020 (ICLR) · **File**: `IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`

Not a Bilionis-lab paper (no `lab` tag). Note the file name says "Ruqi Zhang" but the first author is Zhang, with Wilson as senior author.

---

## Problem

SG-MCMC ([[stochastic-gradient-mcmc]]) as introduced in [[welling-2011-sgld]] needs a decreasing step size for asymptotic consistency, but in finite time it has bounded estimation error and, with small step sizes, gets stuck in one mode of the highly multimodal posterior of a deep network (pp. 1-2). The step size controls both drift toward high density and the amount of injected noise, so small steps reduce exploration. Stochastic MH correction to allow larger steps is judged too expensive, and large steps get rejected (p. 4).

## Method

Notation (p. 2-3): posterior $p(\theta|D)\propto\exp(-U(\theta))$ with $U(\theta)=-\log p(D|\theta)-\log p(\theta)$; mini-batch estimate $\tilde U(\theta)=-\frac{N'}{N}\sum_{i=1}^{N'}\log p(x_i|\theta)-\log p(\theta)$ (as printed; the factor $N'/N$ appears there, likely meaning $N/N'$ [unverified]). The paper writes step size $\alpha_k$ and uses $U$ and a unit-coefficient SDE; [[welling-2011-sgld]] writes $\epsilon_t/2$ and $\log p$. Wiki note: the two parametrisations agree after $\alpha=\epsilon/2$ and $U=-\log p$.

> [!definition] SGLD and SGHMC updates (as used here)
> SGLD: $\theta_k=\theta_{k-1}-\alpha_k\nabla\tilde U(\theta_k)+\sqrt{2\alpha_k}\,\epsilon_k$, $\epsilon_k\sim\mathcal N(0,I)$.
> SGHMC: $\theta_k=\theta_{k-1}+v_{k-1}$, $v_k=v_{k-1}-\alpha_k\nabla\tilde U(\theta_k)-\eta v_{k-1}+\sqrt{2(\eta-\hat\gamma)\alpha_k}\,\epsilon_k$, with $1-\eta$ the momentum term and $\hat\gamma$ the gradient-noise estimate.
>
> (source: Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf, §2, p. 3) See [[stochastic-gradient-langevin-dynamics]], [[stochastic-gradient-hmc]].

> [!definition] Standard step-size assumption (Assumption 1)
> $0<\alpha_{k+1}<\alpha_k$, $\sum_k\alpha_k=\infty$, $\sum_k\alpha_k^2<\infty$; typical $\alpha_k=a(b+k)^{-\gamma}$, $\gamma\in(0.5,1]$.
>
> (source: ibid., Assumption 1, p. 3)

> [!definition] Cyclical cosine step size
> With $\alpha_0$ the initial step, $M$ the number of cycles, $K$ total iterations,
> $$\alpha_k=\frac{\alpha_0}{2}\Big[\cos\Big(\frac{\pi\,\mathrm{mod}(k-1,\lceil K/M\rceil)}{\lceil K/M\rceil}\Big)+1\Big].$$
> Each period starts at $\alpha_0$ and decays to $\approx0$; the chain then restarts with a large step.
>
> (source: ibid., eq. 1, p. 3; after Loshchilov & Hutter 2016, Huang et al. 2017)

> [!definition] Tempered posterior and cycle proportion
> System temperature $T$: $p(\theta|D)\propto\exp(-U(\theta)/T)$. $T=1$ is the untempered posterior; $T\to0$ makes sampling equivalent to minimising $U$. Define the completed proportion of a cycle $r(k)=\mathrm{mod}(k-1,\lceil K/M\rceil)/\lceil K/M\rceil$. Exploration uses $T=0$ while $r(k)<\beta$; sampling uses $T=1$ afterwards. $\beta\in(0,1)$ sets the exploration/sampling split.
>
> (source: ibid., §3.1, p. 4)

> [!algorithm] Cyclical SG-MCMC (Algorithm 1)
> Input: $\alpha_0$, $M$, $K$, $\beta$.
> for $k=1,\dots,K$: set $\alpha\leftarrow\alpha_k$ by eq. 1;
> - if $r(k)<\beta$ (exploration): $\theta\leftarrow\theta-\alpha\nabla\tilde U_k(\theta)$;
> - else (sampling): collect samples with an SG-MCMC update (SGLD or SGHMC).
> Output $\{\theta_k\}$.
>
> (source: ibid., Alg. 1, p. 4) See [[cyclical-sg-mcmc]].

> [!definition] Combining samples across cycles
> Cycle $m$ covers region $\Theta_m$ with sub-posterior $p_m(\theta|D)=p(\theta|D)\mathbf 1_{\Theta_m}/w_m$, $w_m=\int_{\Theta_m}p(\theta|D)d\theta$. Then
> $$\hat f=\sum_{m=1}^Mw_m\hat f_m,\qquad \hat f_m=\frac1{K_m}\sum_{j=1}^{K_m}f(\theta_j^{(m)}),$$
> with weights from the harmonic-mean estimator $\hat w_m\approx\big[\frac1{K_m}\sum_j\frac1{p(D|\theta^{(m)}_j)}\big]^{-1}$. If the $\Theta_m$ overlap, indicator functions of disjoint sub-regions $\tilde\Theta_m$ and a count $n_m$ are used instead.
>
> (source: ibid., App. F, eq. 33, p. 23-24). In the DNN experiments the weights are simply set equal (p. 7).

### Theory (§4, App. B-G)

Analysis covers cyclical SGLD only and omits the exploration stage (it is stochastic optimization). Underlying SDE: $d\theta_t=-\nabla U(\theta_t)dt+\sqrt2\,dW_t$.

> [!theorem] Weak convergence of cSGLD (Theorem 1)
> Under Assumption 2 (bounded Poisson-equation solution and derivatives), for smooth test function $\phi$, with $\hat\phi$ the sample average and $\bar\phi$ the posterior mean:
> $$\big|\mathbb E\hat\phi-\bar\phi\big|=O\Big(\frac1{\alpha_0K}+\alpha_0\Big),\qquad \mathbb E\big(\hat\phi-\bar\phi\big)^2=O\Big(\frac1{\alpha_0K}+\alpha_0^2\Big).$$
>
> (source: ibid., Thm. 1, eq. 2, p. 5). Proof (App. C): special case of Chen et al. (2015) Lemma 1 with first-order integrator, $S_K=\sum\alpha_k=O(\alpha_0K)$ and $\sum_j\alpha_{j+1}^2=\frac{3\alpha_0^2K}{8}$ (eq. 6). The proof notes the algorithm is biased since Assumption 4 (decaying step) fails.

> [!theorem] 2-Wasserstein convergence of cSGLD (Theorem 2)
> Under Assumption 3 (smooth, dissipative $U$, bounded gradient-noise second moment, finite initial exponential moment), there are constants $C_0,\dots,C_4$ independent of the step sizes such that for $K\bmod M=0$,
> $$W_2(\mu_K,\nu_\infty)\le C_3\exp\!\Big(-\frac{K\alpha_0}{2C_4}\Big)+\Big(6+\frac{C_2K\alpha_0}{2}\Big)^{1/2}\Big[\Big(\frac{3C_1\alpha_0^2K}{8}+\frac{\sigma C_0K\alpha_0}{2}\Big)^{1/2}+\Big(\frac{3C_1\alpha_0^2K}{16}+\frac{\sigma C_0K\alpha_0}{4}\Big)^{1/4}\Big].$$
> (Main-text extraction is garbled; the form above follows the appendix derivation, App. D.1, p. 19.) With $\alpha_0=O(K^{-\beta})$, $\beta>1$, a simplified bound is given.
>
> (source: ibid., Thm. 2, p. 5; proof App. D, pp. 15-19). Proof route: split $W_2(\mu_K,\nu_\infty)\le W_2(\mu_K,\nu_{\sum\alpha_k})+W_2(\nu_{\sum\alpha_k},\nu_\infty)$ (eq. 9); first term via KL bound on interpolated processes and Bolley-Villani, after Raginsky et al. (2017); second term exponential decay $C_3\exp(-\sum\alpha_k/C_4)$.

Remark 1 (p. 6): first part of the bound is the speed of the exact diffusion to stationarity, the second is numerical error; the dependence on $K$ matches standard SGLD; stricter (convex) assumptions improve it (App. G, Assumption 5, eq. 36-37, a Dalalyan-Karagulyan-style bound that contracts at rate $(1-m\alpha_{\min})^K$).

Informal comparison with SGLD (App. E, p. 23): since $\sum_k\alpha_k=K\alpha_0/2$ while for $h_k=h_0/k$, $\sum h_k=O(h_0\log K)$, cyclical SGLD advances much more diffusion time per $K$ iterations, so the exponentially decaying term is smaller. Raising $h_0$ to match needs $h_0=O(\alpha_0K/\log K)$, which blows up the discretisation term. This is heuristic and conditional on $\alpha_0$ small.

Conceptual points (§3): exploration acts as warm restarts; cSG-MCMC approximates parallel MCMC at single-chain cost; it inverts the Santa algorithm (Chen et al. 2016a), which explores at $T=1$ then anneals $T\to0$.

## Results

- **Synthetic, 25-Gaussian mixture (§5.1, App. A.1, pp. 6, 13)**: grid means $\{-4,-2,0,2,4\}^2$, covariance $0.03I$. 4 parallel chains of 50k iterations each: SGLD found 4 of 25 modes, cSGLD fully covered (Fig. 2; $M=30$, $\alpha_0=0.09$, $\beta=1/4$, SGLD $\alpha_k\propto0.05k^{-0.55}$). Single chain, 50k samples: SGLD 1 mode. Mode coverage over 10 runs (radius 0.25, threshold 100 samples; Table 4): SGLD $1.8\pm0.13$, cSGLD $6.7\pm0.52$, parallel SGLD $18\pm0.47$, parallel cSGLD $24.4\pm0.22$.
- **Bayesian logistic regression, unimodal (App. A.2, p. 13-14)**: UCI Australian, German, Heart; 5000 samples after 5000 burn-in; median ESS (Table 5): Australian SGLD 1676, cSGLD 2138, SGHMC 1317, cSGHMC 4707; German 492, 978, 2007, 2436; Heart 2199, 2541, 5000, 5000.
- **ResNet-18, CIFAR-10/100 (Table 1, p. 7)**, 200 epochs, 3 runs, $M=4$, $\alpha_0=0.5$, $\beta=0.8$/$0.94$, 3 samples per cycle, tempering at the pSGLD temperature ($T\approx0.0045$). Test error % (CIFAR-10 / CIFAR-100): SGD 5.29 / 23.61; SGDM 5.17 / 22.98; Snapshot-SGD 4.46 / 20.83; Snapshot-SGDM 4.39 / 20.81; SGLD 5.20 / 23.23; **cSGLD 4.29 / 20.55**; SGHMC 4.93 / 22.60; **cSGHMC 4.27 / 20.50**. Baseline SG-MCMC runs noise-free for the first 150 epochs.
- **Weight-space diversity (Fig. 3, p. 7-8)**: MDS of 12 CIFAR-100 samples forms 4 clusters for cSG-MCMC, one cluster for SG-MCMC. Linear interpolation between samples from neighbouring cycles shows a test-error spike (different modes); SG-MCMC samples interpolate smoothly. Single cSG-MCMC samples are individually worse than SG-MCMC samples; the ensemble is better.
- **Versus parallel MCMC (Table 2, p. 8)**, CIFAR-10 / CIFAR-100 test error: cyclical + 4 parallel chains (cost 200/800 epochs) SGLD 4.09 / 19.37, SGHMC 3.95 / 19.19; decreasing + 4 parallel 4.15 / 20.29, 4.09 / 19.72; decreasing + parallel at 100/400 epochs 5.11 / 21.16, 4.52 / 20.82; cyclical single chain (200/200) 4.29 / 20.55, 4.27 / 20.50. Single cyclical chain beats 4 decreasing-schedule chains at half the total cost (200 vs 400 epochs). Table 6 (App. I.1): robust over $M\in\{2,5\}$, $\beta\in\{0.7,0.9\}$ on CIFAR-10.
- **ImageNet, ResNet-50, 120 epochs (Table 3, p. 8)**: NLL / Top-1 / Top-5: SGDM 0.9595 / 76.046 / 92.776; Snapshot-SGDM 0.8941 / 77.142 / 93.344; SGHMC 0.9308 / 76.274 / 92.994; cSGHMC 0.8882 / 77.114 / 93.524. cSGHMC has the best NLL and Top-5; Snapshot-SGDM has slightly higher Top-1.
- **Uncertainty (§5.3, p. 9)**: 3-layer MLP trained on MNIST, predictive entropy on notMNIST; cSGLD and cSGHMC have lower probability of low-entropy predictions than baselines (Fig. 4, empirical CDF; no table).
- **Tempering (App. J, p. 26)**: best $T=0.1$ on CIFAR-10 (NLL 0.1331, error 4.22%) and $T=0.01$ on CIFAR-100 (NLL 0.7835, error 20.53%); optimal $T<1$ usually. Authors attribute this to model misspecification (**their hypothesis**).

## Limitations

As stated: the convergence bounds omit the exploration stage and $\alpha_0$ must be small for them to be meaningful (p. 5, App. E); the cyclical algorithm is biased with respect to the true posterior (no decaying step, App. C); $\beta$ needs cross-validation per task and the cycle length is a trade-off against $M$ (App. I.2); results depend on tempering and on turning off noise early in training for baselines (p. 7); sample weights are set equal in the DNN experiments rather than estimated (p. 7).

Wiki note: Theorem 2's bound grows with $K\alpha_0$ and $\alpha_0^2K$ in the numerical-error term, so it is informative only for small $\alpha_0$, while the experiments use $\alpha_0=0.5$; the theory and the practical regime are not the same. The reported "T≈0.0045" tempering means the CIFAR numbers are for a heavily sharpened posterior, not the untempered posterior.

## Connections

- Builds on [[welling-2011-sgld]] (the SGLD update and the decaying step-size assumption); applies the cyclical schedule from SGDR/Snapshot ensembles in optimization to [[stochastic-gradient-mcmc]]; uses [[stochastic-gradient-hmc]] as the second base sampler.
- Complementary to [[zhang-2020-amagold]] (same first author): AMAGOLD addresses step-size bias by a stochastic MH-style correction, whereas cSG-MCMC accepts the bias and spends large steps on exploration with no correction. [[zhang-2022-low-precision-sgld]] is a third paper by the same first author, about low-precision arithmetic.
- Related concepts: [[langevin-dynamics]], [[metropolis-hastings-correction]], [[cyclical-sg-mcmc]], [[cyclical-sg-mcmc]], [[wasserstein-distance]], [[bayesian-model-averaging]].

**Sources**: `IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[welling-2011-sgld]]
- [[zhang-2020-amagold]]
- [[zhang-2022-low-precision-sgld]]
- [[stochastic-gradient-langevin-dynamics]]
- [[stochastic-gradient-mcmc]]
- [[stochastic-gradient-hmc]]
- [[cyclical-sg-mcmc]]
- [[langevin-dynamics]]
- [[metropolis-hastings-correction]]
- [[cyclical-sg-mcmc]]
- [[wasserstein-distance]]
