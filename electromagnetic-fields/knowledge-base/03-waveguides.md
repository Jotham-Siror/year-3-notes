---
kb: "Electromagnetic Fields — Year 3"
course_code: "EEE3202"
lecturer: "withheld"
file_role: topic
section: "03 — Rectangular waveguides"
source: "WG — 'Waveguides.pdf', 10 pp., lecturer-authored. Received 30 Sep 2026"
built: "Transcribed from pages rendered at 130 dpi and read directly; equations in canonical LaTeX; the transverse-field equations re-derived symbolically; suspected errors flagged inline and collected in _verification-log.md § W; both numerical revision questions solved and checked against the handout's own printed answers"
coverage: "10/10 pages mapped, no gaps"
subtopics:
  - "TEM versus higher-order lines; TE and TM modes"
  - "The four-step method"
  - "Phasor fields with e^{-jβz} dependence"
  - "Maxwell's curl equations in component form"
  - "Transverse fields from E_z and H_z; cut-off wave number k_c"
  - "TM modes: Helmholtz equation and separation of variables"
  - "Boundary conditions and the mode integers m, n"
  - "Results: β, f_c, λ_c, V_p, λ_g, Z_TE"
  - "Revision questions 1–5"
key_equations: [wg-kc, wg-beta, wg-fc, wg-lambda-c, wg-vp, wg-lambda-g, wg-zte]
prerequisites: ["01 §1 wave equation and γ² = jωμ(σ + jωε)", "01 §4 intrinsic impedance η", "02 §5 phasor form, β"]
leads_to: []
verification_flags: 21
tags: [waveguides, rectangular-waveguide, te-mode, tm-mode, tem, cut-off, guide-wavelength, phase-velocity, group-velocity, wave-impedance, high-pass]
---

# Rectangular Waveguides — WG

**What this is.** The waveguide topic, built from the lecturer's own handout *Waveguides* (10 pp.,
cited **·WG pN**). Until this arrived, rectangular waveguides were absent from the knowledge base
while being examined for about 17 marks on the 2024 end-of-semester paper. See `00-index.md` § Gap map.

> **Read this before teaching from the handout.** Three things about its shape matter.
>
> 1. **It derives the TM case only.** ·WG pp. 5–8 solve for $E_z$ with $H_z = 0$. The **TE** case is
>    never derived — yet the handout's own results page gives $Z_{TE}$, and **every revision
>    question is about a TE mode** ($TE_{10}$, $TE_{11}$).
> 2. **It gives no group velocity**, though revision Q4(c) and Q5(c) ask for it.
> 3. **·WG p9 says the short forms are not supplied in the exam:** *"Be familiar with the shorter
>    forms of the equations discussed in class as they will not be provided in the exams."* The
>    short forms in § 8 below are therefore the ones to memorise. Those not printed in the handout are
>    tagged `[added]`; the handout's own printed answers confirm every one of them.

## Exam weight — read first

| Part | Examined? |
|---|---|
| § 1 TEM vs TE vs TM | **Yes** — "why TEM cannot propagate in a waveguide", 2 marks, on the 3 Oct 2024 CAT *and* the 25 Oct 2024 exam |
| §§ 2–7 the derivation | **Never asked** in the six papers on file. Teach for understanding of where $k_c$ and $m$, $n$ come from; do not drill reproduction |
| § 8 the results | **Yes** — 8 marks (2024 exam Q4c) + 4 marks (2024 exam Q1e) |
| § 9 revision questions | **Q3 and Q4 are the 2024 exam's Q4(d) and Q4(c) word for word.** Q1(b) is its Q4(b) |

**Teach § 1, then § 8, then § 9.** Come back to §§ 2–7 only if time allows.

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example
(lecturer's numbers) · `[exercise]` problem stated but **not solved** in the source · `[fig]` figure
described from the rendered page · `[added]` supplied here, **not** in the source · `·WG pN`
provenance · `⚠ VERIFY` flagged suspected source error.

## Symbols used in this file

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $a$, $b$ | inner width and height of the guide | m | $a$ is the **broad** wall by convention, $a > b$ `[added]` |
| $m$, $n$ | mode integers — half-wave variations across $a$ and across $b$ | – | 0, 1, 2, … |
| $k = \omega\sqrt{\mu\varepsilon}$ | unbounded-medium wave number | rad/m | — |
| $k_c$ | **cut-off wave number** | rad/m | $\sqrt{(m\pi/a)^2 + (n\pi/b)^2}$ |
| $k_x$, $k_y$ | separation constants, $k_c^2 = k_x^2 + k_y^2$ | rad/m | $m\pi/a$, $n\pi/b$ |
| $\beta$ | phase constant **in the guide** | rad/m | — |
| $f_c$, $\lambda_c$ | cut-off frequency, cut-off wavelength | Hz, m | — |
| $\lambda$ | free-space (unbounded-medium) wavelength $c/f$ | m | — |
| $\lambda_g$ | **guide wavelength** $2\pi/\beta$ | m | always $> \lambda$ |
| $V_p$ | **phase velocity in the guide**, $\omega/\beta$ | m/s | always $> c$ |
| $V_g$ | **group velocity** — the speed energy travels | m/s | always $< c$ |
| $u = 1/\sqrt{\mu\varepsilon}$ | speed in the **unbounded** medium; $= c$ for an air-filled guide | m/s | $3\times10^8$ |
| $\eta = \sqrt{\mu/\varepsilon}$ | intrinsic impedance of the filling medium | Ω | 377 for air |
| $Z_{TE}$ | **wave impedance** of a TE mode in the guide | Ω | always $> \eta$ |
| $e_x(x,y)$, $h_x(x,y)$, … | lowercase: field components **without** the $e^{-j\beta z}$ factor | V/m, A/m | — |

> ⚠ **Two velocity symbols collide on ·WG p8.** The handout writes $V_p$ inside the $f_c$ formula
> where it means $u = 1/\sqrt{\mu\varepsilon}$, then writes $V_p = \omega/\beta$ for the guide phase
> velocity four lines later. They are different speeds. See W8 in § 8.

---

## § 1 · TEM, TE and TM — the three families

·WG pp. 1–2

**[def]** ·WG p1 · Transmission lines fall into two families:

1. Those that support **transverse electromagnetic (TEM)** modes — coaxial cable, two-wire line,
   parallel-plate line. $E$ and $H$ are **both** orthogonal to the direction of propagation.
2. **Higher-order** transmission lines, which may support $E$ **or** $H$ orthogonal to the direction
   of propagation, **but not both at once**. At least one field component lies along the direction of
   propagation. Examples: **waveguides** and **optical fibre**.

**[def]** ·WG p1 · The two higher-order mode types:

| Mode | Transverse to the propagation direction | Has a component along $z$ |
|---|---|---|
| **TE** — transverse electric | $E$ | $H$ ($H_z \neq 0$, $E_z = 0$) |
| **TM** — transverse magnetic | $H$ | $E$ ($E_z \neq 0$, $H_z = 0$) |

**[fig]** ·WG p1 — two product photographs of waveguide hardware: a blue flanged waveguide
assembly with square end flanges, and a set of black flexible waveguide sections with brass
flanges. No instructional content.

**[fig]** ·WG p2 — two hollow rectangular guides side by side, a green arrow labelled *Wave
propagation* running along their length.
- **TE mode** (left): blue electric-field lines run straight **across** the guide, top wall to
  bottom wall, with no component along the guide; orange magnetic-field loops lie in planes
  **parallel** to the broad walls and stretch along the guide.
- **TM mode** (right): orange magnetic loops lie **across** the guide, in the cross-section; blue
  electric lines curve round and run **along** the guide.
- Caption: *"Magnetic flux lines appear as continuous loops. Electric flux lines appear with
  beginning and end points."*

> **Exam note.** "Explain why TEM waves cannot propagate in (be supported by) a waveguide" — 2 marks
> on the 3 Oct 2024 CAT Q2(a) and again on the 25 Oct 2024 exam Q4(b). It is also this handout's
> revision Q1(b). The handout states the families but **does not give the reason**; it is answered,
> `[added]`, in § 9.

---

## § 2 · The four-step method

·WG pp. 2–3

**[def]** The handout lays out the route before taking it:

1. Manipulate Maxwell's equations to express the **transverse** components $E_x$, $E_y$, $H_x$,
   $H_y$ in terms of the **longitudinal** components $E_z$ and $H_z$. For TE these become functions
   of $H_z$ only; for TM, of $E_z$ only. ·WG p2
2. Solve the homogeneous wave equation for $E_z$ (TM) or $H_z$ (TE) inside the guide. ·WG p2
3. Use the expressions from step 1 to find $E_x$, $E_y$, $H_x$, $H_y$. ·WG p3
4. Analyse the solution for the phase velocity and the other properties. ·WG p3

**[fig]** ·WG p3 — a rectangular guide drawn in oblique projection on a mesh, with axes: $y$ up,
$x$ pointing left, $z$ running away along the guide. This is the coordinate frame used throughout.

> The handout carries out **steps 1, 2 and 4**. Step 3 — writing out the four transverse components
> for a particular mode — is never done. Nothing examined so far needs it.

---

## § 3 · Phasor fields in the guide

·WG pp. 3–4

**[eq]** ·WG p3 · The general phasor fields:

$$\tilde{\mathbf{E}} = \mathbf{a}_x\tilde{E}_x + \mathbf{a}_y\tilde{E}_y + \mathbf{a}_z\tilde{E}_z \qquad(1a)$$

$$\tilde{\mathbf{H}} = \mathbf{a}_x\tilde{H}_x + \mathbf{a}_y\tilde{H}_y + \mathbf{a}_z\tilde{H}_z \qquad(1b)$$

**[def]** ·WG p3 · All six components may depend on $(x, y, z)$. A wave travelling in $+z$ is
expected to vary as $e^{-j\beta z}$, with $\beta$ still to be found. So each component is written

$$\tilde{E}_x(x,y,z) = e_x(x,y)\,e^{-j\beta z}$$

giving

$$\tilde{\mathbf{E}} = \left(\mathbf{a}_x e_x + \mathbf{a}_y e_y + \mathbf{a}_z e_z\right)e^{-j\beta z} \qquad(2a)$$

$$\tilde{\mathbf{H}} = \left(\mathbf{a}_x h_x + \mathbf{a}_y h_y + \mathbf{a}_z h_z\right)e^{-j\beta z} \qquad(2b)$$

**[def]** ·WG p4 · Uppercase $\tilde{E}$, $\tilde{H}$ vary with $(x,y,z)$; lowercase $e$, $h$ vary
with $(x,y)$ only — the $z$-dependence has been pulled out.

> ⚠ **VERIFY (C40)** — ·WG p4 prints (2b) with $h_z e_z$ as its last term: the unit vector
> $\mathbf{a}_z$ has been replaced by the electric component $e_z$. ·WG p3's (2a) puts a tilde on
> the unit vector, $\tilde{a}_z$. Both are typesetting slips; the forms above are meant.

---

## § 4 · Maxwell's curl equations, component by component

·WG p4

**[def]** ·WG p4 · Inside the guide the medium is **lossless and source-free**: permittivity
$\varepsilon$, permeability $\mu$, and $\sigma = J = 0$. Maxwell's curl equations are

$$\nabla\times\tilde{\mathbf{E}} = -j\omega\mu\tilde{\mathbf{H}} \qquad(3a) \qquad\qquad \nabla\times\tilde{\mathbf{H}} = j\omega\varepsilon\tilde{\mathbf{E}} \qquad(3b)$$

**[derivation]** ·WG p4 · Substituting (2) into (3), and using the fact that

> **differentiating with respect to $z$ is the same as multiplying by $-j\beta$,**

gives six scalar equations — three from each curl:

$$\frac{\partial e_z}{\partial y} + j\beta e_y = -j\omega\mu\,h_x$$

$$-j\beta e_x - \frac{\partial e_z}{\partial x} = -j\omega\mu\,h_y$$

$$\frac{\partial e_y}{\partial x} - \frac{\partial e_x}{\partial y} = -j\omega\mu\,h_z$$

$$\frac{\partial h_z}{\partial y} + j\beta h_y = j\omega\varepsilon\,e_x$$

$$-j\beta h_x - \frac{\partial h_z}{\partial x} = j\omega\varepsilon\,e_y$$

$$\frac{\partial h_y}{\partial x} - \frac{\partial h_x}{\partial y} = j\omega\varepsilon\,e_z$$

> ⚠ **VERIFY (W1) — the fourth equation prints $e_y$ where $h_y$ belongs.** ·WG p4 reads
> $\dfrac{dh_z}{dy} + j\beta e_y = j\omega\varepsilon e_x$. It comes from the $x$-component of
> $\nabla\times\tilde{\mathbf{H}}$, which contains **only $H$ components** on the left — every term
> must be an $h$. Compare the first equation, its mirror from $\nabla\times\tilde{\mathbf{E}}$, which
> correctly has $e$ throughout.

> ⚠ **VERIFY (C41)** — every derivative on ·WG pp. 4–6 is printed as an ordinary $d/dx$, $d/dy$.
> They are **partial** derivatives; the fields depend on both $x$ and $y$. ·WG p6 mixes the two
> notations inside single equations.

---

## § 5 · Transverse fields in terms of $E_z$ and $H_z$

·WG p5

**[eq]** ·WG p5 · Solving the six equations algebraically for the four transverse components:

$$\tilde{E}_x = \frac{-j}{k_c^2}\left(\beta\,\frac{\partial E_z}{\partial x} + \omega\mu\,\frac{\partial H_z}{\partial y}\right)$$

$$\tilde{E}_y = \frac{j}{k_c^2}\left(-\beta\,\frac{\partial E_z}{\partial y} + \omega\mu\,\frac{\partial H_z}{\partial x}\right)$$

$$\tilde{H}_x = \frac{j}{k_c^2}\left(\omega\varepsilon\,\frac{\partial E_z}{\partial y} - \beta\,\frac{\partial H_z}{\partial x}\right)$$

$$\tilde{H}_y = \frac{-j}{k_c^2}\left(\omega\varepsilon\,\frac{\partial E_z}{\partial x} + \beta\,\frac{\partial H_z}{\partial y}\right)$$

**[added] Checked** by solving the four relevant equations of § 4 symbolically. $\tilde{E}_x$ and
$\tilde{H}_x$ agree with the handout as printed; the other two do not:

> ⚠ **VERIFY (W2) — $\tilde{E}_y$ has the wrong sign in front.** ·WG p5 prints
> $\tilde{E}_y = \dfrac{-j}{k_c^2}\left(-\beta\dfrac{dE_z}{dy} + \omega\mu\dfrac{dH_z}{dx}\right)$.
> The prefactor is $+j/k_c^2$. As printed, every $E_y$ the formula produces points the wrong way.

> ⚠ **VERIFY (W3) — $\tilde{H}_y$ differentiates $E_z$ in the wrong direction.** ·WG p5 prints
> $\omega\varepsilon\dfrac{dE_z}{dy}$ inside the $\tilde{H}_y$ bracket; it is
> $\omega\varepsilon\dfrac{\partial E_z}{\partial x}$. Check by symmetry: in each pair the $E_z$
> term of one component and the $H_z$ term of the *same* component differentiate in **different**
> directions. As printed, $\tilde{H}_y$ has both in $y$.

**[eq]** ·WG p5 · The **cut-off wave number** and the **unbounded-medium wave number**:

$$\boxed{k_c^2 = k^2 - \beta^2 = \omega^2\mu\varepsilon - \beta^2} \qquad\qquad \boxed{k = \omega\sqrt{\mu\varepsilon}}$$

> ⚠ **VERIFY (W4) — two errors in one line.** ·WG p5 prints $k_c = k^2 - \beta^2 = \omega\sqrt{\mu\varepsilon} - \beta^2$.
> - The left-hand side is missing its square: it is $k_c^{2}$. Units: $k^2 - \beta^2$ is m⁻², $k_c$ is m⁻¹.
> - The middle term is $k^2 = \omega^2\mu\varepsilon$, not $\omega\sqrt{\mu\varepsilon}$ — that is $k$
>   itself, printed on the very next line. As written the line subtracts a m⁻² quantity from a m⁻¹ one.
>
> Both are caught on sight by the dimensional check. The handout uses the correct
> $\beta = \sqrt{k^2 - k_c^2}$ on ·WG p8, so the error does not propagate.

**[def]** ·WG p5 · Once $E_z$ and $H_z$ are known, all four transverse components follow. For **TE**,
$E_z = 0$ and only $H_z$ is needed; for **TM**, $H_z = 0$ and only $E_z$ is needed.

> **[added] A consequence worth knowing — it answers revision Q1(b).** If both $E_z = 0$ **and**
> $H_z = 0$ (a TEM wave), every bracket above is zero, so all four transverse fields vanish — unless
> $k_c = 0$, where the formulas break down. A hollow guide forces $k_c \neq 0$ (§ 7). So the
> handout's own equations say a hollow guide carries **no** TEM field. See § 9, Q1(b).

---

## § 6 · TM modes: the wave equation for $E_z$

·WG pp. 5–6

**[derivation]** ·WG p5 · With $H_z = 0$, find $E_z$. From the homogeneous wave equation (WC1 § 1):

$$\nabla^2 E = \gamma^2 E = j\omega\mu(\sigma + j\omega\varepsilon)E$$

With $\sigma = 0$:

$$\nabla^2 E = \gamma^2 E = -\omega^2\mu\varepsilon E = -k^2 E$$

$$\boxed{\nabla^2 E + k^2 E = 0}\qquad(1)$$

This is the **Helmholtz equation**. Each component satisfies it separately, so for $E_z$: ·WG p6

$$\frac{\partial^2 E_z}{\partial x^2} + \frac{\partial^2 E_z}{\partial y^2} + \frac{\partial^2 E_z}{\partial z^2} + k^2 E_z = 0$$

Since $\partial^2/\partial z^2 \to (-j\beta)^2 = -\beta^2$:

$$\frac{\partial^2 E_z}{\partial x^2} + \frac{\partial^2 E_z}{\partial y^2} + \left(k^2 - \beta^2\right)E_z = 0$$

$$\boxed{\frac{\partial^2 e_z}{\partial x^2} + \frac{\partial^2 e_z}{\partial y^2} + k_c^2\,e_z = 0}$$

> ⚠ **VERIFY (W5) — the bracket prints $(\beta^2 + k^2)$.** ·WG p6 line 2. It must be
> $(k^2 - \beta^2)$: the $z$-derivative contributes $(-j\beta)^2 = -\beta^2$, and only the minus sign
> lets the next line call it $k_c^2$, which § 5 defines as $k^2 - \beta^2$.

> ⚠ **VERIFY (C42)** — ·WG p5 says "each of the components $a_x$, $a_y$ and $a_z$" must satisfy (1)
> independently; the components are $E_x$, $E_y$, $E_z$ — $\mathbf{a}$ is the unit vector. And ·WG p6
> writes $+k^2E$ and $+k_c^2E$ where it means $E_z$.

**[derivation]** ·WG p6 · **Separation of variables.** Try $e_z = X(x)\,Y(y)$:

$$\frac{\partial^2 (XY)}{\partial x^2} + \frac{\partial^2 (XY)}{\partial y^2} + k_c^2\,XY = 0$$

$$Y\frac{d^2X}{dx^2} + X\frac{d^2Y}{dy^2} + k_c^2\,XY = 0$$

Divide through by $XY$:

$$\frac{1}{X}\frac{d^2X}{dx^2} + \frac{1}{Y}\frac{d^2Y}{dy^2} + k_c^2 = 0$$

The first term depends on $x$ only and the second on $y$ only, so each must be a constant:

$$\frac{1}{X}\frac{d^2X}{dx^2} + k_x^2 = 0 \qquad\qquad \frac{1}{Y}\frac{d^2Y}{dy^2} + k_y^2 = 0 \qquad\qquad \boxed{k_c^2 = k_x^2 + k_y^2}$$

> ⚠ **VERIFY (W6) — ·WG p6 prints $Y\dfrac{d^2X}{dx^2} + Y\dfrac{d^2Y}{dy^2}$.** The second $Y$ must be
> $X$: differentiating $XY$ twice in $y$ leaves $X$ untouched. The next line (divided by $XY$) is
> correct, so the slip does not propagate — but a derivation copied from the page loses the mark.

---

## § 7 · Boundary conditions and the mode integers

·WG pp. 7–8

**[def]** ·WG p7 · $E_z$ is **tangential** to all four walls. The tangential electric field at a
perfect conductor is zero, so $E_z$ must vanish as $x \to 0$ and $x \to a$, and as $y \to 0$ and
$y \to b$.

**[fig]** ·WG p7 — the guide drawn with its corner at the origin: $x$ along the bottom edge to the
left, reaching $a$; $y$ up the near vertical edge, reaching $b$; $z$ running away along the guide.
A dashed line marks the hidden bottom-far edge.

**[derivation]** ·WG p7 · Sinusoidal solutions satisfy the two separated equations:

$$X(x) = A\cos k_x x + B\sin k_x x \qquad\qquad Y(y) = C\cos k_y y + D\sin k_y y$$

$$e_z = \left(A\cos k_x x + B\sin k_x x\right)\left(C\cos k_y y + D\sin k_y y\right)$$

The boundary conditions on $e_z$:

$$e_z = 0 \text{ at } x = 0 \text{ and } x = a \qquad\qquad e_z = 0 \text{ at } y = 0 \text{ and } y = b$$

- $e_z = 0$ at $x = 0$ forces $A = 0$.
- $e_z = 0$ at $y = 0$ forces $C = 0$.
- $e_z = 0$ at $x = a$ forces $\sin k_x a = 0$: ·WG p8

$$\boxed{k_x = \frac{m\pi}{a}}\qquad m = 1, 2, 3, \ldots$$

- $e_z = 0$ at $y = b$ forces $\sin k_y b = 0$:

$$\boxed{k_y = \frac{n\pi}{b}}\qquad n = 1, 2, 3, \ldots$$

> ⚠ **VERIFY (W7) ★ most serious in this document — $b$ replaced by $a$, four times.**
> - ·WG p7 prints the second boundary condition as "$e_z = 0$ at $y = 0$ and $y = a$". The text
>   directly above it, and the next page, both say $y = b$.
> - ·WG p8 prints $k_y = \dfrac{n\pi}{a}$ — and the error is then **carried into two results**: the
>   printed $\beta$ and the printed $\lambda_g$ both contain $(n\pi/a)^2$.
> - Yet the printed $f_c$ and $\lambda_c$ on the same page correctly use $(n\pi/b)^2$. The page
>   contradicts itself.
>
> **It changes answers.** On revision Q5 ($TE_{11}$, $7.22 \times 3.4$ cm, 8 GHz) the printed
> $\lambda_g$ formula gives **4.03 cm**; the correct one gives **4.73 cm**, which is the handout's own
> printed answer. *(Both re-computed.)* Use $b$ for everything in $y$.

**[def]** ·WG p8 · Each combination of $m$ and $n$ is a valid solution — a **mode**, written
$TM_{mn}$, each with its own field pattern inside the guide.

> ⚠ **VERIFY (C43)** — ·WG p8 writes the mode as $T_{mn}$; it is $TM_{mn}$.

**[added]** For **TM** modes neither $m$ nor $n$ can be zero — if either were, $\sin(0) = 0$ would make
$e_z$ vanish everywhere. That is why the handout starts both at 1, and why the lowest TM mode is
$TM_{11}$. For **TE** modes (not derived in the handout) one of $m$, $n$ *may* be zero, but not both.

**[added] What $m$ and $n$ mean physically.** $e_z \propto \sin(m\pi x/a)\sin(n\pi y/b)$, so $m$ is the
number of **half-wave variations of the field across the width $a$**, and $n$ the number across the
height $b$. This answers revision Q2(a).

---

## § 8 · The results — the formulas to memorise

·WG p8. Corrected forms; the flags say what the page prints.

**Phase constant** ·WG p8 ⚠ W7

$$\boxed{\beta = \sqrt{k^2 - k_c^2} = \sqrt{\omega^2\mu\varepsilon - \left(\frac{m\pi}{a}\right)^2 - \left(\frac{n\pi}{b}\right)^2}}$$

**Cut-off frequency** ·WG p8 ⚠ W8

$$\boxed{f_c = \frac{1}{2\pi\sqrt{\mu\varepsilon}}\sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2} = \frac{u}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}}$$

where $u = 1/\sqrt{\mu\varepsilon}$, the speed in the unbounded filling medium ($= c$ for air). The
second form is `[added]` — the same expression with $\pi$ cancelled.

**Cut-off wavelength** ·WG p8

$$\boxed{\lambda_c = \frac{2\pi}{\sqrt{\left(\dfrac{m\pi}{a}\right)^2 + \left(\dfrac{n\pi}{b}\right)^2}} = \frac{2}{\sqrt{\left(\dfrac{m}{a}\right)^2 + \left(\dfrac{n}{b}\right)^2}}}$$

**Phase velocity in the guide** ·WG p8

$$\boxed{V_p = \frac{\omega}{\beta} = \frac{c}{\sqrt{1 - \left(f_c/f\right)^2}}}$$

**Guide wavelength** ·WG p8 ⚠ W7

$$\lambda_g = \frac{2\pi}{\beta} = \frac{2\pi}{\sqrt{\omega^2\mu\varepsilon - \left(\dfrac{m\pi}{a}\right)^2 - \left(\dfrac{n\pi}{b}\right)^2}}$$

**Wave impedance, TE modes** ·WG p8

$$\boxed{Z_{TE} = \frac{\eta}{\sqrt{1 - \left(f_c/f\right)^2}}}$$

> ⚠ **VERIFY (W8) — $V_p$ means two different speeds on one page.** ·WG p8 writes
> $f_c = \dfrac{V_p}{2\pi}\sqrt{\cdots}$, where $V_p$ must be $1/\sqrt{\mu\varepsilon}$ — the speed in the
> unbounded medium, $c$ for air. Four lines later it defines $V_p = \omega/\beta$, the phase velocity
> **in the guide**, which is always **greater** than $c$. Substituting the guide's $V_p$ into the
> $f_c$ formula gives the wrong cut-off. **For $f_c$, use $c$ (air) or $u = 1/\sqrt{\mu\varepsilon}$.**

### The short forms — `[added]`, confirmed by the handout's own answers

·WG p9 says the short forms "discussed in class" will not be given in the exam. The handout prints
only two of them ($V_p$ and $Z_{TE}$). The rest follow from the long forms above in one line each.
**Every one reproduces the lecturer's printed answers to revision Q4 and Q5** (§ 9), which is the
evidence that these are the forms used in class.

Write $\;F = \sqrt{1 - \left(f_c/f\right)^2}\;$ — the factor that appears in all of them.

| Quantity | Short form | From |
|---|---|---|
| Cut-off wavelength, **dominant $TE_{10}$** | $\lambda_c = 2a$ | $\lambda_c$ with $m=1$, $n=0$ |
| Cut-off frequency, $TE_{10}$ | $f_c = \dfrac{c}{2a}$ | $f_c = c/\lambda_c$ |
| Phase constant | $\beta = \dfrac{2\pi}{\lambda}F$ | $\beta = \sqrt{k^2 - k_c^2} = k\sqrt{1 - (k_c/k)^2}$ and $k_c/k = f_c/f$ |
| Guide wavelength | $\lambda_g = \dfrac{\lambda}{F}$ | $\lambda_g = 2\pi/\beta$ |
| Phase velocity | $V_p = \dfrac{c}{F}$ | printed ·WG p8 |
| **Group velocity** | $V_g = c\,F$ | not in the handout at all; $V_g = d\omega/d\beta$ |
| Product rule | $V_p V_g = c^2$ | multiply the two rows above |
| TE wave impedance | $Z_{TE} = \dfrac{\eta}{F}$ | printed ·WG p8 |
| TM wave impedance | $Z_{TM} = \eta\,F$ | not in the handout |

Here $\lambda = c/f$ is the free-space wavelength, $\eta = 120\pi \approx 377\ \Omega$ for air.

**[added] Reading the factor $F$:**

- $f > f_c$: $F$ is real and between 0 and 1 → the mode **propagates**. $\lambda_g > \lambda$, $V_p > c$, $V_g < c$.
- $f = f_c$: $F = 0$ → $\beta = 0$, $V_g = 0$, $\lambda_g \to \infty$. Cut-off.
- $f < f_c$: $F$ is imaginary → $\beta$ is imaginary, $e^{-j\beta z}$ becomes a **real decaying
  exponential**. The mode does not propagate; it dies away. This is why a waveguide is a
  **high-pass filter** (revision Q1a).

**[added] The attenuation below cut-off** follows from the handout's own $\beta = \sqrt{k^2 - k_c^2}$
with $k < k_c$:

$$\beta = -j\alpha \qquad \alpha = \sqrt{k_c^2 - k^2} = \frac{2\pi}{c}\sqrt{f_c^2 - f^2}\quad(\text{Np/m})$$

so the field varies as $e^{-\alpha z}$. Needed for the 2024 exam Q1(e)(ii) — worked in § 9.

---

## § 9 · Revision questions, solved

·WG pp. 9–10. The handout prints answers in red for Q4 and Q5 but no working. **Every answer below has
been computed and checked against those printed answers.** All solutions are `[added]`.

### Q1 · Explain why — `[exercise]` ·WG p9

**(a) Waveguides are called high-pass filters.** `[added]`

- Every mode has a cut-off frequency $f_c$ fixed by the guide's size (§ 8).
- Above $f_c$, $\beta$ is real: the wave propagates.
- Below $f_c$, $\beta$ is imaginary: the field decays as $e^{-\alpha z}$ and nothing is carried.
- So the guide **passes frequencies above cut-off and blocks those below** — a high-pass filter.

**(b) TEM waves cannot propagate in waveguides.** `[added]` *(also 3 Oct 2024 CAT Q2a; 25 Oct 2024 exam Q4b, 2 marks)*

- A TEM wave has $E_z = 0$ **and** $H_z = 0$.
- By § 5, with both zero every transverse field is zero too — the guide carries nothing.
- Physically: magnetic field lines form closed loops in the cross-section. A loop of $H$ must
  enclose a current. With $E_z = 0$ there is no displacement current along $z$, and a hollow guide
  has **no inner conductor** to carry one.
- A TEM wave needs **two separate conductors** (like coax or two-wire line). A waveguide has one.

### Q2 · What is the — `[exercise]` ·WG p9

**(a) Meaning of $m$ and $n$** in $TE_{mn}$ and $TM_{mn}$. `[added]`

- $m$ = the number of half-wave variations of the field across the **broad dimension $a$** ($x$).
- $n$ = the number of half-wave variations across the **narrow dimension $b$** ($y$).

**(b) Dominant modes.** `[added]` The dominant mode is the one with the **lowest cut-off frequency**.

- **TM:** $TM_{11}$. Neither index can be zero (§ 7), so $m = n = 1$ is the lowest.
- **TE:** $TE_{10}$ (for $a > b$). One index may be zero; with $a$ the larger side, $m = 1$, $n = 0$
  gives the smallest $\sqrt{(m/a)^2 + (n/b)^2}$. Its cut-off is $f_c = c/2a$.
- $TE_{10}$ is the dominant mode of the guide overall, which is why "assuming the dominant mode"
  in Q4 means $TE_{10}$.

### Q3 · Sketch the $TE_{10}$ field patterns from X, Y and Z — `[exercise]` ·WG p9

*Identical to the 25 Oct 2024 exam Q4(d), same figure.*

**[fig]** ·WG p9 — the same open-ended box as the exam's Figure Q4: arrow **X** enters horizontally from
the left onto the near open end; arrow **Y** comes down vertically onto the top face; arrow **Z**
comes up from below-left onto the bottom-front. The end face is labelled $b$ (vertical edge) and $a$
(edge running into the page). A dashed line runs along the guide. No dimensions.

> **The labels are ambiguous on this drawing** — see the exam paper's `figure_data` block. $TE_{10}$
> is defined with $a$ as the **broad** wall. State that convention before sketching.

**[added] What to draw.** The $TE_{10}$ fields are not derived in the handout; these are the
standard patterns. For $TE_{10}$, $e_y \propto \sin(\pi x/a)$, $h_x \propto \sin(\pi x/a)$,
$h_z \propto \cos(\pi x/a)$.

- **Looking along the guide (into the open end):** $E$ lines run straight **vertically**, top wall to
  bottom wall. They are **densest in the middle** of the broad wall and **fade to zero** at the two
  side walls (half a sine wave across $a$). No variation from top to bottom. Horizontal $H$ lines
  ($H_x$) cross them, also strongest at mid-width.
- **Looking down on the broad (top) wall:** $H$ lines form **closed loops** lying in the horizontal
  plane, each loop half a guide wavelength long. Between loops, dots and crosses mark $E$ coming
  out of and going into the page, alternating every $\lambda_g/2$.
- **Looking at the narrow (side) wall:** $E$ lines vertical, bunched in bands that **alternate in
  direction every $\lambda_g/2$** along the guide. $H_x$ is in step with $E_y$, so its dots and
  crosses sit **on** the $E$ bands; between the bands the $H$ that shows is $H_z$, running along the
  guide in the plane of the page.

### Q4 · 4 GHz, 5 cm × 2.5 cm, dominant mode — `[exercise]` ·WG p9

*Identical to the 25 Oct 2024 exam Q4(c), 8 marks.* Printed answers in brackets.

Given: $f = 4\ \mathrm{GHz}$, $a = 5\ \mathrm{cm}$, $b = 2.5\ \mathrm{cm}$, air-filled, $TE_{10}$.

**(a) Cut-off wavelength** (printed: 10 cm)

$$\lambda_c = 2a = 2(5) = \mathbf{10\ cm}$$

**(b) Guide wavelength** (printed: 11.34 cm)

$$f_c = \frac{c}{\lambda_c} = \frac{3\times10^{8}}{0.10} = 3\ \mathrm{GHz}$$

$$F = \sqrt{1 - \left(\frac{3}{4}\right)^2} = \sqrt{1 - 0.5625} = \sqrt{0.4375} = 0.6614$$

$$\lambda = \frac{c}{f} = \frac{3\times10^{8}}{4\times10^{9}} = 7.5\ \mathrm{cm}$$

$$\lambda_g = \frac{\lambda}{F} = \frac{7.5}{0.6614} = \mathbf{11.34\ cm}$$

**(c) Group velocity** (printed: $1.984\times10^{8}$ m/s)

$$V_g = cF = (3\times10^{8})(0.6614) = \mathbf{1.984\times10^{8}\ m/s}$$

**(d) Phase velocity** (printed: $4.536\times10^{8}$ m/s)

$$V_p = \frac{c}{F} = \frac{3\times10^{8}}{0.6614} = \mathbf{4.536\times10^{8}\ m/s}$$

Check: $V_pV_g = (4.536\times10^{8})(1.984\times10^{8}) = 9.00\times10^{16} = c^2$ ✓

**(e) Characteristic impedance of the guide** (printed: 570 Ω)

$$Z_{TE} = \frac{\eta}{F} = \frac{377}{0.6614} = \mathbf{570\ \Omega}$$

**Verified** — all five match the printed answers to the figures shown.

### Q5 · 8 GHz, 7.22 cm × 3.4 cm, $TE_{11}$ — `[exercise]` ·WG pp. 9–10

Given: $f = 8\ \mathrm{GHz}$, $a = 7.22\ \mathrm{cm}$, $b = 3.4\ \mathrm{cm}$, air-filled, $m = n = 1$.

**(a) Cut-off wavelength** (printed: 6.152 cm)

$$\frac{1}{a} = \frac{1}{7.22} = 0.13850\ \mathrm{cm^{-1}} \qquad \frac{1}{b} = \frac{1}{3.4} = 0.29412\ \mathrm{cm^{-1}}$$

$$\lambda_c = \frac{2}{\sqrt{0.13850^2 + 0.29412^2}} = \frac{2}{\sqrt{0.019183 + 0.086505}} = \frac{2}{0.32510} = \mathbf{6.152\ cm}$$

**(b) Guide wavelength** (printed: 4.731 cm)

$$f_c = \frac{c}{\lambda_c} = \frac{3\times10^{8}}{0.06152} = 4.877\ \mathrm{GHz}$$

$$F = \sqrt{1 - \left(\frac{4.877}{8}\right)^2} = \sqrt{1 - 0.3716} = 0.7927$$

$$\lambda = \frac{c}{f} = 3.75\ \mathrm{cm} \qquad \lambda_g = \frac{\lambda}{F} = \frac{3.75}{0.7927} = \mathbf{4.730\ cm}$$

The handout's 4.731 is the same value to rounding (unrounded: 4.7304 cm).

**(c) Group velocity** (printed: $2.378\times10^{8}$ m/s)

$$V_g = cF = (3\times10^{8})(0.7927) = \mathbf{2.378\times10^{8}\ m/s}$$

**(d) Phase velocity** (printed: $3.785\times10^{8}$ m/s)

$$V_p = \frac{c}{F} = \frac{3\times10^{8}}{0.7927} = \mathbf{3.784\times10^{8}\ m/s}$$

> ⚠ **VERIFY (C45)** — the handout prints $3.785\times10^{8}$. Unrounded the value is
> $3.7843\times10^{8}$, which rounds to **3.784**. A last-digit slip only.

**(e) Characteristic impedance of the guide** (printed: 475.6 Ω)

$$Z_{TE} = \frac{\eta}{F} = \frac{377}{0.7927} = \mathbf{475.6\ \Omega}$$

**Verified** — all five match the printed answers, (b) and (d) to rounding.

> **The printed-formula trap, measured.** Q5 is the one question where W7 bites. Using the
> handout's printed $\lambda_g$ (with $n\pi/a$) gives $\lambda_g = 4.03$ cm — off by 15 %. The
> correct formula reproduces the handout's own answer. *(Both re-computed.)*

### Exam question not in the handout — 25 Oct 2024 exam Q1(e), 4 marks

> *A hollow rectangular waveguide has dimensions $a = 4$ cm, $b = 2$ cm. It propagates a signal of
> frequency 3 GHz. For the dominant mode, determine (i) cut-off frequency (ii) amount of attenuation.*

**[added] Solution.** Dominant mode $TE_{10}$.

**(i)**

$$f_c = \frac{c}{2a} = \frac{3\times10^{8}}{2(0.04)} = \mathbf{3.75\ GHz}$$

**(ii)** The signal (3 GHz) is **below** cut-off (3.75 GHz), so the mode does not propagate — it is
attenuated (§ 8, the attenuation below cut-off).

$$\alpha = \frac{2\pi}{c}\sqrt{f_c^2 - f^2} = \frac{2\pi}{3\times10^{8}}\sqrt{(3.75\times10^{9})^2 - (3\times10^{9})^2}$$

$$\alpha = \frac{2\pi}{3\times10^{8}}\,(2.25\times10^{9}) = \mathbf{47.1\ Np/m}$$

In decibels: $47.1 \times 8.686 = \mathbf{409\ dB/m}$, about 4.1 dB per centimetre.

**Verified** numerically. The handout does not state the below-cut-off case; this follows from its
$\beta = \sqrt{k^2 - k_c^2}$ with $k < k_c$. Flag that it is beyond the handout's printed scope.

---

## Verification summary — 21 flags

Full entries in `_verification-log.md` § W.

| Type | IDs | Count |
|---|---|---|
| Substantive | W1–W8 | 8 |
| Cosmetic | C36–C48 | 13 |

**The physics is sound; the transcription has the same faults as TL.** Three habits catch all eight
substantive flags:

1. **Dimensions** — W4 subtracts m⁻² from m⁻¹.
2. **Symmetry** — W3 and W1 break a pattern every other equation in the set keeps.
3. **Trace a symbol back to where it was set** — W7: $k_y$ comes from the wall at $y = b$, so it
   cannot contain $a$.

**W7 is the one that costs marks**: it changes $\beta$ and $\lambda_g$ for any mode with $n \neq 0$.
For the dominant $TE_{10}$ mode ($n = 0$) it is harmless — which is why revision Q4 comes out right
from the printed formulas and Q5 does not.

## Provenance notes

- All 10 pages rendered and read directly. Every figure is described above. **No page requires a
  screenshot.**
- ·WG p1 is two product photographs with no instructional content.
- The handout prints answers to its two numerical revision questions. **All ten printed answers were
  reproduced** — two to the last digit only (C45 and the 4.731 / 4.730 rounding in Q5b).
- **The TE derivation, group velocity, $Z_{TM}$ and attenuation below cut-off are not in the
  handout.** Every use of them above is tagged `[added]`. The group-velocity and short-form
  $\lambda_g$ answers are confirmed by the lecturer's own printed values.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
