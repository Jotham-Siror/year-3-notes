# Thermodynamics — MEC 3105

Verified notes for MEC 3105, BSc Electrical Engineering Year 3 Semester 1, Strathmore University.

**Everything the five lecture documents contain — 200 pages — transcribed, recomputed and
cross-checked**, plus both assessed group activities with **every question worked and verified**. Every
equation in LaTeX, every claim anchored to the page or slide it came from, every figure described, and
**51 suspected errors flagged with the corrected form**.

These are **unofficial student notes**. Nobody has endorsed or reviewed them. Read
*[Before you rely on this](#before-you-rely-on-this)* at the bottom.

---

## Start here

| If you want to… | Open |
|---|---|
| **See what's covered and where** | [`knowledge-base/00-index.md`](knowledge-base/00-index.md) |
| **Revise a topic** | the numbered file for it, below |
| **Check a formula before an exam** | [`knowledge-base/_formula-sheet.md`](knowledge-base/_formula-sheet.md) |
| **Know what the slides get wrong** | [`knowledge-base/_verification-log.md`](knowledge-base/_verification-log.md) — the highest-value file here |
| **Work out which $T_C$ a slide means** | [`knowledge-base/_nomenclature.md`](knowledge-base/_nomenclature.md) |
| **Find a group-activity question — or its solution** | [`knowledge-base/exercises/`](knowledge-base/exercises/00-exercises-index.md) |

## The topic files

| File | Source | Covers |
|---|---|---|
| [`01-temperature-thermometry.md`](knowledge-base/01-temperature-thermometry.md) | TT, 17 pp. | Temperature as a base quantity, thermal equilibrium, the zeroth law, thermometers, Celsius / Kelvin / Fahrenheit, the constant-volume gas thermometer and absolute zero |
| [`02-first-law.md`](knowledge-base/02-first-law.md) | FL, 37 slides | Heat as energy, the first law built from a piston, sign conventions, energy balance, enthalpy, the four elementary processes, polytropic processes, boundary work, equations of state and $Z$ |
| [`03a-phase-behaviour-and-equilibrium.md`](knowledge-base/03a-phase-behaviour-and-equilibrium.md) | EPC s1–21 | Phases of matter, evaporation, vapour pressure, boiling, liquid nitrogen, the kinds of equilibrium |
| [`03b-second-law-and-cycles.md`](knowledge-base/03b-second-law-and-cycles.md) | EPC s22–92 | Why a second law is needed, reversibility, heat engines, thermal efficiency, Kelvin–Planck and Clausius, refrigerators and COP, the Carnot cycle and principles, the Diesel cycle |
| [`04-thermodynamic-cycles.md`](knowledge-base/04-thermodynamic-cycles.md) | TC, 24 slides | What a cycle is, state points and processes, cycle diagrams, which cycle models which machine, cycle analysis and selection, common mistakes |
| [`05-heat-engines-and-carnot.md`](knowledge-base/05-heat-engines-and-carnot.md) | HE, 30 slides | Heat engines, efficiency equations, engine types, the Carnot cycle in depth, the reversed Carnot cycle, the $T$–$s$ rectangle and the course's only entropy equations |

Topic 1 is **01** + **02**. Topic 2 is **03a** + **03b**. Topic 3 is **04** + **05**.

---

## ⚠ Three things to know before you revise from the slides

**1. The First Law deck states two contradictory sign conventions — and its own worked example
mixes them.** Slide 13 gives the physics convention ($W$ positive done *on* the system,
$\Delta U = Q + W$); slide 30 onward uses the engineering convention ($W$ positive done *by* the
system, $\Delta U = Q - W$). Slide 20's worked example flips a sign partway through and prints
$Q = -505\ \mathrm{J}$ where the correct answer is $-2532\ \mathrm{J}$ — **wrong by a factor of
five**, confirmed independently via $Q = n c_p \Delta T$. Default to $\Delta U = Q - W$.
→ `02-first-law.md` §2.3, §2.6; flag **V8**.

**2. $T_C$ means two different things in two different decks.** In the temperature notes it is the
**Celsius temperature**. In the heat-engine deck it is the **cold-reservoir temperature**, and it
must be in kelvin. Substituting a Celsius value into a Carnot efficiency is the single easiest way
to lose marks in this course. Prefer $T_L$ in your own work. → `_nomenclature.md` clash 11.

**3. Slide numbers in the Topic 3 decks are shifted.** TC slide 2 is a full-bleed image with no text,
so every title sits one slide later than a contents listing implies. All `·TC sN` citations here are
**true PDF page numbers** — count pages in the viewer, not titles.

**4. The group activity's Van der Waals constants are printed in the wrong units.** GA1 gives $a$ as
$\mathrm{J\,m^3\,mol^{-2}}$; the numbers are the standard $\mathrm{L^2\,bar\,mol^{-2}}$ values, so
**divide every printed $a$ by 10**. Substituted as printed, the cubic returns a molar volume barely
above $b$ — a liquid-like volume for a gas at 5 MPa — and $Z = 0.08$ instead of $0.785$. Corrected, all
eight groups' answers agree with published compressibility data, including hydrogen's $Z > 1$.
→ flag **V28**.

There are 47 more flags. `_verification-log.md` has all of them, each with the correct form and the
reasoning.

---

## Three things the course assesses but never teaches

Documented rather than glossed over, because finding them missing during a CAT is worse.

- **The Van der Waals equation** — assessed in GA1, absent from all five decks (the First Law deck
  gives Beattie–Bridgeman, Benedict–Webb–Rubin and virial instead). Supplied here, tagged `[added]`.
- **Efficiency formulae for the Otto, Diesel, Brayton, Rankine and Stirling cycles** — the cycles are
  named and tabulated, but analysed nowhere. Supplied here, tagged `[added]`.
- **The steady-flow energy equation** — referenced by a GA2 discussion prompt, written in no deck.
  Left as a documented gap.

There is also **no general definition of entropy anywhere in the course** — only the Carnot-specific
$Q_H = T_H\,\Delta s$ on HE slide 28. `00-index.md` § Gap map has the full list.

---

## How the files are written

Anything tagged `[added]` is **not in the lecture material** — it was supplied to fill a gap, and is
marked so you always know which is which. `⚠ VERIFY` marks a suspected error in the source, with the
ID resolving in `_verification-log.md`. Citations look like `·TT p7` (page-based document) or
`·EPC s68` (slide decks); `·GA1 G3 Part B (ii)` points into a group activity.

**Every page was read from a rendered image, never from the PDF text layer.** A large share of the
equation slides are pictures, and the text layer silently omits them — one early note read that way
recorded a worked example as "sound" when its final answer is wrong by 5×. The method, and exactly
which pages were read at what resolution, is stated in `_verification-log.md` § Method.

The full format specification is [`../docs/kb-format.md`](../docs/kb-format.md).

## Using it with Claude

Clone the repository and open it — `CLAUDE.md` at the root loads automatically and tells Claude how to
teach from these files, including which errors to correct silently. Then ask for what you want:
*"tutor me through the Carnot cycle"*, *"quiz me on sign conventions"*, *"work GA2 Task 3 with me"*.

It reads perfectly well without Claude too. It is just Markdown.

## The source PDFs are not here

Lecture decks and group-activity sheets are the lecturer's material, not ours, so this repository
carries only what we wrote. [`sources/SOURCES.md`](sources/SOURCES.md) lists exactly which files
belong there, under what names, and where the citations resolve. **The notes are self-contained** —
you need the originals only to check a citation against the original page.

The group-activity sheets additionally carry the names of every student in each group. They are
untracked, and the transcriptions here refer to **groups by number only**.

---

## Before you rely on this

- **Don't submit any of it as your own work.** Your institution's rules on collaboration and
  plagiarism apply to you, whatever you found here.
- **Don't treat a correction as authoritative.** The verification log records errors believed to
  exist in the teaching material. That analysis is careful, recomputed and cross-checked — but it is
  one student's. Where a mark depends on it, confirm against a standard textbook or ask the lecturer.
  One flag in this log was raised, investigated and **withdrawn** as a false alarm; the withdrawal is
  recorded rather than deleted, which is the standard the rest is held to.
- **Check before an assessment.** Course content changes between cohorts. This reflects the material
  as issued in 2026.

Found an error *in these notes*? That is the most useful possible contribution — open an issue.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026 · <a href="../LICENSE">CC BY-NC-SA 4.0</a></i></sub>
