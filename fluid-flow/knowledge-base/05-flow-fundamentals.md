---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "05 — Fundamentals of Flow"
slides: "166-214"
file_role: topic
subtopics:
  - "streamline, streakline, pathline, stream tube"
  - "steady flow; relative vs absolute streamlines"
  - "flow dimensionality (3-D, 2-D, 1-D)"
  - "laminar vs turbulent flow; Reynolds' experiment; Reynolds number; critical Re"
  - "rotation, deformation, vorticity; rotational (forced) vs irrotational (free) vortex"
  - "circulation; Stokes' theorem"
  - "continuity equation (conservation of mass); mass & volume flow rate"
key_equations: [streamline-eq, reynolds-number, vorticity, circulation, stokes, continuity]
prerequisites: ["03-fluid-properties (viscosity)"]
leads_to: ["06-energy-bernoulli", "07-momentum", "08-viscous-flow", "11-drag-and-lift"]
verification_flags: 0
tags: [streamline, pathline, streakline, steady-flow, reynolds, laminar, turbulent, vorticity, vortex, circulation, continuity, mass-flow]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTATION: deck sometimes writes "u" for kinematic viscosity (clashes with velocity u). This KB uses ν for
  kinematic viscosity throughout. -->

# 05 — Fundamentals of Flow

The kinematic vocabulary and the mass-conservation law that the later dynamics (energy, momentum, viscous flow)
build on. Central results: the Reynolds number as the laminar/turbulent discriminator, vorticity/circulation,
and the continuity equation.

## 5.1 Streamline, streakline, pathline, stream tube ·slides 168–174
- [def] **Streamline** — a curve whose tangent at every point gives the fluid velocity direction at a chosen
  instant; velocity has no normal component, so **no flow crosses a streamline**. ·slide 168
- [eq: streamline-eq] 2-D streamline equation (velocity components u, v): ·slide 169
  $$\frac{dx}{u} = \frac{dy}{v}$$
  Streamlines around a body depend on the observer–body relative motion (**relative** vs **absolute**
  streamlines: move both cylinder+camera vs move only the cylinder). ·slides 169–171
- [def] **Streakline** — the line of all particles that have passed a fixed point in turn. **Pathline** — the
  trajectory of one particular particle. ·slide 172
- [def] In **steady flow** streamline, streakline and pathline **coincide**. Drawing the streamlines through all
  points of a closed curve forms a **stream tube**; no fluid crosses its wall, so it behaves like a solid tube. ·slides 173–174

## 5.2 Steady flow & dimensionality ·slides 175–178
- [def] **Steady flow:** velocity, pressure, density, etc. at any position do not change with time. ·slide 175
- [def] **3-D** (general): $u,v,w = f(x,y,z,t)$. **2-D**: flow identical on all planes parallel to a cut plane,
  $u,v = f(x,y,t)$ (e.g. between parallel plates). **1-D**: one velocity component, mean-velocity tube flow,
  $u = u(x,t)$ — easiest to handle. ·slides 176–178

## 5.3 Laminar vs turbulent flow — Reynolds ·slides 179–189
- [hist] **Osborne Reynolds' experiment:** dye injected at a glass-tube entrance; at low speed it runs as an
  unmixed thread (**laminar**); above a **critical velocity** it suddenly mixes/disperses (**turbulent**). ·slides 179–184
- [eq: reynolds-number] Transition is governed by a single dimensionless group regardless of individual v, d, ρ, μ: ·slide 185
  $$\boxed{\,Re = \frac{\rho v d}{\mu} = \frac{v d}{\nu}\,}$$
  Critical value $Re_c = v_c d/\nu$ at the critical velocity.
- [def] **Lower critical Reynolds number** — Re below which flow stays laminar however agitated the inlet:
  **≈ 2320** (Schiller). **Upper critical Re** (very calm inlet water): **≈ 5×10⁴** (Ekman). ·slides 186–187
- [ex ·slide 188] Water, d=3 cm, v=2 m/s, ν=1×10⁻⁶ m²/s: $Re = (2)(0.03)/10^{-6} = 6\times10^{4}$ ⇒ **turbulent**
  (≫ 2320). *(answer computed; slide poses the question.)*
- [ex ·slide 189] SAE 10W oil (ρ=870, μ=0.104 kg/m·s), Q=1.1 m³/h, d=2 cm, L=12 m; use
  $Q = \dfrac{\pi R^4 \Delta P}{8\mu L}$ (Hagen–Poiseuille) and Power $= Q\,\Delta P$. Find v, Re, ΔP, power.
  *(Setup slide; the deck does not show the solution. Computed: v≈0.97 m/s, Re≈163 (laminar), ΔP≈97 kPa,
  Power≈30 W. Computed here, not on a slide. Full Hagen–Poiseuille theory in 08-viscous-flow / 09-pipe-flow.)*

## 5.4 Compressible vs incompressible (revision) ·slide 190
Liquid ≈ incompressible (but consider compressibility for highly pressurized oil in hydraulic machines); gas ≈
compressible (but ignore compressibility for small pressure changes).

## 5.5 Rotation, deformation & vorticity ·slides 191–198
- [derivation] An elementary fluid rectangle ABCD (sides dx, dy) translates, deforms and rotates over time dt.
  Edge angular velocities $\omega_1 = \partial v/\partial x$ (edge AB) and $\omega_2 = -\partial u/\partial y$
  (edge AD). ·slides 191–194
- [eq: vorticity] Mean angular velocity and **vorticity** ζ about the z-axis: ·slide 195
  $$\omega = \tfrac{1}{2}(\omega_1+\omega_2) = \tfrac{1}{2}\Big(\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\Big),
  \qquad \zeta = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = 2\omega$$
  **Irrotational flow** ⟺ ζ = 0 (∂v/∂x = ∂u/∂y).
  *(Slide 195 prints the ω term once as "½(∂v/∂x − ∂v/∂y)"; the second term should be ∂u/∂y — a typo; the very
  next line writes ζ correctly.)*
- [def] **Rotational / forced vortex** — liquid spun with its vessel; each element both revolves *and* spins on
  itself. **Irrotational / free vortex** — liquid draining through a bottom hole; elements revolve but keep
  facing the same direction (no self-rotation). Natural vortices (hurricanes, drains) = **forced-vortex core +
  free-vortex periphery**. ·slides 196–198

## 5.6 Circulation & Stokes' theorem ·slides 199–207
- [def+eq: circulation] Around a closed curve s, with tangential velocity component $v_s'$: ·slides 200–201
  $$\Gamma = \oint_s v_s'\,ds = \oint_s v_s\cos\theta\,ds$$
- [derivation] For an elementary rectangle (area dA): $d\Gamma = \Big(\dfrac{\partial v}{\partial x} -
  \dfrac{\partial u}{\partial y}\Big)dx\,dy = \zeta\,dA$. ·slides 202–203
- [eq: stokes] Since ζ = 2ω, **circulation = surface integral of vorticity** (Stokes' theorem): ·slides 204–205
  $$\Gamma = \iint_A \zeta\,dA$$
  If there is no vorticity inside the curve, the circulation around it is zero. Used for pump/blower impeller
  flow and flow around aircraft wings.
- [ex ·slides 206–207] Cylinder d=1 m spinning at 500 rpm, fluid in contact: peripheral speed
  $= 500\,\pi\ \text{m/min} = 26.18$ m/s; $\Gamma = (\text{peripheral speed})\times(\pi d) = 2\pi R^2\omega
  \approx \boxed{82.2\ \text{m}^2/\text{s}}$. ✓

## 5.7 Continuity equation (conservation of mass) ·slides 208–214
- [def] Many 3-D flows are treated as **1-D** via mean velocity (e.g. tube flow). Three tools for 1-D flow:
  **continuity, energy, momentum** equations. ·slides 208–210
- [eq: continuity] Steady flow: mass per unit time through every section is constant (conservation of mass). For
  a pipe narrowing from section 1 to 2: ·slides 211–213
  $$\boxed{\,\rho_1 A_1 v_1 = \rho_2 A_2 v_2 \;\Rightarrow\; \rho A v = \text{const}\,}$$
  Incompressible (ρ const): $A v = \text{const}$.
- [def] **Mass flow rate** $\dot{m} = \rho A v$; **volumetric flow rate** $Q = A v$. Hence velocity ∝ 1/area
  (narrow section ⇒ faster flow). ·slide 214

### Cross-references
- Continuity is used with Bernoulli throughout **06-energy-bernoulli** and in every metering device.
- Vorticity/circulation return in **11-drag-and-lift** (lift = circulation, Kutta condition) and underlie the
  vortex behaviour in **08-viscous-flow** (Navier–Stokes vorticity transport).
- Reynolds number gates laminar/turbulent treatment in **08-viscous-flow** and **09-pipe-flow**.

### Verification notes for this section
- 0 substantive flags. Verified: Re=vd/ν and Re_c≈2320 (Schiller)/5×10⁴ (Ekman); vorticity ζ=2ω; Γ=∬ζdA;
  circulation example 82.2 m²/s; continuity ρAv=const.
- Minor slide typo noted inline (slide 195 ω term). Deck's "u" for kinematic viscosity standardized to ν here.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
