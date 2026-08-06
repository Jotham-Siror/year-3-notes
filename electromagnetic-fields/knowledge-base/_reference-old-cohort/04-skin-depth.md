---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld"
section: "04 — Depth of Penetration & Skin Depth"
source_pages: "EMW p16–17, UPW p15–16"
file_role: topic
subtopics:
  - "why a wave dies out fast inside a conductor"
  - "definition of depth of penetration δ (attenuation to 1/e ≈ 37%)"
  - "δ = 1/α = √(2/ωμσ) = 1/√(πfμσ)"
  - "dependence on frequency, permeability, conductivity"
  - "practical consequences: surface coating, HF conduction on a thin skin"
key_equations: [skin-depth]
prerequisites: ["03-waves-in-media (good-conductor α)"]
leads_to: []
verification_flags: 0
tags: [skin-depth, depth-of-penetration, attenuation, conductor, surface-coating, high-frequency, eddy-currents]
---

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · ·EMW/UPW/POL pN provenance ·
  ⚠ VERIFY = flagged suspected handout error (see _verification-log.md). -->

# 04 — Depth of Penetration & Skin Depth

Scope: a short corollary of the good-conductor case (Topic 03). A wave entering a conductor is attenuated so
fast that it survives only a thin surface layer — the **skin depth**. This one length scale explains why HF
current flows on the surface and why cheap conductors can be silver-plated.

---

## 4.1 Why the wave dies inside a conductor ·EMW p16, UPW p15

[def] In a conducting medium the conduction losses are very high, so a propagating EM wave is **greatly
attenuated** and can penetrate **only a very short distance** below the surface. The attenuation is captured by
the factor $e^{-\alpha x}$ on a wave travelling in the +x direction (into the conductor). ·EMW p16

---

## 4.2 Definition of depth of penetration ·EMW p16, UPW p15

[def] **Depth of penetration δ** = the depth at which the wave (E, H, and J) has been attenuated to **1/e ≈ 37 %**
of its surface value. ·EMW p16, UPW p15

[derivation] With amplitude $A = A_0 e^{-\alpha x}$, the 1/e point is where $e^{-\alpha x} = e^{-1}$, i.e.
$\alpha x = 1$:
$$\delta = x = \frac{1}{\alpha}$$

[eq: skin-depth] Substituting the good-conductor value $\alpha = \sqrt{\omega\mu\sigma/2} = \sqrt{\pi f\mu\sigma}$ (Topic 03):
$$\boxed{\;\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega\mu\sigma}} = \frac{1}{\sqrt{\pi f\mu\sigma}}\;}$$
- $\delta$ = skin depth (m); $f$ = frequency (Hz); $\mu$ = permeability (H/m); $\sigma$ = conductivity (S/m).
- Also called the **skin depth**. (In a good conductor δ is very small, so the wave exists only in a thin surface
  layer.)

---

## 4.3 What δ depends on, and why it matters ·EMW p16–17, UPW p16

[def] δ depends on three things — it **decreases** as any of them rises: ·UPW p16
- **frequency** f — higher f ⇒ shallower penetration;
- **permeability** μ;
- **conductivity** σ.

[def] Practical consequences ·EMW p16–17:
- As f rises, the field/current is squeezed onto the conductor's **surface** ("skin effect").
- At **microwave frequencies** δ is tiny, so essentially all the microwave energy travels in a very thin surface
  layer. Only the **surface coating** then matters: a waveguide can be made of a poor conductor and **plated with
  a thin layer of silver or copper** to keep $I^2R$ losses low. ·EMW p17
- The dependence of δ on **μ** shows **eddy currents** are driven by $dB/dt$.

---

### Cross-references
- α = √(ωμσ/2) for a good conductor comes from → **03-waves-in-media §3.5**.
- The strong reflection off a conductor (only a little penetrates) → **03 §3.5 NOTE(4)** and
  **07-reflection-transmission**.

### Verification notes for this section
- 0 flags. Verified correct: δ = 1/α = √(2/ωμσ) = 1/√(πfμσ) (algebraically consistent with the Topic 03
  good-conductor α; the two √-forms are identical since ω = 2πf).
- Minor spelling typos on these pages ("ski depth", "atteuation") noted once in the index; no physics impact.
