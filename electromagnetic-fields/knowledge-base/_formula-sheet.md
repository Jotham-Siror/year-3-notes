---
kb: "Electromagnetic Fields — EEE3202"
file_role: formula-sheet
purpose: "Every key equation from the current-cohort material in one place, each tagged to its source page. All forms given here are the CORRECTED forms; where the handout prints something different, the flag ID is noted."
scope: "WC1 (§1-8), TL and TLT (§9-13), WG (§14), CEM (§15). Extend as further material arrives."
---

# Formula sheet — Electromagnetic Fields (EEE3202)

Every equation below is the **corrected** form. A ⚠ marks one where the handout's printed version
differs — the ID points into `_verification-log.md`.

---

## 1 · Maxwell's equations

**Differential form** ·WC1 p1

$$\nabla \times \vec{H} = \frac{\partial\vec{D}}{\partial t} + \vec{J} \qquad \nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t} \qquad \nabla \cdot \vec{D} = \rho_v \qquad \nabla \cdot \vec{B} = 0$$

**Constitutive relations** ·WC1 p1

$$\vec{D} = \varepsilon\vec{E} \qquad \vec{B} = \mu\vec{H} \qquad \vec{J} = \sigma\vec{E}$$

**Harmonic (phasor) form** ·WC1 p6 ⚠ V3

$$\nabla \times \vec{H} = (\sigma + j\omega\varepsilon)\vec{E} \qquad \nabla \times \vec{E} = -j\omega\bar{B}$$

Every $\partial/\partial t$ becomes $\times\, j\omega$; every $\partial^2/\partial t^2$ becomes
$\times\, (-\omega^2)$.

---

## 2 · Wave equations

**General homogeneous medium** ·WC1 p2–3 ⚠ V5 (printed as $\nabla^2\bar{A}$)

$$\nabla^2\bar{H} = \mu\varepsilon\frac{\partial^2 H}{\partial t^2} + \mu\sigma\frac{\partial H}{\partial t} \qquad \nabla^2\bar{E} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2} + \mu\sigma\frac{\partial\bar{E}}{\partial t}$$

**Perfect dielectric** ($\sigma = 0$) ·WC1 p3

$$\nabla^2\bar{H} = \mu\varepsilon\frac{\partial^2 H}{\partial t^2} \qquad \nabla^2\bar{E} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2}$$

**Free space** ·WC1 p3–4

$$\nabla^2\bar{E} = \mu_0\varepsilon_0\frac{\partial^2\bar{E}}{\partial t^2}$$

**One-dimensional (plane wave along $z$)** ·WC1 p5

$$\frac{\partial^2\bar{E}}{\partial z^2} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2} \qquad \frac{\partial^2\bar{H}}{\partial z^2} = \mu\varepsilon\frac{\partial^2\bar{H}}{\partial t^2}$$

**Phasor form** ·WC1 p7

$$\nabla^2 E = -\omega^2\mu\varepsilon E \quad \text{(lossless)} \qquad \nabla^2 E + (\omega^2\mu\varepsilon - j\omega\mu\sigma)E = 0 \quad \text{(conducting)}$$

**Useful operators** ·WC1 p2, p5 ⚠ V2

$$\nabla \times \nabla \times \bar{A} = \nabla(\nabla\cdot\bar{A}) - \nabla^2\bar{A} \qquad \nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

---

## 3 · Plane-wave solution

**d'Alembert solution** ·WC1 p5

$$E(z,t) = f(z - vt) + g(z + vt)$$

$f$ travels in $+z$; $g$ travels in $-z$.

**Propagation velocity (lossless)** ·WC1 p5

$$v = \frac{1}{\sqrt{\mu\varepsilon}} \qquad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = 3\times10^8\ \text{m/s}$$

**Field relationship** ·WC1 p7

$$E(z) = E_0e^{-jkz}\,a_x \qquad H(z) = \frac{E_0}{\eta}e^{-jkz}\,a_y \qquad k = \omega\sqrt{\mu\varepsilon}$$

$E$, $H$ and the propagation direction are mutually perpendicular.

---

## 4 · Intrinsic impedance

**General (lossless)** ·WC1 p7–8

$$\eta = \frac{E_x}{H_y} = \frac{\omega\mu}{k} = \sqrt{\frac{\mu}{\varepsilon}}$$

**Free space** ·WC1 p8 ⚠ V1 ($\mu_0$ printed as $4\pi\times10^{-12}$)

$$\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = 120\pi \approx 377\ \Omega \qquad \mu_0 = 4\pi\times10^{-7}\ \text{H/m}, \quad \varepsilon_0 = \frac{10^{-9}}{36\pi}\ \text{F/m}$$

**In a dielectric** (handy working form) [added — standard]

$$\eta = \frac{\eta_0}{\sqrt{\varepsilon_r}} \quad (\mu_r = 1) \qquad v_p = \frac{c}{\sqrt{\varepsilon_r}} \quad (\mu_r = 1)$$

**General lossy medium** ·WC1 p10–11 ⚠ V16

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}} \qquad |\eta| = \frac{\sqrt{\mu/\varepsilon}}{\left[1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2\right]^{1/4}} \qquad \theta_\eta = \frac{1}{2}\tan^{-1}\left(\frac{\sigma}{\omega\varepsilon}\right)$$

with $0 \le \theta_\eta \le 45°$.

---

## 5 · Propagation constant

**Definition** ·WC1 p9

$$\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon) = j\mu\omega\sigma - \omega^2\mu\varepsilon \qquad \gamma = \alpha + j\beta$$

**General $\alpha$ and $\beta$** ·WC1 p9 ⚠ V10 (bracket grouping), V15 (labelled $\sigma$)

$$\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1\right]}$$

$$\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1\right]}$$

**Derivation identities** ·WC1 p10 ⚠ V11, V12, V13, V14

$$\alpha^2 - \beta^2 = -\omega^2\mu\varepsilon \qquad 2\alpha\beta = \mu\omega\sigma \qquad \alpha^2 + \beta^2 = \omega^2\mu\varepsilon\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2}$$

---

## 6 · Classifying the medium

**Loss tangent** ·WC1 p11–12

$$\frac{J_c}{J_{disp}} = \frac{\sigma}{j\omega\varepsilon} \qquad \tan\theta = \frac{\sigma}{\omega\varepsilon}$$

**Complex permittivity** ·WC1 p12 ⚠ V17 (printed as $\gamma^2$)

$$\varepsilon^* = \varepsilon\left(1 - \frac{j\sigma}{\omega\varepsilon}\right) \qquad \gamma = j\omega\sqrt{\mu\varepsilon^*}$$

**Classification** ·WC1 p13

| $\sigma/\omega\varepsilon \gg 1$ | conducting medium |
|---|---|
| $\sigma/\omega\varepsilon \ll 1$ | dielectric medium |
| $\sigma/\omega\varepsilon = 1$ | crossover ($\omega = \sigma/\varepsilon$) |

The **same material** can be a conductor at one frequency and a dielectric at another.

---

## 7 · The four media, side by side

| | Perfect dielectric | Lossy dielectric | Good conductor |
|---|---|---|---|
| **Condition** | $\sigma = 0$ | $\dfrac{\sigma}{\omega\varepsilon} \ll 1$ | $\dfrac{\sigma}{\omega\varepsilon} \gg 1$ |
| **$\gamma$** | $j\omega\sqrt{\mu\varepsilon}$ | $\alpha + j\beta$ | $\alpha + j\beta$ |
| **$\alpha$** | $0$ | $\dfrac{\sigma}{2}\sqrt{\dfrac{\mu}{\varepsilon}}$ | $\sqrt{\dfrac{\omega\mu\sigma}{2}}$ |
| **$\beta$** | $\omega\sqrt{\mu\varepsilon}$ | $\omega\sqrt{\mu\varepsilon}\left(1 + \dfrac{\sigma^2}{8\omega^2\varepsilon^2}\right)$ | $\sqrt{\dfrac{\omega\mu\sigma}{2}}$ |
| **$v_p$** | $\dfrac{1}{\sqrt{\mu\varepsilon}}$ | $\dfrac{1}{\sqrt{\mu\varepsilon}\left(1 + \dfrac{\sigma^2}{8\omega^2\varepsilon^2}\right)}$ | $\sqrt{\dfrac{2\omega}{\mu\sigma}}$ |
| **$\eta$** | $\sqrt{\dfrac{\mu}{\varepsilon}}$ | $\eta\left(1 + \dfrac{j\sigma}{2\omega\varepsilon}\right)$ | $\sqrt{\dfrac{\omega\mu}{2\sigma}}(1+j)$ |
| **Source** | ·WC1 p15 | ·WC1 p14–15 ⚠ V18 | ·WC1 p16–17 ⚠ V19, V20 |

**Binomial expansion used for the lossy case** ·WC1 p14 *(correct as printed)*

$$\left(1 - \frac{j\sigma}{\omega\varepsilon}\right)^{1/2} = 1 - \frac{j\sigma}{2\omega\varepsilon} + \frac{1}{8}\frac{\sigma^2}{\omega^2\varepsilon^2}$$

Note the **$+$** on the third term — with $x = -j\sigma/\omega\varepsilon$,
$-x^2/8 = +\sigma^2/8\omega^2\varepsilon^2$.

**Good-conductor intrinsic impedance, long form** ·WC1 p16–17

$$\eta^* = \sqrt{\frac{j\omega\mu}{\sigma}} = \sqrt{\frac{\omega\mu}{\sigma}}\,e^{j\pi/4} = \sqrt{\frac{\omega\mu}{2\sigma}}(1+j)$$

using $\varepsilon^* \approx -j\sigma/\omega$ for $\sigma/\omega\varepsilon \gg 1$ ⚠ V20.

---

## 8 · Skin depth

·WC1 p17 *(correct as printed)*

$$\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega\mu\sigma}} = \frac{1}{\sqrt{\pi f\mu\sigma}}$$

Attenuation to $1/e \approx 37\%$ of the surface value. $\delta$ falls as $f$, $\mu$ or $\sigma$
rises.

---

## 9 · Transmission lines — the RLGC model

*Source: TL and TLT. See `02-transmission-lines.md`. Every form below is the **corrected** form; a ⚠
marks one where a source prints something different.*

**The four primary line constants** — all **per unit length** ·TL p1 · ·TLT pp. 3–4

| $R$ (Ω/m) | $L$ (H/m) | $G$ (S/m) | $C$ (F/m) |
|---|---|---|---|
| conductor ohmic loss | magnetic energy storage | dielectric leakage | dielectric energy storage |

**Telegrapher's equations** ·TL pp. 1–2 ⚠ T1, T2 (printed with $\partial/\partial t$ on the left) · ·TLT p7

$$-\frac{\partial v}{\partial z} = R\,i + L\frac{\partial i}{\partial t} \qquad\qquad -\frac{\partial i}{\partial z} = G\,v + C\frac{\partial v}{\partial t}$$

**Lossy wave equation** ·TLT p8

$$\frac{\partial^2 V}{\partial z^2} = LC\frac{\partial^2 V}{\partial t^2} + (LG+RC)\frac{\partial V}{\partial t} + RG\,V$$

Identical in form for $I$ — so identical solutions.

**Lossless wave equation and phase velocity** ·TL pp. 2–3 · ·TLT p10

$$\frac{\partial^2 v}{\partial z^2} = LC\frac{\partial^2 v}{\partial t^2} = \frac{1}{u_p^2}\frac{\partial^2 v}{\partial t^2} \qquad\qquad u_p = \frac{1}{\sqrt{LC}}$$

**d'Alembert solution** ·TL p3

$$v(z,t) = V^{+}\!\left(t - \frac{z}{u_p}\right) + V^{-}\!\left(t + \frac{z}{u_p}\right)$$

---

## 10 · Line propagation constant and characteristic impedance

**Propagation constant** ·TL p4 ⚠ T3 (eqs 8, 9 printed with $-j\omega L$, $-j\omega C$) · ·TLT p12, p16

$$\gamma = \sqrt{(R+j\omega L)(G+j\omega C)} = \sqrt{RG + j\omega(LG+RC) - \omega^2 LC} = \alpha + j\beta$$

The two radicands are the same expression multiplied out. **Lossless case:**

$$\alpha = 0 \qquad\qquad \beta = \omega\sqrt{LC} = \frac{2\pi}{\lambda} \qquad\qquad \gamma = j\beta$$

> ⚠ **Do not confuse with WC1's $\gamma$.** WC1 § 5 gives
> $\gamma^2 = j\mu\omega(\sigma+j\omega\varepsilon)$ — a property of the **medium**. This one is a
> property of the **line**. Same symbol, same meaning, different formula.

**Characteristic impedance** ·TLT p15

$$Z_0 = \frac{V_0^{+}}{I_0^{+}} = \sqrt{\frac{R+j\omega L}{G+j\omega C}} \qquad\qquad \text{lossless:}\quad Z_0 = \sqrt{\frac{L}{C}} \quad\text{(purely real)}$$

$$Z_0 = \frac{\text{forward voltage}}{\text{forward current}} = -\,\frac{\text{backward voltage}}{\text{backward current}}$$

**Travelling-wave solution** ·TLT p13 ⚠ T4 (backward term printed $e^{j\gamma}$)

$$V(z) = V_0^{+}e^{-\gamma z} + V_0^{-}e^{+\gamma z} \qquad\qquad I(z) = I_0^{+}e^{-\gamma z} + I_0^{-}e^{+\gamma z}$$

$e^{-\gamma z}$ travels in $+z$; $e^{+\gamma z}$ travels in $-z$.

---

## 11 · Reflection, standing waves and VSWR

**Reflection coefficient** ·TL p5 ⚠ T5, T6, T7 · ·TLT p17

$$\Gamma = \frac{V_0^{-}}{V_0^{+}} = \frac{Z_L-Z_0}{Z_L+Z_0} = |\Gamma|e^{j\theta_r} \qquad\qquad V_{ref} = \Gamma V_{in}$$

$$Z_L = Z_0\,\frac{1+\Gamma}{1-\Gamma} \quad \text{[added — the inverted form, needed for every slotted-line problem]}$$

| Termination | $Z_L$ | $\Gamma$ |
|---|---|---|
| Matched | $Z_0$ | $0$ — no reflection, no standing wave |
| Open circuit | $\infty$ | $+1$ |
| Short circuit | $0$ | $-1$ |

For a passive load on a lossless line, $0 \le |\Gamma| \le 1$.

**Standing-wave magnitude** ·TL p7 ⚠ T8, T9 (brackets and square root both missing) · ·TL p11 *(correct there)*

$$|V(z)| = |V_0^{+}|\left[1 + |\Gamma|^2 + 2|\Gamma|\cos(2\beta z + \theta_r)\right]^{1/2}$$

**Positions of maxima and minima** ·TL p9 ⚠ T10 (minimum labelled $-z_{max}$)

$$-z_{max} = \frac{\theta_r\lambda}{4\pi} + \frac{n\lambda}{2} \qquad\qquad -z_{min} = \frac{\theta_r\lambda}{4\pi} + \frac{(2n+1)\lambda}{4}$$

Max-to-max $= \lambda/2$. Min-to-min $= \lambda/2$. **Max to adjacent min $= \lambda/4$** ⚠ C25.
Voltage maxima coincide with current minima.

**VSWR and return loss** ·TL p9 · ·TLT p17

$$S = \frac{|V|_{max}}{|V|_{min}} = \frac{1+|\Gamma|}{1-|\Gamma|} \qquad\qquad |\Gamma| = \frac{S-1}{S+1}\ \text{[added]} \qquad\qquad \text{RL} = -20\log_{10}|\Gamma|\ \text{dB}$$

$\Gamma$, $S$ and RL are three expressions of the same thing — given any one, you have the others.

**Slotted-line inversion** [added] — the step neither source writes, needed by both its exercises

$$|\Gamma| = \frac{S-1}{S+1} \;;\quad \lambda = 2\times(\text{minimum spacing}) \;;\quad \theta_r = 2\beta d_{min} - \pi \;;\quad Z_L = Z_0\frac{1+\Gamma}{1-\Gamma}$$

---

## 12 · Line impedance, stubs and matching

**Input impedance at distance $z$ back from the load** ·TL p12

$$Z_{in}(-z) = Z_0\,\frac{Z_L\cos\beta z + jZ_0\sin\beta z}{Z_0\cos\beta z + jZ_L\sin\beta z} = Z_0\,\frac{Z_L + jZ_0\tan\beta z}{Z_0 + jZ_L\tan\beta z}\ \text{[added form]}$$

This one equation is the parent of everything below — each case is a particular $Z_L$ or $z$.

**Stubs** ·TL pp. 12–14 ⚠ C26

$$\text{short-circuit } (Z_L = 0):\quad Z_{in} = jZ_0\tan\beta z \qquad\qquad \text{open-circuit } (Z_L \to \infty):\quad Z_{in} = -jZ_0\cot\beta z$$

Both are **purely reactive**. Which half gives which reactance **depends on the termination**:

| Length | Shorted stub | Open stub |
|---|---|---|
| $0 \to \lambda/4$ | **inductive** ($X: 0 \to +\infty$) | **capacitive** |
| $\lambda/4 \to \lambda/2$ | **capacitive** ($X: -\infty \to 0$) | **inductive** |

The pattern repeats every $\lambda/2$.

**Quarter-wave transformer** ·TL pp. 14–15 ⚠ T11 ($\beta z$ printed as $\lambda/2$)

$$z = \frac{\lambda}{4} \;\Longrightarrow\; \beta z = \frac{\pi}{2} \;\Longrightarrow\; \boxed{Z_{in} = \frac{Z_0^2}{Z_L}} \qquad\qquad \boxed{Z_0 = \sqrt{Z_{in}Z_L}}\ \text{[added — the design form]}$$

The section's characteristic impedance is the **geometric mean** of the two impedances it matches.

---

## 13 · The Smith chart

·TLT pp. 18–22. **The only source for this in the repository. ·TLT p20 is a full blank chart — print it.**

**Normalize first, always:**

$$z_L = \frac{Z_L}{Z_0} \qquad\text{(dimensionless; the chart centre is } 1+j0\text{)}$$

**Procedure** ·TLT p19, p21:

1. Plot $z_L$.
2. Draw the circle through it centred on $1+j0$ — the constant-$|\Gamma|$ (constant-VSWR) circle.
   Every impedance along the line lies on it.
3. Move round that circle **toward the generator**; read the distance off the *wavelengths toward
   generator* perimeter scale.

The chart also reads off $\Gamma$ (magnitude and angle), VSWR, return loss and power delivered.

---

## 14 · Rectangular waveguides

·WG pp. 5–8. ·WG p9: the short forms **are not provided in the exam** — memorise them.

**Wave numbers** ·WG p5 ⚠ W4

$$k = \omega\sqrt{\mu\varepsilon} \qquad\qquad k_c^2 = k^2 - \beta^2 \qquad\qquad k_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$

**Phase constant** ·WG p8 ⚠ W7 ($b$ printed as $a$)

$$\beta = \sqrt{k^2 - k_c^2} = \sqrt{\omega^2\mu\varepsilon - \left(\frac{m\pi}{a}\right)^2 - \left(\frac{n\pi}{b}\right)^2}$$

**Cut-off** ·WG p8 ⚠ W8 (the speed here is $1/\sqrt{\mu\varepsilon}$, not the guide $V_p$)

$$f_c = \frac{1}{2\pi\sqrt{\mu\varepsilon}}\sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2} \qquad\qquad \lambda_c = \frac{2}{\sqrt{(m/a)^2 + (n/b)^2}}$$

**Dominant mode $TE_{10}$** `[added]`

$$\lambda_c = 2a \qquad\qquad f_c = \frac{c}{2a}$$

**The short forms.** Let $F = \sqrt{1 - (f_c/f)^2}$ and $\lambda = c/f$. Printed ·WG p8 unless tagged.

| Quantity | Formula | Source |
|---|---|---|
| Phase velocity | $V_p = \omega/\beta = c/F$ | ·WG p8 |
| Guide wavelength | $\lambda_g = 2\pi/\beta = \lambda/F$ | long form ·WG p8 ⚠ W7; short form `[added]` |
| Group velocity | $V_g = cF$ | `[added]` — not in the handout |
| Product | $V_pV_g = c^2$ | `[added]` |
| TE wave impedance | $Z_{TE} = \eta/F$ | ·WG p8 |
| TM wave impedance | $Z_{TM} = \eta F$ | `[added]` — not in the handout |
| Below cut-off ($f < f_c$) | $\alpha = \dfrac{2\pi}{c}\sqrt{f_c^2 - f^2}$ Np/m | `[added]` — from $\beta = \sqrt{k^2-k_c^2}$ with $k < k_c$ |

All the `[added]` forms reproduce the handout's own printed answers to its revision Q4 and Q5.

---

## 15 · Computational EM — finite differences

·CEM pp. 1–6.

**Taylor pair** ·CEM pp. 1–2 ⚠ F1 (·CEM p2 labels the alternating series $f(x+\Delta x)$)

$$f(x+\Delta x) = \sum_{k=0}^{\infty}\frac{f^{(k)}(x)(\Delta x)^k}{k!} \qquad\qquad f(x-\Delta x) = \sum_{k=0}^{\infty}\frac{(-1)^kf^{(k)}(x)(\Delta x)^k}{k!}$$

**Second difference** ·CEM p2 ⚠ F2 (error is $O(\Delta x^2)$)

$$f''(x) \approx \frac{f(x+\Delta x) - 2f(x) + f(x-\Delta x)}{\Delta x^2}$$

**First differences** ·CEM pp. 2–3 ⚠ F3 (backward printed with $+\Delta x$)

| Name | Formula | Error |
|---|---|---|
| Forward | $f'(x) \approx \dfrac{f(x+\Delta x) - f(x)}{\Delta x}$ | $O(\Delta x)$ |
| Backward | $f'(x) \approx \dfrac{f(x) - f(x-\Delta x)}{\Delta x}$ | $O(\Delta x)$ |
| Central | $f'(x) \approx \dfrac{f(x+\Delta x) - f(x-\Delta x)}{2\Delta x}$ | $O(\Delta x^2)$ |

**Poisson, finite-difference form** ·CEM p6 ⚠ F6 ($\rho_v$, not $\rho_s$), $\Delta x = \Delta y = h$

$$V_{i,j} = \frac{1}{4}\left(V_{i+1,j} + V_{i,j+1} + V_{i-1,j} + V_{i,j-1} + \frac{h^2\rho_v}{\varepsilon}\right)$$

**Laplace — the five-node molecule** ·CEM p6

$$V_{i,j} = \frac{1}{4}\left(V_{i+1,j} + V_{i,j+1} + V_{i-1,j} + V_{i,j-1}\right) \qquad\qquad V_0 = \frac{1}{4}\left(V_1 + V_2 + V_3 + V_4\right)$$

Each free node is the **average of its four neighbours**. Iterate with the **newest** values
(·CEM p8; ⚠ F7).

---

## Quick numerical anchors

| Quantity | Value |
|---|---|
| $c$ | $3\times10^8$ m/s |
| $\eta_0$ | $120\pi = 377\ \Omega$ |
| $\mu_0$ | $4\pi\times10^{-7}$ H/m |
| $\varepsilon_0$ | $\dfrac{10^{-9}}{36\pi} = 8.854\times10^{-12}$ F/m |
| $\alpha$ conversion | Np/m × 8.686 = dB/m |
| $Z_0$ common values | 50 Ω (RF/coax), 75 Ω (video/aerial), 300 Ω (twin-lead / folded dipole) |
| dipole input impedance | 73 Ω (half-wave, the value both TL and TLT use) |
| $S = 1$ | perfectly matched; $\Gamma = 0$; RL $= \infty$ |
| $TE_{10}$ cut-off | $\lambda_c = 2a$, $f_c = c/2a$ — a 5 cm guide cuts off at 3 GHz |
| waveguide | $V_p > c > V_g$, $V_pV_g = c^2$, $\lambda_g > \lambda$, $Z_{TE} > \eta$ |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
