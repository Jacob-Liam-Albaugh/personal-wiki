---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [real]
tasks: [classification]
uses: 4
---

# HMX drop-weight sensitivity

**Summary**: 4 uses in Intro SciML (ME 539). Data: real. Tasks: classification.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.1.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## HMX drop-weight explosion sensitivity

`text_books/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: classification
- **Technique**: maximum-likelihood logistic regression (sklearn penalty=None)
- **Data**: 60 drop tests, columns Height (cm; 6 levels 22.5, 25.5, 28.5, 32.0, 36.0, 40.5, 10 each) and Result (E=explode 29, N=no explosion 31). Empirical explode counts per height: 0,1,3,7,8,10 of 10. Source: L. Smith, LANL explosives orientation course, 1987.
- **Data origin**: real
- **Data file**: data/hmx_data.csv
- **Forward model**: p(E/h)=sigm(w0+w1 h)
- **Unknown dimension**: 2 weights (linear) or 3 weights (quadratic)
- **Data dimension**: 60 binary outcomes at 6 heights
- **Ground truth**: none (no reference posterior); empirical frequencies only
- **What makes it hard**: tiny, very sparse binary data with a sharp transition between ~25 and ~36 cm; test for calibrated probabilistic classification
- **Libraries**: numpy, pandas, scikit-learn, matplotlib
- **References**: L. Smith, Los Alamos National Laboratory explosives orientation course: sensitivity tests to impact, friction, spark and shock, Tech. Rep. (1987)
- **Notes**: Probability curve for h in 20-45 cm.

## HMX drop-weight explosion sensitivity

`text_books/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.2.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: classification
- **Technique**: maximum-likelihood logistic regression with PolynomialFeatures(2)
- **Data**: 60 drop tests, columns Height (cm; 6 levels 22.5, 25.5, 28.5, 32.0, 36.0, 40.5, 10 each) and Result (E=explode 29, N=no explosion 31). Empirical explode counts per height: 0,1,3,7,8,10 of 10. Source: L. Smith, LANL explosives orientation course, 1987.
- **Data origin**: real
- **Data file**: data/hmx_data.csv
- **Forward model**: p(E/h)=sigm(w0+w1 h+w2 h^2)
- **Unknown dimension**: 2 weights (linear) or 3 weights (quadratic)
- **Data dimension**: 60 binary outcomes at 6 heights
- **Ground truth**: none
- **What makes it hard**: tiny, very sparse binary data with a sharp transition between ~25 and ~36 cm; test for calibrated probabilistic classification
- **Libraries**: numpy, pandas, scikit-learn, matplotlib
- **References**: L. Smith, Los Alamos National Laboratory explosives orientation course: sensitivity tests to impact, friction, spark and shock, Tech. Rep. (1987)
- **Notes**: Quadratic feature model; same data as 16.1.

## HMX drop-weight explosion sensitivity

`text_books/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.3.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: classification with decision making
- **Technique**: expected-cost minimisation with cost matrix [ [0,1],[1,0]]; train_test_split test_size=0.33
- **Data**: 60 drop tests, columns Height (cm; 6 levels 22.5, 25.5, 28.5, 32.0, 36.0, 40.5, 10 each) and Result (E=explode 29, N=no explosion 31). Empirical explode counts per height: 0,1,3,7,8,10 of 10. Source: L. Smith, LANL explosives orientation course, 1987.
- **Data origin**: real
- **Data file**: data/hmx_data.csv
- **Forward model**: quadratic logistic model p(E/h)=sigm(w0+w1 h+w2 h^2)
- **Unknown dimension**: 2 weights (linear) or 3 weights (quadratic)
- **Data dimension**: 60 binary outcomes at 6 heights
- **Ground truth**: held-out validation set (~20 points)
- **What makes it hard**: tiny, very sparse binary data with a sharp transition between ~25 and ~36 cm; test for calibrated probabilistic classification
- **Libraries**: numpy, pandas, scikit-learn, matplotlib
- **References**: L. Smith, Los Alamos National Laboratory explosives orientation course: sensitivity tests to impact, friction, spark and shock, Tech. Rep. (1987)
- **Notes**: Also shows expected cost via einsum.

## HMX drop-weight explosion sensitivity

`text_books/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: classification diagnostics
- **Technique**: accuracy, balanced accuracy, confusion matrix on 33% validation split
- **Data**: 60 drop tests, columns Height (cm; 6 levels 22.5, 25.5, 28.5, 32.0, 36.0, 40.5, 10 each) and Result (E=explode 29, N=no explosion 31). Empirical explode counts per height: 0,1,3,7,8,10 of 10. Source: L. Smith, LANL explosives orientation course, 1987.
- **Data origin**: real
- **Data file**: data/hmx_data.csv
- **Forward model**: quadratic logistic model
- **Unknown dimension**: 2 weights (linear) or 3 weights (quadratic)
- **Data dimension**: 60 binary outcomes at 6 heights
- **Ground truth**: held-out validation set (~20 points)
- **What makes it hard**: tiny, very sparse binary data with a sharp transition between ~25 and ~36 cm; test for calibrated probabilistic classification
- **Libraries**: numpy, pandas, scikit-learn, matplotlib
- **References**: L. Smith, Los Alamos National Laboratory explosives orientation course: sensitivity tests to impact, friction, spark and shock, Tech. Rep. (1987)
- **Notes**: Exercise: degree 5. Split is unseeded so numbers vary.

## Related pages
- [[Examples catalogue]]
- [[Sensitivity analysis]]
