---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [sampling, mcmc, bayesian, inverse-problems]
data-origin: [synthetic]
tasks: [sampling, inverse problem and calibration]
uses: 1
---

# Cars on a bumpy road

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: sampling, inverse problem and calibration.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/hbayes/02_hbayes_example.ipynb`.
**Last updated**: 2026-11-18

---

## Cars on a bumpy road (hierarchical Bayes)

`text_books/advanced-scientific-machine-learning/book/inverse/hbayes/02_hbayes_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Hierarchical Bayesian inverse problem + predictive forecast
- **Technique**: numpyro model -> blackjax NUTS; 3 chains, 1000 warmup, 1000 samples, step 0.001, identity mass, tempering annealing (const 200 / cosine 600); centered vs non-centered flag; manual bad-chain removal; R-hat; prediction of P(new bump x0~N(5,1) drives displacement below -3) vs threshold 0.1
- **Data**: N_INDIVIDUALS=100, N_TIMES=20 on linspace(0,4,20), noise 0.1 known; y shape (20,100)=2000. Truth: x0=3.5; p~MVN([-1.5,1.0],[ [0.1,0.07],[0.07,0.1]]), zeta=exp(p0), omega=exp(p1+0.3cos(2(p1-1))) (non-Gaussian, misspecified population)
- **Data origin**: synthetic
- **Forward model**: Damped oscillator x''+2 zeta x'+omega^2 x=0, x(0)=x0, x'(0)=0; analytic solution (lax.switch over under/critical/over-damped)
- **Unknown dimension**: 205 = 4 population + 1 x0 + 2x100 individual
- **Data dimension**: 2000 = 20 times x 100 cars
- **Ground truth**: true generating parameters known
- **What makes it hard**: Funnel geometry of hierarchical model; model misspecification; high dimension
- **Libraries**: jax, numpyro, blackjax, arviz
- **Notes**: Priors in code: mu_zeta~N(-2,1) (text says N(-1,1)), tau~Exp(10), mu_omega~N(0,0.5), x0~U(0,5). Text says 30 cars/20 snapshots, code uses 100; threshold -3 in code vs -2 in one text place. Questions: N=10, T=8, noise 0.3.

## Related pages
- [[Examples catalogue]]
- [[NUTS]] · [[Hierarchical Bayesian model]]
