---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "Exercises — index"
file_role: index
covers: "GA1 (Topic 1 Part 1) and GA2 (Topic 1 Part 2)"
solutions: "worked and verified in both files, § Solutions. All tagged [added]."
verification_flags: 1
tags: [exercises, index, group-activity]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Exercises — index

The two assessed **group discussion activities** — every question transcribed, every one **worked and
verified**, each cross-linked into the topic file that carries the theory.

| File | Activity | Covers | Groups | Maps to | Flags |
|---|---|---|---|---|---|
| [`ga1-topic1-part1-equations-of-state.md`](ga1-topic1-part1-equations-of-state.md) | **GA1** — Topic 1 Part 1 | 1.1 Temperature and thermometry · 1.2 Equations of state (ideal gas, Van der Waals, $Z$) | 8 | **01**, **02** §2.12 | ⚠ **V28** |
| [`ga2-topic1-part2-first-law.md`](ga2-topic1-part2-first-law.md) | **GA2** — Topic 1 Part 2 | 1.3 Work, heat and the first law | 9 | **02**, **03b** | clean |

---

## What is in these files, and what is not

**In:** every question as set, the per-group data tables, the session structure, a cross-link from each
question to the section of the knowledge base that answers it, and a **§ Solutions** section in each
file working every numerical part and giving answer points for the discussion parts. Plus the traps
worth knowing before you start — **V28**, the sign convention, and the mixed scenario shapes in GA2's
Task 1.

**How the solutions are placed.** At the **end** of each file, not under each question, so you can
attempt a task before seeing the answer. Every one is tagged `[added]`.

**Not in — deliberately:**

1. **No facilitator answer key.** GA1's master brief carries a section headed **"FACILITATOR /
   LECTURER NOTES (Not distributed to students)"** with model answers for all eight groups. It is
   marked not for distribution and is **not reproduced, quoted or paraphrased** anywhere in this
   knowledge base — not a number, not a phrase. **The solutions here are our own working**, computed
   from scratch and shown with their method so you can check them rather than trust them. GA2 has no
   such section in any of its nine files.
2. **No student names, ever.** The raw submission files carry group member lists and document
   metadata. Groups are identified **by number only** throughout. See `00-index.md` § *Why exercises
   are a separate folder*.

---

## Why exercises live in their own folder

The topic files **01**–**05** are a transcription of the lecture documents, verified line by line
against rendered pages. The group activities are a **different kind of source**: they were written for
a 55-minute session, they introduce two topics (Van der Waals, the SFEE) that appear in no lecture
deck, and their numbers are not the lecturer's worked examples. Interleaving them would blur the line
between *what the course taught* and *what the course asked you to do with it*.

They are cross-linked in both directions instead — each question points at its section, and each topic
file's *Cross-references* block points back here.

---

## What GA1 and GA2 assess that no lecture deck teaches

Three items, all tracked in `00-index.md` § **Gap map**:

| Item | Activity | Where it is supplied |
|---|---|---|
| **Van der Waals equation**, constants $a$, $b$ | GA1 Part B (ii), all 8 groups | `[added]` in **02 §2.12** and `_formula-sheet.md` § *[added] Van der Waals*. FL s37 gives Beattie–Bridgeman, Benedict–Webb–Rubin and virial instead. ⚠ **GA1 prints $a$ in the wrong units — V28.** |
| **Steady-flow energy equation (SFEE)** | GA2 Part A Q3 | ❌ **still not supplied.** FL covers enthalpy but never writes a flow-device balance. `_nomenclature.md` marks $h_1$, $h_2$ as GA2-only. |
| **Seebeck effect** / thermoelectric measurement | GA1 Part B, G1 (b) | ❌ not supplied — outside the lecture syllabus. TT's list of six exploited properties (**01 §1.4**) does not include thermoelectric emf. |

*Partial, and both also in the gap map:* the **Rankine temperature scale** (GA1, four groups) —
**01 §1.6–§1.7** covers Celsius, Kelvin and Fahrenheit only, and Rankine is named just once in the
whole course, inside the ·HE s26 quotation at **05 §5.3**, with **no conversion given anywhere**; the
brief supplies $T(^\circ\mathrm{R}) = 1.8\,T(\mathrm{K})$ in its own hint line. And the **Rankine
cycle** (GA2 Part A Q2) is named in **05 §5.4** and **04 §4.5** but no deck gives its efficiency
formula — a course-wide gap covering Otto, Diesel, Brayton and Stirling too, filled `[added]` on
`_formula-sheet.md`.

---

## Three things to read before either activity

**GA1 — ⚠ V28, the Van der Waals units.** The brief prints $a$ as $\mathrm{J\,m^3\,mol^{-2}}$; the
values are actually $\mathrm{L^2\,bar\,mol^{-2}}$. **Divide every printed $a$ by 10.** Read literally,
the cubic returns a liquid-like molar volume and $Z \approx 0.08$ for a gas at 5 MPa. Full entry in
`../_verification-log.md`; flag box in the GA1 file above the data table.

**GA1 — the $T_C$ clash.** In **TT** (and **01**), $T_C$ is the **Celsius temperature**. In **HE**
(and **05**), $T_C$ is the **cold-reservoir temperature**. GA1 uses the TT sense.
→ `_nomenclature.md` **clash 11**.

**GA2 — the sign convention.** GA2 states $\Delta U = Q - W$ with $W$ positive **done by** the system.
The FL deck states **two conflicting conventions** (s13 vs s30); GA2 agrees with FL's second half, and
so does this knowledge base. → **02 §2.3**; `_nomenclature.md` **clash 1**.

---

### Cross-references

- Register of every source document and its coverage → `../00-index.md`.
- All equations in corrected form → `../_formula-sheet.md`.
- Symbol table and the 14 clashes → `../_nomenclature.md`.
- Every flagged error in the lecture material → `../_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
