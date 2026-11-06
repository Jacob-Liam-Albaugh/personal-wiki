---
type: definition
area: stochastic
areas: [stochastic, operators]
source-ref: "Lu et al. 2021, p. 9"
---

# Karhunen-Loève expansion

> [!definition] Truncated KL expansion (as used in Lu et al. 2021, p. 9)
> $$k(t;\omega)\approx\sum_{i=1}^N\sqrt{\lambda_i}\,e_i(t)\,\xi_i(\omega)$$
> with $(\lambda_i,e_i)$ the eigenpairs of the covariance operator (eigenfunctions normalized) and $\xi_i$ i.i.d. standard Gaussians.
>
> (source: `26.10.22 - DeepONets.pdf`, p. 9)

**Intuition**: the eigenfunctions of the covariance are the optimal basis for a random field in mean square; truncation turns a random function into $N$ independent Gaussian numbers.

## Where it appears
- [[lu-2021-deeponet]] — random coefficients in Problems 5-6.
- [[alberts-2023-pift]] — Ex. 3b: 10-term KLE of a squared-exponential GP (lengthscale 0.3, >99% variance) via Nyström.
- [[alberts-2026-ift-thermal-conductivity]] — $k(u)=\exp(a_1+a_2u+\sum_{n=1}^{25}z_n\lambda_n^{1/2}\varphi_n(u))$ with exact Hermite eigenpairs of the SE kernel (eq. 10, App. A).

## Queued sources
Four KL papers in `Stochastic Methods/` (Alexanderian; Betz-Papaioannou-Straub; Deheuvels; Prakash et al.) should extend this page with the Mercer / convergence statements. Everything beyond the formula above is **[unverified]** until then.

**Sources**: `26.10.22 - DeepONets.pdf`, `IFT/Bilionis, Alberts - IFT.pdf`, `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[deeponet]]
