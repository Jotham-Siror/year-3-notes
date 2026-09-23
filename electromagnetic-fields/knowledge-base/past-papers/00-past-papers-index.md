---
kb: "Electromagnetic Fields — EEE3202"
file_role: past-papers-index
purpose: "Register of every CAT / exam paper transcribed into this KB, plus the house format for adding the next one."
papers: 6
total_questions: 20
total_parts: 79
unit_codes: ["EEE 3202", "BEE 3101", "BEE 3102"]
unit_code_note: "⚠ ONE unit, THREE codes, and one of them collides with another subject. The current cohort sits Electromagnetic Fields and Waves as EEE 3202. The 2024 cohort sat the SAME unit as BEE 3102 (both CATs) and BEE 3101 (end-of-semester exam) — in the same semester. And BEE 3102 is ALSO the code on the 2024 Digital Electronics CAT of 6 Aug 2024. Match every paper by unit NAME, never by code."
status_legend: "unsolved = questions only · partial = some model solutions worked & verified · solved = all verified"
canonical_house_format: "../../../fluid-flow/knowledge-base/past-papers/00-past-papers-index.md § House format"
---

<!-- Compiled by Jotham-JS, 2026. Electromagnetic Fields (EEE3202) knowledge base — past papers. -->

# Past Papers — index

> **Read me first.** This folder holds the actual assessment papers, transcribed verbatim and
> machine-readable. Use it to quiz him, to set timed mocks, or to work a question with him. Each paper file
> is self-contained and says what it maps to in the main KB.
>
> **Two rules that matter:**
> 1. `[q]` text is the paper's exact wording — quote it as printed. Where the paper is *wrong*, it stays wrong
>    in the `[q]` block and carries a `⚠ VERIFY` marker; the correction lives in `../_verification-log.md`
>    (§ E — Exam papers). Teach the correct form, and tell him the paper is wrong — never silently fix it.
> 2. Every figure is stored **twice**: a `figure_data:` YAML block inside the paper file (the authoritative
>    geometry, in words and numbers) and a rendered SVG in `figures/`. Reason from the block; show him the SVG.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| EEE 3202 **CAT 1** | 13 Aug 2025 | 30 | 2 | `solved` | [`EEE3202-CAT1-2025-08-13.md`](EEE3202-CAT1-2025-08-13.md) |
| BEE 3101 **End of Semester** | 25 Oct 2024 | 60 (75 printed) | 5 (23 parts) | `unsolved` | [`BEE3101-EXAM-2024-10-25.md`](BEE3101-EXAM-2024-10-25.md) |
| BEE 3102 **CAT 1** | 29 Aug 2024 | 37 (no total printed) | 2 (4 parts) | `unsolved` | [`BEE3102-CAT1-2024-08-29.md`](BEE3102-CAT1-2024-08-29.md) |
| BEE 3102 **CAT** *(printed "CAT 1")* | 3 Oct 2024 | none printed | 2 (4 parts) | `unsolved` | [`BEE3102-CAT1-2024-10-03.md`](BEE3102-CAT1-2024-10-03.md) |
| BEE 3101 **CAT** *(no number printed)* | 1 Oct 2025 | 30 in parts, no total | 2 (4 parts) | `unsolved` | [`BEE3101-CAT-2025-10-01.md`](BEE3101-CAT-2025-10-01.md) |
| BEE 3102 **End of Semester** | 23 Oct 2025 | 90 printed / 60 sat ✓ | 5 (34 parts) | `unsolved` | [`BEE3102-EXAM-2025-10-23.md`](BEE3102-EXAM-2025-10-23.md) |

**Errata IDs.** `P1`–`P13` = 25 Oct 2024 exam · `P14`–`P16` = 29 Aug 2024 CAT · `P17`–`P20` = 3 Oct 2024 CAT ·
`P21`–`P26` = 1 Oct 2025 CAT · `P27`–`P37` = 23 Oct 2025 exam. The next paper starts at **P38**.

**The 23 Oct 2025 exam is the first paper in this folder whose arithmetic passes** — Question One sums to
exactly 30 and Questions Two to Five to exactly 15 each. Five of the six do not reconcile. Full entries live in `../_verification-log.md`
**§ E — Exam papers**, and nowhere else.

> ⚠ **One inconsistency to tidy when convenient.** The 2025 CAT predates this register; its two misprints are
> documented *inside its own file* rather than in the verification log, and carry no P-numbers. Leave them
> there unless he asks — moving them would mean editing a solved file — but do not assume the P-series is a
> complete list of every exam defect in this subject.

## Topic coverage so far

| KB section | Questions that have appeared |
|---|---|
| `01` §2 — uniform plane waves | 2024 CAT 1 Q1a · 2024 Exam Q1a, Q4a |
| `01` §4, §7 — E–H relation, η, media | 2025 CAT Q2a · 2024 CAT 1 Q1b(iii) · 2024 Exam Q1b |
| `01` §5 — propagation constant, β | 2024 CAT 1 Q1b(i), (ii) |
| `01` §6 — loss tangent | 2024 Exam Q1c(ii) |
| `01` §8 — skin depth | Aug 2025 CAT Q1b(i), Q1b(ii), Q2b · 2024 exam Q1c(i), Q1d · **2025 exam Q1a(i)–(ii)** |
| old `05` — Poynting | Aug 2025 CAT Q1c, Q1d, Q2a(v) · 2024 CAT 1 Q1b(iv), Q2a · 2024 exam Q2a · **2025 exam Q1b, Q1c, Q3b, Q3c(ii)–(iii), Q4a** |
| old `06` — polarization | Aug 2025 CAT Q1a, Q1e · 2024 exam Q1f · **2025 exam Q1d, Q3a** |
| old `07` — reflection & transmission | 2024 CAT 1 Q2b (ten parts) · 2024 exam Q2b, Q2c · **2025 exam Q1f(ii), Q4a, Q4b(ii)–(iv)** |
| ❌ **transmission lines** | 2024 CAT (3 Oct) Q1a, Q1b · 2024 exam Q3a–c · **2025 CAT Q1 (15 marks, Smith chart)** · **2025 exam Q2 (15 marks, entire question)** |
| ❌ **rectangular waveguides** | 2024 CAT (3 Oct) Q2a, Q2b · 2024 Exam Q1e, Q4b, Q4c, Q4d |
| ❌ **computational EM / finite differences** | 2024 exam Q5a, Q5b · **2025 CAT Q2 (15 marks)** · **2025 exam Q5 (15 marks, entire question)** |

**`01` §1 (the wave equation itself) and §3 (phasor form) have never been examined directly** in any of the
four papers — they are the machinery, not the questions.

---

## What the 2024 set changes about examinable scope

The Aug 2025 CAT already told us ~13 of 30 marks fell outside WC1. The three 2024 papers say the gap is
larger and more structural than that, and they say it in three different ways.

**1 · Three whole territories have no notes behind them.**

| Territory | Marks across the 2024 papers | Notes anywhere in this repo? |
|---|---|---|
| Transmission lines — matching, stub reactances, quarter-wave transformer | 15 on the exam, plus most of the 3 Oct CAT | ❌ none |
| Rectangular waveguides — cut-off, λ_g, v_g, v_p, guide impedance, TE₁₀ patterns | 14 printed on the exam (+3 unprinted), plus the 3 Oct CAT | ❌ none |
| Computational electromagnetics / the finite-difference method | 15 on the exam | ❌ none |

That is **44 of the exam paper's 76 printed marks**. Say so to him plainly, and **do not write the standard
formulae into this knowledge base** to fill the hole — they would then look like his lecturer's notes. The
right move is to ask him for the handouts these questions came from; they belong in `../../sources/current/`
and then in a topic file.

**2 · The 3 Oct CAT is the exam in miniature.** Three of its four parts reappeared, essentially word for
word, on the end-of-semester paper three weeks later. Details in
[`BEE3102-CAT1-2024-10-03.md`](BEE3102-CAT1-2024-10-03.md) § Recurrence. One pair of papers is not a rule —
but it is the strongest single signal in this folder about what the lecturer treats as core.

**3 · Two questions recur across cohorts.**

- *"Distinguish between the Poynting theorem and the Poynting vector"* — 2 marks on the **Aug 2024 CAT 1**
  (Q2a) and 2 marks on the **Aug 2025 CAT** (Q1c). Verbatim both times.
- *Polarization and antennas* — 2 marks on the **2024 exam** (Q1f), and the 2025 CAT opened with it. Both sit
  only in `_reference-old-cohort/06-polarization.md`.

**4 · Reflection and transmission is worth drilling in full.** The Aug 2024 CAT's Q2(b) walks all ten steps
(Γ, τ, both reflected fields, both transmitted fields, all three powers) on a 300 Ω / 100 Ω boundary — and
the exam then asked **three of those same ten parts** on the **same numbers**. Working the CAT question end
to end is the most efficient preparation in the folder.

**5 · The papers are unusually error-prone.** Twenty errata across three papers, and they are not all
cosmetic: an aluminium conductivity with the wrong exponent sign (P3), a boundary-value problem whose
boundary is not fully specified (P13), a question total that overstates its parts by nine marks (P1), and
two parts with no mark allocation at all (P8, P12). **Check the arithmetic of any paper before setting it as
a timed mock**, and decide in advance what to do about the missing allocations.

---

## ⚠ What the 2025 pair changes — and it is not good news

**The 1 October 2025 CAT is 100 % outside both knowledge bases.** Thirty marks: fifteen on transmission
lines and the Smith chart, fifteen on the finite-difference method. Not one mark is revisable from anything
in this repository. It is the first paper in the folder with a total coverage gap.

**The 23 October 2025 end-of-semester paper**, of its 90 printed marks:

| | Marks | Share |
|---|---|---|
| Covered by **WC1**, this cohort's own handout | 17 | 19 % |
| Only in `_reference-old-cohort/` | 35 | 39 % |
| In **neither** | **38** | **42 %** |

Question Two (15 marks) and Question Five (15 marks) are absent end to end, plus 8 marks scattered through
Question One. On the worst legitimate answer-choice — Q1 + Q2 + Q5 — **38 of his 60 marks would be on
material the course has given him no notes for.**

**Say this to him, and do not fill the hole.** Writing standard transmission-line, waveguide and
finite-difference theory into this knowledge base would make it look like his lecturer's notes. The right
move is to ask him for the handouts those questions came from; they belong in `../../sources/current/`.

## ⚠ Recurrence — the strongest signal in this folder

**Twenty of the 2025 exam's thirty compulsory marks are the 13 August 2025 CAT, reused.** Same cohort, ten
weeks apart. Several parts are verbatim, including the entire $150\cos(10^8 t + 8x)$ plane-wave problem.
**That CAT is already `solved` in this folder** — `EEE3202-CAT1-2025-08-13.md`. Working it until it is
automatic is the highest-yield preparation available for this unit's final.

**And the October CAT rehearses the exam.** All four parts of the 1 Oct 2025 CAT reappear on the 23 Oct
exam — exactly the pattern the 3 Oct 2024 CAT showed against the 25 Oct 2024 exam. **Two cohorts, two
Octobers, the same rehearsal.**

**Third recurrence:** *"Distinguish between the Poynting theorem and the Poynting vector"* now appears on
**three** papers — Aug 2024, Aug 2025 and Oct 2025 — verbatim each time, 2 marks each time.

⚠ **The Smith chart is missing.** The 2025 exam's instruction 3 says one is provided; the 1 Oct CAT demands
"determine using Smith Chart" for 11 of its 30 marks and neither supplies one nor says one is provided
(P22). No chart is among the photographed pages of either paper — almost certainly a separate loose sheet.
**Worth asking him for it**, since two papers' worth of transmission-line questions cannot be worked without.

---

# House format — adding the next paper

The canonical statement lives in
[`../../../fluid-flow/knowledge-base/past-papers/00-past-papers-index.md`](../../../fluid-flow/knowledge-base/past-papers/00-past-papers-index.md)
§ House format, and `../../../docs/kb-format.md` governs the KB as a whole. The short version:

1. **Naming** — `<UNIT>-<TYPE>-<YYYY-MM-DD>.md`; figures `figures/<same-stem>-q<N><-subject>.svg`. Add a row
   to the Register and update Topic coverage.
2. **Frontmatter** — `kb, file_role: past-paper, paper_id, paper, unit_code, institution, date, duration_min,
   rubric, questions, total_marks, marks_reconcile, status, source, transcription, figures, figure_dir,
   errata_logged, kb_sections, tags`. Set `marks_reconcile: true` **only** after adding the printed part-marks
   and checking them against the stated total — on this subject's papers that check has failed three times
   out of three.
3. **Transcription** — verbatim in `[q]` blocks, typos included; LaTeX for maths; never reconstruct
   unreadable text or figures (record `legibility:` and ask him to re-shoot); a `→ KB section` mapping and
   the marks on every question; and note any photo artefact — his own pencil especially — that a future chat
   could mistake for exam content.
4. **Figures** — both layers, always: a `figure_data:` block (with `derived_not_printed:`, `legibility:` and
   `ambiguity:` where they apply) and a self-contained SVG with `<title>` and `<desc>` filled in.
5. **Errata** — `../_verification-log.md` **§ E — Exam papers**, IDs allocated continuously across the whole
   folder, referenced from the question by `⚠ VERIFY`. The full entry lives in the log only.
6. **Solutions** — `status: unsolved` by default. Worked solutions go in a separate
   `<paper_id>-solutions.md` so the questions stay usable as clean practice.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
