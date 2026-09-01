---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
file_role: index
tiers: "1 = the course lecture notes (100 pp., primary) · 2 = seven lesson documents (169 pp., supporting) · 3 = four slide decks (59 pp., reference)"
source: "328 pages across three tiers"
built: "Every page rendered to an image and read from the render; equations rewritten in canonical LaTeX; every numerical claim recomputed; suspected errors flagged inline and collected in _verification-log.md; every unsolved exercise solved and verified and tagged [added]"
coverage: "328/328 pages mapped. Several source documents are internally incomplete - see the Gap map"
total_verification_flags: 388
substantive_flags: 158
cosmetic_flags: 230
tags: [analogue-electronics, semiconductors, dc-circuits, network-theorems, passives, diodes, rectifiers, filters, zener, bjt, fet, mosfet, biasing, amplifiers, h-parameters, feedback, frequency-response, fabrication]
---

# Analogue Electronics I (BEE 3103) — Knowledge Base Index

**What this is.** A verified map of every source issued for BEE 3103 — every claim anchored to its
page, every suspected error flagged and corrected, every worked example re-computed. Start here,
then open the topic file you need rather than re-reading the raw PDFs.

**Status.** 328 pages read, 388 defects logged, three tiers complete.

> **Operating instructions** — how to navigate and teach from this knowledge base — live in
> `CLAUDE.md` at the project root, not in this file.

---

## The three tiers, and which one wins

| Tier | Source | Pages | Code | Files | Standing |
|---|---|---|---|---|---|
| **1 — PRIMARY** | **The course's own lecture notes** | 100 | **`·J p33`** | `01`–`07` | **This is what the course teaches. It sets the scope and the emphasis.** |
| 2 — supporting | Seven lesson documents | 169 | `·L1 p7` … `·L7 p27` | `11`–`17` | Fuller textbook treatment. The **only** source for four topics — see the topic map |
| 3 — reference | Four slide decks | 59 | `·RD3 p5` | `_reference-decks.md` | Mapped, **not verified**. Label anything taught from it |

**How to use the tiers together.**

1. **Scope comes from tier 1.** If the lecture notes do not cover it, it is unlikely to be examined —
   with the four exceptions listed in the topic map below, which tier 1 skips but the syllabus does
   not.
2. **Depth comes from tier 2** where the two overlap. The lesson documents carry more worked
   examples and fuller derivations on diodes, rectifiers, BJTs and FETs.
3. **Where they disagree, neither wins automatically.** `_verification-log.md` § Cross-tier
   resolutions settles each case individually — 8 go to tier 1, 10 go to tier 2, and 3 are defects
   both inherited, where a second source is *not* confirmation.
4. **Tier 3 fills two holes tier 1 leaves** (below) and is otherwise background.

---

## Topic map — which tier covers what

| Topic | Tier 1 (primary) | Tier 2 (supporting) | Tier 3 |
|---|---|---|---|
| What electronics is; analogue vs digital signals | `01` ·J p2 | — | RD1 |
| Matter, atomic structure, energy bands, **doping** | `01` ·J p3–p9 | — | RD2 |
| **Resistors, Ohm's law, series/parallel, colour code** | `02` ·J p10–p15, p23 | ❌ **none** | — |
| **Source models, Thevenin, Norton, mesh analysis** | `02` ·J p16–p22 | ❌ **none** | — |
| **Capacitors, inductors, transformers** | `03` ·J p24–p32 | ❌ **none** | — |
| Junction diode, models, load line, special diodes | `04` ·J p33–p45 | `11` | RD3 |
| Rectifiers, filters, zener regulation | `05` ·J p46–p56 | `12` | — |
| Bipolar junction transistor and biasing | `06` ·J p57–p83 | `13` | — |
| Field effect transistors and biasing | `07` ·J p84–p100 | `14` | — |
| **Fabrication and integrated circuits** | ❌ two passing lines | `15` | — |
| **$h$-parameters and small-signal analysis** | ❌ a symbol table only, ·J p61 | `16` | — |
| **Feedback, multistage amplifiers, frequency response** | ❌ **none** | `17` | — |
| **Small-signal FET parameters $g_m$, $r_d$, $\mu$** | ❌ **named once, never defined** | `14` §4.8, §4.12 | — |
| The electronic system: sensors, ADC/DAC, actuators | — | — | RD4 |

**Read the ❌ rows carefully — they are the whole reason both tiers exist.**

- **Tier 2 has no passive components and no dc circuit theory at all.** Colour coding, resistivity,
  series/parallel reduction, Thevenin, Norton, mesh analysis, capacitors, inductors and transformers
  appear **only** in tier 1. That is 23 of its 100 pages, about a quarter of the course.
- **Tier 1 stops at the FET.** It has no $h$-parameter analysis, no feedback theory, no frequency
  response, no fabrication, and it never defines $g_m$ — so it cannot compute a single amplifier
  gain in V/V. Those come **only** from tier 2, files `15`, `16`, `17` and `14` §4.8.

---

## File register

### Tier 1 — the lecture notes (primary)

Cited **·J p33** — the PDF page. The document's own printed page number runs **one behind**
(PDF p33 shows printed 32), unbroken from PDF p2 (printed 1) to PDF p100 (printed 99). PDF p1 is a
download-service cover sheet with no course content.

| File | Pages | Size | Flags | Content |
|---|---|---|---|---|
| `01-matter-atoms-and-semiconductors.md` | ·J p2–p9 | 68 KB | 22 | Electronics defined; analogue and digital signals; states of matter and the first-20-elements table; electron theory, shells and the forbidden gap; exclusion principle; atomic number and weight; valence electrons and ionisation; conductors, insulators, semiconductors and their band gaps; intrinsic silicon; **P-type and N-type doping**; $Q = It$ |
| `02-resistors-and-dc-network-theorems.md` | ·J p10–p23 | 87 KB | 28 | Voltage, power, resistivity; the four-band colour code with its full table; Ohm's law; series, parallel and combined networks; power rating; source internal resistance and the constant-current source; **Thevenin** and **Norton** with worked examples; mesh analysis; resistor types. **The most arithmetic-dense range in the course** |
| `03-capacitors-inductors-and-transformers.md` | ·J p24–p32 | 63 KB | 20 | Capacitance and the parallel-plate formula; charging and discharging; series and parallel combination; $\tfrac12CV^2$; capacitive reactance; the capacitor-type catalogue; inductors, self and mutual inductance; transformers — construction, phase, efficiency, losses, turns ratio, one worked example |
| `04-diodes.md` | ·J p33–p45 | 72 KB | 23 | Depletion layer and barrier potential; forward and reverse bias; the V–I characteristic; the diode static equation; **Thevenin reduction of a diode circuit**; $r_{dc}$ and $r_{ac}$; the **dc load line and Q point**; the three diode models; two worked examples; LED, photodiode, tunnel diode, varactor |
| `05-rectifiers-filters-and-regulation.md` | ·J p46–p56 | 80 KB | 18 | The power-supply block diagram; half-wave, centre-tap and bridge rectifiers, each derived from the integral through to efficiency and ripple factor; **the capacitor, choke-input and Π filters**; zener characteristic and equivalent circuits; a worked regulator; zener clipping |
| `06-bipolar-junction-transistors.md` | ·J p57–p83 | 110 KB | 29 | NPN and PNP construction and operation; $I_E = I_C + I_B$; CB, CE and CC with $\alpha$, $\beta$ and $\theta$; leakage and thermal runaway; **all nine static characteristic families**; **six biasing methods**; the CE amplifier and its capacitors; dc and ac equivalent circuits; dc and ac load lines; clipping; stability factor; a worked amplifier **design**; a worked Q-point example; two problems solved here |
| `07-field-effect-transistors.md` | ·J p84–p100 | 97 KB | 19 | JFET construction, operation and pinch-off; $I_{DSS}$, $V_P$, $V_{GS(\text{off})}$; drain and transfer characteristics; Shockley's equation; DE MOSFET; enhancement-only NMOS and the $K$ square law; **four JFET bias schemes and two E-MOSFET schemes** with four worked examples; FET amplifiers; CS, CD and CG configurations |

### Tier 2 — the lesson documents (supporting)

Cited **·L3 p12** — lesson 3, PDF page 12.

| File | Source | Pages | Size | Flags | Content |
|---|---|---|---|---|---|
| `11-diodes.md` | L1 | 18 | 87 KB | 17 | Barrier voltage from doping; the diode equation with $\eta$; $r_B$, $r_j$, $r_{ac}$; **Zener diode, biasing and voltage regulation — seven circuits**; LED; varactor |
| `12-rectifiers.md` | L2 | 26 | 133 KB | 43 | The full seven-parameter set three times over — including **PIV, TUF and form factor, which tier 1 never gives**; Fourier content; three-phase rectifiers; clippers, clampers, voltage multipliers; tunnel diode |
| `13-bipolar-junction-transistor.md` | L3 | 25 | 150 KB | 52 | The same BJT ground as `06`, with $K_\beta$, the β-rule and the solved bias formulas tier 1 leaves as loop equations |
| `14-field-effect-transistors.md` | L4 | 24 | 115 KB | 36 | The same FET ground as `07`, **plus $g_m$, $r_d$, $\mu$, the FET load line and Q point, the Miller effect, and the three computable configuration gains** |
| `15-fabrication-and-integrated-circuits.md` | L5 | 23 | 116 KB | 21 | **Sole source.** Crystal growth, the seven wafer-fabrication processes, packaging, the seven-mask bipolar and five-mask NMOS flows |
| `16-h-parameters-and-bjt-amplifiers.md` | L6 | 26 | 76 KB | 12 | **Sole source.** The two-port model; $A_I$, $Z_i$, $A_V$, $Y_o$, $A_{VS}$, $A_{IS}$; CB/CE/CC; the simplified model; three problems solved exactly and approximately |
| `17-multistage-feedback-frequency-response.md` | L7 | 27 | 124 KB | 48 | **Sole source.** The feedback equation and its five consequences; four topologies; cascading and coupling; the decibel; bandwidth, half-power points, the Miller effect, $f_\alpha$, $f_\beta$, $f_T$ |

### Tier 3 and the cross-cutting files

| File | What it is |
|---|---|
| `_reference-decks.md` | Page-by-page map of the four slide decks, RD1–RD4, 59 pages. **Not verified** |
| `_nomenclature.md` | Every symbol with meaning and units, the **47-row clash table**, and the cross-tier translation table. Open this before any calculation you are unsure of |
| `_formula-sheet.md` | Every equation in one place, all in **corrected** form, tagged to source, with a concordance of the results both tiers give and a 25-item memorise list |
| `_verification-log.md` | All 388 flagged defects, the eleven recurring failure modes, and the **cross-tier resolutions** |
| `../sources/SOURCES.md` | Manifest of the raw PDFs. Not tracked |

### Numbering and splitting

Tier 1 takes `01`–`07`, tier 2 takes `11`–`17`. **The numbers encode precedence, not teaching order** —
teaching order is below.

**One source document = one topic file.** Split into `NNa` / `NNb` only when a document covers **two
genuinely independent themes** *and* exceeds ~25 KB. Every file here exceeds 25 KB and **none was
split**: each is one continuous argument, and splitting would put a flag and the section that
consumes it in different files.

## Tag legend

`[def]` definition · `[derivation]` step-by-step working · `[eq]` key equation (`[eq: name]`
cross-references the formula sheet) · `[ex]` worked example with the source's own numbers ·
`[exercise]` unsolved problem set in the source · `[fig]` figure described from the rendered page ·
`[table]` tabulated data · `[hist]` historical note · `[added]` **supplied here, not in any source** ·
`·J p33` / `·L3 p12` / `·RD2 p7` provenance · `⚠ VERIFY` flagged defect · `⚠ ILLEGIBLE` unreadable ·
`⚠ REDACTED` text destroyed by an opaque block in the primary PDF.

---

## Teaching order

Follow tier 1, and pull tier 2 in where the arrow says so.

- `01` matter and semiconductors → `02` dc circuits → `03` passives
- → `04` diodes → `05` rectifiers and regulation
  - `05` needs **`11` § Zener** alongside it, and **`12`** for PIV, TUF, clampers and multipliers
  - `04` needs **`11`** for the barrier-voltage formula and the diode parameters
- → `06` BJT — with **`13`** for $K_\beta$, the β-rule and the solved bias forms
- → `16` $h$-parameters → `17` feedback and frequency response *(tier 2 only; tier 1 has neither)*
- → `07` FET — with **`14` §4.8 and §4.12** for $g_m$, $r_d$, $\mu$ and the three gains
- `15` fabrication is independent; teach it any time after `07`

**Five points where the order matters:**

1. **`01` before `04`.** The diode files name p-type and n-type as an assumed prerequisite; `01` is
   the only place in the primary notes that supplies it.
2. **`03` before `05`.** The filter section needs capacitive reactance and the turns ratio.
3. **`11` § Zener immediately after `05`.** Tier 1 gives the zener characteristic and one worked
   regulator; it gives **no regulator design** — no $I_{z\min}$–$I_{z\max}$ band, no sizing of $R$.
   That is entirely in `11` §1.8–§1.10.
4. **`16` before `17`.** The feedback material assumes the small-signal picture.
5. **Inside `17`, teach §7.25 before §7.10.** The source uses $f_1$ and $f_2$ fourteen pages before
   it defines them.

**Three sections must be read before any calculation in their file:**

- **`07` §7.4 and `14` §4.4 — the $V_P$ sign trap.** Both sources use $V_P$ with both signs.
  Substituting the positive one into Shockley's equation returns a drain current larger than
  $I_{DSS}$, which is impossible.
- **`17` §7.2 — the $\beta$ clash.** In `17`, $\beta$ is the feedback fraction, not the transistor
  current gain. Both meanings appear within eight lines of each other on ·L7 p11.
- **`_nomenclature.md` § clash table** — 47 rows, and the top five change answers rather than merely
  confusing.

---

## Triage — where the marks are

Judged from each source's own weighting: how many worked examples it spends on a result, and which
results its exercises use. **Tier 1 sets the priority, because it is what the course teaches.**

**Highest value**

| Topic | File | Why |
|---|---|---|
| Combined series–parallel network reduction | `02` ·J p14–p15 | A page and a half, fourteen steps, worked in full. The most CAT-shaped question in the course |
| The colour code | `02` ·J p11–p12 | Complete table plus five decode exercises. Pure marks — but two of the five carry defects |
| Thevenin and Norton | `02` ·J p16–p22 | Stated as procedures, then worked. Reused for divider bias in `06` |
| Diode Thevenin → load line → Q point | `04` ·J p35–p40 | Set up over two pages, stated as a rule, then executed on numbers. Reused verbatim for the BJT load line |
| The rectifier derivations | `05` ·J p47–p49 | The same four integrals done twice. "Derive the efficiency of a half-wave rectifier" is the single most predictable question in the range |
| The six biasing circuits | `06` ·J p70–p74 | Five near-identical treatments; a CAT can lift any of them |
| dc and ac load lines, Q point, clipping | `06` ·J p76–p80 | Short, mechanical, reliably assessed |
| The two worked amplifier examples | `06` ·J p81–p83 | Design and analysis, one each. Reproduce both from memory |
| The four FET bias schemes and $K$ from the data sheet | `07` ·J p92–p97 | Every number in the FET range lives here |
| Zener regulator circuits | `11` §1.8–§1.10 | Seven circuits sharing one node equation. Tier 1 has no equivalent |
| The $h$-parameter gain set | `16` §6.8–§6.20 | The whole file converges on it; three problems apply it twice each |
| The feedback equation family | `17` §7.4–§7.10 | 16 of that file's 23 worked examples |

**Teach for use, not reproduction**

- `06` §6.31 and `13` §3.19 — the stability-factor derivations. Learn to evaluate, not to derive.
- `17` §7.9 — the multistage feedback sensitivity derivation. State the conclusion, skip the calculus.
- `16` §6.18's error bound. Read once for the 5 % figure.
- `04` §4.6 — the diode static equation is quotable but is **never used in a calculation** anywhere
  in tier 1.

**Descriptive, so learn the lists**

`15` in its entirety; `03` ·J p27–p28 (the capacitor catalogue); `02` ·J p23 (resistor types);
`04` ·J p41–p45 (the four special diodes); `07` ·J p98–p100 (configurations and applications);
`17` §7.17 and §7.20 (coupling methods). Almost no arithmetic — the value is in ordered lists and
sketchable figures. `15` §5.24 collects every list in that file onto one page for this reason.

**Lowest value**

`06` ·J p68–p70 — the three common-collector characteristic families. `07` ·J p91's static
characteristics, which are **the wrong figure for the device they label** (JV7.2, JV7.3). `01`'s Bohr
postulates, stated and then never used again.

---

## ⚠ Gap map

### Tier 1 — the primary notes are physically damaged in places

| Gap | Where | Status |
|---|---|---|
| **Opaque redaction blocks** over text on **eleven pages** — ·J p35, p40, p41, p42, p44, p53, p55, p58, p87, p88, p89 | throughout | Contrast recovery was tested; **there is nothing underneath**. Seven were inferred with certainty from context and are labelled `[added]`; the rest are marked `⚠ REDACTED` and left open. Full list in `_verification-log.md` |
| **·J p25** — body absent; only the sub-heading "Charging" survives | `03` | ❌ RC charging supplied `[added]` as standard theory |
| **·J p26** — upper half absent; the discharging figure and text | `03` | ❌ RC discharging supplied `[added]` |
| **·J p30** — **entirely blank**; printed page 29 is gone outright | `03` | ❌ Almost certainly carried the transformer heading and opening. **Needs a screenshot** |
| **Section headings absent** at ·J p31, p33, p46, p57, p65, p73, p79, p81, p84, p85, p94, p95 | all | Lost with the blank space above them. Editorial titles used, marked as such |
| **No contents page, no syllabus, no objectives, no reference list** | — | The document opens straight into body text and **ends mid-topic on ·J p100** inside its own applications list |
| **$h$-parameter analysis** — a symbol table on ·J p61 and nothing else | — | ✅ **Closed by `16`** |
| **Feedback theory, multistage amplifiers, frequency response** | — | ✅ **Closed by `17`** |
| **Fabrication and integrated circuits** — two passing lines | — | ✅ **Closed by `15`** |
| **$g_m$, $r_d$, $\mu$** — "forward trans-conductance" named once in a purchase checklist, never defined | `07` | ✅ **Closed by `14` §4.8, §4.12.** Without them tier 1 cannot compute any amplifier gain in V/V |
| **PIV, TUF and form factor** — never given for any rectifier topology | `05` | ✅ **Closed by `12`.** Without PIV, tier 1 gives no reason to prefer a bridge over a centre-tap |
| **Zener regulator design** | `05` | ✅ **Closed by `11` §1.8–§1.10** |

### Tier 2 — four of the seven lesson PDFs are missing pages

| Gap | Where | Status |
|---|---|---|
| Six-phase half-wave and three-phase bridge rectifiers, promised in a list of eight | `12` | ❌ Not delivered |
| Example 55.2, referenced by Example 55.5 | `12` | ⚠️ Data reconstructed and labelled |
| Printed pp. 2194–2195 — the CE half of §57.12 and **Examples 57.2, 57.3** | `13` | ⚠️ Leakage relations reconstructed `[added]`; **·J p63–p64 derives them properly** |
| Printed pp. 2205–2222 — **§57.24, the β-rule**, cited twice and never stated | `13` | ❌ |
| Printed p. 2233 — Fig. 58.25 and the rest of Example 58.12 | `13` | ⚠️ ·J p83's Problem 1 is a near-twin; worked in full in `06` §6.34 |
| Articles 67.3–67.12 — IC classification and the **scales of integration** (SSI…ULSI) | `15` | ❌ LSI/VLSI/ULSI are used without ever being defined |
| Printed pp. 2318–2322 — §61.3–61.5 and Examples 61.1–61.4 | `17` | ❌ |
| Printed pp. 2302–2306 — including **the definition of the decibel** | `17` | ✅ Supplied `[added]` |
| Tutorial 60.1 Q7, cut off mid-sentence | `17` | ⚠️ Partial `[added]` solution |
| Darlington pair, differential amplifier, op-amp feedback — listed in the objectives | `17` | ❌ No sections exist |
| Tunnel diode and the diode load line, promised in L1's outline | `11` | ✅ Closed — by `12` §2.16 and by **·J p36–p40**, which teaches the load line properly |

### Pages that need a screenshot

Only **three** in 328:

1. **·J p30** — entirely blank. Printed page 29 of the lecture notes.
2. **·J p41** — two redaction blocks over the LED semiconductor material names. Widths fit spelled-out
   compound names; which two cannot be determined.
3. **·L5 p16, Fig. 67.20** — a washed-out photograph that cannot be identified at any resolution.

Everything else in all 328 pages was legible.

---

## Verification summary — 388 flags

Full detail in `_verification-log.md`. **158 substantive** and **230 cosmetic**.

| Tier | Source | Substantive | Cosmetic | Total |
|---|---|---|---|---|
| 1 | `01` matter and semiconductors | 7 | 15 | 22 |
| 1 | `02` dc circuits | 7 | 21 | 28 |
| 1 | `03` passives | 8 | 12 | 20 |
| 1 | `04` diodes | 10 | 13 | 23 |
| 1 | `05` rectifiers | 7 | 11 | 18 |
| 1 | `06` BJT | 13 | 16 | 29 |
| 1 | `07` FET | 10 | 9 | 19 |
| | **Tier 1 subtotal** | **62** | **97** | **159** |
| 2 | `11`–`17` | 96 | 133 | 229 |
| | **Total** | **158** | **230** | **388** |

**ID schemes differ between tiers and must not be confused.** `JV3.2` is the second substantive flag
in **primary file 03**; `V3.2` is the second substantive flag in **Lesson 3**. They are different
flags about different documents.

**The two sources fail in opposite ways.** Tier 2 is a photographed textbook, so its defects are
rendering faults — lost brackets, dropped prefixes, glyphs that did not survive the scan. Tier 1 is
someone's own compilation, so its defects are **prose and figure faults** — a definition that
describes a different quantity, a figure copied from a neighbouring device and never adapted, a
correct answer printed beside a wrong middle line.

### The eleven recurring failure modes

Each has a check the reader can repeat; full lists in the log.

1. **Unit-prefix and unit-glyph loss** — mA for µA, Ω rendering as roman W. *Form $\beta = I_C/I_B$
   from the printed numbers; it must land between 20 and 300.*
2. **Dropped exponents and lost $\sqrt2$ or $\pi$ factors.** *Evaluate the printed expression exactly
   as written and compare it with the answer beside it.*
3. **Self-referential equations.** *If the left-hand symbol also appears on the right, the label is
   wrong.* Nine in tier 2; almost absent from tier 1.
4. **Mislabelled figure axes and substituted panels** — the largest family in tier 1. *Check the axis
   unit before reading any value off a graph.*
5. **Symbol collisions inside one derivation**, including symbols that exist nowhere else
   ($R_\beta$, $V_{DSS}$, $f_0$).
6. **Arithmetic contradicted by the page's own next line** — 29 of tier 1's 62 substantive flags.
   *Read one line further before trusting a number.*
7. **Glyphs that did not survive the page** — $\Delta$, $\beta$, $\eta$, minus set as $\times$. In
   tier 1 the same mechanism swallows whole sub-expressions.
8. **Dangling cross-references and absent material.** Tier 1 has no dangling references; it has the
   absence instead — five missing headings, a table with no column headings, four clipped lines.
9. **A block copied from the neighbouring case and never adapted.** *New in tier 1.* ·J p91
   illustrates *and* narrates the enhancement-only MOSFET using the DE MOSFET figure and the JFET
   bullets. *Ask whether the figure's labels actually belong to the device named above it.*
10. **The right answer printed beside the wrong middle line.** *New in tier 1* — 18 of its 62. The
    signature fault, and invisible to answer-checking. *Redo the middle line, not just the result.*
11. **A definition that describes a different quantity.** *New in tier 1* — 16 of its 62. Permittivity
    defined as permeability; self-inductance defined as mutual inductance; charge defined as current;
    the photodiode's mechanism run backwards. *Check the units named in the definition against the
    units of the quantity being defined.*

### Cross-tier resolutions — where one source settles the other

This is the most valuable thing two independent sources buy. Full table in the log.

- **Tier 1 right, tier 2 wrong — 8 cases**, including $\alpha = I_C/I_E$ (·J p60 and p63 print it
  correctly where **V3.1** flags the lesson document for inverting it) and the $-1$ **outside** the
  bracket in the diode equation (·J p35, where **V1.3** flags the lesson document for putting it
  inside, five times).
- **Tier 2 right, tier 1 wrong — 10 cases**, including Boltzmann's constant (·J p35 prints
  $1.38\times10^{-28}$, flagged **JV4.2**; the lesson document has $1.38\times10^{-23}$) and the
  enhancement-only MOSFET characteristics.
- **Both carry the same inherited defect — 3 cases.** The $V_P$ sign collision in Shockley's equation
  and the LED luminosity claim. **A second source is not confirmation here** — for the FET material
  the two documents are not independent at all: three of tier 1's four FET worked examples *are* the
  tier-2 textbook's own examples, which is exactly why they share the defect.

### Three habits worth teaching from this

1. **Check dimensions before substituting.** A gain is dimensionless; an exponent is dimensionless; a
   divider ratio lies between 0 and 1. Those three checks alone catch a dozen flags on sight.
2. **Redo the middle line.** Tier 1's most common fault leaves the final answer correct, so checking
   the answer proves nothing.
3. **Check what a figure is a figure *of*.** Four of tier 1's substantive flags are a picture of the
   wrong device.

---

## Provenance notes

- **All 328 pages were rendered to images and read from the render**, never from a text layer. The
  primary PDF has **no text layer at all**; one lesson document has none either; and four more are
  photographs of printed pages whose OCR mangles mathematics silently.
- **Every numerical claim was recomputed.** Where a source's answer and the recomputed answer differ,
  both appear in the flag.
- **Every unsolved exercise was solved here**, numerically verified, and tagged `[added]`.
- **Printed page numbers differ from PDF page numbers** in the primary notes (offset 1) and in the
  four scanned lesson documents (offset in the thousands). Citations always use the **PDF** page;
  each file states its printed range once, near the top.
- **Nothing was invented.** Three pages need a screenshot and are named above; every other gap is
  recorded rather than filled.

## No past papers yet

There is no `past-papers/` folder for this unit. When a CAT or exam arrives, transcribe it into
`past-papers/` **inside this knowledge base** — see `../../docs/kb-format.md` § Folder layout —
following the pattern in `../../fluid-flow/knowledge-base/past-papers/`, work the
solutions, and add a past-paper register here. **The mark distribution should then replace the triage
table above**, which currently rests on the sources' own weighting alone.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
