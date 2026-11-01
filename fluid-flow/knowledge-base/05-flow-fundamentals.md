---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "05 — Fundamentals of Flow"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "157-204"
file_role: topic
subtopics:
  - "Lagrangian vs Eulerian description of a flow"
  - "streamline, streakline, pathline, stream tube"
  - "steady flow; relative vs absolute streamlines"
  - "flow dimensionality (3-D, 2-D, 1-D)"
  - "laminar vs turbulent flow; Reynolds' experiment; Reynolds number; critical Re"
  - "worked examples: Reynolds number of a water flow; laminar oil pipe (Hagen–Poiseuille pressure drop, pumping power); flow-type exercise"
  - "rotation, deformation, vorticity; rotational (forced) vs irrotational (free) vortex"
  - "circulation; Stokes' theorem"
  - "worked examples: circulation of a spinning cylinder; rotationality of given 2-D velocity fields"
  - "continuity equation (conservation of mass); mass & volume flow rate"
key_equations: [streamline-eq, reynolds-number, kinematic-viscosity, hagen-poiseuille-Q, pumping-power, vorticity, circulation, stokes, continuity]
prerequisites: ["03-fluid-properties (viscosity)"]
leads_to: ["06-energy-bernoulli", "07-momentum", "08-viscous-flow", "11-drag-and-lift"]
verification_flags: 6   # S47–S52 (Oct 2026 edition); the old slide-184 ω typo is fixed in this edition
tags: [streamline, pathline, streakline, lagrangian, eulerian, steady-flow, reynolds, laminar, turbulent, hagen-poiseuille, vorticity, vortex, circulation, continuity, mass-flow]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · [added] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTATION: deck sometimes writes "u" for kinematic viscosity (clashes with velocity u). This KB uses ν for
  kinematic viscosity throughout. The deck also writes δ for the partial-derivative sign ∂; this KB uses ∂. -->

# 05 — Fundamentals of Flow

The kinematic vocabulary and the mass-conservation law that the later dynamics (energy, momentum, viscous flow)
build on. Central results: the Reynolds number as the laminar/turbulent discriminator, vorticity/circulation,
and the continuity equation.

## 5.1 Describing a flow; streamline, streakline, pathline, stream tube ·slides 157–164
- [def] Two ways of describing a flow ·slide 158:
  - **Lagrangian** — follow one particle and record how its velocity and acceleration change.
  - **Eulerian** — record velocity $v$ and pressure $p$ at fixed positions $(x, y, z)$ as time $t$ passes.
  > ⚠ VERIFY S49 ·slide 158 — the slide spells these "Langrarian" and "Eularian" (also so in the Jul 2026
  > edition). Correct spellings: **Lagrangian**, **Eulerian**. Cosmetic.
- ·slide 159 — new in the Oct 2026 edition: a single web link to a video on relative streamlines. No other content.
- [def] **Streamline** — a curve whose tangent at every point gives the fluid velocity direction at a chosen
  instant; velocity has no normal component, so **no flow crosses a streamline**. ·slide 160
- [eq: streamline-eq] 2-D streamline equation (velocity components u, v): ·slide 161
  $$\frac{dx}{u} = \frac{dy}{v}$$
  Streamlines around a body depend on the observer–body relative motion (**relative** vs **absolute**
  streamlines: move both cylinder+camera vs move only the cylinder). ·slides 161–162
- [def] **Streakline** — the line of all particles that have passed a fixed point in turn. **Pathline** — the
  trajectory of one particular particle. ·slide 163
- [def] In **steady flow** streamline, streakline and pathline **coincide**. Drawing the streamlines through all
  points of a closed curve forms a **stream tube**; no fluid crosses its wall, so it behaves like a solid tube. ·slide 164

## 5.2 Steady flow & dimensionality ·slides 165–168
- [def] **Steady flow:** velocity, pressure, density, etc. at any position do not change with time. ·slide 165
- [def] **3-D** (general): $u,v,w = f(x,y,z,t)$. **2-D**: flow identical on all planes parallel to a cut plane,
  $u,v = f(x,y,t)$ (e.g. between parallel plates). **1-D**: one velocity component, mean-velocity tube flow,
  $u = u(x,t)$ — easiest to handle. ·slides 166–168

## 5.3 Laminar vs turbulent flow — Reynolds ·slides 169–179
- [hist] **Osborne Reynolds' experiment:** dye injected at a glass-tube entrance; at low speed it runs as an
  unmixed thread (**laminar**); above a **critical velocity** it suddenly mixes/disperses (**turbulent**). ·slides 169–171
  *(The Oct 2026 edition merges the Reynolds-experiment slides into 169–172; slide 170 adds a figure of a tap
  running laminar and turbulent.)*
- [eq: reynolds-number] Transition is governed by a single dimensionless group regardless of individual v, d, ρ, μ: ·slide 172
  $$\boxed{\,Re = \frac{\rho v d}{\mu} = \frac{v d}{\nu}\,}$$
  Critical value $Re_c = v_c d/\nu$ at the critical velocity.
- [eq: kinematic-viscosity] New in the Oct 2026 edition, slide 172 defines the kinematic viscosity on the page
  (written "u" there): ·slide 172
  $$\nu = \frac{\mu}{\rho}$$
  > ⚠ VERIFY S48 ·slides 172, 177, 178 (and 223–226, 233, 241–242, 248 in topic 06) — the PDF of the Oct 2026
  > edition **drops some glyphs when rendered**: $\mu$, $^2$ and $^3$ are missing from the printed page while the
  > text layer still holds them. Slide 172 shows "kinematic viscosity = /ρ" (μ missing); slide 177 shows
  > "(0.01m) π" for $(0.01\ \mathrm{m})^2\pi$ and "1.1 m /hr" for $1.1\ \mathrm{m^3/h}$. Read every blank gap
  > next to a unit or a radius as a missing $\mu$, $^2$ or $^3$. Cosmetic.
- [def] **Lower critical Reynolds number** — Re below which flow stays laminar however agitated the inlet:
  **≈ 2320** (Schiller). **Upper critical Re** (very calm inlet water): **≈ 5×10⁴** (Ekman). ·slide 173
- [ex ·slides 174–175] Water in a round tube, $d = 3\ \mathrm{cm}$, $v = 2\ \mathrm{m/s}$,
  $\nu = 1\times10^{-6}\ \mathrm{m^2/s}$. Laminar or turbulent? The Oct 2026 edition adds the solution (slide 175):
  $$Re = \frac{v d}{\nu} = \frac{(2)(0.03)}{1\times10^{-6}} = 60\,000$$
  The slide compares this with $50\,000$, the Ekman upper critical value: $60\,000 > 50\,000$ ⇒ **turbulent**.
  It is also far above the lower critical value 2320, so the answer is turbulent on either test.
- [ex ·slides 176–178] SAE 10W oil at 20 °C, $Q = 1.1\ \mathrm{m^3/h}$, horizontal pipe $d = 2\ \mathrm{cm}$,
  $L = 12\ \mathrm{m}$, $\rho = 870\ \mathrm{kg/m^3}$, $\mu = 0.104\ \mathrm{kg/(m\,s)}$. Find (a) average
  velocity, (b) Re, (c) pressure drop, (d) power. Given on the slide: ·slide 176
  $$[\text{eq: hagen-poiseuille-Q}]\quad Q = \frac{\pi R^{4}\,\Delta P}{8\mu L},
  \qquad [\text{eq: pumping-power}]\quad \text{Power} = Q\,\Delta P$$
  The Oct 2026 edition adds the solution (slides 177–178). Correct working, with $R = 0.01\ \mathrm{m}$ and
  $Q = 1.1/3600 = 3.056\times10^{-4}\ \mathrm{m^3/s}$:
  $$v = \frac{Q}{\pi R^{2}} = \frac{3.056\times10^{-4}}{\pi(0.01)^{2}} = 0.973\ \mathrm{m/s}$$
  $$Re = \frac{\rho v d}{\mu} = \frac{(870)(0.973)(0.02)}{0.104} = 163 \;<\; 2320 \;\Rightarrow\; \text{laminar}$$
  $$\Delta P = \frac{8\mu L Q}{\pi R^{4}} = \frac{(8)(0.104)(12)(3.056\times10^{-4})}{\pi(0.01)^{4}} = 97.1\ \mathrm{kPa}$$
  $$\text{Power} = Q\,\Delta P = (3.056\times10^{-4})(97\,105) = 29.67\ \mathrm{W}$$
  > ⚠ VERIFY S47 ·slide 177 — the slide divides by an extra length: it prints
  > "Average velocity = Q/A = 1.1 m³/hr ÷ [(0.01m)² π · 12 m · 3600 s/hr] = 0.08 m/s". Multiplying the area by
  > $L = 12\ \mathrm{m}$ gives m³, not m², so the result is not a velocity. Correct: $v = 0.973\ \mathrm{m/s}$
  > (0.08 is 0.973/12). Part (b) carries the error: the slide prints $Re = 13.8$ (its own numbers give 13.4);
  > correct $Re = 163$. The conclusion "laminar" survives, because 163 is still far below the critical value.
  > Parts (c) and (d) on slide 178 do not use $v$ and are **correct** (97.1 kPa, 29.67 W). The slide compares Re
  > with 2300 rather than the 2320 of slide 173 — immaterial here.
- [exercise ·slide 179] (1) Determine the type of flow in a 12-in pipe when (a) water at 60 °F,
  $\nu = 1.21\times10^{-5}\ \mathrm{ft^2/s}$, flows at $3.50\ \mathrm{ft/s}$; (b) heavy fuel oil at 60 °F,
  $\nu = 2.21\times10^{-3}\ \mathrm{ft^2/s}$, flows at the same velocity. (2) For laminar flow, what size pipe will
  deliver 90 gpm of medium fuel oil at 40 °F, $\nu = 6.55\times10^{-5}\ \mathrm{ft^2/s}$? *(The slide writes "u"
  for $\nu$.)*
  [added] Worked answer (not on the slides), with $d = 1\ \mathrm{ft}$:
  $$\text{(1a)}\quad Re = \frac{(3.50)(1)}{1.21\times10^{-5}} = 2.89\times10^{5} \;\Rightarrow\; \text{turbulent}$$
  $$\text{(1b)}\quad Re = \frac{(3.50)(1)}{2.21\times10^{-3}} = 1584 \;\Rightarrow\; \text{laminar}$$
  For (2), $Q = 90\ \mathrm{gal/min} \times 0.13368\ \mathrm{ft^3/gal} \div 60 = 0.2005\ \mathrm{ft^3/s}$ and
  $v = 4Q/(\pi d^{2})$, so
  $$Re = \frac{4Q}{\pi d\,\nu} \le Re_c \;\Rightarrow\; d \ge \frac{4Q}{\pi\,\nu\,Re_c}
  = \frac{4(0.2005)}{\pi(6.55\times10^{-5})(2320)} = 1.68\ \mathrm{ft}\ (20.2\ \mathrm{in})$$
  The pipe must be at least this large (a larger pipe lowers Re for a fixed $Q$). Many textbooks use
  $Re_c = 2000$, which gives $d \ge 1.95\ \mathrm{ft}$ (23.4 in) — state which critical value is used.

## 5.4 Compressible vs incompressible (revision) ·slide 180
Liquid ≈ incompressible (but consider compressibility for highly pressurized oil in hydraulic machines); gas ≈
compressible (but ignore compressibility for small pressure changes).

## 5.5 Rotation, deformation & vorticity ·slides 181–187
- [derivation] An elementary fluid rectangle ABCD (sides dx, dy) translates, deforms and rotates over time dt.
  Edge angular velocities $\omega_1 = \partial v/\partial x$ (edge AB) and $\omega_2 = -\partial u/\partial y$
  (edge AD). ·slides 181–183
- [eq: vorticity] Mean angular velocity and **vorticity** ζ about the z-axis: ·slide 184
  $$\omega = \tfrac{1}{2}(\omega_1+\omega_2) = \tfrac{1}{2}\Big(\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\Big),
  \qquad \zeta = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = 2\omega$$
  **Irrotational flow** ⟺ ζ = 0 (∂v/∂x = ∂u/∂y).
  *(The Jul 2026 edition printed the ω term once as "½(∂v/∂x − ∂v/∂y)". **Fixed in the Oct 2026 edition** —
  slide 184 now reads ½(δv/δx − δu/δy).)*
- [def] **Rotational / forced vortex** — liquid spun with its vessel; each element both revolves *and* spins on
  itself. **Irrotational / free vortex** — liquid draining through a bottom hole; elements revolve but keep
  facing the same direction (no self-rotation). Natural vortices (hurricanes, drains) = **forced-vortex core +
  free-vortex periphery**. ·slides 185–187

## 5.6 Circulation & Stokes' theorem ·slides 188–198
- [def+eq: circulation] Around a closed curve s, with tangential velocity component $v_s'$: ·slide 189
  $$\Gamma = \oint_s v_s'\,ds = \oint_s v_s\cos\theta\,ds$$
- [derivation] For an elementary rectangle (area dA): $d\Gamma = \Big(\dfrac{\partial v}{\partial x} -
  \dfrac{\partial u}{\partial y}\Big)dx\,dy = \zeta\,dA$. ·slides 190–191
- [eq: stokes] Since ζ = 2ω, **circulation = surface integral of vorticity** (Stokes' theorem): ·slides 191–192
  $$\Gamma = \iint_A \zeta\,dA$$
  If there is no vorticity inside the curve, the circulation around it is zero. Used for pump/blower impeller
  flow and flow around aircraft wings.
  > ⚠ VERIFY S50 ·slides 191–192 (and 194) — the slides write the surface integral with a closed-contour sign,
  > "Γ = ∮_A ζ dA"; the Oct 2026 edition puts this form in the title of slide 192. An integral over an area is
  > $\iint_A$; $\oint$ belongs to the line integral of slide 189. Also so in the Jul 2026 edition. Cosmetic.
- [ex ·slides 193–194] Cylinder $d = 1\ \mathrm{m}$ turning counterclockwise at 500 rpm, fluid in contact.
  The slide's working: ·slide 194
  $$\text{peripheral distance per minute} = 500\,\pi d = 500\pi(1) = 1570\ \mathrm{m/min}$$
  $$\Gamma = (1570\ \mathrm{m/min})(\pi d) = 4934\ \mathrm{m^2/min} \div 60 = 82.23\ \mathrm{m^2/s}$$
  Equivalently $\Gamma = (\text{peripheral speed})\times(\pi d) = 2\pi R^{2}\omega$, with peripheral speed
  $= 26.18\ \mathrm{m/s}$, giving $\boxed{\Gamma \approx 82.2\ \mathrm{m^2/s}}$ (unrounded 82.25; the slide's
  82.23 comes from rounding 4934). ✓
- [exercise ·slide 195] A cylindrical column of radius 5 cm is turned counterclockwise in fluid at 300 rpm.
  Obtain the circulation of the fluid in contact with the column.
  [added] Worked answer (not on the slides), same method as slide 194 with $d = 0.1\ \mathrm{m}$:
  $$v = \frac{\pi d N}{60} = \frac{\pi(0.1)(300)}{60} = 1.571\ \mathrm{m/s}$$
  $$\Gamma = v\,(\pi d) = (1.571)(\pi)(0.1) = \boxed{0.493\ \mathrm{m^2/s}}$$
- [ex ·slides 196–198] Two-dimensional velocity fields (k a constant): (a) $u = -ky,\ v = kx$;
  (b) $u = x^{2} - y^{2},\ v = -2xy$. Solution to (a), slide 197:
  $$\frac{\partial v}{\partial x} = k,\qquad \frac{\partial u}{\partial y} = -k,\qquad
  \zeta = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = k-(-k) = 2k \ne 0
  \;\Rightarrow\; \text{rotational}$$
  Part (b) is left as an exercise (slide 198).
  > ⚠ VERIFY S51 ·slides 196–197 — slide 196 asks to "obtain the **equation of the streamline**", but slide 197
  > answers a different question (is the flow rotational?) and labels the quantity it computes "Circulation".
  > What it computes is the vorticity ζ (units s⁻¹); circulation Γ has units m²/s. Learn the working as a
  > vorticity test. Cosmetic.

  [added] Answers to everything the slides set but do not solve (not on the slides):
  - (a) streamline, from $dx/u = dy/v$:
    $$\frac{dx}{-ky} = \frac{dy}{kx} \;\Rightarrow\; x\,dx + y\,dy = 0 \;\Rightarrow\; x^{2} + y^{2} = C$$
    Streamlines are circles about the origin — a rigid-body (forced-vortex) rotation, consistent with $\zeta = 2k$.
  - (b) vorticity:
    $$\frac{\partial v}{\partial x} = -2y,\qquad \frac{\partial u}{\partial y} = -2y,\qquad
    \zeta = -2y-(-2y) = 0 \;\Rightarrow\; \text{irrotational}$$
  - (b) streamline, from $dx/u = dy/v$:
    $$-2xy\,dx - (x^{2}-y^{2})\,dy = 0 \;\Rightarrow\; 3x^{2}y - y^{3} = C$$
    Check: the stream function $\psi = x^{2}y - y^{3}/3$ gives $u = \partial\psi/\partial y = x^{2}-y^{2}$ and
    $v = -\partial\psi/\partial x = -2xy$. Both fields also satisfy continuity,
    $\partial u/\partial x + \partial v/\partial y = 0$.

## 5.7 Continuity equation (conservation of mass) ·slides 199–204
- [def] Many 3-D flows are treated as **1-D** via mean velocity (e.g. tube flow). Three tools for 1-D flow:
  **continuity, energy, momentum** equations. ·slides 199–201
- [eq: continuity] Steady flow: mass per unit time through every section is constant (conservation of mass). For
  a pipe narrowing from section 1 to 2: ·slides 202–203
  $$\boxed{\,\rho_1 A_1 v_1 = \rho_2 A_2 v_2 \;\Rightarrow\; \rho A v = \text{const}\,}$$
  Incompressible (ρ const): $A v = \text{const}$.
  > ⚠ VERIFY S52 ·slide 203 — the text names the mean velocities "$u_1$ and $u_2$" while the equation on the same
  > slide uses $v_1$, $v_2$. Same quantity; read both as $v$. Cosmetic.
- [def] **Mass flow rate** $\dot{m} = \rho A v$; **volumetric flow rate** $Q = A v$. Hence velocity ∝ 1/area
  (narrow section ⇒ faster flow). ·slide 204

### Cross-references
- Continuity is used with Bernoulli throughout **06-energy-bernoulli** and in every metering device.
- Vorticity/circulation return in **11-drag-and-lift** (lift = circulation, Kutta condition) and underlie the
  vortex behaviour in **08-viscous-flow** (Navier–Stokes vorticity transport).
- Reynolds number gates laminar/turbulent treatment in **08-viscous-flow** and **09-pipe-flow**; the
  Hagen–Poiseuille formula given on slide 176 is derived in **08-viscous-flow**.

### Verification notes for this section
- Re-checked against the Oct 2026 edition (pages 157–204). Verified: Re=vd/ν and Re_c≈2320 (Schiller)/5×10⁴
  (Ekman); ν=μ/ρ; vorticity ζ=2ω; Γ=∬ζdA; circulation example 82.2 m²/s; continuity ρAv=const.
- Every number in the new worked examples recomputed: slide 175 (60 000) ✓; slide 178 (97.1 kPa, 29.67 W) ✓;
  slide 177 velocity and Re wrong (S47, substantive).
- Old slide-184 ω typo: **fixed** in the Oct 2026 edition.
- 6 flags open: S47 (substantive), S48–S52 (cosmetic). Deck's "u" for kinematic viscosity standardized to ν here.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
