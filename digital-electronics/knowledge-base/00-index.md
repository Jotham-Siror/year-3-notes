---
kb: "Digital Electronics — BEE 3102"
lecturer: "withheld"
file_role: index
unit_title: "Digital Electronics II"
subject_status: "six chapter decks indexed in full; one lab indexed; taught unit"
visibility: "tracked; labs/ and its study guide excluded deliberately — see the lab register"
topics: 10
labs: 1
figures: 156
verification_flags: 81
tags: [digital-electronics, bee-3102, logic-families, memory, plds, adc, dac, fsm, asm]
---

<!-- FOR FUTURE CLAUDE — start here.
  · This is now a full taught-course knowledge base. Six chapter decks — 348 slides — are indexed
    in ten topic files, with _nomenclature.md, _formula-sheet.md and _verification-log.md alongside.
    One laboratory is indexed as well. The earlier version of this file said "lab material only,
    no lecture notes"; that is out of date and every statement of it has been replaced.
  · The unit code is BEE 3102. The decks' own footers title the unit "Digital Electronics II".
    Both are recorded in the frontmatter above.
  · VISIBILITY HAS CHANGED. This subject is no longer local-only. The earlier decision to exclude
    the tree via .git/info/exclude has been REVERSED: digital-electronics/ is tracked, and the
    subject belongs in the tables in CLAUDE.md and README.md.
  · THE LAB IS NOT PART OF THESE NOTES, and this is settled — do not reopen it. "The notes" for
    this subject means the six chapter decks and the excitation-table sheet, nothing else. The lab
    predates them and is held in the working copy only: labs/ is excluded in .git/info/exclude,
    along with study-guides/lab-01-ttl-nand-nor.html, because the lab file quotes a commercial
    manual's procedure text and questions verbatim and labs/figures/scan/ holds page crops of it.
    That material stays unpublished. Do not propose scrubbing it as outstanding work, and do not
    add labs/ to a commit.
  · WHERE AUTHORITY LIES. The ten topic files are authoritative. Do not re-parse the PDFs in
    sources/ — every slide was already read as a 200 dpi page render (never the text layer, which
    carries nothing but the footer on eleven slides: CH1 4, CH3 20-21, CH4 45-46 and CH6 13, 17,
    37-40), every number recomputed, every state table and K-map rederived. Re-reading the raw decks reintroduces exactly the defects the verification log
    removes.
  · Teach the CORRECTED form, and say what the slide prints only where a reader has to recognise
    it — in a tutorial worked off the printed page, or in a CAT.
  · [added] IS NOT OPTIONAL. Anything supplied here that is not on a slide — a standard result the
    deck omitted, a solution the deck left open, extra context — carries [added]. A reader must
    always be able to separate the lecturer's material from ours.
  · Neutral voice. No lecturer name appears on any slide in any deck; the footer carries a social
    handle instead, which is treated as a contact detail and appears nowhere in this subject.
    Anything personal belongs in _personal/.
-->

# Digital Electronics (BEE 3102) — knowledge-base index

**What this is.** A verified map of the BEE 3102 chapter decks and the one laboratory held for this
unit. Every claim is anchored to its slide, every suspected error flagged and corrected. Start here,
then open the file you need rather than going back to the raw PDFs.

**Unit title.** The decks title themselves **Digital Electronics II**; the code on the timetable is
**BEE 3102**. Both names refer to the same unit.

> **Operating instructions** — how to navigate and teach from this knowledge base — live in
> `CLAUDE.md` at the project root, not in this file.

---

## Status

| | |
|---|---|
| Lecture notes | **six chapter decks, 348 slides, indexed in full** as ten topic files |
| Labs | 1, indexed in full — `labs/lab-01-ttl-nand-nor.md` |
| Unit code | **BEE 3102**; the decks' footers title the unit *Digital Electronics II* |
| Verification log | **`_verification-log.md`** — 81 defects: 36 substantive, 45 cosmetic |
| Nomenclature | **`_nomenclature.md`** — every symbol, with a two-tier clash table |
| Formula sheet | **`_formula-sheet.md`** — every equation, in corrected form, tagged to its slide |
| Visibility | **tracked** — but see § Open questions, item 1, before pushing |

Coverage is complete: every slide of all six decks is either taught, cited, or explicitly recorded
as a title, blank or duplicate slide. No slide was left unread.

---

## Contents

```
digital-electronics/
├── knowledge-base/
│   ├── 00-index.md                          ← this file
│   ├── 01-introduction-and-recap.md
│   ├── 02-digital-logic-families.md
│   ├── 03-semiconductor-memory.md
│   ├── 04-programmable-logic-devices.md
│   ├── 05-analogue-to-digital-conversion.md
│   ├── 06-digital-to-analogue-conversion.md
│   ├── 07-fsm-fundamentals-and-analysis.md
│   ├── 08-sequential-circuit-design.md
│   ├── 09-state-reduction-and-assignment.md
│   ├── 10-algorithmic-state-machines.md
│   ├── _nomenclature.md
│   ├── _formula-sheet.md
│   ├── _verification-log.md
│   ├── flags/
│   │   └── 01.md … 10.md                    ← per-file defect entries, cited from the topic files
│   ├── figures/
│   │   └── NN-<slug>.svg                    ← 142 redrawn figures, prefixed by topic-file number
│   └── labs/
│       ├── lab-01-ttl-nand-nor.md
│       └── figures/
│           ├── fig-4-*.svg                  ← 14 redrawn figures
│           └── scan/                        ← ⚠ page crops — must go before any push
├── study-guides/
│   └── lab-01-ttl-nand-nor.html             ← printable bench companion
└── sources/                                  ← raw material, untracked; see SOURCES.md
    ├── SOURCES.md
    ├── "BEE 3102 Chapter 1 … Chapter 6" .pdf ← the six chapter decks, 348 slides
    ├── the excitation-table page             ← one A4 page, cited as ·EXC
    └── lab-01-ttl-nand-nor-gates.pdf
```

Everything we author is kebab-case; a leading `_` marks a cross-cutting file rather than a topic.
Raw material in `sources/` keeps the filenames it arrived with and is listed in abbreviated form
above — `sources/SOURCES.md` is the manifest.

---

## Topic register

The main navigation aid. Sizes are the written files; flags are counted as substantive / cosmetic.

| № | Section | Deck · slides | Size | Flags | Status |
|---|---|---|---|---|---|
| **01** | Introduction and Recap | CH1 · 1–32 | 39 KB | 1 V, 3 C | ✅ complete |
| **02** | Digital Logic Families | CH2 · 1–43 | 50 KB | 5 V, 6 C | ✅ complete |
| **03** | Semiconductor Memory | CH3 · 1–33 | 46 KB | 4 V, 2 C | ✅ complete |
| **04** | Programmable Logic Devices | CH3 · 34–66 | 42 KB | 1 V, 6 C | ✅ complete |
| **05** | Analogue-to-Digital Conversion | CH4 · 1–29 | 43 KB | 5 V, 5 C | ✅ complete |
| **06** | Digital-to-Analogue Conversion | CH4 · 30–49 | 38 KB | 9 V, 6 C | ✅ complete — **most defects of any file** |
| **07** | FSM Fundamentals and Sequential Circuit Analysis | CH5 · 1–38 + EXC | 54 KB | 3 V, 4 C | ✅ complete |
| **08** | Sequential Circuit Design and Sequence Detectors | CH5 · 39–71 | 47 KB | 2 V, 6 C | ✅ complete |
| **09** | State Reduction and State Assignment | CH5 · 72–118 | 62 KB | 3 V, 3 C | ✅ complete |
| **10** | Algorithmic State Machines | CH6 · 1–40 | 64 KB | 3 V, 4 C | ✅ complete |

**On file sizes.** Eight files sit above the ~40 KB guideline and none has been split. The split
rule in `docs/kb-format.md` requires *two genuinely independent themes*, and each of these is one
continuous argument. Each file states, at its end, exactly where a future split would fall:

- **02** between slides 19 and 20 — the deck's own outline draws the same line
- **03** between §10 and §11 — how memory is built and addressed, then coding theory applied to it
- **04** after §4.9 — the combinational PLDs, then the descriptive sequential-device coverage
- **05** between §5.6 and §5.7 — the conversion process, then the converter circuits
- **07** between slides 17 and 18 — FSM fundamentals, then sequential-circuit analysis
- **08** after §8.9 — but this cut still separates a Mealy machine from its Moore counterpart
- **09** between slides 90 and 91 — state reduction, then state assignment and the worked Cases
- **10** at the deck's own appendix boundary, slides 22 / 23

Do not split without reading those notes first.

---

## Chapter-to-file map

Three of the six decks are split across two or three files. Holding a chapter PDF, this is the file
to open.

| Deck | Slides | Topic file(s) |
|---|---|---|
| **CH1** — Introduction | 1–32 | `01-introduction-and-recap.md` (all of it) |
| **CH2** — Digital Logic Families | 1–43 | `02-digital-logic-families.md` (all of it) |
| **CH3** — Memory and Programmable Logic Devices | 1–33 | `03-semiconductor-memory.md` |
| | 34–66 | `04-programmable-logic-devices.md` |
| **CH4** — Signal Conversion (ADC / DAC) | 1–29 | `05-analogue-to-digital-conversion.md` |
| | 30–49 | `06-digital-to-analogue-conversion.md` |
| **CH5** — Finite State Machines & Sequential Circuit Design | 1–38 | `07-fsm-fundamentals-and-analysis.md` |
| | 39–71 | `08-sequential-circuit-design.md` |
| | 72–118 | `09-state-reduction-and-assignment.md` |
| **CH6** — Algorithmic State Machines | 1–40 | `10-algorithmic-state-machines.md` |
| **EXC** — Excitation table | 1 page | `07-fsm-fundamentals-and-analysis.md` §7.15 |

Citations in the topic files take the form **·CH4 slide 16**. The printed footer number equals the
PDF page number in every deck, so slide 16 of CH4 is page 16 of the CH4 PDF — verified across all
six. The single-page excitation handout is cited as **·EXC**.

---

## Dependency and reading order

Taken from the files' own `prerequisites` and `leads_to` frontmatter. One line of reason each.

1. **01 — Introduction and Recap** — no prerequisites. Sets integration scale, propagation delay and
   the D / JK flip-flop, register and counter recap that both later chains assume.
2. **02 — Digital Logic Families** — needs 01's propagation delay and integration scale; supplies
   logic levels, noise margins, fan-out and the TTL and CMOS circuits everything else is built from.
3. **03 — Semiconductor Memory** — needs 02, because a memory cell *is* a logic-family circuit: the
   six-transistor SRAM cell is read as a pair of CMOS inverters.
4. **04 — Programmable Logic Devices** — needs 03; the PROM is a ROM with one array made
   programmable, and the ROM / PAL / PLA comparison is stated in ROM terms.
5. **05 — Analogue-to-Digital Conversion** — needs 02 only, for the comparator and the logic levels.
   It does **not** need 03 or 04.
6. **06 — Digital-to-Analogue Conversion** — needs 05; the resolution and step-size argument, and
   the $2^{n}$ against $2^{n}-1$ distinction, are set up there.
7. **07 — FSM Fundamentals and Analysis** — needs 01 for the flip-flops and their characteristic
   equations; the excitation table is introduced here.
8. **08 — Sequential Circuit Design** — needs 07; design is analysis run backwards, on the same
   state tables, state diagrams and excitation tables.
9. **09 — State Reduction and Assignment** — needs 08; it reduces and encodes the very state tables
   08 produces.
10. **10 — Algorithmic State Machines** — needs 09 for state assignment and K-map realisation, and
    07 for the JK characteristic equation.

**Where order is safe to break.**

- The converter pair **05 → 06** is independent of everything after it. Nothing in 07–10 refers to
  it and it refers to nothing in 03 or 04. It can be read at any point once 02 is done.
- The memory pair **03 → 04** likewise sits outside the FSM chain entirely.
- **01 → 07** is a valid entry: the FSM chain hangs off the recap, not off the device chapters.

**Where order cannot be broken.**

- **09 needs 08 needs 07.** Each of the three is the previous one applied further to the same
  machines; the worked Cases in 09 refer back to detectors first built in 08.
- **06 needs 05.** Reading 06 alone is the fastest route to the unit's most common error — see the
  $2^{n}$ / $2^{n}-1$ row at the top of `_nomenclature.md`.
- Within CH5, the deck's own numbering runs 1 → 118 continuously; 07, 08 and 09 are one argument in
  three files.

---

## Verification summary — 81 flags

Full detail in **`_verification-log.md`**: **36 substantive** (`V01-1` … `V10-3`) and
**45 cosmetic** (`C01-1` … `C10-4`). Per-file entries are in `flags/01.md` … `flags/10.md`, which
the topic files cite inline. The IDs are globally unique by file number — **do not renumber them.**

**The distribution is uneven, and that is the useful fact.** CH1, CH2, CH3 and CH6 are mostly sound;
their defects are prose, labels and taxonomy. **CH4 is the problem deck** — 14 of the 36 substantive
defects on 49 slides, nine of them in the D/A half alone. CH5 is structurally excellent: all fifteen
state machines in the deck were rebuilt in software and every one is functionally correct; its
substantive defects are in the surrounding text, equations and figures, never in a machine.

### ⚠ Read before a CAT

The full shortlist is `_verification-log.md` § 2, worst first. It is not duplicated here — but a
reader who opens only this index should still meet the worst three.

- **V06-9 · CH4 slides 44 and 47 — the R/2R bit weight is off by one in the exponent.** The deck
  prints $V_S/2^{\,n-i}$ where its own $D_0 \ldots D_{n-1}$ numbering requires

  $$V_{\text{out}}(D_i) = -\frac{V_S}{2^{\,n-1-i}}$$

  Every value the deck gives for that converter is a factor of two low: the printed $-3.4375$ V for
  input 1011 should be $-6.875$ V. **A marking scheme built from the slide will mark the correct
  answer wrong.** Know both numbers.

- **V05-1 · CH4 slide 20 — the SAR comparator decision rule is stated backwards.** Follow the slide
  and every bit of every conversion is inverted; the converter returns the ones-complement of the
  right code.

- **V03-4 · CH3 slide 29 — the Hamming syndrome for an error at position 12 is printed $1000$.** But
  $1000_2 = 8$, so positions 8 and 12 would share a syndrome; the decoder then "corrects" the wrong
  bit and injects a second error. It is $1100$.

Two more worth knowing by name: **V06-3 and V06-4** (CH4 slides 36 and 37 — a reversed inequality
chain that concludes 7 bits where the answer is 8, and a BCD DAC worked through the binary formula,
putting three numbers wrong on one slide), and **V08-1** (CH5 slide 53 — a Moore specification
copy-pasted from the Mealy one, still claiming an output coincident with the last input; it is the
single most commonly lost mark in the sequence-detector topic).

`_verification-log.md` § 4 records what was checked and found **correct**, so nobody re-checks it,
and § 5 records the open questions, including which corrections came from the deck itself and which
from a standard result.

---

## Lab register

> **Outside the notes, and held locally.** This subject's *notes* are the six chapter decks and the
> excitation-table sheet — files `01`–`10` and the three cross-cutting files. The laboratory below
> is separate material that predates them, kept for reference. `labs/` is excluded from git
> deliberately and permanently: the lab file quotes a commercial manual's procedure text and
> questions verbatim, and `labs/figures/scan/` holds crops of its pages. On a clone of the public
> repository the whole directory is absent and the links in this section will not resolve; in the
> working copy it is all present. This is a settled decision, not an outstanding task.


| Lab | Title | Devices | Phases | Status | File |
|---|---|---|---|---|---|
| 1 | TTL NAND/NOR gates — definitions and operation | 7400, 7403 | simulation → practical | `unrun` | `labs/lab-01-ttl-nand-nor.md` |

### Lab 1 at a glance

- **Source:** Experiment 4, pp. 31–44 of a commercial laboratory manual. Scanned, image-only,
  14 pages. Blank worksheet copy.
- **Five procedure parts**, four experimental tables, four required-results tables, nine discussion
  questions, thirteen numbered figures.
- **Two instructor checkpoints** written into the procedure: after Part 3(c) ("DO NOT PROCEED") and
  after Part 4(b) (data *and* plotted curve must be approved).
- **Every table is a three-column form** — Predicted / Simulated / Measured. The disagreements
  between columns are what the discussion questions ask about.
- **`status: unrun`.** Nothing has been computed, predicted or answered. That is deliberate: the
  department brief has not been seen, so scope is unknown. The manual is indexed in full so that any
  scope is covered.
- **Chapter 2 is this lab's theoretical partner**, and `02-digital-logic-families.md` cross-references
  it throughout — the transfer characteristic (§3 there, Part 4 here), the unit load and fan-out
  (§5 there, Part 3(a) here), current sinking as the mechanism behind the unit load (§8 there),
  floating inputs sitting at logic 1 (§9 there, Parts 2(b), 4 and 5 here), and capacitive loading
  (§4 there, Part 5 here). Every one of those cross-references is tagged `[added]`, because the
  connection is ours and not the deck's.

### Why the lab has no verification log entries

The reasoning that once covered the whole subject now covers only the lab. `_verification-log.md`
catalogues defects in the **lecturer's own teaching material** — the six chapter decks. The lab is
different: it is a published commercial manual, and **nothing in it was found to be wrong**.

Three things about the manual are worth knowing before meeting them on the page. They are recorded
under "Observations about the manual itself" in the lab file, as observations rather than defects:

1. **Part 4 carries no number** on the page; its number is established only by cross-references.
2. **Several gate inputs are drawn as open stubs** (pin 2 in Fig. 4-10; pins 2 and 5 in Fig. 4-12).
   Deliberate, not an omission — a floating TTL input sits at logic 1, which Part 2(b) has just
   established.
3. **The title says NAND/NOR, but every IC is a NAND.** The NOR appears only under the
   negative-logic reading in Required Result 2(b) and Discussion 2(b).

If a defect is found once the lab is worked, add it to `_verification-log.md` under an `L1` heading
rather than starting a second log, and follow the `V`/`C` convention in `docs/kb-format.md`.

### Reading order within the lab

1. **Fig. 4-1(a) and (b)** — the two circuits. Everything else refers back to them.
2. **The unit load and fan-out** — lab file, "Theory the questions actually depend on"; read
   alongside §5 and §8 of `02-digital-logic-families.md`.
3. **Parts 1 and 2** — trivial to run, and they set up the logic-level definitions.
4. **The threshold argument** at node N — needed for Discussion 6 and all of Discussion 7.
5. **Part 3** — loading rules; feeds Discussion 4, 5 and 8(f).
6. **Part 4** — transfer characteristic; feeds all of Discussion 7 and 8(c).
7. **Part 5** — capacity loading; feeds Discussion 8.
8. **Required Results 2(a) against 2(b)** — positive against negative logic; feeds Discussion 2 and 9.

Dependency worth noting: **Part 4 must be done before Discussion 8(c) can be answered**, because
8(c) compares the pin-3 peak voltage against the threshold read off the Fig. 4-11 curve.

---

## Figure map

**156 figures**, all hand-written SVG, all authored here. None is reproduced from a source.

| Where | Count | Naming |
|---|---|---|
| `01-introduction-and-recap.md` | 9 | `figures/01-*.svg` |
| `02-digital-logic-families.md` | 14 | `figures/02-*.svg` |
| `03-semiconductor-memory.md` | 11 | `figures/03-*.svg` |
| `04-programmable-logic-devices.md` | 12 | `figures/04-*.svg` |
| `05-analogue-to-digital-conversion.md` | 14 | `figures/05-*.svg` |
| `06-digital-to-analogue-conversion.md` | 11 | `figures/06-*.svg` |
| `07-fsm-fundamentals-and-analysis.md` | 18 | `figures/07-*.svg` |
| `08-sequential-circuit-design.md` | 10 | `figures/08-*.svg` |
| `09-state-reduction-and-assignment.md` | 23 | `figures/09-*.svg` |
| `10-algorithmic-state-machines.md` | 20 | `figures/10-*.svg` |
| **Topic-file subtotal** | **142** | |
| `labs/lab-01-ttl-nand-nor.md` | 14 | `labs/figures/fig-4-*.svg` — 14 files for 13 numbered figures, because Fig. 4-1 splits into (a) and (b) |
| **Total** | **156** | |

Individual figures are not listed here. Each topic file carries its own numbered figures inline, and
the number prefix says which file a figure belongs to.

### The `figure_data` convention

Every redrawn figure appears **twice** in its file:

1. a **`figure_data` YAML block** carrying the authoritative content — component values, nets, pin
   numbers, states, transitions, table entries;
2. the **SVG**, as a Markdown image reference.

To *show* the picture, render the SVG. To *reason* about the circuit or the machine, read the block.
**Never re-measure from SVG path coordinates** — the drawing is a rendering of the data, not the
other way round, and a coordinate is not a component value.

### Captioned, not redrawn

Third-party artwork is **never** reproduced, regardless of watermark — the rule is *commit what we
authored*. Where a slide's figure is a photograph, a chip-package shot, a datasheet screenshot,
decorative art, or plainly lifted from a textbook or published paper, the topic file carries a
`[fig]` caption describing what the slide showed, with its citation, and no image.

Examples: the microprocessor-trend chart on CH1 slide 4 (widely circulated, must never be
reproduced); the DRAM-organisation diagram on CH3 slide 21 (from a published paper); the fan-in and
fan-out line art on CH2 slide 11; the datapath redraw on CH6 slide 30.

The dividing line is **whether a reader must reason from it**. A schematic, state diagram, ASM
chart, ladder network, K-map, fuse map or timing diagram is redrawn from scratch. Anything else is
captioned. When in doubt, caption.

---

## Coverage and gaps

**What the decks teach, and examine.** All six chapters are taught in full, and the examinable
weight sits where the worked examples are:

- **CH4** is the most numerical chapter in the unit — eleven worked examples in the D/A half alone,
  and every one of them arithmetic. It is also the deck with the most defects, which is a bad
  combination and the reason `_verification-log.md` § 2 leads with it.
- **CH5** carries the most worked machines — ten analysis examples in file 07, six sequence
  detectors in file 08, four full Cases in file 09 — all rebuilt and simulated.
- **CH2** is the parameter chapter: logic levels, noise margins, fan-out, power. Three worked
  examples, and the lab measures the same quantities.
- **CH1** is a recap and a roadmap; **CH3**, **CH6** are mostly structural, with sizing arithmetic
  in CH3 and the PLA table in CH6.

**What the decks name but never teach.** Recorded so that a reader does not go looking for a
treatment that is not there.

| Topic | Where it is named | Where it is meant to come from |
|---|---|---|
| **ECL (emitter-coupled logic)** | the family classification ·CH2 slide 20 | textbook reading, set as homework ·CH2 slide 43 — **taught nowhere in the deck** |
| **Plain PMOS and NMOS logic** | the same classification ·CH2 slide 20; called obsolete in passing | the same homework ·CH2 slide 43 — **taught nowhere in the deck** |
| **Digital-ramp (counter-type) ADC** | **one row** of the comparison table ·CH4 slide 28 | set as homework ·CH4 slide 24 — the exercise deliberately sends the reader outside the deck |
| **Monotonicity, linearity error, settling time** | ·CH4 slide 49 only | named on no other slide in any of the six decks; the homework asks for all three |
| **Final expressions from map-entered variables** | ·CH6 slide 22 stops at the maps and refers out to the textbook | file 10 reads them off the maps and supplies the final expressions, tagged `[added]` |
| **PROM/EPROM/EEPROM detail, flash memory, memory expansion, magnetic and optical storage** | reading list ·CH3 slide 64 | textbook reading; the decks give the block-level treatment only |
| **TTL worked examples 15-3 to 15-7** | pointer only ·CH2 slide 34 | third-party textbook, not reproduced here |
| **Microcontroller against PLD** | question posed ·CH1 slide 25 | never answered — by the deck or here |

**One acknowledged gap in the source, not a defect.** CH5 slide 41 draws an input and output
waveform but never states which sequence the machine detects. What can be read from the drawing
without guessing is recorded in file 08; **no target sequence has been inferred.**

**Every figure is read — none outstanding.** One was open when this file was first written and was
settled on 19 Aug 2026: the solid mark on each RTL base lead in CH2 slide 24 is a **diode in series
with the base**, protecting the emitter-base junction from the negative rail $V-$ that $R_1$ returns
the base to. Fig. 2-5 in `02-digital-logic-families.md` now draws it; the reasoning is `[added]`,
since the deck never states it. See `_verification-log.md` § 5.3.

---

## Homework register

The decks set homework on eight slides. **All are transcribed in full in the topic files and left
unsolved** — they are the student's to do.

| Slide | Lives in | What is set |
|---|---|---|
| **CH2 s43** | `02` §16 | Textbook reading — ECL circuits (p. 882), PMOS / NMOS / E²CMOS (p. 884) — plus the end-of-chapter problems, pp. 887–893 |
| **CH3 s64** | `04` §4.13 | Reading — programmable ROMs, flash memory, memory expansion, magnetic and optical storage |
| **CH3 s65** | `04` §4.13 | Problems 1–3 — address and I/O lines for four memory sizes, bytes stored, and the address and content of word 723 of a $1024 \times 16$ memory |
| **CH3 s66** | `04` §4.13 | Problems 4–5 — ROM size for four combinational blocks, and the truth table of an $8 \times 4$ ROM realising four given functions |
| **CH4 s18** | `05` §5.9 | 3-bit flash ADC at $V_{\text{REF}} = 8$ V — comparator count, resolution, and the codes for four input voltages |
| **CH4 s23** | `05` §5.11 | 4-bit SAR ADC at $V_{\text{REF}} = 5$ V and $f_{\text{CLK}} = 1$ MHz — clock cycles, conversion time, the code for 3.2 V, then the same by flowchart |
| **CH4 s24** | `05` §5.11 | "Draw and discuss Digital Ramp ADC" — a converter the deck never teaches |
| **CH4 s49** | `06` §6.8 | Discuss resolution, accuracy, full-scale error, monotonicity, linearity error, maximum sampling frequency and settling time; then analyse applications of ADCs and DACs |

**The three CH4 items on slides 18, 23 and 24 print a due date of 6 August 2025.** That is from a
**previous run of the unit** and is historical — it is not a current deadline. The topic files say
so at each occurrence. Slide 49's homework carries no date.

**Two further questions are set but do not belong to the homework list**, and are also left
unsolved:

- **·CH1 slide 25** — *What is the difference between a Microcontroller and a PLD?* Posed by the
  deck and never answered by it (file `01`).
- **·CH5 slide 107** — *Check by yourself:* clock the realised Case II circuit through the sixteen
  input bits $X = 0011011001010100$ and confirm $Z = 0000010000010100$. To be worked from the gates,
  not from the state graph (file `09`).

Two in-deck identification exercises are answered where the deck answers them: **·CH2 slide 24**
(three RTL circuits — only one carries its answer on the page) and **·CH2 slide 30** (a two-emitter
TTL gate; the answer is supplied and tagged `[added]`).

---

## Open questions

1. **Whether the department's marking scheme follows the decks where they are wrong.** Where a
   printed value is the deck's only stated result, a scheme derived from the slide will award the
   printed answer. Worth raising before a CAT: **V06-9** ($-3.4375$ V against the correct
   $-6.875$ V), **V06-4** and companions (the BCD DAC), **V06-3** (the printed chain answers 7 bits
   where the stated answer is 8), **V05-4** (the dual-slope count), **C10-2** (which counter
   numbering an exam question will quote), and **V02-1** (which of the deck's two incompatible
   integration-scale tables will be examined).
2. **The lab brief.** Scope, deliverables, report format, and how the work divides between the
   simulation and practical phases.
3. **Which simulator** phase 1 of the lab uses. This determines whether Parts 3, 4 and 5 can be
   simulated at all — see "Simulation notes" in the lab file.
4. **Whether more labs follow.** If they do, the layout above already scales: add
   `labs/lab-02-*.md` and extend the register.
*(A sixth item — a screenshot of CH2 slide 24, to settle the unexplained mark on the RTL base
leads — was **closed on 19 Aug 2026**. It is a series base diode; see `_verification-log.md` § 5.3.
Every figure in the 348 slides is now read.)*

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026. Every cross-reference in this
file was checked against the files actually present; flag counts were recounted from the per-file
lists and the verification log, and figure counts from the figures directory.</i></sub>
