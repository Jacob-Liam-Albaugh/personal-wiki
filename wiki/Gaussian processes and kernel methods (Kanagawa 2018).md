---
type: paper
area: gp
areas: [gp, math]
source-ref: "Kanagawa, Hennig, Sejdinovic, Sriperumbudur 2018, arXiv review, Props 3.6-3.12, Thms 4.1-4.12, Props 6.1-6.3"
tags: [gp, bayesian, ml]
authors: ["[[Motonobu Kanagawa]]", "[[Philipp Hennig]]", "[[Dino Sejdinovic]]", "[[Bharath K. Sriperumbudur]]"]
year: 2018
venue: "arXiv review, 10 Jul 2018"
file: "papers/Guassian Processes/Kanagawa, Hennig, Sejdinovic, Sriperumbudur - GPs & Kernel Methods.pdf"
---

# Gaussian processes and kernel methods (Kanagawa 2018)

**Summary**: A review that matches up the Bayesian view ([[Gaussian process]]) and the frequentist view ([[Kernel methods]], [[RKHS]]) of the same positive definite kernel. GP posterior mean equals kernel ridge regression; posterior standard deviation equals a worst-case error; GP draws miss the RKHS but lie in a slightly larger "power" space; convergence rates, MMD and Bayesian quadrature match too.

**Authors**: Motonobu Kanagawa, Philipp Hennig, Dino Sejdinovic, Bharath K. Sriperumbudur · **Year**: 2018 · **File**: `papers/Guassian Processes/Kanagawa, Hennig, Sejdinovic, Sriperumbudur - GPs & Kernel Methods.pdf`

---

## Regression and interpolation (§3)

GP regression with prior $f\sim GP(0,k)$ and noise $N(0,\sigma^2)$ gives a posterior GP (eqs. 16-17, pp. 15-17). Kernel ridge regression (KRR) solves
$$\hat f=\arg\min_{f\in H_k}\tfrac1n\sum_i (f(x_i)-y_i)^2+\lambda\|f\|^2_{H_k}.$$

> [!theorem] KRR solution (Thm 3.4, representer theorem)
> For $\lambda>0$ the minimiser is unique and
> $$\hat f(x)=k_{xX}(k_{XX}+n\lambda I)^{-1}Y.$$
>
> (source: p. 19, eqs. 24-25)

> [!theorem] GP = KRR (Prop 3.6)
> The GP posterior mean equals the KRR estimator when
> $$\sigma^2=n\lambda.$$
> So the posterior mean lies in $H_k$. Noise variance acts as the regulariser: bigger noise assumes a smoother latent $f$ than the observed process (Remarks 3.8-3.9).
>
> (source: pp. 21-22)

Noise-free case: GP interpolation $\bar m(x)=k_{xX}k_{XX}^{-1}f_X$ is the minimum-norm interpolant in $H_k$ (Thm 3.5, Prop 3.7, pp. 20-22). "Smoothest function through the data" (Remark 3.6). Small "jitter" regularisation is for numerics only (Remarks 3.4, 3.7).

## Error: average case = worst case (§3.4-3.5)

> [!theorem] Posterior variance as worst-case error (Prop 3.10, noise free)
> $$\sqrt{\bar k(x,x)}=\sup_{\|f\|_{H_k}\le1}\Big|\sum_i w_i(x)f(x_i)-f(x)\Big|,\quad w=k_{XX}^{-1}k_{Xx}.$$
> Consequence (Cor 3.11):
> $$(\bar m(x)-f(x))^2\le\|f\|^2_{H_k}\,\bar k(x,x).$$
>
> (source: p. 26)

With noise (Prop 3.8, p. 24) the same holds for $\sqrt{\bar k(x,x)+\sigma^2}$ over the unit ball of $H_{k^\sigma}$, $k^\sigma=k+\sigma^2\delta$: the worst case is more pessimistic by the unfittable noise. Prop 3.12 (p. 27): the weights minimise noise-free worst-case error squared plus $\sigma^2\|w\|^2$, so $\sigma^2$ is a ridge penalty on weights.

## Do GP draws lie in the RKHS? (§4)

Answer: no (almost surely, if $H_k$ is infinite dimensional), but nearly.

- Mercer (Thm 4.1, p. 30): $k(x,x')=\sum_i\lambda_i\phi_i(x)\phi_i(x')$ for the eigensystem of the [[Kernel integral operator]] on a compact space. The expansion depends on the measure $\nu$; $k$ does not (Remark 4.1).
- Mercer representation (Thm 4.2, p. 30): $\{\lambda_i^{1/2}\phi_i\}$ is an orthonormal basis of $H_k$.
- [[Karhunen-Loève expansion]] (Thm 4.3, p. 31):
$$f(x)=\sum_i z_i\lambda_i^{1/2}\phi_i(x),\quad z_i\sim N(0,1)\ \text{independent}.$$
Same basis as $H_k$, but coefficients with variance one, so $\|f\|_{H_k}^2=\sum z_i^2=\infty$. Used numerically in [[Reduced-rank GPs (Greengard 2022)]].
- Driscoll zero-one law (Thm 4.9, p. 33): for $H_k\subset H_r$ and $f\sim GP(m,k)$ with $m\in H_r$, a version of $f$ lies in $H_r$ with probability 1 if the inclusion $H_k\to H_r$ is Hilbert-Schmidt, and with probability 0 otherwise. Corollary 4.10: $f\notin H_k$ a.s. if $H_k$ is infinite dimensional. Example 4.1: Brownian motion has RKHS equal to the first-order Sobolev space and is not in it (p. 35).
- Powers of an RKHS (Def 4.11, Thm 4.12, pp. 35-36): $H_k^\theta$ has basis $\lambda_i^{\theta/2}\phi_i$; it sits between $H_k$ and $L^2(\nu)$. A version of $f$ lies in $H_k^\theta$ a.s. iff
$$\sum_i\lambda_i^{1-\theta}<\infty.$$
- Squared exponential (Cor 4.13, p. 37): draws lie in $H_k^\theta$ for every $\theta<1$, "infinitesimally larger" than $H_k$. Matérn (Cor 4.15): draws are about $d/2$ less smooth than the RKHS (Remark 4.14, p. 38).

## Convergence (§5)

- GP posterior contraction in Sobolev spaces (Thm 5.1, p. 39): $O(n^{-2\min(\alpha,\beta)/(2\alpha+d)})$, best at $\alpha=\beta$: $n^{-2\beta/(2\beta+d)}$, minimax optimal.
- KRR (Thm 5.2, p. 40) with $\lambda_n=cn^{-2s/(2\beta+d)}$ reaches the same rate. With $\sigma^2$ fixed in $n$, $\lambda_n=c/n$ (Cor 5.3, Remark 5.5, p. 41): the two results are the same statement.
- Posterior variance (power function) contracts with local fill distance, dimension and smoothness: $\bar k(x,x)=O(n^{-b(2s-d)})$ for fill distance $O(n^{-b})$ (Cor 5.5, p. 42). On a grid this is $O(n^{-(2s/d-1)})$: curse of dimensionality (Remark 5.8). Relevant to [[Active learning]]-style design.

## MMD, quadrature, other links (§6)

- Kernel mean $\mu_P=\int k(\cdot,x)\,dP$; maximum mean discrepancy is the RKHS distance between means (eqs. 67-68, pp. 43-44), with $\mathrm{MMD}^2=E[k(x,x')]-2E[k(x,y)]+E[k(y,y')]$ (Remark 6.3).
- Prop 6.1 (p. 45): worst-case squared error over the unit ball equals the GP average squared error,
$$\mathrm{MMD}^2(P,Q)=E_{f\sim GP(0,k)}\big[(Pf-Qf)^2\big].$$
- Kernel quadrature weights $w=k_{XX}^{-1}\mu_X$ (eq. 70) coincide with the Bayesian quadrature posterior mean; the posterior variance equals the squared MMD of the rule (Prop 6.3, pp. 46-48). Ridge-regularised weights $(k_{XX}+n\lambda I)^{-1}\mu_X$ handle misspecification (eq. 77).
- Shrinkage kernel-mean estimator (eqs. 80-81) has a GP interpretation with a powered kernel $k^\theta$ (pp. 49-51). The paper continues with HSIC (not summarised here).

## Connections

- Wiki note: the same kernel/RKHS picture underlies the weight-space view in [[Reduced-rank GPs (Greengard 2022)]] and the kernel design in [[Duvenaud thesis (Duvenaud 2014)]].
- Wiki note: for surrogate use ([[Surrogate model]], [[Multi-fidelity Gaussian process]]) the useful consequences are that noise level equals regularisation, and $\sqrt{\bar k}$ is a certified error bar for functions of bounded RKHS norm.
- [[Random features model]] approximates the same kernel with finite features.

**Sources**: `papers/Guassian Processes/Kanagawa, Hennig, Sejdinovic, Sriperumbudur - GPs & Kernel Methods.pdf` (§2-6 read; §7, HSIC and appendices not read in detail).
**Last updated**: 2026-11-06

---

## Related pages
- [[Gaussian process]] · [[Kernel methods]] · [[RKHS]] · [[Kernel integral operator]] · [[Karhunen-Loève expansion]]
- [[Kernel composition]] · [[Multi-fidelity Gaussian process]] · [[Random features model]] · [[Surrogate model]] · [[Active learning]]
- [[Reduced-rank GPs (Greengard 2022)]] · [[Duvenaud thesis (Duvenaud 2014)]]
