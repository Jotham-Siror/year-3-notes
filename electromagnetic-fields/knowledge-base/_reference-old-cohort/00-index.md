---
kb: "Electromagnetic Fields — Year 3 (Mechanical Engineering)"
lecturer: "withheld (only the Polarization handout is explicitly signed; the other two handouts are unsigned but belong to the same EM Fields set)"
course_code: "EEE3202 (confirmed from the current-cohort handout; not printed on these older ones)"
file_role: index
source: "3 lecture-note PDFs in the Electromagnetic Fields folder — 51 pages total"
built: "extracted + verified from the three PDFs; equations transcribed to canonical LaTeX; typo/error slides flagged and collected in _verification-log.md; two worked examples numerically re-solved and confirmed"
coverage: "51/51 pages mapped, no gaps (the source PDFs themselves overlap heavily — see below)"
total_verification_flags: 6
---

# Electromagnetic Fields — Knowledge Base Index

> ## ⚠ SUPERSEDED — old-cohort reference only
>
> This knowledge base was built from **three handouts belonging to a previous cohort** of EEE3202
> (same lecturer, same course). It is **not authoritative** for the current cohort.
>
> **The current knowledge base is one level up:** `../00-index.md`.
>
> Two legitimate uses for this material:
>
> 1. **Filling a gap** where the current cohort's handout has not yet been issued — at present that
>    means polarization, the Poynting vector, and reflection/transmission.
> 2. **Cross-checking** a derivation that appears in both sets.
>
> Anything taught from here must be labelled as old-cohort material pending this year's handout.
> ⚠ Note the **axis-convention clash**: the POL handout below propagates along **x** with transverse
> components (E_y, E_z), while the current handout uses **z** with (E_x, E_y). Teach in the current
> convention and translate.

**What it is.** A verified map of the three older lecture-note PDFs. Every claim is anchored to a
source PDF and page; suspected lecturer errors are flagged inline (⚠ VERIFY) and collected in
`_verification-log.md` — prefer the corrected form, and mention the handout's version only where it
is useful.

## The three source PDFs (and their shorthand codes)
| Code | File | Pages | What it is |
|---|---|---|---|
| **EMW** | `ELECTROMAGNETIC WAVES.pdf` | 31 | The main, fullest document — Maxwell → waves → media → skin depth → Poynting → polarization → reflection/transmission. |
| **UPW** | `THE UNIFORM PLANE WAVE.pdf` | 16 | Largely a subset of EMW (plane wave + waves-in-media + skin depth), but **uniquely holds the two worked examples**. |
| **POL** | `POLARIZATION OF WAVES.pdf` | 4 | A short, focused handout on polarization (linear/circular/elliptical) in complex notation; signed by the lecturer |

Provenance is cited as **·EMW p5**, **·UPW p7**, **·POL p2** in the topic files.

> **Heads-up on overlap:** EMW and UPW cover the "plane waves in dielectric / lossy dielectric / perfect dielectric
> / conducting media" and "skin depth" material **twice**, almost identically. The topic files below consolidate
> the two into one clean treatment and cite both sources.

## How the files are organized
- **Topic files `01`–`07`** — one per major theme, in teaching order (consolidated across the three PDFs).
- **`_nomenclature.md`** — every symbol + meaning + SI units (resolve notation clashes here).
- **`_formula-sheet.md`** — all key equations in one place, each tagged to its topic.
- **`_verification-log.md`** — every flagged handout error/typo, with the correct form + a source.

## Tag legend (used in every topic file)
`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example (lecturer's
numbers, re-verified) · `[exercise]` unsolved problem · `[fig]` figure described from the page image ·
`·EMW/UPW/POL pN` provenance · `⚠ VERIFY` flagged suspected handout error.

## Coverage map (topic files)
| File | Theme | Source pages | Key content |
|---|---|---|---|
| `01-maxwell-wave-equations.md` | Maxwell's equations → wave equation | EMW p1–6 | 4 Maxwell eqns, source-free simplification, curl-of-curl derivation of ∇²E, harmonic fields, propagation constant γ=α+jβ |
| `02-uniform-plane-wave.md` | The uniform (TEM) plane wave | UPW p1–7, EMW p6–8 | plane-wave definition, why it's TEM, coupled E–H equations, general solution f₁/f₂, v=1/√(μ₀ε₀), intrinsic impedance η=377 Ω |
| `03-waves-in-media.md` | Plane waves in the four media | EMW p9–15, UPW p7–14 | loss tangent, complex permittivity ε*, dielectric / lossy dielectric / perfect dielectric / good conductor: α, β, vₚ, η; classification table; **2 worked examples** |
| `04-skin-depth.md` | Depth of penetration / skin depth | EMW p16–17, UPW p15–16 | δ=1/α=√(2/ωμσ)=1/√(πfμσ); dependence on f, μ, σ; surface-coating/HF consequences |
| `05-poynting-vector.md` | Poynting vector & energy | EMW p17–23 | P=E×H, Poynting theorem (derivation), receiver vs transmitter interpretation, average power ½E₀²/η |
| `06-polarization.md` | Polarization of waves | EMW p24–27, POL p1–4 | linear / elliptical / circular; complex notation; ±j ⇒ 90° phase; left- vs right-hand; the two axis conventions reconciled |
| `07-reflection-transmission.md` | Normal incidence at a boundary | EMW p28–31 | incident/reflected/transmitted fields, boundary conditions, reflection Γ=(η₂−η₁)/(η₂+η₁) & transmission T=2η₂/(η₁+η₂), 1+Γ=T |

## Dependency / teaching order
`01` Maxwell & wave equation (the foundation) → `02` uniform plane wave (η, velocity, TEM) → `03` waves in media
(needs γ, η from 01–02) → `04` skin depth (a corollary of the good-conductor case in 03) → `05` Poynting/energy
(uses η and the field solutions) → `06` polarization (uses the plane-wave field form) → `07` reflection &
transmission (uses η from 02–03). `03` is the heaviest and most exam-relevant.

## Verification summary (6 flags — see `_verification-log.md`)
The physics in these handouts is sound; the errors are transcription/labelling slips, not conceptual. The ones a
learner should NOT absorb from the raw pages:
- **EMW p6** — the exact attenuation/phase formulas: **both** boxed results are labelled "α" (the second, the
  `…+1` one, is **β**); and the bracket is shown raised to power **2** when the outer operation is a **square
  root (power ½)**. Correct: α=ω√(με/2)·[√(1+(σ/ωε)²)−1]^½, β=…[…+1]^½. (Unit for α is Np/m, not "dB/m".)
- **EMW p14 & UPW p13–14** — good-conductor result: after separating real/imaginary parts the second line is
  again labelled "α"; it is **β**. (The value α=β=√(ωμσ/2) is correct.)
- **UPW p15, Example 1 answer** — the H-field answer is printed "**42.2 μ/m**"; the unit is **μA/m**
  (microamperes per metre). The numeric value 42.2 is correct (re-verified with εᵣ=2.53).
- **EMW p27** — elliptical-polarization line "E(z,t)=Eₓ(z,t)**aₓ** + Eₓ(z,t)**a_y**": the second component
  should be **E_y(z,t) a_y**, not Eₓ.
- **POL p4** — text says circular polarization needs "**180°** phase between the two components"; the standard
  condition (and POL's own math, Ey=Ea cos ωt, Ez=Ea sin ωt) is a **90°** phase difference (the ±j). The 180°
  refers only to the LHC↔RHC sign flip; as written it's misleading.
- **Pervasive minor spelling typos** across EMW/UPW (e.g. "ca"→can, "ad"→and, "I"→in, "atteuation", "Poyting",
  "ski depth", "coductivity") — OCR/typing artifacts, no effect on physics. Logged once as a group, not per word.

Also a **convention note** (not an error): POL propagates along **x** with transverse components **(E_y, E_z)**,
while EMW propagates along **z** with **(Eₓ, E_y)**. Same physics, different axis labels — the topic files use
EMW's z-propagation convention and note POL's where it matters.

## Provenance notes
- All text and equations transcribed from the three PDFs (pages viewed as images). Where a page's typed math was
  garbled or shorthand, the canonical form is given and any real discrepancy is flagged (not silently changed).
- The two worked examples (polystyrene 5 GHz; σ=0.1 medium at 50 kHz vs 10 GHz) were re-solved numerically and
  match the handout answers — see `03-waves-in-media.md` and `_verification-log.md`.
- Nothing was invented. If a future question needs content not in these three PDFs, say so and ask
  rather than filling the gap.
