---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "08 — Flow of Viscous Fluid"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "289-375"
file_role: topic
subtopics:
  - "continuity equation (differential form, compressible & incompressible); testing a velocity field for continuity (slides 294–295)"
  - "Navier–Stokes equation (2-D derivation: body/pressure/viscous forces)"
  - "Navier–Stokes in cylindrical (axisymmetric) form (slides 309, 310, 314)"
  - "vorticity transport equation; Helmholtz; non-dimensional form (Re)"
  - "laminar flow between parallel plates (plane Poiseuille & Couette); worked pressure-drop example (slides 323–324)"
  - "laminar flow in circular pipes (Hagen–Poiseuille)"
  - "turbulent velocity distribution: Reynolds stress, eddy viscosity, Prandtl mixing length, log law, 1/7-power law"
  - "boundary layer: concept, thickness, wake, displacement & momentum thickness"
  - "boundary-layer equations (laminar & turbulent)"
  - "boundary-layer separation"
  - "lubrication theory (Reynolds bearing / slipper bearing): pressure distribution and load"
key_equations: [continuity-diff, navier-stokes, navier-stokes-cyl, vorticity-transport, plane-poiseuille, couette-poiseuille, hagen-poiseuille, reynolds-stress, eddy-viscosity, mixing-length, log-law, power-law-17, displacement-thickness, momentum-thickness, bl-equations, lubrication-pressure, lubrication]
prerequisites: ["03-fluid-properties (viscosity)", "05-flow-fundamentals (continuity, vorticity, Reynolds)"]
leads_to: ["09-pipe-flow (friction, Moody)", "11-drag-and-lift (boundary layer, separation, drag)"]
verification_flags: 12   # still printed or new in the Oct 2026 edition; 2 more are marked fixed in place
tags: [navier-stokes, continuity, vorticity, poiseuille, couette, hagen-poiseuille, turbulence, reynolds-stress, mixing-length, log-law, boundary-layer, separation, lubrication, bearing]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTE: many intermediate derivation lines in this section are algebra-heavy and were garbled in the raw text;
  the canonical/standard results are given here (all cross-checked). Deck sometimes writes "v" for kinematic
  viscosity ν and "u" for velocity in the same line — disambiguated here. -->

# 08 — Flow of Viscous Fluid

All real fluids are viscous; treating viscosity lets us capture pressure loss, drag, and separation (ignored in
the ideal-fluid treatment of 06). This section derives the governing equations (continuity + Navier–Stokes),
solves the two cases with analytical solutions (parallel plates, circular pipe), then treats turbulence,
boundary layers, separation, and lubrication.

## 8.1 Continuity equation (differential form) ·slides 291–296
- [derivation] Mass balance on an element dx·dy·b: (inflow − outflow) = rate of storage. ·slides 291–293
- [eq: continuity-diff] General (unsteady, compressible):
  $$\frac{\partial\rho}{\partial t} + \frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} = 0$$
  Steady ⇒ drop the time term. Incompressible (ρ const): $\dfrac{\partial u}{\partial x}+\dfrac{\partial v}{\partial y}=0$
  (holds for steady & unsteady). Axisymmetric (cylindrical):
  $\dfrac{\partial u}{\partial x}+\dfrac{1}{r}\dfrac{\partial(rv)}{\partial r}=0$ (also valid for ideal fluid). ·slides 293, 296
- [ex ·slides 294–295] *(new in the Oct 2026 edition)* Investigate whether each field satisfies continuity
  (incompressible, 2-D: $\partial u/\partial x + \partial v/\partial y = 0$).
  - (a) $u = -x$, $v = y$:
    $$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = -1 + 1 = 0 \;\Rightarrow\; \text{satisfies continuity}$$
  - (b) $u = 4x^2y^3$, $v = -2xy$:
    $$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 8xy^3 - 2x \neq 0 \;\Rightarrow\; \text{does not satisfy continuity}$$
  *(Checked: (b) vanishes only on the lines $x=0$ and $y=(1/4)^{1/3}$, not everywhere. The rendered slide drops
  the cube on $8xy^3$; the PDF text layer has it.)* Same test as the 2025 exam Q3(a) field (P36).

## 8.2 Navier–Stokes equation (2-D) ·slides 297–308
- [derivation] Newton's 2nd law on element dx·dy·b: $\rho\,b\,dx\,dy\,\dfrac{du}{dt}=F_x$ (and y). The material
  acceleration expands as $\dfrac{du}{dt}=\dfrac{\partial u}{\partial t}+u\dfrac{\partial u}{\partial x}+v\dfrac{\partial u}{\partial y}$
  (unsteady + convective terms). ·slides 298–299
- The total force splits into **body + pressure + viscous** ($F=F_B+F_P+F_S$): ·slides 300–307
  - body: $B_x=\rho X\,b\,dx\,dy$ (gravity: $X=0,\,Y=-g$);
  - pressure: $P_x=-\dfrac{\partial p}{\partial x}b\,dx\,dy$;
  - viscous (angular + elongation deformation, using $\tau=\mu\,\partial\gamma/\partial t$ and
    $\sigma_x=2\mu\,\partial u/\partial x$): combine to $\mu\nabla^2 u\cdot b\,dx\,dy$. ·slides 303–307
    *(The Oct 2026 edition writes these steps out in full — angular deformation $S_{x1}=\mu(\partial^2u/\partial y^2-\partial^2u/\partial x^2)\,b\,dx\,dy$
    on 303, elongation $S_{x2}=2\mu\,\partial^2u/\partial x^2\,b\,dx\,dy$ on 306, sum on 307 — and merges old
    slide 317, $\sigma_x = 2\tau = 2\mu\,\partial u/\partial x$, into 305.)*
  > ⚠ VERIFY S72 ·slide 306 — the tensile stress on the far face is labelled
  > "$\tau = \sigma_x + \frac{\partial\sigma_x}{\partial x}dx$". $\tau$ is the shear stress; this is the normal
  > stress $\sigma_x + (\partial\sigma_x/\partial x)\,dx$ (the Jul 2026 edition labelled it "dx", also wrong).
  > Cosmetic.
- [eq: navier-stokes] Result — the **Navier–Stokes equations** (2-D, incompressible): ·slide 308
  $$\boxed{\;\rho\Big(\underbrace{\tfrac{\partial u}{\partial t}}_{\text{unsteady}}+\underbrace{u\tfrac{\partial u}{\partial x}+v\tfrac{\partial u}{\partial y}}_{\text{convective (inertia)}}\Big)
  = \underbrace{\rho X}_{\text{body}} - \underbrace{\tfrac{\partial p}{\partial x}}_{\text{pressure}} + \underbrace{\mu\Big(\tfrac{\partial^2 u}{\partial x^2}+\tfrac{\partial^2 u}{\partial y^2}\Big)}_{\text{viscous}}\;}$$
  $$\rho\Big(\tfrac{\partial v}{\partial t}+u\tfrac{\partial v}{\partial x}+v\tfrac{\partial v}{\partial y}\Big)
  = \rho Y - \tfrac{\partial p}{\partial y} + \mu\Big(\tfrac{\partial^2 v}{\partial x^2}+\tfrac{\partial^2 v}{\partial y^2}\Big)$$
  > ⚠ VERIFY S22 ·slides 299 & 308 — the y-equation is printed with $u$ where $v$ is needed: on 308 the LHS
  > reads $\rho(\partial u/\partial t + u\,\partial u/\partial x + v\,\partial u/\partial y)$, and on 299
  > $dv/dt$ starts with $\partial u/\partial t$. The deck writes it correctly on 309. *(still printed in the
  > Oct 2026 edition)*

## 8.3 Navier–Stokes in cylindrical form; vorticity transport, Helmholtz, non-dimensional form ·slides 309–314
- [eq: navier-stokes-cyl] **Cylindrical (axisymmetric) form**, $x$ axial with velocity $u$, $r$ radial with
  velocity $v$, $R$ = r-direction component of the external (body) force. ·slides 309, 310, 314
  *[added]* standard form (the printed versions are flagged below):
  $$\rho\Big(\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial r}\Big)
  = \rho X - \frac{\partial p}{\partial x} + \mu\Big(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial r^2}+\frac{1}{r}\frac{\partial u}{\partial r}\Big)$$
  $$\rho\Big(\frac{\partial v}{\partial t}+u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial r}\Big)
  = \rho R - \frac{\partial p}{\partial r} + \mu\Big(\frac{\partial^2 v}{\partial x^2}+\frac{\partial^2 v}{\partial r^2}+\frac{1}{r}\frac{\partial v}{\partial r}-\frac{v}{r^2}\Big)$$
  Vorticity $\zeta = \partial v/\partial x - \partial u/\partial r$; shearing stress
  $\tau = -\mu(\partial u/\partial r + \partial v/\partial x)$ (the deck's sign convention). ·slide 309
  Slide 314 *(new page in the Oct 2026 edition)* holds only this pair of equations; slide 315 repeats it as
  the starting point for the parallel-plate and pipe solutions.
  > ⚠ VERIFY S70 ·slides 309, 310, 314 (and 327) — every printed version mixes Cartesian $y$ terms into the
  > cylindrical equations. 314 prints the x-equation with $v\,\partial u/\partial y$ and viscous term
  > $\mu(\partial^2u/\partial y^2 + \frac{1\,\partial^2u}{r\,\partial r^2})$, and the r-equation with
  > $\partial P/\partial y$ and "$-\frac{v}{r^2}\frac{\partial^2v}{\partial r^2}$" (a product, where it should be
  > $-\frac{v}{r^2} + \frac{\partial^2v}{\partial r^2}$). 310 has $\partial^2u/\partial y^2$ in place of
  > $\partial^2u/\partial x^2$ and $\partial P/\partial y$ in place of $\partial P/\partial r$. 309 has
  > $\partial^2u/\partial y^2$ and $\partial^2v/\partial r^2$ in the x-equation (should be $\partial^2u/\partial x^2$,
  > $\partial^2u/\partial r^2$) and $\partial^2v/\partial y^2$ in the r-equation. Check: the x-equation may
  > contain only $u$ and only the variables $x$, $r$; setting $u=u(r)$ must reduce it to slide 327's
  > $\partial p/\partial x = \mu(\partial^2u/\partial r^2 + \frac1r\partial u/\partial r)$. Use the [added] form above.
- [derivation] Eliminating body & pressure terms (cross-differentiate) gives the **vorticity transport equation**: ·slides 310–311
  $$\rho\Big(\frac{\partial\zeta}{\partial t}+u\frac{\partial\zeta}{\partial x}+v\frac{\partial\zeta}{\partial y}\Big)
  = \mu\Big(\frac{\partial^2\zeta}{\partial x^2}+\frac{\partial^2\zeta}{\partial y^2}\Big),\quad\text{i.e. } \frac{D\zeta}{Dt}=\nu\nabla^2\zeta$$
- [def] **Ideal flow** (inviscid, incompressible; μ=0) ⇒ RHS = 0 ⇒ vorticity is conserved = **Helmholtz's
  vortex theorem**. ·slide 311
- [eq: vorticity-transport] Non-dimensionalizing with length $l$, velocity $U$ ($Re=\rho Ul/\mu$): ·slides 311–312
  $$\frac{\partial\zeta^*}{\partial t^*}+u^*\frac{\partial\zeta^*}{\partial x^*}+v^*\frac{\partial\zeta^*}{\partial y^*}
  = \frac{1}{Re}\Big(\frac{\partial^2\zeta^*}{\partial x^{*2}}+\frac{\partial^2\zeta^*}{\partial y^{*2}}\Big)$$
  (change of vorticity by advection = diffusion of vorticity by viscosity; $1/Re$ = diffusion coefficient —
  smaller Re ⇒ stronger vorticity diffusion). ·slide 312
  > ⚠ VERIFY S19 ·slides 311, 312 — the Jul 2026 edition printed this equation with a leading $\rho$.
  > *(fixed in the Oct 2026 edition — no $\rho$ on either slide)*
  > ⚠ VERIFY S71 ·slide 311 — the new intermediate line reads
  > "$\ldots = \mu/Ul\rho\,(\partial^2\zeta/\partial x^2 + \partial^2\zeta/\partial y^2)$" with unstarred
  > $\zeta$, $x$, $y$; it should be $\frac{\mu}{\rho Ul}\big(\frac{\partial^2\zeta^*}{\partial x^{*2}}+\frac{\partial^2\zeta^*}{\partial y^{*2}}\big)$.
  > The next line is right. Cosmetic.

## 8.4 Laminar flow between parallel plates ·slides 313–324
- [derivation] With horizontal, steady, fully-developed, no-body-force assumptions the NS x-equation collapses to
  $\dfrac{\partial p}{\partial x} = \mu\dfrac{\partial^2 u}{\partial y^2}$ (·slides 317–318; the Oct 2026 edition
  applies each assumption to the equation in turn). The equivalent force balance
  $\partial p/\partial x = \partial\tau/\partial y$, $\tau=\mu\,\partial u/\partial y$ was on old slides 330–331 *(not in the Oct 2026
  edition — slide 318 keeps only "no change in momentum between the 2 faces")*. Double-integrate with $u=0$ at
  $y=0,h$: ·slide 319
  > ⚠ VERIFY S73 ·slide 317 — after "3. No body force ⇒ $\rho X = 0$" the line reads
  > $\rho(u\,\partial u/\partial x + v\,\partial u/\partial y) = \partial P/\partial x + \mu(\ldots)$ — the minus on
  > $\partial P/\partial x$ is lost (the line above has it, and slide 318 restores it). Cosmetic.
- [eq: plane-poiseuille] Plane Poiseuille (pressure-driven, gap h):
  $$u = -\frac{1}{2\mu}\frac{dp}{dx}(h-y)y \;\;(\text{parabola}),\quad
  u_{max}=-\frac{1}{8\mu}\frac{dp}{dx}h^2,\quad
  Q=-\frac{1}{12\mu}\frac{dp}{dx}h^3$$
  $$v_{mean}=\frac{Q}{h}=-\frac{1}{12\mu}\frac{dp}{dx}h^2=\tfrac{2}{3}u_{max},\qquad
  \tau=\mu\frac{du}{dy}=-\frac{1}{2}\frac{dp}{dx}(h-2y)$$
- [eq: couette-poiseuille] With $-dp/dx=\Delta P/l$ and the **upper plate moving** at $\pm U$ (Couette
  superposition): ·slide 322
  $$u = \frac{\Delta P}{2\mu l}(h-y)y \pm \frac{Uy}{h},\qquad Q=\frac{\Delta P}{12\mu l}h^3 \pm \frac{Uh}{2}$$
  (all flow rates here are **per unit width** of plate, m²/s.)
  > ⚠ VERIFY S74 ·slides 322, 324 (and 329–330) — slide 322 defines $-\dfrac{dP}{dx} = \dfrac{\Delta P}{l}$ (ΔP =
  > pressure drop) but the next line writes $Q = -\dfrac{1}{12}\dfrac{\Delta P}{\mu l}h^3$, i.e. it substitutes
  > $dP/dx = +\Delta P/l$. Correct: $Q = +\dfrac{\Delta P\,h^3}{12\mu l}$. The slip makes the pressure drop come
  > out **negative** in the example on 324 (ΔP = −11.11 Pa). The pipe slides do the same: 329 says "If P drop =
  > ΔP" then prints $\Delta P = -128Q\mu l/\pi d^4 = -32\mu lv/d^2$, and 330 uses the minus. A pressure drop is
  > positive; quote the magnitude and say which end is at higher pressure. *(322 and 329 carry this from the
  > Jul 2026 edition; 324 is new.)*
- [ex ·slides 323–324] Water passes between two parallel plates 60 mm apart and 2 m long at 600 L/min; take
  μ = 0.01 kg/m·s. Determine the change in pressure ΔP. *(The solution on 324 is new in the Oct 2026 edition.)*
  - Slide's working: $Q = -\dfrac{1}{12}\dfrac{\Delta P}{\mu l}h^3$; $0.6\ \text{m}^3/\text{min} \div 60 = 0.01\ \text{m}^3/\text{s}$;
    answer printed $\Delta P = -11.11$ Pa.
  - *[added]* Check, taking Q as per metre of plate width (the slide gives no width, and the formula is per
    unit width):
    $$\frac{h^3}{12\mu l} = \frac{0.06^3}{12(0.01)(2)} = 9.0\times10^{-4}\ \text{m}^3/(\text{Pa}\cdot\text{s})$$
    $$\Delta P = \frac{12\mu l\,Q}{h^3} = \frac{0.01}{9.0\times10^{-4}} = 11.1\ \text{Pa (drop)}$$
    *(Checked in Python.)* The magnitude 11.11 Pa is right; the minus comes from S74.
  > ⚠ VERIFY S75 ·slide 324 — the middle line prints "$0.01\ \text{m}^3/\text{sec} = -1.11\,\Delta P$". The
  > coefficient is $-h^3/(12\mu l) = -9.0\times10^{-4}$; with $-1.11$ the next line would give ΔP = −0.009 Pa,
  > not the printed −11.11 Pa. Cosmetic (the final number is consistent with the correct coefficient).

## 8.5 Laminar flow in a circular pipe — Hagen–Poiseuille ·slides 325–330
- [derivation] Axisymmetric NS reduces to $\dfrac{\partial p}{\partial x}=\mu\Big(\dfrac{\partial^2 u}{\partial r^2}+\dfrac1r\dfrac{\partial u}{\partial r}\Big)$;
  integrate with $u$ finite at $r=0$ and $u=0$ at $r=r_0$: ·slide 327
- [eq: hagen-poiseuille] Parabolic profile & flow rate:
  $$u = -\frac{1}{4\mu}\frac{dp}{dx}(r_0^2-r^2),\quad u_{max}=-\frac{r_0^2}{4\mu}\frac{dp}{dx},\quad
  Q=\int_0^{r_0}2\pi r\,u\,dr = -\frac{\pi r_0^4}{8\mu}\frac{dp}{dx}$$
  $$v_{mean}=\frac{Q}{\pi r_0^2}=-\frac{r_0^2}{8\mu}\frac{dp}{dx}=\tfrac12 u_{max},\qquad \tau=-\mu\frac{du}{dr}=-\tfrac12\frac{dp}{dx}r$$
  *[added]* intermediate: integrating gives $u = \dfrac{1}{4\mu}\dfrac{dp}{dx}r^2 + c_1\ln r + c_2$; finite $u$ at
  $r=0$ ⇒ $c_1=0$; $u(r_0)=0$ ⇒ the profile above. ·slides 327–328
  > ⚠ VERIFY S76 ·slides 327–328 — the signs of $u(r)$ disagree across the two slides. 327 now prints the
  > integrated form as $U = -\frac{1}{4\mu}\frac{dP}{dx}r^2 + c_1\log r + c_2$ (should be $+$; the Jul 2026
  > edition had $+$ here) and then the correct $U = -\frac{1}{4\mu}\frac{dP}{dx}(r_0^2-r^2)$; 328 heads the page
  > with $U = +\frac{1}{4\mu}\frac{dP}{dx}(r_0^2-r^2)$ (should be $-$; carried from the Jul 2026 edition). Check:
  > with $dP/dx<0$ the velocity must be positive, which needs the minus. 328's shear column is also garbled
  > ("$-\tfrac12\,dP/dr\cdot r$", then "$-\mu\cdot\frac{1}{4\mu}\frac{dP}{dx}r_0^2 = 2\cdot\tfrac14\frac{dP}{dx}r_0 = \tfrac12\frac{dP}{dx}r$");
  > use $\tau = -\tfrac12 (dp/dx)\,r$ as above. In 327, "log" is the natural log.
- [eq] **Hagen–Poiseuille law** (ΔP over length l, diameter d): ·slide 329
  $$\boxed{\,\Delta P = \frac{128\,Q\,\mu\,l}{\pi d^4} = \frac{32\,\mu\,l\,v}{d^2}\,}$$
  (viscosity can be measured from the pressure drop.) The slide prints both forms with a leading minus — see
  S74 above.
- [ex ·slide 330] μ=0.2 kg/m·s, d=9 cm, l=1.5 m, Q=800 L/min: $\Delta P = 128Q\mu l/(\pi d^4) \approx 2.5$ kPa
  (flow laminar, Re≈9×10² taking ρ = 1000 kg/m³). *[added] — the slide gives only the formula, printed as
  $\Delta P = -128Q\mu l/\pi d^4$; numbers computed and re-checked in Python: 2484 Pa, v = 2.10 m/s.*

## 8.6 Turbulent velocity distribution ·slides 331–344
- [def] Above $Re\approx2320$ pipe flow becomes turbulent: velocity = time-mean + fluctuation,
  $u=\bar u + u'$, $v=\bar v + v'$. ·slides 332–333
- [eq: reynolds-stress] Total shear = laminar + turbulent; the turbulent (**Reynolds**) stress: ·slides 334–336
  $$\tau = \tau_l + \tau_t,\qquad \tau_t = -\rho\,\overline{u'v'}$$
- [eq: eddy-viscosity] Writing the turbulent stress like a viscous one: ·slide 337
  $$\tau_t = \rho\,\nu_t\frac{d\bar u}{dy},\qquad \tau = \rho(\nu+\nu_t)\frac{d\bar u}{dy}$$
  $\nu_t$ = **turbulent kinematic viscosity** — not a fluid property; it fluctuates with the flow conditions.
  *(The Oct 2026 edition names $\nu_t$ explicitly; the deck types $\nu$ as "v" and $\nu_t$ as "v₁"/"vt".)*
- [eq: mixing-length] **Prandtl mixing-length** hypothesis ($|u'|\approx|v'|\approx l\,d\bar u/dy$): ·slides 337–339
  $$\tau_t = \rho\,l^2\Big(\frac{d\bar u}{dy}\Big)^2,\qquad l = 0.4\,y \text{ near the wall (κ=0.4)}$$
- [derivation] **Viscous sublayer** δ₀ near the wall (turbulence suppressed): $\tau_0=\mu\,du/dy$; define
  **friction velocity** $v^*=\sqrt{\tau_0/\rho}$, giving $u/v^*=yv^*/\nu$ in the sublayer. Matching to the
  mixing-length region (τ_t=τ_0) and integrating: ·slides 340–342
- [eq: log-law] **Logarithmic velocity distribution** (valid near the wall, any Re): ·slide 343
  $$\boxed{\,\frac{\bar u}{v^*} = 5.75\,\log\!\Big(\frac{v^* y}{\nu}\Big) + 5.5\,}$$
- [eq: power-law-17] **Kármán–Prandtl 1/n power law** (pipe, experimental): ·slide 344
  $$\frac{\bar u}{\bar u_{max}} = \Big(\frac{y}{r_0}\Big)^{1/n},\quad n=7 \text{ at } Re=10^5\ (\text{1/7-power law}),\quad n=3.45\,Re^{0.07}$$
  (mean/max velocity ratio ≈ 0.8–0.88 in turbulent pipe flow.)

## 8.7 Boundary layer — concept & thickness ·slides 345–356
- [def] **Boundary layer** (Prandtl): thin near-wall region where viscous friction controls the flow; outside it
  is the (effectively inviscid) **main flow**. At the wall the velocity is zero (no slip) and rises to ≈U across
  the layer. ·slides 346–348
- [def] **Wake**: the zone of reduced velocity behind a body, where vortices are cast off downstream. ·slide 349
- Practical example: the boundary layer over the ground can be about **1 m** thick, so the wind feels stronger
  standing on a beach than lying down — the nearer the ground, the lower the wind speed. ·slides 349–350
- [def] **Boundary-layer thickness δ** = distance from the wall where u reaches **99 %** of U. It thickens
  downstream (a few mm at an aircraft nose, up to ~50 cm at an airship tail). ·slides 350–351
- [eq: displacement-thickness / momentum-thickness] ·slide 352
  $$U\delta^* = \int_0^\infty (U-u)\,dy \quad(\text{displacement thickness}),\qquad
  \rho U^2\theta = \rho\int_0^\infty u(U-u)\,dy \quad(\text{momentum thickness})$$
  δ* = amount by which the body "appears larger" to the outer flow; θ relates to the viscous drag on the body
  (drag ≈ momentum deficit). ·slides 353–354
- [def] A laminar boundary layer on a flat plate transitions through a **transition zone** to a **turbulent
  boundary layer** downstream; profiles resemble the laminar/turbulent pipe profiles. ·slides 355–356

## 8.8 Boundary-layer equations ·slides 357–359
- [eq: bl-equations] In a laminar BL, $\partial^2u/\partial x^2 \ll \partial^2u/\partial y^2$ and the y-momentum
  reduces to $\partial p/\partial y = 0$; NS becomes **Prandtl's boundary-layer equations**: ·slide 358
  *(NOTE: this slide was **hidden** in the Jul 2026 edition (old slide 369); it is visible as slide 358 in the
  Oct 2026 edition, so it is now ordinary course content.)*
  $$\rho\Big(u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}\Big) = -\frac{\partial p}{\partial x}+\mu\frac{\partial^2 u}{\partial y^2},\qquad
  \frac{\partial p}{\partial y}=0,\qquad \frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}=0$$
- Turbulent BL (mean quantities): same form with $\tau=\mu\,\partial\bar u/\partial y - \rho\,\overline{u'v'}$. ·slide 359
  $$\rho\Big(\bar u\frac{\partial\bar u}{\partial x}+\bar v\frac{\partial\bar u}{\partial y}\Big) = -\frac{\partial\bar p}{\partial x}+\frac{\partial\tau}{\partial y},\qquad \frac{\partial\bar p}{\partial y}=0$$
  > ⚠ VERIFY S20 ·slide 359 — printed "$= -\partial\bar p/\partial x + \mu\,\delta\tau/\delta y$". τ already
  > contains μ, so the μ must go: $\partial\tau/\partial y$. *(still printed in the Oct 2026 edition)*

## 8.9 Separation of the boundary layer ·slides 360–362
- [def] **Favourable** gradient (pressure falling downstream, e.g. a contraction): flow accelerates, BL thins,
  stays attached. **Adverse** gradient (pressure rising, e.g. a divergence or curved wall): near-wall fluid has
  too little inertia to advance against the pressure; the wall velocity gradient falls to zero at the
  **separation point**, beyond which the flow reverses, sheds vortices, becomes turbulent, and loses energy. An
  expansion flow separates readily with large loss. ·slides 360–362

## 8.10 Lubrication theory (bearing) ·slides 363–369
- [def] Wedge-shaped oil film between a stationary inclined upper plane (length l, angle α) and a lower plane
  moving at U. Oil dragged into the narrowing wedge raises the internal pressure, lifting the upper plane so the
  surfaces never touch — the **principle of a (journal/slipper) bearing**; the thin film is dominated by
  viscosity ⇒ laminar. ·slides 363–365
- [derivation] Combining the plate-flow velocity profile with continuity ($Q$ constant), with local gap
  $h=h_1-\alpha x$: ·slides 366–368
  $$u = U\Big(1-\frac{y}{h}\Big) - \frac{dp}{dx}\frac{h^2}{2\mu}\frac{y}{h}\Big(1-\frac{y}{h}\Big),\qquad
  Q = \frac{Uh}{2} - \frac{h^3}{12\mu}\frac{dp}{dx}$$
  $$\frac{dp}{dx} = \frac{6\mu U}{(h_1-\alpha x)^2} - \frac{12\mu Q}{(h_1-\alpha x)^3},\qquad Q=\frac{h_1 h_2}{h_1+h_2}U$$
  ($\alpha = (h_1-h_2)/l$ in radians.) ·slides 367–368
- [eq: lubrication-pressure] Integrating, with $p=0$ at both ends of the pad: ·slide 368
  $$p = \frac{6\mu U}{\alpha(h_1-\alpha x)} - \frac{6\mu Q}{\alpha(h_1-\alpha x)^2} + c,\qquad c = -\frac{6\mu U}{\alpha(h_1+h_2)}$$
  *(New in the Oct 2026 edition — the Jul 2026 slide 379 printed a garbled single-line $p$. Checked here
  numerically: with $Q = h_1h_2U/(h_1+h_2)$ this gives $p(0) = p(l) = 0$.)*
- [eq: lubrication] Supporting load (per unit width) and its maximum at $h_1/h_2 = 2.2$: ·slide 369
  $$W = \int_0^l p\,dx = \frac{6\mu U l^2}{(h_1-h_2)^2}\Big[\ln\frac{h_1}{h_2} - \frac{2(h_1-h_2)}{h_1+h_2}\Big]$$
  $$P_{max} \approx 0.16\,\frac{\mu U l^2}{h_2^2}$$
  *[added] check: the bracketed load formula, maximised over $h_1/h_2$, peaks at $h_1/h_2 = 2.19$ with
  coefficient 0.160 (Python), matching the slide.*
  > ⚠ VERIFY S77 ·slide 369 — (i) the top line repeats the pressure as
  > "$\ldots - \frac{6\mu U}{\alpha(h_1+h_2)}\,x$": the constant $c$ has picked up a stray $x$ (with it, $p(l)\neq0$).
  > (ii) The load is printed "$\frac{6\mu Ul^2(h_1-h_2)}{(h_1-h_2)^2}[\log(\frac{h_1}{h_2}) - 2\frac{h_1-h_2}{h_1+h_2}]\,x$"
  > — an extra $(h_1-h_2)$ in the numerator (carried from the Jul 2026 edition) and another stray $x$. Without
  > them the formula integrates $p$ exactly and reproduces the slide's own $0.16\,\mu Ul^2/h_2^2$. "log" = ln.

## 8.11 Worked examples ·slides 370–375
- [ex ·slides 370–371] Air BL, sinusoidal profile, δ=7 mm, v_max=9 m/s, μ=1.81×10⁻⁵: shear at y=0/3.5/7 mm =
  **0.0366 / 0.0259 / ~1.0×10⁻⁴ Pa** (τ largest at the wall, ~0 at the edge).
  > ⚠ VERIFY ·slide 371 — the Jul 2026 edition wrote the profile as $v=v_{max}\cos(\pi y/2\delta)$, but its own
  > $dv/dy$ and the numbers correspond to $v=v_{max}\sin(\pi y/2\delta)$ (zero at wall, peak at edge, max shear at
  > wall). See _verification-log.md. *(fixed in the Oct 2026 edition — now reads $v=v_{max}\sin(\pi y/2\delta)$)*
  > ⚠ VERIFY S21 ·slide 371 — $dv/dy$ is given as "2020 m³/s"; a velocity gradient is s⁻¹. *(still printed in
  > the Oct 2026 edition — the cube does not draw in the rendered PDF but is in its text layer)*
  - *[added] check:* $\pi v_{max}/2\delta = \pi(9)/(0.014) = 2020\ \text{s}^{-1}$; $\mu\times2020 = 0.03655$ Pa;
    $\cos(224.4\times0.0035) = 0.707$ ⇒ 0.02585 Pa (slide 0.0259, using 224 rad/m); at $y=\delta$ the exact value is 0
    (slide's $1.02\times10^{-4}$ Pa comes from rounding 224.4 to 224).
- [ex ·slides 372–373] Shaft d=10 cm in a 10.03 cm sleeve, L=12 cm, μ=0.11 Pa·s, 100 rpm: surface speed 0.524
  m/s, clearance 0.15 mm, τ=384 N/m², F=14.5 N, **heat rate = F·v ≈ 7.58 W**. ✓
  > ⚠ VERIFY S78 ·slide 373 — the Oct 2026 edition prints the surface speed as "1.667 rps(π·0.10 m) = **0.5436**
  > m/s" (Jul 2026: 0.5236) and carries 0.5436 into the τ line, yet still gets τ = 384.0 N/m². Check:
  > $1.667\times\pi\times0.10 = 0.5236$ m/s, and $0.11\times0.5236/0.00015 = 384.0$ (0.5436 would give 398.6). The
  > energy line uses 0.5236. Typo; results unaffected.
- [ex ·slides 374–375] Plate 0.5 mm gap, U=0.50 m/s, τ=4.0 N/m²: $\mu = \tau/(U/h) = 4.0/(0.50/0.0005) =
  0.004\ \text{Pa·s} = 4.0$ mPa·s. ✓

### Cross-references
- Hagen–Poiseuille → laminar friction factor λ=64/Re in **09-pipe-flow**; the log/power laws → turbulent pipe
  friction (Blasius, Moody).
- Boundary layer, separation & momentum thickness → drag and the drag crisis in **11-drag-and-lift**.
- Uses viscosity/Newton's law (**03**) and vorticity/Reynolds number (**05**).

### Verification notes for this section
- 0 physics errors in the results. The Navier–Stokes, plane/pipe Poiseuille, Hagen–Poiseuille (ΔP=32μlv/d²),
  log law (5.75 log + 5.5), 1/7-power law, δ*/θ definitions, BL equations, and lubrication P_max all match
  standard references.
- Jul 2026 flags rechecked against the Oct 2026 edition: slide 371 sin/cos — fixed; S19 (311–312) — fixed;
  S20 (359), S21 (371), S22 (299, 308) — still printed. Slide 358 is no longer hidden.
- New in the Oct 2026 edition (or found on reworded slides): S70 cylindrical NS (309, 310, 314); S71 (311);
  S72 (306); S73 (317); S74 ΔP sign (322, 324, 329–330); S75 (324); S76 $u(r)$ signs (327–328); S77
  lubrication load line (369); S78 (373). The final results the course examines — Hagen–Poiseuille, plane
  Poiseuille, log law, BL equations, lubrication $P_{max}$ — are unaffected.
- Reading note: in the rendered PDF many superscripts (², ³) do not draw (e.g. 295, 324, 327–328, 338–341,
  371, 373); exponents were read from the PDF text layer.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
