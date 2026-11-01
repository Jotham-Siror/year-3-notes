---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "03 — Fluid Properties (Matter, Units, Viscosity, Surface Tension, Compressibility, Perfect Gas, Dimensional Homogeneity)"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "30-65"
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
  - "dimensional homogeneity; BG/SI weight–mass worked example (new in the Oct 2026 edition)"
key_equations: [newton-viscosity, kinematic-visc, specific-gravity, drop-dP, capillary-rise, bulk-modulus, wave-speed, perfect-gas, polytropic, dimensional-homogeneity]
prerequisites: ["01-course-admin"]
leads_to: ["04-fluid-statics", "06-energy-bernoulli", "08-viscous-flow"]
verification_flags: 6   # s33 and s43 still printed + new S33–S36 (Oct 2026 edition); S1 fixed in that edition
tags: [density, viscosity, couette, newtonian, non-newtonian, surface-tension, capillarity, bulk-modulus, compressibility, perfect-gas, polytropic, units, dimensional-homogeneity]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTATION NOTE: the deck uses the symbol τ for BOTH shear stress AND surface tension. This KB uses
  τ = shear stress and σ = surface tension to avoid ambiguity; slide provenance is unchanged. -->

# 03 — Fluid Properties

## 3.1 Matter & defining fluid characteristics ·slides 30–34
- [fig ·slide 30] Tree diagram: matter → solids, and fluids ("compressible?") → liquids (take the shape of the
  vessel) and gases (fill the container).
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
  > *(still printed in the Oct 2026 edition)*
- [def] Ideal/perfect fluid: a gas obeying Boyle's–Charles' law is a **perfect/ideal gas**. A fluid with *no*
  viscosity and *no* compressibility does not exist; a fluid with compressibility but no viscosity is a
  **perfect fluid**. ·slide 34

## 3.2 Units & dimensions ·slides 35–42
- [fig ·slide 35] Section title slide with a "Fluid properties" chart: density, specific gravity, viscosity,
  vapour pressure, specific weight, specific volume.
- [def] Physical quantities have **base units**; combinations are **derived units**. A system taking length,
  mass, time as basic is an **absolute system**; the slide's diagram names MKS, CGS, BG and SI. ·slide 36
- [table] Absolute systems of units ·slide 37 *(one table in the Oct 2026 edition; three separate slides in the
  Jul 2026 edition)*:

  | Dimension | MKS | CGS | BG | SI |
  |---|---|---|---|---|
  | Length {L} | metre (m) | centimetre (cm) | foot (ft) | metre |
  | Force | newton (N) | dyne | pound-force (lbf) | newton |
  | Mass {M} | kilogram (kg) | gram (g) | slug | kg |
  | Temperature {θ} | K / °C | kelvin (K) | degree Rankine (°R) | K |
  | Time | second | second (s) | second (s) | second (s) |

- **SI** (Le Système International d'Unités): developed from MKS; consistent; one unit per quantity. ·slide 38
- [table] Primary dimensions & SI/BG conversions ·slide 39:
  Mass {M} kg / slug, 1 slug = 14.5939 kg · Length {L} m / ft, 1 ft = 0.3048 m ·
  Time {T} s / s · Temperature {θ} K / °R, 1 K = 1.8 °R.
- Other SI base units: electric current — ampere (A); amount — mole (mol); luminous intensity — candela (cd). ·slide 40
- [def] A **dimension** is "the index number of the combination of base units expressing a physical quantity":
  length {L}, mass {M}, time {T}. ·slide 41
- [table] Representative derived dimensions ·slide 42: Area {L²} (1 m² = 10.764 ft²); Volume {L³}; Velocity
  {LT⁻¹} (1 ft/s = 0.3048 m/s); Acceleration {LT⁻²} (1 ft/s² = 0.3048 m/s²); Pressure/stress {ML⁻¹T⁻²}
  (Pa = N/m², 1 lbf/ft² = 47.88 Pa); Angular velocity {T⁻¹} (s⁻¹ in both systems); Energy/work {ML²T⁻²} (J,
  1 ft·lbf printed as 1.35558 J); Power {ML²T⁻³} (W, 1 ft·lbf/s printed as 1.35558 W); Density {ML⁻³}
  (1 slug/ft³ = 515.4 kg/m³); Viscosity {ML⁻¹T⁻¹} (1 slug/(ft·s) = 47.88 kg/(m·s)); Specific heat {L²T⁻²θ⁻¹}
  (1 m²/(s²·K) = 5.980 ft²/(s²·°R)).
  *(Table has minor slide typos: "35.335 ft³" for 1 m³ — standard value is 35.315 ft³; BG viscosity unit printed
  "slug/m/s" should be slug/(ft·s); "Lbg/ft²"→lbf/ft². Logged as minor. Oct 2026 edition: "Lbg/ft²" is **fixed**
  (now reads "Lbf/ft²"); 35.335 and "Slugs/m/s" are **still printed**.)*
  > ⚠ VERIFY S33 ·slide 42 — energy and power rows print "1 ft·lbf = **1.35558** J" and "1 ft·lbf/s = 1.35558 W".
  > Correct: $1\ \text{ft}\cdot\text{lbf} = 0.3048\ \text{m} \times 4.44822\ \text{N} = 1.35582\ \text{J}$ (two digits
  > transposed). Do not memorise 1.35558. *(Present in both editions; not previously logged.)*

## 3.3 Density, specific gravity, specific volume ·slides 43–44
- [def] **Density** ρ = mass / volume. Gas density varies with pressure; liquid density ≈ fixed. ·slide 43
  Heaviest liquid: mercury ρ ≈ 13,580 kg/m³. Lightest gas: hydrogen ρ ≈ 0.0838 kg/m³ (ratio ≈ 162,000×).
  > ⚠ VERIFY ·slide 43 — slide says "liquids are 3 **times** denser than gases at 1 atm". Water (≈1000) vs air
  > (≈1.2) is ≈ 800–1000×, i.e. ~**3 orders of magnitude**, not 3×. Read as "3 orders of magnitude." See log.
  > *(still printed in the Oct 2026 edition)*
- [eq: specific-gravity] **Specific gravity** SG = ρ / ρ_reference (water at 4 °C for liquids; air at 1 atm for
  gases). Example SG(Hg) = 13600/1000 = 13.6. **Specific volume** $v = 1/\rho$ (m³/kg). ·slide 44
  *(S1 fixed in the Oct 2026 edition — now reads "13600 kg/m³ / 1000 kg/m³ = 13.6"; the Jul 2026 edition
  printed 13500/1000 = 13.6. Slide 43 still quotes 13,580 kg/m³, so the example uses a rounded value.)*

## 3.4 Viscosity & Couette flow ·slides 45–50
- [fig ·slides 46–47] Two parallel plates, gap $h$, lower fixed, upper dragged at velocity
  $U$ by force $F$; fluid fills the gap. Below $Uh/\nu < 1500$ the flow stays laminar with a **linear** velocity
  profile — **Couette flow**. *(Oct 2026 edition: slide 46 has a new 3-D sketch of the plates (area $A$, gap
  labelled $h$; the Jul 2026 figure labelled it H) plus a curved profile marked "in the case of $U = 0$"; slide 47
  shows the linear profile with its gradient $\partial u/\partial y$.)*
- [fig ·slide 45] Velocity profile between a fixed lower plate ($u = 0$) and a moving upper plate ($u = U_0$),
  drawn curved (a pressure gradient is also set), with the text "the flow = shear flow".
- [eq] Shear stress ∝ U, ∝ 1/h: ·slide 45
  $$\tau = \frac{F}{A} = \mu\frac{U}{h}$$
  $\mu$ = **viscosity** (dynamic/absolute viscosity); the flow is a **shear flow**.
- [eq: newton-viscosity] For a general shear flow, at distance $y$ from the wall: ·slide 48
  $$\boxed{\,\tau = \mu\frac{du}{dy}\,}\qquad\text{— Newton's law of viscosity}$$
- [def] Temperature dependence: **gases** — μ **increases** with T (more molecular motion/mixing); **liquids** —
  μ **decreases** with T (molecules separate, attraction falls). ·slide 49
  [fig ·slide 49] Dynamic viscosity against temperature: the gas curve rises, the liquid curve falls.
- [eq: kinematic-visc] **Kinematic viscosity** $\nu = \mu/\rho$ (units m²/s). ·slide 50
  Units: μ in Pa·s (SI), g/(cm·s) = **Poise** (P, CGS/absolute). ν: 1 cm²/s = 1 **Stokes** (St);
  1 St = 1×10⁻⁴ m²/s; 1 cSt = 1×10⁻⁶ m²/s. Oils: ν ≈ 30–100 cSt.
  *(Oct 2026 edition merges the μ and ν unit slides into slide 50. The line "1 cSt = 1×10⁻⁶ m²/s" is from old
  slide 53 and is not in the Oct 2026 edition, though slide 50 still quotes oils in cSt.)*
- [def] **Viscosity Index (VI)**: dimensionless temperature-sensitivity measure; VI 100 = least sensitive,
  0 = most sensitive; additives can push VI > 100. ·slide 50

## 3.5 Newtonian vs non-Newtonian fluids ·slide 51
- [def] **Newtonian fluid**: τ ∝ du/dy (water, oil, air). **Non-Newtonian**: does not obey Newton's law
  (pulp, high-molecular-weight solutions, asphalt). ·slide 51
- [fig ·slide 51] **Rheological diagram** — shear stress τ vs shear strain rate γ̇:
  - **Newtonian** — straight line through the origin, slope = μ₀;
  - **Bingham plastic** — straight line but with a yield stress τ₀ intercept (flows only past τ₀);
  - **Herschel–Bulkley** — yield stress τ₀ then a curve (nonlinear past yield);
  - **Shear-thinning (pseudoplastic)** — concave-down curve from origin (apparent viscosity falls with γ̇);
  - **Shear-thickening (dilatant)** — concave-up curve from origin (apparent viscosity rises with γ̇).

## 3.6 Surface tension ·slides 52–53
- [def] **Surface tension** σ = tensile force per unit length on a section of a liquid's free surface; the
  surface tends to shrink (acts like a stretched elastic film). A dewdrop is spherical for this reason, and its
  internal pressure exceeds the outside. ·slides 52–53
  [fig ·slide 52] An insect standing on water, and a sketch of molecules: those inside are pulled equally in all
  directions, those at the air–water surface are pulled sideways and inward — the surface-tension pull.
- [derivation/eq: drop-dP] Force balance on a liquid drop of diameter $d$ (circumference tension =
  pressure × cut area): $\sigma\,\pi d = \Delta P\,\dfrac{\pi d^2}{4}$ ·slide 53
  $$\boxed{\,\Delta P = \frac{4\sigma}{d} \;\Big(=\frac{2\sigma}{r}\Big)\,}$$
  *(Deck writes σ as τ. Result is the single-surface drop form; a bubble with two surfaces would give 8σ/d.)*

## 3.7 Capillarity ·slide 54 (and old slide 64)
- [def] **Capillarity**: interplay of surface tension and the liquid–solid adhesive force. ·slide 54
- [derivation/eq: capillary-rise] Balance of the adhesive (surface-tension) pull up the wall against the weight
  of the raised column: $\pi d\,\sigma\cos\theta = \dfrac{\pi d^2}{4}\rho g h$ ·slide 54
  $$\boxed{\,h = \frac{4\sigma\cos\theta}{\rho g d}\,}$$
  where $d$ = tube diameter, $\theta$ = contact angle, $\rho$ = liquid density, $h$ = mean rise. ·slide 54
  *(The symbol definitions come from old slide 62; the Oct 2026 edition condenses capillarity onto slide 54 and
  leaves the symbols to the figure.)*
  [fig ·slide 54] *(Oct 2026 figure)* Tube of diameter $d$ dipped in liquid of density $\rho$: the meniscus
  rises $h$ above the outside level; the surface-tension pull $T$ acts at the wall at contact angle $\theta$.
  *(The Jul 2026 figure, old slides 61–62, also drew the wall-force components $\sigma\pi d\cos\theta$
  (vertical, lifting) and $\sigma\pi d\sin\theta$.)*
- [data] Glass tube, $d$ in mm, $h$ in mm ·slide 54: Water $h = 30/d$; Alcohol $h = 11.6/d$;
  Mercury $h = -10/d$ (negative ⇒ depression, θ > 90°). *(Water 30/d verified: 4σcosθ/ρgd with σ≈0.073, θ≈0.)*
  > ⚠ VERIFY S34 ·slide 54 — the Oct 2026 edition lists "Water: h = 30/d · Alcohol: h = 11.6/d · Mercury:
  > h = −10/d" with **no units and no tube material**. The constants only work with $d$ and $h$ both in **mm**
  > for a **glass** tube (as old slide 63 said). With $d$ in metres, $h = 30/d$ is wrong by a factor of $10^{6}$.
  > Check: $4\sigma/(\rho g) = 4(0.0728)/(998 \times 9.81) = 2.97\times10^{-5}\ \text{m}^2 = 29.7\ \text{mm}^2$.
- [exercise ·old slide 64] (1) Compute the column heights of the slide-54 liquids for $d = 10$ mm.
  (2) Look up densities & surface tensions and back-calculate the contact angle θ for each.
  *(not in the Oct 2026 edition)*
  - [added] Part (1), straight from the slide's constants with $d = 10$ mm: water $h = 30/10 = 3.0$ mm;
    alcohol $h = 11.6/10 = 1.16$ mm; mercury $h = -10/10 = -1.0$ mm (a 1 mm depression).

## 3.8 Compressibility & bulk modulus ·slides 55–57
- [derivation] Volume $V$ at pressure $p$ drops by $\Delta V$ under a rise $\Delta p$. Cubic dilatation
  $\Delta V/V$; **bulk modulus** $K$: ·slide 56
  $$K = \frac{\Delta P}{\Delta V/V} = -V\frac{dP}{dV} = \rho\frac{dP}{d\rho}\qquad\text{[eq: bulk-modulus]}$$
  The $\rho$ form follows from constant mass, $M = \rho V$ (stated on slide 56).
  [fig ·slide 56] Cube of volume $V_0$, faces area $A$, compressed on all sides by forces $F$ to $V_0-\Delta V$.
  > ⚠ VERIFY S35 ·slide 56 — the Oct 2026 edition prints "K = ΔP/ΔV/V = **V**dP/dV" — the **minus sign is
  > missing** (the Jul 2026 edition, old slide 66, had $-V\,dP/dV$). A pressure rise ($dP > 0$) shrinks the
  > volume ($dV < 0$), so without the minus sign $K$ comes out negative. Correct: $K = -V\,dP/dV$.
- [def] **Compressibility** $\beta = 1/K$ (indicates how compressible the fluid is). Values ·slide 57:
  water $K = 2.06\times10^{9}$ Pa; air $K = 1.4\times10^{5}$ Pa (adiabatic, = γP); water
  $\beta = 4.85\times10^{-10}$ Pa⁻¹ (shrinks only ≈0.005 % under +1 atm). *(All three verified consistent.)*
- [eq: wave-speed] $K$ sets the speed $a$ of a pressure (sound) wave in the liquid: ·slide 57
  $$a = \sqrt{\frac{dP}{d\rho}} = \sqrt{\frac{K}{\rho}}$$
  The Oct 2026 slide shows the step: from $K = \rho\,dP/d\rho$, $dP = K\,d\rho/\rho$, so
  $$a = \sqrt{\frac{K\,d\rho/\rho}{d\rho}} = \sqrt{\frac{K}{\rho}}$$
  with the $d\rho$ struck through to show it cancelling. ·slide 57
  > ⚠ VERIFY S36 ·slide 57 — cosmetic. The cancellation line prints "√(Kdρ/ρ) /dρ)" — one opening bracket, two
  > closing; it should read $\sqrt{(K\,d\rho/\rho)/d\rho}$. The same slide also writes "l0⁹", "l0⁵", "l0⁻¹⁰" and
  > "l/Pa" with the letter l for the digit 1 (also in the Jul 2026 edition). Values are right once read as 1.
- [homework ·old slide 71] Obtain density, SG, specific volume, viscosity, surface tension, compressibility for at
  least five fluids in BG, SI and CGS units. *(not in the Oct 2026 edition)*

## 3.9 Perfect gas & polytropic process ·slides 58–59
- [eq: perfect-gas] With $p$ pressure, $v$ specific volume, $T$ absolute temperature, $R$ gas constant
  (Boyle's–Charles' law): ·slide 58
  $$\boxed{\,pv = RT\,}\qquad (v = 1/\rho)$$
  Equation of state; a gas obeying it is a **perfect/ideal gas** (strictly, none exist, but a gas far above its
  liquefaction temperature is well approximated). [Q on old slide 73: units of R → J/(kg·K).] *(The question
  is not in the Oct 2026 edition; the answer is ours, not the deck's.)*
- [eq: polytropic] State change of a perfect gas: ·slides 58–59
  $$pv^{n} = \text{constant}$$
  $n$ = **polytropic exponent**, ranging $0\to\infty$, giving five process types: **isobaric, isothermal,
  polytropic, adiabatic, isochoric**.
- [fig ·slide 59] *(new in the Oct 2026 edition)* Pressure $p$ against specific volume $v$, five curves through
  one state point: **isobaric** $n = 0$ (horizontal line); **isothermal** $n = 1$; **polytropic** $1 < n < \kappa$;
  **adiabatic** $n = \kappa$ (steepest of the falling curves); **isochoric** $n = \infty$ (vertical line).
- [def] For an **adiabatic** change $n = \gamma = C_p/C_v$ (ratio of specific heats / isentropic index). ·slide 59
  *(Deck writes γ as "K" here — not the bulk modulus K of §3.8; watch the symbol clash. The Oct 2026 slide prints
  both "n = K, K = cp/cv" and "n = γ = Cp/cv", and its new figure uses a third symbol, κ, for the same ratio.)*

## 3.10 Dimensional homogeneity ·slides 60–65 *(new in the Oct 2026 edition)*
- [def] **All** equations must be **dimensionally homogeneous**: each additive term in an equation must have
  the same dimensions. ·slide 61
- [eq: dimensional-homogeneity] Example — the incompressible Bernoulli equation: ·slide 61
  $$P + \tfrac{1}{2}\rho V^{2} + \rho g Z = \text{constant}$$
  "Each term must have the unit of pressure."
  $P$ = pressure (Pa) · $\rho$ = density (kg/m³) · $V$ = velocity (m/s) · $g$ = gravitational acceleration
  (m/s²) · $Z$ = elevation (m).
  *(Here $V$ is velocity, not the volume $V$ of §3.8. The rendered page shows a gap after "ρV"; the slide's
  text layer has $V^{2}$, so the square is a rendering artefact of the PDF, not a slide error.)*
  - [added] Dimension check of each term, using slide 42's table:
    $$[P] = \{ML^{-1}T^{-2}\}$$
    $$[\tfrac{1}{2}\rho V^{2}] = \{ML^{-3}\}\{L^{2}T^{-2}\} = \{ML^{-1}T^{-2}\}$$
    $$[\rho g Z] = \{ML^{-3}\}\{LT^{-2}\}\{L\} = \{ML^{-1}T^{-2}\}$$
- [ex ·slides 62–65] A body weighs **1000 lbf** under standard earth gravity $g = 32.174$ ft/s².
  (a) Its mass in kg? (b) Its weight in N under the moon's $g_{\text{moon}} = 1.62$ m/s²? (c) Its acceleration
  if a net force of 400 lbf acts on it, on the moon or on the earth? ·slide 62
  - (a) ·slide 63
    $$m = \frac{W}{g} = \frac{1000\ \text{lbf}}{32.174\ \text{ft/s}^{2}} = 31.08\ \text{slugs}$$
    $$m = (31.08\ \text{slugs})(14.5939\ \text{kg/slug}) = 454\ \text{kg}$$
  - (b) ·slide 64
    $$W_{\text{moon}} = m\,g_{\text{moon}} = (454\ \text{kg})(1.62\ \text{m/s}^{2}) = 735\ \text{N}$$
  - (c) ·slide 65
    $$a = \frac{F}{m} = \frac{400\ \text{lbf}}{31.08\ \text{slugs}} = 12.87\ \text{ft/s}^{2}$$
    $$a = (12.87\ \text{ft/s}^{2})(0.3048\ \text{m/ft}) = 3.92\ \text{m/s}^{2}$$
    "This acceleration is the same anywhere" — mass does not depend on location; only weight does.
  - *Recomputed:* $1000/32.174 = 31.081$ slug; $\times 14.5939 = 453.6$ kg; $453.6 \times 1.62 = 734.8$ N
    (the slide's 735 N uses the rounded 454 kg); $400/31.08 = 12.870$ ft/s² $= 3.923$ m/s². All agree.
  - [added] The example works because $1\ \text{lbf} = 1\ \text{slug}\cdot\text{ft/s}^{2}$ in BG units, just as
    $1\ \text{N} = 1\ \text{kg}\cdot\text{m/s}^{2}$ in SI, so $W = mg$ and $F = ma$ need no conversion constant.
- *Note:* this is the method the 2025 CAT 1 Q1 examined (see `_verification-log.md` P15, written when the deck
  had no slide on it). The Oct 2026 edition states the principle and gives the Bernoulli example, but still does
  not work a "find the dimensions of an unknown constant" problem.

### Cross-references
- Viscosity & Newton's law underpin all of **08-viscous-flow** (Navier–Stokes, laminar profiles).
- Polytropic/perfect-gas relations are reused for atmospheric pressure variation in **04-fluid-statics** (§ gas column).
- Bulk modulus / wave speed connect to compressibility effects noted in **05-flow-fundamentals**.
- The Bernoulli equation used as the homogeneity example (§3.10) is derived and applied in **06-energy-bernoulli**.

### Verification notes for this section
- 2 flags logged: mean free path units (slide 33), "3× denser" (slide 43). Both **still printed** in the Oct 2026
  edition. S1 (SG(Hg) arithmetic, slide 44) is **fixed** in that edition.
- New in the Oct 2026 check (placeholder IDs until the log is updated): S33 ft·lbf conversion (slide 42), S34
  capillary constants without units (slide 54), S35 missing minus sign in $K = -V\,dP/dV$ (slide 56), S36 bracket
  and l-for-1 typos (slide 57).
- Verified correct: drop ΔP=4σ/d, capillary h=4σcosθ/ρgd (and water 30/d), K/β values for water & air, wave
  speed a=√(K/ρ), perfect-gas & polytropic relations, every number in the slides 62–65 example.
- Minor slide typos (units table, slide 42) logged lightly, not as physics errors.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
