---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld"
section: "02 — The Uniform Plane Wave"
source_pages: "UPW p1–7, EMW p6–8"
file_role: topic
subtopics:
  - "definition of a plane wave / uniform plane wave"
  - "the free-space Maxwell equations and the TEM assumption"
  - "why the wave is Transverse Electromagnetic (E ⟂ H ⟂ direction of travel)"
  - "the coupled first-order E–H equations"
  - "the second-order wave equation and the speed of light 1/√(μ₀ε₀)"
  - "general travelling-wave solution f₁(z−v₀t)+f₂(z+v₀t)"
  - "relating E and H → intrinsic (characteristic) impedance η = √(μ/ε) = 377 Ω in free space"
key_equations: [tem-coupled, plane-wave-eqn, light-speed, general-solution, intrinsic-impedance, eta-freespace]
prerequisites: ["01-maxwell-wave-equations"]
leads_to: ["03-waves-in-media", "05-poynting-vector", "07-reflection-transmission"]
verification_flags: 0
tags: [plane-wave, uniform-plane-wave, TEM, transverse, intrinsic-impedance, eta, 377-ohm, speed-of-light, characteristic-impedance]
---

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · ·EMW/UPW/POL pN provenance ·
  ⚠ VERIFY = flagged suspected handout error (see _verification-log.md). -->

# 02 — The Uniform Plane Wave

Scope: specialises Topic 01 to the simplest wave — the uniform plane wave — in free space. Shows it is
transverse (TEM), that it travels at the speed of light, and that E and H are locked together by a fixed ratio,
the **intrinsic impedance** (377 Ω in free space). This ratio and the velocity are used everywhere afterwards.

---

## 2.1 What "plane wave" and "uniform" mean ·UPW p1

[def] A **plane wave** is a quantity whose value, at any instant, is **constant over any plane perpendicular to a
fixed direction** in space (the direction of propagation). ·UPW p1
[def] **Uniform** plane wave: the fields E and H are **constant in magnitude over that transverse plane** — they
vary only along the direction of travel.

[def] Assumptions used to get the free-space wave equations ·UPW p1:
1. no free charge in the field, $\rho_v = 0$;
2. the medium is **homogeneous and isotropic** (and here, lossless: σ=0).

The free-space Maxwell equations (from Topic 01) are:
$$\nabla\times\mathbf H = \varepsilon_0\frac{\partial\mathbf E}{\partial t},\quad
  \nabla\times\mathbf E = -\mu_0\frac{\partial\mathbf H}{\partial t},\quad
  \nabla\cdot\mathbf E = 0,\quad \nabla\cdot\mathbf H = 0$$

---

## 2.2 The wave is Transverse (TEM) ·UPW p2–3

[def] Assume a uniform plane wave with both **E and H lying in the transverse plane** — the plane whose normal is
the direction of propagation. ·UPW p2
[fig ·UPW p3] E points along **x** ($E_x$), H points along **y** ($H_y$), and the wave travels along **z**. The
three are mutually perpendicular. Because both fields lie in the transverse plane, the wave is called a
**Transverse Electromagnetic (TEM) wave** — there is **no field component along the direction of travel**. ·UPW p3

[derivation] Writing the curl in full and keeping only the surviving derivative (fields depend on z only): ·UPW p3–4
$$\nabla\times\mathbf H = -\frac{\partial H_y}{\partial z}\,\mathbf a_x = \varepsilon_0\frac{\partial E_x}{\partial t}\,\mathbf a_x
  \;\Rightarrow\; -\frac{\partial H_y}{\partial z} = \varepsilon_0\frac{\partial E_x}{\partial t}$$
and from Faraday's law:
$$\frac{\partial E_x}{\partial z} = -\mu_0\frac{\partial H_y}{\partial t}$$

[eq: tem-coupled] The two **coupled first-order equations** (UPW eqns 7 & 8): ·UPW p4
$$\boxed{\;\frac{\partial H_y}{\partial z} = -\varepsilon_0\frac{\partial E_x}{\partial t}, \qquad
  \frac{\partial E_x}{\partial z} = -\mu_0\frac{\partial H_y}{\partial t}\;}$$
- These are the field analogue of the **transmission-line equations** (a comparison the handout flags for later).
- $E_x$ changing along z is fed by $H_y$ changing in time, and vice-versa — the two fields regenerate each other.

> [fig cross-check ·EMW p7] EMW derives the same result more formally with a determinant form of Faraday's law
> and concludes $B_z = E_z = 0$ (no z-components) and that the fields split into **two independent (uncoupled)
> pairs** $(E_x,H_y)$ and $(E_y,H_x)$. We follow one pair, $(E_x,H_y)$; the other behaves identically. This is
> the fact that makes **polarization** (Topic 06) possible — both pairs can be present at once.

---

## 2.3 The wave equation and the speed of light ·UPW p4–5

[derivation] Differentiate one coupled equation by z and the other by t, then eliminate $H_y$: ·UPW p5
$$\boxed{\;\frac{\partial^2 E_x}{\partial z^2} = \varepsilon_0\mu_0\frac{\partial^2 E_x}{\partial t^2}\;}\qquad\text{[eq: plane-wave-eqn]}$$
This is the standard 1-D wave equation; comparing with $\partial^2\!/\partial z^2 = (1/v^2)\,\partial^2\!/\partial t^2$
identifies the propagation speed:

[eq: light-speed]
$$\boxed{\;v = \frac{1}{\sqrt{\varepsilon_0\mu_0}} = 3\times10^{8}\ \text{m/s}\;}$$
— i.e. **the speed of light**. (An identical equation holds for $H_y$.) This is the headline result: Maxwell's
equations predict that EM disturbances travel at $c$.

---

## 2.4 General travelling-wave solution ·UPW p5–6

[eq: general-solution] The general solution of the travelling-wave equation is:
$$E_x = f_1(z - v_0 t) + f_2(z + v_0 t), \qquad v_0 = \frac{1}{\sqrt{\varepsilon_0\mu_0}}$$
- $f_1(z-v_0t)$ = a wave travelling in the **+z** direction (forward);
- $f_2(z+v_0t)$ = a wave travelling in the **−z** direction (a **reflected** wave).
- The actual shapes of $f_1,f_2$ depend on the disturbance that launched the wave. ·UPW p6

---

## 2.5 Relating E and H → intrinsic impedance ·UPW p6–7, EMW p8

[derivation] Take the forward wave only ($f_2=0$), substitute $E_x=f_1(z-v_0t)$ into
$\partial E_x/\partial z = -\mu_0\,\partial H_y/\partial t$, and integrate. The constant of integration is a
static field, not part of the wave, so it is dropped. The result is a **fixed ratio** between E and H: ·UPW p6–7

[eq: intrinsic-impedance]
$$\boxed{\;\frac{E_x}{H_y} = \mu\,v_0 = \frac{\mu}{\sqrt{\mu\varepsilon}} = \sqrt{\frac{\mu}{\varepsilon}} = \eta\;}$$
- $\eta$ = **intrinsic (characteristic) impedance** of the medium (Ω), because E is in V/m and H in A/m so E/H
  has units of ohms. For a travelling plane wave this ratio is **definite and constant**. ·UPW p7

[eq: eta-freespace] **Free space** ($\mu_0=4\pi\times10^{-7}$ H/m, $\varepsilon_0=\tfrac{10^{-9}}{36\pi}$ F/m): ·UPW p7
$$\boxed{\;\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = 120\pi \approx 377\ \Omega\;}$$
- Remember this number: **377 Ω (=120π)** is the impedance of free space. E and H in a free-space plane wave
  always satisfy $E = 377\,H$.

---

### Cross-references
- η and v generalise to lossy/conducting media (η becomes complex) → **03-waves-in-media**.
- The E/H ratio sets the power carried by the wave, $P_{av}=\tfrac12 E_0^2/\eta$ → **05-poynting-vector**.
- η mismatch at a boundary drives reflection and transmission → **07-reflection-transmission**.
- The two independent $(E_x,H_y)$ / $(E_y,H_x)$ pairs underlie → **06-polarization**.

### Verification notes for this section
- 0 flags. Verified correct: TEM structure, $v=1/\sqrt{\mu_0\varepsilon_0}=3\times10^8$ m/s,
  $\eta_0=\sqrt{\mu_0/\varepsilon_0}=120\pi\approx377\ \Omega$.
- Minor label slip noted inline: UPW p3 heading says "Writing ∇×E in full form" above what is actually the
  **∇×H** expansion — content is correct, only the heading names the wrong operator.
