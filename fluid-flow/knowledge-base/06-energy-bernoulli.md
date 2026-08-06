---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "06 — Conservation of Energy & Bernoulli's Equation"
slides: "215-263"
file_role: topic
subtopics:
  - "energy forms in a fluid (PE, KE, pressure energy)"
  - "Euler's equation of motion (1-D, inviscid)"
  - "Bernoulli's equation and the three heads"
  - "static / dynamic / stagnation (total) pressure"
  - "hydraulic grade line and energy line"
  - "Venturi tube (flow-rate metering)"
  - "Pitot and Pitot-static tube (velocity metering)"
  - "flow through an orifice: Torricelli, vena contracta, Cc/Cv/Cd"
  - "tank drainage: falling-head time, constant-descent vessel shape"
  - "weirs"
key_equations: [euler-1d, bernoulli-head, bernoulli-pressure, venturi-Q, pitot-v, torricelli, orifice-Q, weir-Q]
prerequisites: ["05-flow-fundamentals (continuity, streamline, steady flow)"]
leads_to: ["07-momentum", "09-pipe-flow", "10-open-channel-flow"]
verification_flags: 1
tags: [bernoulli, euler, energy, head, venturi, pitot, orifice, torricelli, weir, discharge-coefficient]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the slide image · [hist] historical/biographical note ·
  ·slide N / ·slides N–M = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected slide error; detail in _verification-log.md.
  Equations are written in canonical LaTeX; where the slide's typed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 06 — Conservation of Energy & Bernoulli's Equation

Scope: derives Euler's 1-D equation of motion and integrates it to Bernoulli's equation, then applies
Bernoulli to pressure measurement (static/dynamic/stagnation), flow metering (Venturi, Pitot), discharge
through orifices (Torricelli + real-fluid coefficients), tank drainage, and weirs. Inviscid, incompressible,
steady, along-a-streamline assumptions throughout (losses reintroduced empirically via discharge coefficients).

---

## 6.1 Energy in a fluid — the three interchangeable forms ·slides 215–219

[def] A fluid parcel carries three exchangeable forms of mechanical energy; in ideal (frictionless) flow their
sum is conserved — the fluid statement of conservation of energy:
- **potential energy** — set by elevation (its level),
- **kinetic energy** — set by speed (e.g. the speed a jet gushes from a pipe),
- **pressure energy** — a fluid under pressure can be given up as work/KE (basis of hydraulic/oil press machines). ·slides 218–219

[hist/analogy] Introduced by analogy with a roller-coaster car: at the top of a slope KE↓/PE↑, at the bottom
KE↑/PE↓, the sum constant at every height. ·slides 216–217
[fig ·slide 216] Roller-coaster with a vertical loop — the solid-body energy-exchange analogy.

---

## 6.2 Euler's equation of motion (1-D, inviscid) ·slides 220–226

[fig ·slides 220–221] A cylindrical fluid element on a streamline: cross-sectional area `dA`, length `ds`,
axis inclined at angle `θ` to the horizontal (rise `dz` over `ds`). Pressure `p` acts on the lower face and
`p + (∂p/∂s)ds` on the upper face; weight `ρg·dA·ds` acts vertically down. `z` is vertical, `s` is along the
streamline.

[derivation] Newton's 2nd law along the streamline (net pressure force + weight component = mass × accel):
$$\rho\,dA\,ds\,\frac{dv}{dt} = -\,dA\,\frac{\partial p}{\partial s}\,ds \;-\; \rho g\,dA\,ds\,\cos\theta$$
$$\Rightarrow\quad \frac{dv}{dt} = -\frac{1}{\rho}\frac{\partial p}{\partial s} - g\cos\theta \qquad\text{·slide 223}$$
For 1-D flow the velocity is $v=v(s,t)$, so the material (total) acceleration expands by the chain rule:
$$\frac{dv}{dt} = \frac{\partial v}{\partial s}\frac{ds}{dt} + \frac{\partial v}{\partial t}
= v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} \qquad\text{·slides 223–224}$$
Using $\cos\theta = dz/ds$ and steady flow ($\partial v/\partial t = 0$): ·slide 225
$$\boxed{\,v\frac{\partial v}{\partial s} = -\frac{1}{\rho}\frac{\partial p}{\partial s} - g\frac{dz}{ds}\,}
\qquad\text{[eq: euler-1d] — Euler's equation of motion, 1-D non-viscous flow}$$
[hist ·slide 226] Leonhard Euler (1707–1783), Swiss mathematician.

---

## 6.3 Bernoulli's equation ·slides 227–231

[def] To close the problem two unknowns ($v,p$) need the continuity equation $Av=\text{const}$ solved
simultaneously; for compressible flow $\rho$ is a third unknown and a gas equation of state is added. ·slide 227

[derivation] Integrate Euler's equation along the streamline (with $\rho,g$ constant): ·slides 228–229
$$\int v\frac{\partial v}{\partial s}\,ds + \frac{1}{\rho}\int\frac{\partial p}{\partial s}\,ds
+ g\int\frac{dz}{ds}\,ds = \text{const}
\;\Rightarrow\; \frac{v^{2}}{2} + \frac{p}{\rho} + gz = \text{const (along a streamline)}$$

[eq: bernoulli-head] Dividing by $g$ (every term now has units of metres — a "head"): ·slides 229–230
$$\boxed{\,\frac{v^{2}}{2g} + \frac{p}{\rho g} + z = H = \text{const}\,}$$
- $H$ = **total head**; $\dfrac{v^2}{2g}$ = **velocity head** (KE); $\dfrac{p}{\rho g}$ = **pressure head**;
  $z$ = **potential/elevation head**. ·slide 229
- [hist ·slide 230] Daniel Bernoulli (1700–1782), Swiss mathematician. *(Note: slide prints "1700 – 1783";
  Bernoulli died 1782 — see _verification-log.md.)*

[eq: bernoulli-pressure] Multiply by $\rho$ for the pressure form; for a horizontal streamline drop $\rho g z$: ·slide 231
$$\tfrac{1}{2}\rho v^{2} + p + \rho g z = \text{const}, \qquad
\underbrace{\tfrac{1}{2}\rho v^{2}}_{\text{dynamic }p} + \underbrace{p_s}_{\text{static }p}
= \underbrace{p_t}_{\text{total / stagnation }p}$$

---

## 6.4 Static, dynamic and stagnation pressure ·slides 231–234

[def] **Static pressure** $p_s$ — measured through a hole in a wall *parallel* to the flow (does not disturb it). ·slide 232
[def] **Dynamic pressure** $\tfrac12\rho v^2$; **total/stagnation pressure** $p_t = p_s + \tfrac12\rho v^2$. ·slide 231
[eq] Bernoulli on a horizontal pipe (z₁=z₂): $\dfrac{v_1^{2}}{2g}+\dfrac{p_1}{\rho g}=\dfrac{v_2^{2}}{2g}+\dfrac{p_2}{\rho g}$. ·slide 233
[fig ·slides 233–234] Pipe with two piezometer tubes over a contraction: with $v_1A_1=v_2A_2$, the narrow
section has higher velocity ⇒ lower pressure head (tube 2 stands lower than tube 1). Total-head line is level.

---

## 6.5 Hydraulic grade line & energy line ·slides 235–238

[def] **Hydraulic grade line (HGL)** connects the pressure-head heights $(p/\rho g + z)$ along the pipe;
**energy line (EL)** connects the total heads $(v^2/2g + p/\rho g + z)$. The EL lies a velocity head above the
HGL and slopes down in the flow direction by the head loss. ·slide 236
[fig ·slides 235–236] Water tank 1 → sections 1,2,3 → water tank 2, showing at each section the velocity head
$v^2/2g$, pressure head $p/\rho g$, elevation $z$ above a datum, with the energy line and hydraulic grade line
drawn; $h_2,h_3$ are head losses from section 1 to sections 2,3. General energy equation between sections:
$$\frac{v_1^{2}}{2g}+\frac{p_1}{\rho g}+z_1 = \frac{v_i^{2}}{2g}+\frac{p_i}{\rho g}+z_i + h_i$$

[ex ·slides 237–238] Conduit with $Q=800\ \mathrm{L/min}$, diameters $d_1,d_2,d_3 = 50,60,100\ \mathrm{mm}$.
Find $v_1,v_2,v_3$. Solution via continuity $Q=A v$:
$Q = 800/1000/60 = 0.013\ \mathrm{m^3/s}$;
$v_1 = 0.013/[\pi(0.025)^2] = 6.62\ \mathrm{m/s}$;
$v_2 = A_1v_1/A_2 = (0.025^2\pi\cdot 6.62)/(0.03^2\pi) = 4.59\ \mathrm{m/s}$;
$v_3$ from $A_1v_1=A_3v_3$ with $d_3=100$ mm ⇒ $v_3 = 6.62(25/50)^2 = 1.66\ \mathrm{m/s}$.
*(Slide 238 prints the $v_2$ unit as "m/2" — typo for m/s.)*

---

## 6.6 Venturi tube ·slides 240–244

[def] A converging–diverging insert in a pipe: the throat speeds the flow up, and the accompanying pressure
drop between inlet (1) and throat (2) meters the flow rate. ·slide 241
[hist ·slide 240] Giovanni Battista Venturi (1746–1822).
[fig ·slide 241] Horizontal pipe with a smooth contraction to a throat then expansion; pressure tappings at the
wide section $A_1$ and throat $A_2$ feed a manometer reading the head difference $H$.

[derivation] Bernoulli (horizontal, z₁=z₂) + continuity $A_1v_1=A_2v_2$: ·slides 242–243
$$\frac{v_2^{2}-v_1^{2}}{2g}=\frac{p_1-p_2}{\rho g},\qquad v_1=\frac{A_2}{A_1}v_2$$
[eq: venturi-Q] ·slides 243–244
$$v_2=\frac{1}{\sqrt{1-(A_2/A_1)^{2}}}\sqrt{\frac{2(p_1-p_2)}{\rho}},\qquad
\frac{p_1-p_2}{\rho g}=H$$
$$\boxed{\,Q = C\,\frac{A_2}{\sqrt{1-(A_2/A_1)^{2}}}\,\sqrt{2gH}\,}$$
$C$ = **coefficient of discharge** (empirical, accounts for the real energy loss between $A_1$ and $A_2$). For a
gas, $p_1-p_2$ is read on a U-tube. ·slide 244

---

## 6.7 Pitot and Pitot-static tube ·slides 245–252

[def] A tube facing the flow with a hole at the streamlined nose (stagnation opening B) and a side hole normal
to the flow (static opening C). The stagnation–static pressure difference gives the local velocity. ·slides 246–248
[hist ·slide 245] Henri de Pitot (1695–1771).
[fig ·slides 246–248] Right-angled ("hook") tube in a duct: at nose B the flow is brought to rest (stagnation
point, v=0, pressure $p_B$); upstream point A is undisturbed ($p_A,v_A$); side hole C reads the static pressure
$p_C=p_A$. A manometer of height $H$ between B and C gives the reading.

[derivation] Bernoulli A→B with $v_B=0$: ·slide 249
$$\frac{p_A}{\rho g}+\frac{v_A^{2}}{2g}=\frac{p_B}{\rho g}\;\Rightarrow\;
v_A=\sqrt{\frac{2(p_B-p_A)}{\rho}}=\sqrt{\frac{2(p_B-p_C)}{\rho}}=\sqrt{2gH}$$
> ⚠ VERIFY ·slide 249 — the slide writes $v_A=\sqrt{2g\,(p_B - p_A/\rho g)}$, which mixes a pressure with a head
> inside the root (dimensionally inconsistent). Intended/canonical form is
> $v_A=\sqrt{2g\,(p_B/\rho g - p_A/\rho g)} = \sqrt{2(p_B-p_A)/\rho}$. Treat as a notation slip, not a new result.
> See _verification-log.md.

[eq: pitot-v] With a real tube (shape + viscosity losses) a coefficient of velocity is applied: ·slide 250
$$v_A = C_v\sqrt{2gH}\qquad (C_v = \text{coefficient of velocity})$$

[ex ·slides 251–252] Pitot-static tube, mercury manometer, in a water flow, reading $h=8.4\ \mathrm{in}$.
$p_B-p_C=(\rho_m-\rho_w)h=(846-62.4\ \mathrm{lbf/ft^3})(8.4/12\ \mathrm{ft})=549\ \mathrm{lbf/ft^2}$;
$v_A=\sqrt{2(p_B-p_C)/\rho}=\sqrt{2(549)/1.94}=23.8\ \mathrm{ft/s}$ (with $\rho_{water}=1.94\ \mathrm{slug/ft^3}$). ✓ numbers check.

---

## 6.8 Flow through a small hole (orifice) ·slides 253–261

Three cases: (1) water level constant (very large tank), (2) level falling, (3) level falling at constant speed. ·slide 253

### Case 1 — constant head → Torricelli ·slides 254–257
[fig ·slides 254–255] Tank with a side orifice; the jet contracts to its minimum section (**vena contracta**, B)
a short distance downstream where streamlines are parallel and pressure uniform. Particle A (at the surface)
flows to B.
[derivation] Bernoulli surface(A)→jet(B) with $v_A\approx0$, $z_A=H$, $z_B=0$, $p_A=p_B=$ atm: ·slide 256
$$\frac{v_B^{2}}{2g}=\frac{p_A-p_B}{\rho g}+H \;\Rightarrow\; \boxed{v_B=\sqrt{2gH}}\quad\text{[eq: torricelli]}$$
[def] Real-fluid coefficients ·slide 257:
- coefficient of contraction $C_c = a_c/a \approx 0.65$ ($a_c$ = vena-contracta area, $a$ = hole area),
- coefficient of velocity $C_v = v_{act}/\sqrt{2gH} \approx 0.95$,
- coefficient of discharge $C_d = C_cC_v$ ⇒ $Q = C_d\,a\sqrt{2gH}$; for a sharp-edged hole $C_d\approx0.60$.
$$\boxed{\,Q = C_d\,a\,\sqrt{2gH}\,}\quad\text{[eq: orifice-Q]}$$

### Case 2 — falling head (time to drain) ·slide 258
[derivation] Outflow $dQ = C_d a\sqrt{2gH}\,dt = -A\,dH$ (tank area $A$); integrate:
$$t_2-t_1 = \frac{2A}{C_d\,a\sqrt{2g}}\left(\sqrt{H_1}-\sqrt{H_2}\right)$$

### Case 3 — constant descent velocity → vessel shape ·slides 259–260
[derivation] For a round vessel radius $r$, $-dH/dt=v=\text{const}$ with $dQ=C_d a\sqrt{2gH}\,dt=-\pi r^2 dH$:
$$v=\frac{C_d a\sqrt{2gH}}{\pi r^{2}} \;\Rightarrow\; H=\Big(\frac{\pi v}{C_d a}\Big)^2\frac{r^{4}}{2g}
\;\Rightarrow\; \boxed{H \propto r^{4}}$$
A vessel whose radius follows $r \propto H^{1/4}$ drains with a constant fall of water level. ·slide 260
[hist ·slide 261] Application: the Egyptian water clock (clepsydra), ~3400 years ago — tells time by the water level.

---

## 6.9 Weir ·slides 262–263

[def] A weir is a wall/board over which channel water flows, used to set/measure flow rate. ·slide 262
[fig ·slides 262–263] Rectangular weir of width $b$; treat a strip of depth $dz$ at depth $z$ below the surface
as an orifice; total head $H$ over the crest.
[derivation] Strip velocity $v=\sqrt{2gz}$ (Bernoulli), strip discharge $dQ = C\,b\,\sqrt{2g}\,\sqrt{z}\,dz$;
integrate $z:0\to H$:
$$\boxed{\,Q = \tfrac{2}{3}\,C\,b\,\sqrt{2g}\,H^{3/2}\,}\quad\text{[eq: weir-Q]}$$
Measuring the head $H$ over the crest gives $Q$. ·slide 263

---

### Cross-references
- Continuity $Av=\text{const}$ and streamline/steady-flow definitions → **05-flow-fundamentals**.
- Discharge coefficients & real losses are quantified for pipe fittings in **09-pipe-flow**; weirs recur in
  open-channel flow → **10-open-channel-flow**.
- The momentum counterpart (force of jets, not energy) → **07-momentum**.

### Verification notes for this section (spot-check basis)
- All core equations (Euler, Bernoulli head/pressure forms, Venturi $Q$, Pitot $v$, Torricelli, orifice $Q$,
  weir $Q$) match standard references — verified, no substantive errors.
- 1 flag: slide 249 Pitot expression (dimensional/notation slip) — logged.
- Minor slide typos noted inline: slide 238 "m/2"→"m/s"; slide 230 Bernoulli death year "1783"→1782.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
