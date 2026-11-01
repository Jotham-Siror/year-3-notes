---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "04 — Fluid Statics"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "66-156"
file_role: topic
subtopics:
  - "pressure definition & units; absolute vs gauge"
  - "characteristics of pressure: perpendicularity, isotropy, Pascal's law, hydraulic press"
  - "pressure variation with depth in a liquid (Newfound Lake example)"
  - "pressure variation in a gas / the polytropic atmosphere; lapse rate; troposphere n; 5000 m example"
  - "pressure measurement: manometers (upright, U-tube, differential, inclined); three-liquid exercise"
  - "elastic & electric pressure gauges (Bourdon tube)"
  - "force on submerged plane surfaces; revolving gate; centre of pressure; parallel-axis theorem"
  - "worked problem: hinged inclined gate (force, wall reaction, hinge reactions); dam exercise"
  - "hoop tension / bursting a thin cylinder"
  - "buoyancy & Archimedes' principle; block-weighed-in-water example"
  - "ship stability & the metacentre; metacentric-height formula; barge example"
  - "relative equilibrium: linear acceleration (coffee-mug example) and rigid-body rotation"
key_equations: [pressure-def, hydrostatic-depth, polytropic-atmosphere, lapse-rate, manometer, force-on-plane, parallel-axis, centre-of-pressure, cp-offset-inclined, hoop-tension, buoyancy, metacentric-height, accel-free-surface, rotating-free-surface]
prerequisites: ["03-fluid-properties (density, perfect gas, polytropic)"]
leads_to: ["06-energy-bernoulli", "10-open-channel-flow"]
verification_flags: 16
tags: [statics, pressure, gauge, pascal, manometer, bourdon, centre-of-pressure, buoyancy, archimedes, metacentre, relative-equilibrium]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTATION: deck uses p = pressure and P (capital) = pressure FORCE in some slides, and elsewhere P = pressure.
  This KB uses p for pressure and F/P_force for force where the slide means force; noted where it matters.
  EDITION: slide numbers are the Oct 2026 edition (561 pp.). "old slide N" = Jul 2026 edition only.
  EXPORT NOTE: the Oct 2026 PDF loses many superscripts — a blank gap is printed where an exponent stood
  (e.g. slide 128 "h  /12y_G", slide 147 "1/12 bL", slide 156 "ω²r /2g", units "lbf/ft", "m/s"). The arithmetic on
  those slides uses the exponent, so this KB writes it in and does not flag the gap as a lecturer error. -->

# 04 — Fluid Statics

Balance of forces in fluids at rest — including "relative rest" (liquid moving rigidly with its vessel, e.g.
steady acceleration or rotation), which is analysed as a statics problem in vessel-fixed coordinates. ·slide 67
(Section title slide ·slide 66.)

## 4.1 Pressure: definition & units ·slides 68–69
- [eq: pressure-def] Uniform load: $p = F/A$ (F = pressure force). Non-uniform:
  $p = \lim_{\Delta A\to0}\dfrac{\Delta F}{\Delta A} = \dfrac{dF}{dA}$. ·slide 68 *(the Oct 2026 edition writes the
  force as F; the Jul 2026 edition wrote capital P.)*
- Units: SI **pascal** (Pa); also bar, or metres of water column (mH₂O). Standard atmosphere:
  $1\ \text{atm} = 760\ \text{mmHg} = 101{,}325\ \text{Pa}$ (at 273.15 K, g = 9.80665 m/s²). ·slide 69

## 4.2 Absolute vs gauge pressure ·slide 70
- [def] Referenced to a **perfect vacuum** → **absolute** pressure; referenced to **atmospheric** → **gauge**
  pressure. $p_\text{gauge} = p_\text{abs} - p_\text{atm}$ (negative gauge = below atmospheric).

## 4.3 Characteristics of pressure ·slides 71–75
1. [def] Fluid pressure always acts **perpendicular** to the wall in contact. ·slide 71
2. [def] Pressure at a point in a fluid at rest is **equal in all directions** (isotropic). ·slides 71, 72–73
   [derivation] Small triangular prism of unit width, faces $dA, dA_1, dA_2$ with pressures $p, p_1, p_2$; with
   geometry $dA_1 = dA\sin\theta$, $dA_2 = dA\cos\theta$ and the weight term second-order (negligible), force
   balance gives $p_1 = p_2 = p$ for any θ. ·slides 72–73
3. [def] **Pascal's law:** pressure applied to a confined fluid transmits undiminished to all parts. ·slides 71, 74
   [eq] Hydraulic press: small piston $p = F_1/A_1$; large piston $F_2 = pA_2 = F_1\,A_2/A_1$ (force amplification). ·slide 75

## 4.4 Pressure variation with depth — liquid ·slides 76–81
- [derivation] Vertical column, area $dA$: balance of bottom pressure, top pressure $p+(dp/dz)dz$, and weight
  $\rho g\,dA\,dz$ gives $\dfrac{dP}{dz} = -\rho g$, i.e. $dP = -\rho g\,dz$. ·slides 77–78
- [eq: hydrostatic-depth] Integrating (p = p₀ at z = z₀): ·slide 79
  $$p = p_0 + \rho g (z_0 - z) = p_0 + \rho g h \qquad\text{(pressure rises with depth } h)$$
  *(S5 fixed in the Oct 2026 edition — slide 79 now ends "P = p₀ + ρgh"; the Jul 2026 edition dropped the p₀.)*
- [ex ·slides 80–81] Newfound Lake, max depth 60 m, mean atmospheric 91 kPa, specific weight
  $\gamma_{\text{water}} = 9790$ N/m³ (this is $\rho g$ already):
  $$p_{\max} = 91{,}000 - (9790)(-60) = 678{,}400\ \text{Pa} \approx 678\ \text{kPa}$$
  ✓ (sign convention as printed: z measured upward from the surface, so the depth enters as −60 m.)
  > ⚠ VERIFY S37 ·slide 81 — the Oct 2026 edition multiplies by g a second time: "pmax = 91,000 Pa −
  > (9790 N/m³)(−60 m)(9.81) = 678,400(9.81) Pa ≈ 678 (9.81) kPa". Since γ = 9790 N/m³ already contains g,
  > the extra (9.81) is wrong — and the line is not even self-consistent
  > ($91{,}000 + 9790\cdot60\cdot9.81 = 5.85\times10^6$, while $678{,}400\times9.81 = 6.66\times10^6$).
  > Correct answer unchanged: **678 kPa**
  > (the Jul 2026 edition printed it correctly).

## 4.5 Pressure variation in a gas — the polytropic atmosphere ·slides 82–93
- [derivation] Gas density varies with p; assume a polytropic change $p v^{n} = \text{const}$, i.e.
  $p/\rho^{n} = p_0/\rho_0^{n}$, so $\rho = \rho_0 (p/p_0)^{1/n}$. Substituting into $dP/dz = -\rho g$ and
  integrating from sea level (z=0, p₀, ρ₀): ·slides 82–87
  The Oct 2026 edition reworks the middle of this derivation over two new slides:
  - ·slide 83 (new): separate variables and non-dimensionalise —
    $$dP = -\Big(\frac{P}{P_0}\Big)^{1/n}\rho_0 g\,dz
    \;\Rightarrow\; dz = -\frac{1}{g}\,\frac{P_0}{\rho_0}\Big(\frac{P_0}{P}\Big)^{1/n} d\Big(\frac{P}{P_0}\Big)$$
    (multiply through by $P_0/P_0$ so the variable is $x = P/P_0$). Every step checks.
  - ·slides 84–85 (85 new): integrate with $\int x^{a}dx = \dfrac{x^{a+1}}{a+1}$, $a = -1/n$, so
    $\dfrac{1}{1-1/n} = \dfrac{n}{n-1}$, then rearrange for $P/P_0$.
  - [added] Clean version of the integration (limits $x = 1$ at $z = 0$ to $x = P/P_0$ at $z$):
    $$z = -\frac{1}{g}\frac{P_0}{\rho_0}\int_{1}^{P/P_0} x^{-1/n}\,dx
        = -\frac{1}{g}\frac{P_0}{\rho_0}\,\frac{n}{n-1}\Big[\Big(\frac{P}{P_0}\Big)^{\frac{n-1}{n}} - 1\Big]$$
    $$\Big(\frac{P}{P_0}\Big)^{\frac{n-1}{n}} = 1 - \frac{n-1}{n}\,\frac{\rho_0 g}{P_0}\,z$$
  > ⚠ VERIFY S38 ·slides 84–85 — the constant of integration is handled wrongly, so the middle lines do not
  > follow from each other (the end result is right). Slide 84 prints "At z = 0; P/P₀ = P₀/P₀; or, c = P₀/P₀ = 1"
  > and "Z = −(1/g)(P₀/ρ₀)·[(n/(n−1))(P/P₀)^{(n−1)/n} + 1]"; setting $z = 0$, $P/P_0 = 1$ in that line gives
  > $0 = -\frac{1}{g}\frac{P_0}{\rho_0}\big(\frac{n}{n-1}+1\big) \neq 0$. The bracket must be
  > $\frac{n}{n-1}\big[(P/P_0)^{(n-1)/n} - 1\big]$. Slide 85 then keeps "+ 1" after multiplying by $(n-1)/n$, and
  > its line "[1 − g(ρ₀/P₀)z]·(n−1)/n = (P/P₀)^{n−1/n}" puts $(n-1)/n$ on the 1 as well; only the z-term carries it.
  > The boxed result below (last line of slide 85, top of slide 86) is correct. The same constant slip was on
  > old slides 97–98.
  $$\boxed{\;\frac{p(z)}{p_0} = \Big[\,1 - \frac{n-1}{n}\,\frac{\rho_0 g}{p_0}\,z\,\Big]^{\frac{n}{n-1}}\;}
  \qquad\text{[eq: polytropic-atmosphere]}$$
  $$\frac{\rho(z)}{\rho_0} = \Big[\,1 - \frac{n-1}{n}\,\frac{\rho_0 g}{p_0}\,z\,\Big]^{\frac{1}{n-1}}$$
  (density from $\rho/\rho_0 = (P/P_0)^{1/n}$; exponent $\frac{n}{n-1}\cdot\frac{1}{n} = \frac{1}{n-1}$ ·slide 86)
  > ⚠ VERIFY S3 ·slides 86–87 — *changed in the Oct 2026 edition.* Slide 87's bracket is **fixed** (now
  > "[1 − ((n−1)/n)ρ₀g/P₀ z]"), and slide 86's pressure lines are correct. But slide 86's final density line now
  > prints "ρ(z)/ρ₀ = [1 − ((n−1)/n) g z **P₀/ρ₀**]^{1/(n−1)}" — the ratio is upside down (the Jul 2026 edition
  > printed "P₀gz"). Check: $(\rho_0/P_0)gz$ is dimensionless; $(P_0/\rho_0)gz$ has units m⁴/s⁴. Use $\rho_0 g/p_0$.
- [eq: lapse-rate] Using $p = \rho R T$, the temperature falls linearly (constant lapse rate): ·slides 87–88
  $$\frac{T(z)}{T_0} = 1 - \frac{n-1}{n}\frac{\rho_0 g}{p_0}z,\qquad
  \frac{dT}{dz} = -\frac{n-1}{n}\frac{g}{R}$$
- **Standard sea-level conditions** (aeronautics): $p_0 = 101.325$ kPa, $T_0 = 288.15$ K, $\rho_0 = 1.225$ kg/m³. ·slide 88
  > ⚠ VERIFY ·slide 89 — slide: "temperature decreases 0.65 °C/100 m in the troposphere **up to ≈1 km**, then
  > constant at **−50.5 °C from 1 km to 10 km**." Per the International Standard Atmosphere the 6.5 °C/km lapse
  > runs through the **whole troposphere to ≈11 km**, reaching ≈ **−56.5 °C** at the tropopause; the isothermal
  > (−56.5 °C) layer is the lower stratosphere, **≈11–20 km**. The slide's 1 km / 10 km / −50.5 °C appear to be
  > digit errors (11 km / 20 km / −56.5 °C). See _verification-log.md. *(Still printed in the Oct 2026 edition —
  > slide 89 also asks for n "at the troposphere (less than 1Km)".)*
- [ex ·slides 89–90] Troposphere polytropic index from the lapse rate and the standard $p_0 = 101.325$ kPa,
  $T_0 = 288.15$ K, $\rho_0 = 1.225$ kg/m³, $g = 9.80665$ m/s². The Oct 2026 edition now works it on slide 90
  (the Jul 2026 edition only stated the result):
  $$-0.0065 = -\frac{n-1}{n}\cdot\frac{(1.225)(9.80665)(288.15)}{101{,}325} = -0.034\,\frac{n-1}{n}$$
  $$-0.0065\,n = -0.034\,n + 0.034 \;\Rightarrow\; n = 1.23496 \approx \mathbf{1.235}$$
  ✓ Unrounded $\rho_0 g T_0/p_0 = 0.03416$ gives $n = 1.2350$; carrying the slide's rounded 0.034 gives 1.236 —
  the printed 1.23496 comes from the unrounded value. Same as $(n-1)/n = (dT/dz)R/g = 0.0065\cdot287/9.807 = 0.190$.
  *(S4 fixed in the Oct 2026 edition — slide 90 no longer prints the lapse rate as "0.0065 K/100"; the
  value enters as 0.0065 with no unit written; slide 89 gives 0.65 °C per 100 m and slide 91 gives
  B = 0.00650 K/m.)*
- [ex ·slides 91–93] Pressure at 5000 m if sea-level pressure is 101,350 Pa, (a) by
  $P = P_0\{1 - (dT/dz)z/T_0\}^{g/RB}$, (b) isothermal at 15 °C, $P = P_0 e^{-gz/RT}$; is the isothermal
  approximation adequate? The Oct 2026 edition gives $R = 287$ m²/s²·K, $g = 9.80665$ m/s², lapse rate
  $B = 0.00650$ K/m and computes the exponent (the Jul 2026 edition simply said "take $g/RB = 5.26$"):
  $$\frac{g}{RB} = \frac{9.807}{(287)(0.0065)} = 5.26$$
  $$p = 101{,}350\Big[1-\frac{(0.0065)(5000)}{288.16}\Big]^{5.26} = 101{,}350\,(0.8872)^{5.26} = 101{,}350\,(0.5328) \approx 54{,}000\ \text{Pa}$$
  $$p \approx p_0 e^{-gz/RT} = 101{,}350\,e^{-\frac{(9.807)(5000)}{(287)(288.16)}} = 101{,}350\,e^{-0.5929} \approx 56{,}000\ \text{Pa}$$
  Isothermal overestimates by ~2 kPa (adequate as a rough approximation). ✓ (recomputed: 54,008 Pa and 56,018 Pa)
  > ⚠ VERIFY S39 ·slide 92 — prints "g/RB = **9.087** m/s² / 287 m²/s².K × 0.0065 K/m = 5.26". Digits swapped:
  > g = 9.807. Check: $9.087/1.8655 = 4.87$, but $9.807/1.8655 = 5.26$, the value the slide uses.
  *(S6 fixed in the Oct 2026 edition — slides 91 and 93 now print $P \approx P_0 e^{-gZ/RT}$ with the minus sign.)*

## 4.6 Pressure measurement — manometers ·slides 94–108
- [def+eq: manometer] **Upright manometer:** $p = p_0 + \rho g H$. ·slides 95–96
- **U-tube** (dense fluid ρ′, e.g. Hg, for large p): $p + \rho g H = p_0 + \rho' g H'$ ⇒
  $p = p_0 + \rho' g H' - \rho g H$; for gas ρ′≫ρ ⇒ $p \approx p_0 + \rho' g H'$. Not good for fluctuating p. ·slide 97
- **Differential manometer** (pressure difference between two pipes carrying fluid ρ): ·slides 98–100
  small ΔP with lighter fluid ρ′: $p_1-p_2 = (\rho-\rho')gH$ (gas gauge ρ′: $=\rho gH$);
  large ΔP with denser fluid ρ′: $p_1-p_2 = (\rho'-\rho)gH'$ (gas ρ: $=\rho'gH'$).
- **Fluctuating-P / one wide tube:** one leg made large-area so only the narrow leg's level is read. ·slide 101
- [eq] **Inclined manometer** (minute pressures): tube at angle α, liquid travel $L$ ⇒ effective head
  $H = L\sin\alpha$; smaller α → larger, more readable L. ·slide 102
  > ⚠ VERIFY S2 ·slide 102 — still printed in the Oct 2026 edition: "The smaller the α, the larger the H." With
  > $H = L\sin\alpha$ a smaller α gives a *smaller* H for a given L. The intended point: for a **given H**, a smaller
  > α gives a **longer L**, which is easier to read.
- [ex ·slides 103–104] Equal-leg U-tube across a device: $p_a - p_b = (\rho_2-\rho_1)gh$.
- [ex ·slides 105–106] Gauge B (87 kPa) → pressure at A in a water flow, fluids at 20 °C. Specific weights
  (the slide writes γ = ρg): $\gamma_w = 9790$, $\gamma_m = 133{,}100$, $\gamma_o = 8720$ N/m³:
  $$p_A + (9790)(0.05) - (133{,}100)(0.07) - (8720)(0.06) = 87{,}000$$
  $$p_A + 490 - 9317 - 523 = 87{,}000 \;\Rightarrow\; p_A \approx 96{,}350\ \text{Pa} \approx 96.4\ \text{kPa}$$
  ✓ (recomputed: 489.5, 9317, 523.2 → 96,350.7 Pa)
- [exercise ·slide 107] (new in the Oct 2026 edition) Three-liquid system: compute $h_1$ and $h_2$; neglect air
  density; use the specific weights given earlier.
  [fig] Three vertical tubes, open at the top, joined along the bottom by one tube full of mercury. Left tube:
  27 cm of water sitting on a mercury column of height $h_1$ (measured from the bottom). Middle tube: mercury
  only, 8 cm above the bottom. Right tube: 5 cm of mercury with a column $h_2$ of oil, SG = 0.78, on top.
  - [added] Worked answer. Pressure at the common bottom level is the same under all three tubes:
    $$\gamma_w(0.27) + \gamma_m h_1 = \gamma_m(0.08) = \gamma_m(0.05) + \gamma_o h_2$$
    with $\gamma_w = 9790$, $\gamma_m = 133{,}100$ N/m³ (·slide 105) and $\gamma_o = 0.78\times9790 = 7636$ N/m³:
    $$h_1 = 0.08 - \frac{(9790)(0.27)}{133{,}100} = 0.08 - 0.0199 = 0.0601\ \text{m} \approx \mathbf{6.0\ cm}$$
    $$h_2 = \frac{(133{,}100)(0.08-0.05)}{7636} = 0.523\ \text{m} \approx \mathbf{52.3\ cm}$$
    (checked in Python; SG(Hg) = 13.6 with $\gamma_w = 9810$ gives the same 6.0 cm and 52.3 cm.)
- Small-pressure instruments: Göttingen micromanometer, Chattock tilting micromanometer. ·slide 108

## 4.7 Elastic & electric pressure gauges ·slides 109–113
- [def] **Elastic gauge:** balances fluid pressure against an elastic solid's deformation. ·slide 109
- [hist] **Bourdon tube** (Eugène Bourdon, 1808–1884; gauge invented 1849): a curved metal tube of elliptical
  cross-section, sealed & free at one end, fixed at the other; pressure rounds the cross-section and moves the
  free end, whose (amplified) motion reads the pressure. Simple, accurate, measures very high pressures. ·slides 110–112
- **Electric gauge:** pressure → diaphragm/Bourdon/bellows displacement → electrical change via wire or
  semiconductor strain gauge (piezoresistance); strain gauges suit **fluctuating** pressures. ·slide 113

## 4.8 Force on submerged plane surfaces & centre of pressure ·slides 114–133
- Section title ·slide 114 (new). Motivating questions: force on a dam bank, a sluice gate or a tank wall; the
  torque needed to open a sluice gate; the force needed to tear open a pressurised cylinder. ·slides 115–116
- ·slide 117 (new) is only a video link, on the **Solai dam** case. No content to learn from the slide itself.
- [derivation/eq: force-on-plane] Bank/gate at angle θ to the water surface, atmospheric pressure disregarded;
  strip at depth $h = y\sin\theta$ carries $dP = \rho g\,y\sin\theta\,dA$. Integrate with $\int_A y\,dA = y_G A$
  (centroid G, depth $h_G$): ·slides 118–119
  $$\boxed{\,P = \rho g\sin\theta\,y_G A = \rho g\,h_G A\,}$$
  i.e. **total force = (pressure at the centroid) × area**.
  > ⚠ VERIFY S40 ·slide 119 — new lines in the Oct 2026 edition strike out ρg ("P = ~~ρg~~ sin θ y_G A =
  > ~~ρg~~h_G A") and then state "P = sin θ y_G A = h_G A → P = the product of P at the centroid G and the
  > underwater area". Without ρg, $h_G A$ has units m³, not N — it is a volume, not a force. Keep
  > $P = \rho g h_G A$. (The words "P at the centroid" mean the *pressure* at the centroid, $\rho g h_G$.)
- [fig/def] **Revolving gate** ·slides 120–121 (new): a vertical rectangular sluice gate hinged on a horizontal
  axis x at the water surface (top edge); the water force P acts at the centre of pressure C, below the centroid
  G, and a force F at the bottom edge holds the gate shut. Question set: the torque about the turning (x) axis.
- [derivation/eq: centre-of-pressure] Moment of the strip force about x is $(\rho g\,y\,dA)\,y$, so the total
  moment is $\rho g\int_A y^2\,dA = \rho g I_x$. The **centre of pressure C** is where the single resultant P gives
  the same moment: ·slides 121–123
  $$P\,y_C = \rho g I_x$$
  > ⚠ VERIFY S7 ·slide 121 — still printed in the Oct 2026 edition (it has moved from the slide numbered 122
  > to 121): "Force acting on a minute area dA = ρg**y_G** dA". The strip force is $\rho g\,y\,dA$ for a vertical
  > gate ($\rho g\,y\sin\theta\,dA$ in general) — the strip's own y, not the centroid's.
  > ⚠ VERIFY S41 ·slides 122–123 — new wording in the Oct 2026 edition takes $y^2$ out of the integral: "Total
  > moment on the gate = ∫ρgy² dA = ρg **y²∫dA**" and the title of 123 "ρg y² ∫dA; **ρg y²A = I_x**". y varies over
  > the gate, so it cannot leave the integral, and $I_x$ has no ρg in it. Correct: $\rho g\int_A y^2\,dA = \rho g I_x$
  > with $I_x = \int_A y^2\,dA$ (the Jul 2026 edition had this right).
- [def/eq: parallel-axis] **Parallel-axis theorem** ·slides 123–124 (124 new): the second moment about any axis
  equals that about the parallel axis through the centroid plus area × (distance between the axes)²:
  $$I_x = I_G + A\,y_G^2$$
  > ⚠ VERIFY S42 ·slide 124 — prints "Ix = I_G + Ay_G" (no square; this is not an export gap — there is no
  > space for an exponent). Units: $A y_G$ is m³ but $I$ is m⁴. Slide 123 prints it correctly with $y_G^2$.
- Substituting into $P y_C = \rho g I_x$ with $P = \rho g y_G A$ (vertical gate):
  $$\boxed{\,y_C = y_G + \frac{I_G}{A\,y_G}\,}$$
  Second moments about the centroid: rectangle $I_G = \tfrac{1}{12}bh^3$, circle $I_G = \tfrac{\pi}{64}d^4$. ·slide 125
  For a vertical rectangle this gives $y_C = y_G + \dfrac{h^2}{12\,y_G}$ (C is $h^2/12y_G$ deeper than G). ·slides 123, 133
  > ⚠ VERIFY S8 ·slide 133 — still printed in the Oct 2026 edition: "y_c = y_G + h²/12h_G; h_G is substituted for
  > y_G". That swap is valid only for a vertical surface (θ = 90°); for an inclined plane y is measured **along the
  > plane** from the line where the plane meets the free surface, and $y_G = h_G/\sin\theta$.
- [added] [eq: cp-offset-inclined] For an inclined plane, the same result written with depths: the centre of
  pressure lies a distance $l$ below the centroid, measured along the plane,
  $$l = y_C - y_G = \frac{I_G\sin\theta}{h_G\,A}$$
  where $I_G$ is about the centroidal axis. This is the form the gate problem below needs.

- [ex ·slides 126–131] (new in the Oct 2026 edition) **Hinged inclined gate.**
  [fig] A gate AB, 10 ft long and 5 ft wide, hinged at its lower end B on the bottom, leans up against a smooth
  vertical wall at A. Seawater, $\gamma = 64$ lbf/ft³, stands 15 ft deep above B. A is 6 ft higher than B and
  8 ft from it horizontally, so $\sin\theta = 0.6$, $\cos\theta = 0.8$. Atmospheric pressure acts on both sides
  and is neglected. Find (a) the water force on the gate, (b) the horizontal force P from the wall at A,
  (c) the hinge reactions at B.
  - (a) ·slide 127 — centroid halfway along, 3 ft above B, so $h_{CG} = 15 - 3 = 12$ ft; $A = 5\times10 = 50$ ft²:
    $$F = \gamma h_{CG} A = (64)(12)(50) = 38{,}400\ \text{lbf}$$
    ✓
  - (b) ·slides 128–130 — the slide finds the centre of pressure, then takes moments about B
    (clockwise = anticlockwise): $P\,(L\sin\theta) = F \times (\text{distance from B to CP})$.
  - (c) ·slide 131 — $\sum F_x = 0 = B_x + F\sin\theta - P$; $\sum F_z = 0 = B_z - F\cos\theta$, giving
    $B_z = (38{,}400)(0.8) = 30{,}720 \approx 30{,}700$ lbf ✓.
  > ⚠ VERIFY S43 ·slides 128–131 — **the centre of pressure is put in the wrong place, so P and B_x are wrong.**
  > Slide 128 prints "Yc = y_G + h²/12y_G = 5 ft + (10 ft)²/(12 × 5 ft) = 5 ft + 1.667 ft = 6.667 ft", then
  > slide 130 "Dist from B: 10 − 6.667 ft = 3.333 ft … P(10)(6/10) = (38,400)(3.333) = 128064 … P = 21,344 lbf",
  > and slide 131 "B_x = 1696 lbf". The "OR" route on slide 129 makes the same error another way: it uses
  > $I_{xx} = bL^3/12 + A(5)^2 = 1665$ ft⁴ (an axis at the gate's end) in $l = I\sin\theta/(h_{CG}A)$ and gets
  > l = 1.665 ft. **Why it is wrong:** in $y_C = y_G + I_G/(Ay_G)$, y is measured along the plane **from the free
  > surface**, not from the end of the gate. Here $y_G = h_{CG}/\sin\theta = 20$ ft, not 5 ft; and the $l$ formula
  > takes $I_G$ about the centroid (416.7 ft⁴), not about an end. Repeatable check: both routes must agree with
  > $y_C - y_G = \dfrac{10^2}{12\times20} = \dfrac{(416.7)(0.6)}{(12)(50)} = 0.417$ ft.
  - [added] Corrected (b) and (c):
    $$l = \frac{I_G\sin\theta}{h_{CG}A} = \frac{\tfrac{1}{12}(5)(10)^3\,(0.6)}{(12)(50)} = \frac{(416.7)(0.6)}{600} = 0.417\ \text{ft}$$
    CP is $5 - 0.417 = 4.583$ ft up the gate from B. Moments about B (P acts 6 ft above B):
    $$P\,(10)(0.6) = (38{,}400)(4.583) \;\Rightarrow\; P = 29{,}333 \approx \mathbf{29{,}300\ lbf}$$
    $$B_x = P - F\sin\theta = 29{,}333 - 23{,}040 = 6{,}293 \approx \mathbf{6{,}300\ lbf}, \qquad
      B_z = F\cos\theta = \mathbf{30{,}700\ lbf}$$
    (checked in Python. Note too that the slide's own numbers give $B_x = 21{,}344 - 23{,}040 = -1{,}696$ lbf —
    it prints +1696, dropping the sign; and $128{,}064/38{,}400 = 3.335$, not 3.333 — both minor beside S43.)

- [exercise ·slide 132] (new in the Oct 2026 edition) A dam 20 m long holds back 7 m of water. Find the total
  resultant force on the dam and where the centre of pressure is. "Take γ = 9.79 N/m".
  [fig] Rubble dam with a straight upstream face sloping at 60° to the horizontal base; water 7 m deep against
  that face; the resultant F acts normal to the face at depth $h_{cp}$ below the surface.
  > ⚠ VERIFY S44 ·slide 132 — "γ = 9.79 N/m": the unit should be **kN/m³** (water is 9790 N/m³).
  - [added] Worked answer. Wetted length of the face $L_s = 7/\sin60^\circ = 8.083$ m; area
    $A = 20\times8.083 = 161.7$ m²; centroid depth $h_G = 3.5$ m:
    $$F = \gamma h_G A = (9790)(3.5)(161.7) = 5.54\times10^{6}\ \text{N} \approx \mathbf{5.54\ MN}$$
    Measured along the face from the surface, $y_G = 4.041$ m and
    $$y_C = y_G + \frac{L_s^2}{12\,y_G} = 4.041 + \frac{(8.083)^2}{12(4.041)} = 4.041 + 1.347 = 5.389\ \text{m}$$
    $$h_{cp} = y_C\sin60^\circ = 4.67\ \text{m} \;(= \tfrac{2}{3}\times7\ \text{m, as for any plane reaching the surface})$$
    (checked in Python; horizontal and vertical parts 4.80 MN and 2.77 MN.)

## 4.9 Hoop tension — bursting a thin cylinder ·slides 134–136
- [derivation/eq: hoop-tension] Thin cylinder, diameter $d$, length $l$, internal pressure $p$. Force on the
  projected (diametral) plane $= p\,d\,l$, balanced by wall tension on the two cut edges $2Tl$:
  $$2Tl = p\,d\,l \;\Rightarrow\; \boxed{\,T = \frac{p d}{2}\,}$$
  $T$ = tension force per unit length; if the resulting tensile stress < allowable, the tank is safe (basis of
  thin-walled pressure-tank design). ·slide 136

## 4.10 Buoyancy & Archimedes' principle ·slides 137–143
- [def] Pressure over a floating body's wetted surface gives a net **upward** resultant = **buoyancy** (air
  buoyancy usually negligible). ·slides 137–138
- [derivation/eq: buoyancy] Submerged block, top/bottom at depths $h_1,h_2$, area $A$; horizontal pressures
  cancel:
  $F_1 = (p_0+\rho g h_1)A$, $F_2 = (p_0+\rho g h_2)A$; net ·slides 139–140
  $$F = F_2 - F_1 = \rho g (h_2-h_1)A = \rho g\,V \qquad\text{[= weight of displaced liquid]}$$
- [def] **Archimedes' principle:** a floating or submerged body feels a buoyancy equal to the weight of liquid
  it displaces ·slide 140; it acts through the **centre of buoyancy**, the centre of gravity of the displaced
  liquid ·slide 141 (a new title slide for the principle in the Oct 2026 edition; the Jul 2026 edition had this
  sentence on the floating-cube slide).
- [ex ·slides 142–143] (new in the Oct 2026 edition) A block weighs 100 lbf in air and 60 lbf when immersed in
  fresh water ($\gamma = 62.4$ lbf/ft³). Find its average specific gravity ("specific density" on the slide).
  $$\sum F_z = 0 = 60 + F_B - 100 \;\Rightarrow\; F_B = 40\ \text{lbf} = \gamma V$$
  $$V = \frac{40}{62.4} = 0.641\ \text{ft}^3, \qquad \gamma_{\text{block}} = \frac{100}{0.641} = 156\ \text{lbf/ft}^3$$
  ✓ [added] The slide stops at the specific weight; the specific gravity asked for is
  $156/62.4 = \mathbf{2.50}$.

## 4.11 Ship stability & the metacentre ·slides 144–148
- [fig/def] Ship of weight $W$ heeled by a small angle θ. The centroid **G** stays put; the centre of buoyancy
  moves **C → C′**. The vertical (buoyancy line) through C′ meets the ship's centreline at the **metacentre M**;
  **GM = metacentric height**. ·slides 144–145 (the Oct 2026 figures label the centre of buoyancy **B**, B′
  rather than C, C′. Watch the letters: C is also the centre of pressure in §4.8, and B is also the hinge in the
  §4.8 gate problem and the lapse rate in §4.5.)
- [def] **Stability criterion:** M above G ⇒ restoring couple (stable); M below G ⇒ couple increases the roll
  (unstable). ·slide 145
- [eq: metacentric-height] (new in the Oct 2026 edition) ·slide 146
  $$\boxed{\,\overline{MG} = \frac{I_o}{V_{\text{sub}}} - \overline{GB}\,}$$
  $I_o$ = second moment of the **waterline area** about the tilt axis O (m⁴); $V_{\text{sub}}$ = submerged volume
  (m³); $\overline{GB}$ = distance from G down to the centre of buoyancy B (m). Keep $\overline{MG}$ positive
  for stability.
- [ex ·slides 147–148] (new) **Barge.** Uniform rectangular section, width $2L$, draft $H$, length $b$ (the
  solution slide calls b the "width" and 2L the "length"; the formula is the same). (a) metacentric height for a
  small tilt; (b) range of L/H for static stability ("statistically stable" on the slide) if G is exactly at the
  water line.
  $$I_o = \frac{b(2L)^3}{12} = \frac{8bL^3}{12}, \qquad V_{\text{sub}} = 2LbH, \qquad \overline{GB} = \frac{H}{2}$$
  $$\overline{MG} = \frac{8bL^3/12}{2LbH} - \frac{H}{2} = \frac{L^2}{3H} - \frac{H}{2}$$
  Stable if $\overline{MG} > 0$: $L^2 > \tfrac{3}{2}H^2$, i.e. $L > 1.225H$, or $2L > 2.45H$. ✓
  > ⚠ VERIFY S45 ·slide 148 — the text says "b) for stability, MG needs to be **> GB**". The criterion is
  > $\overline{MG} > 0$ (equivalently $I_o/V_{\text{sub}} > \overline{GB}$). Check: $\overline{MG} > \overline{GB}$
  > would give $L^2/3H > H$, i.e. $L > 1.73H$ — not the slide's own answer $2L > 2.45H$, which follows from
  > $\overline{MG} > 0$.

## 4.12 Relative equilibrium — linear acceleration ·slides 149–153
- [def] Liquid moving rigidly with its vessel (no relative flow) = **relatively stationary state**, solvable by
  statics in vessel-fixed axes. ·slide 149
- [derivation/eq: accel-free-surface] Surface element mass $m$ under gravity $-mg$ and inertial force $-m\alpha$;
  the free surface is normal to the resultant, giving ·slides 150–151
  $$\boxed{\,\tan\theta = \frac{\alpha}{g}\,}$$
  and along the vertical the usual $p = \rho\,\beta\,h$-type relation holds (β = resultant FORCE per unit mass — slide 151 defines β = F/m — numerically the resultant acceleration). ⚠ KB-FIX 2026-08-03. ·slide 151
  *(Slide 151 still prints "β = F/m" in the Oct 2026 edition; the KB-FIX stands.)*
- [ex ·slides 152–153] (new in the Oct 2026 edition) **Coffee mug on an accelerating tray.** A racer rests her
  coffee mug on a horizontal tray while she accelerates at $a_x = 7$ m/s². The mug is 10 cm deep and 6 cm in
  diameter and holds coffee 7 cm deep at rest. Assuming rigid-body acceleration, will it spill?
  [fig] Mug with 3 cm of free board above the 7 cm rest level; the tilted surface pivots about the mug's centre
  line, rising by Δz at the rear wall, 3 cm (the radius) from the centre.
  $$\theta = \tan^{-1}\frac{a}{g} = \tan^{-1}\frac{7.0}{9.81} = 35.5^\circ$$
  The mug is symmetric, so the tilted surface passes through the centre of the rest level:
  $$\Delta z = (3\ \text{cm})\tan35.5^\circ = 2.14\ \text{cm} < 3\ \text{cm} \;\Rightarrow\; \text{no spill}$$
  ✓ (recomputed: 35.51°, 2.141 cm)
  > ⚠ VERIFY S46 ·slides 147, 152 — cosmetic wording slips new in the Oct 2026 edition: slide 152 "A **dog**
  > racer" (a *drag* racer), slide 147 "**statistically** stable" (*statically* stable).

## 4.13 Relative equilibrium — rigid-body rotation ·slides 154–156
- [def] Cylindrical vessel spun at constant angular velocity ω → concave (parabolic) free surface (gyrostatics);
  work in cylindrical coordinates $(r, \theta, z)$. ·slide 154
- [derivation/eq: rotating-free-surface] Surface element under $-mg$ (vertical) and centrifugal $-m r\omega^2$
  (radial); resultant normal to the surface: ·slides 154–156
  $$\tan\Phi = \frac{r\omega^2}{g} = \frac{dz}{dr} \;\Rightarrow\; z = \frac{\omega^2 r^2}{2g} + c,\qquad
  \boxed{\,z - h_0 = \frac{\omega^2 r^2}{2g}\,}$$
  The free surface is a **rotating paraboloid**. ·slide 156 *(Fixed in the Oct 2026 edition: the Jul 2026 slide's
  intermediate "Z = ωr²/2g" dropped the square on ω. Slide 156 now prints "Z = ω²r /2g + c" and
  "Z − ho = ω² * r /2g" — ω² is there, and the gap after r is a lost superscript (export), so read $r^2$.)*
  > ⚠ VERIFY S9 ·slide 155 — still printed in the Oct 2026 edition: "−mrω² due to the **centripetal**
  > acceleration rω²". In axes turning with the vessel the force on the element is the outward **centrifugal**
  > inertial force $m r\omega^2$; a centripetal force points inward and would tilt the surface the wrong way.

### Cross-references
- Hydrostatic pressure & the atmosphere build on **03-fluid-properties** (perfect gas, polytropic).
- Buoyancy/pressure feed into **06-energy-bernoulli** (static pressure) and free surfaces recur in
  **10-open-channel-flow**.

### Verification notes for this section
- Checked against the Oct 2026 edition (pages 66–156, every page read from the rendered image).
- 16 inline flags still standing: slide 89 standard atmosphere; S2, S3 (changed, still wrong on slide 86), S7,
  S8, S9 from the second-pass audit; and S37–S46 found in the Oct 2026 edition (XB IDs are placeholders until
  logged). Most serious: **S43** (hinged-gate problem — wrong centre of pressure, so P and B_x are wrong) and
  **S37** (Newfound Lake answer multiplied by g twice).
- Fixed in the Oct 2026 edition: S4 (lapse-rate unit), S5 (p₀ dropped), S6 (exponent sign), the ω/θ notation on
  slide 154, and the missing square on ω on slide 156.
- Verified correct (recomputed): Newfound Lake 678 kPa; troposphere n = 1.235; 5000 m pressures (54,008 Pa
  polytropic / 56,018 Pa isothermal); manometer p_A ≈ 96.4 kPa; three-liquid h₁ = 6.0 cm, h₂ = 52.3 cm [added];
  gate F = 38,400 lbf and B_z = 30,700 lbf; dam 5.54 MN at 4.67 m depth [added]; block γ = 156 lbf/ft³,
  SG 2.50; barge 2L > 2.45H; mug 35.5°, Δz = 2.14 cm; centre-of-pressure, hoop-tension, buoyancy, tanθ = a/g,
  rotating paraboloid.
- Slide 154's notation is fixed: the Jul 2026 edition used θ for angular velocity; the Oct 2026 edition uses ω,
  and θ only as the cylindrical-coordinate angle.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
