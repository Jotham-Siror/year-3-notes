---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
file_role: verification-log
tiers: "Two sources, logged separately and cross-checked against each other. **Tier 1 (·J)** is the course's own lecture notes, 100 pp., the primary source. **Tier 2 (·L1–·L7)** is the seven lesson handouts, 169 pp., a textbook compilation. Part A logs tier 1, Part B logs tier 2, and a cross-tier section records where one source settles a question the other gets wrong."
source: "Tier 1 — 'Analogue Electronics I Lecture Notes', 100 pp., ·J p2–p100. Tier 2 — seven lesson handouts, L1–L7, 169 pages. Every page of both read as a rendered image."
coverage: "BOTH TIERS COMPLETE — 99 / 99 content pages of the lecture notes and 169 / 169 pages of the lesson handouts. Every worked example in both recomputed."
total_flags: 388
substantive: 158
cosmetic: 230
tags: [verification, errata, corrections, two-tier, cross-tier, unit-prefixes, dropped-exponents, symbol-clashes, figure-labels, redactions]
---

<!-- BEE 3103 Analogue Electronics I knowledge base. Compiled 2026. -->

# Verification log — BEE 3103

Every suspected defect found in the **two written sources of this course**, with what the page
**prints**, what it **should** say, and **why** — stated wherever possible as a check that can be
repeated.

- **Part A — Tier 1: the lecture notes (`·J`).** The course's own 100-page document. **159 flags**:
  62 substantive, 97 cosmetic.
- **Part B — Tier 2: the lesson documents (`·L1`–`·L7`).** Seven handouts, 169 pages, compiled from
  a printed textbook. **229 flags**: 96 substantive, 133 cosmetic.

**Never silently corrected.** The printed version is recorded verbatim so that it can be recognised
when it turns up in a CAT, an exam, or a tutorial worked from the page itself.

**The two tiers overlap on four topics** — diodes, rectifiers, BJTs and FETs — and were verified
independently of each other. Where they disagree, one of them is wrong and the other settles it;
those cases are collected in **Cross-tier resolutions** below and are the most reliable material in
this log.

---

## How to read this log

### Substantive or cosmetic

| Class | Prefix | Meaning |
|---|---|---|
| **Substantive** | `JV{file}.{n}` / `V{lesson}.{n}` | changes an answer, a sign, a unit, or a physical claim — a reader who copies the page gets it wrong |
| **Cosmetic** | `JC{file}.{n}` / `C{lesson}.{n}` | typography, OCR artefact, notation drift, a dangling cross-reference, a missing panel letter — nothing computed changes |

The boundary is drawn at **consequence, not at size**. A single dropped prefix is substantive when
it turns 20 µA into 20 mA and cosmetic when it appears on a caption that nothing depends on. A
missing bracket is substantive when the printed expression evaluates to the wrong number and
cosmetic when the arithmetic printed beside it is nevertheless right.

### The two ID schemes

The leading **J** is the whole distinction: a `J` prefix means the flag was raised against the
**lecture notes**, no `J` means it was raised against a **lesson handout**.

| ID | Reads as |
|---|---|
| `JV3.2` | the **second substantive** flag raised in the **third primary topic file** — `03-capacitors-inductors-and-transformers.md`, covering ·J p24–p32 |
| `JC1.15` | the **fifteenth cosmetic** flag raised in the **first primary topic file** — ·J p2–p9 |
| `V3.2` | the **second substantive** flag raised in **Lesson 3** — the tier-2 handout on the bipolar junction transistor |
| `C7.12` | the **twelfth cosmetic** flag raised in **Lesson 7** |

**`JV3.2` and `V3.2` are different flags in different documents.** Read the J.

IDs are namespaced by file because the topic files were built in parallel. Within each file the
numbering is **contiguous** — no ID has been withdrawn, retired or reused. A few flags appear out of
numeric order *inside* a topic file, because page order and drafting order differ; this log lists
them in numeric order.

Every ID here matches an inline `⚠ VERIFY` flag in the topic file that raised it. Citations use
**·J p35** for page 35 of the lecture notes, and the lesson-and-page form **·L3 p14** for page 14 of
Lesson 3. Both are counted as PDF pages.

### ⚠ REDACTED — a gap, not a defect

The primary PDF carries **opaque blocks over text on eleven pages**: ·J p35, p40, p41, p42, p44,
p53, p55, p58, p87, p88 and p89. Contrast recovery finds **nothing underneath** — the text is
destroyed, not merely hidden.

**These are recorded as gaps, not as defects, and they carry no flag ID.** Nothing was written by
the lecturer that is wrong there; something was written and is now unreadable. They are logged at
the point of use in each topic file, and inventoried in that file's "items needing a clean page"
section, with the block width in pixels and the character count it implies.

- Where the covering block sits over a term the surrounding text defines anyway, the topic file
  states the recovery **and marks it as an inference** — ·J p35's "knee voltage" and ·J p58's
  forward/reverse bias condition are the two clear cases.
- Where it is not recoverable, **nothing is guessed**. ·J p41's two LED material names, ·J p88's and
  ·J p89's whole destroyed bullets, and ·J p53's two opening sentences are left empty and a
  screenshot is requested.

Two neighbouring categories are also marked in the topic files and are likewise **not** defects:
`⚠ ILLEGIBLE`, for a line clipped by the page margin, and plain **content gaps**, where a heading or
a line was lost with the blank space at a page break and was never printed at all.

### The standing rule

**Teach the corrected form; keep the printed form recognisable.**

The corrected expression is what goes into working, into notes, and into an answer script. The
printed form is recorded so that when a tutorial sheet, a CAT or a lecture slide reproduces the
page verbatim, the defect is recognised on sight instead of being copied or, worse, argued with in
an exam hall. Where an examiner is likely to expect the handout's own number rather than the exact
one — `C2.4` and `JV3.5` are the clearest cases — the entry says so explicitly.

---

## Summary and patterns

### Coverage — tier 1, the lecture notes

| File | Title | Pages | Substantive | Cosmetic | Total |
|---|---|---|---|---|---|
| **J1** | Matter, Atomic Structure and Semiconductor Materials | ·J p2–p9 (8) | 7 | 15 | 22 |
| **J2** | Resistors and DC Network Theorems | ·J p10–p23 (14) | 7 | 21 | 28 |
| **J3** | Capacitors, Inductors and Transformers | ·J p24–p32 (9) | 8 | 12 | 20 |
| **J4** | Diodes | ·J p33–p45 (13) | 10 | 13 | 23 |
| **J5** | Rectifiers, Filters and Regulation | ·J p46–p56 (11) | 7 | 11 | 18 |
| **J6** | Bipolar Junction Transistors | ·J p57–p83 (27) | 13 | 16 | 29 |
| **J7** | Field Effect Transistors | ·J p84–p100 (17) | 10 | 9 | 19 |
| **Total** | | **99 / 99** | **62** | **97** | **159** |

### Coverage — tier 2, the lesson documents

| Lesson | Title | Pages | Substantive | Cosmetic | Total |
|---|---|---|---|---|---|
| **L1** | Semiconductor Diodes | 18 | 6 | 11 | 17 |
| **L2** | Rectification and Power Supplies | 26 | 18 | 25 | 43 |
| **L3** | The Bipolar Junction Transistor | 25 | 22 | 30 | 52 |
| **L4** | Field Effect Transistors | 24 | 15 | 21 | 36 |
| **L5** | Fabrication and Integrated Circuits | 23 | 9 | 12 | 21 |
| **L6** | h-Parameters and Small-Signal BJT Amplifiers | 26 | 4 | 8 | 12 |
| **L7** | Multistage Amplifiers, Feedback, Frequency Response | 27 | 22 | 26 | 48 |
| **Total** | | **169 / 169** | **96** | **133** | **229** |

### Both tiers together

**388 flags over 268 pages — one every 0.69 pages.** The two sources are almost equally dirty per
page (1.61 flags per page in the lecture notes, 1.36 in the lesson handouts) but they are dirty in
**different ways**, and that difference is the single most useful thing in this log:

- The **lesson documents** are a *textbook* compilation. Their prose is sound; what fails is the
  **rendering** — lost prefixes, lost exponents, lost Greek letters, dangling article numbers.
- The **lecture notes** are a *compiled* document. Their arithmetic usually lands on the right
  answer; what fails is the **prose and the figures** — a definition attached to the wrong quantity,
  a figure lifted from the previous device, an intermediate line that does not produce the answer
  printed under it.

Density is not evenly spread in either tier. In tier 1, `04-diodes.md` carries **10 substantive
flags in 13 pages** — the worst rate in the course — while `07-field-effect-transistors.md` has the
fewest cosmetic flags of any file because its author was transcribing a clean textbook chapter. In
tier 2, L2, L3 and L7 hold **62 of the 96** substantive flags between them.

### The eleven recurring failure modes

Counting flags is not the useful part. Almost every substantive defect in the 268 pages belongs to
one of **eleven** families, and each family has a check that catches it. Learn the eleven checks and
the log becomes something a reader can reproduce rather than something they have to trust.

**Eight of the families were derived from the lesson documents. All eight survive the primary
notes** — though two of them barely — and the primary notes add **three more** that the lesson
documents show only in isolated cases. The three new families are §9, §10 and §11.

The families **overlap by design** — `V7.14` is both a lost exponent and an answer the page's own
ratio check contradicts, and `JV5.2` belongs to four families at once. A flag appearing more than
once is a flag with more than one independent way of being caught.

**Coverage of the classification.** In tier 1, **61 of the 62** substantive flags fall into at least
one family; the single exception is `JV7.8`, where the notes' arithmetic is internally correct and
the fault is that the question lands the device outside the region its own equation is valid in. In
tier 2, the original eight families account for **68 of the 96**.

---

#### 1 · Unit-prefix and unit-glyph loss

The single most damaging family in the lesson documents, because the arithmetic around it usually
stays correct and only the printed unit is wrong — so nothing looks broken.

Two distinct mechanisms:

- **The µ prefix drops**, leaving mA where µA is meant, or m where µ is meant (or, once, bare
  amperes).
- **The Ω glyph renders as a roman W**, so resistances are printed as though they were powers.

**Tier 1 — substantive:** `JV3.2` **· cosmetic:** `JC2.20`, `JC4.3`, `JC4.5`, `JC5.4`
**Tier 2 — substantive:** `V3.2`, `V3.4`, `V3.8`, `V3.9`, `V4.7`, `V7.7`, `V7.21`, `V7.22`
**· cosmetic:** `C1.5`, `C2.13`, `C2.21`, `C2.25`, `C3.25`, `C5.9`, `C7.2`, `C7.7`

The family is **much thinner in the lecture notes** — one substantive case in 99 pages against eight
in 169 — but the mechanism is identical: `JV3.2` prints an NPO ceramic range as "0.033 mF" for
$0.033\ \mathrm{\mu F}$, a factor of $10^{3}$, and `JC2.20` prints "1 MW" for $1\ \mathrm{M\Omega}$.
The lecture notes add a variant of their own: **the right number under the wrong unit symbol** —
$13.33\ \Omega$ for a voltage (`JC4.5`), $0.46875\ \mathrm{A}$ for a power (`JC5.4`).

> **Check you can repeat:** in any small-signal BJT or FET problem, form $\beta = I_C/I_B$ from the
> printed numbers. It must land somewhere between about 20 and 300. A base current printed in
> **milliamps beside a collector current in milliamps** fails that test instantly. Separately, read
> every stray roman **W** that follows a resistance value as **Ω**, and check that the unit on every
> boxed answer is the unit its own formula produces.

#### 2 · Dropped or misplaced exponents, and lost $\sqrt2$ and $\pi$ factors

Both sources lose multiplicative constants in typesetting far more often than they get the physics
wrong. In almost every case **the final answer printed on the page is correct** and only the
intermediate expression is defective — which is exactly what makes this family dangerous, because
the visible answer certifies the invisible error. (That mechanism is now a family in its own
right — see §10.)

**Tier 1 — substantive:** `JV1.4`, `JV3.6`, `JV3.7`, `JV4.2`, `JV5.1`, `JV5.2`, `JV5.3`, `JV5.4`,
`JV7.5` **· cosmetic:** `JC2.10`, `JC4.7`, `JC6.15`
**Tier 2 — substantive:** `V1.5`, `V2.2`, `V2.3`, `V2.4`, `V2.7`, `V2.11`, `V2.14`, `V6.4`,
`V7.13`, `V7.14` **· cosmetic:** `C2.7`, `C2.8`, `C3.17`, `C4.8`, `C4.15`, `C7.19`

The primary notes contribute two mechanisms the lesson documents do not: **a single digit added to
or dropped from a denominator** (`JV3.6` prints 200 for 2000, `JV3.7` prints 40 for 4, `JV5.4`
prints 400 for 40 — three tenfold errors, all in intermediate lines whose answers are right), and
**an exponent placed on the wrong bracket** (`JV5.1`, `JV5.3`, where the square migrates from
$I_{rms}$ to $(R_L+r_f)$).

> **Check you can repeat:** evaluate the printed expression *exactly as written* and compare it with
> the answer printed beside it. When the two differ by $\pi$, $\sqrt2$, $2$ or a power of ten, the
> factor was lost by the typesetter — recover it from the answer, and write the corrected
> expression, never the printed one. Where an exponent is in doubt, check dimensions: `JV5.1`'s
> printed denominator is $\mathrm{A}\cdot\Omega^{2}$ against a numerator of $\mathrm{A}^{2}\Omega$,
> so the ratio is not dimensionless and cannot be an efficiency.

#### 3 · Self-referential equations

The symbol on the left of the equals sign reappears on the right, or the same symbol appears above
and below a fraction bar. Such an expression is either trivially equal to 1 or silently mislabelled;
it is never what was meant.

**Tier 1 — substantive:** `JV6.5` **· cosmetic:** `JC4.11`
**Tier 2 — substantive:** `V2.5`, `V3.5`, `V3.7`, `V3.20`, `V6.2`, `V7.3`, `V7.6`, `V7.11`, `V7.19`

**This is the one family that nearly disappears in the primary notes** — nine tier-2 substantive
flags against one. The single case is instructive: `JV6.5` prints
$\theta = I_E/I_C = (I_E/I_C)(I_C/I_B) = \ldots = 1+\beta$, where the product on the right cancels
to $I_E/I_B$, not to the $I_E/I_C$ on the left. The cosmetic case is a list headed *"Factors
affecting light intensity"* whose first item is *"Light intensity"* (`JC4.11`) — the same fault in
prose.

> **Check you can repeat:** read the equals sign as a *test*, not as an instruction. If the
> left-hand symbol occurs on the right, either the label is wrong or one of the two occurrences is
> a different quantity that has lost its subscript. Apply it to headings and lists too.

#### 4 · Mislabelled figure axes and swapped or substituted figure panels

The figures in this course are less reliable than the text beside them, in **both** sources. Axes
carry the wrong quantity or the wrong unit; two terminals share one label; a panel shows a different
circuit from the one the caption announces; two photographs exchange captions.

**Tier 1 — substantive:** `JV1.3`, `JV1.6`, `JV4.7`, `JV4.8`, `JV5.6`, `JV5.7`, `JV7.2`
**· cosmetic:** `JC1.11`, `JC1.12`, `JC3.3`, `JC3.10`, `JC4.4`, `JC4.6`, `JC5.9`, `JC6.3`, `JC6.7`,
`JC6.8`, `JC6.9`, `JC6.10`, `JC7.1`, `JC7.4`
**Tier 2 — substantive:** `V2.9`, `V2.15`, `V3.8`, `V3.10`, `V3.19`, `V4.1`, `V5.5`, `V5.8`, `V7.10`
**· cosmetic:** `C1.5`, `C1.10`, `C2.11`, `C2.20`, `C2.22`, `C2.24`, `C3.1`, `C3.3`, `C3.14`,
`C4.2`, `C4.3`, `C4.7`, `C4.12`, `C4.14`, `C4.21`, `C5.6`, `C7.12`, `C7.13`, `C7.15`

**This is the largest family in the primary notes.** Seven substantive and fourteen cosmetic — about
one tier-1 flag in eight. Three of the seven are not mislabels at all but **drawings of the
wrong circuit**: `JV5.6` draws two zeners series-aiding where the symmetric clipper needs them
anode-to-anode, and `JV5.7` substitutes a battery for the zener it names.

> **Check you can repeat:** read every axis label and every in-figure symbol *against the worked
> numbers on the same page*. Where the drawing and the arithmetic disagree, the arithmetic is
> almost always the reliable one — `V3.10` was settled precisely that way, and so was `JV4.7`, where
> the figure labels both silicon forward resistances $20\ \Omega$ and the arithmetic three lines
> below computes $52\times2/(52+2)$, which is only available with $2\ \Omega$.

#### 5 · Symbol collisions inside one derivation

Two different quantities wearing the same symbol, or a symbol appearing exactly once in the whole
chapter because it was invented by a typesetting slip ($R_\beta$, $V_{DSS}$, $f_0$).

**Tier 1 — substantive:** `JV4.4`, `JV6.2`, `JV7.1`, `JV7.9`, `JV7.10`
**· cosmetic:** `JC1.4`, `JC2.5`, `JC4.1`, `JC5.7`, `JC5.11`, `JC7.3`, `JC7.5`, `JC7.9`
**Tier 2 — substantive:** `V2.6`, `V2.13`, `V3.18`, `V3.19`, `V3.21`, `V3.22`, `V4.6`, `V6.1`,
`V6.3`, `V7.9`, `V7.11`, `V7.18`, `V7.19`, `V7.20`
**· cosmetic:** `C3.10`, `C3.11`, `C3.22`, `C3.29`, `C3.30`, `C4.3`, `C4.12`, `C6.3`, `C6.4`,
`C7.10`, `C7.17`, `C7.23`, `C7.24`

The primary notes' worst instance is `JC7.9`: **$V_{SS}$ carries three meanings inside seventeen
pages** — the negative source-bias rail on ·J p94, the substrate terminal on ·J p88 and p90, and the
common-drain supply on ·J p99, where it should be $V_{DD}$. `JV7.1` and `JV7.10` are the two that
cost marks: $V_P$ used with both signs, and $V_{GS(\text{off})}$ printed where
$V_{GS(\text{th})}$ belongs. `JV6.2` is the dimensional variant of the same fault — an
**admittance** in siemens set equal to a **resistance** in ohms, on two pages.

> **Check you can repeat:** three tests, all fast. (i) **Every parameter in one configuration's
> formula must carry the same second subscript** — an $h_{ie}$ inside an otherwise common-collector
> expression is a slip (`V6.3`). (ii) **A symbol that appears once and nowhere else does not exist**
> — search the chapter for a second occurrence before using it. (iii) **A symbol used with two
> signs is being used for two quantities** — `JV7.1` is exactly that, and the tell is that
> substituting one for the other gives $I_D > I_{DSS}$, which is impossible.

#### 6 · Arithmetic that contradicts the page's own next line

The most frequent substantive fault in **both** sources, and the most easily caught: a printed
answer or step that the same solution then fails to use, or that a later part of the same question
contradicts.

**Tier 1 — substantive:** `JV1.4`, `JV1.5`, `JV1.7`, `JV2.1`, `JV2.3`, `JV2.4`, `JV2.6`, `JV3.6`,
`JV3.7`, `JV3.8`, `JV4.5`, `JV4.6`, `JV4.7`, `JV5.2`, `JV5.4`, `JV5.5`, `JV6.3`, `JV6.4`, `JV6.5`,
`JV6.6`, `JV6.7`, `JV6.8`, `JV6.9`, `JV6.10`, `JV6.11`, `JV7.4`, `JV7.5`, `JV7.6`, `JV7.7`
**· cosmetic:** `JC2.19`, `JC4.6`, `JC6.2`, `JC6.16`
**Tier 2 — substantive:** `V1.4`, `V2.12`, `V3.3`, `V3.6`, `V3.14`, `V3.17`, `V4.9`, `V4.12`,
`V4.13`, `V4.14`, `V4.15`, `V6.4`, `V7.1`, `V7.5`, `V7.8`, `V7.14`, `V7.15`, `V7.16`, `V7.17`
**· cosmetic:** `C2.12`, `C2.17`, `C3.18`, `C3.19`, `C7.3`, `C7.11`, `C7.18`

**Twenty-nine of the 62 tier-1 substantive flags are in this family** — nearly half. The lecture
notes contradict themselves constantly and almost always in the reader's favour: the correction is
on the same page. `JV6.8` prints the silicon and germanium leakage-doubling temperatures **both ways
round on one page**; `JV1.7` defines charge as a current five pages after defining it correctly.

> **Check you can repeat:** recompute every printed intermediate and ask **which number the next
> line actually carries forward**. `V4.9` prints $V_D = 1.54$ V and then uses 10.54 V two lines
> later; `V6.4` prints $Y_o = 194\times10^{-5}$ S and then quotes an $R_o$ that only follows from
> $1.944\times10^{-5}$ S; `JV6.6` drops an $\alpha$ that the very next line restores. The page
> usually contains its own correction.

#### 7 · Glyphs, and whole sub-expressions, that did not survive the page

Greek letters and operators that the source's rendering drops or substitutes: $\Delta$ vanishes,
$\beta$ becomes nothing at all in figure annotations, $\eta$ becomes a roman h, $\omega$ becomes a
roman w, $\pi$ becomes capital $\Pi$, a minus sign becomes a multiplication sign, and the digit 1
becomes I or l.

**Tier 1 — substantive:** `JV2.5`, `JV4.3`, `JV5.1`, `JV5.3`
**· cosmetic:** `JC1.15`, `JC2.5`, `JC2.10`, `JC2.14`, `JC2.20`, `JC3.2`, `JC3.6`, `JC3.8`,
`JC3.11`, `JC4.12`
**Tier 2 — substantive:** `V2.1`, `V4.3`, `V4.4`, `V4.5`
**· cosmetic:** `C1.6`, `C2.3`, `C2.5`, `C3.2`, `C3.3`, `C3.4`, `C3.13`, `C3.24`, `C3.26`, `C3.27`,
`C4.5`, `C4.6`, `C4.9`, `C7.4`, `C7.22`, `C7.26`

**In the primary notes the same mechanism operates one level up, on whole sub-expressions.** The
document was typed in an equation editor and the editor loses structure, not just characters:
`JV2.5` stacks the two halves of $Z = R+jX = \sqrt{R^2+X^2}\,\angle\tan^{-1}(X/R)$ into a fraction,
producing a unit phasor; `JV4.3` moves $V_D$ from the exponent into a numerator over
$e^{\eta V_T}$; `JC4.7` splits a denominator, leaving $19/32$ under the bar and $.926$ stranded
beside it; `JC2.10` does the same to five decimal points across four pages.

**L6 contributes nothing to this family**, and the reason is instructive: it is the one handwritten
source in the course, so it has manuscript corrections (`C6.1`, `C6.6`) instead of rendering
artefacts.

> **Check you can repeat:** when an equation looks **dimensionally impossible or trivially true**,
> suspect a missing glyph or a collapsed layout before suspecting the physics. $V_{CC}\times I_CR_L$
> giving volts (`C3.4`), $r_d = V_{DS}/I_D$ presented as a small-signal slope (`V4.3`) and an
> impedance of modulus exactly 1 (`JV2.5`) are all single lost characters or brackets, not
> misunderstandings.

#### 8 · Cross-references that lead nowhere, and material that is simply absent

In the lesson documents, article and figure numbers lose their leading digit — "Art. 1.40" for
Art. 51.40, "Fig. 3.5" for Fig. 53.5, "Fig. 13.37" for Fig. 63.37 — and in several places the target
does not exist at all because the compilation dropped it.

**Tier 1 — substantive:** `JV2.2`
**· cosmetic:** `JC1.9`, `JC1.11`, `JC2.8`, `JC2.9`, `JC2.11`, `JC2.16`, `JC3.4`, `JC3.7`, `JC5.6`,
`JC5.8`, `JC6.1`, `JC6.4`, `JC6.15`, `JC7.6`
**Tier 2 — substantive:** `V4.10`, `V4.14`
**· cosmetic:** `C1.2`, `C1.7`, `C1.11`, `C2.1`, `C2.9`, `C2.14`, `C3.5`, `C3.6`, `C3.14`, `C3.15`,
`C3.23`, `C4.19`, `C5.6`

**The primary notes have no dangling cross-references at all** — they contain almost no numbered
references to number wrongly. What they have instead is the **absence half** of the family, and they
have far more of it: **five missing section headings** (`JC3.4`, `JC3.7`, `JC5.6`, `JC5.8`, and the
absent power-supply heading at ·J p46), a table with **no column headings** (`JC6.4`), four lines
clipped away by page margins (`JC2.11`, `JC2.16`, `JC6.15`, `JC7.6`), and one exercise stem
truncated so badly that both its solutions read the answer backwards (`JV2.2`, `JC2.8`).

> **Check you can repeat:** a reference whose leading digit looks too small is almost always missing
> a 5 or a 6 — restore it and check the target exists before trusting it. Where a worked solution
> uses a value that appears nowhere in its own question (`V4.10`, `C2.14`, `JV2.2`), the question,
> not the solution, is what went missing.

---

### The three families the primary notes add

#### 9 · [new] A block copied from the neighbouring case and never adapted

**The primary notes' most characteristic figure fault.** A figure, a bullet list, a table row or a
substituted value is carried over from the page before and applied to a device or a circuit it does
not describe. The give-away is that the copied material is **internally consistent and correct** —
it is simply about something else.

**Tier 1 — substantive:** `JV2.3`, `JV5.2`, `JV6.3`, `JV7.2`, `JV7.3`
**· cosmetic:** `JC6.3`, `JC6.7`, `JC6.8`, `JC6.9`
**Tier 2 — substantive:** `V4.14` **· cosmetic:** `C7.13`

The two clearest cases sit on one page. **·J p91 illustrates the enhancement-only MOSFET with the
depletion-enhancement MOSFET figure of ·J p89, reproduced unchanged** (`JV7.2`) — complete with
$I_{DSS}$, a $V_{GS} = 0$ curve carrying current and a $V_{GS} = -2\ \mathrm{V}$ curve, none of
which an enhancement-only device has — **and prints under it the six-bullet JFET operating narrative
of ·J p85, verbatim** (`JV7.3`), depletion regions and all. The others follow the same mechanism in
text: `JV2.3` opens the parallel-resistor derivation with the series rule
$I = I_{R1} = I_{R2} = I_{R3}$; `JV5.2` substitutes the half-wave $I_{rms} = I_m/2$ into the
full-wave efficiency two lines
after deriving $I_m/\sqrt2$ for that circuit; `JV6.3` gives the common-emitter input power as
$I_EV_{BE}$, which is the common-base entry from the previous page; `JC6.8` labels **all five**
common-emitter output curves $I_B = 40\ \mathrm{\mu A}$.

**Why this is a family and not nine coincidences:** in every case the copied block is a *neighbour* —
the previous page, the previous row of the same table, the previous configuration — and in every
case the page's own equation on the same page contradicts it.

The lesson documents show the mechanism only twice, `V4.14` (a $K$ evaluated from the previous
example's data) and `C7.13` (two photographs with exchanged captions), which is why it was not
raised as a family in Part B.

> **Check you can repeat:** for every figure, ask **what would be different if this were the
> previous device**. If the answer is "nothing", the figure has been copied. Then check the labels
> that *must* differ: an enhancement-only MOSFET cannot carry an $I_{DSS}$, a PNP block diagram
> cannot read N-P-N, a common-emitter test circuit cannot measure $V_{CB}$.

#### 10 · [new] The right answer printed beside the wrong middle line

**The primary notes' signature fault.** The final number is correct; the line that is supposed to
produce it is not. Because the answer is right, nothing downstream breaks and no reader checking
answers ever notices — but a reader **following the working** arrives somewhere else.

**Tier 1 — substantive:** `JV1.4`, `JV1.5`, `JV2.1`, `JV2.4`, `JV2.6`, `JV3.6`, `JV3.7`, `JV4.5`,
`JV4.7`, `JV5.1`, `JV5.2`, `JV5.3`, `JV5.4`, `JV6.5`, `JV6.6`, `JV6.7`, `JV7.5`, `JV7.6`
**· cosmetic:** `JC2.10`, `JC4.6`, `JC4.7`, `JC6.15`, `JC6.16`
**Tier 2 — substantive:** `V1.5`, `V2.3`, `V2.7`

**Eighteen of the 62 tier-1 substantive flags — more than one in four.** The mechanism is always the
same and the sizes are startling: `JV3.6` prints $\frac{400\times20}{200} = 4$ V, where the printed
fraction evaluates to 40; `JV3.7`, four lines later, prints a denominator of 40 where 4 belongs and
gets 0.09 A from an expression that yields 0.9; `JV5.4` prints $\frac{400}{1300} = 0.031$ A, where
the fraction is $\frac{40}{1300}$; `JV7.5` prints $1.5\times10^{-3}$ for a $1.5\ \mathrm{k\Omega}$
resistor and still lands on 6 V.

**This family is why the log exists.** Every other family announces itself — a wrong answer, a
broken dimension, a symbol that cannot be right. This one is invisible unless the working is
re-done, and it is precisely the material a CAT lifts verbatim.

It overlaps §2 and §6 heavily and deliberately: §2 names the *mechanism* (a lost factor), §6 names
the *detection route* (the next line disagrees), and §10 names the *consequence* — that the printed
answer certifies a defective derivation. `V2.7` is the purest tier-2 example: the half-wave TUF
derivation loses a factor $\pi$ **twice**, and the two slips cancel exactly in the final 0.287.

> **Check you can repeat:** never accept an answer because it matches the book. **Evaluate every
> printed intermediate on a calculator and check it gives the number printed under it.** One line,
> one keystroke sequence, and it catches eighteen of the sixty-two.

#### 11 · [new] A definition that describes a different quantity

The lesson documents are a textbook compilation, so their prose is largely sound and their defects
are typographic. **The lecture notes are the opposite: their arithmetic mostly lands, and it is the
sentences that fail.** A definition is attached to the wrong quantity, or states a mechanism that
runs the other way, or describes an effect instead of the thing.

**Tier 1 — substantive:** `JV1.1`, `JV1.2`, `JV1.3`, `JV1.7`, `JV2.7`, `JV3.1`, `JV3.3`, `JV3.4`,
`JV3.5`, `JV4.1`, `JV4.4`, `JV4.9`, `JV4.10`, `JV6.1`, `JV6.12`, `JV6.13`
**· cosmetic:** `JC1.10`, `JC1.13`, `JC2.1`, `JC2.2`, `JC2.3`, `JC2.12`, `JC2.17`, `JC2.18`,
`JC3.1`, `JC3.9`, `JC3.12`, `JC5.11`, `JC7.7`
**Tier 2 — substantive:** `V1.1`, `V1.6`

**Sixteen of the 62 tier-1 substantive flags**, and the family is heaviest exactly where the notes
are most definitional — `03-capacitors-inductors-and-transformers.md` puts **four of its eight**
substantive flags here. The clearest pair is on ·J p24 and ·J p29: **permittivity is defined as "the
extent to which a material affects magnetic field"** (`JV3.1`), which is permeability, and five
pages later permeability is defined correctly in almost the same words. **Self-inductance is defined
as inducing emf "at the surroundings"** (`JV3.3`), which is mutual inductance, defined identically
three lines below. The reader is left with two names for one idea and no name for the other.

Others reverse a physical mechanism outright: `JV4.9` says a photodiode is **heavily** doped to
raise reverse current (it is lightly doped, to widen the depletion region); `JV4.10` makes the
**applied voltage**, not the light, generate the carriers in a photodiode; `JV6.13` says an open
$R_{B2}$ turns the transistor **off** when it drives it into saturation; `JV6.1` credits moderate
collector doping with reducing dissipation when lighter doping raises $\rho$ and therefore raises
$I_C^2R$.

> **Check you can repeat:** for every definition, ask **which other quantity in the course this
> sentence is the definition of**. If it is the definition of something else, one of the two is
> mislabelled — and the notes almost always define the other one correctly somewhere nearby, so the
> pair can be settled from the document itself. Then ask **which way the mechanism runs**: raise the
> doping, does the depletion layer widen or narrow? Open the lower divider resistor, does the base
> current rise or fall?

---

## Cross-tier resolutions — where one source settles the other

This is the most valuable section in the log.

The two tiers cover **four topics twice** — diodes, rectifiers, BJTs and FETs — and were verified
independently, page against page. Where both print the same thing, confidence is high. Where they
**differ**, one of them is wrong and the other one settles it, and a question that would otherwise
stay open is closed. Where they carry the **same** defect, a second source is *not* confirmation and
the entry says so.

Every case below is taken from a topic file's own cross-check section: `04-diodes.md` §4.18,
`05-rectifiers-filters-and-regulation.md` §5.26, `06-bipolar-junction-transistors.md` §6.35, and
`07-field-effect-transistors.md` §7.23.

### Where the primary notes are right and the lesson documents are wrong

| Point | ·J prints | ·L prints | Resolution |
|---|---|---|---|
| **The defining current ratio of the transistor** | $\alpha = I_C/I_E$, **correctly, twice** — ·J p60 and ·J p63 | $\alpha = I_E/I_C$, inverted — ·L3 p4, flagged **V3.1** | **·J.** $\alpha$ is quoted on the same tier-2 page as ranging 0.95–0.999, which $I_E/I_C \approx 1.01$–$1.05$ cannot be. Everything downstream — $\beta$, $I_C$, $I_{CEO}$ — inverts with it |
| **Placement of the $-1$ in the diode equation** | **outside** the bracket, $I_o\!\left(e^{V_D/\eta V_T}-1\right)$ — ·J p35 | **inside the exponent** in all four highlighted forms and again in a worked example — ·L1 p7–p8, flagged **V1.3** | **·J.** At $V = 0$ the tier-2 form gives $I = I_0e^{-1} = 0.368\,I_0$ — an unbiased diode passing a third of its saturation current |
| **DC power in a rectifier** | $P_{dc} = I_{dc}^{2}R_L$ — ·J p47 and ·J p49 | $P_{dc} = I_{dc}^{2}(R_0+R_L)$ on the full-wave page — ·L2 p8, flagged **V2.10** | **·J.** The dc power *delivered to the load* cannot include the source resistance; ·L2's own half-wave page (p4) prints it correctly |
| **Half-wave rectifier efficiency** | **40.5 %** — ·J p47 | **40.6 %**, and once **409.6 %** — ·L2 p4, flagged **V2.2** and **C2.4** | **·J.** $4/\pi^{2} = 40.53\,\%$, so ·J's rounding is the accurate one and ·L2's parent textbook rounds the wrong way |
| **Full-wave rectifier efficiency** | **81.1 %** — ·J p49 | **81.2 %** — ·L2 p9 | **·J.** $8/\pi^{2} = 81.06\,\%$ |
| **The ideality factor in the master equation** | $\eta$ present, with $\eta = 1$ for Ge and $\eta = 2$ for Si — ·J p35 | $\eta$ **dropped** from the highlighted master equation — ·L1 p6, flagged **V1.2** | **·J's equation is the better-formed one.** The two agree exactly on the values; only the tier-2 box omits the factor it then uses three lines later |
| **The $I_{CEO}$ derivation** | derived on the page, $I_{CEO} = (1+\beta)I_{CBO} = I_{CBO}/(1-\alpha)$ — ·J p64 | result quoted; the pages carrying the derivation are **missing from the extract**, so `13-…` supplies it as `[added]` | **·J is the primary source for the derivation.** Not a defect in ·L3 — a gap, now closed |
| **Exact vs approximate emitter-feedback bias** | $I_B = \dfrac{V_{CC}-V_{BE}}{R_B+(1+\beta)R_E}$, the **exact** form — ·J p71 | $I_C \cong \dfrac{V_{CC}-V_{BE}}{R_E+R_B/\beta}$, the approximation | **·J's is exact**; the two agree to within $1/\beta$ |

> **One caveat on the two efficiencies.** *More accurate* is not the same as *what the examiner
> expects.* `C2.4` records that the tier-2 handout's 40.6 % and 81.2 % are inherited from its parent
> textbook and are what a CAT lifted from that page will mark as correct. **Quote the handout's
> figure when the question is plainly lifted from it; quote $4/\pi^{2} = 40.5\,\%$ and
> $8/\pi^{2} = 81.1\,\%$ when the question asks for the constant.** ·J's rounding is the correct
> one either way.

### Where the lesson documents are right and the primary notes are wrong

| Point | ·J prints | ·L prints | Resolution |
|---|---|---|---|
| **Boltzmann's constant** | $k = 1.38\times10^{-28}\ \mathrm{J/K}$ — ·J p35, flagged **JV4.2** | $k = 1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$, and evaluates $V_T$ from it — ·L1 p3 | **·L1.** ·J is wrong by a factor of $10^{5}$: the printed constant gives $V_T = 2.6\times10^{-7}\ \mathrm{V}$, a quarter of a microvolt |
| **The exponent of the diode equation** | $V_D$ typeset as a **numerator over** $e^{\eta V_T}$ — ·J p35, flagged **JV4.3** | correct exponential form; its own defect is the $-1$, not the exponent | **·L1's exponent with ·J's $-1$ is the correct equation.** Neither source prints it whole |
| **A number for $V_T$** | never evaluated anywhere in ·J | 26 mV at 300 K, 25 mV at 293 K — ·L1 p3, p7 | **·L1** — the only source that puts a number to it |
| **Enhancement-only MOSFET static characteristics** | the **DE MOSFET figure reproduced unchanged**, with $I_{DSS}$ and a depletion mode — ·J p91, flagged **JV7.2** and **JV7.3** | Fig. 63.30: positive-$V_{GS}$ curves only, no $I_{DSS}$, no depletion mode — ·L4 p20 | **·L4's figure, without qualification.** ·J p91's figure and its six bullets both describe a different device |
| **Drain-feedback bias sign** | $V_{GS} = -V_{DS}$ — ·J p96, flagged **JV7.4** | $V_{GS} = V_{DS}$, with the reason stated — ·L4 p20 | **·L4.** The negative form cuts the N-channel enhancement MOSFET off, so the circuit could not work; ·J's own next line prints $V_D = V_{DS}$ |
| **E-MOSFET drain-loop equation** | $V_{DS} = V_{DD} - I_SR_S$, in an example where $R_S = 0$ — ·J p97, flagged **JV7.6** | $V_{DS} = V_{DD} - I_DR_L$ — ·L4 p20 | **·L4.** Same worked example in both; ·J's is a transcription slip on the resistor symbol |
| **The 5 V in the E-MOSFET exercise** | called $V_{GS(\text{off})}$ — ·J p97, flagged **JV7.10** | called $V_{GS(\text{th})}$ — ·L4 p21 | **·L4.** Same problem, same 1.44 mA answer, correct label. ·J's label sends the reader to Shockley's equation, for which no $I_{DSS}$ is given |
| **Data-sheet symbols for $K$** | $K = I_D/(V_{GS}-V_{GS(\text{th})})^2$, with $I_D$ and $V_{GS}$ each doing double duty — ·J p97, flagged **JV7.9** | $K = I_{D(\mathrm{ON})}/(V_{GS}-V_{GS(\text{th})})^2$ — ·L4 p19 | **·L4's labels.** The formula is the same; ·L4 distinguishes the data-sheet ON point from the circuit's operating point and ·J does not |
| **Common-source phase inversion** | $A_v = V_{DS}/V_{GS}$, unsigned — ·J p99 | $A_v = -g_m(r_d\parallel R_L)$, inversion stated and drawn — ·L4 p12 | **·L4.** The inversion is real and examinable; ·J gives ratios of terminal quantities that cannot produce a number at all |
| **Common-drain subscript order** | $V_{DG}$, $V_{DS}$ — ·J p99, flagged **JC7.5** | $V_o/V_i$ with an explicit a.c. equivalent — ·L4 p13–p14 | **·L4.** ·J's ratio is numerically right and its subscript order is not — cosmetic, but it breaks the $V_{XY} = V_X - V_Y$ convention used everywhere else in ·J |

### Where both sources carry the same defect — and a second source is not confirmation

Three cases. **In each, finding the error twice is finding one error twice**, because the two
documents share an ancestor. Treat them as unconfirmed, not as doubly confirmed.

| Defect | In ·J | In ·L | Why it is not independent |
|---|---|---|---|
| **The $V_P$ sign collision in Shockley's equation** | ·J p85–p86 define $V_P$ on the **$V_{DS}$ axis** (positive); ·J p87 then prints the equation over $V_P$ **and** over $V_{GS(\text{off})}$, asserting they are equal — flagged **JV7.1** | ·L4 p4–p8 and p15 carry the identical contradiction — flagged **V4.2** | **The same double-form equation, printed the same way on one page in both.** ·L4's exposure is worse: it puts *numbers* to a negative $V_P$ in three worked examples, where ·J never puts a number to $V_P$ at all. **Correct form:** the denominator is the cut-off voltage, $I_D = I_{DSS}\left(1-V_{GS}/V_{GS(\text{off})}\right)^{2}$, with $\lvert V_P\rvert = \lvert V_{GS(\text{off})}\rvert$ and $V_{GS(\text{off})} = -\lvert V_P\rvert$ for N-channel. Substituting a positive $V_P$ for a negative $V_{GS}$ gives $I_D > I_{DSS}$, which is impossible |
| **LED light output claimed proportional to forward current** | the luminosity characteristic **drawn as an exact straight line through the origin** — ·J p42, flagged **JV4.8** | the text claims light output is *"directly proportional"* to $I_F$ — ·L1 p14, flagged **V1.6** | **The same claim in two forms.** But here the tier-2 document **contradicts itself in the reader's favour**: the figure ·L1 p14 points at plots the real, saturating curve — ≈1.8 mW at 50 mA, ≈2.8 mW at 100 mA, ≈3.4 mW at 150 mA. Doubling the current raises output by 1.6, not 2. **Take ·L1's figure; reject both texts and ·J's straight line.** Output rises monotonically but **sub-linearly**, saturating at high current |
| **The conductor band diagram drawn with a visible forbidden band** | ·J p7 draws a clear gap while its own text states $E_g = 0$ eV — flagged **JV1.6** | the identical figure in reference deck **·RD2 p2** (tier 3, mapped not verified), likewise with $E_g = 0$ eV beneath it | **Inherited from a common ancestor**, so RD2 is not a second opinion. Redraw the conductor with **no** forbidden band — the three band diagrams differ *only* in the width of the middle strip, so a conductor drawn with a gap is indistinguishable from a narrow-gap semiconductor |

### Which agreements actually count as confirmation

Agreement between the two tiers is strong evidence **only where the two derivations are
independent**, and they are not always.

- **Rectifiers — genuinely independent, and they agree on everything.** The two sources derive the
  half-wave and full-wave average, rms, efficiency and ripple factor by different routes (·J
  integrates; ·L2 also reaches the ripple factors from the form factor and from the harmonic sum),
  and **all eight constants agree**. Where the printed roundings differ, ·J is the more accurate.
  This is the strongest mutual confirmation in the knowledge base.
- **BJTs — independent, and no disagreement on the physics was found anywhere.** Every difference
  between ·J p57–p83 and ·L3 is one of completeness, of exact-versus-approximate form, or a printing
  defect in one that the other gets right.
- **FETs — *not* independent.** ·J p95's worked example **is** the textbook's Example 63.2; ·J
  p96–p97's is Example 63.10; ·J p97's exercise is Example 63.11 — same circuits, same numbers, same
  answers. The lecture notes are a compilation from that chapter. So agreement between ·J and ·L4 on
  FET material is **weak** evidence, and the shared $V_P$ defect above is exactly what that predicts.
  The compensation is that where the two differ on a number, ·L4 usually shows what ·J was
  transcribing — which is how `JV7.5`, `JV7.6` and `JV7.10` were confirmed.

### Where there is no second source at all

Four bodies of material in this course exist in **one** tier only, so nothing here can be
cross-checked and every flag against them stands alone.

| Material | Only source | Note |
|---|---|---|
| **DC network theorems and passive components** — resistivity, colour code, series/parallel, Thevenin, Norton, mesh analysis, source models, capacitors, inductors, transformers | **·J p10–p32** | The seven lesson documents contain **no treatment of any of it**. They *use* Thevenin (·L3 p22) and Norton (·L6 p12) without stating either theorem. This is 23 of the 99 pages and 15 substantive flags with no second opinion |
| **Smoothing filters** — capacitor, choke-input and Π filters, with waveforms and charge/discharge equations | **·J p50–p53** | `12-rectifiers.md` §2.12 is headed *"[added] Smoothing — supplied here, NOT in the handout"*: ·L2 promises smoothing on its first page and never delivers it |
| **Peak inverse voltage per topology** — $V_{sm}$ half-wave, $2V_{sm}$ centre-tap, $V_{sm}$ bridge | **·L2** | ·J mentions PIV once (·J p46) only as a diode *rating*, and never computes it. Without it, ·J p50 gives no reason to prefer the bridge over the centre-tap circuit |
| **FET small-signal parameters and gain** — $r_d$, $g_m$, $\mu$, $g_{mo}$, $A_v = -g_m(r_d\parallel R_L)$, the FET load line, the Miller input capacitance | **·L4** | ·J names "forward trans-conductance" once, in a list of purchase parameters, and never defines or uses it. **Nothing in ·J lets a gain be computed as a number** |
| **Zener regulator design** — $R$ from $I_{z\max}$, the $I_{z\min}$/$I_{z\max}$ band, dynamic impedance, four worked regulator examples | **·L1** | ·J p53–p55 gives the zener as a stabiliser block and the off-state/on-state method, but no design procedure |

---

# Part A — Tier 1: the lecture notes (`·J`)

**The course's own document, 100 pages, ·J p2–p100.** Seven topic files, 62 substantive flags and 97
cosmetic. Citations are of the form **·J p35** — page 35, counted as PDF pages.

**What this source is like.** It is a compiled document, not a scan: the text was typed and the
equations set in an equation editor. That shapes its defects. The arithmetic usually reaches the
right answer; what fails is the **prose** (§11 of the pattern list), the **figures** (§4 and §9) and
the **intermediate lines** that are supposed to produce the answers (§10). Read it expecting a
correct final number over a defective step, and re-do every worked example.

---

## J1 — Matter, Atomic Structure and Semiconductor Materials

·J p2–p9, 8 pages. **Seven substantive flags, fifteen cosmetic.** This is the most definitional range
in the course and its defects are correspondingly verbal: five of the seven substantive flags are
sentences that describe the wrong thing. Only one calculation appears in the whole range, and its
formula is misprinted (`JV1.4`).

### Substantive

#### JV1.1 · Hydrogen given a nucleus of protons and neutrons ·J p4

**Printed:** *"The nucleus has only one proton apart. In a simple hydrogen atom the nucleus is made
of protons and neutrons of approximately equal numbers."*

**Should read:**
$$\boxed{\;\text{hydrogen nucleus} = 1\ \text{proton},\ 0\ \text{neutrons};\quad \text{heavier nuclei} \approx \text{equal numbers of protons and neutrons}\;}$$

**Why.** Ordinary hydrogen has **no neutron at all** — that is exactly what makes it the simplest
atom, as the bullet immediately above it says. The sentence has been broken in the wrong place: the
"approximately equal numbers" claim is true of light-to-medium nuclei generally (carbon-12 is 6 p,
6 n), and only its attachment to *hydrogen* is wrong.

#### JV1.2 · A proton emitted on an electron transition ·J p5

**Printed:** *"a single **proton** is emitted"*, introducing $hf = E_i - E_f$.

**Should read:**
$$\boxed{\;\text{a single \textbf{photon} is emitted, of energy } E_i - E_f \text{ and frequency } f = (E_i-E_f)/h\;}$$

**Why.** A proton is a nuclear particle; if an orbital transition emitted one the atom would change
element. **The equation beside the sentence is the giveaway** — $hf$ is a photon energy, and the
same $hf$ returns later in the course for photodiodes and LEDs with $E_g$ in place of $E_i - E_f$.

#### JV1.3 · A generic shell schematic captioned as a carbon atom ·J p5

**Printed:** *"The figure above shows the structure of a **carbon atom**."*

**Should read:** a generic shell / sub-shell / forbidden-gap schematic. Carbon is
$$\boxed{\;\mathrm{C}:\ Z = 6,\quad \text{shells } 2\!:\!4,\quad 4\ \text{valence electrons}\;}$$

**Why.** Count the drawing: **eight rings** — five solid, three dashed — and only **two × marks**.
Carbon has two shells and six electrons; neither number fits on any reading. Check: $2+4 = 6 = Z$.
That four-valence-electron structure is what the semiconductor classification three pages later
depends on.

#### JV1.4 · The shell-capacity rule printed as $2^{n}$ ·J p6

**Printed:** *"Max No $= 2^{n}$"*, with $n$ as an exponent.

**Should read:**
$$\boxed{\;N = 2n^{2}\;}$$

**Why.** **The printed formula contradicts its own next line**, which substitutes $2\times3^{2}$ —
that is $2n^2$, not $2^n$ — and reaches 18, the answer the page states. The rule is given as $2n^2$
twice on ·J p5. The two agree only at $n = 1$; at $n = 2$ they give 4 against 8, at $n = 3$ 8
against 18, at $n = 4$ 16 against 32.

#### JV1.5 · Sulphur's shell structure printed as 2.3.6 ·J p6

**Printed:** *"S = 16   2.3.6"*

**Should read:**
$$\boxed{\;\mathrm{S}:\ Z = 16,\quad 2\,.\,8\,.\,6\;}$$

**Why.** The shell occupancies must sum to the atomic number, and $2+3+6 = 11 \neq 16$; with 8 in
the middle, $2+8+6 = 16$ ✓. The boron line on the same page is right ($2+3 = 5$), so the notation is
sound and only the sulphur figure slipped — and 8 is both the $2n^2$ capacity of the second shell and
the middle digit ·J p8 and ·J p9 print for silicon ($2\!:\!8\!:\!4$) and phosphorus ($2\!:\!8\!:\!5$).

#### JV1.6 · The conductor band diagram drawn with a forbidden band ·J p7

**Printed:** a band diagram with a **distinct, clear forbidden band** between the conduction and
valence bands, above text stating that the two **overlap** and that $E_g = 0$ eV.

**Should read:**
$$\boxed{\;\text{conductor: conduction and valence bands touch or overlap},\quad E_g = 0\ \mathrm{eV},\quad \text{no forbidden band}\;}$$

**Why.** A gap that is drawn is not a gap of zero width, and the figure contradicts the text beside
it. It matters because the three band diagrams in this section are distinguished from each other
**only** by the width of the middle strip — a conductor drawn with a visible gap is
indistinguishable from a narrow-gap semiconductor. The same figure appears in reference deck ·RD2
p2; see the cross-tier section, because that is not independent confirmation.

#### JV1.7 · Charge defined as an amount of current ·J p9

**Printed:** *"Charge — amount of current passing through a given point for a given time"*, with a
second line, *"the ability to attract or repel electrons"*.

**Should read:**
$$\boxed{\;\text{charge is the quantity of electricity in a body};\quad Q = It \text{ is the charge a steady current } I \text{ transports in time } t\;}$$

**Why.** Charge and current are different quantities with different units, and the printed sentence
puts charge in amperes; the second line describes an *effect* of charge rather than defining it.
Check by units: $[Q] = \mathrm{A\cdot s} = \mathrm{C}$ ✓. **The equation is right and only the words
above it are wrong** — and ·J p4 gives the sound definition, so the document contradicts itself five
pages apart.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC1.1** | p5 | "Neil Bohrls", "Bohrl" | Niels Bohr | the physicist's name, twice |
| **JC1.2** | p5 | "Paul's exclusion principle" | **Pauli** exclusion principle | Wolfgang Pauli; "Paul's" is not a variant |
| **JC1.3** | p6 | heading "VALENCE ELECTORNS (State electron)" | VALENCE ELECTRONS | letters transposed; the parenthetical does not resolve and is **not** guessed at |
| **JC1.4** | p6 | "N = 3" for the **shell number** | $n = 3$ | ·J p5 uses capital $N$ for the electron **count** and lower-case $n$ for the shell — here the letter that should be the answer is used for the input |
| **JC1.5** | p4 | "an equal number of +vely charged **atoms** and –vely charged electrons" | +vely charged **protons** | atoms are not the positive charge carrier in a neutral atom |
| **JC1.6** | p3, p9 | "Phosphorous" | phosphorus | *phosphorous* is the adjective for phosphorus(III) compounds, a different word |
| **JC1.7** | p6 | "for all the atoms with two **shall**"; "if the atom" printed twice | "with two **shells**"; single occurrence | one typo, one duplicated clause |
| **JC1.8** | p6 | "leaving the atom with an **access the charge**" | "an **excess positive** charge" | word-substitution; the sense is fixed by the neighbouring anion bullet |
| **JC1.9** | p6 | "determined by comparing the weight of it's atoms of carbon = 12" | "…with that of an atom of carbon, taken as 12" | the object of the comparison is missing from the sentence |
| **JC1.10** | p7 | "The conduction band and valence band overlap and **are very small**" | the **gap between them** is very small | it is the gap that is small, not the bands |
| **JC1.11** | p8 | semiconductor band figure: **conduction band absent**, lost at the page break | hatched conduction band above a moderate forbidden band | the figure as printed shows two of three bands |
| **JC1.12** | p4 | atom-figure leaders: "Shell" lands on a **dashed** ring, one "Sub Shells" leader sits between **solid** rings | solid rings are shells, dashed rings sub-shells | fixed from the ·J p5 text, which states the convention |
| **JC1.13** | p2 | "comes from the 2 words: Electrons …, Mechanics – Study of motion of an electron" | *electronics* = electron + *-ics*; mechanics is the study of motion generally | the etymology is invented; mechanics is not "of an electron" |
| **JC1.14** | p3, p8 | "Entertainment - **3** stereos"; "a moderately sized **of** forbidden band" | delete both | stray tokens left in the text |
| **JC1.15** | p2–p9 | a residual cluster of typographic slips: "When **is** exists in liquid or gas"; "the individual elements **poses** the same properties"; "consists **on** one electron"; "well defined shells **of** levels"; "the general **formulae** $N = 2n^2$"; "**plank's** constant"; "no room for all the electrons in **state** near the nucleus"; "determines **it'd** stability"; "an **addition** orbit/electron"; "ionize **it.The** gas"; "0**ev**", "5**ev**", "1.1**ev**"; "**Material** used in electrical & electronic circuits"; "**semi conductors**", "e. g silicon" | it; possess; **of**; **or**; formula; **Planck's**; states; its; **additional orbital**; add the space; **eV**; Materials; semiconductors; e.g. | spelling, grammar and unit-capitalisation cluster; nothing computed changes. Note **eV** takes a capital V, for Volta |

---

## J2 — Resistors and DC Network Theorems

·J p10–p23, 14 pages. **Seven substantive flags, twenty-one cosmetic** — the largest cosmetic count
in the course. It is also the range with **no second source anywhere in the knowledge base**: the
seven lesson documents contain no treatment of dc network theory or passive components at all, so
every flag here stands alone and every gap is marked rather than filled.

### Substantive

#### JV2.1 · The multiplier band given the wrong colour ·J p11

**Printed:** **Orange, Blue, Yellow, Brown** for $36\times10^{6}\ \Omega \pm 1\,\%$.

**Should read:**
$$\boxed{\;\text{Orange},\ \text{Blue},\ \textbf{Blue},\ \text{Brown}\;}$$

**Why.** Bands 1 and 2 are right (Orange = 3, Blue = 6) and Brown = ±1 % is right. The third band is
the multiplier and must carry $10^{6}$, which **the page's own table gives as Blue**; Yellow is
$10^{4}$, so the printed code decodes to $36\times10^{4} = 360\ \mathrm{k\Omega}$ — a hundred times
too small. The stated answer is correct; only the colour is wrong.

#### JV2.2 · Both solutions read the colour bands backwards ·J p12

**Printed:** part (i) is *given* as Brown, Orange, Black, Red and *solved* as Red, Black, Orange,
Brown; part (ii) is given as Yellow, brown, Green and solved as Green, Brown, Yellow. The page never
says why.

**Should read:** state the reading direction before decoding. Read left-to-right exactly as listed,
$$\text{i:}\quad 1,\ 3,\ \times10^{0},\ \pm2\,\% = 13\ \Omega \pm 2\,\%;\qquad \text{ii:}\quad 4,\ 1,\ \times10^{5},\ \pm20\,\% = 4.1\ \mathrm{M\Omega} \pm 20\,\%$$
— neither of which is the printed answer.

**Why.** The exercise stem is truncated to "**left are.**" (`JC2.8`), and the missing opening almost
certainly read *"…whose colour bands from **right to** left are"*, which makes both reversals
correct and makes the exercise a deliberate test of which end to start from. **Two independent parts
reversing the same way is not a slip.** This is an inference from the surviving fragment, not the
notes' words, and it cannot be confirmed from the pages supplied.

#### JV2.3 · The parallel derivation opened with the series rule ·J p13

**Printed:** $I = I_{R1} = I_{R2} = I_{R3}$, as the first line under the parallel circuit.

**Should read:**
$$\boxed{\;V_s = V_{R1} = V_{R2} = V_{R3}, \qquad I_t = I_{R1}+I_{R2}+I_{R3}\;}$$

**Why.** That is the **series** result, copied over from the previous section. It is false for the
circuit drawn — three different resistors across one supply carry three different currents, and the
page's own worked numbers are 0.222 A, 0.034 A and 0.000027 A. **The page's own next two lines say
exactly the corrected form**, so the opening line contradicts the two beneath it.

#### JV2.4 · A voltage assigned to the wrong resistor ·J p15

**Printed:** $V_{R3} = V_{R6} = V_{Rc} = 30.104\ \mathrm{V}$

**Should read:**
$$\boxed{\;V_{R3} = V_{Rb} = V_{Rc} = 30.104\ \mathrm{V}\;}$$

**Why.** $R_c$ is the parallel combination of $R_3$ and $R_b$, so the two things across it are $R_3$
and $R_b$; $R_6$ sits inside $R_a$, two levels further down the ladder. **The page itself computes
$V_{R6} = 10.754\ \mathrm{V}$ six lines later.** Taking $V_{R6} = 30.104\ \mathrm{V}$ would give
$I_{R6} = 0.602\ \mathrm{A}$ instead of 0.215 A, and the branch currents would no longer sum to
$I_{R4}$.

#### JV2.5 · The polar impedance printed with its magnitude in the denominator ·J p16

**Printed:**
$$Z = \frac{R+jX}{\sqrt{R^{2}+X^{2}}}\ \angle\,\tan^{-1}\frac{X}{R}$$

**Should read:**
$$\boxed{\;Z = R + jX = \sqrt{R^{2}+X^{2}}\ \angle\,\tan^{-1}\frac{X}{R}\;}$$

**Why.** $\sqrt{R^2+X^2}$ **is** the modulus of $R + jX$, so the printed quotient has modulus exactly
**1** for every $R$ and $X$ — a unit phasor, and dimensionless where an impedance must be in ohms.
The likely origin is a layout accident: the two halves of one equation stacked into a fraction.
Nothing else on the page uses it; everything that follows is purely resistive.

#### JV2.6 · The second load case multiplied by the first case's current ·J p16

**Printed:** $V_{RL} = I_tR_L = \mathbf{10}\times5.995 = 5.995\ \mathrm{V}$

**Should read:**
$$\boxed{\;V_{RL} = I_tR_L = 1\times5.995 = 5.995\ \mathrm{V}\;}$$

**Why.** **The line immediately above computes $I_t = 6/6 = 1\ \mathrm{A}$ for this case**; the 10 A
belongs to the first case. The printed answer is right but the printed step is not — worked as it
stands it gives 59.95 V, ten times the emf, from a 6 V battery.

#### JV2.7 · The source transformation stated as shorting the source ·J p17

**Printed:** *"If you short circuit constant voltage source get a constant current source"*.

**Should read:**
$$\boxed{\;I_N = \frac{V_s}{R_i}\;}$$
A constant-voltage source $V_s$ in **series** with $R_i$ is equivalent, at its terminals, to a
constant-current source $I_N = V_s/R_i$ in **parallel** with the same $R_i$, where $I_N$ is the
current that flows when the **terminals** are short-circuited.

**Why.** It is the terminals that are shorted to *measure* $I_N$, not the source that is shorted to
*become* a current source — shorting a real voltage source simply collapses its terminal voltage to
zero (at 6 V into 0.005 Ω, two sections earlier, it would draw 1200 A). The transformation also
requires $R_i$ to be carried across in parallel; dropping it leaves an ideal current source, a
different circuit. This is the same transformation ·J p19–p21 uses to get from the Thevenin form to
the Norton form.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC2.1** | p10 | "A resistor is a passive component which **apposes** the flow of current in **Q** circuit" | opposes … in **a** circuit | two character-level slips in one sentence |
| **JC2.2** | p10 | "Power … Is the **amount** of energy dissipated in a circuit" | the **rate** at which energy is dissipated | the 1 A / 1 V sentence beside it defines the **watt**, which is a rate |
| **JC2.3** | p10 | "Voltage … is the **energy** which drives charge" | energy **per unit charge**, $V = W/Q$ (J/C) | energy alone is joules, not volts |
| **JC2.4** | p10 | factor (b) headed "Cross sectional Area" with the relation $R \propto L/A$ | the area factor alone is $R \propto 1/A$ | the combined relation is printed under a heading naming one variable |
| **JC2.5** | p10 | the proportionality sign typed as a Greek **α**: "R α L" | $R \propto L$ | α is the common-base current gain elsewhere in BEE 3103 — a clash worth avoiding |
| **JC2.6** | p11 | last table row printed "**No. band**" | **no band** — a three-band resistor, tolerance ±20 % | reads as an abbreviation for "number of bands"; it is the absence of one |
| **JC2.7** | p11 | "4K54 … This is **equivalent** to $4.5\times10^{3}$" | 4K54 = 4.54 kΩ; 4.5 kΩ is a **rounding** to two significant figures | "equivalent" asserts an identity that is 0.9 % out |
| **JC2.8** | p12 | the exercise stem truncated to "**left are.**" | the opening is lost at the p11/p12 break | the reversal in both solutions implies "…from **right to** left are" — see **JV2.2** |
| **JC2.9** | p13 | parts lettered "(a) (b) (c) **(e)**"; part (c) answered with voltages | there is no (d); (c) asks for currents | all three currents are the same 27.0 µA |
| **JC2.10** | p13, p14, p15, p21 | the decimal point set as a separate dot: $\frac{200}{779}.022$, $\frac{1}{62}.22$, $\frac{50}{9}.39$, $30.\frac{104}{20}$, $\frac{40}{16}.67$ | $\frac{200}{779.022}$, $\frac{1}{62.22}$, $\frac{50}{9.39}$, $\frac{30.104}{20}$, $\frac{40}{16.67}$ | equation-editor artefact, five times across four pages; every printed answer is nevertheless right |
| **JC2.11** | p14 | first line of part (d) clipped by the page edge | $I_{R1} = V_{R1}/R_1 = 200/900$ | ⚠ ILLEGIBLE — the result is not recoverable from the render |
| **JC2.12** | p14 | "(d) Voltage **through** each resistor" | voltage **across** each resistor | current is *through*, voltage is *across* |
| **JC2.13** | p15 | "Wattage for one **reisistor**", twice | resistor | letters transposed, both occurrences |
| **JC2.14** | p12, p18 | bold subscript digits **2** and **3** render almost identically, so $V_{R3}$ reads as $V_{R2}$; and "$R_t = R_{Th\underline{=}}R_3+\dots$" sets the second equals sign at subscript level | $V_{R3}$; $R_t = R_{Th} = R_3 + \frac{R_1R_2}{R_1+R_2}$ | font artefacts of the equation editor |
| **JC2.15** | p19 | heading "**NORTONS THEOREM**" | Norton's theorem | missing apostrophe |
| **JC2.16** | p20 | first line clipped; only "$R_t$" survives | $I_t = V_s/R_t$ | ⚠ ILLEGIBLE — recovered from the procedure it belongs to, recorded as an inference |
| **JC2.17** | p22 | "Using **Kirchoff's current law** the two loops …" | Kirchhoff's **voltage** law for the loops | KCL is the node equation $I_1+I_3 = I_2$, printed separately; the name is also misspelt |
| **JC2.18** | p22 | "Simplifying and **eliminating $I_3$**" | $I_3$ is still present | the two lines are the pair **scaled** so that subtracting them eliminates it |
| **JC2.19** | p22 | $I_3 = 0.8185\ \mathrm{A}$ | $I_3 = 9/11 = 0.8182\ \mathrm{A}$ | rounding slip in the fourth decimal; nothing downstream moves |
| **JC2.20** | p23 | "1 **MW**", "0.3 **MW**" | 1 MΩ, 0.3 MΩ | the ohm glyph lost to a font substitution — the same mechanism as `C2.13` in Part B |
| **JC2.21** | p23 | "time stabilities" set in **blue hyperlink colouring** (also "doped" on ·J p24) | ordinary body text | a web-copy artefact; the text is readable and carries no link |

---

## J3 — Capacitors, Inductors and Transformers

·J p24–p32, 9 pages. **Eight substantive flags, twelve cosmetic.** Like J2, this range has **no
second source**: no lesson document defines capacitance, derives the series or parallel rule, or
sets out the transformer relations. Five of the eight substantive flags are definitions attached to
the wrong quantity, and the remaining three are all in one worked example.

### Substantive

#### JV3.1 · Permittivity defined as permeability ·J p24

**Printed:** *"Dielectric material (ε) - Permittivity is the ability of material to allow an
electronic field to pass through, the extent to which a material affects magnetic field."*

**Should read:** permittivity is an **electric** quantity,
$$\boxed{\;\varepsilon = \varepsilon_r\varepsilon_0,\qquad \mathbf{D} = \varepsilon\,\mathbf{E}\;}$$

**Why.** The property that measures how a material affects the **magnetic** field is **permeability**
$\mu$ — and **·J p29 defines it correctly, in almost the same words**: *"Permeability is the ability
of a material to affect the magnetic field H."* Two sentences five pages apart say the same thing
about two opposite quantities, which leaves the reader with no distinct idea for $\mu$ when the
inductor section arrives.

#### JV3.2 · The NPO ceramic range out by a factor of 1000 ·J p27

**Printed:** *"…come in a capacitance range of 1.0 pF to 0.033 **mF**."*

**Should read:**
$$\boxed{\;1.0\ \mathrm{pF}\ \text{to}\ 0.033\ \mathrm{\mu F}\;}$$

**Why.** $0.033\ \mathrm{mF} = 33\ \mathrm{\mu F}$, and a 33 µF NPO ceramic does not exist: the same
paragraph has just said that even *high-K* ceramics reach only "several microfarads", and NPO is the
least dense ceramic dielectric of all. The neighbouring N750 range (4.0–680 pF) confirms the order
of magnitude. **µ set as m is the commonest unit slip in these notes and is always a factor of
$10^{3}$.**

#### JV3.3 · Self-inductance defined as mutual inductance ·J p29

**Printed:** *"Self–Inductance: This is the ability of material / coil to induce emf at the
surroundings."*

**Should read:**
$$\boxed{\;e = -L\,\frac{\mathrm{d}i}{\mathrm{d}t}\;}$$
— the emf a coil induces **in itself** when the current **through itself** changes.

**Why.** The whole distinction between *self* and *mutual* is whether the emf appears in the same
circuit or a different one, and "inducing emf at the surroundings" is the definition of **mutual**
inductance — which the page gives, in those words, three lines below. **As printed the two
definitions say the same thing** and there is no way to tell them apart.

#### JV3.4 · Mutual inductance driven by changing voltage ·J p29

**Printed:** *"Mutual inductance: This is the process by which changing **voltage** in a conductor
induces emf in a second conductor which is in the opposite direction (Lenz's Law)."*

**Should read:**
$$\boxed{\;e_2 = -M\,\frac{\mathrm{d}i_1}{\mathrm{d}t}\;}$$
with $M$ the mutual inductance in henries.

**Why.** Faraday's law is about flux linkage, and flux is set by **current**, not by terminal
voltage — two circuits can have identical voltages and completely different couplings. A second slip
in the same sentence: Lenz's law says the induced emf opposes **the change in flux that produced
it** (the minus sign), not that the second conductor's emf points opposite to the first's.

#### JV3.5 · A flat 180° phase claim for every transformer ·J p31

**Printed:** *"The phase difference between the primary coil and secondary coil voltage is $180^0$
as shown in the diagram below."*

**Should read:**
$$\boxed{\;\text{like-marked (dotted) terminals} \Rightarrow V_p,\,V_s \text{ in phase};\quad \text{opposite marking} \Rightarrow 180^\circ\;}$$

**Why.** Both windings link the *same* core flux, so both emfs follow the same
$-\mathrm{d}\Phi/\mathrm{d}t$; whether the secondary voltage comes out in phase or antiphase depends
purely on **which way the secondary is wound**, which is what the dot convention exists to record.
Reverse the secondary's two leads and the same transformer gives the opposite answer — and the
centre-tapped rectifier depends on exactly this, its two half-secondaries being deliberately in
antiphase. **In an exam:** these are the course's own notes and they state 180° flatly, so a CAT
question lifted from this page expects **180°**. Give it, and add the one-line qualifier.

#### JV3.6 · A digit dropped from the denominator of $V_p$ ·J p32

**Printed:** $V_p = \dfrac{N_p\times V_s}{N_s} = \dfrac{400\times20}{\mathbf{200}} = 4\ \mathrm{V}$

**Should read:**
$$\boxed{\;V_p = \frac{400\times20}{2000} = 4\ \mathrm{V}\;}$$

**Why.** $N_s = 2000$, as the statement says two lines above and as the step immediately before
divides by correctly. **As printed the arithmetic is false**: $8000/200 = 40$, not 4. The printed
*answer* is right, so a reader who re-does the sum as written gets 40 V and then cannot reproduce
the answer beneath it.

#### JV3.7 · A digit added to the denominator of the efficiency step ·J p32

**Printed:** $\dfrac{I_s\times V_s}{I_p\times V_p} = \dfrac{I_s\times20}{\mathbf{40}\times0.5} = 0.9$

**Should read:**
$$\boxed{\;\frac{I_s\times20}{4\times0.5} = 0.9 \;\Longrightarrow\; I_s = 0.09\ \mathrm{A}\;}$$

**Why.** The slot holds $V_p$, which the line above has just established as **4 V**, not 40. As
printed the denominator is 20 and $I_s = 0.9\ \mathrm{A}$ — **ten times** the answer the page then
states. **Note the pattern:** `JV3.6` drops a zero and `JV3.7` adds one, in consecutive lines of the
same example, both around a correct result.

#### JV3.8 · Two different answers for $I_s$, with neither withdrawn ·J p32

**Printed:** step 1 obtains $I_s = 0.1\ \mathrm{A}$ from $I_s/I_p = N_p/N_s$; step 3 obtains
$I_s = 0.09\ \mathrm{A}$ from $\eta = 90\,\%$. Both stand, and the question asked for one number.

**Should read:**
$$\boxed{\;I_s\big|_{\text{ideal}} = 0.1\ \mathrm{A}\ \text{ is superseded by }\ I_s\big|_{\eta = 90\%} = 0.09\ \mathrm{A}\;}$$

**Why.** $I_s/I_p = N_p/N_s$ is a **consequence of $P_p = P_s$** and holds only for a lossless
transformer; once $\eta = 90\,\%$ is imposed it fails by exactly that factor —
$I_s/I_p = 0.09/0.5 = 0.18$ against $N_p/N_s = 0.2$, and $0.18 = 0.9\times0.2$. The general form is
$$\boxed{\;\frac{I_s}{I_p} = \eta\,\frac{N_p}{N_s}\;}$$
The **voltage** relation $V_p/V_s = N_p/N_s$ survives, because it comes from flux linkage and not
from power balance, which is why step 2 is legitimate. A reader who stops at step 1 answers 0.1 A;
the notes' own answer is 0.09 A.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC3.1** | p24 | "allow an **electronic** field to pass through" | **electric** field | an electronic field is not a thing; same sentence as **JV3.1** |
| **JC3.2** | p24 | $\varepsilon_0 = \frac{1}{36\Pi}\times\frac{10^{-9}\,\mathrm{F}}{\mathrm{m}}$, joined by "or" to $8.854\times10^{-12}$ | $\pi$, not capital $\Pi$; and the two values are **not** equal | $\frac{1}{36\pi}\times10^{-9} = 8.8419\times10^{-12}$, 0.14 % below $8.854\times10^{-12}$ — the standard convenience approximation, not an identity |
| **JC3.3** | p24 | the two-straight-plate symbol captioned "**Ceramic capacitor**" | the **general non-polarised fixed-capacitor** symbol | it serves ceramic, film, mica and paper alike; a reader taking it literally will look for a different symbol when a film capacitor appears |
| **JC3.4** | p27 | the parallel-capacitor section opens with **no heading at all** | "Parallel Connection of Capacitors" | ·J p26 heads its series section properly; the heading appears lost with the blank space above it |
| **JC3.5** | p27 | "$Q_t = = Q_{c1}+Q_{c2}+Q_{c3}$" | one equals sign | typographic; the equation is correct as read |
| **JC3.6** | p27 | $X_c = \frac{1}{2\Pi fC}$; "the formula is dependent **of** frequency" | $\pi$; dependent **on** | the same capital-Pi substitution as **JC3.2**, plus a preposition |
| **JC3.7** | p28 | the Film Capacitors section opens with **no heading** | "Film Capacitors" | every neighbouring type — Mica, Paper-Foil-Filled, Electrolytic — has one, and ·J p27 ends before the break |
| **JC3.8** | p28 | "The **De** is equal to the total peak-to-peak ripple voltage" | almost certainly $\Delta E$ | "De" is defined nowhere and is not standard; the Symbol-font $\Delta$ appears to have dropped to a Latin D. **The reading is probable, not certain**, and nothing downstream depends on it |
| **JC3.9** | p29 | "**Henrys**"; permeability glossed as the ability to "affect the magnetic field $H$" | **henries**; strictly $\mu$ is the constant in $B = \mu H$ | the SI plural is *henries*, unit name lower-case and symbol upper-case because it honours a person; and it is $B$ the material affects for a given $H$ |
| **JC3.10** | p31 | the labels $R_p$ and $R_s$ under the transformer terminals | **not determinable** | no resistor symbol is drawn at either place, the body text never mentions them, and the two later figures on the page are the same drawing with the labels removed. ⚠ ILLEGIBLE — **nothing is inferred**; a full-resolution screenshot of the figure is needed |
| **JC3.11** | p31 | the angle typeset $180^{0}$, with a superscript zero | $180^\circ$ | degree sign lost; it recurs |
| **JC3.12** | p31 | loss item (b) printed as one run-on entry, "Eddy currents leakage current" | "Eddy currents **and** leakage flux" | two different loss mechanisms — eddy currents circulating in the core, and leakage flux failing to link the secondary — read as one |

---

## J4 — Diodes

·J p33–p45, 13 pages. **Ten substantive flags, thirteen cosmetic** — the worst substantive density in
the course, one every 1.3 pages. Two of the ten (`JV4.2`, `JV4.3`) attack the diode equation itself,
and two more (`JV4.9`, `JV4.10`) get the photodiode's mechanism backwards. **Five pages in this
range carry opaque redaction blocks** — ·J p35, p40, p41, p42 and p44.

### Substantive

#### JV4.1 · Diffusion described as the movement of ions ·J p33

**Printed:** *"The movement of ions process is called diffusion."*

**Should read:**
$$\boxed{\;\text{diffusion is the movement of the \textbf{mobile charge carriers} — electrons and holes — across the junction}\;}$$

**Why.** **The ions do not move**: the depletion layer consists of fixed, ionised dopant atoms locked
in the crystal lattice, as the two preceding sentences say. It matters because a reader who believes
ions migrate cannot explain why the barrier is **self-limiting** — it is precisely because the ions
stay put that the field they create grows until it cancels the diffusion tendency. The page's own
next sentence, *"the positive ions will repel the holes and the negative ions will repel the
electrons"*, only makes sense with the ions stationary.

#### JV4.2 · Boltzmann's constant printed as $1.38\times10^{-28}$ ·J p35

**Printed:** *"$k$ = Boltzmann's constant $= 1.38\times10^{-28}$ J/K"*

**Should read:**
$$\boxed{\;k = 1.38\times10^{-23}\ \mathrm{J\,K^{-1}}\;}$$

**Why, in one line a reader can repeat.** With the printed exponent,
$V_T = 1.38\times10^{-28}\times300/1.6\times10^{-19} = 2.6\times10^{-7}\ \mathrm{V}$ — a quarter of a
**microvolt**. The constant is wrong by $10^{5}$ and every exponent computed from it would be $10^5$
too large. Nothing on the page uses it numerically, so no result in this range is corrupted — but a
constant is memorised from pages like this one. **·L1 p3 has it right; see the cross-tier section.**

#### JV4.3 · The exponent typeset as a denominator ·J p35

**Printed:** $i_o = I_o\!\left(\dfrac{V_D}{e^{\eta V_T}} - 1\right)$

**Should read:**
$$\boxed{\;i_D = I_o\left(e^{\,V_D/\eta V_T} - 1\right)\;}$$

**Why, three ways.** (i) **Dimensions:** as printed, $e^{\eta V_T}$ exponentiates a quantity in
**volts**, and an exponent must be dimensionless. (ii) **Numbers:** silicon, $\eta = 2$,
$V_T = 25.85\ \mathrm{mV}$, $V_D = 0.7\ \mathrm{V}$, $I_o = 1\ \mathrm{pA}$ — the correct form gives
$0.76\ \mathrm{\mu A}$, the printed form gives $-3.4\times10^{-13}\ \mathrm{A}$, a **negative**
current for a **forward**-biased diode. (iii) **Behaviour:** the printed form is linear in $V_D$,
while the characteristic drawn two pages earlier is exponential. Almost certainly an equation-editor
casualty — but it is what a reader copying the page will write.

#### JV4.4 · Breakdown voltage equated with peak inverse voltage ·J p35

**Printed:** *"This point can be called breakdown voltage or peak inverse voltage (PIV)."*

**Should read:**
$$\boxed{\;V_{BR} = \text{the voltage at which breakdown physically occurs};\quad \mathrm{PIV} = \text{the manufacturer's \textbf{rating}, the largest reverse voltage the diode may safely see}\;}$$

**Why.** PIV is specified *below* $V_{BR}$, with margin — a 1N4007 is rated PIV = 1000 V and its
actual avalanche point is higher. Design to the PIV, not to the breakdown voltage; treating them as
synonyms is how rectifier diodes get destroyed in design work. ·J p46 repeats the conflation, logged
separately as `JC5.11`.

#### JV4.5 · The Thevenin divider taken across the load ·J p36

**Printed:** $V_{Th} = V_S\dfrac{R}{R_L+R}$

**Should read:**
$$\boxed{\;V_{Th} = V_S\,\frac{R}{R_S+R}\;}$$

**Why, three ways, all from the notes' own pages.** (i) The line immediately above reads *"No current
flows through $R_L$"* — a resistor carrying no current cannot appear in a divider ratio. (ii) The
next equation is $R_{Th} = R_SR/(R+R_S)$, the parallel combination of $R_S$ and $R$; a Thevenin pair
must be built from the same two elements. (iii) **·J p39 evaluates $20\times200/(100+200) = 13.33$
V**, using $R_S = 100$; as printed with $R_L = 500$ the same circuit gives 5.71 V, which the notes
never use.

#### JV4.6 · The load line's current intercept without the load ·J p36, restated p40, used p39

**Printed:** current-axis intercept $= V_{Th}/R_{Th}$.

**Should read:**
$$\boxed{\;V_D\text{-intercept} = V_{Th};\qquad I_D\text{-intercept} = \frac{V_{Th}}{R_{Th}+R_L}\;}$$

**Why.** **·J p36 itself states $I_D = V_{Th}/(R_L+R_{Th})$ three lines above the load-line
paragraph.** The short-circuit current of a loop and the current-axis intercept of its load line are
the same quantity — set $V_D = 0$ in the KVL equation — so the two statements on one page cannot both
be right. For the worked example ($V_{Th} = 13.33$ V, $R_{Th} = 66.67\ \Omega$, $R_L = 500\ \Omega$)
the notes give $13.33/66.67 = 0.2$ A against the correct $13.33/566.67 = 23.5$ mA — a factor of
**8.5**, and it moves the Q point badly. The $V_D$ intercept is right either way.

#### JV4.7 · Both silicon forward resistances labelled 20 Ω ·J p41

**Printed:** an equivalent-circuit figure labelling **both** silicon forward resistances
$20\ \Omega$.

**Should read:**
$$\boxed{\;r_f(\mathrm{Si}) = 2\ \Omega\ \text{in both branches}\;}$$

**Why, from the notes' own next line.** The problem statement on ·J p40 gives
$\mathrm{Si}: r_f = 2\ \Omega$, and the arithmetic immediately under the figure computes the
parallel combination as
$52\times2/(52+2)$ — the $D_3$ branch ($2+50 = 52\ \Omega$) against the $D_2$ branch ($2\ \Omega$).
Neither number exists if $r_f = 20\ \Omega$. With 20 Ω the branches become 20 and 70 Ω, the parallel
value 15.56 Ω, $R_t = 46.56\ \Omega$, $I_t = 0.408$ A and $P = 3.33$ W — exactly **half** the notes'
own answer.

#### JV4.8 · LED luminosity drawn as an exact straight line ·J p42

**Printed:** the luminosity characteristic as a **straight line through the origin**, asserting
$L \propto I_f$ over the whole range.

**Should read:**
$$\boxed{\;L \text{ increases \textbf{monotonically but sub-linearly} with } I_f,\ \text{saturating at high current}\;}$$

**Why, and a check.** Proportionality would mean an LED run at 10× its rated current gives 10× the
light; it gives rather less, and then fails. ·L1 p14's figure plots the measured curve — ≈1.8 mW at
50 mA, ≈2.8 mW at 100 mA, ≈3.4 mW at 150 mA, so doubling the current raises output by 1.6, not 2.
Within the 10–20 mA operating window the straight line is a fair approximation, which is presumably
the intent. **Both sources make this claim; see the cross-tier section.**

#### JV4.9 · The photodiode said to be heavily doped ·J p42

**Printed:** *"Doping is higher than other diodes to increase reverse bias current."*

**Should read:**
$$\boxed{\;\text{the active region of a photodiode is \textbf{lightly} doped — commonly an intrinsic layer (the PIN structure) — to \textbf{widen} the depletion region}\;}$$

**Why.** The photocurrent is produced by electron–hole pairs generated **inside the depletion
region**, where the field sweeps them apart before they recombine; depletion width **falls** as
doping rises, so heavy doping shrinks the light-collecting volume and cuts the responsivity. Heavy
doping also raises the **dark current**, which is the photodiode's noise floor and the one number
every datasheet minimises — so the sentence describes the parameter you want *smaller* as something
to increase.

#### JV4.10 · The photodiode's carriers generated by the applied voltage ·J p42

**Printed:** *"When a reverse voltage is applied electrons move from the valence band to the
conduction band increasing the conductivity of the material."*

**Should read:**
$$\boxed{\;\text{\textbf{absorbed photons} of energy } h\nu \ge E_g \text{ generate the electron–hole pairs; the reverse bias merely \textbf{sweeps them out} as photocurrent}\;}$$

**Why, from the notes' own next page.** **Light is never mentioned in the operating mechanism at
all** — in the description of a *photo*diode. ·J p43's first figure plots $I_R$ against light
intensity $E$ as a line **through the origin**: zero light, zero photocurrent, whatever the reverse
voltage. If the applied voltage caused the excitation, that line would not pass through the origin.
The page's own **dark current** is the small residue left when the photo-generation is switched off.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC4.1** | p35 | diode current written $i_o$, saturation current $I_o$ | $i_D$ (or $I_D$) and $I_o$ (or $I_S$) | the same letter in two cases, distinguished only by capitalisation, on the two sides of one equation — a `_nomenclature.md` clash |
| **JC4.2** | p34 | "the depletion layer is enlarged due to majority charge carriers **(electrons)** moving away" | **both** majority species retreat | electrons withdraw into the N region *and* holes into the P region; it takes both to widen the layer at both edges |
| **JC4.3** | p34 | leakage current "expressed in terms of **µA**", unqualified | µA is the **germanium** order; silicon is **nA** | three orders of magnitude apart; `11-diodes.md` §1.4 states both |
| **JC4.4** | p37 | the small-signal source drawn as a **circle with an arrow** (an ideal current source), in series with $V_{Th}$ and $R_{Th}$, and labelled $i_D$ | a small-signal **voltage** source $v_d$ in series with $V_{Th}$ | a current source in that position would fix the loop current and make $R_{Th}$ and $R_L$ irrelevant; the construction on the next page needs a voltage swing |
| **JC4.5** | p39 | "$V_{Th} = 13.33\ \Omega$" | $13.33\ \mathrm{V}$ | $20\ \mathrm{V}\times200\,\Omega/300\,\Omega$ has units of volts; the same number is used correctly on the next page |
| **JC4.6** | p41 | figure labels the combined branch resistance **1.962 Ω** | **1.926 Ω**, as computed on the line above and used in $R_t = 32.926$ | digit transposition in the figure only; using 1.962 moves the answer in the fourth significant figure and the printed 6.66 W is unaffected |
| **JC4.7** | p41 | $I_t = \dfrac{19}{32}.926 = 0.577\ \mathrm{A}$ | $19/32.926$ | the equation editor split the denominator, stranding $.926$ beside the bar; read literally $19/32 = 0.594$, not 0.577 |
| **JC4.8** | p41 | "a transducer which changes **bacterial** energy to light energy" | **electrical** | settled by the application list on ·J p42: *"since it converts **electrical** energy to light energy"* |
| **JC4.9** | p42 | LED current rating printed "**20 – 10mA**" | 10–20 mA | written from the larger value to the smaller; both endpoints are the conventional ones |
| **JC4.10** | p43 | the page's top heading survives only as the bottom two or three pixel rows of its glyphs | **"Characteristic Curve"** | ⚠ ILLEGIBLE — word-shape gives two words of about 14 and 5 characters, and the same heading occupies the same position in the LED (·J p42) and varactor (·J p45) sections. **Recorded as an inference** |
| **JC4.11** | p43 | list headed "Factors affecting light intensity" whose **first item is "Light intensity"** | "Factors affecting the (reverse) photocurrent $I_R$" | a quantity cannot be a factor affecting itself; the list's position, right after the dark-current equation and the $I_R$ curves, fixes what it is about |
| **JC4.12** | p45 | $f_r = \dfrac{1}{2\Pi\sqrt{LC}}$ | $f_r = \dfrac{1}{2\pi\sqrt{LC}}$ | capital $\Pi$ is the product operator; the same substitution as `JC3.2` and `JC3.6` |
| **JC4.13** | p33–p45 | word-substitution cluster: "electrons … **more** to fit in the holes"; "a diode **exhibits** negative resistance"; "there will **an** increment of current"; "the diode **stars** behaving"; "P–N junction as the **electric** material"; "Tuning circuit **log** with inductors" | move; a diode **which** exhibits; there will **be** an; starts; **dielectric**; **along** with | the dielectric case is settled by the same figure's own label, "Dielectric materials" |

---

## J5 — Rectifiers, Filters and Regulation

·J p46–p56, 11 pages. **Seven substantive flags, eleven cosmetic.** Unusually derivation-heavy for
these notes — ·J p47, p48 and p49 are almost nothing but integration and algebra — and every one of
the four constants derived there is confirmed independently by ·L2. Two pages, ·J p53 and ·J p55,
carry opaque redaction blocks.

### Substantive

#### JV5.1 · The half-wave efficiency with the exponent on the wrong bracket ·J p47

**Printed:**
$$\eta = \frac{\left(\dfrac{I_m}{\pi}\right)^{2}R_L}{\left(\dfrac{I_m}{2}\right)\left(R_L+r_f\right)^{2}}$$

**Should read:**
$$\boxed{\;\eta = \frac{\left(\dfrac{I_m}{\pi}\right)^{2}R_L}{\left(\dfrac{I_m}{2}\right)^{2}\left(R_L+r_f\right)}\;}$$

**Why, two checks.** (i) **Dimensionally**, the printed denominator is $\mathrm{A}\cdot\Omega^{2}$
against a numerator of $\mathrm{A}^{2}\Omega$, so the ratio is not dimensionless and cannot be an
efficiency. (ii) **Algebraically**, the printed form does not reduce to the $4/\pi^{2}$ the very next
line states; only the corrected form does. The denominator is $P_{ac} = I_{rms}^{2}(R_L+r_f)$, so
the square belongs on $I_m/2$.

#### JV5.2 · The half-wave rms substituted into the full-wave power ·J p49

**Printed:**
$$P_{ac} = I_{rms}^{2}\left(R_L+r_f\right) = \left(\frac{I_m}{2}\right)^{2}\left(R_L+r_f\right)$$

**Should read:**
$$\boxed{\;P_{ac} = \left(\frac{I_m}{\sqrt2}\right)^{2}\left(R_L+r_f\right) = \frac{I_m^{2}}{2}\left(R_L+r_f\right)\;}$$

**Why.** $I_m/2$ is the **half-wave** value, carried over verbatim from ·J p47 — and **two lines
above, this same page derives $I_{rms} = I_m/\sqrt2$ for this circuit**. Substituting $I_m/2$ gives
$\eta = 8/\pi^{2}\times\tfrac12 = 4/\pi^{2} = 40.5\,\%$, the half-wave answer, not the 81.1 % the
next line states.

#### JV5.3 · The full-wave efficiency with the same misplaced exponent ·J p49

**Printed:**
$$\eta = \frac{\left(\dfrac{2I_m}{\pi}\right)^{2}R_L}{\left(\dfrac{I_m}{\sqrt2}\right)\left(R_L+r_f\right)^{2}}$$

**Should read:**
$$\boxed{\;\eta = \frac{\left(\dfrac{2I_m}{\pi}\right)^{2}R_L}{\left(\dfrac{I_m}{\sqrt2}\right)^{2}\left(R_L+r_f\right)}\;}$$

**Why.** Identical to `JV5.1`. Dimensional check: printed denominator $\mathrm{A}\cdot\Omega^{2}$
against numerator $\mathrm{A}^{2}\Omega$. Algebraic check: only the corrected form collapses to the
$8/\pi^{2}$ printed on the next line.

#### JV5.4 · An extra zero in the off-state current ·J p55

**Printed:**
$$I_t = \frac{V_S}{R+R_L} = \frac{40}{500+800} = \frac{400}{1300} = 0.031\ \mathrm{A}$$

**Should read:**
$$\boxed{\;I_t = \frac{40}{1300} = 0.0308\ \mathrm{A} \approx 31\ \mathrm{mA}\;}$$

**Why.** The third fraction has an extra zero in its numerator. $40/1300 = 0.03077$, which is the
0.031 A stated; $400/1300 = 0.3077$, ten times larger. **A learner copying the printed fraction gets
0.31 A and a tenfold error in everything downstream.**

#### JV5.5 · Charge and discharge given the same time constant ·J p51

**Printed:** both exponentials with time constant $RC$ —
$V_C = V_S(1-e^{-t/RC})$ and $V_C = V_Se^{-t/RC}$.

**Should read:**
$$\boxed{\;V_C = V_S\left(1-e^{-t/r_fC}\right)\ \text{(charging)};\qquad V_C = V_S\,e^{-t/R_LC}\ \text{(discharging)}\;}$$

**Why.** **The page's own argument turns on the capacitor "taking a longer time to discharge" than to
charge**, which is only true if the two paths have different resistances — and they do: charging is
through the conducting diode and transformer, resistance $r_f$ (tens of ohms); discharging is through
the load, $R_L$ (hundreds of ohms or more). With this range's values, $r_fC = 20C$ against
$R_LC = 800C$, a factor of **40**, which is exactly why the drawn waveform has a short charging
interval and a long discharging one. Written with one $RC$ the equations describe a symmetric wave
that the same page then draws asymmetrically.

#### JV5.6 · The two-sided zener clipper with one zener reversed ·J p56

**Printed:** in the **lower** of the two "both sides" circuits, both zeners point the same way —
upper anode to lower cathode, i.e. series-aiding.

**Should read:** the two zeners joined **anode to anode** (as in the upper circuit of the pair) or
**cathode to cathode**; either works, and both give
$$\boxed{\;v_{out} = \pm\left(V_Z+V_F\right)\;}$$

**Why.** As drawn, a **positive** input reverse-biases both, so the branch does not conduct until the
node reaches $2V_Z = 50$ V, not 25 V; a **negative** input forward-biases both, clamping at about
$-1.4$ V. That is a strongly asymmetric limiter, $+50$ V against $-1.4$ V, and **it cannot produce
the symmetric waveform drawn directly beneath it**. Two zeners series-aiding are the
voltage-reference divider arrangement — a different circuit for a different purpose.

#### JV5.7 · The shunt clipping element drawn as a battery ·J p56

**Printed:** a plain 25 V **battery** across the load, with a clipped output waveform beneath.

**Should read:**
$$\boxed{\;v_{out} = \begin{cases} +V_Z \approx +25\ \mathrm{V}, & v_{in}\ \text{large and positive}\\ v_{in}\dfrac{R_L}{R+R_L}, & \text{between the limits}\\ -V_F \approx -0.7\ \mathrm{V}, & v_{in}\ \text{negative}\end{cases}\;}$$

**Why, two separate problems.** (i) **The symbol.** A battery across the load would hold the output at
exactly $+25$ V for the **whole** cycle — a flat dc line, not the drawn waveform. What the caption
and waveform describe is a **zener**, cathode to the top rail; the battery is the zener's *on-state
equivalent* from ·J p54, substituted into the circuit diagram itself. (ii) **The negative half
cycle.** A real single zener in that position is **forward** biased on the negative half cycle,
conducts heavily and clamps at about $-0.7$ V — so the lower graph should be a nearly flat line just
below the axis, not the full $-25$ V half-sine drawn.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC5.1** | p47 | $\frac{I_m}{2\pi}\left[-\cos\theta\right]_0^{\pi}\,\mathbf{d\theta} = \dots$ | the $\mathrm{d}\theta$ belongs with the integral sign on the line above | once the antiderivative is in square brackets the differential is gone; the line also drops its "$I_{dc} =$" label |
| **JC5.2** | p47, repeated p49 | $\eta = 0.\dfrac{405}{\left(1+r_f/R_L\right)}$, and $0.\dfrac{811}{(\cdots)}$ | $\dfrac{0.405}{1+r_f/R_L}$, $\dfrac{0.811}{1+r_f/R_L}$ | "0." stranded outside the fraction — a broken decimal, not a coefficient |
| **JC5.3** | p47, repeated p49 | ripple factor as "the ratio of ac to dc current ( $I_1ac/I_1dc$ )" | $I_{ac}/I_{dc}$ | a spurious subscript 1 on both currents, with "ac"/"dc" set as italic variables rather than subscripts |
| **JC5.4** | p55 | "$P_Z = I_ZV_Z = 0.03125\times15 = 0.46875\ \mathbf{A}$" | $0.46875\ \mathrm{W}$, or 469 mW | the number is right and the unit is not; $P_Z$ is the quantity compared against the diode's wattage rating, so "A" invites the wrong comparison |
| **JC5.5** | p49, p54 | two items printed **in red ink**: the heading "Rms value of a.c output current" (·J p49) and "(Si – 0.7V, Ge- 0.3V)" (·J p54) | ordinary black body text | colour carries no meaning anywhere else in the document, and the identical heading on ·J p47 is black; a reader on the colour PDF should not read emphasis into it |
| **JC5.6** | p50 | the bridge-rectifier section opens with **no heading** | "(b) Bridge Rectifier" | ·J p48 heads the centre-tapped circuit "(a) Centre-Tapped Rectifier"; the blank foot of ·J p49 shows nothing was pushed over the break — **this heading was never typed** |
| **JC5.7** | p51 | figure, then heading *Half-wave rectifier*, then waveforms, then heading *Capacitor filter*; and the capacitor charges towards $V_S$ in the equation but to $V_m$ in the prose | the circuit belongs under "Capacitor filter"; one symbol for one quantity | the figure precedes its own heading by two headings; layout only |
| **JC5.8** | p55 | the off-state circuit opens the page with **no heading**; "On state" appears only above the *second* circuit | add "Off state" | the reader must deduce the state from the open gap in the figure; ·J p54 ends with blank space, so nothing was lost at the break |
| **JC5.9** | p54 | in panel 2 the battery replacing the diode **carries no label** | label it $V_Z$ | the neighbouring panels both label their device ($Z$, and $I_z = 0$), and the same battery **is** labelled $V_Z$ when redrawn on ·J p55 |
| **JC5.10** | p46–p56 | grammar cluster: "an output can be **from** the resistor"; "there will be an output at $R_L$ **is** as a result of"; "made **using of** capacitors"; "result **to** an output"; "less than **of** half-wave"; "minimized"; "results **to** a more refined"; "behaves like any other diode **conducts** at"; "to limit amount of current related to diode **the rating**" | can be **taken from**; strike the "is"; made **using** / made **use of**; result **in**; less than **that of**; minimised; results **in**; diode **and conducts**; **the diode rating** | word substitutions and transpositions; nothing computed changes |
| **JC5.11** | p46 | "diodes which have a high power rating and peak inverse voltage**/** breakdown voltage" | PIV and $V_{BR}$ are different quantities | PIV is a *circuit* quantity, $V_{BR}$ a *device* rating, and a diode is chosen so that $\mathrm{PIV} < V_{BR}$. The same conflation is flagged substantively at ·J p35 as **JV4.4** |

---

## J6 — Bipolar Junction Transistors

·J p57–p83, 27 pages. **Thirteen substantive flags, sixteen cosmetic** — the longest range in the
course and the one with the most flags, but the *lowest* substantive density outside J2. Nine of the
thirteen are single wrong symbols in otherwise correct equations, and in almost every case the same
page carries its own correction. ·J p58 carries two opaque redaction blocks. **No genuine
disagreement on the physics was found between this range and ·L3.**

### Substantive

#### JV6.1 · Moderate collector doping credited with reducing dissipation ·J p58

**Printed:** *"Moderate doping also reduced the amount of power dissipated."*

**Should read:** it is the **large cross-sectional area** $A$, not the moderate doping, that lowers
$R$ and therefore $P = I_C^{2}R$.

**Why.** Read the page's own two formulas together: lighter doping means fewer carriers, hence
**larger** $\rho$, hence — at fixed $L$ and $A$ — **larger** $R$ and larger $I_C^{2}R$. Moderate
doping *increases* dissipation for a given current. The real reason collectors are moderately doped
is different: a lightly doped collector lets the collector–base depletion layer spread into the
collector, **raising the reverse breakdown voltage** of that junction.

#### JV6.2 · Output resistance equated to $h_{OB}$, an admittance ·J p60, p61

**Printed:** *"Output resistance $= \dfrac{V_{CB}}{I_C} = h_{OB}$."*

**Should read:**
$$\boxed{\;h_{OB} = \frac{I_C}{V_{CB}}\ [\mathrm{S}],\qquad \text{output resistance} = \frac{V_{CB}}{I_C} = \frac{1}{h_{OB}}\;}$$

**Why.** In the hybrid set $h_o$ is the **output admittance**, in siemens; $V/I$ is a resistance in
ohms, and the two cannot be equal. **The same document gets the CE version right two pages later** —
·J p62 prints $h_{OE} = I_C/V_{CE} = 1/r_o$, current over voltage, which is the correct shape.

#### JV6.3 · The common-emitter input power written with $I_E$ ·J p61

**Printed:** *"Input power $= I_EV_{BE}$."*

**Should read:**
$$\boxed{\;\text{CE input power} = I_BV_{BE}\;}$$

**Why.** **The page states two lines above that the CE input current is $I_B$**, and power at a port
is (port current) × (port voltage). The $I_EV_{BE}$ form is the **common-base** entry from ·J p60,
carried over unchanged. With $\beta = 50$ it overstates the input power — and so understates the
power gain — by a factor of 51.

#### JV6.4 · The common-collector output resistance written with $I_C$ ·J p62

**Printed:** *"Output resistance $= \dfrac{V_{CE}}{I_C}$."*

**Should read:**
$$\boxed{\;\text{CC output resistance} = \frac{V_{CE}}{I_E}\;}$$

**Why.** **The same column of the same table names the CC output current as $I_E$**, and the output
power on the line below is written $I_EV_{CE}$. A port's resistance must use that port's own current.
Since $I_E = I_C/\alpha$ the printed version overstates it by $1/\alpha \approx 1.02$ — small
numerically, wrong in principle, and it breaks the pattern the CB and CE tables follow.

#### JV6.5 · The common-collector gain chain opened with $I_E/I_C$ ·J p62

**Printed:**
$$\theta = \frac{I_E}{I_C} = \frac{I_E}{I_C}\times\frac{I_C}{I_B} = \frac{\beta}{\alpha} = \ldots = 1+\beta$$

**Should read:**
$$\boxed{\;\theta = \frac{I_E}{I_B} = \frac{I_E}{I_C}\times\frac{I_C}{I_B} = \frac{\beta}{\alpha} = 1+\beta\;}$$

**Why, three checks.** (i) Two lines above, the page defines the CC current gain as $I_E/I_B$.
(ii) The product on the right cancels to $I_E/I_B$, not to $I_E/I_C$. (iii) Numerically
$I_E/I_C = 1/\alpha \approx 1.02$, against the line's own answer $1+\beta \approx 51$ — a factor of
50 apart. **Only the leading symbol is wrong; everything after it is right.**

#### JV6.6 · An $\alpha$ lost from the middle step of the $I_C$ derivation ·J p63

**Printed:** $I_C - \alpha I_C = I_B + I_{CBO}$

**Should read:**
$$\boxed{\;I_C - \alpha I_C = \alpha I_B + I_{CBO}\;}$$

**Why.** Expand the line above: $I_C = \alpha I_C + \alpha I_B + I_{CBO}$, so the $I_B$ term carries
an $\alpha$ — and **the page's own next line restores it**,
$I_C = \frac{\alpha}{1-\alpha}I_B + \frac{1}{1-\alpha}I_{CBO}$. The printed step contradicts both its
neighbours. A student reproducing it gets $I_C = (1+\beta)I_B$ instead of $\beta I_B$.

#### JV6.7 · The $(1+\beta)$ applied twice to the leakage term ·J p64

**Printed:** $I_E = (1+\beta)I_B + I_{CEO} = (1+\beta)I_B + \dfrac{1}{1-\alpha}I_{CEO}$

**Should read:**
$$\boxed{\;I_E = (1+\beta)I_B + I_{CEO},\qquad\text{with}\qquad I_{CEO} = \frac{1}{1-\alpha}\,I_{CBO}\;}$$

**Why.** The factor $1/(1-\alpha) = 1+\beta$ is what converts $I_{CBO}$ **into** $I_{CEO}$; applying
it a second time to $I_{CEO}$ multiplies the leakage by $(1+\beta)$ twice over. **The two halves of
the printed equality differ by a factor of 51** for $\beta = 50$. The first half is correct.

#### JV6.8 · Silicon and germanium doubling temperatures printed both ways round ·J p64

**Printed:** half a page apart on one page — *"$I_{CBO}$ doubles for every **10 °C** rise for
**germanium** and **6 °C** for **silicon**"*, then, under *Thermal Runaway*, *"Si = **10 °C** …
Ge = **6 °C**"*.

**Should read:**
$$\boxed{\;\text{Ge: doubles per }10\ ^\circ\mathrm{C};\qquad \text{Si: doubles per }6\ ^\circ\mathrm{C}\;}$$

**Why.** The first of the two statements is the standard one and the one used elsewhere in this
knowledge base — `11-diodes.md` works an exam problem on the explicit assumption that a germanium
diode's reverse saturation current doubles every 10 °C. Silicon's larger band gap makes its
saturation current a **steeper** function of temperature in relative terms, so silicon doubles in
**fewer** degrees, not more. Use $2^{\Delta T/T_2}$ with whichever interval $T_2$ a question supplies.

#### JV6.9 · $V_{EE}$ on the wrong side of the collector loop ·J p73

**Printed:** $V_{CC} = I_CR_C + V_{CE} + I_ER_E + V_{EE}$

**Should read:**
$$\boxed{\;V_{CC} + V_{EE} = I_CR_C + V_{CE} + I_ER_E\;}$$

**Why.** Walk the collector loop from $+V_{CC}$ down to $-V_{EE}$: the total voltage traversed is
$V_{CC}-(-V_{EE}) = V_{CC}+V_{EE}$, dropped across $R_C$, the transistor and $R_E$. **The page's own
base-loop equation on the line above uses $V_{EE}$ as a positive magnitude** and is correct, so the
two as printed cannot both hold. With $V_{CC} = V_{EE} = 10$ V, $R_C = R_E = 2$ kΩ and
$I_C \cong I_E = 4$ mA, the printed form gives $V_{CE} = -6$ V against the correct $+4$ V.

#### JV6.10 · The wrong sign on $I_BR_B$ in the collector-to-base equation ·J p73

**Printed:** $V_{CC} = I_CR_C + I_BR_B + V_{CB}$

**Should read:**
$$\boxed{\;V_{CC} = I_CR_C + V_{CB} - I_BR_B\;}$$

**Why.** The base current flows from ground **through $R_B$ into the base**, so the base sits below
ground at $V_B = -I_BR_B$; then $V_{CB} = (V_{CC}-I_CR_C) + I_BR_B$, which rearranges to the boxed
form. **The check that settles it:** the corrected pair must satisfy $V_{CB} = V_{CE}-V_{BE}$, and
subtracting the base loop from the corrected collector loop returns exactly the boxed equation. The
printed version does not.

#### JV6.11 · $V_{BB}$ and $I_BR_B$ both reversed in sign ·J p74

**Printed:** $V_{CC} = I_CR_C + V_{CB} + I_BR_B - V_{BB}$

**Should read:**
$$\boxed{\;V_{CC} = I_CR_C + V_{CB} + V_{BB} - I_BR_B\;}$$

**Why.** In the Thevenised circuit $V_B = V_{BB}-I_BR_B$ and $V_C = V_{CC}-I_CR_C$; subtracting gives
$V_{CB} = V_{CC}-I_CR_C-V_{BB}+I_BR_B$, which rearranges to the boxed form. **Numerical check:** with
$V_{CC} = 10$ V, $I_CR_C = 3$ V, $V_{BB} = 1.8$ V and $I_BR_B = 0.02$ V, the base sits at 1.78 V and
the collector at 7 V, so $V_{CB} = 5.22$ V. The corrected equation returns
$3+5.22+1.8-0.02 = 10.0$ V ✓; the printed one returns $3+5.22+0.02-1.8 = 6.44$ V ✗.

#### JV6.12 · Each divider resistor assigned its own junction to bias ·J p75

**Printed:** *"$R_{B1}$ is used to reverse bias the collector-base junction and $R_{B2}$ is use to
forward bias the base-emitter junction."*

**Should read:** $R_{B1}$ and $R_{B2}$ **together** set one thing, the base voltage
$V_B = V_{CC}R_{B2}/(R_{B1}+R_{B2})$. The **base–emitter** junction is forward biased because $V_B$
exceeds $V_E$ by $V_{BE}$; the **collector–base** junction is reverse biased because
$V_C = V_{CC}-I_CR_C$ is held above $V_B$ by $V_{CC}$ acting through $R_C$.

**Why it is backwards, not merely loose:** raising $R_{B1}$'s pull-up raises $V_B$ and therefore
**reduces** the collector–base reverse bias. Neither resistor can be assigned to one junction; the
divider is a single two-resistor network with a single output.

#### JV6.13 · An open $R_{B2}$ said to turn the transistor off ·J p80

**Printed:** *"If $R_{B2} = \infty$ then the transistor is off."*

**Should read:** with $R_{B2}$ open the stage reverts to **base bias** with $R_B = R_{B1}$,
$$I_B = \frac{V_{CC}-V_{BE}}{R_{B1}+(1+\beta)R_E}$$
which is normally far more base current than the divider supplied — **driving the transistor into
saturation**. It is **$R_{B1}$ open** that removes the base drive and turns the transistor off.

**Numerical check** with this range's own divider values ($V_{CC} = 20$ V, $R_{B1} = 47$ kΩ,
$R_{B2} = 10$ kΩ, $R_E = 2$ kΩ, $\beta = 200$): normally $I_C = 1.37$ mA; with $R_{B2}$ open,
$I_B = 19.3/(47+402) = 43\ \mathrm{\mu A}$ and $\beta I_B = 8.6$ mA, far above
$I_{C(sat)} = 3.77$ mA.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC6.1** | p57→p58 | the sentence across the page break repeats "reduce the base current" | one clause of the form "…by minimising recombination, which increases the collector current and reduces the base current" | a line has been lost or duplicated at the break; the physics is not in doubt |
| **JC6.2** | p58 | $I_B$ **(5 %)** and, one line later, the collector share **"(95 % /98 %)"** | read the pair as $(\alpha,\ 1-\alpha)$: either $(95,5)$ or $(98,2)$, never a mixture | $5+95 = 100$ ✓ but $5+98 = 103$ ✗; ·J p59 and ·J p60 both give 95/5 |
| **JC6.3** | p59 | the **PNP** operation block diagram drawn **N \| P \| N** | **P \| N \| P** | copied from the NPN page opposite; the construction diagram directly above it on the same page reads P–N–P correctly |
| **JC6.4** | p61 | the h-parameter table's **column headings are absent**, and the "Hybrid" row prints $h_{IB}$ **twice** | columns are ac / dc / total instantaneous; the total-instantaneous entry is $h_{iB}$ | every other row already follows the case convention, which fixes the missing headings with certainty |
| **JC6.5** | p65 | "Admittance $= I_E/V_{BE}$", beside a figure drawing a **slope triangle** | $\dfrac{\Delta I_E}{\Delta V_{BE}}\Big\rvert_{V_{CB}} = \dfrac{1}{h_{ib}}$ | the characteristic is strongly non-linear, so the ratio at a point and the slope at that point are different numbers; ·J p67 uses the $\Delta$ form correctly |
| **JC6.6** | p66 | "Avalacnhe Breakdown" | Avalanche | letters transposed in a figure label |
| **JC6.7** | p66 | CE test circuit labels the collector supply $V_{EE}$ and the output voltmeter $V_{CB}$ | $V_{CC}$ and $V_{CE}$ | the same circuit also shows $V_{CC}$ correctly at the far right; the measurement procedure in the text is right and only the labels are wrong |
| **JC6.8** | p67 | **all five** CE output curves labelled $I_B = 40\ \mathrm{\mu A}$ | a ladder — conventionally 10, 20, 30, 40, 50 µA | curves of equal $I_B$ would coincide, and ·J p77 draws the same family correctly; as printed the figure cannot be used to read $\beta = \Delta I_C/\Delta I_B$, which is its purpose |
| **JC6.9** | p68 | CC test circuit labels the output voltmeter $V_{CB}$ and the supply $V_{EE}$ | $V_{CE}$ and $V_{CC}$ | the CC output port is collector-to-emitter; $V_{CB}$ is the CC *input* voltage, as the page's own table on ·J p62 says |
| **JC6.10** | p69 | CC output figure's vertical axis labelled $I_C$ | $I_E$ (mA) | the text under the figure says the plot is $I_E$ against $V_{CE}$; nothing quantitative changes because $I_E \cong I_C$, but the axis contradicts the caption |
| **JC6.11** | p72 | $I_{sat} = \frac{V_{CC}}{R_C+R_E}\left(\frac{\beta}{1+\beta}\right) = \frac{V_{CC}}{R_C+R_E}$ | the second equals sign must be $\cong$ | $\beta/(1+\beta) = \alpha \approx 0.98$, not 1; the error is 1–5 % and every later use in this range takes the approximation deliberately |
| **JC6.12** | p73 | the voltage-divider figure's bottom rail carries **both** a ground symbol and a $-V_{EE}$ label | ground only | carried over from the two-supply figure directly above it; single-supply operation is the whole selling point of the circuit, and every subsequent figure draws it that way |
| **JC6.13** | p78 | "When $I_C$ is increasing from the Q-point, **$V_{CC}$** is decreasing" | $V_{CE}$ | $V_{CC}$ is the fixed supply and by definition the $V_{CE}$-axis intercept of the load line — it cannot move |
| **JC6.14** | p80 | "thermal **runway**" | thermal runaway | one letter |
| **JC6.15** | p82 | the page's first line clipped by the page top; and $R_{B2} = 1.\dfrac{9}{0.4\times10^{-3}}$ | $R_{B1}+R_{B2} = 9/(0.4\times10^{-3}) = 22.5\ \mathrm{k\Omega}$; and $1.9/(0.4\times10^{-3}) = 4.75\ \mathrm{k\Omega}$ | ⚠ ILLEGIBLE for the first — recovered with certainty because the next equation subtracts 4.75 from it to get 17.75. In the second, the "9" of "1.9" has fallen into the numerator |
| **JC6.16** | p83 | $S = 7.537$ | $S \cong 7.54$ | recomputes to 7.5393 with the page's rounded $\beta = 66$ and 7.5355 with the unrounded $\beta = 65.667$ — 7.537 matches neither. Nothing downstream depends on the third decimal |

---

## J7 — Field Effect Transistors

·J p84–p100, 17 pages. **Ten substantive flags, nine cosmetic** — the fewest cosmetic flags in the
course, because this range is transcribed closely from a clean printed chapter. That closeness is
itself the finding: **·J p95, ·J p96–p97 and ·J p97 are the textbook's Examples 63.2, 63.10 and
63.11**, circuit for circuit and number for number, so agreement with ·L4 here is **not** independent
confirmation. Three pages, ·J p87, p88 and p89, carry opaque redaction blocks, and ·J p100 ends
mid-topic with no summary, no problem set and no reference list.

### Substantive

#### JV7.1 · $V_P$ used with two opposite signs ·J p85, p86, p87

**Printed:** ·J p85 defines $V_P$ as *"the corresponding value of $V_{DS}$"* at pinch-off, and ·J p86
ticks $V_P$ on the **horizontal $V_{DS}$ axis** — a **positive** voltage. ·J p87 then prints
Shockley's equation with $V_P$ **and** with $V_{GS(\text{off})}$ in the denominator of the same
expression, asserting $V_P = V_{GS(\text{off})}$ — a **negative** voltage for N-channel.

**Should read:** the denominator is the cut-off voltage,
$$\boxed{\;I_D = I_{DSS}\left(1-\frac{V_{GS}}{V_{GS(\text{off})}}\right)^{2}\;}$$
with $\lvert V_P\rvert = \lvert V_{GS(\text{off})}\rvert$ and $V_{GS(\text{off})} = -\lvert V_P\rvert$.

**Why.** Both cannot hold. Substituting a positive $V_P$ for a negative $V_{GS}$ gives
$I_D > I_{DSS}$, which is physically impossible. **·L4 carries the identical contradiction
(`V4.2`) — see the cross-tier section; this is one defect found twice, not two sources agreeing.**

#### JV7.2 · The enhancement-only MOSFET illustrated with the DE MOSFET figure ·J p91

**Printed:** the static-characteristic figure of ·J p89 — the depletion-enhancement MOSFET —
**reproduced unchanged**, complete with $I_{DSS}$, a $V_{GS} = 0$ curve carrying current, a
$V_{GS} = -2\ \mathrm{V}$ curve and a labelled $V_{GS(\text{off})}$.

**Should read:** a family of $I_D$–$V_{DS}$ curves labelled with **positive** $V_{GS}$ values, all
above $V_{GS(\text{th})}$; any curve for $V_{GS} \le V_{GS(\text{th})}$ **lies on the axis**; the
saturation boundary is $V_{DS} = V_{GS}-V_{GS(\text{th})}$; **nothing labelled $I_{DSS}$ appears**.

**Why.** An enhancement-only MOSFET **has no channel at $V_{GS} = 0$**, so it has no $I_{DSS}$ and no
depletion mode at all. **The figure contradicts the same page's own equation**
$I_D = K(V_{GS}-V_{GS(\text{th})})^2$, which is zero for every $V_{GS} \le V_{GS(\text{th})}$. The
correct **transfer** characteristic is on the next page (·J p92) and is drawn properly — learn the
equation from ·J p91 and the figure from ·J p92.

#### JV7.3 · The JFET operating narrative reprinted under the E-only MOSFET figure ·J p91

**Printed:** the six bullets of ·J p85, **verbatim** — that "the depletion regions penetrate more
deeply into the channel at points which lie closer to the drain", that $I_D = V_{DS}/R_{DS}$, that
"$I_D$ increases up to a maximum value $I_{DSS}$", and that "at this stage $I_D = I_{DSS}$".

**Should read:** $I_D$ is **zero** until $V_{GS}$ exceeds $V_{GS(\text{th})}$; above threshold an
inversion layer forms, and once $V_{DS} \ge V_{GS}-V_{GS(\text{th})}$ the device saturates at
$$\boxed{\;I_D = K\left(V_{GS}-V_{GS(\text{th})}\right)^{2}\;}$$
Below that $V_{DS}$ it is in the **ohmic** region.

**Why.** **None of the printed narrative describes an enhancement-only MOSFET.** There are no gate
depletion regions — the gate is insulated and the channel is *created*, not depleted — and there is
no $I_{DSS}$, since $I_D = 0$ at $V_{GS} = 0$ by construction. Paired with `JV7.2`, the whole page is
about the previous device.

#### JV7.4 · The drain-feedback bias printed with a minus sign ·J p96

**Printed:** $V_{GS} = -V_{DS}$

**Should read:**
$$\boxed{\;V_{GS} = V_{DS} = V_{DD}-I_DR_D\;}$$

**Why.** With $I_G \approx 0$ there is **no drop across $R_G$**, so the gate sits at exactly the drain
potential: $V_G = V_D$, $V_S = 0$, $V_{GS} = V_D = V_{DS}$. **The page's own next line says
$V_D = V_{DS}$, and its own bullet says "the gate voltage is made more +ve than the source"** — both
require the positive form. As printed, $V_{GS}$ is negative, which for an N-channel enhancement-only
MOSFET means $V_{GS} < V_{GS(\text{th})}$ and the device is **cut off**: the circuit could not work.

#### JV7.5 · A kilohm written as $10^{-3}$ ·J p95

**Printed:** $V_D = 12 - 1.5\times10^{-3}\times4\times10^{-3}$

**Should read:**
$$\boxed{\;V_D = 12 - \left(4\times10^{-3}\right)\left(1.5\times10^{3}\right) = 12-6 = 6\ \mathrm{V}\;}$$

**Why.** $R_D$ is $1.5\ \mathrm{k\Omega}$, i.e. $1.5\times10^{3}$. As printed the product is
$6\times10^{-6}$ and the line evaluates to $11.999994\ \mathrm{V}$, not the 6 V stated. **The stated
answer is right and only the exponent is wrong**; the companion example on the same page prints its
exponents correctly, which is how the slip is identified.

#### JV7.6 · The drain loop written with $R_S$ in an example where $R_S = 0$ ·J p97

**Printed:** $V_{DS} = V_{DD}-I_SR_S$

**Should read:**
$$\boxed{\;V_{DS} = V_{DD}-I_D\left(R_D+R_S\right) = 25 - 16\times10^{-3}\times1\times10^{3} = 9\ \mathrm{V}\;}$$

**Why.** This example has **$R_S = 0$**; the $1\ \mathrm{k\Omega}$ actually substituted is $R_D$.
Followed literally the printed formula gives $V_{DS} = 25-0 = 25$ V. The answer 9 V is right and the
symbol on the resistance is wrong. **·L4 p20 prints $V_{DS} = V_{DD}-I_DR_L$ for the same worked
example.**

#### JV7.7 · The gate-loop equation with the wrong sign for the circuit drawn ·J p93

**Printed:** $V_{GG} = V_{GS}+I_SR_S$, which rearranges to $V_{GS} = V_{GG}-I_SR_S$.

**Should read:**
$$\boxed{\;V_{GS} = -V_{GG}-I_SR_S \qquad (V_{GG} > 0,\ \text{the magnitude of the rail})\;}$$

**Why.** The figure's gate rail is labelled **$-V_{GG}$**, so with $I_G \approx 0$ there is no drop
across $R_G$ and $V_G = -V_{GG}$, $V_S = +I_SR_S$, $V_{GS} = V_G-V_S$. The printed form is
**positive** whenever $I_SR_S < V_{GG}$ — a forward-biased gate on an N-channel JFET, which the
device does not survive. **Note the contrast with source bias on ·J p94, where the identical-looking
equation is correct** because the negative rail is in the *source* branch, not the gate branch. That
is exactly why the two must not be memorised as one formula.

#### JV7.8 · An operating point outside the region its own equation is valid in ·J p96–p97

**Printed:** the worked E-MOSFET example reaches $V_{GS} = 15$ V, $I_D = 16$ mA and $V_{DS} = 9$ V
from $I_D = K(V_{GS}-V_{GS(\text{th})})^2$.

**Should read:** the square law holds **only in saturation**, i.e. only while
$$V_{DS} \ \ge\ V_{GS}-V_{GS(\text{th})}$$
Here $V_{GS}-V_{GS(\text{th})} = 15-5 = 10$ V, and $V_{DS} = 9\ \mathrm{V} < 10\ \mathrm{V}$.

**Why.** The device is in the **ohmic (triode) region**, where the square law **overestimates**
$I_D$; the circuit as specified could not actually deliver 16 mA at 9 V. **The arithmetic in the
notes is internally correct** — 9 V does follow from the numbers given — which is why this is the one
substantive flag in the course that belongs to none of the eleven families. A self-consistent version
needs a larger $V_{DD}$ or a smaller $R_D$: with $R_D = 800\ \Omega$,
$V_{DS} = 25-12.8 = 12.2\ \mathrm{V} > 10\ \mathrm{V}$ ✓. **Answer the question as set — the marks
are for the method — and state the check.**

#### JV7.9 · $I_D$ and $V_{GS}$ each used for two different things in one problem ·J p96

**Printed:** the data *"$I_D = 4\ \mathrm{mA}$, $V_{GS} = 10\ \mathrm{V}$"*, which the solution
substitutes into $K = I_D/(V_{GS}-V_{GS(\text{th})})^2$.

**Should read:**
$$\boxed{\;I_{D(\mathrm{ON})} = 4\ \mathrm{mA}\ \text{ at }\ V_{GS(\mathrm{ON})} = 10\ \mathrm{V}\;}$$

**Why.** Those are the **data-sheet ON point** of the device; the $V_{GS}$ the question asks for is
the **circuit's** bias, which comes out at 15 V, with $I_D = 16$ mA beside it. A reader who takes the
given $V_{GS} = 10$ V as the operating point gets $I_D = 4$ mA and $V_{DS} = 21$ V — a completely
different answer. **·L4 p19 labels the same pair $I_{D(\mathrm{ON})}$ and distinguishes them.**

#### JV7.10 · A threshold voltage labelled as a cut-off voltage ·J p97

**Printed:** the exercise gives the 5 V parameter as $V_{GS(\text{off})}$.

**Should read:**
$$\boxed{\;V_{GS(\text{th})} = 5\ \mathrm{V}\;}$$

**Why.** They are different quantities belonging to different devices. $V_{GS(\text{off})}$ is the
**negative** voltage at which a JFET or DE MOSFET stops conducting, and it belongs in **Shockley's**
equation; $V_{GS(\text{th})}$ is the **positive** voltage at which an enhancement-only MOSFET starts
conducting, and it belongs in the **$K$** equation. A reader taking the label at face value reaches
for $I_D = I_{DSS}(1-V_{GS}/V_{GS(\text{off})})^2$, for which no $I_{DSS}$ is even given — and **the
printed answer of 1.44 mA is obtained only by reading the 5 V as the threshold.** ·L4 p21 labels it
$V_{GS(\text{th})}$.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **JC7.1** | p87 | the transfer-characteristic figure's held-constant quantity printed "**$V_D$ = constant**" | $V_{DS}$ = constant | a transfer characteristic is taken at constant drain–**source** voltage; $V_D$ elsewhere in this document (·J p93–p95) is the drain **node potential**, a different quantity |
| **JC7.2** | p90, p92 | "**MOSEFET**", twice, both times in a heading | MOSFET | **m**etal-**o**xide-**s**emiconductor **f**ield **e**ffect **t**ransistor |
| **JC7.3** | p91, p92 | the square-law constant set as capital $K$ in the equation and lower-case k in the sentence beneath, both times | **$K$** | lower-case $k$ is Boltzmann's constant elsewhere in this knowledge base (·J p35) |
| **JC7.4** | p98 | **both** waveforms in the figure labelled "Input signal" | the upper one, drawn against the $I_D$ axis, is the **output** | the ·J p97 figure is identical in construction and labels the same pair correctly |
| **JC7.5** | p99 | common-drain table written with $V_{DG}$ and $V_{DS}$ throughout | $V_{GD}$ and $V_{SD}$, giving $A_v = V_{SD}/V_{GD}$ | with the **drain** common, input is measured gate-to-drain and output source-to-drain. As printed both are measured *from* the drain, which reverses both signs and leaves the ratio unchanged — nothing computed changes, but the $V_{XY} = V_X-V_Y$ convention used everywhere else in ·J is broken |
| **JC7.6** | p97 | the page's top line clipped: $V_{R_2} = \frac{\;\;}{R_1+R_2}\times R_2 = \frac{\;\;}{9+6}\times9 = 15\ \mathrm{V}$ | the numerators are $V_{DD}$ and 25 | ⚠ ILLEGIBLE — **recovered with certainty** from ·J p96's data and from the arithmetic, $25\times9/15 = 15$ exactly |
| **JC7.7** | p88 | "insulated … by an ultra thin **metal oxide** insulating film of silicon dioxide" | "…by an ultra-thin film of silicon dioxide, the oxide layer of the metal-oxide-semiconductor sandwich" | **silicon dioxide is not a metal oxide** — silicon is a metalloid. The "MOS" names the sandwich, not the composition of the oxide |
| **JC7.8** | p84–p100 | word cluster: "an N-channel **JEET**"; "$V_{GS}$ is **increased to the -ve**"; "**VGS**"; "is **a like** a switch"; "**N-types material**"; "the **+ve gates** only"; "The **switching consideration**"; "**Voltage variables resistors**" | JFET; made **more negative**; $V_{GS}$; is **like**; N-type material; +ve **gate**; switching **characteristics**; voltage-**variable** resistors | "increased" and "-ve" pull opposite ways; the MOSFET purchase list on the same page uses "characteristics" correctly |
| **JC7.9** | p99 | the common-drain supply rail labelled **$V_{SS}$** | $V_{DD}$ | the common-source and common-gate sketches on ·J p98–p99 both use $V_{DD}$, and $V_{SS}$ already means the negative source-bias supply (·J p94) and **SS** the substrate terminal (·J p88, p90). **Three meanings for the same letters inside seventeen pages** — also in `_nomenclature.md` |

---

# Part B — Tier 2: the lesson documents (`·L1`–`·L7`)

**Seven lesson handouts, 169 pages, compiled from a printed textbook.** 96 substantive flags and 133
cosmetic. Citations are of the form **·L3 p14** — page 14 of Lesson 3, counted as PDF pages.

**What this source is like.** It is a scan-and-retype compilation of textbook chapters, so its
*prose* is largely sound and its defects are overwhelmingly **rendering** faults: lost unit prefixes,
lost exponents, Greek letters substituted by Latin ones, article and figure numbers missing their
leading digit. That is the mirror image of the lecture notes, and it is why the two sources correct
each other so effectively — see **Cross-tier resolutions** above.

The entries below are unchanged from the single-tier edition of this log; only the heading placing
them under Part B is new.

## L1 — Semiconductor Diodes

18 pages. Six substantive flags, eleven cosmetic. Two of the six (`V1.2`, `V1.3`) attack the diode
equation itself, which makes this lesson's error density more serious than its count suggests.

### Substantive

#### V1.1 · The depletion layer given only one sign of ion ·L1 p2

**Printed:** *"there being present only **positive ions** which are not free to move."*

**Should read:** the depletion layer holds **both** signs of fixed ion —
$$\text{fixed } \ominus \text{ acceptor ions on the P side} \;+\; \text{fixed } \oplus \text{ donor ions on the N side}$$

**Why.** The page's own Fig. 51.33(b) draws $\ominus$ on the P side and $\oplus$ on the N side, and
p3 states both rows explicitly. With one sign only there is no charge separation, hence no barrier
potential and no diode.

#### V1.2 · The master diode equation printed without its ideality factor ·L1 p6

**Printed:** $I = I_0\left(e^{\,eV/kT}-1\right)$, highlighted as the general form.

**Should read:**
$$\boxed{\;I = I_0\left(e^{\,eV/\eta kT}-1\right) = I_0\left(e^{\,V/\eta V_T}-1\right)\;}$$

**Why.** $\eta$ is defined three lines below the box and appears in every subsequent form on p6 and
p7. For **silicon** ($\eta = 2$) the printed box doubles the exponent: at $V = 0.2$ V and
$V_T = 25$ mV it gives $e^{8} = 2981$ against the correct $e^{4} = 54.6$ — a factor of **55**.

#### V1.3 · The $-1$ printed inside the exponent, five times ·L1 p7, p8

**Printed:** all four highlighted forms on p7 — $I_0(e^{40V-1})$, $I_0(e^{20V-1})$,
$I_0(e^{V_f/\eta V_T-1})$, $I_0(e^{V_R/\eta V_T-1})$ — and again at the top of Example 52.2 on p8,
$I = I_0\exp(eV/kT-1)$.

**Should read:**
$$\boxed{\;I = I_0\left(e^{\,V/\eta V_T}-1\right)\;}$$

**Why.** Three independent disproofs, any one sufficient. (i) At $V = 0$ the printed form gives
$I = I_0e^{-1} = 0.368\,I_0$ — an unbiased diode passing a third of its saturation current.
(ii) The next line's approximation $I_0(e^{40V}-1)\cong I_0e^{40V}$ only holds with the $-1$
outside. (iii) Example 52.7 on p18 prints the same equation **correctly**.

#### V1.4 · $kT/e$ at 398 K, and the answer that follows from it ·L1 p8

**Printed:** $kT/e = 36$ mV at 398 K, and a final barrier voltage of **0.5 V**.

**Should read:**
$$\frac{kT}{e}\bigg|_{398\ \mathrm{K}} = \frac{1.38\times10^{-23}\times398}{1.6\times10^{-19}} = 34.33\ \mathrm{mV}
\quad\Longrightarrow\quad \boxed{\;V_B = 34.33\times\ln(10^{6}+1) = 0.474\ \mathrm{V}\;}$$

**Why.** $kT/e$ is **linear in $T$**, and the same page has just computed 26 mV at 300 K — so the
398 K value must be $26\times398/300 = 34.5$ mV. No calculator is needed to reject 36 mV. The
printed 0.5 V is about 5 % high.

#### V1.5 · A sign lost from an exponent, in the numerator only ·L1 p18

**Printed:** $I_0 = \dfrac{40\times10^{\mathbf{3}}}{e^{10}-1}$

**Should read:**
$$\boxed{\;I_0 = \frac{40\times10^{-3}}{e^{10}-1} = \frac{0.04}{22{,}025.5} = 1.82\ \mu\mathrm{A}\;}$$

**Why.** The line immediately above prints $40\times10^{-3}$ correctly. As printed the expression
evaluates to **1.816 A**, a factor $10^{6}$ from the page's own (correct) stated answer and
dimensionally absurd for a saturation current. The correct final answer is what makes this easy to
copy into a CAT unnoticed.

#### V1.6 · LED light output called directly proportional to forward current ·L1 p14

**Printed:** *"The amount of power output translated into light is **directly proportional** to the
forward current as shown in Fig. 53.3(b)."*

**Should read:** light output rises **monotonically but sub-linearly** with $I_F$, saturating at
high current.

**Why.** Proportionality requires that doubling $I_F$ from 50 mA to 100 mA doubles the output,
1.8 mW → 3.6 mW; the figure the sentence points at reads ≈2.8 mW and is visibly concave-down. The
next sentence — *"greater the forward current, the greater the light output"* — is the correct,
weaker claim.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C1.1** | p3, p6, p8, p18 | "300°K", "293°K", "398°K", "343°K"; Boltzmann's constant in "J/°K" | $300\ \mathrm{K}$; $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ | the kelvin takes no degree sign |
| **C1.2** | p4, p10, p18 | "Art. 1.40", "Art 4.1", "Art. 1.38" | Art. 51.40 (p3), Art. 54.1 (p9), Art. 51.40 (p3) | the leading 5 has dropped from all three; the cited articles do not exist |
| **C1.3** | p4 | $V_B = 26\log_e(N_aN_d/n^{2})$ | $n_i^{2}$ | $n$ alone is the free-electron concentration, a different quantity; the two later lines restore $n_i^2$ |
| **C1.4** | p4, p8, p11, p15 | "Difusion Currents"; "perferred"; "This increases in I"; "againt"; "To chose"; "Each of this segments" | Diffusion; preferred; increase; again; choose; these | spelling cluster; nothing computed changes |
| **C1.5** | p6 | reverse-current axis of Fig. 52.4 labelled "**200 A**" | $200\ \mu\mathrm{A}$ | the µ prefix has dropped; the same page's text requires microamperes for Ge |
| **C1.6** | p8 | "$1.38\times10^{-23}\times398\times(1.6\times10^{-19})$"; result written "$36\,\mathbf{In}(\ldots)$" | division by $e$, not multiplication; $\ln$, not "In" | as printed the product is $8.8\times10^{-40}$, not a voltage; the 300 K line above uses "/" correctly |
| **C1.7** | p10–p11 | Example 54.4's solution opens with **no question above it**; numbering jumps 54.3 → 54.5 | the question statement is missing from the compilation | reconstructable ($E_o$ in Fig. 54.6 for $E_{in} = 6$ V and 20 V) but not followable as printed |
| **C1.8** | p10 | "IN 750", "IN 4000" | **1N750**, **1N4000**-series | the JEDEC prefix is the digit one, not the letter I; read as I the part is unsearchable. *Unverified against a datasheet: the standard 1N750 is a 4.7 V, ~0.5 W device, consistent with the 4.7 V quoted but not with the bracketed "(10 W power)"* |
| **C1.9** | p11 | the first line of §54.2 and the "Fig. 54.6" caption each printed **twice, overlapping** | one copy | compilation artefact — retyped text laid over the scan |
| **C1.10** | p3, p16 | the two-chip cut-away picture placed on p3, beside the barrier-voltage text | it belongs with the multicoloured-LED discussion, where it reappears on p16 | nothing on p3 refers to it |
| **C1.11** | p16 | "a three-terminal device as shown in **Fig. 3.5**" | Fig. **53**.5, on the same page | the leading 5 has dropped, exactly as in `C1.2` |

---

## L2 — Rectification and Power Supplies

26 pages, 43 flags — the highest count in the course and the lesson with the most arithmetic. Nine
of the eighteen substantive faults are lost multiplicative constants ($\pi$, $\sqrt2$, a factor 2),
and in most of those **the final answer printed on the page is correct**, which is precisely what
makes them easy to copy.

### Substantive

#### V2.1 · The supply waveform printed without its sine ·L2 p2

**Printed:** $V_s = V_{sm}\,wt$

**Should read:**
$$\boxed{\;v_s = V_{sm}\sin\omega t\;}$$

**Why.** Two defects in one line: the $\sin$ is missing and $\omega$ is set as a roman "w". As
printed the right-hand side has units of volt-radians and grows without bound, so it cannot be a
supply voltage.

#### V2.2 · A rectifier efficiency of 409.6 % ·L2 p4

**Printed:** $\eta = \dfrac{0.406}{1+R_0/R_L} = \dfrac{409.6\,\%}{(1+R_0/R_L)}$

**Should read:**
$$\boxed{\;\eta = \frac{4}{\pi^{2}}\cdot\frac{R_L}{R_L+R_0} = \frac{40.5\,\%}{1+R_0/R_L}\;}$$

**Why.** A rectifier cannot deliver ten times the power put into it, and the preceding expression
$0.406$ **is** 40.6 %, not 409.6 % — a stray digit. Recomputed: $4/\pi^2 = 0.405285$.

#### V2.3 · A $\sqrt2$ lost from the second-harmonic rms ·L2 p4

**Printed:** $I_{L2} = \text{peak}/\sqrt2 = \dfrac{2I_{LM}}{3\pi\sqrt2} = \dfrac{I_{LM}}{3\pi}$

**Should read:**
$$\boxed{\;I_{L2} = \frac{2I_{LM}}{3\pi\sqrt2} = \frac{\sqrt2\,I_{LM}}{3\pi} = 0.1501\,I_{LM}\;}$$

**Why.** $2/\sqrt2 = \sqrt2$, not 1 — the middle expression is right and the final one has lost the
factor. Two confirmations: the next page prints the voltage version correctly as
$V_{L2} = \sqrt2 V_{LM}/3\pi$; and the page's own total $I_{L(ac)} = 0.385I_{LM}$ only comes out
with the $\sqrt2$ present ($\sqrt{0.125+0.022516+0.000901} = 0.38525$ ✓ against $0.3702$ ✗). The
printed value is **29 % low**.

#### V2.4 · A factor 2 lost from the fundamental ·L2 p5

**Printed:** $V_{L1} = V_{LM}/\sqrt2$

**Should read:**
$$\boxed{\;V_{L1} = \frac{V_{LM}}{2\sqrt2} = 0.354\,V_{LM}\;}$$

**Why.** The fundamental's **peak** is $V_{LM}/2$, from the $\tfrac12\sin\omega t$ term of the
series; its rms is that divided by $\sqrt2$. The same page prints the current version correctly as
$I_{L1} = I_{LM}/2\sqrt2$, and $0.707V_{LM}$ would on its own exceed the whole rms output
$V_L = 0.5V_{LM}$ — impossible for one harmonic.

#### V2.5 · The ripple factor written over itself ·L2 p5

**Printed:** $\gamma = \dfrac{I_{L(ac)}}{I_{L(ac)}} = \dfrac{\sqrt{I_L^2-I_{L(dc)}^2}}{I_{L(dc)}}$

**Should read:**
$$\boxed{\;\gamma = \frac{I_{L(ac)}}{I_{L(dc)}}\;}$$

**Why.** The first fraction has the **same symbol above and below the line** and is therefore
identically 1, contradicting the expression immediately to its right. The self-reference test
catches it without any physics.

#### V2.6 · Ripple factor divided by an rms value instead of a dc value ·L2 p5, p9

**Printed:** $\gamma = \dfrac{V_{L(ac)}}{V_{L(dc)}} = \dfrac{V_{r(ms)}}{V_{L(ms)}}$

**Should read:**
$$\boxed{\;\gamma = \frac{V_{L(ac)}}{V_{L(dc)}} = \frac{V_{r(rms)}}{V_{L(dc)}}\;}$$

**Why.** The two fractions on one line disagree with each other: the first divides by a dc value,
the second by an rms value. Dividing by the total rms would cap $\gamma$ at 1 and make it
meaningless for the half-wave case, where the true answer is **1.21**. p10 prints it correctly,
which settles which form is intended. ("(ms)" is itself a dropped-r rendering of "(rms)".)

#### V2.7 · The half-wave TUF derivation loses a factor $\pi$ twice ·L2 p6

**Printed:**
$$P_{dc}=\frac{V_{LM}}{\pi}\cdot\frac{V_{LM}}{R_L}=\frac{V_{LM}^{2}}{\pi R_L}
\qquad\text{then}\qquad
\mathrm{TUF}=\frac{V_{sm}^2/\pi R_L}{V_{sm}^2/2\sqrt2 R_L}=\frac{2\sqrt2}{\pi}=0.287$$

**Should read:**
$$\boxed{\;P_{dc}=\frac{V_{LM}^{2}}{\pi^{2}R_L}\;}\qquad
\boxed{\;\mathrm{TUF}_{\text{HW}}=\frac{2\sqrt2}{\pi^{2}}=0.2866\;}$$

**Why.** (i) $V_{LM}/R_L$ is $I_{LM}$, not $I_{L(dc)}$ — the dc current is $V_{LM}/\pi R_L$.
(ii) $2\sqrt2/\pi = 0.900$, not 0.287; the quoted 0.287 is $2\sqrt2/\pi^2 = 0.28658$, which is
exactly what the corrected $P_{dc}$ gives. **The two slips cancel in the final number**, so the
printed answer certifies a defective derivation.

#### V2.8 · A centre-tap PIV quoted for a half-wave rectifier ·L2 p7

**Printed:** part (iv): PIV $= 2V_{sm} = 2\times31 = 62$ V.

**Should read:**
$$\boxed{\;\mathrm{PIV} = V_{sm} = 31\ \mathrm{V}\;}$$

**Why.** $2V_{sm}$ is the PIV of a **centre-tapped full-wave** rectifier, where the idle diode sees
both half-secondaries in series. In a half-wave rectifier only one secondary winding stands across
the reverse-biased diode — and **p5 of this same handout states PIV $=V_{sm}$**.

#### V2.9 · Fig. 55.6(a) shows the wrong circuit ·L2 p7, p11

**Printed:** Art. 55.7 announces *"the full-wave rectifier circuit using **two diodes and a
centre-tapped transformer** shown in 55.6(a)"*; the figure under that label is a **four-diode
bridge** — a diamond of $D_1$–$D_4$ between nodes E, A, F, C, with the secondary M–N feeding E and F
and the load between A and C, its waveform panels captioned "Output of $D_1$ & $D_3$" and "Output of
$D_2$ & $D_4$".

**Should read:** that bridge belongs to Art. 55.8, whose own figure (Fig. 55.10) is **missing** from
the handout. The genuine centre-tapped circuit appears one figure later, as **Fig. 55.7**.

**Why it matters.** A reader working from Fig. 55.6(a) draws a bridge when asked for a centre-tap
rectifier, and then gets the PIV wrong — bridge PIV is $V_{sm}$, centre-tap PIV is $2V_{sm}$.

#### V2.10 · Total series resistance where the load resistance belongs ·L2 p8

**Printed:** $P_{dc} = I_{L(dc)}^{2}(R_0+R_L)$

**Should read:**
$$\boxed{\;P_{dc} = I_{L(dc)}^{2}R_L\;}$$

**Why.** $P_{dc}$ is by definition the dc power *delivered to the load*. The next line's result,
$\eta = \frac{8}{\pi^2}\frac{R_L}{R_0+R_L}$, can only be reached that way: with $(R_0+R_L)$ in both
numerator and denominator the ratio collapses to the constant $8/\pi^2$ and the $R_L/(R_0+R_L)$
factor vanishes.

#### V2.11 · A $\pi$ missing from the third ripple term ·L2 p9

**Printed:** $-\dfrac{4}{35}\cos6\omega t$

**Should read:**
$$\boxed{\;-\frac{4}{35\pi}\cos6\omega t\;}$$

**Why.** The general term of the full-wave series is $-\dfrac{4}{\pi(n^2-1)}\cos n\omega t$ for even
$n$, giving $4/3\pi$, $4/15\pi$, $4/35\pi$ — and every other term on the page carries its $\pi$.
As printed the coefficient is $\pi$ times too large: $4/35 = 0.1143$ against $4/35\pi = 0.0364$.

#### V2.12 · A radicand with no real value ·L2 p9

**Printed:** $I_{L(ac)} = \sqrt{0.55^{2}-49.6^{2}} = 0.238\ \mathrm{A}$

**Should read:**
$$\boxed{\;I_{L(ac)} = \sqrt{0.55^{2}-0.496^{2}} = \sqrt{0.0565} = 0.2377\ \mathrm{A}\;}$$

**Why.** The second term is the **voltage** 49.6 V, not the current 0.496 A — the decimal point has
moved two places. As printed the radicand is $-2459.9$, so the expression has no real value at all;
the quoted answer 0.238 A is the one the corrected radicand gives.

#### V2.13 · Peak subscripts on a ripple-factor definition ·L2 p9

**Printed:** $\gamma = I_{L(ac)}/I_{L(dc)} = I_{r(\mathbf{max})}/I_{L(\mathbf{max})}$

**Should read:**
$$\boxed{\;\gamma = \frac{I_{r(rms)}}{I_{L(dc)}}\;}$$

**Why.** Both subscripts are wrong: the numerator is the rms ripple current and the denominator the
dc load current — which is exactly what the numbers 0.238 A and 0.496 A beside them are. Peak values
would give $I_{LM}/I_{LM} = 1$ for every rectifier ever built.

#### V2.14 · A factor 2 lost from the full-wave dc current ·L2 p10

**Printed:** $I_{L(dc)} = \dfrac{I_{LM}}{\pi} = \dfrac{2\times0.414}{\pi} = 0.263\ \mathrm{A}$

**Should read:**
$$\boxed{\;I_{L(dc)} = \frac{2I_{LM}}{\pi} = 0.636\,I_{LM}\;}$$

**Why.** The symbolic form has lost the 2 while the arithmetic beside it keeps it. $I_{LM}/\pi$ is
the **half-wave** result and would give 0.132 A, half the printed answer.

#### V2.15 · A series-clipper output drawn starting at $-10$ V ·L2 p16

**Printed:** Fig. 52.34(c) plots an output that **starts at $-10$ V** at $t = 0$ and rises through
zero to its peak.

**Should read:**
$$\boxed{\;V_o = \max\!\left(v_{in}-10,\ 0\right)\;}$$
— zero from $\omega t = 0$ to $30°$, a hump of peak 10 V from $30°$ to $150°$, zero thereafter.

**Why.** A *series* clipper whose diode is blocking passes no current, so $V_o$ across $R$ must be
exactly zero whenever $v_{in} < 10$ V; the battery cannot drive current, being the element that
reverse-biases the diode. The whole of $v_{in}-10$ appears to have been plotted on the rising flank
while the falling flank was correctly flattened. **Fig. 52.35(c) on the same page is drawn
correctly** for the reversed battery.

#### V2.16 · Clamper diode reverse voltage under-stated by a third — 10 V printed for 15 V ·L2 p19

**Printed:** B going positive *"**reverse-biases D by 10 V**"*.

**Should read:**
$$\boxed{\;V_{R,\text{diode}} = V_C + |V_{in}| = 5+10 = 15\ \mathrm{V}\;}$$

**Why.** The diode has the whole output across it, and p20 derives that output as $5+10 = 15$ V —
the capacitor's stored 5 V adds to the 10 V input. A diode chosen on the printed figure would be
**under-rated by 50 %**.

#### V2.17 · Two different ripple frequencies for one topology ·L2 p21, p23

**Printed:** p21, of the half-wave (cascade) doubler: *"Ripple frequency is equal to the supply
frequency"*. p23, of Fig. 55.34 — which §55.28(a) has just described as *"the half-wave voltage
doubler circuit (Fig. 55.31) extended"* — *"ripple frequency is **twice** the line frequency"*.

**Should read:**
$$\boxed{\;f_{\text{ripple}} = f_{\text{supply}}\ \text{for the cascade (Cockcroft–Walton) multiplier}\;}$$

**Why.** Each output capacitor of a cascade multiplier is refilled once per input cycle. The
"twice" belongs to the **full-wave** doubler of §55.27 on p22, where it is correctly stated.

#### V2.18 · Tunnel-diode negative resistance said to increase from A to B ·L2 p24

**Printed:** *"this resistance **increases as we go from point A to B** because as voltage is
increased, current keeps decreasing which means that diode negative resistance keeps increasing."*

**Should read:**
$$\boxed{\;R_N=-\frac{dV_T}{di_T}\ \text{is least in the middle of AB and unbounded at both ends}\;}$$

**Why.** $R_N$ is a **slope** quantity, and at both A and B the curve is flat ($di_T/dV_T = 0$), so
$R_N$ is infinite at each end and passes through a minimum between them — it is not monotonic. What
does increase monotonically is the static chord ratio $V_T/i_T$, a positive quantity and not the
negative resistance at all. This matters for §54.7(f): the Q-point is placed **near the middle of
AB** precisely because $|R_N|$ is smallest and most nearly constant there.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C2.1** | p2, p10 | eight rectifier circuits promised; **six** delivered — items 6 (six-phase half-wave) and 7 (three-phase bridge) never appear; Figs. 55.5, 55.10, 55.15–55.30 absent; Example 55.2 missing | the promised material is not in the handout | a compilation gap, not a physics error, but Example 55.5 is built entirely on Example 55.2's data |
| **C2.2** | p3 | $V_B$ used in the boxed $I_{LM}$ formula but absent from the "Let" list above it | $V_B$ = the diode barrier (knee) voltage, 0.7 V Si / 0.3 V Ge | missing definition only; the formula is right |
| **C2.3** | p3 | $I_L = I_LM_n/2 = 0.5I_{LM}$ | $I_L = I_{LM}/2$ | the subscript has broken apart and picked up a stray "n"; the rest of the line is correct |
| **C2.4** | p4, p8 | maxima quoted as **40.6 %** and **81.2 %** | exactly $4/\pi^2 = 40.53\,\%$ and $8/\pi^2 = 81.06\,\%$ | rounded up, inherited from the parent textbook. **Use 40.6 / 81.2 in a CAT** — but a question asking for $4/\pi^2$ to three figures wants 0.405 |
| **C2.5** | p4, p8 | "If $R_0$ is neglected **h** = 40.6 %"; "effficiency" | $\eta$; efficiency | the $\eta$ glyph has rendered as a roman h; three-f misspelling beside it |
| **C2.6** | p4 | the fourth term called *"the third harmonic component whose frequency is four times the supply frequency"* | the **fourth** harmonic, on the naming used one sentence earlier | the page has slipped from harmonic-numbering to term-numbering mid-paragraph; the coefficient is right |
| **C2.7** | p5 | $I_{L(ac)}=\sqrt{I_{L1}^2+I_{L2}^2+I_{L3}^3+\cdots}$ | $I_{L3}^{2}$ | the third term carries a cube; the arithmetic that follows uses squares and lands on the correct 0.385 |
| **C2.8** | p6, p9, p10, p22 | "$V_{pm}=220=312$ V"; "$V_{sm}=300=424$ V"; "$V_{dc}=2V_m=2\times\sqrt2=620$ V" | $220\sqrt2$, $300\sqrt2$, $2\times220\sqrt2$ | the $\sqrt2$ (or the 220) drops out of peak-value lines; **every numerical answer is right**. Note 310 V on p6 and 312 V on p9 are the same quantity rounded opposite ways |
| **C2.9** | p7, p8 | "**Totol** Output"; a sentence ending mid-clause at Fig. 55.7(b); "Fig. **5.8**"; "As proved earlier in and now shown in Fig. 5.8" | Total; Fig. 55.8; the cross-reference is missing | typographic cluster; no physics affected |
| **C2.10** | p8 | "$V_{L(dc)}=2V_{LM}/\pi=0.636$ **V**" | $0.636\,V_{LM}$ | the trailing "V" is $V_{LM}$ with its subscript lost, so the line reads as 0.636 volts |
| **C2.11** | p8 | in Fig. 55.8(b), a *current* graph, the ripple region labelled "$V_L$ (ac)" | $I_L$ (ac) | a voltage symbol on a current axis; the neighbouring label on the same panel is $I_L$ (dc) |
| **C2.12** | p9 | "$4V_{IM}$"; quadrature sum $0.305V_{LM}$; ripple factor **0.482** | $V_{LM}$; **0.306**; the exact $\sqrt{\pi^2/8-1}=0.4834$ | recomputed $\sqrt{0.300105^2+0.0600211^2}=0.30605$; neither $0.305/0.636$ nor $0.306/0.636$ gives 0.482 |
| **C2.13** | p10 | "supplies power to a **1 k W** load"; "diode resistance is **25 W**"; the statement ends *determine"* | $1\ \mathrm{k\Omega}$; $25\ \Omega$; a colon, not a stray closing quote | the Ω glyph has been substituted by a roman W by the font; the solution uses 1000 Ω and 25 Ω throughout. **Read every stray W after a resistance value as Ω** |
| **C2.14** | p10 | Example numbering runs 55.1 → 55.3 → 55.4 → 55.5; **Example 55.2 does not exist** | Example 55.5 silently uses $I_{LM}=1.88$ A, $R_L=10\ \Omega$, $R_0=0.25\ \Omega$, $V_{sm}=20$ V | none of those values appears anywhere in the 26 pages, so Example 55.5 is unsolvable as printed |
| **C2.15** | p11 | "point A of the bridge rectifier always acts as an **anode** and point C as **cathode**"; "three distinct **physics** forms" | A is the **positive dc output** terminal and C the negative; physical | in diode-terminal language it is the opposite way round — A is where the *cathodes* of $D_1$, $D_2$ meet |
| **C2.16** | p13 | "$D_2$ will conduct current **upto $t_2$** after which **$D_2$** will take over … till $t_3$" | "$D_2$ … up to $t_3$ after which **$D_3$** will take over … till $t_4$" | as printed $D_2$ conducts up to the instant it starts and then hands over to itself |
| **C2.17** | p13 | three-phase half-wave figures of merit **η = 96.5 %**, **γ = 0.17** | **η = 96.8 %**; γ = 0.17 is defensible | recomputed exactly for an ideal three-pulse rectifier with a resistive load. The printed γ follows from counting only the lowest ripple harmonic, $\sqrt2/(p^2-1)=0.177$ — the same truncation used for the single-phase cases. The efficiency has no such explanation |
| **C2.18** | p14, p15 | "clamper circuits simply **clams**"; "it is **forward-biases B** which acts as a short" | clamp; forward-biased, and B acts as a short | wording only |
| **C2.19** | p16 | Fig. 52.33(c) clipping level labelled "**0.7 V**" while drawn **below** zero | $-0.7$ V | missing sign; the text calls it the negative clipping level |
| **C2.20** | p18 | Fig. 52.40: all three ordinates labelled $V_{in}$; panel (c) dc level labelled "**5 V**" | panels (b) and (c) are **outputs**, $V_o$; $-5$ V | the peak below it does carry its "−10 V", so the sign convention is established on the same panel |
| **C2.21** | p19, p20 | "$0\to t_1=t_1\to t_2=t_2\to t_2=T/2$"; "$\lambda = C_R$"; capacitor labelled "**1 F**" and "$C=1.0$ F"; "Fig. 52.40(a)"; "$\lambda = 100\times1\times10^{-6}$ **ms**"; $5\lambda$ = "**0.5 s**"; level ticked "**15 V**" | $t_2\to t_3$; $\lambda = CR$; $1\ \mu$F; Fig. 52.42(a); seconds; 0.5 ms; $-15$ V | a cluster of drops — the µ prefix twice, a subscript, a unit and a sign. **All the numbers used are right** |
| **C2.22** | p20 | "seen from **Fig. 52.44 and 52.45**"; Fig. 52.47(b) ordinate labelled $V_{in}$; its clamping level, drawn below zero, labelled $V_1$ | Figs. **52.45 and 52.46**; $V_o$; $-V_1$ | Fig. 52.44 is the *input* waveform; Fig. 52.48(b) labels the corresponding level $-V_1$, the consistent form |
| **C2.23** | p22, p23 | Fig. 55.33(a) prints an overstruck "−" above the "+" on $C_1$'s upper plate; "$C_2$\*"; "**If** is seen from Fig. 55.34"; "$D_3$ **conduct**" | "+" alone; no asterisk; It; conducts | the two capacitors must be series-**aiding** for the output to be $2V_m$; the rest is typography |
| **C2.24** | p23, p24 | Fig. 54.18's **middle symbol has both terminals marked "−"**; "Dr. Leo **Easki**" | − at the top, + at the bottom, matching the left and right symbols; Leo **Esaki** | a two-terminal device with two negative terminals has no defined bias |
| **C2.25** | p25 | $R_N=-200/I_P$, $-120/I_P$, $-60/I_P$, with **no units stated for $I_P$** | $I_P$ in **milliamperes** (numerators in mV) | dimensionally the numerators must be voltages; only mA lands inside the page's own quoted range of $-10$ Ω to $-200$ Ω. Read in amperes the same formula gives $-200$ kΩ |

---

## L3 — The Bipolar Junction Transistor

25 pages, 52 flags — the largest count in the course. The lesson spans two source chapters (57,
transistor fundamentals; 58, biasing), and the defects cluster tightly: **unit prefixes** in the
worked examples and on the characteristic curves, and **wrong resistor symbols** in the bias
formulas. Six of the twenty-two substantive flags would, if copied, produce a transistor with a
current gain below 1.

### Substantive

#### V3.1 · $\alpha$ printed upside down ·L3 p4

**Printed:** *"If we write adc simply as $\alpha$, then $\alpha = I_E/I_C$."*

**Should read:**
$$\boxed{\;\alpha = \frac{I_C}{I_E}\;}$$

**Why.** Three checks on the same two pages contradict it. (i) Two lines above, the page defines
$\alpha_{dc} = -I_C/I_E$; dropping the sign gives $I_C/I_E$, not its reciprocal. (ii) The next
sentence says $\alpha$ *"ranges from 0.95 to 0.999"* — but $I_E/I_C = 1/\alpha \approx 1.01$–$1.05$,
always **greater than one**. (iii) §57.9 on p5 prints $\alpha = I_C/I_E$.

#### V3.2 · Base current printed in milliamps ·L3 p5

**Printed:** $I_B = 20\ \mathrm{mA}$

**Should read:** $I_B = 20\ \mu\mathrm{A}$.

**Why.** The page's own solution substitutes $20\times10^{-6}$ A. Worked as printed,
$I_C = I_E - I_B = 2 - 20 = -18\ \mathrm{mA}$ — a negative collector current — and $\alpha = -9$.

#### V3.3 · A digit dropped inside $\beta = \alpha/(1-\alpha)$ ·L3 p7

**Printed:** $\beta = \alpha/(1-\alpha) = 0.99/(1 - \mathbf{0.09}) = 99$

**Should read:**
$$\boxed{\;\beta = \frac{0.99}{1-0.99} = \frac{0.99}{0.01} = 99\;}$$

**Why.** As printed $0.99/0.91 = 1.088$, not 99 — and carrying $\beta = 1.088$ forward gives
$I_C = 0.054$ mA instead of the page's own (correct) 3.97 mA, a factor of 73 out.

#### V3.4 · Two currents printed in the wrong unit ·L3 p7

**Printed:** $I_B = 50\ \mathrm{mA}$ and $I_{CO} = 5\ \mathrm{mA}$.

**Should read:** $I_B = 50\ \mu\mathrm{A}$, $I_{CO} = 5\ \mu\mathrm{A}$.

**Why.** The page's own first line works in microamps:
$5.505\times10^{3} = \beta\times50 + (1+\beta)\times5$. Taken as printed (all in mA) the same
equation reads $5.505 = 55\beta+5$, giving $\beta = 0.009$. And $I_B = 50$ mA beside
$I_C = 5.505$ mA would make the base current nine times the collector current.

#### V3.5 · A self-referential leakage current ·L3 p7

**Printed:** $I_{CEO} = \dfrac{I_C}{1-\alpha}$

**Should read:**
$$\boxed{\;I_{CEO} = \frac{I_{CO}}{1-\alpha}\;}$$

**Why.** $I_C$ appears on both sides — the self-reference test. Only the *leakage* current is
divided by $(1-\alpha)$; solving the printed version literally gives
$I_C[1 - 1/(1-\alpha)] = \beta I_B$, i.e. a negative collector current.

#### V3.6 · The leakage term typeset but never added ·L3 p7

**Printed:** $I_C = 1.9\ \mathrm{mA}$ and $I_E = 1.94\ \mathrm{mA}$.

**Should read:** recomputing the page's own expression term by term,
$$46.6\times0.04 = 1.864\ \mathrm{mA},\qquad (1+46.6)\times0.008 = 0.381\ \mathrm{mA}$$
$$\boxed{\;I_C = 2.25\ \mathrm{mA},\qquad I_E = I_C + I_B = 2.29\ \mathrm{mA}\;}$$

**Why.** $1.9$ mA is $\beta I_B$ alone — the leakage term $(1+\beta)I_{CO} = 0.381$ mA is printed
and then not carried into the sum, so the answer is short by exactly one leakage term. Independent
confirmation without $\beta$: $I_C = (\alpha I_B + I_{CO})/(1-\alpha) = 0.04716/0.021 = 2.246$ mA.

#### V3.7 · $BC$ is not $\Delta I_E$ ·L3 p9

**Printed:** $\alpha_{ac} = \Delta I_C/\Delta I_E = DE/BC$, then $(6.2-4.3)/2$.

**Should read:**
$$\boxed{\;\alpha_{ac} = \frac{DE}{\Delta I_E} = \frac{6.2-4.3}{6-4} = 0.95\;}$$
where $\Delta I_E = 2$ mA is the difference between the two curves' $I_E$ **labels**, not a distance
measured on the graph.

**Why.** $B$ and $C$ lie on the $I_E = 6$ mA and $I_E = 4$ mA curves at the same $V_{CB}$, and $D$
and $E$ are their projections onto the $I_C$ axis — so $DE$ and $BC$ are the **same length** and
$DE/BC = 1$. A reader who measures both segments off the page as instructed gets $\alpha_{ac} = 1$,
impossible for a CB current gain.

#### V3.8 · The ordinate of Fig. 57.18 in the wrong unit ·L3 p10

**Printed:** the $I_B$ axis labelled **mA**, ticked 25, 50, 75.

**Should read:** **µA**.

**Why.** (i) 75 mA of base current at $V_{BE} = 0.4$ V is impossible for a small-signal transistor —
with $\beta\approx100$ it implies 7.5 A of collector current. (ii) The text beside the figure gives
$R_{in}$ from 4 kΩ down to 600 Ω; read in mA the slopes are a few ohms. (iii) The corresponding CE
output family two pages later labels its base-current curves **µA**.

#### V3.9 · The top curve of Fig. 57.19 labelled 80 mA ·L3 p11

**Printed:** $I_B = 80\ \mathrm{mA}$.

**Should read:** $I_B = 80\ \mu\mathrm{A}$.

**Why.** The text on the same page selects points on the *"$I_B = 60\ \mu\mathrm{A}$ and
$40\ \mu\mathrm{A}$ lines"* — the other four curves of the same family are explicitly microamps. And
with $I_C \approx 8$ mA on that curve, 80 mA would give $\beta = 0.1$; 80 µA gives $\beta = 100$.

#### V3.10 · The abscissa of Fig. 57.22(b) is $V_{CB}$, not $V_{CE}$ ·L3 p12

**Printed:** the horizontal axis labelled $V_{CE}$ **and** the two plotted curves labelled
$V_{CE} = 2$ V and $V_{CE} = 4$ V.

**Should read:**
$$\boxed{\;V_{CB}\ \text{on the abscissa},\quad I_B\ \text{on the ordinate},\quad\text{one curve per } V_{CE}\;}$$

**Why.** One symbol cannot be both the abscissa and the family parameter. p11 computes
$V_{CB} = 1.3$ V for $V_{CE} = 2$ V and $V_{CB} = 3.3$ V for $V_{CE} = 4$ V, both at
$I_B = 100\ \mu$A — and on the figure the two curves cross the dashed $100\ \mu$A line at exactly
**1.3** and **3.3**.

#### V3.11 · $R_L$ missing from a collector-voltage expression ·L3 p13

**Printed:** $V_{CB} = V_{CC} - I_C \cong V_{CC} - I_ER_L = 25 - 0.5\times10 = 20\ \mathrm{V}$

**Should read:**
$$\boxed{\;V_{CB} = V_{CC} - I_CR_L\;}$$

**Why — dimensional.** $V_{CC}-I_C$ is volts minus amperes. The second expression on the same line
carries $R_L$ correctly, and the arithmetic uses it.

#### V3.12 · A formula labelled $I_E$ that is $I_B$, with the wrong denominator ·L3 p15

**Printed:** $I_E = \dfrac{V_{CC}-V_{BE}}{R_E + \beta R_E}$

**Should read:**
$$\boxed{\;I_B = \frac{V_{CC}-V_{BE}}{R_B + \beta R_E}\;}$$

**Why — three checks.** (i) The first member of the same box already gives
$I_E = (V_{CC}-V_{BE})/(R_E + R_B/\beta)$; multiplying through by $\beta$ and dividing by $\beta$
yields the corrected form for $I_B$, so the two printed forms cannot both be $I_E$. (ii) As printed,
$R_E+\beta R_E = (1+\beta)R_E$ contains **no $R_B$ at all** — the bias current would not depend on
the base resistor. (iii) The very next item in the box is $I_C = \beta I_B$, which needs an $I_B$ to
use.

#### V3.13 · Beta sensitivity defined against $I_B$ instead of $\beta$ ·L3 p17

**Printed:**
$$\frac{dI_C}{I_C} = K_\beta\frac{dI_B}{\beta},\qquad K_\beta = \frac{\beta}{I_C}\cdot\frac{dI_C}{dI_B}$$

**Should read:**
$$\boxed{\;\frac{dI_C}{I_C} = K_\beta\frac{d\beta}{\beta},\qquad K_\beta = \frac{\beta}{I_C}\cdot\frac{dI_C}{d\beta}\;}$$

**Why — dimensional, and the page contradicts itself one line later.** $dI_C/I_C$ is a pure number,
while $K_\beta\,dI_B/\beta$ carries **amperes**. The very next sentence asserts that *"$K_\beta$ is
a dimensionless ratio"*. A quantity named "beta sensitivity" must be defined against a change in
$\beta$.

#### V3.14 · The 75 °C block headed "At 25°" ·L3 p19

**Printed:** **"At 25°"** over the working $I_B = 0.113$ mA, $I_C = 150\times0.113 = 16.95$ mA,
$V_{CE} = 3.52$ V.

**Should read:** **At 75 °C.**

**Why.** $\beta = 150$ is, by the question's own statement, the 75 °C value; the 25 °C block
($\beta = 100$, $I_C = 11.3$ mA, $V_{CE} = 6.35$ V) sits immediately above it, and the percentage
changes that follow are computed **between the two blocks** — meaningless unless they are at
different temperatures.

#### V3.15 · $K_\beta$ printed without its "$1+$" ·L3 p19

**Printed:** $K_\beta = \dfrac{1}{\beta R_L/R_B} = 1 - \dfrac{I_C}{I_{C(sat)}}$

**Should read:**
$$\boxed{\;K_\beta = \frac{1}{1 + \beta R_L/R_B}\;}$$

**Why — the page's own two expressions disagree.** Substituting
$I_C = V_{CC}/(R_L+R_B/\beta)$ and $I_{C(sat)} = V_{CC}/R_L$ into the right-hand expression gives
$$1-\frac{I_C}{I_{C(sat)}} = \frac{R_B/\beta}{R_L+R_B/\beta} = \frac{1}{1+\beta R_L/R_B}$$
— the corrected form. Numerically, Example 58.7 ($R_L = 1$ K, $R_B = 100$ K, $\beta = 100$) gives
1.0 from the printed formula and 0.5 from the corrected one, and **p20 part (iv) evaluates 0.5**.

#### V3.16 · An "approximation" for $S$ that is a current ·L3 p19

**Printed:**
$$S = \frac{1+R_B/R_L}{1+R_B/(1+\beta)R_L}\;\cong\;\frac{V_{CC}}{R_L+R_B/\beta}$$

**Should read:** there is **no such approximation** — the right-hand expression is the formula for
$I_C$, printed six lines earlier on the same page. Use the left-hand expression.

**Why — dimensional.** $S = dI_C/dI_{CO}$ is dimensionless; $V_{CC}/(R_L+R_B/\beta)$ has units of
current. For Example 58.7 the printed "approximation" gives $12/2 = 6$ (milliamps) where the correct
$S$ is $(1+100)/(1+100/101) = 50.75$ — a factor of eight out and in the wrong unit.

#### V3.17 · A base resistance printed as 50 instead of 500 ·L3 p20

**Printed:** $K_\beta = \dfrac{1}{1+100(10+10)/\mathbf{50}} = 0.2$

**Should read:**
$$\boxed{\;K_\beta = \frac{1}{1+\beta(R_E+R_L)/R_B} = \frac{1}{1+100(20)/500} = 0.2\;}$$

**Why.** $R_B$ is **500 K** in Fig. 58.13. Evaluated as printed, $1/(1+2000/50) = 0.024$ — not the
0.2 the page itself reports, and the page's second route, $1 - I_C/I_{C(sat)} = 1-0.6/0.75 = 0.2$,
confirms 0.2.

#### V3.18 · The simplified emitter current divided by $R_B$ ·L3 p21

**Printed:** *"If $V_{EE}\gg V_{BE}$ and $R_E \gg R_B/\beta$, $I_E = V_{EE}/R_B$."*

**Should read:**
$$\boxed{\;I_E \cong \frac{V_{EE}}{R_E}\;}$$

**Why.** Dropping the two small terms from $I_E = (V_{EE}-V_{BE})/(R_E+R_B/\beta)$ leaves
$V_{EE}/R_E$ — **the surviving denominator is the one the condition says is large**, not the one it
says is small. The same result is printed correctly in §57.22 on p14, and Example 58.9 uses $R_E$;
with its values the printed form gives 1 mA against the correct 0.5 mA.

#### V3.19 · Fig. 58.14 labels both resistors $R_E$ ·L3 p21

**Printed:** the base resistor (left branch, to ground) and the emitter resistor (right branch, to
$-V_{EE}$) are **both labelled $R_E$**.

**Should read:** the base resistor is $R_B$.

**Why.** Every equation in the surrounding derivation —
$I_BR_B + I_ER_E = V_{EE}-V_{BE}$, $I_E = (V_{EE}-V_{BE})/(R_E+R_B/\beta)$, $S$, $K_\beta$ — treats
$R_B$ and $R_E$ as two distinct quantities, and Example 58.9's Fig. 58.15 gives them different
values ($R_B = 10$ K, $R_E = 20$ K). As labelled the figure has no $R_B$ at all.

#### V3.20 · A self-referential stability-factor denominator ·L3 p21

**Printed:** $S = \dfrac{1+R_B/R_E}{1+R_B/\beta R_{\mathbf{B}}}$

**Should read:**
$$\boxed{\;S = \frac{1+R_B/R_E}{1+R_B/\beta R_E}\;}$$

**Why.** $R_B/\beta R_B = 1/\beta$, which deletes $R_E$ from the denominator entirely — $S$ would
then be independent of the emitter resistor, contradicting the general formula three lines above and
the whole point of emitter degeneration. The **numeric substitution on the same line uses 20**, i.e.
$R_E$.

#### V3.21 · A beta-sensitivity formula that invents a symbol and loses $\beta$ ·L3 p21

**Printed:** $K_\beta = \dfrac{1}{1+R_E/R_\beta}$

**Should read:**
$$\boxed{\;K_\beta = \frac{1}{1+\beta R_E/R_B}\;}$$

**Why.** $R_\beta$ is not defined anywhere in either chapter. The correct expression is printed four
lines earlier in the same section, and the numeric substitution on the same line — "$1+50\times20/10$"
— is exactly $1+\beta R_E/R_B$ with $\beta = 50$, $R_E = 20$ K, $R_B = 10$ K.

#### V3.22 · $V_{BB}$ printed where $V_{BE}$ is meant ·L3 p23

**Printed:** the question specifies $V_{BB} = 0.3\ \mathrm{V}$.

**Should read:** $V_{BE} = 0.3$ V, the germanium base–emitter drop.

**Why — the two symbols collide inside this very problem.** $V_{BB}$ is the Thevenin base supply,
and the solution computes it explicitly as $20\times25/125 = 4$ V. The 0.3 V is used in both halves
of the solution as the junction drop: $I_E = (4-0.3)/6$ and $I_B = (4-0.3)/(20+51\times6)$. Taken as
printed, $V_{BB} = 0.3$ V would leave the transistor cut off.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C3.1** | p1–p2 | *"Fig 57.1 (c), shows the picture of C1815 transistor"* — panel (c) is a row of coloured LEDs; *"refer to the picture shown in Fig. 57.2 (c)"* mid-biasing-discussion — that panel is a seven-segment display | the transistor photograph is the unnumbered one at top right | figure/text mismatch in both places |
| **C3.2** | p5, p8, p9, p10 | $\alpha_{ac} = \dfrac{-I_C}{I_E}$ and $\beta_{ac} = \dfrac{I_C}{I_B}$, with **no increments** — the same dropout hits $R_{in}$, $R_{out}$, $\alpha_{ac}$, $\beta_{ac}$ | $\Delta I_C/\Delta I_E$, $\Delta I_C/\Delta I_B$ | the $\Delta$ glyph does not render, making the ac definitions look identical to the dc ones; the prose beside them says *"the ratio of **change** in…"* |
| **C3.3** | p14, p15, p18, p19, p20 | figure annotations print "**=100**" and "**=100-150**" with nothing to the left of the equals sign (Figs. 57.28, 57.30, 58.9, 58.10, 58.13) | $\beta = 100$, $\beta = 100$–$150$ | the $\beta$ glyph drops out of figure annotations; confirmed by the accompanying example statements |
| **C3.4** | p18, p19, p24 | $V_C = V_{CC}\times I_CR_L = 30-2\times7.5$; $I_BR_B+V_{BE}\cong V_{CC}\times I_CR_L$; $V_{CE} = V_{CC}\times I_CR_L = 10-2\times2$ | $V_{CC} - I_CR_L$ in all three | a minus sign set as a multiplication sign; the arithmetic to the right of each equals sign performs the correct **subtraction**. Note that as printed each is dimensionally impossible, $\mathrm{V}\times\mathrm{V} = \mathrm{V^2}$ |
| **C3.5** | p6 | *"the CB transistor circuit shown in Fig. 57.11"* | the figure beside it is captioned **Fig. 57.10** | cross-reference slip |
| **C3.6** | p7 | *"As seen from Art. 7.12"* | Art. **57**.12 | leading digit dropped |
| **C3.7** | p7 | *"$I_{CO} = 8\ \mu\mathrm{A} = 0.008\ \mu\mathrm{A}$"* | $0.008\ \mathrm{mA}$ | the working uses currents in mA throughout |
| **C3.8** | p7 | Example 57.7 asks *"What is the collector current when base current is zero?"* and the solution stops after $I_C$ and $I_E$ | the answer is $I_{CEO} = I_{CO}/(1-\alpha) = 381\ \mu\mathrm{A}$ | nothing printed is wrong; the solution is incomplete |
| **C3.9** | p12 | the paragraph argues in NPN terms ($V_{CB}$, $V_{BE}$) beside Fig. 57.23, a **PNP** correctly labelled $V_{EB}$, $V_{BC}$; and cites *"the transistor polarity rule (Art. 57.2)"* | both halves are individually right; the polarity rule is **Art. 57.3** | placing them side by side invites the reader to think one is mislabelled |
| **C3.10** | p13 | §57.21 writes $V_{BE}$ and $V_{CB}$ for the **PNP** of Fig. 57.23 | $V_{EB}$ and $V_{BC}$, per the figure's own labels and §57.3's double-subscript rule | read them as magnitudes and take the sign from the transistor type |
| **C3.11** | p14 | part (iv) prints $V_{CE} = V_{CC}-I_CR_C$ while Fig. 57.28 labels the collector resistor $R_L$ | either symbol, consistently | $R_L$ and $R_C$ are used interchangeably for the collector load throughout both chapters |
| **C3.12** | p15 | part (i) result printed *"$\cong]$1 mA"* | $\cong 1\ \mathrm{mA}$ | stray closing bracket |
| **C3.13** | p16 | *"$I_C = I\beta + (I+\beta)I_{CO}$"*; and the differentiated line opening *"$I = \beta\,dI_B/dI_C+\ldots$"* | $\beta I_B + (1+\beta)I_{CO}$; left-hand side is $\mathbf{1}$, being $dI_C/dI_C$ | a digit-1 / letter-I substitution. The quoted result $S = (1+\beta)/(1-\beta\,dI_B/dI_C)$ can only follow from a left-hand side of 1 |
| **C3.14** | p17 | the summary list cites Fig. 58.9 for base bias, 58.10 for emitter feedback, 58.13 and 58.15 for two-supply and divider bias | on p18–p21 those figures are, respectively, emitter-feedback, plain base-bias, collector-and-emitter-feedback and the divider *example* (the general circuits being 58.14 and 58.16) | work from the figure captions on the page, not from this list |
| **C3.15** | p17 | §58.9 forward-references Art. 58.20 and Fig. 58.25 | both lie **beyond the extract** and cannot be checked | the chapter's own base-bias circuit appears as Fig. 58.7 (p16) and Fig. 58.10 (p19) |
| **C3.16** | p13 | §57.21 works *"circuit MEBM"* and *"circuit NCBN"* | nodes **M** and **N** are not marked anywhere on Fig. 57.23(b) | from the loops as traversed, M is the $V_{EE}$ terminal at the top of $R_E$ and N the $V_{CC}$ terminal at the top of $R_L$ |
| **C3.17** | p19 | *"$V_{CE} = I_CR_C = 12-(11.3\times10\text{–}3\times500)$"*, then repeated as *"$V_{CE} = V_{CC}-I_CR_C = 12\times(11.3\times10\times3\times500)$"* | $V_{CE} = V_{CC}-I_CR_C$ with the exponent as $10^{-3}$ | the first line loses "$V_{CC}-$", the second sets the minus as $\times$ and breaks the exponent further. **Both printed results are the correct 6.35 V** |
| **C3.18** | p20 | part (i) answer bolded **5.6 mA**; part (iv) symbol printed $K_B$ | $11.3/2 = \mathbf{5.65}$ mA, which parts (ii) and (iii) both use; $K_\beta$ | rounding and an upright-B subscript |
| **C3.19** | p20 | part (v) answer **50.5** | $S = \dfrac{1+100/1}{1+100\times1/101} = \dfrac{101}{1.9901} = \mathbf{50.75}$ | the printed 50.5 is $101/2$, i.e. the denominator rounded from 1.9901 to 2 — a 0.5 % slip |
| **C3.20** | p20 | *"$V_C = V_{CC}-(I_C+I_B)$; $\;R_L \cong V_{CC}-I_CR_L$"* | $V_C = V_{CC}-(I_C+I_B)R_L \cong V_{CC}-I_CR_L$ | a semicolon separates $R_L$ from the bracket it multiplies; as printed the first expression is volts minus amperes |
| **C3.21** | p21 | *"$V_E = -(V_{BE}+I_CR_B/\beta) = (0.7+0.46\times10/50) = -0.8\ \mathrm{V}$"* | the middle expression needs its leading minus | as printed it reads $+0.792$ while the answer beside it reads $-0.8$ V; first and last forms are correct |
| **C3.22** | p22 | the first form of $S$ prints $R_e$ (lower-case e) | $R_E$, as the second form on the next line has it | lower-case $r_e$ is elsewhere the **small-signal emitter resistance**, a different quantity |
| **C3.23** | p18, p22 | the $\beta$-rule cited as *"Art. 57.24"* (p18) and *"Art. 58.12"* (p22); *"Fig. 8.18"*; *"Substituting the value of $I_E = (1+\beta)I_B$ in (i) above"* | neither article can be followed — 58.12 is *Base Bias with Collector and Emitter Feedbacks* and 57.24 lies outside the extract; Fig. **58**.18; the equation meant is the KVL line immediately above | no equation on that page carries an (i) tag |
| **C3.24** | p23 | $I_C = \beta I_B = 50\times11.3$ set as *"50×l1.3"*; *"$I_E = (1+\beta\,I_B$"* | 11.3; $I_E = (1+\beta)I_B$ | a letter l for the digit 1, and a missing closing bracket |
| **C3.25** | p24 | *"on the $(20+10) = 30$ **mA** line"*; *"at point $D$, $I_C$ measures $1.1\ \mu\mathrm{A}$"* | $30\ \mu\mathrm{A}$; $1.1\ \mathrm{mA}$ | the symmetric sentence one line later correctly says $10\ \mu$A, and the arithmetic that follows ($10-2\times1.1 = 7.8$ V) plus Fig. 58.23 both require 1.1 mA |
| **C3.26** | p25 | *"rms voltage variation $\;1.8\sqrt2\;\;1.27\ \mathrm{V}$"*; *"Now, **proper** dissipated in RL"* | $1.8/\sqrt2 = 1.27\ \mathrm{V}$; power dissipated in $R_L$ | both the division sign and the equals sign are missing, so the page reads as $1.8\sqrt2 = 2.55$ V beside a printed 1.27 V; the $P_{ac}$ calculation uses 1.27 |
| **C3.27** | p25 | *"$V_{CE(\mathbf{out}\text{-}off)}$"*; *"The slope of the ac load line is given by $y = \times\;1/R_{ac}$"* | $V_{CE(cut\text{-}off)}$; slope $= -1/R_{ac}$ | the same minus-as-$\times$ fault as `C3.4`, plus a stray $y$ |
| **C3.28** | p2, p4, p6, p8, p11, p12, p24, p25 | "emmitter"; "adc" (upright) for $\alpha_{dc}$ and "tranistor"; "the **about** 2 equations"; "**ac-ross** C/B junction"; "common **carrier** to both the input (CB) and output (CE) **carriers** circuits" and "practically **idential**"; "potential difference … **in** written as $V_{CB}$"; "**Suposse** an ac input signal"; "Now, **proper** dissipated in RL" | emitter; $\alpha_{dc}$, transistor; above; across; *common to both the input and output circuits*, identical; is written as; Suppose; power | spelling and word-substitution cluster gathered in one ID; nothing computed changes |
| **C3.29** | p25 | $I_{C(sat)} = V_{CC}/(\mathbf{R_1}+R_E)$; and *"$A_{QB}$"* set with QB as a subscript | $R_L$ (or $R_C$); the line **AQB**, through points A, Q and B | $R_1$ is everywhere else the upper arm of a base potential divider — a resistor that cannot appear in a collector-saturation formula. Fig. 58.25(a) is not in the extract, so its own labelling cannot be confirmed |
| **C3.30** | p16 | §58.4: *"The collector current for $C_E$ circuit is given by"* | CE, the **configuration**, not a subscripted symbol | as set, $C_E$ reads as a capacitance |

---

## L4 — Field Effect Transistors

24 pages, 36 flags. The dominant fault here is the **loss of the increment symbol**: three of the
lesson's small-signal parameter definitions ($r_d$, $g_m$, $\mu$) are printed as ratios of totals
rather than ratios of increments, which turns every slope into a chord. Alongside it sits an
unresolved **sign convention on $V_P$** that runs the length of the chapter.

### Substantive

#### V4.1 · The N-channel bar labelled P ·L4 p3

**Printed:** in Fig. 63.1(a) the **N-channel** drawing labels the bar itself **P** and the gate
diffusion **P**. (The P-channel drawing beside it labels the bar **P** and the gate diffusion **N**,
so the outer label is the bar material.)

**Should read:**
$$\boxed{\;\text{bar} = N,\qquad\text{both gate diffusions} = P\;}$$

**Why.** p2's own text requires it: *"a narrow bar of N-type semiconductor … two P-type junctions
are diffused on opposite sides"*.

#### V4.2 · $V_P$ used with both signs in one chapter ·L4 p4–p8, p15

**Printed:** Fig. 63.5, Fig. 63.6 and the p6 footnote place $V_P$ on the $V_{DS}$ axis as a
**positive** voltage; Shockley's equation, Fig. 63.7, the statement *"$I_D = 0$ when
$V_{GS} = V_P$"* and every worked example use $V_P$ as the **negative** $V_{GS(off)}$. Nothing on
the page reconciles them.

**Should read** — name the cut-off voltage explicitly:
$$\boxed{\;I_D = I_{DSS}\left(1-\frac{V_{GS}}{V_{GS(off)}}\right)^{2},\qquad V_{GS(off)} < 0\ \text{for an N-channel JFET}\;}$$

**Why.** Put $V_{GS} = -1$ V into a device with $|V_P| = 4$ V. With the negative value,
$I_D = I_{DSS}(1-0.25)^2 = 0.56\,I_{DSS}$ — sensible. With the positive value,
$I_D = I_{DSS}(1+0.25)^2 = 1.56\,I_{DSS}$ — **larger than $I_{DSS}$, which is impossible**.

#### V4.3 · $r_d$ printed as a ratio of totals ·L4 p7

**Printed:** $r_d = \dfrac{V_{DS}}{I_D}\,\big|\,V_{GS}$, with no increment symbols; the "constant"
qualifier of the first form printed as "$-V_{GS}$ constant" (a lost vertical bar).

**Should read:**
$$\boxed{\;r_d = \left.\frac{\delta V_{DS}}{\delta I_D}\right|_{V_{GS}}\;\neq\;\frac{V_{DS}}{I_D}\;}$$

**Why.** As printed, $V_{DS}/I_D$ is the **d.c.** drain resistance $R_{DS}$, which the same chapter
defines separately on p8. A ratio of totals is a chord; a ratio of increments is a slope, and only
the slope is the small-signal parameter.

#### V4.4 · The same increment loss in $g_m$ and $\mu$ ·L4 p8

**Printed:** $g_m$ given a second form $\dfrac{I_D}{V_{GS}}\,\big|\,V_{DS}$, and
$\mu = \dfrac{V_{DS}}{V_{GS}}\,\big|\,I_D$.

**Should read:**
$$\boxed{\;g_m = \left.\frac{\delta I_D}{\delta V_{GS}}\right|_{V_{DS}},\qquad
\mu = \left.\frac{\delta V_{DS}}{\delta V_{GS}}\right|_{I_D}\;}$$

**Why.** Taken literally they give the wrong number: for Example 63.1 at $V_{GS} = -2$ V the ratio
of totals gives $0.967\ \mathrm{mA}/2\ \mathrm{V} = 0.48$ mS where the true $g_m$ is 1.93 mS — out
by a factor of four.

#### V4.5 · A derivative taken with respect to the wrong variable ·L4 p8

**Printed:** the differentiation line's left-hand side is $\dfrac{dI_D}{dI_{DSS}}$.

**Should read:**
$$\boxed{\;\frac{dI_D}{dV_{GS}} = 2I_{DSS}\left(1-\frac{V_{GS}}{V_P}\right)\left(-\frac{1}{V_P}\right)\;}$$

**Why.** The right-hand side carries the chain-rule factor $-1/V_P$, which can only come from
$d(V_{GS}/V_P)/dV_{GS}$, and the result is then named $g_m$, which is $\delta I_D/\delta V_{GS}$ by
definition. A derivative with respect to $I_{DSS}$ would carry units of A/A, not A/V.

#### V4.6 · A symbol that exists nowhere in the chapter ·L4 p8

**Printed:** $g_m = g_{mo}\left(1-\dfrac{V_{DSS}}{V_P}\right) = g_{mo}\sqrt{I_D/I_{DSS}}$

**Should read:**
$$\boxed{\;g_m = g_{mo}\left(1-\frac{V_{GS}}{V_P}\right)\;}$$

**Why.** There is no quantity $V_{DSS}$ anywhere in the chapter. Both equations being combined carry
$V_{GS}$, and Example 63.1(iii) confirms it by substituting $V_{GS} = -1$ V.

#### V4.7 · A JFET drain current printed in amperes ·L4 p8

**Printed:** part (i) answer **3.87 A**.

**Should read:**
$$\boxed{\;I_D = 3.87\ \mathrm{mA}\;}$$

**Why.** The data are in milliamperes ($I_{DSS} = 8.7$ mA) and Shockley's equation is linear in
$I_{DSS}$, so the answer inherits the unit. A JFET passing 3.87 A would dissipate tens of watts.

#### V4.8 · A gate-source bias that has lost its minus sign ·L4 p10

**Printed:** $V_{GS} = -I_DR_S = -10\times150 = \mathbf{1.5\ V}$

**Should read:**
$$\boxed{\;V_{GS} = -1.5\ \mathrm{V}\;}$$

**Why.** The left-hand side of the same line carries the minus, and the sentence underneath says the
gate is *"1.5 V negative"*. A positive $V_{GS}$ on an N-channel JFET would forward-bias the gate
junction.

#### V4.9 · A leading digit dropped from a drain voltage ·L4 p11

**Printed:** $V_D = 12 - 0.73\times2 = \mathbf{1.54\ V}$

**Should read:**
$$\boxed{\;V_D = 10.54\ \mathrm{V}\;}$$

**Why.** $12 - 1.46 = 10.54$, and the **very next line of the same solution uses 10.54 V** to get
$V_{DS} = 6.89$ V.

#### V4.10 · A drain resistor that appears nowhere in the question ·L4 p11

**Printed:** the same line uses $R_L = 2\ \mathrm{k\Omega}$, a value absent from the question and
from Fig. 63.13, where the drain resistor is drawn unlabelled.

**Should read:**
$$\boxed{\;R_L = 2\ \mathrm{k\Omega}\ \text{(inferred from the working, not given)}\;}$$

**Why.** The example cannot be reproduced from the data as printed. $V_{GS}$ and $I_D$ do not depend
on $R_L$ and are unaffected; $V_D$ and $V_{DS}$ do.

#### V4.11 · A voltage gain with units of ohms ·L4 p13

**Printed:** $A_v = \dfrac{r_dR_L}{r_d+R_L+g_mr_dR_L}$

**Should read:**
$$\boxed{\;A_v = \frac{g_mr_dR_L}{r_d+R_L+g_mr_dR_L}\;}$$

**Why.** (i) The numerator as printed has units of $\Omega^2$ against a denominator in $\Omega$, so
the "gain" would carry units of ohms. (ii) It does not follow from the chapter's own equation (i)
one line above, which carries $g_m$. **Example 63.8 on the next page uses the correct form.**

#### V4.12 · Two printed answers that contradict each other ·L4 p15

**Printed:** part (ii) answer **12 mA**, i.e. $I_{DSS}$.

**Should read:**
$$\boxed{\;I_D = 12\left(1-\tfrac58\right)^2 = 1.69\ \mathrm{mA}\;}$$

**Why.** $I_{DSS}$ is the saturated current for $V_{GS} = 0$ only. The same problem's part (i) can
give 3 V only if $V_{GS} = -5$ V — so 3 V requires a bias of $-5$ V and 12 mA requires a bias of
0 V. The two printed answers cannot both belong to one operating point.

#### V4.13 · A cut-off voltage twice its correct value ·L4 p15

**Printed:** part (i) answer **$-5$ V**.

**Should read:** from the data given ($I_{DSS} = 5$ mA, $g_{mo} = 4000\ \mu$S) and the chapter's own
relation $g_{mo} = -2I_{DSS}/V_P$ (p8),
$$\boxed{\;V_{GS(off)} = -\frac{2\times5\ \mathrm{mA}}{4000\ \mu\mathrm{S}} = -2.5\ \mathrm{V}\;}$$

**Why.** The printed $-5$ V would require $I_{DSS} = 10$ mA. Cross-check: tutorial problem 6 uses
the same relation correctly, $2\times8.4/3 = 5600\ \mu$S ✓.

#### V4.14 · A $K$ evaluated from the previous example's data ·L4 p22

**Printed:** the question gives $V_{GS(th)} = 4$ V, but $K$ is evaluated as $4/(10-5)^2$ — i.e. with
$V_{GS(th)} = 5$ V, the value belonging to Example 63.11 on the previous page. The question also
quotes $I_{D(ON)}$ *"at $V_{DS} = 10$ V"*, where $K$ requires the $V_{GS}$ at which $I_{D(ON)}$ was
measured.

**Should read** — taking $I_{D(ON)} = 4$ mA at $V_{GS} = 10$ V with $V_{GS(th)} = 4$ V:
$$\boxed{\;K = \frac{4}{(10-4)^2} = 0.111\ \mathrm{mA/V^2},\quad I_D = 0.111(6-4)^2 = 0.444\ \mathrm{mA},\quad V_{DS} = 16-2.22 = 13.8\ \mathrm{V}\;}$$

**Why.** $A_v = 25$ and $v_o = 2.5$ V are unaffected, depending only on $g_m$ and $R_L$.

#### V4.15 · An internally inconsistent answer set ·L4 p24

**Printed:** $V_{DS} = \mathbf{12.2\ V}$.

**Should read:** with the drain resistor Fig. 63.38(d) actually shows, $3\ \mathrm{k\Omega}$,
$$\boxed{\;V_{DS} = 15-0.556\times3 = 13.3\ \mathrm{V}\;}$$

**Why.** 12.2 V is what a $5\ \mathrm{k\Omega}$ drain resistor would give ($15-2.78$). But the same
answer line's $v_o = 0.825$ V can only come from $R_L = 3\ \mathrm{k\Omega}$ —
$5500\ \mu\mathrm{S}\times5\ \mathrm{k\Omega}\times50\ \mathrm{mV}$ would give 1.375 V — so
$3\ \mathrm{k\Omega}$ is the right reading and the printed answer set contradicts itself.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C4.1** | p1 | eighth objective: "D.C. **Baising** of a JFET" | Biasing | §63.8 on p9 spells it correctly |
| **C4.2** | p4 | all four panels of Fig. 63.2 label the gate-source voltage **$V_{SS} = 0$** | $V_{GS} = 0$ | $V_{SS}$ is used later in the same chapter (Fig. 63.8c, p9) for the **source supply voltage**, a different quantity |
| **C4.3** | p4 | Fig. 63.2 labels the resistor between $V_{DD}$ and the **drain** as $R_S$; and calls the channel current $I_D$ in panel (b) but $I_S$ in (c) and (d) | $R_L$ for the drain resistor; either current symbol | from §63.8 onward $R_S$ is consistently the **source** resistor. $I_S = I_D$ when $I_G = 0$, so the current labels are harmless |
| **C4.4** | p5 | footnote: "It has negative value for an N-channel JFET but a positive value **or** a P-channel JFET" | **for** a P-channel JFET | a one-letter typo in the sign convention the whole chapter depends on |
| **C4.5** | p6 | $I_{DSS}\left(\mathbf{I}-V_{GS}/V_{GS(off)}\right)^2$ — an italic capital I for the digit 1 | the digit **1** | the identical equation on p7 prints it correctly |
| **C4.6** | p6 | footnote "$V_p = /V_{GSC(off)}/$" | $V_p = \lvert V_{GS(off)}\rvert$ | the modulus bars have come through as forward slashes and the subscript has an extra C |
| **C4.7** | p12 | the drain-to-source capacitor in Fig. 63.15 labelled **$C_{dl}$** | $C_{ds}$ | every other capacitance in the figure is named by its two terminals, and this one connects d to s; Example 63.14 (p22) calls it $C_{ds}$ |
| **C4.8** | p13 | $A_v = -3000\times10^{-6}\times4.76 = -14.3$ | $4.76\times10^{3}\ \Omega$ | the factor $10^3$ that turns 4.76 kΩ into ohms has dropped; as printed the arithmetic gives $-0.0143$ |
| **C4.9** | p13 | "The current generator is $g_m,\ V_{gs}$" | $g_mV_{gs}$ | a comma where a multiplication is meant; Fig. 63.18(b) labels the source correctly |
| **C4.10** | p14 | "$i_d = g_mV_{gs} = g_mV_i$", as though $V_{gs} = V_i$ | $i_d = -g_mV_{gs} = +g_mV_i \Rightarrow A_v = +g_m(r_d \parallel R_L)$ | with the gate grounded and the signal on the source, $V_{gs} = -V_i$. The published result is still the standard one, because Fig. 63.20(b) draws the current-source arrow **reversed**, absorbing the sign |
| **C4.11** | p15 | problems 4 and 5 spell the device **"JEET"**; problem 5 prints "$I_{DSS}$ 5 mA" | JFET; $I_{DSS} = 5$ mA | scan noise; no physics affected |
| **C4.12** | p16 | in Fig. 63.23 the **substrate** lead is labelled **S** and the **source** lead below it is labelled **s / "Source"** | the substrate terminal is **SS**, as p17–p18 calls it | one letter for two different terminals in one drawing |
| **C4.13** | p17 | "the gate, $\mathrm{SiO_2}$ insulator and channel **from** a parallel-plate capacitor"; "it is shorted **the source** internally" | **form**; shorted **to** the source | scan noise |
| **C4.14** | p17 | the drain current in Fig. 63.24(b) labelled **$I_B$** | $I_D$, as panel (a) labels the same current | there is no base terminal in a MOSFET |
| **C4.15** | p19 | "$I_D = \mathrm{K}(V_{GS}-V_{GS(th)})2$" — the exponent stranded outside the bracket | $I_D = K\left(V_{GS}-V_{GS(th)}\right)^{2}$ | the squared form above is what is meant; p20's differentiation and Examples 63.10–63.13 all confirm it |
| **C4.16** | p20 | "A P-channel E-only MOSFET (PMOS) is constructed like **NOMS**" | NMOS | transposed letters |
| **C4.17** | p22 | the numerator of the $K$ expression printed **$I_{D(NO)}$**; Example 63.13's quadratic denominator printed "**.2**" | $I_{D(ON)}$; 2 | scan noise |
| **C4.18** | p22 | the gain quoted as **$+48.9$** | $A_v = -48.9$, i.e. 48.9 with phase inversion | this is a **common-source** stage, and the chapter's own expression (p12) is $A_v = -g_m(r_d \parallel R_L)$ |
| **C4.19** | p23 | "As shown in **Fig. 13.37**, some MOSFETs have back-to-back Zener diodes" | Fig. **63**.37, on the same page | chapter-number typo |
| **C4.20** | p23 | the problem quotes $V_{GS(off)} = 5$ V, **positive** | $-5$ V | for an N-channel depletion device $V_{GS(off)}$ is negative — p5's footnote and every other problem in both tutorial sets. The answer does not depend on it |
| **C4.21** | p22 | panel (a) of Fig. 63.36 does **not** draw the drain-feedback connection the solution assumes (*"Since drain is directly returned to gate, $V_{GS} = V_{DS}$"*) | read panel (a) as gate wired directly to the drain, $V_{GS} = V_{DS}$ | panel (b) draws its gate link explicitly and Fig. 63.38(a) on p23 draws the same link properly, so the omission is in this panel alone. The computed answers are unaffected — the text states the connection |

---

## L5 — Fabrication of Transistors and Integrated Circuits

23 pages, 21 flags. This is the course's only descriptive, non-numerical lesson, and its defects are
of a different kind: **process names and mechanisms stated wrongly**, rather than arithmetic. Two of
the nine substantive flags are self-contradictions the page makes with itself a paragraph or a page
apart.

### Substantive

#### V5.1 · "Flat zone" for float-zone ·L5 p3

**Printed:** the **"flat zone" process**, twice.

**Should read:**
$$\boxed{\;\text{float-zone (FZ) process: crucible-free, ultra-pure, high-power / high-voltage silicon}\;}$$

**Why.** A narrow molten zone is *floated* along a vertical polycrystalline rod by an RF coil, with
**no crucible touching the melt** — which is precisely why it yields the ultra-pure,
high-resistivity silicon that high-voltage, high-power devices need. "Flat zone" is not the name of
any process, and a reader who memorises it loses the reason behind the method.

#### V5.2 · "MPE" for molecular beam epitaxy ·L5 p12

**Printed:** *"molecular beam epitaxy (**MPE**)"*.

**Should read:** **MBE** — the initials of *Molecular Beam Epitaxy*.

**Why.** MPE corresponds to no deposition technique. Substantive in the exam sense: a student who
writes MPE has named a process that does not exist.

#### V5.3 · A false capability boundary between epitaxy and diffusion ·L5 p12

**Printed:** *"Epitaxy is used to deposit N or N$^+$ (i.e., heavily doped N-type) silicon, **which
is impossible to accomplish by diffusion**."*

**Should read:**
$$\boxed{\;\text{epitaxy is required when the new surface layer must be more \textit{lightly} doped than what lies beneath it, or doped independently of it}\;}$$

**Why.** This contradicts **the paragraph immediately above it on the same page**, which correctly
states that what diffusion cannot do is produce a surface layer of *lower* concentration. Heavily
doped N$^+$ regions are made by diffusion routinely — the N$^+$ emitter of the bipolar transistor on
p20 is diffused, not grown.

#### V5.4 · A resistance formula with no brackets in the denominator ·L5 p16

**Printed:** $R = \rho.l/a$ **or** $\rho.l/w.d$

**Should read:**
$$\boxed{\;R = \frac{\rho\,l}{w\,d}\;}$$

**Why — dimensional, in one line.** Read literally, $\rho l/w.d$ parses as $(\rho l/w)\cdot d$,
whose units are $\Omega\!\cdot\!\mathrm{cm^2}$, not ohms. The bracket is the difference between an
answer in ohms and an answer in $\Omega\!\cdot\!\mathrm{cm^2}$.

#### V5.5 · Contacts described on the wrong layer ·L5 p16

**Printed:** *"Notice the metallic contacts made **at the two ends of the epitaxial layer**."*

**Should read:** contacts are made at the two ends of the **diffused P-type resistor body**.

**Why.** Fig. 67.21(a) as rendered shows both contacts landing on the diffused P region; the N
epitaxial layer around it is not contacted at all. If it were, the resistor would be short-circuited
through the epi and the isolating junction defeated — the sentence as printed describes a structure
that would not work.

#### V5.6 · A capacitor argument that contradicts itself ·L5 p17

**Printed:** *"The combination film has a **lower** dielectric constant, allowing a capacitor area
**smaller** than a conventional silicon dioxide capacitor."*

**Should read:**
$$C = \frac{\varepsilon_0\varepsilon_rA}{t}\quad\Longrightarrow\quad A = \frac{C\,t}{\varepsilon_0\varepsilon_r}$$
$$\boxed{\;\text{the ONO film has a \textit{higher} dielectric constant, allowing a smaller capacitor area}\;}$$

**Why.** For a given $C$ and thickness $t$, a **smaller area requires a larger $\varepsilon_r$** —
the two halves of the printed sentence pull opposite ways. Silicon nitride has
$\varepsilon_r \approx 7$ against $\approx 3.9$ for silicon dioxide, so the oxide/nitride/oxide (ONO)
stack does have the higher constant, which is exactly why it is used.

#### V5.7 · The masking roles of oxide and nitride swapped ·L5 p21

**Printed:** *"**The silicon dioxide** permits selective oxidation so that a thick oxide (about
500 nm) can be formed in the field region."*

**Should read:**
$$\boxed{\;\text{the silicon \textit{nitride} permits selective oxidation, so thick field oxide grows only where the nitride is removed}\;}$$

**Why.** The same paragraph has already assigned the silicon dioxide its own job — *"to provide
stress relief to the wafer"*. In the LOCOS scheme being described, $\mathrm{Si_3N_4}$ is the
oxidation barrier: oxygen cannot diffuse through it. If the oxide were the barrier, the pad oxide
would block oxidation everywhere and no field oxide could grow at all.

#### V5.8 · Two figure panels that invert the comparison ·L5 p20

**Printed:** *"This path is considerably longer than the path in **the discrete BJT shown in
Fig. 67.26 (a)**."*

**Should read:**
$$\boxed{\;\text{Fig. 67.26(a) = IC transistor \textit{without} a buried layer (long path); (b) = the same device \textit{with} the N}^+\text{ buried layer (short path)}\;}$$

**Why.** The render of Fig. 67.26(a) shows a **planar integrated** transistor — E, B and C contacts
all on the top surface, an N collector region in a P substrate, and the long lateral carrier path
drawn in dashed arrows. That is the *long* path the paragraph is complaining about. In a genuine
discrete BJT the collector contact is the back face of the die, so the path is short and vertical,
and no such drawing appears anywhere in L5.

#### V5.9 · MOS speed answered both ways, one page apart ·L5 p22, p23

**Printed:** point 4 (p22) says the MOS transistor has the **better cut-off frequency and higher
bandwidth**; the paragraph closing the same article (p23) says *"the main disadvantage of MOS ICs is
their slower speed as compared to bipolar ICs"*, and that they do not compete in ultra-high-speed
applications.

**Should read:**
$$\boxed{\;\text{point 4 compares \textit{devices at equal channel length and base width}; the closing paragraph compares \textit{circuits as actually built}}\;}$$

**Why.** The reconciliation is buried in point 4's own qualifier and never stated. Substantive for
exam purposes: *"Is MOS faster or slower than bipolar?"* has two opposite answers in the source, and
a student must know which qualifier goes with which.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C5.1** | p1 | "the invention of the transistor in 1948 by W.H. Brattain and **I. Bardeen**" | **J.** Bardeen (John Bardeen) | the working point-contact device was demonstrated in December **1947** and announced in 1948, which is why both years are quoted; only the initial is wrong |
| **C5.2** | p2 | "**In Sb** and CdSe are used as light detectors" | **InSb** (indium antimonide) | a stray space splits the formula, making it read as two separate elements |
| **C5.3** | p3 | "silicon dioxide, which constitutes about **20 %** of earth's crust" | crustal abundances give a **silica-equivalent share of about 59 %**; **free silica** is about 12 % | oxygen ≈ 47 % and silicon ≈ 28 % by mass. The printed 20 % matches neither figure and should not be quoted as fact |
| **C5.4** | p4 | "The **seet** is rotated and pulled up very slowly" | seed | the same sentence uses "seed" correctly twice |
| **C5.5** | p4 | "the ingot surface is **grounded** throughout to an exact diameter" | **ground** (machined down) | an unfortunate homograph in an electronics text |
| **C5.6** | p4, p5 | Fig. 67.7's lower two panels captioned only "{100} P-type" and "{100} N-type" — the **(c) and (d) panel letters are missing** | (c) {100} P-type, (d) {100} N-type | the running text on p4 refers to "Fig. 67.7 (c)" and "(d)", so the cross-references dangle |
| **C5.7** | p6 | "The oxidizing agent may be *dry* by using dry oxygen **or be using** a mixture of water vapour and oxygen" | "or **wet** by using a mixture of water vapour and oxygen" | the word *wet* has dropped, and the dry/wet pair is then used twice more without ever being named |
| **C5.8** | p7 | Fig. 67.10's first curve labelled "**Predeposition**"; horizontal axis captioned "Depth into**-** substrate" | pre-deposition, as the body text has it; no hyphen | typesetting only |
| **C5.9** | p9 | Fig. 67.13 labels the accelerator supply "**180 KV**" | 180 **kV** | lower-case k is the prefix *kilo*; capital K is the kelvin. The **same figure prints "20 kV" correctly** two labels away |
| **C5.10** | p15 | Fig. 67.19 uses **LCC for two different packages** — "LCC (Leadless Chip Carrier)" at (k) and "LCC SOJ (Leaded Chip Carrier…)" at (l) | **LCC** for the leadless part; **LDCC** (or PLCC in plastic) for the leaded one | *leadless* and *leaded* sharing one abbreviation one line apart — a genuine notation clash, also recorded in `_nomenclature.md` |
| **C5.11** | p18 | "Then boron is diffused to form P-type region **a** shown in Fig. 67.24 (f)" | **as** shown | dropped letter |
| **C5.12** | p20 | "an aluminium film **0.5 and 1 µm** thick" | 0.5 **to** 1 µm | matches the range notation used for every other thickness on the page |

---

## L6 — h-Parameters and Small-Signal BJT Amplifiers

26 pages, 12 flags — **the cleanest lesson in the course**, and the only one whose substantive count
reaches single figures. It is also the only handwritten source, which shows in the cosmetic list:
struck-through words, carets and inserted corrections rather than OCR artefacts. Of the four
substantive faults, one (`V6.3`) happens to leave the numbers unchanged; the other three do not.

### Substantive

#### V6.1 · A dimensionless parameter defined as a resistance ·L6 p4

**Printed:**
$$h_{12} = h_r = \left.\frac{V_i}{I_o}\right|_{I_i=0}$$

**Should read:**
$$\boxed{\;h_r = \left.\frac{V_i}{V_o}\right|_{I_i=0}\;}$$

**Why — three checks.** (i) **Dimensions:** $V_i/I_o$ is in ohms, but $h_r$ must be dimensionless,
because in $V_i = h_iI_i + h_rV_o$ the term $h_rV_o$ has to be a voltage. (ii) **The constraint**
written alongside is $I_i = 0$, i.e. the *input* open; a ratio taken to $I_o$ would be constrained at
the output. (iii) **The page's own words:** it is called a *voltage* transfer ratio, and $V_i/I_o$ is
not a ratio of two voltages. The page's other three definitions are correct, so this is an isolated
slip of one subscript.

#### V6.2 · Both output equations self-referential ·L6 p7

**Printed:**
$$i_c = h_{fe}i_b + h_{oe}\,i_c \qquad i_c = h_{fb}i_e + h_{ob}\,i_c$$

**Should read:**
$$\boxed{\;i_c = h_{fe}i_b + h_{oe}v_c\;}\qquad\boxed{\;i_c = h_{fb}i_e + h_{ob}v_c\;}$$

**Why — three checks.** (i) **Dimensions:** $h_{oe}$ is in siemens, so $h_{oe}i_c$ has units
$\mathrm{A^2/V}$ and cannot be added to a current. (ii) **Self-reference:** the symbol left of the
equals sign reappears on the right. (iii) **The model:** $h_o$ is the output branch's admittance and
sits across the output port, so the current it carries is $h_o \times$ the port **voltage**. The CC
row on the same page is written correctly with $v_e$, and p6 and p9–p13 use the correct forms — the
slip is confined to p7.

#### V6.3 · A common-emitter parameter inside a common-collector formula ·L6 p10

**Printed:**
$$Z_i\big|_{CC} = h_{ie} - \frac{h_{fc}h_{rc}}{Y_L+h_{oc}}$$

**Should read:**
$$\boxed{\;Z_i\big|_{CC} = h_{ic} - \frac{h_{fc}h_{rc}}{Y_L+h_{oc}}\;}$$

**Why.** All four parameters in a configuration's formula must carry the same second subscript, and
the general result on this same page is $Z_i = h_i - h_fh_r/(Y_L+h_o)$ with a single parameter set.
**In this instance the numbers happen not to move**, because $h_{ic} = h_{ie}$ exactly (§6.15) — but
the same slip in a CB row would change the answer by a factor of about $\beta$. p13 prints the CC
result correctly with $h_{ic}$, so the two pages disagree.

#### V6.4 · An output admittance a hundred times too large ·L6 p23

**Printed:** $Y_o = 194\times10^{-5}\ \text{mho}$, i.e. $1.94\times10^{-3}$ S.

**Should read:** recomputing from the page's own formula and numbers,
$$Y_o = 25\times10^{-6} - \frac{(50)(2\times10^{-4})}{1800} = 25\times10^{-6}-5.556\times10^{-6}$$
$$\boxed{\;Y_o = 1.944\times10^{-5}\ \mathrm{S} = 19.44\ \mu\mathrm{S}\;}$$

**Why.** **The page contradicts itself on the very next line**, giving
$R_o = 1/Y_o = 51.42\ \mathrm{k\Omega}$ — and $1/(1.94\times10^{-3}) = 515\ \Omega$, not 51.4 kΩ. A
learner who carried $194\times10^{-5}$ into a power calculation would be out by $10^{4}$.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C6.1** | p4 | *"short circuit current gain"* with **"Forward"** inserted above the line with a caret | short circuit **forward** current gain | the inserted word sits above the line and is easy to miss when copying |
| **C6.2** | p5, p6, p7, p8 | the output element drawn as a **resistor zigzag** but labelled $h_o$ (or $h_{oe}$, $h_{ob}$, $h_{oc}$) | the branch **resistance** is $1/h_o$; p16 draws the same element labelled $1/h_{oe}$ | $h_o$ is an admittance in siemens. Every formula in the lesson uses it as an admittance, so nothing computed changes — but a reader redrawing the figure should write $1/h_o$ beside the zigzag |
| **C6.3** | p9 | heading *"Current Gain (or) Current Amplification $A_i$"* | $A_I$ | every equation on the page and the eighteen that follow use the upper-case subscript |
| **C6.4** | p11, p12 | the condition written **"$R_L = \infty$"** on a page whose every other load symbol is $Z_L$; $A_{VS}$ written with $R_L$ two lines after $A_V$ was written with $Z_L$ | one symbol, consistently | the lesson treats $Z_L = R_L$ throughout and p12 states this explicitly in a bracket |
| **C6.5** | p17 | *"the magnitude of voltage generated in the **emitter** circuit is $h_{re}\lvert V_c\rvert$…"* | the **base (input)** loop | the $h_{re}V_c$ source sits in the input loop of the CE model; the emitter is the common terminal and carries no such generator. The algebra that follows is correct |
| **C6.6** | p20 | heading *"output impedance $(Y_o)$"*, with **impedance struck through** and **admittance** written above it | output **admittance** $Y_o$, in siemens; $R_o = 1/Y_o$ is on the next line | as left on the page the label and the symbol disagree unless the correction is noticed |
| **C6.7** | p26 | closing statement *"$A_{VS}$, $A_{IS}$, $A_P$ are same as that of exact analysis"* | $A_{VS}$ and $A_{IS}$ are the same; **$A_P$ rises to 43.65** | recomputed with the approximate values ($A_V = 44.54$, $A_I = 0.98$, $R_i = 22\ \Omega$): $A_{VS} = 0.802$ ✓, $A_{IS} = 0.962$ ✓, but $A_P = 43.65$ against the exact 43.06 — **1.4 % higher**. The two overall gains are unchanged because the approximation moves $A_V$ up by the same factor it moves $R_i$ down, and the two cancel in $A_VR_i$; $A_P$ has no such cancellation |
| **C6.8** | p3, p5, p24, p26 | "Transiston" throughout p3; $V_i = f_1(I_l, V_o)$ with a letter l subscript; "Benifits"; "convinient"; "convertable"; "sepecify"; "Convension formulae"; "Convusion formulae" | transistor; $f_1(I_i,V_o)$; Benefits; convenient; convertible; specify; Conversion; Conversion | handwriting and transcription cluster; nothing computed changes |

---

## L7 — Multistage Amplifiers, Feedback and Frequency Response

27 pages, 48 flags — second only to L3, and the lesson with the highest proportion of **wrong
printed answers**: eleven of its twenty-two substantive flags are numerical results the page's own
next line contradicts. It is also where symbol collisions bite hardest, because feedback,
transformer coupling and frequency response each bring their own $R$'s and $f$'s into the same
worked example.

### Substantive

#### V7.1 · A solution worked with the next example's data ·L7 p4

**Printed:** the second line substitutes $\beta = 0.04$, $A = 100$, $V_i = 50$ mV — the data of
**Example 62.3**, printed immediately below.

**Should read:** this example's data are $A = 1000$, $\beta = 0.1$, and **no $V_i$ is given at all**:
$$1+\beta A = 1+0.1\times1000 = 101\quad\Longrightarrow\quad\boxed{\;V_i' = 101\,V_i\;}$$

**Why.** The input must be raised 101-fold, and a numerical answer is impossible without $V_i$.
Check on the exact gain: $A' = 1000/101 = 9.90$, which the $1/\beta = 10$ approximation matches.

#### V7.2 · A question that asks for the trivial quantity ·L7 p4

**Printed:** the question asks for *"the percentage fall in gain **without** feedback"*; the solution
computes the percentage fall in gain **with** feedback.

**Should read:** *percentage fall in gain **with** feedback*.

**Why.** Without feedback the fall is 20 % by hypothesis — the question as printed answers itself.
The solution, not the question, is the reliable half.

#### V7.3 · Two different gains both labelled $A_1$ ·L7 p6

**Printed:** equation (i) prints both results as $A_1$ —
*"$A_1 = \left(\frac{A}{1+A\beta_1}\right)^n$ and $A_1 = \frac{A^n}{1+A^n\beta_2}$"*.

**Should read:**
$$\boxed{\;A_2 = \frac{A^n}{1+A^n\beta_2}\;}$$

**Why.** The text one line above defines $A_2$ as *"the overall gain"* of Fig. 62.4(b), and three
lines below the page writes *"$A_1 = A_2$"* — meaningless if both are already called $A_1$.

#### V7.4 · A sign and a symbol lost from one side of an identity ·L7 p6

**Printed:** $(1 - 1\beta)^n = 1 + A^n\beta_2$

**Should read:**
$$\boxed{\;(1+A\beta_1)^n = 1+A^n\beta_2\;}$$

**Why.** The left side is mangled twice: the sign is minus where it must be plus, and "$1\beta$" is a
corrupted "$A\beta_1$". One-line check: the identity is simply $A_1 = A_2$ with $A^n$ cancelled from
both numerators. As printed the equality cannot hold even for $n = 1$.

#### V7.5 · A closed-loop gain the page's own decibel answer disproves ·L7 p7

**Printed:** $A_f = A/(1+\beta A) = 63/(1+6.3) = \mathbf{6.63}$ or **18.72 dB**.

**Should read:**
$$\boxed{\;A_f = \frac{63}{7.3} = 8.63 \equiv 18.72\ \mathrm{dB}\;}$$

**Why.** $63/7.3 = 8.63$, not 6.63 — and the page's own decibel figure proves it, since
$20\log_{10}8.63 = 18.72$ dB while $20\log_{10}6.63 = 16.43$ dB. Second check: in decibels the
closed-loop gain is $36 - 20\log_{10}(7.3) = 18.73$ dB.

#### V7.6 · A bandwidth identity that forces $BW = BW'$ ·L7 p8

**Printed:** $A(f_2-f_1') = A(f_2'-f_1')$

**Should read:**
$$\boxed{\;A\,(f_2-f_1) = A'\,(f_2'-f_1')\;}$$

**Why.** Two errors on one line: the left bracket should contain $f_1$, the *no-feedback* lower
cut-off, and the right-hand gain should be $A'$. As printed the equation says
$A\times BW = A\times BW'$, forcing $BW = BW'$ — the exact opposite of the section's own claim that
feedback widens the band.

#### V7.7 · A cut-off frequency printed in the wrong prefix ·L7 p9

**Printed:** $f_2' = f_0(1+\beta A) = 20(1+0.02\times200) = \mathbf{100\ Hz}$

**Should read:**
$$\boxed{\;f_2' = f_2(1+\beta A) = 20\ \mathrm{kHz}\times5 = 100\ \mathrm{kHz}\;}$$

**Why.** Two faults: the subscript should be $f_2$ (there is no $f_0$ in this problem), and $f_2$ is
20 **kHz**, so the answer is 100 kHz. The very next line and the gain–bandwidth check below it both
use 100 kHz.

#### V7.8 · $\beta A$ replaced by $A$ in a denominator ·L7 p12

**Printed:** $A' = \dfrac{A}{1+\beta A} = \dfrac{400}{1+400} = 9.756$

**Should read:**
$$\boxed{\;A' = \frac{400}{1+40} = 9.76\;}$$

**Why.** $\beta A = 40$ was computed three lines earlier. As printed the expression evaluates to
$400/401 = 0.998$, not the 9.756 beside it.

#### V7.9 · The feedback path attributed to the emitter resistor ·L7 p12

**Printed:** *"a portion of the output voltage is coupled through **$R_E$** in parallel with the
input signal at the base."*

**Should read:** coupled through **$R_F$**.

**Why.** $R_E$ is the emitter resistor, bypassed to ground in this very figure and carrying no
feedback. The element drawn from collector to base — and the one appearing in the section's own
result $\beta = R_C/R_F$ — is $R_F$.

#### V7.10 · Both terminals of Fig. 62.11 labelled $V_i$ ·L7 p12

**Printed:** the terminal at the lower left (correctly, the input) and the terminal at the upper
right, on the far side of the collector coupling capacitor, are **both labelled $V_i$**.

**Should read:** the upper-right terminal is the **output**, $V_o$.

**Why.** Every other figure in the chapter labels that terminal $V_o$.

#### V7.11 · A reflected load called the emitter resistance ·L7 p17–p18

**Printed:** *"$A_{e.2} = \dfrac{r_{0.2}}{r_{e.2}}$ where $\mathbf{r_{e.2}} = a^2R_7$"*.

**Should read:**
$$\boxed{\;r_{o.2} = a^2R_7\;}$$

**Why.** $a^2R_7$ is the load **reflected into $T_2$'s primary**, i.e. $r_{o.2}$ — it cannot also be
$r_{e.2}$, which the *same page* computes as $33.3\ \Omega$ from $50\ \mathrm{mV}/I_E$ while
$a^2R_7 = 25\ \mathrm{k\Omega}$. As printed the gain formula reads $A = r_{o.2}/r_{o.2} = 1$.

#### V7.12 · Capacitance said to be large at low frequency ·L7 p17

**Printed:** *"At low frequencies, the gain is low due to large **capacitance** offered by the
coupling capacitor."*

**Should read:** what is large at low frequency is its **reactance**,
$$\boxed{\;X_C = \frac{1}{2\pi fC}\;}$$

**Why.** A capacitor's capacitance is a fixed component value and does not depend on frequency. The
same section uses "reactance" correctly two lines later, for the high-frequency end.

#### V7.13 · An exponent dropped from a reflected load ·L7 p18

**Printed:** $A_{v.2} = \dfrac{25\times\mathbf{100}}{33.3} = 750$

**Should read:**
$$\boxed{\;A_{v.2} = \frac{25{,}000}{33.3} = 750\;}$$

**Why.** $25\times100 = 2500$ and $2500/33.3 = 75$, not 750. The numerator is
$r_{o.2} = a^2R_7 = 25\times10^{3}\ \Omega$ — the exponent has dropped out of "$25\times10^3$".

#### V7.14 · A turns ratio wrong by a factor of three ·L7 p19

**Printed:** *"For primary winding $0.4 = 10^{-5}N_p^2\times5$ or $N_p = \mathbf{632}$"*, closing
*"it is a nearly **7 : 1** step-down transformer."*

**Should read:**
$$\boxed{\;N_p = 200,\quad N_s = 89,\quad \frac{N_p}{N_s} = 2.25\;}$$

**Why.** With the page's own $k = 10^{-5}$, $N_p = \sqrt{0.4/10^{-5}} = 200$; the printed 632 is
$\sqrt{0.4/10^{-6}}$, i.e. it silently uses $k = 10^{-6}$ — inconsistent with the secondary, which
*was* computed from $k = 10^{-5}$ ($N_s = \sqrt{0.08/10^{-5}} = 89$). The stray "$\times5$" has no
meaning. **Independent check:** a matching transformer's turns ratio is
$\sqrt{Z_p/Z_s} = \sqrt{5000/1000} = 2.24$, which is $200/89$, not $632/89 = 7.1$.

#### V7.15 · A corner frequency the page later contradicts ·L7 p24

**Printed:** part (i) answer **40 Hz**.

**Should read:** with $R_{eq} = 11.26$ kΩ and $C_1 = 1\ \mu$F,
$$\boxed{\;f_1\big|_{C_1} = \frac{1}{2\pi(11{,}260)(10^{-6})} = 14.1\ \mathrm{Hz}\;}$$

**Why.** Part (iii) of the same solution states *"cut-off for $C_1$ occurs way down at **14 Hz**"*.

#### V7.16 · A numerical answer missing from the page ·L7 p24

**Printed:** *"$f_1 = \dfrac{1}{2\pi\times20\times10^3\times0.2\times10^{-6}} = $ **Hz**"* — the
number has dropped out entirely.

**Should read:**
$$\boxed{\;f_1\big|_{C_2} = 39.8\ \mathrm{Hz}\approx40\ \mathrm{Hz}\;}$$

**Why.** The expression is complete; only the evaluated value is absent.

#### V7.17 · The lower cut-off taken as the minimum instead of the maximum ·L7 p24

**Printed:** *"Since cut-off frequency for $C_2$ occurs at 40 Hz while cut-off for $C_1$ occurs way
down at 14 Hz, $C_2$ determines the lower cut-off frequency for the amplifier i.e. **14 Hz**."*

**Should read:**
$$\boxed{\;f_1(\text{amplifier}) = \max\{14.1,\ 39.8\} = 39.8\ \mathrm{Hz},\ \text{set by } C_2\;}$$

**Why.** The sentence contradicts itself — it names $C_2$ as the determining capacitor and then
quotes $C_1$'s frequency. **Why the maximum:** each series capacitor is a high-pass section, so
going down in frequency the amplifier is already 3 dB down as soon as the *first* corner is met —
the **highest** of the individual corner frequencies.

#### V7.18 · A gain formula with the wrong symbol and the wrong value ·L7 p25

**Printed:** $A_v \cong \dfrac{\mathbf{R_E}}{r_e} = \dfrac{\mathbf{100\ K}}{50\ \Omega} = 200$

**Should read:**
$$\boxed{\;A_v \cong \frac{R_L}{r_e} = \frac{10\ \mathrm{k\Omega}}{50\ \Omega} = 200\;}$$

**Why.** Two faults on one line: the numerator symbol should be $R_L$ (the question says "circuit
**load** resistor"; $R_E$ appears nowhere in the problem), and the value should be **10 K** as given.
As printed the quotient is $100{,}000/50 = 2000$, ten times the printed answer. The answer
$C_{in} = 814$ pF is right, because it uses the correct $A_v = 200$.

#### V7.19 · A self-referential gain expression ·L7 p25

**Printed:** $A_v \cong \dfrac{R_C \parallel R_L}{\mathbf{R_L}} = \dfrac{20\mathrm{K}\parallel20\mathrm{K}}{400\ \Omega} = 25$

**Should read:**
$$\boxed{\;A_v \cong \frac{R_C \parallel R_L}{R_E} = \frac{10\ \mathrm{k\Omega}}{400\ \Omega} = 25\;}$$

**Why.** The 400 Ω used is the emitter resistor; $R_L$ is 20 K and already appears in the numerator,
so $\left(R_C\parallel R_L\right)/R_L$ would be 0.5, not 25.

#### V7.20 · The alpha cut-off frequency printed as $f_1$ ·L7 p27

**Printed:** $f_\beta = \dfrac{\mathbf{f_1}}{80} = \dfrac{8\ \mathrm{MHz}}{80}$

**Should read:**
$$\boxed{\;f_\beta = \frac{f_\alpha}{\beta} = \frac{8\ \mathrm{MHz}}{80} = 100\ \mathrm{kHz}\;}$$

**Why.** $f_1$ is the **lower cut-off frequency** throughout this chapter (§60.42, §60.45, Ex 60.20).
The quantity divided here is the alpha cut-off frequency $f_\alpha = 8$ MHz, the only 8 MHz in the
problem. The relation is $f_\alpha \cong \beta f_\beta$ rearranged.

#### V7.21 · A noise power quoted as the signal power ·L7 p27

**Printed:** answer key **[5 mW]**.

**Should read:** **5 µW**.

**Why.** 5 mW is the *signal* power; as printed the noise would be 0 dB below the signal,
contradicting the question. Compare Q1, whose answer key correctly applies the same factor of 1000
in the other direction.

#### V7.22 · An **input** power out by a factor of 1000 ·L7 p27

**Printed:** answer key **[72 µW]**.

**Should read:** **72 mW**.

**Why.** $72\ \mu$W would require a power gain of
$10\log_{10}\!\left(72/72\times10^{-6}\right) = 60$ dB, not the 30 dB the question specifies.

### Cosmetic

| ID | Page | Printed | Should read | Why |
|---|---|---|---|---|
| **C7.1** | p2 | Fig. 62.2's in-figure caption "**Feeback** Loop" | Feedback Loop | spelling; the figure is otherwise correct |
| **C7.2** | p4 | $A' = 10\ \mathrm{V}/251\ \mathbf{mA} = 40$ | 251 **mV** | the line above states it as a voltage; the number 40 is right ($10/0.251 = 39.84$) |
| **C7.3** | p4 | $400/4.2 = 95.3$, hence a fall of 4.7 % | $400/4.2 = 95.238$, a fall of **4.76 %** | rounding only |
| **C7.4** | p5 | "After amplification, it become $\beta x D_A$" | $\beta x D A$ | $A$ is a **factor**, not a subscript; the next line uses it correctly |
| **C7.5** | p7 | the solution labels the distortion "(a)" and the gain "(b)" | the question asks (a) gain of the first stage, (b) second harmonic distortion | both answers are correct; only the part labels are transposed |
| **C7.6** | p7 | the statement gives the second stage's forward gain as **$-150$**; the solution uses $+150$ | either, stated | defensible — the minus is the CE stage's phase inversion, which is *what makes the feedback negative*, and the $(1+\beta A)$ form assumes it — but the page never says so. $A/(1-\beta A)$ with the signed value gives $150/(1+15)$, the same 9.38 |
| **C7.7** | p8 | "$A' = \frac{200}{1+0.02\times200} = $ **40 Hz**" | 40, dimensionless | a voltage gain is a pure number; the Hz is imported from the frequency working that follows |
| **C7.8** | p9 | the bandwidth written **$dW$** and **$dW'$** throughout the example | $BW$ and $BW'$ | $dW$ is not a bandwidth symbol anywhere else in the chapter; §60.42 uses $\Delta f$ or $BW$ |
| **C7.9** | p12 | $10{,}000/(\mathbf{20}+1000)$ | $10{,}000/(25+1000) = 9.756$ | $r_e = 25\ \Omega$ was established on the previous page, and 1025 gives the printed answer; 1020 would give 9.804 |
| **C7.10** | p12 | the question asks for "$I_{o(\text{stage})}$", a **current**; the solution computes an output **resistance** | $r_{o(\text{stage})}$ | symbol/quantity mismatch in the question only |
| **C7.11** | p13 | $A_f = 7360/819 = \mathbf{8.9}$ | $8.986$, i.e. **9.0** | arithmetic slip in the last digit |
| **C7.12** | p15 | in Fig. 61.1 the **input** terminal of the second stage labelled $v_{o2}$; the right-most label $v_{o3}$ clipped by the frame | $v_{i2}$, by the figure's own $v_{i1}\ldots v_{i3}$ pattern | $v_{o2}$ then correctly appears again on that stage's output |
| **C7.13** | p16 | the two photographs have **swapped captions** — the rack-mounted instrument captioned "Modern coupling transformer", the tray of wound iron-cored components captioned "R.C. Coupled two-stage amplifier" | exchange them | neither caption belongs to the picture above it |
| **C7.14** | p17 | disadvantage 3: "not as good as those of **BC** coupling" | **RC** coupling | there is no "BC coupling"; the rest of the section confirms it |
| **C7.15** | p17 | Fig. 61.13's horizontal axis labelled **$t$** | **$f$**, on a logarithmic scale | the text has just described it as *"the frequency versus gain curve"*; read as gain against frequency |
| **C7.16** | p17 | "gain drops **of** again" | drops **off** again | typo |
| **C7.17** | p18 | the gain printed **$A_{e.2}$** | $A_{v.2}$ | every other occurrence in the section and in the worked example uses $A_{v.2}$ |
| **C7.18** | p18 | part (i) "$\cong$ **830**" | $27{,}750/33.3 = 833.3$ | the 830 is carried into part (iii); using 833 throughout gives $A_v = 625{,}000$ and $G_v = 115.9$ dB — the same 116 dB. Rounding only |
| **C7.19** | p19 | "$10\times10^{-6} = k\times\mathbf{12^2}$" | $k\times1^2$ | the turns number substituted is $N = 1$; the printed "12" is a corrupted "1". The resulting $k = 10^{-5}$ is right |
| **C7.20** | p20 | "Because of **his** distortion" | this | typo |
| **C7.21** | p22 | the unit printed "$\mathrm{dB_{in}}$" | $\mathrm{dBm}$ | the line immediately above defines the abbreviation as dBm, *"indicating that it uses 1 mW as a reference"* |
| **C7.22** | p23 | "$f = f_2-f_1 = $ band width (BW) = passband" | $\Delta f = f_2-f_1$ | the $\Delta$ has dropped out of the rendered glyph, leaving a plain $f$ on the left of an equation whose right side is a *difference* of two $f$'s |
| **C7.23** | p24 | "$R_{er} = 3\mathrm{K}+\ldots$" | $R_{eq}$ | the symbol defined and used everywhere else |
| **C7.24** | p25 | the question lists "$C_b = 10$ pF" | $C_{be}$, as §60.44 defines and the solution uses | missing subscript |
| **C7.25** | p27 | "=100 **kHZ**" | kHz | capital Z |
| **C7.26** | p26 | section heading "Relation Between $f_a$, $f_b$ and $f_T$" with Latin **a** and **b** | $f_\alpha$, $f_\beta$, as the body text has them | Greek-to-Latin substitution in the heading font |

---

## Worst offenders — the errors most likely to cost marks

Re-picked across **both** tiers. Ranked by *exam exposure*: how likely the defect is to be copied
without noticing, multiplied by how much of an answer it destroys once it has been — and now also
adjusted for whether **the other source settles it**. A flag the second tier corrects is still worth
recognising on the page, but it is no longer an open question; a flag with **no second source** is
the dangerous kind.

| Rank | Flag | Where | What goes wrong if it is absorbed | Settled by the other tier? |
|---|---|---|---|---|
| **1** | `JV7.2` + `JV7.3` | ·J p91 | **A whole page about the wrong device.** The enhancement-only MOSFET is illustrated with the DE MOSFET's static characteristics — $I_{DSS}$, a conducting $V_{GS} = 0$ curve, a depletion mode — and described with the JFET's operating narrative, verbatim. Every one of those features is absent from the device the page names, and the page's own equation says so | **Yes** — ·L4 p20, Fig. 63.30 |
| **2** | `V1.3` | ·L1 p7–p8 | The $-1$ printed **inside** the exponent of the diode equation, in **all four** highlighted forms on one page and again in a worked example. Every diode current is wrong at every bias, and at $V = 0$ an unbiased diode passes $0.368I_0$ | **Yes** — ·J p35 has it outside |
| **3** | `V3.1` | ·L3 p4 | $\alpha = I_E/I_C$ — the defining ratio of the transistor, printed upside down, two lines from the page's own correct definition. Everything downstream ($\beta$, $I_C$, $I_{CEO}$) inverts with it | **Yes** — ·J p60 and ·J p63, both correct |
| **4** | `JV4.6` | ·J p36, p39, p40 | The dc load line's **current-axis intercept taken as $V_{Th}/R_{Th}$**, omitting the series load. Stated once, restated on a second page and used numerically on a third — 0.2 A against the correct 23.5 mA, a factor of **8.5**, and it moves the Q point badly | **No.** ·L1 never draws a load line at all |
| **5** | `JV7.1` / `V4.2` | ·J p85–p87 **and** ·L4 p4–p15 | $V_P$ used with **both signs**, in **both sources**, with nothing on either page to resolve it. Sign-flip Shockley's equation and $I_D$ comes out larger than $I_{DSS}$ — impossible, and easy to write down under time pressure | **No — the same inherited defect twice.** Neither source can settle it |
| **6** | `V2.8` | ·L2 p7 | PIV $= 2V_{sm}$ quoted for a **half-wave** rectifier. It is the centre-tap answer, and the same handout states PIV $= V_{sm}$ two pages earlier. A named-topology fact of exactly the kind a CAT asks for in one mark | **No.** ·J mentions PIV only as a diode rating and never computes it |
| **7** | `V3.12` | ·L3 p15 | A bias formula labelled $I_E$ that is really $I_B$, with $R_B$ replaced by $R_E$ in the denominator — so the printed expression contains **no base resistor at all**. Straight into every emitter-bias calculation | **Partly** — ·J p71 prints the exact form correctly |
| **8** | `JV3.6` + `JV3.7` | ·J p32 | The signature fault of the lecture notes, twice in four lines of one example: a **dropped zero** then an **added zero**, each in a denominator, each producing a printed answer that is right. A reader following the working gets 40 V and 0.9 A instead of 4 V and 0.09 A | **No.** No lesson document covers transformers |
| **9** | `JV6.8` | ·J p64 | The silicon and germanium leakage-doubling temperatures printed **both ways round on one page**. Whichever the reader memorises, a thermal-runaway question has a 50 % chance of coming out inverted, and the two differ by $2^{5}$ against $2^{3}$ over a 30 °C rise | **Partly** — `11-diodes.md` works a problem on Ge doubling every 10 °C |
| **10** | `V7.17` | ·L7 p24 | The amplifier's lower cut-off taken as the **minimum** of the individual corner frequencies instead of the **maximum**, in a sentence that contradicts itself mid-clause. Reverses the answer to the most-asked frequency-response question in the lesson | **No.** ·J has no frequency-response material |
| **11** | `JV7.10` | ·J p97 | $V_{GS(\text{off})}$ printed where $V_{GS(\text{th})}$ belongs, in an **exercise**. It sends the reader to Shockley's equation, for which the question supplies no $I_{DSS}$ — and the printed 1.44 mA is only reachable by reading the label as *threshold* | **Yes** — ·L4 p21 labels it correctly |
| **12** | `V6.2` | ·L6 p7 | Both CE and CB **output** h-parameter equations printed with $i_c$ where $v_c$ belongs — dimensionally impossible and self-referential. The whole small-signal model rests on those two lines | **No.** ·J p61 gives the h-parameter *symbols* but not the model equations |
| **13** | `JV6.13` | ·J p80 | *"If $R_{B2} = \infty$ then the transistor is off"* — it saturates. A fault-finding question answered from this sentence is answered backwards, and fault-finding is cheap to examine | **No.** ·L3 has no fault-finding section |
| **14** | `JV4.2` + `JV4.3` | ·J p35 | Boltzmann's constant as $1.38\times10^{-28}$ (a factor of $10^{5}$), and the diode equation's exponent typeset as a **denominator** — on one page, in the two lines a reader copies to memorise the diode equation | **Yes** — ·L1 p3 and p6–p7 |
| **15** | `V2.7` | ·L2 p6 | The half-wave TUF derivation loses a factor $\pi$ **twice**, and the two slips cancel in the final number — so the printed 0.287 certifies a derivation wrong in both intermediate steps. The exam risk is a derivation question, not a numerical one | **No.** ·J does not derive TUF |

**The pattern behind the list.** Eleven of these fifteen are *not* conceptual misunderstandings —
they are single characters: a bracket, a prefix, a minus sign, a subscript, an exponent, a zero. The
four that are conceptual (`JV7.2`/`JV7.3`, `V2.8`, `JV6.13` and the $V_P$ collision) are all cases of
**the right statement attached to the wrong device or topology**.

**And the newer pattern.** Only **seven of the fifteen are settled by the other source**. The rest
sit in material one tier covers and the other does not — transformers, load lines, PIV,
frequency response, fault-finding, TUF — which is exactly where a reader has no second opinion and
must rely on the check rather than on a cross-reference.

That is the argument for reading this course with the **four cheapest checks in the log** always
running:

1. **Dimensions.** Does every term on both sides carry the same units?
2. **Self-reference.** Does the left-hand symbol appear on the right?
3. **The next line.** Does the page itself use the number it just printed?
4. **The middle line.** Does the printed expression, evaluated exactly as written, give the answer
   printed under it? — the one check that catches the eighteen tier-1 flags of family §10, which
   nothing else catches at all.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
