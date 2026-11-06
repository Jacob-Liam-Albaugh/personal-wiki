---
type: method
area: ift
areas: [ift, bayesian]
tags: [lab, sampling, mcmc, ift]
source-ref: "Alberts & Bilionis 2023, eqs. 24-27, Alg. 3, App. B; Alberts et al. 2026, eq. 13"
---

# Nested SGLD

> [!algorithm] Hyperparameter inference with two SGLD chains (Alberts & Bilionis 2023, eq. 27, Alg. 3, pp. 13-15)
> Joint posterior (eq. 24): $p(\phi,\lambda,\beta|d)=p(d|\phi)\,e^{-(H[\phi|\lambda,\beta]+H[\lambda,\beta])}/Z[\lambda,\beta]$.
> The partition function $Z[\lambda]$ depends on $\lambda$; its gradient is a prior expectation:
> $$\nabla_\lambda H(\lambda|d)=\mathbb E[\nabla_\lambda H[\phi|\lambda]\mid d,\lambda]-\mathbb E[\nabla_\lambda H[\phi|\lambda]\mid\lambda]+\nabla_\lambda H(\lambda).$$
> Estimate the first term with a data-conditioned SGLD chain, the second with a prior SGLD chain, and step $\lambda$ by SGLD.

> [!proof]
> Identity proved in App. B of paper 1.

**Settings (paper 1)**: $10^6$ warm-up steps, $T=10$ prior steps and $\tilde T=1$ posterior step per outer iteration, $n=\tilde n=1$, $q$ uniform, $\alpha_1=0.51$.

> [!failure] Multimodality
> SGLD chains mix poorly between modes; for the bimodal Allen-Cahn example paper 1 switched to HMC with energy-conserving subsampling (NumPyro, NUTS inner kernel, $b=8$).

## Where it appears
- [[PIFT (Alberts 2023)]] — introduces it.
- [[IFT thermal conductivity (Alberts 2026)]] — infers the 25 KLE coefficients of $k(u)$ and log-GP hyperparameters (eq. 13, log-density sign convention).

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`, `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SGLD]] · [[Physics-informed prior]] · [[Karhunen-Loève expansion]]
