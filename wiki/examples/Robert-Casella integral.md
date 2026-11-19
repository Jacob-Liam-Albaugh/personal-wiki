---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [uq]
data-origin: [analytic]
tasks: [uncertainty propagation]
uses: 7
---

# Robert-Casella integral

**Summary**: 7 uses in Intro SciML (ME 539). Data: analytic. Tasks: uncertainty propagation.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/08 - The Monte Carlo Method for Estimating Expectations/hands-on-08.3.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/08 - The Monte Carlo Method for Estimating Expectations/hands-on-08.3.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo expectation
- **Technique**: running sample mean, N=100, law of large numbers
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)
- **Notes**: Also contains a generic synthetic LLN demo (skipped as a toy).

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/08 - The Monte Carlo Method for Estimating Expectations/hands-on-08.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo variance
- **Technique**: sample-average variance estimator, N=100
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)
- **Notes**: Compares to V[g]~1.093.

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/09 - Monte Carlo Estimates of Various Statistics/hands-on-09.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo CDF estimation
- **Technique**: empirical CDF (statsmodels ECDF) with N=10,100,10000; p(1<=Y<=3)
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/09 - Monte Carlo Estimates of Various Statistics/hands-on-09.2.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo PDF estimation
- **Technique**: histograms with 100 bins, N=100,1000,10000
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/09 - Monte Carlo Estimates of Various Statistics/hands-on-09.3.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo quantile estimation
- **Technique**: empirical quantiles 0.5, 0.025, 0.975 from 10000 samples
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/10 - Quantify Uncertainty in Monte Carlo Estimates/hands-on-10.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo error quantification
- **Technique**: repeated MC estimates to visualise estimator spread
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)

## Robert-Casella 1D oscillatory integral

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/10 - Quantify Uncertainty in Monte Carlo Estimates/hands-on-10.3.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Monte Carlo error quantification
- **Technique**: CLT-based running +/-2 sigma/sqrt(N) interval, N=100
- **Data**: No data; X~U([0,1]) sampled with numpy. g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093
- **Data origin**: analytic
- **Forward model**: g(x)=(cos(50x)+sin(20x))^2 with X~U(0,1); E[g]=0.965, V[g]~1.093. Plain numpy, not JAX.
- **Unknown dimension**: 1
- **Data dimension**: 1 scalar output
- **Ground truth**: E[g]=0.965 and V[g]~1.093 stated by notebook
- **What makes it hard**: highly oscillatory integrand, moderate MC variance; small known-answer test for MC estimators
- **Libraries**: numpy, matplotlib, statsmodels, scipy.stats
- **References**: Robert and Casella, Monte Carlo Statistical Methods (2004), Example 3.4 (cite key robert_monte_2004)

## Related pages
- [[Examples catalogue]]
