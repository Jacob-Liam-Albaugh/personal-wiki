---
type: method
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Enßlin, IT & IFT, ch. 14, eqs. 346-360, pp. 149-155"
tags: [ift, bayesian, sampling, pde]
---

# Information field dynamics

**Summary**: Inference for fields that evolve in time under a dynamical law. The field prior comes from the law plus a noise field, the partition function carries a functional determinant, and information field dynamics (IFD) derives simulation schemes by evolving a posterior and matching it back to finite data.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Field prior and posterior (§14.1.1-14.1.2, pp. 149)
Background information $I$: $\partial_t\phi=F[\phi]+\xi$ (eq. 346), with $F$ possibly non-linear and non-local, and $\xi$ a noise field. Given $\xi$ and the initial field $\phi_0$ the field is determined, so

> [!definition] Dynamical field prior (eqs. 347-349)
> $$P(\phi|I)=\big|\partial_t-\partial_\phi F(\phi)\big|\;\delta\{\phi(0)-\phi_0\}\;P\big(\xi=\partial_t\phi-F[\phi]\,\big|\,I\big).$$
> The first factor is the functional determinant of the stochastic differential equation, from the change of variables $\xi\to\phi$.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §14.1.1, p. 149)

Data $d$ enter by $P(d|\phi)$ (field measurements, the initial configuration of a simulation, or simulation steps). The posterior is $P(\phi|d,I)=P(d|\phi,I)P(\phi|I)/P(d|I)$ with information energy $H=-\ln P(d,\phi|I)$ (eq. 350).

## Partition function (§14.1.3, p. 150)
For Gaussian measurement and driving noise, $P(d|\phi)=\mathcal G(d-R\phi,N)$, $P(\xi)=\mathcal G(\xi,\Xi)$:
$$Z(d,J)=\int\mathcal D\phi\,\frac{|\partial_t-\partial_\phi F|}{|2\pi\Xi|^{1/2}|2\pi N|^{1/2}}\,e^{-\frac12\{(\partial_t\phi-F[\phi])^\dagger\Xi^{-1}(\cdot)+(d-R\phi)^\dagger N^{-1}(d-R\phi)\}+J^\dagger\phi}.$$
(eq. 351; $J^\dagger\phi=\int dx\,dt\,J^*\phi$)

## Linear dynamics (§14.1.4, pp. 150-151)
For $F[\phi]=F\phi$, $(\partial_t-F)\phi=\xi$ so $\phi=G\xi$ with $G=(\partial_t-F)^{-1}$ the Green function. If $F$ is stationary, in temporal Fourier space $G_{\omega\omega'}=2\pi\delta(\omega-\omega')(i\omega-F)^{-1}$. The determinant is constant and the theory is free:
$$D=\big[\Phi^{-1}+R^\dagger N^{-1}R\big]^{-1},\quad \Phi=G\,\Xi\,G^\dagger,\quad j=R^\dagger N^{-1}d,$$
$\langle\phi\rangle=Dj$, $\langle\phi\phi^\dagger\rangle_c=D$: a Wiener filter with prior covariance $\Phi$ ([[Free theory (IFT)]]).

> [!example] Diffusion equation (p. 151)
> $F=\Delta$: $G_{(x,t)(x',t')}=\theta(t-t')\,\mathcal G(x-x',2(t-t'))$, and in Fourier space $G_{(k,\omega)}\propto(i\omega+k^2)^{-1}$, so $P_\phi(k,\omega)=P_\xi(k,\omega)/(\omega^2+k^4)$.

## Noise-free case (§14.1.5, pp. 151-152)
With $\partial_t\phi=F[\phi]$ and no data, $Z(J)=\int\mathcal D\phi\,|\partial_t-\partial_\phi F|\,\delta\{\partial_t\phi-F[\phi]\}\,e^{J^\dagger\phi}$ has two obstacles: the functional determinant and the functional delta. Auxiliary fields remove them (eq. 353): a bosonic field $\eta$ for the delta, $\delta\{\cdot\}\propto\int\mathcal D\eta\,e^{i\eta^\dagger(\partial_t\phi-F)}$, and fermionic Grassmann fields $\chi,\bar\chi$ for the determinant,
$$|A|=\int d\bar\chi\,d\chi\,e^{\bar\chi^\dagger A\chi}\qquad\text{(eq. 359)}.$$
The result (eq. 360) is a supersymmetric field theory (Parisi-Sourlas-Wu quantisation); the book states details are beyond the course.

## Information field dynamics proper (§14.2, pp. 152-155)
The idea (Fig. 19): simulations store a finite data vector $d$ that represents an unknown field.
1. Treat the field $\phi$ as unknown and the data in memory as a measurement, $d=R\phi+n$, with known $R$ and covariances $N$, $\Phi$.
2. Reconstruct the posterior $P(\phi|d)$, e.g. $\mathcal G(\phi-m,D)$.
3. Every field configuration evolves by $\phi'=\phi+\delta t\,F[\phi]+O(\delta t^2)$, so the posterior evolves too:
$$P(\phi'|d)=P(\phi|d)\Big(1-\delta t\,\frac{\partial F}{\partial\phi}\Big)\Big|_{\phi=\phi'-\delta tF[\phi']}.$$
4. Choose new data $d'$ whose posterior $P'(\phi'|d')$ best matches it, by maximising the entropy $S_B(P'|P)=-\int\mathcal D\phi'\,P'\ln(P'/P)$ over $d'$ (and, if needed, $R$, $N$, $\Phi$). The result has the form $d'=F[d]$: a simulation scheme.

The scheme thus encodes the sub-grid statistics ($\Phi$), the field-data relation ($R,N$) and the exact dynamics ($F$).

> [!theorem] Ensemble dynamics of stochastic systems (§14.2.2, pp. 154-155)
> For $\partial_t\phi=F(\phi)+\xi$ with white noise of covariance $\Xi$ and Gaussian ansatz $P(\phi|t)=\mathcal G(\phi-m_t,\Phi_t)$:
> - linear noise approximation: $\partial_tm=F(m)$, $\partial_t\Phi=F'\Phi+\Phi F'^\dagger+\Xi$ with $F'=\partial F(m)/\partial m$;
> - entropic matching: $\partial_tm=\langle F(\phi)\rangle_{\mathcal G}$, $\partial_t\Phi=\langle F'\rangle_{\mathcal G}\Phi+\Phi\langle F'\rangle_{\mathcal G}^\dagger+\Xi$, as in the book (the Gaussian averages couple $m$ and $\Phi$).
>
> The book reports (citing numerical experiments) that entropic matching beats the linear noise approximation for nonlinear stochastic systems.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §14.2.2, pp. 154-155, citing ref. [22])

Wiki note: the entropic matching update uses Gaussian averages of $F$, which is where [[Operator calculus for free theory]] gives closed forms for polynomial or exponential $F$. **[unverified]** link.

**Covered in**: Enßlin IT & IFT ch. 14 (pp. 149-155)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information field theory]] · [[Stochastic differential equation]] · [[Free theory (IFT)]]
- [[IFT state and parameter estimation (Hao 2024)]] — IFT for ODE initial-value problems (the wiki's treatment of dynamics in IFT)
- [[Gibbs free energy]] · [[Kalman filter]] · [[Wiener process]]
