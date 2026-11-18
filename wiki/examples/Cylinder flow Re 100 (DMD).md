---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [inverse-problems]
data-origin: [simulated]
tasks: [system identification]
uses: 1
---

# Cylinder flow Re 100 (DMD)

**Summary**: 1 use in ASML (ME 697). Data: simulated. Tasks: system identification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/dynamics/05_dmd_example.ipynb`.
**Last updated**: 2026-11-18

---

## Flow past a cylinder Re=100 vorticity (DMD)

`text_books/advanced-scientific-machine-learning/book/dynamics/05_dmd_example.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: system identification (linear dynamics from snapshots); prediction
- **Technique**: exact DMD in NumPy (SVD rank r=50 of X = snapshots 0..139, X' shifted by one); modes sorted by /b/; reconstruction x(t) = sum b_j exp(omega_j t) phi_j with omega = log(lambda)/Dt, Dt=1, evaluated with jax vmap/jit
- **Data**: 151 snapshots of u, v and vorticity fields on a 449 x 199 grid; notebook uses vorticity only, clipped to +-10, cylinder not masked in data.
- **Data origin**: simulated
- **Data file**: http://dmdbook.com/DATA.zip -> DATA/FLUIDS/CYLINDER_ALL.mat (downloaded by curl in the notebook; not in data/)
- **Forward model**: Incompressible Navier-Stokes, Re=100 (precomputed in dataset); vorticity = dv/dx - du/dy.
- **Unknown dimension**: rank 50 DMD modes/eigenvalues
- **Data dimension**: n=449\*199 states, 140 snapshot pairs
- **Ground truth**: held-out snapshots beyond step 140 (text says 100, code uses 140)
- **What makes it hard**: periodic vortex shedding; DMD is linear
- **Libraries**: numpy, scipy.io.loadmat, jax, matplotlib, seaborn
- **References**: Brunton & Kutz, Data-Driven Science and Engineering, Fig. 7.3 / Ch. 7.2
- **Notes**: Replicates book Fig. 7.3. Text says data after step 100 unused but code trains on first 140. File is 55 MB with outputs.

## Related pages
- [[Examples catalogue]]
- [[Singular value decomposition]] · [[Dynamic mode decomposition]] · [[Navier-Stokes equations]]
