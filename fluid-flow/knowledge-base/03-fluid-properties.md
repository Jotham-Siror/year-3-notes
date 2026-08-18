---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "03 — Fluid Properties (Matter, Units, Viscosity, Surface Tension, Compressibility, Perfect Gas)"
slides: "30-76"
file_role: topic
subtopics:
  - "matter & defining fluid characteristics (compressibility, viscosity, continuum, ideal/perfect fluid)"
  - "units & dimensions (MKS, CGS, BG, SI; primary & derived dimensions)"
  - "density, specific gravity, specific volume"
  - "viscosity & Couette flow; Newton's law of viscosity; dynamic vs kinematic viscosity; viscosity index"
  - "Newtonian vs non-Newtonian fluids; rheological diagram"
  - "surface tension (drop pressure)"
  - "capillarity (capillary rise)"
  - "compressibility & bulk modulus; speed of a pressure wave"
  - "perfect gas law & polytropic process"
key_equations: [newton-viscosity, kinematic-visc, specific-gravity, drop-dP, capillary-rise, bulk-modulus, wave-speed, perfect-gas, polytropic]
prerequisites: ["01-course-admin"]
leads_to: ["04-fluid-statics", "08-viscous-flow"]
verification_flags: 2
tags: [density, viscosity, couette, newtonian, non-newtonian, surface-tension, capillarity, bulk-modulus, compressibility, perfect-gas, polytropic, units]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTATION NOTE: the deck uses the symbol τ for BOTH shear stress AND surface tension. This KB uses
  τ = shear stress and σ = surface tension to avoid ambiguity; slide provenance is unchanged. -->

# 03 — Fluid Properties

## 3.1 Matter & defining fluid characteristics ·slides 30–34
- [def] A **solid** shows elasticity under tension, compression, or shear. A **fluid** is defined by:
  **compressibility** (raises pressure to resist compression) and **viscosity** (resists two layers sliding
  over each other). ·slide 31
- [def] Generally: **liquids ≈ incompressible** (but consider compressibility if highly pressurized);
  **gases ≈ compressible** (but compressibility may be ignored for small pressure changes). ·slide 32
- [def] **Continuum:** molecules are in constant motion; because the molecular mean free path is very small
  relative to flow dimensions, a fluid is treated as a continuous, isotropic substance. ·slide 33
  > ⚠ VERIFY ·slide 33 — slide states mean free path "about 0.06 **pm**". That is ~6×10⁻¹⁴ m (nuclear scale),
  > physically wrong. Air's molecular mean free path at STP is ≈ **68 nm ≈ 0.068 µm**, so the intended unit is
  > almost certainly **µm** (micrometre), not pm. See _verification-log.md.
- [def] Ideal/perfect fluid: a gas obeying Boyle's–Charles' law is a **perfect/ideal gas**. A fluid with *no*
  viscosity and *no* compressibility does not exist; a fluid with compressibility but no viscosity is a
  **perfect fluid**. ·slide 34

## 3.2 Units & dimensions ·slides 35–44
- [def] Physical quantities have **base units**; combinations are **derived units**. A system taking length,
  mass, time as basic is an **absolute system**. ·slide 36
- Systems: **MKS** (m, N, K/°C, kg, s); **CGS** (cm, dyne, g, K, s); **British Gravitational (BG)** (lbf, slug,
  ft, °R, s); **SI** (developed from MKS; one unit per quantity). ·slides 37–40
- [table] Primary dimensions & SI/BG conversions ·slide 41:
  Mass {M} kg / slug, 1 slug = 14.5939 kg · Length {L} m / ft, 1 ft = 0.3048 m ·
  Time {T} s / s · Temperature {θ} K / °R, 1 K = 1.8 °R.
- Other SI base units: electric current — ampere (A); amount — mole (mol); luminous intensity — candela (cd). ·slide 42
- [table] Representative derived dimensions ·slide 44: Area {L²}; Volume {L³}; Velocity {LT⁻¹}; Acceleration
  {LT⁻²}; Pressure/stress {ML⁻¹T⁻²} (Pa = N/m², 1 lbf/ft² = 47.88 Pa); Energy/work {ML²T⁻²} (J, 1 ft·lbf =
  1.35558 J); Power {ML²T⁻³} (W); Density {ML⁻³} (1 slug/ft³ = 515.4 kg/m³); Viscosity {ML⁻¹T⁻¹}; Specific heat
  {L²T⁻²θ⁻¹}.
  *(Table has minor slide typos: "35.335 ft³" for 1 m³ — standard value is 35.315 ft³; BG viscosity unit printed
  "slug/m/s" should be slug/(ft·s); "Lbg/ft²"→lbf/ft². Logged as minor.)*

## 3.3 Density, specific gravity, specific volume ·slides 45–46
- [def] **Density** ρ = mass / volume. Gas density varies with pressure; liquid density ≈ fixed. ·slide 45
  Heaviest liquid: mercury ρ ≈ 13,580 kg/m³. Lightest gas: hydrogen ρ ≈ 0.0838 kg/m³ (ratio ≈ 162,000×).
  > ⚠ VERIFY ·slide 45 — slide says "liquids are 3 **times** denser than gases at 1 atm". Water (≈1000) vs air
  > (≈1.2) is ≈ 800–1000×, i.e. ~**3 orders of magnitude**, not 3×. Read as "3 orders of magnitude." See log.
- [eq: specific-gravity] **Specific gravity** SG = ρ / ρ_reference (water at 4 °C for liquids; air at 1 atm for
  gases). Example SG(Hg) = 13500/1000 = 13.6. **Specific volume** $v = 1/\rho$ (m³/kg). ·slide 46

## 3.4 Viscosity & Couette flow ·slides 47–54
- [fig ·slides 47–48] Two parallel plates, gap $h$ (fig labels it H), lower fixed, upper dragged at velocity
  $U$ by force $F$; fluid fills the gap. Below $Uh/\nu < 1500$ the flow stays laminar with a **linear** velocity
  profile — **Couette flow**.
- [eq] Shear stress ∝ U, ∝ 1/h: ·slide 49
  $$\tau = \frac{F}{A} = \mu\frac{U}{h}$$
  $\mu$ = **viscosity** (dynamic/absolute viscosity); the flow is a **shear flow**.
- [eq: newton-viscosity] For a general shear flow, at distance $y$ from the wall: ·slide 50
  $$\boxed{\,\tau = \mu\frac{du}{dy}\,}\qquad\text{— Newton's law of viscosity}$$
- [def] Temperature dependence: **gases** — μ **increases** with T (more molecular motion/mixing); **liquids** —
  μ **decreases** with T (molecules separate, attraction falls). ·slide 51
- [eq: kinematic-visc] **Kinematic viscosity** $\nu = \mu/\rho$ (units m²/s). ·slides 52–53
  Units: μ in Pa·s (SI), g/(cm·s) = **Poise** (P, CGS/absolute). ν: 1 cm²/s = 1 **Stokes** (St);
  1 St = 1×10⁻⁴ m²/s; 1 cSt = 1×10⁻⁶ m²/s. Oils: ν ≈ 30–100 cSt.
- [def] **Viscosity Index (VI)**: dimensionless temperature-sensitivity measure; VI 100 = least sensitive,
  0 = most sensitive; additives can push VI > 100. ·slide 54

## 3.5 Newtonian vs non-Newtonian fluids ·slides 55–56
- [def] **Newtonian fluid**: τ ∝ du/dy (water, oil, air). **Non-Newtonian**: does not obey Newton's law
  (pulp, high-molecular-weight solutions, asphalt). ·slide 55
- [fig ·slide 56] **Rheological diagram** — shear stress τ vs shear strain rate γ̇:
  - **Newtonian** — straight line through the origin, slope = μ₀;
  - **Bingham plastic** — straight line but with a yield stress τ₀ intercept (flows only past τ₀);
  - **Herschel–Bulkley** — yield stress τ₀ then a curve (nonlinear past yield);
  - **Shear-thinning (pseudoplastic)** — concave-down curve from origin (apparent viscosity falls with γ̇);
  - **Shear-thickening (dilatant)** — concave-up curve from origin (apparent viscosity rises with γ̇).

## 3.6 Surface tension ·slides 57–59
- [def] **Surface tension** σ = tensile force per unit length on a section of a liquid's free surface; the
  surface tends to shrink (acts like a stretched elastic film). A dewdrop is spherical for this reason, and its
  internal pressure exceeds the outside. ·slides 57–58
- [derivation/eq: drop-dP] Force balance on a liquid drop of diameter $d$ (circumference tension =
  pressure × cut area): $\sigma\,\pi d = \Delta P\,\dfrac{\pi d^2}{4}$ ·slide 59
  $$\boxed{\,\Delta P = \frac{4\sigma}{d} \;\Big(=\frac{2\sigma}{r}\Big)\,}$$
  *(Deck writes σ as τ. Result is the single-surface drop form; a bubble with two surfaces would give 8σ/d.)*

## 3.7 Capillarity ·slides 60–64
- [def] **Capillarity**: interplay of surface tension and the liquid–solid adhesive force. ·slide 60
- [derivation/eq: capillary-rise] Balance of the adhesive (surface-tension) pull up the wall against the weight
  of the raised column: $\pi d\,\sigma\cos\theta = \dfrac{\pi d^2}{4}\rho g h$ ·slide 61
  $$\boxed{\,h = \frac{4\sigma\cos\theta}{\rho g d}\,}$$
  where $d$ = tube diameter, $\theta$ = contact angle, $\rho$ = liquid density, $h$ = mean rise. ·slide 62
  [fig ·slide 61] Tube dipped in liquid: meniscus rises $h$; wall force components $\sigma\pi d\cos\theta$
  (vertical, lifting) and $\sigma\pi d\sin\theta$; contact angle $\theta$.
- [data] Glass tube, $d$ in mm, $h$ in mm ·slide 63: Water $h = 30/d$; Alcohol $h = 11.6/d$;
  Mercury $h = -10/d$ (negative ⇒ depression, θ > 90°). *(Water 30/d verified: 4σcosθ/ρgd with σ≈0.073, θ≈0.)*
- [exercise ·slide 64] (1) Compute the column heights of the slide-63 liquids for $d = 10$ mm.
  (2) Look up densities & surface tensions and back-calculate the contact angle θ for each.

## 3.8 Compressibility & bulk modulus ·slides 65–70
- [derivation] Volume $V$ at pressure $p$ drops by $\Delta V$ under a rise $\Delta p$. Cubic dilatation
  $\Delta V/V$; **bulk modulus** $K$: ·slides 66–67
  $$K = \frac{\Delta P}{\Delta V/V} = -V\frac{dP}{dV} = \rho\frac{dP}{d\rho}\qquad\text{[eq: bulk-modulus]}$$
  [fig ·slide 66] Cube of volume $V_0$, faces area $A$, compressed on all sides by forces $F$ to $V_0-\Delta V$.
- [def] **Compressibility** $\beta = 1/K$ (indicates how compressible the fluid is). Values ·slides 68–69:
  water $K = 2.06\times10^{9}$ Pa; air $K = 1.4\times10^{5}$ Pa (adiabatic, = γP); water
  $\beta = 4.85\times10^{-10}$ Pa⁻¹ (shrinks only ≈0.005 % under +1 atm). *(All three verified consistent.)*
- [eq: wave-speed] $K$ sets the speed $a$ of a pressure (sound) wave in the liquid: ·slide 70
  $$a = \sqrt{\frac{dP}{d\rho}} = \sqrt{\frac{K}{\rho}}$$
- [homework ·slide 71] Obtain density, SG, specific volume, viscosity, surface tension, compressibility for at
  least five fluids in BG, SI and CGS units.

## 3.9 Perfect gas & polytropic process ·slides 72–76
- [eq: perfect-gas] With $p$ pressure, $v$ specific volume, $T$ absolute temperature, $R$ gas constant
  (Boyle's–Charles' law): ·slides 72–73
  $$\boxed{\,pv = RT\,}\qquad (v = 1/\rho)$$
  Equation of state; a gas obeying it is a **perfect/ideal gas** (strictly, none exist, but a gas far above its
  liquefaction temperature is well approximated). [Q on slide 73: units of R → J/(kg·K).]
- [eq: polytropic] State change of a perfect gas: ·slides 74–75
  $$pv^{n} = \text{constant}$$
  $n$ = **polytropic exponent**, ranging $0\to\infty$, giving five process types: **isobaric, isothermal,
  polytropic, adiabatic, isochoric**.
- [def] For an **adiabatic** change $n = \gamma = C_p/C_v$ (ratio of specific heats / isentropic index). ·slide 76
  *(Deck writes γ as "K" here — not the bulk modulus K of §3.8; watch the symbol clash.)*

### Cross-references
- Viscosity & Newton's law underpin all of **08-viscous-flow** (Navier–Stokes, laminar profiles).
- Polytropic/perfect-gas relations are reused for atmospheric pressure variation in **04-fluid-statics** (§ gas column).
- Bulk modulus / wave speed connect to compressibility effects noted in **05-flow-fundamentals**.

### Verification notes for this section
- 2 flags logged: mean free path units (slide 33), "3× denser" (slide 45).
- Verified correct: drop ΔP=4σ/d, capillary h=4σcosθ/ρgd (and water 30/d), K/β values for water & air, wave
  speed a=√(K/ρ), perfect-gas & polytropic relations.
- Minor slide typos (units table, slide 44) logged lightly, not as physics errors.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
