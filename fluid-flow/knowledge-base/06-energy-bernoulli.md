---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "06 — Conservation of Energy & Bernoulli's Equation"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "205-255"
file_role: topic
subtopics:
  - "energy forms in a fluid (PE, KE, pressure energy)"
  - "Euler's equation of motion (1-D, inviscid)"
  - "Bernoulli's equation and the three heads"
  - "static / dynamic / stagnation (total) pressure"
  - "hydraulic grade line and energy line"
  - "worked examples: conduit velocities by continuity; discharge from an oil-over-water tank"
  - "exercise: closed pressurised tank with losses"
  - "Venturi tube (flow-rate metering); worked example and exercise with a mercury manometer"
  - "Pitot and Pitot-static tube (velocity metering)"
  - "flow through an orifice: Torricelli, vena contracta, Cc/Cv/Cd; worked example (jet diameter, Q, actual velocity)"
  - "tank drainage: falling-head time, constant-descent vessel shape"
  - "weirs"
key_equations: [euler-1d, bernoulli-head, bernoulli-pressure, bernoulli-loss, venturi-Q, venturi-manometer, pitot-v, torricelli, orifice-Q, orifice-jet-diameter, weir-Q]
prerequisites: ["05-flow-fundamentals (continuity, streamline, steady flow)"]
leads_to: ["07-momentum", "09-pipe-flow", "10-open-channel-flow"]
verification_flags: 16   # still printed: Bernoulli dates, S11 (part), S12 (part), S13, S14, S18; new: S53–S62. Fixed in Oct 2026: Pitot slide 239, "m/2" slide 223, S10 Torricelli
tags: [bernoulli, euler, energy, head, venturi, pitot, orifice, torricelli, weir, discharge-coefficient]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the slide image · [hist] historical/biographical note ·
  [added] not in the source — supplied by us ·
  ·slide N / ·slides N–M = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected slide error; detail in _verification-log.md.
  Equations are written in canonical LaTeX; where the slide's typed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 06 — Conservation of Energy & Bernoulli's Equation

Scope: derives Euler's 1-D equation of motion and integrates it to Bernoulli's equation, then applies
Bernoulli to pressure measurement (static/dynamic/stagnation), flow metering (Venturi, Pitot), discharge
through orifices (Torricelli + real-fluid coefficients), tank drainage, and weirs. Inviscid, incompressible,
steady, along-a-streamline assumptions throughout (losses reintroduced empirically via discharge coefficients).

> Several pages of the Oct 2026 PDF drop the glyphs $\mu$, $^2$ and $^3$ when rendered (pages 223–226, 233,
> 241–242, 248 here) — see **S48** in `05-flow-fundamentals.md`. A blank next to a unit or radius is a missing
> square, cube or $\mu$.

---

## 6.1 Energy in a fluid — the three interchangeable forms ·slides 205–209

[def] A fluid parcel carries three exchangeable forms of mechanical energy; in ideal (frictionless) flow their
sum is conserved — the fluid statement of conservation of energy:
- **potential energy** — set by elevation (its level),
- **kinetic energy** — set by speed (e.g. the speed a jet gushes from a pipe),
- **pressure energy** — a fluid under pressure can be given up as work/KE (basis of hydraulic/oil press machines). ·slides 208–209

[hist/analogy] Introduced by analogy with a roller-coaster car: at the top of a slope KE↓/PE↑, at the bottom
KE↑/PE↓, the sum constant at every height. ·slides 206–207
[fig ·slide 206] Roller-coaster with a vertical loop — the solid-body energy-exchange analogy.

---

## 6.2 Euler's equation of motion (1-D, inviscid) ·slides 210–215

[fig ·slides 210–211] A cylindrical fluid element on a streamline: cross-sectional area $dA$, length $ds$,
axis inclined at angle $\theta$ to the horizontal (rise $dz$ over $ds$). Pressure $p$ acts on the lower face and
$p + (\partial p/\partial s)\,ds$ on the upper face; weight $\rho g\,dA\,ds$ acts vertically down. $z$ is vertical,
$s$ is along the streamline.

[derivation] Newton's 2nd law along the streamline (net pressure force + weight component = mass × accel):
$$\rho\,dA\,ds\,\frac{dv}{dt} = -\,dA\,\frac{\partial p}{\partial s}\,ds \;-\; \rho g\,dA\,ds\,\cos\theta$$
$$\Rightarrow\quad \frac{dv}{dt} = -\frac{1}{\rho}\frac{\partial p}{\partial s} - g\cos\theta \qquad\text{}\cdot\text{slide 213}$$
For 1-D flow the velocity is $v=v(s,t)$, so the material (total) acceleration expands by the chain rule:
$$\frac{dv}{dt} = \frac{\partial v}{\partial s}\frac{ds}{dt} + \frac{\partial v}{\partial t}
= v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} \qquad\text{}\cdot\text{slides 213–214}$$
Using $\cos\theta = dz/ds$ and steady flow ($\partial v/\partial t = 0$): ·slide 215
$$\boxed{\,v\frac{\partial v}{\partial s} = -\frac{1}{\rho}\frac{\partial p}{\partial s} - g\frac{dz}{ds}\,}
\qquad\text{[eq: euler-1d] — Euler's equation of motion, 1-D non-viscous flow}$$
[hist ·slide 215] Leonhard Euler (1707–1783), Swiss mathematician.

---

## 6.3 Bernoulli's equation ·slides 216–218

[def] To close the problem two unknowns ($v,p$) need the continuity equation $Av=\text{const}$ solved
simultaneously; for compressible flow $\rho$ is a third unknown and a gas equation of state is added. ·slide 216

[derivation] Integrate Euler's equation along the streamline (with $\rho,g$ constant): ·slides 216–217
$$\int v\frac{\partial v}{\partial s}\,ds + \frac{1}{\rho}\int\frac{\partial p}{\partial s}\,ds
+ g\int\frac{dz}{ds}\,ds = \text{const}
\;\Rightarrow\; \frac{v^{2}}{2} + \frac{p}{\rho} + gz = \text{const (along a streamline)}$$

[eq: bernoulli-head] Dividing by $g$ (every term now has units of metres — a "head"): ·slide 217
$$\boxed{\,\frac{v^{2}}{2g} + \frac{p}{\rho g} + z = H = \text{const}\,}$$
- $H$ = **total head**; $\dfrac{v^2}{2g}$ = **velocity head** (KE); $\dfrac{p}{\rho g}$ = **pressure head**;
  $z$ = **potential/elevation head**. ·slide 217
- [hist ·slide 217] Daniel Bernoulli (1700–1782), Swiss mathematician. *(Note: slide prints "1700 – 1783";
  Bernoulli died 1782 — see _verification-log.md. Still printed in the Oct 2026 edition.)*

> ⚠ VERIFY S11 ·slide 217 — head definitions. *(Partly fixed in the Oct 2026 edition.)* The Jul 2026 edition
> printed "p/ρ = pressure head"; the Oct 2026 edition now reads **p/ρg** — fixed. **Still printed:**
> "V²/2g = velocity head (K.E/unit mass)" and "Z = potential head (P.E. /unit mass)". A head is in metres, i.e.
> energy per unit **weight** (J/N); per unit mass would be J/kg = m²/s².

[eq: bernoulli-pressure] Multiply by $\rho$ for the pressure form; for a horizontal streamline drop $\rho g z$: ·slide 218
$$\tfrac{1}{2}\rho v^{2} + p + \rho g z = \text{const}, \qquad
\underbrace{\tfrac{1}{2}\rho v^{2}}_{\text{dynamic }p} + \underbrace{p_s}_{\text{static }p}
= \underbrace{p_t}_{\text{total / stagnation }p}$$

> ⚠ VERIFY S12 ·slide 218 — *(changed in the Oct 2026 edition.)* The broken line of the Jul 2026 edition
> ("ρV²/2 + Ps =" left unfinished) now reads **ρV²/2 + Ps = Pt** — fixed. **Still printed:** the constant is
> called $H$ ("ρV²/2 + P + ρgz = H", "ρV²/2 + P = H", and now "If H = Pt and P = Ps"). That $H$ is a pressure in
> Pa, while slide 217's $H$ is a head in metres. Keep them apart: write the pressure-form constant as $p_t$.

---

## 6.4 Static, dynamic and stagnation pressure ·slides 218–219

[def] **Static pressure** $p_s$ — measured through a hole in a wall *parallel* to the flow (does not disturb it). ·slide 218
[def] **Dynamic pressure** $\tfrac12\rho v^2$; **total/stagnation pressure** $p_t = p_s + \tfrac12\rho v^2$. ·slide 218
[eq] Bernoulli on a horizontal pipe (z₁=z₂): $\dfrac{v_1^{2}}{2g}+\dfrac{p_1}{\rho g}=\dfrac{v_2^{2}}{2g}+\dfrac{p_2}{\rho g}$. ·slide 219
[fig ·slide 219] Pipe with two piezometer tubes over a contraction: with $v_1A_1=v_2A_2$, the narrow
section has higher velocity ⇒ lower pressure head (tube 2 stands lower than tube 1). Total-head line is level.

---

## 6.5 Hydraulic grade line, energy line & first Bernoulli examples ·slides 220–226

[def] **Hydraulic grade line (HGL)** connects the pressure-head heights $(p/\rho g + z)$ along the pipe;
**energy line (EL)** connects the total heads $(v^2/2g + p/\rho g + z)$. The EL lies a velocity head above the
HGL and slopes down in the flow direction by the head loss. ·slide 221
[fig ·slides 220–221] Water tank 1 → sections 1,2,3 → water tank 2, showing at each section the velocity head
$v^2/2g$, pressure head $p/\rho g$, elevation $z$ above a datum, with the energy line and hydraulic grade line
drawn; $h_2,h_3$ are head losses from section 1 to sections 2,3. [eq: bernoulli-loss] General energy equation
between section 1 and section $i$:
$$\frac{v_1^{2}}{2g}+\frac{p_1}{\rho g}+z_1 = \frac{v_i^{2}}{2g}+\frac{p_i}{\rho g}+z_i + h_i$$
> ⚠ VERIFY S53 ·slide 220 — the slide chains the sections with "+" where "=" is meant: it prints
> "V₁²/2g + P₁/ρg + z₁ = V₂²/2g + P₂/ρg + z₂ + h₂ **+** V₃²/2g + P₃/ρg + z₃ + h₃ …". Read literally, this adds
> section 3's total head to section 2's. Intended: $\ldots + z_2 + h_2 = v_3^2/2g + p_3/\rho g + z_3 + h_3$.
> Also so in the Jul 2026 edition. Cosmetic.

[ex ·slides 222–223] Conduit with $Q=800\ \mathrm{L/min}$, diameters $d_1,d_2,d_3 = 50,60,100\ \mathrm{mm}$.
Find $v_1,v_2,v_3$. Solution via continuity $Q=A v$ (slide 223):
$Q = 800/1000/60 = 0.013\ \mathrm{m^3/s}$;
$v_1 = 0.013/[\pi(0.025)^2] = 6.62\ \mathrm{m/s}$;
$v_2 = A_1v_1/A_2 = (0.025^2\pi\cdot 6.62)/(0.03^2\pi) = 4.59\ \mathrm{m/s}$.
The slide stops at "Find $v_3$….". [added] Same method: $v_3 = v_1(d_1/d_3)^2 = 6.62(25/50)^2 = 1.66\ \mathrm{m/s}$.
*(The Jul 2026 edition printed the $v_2$ unit as "m/2"; **fixed in the Oct 2026 edition** — now m/s.)*
> ⚠ VERIFY S18 ·slide 223 — *(still printed in the Oct 2026 edition.)* 800 L/min is truncated to
> 0.013 m³/s instead of 0.01333 m³/s, making every velocity ≈2.5 % low. Unrounded: $v_1 = 6.79$,
> $v_2 = 4.72$, $v_3 = 1.70\ \mathrm{m/s}$.
*(This conduit example also appeared as old slide 296 in the Jul 2026 momentum block; in the Oct 2026 edition it
maps to slide 222 — see 07-momentum §7.10.)*

[ex ·slides 224–225] Neglecting losses, determine the discharge from the tank in the figure. Data on the slide:
$\gamma_o = 62.4\ \mathrm{lbf/ft^3}$, $g = 32.2\ \mathrm{ft/s^2}$.
[fig ·slide 224] Open tank: a 3 ft layer of oil (s.g. 0.86) floats on water. Point ① is on the oil–water
interface, 4 ft above the centreline of a 2-in-diameter outlet nozzle on the side wall; point ② is the jet.
*(The slide's $\gamma_o = 62.4$ is the specific weight of **water**; the oil's is $0.86 \times 62.4 = 53.7\ \mathrm{lbf/ft^3}$.)*
Solution (slide 225), Bernoulli ① → ② with $v_1 \approx 0$, $p_2 = 0$ gauge, $z_2 = 0$, $h_2 = 0$, and
$p_1 = \gamma_{oil} \times 3\ \mathrm{ft}$ (pressure $p = h\rho g$ under the oil layer):
$$0 + \frac{(0.86)(62.4)(3)}{62.4} + 4 = \frac{v_2^{2}}{2(32.2)} + 0 + 0$$
$$6.58 = \frac{v_2^{2}}{2(32.2)} \;\Rightarrow\; v_2^{2} = 423.75\ \mathrm{ft^2/s^2} \;\Rightarrow\; v_2 = 20.59\ \mathrm{ft/s}$$
$$Q = A v_2 = \pi\Big(\frac{1}{12}\Big)^{2}(20.59) = \boxed{0.449\ \mathrm{ft^3/s}}$$
✓ all numbers check.

[exercise ·slide 226] The figure has losses of 0.1 m. The barometer reads 750 mmHg. Determine the velocity
at A. Answer printed on the slide: **[2.66 m/s]**.
[fig ·slide 226] Closed tank of water. The air space above the water (point B on the surface) is at 75 kPa abs.
A side outlet at A, 3 m below the water surface, discharges to the atmosphere.
> ⚠ VERIFY S54 ·slide 226 — the data line reads "Take γ(air) = 9.79 N/m² and g = 9.807 g/m²" (the rendered
> page shows "N/m" and "g/m" with the squares missing). 9.79 is the specific weight of **water** in
> **kN/m³** (air is about 0.012 kN/m³), and $g$ is in m/s². The printed answer 2.66 m/s needs
> $\gamma_{water} = 9.79\ \mathrm{kN/m^3}$. Substantive: substituting the specific weight of air, as labelled,
> gives a nonsense result.

[added] Worked answer (not on the slides). Atmospheric pressure from the barometer, taking
$\gamma_{Hg} = 13.6\,\gamma_{water}$:
$$p_{atm} = (0.750)(13.6)(9.79) = 99.86\ \mathrm{kPa\ abs}$$
Bernoulli from B (surface, $v_B \approx 0$, $z_B = 3\ \mathrm{m}$) to A ($p_A = p_{atm}$, $z_A = 0$), absolute pressures:
$$\frac{p_B}{\gamma} + z_B = \frac{p_{atm}}{\gamma} + \frac{v_A^{2}}{2g} + h_L$$
$$\frac{v_A^{2}}{2g} = 3 + \frac{75 - 99.86}{9.79} - 0.1 = 3 - 2.539 - 0.1 = 0.361\ \mathrm{m}$$
$$v_A = \sqrt{2(9.807)(0.361)} = \boxed{2.66\ \mathrm{m/s}}$$
This matches the slide. Converting 750 mmHg with the standard 760 mmHg = 101.325 kPa instead gives
$p_{atm} = 99.99\ \mathrm{kPa}$ and $v_A = 2.61\ \mathrm{m/s}$ — state which conversion is used.

---

## 6.6 Venturi tube ·slides 227–234

[def] A converging–diverging insert in a pipe: the throat speeds the flow up, and the accompanying pressure
drop between inlet (1) and throat (2) meters the flow rate. ·slide 229
[hist ·slide 228] Giovanni Battista Venturi (1746–1822).
[fig ·slide 229] Horizontal pipe with a smooth contraction to a throat then expansion; pressure tappings at the
wide section $A_1$ and throat $A_2$ feed a manometer reading the head difference $H$.

[derivation] Bernoulli (horizontal, z₁=z₂) + continuity $A_1v_1=A_2v_2$: ·slides 230–231
$$\frac{v_2^{2}-v_1^{2}}{2g}=\frac{p_1-p_2}{\rho g},\qquad v_1=\frac{A_2}{A_1}v_2$$
[eq: venturi-Q] ·slide 231
$$v_2=\frac{1}{\sqrt{1-(A_2/A_1)^{2}}}\sqrt{\frac{2(p_1-p_2)}{\rho}},\qquad
\frac{p_1-p_2}{\rho g}=H$$
$$\boxed{\,Q = C\,\frac{A_2}{\sqrt{1-(A_2/A_1)^{2}}}\,\sqrt{2gH}\,}$$
$C$ = **coefficient of discharge** (empirical, accounts for the real energy loss between $A_1$ and $A_2$). For a
gas, $p_1-p_2$ is read on a U-tube. ·slide 231
> ⚠ VERIFY S13 ·slide 231 — *(still printed in the Oct 2026 edition.)* The last line reads
> "Q = C[A₂/{√1 − (A₂/A₁)²} * √2gH": the root sits on the 1 alone instead of on the whole $1-(A_2/A_1)^2$, and
> the square bracket never closes. Use the boxed form above; the unboxed $Q = A_2v_2$ line two rows up on the
> same slide has it right.

[ex ·slides 232–233] A Venturi meter with a 150 mm throat sits in a horizontal 300 mm water main. Discharge
$Q = 0.142\ \mathrm{m^3/s}$, discharge coefficient 0.982, mercury s.g. 13.6. Find the difference $y$ in the
levels of the mercury columns of the differential manometer.
[fig ·slide 232] Horizontal pipe, flow left to right, 300 mm main narrowing to a 150 mm throat; a U-tube of
mercury joins the main and the throat, deflection $y$.
Solution (slide 233):
$$A_2 = \pi(0.075)^{2} = 0.01767\ \mathrm{m^2},\qquad A_1 = \pi(0.150)^{2} = 0.07069\ \mathrm{m^2}$$
$$0.142 = (0.982)(0.01767)\sqrt{\frac{2(9.807)\,(p_1-p_2)/\gamma}{1-(0.01767/0.07069)^{2}}}
\;\Rightarrow\; \frac{p_1-p_2}{\gamma} = 3.201\ \mathrm{m\ of\ water}$$
[eq: venturi-manometer] For a mercury U-tube under water the manometer reading $y$ gives
$$p_1 - p_2 = (\gamma_{Hg} - \gamma)\,y = (13.6 - 1)\,\gamma\,y = 12.6\,\gamma\,y$$
$$y = \frac{3.201}{12.6} = 0.254\ \mathrm{m} = \boxed{254\ \mathrm{mm}}$$
> ⚠ VERIFY S55 ·slides 232–233 — the slide prints "But P₁ − P₂ = hγ = 13.6 y" and "y = 3.201 m/13.6", then
> "y = 0.254 m". But $3.201/13.6 = 0.235$; the printed 0.254 is $3.201/12.6$. The manometer relation must
> subtract the water column above the mercury: $p_1-p_2 = (13.6-1)\gamma y$. The answer 254 mm is right; the line
> that produces it is not. Same slide, symbolic line: "$= A_2\sqrt{[2g(p_1-p_2)/\gamma]/[1-(A1/A2)^2]}$" inverts
> the area ratio and drops $C$ (the numerical line uses $0.01767/0.07069$, i.e. $A_2/A_1$, correctly). Slide 232
> also writes "γ(Hg) = 13.6", which is the specific **gravity**, not a specific weight. Substantive.

[exercise ·slide 234] Water flows through the Venturi meter shown. Determine the discharge coefficient of the
meter if the discharge is 2.12 cfs. The slide adds "Take C = 0.979".
[fig ·slide 234] 12-in pipe, 4-in throat, mercury manometer between pipe and throat with a 9-in deflection.
> ⚠ VERIFY S56 ·slide 234 — the question asks for the discharge coefficient and then gives it ("Take
> C = 0.979"). 0.979 is the answer (checked below), printed where the data go. Cosmetic.

[added] Worked answer (not on the slides). $A_2 = \pi(2/12)^2 = 0.08727\ \mathrm{ft^2}$,
$(A_2/A_1)^2 = (4/12)^4 = 1/81$; water head from the mercury reading:
$$\frac{p_1-p_2}{\gamma} = (13.6-1)\Big(\frac{9}{12}\Big) = 9.45\ \mathrm{ft}$$
$$Q_{ideal} = A_2\sqrt{\frac{2(32.2)(9.45)}{1-1/81}} = (0.08727)(24.82) = 2.166\ \mathrm{ft^3/s}$$
$$C = \frac{Q}{Q_{ideal}} = \frac{2.12}{2.166} = \boxed{0.979}$$

---

## 6.7 Pitot and Pitot-static tube ·slides 235–242

[def] A tube facing the flow with a hole at the streamlined nose (stagnation opening B) and a side hole normal
to the flow (static opening C). The stagnation–static pressure difference gives the local velocity. ·slides 236–238
[hist ·slide 235] Henri de Pitot (1695–1771).
[fig ·slides 236–238] Right-angled ("hook") tube in a duct: at nose B the flow is brought to rest (stagnation
point, v=0, pressure $p_B$); upstream point A is undisturbed ($p_A,v_A$); side hole C reads the static pressure
$p_C=p_A$. A manometer of height $H$ between B and C gives the reading.

[derivation] Bernoulli A→B with $v_B=0$: ·slide 239
$$\frac{p_A}{\rho g}+\frac{v_A^{2}}{2g}=\frac{p_B}{\rho g}\;\Rightarrow\;
v_A=\sqrt{\frac{2(p_B-p_A)}{\rho}}=\sqrt{\frac{2(p_B-p_C)}{\rho}}=\sqrt{2gH}$$
> ⚠ VERIFY ·slide 239 — *(fixed in the Oct 2026 edition.)* The Jul 2026 edition wrote
> $v_A=\sqrt{2g\,(p_B - p_A/\rho g)}$, mixing a pressure with a head inside the root. The Oct 2026 edition adds
> the intermediate steps and now reads $v_A = \sqrt{2g(p_B - p_A)/\rho g}$ — dimensionally correct (one stray
> closing bracket remains). See _verification-log.md.

[eq: pitot-v] With a real tube (shape + viscosity losses) a coefficient of velocity is applied: ·slide 240
$$v_A = C_v\sqrt{2gH}\qquad (C_v = \text{coefficient of velocity})$$

[ex ·slides 241–242] Pitot-static tube, mercury manometer, in a water flow, reading $h=8.4\ \mathrm{in}$.
$p_B-p_C=(\gamma_m-\gamma_w)h=(846-62.4\ \mathrm{lbf/ft^3})(8.4/12\ \mathrm{ft})=549\ \mathrm{lbf/ft^2}$;
$v_A=\sqrt{2(p_B-p_C)/\rho}=\sqrt{2(549)/1.94}=23.8\ \mathrm{ft/s}$ (with $\rho_{water}=1.94\ \mathrm{slug/ft^3}$). ✓ numbers check.
> ⚠ VERIFY S57 ·slides 241–242 — the Oct 2026 edition relabels the data with broken units: "γm = 846 lbf ft/s²;
> γw = 62.4 lbf ft s²" and "= 549 lbf ft²/s²". Specific weights are in **lbf/ft³** and the pressure difference in
> **lbf/ft²** (the Jul 2026 edition had lbf/ft³ and lbf/ft²). The numbers are right; only the units are wrong.
> Cosmetic.

---

## 6.8 Flow through a small hole (orifice) ·slides 243–253

Three cases: (1) water level constant (very large tank), (2) level falling, (3) level falling at constant speed. ·slide 244

### Case 1 — constant head → Torricelli ·slides 243–249
[fig ·slide 245] Tank with a side orifice; the jet contracts to its minimum section (**vena contracta**, B)
a short distance downstream where streamlines are parallel and pressure uniform. Particle A (at the surface)
flows to B.
[derivation] Bernoulli surface(A)→jet(B) with $v_A\approx0$, $z_A=H$, $z_B=0$, $p_A=p_B=$ atm: ·slide 246
$$\frac{v_B^{2}}{2g}=\frac{p_A-p_B}{\rho g}+H \;\Rightarrow\; \boxed{v_B=\sqrt{2gH}}\quad\text{[eq: torricelli]}$$
> ⚠ VERIFY S10 ·slide 246 — *(fixed in the Oct 2026 edition.)* The Jul 2026 edition dropped the elevation term
> ($p_A/\rho g + 0 = p_B/\rho g + v_B^2/2g$, whose own algebra gives $v_B = 0$). The Oct 2026 edition restores it:
> "P_A/ρg + H = P_B/ρg + V_B²/2g", and the chain ends correctly at $v_B = \sqrt{2gH}$.
> ⚠ VERIFY S58 ·slide 246 — the new intermediate line has a sign slip: "P_A/ρg **+** P_B/ρg = V_B²/2g − H"
> should be $p_A/\rho g - p_B/\rho g = v_B^2/2g - H$. The next line, "(P_A − P_B)/ρg = V_B²/2g − H", is correct
> again. Cosmetic.

[def] Real-fluid coefficients ·slide 243:
- coefficient of contraction $C_c = a_c/a \approx 0.65$ ($a_c$ = vena-contracta area, $a$ = hole area),
- coefficient of velocity $C_v = v_{act}/\sqrt{2gH} \approx 0.95$,
- coefficient of discharge $C_d = C_cC_v$ ⇒ $Q = C_d\,a\sqrt{2gH}$; for a sharp-edged hole $C_d\approx0.60$.
$$\boxed{\,Q = C_d\,a\,\sqrt{2gH}\,}\quad\text{[eq: orifice-Q]}$$

[ex ·slides 247–249] Water flows from a large tank through a 2-in-diameter sharp-edged orifice and discharges to
the atmosphere under a head of 10 ft (figure). $C_v = 0.96$, $C_c = 0.62$. Find (a) the diameter of the
contracted jet, (b) the actual velocity in the jet, (c) the discharge.
*(Letters: slide 248 writes "Cc = a/A" with $a$ = **jet** area and $A$ = **orifice** area — the opposite of
slide 243, where $a$ is the hole. Here: $A = \pi(1/12)^2\ \mathrm{ft^2}$ is the orifice.)*
(a) Jet (vena-contracta) area and diameter, slide 248: [eq: orifice-jet-diameter]
$$a_{jet} = C_c A = (0.62)(\pi)\Big(\frac{1}{12}\Big)^{2} = 0.01353\ \mathrm{ft^2}$$
$$r_{jet}^{2} = \frac{0.01353}{\pi} = 0.004306\ \mathrm{ft^2} \;\Rightarrow\; r_{jet} = 0.0656\ \mathrm{ft}$$
$$D_{jet} = 0.1313\ \mathrm{ft} = \boxed{1.58\ \mathrm{in}}\qquad (\text{equivalently } D_{jet} = d\sqrt{C_c})$$
(b, c) Slide 249:
$$C = C_cC_v = (0.62)(0.96) = 0.595$$
$$Q = C A\sqrt{2gH} = (0.595)\,\pi\Big(\frac{1}{12}\Big)^{2}\sqrt{2(32.2)(10)} = \boxed{0.329\ \mathrm{ft^3/s}}$$
$$v_{act} = \frac{Q}{a_{jet}} = \frac{0.329}{0.01353} = \boxed{24.3\ \mathrm{ft/s}}$$
[added] Check: $v_{act} = C_v\sqrt{2gH} = 0.96 \times 25.38 = 24.4\ \mathrm{ft/s}$ — the same to rounding. ✓
> ⚠ VERIFY S59 ·slide 248 — prints "(r_jet)² = 0.004297 ft²"; $0.01353/\pi = 0.004306$. $r_{jet} = 0.0656$
> and $D_{jet} = 1.58$ in are unaffected. Cosmetic.
> ⚠ VERIFY S60 ·slide 249 — prints "v = Q/a = 0.329/0.1353"; the jet area is 0.01353 ft² (slide 248).
> $0.329/0.1353 = 2.43$; the printed result 24.3 ft/s is right. Cosmetic.

### Case 2 — falling head (time to drain) ·slide 250
[derivation] Outflow $dQ = C_d a\sqrt{2gH}\,dt = -A\,dH$ (tank area $A$); integrate:
$$t_2-t_1 = \frac{2A}{C_d\,a\sqrt{2g}}\left(\sqrt{H_1}-\sqrt{H_2}\right)$$
*(The slide writes $C_a$ for the product $C_d\,a$.)*
> ⚠ VERIFY S61 ·slide 250 — the side working prints "∫dH/H^(−½)"; the integral is
> $\int H^{-1/2}\,dH = \int dH/H^{1/2} = 2H^{1/2}$ (dividing by $H^{-1/2}$ would multiply by $\sqrt{H}$). The slide's
> next line, "1/(1/2) · H^(1/2)", and the result are correct. Also so in the Jul 2026 edition. Cosmetic.

### Case 3 — constant descent velocity → vessel shape ·slides 251–252
[derivation] For a round vessel radius $r$, $-dH/dt=v=\text{const}$ with $dQ=C_d a\sqrt{2gH}\,dt=-\pi r^2 dH$:
$$v=\frac{C_d a\sqrt{2gH}}{\pi r^{2}} \;\Rightarrow\; H=\Big(\frac{\pi v}{C_d a}\Big)^2\frac{r^{4}}{2g}
\;\Rightarrow\; \boxed{H \propto r^{4}}$$
A vessel whose radius follows $r \propto H^{1/4}$ drains with a constant fall of water level. ·slide 252
> ⚠ VERIFY S14 ·slide 251 — *(still printed in the Oct 2026 edition.)* $A$ is used for both the hole ("a small
> hole of area A") and the tank cross-section ("−dH A = −dH π r² dt", and "v = Q/A" on slide 252), after slide 250
> used $a$ for the hole. Here $a$ = hole, $\pi r^2$ = tank section.
> ⚠ VERIFY S62 ·slide 252 — new line "H = (πv)²/C_a · 1/2g · r⁴" leaves $C_a$ unsquared; it must be
> $(\pi v/C_a)^2\,r^4/2g$, as the line above it has. $H \propto r^4$ is unaffected. Cosmetic.
[hist ·slide 253] Application: the Egyptian water clock (clepsydra), ~3400 years ago — tells time by the water level.

---

## 6.9 Weir ·slides 254–255

[def] A weir is a wall/board over which channel water flows, used to set/measure flow rate. ·slide 254
[fig ·slides 254–255] Rectangular weir of width $b$; treat a strip of depth $dz$ at depth $z$ below the surface
as an orifice; total head $H$ over the crest.
[derivation] Strip velocity $v=\sqrt{2gz}$ (Bernoulli), strip discharge $dQ = C\,b\,\sqrt{2g}\,\sqrt{z}\,dz$;
integrate $z:0\to H$:
$$\boxed{\,Q = \tfrac{2}{3}\,C\,b\,\sqrt{2g}\,H^{3/2}\,}\quad\text{[eq: weir-Q]}$$
Measuring the head $H$ over the crest gives $Q$. ·slide 255

---

### Cross-references
- Continuity $Av=\text{const}$ and streamline/steady-flow definitions → **05-flow-fundamentals**.
- Discharge coefficients & real losses are quantified for pipe fittings in **09-pipe-flow**; weirs recur in
  open-channel flow → **10-open-channel-flow**.
- The momentum counterpart (force of jets, not energy) → **07-momentum**.

### Verification notes for this section
- Re-checked page by page against the Oct 2026 edition (pages 205–255). All core equations (Euler, Bernoulli
  head/pressure forms, Venturi $Q$, Pitot $v$, Torricelli, orifice $Q$, weir $Q$) match standard references.
- Every number in the new worked examples and exercises recomputed: slides 225 (0.449 ft³/s), 226 (2.66 m/s),
  233 (254 mm), 234 (C = 0.979), 248–249 (1.58 in, 0.329 ft³/s, 24.3 ft/s) — all final answers ✓; working
  defects flagged S55, S59, S60.
- **Fixed in the Oct 2026 edition:** Pitot expression (slide 239); "m/2" unit (slide 223); S10 Torricelli
  elevation term (slide 246). **Partly fixed:** S11 (p/ρg now right; "per unit mass" still printed); S12 (broken
  line fixed; $H$ still reused for a pressure).
- **Still printed:** Bernoulli death year 1783 (slide 217); S13 Venturi radical (slide 231); S14 $A$ for hole and
  tank (slide 251); S18 rounding 0.013 m³/s (slide 223).
- New flags: S53–S62 (S54, S55 substantive; the rest cosmetic).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
