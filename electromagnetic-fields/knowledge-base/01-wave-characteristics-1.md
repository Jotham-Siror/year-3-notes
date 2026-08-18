---
kb: "Electromagnetic Fields — EEE3202"
lecturer: "withheld"
section: "01 — Electromagnetic Wave Characteristics I"
source: "WC1 — 'ELECTROMAGNEIC WAVE CHARACTERISTICS I.pdf', 18 pp."
file_role: topic
subtopics:
  - "wave equation derived from Maxwell's equations (general homogeneous medium)"
  - "wave equation specialised: conducting / perfect dielectric / free space"
  - "uniform plane waves and the one-dimensional reduction"
  - "d'Alembert solution and the travelling-wave picture"
  - "sinusoidal (phasor) form of the fields and of Maxwell's equations"
  - "E–H relationship in a plane wave; intrinsic impedance"
  - "propagation constant, attenuation constant, phase constant"
  - "loss tangent, complex permittivity, conductor/dielectric classification"
  - "plane waves in lossy, perfect-dielectric and conducting media"
  - "depth of penetration and skin depth"
key_equations:
  [wave-equation-general, wave-equation-dielectric, wave-equation-free-space,
   dalembert, intrinsic-impedance, eta-free-space, propagation-constant,
   alpha-general, beta-general, loss-tangent, complex-permittivity,
   alpha-lossy, beta-lossy, eta-lossy, alpha-beta-conductor, eta-conductor,
   skin-depth]
prerequisites: []
leads_to: ["02 — Wave Characteristics II (not yet issued)"]
verification_flags: 43   # 20 substantive (V1–V20) + 23 cosmetic (C1–C23)
tags: [maxwell, wave-equation, plane-wave, tem, intrinsic-impedance,
       propagation-constant, attenuation, phase-constant, loss-tangent,
       complex-permittivity, lossy-dielectric, good-conductor, skin-depth,
       depth-of-penetration, eee3202]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set on the handout ·
  [fig] figure described from the rendered page · [added] not in the handout — supplied here ·
  ·WC1 pN provenance · ⚠ VERIFY = flagged suspected handout error, see _verification-log.md -->

# 01 — Electromagnetic Wave Characteristics I

**Source:** WC1, 18 pages. Covers stated objectives (i)–(iii). Objective (iv), *Types of
polarization*, is listed on p1 but **never appears in this handout** — see `00-index.md` § Gap map.

This handout is one continuous argument: start from Maxwell's equations, produce a wave equation,
specialise it to a plane wave, solve it in each class of medium, and let skin depth fall out of the
good-conductor case. Later sections depend on earlier ones throughout.

> **Reliability note.** The physics here is sound but the typesetting is not. Twenty substantive
> defects were found, concentrated on pp. 9–11 and 16, where $\sigma$ is used for both conductivity
> and the attenuation constant. Prefer the corrected forms below; each departure from the page is
> marked ⚠ VERIFY with an ID into `_verification-log.md`.

---

## 1. The wave equation

### 1.1 What a wave is ·WC1 p1

[def] A **wave** is a disturbance or variation in a medium that transfers energy from one point to
another in that medium.

### 1.2 Maxwell's equations, differential form ·WC1 p1

[eq] The four equations the whole handout is built on:

$$\nabla \times \vec{H} = \frac{\partial \vec{D}}{\partial t} + \vec{J} \tag{1}$$

$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} \tag{2}$$

$$\nabla \cdot \vec{D} = \rho_v \tag{3}$$

$$\nabla \cdot \vec{B} = 0 \tag{4}$$

with the constitutive relations $\vec{D} = \varepsilon\vec{E}$, $\vec{B} = \mu\vec{H}$,
$\vec{J} = \sigma\vec{E}$.

- $\vec{E}$ = electric field intensity (V/m); $\vec{H}$ = magnetic field intensity (A/m)
- $\vec{D}$ = electric flux density (C/m²); $\vec{B}$ = magnetic flux density (T)
- $\vec{J}$ = current density (A/m²); $\rho_v$ = volume charge density (C/m³)
- $\varepsilon$ = permittivity (F/m); $\mu$ = permeability (H/m); $\sigma$ = conductivity (S/m)

**Assumption used throughout:** a *homogeneous* medium — $\varepsilon$, $\mu$, $\sigma$ constant
everywhere.

### 1.3 Wave equation for $\vec{H}$ ·WC1 p1–2

[derivation] Take the curl of (1):

$$\nabla \times \nabla \times \vec{H} = \left(\nabla \times \frac{\partial \vec{D}}{\partial t}\right) + (\nabla \times \vec{J})$$

Substitute $\vec{D} = \varepsilon\vec{E}$ and $\vec{J} = \sigma\vec{E}$:

$$\nabla \times \nabla \times \vec{H} = \varepsilon\frac{\partial(\nabla \times \vec{E})}{\partial t} + \sigma(\nabla \times \vec{E}) \tag{5}$$

> ⚠ VERIFY **V4** — the handout writes the second term as $\varepsilon(\nabla \times \vec{E})$ on
> **both** lines of this step. It must be $\sigma(\nabla \times \vec{E})$: the bracket printed
> directly beneath states $\vec{J} = \sigma\vec{E}$, and the very next line (p2) correctly produces
> $-\mu\sigma\,\partial H/\partial t$.

Now substitute (2), $\nabla \times \vec{E} = -\mu\,\partial \vec{H}/\partial t$:

$$\nabla \times \nabla \times \vec{H} = -\mu\varepsilon\frac{\partial^2 H}{\partial t^2} - \mu\sigma\frac{\partial H}{\partial t}$$

Apply the vector identity $\nabla \times \nabla \times \bar{A} = \nabla(\nabla \cdot \bar{A}) - \nabla^2\bar{A}$:

$$\nabla(\nabla \cdot \bar{H}) - \nabla^2\bar{H} = -\mu\varepsilon\frac{\partial^2 H}{\partial t^2} - \mu\sigma\frac{\partial H}{\partial t}$$

and $\nabla \cdot \bar{H} = 0$ (since $\nabla \cdot \bar{B} = 0$ and $\bar{B} = \mu\bar{H}$), giving:

[eq: wave-equation-general]
$$\boxed{\;\nabla^2\bar{H} = \mu\varepsilon\frac{\partial^2 H}{\partial t^2} + \mu\sigma\frac{\partial H}{\partial t}\;} \tag{6}$$

> ⚠ VERIFY **V5** — the handout writes this boxed result (and (8) and (10) later) as
> $\nabla^2\bar{A}$. $\bar{A}$ is only the dummy vector of the identity; the equation being derived
> is for $\bar{H}$. Equation (9) on p3 writes $\nabla^2\bar{H}$ correctly, confirming the slip.

### 1.4 Wave equation for $\vec{E}$ ·WC1 p2–3

[derivation] Same procedure, starting from the curl of (2):

$$\nabla \times \nabla \times \bar{E} = -\frac{\partial(\nabla \times \bar{B})}{\partial t} = -\mu\frac{\partial(\nabla \times \bar{H})}{\partial t}$$

Using (1):

$$\nabla \times \nabla \times \bar{E} = -\mu\frac{\partial}{\partial t}\left(\frac{\partial \vec{D}}{\partial t} + \vec{J}\right)$$

With the identity, $\vec{D} = \varepsilon\vec{E}$, $\vec{J} = \sigma\vec{E}$, and
$\nabla \cdot \bar{E} = 0$ in a charge-free medium:

[eq]
$$\boxed{\;\nabla^2\bar{E} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2} + \mu\sigma\frac{\partial\bar{E}}{\partial t}\;} \tag{7}$$

(6) and (7) are **the wave equations for a homogeneous medium**. Everything that follows is these
two equations under different assumptions about $\sigma$.

### 1.5 Conducting media ·WC1 p3

[def] In a conducting medium no net charge exists in the bulk, so the charge density is zero:

$$\nabla \cdot \bar{D} = \rho_v = 0 \quad\Longrightarrow\quad \nabla \cdot \bar{E} = 0$$

> ⚠ VERIFY **V6** — the handout prints this as one chain,
> $\nabla \cdot \bar{D} = \rho_s = \nabla \cdot \bar{E} = 0$. Two faults: $\rho_s$ is *surface*
> charge density (C/m²) where the volume density $\rho_v$ (C/m³) is meant — as correctly used in
> (3) on p1; and $\nabla \cdot \bar{D}$ and $\nabla \cdot \bar{E}$ differ by a factor $\varepsilon$
> and cannot be equated. They are two separate statements.

[eq] The wave equations are therefore unchanged from (6) and (7) — the full lossy form:

$$\nabla^2\bar{H} = \mu\varepsilon\frac{\partial^2 H}{\partial t^2} + \mu\sigma\frac{\partial H}{\partial t}, \qquad \nabla^2\bar{E} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2} + \mu\sigma\frac{\partial\bar{E}}{\partial t} \tag{8}$$

### 1.6 Perfect dielectric ·WC1 p3

[def] A perfect dielectric has **zero conductivity**, $\sigma = 0$. The first-order (damping) term
vanishes:

[eq: wave-equation-dielectric]
$$\boxed{\;\nabla^2\bar{H} = \mu\varepsilon\frac{\partial^2 H}{\partial t^2}, \qquad \nabla^2\bar{E} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2}\;} \tag{9}$$

### 1.7 Free space ·WC1 p3–4

[def] Free space is a perfect dielectric with no sources — both conductivity and charge density
are zero:

[eq: wave-equation-free-space]
$$\boxed{\;\nabla^2\bar{H} = \mu_0\varepsilon_0\frac{\partial^2 H}{\partial t^2}, \qquad \nabla^2\bar{E} = \mu_0\varepsilon_0\frac{\partial^2\bar{E}}{\partial t^2}\;} \tag{10}$$

---

## 2. Uniform plane waves

### 2.1 Definition and characteristics ·WC1 p4

[def] A **plane wave** is an idealised wave whose wave fronts are infinite, parallel, flat planes
perpendicular to the direction of travel.

Characteristics as listed on the handout:

1. **Constant values** — wave properties are identical at every point of a given wave front.
2. **Direction** — the wave travels in a single, unchanging direction.
3. **No energy loss** — unlike spherical waves, it does not spread out.

> ⚠ VERIFY **V7** — the handout's wording for (1) is *"Wave properties (e.g the electric field) are
> identical across any chosen direction"*, which is false as written: the field certainly varies
> along the propagation direction $z$ — that variation **is** the wave. The correct statement is
> that the field is identical at every point of any plane **perpendicular to** the direction of
> propagation.

### 2.2 Why plane waves matter ·WC1 p4

- They simplify the mathematics used to solve real-world problems
- They are mathematical building blocks (via Fourier series)
- They are easier to solve
- They are accurate approximations — far from a source, curved wave fronts flatten and appear plane
- They are the foundation of antenna design

### 2.3 The one-dimensional reduction ·WC1 p4–5

[def] A **uniform plane wave** travels in one direction and is independent of the other two. For
propagation along $z$:

$$\frac{\partial\bar{E}}{\partial x} = \frac{\partial\bar{E}}{\partial y} = 0$$

[eq] In Cartesian coordinates the Laplacian is

$$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

> ⚠ VERIFY **V2** — the handout prints
> $\nabla^2 = \partial/\partial x + \partial/\partial y + \partial/\partial z$, **without the
> squares**. As printed it is a first-order operator and cannot produce the
> $\partial^2\bar{E}/\partial z^2$ that appears three lines below it.

So (9) reduces to the one-dimensional wave equations:

[eq]
$$\frac{\partial^2\bar{E}}{\partial z^2} = \mu\varepsilon\frac{\partial^2\bar{E}}{\partial t^2} \tag{11}$$

$$\frac{\partial^2\bar{H}}{\partial z^2} = \mu\varepsilon\frac{\partial^2\bar{H}}{\partial t^2} \tag{12}$$

### 2.4 d'Alembert solution ·WC1 p5–6

[def] Any twice-differentiable function whose argument is a linear combination of position and time
solves this 1-D wave equation. The general solution:

[eq: dalembert]
$$\boxed{\;E(z,t) = f(z - vt) + g(z + vt)\;}$$

- $f(z-vt)$ — a wave profile travelling in the **positive** $z$-direction
- $g(z+vt)$ — a wave profile travelling in the **negative** $z$-direction

[eq] with propagation velocity

$$v = \frac{1}{\sqrt{\mu\varepsilon}}$$

[fig] **Figure 1 ·WC1 p6.** Vertical axis arrow labelled $F$; horizontal axis arrow. Two identical
wave profiles sit on the horizontal axis — the left labelled $f(z,0)$, the right labelled $f(z,t)$,
each roughly one full sine cycle (positive hump then trough). Below them a double-headed dimension
arrow between two vertical ticks is labelled $vt$, spanning the rigid rightward shift of the profile
between the two instants. The figure shows a wave shape translating without changing form.

> ⚠ VERIFY **V8** — Figure 1's horizontal axis is labelled **$t$**; it must be **$z$**. The two
> profiles are separated on that axis by the interval $vt$, which is a *distance*. Plotting $F$
> against $t$ cannot display a spatial displacement.

---

## 3. Sinusoidal (phasor) form

### 3.1 Harmonic field quantities ·WC1 p6

[eq] For sinusoidal variation:

$$\tilde{E} = E e^{j\omega t}, \qquad \tilde{H} = H e^{j\omega t}$$

$$\frac{d\tilde{E}}{dt} = j\omega E e^{j\omega t} = j\omega\tilde{E}, \qquad \frac{\partial^2\tilde{E}}{\partial t^2} = j^2\omega^2\tilde{E} = -\omega^2\tilde{E}$$

This is the step that turns the PDEs into algebraic equations: every $\partial/\partial t$ becomes
a multiplication by $j\omega$.

### 3.2 Maxwell's equations for harmonic fields ·WC1 p6

[eq]
$$\nabla \times \vec{H} = \sigma\vec{E} + j\omega\varepsilon\vec{E} = (\sigma + j\omega\varepsilon)\vec{E} \tag{1'}$$

$$\nabla \times \vec{E} = -j\omega\bar{B} \tag{2'}$$

$$\nabla \cdot \vec{D} = \rho_v \tag{3'}$$

$$\nabla \cdot \vec{B} = 0 \tag{4'}$$

> ⚠ VERIFY **V3** — the handout prints (1′) as
> $\nabla \times \vec{H} = j\omega\varepsilon E + j\omega\sigma E$. Only $\partial D/\partial t$
> picks up the $j\omega$ factor; the conduction term $\vec{J} = \sigma\vec{E}$ is not
> time-differentiated. The handout's own later result
> $\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon)$ (pp. 9 and 13) **requires** $\sigma E$, so
> the page contradicts itself.

### 3.3 Wave equations in phasor form ·WC1 p7

[eq] Lossless medium:

$$\nabla^2 E = -\omega^2\mu\varepsilon E$$

[eq] Conducting medium:

$$\nabla^2 E + (\omega^2\mu\varepsilon - j\omega\mu\sigma)E = 0$$

*(Both correct as printed.)*

---

## 4. Relationship between E and H, and intrinsic impedance

### 4.1 E and H are mutually perpendicular ·WC1 p7

[derivation] Take a linearly polarised plane wave travelling in $+z$ through a source-free, lossless
medium, with $\vec{E}$ entirely along $x$:

$$E(z) = E_0 e^{-jkz}\,a_x$$

Apply $\nabla \times \vec{E} = -j\omega\mu H$. The curl determinant

$$\nabla \times \vec{E} = \begin{vmatrix} a_x & a_y & a_z \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] E_x(z) & 0 & 0 \end{vmatrix} = \frac{\partial E_x}{\partial z}\,\bar{a}_y$$

Substituting $E_x = E_0 e^{-jkz}$:

$$\frac{\partial E_x}{\partial z} = -jkE_0 e^{-jkz}$$

Equating and solving for $H$:

$$-j\omega\mu H = -jkE_0 e^{-jkz} \quad\Longrightarrow\quad H = \left(\frac{k}{\omega\mu}\right)E_0 e^{-jkz}\,a_y$$

**Result:** $E$ lies along $x$, $H$ lies along $y$, propagation is along $z$ — $E$, $H$ and the
direction of propagation are **mutually perpendicular**. This is what makes the wave TEM.

### 4.2 Intrinsic impedance ·WC1 p7–8

[def] The ratio of electric to magnetic field amplitude is the **intrinsic impedance** $\eta$.

[eq: intrinsic-impedance] With $k = \omega\sqrt{\mu\varepsilon}$:

$$\boxed{\;\eta = \frac{E_x}{H_y} = \frac{\omega\mu}{k} = \sqrt{\frac{\mu}{\varepsilon}}\;}$$

- $\eta$ = intrinsic (characteristic) impedance (Ω)
- $k$ = wave number (rad/m)

[eq] So the magnetic field follows directly from the electric field:

$$H(z) = \frac{E_0}{\eta}e^{-jkz}\,a_y$$

### 4.3 Intrinsic impedance of free space ·WC1 p8

[eq: eta-free-space] With $\mu_0 = 4\pi \times 10^{-7}$ H/m and
$\varepsilon_0 = \dfrac{10^{-9}}{36\pi}$ F/m:

$$\boxed{\;\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = 120\pi \approx 377\ \Omega\;}$$

> ⚠ VERIFY **V1** — the handout prints $\mu_0 = 4\pi \times 10^{-12}$ H/m. This is the single most
> damaging error in the document. With the printed value,
> $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = 1.19\ \Omega$, not the 377 Ω stated on the very next line,
> and $c = 1/\sqrt{\mu_0\varepsilon_0} = 9.49\times10^{10}$ m/s — some 317 times the speed of
> light. Self-contradictory within three lines. Correct value: $\mu_0 = 4\pi \times 10^{-7}$ H/m.
> *(Both figures re-computed — see `_verification-log.md` V1.)*

[def] Physical reading: for every 377 V/m of electric field strength in a free-space plane wave,
there is exactly 1 A/m of magnetic field intensity.

### 4.4 Summary as given ·WC1 p8

1. The ratio of electric to magnetic field amplitude is the characteristic impedance $\eta$; in free
   space its value is $120\pi$.
2. The electric field is normal to the magnetic field.
3. The cross product of the fields gives the direction of travel.

---

## 5. Wave propagation and the propagation constant

### 5.1 The propagation constant ·WC1 p8–9

[def] The most general case is a **lossy dielectric**, where the wave loses power as it propagates.
In phasor form:

$$\nabla^2 H = j\mu\omega(\sigma + j\omega\varepsilon)\bar{H} \quad\Longrightarrow\quad \nabla^2 H = \gamma^2\bar{H}$$

[eq: propagation-constant]
$$\boxed{\;\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon)\;}$$

and identically $\nabla^2 E = \gamma^2\bar{E}$.

[def] $\gamma$ is complex, with **real part $\alpha$** (attenuation constant, Np/m) and **imaginary
part $\beta$** (phase constant, rad/m):

$$\gamma = \alpha + j\beta$$

> ⚠ VERIFY **V9** — the handout says *"The propagation constant is complex with real value $\sigma$
> and complex value $\beta$."* Two faults: $\sigma$ is the conductivity, already in use — the real
> part is $\alpha$; and $\beta$ is the *imaginary part*, not a "complex value". This sentence seeds
> the $\sigma$/$\alpha$ confusion that then corrupts pp. 10 and 16.

[eq: alpha-general] [eq: beta-general] The two constants:

$$\boxed{\;\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1\right]}\;}$$

$$\boxed{\;\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1\right]}\;}$$

> ⚠ VERIFY **V10** — bracket grouping. As typeset on pp. 9, 10 and 16, the outer radical spans
> everything but there is **no bracket** grouping $\left[\sqrt{1+(\sigma/\omega\varepsilon)^2} \mp 1\right]$
> as the factor multiplying $\mu\varepsilon/2$. Read literally the page says
> $\omega\sqrt{(\mu\varepsilon/2)\sqrt{1+(\sigma/\omega\varepsilon)^2} - 1}$, which is wrong. The
> $\mp 1$ must sit **inside** the square bracket, multiplied by $\mu\varepsilon/2$.

### 5.2 Derivation of $\alpha$ and $\beta$ ·WC1 p9–10

[derivation] Expand $\gamma^2$:

$$\gamma^2 = j\mu\omega(\sigma + j\omega\varepsilon) = j\mu\omega\sigma - \omega^2\mu\varepsilon$$

and separately $(\alpha + j\beta)^2 = \alpha^2 - \beta^2 + j2\alpha\beta$.

> ⚠ VERIFY **V11** — the handout writes this as $(\sigma + j\beta)^2$. The RHS printed is the
> expansion of $(\alpha + j\beta)^2$, and $\gamma = \alpha + j\beta$ was defined one line earlier.

Equating real and imaginary parts:

$$\alpha^2 - \beta^2 = -\omega^2\mu\varepsilon \tag{2}$$

$$2\alpha\beta = \mu\omega\sigma \tag{3}$$

Using the algebraic identity $(\alpha^2+\beta^2)^2 = (\alpha^2-\beta^2)^2 + (2\alpha\beta)^2$:

$$\alpha^2 + \beta^2 = \sqrt{(\alpha^2 - \beta^2)^2 + 4\alpha^2\beta^2} \tag{4}$$

$$= \sqrt{(\omega^2\mu\varepsilon)^2 + (\mu\omega\sigma)^2} = \omega^2\mu\varepsilon\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} \tag{5}$$

> ⚠ VERIFY **V12** — the handout prints (4) as $\sigma^2 + \beta^2 = \sqrt{(\alpha^2-\beta^2)^2 + 4\sigma^2\beta^2}$
> — two independent $\sigma$-for-$\alpha$ slips in one line.
>
> ⚠ VERIFY **V13** — the handout prints (5) as $\omega\sqrt{\mu\varepsilon}\sqrt{1+(\sigma/\omega\varepsilon)^2}$,
> **missing a power**. It must be $\omega^2\mu\varepsilon$. Dimensional check: the LHS
> $\alpha^2+\beta^2$ is m⁻², while $\omega\sqrt{\mu\varepsilon}$ is m⁻¹.

Adding (2) and (5) gives $2\alpha^2$; subtracting gives $2\beta^2$. Hence the boxed results in §5.1.

> ⚠ VERIFY **V14** — the handout's "adding" line reads
> $2\sigma^2 = \omega\sqrt{\mu\varepsilon\sqrt{1+(\sigma/\omega\varepsilon)^2} - 1}$, with an outer
> radical over the whole right-hand side. Adding (2) to the corrected (5) gives $2\alpha^2$
> **directly** — no square root at that step — and $\omega^2\mu\varepsilon$, not
> $\omega\sqrt{\mu\varepsilon}$.
>
> ⚠ VERIFY **V15** — the boxed result on p10 is labelled $\sigma$, not $\alpha$. Because $\sigma$
> also appears *inside* the same expression, the equation as printed is self-referential and cannot
> be solved. The formula itself is correct; only the label is wrong.

### 5.3 General intrinsic impedance ·WC1 p10–11

[eq] Solving Maxwell's equations in phasor form:

$$\frac{E}{H} = \eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$

[eq] The impedance is complex, with magnitude and angle:

$$|\eta| = \frac{\sqrt{\mu/\varepsilon}}{\left[1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2\right]^{1/4}} \qquad\text{equivalently}\qquad |\eta| = \frac{\sqrt{\omega\mu}}{\left[\sigma^2 + (\omega\varepsilon)^2\right]^{1/4}}$$

$$\theta_\eta = \frac{1}{2}\tan^{-1}\left(\frac{\sigma}{\omega\varepsilon}\right), \qquad 0 \le \theta_\eta \le 45°$$

> ⚠ VERIFY **V16** — the handout prints
> $|\eta| = \sqrt{\mu/\varepsilon}\big/[\sigma + (j\omega\varepsilon)^2]^{1/4}$. Three faults:
> $\sigma$ should be $\sigma^2$; $(j\omega\varepsilon)^2 = -\omega^2\varepsilon^2$ makes the bracket
> $\sigma - \omega^2\varepsilon^2$, typically negative, so the fourth root would be imaginary; and
> adding $\sigma$ (S/m) to $(\omega\varepsilon)^2$ (S²/m²) is dimensionally inhomogeneous.

---

## 6. Classifying the medium: loss tangent

### 6.1 Conduction versus displacement current ·WC1 p11–12

[derivation] From Maxwell's curl equation for $H$:

$$\nabla \times H = \vec{J}_c + \frac{\partial \vec{D}}{\partial t} = \sigma E + \varepsilon\frac{\partial E}{\partial t}$$

- $\vec{J}_c = \sigma E$ — conduction current density
- $\vec{J}_{disp} = \partial D/\partial t$ — displacement current density

[eq] Their ratio:

$$\boxed{\;\frac{J_c}{J_{disp}} = \frac{\sigma}{j\omega\varepsilon}\;}$$

The two are **90° out of phase in time**, with $J_{disp}$ leading $J_c$.

[eq: loss-tangent] The displacement current density leads the *total* current density by an angle
$\theta$:

$$\boxed{\;\tan\theta = \frac{\sigma}{\omega\varepsilon}\;}$$

This is the **loss tangent** — the single number that decides whether a medium behaves as a
conductor or a dielectric at a given frequency.

[fig] **Figure 2 ·WC1 p12.** A current-density phasor diagram drawn as a parallelogram. From a
common origin at the lower left: a solid arrow up-and-right to $J_{disp} = \omega\varepsilon E$;
a solid arrow down-and-right to $J_c = \sigma E$ (drawn roughly perpendicular to the first, as they
should be); and a solid resultant arrow to the right, lying between them, labelled
$J = (\sigma + j\omega\varepsilon)E$. Dashed lines complete the parallelogram. A small arc at the
origin marks $\theta$ between $J_{disp}$ and the resultant $J$, with a label along the lower dashed
line reading $\theta = \tan^{-1}(\sigma/\omega\varepsilon)$.

The geometry is **correct and self-consistent**:
$\tan\theta = |J_c|/|J_{disp}| = \sigma/\omega\varepsilon$, matching the boxed equation.
*(Cosmetic defect C13: the $J_{disp}$ label drops the $j$, while the resultant on the same drawing
keeps it.)*

### 6.2 Complex permittivity ·WC1 p12

[derivation] Rewriting the propagation constant:

$$\gamma^2 = j^2\omega^2\mu\varepsilon\left(1 + \frac{\sigma}{j\omega\varepsilon}\right) \qquad\text{or}\qquad \gamma = j\omega\sqrt{\mu\varepsilon^*}$$

> ⚠ VERIFY **V17** — the handout prints the second form as $\gamma^2 = j\omega\sqrt{\mu\varepsilon^*}$.
> The LHS would be m⁻² and the RHS m⁻¹. It is $\gamma$, not $\gamma^2$ — as the handout itself uses
> correctly on pp. 13 and 15.

[eq: complex-permittivity] where $\varepsilon^*$ is the **generalised complex permittivity**:

$$\boxed{\;\varepsilon^* = \varepsilon\left(1 - \frac{j\sigma}{\omega\varepsilon}\right)\;}$$

### 6.3 Conductor or dielectric? ·WC1 p13

[def] The classification table as given:

| Condition | Current comparison | Medium behaves as |
|---|---|---|
| $\sigma/\omega\varepsilon \gg 1$ | $J_c \gg dD/dt$ | **Conducting** medium |
| $\sigma/\omega\varepsilon \ll 1$ | $J_c \ll dD/dt$ | **Dielectric** medium |
| $\omega = \sigma/\varepsilon$ | — | Borderline (crossover) |

The frequency $\omega$ and the ratio $\sigma/\varepsilon$ are together enough to characterise a
medium.

> **Note (C22, not an error):** the handout's third row reads *"Property of conductor and
> dielectric"* with an empty middle cell. It is the crossover condition where
> $\sigma/\omega\varepsilon = 1$ — the medium behaves as neither a good conductor nor a good
> dielectric. **Consequence worth remembering: the same material can be a conductor at one frequency
> and a dielectric at another.** Classification is not a property of the material alone.

---

## 7. Plane waves in each class of medium

### 7.1 Lossy medium ·WC1 p13–15

[def] A **lossy dielectric** has $\sigma/\omega\varepsilon \ll 1$ but not zero — a small amount of
energy is extracted from the wave as it travels.

[derivation] Starting from $\gamma = \sqrt{j\mu\omega(\sigma + j\omega\varepsilon)}$:

$$\gamma = j\omega\sqrt{\mu\varepsilon}\left(1 - \frac{j\sigma}{\omega\varepsilon}\right)^{1/2}$$

Since $\sigma/\omega\varepsilon \ll 1$, expand binomially and neglect third-order and higher terms:

$$\left(1 - \frac{j\sigma}{\omega\varepsilon}\right)^{1/2} = 1 - \frac{j\sigma}{2\omega\varepsilon} + \frac{1}{8}\frac{\sigma^2}{\omega^2\varepsilon^2}$$

*(Correct as printed — including the **+** sign on the third term, which is easy to get wrong:
with $x = -j\sigma/\omega\varepsilon$, the term $-x^2/8 = +\sigma^2/8\omega^2\varepsilon^2$.)*

$$\gamma = \omega\sqrt{\mu\varepsilon}\,\frac{\sigma}{2\omega\varepsilon} + j\omega\sqrt{\mu\varepsilon}\left(1 + \frac{1}{8}\frac{\sigma^2}{\omega^2\varepsilon^2}\right)$$

[eq: alpha-lossy] [eq: beta-lossy] Separating real and imaginary parts:

$$\boxed{\;\alpha = \frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}}\;} \qquad \boxed{\;\beta = \omega\sqrt{\mu\varepsilon}\left(1 + \frac{1}{8}\frac{\sigma^2}{\omega^2\varepsilon^2}\right)\;}$$

*(Both correct as printed.)*

[eq] Phase velocity $v_p = \omega/\beta$:

$$\boxed{\;v_p = \frac{1}{\sqrt{\mu\varepsilon}\left(1 + \dfrac{1}{8}\dfrac{\sigma^2}{\omega^2\varepsilon^2}\right)}\;}$$

> ⚠ VERIFY **V18** — the handout's line at the bottom of p14 is correct
> ($v_p = \omega\big/[\omega\sqrt{\mu\varepsilon}(1+\ldots)]$), but the version carried to the top
> of p15 cancels the $\omega$ from the denominator **while leaving it in the numerator**. As printed
> $v_p$ carries units of (m/s)·s⁻¹.

[eq: eta-lossy] Intrinsic impedance of a medium with finite conductivity:

$$\eta^* = \sqrt{\frac{\mu}{\varepsilon^*}} = \sqrt{\frac{\mu}{\varepsilon}}\,\frac{1}{\sqrt{1 - \dfrac{j\sigma}{\omega\varepsilon}}} \cong \sqrt{\frac{\mu}{\varepsilon}}\left(1 + \frac{j\sigma}{2\omega\varepsilon}\right) = \eta\left(1 + \frac{j\sigma}{2\omega\varepsilon}\right)$$

[def] Finite conductivity adds a **small reactive component** to the intrinsic impedance — that is
the loss, made visible. For most practical purposes the reactive part can be neglected without
appreciable error.

### 7.2 Perfect dielectric ·WC1 p15

[def] A perfect dielectric has $\sigma = 0$ exactly, so $j\sigma/\omega\varepsilon$ vanishes:

[eq]
$$\boxed{\;\gamma = j\omega\sqrt{\mu\varepsilon}\;}$$

With $\alpha = 0$: no attenuation, and $\beta = \omega\sqrt{\mu\varepsilon}$.

### 7.3 Good conductor ·WC1 p16–17

[def] For a conductor $\sigma/\omega\varepsilon \gg 1$, so the $1$ under the inner radical is
negligible and the general $\alpha$, $\beta$ collapse to the same value:

[eq: alpha-beta-conductor]
$$\boxed{\;\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \sqrt{\pi f\mu\sigma}\;}$$

> ⚠ VERIFY **V19** — on p16 the handout prints both results as $\sqrt{\omega\mu\alpha/2}$ and
> labels the first one $\sigma$: **$\sigma$ and $\alpha$ have been swapped with each other**. The
> next line confirms it — $v_p = \omega/\sqrt{\omega\mu\alpha/2}$ is then evaluated as
> $\sqrt{2\omega/\mu\sigma}$, using $\sigma$. *(Minor: the "$-1$" is dropped without an $\cong$
> sign; this step is an approximation, not an equality.)*

[eq] Phase velocity in a conductor:

$$v_p = \frac{\omega}{\beta} = \sqrt{\frac{2\omega}{\mu\sigma}}$$

[eq: eta-conductor] Intrinsic impedance. For a good conductor
$\varepsilon^* \approx -j\sigma/\omega$, so:

$$\eta^* = \sqrt{\frac{\mu}{\varepsilon^*}} = \sqrt{\frac{\mu}{-j\sigma/\omega}} = \sqrt{\frac{j\omega\mu}{\sigma}} = \sqrt{\frac{\omega\mu}{\sigma}}\,e^{+j\pi/4}$$

$$\boxed{\;\eta^* = \sqrt{\frac{\omega\mu}{\sigma}}\left(\cos\frac{\pi}{4} + j\sin\frac{\pi}{4}\right) = \sqrt{\frac{\omega\mu}{2\sigma}}(1 + j)\;}$$

> ⚠ VERIFY **V20** — the handout's middle term is $\sqrt{\mu\big/(-j\omega/\sigma)}$, with
> $\omega$ and $\sigma$ inverted. As printed that equals $j\mu\sigma/\omega$, which is **not** the
> $j\omega\mu/\sigma$ the third term correctly states. The correct intermediate is
> $\varepsilon^* \approx -j\sigma/\omega$.

[def] Consequences, as the handout states them: in a good conductor $\sigma$ is very large, so
$\alpha$ and $\beta$ are both very large. The wave is **greatly attenuated**, carries a large phase
shift per unit distance, and travels **very slowly** — so the wavelength contracts sharply as the
wave passes from free space into a conductor.

---

## 8. Depth of penetration and skin depth

### 8.1 Definition ·WC1 p17

[def] Conducting losses are very high, so at radio frequencies an EM wave penetrates **only a very
short distance** below a conductor's surface.

[def] **Depth of penetration $\delta$** is the depth at which the wave ($E$, $H$ and $J$) has been
attenuated to $1/e$, or approximately **37%**, of its surface value.

[derivation] With attenuation $e^{-\alpha x}$ into the conductor, the $1/e$ point is where
$\alpha x = 1$:

$$x = \frac{1}{\alpha} = \text{depth of penetration}$$

[eq: skin-depth] Substituting the good-conductor $\alpha$ from §7.3:

$$\boxed{\;\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega\mu\sigma}} = \frac{1}{\sqrt{\pi f\mu\sigma}}\;}$$

- $\delta$ = skin depth (m); $f$ = frequency (Hz); $\mu$ = permeability (H/m); $\sigma$ = conductivity (S/m)

*(Correct as printed. The two radical forms are identical since $\omega = 2\pi f$.)*

### 8.2 What $\delta$ depends on, and why it matters ·WC1 p17–18

[def] $\delta$ depends on **frequency, permeability and conductivity**, and **decreases** as any of
them rises.

Practical consequences as given:

- Rising frequency pushes the field and current toward the conductor's **surface** — the skin effect
- At high frequencies only the **surface coating** matters, since that is where the current flows
- A guiding structure can therefore be made of a **poor** conductor and plated with a thin layer of
  silver, copper or another good conductor, keeping $I^2R$ losses within tolerable limits

---

## 9. Tutorial questions ·WC1 p18

Two questions are set. Neither is solved on the handout.

### Question 1

[exercise] A plane electromagnetic wave travels in an unbounded **lossless dielectric** with
$\mu_r = 1$, $\varepsilon_r = 3$, and has a peak electric field intensity of 6 V/m. Find:
(a) the velocity of the wave; (b) the intrinsic impedance of the medium; (c) the peak value of the
magnetic field.

> ⚠ VERIFY **C21** — the handout prints the field as "6V". The volt is not a unit of field
> *intensity*, and part (c) divides this by $\eta$ (Ω) to obtain $H$ in A/m — the arithmetic only
> closes if the input is **V/m**.

[added] **Worked solution** — not on the handout; computed and numerically verified here.

No frequency is given, and none is needed: in a lossless medium both $v$ and $\eta$ are
frequency-independent.

**(a)** $v = \dfrac{c}{\sqrt{\mu_r\varepsilon_r}} = \dfrac{3\times10^8}{\sqrt{3}}$

$$v = 1.73 \times 10^8\ \text{m/s}$$

**(b)** $\eta = \eta_0\sqrt{\dfrac{\mu_r}{\varepsilon_r}} = \dfrac{120\pi}{\sqrt{3}}$

$$\eta = 217.7\ \Omega$$

**(c)** $H_{peak} = \dfrac{E_{peak}}{\eta} = \dfrac{6}{217.7}$

$$H_{peak} = 0.0276\ \text{A/m} = 27.6\ \text{mA/m}$$

### Question 2

[exercise] A plane electromagnetic wave of frequency **100 MHz** travels in an unbounded lossless
dielectric with $\mu_r = 1$, $\varepsilon_r = 4$. Find: (a) phase velocity $v_p$; (b) phase-shift
constant $\beta$; (c) wavelength; (d) intrinsic impedance.

> ⚠ VERIFY **C23** — part (d) reads "Intrinsic impedance of the **wave**". Intrinsic impedance is a
> property of the **medium**, not of the wave. Q1(b) words it correctly.

[added] **Worked solution** — not on the handout; computed and numerically verified here.

**(a)** $v_p = \dfrac{c}{\sqrt{\varepsilon_r}} = \dfrac{3\times10^8}{2}$

$$v_p = 1.5 \times 10^8\ \text{m/s}$$

**(b)** $\beta = \dfrac{\omega}{v_p} = \dfrac{2\pi \times 10^8}{1.5\times10^8}$

$$\beta = 4.19\ \text{rad/m}$$

**(c)** $\lambda = \dfrac{v_p}{f} = \dfrac{2\pi}{\beta}$

$$\lambda = 1.5\ \text{m}$$

**(d)** $\eta = \dfrac{\eta_0}{\sqrt{\varepsilon_r}} = \dfrac{377}{2} = 60\pi$

$$\eta = 188.5\ \Omega$$

*(Both solutions use the handout's own $\varepsilon_0 = 10^{-9}/36\pi$, $\eta_0 = 120\pi$
convention. Using the exact SI $\varepsilon_0 = 8.854\times10^{-12}$ shifts every answer by less
than 0.1%.)*

---

### Cross-references

- Symbol clashes — especially $\sigma$ (conductivity) versus the handout's misuse of $\sigma$ for
  $\alpha$ → `_nomenclature.md`
- All 43 flagged defects with corrected forms → `_verification-log.md`
- Every equation in one place → `_formula-sheet.md`
- Polarization (syllabus objective iv, absent here) → `00-index.md` § Gap map

### Verification notes for this section

- **43 flags: 20 substantive (V1–V20), 23 cosmetic (C1–C23).** Heaviest concentration on pp. 9–11
  and 16.
- Every page was read as a rendered image, not from the PDF text layer.
- Both tutorial questions were solved numerically; answers above are verified.
- $\mu_0$ (V1) is the most damaging single error — it makes $\eta_0$ and $c$ wrong by factors of
  317 and contradicts the handout's own next line.
- Confirmed **correct** and safe to learn as printed: the four Maxwell equations (p1); the
  curl-of-curl derivation for $E$ (p2); eq. 7; the d'Alembert solution and $v = 1/\sqrt{\mu\varepsilon}$
  (p5); the phasor derivatives (p6); the curl determinant and $H = (k/\omega\mu)E_0e^{-jkz}a_y$ (p7);
  $\eta = \omega\mu/k = \sqrt{\mu/\varepsilon}$ (p8); $\varepsilon_0 = 10^{-9}/36\pi$ and
  $\eta_0 = 120\pi = 377\ \Omega$ (p8); $\gamma^2 = j\mu\omega\sigma - \omega^2\mu\varepsilon$ and
  $2\alpha\beta = \mu\omega\sigma$ (pp. 9–10); $\theta_\eta = \frac12\tan^{-1}(\sigma/\omega\varepsilon)$
  with $0 \le \theta \le 45°$ (p11); $J_c/J_{disp} = \sigma/j\omega\varepsilon$ and
  $\tan\theta = \sigma/\omega\varepsilon$ (pp. 11–12); $\varepsilon^* = \varepsilon(1-j\sigma/\omega\varepsilon)$
  (p12); the binomial expansion including its **+** third term (p14); $\alpha = (\sigma/2)\sqrt{\mu/\varepsilon}$
  and $\beta = \omega\sqrt{\mu\varepsilon}(1+\sigma^2/8\omega^2\varepsilon^2)$ (p14);
  $\eta^* \cong \eta(1+j\sigma/2\omega\varepsilon)$ (p15); $v_p = \sqrt{2\omega/\mu\sigma}$ (p16);
  $\eta^* = \sqrt{\omega\mu/2\sigma}(1+j)$ (pp. 16–17); and
  $\delta = 1/\alpha = \sqrt{2/\omega\mu\sigma} = 1/\sqrt{\pi f\mu\sigma}$ (p17).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
