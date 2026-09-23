---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
file_role: past-papers-index
purpose: "Register of every CAT / exam / assignment / tutorial paper transcribed into this knowledge base, plus the house format for adding the next one."
papers: 5
total_questions: 25
total_parts: 65
unit_codes: ["EMT 3101"]
errata_next_id: "P23"
status_legend: "unsolved = questions only · partial = some model answers worked & verified · solved = all worked & verified"
---

# EMT 3101 — Assessed and tutorial work index

> **Read me first.** This folder holds assessment papers **and tutorial sheets** transcribed into Markdown
> and, where marked `solved`, worked through. Use it to quiz him, to set a timed mock, or to work a question with him. Open the paper
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
>
> **⚠ Errata convention changed.** `P1`–`P3` live in Assignment 1's own **Errata** section, as this folder
> originally did it. **Everything from `P4` on lives in `../_verification-log.md` § F · Exam papers**,
> matching every other subject. Both places are canonical for their own IDs.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| EMT 3101 **Assignment 1** | 10 Aug 2026 | — | 5 | `solved` | [`EMT3101-ASSIGNMENT1-2026-08-10.md`](EMT3101-ASSIGNMENT1-2026-08-10.md) |
| EMT 3101 **CAT 1** | 20 Aug 2024 | none printed (24 by inference) | 4 (9 parts) | `unsolved` | [`EMT3101-CAT1-2024-08-20.md`](EMT3101-CAT1-2024-08-20.md) |
| EMT 3101 **End of Semester** | 23 Oct 2024 | 90 printed / 60 sat ✓ | 5 (21 parts) | `unsolved` | [`EMT3101-EXAM-2024-10-23.md`](EMT3101-EXAM-2024-10-23.md) |
| EMT 3101 **End of Semester** | 27 Oct 2025 | 90 printed / 60 sat ✓ | 5 (20 parts) | `unsolved` | [`EMT3101-EXAM-2025-10-27.md`](EMT3101-EXAM-2025-10-27.md) |
| EMT 3101 **Tutorial 1** | 31 Aug 2026 | 26 in parts, no total | 6 (10 parts) | `unsolved` | [`EMT3101-TUTORIAL1-2026-08-31.md`](EMT3101-TUTORIAL1-2026-08-31.md) |

Assignment 1 and the 2024 CAT show **no mark allocation**; Tutorial 1 prints part-marks but no total. Both
end-of-semester papers reconcile question by question, though neither prints a paper total. Errata IDs run
across the whole folder: **P1–P3** belong to Assignment 1 (in its own file), **P4–P22** to the four items
added since (in `../_verification-log.md` § F). The next paper starts at **P23**.

**Two of the five are current-cohort (2026) material** — Assignment 1 and Tutorial 1. The other three are
the papers the 2024 and 2025 cohorts actually sat.

**⚠ EMT 3201 is a different unit.** Engineering Mathematics IV — statistics, sat in Semester 2 — lives in
`../../../engineering-math-iv/`, has no knowledge base, and has its own separate `P`-series. Do not confuse
the two.

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


---

## ⚠⚠ The 2025 final is the 2024 final, and not one repeated question was reworded

This is the strongest recurrence anywhere in this repository, and it deserves to be stated precisely.

**70 of the 2025 paper's 90 printed marks are questions from the 2024 paper.** Every single repeat is
**word for word** — not one was rephrased, and not one had its numbers changed. Four repeats had their
marks adjusted (Q1(e) 4→5, Q1(f) 4→5, Q3(a)(i) 3→4, Q4(b) 15→11). Questions Two and Five were reprinted
identically — same slots, same marks, same wording. **The formula sheet was reprinted with its defect
intact.**

All four genuinely new questions — 20 marks — went into **Question One**, the compulsory one. Nineteen
marks were dropped.

**And a third paper agrees.** The ODE $y'' + xy' + 2y = 0$ appears on **all three** papers in identical
wording: the 2024 CAT (7 marks), the 2024 final (15) and the 2025 final (11) — **33 marks across three
sittings**.

The honest caveat, which should be said alongside: **this is two finals and one CAT, not a rule.** A
lecturer can change a paper at any time. But if he works the 2024 final until it is automatic, the evidence
says he has seen most of the next one.

### ⚠ And the 2026 tutorial draws from the same pool

`EMT3101-TUTORIAL1-2026-08-31.md` was issued to **this** cohort on 31 August 2026. **Three of its six
questions are already in this folder — and between them they touch every prior EMT 3101 paper we hold:**

- **Q6** — the Beta reduction formula and $\int_0^1 x^5(1-x^3)^2dx$ — **is the 2025 final's Q3(b),
  reissued with its printed error intact.** The identity is still missing the $x^n$ it depends on
  (**P13** on the final, **P21** on the tutorial). The lecturer has now published that same broken
  identity twice.
- **Q4** — the second moment of area $bl^3/12$ with $b$ up 3.5 % and $l$ down 2.5 % — is on **both** the
  2024 and 2025 finals. Third appearance, and the tutorial adds a symbol typo the exams do not have (P20).
- **Q5** — expand $\sqrt{x}\ln(x+1)$, then integrate to 3 d.p. over $[0,0.5]$ — **is the 20 Aug 2024
  CAT 1's Q4, verbatim.** Same function, same interval, same instruction; only the mark changed, 5 → 4.

So the recurrence runs in every direction available: **the finals repeat each other, the tutorials draw
from the same pool, and the CAT feeds the tutorials.** Half of the 2026 tutorial has been examined before.
Three of its six questions are genuinely new, so this is a tendency rather than a rule — but on this
evidence **every paper in this folder is live revision material**, not history.

## Coverage across the five papers

| KB topic file | Where it has been examined |
|---|---|
| `01-gamma-and-beta-functions` | CAT Q2 · 2024 Q1(f), Q5(b)(i) · 2025 Q1(e), Q3(b), Q5(b)(i) · **Tutorial 1 Q3 (all four items), Q6(a)–(b)** |
| `02-crv-and-beta-distribution` | CAT Q1 · 2024 Q1(c), Q3(a), Q3(b), Q5(a) · 2025 Q1(c), Q3(a), Q5(a) — **the heaviest section in the unit** |
| `03-binomial-theorem` | 2024 Q1(a), Q1(b), Q2(c) · 2025 Q1(b), Q2(c), Q4(a) · **Tutorial 1 Q1, Q2** |
| `04-maclaurin-theorem` | CAT Q4 · 2024 Q1(g), Q2(a) · 2025 Q1(f), Q2(a) · **Tutorial 1 Q5** |
| `05-leibniz-theorem` | 2024 Q1(e) — **once** |
| `06-bessels-equation` | 2025 Q1(a) — **once** |
| ❌ **not in the KB** | CAT Q3 · 2024 Q1(d), Q2(b), Q4, Q5(b)(ii) · 2025 Q1(d), Q2(b), Q4(b), Q5(b)(ii) · **Tutorial 1 Q4** (small changes / total differentials — in none of the six topic files, and now examined three times) |

**Gap totals: 27 of 90 on the 2024 final, 24 of 90 on the 2025 final, 7 of 24 on the CAT.** Frobenius is
already a documented gap; **Legendre polynomials and the Gamma duplication formula appear nowhere in the
knowledge base** and should be added to the gap map.

**Two questions run the other way — they are lifted verbatim from the lecture notes.** Q2(c) is ·BIN p8
Example 1 and Q5(a) is ·CRV p16 Example 1, on both finals. ⚠ The knowledge base already flags **V3** inside
the latter, so check the correction before teaching it.

## ⚠ Four defects worth knowing before he revises

- **P4 ★** 2024 Q1(c) asks him to *show* the variance is $1/(18a^2)$. It is $a^2/18$ — confirmed
  symbolically. He cannot show what is printed.
- **P9 ★** The 2024 CAT's Q2 gives the Gamma integral the domain of its analytic continuation, so as printed
  it claims convergence at $x = -\tfrac12$.
- **P13 ★** The 2025 Q3(b) Beta reduction formula is printed with no $n$ on the left; the corrected form
  gives $1/36$, matching direct integration.
- The formula sheet on the 2024 paper carries a defect and was reprinted unchanged in 2025.

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
