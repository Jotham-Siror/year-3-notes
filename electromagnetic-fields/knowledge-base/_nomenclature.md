---
kb: "Electromagnetic Fields — EEE3202"
file_role: nomenclature
purpose: "Every symbol used in the course material with meaning and SI units. Resolves symbol clashes. Consult this when a topic file's notation is ambiguous."
scope: "Sections marked CURRENT are covered by a current-cohort document (WC1, TL, TLT, WG or CEM). Sections marked PENDING are carried over from the old cohort and await this year's equivalent."
---

# Nomenclature and symbols

## ⚠ Symbol clashes and look-alikes — read first

This subject is unusually bad for symbol collisions, and **the sources themselves make several of
them**. Flag these explicitly when teaching.

| Symbol | Meaning | Clash / warning |
|---|---|---|
| **$\sigma$** | **conductivity** (S/m, formerly mho/m) | ⚠ **WC1 repeatedly prints $\sigma$ where it means $\alpha$** — pp. 9, 10 and 16, six equations. See `_verification-log.md` V9, V12, V14, V15, V19. Where an equation has $\sigma$ on *both* sides, the left-hand one is $\alpha$ |
| **$\alpha$** | **attenuation constant** (Np/m) | the victim of the collision above. Multiply by 8.686 to convert Np/m → dB/m |
| **$\beta$** | **phase constant** / phase-shift constant (rad/m) | always the phase constant in this subject; also mislabelled as $\alpha$ in the old-cohort handouts |
| **$\gamma$** | **propagation constant** $= \alpha + j\beta$ (m⁻¹) | ⚠ **two different formulas, same symbol.** In WC1 it is a *medium* property, $\sqrt{j\mu\omega(\sigma+j\omega\varepsilon)}$; in TL/TLT it is a *line* property, $\sqrt{(R+j\omega L)(G+j\omega C)}$. Same meaning, different sources — do not mix the formulas. Not the ratio of specific heats (that is Thermodynamics) |
| **$\eta$** | **intrinsic impedance** $\sqrt{\mu/\varepsilon}$ (Ω); $\eta^*$ = complex $\eta$ in a lossy medium | not efficiency. ⚠ WC1 p11 writes the impedance angle as $\theta_n$; the subscript is $\eta$, not the letter n |
| **$Z_0$** vs **$\eta_0$** | $Z_0$ = a **line's** characteristic impedance; $\eta_0$ = **free space's** intrinsic impedance | ⚠ **both are called "impedance" and both take subscript zero, and they are unrelated.** $Z_0$ varies by cable (50, 75, 300 Ω); $\eta_0$ is fixed at 377 Ω |
| **$C$** vs **$c$** | $C$ = **capacitance per unit length** (F/m) in TL/TLT; $c$ = **speed of light** | ⚠ **·TL pp. 3–4 print the capacitance as lowercase $c$** inside $(G+j\omega c)$, four times (C32). Rule: inside a $(G+j\omega\,\cdot)$ bracket it is always capacitance |
| **$\Gamma$** | **reflection coefficient** | ⚠ **two formulas.** At a *material boundary* (old cohort): $(\eta_2-\eta_1)/(\eta_2+\eta_1)$. On a *transmission line* (TL/TLT): $(Z_L-Z_0)/(Z_L+Z_0)$. Structurally identical, physically different — pick by whether the problem is a wave crossing a medium or a wave reaching a load |
| **$z$** vs **$z_L$, $z_N$** | $z$ = **position** along the line (m) | ⚠ on the Smith chart pages lowercase $z$ means a **normalized impedance** (dimensionless), not a distance. TLT writes $z_N$ for the same thing |
| **$S$** | **standing wave ratio** in TL/TLT (dimensionless) | not the Poynting vector, which is $P$ in this KB's old-cohort files but $S$ in most textbooks |
| **$T$** | **transmission coefficient** (boundary) *or* **period** (energy section) | two unrelated uses already in this file. Neither is used in TL/TLT |
| **$\mu$** | **permeability** (H/m) | also the SI prefix **micro** ($10^{-6}$) — "μA/m" is microamps per metre. Watch context |
| **$\varepsilon$** | **permittivity** (F/m); $\varepsilon^*$ = complex permittivity | $\varepsilon_0$ = free-space value |
| **$\rho_v$** vs **$\rho_s$** | $\rho_v$ = **volume** charge density (C/m³) — the one used throughout | $\rho_s$ = *surface* charge density (C/m²). ⚠ WC1 p3 prints $\rho_s$ where $\rho_v$ is meant (V6), and ·CEM p6 does it again for 2-D Poisson (F6) |
| **$\delta$** | **skin depth / depth of penetration** (m) | not a boundary-layer thickness (that is Fluid Flow) |
| **$\theta$** | **loss-tangent angle**, $\tan\theta = \sigma/\omega\varepsilon$ | distinguish from $\theta_\eta$, the impedance angle, which is *half* the arctangent; and from $\theta_r$, the phase of $\Gamma$ in TL/TLT |
| **$k$** vs **$\beta$** vs **$k_c$** | $k = \omega\sqrt{\mu\varepsilon}$ is the **wave number** in a lossless *unbounded* medium; $k_c$ the waveguide **cut-off** wave number | in an unbounded lossless medium $k$ and $\beta$ coincide; in a lossy one they do not; **in a waveguide they differ even with no loss**: $\beta^2 = k^2 - k_c^2$. ⚠ ·WG p5 prints $k_c$ for $k_c^2$ (W4) |
| **$\mathbf{a}$** vs **$\alpha$** | $\mathbf{a}_x, \mathbf{a}_y, \mathbf{a}_z$ = **unit vectors** | visually close to $\alpha$ in the handout's font |
| **$J$** | current density (A/m²) — $J_c$ conduction, $J_{disp}$ displacement | not to be confused with $j = \sqrt{-1}$; and ⚠ ·TL p7 switches from $j$ to $i$ for the imaginary unit mid-equation (C34) |
| **superscripts $^{+}$ / $^{-}$** | forward- / backward-travelling wave amplitude | ⚠ **·TL prints $V_0^{+}$ where $V_0^{-}$ belongs three times** (T5, T6, T7), each time collapsing the expression to something trivial. Check the superscript against which direction the term travels |
| **$V_p$** (·WG) vs **$u$** | $V_p = \omega/\beta$ = phase velocity **in the guide**, always $> c$; $u = 1/\sqrt{\mu\varepsilon}$ = speed in the **unbounded** filling medium, $c$ for air | ⚠ **·WG p8 uses $V_p$ for both on one page** (W8). In the $f_c$ formula it means $u$. Substituting the guide's $V_p$ there is wrong. Also distinct from $u_p = 1/\sqrt{LC}$ on a transmission line |
| **$\lambda$**, **$\lambda_c$**, **$\lambda_g$** | free-space wavelength $c/f$; **cut-off** wavelength; **guide** wavelength $2\pi/\beta$ | three wavelengths in one waveguide question. $\lambda_g > \lambda$ always; a mode propagates only if $\lambda < \lambda_c$ |
| **$\eta$** vs **$Z_{TE}$**, **$Z_{TM}$** | $\eta$ = the filling medium's intrinsic impedance (377 Ω for air); $Z_{TE}$, $Z_{TM}$ = the **wave impedance in the guide** | ⚠ ·WG pp. 9–10 ask for "characteristic impedance of the guide $\eta$" (C48). The answer is $Z_{TE} = \eta/\sqrt{1-(f_c/f)^2}$, not $\eta$ |
| **$a$, $b$** (waveguide) | inner width and height of the guide (m); $a$ the **broad** wall by convention | not the unit vectors $\mathbf{a}_x$…, not the polarization phase angle $a$ (old cohort). ⚠ ·WG pp. 7–8 print $a$ where $b$ belongs four times (W7) |
| **$m$, $n$** | waveguide **mode integers** — half-wave variations across $a$ and $b$ | TM: both $\ge 1$. TE: one may be 0, not both |
| **$V_1, V_2, \ldots$** (·CEM) | in the five-node molecule: the four **neighbours** of $V_0$ (top, left, bottom, right). In an iteration example: **node numbers** | ⚠ **same symbols, two meanings in one handout.** Applying the molecule to node 3, the molecule's "$V_1$" is the node above 3 — not node 1 |
| **$f^k$** (·CEM) | the handout's notation for the $k$-th **derivative** $f^{(k)}$ | reads as a power. Write $f^{(k)}$ (C50) |
| **$h$** (·CEM) | **mesh size**, $\Delta x = \Delta y = h$ (m) | not Planck's constant; not the lowercase magnetic-field components $h_x$, $h_y$, $h_z$ of ·WG |

---

## Fields and sources — CURRENT

| Symbol | Quantity | SI unit |
|---|---|---|
| $\vec{E}$ | electric field intensity | V/m |
| $\vec{H}$ | magnetic field intensity | A/m |
| $\vec{D} = \varepsilon\vec{E}$ | electric flux density (displacement) | C/m² |
| $\vec{B} = \mu\vec{H}$ | magnetic flux density | T (Wb/m²) |
| $\vec{J}_c = \sigma\vec{E}$ | conduction current density | A/m² |
| $\vec{J}_{disp} = \partial\vec{D}/\partial t$ | displacement current density | A/m² |
| $\rho_v$ | volume (free) charge density | C/m³ |
| $E_0$ | peak / amplitude value of $E$ | V/m |

## Medium constants — CURRENT

| Symbol | Quantity | SI unit | Standard value |
|---|---|---|---|
| $\varepsilon$ | permittivity $= \varepsilon_r\varepsilon_0$ | F/m | — |
| $\varepsilon_0$ | free-space permittivity | F/m | $8.854\times10^{-12} \approx \dfrac{10^{-9}}{36\pi}$ |
| $\varepsilon_r$ | relative permittivity (dielectric constant) | – | 1 in vacuum |
| $\varepsilon^*$ | complex permittivity $\varepsilon\left(1 - \dfrac{j\sigma}{\omega\varepsilon}\right)$ | F/m | — |
| $\mu$ | permeability $= \mu_r\mu_0$ | H/m | — |
| $\mu_0$ | free-space permeability | H/m | $4\pi\times10^{-7}$ ⚠ **WC1 p8 prints $10^{-12}$ — wrong, see V1** |
| $\mu_r$ | relative permeability | – | 1 for non-magnetic media |
| $\sigma$ | conductivity | S/m | 0 for a perfect dielectric |

## Wave and propagation quantities — CURRENT

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $\gamma$ | propagation constant $= \alpha + j\beta$ | m⁻¹ | $\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon)$ **in a medium** |
| $\alpha$ | attenuation constant | Np/m | ×8.686 → dB/m |
| $\beta$ | phase constant | rad/m | $\lambda = 2\pi/\beta$ |
| $k$ | wave number $= \omega\sqrt{\mu\varepsilon}$ | rad/m | lossless media |
| $\omega$ | angular frequency $= 2\pi f$ | rad/s | — |
| $f$ | frequency | Hz | — |
| $\lambda$ | wavelength $= 2\pi/\beta = v_p/f$ | m | — |
| $v$, $v_p$ | (phase) velocity of propagation | m/s | $v = 1/\sqrt{\mu\varepsilon}$ lossless |
| $c$ | speed of light $= 1/\sqrt{\mu_0\varepsilon_0}$ | m/s | $3\times10^8$ |
| $\eta$, $\eta^*$ | intrinsic impedance $\sqrt{\mu/\varepsilon}$; complex $\eta^*$ | Ω | — |
| $\eta_0$ | free-space impedance | Ω | $120\pi \approx 377$ |
| $\theta_\eta$ | impedance angle $= \frac12\tan^{-1}(\sigma/\omega\varepsilon)$ | ° | $0 \le \theta_\eta \le 45°$ |
| $\tan\theta$ | loss tangent $= \sigma/\omega\varepsilon$ | – | the medium-classifying number |
| $\delta$ | skin depth $= 1/\alpha$ | m | — |
| $f$, $g$ | forward / backward travelling-wave profiles (d'Alembert) | field units | $f(z-vt)$, $g(z+vt)$ |

## Transmission lines — CURRENT

*Covered by TL and TLT. See `02-transmission-lines.md`.*

### The four primary line constants — all **per unit length**

| Symbol | Quantity | SI unit | Represents |
|---|---|---|---|
| $R$ | series resistance per unit length | Ω/m | conductor ohmic loss |
| $L$ | series inductance per unit length | H/m | magnetic energy storage |
| $G$ | shunt conductance per unit length | S/m | dielectric leakage |
| $C$ | shunt capacitance per unit length | F/m | dielectric energy storage |

> These four are a recurring **4-mark bookwork question** — asked on the 1 Oct 2025 CAT (Q1a) and
> again on the 23 Oct 2025 exam (Q1g). The marks are for the *significance*, not the names.

### Line and wave quantities

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $\Delta z$, $\Delta\ell$ | length of the elementary line cell | m | must satisfy $\Delta\ell \ll \lambda$ |
| $v(z,t)$, $i(z,t)$ | instantaneous line voltage and current | V, A | lowercase = time domain |
| $V(z)$, $I(z)$ | phasor line voltage and current | V, A | uppercase = phasor |
| $V_0^{+}$, $V_0^{-}$ | forward / backward voltage wave amplitudes | V | ⚠ see the superscript warning above |
| $I_0^{+}$, $I_0^{-}$ | forward / backward current wave amplitudes | A | — |
| $u_p$ | phase velocity along the line | m/s | $u_p = 1/\sqrt{LC}$ |
| $\gamma$ | propagation constant **of the line** | m⁻¹ | $\sqrt{(R+j\omega L)(G+j\omega C)}$ |
| $\alpha$, $\beta$ | attenuation and phase constants | Np/m, rad/m | lossless: $\alpha = 0$, $\beta = \omega\sqrt{LC}$ |
| $Z_0$ | **characteristic impedance** of the line | Ω | $\sqrt{(R+j\omega L)/(G+j\omega C)}$; lossless $\sqrt{L/C}$. Common: 50, 75, 300 Ω |
| $Z_L$ | load impedance terminating the line | Ω | — |
| $Z_{in}(-z)$ | input impedance seen from distance $z$ **back from the load** | Ω | the argument is negative because $z$ is measured from the load |
| $z_L$, $z_N$ | **normalized** impedance $Z_L/Z_0$ | – | dimensionless; Smith chart only. Centre of chart is $1+j0$ |

### Reflection and standing waves

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $\Gamma$ | voltage reflection coefficient | – | $(Z_L-Z_0)/(Z_L+Z_0)$. $0 \le \lvert\Gamma\rvert \le 1$ for a passive load |
| $\theta_r$ | phase angle of $\Gamma$ | rad or ° | $\Gamma = \lvert\Gamma\rvert e^{j\theta_r}$ |
| $S$, VSWR, SWR | voltage standing wave ratio | – | $(1+\lvert\Gamma\rvert)/(1-\lvert\Gamma\rvert)$; $S=1$ matched, $S\to\infty$ total reflection |
| RL | return loss | dB | $-20\log_{10}\lvert\Gamma\rvert$; $\infty$ when matched |
| $z_{max}$, $z_{min}$ | positions of voltage maxima / minima | m | max-to-max is $\lambda/2$; max-to-adjacent-min is $\lambda/4$. ⚠ ·TL p9 labels the minimum $z_{max}$ (T10) |
| $d_{min}$ | distance from the load to the **first** voltage minimum | m | the slotted-line input that fixes $\theta_r$ |
| $X$ | reactance — imaginary part of a stub's input impedance | Ω | $+$ inductive, $-$ capacitive |
| $\ell$ | physical line length | m or λ | exam answers usually want it in wavelengths |

---

## Rectangular waveguides — CURRENT

*Covered by WG. See `03-waveguides.md`.*

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| $a$, $b$ | inner width and height of the guide | m | $a > b$; $a$ is the broad wall |
| $m$, $n$ | mode integers | – | $TE_{mn}$, $TM_{mn}$ |
| $TE_{mn}$ | transverse-electric mode: $E_z = 0$, $H_z \neq 0$ | – | dominant: $TE_{10}$ |
| $TM_{mn}$ | transverse-magnetic mode: $H_z = 0$, $E_z \neq 0$ | – | lowest: $TM_{11}$ |
| $e_x(x,y)$, $h_x(x,y)$, … | field components with the $e^{-j\beta z}$ factor removed | V/m, A/m | lowercase = cross-section only |
| $k$ | unbounded-medium wave number $\omega\sqrt{\mu\varepsilon}$ | rad/m | — |
| $k_c$ | cut-off wave number $\sqrt{(m\pi/a)^2 + (n\pi/b)^2}$ | rad/m | $k_c^2 = k^2 - \beta^2$ |
| $k_x$, $k_y$ | separation constants $m\pi/a$, $n\pi/b$ | rad/m | $k_c^2 = k_x^2 + k_y^2$ |
| $\beta$ | phase constant in the guide | rad/m | imaginary below cut-off |
| $\alpha$ | attenuation below cut-off, $\sqrt{k_c^2 - k^2}$ | Np/m | `[added]` — not in the handout |
| $f_c$ | cut-off frequency | Hz | $TE_{10}$: $c/2a$ |
| $\lambda_c$ | cut-off wavelength | m | $TE_{10}$: $2a$ |
| $\lambda_g$ | guide wavelength $2\pi/\beta$ | m | $\lambda/\sqrt{1-(f_c/f)^2}$ |
| $V_p$ | phase velocity in the guide | m/s | $c/\sqrt{1-(f_c/f)^2} > c$ |
| $V_g$ | group velocity | m/s | $c\sqrt{1-(f_c/f)^2} < c$. `[added]` — not in the handout |
| $Z_{TE}$ | TE wave impedance | Ω | $\eta/\sqrt{1-(f_c/f)^2}$ |
| $Z_{TM}$ | TM wave impedance | Ω | $\eta\sqrt{1-(f_c/f)^2}$. `[added]` — not in the handout |

## Computational electromagnetics — CURRENT

*Covered by CEM. See `04-computational-em.md`.*

| Symbol | Quantity | SI unit | Notes |
|---|---|---|---|
| CEM | computational electromagnetics | – | numerical solution of Maxwell's equations |
| FDM | finite-difference method | – | — |
| $\Delta x$, $\Delta y$ | grid spacing | m | — |
| $h$ | mesh size, when $\Delta x = \Delta y$ | m | — |
| $O(\Delta x^n)$ | truncation error of order $n$ | – | forward/backward $O(\Delta x)$; central $O(\Delta x^2)$ |
| $f^{(k)}(x)$ | $k$-th derivative | – | handout writes $f^k$ |
| $y_i$ | ODE solution value at node $i$ | – | — |
| $V_{i,j}$ | potential at grid node $(i, j)$ | V | $i$ along $x$, $j$ along $y$ |
| $V_0$; $V_1$–$V_4$ | molecule centre; neighbours top, left, bottom, right | V | ⚠ see the clash table |
| fixed node | boundary node, potential given | – | — |
| free node | interior node, potential unknown | – | — |

---

## Energy and power — PENDING

*No current-cohort document covers the Poynting vector yet. These symbols come from the old-cohort
material in `_reference-old-cohort/05-poynting-vector.md` and are listed so notation stays
consistent when this year's equivalent arrives.*

| Symbol | Quantity | SI unit |
|---|---|---|
| $P$ | Poynting vector $= \vec{E} \times \vec{H}$ | W/m² |
| $P_{av}$ | time-average power density $= \frac12 E_0^2/\eta$ | W/m² |
| $\varepsilon E^2/2$ | electric energy density | J/m³ |
| $\mu H^2/2$ | magnetic energy density | J/m³ |
| $T$ | period $= 1/f = 2\pi/\omega$ | s |

## Boundary and reflection — PENDING

*From `_reference-old-cohort/07-reflection-transmission.md`. Awaiting this year's equivalent.*

> ⚠ **$\Gamma$ now has two live meanings in this knowledge base.** Below it is a wave crossing a
> **material boundary**, written in intrinsic impedances $\eta$. In `02-transmission-lines.md` it is
> a wave reaching a **load on a line**, written in $Z_L$ and $Z_0$. The algebra is the same shape;
> the quantities are not. The transmission-line one is CURRENT and examinable; this one is still
> pending its handout.

| Symbol | Quantity | SI unit |
|---|---|---|
| $\Gamma$ | reflection coefficient $= (\eta_2-\eta_1)/(\eta_2+\eta_1)$ | – |
| $T$ | transmission coefficient $= 2\eta_2/(\eta_1+\eta_2)$ | – |
| $\eta_1$, $\eta_2$ | intrinsic impedances of regions 1 and 2 | Ω |
| $\gamma_1$, $\gamma_2$ | propagation constants of regions 1 and 2 | m⁻¹ |

## Polarization — PENDING ⚠ axis-convention warning

*Syllabus objective (iv), but **not** in WC1. Old-cohort coverage is in
`_reference-old-cohort/06-polarization.md`.*

> **Convention clash.** The old-cohort polarization handout propagates along **$x$** with transverse
> components $(E_y, E_z)$. WC1 propagates along **$z$** with transverse components $(E_x, E_y)$.
> Same physics, different axis labels. **Teach in WC1's $z$-propagation convention** and translate
> the old material rather than quoting its axes directly.

| Symbol | Quantity | Note |
|---|---|---|
| $a$ (scalar) | a phase angle in polarization | distinct from $\alpha$ the attenuation constant |
| $\pm j$ | the 90° phase difference producing circular polarization | — |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026. Symbol tables for the PENDING sections adapted from the old-cohort knowledge base and re-verified against WC1 where they overlap.</i></sub>
