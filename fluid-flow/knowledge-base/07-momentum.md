---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "07 — Conservation of Momentum"
slides: "264-301"
file_role: topic
subtopics:
  - "linear momentum principle; control volume"
  - "momentum equation for a curved pipe (force on a bend)"
  - "force of a jet on a plate (stationary and moving)"
  - "jet split on an inclined plate (Q1/Q2)"
  - "sudden-expansion (Borda–Carnot) head loss"
  - "jet pump"
  - "propeller thrust & efficiency (actuator disk)"
  - "angular momentum; torque & power of an impeller (Euler turbomachine equation)"
key_equations: [momentum-cv, bend-force, jet-force, jet-split, moving-plate-force, borda-carnot, propeller-thrust, propeller-eff, euler-turbomachine]
prerequisites: ["05-flow-fundamentals (continuity)", "06-energy-bernoulli"]
leads_to: ["09-pipe-flow (fittings losses, pumps)", "11-drag-and-lift"]
verification_flags: 4
tags: [momentum, control-volume, jet-force, bend, borda-carnot, jet-pump, propeller, angular-momentum, euler-turbomachine, impeller]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  This section had several genuine slide errors (resultant sign, moving-plate exponent, torque using u vs v);
  each was confirmed by viewing the actual rendered slide, and canonical forms are given. -->

# 07 — Conservation of Momentum

Momentum lets forces on solid boundaries be found from inlet/outlet flow states alone, without the internal
detail. Method: draw a **control volume**, equate the net force (pressure + reaction) to the momentum flux out
minus in.

## 7.1 Linear momentum principle ·slides 264–267
- [def] Motion effects need **momentum** $M v$, not just velocity (a fast baseball is catchable; a car is hard to
  stop). ·slide 265
- [eq] Newton's 2nd law (impulse–momentum): force = rate of change of momentum. ·slide 266
  $$F = \frac{M v_2 - M v_1}{t} = \dot{m}(v_2 - v_1)$$
  > ⚠ VERIFY ·slide 266 — slide writes $F=(Mv_1-Mv_2)/t$ (initial − final); correct is final − initial,
  $F=(Mv_2-Mv_1)/t$. Sign slip. See _verification-log.md.
- [def] A force on a wall in contact with flow is obtained from the momentum change over a **control volume** —
  no need to examine the internal phenomena. ·slide 267

## 7.2 Momentum equation for a curved pipe (bend force) ·slides 268–271
- [fig ·slides 268–271] Control volume ABCD in a bend: inlet AB (area $A_1$, velocity $v_1$, pressure $p_1$,
  angle $\alpha_1$), outlet CD ($A_2,v_2,p_2,\alpha_2$). $F$ = force of the fluid on the pipe; reaction on fluid
  is $-F$ with components $F_x,F_y$.
- [eq: bend-force] With $\dot{m} = \rho Q = \rho A_1 v_1 = \rho A_2 v_2$: ·slide 271
  $$-F_x + A_1p_1\cos\alpha_1 - A_2p_2\cos\alpha_2 = \dot m(v_2\cos\alpha_2 - v_1\cos\alpha_1)$$
  $$-F_y + A_1p_1\sin\alpha_1 - A_2p_2\sin\alpha_2 = \dot m(v_2\sin\alpha_2 - v_1\sin\alpha_1)$$
  Resultant $F = \sqrt{F_x^{2} + F_y^{2}}$.
  > ⚠ VERIFY ·slide 271 — slide prints the resultant as $F=\sqrt{F_x^{2} - F_y^{2}}$ (minus). Correct is
  > $\sqrt{F_x^{2} + F_y^{2}}$ (confirmed on the rendered slide). See log.

## 7.3 Force of a jet on a stationary inclined plate ·slides 273–275
- [fig ·slide 273] 2-D jet (flow rate $Q$, velocity $v$) strikes a plate inclined at θ, splitting into up-jet
  $Q_1$ and down-jet $Q_2$. Assumptions: jet pressure = ambient; no loss ⇒ along-plate velocity component
  unchanged (normal component brought to 0).
- [eq: jet-force] Normal force (velocity normal component $v\sin\theta$ destroyed): ·slide 274
  $$F = \rho Q v\sin\theta,\qquad F_x = F\sin\theta = \rho Q v\sin^2\theta,\qquad F_y = F\cos\theta = \rho Q v\sin\theta\cos\theta$$
- [eq: jet-split] No force along a frictionless plate ⇒ from momentum + continuity ($Q=Q_1+Q_2$,
  $Q\cos\theta = Q_1-Q_2$): ·slide 275
  $$\boxed{\,Q_1 = \tfrac{Q}{2}(1+\cos\theta),\qquad Q_2 = \tfrac{Q}{2}(1-\cos\theta)\,}$$

## 7.4 Force of a jet on a moving plate ·slides 276–277
- [derivation] Plate recedes at $u$ in the flow direction; relative jet velocity $(v-u)$; intercepted flow
  $Q' = Q\dfrac{v-u}{v}$; normal velocity change $(v-u)\sin\theta$. ·slide 276
- [eq: moving-plate-force] ·slide 277
  $$F = \rho Q'(v-u)\sin\theta = \boxed{\,\rho\,\frac{Q\,(v-u)^2\sin\theta}{v}\,}$$
  > ⚠ VERIFY ·slide 277 — slide prints $\rho Q(v-u)^2\sin\theta/\mathbf{v^2}$. Substituting the slide's own
  > $Q'=Q(v-u)/v$ gives $/v$, not $/v^2$; also $/v^2$ is dimensionally not a force. Correct denominator is **v**
  > (confirmed on the rendered slide). See log.

## 7.5 Sudden-expansion (Borda–Carnot) head loss ·slides 278–279
- [derivation] Horizontal sudden enlargement $A_1\to A_2$. At the joint the pressure equals $p_1$ (parallel
  streamlines in the small pipe). Combining Bernoulli (with loss $h_s$) and the momentum equation
  $\rho Q(v_2^2-v_1^2)=(p_1-p_2)A_2$: ·slides 278–279
- [eq: borda-carnot]
  $$\boxed{\,h_s = \frac{(v_1-v_2)^2}{2g} = \Big(1-\frac{A_1}{A_2}\Big)^2\frac{v_1^2}{2g}\,}\qquad\text{(Borda–Carnot loss)}$$

## 7.6 Jet pump ·slides 280–282
- [def] A high-velocity jet ($v_0$, through area $\tfrac{\pi}{4}d^2$) discharges into a larger pipe (diameter
  $D$) carrying water at $v_1$; they mix to $v_2$, and the jet drags the surrounding water along — pumping it. ·slides 280–282
- [derivation/eq] Momentum balance (out − in) = pressure force $\tfrac{\pi}{4}D^2(p_1-p_2)$: ·slide 282
  $$\tfrac{\pi}{4}\rho\big[D^2v_2^2-(D^2-d^2)v_1^2-d^2v_0^2\big] = \tfrac{\pi}{4}D^2(p_1-p_2)$$
  $$p_2 - p_1 = \rho\,\frac{d^2}{D^2}\,\frac{D^2-d^2}{D^2}\,(v_0-v_1)^2 \;(>0)$$
  Since $p_2>p_1$, the jet pump forces water out against a pressure difference. ·slide 282

## 7.7 Propeller thrust & efficiency (actuator disk) ·slides 283–285
- [fig ·slide 284] Uniform flow $U$ meets a propeller (diameter $D$); the slipstream is accelerated to $U+u$
  far downstream; upstream/downstream static pressures equal.
- [eq: propeller-thrust] From momentum + energy: ·slide 284
  $$T = \frac{\pi}{4}D^2\,\rho\,u\Big(U + \frac{u}{2}\Big)$$
- [eq: propeller-eff] Ideal (Froude) propulsive efficiency — the attainable upper limit: ·slide 285
  $$\boxed{\,\eta = \frac{2}{2 + u/U}\,}$$

## 7.8 Angular momentum ·slides 286–288
- [eq] For mass $M$ rotating at radius $r$, speed $v$: angular momentum
  $= (\text{moment of inertia})\times(\text{angular velocity}) = Mr^2\cdot\dfrac{v}{r} = Mrv$. ·slide 287
- [def] **Torque** = rate of change of angular momentum = moment of inertia × angular acceleration
  (conservation of angular momentum). Illustration: a skater spreading her arms raises her moment of inertia and
  slows her spin. ·slides 287–288

## 7.9 Torque & power of an impeller — Euler turbomachine equation ·slides 289–295
- [fig ·slides 289–294] Fluid crossing a rotating impeller from radius $r_1$ to $r_2$. Velocity triangles:
  peripheral (blade) velocity $u$, absolute velocity $v$ at angle $\alpha$ to $u$, relative velocity $w$.
- [derivation] Angular-momentum equation about the shaft O (pressure forces pass through O ⇒ their moments
  vanish): ·slides 291, 294–295
- [eq: euler-turbomachine]
  $$\boxed{\,T = \dot m\,(r_2 v_2\cos\alpha_2 - r_1 v_1\cos\alpha_1)\,},\qquad \text{power } L = T\omega$$
  (torque set by the tangential component of the **absolute** velocity, $v\cos\alpha$, at inlet and outlet.)
  > ⚠ VERIFY ·slides 291 & 295 — slides write the torque with the **peripheral** velocity,
  > $\dot m(r_2 u_2\cos\alpha_2 - r_1 u_1\cos\alpha_1)$. The moment of momentum uses the tangential component of
  > the **absolute** velocity $v\cos\alpha$ (α is defined as the angle of $v$ to $u$ on slide 293), so it must be
  > $v_2,v_1$, not $u_2,u_1$ — and the linear version on slide 271 correctly uses $v$. Confirmed on the rendered
  > slides. See log.

## 7.10 Worked / review examples ·slides 296–301
- ·296 — conduit velocities (same as 06 §6.5 example: v₁=6.62, v₂=4.59, v₃=1.66 m/s). ·297 — pressures p₂,p₃ from
  Bernoulli given p₁=24.5 kPa. ·298 — time to empty a tank (orifice, falling head → 06 §6.8). ·299 — vessel shape
  for constant surface descent ($H\propto r^4$ → 06 §6.8). *(These reuse continuity/Bernoulli; solutions not
  fully shown on the slides.)*
- [ex ·slides 300–301] Jet on a plate, θ=60°, d=25 mm, Q=0.12 m³/s:
  $Q_1 = \tfrac{Q}{2}(1+\cos60°) = 0.09\ \text{m}^3/\text{s}$; $Q_2 = \tfrac{Q}{2}(1-\cos60°) = 0.03\ \text{m}^3/\text{s}$;
  $F = \rho Q v\sin\theta$ with $v = Q/A$ (ρ=998 kg/m³). *(Q₁,Q₂ computed; the slide's F line is cut off. Note the
  given d gives a very high v = Q/A, so F is correspondingly large — flagged as an unrealistic textbook data set,
  not an equation error.)*

### Cross-references
- Sudden-expansion loss & pump/turbine torque are applied in **09-pipe-flow** (minor losses, pumping).
- Jet/plate forces connect to the drag concepts in **11-drag-and-lift**.
- Uses continuity (**05**) and Bernoulli (**06**).

### Verification notes for this section
- **4 flags** (all confirmed against the rendered slides): momentum sign (266); resultant $\sqrt{F_x^2-F_y^2}$
  → $+$ (271); moving-plate force $/v^2$ → $/v$ (277); impeller torque $u$ → $v$ (291 & 295).
- Verified correct: jet split Q₁,Q₂; Borda–Carnot $(1-A_1/A_2)^2 v_1^2/2g$; propeller thrust & η=2/(2+u/U);
  angular momentum = Mrv.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
