---
type: paper
area: ift
areas: [ift, bayesian, physics-informed]
source-ref: "Alberts, Bilionis 2023, J. Comput. Phys. 486, 112100"
tags: [lab, paper, ift, bayesian, physics-informed, inverse-problems, sampling]
authors: [Alberts, Bilionis]
year: 2023
venue: "Journal of Computational Physics 486, 112100"
file: "IFT/Bilionis, Alberts - IFT.pdf"
---

# Physics-informed information field theory (Alberts 2023)

**Summary**: The paper builds a Bayesian prior over fields directly from a physical energy functional, $p(\phi) \propto e^{-\beta U[\phi]}$, using the language of [[Information field theory]]. Forward problems, inverse problems (unknown physics parameters, source terms and trust $\beta$) are solved by sampling with [[SGLD]] and a nested variant for the marginal posterior over hyperparameters. The authors show that a classical [[PINN]] is the MAP estimate of this posterior and that [[PINN]] agrees with it only under restrictive conditions.

**Authors**: Alberts, Bilionis · **Year**: 2023 · **File**: `IFT/Bilionis, Alberts - IFT.pdf`

---

## Problem

Given a PDE $\mathcal{D}[\phi]=f$ and possibly noisy, sparse data $d$, infer the field $\phi$, and possibly the physics parameters $\lambda$ and the source $f$, with uncertainty that reflects how much one trusts the PDE model. Existing PINN training gives a point estimate, and [[PINN]] posteriors need a fictitious likelihood on the residual (source: `Bilionis, Alberts - IFT.pdf`, pp. 15-17).

## Method

### Free theory and data (Gaussian/quadratic case)

The paper recalls [[Information field theory]] for a quadratic prior. Notation: the paper writes $\phi^\dagger S \phi$ for the quadratic form and $\int \mathcal{D}\phi$ for the path integral.

> [!definition] Free-theory prior and partition function
> $$p(\phi) \propto \exp\{-\tfrac12 \phi^\dagger S \phi\}$$
> $$Z[q] = \int \mathcal{D}\phi\, \exp\{-\tfrac12 \phi^\dagger S\phi + \phi^\dagger q\}$$
> $$Z[q] = C\,[\det S]^{-1/2}\exp\{\tfrac12 q^\dagger S^{-1} q\}$$
> Then $\mathbb{E}[\phi]=0$ and $\mathrm{Cov}[\phi]=S^{-1}$.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 2-6, p. 4)

> [!theorem] Linear-Gaussian posterior (Wiener filter / GP regression)
> With $d = R\phi + n$, $n\sim\mathcal N(0,N)$:
> $$\tilde S = S + R^\dagger N^{-1} R$$
> $$\tilde m = \tilde S^{-1} R^\dagger N^{-1} d = S^{-1}R^\dagger K^{-1} d$$
> $$\tilde S^{-1} = S^{-1} - S^{-1}R^\dagger K^{-1} R S^{-1}$$
> $$K = N + R S^{-1} R^\dagger$$
> The information Hamiltonian is $H[\phi|d] = \tfrac12[\phi^\dagger S\phi + (R\phi-d)^\top N^{-1}(R\phi-d)]$. Choosing $R$ as Dirac point evaluations recovers GP regression.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 8-11, pp. 5-6)

See [[Information field theory]] for the general notion.

### Physics-informed functional prior

> [!definition] Physics-informed prior and posterior
> A PDE $\mathcal D[\phi]=f$ (eq. 12) is paired with an energy $U[\phi]=\int dx\,u(x,\phi,\nabla\phi,\dots)$ (eq. 13), for example $U=\int(\mathcal D[\phi]-f)^2$ (eq. 14). The prior is
> $$p(\phi)\propto \exp\{-\beta\, U[\phi]\}$$
> optionally multiplied by $\exp\{-\tfrac12\phi^\dagger S\phi\}$ (eq. 15). The likelihood is $p(d|\phi)\propto e^{-\ell(d,R\phi)}$; for Gaussian noise $\ell=\sum_j(\phi(x_j)-d_j)^2/(2\sigma^2)$ (eq. 17). The posterior has
> $$H[\phi|d] = \ell(d,R\phi)+\beta\,U[\phi]$$
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 12-18, pp. 6-7)

$\beta$ is an inverse temperature that sets how much the model trusts the physics; see [[Physics-informed prior]]. The prior is a [[Physics-informed prior]].

### Analytic example: Klein-Gordon

For $(-\nabla^2+\alpha^2)\phi=q$ on $\mathbb R^k$ the energy is quadratic, so the free theory applies exactly.

> [!theorem] Klein-Gordon physics-informed prior and posterior
> $U[\phi]=\tfrac12[(\nabla\phi)^\dagger\nabla\phi+\alpha^2\phi^\dagger\phi]-q^\dagger\phi=\tfrac12\phi^\dagger S\phi-q^\dagger\phi$ with $S(x,x')=\delta(x-x')(-\nabla^2_{x'}+\alpha^2)$. The prior is $\phi\sim\mathcal N(S^{-1}q,\ \beta^{-1}S^{-1})$ where $S^{-1}$ is the Green's function: $(-\nabla^2+\alpha^2)S^{-1}(x,x'')=\delta(x-x'')$ (eq. 20), with Fourier form $\int \tfrac{d\xi}{(2\pi)^k}\,\tfrac{e^{-i\xi\cdot(x-x')}}{\xi^2+\alpha^2}$.
>
> Posterior (eq. 21): $p(\phi|d)=\mathcal N(\phi|\tilde m,\beta^{-1}\tilde S^{-1})$ with
> $$\tilde S = S+\beta^{-1}R^\dagger N^{-1}R$$
> $$\tilde m = m+\beta^{-1}\tilde S^{-1}R^\dagger N^{-1}(d-Rm)$$
> $$\tilde S^{-1}=S^{-1}-\beta^{-1}S^{-1}R^\dagger K^{-1}RS^{-1}$$
> $$K=N+\beta^{-1}RS^{-1}R^\dagger$$
> The covariance goes to 0 as $\beta\to\infty$ and diverges as $\beta\to0$.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 20-21, pp. 8-10)

See [[Physics-informed prior]] and [[Physics-informed prior]] (the Dirichlet energy used in the examples).

### Sampling: SGLD for forward problems

The field is parameterised as $\hat\phi(x;\theta)$ (Fourier or neural). The energy gradient is estimated without bias by importance sampling collocation points $X\sim q$.

> [!algorithm] SGLD for the physics-informed posterior
> $$\theta_{t+1}=\theta_t-\varepsilon_t\Big[\nabla_\theta \ell+\sum_{i=1}^n\frac{\nabla_\theta u(x_{ti},\cdot)}{q(x_{ti})}\Big]+\eta_t,\quad \eta_t\sim\mathcal N(0,\sqrt{\varepsilon_t})$$
> Robbins-Monro: $\sum\varepsilon_t=\infty$, $\sum\varepsilon_t^2<\infty$; $\varepsilon_t=\alpha_0/t^{\alpha_1}$, $\alpha_1\in(0.5,1]$. Data are subsampled as $\tfrac sb\sum_{i=1}^b\nabla\ell_{j_{ti}}$ (eq. 23). Algorithm 1 samples the prior, Algorithm 2 the posterior. Defaults: $n=b=1$, $\alpha_1=0.51$, prior $\alpha_0=0.1/\beta$, posterior $\alpha_0=\hat\alpha_0/\max(\beta,\sigma^{-2})$.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 22-23, Algs. 1-2, pp. 10-12)

Notation: this paper writes the injected noise as $\mathcal N(0,\sqrt{\varepsilon_t})$ and has no factor $\tfrac12$ on the gradient; see [[SGLD]] for the convention used on the method page and [[SG-MCMC]] for the family. For multimodal posteriors the paper switches to [[Nested SGLD]] with a NUTS inner kernel.

### Inverse problems: nested SGLD

With unknown physics/trust hyperparameters $\lambda$ the joint posterior is $p(\phi,\lambda,\beta|d)=p(d|\phi)\,e^{-(H[\phi|\lambda,\beta]+H[\lambda,\beta])}/Z[\lambda,\beta]$ (eq. 24). The marginal over $\lambda$ depends on the partition function $Z[\lambda,\beta]$ (eq. 25), which cannot be dropped, because it varies with $\lambda$.

> [!theorem] Gradient of the hyperparameter marginal
> $$\nabla_\lambda H(\lambda|d)=\mathbb E[\nabla_\lambda H[\phi|\lambda]\mid d,\lambda]-\mathbb E[\nabla_\lambda H[\phi|\lambda]\mid\lambda]+\nabla_\lambda H(\lambda)$$
> The first expectation is under the data-conditioned posterior of $\phi$, the second under the prior (physics only). Proof in Appendix B.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eq. 26, p. 13, App. B)

> [!algorithm] Nested SGLD
> $$\lambda_{t+1}=\lambda_t-\varepsilon_t\Big[\tfrac1{\tilde k\tilde n}\sum\sum\tfrac{\nabla_\lambda h(\text{post. samples})}{q}-\tfrac1{kn}\sum\sum\tfrac{\nabla_\lambda h(\text{prior samples})}{q}+\nabla_\lambda H(\lambda_t)\Big]+\eta_t$$
> Each outer step runs $T$ inner SGLD steps on the prior chain and $\tilde T$ on the posterior chain (Algorithm 3). Settings in the paper: 1M warm-up steps, $T=10$, $\tilde T=1$, $n=\tilde n=1$, $q$ uniform, $\alpha_1=0.51$.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eq. 27, Alg. 3, pp. 13-15)

See [[Nested SGLD]].

### Relation to PINNs and B-PINNs

> [!theorem] PINN as MAP of PIFT
> The PINN loss (eq. 28) equals the parameter-space information Hamiltonian when $r_d=s/(2\sigma^2)$ and $r_p=\beta$. A classical PINN is therefore the MAP estimate under a flat prior on $\theta$ with the partition function treated as constant. With physics parameters $\lambda$, $-\log p(\theta,\lambda|d)$ also contains $\log Z(\lambda)+H(\lambda)$ (eq. 30), which the PINN loss omits.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 28-30, pp. 15-16)

> [!theorem] B-PINN agrees with PIFT only conditionally
> B-PINN uses a fictitious zero-residual likelihood with noise $\sigma_r$ and a Gaussian prior on $\theta$ (eq. 31). Its $p(\theta|d,\lambda)$ equals the PIFT posterior only if (i) collocation points are shared, (ii) the prior is flat ($\sigma_\theta=\infty$), and (iii)
> $$\sigma_r^2=\frac{n}{2\beta}$$
> (eq. 32). Because $\sigma_r^2$ scales with $n$, B-PINN posteriors collapse as $n\to\infty$ by Bayesian asymptotics, while PIFT's spread is controlled by $\beta$ independently of $n$.
>
> (source: `Bilionis, Alberts - IFT.pdf`, eqs. 31-32, pp. 16-17)

## Results

All numerical examples are one- or two-dimensional (source: `Bilionis, Alberts - IFT.pdf`, pp. 17-24).

- **Example 1, 1D heat equation** $D\phi''+q=0$ on $[0,1]$, $\phi(0)=1$, $\phi(1)=0.1$, $D=1/4$, $q=e^{-x}$. Dirichlet energy (eq. 34), Fourier parameterisation with $K=20$ giving 39 parameters and BCs satisfied by construction (eqs. 35-36). Larger $\beta$ collapses the posterior onto a single function (Fig. 1).
- **Example 2, nonlinear** $D\phi''-\kappa\phi^3=f$, $D=0.1$, $\kappa=1$, $f=\cos 4x$, zero BCs, 40 equidistant measurements, noise level $0.012$ as printed. Two deliberate model errors: (a) source term $f(x;\gamma)=\gamma\cos 4x+(1-\gamma)e^{-x}$; (b) an energy error (eq. 39). Six values of $\gamma$ in each. A Jeffreys prior on $\beta$ is sampled as $\lambda=\log\beta$ (with $\alpha_0=10^{-3}$, $\hat\alpha_0=2$). Inferred $\beta$ trends upward with $\gamma$, so $\beta$ behaves as a model-form-error detector (Fig. 2).
- **Example 3, physics parameters** with $\beta=10^5$ fixed and Jeffreys priors on $D$, $\kappa$. In 3a $D$ is identified well, while $\kappa$ is poorly identifiable and its marginal shifts between runs, which the authors attribute to slow SGLD mixing. 100,000 iterations take about 1 s on an M1 Max. In 3b the source term $f$ is also inferred with a squared-exponential GP prior (lengthscale 0.3) and a 10-term [[Karhunen-Loève expansion]] (over 99% of variance) via the Nystrom approximation. $f$ is recovered fairly well, but the authors note this is probably due to the informative prior, and that $D$, $\kappa$ and $f$ are not jointly identifiable without prior knowledge.
- **Example 4, 2D Allen-Cahn** $\varepsilon\nabla^2\phi-\phi(\phi^2-1)+f=0$ on $[-1,1]^2$, $\varepsilon=0.01$, truth $\phi=2e^{-(x^2+y^2)}\sin(\pi x)\sin(\pi y)$, energy eq. 41. The one-parameter prior (eq. 42) is bimodal (Fig. 5). Data: 15 noisy points on each of only 3 boundaries ($\sigma^2=0.012$ as printed). 9 Fourier terms, HMCECS with NUTS inner kernel, minibatch $b=8$, 100,000 samples, $\beta=50$. The posterior is bimodal: a Gaussian mixture separates the modes, one mode recovers the true solution, and the other mode and the overall median fail (Figs. 6-8).

## Limitations

As stated by the authors (source: `Bilionis, Alberts - IFT.pdf`, p. 24):

- Analytic results exist only for quadratic operators; extending them would need perturbation theory or Feynman-diagram techniques.
- Only deterministic, time-independent problems are treated.
- No real physical system is tested.
- Fourier surrogates suffer from Gibbs phenomena at discontinuities.
- Alternatives such as variational inference are untried.
- SGLD mixes slowly and needs unimodality; multimodal posteriors need HMCECS.

Wiki note: the published values for the noise in Examples 2 and 4 (both printed as $0.012$ in the extraction) should be checked against the PDF before quoting them as standard deviations versus variances.

## Connections

- Alberts and Bilionis authored this; the same nested SGLD is reused for thermal conductivity identification in [[IFT thermal conductivity (Alberts 2026)]], with $\beta=1000$ fixed and a log-GP prior on $k(u)$.
- SGLD itself follows [[SGLD (Welling 2011)]]; see [[SGLD]] and [[SG-MCMC]].
- The Gibbs-type prior $e^{-\beta U}$ plays the role of a prior over fields that a [[Generative priors for turbulence (Wang 2026)]] style learned generative prior replaces with a data-driven $p_\theta(x)$. Both then condition on observations through $p(x|y)\propto p(x)p(y|x)$. Wiki note: this is a structural analogy drawn by the wiki, not a claim in either paper.
- Wiki note: a Finder alias named "Physics Informed Information Field Theory" exists in `Bayesian/` and `Physics Informed Architectures/`; it is likely this paper (alias not opened).
- The paper cites the follow-up on well-posedness and the choice of $\beta$ (Alberts, Bilionis, arXiv:2401.14224, cited in [[IFT thermal conductivity (Alberts 2026)]], not read here).
- Code: github PredictiveScienceLab/pift-paper-2023 (as cited in the paper).

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Information field theory]]
- [[Physics-informed prior]]
- [[SGLD]]
- [[SG-MCMC]]
- [[Nested SGLD]]
- [[Nested SGLD]]
- [[PINN]]
- [[PINN]]
- [[Karhunen-Loève expansion]]
- [[Physics-informed prior]]
- [[Physics-informed prior]]
- [[SGLD (Welling 2011)]]
- [[IFT thermal conductivity (Alberts 2026)]]
- [[Generative priors for turbulence (Wang 2026)]]
