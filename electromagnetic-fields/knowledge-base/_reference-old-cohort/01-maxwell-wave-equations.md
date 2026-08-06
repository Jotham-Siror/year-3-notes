---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld"
section: "01 — Maxwell's Equations & the Wave Equation"
source_pages: "EMW p1–6"
file_role: topic
subtopics:
  - "the four Maxwell equations (curl + divergence forms)"
  - "the source-free / charge-free simplification (ρ=0, σ=0)"
  - "physical interpretation: changing E makes H, changing H makes E"
  - "deriving the wave equation via curl-of-curl and the vector identity"
  - "the general lossy wave equation for E and H"
  - "harmonic (e^{jωt}) fields and the propagation constant γ = α + jβ"
key_equations: [maxwell-curlH, maxwell-curlE, maxwell-divD, maxwell-divB, wave-eqn-E, wave-eqn-H, propagation-constant]
prerequisites: ["vector calculus: curl, divergence, the identity ∇×(∇×A)=∇(∇·A)−∇²A"]
leads_to: ["02-uniform-plane-wave", "03-waves-in-media"]
verification_flags: 1
tags: [maxwell, ampere, faraday, gauss, wave-equation, curl-of-curl, harmonic-fields, propagation-constant, gamma]
---

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers, re-verified) · [exercise] unsolved problem ·
  [fig] figure described from the page image · ·EMW/UPW/POL pN = provenance (which PDF + page) ·
  ⚠ VERIFY = flagged suspected handout error; detail in _verification-log.md.
  Equations are canonical LaTeX; garbled/shorthand typed math is given in standard form, real discrepancies flagged. -->

# 01 — Maxwell's Equations & the Wave Equation

Scope: states the four Maxwell equations, simplifies them for a source-free medium, and shows how taking the curl
of Faraday's law and using a vector identity collapses them into a **wave equation** — the mathematical proof
that E and H propagate as waves. Then introduces the harmonic (phasor) form and the **propagation constant** γ
that governs everything in Topics 02–04.

---

## 1.1 The four Maxwell equations ·EMW p1

[def] Maxwell's hypothesis: a **time-varying electric field produces a magnetic field**, from the sum of the
conduction current and the displacement current. The four equations (general, for any medium):

[eq: maxwell-curlH] **Ampère's law (with Maxwell's correction):**
$$\nabla\times \mathbf H = \mathbf J_c + \frac{\partial \mathbf D}{\partial t} = \sigma\mathbf E + \varepsilon\frac{\partial \mathbf E}{\partial t}$$
- $\mathbf J_c=\sigma\mathbf E$ = conduction current density (A/m²); $\dfrac{\partial \mathbf D}{\partial t}$ = displacement current density.
- $\sigma$ = conductivity (S/m), $\varepsilon$ = permittivity (F/m), $\mathbf D=\varepsilon\mathbf E$.

[eq: maxwell-curlE] **Faraday's law:**
$$\nabla\times \mathbf E = -\frac{\partial \mathbf B}{\partial t} = -\mu\frac{\partial \mathbf H}{\partial t}$$
- $\mu$ = permeability (H/m), $\mathbf B=\mu\mathbf H$.

[eq: maxwell-divD] **Gauss's law (electric):** $\;\nabla\cdot \mathbf D = \rho$ — $\rho$ = free charge density (C/m³).

[eq: maxwell-divB] **Gauss's law (magnetic, no monopoles):** $\;\nabla\cdot \mathbf B = 0$.

---

## 1.2 The source-free simplification ·EMW p1–2

[def] Consider a **homogeneous medium with no free charge ($\rho=0$) and zero conductivity ($\sigma=0$)**. The
four equations reduce to:
$$\nabla\times \mathbf H = \varepsilon\frac{\partial \mathbf E}{\partial t}, \qquad
  \nabla\times \mathbf E = -\mu\frac{\partial \mathbf H}{\partial t}, \qquad
  \nabla\cdot \mathbf D = 0, \qquad \nabla\cdot \mathbf B = 0$$

[def] **Physical interpretation** ·EMW p2:
- A **changing E field produces a (curling) H field**; a **changing H field produces a (curling) E field**.
- The induced field appears **both where the source field is changing and in the surrounding region** — so a
  disturbance of either kind does not stay put: **energy propagates into the surrounding space.** That is the
  qualitative statement of a wave.

> Note ·EMW p3 writes "∇(V.E)=0" for the charge-free condition — read as $\nabla\cdot\mathbf E=0$ (the "V" is a
> typo for the del operator ∇). Minor, logged as a typo.

---

## 1.3 Deriving the wave equation ·EMW p3–4

[derivation] Start from Faraday's law and take the **curl of both sides** (using $\mathbf B=\mu\mathbf H$):
$$\nabla\times(\nabla\times\mathbf E) = -\mu\,\frac{\partial(\nabla\times\mathbf H)}{\partial t}$$

Apply the **vector identity** (the key step): ·EMW p3
$$\boxed{\;\nabla\times(\nabla\times\mathbf A) = \nabla(\nabla\cdot\mathbf A) - \nabla^2\mathbf A\;}$$

So the left side becomes $\nabla(\nabla\cdot\mathbf E) - \nabla^2\mathbf E$. In a charge-free medium
$\nabla\cdot\mathbf E = 0$, killing the first term. Substituting Ampère's law
$\nabla\times\mathbf H = \sigma\mathbf E + \varepsilon\,\partial\mathbf E/\partial t$ on the right gives the
**general (lossy) wave equation for E**: ·EMW p4

[eq: wave-eqn-E]
$$\boxed{\;\nabla^2\mathbf E = \mu\frac{\partial}{\partial t}\!\left(\sigma\mathbf E + \varepsilon\frac{\partial \mathbf E}{\partial t}\right)
   = \mu\sigma\frac{\partial \mathbf E}{\partial t} + \mu\varepsilon\frac{\partial^2 \mathbf E}{\partial t^2}\;}$$

[eq: wave-eqn-H] By the same procedure starting from Ampère's law, the **wave equation for H** (set as an
exercise on ·EMW p4): 
$$\nabla^2\mathbf H = \mu\sigma\frac{\partial \mathbf H}{\partial t} + \mu\varepsilon\frac{\partial^2 \mathbf H}{\partial t^2}$$

- The **σ term** (first order in time) is the **loss/damping** term; it vanishes in a lossless medium (σ=0),
  leaving the pure wave equation $\nabla^2\mathbf E = \mu\varepsilon\,\partial^2\mathbf E/\partial t^2$
  (propagation speed $1/\sqrt{\mu\varepsilon}$ — see Topic 02).

---

## 1.4 Harmonic (phasor) fields ·EMW p4–5

[def] Assume a **sinusoidal / exponential time variation** $e^{j\omega t}$:
$$\mathbf E = \mathbf E_0\,e^{j\omega t} = \mathbf E_0(\cos\omega t + j\sin\omega t)$$
Only the real part (cosine) or imaginary part (sine) is physical; carrying $e^{j\omega t}$ makes the calculus
algebraic. With this form the time derivatives become multiplications: ·EMW p5
$$\frac{\partial\mathbf E}{\partial t} = j\omega\,\mathbf E, \qquad
  \frac{\partial^2\mathbf E}{\partial t^2} = (j\omega)^2\,\mathbf E = -\omega^2\mathbf E$$

[derivation] Putting these into the wave equation (1.3) turns it into the **Helmholtz equation**: ·EMW p5
$$\nabla^2\mathbf E = \mu\big(j\omega\sigma\,\mathbf E + \varepsilon(j\omega)^2\mathbf E\big)
  = j\omega\mu(\sigma + j\omega\varepsilon)\,\mathbf E$$
$$\boxed{\;\nabla^2\mathbf E = \gamma^2\mathbf E, \qquad \nabla^2\mathbf H = \gamma^2\mathbf H\;}$$

---

## 1.5 The propagation constant γ ·EMW p5–6

[eq: propagation-constant]
$$\boxed{\;\gamma = \sqrt{\,j\omega\mu(\sigma + j\omega\varepsilon)\,} = \alpha + j\beta\;}$$
- $\gamma$ = **propagation constant** (m⁻¹) — controls all propagation behaviour (hence the name). ·EMW p6
- $\alpha$ = **attenuation constant** — rate the wave's amplitude decays (SI unit **Np/m**, nepers per metre).
- $\beta$ = **phase constant** (or phase-shift coefficient) — rate the phase advances per metre (rad/m).

[eq] Separating γ into real and imaginary parts for a **general lossy medium** gives the exact forms
(derived over EMW p6, p10–11): 
$$\alpha = \omega\sqrt{\tfrac{\mu\varepsilon}{2}}\left[\sqrt{1+\left(\tfrac{\sigma}{\omega\varepsilon}\right)^2}-1\right]^{1/2}, \qquad
  \beta = \omega\sqrt{\tfrac{\mu\varepsilon}{2}}\left[\sqrt{1+\left(\tfrac{\sigma}{\omega\varepsilon}\right)^2}+1\right]^{1/2}$$

> ⚠ VERIFY ·EMW p6 — as printed, **both** boxed results are labelled "α", and the bracket is shown raised to
> power **2**. Corrections: (1) the second one (the `…+1` form) is **β**, not α; (2) the outer operation is a
> **square root**, i.e. power **½**, not squared; (3) α's unit is **Np/m** (the page writes "dB/m" — 1 Np ≈
> 8.686 dB, so "dB/m" is only right after multiplying by 8.686). The simplified low-loss and good-conductor
> limits the handout derives later (Topic 03) are consistent with the **½-power, α-then-β** forms above, which
> confirms the p6 printing is a labelling/exponent slip. See _verification-log.md.

- Both α and β depend on **frequency ω** and on the medium constants **μ, ε, σ**. Everything in Topic 03 is just
  this γ evaluated in four limiting cases (perfect dielectric, low-loss dielectric, good conductor, general).

---

### Cross-references
- The velocity $1/\sqrt{\mu\varepsilon}$ and intrinsic impedance that fall out of these equations for a plane
  wave → **02-uniform-plane-wave**.
- γ, α, β evaluated for dielectric / lossy / conducting media → **03-waves-in-media**; the good-conductor α feeds
  skin depth → **04-skin-depth**.

### Verification notes for this section
- 1 flag: EMW p6 α/β labelling + squared-vs-half-power bracket (+ Np/m vs dB/m unit). See log.
- Verified correct: the four Maxwell equations, the curl-of-curl identity, the lossy wave equation
  $\nabla^2E=\mu\sigma\,\partial_t E+\mu\varepsilon\,\partial_t^2 E$, and γ=√(jωμ(σ+jωε)).
- Minor typo noted: EMW p3 "∇(V.E)=0" → $\nabla\cdot\mathbf E=0$.
