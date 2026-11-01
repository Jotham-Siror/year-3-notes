---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "11 — Drag and Lift (External Flows)"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "498-561"
file_role: topic
subtopics:
  - "flow around a body: boundary layer, stagnation point, wake, separation"
  - "drag & lift definitions; form (pressure) drag vs friction drag"
  - "drag coefficient; flat-plate friction drag"
  - "flow past a cylinder: ideal flow, d'Alembert's paradox, viscous regimes, Kármán vortex street, drag crisis"
  - "Strouhal number & vortex shedding"
  - "drag of a sphere; Stokes flow"
  - "friction torque on a revolving disc"
  - "lift: rotating cylinder (Magnus), Kutta–Joukowski theorem"
  - "wings/aerofoils: geometry, coefficients, stall, lift-drag polar, circulation theory"
  - "cascade; cavitation & cavitation number"
key_equations: [stagnation-pressure, drag-eq, flat-plate-friction, cylinder-ideal, dalembert, strouhal, sphere-stokes, disc-torque, kutta-joukowski, aspect-ratio, wing-coeffs, cavitation-number]
prerequisites: ["05-flow-fundamentals (circulation)", "08-viscous-flow (boundary layer, separation)"]
leads_to: []
verification_flags: 4   # old-slide-531 τ₀ (dropped with the slide) + slide 533 "0.31" still printed + new S84–S85 (Oct 2026 edition); slide 545 L→M, S30, S31 still printed
tags: [drag, lift, boundary-layer, separation, cylinder, dalembert, karman-vortex, strouhal, sphere, stokes, magnus, kutta-joukowski, aerofoil, wing, stall, cascade, cavitation]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md). -->

# 11 — Drag and Lift (External Flows)

Forces on a body immersed in a stream. Drag (along the flow) comes from pressure (form) drag + friction drag;
lift (normal to the flow) comes from circulation. Central results: the drag equation with an experimental $C_D$,
d'Alembert's paradox and its viscous resolution (separation, wakes, the Kármán street and the drag crisis), and
the Kutta–Joukowski lift theorem underpinning wings.

## 11.1 Flow around a body ·slides 498–502
- [def] **External flows** (a baseball or golf ball in flight, a vehicle, an aircraft, a submarine) as opposed to the
  **internal flows** of sections 09–10 (pipes, water courses). ·slide 498
- [def] A body in a uniform stream develops a **boundary layer**, a front **stagnation point** (velocity → 0),
  then **separation** and a **wake** of eddies behind. ·slides 499–500
- [eq: stagnation-pressure] $p_0 = p_\infty + \dfrac{\rho U^2}{2}$ (stagnation vs freestream). ·slide 501
- A flat plate aligned with the flow feels only downstream force; a wing feels a resultant $R$ inclined to the flow. ·slide 502

## 11.2 Drag & lift; form vs friction drag ·slides 502–505
- [def] Resultant $R$ resolves into **drag D** (along U) and **lift L** (normal to U). ·slide 502
- [eq] Pressure $p\,dA$ acts normal to the surface, friction $\tau\,dA$ tangential: ·slides 503–504
  $$D_p = \int_A p\,dA\cos\theta\ \text{(form / pressure drag)},\qquad D_f = \int_A \tau\,dA\sin\theta\ \text{(friction drag)}$$
  $$D = D_p + D_f\quad(\text{shape-dependent});\qquad L = \int(\text{components of } p\,dA,\ \tau\,dA \text{ normal to } U)$$

## 11.3 Drag coefficient & flat-plate friction ·slides 506–510 (and old slides 530–531, not in the Oct 2026 edition)
- [eq: drag-eq] Experimental drag law:
  $$\boxed{\,D = C_D\,A\,\frac{\rho U^2}{2}\,}$$
  A = projected (frontal) area; $C_D$ = drag coefficient (dimensionless). ·slide 506
- [eq: flat-plate-friction] *(not in the Oct 2026 edition)* Smooth flat plate, turbulent: $C_f = 0.074\,Re^{-1/5}$;
  with a laminar leading portion: $C_f = \dfrac{0.074}{Re^{1/5}} - \dfrac{1700}{Re}$. ·old slide 530
- *(not in the Oct 2026 edition)* Laminar boundary layer: $\delta = 5.48\sqrt{\nu x/U}$ (grows as $\sqrt{x}$); wall
  shear $\tau_0 \propto 1/\sqrt{x}$. ·old slide 531
  > ⚠ VERIFY ·old slide 531 — slide gives $\tau_0 = 3.65\sqrt{\mu\rho U^3/x}$. A coefficient of 3.65 is physically
  > implausible (it would make $C_f\sim7$); the standard laminar flat-plate wall shear is
  > $\tau_0 = 0.332\sqrt{\rho\mu U^3/x}$ (Blasius; ≈0.33–0.37 by momentum-integral). "3.65" looks like a
  > decimal-point error for ≈0.365/0.33. Use ≈0.33. See _verification-log.md. *(Dropped — old slide 531 is not
  > in the Oct 2026 edition.)*
- [ex ·slides 509–510] Smooth plate 8 ft × 80 ft towed lengthwise at 17 ft/s, $C_D=0.0020$, ρ=1.93:
  $D_f = 0.0020(1.93)(17^2/2)(80\cdot8) = 357$ lb (one side). ✓ *(ρ printed "1.93 lb/cft" — it is slug/ft³; S31,
  still printed in the Oct 2026 edition.)*

## 11.4 Flow past a cylinder ·slides 511–523
- [eq: cylinder-ideal] **Ideal (inviscid) flow:** surface velocity $v_\theta = 2U\sin\theta$; by Bernoulli ·slides 511–512
  $$p - p_\infty = \frac{\rho(U^2 - v_\theta^2)}{2} = \frac{\rho U^2}{2}(1 - 4\sin^2\theta)$$
- [def: dalembert] The pressure distribution is fore–aft symmetric ⇒ integrated pressure drag = **0** — no force
  on the cylinder. This contradicts reality: **d'Alembert's paradox** (d'Alembert, 1717–1783). ·slides 512–513
- [def] **Viscous regimes** (increasing Re): Re<1 attached symmetric flow; Re≈2–30 two symmetric standing
  eddies; Re≈40–70 wake oscillation begins; Re>90 alternate **vortex shedding**; 10²<Re<10⁵ the **Kármán vortex
  street** (separation ≈80° from front stagnation); at $Re \approx 3.8\times10^5$ (**critical Re**, $R_c$) the
  boundary layer turns turbulent, separation moves back to ≈130°. ·slides 514–518
- [def] Because separation lowers the rear pressure, most drag is **form drag**; $C_D \approx 1$–1.2 for
  $10^3<Re<2\times10^5$, then **drops abruptly to ≈0.3** at $R_c$ (**drag crisis** — separation point jumps
  downstream). Minimizing separation → the **streamline shape**. ·slides 521, 523
- [eq: strouhal] Vortex-shedding frequency (G. I. Taylor — the slide names Taylor only, unchanged in the Oct 2026
  edition; 250<Re<2×10⁵): ·slide 522
  $$f = 0.198\,\frac{U}{d}\Big(1 - \frac{19.7}{Re}\Big),\qquad St = \frac{fd}{U}\ \text{(Strouhal number)}$$
  Kármán vortices exert a cyclic force → vibration/sound (e.g. power lines "singing"). ·slide 522
- [ex ·slides 524–525] Pole (cylinder) d=100 mm, height 17 m, wind 15 m/s, $C_D=1.3$, ρ=1.16:
  $D = 1.3(1.16)(15^2/2)(17\cdot0.1) = 288$ N; bending moment about base $= 288\times8.5 = 2448$ N·m. ✓

## 11.5 Drag of a sphere; Stokes flow ·slides 526–529
- [def] Sphere $C_D \approx 0.44$ for $10^3<Re<2\times10^5$; drops to ≈0.1 near $Re\approx3\times10^5$
  (laminar→turbulent separation, like the cylinder), then rises toward ≈0.2. ·slide 526
- [eq: sphere-stokes] **Stokes flow** (creeping, Re<1): $D = 3\pi\mu U d$, hence $C_D = \dfrac{24}{Re}$
  (matches experiment for Re<1). ·slide 527
- [ex ·slides 528–529] Basketball d=9.3 in, 27 mph (=39.6 ft/s), $C_D=0.41$, ρ=0.00242:
  $D = 0.41(0.00242)(39.6^2/2)\,[\pi(9.3/12)^2/4] = 0.367$ lb. ✓ *(ρ printed "0.00242 lb/cft" — slug/ft³; S31,
  still printed in the Oct 2026 edition.)*

## 11.6 Friction torque on a revolving disc ·slides 530–534
- [eq: disc-torque] Disc radius $r_0$, thickness $b$, angular velocity ω, friction coefficient f (=f′):
  surface-friction torque on one face, from $dF = f\,\frac{\rho(r\omega)^2}{2}\,2\pi r\,dr$: ·slide 530
  $$T_1 = \int_0^{r_0} r\,dF = \frac{\pi f}{5}\rho\omega^2 r_0^{5}$$
  *(the Oct 2026 edition prints $r_0^5$ correctly on slide 530; old slide 557 printed $r_0^2$.)*
  Rim (cylindrical part, friction coefficient $f'$): $F' = f'\,\frac{\rho(r_0\omega)^2}{2}\,2\pi r_0 b$, so
  $T_2 = F' r_0 = \pi f'\rho\omega^2 r_0^4\,b$. ·slide 531 Total (two faces + rim, $f = f'$):
  $$T = 2T_1 + T_2 = \pi f\rho\omega^2 r_0^4\Big(\frac{2}{5}r_0 + b\Big),\qquad L = T\omega = \pi f\rho\omega^3 r_0^4\Big(\frac{2}{5}r_0 + b\Big)$$
  (used for impeller friction power loss in centrifugal pumps/turbines.) ·slides 530–532
  > ⚠ VERIFY S85 ·slide 531 — prints "$T_2 = \pi f'\rho\omega^2 r_o b$" and, in the sum, "$+\ \pi f\rho\omega^2 r_o b$". Both lack
  > $r_0^3$: it should be $\pi f'\rho\omega^2 r_0^{4} b$. Dimension check — $\rho\omega^2 r_0 b$ is kg·m⁻³·s⁻²·m² = Pa,
  > not N·m; $\rho\omega^2 r_0^4 b$ is N·m ✓. The slide's own final line, $\pi f\rho\omega^2 r_0^4(\tfrac25 r_0 + b)$, needs
  > $r_0^4 b$. Already on old slide 558; not previously logged.
- [ex ·slides 533–534] Airplane wing 6.5×50 m at 230 m/s, 9 km altitude, $C_D = 0.031\,Re^{-1/7}$: Re=4.68×10⁷,
  $C_D=0.00249$, $F_D=0.0201$ MN (both sides), **P = F_D·V ≈ 4.63 MW**. ✓ *(slide 533 prints "0.31"; the solution
  correctly uses 0.031 — logged. **Still printed in the Oct 2026 edition.**)*

## 11.7 Lift — rotating cylinder & Kutta–Joukowski ·slides 535–541
- [derivation] A cylinder in stream U rotating at ω (no separation): surface velocity
  $v_\theta = 2U\sin\theta + r_0\omega$. Integrating the Bernoulli pressure over the surface gives the lift per
  unit width. ·slides 536–540
  - Bernoulli on the surface ·slide 538:
    $$\frac{p - p_\infty}{\rho U^2/2} = 1 - \Big(\frac{2U\sin\theta + r_0\omega}{U}\Big)^2$$
  - Lift per unit width, with the square expanded ·slides 539–540:
    $$L = -r_0\rho U^2\int_{-\pi/2}^{\pi/2}\Big[1 - \Big(\frac{r_0\omega}{U}\Big)^2 - \frac{4r_0\omega}{U}\sin\theta - 4\sin^2\theta\Big]\sin\theta\,d\theta = 2\pi r_0^2\omega\rho U$$
    Only the cross term $-\frac{4r_0\omega}{U}\sin\theta$ survives the integration — it is the whole of the lift.
  > ⚠ VERIFY S84 ·slide 538 — new in the Oct 2026 edition. The expansion line prints
  > "$\rho U^2/2 - \rho(4U^2\sin^2\theta + r_o^2\omega^2)/2 = p - p_\infty$". The square has lost its cross term:
  > $(2U\sin\theta + r_0\omega)^2 = 4U^2\sin^2\theta + 4Ur_0\omega\sin\theta + r_0^2\omega^2$. Check: with $\omega = 0$ the
  > two forms agree; with $\omega \ne 0$ they differ by $2\rho U r_0\omega\sin\theta$. That dropped term is the one that
  > produces the lift — without it the integrand is odd in θ and the integral gives $L = 0$. The next line on 538
  > and the expansion on 540 are correct.
- [eq: kutta-joukowski] With circulation $\Gamma = 2\pi r_0 u = 2\pi r_0^2\omega$:
  $$\boxed{\,L = \rho U\Gamma\,}\qquad\text{— Kutta–Joukowski theorem}$$
  Explains why spinning balls (baseball/tennis/golf) curve; wings and sails generate circulation ⇒ lift. Golf
  dimples add turbulence to enlarge circulation and lift while stabilizing flight. ·slides 540–541 *(the equation
  closes slide 540, where $L = 2\pi r_0 u\rho U$ with $u = r_0\omega$; slide 541 repeats it as its title, with the
  spinning-ball and dimple prose. The old deck spread this over old slides 566–568, and old slide 566 printed
  "$2\pi r_0\rho U$" without the $u$ — corrected in the Oct 2026 edition.)*

## 11.8 Wings / aerofoils ·slides 542–552
- [def] A **wing/aerofoil** is shaped so lift ≫ drag. Geometry: **chord** (leading→trailing edge), **camber
  line** (mid-points of upper/lower surfaces), **camber**, **thickness**, **angle of attack α** (chord to flow). ·slides 542–544
- [eq: aspect-ratio] Span b, planform area A, chord l (A = bl): **aspect ratio** $= b^2/A = b/l$. ·slide 544
- [eq: wing-coeffs] $L = C_L\,l\,\dfrac{\rho U^2}{2}$, $D = C_D\,l\,\dfrac{\rho U^2}{2}$,
  $M = C_M\,l\,\dfrac{\rho U^2}{2}$ (per unit span). Coefficients depend on aerofoil section, Mach, Re. $C_L=0$
  at the **zero-lift angle**. ·slide 545 *(slide's third line prints "L = C_M…"; it should read M = moment, and
  per unit span the moment needs $l^2$ — S30. Both **still printed** in the Oct 2026 edition.)*
- [def] $C_L$ rises ~linearly with α, then peaks (**maximum lift coefficient**) and falls — **stall** — when the
  flow separates on the upper surface (α too large); that α = **stalling angle**. ·slides 546–547 *(547, "Stalled
  wing", is a separate page in the Oct 2026 edition: maximum lift coefficient = maximum value of $C_L$; the α at
  which it occurs = stalling angle; [fig] stalled-flow photo and $C_L$–α curves for three aerofoil sections.)*
- [def] **Lift-drag polar** = plot of $C_L$ vs $C_D$; its tangent from the origin gives the α of maximum
  $C_L/C_D$. ·slide 548
- [def] **Circulation theory of lift:** as a wing starts from rest a **starting vortex** sheds off the sharp
  trailing edge; by conservation an equal, opposite **bound vortex** (circulation) forms around the wing,
  producing lift. The flow leaves smoothly at the sharp trailing edge = **Kutta condition / Joukowski
  hypothesis**. ·slides 549–552

## 11.9 Cascade ·slides 553–555
- [def] A **cascade** = identical blades spaced around an axial blower/compressor/turbine, turning the flow with
  small loss via a stagger angle. Blade lift $= \rho v_\infty\Gamma$ ($v_\infty$ = mean of inlet/outlet
  velocity). ·slides 553–554
- [eq] **Interference coefficient** $k = L/L_0$ (cascade lift / solitary-blade lift); function of $l/t$ and β,
  and $k \approx 1$ when $l/t \le 0.5$. ·slide 555

## 11.10 Cavitation ·slides 556–561
- [def] By Bernoulli, high velocity → low pressure. If local pressure falls below the liquid's **saturation
  (vapour) pressure**, the liquid boils locally, forming vapour bubbles = **cavitation**. Dissolved gas also
  comes out earlier (Henry's law). Bubbles carried to higher-pressure regions collapse violently → noise,
  vibration, and pitting/erosion (pump/turbine blades, propellers, hydrofoils). ·slides 556–558
- [def] Beyond ~twice the chord the cavity stabilizes = **supercavitation** (applied to hydrofoil craft). ·slide 560
- [eq: cavitation-number] $$k_d = \frac{p_\infty - p_u}{\rho U^2/2}\quad\text{(cavitation number; }p_u=\text{saturation pressure)}$$
  Small $k_d$ ⇒ cavitation likely. ·slide 561

### Cross-references
- Boundary layer & separation from **08-viscous-flow** drive form drag and the drag crisis here.
- Circulation/vorticity from **05-flow-fundamentals**; the Kutta–Joukowski lift underlies pump/turbine cascades
  (**07-momentum** impeller work) and cavitation limits pump performance (**09-pipe-flow**).

### Verification notes for this section
- Verified correct: stagnation p₀; D=C_D A ρU²/2; ideal-cylinder p−p∞=(ρU²/2)(1−4sin²θ) and d'Alembert paradox
  (dates 1717–1783 correct); Kármán/drag-crisis Re values; Strouhal f=0.198(U/d)(1−19.7/Re); sphere C_D & Stokes
  C_D=24/Re; disc torque; Kutta–Joukowski L=ρUΓ; aspect ratio; cavitation number. Worked examples (357 lb, 288 N
  / 2448 N·m, 0.367 lb, 4.63 MW) all check.
- 2 flags logged: old slide 531 τ₀ coefficient 3.65 (decimal error → ≈0.33); slide 533 C_D "0.31"→0.031 (solution
  uses 0.031). Minor: slide 545 third line "L"→"M" (moment). Extraction garble (T₁ exponent) corrected to r₀⁵.
- Oct 2026 edition (rechecked on rendered pages 498–561): old slides 530–531 (flat-plate $C_f$, δ, τ₀) are **not in
  the new edition** — the τ₀ flag goes with them. **Still printed:** 533 "0.31", 545 L→M and S30, S31 (509, 528),
  Taylor-only attribution (522). **Fixed:** T₁ now printed with $r_0^5$ (530); the lift expansion on 540 is complete
  and $L = 2\pi r_0 u\rho U$ keeps its $u$. New flags S84 (538, dropped cross term — substantive) and S85 (531, $T_2$
  exponent — present since the old deck). Slides 515, 531, 538 and 547 are split-out pages of old material; the
  only genuinely new content among them is the expansion on 538 (with S84).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
