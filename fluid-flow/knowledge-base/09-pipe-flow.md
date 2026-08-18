---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "09 — Flow in Pipes"
slides: "387-478"
file_role: topic
subtopics:
  - "inlet/entrance region & length; kinetic-energy correction factor"
  - "pipe friction (Darcy–Weisbach); laminar λ=64/Re"
  - "turbulent friction: smooth (Blasius, Nikuradse, Kármán–Nikuradse) & rough pipes; Moody diagram"
  - "non-circular pipes: hydraulic mean depth / hydraulic diameter"
  - "minor losses: sudden & gradual area change, contraction, diffuser & recovery efficiency"
  - "throttle (choke/orifice/nozzle) discharge coefficient"
  - "losses at bends, elbows, branches, junctions, valves & cocks"
  - "total pipeline loss"
  - "pumping to higher levels: heads, water power, efficiency, characteristic & resistance curves"
key_equations: [entrance-length, ke-correction, darcy-weisbach, lambda-laminar, blasius, karman-nikuradse, rough-pipe, hydraulic-diameter, minor-loss, sudden-expansion, sudden-contraction, throttle-C, diffuser-eff, total-loss, pump-power]
prerequisites: ["06-energy-bernoulli", "08-viscous-flow (Hagen–Poiseuille, boundary layer)"]
leads_to: ["10-open-channel-flow"]
verification_flags: 0
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

## 9.1 Inlet region & kinetic-energy correction ·slides 388–398
- [def] **Entrance/inlet region:** from the pipe entrance to where the boundary layers meet at the centre and the
  velocity profile is fully developed; its length is the **inlet (entrance) length** $L$. ·slides 389–391
- [eq: entrance-length] Laminar: $L = 0.065\,Re\,d$ (Boussinesq/Nikuradse) or $0.06\,Re\,d$. Turbulent:
  $L = 0.693\,Re^{1/4}d$ (Latzko), or $L \approx (25\text{–}40)\,d$ (Nikuradse). ·slide 392
- [eq: ke-correction] The developing profile carries more kinetic energy than the mean velocity implies; the
  **kinetic-energy correction factor** ζ = (true KE flux)/(KE at mean velocity): **ζ = 2 (laminar,** since
  v_mean = ½u_max), **ζ = 1.09 (turbulent)**. Total inlet head drop $H = \lambda\frac{l}{d}\frac{v^2}{2g} +
  \zeta\frac{v^2}{2g}$. ·slides 393–398

## 9.2 Pipe friction — Darcy–Weisbach ·slides 399–404
- [def] Fully developed head loss $h = (p_1-p_2)/\rho g$. Laminar: $h\propto v$; turbulent: $h\propto v^{1.75\text{–}2}$. ·slide 401
- [eq: darcy-weisbach]
  $$\boxed{\,h = \lambda\frac{l}{d}\frac{v^2}{2g}\,}\qquad\text{(Darcy–Weisbach; λ = pipe friction coefficient)}$$
- [eq: lambda-laminar] From Hagen–Poiseuille ($\Delta p = 32\mu l v/d^2$): ·slide 402
  $$\lambda = \frac{64\mu}{\rho v d} = \frac{64}{Re}\qquad\text{(laminar; independent of wall roughness)}$$
  Roughness has no effect in laminar flow because near-wall inertia is small and viscosity dominates. ·slide 402
- [ex ·slides 403–404] Water 70 °C, new cast iron, v=9.7 ft/s, l=1200 ft, d=6 in, λ=0.0230:
  $h_f = 0.0230\frac{1200}{0.5}\frac{9.7^2}{2\cdot32.2} = 80.6$ ft. ✓ *(slide labels it "assume laminar", but
  λ=0.023 is a turbulent value — a mislabel; the arithmetic uses the given λ.)*

## 9.3 Turbulent friction — smooth & rough pipes ·slides 405–413
- [def] λ depends on **Re and relative roughness ε/d**. **Smooth** pipe: roughness buried in the viscous sublayer
  ($\varepsilon \le 5\,v^*/\nu$). **Fully rough**: $\varepsilon \ge 70\,v^*/\nu$, roughness reaches the turbulent
  region, λ depends on roughness only (not Re). ·slides 405, 408
- [eq: blasius] Smooth-pipe correlations: ·slides 405–406
  - **Blasius:** $\lambda = 0.3164\,Re^{-1/4}$ (Re = 3×10³–1×10⁵);
  - **Nikuradse:** $\lambda = 0.0032 + 0.221\,Re^{-0.237}$ (Re = 10⁵–3×10⁶);
- [eq: karman-nikuradse] **Kármán–Nikuradse** (implicit, Re = 3×10³–3×10⁶):
  $$\frac{1}{\sqrt{\lambda}} = 2\log(Re\sqrt{\lambda}) - 0.8$$
- [eq: rough-pipe] Fully rough pipe (Nikuradse, Re > 900(ε/d)): ·slide 409
  $$\lambda = \frac{1}{\big[\,1.74 - 2\log(2\varepsilon/d)\,\big]^2},\qquad \frac{u}{v^*} = 8.48 + 5.75\log\frac{y}{\varepsilon}$$
- [def] Real (irregular) roughness → read λ from the **Moody diagram** (λ vs Re, curves of ε/d). ·slide 410
- [ex ·slides 411–412] Glycerin 68 °F, d=6 in, v=10 ft/s, μ=3.11×10⁻² lb/ft·s, ρ=2.44 lb/ft³:
  $Re = (2.44)(0.5)(10)/(3.11\times10^{-2}) = 392$ → **laminar**; $\lambda = 64/392 = 0.163$; $h_f = 60.9$ ft. ✓
- [exercise ·slide 413] Oil ν=0.005 ft²/s, γ=54 lb/ft³, l=3600 ft, d=4 in, Re=800 → find Q and head loss.

## 9.4 Non-circular pipes — hydraulic diameter ·slides 414–418
- [derivation] Force balance $\rho g h A = l\tau_0 s$ ⇒ loss set by $A/s$ = **hydraulic mean depth** $m = A/s$. ·slide 415
- [eq: hydraulic-diameter] For a full circular pipe $m = d/4$, so define **hydraulic diameter** $d = 4m$ and use
  $h_f = \lambda\frac{l}{4m}\frac{v^2}{2g}$, with $\lambda = f(Re,\varepsilon/4m)$ and $Re = 4mv/\nu$. ·slide 416
  - rectangle $a\times b$: $4m = \dfrac{2ab}{a+b}$; coaxial (annulus, $d_1$ inner, $d_2$ outer):
    $4m = d_2 - d_1$. ·slide 418

## 9.5 Minor (fitting) losses ·slides 419–424
- [eq: minor-loss] General form (change of area/direction, branch, junction, bend, valve):
  $$h_s = \zeta\frac{v^2}{2g}$$
  v = mean velocity in the unaffected section (use the larger v if it changes across the fitting). ·slide 420
- [eq: sudden-expansion] Sudden **enlargement** (Borda–Carnot): $h_s = \dfrac{(v_1-v_2)^2}{2g} =
  (1-\tfrac{A_1}{A_2})^2\dfrac{v_1^2}{2g}$; at a pipe **outlet** into a tank ($v_2\approx0$) ζ ≈ 1. ·slide 421
- [eq: sudden-contraction] Sudden **contraction** (vena contracta $A_c$, $C_c=A_c/A_2$):
  $h_s = \dfrac{(v_c-v_2)^2}{2g} = \big(\tfrac{1}{C_c}-1\big)^2\dfrac{v_2^2}{2g}$. ·slide 422
- [def] **Inlet loss** from a large vessel: $h_s = \zeta\frac{v^2}{2g}$, ζ = inlet-loss factor depending on inlet
  shape (tabulated). ·slides 423–424

## 9.6 Throttle (choke / orifice / nozzle) ·slides 425–428
- [def] A **throttle** reduces the flow area to add resistance. Three kinds: **choke** (narrow section long vs its
  diameter), **orifice** (small hole), **nozzle** (smaller than an orifice). ·slide 425
- [eq: throttle-C] Discharge: $Q = C\,\dfrac{\pi d^2}{4}\sqrt{\dfrac{2\Delta P}{\rho}}$, with the discharge
  coefficient a function of the **choke number** $\sigma = \dfrac{Q}{\nu l}$: ·slides 426–427
  $$\text{rounded entrance: } C = \frac{1}{1.16 + 6.25\,\sigma^{-0.61}};\qquad
  \text{not rounded: } C = \frac{1}{1 + 5.3/\sqrt{\sigma}}$$
  *(σ^(−0.61) — a superscript exponent; verified against the rendered slide/chart. Experimental range l/d ≈ 1–99.)* ·slide 428

## 9.7 Gradual area change — diffuser ·slides 429–435
- [eq: diffuser] Divergent pipe/diffuser loss $h_s = \zeta\dfrac{(v_1-v_2)^2}{2g}$; ζ varies with the total angle
  θ. Minimum ζ ≈ **0.135 at θ ≈ 5°30′** (circular); ≈ 0.145 at θ ≈ 6° (rectangular). Past that angle the flow
  separates and loss rises sharply. ·slides 430–433
- [eq: diffuser-eff] A diffuser converts velocity head to pressure head; **pressure-recovery efficiency**: ·slides 434–435
  $$\eta = \frac{p_2-p_1}{p_{2,th}-p_1} = 1 - \zeta\frac{v_1-v_2}{v_1+v_2} = 1 - \zeta\frac{1-A_1/A_2}{1+A_1/A_2}$$

## 9.8 Worked examples (energy equation) ·slides 436–446
- [ex ·436–437] Expansion 12→24 in, Q=13.2 cfs, head_A=22.1 ft, z drop → **head_B = 11.2 ft**. ✓
- [ex ·438–439] Oil SG 0.877, 6→18 in, ΔH: $H_E=45.50$, $H_R=35.16$ ft ⇒ flow **E→R**, lost head **10.34 ft**. ✓
- [ex ·440–441] Hump in a rectangular channel ("venturi flume"): $q = h v_1$ with
  $v_1 = \sqrt{\dfrac{-2gd}{1-[h/(h-d-\delta)]^2}}$. *(open-channel preview; see 10.)*
- [ex ·443–444] Ideal flow through an inclined pipe + manometer: $v_1 = 3.807$ m/s, **Q = 0.120 m³/s**. ✓
- [ex ·445–446] Discharge from a head of 5.1 m: $v_2 = \sqrt{2g(5.1)} = 10.0$ m/s, **Q = 0.177 m³/s**. ✓

## 9.9 Losses at direction change — bend & elbow ·slides 447–451
- [def] **Bend** = gently curving pipe; loss = pipe friction + direction-change loss + secondary (centrifugal)
  flow; guide vanes reduce it. **Elbow** = sharp curve; flow separates ⇒ larger loss than a bend. ·slides 448–451
- [eq] $h_b = \zeta_b\dfrac{v^2}{2g} = \big(\zeta + \lambda\tfrac{l}{d}\big)\dfrac{v^2}{2g}$ (ζ = bend-effect
  factor, λl/d = friction part). ·slides 449, 451

## 9.10 Branch, junction, valves & cocks ·slides 452–466
- **Branch** (one pipe → several) and **junction** (several → one): each leg $h_s = \zeta\frac{v^2}{2g}$ with
  tabulated ζ. ·slides 452–456
- **Valves/cocks:** $h_s = \zeta\frac{v^2}{2g}$; ζ depends on type and opening. **Gate valve** (ζ vs d′/d),
  **globe valve**, **butterfly valve**, cock, relief/disc/needle/ball/spool valves. ·slides 457–466
  - [data] Circular **butterfly valve** ζ vs plate angle θ: 10°→0.52, 20°→1.54, 30°→3.91, 50°→32.6, 70°→**751**
    (rises steeply). ·slide 462
  - Disc valve $\zeta = 1.3 + 0.2(A/a)^2$; ball/needle $\zeta = 0.5 + 0.15(A/a)^2$; spool (full open) ζ ≈ 3–5.5. ·slides 464–466

## 9.11 Total pipeline loss ·slides 467–470
- [eq: total-loss] $$h = \Big(\lambda\frac{l}{d} + \sum\zeta\Big)\frac{v^2}{2g}$$
  Including the **exit velocity loss** (two tanks, level difference h): $h = \big(\lambda\frac{l}{d} + \sum\zeta
  + 1\big)\frac{v^2}{2g}$. For long lines ($l/d > 2000$) with no small-opening valves, non-friction losses are
  neglected. ·slides 467–469
- [data] Typical design velocities: urban water mains 1.0–1.5 m/s (long runs), up to ~2.5 m/s (short runs);
  hydro headrace 2–5 m/s. ·slide 470

## 9.12 Pumping to higher levels ·slides 471–478
- [def] Pump adds energy to lift water. **Total head** $H = H_a + h$ (actual lift $H_a$ + total loss $h = h_s +
  h_d$). ·slide 472
- [eq: pump-power] **Water power** (given to the water) $L_w = \rho g Q H$; **shaft power** $L_s$; pump
  **efficiency** $\eta = L_w/L_s < 1$. ·slide 473
- [def] **Characteristic/head curve** = H vs Q; the loss ($\propto Q^2$) plots as the **resistance curve**, which
  added to $H_a$ gives the **load curve**; the operating discharge is their intersection with the head curve. ·slides 474–476
- [ex ·slides 477–478] d=60 in, l=6000 ft, delivery 1300 ft below intake (K=0.5, f=0.025), Q=300 cfs:
  v=15.28 ft/s, $h_f=108.76$, $h_m=1.81$, $h_L=110.57$ ft; $P = Q\gamma(\Delta z - h_L) = 300(62.4)(1189.43) =
  2.227\times10^7$ ft·lb/s → **≈ 40{,}491 hp** (delivered, since the water falls 1300 ft). ✓

### Cross-references
- Friction factor λ derives from Hagen–Poiseuille & turbulent profiles in **08-viscous-flow**; sudden-expansion
  loss is the Borda–Carnot result of **07-momentum**.
- Uses the energy equation of **06-energy-bernoulli** throughout; open-channel loss (Chézy/Manning) parallels
  this in **10-open-channel-flow**.

### Verification notes for this section
- 0 physics errors. Verified: λ=64/Re; Blasius 0.3164Re^−¼; Kármán–Nikuradse 1/√λ=2log(Re√λ)−0.8; rough-pipe λ;
  hydraulic diameter (rectangle 2ab/(a+b), annulus d₂−d₁); sudden expansion/contraction; diffuser η; butterfly ζ
  table; example results (80.6 ft, 60.9 ft, 11.2 ft, 10.34 ft, 0.120/0.177 m³/s, 40,491 hp).
- Throttle C formula superscript recovered by viewing the slide (σ^−0.61). Slide 404 "assume laminar" mislabel
  noted inline (non-substantive).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
