---
kb: "Analogue Electronics I — BEE 3103"
file_role: past-papers-index
purpose: "Register of every CAT / exam paper transcribed into this KB, plus the house format for adding the next one."
papers: 4
total_questions: 12
total_parts: 71
unit_codes: ["BEE 3106", "BEE 3103"]
unit_code_note: "⚠ THE KB AND THE PAPERS DISAGREE. This knowledge base and CLAUDE.md both call the unit BEE 3103; all four papers are printed BEE 3106. Same unit, same lecturer, same content — the code on the paper is what the file names use. Logged once as erratum P1. Codes are not unique anywhere in this repository; match a paper by unit NAME."
status_legend: "unsolved = questions only · partial = some model solutions worked & verified · solved = all verified"
canonical_house_format: "../../../fluid-flow/knowledge-base/past-papers/00-past-papers-index.md § House format"
---

<!-- Compiled by Jotham-JS, 2026. Analogue Electronics I knowledge base — past papers. -->

# Past Papers — index

> **Read me first.** This folder holds the actual assessment papers, transcribed verbatim and
> machine-readable. Use it to quiz him, to set timed mocks, or to work a question with him. Each paper file
> is self-contained and says what it maps to in the main KB.
>
> **Two rules that matter:**
> 1. `[q]` text is the paper's exact wording — quote it as printed. Where the paper is *wrong*, it stays
>    wrong in the `[q]` block and carries a `⚠ VERIFY` marker; the correction lives in
>    `../_verification-log.md` (§ Exam papers). Teach the correct form, and tell him the paper is wrong.
> 2. Figures are recorded as `figure_data:` blocks — every component, value, rail and node in words. **No
>    SVGs have been drawn for this subject yet.** The blocks are the authoritative record; redraw on demand.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| **CAT** | 17 Sep 2024 | 40 ✓ | 1 (8 items) | `unsolved` | [`BEE3106-CAT-2024-09-17.md`](BEE3106-CAT-2024-09-17.md) |
| **End of Semester** | 22 Oct 2024 | 90 printed / 60 sat | 5 (25 parts) | `unsolved` | [`BEE3106-EXAM-2024-10-22.md`](BEE3106-EXAM-2024-10-22.md) |
| **CAT** | 9 Sep 2025 | 40 ✓ | 1 (8 items) | `unsolved` | [`BEE3106-CAT-2025-09-09.md`](BEE3106-CAT-2025-09-09.md) |
| **End of Semester** | 21 Oct 2025 | 90 printed / 60 sat | 5 (30 parts) | `unsolved` | [`BEE3106-EXAM-2025-10-21.md`](BEE3106-EXAM-2025-10-21.md) |

**Errata IDs** run across the whole folder, not per paper: **P1–P20**. The next paper starts at **P21**. Full
entries live in `../_verification-log.md` **§ Exam papers**, and nowhere else.

**All four papers reconcile per question.** Neither exam prints a paper-level total, and neither CAT prints a
total or a rubric — but every printed allocation adds up to its heading. This is the best-behaved set of
papers in the repository.

---

## ⚠ The finding that matters most: the 2025 CAT is the 2024 CAT, verbatim

**All eight items. All forty marks. Word for word.** Two cohorts, twelve months apart, the same paper —
the same P-N junction biasing question, the same clipper with the same 15 V sinusoid and 0.7 V silicon
diode, the same FET tree diagram, the same enhancement-only NMOS pair at V_GS(th) = 2 V and
K = 2 × 10⁻³ A/V², the same five-mask NMOS flow.

Say this to him plainly, and then say the honest caveat: **two papers is not a rule.** But if he sits a CAT
in this unit, working the 2024/2025 CAT until it is automatic is the single highest-yield hour available to
him anywhere in this repository.

**And the CAT feeds the exam.** Five of its eight items — 25 of its 40 marks — reappear on the 2024
end-of-semester paper. **Czochralski crystal growth** appears on both exams; so does **ion implantation**.
The **transformer-coupled two-stage amplifier** figure is reused between exams with only β changed, 50 → 75.

---

## Topic coverage

| KB topic file | Where it has been examined |
|---|---|
| `01-matter-atoms-and-semiconductors` | ❌ **never** |
| `02-resistors-and-dc-network-theorems` | ❌ **never — zero marks across all four papers** |
| `03-capacitors-inductors-and-transformers` | 2024 exam Q5(a) · 2025 exam Q2(b) *(turns ratio only)* |
| `04-diodes` / `11-diodes` | CAT (a) · 2024 exam Q1(b), Q2(a) · 2025 exam Q1(b), Q3(b), Q3(d), Q3(e), Q5(c) |
| `05-rectifiers-filters-and-regulation` / `12-rectifiers` | CAT (b) · 2024 exam Q1(c), Q2(b), Q2(c) · 2025 exam Q1(d), Q4(b), Q5(d) |
| `06-bipolar-junction-transistors` / `13` | CAT (c), (h) · 2024 exam Q1(d), Q1(i), Q3(b) · 2025 exam Q1(b), Q2(c) |
| `07-field-effect-transistors` / `14` | CAT (d), (e) · 2024 exam Q1(a), Q1(e), Q3(a), Q3(c) · 2025 exam Q1(c), Q1(g), Q4(a), Q4(c) |
| `15-fabrication-and-integrated-circuits` | CAT (f), (g) · 2024 exam Q1(f), Q4(a), Q4(c), Q5(b) · 2025 exam Q1(a), Q1(h), Q5(a), Q5(b) |
| `16-h-parameters-and-bjt-amplifiers` | 2024 exam Q1(h), Q4(b) · 2025 exam Q1(e), Q2(a), Q3(a) |
| `17-multistage-feedback-frequency-response` | 2024 exam Q1(g), Q5(a), Q5(c) · 2025 exam Q1(f), Q2(b), Q3(c), Q4(d) |

**`15`, `16` and `17` carry the exams.** Between them they take roughly half of every end-of-semester paper —
fabrication and IC processing, h-parameter analysis, and multistage/feedback/frequency response. They are
also the three topic files that sit furthest from the CATs, which never leave diodes, transistors and
fabrication. **Revising for a CAT and revising for the exam are different jobs in this unit.**

**`02` has never been worth a single mark.** Worth knowing before he spends an evening on network theorems.

---

## ⚠ Where the papers outrun the primary source

Nothing on these four papers is absent from the knowledge base — but a great deal of it is absent from
**tier 1**, the 100-page course lecture notes, and is only covered by the tier-2 lesson documents and tier-3
decks that `00-index.md` classes as supporting material.

| Paper | Marks on material tier 1 does not teach |
|---|---|
| 2024 end-of-semester | **59 of 90 (66 %)** — 21 on `15`, 11 on `16`, 9 on `17`, 8 `11`-only, 7 `12`-only, 3 on `14` §4.8 |
| 2025 end-of-semester | **43 of 90 (48 %)** |
| Either CAT | 10 of 40, all on `15` |

**Two-thirds of the 2024 exam could not be revised from the course lecture notes alone.** Teach from the
tier-2 and tier-3 material without apology — but say which tier it comes from, because he will not find it
in the notes he was handed.

### ⚠ Three questions sit on redacted source pages

The verification log records certain source pages as unusable. These questions land on them:

- **2024 exam Q5(c)** sits exactly on **V7.17**.
- **CAT item (e)** and **2024 exam Q3(c)** sit on **·J p91** — the log's worst offender.
- **2025 exam Q4(a), 6 marks**, sits on **·J p87–p89**.

Check the verification log before teaching any of these three, and tell him the source is unreliable rather
than letting him absorb it.

---

# House format — adding the next paper

The canonical statement lives in
[`../../../fluid-flow/knowledge-base/past-papers/00-past-papers-index.md`](../../../fluid-flow/knowledge-base/past-papers/00-past-papers-index.md)
§ House format; `../../../docs/kb-format.md` governs the KB as a whole. In short:

1. **Naming** — `<UNIT>-<TYPE>-<YYYY-MM-DD>.md`, using the code **as printed** (BEE 3106 here, not BEE 3103).
2. **Frontmatter** — the full key list, with `marks_reconcile: true` only after the printed part-marks have
   been added and checked against the stated total.
3. **Transcription** — verbatim `[q]` blocks including typos; LaTeX for maths; a `→ KB section` mapping and
   the marks on every question; never reconstruct anything unreadable; record every photo artefact.
4. **Figures** — exhaustive `figure_data:` blocks. In this subject that means every resistor value, every
   supply rail, every labelled node, every device with its β or K where given, and the input waveform's
   shape and amplitude. **Never guess a component value or a device polarity** — flag `legibility:` instead.
5. **Errata** — `../_verification-log.md` **§ Exam papers**, IDs continuous across the folder, referenced
   from the question by `⚠ VERIFY`. The full entry lives in the log only.
6. **Solutions** — `status: unsolved` by default; worked solutions go in a separate `<paper_id>-solutions.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
