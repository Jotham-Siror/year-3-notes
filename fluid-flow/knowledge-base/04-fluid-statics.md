---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "04 — Fluid Statics"
slides: "77-165"
file_role: topic
subtopics:
  - "pressure definition & units; absolute vs gauge"
  - "characteristics of pressure: perpendicularity, isotropy, Pascal's law, hydraulic press"
  - "pressure variation with depth in a liquid"
  - "pressure variation in a gas / the polytropic atmosphere; lapse rate"
  - "pressure measurement: manometers (upright, U-tube, differential, inclined)"
  - "elastic & electric pressure gauges (Bourdon tube)"
  - "force on submerged plane surfaces; centre of pressure"
  - "hoop tension / bursting a thin cylinder"
  - "buoyancy & Archimedes' principle"
  - "ship stability & the metacentre"
  - "relative equilibrium: linear acceleration and rigid-body rotation"
key_equations: [pressure-def, hydrostatic-depth, polytropic-atmosphere, lapse-rate, manometer, force-on-plane, centre-of-pressure, hoop-tension, buoyancy, accel-free-surface, rotating-free-surface]
prerequisites: ["03-fluid-properties (density, perfect gas, polytropic)"]
leads_to: ["06-energy-bernoulli", "10-open-channel-flow"]
verification_flags: 1
tags: [statics, pressure, gauge, pascal, manometer, bourdon, centre-of-pressure, buoyancy, archimedes, metacentre, relative-equilibrium]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTATION: deck uses p = pressure and P (capital) = pressure FORCE in some slides, and elsewhere P = pressure.
  This KB uses p for pressure and F/P_force for force where the slide means force; noted where it matters. -->

# 04 — Fluid Statics

Balance of forces in fluids at rest — including "relative rest" (liquid moving rigidly with its vessel, e.g.
steady acceleration or rotation), which is analysed as a statics problem in vessel-fixed coordinates. ·slide 78

## 4.1 Pressure: definition & units ·slides 79–80
- [eq: pressure-def] Uniform load: $p = P/A$ (P = pressure force). Non-uniform:
  $p = \lim_{\Delta A\to0}\dfrac{\Delta P}{\Delta A} = \dfrac{dP}{dA}$. ·slide 79
- Units: SI **pascal** (Pa); also bar, or metres of water column (mH₂O). Standard atmosphere:
  $1\ \text{atm} = 760\ \text{mmHg} = 101{,}325\ \text{Pa}$ (at 273.15 K, g = 9.80665 m/s²). ·slide 80

## 4.2 Absolute vs gauge pressure ·slide 81
- [def] Referenced to a **perfect vacuum** → **absolute** pressure; referenced to **atmospheric** → **gauge**
  pressure. $p_\text{gauge} = p_\text{abs} - p_\text{atm}$ (negative gauge = below atmospheric).

## 4.3 Characteristics of pressure ·slides 82–88
1. [def] Fluid pressure always acts **perpendicular** to the wall in contact. ·slide 82
2. [def] Pressure at a point in a fluid at rest is **equal in all directions** (isotropic). ·slides 82, 84–86
   [derivation] Small triangular prism of unit width, faces $dA, dA_1, dA_2$ with pressures $p, p_1, p_2$; with
   geometry $dA_1 = dA\sin\theta$, $dA_2 = dA\cos\theta$ and the weight term second-order (negligible), force
   balance gives $p_1 = p_2 = p$ for any θ. ·slides 84–86
3. [def] **Pascal's law:** pressure applied to a confined fluid transmits undiminished to all parts. ·slides 83, 87
   [eq] Hydraulic press: small piston $p = F_1/A_1$; large piston $F_2 = pA_2 = F_1\,A_2/A_1$ (force amplification). ·slide 88

## 4.4 Pressure variation with depth — liquid ·slides 89–94
- [derivation] Vertical column, area $dA$: balance of bottom pressure, top pressure $p+(dp/dz)dz$, and weight
  $\rho g\,dA\,dz$ gives $\dfrac{dP}{dz} = -\rho g$, i.e. $dP = -\rho g\,dz$. ·slides 90–91
- [eq: hydrostatic-depth] Integrating (p = p₀ at z = z₀): ·slide 92
  $$p = p_0 + \rho g (z_0 - z) = p_0 + \rho g h \qquad\text{(pressure rises with depth } h)$$
- [ex ·slides 93–94] Newfound Lake, max depth 60 m, mean atmospheric 91 kPa, ρ_water = 9790 N/m³:
  $p_\max = 91{,}000 - (9790)(-60) = 678{,}400\ \text{Pa} \approx 678\ \text{kPa}$. ✓

## 4.5 Pressure variation in a gas — the polytropic atmosphere ·slides 95–107
- [derivation] Gas density varies with p; assume a polytropic change $p v^{n} = \text{const}$, i.e.
  $p/\rho^{n} = p_0/\rho_0^{n}$, so $\rho = \rho_0 (p/p_0)^{1/n}$. Substituting into $dP/dz = -\rho g$ and
  integrating from sea level (z=0, p₀, ρ₀): ·slides 95–99
  $$\boxed{\;\frac{p(z)}{p_0} = \Big[\,1 - \frac{n-1}{n}\,\frac{\rho_0 g}{p_0}\,z\,\Big]^{\frac{n}{n-1}}\;}
  \qquad\text{[eq: polytropic-atmosphere]}$$
  $$\frac{\rho(z)}{\rho_0} = \Big[\,1 - \frac{n-1}{n}\,\frac{\rho_0 g}{p_0}\,z\,\Big]^{\frac{1}{n-1}}$$
- [eq: lapse-rate] Using $p = \rho R T$, the temperature falls linearly (constant lapse rate): ·slides 100–101
  $$\frac{T(z)}{T_0} = 1 - \frac{n-1}{n}\frac{\rho_0 g}{p_0}z,\qquad
  \frac{dT}{dz} = -\frac{n-1}{n}\frac{g}{R}$$
- **Standard sea-level conditions** (aeronautics): $p_0 = 101.325$ kPa, $T_0 = 288.15$ K, $\rho_0 = 1.225$ kg/m³. ·slide 101
  > ⚠ VERIFY ·slide 102 — slide: "temperature decreases 0.65 °C/100 m in the troposphere **up to ≈1 km**, then
  > constant at **−50.5 °C from 1 km to 10 km**." Per the International Standard Atmosphere the 6.5 °C/km lapse
  > runs through the **whole troposphere to ≈11 km**, reaching ≈ **−56.5 °C** at the tropopause; the isothermal
  > (−56.5 °C) layer is the lower stratosphere, **≈11–20 km**. The slide's 1 km / 10 km / −50.5 °C appear to be
  > digit errors (11 km / 20 km / −56.5 °C). See _verification-log.md.
- [exercise/result ·slides 103–104] Troposphere polytropic index from $dT/dz = 0.0065$ K/m, and the standard
  $p_0,T_0,\rho_0$: **n = 1.235**. ✓ (verified: $(n-1)/n = (dT/dz)R/g = 0.0065\cdot287/9.807 = 0.190 \Rightarrow n=1.235$.)
- [ex ·slides 105–107] Pressure at 5000 m (take $g/RB = 5.26$):
  polytropic $p = 101350[1-(0.0065)(5000)/288.16]^{5.26} = 101350(0.8872)^{5.26} \approx 54{,}000$ Pa;
  isothermal $p \approx p_0 e^{-gz/RT} = 101350\,e^{-0.5929} \approx 56{,}000$ Pa. Isothermal overestimates by ~2 kPa
  (adequate as a rough approximation). ✓

## 4.6 Pressure measurement — manometers ·slides 108–121
- [def+eq: manometer] **Upright manometer:** $p = p_0 + \rho g H$. ·slides 109–110
- **U-tube** (dense fluid ρ′, e.g. Hg, for large p): $p + \rho g H = p_0 + \rho' g H'$ ⇒
  $p = p_0 + \rho' g H' - \rho g H$; for gas ρ′≫ρ ⇒ $p \approx p_0 + \rho' g H'$. Not good for fluctuating p. ·slide 111
- **Differential manometer** (pressure difference between two pipes carrying fluid ρ): ·slides 112–114
  small ΔP with lighter fluid ρ′: $p_1-p_2 = (\rho-\rho')gH$ (gas gauge ρ′: $=\rho gH$);
  large ΔP with denser fluid ρ′: $p_1-p_2 = (\rho'-\rho)gH'$ (gas ρ: $=\rho'gH'$).
- **Fluctuating-P / one wide tube:** one leg made large-area so only the narrow leg's level is read. ·slide 115
- [eq] **Inclined manometer** (minute pressures): tube at angle α, liquid travel $L$ ⇒ effective head
  $H = L\sin\alpha$; smaller α → larger, more readable L. ·slide 116
- [ex ·slides 117–118] Equal-leg U-tube across a device: $p_a - p_b = (\rho_2-\rho_1)gh$.
- [ex ·slides 119–120] Gauge B (87 kPa) → pressure at A in a water flow (ρ_w=9790, ρ_m=133100, ρ_o=8720 N/m³):
  $p_A + 490 - 9317 - 523 = 87000 \Rightarrow p_A \approx 96{,}350\ \text{Pa} \approx 96.4\ \text{kPa}$. ✓
- Small-pressure instruments: Göttingen micromanometer, Chattock tilting micromanometer. ·slide 121

## 4.7 Elastic & electric pressure gauges ·slides 122–127
- [def] **Elastic gauge:** balances fluid pressure against an elastic solid's deformation. ·slide 122
- [hist] **Bourdon tube** (Eugène Bourdon, 1808–1884; gauge invented 1849): a curved metal tube of elliptical
  cross-section, sealed & free at one end, fixed at the other; pressure rounds the cross-section and moves the
  free end, whose (amplified) motion reads the pressure. Simple, accurate, measures very high pressures. ·slides 123–125
- **Electric gauge:** pressure → diaphragm/Bourdon/bellows displacement → electrical change via wire or
  semiconductor strain gauge (piezoresistance); strain gauges suit **fluctuating** pressures. ·slides 126–127

## 4.8 Force on submerged plane surfaces & centre of pressure ·slides 128–140
- [derivation/eq: force-on-plane] Bank/gate at angle θ; strip at depth $h = y\sin\theta$ carries
  $dP = \rho g\,y\sin\theta\,dA$. Integrate with $\int_A y\,dA = y_G A$ (centroid G): ·slides 130–132
  $$\boxed{\,P = \rho g\sin\theta\,y_G A = \rho g\,h_G A\,}$$
  i.e. **total force = (pressure at the centroid) × area**.
- [derivation/eq: centre-of-pressure] The **centre of pressure C** (where the single resultant acts) sits below
  G. From moment balance $P y_C = \rho g I_x$ with $I_x = I_G + A y_G^2$: ·slides 134–140
  $$y_C = y_G + \frac{I_G}{A\,y_G}$$
  Second moments about the centroid: rectangle $I_G = \tfrac{1}{12}bh^3$, circle $I_G = \tfrac{\pi}{64}d^4$. ·slide 137
  For a vertical rectangle this gives $y_C = y_G + \dfrac{h^2}{12\,y_G}$ (C is $h^2/12y_G$ deeper than G). ·slides 138–140

## 4.9 Hoop tension — bursting a thin cylinder ·slides 141–144
- [derivation/eq: hoop-tension] Thin cylinder, diameter $d$, length $l$, internal pressure $p$. Force on the
  projected (diametral) plane $= p\,d\,l$, balanced by wall tension on the two cut edges $2Tl$:
  $$2Tl = p\,d\,l \;\Rightarrow\; \boxed{\,T = \frac{p d}{2}\,}$$
  $T$ = tension force per unit length; if the resulting tensile stress < allowable, the tank is safe (basis of
  thin-walled pressure-tank design). ·slide 144

## 4.10 Buoyancy & Archimedes' principle ·slides 145–151
- [def] Pressure over a floating body's wetted surface gives a net **upward** resultant = **buoyancy** (air
  buoyancy usually negligible). ·slides 146–147
- [derivation/eq: buoyancy] Submerged block, top/bottom at depths $h_1,h_2$, area $A$:
  $F_1 = (p_0+\rho g h_1)A$, $F_2 = (p_0+\rho g h_2)A$; net
  $$F = F_2 - F_1 = \rho g (h_2-h_1)A = \rho g\,V \qquad\text{[= weight of displaced liquid]}$$ ·slides 149–150
- [def] **Archimedes' principle:** buoyancy = weight of displaced liquid; it acts through the **centre of
  buoyancy** (centroid of the displaced volume). ·slide 151

## 4.11 Ship stability & the metacentre ·slides 152–155
- [fig/def] Ship of weight $W$ heeled by a small angle θ. The centroid **G** stays put; the centre of buoyancy
  moves **C → C′**. The vertical (buoyancy line) through C′ meets the ship's centreline at the **metacentre M**;
  **GM = metacentric height**. ·slides 152–154
- [def] **Stability criterion:** M above G ⇒ restoring couple (stable); M below G ⇒ couple increases the roll
  (unstable). ·slide 155

## 4.12 Relative equilibrium — linear acceleration ·slides 156–160
- [def] Liquid moving rigidly with its vessel (no relative flow) = **relatively stationary state**, solvable by
  statics in vessel-fixed axes. ·slide 156
- [derivation/eq: accel-free-surface] Surface element mass $m$ under gravity $-mg$ and inertial force $-m\alpha$;
  the free surface is normal to the resultant, giving ·slides 157–159
  $$\boxed{\,\tan\theta = \frac{\alpha}{g}\,}$$
  and along the vertical the usual $p = \rho\,\beta\,h$-type relation holds (β = resultant FORCE per unit mass — slide 159 defines β = F/m — numerically the resultant acceleration). ⚠ KB-FIX 2026-08-03. ·slides 159–160

## 4.13 Relative equilibrium — rigid-body rotation ·slides 161–165
- [def] Cylindrical vessel spun at constant angular velocity ω → concave (parabolic) free surface (gyrostatics). ·slide 161
- [derivation/eq: rotating-free-surface] Surface element under $-mg$ (vertical) and centrifugal $-m r\omega^2$
  (radial); resultant normal to the surface: ·slides 162–165
  $$\tan\Phi = \frac{r\omega^2}{g} = \frac{dz}{dr} \;\Rightarrow\; z = \frac{\omega^2 r^2}{2g} + c,\qquad
  \boxed{\,z - h_0 = \frac{\omega^2 r^2}{2g}\,}$$
  The free surface is a **rotating paraboloid**. ·slide 165 *(slide's intermediate "Z = ωr²/2g" drops the square
  on ω; the boxed final form is correct.)*

### Cross-references
- Hydrostatic pressure & the atmosphere build on **03-fluid-properties** (perfect gas, polytropic).
- Buoyancy/pressure feed into **06-energy-bernoulli** (static pressure) and free surfaces recur in
  **10-open-channel-flow**.

### Verification notes for this section
- 1 flag: slide 102 standard-atmosphere altitudes/temperature (logged with ISA correction).
- Verified correct: Newfound Lake 678 kPa; troposphere n=1.235; 5000 m pressures (54 kPa polytropic / 56 kPa
  isothermal); manometer example p_A≈96.4 kPa; centre-of-pressure, hoop-tension, buoyancy, tanθ=α/g, rotating
  paraboloid.
- Minor notation: slide 161 uses θ for angular velocity (later slides use ω).

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
