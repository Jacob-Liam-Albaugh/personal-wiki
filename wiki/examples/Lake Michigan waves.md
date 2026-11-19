---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [uq]
data-origin: [real]
tasks: [distribution fitting]
uses: 1
---

# Lake Michigan waves

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: distribution fitting.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-02.ipynb`.
**Last updated**: 2026-11-18

---

## Lake Michigan wave height and period dependence

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-02.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: joint distribution / dependence
- **Technique**: marginals and dependence analysis (copula-style)
- **Data**: 5046 rows; timestamp_utc, Hs_m (0.02-3.09), Tavg_s (2.2-6.2)
- **Data origin**: real
- **Data file**: data/homework/hw02_noaa_45007_2023_hourly.csv
- **Data dimension**: 2 variables
- **What makes it hard**: correlated heavy-tailed marginals
- **Libraries**: pandas, scipy
- **References**: NOAA NDBC 45007h2023; EPRI 1024637 (2011) App. A Eq A-7

## Related pages
- [[Examples catalogue]]
