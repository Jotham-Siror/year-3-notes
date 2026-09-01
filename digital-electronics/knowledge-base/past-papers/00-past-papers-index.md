---
kb: "Digital Electronics — BEE 3102"
lecturer: "withheld"
file_role: past-papers-index
purpose: "Register of every CAT / exam / assignment paper transcribed into this knowledge base, plus the house format for adding the next one."
papers: 1
total_questions: 8
total_marks: 30
unit_codes: ["BEE 3102"]
errata_next_id: "P4"
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
> 3. Every figure is stored **twice**: a `figure_data:` block inside the paper file (authoritative,
>    in words and numbers) and a rendered SVG in `figures/`. Reason from the block; show him the SVG.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| BEE 3102 **CAT 1** | 6 Aug 2024 | 30 | 8 | `solved` | [`BEE3102-CAT1-2024-08-06.md`](BEE3102-CAT1-2024-08-06.md) |

Errata IDs run across the whole folder, not per paper: **P1–P3** belong to the 2024 CAT. The next
paper starts at **P4**.

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
