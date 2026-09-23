---
kb: "Electromagnetic Fields — EEE3202"
file_role: verification-log
purpose: "Every suspected error found in the current-cohort handouts, with what the page prints, the correct form, and why. Consult before teaching any section; prefer the corrected form."
sources_covered: "WC1 (18 pp.) — § A–D; TL (16 pp.) and TLT (22 pp.) — § T; past papers — § E"
totals: "67 source flags — WC1: 20 substantive (V1–V20) + 23 cosmetic (C1–C23) in § A–D; TL/TLT: 12 substantive (T1–T12) + 12 cosmetic (C24–C35) in § T. Plus 37 exam-paper defects (P1–P37) in § E"
method: "Every page rendered to image and read directly (not from the PDF text layer, which mangles mathematics). All numerical claims re-computed."
---

# Verification log — Electromagnetic Fields (EEE3202)

**How to use this.** When teaching from `01-wave-characteristics-1.md`, use the corrected form.
Mention the handout's own version only where the student needs to recognise it — for instance when
working from the printed page in a tutorial or exam.

**The one-line summary:** the physics in WC1 is sound; the transcription is not. Two failure modes
dominate — **a wrong constant** ($\mu_0$), and **a symbol collision** where $\sigma$ is used for both
conductivity and the attenuation constant $\alpha$, corrupting six equations across pp. 9–11 and 16.

---

## § A — Substantive errors (would teach something false)

Ordered by seriousness.

### V1 · p8 · The value of $\mu_0$ ★ most serious

**Prints:** $\mu_0 = 4\pi \times 10^{-12}\ H/m$
**Correct:** $\mu_0 = 4\pi \times 10^{-7}\ H/m$

With the printed value, $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = \mathbf{1.19\ \Omega}$ — not the
377 Ω stated on the very next line — and $c = 1/\sqrt{\mu_0\varepsilon_0} = 9.49\times10^{10}$ m/s,
about **317× the speed of light**. Self-contradictory within three lines.
*(Both values re-computed numerically.)* $\varepsilon_0 = 10^{-9}/36\pi$ F/m on the same line is
correct.

### V2 · p5 · Laplacian operator missing its squares

**Prints:** $\nabla^2 = \dfrac{\partial}{\partial x} + \dfrac{\partial}{\partial y} + \dfrac{\partial}{\partial z}$
**Correct:** $\nabla^2 = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} + \dfrac{\partial^2}{\partial z^2}$

As printed this is a first-order operator and cannot produce the $\partial^2\bar{E}/\partial z^2$
appearing in eq. 11 three lines below.

### V3 · p6 · Harmonic-form Ampère's law

**Prints:** $\nabla \times \vec{H} = j\omega\varepsilon E + j\omega\sigma E$
**Correct:** $\nabla \times \vec{H} = \sigma E + j\omega\varepsilon E = (\sigma + j\omega\varepsilon)E$

Only $\partial D/\partial t$ acquires the $j\omega$ factor; the conduction term $J = \sigma E$ is not
time-differentiated. The handout's own $\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon)$ (pp. 9,
13) **requires** $\sigma E$ — the page contradicts itself.

### V4 · p1 · Conductivity replaced by permittivity (twice)

**Prints:** $\nabla \times \nabla \times \vec{H} = \left(\nabla \times \varepsilon\frac{\partial E}{\partial t}\right) + \varepsilon(\nabla \times E)$, and again in eq. 5
**Correct:** second term is $\sigma(\nabla \times E)$ in both lines

The bracket printed directly beneath states $\vec{J} = \sigma\vec{E}$, and the next step (p2)
correctly yields $-\mu\sigma\,\partial H/\partial t$.

### V5 · pp. 2, 3, 4 · Wave equation written for the wrong variable (3 occurrences)

**Prints:** eqs. 6, 8 and 10 all as $\nabla^2\bar{A} = \ldots$
**Correct:** $\nabla^2\bar{H} = \ldots$

$\bar{A}$ is only the dummy vector of the identity
$\nabla \times \nabla \times \bar{A} = \nabla(\nabla \cdot \bar{A}) - \nabla^2\bar{A}$. Eq. 9 on p3
writes $\nabla^2\bar{H}$ correctly, confirming the slip.

### V6 · p3 · Charge-density symbol, and an invalid chain of equalities

**Prints:** $\nabla \cdot \bar{D} = \rho_s = \nabla \cdot \bar{E} = 0$
**Correct:** $\nabla \cdot \bar{D} = \rho_v = 0$, hence $\nabla \cdot \bar{E} = 0$ — **two** statements

$\rho_s$ is *surface* charge density (C/m²); the quantity meant is the *volume* density $\rho_v$
(C/m³), as correctly used in eq. 3 on p1. Separately, $\nabla \cdot \bar{D}$ (C/m³) and
$\nabla \cdot \bar{E}$ (V/m²) differ by a factor $\varepsilon$ and cannot be set equal.

### V7 · p4 · Definition of a uniform plane wave

**Prints:** "Wave properties (e.g the electric field) are identical **across any chosen direction**"
**Correct:** identical at every point of any plane **perpendicular to the direction of propagation**

As written it is false: the field certainly varies along the propagation direction $z$ — that
variation *is* the wave.

### V8 · p6 · Figure 1 axis label

**Prints:** horizontal axis labelled $t$
**Correct:** $z$

The profiles $f(z,0)$ and $f(z,t)$ are separated on that axis by the dimensioned interval $vt$,
which is a *distance*. Plotting $F$ against $t$ cannot show a spatial displacement.

### V9 · p9 · "real value $\sigma$"

**Prints:** "The propagation constant is complex with real value $\sigma$ and complex value $\beta$."
**Correct:** real part $\alpha$, imaginary part $\beta$

$\sigma$ is the conductivity, already in use. And $\beta$ is the *imaginary* part, not a "complex
value". **This sentence is the origin of the $\sigma$/$\alpha$ collision** that then corrupts V12,
V14, V15 and V19.

### V10 · pp. 9, 10, 16 · Bracket grouping in $\alpha$ and $\beta$

**Prints:** the outer radical spans everything, but with **no bracket** grouping
$\left[\sqrt{1+(\sigma/\omega\varepsilon)^2} \mp 1\right]$ as the factor multiplying $\mu\varepsilon/2$.
Read literally: $\omega\sqrt{(\mu\varepsilon/2)\sqrt{1+(\sigma/\omega\varepsilon)^2} - 1}$.

**Correct:**
$$\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1\right]}, \qquad \beta = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1\right]}$$

The $\mp 1$ must sit **inside** the bracket, multiplied by $\mu\varepsilon/2$. Only visible on the
rendered page — the text layer hides it entirely.

### V11 · p9 · Squaring the propagation constant

**Prints:** $(\sigma + j\beta)^2 = \alpha^2 - \beta^2 + j2\alpha\beta$
**Correct:** $(\alpha + j\beta)^2 = \alpha^2 - \beta^2 + j2\alpha\beta$

The RHS *is* the expansion of $(\alpha + j\beta)^2$, and $\gamma = \alpha + j\beta$ was defined one
line earlier.

### V12 · p10 · Algebraic identity, eq. 4

**Prints:** $\sigma^2 + \beta^2 = \sqrt{(\alpha^2 - \beta^2)^2 + 4\sigma^2\beta^2}$
**Correct:** $\alpha^2 + \beta^2 = \sqrt{(\alpha^2 - \beta^2)^2 + 4\alpha^2\beta^2}$

The identity is $(\alpha^2+\beta^2)^2 = (\alpha^2-\beta^2)^2 + (2\alpha\beta)^2$. Two independent
$\sigma$-for-$\alpha$ slips in a single line.

### V13 · p10 · Eq. 5, a missing power

**Prints:** $= \omega\sqrt{\mu\varepsilon}\sqrt{1 + (\sigma/\omega\varepsilon)^2}$
**Correct:** $= \omega^2\mu\varepsilon\sqrt{1 + (\sigma/\omega\varepsilon)^2}$

$\sqrt{(\omega^2\mu\varepsilon)^2 + (\mu\omega\sigma)^2} = \omega^2\mu\varepsilon\sqrt{1+\sigma^2/\omega^2\varepsilon^2}$.
Dimensional check: the LHS ($\alpha^2+\beta^2$) is m⁻²; the printed RHS is m⁻¹.

### V14 · p10 · The "adding" step

**Prints:** $2\sigma^2 = \omega\sqrt{\mu\varepsilon\sqrt{1+(\sigma/\omega\varepsilon)^2} - 1}$ — outer radical over the whole RHS
**Correct:** $2\alpha^2 = \omega^2\mu\varepsilon\left[\sqrt{1+(\sigma/\omega\varepsilon)^2} - 1\right]$ — no outer radical

Adding eq. 2 ($\alpha^2-\beta^2 = -\omega^2\mu\varepsilon$) to the corrected eq. 5 gives $2\alpha^2$
**directly**. Taking a square root at this step is unjustified and breaks the dimensions again.

### V15 · p10 · Attenuation constant labelled $\sigma$

**Prints:** $\sigma = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+(\sigma/\omega\varepsilon)^2} - 1\right]}$
**Correct:** the left-hand side is $\alpha$

The formula is right; only the label is wrong. But because $\sigma$ also appears *inside* the same
expression, the equation as printed is **self-referential and unsolvable**.

### V16 · p11 · Magnitude of the intrinsic impedance

**Prints:** $|\eta| = \dfrac{\sqrt{\mu/\varepsilon}}{\left[\sigma + (j\omega\varepsilon)^2\right]^{1/4}}$
**Correct:** $|\eta| = \dfrac{\sqrt{\mu/\varepsilon}}{\left[1 + (\sigma/\omega\varepsilon)^2\right]^{1/4}}$, equivalently $\dfrac{\sqrt{\omega\mu}}{\left[\sigma^2 + (\omega\varepsilon)^2\right]^{1/4}}$

Three faults in one line: $\sigma$ should be $\sigma^2$; $(j\omega\varepsilon)^2 = -\omega^2\varepsilon^2$
makes the bracket $\sigma - \omega^2\varepsilon^2$, usually negative, so the fourth root would be
imaginary; and adding $\sigma$ (S/m) to $(\omega\varepsilon)^2$ (S²/m²) is dimensionally
inhomogeneous.

### V17 · p12 · $\gamma^2$ where $\gamma$ is meant

**Prints:** $\gamma^2 = j\omega\sqrt{\mu\varepsilon^*}$
**Correct:** $\gamma = j\omega\sqrt{\mu\varepsilon^*}$ (so $\gamma^2 = -\omega^2\mu\varepsilon^*$)

LHS is m⁻², printed RHS is m⁻¹. The handout uses the correct relation on pp. 13 and 15.

### V18 · p15 · Phase velocity in a lossy medium

**Prints:** $v_p = \dfrac{\omega}{\sqrt{\mu\varepsilon}\left(1 + \frac{1}{8}\frac{\sigma^2}{\omega^2\varepsilon^2}\right)}$
**Correct:** $v_p = \dfrac{1}{\sqrt{\mu\varepsilon}\left(1 + \frac{1}{8}\frac{\sigma^2}{\omega^2\varepsilon^2}\right)}$

The line at the **bottom of p14 is correct**. Carrying it to the top of p15, the $\omega$ was
cancelled from the denominator but left in the numerator. As printed, $v_p$ carries units of
(m/s)·s⁻¹.

### V19 · p16 · Good-conductor $\alpha$ and $\beta$

**Prints:** $\sigma = \omega\sqrt{\frac{\mu\varepsilon}{2}\sqrt{(\sigma/\omega\varepsilon)^2}} = \sqrt{\frac{\omega\mu\alpha}{2}}$, and the same for $\beta$
**Correct:** $\alpha = \beta = \sqrt{\dfrac{\omega\mu\sigma}{2}} = \sqrt{\pi f\mu\sigma}$

**$\sigma$ and $\alpha$ have been swapped with each other.** The next line confirms it:
$v_p = \omega/\sqrt{\omega\mu\alpha/2}$ is evaluated as $\sqrt{2\omega/\mu\sigma}$, using $\sigma$.
*(Minor: the "$-1$" is dropped without an $\cong$ sign — the step is an approximation, not an
equality.)*

### V20 · p16 · Complex permittivity of a good conductor, inverted

**Prints:** $\eta^* = \sqrt{\dfrac{\mu}{\varepsilon^*}} = \sqrt{\dfrac{\mu}{-j\omega/\sigma}} = \sqrt{\dfrac{j\omega\mu}{\sigma}}$
**Correct:** the middle term is $\sqrt{\dfrac{\mu}{-j\sigma/\omega}}$

For $\sigma/\omega\varepsilon \gg 1$, $\varepsilon^* = \varepsilon - j\sigma/\omega \approx
\mathbf{-j\sigma/\omega}$, not $-j\omega/\sigma$. As printed,
$\mu/(-j\omega/\sigma) = j\mu\sigma/\omega$, which is **not** the $j\omega\mu/\sigma$ that the third
term correctly states. First and third terms are right; the bridge between them is wrong.

---

## § B — Cosmetic (spelling, formatting, notation)

Nothing false is taught, but C21 and C23 are worth correcting in his own written work.

| ID | Page | Prints | Should be |
|---|---|---|---|
| C1 | p1, filename | ELECTROMAGN**EI**C | ELECTROMAGN**ETI**C |
| C2 | p1, p3 | homogenous (×2) | homogeneous |
| C3 | p1 | `medium where𝜀` | missing space before $\varepsilon$ |
| C4 | p2 | "for a charge less medium" | charge-free medium |
| C5 | p4 | "Plane waves is an idealized wave" | "A plane wave is an idealised wave" |
| C6 | p4 | "do not spread or **loose** energy" | lose |
| C7 | p4 | "(e.g the electric field)" | e.g. |
| C8 | p8 | WAVE PROPAGATION heading set smaller than every other red heading | formatting inconsistency |
| C9 | pp. 9–10 | equation numbers restart at 2, 3, 4, 5 although 1–12 were already used on pp. 1–5 | two different equations now share each number |
| C10 | p10 | "Adding equation 2 and **+**5" | stray `+` |
| C11 | p11, p12 | $45^0$, $90^0$ | $45°$, $90°$ — superscript zero used for the degree symbol |
| C12 | p11 | $\theta_n$ | $\theta_\eta$ — the subscript is eta (the impedance angle), not n |
| C13 | p12 | Figure 2 arrow labelled $J_{disp} = \omega\varepsilon E$ | drops the $j$, while the resultant on the same drawing keeps it |
| C14 | p13 | "the second **tem** in bracket" | term |
| C15 | p14 | "higher **term s**" | terms |
| C16 | p15 | final line $\eta\left(1+\frac{j\sigma}{2\omega\varepsilon}\right)$ | missing its leading `=` |
| C17 | p15 | "**far much** less than 1" | "much less than 1" |
| C18 | p17 | "quantatively" | quantitatively |
| C19 | p17 | "associated with a large **phase** per unit distance" | large phase **shift** per unit distance |
| C20 | p17 | "as the wave **transverses** from free-space" | traverses |
| **C21** | **p18** | **Q1: "peak electric field intensity of 6V"** | **6 V/m** — the volt is not a unit of field intensity, and part (c) divides by $\eta$ (Ω) to get A/m |
| C22 | p13 | table row 3: $\omega = \sigma/\varepsilon$, middle cell blank, "Property of conductor and dielectric" | not wrong — it is the crossover where $\sigma/\omega\varepsilon = 1$ — but the wording is opaque |
| **C23** | **p18** | **Q2(d): "Intrinsic impedance of the wave"** | **of the medium** — intrinsic impedance is a property of the medium. Q1(b) words it correctly |

---

## § C — Scope note (not an error)

**p1 · Objective (iv) is never delivered.** The handout lists four learning objectives; *"Types of
polarization"* does not appear anywhere in the 18 pages. Presumably deferred to Part II. The
objective list as printed overstates the handout's contents. Routing for this gap is in
`00-index.md` § Gap map.

---

## § D — Pattern across cohorts

The old-cohort handouts in `_reference-old-cohort/` carry **the same class of defect**: their
verification log records that on EMW p6 and EMW p14 / UPW p13–14, results that are actually $\beta$
are labelled $\alpha$.

WC1 repeats and worsens it — here it is $\alpha$ mislabelled as $\sigma$, in six places.

**Practical consequence:** in any future handout from this course, treat every $\alpha$/$\beta$/$\sigma$
label in the propagation-constant material as suspect until checked against a dimensional or
limiting-case test. Two checks catch nearly all of it:

1. **Dimensions** — $\alpha$ and $\beta$ are m⁻¹; $\sigma$ is S/m. They cannot be interchanged.
2. **Self-reference** — if the symbol on the left of the equals sign also appears on the right, the
   label is wrong.

---

## § T — TL and TLT (transmission-line documents)

**24 flags: 12 substantive (T1–T12), 12 cosmetic (C24–C35).**

TL is the most error-dense document in this knowledge base — roughly one substantive defect per 1.3
pages, against WC1's one per 0.9. TLT is markedly cleaner and is used below to settle several of
TL's forms.

### Substantive — T1–T12

### T1 · ·TL p1, equation 1 · Telegrapher's equation, wrong differential variable ★
- **Printed:** $-\dfrac{dv(z,t)}{dt} = i(z,t)R + L\dfrac{di(z,t)}{dt}$
- **Correct:** $-\dfrac{\partial v(z,t)}{\partial z} = R\,i(z,t) + L\dfrac{\partial i(z,t)}{\partial t}$
- **Why:** the line directly above it takes $\lim_{\Delta z\to 0}$ of a difference in $z$ divided by
  $\Delta z$ — that limit **is** $\partial v/\partial z$. As printed, the equation says a
  time-derivative equals a quantity built from the same time-derivative: self-referential and
  unsolvable.
- **Cross-check:** ·TLT p7 prints the correct $z$-form.
- **Severity:** substantive — this is the founding equation of the whole topic.

### T2 · ·TL p2, equation 2 · The same defect in the KCL equation
- **Printed:** $-\dfrac{di(z,t)}{dt} = v(z,t)G + C\dfrac{dv(z,t)}{dt}$
- **Correct:** $-\dfrac{\partial i(z,t)}{\partial z} = G\,v(z,t) + C\dfrac{\partial v(z,t)}{\partial t}$
- **Note:** the handout **silently corrects both T1 and T2** further down ·TL p2, under "for
  simplicity of notation we may write", where it prints $-\frac{dv}{dz} = L\frac{di}{dt}$ and
  $-\frac{di}{dz} = C\frac{dv}{dt}$ with the $z$ restored. No erratum, no comment. A reader who
  stops at the boxed equations 1 and 2 learns the wrong pair.
- **Severity:** substantive.

### T3 · ·TL p4, equations 8 and 9 · Sign of the reactive term
- **Printed:** $-\dfrac{dV}{dz} = RI - j\omega LI$ and $-\dfrac{dI}{dz} = GV - j\omega CV$
- **Correct:** $-\dfrac{dV}{dz} = (R + j\omega L)I$ and $-\dfrac{dI}{dz} = (G + j\omega C)V$
- **Why:** the phasor rule stated on the previous page is $\partial/\partial t \to +j\omega$.
- **Does it propagate?** No — the next line correctly forms $(R+j\omega L)(G+j\omega C)$.
- **Severity:** substantive but self-limiting.

### T4 · ·TLT p13 · Backward-wave exponent
- **Printed:** $V(z) = V_0^{+}e^{-\gamma z} + V_0^{-}e^{j\gamma}$ (and the same for $I$)
- **Correct:** $V(z) = V_0^{+}e^{-\gamma z} + V_0^{-}e^{+\gamma z}$
- **Why:** wrong symbol ($j$ for $+$) **and** the $z$ is missing, so the term is a constant, not a
  wave. ·TLT p14's own text says "the terms including $e^{+\gamma z}$", confirming it.
- **Severity:** substantive. *The only substantive flag against TLT.*

### T5 · ·TL p4 · Reflected current term carries the wrong superscript
- **Printed:** $I(z) = \dfrac{V_0^{+}}{Z_0}e^{-j\beta z} - \dfrac{V_0^{+}}{Z_0}e^{+j\beta z}$
- **Correct:** $I(z) = \dfrac{V_0^{+}}{Z_0}e^{-j\beta z} - \dfrac{V_0^{-}}{Z_0}e^{+j\beta z}$
- **Why:** the second term is the **reflected** wave and must carry $V_0^{-}$. The minus sign is
  correct and follows from $Z_0 = -(\text{backward voltage})/(\text{backward current})$, ·TLT p15.
- **Severity:** substantive.

### T6 · ·TL p5 · The load-current line is both mislabelled and identically zero
- **Printed:** $V(l) = \dfrac{V_0^{+}}{Z_0} - \dfrac{V_0^{+}}{Z_0}$
- **Correct:** $I_L = \dfrac{V_0^{+}}{Z_0} - \dfrac{V_0^{-}}{Z_0}$
- **Why:** two errors at once — it is the load **current**, not a voltage $V(l)$; and as printed it
  evaluates to exactly 0 for every load.
- **Severity:** substantive.

### T7 · ·TL p5 · The $Z_L$ expression makes every load matched ★ most serious in this document
- **Printed:** $Z_L = \dfrac{V_L}{I_L} = \left(\dfrac{V_0^{+}+V_0^{-}}{V_0^{+}+V_0^{-}}\right)Z_0$
- **Correct:** $Z_L = \left(\dfrac{V_0^{+}+V_0^{-}}{V_0^{+}-V_0^{-}}\right)Z_0$
- **Why:** the denominator must be the **difference**, since $I_L = (V_0^{+}-V_0^{-})/Z_0$. As
  printed the bracket is identically 1, so $Z_L = Z_0$ for every load — which would make
  $\Gamma = 0$ always and destroy the result derived on the very next line.
- **Why it matters more than the others:** the conclusion that follows it *is* correct, so the page
  shows a right answer drawn from an absurd premise. A student checking their working against this
  page will not find the join.
- **Severity:** substantive.

### T8 · ·TL p7 · Standing-wave magnitude, missing brackets
- **Printed:** $|V(z)| = |V_0^{+}|1 + |\Gamma|^2 + 2|\Gamma|\cos(2\beta z+\theta)^{\frac{1}{2}}$
- **Correct:** $|V(z)| = |V_0^{+}|\left[1 + |\Gamma|^2 + 2|\Gamma|\cos(2\beta z+\theta_r)\right]^{1/2}$
- **Why:** the exponent $\tfrac12$ must apply to the whole bracket, not to the cosine alone.
- **⚠ Invisible in the PDF text layer — only the rendered page shows it.** Same defect class as V10.
- **Settled by:** ·TL p11's photographed slide, which prints the correctly bracketed form.
- **Severity:** substantive.

### T9 · ·TL p7 · The square root is missing from the line above
- **Printed:** $|V(z)| = \left[V_0^{+}(\ldots)\right]\left[(V_0^{+})^{*}(\ldots)\right]$
- **Correct:** $|V(z)| = \sqrt{\left[V(z)\right]\left[V(z)\right]^{*}}$
- **Why:** the prose one line earlier says "must take square root of product with complex
  conjugate", and the equation then omits it.
- **Same line, minor:** $\Gamma$ is written twice in $|\Gamma|e^{j\theta}\Gamma e^{+i\beta z}$ — but
  $|\Gamma|e^{j\theta}$ **is** $\Gamma$.
- **Severity:** substantive.

### T10 · ·TL p9 · The voltage minimum is labelled $-z_{max}$ ★
- **Printed:** $-z_{max} = \dfrac{\theta+(2n+1)\pi}{2\beta} = \dfrac{\theta\lambda}{4\pi} + \dfrac{(2n+1)\lambda}{4}$
- **Correct:** $-z_{min} = \ldots$
- **Why:** this result follows from $\cos(2\beta z+\theta) = -1$ — the **minimum** condition, stated
  three lines above it. The page therefore uses one symbol for two positions a quarter-wavelength
  apart.
- **Pattern:** this is § D's cross-cohort label failure appearing in a new document and outside
  propagation-constant material. See the pattern note at the end of this section.
- **Severity:** substantive.

### T11 · ·TL p14 · An angle set equal to a length
- **Printed:** "Substituting $z = \lambda/4$, or $\beta z = \lambda/2$ in equation 1"
- **Correct:** $\beta z = \dfrac{2\pi}{\lambda}\cdot\dfrac{\lambda}{4} = \dfrac{\pi}{2}$
- **Why:** $\beta z$ is an angle in radians; $\lambda/2$ is a length in metres. Fails a dimensional
  check on sight — the first of the two habits in § D catches it.
- **Does it propagate?** No — $Z_{in} = Z_0^2/Z_L$ that follows is correct.
- **Severity:** substantive.

### T12 · ·TL p6 · Stated frequency contradicts the substituted frequency
- **Printed:** "$f = 100\ Hz$", then $Z_L = 50 - \dfrac{j}{(2\pi)(10^{8})(10^{-11})}$
- **Correct:** $f = 100\ \mathrm{MHz}$
- **Why:** $10^{8}$ Hz is 100 MHz, not 100 Hz.
- **Re-computed:** at 100 MHz, $Z_L = 50 - j159.15\,\Omega$ and
  $\Gamma = 0.3728 - j0.6655 = 0.7628\angle-60.74^{\circ}$ — matching the handout's own printed
  $0.3721 - j0.6655 = 0.76\angle-60.8^{\circ}$. At a literal 100 Hz,
  $Z_L = 50 - j1.59\times10^{8}\,\Omega$ and $|\Gamma| = 1.0000$: the load reads as an open circuit
  and the example collapses. **The substitution is right; the label is wrong.**
- **Severity:** substantive — same class as V1, a stated constant contradicted by the working.

### Cosmetic — C24–C35

Nothing false is taught, but C28 changes how you cite this handout and C32 changes how you read it.

| ID | Page | Prints | Should be |
|---|---|---|---|
| C24 | ·TLT p14 | body text clipped off the left edge ("ach f", "hese solutions", "n the +z direction") | recoverable from context, but not readable as printed |
| C25 | ·TL p8 | "Maximum and minima separated by half a wavelength" | true of max-to-max and min-to-min only; a maximum and its **adjacent** minimum are $\lambda/4$ apart — as the figure directly above it shows |
| **C26** | **·TL p12** | $\dfrac{jZ_0\sin\beta z}{\cos\beta}$ | $\dfrac{jZ_0\sin\beta z}{\cos\beta z}$ — the $z$ is dropped from the denominator, though the result $jZ_0\tan\beta z$ is right |
| C27 | ·TL p12 | "capacitive reactance (negative X) from 0 to ∞", closing "X = 0 to X = −∞" | $0 \to +\infty$ inductive, $-\infty \to 0$ capacitive; the closing summary drops the inductive half it had just established |
| **C28** | **·TL pp. 1–3** | **"2" labels both the KCL equation and the first lossless voltage equation; "3" is likewise reused** | **five equations carry four distinct numbers — cite by page and content, never by the handout's own equation number** |
| C29 | ·TL p2 | "equation 3 with respect to **3**" | with respect to $t$ |
| C30 | ·TL p4 | "Let $z=0$ at the load and $z=-l$ at the generator then $V(z=0) = V_L = -l$ at the generator then" | a duplicated clause spliced into the middle of the equation it introduces |
| C31 | ·TL p1 | "the transmission **lie**" | line |
| **C32** | **·TL pp. 3–4** | $(G + j\omega c)$, four times | $(G+j\omega C)$ — lowercase $c$ for the capacitance per unit length collides with $c$ for the speed of light used throughout WC1. See `_nomenclature.md` § clashes |
| C33 | ·TL p5 | "$Z_L \to Z_L = infinity$" | $Z_L \to \infty$ — $Z_L$ sits on both sides, and "infinity" is spelled out |
| C34 | ·TL p7 | $e^{-i\beta z}$ alongside $e^{j\theta}$ **within one equation** | $j$ throughout — the imaginary unit switches mid-equation |
| C35 | ·TL p12 | "Short-Circuit Termination of Lossless Section of Transmission Line" twice on one page | once in red as the section head, again in blue as item (a) |

### Pattern note — widening § D

§ D records the cross-cohort warning: distrust every $\alpha$/$\beta$/$\sigma$ label in
propagation-constant material until dimensionally checked. **T10 is that same failure outside
propagation-constant material** — a standing-wave *position* labelled $max$ that is a $min$. And
**T5–T7 are the same failure in superscripts** — $V_0^{+}$ where $V_0^{-}$ belongs, three times.

> **Widen the rule: treat every label in this course's material — Greek symbol, subscript, or
> superscript sign — as suspect until checked against the condition that produced it.**

A third habit joins § D's two, and it catches T5, T6 and T7 with no algebra at all:

3. **Distrust any expression that collapses to something trivial.** T6 gives $I_L = 0$ for every
   load; T7 gives $Z_L = Z_0$ for every load. Both are visible on sight.

---

## § E — Exam papers

Defects in the actual assessment papers (not the handouts). Entry IDs are `P1`, `P2`, … allocated
continuously across the whole `past-papers/` folder, and referenced by a `⚠ VERIFY` marker at the matching
question in `past-papers/<paper>.md`. Per standing instruction the full entry lives **here only** — the paper
file just points to it.

**Allocation:** `P1`–`P13` = BEE 3101 End of Semester, 25 Oct 2024 · `P14`–`P16` = BEE 3102 CAT 1,
29 Aug 2024 · `P17`–`P20` = BEE 3102 CAT ("CAT 1"), 3 Oct 2024 · `P21`–`P26` = BEE 3101 CAT (no CAT number
printed), 1 Oct 2025 · `P27`–`P37` = BEE 3102 End of Semester, 23 Oct 2025. Next paper starts at **P38**.

> ⚠ The **13 Aug 2025 CAT** predates this section. Its two misprints are documented inside
> `past-papers/EEE3202-CAT1-2025-08-13.md` itself and carry no P-numbers. This series is therefore not a
> complete list of every exam defect in the subject.

### P1 · BEE 3101 End of Semester (25 Oct 2024), Question One — printed parts sum to 21, header says 30 ★
- **Paper:** "QUESTION ONE (30 MARKS-COMPULSARY)", then parts marked (4), (6), (2), (3), (4), (2).
- **Issue:** those sum to **21**. Nine marks are unaccounted for on a compulsory question — the largest
  single arithmetic defect on any paper in this repository.
- **Two readings, and no way to choose between them from the page:** either a part has been dropped in
  typesetting, or the printed part-marks are simply wrong and the question really is out of 30. Pages 1–4 are
  all present and consecutive ("Page 1 of 4" … "Page 4 of 4"), and nothing is cropped, so **this is a defect
  in the paper rather than a gap in the photographs**.
- **How to handle:** if setting this as a timed mock, mark Question One out of 21 and say so, or scale to 30
  and say so. Do not invent a missing part. Worth raising with the lecturer.
- **Severity:** structural (marks). Affects how the paper is graded, not what it teaches.

### P2 · BEE 3101 End of Semester (25 Oct 2024), Q1(b) — a field intensity given in volts
- **Paper:** "peak electric field intensity of $6V$".
- **Issue:** the volt is a unit of potential; electric field intensity is **V/m**.
- **Correct form:** $E_0 = 6\ \text{V/m}$.
- **How to handle:** the value is unambiguous, so this costs nothing numerically — but it is worth pointing
  out, because Q1(b)(iii) asks for $H$ and the whole check on that answer is that $E/H$ comes out in ohms.
  A field in volts makes that dimensional check impossible.
- **Severity:** notation (unit). The same slip appears on the 29 Aug CAT — see **P15**.

### P3 · BEE 3101 End of Semester (25 Oct 2024), Q1(d) — conductivity of aluminium, exponent sign inverted ★ most serious
- **Paper:** "Determine the frequency for which the **ski depth** in aluminium is 0.01mm, given that
  $\sigma = 3.54 \times 10^{-7}\ mho/m$".
- **Issue (two defects in one line):**
  1. "**ski depth**" for **skin depth**.
  2. The conductivity of aluminium is $3.54 \times 10^{7}$ S/m. The printed value has a **negative**
     exponent — it is wrong by a factor of $10^{14}$, and it describes an insulator, not a metal.
- **Correct form:** $\sigma_{Al} = 3.54 \times 10^{7}\ \text{S/m}$ (mho/m and S/m are the same unit; "mho" is
  the older name for the siemens and is not itself an error).
- **How to handle:** rearranging $\delta = 1/\sqrt{\pi f \mu \sigma}$ for $f$ is the whole question, and the
  method is unaffected. Work it with $3.54 \times 10^{7}$ S/m — with the printed value the answer is
  physically absurd. Note also that $\mu_r = 1$ for aluminium is **needed and not supplied**; state that
  assumption in the answer.
- **Severity:** value (wrong by $10^{14}$). This is the defect on this paper most likely to teach something
  false, and the pattern matches the 2025 CAT, whose own σ misprint is logged inside its solutions file.

### P4 · BEE 3101 End of Semester (25 Oct 2024), Question One header — spelling
- **Paper:** "(30 MARKS-**COMPULSARY**)".
- **Correct form:** COMPULSORY.
- **Severity:** cosmetic.

### P5 · BEE 3101 End of Semester (25 Oct 2024), Q1(a) — "ad" for "and", and **B** silently becomes **H**
- **Paper:** bullets 2 and 3 ask about "**E**- and **B**-field components" and the "orientation of **E** and
  **B** fields"; bullet 4 then asks for "The ratio between $E_x$ **ad** $H_y$".
- **Issue:** "ad" is a typo for "and". More substantively, the question switches from $\mathbf{B}$ to
  $\mathbf{H}$ between bullets without saying that $\mathbf{B} = \mu\mathbf{H}$ — and the *ratio* asked for
  in bullet 4 is the intrinsic impedance $\eta = E_x/H_y$, which is only a clean 377 Ω-family quantity in the
  $\mathbf{H}$ form. A student who answers bullet 4 with $E_x/B_y$ gets a velocity, not an impedance.
- **How to handle:** make him write $\mathbf{B} = \mu\mathbf{H}$ explicitly, then answer in $\mathbf{H}$.
- **Severity:** notation, with a real trap behind it.

### P6 · BEE 3101 End of Semester (25 Oct 2024), Q2(b) — the figure is called by two different names
- **Paper:** the question says "Two perfect dielectrics are shown in **Figure Q1**"; the figure directly below
  it is captioned "**Figure Q2**". There is no Figure Q1 anywhere on the paper.
- **Correct reading:** Figure Q2 — it is the only two-dielectric figure on the paper, immediately below the
  question that refers to it.
- **Severity:** cosmetic (cross-reference). Intent unambiguous.

### P7 · BEE 3101 End of Semester (25 Oct 2024), Figure Q2 — both regions labelled σ₁ = 0
- **Paper:** the figure prints "$\sigma_1 = 0$" in Region 1 **and** "$\sigma_1 = 0$" in Region 2.
- **Correct form:** $\sigma_2 = 0$ in Region 2.
- **How to handle:** read it as $\sigma_2 = 0$. The stem states both media are perfect dielectrics, so the
  intent is not in doubt — but the subscript is what tells a student the second region is lossless, and it is
  the reason $\eta_2$ may be treated as purely real.
- **Severity:** notation (subscript). Intent recoverable from the stem.

### P8 · BEE 3101 End of Semester (25 Oct 2024), Q2(b)(iii) — no mark allocation
- **Paper:** Q2 is headed "(15 MARKS)". Its parts are marked (2), (3), (1), (3), (3), then **nothing** for
  "iii. Transmitted power", then (1). The printed parts sum to **13**.
- **Issue:** two marks are unallocated, and (b)(iii) is the part left without a figure.
- **How to handle:** the arithmetic points to 2 marks for (b)(iii), and that is a reasonable working
  assumption for a mock — but it is an assumption, not something the paper states. Say which you are using.
- **Severity:** omission (marks).

### P9 · 25 Oct 2024 exam Q2(a) **and** 29 Aug 2024 CAT Q2(a) — "Poyting"
- **Paper:** "The **Poyting** theorem can be expressed as…" (exam Q2a) and "Distinguish between the
  **Poyting** theorem and Poynting vector" (CAT Q2a). In the CAT the same sentence spells it *both* ways.
- **Correct form:** **Poynting**, after John Henry Poynting.
- **Severity:** cosmetic (name). Logged once and referenced from both papers because it is the same slip.

### P10 · BEE 3101 End of Semester (25 Oct 2024), Q3(b) — the same equation printed with two different left-hand sides
- **Paper:** the transmission-line input-impedance equation appears **twice**. At the foot of page 2 it is
  printed "$Z_L = Z_0\frac{Z_L\cos\beta z + jZ_0\sin\beta z}{Z_0\cos\beta z + jZ_L\sin\beta z}$"; at the top
  of page 3, immediately below, it is printed with "$Z_{in} =$". Also "at any point **a long** a transmission
  line" for "along".
- **Issue:** with $Z_L$ on the left the equation is **circular** — $Z_L$ appears on both sides, and it defines
  nothing. The page-3 version is the correct one.
- **Correct form:** $Z_{in} = Z_0\dfrac{Z_L\cos\beta z + jZ_0\sin\beta z}{Z_0\cos\beta z + jZ_L\sin\beta z}$.
- **How to handle:** this is exactly the "self-reference" test in § D above — if the symbol on the left also
  appears on the right, the label is wrong. Use it as a teaching moment rather than just a correction.
- **Severity:** error as printed; intent recoverable from the duplicate on the next page.
- **Related:** the 3 Oct 2024 CAT prints only the broken version — see **P18**.

### P11 · BEE 3101 End of Semester (25 Oct 2024), Q4(c)(iv) — "Phase $v_p$"
- **Paper:** the five sub-parts read "Cut-off wavelength", "Guide wavelength", "Group velocity", "**Phase**
  $v_p$", "Characteristic impedance".
- **Correct form:** "Phase **velocity** $v_p$" — the subscript makes the intent plain.
- **Severity:** cosmetic (dropped word).

### P12 · BEE 3101 End of Semester (25 Oct 2024), Q4(d) — no mark allocation
- **Paper:** Q4 is headed "(15 marks)". Its parts are marked (2), (2), (8) and then **nothing** for (d),
  the TE₁₀ field-pattern sketch. The printed parts sum to **12**.
- **How to handle:** three marks are implied. Same caution as P8 — it is an inference, so state it.
- **Severity:** omission (marks). Together with P1 and P8, **three of this paper's five questions do not add
  up as printed**.

### P13 · BEE 3101 End of Semester (25 Oct 2024), Fig.1Q5 — the boundary-value problem is not closed
- **Paper:** the L-shaped finite-difference region carries three arrows — 20 V onto the top edge, 30 V onto
  the right edge, 0 V onto the bottom edge of the left portion.
- **Issue:** the region has **six** boundary segments (top, right, the bottom of the lower limb, the vertical
  left edge, the horizontal step edge, and the bottom edge of the left portion). Only three carry a
  potential. **A finite-difference solution needs a value on every boundary node**, so as printed the problem
  cannot be solved — nodes 1, 2 and 8 all have at least one unlabelled neighbour.
- **The reading that closes it:** each arrow labels the **whole side** it touches — 20 V the entire top, 30 V
  the entire right-hand boundary including the lower limb, 0 V everything else. That is the conventional way
  such a figure is drawn and it makes the problem well-posed.
- **How to handle:** use that reading, **state it out loud as an assumption before starting the iteration**,
  and flag it to the lecturer. Do not present the assumption as something the figure says.
- **Severity:** omission (paper defect). The question is unanswerable as printed without it.

### P14 · BEE 3102 CAT 1 (29 Aug 2024) — no total printed, and the parts sum to 37
- **Paper:** Q1 is marked (2) and (13); Q2 is marked (2) and (20). **No total appears anywhere** on the sheet.
- **Issue:** the parts sum to **37** — not 30, 40 or 50, and an unusual figure for a one-hour CAT.
- **How to handle:** mark it out of 37 and say so, or scale it. Either is defensible; guessing that a part is
  missing is not, since the page is complete ("Page 1 of 1") and nothing is cropped.
- **Severity:** omission (marks).

### P15 · BEE 3102 CAT 1 (29 Aug 2024), Q2(b) — a field intensity given in volts
- **Paper:** "$\eta_1 = 300\Omega, \eta_2 = 100\Omega$ and $E_{xi1} = 100V$".
- **Correct form:** $E_{xi1} = 100\ \text{V/m}$.
- **How to handle:** as with P2, the value is unambiguous — but the whole of Q2(b) is a chain of field and
  power calculations in which the units are the only running check available. Insist on V/m.
- **Severity:** notation (unit). Same slip as **P2** on the exam paper.

### P16 · BEE 3102 CAT 1 (29 Aug 2024), Q2(b)(x) — "I" for "in"
- **Paper:** "x. The transmitted power **I** region 2".
- **Correct form:** "The transmitted power **in** region 2".
- **Severity:** cosmetic (typo). Intent unambiguous.

### P17 · BEE 3102 CAT (3 Oct 2024) — labelled "CAT 1", but it is the second CAT ★
- **Paper:** the header reads "CAT 1 · BEE 3102: ELECTROMAGNETIC FIELDS AND WAVES · DATE: 3 October, 2024".
- **Issue:** a paper for the **same unit**, also headed "CAT 1", was sat on **29 August 2024** — five weeks
  earlier. Two CAT 1s in one semester is not possible; the October paper is on its face the **CAT 2**. It
  also sits three weeks before the 25 October end-of-semester exam, exactly where a CAT 2 belongs.
- **How to handle:** the file keeps the printed label (`BEE3102-CAT1-2024-10-03.md`) so the name matches the
  paper, and the **date** is what distinguishes the two. When talking to him, call it "the October CAT" and
  explain why. Do not silently re-label it CAT 2.
- **Severity:** structural (paper identity). Matters for filing, not for the physics.

### P18 · BEE 3102 CAT (3 Oct 2024), Q1(b) — the input-impedance equation is circular
- **Paper:** "$Z_L = Z_0\frac{Z_L\cos(\beta z) + jZ_0\sin\beta z}{Z_0\cos(\beta z) + jZ_L\sin\beta z}$", and
  "at any point **a long** a transmission line" for "along".
- **Issue:** $Z_L$ on the left and $Z_L$ twice on the right. **This paper prints only the broken version** —
  unlike the 25 Oct exam, which prints it wrongly once and correctly once (P10). A student working from this
  CAT alone has no way to spot it except by noticing the self-reference.
- **Correct form:** $Z_{in} = Z_0\dfrac{Z_L\cos\beta z + jZ_0\sin\beta z}{Z_0\cos\beta z + jZ_L\sin\beta z}$.
- **Severity:** error as printed. Recoverable only from the physics, or from the exam paper.

### P19 · BEE 3102 CAT (3 Oct 2024), Q2(b) — one word in the stem is illegible
- **Paper:** "Consider a short-circuited **son** lossless transmission line as shown in Fig. 1."
- **Issue:** "son" is not a word that fits this sentence, and the intended text **cannot be recovered with
  certainty** from the photograph. The obvious candidate is "50 Ω", which is what Fig. 1 labels the line, but
  that is a guess about the glyphs, not a reading of them.
- **How to handle:** nothing in the calculation depends on it — $Z_0 = 50\ \Omega$ comes from the figure.
  Record it as illegible and move on. **If he wants it settled, ask him to re-shoot that line.**
- **Severity:** legibility (unresolved). Deliberately not reconstructed.

### P20 · BEE 3102 CAT (3 Oct 2024) — no marks printed anywhere
- **Paper:** neither part-marks nor a total appear on the sheet, which is complete ("Page 1 of 1").
- **Issue:** with no allocation at all, the paper cannot be marked as printed, and it cannot be timed
  realistically either.
- **How to handle:** for a mock, borrow the allocation from the questions' twins on the 25 Oct exam — Q1(a)
  → 2, Q1(b)(i–iii) → 3 each, Q2(a) → 2 — and say that is where the numbers came from. Q2(b) has no twin and
  no allocation; judge it on its own.
- **Severity:** omission (marks).

### P21 · BEE 3101 CAT (1 Oct 2025), Question One — the question heading is missing
- **Paper:** a horizontal rule is printed where "QUESTION ONE" belongs — the same rule style used under
  "QUESTION TWO" further down the same page — but **no heading text sits above it**.
- **Issue:** parts (a) and (b) are Question One only by position on the page. Nothing on the paper labels
  them. Question Two, by contrast, is properly headed.
- **Correct form:** "QUESTION ONE", above that rule.
- **How to handle:** transcribe by position and say that is what you are doing. Nothing mathematical is
  lost. This is **not** a photograph problem: the rule, the instructions above it and the part (a) text
  below it are all fully inside the frame and sharp.
- **Severity:** structural.

### P22 · BEE 3101 CAT (1 Oct 2025), Q1(b) — a Smith chart is required, but none is supplied or promised ★
- **Paper:** "Determine using Smith Chart, a) The VSWR; b) Reflection coefficient; c) The input impedance;
  d) The impedance at a voltage maximum ; e) The impedance at voltage minimum; **(11 marks)**".
- **Issue:** **11 of this paper's 30 marks are explicitly reserved for a graphical method**, yet no chart is
  printed on the sheet and the instructions never say one is provided. The end-of-semester paper three weeks
  later does say so (its instruction 3) — this one does not.
- **How to handle:** get him a blank Smith chart before this is ever set as a timed mock. Working Q1(b)
  algebraically answers a *different* question from the one asked; if that is done anyway, say so out loud
  and mark it as a substitute method.
- **✅ RESOLVED 10 Sep 2026.** A full blank Smith chart — with resistance/reactance grid, both perimeter
  wavelength scales, angle of reflection coefficient, and the radially scaled SWR / return-loss / reflection
  rule — is **·TLT p20**, in `../sources/current/TransmissionLineTheory.pdf`. Print that page. The method is
  written up in `02-transmission-lines.md` § 14 and worked end to end in its § 15 Example 5.
- **Severity:** omission. **The worst defect on this paper** — it makes more than a third of it
  unattemptable as printed.

### P23 · BEE 3101 CAT (1 Oct 2025), Q1(b) — sub-items lettered a)–e), colliding with the part letters
- **Paper:** Question One's two parts are lettered a) and b); Q1(b)'s five sub-items are then lettered
  a), b), c), d), e) as well.
- **Issue:** "part (b)" is ambiguous on this paper — it is both the 11-mark Smith-chart question and its own
  second sub-item. Referencing needs the ugly "Q1(b)(b)".
- **Correct form:** roman numerals for sub-items, i.–v., which is what every other paper in this folder uses.
- **How to handle:** this file cites them as Q1b(a)–(e). When talking to him, name the item rather than the
  letter ("the input-impedance part").
- **Severity:** structural (cataloguing).

### P24 · BEE 3101 CAT (1 Oct 2025) — no total mark is printed anywhere
- **Paper:** part-marks (4 marks), (11 marks), (3 marks), (12 marks). No total in any heading, no total at
  the foot of the page.
- **Issue:** with no stated total there is nothing to reconcile the parts against, so `marks_reconcile`
  cannot honestly be `true` even though the parts are internally consistent.
- **Verified here 2026-09-03:** the four parts sum to **30** (15 + 15), and 30 marks in 60 minutes is exactly
  the format of this cohort's CAT 1 of 13 Aug 2025. So 30 is almost certainly right — but it is a deduction,
  not a printed fact.
- **How to handle:** mark out of 30 and say the 30 came from adding the parts.
- **Severity:** omission (marks).

### P25 · BEE 3101 CAT (1 Oct 2025) — the unit code is the 2024 exam's code
- **Paper:** "BEE3101: ELECTROMAGNETIC FIELDS AND WAVES".
- **Issue:** BEE 3101 is the code the **2024 end-of-semester paper** carried. The same 2025 cohort sat CAT 1
  as **EEE 3202** (13 Aug 2025) and the end-of-semester exam as **BEE 3102** (23 Oct 2025). That is three
  codes for one unit inside one semester, and the two 2024 codes have effectively **swapped roles** for
  2025: BEE 3101 has moved from the exam to a CAT, BEE 3102 from the CATs to the exam.
- **How to handle:** match every paper in this subject by unit **name** and **date**. The code carries no
  information at all. See also P37 and the `unit_code_note` in each paper file.
- **Severity:** cataloguing.

### P26 · BEE 3101 CAT (1 Oct 2025) — no CAT number is printed
- **Paper:** the sheet says only "This examination consists of TWO questions." Nowhere does it say CAT 1,
  CAT 2 or anything else.
- **Issue:** the paper cannot be placed in the semester's assessment sequence from its own face.
- **Inference, offered as an inference:** it sits between CAT 1 (13 Aug 2025) and the end-of-semester exam
  (23 Oct 2025), which puts it in the **CAT 2 slot**. That is a deduction from the calendar.
- **How to handle:** file it by date, call it "the 1 October CAT", and say "probably CAT 2" rather than
  "CAT 2". Note the precedent for caution: the 2024 cohort's equivalent paper (3 Oct 2024) was printed
  "CAT 1" five weeks *after* that year's actual CAT 1 (P17). The labelling on these papers is unreliable in
  both directions — present and absent.
- **Severity:** cataloguing.

### P27 · BEE 3102 End of Semester (23 Oct 2025) — the promised Smith chart is not in the photographed set
- **Paper:** instruction 3, "**Smith chart** is provided."
- **Issue:** the four photographs are "Page 1 of 4" … "Page 4 of 4" and are all question paper. **No Smith
  chart is among them.** Q2(b) is 11 of Question Two's 15 marks and is explicitly "Using a Smith chart".
- **Two readings, and the photographs cannot settle it:** either the chart was a separate loose sheet (which
  is what "is provided" suggests) and simply was not photographed, or it was never handed out. The page
  numbering supports the first reading — the question paper itself is complete.
- **How to handle:** ask him whether a chart came with the paper, and get a blank chart either way. Do not
  record the paper as incomplete without asking.
- **✅ Chart obtained 10 Sep 2026** — see P22. **·TLT p20** supplies a usable blank Smith chart, so the
  practical consequence is gone. The provenance question (was a chart handed out with this paper?) is still
  open and still worth asking him, but it no longer blocks setting this paper as a mock.
- **Severity:** cataloguing (provenance), with an 11-mark practical consequence.

### P28 · BEE 3102 End of Semester (23 Oct 2025), instruction 4 — μ₀ given in A/m
- **Paper:** "You may use the following constants: $\varepsilon_0 = 8.85\times10^{-12}\ F/m$,
  $\mu_0 = 4\pi\times10^{-7}\ A/m$".
- **Issue:** the permeability of free space is in **H/m**. A/m is the unit of magnetic field strength $H$ —
  the very quantity three of this paper's parts ask for, so the clash is not harmless.
- **Correct form:** $\mu_0 = 4\pi\times10^{-7}\ \text{H/m}$.
- **Checked here 2026-09-03:** the *values* are right — with the printed $\varepsilon_0$ and
  $4\pi\times10^{-7}$ H/m, $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = 376.82\ \Omega$ (textbook $120\pi =
  376.99$) and $c = 1/\sqrt{\mu_0\varepsilon_0} = 2.999\times10^8$ m/s. Only the unit is wrong. Contrast
  WC1 p8, where the *value* is wrong by five orders of magnitude (**V1**).
- **Severity:** notation (unit).

### P29 · BEE 3102 End of Semester (23 Oct 2025), Q5(b) — the Taylor series is printed with a $(-1)^k$ ★ most serious
- **Paper:** "From the Taylors series
  $f(x + \Delta x) = \sum_{k=0}^{\infty} \dfrac{(-1)^k f^{(k)}(x)(\Delta x)^k}{k!}$ show that the second
  difference equation is approximated by
  $f''(x) \approx \dfrac{f(x + \Delta x) - 2f(x) + f(x - \Delta x)}{(\Delta x)^2}$".
- **Issue:** with the $(-1)^k$ factor the series on the right is the expansion of $f(x - \Delta x)$, **not**
  $f(x + \Delta x)$. The requested result therefore does not follow from what is printed: adding the printed
  series to itself gives $2f(x-\Delta x)$, and the $f(x+\Delta x)$ term in the answer never appears. **A
  three-mark "show that" that cannot be shown.**
- **Correct form:** the derivation needs the **pair**,
  $f(x+\Delta x) = \sum_k \frac{f^{(k)}(x)(\Delta x)^k}{k!}$ and
  $f(x-\Delta x) = \sum_k \frac{(-1)^k f^{(k)}(x)(\Delta x)^k}{k!}$; add them and truncate at $k = 2$, and
  the odd-order terms cancel to leave the stated second difference.
- **How to handle:** teach both expansions and say plainly that the paper prints one of the pair with the
  wrong left-hand side. **Do not** write the full derivation into this knowledge base — finite-difference
  material has no handout behind it and would read as his lecturer's notes. Flag it and ask for the handout.
- **Severity:** error as printed (substantive). The worst defect on this paper.

### P30 · BEE 3102 End of Semester (23 Oct 2025), Q4(b) — region 1 is never specified
- **Paper:** "A uniform plane wave with amplitude $E_m = 100\ V/m$ is normally incident on the plane of the
  lossless dielectric with parameters $\mu = \mu_0$, $\varepsilon = 4\varepsilon_0$ and $\sigma_2 = 0$."
- **Issue:** the subscript on $\sigma_2$ announces a *second* medium, but the **first is never given**.
  $\eta_1$ is needed for the reflection and transmission coefficients, so parts (ii), (iii) and (iv) — 9 of
  the question's 12 marks — cannot be worked from what is printed.
- **Likeliest intent:** region 1 is free space. **Computed here 2026-09-03 on that assumption:**
  $\eta_2 = \eta_0/\sqrt{4} \approx 188.4\ \Omega$, $\Gamma = (\eta_2-\eta_0)/(\eta_2+\eta_0) = -1/3$,
  $\tau = 2/3$. The numbers come out clean, which is itself weak evidence the free-space reading is intended.
- **How to handle:** state the assumption in the first line of any answer, every time.
- **Severity:** omission.

### P31 · BEE 3102 End of Semester (23 Oct 2025), Q5(c) — the figure is named for a different question
- **Paper:** "Consider the potential shown in **Figure  Q3c**", and the drawing itself is captioned
  "**Figure Q3c**".
- **Issue:** "Q3c" names a part of Question **Three**; this is Question **Five**. Because the caption carries
  the same wrong number as the text, the figure looks lifted from another paper rather than mis-referenced.
  Separately, Question Four's figure is captioned "**Figure 1**", which is also the caption on the figure of
  the 1 Oct 2025 CAT — two different drawings, three weeks apart, same name.
- **How to handle:** cite figures in this folder as `<paper_id> <figure id>`, never by the paper's own
  caption alone.
- **Severity:** cataloguing.

### P32 · BEE 3102 End of Semester (23 Oct 2025), Question Five — no marks in the heading, and "points" for marks
- **Paper:** "QUESTION FIVE", with no total, while Questions TWO, THREE and FOUR each print "(15 MARKS)".
  Its sub-parts are then marked "**(4 points)**" and "**(6 points)**".
- **Issue:** inconsistent with the rest of the paper on both counts.
- **Verified here 2026-09-03:** Question Five's parts sum to 2 + 3 + 4 + 6 = **15**, matching the other
  optional questions exactly, so nothing is actually lost — unlike the 2024 exam, where the same class of
  omission hid nine marks (P1).
- **Severity:** structural (no numerical consequence).

### P33 · BEE 3102 End of Semester (23 Oct 2025), Figure Q3c — one boundary point that two node equations need is unlabelled
- **Paper:** the stepped mesh carries five boundary values — 20 V on the top of the upper block, 20 V on the
  top of the lower-left portion, 40 V on the right edge, −10 V on the left edge, 0 V on the bottom.
- **Issue:** the **re-entrant corner** — the point where the lower-left portion's 20 V top edge meets the
  upper block's left wall — carries no value, and the upper block's left wall is unlabelled along its whole
  length. **Traced here 2026-09-03 through the five-point stencil:** that corner is the *up*-neighbour of
  node 3 **and** the *left*-neighbour of node 1. Two of the four node equations need a number the figure
  never gives.
- **Likeliest reading:** 20 V — the corner is the end point of the 20 V segment. That closes the problem.
- **How to handle:** state which reading is being used before working the question, and ask the lecturer.
  Working it both ways costs little and shows how much the answer moves. The 25 Oct 2024 exam's Fig.1Q5
  carries the same class of defect (**P13**), which suggests the drawings are reused without checking that
  the boundary closes.
- **Severity:** ambiguity.

### P34 · BEE 3102 End of Semester (23 Oct 2025), Q1(c) — 10 mW/m² for an exposure limit, again
- **Paper:** "Human exposure to the electromagnetic radiation in air is regarded as safe if the power density
  is less than **10 mW/m²**. Determine the corresponding electric field intensity".
- **Issue:** this is the **same value, in the same question**, that the 13 Aug 2025 CAT printed (its Q1d),
  where it is already flagged as probably meaning **10 W/m²**. The recurrence means it is a fixed feature of
  the question bank, not a one-off typo.
- **Computed here 2026-09-03**, using $\eta_0 = 376.82\ \Omega$ from this paper's own constants:
  10 mW/m² → $E_{peak} = 2.75$ V/m ($E_{rms} = 1.94$ V/m); 10 W/m² → $E_{peak} = 86.8$ V/m
  ($E_{rms} = 61.4$ V/m).
- **How to handle:** answer as printed and add one line naming the alternative and its number. Do not
  silently substitute. The paper also does not say whether peak or rms is wanted — give both.
- **Severity:** value (suspected, not proven).

### P35 · BEE 3102 End of Semester (23 Oct 2025), Q3(b) — a closed-loop integral sign over a volume element
- **Paper:** $\oint -(E \times H).ds = \oint (E.J_c)dv + \frac{\partial}{\partial t}\int\left(\frac{\varepsilon E^2}{2} + \frac{\mu H^2}{2}\right)dv$
- **Issue:** the **middle** term pairs a closed-surface/loop integral sign with a **volume** element $dv$.
  The term is the ohmic dissipation throughout the volume and should be an ordinary volume integral
  $\int(E\cdot J_c)dv$. The first term is correctly a closed surface integral over $ds$; the third term is
  correctly an open $\int … dv$ — so the equation is inconsistent with itself inside one line.
- **How to handle:** it does not change what the three terms *mean*, which is all the question asks for, so
  it costs no marks — but point it out, because the whole skill being taught here is reading the integral
  signs to tell the three terms apart.
- **Severity:** notation.

### P36 · BEE 3102 End of Semester (23 Oct 2025) — cosmetic slips, collected
- "equitation" for "equation" (Q3b) · "(1 marks)" (Q1h iv) · "state one area of its  of application" — a word
  duplicated or dropped (Q5a) · "The total E=electric field" (Q4b iv) · "Taylors" for "Taylor's" (Q5b) ·
  Question One's items **g.** and **h.** printed with full stops and in a different type style from the
  bracketed a)–f) above them · "QUESTION FOUR(15 MARKS)" with no space · "20Cos" capitalised mid-expression
  (Q1f) · double spaces in "wave exist  simultaneously", "Figure  1", "Figure  Q3c", "the **FOUR**  primary",
  "Use **four**  iterations", "( 4 marks)", "( 2 marks)" · "with respect to the load line" in Q2(b)(iv),
  where "with respect to the load" is meant.
- **Severity:** cosmetic. One entry for the lot, as the house rule requires.

### P37 · BEE 3102 End of Semester (23 Oct 2025) — the unit code is the 2024 CATs' code, and Digital Electronics'
- **Paper:** "BEE3102 : ELECTROMAGNETIC FIELDS AND WAVES".
- **Issue:** BEE 3102 is (a) the code both **2024 CATs** for this unit carried, and (b) the code on the
  **2024 Digital Electronics CAT of 6 Aug 2024**
  (`../../../digital-electronics/knowledge-base/past-papers/`). Meanwhile this same 2025 cohort sat CAT 1 as
  **EEE 3202** and the 1 Oct CAT as **BEE 3101**. That is **four code/date combinations** for one unit across
  two cohorts, with the 2024 codes swapped between exam and CAT for 2025.
- **How to handle:** match by unit **name** and **date**, always. Treat the code as decoration. See P25.
- **Severity:** cataloguing.

<!-- Later papers append their own P-numbered entries above this line. -->

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
