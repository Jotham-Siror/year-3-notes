---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "09 — Flow in Pipes"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "376-458"
file_role: topic
subtopics:
  - "section page of pipe-system figures (new in the Oct 2026 edition)"
  - "inlet/entrance region & length; kinetic-energy correction factor"
  - "pipe friction (Darcy–Weisbach); laminar λ=64/Re"
  - "turbulent friction: smooth (Blasius, Nikuradse, Kármán–Nikuradse, Itaya) & rough pipes; Moody diagram"
  - "non-circular pipes: hydraulic mean depth / hydraulic diameter"
  - "minor losses: sudden & gradual area change, contraction, diffuser & recovery efficiency, wall effect"
  - "throttle (choke/orifice/nozzle) discharge coefficient"
  - "losses at bends, elbows, branches, junctions, valves & cocks"
  - "total pipeline loss"
  - "pumping to higher levels: heads, water power, efficiency, characteristic & resistance curves"
  - "pump head & power between two reservoirs — Moody f + minor losses (worked exercise new in the Oct 2026 edition)"
key_equations: [entrance-length, ke-correction, darcy-weisbach, lambda-laminar, blasius, karman-nikuradse, itaya, rough-pipe, hydraulic-diameter, minor-loss, sudden-expansion, sudden-contraction, throttle-C, diffuser-eff, total-loss, pump-power, pump-head]
prerequisites: ["06-energy-bernoulli", "08-viscous-flow (Hagen–Poiseuille, boundary layer)"]
leads_to: ["10-open-channel-flow"]
verification_flags: 3   # new S79–S81 (Oct 2026 edition, slides 455–457); slide flags S23–S26 still printed; S32 dropped with old slide 440
tags: [pipe-flow, friction, darcy-weisbach, moody, blasius, hydraulic-diameter, minor-losses, diffuser, throttle, valves, bend, pump, head-loss]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTE: deck uses "v" for kinematic viscosity ν in several friction/throttle formulas — disambiguated here. -->

# 09 — Flow in Pipes

Practical, mean-velocity treatment of incompressible viscous flow in full pipes: how to quantify friction and
fitting losses (the empirical side that complements the exact solutions of 08). Core tool: the Darcy–Weisbach
head-loss equation with a friction factor λ read from formulas or the Moody diagram, plus minor-loss
coefficients ζ.

## 9.1 Inlet region & kinetic-energy correction ·slides 376–386
- [fig ·slide 382] *(new in the Oct 2026 edition)* A "Flow in pipes" section page carrying four pipe-system
  figures and **no question text**: (1) water at 20 °C leaving a tank through a square-edged entrance into a
  150-mm clean cast-iron pipe — 30 m horizontal, a 12 m rise through two standard elbows, then 60 m horizontal
  past a globe valve to a free jet, with the tank surface $H = 10$ m above the outlet; (2) two tanks joined in
  series by a 1-in and a 2-in pipe, each 20 ft long; (3) "Lite beer" (s.g. 1.00, $\mu = 0.04$ poise) flowing
  from tank A to tank B through 30 m of 210-mm then 60 m of 305-mm smooth pipe, with 6° tapers and a 450-mm
  outlet; (4) three reservoirs joined at a junction J by pipes 1, 2, 3 (elevations $z_1$, $z_2$, $z_3$). No data
  beyond the drawings — treat them as previews of the kind of system the section analyses.
- [def] **Entrance/inlet region:** from the pipe entrance to where the boundary layers meet at the centre and the
  velocity profile is fully developed; its length is the **inlet (entrance) length** $L$. ·slides 378–380
- [eq: entrance-length] Laminar: $L = 0.065\,Re\,d$ (Boussinesq/Nikuradse) or $0.06\,Re\,d$. Turbulent:
  $L = 0.693\,Re^{1/4}d$ (Latzko), or $L \approx (25\text{–}40)\,d$ (Nikuradse). ·slide 381
- [eq: ke-correction] The developing profile carries more kinetic energy than the mean velocity implies; the
  **kinetic-energy correction factor** ζ = (true KE flux)/(KE at mean velocity): **ζ = 2 (laminar,** since
  v_mean = ½u_max), **ζ = 1.09 (turbulent)**. Total inlet head drop $H = \lambda\frac{l}{d}\frac{v^2}{2g} +
  \zeta\frac{v^2}{2g}$. ·slides 383–386

## 9.2 Pipe friction — Darcy–Weisbach ·slides 387–391
- [def] Fully developed head loss $h = (p_1-p_2)/\rho g$. Laminar: $h\propto v$; turbulent: $h\propto v^{1.75\text{–}2}$. ·slide 388
- [eq: darcy-weisbach]
  $$\boxed{\,h = \lambda\frac{l}{d}\frac{v^2}{2g}\,}\qquad\text{(Darcy–Weisbach; λ = pipe friction coefficient)}$$
- [eq: lambda-laminar] From Hagen–Poiseuille ($\Delta p = 32\mu l v/d^2$): ·slide 389
  $$\lambda = \frac{64\mu}{\rho v d} = \frac{64}{Re}\qquad\text{(laminar; independent of wall roughness)}$$
  Roughness has no effect in laminar flow because near-wall inertia is small and viscosity dominates. ·slide 389
- [ex ·slides 390–391] Water 70 °C, new cast iron, v=9.7 ft/s, l=1200 ft, d=6 in, λ=0.0230:
  $h_f = 0.0230\frac{1200}{0.5}\frac{9.7^2}{2\cdot32.2} = 80.6$ ft. ✓ *(slide labels it "assume laminar", but
  λ=0.023 is a turbulent value — a mislabel; the arithmetic uses the given λ. S26, still printed in the Oct 2026
  edition.)*

## 9.3 Turbulent friction — smooth & rough pipes ·slides 392–400
- [def] λ depends on **Re and relative roughness ε/d**. **Smooth** pipe: roughness buried in the viscous sublayer
  ($\varepsilon \le 5\,v^*/\nu$). **Fully rough**: $\varepsilon \ge 70\,v^*/\nu$, roughness reaches the turbulent
  region, λ depends on roughness only (not Re). ·slides 392, 395 *(the slides print "ε ≤ 5u/v" and "ε ≥ 70 u/v" —
  the ratio is inverted; the bounds are $\varepsilon \le 5\nu/v^*$ and $\varepsilon \ge 70\nu/v^*$. S23, still printed in the
  Oct 2026 edition.)*
- [eq: blasius] Smooth-pipe correlations: ·slides 392–393
  - **Blasius:** $\lambda = 0.3164\,Re^{-1/4}$ (Re = 3×10³–1×10⁵);
  - **Nikuradse:** $\lambda = 0.0032 + 0.221\,Re^{-0.237}$ (Re = 10⁵–3×10⁶);
- [eq: karman-nikuradse] **Kármán–Nikuradse** (implicit, Re = 3×10³–3×10⁶):
  $$\frac{1}{\sqrt{\lambda}} = 2\log(Re\sqrt{\lambda}) - 0.8$$
  (slide 393 prints it solved for λ: $\lambda = 1/[\,2\log(Re\sqrt{\lambda}) - 0.8\,]^2$ — the same equation.)
- [eq: itaya] **Itaya** (smooth pipe): ·slide 393
  $$\lambda = \frac{0.314}{0.7 - 1.65\log_{10}Re + (\log_{10}Re)^2}$$
  *[added] check: at $Re = 10^5$ it gives 0.0180, against Blasius 0.0178 — consistent.*
- [eq: rough-pipe] Fully rough pipe (Nikuradse, Re > 900(ε/d) as printed — should be **900(d/ε)**, S24, still printed
  in the Oct 2026 edition): ·slide 396
  $$\lambda = \frac{1}{\big[\,1.74 - 2\log(2\varepsilon/d)\,\big]^2},\qquad \frac{u}{v^*} = 8.48 + 5.75\log\frac{y}{\varepsilon}$$
- [def] Real (irregular) roughness → read λ from the **Moody diagram** (λ vs Re, curves of ε/d). ·slide 397
- [ex ·slides 398–399] Glycerin 68 °F, flowing **120 ft** through a 6-in new wrought pipe, v=10 ft/s,
  μ=3.11×10⁻² lb/ft·s, ρ=2.44 lb/ft³ *(slug units labelled lb — S25, still printed)*:
  $Re = (2.44)(0.5)(10)/(3.11\times10^{-2}) = 392$ → **laminar**; $\lambda = 64/392 = 0.1633$;
  $h_f = 0.1633\,\frac{120}{0.5}\,\frac{10^2}{2(32.2)} = 60.9$ ft. ✓
- [exercise ·slide 400] Oil ν=0.005 ft²/s, γ=54 lb/ft³, l=3600 ft, d=4 in, Re=800 → find Q and head loss.

## 9.4 Non-circular pipes — hydraulic diameter ·slides 401–404
- [derivation] Force balance $\rho g h A = l\tau_0 s$ ⇒ loss set by $A/s$ = **hydraulic mean depth** $m = A/s$. ·slide 402
- [eq: hydraulic-diameter] For a full circular pipe $m = d/4$, so define **hydraulic diameter** $d = 4m$ and use
  $h_f = \lambda\frac{l}{4m}\frac{v^2}{2g}$, with $\lambda = f(Re,\varepsilon/4m)$ and $Re = 4mv/\nu$. ·slide 403
  - rectangle $a\times b$: $4m = \dfrac{2ab}{a+b}$; coaxial (annulus, $d_1$ inner, $d_2$ outer):
    $4m = d_2 - d_1$. ·slide 404

## 9.5 Minor (fitting) losses ·slides 405–409
- [eq: minor-loss] General form (change of area/direction, branch, junction, bend, valve):
  $$h_s = \zeta\frac{v^2}{2g}$$
  v = mean velocity in the unaffected section (use the larger v if it changes across the fitting). ·slide 405
- [eq: sudden-expansion] Sudden **enlargement** (Borda–Carnot): $h_s = \dfrac{(v_1-v_2)^2}{2g} =
  (1-\tfrac{A_1}{A_2})^2\dfrac{v_1^2}{2g}$; at a pipe **outlet** into a tank ($v_2\approx0$) ζ ≈ 1. ·slide 406
- [eq: sudden-contraction] Sudden **contraction** (vena contracta $A_c$, $C_c=A_c/A_2$):
  $h_s = \dfrac{(v_c-v_2)^2}{2g} = \big(\tfrac{1}{C_c}-1\big)^2\dfrac{v_2^2}{2g}$. ·slide 407
- [def] **Inlet loss** from a large vessel: $h_s = \zeta\frac{v^2}{2g}$, ζ = inlet-loss factor depending on inlet
  shape (tabulated). ·slides 408–409

## 9.6 Throttle (choke / orifice / nozzle) ·slides 410–412
- [def] A **throttle** reduces the flow area to add resistance. Three kinds: **choke** (narrow section long vs its
  diameter), **orifice** (small hole), **nozzle** (smaller than an orifice). ·slide 410
- [eq: throttle-C] Discharge: $Q = C\,\dfrac{\pi d^2}{4}\sqrt{\dfrac{2\Delta P}{\rho}}$, with the discharge
  coefficient a function of the **choke number** $\sigma = \dfrac{Q}{\nu l}$: ·slides 411–412
  $$\text{rounded entrance: } C = \frac{1}{1.16 + 6.25\,\sigma^{-0.61}};\qquad
  \text{not rounded: } C = \frac{1}{1 + 5.3/\sqrt{\sigma}}$$
  *(σ^(−0.61) — a superscript exponent; verified against the rendered slide/chart. Experimental range l/d ≈ 1–99.)* ·slide 412

## 9.7 Gradual area change — diffuser ·slides 413–419
- [eq: diffuser] Divergent pipe/diffuser loss $h_s = \zeta\dfrac{(v_1-v_2)^2}{2g}$; ζ varies with the total angle
  θ. Minimum ζ ≈ **0.135 at θ ≈ 5°30′** (circular); ≈ 0.145 at θ ≈ 6° (rectangular). Past that angle the flow
  separates and loss rises sharply. ·slides 414–417
  - Rectangular section: ζ ≈ 1 (almost constant) once θ reaches 50°–60° or more. ·slide 416
  - [def] **Wall effect:** in a two-dimensional duct with small θ, the flow attaches to one of the side walls — a
    *wall-attachment phenomenon*; the reduced pressure on that side deflects the jet. [fig] a tap stream bent by
    a curved spoon, and tea poured from a tilted cup. ·slide 416 *[added] — the general name for
    this is the Coandă effect; the slide does not use that name.*
  - When θ exceeds the minimum-ζ angle in a circular pipe, the flow separates midway, turbulence results and the
    head loss rises suddenly. [fig] flow-visualisation photo: inlet velocity 6 cm/s, Re (inlet) = 900, divergent
    angle 20°. ·slide 417
- [def] **Convergent pipe:** pressure falls in the flow direction, the flow runs freely without extra turbulence,
  and losses other than pipe friction are normally negligible. ·slide 422
- [eq: diffuser-eff] A diffuser converts velocity head to pressure head; **pressure-recovery efficiency**: ·slides 418–419
  $$\eta = \frac{p_2-p_1}{p_{2,th}-p_1} = 1 - \zeta\frac{v_1-v_2}{v_1+v_2} = 1 - \zeta\frac{1-A_1/A_2}{1+A_1/A_2}$$

## 9.8 Worked examples (energy equation) ·slides 420–426 (and old slides 438–441, not in the Oct 2026 edition)
- [ex ·420–421] Expansion 12→24 in, Q=13.2 cfs, head_A=22.1 ft, z drop → **head_B = 11.2 ft**. ✓
- [ex ·old slides 438–439] *(not in the Oct 2026 edition)* Oil SG 0.877, 6→18 in, ΔH: $H_E=45.50$, $H_R=35.16$ ft ⇒
  flow **E→R**, lost head **10.34 ft**. ✓
- [ex ·old slides 440–441] *(not in the Oct 2026 edition)* Hump in a rectangular channel ("venturi flume"):
  $q = h v_1$ with $v_1 = \sqrt{\dfrac{-2gd}{1-[h/(h-d-\delta)]^2}}$. *(open-channel preview; see 10. Old slide 440
  printed "venturi **flame**" — S32; dropped with the slide.)*
- [ex ·423–424] Ideal flow through an inclined pipe + manometer: $v_1 = 3.807$ m/s, **Q = 0.120 m³/s**. ✓
- [ex ·425–426] Discharge from a head of 5.1 m: $v_2 = \sqrt{2g(5.1)} = 10.0$ m/s, **Q = 0.177 m³/s**. ✓

## 9.9 Losses at direction change — bend & elbow ·slides 427–431
- [def] **Bend** = gently curving pipe; loss = pipe friction + direction-change loss + secondary (centrifugal)
  flow; guide vanes reduce it. **Elbow** = sharp curve; flow separates ⇒ larger loss than a bend. ·slides 428–431
- [eq] $h_b = \zeta_b\dfrac{v^2}{2g} = \big(\zeta + \lambda\tfrac{l}{d}\big)\dfrac{v^2}{2g}$ (ζ = bend-effect
  factor, λl/d = friction part). ·slides 429, 431

## 9.10 Branch, junction, valves & cocks ·slides 432–446
- **Branch** (one pipe → several) and **junction** (several → one): each leg $h_s = \zeta\frac{v^2}{2g}$ with
  tabulated ζ. ·slides 432–436
- **Valves/cocks:** $h_s = \zeta\frac{v^2}{2g}$; ζ depends on type and opening. **Gate valve** (ζ vs d′/d),
  **globe valve**, **butterfly valve**, cock, relief/disc/needle/ball/spool valves. ·slides 437–446
  - [data] Circular **butterfly valve** ζ vs plate angle θ: 10°→0.52, 20°→1.54, 30°→3.91, 50°→32.6, 70°→**751**
    (rises steeply). ·slide 442
  - Disc valve $\zeta = 1.3 + 0.2(A/a)^2$; ball/needle $\zeta = 0.5 + 0.15(A/a)^2$; spool (full open) ζ ≈ 3–5.5. ·slides 444–446

## 9.11 Total pipeline loss ·slides 447–449
- [eq: total-loss] $$h = \Big(\lambda\frac{l}{d} + \sum\zeta\Big)\frac{v^2}{2g}$$
  Including the **exit velocity loss** (two tanks, level difference h): $h = \big(\lambda\frac{l}{d} + \sum\zeta
  + 1\big)\frac{v^2}{2g}$. For long lines ($l/d > 2000$) with no small-opening valves, non-friction losses are
  neglected. ·slides 447–448
- [data] Typical design velocities: urban water mains 1.0–1.5 m/s (long runs), up to ~2.5 m/s (short runs);
  hydro headrace 2–5 m/s. ·slide 449

## 9.12 Pumping to higher levels ·slides 450–458 (and old slide 471, not in the Oct 2026 edition)
- [fig ·old slide 471] *(not in the Oct 2026 edition)* "Example 8" — a figure only, no question text: a pipe
  from a sharp-edged entrance through a globe valve (25 % closed), a 12-in bend radius and a 90° long-radius
  elbow to a sharp-edged exit, upper surface at elev. 655.5 ft. The new exercise at slides 455–458 below uses
  the same family of fittings.
- [def] Pump adds energy to lift water. **Total head** $H = H_a + h$ (actual lift $H_a$ + total loss $h = h_s +
  h_d$). ·slide 450
- [eq: pump-power] **Water power** (given to the water) $L_w = \rho g Q H$; **shaft power** $L_s$; pump
  **efficiency** $\eta = L_w/L_s < 1$. ·slide 451
- [def] **Characteristic/head curve** = H vs Q; the loss ($\propto Q^2$) plots as the **resistance curve**, which
  added to $H_a$ gives the **load curve**; the operating discharge is their intersection with the head curve. ·slide 452
- [ex ·slides 453–454] d=60 in, l=6000 ft, delivery 1300 ft below intake (K=0.5, f=0.025), Q=300 cfs:
  v=15.28 ft/s, $h_f=108.76$, $h_m=1.81$, $h_L=110.57$ ft; $P = Q\gamma(\Delta z - h_L) = 300(62.4)(1189.43) =
  2.227\times10^7$ ft·lb/s → **≈ 40{,}491 hp** (delivered, since the water falls 1300 ft). ✓
- [ex ·slides 455–458] *(new in the Oct 2026 edition)* **Pump between two reservoirs.** Water, $\rho = 1.94$
  slug/ft³, is pumped at $Q = 0.2$ ft³/s from reservoir 1 ($z_1 = 20$ ft) to reservoir 2 ($z_2 = 120$ ft) through
  400 ft of 2-in pipe ($d = 2/12$ ft), $\varepsilon/d = 0.001$. Fittings [fig ·455]: sharp entrance, open globe
  valve, pump, 12-in bend radius, screwed regular 90° elbow, half-open gate valve, sharp exit. Find the pump
  horsepower.
  - Energy equation between the two free surfaces, with $h_p$ = head added by the pump: ·slide 456
    $$\frac{p_1}{\rho g} + \frac{v_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{v_2^2}{2g} + z_2 + h_f + \sum h_m - h_p$$
  - $p_1 = p_2$ (both atmospheric), $v_1 \approx v_2 \approx 0$ (large reservoirs), so ·slide 456
    $$\boxed{\,h_p = z_2 - z_1 + h_f + \sum h_m = (z_2 - z_1) + \frac{v^2}{2g}\Big(\frac{fL}{d} + \sum\zeta\Big)\,}$$
    $f$ = Darcy friction factor (the deck's λ), $L$ = pipe length (ft), $\sum\zeta$ = sum of minor-loss
    coefficients.
  - Velocity and Reynolds number: ·slide 456
    $$v = \frac{Q}{A} = \frac{0.2}{\tfrac{\pi}{4}(2/12)^2} = 9.17\ \text{ft/s}$$
    $$Re = \frac{vd}{\nu} = \frac{9.17\,(2/12)}{0.000011} = 139{,}000\ \Rightarrow\ \text{turbulent}$$
  - Friction factor from the Moody chart at $\varepsilon/d = 0.001$: **0.0216** (used in the working). ·slides 457–458
  - Minor-loss coefficients ·slide 457: sharp entrance 0.5; open globe valve (2 in) 6.9; 12-in bend 0.25;
    regular 90° elbow 0.95; half-closed gate valve 3.8; sharp exit 1.0; $\sum\zeta = 13.4$.
  - Pump head ·slide 458:
    $$h_p = 100 + \frac{9.17^2}{2(32.2)}\Big(\frac{0.0216(400)}{2/12} + 13.4\Big) = 100 + 85 = 185\ \text{ft}$$
  - Power given to the water ·slide 458:
    $$P = \rho g Q h_p = [1.94(32.2)](0.2)(185) \approx 2300\ \text{ft}\cdot\text{lbf/s};\qquad \frac{2300}{550} = \mathbf{4.2\ hp}$$
    With a pump efficiency of 70–80 %, the required input ≈ **6 hp**. ✓ *(Python: $v = 9.167$ ft/s,
    $Re = 1.389\times10^5$; Colebrook gives $f = 0.02156$; loss term 85.1 ft; $h_p = 185.1$ ft;
    $P = 2313$ ft·lbf/s = 4.21 hp; 4.21/0.7 = 6.0 hp, 4.21/0.8 = 5.3 hp.)*
  > ⚠ VERIFY S79 ·slide 457 — the slide says "From Moody chart: for ε/d = 0.001, **f = 0.0219**", then substitutes
  > **0.0216** on 457 and 458. 0.0216 is the right value (Colebrook at $Re = 1.39\times10^5$, $\varepsilon/d = 0.001$
  > gives 0.02156). Using 0.0219 would give $h_p = 186$ ft — the final 4.2 hp is unaffected.
  >
  > ⚠ VERIFY S80 ·slide 457 — the heading prints "[**hf** = 120 ft – 20 ft + $\frac{v^2}{2g}(\frac{fL}{d} + \sum\zeta)$]".
  > That expression is the **pump head $h_p$**; $h_f$ is the pipe-friction loss alone.
  >
  > ⚠ VERIFY S81 ·slides 455–456 — the problem gives ρ but **no viscosity**; the solution uses
  > $\nu = 0.000011$ ft²/s (water near 68 °F) for Re, without stating it. Re, and so f, cannot be found from the
  > question as set. (The slide also writes ν as "v".)

### Cross-references
- Friction factor λ derives from Hagen–Poiseuille & turbulent profiles in **08-viscous-flow**; sudden-expansion
  loss is the Borda–Carnot result of **07-momentum**.
- Uses the energy equation of **06-energy-bernoulli** throughout; open-channel loss (Chézy/Manning) parallels
  this in **10-open-channel-flow**.

### Verification notes for this section
- Verified: λ=64/Re; Blasius 0.3164Re^−¼; Kármán–Nikuradse 1/√λ=2log(Re√λ)−0.8; Itaya; rough-pipe λ;
  hydraulic diameter (rectangle 2ab/(a+b), annulus d₂−d₁); sudden expansion/contraction; diffuser η; butterfly ζ
  table; example results (80.6 ft, 60.9 ft, 11.2 ft, 10.34 ft, 0.120/0.177 m³/s, 40,491 hp, and the new
  pump exercise: 9.17 ft/s, Re 139,000, Σζ 13.4, 185 ft, 4.2 hp).
- Throttle C formula superscript recovered by viewing the slide (σ^−0.61). Slide 391 "assume laminar" mislabel
  noted inline (S26).
- Oct 2026 edition (rechecked on rendered pages 376–458): S23 (392, 395), S24 (396), S25 (398), S26 (391) are
  **still printed**; S32 went with old slide 440, which is **not in the new edition**. New flags S79–S81 on the
  new pump exercise (455–457). Slide 398 now states the pipe length (120 ft) the earlier KB entry lacked.
- Rendering note: some viewers drop the superscript ² and ³ glyphs on these slides (e.g. "slugs/ft" for
  slugs/ft³ on 455); the PDF text layer carries them. Read a missing exponent from context, not as an error.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
