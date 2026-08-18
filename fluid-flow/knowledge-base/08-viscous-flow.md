---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "08 — Flow of Viscous Fluid"
slides: "302-386"
file_role: topic
subtopics:
  - "continuity equation (differential form, compressible & incompressible)"
  - "Navier–Stokes equation (2-D derivation: body/pressure/viscous forces)"
  - "vorticity transport equation; Helmholtz; non-dimensional form (Re)"
  - "laminar flow between parallel plates (plane Poiseuille & Couette)"
  - "laminar flow in circular pipes (Hagen–Poiseuille)"
  - "turbulent velocity distribution: Reynolds stress, Prandtl mixing length, log law, 1/7-power law"
  - "boundary layer: concept, thickness, displacement & momentum thickness"
  - "boundary-layer equations (laminar & turbulent)"
  - "boundary-layer separation"
  - "lubrication theory (Reynolds bearing / slipper bearing)"
key_equations: [continuity-diff, navier-stokes, vorticity-transport, plane-poiseuille, couette-poiseuille, hagen-poiseuille, reynolds-stress, mixing-length, log-law, power-law-17, displacement-thickness, momentum-thickness, bl-equations, lubrication]
prerequisites: ["03-fluid-properties (viscosity)", "05-flow-fundamentals (continuity, vorticity, Reynolds)"]
leads_to: ["09-pipe-flow (friction, Moody)", "11-drag-and-lift (boundary layer, separation, drag)"]
verification_flags: 1
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

## 8.1 Continuity equation (differential form) ·slides 304–307
- [derivation] Mass balance on an element dx·dy·b: (inflow − outflow) = rate of storage. ·slides 304–306
- [eq: continuity-diff] General (unsteady, compressible):
  $$\frac{\partial\rho}{\partial t} + \frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} = 0$$
  Steady ⇒ drop the time term. Incompressible (ρ const): $\dfrac{\partial u}{\partial x}+\dfrac{\partial v}{\partial y}=0$
  (holds for steady & unsteady). Axisymmetric (cylindrical):
  $\dfrac{\partial u}{\partial x}+\dfrac{1}{r}\dfrac{\partial(rv)}{\partial r}=0$ (also valid for ideal fluid). ·slides 306–307

## 8.2 Navier–Stokes equation (2-D) ·slides 308–320
- [derivation] Newton's 2nd law on element dx·dy·b: $\rho\,b\,dx\,dy\,\dfrac{du}{dt}=F_x$ (and y). The material
  acceleration expands as $\dfrac{du}{dt}=\dfrac{\partial u}{\partial t}+u\dfrac{\partial u}{\partial x}+v\dfrac{\partial u}{\partial y}$
  (unsteady + convective terms). ·slides 309–310
- The total force splits into **body + pressure + viscous** ($F=F_B+F_P+F_S$): ·slides 311–319
  - body: $B_x=\rho X\,b\,dx\,dy$ (gravity: $X=0,\,Y=-g$);
  - pressure: $P_x=-\dfrac{\partial p}{\partial x}b\,dx\,dy$;
  - viscous (angular + elongation deformation, using $\tau=\mu\,\partial\gamma/\partial t$ and
    $\sigma_x=2\mu\,\partial u/\partial x$): combine to $\mu\nabla^2 u\cdot b\,dx\,dy$.
- [eq: navier-stokes] Result — the **Navier–Stokes equations** (2-D, incompressible): ·slide 320
  $$\boxed{\;\rho\Big(\underbrace{\tfrac{\partial u}{\partial t}}_{\text{unsteady}}+\underbrace{u\tfrac{\partial u}{\partial x}+v\tfrac{\partial u}{\partial y}}_{\text{convective (inertia)}}\Big)
  = \underbrace{\rho X}_{\text{body}} - \underbrace{\tfrac{\partial p}{\partial x}}_{\text{pressure}} + \underbrace{\mu\Big(\tfrac{\partial^2 u}{\partial x^2}+\tfrac{\partial^2 u}{\partial y^2}\Big)}_{\text{viscous}}\;}$$
  $$\rho\Big(\tfrac{\partial v}{\partial t}+u\tfrac{\partial v}{\partial x}+v\tfrac{\partial v}{\partial y}\Big)
  = \rho Y - \tfrac{\partial p}{\partial y} + \mu\Big(\tfrac{\partial^2 v}{\partial x^2}+\tfrac{\partial^2 v}{\partial y^2}\Big)$$

## 8.3 Vorticity transport, Helmholtz, non-dimensional form ·slides 321–324
- Cylindrical-coordinate NS form is also given (axisymmetric). Vorticity $\zeta = \partial v/\partial x - \partial u/\partial y$. ·slide 321
- [derivation] Eliminating body & pressure terms (cross-differentiate) gives the **vorticity transport equation**: ·slides 322–323
  $$\rho\Big(\frac{\partial\zeta}{\partial t}+u\frac{\partial\zeta}{\partial x}+v\frac{\partial\zeta}{\partial y}\Big)
  = \mu\Big(\frac{\partial^2\zeta}{\partial x^2}+\frac{\partial^2\zeta}{\partial y^2}\Big),\quad\text{i.e. } \frac{D\zeta}{Dt}=\nu\nabla^2\zeta$$
- [def] **Ideal flow** (μ=0) ⇒ RHS = 0 ⇒ vorticity is conserved = **Helmholtz's vortex theorem**. ·slide 323
- [eq: vorticity-transport] Non-dimensionalizing with length $l$, velocity $U$ ($Re=\rho Ul/\mu$): ·slides 323–324
  $$\frac{\partial\zeta^*}{\partial t^*}+u^*\frac{\partial\zeta^*}{\partial x^*}+v^*\frac{\partial\zeta^*}{\partial y^*}
  = \frac{1}{Re}\Big(\frac{\partial^2\zeta^*}{\partial x^{*2}}+\frac{\partial^2\zeta^*}{\partial y^{*2}}\Big)$$
  (change of vorticity by advection = diffusion of vorticity by viscosity; $1/Re$ = diffusion coefficient —
  smaller Re ⇒ stronger vorticity diffusion). ·slide 324

## 8.4 Laminar flow between parallel plates ·slides 325–335
- [derivation] With horizontal, steady, fully-developed, no-body-force assumptions the NS x-equation collapses to
  $\dfrac{\partial p}{\partial x} = \mu\dfrac{\partial^2 u}{\partial y^2}$ (a force balance $\partial p/\partial x =
  \partial\tau/\partial y$, $\tau=\mu\,\partial u/\partial y$). Double-integrate with $u=0$ at $y=0,h$: ·slides 328–331
- [eq: plane-poiseuille] Plane Poiseuille (pressure-driven, gap h):
  $$u = -\frac{1}{2\mu}\frac{dp}{dx}(h-y)y \;\;(\text{parabola}),\quad
  u_{max}=-\frac{1}{8\mu}\frac{dp}{dx}h^2,\quad
  Q=-\frac{1}{12\mu}\frac{dp}{dx}h^3$$
  $$v_{mean}=\frac{Q}{h}=-\frac{1}{12\mu}\frac{dp}{dx}h^2=\tfrac{2}{3}u_{max},\qquad
  \tau=\mu\frac{du}{dy}=-\frac{1}{2}\frac{dp}{dx}(h-2y)$$
- [eq: couette-poiseuille] With $-dp/dx=\Delta P/l$ and the **upper plate moving** at $\pm U$ (Couette
  superposition): ·slide 334
  $$u = \frac{\Delta P}{2\mu l}(h-y)y \pm \frac{Uy}{h},\qquad Q=\frac{\Delta P}{12\mu l}h^3 \pm \frac{Uh}{2}$$
- [exercise ·slide 335] Water between plates 60 mm apart, 2 m long, 600 L/min, μ=0.01 kg/m·s → find ΔP.

## 8.5 Laminar flow in a circular pipe — Hagen–Poiseuille ·slides 336–341
- [derivation] Axisymmetric NS reduces to $\dfrac{\partial p}{\partial x}=\mu\Big(\dfrac{\partial^2 u}{\partial r^2}+\dfrac1r\dfrac{\partial u}{\partial r}\Big)$;
  integrate with $u$ finite at $r=0$ and $u=0$ at $r=r_0$: ·slide 338
- [eq: hagen-poiseuille] Parabolic profile & flow rate:
  $$u = -\frac{1}{4\mu}\frac{dp}{dx}(r_0^2-r^2),\quad u_{max}=-\frac{r_0^2}{4\mu}\frac{dp}{dx},\quad
  Q=\int_0^{r_0}2\pi r\,u\,dr = -\frac{\pi r_0^4}{8\mu}\frac{dp}{dx}$$
  $$v_{mean}=\frac{Q}{\pi r_0^2}=-\frac{r_0^2}{8\mu}\frac{dp}{dx}=\tfrac12 u_{max},\qquad \tau=-\mu\frac{du}{dr}=-\tfrac12\frac{dp}{dx}r$$
- [eq] **Hagen–Poiseuille law** (ΔP over length l, diameter d): ·slide 340
  $$\boxed{\,\Delta P = \frac{128\,Q\,\mu\,l}{\pi d^4} = \frac{32\,\mu\,l\,v}{d^2}\,}$$
  (viscosity can be measured from the pressure drop.)
- [ex ·slide 341] μ=0.2 kg/m·s, d=9 cm, l=1.5 m, Q=800 L/min: $\Delta P = 128Q\mu l/(\pi d^4) \approx 2.5$ kPa
  (flow laminar, Re≈9×10²). *(computed.)*

## 8.6 Turbulent velocity distribution ·slides 342–355
- [def] Above $Re\approx2320$ pipe flow becomes turbulent: velocity = time-mean + fluctuation,
  $u=\bar u + u'$, $v=\bar v + v'$. ·slides 343–344
- [eq: reynolds-stress] Total shear = laminar + turbulent; the turbulent (**Reynolds**) stress: ·slides 345–347
  $$\tau = \tau_l + \tau_t,\qquad \tau_t = -\rho\,\overline{u'v'}$$
- [eq: mixing-length] **Prandtl mixing-length** hypothesis ($|u'|\approx|v'|\approx l\,d\bar u/dy$): ·slides 348–350
  $$\tau_t = \rho\,l^2\Big(\frac{d\bar u}{dy}\Big)^2,\qquad l = 0.4\,y \text{ near the wall (κ=0.4)}$$
- [derivation] **Viscous sublayer** δ₀ near the wall (turbulence suppressed): $\tau_0=\mu\,du/dy$; define
  **friction velocity** $v^*=\sqrt{\tau_0/\rho}$, giving $u/v^*=yv^*/\nu$ in the sublayer. Matching to the
  mixing-length region (τ_t=τ_0) and integrating: ·slides 351–353
- [eq: log-law] **Logarithmic velocity distribution** (valid near the wall, any Re): ·slide 354
  $$\boxed{\,\frac{\bar u}{v^*} = 5.75\,\log\!\Big(\frac{v^* y}{\nu}\Big) + 5.5\,}$$
- [eq: power-law-17] **Kármán–Prandtl 1/n power law** (pipe, experimental): ·slide 355
  $$\frac{\bar u}{\bar u_{max}} = \Big(\frac{y}{r_0}\Big)^{1/n},\quad n=7 \text{ at } Re=10^5\ (\text{1/7-power law}),\quad n=3.45\,Re^{0.07}$$
  (mean/max velocity ratio ≈ 0.8–0.88 in turbulent pipe flow.)

## 8.7 Boundary layer — concept & thickness ·slides 356–367
- [def] **Boundary layer** (Prandtl): thin near-wall region where viscous friction controls the flow; outside it
  is the (effectively inviscid) **main flow**. At the wall the velocity is zero (no slip) and rises to ≈U across
  the layer. ·slides 357–359
- [def] **Boundary-layer thickness δ** = distance from the wall where u reaches **99 %** of U. It thickens
  downstream (a few mm at an aircraft nose, up to ~50 cm at an airship tail). ·slides 361–362
- [eq: displacement-thickness / momentum-thickness] ·slide 363
  $$U\delta^* = \int_0^\infty (U-u)\,dy \quad(\text{displacement thickness}),\qquad
  \rho U^2\theta = \rho\int_0^\infty u(U-u)\,dy \quad(\text{momentum thickness})$$
  δ* = amount by which the body "appears larger" to the outer flow; θ relates to the viscous drag on the body
  (drag ≈ momentum deficit). ·slides 364–365
- [def] A laminar boundary layer on a flat plate transitions through a **transition zone** to a **turbulent
  boundary layer** downstream; profiles resemble the laminar/turbulent pipe profiles. ·slides 366–367

## 8.8 Boundary-layer equations ·slides 368–370
- [eq: bl-equations] In a laminar BL, $\partial^2u/\partial x^2 \ll \partial^2u/\partial y^2$ and the y-momentum
  reduces to $\partial p/\partial y = 0$; NS becomes **Prandtl's boundary-layer equations**: ·slide 369
  *(NOTE: slide 369 is **hidden** in the deck — included here for completeness.)*
  $$\rho\Big(u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}\Big) = -\frac{\partial p}{\partial x}+\mu\frac{\partial^2 u}{\partial y^2},\qquad
  \frac{\partial p}{\partial y}=0,\qquad \frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}=0$$
- Turbulent BL (mean quantities): same form with $\tau=\mu\,\partial\bar u/\partial y - \rho\,\overline{u'v'}$. ·slide 370

## 8.9 Separation of the boundary layer ·slides 371–373
- [def] **Favourable** gradient (pressure falling downstream, e.g. a contraction): flow accelerates, BL thins,
  stays attached. **Adverse** gradient (pressure rising, e.g. a divergence or curved wall): near-wall fluid has
  too little inertia to advance against the pressure; the wall velocity gradient falls to zero at the
  **separation point**, beyond which the flow reverses, sheds vortices, becomes turbulent, and loses energy. An
  expansion flow separates readily with large loss. ·slides 371–373

## 8.10 Lubrication theory (bearing) ·slides 374–380
- [def] Wedge-shaped oil film between a stationary inclined upper plane (length l, angle α) and a lower plane
  moving at U. Oil dragged into the narrowing wedge raises the internal pressure, lifting the upper plane so the
  surfaces never touch — the **principle of a (journal/slipper) bearing**; the thin film is dominated by
  viscosity ⇒ laminar. ·slides 374–376
- [derivation] Combining the plate-flow velocity profile with continuity ($Q$ constant), with local gap
  $h=h_1-\alpha x$: ·slides 377–379
  $$u = U\Big(1-\frac{y}{h}\Big) - \frac{dp}{dx}\frac{h^2}{2\mu}\frac{y}{h}\Big(1-\frac{y}{h}\Big),\qquad
  Q = \frac{Uh}{2} - \frac{h^3}{12\mu}\frac{dp}{dx}$$
  $$\frac{dp}{dx} = \frac{6\mu U}{(h_1-\alpha x)^2} - \frac{12\mu Q}{(h_1-\alpha x)^3},\qquad Q=\frac{h_1 h_2}{h_1+h_2}U$$
- [eq: lubrication] Integrated load capacity, maximum at $h_1/h_2 = 2.2$: ·slide 380
  $$P_{max} \approx 0.16\,\frac{\mu U l^2}{h_2^2}$$

## 8.11 Worked examples ·slides 381–386
- [ex ·slides 381–382] Air BL, sinusoidal profile, δ=7 mm, v_max=9 m/s, μ=1.81×10⁻⁵: shear at y=0/3.5/7 mm =
  **0.0366 / 0.0259 / ~1.0×10⁻⁴ Pa** (τ largest at the wall, ~0 at the edge).
  > ⚠ VERIFY ·slide 382 — slide writes the profile as $v=v_{max}\cos(\pi y/2\delta)$, but its own $dv/dy$ and the
  > numbers correspond to $v=v_{max}\sin(\pi y/2\delta)$ (zero at wall, peak at edge, max shear at wall). Read as
  > **sin**. See _verification-log.md.
- [ex ·slides 383–384] Shaft d=10 cm in a 10.03 cm sleeve, L=12 cm, μ=0.11 Pa·s, 100 rpm: surface speed 0.524
  m/s, clearance 0.15 mm, τ=384 N/m², F=14.5 N, **heat rate = F·v ≈ 7.58 W**. ✓
- [ex ·slides 385–386] Plate 0.5 mm gap, U=0.50 m/s, τ=4.0 N/m²: $\mu = \tau/(U/h) = 4.0/(0.50/0.0005) =
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
- 1 notation flag logged: slide 382 sin/cos. Many algebra-heavy intermediate slides were garbled in raw text;
  canonical results shown. Slide 369 is hidden in the deck (noted).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
