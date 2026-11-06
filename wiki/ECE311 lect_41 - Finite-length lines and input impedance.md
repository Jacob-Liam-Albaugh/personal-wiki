---
type: lecture
area: em
source-ref: "ECE 311 lect_41, slides pp. 1-7"
tags: [electromagnetics]
course: ece311
lecture: lect_41
---
# ECE311 lect_41 - Finite-length lines and input impedance

**Summary**: Terminated finite line: reflection coefficient at the load and input impedance.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 19 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_41.pdf` (7 slides)

---

## Topics
- Incident and reflected waves on a finite line
- Reflection coefficient at the load
- V(z), I(z) from the load
- Input impedance Zin
- Special loads: matched, short, open

## Key results
Finite line with load at $z=0$ and source at $z=-\ell$ (PDF pp. 2-3, [3-4]). Slide numbers in brackets.
$$V(z)=V_0^+e^{-\gamma z}+V_0^-e^{+\gamma z}$$
$$I(z)=I_0^+e^{-\gamma z}+I_0^-e^{+\gamma z}$$
$$\frac{V_0^+}{I_0^+}=Z_0,\qquad \frac{V_0^-}{I_0^-}=-Z_0$$
At the load, $V_L=V_0^++V_0^-$ and $I_LZ_0=V_0^+-V_0^-$ [4]. With $V_L=Z_LI_L$, reflection coefficient (PDF p. 3, [5]):
$$\Gamma\equiv\frac{V_0^-}{V_0^+}=\frac{Z_L-Z_0}{Z_L+Z_0}$$
Fields at any $z$ (PDF pp. 3-5, [6, 8, 10]):
$$V(z)=I_L[Z_L\cosh(-\gamma z)+Z_0\sinh(-\gamma z)]$$
$$I(z)=\frac{I_L}{Z_0}[Z_L\sinh(-\gamma z)+Z_0\cosh(-\gamma z)]$$
Lossless: replace by $\cos(-\beta z)$ and $j\sin(-\beta z)$ [6, 8].
Input impedance, $Z_{in}=V(-\ell)/I(-\ell)$ (PDF p. 5, [10]):
$$Z_{in}=Z_0\frac{Z_L+Z_0\tanh\gamma\ell}{Z_0+Z_L\tanh\gamma\ell}$$
$$Z_{in}=R_0\frac{Z_L+jR_0\tan\beta\ell}{R_0+jZ_L\tan\beta\ell}\ \text{(lossless)}$$
Special loads (PDF p. 6, [11-12]):
$$Z_L=Z_0:\ \Gamma=0,\ Z_{in}=Z_0$$
$$Z_L=0:\ Z_{in}=jR_0\tan\beta\ell$$
$$Z_L\to\infty:\ Z_{in}=-jR_0\cot\beta\ell$$
Matched load gives $V(z)=I_LZ_0e^{-j\beta z}$, a pure travelling wave [11]. Plots of incident, reflected, total $V(z)$ and $Z_0I(z)$ for $\Gamma=-1$ (short) are on PDF pp. 4-5 [7, 9].

## Examples
> [!example] i-Clicker (PDF p. 3, [5])
> 50 ohm coax, 2 m long, with a 25 ohm load: $\Gamma=(25-50)/(25+50)=-1/3$. Answer b on the slide's choices; the slide does not mark it, so this value is computed here.

**Sources**: `Electromagnetics/Lectures Slides/lect_41.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Transmission line]]
- [[Reflection and transmission of waves]]
- [[ECE311 lect_39 - Transmission line losses]]
- [[ECE311 lect_42 - SWR and lines as circuit elements]]
