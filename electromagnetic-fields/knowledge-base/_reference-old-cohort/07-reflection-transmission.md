---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld"
section: "07 — Normal-Incidence Reflection & Transmission"
source_pages: "EMW p28–31"
file_role: topic
subtopics:
  - "a plane wave normally incident on a boundary between two media"
  - "incident, reflected and transmitted fields"
  - "why incident+reflected alone can't satisfy the boundary → a transmitted wave is needed"
  - "boundary conditions on tangential E and H at z=0"
  - "transmission coefficient T = 2η₂/(η₁+η₂)"
  - "reflection coefficient Γ = (η₂−η₁)/(η₂+η₁)"
  - "the relation 1 + Γ = T"
key_equations: [rt-boundary-E, rt-boundary-H, transmission-coeff, reflection-coeff, gamma-plus-one]
prerequisites: ["02-uniform-plane-wave (η)", "03-waves-in-media (η, η*)"]
leads_to: []
verification_flags: 0
tags: [reflection, transmission, normal-incidence, reflection-coefficient, transmission-coefficient, boundary-conditions, intrinsic-impedance, interface]
---

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · ·EMW/UPW/POL pN provenance ·
  ⚠ VERIFY = flagged suspected handout error (see _verification-log.md). -->

# 07 — Normal-Incidence Reflection & Transmission at a Boundary

Scope: what happens when a plane wave hits, **head-on (normal incidence)**, the flat boundary between two media
of different intrinsic impedance. Matching the fields at the boundary gives the fraction reflected (**Γ**) and
the fraction transmitted (**T**) — both set entirely by the two impedances η₁ and η₂.

---

## 7.1 The three waves ·EMW p28

[fig ·EMW p28] Region 1 (z<0) and Region 2 (z>0) meet at the plane z=0. A wave travels in +z (along $\mathbf a_z$)
and is **normally incident** on the interface. It splits into a **reflected** wave (back into region 1, −z) and a
**transmitted** wave (on into region 2, +z).

[eq] Incident wave in region 1 (propagation constant $\gamma_1=\alpha_1+j\beta_1$): ·EMW p28
$$\hat E_x^{\,i} = \hat E_{m1}^{+}e^{-\gamma_1 z}, \qquad \hat H_y^{\,i} = \frac{\hat E_{m1}^{+}}{\hat\eta_1}e^{-\gamma_1 z}$$
Transmitted wave in region 2 ($\gamma_2$): $\;\hat E_x^{\,t} = \hat E_{m2}^{+}e^{-\gamma_2 z}, \;
\hat H_y^{\,t} = \dfrac{\hat E_{m2}^{+}}{\hat\eta_2}e^{-\gamma_2 z}$.
- $\hat\eta_1,\hat\eta_2$ = intrinsic impedances of the two media (complex if lossy — Topic 03).

---

## 7.2 Why a reflected wave is unavoidable ·EMW p29

[derivation] Apply the boundary conditions at z=0 with **only** an incident + transmitted wave:
- tangential E continuous: $\hat E_{m1}^{+} = \hat E_{m2}^{+}$;
- tangential H continuous: $\dfrac{\hat E_{m1}^{+}}{\hat\eta_1} = \dfrac{\hat E_{m2}^{+}}{\hat\eta_2}$.

These two can hold together **only if $\hat\eta_1=\hat\eta_2$** — i.e. only if the media are identical. For any
real interface, therefore, a **reflected wave must also exist** to satisfy both conditions. ·EMW p29

---

## 7.3 Boundary conditions with the reflected wave ·EMW p29–30

[eq: rt-boundary-E] At z=0, tangential **E** continuous (incident + reflected = transmitted): ·EMW p29
$$\hat E_{m1}^{+} + \hat E_{m1}^{-} = \hat E_{m2}^{+}$$

[eq: rt-boundary-H] At z=0, tangential **H** continuous: ·EMW p30
$$\frac{\hat E_{m1}^{+}}{\hat\eta_1} + \frac{\hat E_{m1}^{-}}{\hat\eta_1} \cdot(-1)= \frac{\hat E_{m2}^{+}}{\hat\eta_2}
  \quad\Longrightarrow\quad \frac{\hat E_{m1}^{+}}{\hat\eta_1} - \frac{\hat E_{m1}^{-}}{\hat\eta_1} = \frac{\hat E_{m2}^{+}}{\hat\eta_2}$$
(the reflected wave's H reverses sign so its Poynting vector points back along −z). ·EMW p29

---

## 7.4 Transmission and reflection coefficients ·EMW p30

[derivation] Solve the two boundary equations simultaneously. Multiply the E-equation by η₁ and add/subtract:

[eq: transmission-coeff] **Transmission coefficient** = transmitted / incident E amplitude:
$$\boxed{\;T = \frac{\hat E_{m2}^{+}}{\hat E_{m1}^{+}} = \frac{2\hat\eta_2}{\hat\eta_1 + \hat\eta_2}\;}$$

[eq: reflection-coeff] **Reflection coefficient** = reflected / incident E amplitude:
$$\boxed{\;\Gamma = \frac{\hat E_{m1}^{-}}{\hat E_{m1}^{+}} = \frac{\hat\eta_2 - \hat\eta_1}{\hat\eta_2 + \hat\eta_1}\;}$$

[eq: gamma-plus-one] The two are linked (add 1 to Γ): ·EMW p30
$$\boxed{\;1 + \Gamma = T\;}$$
- **Check:** $1+\dfrac{\eta_2-\eta_1}{\eta_2+\eta_1} = \dfrac{(\eta_2+\eta_1)+(\eta_2-\eta_1)}{\eta_2+\eta_1} = \dfrac{2\eta_2}{\eta_2+\eta_1} = T$. ✓ (re-verified)
- **Limiting cases:** η₂=η₁ ⇒ Γ=0, T=1 (no reflection, matched). η₂=0 (perfect conductor, region 2) ⇒ Γ=−1,
  T=0 (total reflection, wave excluded from the conductor — ties back to Topic 03 §3.5 NOTE 5).

> ·EMW p31 is a blank "Questions" page — no problems were printed there.

---

### Cross-references
- η (real dielectric) and η* (complex, lossy/conducting) → **02-uniform-plane-wave**, **03-waves-in-media**.
- Total reflection off a perfect conductor → **03 §3.5**; power split uses the Poynting vector → **05**.

### Verification notes for this section
- 0 flags. Verified correct: T=2η₂/(η₁+η₂), Γ=(η₂−η₁)/(η₂+η₁), and the identity **1+Γ=T** (checked
  algebraically and numerically).
- Minor spelling typos on these pages ("ad"→and, "I the negative direction") noted once in the index; no physics
  impact.
