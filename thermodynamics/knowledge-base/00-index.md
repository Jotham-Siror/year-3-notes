---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
programme: "BSc Electrical Engineering, Year 3 Semester 1"
lecturer: "withheld"
file_role: index
source: "5 lecture documents (200 pp.) + 2 sets of assessed group activities. See ../sources/SOURCES.md"
built: "COMPLETE — all five lecture documents plus both group activities."
coverage: "200 / 200 lecture pages transcribed and verified. GA1 (8 groups) and GA2 (9 groups) transcribed and solved."
total_verification_flags: 51
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Thermodynamics (MEC 3105) — Knowledge Base Index

> ## ✅ Build status — complete
>
> **Every one of the 200 lecture pages is transcribed and verified.** Both assessed group activities
> are in `exercises/` — **every question transcribed, every one worked and verified**, each
> cross-linked to the section that carries its theory. Study from `01-` … `05-` freely.
>
> ### ⚠ Three things to know before teaching from any of it
>
> 1. **FL states two contradictory sign conventions for $W$** and its only worked example mixes them,
>    giving an answer **wrong by a factor of five** (V8). Default to $\Delta U = Q - W$.
>    See `_nomenclature.md` clash 1.
> 2. **$T_C$ means Celsius temperature in TT but cold-reservoir temperature in HE** — and HE's must be
>    in kelvin. `_nomenclature.md` clash 11. **Prefer $T_L$ in your own work.**
> 3. **`03b` holds all nine worked numerical examples in the course, and every one is correct.** TC and
>    HE contain no arithmetic at all.

**What this will be.** A verified map of the five MEC 3105 lecture documents — every claim anchored
to its source page, every suspected error flagged and corrected — plus the assessed group activities,
transcribed and solved, kept in a separate folder.

> **Operating instructions** (how to navigate and teach from this KB) live in `CLAUDE.md` at the
> project root, not in this file.

---

## Course framing — read this first

MEC 3105 is delivered as an **Electrical Engineering** unit. Every applied scenario in the group
activities is electrical: thermocouples in 33 kV transformer oil-cooling circuits, RTDs in generator
stator windings, SF₆ in GIS switchgear, generator hydrogen cooling.

**Teach the applications the way the course sets them.** The physics is standard, but a worked
example about a transformer cooling load is what the assessment will look like — not one about a
piston engine.

## Document register

| Code | Document | Pages | Topic | Topic file | Status |
|---|---|---|---|---|---|
| **TT** | Temperature and Thermometry | 17 | 1 — §1.1 | `01-temperature-thermometry.md` | ✅ **verified — 4 V, 2 C** |
| **FL** | First Law of Thermodynamics | 37 | 1 — **§1.2 + §1.3** | `02-first-law.md` | ✅ **verified — 5 V, 5 C** |
| **EPC** | Energy Equations and Phase Changes | 92 | 2 | `03a-…` **+** `03b-…` *(split)* | ✅ **verified — 8 V, 8 C** |
| **TC** | Power Production and Thermodynamic Cycles (1) | 24 | 3 | `04-thermodynamic-cycles.md` | ✅ **verified — 5 V, 7 C** |
| **HE** | Power Production and Thermodynamic Cycles (2) | 30 | 3 | `05-heat-engines-and-carnot.md` | ✅ **verified — 4 V, 2 C** |
| **GA1** | Group Activities 1 — 8 groups | — | 1 — §1.1, §1.2 | `exercises/ga1-…md` | ✅ **solved — 1 V (V28)** |
| **GA2** | Group Activities 2 — 9 groups | — | 1 — §1.3 | `exercises/ga2-…md` | ✅ **solved — clean** |

Provenance: **·TT p7** (page-based) · **·EPC s68** (slide-based) · **·GA1 G3 Part B Q2** (exercises).
Full detail in `../sources/SOURCES.md`.

> **⚠ TC slide numbers are shifted by an untitled image slide.** TC slide 2 is a full-bleed image with
> **no text layer**, so every title sits one slide later than a text-based contents listing implies. All
> `·TC sN` citations are **true PDF page numbers**. This also corrects `../sources/SOURCES.md`, which
> wrongly lists TC and HE as having no image-only pages — TC has one (s2), HE has three (s2, s16, s18).

> **⚠ TT page numbers are the document's own printed footer numbers**, which run **2 → 18** across its
> 17 pages — the footer starts at 2 on the title page. A PDF viewer therefore shows **one less** than
> the citation: `·TT p13` is the page whose footer reads 13, i.e. **PDF page 12**. Check the footer,
> not the viewer, when resolving a TT citation.

## The lecturer's syllabus map

Recovered from the group-activity headers, which carry section numbers the decks do not.

| Topic | Sections | Documents |
|---|---|---|
| **Topic 1** | 1.1 Temperature & Thermometry · 1.2 Equations of State · 1.3 Work, Heat & First Law | TT, FL + **GA1, GA2** |
| **Topic 2** | Energy Equations & Phase Changes *(EPC's own title page)* | EPC |
| **Topic 3** | Power Production & Thermodynamic Cycles | TC, HE |

**GA1 and GA2 are both Topic 1.** GA numbering is not topic numbering.

## File layout

```
knowledge-base/
├── 00-index.md              ← this file
├── 01- … 05-….md            ← lecture documents ONLY
├── _nomenclature.md
├── _formula-sheet.md
├── _verification-log.md
└── exercises/               ← group activities, never interleaved
    ├── 00-exercises-index.md
    ├── ga1-topic1-part1-equations-of-state.md
    └── ga2-topic1-part2-first-law.md
```

### Why exercises are a separate folder

Four rules keep the separation real:

1. Topic files cite **lecture documents only**; exercise files cite **group activities only**.
2. **Every solution we write carries `[added]`** and was computed from scratch. GA1's master brief
   does contain a facilitator answer key marked *"Not distributed to students"*; it is **not
   reproduced, quoted or paraphrased anywhere**, and no number from it appears in this repository.
3. This index cross-links the two, but nothing merges them.
4. **No student names anywhere.** Groups are referred to by number. The raw `.docx` files carry the
   names of every member; they stay untracked in `../sources/`.

### Splitting rule

**One document = one topic file**, per `../../docs/kb-format.md`. Split into `NNa`/`NNb` only where a
document covers two genuinely independent themes *and* exceeds ~25 KB.

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example
(lecturer's numbers) · `[exercise]` unsolved problem set in the source · `[fig]` figure described
from the rendered page · `[added]` supplied here, **not** in the source · `⚠ VERIFY` flagged
suspected error.

---

## ⚠ Overlap map — EPC, TC and HE cover the same ground

The reason this subject needs a reconciliation layer at all. **EPC is the quantitative spine; TC and
HE are a qualitative engineering-practice layer over the same concepts.**

| Concept | EPC | TC | HE | Authoritative |
|---|---|---|---|---|
| Kelvin–Planck & Clausius statements | full, + equivalence proof | — | — | **EPC** (`03b` §3b.5, §3b.7) |
| Heat engine, $Q_H$ / $W$ / $Q_L$ | full | brief | full | **EPC**, HE for framing |
| Thermal efficiency $\eta_{th}=1-Q_L/Q_H$ | full + derivation | stated | stated | **EPC** — all three agree |
| Carnot cycle, four processes | full + piston panels | — | full + **process/entropy table** | **EPC**, **HE's table added** |
| Carnot efficiency $\eta=1-T_L/T_H$ | full + absolute-scale derivation | ❌ never written | formula, **twice**, + unit warnings | **EPC** for *why*, **HE** for the formula and traps |
| COP, $\mathrm{COP}_{HP}=\mathrm{COP}_R+1$ | full, with $T$-forms | $\mathrm{COP}_R$ only | ❌ concept only, no formula | **EPC** (`03b` §3b.6, §3b.10) |
| Irreversibilities | itemised list | factors table | factors table | **EPC** for the list, TC/HE for practice |
| **$P$–$V$ diagram of the Carnot cycle** | s70 — correct *(states renumbered in the lower diagram)* | s9–s11 — reused 3× | s18 — correct | EPC or HE |
| **$T$–$s$ diagram** | — | s11 — ⚠ **isentrope error (V23)** | **s28 — correct rectangle** | ✅ **HE** |
| **Entropy equations** | ❌ none | ❌ none (words only, and wrong — V19) | **$Q=T\Delta s$, s28** | ✅ **HE — the only ones in the course** |
| **$P$–$h$ diagram** | — | **s11 — the only one** | — | ✅ **TC** |
| Otto / Diesel / Brayton / Rankine / Stirling | Diesel described qualitatively | named (s13) | tabulated (s12) | ⚠ **none — no efficiency formula anywhere** |
| Selection workflow, deviations, common mistakes | — | **full (s20–s24)** | analysis checklists | ✅ **TC** |
| Heat-engine & Carnot analysis checklists | — | — | **full (s13–s14, s29–s30)** | ✅ **HE** |
| Quality of energy | **s84 table** | — | — | ✅ **EPC** |
| Phase behaviour, vapour pressure | **s1–s21** | — | — | ✅ **EPC** (`03a`) |
| **Worked numerical examples** | **9 — all correct** | **0** | **0** | ✅ **EPC — the only numbers in the course** |

**The map as built differs from the Stage 0 forecast in three ways worth noting:**

1. EPC has **nine** worked examples, not five.
2. **HE, not EPC, owns the correct diagrams** — EPC's Carnot $P$–$v$ and TC's $T$–$s$ both contain figure
   errors, and HE's are the only ones drawn correctly.
3. **HE, not EPC, owns entropy** — EPC has no entropy equation at all.

**Build order follows from this:** EPC must be written *before* TC and HE, or Carnot gets written
three times and unpicked afterwards.

---

## ⚠ Gap map — FINAL, all five documents checked

| Topic | Assessed in | Final verdict |
|---|---|---|
| **Van der Waals equation, constants $a$, $b$** | GA1 Part B | ❌ **ABSENT FROM ALL FIVE DECKS.** FL s37 gives Beattie-Bridgeman, Benedict-Webb-Rubin and virial instead. Supplied `[added]` in `02-first-law` §2.12 and on the formula sheet. ⚠ **And GA1 prints the constants in the wrong units — see V28.** |
| **Steady-flow energy equation** | GA2 | ❌ **ABSENT FROM ALL FIVE DECKS.** FL covers closed systems only; TC and HE never write it. **Still unsupplied** — it is needed for one GA2 *discussion* prompt (Part A Q3), not for any numerical task, so it was left as a documented gap rather than invented. |
| **Otto / Diesel / Brayton / Rankine / Stirling efficiency** | likely CAT | ❌ **ABSENT FROM ALL FIVE DECKS.** Named in TC s13, tabulated in HE s12, analysed nowhere. Supplied `[added]` on the formula sheet. |
| **Entropy as a property** (general definition, Clausius inequality, $T\,ds$) | — | ⚠ **PARTIAL.** No general definition anywhere. HE s28 gives the **Carnot-specific** $Q_H = T_H\Delta s$, $Q_C = T_C\Delta s$ — the only entropy equations in the course. $dS = \delta Q_{rev}/T$ supplied `[added]`. |
| Compressibility factor $Z$, $Z \gtrless 1$ | GA1 Part B | ✅ **taught in full** — FL s35–s36, with reduced properties and the generalised chart |
| Specific heats, $c_p - c_v = R$ | GA2 Part B | ✅ **taught** — FL s28, molar form via $\gamma$; convert basis for the exercises |
| Enthalpy $h = u + Pv$ | GA2 | ✅ **taught and derived** — FL s21 |
| Property / steam tables | — | ❌ **referenced but never reproduced** (FL s15, s21; EPC s15). Needed to finish FL s21's example. |
| Third law | — | ⚠ appears **once**, on TC's orphan decorative slide 2. Nowhere else. |

**Three hard gaps remain, and all three are assessable.** Van der Waals is *directly* assessed in
GA1 Part B and has been supplied `[added]`. The named-cycle efficiencies are a CAT risk given Topic 3
is entirely about those cycles, and are supplied `[added]` on the formula sheet. The **SFEE is the one
gap left open**: it is asked about in GA2 Part A Q3 only, as a discussion prompt with no numbers
attached, so it is documented rather than filled.

Two further, smaller gaps surfaced when GA1 was extracted, both left documented rather than filled:

- **The Seebeck effect** (GA1 G1 Part B (b)) — TT's list of the six physical properties thermometers
  exploit (**01 §1.4**) does not include thermoelectric emf, so the thermocouple is not derivable from
  anything the course teaches. Outside the lecture syllabus.
- **The Rankine temperature scale** (GA1 Part B, four groups) — TT covers Celsius, Kelvin and
  Fahrenheit only (**01 §1.6–§1.7**). Rankine is *named* once in the whole course, inside the ·HE s26
  quotation at **05 §5.3**, and **no conversion is given anywhere**. The GA1 brief supplies
  $T(^\circ\mathrm{R}) = 1.8\,T(\mathrm{K})$ in its own hint line, which is the only place it appears.

---

## Verification summary

Full detail in `_verification-log.md`.

| Doc | Pages | Substantive `V` | Cosmetic `C` | Status |
|---|---|---|---|---|
| **TT** | 17 | **4** | **2** | ✅ complete |
| **FL** | 37 | **5** | **5** | ✅ complete |
| **EPC** | 92 | **8** | **8** | ✅ complete |
| **TC** | 24 | **5** | **7** | ✅ complete |
| **HE** | 30 | **4** | **2** | ✅ complete |
| **Total (lecture documents)** | **200 / 200** | **26** | **24** | **50 flags** |
| **GA1** — group activity | — | **1** *(V28)* | **0** | ✅ |
| **Grand total** | — | **27** | **24** | **51 flags** |

> **✅ The knowledge base itself has been verified**, not just written — an independent pass re-checked
> every citation, quotation, figure description and number in all seven topic files against the source
> renders. It **withdrew one false flag (V12)**, **found one new defect (V27)**, and corrected five
> figure descriptions. **No number in any topic file was wrong.** Detail in `_verification-log.md`
> § Verification of the knowledge base itself.

**Where the arithmetic stands.** EPC is the **only** document with worked numbers — nine examples, a
five-row efficiency table and several unit conversions, **all correct**. TT's one example has a rounding
fault (V4); **FL's one example is wrong by a factor of five** (V8); TC and HE contain no arithmetic.

### FL's flags at a glance

| ID | Slide | Defect | Correct form |
|---|---|---|---|
| **V5** | s7 | $W = P\Delta V$ for work done **on** the gas | $W = -P\Delta V$ |
| **V6** | s12 | $Q = W + \Delta U$ contradicts s13's stated convention, and s6/s8 | $Q = \Delta U - W$ |
| **V7** | s17 | $Q$ and $W$ swapped vs the slide's own boxes | $E_1 + Q_{1-2} - W_{1-2} = E_2$ |
| **V8** | s20 | worked example gives $Q = -505\ \mathrm{J}$ | $Q = -2532\ \mathrm{J}$ |
| **V9** | s22 | premises in the other convention ($dQ - dW = C_VdT$, $dW = P\,dV$) | $dQ + dW = C_VdT$, $dW = -P\,dV$ |
| **C3** | s15 | $V$ = velocity where the deck elsewhere uses $V$ = volume | — |
| **C4** | s20 | $T_f$ left blank in the example data | $T_f = 240\ \mathrm{K}$ |
| **C5** | s28 | capital I for the digit 1 | $\gamma = 1 + R/C_V$ |
| **C6** | s29 | $\delta$ as polytropic index collides with $\delta Q$, $\delta W$ | — |
| **C7** | s32 | title reads "Moving Boundary Woek" | — |

**V5–V8 are one fault, not four:** FL does not hold a single sign convention. s13 says "work done on
the gas is positive"; s30 says the exact opposite. The example (s20) mixes them inside one calculation
and its answer is one fifth of the correct magnitude — confirmed independently via
$Q = nc_p\Delta T$. Full diagnosis in `_verification-log.md` § The FL sign-convention fault.

### TT's flags at a glance

| ID | Page | Defect | Correct form |
|---|---|---|---|
| **V1** | p13 | absolute zero printed $273.15\ ^\circ\mathrm{C}$ — minus sign absent from the page | $-273.15\ ^\circ\mathrm{C}$ |
| **V2** | p13 | Kelvin zero point printed $273.15\ ^\circ\mathrm{C}$ — same missing minus | $-273.15\ ^\circ\mathrm{C}$ |
| **V3** | p17 | Example 1(b) says "using Equation 2a"; the working correctly uses Equation 1 | Equation 1 |
| **V4** | p17 | $\Delta T = 7\ \mathrm{K}$ — endpoints rounded before subtracting | $\Delta T = 6.7\ \mathrm{K}$ |
| **C1** | p14 | kelvin defined via the triple point — the pre-2019 SI definition | teach as printed |
| **C2** | p12–13 | text says "curves" and describes an extrapolation Figure 5 does not draw | sketch it yourself |

**V4 is the one that matters most.** TT's single worked example is the likeliest thing for a CAT to
lift, and its printed $\Delta T = 7\ \mathrm{K}$ contradicts both TT p14's own "a Celsius degree equals
a kelvin" and the check with Equation 3 that the page itself sets as an exercise. It teaches a method
error — round, then subtract — not just a wrong digit.

**Both minus signs were confirmed at 400 dpi** to rule out text-extraction loss. They are page defects.

TT's **equations are all sound** — Equations 1, 2a, 2b and 3 need no correction. Every substantive flag
concerns the prose or the arithmetic around them.

---

## ⚠ Early observations — NOT YET VERIFIED

Read from the text layer only. Each must be confirmed against a render before it earns a `V`/`C` ID
in `_verification-log.md`. Recorded here so they are not lost.

*(Items 1–3 are now resolved by the FL build; only 4 and 5 remain unverified.)*

**1 · Sign-convention conflict.** ✅ **RESOLVED — V6, and worse than recorded here.** The conflict is
**internal to FL**: s13 states "work done on the gas is positive", s30 states the exact opposite. GA2
agrees with FL's second half. Full diagnosis in `_verification-log.md`; working rule in
`_nomenclature.md` clash 1.

**2 · Two forms of the gas constant.** ✅ **RESOLVED — not a conflict.** FL s34 teaches $R = R_u/M$ and
tabulates N₂ at $0.2968\ \mathrm{kJ\,kg^{-1}K^{-1}}$, which is the exercises' $0.297$. Same equation,
different basis. No flag issued.

**3 · "FL's own worked example checks out."** ❌ **OVERTURNED — V8.** The intermediates are sound
($n=2.03$ mol, $\Delta T=-60$ K, $W=+1013$ J, $\Delta U=-1518$ J) but the **final answer is wrong**:
the slide prints $Q=-505$ J where the correct value is $-2532$ J, confirmed independently by
$Q = nc_p\Delta T$. This observation had been read from the text layer, which does not include the
final line. **A cautionary case for the whole method: nothing from a text layer is verified.**

**4 · EPC, Carnot's dates.** Printed as "Nicolas Sadi Carnot (**1769**–1832)". Sadi Carnot was born
**1796**; 1769 would have him publishing *Réflexions* at 55 rather than 28. Likely a transposition.
⧗ awaiting Stage 2.

**5 · EPC, Diesel slide.** Lists "less expensive" under Advantages and "initial high cost" under
Disadvantages. ⧗ awaiting Stage 2.

---

## Build plan

Staged deliberately — one document at a time, each stage independently finishable.

| Stage | Work | Status |
|---|---|---|
| **0** | Folder structure, `SOURCES.md`, this index, `.gitignore`, repo corrections | ✅ done |
| **1a** | **TT** → `01-temperature-thermometry.md` — 17 pp. Plus `_nomenclature.md`, `_formula-sheet.md`, `_verification-log.md` created. | ✅ done |
| **1b** | **FL** → `02-first-law.md` — 37 slides. Resolved the $Z$ / Van der Waals gap **and the work sign convention**. | ✅ done |
| **1c** | **GA1 + GA2** → `exercises/` — every question transcribed **and solved**, each cross-linked to the section that answers it. Solving GA1 exposed **V28**. | ✅ done |
| **2** | **EPC** → **`03a-` + `03b-`** *(split — see below)* — 92 slides, 9 examples recomputed | ✅ done |
| **3** | **TC + HE** → `04-`, `05-` — 54 slides | ✅ done |
| **4** | Close out: `README.md`, `exercises/00-exercises-index.md`, `SOURCES.md` corrections, final safety re-run | ✅ done |

`_nomenclature.md`, `_formula-sheet.md` and `_verification-log.md` are **appended at every stage**,
never written at the end. All three now exist, covering TT; each carries its own `coverage:` field and
a "pending" section listing what the next stage must add.

### Why EPC was split into `03a` and `03b`

`docs/kb-format.md` splits a document into `NNa`/`NNb` when it covers **two genuinely independent
themes** *and* exceeds ~25 KB. EPC does both. Slides 1–21 are **phase behaviour and equilibrium** —
qualitative, with **not a single equation**. Slides 22–92 are the **second law, heat engines, Carnot and
the Diesel cycle** — quantitative, and the examinable spine of Topic 3. They share no equations and only
one concept (thermal equilibrium). Keeping them in one file would have buried the second law behind
twenty slides of particle pictures. **Recorded here so the split is not undone.**

### Stage 1c — transcribed, then solved

The exercise files were first built as **questions only**, then the solutions were added on a second
pass. Both halves are in place: every question, every worked answer, and a cross-link from each
question to the section of `01-`…`05-` that carries its theory. **All solutions are tagged `[added]`**
— the brief supplies no answers to students.

**Solving GA1 is what exposed V28**, the Van der Waals unit error. It was invisible while the file
carried questions only, because the constants look unremarkable until you substitute them and get a
liquid-like molar volume for a gas. **That is the argument for working every exercise rather than
transcribing it** — the same argument that produced V8 in the lecture material.

Three further findings from the extraction:

- **GA1's master file carries a facilitator answer key**, headed *"FACILITATOR / LECTURER NOTES (Not
  distributed to students)"* — model answers for all eight groups. It is **not reproduced, quoted or
  paraphrased** anywhere in this knowledge base. GA2 has no equivalent section in any of its nine files.
- **GA2 has no master file.** It ships as nine per-group documents whose Part A is identical; GA1's
  single master covers all eight of its groups.

- **The lecturer's Van der Waals constants are right; only their printed unit is wrong** — V28. The
  correction is a factor of ten, and it changes every Part (ii) answer.

Of the two gaps Stage 1c was meant to fill, **Van der Waals** was supplied `[added]` in `02-first-law`
§2.12 and on the formula sheet, and the **steady-flow energy equation remains unsupplied** — it is
needed only for one GA2 discussion prompt, not for any numerical task.

## Open questions

| Question | Impact | Status |
|---|---|---|
| What does the `3.0 / 3.01 / 3.02 / 3.1 / 3.2` file prefix mean? It is not the internal topic numbering. | cosmetic — letter codes sidestep it | open |
| Are further decks expected (3.3, 3.4…)? | this index is built as a register either way | open |
| Is there a CAT on Topic 1, and when? | would move GA1/GA2 ahead of the deck builds | open |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
