---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld (Polarization handout explicitly signed)"
section: "06 — Polarization of Waves"
source_pages: "EMW p24–27, POL p1–4"
file_role: topic
subtopics:
  - "polarization = the time-varying behaviour of the E vector"
  - "the three types: linear, elliptical, circular"
  - "two transverse components with a relative phase (a, b)"
  - "linear polarization (equal phase): E stays on a line"
  - "circular polarization (equal amplitude, 90° phase, ±j): E traces a circle"
  - "elliptical polarization (unequal amplitude and/or general phase)"
  - "left- vs right-hand rotation"
  - "reconciling the two axis conventions (EMW z-propagation vs POL x-propagation)"
key_equations: [pol-general-field, pol-linear, pol-circular, pol-elliptical]
prerequisites: ["02-uniform-plane-wave (the two independent (Eₓ,H_y)/(E_y,Hₓ) pairs)"]
leads_to: []
verification_flags: 1
tags: [polarization, linear, circular, elliptical, phase-difference, left-hand, right-hand, complex-notation]
---

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · ·EMW/UPW/POL pN provenance ·
  ⚠ VERIFY = flagged suspected handout error (see _verification-log.md). -->

# 06 — Polarization of Waves

Scope: **polarization** describes how the tip of the E vector moves in time as the wave goes by. With two
transverse E-components and a relative phase between them, the tip traces a **line, an ellipse, or a circle** —
the three polarization types. Covered in two handouts (EMW p24–27 and the dedicated POL handout).

> **Convention note (important):** EMW propagates along **z** with transverse components **(Eₓ, E_y)**; POL
> propagates along **x** with transverse components **(E_y, E_z)**. Same physics, different axis labels. This file
> uses **EMW's z-propagation, (Eₓ, E_y)** convention and flags POL's where needed.

---

## 6.1 The idea and the three types ·POL p1, EMW p24

[def] **Polarization** = the time-varying behaviour of the **electric field** vector as the wave passes a point.
The three types: **linear, elliptical, circular**. ·POL p1

[def] Consider a plane wave (propagating along z) with **two transverse components**, $E_x$ and $E_y$, that may be
complex: ·EMW p24
$$\mathbf E = (E_x\mathbf a_x + E_y\mathbf a_y)e^{-j\beta z}, \qquad
  E_x = |E_x|e^{ja}, \quad E_y = |E_y|e^{jb}$$
- $a, b$ = the phase angles of the two components. **Their difference $(a-b)$ decides the polarization type.**
- If one component is zero, the wave is linearly polarized along the other axis. ·POL p1, EMW p26

---

## 6.2 Linear polarization — components in phase ·EMW p24–26, POL p1

[def] When $E_x$ and $E_y$ have the **same phase** ($a = b$), the real-time field is: ·EMW p25
$$\mathbf E = (E_x\mathbf a_x + E_y\mathbf a_y)\cos(\omega t - \beta z + a)$$

[eq: pol-linear] As the wave travels, the E vector keeps a **fixed direction** — an angle θ to the y-axis (or x-axis):
$$\boxed{\;\tan\theta = \frac{E_x}{E_y}\;}$$
- Only the **magnitude** oscillates (∝ cos); the **direction is constant**. Viewed head-on, the tip of E slides
  **up and down a straight line** — hence **linear polarization**. ·EMW p26, POL p1
- [fig ·EMW p26, POL p1] Two in-phase components add to a resultant vector on a fixed diagonal line.

---

## 6.3 Circular polarization — equal amplitude, 90° phase ·POL p3–4, EMW p27

[def] Take the two components with **equal amplitude** and a **90° (π/2) phase difference** — represented by a
factor **±j**. In complex form $\mathbf E_0 = (\mathbf a_y + j\mathbf a_z)E_a$ (POL's x-propagation labels), the
real-time components are: ·POL p3
$$E_y = E_a\cos\omega t, \qquad E_z = E_a\sin\omega t$$

[eq: pol-circular] Squaring and adding removes the time:
$$\boxed{\;E_y^2 + E_z^2 = E_a^2\;}$$
- The locus of the E tip is a **circle** of radius $E_a$ — **circular polarization**. ·POL p4
- $\mathbf E_0=(\mathbf a_y + j\mathbf a_z)E_a$ ⇒ **left** circular; $\mathbf E_0=(\mathbf a_y - j\mathbf a_z)E_a$
  ⇒ **right** circular. The two differ by the **sign of the ±j** (a 90° lead vs lag). ·POL p4

> ⚠ VERIFY ·POL p4 — the text says circular polarization requires "**180°** phase between the two components."
> The correct condition (and POL's own math above, a 90° offset between cos and sin) is a **90° (π/2)** phase
> difference — that is exactly the ±j. The "180°" refers only to the *difference between* the left-hand (+j) and
> right-hand (−j) cases; as a standalone statement it is misleading. **A 180° phase difference gives linear
> polarization, not circular.** See _verification-log.md.

---

## 6.4 Elliptical polarization — the general case ·EMW p26–27, POL p4

[def] When the components have **different phase angles** (general $a, b$), or **unequal amplitudes**, E no longer
stays in one plane. Take the special case $a=0$, $b=\pi/2$: ·EMW p26
$$E_x = |E_x|\cos(\omega t-\beta z), \qquad E_y = -|E_y|\sin(\omega t-\beta z)$$

[eq: pol-elliptical] For unequal amplitudes $A_y, A_z$ with a 90° offset, eliminating time gives: ·POL p4
$$\boxed{\;\left(\frac{E_y}{A_y}\right)^2 + \left(\frac{E_z}{A_z}\right)^2 = 1\;}$$
- The locus is an **ellipse** traced once per cycle — **elliptical polarization**. ·EMW p27, POL p4
- **Circular** is the special case $A_y = A_z$ (equal amplitudes, 90° phase). **Linear** is the special case of
  zero phase difference. So elliptical is the general form; linear and circular are its limits. ·EMW p27

[def] **Left- vs right-hand** ·EMW p27: point the thumb along the propagation direction; if the E vector rotates
the way the **right** hand's fingers curl, it is **right-hand** (elliptical/circular) polarization; if it matches
the **left** hand, **left-hand**. (Equivalently, specified clockwise/counter-clockwise with the wave coming
toward the observer.)

> ⚠ VERIFY ·EMW p27 — the elliptical real-time line is printed
> "$E(z,t) = E_x(z,t)\mathbf a_x + E_x(z,t)\mathbf a_y$"; the **second** component should be
> **$E_y(z,t)\mathbf a_y$**, not $E_x$. Typo. See _verification-log.md.

---

### Cross-references
- The two independent transverse pairs that make polarization possible → **02-uniform-plane-wave §2.2** (EMW's
  $(E_x,H_y)$ and $(E_y,H_x)$).

### Verification notes for this section
- 1 flag on physics wording: POL p4 "180°" for circular → should be **90°** (the ±j). Plus a typo: EMW p27
  Eₓ→E_y on the elliptical line. Both logged.
- Verified correct: linear (in-phase, tanθ=Eₓ/E_y), circular ($E_y^2+E_z^2=E_a^2$ from equal-amplitude 90°),
  elliptical $(E_y/A_y)^2+(E_z/A_z)^2=1$, and the linear/circular-as-limits-of-elliptical hierarchy.
- **Convention reconciliation** (not an error): POL uses x-propagation with (E_y,E_z); EMW uses z-propagation with
  (Eₓ,E_y). When teaching, pick one and state it — don't mix the two axis sets mid-problem.
