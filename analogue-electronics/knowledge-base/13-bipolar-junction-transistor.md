---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "13 — The Bipolar Junction Transistor (supporting)"
source: "L3 — 'Lesson 3 Notes Bipolar Junction Transistor .pdf', 25 pp."
pages: "1-25"
tier: supporting
file_role: topic
subtopics:
  - "BJT structure: PNP and NPN sandwiches, emitter/base/collector doping and geometry, circuit symbols"
  - "FR biasing and the polarity rule; double-subscript voltage notation"
  - "the three transistor currents and Kirchhoff's current law for a BJT"
  - "the three configurations: common-base, common-emitter, common-collector"
  - "current gains: alpha (CB), beta (CE), (1 + beta) (CC), and the relations between them"
  - "leakage currents: collector-base with emitter open, collector-emitter with base open"
  - "worked examples 57.1 and 57.4-57.12 with leakage"
  - "CB static characteristics: test circuit, input, output and transfer curves"
  - "CE static characteristics: test circuit, input, output and transfer curves; saturation, cut-off, breakdown"
  - "CC static characteristics"
  - "circuit-drawing conventions: two-battery form versus single-rail form"
  - "CB, CE and CC dc bias formulas"
  - "need for biasing; what shifts the Q-point; thermal runaway"
  - "stability factor S and beta sensitivity"
  - "six biasing methods: base bias, emitter feedback, collector feedback, both feedbacks, two-supply emitter bias, voltage divider"
  - "voltage divider bias by inspection, by Thevenin and by the beta-rule"
  - "dc load line, Q-point and signal swing on the output characteristics"
  - "ac load line and peak-signal handling capacity"
key_equations: [ie-ib-ic, alpha-dc, beta-dc, alpha-beta, cc-current-gain, current-relations, current-ratio, icbo-iceo, ic-with-leakage, cb-rin, cb-rout, ce-rin, beta-ac-graph, ce-rout, cb-emitter-current, cb-vcb, ce-base-current, ce-vce, two-supply-ie, cc-formulas, stability-factor, stability-factor-general, beta-sensitivity, s-cb, s-ce, ic-sat-general, emitter-feedback-ic, kbeta-emitter-feedback, collector-feedback-ic, kbeta-collector-feedback, both-feedbacks-ic, kbeta-both-feedbacks, divider-v2, divider-ie, divider-vce, kbeta-divider, thevenin-divider, thevenin-ib, thevenin-ie, beta-rule-vb, dc-load-line, power-in-load, ac-load-line, signal-handling]
prerequisites: ["01-diodes (P-N junction, forward and reverse bias, majority and minority carriers, forward characteristic, reverse saturation current)"]
leads_to: ["04-field-effect-transistors (the other transistor family; the source calls it chapter 13)", "transistor amplifiers: small-signal models, h-parameters, ac load line in use"]
verification_flags: 52
tags: [bjt, transistor, pnp, npn, biasing, alpha, beta, common-base, common-emitter, common-collector, leakage-current, static-characteristics, load-line, q-point, stability-factor, beta-sensitivity, voltage-divider-bias, thermal-runaway]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·L3 pN = provenance (which PDF page of Lesson 3 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 03 — The Bipolar Junction Transistor

Scope: the whole of L3, 25 PDF pages. Builds the BJT from two back-to-back junctions, fixes the
biasing and polarity rules, defines the three configurations and their current gains, works through
leakage, reads all three families of static characteristics, sets out the dc bias formulas for CB,
CE and CC, then turns to bias stability — stability factor, beta sensitivity, the six biasing
methods — and finishes on the dc and ac load lines.

---

## 3.0 What this document is, and where its gaps are

**L3 is not a lecture handout. It is a scan of two consecutive chapters of a printed
electrical-technology textbook**, bundled into one PDF. That matters for three reasons: the
material carries its own section numbering, the worked examples are numbered in the book's scheme,
and **two blocks of pages are missing from the bundle**.

[table] **Page map — PDF page against the book's printed page and chapter**

| PDF pages (·L3) | Printed pages | Chapter | Book sections covered |
|---|---|---|---|
| p1–p6 | 2188–2193 | 57 — Bipolar Junction Transistor | 57.1 – 57.12 (start) |
| *(missing)* | **2194–2195** | 57 | rest of 57.12, **57.13**, Examples **57.2** and **57.3** |
| p7–p15 | 2196–2204 | 57 | 57.13 (end) – 57.23 |
| *(missing)* | **2205–2222** | 57 end + 58 start | 57.24 (**the β-rule**) onwards; 58.1, 58.2 |
| p16–p25 | 2223–2232 | 58 — Load Lines and DC Bias Circuits | 58.3 – 58.16 (Example 58.12 breaks off) |

> ### ⚠ Three gaps to know about before working from this file
>
> 1. **Printed pages 2194–2195 are absent.** The extract jumps from §57.12's opening (CB leakage) on
>    ·L3 p6 straight to the tail of an $I_{CEO}$ calculation on ·L3 p7. **Examples 57.2 and 57.3 are
>    not in the extract**, nor is §57.13's opening or the CE-leakage half of §57.12. §3.10 below
>    reconstructs the standard leakage relations from the surviving fragments and marks every
>    reconstructed step `[added]`.
> 2. **Chapter 57 ends mid-example.** ·L3 p15 states Example 57.13 and stops; **Fig. 57.33 and the
>    solution are not in the extract**. Likewise §57.24, the "β-rule" that ·L3 p18 and p22 both lean
>    on, is on a missing page.
> 3. **Chapter 58 ends mid-example.** ·L3 p25 breaks off inside Example 58.12; **Fig. 58.25 is not in
>    the extract**, so the Q-point and the peak-to-peak swing it asks for cannot be completed. What
>    *is* determinable is worked in §3.27.
>
> Nothing in this file is invented to paper over those gaps. Where a value cannot be obtained from
> the pages supplied, it says so.

**Citation.** **·L3 p7** means PDF page 7 of Lesson 3, which is printed page 2196. Section references
in the form §57.7 or §58.11 are the **book's own** numbering, kept because the examples and figures
are numbered against it; §3.x are this file's own headings.

**A note on the render.** The PDF's embedded font drops two glyphs when the pages are rasterised: the
increment symbol $\Delta$ in body-text equations, and $\beta$ in figure annotations. Both are present
in the file's text layer. They are logged as **C3.2** and **C3.3** and the correct forms are given
wherever they occur, because a reader working from a printed copy will meet the same blanks.

---

## 3.1 What a bipolar junction transistor is ·L3 p1

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $E$, $B$, $C$ | emitter, base, collector terminals | — | — |
| $I_E$ | emitter current | A (usually mA) | 1–10 mA |
| $I_B$ | base current | A (usually µA) | 10–100 µA |
| $I_C$ | collector current | A (usually mA) | 1–10 mA |

[def] A **bipolar junction transistor** is two back-to-back P-N junctions formed in a single crystal
of semiconductor. The two junctions divide the crystal into three regions — **emitter**, **base**
and **collector** — and are named the **emitter–base (E/B) junction** and the **collector–base (C/B)
junction**. ·L3 p1

Two types exist, according to which material is the filling of the sandwich:

- **PNP** — a layer of N-type between two layers of P-type. ·L3 p1
- **NPN** — a layer of P-type between two layers of N-type. ·L3 p1

The device was invented at Bell Laboratories in **1947** by a team of three scientists; the first
transistor was not itself a bipolar junction device. ·L3 p1

Two broad uses, and the whole of analogue electronics sits on the first: ·L3 p1

1. as a **linear amplifier**, to boost an electrical signal;
2. as an **electronic switch**.

The other transistor family, the **field-effect transistor (FET)**, is treated in the book's
chapter 13 and is not part of this lesson. ·L3 p1

### The three regions, and why they are not interchangeable ·L3 p1–p2

[def] **Emitter** — **more heavily doped than any other region**, because its job is to supply
majority carriers (electrons in an NPN, holes in a PNP) into the base. ·L3 p1

[def] **Base** — the middle section. **Very thin, of the order of $10^{-6}\ \mathrm{m}$**, and **very
lightly doped**. ·L3 p1

[def] **Collector** — collects the majority carriers that came from the emitter and crossed the base.
**Physically larger than the emitter**, because it has to dissipate much more power. ·L3 p1–p2

> [added] The consequence the book draws next is worth holding onto: because the emitter and
> collector differ in both doping and size, **a transistor cannot be run backwards**. Swapping the
> emitter and collector leads does not give a working transistor. ·L3 p2

### The circuit symbols ·L3 p1

[fig ·L3 p1] **Fig. 57.1** has three panels.

**(a) PNP.** On the left, the structure: three touching rectangles labelled **P | N | P**, with the
lead marked *Emitter, E* entering the left-hand P block, *Collector, C* leaving the right-hand P
block, and *Base, B* dropping out of the middle N block. On the right, the symbol: a circle with a
vertical bar (the base) inside it, a lead from the bar going up-left to **E** and one going up-right
to **C**, and the base lead leaving the bottom to **B**. The **arrowhead sits on the emitter lead and
points inward, from E towards the base bar**.

**(b) NPN.** Same layout with the blocks reading **N | P | N**, and the **emitter arrowhead pointing
outward, from the base bar towards E**.

**(c)** A photograph of seven coloured LEDs in a row. A separate photograph at the top right of the
page, captioned *"Bipolar junction transistor"*, shows a small black three-lead device.

> ⚠ VERIFY **C3.1** ·L3 p1–p2 — the text on p2 states *"Fig 57.1 (c), shows the picture of C1815
> (front and the back view) transistor"*, but panel (c) is a row of coloured LEDs, not a C1815. The
> transistor photograph on the page is the unnumbered one at top right. A related mismatch: ·L3 p2's
> **Fig. 57.2(c)** is a photograph of a seven-segment LED display module, and the text says *"Also
> refer to the picture shown in Fig. 57.2 (c)"* in the middle of a discussion of transistor biasing.
> Nothing computed changes. See `_verification-log.md`.

[def] **What the arrowhead means.** The arrowhead is **always on the emitter, never on the
collector**, and it points along the **conventional** direction of current flow. ·L3 p1

- **PNP** — arrow points *from emitter to base*: the emitter is positive with respect to the base
  (and to the collector). ·L3 p1
- **NPN** — arrow points *from base to emitter*: the base (and the collector) is positive with
  respect to the emitter. ·L3 p1

> [added] **Memory hook, and it is the book's own.** Read the middle letter of the type name as the
> polarity of *base and collector relative to the emitter*: P**N**P → **N**egative; N**P**N →
> **P**ositive. This is §57.3 and it is set out in §3.2 below.

---

## 3.2 Biasing and the polarity rule ·L3 p2

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{EE}$ | dc emitter supply voltage | V | 10 V |
| $V_{CC}$ | dc collector supply voltage | V | 20–30 V |
| $V_{BB}$ | dc base supply voltage | V | 10 V |
| $V_{EB}$, $V_{BE}$ | emitter–base voltage (first subscript is the more positive terminal) | V | 0.3 V (Ge), 0.7 V (Si) |
| $V_{CB}$, $V_{BC}$ | collector–base voltage | V | 5–20 V |

[def] **FR biasing** — the biasing arrangement required for normal (active-region) operation: ·L3 p2

1. the **emitter–base junction is always forward-biased**, and
2. the **collector–base junction is always reverse-biased**.

**F**orward, then **R**everse — hence *FR*. ·L3 p2

[fig ·L3 p2] **Fig. 57.2** is a two-by-two array plus a photograph.

**Column (a), PNP.** Top: the block form — **P | N | P** with $I_E$ entering the left P block from a
battery $V_{EE}$ whose **positive** terminal faces the emitter, $I_C$ leaving the right P block into
a battery $V_{CC}$ whose **negative** terminal faces the collector, and $I_B$ leaving the base
downward into the node the two batteries share. Bottom: the identical circuit redrawn with the PNP
symbol in place of the blocks.

**Column (b), NPN.** The same two drawings with **N | P | N**, every current arrow reversed, and both
battery polarities reversed ($V_{EE}$ negative to the emitter, $V_{CC}$ positive to the collector).
A letter **A** is printed in the base branch of both (b) drawings.

**(c)** A photograph of a seven-segment LED display module (see **C3.1**).

**How the supplies do their work, in the book's own physical language (PNP):** the **P**ositive
terminal of $V_{EE}$ is tied to the **P**-type emitter so as to **P**ush holes into the base; the
**negative** terminal of $V_{CC}$ is tied to the collector so as to **pull** those holes through the
base. ·L3 p2

> **A transistor never conducts if its emitter–base junction is not forward-biased.** ·L3 p2
> The page's footnote adds the qualification that matters later: there would be no current *due to
> majority carriers*, but an extremely small current *due to minority carriers* still flows — the
> **leakage current**, §57.12, treated in §3.10. ·L3 p2

### §57.3 The important biasing rule ·L3 p2

[def] **PNP** — both collector and base are **negative** with respect to the emitter (the letter
**N** of Negative is the middle letter of P**N**P), and the **collector is more negative than the
base**. ·L3 p2

[def] **NPN** — both collector and base are **positive** with respect to the emitter (the letter
**P** of Positive is the middle letter of N**P**N), and the **collector is more positive than the
base**. ·L3 p2

[fig ·L3 p2] **Fig. 57.3** draws the transistor vertically. **(a) PNP:** collector at the top marked
$-\,-$, base at the left marked $-$, emitter at the bottom marked $+$; $V_{BC}$ spans base to
collector, $V_{EB}$ spans emitter to base. **(b) NPN:** collector $+\,+$, base $+$, emitter $-$;
$V_{CB}$ and $V_{BE}$ marked. **Fig. 57.4** repeats the same information with the transistor drawn
horizontally: PNP with $E$ marked $+$, $C$ marked $-\,-$, $B$ marked $-$, showing $V_{EB}$ and
$V_{BC}$; NPN with $E$ marked $-$, $C$ marked $+\,+$, $B$ marked $+$, showing $V_{BE}$ and $V_{CB}$.

> ⚠ VERIFY **C3.28** ·L3 p2 — the page spells *"emmitter"*. One of a set of spelling slips logged
> together as C3.28 (see §3.29). Nothing computed changes.

### The double-subscript convention ·L3 p3

[def] **The first subscript is the terminal that is more positive (or less negative).** ·L3 p3

So for the PNP of Fig. 57.3(a) the emitter–base potential difference is written $V_{EB}$ **and not**
$V_{BE}$, because the emitter is positive with respect to the base; and the base–collector
difference is written $V_{BC}$ **and not** $V_{CB}$, because the collector is the more negative of
the two. ·L3 p3

> [added] **This convention is not kept consistently later in the source.** §57.21 (·L3 p13) writes
> $V_{BE}$ and $V_{CB}$ for the PNP circuit of Fig. 57.23 whose own labels read $V_{EB}$ and
> $V_{BC}$ — logged as **C3.10**. In practice, read every $V_{XY}$ in this chapter as *the magnitude
> of the junction voltage*, and take the sign from the transistor type.

---

## 3.3 The three transistor currents ·L3 p3–p4

[eq: ie-ib-ic] The single most-used relation in the chapter. ·L3 p3

$$\boxed{\;I_E = I_B + I_C\;}$$

- $I_E$ — emitter current, A. **Flows into** the transistor.
- $I_B$ — base current, A. **Flows out of** it.
- $I_C$ — collector current, A. **Flows out of** it.

[derivation] The book derives it from Kirchhoff's current law with the sign convention *currents
into the transistor are positive, currents out of it are negative*: ·L3 p3

$$I_E + (-I_B) + (-I_C) = 0$$

$$I_E - I_B - I_C = 0$$

$$I_E = I_B + I_C$$

**This statement is true regardless of transistor type or transistor configuration.** ·L3 p3

**How the current splits.** Only about **1–2 %** of the emitter current becomes base current; the
remaining **98–99 %** becomes collector current. ·L3 p3

[fig ·L3 p3] **Fig. 57.5** shows the split twice over, for a PNP.

**(a) Common-base.** Left: the **P | N | P** block with a wide tapering arrow entering the left face
labelled $I_E$ at **100 %**, narrowing as a **2 %** branch labelled $I_B$ peels downward out of the
base, and leaving the right face as $I_C$ at **98 %**. $V_{EE}$ sits in the emitter–base loop,
$V_{CC}$ in the collector–base loop. Right: the same circuit with the PNP symbol, the input current
labelled simply $I$ at 100 %, $I_C$ at 98 % out of the collector and $I_B$ at 2 % out of the base.

**(b) Common-emitter.** The same block turned on end — **P** (collector) on top, **N** (base) in the
middle, **P** (emitter) at the bottom. $I_E$ enters from below at **100 %**, $I_B$ leaves sideways to
the left at **2 %**, $I_C$ leaves upward at **98 %**. $V_{BB}$ sits in the base loop and $V_{CC}$ in
the collector loop. Right: the same with the PNP symbol.

> [added] The percentages are the figure's own and are consistent with $\alpha \approx 0.98$ — see
> §3.5. They are illustrative, not a specification.

### §57.5 Summing up — the four guideposts ·L3 p4

The book compresses everything so far into four statements, and they are worth memorising verbatim:

1. **Conventional current flows along the arrow; electrons flow against it.** ·L3 p4
2. **The E/B junction is always forward-biased.** ·L3 p4
3. **The C/B junction is always reverse-biased.** ·L3 p4
4. $I_E = I_B + I_C$. ·L3 p4

**Note.** Leakage currents have been left out of everything up to this point; they enter at §57.12
(§3.10 here). ·L3 p4

---

## 3.4 The three circuit configurations ·L3 p4

[def] A transistor is a **three**-terminal device, not a four-terminal one, so **one terminal must be
common to the input circuit and the output circuit**. Which one is chosen names the configuration.
·L3 p4

| Configuration | Common terminal | Input | Output |
|---|---|---|---|
| **Common-base (CB)** | base | emitter–base | collector–base |
| **Common-emitter (CE)** | emitter | base–emitter | collector–emitter |
| **Common-collector (CC)** | collector | base–collector | emitter–collector |

Because the common electrode is usually grounded, the three are also called **grounded-base**,
**grounded-emitter** and **grounded-collector**. ·L3 p4

[fig ·L3 p4] **Fig. 57.6** draws all three for a PNP, each as a transistor with two input terminals
on the left marked *I/P* and two output terminals on the right marked *O/P*, the common electrode
running along the bottom to a ground symbol.

- **(a) CB** — $E$ at top left, $C$ at top right, **$B$ at the bottom, grounded**; input across E–B,
  output across C–B.
- **(b) CE** — $B$ at the left, $C$ at the top, **$E$ at the bottom, grounded**; input across B–E,
  output across C–E.
- **(c) CC** — $B$ at the left, $E$ at the top, **$C$ at the bottom, grounded**; input across B–C,
  output across E–C.

---

## 3.5 CB configuration and $\alpha$ ·L3 p4–p5

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $\alpha_{dc}$, $\alpha$ | dc common-base current gain | dimensionless | 0.95–0.999 |
| $\alpha_{ac}$ | ac (incremental) common-base current gain | dimensionless | ≈ $\alpha_{dc}$ |
| $-h_{FB}$ | the same quantity in $h$-parameter notation (dc) | dimensionless | — |
| $-h_{fb}$ | the same quantity in $h$-parameter notation (ac) | dimensionless | — |
| $I_{CBO}$ | collector-to-base leakage with the emitter open | A (µA) | 5–10 µA |

In CB, **$I_E$ is the input current and $I_C$ is the output current**; the signal goes in between
emitter and base and comes out between collector and base. ·L3 p4

[def] **dc alpha** is the ratio of collector current to emitter current. The book first writes it
with the sign convention of §3.3 in force ($I_E$ into the device, $I_C$ out of it): ·L3 p4

$$\alpha_{dc} = \frac{-I_C}{I_E}$$

and its footnote gives the accurate version, which anticipates §57.12: ·L3 p4

$$\alpha_{dc} = \frac{I_C - I_{CBO}}{I_E}$$

[eq: alpha-dc] Dropping the sign, since only magnitudes matter in practice: ·L3 p4–p5

$$\boxed{\;\alpha = \frac{I_C}{I_E}\;}\qquad\Longleftrightarrow\qquad \boxed{\;I_C = \alpha I_E\;}$$

> ### ⚠ VERIFY **V3.1** ·L3 p4 — $\alpha$ is printed upside down
>
> The page prints: *"If we write adc simply as $\alpha$, then $\alpha = I_E/I_C$."*
>
> **Correct form:**
> $$\boxed{\;\alpha = \frac{I_C}{I_E}\;}$$
>
> **Why.** Three checks on the same two pages contradict the printed version. (i) Two lines above,
> the page itself defines $\alpha_{dc} = -I_C/I_E$; dropping the sign gives $I_C/I_E$, not its
> reciprocal. (ii) The very next sentence says $\alpha$ *"ranges from 0.95 to 0.999"* — but
> $I_E/I_C = 1/\alpha \approx 1.01$–$1.05$, always **greater than one**. (iii) §57.9 on ·L3 p5 prints
> $\alpha = I_C/I_E$. See `_verification-log.md`.

**Other names for the same number.** $\alpha_{dc}$ is the **forward current transfer ratio**,
written $-h_{FB}$ — subscript **F** for *forward*, **B** for *common-base*. ·L3 p4

[def] **ac alpha** is the ratio of the *change* in collector current to the *change* in emitter
current, also called the **short-circuit gain**, written $-h_{fb}$: ·L3 p5

$$\alpha_{ac} = \frac{-\Delta I_C}{\Delta I_E}$$

**Upper-case subscript FB means the dc value; lower-case fb means the ac value.** ·L3 p5

**For all practical purposes** $\alpha_{dc} = \alpha_{ac} = \alpha$. ·L3 p5

> ⚠ VERIFY **C3.2** ·L3 p5 — the $\Delta$ symbol does not render on the page: $\alpha_{ac}$ prints as
> $\dfrac{-I_C}{I_E}$ and $\beta_{ac}$ as $\dfrac{I_C}{I_B}$, both without increments, which makes
> the ac definitions look identical to the dc ones. The PDF's text layer carries $\Delta I_C/\Delta I_E$ and $\Delta I_C/\Delta I_B$, and the prose beside them says *"the ratio of **change** in
> collector current to the **change** in emitter current"*, so the increments are intended. **The
> same dropout affects $R_{in}$ and $R_{out}$ on ·L3 p8, $\alpha_{ac}$ on ·L3 p9, and $R_{in}$ and
> $\beta_{ac}$ on ·L3 p10.** See `_verification-log.md`.

**What $\alpha$ is for.** It measures the quality of the transistor: the higher $\alpha$, the more
closely the collector current equals the emitter current. Its value ranges from **0.95 to 0.999**,
and it applies **only to the CB configuration**. ·L3 p4–p5

[eq] Since $I_C = \alpha I_E$, the base current follows immediately: ·L3 p5

$$\boxed{\;I_B = I_E - \alpha I_E = (1-\alpha)\,I_E\;}$$

[fig ·L3 p5] **Fig. 57.7** is the CB circuit annotated with those two results. Left: the **P | N | P**
block, $I_E$ entering the emitter, a stream labelled $\alpha I_E$ continuing through to the collector
and out as $I_C = \alpha I_E$, and $I_B = (1-\alpha)I_E$ dropping out of the base. $V_{EE}$ in the
emitter loop, $V_{CC}$ in the collector loop. Right: the same with the PNP symbol.

### [ex] Example 57.1 — $\alpha$ from two current readings ·L3 p5

*(Electronics-II, Punjab Univ. 1992)*

**Statement.** The following current readings are obtained on a transistor connected in CB
configuration: $I_E = 2\ \mathrm{mA}$ and $I_B = 20\ \mathrm{mA}$. Compute $\alpha$ and $I_C$.

> ### ⚠ VERIFY **V3.2** ·L3 p5 — the base current is printed in the wrong unit
>
> The statement prints $I_B = 20\ \mathrm{mA}$. **It must be $I_B = 20\ \mathrm{\mu A}$.**
>
> **Why.** The page's own solution substitutes $20 \times 10^{-6}\ \mathrm{A}$. Worked as printed,
> $I_C = I_E - I_B = 2 - 20 = -18\ \mathrm{mA}$ — a negative collector current, which is impossible,
> and $\alpha = -9$. See `_verification-log.md`.

**Solution** (the page's own, with the unit corrected)

$$I_C = I_E - I_B = 2\times10^{-3} - 20\times10^{-6}$$

$$I_C = 1.98\ \mathrm{mA}$$

$$\alpha = \frac{I_C}{I_E} = \frac{1.98}{2} = 0.99$$

*[added] Verified: $0.002 - 0.00002 = 0.00198\ \mathrm{A}$ ✓; $1.98/2 = 0.99$ ✓. Sanity check —
$\alpha = 0.99$ sits inside the stated 0.95–0.999 band, and $I_B/I_E = 1\,\%$, inside the stated
1–2 % band.*

---

## 3.6 CE configuration and $\beta$ ·L3 p5

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $\beta_{dc}$, $\beta$ | dc common-emitter current gain | dimensionless | 50–300 (up to 500) |
| $\beta_{ac}$ | ac (incremental) common-emitter current gain | dimensionless | ≈ $\beta_{dc}$ |
| $h_{FE}$ | the same quantity in $h$-parameter notation (dc) | dimensionless | — |
| $h_{fe}$ | the same quantity in $h$-parameter notation (ac) | dimensionless | — |

In CE, the signal goes in between **base and emitter** and comes out between **collector and
emitter**, so **$I_B$ is the input current and $I_C$ is the output current**. ·L3 p5

[eq: beta-dc] [def] **dc beta** is the ratio of dc collector current to dc base current: ·L3 p5

$$\beta = \frac{-I_C}{-I_B} = \frac{I_C}{I_B} \qquad\Longleftrightarrow\qquad
\boxed{\;I_C = \beta I_B\;}$$

It is the **common-emitter dc forward transfer ratio**, written $h_{FE}$. **$\beta$ can be as high as
500.** ·L3 p5

[def] **ac beta**, written $h_{fe}$: ·L3 p5

$$\beta_{ac} = \frac{\Delta I_C}{\Delta I_B}$$

*(the $\Delta$ symbols do not render on the page — see **C3.2**)*

[eq] Combining $I_E = I_B + I_C$ with $I_C = \beta I_B$: ·L3 p5

$$I_E = I_B + I_C = I_B + \beta I_B$$

$$\boxed{\;I_E = (1+\beta)\,I_B\;}$$

[fig ·L3 p5] **Fig. 57.8** shows the CE current paths twice. **(a) PNP:** the symbol drawn with the
base to the left, $I_B$ leaving the base to the left, $I_C$ leaving the collector upward, $I_E$
entering the emitter from below; a battery in the base loop and one in the collector loop, with the
emitter node grounded. **(b) NPN:** the identical drawing with every arrow reversed and both battery
polarities reversed.

---

## 3.7 The relation between $\alpha$ and $\beta$ ·L3 p5–p6

[derivation] Start from the two definitions. ·L3 p5–p6

$$\beta = \frac{I_C}{I_B}, \qquad \alpha = \frac{I_C}{I_E}$$

$$\frac{\beta}{\alpha} = \frac{I_C/I_B}{I_C/I_E} = \frac{I_E}{I_B}$$

Now substitute $I_B = I_E - I_C$:

$$\beta = \frac{I_C}{I_E - I_C} = \frac{I_C/I_E}{I_E/I_E - I_C/I_E}$$

[eq: alpha-beta] which gives the pair worth memorising: ·L3 p6

$$\boxed{\;\beta = \frac{\alpha}{1-\alpha}\;}\qquad\text{and}\qquad
\boxed{\;\alpha = \frac{\beta}{1+\beta}\;}$$

[derivation] The book's cross-multiplication, step by step: ·L3 p6

$$\beta(1-\alpha) = \alpha$$

$$\beta = \alpha(1+\beta)$$

$$\alpha = \frac{\beta}{1+\beta}$$

[eq] And the corollary the leakage work needs: ·L3 p6

$$\boxed{\;1-\alpha = \frac{1}{1+\beta}\;}$$

*[added] Check: $1 - \dfrac{\beta}{1+\beta} = \dfrac{1+\beta-\beta}{1+\beta} = \dfrac{1}{1+\beta}$ ✓.*

*[added] Numerical feel: $\alpha = 0.98 \Rightarrow \beta = 49$; $\alpha = 0.99 \Rightarrow \beta = 99$; $\alpha = 0.995 \Rightarrow \beta = 199$. A small change in $\alpha$ near 1 is a large change in
$\beta$ — which is exactly why the CE configuration's gain is the unstable one.*

> ⚠ VERIFY **C3.28** ·L3 p6 — the derivation prints *"$\beta\,(1 - a) = \alpha$"* with a Latin **a**
> for $\alpha$, and *"It is seen from the **about** 2 equations"* for *above*. Nothing computed
> changes.

---

## 3.8 CC configuration and the gain $(1+\beta)$ ·L3 p6

In CC the signal goes in between **base and collector** and comes out between **emitter and
collector**, so conventionally **$I_B$ is the input current and $I_E$ is the output current**. ·L3 p6

[derivation] The current gain: ·L3 p6

$$\frac{I_E}{I_B} = \frac{I_E}{I_C}\cdot\frac{I_C}{I_B} = \frac{1}{\alpha}\cdot\beta = \frac{\beta}{\alpha}$$

$$= \frac{\beta}{\beta/(1+\beta)}$$

[eq: cc-current-gain]

$$\boxed{\;\frac{I_E}{I_B} = 1+\beta\;}\qquad\text{i.e.}\qquad
\text{output current} = (1+\beta)\times\text{input current}$$

Consistently with §3.6: ·L3 p6

$$I_E = I_B + I_C = I_B + \beta I_B = (1+\beta)I_B$$

[fig ·L3 p6] **Fig. 57.9** shows the CC current paths. **(a) PNP:** the symbol with the base at the
left fed through a battery, $I_B$ entering the base, $I_C$ leaving the collector downward to the node
the two batteries share, and $I_E$ leaving along the top rail. **(b) NPN:** the same with all arrows
and both battery polarities reversed. In both, the **collector is the common terminal**, tied to the
junction of the two supplies.

---

## 3.9 The complete set of current relations ·L3 p6

This is §57.11 and it is the single most exam-useful table in the chapter. Every relation below
follows from $I_E = I_B + I_C$, $\alpha = I_C/I_E$ and $\beta = I_C/I_B$. ·L3 p6

[eq: current-relations] **(i) Collector current, three ways**

$$\boxed{\;I_C = \beta I_B = \alpha I_E = \frac{\beta}{1+\beta}\,I_E\;}$$

[eq] **(ii) Base current, three ways**

$$\boxed{\;I_B = \frac{I_C}{\beta} = \frac{I_E}{1+\beta} = (1-\alpha)\,I_E\;}$$

[eq] **(iii) Emitter current, four ways**

$$\boxed{\;I_E = \frac{I_C}{\alpha} = \frac{1+\beta}{\beta}\,I_C = (1+\beta)\,I_B
= \frac{I_B}{1-\alpha}\;}$$

[eq: current-ratio] **(iv) The three dc currents always stand in this ratio** ·L3 p6

$$\boxed{\;I_E : I_B : I_C \;::\; 1 : (1-\alpha) : \alpha\;}$$

The book's footnote notes the analogy with the power-distribution relationship in an induction
motor. ·L3 p6

**Notation for ac quantities.** For ac currents, **lower-case letters** are used: $i_e$, $i_b$,
$i_c$. ·L3 p6

> [added] **Why (iv) is worth memorising.** It turns any one measured current into the other two in a
> single step. With $\alpha = 0.98$: $I_E : I_B : I_C = 1 : 0.02 : 0.98$, so a 5 mA emitter current
> means 100 µA of base current and 4.9 mA of collector current, no algebra required.

---

## 3.10 Leakage currents ·L3 p6, p7

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_{CBO}$ | collector–base leakage, **emitter open** | A (µA) | 1–10 µA (Si), µA–mA (Ge) |
| $I_{CO}$ | the same quantity, the book's shorthand in the examples | A (µA) | 5 µA |
| $I_{CEO}$ | collector–emitter leakage, **base open** | A (µA) | $(1+\beta)I_{CBO}$ |

[def] **$I_{CBO}$** — the current that flows from **C**ollector to **B**ase with the emitter
**O**pen. It is the reverse saturation current of the reverse-biased C/B junction, carried by
**minority** carriers. ·L3 p6

**How the emitter current actually splits, once leakage is admitted.** ·L3 p6 The emitter current
initiated by the forward-biased E/B junction divides into two parts:

- $(1-\alpha)I_E$, which becomes the external base current $I_B$;
- $\alpha I_E$, which becomes the external collector current $I_C$.

[fig ·L3 p6] **Fig. 57.10** shows the CB leakage measurement. **(a)** The **P | N | P** block with
$V_{EE}$ on the left through a switch $\mathbf{S_1}$ and $V_{CC}$ on the right through a switch
$\mathbf{S_2}$; with $S_1$ **open** the emitter carries no current, and a small loop drawn as a
**red dashed rectangle** circulates $I_{CBO}$ around the collector–base circuit. **(b)** The same
condition on the symbol: the emitter lead is drawn broken with $\mathbf{I_E = 0}$ and the word
**OPEN** beside it, and $I_{CBO}$ circulates in a dashed loop from collector through base and back
via $V_{CC}$.

> ⚠ VERIFY **C3.5** ·L3 p6 — the text reads *"Consider the CB transistor circuit shown in Fig.
> 57.11"* while the figure printed beside it is captioned **Fig. 57.10**. A cross-reference slip;
> nothing computed changes. See `_verification-log.md`.

### ⚠ The missing pages, and what has to be reconstructed

Printed pages **2194–2195** are absent from the PDF. They carried the rest of §57.12 (the **CE**
leakage case), all of §57.13's opening, and **Examples 57.2 and 57.3**. ·L3 p6 ends inside the CB
discussion; ·L3 p7 opens on the last line of an $I_{CEO}$ calculation.

**The one line that survives from the missing pages** ·L3 p7 — it is the tail of Example 57.3:

$$I_{CEO} = (1+\beta)\,I_{CO} = (1+49)\times 5 = 250\ \mathrm{\mu A} = 0.25\ \mathrm{mA}$$

*[added] Verified: $50 \times 5 = 250\ \mathrm{\mu A}$ ✓. The data can be read back out of it:
$\beta = 49$ (hence $\alpha = 49/50 = 0.98$) and $I_{CO} = 5\ \mathrm{\mu A}$.*

> ### [added] The leakage relations, reconstructed
>
> These are **standard results**, not lifted from the missing pages, but every one of them is used
> without further comment by the examples on ·L3 p7 — so the file would be unusable without them.
> They follow from $I_E = I_B + I_C$ plus the definition of $I_{CBO}$.
>
> [eq: icbo-iceo] **Leakage in the two configurations**
> $$\boxed{\;I_{CEO} = (1+\beta)\,I_{CBO} = \frac{I_{CBO}}{1-\alpha}\;}$$
> $I_{CEO}$ is $(1+\beta)$ times larger than $I_{CBO}$ — the leakage is itself amplified by the
> transistor when the base is left open, which is why the CE configuration is the thermally
> dangerous one (§3.18).
>
> [eq: ic-with-leakage] **Collector current including leakage**
> $$\boxed{\;I_C = \alpha I_E + I_{CBO}\;}\qquad\text{(common-base)}$$
> $$\boxed{\;I_C = \beta I_B + (1+\beta)\,I_{CBO}\;}\qquad\text{(common-emitter)}$$
>
> **Derivation of the CE form from the CB form** — the step ·L3 p7's Example 57.4 uses silently:
> $$I_C = \alpha(I_B + I_C) + I_{CBO}$$
> $$I_C(1-\alpha) = \alpha I_B + I_{CBO}$$
> $$I_C = \frac{\alpha I_B}{1-\alpha} + \frac{I_{CBO}}{1-\alpha} = \beta I_B + (1+\beta)I_{CBO}$$
>
> The book writes $I_{CO}$ for $I_{CBO}$ throughout the examples. Treat the two as the same symbol.

### [ex] Example 57.4 — collector and emitter current with leakage ·L3 p7

**Statement.** For a transistor, $I_B = 100\ \mathrm{\mu A}$, $\alpha_{dc} = 0.98$ and
$I_{CO} = 5\ \mathrm{\mu A}$. Find $I_C$ and $I_E$.

**Solution** (the page's own)

$$I_C = \frac{\alpha I_B}{1-\alpha} + \frac{I_{CO}}{1-\alpha}
= \frac{0.98\times100}{1-0.98} + \frac{5}{1-0.98}$$

$$I_C = \frac{98}{0.02} + \frac{5}{0.02} = 4900 + 250 = 5150\ \mathrm{\mu A} = 5.15\ \mathrm{mA}$$

$$I_E = I_C + I_B = 5.15 + 100\times10^{-3} = 5.25\ \mathrm{mA}$$

*[added] Verified: $0.98\times100/0.02 = 4900$ ✓; $5/0.02 = 250$ ✓; sum $5150\ \mathrm{\mu A}$ ✓;
$5.15 + 0.1 = 5.25\ \mathrm{mA}$ ✓. Cross-check with the boxed CE form: $\beta = 0.98/0.02 = 49$, so
$I_C = 49(0.1) + 50(0.005) = 4.9 + 0.25 = 5.15\ \mathrm{mA}$ ✓.*

### [ex] Example 57.5 — CB data used to predict a CE collector current ·L3 p7

*(Electronics-II, M.S. Univ. Vadodra 1990)*

**Statement.** A transistor operating in CB configuration has $I_C = 2.98\ \mathrm{mA}$,
$I_E = 3.00\ \mathrm{mA}$ and $I_{CO} = 0.01\ \mathrm{mA}$. What current will flow in the collector
circuit of this transistor when it is connected in CE configuration with a base current of
$30\ \mathrm{\mu A}$?

**Solution** (the page's own)

For CE, $I_C = \beta I_B + (1+\beta)I_{CO}$. First get $\beta$ from the CB data, where
$I_C = \alpha I_E + I_{CO}$:

$$2.98 = \alpha\times3 + 0.01 \quad\Longrightarrow\quad \alpha = \frac{2.97}{3} = 0.99$$

$$\beta = \frac{\alpha}{1-\alpha} = \frac{0.99}{1-0.99} = 99$$

$$I_C = 99\times0.03 + (1+99)\times0.01 = 2.97 + 1.00 = 3.97\ \mathrm{mA}$$

> ### ⚠ VERIFY **V3.3** ·L3 p7 — a digit is dropped inside $\beta = \alpha/(1-\alpha)$
>
> The page prints: *"$\beta = \alpha/(1-\alpha) = 0.99/(1 - \mathbf{0.09}) = 99$."*
>
> **Correct form:**
> $$\boxed{\;\beta = \frac{0.99}{1-0.99} = \frac{0.99}{0.01} = 99\;}$$
>
> **Why.** As printed, $0.99/0.91 = 1.088$, not 99 — and carrying $\beta = 1.088$ forward gives
> $I_C = 1.088(0.03) + 2.088(0.01) = 0.054\ \mathrm{mA}$ instead of 3.97 mA, a factor of 73 out. The
> page's own final answer of 3.97 mA is correct and confirms that $1-0.99$ was intended.
> See `_verification-log.md`.

*[added] Verified: $2.97/3 = 0.99$ ✓; $0.99/0.01 = 99$ ✓; $99(0.03) = 2.97$ and $100(0.01) = 1.00$,
sum $3.97\ \mathrm{mA}$ ✓. Note how large the leakage term has become — $1.00\ \mathrm{mA}$ out of
$3.97\ \mathrm{mA}$, a quarter of the collector current, from a CB leakage of only 10 µA. That is
the $(1+\beta)$ multiplication in action.*

### [ex] Example 57.6 — $\alpha$, $\beta$, $I_E$, and re-biasing for a target $I_C$ ·L3 p7

**Statement.** For a certain transistor, $I_C = 5.505\ \mathrm{mA}$, $I_B = 50\ \mathrm{mA}$,
$I_{CO} = 5\ \mathrm{mA}$. Determine **(i)** $\alpha$, $\beta$ and $I_E$; **(ii)** the new level of
$I_B$ required to make $I_C = 10\ \mathrm{mA}$.

> ### ⚠ VERIFY **V3.4** ·L3 p7 — two currents printed in the wrong unit
>
> The statement prints $I_B = 50\ \mathrm{mA}$ and $I_{CO} = 5\ \mathrm{mA}$. **Both must be
> microamps:** $I_B = 50\ \mathrm{\mu A}$, $I_{CO} = 5\ \mathrm{\mu A}$.
>
> **Why.** The page's own first line works in microamps: $5.505\times10^{3} = \beta\times50 + (1+\beta)\times5$, i.e. $I_C$ converted to µA on the left and $I_B$, $I_{CO}$ already in µA on the
> right. Taken as printed (all in mA), the same equation reads $5.505 = 55\beta + 5$, giving
> $\beta = 0.009$ — a transistor with a current gain of one hundredth. Also, $I_B = 50\ \mathrm{mA}$
> with $I_C = 5.505\ \mathrm{mA}$ would make the base current nine times the collector current.
> See `_verification-log.md`.

**Solution** (the page's own, in microamps throughout)

**(i)**
$$I_C = \beta I_B + (1+\beta)I_{CO}$$
$$5.505\times10^{3} = \beta\times50 + (1+\beta)\times5$$
$$5505 = 55\beta + 5 \quad\Longrightarrow\quad \beta = 100$$

$$I_E = I_C + I_B = 5.505 + 50\times10^{-3} = 5.555\ \mathrm{mA}$$

$$I_C = \alpha I_E + I_{CO}: \quad 5.505 = \alpha\times5.555 + 5\times10^{-3}$$
$$\alpha = \frac{5.500}{5.555} = 0.99$$

**(ii)** For $I_C = 10\ \mathrm{mA}$, using $I_C = \beta I_B + (1+\beta)I_{CO}$:

$$10 = 100\,I_B + 101\times5\times10^{-3}$$
$$100\,I_B = 10 - 0.505 = 9.495$$
$$I_B = 0.09495\ \mathrm{mA} = 94.95\ \mathrm{\mu A}$$

*[added] Verified: $(5505-5)/55 = 100$ ✓; $5.505+0.05 = 5.555$ ✓; $5.500/5.555 = 0.9901$ ✓;
$(10-0.505)/100 = 0.09495\ \mathrm{mA}$ ✓. Cross-check on $\alpha$: $\beta = 100 \Rightarrow \alpha = 100/101 = 0.9901$ ✓ — the two routes agree.*

> ⚠ VERIFY **C3.6** ·L3 p7 — part (ii) opens *"As seen from Art. 7.12"*; the article is **57.12**.
> Nothing computed changes.

### [ex] Example 57.7 — a germanium OC 71, and a wrong printed answer ·L3 p7

*(Electronics-1, Gwalior Univ. 1986)*

**Statement.** *(The page opens with a stray instruction, "Discuss the operation of a PNP
transistor", before the actual question.)* The reverse saturation current in a PNP germanium
transistor type **OC 71** is $8\ \mathrm{\mu A}$. If the transistor's common-base current gain is
**0.979**, calculate the collector and emitter current for a $40\ \mathrm{\mu A}$ base current. What
is the collector current when the base current is zero?

**Given** $I_{CO} = 8\ \mathrm{\mu A} = 0.008\ \mathrm{mA}$, $\alpha = 0.979$,
$I_B = 40\ \mathrm{\mu A} = 0.04\ \mathrm{mA}$.

**The page's method line**

$$I_C = \beta I_B + I_{CEO} = \beta I_B + \frac{I_C}{1-\alpha}$$

> ### ⚠ VERIFY **V3.5** ·L3 p7 — a self-referential $I_C$
>
> The method line prints $I_{CEO} = \dfrac{I_C}{1-\alpha}$.
>
> **Correct form:**
> $$\boxed{\;I_{CEO} = \frac{I_{CO}}{1-\alpha}\;}$$
>
> **Why.** $I_C$ appears on both sides of the equation — the self-reference test. Only the *leakage*
> current is divided by $(1-\alpha)$; solving the printed version literally gives
> $I_C[1 - 1/(1-\alpha)] = \beta I_B$, i.e. a negative collector current. See `_verification-log.md`.

**The page's working**

$$\beta = \frac{\alpha}{1-\alpha} = \frac{0.979}{1-0.979} = 46.6$$

$$I_C = 46.6\times0.04 + (1+46.6)\times0.008 = \mathbf{1.9\ mA}$$

$$I_E = I_C + I_B = 1.9 + 0.04 = \mathbf{1.94\ mA}$$

> ### ⚠ VERIFY **V3.6** ·L3 p7 — the printed answers are wrong; the leakage term is written but never added
>
> The page prints $I_C = 1.9\ \mathrm{mA}$ and $I_E = 1.94\ \mathrm{mA}$.
>
> **Recompute the page's own expression, term by term:**
> $$46.6 \times 0.04 = 1.864\ \mathrm{mA}$$
> $$(1+46.6)\times0.008 = 47.6\times0.008 = 0.381\ \mathrm{mA}$$
> $$I_C = 1.864 + 0.381 = 2.245\ \mathrm{mA}$$
>
> **Correct answers:**
> $$\boxed{\;I_C = 2.25\ \mathrm{mA},\qquad I_E = I_C + I_B = 2.25 + 0.04 = 2.29\ \mathrm{mA}\;}$$
>
> **Why, and the signature of the slip.** $1.9\ \mathrm{mA}$ is $\beta I_B$ alone — the leakage term
> $(1+\beta)I_{CO} = 0.381\ \mathrm{mA}$ is typeset but not carried into the sum, so the printed
> answer is short by exactly one leakage term.
>
> **Independent confirmation, without $\beta$ at all.** From $I_C = \alpha I_E + I_{CO}$ and
> $I_E = I_B + I_C$:
> $$I_C = \frac{\alpha I_B + I_{CO}}{1-\alpha} = \frac{0.979(0.04) + 0.008}{0.021}
> = \frac{0.04716}{0.021} = 2.246\ \mathrm{mA}$$
> Exact agreement with the corrected route. See `_verification-log.md`.

> ⚠ VERIFY **C3.7** ·L3 p7 — the "Given" line prints *"$I_{CO} = 8\ \mathrm{\mu A} = 0.008\ \mathrm{\mu A}$"*. The conversion should read **0.008 mA**; the working uses currents in mA
> throughout. Nothing computed changes.

> ⚠ VERIFY **C3.8** ·L3 p7 — Example 57.7's statement ends *"What is the collector current when base
> current is zero?"* and **the printed solution never answers that part** — it stops after $I_C$ and
> $I_E$. Nothing printed is wrong; the solution is incomplete. The missing answer is supplied below.
> See `_verification-log.md`.

> ### [added] The part of Example 57.7 the page never answers
>
> With $I_B = 0$ the base is open, so the collector current is the common-emitter leakage:
> $$I_C\big|_{I_B=0} = I_{CEO} = \frac{I_{CO}}{1-\alpha} = \frac{0.008}{0.021} = 0.381\ \mathrm{mA}
> = \boxed{381\ \mathrm{\mu A}}$$
> **Cross-check:** $I_{CEO} = (1+\beta)I_{CO} = 47.6\times8\ \mathrm{\mu A} = 381\ \mathrm{\mu A}$ ✓.
>
> Note the size of it — **381 µA of collector current with the base disconnected**, from a device
> whose C/B leakage is only 8 µA. This is a germanium transistor, and this number is the reason
> germanium fell out of use.

---

## 3.11 CB static characteristics ·L3 p7–p9

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $R_{in}$ | input resistance, $\Delta V/\Delta I$ at the input port | Ω | ≈ 50 Ω (CB) |
| $R_{out}$ | output resistance, $\Delta V/\Delta I$ at the output port | Ω | ≈ 500 kΩ (CB) |
| $R_1$, $R_2$ | rheostat / potentiometer setting $V_{CB}$ and $V_{BE}$ in the test rig | Ω | — |

[def] **Static characteristics** are the curves relating the transistor's dc currents and voltages.
There are three of them for each configuration: ·L3 p7

1. **input characteristic**,
2. **output characteristic**,
3. **constant-current transfer characteristic**.

### The CB test circuit ·L3 p7–p8

[fig ·L3 p7] **Fig. 57.13** — the rig for measuring the CB characteristics of an **NPN** transistor.
Reading left to right: a battery $V_{EE}$; a **potentiometer $R_2$** across it whose wiper feeds the
emitter; a **milliammeter in the emitter lead reading $I_E$**; the transistor, drawn horizontally
with $E$ on the left, $C$ on the right, and the **base lead running down to ground** (the emitter
arrow points *outward*, away from the base bar — NPN); a **voltmeter $V_{BE}$ connected between the
base and emitter**; a **milliammeter in the collector lead reading $I_C$**; a **voltmeter $V_{CB}$
between collector and base**; a **rheostat $R_1$**; and the collector supply $V_{CC}$.

**What each control does** ·L3 p8

- **$R_1$** supplies a variable voltage from the collector supply — it sets $V_{CB}$.
- **$R_2$** supplies a variable voltage from the emitter supply — it sets $V_{BE}$, hence $I_E$.
- Milliammeters sit in series with the emitter and collector to read $I_E$ and $I_C$; voltmeters go
  across E–B and across C–B.

### (a) Input characteristic — $I_E$ against $V_{BE}$, at constant $V_{CB}$ ·L3 p8

**Method.** Set $V_{CB}$ to a convenient value with $R_1$. Raise $V_{BE}$ in discrete steps and read
$I_E$ at each step. Plot. ·L3 p8

[fig ·L3 p8] **Fig. 57.14.** Vertical axis $I_E$ in **mA**, marked 0, 2, 4, 6, 8. Horizontal axis
$V_{BE}$ in **volts**, marked 0.2, 0.4, 0.6, 0.8. **Two curves**, both the shape of a forward-biased
diode characteristic: the left one labelled **Ge**, lifting off the axis at roughly 0.2–0.3 V and
rising steeply past 0.4 V; the right one labelled **Si**, flat until about 0.55–0.6 V then rising
steeply. A small right-angled triangle is drawn on the Ge curve with its vertical side labelled
$I_E$ and its horizontal side labelled $V_{BE}$, marking the slope used for $R_{in}$.

**Both curves are exactly the forward characteristic of a P-N diode** — which is what the E/B
junction is. ·L3 p8

[eq: cb-rin] **Input resistance is the reciprocal of the slope:** ·L3 p8

$$\boxed{\;R_{in} = \frac{\Delta V_{BE}}{\Delta I_E}\;}\qquad(V_{CB}\ \text{constant})$$

*(the $\Delta$ symbols do not render on the page — see **C3.2**)*

- Because the characteristic is **initially non-linear**, $R_{in}$ varies with where it is measured.
- Over the **linear part** it is about **50 Ω**; **for low $V_{BE}$ it is considerably greater**.
- **This variation of $R_{in}$ with $V_{BE}$ is what produces distortion** in signals handled by the
  transistor. ·L3 p8
- The input characteristic is **hardly affected** by changes in $V_{CB}$ or in temperature. ·L3 p8

### (b) Output characteristic — $I_C$ against $V_{CB}$, at constant $I_E$ ·L3 p8–p9

**Method.** Set $I_E$ with $R_2$. Holding $I_E$ constant, raise $V_{CB}$ from zero in steps and note
$I_C$. Return $V_{CB}$ to zero, raise $I_E$ a little, repeat. The result is a family of curves. ·L3 p8

[fig ·L3 p9] **Fig. 57.15** — the CB output characteristic family.

- **Vertical axis** $I_C$ in **mA**, marked 2, 4, 6, 8.
- **Horizontal axis** $V_{CB}$ in **volts**, running from **−4 through 0 to 12 V**, marked at
  −4, −2, 0, 2, 4, 6, 8, 10, 12.
- **Five curves**, labelled at their right-hand ends $I_E = 0$, **2 mA**, **4 mA**, **6 mA** and
  **8 mA**. Each rises almost vertically in the region $-1 < V_{CB} < 0$, turns a sharp knee just
  right of $V_{CB} = 0$, and then runs **almost horizontally** all the way across, sloping very
  gently upward.
- At the far right (about 11–12 V) all the curves sweep steeply upward together; this region is
  labelled **"Break Down Region"**.
- The narrow band left of $V_{CB} = 0$, where the curves are near-vertical, is bracketed and labelled
  **"Saturation Region"**.
- The region **below the $I_E = 0$ curve** is labelled **"Cut-Off Region"**.
- A small arrow at about $V_{CB} = 5$ points to the $I_E = 0$ curve and is labelled $\mathbf{I_{CBO}}$.
- Two horizontal **dashed** construction lines run from the $I_C$ axis to the curves: from **D**
  (at $I_C \approx 6.2$) across to **B** on the $I_E = 6\ \mathrm{mA}$ curve, and from **E** (at
  $I_C \approx 4.3$) across to **C** on the $I_E = 4\ \mathrm{mA}$ curve. Point **A** is marked on
  the $I_E = 2\ \mathrm{mA}$ curve near its knee.

**Five things the page draws out of this family** ·L3 p8–p9

**1. Output resistance is very high.** The reciprocal of the near-horizontal slope:

[eq: cb-rout]
$$\boxed{\;R_{out} = \frac{1}{\Delta I_C/\Delta V_{CB}} = \frac{\Delta V_{CB}}{\Delta I_C}\;}$$

Since $I_C$ is virtually independent of $V_{CB}$ over most of the range, $R_{out}$ is very high — a
typical value is **500 kΩ**. ·L3 p8

**2. $I_C$ flows even when $V_{CB} = 0$.** For example $I_C = 1.8\ \mathrm{mA}$ at $V_{CB} = 0$ when
$I_E = 2\ \mathrm{mA}$. The reason: carriers injected into the base by the forward-biased E/B
junction are still collected, driven by the **internal junction voltage** at the C/B junction. To
push $I_C$ to zero you must **apply a small forward bias across the C/B junction** to neutralise that
built-in barrier — which is why the curves only reach the axis at *negative* $V_{CB}$. ·L3 p8

**3. $I_C$ flows even when $I_E = 0$.** That current is the collector leakage $I_{CBO}$. ·L3 p9

**4. The family gives $\alpha_{ac}$.** ·L3 p9

$$\alpha_{ac} = \frac{\Delta I_C}{\Delta I_E} = \frac{DE}{BC} = \frac{6.2-4.3}{2} = 0.95$$

> ### ⚠ VERIFY **V3.7** ·L3 p9 — $BC$ is not $\Delta I_E$
>
> The page prints $\alpha_{ac} = \Delta I_C/\Delta I_E = DE/BC$, then substitutes $(6.2-4.3)/2$.
>
> **What is actually on the figure.** $B$ and $C$ are points on the $I_E = 6\ \mathrm{mA}$ and
> $I_E = 4\ \mathrm{mA}$ curves **at the same $V_{CB}$**, and $D$ and $E$ are their projections onto
> the $I_C$ axis. So $DE$ and $BC$ are the **same length**, both equal to $\Delta I_C = 1.9\ \mathrm{mA}$, and $DE/BC = 1$ — not 0.95.
>
> **Correct form:**
> $$\boxed{\;\alpha_{ac} = \frac{DE}{\Delta I_E} = \frac{6.2-4.3}{6-4} = \frac{1.9}{2} = 0.95\;}$$
> where $\Delta I_E = 2\ \mathrm{mA}$ is the **difference between the two curves' $I_E$ labels**, not
> a distance measured on the graph.
>
> **Why it matters.** A reader who measures both segments off the page as the notation instructs gets
> $\alpha_{ac} = 1$, which is impossible for a CB current gain. See `_verification-log.md`.

**5. Breakdown.** Although $I_C$ is practically independent of $V_{CB}$ over the working range, if
$V_{CB}$ is pushed beyond a certain value $I_C$ **increases rapidly due to avalanche breakdown**.
·L3 p9

### (c) Current transfer characteristic — $I_C$ against $I_E$, at constant $V_{CB}$ ·L3 p9

**Method.** Set $V_{CB}$ to a convenient value, raise $I_E$ in steps and note $I_C$. ·L3 p9

[fig ·L3 p9] **Fig. 57.16.** **(a)** Vertical axis $I_C$ in **mA** marked 0, 2, 4, 6; horizontal axis
$I_E$ marked 0, 5, 10 mA; a **straight line rising from the origin** with slope a little less than 1,
boxed label *"$V_{CB}$ Constant"*; a small right-angled triangle on the line with its vertical side
labelled $I_C$ and horizontal side $I_E$. **(b)** A magnified view of the region near the origin,
showing that the line does **not** pass exactly through the origin — it meets the $I_C$ axis at a
**small positive intercept marked $I_{CBO}$**, with arrows above and below marking that offset.

[eq]
$$\alpha_{ac} = \frac{\Delta I_C}{\Delta I_E}$$

**Usually $\alpha_{ac}$ is found from the output characteristic rather than from this one.** ·L3 p9

> [added] Panel (b) is the graphical statement of $I_C = \alpha I_E + I_{CBO}$: the **slope** is
> $\alpha$ and the **intercept** is $I_{CBO}$. That single line contains everything §3.10 derived.

**Why CB is rarely used for audio-frequency circuits** ·L3 p9

1. its **current gain is less than unity**, and
2. its **input and output resistances are so different** (tens of ohms against hundreds of
   kilohms) that matching between stages is impractical.

---

## 3.12 CE static characteristics ·L3 p9–p11

### The CE test circuit ·L3 p9–p10

[fig ·L3 p10] **Fig. 57.17** — the rig for an **NPN** transistor in CE. Left to right: the base
supply $V_{BB}$; a **potentiometer $R_2$ across $V_{BB}$**, used to vary $I_B$ and $V_{BE}$; a
**milliammeter (or microammeter for a low-power transistor) in the base lead reading $I_B$**; the
transistor drawn with $B$ at the left, $C$ at the top right, $E$ at the bottom right (emitter arrow
pointing *outward* — NPN); a **voltmeter $V_{BE}$, typical range 0–1 V, across base and emitter**; a
**milliammeter in the collector lead reading $I_C$**; a **second voltmeter $V_{CE}$, typical range
0–20 V, across collector and emitter**; a **rheostat $R_1$**; and $V_{CC}$. The **emitter is
grounded**.

### (a) Input characteristic — $I_B$ against $V_{BE}$, at constant $V_{CE}$ ·L3 p10

**Method.** Hold $V_{CE}$ at a convenient constant value; raise $V_{BE}$ in steps and read $I_B$.
Repeat for a different constant $V_{CE}$. ·L3 p10

[fig ·L3 p10] **Fig. 57.18.** Vertical axis $I_B$, marked 0, 25, 50, 75, with the unit printed at the
top of the axis as **mA**. Horizontal axis $V_{BE}$ in **volts**, marked 0.1, 0.2, 0.3, 0.4. A
**single curve** leaving the origin almost flat and curving upward with steadily increasing slope —
the forward diode shape again. A small right-angled triangle near the top of the curve has its
vertical side labelled $I_B$ and horizontal side $V_{BE}$.

> ### ⚠ VERIFY **V3.8** ·L3 p10 — the ordinate of Fig. 57.18 is in the wrong unit
>
> The axis is labelled **mA**, with ticks at 25, 50, 75.
>
> **Correct: µA.**
>
> **Why.** (i) A base current of 75 mA at $V_{BE} = 0.4\ \mathrm{V}$ is physically impossible for a
> small-signal transistor — with $\beta \approx 100$ it implies 7.5 A of collector current. (ii) The
> text immediately beside the figure gives $R_{in}$ ranging from **4 kΩ to 600 Ω**; reading the graph
> in mA gives slopes of a few ohms. (iii) The corresponding CE **output** family two pages later
> (·L3 p12, Fig. 57.22) labels its base-current curves **µA**, and ·L3 p11's text speaks of
> *"$I_B = 60\ \mathrm{\mu A}$ and $40\ \mathrm{\mu A}$ lines"*. See `_verification-log.md`.

**Like the CB input characteristic, the overall shape is the forward characteristic of a P-N diode.**
·L3 p10

[eq: ce-rin]
$$\boxed{\;R_{in} = \frac{1}{\Delta I_B/\Delta V_{BE}} = \frac{\Delta V_{BE}}{\Delta I_B}\;}$$

Because of the initial non-linearity, $R_{in}$ varies considerably — from about **4 kΩ near the
origin** to about **600 Ω over the more linear part** of the curve. ·L3 p10

### (b) Output (collector) characteristic — $I_C$ against $V_{CE}$, at constant $I_B$ ·L3 p10–p11

**Method.** Set $I_B$ and hold it; raise $V_{CE}$ from zero in steps, noting $I_C$. Return $V_{CE}$
to zero, set a new $I_B$, repeat. ·L3 p10

[fig ·L3 p11] **Fig. 57.19** — the CE output characteristic family, and the most information-dense
figure in the chapter.

- **Vertical axis** $I_C$ in **mA**, marked 2, 4, 6, 8.
- **Horizontal axis** $V_{CE}$ in **volts**, marked 0, 5, 10, 15, 20, 25.
- **Five curves**, labelled from the top **$I_B = 80\ \mathrm{mA}$** *(see V3.9)*, **60**, **40**,
  **20**, **0**. Each rises steeply from the origin region, knees over at a low $V_{CE}$, then runs
  nearly horizontally with a **noticeably greater upward slope than the CB family**.
- A steep straight line from the origin up to a point **M** at the top left is labelled **"Saturation
  Line"**; the wedge between it and the $I_C$ axis is **hatched with diagonal lines** and labelled
  **"Saturation Region"**, with an arrow pointing to the knee area.
- The thin hatched band **below the $I_B = 0$ curve** is labelled **"Cut-Off Region"**, and an arrow
  on the $I_B = 0$ curve is labelled $\mathbf{I_{CEO}}$.
- On the right-hand side, where all curves sweep upward near 25 V, the words **"Break Down"** are
  printed vertically.
- Between the $I_B = 60$ and $I_B = 40$ curves, two points **A** (upper) and **B** (lower) are marked
  with a small step construction: a horizontal segment labelled $\boldsymbol{\Delta V_{CE}}$ and a
  vertical segment labelled $\boldsymbol{\Delta I_C}$.

> ### ⚠ VERIFY **V3.9** ·L3 p11 — the top curve of Fig. 57.19 is labelled $I_B = 80\ \mathrm{mA}$
>
> **Correct: $I_B = 80\ \mathrm{\mu A}$.**
>
> **Why.** The text on the same page says *"We may select any two points $A$ and $B$ on the
> $I_B = 60\ \mathrm{\mu A}$ and $40\ \mathrm{\mu A}$ lines"* — the other four curves in the same
> family are explicitly microamps. And with $I_C \approx 8\ \mathrm{mA}$ on that curve, $I_B = 80\ \mathrm{mA}$ would give $\beta = 0.1$; $80\ \mathrm{\mu A}$ gives $\beta = 100$.
> See `_verification-log.md`.

**Reading the family** ·L3 p10–p11

- As $V_{CE}$ rises from zero at fixed $I_B$, $I_C$ **rises rapidly to a near-saturation level** and
  then flattens. ·L3 p10
- A small collector current flows **even when $I_B = 0$**; it is $I_{CEO}$. With the main collector
  current zero, the transistor is said to be **cut off**. ·L3 p10
- Push $V_{CE}$ too far and the **C/B junction breaks down completely**; avalanche breakdown makes
  $I_C$ rise rapidly and **may destroy the transistor**. ·L3 p10
- When $V_{CE}$ is **very low (ideally zero)** the transistor is **saturated** and operates in the
  saturation region. **In saturation, a change in $I_B$ produces no corresponding change in
  $I_C$** — control is lost. ·L3 p10

[eq: beta-ac-graph] **Reading $\beta_{ac}$ off the family** ·L3 p10–p11

$$\boxed{\;\beta_{ac} = \frac{\Delta I_C}{\Delta I_B}\;}$$

taken at a specified $I_B$ and $V_{CE}$. Using points $A$ and $B$ on the 60 µA and 40 µA curves,
$\Delta I_B = (60-40) = 20\ \mathrm{\mu A}$ and $\Delta I_C$ is read from the diagram. ·L3 p11

[eq: ce-rout] **Output resistance** ·L3 p11

$$\boxed{\;R_{out} = \frac{\Delta V_{CE}}{\Delta I_C}\;}$$

over the near-horizontal part, **varying from 10 kΩ to 50 kΩ**. ·L3 p11

> [added] **The CB/CE contrast worth carrying into an exam.** $R_{out}$ is ≈ 500 kΩ in CB and only
> 10–50 kΩ in CE. That is the same physical fact as the CE family's visibly steeper horizontal
> sections, and it is why the CE stage is the one that can drive a following stage.

### (c) Current transfer characteristic — $I_C$ against $I_B$, at constant $V_{CE}$ ·L3 p11

[fig ·L3 p11] **Fig. 57.20.** **(a)** Vertical axis $I_C$ in **mA**; horizontal axis $I_B$ in
**µA**; a straight line of slope $\beta$ rising from a small positive intercept, with a boxed label
*"$V_{CE}$ Constant"* and a step triangle whose sides are marked $\boldsymbol{\Delta I_C}$ (vertical)
and $\boldsymbol{\Delta I_B}$ (horizontal). **(b)** The region near the origin magnified, showing the
line meeting the $I_C$ axis at a positive intercept marked $\mathbf{I_{CEO}}$, with arrows marking
that offset.

$$\beta_{ac} = \frac{\Delta I_C}{\Delta I_B}$$

**Leakage in CE.** A small collector current flows even at $I_B = 0$; it is the common-emitter
leakage ·L3 p11

$$\boxed{\;I_{CEO} = (1+\beta)\,I_{CO}\;}$$

and, like $I_{CO}$, it is due to **minority carriers crossing the reverse-biased C/B junction**.
·L3 p11

---

## 3.13 CC static characteristics ·L3 p11–p12

In CC the **collector is common to both the input (base–collector) and the output
(emitter–collector) circuits**. ·L3 p11

[fig ·L3 p11] **Fig. 57.21** — the CC test rig, for an **NPN**. The transistor is drawn with the
**base at the left**, the **emitter leaving at the upper right** (arrow pointing outward) and the
**collector leaving at the lower right**. The **input** port is at the left: an ammeter $A_1$ in the
base lead reading $I_B$, and a voltmeter $\mathbf{V_{CB}}$ from the base node down to the bottom
(collector) rail. The **output** port is at the right: an ammeter $A_2$ in the emitter rail reading
$I_E$, and a voltmeter $\mathbf{V_{CE}}$ from the emitter rail down to the collector rail. A
$\mathbf{V_{BE}}$ arrow runs from the emitter rail down to the base node, marked $-\,-$ at the
emitter end and $+$ at the base node; the bottom (collector) rail is marked $+\,+$; $I_C$ points
upward into the collector. Output terminals at the far right are marked $-$ (top) and $+$ (bottom).

**The polarity marks are §57.3 in miniature:** collector $+\,+$, base $+$, emitter $-\,-$ — an NPN
with the collector most positive.

### The three CC curves ·L3 p11–p12

**Output characteristic** — $I_E$ against $V_{CE}$, for several fixed $I_B$. Since $I_C \cong I_E$,
this is **practically identical to the CE output characteristic**. ·L3 p11

[fig ·L3 p12] **Fig. 57.22(a).** Vertical axis $I_E$ in **mA**, marked 1 to 6; horizontal axis
$V_{CE}$ in **volts**, marked 1 to 6. **Six curves**, labelled from the top
$\mathbf{I_B = 100\ \mu A}$, **80**, **60**, **40**, **20**, **0**, each rising steeply from the
origin, kneeing at about $V_{CE} = 0.5\ \mathrm{V}$, then sloping gently upward across the page.

**Current gain characteristic** — $I_C$ against $I_B$ for different $V_{CE}$: **similar to the CE
version**, again because $I_C \cong I_E$. ·L3 p11

**Input characteristic** — this is the one that is genuinely different. It is a plot of
**$V_{CB}$ against $I_B$ for different values of $V_{CE}$**, and it *"is quite different from those
for CB or CE circuit"*. ·L3 p11

[derivation] **Why it is different.** The input voltage $V_{CB}$ is largely fixed by the output
voltage $V_{CE}$: ·L3 p11

$$V_{CB} = V_{CE} - V_{BE}$$

For $I_B = 100\ \mathrm{\mu A}$ and $V_{CE} = 2\ \mathrm{V}$, with silicon ($V_{BE} = 0.7\ \mathrm{V}$):

$$V_{CB} = 2 - 0.7 = 1.3\ \mathrm{V}$$

For $V_{CE} = 4\ \mathrm{V}$ at the same $I_B$:

$$V_{CB} = 4 - 0.7 = 3.3\ \mathrm{V}$$

**As $V_{CB}$ is increased, $V_{BE}$ is reduced, and so $I_B$ decreases** — the curves therefore
slope *downward*, unlike every other input characteristic in the chapter. ·L3 p11

[fig ·L3 p12] **Fig. 57.22(b).** Vertical axis $I_B$ in **µA**, marked 20, 40, 60, 80, 100.
Horizontal axis labelled $V_{CE}$ *(see V3.10)*, marked 1 to 6 V. A **horizontal dashed line at
$I_B = 100\ \mathrm{\mu A}$** runs right across the plot. **Two nearly straight curves** slope
steeply **down to the right**: the left one labelled *"$V_{CE} = 2\mathrm{V}$"*, crossing the dashed
100 µA line at about **1.3** on the horizontal axis and reaching zero at about 2; the right one
labelled *"$V_{CE} = 4\mathrm{V}$"*, crossing the dashed line at about **3.3** and reaching zero at
about 4.

> ### ⚠ VERIFY **V3.10** ·L3 p12 — the abscissa of Fig. 57.22(b) is labelled $V_{CE}$; it is $V_{CB}$
>
> The horizontal axis is labelled $V_{CE}$ **and** the two plotted curves are labelled
> $V_{CE} = 2\ \mathrm{V}$ and $V_{CE} = 4\ \mathrm{V}$ — the same symbol used for both the abscissa
> and the family parameter, which cannot be right.
>
> **Correct form:** the CC input characteristic is
> $$\boxed{\;V_{CB}\ \text{on the abscissa},\quad I_B\ \text{on the ordinate},\quad
> \text{one curve per value of } V_{CE}\;}$$
>
> **Why — the figure proves it against the text.** ·L3 p11 computes $V_{CB} = 1.3\ \mathrm{V}$ for
> $V_{CE} = 2\ \mathrm{V}$ and $V_{CB} = 3.3\ \mathrm{V}$ for $V_{CE} = 4\ \mathrm{V}$, both at
> $I_B = 100\ \mathrm{\mu A}$. On the figure the two curves cross the dashed $I_B = 100\ \mathrm{\mu A}$ line at **1.3** and **3.3** respectively. Those are $V_{CB}$ values, read off the axis the page
> calls $V_{CE}$. See `_verification-log.md`.

> ⚠ VERIFY **C3.28** ·L3 p11 — the section opens *"collector terminal is common **carrier** to both
> the input (CB) and output (CE) **carriers** circuits"* (the word *carrier(s)* is intrusive; it
> should read *common to both the input and output circuits*), and prints *"practically **idential**"*
> for *identical*. Nothing computed changes.

---

## 3.14 Different ways of drawing transistor circuits ·L3 p12–p13

This section exists because the same circuit appears in three visual dialects, and mistaking one for
another is a common source of sign errors.

### Dialect 1 — two explicit batteries ·L3 p12

[fig ·L3 p12] **Fig. 57.23(a).** A **PNP** in CB. From the left: $I_E$ flows through
$\mathbf{R_E = 20\ K}$ into the emitter, fed by $\mathbf{V_{EE} = 10\ V}$; the collector feeds
$\mathbf{R_L = 10\ K}$ and $\mathbf{V_{CC} = 25\ V}$; the **base is grounded**; $\mathbf{V_{EB}}$ is
marked across emitter–base and $\mathbf{V_{BC}}$ across base–collector; $I_B$ leaves the base
downward.

**How to get the battery polarities right:** apply the polarity rule of §57.3. ·L3 p12 For an **NPN**
both collector and base must be **positive** with respect to the emitter, and the collector a *little
bit more* positive than the base. Equivalently: the collector is positive w.r.t. the base, the base
negative w.r.t. the collector — which is why the potential difference is written $V_{CB}$ and not
$V_{BC}$, *the terminal at higher potential being mentioned first*. The same reasoning fixes
$V_{BE}$. ·L3 p12

> ⚠ VERIFY **C3.9** ·L3 p12 — this paragraph argues in terms of an **NPN** ($V_{CB}$, $V_{BE}$) while
> the figure it introduces, Fig. 57.23, is a **PNP** and correctly carries the reversed labels
> $V_{EB}$ and $V_{BC}$. The rule is stated generically and both halves are individually right, but
> placing them side by side invites the reader to think one of them is mislabelled. The page also
> cites *"the transistor polarity rule (Art. 57.2)"*; the polarity rule is **Art. 57.3**. Nothing
> computed changes.

### Dialect 2 — one rail shown, ground implied ·L3 p12

[fig ·L3 p12] **Fig. 57.23(b).** The same PNP circuit with the batteries replaced by supply
terminals: **$V_{EE} = +10\ \mathrm{V}$** at the top left feeding $R_E = 20\ \mathrm{K}$ down into
the emitter ($I_E$ arrow pointing down), and **$V_{CC} = -25\ \mathrm{V}$** at the top right above
$R_L = 10\ \mathrm{K}$ ($I_C$ arrow pointing **up**, out of the collector). The base is grounded.
$V_{EB}$ is drawn from the emitter node ($+$) down to a reference bar ($-$); $V_{BC}$ from the
collector node ($-$) down to a reference bar ($+$); $I_B$ leaves the base downward to ground.

**The rule for reading this dialect:** *only one terminal of each battery is shown; the other terminal
is understood to be grounded so as to provide a complete path for the current.* ·L3 p12 In
Fig. 57.23(b) the **negative** terminal of $V_{CC}$ and the **positive** terminal of $V_{EE}$ are
grounded — as is the base — even though none of it is drawn. ·L3 p12

### The CE and CC equivalents ·L3 p12–p13

[fig ·L3 p12] **Fig. 57.24** — an **NPN** in CE with two supplies. **(a)** $\mathbf{V_{BB} = 10\ V}$
drives the base through $\mathbf{R_B = 1\ M}$; $\mathbf{V_{CC} = 20\ V}$ feeds the collector through
$\mathbf{R_L = 10\ K}$; the emitter is grounded; $V_{BE}$ and $V_{CE}$ are marked, and $I_B$, $I_C$,
$I_E$ arrowed. **(b)** The same circuit in the rail dialect: $\mathbf{+V_{BB}}$ over $R_B = 1\ \mathrm{M}$ and $\mathbf{+V_{CC}}$ over $R_L = 10\ \mathrm{K}$, emitter grounded.

[fig ·L3 p13] **Fig. 57.25** — the same NPN CE stage run from a **single battery**. $V_{CC} = 20\ \mathrm{V}$ at the top feeds **both** $R_B$ (to the base) and $R_L$ (to the collector); the emitter
goes to ground. This is possible because **both the collector and the base are positive with respect
to the common electrode, the emitter**. ·L3 p13

[fig ·L3 p13] **Fig. 57.26** — the CC configuration of an NPN, drawn two ways. **(a)** $V_{BB}$
through $R_B$ into the base; the emitter through $R_E$ (drawn along the top) to $V_{EE}$; the
collector tied to the node the supplies share; $V_{CB}$ and $V_{CE}$ marked, with polarity marks
$+\,+$ at the bottom rails. **(b)** The same circuit redrawn with $R_B$ on the left to the base and
$R_E$ on the right in the emitter lead, $I_C$ entering the collector from the top. ·L3 p13

---

## 3.15 Common-base dc formulas ·L3 p13–p14

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $R_E$ | emitter-circuit resistor | Ω (usually kΩ) | 10–40 kΩ |
| $R_L$ | collector load resistor | Ω (usually kΩ) | 10–20 kΩ |
| $V_{BE}$ | base–emitter junction drop | V | 0.3 V (Ge), **0.7 V (Si)** |

[derivation] Work the emitter loop of Fig. 57.23(b) — the book calls it *circuit MEBM*. Apply KVL
starting from the base (ground) and going upwards: ·L3 p13

$$-V_{BE} - I_E R_E + V_{EE} = 0$$

[eq: cb-emitter-current]

$$\boxed{\;I_E = \frac{V_{EE} - V_{BE}}{R_E}\;}$$

with $V_{BE} = 0.3\ \mathrm{V}$ for germanium and $\mathbf{0.7\ V}$ for silicon. ·L3 p13
*(The page's footnote explains the $+V_{EE}$ sign: it is taken positive because the traverse goes
from the negative to the positive terminal of the emitter battery.)*

**Since generally $V_{EE} \gg V_{BE}$, this simplifies to** ·L3 p13

$$I_E \cong \frac{V_{EE}}{R_E} = \frac{10\ \mathrm{V}}{20\ \mathrm{K}} = 0.5\ \mathrm{mA}$$

**Taking $V_{BE}$ into account, for a silicon transistor:**

$$I_E = \frac{(10-0.7)\ \mathrm{V}}{20\ \mathrm{K}} = 0.465\ \mathrm{mA}$$

*[added] Verified: $9.3/20 = 0.465\ \mathrm{mA}$ ✓ — a 7 % correction, which is why the
approximation is usually good enough for a first pass but not for an exam answer that asks for
"exact".*

[eq] **Collector current** ·L3 p13

$$I_C = \alpha I_E \cong I_E = 0.5\ \mathrm{mA}\qquad\text{(neglecting leakage)}$$

[eq: cb-vcb] **Collector–base voltage** — from the collector loop, *circuit NCBN*: ·L3 p13

$$\boxed{\;V_{CB} = V_{CC} - I_C R_L\;}$$

$$V_{CB} \cong V_{CC} - I_E R_L = 25 - 0.5\times10 = 20\ \mathrm{V}$$

> ### ⚠ VERIFY **V3.11** ·L3 p13 — $R_L$ is missing from the first expression
>
> The page prints: $V_{CB} = V_{CC} - I_C \cong V_{CC} - I_E R_L = 25 - 0.5\times10 = 20\ \mathrm{V}$.
>
> **Correct form:**
> $$\boxed{\;V_{CB} = V_{CC} - I_C R_L\;}$$
>
> **Why — dimensional.** $V_{CC} - I_C$ is volts minus amperes. The second expression on the same
> line carries $R_L$ correctly, and the arithmetic ($25 - 0.5\ \mathrm{mA}\times10\ \mathrm{k\Omega} = 25 - 5 = 20\ \mathrm{V}$) uses it. See `_verification-log.md`.

> ⚠ VERIFY **C3.10** ·L3 p13 — §57.21 writes the junction voltages as $V_{BE}$ and $V_{CB}$ for the
> **PNP** of Fig. 57.23, whose own labels (and §57.3's own double-subscript rule) give $V_{EB}$ and
> $V_{BC}$. Read them as magnitudes and take the sign from the transistor type. Nothing computed
> changes.

> ⚠ VERIFY **C3.16** ·L3 p13 — §57.21 works *"circuit MEBM"* and *"circuit NCBN"*, but the nodes
> **M** and **N** are **not marked anywhere on Fig. 57.23(b)** (only E, B and C are). From the loops
> as traversed, **M is the $V_{EE}$ supply terminal** at the top of $R_E$ and **N the $V_{CC}$
> terminal** at the top of $R_L$. Nothing computed changes.

### [ex] Example 57.8 — choose $R_L$ for a target $V_{CB}$ ·L3 p13

**Statement.** In the circuit of Fig. 57.27(a), what value of $R_L$ causes $V_{CB} = 5\ \mathrm{V}$?

[fig ·L3 p14] **Fig. 57.27(a).** An **NPN** in CB: $\mathbf{V_{EE} = -10\ V}$ at the top left feeding
a $\mathbf{10\ k}$ emitter resistor ($I_E$ arrow pointing **up** into the emitter);
$\mathbf{V_{CC} = 20\ V}$ at the top right feeding $R_L$ (value unlabelled — it is the unknown), with
$I_C$ pointing **down** into the collector; the **base grounded**; $\mathbf{V_{CB} = 5\ V}$ marked.

**Solution** (the page's own)

$$I_E \cong \frac{V_{EE}}{R_E} = \frac{10\ \mathrm{V}}{10\ \mathrm{K}} = 1\ \mathrm{mA}$$

$$I_C = \alpha I_E \cong I_E = 1\ \mathrm{mA}$$

$$V_{CC} = I_C R_L + V_{CB}$$

$$R_L = \frac{V_{CC} - V_{CB}}{I_C} = \frac{20-5}{1\ \mathrm{mA}} = \mathbf{15\ K}$$

*[added] Verified: $10/10 = 1\ \mathrm{mA}$ ✓; $(20-5)/1\ \mathrm{mA} = 15\ \mathrm{k\Omega}$ ✓.
Sanity check: $1\ \mathrm{mA}\times15\ \mathrm{k\Omega} = 15\ \mathrm{V}$ dropped across $R_L$,
leaving $20-15 = 5\ \mathrm{V}$ at the collector ✓.*

### [ex] Example 57.9 — choose $R_E$ for a target $V_{BC}$ ·L3 p13–p14

**Statement.** For the circuit shown in Fig. 57.27(b), find the value of $R_E$ which causes
$V_{BC} = 10\ \mathrm{V}$.

[fig ·L3 p14] **Fig. 57.27(b).** A **PNP** in CB: $\mathbf{20\ V}$ at the top left feeding $R_E$
(value unlabelled — the unknown) with $I_E$ pointing **down** into the emitter;
$\mathbf{-20\ V}$ at the top right above $\mathbf{R_L = 20\ k}$ with $I_C$ pointing **up** out of the
collector; the **base grounded**; $\mathbf{V_{EB}}$ and $\mathbf{V_{BC} = 10\ V}$ marked; $I_B$
leaves the base downward.

**Solution** (the page's own)

$$I_C = \frac{V_{CC} - V_{BC}}{R_L} = \frac{20-10}{20\ \mathrm{K}} = 0.5\ \mathrm{mA}$$

$$I_E = \frac{I_C}{\alpha} \cong I_C = 0.5\ \mathrm{mA}$$

Neglecting $V_{BE}$, the whole of $V_{EE} = 20\ \mathrm{V}$ is dropped across $R_E$:

$$0.5\,R_E = 20 \quad\Longrightarrow\quad R_E = \frac{20}{0.5\ \mathrm{mA}} = \mathbf{40\ K}$$

*[added] Verified: $(20-10)/20 = 0.5\ \mathrm{mA}$ ✓; $20\ \mathrm{V}/0.5\ \mathrm{mA} = 40\ \mathrm{k\Omega}$ ✓. Note the mixed-unit shorthand in "$0.5\,R_E = 20$": with $I$ in mA and $R$ in
kΩ, $IR$ comes out directly in volts. **That shorthand is used throughout both chapters** and is
worth adopting — it removes almost every power-of-ten error.*

---

## 3.16 Common-emitter dc formulas ·L3 p14–p15

[derivation] Take the base–emitter circuit of Fig. 57.28. ·L3 p14

[eq: ce-base-current]

$$\boxed{\;I_B = \frac{V_{BB} - V_{BE}}{R_B} \cong \frac{V_{BB}}{R_B}\;}$$

[eq]

$$\boxed{\;I_C = \beta I_B\;}\qquad\text{(neglecting the leakage current } I_{CEO})$$

[eq: ce-vce]

$$\boxed{\;V_{CE} = V_{CC} - I_C R_L\;}$$

[fig ·L3 p14] **Fig. 57.28.** An **NPN** in CE, rail dialect: $\mathbf{+V_{BB} = 10\ V}$ over
$\mathbf{R_B = 1\ M}$ into the base ($I_B$ down); $\mathbf{+V_{CC} = 15\ V}$ over
$\mathbf{R_L = 10\ k}$ into the collector ($I_C$ down); the **emitter grounded** with $I_E$ leaving
downward; $V_{BE}$ marked from base to ground and $V_{CE}$ from collector to ground. An annotation
beside the transistor reads **"=100"**.

> ⚠ VERIFY **C3.3** ·L3 p14 — the $\beta$ glyph does not render in figure annotations: Fig. 57.28
> prints **"=100"** with nothing to the left of the equals sign. The same dropout affects **Fig.
> 57.30** (·L3 p15, "=100"), **Fig. 58.9** (·L3 p18, "=100"), **Fig. 58.10** (·L3 p19,
> "=100-150") and **Fig. 58.13** (·L3 p20, "=100"). In every case the intended annotation is
> $\beta = \ldots$, confirmed by the accompanying example statements. See `_verification-log.md`.

### [ex] Example 57.10 — the four CE quantities ·L3 p14

**Statement.** For the circuit of Fig. 57.28, find **(i)** $I_B$, **(ii)** $I_C$, **(iii)** $I_E$ and
**(iv)** $V_{CE}$. Neglect $V_{BE}$.

**Solution** (the page's own)

$$\text{(i)}\quad I_B \cong \frac{V_{BB}}{R_B} = \frac{10}{1\ \mathrm{M}} = \mathbf{10\ \mu A}$$

$$\text{(ii)}\quad I_C = \beta I_B = 100\times10\ \mathrm{\mu A} = \mathbf{1\ mA}$$

$$\text{(iii)}\quad I_E = I_B + I_C = 1\ \mathrm{mA} + 10\ \mathrm{\mu A} = \mathbf{1.01\ mA}$$

$$\text{(iv)}\quad V_{CE} = V_{CC} - I_C R_L = 15 - 1\times10 = \mathbf{5\ V}$$

*[added] Verified: $10\ \mathrm{V}/1\ \mathrm{M\Omega} = 10\ \mathrm{\mu A}$ ✓;
$100\times10\ \mathrm{\mu A} = 1\ \mathrm{mA}$ ✓; $1 + 0.01 = 1.01\ \mathrm{mA}$ ✓;
$1\ \mathrm{mA}\times10\ \mathrm{k\Omega} = 10\ \mathrm{V}$, so $15-10 = 5\ \mathrm{V}$ ✓. Taking $V_{BE} = 0.7$ into account
would give $I_B = 9.3\ \mathrm{\mu A}$, $I_C = 0.93\ \mathrm{mA}$ and $V_{CE} = 5.7\ \mathrm{V}$ —
worth knowing how much the "neglect $V_{BE}$" instruction is worth.*

> ⚠ VERIFY **C3.11** ·L3 p14 — part (iv) prints $V_{CE} = V_{CC} - I_C R_C$ while the collector
> resistor in Fig. 57.28 is labelled $\mathbf{R_L}$. The two symbols are used interchangeably for the
> collector load throughout both chapters. Nothing computed changes.

### [ex] Example 57.11 — the exact emitter current of a two-supply emitter bias circuit ·L3 p14

*(Electronics-1, Bangalore Univ. 1989)*

**Statement.** Find the **exact** value of the emitter current $I_E$ in the two-supply emitter bias
circuit of Fig. 57.29.

[fig ·L3 p14] **Fig. 57.29.** An **NPN**: $V_{CC}$ at the top feeding $R_L$ into the collector ($I_C$
down); the **base** fed through $\mathbf{R_B}$ down to ground ($I_B$ arrow pointing up towards the
base); the **emitter** through $\mathbf{R_E}$ down to $\mathbf{-V_{EE}}$ ($I_E$ arrow pointing down);
$\mathbf{+V_{BE}}$ marked at the base.

[derivation] Apply KVL to the loop containing $R_B$, $R_E$ and $V_{EE}$, starting from the emitter
and going clockwise: ·L3 p14

$$-I_E R_E + V_{EE} - I_B R_B - V_{BE} = 0$$

$$I_E R_E + I_B R_B = V_{EE} - V_{BE} \qquad \ldots(i)$$

Now $\beta = I_C/I_B \cong I_E/I_B$, so $I_B \cong I_E/\beta$. Substituting into (i):

$$I_E R_E + \frac{I_E R_B}{\beta} = V_{EE} - V_{BE}$$

[eq: two-supply-ie]

$$\boxed{\;I_E = \frac{V_{EE} - V_{BE}}{R_E + R_B/\beta}\;}$$

**Since in most cases $R_B/\beta \ll R_E$:** ·L3 p14

$$\boxed{\;I_E = \frac{V_{EE} - V_{BE}}{R_E} \cong \frac{V_{EE}}{R_E}\;}$$

> [added] **This is the headline property of two-supply emitter bias.** With $R_B/\beta$ negligible,
> $I_E$ depends only on $V_{EE}$ and $R_E$ — **$\beta$ has vanished from the bias equation**. §58.13
> (·L3 p21) returns to exactly this point.

### [ex] Example 57.12 — a full two-supply bias calculation ·L3 p15

**Statement.** In the circuit of Fig. 57.30, find **(i)** $I_E$, **(ii)** $I_B$, **(iii)** $I_C$ and
**(iv)** $V_{CE}$. Neglect $V_{BE}$ and take $\beta = 100$.

[fig ·L3 p15] **Fig. 57.30.** An **NPN**: $\mathbf{V_{CC} = 30\ V}$ at the top over
$\mathbf{R_L = 10\ K}$ into the collector **C** ($I_C$ down); the base **B** fed through
$\mathbf{R_B = 20\ K}$ down to **ground** ($I_B$ up); the emitter **E** through
$\mathbf{R_E = 30\ K}$ down to $\mathbf{V_{EE} = -30\ V}$ ($I_E$ down); $\mathbf{V_{CE}}$ marked from
the collector node downward; the annotation **"=100"** beside the transistor (see **C3.3**).

**Solution** (the page's own)

$$\text{(i)}\quad I_E = \frac{V_{EE}}{R_E + R_B/\beta} = \frac{30}{30 + 20/100} = \frac{30}{30.2}
\cong \mathbf{1\ mA}$$

$$\text{(ii)}\quad I_B \cong \frac{I_E}{\beta} = \frac{1}{100} = \mathbf{0.01\ mA}$$

$$\text{(iii)}\quad I_C = I_E - I_B = 1 - 0.01 = \mathbf{0.99\ mA}$$

$$\text{(iv)}\quad V_{CE} = V_{CC} - I_C R_L = 30 - 10\times0.99 = \mathbf{20.1\ V}$$

*[added] Verified: $30/30.2 = 0.9934\ \mathrm{mA} \approx 1\ \mathrm{mA}$ ✓; $0.99\ \mathrm{mA}\times 10\ \mathrm{k\Omega} = 9.9\ \mathrm{V}$, so $30-9.9 = 20.1\ \mathrm{V}$ ✓. Note also how small the
$R_B/\beta = 0.2\ \mathrm{k\Omega}$ term is against $R_E = 30\ \mathrm{k\Omega}$ — 0.7 %, exactly the
condition Example 57.11 assumed.*

> [added] **Why part (iv) is legitimate here even though the emitter is not grounded.** In general
> $V_{CE} = V_C - V_E$, and $V_E = -V_{EE} + I_E R_E$. Here $V_E = -30 + (1\ \mathrm{mA})(30\ \mathrm{k\Omega}) = 0\ \mathrm{V}$, so the emitter happens to sit at ground potential and
> $V_{CE} = V_C$. **That coincidence is specific to these numbers**; do not carry
> $V_{CE} = V_{CC} - I_C R_L$ into a two-supply problem without checking $V_E$ first.

> ⚠ VERIFY **C3.12** ·L3 p15 — part (i) prints the result as *"$\cong]$1 mA"*, with a stray closing
> bracket. Nothing computed changes.

---

## 3.17 Common-collector dc formulas ·L3 p15

[fig ·L3 p15] **Fig. 57.31** — the CC circuit with proper dc biasing sources, drawn twice.
**(a)** An **NPN** with the **base at the left** fed through $R_B$ from $V_{BB}$ ($I_B$ arrow up on
the left branch); the **emitter leaving at the top**, passing left-to-right through $\mathbf{R_E}$
drawn along the **top** of the diagram, then down the right-hand side ($I_E$ arrow down) into
$V_{CC}$; the **collector at the bottom**, tied to the node the two batteries share ($I_C$ arrow up
into it). **(b)** The same circuit rearranged: base at the left through $R_B$ from $V_{BB}$; the
**collector leaving at the top** and running right ($I_C$ arrow pointing left along the top rail)
into $V_{CC}$; the **emitter leaving downward** through $\mathbf{R_E}$ ($I_E$ arrow down) to the
bottom rail. *"The two circuits given in Fig. 57.31 represent the same thing."* ·L3 p15

[fig ·L3 p15] **Fig. 57.32** — the same stage from a **single** supply, i.e. the **emitter
follower**. **(a)** $\mathbf{+V_{CC}}$ along the top; $R_B$ hangs from the rail down and across into
the base ($I_B$ arrow pointing left along the top branch); the **collector connects directly to the
rail** ($I_C$ arrow down); $\mathbf{R_E}$ runs from the emitter down to ground; $\mathbf{V_{out}}$ is
taken between the emitter node and ground. **(b)** The same with the terminals named: $\mathbf{C}$ at
the top on the $+V_{CC}$ rail, $\mathbf{B}$ at the left with $\mathbf{V_{IN}}$ applied between base
and ground, $\mathbf{E}$ at the emitter above $R_E$, and $\mathbf{V_{out}}$ across $R_E$.

**Two things the text flags about Fig. 57.32:** ·L3 p15

- **the load resistor is not in the collector lead but in the emitter lead**;
- **the input is between base and collector, the output between emitter and collector** — which,
  with the collector on the supply rail (an ac ground), is what makes it a common-collector stage.

[eq: cc-formulas] **The CC bias formulas** ·L3 p15

$$\boxed{\;I_E = \frac{V_{CC} - V_{BE}}{R_E + R_B/\beta}\;}$$

$$\boxed{\;V_{CC} = V_{CE} + I_E R_E\;}$$

$$\boxed{\;I_C = \beta I_B\;}$$

> ### ⚠ VERIFY **V3.12** ·L3 p15 — the third formula in the box is for $I_B$, not $I_E$, and its denominator is wrong
>
> The page prints, as the third member of the same formula box:
> $$I_E = \frac{V_{CC} - V_{BE}}{R_E + \beta R_E}$$
>
> **Correct form:**
> $$\boxed{\;I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta R_E}\;}$$
>
> **Why — three independent checks.**
> 1. **Self-consistency.** The *first* member of the same box already gives
>    $I_E = (V_{CC}-V_{BE})/(R_E + R_B/\beta)$. Multiplying numerator and denominator of that by
>    $\beta$ gives $I_E = \beta(V_{CC}-V_{BE})/(\beta R_E + R_B)$, hence
>    $I_B = I_E/\beta = (V_{CC}-V_{BE})/(R_B + \beta R_E)$. The two printed forms cannot both be
>    $I_E$.
> 2. **The base resistor disappears.** As printed, $R_E + \beta R_E = (1+\beta)R_E$ contains **no
>    $R_B$ at all** — the bias current would not depend on the base resistor, which is false for this
>    circuit.
> 3. **What follows it.** The very next item in the box is $I_C = \beta I_B$, which only has an $I_B$
>    to use if the preceding formula produced one.
>
> See `_verification-log.md`.

### [exercise] Example 57.13 — stated but not solvable from this extract ·L3 p15

**Statement as printed.** In the CC circuit of Fig. 57.33, find **(a)** $I_B$, **(b)** $I_E$,
**(c)** $V_{CE}$, **(d)** $V_E$ and **(e)** $V_B$. Take $\beta = 49$ and $V_{BE} = 0.7\ \mathrm{V}$.

> ⚠ ILLEGIBLE ·L3 p15 — **needs a screenshot: Fig. 57.33 and the solution to Example 57.13**, i.e.
> printed page 2205 of the source textbook. Chapter 57 ends at printed page 2204 in this PDF, so the
> circuit's supply voltage and resistor values are simply not present.
>
> **[added] What can be said without the figure.** The method is fixed even though the numbers are
> not. For an emitter follower biased as in Fig. 57.32:
> $$I_B = \frac{V_{CC} - V_{BE}}{R_B + (1+\beta)R_E},\qquad I_E = (1+\beta)I_B,$$
> $$V_E = I_E R_E,\qquad V_B = V_E + V_{BE},\qquad V_{CE} = V_{CC} - V_E$$
> With $\beta = 49$, $(1+\beta) = 50$ — the round number is the giveaway that the intended circuit
> uses the exact $(1+\beta)$ form rather than the $\beta$ approximation. **No values are supplied
> here, because none can be recovered from the pages given.**

---

# Chapter 58 — Load Lines and DC Bias Circuits ·L3 p16–p25

> **The extract resumes at printed page 2223.** Printed pages 2205–2222 — the end of chapter 57
> (including §57.24, the **β-rule**) and §§58.1–58.2 — are **not in the PDF**. ·L3 p16 opens on the
> last two lines of a worked example belonging to §58.2.

**The surviving fragment of that example** ·L3 p16

$$V_{CC} = I_B R_B + V_{BE}$$

$$R_B = \frac{V_{CC} - V_{BE}}{I_B} = \frac{20 - 0.7}{20\times10^{-6}} = \mathbf{965\ K}$$

*[added] Verified: $19.3/20\times10^{-6} = 965{,}000\ \Omega$ ✓. The data behind it: $V_{CC} = 20\ \mathrm{V}$, $V_{BE} = 0.7\ \mathrm{V}$ (silicon), target $I_B = 20\ \mathrm{\mu A}$. This is the
base-bias design equation, and it reappears as the first step of §3.21.*

---

## 3.18 Why a transistor must be biased, and what moves the Q-point ·L3 p16

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $Q$-point | quiescent operating point, $(V_{CE},\,I_C)$ with no signal | (V, A) | (6 V, 2 mA) |
| $I_{CO}$ | reverse saturation (leakage) current of the C/B junction | A (µA) | 5 µA |
| $S$ | current stability factor, $dI_C/dI_{CO}$ | dimensionless | 1 (CB) to $1+\beta$ (CE) |
| $K_\beta$ | beta sensitivity | dimensionless | 0 to 1 |

[def] For normal operation of a transistor **amplifier** circuit it is essential that there is ·L3 p16

**(a)** a **forward bias** on the emitter–base junction, and
**(b)** a **reverse bias** on the collector–base junction.

**In addition, the *amount* of bias matters**, because it establishes the **Q-point**, which is
dictated by the intended mode of operation. ·L3 p16

**If the transistor is not biased correctly it will** ·L3 p16

1. **work inefficiently**, and
2. **produce distortion in the output signal**.

**And it is desirable that, once selected, the Q-point should not shift** — for instance with a
temperature rise. *"Unfortunately, this does not happen in practice unless special efforts are made
for the purpose."* ·L3 p16

[fig ·L3 p16] **Fig. 58.7** — a base-biased CE amplifier. $\mathbf{V_{CC} = 20\ V}$ along the top;
$\mathbf{R_B}$ drawn as a **rheostat** from the rail to the base; $\mathbf{R_L = 10\ K}$ from the
rail to the collector; the signal source $\mathbf{V_S}$ in series with $\mathbf{R_S}$ feeding the
base through coupling capacitor $\mathbf{C_1}$; the collector feeding $\mathbf{V_{out}}$ through
coupling capacitor $\mathbf{C_2}$; the **emitter grounded**.

### §58.4 What makes the bias drift ·L3 p16

[def] **Bias instability is the direct result of thermal instability**, which is itself produced by a
**cumulative increase in $I_C$** that, unchecked, leads to **thermal runaway**. ·L3 p16

[eq: ic-with-leakage] The collector current of a CE circuit: ·L3 p16

$$\boxed{\;I_C = \beta I_B + I_{CEO} = \beta I_B + (1+\beta)\,I_{CO}\;}$$

**This equation has three variables — $\beta$, $I_B$ and $I_{CO}$ — and all three increase with
temperature.** ·L3 p16

[derivation] **The runaway loop, in the book's own order:** ·L3 p16

1. temperature rises, so $I_{CO}$ rises;
2. an increase in $I_{CO}$ produces a **significant** increase in $I_C$ (because it is multiplied by
   $(1+\beta)$);
3. a larger $I_C$ means **increased power dissipation**;
4. increased dissipation raises the temperature further, and hence $I_C$ again;
5. **being a cumulative process, it can lead to thermal runaway, which will destroy the transistor.**

**The cure, stated as a design objective:** if by some circuit modification $I_C$ can be made to
*decrease* with temperature automatically, then the **decrease in the $\beta I_B$ term can be made
to neutralise the increase in the $(1+\beta)I_{CO}$ term**, keeping $I_C$ constant. That is thermal
stability, and hence bias stability. ·L3 p16

---

## 3.19 Stability factor and beta sensitivity ·L3 p16–p17

[def] **Stability factor $S$** — the degree of success achieved in stabilising $I_C$ against
variations in $I_{CO}$. It is the **rate of change of $I_C$ with respect to $I_{CO}$, with $\beta$
and $I_B$ (i.e. $V_{BE}$) held constant**: ·L3 p16

[eq: stability-factor]

$$\boxed{\;S = \frac{dI_C}{dI_{CO}}\;}\qquad (\beta,\ I_B\ \text{constant})$$

**The larger $S$, the greater the thermal instability** — the page notes, correctly, that *"in view
of the above, this factor should more appropriately be called instability factor!"* ·L3 p16

[derivation] **The alternative expression.** Differentiate $I_C = \beta I_B + (1+\beta)I_{CO}$ with
respect to $I_C$: ·L3 p16

$$1 = \beta\frac{dI_B}{dI_C} + (1+\beta)\frac{dI_{CO}}{dI_C}
= \beta\frac{dI_B}{dI_C} + (1+\beta)\frac{1}{S}$$

$$\frac{1+\beta}{S} = 1 - \beta\frac{dI_B}{dI_C}$$

[eq]

$$\boxed{\;S = \frac{1+\beta}{1 - \beta\,(dI_B/dI_C)}\;}$$

> ⚠ VERIFY **C3.13** ·L3 p16 — the source equation prints as *"$I_C = I\beta + (I + \beta)\, I_{CO}$"* — an upright $I$ where $\beta I_B$ and $(1+\beta)$ belong — and the differentiated line
> opens *"$I = \beta\,dI_B/dI_C + \ldots$"*, where the left-hand side is $\mathbf{1}$ (being
> $dI_C/dI_C$). The result quoted after it, $S = (1+\beta)/(1 - \beta\,dI_B/dI_C)$, is correct and
> can only follow from a left-hand side of 1. A digit-1/letter-I substitution; nothing computed
> changes. See `_verification-log.md`.

[eq: stability-factor-general] **The general formula, which works for any of the bias circuits:**
·L3 p16

$$\boxed{\;S = \frac{1 + R_B/R_E}{1 + (1-\alpha)\,(R_B/R_E)}\;}$$

where ·L3 p17

- $R_B$ = **total series parallel resistance in the base**, Ω;
- $R_E$ = **total series dc resistance in the emitter**, Ω;
- $\alpha$ = dc alpha of the transistor.

> [added] **The equivalent form used everywhere in §§58.10–58.14.** Substituting
> $1-\alpha = 1/(1+\beta)$:
> $$\boxed{\;S = \frac{1 + R_B/R_E}{1 + R_B/(1+\beta)R_E} \;\cong\; \frac{1 + R_B/R_E}{1 + R_B/\beta R_E}\;}$$
> Every stability factor in the rest of the chapter is this expression with $R_B$ and $R_E$ read off
> the particular circuit. **Learn it in this form** — it is the one the examples use.

### §58.6 Beta sensitivity ·L3 p17

[def] **$\beta$-sensitivity** measures the influence the value of $\beta$ has on the dc operating
point. Variations in $\beta$ come from changes in operating conditions **or from substituting one
transistor for another**. ·L3 p17

[eq: beta-sensitivity]

$$\boxed{\;\frac{dI_C}{I_C} = K_\beta\,\frac{d\beta}{\beta}\;}
\qquad\Longleftrightarrow\qquad
\boxed{\;K_\beta = \frac{\beta}{I_C}\cdot\frac{dI_C}{d\beta}\;}$$

**$K_\beta$ is a dimensionless ratio and can take values from zero to unity.** ·L3 p17

> ### ⚠ VERIFY **V3.13** ·L3 p17 — beta sensitivity is printed against $I_B$, not $\beta$
>
> The page prints
> $$\frac{dI_C}{I_C} = K_\beta\,\frac{dI_B}{\beta}\qquad\text{and}\qquad
> K_\beta = \frac{\beta}{I_C}\cdot\frac{dI_C}{dI_B}$$
>
> **Correct form:**
> $$\boxed{\;\frac{dI_C}{I_C} = K_\beta\,\frac{d\beta}{\beta},\qquad
> K_\beta = \frac{\beta}{I_C}\cdot\frac{dI_C}{d\beta}\;}$$
>
> **Why — dimensional, and the page contradicts itself one line later.** The left-hand side
> $dI_C/I_C$ is a pure number. The printed right-hand side is $K_\beta\,dI_B/\beta$, which has units
> of **amperes** ($dI_B$ in A, $\beta$ dimensionless). The very next sentence asserts that *"$K_\beta$
> is a dimensionless ratio"* — impossible if the defining equation carries amperes. The quantity
> named "beta sensitivity" must be defined against a change in $\beta$.
> See `_verification-log.md`.

### §58.7 Stability factor for CB and CE ·L3 p17

[derivation] **(i) CB circuit.** Here $I_C = \alpha I_E + I_{CO}$, so differentiating with respect to
$I_{CO}$ at constant $I_E$: ·L3 p17

$$\frac{dI_C}{dI_{CO}} = 0 + 1$$

[eq: s-cb]

$$\boxed{\;S = 1\;}\qquad\text{(common-base)}$$

[derivation] **(ii) CE circuit.** Here $I_C = \beta I_B + (1+\beta)I_{CO}$, and treating $I_B$ as a
constant: ·L3 p17

$$\frac{dI_C}{dI_{CO}} = (1+\beta)$$

[eq: s-ce]

$$\boxed{\;S = 1+\beta\;}\qquad\text{(common-emitter)}$$

**If $\beta = 100$ then $S = 101$, which means $I_C$ changes 101 times as much as $I_{CO}$.** ·L3 p17

> [added] **This single comparison is the reason the whole of chapter 58 exists.** $S = 1$ in CB and
> $S = 101$ in CE: the configuration with useful gain is the one that amplifies its own leakage a
> hundredfold. Every biasing scheme that follows is an attempt to pull $S$ back down towards 1.

---

## 3.20 The six methods of biasing ·L3 p17

[table] The book's own list, with its own figure references. ·L3 p17

| # | Method | Figure | What the book says about it |
|---|---|---|---|
| 1 | **base bias** (fixed current bias) | Fig. 58.9 | *"Not a very satisfactory method because bias voltages and currents do not remain constant during transistor operation."* |
| 2 | **base bias with emitter feedback** | Fig. 58.10 | *"Achieves good stability of dc operating point against changes in $\beta$ with the help of emitter resistor which causes degeneration to take place."* |
| 3 | **base bias with collector feedback** | Fig. 58.11 | Also called **collector-to-base bias** or **collector feedback bias**. *"Provides better bias stability."* |
| 4 | **base bias with collector and emitter feedbacks** | — | *"A combination of (2) and (3) above."* |
| 5 | **emitter bias with two supplies** | Fig. 58.13 | Uses both a positive and a negative supply. **The base sits at approximately 0 V**, $V_B \cong 0$. |
| 6 | **voltage divider bias** | Fig. 58.15 | *"Most widely used in linear discrete circuits because it provides good bias stability."* Also called the **universal bias circuit** or **base bias with one supply**. |

> ⚠ VERIFY **C3.14** ·L3 p17 — the figure numbers in this list do not all agree with the figures as
> they later appear. The list cites Fig. 58.9 for base bias, but Fig. 58.9 on ·L3 p18 is the
> *emitter-feedback* circuit of Example 58.5; it cites Fig. 58.10 for emitter feedback, but Fig.
> 58.10 on ·L3 p19 is a *plain base-bias* circuit; and it cites Figs. 58.13 and 58.15 for two-supply
> and divider bias, which on ·L3 p20–p21 are the *collector-and-emitter-feedback* circuit and the
> divider *example* circuit respectively (the general circuits being Figs. 58.14 and 58.16). Work
> from the figure captions on the page, not from this list. Nothing computed changes.
> See `_verification-log.md`.

### §58.9 Base bias ·L3 p17

The page says base bias *"has already been discussed in Art. 58.20 and is shown in Fig. 58.25"*, and
records its two figures of merit: ·L3 p17

$$\boxed{\;S = (1+\beta) \cong \beta,\qquad K_\beta = 1\;}$$

> ⚠ VERIFY **C3.15** ·L3 p17 — §58.9 is a *forward* reference to Art. 58.20 and Fig. 58.25, both of
> which lie beyond the extract (the chapter's own base-bias circuit appears as Fig. 58.7 on ·L3 p16
> and as Fig. 58.10 on ·L3 p19). It cannot be checked from the pages supplied. Nothing computed
> changes.

> [added] **Read those two numbers as the baseline against which every other scheme is measured.**
> $S \cong \beta$ is the worst possible stability factor, and $K_\beta = 1$ means the Q-point moves
> in exact proportion to $\beta$ — swap the transistor for one with twice the gain and $I_C$ doubles.
> Example 58.6 (§3.21) demonstrates exactly that.

---

## 3.21 Base bias with emitter feedback ·L3 p18–p19

[def] The circuit is base bias **with an emitter resistor added**. ·L3 p18

[fig ·L3 p18] **Fig. 58.8.** An **NPN**, rail dialect. $\mathbf{+V_{CC}}$ along the top;
$\mathbf{R_B}$ from the rail to the base ($I_B$ down); $\mathbf{R_L}$ from the rail to the collector
($I_C$ down); $\mathbf{R_E}$ from the emitter to **ground** ($I_E$ down). Marked on the right-hand
side: $\mathbf{V_{CE}}$ from collector to emitter, $\mathbf{V_C}$ from collector to ground,
$\mathbf{V_E}$ from emitter to ground; and $\mathbf{+V_{BE}}$ at the base.

**1. Saturation.** At saturation $V_{CE}$ is essentially zero, so $V_{CC}$ is distributed over $R_L$
and $R_E$: ·L3 p18

[eq: ic-sat-general]

$$\boxed{\;I_{C(sat)} = \frac{V_{CC}}{R_E + R_L}\;}$$

**2. The actual collector current.** [derivation] Take the supply–base–emitter–ground route and
apply KVL: ·L3 p18

$$-I_B R_B - V_{BE} - I_E R_E + V_{CC} = 0$$

$$V_{CC} = I_B R_B + V_{BE} + I_E R_E \qquad\ldots(i)$$

Now $I_B = I_C/\beta$ and $I_E \cong I_C$; substituting into (i):

$$V_{CC} \cong \frac{I_C R_B}{\beta} + V_{BE} + I_C R_E$$

[eq: emitter-feedback-ic]

$$\boxed{\;I_C \cong \frac{V_{CC} - V_{BE}}{R_E + R_B/\beta} \cong \frac{V_{CC}}{R_E + R_B/\beta}\;}
\qquad\text{(the right-hand form neglects } V_{BE})$$

*(The page notes this could also have been obtained from the β-rule of Art. 57.24 — a section outside
this extract; see **C3.23**.)* ·L3 p18

**3. Collector-to-ground voltage** ·L3 p18

$$\boxed{\;V_C = V_{CC} - I_C R_L\;}$$

**4. Emitter-to-ground voltage** ·L3 p18

$$\boxed{\;V_E = I_E R_E \cong I_C R_E\;}$$

**5. Stability factor** ·L3 p18

$$\boxed{\;S = \frac{1 + R_B/R_E}{1 + R_B/(1+\beta)R_E} = \frac{1 + R_B/R_E}{1 + R_B/\beta R_E}\;}$$

**6. Beta sensitivity** ·L3 p18

[eq: kbeta-emitter-feedback]

$$\boxed{\;K_\beta = \frac{1}{1 + \beta R_E/R_B}\;}$$

> [added] **Read (6) as a design rule.** $K_\beta$ is small — i.e. the Q-point is insensitive to
> $\beta$ — when $\beta R_E \gg R_B$. That is the whole point of the emitter resistor: **the larger
> $R_E$ relative to $R_B/\beta$, the more $\beta$ drops out of the bias equation.** Compare with
> plain base bias, where $R_E = 0$ and $K_\beta = 1$.

### [ex] Example 58.5 — the six quantities of an emitter-feedback stage ·L3 p18

**Statement.** For the circuit shown in Fig. 58.9, find **(i)** $I_{C(sat)}$, **(ii)** $I_C$,
**(iii)** $V_C$, **(iv)** $V_E$, **(v)** $V_{CE}$ and **(vi)** $K_\beta$.

[fig ·L3 p18] **Fig. 58.9.** An **NPN**: $\mathbf{V_{CC} = 30\ V}$ at the top; $\mathbf{R_B = 300\ K}$
from the rail to the base; $\mathbf{R_L = 2\ K}$ from the rail to the collector ($I_C$ down);
$\mathbf{R_E = 1\ K}$ from the emitter to ground ($I_E$ down); the annotation **"=100"** beside the
transistor (i.e. $\beta = 100$ — see **C3.3**); $\mathbf{V_{CE}}$, $\mathbf{V_C}$ and $\mathbf{V_E}$
marked down the right-hand side.

**Solution** (the page's own)

$$\text{(i)}\quad I_{C(sat)} = \frac{V_{CC}}{R_E + R_L} = \frac{30}{1+2} = \mathbf{10\ mA}$$

$$\text{(ii)}\quad I_C \cong \frac{V_{CC}}{R_E + R_B/\beta} = \frac{30}{1 + 300/100}
= \frac{30}{4} = \mathbf{7.5\ mA}$$

$$\text{(iii)}\quad V_C = V_{CC} - I_C R_L = 30 - 2\times7.5 = \mathbf{15\ V}$$

$$\text{(iv)}\quad V_E \cong I_E R_E \cong I_C R_E = 7.5\times1 = \mathbf{7.5\ V}$$

$$\text{(v)}\quad V_{CE} = V_C - V_E = 15 - 7.5 = \mathbf{7.5\ V}$$

$$\text{(vi)}\quad K_\beta = \frac{1}{1 + 100\times1/300} = \frac{1}{1.3333} = \mathbf{0.75}$$

*[added] Verified: $30/3 = 10$ ✓; $30/4 = 7.5$ ✓; $7.5\ \mathrm{mA}\times2\ \mathrm{k\Omega} = 15\ \mathrm{V}$, $30-15 = 15\ \mathrm{V}$ ✓; $7.5\times1 = 7.5\ \mathrm{V}$ ✓; $15-7.5 = 7.5\ \mathrm{V}$
✓; $1/(1+0.3333) = 0.75$ ✓. Cross-check on (v) via $V_{CE} = V_{CC} - I_C(R_L+R_E) = 30 - 7.5(3) = 7.5\ \mathrm{V}$ ✓. Note $K_\beta = 0.75$ — still poor: this stage's $I_C$ moves three quarters as
much as $\beta$ does.*

> ### ⚠ VERIFY **C3.4** ·L3 p18, p19, p24 — a minus sign is set as a multiplication sign, three times
>
> The same typographic fault appears in three collector-voltage equations:
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·L3 p18, Example 58.5(iii) | $V_C = V_{CC} \times I_C R_L = 30 - 2\times7.5 = 15\ \mathrm{V}$ | $V_C = V_{CC} - I_C R_L$ |
> | ·L3 p19, §58.11 | $I_B R_B + V_{BE} \cong V_{CC} \times I_C R_L$ | $\cong V_{CC} - I_C R_L$ |
> | ·L3 p24, §58.15 | $V_{CE} = V_{CC} \times I_C R_L = 10 - 2\times2 = 6\ \mathrm{V}$ | $V_{CE} = V_{CC} - I_C R_L$ |
>
> **Why it is only cosmetic.** In each case the arithmetic printed immediately to the right of the
> equals sign performs the correct **subtraction**, and each page states the correct general form
> elsewhere (·L3 p18 item 3, ·L3 p19 two lines later, ·L3 p14 §57.22). Note, though, that as printed
> each expression is **dimensionally impossible** — $\mathrm{V}\times\mathrm{V} = \mathrm{V^2}$.
> See `_verification-log.md`.

### [ex] Example 58.6 — what a temperature rise does to a base-biased Q-point ·L3 p18–p19

**Statement.** The base-biased transistor circuit of Fig. 58.10 is subjected to an increase in
junction temperature from **25 °C to 75 °C**. If $\beta$ increases from **100 to 150** with rising
temperature, calculate the **percentage change in the Q-point values $(I_C,\ V_{CE})$** over the
temperature range. Assume $V_{BE}$ remains constant at 0.7 V.

[fig ·L3 p19] **Fig. 58.10.** A plain **base-biased NPN**: $\mathbf{+12\ V}$ ($V_{CC}$) at the top;
$\mathbf{R_C = 500}$ (ohms) from the rail to the collector ($I_C$ down); $\mathbf{R_B = 100\ K}$ from
a left-hand branch of the same rail into the base; the **emitter grounded**. Annotation
**"=100-150"** beside the transistor (i.e. $\beta = 100$ to $150$ — see **C3.3**). There is **no
emitter resistor** — this is method 1 of §58.8, not method 2.

**Solution** (the page's own)

**At 25 °C, $\beta = 100$:**

$$I_B = \frac{V_{CC} - V_{BE}}{R_B} = \frac{12 - 0.7}{100\times10^{3}} = 0.113\ \mathrm{mA}$$

$$I_C = \beta I_B = 100\times0.113 = 11.3\ \mathrm{mA}$$

$$V_{CE} = V_{CC} - I_C R_C = 12 - (11.3\times10^{-3}\times500) = 6.35\ \mathrm{V}$$

**At 75 °C, $\beta = 150$** *(the page heads this block "At 25°" — see V3.14)*:

$$I_B = 0.113\ \mathrm{mA}\qquad\text{(unchanged — } I_B \text{ is set by } R_B \text{ alone)}$$

$$I_C = \beta I_B = 150\times0.113 = 16.95\ \mathrm{mA}$$

$$V_{CE} = 12 - (16.95\times10^{-3}\times500) = 3.52\ \mathrm{V}$$

**Percentage changes:**

$$\%\,\Delta I_C = \frac{16.95 - 11.3}{11.3}\times100 = \mathbf{50\ \%\ (increase)}$$

$$\%\,\Delta V_{CE} = \frac{3.52 - 6.35}{6.35}\times100 = \mathbf{-44.57\ \%\ (decrease)}$$

**It is seen that the Q-point is very much dependent on temperature, and this makes the base-bias
arrangement very unstable.** ·L3 p19

*[added] Verified: $11.3/100000\times1000 = 0.113\ \mathrm{mA}$ ✓; $11.3\times10^{-3}\times500 = 5.65\ \mathrm{V}$, $12-5.65 = 6.35\ \mathrm{V}$ ✓; $16.95\times10^{-3}\times500 = 8.475\ \mathrm{V}$,
$12-8.475 = 3.525\ \mathrm{V}$ ✓ (printed 3.52); $5.65/11.3 = 50.0\ \%$ ✓; $2.83/6.35 = 44.57\ \%$ ✓.
**Note that $I_C$ moves by exactly the same 50 % as $\beta$ does** — $K_\beta = 1$ for base bias,
just as §58.9 states.*

> ### ⚠ VERIFY **V3.14** ·L3 p19 — the 75 °C block is headed "At 25°"
>
> The page prints **"At 25°"** as the heading over the working $I_B = 0.113\ \mathrm{mA}$,
> $I_C = 150\times0.113 = 16.95\ \mathrm{mA}$, $V_{CE} = 3.52\ \mathrm{V}$.
>
> **Correct: At 75 °C.**
>
> **Why.** $\beta = 150$ is, by the question's own statement, the **75 °C** value; the 25 °C block
> ($\beta = 100$, $I_C = 11.3\ \mathrm{mA}$, $V_{CE} = 6.35\ \mathrm{V}$) sits immediately above it,
> and the percentage changes that follow are computed **between the two blocks** — which is only
> meaningful if they are at different temperatures. As printed, the page appears to give two
> different answers for 25 °C. See `_verification-log.md`.

> ⚠ VERIFY **C3.17** ·L3 p19 — the same example's first $V_{CE}$ line prints
> *"$V_{CE} = I_C R_C = 12 - (11.3\times10\text{–}3\times500) = 6.35\ \mathrm{V}$"*: the left-hand
> side is missing $V_{CC} -$, and the exponent $-3$ is flattened onto the line as "10–3". The line
> is then repeated as *"$V_{CE} = V_{CC} - I_C R_C = 12 \times (11.3\times10\times3\times500) = 6.35\ \mathrm{V}$"*, this time with the correct left-hand side but with the minus set as $\times$ and the
> exponent broken up further. Both printed results are the correct 6.35 V. Nothing computed changes.

---

## 3.22 Base bias with collector feedback ·L3 p19–p20

[def] Like base bias, **except that the base resistor is returned to the collector rather than to
the $V_{CC}$ supply**. Also called **collector-to-base bias** or **collector feedback bias**. ·L3 p19

[fig ·L3 p19] **Fig. 58.11.** An **NPN**: $V_{CC}$ at the top feeding $\mathbf{R_L}$, whose current
is labelled $\mathbf{(I_C + I_B)}$, down to the **collector node**; from that same collector node,
$\mathbf{R_B}$ runs **left and back into the base** (with $I_B$ arrowed towards the base); the
**emitter grounded**; $\mathbf{V_{BE}}$ marked from base ($+$) to ground ($-$) and $\mathbf{V_{CE}}$
from collector to ground.

[derivation] **Why it stabilises — the feedback loop in the book's own words:** ·L3 p19

1. suppose $\beta$ somehow increases;
2. $I_C$ increases, and so does $I_C R_L$;
3. therefore $V_C$ **decreases** — and $V_C$ is the voltage applied across $R_B$;
4. consequently $I_B$ decreases,
5. which **partially compensates for the original increase in $\beta$**.

**(i) Saturation** — since $V_{CE} = 0$ at saturation: ·L3 p19

$$\boxed{\;I_{C(sat)} = \frac{V_{CC}}{R_L}\;}$$

**(ii) Actual collector current.** [derivation] Two expressions for the collector voltage: ·L3 p19

$$V_C = V_{CC} - (I_B + I_C)R_L \cong V_{CC} - I_C R_L$$

$$V_C = I_B R_B + V_{BE}$$

Equating them, and putting $I_B = I_C/\beta$:

$$I_B R_B + V_{BE} \cong V_{CC} - I_C R_L$$

$$\frac{I_C}{\beta}R_B + V_{BE} \cong V_{CC} - I_C R_L$$

[eq: collector-feedback-ic]

$$\boxed{\;I_C = \frac{V_{CC} - V_{BE}}{R_L + R_B/\beta} \cong \frac{V_{CC}}{R_L + R_B/\beta}\;}$$

**This is also the approximate value of $I_E$.** ·L3 p19

**(iii) Beta sensitivity and stability factor** ·L3 p19

[eq: kbeta-collector-feedback]

$$\boxed{\;K_\beta = \frac{1}{1 + \beta R_L/R_B} = 1 - \frac{I_C}{I_{C(sat)}}\;}$$

$$\boxed{\;S = \frac{1 + R_B/R_L}{1 + R_B/(1+\beta)R_L}\;}$$

> ### ⚠ VERIFY **V3.15** ·L3 p19 — $K_\beta$ is printed without its "$1 +$"
>
> The page prints:
> $$K_\beta = \frac{1}{\beta R_L/R_B} = 1 - \frac{I_C}{I_{C(sat)}}$$
>
> **Correct form:**
> $$\boxed{\;K_\beta = \frac{1}{1 + \beta R_L/R_B}\;}$$
>
> **Why — the page's two expressions disagree with each other.** Substituting
> $I_C = V_{CC}/(R_L + R_B/\beta)$ and $I_{C(sat)} = V_{CC}/R_L$ into the right-hand expression:
> $$1 - \frac{I_C}{I_{C(sat)}} = 1 - \frac{R_L}{R_L + R_B/\beta}
> = \frac{R_B/\beta}{R_L + R_B/\beta} = \frac{1}{1 + \beta R_L/R_B}$$
> which is the corrected left-hand form, not the printed one.
>
> **Numerical confirmation from the very next example.** Example 58.7 has $R_L = 1\ \mathrm{K}$,
> $R_B = 100\ \mathrm{K}$, $\beta = 100$. The printed formula gives $1/(100\times1/100) = 1.0$; the
> corrected formula gives $1/(1+1) = 0.5$ — **and ·L3 p20 part (iv) evaluates
> $1/(1 + 100\times1/100) = 0.5$**, i.e. the example itself uses the corrected form.
> See `_verification-log.md`.

> ### ⚠ VERIFY **V3.16** ·L3 p19 — the "approximation" offered for $S$ is a current, not a ratio
>
> The page prints:
> $$S = \frac{1 + R_B/R_L}{1 + R_B/(1+\beta)R_L} \;\cong\; \frac{V_{CC}}{R_L + R_B/\beta}$$
>
> **Correct: there is no such approximation.** The right-hand expression is the formula for $I_C$,
> printed six lines earlier on the same page.
>
> **Why — dimensional.** $S = dI_C/dI_{CO}$ is **dimensionless**, while
> $V_{CC}/(R_L + R_B/\beta)$ has units of **current**. For Example 58.7's numbers the printed
> "approximation" evaluates to $12/2 = 6$ (milliamps), whereas the correct $S$ is
> $(1+100)/(1 + 100/101) = 50.75$ — different by a factor of eight and in the wrong unit.
> Use the left-hand expression. See `_verification-log.md`.

### [ex] Example 58.7 — a collector-feedback stage in full ·L3 p19–p20

**Statement.** In Fig. 58.11, $V_{CC} = 12\ \mathrm{V}$, $V_{BE} = 0.7\ \mathrm{V}$,
$R_L = 1\ \mathrm{K}$, $R_B = 100\ \mathrm{K}$, $\beta = 100$. Find **(i)** $I_C$, **(ii)** $V_{CE}$,
**(iii)** $I_B$, **(iv)** $K_\beta$ and **(v)** $S$.

**Solution** (the page's own)

$$\text{(i)}\quad I_C \cong I_E = \frac{12 - 0.7}{1 + 100/100} = \frac{11.3}{2} = 5.65\ \mathrm{mA}$$

$$\text{(ii)}\quad V_{CE} \cong 12 - (5.65\times1) = \mathbf{6.35\ V}$$

$$\text{(iii)}\quad I_B = \frac{I_C}{\beta} = \frac{5.65}{100} = \mathbf{56.5\ \mu A}$$

$$\text{(iv)}\quad K_\beta = \frac{1}{1 + 100\times1/100} = \mathbf{0.5}$$

$$\text{(v)}\quad S = \frac{1 + 100/1}{1 + 100\times1/101} = \mathbf{50.5}$$

*[added] Verified: $11.3/2 = 5.65\ \mathrm{mA}$ ✓; $12 - 5.65 = 6.35\ \mathrm{V}$ ✓;
$5.65/100 = 0.0565\ \mathrm{mA} = 56.5\ \mathrm{\mu A}$ ✓; $1/2 = 0.5$ ✓. **(v) does not check out
exactly** — see C3.19.*

> ⚠ VERIFY **C3.18** ·L3 p20 — part (i)'s answer is bolded as **5.6 mA**, but the expression beside
> it, $11.3/2$, is $\mathbf{5.65\ mA}$, and parts (ii) and (iii) both go on to use 5.65. Also, part
> (iv) prints the symbol as $K_B$ (upright capital B subscript) rather than $K_\beta$. Nothing
> computed changes.

> ⚠ VERIFY **C3.19** ·L3 p20 — part (v) prints the answer as **50.5**, but the expression it is
> printed beside evaluates to
> $$S = \frac{1 + 100/1}{1 + 100\times1/101} = \frac{101}{1.9901} = \mathbf{50.75}$$
> The printed 50.5 is $101/2$, i.e. the denominator rounded from 1.9901 to 2. A 0.5 % rounding slip;
> nothing physical changes. See `_verification-log.md`.

> [added] **The comparison worth drawing.** Base bias gives $K_\beta = 1$ and $S \cong \beta = 100$.
> Collector feedback with these components gives $K_\beta = 0.5$ and $S \cong 50$ — **both halved**,
> from one resistor moved. It is still a long way from good; §3.25's voltage divider is what actually
> fixes the problem.

---

## 3.23 Base bias with collector *and* emitter feedback ·L3 p20

[def] Both feedbacks used together, *"in an attempt to reduce circuit sensitivity to changes in
$\beta$"*. ·L3 p20

[derivation] **How the two feedbacks combine:** if $\beta$ increases, the **emitter voltage rises**
but the **collector voltage falls**; the voltage across $R_B$ — which is $V_C - V_B$ — is therefore
reduced from both ends at once, causing $I_B$ to decrease and **partially offsetting the increase in
$\beta$**. ·L3 p20

[fig ·L3 p20] **Fig. 58.12.** An **NPN**: $\mathbf{+V_{CC}}$ at the top over $\mathbf{R_L}$, whose
current is labelled $\mathbf{(I_C + I_B)}$, into the **collector node**; $\mathbf{R_B}$ from that
collector node left and back into the **base** ($I_B$ arrowed); $\mathbf{R_E}$ from the emitter down
to **ground** ($I_E$ down); $\mathbf{V_{CE}}$, $\mathbf{V_C}$ and $\mathbf{V_E}$ marked down the
right-hand side.

**Saturation**, assuming $I_B$ negligible against $I_C$ so that $V_{CC}$ divides over $R_L$ and
$R_E$: ·L3 p20

$$\boxed{\;I_{C(sat)} = \frac{V_{CC}}{R_E + R_L}\;}$$

[eq: both-feedbacks-ic] **Actual collector current**, going *via* $R_B$ because $V_{CE}$ is unknown:
·L3 p20

$$\boxed{\;I_C = \frac{V_{CC} - V_{BE}}{R_E + R_L + R_B/\beta}\;}$$

**The node voltages** ·L3 p20

$$\boxed{\;V_C = V_{CC} - (I_C + I_B)R_L \cong V_{CC} - I_C R_L\;}$$

$$\boxed{\;V_E = I_E R_E \cong I_C R_E\;}$$

$$\boxed{\;V_{CE} = V_C - V_E \cong V_{CC} - I_C(R_L + R_E)\;}$$

**Stability factor and beta sensitivity** ·L3 p20

$$\boxed{\;S = \frac{1 + R_B/(R_E + R_L)}{1 + R_B/\beta(R_E + R_L)}\;}$$

[eq: kbeta-both-feedbacks]

$$\boxed{\;K_\beta = \frac{1}{1 + \beta(R_E + R_L)/R_B} = 1 - \frac{I_C}{I_{C(sat)}}\;}$$

**Obviously, $K_\beta$ will be degraded with an increase in $R_B$.** ·L3 p20

> [added] **Note the pattern across §§58.10–58.12.** Every one of these three circuits has
> $$K_\beta = \frac{1}{1 + \beta R_{\text{fb}}/R_B},\qquad
> S = \frac{1 + R_B/R_{\text{fb}}}{1 + R_B/\beta R_{\text{fb}}}$$
> where the "feedback resistance" $R_{\text{fb}}$ is $R_E$ for emitter feedback, $R_L$ for collector
> feedback, and $\mathbf{R_E + R_L}$ when both are present. **Learn the pattern, not three
> formulas.** Note also that this section's $K_\beta$ **does** carry the leading "$1 +$" that §58.11's
> printed version dropped — independent confirmation of **V3.15**.

### [ex] Example 58.8 — a stage with both feedbacks ·L3 p20

**Statement.** For the circuit shown in Fig. 58.13, find **(a)** $I_{C(sat)}$, **(b)** $V_{CE}$ and
**(c)** $K_\beta$. Neglect $V_{BE}$ and take $\beta = 100$.

[fig ·L3 p20] **Fig. 58.13.** An **NPN**: $\mathbf{15\ V}$ at the top; $\mathbf{R_L = 10\ K}$ down to
the **collector node** ($I_C$ down through it); from that node a wire runs **left through
$\mathbf{R_B = 500\ K}$, down, and back into the base**; the emitter runs down through
$\mathbf{R_E = 10\ K}$ to **ground** (arrow down); output terminals tap the collector node and the
emitter node, with $\mathbf{V_{CE}}$ marked between them; the annotation **"=100"** beside the
transistor (see **C3.3**).

**Solution** (the page's own)

$$\text{(a)}\quad I_{C(sat)} = \frac{15}{10+10} = \mathbf{0.75\ mA}$$

$$\text{(b)}\quad I_C = \frac{V_{CC}}{R_E + R_L + R_B/\beta}
= \frac{15}{10 + 10 + 500/100} = \frac{15}{25} = 0.6\ \mathrm{mA}$$

$$V_{CE} = 15 - 0.6\,(10 + 10) = 15 - 12 = \mathbf{3\ V}$$

$$\text{(c)}\quad K_\beta = \frac{1}{1 + 100(10+10)/500} = \frac{1}{5} = \mathbf{0.2}$$

$$\text{or}\quad K_\beta = 1 - \frac{I_C}{I_{C(sat)}} = 1 - \frac{0.6}{0.75} = \mathbf{0.2}$$

> ### ⚠ VERIFY **V3.17** ·L3 p20 — the base resistance in part (c) is printed as 50, not 500
>
> The page prints: $K_\beta = \dfrac{1}{1 + 100(10+10)/\mathbf{50}} = 0.2$.
>
> **Correct form:**
> $$\boxed{\;K_\beta = \frac{1}{1 + \beta(R_E+R_L)/R_B} = \frac{1}{1 + 100(20)/500}
> = \frac{1}{5} = 0.2\;}$$
>
> **Why.** $R_B$ is **500 K** in Fig. 58.13. Evaluated as printed, $1/(1 + 2000/50) = 1/41 = 0.024$ —
> not the 0.2 the page reports. The page's own second route, $1 - I_C/I_{C(sat)} = 1 - 0.6/0.75 = 0.2$, confirms 0.2, and 0.2 is what $R_B = 500$ gives. See `_verification-log.md`.

*[added] Verified: $15/20 = 0.75\ \mathrm{mA}$ ✓; $15/25 = 0.6\ \mathrm{mA}$ ✓; $0.6\times20 = 12\ \mathrm{V}$, $15-12 = 3\ \mathrm{V}$ ✓; $1/(1+4) = 0.2$ ✓; $1 - 0.8 = 0.2$ ✓. $K_\beta = 0.2$ against
0.5 for collector feedback alone and 1.0 for plain base bias — the two feedbacks together are worth
a factor of five.*

> ⚠ VERIFY **C3.20** ·L3 p20 — §58.12's node-voltage line is broken by the typesetting:
> *"$V_C = V_{CC} - (I_C + I_B)$; $\;R_L \cong V_{CC} - I_C R_L$"*, with a semicolon separating
> $R_L$ from the bracket it multiplies. The intended line is
> $V_C = V_{CC} - (I_C + I_B)R_L \cong V_{CC} - I_C R_L$. As printed the first expression is volts
> minus amperes; the second, on the same line, is correct. Nothing computed changes.

---

## 3.24 Emitter bias with two supplies ·L3 p20–p21

[def] The circuit *"gives a reasonably stable Q-point and is widely used whenever two supplies
(positive and negative) are available. Its popularity is due to the fact that $I_C$ is essentially
independent of $\beta$."* ·L3 p20

**Its defining property:** the **base sits at approximately zero volts**, $V_B \cong 0$, and hence
·L3 p17, p21

$$\boxed{\;V_E = -V_{BE}\;}$$

[fig ·L3 p21] **Fig. 58.14.** An **NPN**: $\mathbf{+V_{CC}}$ at the top over $\mathbf{R_L}$ into the
collector ($I_C$ down); the **base** taken through a resistor on the left down to **ground** ($I_B$
arrowed into the base); the **emitter** taken down through a resistor to $\mathbf{-V_{EE}}$ ($I_E$
down); $\mathbf{V_{BE}}$ marked with $+$ at the base and $-$ at the emitter.

> ### ⚠ VERIFY **V3.19** ·L3 p21 — Fig. 58.14 labels both resistors $R_E$
>
> The base resistor (left branch, to ground) and the emitter resistor (right branch, to $-V_{EE}$)
> are **both labelled $\mathbf{R_E}$** on the figure.
>
> **Correct: the base resistor is $\mathbf{R_B}$.**
>
> **Why.** Every equation in the surrounding derivation — $I_B R_B + I_E R_E = V_{EE} - V_{BE}$,
> $I_E = (V_{EE}-V_{BE})/(R_E + R_B/\beta)$, $S$, $K_\beta$ — uses $R_B$ for the base resistor and
> $R_E$ for the emitter resistor as **two distinct quantities**, and Example 58.9's Fig. 58.15 gives
> them different values ($R_B = 10\ \mathrm{K}$, $R_E = 20\ \mathrm{K}$). As labelled, the figure has
> no $R_B$ at all. See `_verification-log.md`.

[derivation] **Starting from ground and going clockwise round the base–emitter circuit:** ·L3 p21

$$-I_B R_B - V_{BE} - I_E R_E + V_{EE} = 0$$

$$I_B R_B + I_E R_E = V_{EE} - V_{BE} \qquad\ldots(i)$$

With $I_B = I_C/\beta \cong I_E/\beta$:

$$\frac{I_E R_B}{\beta} + I_E R_E = V_{EE} - V_{BE}$$

[eq: two-supply-ie]

$$\boxed{\;I_E = \frac{V_{EE} - V_{BE}}{R_E + R_B/\beta}\;}$$

**If $V_{EE} \gg V_{BE}$ and $R_E \gg R_B/\beta$:** ·L3 p21

$$\boxed{\;I_E \cong \frac{V_{EE}}{R_E}\;}$$

> ### ⚠ VERIFY **V3.18** ·L3 p21 — the simplified emitter current is printed over $R_B$
>
> The page prints: *"If $V_{EE} \gg V_{BE}$ and $R_E \gg R_B/\beta$, $I_E = V_{EE}/R_B$."*
>
> **Correct form:**
> $$\boxed{\;I_E \cong \frac{V_{EE}}{R_E}\;}$$
>
> **Why.** Dropping the two small terms from $I_E = (V_{EE}-V_{BE})/(R_E + R_B/\beta)$ leaves
> $V_{EE}/R_E$ — the surviving denominator is the one the condition says is *large*, not the one it
> says is small. The identical result is printed correctly as $I_E = (V_{EE}-V_{BE})/R_E \cong V_{EE}/R_E$ in §57.22 on ·L3 p14, and Example 58.9 uses $R_E$. Numerically, with Example 58.9's
> values the printed form gives $10/10 = 1\ \mathrm{mA}$ against the correct $10/20 = 0.5\ \mathrm{mA}$ — a factor of two. See `_verification-log.md`.

[derivation] **Emitter-to-ground voltage** ·L3 p21

$$-I_B R_B - V_{BE} - V_E = 0$$

$$\boxed{\;V_E = -(I_B R_B + V_{BE}) = -\left(V_{BE} + \frac{I_C R_B}{\beta}\right) \cong -V_{BE}\;}$$

**Stability factor and beta sensitivity** ·L3 p21

$$\boxed{\;S = \frac{1 + R_B/R_E}{1 + R_B/\beta R_E}\;}\qquad
\boxed{\;K_\beta = \frac{1}{1 + \beta R_E/R_B}\;}$$

*(the same pattern as §3.21, with the same $R_{\text{fb}} = R_E$)*

### [ex] Example 58.9 — a two-supply emitter bias stage in full ·L3 p21

*(Electronics-II, Bangalore Univ. 1995)*

**Statement.** For the circuit of Fig. 58.15, find **(i)** $I_E$, **(ii)** $I_C$, **(iii)** $V_C$,
**(iv)** $V_E$, **(v)** $V_{CE}$, **(vi)** the stability factor and **(vii)** $K_\beta$, for a
$\beta$ of **50**. Take $V_{BE} = 0.7\ \mathrm{V}$.

[fig ·L3 p21] **Fig. 58.15.** An **NPN**: $\mathbf{+20\ V}$ at the top over $\mathbf{R_L = 10\ K}$
into the collector; $\boldsymbol{\beta = 50}$ printed beside the transistor; $\mathbf{R_B = 10\ K}$
from the base down to **ground**; $\mathbf{R_E = 20\ K}$ from the emitter down to $\mathbf{-10\ V}$.

**Solution** (the page's own)

$$\text{(i)}\quad I_E = \frac{V_{EE} - V_{BE}}{R_E + R_B/\beta} = \frac{10 - 0.7}{20 + 10/50}
= \frac{9.3}{20.2} = \mathbf{0.46\ mA}$$

$$\text{(ii)}\quad I_C \cong I_E = \mathbf{0.46\ mA}$$

$$\text{(iii)}\quad V_C = V_{CC} - I_C R_L = 20 - 0.46\times10 = \mathbf{15.4\ V}$$

$$\text{(iv)}\quad V_E = -\left(V_{BE} + \frac{I_C R_B}{\beta}\right)
= -(0.7 + 0.46\times10/50) = \mathbf{-0.8\ V}$$

$$\text{(v)}\quad V_{CE} = V_C - V_E = 15.4 - (-0.8) = \mathbf{16.2\ V}$$

$$\text{(vi)}\quad S = \frac{1 + R_B/R_E}{1 + R_B/\beta R_E} = \frac{1 + 10/20}{1 + 10/(50\times20)}
= \frac{1.5}{1.01} = \mathbf{1.485}$$

$$\text{(vii)}\quad K_\beta = \frac{1}{1 + \beta R_E/R_B} = \frac{1}{1 + 50\times20/10}
= \frac{1}{101} \cong \mathbf{0.01}$$

*[added] Verified: $9.3/20.2 = 0.4604\ \mathrm{mA}$ ✓; $0.46\times10 = 4.6$, $20-4.6 = 15.4\ \mathrm{V}$ ✓; $0.46\times10/50 = 0.092$, $-(0.7+0.092) = -0.792 \approx -0.8\ \mathrm{V}$ ✓;
$15.4+0.8 = 16.2\ \mathrm{V}$ ✓; $1.5/1.01 = 1.4851$ ✓; $1/101 = 0.0099$ ✓.*

> ### ⚠ VERIFY **V3.20** ·L3 p21 — the stability-factor denominator in (vi) is self-referential
>
> The page prints the general form as
> $$S = \frac{1 + R_B/R_E}{1 + R_B/\beta R_{\mathbf{B}}}$$
>
> **Correct form:**
> $$\boxed{\;S = \frac{1 + R_B/R_E}{1 + R_B/\beta R_E}\;}$$
>
> **Why.** $R_B/\beta R_B = 1/\beta$, which deletes $R_E$ from the denominator entirely — $S$ would
> then be independent of the emitter resistor, contradicting the general formula given three lines
> above on the same page and the whole point of emitter degeneration. The **numeric substitution on
> the same line uses 20**, i.e. $R_E$: "$1 + 10/50\times20$". See `_verification-log.md`.

> ### ⚠ VERIFY **V3.21** ·L3 p21 — the beta-sensitivity formula in (vii) invents a symbol and loses $\beta$
>
> The page prints
> $$K_\beta = \frac{1}{1 + R_E/R_\beta}$$
>
> **Correct form:**
> $$\boxed{\;K_\beta = \frac{1}{1 + \beta R_E/R_B}\;}$$
>
> **Why.** $R_\beta$ is not a defined quantity anywhere in either chapter. The correct expression is
> printed four lines earlier in the same section, and the numeric substitution on the same line,
> "$1 + 50\times20/10$", is exactly $1 + \beta R_E/R_B$ with $\beta = 50$, $R_E = 20\ \mathrm{K}$,
> $R_B = 10\ \mathrm{K}$. See `_verification-log.md`.

> ⚠ VERIFY **C3.21** ·L3 p21 — part (iv) prints
> *"$V_E = -(V_{BE} + I_C R_B/\beta) = (0.7 + 0.46\times10/50) = -0.8\ \mathrm{V}$"*: the **leading
> minus sign is missing from the middle expression**, which therefore reads $+0.792$ while the answer
> beside it reads $-0.8\ \mathrm{V}$. The first and last forms are correct. Nothing computed changes.

> [added] **Look at what this circuit achieves.** $S = 1.485$ and $K_\beta = 0.01$ — against
> $S \cong 100$, $K_\beta = 1$ for plain base bias. Both are within a factor of 1.5 of the ideal
> ($S = 1$, $K_\beta = 0$). **This is what "essentially independent of $\beta$" means**, and it is
> bought entirely by making $R_E \gg R_B/\beta$: here $R_B/\beta = 0.2\ \mathrm{k\Omega}$ against
> $R_E = 20\ \mathrm{k\Omega}$, a ratio of 100.

---

## 3.25 Voltage divider bias ·L3 p21–p23

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $R_1$, $R_2$ | upper and lower arms of the base potential divider | Ω (kΩ) | 14 kΩ, 6 kΩ |
| $V_2$ | voltage across $R_2$, i.e. the base voltage before $V_{BE}$ | V | 4–6 V |
| $V_{th}$, $V_{BB}'$ | Thevenin voltage of the divider | V | = $V_2$ |
| $R_{th}$, $R_B'$ | Thevenin resistance of the divider, $R_1\parallel R_2$ | Ω (kΩ) | 4.2–20 kΩ |
| $V_B$ | base-to-ground voltage | V | — |

[def] The arrangement *"commonly used for transistors incorporated in integrated circuits"*, and the
**most widely used** discrete bias circuit. Its name comes from the fact that **$R_1$ and $R_2$ form
a potential divider across $V_{CC}$**. The book's footnote records its other name: **Universal Bias
Stabilization Circuit**. ·L3 p21

**How it works:** the voltage drop $V_2$ across $R_2$ **forward-biases the emitter**, while the
$V_{CC}$ supply **reverse-biases the collector**. ·L3 p21

[fig ·L3 p21] **Fig. 58.16.** An **NPN**: $\mathbf{+V_{CC}}$ along the top; $\mathbf{R_1}$ from the
rail down to the **base node**; $\mathbf{R_2}$ from the base node down to **ground**, with
$\mathbf{V_2}$ marked across it ($+$ at the top, $-$ at the bottom); $\mathbf{R_L}$ from the rail to
the collector; $\mathbf{R_E}$ from the emitter to ground with $I_E$ arrowed down; $\mathbf{V_{BE}}$
marked at the base–emitter, and $\mathbf{V_{CE}}$, $\mathbf{V_C}$, $\mathbf{V_E}$ down the right-hand
side.

### Method 1 — by inspection (the "approximate method") ·L3 p21–p22

[eq: divider-v2] By the voltage-divider theorem, **assuming the base draws negligible current**:

$$\boxed{\;V_2 = V_{CC}\cdot\frac{R_2}{R_1 + R_2}\;}$$

$$\boxed{\;V_E = V_2 - V_{BE}\;}$$

[eq: divider-ie]

$$\boxed{\;I_E = \frac{V_E}{R_E} = \frac{V_2 - V_{BE}}{R_E} \cong \frac{V_2}{R_E}\;}$$

$$\boxed{\;V_C = V_{CC} - I_C R_L\;}$$

[eq: divider-vce] ·L3 p22

$$V_{CE} = V_C - V_E = V_{CC} - I_C R_L - I_E R_E$$

$$\boxed{\;V_{CE} \cong V_{CC} - I_C(R_L + R_E)\;}\qquad (I_C \cong I_E)$$

$$\boxed{\;I_{C(sat)} \cong \frac{V_{CC}}{R_L + R_E}\;}$$

> **The point of the whole circuit, in the book's own sentence:** *"It is seen from above
> calculations that the value of $\beta$ was never used anywhere. The base voltage is set by $V_{CC}$
> and $R_1$ and $R_2$. The dc bias circuit is independent of transistor $\beta$. That is why it is
> such a very popular bias circuit."* ·L3 p22

**Stability factor and beta sensitivity** — with $R_B = R_1\parallel R_2$: ·L3 p22

[eq: kbeta-divider]

$$\boxed{\;K_\beta = \frac{1}{1 + \beta R_E/(R_1\parallel R_2)}\;}$$

$$\boxed{\;S = \frac{1 + (R_1\parallel R_2)/R_E}{1 + (R_1\parallel R_2)/(1+\beta)R_E}
\cong \frac{1 + (R_1\parallel R_2)/R_E}{1 + (R_1\parallel R_2)/\beta R_E}\;}$$

> ⚠ VERIFY **C3.22** ·L3 p22 — the first form of $S$ prints its numerator denominator as $R_e$
> (lower-case e) where $R_E$ is meant; the second form on the next line has $R_E$ correctly. The
> lower-case $r_e$ is, elsewhere in analogue electronics, the **small-signal emitter resistance** — a
> different quantity entirely. Nothing computed changes. See `_verification-log.md`.

### Method 2 — Thevenin's theorem (the "more accurate" method) ·L3 p22

[derivation] **Step 1.** *"Open the base lead at point $A$ and remove the transistor along with $R_L$
and $R_E$, thereby leaving the voltage divider circuit behind."* ·L3 p22

[fig ·L3 p22] **Fig. 58.17.** **(a)** $+V_{CC}$ at the top over $R_1$ down to node $\mathbf{B}$; from
B a lead goes right to an open terminal $\mathbf{A}$; $R_2$ runs from B to ground; the open-circuit
voltage between A and the lower terminal is labelled $\mathbf{V_2 = V_{th}}$. **(b)** The same network
with the supply replaced by a **ground symbol at the top**, so $R_1$ and $R_2$ appear in parallel
looking back into terminal A; the resistance is labelled $\mathbf{R_{th}}$ with an arrow pointing
into A. **(c)** The Thevenin equivalent driving the transistor: a source $\mathbf{V_{BB}}$ (drawn as
a dashed circle, annotated $\mathbf{V_{th}}$) in series with $\mathbf{R_B}$ (annotated
$\mathbf{R_{th}}$) into the base ($I_B$ arrowed); $\mathbf{+V_{CC}}$ over $\mathbf{R_L}$ into the
collector ($I_C$ down); $\mathbf{R_E}$ from the emitter to ground ($I_E$ down); $\mathbf{V_{BE}}$
marked $+$ at the base, $-$ at the emitter.

[eq: thevenin-divider] **Step 2 — the equivalent source:** ·L3 p22

$$\boxed{\;V_{th} = V_2 = V_{CC}\cdot\frac{R_2}{R_1+R_2}\;}\qquad
\boxed{\;R_{th} = R_1\parallel R_2 = \frac{R_1R_2}{R_1+R_2}\;}$$

The original circuit is thereby reduced to Fig. 58.17(c), where **$V_{th} = V_{BB}'$ and
$R_{th} = R_B'$**. ·L3 p22

[derivation] **Step 3 — KVL round the base–emitter loop:** ·L3 p22

$$V_{BB}' - I_B R_B' - V_{BE} - I_E R_E = 0$$

Substituting $I_E = (1+\beta)I_B$:

[eq: thevenin-ib]

$$\boxed{\;I_B = \frac{V_{BB}' - V_{BE}}{R_B' + (1+\beta)R_E}\;}$$

Or, substituting $I_B = I_E/(1+\beta)$ instead:

[eq: thevenin-ie]

$$\boxed{\;I_E = \frac{V_{BB}' - V_{BE}}{R_E + R_B'/(1+\beta)}\;}$$

$$\boxed{\;V_{CE} = V_{CC} - I_C R_L - I_E R_E \cong V_{CC} - I_C(R_L + R_E)\;}$$

### Method 3 — the $\beta$-rule ·L3 p22–p23

[def] **The $\beta$-rule as stated here:** when $R_E$ is transferred to the base circuit it becomes
$(1+\beta)R_E$, and it appears **in parallel with $R_2$**. ·L3 p22

[fig ·L3 p22] **Fig. 58.18.** $+V_{CC}$ along the top; $\mathbf{R_1}$ from the rail down to the base
node; from the base node, **two parallel branches to ground — $\mathbf{R_2}$ and
$\boldsymbol{(1+\beta)R_E}$** (the latter drawn as a vertical resistor with its value written
sideways); $\mathbf{R_L}$ from the rail to the collector; $\mathbf{V_B}$ marked at the base node
(with $+$ above and $-$ below) and $\mathbf{V_E}$ at the emitter.

**$V_{CC}$ therefore drops over $R_1$ and $R_2\parallel(1+\beta)R_E$**, so: ·L3 p22–p23

[eq: beta-rule-vb]

$$\boxed{\;V_B = V_{CC}\cdot\frac{R_2\parallel(1+\beta)R_E}{R_1 + R_2\parallel(1+\beta)R_E}\;}$$

$$\boxed{\;V_E = V_B - V_{BE},\qquad I_E = \frac{V_E}{R_E}\;}$$

> ⚠ VERIFY **C3.23** ·L3 p18, p22 — three cross-reference defects around the $\beta$-rule.
> (i) It is cited as **"Art. 57.24"** on ·L3 p18 and as **"Art. 58.12"** on ·L3 p22; Art. 58.12 in
> this chapter is *Base Bias with Collector and Emitter Feedbacks* and contains no $\beta$-rule, and
> Art. 57.24 lies on a page absent from the extract, so **neither reference can be followed**.
> (ii) ·L3 p22 refers to *"Fig. 8.18"*, meaning **Fig. 58.18**. (iii) ·L3 p22's Thevenin derivation
> says *"Substituting the value of $I_E = (1+\beta)I_B$ in (i) above"*, but **no equation on that
> page carries an $(i)$ tag** — the equation meant is the KVL line immediately above.
> Nothing computed changes. See `_verification-log.md`.

### [ex] Example 58.10 — a voltage-divider stage by inspection ·L3 p23

*(Electronics, Gorakhpur Univ.)*

**Statement.** For the circuit of Fig. 58.19, find **(a)** $I_{C(sat)}$, **(b)** $I_C$,
**(c)** $V_{CE}$ and **(d)** $K_\beta$. Neglect $V_{BE}$ and take $\beta = 50$.

[fig ·L3 p23] **Fig. 58.19.** An **NPN**: $\mathbf{20\ V}$ rail along the top; a divider of
$\mathbf{14\ K}$ (upper, $=R_1$) and $\mathbf{6\ K}$ (lower, $=R_2$) with $\mathbf{V_2}$ marked
across the lower arm ($+$ at its top); $\mathbf{2\ K}$ ($=R_L$) from the rail to the collector, with
$I_C$ arrowed down; $\mathbf{6\ K}$ ($=R_E$) from the emitter to ground; $\mathbf{V_{CE}}$ marked
between the two open output terminals at the collector and emitter. *(The resistors carry values but
not the symbol names $R_1$, $R_2$, $R_L$, $R_E$; the names come from the solution.)*

**Solution** (the page's own)

$$\text{(a)}\quad I_{C(sat)} = \frac{V_{CC}}{R_L + R_E} = \frac{20}{2+6} = \mathbf{2.5\ mA}$$

$$\text{(b)}\quad V_2 = 20\times\frac{6}{20} = 6\ \mathrm{V};\qquad
I_C \cong I_E \cong \frac{V_2}{R_E} = \frac{6}{6} = \mathbf{1\ mA}$$

$$\text{(c)}\quad V_{CE} = V_{CC} - I_C(R_L + R_E) = 20 - 1(2+6) = \mathbf{12\ V}$$

$$\text{(d)}\quad R_1\parallel R_2 = \frac{14\times6}{14+6} = \frac{84}{20} = 4.2\ \mathrm{K}$$

$$K_\beta = \frac{1}{1 + 50\times6/4.2} = \frac{1}{72.43} = \mathbf{0.0138}$$

*[added] Verified: $20/8 = 2.5\ \mathrm{mA}$ ✓; $20\times6/20 = 6\ \mathrm{V}$ ✓; $6/6 = 1\ \mathrm{mA}$ ✓; $20 - 8 = 12\ \mathrm{V}$ ✓; $84/20 = 4.2\ \mathrm{k\Omega}$ ✓;
$50\times6/4.2 = 71.43$, $1/72.43 = 0.01381$ ✓.*

### [ex] Example 58.11 — dc load line and Q-point, both methods compared ·L3 p23–p24

*(Electronics-I, M.S. Univ. 1991)*

**Statement.** For the circuit shown in Fig. 58.20(a), draw the dc load line and mark the Q-point of
the circuit. Assume **germanium** material with $V_{BB} = 0.3\ \mathrm{V}$ *(see V3.22)* and
$\beta = 50$.

> ### ⚠ VERIFY **V3.22** ·L3 p23 — the question specifies $V_{BB} = 0.3\ \mathrm{V}$; it means $V_{BE}$
>
> **Correct: $V_{BE} = 0.3\ \mathrm{V}$**, the germanium base–emitter drop.
>
> **Why — the two symbols collide inside this very problem.** $V_{BB}$ is the Thevenin base supply,
> and the solution computes it explicitly: $V_{BB} = 20\times25/125 = 4\ \mathrm{V}$. The 0.3 V is
> used in both halves of the solution as the junction drop: $I_E = (V_2 - V_{BE})/R_E = (4-0.3)/6$ and $I_B = (V_{BB}' - V_{BE})/(R_B' + (1+\beta)R_E) = (4-0.3)/(20+51\times6)$. Taken as
> printed, $V_{BB} = 0.3\ \mathrm{V}$ would leave the transistor cut off.
> See `_verification-log.md`.

[fig ·L3 p23] **Fig. 58.20.** **(a)** An **NPN**: $\mathbf{20\ V}$ rail; divider
$\mathbf{100\ K}$ (upper) and $\mathbf{25\ K}$ (lower); $\mathbf{4\ K}$ collector resistor;
$\mathbf{6\ K}$ emitter resistor to ground. **(b)** The same circuit **Thevenised**:
$\mathbf{20\ V}$ over the $\mathbf{4\ K}$ collector resistor ($I_C$ down),
$\mathbf{R_B = 20\ K}$ in series with a battery $\mathbf{V_{BB} = 4\ V}$ driving the base, and the
$\mathbf{6\ K}$ emitter resistor to ground ($I_E$ down).

**Solution — the load-line end points** ·L3 p23

$$V_{CC(cut\text{-}off)} = V_{CC} = 20\ \mathrm{V}$$

$$I_{C(sat)} = \frac{V_{CC}}{R_L + R_E} = \frac{20}{4+6} = 2\ \mathrm{mA}$$

**(a) Approximate method** ·L3 p23

$$V_2 = V_{CC}\cdot\frac{R_2}{R_1+R_2} = 20\times\frac{25}{125} = 4\ \mathrm{V}$$

$$I_E = \frac{V_2 - V_{BE}}{R_E} = \frac{4 - 0.3}{6} = 0.62\ \mathrm{mA}$$

$$V_{CE} = V_{CC} - I_C(R_L + R_E) = 20 - 0.62\times10 = \mathbf{13.8\ V}$$

**Q-point $(13.8\ \mathrm{V},\ 0.62\ \mathrm{mA})$**, shown in Fig. 58.21(a). ·L3 p23

**(b) Exact method, via the Thevenin circuit of Fig. 58.20(b)** ·L3 p23–p24

$$V_{BB} = 20\times\frac{25}{125} = 4\ \mathrm{V}$$

$$I_B = \frac{V_{BB}' - V_{BE}}{R_B' + (1+\beta)R_E} = \frac{4 - 0.3}{20 + 51\times6}
= \frac{3.7}{326} = 11.3\ \mathrm{\mu A}$$

$$I_C = \beta I_B = 50\times11.3 = 565\ \mathrm{\mu A} = 0.565\ \mathrm{mA}$$

$$I_E = (1+\beta)I_B = 51\times11.3 = 576\ \mathrm{\mu A} = 0.576\ \mathrm{mA}$$

$$V_{CE} = V_{CC} - I_C R_C - I_E R_E = 20 - 0.565\times4 - 0.576\times6 = \mathbf{14.3\ V}$$

**The new and more accurate Q-point is $(14.3\ \mathrm{V},\ 0.565\ \mathrm{mA})$**, shown in
Fig. 58.21(b). ·L3 p24

*[added] Verified: $20/10 = 2\ \mathrm{mA}$ ✓; $20\times25/125 = 4\ \mathrm{V}$ ✓;
$3.7/6 = 0.6167 \approx 0.62\ \mathrm{mA}$ ✓; $20 - 6.2 = 13.8\ \mathrm{V}$ ✓;
$20 + 306 = 326$, $3.7/326 = 0.011350\ \mathrm{mA} = 11.35\ \mathrm{\mu A}$ ✓;
$50\times11.35 = 567\ \mathrm{\mu A}$ (printed 565, from $\beta\times11.3$) ✓;
$51\times11.3 = 576.3\ \mathrm{\mu A}$ ✓;
$0.565\times4 = 2.26$, $0.576\times6 = 3.456$, $20 - 2.26 - 3.456 = 14.284 \approx 14.3\ \mathrm{V}$ ✓.*

> [added] **What the comparison is teaching.** The approximate method puts the Q-point at
> $(13.8, 0.62)$ and the exact method at $(14.3, 0.565)$ — a **9 % error in $I_C$**. The
> approximation fails here because $R_B' = 20\ \mathrm{k\Omega}$ is **not** negligible against
> $(1+\beta)R_E = 306\ \mathrm{k\Omega}$; it contributes 6 % of the denominator. Rule of thumb:
> the by-inspection method is safe when $R_2 \ll (1+\beta)R_E$, i.e. when the divider is *stiff*.

[fig ·L3 p23] **Fig. 58.21** — the two dc load lines. Both panels have $I_C$ in **mA** on the
vertical axis (marked 1, 2) and $V_{CE}$ in **volts** on the horizontal axis. **(a)** A straight
line from $(0,\,2\ \mathrm{mA})$ down to $(20\ \mathrm{V},\,0)$, ticks at 0, 5, 10, 15, 20 V; the
point **Q** is marked on the line, with a solid horizontal line back to $\mathbf{0.62}$ on the $I_C$
axis and a vertical drop to $\mathbf{13.8}$ on the $V_{CE}$ axis. **(b)** The same load line, ticks
at 0, 5, 10, 15; **Q** marked with **dashed** construction lines back to $\mathbf{0.565}$ on the
$I_C$ axis and down to $\mathbf{14.3}$ on the $V_{CE}$ axis.

> ⚠ VERIFY **C3.24** ·L3 p23 — two typesetting slips in this example: $I_C = \beta I_B = 50\times11.3$
> is set as *"50×l1.3"* (a lower-case letter **l** standing in front of the 1), and the emitter line prints
> *"$I_E = (1 + \beta\,I_B$"* with **no closing bracket** — it should read $I_E = (1+\beta)I_B$.
> Nothing computed changes.

---

## 3.26 The dc load line on the output characteristics ·L3 p24–p25

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_{CQ}$ | quiescent collector current | A (mA) | 2 mA |
| $V_{CEQ}$ | quiescent collector–emitter voltage | V | 6 V |
| $R_{ac}$ ($r_L$) | ac load resistance seen by the collector | Ω (kΩ) | — |
| $P_{ac}$, $P_{dc}$ | ac and dc power dissipated in $R_L$ | W (mW) | 0.81 mW, 8 mW |

**Why bother.** *"In order to study the effect of bias conditions on the performance of a CE circuit,
it is necessary to superimpose the dc load line on the transistor output ($V_{CE}/I_C$)
characteristics."* ·L3 p24

[fig ·L3 p24] **Fig. 58.22** — the CE amplifier under study, a silicon **NPN**.
$\mathbf{V_{CC} = 10\ V}$ at the top; $\mathbf{R_B = 470\ K}$ from the rail to the base;
$\mathbf{R_L = 2\ K}$ from the rail to the collector ($I_C$ down, $I_B$ down); the source
$\mathbf{v_S}$ in series with $\mathbf{R_S}$ coupled to the base through $\mathbf{C_1}$; the
collector coupled to $\mathbf{V_{out}}$ through $\mathbf{C_2}$; the **emitter grounded**;
$\boldsymbol{\beta = 100}$ printed beside the transistor; $\mathbf{V_{CE}}$ marked from collector to
ground.

[eq: dc-load-line] **The two end points of the dc load line** ·L3 p24

$$\boxed{\;I_{C(sat)} = \frac{V_{CC}}{R_L} = \frac{10}{2} = 5\ \mathrm{mA}\;}\qquad
\text{— point } B \text{ (on the } I_C \text{ axis)}$$

$$\boxed{\;V_{CE(cut\text{-}off)} = V_{CC} = 10\ \mathrm{V}\;}\qquad
\text{— point } A \text{ (on the } V_{CE} \text{ axis)}$$

**Locating the Q-point** ·L3 p24

$$I_B = \frac{V_{CC} - V_{BE}}{R_B} = \frac{10 - 0.7}{470} = 20\ \mathrm{\mu A}$$

$$I_C = \beta I_B = 100\times20 = 2000\ \mathrm{\mu A} = 2\ \mathrm{mA}$$

$$V_{CE} = V_{CC} - I_C R_L = 10 - 2\times2 = 6\ \mathrm{V}$$

**Q-point: $(6\ \mathrm{V},\ 2\ \mathrm{mA})$.** ·L3 p24

*[added] Verified: $9.3/470 = 0.01979\ \mathrm{mA} = 19.8\ \mathrm{\mu A}$ (the page rounds to
20 µA) ✓; $100\times20\ \mathrm{\mu A} = 2\ \mathrm{mA}$ ✓; $2\ \mathrm{mA}\times2\ \mathrm{k\Omega} = 4\ \mathrm{V}$, $10-4 = 6\ \mathrm{V}$ ✓. The Q-point sits at $V_{CC}/2$ — mid-way along the load
line, which is where a class-A stage wants it.* *(The $V_{CE}$ line prints its minus as $\times$ —
see **C3.4**.)*

[fig ·L3 p24] **Fig. 58.23** — the load line drawn on the CE output characteristics, with the signal
swing constructed on it. This is the busiest figure in the lesson; described piece by piece:

- **Axes.** $I_C$ in **mA** vertically, ticks at 2, 4, 5. $V_{CE}$ in **volts** horizontally, with
  the special values **4.2, 6, 7.8** and **10** marked.
- **Curve family.** Five characteristics, labelled from the top **$I_B = 50\ \mathrm{\mu A}$**,
  **40**, **30**, **20**, **10** — each rising steeply from the origin, kneeing, then running nearly
  flat.
- **Load line.** A straight line from **$B$** at $(0,\,5\ \mathrm{mA})$ on the $I_C$ axis down to
  **$A$** at $(10\ \mathrm{V},\,0)$ on the $V_{CE}$ axis.
- **Q-point.** Marked **$Q$** where the load line crosses the **20 µA** curve, at
  $(6\ \mathrm{V},\ 2\ \mathrm{mA})$.
- **Signal extremes.** **$C$** where the load line crosses the **30 µA** curve, at
  $(4.2\ \mathrm{V},\ 2.9\ \mathrm{mA})$; **$D$** where it crosses the **10 µA** curve, at
  $(7.8\ \mathrm{V},\ 1.1\ \mathrm{mA})$. Dashed horizontal and vertical construction lines run from
  $C$, $Q$ and $D$ to both axes.
- **Waveforms.** To the **right** of the characteristics, an $I_C$-against-$t$ sinusoid oscillating
  between **2.9 mA** and **1.1 mA** about the 2 mA mean, with both levels marked by dashed lines
  carried across from the characteristic. **Below** the characteristics, a $V_{out}$-against-$t$
  sinusoid swinging between the 4.2 V and 7.8 V dashed verticals — **inverted** relative to the
  current waveform. A further sinusoid drawn along a 45° dashed corridor and labelled $I_B$
  represents the input base current swinging the operating point up and down the load line.

### Reading the signal swing off the load line ·L3 p24

Suppose an ac input injects a sinusoidal base current of **peak value 10 µA** into the circuit of
Fig. 58.22. It swings the operating point up and down the load line. ·L3 p24

| Half-cycle | $I_B$ | Point | $I_C$ | $V_{CE} = 10 - 2I_C$ |
|---|---|---|---|---|
| positive | $20+10 = 30\ \mathrm{\mu A}$ | $C$ | 2.9 mA | $10 - 5.8 = 4.2\ \mathrm{V}$ |
| quiescent | $20\ \mathrm{\mu A}$ | $Q$ | 2.0 mA | $10 - 4.0 = 6.0\ \mathrm{V}$ |
| negative | $20-10 = 10\ \mathrm{\mu A}$ | $D$ | 1.1 mA | $10 - 2.2 = 7.8\ \mathrm{V}$ |

**So $V_{CE}$ falls from 6 V to 4.2 V — a peak of 1.8 V — when the base current goes positive, and
rises from 6 V to 7.8 V — again a peak of 1.8 V — when it goes negative.** Since changes in $V_{CE}$
*are* changes in output voltage, an input signal makes $I_B$ vary according to the signal amplitude,
which makes $I_C$ vary, which produces the output voltage variations. ·L3 p24–p25

> ⚠ VERIFY **C3.25** ·L3 p24 — two mA/µA slips in this passage. The page says the positive
> half-cycle puts the Q-point *"on the $(20+10) = 30$ **mA** line"* — the curve is
> $30\ \mathrm{\mu A}$, and the symmetric sentence one line later correctly says *"the $(20-10) = 10\ \mathrm{\mu A}$ line"*. It then says *"at point $D$, $I_C$ measures $1.1\ \mathrm{\mu A}$"* —
> the arithmetic that follows, $10 - 2\times1.1 = 7.8\ \mathrm{V}$, and Fig. 58.23 itself both give
> **1.1 mA**. Nothing computed changes. See `_verification-log.md`.

### The same swing seen as a voltage across $R_L$ ·L3 p25

*"Variations in voltage drop across $R_L$ are exactly the same as in $V_{CE}$."* ·L3 p25

$$\text{no signal:}\quad I_C R_L = 2\times2 = 4\ \mathrm{V}$$
$$\text{positive half-cycle:}\quad 2\times2.9 = 5.8\ \mathrm{V}$$
$$\text{negative half-cycle:}\quad 2\times1.1 = 2.2\ \mathrm{V}$$

$$\text{voltage variation} = 5.8 - 4 = 1.8\ \mathrm{V}\ \text{(positive half-cycle)}$$
$$= 4 - 2.2 = 1.8\ \mathrm{V}\ \text{(negative half-cycle)}$$

[eq] **rms output voltage variation** ·L3 p25

$$V_{rms} = \frac{1.8}{\sqrt{2}} = 1.27\ \mathrm{V}$$

[eq: power-in-load] **Power dissipated in $R_L$** ·L3 p25

$$P_{ac} = \frac{V_{rms}^2}{R_L} = \frac{1.27^2}{2} = 0.81\ \mathrm{mW}$$

$$P_{dc} = I_C^2 R_L = 2^2\times2 = 8\ \mathrm{mW}$$

$$\boxed{\;P_{total} = P_{dc} + P_{ac} = 8 + 0.81 = 8.81\ \mathrm{mW}\;}$$

*[added] Verified: $1.8/1.4142 = 1.2728\ \mathrm{V}$ ✓; $1.2728^2/2 = 0.810\ \mathrm{mW}$ ✓ (with $V$
in volts and $R$ in kΩ the answer comes out in mW directly); $4\times2 = 8\ \mathrm{mW}$ ✓;
$8+0.81 = 8.81\ \mathrm{mW}$ ✓. Note the ratio — **0.81 mW of signal for 8 mW of dc dissipation**, an
efficiency of about 10 %, which is typical of a class-A stage.*

> ⚠ VERIFY **C3.26** ·L3 p25 — the rms line prints as *"rms voltage variation $\;1.8\sqrt{2}\;\; 1.27\ \mathrm{V}$"*: **both the division sign and the equals sign are missing**, so the page reads
> as $1.8\sqrt2$, which is 2.55 V, not the 1.27 V printed beside it. The intended line is
> $1.8/\sqrt2 = 1.27\ \mathrm{V}$, confirmed by the $P_{ac}$ calculation that uses 1.27. The same
> sentence also prints *"Now, **proper** dissipated in RL"* for *power dissipated in $R_L$*.
> Nothing computed changes. See `_verification-log.md`.

---

## 3.27 The ac load line ·L3 p25

[def] **The ac load line is the line along which the Q-point shifts up and down when changes in the
output voltage and current of an amplifier are caused by an ac signal.** ·L3 p25

Three properties, stated in the source: ·L3 p25

1. it is **steeper** than the dc load line;
2. the two lines **intersect at the Q-point** determined by the biasing dc voltages and currents;
3. it takes into account the **ac** load resistance $R_{ac}$, whereas the dc load line considers only
   the **dc** load resistance. *(The footnote records that $R_{ac}$ is written $r_L$ in Art. 59.4 —
   outside this extract.)*

[table] **The two load lines, end for end** ·L3 p25

| | dc load line ($AQB$) | ac load line ($CQD$) |
|---|---|---|
| **cut-off point** (on the $V_{CE}$ axis) | $V_{CE(cut\text{-}off)} = V_{CC}$ | $V_{CE(cut\text{-}off)} = V_{CEQ} + I_{CQ}R_{ac}$ |
| **saturation point** (on the $I_C$ axis) | $I_{C(sat)} = V_{CC}/R_L$ | $I_{C(sat)} = I_{CQ} + V_{CEQ}/R_{ac}$ |
| **slope** | $-1/R_L$ | $-1/R_{ac}$ |

[eq: ac-load-line]

$$\boxed{\;V_{CE(cut\text{-}off)} = V_{CEQ} + I_{CQ}R_{ac}\;}\qquad
\boxed{\;I_{C(sat)} = I_{CQ} + \frac{V_{CEQ}}{R_{ac}}\;}$$

$$\boxed{\;\text{slope of the ac load line} = -\frac{1}{R_{ac}}\;}$$

> ⚠ VERIFY **C3.27** ·L3 p25 — two slips in §58.16(ii). The cut-off point is introduced as
> *"$V_{CE(\mathbf{out}\text{-}off)}$"* for $V_{CE(cut\text{-}off)}$; and the slope is given as
> *"The slope of the ac load line is given by $y = \times\;1/R_{ac}$"*, in which the intended
> statement is $\text{slope} = -1/R_{ac}$ — the same minus-as-$\times$ fault as **C3.4**, plus a
> stray $y$. Nothing computed changes. See `_verification-log.md`.

[fig ·L3 p25] **Fig. 58.24** — the two load lines on one set of axes ($I_C$ vertical, $V_{CE}$
horizontal), no characteristic curves drawn.

- The **dc load line** runs from **$B$** on the $I_C$ axis, marked $\mathbf{V_{CC}/R_L}$, down to
  **$A$** on the $V_{CE}$ axis, marked $\mathbf{V_{CC}}$.
- The **ac load line** is steeper and runs from **$D$** on the $I_C$ axis, marked
  $\mathbf{I_{CQ} + V_{CEQ}/R_{ac}}$ (i.e. **above** $B$), down to **$C$** on the $V_{CE}$ axis,
  marked $\mathbf{V_{CEQ} + I_{CQ}R_{ac}}$ (i.e. **to the left of** $A$).
- **$Q$** is marked at the crossing of the two lines, with **dashed** construction lines back to
  $\mathbf{I_{CQ}}$ on the $I_C$ axis and down to $\mathbf{V_{CEQ}}$ on the $V_{CE}$ axis.

[eq: signal-handling] **Peak-signal handling capacity** ·L3 p25

$$\boxed{\;\text{maximum positive swing} = I_{CQ}R_{ac},\qquad
\text{maximum negative swing} = V_{CEQ}\;}$$

$$\boxed{\;\text{peak-signal handling capacity} = \min\left(I_{CQ}R_{ac},\ V_{CEQ}\right)\;}$$

> [added] **Reading that off the figure.** Moving right from $Q$ you run out of line at $C$, a
> distance $I_{CQ}R_{ac}$; moving left you run out at $V_{CE} = 0$, a distance $V_{CEQ}$. **The
> shorter of the two arms is what clips first**, which is why a Q-point set for maximum undistorted
> swing puts $V_{CEQ} = I_{CQ}R_{ac}$ — the mid-point of the *ac* load line, not the dc one.

### [exercise] Example 58.12 — stated, and only partly solvable from this extract ·L3 p25

*(Applied Electronics, Kerala Univ. 1991)*

**Statement.** Draw the dc and ac load lines for the CE circuit shown in Fig. 58.25(a). **What is the
maximum peak-to-peak signal that can be obtained?**

**What the page gets through before the extract ends** ·L3 p25

$$V_{CE(cut\text{-}off)} = V_{CC} = 20\ \mathrm{V}\qquad\text{(point } A)$$

$$I_{C(sat)} = \frac{V_{CC}}{R_1 + R_E} = \frac{20}{5} = 4\ \mathrm{mA}\qquad\text{(point } B)$$

so **$AQB$ represents the dc load line for the given circuit**. The page then says *"Approximate bias
conditions can be quickly found by assuming that $I_B$ is too small to affect the base bias in
Fig. 58.25 (a)"* — **and the extract ends there.**

> ⚠ ILLEGIBLE ·L3 p25 — **needs a screenshot: Fig. 58.25 and the remainder of Example 58.12**, i.e.
> printed page 2233 of the source textbook. Without the circuit, the Q-point, $R_{ac}$, the ac load
> line and the peak-to-peak answer cannot be obtained.
>
> **[added] What *is* determinable from the two printed lines.**
> - The dc load line runs from $(0,\ 4\ \mathrm{mA})$ to $(20\ \mathrm{V},\ 0)$.
> - Its slope is $-1/(R_{\text{collector}} + R_E) = -1/5\ \mathrm{k\Omega}$, so the **total dc
>   resistance in the collector–emitter path is 5 kΩ**.
> - Once the Q-point is known, the peak-to-peak answer follows from
>   $$V_{pp} = 2\min\left(I_{CQ}R_{ac},\ V_{CEQ}\right)$$
>
> **No Q-point is given here, because none can be recovered from the pages supplied.**

> ⚠ VERIFY **C3.29** ·L3 p25 — the saturation line prints $I_{C(sat)} = V_{CC}/(\mathbf{R_1} + R_E)$.
> Everywhere else in chapter 58 the collector load resistor is $R_L$ (or $R_C$), and $R_1$ is the
> **upper arm of a base potential divider** — a resistor that cannot appear in a collector-saturation
> formula. Fig. 58.25(a) is not in the extract, so it cannot be confirmed whether that figure happens
> to label its collector resistor $R_1$. The same line sets *"$A_{QB}$"* with QB as a subscript; the
> line is **AQB**, through points A, Q and B. Nothing computed changes.
> See `_verification-log.md`.

---

## 3.28 Formula summary — the whole lesson on one page

[table] **Currents and gains**

| Quantity | Formula | Source |
|---|---|---|
| Current law | $I_E = I_B + I_C$ | ·L3 p3 |
| dc alpha | $\alpha = I_C/I_E$ | ·L3 p4 ⚠ V3.1 |
| dc beta | $\beta = I_C/I_B$ | ·L3 p5 |
| ac alpha, ac beta | $\alpha_{ac} = \Delta I_C/\Delta I_E$, $\beta_{ac} = \Delta I_C/\Delta I_B$ | ·L3 p5 ⚠ C3.2 |
| alpha ↔ beta | $\beta = \dfrac{\alpha}{1-\alpha}$, $\alpha = \dfrac{\beta}{1+\beta}$, $1-\alpha = \dfrac{1}{1+\beta}$ | ·L3 p6 |
| CC gain | $I_E/I_B = 1+\beta$ | ·L3 p6 |
| Current ratio | $I_E : I_B : I_C :: 1 : (1-\alpha) : \alpha$ | ·L3 p6 |
| Leakage | $I_{CEO} = (1+\beta)I_{CBO} = \dfrac{I_{CBO}}{1-\alpha}$ | ·L3 p7, p11 |
| With leakage, CB | $I_C = \alpha I_E + I_{CBO}$ | ·L3 p7 |
| With leakage, CE | $I_C = \beta I_B + (1+\beta)I_{CBO}$ | ·L3 p7, p16 |

[table] **DC bias**

| Configuration / circuit | Key formulas | Source |
|---|---|---|
| **CB** | $I_E = \dfrac{V_{EE}-V_{BE}}{R_E}$; $I_C = \alpha I_E$; $V_{CB} = V_{CC}-I_C R_L$ | ·L3 p13 ⚠ V3.11 |
| **CE** | $I_B = \dfrac{V_{BB}-V_{BE}}{R_B}$; $I_C = \beta I_B$; $V_{CE} = V_{CC}-I_C R_L$ | ·L3 p14 |
| **CC (emitter follower)** | $I_E = \dfrac{V_{CC}-V_{BE}}{R_E + R_B/\beta}$; $I_B = \dfrac{V_{CC}-V_{BE}}{R_B + \beta R_E}$; $V_{CC} = V_{CE}+I_E R_E$ | ·L3 p15 ⚠ V3.12 |
| **Base bias** | $S \cong \beta$; $K_\beta = 1$ | ·L3 p17 |
| **+ emitter feedback** | $I_C = \dfrac{V_{CC}-V_{BE}}{R_E + R_B/\beta}$; $K_\beta = \dfrac{1}{1+\beta R_E/R_B}$ | ·L3 p18 |
| **+ collector feedback** | $I_C = \dfrac{V_{CC}-V_{BE}}{R_L + R_B/\beta}$; $K_\beta = \dfrac{1}{1+\beta R_L/R_B}$ | ·L3 p19 ⚠ V3.15, V3.16 |
| **+ both feedbacks** | $I_C = \dfrac{V_{CC}-V_{BE}}{R_E+R_L+R_B/\beta}$; $K_\beta = \dfrac{1}{1+\beta(R_E+R_L)/R_B}$ | ·L3 p20 |
| **Two-supply emitter bias** | $I_E = \dfrac{V_{EE}-V_{BE}}{R_E + R_B/\beta} \cong \dfrac{V_{EE}}{R_E}$; $V_E \cong -V_{BE}$ | ·L3 p21 ⚠ V3.18 |
| **Voltage divider** | $V_2 = V_{CC}\dfrac{R_2}{R_1+R_2}$; $I_E = \dfrac{V_2-V_{BE}}{R_E}$; $K_\beta = \dfrac{1}{1+\beta R_E/(R_1\parallel R_2)}$ | ·L3 p21–p22 |
| **Divider, Thevenin** | $I_B = \dfrac{V_{BB}'-V_{BE}}{R_B'+(1+\beta)R_E}$, $R_B' = R_1\parallel R_2$ | ·L3 p22 |

[table] **Stability and load lines**

| Quantity | Formula | Source |
|---|---|---|
| Stability factor | $S = \dfrac{dI_C}{dI_{CO}} = \dfrac{1+R_B/R_E}{1+(1-\alpha)(R_B/R_E)}$ | ·L3 p16 |
| $S$, CB / CE | $S = 1$ / $S = 1+\beta$ | ·L3 p17 |
| Beta sensitivity | $K_\beta = \dfrac{\beta}{I_C}\dfrac{dI_C}{d\beta}$ | ·L3 p17 ⚠ V3.13 |
| Universal $K_\beta$ pattern | $K_\beta = \dfrac{1}{1+\beta R_{\text{fb}}/R_B} = 1 - \dfrac{I_C}{I_{C(sat)}}$ | ·L3 p19–p20 |
| dc load line | from $(0,\,V_{CC}/R_L)$ to $(V_{CC},\,0)$; slope $-1/R_L$ | ·L3 p24–p25 |
| ac load line | from $(0,\,I_{CQ}+V_{CEQ}/R_{ac})$ to $(V_{CEQ}+I_{CQ}R_{ac},\,0)$; slope $-1/R_{ac}$ | ·L3 p25 |
| Peak-signal capacity | $\min(I_{CQ}R_{ac},\ V_{CEQ})$ | ·L3 p25 |

---

## 3.29 Triage — what to study, in what order

> [added] This section is not in the source. It is a reading order derived from how the extract
> weights its own material.

**The lesson is heavily numerical.** Fifteen worked examples across 25 pages, against roughly six
pages of derivation. Every derivation in it is short (three to five lines) and every one exists to
produce a formula that is then used on numbers. **Work the examples; the theory will come with them.**

**Highest exam value — do these first**

1. **§3.9, the current relations** and **§3.7, $\alpha \leftrightarrow \beta$.** Every later
   calculation runs through them, and they are the cheapest marks in the topic.
2. **§3.16 and §3.25, the CE and voltage-divider bias calculations.** Examples 57.10, 58.5, 58.9,
   58.10 and 58.11 are five variations on one procedure; a CAT can lift any of them verbatim.
3. **§3.26–§3.27, the load lines.** Two end points, one Q-point, one swing — and the figures are
   easy to reproduce under exam conditions.
4. **§3.10, leakage.** Examples 57.4–57.7 all turn on
   $I_C = \beta I_B + (1+\beta)I_{CO}$; **note that Example 57.7's printed answer is wrong (V3.6)**.

**Medium value**

5. **§3.11–§3.13, the static characteristics.** Learn to *describe and sketch* the three CE curves
   and the CB output family, and know what saturation, cut-off and breakdown look like on them.
   Four of this file's flags are figure-labelling errors in exactly these figures (V3.8, V3.9,
   V3.10, V3.19) — check axis units before reading values off any reproduction of them.
6. **§3.19, $S$ and $K_\beta$.** Learn the two definitions, the CB/CE results ($S = 1$ and
   $S = 1+\beta$), and the single $K_\beta = 1/(1+\beta R_{\text{fb}}/R_B)$ pattern rather than four
   separate formulas.

**Lower value, but do not skip entirely**

7. **§3.2–§3.4, biasing and the polarity rule.** Short, and it is the source of most sign errors.
8. **§3.14, drawing conventions.** Half a page of reading that prevents misreading every subsequent
   circuit.

**Present in the notes but never assessed in this extract**

- The historical material in §3.1 (Bell Labs, 1947) and the photographs.
- §3.5's $h$-parameter aliases ($h_{FB}$, $h_{fb}$, $h_{FE}$, $h_{fe}$) — named but never used in any
  calculation here. They matter in the small-signal topic, not this one.

**Two things this extract cannot teach you, because the pages are missing**

- **Examples 57.2 and 57.3** (leakage, printed pp. 2194–2195) — the surviving fragment
  $I_{CEO} = (1+\beta)I_{CO} = 250\ \mathrm{\mu A}$ is all that remains of 57.3.
- **The $\beta$-rule** (Art. 57.24, printed p. 2205+) — cited twice as a shortcut but never stated in
  the extract. §3.25's Method 3 records the one form of it that ·L3 p22 does spell out.

---

## 3.30 Typography — the spelling and notation slips, collected

> ⚠ VERIFY **C3.28** — spelling and word-substitution errors across the extract, gathered in one
> place because none of them changes anything computed. Listed so that a reader meeting them on the
> page knows they are the source's, not a misreading.
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·L3 p2 | "emmitter" | emitter |
> | ·L3 p4 | "adc" (upright) for $\alpha_{dc}$; "tranistor" | $\alpha_{dc}$; transistor |
> | ·L3 p6 | "the **about** 2 equations" | the above 2 equations |
> | ·L3 p8 | "small forward bias **ac-ross** C/B junction" | across |
> | ·L3 p11 | "common **carrier** to both the input (CB) and output (CE) **carriers** circuits"; "practically **idential**" | common to both the input and output circuits; identical |
> | ·L3 p12 | "potential difference … **in** written as $V_{CB}$" | is written as |
> | ·L3 p24 | "**Suposse** an ac input signal voltage" | Suppose |
> | ·L3 p25 | "Now, **proper** dissipated in RL" | power dissipated in $R_L$ |
>
> See `_verification-log.md`.

> ⚠ VERIFY **C3.30** ·L3 p16 — §58.4 introduces the leakage relation with *"The collector current for
> $C_E$ circuit is given by"*, setting **CE** (the configuration) as a subscripted symbol $C_E$,
> which reads as a capacitance. Nothing computed changes.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
