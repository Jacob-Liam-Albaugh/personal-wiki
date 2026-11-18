---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [real]
tasks: [dimensionality reduction, classification, clustering]
uses: 2
---

# Steel plates faults

**Summary**: 2 uses in Intro SciML (ME 539). Data: real. Tasks: dimensionality reduction, classification, clustering.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-05.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Steel plates faults, PCA before classification

`text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-05.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: binary classification, dimensionality reduction
- **Technique**: StandardScaler, LogisticRegression C=1, confusion-matrix costs, PCA 2 comps vs 90% variance
- **Data**: 1941 faults, 27 numerical features, 7 fault types; K-scratch vs other
- **Data origin**: real
- **Data file**: UCI download steel-plates-faults.zip (Faults.NNA)
- **Data dimension**: 27
- **Ground truth**: fault labels
- **What makes it hard**: information discarded by PCA
- **Libraries**: sklearn
- **References**: UCI doi 10.24432/C5J88N CC BY 4.0

## Steel plates faults, k-means on geometry

`text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-05.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: clustering
- **Technique**: KMeans k=2 n_init=20
- **Data**: same 1941 records, geometric features
- **Data origin**: real
- **Data file**: UCI download steel-plates-faults.zip
- **Data dimension**: geometry subset of 27
- **Ground truth**: fault labels
- **What makes it hard**: clusters need not match fault types
- **Libraries**: sklearn
- **References**: UCI doi 10.24432/C5J88N

## Related pages
- [[Examples catalogue]]
- [[Principal component analysis]]
