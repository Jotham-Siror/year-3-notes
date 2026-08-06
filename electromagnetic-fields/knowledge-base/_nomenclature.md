---
kb: "Electromagnetic Fields — EEE3202"
file_role: nomenclature
purpose: "Every symbol used in the handouts with meaning and SI units. Resolves symbol clashes. Consult this when a topic file's notation is ambiguous."
scope: "Sections marked CURRENT are covered by a current-cohort handout. Sections marked PENDING are carried over from the old cohort and await this year's handout."
---

# Nomenclature and symbols

## ⚠ Symbol clashes and look-alikes — read first

This subject is unusually bad for symbol collisions, and **the handout itself makes one of them**.
Flag these explicitly when teaching.

| Symbol | Meaning | Clash / warning |
|---|---|---|
| **$\sigma$** | **conductivity** (S/m, formerly mho/m) | ⚠ **WC1 repeatedly prints $\sigma$ where it means $\alpha$** — pp. 9, 10 and 16, six equations. See `_verification-log.md` V9, V12, V14, V15, V19. Where an equation has $\sigma$ on *both* sides, the left-hand one is $\alpha$ |
| **$\alpha$** | **attenuation constant** (Np/m) | the victim of the collision above. Multiply by 8.686 to convert Np/m → dB/m |
| **$\beta$** | **phase constant** / phase-shift constant (rad/m) | always the phase constant in this subject; also mislabelled as $\alpha$ in the old-cohort handouts |
| **$\gamma$** | **propagation constant** $= \alpha + j\beta$ (m⁻¹) | not the ratio of specific heats (that is Thermodynamics) |
| **$\eta$** | **intrinsic impedance** $\sqrt{\mu/\varepsilon}$ (Ω); $\eta^*$ = complex $\eta$ in a lossy medium | not efficiency. ⚠ WC1 p11 writes the impedance angle as $\theta_n$; the subscript is $\eta$, not the letter n |
| **$\mu$** | **permeability** (H/m) | also the SI prefix **micro** ($10^{-6}$) — "μA/m" is microamps per metre. Watch context |
| **$\varepsilon$** | **permittivity** (F/m); $\varepsilon^*$ = complex permittivity | $\varepsilon_0$ = free-space value |
| **$\rho_v$** vs **$\rho_s$** | $\rho_v$ = **volume** charge density (C/m³) — the one used throughout | $\rho_s$ = *surface* charge density (C/m²). ⚠ WC1 p3 prints $\rho_s$ where $\rho_v$ is meant (V6) |
| **$\delta$** | **skin depth / depth of penetration** (m) | not a boundary-layer thickness (that is Fluid Flow) |
| **$\theta$** | **loss-tangent angle**, $\tan\theta = \sigma/\omega\varepsilon$ | distinguish from $\theta_\eta$, the impedance angle, which is *half* the arctangent |
| **$k$** vs **$\beta$** | $k = \omega\sqrt{\mu\varepsilon}$ is the **wave number** in a lossless medium | in a lossless medium $k$ and $\beta$ coincide; in a lossy one they do not |
| **$\mathbf{a}$** vs **$\alpha$** | $\mathbf{a}_x, \mathbf{a}_y, \mathbf{a}_z$ = **unit vectors** | visually close to $\alpha$ in the handout's font |
| **$J$** | current density (A/m²) — $J_c$ conduction, $J_{disp}$ displacement | not to be confused with $j = \sqrt{-1}$ |

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
| $\gamma$ | propagation constant $= \alpha + j\beta$ | m⁻¹ | $\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon)$ |
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

## Vectors and operators — CURRENT

| Symbol | Meaning |
|---|---|
| $\mathbf{a}_x, \mathbf{a}_y, \mathbf{a}_z$ | unit vectors along $x$, $y$, $z$ |
| $\nabla \times$ | curl |
| $\nabla \cdot$ | divergence |
| $\nabla^2$ | Laplacian ⚠ **WC1 p5 omits the squares — see V2** |
| $j$ | imaginary unit $\sqrt{-1}$; $\sqrt{j} = (1+j)/\sqrt{2}$; $e^{j\pi/4} = (1+j)/\sqrt{2}$ |
| $\bar{A}$ | the dummy vector of the identity $\nabla \times \nabla \times \bar{A} = \nabla(\nabla\cdot\bar{A}) - \nabla^2\bar{A}$ — **not a field**. ⚠ WC1 leaves it in three boxed results that should read $\bar{H}$ (V5) |

---

## Energy and power — PENDING

*No current-cohort handout covers the Poynting vector yet. These symbols come from the old-cohort
material in `_reference-old-cohort/05-poynting-vector.md` and are listed so notation stays
consistent when this year's handout arrives.*

| Symbol | Quantity | SI unit |
|---|---|---|
| $P$ | Poynting vector $= \vec{E} \times \vec{H}$ | W/m² |
| $P_{av}$ | time-average power density $= \frac12 E_0^2/\eta$ | W/m² |
| $\varepsilon E^2/2$ | electric energy density | J/m³ |
| $\mu H^2/2$ | magnetic energy density | J/m³ |
| $T$ | period $= 1/f = 2\pi/\omega$ | s |

## Boundary and reflection — PENDING

*From `_reference-old-cohort/07-reflection-transmission.md`. Awaiting this year's handout.*

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

<sub><i>Compiled by Jotham-JS · 2026. Symbol tables for the PENDING sections adapted from the old-cohort knowledge base and re-verified against WC1 where they overlap.</i></sub>
