---
type: paper
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Zhang, Cooper, De Sa 2020, AISTATS, Alg. 2, eq. 6, Thm. 1-2"
tags: [paper, sampling, mcmc, bayesian]
authors: [Zhang, Cooper, De Sa]
year: 2020
venue: "AISTATS (PMLR 108)"
file: "IFT/Ruqi Zhang - AMAGOLD.pdf"
---

# AMAGOLD: Amortized Metropolis Adjustment for Efficient Stochastic Gradient MCMC (Zhang 2020)

**Summary**: SGHMC with a constant step size is biased. AMAGOLD runs $T$ stochastic leapfrog steps and applies one Metropolis-Hastings accept/reject at the end, using an accumulated energy term so that the correction needs no extra gradient evaluations. The chain has the exact target as stationary distribution at fixed step size, and its spectral gap is within a constant factor of the full-batch L2MC chain.

**Authors**: Ruqi Zhang, A. Feder Cooper, Christopher De Sa (Cornell) · **Year**: 2020 · **File**: `IFT/Ruqi Zhang - AMAGOLD.pdf`

Not a Bilionis-lab paper (no `lab` tag). The PDF in the library has 10 pages (main text and references); the appendices cited in the text (proofs, App. A-G) are not included in it, so proof details below are from the main text only.

---

## Problem

[[SGHMC]] (SGHMC) replaces the full gradient in HMC by a mini-batch estimate. This introduces bias from two sources: time discretization with a non-vanishing step $\epsilon$, and gradient noise. The usual fix is $\epsilon\to0$, which slows convergence. The standard unbiasing tool is the [[Metropolis-Hastings correction]], but it needs a sum over the whole dataset each iteration, which defeats mini-batching (pp. 1-2). First-order methods with mini-batch MH exist (Korattikara et al. 2014); the authors claim no unbiased, efficient second-order SG-MCMC existed (p. 3).

## Method

Setup (p. 3): target $\pi(\theta)\propto\exp(-U(\theta))$, $U(\theta)=-\sum_{x\in D}\log p(x|\theta)-\log p(\theta)$; mini-batch estimate $\tilde U(\theta)\approx-\frac{|D|}{|\tilde D|}\sum_{x\in\tilde D}\log p(x|\theta)-\log p(\theta)$. Augmented target with isotropic momentum:

> [!definition] Hamiltonian and dynamics
> $$\pi(\theta,r)\propto\exp(-H(\theta,r))=\exp\Big(-U(\theta)-\frac1{2\sigma^2}\|r\|^2\Big),$$
> $$d\theta=\sigma^{-2}r\,dt,\qquad dr=-\nabla U(\theta)\,dt.$$
> HMC resamples $r$ periodically; L2MC (second-order Langevin) adds friction and Gaussian noise continuously. Discretised versions of either need an MH correction.
>
> (source: Ruqi Zhang - AMAGOLD.pdf, §3, eq. 1, p. 3)

SGHMC (Algorithm 1, p. 2) is the leapfrog scheme with $\nabla\tilde U$ and friction $\beta$, noise $\eta_t\sim\mathcal N(0,4\epsilon\beta\sigma^2)$, and no MH step.

> [!definition] Reversibility and skew-reversibility
> A chain with kernel $G$ is reversible if $\pi(x)G(x,y)=\pi(y)G(y,x)$ (eq. 2). Given a measure-preserving involution $x\mapsto x^\star$ with $\pi(x)=\pi(x^\star)$, it is skew-reversible if
> $$\pi(x)G(x,y)=\pi(y^\star)G(y^\star,x^\star).$$
> For Hamiltonian dynamics $(\theta,r)^\star=(\theta,-r)$. Skew-reversible chains also have stationary distribution $\pi$. Resampling the momentum at the start of the outer loop recovers a reversible chain.
>
> (source: ibid., §4, eq. 2 and 5, pp. 3-4)

> [!definition] Amortized Metropolis adjustment (AMA)
> Run $T$ proposal steps $x_{t+1}\sim P(x_t,x_{t+1};\zeta_t)$ from $x_0=x$ with independent stochastic samples $\zeta_t$ (e.g. mini-batch indices), set $y=x_T$, accept with
> $$\tau=\min\Big(1,\frac{\pi(y)}{\pi(x)}\prod_{t=0}^{T-1}\frac{P(x_{t+1},x_t;\zeta_t)}{P(x_t,x_{t+1};\zeta_t)}\Big)$$
> (eq. 3, equivalently eq. 4 as a product of per-step MH ratios), else stay at $x$. Skew-reversible version:
> $$\tau=\min\Big(1,\frac{\pi(y^\star)}{\pi(x)}\prod_{t=0}^{T-1}\frac{P(x^\star_{t+1},x^\star_t;\zeta_t)}{P(x_t,x_{t+1};\zeta_t)}\Big)\quad(\text{eq. 6}).$$
> The cost of the correction is divided by $T$. It is effective when the proposals are close to (skew-)reversible, which SGHMC steps are, in the skew sense.
>
> (source: ibid., §4, eq. 3-6, pp. 4)

> [!algorithm] AMAGOLD (Algorithm 2)
> Given $U,\theta,\epsilon,\sigma^2,\beta$; loop:
> 1. optionally resample $r\sim\mathcal N(0,\sigma^2I)$ (reversible variant);
> 2. $r_{-1/2}\leftarrow r$, $\rho_{-1/2}\leftarrow0$; half position step $\theta_0\leftarrow\theta+\frac12\epsilon\sigma^{-2}r_{-1/2}$;
> 3. for $t=0,\dots,T-1$: if $t\ne0$, $\theta_t\leftarrow\theta_{t-1}+\epsilon\sigma^{-2}r_{t-1/2}$; draw $\eta_t\sim\mathcal N(0,4\epsilon\beta\sigma^2I)$ and a mini-batch for $\tilde U_t$;
>    $$r_{t+1/2}\leftarrow\frac{(1-\epsilon\beta)r_{t-1/2}-\epsilon\nabla\tilde U_t(\theta_t)+\eta_t}{1+\epsilon\beta},$$
>    $$\rho_{t+1/2}\leftarrow\rho_{t-1/2}+\tfrac12\epsilon\sigma^{-2}\nabla\tilde U_t(\theta_t)^\top\big(r_{t-1/2}+r_{t+1/2}\big);$$
> 4. half position step $\theta_T\leftarrow\theta_{T-1}+\frac12\epsilon\sigma^{-2}r_{T-1/2}$; $\theta^*=\theta_T$, $r^*=r_{T-1/2}$;
> 5. $a\leftarrow\exp\big(U(\theta)-U(\theta^*)+\rho_{T-1/2}\big)$; with probability $\min(1,a)$ set $\theta\leftarrow\theta^*$, $r\leftarrow r^*$ (if $\theta^*\in\Theta$); otherwise $r\leftarrow-r_{-1/2}$.
>
> (source: ibid., Alg. 2, p. 5). The proposal is the stochastic leapfrog $\theta_0=\theta+\frac12\epsilon\sigma^{-2}r$, $r^*=((1-\epsilon\beta)r-\epsilon\nabla\tilde U_t(\theta_0)+\mathcal N(0,4\epsilon\beta\sigma^2I))/(1+\epsilon\beta)$, $\theta^*=\theta_0+\frac12\epsilon\sigma^{-2}r^*$ (§5, p. 4). See [[AMAGOLD]].

Differences from SGHMC (p. 4-5): a time-symmetric inner update (Line 12, equivalent to Alg. 1 Line 11 after reparametrising hyperparameters); half-position-updates at both ends of the outer loop; the energy accumulator $\rho$, which sums the log of the product in eq. 6 and costs almost nothing since all terms are already computed. Special cases (p. 5): full batch gives L2MC with amortized MH; full batch, $\beta=0$ and momentum resampling gives HMC (App. D); disabling the MH step gives SGHMC.

> [!theorem] Correctness (Theorem 1)
> With momentum resampled (Line 3) the AMAGOLD chain is reversible; otherwise it is skew-reversible. In either case its stationary distribution is $\pi$.
>
> (source: ibid., Thm. 1, p. 5; explicit proof in the appendix, not in the library PDF)

> [!theorem] Convergence rate relative to L2MC (Theorem 2)
> Assume geometric ergodicity of the full-batch chain and a bounded gradient covariance
> $$\mathbb E\big[(\nabla\tilde U-\nabla U)(\nabla\tilde U-\nabla U)^\top\big]\preceq\frac{V^2}{d}I.$$
> Let $\bar\gamma$ be the spectral gap of L2MC with parameters $(\epsilon,\sigma,\beta)$ and assume $\epsilon V^2\le4\sigma^2\beta d$. Define $c=1+\sqrt{\epsilon V^2/(16\sigma^2\beta Td^2)}$ and let $\gamma$ be the spectral gap of AMAGOLD with parameters $(\epsilon,\sigma c^{-1/4},\beta c^{-1/2})$. Then
> $$\frac{\gamma}{\bar\gamma}\ge\exp\Big(-\frac{\epsilon TV^2}{4\sigma^2\beta}-\sqrt{\frac{\epsilon TV^2}{\sigma^2\beta}}\Big).$$
>
> (source: ibid., Thm. 2, p. 6; equation verified against the PDF page image). See [[AMAGOLD]].

Takeaways stated by the authors (p. 6): the rate matches L2MC up to a constant tending to 1 as batch size grows or $\epsilon$ shrinks; shrinking the mini-batch ($V^2$ up) degrades the rate like $\exp(-O(V^2))$; the bound is useful when $\epsilon TV^2\ll\sigma^2\beta$.

Practical modifications (§5.2, p. 6-7): use a mini-batch for the MH energy difference on line 17 (composable with Korattikara et al. 2014 and similar); tune $\epsilon$ during burn-in to target an average acceptance probability (85% in the double-well demonstration) since the MH acceptance rate gives step-size feedback; for networks reparametrise with $v=\epsilon\sigma^{-2}r$, $b=\epsilon\beta$, $h=\epsilon^2\sigma^{-2}$ (App. F) so the update resembles SGD with momentum.

## Results

Defaults: reversible AMAGOLD, $T=10$, $\beta=0.25$ (p. 7).

- **Double well (§5, Fig. 1, p. 5)**: $U(\theta)=(\theta+4)(\theta+1)(\theta-1)(\theta-3)/14+0.5$ with $\nabla\tilde U=\nabla U+\mathcal N(0,1)$. At $\epsilon=0.25$ SGHMC visibly diverges from the true density while AMAGOLD matches it; symmetric KL vs step size shows SGHMC sensitive to $\epsilon$ and AMAGOLD robust. At $\epsilon=0.01$ both are poor (step too small); with $\epsilon$ tuned to 85% acceptance AMAGOLD recovers the density (Fig. 1c). No KL numbers in the text.
- **Synthetic 2D distributions (§6.1, Fig. 2-3, p. 7)**: Dist1, Dist2 adapted from Yin and Zhou (2018), $5\times10^6$ samples, step size 0.01 to 0.25, baselines HMC, L2MC with amortized MH, SGHMC; stochastic gradients simulated by adding $\mathcal N(0,I)$. AMAGOLD's symmetric KL is close to the full-batch methods and well below SGHMC's, especially at large $\epsilon$. Convergence speed matches L2MC "up to a constant factor slowdown of about $10^{-3}$" (as printed, p. 7; the text does not say whether this is a measured ratio or an order of magnitude).
- **Bayesian logistic regression (§6.2, Fig. 4, p. 7-8)**: Australian (15 covariates, 690 points, batch 32) and Heart (14 covariates, 270 points, batch 16); MSE of the parameter estimate against $10^7$ HMC samples; $5\times10^6$ samples, step sizes $10^{-6}$ to $5\times10^{-3}$. AMAGOLD has smaller error than SGHMC across step sizes; runtime at $\epsilon=10^{-4}$ is much below full-batch HMC/L2MC and not much above SGHMC. AMAGOLD's error at large $\epsilon$ is large because acceptance probability drops; the authors suggest a 20-80% acceptance target or the §5.2 tuning.
- **Bayesian neural network, MLP with two ReLU layers, 60000 points, batch 2000 (§6.3, Table 2, p. 8)**: irreversible AMAGOLD, 3 epochs of SGD-momentum burn-in, 20 samples. Test error %, $\pm$ standard error:

  | Algorithm | $b$ | $h=0.0005$ | $h=0.001$ |
  |---|---|---|---|
  | SGHMC | 0.01 | 3.69 ± 0.03 | 3.77 ± 0.17 |
  | SGHMC | 5e-6 | 89.95 ± 0.29 | 89.70 ± 0.91 |
  | AMAGOLD | 0.01 | 3.63 ± 0.04 | 3.65 ± 0.08 |
  | AMAGOLD | 5e-6 | 3.65 ± 0.10 | 3.63 ± 0.10 |

  SGHMC diverges at small $b$; AMAGOLD is insensitive to the hyperparameters.
- **Uncertainty (Fig. 5, p. 8)**: entropy of predictive distribution on notMNIST for the eight models of Table 2. AMAGOLD is consistent across settings; SGHMC is overconfident for small $b$ or large $h$ (CDF plot only).

## Limitations

As stated: the MH step still needs the full-data energy, so mini-batch MH is recommended for large data (p. 6); large step sizes lower the acceptance rate and inflate error (p. 7); the rate bound needs geometric ergodicity and a bounded-variance assumption and holds for the reversible variant (p. 6); stochastic MH variants, other SG-MCMC variants (thermostats, complete-recipe) are left as future combinations (p. 8).

Wiki note: the paper's theorems concern stationarity and a spectral gap relative to L2MC, not a non-asymptotic error bound in a distance such as 2-Wasserstein (contrast the cyclical paper, [[Cyclical SG-MCMC (Zhang 2020)]]). Mini-batch MH, which is what is needed at scale, is outside the exactness guarantee: the guarantee is for the full-energy MH of Alg. 2. The neural-network experiment is a small MLP; the paper does not test deep networks.

## Connections

- Corrects the bias of [[SGHMC]]; the first-order analogue is SGLD ([[SGLD (Welling 2011)]]), which dropped MH because rejections vanish as $\epsilon\to0$, the very decay AMAGOLD avoids.
- Same first author as [[Cyclical SG-MCMC (Zhang 2020)]] (which sidesteps MH and accepts bias) and [[Low-precision SGLD (Zhang 2022)]]. Zhang et al. 2020 cited in §6.3 for the SGD-momentum burn-in is the cyclical paper.
- Related concepts: [[Metropolis-Hastings correction]], [[Langevin dynamics]], [[SGHMC]], [[AMAGOLD]], [[AMAGOLD]], [[SG-MCMC]].

**Sources**: `IFT/Ruqi Zhang - AMAGOLD.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGLD (Welling 2011)]]
- [[Cyclical SG-MCMC (Zhang 2020)]]
- [[Low-precision SGLD (Zhang 2022)]]
- [[AMAGOLD]]
- [[SGHMC]]
- [[SG-MCMC]]
- [[Metropolis-Hastings correction]]
- [[SGHMC]]
- [[AMAGOLD]]
- [[AMAGOLD]]
- [[Langevin dynamics]]
