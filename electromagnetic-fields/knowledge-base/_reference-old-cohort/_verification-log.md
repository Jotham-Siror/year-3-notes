---
kb: "Electromagnetic Fields — Year 3"
file_role: verification-log
purpose: "Every flagged discrepancy between a handout page and an independently checked standard form. Handout-faithful content is preserved in the topic files; nothing is silently 'corrected'."
scale: "3 source PDFs (EMW 31 pp, UPW 16 pp, POL 4 pp); grows if more material is added"
---

# Verification log

Format per entry: **·CODE pN** — what the page says → the issue → checked standard form → note.
Codes: **EMW** = ELECTROMAGNETIC WAVES.pdf, **UPW** = THE UNIFORM PLANE WAVE.pdf, **POL** = POLARIZATION OF WAVES.pdf.
Severity: `error` (wrong result), `notation` (dimensionally/typographically loose but intent clear),
`typo` (trivial), `ok-nonstandard` (unusual but defensible), `convention` (a labelling choice, not an error).

---

## Substantive flags (do not let a learner absorb the raw version)

### ·EMW p6 — exact α and β: mislabelled and wrong exponent
- **Page:** prints two boxed results, **both labelled "α"**; the first with unit "dB/m" and a **squared**
  bracket, the second (the `…+1` form) with unit "rad/m".
- **Issues:** (1) the second result is **β**, not α; (2) the outer operation is a **square root**, i.e. power
  **½**, not squared; (3) α's SI unit is **Np/m** (nepers/m), not dB/m (1 Np = 8.686 dB).
- **Correct (standard):**
  $\alpha=\omega\sqrt{\tfrac{\mu\varepsilon}{2}}\big[\sqrt{1+(\sigma/\omega\varepsilon)^2}-1\big]^{1/2}$ (Np/m),
  $\beta=\omega\sqrt{\tfrac{\mu\varepsilon}{2}}\big[\sqrt{1+(\sigma/\omega\varepsilon)^2}+1\big]^{1/2}$ (rad/m).
- **Consistency check:** the handout's own low-loss limits (EMW p11 / UPW p11: α≈(σ/2)√(μ/ε),
  β≈ω√(με)[1+⅛(σ/ωε)²]) and good-conductor limits (α=β=√(ωμσ/2)) follow from the ½-power α-then-β forms — so
  p6 is a labelling/exponent printing slip, not a different physics.
- **Severity:** error (labelling + exponent) / notation (unit). Topic 01 §1.5, Topic 03 §3.3.

### ·EMW p14 & UPW p13–14 — good conductor: β printed as α
- **Page:** after $\gamma=\sqrt{\omega\mu\sigma/2}\,(1+j)$ is split into real and imaginary parts, both lines are
  labelled "**α**" (α=√(ωμσ/2)[1−ωε/2σ] and α=√(ωμσ/2)[1+ωε/2σ]).
- **Issue:** the **second** line is **β**. (The two approximate to the same value α=β=√(ωμσ/2), which is correct
  for a good conductor — only the symbol on the second line is wrong.)
- **Correct:** $\alpha=\beta=\sqrt{\dfrac{\omega\mu\sigma}{2}}=\sqrt{\pi f\mu\sigma}$. Verified numerically
  (√(ωμσ/2)=√(πfμσ) identically).
- **Severity:** error (label). Topic 03 §3.5.

### ·UPW p15 — Example 1 answer, H-field unit
- **Page:** answer bracket "[1.88×10⁸ m/s, 3.77 cm, 166.6 rad/m; **42.2 μ/m**]".
- **Issue:** the H-field unit "μ/m" is missing the ampere — it should be **μA/m** (microamperes per metre).
- **Value is correct:** re-solved with polystyrene εᵣ=2.53 → v_p=1.886×10⁸ m/s, λ=3.77 cm, β=166.6 rad/m,
  η=237 Ω, H=E/η=0.010/237=4.22×10⁻⁵ A/m = **42.2 μA/m**. All four printed values reproduced exactly.
- **Severity:** typo (unit). Topic 03 §3.6.

### ·POL p4 — circular polarization phase condition
- **Page:** "To get this type of polarization **180°** phase between two components is required."
- **Issue:** circular polarization requires a **90° (π/2)** phase difference between equal-amplitude components
  (the ±j). POL's own math on the same page uses 90° (Ey=Ea cos ωt, Ez=Ea sin ωt ⇒ Ey²+Ez²=Ea², a circle). A
  **180°** phase difference gives **linear** polarization, not circular. The "180°" only makes sense as the
  *difference between* the left-hand (+j) and right-hand (−j) cases.
- **Correct:** 90° (±j) with equal amplitudes ⇒ circular; sign of j sets left/right hand.
- **Severity:** error/misleading wording. Topic 06 §6.3.

### ·EMW p27 — elliptical real-time field, repeated component
- **Page:** "$E(z,t)=E_x(z,t)\mathbf a_x + E_x(z,t)\mathbf a_y$".
- **Issue:** the **second** term should be **$E_y(z,t)\mathbf a_y$**, not $E_x$. (A wave with two equal-labelled
  components would just be linear along the diagonal — not the ellipse the section is describing.)
- **Severity:** typo. Topic 06 §6.4.

---

## Minor / grouped

### Pervasive spelling & OCR-style typos (EMW, UPW)
- Frequent small transcription errors that do **not** affect the physics, logged once here rather than per
  instance: "ca"→can, "ad"→and, "I"→in, "coductivity"→conductivity, "atteuation"→attenuation, "Poyting"→Poynting,
  "ski depth"→skin depth, "constrction"→contraction, "indicted"→indicated, "sum by the sum" (EMW p1, repeated
  words), "∇(V.E)=0" (EMW p3) → $\nabla\cdot\mathbf E=0$.
- **Severity:** typo (cosmetic).

### ·UPW p3 — heading names wrong operator
- **Page:** heading "Writing ∇×E in full form, we have in rectangular form" appears directly above the **∇×H**
  expansion.
- **Issue:** the expansion shown is of ∇×H, not ∇×E; content is correct, only the heading names the wrong
  operator. **Severity:** typo (label).

---

## Convention notes (NOT errors)

### Polarization axis convention differs between handouts
- **EMW (p24–27):** wave propagates along **z**; transverse components **(Eₓ, E_y)**.
- **POL (p1–4):** wave propagates along **x**; transverse components **(E_y, E_z)**; "polarized in the y-direction
  if E_z=0", etc.
- Both are internally consistent and physically identical — just different axis labels. The topic files adopt
  **EMW's z-propagation, (Eₓ,E_y)** convention. When teaching, state which convention you're using and don't mix
  the two axis sets within one problem. **Severity:** convention.

<!-- If more EM Fields material is added later, append its flags below. -->
