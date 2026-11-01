---
kb: "MEC 3104 Fluid Theory"
file_role: nomenclature
purpose: "Every symbol used in the deck with meaning + SI units. Resolves the deck's symbol clashes (it reuses τ, ζ, n, K, L, σ, m, T for different quantities). Use this to disambiguate when reading the topic files."
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

# Nomenclature & symbols

## ⚠ Symbol clashes in the deck (read first)

*Oct 2026 edition: further clashes (e.g. slide 59 uses K, γ and κ for the same specific-heat ratio) are listed under **Oct 2026 edition — additions** at the end of this file.*
The lecturer reuses several symbols; this KB disambiguates by context/section:
| Symbol | Meaning A | Meaning B (clash) |
|---|---|---|
| **τ** | shear stress (Pa) — everywhere | **surface tension** (N/m) in §03.6–03.7 — this KB uses **σ** for surface tension |
| **ζ** | **vorticity** (s⁻¹) in §05.5–05.6, §08 | **loss coefficient** & **KE-correction factor** in §09 |
| **n** | **polytropic exponent** (§03.9, §04.5) | **Manning roughness** (§10); turbulent power-law index (§08.6) |
| **K** | **bulk modulus** (Pa) (§03.8) | **ratio of specific heats** γ (§03.9, slide 59) |
| **L** | length (m) | **power** L=Tω, water/shaft power (§07, §08, §09) |
| **T** | temperature (K) (§03–04) | **torque** (N·m) (§07, §11) |
| **σ** | surface tension (this KB) / normal stress (§08.2) | **choke number** Q/(νl) (§09.6); Strouhal sometimes |
| **m** | **hydraulic mean depth** A/s (m) (§09–10) | mass (kg) |
| **s** | wetted perimeter (m) (§09–10) | streamline coordinate (§06.2) |
| **p / P** | pressure (Pa) | some slides use capital **P** for pressure *force* (N) (§04, §08) |
| **v, u** | velocity components (m/s) | deck sometimes writes **v** or **u** for **kinematic viscosity ν** — this KB always uses ν |
| **θ** | angle (rad/°) | **momentum thickness** (m) (§08.7) |

## Fluid properties
| Symbol | Quantity | SI unit |
|---|---|---|
| ρ | density | kg/m³ |
| μ | dynamic (absolute) viscosity | Pa·s = kg/(m·s) |
| ν | kinematic viscosity = μ/ρ | m²/s |
| σ | surface tension (this KB) | N/m |
| SG | specific gravity (ρ/ρ_ref) | – |
| v_s | specific volume = 1/ρ | m³/kg |
| K | bulk modulus | Pa |
| β | compressibility = 1/K | Pa⁻¹ |
| a | pressure/sound wave speed = √(K/ρ) | m/s |
| R | specific gas constant | J/(kg·K) |
| γ (=κ) | ratio of specific heats C_p/C_v | – |
| VI | viscosity index | – |

## Kinematics & flow
| Symbol | Quantity | SI unit |
|---|---|---|
| u, v, w | velocity components (x, y, z) | m/s |
| U | uniform / freestream velocity | m/s |
| v (mean), v̄ | mean velocity | m/s |
| Q | volumetric flow rate | m³/s |
| q | discharge per unit width (open channel) | m²/s |
| ṁ | mass flow rate = ρAv | kg/s |
| A | area (cross-section / projected) | m² |
| ζ | vorticity = ∂v/∂x − ∂u/∂y | s⁻¹ |
| ω | angular velocity (= ζ/2 for rotation) | rad/s |
| Γ | circulation = ∮v·ds = ∬ζ dA | m²/s |
| δ* | displacement thickness | m |
| θ | momentum thickness | m |
| δ | boundary-layer thickness (99% U) | m |
| v* | friction velocity = √(τ₀/ρ) | m/s |
| l | mixing length | m |

## Pressure & statics
| Symbol | Quantity | SI unit |
|---|---|---|
| p | pressure | Pa |
| p₀, p_t | stagnation / total pressure | Pa |
| p_∞ | freestream pressure | Pa |
| h | head / depth / gap | m |
| H | total head | m |
| z | elevation | m |
| g | gravitational acceleration (9.80665) | m/s² |
| γ (=ρg) | specific weight | N/m³ |
| I_G, I_x | second moment of area | m⁴ |
| y_c, y_G | centre of pressure / centroid position | m |
| GM | metacentric height | m |

## Dimensionless groups
| Symbol | Group | Definition |
|---|---|---|
| Re | Reynolds number | ρvd/μ = vd/ν |
| Fr | Froude number | v/√(gh) |
| St | Strouhal number | fd/U |
| C_D, C_L, C_M | drag / lift / moment coefficient | force / (½ρU²·A or ·l) |
| C_c, C_v, C_d(=C) | contraction / velocity / discharge coefficient | – |
| k_d | cavitation number | (p_∞−p_u)/(½ρU²) |
| σ (choke) | choke number | Q/(νl) |

## Pipe / channel / friction
| Symbol | Quantity | SI unit |
|---|---|---|
| λ | Darcy pipe-friction factor | – |
| f | friction coefficient (= λ/4, Fanning) | – |
| ζ | minor-loss coefficient / KE-correction factor | – |
| ε | wall roughness height | m |
| d (=4m) | (hydraulic) diameter | m |
| m | hydraulic mean depth = A/s (= hydraulic radius R) | m |
| s | wetted perimeter | m |
| i | bed slope (= tan θ ≈ sin θ) | – |
| c | Chézy coefficient | – |
| n | Manning roughness coefficient | – |
| α (Bazin) | Bazin roughness coefficient | – |
| h_f, h_s, h_L | friction / minor / total head loss | m |

## Forces, work, machines
| Symbol | Quantity | SI unit |
|---|---|---|
| F, R | force / resultant force | N |
| D, L | drag / lift force | N |
| T | torque | N·m |
| L (power) | power = Tω or ρgQH | W |
| L_w, L_s | water power / shaft power | W |
| η | efficiency (<1) | – |
| M | moment | N·m |
| n (polytropic) | polytropic exponent | – |

## Oct 2026 edition — additions

New symbols and new clashes found in the October 2026 edition, by topic group. Read with the clash table above.

### Topics 01–03 (slides 1–65)

- $g_{\text{moon}}$ — moon's standard gravitational acceleration, 1.62 m/s² ·slide 62.
- $W$ — weight (N or lbf) ·slides 62–64. $W_{\text{moon}}$ — weight on the moon.
- slug — BG mass unit, 1 slug = 14.5939 kg = 1 lbf·s²/ft ·slides 39, 63.
- $Z$ — elevation (m) in the Bernoulli homogeneity example ·slide 61.
- **Clash: $V$** — volume on slide 56 (bulk modulus) vs velocity on slide 61 (Bernoulli), five pages apart.
- **Clash: specific-heat ratio now has three symbols** — slide 59 prints "n = K, K = cp/cv" and "n = γ = Cp/cv",
  and its new p–v figure labels it κ ("1 < n < κ", "n = κ"). K is also the bulk modulus (slides 56–57).
- $\tau$ still used for both shear stress (slides 45–48, 51) and surface tension (slides 53–54); the new slide 54
  figure labels the surface-tension pull "T". No change to the KB's τ/σ convention.

### Topic 04 — Fluid Statics (slides 66–156)

- $\gamma$ — specific weight, N/m³ (lbf/ft³ in the US-unit examples, slides 126, 142). Already listed; note it clashes with γ = ratio of specific heats (§03.9) — the clash table lists γ only as κ.
- $B$ — clash: lapse rate in K/m (slide 91, "g/RB"); hinge point (slides 126–131); centre of buoyancy in the Oct 2026 ship/barge figures (slides 144–148, B and B′).
- $C$ — clash: centre of pressure (slides 121–123, 133); centre of buoyancy (slides 144–145 text, C → C′).
- $P$ — triple use in §04: pressure (slides 75, 79), pressure force (slides 118–123), and the wall's horizontal reaction at A (slides 126–131). Slide 68 now uses F for the pressure force.
- $I_o$ — second moment of the waterline area about the tilt axis O, m⁴ (slide 146).
- $V_{\text{sub}}$ — submerged volume, m³ (slide 146).
- $\overline{GB}$ — distance from centre of gravity G to centre of buoyancy B, m (slide 146). The KB nomenclature has GM; slides write MG.
- $l$ — distance along the gate from centroid to centre of pressure, ft/m (slides 128–129); clashes with $l$ = cylinder length (slide 134) and mixing length (§08).
- $h_{CG}$, $p_{CG}$ — depth of and pressure at the centroid (slide 127; earlier slides write $h_G$).
- $L$ — gate length (slide 128) and barge half-width (slides 147–148) — adds to the existing L clash (length / power).
- $\theta$ — now: bank/gate angle (118, 126), heel angle (144), free-surface tilt (151–153), cylindrical coordinate (154). Slide 154 no longer uses θ for angular velocity.
- $a$ — linear acceleration of the vessel (slides 150–153); the KB writes α in §4.12.

### Topics 05–06 (slides 157–255)

| Symbol | Meaning | Units | Where | Clash / note |
|---|---|---|---|---|
| ν (deck "u") | kinematic viscosity $= \mu/\rho$ | m²/s, ft²/s | 172, 174–175, 179 | deck writes "u" — clashes with velocity component u (already in clash table) |
| $R$ | pipe radius | m | 176–178 | vs gas constant R (topic 03/04) |
| $\Delta P$ | pressure drop along a pipe | Pa | 176–178 | |
| $k$ | constant in a velocity field ($u=-ky$, $v=kx$) | s⁻¹ | 196–197 | |
| $\gamma_o$ | specific weight of **water**, 62.4 lbf/ft³ | lbf/ft³ | 224 | subscript "o" reads like "oil" — the oil's γ is 0.86 × 62.4 |
| $\gamma$(air) | printed for water's 9.79 kN/m³ | — | 226 | mislabel (S54) |
| $\gamma$(Hg) = 13.6 | printed for mercury's **specific gravity** | — | 232 | an s.g., not a specific weight (S55) |
| $y$ | manometer deflection (mercury) | m | 232–233 | vs coordinate y |
| $h$ | manometer reading | in | 241–242 | vs head loss h₂, h₃ (220) |
| $C_a$ | coefficient × hole area, $C_d\,a$ | m² | 250–255 | looks like a subscripted coefficient; it is a product |
| $a$, $A$ (orifice ex.) | 248: $a$ = **jet** area, $A$ = **orifice** area ("Cc = a/A") | ft² | 248 | **opposite** of 243, where $a_c$ = jet and $a$ = hole; and 251 uses A for the hole and the tank (S14) |
| $r_{jet}$, $D_{jet}$ | radius, diameter of contracted jet | ft, in | 248 | |
| $N$ | rotational speed | rpm | 193–195 | used implicitly ("500 rpm") |

### Topics 07–08 (slides 256–375)

- $w_1$, $w_2$ — relative velocities at impeller inlet/outlet (m/s). **Clash:** slide 287 prints them as
  $\omega_1$, $\omega_2$, colliding with $\omega$ = impeller angular velocity (rad/s) on 288 (S69).
- $p$ used for **momentum flux** on slides 274 ("Or p = Aρv²") and 278 ("Δp (= Aρv²)"), units N — clashes with
  pressure $p$ (Pa) on the same slides (275: $p_1$, $p_2$). Not an error, but a clash worth a row.
- $\nu_t$ — turbulent (eddy) kinematic viscosity, m²/s (slide 337; printed "v₁"/"vt"). Joins the existing
  "v" for $\nu$ clash.
- "$\mu_{max}$" printed for $u_{max}$ on slides 320 ("v = (1/1.5) μmax") and 328 ("= ½μmax") — clashes with
  viscosity μ.
- $R$ — r-direction component of external (body) force per unit mass, m/s² (slides 309–314); not the gas
  constant.
- $a$ — jet cross-section area, m² (slide 265 inset, $F_N = \rho aV^2\sin\theta$); deck elsewhere uses $A$.
- $V_j$, $A_j$ — jet velocity and area; $R_x$, $R_y$ — reaction components (slide 259 figure).
- Starred non-dimensional variables $x^*, y^*, u^*, v^*, t^*, \zeta^*$ (slide 311) — already in KB text; add if
  not in `_nomenclature.md`.

### Topics 09–11 (slides 376–561)

- $h_p$ — head added by the pump, ft (·slides 456–458). **Clash:** on slide 458 "hp" also means **horsepower** (1 hp = 550 ft·lbf/s), on the same page.
- $f$ — Darcy friction factor (= the deck's λ) on 455–458. **Clash** with f = λ/4 (open-channel friction coefficient, ·465), f = disc friction coefficient (·530), f = vortex-shedding frequency (·522).
- $f'$ — friction coefficient on the disc's cylindrical rim (·531).
- $h_m$, $\sum h_m$ — minor (fitting) head losses (·456); the deck elsewhere writes $h_s$.
- $\varepsilon/d$ — relative roughness, stated directly as a datum (·455).
- $b$ — channel width (·497). Same quantity as $B$ on ·480. **Clash:** $b$ is also disc thickness (·530) and wing span (·544).
- "v" for ν again on ·456 ("Re = Vd/v") — the deck's known kinematic-viscosity habit.
- $E_{\min}$ — minimum specific energy, ft (·497).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
