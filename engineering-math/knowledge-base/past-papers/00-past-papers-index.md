---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
file_role: past-papers-index
purpose: "Register of every CAT / exam / assignment paper transcribed into this knowledge base, plus the house format for adding the next one."
papers: 1
total_questions: 5
total_marks: null          # the paper shows no mark allocation
unit_codes: ["EMT 3101"]
errata_next_id: "P4"
status_legend: "unsolved = questions only · partial = some model answers worked & verified · solved = all worked & verified"
---

# EMT 3101 — Assessed work index

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
> 3. Every solution is **ours** — none of these papers carries answers. Verify every number
>    independently before writing it down, and show the check.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| EMT 3101 **Assignment 1** | 10 Aug 2026 | — | 5 | `solved` | [`EMT3101-ASSIGNMENT1-2026-08-10.md`](EMT3101-ASSIGNMENT1-2026-08-10.md) |

The paper shows **no mark allocation** — only "Answer ALL questions". Errata IDs run across the
whole folder, not per paper: **P1–P3** belong to Assignment 1. The next paper starts at **P4**.

*(No CAT or end-of-semester paper has been seen yet. Add a row as each arrives.)*

---

## What we know about examinable scope

**One paper is a thin evidence base** — treat what follows as a working hypothesis, not a
prediction, and revise the whole syllabus.

### Coverage so far

| Knowledge-base file | Questions drawn from it |
|---|---|
| `01` Gamma and Beta Functions | **Q1, Q2, Q3(a), Q3(b), Q5** — four of five questions |
| `04` Maclaurin's Theorem | Q4 (expand, then integrate term by term) |
| `02` CRV and Beta Distribution | none |
| `03` Binomial Theorem | none |
| `05` Leibniz Theorem | none |
| `06` Bessel's Equation | none |

### The pattern

**Four of the five questions are the same skill in different clothing: recognise an integral's
shape and read the Gamma or Beta parameters off it.** Not one asks for a definition, a property, or
a derivation reproduced from the notes.

That points revision at `01` §5.4 and §5.5 — the improper form and the trigonometric form, and the
read-off rules that go with them. Those two pages carry the paper.

**Q4 is the exception** and worth naming precisely: it expands $\cos2\theta$ by Maclaurin and then
integrates $\theta^{2k-1/3}$ term by term. **No Gamma or Beta function appears in it** — it is the
one question testing the *series* half of the course rather than the *special functions* half.

**Two further habits the paper rewards:**

- **Two of the five integrals are improper** — Q3(b) is singular at $x = 3$, Q4 at $\theta = 0$ —
  and neither question mentions it. The Beta and Gamma definitions absorb both without special
  treatment, because all they require is $m, n > 0$. Saying so explicitly is a free mark.
- **Q1 and Q3 both hinge on choosing the right substitution**, and in both cases the substitution is
  handed to you. When it is not, the thing to look for is the one that makes an unwanted term cancel
  (Q1) or maps the interval onto $[0,1]$ (Q3).

### Where a future paper would most plausibly go

- **Q4 is the only cross-topic question** — Maclaurin feeding an integral. It is the one natural
  bridge between the two halves of the course, so it is the likeliest place for another combined
  question.
- **Files `02`, `03`, `05` and `06` are entirely untested so far.** `06` in particular is the
  course's technical peak — six recurrence proofs across five pages — and it would be surprising for
  it to stay unassessed. **Do not read "not on Assignment 1" as "not examinable".**

---

## Paper errata (P1–P3)

Defects found in the papers themselves, as distinct from the lecture notes. Same numbering habit as
the rest of the project: `P1`, `P2`, …

| ID | Paper | Question | The paper prints | Should be |
|---|---|---|---|---|
| **P1** | Assignment 1 | Q1 | substitution "$u = x + u\sqrt x$" | $t = x + u\sqrt x$ — as printed it is self-referential; the integration variable has been lost |
| **P2** | Assignment 1 | Q3 | **both parts lettered "(a)"** | (a) and (b) — "Hence" makes the order unambiguous |
| **P3** | Assignment 1 | Q1 | $n! \;=\; \sqrt{2\pi}e^{-n}n^{n+1/2}$ | Stirling's formula is **asymptotic**: $\sim$ or $\approx$, not $=$. At $n = 50$ the ratio is still 1.0017 |

**One paper, three defects, and one of them (P1) blocks the first step of the question.** That is
consistent with the lecture notes, where 24 flags were raised across 66 pages. **Read the question
paper as critically as you read the notes** — and if a printed substitution or constant cannot
possibly work, say so in your answer and proceed with the corrected version rather than stalling.

---

## Format for adding the next paper

1. Transcribe the questions into Markdown — **never commit a scan or photograph of the paper**.
2. Name the file `EMT3101-<TYPE>-<YYYY-MM-DD>.md`, e.g. `EMT3101-CAT1-2026-10-15.md`.
   Wrap each question stem in a `[q]` block — the paper's wording **verbatim**, typos and all.
3. Solve every question. **Verify every numerical answer independently before writing it down**, and
   show the check at the end of each solution.
4. Mark clearly that the solutions are ours — the papers carry no answers.
5. Log any defect in the paper as `P4`, `P5`, … in the table above, and repeat it in the paper's own
   file.
6. Add a row to the register, and update § What we know about examinable scope.
7. Redraw any figure as SVG in `figures/` — never screenshot it.
8. Update the past-paper register in `../00-index.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
