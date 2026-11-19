---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [real]
tasks: [dimensionality reduction]
uses: 2
---

# SVD image compression

**Summary**: 2 uses in ASML (ME 697). Data: real. Tasks: dimensionality reduction.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/02_svd.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## SVD image compression

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/02_svd.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: dimensionality reduction
- **Technique**: truncated SVD reconstruction at several ranks; k chosen by cumulative sum(s^2) >= 0.998
- **Data**: Grayscale photo, 1798 x 2400 pixels.
- **Data origin**: real
- **Data file**: neom-DMGDdksVoWI-unsplash.jpg (in the same folder)
- **Forward model**: none
- **Unknown dimension**: rank k
- **Data dimension**: 1798 x 2400
- **Ground truth**: original image
- **Libraries**: numpy, matplotlib
- **Notes**: Listed ks end at 682, whose relation to the image shape is unclear. Near-duplicate of the other SVD notebook (differs by curl path).

## SVD image compression

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/reduced_order_modeling/01_svd.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: dimensionality reduction
- **Technique**: truncated SVD reconstruction at several ranks; k chosen by cumulative sum(s^2) >= 0.998
- **Data**: Grayscale photo, 1798 x 2400 pixels.
- **Data origin**: real
- **Data file**: neom-DMGDdksVoWI-unsplash.jpg (in the same folder)
- **Forward model**: none
- **Unknown dimension**: rank k
- **Data dimension**: 1798 x 2400
- **Ground truth**: original image
- **Libraries**: numpy, matplotlib
- **Notes**: Listed ks end at 682, whose relation to the image shape is unclear. Near-duplicate of the other SVD notebook (differs by curl path).

## Related pages
- [[Examples catalogue]]
- [[Singular value decomposition]] · [[Image compression]]
