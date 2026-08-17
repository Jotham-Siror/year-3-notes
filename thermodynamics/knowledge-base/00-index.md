---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
programme: "BSc Electrical Engineering, Year 3 Semester 1"
lecturer: "withheld"
file_role: index
source: "5 lecture documents (200 pp.) + 2 sets of assessed group activities. See ../sources/SOURCES.md"
built: "IN PROGRESS — Stage 1a complete (TT transcribed and verified). Stages 1b–4 outstanding."
coverage: "17 / 200 pages transcribed and verified (TT)"
total_verification_flags: 6
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Thermodynamics (MEC 3105) — Knowledge Base Index

> ## ⚠ Build status — 1 of 5 documents complete
>
> **§1.1 Temperature and Thermometry (TT) is transcribed and fully verified** — teach from
> `01-temperature-thermometry.md` freely. Every one of its 17 pages was read from a render and every
> number recomputed.
>
> **Everything else is still scaffold.** For FL, EPC, TC, HE and the group activities, say so plainly
> and work from the raw notes in `../sources/`. In particular, the entries in § Early observations are
> text-layer readings that have **not** been checked against a render and carry no ID.

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
| **FL** | First Law of Thermodynamics | 37 | 1 — §1.3 | `02-first-law.md` | ⏳ not started |
| **EPC** | Energy Equations and Phase Changes | 92 | 2 | `03-second-law-and-cycles.md` | ⏳ not started |
| **TC** | Power Production and Thermodynamic Cycles (1) | 24 | 3 | `04-thermodynamic-cycles.md` | ⏳ not started |
| **HE** | Power Production and Thermodynamic Cycles (2) | 30 | 3 | `05-heat-engines-and-carnot.md` | ⏳ not started |
| **GA1** | Group Activities 1 | — | 1 — §1.1, §1.2 | `exercises/ga1-…md` | ⏳ not started |
| **GA2** | Group Activities 2 | — | 1 — §1.3 | `exercises/ga2-…md` | ⏳ not started |

Provenance: **·TT p7** (page-based) · **·EPC s68** (slide-based) · **·GA1 G3 Part B Q2** (exercises).
Full detail in `../sources/SOURCES.md`.

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

## Planned file layout

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
2. Every solution we write carries `[added]` — the sheets ship with no answers at all.
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
| Kelvin–Planck & Clausius statements | full, + equivalence | — | implied | **EPC** |
| Heat engine, $Q_H$ / $W$ / $Q_C$ | full | brief | full | **EPC**, HE for framing |
| Thermal efficiency $\eta_{th}=1-Q_L/Q_H$ | full + derivation | stated | full | **EPC** |
| Carnot cycle, four processes | full | named | full + entropy table | **EPC**, HE's table added |
| Carnot efficiency $\eta=1-T_L/T_H$ | full + absolute-scale derivation | named | full + unit traps | **EPC**, HE for the traps |
| COP, $\mathrm{COP}_{HP}=\mathrm{COP}_R+1$ | full | stated | — | **EPC** |
| Irreversibilities | itemised | factors table | factors table | **EPC** |
| $T$–$s$ diagram | — | named | Carnot rectangle | **HE** |
| Otto / Brayton / Rankine / Stirling | Diesel only | table | table | **TC/HE** |
| Selection workflow, common mistakes | — | full | full | **TC/HE** |
| **Worked numerical examples** | **5** | **0** | **0** | **EPC — the only numbers in the set** |

**Build order follows from this:** EPC must be written *before* TC and HE, or Carnot gets written
three times and unpicked afterwards.

---

## ⚠ Gap map — syllabus assessed but not (visibly) taught

Recovered from the group activities. **These are examined.**

| Topic | Assessed in | Present in the decks? |
|---|---|---|
| Van der Waals equation, constants $a$, $b$ | GA1 Part B | FL has a slide *titled* "Other Equations of State" — **image-only, contents unknown** |
| Compressibility factor $Z$, $Z\gtrless1$ | GA1 Part B | FL has two slides *titled* "Compressibility Factor Z" — **image-only, contents unknown** |
| Specific heats, $c_p-c_v=R$ | GA2 Part B | not seen in the text layer |
| Enthalpy $h=u+Pv$; steady-flow energy equation | GA2 | TC defines enthalpy in one line; SFEE not seen |
| Property / steam tables | — | absent |
| Entropy as a property (Clausius inequality, $T\,ds$) | — | absent |
| Worked Otto / Rankine / Brayton analysis | — | named in TC/HE tables, never analysed |

**Resolving rows 1–2 is the first job of the FL build.** Until those slides are rendered we do not
know whether the material is taught or merely listed.

---

## Verification summary

Full detail in `_verification-log.md`.

| Doc | Pages | Substantive `V` | Cosmetic `C` | Status |
|---|---|---|---|---|
| **TT** | 17 | **4** | **2** | ✅ complete |
| FL | 37 | — | — | ⏳ |
| EPC | 92 | — | — | ⏳ |
| TC | 24 | — | — | ⏳ |
| HE | 30 | — | — | ⏳ |
| **Total** | **17 / 200** | **4** | **2** | — |

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

*(TT is no longer in this list — it is verified. All five items below belong to FL and EPC.)*

**1 · Sign-convention conflict between the deck and the exercises.** The highest-impact item found
so far.

FL states *"work done on the gas is positive"* and writes

$$Q = W + \Delta U$$

GA2 states *"Q positive into the system; W positive done **BY** the system"* and writes

$$\Delta U = Q - W$$

These define $W$ with **opposite signs**. The same compression gives $W=+1013$ J under FL's
convention and $W=-1013$ J under GA2's. Belongs in `_nomenclature.md`'s clash table.

**2 · Two forms of the gas constant.** FL uses $PV=nRT$ with $\bar R = 8.314$ J·mol⁻¹·K⁻¹; the group
activities use $PV=mRT$ with a specific $R$ (e.g. $0.297$ kJ·kg⁻¹·K⁻¹ for N₂). Both correct, easy to
conflate under time pressure.

**3 · FL's own worked example checks out.** Recomputed independently: $n=2.03$ mol, $\Delta T=-60$ K,
$W=+1013$ J, $\Delta U=-1518$ J, $Q=-505$ J. The arithmetic is sound; only the sign convention is
inconsistent *between slides*.

**4 · EPC, Carnot's dates.** Printed as "Nicolas Sadi Carnot (**1769**–1832)". Sadi Carnot was born
**1796**; 1769 would have him publishing *Réflexions* at 55 rather than 28. Likely a transposition.

**5 · EPC, Diesel slide.** Lists "less expensive" under Advantages and "initial high cost" under
Disadvantages.

---

## Build plan

Staged deliberately — one document at a time, each stage independently finishable.

| Stage | Work | Status |
|---|---|---|
| **0** | Folder structure, `SOURCES.md`, this index, `.gitignore`, repo corrections | ✅ done |
| **1a** | **TT** → `01-temperature-thermometry.md` — 17 pp. Plus `_nomenclature.md`, `_formula-sheet.md`, `_verification-log.md` created. | ✅ done |
| **1b** | **FL** → `02-first-law.md` — 37 slides, 19 image-only. Resolves the $Z$ / Van der Waals gap **and the work sign convention**. | ⏳ **next** |
| **1c** | **GA1 + GA2** → `exercises/`, transcribed and solved | ⏳ |
| **2** | **EPC** → `03-second-law-and-cycles.md` — 92 slides, 5 examples to recompute | ⏳ |
| **3** | **TC + HE** → `04-`, `05-` — fast; EPC already owns the shared concepts | ⏳ |
| **4** | Close out: overlap map finalised, gap map, formula sheet, nomenclature, `README.md` | ⏳ |

`_nomenclature.md`, `_formula-sheet.md` and `_verification-log.md` are **appended at every stage**,
never written at the end. All three now exist, covering TT; each carries its own `coverage:` field and
a "pending" section listing what the next stage must add.

**Stage 1b's first jobs, in order:** resolve the work sign convention (`_nomenclature.md` clash 1 —
pre-registered but unverified), then render FL's 19 image-only slides to settle the Van der Waals / $Z$
rows of the gap map below.

## Open questions

| Question | Impact | Status |
|---|---|---|
| What does the `3.0 / 3.01 / 3.02 / 3.1 / 3.2` file prefix mean? It is not the internal topic numbering. | cosmetic — letter codes sidestep it | open |
| Are further decks expected (3.3, 3.4…)? | this index is built as a register either way | open |
| Is there a CAT on Topic 1, and when? | would move GA1/GA2 ahead of the deck builds | open |

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
