---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "07 — Conservation of Momentum"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "256-288 (plus slide 222 and old slides 297-301 in §7.10)"
file_role: topic
subtopics:
  - "linear momentum principle; control volume"
  - "momentum equation for a curved pipe (force on a bend)"
  - "force of a jet on a plate (stationary and moving)"
  - "jet split on an inclined plate (Q1/Q2)"
  - "sudden-expansion (Borda–Carnot) head loss — reworked derivation (slides 269–271)"
  - "jet pump — force derivation and example (slides 272–276)"
  - "propeller thrust & efficiency (actuator disk)"
  - "angular momentum; torque & power of an impeller (Euler turbomachine equation)"
key_equations: [momentum-cv, bend-force, jet-force, jet-split, moving-plate-force, borda-carnot, jet-pump, propeller-thrust, propeller-eff, euler-turbomachine]
prerequisites: ["05-flow-fundamentals (continuity)", "06-energy-bernoulli"]
leads_to: ["09-pipe-flow (fittings losses, pumps)", "11-drag-and-lift"]
verification_flags: 9   # still printed or new in the Oct 2026 edition; 4 more are marked fixed and 1 (S16) changed, in place
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

## 7.1 Linear momentum principle ·slides 256–259
- [def] Motion effects need **momentum** $M v$, not just velocity (a fast baseball is catchable; a car is hard to
  stop). ·slide 257
- [eq] Newton's 2nd law (impulse–momentum): force = rate of change of momentum. ·slide 258
  $$F = \frac{M v_2 - M v_1}{t} = \dot{m}(v_2 - v_1)$$
  > ⚠ VERIFY ·slide 258 — slide writes $F=(Mv_1-Mv_2)/t$ (initial − final); correct is final − initial,
  > $F=(Mv_2-Mv_1)/t$. Sign slip. See _verification-log.md. *(still printed in the Oct 2026 edition)*
- [def] A force on a wall in contact with flow is obtained from the momentum change over a **control volume** —
  no need to examine the internal phenomena. ·slide 259
- [fig ·slide 259] *(new in the Oct 2026 edition)* A dashed control surface around a jet ($V_j$, area $A_j$)
  striking a flat plate head-on and splitting into two equal streams, $A_1 = A_2 = \tfrac12 A_j$, with the
  reaction components $R_x$, $R_y$ marked.

## 7.2 Momentum equation for a curved pipe (bend force) ·slides 260–263
- [fig ·slides 260–263] Control volume ABCD in a bend: inlet AB (area $A_1$, velocity $v_1$, pressure $p_1$,
  angle $\alpha_1$), outlet CD ($A_2,v_2,p_2,\alpha_2$). $F$ = force of the fluid on the pipe; reaction on fluid
  is $-F$ with components $F_x,F_y$. *(Oct 2026 edition adds a photograph of pipe bends on 260 and a small
  sketch of a 45° bend on 261.)*
- [eq: bend-force] With $\dot{m} = \rho Q = \rho A_1 v_1 = \rho A_2 v_2$: ·slides 262–263
  $$-F_x + A_1p_1\cos\alpha_1 - A_2p_2\cos\alpha_2 = \dot m(v_2\cos\alpha_2 - v_1\cos\alpha_1)$$
  $$-F_y + A_1p_1\sin\alpha_1 - A_2p_2\sin\alpha_2 = \dot m(v_2\sin\alpha_2 - v_1\sin\alpha_1)$$
  Rearranged for the force components: ·slide 263
  $$F_x = \dot m(v_1\cos\alpha_1 - v_2\cos\alpha_2) + A_1p_1\cos\alpha_1 - A_2p_2\cos\alpha_2$$
  $$F_y = \dot m(v_1\sin\alpha_1 - v_2\sin\alpha_2) + A_1p_1\sin\alpha_1 - A_2p_2\sin\alpha_2$$
  Resultant $F = \sqrt{F_x^{2} + F_y^{2}}$.
  > ⚠ VERIFY ·slide 263 — the Jul 2026 edition printed the resultant as $F=\sqrt{F_x^{2} - F_y^{2}}$ (minus).
  > Correct is $\sqrt{F_x^{2} + F_y^{2}}$. See log. *(fixed in the Oct 2026 edition — now reads
  > $F=\sqrt{F_x^{2}+F_y^{2}}$)*
  > ⚠ VERIFY S17 ·slide 263 — the Jul 2026 edition printed the rearranged pair as $-F_x$/$-F_y$ with the
  > velocities missing from the $F_x$ line. *(fixed in the Oct 2026 edition — now reads as above; the algebra
  > follows from the first pair)*

## 7.3 Force of a jet on a stationary inclined plate ·slides 265–267
- [fig ·slide 265] 2-D jet (flow rate $Q$, velocity $v$) strikes a plate inclined at θ, splitting into up-jet
  $Q_1$ and down-jet $Q_2$. Assumptions: jet pressure = ambient; no loss ⇒ along-plate velocity component
  unchanged (normal component brought to 0).
- [fig ·slide 265] *(new in the Oct 2026 edition)* a small pasted inset, "Force exerted by the jet on a
  stationary plate", listing $F_N = \rho a V^2\sin\theta$, $F_x = F_N\sin\theta$ and a second line also
  labelled $F_x = F_N\cos\theta$.
  > ⚠ VERIFY S65 ·slide 265 — the inset's third line is labelled $F_x$ again; it is the other component,
  > $F_y = F_N\cos\theta$ (it matches the $F_y$ of slide 266). Cosmetic.
- [eq: jet-force] Normal force (velocity normal component $v\sin\theta$ destroyed): ·slide 266
  $$F = \rho Q v\sin\theta,\qquad F_x = F\sin\theta = \rho Q v\sin^2\theta,\qquad F_y = F\cos\theta = \rho Q v\sin\theta\cos\theta$$
  > ⚠ VERIFY S63 ·slide 266 — the Oct 2026 edition prints "$F_x = F\sin\theta = \rho Qv\sin\theta$" (the
  > square is gone; the Jul 2026 edition printed $\sin^2\theta$). Substituting the slide's own
  > $F=\rho Qv\sin\theta$ into $F\sin\theta$ gives $\rho Qv\sin^2\theta$. Learn the squared form.
- [eq: jet-split] No force along a frictionless plate ⇒ from momentum + continuity ($Q=Q_1+Q_2$,
  $Q\cos\theta = Q_1-Q_2$): ·slide 267
  $$\boxed{\,Q_1 = \tfrac{Q}{2}(1+\cos\theta),\qquad Q_2 = \tfrac{Q}{2}(1-\cos\theta)\,}$$
  > ⚠ VERIFY S64 ·slide 267 — two reworded lines in the Oct 2026 edition: "Force acting along flat board if
  > the flow loss is disregarded, **v** = 0" (it is the **force** along the board that is zero; the velocity
  > along the board stays $v$), and "$\Delta m = F\cos\theta = \rho Qv\cos\theta$" ($\rho Qv\cos\theta$ is the
  > incoming along-board momentum flux; $F\cos\theta$ is $F_y=\rho Qv\sin\theta\cos\theta$). The $Q_1$, $Q_2$
  > results are unaffected. Cosmetic.

## 7.4 Force of a jet on a moving plate ·slide 268
- [derivation] Plate recedes at $u$ in the flow direction; relative jet velocity $(v-u)$; intercepted flow
  $Q' = Q\dfrac{v-u}{v}$; normal velocity change $(v-u)\sin\theta$. ·slide 268
- [eq: moving-plate-force] ·slide 268
  $$F = \rho Q'(v-u)\sin\theta = \boxed{\,\rho\,\frac{Q\,(v-u)^2\sin\theta}{v}\,}$$
  > ⚠ VERIFY ·old slide 277 — the Jul 2026 edition printed $\rho Q(v-u)^2\sin\theta/\mathbf{v^2}$. Substituting
  > the slide's own $Q'=Q(v-u)/v$ gives $/v$, not $/v^2$; also $/v^2$ is dimensionally not a force. See log.
  > *(fixed in the Oct 2026 edition — old slide 277 is gone and slide 268 now reads
  > $F=\rho Q(v-u)^2\sin\theta/v$)*

## 7.5 Sudden-expansion (Borda–Carnot) head loss ·slides 269–271
- [derivation] Horizontal sudden enlargement $A_1\to A_2$. At the joint the pressure equals $p_1$ (parallel
  streamlines in the small pipe). Bernoulli with the loss $h_s$: ·slide 269
  $$h_s = \frac{p_1-p_2}{\rho g} + \frac{v_1^2-v_2^2}{2g}$$
- [derivation] Momentum on the control volume, with $Q = A_2v_2$ and $v_2 = A_1v_1/A_2$: ·slide 270
  $$\rho Q(v_2-v_1) = (p_1-p_2)A_2 \;\Rightarrow\; \frac{p_1-p_2}{\rho g} = \frac{v_2}{g}(v_2-v_1) = \frac{v_2}{g}\,v_1\Big(\frac{A_1}{A_2}-1\Big)$$
  > ⚠ VERIFY S15 ·slide 270 — the Jul 2026 edition printed this momentum line as $\rho Q(v_2^2-v_1^2)=(p_1-p_2)A_2$
  > (watts = newtons). *(fixed in the Oct 2026 edition — now reads $\rho Q(v_2-v_1)=(p_1-p_2)A_2$)*
- [derivation] Substituting into Bernoulli: ·slides 270–271
  $$h_s = \frac{2v_2v_1}{2g}\Big(\frac{A_1}{A_2}-1\Big) + \frac{v_1^2-v_2^2}{2g}$$
  *[added]* With $v_2 = (A_1/A_2)v_1$, the first term is $\dfrac{2v_2^2-2v_1v_2}{2g}$, so
  $$h_s = \frac{v_1^2-2v_1v_2+v_2^2}{2g} = \frac{(v_1-v_2)^2}{2g}$$
  (the slide quotes $a^2-2ab+b^2=(a-b)^2$ for this step).
- [eq: borda-carnot] ·slide 271
  $$\boxed{\,h_s = \frac{(v_1-v_2)^2}{2g} = \Big(1-\frac{A_1}{A_2}\Big)^2\frac{v_1^2}{2g}\,}\qquad\text{(Borda–Carnot loss)}$$
  > ⚠ VERIFY S66 ·slide 271 — the reworked chain carries a spurious factor: the first line multiplies
  > $(v_1^2-v_2^2)/2g$ by $[(A_1/A_2)-1]$, and the next lines carry $[1-(A_1/A_2)]$ through
  > "$h_s = \frac{(v_1-v_2)^2}{2g}[1-(A_1/A_2)]$" and "$h_s = \frac{v_1^2(1-A_1/A_2)^2}{2g}[1-(A_1/A_2)]$" — then the
  > final boxed line drops it. The line "$-2v_2v_1/2g + (v_1^2-v_2^2)/2g$" is also not $(v_1-v_2)^2/2g$ (that needs
  > $+v_2^2$). The **final result is right**; do not copy the intermediate lines. Check: with $r=A_1/A_2$,
  > $2r(r-1)+1-r^2=(1-r)^2$ exactly, with no extra factor.
  *(Reading note: in the rendered PDF several superscript glyphs on 271, 274–276 and 278 do not draw — e.g. the
  final line shows "$(1-A_1/A_2)\,v_1^2/2g$". The PDF text layer has the squares, so this is a rendering gap,
  not a printed error.)*

## 7.6 Jet pump ·slides 272–276
- [def] A high-velocity jet ($v_0$, through area $\tfrac{\pi}{4}d^2$) discharges into a larger pipe (diameter
  $D$) carrying water at $v_1$; they mix to $v_2$, and the jet drags the surrounding water along — pumping it. ·slides 272–274
  *(Oct 2026 edition adds a photograph of a jet-pump unit on 272.)*
- [derivation] Momentum flux = $\rho Q v = \rho A v^2$ (·slide 274). Outflow $\tfrac{\pi}{4}D^2\rho v_2^2$;
  inflow $\tfrac{\pi}{4}(D^2-d^2)\rho v_1^2 + \tfrac{\pi}{4}d^2\rho v_0^2$. Force on the fluid
  $\tfrac{\pi}{4}D^2(p_1-p_2)$. By the law of momentum: ·slides 274–275
  $$\tfrac{\pi}{4}\rho\big[D^2v_2^2-(D^2-d^2)v_1^2-d^2v_0^2\big] = \tfrac{\pi}{4}D^2(p_1-p_2)$$
- [eq: jet-pump] With continuity $D^2v_2 = (D^2-d^2)v_1 + d^2v_0$ *[added — the slide does not write it]*:
  $$\boxed{\,p_2 - p_1 = \rho\,\frac{d^2}{D^2}\,\frac{D^2-d^2}{D^2}\,(v_0-v_1)^2 \;(>0)\,}$$
  Since $p_2>p_1$, the jet pump forces water out against a pressure difference. ·slide 275
  > ⚠ VERIFY S67 ·slides 275–276 — the Oct 2026 edition prints "$P_1 - p_2 = \rho\frac{d^2}{D^2}\frac{D^2-d^2}{D^2}(v_o-v_1)^2$"
  > with "$p_1 - p_2$ is always positive"; the Jul 2026 edition printed "$P_2 - p_1 = \ldots$". The momentum
  > line above gives $p_1-p_2 = -\rho\frac{d^2}{D^2}\frac{D^2-d^2}{D^2}(v_0-v_1)^2 < 0$ — the pressure **rises**
  > from section 1 to 2. This is the same reversed subtraction as the 2025 exam (P33).
  > ⚠ VERIFY S16 ·slide 275 — the Jul 2026 slide had $p_2-p_1$ in the formula but "$p_1-p_2$ is always
  > positive" in the prose. *(changed in the Oct 2026 edition — the formula was flipped to match the prose, so
  > both are now wrong; see S67)*
  > ⚠ VERIFY S68 ·slide 275 — a scrap of continuity on the right: "$A_1v_1 = A_2v_2$; $V_2 = A_1v_1/A_2$;
  > $V_2 = D^2/d^2$". The last line sets a velocity equal to a pure number, and single-stream continuity is not
  > the jet-pump continuity ($D^2v_2 = (D^2-d^2)v_1 + d^2v_0$). Not used in the result. Cosmetic.
- [exercise ·slide 276] *(new in the Oct 2026 edition)* Using the expression above, determine the change in
  pressure when a jet of radius 3 cm discharges water at 8.9 m/s into water in a larger pipe of radius 8 cm
  whose velocity is 6.3 m/s. (Same data as the 2024 CAT 1 Q4(a), which called 6.3 m/s a "flow rate" — P9; the
  slide now says "velocity".)
  - *[added]* Worked answer. Radii can be used directly, since only $d^2/D^2$ appears: $d^2/D^2 = (3/8)^2 = 0.1406$,
    $(D^2-d^2)/D^2 = 0.8594$, $(v_0-v_1)^2 = 2.6^2 = 6.76\ \text{m}^2/\text{s}^2$. Water density not given; with
    $\rho = 1000\ \text{kg/m}^3$:
    $$\Delta p = 1000 \times 0.1406 \times 0.8594 \times 6.76 = 817\ \text{Pa} \approx 0.82\ \text{kPa}$$
    ($815$ Pa with $\rho = 998$). Continuity gives $v_2 = 6.67$ m/s, and the full momentum balance gives
    $p_1-p_2 = -817$ Pa: the pressure **rises** by about 0.82 kPa, so state the answer as $p_2-p_1 = +817$ Pa.
    *(Checked in Python.)*

## 7.7 Propeller thrust & efficiency (actuator disk) ·slides 277–279
- [fig ·slide 278] Uniform flow $U$ meets a propeller (diameter $D$); the slipstream is accelerated to $U+u$
  far downstream; upstream/downstream static pressures equal.
- [eq: propeller-thrust] From momentum + energy (the Oct 2026 edition words it "from $\Delta p$
  ($=A\rho v^2$) and K.E.", using $p$ for the momentum flux — not pressure): ·slide 278
  $$T = \frac{\pi}{4}D^2\,\rho\,u\Big(U + \frac{u}{2}\Big)$$
- [eq: propeller-eff] Ideal (Froude) propulsive efficiency — the attainable upper limit: ·slide 279
  $$\boxed{\,\eta = \frac{2}{2 + u/U}\,}$$

## 7.8 Angular momentum ·slides 280–282
- [eq] For mass $M$ rotating at radius $r$, speed $v$: angular momentum
  $= (\text{moment of inertia})\times(\text{angular velocity}) = Mr^2\cdot\dfrac{v}{r} = Mrv$. ·slide 281
- [def] **Torque** = rate of change of angular momentum = moment of inertia × angular acceleration
  (conservation of angular momentum). Illustration: a skater spreading her arms raises her moment of inertia and
  slows her spin. ·slides 281–282
- Slide 283 *(new in the Oct 2026 edition)* carries only a video link — no content to learn from the slide.

## 7.9 Torque & power of an impeller — Euler turbomachine equation ·slides 284–288
- [fig ·slides 284–287] Fluid crossing a rotating impeller from radius $r_1$ to $r_2$. Velocity triangles:
  peripheral (blade) velocity $u$, absolute velocity $v$ at angle $\alpha$ to $u$, relative velocity $w$.
  *(In the Oct 2026 edition the curved-tube material of old slides 289–291 is merged onto slide 284; slide 285
  adds a water-wheel photograph and an overshot-wheel sketch.)*
  > ⚠ VERIFY S69 ·slide 287 — the Oct 2026 edition calls the relative velocities "$\omega_1$ and $\omega_2$"
  > (the Jul 2026 edition and the figure use $w_1$, $w_2$). $\omega$ is the impeller's angular velocity on
  > slide 288 ($L = T\omega$). Read them as $w_1$, $w_2$. Cosmetic.
- [derivation] Angular-momentum equation about the shaft O (pressure forces pass through O ⇒ their moments
  vanish): ·slides 284, 287–288
- [eq: euler-turbomachine]
  $$\boxed{\,T = \dot m\,(r_2 v_2\cos\alpha_2 - r_1 v_1\cos\alpha_1)\,},\qquad \text{power } L = T\omega$$
  (torque set by the tangential component of the **absolute** velocity, $v\cos\alpha$, at inlet and outlet.)
  > ⚠ VERIFY ·slides 284 & 288 — slides write the torque with the **peripheral** velocity,
  > $\dot m(r_2 u_2\cos\alpha_2 - r_1 u_1\cos\alpha_1)$. The moment of momentum uses the tangential component of
  > the **absolute** velocity $v\cos\alpha$ (α is defined as the angle of $v$ to $u$ on slide 286), so it must be
  > $v_2,v_1$, not $u_2,u_1$ — and the linear version on slide 263 correctly uses $v$. Confirmed on the rendered
  > slides. See log. *(still printed in the Oct 2026 edition — on 284, 287 and 288)*

## 7.10 Worked / review examples ·slide 222 (and old slides 297–301, not in the Oct 2026 edition)
- *The old review slides 297–301 below are not in the Oct 2026 edition; the content is kept for reference.*
- ·222 — conduit velocities (same as 06 §6.5 example: v₁=6.62, v₂=4.59, v₃=1.66 m/s — v₃ is [added]; slide 223 stops at "Find v₃"). *(S18 — the 0.013 m³/s
  rounding on slide 223 is still printed in the Oct 2026 edition.)* ·old slide 297 — pressures p₂,p₃ from
  Bernoulli given p₁=24.5 kPa. ·old slide 298 — time to empty a tank (orifice, falling head → 06 §6.8). ·old slide 299 — vessel shape
  for constant surface descent ($H\propto r^4$ → 06 §6.8). *(These reuse continuity/Bernoulli; solutions not
  fully shown on the slides.)*
- [ex ·old slides 300–301] Jet on a plate, θ=60°, d=25 mm, Q=0.12 m³/s:
  $Q_1 = \tfrac{Q}{2}(1+\cos60°) = 0.09\ \text{m}^3/\text{s}$; $Q_2 = \tfrac{Q}{2}(1-\cos60°) = 0.03\ \text{m}^3/\text{s}$;
  $F = \rho Q v\sin\theta$ with $v = Q/A$ (ρ=998 kg/m³). *(Q₁,Q₂ computed; the slide's F line is cut off. Note the
  given d gives a very high v = Q/A, so F is correspondingly large — flagged as an unrealistic textbook data set,
  not an equation error.)*

### Cross-references
- Sudden-expansion loss & pump/turbine torque are applied in **09-pipe-flow** (minor losses, pumping).
- Jet/plate forces connect to the drag concepts in **11-drag-and-lift**.
- Uses continuity (**05**) and Bernoulli (**06**).

### Verification notes for this section
- **Jul 2026 flags, rechecked against the Oct 2026 edition:** impulse sign (258) — still printed; resultant
  $\sqrt{F_x^2-F_y^2}$ (263) — fixed; moving-plate force $/v^2$ (old 277) — fixed (slide gone, 268 correct);
  impeller torque $u$ → $v$ (284, 287, 288) — still printed. S15 (270) fixed; S16 (275) changed — see S67;
  S17 (263) fixed; S18 (223) still printed.
- **New in the Oct 2026 edition:** S63 $\sin\theta$ for $\sin^2\theta$ (266); S64 wording on 267; S65 inset
  label (265); S66 spurious factor in the reworked Borda–Carnot chain (271); S67 jet-pump sign now reversed
  in the formula itself (275–276); S68 stray continuity line (275); S69 $\omega$ for $w$ (287).
- Verified correct: bend-force rearrangement (263); jet split Q₁,Q₂; Borda–Carnot final result
  $(1-A_1/A_2)^2 v_1^2/2g$; moving-plate force (268); propeller thrust & η=2/(2+u/U); angular momentum = Mrv;
  jet-pump example 276 recomputed (817 Pa rise).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
