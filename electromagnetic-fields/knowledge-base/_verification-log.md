---
kb: "Electromagnetic Fields — EEE3202"
file_role: verification-log
purpose: "Every suspected error found in the current-cohort handouts, with what the page prints, the correct form, and why. Consult before teaching any section; prefer the corrected form."
sources_covered: "WC1 (18 pp.)"
totals: "43 flags on WC1 — 20 substantive (V1–V20), 23 cosmetic (C1–C23)"
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

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
