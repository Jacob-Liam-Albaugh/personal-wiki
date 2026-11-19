---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [bayesian, inverse-problems]
data-origin: [synthetic]
tasks: [inverse problem and calibration, system identification]
uses: 1
---

# Harmonic oscillator identifiability

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: inverse problem and calibration, system identification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/odes/02_identifiability.ipynb`.
**Last updated**: 2026-11-18

---

## Structural identifiability: harmonic oscillator m x''=kx

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/odes/02_identifiability.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Bayesian inverse problem / identifiability
- **Technique**: NUTS (blackjax window_adaptation, dense mass, 1000 warmup, 1000 samples); priors m~U(1,2), k~U(0.5,3), sigma=exp(0.5 xi-1); fix by reparameterising omega^2=k/m ~U(0.25,3)
- **Data**: 50 times on linspace(0,10,50), 1D position; truth m=1.5,k=1.5,sigma=0.05; x(0)=1,v(0)=0
- **Data origin**: synthetic
- **Forward model**: m x''=k x as written in notebook; analytic solution with omega=sqrt(k/m)
- **Unknown dimension**: 3 (m,k,sigma); 2 after reparameterisation
- **Data dimension**: 50
- **Ground truth**: true parameters known
- **What makes it hard**: Structural non-identifiability: ridge m=k, random-walk traces
- **Libraries**: jax, blackjax, arviz
- **Notes**: Pair plot shows the ridge; reparameterised posterior well behaved.

## Related pages
- [[Examples catalogue]]
- [[NUTS]] · [[Markov chain Monte Carlo]] · [[Identifiability]]
