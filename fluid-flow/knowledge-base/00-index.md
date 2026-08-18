---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
file_role: index
source: "MEC 3104 FLUID THEORY NOTES.pptx (594 slides)"
built: "extracted + verified from the deck; equations from OMML→LaTeX + canonical reconstruction; figures from slide images"
coverage: "594/594 slides mapped, contiguous, no gaps or overlaps (verified)"
total_verification_flags: 50   # 18 first-pass + 32 second-pass slide flags (S1–S32); plus 13 exam-paper flags (P1–P13)
past_papers: 2                 # see past-papers/00-past-papers-index.md
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

# MEC 3104 Fluid Theory — Knowledge Base Index

**What this is.** A complete, verified map of the MEC 3104 Fluid Theory lecture deck — all 594
slides, reorganised into 11 topic files plus a formula sheet, a nomenclature guide and a
verification log. Every claim is anchored to the slide it came from. Where a slide appears to
contain an error it is flagged inline (⚠ VERIFY), corrected against a standard reference, and
logged in `_verification-log.md` — the slide's original wording is never silently overwritten.

**How to use it.** Find your topic in the coverage map below and open that file. `_nomenclature.md`
resolves the deck's symbol clashes; `_formula-sheet.md` collects every equation in one place.
Prefer the corrected form when revising, and check the log to see what the slide actually said.

Finished human-facing study guides live in the `study-guides/` folder alongside this knowledge base
(currently Topics 03 and 04) — reuse them, and match their style when building new study material.

> Operating instructions — how to navigate and teach from this knowledge base — live in `CLAUDE.md`
> at the project root.

## How the files are organized
- **Topic files `01`–`11`** — one per major course section, in teaching order.
- **`_nomenclature.md`** — every symbol + meaning + SI units (resolve notation clashes here).
- **`_formula-sheet.md`** — all key equations in one place, each tagged to its section.
- **`_verification-log.md`** — every flagged slide error/typo, with the correct form + a source. Also holds
  **§ Exam papers** (IDs `P1`, `P2`, …): defects found in his actual CAT/exam papers.
- **`past-papers/`** — his real assessment papers, transcribed verbatim and machine-readable, with figures
  redrawn as SVG. Start at `past-papers/00-past-papers-index.md` (register + the format for adding the next one).

## Tag legend (used in every topic file)
`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example (lecturer's
numbers) · `[exercise]` unsolved problem · `[fig]` figure described from the slide image · `[hist]` historical
note · `·slide N` provenance · `⚠ VERIFY` flagged suspected slide error.

## Coverage map (594 slides, verified complete)
| File | Slides | # | Topic | Key content |
|---|---|---|---|---|
| `01-course-admin.md` | 1–10 | 10 | Course Administration | instructor, syllabus, objectives, assessment, references |
| `02-history.md` | 11–29 | 19 | History of Fluid Mechanics | hydraulics, ships, da Vinci, Euler, Navier–Stokes, Kirchhoff |
| `03-fluid-properties.md` | 30–76 | 47 | Fluid Properties | units, density/SG, viscosity & Couette, surface tension, capillarity, bulk modulus, perfect gas |
| `04-fluid-statics.md` | 77–165 | 89 | Fluid Statics | pressure, manometers, Bourdon, forces on surfaces, buoyancy, metacentre, relative equilibrium |
| `05-flow-fundamentals.md` | 166–214 | 49 | Fundamentals of Flow | streamlines, Reynolds, vorticity, circulation, continuity |
| `06-energy-bernoulli.md` | 215–263 | 49 | Energy & Bernoulli | Euler eqn, Bernoulli, Venturi, Pitot, orifice/Torricelli, weir |
| `07-momentum.md` | 264–301 | 38 | Conservation of Momentum | bend force, jet force, Borda–Carnot, jet pump, propeller, Euler turbomachine |
| `08-viscous-flow.md` | 302–386 | 85 | Flow of Viscous Fluid | Navier–Stokes, plane/pipe Poiseuille, Hagen–Poiseuille, turbulence (log law), boundary layer, lubrication |
| `09-pipe-flow.md` | 387–478 | 92 | Flow in Pipes | Darcy–Weisbach, Moody, minor losses, valves, diffuser, pumping |
| `10-open-channel-flow.md` | 479–519 | 41 | Open-Channel Flow | Chézy/Manning, best section, specific energy, critical depth, Froude, hydraulic jump |
| `11-drag-and-lift.md` | 520–594 | 75 | Drag and Lift | drag/lift, d'Alembert, Kármán street, drag crisis, sphere/Stokes, Kutta–Joukowski, wings, cavitation |

*(Ranges are contiguous and cover 1–594 exactly. Slide 369 is **hidden** in the deck; included in `08` and marked.)*

## Dependency / teaching order
`01` admin → `02` history (context) → `03` properties → `04` statics → `05` flow fundamentals (continuity,
Reynolds, vorticity) → `06` energy/Bernoulli → `07` momentum → `08` viscous flow (Navier–Stokes, boundary
layer) → `09` pipe flow → `10` open-channel → `11` drag & lift. Later sections lean on `05` (continuity,
circulation) and `08` (boundary layer, separation).

## Verification summary (49 slide flags + 13 exam-paper errata — see `_verification-log.md`)

> **A second, independent audit of all 11 topic files was run on 2026-08-03.** All 594 slides were re-extracted
> from the .pptx XML **including equation objects** (the first pass read text boxes only), ~200 `·slide N`
> citations were sampled, and every worked example was re-computed. Result: all 18 original flags **confirmed
> verbatim**, only 2 wrong citations found, `_formula-sheet.md` clean — but **31 further slide errors** (`S1`–`S31`)
> and **4 errors in the KB itself** (now fixed, tagged `⚠ KB-FIX 2026-08-03`). Read `_verification-log.md`
> **§ Second-pass audit** before teaching sections 04, 06, 07 or 09: several derivations there are broken on the
> slides in ways the topic files had silently repaired without flagging. The worst is slide 256, where the
> Torricelli derivation drops the elevation term and its own algebra yields v = 0.
Most content is correct. Notable **substantive** errors a learner should NOT absorb from the raw slides:
- **07 Momentum** (4): resultant $\sqrt{F_x^2-F_y^2}$→`+` (s271); moving-plate force `/v²`→`/v` (s277); impeller
  torque uses peripheral `u`→absolute `v` (s291/295); impulse sign (s266). *(all confirmed on rendered slides.)*
- **02 History** (2): da Vinci dates "14 Apr 1452 – 1514" → **15 Apr 1452 – 1519** (s21); "Kirchoff"→Kirchhoff.
- **03 Properties** (2): mean free path "0.06 pm" → **0.06 µm** (s33); "liquids 3× denser than gases" → ~3 orders
  of magnitude (s45).
- **04 Statics** (1): standard-atmosphere "lapse to 1 km, −50.5 °C to 10 km" → **11 km / −56.5 °C / 20 km** (s102).
- **10 Open-channel** (1): Manning "n=0.12" → **0.012** (s493, solution uses 0.012).
- **11 Drag/Lift** (2): flat-plate τ₀ coefficient "3.65" → **≈0.33** (s531); "C_D=0.31/Re^(1/7)" → **0.031** (s560).
- Plus minor typos in 01, 05, 06, 08, 09 (sign/label/unit slips) — logged, non-substantive.
- **Exam papers** (13 across 2 papers, § Exam papers). *CAT 1 2025:* γ_w printed in "N m/s²" (→ **9.79 kN/m³**,
  P1); Q6(c) is blank on the paper (P2); Q8(b) omits "or turbulent" (P3); Q9 writes δ for ∂ and calls the
  z-component "along the x-axis" (P4); Q5(b) never defines the datum for X (P5); Lagrangian/Reynolds misspelt
  (P6). *CAT 1 2024:* Re written as vd/μ with ρ missing (P7); Q2 has two items lettered "a." (P8); a velocity
  called a flow rate (P9); a 5 cm "hole" in a question whose figure and integral are a **weir** (P10); "coefficient
  of discharge = 3.2" is an imperial weir constant, not a dimensionless C_d (P11); "g = 9.81 **N**" (P12);
  Reynolds/∂-δ again (P13). **Both papers misprint a unit in their data block — teach him to check units before
  substituting.**

## Provenance notes
- Text + equations extracted directly from the .pptx XML (OMML math objects → LaTeX deterministically; typed
  garbled math reconstructed to standard form and cross-checked). Figures viewed from the slide images/renders.
- Where a slide was ambiguous, the actual rendered slide was viewed before writing (nothing invented). No slide
  currently requires a user screenshot; if one ever does, it will be listed here.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
