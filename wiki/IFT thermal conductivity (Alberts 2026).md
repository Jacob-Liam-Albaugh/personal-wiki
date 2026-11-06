---
type: paper
area: ift
areas: [ift, bayesian, physics-informed]
source-ref: "Alberts, Thomas, Daryabeigi, Bilionis 2026, arXiv:2601.15427v1"
tags: [ift, bayesian, physics-informed, inverse-problems]
authors: ["[[Alex Alberts]]", "[[Akshay Jacob Thomas]]", "[[Kamran Daryabeigi]]", "[[Ilias Bilionis]]"]
year: 2026
venue: "arXiv:2601.15427v1 (Jan 2026)"
file: "IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf"
---

# IFT identification of fibrous insulation conductivity (Alberts 2026)

**Summary**: The paper identifies the temperature-dependent thermal conductivity $k(T)$ of an Opacified Fibrous Insulation (OFI) for spacecraft thermal protection systems from NASA heat-flow-meter temperature data, with no finite-element solver in the inverse loop. It applies the [[Physics-informed prior]] of [[PIFT (Alberts 2023)]] to the 1D steady heat equation, puts a log-GP prior on $k$, and samples jointly over temperature field and conductivity with [[Nested SGLD]]. The posterior is then propagated through an ABAQUS model of a HIAD-like flexible TPS for Mars and Earth entry.

**Authors**: Alex Alberts, Akshay Jacob Thomas, Kamran Daryabeigi, Ilias Bilionis · **Year**: 2026 · **File**: `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`

---

## Problem

Design of flexible TPS needs $k(T)$ of the insulation layer with uncertainty, over 300-1900 K and across gas pressures. Data are heat-flow-meter measurements of temperature through a 2.77 cm OFI sample at 0.001-760 torr; only temperatures are measured, not fluxes or conductivity. The standard route is a cubic-polynomial regression of $k(T)$, or MCMC around a finite-element forward solver. The paper states that one FE solve takes under 5 minutes and MCMC typically needs about 10,000 samples (source: `Bilionis, Alberts - IFT Thermal Conductivity.pdf`, Introduction). Training uses hot-end data up to 1367 K, and the posterior is then extrapolated to about 2000 K and compared with the reference regression.

## Method

### Physics prior

> [!definition] Heat-equation Gibbs prior
> The 1D steady heat equation with Dirichlet boundary conditions is
> $$\partial_y\big(k(u)\,\partial_y u\big)=0$$
> (eq. 1). Its Dirichlet energy and Gibbs prior are
> $$E(u;k)=\int \tfrac{k(u)}{2}\,(u_y)^2\,dy,\qquad p(u|k)=\frac{e^{-\beta E(u;k)}}{Z(k)}$$
> (eqs. 2-3). Notation: the paper's displayed eq. 2 writes $\kappa(u)$ while the text uses $k$; read both as the conductivity.
>
> (source: `Bilionis, Alberts - IFT Thermal Conductivity.pdf`, eqs. 1-3)

This is an instance of [[Physics-informed prior]], with the energy given by the [[Physics-informed prior]]. The partition function $Z(k)$ depends on $k$, so it cannot be dropped when $k$ is unknown.

### Priors and likelihood

> [!definition] Log-GP conductivity prior and likelihood
> $$\log p(k)=\mathrm{GP}\big(k\,|\,c_1+c_2u,\ s\big)$$
> (eq. 4), squared-exponential kernel $s$, with $(c_1,c_2,\ell)$ fitted by maximum likelihood. Gaussian likelihood with noise $\xi=2.5$ K (eq. 5). Joint posterior
> $$p(u,k|d)=\frac{p(d|u)\,p(u|k)\,p(k)}{p(d)}$$
> (eq. 6), with $Z(k)$ hidden inside $p(u|k)$.
>
> (source: `Bilionis, Alberts - IFT Thermal Conductivity.pdf`, eqs. 4-6)

### Parameterisation

- $u$: Fourier series with $N=20$ terms, boundary conditions satisfied a priori.
- $k$: [[Karhunen-Loève expansion]] with $M=25$ terms of the GP, using the exact Hermite eigenpairs of the squared-exponential kernel under a Gaussian measure (Appendix A), with standard-normal priors on the mean coefficients $a_1,a_2$:
$$k(u)=\exp\Big(a_1+a_2u+\sum_n z_n\lambda_n^{1/2}\varphi_n(u)\Big)$$
(eq. 10). The temperature coefficients and KLE coefficients together form $\theta$.
- Data are non-dimensionalised to $[0,1]$.

### Sampling

> [!algorithm] SGLD update and hyperparameter gradient
> SGLD (eq. 7), as written by this paper:
> $$\theta_{t+1}=\theta_t+\tfrac12\varepsilon_t\nabla\log p(\theta_t)+\eta_t,\quad\eta_t\sim\mathcal N(0,\varepsilon_t)$$
> The gradient of the log marginal over hyperparameters $\lambda$ (here the conductivity coefficients) is, as printed in eq. 13:
> $$\nabla_\lambda\log p(\lambda|d)=\mathbb E_{\theta\sim p(\theta|\lambda)}[\nabla_\lambda\beta E]-\mathbb E_{\theta\sim p(\theta|d,\lambda)}[\nabla_\lambda\beta E]-\nabla_\lambda\log p(\lambda)$$
> The energy integral is estimated with uniformly drawn collocation points $Y_i$ (eq. 14). This is the [[Nested SGLD]] of [[PIFT (Alberts 2023)]], eq. 26-27, in log-density form.
>
> (source: `Bilionis, Alberts - IFT Thermal Conductivity.pdf`, eqs. 7, 13-14)

Notation: this paper writes the SGLD noise variance as $\varepsilon_t$ with a factor $\tfrac12$ on the gradient, whereas [[PIFT (Alberts 2023)]] writes $\mathcal N(0,\sqrt{\varepsilon_t})$ without the $\tfrac12$. [[SGLD]] states the convention the wiki uses, following [[SGLD (Welling 2011)]]. See also [[SG-MCMC]].

Settings: $\beta=1000$ ([[Physics-informed prior]]); step size $\varepsilon_t=\alpha_1/(t+\alpha_2)^{\alpha_3}$ with $\alpha_2=0.01$, $\alpha_3=0.51$, $\alpha_1=0.1/\beta$; 100,000 posterior samples with 10% burn-in. The temperature field is initialised at its MAP estimate obtained with Adam (Optax). The marginal over $k$ and the conditional over $u$ are eqs. 8 and 9. The guideline for choosing $\beta$ is deferred to the authors' well-posedness paper (arXiv:2401.14224; cited, not read here).

## Results

Identification (source: `Bilionis, Alberts - IFT Thermal Conductivity.pdf`, Results and Appendices B-C):

- The temperature reconstruction is accurate across all pressures.
- The conductivity reconstruction degrades towards atmospheric pressure, which the authors attribute to gas conduction that the model omits (Appendix B).
- Extending the hot-end training range to 1900 K improves the high-pressure fit.
- Posterior uncertainty grows in the extrapolation range (above the training maximum of 1367 K).
- The method removes the FE solver from the inverse loop.
- Synthetic-data validation with an ABAQUS digital twin (Appendix C) shows accurate recovery, with the same degradation at high pressure.

Uncertainty propagation: the conductivity posterior is pushed through a 1D transient FE model in ABAQUS (custom UMATHT subroutine) of a HIAD-like layered TPS: SiC outer layer, OFI insulation, Kapton.

- Specific heat $C_p=c_1\big(1-1/\exp(c_2T)\big)$ (eq. 15): SiC $c_1=1315$, $c_2=2.57\times10^{-3}$; OFI $c_1=1302.4$, $c_2=2.73\times10^{-3}$. Densities: SiC 799, OFI 99.4, Kapton 932 kg/m$^3$. SiC emittance 0.8.
- Mars (MSL) entry: peak heat flux 70 W/cm$^2$, 25.4 mm total thickness, Kapton limit 625 K. Table 1 reports median error (MSE / max error in K): SiC 0.612/1.50; OFI-SiC 4.07/8.22; 1/4 OFI 48.3/32.9; 1/2 OFI 40.9/21.2; 3/4 OFI 57.3/12.2; Kapton 109/16.8.
- Earth (ISS return) entry: 75 W/cm$^2$, 50.8 mm. Table 2: SiC 0.949/2.74; OFI-SiC 12.7/8.57; 1/4 OFI 80.9/25.7; 1/2 OFI 313/36.1; 3/4 OFI 66.3/18.2; Kapton 15.5/9.5.
- Kapton credible-interval half-width at the final time step: about 30 K for Mars and just over 100 K for Earth.

## Limitations

As stated by the authors:

- The model needs gas conduction added for high-pressure or ground-based use.
- Uncertainty at the cold side is significant, so designers should increase insulation thickness to compensate.
- Validation is on one material and one geometry.

Wiki note: $\beta=1000$ is set rather than inferred; the paper defers justification to its cited well-posedness work, so sensitivity of the credible intervals to $\beta$ is not shown in the sections read. The Table 1-2 MSE units are not stated in the extraction; check the PDF before quoting.

## Connections

- Direct application of [[PIFT (Alberts 2023)]]: same Gibbs prior $e^{-\beta U}$, same nested SGLD, now with the unknown being a function $k(u)$ represented by a [[Karhunen-Loève expansion]] rather than a few scalar physics parameters.
- The contrast with a [[PINN]]/[[PINN]] route is argued in [[PIFT (Alberts 2023)]] (pp. 15-17); this paper cites Hao and Bilionis, "Neural information field filter", for B-PINN's poor extrapolation (cited, not read).
- The wiki's SGLD pages ([[SGLD]], [[SG-MCMC]]) trace to [[SGLD (Welling 2011)]].
- Wiki note: [[Generative priors for turbulence (Wang 2026)]] treats the same inference pattern, a prior over fields conditioned on sparse measurements through $p(x|y)\propto p(x)p(y|x)$, with a learned diffusion prior in place of a physics-derived Gibbs prior.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[PIFT (Alberts 2023)]], [[Physics-informed ML review (Karniadakis 2021)]], [[SGLD (Welling 2011)]]
%% refs:end %%

**Sources**: `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Nested SGLD]]
- [[SGLD]]
- [[SG-MCMC]]
- [[Karhunen-Loève expansion]]
- [[PINN]]
- [[PIFT (Alberts 2023)]]
- [[SGLD (Welling 2011)]]
- [[Generative priors for turbulence (Wang 2026)]]
- Wiki note: the book's placeholder "Inferring thermal conductivity" (`inverse/pdes/02_thermal.ipynb`, empty) names the same problem: [[Bayesian inverse problems]].
