---
type: overview
area: me697
areas: [me697, me539]
source-ref: "Examples catalogue (ASML and Intro SciML books, lab papers)"
tags: [dynamical-systems, uq, inverse-problems, sampling]
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

Examples chosen to fill the gaps, with real measurement data where it exists. None is built yet. Links were collected by web search on 2026-11-19; dataset contents, licences and the papers named are **[unverified]** unless the note says the file was read. "Synthetic only" means no real measurement was found.

### Gap rows

| Gap filled | Example | Real data | Note |
|---|---|---|---|
| Jump process | Lévy-process asset returns (variance gamma, normal inverse Gaussian, CGMY) | [Kenneth French daily market factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip) (daily US market return from 1926, file read) | Fit to returns shows fat tails and skew. Model papers: Madan, Carr and Chang 1998; Carr, Geman, Madan and Yor 2002. |
| Jump process | Lévy option-smile calibration | [CBOE delayed SPX option chain](https://cdn.cboe.com/api/global/delayed_quotes/options/_SPX.json) | Live snapshot only, no history, so not reproducible. No free option-surface history was found. |
| Jump noise | Merton and Kou jump-diffusion on index returns | Kenneth French series above; [FRED SP500](https://fred.stlouisfed.org/series/SP500) (last 10 years, redistribution restricted) | Jump-diffusion is an SDE plus compound-Poisson jumps. |
| Jump noise | Bates stochastic volatility with jumps | [FRED VIXCLS](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS) (daily VIX from 1990, file read) | VIX as a volatility proxy. Papers: Bates 1996; Eraker, Johannes and Polson 2003. |
| Jump noise | Intraday jumps | [Binance 1-minute BTCUSDT candles](https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/BTCUSDT-1m-2024-01-02.zip) | Only login-free intraday source found. Licence not checked. |
| Cellular automaton | Nagel-Schreckenberg traffic model | [NGSIM vehicle trajectories](https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj) (11.85 million rows, US-101 and I-80, CC BY-SA 3.0) | Real traffic against a well-known cellular automaton. Replaces Rule 30 and Game of Life. |
| Cellular automaton | Wildfire spread | [NIFC fire perimeters](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-interagency-fire-perimeters/about) | Weak: final perimeters only, no time-resolved spread. Bayesian model: [Grieshop and Wikle 2023](https://arxiv.org/abs/2306.03214). |
| Hybrid / non-smooth | RC thermal network with on/off thermostat | [ecobee Donate Your Data, 1,000 homes, 2017](https://www.osti.gov/biblio/1854924) (5-minute data) | Best fit for a switched RC model. Column names and login requirement not confirmed. |
| Hybrid / non-smooth | RC thermal network, single house | [NIST Net-Zero house](https://pages.nist.gov/netzero/data.html) (1-minute data, about 400 channels, open) | Best documented. Has HVAC on/off status flags. |
| Hybrid / non-smooth | RC thermal network, controlled experiment | [Twin Houses, Fraunhofer](https://fordatis.fraunhofer.de/handle/fordatis/161) (CC BY-SA 4.0); [Strathclyde copy](https://pureportal.strath.ac.uk/en/datasets/twin-houses-empirical-dataset-experiment-1) (CC BY 4.0) | Two matched test houses. Paper: Strachan et al. 2015. |
| Hybrid / non-smooth | Dry friction (Coulomb, stick-slip) | [EMPS positioning rig](https://www.nonlinearbenchmark.org/benchmarks/emps), loader in [nonlinear_benchmarks](https://github.com/MaartenSchoukens/nonlinear_benchmarks) | Real friction-identification benchmark with a reference model (Janot, Gautier and Brunot 2019). |
| Hybrid / non-smooth | Stick-slip laboratory earthquake | [LANL earthquake data on Kaggle](https://www.kaggle.com/c/LANL-Earthquake-Prediction/data) | Needs a Kaggle login. A signal to time-to-failure task, not a friction-law fit. Paper: [Johnson et al. 2021](https://doi.org/10.1073/pnas.2011362118). |
| SPDE in time | Stochastic heat, stochastic Allen-Cahn, stochastic Burgers | Synthetic only. [torchspde](https://github.com/crispitagorico/torchspde) ([OSF copy](https://osf.io/ahn6v/)) | Standard benchmark code. Paper: [Neural SPDEs](https://arxiv.org/abs/2110.10249). The heat case extends [[Stochastic 1D heat equation]]. |
| Quantum | Double-well tunnelling (ammonia inversion) | [JPL catalogue entry 17002](https://spec.jpl.nasa.gov/ftp/pub/catalog/doc/d017002.cat) (1,716 inversion lines) | Spectral lines, not time-domain data. Fit the well to the doublet splittings. |
| Quantum | Two-level Rabi oscillation | [Trapped-ion sideband Rabi data, Zenodo 15797402](https://zenodo.org/records/15797402) (CC BY 4.0, 733 KB) | Best found. No superconducting-qubit or NMR Rabi data located. |
| Interacting particles | Kuramoto oscillators | [Power grid frequency database](https://osf.io/by5hu/) (17 sites, 1 Hz and faster) | The grid is a second-order Kuramoto network. Paper: [Rydin Gorjão et al. 2020](https://arxiv.org/abs/2006.01771). No metronome data deposit found. |
| Interacting particles | Vicsek or Cucker-Smale flocking | [Schooling-fish trajectories, Zenodo 10890112](https://zenodo.org/records/10890112) (8 and 39 fish, CC BY 4.0) | Paper: [arXiv 2305.17108](https://arxiv.org/abs/2305.17108). Alternatives: [chimney swift flock](https://zenodo.org/record/5084183) (3D, 897 MB), [Jülich pedestrian archive](https://ped.fz-juelich.de/da/doku.php). |
| Interacting particles | Fermi-Pasta-Ulam-Tsingou chain | Synthetic only | No measurement exists. Background: [Dauxois 2008](https://arxiv.org/abs/0801.1590). Related to the granular crystal chain (P). |
| Conservative | Double pendulum | [IBM double pendulum chaotic dataset](https://developer.ibm.com/exchanges/data/all/double-pendulum-chaotic/) | Real video-tracked data, but the project page returned 404. Check the download works before using. |
| Conservative | Two-body (Kepler) orbit | S2 star around Sgr A*: [Gillessen et al. 2017](https://arxiv.org/abs/1611.09144) (tables in the paper); [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) | S2 is 25 years of real astrometry. Horizons is computed ephemerides, usable as ground truth. |
| Conservative | Hénon-Heiles | Synthetic only | No measurement exists. Also fills the quasi-periodic and chaotic mix in one system. |
| Markov chain | Two-state chain on geyser eruptions | [Old Faithful, R faithful](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/faithful.html) (272 eruptions) | Threshold at about 3 minutes for a plain chain, or fit a two-state hidden Markov model. |
| Markov chain | Wet and dry day rainfall chain | [NOAA GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) | Realistic plain Markov chain. Pick one station; no canonical file found. |
| Markov chain | Hidden Markov model of ion-channel gating | [R ionChannelData](https://rolfturner.r-universe.dev/ionChannelData) (patch-clamp currents, about 200,000 points per series) | Hidden discrete state under Gaussian noise. Not on CRAN; licence not read. |
| Markov chain | Poisson hidden Markov model of earthquake counts | [Annual M7+ counts, 1900-2006](https://hmmlearn.readthedocs.io/en/stable/auto_examples/plot_poisson_hmm.html) (107 values) | Tiny. Extends [[California earthquakes]]. Zucchini and MacDonald 2009. |
| Markov chain | Ising model (pairwise maximum entropy) | [Salamander retina recordings, 160 cells](https://research-explorer.ista.ac.at/record/5562) (binary spikes in 20 ms bins, CC0) | Real binary spin patterns. Paper: Tkačik et al. 2014. No real magnetisation data found. |
| Point process | Hawkes / ETAS on earthquakes | [USGS ComCat API](https://earthquake.usgs.gov/fdsnws/event/1/) (any region and window); bundled catalogues in [R PtProcess](https://cran.r-project.org/web/packages/PtProcess/index.html) | Self-exciting aftershocks. Reference fitter: [R ETAS](https://cran.r-project.org/web/packages/ETAS/index.html). Extends [[California earthquakes]]. |
| Delay / memory | Delayed logistic (Nicholson's blowflies) | [pomp blowflies](https://kingaa.github.io/manuals/pomp/html/blowflies.html) (adult counts, Nicholson 1957) | The standard delay-model data. Paper: Wood 2010. |
| Delay / memory | ENSO delayed oscillator | [NOAA Niño indices](https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices) (monthly from 1982, about 540 points) | Model: Suarez and Schopf 1988. |
| Delay / memory | Mackey-Glass | Synthetic only | The motivating blood-count data (cyclical neutropenia) has no machine-readable deposit. |
| Delay / memory | Generalised Langevin equation | Synthetic only | No tracer or optical-trap trajectory deposit found. |
| Differential-algebraic | Power-grid swing dynamics | [ISO-NE oscillation cases](https://web.eecs.utk.edu/~kaisun/Oscillation/actualcases.html) (6 real phasor-measurement cases) | Best real option. Sampling rate not stated. |
| Differential-algebraic | Tennessee Eastman process | [Rieth et al. dataset](https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/6C3JR1) (simulated, 20 faults) | Standard benchmark, but simulated, not measured. |
| Differential-algebraic | Cartesian pendulum, RLC circuit | Synthetic only | Textbook constraint examples. |
| Quasi-periodic | Tides | [NOAA CO-OPS API](https://api.tidesandcurrents.noaa.gov/api/prod/) (6-minute and hourly water level) | Clean sum of incommensurate frequencies. One month of 6-minute data per call. |
| Quasi-periodic | Blazhko RR Lyrae stars | [Kepler light curves at MAST](https://archive.stsci.edu/missions-and-data/kepler) | Two-frequency stellar pulsation. Candidate stars not confirmed. |
| Quasi-periodic | Sunspot cycle | [SILSO sunspot number](https://www.sidc.be/SILSO/datafiles) (monthly from 1749) | Licence is CC BY-NC 4.0. |
| Quasi-periodic | Torus flow, circle map, standard map | Synthetic only | Cardiac phase-locking results (Guevara, Glass and Shrier 1981) exist as figures only. |
| Multiscale / stiff | FitzHugh-Nagumo on neuron voltage | [Allen Cell Types database](https://celltypes.brain-map.org/) (patch-clamp recordings) | Real fast-slow membrane voltage. No squid-axon raw data found. |
| Multiscale / stiff | Oregonator (Belousov-Zhabotinsky reaction) | [Lathrop and Kostelich bromide series](https://complex.umd.edu/data.html) | Real chaotic reaction data. The zip itself was not downloaded. |
| Multiscale / stiff | Robertson kinetics, stiff Van der Pol, two-scale Lorenz 96 | Synthetic only | Standard stiff test problems. |

### Canonical systems absent from the catalogue

| Example | Class | Real data | Note |
|---|---|---|---|
| Van der Pol oscillator | ODE, limit cycle | None deposited. Nearest: [Silverbox](https://www.nonlinearbenchmark.org/benchmarks/silverbox) | Silverbox is an electronic Duffing oscillator, not Van der Pol. Circuit paper without data: [arXiv 1904.11289](https://arxiv.org/abs/1904.11289). |
| Lotka-Volterra | ODE | [Hudson Bay lynx-hare pelts, 1900-1920](https://raw.githubusercontent.com/stan-dev/example-models/master/knitr/lotka-volterra/hudson-bay-lynx-hare.csv) (file read); [R pelt, 1845-1935](https://tsibbledata.tidyverts.org/reference/pelt.html) | Fur returns, not census counts. Worked in the [Stan case study](https://mc-stan.org/learn-stan/case-studies/lotka-volterra-predator-prey.html). |
| SIR epidemic | ODE | [1978 boarding-school influenza](https://r-packages.io/datasets/influenza_england_1978_school) (14 daily rows, R outbreaks package) | Alternative: [Eyam plague 1666](https://rdrr.io/cran/MultiBD/man/Eyam.html) (8 rows). |
| Double-well SDE | SDE, bistable | [NGRIP ice-core d18O, 20-year means](https://www.ncei.noaa.gov/pub/data/paleo/icecore/greenland/summit/ngrip/gicc05-20yr.txt) (file read) | Dansgaard-Oeschger switching as a real bistable record. Coarse and indirect. No optical-tweezers data found. |
| Kuramoto-Sivashinsky | PDE in time, chaotic | Synthetic only | Generate with a spectral solver (Kassam and Trefethen 2005). |
| Wave equation | PDE in time, linear | [Bowed cello string, Zenodo 1302894](https://doi.org/10.5281/zenodo.1302894) (CC BY 4.0) | Weak: torsional waves on a bowed string, not the plain wave equation. Seismic alternative: [SAGE DMC](https://ds.iris.edu/ds/nodes/dmc/data/). |
| Fisher-KPP | PDE in time | [Scratch-assay cell density profiles](https://github.com/jlager/BINNs) (Jin et al. 2016 data, no licence file) | Small real data, standard for PDE calibration. Paper: [Lagergren et al. 2020](https://arxiv.org/abs/2005.13073). |
| Gray-Scott | PDE in time | Synthetic only | Reference patterns: [xmorphia](https://www.mrob.com/pub/comp/xmorphia/). |
| Korteweg-de Vries | PDE in time, solitons | Synthetic only | No open wave-tank or internal-wave dataset located. |
| Lorenz 96 | ODE, chaotic | Synthetic only | Standard filtering test-bed: [DAPPER](https://github.com/nansencenter/DAPPER). |

## Gaps

- **Planned above**: every type marked **none** in the tables now has at least one planned example.
- **Planned but synthetic only**: SPDEs in time, Fermi-Pasta-Ulam-Tsingou, Hénon-Heiles, Kuramoto-Sivashinsky, Gray-Scott, Korteweg-de Vries, Lorenz 96, Mackey-Glass, generalised Langevin, the Cartesian pendulum and RLC circuit, the torus and map examples, the stiff test problems.
- **Planned with weak real data**: Van der Pol, wave equation, wildfire spread, double-well tunnelling, differential-algebraic systems (one small real dataset).

## Related pages
- [[Examples catalogue]]
- [[Planned and stub examples]]
