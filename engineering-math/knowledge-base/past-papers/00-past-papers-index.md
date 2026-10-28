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
> and, where marked `solved`, worked through. Use it for quizzing, for setting a timed mock, or for working
> a single question through. Open the paper file; each one is self-contained and says what it maps to in the
> main knowledge base.
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

**Five papers, read together:** Assignment 1 (10 Aug 2026), CAT 1 (20 Aug 2024), the end-of-semester
finals of 23 Oct 2024 and 27 Oct 2025, and Tutorial 1 (31 Aug 2026). That is still a thin evidence base,
and thinner than it looks: the 2025 final is largely the 2024 final reprinted (see the next section).
Treat what follows as a working hypothesis, not a prediction, and revise the whole syllabus.

### Coverage so far

Printed marks by knowledge-base file. Assignment 1 prints no marks, so it is counted in questions. The
question-by-question list is § Coverage across the five papers, further down. **"Sat papers"** means the
three that a cohort actually sat as assessments: the CAT and the two finals.

| Knowledge-base file | Assignment 1 (questions) | CAT 1 2024 (of 24) | Final 2024 (of 90) | Final 2025 (of 90) | Tutorial 1 (of 26) | Sat papers (of 204) |
|---|---|---|---|---|---|---|
| `01` Gamma and Beta Functions | **4 of 5** | 5 | 8 | 14 | 11 | 27 |
| `02` CRV and Beta Distribution | — | **7** | **26** | **21** | — | **54** |
| `03` Binomial Theorem | — | — | 15 | 15 | 7 | 30 |
| `04` Maclaurin's Theorem | 1 of 5 | 5 | 10 | 11 | 4 | 26 |
| `05` Leibniz Theorem | — | — | 4 | — | — | 4 |
| `06` Bessel's Equation | — | — | — | 5 | — | 5 |
| ❌ **Not in this knowledge base** | — | **7** | **27** | **24** | 4 | **58** |

*Every column reconciles: CAT $5+7+5+7 = 24$; 2024 $8+26+15+10+4+27 = 90$; 2025
$14+21+15+11+5+24 = 90$; Tutorial 1 $11+7+4+4 = 26$. These are **printed** marks. On each final only
60 of the 90 are attemptable (Question One plus any two), so no single candidate meets every mark in a
column.*

### ⚠ Examined, but not in this knowledge base

**58 of the 204 printed marks on the sat papers, plus 4 on Tutorial 1.** That is more than any single
topic file carries. It comes from four items:

| Item | Where it has been set | Printed marks | Avoidable? | Why the knowledge base cannot teach it |
|---|---|---|---|---|
| **Power-series solution of $y'' + xy' + 2y = 0$**, with $y(0) = 1$ and $y'(0) = 2$. By Leibniz–Maclaurin on the CAT; by Leibniz–Maclaurin *or* Frobenius on the finals | CAT Q3 · 2024 Q4 · 2025 Q4(b), with **identical wording all three times** | $7 + 15 + 11 =$ **33** | **No** on the CAT ("Answer ALL"); optional on the finals | Frobenius is a documented gap (`../00-index.md` § Gap map). The Leibniz–Maclaurin route to an ODE is in neither `04` nor `05` |
| **Legendre polynomials** | 2024 Q1(d): $P_2(x)$ by Rodrigues' formula · 2025 Q1(d): a cubic written as a combination of Legendre polynomials | $4 + 5 =$ **9** | **No: inside the compulsory Question One, both years** | *Legendre* and *Rodrigues* occur nowhere in this knowledge base |
| **Gamma duplication formula** | Q2(b) on both finals (formula stated, a corollary asked for) · Q5(b)(ii) on both finals (formula derived) | $3 + 5 + 3 + 5 =$ **16** | optional questions | Not in `01`, and not on either final's printed formula sheet |
| **Small changes / total differentials** | Tutorial 1 Q4, the $bl^3/12$ second-moment question that both finals also set as Q1(b) | **4** | no (tutorial: "Answer ALL") | The finals add "Using the Binomial theorem", which `03` §5 covers. The tutorial drops that instruction, and partial differentiation is in none of the six topic files |

**The ODE is the most-repeated item in the subject, and the one this knowledge base can least help
with.** It is on every paper a cohort has sat. It is the first thing to build if lecture notes for it
arrive. **Legendre is the only gap item that cannot be avoided on a final.**

### The pattern

1. **`02` carries the most marks on every paper actually sat**: 7 of 24 on the CAT, 26 of 90 in 2024,
   21 of 90 in 2025. Across the three that is 54 of 204, nearly twice the next file (`03`, 30). It is
   absent from Assignment 1 and Tutorial 1, the two pieces of this cohort's coursework. Its recurring
   items are the battery-lifetime cdf (2024 Q3(b) = 2025 Q3(a)) and the Beta-parameter fit lifted
   verbatim from ·CRV p16 (Q5(a) on both finals, with **V3** inside it).
2. **`01` and `04` are the only files on all five papers.**
   - `01` is the Gamma/Beta read-off (§5.4–5.5) every time. Beyond Assignment 1 it also brings
     *show-that* proofs: the Beta reduction formula (2025 Q3(b) = Tutorial 1 Q6(a)) and the duplication
     formula (both finals' Q5(b)(ii), which is a gap item).
   - `04`: **expand by Maclaurin, then integrate term by term** is the only question type on every one
     of the five papers. It appears as Assignment 1 Q4 ($\cos2\theta/\theta^{1/3}$), CAT Q4 = Tutorial 1
     Q5 ($\sqrt x\,\ln(x+1)$), and Q2(a) on both finals ($e^{2x}\sin3x$). Both finals also set the same
     Maclaurin limit (2024 Q1(g) = 2025 Q1(f)).
3. **`03` is on both finals, 15 marks each, and on Tutorial 1.** It has never been on the CAT or on
   Assignment 1. Its fixed item is the resonant-frequency percentage error, Q2(c) on both finals, which is
   ·BIN p8 Exercise 1 verbatim.
4. **`05` and `06` have each appeared once, and both times inside the compulsory Question One.** Leibniz
   was 2024 Q1(e), 4 marks, almost verbatim ·LEI p8–9 Example 2. Bessel was 2025 Q1(a), 5 marks: the
   series for $J_n$ and its limit at the origin. Each carries few marks overall, but neither could be
   avoided on the paper where it appeared.

#### Assignment 1 on its own: one paper's evidence

These observations were drawn from Assignment 1 alone, and they still hold *for that paper*. It is the
outlier among the five, not the template.

- **Four of its five questions are the same skill in different clothing:** recognise an integral's
  shape and read the Gamma or Beta parameters off it (`01` §5.4 and §5.5). None asks for a definition,
  a property or a derivation. The later papers do (item 2 above).
- **Q4 is the exception.** It expands $\cos2\theta$ by Maclaurin and integrates $\theta^{2k-1/3}$ term
  by term, with no Gamma or Beta function in it. It turned out to be the most durable question type in
  the subject (item 2).
- **Two of its five integrals are improper:** Q3(b) is singular at $x = 3$ and Q4 at $\theta = 0$. Neither
  question says so. The Beta and Gamma definitions absorb both without special treatment, because all
  they require is $m, n > 0$. Saying so explicitly is a free mark. The CAT's Q4 (= Tutorial 1 Q5) has a
  related trap at its lower limit: $\sqrt x\,\ln(x+1)$ has no Maclaurin series at the origin (**P10**).
- **Q1 and Q3 both hinge on choosing the right substitution**, and both times the paper supplies it.
  When it does not, look for the substitution that makes an unwanted term cancel (Q1) or maps the
  interval onto $[0,1]$ (Q3).
- **Do not carry its "it is all Gamma and Beta" reading into revision for a final.** On the three sat
  papers, `01` supplies 27 of 204 printed marks.

### Where a future paper would most plausibly go

- **A final will most likely look like the last two.** 70 of the 2025 final's 90 printed marks were
  2024 questions, reprinted word for word. Questions Two and Five were reprinted whole, and all four new
  questions went into Question One. Work the 2024 final, then the 2025 final's four new questions:
  Q1(a), Q1(c), Q1(d) and Q3(b).
- **Expect the power-series ODE again.** It is on every paper a cohort has sat, with identical wording
  each time, and this knowledge base cannot teach it (gap table above).
- **Expect expand-then-integrate.** It is the only question type on all five papers.
- **Question One is where new material goes, and that is where `05`, `06` and Legendre have appeared.**
  `06` is the course's technical peak, with six recurrence proofs across five pages. So far only its
  series definition has been examined (2025 Q1(a)). **The recurrence proofs have never been set.** A
  file examined once is not a file examined lightly.
- **Tutorial 1 is this cohort's own sheet**, and half of it has been examined before (see the next
  section). Treat its three new questions as exam material too: Q1 and Q2 (`03`), and Q3 (`01`,
  including the negative-argument $\Gamma(-3/2)$).

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
lecturer can change a paper at any time. But on this evidence, a student who works the 2024 final until it
is automatic has already seen most of the next one.

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
| `01-gamma-and-beta-functions` | Assignment 1 Q1, Q2, Q3(a), Q3(b), Q5 · CAT Q2 · 2024 Q1(f), Q5(b)(i) · 2025 Q1(e), Q3(b), Q5(b)(i) · **Tutorial 1 Q3 (all four items), Q6(a)–(b)** |
| `02-crv-and-beta-distribution` | CAT Q1 · 2024 Q1(c), Q3(a), Q3(b), Q5(a) · 2025 Q1(c), Q3(a), Q5(a) — **the heaviest section in the unit** |
| `03-binomial-theorem` | 2024 Q1(a), Q1(b), Q2(c) · 2025 Q1(b), Q2(c), Q4(a) · **Tutorial 1 Q1, Q2** |
| `04-maclaurin-theorem` | Assignment 1 Q4 · CAT Q4 · 2024 Q1(g), Q2(a) · 2025 Q1(f), Q2(a) · **Tutorial 1 Q5** |
| `05-leibniz-theorem` | 2024 Q1(e) — **once** |
| `06-bessels-equation` | 2025 Q1(a) — **once** |
| ❌ **not in the KB** | CAT Q3 · 2024 Q1(d), Q2(b), Q4, Q5(b)(ii) · 2025 Q1(d), Q2(b), Q4(b), Q5(b)(ii) · **Tutorial 1 Q4** (small changes / total differentials — in none of the six topic files, and now examined three times) |

**Gap totals: 27 of 90 on the 2024 final, 24 of 90 on the 2025 final, 7 of 24 on the CAT, 4 of 26 on
Tutorial 1.** Frobenius is already a documented gap; **Legendre polynomials and the Gamma duplication
formula appear nowhere in the knowledge base** and should be added to the gap map.

**Two questions run the other way — they are lifted verbatim from the lecture notes.** Q2(c) is ·BIN p8
Example 1 and Q5(a) is ·CRV p16 Example 1, on both finals. ⚠ The knowledge base already flags **V3** inside
the latter, so check the correction before teaching it.

## ⚠ Four defects worth knowing before revising

- **P4 ★** 2024 Q1(c) is a *show-that* for a variance of $1/(18a^2)$. It is $a^2/18$ — confirmed
  symbolically. The printed target cannot be shown.
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
