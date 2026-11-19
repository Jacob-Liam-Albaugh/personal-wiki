---
type: overview
area: me697
areas: [me697, me539]
source-ref: "Examples catalogue (ASML and Intro SciML books, lab papers)"
tags: [uq, inverse-problems, sampling]
---

# Dynamical systems table

**Summary**: The space of dynamical system types, with every dynamical example from the [[Examples catalogue]] placed on it. Empty types are marked **none** so the gaps are visible. Steady-state PDE examples (Poisson, Darcy, steady heat) are left out because they have no time evolution.

**Sources**: `wiki/examples/examples.csv` (forward model column) and [[Examples catalogue#Examples from lab papers]]. Placement is a reading of each example's stated model **[unverified]**. (P) marks an example from a lab paper rather than the books.
**Last updated**: 2026-11-19

---

## Structural axes

A system is one choice from each axis.

| Axis | Type | Examples |
|---|---|---|
| Time | discrete | [[Logistic map]], [[Gaussian random walk 2D]], [[Object tracking point mass]], [[Forced damped oscillator (Kalman)]] |
| | continuous | [[Duffing oscillator examples]], [[Lorenz system examples]], [[Catalysis kinetics]], [[PK two-compartment IV bolus]], most others |
| | hybrid | **none** |
| State values | continuous | nearly all |
| | discrete | **none** (closest: [[Coal mining disasters]] counts) |
| | mixed | **none** |
| State dimension | finite | [[Duffing oscillator examples]], [[Lorenz system examples]], [[PK two-compartment IV bolus]], [[A to B to C reaction]], [[SINDy toy systems]] |
| | infinite (PDE in time) | [[Burgers 1D operator benchmark]], [[Cylinder flow Re 100 (DMD)]], [[Navier-Stokes POD (Wang-Perdikaris)]], [[Stochastic cylinder flow (multi-fidelity)]], Raissi Burgers and Navier-Stokes (P), insulation transient (P), aneurysm flow (P) |
| | infinite (delay) | **none** |
| Linearity | linear | [[Exponential decay ODE with random inputs]], [[Catalysis kinetics]], [[PK two-compartment IV bolus]], [[A to B to C reaction]], [[Cars on a bumpy road]], [[Harmonic oscillator identifiability]], [[SINDy toy systems]] (linear cases), [[Object tracking point mass]], [[Forced damped oscillator (Kalman)]], [[Treasury yield (Vasicek)]], OU process (P) |
| | nonlinear | [[Duffing oscillator examples]], [[Lorenz system examples]], [[Logistic map]], [[SINDy toy systems]] (cubic case), [[Burgers 1D operator benchmark]], cylinder flows |
| Randomness | deterministic | [[Lorenz system examples]], [[Logistic map]], [[Catalysis kinetics]], [[PK two-compartment IV bolus]], [[SINDy toy systems]] |
| | random parameters or initial condition | [[Exponential decay ODE with random inputs]], [[Duffing oscillator examples]] (polynomial chaos), [[Lorenz system examples]] (polynomial chaos), [[Stochastic cylinder flow (multi-fidelity)]], [[Cars on a bumpy road]] |
| | noise-driven | [[Duffing oscillator examples]] (stochastic), [[Treasury yield (Vasicek)]], [[Tumour growth (GBM)]], [[Brownian motion, bridge and sheet]], [[Gaussian random walk 2D]], [[Object tracking point mass]], OU process (P) |
| Noise type | additive | [[Duffing oscillator examples]] (stochastic), [[Treasury yield (Vasicek)]], [[Object tracking point mass]], OU process (P) |
| | multiplicative | [[Tumour growth (GBM)]] |
| | jump | **none** |
| Time dependence | autonomous | [[Lorenz system examples]], [[Logistic map]], [[PK two-compartment IV bolus]], [[Catalysis kinetics]] |
| | forced / time-varying | [[Duffing oscillator examples]], [[Forced damped oscillator (Kalman)]], [[Trailer on a rough road]], Cummins engine data (P), habitat thermal twin (P) |
| Memory | Markovian | all |
| | with memory (delay, fractional, integro-differential) | **none** |
| Smoothness of the rule | smooth | all |
| | non-smooth (piecewise, switched, impact) | **none** (closest: switching leak detector in the habitat testbed (P)) |
| Constraints | unconstrained | all |
| | differential-algebraic | **none** |
| Energy | conservative | [[Harmonic oscillator identifiability]], WCA dimer and LJ38 (P), granular crystal chain (P), Schrödinger (P) |
| | dissipative | [[Exponential decay ODE with random inputs]], [[Cars on a bumpy road]], [[SINDy toy systems]], [[Lorenz system examples]] |
| | driven-dissipative | [[Duffing oscillator examples]], [[Forced damped oscillator (Kalman)]] |
| Time scales | single-scale | all book examples |
| | multiscale / stiff | Bayesian reduced-order models (P) only |
| Inputs | closed | most |
| | controlled | [[Object tracking point mass]], [[Forced damped oscillator (Kalman)]], habitat testbed (P), Cummins engine (P) |
| Coupling | single unit | all book examples |
| | interacting units | WCA dimer, LJ38, granular crystal chain (all P) |
| Physics | classical | all but one |
| | quantum | Schrödinger via Raissi PINNs (P) only |

## Equation classes

| Class | Examples |
|---|---|
| Map | [[Logistic map]] |
| Stochastic difference equation | [[Gaussian random walk 2D]], [[Object tracking point mass]], [[Forced damped oscillator (Kalman)]] |
| Cellular automaton / finite-state machine | **none** |
| Markov chain | **none** |
| Jump or point process | **none** (closest: [[Coal mining disasters]], [[California earthquakes]], which are count and rate models) |
| ODE | [[Duffing oscillator examples]], [[Lorenz system examples]], [[Catalysis kinetics]], [[PK two-compartment IV bolus]], [[A to B to C reaction]], [[SINDy toy systems]], [[Lagaris benchmarks]], [[Exponential decay ODE with random inputs]], [[Cars on a bumpy road]] |
| SDE | [[Duffing oscillator examples]] (stochastic), [[Treasury yield (Vasicek)]], [[Tumour growth (GBM)]], [[Brownian motion, bridge and sheet]], OU process (P) |
| PDE in time | [[Burgers 1D operator benchmark]], [[Cylinder flow Re 100 (DMD)]], [[Navier-Stokes POD (Wang-Perdikaris)]], Raissi set (P), insulation transient (P) |
| Delay equation | **none** |
| SPDE in time | **none** (the stochastic PDE examples are steady or have random parameters only) |

## Properties

What a system does, as opposed to what it is.

| Property | Value | Examples |
|---|---|---|
| Long-run behaviour | fixed point | [[Exponential decay ODE with random inputs]], [[PK two-compartment IV bolus]], [[Cars on a bumpy road]], [[SINDy toy systems]] |
| | limit cycle | [[Cylinder flow Re 100 (DMD)]], Hopf (P) |
| | quasi-periodic | **none** |
| | chaotic | [[Lorenz system examples]], [[Logistic map]], [[Duffing oscillator examples]] (strange-attractor regime) |
| Stability | stable | the decaying systems above |
| | bistable | [[Duffing oscillator examples]] (bistable case) |
| | marginal | [[Harmonic oscillator identifiability]] |
| | unstable / growing | [[Tumour growth (GBM)]] |
| Statistical | stationary | [[Treasury yield (Vasicek)]], OU process (P) |
| | non-stationary | [[Brownian motion, bridge and sheet]], [[Gaussian random walk 2D]], [[Tumour growth (GBM)]] |
| | ergodic sampling | [[Lorenz system examples]], LJ38 (P) |
| Regularity of solutions | rough paths | [[Brownian motion, bridge and sheet]] and the SDE examples |
| | shocks | Burgers in the Raissi set (P) |

## Observation

Matters for inference, not for the system itself.

| Type | Examples |
|---|---|
| Partially observed | [[Lorenz system examples]] (partially observed SINDy), [[Catalysis kinetics]] (hidden intermediate), [[A to B to C reaction]], [[Object tracking point mass]], [[Forced damped oscillator (Kalman)]] (position only), [[Duffing oscillator examples]] (filtering), pressure leak (P) |
| Noisy | [[Lorenz system examples]] (noisy SINDy), most calibration examples |
| Sparse in time | [[A to B to C reaction]] (10 times) |

## Planned gap-filling examples

Examples chosen to fill the gaps, with real measurement data where it exists. None is built yet; each has its own page. Every link was opened by script on 2026-11-19; "resolved" means the page loaded, not that the contents were read. "Canonical" marks a well-known system that was absent from the catalogue.

| Example | Gap filled | Data | Links | Link check |
|---|---|---|---|---|
| [[Lévy-process asset returns]] | Jump process | real | [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip) | all resolved |
| [[Lévy option-smile calibration]] | Jump process | real | [CBOE delayed SPX option chain](https://cdn.cboe.com/api/global/delayed_quotes/options/_SPX.json) | all resolved |
| [[Merton and Kou jump-diffusion]] | Jump noise | real | [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [FRED SP500 (last 10 years)](https://fred.stlouisfed.org/series/SP500) | FRED SP500 (last 10 years): timed out for a script; open in a browser |
| [[Bates stochastic volatility with jumps]] | Jump noise | real | [FRED VIXCLS](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip) | FRED VIXCLS: timed out for a script; open in a browser |
| [[Intraday jumps (Bitcoin 1-minute)]] | Jump noise | real | [Binance public klines](https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/BTCUSDT-1m-2024-01-02.zip) | all resolved |
| [[Nagel-Schreckenberg traffic]] | Cellular automaton | real | [NGSIM vehicle trajectories](https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj) | all resolved |
| [[Wildfire spread cellular automaton]] | Cellular automaton | real | [NIFC fire perimeters](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-interagency-fire-perimeters/about); [Grieshop and Wikle 2023](https://arxiv.org/abs/2306.03214) | all resolved |
| [[RC thermal network (ecobee homes)]] | Hybrid / non-smooth | real | [ecobee Donate Your Data (OSTI record)](https://www.osti.gov/biblio/1854924) | all resolved |
| [[RC thermal network (NIST Net-Zero house)]] | Hybrid / non-smooth | real | [NIST Net-Zero data](https://pages.nist.gov/netzero/data.html) | all resolved |
| [[RC thermal network (Twin Houses)]] | Hybrid / non-smooth | real | [Twin Houses, Fraunhofer (CC BY-SA 4.0)](https://fordatis.fraunhofer.de/handle/fordatis/161); [Twin Houses experiment 1, Strathclyde (CC BY 4.0)](https://pureportal.strath.ac.uk/en/datasets/twin-houses-empirical-dataset-experiment-1) | all resolved |
| [[Dry friction (EMPS rig)]] | Hybrid / non-smooth | real | [EMPS benchmark](https://www.nonlinearbenchmark.org/benchmarks/emps); [nonlinear_benchmarks loader](https://github.com/MaartenSchoukens/nonlinear_benchmarks) | all resolved |
| [[Stick-slip laboratory earthquake]] | Hybrid / non-smooth | real | [LANL earthquake data on Kaggle](https://www.kaggle.com/c/LANL-Earthquake-Prediction/data); [Johnson et al. 2021](https://doi.org/10.1073/pnas.2011362118) | LANL earthquake data on Kaggle: page loads; download needs a Kaggle login; Johnson et al. 2021: publisher bot wall (403); not read |
| [[Stochastic PDEs in time]] | SPDE in time | synthetic | [torchspde](https://github.com/crispitagorico/torchspde); [OSF copy](https://osf.io/ahn6v/); [Neural SPDEs paper](https://arxiv.org/abs/2110.10249) | OSF copy: page loads, but the OSF API asks for a login; may be private |
| [[Ammonia inversion (double-well tunnelling)]] | Quantum | real | [JPL catalogue entry 17002](https://spec.jpl.nasa.gov/ftp/pub/catalog/doc/d017002.cat) | all resolved |
| [[Rabi oscillation (trapped ion)]] | Quantum | real | [Zenodo record 15797402](https://zenodo.org/records/15797402) | all resolved |
| [[Kuramoto oscillators (power grid)]] | Interacting particles | real | [Power grid frequency database](https://osf.io/by5hu/); [Rydin Gorjão et al. 2020](https://arxiv.org/abs/2006.01771) | all resolved |
| [[Flocking (schooling fish)]] | Interacting particles | real | [Schooling-fish trajectories, Zenodo 10890112](https://zenodo.org/records/10890112); [Paper](https://arxiv.org/abs/2305.17108); [Chimney swift flock (3D, 897 MB)](https://zenodo.org/record/5084183); [Jülich pedestrian archive](https://ped.fz-juelich.de/da/doku.php) | all resolved |
| [[Fermi-Pasta-Ulam-Tsingou chain]] | Interacting particles | synthetic | [Dauxois 2008 (history)](https://arxiv.org/abs/0801.1590) | all resolved |
| [[Double pendulum]] | Conservative | real | [IBM double pendulum chaotic dataset](https://developer.ibm.com/exchanges/data/all/double-pendulum-chaotic/) | IBM double pendulum chaotic dataset: landing page loads, but the project page is gone and the download host does not resolve; the data may no longer be downloadable |
| [[Two-body orbit (S2 star)]] | Conservative | real | [Gillessen et al. 2017](https://arxiv.org/abs/1611.09144); [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) | all resolved |
| [[Hénon-Heiles]] | Conservative | synthetic | none | no links |
| [[Old Faithful eruptions (Markov chain)]] | Markov chain | real | [R faithful](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/faithful.html) | all resolved |
| [[Wet and dry day rainfall chain]] | Markov chain | real | [NOAA GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) | all resolved |
| [[Ion-channel gating (hidden Markov model)]] | Markov chain | real | [R ionChannelData](https://rolfturner.r-universe.dev/ionChannelData) | R ionChannelData: page refuses scripts (403); the r-universe API confirms the package, version 0.0-3 |
| [[Earthquake counts (Poisson hidden Markov model)]] | Markov chain | real | [hmmlearn example with the counts](https://hmmlearn.readthedocs.io/en/stable/auto_examples/plot_poisson_hmm.html) | all resolved |
| [[Ising model (retina spikes)]] | Markov chain | real | [ISTA record 5562](https://research-explorer.ista.ac.at/record/5562) | all resolved |
| [[Earthquake aftershocks (Hawkes, ETAS)]] | Point process | real | [USGS ComCat API](https://earthquake.usgs.gov/fdsnws/event/1/); [R PtProcess catalogues](https://cran.r-project.org/web/packages/PtProcess/index.html); [R ETAS fitter](https://cran.r-project.org/web/packages/ETAS/index.html) | all resolved |
| [[Nicholson's blowflies (delayed logistic)]] | Delay / memory | real | [pomp blowflies](https://kingaa.github.io/manuals/pomp/html/blowflies.html) | all resolved |
| [[ENSO delayed oscillator]] | Delay / memory | real | [NOAA CPC indices](https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices) | all resolved |
| [[Mackey-Glass]] | Delay / memory | synthetic | none | no links |
| [[Generalised Langevin equation]] | Delay / memory | synthetic | none | no links |
| [[Power-grid swing dynamics]] | Differential-algebraic | real | [ISO-NE oscillation cases](https://web.eecs.utk.edu/~kaisun/Oscillation/actualcases.html) | all resolved |
| [[Tennessee Eastman process]] | Differential-algebraic | synthetic | [Rieth et al. dataset, Harvard Dataverse](https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/6C3JR1) | all resolved |
| [[Constrained pendulum and RLC circuit]] | Differential-algebraic | synthetic | none | no links |
| [[Tides (quasi-periodic)]] | Quasi-periodic | real | [NOAA CO-OPS API](https://api.tidesandcurrents.noaa.gov/api/prod/) | all resolved |
| [[Blazhko RR Lyrae stars]] | Quasi-periodic | real | [Kepler at MAST](https://archive.stsci.edu/missions-and-data/kepler) | all resolved |
| [[Sunspot cycle]] | Quasi-periodic | real | [SILSO data files](https://www.sidc.be/SILSO/datafiles) | all resolved |
| [[Torus flow, circle map and standard map]] | Quasi-periodic | synthetic | none | no links |
| [[FitzHugh-Nagumo (neuron voltage)]] | Multiscale / stiff | real | [Allen Cell Types database](https://celltypes.brain-map.org/) | all resolved |
| [[Oregonator (Belousov-Zhabotinsky reaction)]] | Multiscale / stiff | real | [Lathrop and Kostelich series (UMD)](https://complex.umd.edu/data.html) | all resolved |
| [[Stiff ODE test problems]] | Multiscale / stiff | synthetic | none | no links |
| [[Van der Pol oscillator]] | Canonical | synthetic | [Silverbox benchmark](https://www.nonlinearbenchmark.org/benchmarks/silverbox); [Circuit paper, no data](https://arxiv.org/abs/1904.11289) | all resolved |
| [[Lotka-Volterra (lynx and hare)]] | Canonical | real | [Stan CSV, 1900-1920](https://raw.githubusercontent.com/stan-dev/example-models/master/knitr/lotka-volterra/hudson-bay-lynx-hare.csv); [R pelt, 1845-1935](https://tsibbledata.tidyverts.org/reference/pelt.html); [Stan case study](https://mc-stan.org/learn-stan/case-studies/lotka-volterra-predator-prey.html) | all resolved |
| [[SIR epidemic (boarding school influenza)]] | Canonical | real | [Boarding-school influenza data](https://r-packages.io/datasets/influenza_england_1978_school); [Eyam plague 1666 (8 rows)](https://rdrr.io/cran/MultiBD/man/Eyam.html) | all resolved |
| [[Double-well SDE (ice-core record)]] | Canonical | real | [NGRIP d18O (NOAA)](https://www.ncei.noaa.gov/pub/data/paleo/icecore/greenland/summit/ngrip/gicc05-20yr.txt) | all resolved |
| [[Kuramoto-Sivashinsky]] | Canonical | synthetic | none | no links |
| [[Wave equation]] | Canonical | real | [Bowed cello string, Zenodo 1302894](https://doi.org/10.5281/zenodo.1302894); [SAGE seismic data centre](https://ds.iris.edu/ds/nodes/dmc/data/) | all resolved |
| [[Fisher-KPP (scratch assay)]] | Canonical | real | [BINNs repository](https://github.com/jlager/BINNs); [Lagergren et al. 2020](https://arxiv.org/abs/2005.13073) | all resolved |
| [[Gray-Scott]] | Canonical | synthetic | [xmorphia reference patterns](https://www.mrob.com/pub/comp/xmorphia/) | all resolved |
| [[Korteweg-de Vries]] | Canonical | synthetic | none | no links |
| [[Lorenz 96]] | Canonical | synthetic | [DAPPER](https://github.com/nansencenter/DAPPER) | all resolved |

## Gaps

- **Planned above**: every type marked **none** in the tables now has at least one planned example.
- **Planned but synthetic only**: SPDEs in time, Fermi-Pasta-Ulam-Tsingou, Hénon-Heiles, Kuramoto-Sivashinsky, Gray-Scott, Korteweg-de Vries, Lorenz 96, Mackey-Glass, generalised Langevin, the Cartesian pendulum and RLC circuit, the torus and map examples, the stiff test problems.
- **Planned with weak real data**: Van der Pol, wave equation, wildfire spread, double-well tunnelling, differential-algebraic systems (one small real dataset).

## Related pages
- [[Examples catalogue]]
- [[Planned and stub examples]]
