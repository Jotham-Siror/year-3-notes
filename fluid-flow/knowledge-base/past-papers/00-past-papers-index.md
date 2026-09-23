---
kb: "MEC 3104 Fluid Theory"
file_role: past-papers-index
purpose: "Register of every CAT / exam / assignment paper transcribed into this KB, plus the house format for adding the next one."
papers: 5
total_questions: 25
total_parts: 78
unit_codes: ["MEC 3104", "SCE 3104"]
unit_code_note: "the same course has been examined under both codes — SCE 3104 for the 2024 cohort CAT 1, MEC 3104 for the 2024 CAT 2 and for 2025. Treat papers under either code as the same syllabus. ⚠ AND: the 2024 THERMODYNAMICS papers are ALSO printed MEC 3104 (see ../../../thermodynamics/knowledge-base/past-papers/). One code, two different units, same academic year. Match a paper by unit NAME, never by code alone."
status_legend: "unsolved = questions only · partial = some model solutions worked & verified · solved = all verified"
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base — past papers. -->

# Past Papers — index

> **Read me first.** This folder holds the actual assessment papers, transcribed verbatim
> and machine-readable. Use it to quiz him, to set timed mocks, or to work a question with him. Open the paper
> file below; each one is self-contained and tells you what it maps to in the main KB.
>
> **Two rules that matter:**
> 1. `[q]` text is the paper's exact wording — quote it as printed. Where the paper is *wrong*, it stays wrong in
>    the `[q]` block and carries a `⚠ VERIFY` marker; the correction lives in `../_verification-log.md`
>    (§ Exam papers). Teach the correct form, and tell him the paper is wrong — never silently fix it.
> 2. Every figure is stored **twice**: a `figure_data:` YAML block inside the paper file (the authoritative
>    geometry, in words and numbers) and a rendered SVG in `figures/`. Reason from the block; show him the SVG.

## Register

| Paper | Date | Marks | Qs | Status | File |
|---|---|---|---|---|---|
| MEC 3104 **CAT 1** | 19 Aug 2025 | 40 | 10 | `unsolved` | [`MEC3104-CAT1-2025-08-19.md`](MEC3104-CAT1-2025-08-19.md) |
| SCE 3104 **CAT 1** | 14 Aug 2024 | 40 | 4 (11 parts) | `unsolved` | [`SCE3104-CAT1-2024-08-14.md`](SCE3104-CAT1-2024-08-14.md) |
| MEC 3104 **CAT 2** | 9 Oct 2024 | 40 ✓ | 3 (10 parts) | `unsolved` | [`MEC3104-CAT2-2024-10-09.md`](MEC3104-CAT2-2024-10-09.md) |
| MEC 3104 **CAT 2** | 7 Oct 2025 | 40 ✓ | 3 (15 parts) | `unsolved` | [`MEC3104-CAT2-2025-10-07.md`](MEC3104-CAT2-2025-10-07.md) |
| MEC 3104 **End of Semester** | 29 Oct 2025 | 90 printed / 60 sat | 5 (32 parts) | `unsolved` | [`MEC3104-EXAM-2025-10-29.md`](MEC3104-EXAM-2025-10-29.md) |

Errata IDs are allocated across the whole folder, not per paper: **P1–P6** and **P14–P15** belong to the 2025
CAT 1, **P7–P13** to the 2024 CAT 1, **P16–P22** to the 2024 CAT 2, **P23–P29** to the 2025 CAT 2, **P30–P42**
to the 2025 end-of-semester paper. The next paper starts at **P43**.

## Topic coverage so far

| KB section | Questions that have appeared |
|---|---|
| `02-history` | 2024 Q1a (hydraulics vs hydrodynamics), Q1b (which came first) |
| `03-fluid-properties` | 2025 CAT 1 Q1 (dimensional homogeneity), Q4 (compressibility / bulk modulus) · **2025 exam Q1(a), Q1(b)** |
| `04-fluid-statics` | 2025 CAT 1 Q2, Q3, Q4, Q5 · 2024 CAT 1 Q1c, Q1d · **2025 exam Q1(c), Q1(d), Q1(g)** (metacentric height on an 18 × 32 ft pontoon) |
| ❌ **absent from the KB** | **2025 CAT 2 Q2(5)** — "the wall effect", 2 marks. Zero hits across all eleven topic files, the formula sheet and the nomenclature |
| `05-flow-fundamentals` | 2025 Q6 (streamlines, Lagrangian), Q7 (Re symbols), Q8a, Q9 (vorticity), Q10 (flow rate) · 2024 CAT 1 Q1c (steady flow, continuity, vortices), Q1e (define streamline), Q2a · **2024 CAT 2 Q1a** (matching six scientists to their fields) · **2025 CAT 2 Q1(3)(b)(i)** · **2025 exam Q1(e), Q1(f), Q2(b), Q2(d), Q3(a), Q5(d)(i)** |
| `06-energy-bernoulli` | 2025 Q4 (Bernoulli → headloss) · 2024 CAT 1 Q3a (derive Bernoulli from Euler), Q3b (Venturi), Q4b (weir) · **2024 CAT 2 Q1b** (Pitot tube) · **2025 CAT 2 Q1(1), Q3(1)** · **2025 exam Q1(h), Q4(a)–(d)** (Pitot again, and Bernoulli with a head-loss reservoir) |
| `07-momentum` | 2024 CAT 1 Q4a (jet pump) · **2025 exam Q2(c)** (the jet pump returns — same figure, subtraction reversed) |
| `08-viscous-flow` | 2025 Q8 (Re, laminar/turbulent) · 2024 CAT 1 Q2 (Re from ν and Q) · **2024 CAT 2 Q2a**, **Q2c(ii)** · **2025 CAT 2 Q1(3)(b)(i)–(ii)** · **2025 exam Q3(b), Q3(c), Q5(d)(ii)** |
| `09-pipe-flow` | **2024 CAT 2 Q2b** (pipe branch vs junction), **Q2c(i)** (symbols of Darcy–Weisbach and Hagen–Poiseuille), **Q2c(ii)** (laminar friction factor), **Q2c(iii)** (head loss, 2 km of 200 mm wrought iron at 60 L/s) · **2025 CAT 2 Q1(2), Q1(3)(a), Q1(3)(b)(iii)** · **2025 exam Q2(a), Q5(d)(iii)** |
| `10-open-channel-flow` | 2024 CAT 1 Q4b (weir discharge by integration) · **2024 CAT 2 Q3a** (Manning) · **2025 CAT 2 Q2 — the whole question** (hydraulic jump, subcritical flow, specific energy) · **2025 exam Q4(a), Q4(c), Q5(a)–(c)** |
| `11-drag-and-lift` | 2025 Q4 (Stokes) · 2024 CAT 1 Q1c (constant descending velocity → terminal velocity) · **2024 CAT 2 Q3b** (flat-plate drag) · **2025 CAT 2 Q3** (the whole question) |

**The `09-pipe-flow` gap is closed, and it stayed closed.**

For two papers `09-pipe-flow` was the one large section nobody had tested: 92 slides, the biggest in the
course, and untouched by either CAT 1. The **2024 CAT 2** examined it end to end (14 of 40 marks). The
**2025 CAT 2** did it again — 9 of 40 — and the 2025 exam adds 6 more. Worth saying to him plainly: this was
predicted here before it happened, and it has now happened three papers running. **Pipe flow is CAT 2
territory** specifically: it takes 9 of the 2025 CAT 2's 40 marks but only 6 of the exam's 90.

**What the five papers weight differently:**

| Paper | Centre of gravity |
|---|---|
| 2025 CAT 1 | **statics** — buoyancy, centre of pressure, metacentre |
| 2024 CAT 1 | **energy and momentum** — Euler → Bernoulli, Venturi, jet pump, weir |
| 2024 CAT 2 | **pipe flow and applied substitution** — every numerical part hands him the formula |
| 2025 CAT 2 | **open-channel flow** — the whole of Question Two: hydraulic jump, subcritical flow, specific energy |
| 2025 exam | **broad** — the only paper that reaches all nine topic files, and the only one that opens on `03-fluid-properties` |

**CAT 2 is not a smaller CAT 1.** Both CAT 1s are broad and definition-led. Both CAT 2s are narrow and
heavy: three questions, every numerical part supplied with its formula, and a centre of gravity in the back
half of the course (pipe flow, open channels, drag). If he is revising for a CAT 2 specifically, drill
formula-substitution and the last three topic files, not definitions.

---

## ⚠ Recurrence across the five papers

This is the most useful section in the file. Everything below is a repeat, not a resemblance.

| What repeats | Where |
|---|---|
| **"Define the term: Weir" *(2 marks)*, word for word** | 2025 CAT 2 Q1(1) **and** 2025 exam Q4(a) — **22 days apart** |
| **The jet pump** — same pasted figure, same formula | 2024 CAT 1 Q4(a) → 2025 exam Q2(c), but with the subtraction **reversed** (P33) |
| **The Pitot tube** | 2024 CAT 2 Q1(b) → 2025 exam Q1(h) — and the 2025 printing **repairs both** of the 2024 defects (P16, P17) |
| **The weir discharge coefficient** | P11's imperial `C = 3.2` reappears as `C = 1.69`, its exact SI twin — same weir, same mistake, two unit systems |
| **"Distinguish two pipe fittings" *(3 marks)*** | third paper running |

Two papers is a small sample; five is a pattern worth acting on. **A definitions-or-matching opener, a
Reynolds-number calculation, and the weir turn up in nearly every paper.** Those three are the safest bets
he has.

---

## ⚠ Check the arithmetic and the units before setting any of these

Four of the five papers reconcile. The **2025 end-of-semester paper does not**: Questions One to Four sum
exactly to their printed headings (30/15/15/15), but **Question Five prints no allocation at all** and no
grand total appears anywhere. Its parts sum to 15 by inference only.

**And the unit slips are systematic.** The 2024 CAT 2 mixes inches, feet and SI inside forty marks. The 2025
CAT 2 prints "Take **f = 0.00026 m**" — that is the absolute *roughness* of new cast iron, not a friction
factor, and a friction factor cannot carry metres; taking it literally makes the head loss **88× too small**
(P24, computed here). The 2025 exam prints `I₀ = b(L)³/12` with neither symbol defined and no heel axis
stated, which on the question's own dimensions gives a metacentric height **14× out** (P30). Both are the
most serious defect on their paper, and both are the kind a student cannot catch without knowing the physics
first.

**Twenty of the folder's forty-two errata belong to the two 2025 papers.** Check every paper's arithmetic
and every supplied constant before setting it as a timed mock.

---

# House format — adding the next paper

Follow this exactly so every paper is picked up the same way by a future chat.

### 1 · Naming
- Paper file: `<UNIT>-<TYPE>-<YYYY-MM-DD>.md` — e.g. `MEC3104-CAT2-2025-10-14.md`.
- Figures: `figures/<same-stem>-q<N>.svg` — e.g. `MEC3104-CAT2-2025-10-14-q5.svg`. Where one question has more
  than one figure, suffix the subject too: `-q3-euler.svg`, `-q3b-venturi.svg`.
- Add a row to the **Register** table above and update the **Topic coverage** table.

### 2 · Frontmatter (required keys)
`kb, file_role: past-paper, paper_id, paper, institution, date, time, duration_min, rubric, questions,
total_marks, marks_reconcile, status, source, transcription, figures, figure_dir, errata_logged, kb_sections, tags`

`marks_reconcile: true` only after the printed part-marks have been **added up and checked against the stated
total**. That single arithmetic check is the cheapest way to catch a question lost off the edge of a photo.

### 3 · Transcription rules
- Verbatim in `[q]` blocks, including the paper's own typos and odd units.
- Maths in LaTeX (`$...$` inline, `$$...$$` display) — matches the main KB topic files.
- **Never reconstruct unreadable text or figures.** If a photo can't be read, stop and ask him to re-shoot that
  specific item; record `legibility: illegible` and what is missing. Nothing is guessed into this KB.
- Give every question a `→ KB section` mapping and its marks in the heading.
- Note any photo artefact that could be mistaken for exam content (a sheet visible underneath, his own pencil
  working, a stock-image watermark) so a future chat doesn't try to interpret it.

### 4 · Figures — the two-layer rule
Each figure gets **both**:

- a `figure_data:` YAML block in the paper file — every labelled dimension, angle, fluid property and point label,
  plus a `derived_not_printed:` sub-block for anything computed (clearly separated from what the paper states),
  a `legibility:` flag, and an `ambiguity:` list where the drawing is genuinely unclear;
- a **self-contained SVG** in `figures/`, drawn to true scale from those numbers, with `<title>` and `<desc>`
  filled in so the file is intelligible even without the markdown.

SVG house style (keep new figures consistent): Georgia/serif; `#dbe8f2` fluid fill; `#1a1a1a` walls at 2.6 px;
grey dimension lines with double arrowheads and dashed extension lines; `#1a4a72` for fluid labels, flow arrows
and the free-surface ▽ symbol; gate/target surface as a black bar with a `#f2c14e` core; forces in `#b3261e`;
short single-letter dimension labels set horizontally, longer ones rotated along the dimension line; a one-line
grey caption along the bottom naming the paper and question. Schematic figures (not drawn to scale) say so in
the caption; scale drawings say "Redrawn to scale".

### 5 · Errata
Anything wrong with the paper goes in `../_verification-log.md` under **§ Exam papers**, with an ID (`P1`, `P2`, …)
allocated continuously across the whole folder, and is referenced from the question by a `⚠ VERIFY` marker. Per
explicit instruction, the full entry lives **only** in the verification log — the paper file just points to it.

### 6 · Solutions
Paper files are a **question bank**: `status: unsolved` by default, no answers written in. If he later wants worked
solutions, put them in a **separate** `<paper_id>-solutions.md` and flip `status:` — so the questions stay usable
as clean practice.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
