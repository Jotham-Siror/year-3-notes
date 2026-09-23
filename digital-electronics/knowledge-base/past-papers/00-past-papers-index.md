---
kb: "Digital Electronics — BEE 3102"
lecturer: "withheld"
file_role: past-papers-index
purpose: "Register of every CAT / exam / assignment paper transcribed into this knowledge base, plus the house format for adding the next one."
papers: 5
total_questions: 29
total_parts: 81
unit_codes: ["BEE 3102"]
unit_code_note: "⚠ BEE 3102 is ALSO the code printed on both 2024 Electromagnetic Fields CATs — same code, same cohort, two different units. Match a paper by unit NAME."
errata_next_id: "P22"
status_legend: "unsolved = questions only · partial = some model answers worked & verified · solved = all worked & verified"
---

<!-- Compiled by Jotham-JS, 2026. Digital Electronics BEE 3102 knowledge base — past papers. -->

# Past Papers — index

> **Read me first.** This folder holds assessment papers transcribed into Markdown and worked
> through. Use it to quiz him, to set a timed mock, or to work a question with him. Open the paper
> file; each one is self-contained and says what it maps to in the main knowledge base.
>
> **Three rules that matter:**
>
> 1. **The papers themselves are never committed.** `docs/kb-format.md` rule 4 forbids photographs
>    or scans of examination papers. The transcription in this folder is the only copy held.
> 2. `[q]` text is the paper's exact wording. Where the paper is *wrong*, it stays wrong in the `[q]`
>    block and carries a marker; the correction lives in that paper's **Errata** section. Teach the
>    correct form and say plainly that the paper is wrong — never silently fix it.
> 3. Every figure has a `figure_data:` block inside the paper file — authoritative, in words and
>    numbers. The 2024 CAT 1 also has rendered SVGs in `figures/`; **the four papers added in 2026 have
>    `figure_data` blocks only.** Reason from the block; redraw on demand.
>
> **⚠ Errata convention changed.** `P1`–`P3` live in the 2024 CAT 1's own **Errata** section, as this
> folder originally did it. **Everything from `P4` on lives in `../_verification-log.md` § Exam papers**,
> matching every other subject in the repository. Both places are canonical for their own IDs.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| BEE 3102 **CAT 1** | 6 Aug 2024 | 30 ✓ | 8 | `solved` | [`BEE3102-CAT1-2024-08-06.md`](BEE3102-CAT1-2024-08-06.md) |
| BEE 3102 **CAT 2** | 25 Aug 2024 | 30 stated / **29 printed** ⚠ | 3 (12 parts) | `unsolved` | [`BEE3102-CAT2-2024-08-25.md`](BEE3102-CAT2-2024-08-25.md) |
| BEE 3102 **End of Semester** | 28 Oct 2024 | 90 printed / 60 sat ✓ | 5 (24 parts) | `unsolved` | [`BEE3102-EXAM-2024-10-28.md`](BEE3102-EXAM-2024-10-28.md) |
| BEE 3102 **CAT 1** | 14 Aug 2025 | 30 ✓ | 8 (10 parts) | `unsolved` | [`BEE3102-CAT1-2025-08-14.md`](BEE3102-CAT1-2025-08-14.md) |
| BEE 3102 **End of Semester** | 3 Nov 2025 | 90 printed / 60 sat ✓ | 5 (27 parts) | `unsolved` | [`BEE3102-EXAM-2025-11-03.md`](BEE3102-EXAM-2025-11-03.md) |

Errata IDs run across the whole folder, not per paper: **P1–P3** belong to the 2024 CAT 1 (in its own file),
**P4–P21** to the four papers added since (in `../_verification-log.md` § Exam papers). The next paper starts
at **P22**.

**Four of the five reconcile.** Only the 2024 CAT 2 does not: its printed allocations sum to 29 against a
stated 30, with Question 3's three parts sharing an unallocated 7 (P4).

## What the papers say about scope

Only one paper is held, so treat this as a single data point rather than a pattern — but it is a
sharp one.

| Source | Marks in CAT 1 2024 | Share |
|---|---|---|
| **CH4 — signal conversion, DAC half** | **15** | **50 %** |
| CH2 — digital logic families | 8 | 27 % |
| CH3 — memory and programmable logic | 4 | 13 % |
| Not taught in any deck | 3 | 10 % |
| CH5 + CH6 — FSMs and ASMs | 0 | 0 % |

- **Half the marks came from twenty slides.** `../06-digital-to-analogue-conversion.md` is the whole
  DAC half of Chapter 4 and it carried Q5, Q6, Q7 and Q8. Best marks-per-page in the unit by far.
- **Chapters 5 and 6 were not examined at all** — 158 slides, zero marks. Expected in a CAT 1 sat
  mid-semester; it says where CAT 2 and the final examination must go instead.
- **Three marks were outside the taught material entirely.** Q1 asks for monotonicity, linearity and
  sensitivity; the first two appear only in a list of reading topics on ·CH4 slide 49 and the third
  appears nowhere in any deck.
- **One question sits directly on a defective slide.** Q5 is ·CH4 slide 37's BCD example with a
  fourth digit added, and the deck's version of that example is wrong in three places
  (**V06-4**, **V06-6**, **V06-7**). Revising from the slide as printed would carry the error into
  the exam.

## Coverage by knowledge-base file

| KB file | Questions that have appeared |
|---|---|
| `../02-digital-logic-families.md` | Q2 (TTL NAND truth table), Q3 (draw a DTL NAND) |
| `../04-programmable-logic-devices.md` | Q4 ($8\times4$ PROM) |
| `../06-digital-to-analogue-conversion.md` | Q5 (BCD DAC), Q6 (weighted-resistor ladder), Q7 (transfer relation), Q8 (binary-weighted DAC) |
| *not covered by any file* | Q1 (monotonicity, linearity, sensitivity) |
| `01`, `03`, `05`, `07`, `08`, `09`, `10` | none yet |


---

## Coverage across the five papers

| KB topic file | Where it has been examined |
|---|---|
| `01-introduction-and-recap` | ❌ never directly |
| `02-digital-logic-families` | 2024 CAT 1 Q1, Q3 · 2025 CAT Q2 · 2024 exam Q1(a), Q1(b), Q2(i) · 2025 exam Q1(a) |
| `03-semiconductor-memory` | 2024 exam Q4(c) |
| `04-programmable-logic-devices` | 2024 CAT 1 Q4 · 2025 CAT Q6, Q7 · 2024 exam Q1(c), Q2(a) · 2025 exam Q1(c), Q1(e) |
| `05-analogue-to-digital-conversion` | 2025 CAT Q1 · 2024 exam Q5(a)(i)–(iii) |
| `06-digital-to-analogue-conversion` | 2024 CAT 1 Q5–Q8 · 2025 CAT Q3, Q4, Q5, Q8 · 2024 exam Q1(e), Q1(g), Q2(b) · 2025 exam Q1(b), Q1(d), Q2(b) |
| `07-fsm-fundamentals-and-analysis` | 2024 CAT 2 Q1(i), (iv), (vii) · 2024 exam Q3(a)(iii), Q4(b) · 2025 exam Q1(f)(ii), Q2(a)(i), Q3(a)(iii), Q4(a)(i), Q5(a)(v) |
| `08-sequential-circuit-design` | 2024 CAT 2 Q1(ii), (iii), (vi), (vii), (viii) · 2024 exam Q1(d), Q1(f), Q3(a)(i), (iv), (v) · 2025 exam Q1(f)(i), Q1(g), Q3(a), Q5(a) — **ten separate parts** |
| `09-state-reduction-and-assignment` | 2024 CAT 2 Q1(v), Q2, Q3 · 2024 exam Q3(a)(ii), Q4(a)(ii) · 2025 exam Q2(a)(ii)–(iii), Q3(a)(ii), Q4(a)(ii), Q4(b), Q5(a)(iii) |
| `10-algorithmic-state-machines` | 2024 exam Q1(h) — **once, 6 marks** |

**The CATs and the exams test different halves of the course.** Both CAT 1s live in `02`, `04`, `05` and
`06` — logic families, PLDs and converters. Both CAT 2s and both exams live in `07`, `08` and `09` — state
machines, sequential design and state reduction. `08` and `09` between them carry roughly a third of every
end-of-semester paper.

**`10-algorithmic-state-machines` has been examined once in five papers, for 6 marks.** Worth knowing before
he spends an evening on ASM charts.

## ⚠ Two documented gaps, both on the 2024 exam

| Question | Marks | Status |
|---|---|---|
| Q4(a)(i) — reduce states by the **partitioning method** | 4 | Named on ·CH5 s82, **worked nowhere in 348 slides** |
| Q5(b) — write a **Verilog** full adder | 5 | Verilog appears only in ·CH1 s32's one-line description |

Both sit in optional questions, so they are avoidable — but they are new gap-map rows, and the other three
papers have no gap at all.

## ⚠ Recurrence — heavier here than in any other subject

**The 2025 CAT reprints seven of the 2024 CAT's eight questions.** Three word for word, one carrying the
same `Σm(a,b,c)` typo the 2024 printing had.

**The 2024 exam reprints the 2024 CAT 1's Q5 and Q7 verbatim** as its Q1(e) and Q1(g).

**The 2025 exam reprints the 2024 exam's Figure 2 and the 2024 CAT 2's Table 1 — defects included.** The
same broken state-transition label survives two printings a year apart (P8).

**And two of the 2025 exam's figures are the lecture deck's own worked examples.** Figure 6 is the
·CH5 s83–90 implication-table machine (all sixteen transitions and eight outputs match); Figure 7 is the
·CH5 s75–81 detector tree — and the exam labels node E correctly where the slide prints a second D, which
the verification log already flags. **The lecturer sets his own slides as exam questions.** Working the
deck's worked examples until they are automatic is, on this evidence, the most direct preparation available.

2024 exam Q5(a) is likewise the ·CH4 s18 homework verbatim — 10 marks.

## ⚠ What could not be read

Transistor-level details on the bias figures: substrate-arrow directions on the 2024 exam Q3/Q4 and the
2025 CAT's Figure 1(b), R₂'s subscript in the 2024 printing, and the channel polarity of all four MOSFETs in
the 2025 exam's Figure 1(b). Topology is recorded in full; polarity is **not asserted**. All flagged
`legibility: partly illegible`.

⚠ **One for the lecturer:** in *both* printings of Figure 1(b), Q4's base returns to its own emitter node —
which makes Q4 inert — and neither sub-circuit's output has a pull-up (P13). Not resolved here.

---

## Adding the next paper

1. Name it `BEE3102-<TYPE>-<YYYY-MM-DD>.md` — e.g. `BEE3102-EXAM-2025-12-04.md`.
2. Transcribe the questions **verbatim** into `[q]` blocks, typos and all. Do not commit the scan.
3. Reconcile the printed part-marks against the stated total before going further, and record
   `marks_reconcile:` in the frontmatter. A mismatch means something was missed in the
   transcription.
4. Redraw every figure as SVG into `figures/`, and give each one a `figure_data:` block in the
   paper file.
5. Answer each question in two parts — **Exam answer** sized to the mark allocation, then
   **Working**. Keep them separate so the file can still be used as a mock.
6. **Recompute every number in Python** before writing it down, and say so in a Verification
   section at the foot of the file.
7. Continue the errata numbering from `errata_next_id` in this file's frontmatter, and update it.
8. Map every question to its knowledge-base section, and state honestly where a question is **not**
   covered by any of them. That gap map is the most useful thing a past paper produces.
9. Update the register, the scope table and the coverage table above.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026.</i></sub>
