---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [real]
tasks: [classification]
uses: 1
---

# Handwritten digits (sklearn)

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: classification.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.5.ipynb`.
**Last updated**: 2026-11-18

---

## Handwritten digits (sklearn load_digits)

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/16 - Classification/hands-on-16.5.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: multi-class classification
- **Technique**: unregularised logistic regression (max_iter=2000), predict_proba, classification report and confusion matrix
- **Data**: 8x8 grayscale digit images flattened to 64 features, 10 classes (0-9); sklearn digits set (UCI optical recognition of handwritten digits; 1797 samples, count from sklearn, not printed in source). 50/50 shuffled train/test split.
- **Data origin**: real
- **Data file**: sklearn.datasets.load_digits (built in)
- **Forward model**: multinomial logistic regression p(y=k/x)=softmax_k(w_k^T x), 64 features + intercept
- **Unknown dimension**: 10x64 weights + 10 intercepts
- **Data dimension**: 64 features per sample
- **Ground truth**: held-out test half
- **What makes it hard**: easy standard benchmark
- **Libraries**: scikit-learn, matplotlib
- **References**: follows scikit-learn plot_digits_classification example
- **Notes**: Unseeded split.

## Related pages
- [[Examples catalogue]]
