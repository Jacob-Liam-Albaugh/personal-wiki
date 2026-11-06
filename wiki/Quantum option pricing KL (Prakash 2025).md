---
type: paper
area: stochastic
areas: [stochastic, math]
source-ref: "Prakash et al. 2024, arXiv:2402.10132, Thm 2.5-2.12"
tags: [uq, gp]
authors: ["[[Anupam Prakash]]", "[[Yue Sun]]", "[[Shouvanik Chakrabarti]]", "[[Charlie Che]]"]
year: 2025
venue: "arXiv:2402.10132 (quant-ph), v1 dated 15 Feb 2024"
file: "papers/Stochastic Methods/Prakash, Sun, Chakrabarti, Che - Quantum Option Pricing via the Karhunen-Loéve Expansion.pdf"
---

# Quantum option pricing KL (Prakash 2025)

**Summary**: Prices discretely monitored Asian options on a geometric Brownian motion with quantum Monte Carlo. The path is stored in a "semi-digital" register built from the truncated [[Karhunen-Loève expansion]] of [[Brownian motion]]. The same KL analysis also yields classical algorithms that match the quantum cost.

**Authors**: Anupam Prakash, Yue Sun, Shouvanik Chakrabarti, Charlie Che (and co-authors) · **Year**: 2025 (the PDF is arXiv v1 dated 15 Feb 2024; the page name carries the year used in the wiki queue) · **File**: `papers/Stochastic Methods/Prakash, Sun, Chakrabarti, Che - Quantum Option Pricing via the Karhunen-Loéve Expansion.pdf`

---

## Problem

Option pricing needs sample paths of an asset price, then a Monte Carlo average of the payoff. Quantum Monte Carlo integration based on amplitude estimation gives a quadratic speed-up in the error $\epsilon$ (source: Prakash PDF, p. 1). The question is how to hold a path of $T$ time points in a quantum state.

Two encodings existed before this paper (source: p. 2, p. 5):

- **Digital**: the whole path is stored in basis states. Flexible, but no advantage in $T$ over classical simulation.
- **Analog**: path values sit in amplitudes. Compact (exponentially fewer qubits in $T$), but arithmetic on values is hard. Exponentiated processes such as geometric Brownian motion have no compact Fourier series.

## Semi-digital encoding

Store the time index in superposition and the value in a separate register (source: Def. 2.1, p. 5):

$$|\psi\rangle \propto \sum_{t}|t\rangle\,|v(t)\rangle$$

The value register can be exponentiated by coherent arithmetic. A coherent version adds a register for the randomness used (Def. 2.2). An $\epsilon$-approximate version allows truncated paths with expected squared error at most $\epsilon^2$ (Def. 2.3).

## KL ingredients

- Kosambi-Karhunen-Loève theorem: for a centred, square-integrable process with covariance $k_X$, the expansion converges uniformly in $t$ in $L^2(P)$ (source: Thm 2.5, p. 7).
- Truncation index $L_X(\epsilon)$: smallest $L$ with squared error at most $\epsilon^2$ for all $t$ (Def. 2.6).
- Brownian motion: kernel $\min(s,t)$, eigenvalues $\lambda_k=1/((k-1/2)^2\pi^2)$ (source: Thm 2.7). See [[Wiener process]] and [[KL expansions of the Wiener process (Deheuvels 2006)]].
- The tail variance is $O(1/L)$, so $L_X(\epsilon)=O(1/\epsilon^2)$ (source: Thm 2.8).
- The Wiener series $B(t)=a_0 t+\sum_k a_k\sin(k\pi t)/(k\pi)$ with i.i.d. $a_k\sim N(0,1)$ is the working form (source: Thm 2.9, p. 8). Truncated at $L$ terms it is a degree-$L$ polynomial in $\cos(\pi t)$ via Chebyshev polynomials of the second kind.

Gaussian states on $n$ qubits can be prepared to trace distance $\epsilon$ with $O(n(A+\log(1/\epsilon)))$ gates, taken from a cited result (source: Thm 2.4, p. 6).

## Mapped KL expansion

Geometric Brownian motion has no closed-form KL expansion, but it is the exponential of Brownian motion. So take $S_t=g_t(X_t)$ with $X_t$ having a known KL expansion and sub-Gaussian coefficients. Assume $g$ satisfies a Lipschitz-or-exponential growth bound (source: Assumption 2.1, eq. 10). Then truncating $X_t$ at $L_X(\epsilon)$ terms gives

$$\mathbb{E}\big[(S_t-S'_t)^2\big]\le C_2\,\epsilon^2$$

uniformly in $t\in[0,1]$ (source: Lemma 2.10, Thm 2.11, p. 8-9). For GBM, $L=O(1/\epsilon^2)$ Wiener terms suffice (source: p. 10).

GBM solves the SDE $dS_t=\sigma S_t\,dB_t+\mu S_t\,dt$, with closed form

$$S_t=S_0\,e^{\sigma B_t+(\mu-\sigma^2/2)t}$$

(source: eq. 29-30). Algorithm 2.1 builds its semi-digital encoding at cost $\tilde O(L)$ (source: Thm 2.12).

## Algorithms and complexity

Four algorithms for the discretely monitored Asian option (source: p. 3-4, Table 1; the numeric cells of Table 1 did not extract, so the rates below come from the text):

| Algorithm | Gate complexity |
|---|---|
| Semi-digital quantum MC | $\tilde O(1/\epsilon^4)$ |
| Quantum-inspired (dequantised) classical sampling | $\tilde O(1/\epsilon^6)$ |
| Classical time-domain sub-sampling | matches the semi-digital rate for Brownian motion |
| Quantised sub-sampling | $\tilde O(1/\epsilon^3)$, fastest |
| Standard quantum MCI | $O(T\epsilon^{-1})$ |
| Standard classical MCI | $O(T\epsilon^{-2})$ |

- The semi-digital cost is high because the Asian payoff needs two nested amplitude estimations (source: p. 3).
- Speed-ups over standard Monte Carlo hold in the regime $T\gg1/\epsilon^2$ for GBM (source: p. 3).
- Sub-sampling in time uses $\max(L_X(\epsilon)/\epsilon^2)$-type grid sizes when the KL eigenfunctions are regular (source: p. 3).
- For processes with $L_X(\epsilon)=O(1/\epsilon^\alpha)$, $\alpha\in(1,2]$ (fractional Brownian motion with $H>1/2$), the semi-digital approach costs $\tilde O(L_X(\epsilon)/\epsilon^2)$, beating the classical $\tilde O(1/\epsilon^4)$ sub-sampling. The quantised sub-sampling at $\tilde O(1/\epsilon^3)$ is still the fastest (source: p. 4).

The methods are claimed to extend to smooth functions of sub-Gaussian processes, and multilevel Monte Carlo may reduce the cost further (source: abstract, p. 4).

## Wiki note

- The paper is a clean example of the KL expansion used as a computational device, not just a representation theorem: the coefficients decouple into independent Gaussians, and the basis change is a Fourier transform (source: p. 3).
- The result that dequantisation and sub-sampling match the quantum cost means the quantum advantage is problem specific, as the authors say (source: p. 4).
- Mechanics of the truncation error are the same as in [[KL expansion note (Alexanderian 2015)]]: the discarded variance is the tail sum of eigenvalues.

**Sources**: Prakash PDF, abstract, §1-2 (pages 1-10 read in detail; §3-5 algorithm proofs not summarised).

**Last updated**: 2026-11-06

---

## Related pages
- [[Karhunen-Loève expansion]]
- [[KL expansion note (Alexanderian 2015)]]
- [[KL expansions of the Wiener process (Deheuvels 2006)]]
- [[Brownian motion]]
- [[Wiener process]]
- [[Gaussian process]]
- [[Mercer's theorem]]
