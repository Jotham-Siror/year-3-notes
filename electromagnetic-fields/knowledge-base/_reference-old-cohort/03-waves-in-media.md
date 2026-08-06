---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld"
section: "03 — Plane Waves in Material Media"
source_pages: "EMW p9–15, UPW p7–14"
file_role: topic
subtopics:
  - "loss tangent tanθ = σ/ωε; conduction vs displacement current"
  - "complex permittivity ε* and the general propagation constant"
  - "classifying a medium: conductor vs dielectric (σ/ωε test)"
  - "plane waves in a lossy dielectric (low-loss): α, β, vₚ, η*"
  - "plane waves in a perfect (lossless) dielectric: α=0, β=ω√με, η=√(μ/ε)"
  - "plane waves in a good conductor: α=β=√(ωμσ/2), η*=√(ωμ/σ)∠45°"
  - "worked example 1 — 5 GHz wave in polystyrene"
  - "worked example 2 — is a medium a conductor or dielectric at 50 kHz vs 10 GHz?"
key_equations: [loss-tangent, complex-permittivity, gamma-general, lossy-alpha-beta, dielectric-perfect, conductor-alpha-beta, conductor-eta, vp-general]
prerequisites: ["01-maxwell-wave-equations", "02-uniform-plane-wave"]
leads_to: ["04-skin-depth", "05-poynting-vector", "07-reflection-transmission"]
verification_flags: 3
tags: [loss-tangent, complex-permittivity, lossy-dielectric, perfect-dielectric, good-conductor, attenuation, phase-constant, phase-velocity, intrinsic-impedance, polystyrene, conductor-or-dielectric]
---

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · ·EMW/UPW/POL pN provenance ·
  ⚠ VERIFY = flagged suspected handout error (see _verification-log.md). -->

# 03 — Plane Waves in Material Media

Scope: this is the **core, most exam-relevant** topic. It takes the general γ from Topic 01 and evaluates it in
the media a wave can travel through — classifying each by the **loss tangent** σ/ωε — to get α, β, phase velocity
and intrinsic impedance for a lossy dielectric, a perfect dielectric, and a good conductor. Ends with the two
worked examples (both re-solved and confirmed).

> **Overlap note:** EMW (p9–15) and UPW (p7–14) present this material almost identically. Citations give both.

---

## 3.1 Conduction vs displacement current — the loss tangent ·EMW p9, UPW p7–8

[def] From Ampère's law $\nabla\times\mathbf H = \mathbf J_c + \dfrac{\partial\mathbf D}{\partial t}
= \sigma\mathbf E + \varepsilon\dfrac{\partial\mathbf E}{\partial t} = \mathbf J_c + \mathbf J_{disp}$:
- $\mathbf J_c = \sigma\mathbf E$ = **conduction** current density (in phase with E);
- $\mathbf J_{disp} = j\omega\varepsilon\mathbf E$ = **displacement** current density (leads E by 90°).

[eq: loss-tangent] Their ratio defines the **loss tangent**:
$$\boxed{\;\frac{J_c}{J_{disp}} = \frac{\sigma}{\omega\varepsilon}, \qquad \tan\theta = \frac{\sigma}{\omega\varepsilon}\;}$$
- $\theta$ = the angle by which the displacement current leads the **total** current density. ·EMW p9, UPW p8
- A **small** loss tangent (σ/ωε ≪ 1) ⇒ displacement current dominates ⇒ the medium behaves like a **dielectric**.
- A **large** loss tangent (σ/ωε ≫ 1) ⇒ conduction current dominates ⇒ the medium behaves like a **conductor**.
- **Both σ/ωε and the medium constant depend on frequency** — the *same* material can be a conductor at low f
  and a dielectric at high f (see Example 2).

---

## 3.2 Complex permittivity & the classification test ·EMW p9–10, UPW p9

[eq: complex-permittivity] The general propagation constant can be written with a **complex permittivity** ε*:
$$\gamma = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)} = j\omega\sqrt{\mu\varepsilon^{*}}, \qquad
  \boxed{\;\varepsilon^{*} = \varepsilon\left(1 - \frac{j\sigma}{\omega\varepsilon}\right)\;}$$

[table] Using σ/ωε to classify a medium at a given frequency ·EMW p9, UPW p9:

| Condition | Behaviour |
|---|---|
| Conduction current dominates, $\sigma/\omega\varepsilon \gg 1$ | **Conductor** |
| Displacement current dominates, $\sigma/\omega\varepsilon \ll 1$ | **Dielectric** |
| $\sigma/\varepsilon = \omega$ (loss tangent = 1) | borderline — properties of both |

Frequency ω and the ratio σ/ε are enough to characterise a medium.

---

## 3.3 General lossy dielectric (low-loss) ·EMW p10–12, UPW p9–11

[def] A **lossy dielectric** has small but non-zero conductivity: σ/ωε ≪ 1 but ≠ 0. A little energy is absorbed
from the wave each metre.

[derivation] With σ/ωε ≪ 1, expand $\gamma = j\omega\sqrt{\mu\varepsilon}\left(1-\frac{j\sigma}{\omega\varepsilon}\right)^{1/2}$
**binomially** and keep the first terms; separating real and imaginary parts: ·EMW p10–11, UPW p10–11

[eq: lossy-alpha-beta]
$$\boxed{\;\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}}\;(\text{Np/m}), \qquad
  \beta \approx \omega\sqrt{\mu\varepsilon}\left[1 + \frac{1}{8}\left(\frac{\sigma}{\omega\varepsilon}\right)^{2}\right]\;(\text{rad/m})\;}$$

[eq: vp-general] **Phase velocity** and **intrinsic impedance** (low-loss): ·EMW p11–12, UPW p11
$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\varepsilon}\left[1+\frac18(\sigma/\omega\varepsilon)^2\right]}, \qquad
  \eta^{*} = \sqrt{\frac{\mu}{\varepsilon^{*}}} \approx \sqrt{\frac{\mu}{\varepsilon}}\left(1 + \frac{j\sigma}{2\omega\varepsilon}\right) \approx \eta\left(1+\frac{j\sigma}{2\omega\varepsilon}\right)$$
- The finite σ adds a **small reactive (imaginary) part** to η — i.e. a small loss. For most practical purposes
  the reactive part is neglected. ·EMW p12

> ⚠ VERIFY ·EMW p6 (the exact α, β) — see Topic 01 §1.5: both were printed as "α" and squared instead of √.
> The low-loss forms above (derived on EMW p11 / UPW p11) are the correct, consistent limits. See log.

---

## 3.4 Perfect (lossless) dielectric ·EMW p12–13, UPW p11–12

[def] A **perfect dielectric** is lossless: **σ = 0**. Then the loss tangent is zero and:

[eq: dielectric-perfect] ·EMW p13, UPW p12
$$\boxed{\;\alpha = 0, \qquad \beta = \omega\sqrt{\mu\varepsilon}, \qquad
  v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\varepsilon}}, \qquad \eta = \sqrt{\frac{\mu}{\varepsilon}}\;}$$
- **No attenuation** (α=0): the wave travels forever without losing amplitude.
- These are exactly the free-space results of Topic 02 with ε₀,μ₀ replaced by the medium's ε,μ. Free space is
  the special case ε=ε₀, μ=μ₀ (η=377 Ω, v=c).

---

## 3.5 Good conductor ·EMW p13–15, UPW p12–14

[def] A **good conductor** has σ/ωε ≫ 1 (equivalently ωε/σ ≪ 1): conduction current dominates and the complex
permittivity reduces to $\varepsilon^{*} \approx -\,j\sigma/\omega$. ·EMW p14

[derivation] Then $\gamma = \sqrt{j\omega\mu\sigma}$. Using $\sqrt{j} = (1+j)/\sqrt2$ (so $\sqrt{-j}=e^{-j\pi/4}$): ·EMW p14, UPW p13
$$\gamma = \sqrt{j\omega\mu\sigma} = \sqrt{\frac{\omega\mu\sigma}{2}}\,(1+j) = \alpha + j\beta$$

[eq: conductor-alpha-beta] Equating real and imaginary parts (they are **equal**): ·EMW p14–15, UPW p13–14
$$\boxed{\;\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \sqrt{\pi f\mu\sigma}\;}$$

[eq: conductor-eta] Phase velocity and (complex) intrinsic impedance of a conductor: ·EMW p15
$$v_p = \frac{\omega}{\beta} = \sqrt{\frac{2\omega}{\mu\sigma}}, \qquad
  \eta^{*} = \sqrt{\frac{j\omega\mu}{\sigma}} = \sqrt{\frac{\omega\mu}{2\sigma}}\,(1+j) = \sqrt{\frac{\omega\mu}{\sigma}}\angle 45^{\circ}$$

> ⚠ VERIFY ·EMW p14 & UPW p13–14 — after separating real/imaginary parts the second boxed line is again labelled
> "α". It is **β**. The equal value α=β=√(ωμσ/2) is correct; only the symbol on the second line is wrong. See log.

[def] **NOTE — consequences for a good conductor** ·EMW p15, UPW p14:
1. σ large ⇒ α and β both very large ⇒ the wave is **strongly attenuated** and undergoes a large phase shift per
   metre.
2. $v_p$ is **very small** (large σ) ⇒ the wavelength shrinks sharply as the wave crosses from free space into
   the conductor.
3. η* is **small** and has a reactive component (45° phase).
4. On hitting a conductor most of the wave is **reflected**; only a little penetrates (a real metal, σ≠∞, is an
   *imperfect* conductor and supports a rapidly-attenuating wave). → Topic 04 (skin depth).
5. In a **perfect conductor** (σ=∞), α and β are infinite, $v_p$ and λ are zero ⇒ **no wave can exist inside**.

---

## 3.6 Worked examples ·UPW p15

### [ex] Example 1 — 5 GHz plane wave in polystyrene ·UPW p15
A 5 GHz uniform plane wave propagates in polystyrene; the E-field amplitude is 10 mV/m. Find (a) the velocity of
propagation, (b) the wavelength in polystyrene, (c) the phase constant, (d) the amplitude of H.
**Handout answers:** $v_p=1.88\times10^{8}$ m/s, λ = 3.77 cm, β = 166.6 rad/m, H = 42.2 μA/m.

Solution (polystyrene: $\mu_r=1$, and the answers imply $\varepsilon_r \approx 2.53$; lossless dielectric):
- (a) $v_p = \dfrac{c}{\sqrt{\varepsilon_r}} = \dfrac{3\times10^{8}}{\sqrt{2.53}} = 1.886\times10^{8}$ m/s. ✓
- (b) $\lambda = \dfrac{v_p}{f} = \dfrac{1.886\times10^{8}}{5\times10^{9}} = 0.0377\text{ m} = 3.77$ cm. ✓
- (c) $\beta = \dfrac{2\pi}{\lambda} = \dfrac{\omega}{v_p} = 166.6$ rad/m. ✓
- (d) $\eta = \dfrac{\eta_0}{\sqrt{\varepsilon_r}} = \dfrac{377}{\sqrt{2.53}} = 237\ \Omega$;
  $H = \dfrac{E}{\eta} = \dfrac{0.010}{237} = 4.22\times10^{-5}\text{ A/m} = 42.2\ \mu\text{A/m}$. ✓
- **All four re-verified numerically** (εr=2.53 reproduces every printed value exactly).

> ⚠ VERIFY ·UPW p15 — the (d) answer is printed "**42.2 μ/m**". The unit is **μA/m** (microamperes per metre);
> the number 42.2 is correct. See _verification-log.md.

### [ex] Example 2 — conductor or dielectric? ·UPW p15
A medium has $\sigma = 0.1$ S/m (mho/m), $\mu_r = 1$, $\varepsilon_r = 40$ (assumed frequency-independent). Does
it behave as a conductor or a dielectric at (a) 50 kHz and (b) 10 GHz?

Solution — evaluate the **loss tangent** $\sigma/\omega\varepsilon$ with $\varepsilon = 40\varepsilon_0 = 3.54\times10^{-10}$ F/m:
- (a) f = 50 kHz: $\omega\varepsilon = 2\pi(5\times10^{4})(3.54\times10^{-10}) = 1.11\times10^{-4}$;
  $\dfrac{\sigma}{\omega\varepsilon} = \dfrac{0.1}{1.11\times10^{-4}} \approx 899 \gg 1$ ⇒ **CONDUCTOR**.
- (b) f = 10 GHz: $\omega\varepsilon = 2\pi(10^{10})(3.54\times10^{-10}) = 22.25$;
  $\dfrac{\sigma}{\omega\varepsilon} = \dfrac{0.1}{22.25} \approx 0.0045 \ll 1$ ⇒ **DIELECTRIC**.
- **Verified numerically.** This is the classic point of §3.1: the *same* medium switches character with frequency.

---

### Cross-references
- The good-conductor α → **04-skin-depth** (δ = 1/α).
- η (real for a dielectric, complex for a conductor) sets reflection/transmission → **07-reflection-transmission**.
- The general γ, α, β come from → **01-maxwell-wave-equations §1.5**; η, v from → **02-uniform-plane-wave**.

### Verification notes for this section
- 3 flags: EMW p6 exact α/β (labelling + ½-power — carried from Topic 01); EMW p14 / UPW p13–14 good-conductor
  β-labelled-α; UPW p15 Example 1 unit "μ/m"→"μA/m". All in the log.
- Verified correct (numerically or against standard forms): loss tangent test, low-loss α=σ/2·√(μ/ε) &
  β=ω√(με)[1+⅛(σ/ωε)²], perfect-dielectric set, good-conductor α=β=√(ωμσ/2)=√(πfμσ), η*=√(ωμ/σ)∠45°, and
  **both worked examples** (polystyrene answers with εr=2.53; conductor@50 kHz / dielectric@10 GHz).
