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

# Floor vibration activity recognition

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: classification.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-09.ipynb`.
**Last updated**: 2026-11-18

---

## Floor vibration activity recognition

`text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-09.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: time-series classification
- **Technique**: 1D CNN (Conv1d 4-8 k9 s2, 8-16 k5, dense 32), 70/15/15 split stratified by class and location, balanced accuracy
- **Data**: 4025 events, 4 sensors x 3305 samples (averaged to 661); 7 detailed classes x 115 events x 5 locations; broad classes bag/ball/jump
- **Data origin**: real
- **Data file**: Dropbox ACTIVITY_URL (not in data/)
- **Data dimension**: 4x661
- **Ground truth**: class labels
- **What makes it hard**: location-stratified splits
- **Libraries**: torch, sklearn
- **References**: Lenjani, Dyke, Bilionis, Yeum, Choi, Lund, Maghareh

## Related pages
- [[Examples catalogue]]
- [[Convolutional neural network]]
