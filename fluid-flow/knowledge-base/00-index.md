---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
file_role: index
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition); dropped material from MEC 3104 FLUID THEORY NOTES.pptx (594 slides, Jul 2026)"
built: "extracted + verified from the deck; equations from OMML→LaTeX + canonical reconstruction; figures from slide images"
coverage: "561/561 new-edition slides mapped, contiguous; all 594 old slides traced (kept, merged or dropped) — see _edition-map.md"
total_verification_flags: 103  # 18 first-pass + 32 second-pass (S1–S32) + 53 Oct 2026 edition (S33–S85); plus exam-paper flags P1–P42
past_papers: 5                 # see past-papers/00-past-papers-index.md
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

# MEC 3104 Fluid Theory — Knowledge Base Index

**What this is.** A complete, verified map of the MEC 3104 Fluid Theory lecture deck — all 561
slides of the **October 2026 edition**, reorganised into 11 topic files plus a formula sheet, a nomenclature guide and a
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

## Edition note — read this first
The lecturer reissued the deck in **October 2026** (561 slides, PDF). The knowledge base was first built
from the July 2026 edition (594 slides, .pptx) and has been moved across:
- **Every `·slide N` now means the new edition.** `_edition-map.md` converts old numbers to new ones.
- **New in the Oct 2026 edition** — mostly worked examples with full solutions — is folded into the topic
  files and cited to its new slide.
- **Dropped from the new edition** — a handful of exercises, examples and the flat-plate friction slides — is
  kept, cited `·old slide N` and marked *(not in the Oct 2026 edition)*. Still worth knowing: a CAT set from
  the old deck could use it.
- Flags in `_verification-log.md` say whether each error is **still printed** in the new edition or was
  **fixed** there.

## How the files are organized
- **Topic files `01`–`11`** — one per major course section, in teaching order.
- **`_nomenclature.md`** — every symbol + meaning + SI units (resolve notation clashes here).
- **`_formula-sheet.md`** — all key equations in one place, each tagged to its section.
- **`_edition-map.md`** — old slide number → new slide number, plus what was added, merged and dropped.
- **`_verification-log.md`** — every flagged slide error/typo, with the correct form + a source. Also holds
  **§ Exam papers** (IDs `P1`, `P2`, …): defects found in his actual CAT/exam papers.
- **`past-papers/`** — his real assessment papers, transcribed verbatim and machine-readable. **Five now:**
  2025 CAT 1, 2024 CAT 1, 2024 CAT 2, 2025 CAT 2 and the 2025 end-of-semester paper. The three oldest have
  figures redrawn as SVG; the two 2025 papers carry `figure_data` blocks only. Start at
  `past-papers/00-past-papers-index.md` (register, coverage, recurrence analysis, house format).
  **`09-pipe-flow` is now examined on three papers running** — the gap this index used to flag is closed.

## Tag legend (used in every topic file)
`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example (lecturer's
numbers) · `[exercise]` unsolved problem · `[fig]` figure described from the slide image · `[hist]` historical
note · `·slide N` provenance · `⚠ VERIFY` flagged suspected slide error.

## Coverage map (561 slides, Oct 2026 edition)
| File | Slides | # | Topic | Key content |
|---|---|---|---|---|
| `01-course-admin.md` | 1–10 | 10 | Course Administration | instructor, timetable, syllabus, objectives, assessment, references |
| `02-history.md` | 11–29 | 19 | History of Fluid Mechanics | hydraulics, ships, da Vinci, Euler, Navier–Stokes, Kirchhoff |
| `03-fluid-properties.md` | 30–65 | 36 | Fluid Properties | units, density/SG, viscosity & Couette, surface tension, capillarity, bulk modulus, perfect gas, dimensional homogeneity |
| `04-fluid-statics.md` | 66–156 | 91 | Fluid Statics | pressure, manometers, Bourdon, forces on surfaces, buoyancy, metacentre, relative equilibrium |
| `05-flow-fundamentals.md` | 157–204 | 48 | Fundamentals of Flow | streamlines, Reynolds, vorticity, circulation, continuity |
| `06-energy-bernoulli.md` | 205–255 | 51 | Energy & Bernoulli | Euler eqn, Bernoulli, Venturi, Pitot, orifice/Torricelli, weir |
| `07-momentum.md` | 256–288 | 33 | Conservation of Momentum | bend force, jet force, Borda–Carnot, jet pump, propeller, Euler turbomachine |
| `08-viscous-flow.md` | 289–375 | 87 | Flow of Viscous Fluid | continuity (2-D), Navier–Stokes, plane/pipe Poiseuille, Hagen–Poiseuille, turbulence (log law), boundary layer, lubrication |
| `09-pipe-flow.md` | 376–458 | 83 | Flow in Pipes | Darcy–Weisbach, Moody, minor losses, valves, diffuser, pumping |
| `10-open-channel-flow.md` | 459–497 | 39 | Open-Channel Flow | Chézy/Manning, best section, specific energy, critical depth, Froude, hydraulic jump |
| `11-drag-and-lift.md` | 498–561 | 64 | Drag and Lift | drag/lift, d'Alembert, Kármán street, drag crisis, sphere/Stokes, Kutta–Joukowski, wings, cavitation |

*(Ranges are contiguous and cover 1–561 exactly. Slide 222 — the conduit-velocities example — sits inside the
Bernoulli range but is also used in `07` §7.10. The old deck's hidden slide 369 is a normal slide in the new
edition, slide 358.)*

## Dependency / teaching order
`01` admin → `02` history (context) → `03` properties → `04` statics → `05` flow fundamentals (continuity,
Reynolds, vorticity) → `06` energy/Bernoulli → `07` momentum → `08` viscous flow (Navier–Stokes, boundary
layer) → `09` pipe flow → `10` open-channel → `11` drag & lift. Later sections lean on `05` (continuity,
circulation) and `08` (boundary layer, separation).

## Verification summary (103 slide flags + exam-paper errata P1–P42 — see `_verification-log.md`)

> **Oct 2026 edition re-check (31 Oct 2026).** Every slide of the new edition was viewed rendered and every
> number on new or reworded slides recomputed. Of the earlier flags, some are **fixed** in the new edition
> (among them S1, S4–S6, S10 Torricelli, S15, S17, S19, the Pitot formula and the momentum resultant sign);
> most are **still printed**; S27, S32 and the τ₀ "3.65" left with their dropped slides. **53 new flags,
> S33–S85**, are logged — 35 cosmetic, 18 substantive. The ones a learner must not copy:
> - **Hinged gate, slides 128–131 (S43):** the centre of pressure is measured from the gate end instead of
>   the free surface. The slides' **P = 21,344 lbf and B_x = 1,696 lbf are wrong**; correct values are
>   **P ≈ 29,300 lbf, B_x ≈ 6,300 lbf** (B_z = 30,700 lbf is right).
> - **Jet pump, slides 275–276 (S67):** the pressure-change formula now has the subtraction reversed — the
>   same reversal the 2025 exam printed (P33).
> - **Bulk modulus, slide 56 (S35):** the minus sign in K = −V dP/dV is gone.
> - **Laminar pipe example, slide 177 (S47):** velocity divided by the pipe length — v = 0.08 m/s should be
>   0.973 m/s.
> - **Navier–Stokes in cylindrical form, slides 309–314 (S70)** and **parallel-plate pressure drop sign,
>   slides 322–330 (S74)**.
> The status of each earlier flag is in `_verification-log.md` **§ Oct 2026 edition — re-verification**.

> **A second, independent audit of all 11 topic files was run on 2026-08-03.** All 594 slides were re-extracted
> from the .pptx XML **including equation objects** (the first pass read text boxes only), ~200 `·slide N`
> citations were sampled, and every worked example was re-computed. Result: all 18 original flags **confirmed
> verbatim**, only 2 wrong citations found, `_formula-sheet.md` clean — but **31 further slide errors** (`S1`–`S31`; a 32nd, `S32`, was added later as an addendum — hence the 32 in the frontmatter)
> and **4 errors in the KB itself** (now fixed, tagged `⚠ KB-FIX 2026-08-03`). Read `_verification-log.md`
> **§ Second-pass audit** before teaching sections 04, 06, 07 or 09: several derivations there are broken on the
> slides in ways the topic files had silently repaired without flagging. The worst was the Torricelli derivation
> (now slide 246), which dropped the elevation term so its own algebra yielded v = 0 — *fixed in the Oct 2026 edition*.
Most content is correct. Notable **substantive** errors a learner should NOT absorb from the raw slides:
- **07 Momentum** (4): resultant $\sqrt{F_x^2-F_y^2}$→`+` (s263); moving-plate force `/v²`→`/v` (old s277); impeller
  torque uses peripheral `u`→absolute `v` (s284/288); impulse sign (s258). *(all confirmed on rendered slides. Oct 2026 edition: resultant and moving-plate fixed; impeller torque and impulse sign still printed.)*
- **02 History** (2): da Vinci dates "14 Apr 1452 – 1514" → **15 Apr 1452 – 1519** (s22); "Kirchoff"→Kirchhoff.
- **03 Properties** (2): mean free path "0.06 pm" → **0.06 µm** (s33); "liquids 3× denser than gases" → ~3 orders
  of magnitude (s43).
- **04 Statics** (1): standard-atmosphere "lapse to 1 km, −50.5 °C to 10 km" → **11 km / −56.5 °C / 20 km** (s89).
- **10 Open-channel** (1): Manning "n=0.12" → **0.012** (s472). *Still printed — and the old worked solution that used 0.012 was dropped, so the new edition shows only the wrong value.*
- **11 Drag/Lift** (2): flat-plate τ₀ coefficient "3.65" → **≈0.33** (old s531); "C_D=0.31/Re^(1/7)" → **0.031** (s533).
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
- **Oct 2026 edition (31 Oct 2026):** the 561-page PDF was matched to the old deck slide by slide (text
  similarity, then visual check of every uncertain pair), every page in all 11 ranges was viewed rendered, and
  every number on new or reworded slides recomputed. The new PDF uses a non-embedded font, so some viewers drop
  ² ³ and μ; those were read from the text layer and are not flagged as slide errors.
- Text + equations (Jul 2026 edition) extracted directly from the .pptx XML (OMML math objects → LaTeX deterministically; typed
  garbled math reconstructed to standard form and cross-checked). Figures viewed from the slide images/renders.
- Where a slide was ambiguous, the actual rendered slide was viewed before writing (nothing invented). No slide
  currently requires a user screenshot; if one ever does, it will be listed here.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
