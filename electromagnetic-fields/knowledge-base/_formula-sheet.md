---
kb: "Electromagnetic Fields — EEE3202"
file_role: formula-sheet
purpose: "Every key equation from the current-cohort handouts in one place, each tagged to its source page. All forms given here are the CORRECTED forms; where the handout prints something different, the flag ID is noted."
scope: "WC1 only. Extend as further handouts arrive."
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

## Quick numerical anchors

| Quantity | Value |
|---|---|
| $c$ | $3\times10^8$ m/s |
| $\eta_0$ | $120\pi = 377\ \Omega$ |
| $\mu_0$ | $4\pi\times10^{-7}$ H/m |
| $\varepsilon_0$ | $\dfrac{10^{-9}}{36\pi} = 8.854\times10^{-12}$ F/m |
| $\alpha$ conversion | Np/m × 8.686 = dB/m |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
