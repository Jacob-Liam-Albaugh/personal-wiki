---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [bayesian, signals]
data-origin: [simulated]
tasks: [state estimation]
uses: 2
---

# Forced damped oscillator (Kalman)

**Summary**: 2 uses in Intro SciML (ME 539). Data: simulated. Tasks: state estimation.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-06.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Position-only Kalman filter for forced damped oscillator

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-06.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: state estimation
- **Technique**: Kalman filter with correct covariances, unmeasured velocity estimate, standardised error bands
- **Data origin**: simulated
- **Forward model**: q''+2 zeta omega0 q'+omega0^2 q=u, omega0=2, zeta=0.15, dt=0.05, t in [0,20], u=0.6cos(1.2t), discretised by expm
- **Unknown dimension**: 2 (position, velocity)
- **Data dimension**: 1 per step
- **Ground truth**: simulated true state
- **What makes it hard**: velocity unobserved
- **Libraries**: numpy, scipy

## Kalman filter noise misspecification on the oscillator

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-06.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: filter diagnostics
- **Technique**: vary assumed process and measurement noise, compare RMSE, mean sd, 95% coverage
- **Data origin**: simulated
- **Forward model**: same oscillator as P2
- **Unknown dimension**: 2
- **Ground truth**: simulated true state
- **What makes it hard**: confident filter can be wrong
- **Libraries**: numpy, scipy

## Related pages
- [[Examples catalogue]]
- [[Kalman filter]]
