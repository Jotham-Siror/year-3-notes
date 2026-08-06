---
kb: "MEC 3104 Fluid Theory"
file_role: past-papers-index
purpose: "Register of every CAT / exam / assignment paper transcribed into this KB, plus the house format for adding the next one."
papers: 2
total_questions: 14
unit_codes: ["MEC 3104", "SCE 3104"]
unit_code_note: "the same course has been examined under both codes — SCE 3104 for the 2024 cohort (School of Computing and Engineering Sciences), MEC 3104 for 2025. Treat papers under either code as the same syllabus."
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

Errata IDs are allocated across the whole folder, not per paper: **P1–P6** belong to the 2025 CAT, **P7–P13** to
the 2024 CAT. The next paper starts at P14.

## Topic coverage so far

| KB section | Questions that have appeared |
|---|---|
| `02-history` | 2024 Q1a (hydraulics vs hydrodynamics), Q1b (which came first) |
| `03-fluid-properties` | 2025 Q1 (dimensional homogeneity), Q4 (compressibility / bulk modulus) |
| `04-fluid-statics` | 2025 Q2 (buoyancy derivation), Q3 (floating body), Q4 (manometer, metacentre, relative equilibrium), Q5 (force + centre of pressure on an inclined gate) · 2024 Q1c (inclined manometer), Q1d (three characteristics of pressure) |
| `05-flow-fundamentals` | 2025 Q6 (streamlines, Lagrangian), Q7 (Re symbols), Q8a, Q9 (vorticity), Q10 (flow rate) · 2024 Q1c (steady flow, continuity, vortices), Q1e (define streamline), Q2a |
| `06-energy-bernoulli` | 2025 Q4 (Bernoulli → headloss) · 2024 Q3a (derive Bernoulli from Euler), Q3b (Venturi), Q4b (weir) |
| `07-momentum` | 2024 Q4a (jet pump) |
| `08-viscous-flow` | 2025 Q8 (Re, laminar/turbulent) · 2024 Q2 (Re from ν and Q) |
| `10-open-channel-flow` | 2024 Q4b (weir discharge by integration) |
| `11-drag-and-lift` | 2025 Q4 (Stokes) · 2024 Q1c (constant descending velocity → terminal velocity) |

**Not yet examined in either paper: `09-pipe-flow` — and here is what that section actually is.**

In plain terms, pipe flow is *what it costs to push a fluid through a pipe*. Real pipes rub on the fluid, so
pressure is lost along the way, and more is lost at every bend, valve, sudden widening or narrowing. The
section teaches you to calculate that loss and size the pump needed to overcome it. Its three tools are the
**Darcy–Weisbach equation** (head lost to friction, h_f = λ·(l/d)·v²/2g), the **Moody chart** (which gives the
friction factor λ from the Reynolds number and how rough the pipe is), and **minor-loss coefficients** (a K or
ζ value for each fitting). Slides 387–478.

Two reasons this gap matters. First, it is the **largest section in the course** — 92 slides, more than any
other. Second, it is the most practically useful: sizing a pump and predicting a pressure drop is the everyday
job of a mechanical engineer working with fluids. So it is heavily taught and, so far, untested.

Say this plainly rather than as a prediction: two papers is a small sample, not a pattern. But a large,
heavily-weighted section that has not yet been examined is exactly the kind of thing that turns up next.

**What the two papers weight differently:** 2025 is statics-heavy (buoyancy, centre of pressure, metacentre);
2024 is energy/momentum-heavy (Euler → Bernoulli, Venturi, jet pump, weir). Both open with definitions and a
matching question, and both carry a Reynolds-number calculation — those three are the safest bets.

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

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
