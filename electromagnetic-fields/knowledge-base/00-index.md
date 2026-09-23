---
kb: "Electromagnetic Fields — Year 3"
course_code: "EEE3202"
lecturer: "withheld"
file_role: index
source: "Current-cohort material, issued progressively. 3 documents received so far (56 pp.): WC1 (18 pp.), TL (16 pp.), TLT (22 pp.)"
built: "Transcribed from rendered page images; equations in canonical LaTeX; suspected errors flagged inline and collected in _verification-log.md; every worked example and exercise solved and numerically verified"
coverage: "56/56 pages mapped across WC1, TL and TLT, no gaps"
total_verification_flags: 67
---

# Electromagnetic Fields (EEE3202) — Knowledge Base Index

**What this is.** A verified map of the EEE3202 course material — every claim anchored to its
source page, every suspected error flagged and corrected. Start here, then open the topic file you
need rather than re-reading the raw PDFs.

**Status.** The course is delivered as **material released progressively**. Three documents have
been issued so far. This index is the register — update it as each new one arrives.

> **Operating instructions** (how to navigate and teach from this KB) live in `CLAUDE.md` at the
> project root, not in this file.

---

## Document register

| Code | Document | Pages | Received | Authored by | Topic file |
|---|---|---|---|---|---|
| **WC1** | *Electromagnetic Wave Characteristics I* | 18 | ✅ | the lecturer | `01-wave-characteristics-1.md` |
| **TL** | *Transmission lines* | 16 | ✅ 10 Sep 2026 | the lecturer | `02-transmission-lines.md` |
| **TLT** | *Transmission Line Theory* | 22 | ✅ 3 Sep 2026 | **a distributed slide deck** (Sadiku 5e, Ida 3e, Pozar 4e) — issued by the lecturer, not written by him | `02-transmission-lines.md` |
| WC2 | *Electromagnetic Wave Characteristics II* (expected) | — | ⏳ not yet issued | — | — |

Provenance is cited as **·WC1 p7**, **·TL p12**, **·TLT p20** in the topic files.

> **⚠ TL and TLT are not equal in standing.** TL is the lecturer's own writing and sets the scope.
> TLT is course material he distributed but did not author. Both are current-cohort and both are
> examinable; only TL is *his words*. `02-transmission-lines.md` tags every line accordingly — keep
> that distinction when teaching.

## Past-paper register

| Paper | Sat | Marks | File |
|---|---|---|---|
| CAT 1 — *Electromagnetic Fields and Waves* (EEE 3202) | Wed 13 Aug 2025, 13:15–14:15 | 30 | `past-papers/EEE3202-CAT1-2025-08-13.md` — **solved** |
| **End of Semester** — *Electromagnetic Fields and Waves* (BEE 3101) | Fri 25 Oct 2024, 08:00–10:00 | 60 | `past-papers/BEE3101-EXAM-2024-10-25.md` — unsolved |
| **CAT 1** (BEE 3102) | Thu 29 Aug 2024, 1 hr | 37, no total printed | `past-papers/BEE3102-CAT1-2024-08-29.md` — unsolved |
| **CAT**, printed "CAT 1" (BEE 3102) | Thu 3 Oct 2024, 1 hr | none printed | `past-papers/BEE3102-CAT1-2024-10-03.md` — unsolved |
| **CAT** (BEE 3101) | Wed 1 Oct 2025, 1 hr | 30 in parts, no total | `past-papers/BEE3101-CAT-2025-10-01.md` — unsolved |
| **End of Semester** (BEE 3102) | Thu 23 Oct 2025, 13:30–15:30 | 90 printed / 60 sat ✓ | `past-papers/BEE3102-EXAM-2025-10-23.md` — unsolved |
| Lab 2 — *Propagation coefficient* | — | — | `../assignments/lab2-propagation-coefficient/` — our Python model, sweep plots and verification script |

**Full analysis, coverage tables and the house format:**
[`past-papers/00-past-papers-index.md`](past-papers/00-past-papers-index.md). Exam-paper defects (P1–P20)
are in `_verification-log.md` **§ E**.

**⚠ One unit, three codes.** This course is examined as **EEE 3202** (current cohort), **BEE 3102** (2024
CATs) and **BEE 3101** (2024 end-of-semester exam) — and BEE 3102 is *also* the 2024 Digital Electronics
code. Match a paper by unit **name**, never by code.

**What the papers tell us about examinable scope:**

- **The 2025 CAT:** about **13 of 30 marks** came from material absent from WC1 — polarization (Q1a, Q1e)
  and the Poynting vector (Q1c, Q1d, Q2a(v)). Both live only in `_reference-old-cohort/`.
- **✅ Transmission lines are now covered.** TL and TLT together close what was the largest hole in
  this knowledge base. The **1 Oct 2025 CAT** goes from 100 % uncovered to **15 of 30 marks
  covered** (Q1a line constants → `02` § 1; Q1b Smith chart → `02` § 14). The **23 Oct 2025 exam**
  gains its Q1(g) and Q2(b), another **15 marks**. The **25 Oct 2024 exam Q3** (matching, stub
  reactances, quarter-wave transformer, **15 marks**) is covered end to end by `02` §§ 11–13, and
  most of the 3 Oct 2024 CAT with it.
- **✅ The Smith chart blocker is resolved.** ·TLT p20 is a **full blank Smith chart** with all
  perimeter and radially-scaled parameter scales. Erratum P22 is closed — print that page before
  attempting either 2025 Smith-chart question.
- **What is still missing:** **rectangular waveguides** (≈17 marks on the 2024 exam) and
  **computational electromagnetics / the finite-difference method** (15 marks on the 2024 exam, 15
  on the 1 Oct 2025 CAT, 12 on the 23 Oct 2025 exam). See the gap map below.
- **§5 (the α/β derivation) and §6 (loss tangent)** were untested in 2025; 2024 asked for a *definition* of
  loss tangent (Q1c) and used §5's β as one step of a chain (CAT 1 Q1b). Teach §5 for **use**, not
  reproduction.
- **§8 (skin depth) is the best marks-per-page in WC1** — 7 marks in 2025 across three parts, and
  5 more in 2024 (Q1c(i), Q1d).
- **Two questions recur across cohorts, verbatim:** "distinguish the Poynting theorem from the Poynting
  vector" (2 marks in Aug 2024 *and* Aug 2025) and polarization-in-antenna-design (2024 Q1f, 2025 Q1a).
  **A third now joins them:** the four primary line constants, asked on the 1 Oct 2025 CAT (Q1a, 4
  marks) and again on the 23 Oct 2025 exam (Q1g, 4 marks) three weeks later.
- **The October 2024 CAT is the end-of-semester exam in miniature** — three of its four parts reappeared,
  essentially word for word, three weeks later. **The 2025 pair does the same**: all four parts of the
  1 Oct 2025 CAT reappeared on the 23 Oct 2025 exam. Two cohorts, two CATs, the same behaviour:
  **this lecturer's late CAT is a rehearsal for his final.**
- **⚠ 20 of the 2025 exam's 30 compulsory marks are the 13 Aug 2025 CAT reused** — same cohort, ten weeks
  apart, several parts verbatim. That CAT is already `solved` in `past-papers/`; working it is the
  highest-yield preparation for this unit's final.
- **These papers are error-prone.** Thirty-seven logged defects across five papers, including an
  aluminium conductivity with the wrong exponent sign and three questions whose part-marks do not sum to
  their stated totals. Check a paper's arithmetic before setting it as a mock.

## How the files are organised

- **Topic files `01`, `02`, …** — normally **one document per topic file**, in the order issued.
  **`02` is the exception**: it is built from *two* documents (TL and TLT) because they cover one
  topic between them. See the splitting rule.
- **`_nomenclature.md`** — every symbol with meaning and SI units; resolves the notation clashes,
  which are severe in this subject.
- **`_formula-sheet.md`** — every equation in one place, each tagged to its source page, all in
  corrected form.
- **`_verification-log.md`** — every flagged source error with the correct form and why.
  § A–D cover WC1 and the old cohort, **§ T covers TL and TLT**, § E covers the exam papers.
- **`_reference-old-cohort/`** — the previous cohort's knowledge base. **Not authoritative.** See
  § Old-cohort reference below.
- **`../sources/`** — the raw PDFs. Not tracked; see `../sources/SOURCES.md`.

### Splitting rule

**One document = one topic file.** Split a document into `NNa` / `NNb` only when it covers **two
genuinely independent themes** *and* exceeds ~25 KB. Otherwise keep it whole.

Two files depart from the one-to-one mapping, both deliberately:

- **`01`** holds WC1 whole despite six sections and >25 KB: it is a single continuous argument (wave
  equation → plane wave → media → skin depth), each section leans on the one before, and its
  tutorial questions span the whole thing.
- **`02` merges two documents into one file.** TL and TLT are one topic split across two sources,
  overlapping for their first third and complementary after it. Two files would mean transcribing
  the telegrapher's derivation twice in two inconsistent notations, and cross-referencing on every
  question. Merged, TLT catches TL's errors on the page where they occur — which matters, because
  TL is the most error-dense document in this knowledge base.

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example
(lecturer's numbers) · `[exercise]` problem stated but **not solved** in the source · `[fig]` figure
described from the rendered page · `[added]` supplied here, **not** in the source · `·WC1 pN` /
`·TL pN` / `·TLT pN` provenance · `⚠ VERIFY` flagged suspected source error.

---

## Coverage map

| File | Sources | Pages | Key content |
|---|---|---|---|
| `01-wave-characteristics-1.md` | WC1 | 1–18 | Maxwell → wave equation (general / conducting / dielectric / free space); uniform plane waves; d'Alembert solution; phasor form; E–H relationship and $\eta$; propagation constant $\gamma = \alpha + j\beta$; loss tangent and $\varepsilon^*$; lossy / perfect-dielectric / conductor cases; skin depth; 2 tutorial questions |
| `02-transmission-lines.md` | TL 1–16, TLT 1–22 | 38 | RLGC model and the four primary line constants; telegrapher's equations; lossy and lossless wave equations; $u_p$; phasor form and $\gamma$; $Z_0$; reflection coefficient; standing waves, VSWR, return loss; slotted-line measurement; $Z_{in}(-z)$; short- and open-circuit stubs; quarter-wave transformer; **the Smith chart, with a blank chart**; 2 worked examples + 3 unsolved exercises, all solved and verified |

### Section map within WC1

| § | Pages | Content |
|---|---|---|
| 1 | 1–4 | The wave equation and its four specialisations |
| 2 | 4–6 | Uniform plane waves, 1-D reduction, d'Alembert, **Figure 1** |
| 3 | 6–7 | Sinusoidal / phasor form |
| 4 | 7–8 | E–H relationship, intrinsic impedance, $\eta_0 = 377\ \Omega$ |
| 5 | 8–11 | Propagation constant, derivation of $\alpha$ and $\beta$, general $\eta$ |
| 6 | 11–13 | Loss tangent, **Figure 2**, complex permittivity, classification |
| 7 | 13–17 | Plane waves in lossy / perfect-dielectric / conducting media |
| 8 | 17–18 | Depth of penetration and skin depth |
| 9 | 18 | Tutorial questions (solved and verified here) |

### Section map within `02-transmission-lines.md`

| § | Sources | Content |
|---|---|---|
| 1 | TL p1, TLT 3–5 | The line as a circuit; **the four primary line constants** — recurring 4-mark bookwork |
| 2 | TL 1–2, TLT 6–7 | Telegrapher's equations from KVL/KCL |
| 3 | TLT 8–9 | The **lossy** wave equations — TLT only |
| 4 | TL 2–3, TLT 10 | Lossless line, $u_p = 1/\sqrt{LC}$, d'Alembert solution |
| 5 | TL 3–4, TLT 11–16 | Phasor form, $\gamma = \alpha + j\beta$, lossless $\beta = \omega\sqrt{LC}$ |
| 6 | TLT 15 | **Characteristic impedance $Z_0$** — TLT only |
| 7 | TL 4–5, TLT 17 | Reflection coefficient; matched / open / short cases |
| 8 | TL 7–9, TLT 17 | Standing waves, positions of maxima and minima, VSWR, return loss |
| 9 | TL 10–11 | Slotted-line measurement — TL only |
| 10 | TL 12 | The analytical $Z_{in}(-z)$ — parent of §§ 11–13 |
| 11 | TL 12–13 | Short-circuit stub, $jZ_0\tan\beta z$ |
| 12 | TL 13–14 | Open-circuit stub, $-jZ_0\cot\beta z$ |
| 13 | TL 14–15 | Quarter-wave transformer, $Z_{in} = Z_0^2/Z_L$ |
| 14 | TLT 18–22 | **The Smith chart** — method, blank chart, example. TLT only |
| 15 | TL, TLT | All 5 examples and exercises, solved and numerically verified |

## Dependency / teaching order

Within WC1 the order is strictly sequential — §1 → §2 → §3 → §4 → §5 → §6 → §7 → §8. Nothing can be
taught out of order without forward references.

**Heaviest and most exam-relevant in WC1:** §5 (the $\alpha$/$\beta$ derivation) and §7 (the four media),
which is also where the handout's errors cluster. §8 is a short corollary of §7's good-conductor
case. §4 supplies the one number most likely to appear in a question, $\eta_0 = 377\ \Omega$.

**Within `02` the chain is also strictly sequential** — §1 → … → §14, each section substituting into
the one before. But the **exam weight is concentrated at the two ends**: § 1 (4 marks, twice) and
§§ 10–14 (11–15 marks per paper). §§ 2–5 are the derivation that gets you there; they have been
examined only as bookwork, never reproduced in full. **Teach §§ 10–14 first if time is short** —
they need only $\Gamma$, $Z_{in}$ and the chart, all of which can be quoted.

**`02` depends on `01`.** $\gamma = \alpha + j\beta$, phasor notation and the wave equation are all
established in WC1 §§ 3, 5 and reused here with the same symbols and the same meanings.

---

## ⚠ Gap map — syllabus topics with no current-cohort document

WC1's page 1 lists four learning objectives but delivers only three. The papers widen the picture
further. **Do not write the standard formulae for a missing topic into this KB** — they would then
read as his lecturer's notes. Ask him for the material instead; it belongs in `../sources/current/`.

| Syllabus objective | Status | Interim source | Warning |
|---|---|---|---|
| i. Wave equation in different media | ✅ WC1 §1 | — | — |
| ii. Uniform plane wave and wave propagation | ✅ WC1 §2, §5 | — | — |
| iii. Characterization of conductors and dielectrics | ✅ WC1 §6, §7 | — | — |
| **iv. Types of polarization** | ❌ **absent from WC1** | `_reference-old-cohort/06-polarization.md` | **Axis convention differs — see below. Examined for 5 marks in Aug 2025** |
| **Poynting vector & theorem** | ❌ **absent from WC1** | `_reference-old-cohort/05-poynting-vector.md` | Examined in 2025 **and** twice in 2024. Recurs verbatim across cohorts |
| **Reflection & transmission at a boundary** | ❌ **absent from current cohort** | `_reference-old-cohort/07-reflection-transmission.md` | **22 of 37 marks** on the Aug 2024 CAT; 7 more on the 2024 exam |
| **Transmission lines** — matching, stub reactances, quarter-wave transformer | ✅ **`02` §§ 1–13** (TL) | — | **Closed 10 Sep 2026.** Was the largest hole in this KB |
| **Smith chart** — normalized impedance, VSWR, $\Gamma$, $Z_{in}$ | ✅ **`02` § 14** (TLT), blank chart at ·TLT p20 | — | **Closed 3 Sep 2026.** Erratum P22 resolved |
| **Rectangular waveguides** — cut-off, λ_g, v_g, v_p, guide impedance, TE₁₀ patterns | ❌ **absent from BOTH** | ❌ **nothing** | **≈17 marks** on the 2024 exam. Ask him for the material |
| **Computational EM / finite-difference method** | ❌ **absent from BOTH** | ❌ **nothing** | **15 marks** on the 2024 exam (Q5), **15** on the 1 Oct 2025 CAT, **12** on the 23 Oct 2025 exam. Asked in every paper in the folder. **Now the single biggest remaining gap** |

### Using the polarization gap-filler

The old-cohort material covers linear, elliptical and circular polarization in complex notation.
It is usable, with two cautions:

1. **Axis convention.** The old polarization handout propagates along **$x$** with transverse
   components $(E_y, E_z)$. WC1 propagates along **$z$** with $(E_x, E_y)$. Same physics, different
   labels. **Teach in WC1's $z$-convention** and translate, rather than quoting the old axes.
2. **A known error in that file's source.** The old handout states circular polarization needs a
   **180°** phase difference; the correct condition — and its own mathematics — is **90°**. See
   `_reference-old-cohort/_verification-log.md`.

Flag clearly when teaching from this that it is **old-cohort material pending this year's document**,
not this year's notes.

---

## Old-cohort reference

> **Still not optional.** The Aug 2025 CAT drew ~13 of 30 marks from polarization and the
> Poynting vector, neither of which any current-cohort document contains.

`_reference-old-cohort/` holds a complete knowledge base built from **three handouts belonging to a
previous cohort** (EMW 31 pp., UPW 16 pp., POL 4 pp. — same lecturer, same course).

**It is not authoritative.** Two legitimate uses only:

1. **Filling a gap** where this cohort's equivalent has not been issued (currently: polarization,
   Poynting vector, reflection and transmission).
2. **Cross-checking** a derivation that appears in both.

Anything taught from it must be labelled as such. When the corresponding current-cohort document
arrives, the new topic file supersedes it — as `02` now supersedes nothing, because transmission
lines were absent from the old-cohort set too.

**Where the two sets overlap**, the physics agrees — WC1's §1–§8 maps onto old files `01`–`04`. WC1
is the fuller and better-organised treatment of that ground.

---

## Verification summary — 67 flags

Full detail in `_verification-log.md`.

| Section | Source | Substantive | Cosmetic | Total |
|---|---|---|---|---|
| § A–D | WC1 + old cohort | 20 (V1–V20) | 23 (C1–C32) | 43 |
| **§ T** | **TL + TLT** | **12 (T1–T12)** | **12 (C24–C35)** | **24** |

**The physics is sound throughout. The transcription is not** — and TL is now the worst offender in
the knowledge base, at roughly one substantive defect per 1.3 pages against WC1's one per 0.9. Four
failure modes dominate across the three documents:

**1 · A wrong constant.** WC1 p8 prints $\mu_0 = 4\pi\times10^{-12}$ H/m. It is
$4\pi\times10^{-7}$. With the printed value $\eta_0 = 1.19\ \Omega$ — not the 377 Ω on the very next
line — and $c = 9.49\times10^{10}$ m/s, some **317× the speed of light**. *(V1, re-computed.)*
**TL p6 does the same with a frequency:** it states $f = 100$ Hz and substitutes $10^{8}$ (T12).

**2 · A symbol collision.** $\sigma$ is the conductivity, but WC1 also uses it for the attenuation
constant $\alpha$, corrupting **six equations** across pp. 9–11 and 16. In three of them $\sigma$
appears on *both* sides, making the equation self-referential. *(V9, V12, V14, V15, V19.)*

**3 · The wrong differential variable.** TL prints $\partial/\partial t$ where $\partial/\partial z$
is meant, in three equations across pp. 1–2, then silently corrects itself a page later without
comment (T1, T2). ·TLT p7 is the clean reference for the same equations.

**4 · Dropped and duplicated superscripts.** TL writes $V_0^{+}$ where $V_0^{-}$ belongs, three
times (T5, T6) — each time collapsing the expression to something trivial. ·TL p5's $Z_L$ formula, as
printed, makes **every load matched**.

Other substantive errors a learner should **not** absorb — WC1:

- **p5** — the Laplacian printed without its squares (V2)
- **p6** — harmonic Ampère's law as $j\omega\varepsilon E + j\omega\sigma E$; the conduction term is
  not time-differentiated (V3)
- **p6** — Figure 1's horizontal axis labelled $t$; it is $z$ (V8)
- **p1** — $\sigma$ replaced by $\varepsilon$ twice in the curl-of-curl step (V4)
- **pp. 2–4** — three boxed wave equations written for the identity's dummy vector $\bar{A}$ instead
  of $\bar{H}$ (V5)
- **p3** — $\rho_s$ for $\rho_v$, inside an invalid chain of equalities (V6)
- **p4** — plane-wave definition says fields are constant "across any chosen direction", which is
  false along the propagation direction (V7)
- **pp. 9, 10, 16** — missing brackets in $\alpha$ and $\beta$: the $\mp 1$ must sit inside, not
  outside (V10). *Invisible in the PDF text layer — only the rendered page shows it*
- **p11** — $|\eta|$ with $\sigma$ for $\sigma^2$ and $(j\omega\varepsilon)^2$ for
  $(\omega\varepsilon)^2$ (V16)
- **p12** — $\gamma^2$ written where $\gamma$ is meant (V17)
- **p15** — lossy phase velocity: $\omega$ cancelled from the denominator but left in the numerator
  (V18). *The line at the bottom of p14 is correct; only the version carried onto p15 is broken*
- **p16** — $\varepsilon^* \approx -j\omega/\sigma$; it is $-j\sigma/\omega$ (V20)

— and TL / TLT:

- **·TL p4** — phasor equations printed with $-j\omega L$, $-j\omega C$; both are $+$ (T3)
- **·TL p7** — standing-wave magnitude missing **both** its brackets and its square root (T8, T9).
  *The bracket error is invisible in the PDF text layer, exactly as with V10*
- **·TL p9** — the voltage **minimum** position labelled $-z_{max}$ (T10)
- **·TL p14** — $\beta z = \lambda/2$ where $\beta z = \pi/2$ is meant (T11)
- **·TLT p13** — backward-wave term printed $e^{j\gamma}$ for $e^{+\gamma z}$ (T4)

**Three habits worth teaching from this**, each of which catches these errors independently:

1. **Check dimensions before substituting.** $\alpha$ and $\beta$ are m⁻¹; $\sigma$ is S/m. Half the
   WC1 flags fail a dimensional check on sight, and T11 sets an angle equal to a length.
2. **Distrust any equation whose left-hand symbol also appears on the right.** That single test
   catches V15, V19 and T1.
3. **Distrust any expression that collapses to something trivial.** T5 gives $I_L = 0$; T6 gives
   $Z_L = Z_0$ for every load. Both are visible without doing any algebra.

### Cross-cohort, cross-document pattern

The old-cohort handouts carry the same class of defect — results that are $\beta$ labelled $\alpha$.
TL adds a position that is a minimum labelled $max$ (T10). The warning therefore widens:

> **Treat every label — Greek symbol, subscript, or superscript sign — in this course's material as
> suspect until checked against the condition that produced it.**

See `_verification-log.md` § D and § T.

---

## Provenance notes

- All 56 pages across the three documents were **rendered to images and read directly**. The PDF
  text layer mangles mathematics; V10 and T8 in particular are invisible without the render.
- Every figure in all three documents is described in its topic file. **No page currently requires a
  screenshot.**
- **·TL p7 and ·TL p11 are photographs of other people's slides** pasted into the lecturer's
  handout (one carries a University of Utah ECE logo). Legible and transcribed, but not his own
  typesetting — do not cite them as such. ·TL p10 is a product photograph with no instructional
  content.
- **Nine problems have been solved and numerically verified** across the knowledge base: WC1's two
  tutorial questions, and `02`'s two worked examples plus three exercises the sources left unsolved
  and two revision questions. All are tagged `[added]` — they are not the lecturer's.
- Nothing was invented. If a question needs content absent from the sources, say so and ask rather
  than filling the gap.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
