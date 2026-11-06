---
type: paper
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Welling, Teh 2011, ICML, eq. 4"
tags: [sampling, mcmc, bayesian]
authors: ["[[Max Welling]]", "[[Yee Whye Teh]]"]
year: 2011
venue: "ICML (Proceedings of the 28th International Conference on Machine Learning)"
file: "papers/IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf"
---

# Bayesian Learning via Stochastic Gradient Langevin Dynamics (Welling 2011)

**Summary**: Adds Gaussian noise of variance equal to the step size to a Robbins-Monro mini-batch gradient step on the log posterior, and decays the step size. The iterates start as stochastic optimization and, argued heuristically, turn into samples from the full posterior as the step size goes to zero, without Metropolis-Hastings accept/reject steps. Demonstrated on a two-parameter Gaussian mixture, Bayesian logistic regression, and ICA with natural gradients.

**Authors**: Max Welling, Yee Whye Teh · **Year**: 2011 · **File**: `papers/IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`

---

## Problem

Stochastic optimization ([[SGLD]]) scales to large datasets by using mini-batches but returns a point estimate (papers/ML/MAP) that ignores parameter uncertainty and can overfit. MCMC captures uncertainty but every iteration needs the whole dataset (p. 1-2). The paper wants Bayesian posterior sampling from mini-batch data only.

## Method

Setup (p. 2): parameters $\theta$, prior $p(\theta)$, $N$ data items $X=\{x_i\}$, posterior $p(\theta|X)\propto p(\theta)\prod_{i=1}^N p(x_i|\theta)$.

> [!definition] Stochastic optimization update (Robbins-Monro)
> At step $t$ a subset $X_t=\{x_{t1},\dots,x_{tn}\}$ gives
> $$\Delta\theta_t=\frac{\epsilon_t}{2}\Big(\nabla\log p(\theta_t)+\frac{N}{n}\sum_{i=1}^n\nabla\log p(x_{ti}|\theta_t)\Big)$$
> with step sizes satisfying
> $$\sum_{t=1}^\infty\epsilon_t=\infty,\qquad \sum_{t=1}^\infty\epsilon_t^2<\infty.$$
> Typical choice $\epsilon_t=a(b+t)^{-\gamma}$, $\gamma\in(0.5,1]$.
>
> (source: Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf, eq. 1-2, p. 2)

> [!definition] Langevin dynamics (full data)
> $$\Delta\theta_t=\frac{\epsilon}{2}\Big(\nabla\log p(\theta_t)+\sum_{i=1}^N\nabla\log p(x_i|\theta_t)\Big)+\eta_t,\quad \eta_t\sim\mathcal N(0,\epsilon).$$
> Discretization of an SDE whose equilibrium is the posterior. Can be used as a proposal and corrected by [[Metropolis-Hastings correction]]; the rejection rate goes to 0 as $\epsilon\to0$.
>
> (source: ibid., eq. 3, p. 2) See [[Langevin dynamics]].

> [!algorithm] Stochastic gradient Langevin dynamics (SGLD)
> $$\Delta\theta_t=\frac{\epsilon_t}{2}\Big(\nabla\log p(\theta_t)+\frac{N}{n}\sum_{i=1}^n\nabla\log p(x_{ti}|\theta_t)\Big)+\eta_t,\quad \eta_t\sim\mathcal N(0,\epsilon_t),$$
> with $\epsilon_t$ satisfying eq. 2. No MH accept/reject step.
>
> (source: ibid., eq. 4, p. 2) See [[SGLD]].

Why it should converge (§3, p. 3), an intuitive argument and not a proof:

- Write the true gradient $g(\theta)=\nabla\log p(\theta)+\sum_i\nabla\log p(x_i|\theta)$ and the mini-batch noise $h_t(\theta)=\nabla\log p(\theta)+\frac Nn\sum_i\nabla\log p(x_{ti}|\theta)-g(\theta)$, zero mean with finite variance $V(\theta)$ (eq. 5-6). Then eq. 4 is $\Delta\theta_t=\frac{\epsilon_t}{2}(g+h_t)+\eta_t$ (eq. 7).
- Injected noise has variance $\epsilon_t$; gradient noise has variance $(\epsilon_t/2)^2V(\theta_t)$. For large $t$, $\epsilon_t\to0$, so injected noise dominates and (7) is effectively Langevin dynamics. Discretization error also vanishes, so MH rejection probability goes to 0 and the MH step may be dropped.
- Chain is non-stationary. Fix $0<\epsilon_0\ll1$ and pick a subsequence $t_1<t_2<\dots$ with $\sum_{t=t_s+1}^{t_{s+1}}\epsilon_t\to\epsilon_0$. Over that block the total injected noise is $O(\sqrt{\epsilon_0})$, the total gradient step is $\frac{\epsilon_0}{2}g(\theta_{t_s})+O(\epsilon_0)$ (assuming Lipschitz gradients, i.i.d. mini-batch noise). So the subsequence approaches Langevin dynamics with fixed step $\epsilon_0$, hence the posterior.
- The step size must go to zero for the argument, so mixing slows over time. Authors suggest keeping $\epsilon$ constant below a critical level, or using SGLD as burn-in before switching to another MCMC (not pursued).

> [!definition] Preconditioned SGLD
> $$\Delta\theta_t=\frac{\epsilon_t}{2}M\big(g(\theta_t)+h_t(\theta_t)\big)+\eta_t,\quad\eta_t\sim\mathcal N(0,\epsilon_tM)$$
> with $M$ symmetric positive definite.
>
> (source: ibid., §4.1, p. 4)

> [!definition] Gradient-noise covariance and sampling threshold
> By the central limit theorem, with scores $s_{ti}=\nabla\log p(x_{ti}|\theta_t)+\frac1N\nabla\log p(\theta_t)$ and mean $\bar s_t$,
> $$V(\theta_t)\approx\frac{N^2}{n^2}\sum_{i=1}^n(s_{ti}-\bar s_t)(s_{ti}-\bar s_t)^\top=\frac{N^2}{n}V_s.$$
> Injected noise dominates in all directions when
> $$\frac{\epsilon_tN^2}{4n}\lambda_{\max}\big(M^{1/2}V_sM^{1/2}\big)=\alpha\ll1.$$
> Using $I_F\approx NV_s$ and $\Sigma_\theta\approx I_F^{-1}$, the step size at threshold is $\epsilon_t\approx\frac{4\alpha n}{N}\lambda_{\min}(\Sigma_\theta)$, so about $N/n$ steps (one pass over the data) are needed to traverse the posterior.
>
> (source: ibid., eq. 9-10 and text, p. 4)

> [!definition] Step-size-weighted posterior expectation
> $$\mathbb E[f(\theta)]\approx\frac{\sum_{t=1}^T\epsilon_tf(\theta_t)}{\sum_{t=1}^T\epsilon_t}.$$
> Consistent because $\sum\epsilon_t=\infty$; motivated by effective sample size per iterate being proportional to $\epsilon_t$. The plain average over-weights the correlated tail of the chain.
>
> (source: ibid., eq. 11, pp. 4-5)

ICA with natural gradients (§5.3, p. 6): the preconditioner $M_{ij,kl}=\delta_{ik}(W^\top W)_{jl}$ gives the update $W_{t+1}=W_t+\tfrac12\epsilon_tD_W+\eta_t\sqrt{W^\top W}$ (eq. 16) with $\eta_{ij,t}\sim\mathcal N(0,\epsilon_t)$ and natural-gradient direction $D_W$ in eq. 15. The reference sampler is "corrected Langevin": same proposal over the full data with constant step and an MH accept/reject (eq. 17-19). A posterior "instability" metric $I_i=\sum_j\mathrm{var}(W_{ij})\mathrm{var}(x_j)$ is introduced (eq. 21).

## Results

- **Mixture of Gaussians with tied means (§5.1, pp. 5-6)**: $\theta_1\sim\mathcal N(0,10)$, $\theta_2\sim\mathcal N(0,1)$, $x_i\sim\frac12\mathcal N(\theta_1,2)+\frac12\mathcal N(\theta_1+\theta_2,2)$; 100 points from $\theta=(0,1)$, secondary mode at $(1,-1)$. Batch size 1, 10000 sweeps, $\gamma=0.55$, $\epsilon_t$ from 0.01 to 0.0001. Estimated posterior is "very accurate" (Fig. 1). Fig. 2 shows two phases: gradient noise dominates the injected noise first, then the converse. With $\epsilon$ decaying from $10^{-2}$ to $10^{-8}$, the MH rejection probability falls to zero with step size.
- **Logistic regression (§5.2, pp. 5-6)**: a9a (32561 observations, 123 features), Laplace prior scale 1, batch size 10, 50 runs, 80/20 train/test split. Joint probability converges within at most 10 sweeps, test accuracy within less than 1 sweep (Fig. 3). No final accuracy number is given in the text.
- **ICA, artificial data (§5.3.1, pp. 6-7)**: 1000 cases, six channels (three high-kurtosis, three Gaussian). SGLD with batch 100, 500,000 iterations, $\epsilon_t=\frac4Nt^{-0.55}$. Sampling threshold $\alpha=0.1$ met after about 10,000 iterations; samples then collected when summed step size since last sample exceeds $D_0=\epsilon_t$ at that time (collecting everything made no noticeable difference). Corrected Langevin: constant $\epsilon=0.1/N$, 500,000 samples, initialised at the last SGLD estimate. SGLD mixed over several modes (combinations of the unidentifiable Gaussian components); corrected Langevin explored two modes to a lesser degree; instability index differs between samplers on the Gaussian components (Figs. 4-5). The three high-kurtosis components were stable.
- **ICA, MEG data (§5.3.2, pp. 7-8)**: first 10 of 122 channels, 17730 time points, initialised by fastICA. SGLD $\epsilon_t=\frac{0.1}{N}t^{-0.55}$ gave 500,000 samples in 800 s; corrected Langevin with constant step $1/N$ gave 100,000 samples in 9000 s. Two-dimensional marginals visually similar; instability indices similar (Fig. 6). Most stable component kurtosis 15.4, least stable 3.4 (the paper says 2 is Gaussian; this is as printed, likely a typo for 3 [unverified]).

## Limitations

As stated by the authors:
- Convergence is argued intuitively; "stronger theory providing a solid proof of convergence" is future work (p. 8).
- Step size must decay to zero for the argument, so mixing slows; fixes (constant step below a threshold, switching MCMC after burn-in) are untested (p. 3-4).
- Not a silver bullet: sampling at the threshold step size needs about $N/n$ steps, i.e. one full pass, to traverse the posterior (p. 4).
- Random-walk behaviour; HMC-type extensions and a mini-batch MH correction are listed as open (p. 8).

Wiki note: the experiments compare against corrected Langevin only, not against other posterior approximations, and give no quantitative error metric for posterior accuracy beyond visual marginals and instability indices. The paper's "infinite effective sample size" remark (p. 3) is not substantiated by a later experiment.

## Connections

- Direct ancestor of [[SG-MCMC]]; the Zhang papers below build on it: [[Cyclical SG-MCMC (Zhang 2020)]] (cyclical step-size schedule instead of the monotone decay required here), [[AMAGOLD (Zhang 2020)]] (adds an MH-style correction for stochastic gradients, using an HMC base), [[Low-precision SGLD (Zhang 2022)]] (SGLD in low-precision arithmetic).
- The HMC extension hinted in §6 became [[SGHMC]].
- Related concepts: [[Langevin dynamics]], [[Metropolis-Hastings correction]], [[SGLD]], [[SGLD]].
- Duplicates in the library: `papers/Bayesian/Welling, Teh - Baysian Learning via Stochastic Gradient Langevin Dynamics.pdf` (same paper) and a Finder alias in `papers/Stochastic Methods/`. This page's source-ref is the `papers/IFT/` copy; `areas` records all three folders.

%% refs:start %%
**Cites in this wiki**: [[RMHMC (Girolami 2011)]]
**Cited by in this wiki**: [[AMAGOLD (Zhang 2020)]], [[Cyclical SG-MCMC (Zhang 2020)]], [[IFT thermal conductivity (Alberts 2026)]], [[Low-precision SGLD (Zhang 2022)]], [[PIFT (Alberts 2023)]], [[Variational dropout (Kingma 2015)]]
%% refs:end %%

**Sources**: `papers/IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGLD]]
- [[SG-MCMC]]
- [[Langevin dynamics]]
- [[Metropolis-Hastings correction]]
- [[SGHMC]]
- [[Cyclical SG-MCMC (Zhang 2020)]]
- [[AMAGOLD (Zhang 2020)]]
- [[Low-precision SGLD (Zhang 2022)]]
