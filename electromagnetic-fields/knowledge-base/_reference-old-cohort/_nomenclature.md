---
kb: "Electromagnetic Fields — Year 3"
file_role: nomenclature
purpose: "Every symbol used in the three handouts with meaning + SI units. Resolves symbol clashes. Use this to disambiguate when reading the topic files."
---

# Nomenclature & symbols

## ⚠ Symbol clashes / look-alikes (read first)
| Symbol | Meaning A | Clash / look-alike |
|---|---|---|
| **β** | **phase constant** (rad/m) — the wave quantity | do not confuse with any generic use; here β is always the phase constant |
| **γ** | **propagation constant** $=\alpha+j\beta$ (m⁻¹) | not the ratio of specific heats (that was Fluid Flow) |
| **η** | **intrinsic impedance** $\sqrt{\mu/\varepsilon}$ (Ω); **η\*** = complex η in a lossy medium | not efficiency |
| **μ** | **permeability** (H/m) | also the SI prefix **micro** (10⁻⁶) — e.g. "μA/m" = microamp/m. Watch context! |
| **ε** | **permittivity** (F/m); **ε\*** = complex permittivity | ε₀ = free-space value |
| **σ** | **conductivity** (S/m = mho/m) | (in Fluid Flow σ was surface tension — different subject) |
| **α** | **attenuation constant** (Np/m) | EMW p6 & p14 mislabel β as α — see _verification-log.md |
| **δ** | **skin depth / depth of penetration** (m) | not a boundary-layer thickness |
| **θ** | **loss-tangent angle** (tanθ=σ/ωε); or a polarization tilt angle | context-dependent |
| **P** | **Poynting vector** E×H (W/m²) | not pressure |
| **Γ** | **reflection coefficient** (–) | capital gamma; not circulation |
| **a** vs **α** | $\mathbf a_x,\mathbf a_y,\mathbf a_z$ = **unit vectors**; $a$ (scalar) = a **phase angle** in polarization | distinct from α the attenuation constant |
| **axis conventions** | EMW: propagate along **z**, transverse **(Eₓ,E_y)** | POL: propagate along **x**, transverse **(E_y,E_z)** — same physics, different labels |

## Fields & sources
| Symbol | Quantity | SI unit |
|---|---|---|
| **E** | electric field intensity | V/m |
| **H** | magnetic field intensity | A/m |
| **D** = εE | electric flux density (displacement) | C/m² |
| **B** = μH | magnetic flux density | T (Wb/m²) |
| **J**_c = σE | conduction current density | A/m² |
| **J**_disp = ∂D/∂t | displacement current density | A/m² |
| ρ (rho) | free charge density | C/m³ |

## Medium constants
| Symbol | Quantity | SI unit |
|---|---|---|
| ε | permittivity = εᵣε₀ | F/m |
| ε₀ | free-space permittivity (8.854×10⁻¹² ≈ 10⁻⁹/36π) | F/m |
| εᵣ | relative permittivity (dielectric constant) | – |
| ε* | complex permittivity ε(1−jσ/ωε) | F/m |
| μ | permeability = μᵣμ₀ | H/m |
| μ₀ | free-space permeability (4π×10⁻⁷) | H/m |
| μᵣ | relative permeability | – |
| σ | conductivity | S/m (mho/m) |

## Wave / propagation quantities
| Symbol | Quantity | SI unit |
|---|---|---|
| γ | propagation constant = α + jβ | m⁻¹ |
| α | attenuation constant | Np/m (×8.686 → dB/m) |
| β | phase constant (phase-shift coefficient) | rad/m |
| ω | angular frequency = 2πf | rad/s |
| f | frequency | Hz |
| λ | wavelength = 2π/β = v_p/f | m |
| v, v₀, v_p | (phase) velocity of propagation | m/s |
| c | speed of light = 1/√(μ₀ε₀) = 3×10⁸ | m/s |
| η, η* | intrinsic (characteristic) impedance √(μ/ε), complex η* | Ω |
| η₀ | free-space impedance = 120π ≈ 377 | Ω |
| δ | skin depth / depth of penetration = 1/α | m |
| tan θ | loss tangent = σ/ωε | – |
| f₁, f₂ | forward / reflected travelling-wave functions | (field units) |

## Energy & power
| Symbol | Quantity | SI unit |
|---|---|---|
| P | Poynting vector = E×H | W/m² |
| P_av | time-average power density = ½E₀²/η | W/m² |
| εE²/2 | electric energy density | J/m³ |
| μH²/2 | magnetic energy density | J/m³ |
| S | area normal to power flow | m² |
| T (period) | 1/f = 2π/ω | s |

## Boundary / reflection
| Symbol | Quantity | SI unit |
|---|---|---|
| Γ | reflection coefficient = (η₂−η₁)/(η₂+η₁) | – |
| T (coeff.) | transmission coefficient = 2η₂/(η₁+η₂) | – |
| η₁, η₂ | intrinsic impedances of regions 1, 2 | Ω |
| Ê⁺_m1, Ê⁻_m1, Ê⁺_m2 | incident / reflected / transmitted E amplitudes | V/m |
| γ₁, γ₂ | propagation constants of regions 1, 2 | m⁻¹ |

## Vectors & operators
| Symbol | Meaning |
|---|---|
| $\mathbf a_x,\mathbf a_y,\mathbf a_z$ | unit vectors along x, y, z |
| ∇× | curl |
| ∇· | divergence |
| ∇² | Laplacian |
| j | imaginary unit √(−1); √j = (1+j)/√2, √(−j)=e^{−jπ/4} |
