---
kb: "MEC 3104 Fluid Theory"
file_role: nomenclature
purpose: "Every symbol used in the deck with meaning + SI units. Resolves the deck's symbol clashes (it reuses τ, ζ, n, K, L, σ, m, T for different quantities). Use this to disambiguate when reading the topic files."
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

# Nomenclature & symbols

## ⚠ Symbol clashes in the deck (read first)
The lecturer reuses several symbols; this KB disambiguates by context/section:
| Symbol | Meaning A | Meaning B (clash) |
|---|---|---|
| **τ** | shear stress (Pa) — everywhere | **surface tension** (N/m) in §03.6–03.7 — this KB uses **σ** for surface tension |
| **ζ** | **vorticity** (s⁻¹) in §05.5–05.6, §08 | **loss coefficient** & **KE-correction factor** in §09 |
| **n** | **polytropic exponent** (§03.9, §04.5) | **Manning roughness** (§10); turbulent power-law index (§08.6) |
| **K** | **bulk modulus** (Pa) (§03.8) | **ratio of specific heats** γ (§03.9, slide 76) |
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

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
