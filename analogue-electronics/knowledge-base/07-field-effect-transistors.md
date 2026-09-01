---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "07 — Field Effect Transistors"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 84-100"
pages: "J p84-p100"
tier: primary
file_role: topic
subtopics:
  - "what a FET is; the two families (JFET, MOSFET) and the two channel types"
  - "JFET construction, terminals and circuit symbols, N- and P-channel"
  - "JFET operation in four cases: V_DS = 0, V_DS increasing, V_GS negative, both"
  - "pinch-off, I_DSS, the pinch-off voltage V_P and the cut-off voltage V_GS(off)"
  - "the V_P sign convention used by these notes, and where it breaks"
  - "JFET drain characteristic: ohmic, pinch-off/saturation, breakdown and cut-off regions"
  - "Shockley's square-law equation"
  - "JFET transfer characteristic and its two anchor points"
  - "MOSFET / IGFET: the two types; DE MOSFET construction and symbols"
  - "DE MOSFET depletion-mode and enhancement-mode operation"
  - "DE MOSFET static and transfer characteristics"
  - "enhancement-only N-channel MOSFET (NMOS): construction, inversion layer, threshold voltage"
  - "the E-MOSFET square law I_D = K(V_GS - V_GS(th))^2 and its characteristics"
  - "device parameters considered when purchasing JFETs and MOSFETs"
  - "JFET dc biasing: separate supply, self-bias, source bias, voltage-divider bias"
  - "worked example: self-bias giving V_DS = 4 V"
  - "worked example: divider bias giving V_GSQ = -1.8 V and V_DSQ = 12.5 V"
  - "biasing E-only MOSFETs: drain-feedback bias and voltage-divider bias"
  - "worked example: E-MOSFET divider bias giving V_DS = 9 V; exercise giving I_D = 1.44 mA"
  - "FET amplifiers: DE MOSFET stage and E-MOSFET stage, and the signal swing"
  - "FET configurations: common source, common drain, common gate — terminal parameters and gains"
  - "applications of FETs"
key_equations: [jfet-channel-ohm-j, shockley-j, emosfet-square-law-j, emosfet-k-from-idon-j, fet-supply-loop-j, gate-bias-j, self-bias-j, source-bias-j, divider-bias-j, drain-feedback-bias-j, cs-gains-j, cd-gains-j, cg-gains-j]
prerequisites:
  - "P-N junction, depletion layer, reverse bias (·J p33 onward; 04-diodes.md §4.2, §4.4)"
  - "the bipolar junction transistor and its biasing (·J p60-p83; 13-bipolar-junction-transistor.md)"
  - "dc load line and Q point (04-diodes.md §4.8; 13-bipolar-junction-transistor.md)"
leads_to:
  - "small-signal FET parameters r_d, g_m, mu — NOT in this range; see 14-field-effect-transistors.md §4.8"
  - "FET amplifier gain expressions in terms of g_m — NOT in this range; see 14-field-effect-transistors.md §4.12"
  - "MOS fabrication and integrated circuits (15-fabrication-and-integrated-circuits.md)"
verification_flags: 19
tags: [fet, jfet, mosfet, igfet, de-mosfet, e-mosfet, nmos, unipolar, pinch-off, shockley-equation, square-law, idss, threshold-voltage, inversion-layer, biasing, self-bias, source-bias, voltage-divider-bias, drain-feedback-bias, common-source, common-drain, common-gate, transfer-characteristic, drain-characteristic]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·J pN = provenance (which PDF page of the lecture notes the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ REDACTED = text destroyed by an opaque block in the source PDF ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 07 — Field Effect Transistors

Scope: **·J p84–p100**, the last seventeen pages of the course's own lecture notes, and the point at
which the document stops. Builds the junction FET from its two gate junctions, works the four
operating cases that produce pinch-off, reads both static characteristics, states Shockley's square
law, then crosses to the MOSFET family — DE MOSFET and enhancement-only NMOS, construction,
operation and characteristics — and finishes on **biasing**, which is where the numbers are: four
JFET bias schemes, two E-MOSFET bias schemes, three worked examples and one exercise. It closes with
the three amplifier configurations, listed as terminal parameters rather than gain formulas, and a
bulleted application list.

**This range is the course's only treatment of the FET at first hand.** Everything in it is
examinable. What it does *not* contain — the small-signal parameters $r_d$, $g_m$ and $\mu$, the FET
load line, and the gain expressions built from $g_m$ — is set out in §7.23 with a pointer to the
tier-2 file that does carry them.

---

## 7.0 Citation, the $V_P$ convention, and where this range's gaps are

**Citation.** `·J p91` means **PDF page 91**. The document's own printed page number runs **one
behind the PDF page** — PDF p91 shows printed "90" — and that offset holds unbroken across the whole
document. Everything below cites **PDF pages only**.

### ⚠ Read this before substituting anything into Shockley's equation

These notes use the symbol $V_P$ in **one** place as a definition and in **one** place as an equation
denominator, and the two usages contradict each other.

**The definition (·J p85, and the ·J p86 figure).** $V_P$ is the value of **$V_{DS}$** at which the
channel pinches off:

> "the channel is said to be pinched off and the corresponding value of $V_{DS}$ is called pinch off
> voltage $(V_P)$" — ·J p85

and on the drain characteristic of ·J p86, $V_P$ is a **tick on the horizontal $V_{DS}$ axis**,
between the ohmic region and the pinch-off region. On that reading **$V_P$ is a positive number**.

**The equation (·J p87).** Shockley's equation is printed twice on the same page, first with $V_P$ in
the denominator and immediately again with $V_{GS(\text{off})}$ in the denominator — asserting
$V_P = V_{GS(\text{off})}$. For an N-channel JFET $V_{GS(\text{off})}$ is **negative**.

**Both cannot be true.** The rule this file uses, everywhere, without exception:

> ### The working rule for this file
>
> 1. **In Shockley's equation the denominator is $V_{GS(\text{off})}$** — negative for an N-channel
>    JFET, positive for a P-channel one. Never substitute a positive $V_P$ there.
> 2. **On a drain characteristic, $V_P$ is a positive point on the $V_{DS}$ axis** — it is a value of
>    $V_{DS}$, not of $V_{GS}$. Ask which axis the number lives on.
> 3. The two are equal in **magnitude**: $\;|V_P| = |V_{GS(\text{off})}|$.
>
> **One-line self-check.** A device with $|V_P| = 4\ \mathrm{V}$ biased at $V_{GS} = -1\ \mathrm{V}$:
> with the negative denominator, $I_D = I_{DSS}(1-0.25)^2 = 0.5625\,I_{DSS}$ — sensible. With the
> positive one, $I_D = I_{DSS}(1+0.25)^2 = 1.5625\,I_{DSS}$ — **bigger than $I_{DSS}$, which is
> impossible.** If an answer ever exceeds $I_{DSS}$, the sign is wrong.

Flagged as **JV7.1**; see §7.5. The tier-2 file `14-field-effect-transistors.md` flags exactly the
same collision in its own source (**V4.2**), which is worth knowing: it is a defect of the textbook
tradition these notes are drawn from, not a one-off slip.

### The section starts without a heading ⚠

**·J p84 opens the FET material with no top-level heading.** The preceding page, ·J p83, finishes the
BJT chapter with a stability-factor calculation and two unsolved problems; ·J p84 then begins
directly with the bullet "Generally FET is a 3-terminal unipolar solid state device…". The first
heading on the page, **JUNCTION FIELD EFFECT TRANSISTOR**, sits below four introductory bullets that
are plainly about FETs in general, not about JFETs. A chapter heading was therefore present and has
been lost. **No heading is invented here** — this file's own title is editorial.

### Three more headings lost at page breaks

| Page | What is missing | Evidence |
|---|---|---|
| ·J p85 | the sub-heading **"a) When $V_{DS} = 0$"** | the page opens with the $V_{DS}=0$ construction figure and the bullet "Since $V_{DS}=0$ the drain current $I_D=0$…", and the *next* sub-heading on the same page is lettered **b)**. The letter **a)** never appears |
| ·J p94 | the sub-heading **"c) Source biasing"** | ·J p93 ends inside **b) Self biasing**; ·J p94 opens with the source-bias figure and the next heading on it is **d) Voltage divider biasing**. The letter **c)** never appears |
| ·J p95 | the label **"Example"** above the first worked problem | the page opens "Find the values of $V_{DS}$ in the circuit below if…"; the second problem on the same page *is* labelled **Example** |

None of these is a redaction block — there is no coloured bar, only white space. They are page-break
casualties. Recorded, not filled.

### Opaque redaction blocks in this range

Three pages carry solid yellow blocks over text. **There is nothing underneath** — contrast recovery
on the blue channel returns solid fill, so the text is destroyed, not hidden. Each is marked
`⚠ REDACTED` at the point of use.

[table] **Redaction map for ·J p84–p100** (page image is 1653 px wide; body text runs x = 237 → 1165,
about 11.6 px per character)

| Page | Blocks | Widths (px) | ≈ characters | What the sentence needs | Recovered? |
|---|---|---|---|---|---|
| ·J p87 | 2 | 445, 319 | ≈ 38, ≈ 27 | the names of the **two types of MOSFET** | **yes, with high confidence** — see §7.7 |
| ·J p88 | 2 (one bullet, two lines) | 929, 683 | ≈ 139 total | a construction bullet between "the gate is insulated … by … silicon dioxide" and "Silicon dioxide and the channel form a parallel plate capacitor" | **no** — see §7.7 |
| ·J p89 | 2 (one bullet, two lines) | 929, 437 | ≈ 118 total | a bullet commenting on the DE MOSFET **static characteristics** figure | **no** — see §7.9 |

### One clipped line

⚠ ILLEGIBLE ·J p97 — the **top line of the page is clipped by the page margin**: the two numerators
of the divider expression are cut away, leaving
$V_{R_2} = \dfrac{\;\;\;}{R_1+R_2}\times R_2 = \dfrac{\;\;\;}{9+6}\times 9 = 15\ \mathrm{V}$.
This is the overflow of the example begun on ·J p96, and both missing numerators are recoverable with
certainty from that page's data and from the arithmetic: they are $V_{DD}$ and $25$, since
$25\times9/15 = 15$ exactly. Nothing is lost. Logged as **JC7.6**.

### The document ends mid-topic

**·J p100 is the last page of the document.** It carries the tail of the common-gate parameter list
and then a five-item bulleted section, *Applications of FETS(s)*, ending "…because they come in small
sizes." There is **no summary, no tutorial problem set, no objective test, no reference list and no
closing page** — the file simply stops. Roughly two-thirds of ·J p100 is blank.

That matters for revision planning: the FET material has **three worked examples and one exercise in
total**, all of them in the biasing section, and no end-of-chapter question bank at all. §7.24 says
where to go for practice.

---

## 7.1 What a FET is ·J p84

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| D, G, S | drain, gate, source terminals | — | — |
| $I_D$ | drain current | A (usually mA) | 1–20 mA |
| $I_G$ | gate current | A | $\approx 0$ (pA–nA) |
| $I_S$ | source current | A (usually mA) | $= I_D$ since $I_G \approx 0$ |
| $V_{DS}$ | drain-source voltage | V | 5–20 V |
| $V_{GS}$ | gate-source voltage | V | $0$ to $-6$ V (N-channel JFET) |
| $V_{DD}$ | drain supply voltage | V | 12–25 V |

[def] A **field effect transistor** is a **3-terminal unipolar solid-state device in which the
current is controlled by an electric field**. ·J p84

Two words in that definition carry the whole difference from a BJT:

- **unipolar** — one carrier type does the conducting (electrons in an N-channel device, holes in a
  P-channel one), where a BJT uses both;
- **electric field** — the controlling quantity is a **voltage**, not a current.

[table] **The FET family, as these notes set it out** ·J p84

| Split | Members |
|---|---|
| by gate construction | **Junction FET (JFET)** · **Metal-oxide-semiconductor FET (MOSFET)** |
| by channel type | **P-channel** · **N-channel** — *both* families come in both types |

[added] Because $I_G \approx 0$, the source and drain currents are equal in every calculation in this
range: $I_S = I_D$. The notes use the two symbols interchangeably in the bias equations, and that is
why.

---

## 7.2 JFET construction, terminals and symbols ·J p84

[fig ·J p84] **Two construction diagrams side by side, each with its circuit symbol.**

*Fig (a): N-channel.* A tall rectangle of **N-type** material labelled "N-channel", standing
vertically. A lead leaves the top face to a terminal **Drain (D)**; a lead leaves the bottom face to
**Source (S)**. Two small squares marked **P** are embedded in the left and right faces at
mid-height; they are joined by a wire that leaves to the right as **Gate (G)**, annotated
**"(Always reverse biased)"**. To the right of the block sits the **N-channel circuit symbol**: a
vertical channel line with D at the top and S at the bottom, and a gate lead entering from the left
with its **arrow pointing in towards the channel**, the whole enclosed in a circle.

*Fig (b): P-channel.* Identical geometry with every type letter interchanged — a **P-channel** block
with two embedded **N** squares tied to the gate — and the symbol's gate **arrow pointing outwards**,
away from the channel.

How it is made and named: ·J p84

1. An N-channel is fabricated by **diffusing two P-type junctions into opposite sides of an N-type
   bar**.
2. Those junctions are **two P-N diodes, called the gates**; the material between them is the
   **channel**.
3. The two P regions are **connected internally** and one lead is brought out — the **gate terminal**.
4. **Direct (ohmic) connections** are made at the two ends of the bar: one end is the **source**, the
   other the **drain**.

> [added] **Reading the symbol.** The gate arrow points the way the gate-channel junction would
> conduct if it were ever forward biased — **in** for N-channel, **out** for P-channel. It never is
> forward biased in normal operation, which is exactly why the notes annotate the gate "always
> reverse biased".

---

## 7.3 JFET operation — the four cases ·J p84–p86

Two rules govern everything that follows: ·J p84

- The gates are **always reverse biased**, so the gate current $I_g$ is **practically zero**.
- The **source** is always connected to the end of the drain supply **that provides the necessary
  charge carriers** — negative for an N-channel device, since electrons are the carriers.

The notes then work an **N-channel JFET** through four cases, changing $V_{GS}$, $V_{DS}$ or both.

> **Note the missing sub-heading.** ·J p85 opens straight into case (a) with no letter — see §7.0.
> The case letters below are supplied to keep the sequence readable; **b)**, **c)** and **d)** are the
> notes' own.

### (a) $V_{GS} = 0$ and $V_{DS} = 0$ ·J p85

[fig ·J p85] **Construction diagram, no supplies.** The same N-block as ·J p84 with D at the top and
S at the bottom, the two P gate regions tied out to the right as **Gate (G)**. A **dashed outline**
is drawn around each P region and arrowed **"Uniform depletion layer"**.

With no drain voltage there is no drain current, and with no gate voltage there is no external
reverse bias, so:

- $V_{DS} = 0 \Rightarrow I_D = 0$;
- the depletion regions around the two P-N junctions are **equal in thickness and symmetrical**. ·J p85

### (b) $V_{GS} = 0$, $V_{DS}$ increased from zero ·J p85

[fig ·J p85] **The block wired into a circuit.** Same N-block, gate tied to the left through a source
marked $V_{GS}$, drain taken to the right-hand rail through a variable supply drawn as a battery with
an arrow through it, marked $V_{DD}$, with $V_{DS}$ marked as a long double-headed arrow across the
drain-source pair. $I_D$ is arrowed **downwards** through the channel from D to S. The two depletion
layers are now drawn as **curved wedges, wider at the drain end than at the source end**, arrowed
"Depletion layer".

The mechanism, in the notes' order: ·J p85

1. Electrons — the **majority carriers** — flow through the channel from source to drain.
2. That flow produces a **voltage drop along the channel resistance**.
3. That drop **acts as reverse bias at the gate**.
4. The gate is therefore **more negative with respect to points nearer the drain** than to points
   nearer the source, so **the depletion regions penetrate more deeply into the channel near the
   drain** — hence the wedge shape.

[eq: jfet-channel-ohm-j] While the channel is still behaving as a resistor: ·J p85

$$\boxed{\;I_D = \frac{V_{DS}}{R_{DS}}\;}$$

- $I_D$ — drain current, A
- $V_{DS}$ — drain-source voltage, V
- $R_{DS}$ — **[added]** the dc resistance of the channel between drain and source, $\Omega$. The
  notes use the symbol without defining it; it is the total source-to-drain channel resistance, and
  it **rises** as the depletion wedges close in.

Then: ·J p85

- As $V_{DS}$ rises, $I_D$ rises **to a maximum value $I_{DSS}$**, the saturation current.
- At that stage $I_D = I_{DSS}$ and is **constant**.
- The channel cross-section is at its **minimum**: the channel is **pinched off**, and the
  corresponding value of $V_{DS}$ is the **pinch-off voltage $V_P$**.
- Beyond $V_P$, **$I_D$ does not increase** — it stays constant until the JFET **breaks down**, when
  $I_D$ rises to an excessive value.

[def] $I_{DSS}$ — **drain current with the source shorted to the gate**, i.e. the saturated drain
current at $V_{GS}=0$. Units A (usually mA). It is the **largest current the device will pass** in
normal operation, and it is the sanity check on every Shockley calculation.

### (c) $V_{DS} = 0$, $V_{GS}$ decreased from zero ·J p86

[fig ·J p86] **The block with a gate supply.** As in (b), but the gate now returns through a variable
supply $V_{GG}$ drawn with an arrow through it, with $V_{GS}$ marked across gate-source. The two
depletion wedges have grown until they **meet in the middle**, and the meeting point is arrowed
**"Channel blocked"**.

- Making $V_{GS}$ **more negative** increases the gate reverse bias and therefore the **thickness of
  the depletion regions**. ·J p86
- At a sufficiently negative $V_{GS}$ the **two depletion regions touch** and the channel is **cut
  off**. ·J p86
- [def] The value of $V_{GS}$ that cuts the channel off is $V_{GS(\text{off})}$ — the
  **gate-source cut-off voltage**, V, **negative** for an N-channel JFET. ·J p86

### (d) $V_{GS}$ negative and $V_{DS}$ increased ·J p86

- As $V_{GS}$ is made more negative, **both $V_P$ and the breakdown voltage decrease**. ·J p86
- **N/B:** since the gate voltage controls the main current, a JFET is a **voltage-controlled
  device**. ·J p86
- A **P-channel JFET** works in exactly the same way except that the **channel carriers are holes**
  and the **polarities of both $V_{DD}$ and $V_{GS}$ are reversed**. ·J p86

> [added] **Why $V_P$ falls as $V_{GS}$ goes negative.** The junction needs a fixed total reverse
> bias — $|V_{GS(\text{off})}|$ — before the channel pinches. External bias and the channel's own
> $I_DR_{\text{channel}}$ drop **add**. Supply 1 V externally and the channel only has to supply the
> rest, so pinch-off arrives at a $V_{DS}$ that is 1 V lower. The relation, not printed in these
> notes but implied by the ·J p86 bullet, is
> $$V_{DS(P)} = |V_P| - |V_{GS}|$$
> and it is stated explicitly in the tier-2 file (`14-field-effect-transistors.md` §4.6).

---

## 7.4 JFET characteristics — the drain characteristic ·J p86–p87

Two characteristics are studied: ·J p86

1. **Drain characteristics** — $I_D$ against $V_{DS}$.
2. **Transfer characteristics** — $I_D$ against $V_{GS}$.

[fig ·J p86] **The drain characteristic, one curve, divided into three named spans.** Vertical axis
$I_D$, horizontal axis $V_{DS}$, origin marked 0. The curve rises **steeply and straight** out of the
origin to a knee marked **A**, bends over through **B**, and runs **flat** to **C**, where it turns
sharply upward. A tick on the $I_D$ axis marks $I_{DSS}$ at the level of the flat portion. **Dashed
verticals** drop from B and from C to the $V_{DS}$ axis, meeting it at **$V_P$** and **$V_A$**.
Across the top, three labelled spans with arrows: **"Ohmic region"** (origin to $V_P$),
**"Pinch-off region (Saturation)"** ($V_P$ to $V_A$), and **"Breakdown region"** (beyond $V_A$).

**Note where $V_P$ sits in this figure: on the horizontal $V_{DS}$ axis.** That is the definition
this file calls Usage A in §7.0.

### a) Ohmic region ·J p86

$I_D$ **varies directly with $V_{DS}$**, following Ohm's law: the transistor behaves like a
**resistor**. ·J p86

### b) Pinch-off / saturation region ·J p86–p87

This is the region Shockley's equation describes (§7.5). The notes add one line about it:

- "A transistor operated in this region is like a switch which is on." ·J p87

> ### [added] Read that line carefully
>
> A FET **conducting** is not the same as a FET used as a **closed switch**. In switching use the ON
> state is the **ohmic region**, where $V_{DS}$ is small and the device looks like a low resistance
> $R_{DS(\text{on})}$; the pinch-off region is where the device looks like a **constant-current
> source**, and it is the region used for **amplification**. The notes' sentence is best read as
> "conducting, as opposed to cut off". Nothing computed depends on it, but the distinction is worth
> holding onto, because the ohmic region is what makes a MOSFET useful as a logic switch (·J p100).

### c) Breakdown region ·J p87

Also called the **avalanche region**; $I_D$ **increases to an excessive value**. ·J p87

### d) Cut-off region ·J p87

- The region in which the transistor is **not conducting**, where $V_{GS} = V_{GS(\text{off})}$. ·J p87
- "A transistor operated in this region is like a switch which is off." ·J p87

[table] **The three faces of a JFET, in order of increasing $V_{DS}$** [added] — a compact way to hold
the drain characteristic

| Region | Behaves as | Used for |
|---|---|---|
| ohmic (below $V_P$) | a **resistor**, value set by $V_{GS}$ | voltage-controlled resistors; the ON state of a switch |
| pinch-off / saturation ($V_P$ to $V_A$) | a **constant-current source** | **amplification** — the normal operating region |
| breakdown (beyond $V_A$) | a near **constant-voltage** device | nothing; the device is being destroyed |

---

## 7.5 Shockley's equation ·J p87

[eq: shockley-j] The drain current in the pinch-off region. The notes print it **twice, on one line
each**, as: ·J p87

$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^{2}
\qquad\text{and}\qquad
I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_{GS(\text{off})}}\right)^{2}$$

The form to use, and the one to write in an examination:

$$\boxed{\;I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_{GS(\text{off})}}\right)^{2},
\qquad V_{GS(\text{off})} < 0 \text{ for an N-channel JFET}\;}$$

- $I_D$ — drain current in the pinch-off region, A
- $I_{DSS}$ — saturated drain current at $V_{GS}=0$, A
- $V_{GS}$ — gate-source bias, V (negative for an N-channel JFET)
- $V_{GS(\text{off})}$ — gate-source cut-off voltage, V (**negative** for an N-channel JFET)

The **square** is why FETs are called **square-law devices**.

> ⚠ VERIFY **JV7.1** ·J p85, p86, p87 — **the notes use $V_P$ with two opposite signs.** ·J p85
> defines $V_P$ as "the corresponding value of $V_{DS}$" at pinch-off, and the ·J p86 drain
> characteristic ticks $V_P$ on the **horizontal $V_{DS}$ axis** — so $V_P$ is a **positive** voltage.
> ·J p87 then prints Shockley's equation with $V_P$ and with $V_{GS(\text{off})}$ in the denominator
> of the same expression, which asserts $V_P = V_{GS(\text{off})}$ — a **negative** voltage for an
> N-channel device. Both cannot hold. **Correct form:** the denominator is the cut-off voltage,
> $$\boxed{\;I_D = I_{DSS}\left(1-\frac{V_{GS}}{V_{GS(\text{off})}}\right)^{2}\;}$$
> with $|V_P| = |V_{GS(\text{off})}|$ and $V_{GS(\text{off})} = -|V_P|$ for an N-channel JFET.
> **Why it matters:** substituting a positive $V_P$ for a negative $V_{GS}$ gives
> $I_D > I_{DSS}$, which is physically impossible. See `_verification-log.md`.

[table] **[added] Shockley sanity table** — $I_D/I_{DSS}$ for a device with
$|V_{GS(\text{off})}| = 4\ \mathrm{V}$, computed with the **correct** (negative) denominator

| $V_{GS}$ | $1 - V_{GS}/V_{GS(\text{off})}$ | $I_D/I_{DSS}$ |
|---|---|---|
| $0$ | $1$ | $1$ |
| $-1\ \mathrm{V}$ | $0.75$ | $0.5625$ |
| $-2\ \mathrm{V}$ | $0.50$ | $0.25$ |
| $-3\ \mathrm{V}$ | $0.25$ | $0.0625$ |
| $-4\ \mathrm{V}$ | $0$ | $0$ (cut off) |

*Every entry lies between 0 and 1. That is the check.*

---

## 7.6 The JFET transfer characteristic ·J p87

[fig ·J p87] **Transfer characteristic, drawn with the $I_D$ axis on the right.** The vertical $I_D$
axis stands at the **right-hand** end of the plot with **0** at its foot; the horizontal axis runs
**leftwards** and is labelled $V_{GS}$, with a tick at $V_{GS(\text{off})}$ part-way along. The curve
leaves the horizontal axis at $V_{GS(\text{off})}$ (zero current) and rises, **concave upward**, to
meet the vertical axis at a tick marked $I_{DSS}$. Printed inside the plot: **"$V_D$ = constant"**.

Its two anchor points, in the notes' own words: ·J p87

- when $V_{GS} = 0$, $\;I_D = I_{DSS}$;
- when $I_D = 0$, $\;V_{GS} = V_{GS(\text{off})}$.

and the curve "approximately follows the equation" — Shockley's equation again, this time printed
**only** in the $V_{GS(\text{off})}$ form. ·J p87

> [added] That is a useful piece of evidence for §7.0's working rule: **where the notes write the
> equation once and unambiguously, the denominator they choose is $V_{GS(\text{off})}$.**

> ⚠ VERIFY **JC7.1** ·J p87 — the figure's held-constant quantity is printed **"$V_D$ = constant"**.
> A transfer characteristic is taken at constant **drain-source voltage**, so it should read
> $V_{DS}$ = constant. $V_D$ elsewhere in this document (·J p93–p95) means the **drain node
> potential**, a different quantity. Cosmetic; nothing computed changes.
> See `_verification-log.md`.

---

## 7.7 MOSFET or IGFET, and DE MOSFET construction ·J p87–p88

[table] **Symbols added here**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| SS | **substrate** terminal (the fourth lead) | — | usually tied to the source |
| $\mathrm{SiO_2}$ | silicon dioxide — the gate insulator | — | film thickness ~100 nm |
| $V_{GS(\text{th})}$ | threshold voltage of an enhancement-only MOSFET | V | +2 to +5 V |
| $K$ | constant of the E-MOSFET square law | A·V⁻² (usually mA/V²) | 0.1–0.3 mA/V² |

[def] A **MOSFET** — metal-oxide-semiconductor FET, also called an **IGFET**, insulated-gate FET — has
its gate **insulated from the conducting channel** by an **ultra-thin oxide film of silicon dioxide**.
·J p87–p88

> ⚠ REDACTED ·J p87 — **two opaque blocks destroy the names of the two MOSFET types.** The sentence
> reads: "There are 2 types and are given by ▮▮▮▮▮ (≈38 characters) and ▮▮▮▮▮ (≈27 characters)."

> [added] **The covered names are recoverable with high confidence** — but they are our inference,
> not the notes' words. The very next heading on ·J p87 is **DE MOSFET**, defined there as the type
> that "can be operated both in depletion mode and enhancement mode by changing the polarity of
> $V_{GS}$"; the next major heading, on ·J p90, is **ENHANCEMENT ONLY N-CHANNEL MOSFET (NMOS)**. The
> two types are therefore the **depletion-enhancement (DE) MOSFET** and the **enhancement-only
> MOSFET**. The block widths — about 38 and 27 characters — fit "depletion enhancement MOSFET (DE
> MOSFET)" and "enhancement only MOSFET" closely. The *substance* is certain; the exact wording is
> not.

[def] **DE MOSFET** — "called so because it can be operated **both in depletion mode and in
enhancement mode** by changing the polarity of $V_{GS}$." ·J p87

### Construction ·J p88

[fig ·J p88] **Two construction diagrams with their circuit symbols.**

*Fig (a): N-channel.* A square block labelled **P substrate**, with a **channel** drawn as a
staircase-shaped N region running from the top face down the right and out at the bottom face — the
top lead is **Drain (D)**, the bottom lead **Source (S)**, and the substrate is taken out to the right
as a terminal marked **SS**. On the **left face** a small filled bar is the **metal gate**, with an
arrow labelling the thin layer between it and the channel **$\mathrm{SiO_2}$**; the lead from it is
**Gate (G)**. To the right, the **N-channel circuit symbol**: D at the top, S at the bottom, joined by
a **solid** vertical channel line, the gate drawn as a **separate plate to the left, touching
nothing**, and the substrate arrow pointing **inward**, all in a circle.

*Fig (b): P-channel.* The same drawing with the type letters interchanged — **N substrate**,
**P-channel** — and the symbol's substrate arrow pointing **outward**.

- The gate is **insulated from its conducting channel** by an ultra-thin oxide insulating film of
  **silicon dioxide**. ·J p88
- ⚠ REDACTED ·J p88 — **an entire bullet, two lines long (≈139 characters), is destroyed by two
  opaque blocks.** It sits between the "gate is insulated" bullet and the "parallel plate capacitor"
  bullet.
- **Silicon dioxide and the channel form a parallel-plate capacitor.** ·J p88

> [added] **The missing ·J p88 bullet is NOT recovered, and no wording is offered for it.** The
> position — between "the gate is insulated" and "the oxide and the channel form a capacitor" — is
> where the standard treatment puts the consequence of the insulation, namely that **either polarity
> of gate voltage may be applied because there is no junction to forward-bias** (the tier-2 file's
> ·L4 p17 places exactly that sentence at exactly that point). But the length is about 139 characters
> and the standard sentence is nearer 95, so something else is in there too. **This file states the
> physics from the surviving text and stops:** the gate is a capacitor plate, so gate current is a
> capacitor leakage current, and gate voltage of either sign is permissible. A clean copy of ·J p88
> is needed to recover the lecturer's own bullet.

---

## 7.8 DE MOSFET operation ·J p88–p89

### a) Depletion mode, N-channel ·J p88

[fig ·J p88] **The N-channel DE MOSFET wired for depletion-mode operation, with an inset.** The block
of ·J p88 is redrawn with the drain taken up to a rail through the $V_{DS}$ measurement arrow to a
variable supply $V_{DD}$, the substrate lead SS returned to the source rail, and the gate fed from a
variable supply $V_{GG}$ with $V_{GS}$ marked across gate-source; the drain current is arrowed
downward at the top of the block. To the right sits an **enlarged view of the gate capacitor**: three
columns of charge signs — a **metal gate** plate carrying **−**, the **$\mathrm{SiO_2}$** block
carrying **+** on its gate side and **−** on its channel side, and the channel carrying **+**.

- At $V_{GS} = 0$, electrons flow from source to drain **through the channel that is already there**.
  ·J p88
- With the gate **negative**, it **depletes the N-channel of its electrons by inducing positive
  charge in it**: the more negative the gate, the greater the reduction of electrons and the **lower
  the conductivity**. ·J p88
- Enough negative $V_{GS}$ **cuts the channel off**; that voltage is $V_{GS(\text{off})}$. ·J p88

### b) Enhancement mode, N-channel ·J p89

[fig ·J p89] **The same circuit with the gate supply reversed.** Identical drawing to the depletion
figure except that $V_{GG}$ now drives the gate **positive**, and in the enlarged gate-capacitor inset
**every sign is reversed** — the metal gate carries **+**, the oxide **−** then **+**, and the channel
carries the induced **−**, the free electrons that enhance conduction.

- A **+ve** gate voltage makes the input gate capacitor **create free electrons in the channel**,
  which increases $I_D$. ·J p89
- Those extra electrons **increase — enhance — the conductivity** of the channel. ·J p89
- As the +ve gate voltage rises, source-to-drain conductivity rises and **the current increases**.
  ·J p89

> [added] **The one thing that separates a DE MOSFET from a JFET.** A JFET's gate is a **reverse-biased
> junction**, so positive gate voltage is forbidden — it would forward-bias the junction and destroy
> the input resistance. A DE MOSFET's gate is a **capacitor plate**, so positive gate voltage is
> allowed, and the device runs on **both sides of $V_{GS}=0$**. That is the whole of the enhancement
> mode.

---

## 7.9 Characteristics of a DE MOSFET ·J p89–p90

### a) Static (drain) characteristics ·J p89

[fig ·J p89] **The DE MOSFET drain-characteristic family.** Axes $I_D$ (vertical) and $V_{DS}$
(horizontal), origin 0. A **solid** curve rises out of the origin through a knee **A**, flattens
through **B** and runs level to **C**, where it turns up sharply; it is labelled **$V_{GS}=0$** and
its plateau sits at the $I_{DSS}$ tick on the $I_D$ axis. **Above** it, a **dashed** curve of the same
shape at a higher plateau, labelled **$V_{GS} = +2\ \mathrm{V}$**. **Below** it, a dashed curve at a
lower plateau labelled **$V_{GS} = -2\ \mathrm{V}$**, and below that a nearly flat trace along the
axis labelled **$V_{GS(\text{off})}$** and arrowed **"Leakage current"**. Dashed verticals drop from
B and C to the $V_{DS}$ axis at **$V_P$** and **$V_A$**. Spans across the top read **"Ohmic region"**,
**"Pinch-off region (Saturation)"** and **"Breakdown region"**. At the right, a vertical
double-headed arrow separates **"Enhancement mode"** (above the $V_{GS}=0$ curve) from **"Depletion
mode"** (below it).

> ⚠ REDACTED ·J p89 — **a whole bullet, two lines long (≈118 characters), is destroyed by two opaque
> blocks** immediately under this figure. It is the only commentary the notes offer on the DE MOSFET
> static characteristics.

> [added] **Not recovered, and no wording is offered.** The figure is fully legible and the physics it
> carries is stated below from the figure itself, so nothing in the teaching is lost — but the
> lecturer's own sentence cannot be reconstructed from ≈118 characters of context. A clean copy of
> ·J p89 is needed.

**What the figure itself establishes** [added, read off the ·J p89 figure]:

- the curve family is **continuous through $V_{GS}=0$** — there is nothing special about zero bias;
- the $V_{GS}=0$ plateau is $I_{DSS}$, and curves **above** it carry **more** than $I_{DSS}$;
- the region above $V_{GS}=0$ is the **enhancement mode**, the region below it the **depletion mode**;
- the bottom trace, at $V_{GS(\text{off})}$, is not exactly zero — it is the **leakage current**.

### b) Transfer characteristic ·J p90

[fig ·J p90] **DE MOSFET transfer characteristic.** The $I_D$ axis is drawn **through the middle** of
the plot at $V_{GS}=0$, with **$-V_{GS}$** running left and **$+V_{GS}$** running right. A tick
$V_{GS(\text{off})}$ sits on the negative side. The curve leaves the horizontal axis at
$V_{GS(\text{off})}$, rises concave-upward, **crosses the vertical axis at the tick $I_{DSS}$** and
**keeps rising** into positive $V_{GS}$. The left half is labelled **"Depletion mode"**, the right
half **"Enhancement mode"**.

- For a given $V_{DS}$, $I_D$ **flows even when $V_{GS}=0$**; holding $V_{DS}$ constant and making
  $V_{GS}$ more negative, $I_D$ **falls to zero at $V_{GS} = V_{GS(\text{off})}$**. ·J p90
- Used in enhancement mode, **$I_D$ increases as $V_{GS}$ is made more positive**. ·J p90

> [added] **The structural difference from a JFET's transfer characteristic:** it does not stop at
> $V_{GS}=0$. A JFET's curve ends there, at $I_{DSS}$; a DE MOSFET's continues to the right, where
> $I_D$ **exceeds** $I_{DSS}$. That also means the $I_D \le I_{DSS}$ sanity check of §7.5 applies to
> JFETs only.

---

## 7.10 Enhancement-only N-channel MOSFET (NMOS) ·J p90–p91

[def] An **enhancement-only MOSFET** has **no channel at zero gate bias**. It has to be **created**
by the gate voltage, and it therefore **operates with a positive gate only**. ·J p90

### Construction ·J p90

[fig ·J p90] **Two construction diagrams with their circuit symbols.**

*Fig (a): N-channel (NMOS).* A square block labelled **P substrate** with **two separate N squares**
embedded in it — one at the top face with the **Drain (D)** lead, one at the bottom face with the
**Source (S)** lead — **and no material joining them**. The substrate lead leaves to the right as
**SS**. On the left face, the **metal gate** bar with **$\mathrm{SiO_2}$** arrowed between it and the
substrate, its lead marked **Gate (G)**. To the right, the **N-channel circuit symbol**: D at the top,
S at the bottom, the channel drawn as **three short broken segments** (not a solid line — that is the
symbol's way of saying "no channel until you make one"), the gate a separate plate to the left, and
the substrate arrow pointing **inward**.

*Fig (b): P-channel.* The same with **N substrate** and two **P** squares; the substrate arrow points
**outward**.

- "There is a channel between the source and the drain which has a **P substrate cutting into it**."
  ·J p90
- "It operates with the **+ve gates only**." ·J p90

> [added] The first of those two bullets is the notes' way of describing the figure: the substrate
> comes all the way up to the oxide between the two N islands, so the source-to-drain path is broken
> by P material. The symbol's **broken channel line** says the same thing.

### Operation — the inversion layer ·J p90–p91

[fig ·J p91] **The NMOS wired for operation, with the gate-capacitor inset.** The block of ·J p90 —
two N islands in a P substrate, gate plate on the left, SS taken out to the right and returned to the
source rail — with the drain taken through the $V_{DS}$ arrow to a variable supply $V_{DD}$, the gate
fed from a variable $V_{GG}$ with $V_{GS}$ marked, and $I_D$ arrowed **downward** at the drain. The
enlarged gate capacitor to the right shows the metal gate carrying **+**, the $\mathrm{SiO_2}$
carrying **−** then **+**, and the channel side carrying the induced **−**.

The sequence, in the notes' order: ·J p90–p91

1. When $V_{GS} = 0$, **$I_D$ is non-existent**.
2. For $I_D$ to flow, a **significant +ve gate voltage must be applied**.
3. That voltage **produces a thin layer of electrons close to the metal-oxide film, stretching from
   the source to the drain**.
4. That thin layer **provides the channel with electrons**, so it behaves as N-type material — it is
   called the **N-type inversion layer**, or a **virtual N-channel**.
5. [def] The **minimum gate-source voltage which produces the N-type inversion layer** is the
   **threshold voltage $V_{GS(\text{th})}$**, V, positive for an NMOS. ·J p91
6. For a given $V_{DS}$, as $V_{GS}$ is increased the **virtual channel deepens** and $I_D$
   increases. ·J p91

[eq: emosfet-square-law-j] **The enhancement-MOSFET square law** ·J p91

$$\boxed{\;I_D = K\left(V_{GS} - V_{GS(\text{th})}\right)^{2}\;}$$

- $I_D$ — drain current, A
- $K$ — a constant **which depends on the particular MOSFET**, A·V⁻² (quoted in mA/V²)
- $V_{GS}$ — gate-source voltage, V
- $V_{GS(\text{th})}$ — threshold voltage, V

Valid only for $V_{GS} > V_{GS(\text{th})}$; below threshold $I_D = 0$.

> [added] **Why "inversion".** The surface of a **P** substrate, under a strong enough positive gate,
> ends up with more free **electrons** than holes — it has been inverted from P-type behaviour to
> N-type behaviour. The layer is only a few tens of nanometres thick and exists **only while the gate
> voltage is applied**; hence "virtual channel".

---

## 7.11 Characteristics of an N-channel enhancement-only MOSFET ·J p91–p92

### a) Static characteristics ·J p91

[fig ·J p91] **The figure printed here is, line for line, the DE MOSFET figure of ·J p89** — the same
$V_{GS}=+2\ \mathrm{V}$, $V_{GS}=0$ and $V_{GS}=-2\ \mathrm{V}$ curves, the same $I_{DSS}$ tick, the
same $V_{GS(\text{off})}$ trace arrowed "Leakage current", the same $V_P$ and $V_A$ ticks, the same
ohmic / pinch-off / breakdown spans, and the same "Enhancement mode / Depletion mode" bracket at the
right.

> ⚠ VERIFY **JV7.2** ·J p91 — **the static-characteristic figure of the enhancement-only MOSFET is
> the DE MOSFET figure from ·J p89, reproduced unchanged.** An enhancement-only MOSFET **has no
> channel at $V_{GS}=0$**, so it has **no $I_{DSS}$, no $V_{GS}=0$ curve carrying current, no
> $V_{GS}=-2\ \mathrm{V}$ curve, no $V_{GS(\text{off})}$ and no depletion mode at all.** The printed
> figure contradicts the same page's own equation $I_D = K(V_{GS}-V_{GS(\text{th})})^2$, which is
> zero for every $V_{GS} \le V_{GS(\text{th})}$.
> **Correct figure:** a family of $I_D$–$V_{DS}$ curves labelled with **positive** $V_{GS}$ values,
> all **above** $V_{GS(\text{th})}$ (say $+4, +6, +8, +10\ \mathrm{V}$ for a $V_{GS(\text{th})}$ of
> $+2\ \mathrm{V}$); the curve for any $V_{GS} \le V_{GS(\text{th})}$ **lies on the axis**. The
> saturation boundary is $V_{DS} = V_{GS} - V_{GS(\text{th})}$. Nothing labelled $I_{DSS}$ appears.
> The correct **transfer** characteristic is on the next page (·J p92) and is drawn properly.
> See `_verification-log.md`.

> ⚠ VERIFY **JV7.3** ·J p91 — **the six bullets printed under that figure are the JFET operating
> narrative of ·J p85, reproduced verbatim.** They state that "the depletion regions penetrate more
> deeply into the channel at points which lie closer to the drain", that $I_D = V_{DS}/R_{DS}$, that
> "$I_D$ increases up to a maximum value $I_{DSS}$ (saturation current)", and that "at this stage
> $I_D = I_{DSS}$".
> **None of it describes an enhancement-only MOSFET.** There are **no gate depletion regions** — the
> gate is insulated, and the channel is created, not depleted — and there is **no $I_{DSS}$**, since
> $I_D = 0$ at $V_{GS}=0$ by construction.
> **Correct statement:** $I_D$ is zero until $V_{GS}$ exceeds $V_{GS(\text{th})}$; above threshold an
> inversion layer forms and, once $V_{DS} \ge V_{GS} - V_{GS(\text{th})}$, the device saturates at
> $$\boxed{\;I_D = K\left(V_{GS}-V_{GS(\text{th})}\right)^{2}\;}$$
> Below that $V_{DS}$ the device is in the **ohmic** region. See `_verification-log.md`.

> ### [added] What to do with ·J p91 in revision
>
> **Learn the equation from ·J p91 and the figure from ·J p92.** The transfer characteristic on
> ·J p92 is drawn correctly for an E-only device and carries all the physics the static-characteristic
> figure gets wrong. If an examination asks for the **drain** characteristics of an E-only MOSFET,
> draw the corrected family described in **JV7.2** — positive $V_{GS}$ labels only, no $I_{DSS}$,
> curves that vanish below threshold.

### b) Transfer characteristic ·J p92

[fig ·J p92] **E-MOSFET transfer characteristic — this one is right.** The $I_D$ axis stands at the
left with 0 at its foot; the horizontal axis runs right and is labelled **$+V_{GS}$**, with a tick at
**$V_{GS(\text{th})}$** part-way along. **The curve lies flat on the axis from the origin to
$V_{GS(\text{th})}$**, then leaves the axis and rises steeply, concave upward. Annotations inside the
plot: **"Enhancement mode"**, and **"$I_D$ flows only when $V_{GS}$ exceeds threshold voltage
$V_{GS(\text{th})}$"**. There is **no** negative-$V_{GS}$ half and **no** $I_{DSS}$ tick.

- For $I_D$ to flow, a **significant +ve gate voltage must be applied**. ·J p92
- It **starts conducting at $V_{GS} = V_{GS(\text{th})}$**. ·J p92
- As $V_{GS}$ increases further there is a corresponding increment of $I_D$, following
  $I_D = K(V_{GS}-V_{GS(\text{th})})^2$. ·J p92

[table] **[added] The three FET transfer characteristics side by side** — the single most
examinable comparison in this range

| Device | Curve starts at | Passes through $V_{GS}=0$ at | Extends to positive $V_{GS}$? | Governing law |
|---|---|---|---|---|
| **JFET** (N-ch) | $V_{GS(\text{off})}$, negative | $I_{DSS}$ | **no** — gate junction would forward-bias | $I_D = I_{DSS}(1-V_{GS}/V_{GS(\text{off})})^2$ |
| **DE MOSFET** (N-ch) | $V_{GS(\text{off})}$, negative | $I_{DSS}$ | **yes** — $I_D$ exceeds $I_{DSS}$ | same square law, extended both sides |
| **E-only MOSFET** (NMOS) | $V_{GS(\text{th})}$, **positive** | **zero** | yes — that is the only region | $I_D = K(V_{GS}-V_{GS(\text{th})})^2$ |

---

## 7.12 Parameters considered when purchasing a FET ·J p92

Two lists, given as-is. They are pure recall material and have appeared as short-answer questions.

[table] **JFET purchase parameters** ·J p92 · **MOSFET purchase parameters** ·J p92

| # | JFET | MOSFET |
|---|---|---|
| 1 | the gate-source **breakdown voltage** | **breakdown voltage** |
| 2 | the gate **reverse leakage current** | **forward transconductance** |
| 3 | the gate-source **cut-off voltage** | **drain-source ON resistance** |
| 4 | the **drain current at zero gate voltage** ($I_{DSS}$) | **switching characteristics** |
| 5 | the **forward transconductance** | **zero-gate-voltage drain current** |
| 6 | the **input capacitance** | **input capacitance** |
| 7 | the **switching** consideration | — |
| 8 | the **drain-source ON resistance** | — |
| 9 | the **power rating** | — |

> [added] **Note what item 5 in the JFET list and item 2 in the MOSFET list are.** "Forward
> transconductance" is $g_m$ — the small-signal parameter that governs every FET amplifier gain.
> **This document names it here and nowhere else: it never defines it, never gives its formula and
> never uses it.** §7.23 says where to get it.

---

## 7.13 Biasing of FETs — the four JFET schemes ·J p92–p94

[table] **Symbols for the bias section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $R_D$ | drain resistor | $\Omega$ | 1–5 kΩ |
| $R_S$ | source resistor | $\Omega$ | 0.5–3 kΩ |
| $R_G$ | gate return resistor | $\Omega$ | 1–10 MΩ |
| $R_1$, $R_2$ | upper and lower divider resistors | $\Omega$ | kΩ–MΩ |
| $C_1$, $C_2$ | input and output coupling capacitors | F | µF |
| $C_S$ | source bypass capacitor | F | µF |
| $V_D$, $V_S$ | drain and source **node potentials** w.r.t. ground | V | — |
| $V_{R_2}$ | voltage across $R_2$ = gate node potential | V | — |
| $V_{GG}$ | separate gate supply (magnitude; rail drawn as $-V_{GG}$) | V | 1–5 V |
| $V_{SS}$ | separate source supply (magnitude; rail drawn as $-V_{SS}$) | V | 5–15 V |
| $V_{GSQ}$, $V_{DSQ}$, $I_{DQ}$ | quiescent (Q-point) values | V, V, A | — |

A JFET can be biased by one of four schemes: ·J p92

1. a **separate power source $V_{GG}$**;
2. some form of **self biasing**;
3. **source biasing**;
4. **voltage divider bias**.

Every one of them is analysed with the **same drain-loop equation**:

[eq: fet-supply-loop-j] ·J p93

$$\boxed{\;V_{DD} = I_DR_D + V_{DS} + I_SR_S\;}$$

and every one of them exploits $I_G \approx 0$, so that **no voltage is dropped across $R_G$**.

### a) Separate supply (gate bias) ·J p93

[fig ·J p93] **Common-source stage with a negative gate supply.** $V_{DD}$ rail at the top right;
$R_D$ from the rail down to the **drain**, and the output $V_o$ taken from the drain through $C_2$.
The input $v_i$ enters through $C_1$ to the **gate**. From the gate node, $R_G$ runs **down to a
terminal marked $-V_{GG}$**. The **source** goes to ground through $R_S$, bypassed by $C_S$. The
transistor is labelled $Q_1$.

Printed on the page: ·J p93

$$V_{DD} = I_DR_D + V_{DS} + I_SR_S$$
$$V_{GG} = I_GR_G + V_{GS} + I_SR_S$$
$$V_{GG} = V_{GS} + I_SR_S \quad\text{since } I_G \approx 0$$

> ⚠ VERIFY **JV7.7** ·J p93 — **the gate-loop equation has the wrong sign for the circuit drawn.**
> The figure's gate rail is labelled **$-V_{GG}$**, so $V_{GG}$ is a **magnitude** and the gate node
> sits at $-V_{GG}$ below ground. With $I_G \approx 0$ there is no drop across $R_G$, so
> $$V_G = -V_{GG}, \qquad V_S = +I_SR_S, \qquad V_{GS} = V_G - V_S = -V_{GG} - I_SR_S$$
> The printed form $V_{GG} = V_{GS} + I_SR_S$ rearranges to $V_{GS} = V_{GG} - I_SR_S$, which is
> **positive** whenever $I_SR_S < V_{GG}$ — a forward-biased gate on an N-channel JFET, which the
> device does not survive.
> **Correct form:**
> $$\boxed{\;V_{GS} = -V_{GG} - I_SR_S \qquad (V_{GG} > 0 \text{ the magnitude of the rail})\;}$$
> **Note the contrast with source bias on ·J p94, where the identical-looking equation is CORRECT** —
> there the negative rail sits in the **source** branch, not the gate branch, and the two signs work
> out the other way. That is exactly why the two must not be memorised as one formula.
> See `_verification-log.md`.

[eq: gate-bias-j] **Separate-supply (gate) bias — corrected**

$$\boxed{\;V_{GS} = -V_{GG} - I_SR_S\;}$$

### b) Self biasing ·J p93

[fig ·J p93] **The same stage with the gate returned to ground.** Identical to the separate-supply
figure except that **$R_G$ now runs from the gate to ground** — there is no $V_{GG}$ rail at all. $R_S$
from source to ground, bypassed by $C_S$; $R_D$ from $V_{DD}$ to drain; $v_i$ in through $C_1$, $V_o$
out through $C_2$.

Printed on the page: ·J p93

$$V_{DD} = I_DR_D + V_{DS} + I_SR_S$$
$$V_S = I_SR_S$$
$$V_D = V_{DD} - I_DR_D \quad\text{or}\quad V_{DS} + I_SR_S$$
$$I_GR_G + V_{GS} + I_SR_S = 0$$

[eq: self-bias-j] and therefore, with $I_G \approx 0$: ·J p93

$$\boxed{\;V_{GS} = -I_SR_S\;}$$

Why it works, in the notes' own five points: ·J p93

1. The bias is **obtained from the flow of drain current through $R_S$**: $V_S = I_SR_S$ and
   $V_{GS} = -I_SR_S$.
2. The gate is held **that much negative with respect to ground**.
3. Adding $R_G$ **does not upset the dc bias**, because no gate current flows through it beyond the
   leakage current.
4. **Without $R_G$ the gate would be floating**, would collect charge and would **cut the JFET off**.
5. $R_G$ also **prevents the a.c. input voltage being short-circuited** to ground.

> [added] **This is the equation to have automatic.** The minus sign is the whole point: the drain
> current generates its **own** negative gate bias, with no second supply. Note that the notes write
> $I_S$ here and $I_D$ in the divider-bias equation for the same current — they are equal, because
> $I_G \approx 0$.

### c) Source biasing ·J p94

*(The heading letter **c)** is missing from ·J p94 — see §7.0.)*

[fig ·J p94] **The stage with a negative source rail.** $R_D$ from $V_{DD}$ to the drain, $V_o$ out
through $C_2$; $v_i$ in through $C_1$ to the gate; **$R_G$ from gate to ground**; and $R_S$ from the
source **down to a terminal marked $-V_{SS}$**. There is **no** bypass capacitor drawn on $R_S$ in
this figure.

Printed on the page: ·J p94

$$V_D = V_{DD} - I_DR_D$$
$$V_{SS} = I_GR_G + V_{GS} + I_SR_S$$

[eq: source-bias-j] and with $I_G \approx 0$: ·J p94

$$\boxed{\;V_{SS} = V_{GS} + I_SR_S \quad\Longrightarrow\quad V_{GS} = V_{SS} - I_SR_S\;}$$

with $V_{SS}$ the **magnitude** of the negative rail.

> [added] **This one is correct as printed** — and it is worth seeing why, next to **JV7.7**. Here
> the gate is at ground ($V_G = 0$) and the negative rail is under $R_S$, so
> $$V_S = I_SR_S - V_{SS}, \qquad V_{GS} = -V_S = V_{SS} - I_SR_S$$
> exactly the printed result. For a working N-channel bias we need $V_{GS} < 0$, i.e.
> $I_SR_S > V_{SS}$.
>
> **Why source bias is used:** rearranged, $I_S = (V_{SS} - V_{GS})/R_S$. Make $V_{SS}$ large compared
> with $V_{GS}$ and $I_S \approx V_{SS}/R_S$ — **almost independent of the device's own parameters**.
> That is the most stable of the four schemes, and it is the FET analogue of the BJT's two-supply
> emitter bias (`13-bipolar-junction-transistor.md`).

### d) Voltage divider biasing ·J p94

[fig ·J p94] **The divider-biased common-source stage.** $V_{DD}$ rail across the top. $R_1$ from the
rail to the **gate node**, $R_2$ from the gate node to ground — the two form the divider. $R_D$ from
the rail to the **drain**; $V_o$ out through $C_2$; $v_i$ in through $C_1$ to the gate node. $R_S$
from source to ground, **bypassed by $C_S$**.

Printed on the page: ·J p94

$$V_{DD} = V_{R_2} + V_{R_1}$$
$$V_{DD} = I_DR_D + V_{DS} + I_SR_S$$

[eq: divider-bias-j] **The two equations that do the work** ·J p94

$$\boxed{\;V_{R_2} = \frac{V_{DD}}{R_1+R_2}\times R_2\;}$$

$$\boxed{\;V_{R_2} = V_{GS} + I_DR_S \quad\Longrightarrow\quad V_{GS} = V_{R_2} - I_DR_S\;}$$

- $V_{R_2}$ — the voltage across $R_2$, which **is** the gate node potential, since $I_G \approx 0$
  means the divider is unloaded, V

> [added] **The reason a JFET divider looks odd next to a BJT divider.** In a BJT stage the divider
> sets $V_B$ and $V_{BE}$ is a fixed 0.7 V. Here the divider sets a **positive** gate potential
> $V_{R_2}$, and the *negative* $V_{GS}$ comes from making $I_DR_S$ **larger** than $V_{R_2}$. That
> is why the worked example in §7.15 has a $+1.2\ \mathrm{V}$ gate sitting above a $+3\ \mathrm{V}$
> source, giving $V_{GS} = -1.8\ \mathrm{V}$.

---

## 7.14 [ex] Worked example — self-bias, find $V_{DS}$ ·J p95

*(The label "Example" is missing above this problem — see §7.0.)*

> **Find the value of $V_{DS}$ in the circuit below if $I_D = 4\ \mathrm{mA}$,
> $V_{DD} = 12\ \mathrm{V}$, $R_D = 1\mathrm{k}5$ and $R_S = 500\ \mathrm{R}$.** ·J p95

[fig ·J p95] The circuit is the **self-bias** stage of ·J p93 redrawn: $R_D$ from the $V_{DD}$ rail to
the drain, $V_o$ out through $C_2$, $v_i$ in through $C_1$ to the gate, **$R_G$ from gate to ground**,
$R_S$ from source to ground **bypassed by $C_S$**.

*(Notation: "$1\mathrm{k}5$" is $1.5\ \mathrm{k\Omega}$ and "$500\ \mathrm{R}$" is $500\ \Omega$ —
the old British resistor notation, where the multiplier letter replaces the decimal point.)*

**Solution as printed** ·J p95

$$V_S = I_SR_S = 4\times10^{-3}\times500 = 2\ \mathrm{V}$$

$$V_D = V_{DD} - I_DR_D$$

$$V_D = 12 - 1.5\times10^{-3}\times4\times10^{-3} = 6\ \mathrm{V}$$

$$V_{DS} = V_D - V_S = 6 - 2 = 4\ \mathrm{V}$$

> ⚠ VERIFY **JV7.5** ·J p95 — the third line prints
> $V_D = 12 - 1.5\times10^{-3}\times4\times10^{-3}$. $R_D$ is $1.5\ \mathrm{k\Omega}$, i.e.
> $1.5\times10^{3}$, **not** $1.5\times10^{-3}$. As printed the product is $6\times10^{-6}$ and the
> line evaluates to $11.999994\ \mathrm{V}$, not $6\ \mathrm{V}$. **Correct line:**
> $$\boxed{\;V_D = 12 - \left(4\times10^{-3}\right)\left(1.5\times10^{3}\right) = 12 - 6 = 6\ \mathrm{V}\;}$$
> The stated answer, $6\ \mathrm{V}$, is right; only the exponent is wrong. The same example's
> companion on the same page (§7.15) prints its exponents correctly, which is how the slip is
> identified. See `_verification-log.md`.

**[added] Verified independently with `python3`:**

$$V_S = \left(4\times10^{-3}\right)(500) = 2\ \mathrm{V}\;\checkmark$$

$$V_D = 12 - \left(4\times10^{-3}\right)\left(1.5\times10^{3}\right) = 12 - 6 = 6\ \mathrm{V}\;\checkmark$$

$$\boxed{\;V_{DS} = 6 - 2 = 4\ \mathrm{V}\;}\;\checkmark$$

> ### [added] Two things the example does not say
>
> **1. The bias voltage comes free with the answer.** This is a self-bias circuit, so
> $$V_{GS} = -I_SR_S = -V_S = -2\ \mathrm{V}$$
> The question does not ask for it, but it is one line and it is the quantity every follow-up part
> would need.
>
> **2. The drain-loop check.** Adding the three drops must return the supply:
> $$I_DR_D + V_{DS} + I_SR_S = 6 + 4 + 2 = 12\ \mathrm{V} = V_{DD}\;\checkmark$$
> Use that as the last line of any FET bias answer. It catches a wrong exponent instantly — which is
> precisely the defect **JV7.5** records.

---

## 7.15 [ex] Worked example — voltage-divider bias, find $V_{GSQ}$ and $V_{DSQ}$ ·J p95

> **Example.** In the amplifier given in the figure below, $V_{DD} = 20\ \mathrm{V}$,
> $R_1 = 15.7\ \mathrm{M\Omega}$, $R_2 = 1\ \mathrm{M\Omega}$, $R_D = 3\ \mathrm{k\Omega}$,
> $R_S = 2\ \mathrm{k\Omega}$ and $I_{DQ} = 1.5\ \mathrm{mA}$. **Calculate $V_{GSQ}$ and $V_{DSQ}$.**
> ·J p95

[fig ·J p95] The **voltage-divider** stage of ·J p94, redrawn identically: $R_1$ from the $V_{DD}$ rail
to the gate node, $R_2$ from the gate node to ground, $R_D$ from the rail to the drain, $V_o$ out
through $C_2$, $v_i$ in through $C_1$ to the gate node, $R_S$ from source to ground bypassed by $C_S$.

**Solution as printed** ·J p95

$$V_{R_2} = \frac{V_{DD}}{R_1+R_2}\times R_2 = \frac{20}{15.7+1}\times 1 = 1.2\ \mathrm{V}$$

$$V_{R_2} = V_{GSQ} + I_DR_S$$

$$V_{GSQ} = V_{R_2} - I_DR_S = 1.2 - 1.5\times10^{-3}\times2\times10^{3} = -1.8\ \mathrm{V}$$

$$V_D = V_{DD} - I_DR_D = 20 - 1.5\times10^{-3}\times3\times10^{3} = 15.5\ \mathrm{V}$$

$$V_S = I_SR_S = 1.5\times10^{-3}\times2\times10^{3} = 3\ \mathrm{V}$$

$$V_{DS} = V_D - V_S = 15.5 - 3 = 12.5\ \mathrm{V}$$

*(The resistances are in $\mathrm{M\Omega}$ in the first line and in $\Omega$ thereafter; both are
dimensionally consistent, because the divider ratio is dimensionless.)*

**[added] Verified independently with `python3`:**

$$V_{R_2} = 20\times\frac{1}{16.7} = 1.19760\ldots \approx 1.2\ \mathrm{V}\;\checkmark$$

$$V_{GSQ} = 1.19760 - 3 = -1.8024\ \mathrm{V} \approx \boxed{\;-1.8\ \mathrm{V}\;}\;\checkmark$$

$$V_D = 20 - 4.5 = 15.5\ \mathrm{V}\;\checkmark \qquad V_S = 3\ \mathrm{V}\;\checkmark$$

$$\boxed{\;V_{DSQ} = 12.5\ \mathrm{V}\;}\;\checkmark$$

**Drain-loop check:** $I_DR_D + V_{DS} + I_SR_S = 4.5 + 12.5 + 3 = 20\ \mathrm{V} = V_{DD}$ ✓

*The notes round $V_{R_2}$ to $1.2\ \mathrm{V}$ before subtracting; carrying the exact value
$1.1976\ \mathrm{V}$ changes $V_{GSQ}$ by $2.4\ \mathrm{mV}$ and $V_{DSQ}$ not at all. The rounding is
harmless.*

> ### [added] Why $R_1$ and $R_2$ are in megohms
>
> $15.7\ \mathrm{M\Omega} + 1\ \mathrm{M\Omega}$ draws $20/16.7\ \mathrm{M\Omega} = 1.2\ \mathrm{\mu A}$
> from the supply — a **thousandth** of $I_D$. A BJT divider cannot do that, because it has to supply
> $I_B$; a FET divider can, because $I_G \approx 0$. That is the FET's high input resistance showing
> up in the dc design, and it is the single most quotable practical difference between the two
> families.

---

## 7.16 Biasing of E-only MOSFETs ·J p96

Because an enhancement-only MOSFET needs $V_{GS} > V_{GS(\text{th})}$ — a **positive** gate with
respect to the source — the four JFET schemes reduce to **two**: ·J p96

- **drain-feedback bias**, and
- **voltage-divider bias**;

and in both cases "the gate voltage is made **more +ve than the source** by an amount greater than
$V_{GS(\text{th})}$." ·J p96

### a) Drain-feedback bias ·J p96

[fig ·J p96] **Drain-feedback stage.** $V_{DD}$ at the top right; $R_D$ from the rail down to the
**drain**; $V_o$ taken from the drain through $C_2$. **$R_G$ is connected from the drain back to the
gate** — that is the feedback. $v_i$ enters through $C_1$ to the gate. The **source is taken directly
to ground** — there is no $R_S$ and no $C_S$. The transistor is $Q_1$.

Printed on the page: ·J p96

$$V_{GS} = -V_{DS}$$
$$V_D = V_{DD} - I_DR_D = V_{DS}$$

> ⚠ VERIFY **JV7.4** ·J p96 — **the first line has the wrong sign: it should be $V_{GS} = V_{DS}$.**
> With $I_G \approx 0$ there is **no voltage drop across $R_G$**, so the gate sits at exactly the
> drain potential:
> $$V_G = V_D, \qquad V_S = 0, \qquad V_{GS} = V_G - V_S = V_D = V_{DS}$$
> The page's **own next line** says $V_D = V_{DS}$, and its **own bullet** says "the gate voltage is
> made more +ve than the source" — both of which require the positive form. As printed,
> $V_{GS} = -V_{DS}$ makes the gate **negative**, which for an N-channel enhancement-only MOSFET means
> $V_{GS} < V_{GS(\text{th})}$ and the device is **cut off** — the circuit could not work at all.
> **Correct form:**
> $$\boxed{\;V_{GS} = V_{DS} = V_{DD} - I_DR_D\;}$$
> See `_verification-log.md`.

[eq: drain-feedback-bias-j] **Drain-feedback bias — corrected**

$$\boxed{\;V_{GS} = V_{DS} = V_{DD} - I_DR_D\;}$$

> [added] **Why the feedback stabilises the bias.** If $I_D$ drifts up, $I_DR_D$ grows, $V_D$ falls,
> and since $V_{GS} = V_D$ the gate voltage falls too — which pulls $I_D$ back down. It is the
> **collector-feedback bias** of `13-bipolar-junction-transistor.md`, with the base-emitter junction
> replaced by a capacitor. It also guarantees $V_{DS} = V_{GS} > V_{GS} - V_{GS(\text{th})}$, so the
> device is **always in saturation** — a drain-feedback stage cannot accidentally be biased into the
> ohmic region.

### b) Voltage divider bias ·J p96

[fig ·J p96] **Divider-biased E-MOSFET stage.** Identical in topology to the JFET divider stage of
·J p94: $R_1$ from the $V_{DD}$ rail to the gate node, $R_2$ from the gate node to ground, $R_D$ from
the rail to the drain, $V_o$ out through $C_2$, $v_i$ in through $C_1$, $R_S$ from source to ground
bypassed by $C_S$.

Printed on the page — the **same four equations** as the JFET divider: ·J p96

$$V_{DD} = V_{R_2} + V_{R_1}$$
$$V_{DD} = I_DR_D + V_{DS} + I_SR_S$$
$$V_{R_2} = \frac{V_{DD}}{R_1+R_2}\times R_2$$
$$V_{R_2} = V_{GS} + I_DR_S$$

> [added] **The equations are the same; the sign of the answer is not.** For a JFET, $I_DR_S$ is made
> **bigger** than $V_{R_2}$ so that $V_{GS}$ comes out **negative**. For an E-MOSFET, $V_{R_2}$ is
> made **bigger** than $I_DR_S$ so that $V_{GS}$ comes out **positive and above $V_{GS(\text{th})}$**.
> In the worked example that follows, $R_S = 0$, so $V_{GS} = V_{R_2}$ outright.

---

## 7.17 [ex] Worked example — E-MOSFET divider bias ·J p96–p97

> **Example.** For the E-MOSFET amplifier given above (voltage divider bias) $I_D = 4\ \mathrm{mA}$,
> $V_{GS} = 10\ \mathrm{V}$, $R_1 = 6\ \mathrm{k\Omega}$, $R_2 = 9\ \mathrm{k\Omega}$,
> $R_D = 1\ \mathrm{k\Omega}$, $R_S = 0\ \Omega$, $V_{DD} = 25\ \mathrm{V}$ and
> $V_{GS(\text{th})} = 5\ \mathrm{V}$. **Calculate $V_{GS}$ and $V_{DS}$ for the circuit.**
> ·J p96 (statement), ·J p97 (solution)

> ⚠ VERIFY **JV7.9** ·J p96 — **the symbols $I_D$ and $V_{GS}$ are each used for two different things
> in one problem.** The data "$I_D = 4\ \mathrm{mA}$, $V_{GS} = 10\ \mathrm{V}$" are the **data-sheet
> ON point** of the device — they are what the solution substitutes into $K = I_D/(V_{GS}-V_{GS(\text{th})})^2$
> — while the $V_{GS}$ the question asks for is the **circuit's** bias, which comes out at
> $15\ \mathrm{V}$, and the $I_D$ that goes with it is $16\ \mathrm{mA}$. A reader who takes the given
> $V_{GS} = 10\ \mathrm{V}$ as the operating point gets $I_D = 4\ \mathrm{mA}$ and $V_{DS} = 21\ \mathrm{V}$
> — a completely different answer. **Correct statement of the data:**
> $$\boxed{\;I_{D(\mathrm{ON})} = 4\ \mathrm{mA}\ \text{ at }\ V_{GS(\mathrm{ON})} = 10\ \mathrm{V}\;}$$
> See `_verification-log.md`.

**Solution as printed** ·J p96–p97

$$V_{R_2} = \frac{V_{DD}}{R_1+R_2}\times R_2 = \frac{25}{9+6}\times 9 = 15\ \mathrm{V}$$

$$V_{R_2} = V_{GS} = 15\ \mathrm{V}$$

[eq: emosfet-k-from-idon-j] **the constant $K$, from the data-sheet ON point** ·J p97

$$\boxed{\;K = \frac{I_{D(\mathrm{ON})}}{\left(V_{GS(\mathrm{ON})} - V_{GS(\text{th})}\right)^{2}}\;}$$

$$K = \frac{4\times10^{-3}}{(10-5)^{2}} = 0.16\ \mathrm{mA/V^2}$$

$$I_D = 0.16\,(15-5)^{2} = 16\ \mathrm{mA}$$

$$V_{DS} = V_{DD} - I_SR_S = 25 - 16\times10^{-3}\times1\times10^{3} = 9\ \mathrm{V}$$

> ⚠ VERIFY **JV7.6** ·J p97 — the last line is printed $V_{DS} = V_{DD} - I_SR_S$, but this example
> has **$R_S = 0$**; the $1\ \mathrm{k\Omega}$ actually substituted is **$R_D$**. Followed literally,
> the printed formula gives $V_{DS} = 25 - 0 = 25\ \mathrm{V}$. **Correct form** — and what the
> substitution actually performs:
> $$\boxed{\;V_{DS} = V_{DD} - I_D\left(R_D + R_S\right) = 25 - 16\times10^{-3}\times1\times10^{3} = 9\ \mathrm{V}\;}$$
> The answer $9\ \mathrm{V}$ is right; the symbol on the resistance is wrong.
> See `_verification-log.md`.

**[added] Verified independently with `python3`:**

$$V_{R_2} = 25\times\frac{9}{15} = 15\ \mathrm{V}\;\checkmark \quad\Rightarrow\quad V_{GS} = 15\ \mathrm{V}\ \text{ (since } R_S = 0)$$

$$K = \frac{4\times10^{-3}}{25} = 1.6\times10^{-4}\ \mathrm{A/V^2} = 0.16\ \mathrm{mA/V^2}\;\checkmark$$

$$I_D = 0.16\times(10)^{2} = 16\ \mathrm{mA}\;\checkmark$$

$$\boxed{\;V_{DS} = 25 - (16\times10^{-3})(1\times10^{3}) = 9\ \mathrm{V}\;}\;\checkmark$$

> ⚠ VERIFY **JV7.8** ·J p96–p97 — **the operating point this example lands on is outside the region
> where the equation used to find it is valid.** An enhancement MOSFET obeys
> $I_D = K(V_{GS}-V_{GS(\text{th})})^2$ **only in saturation**, i.e. only while
> $$V_{DS} \ \ge\ V_{GS} - V_{GS(\text{th})}$$
> Here $V_{GS} - V_{GS(\text{th})} = 15 - 5 = 10\ \mathrm{V}$, but the answer is
> $V_{DS} = 9\ \mathrm{V} < 10\ \mathrm{V}$: the device is in the **ohmic (triode) region**, where the
> square law **overestimates** $I_D$. The arithmetic in the notes is internally correct — the answer
> $9\ \mathrm{V}$ follows from the numbers given — but the circuit as specified could not actually
> deliver $16\ \mathrm{mA}$ at $9\ \mathrm{V}$. **A self-consistent version of the same question**
> needs either a larger $V_{DD}$ or a smaller $R_D$; with $R_D = 800\ \Omega$,
> $V_{DS} = 25 - 12.8 = 12.2\ \mathrm{V} > 10\ \mathrm{V}$ ✓.
> **Answer the question as set — the marks are for the method — but state the check.**
> See `_verification-log.md`.

> ### [added] The saturation check, as a habit
>
> After every E-MOSFET bias calculation, one line:
> $$V_{DS} \ \overset{?}{\ge}\ V_{GS} - V_{GS(\text{th})}$$
> If it fails, the square-law answer is an overestimate and the device is acting as a resistor. It is
> the E-MOSFET equivalent of checking a BJT has not saturated.

---

## 7.18 [exercise] and its solution ·J p97

> **Exercise.** An N-channel E-MOSFET has the following parameters: $I_{D(\mathrm{ON})} = 4\ \mathrm{mA}$
> at $V_{GS} = 10\ \mathrm{V}$, and $V_{GS(\text{off})} = 5\ \mathrm{V}$. **Calculate $I_D$ for
> $V_{GS} = 8\ \mathrm{V}$.** *Ans. 1.44 mA.* ·J p97

> ⚠ VERIFY **JV7.10** ·J p97 — **the exercise calls the $5\ \mathrm{V}$ parameter
> $V_{GS(\text{off})}$; for an enhancement-only MOSFET it is $V_{GS(\text{th})}$.** They are
> different quantities belonging to different devices: $V_{GS(\text{off})}$ is the **negative**
> voltage at which a JFET or DE MOSFET stops conducting, and it belongs in **Shockley's** equation;
> $V_{GS(\text{th})}$ is the **positive** voltage at which an E-only MOSFET **starts** conducting, and
> it belongs in the **$K$** equation. A reader taking the label at face value would reach for
> $I_D = I_{DSS}(1-V_{GS}/V_{GS(\text{off})})^2$ — for which no $I_{DSS}$ is even given. **The printed
> answer of 1.44 mA is obtained only by reading the 5 V as the threshold.**
> **Correct statement:** $V_{GS(\text{th})} = 5\ \mathrm{V}$. See `_verification-log.md`.

### [added] Full solution, verified with `python3`

**Step 1 — get $K$ from the ON point.** ·J p97's own equation, §7.17:

$$K = \frac{I_{D(\mathrm{ON})}}{\left(V_{GS(\mathrm{ON})} - V_{GS(\text{th})}\right)^{2}}$$

$$K = \frac{4\ \mathrm{mA}}{(10 - 5)^{2}\ \mathrm{V^2}} = \frac{4}{25}\ \mathrm{mA/V^2} = 0.16\ \mathrm{mA/V^2}$$

**Step 2 — apply the square law at the new bias.**

$$I_D = K\left(V_{GS} - V_{GS(\text{th})}\right)^{2}$$

$$I_D = 0.16 \times (8 - 5)^{2}$$

$$I_D = 0.16 \times 9$$

$$\boxed{\;I_D = 1.44\ \mathrm{mA}\;}$$

**Matches the notes' printed answer exactly.** ✓

**Sanity checks** [added]:

- $8\ \mathrm{V} > V_{GS(\text{th})} = 5\ \mathrm{V}$, so the device conducts ✓
- $8\ \mathrm{V} < 10\ \mathrm{V}$, so $I_D$ must be **less** than $4\ \mathrm{mA}$; $1.44 < 4$ ✓
- the square law scales as $(3/5)^2 = 0.36$, and $0.36\times4 = 1.44\ \mathrm{mA}$ ✓ — **the fastest
  route to the answer, with no $K$ at all**

> [added] **The ratio shortcut, worth remembering.** Because $K$ cancels,
> $$\frac{I_{D2}}{I_{D1}} = \left(\frac{V_{GS2}-V_{GS(\text{th})}}{V_{GS1}-V_{GS(\text{th})}}\right)^{2}$$
> Two data-sheet numbers and one squaring. It is also the check on any answer obtained the long way.

---

## 7.19 FET amplifiers ·J p97–p98

### a) DE MOSFET amplifier ·J p97–p98

[fig ·J p97] **Zero-biased N-channel DE MOSFET stage.** $V_{DD}$ rail at the top; $R_D$ from the rail
to the **drain**; the output $V_o$ taken from the drain through $C_2$. The input $v_i$ enters through
$C_1$ to the gate, and **$R_G$ runs from the gate to ground**. The **source goes straight to ground**
— there is **no $R_S$, no $C_S$ and no divider**. So $V_{GS} = 0$ at rest.

[fig ·J p97] **The transfer characteristic with the signal drawn on it.** $I_D$ vertical, $V_{GS}$
horizontal with $-V_{GS}$ to the left and $+V_{GS}$ to the right, a tick at $V_{GS(\text{off})}$ on
the negative side. The curve is the DE MOSFET parabola of §7.9, and the **Q point is marked at
$V_{GS} = 0$**, on the vertical axis. A sinusoid drawn **below** the horizontal axis, centred on
$V_{GS}=0$ and projected upward with dashed construction lines, is labelled **"Input signal"**; the
sinusoid it produces on the $I_D$ axis, drawn **to the right** of the curve and projected across with
dashed lines, is labelled **"Output signal"**.

- A **zero-biased** N-channel DE MOSFET with an a.c. source **capacitor-coupled to the gate**. ·J p97
- The input a.c. $V_{in}$ makes $V_{GS}$ **swing above and below its zero value**, therefore producing
  a swing in $I_D$. ·J p97
- A **+ve swing in $V_{GS}$ produces enhancement mode**, making $I_D$ **increase**. ·J p98

> [added] **This is the circuit that only a DE MOSFET can have.** Zero bias needs a device that
> conducts at $V_{GS} = 0$ *and* tolerates gate voltage of either sign. A JFET conducts at $V_{GS}=0$
> but cannot take a positive half-cycle; an E-only MOSFET tolerates positive gate voltage but does not
> conduct at zero. **Only the DE MOSFET does both — so it needs no bias network at all**, which is
> why the stage has three components and no divider.

### b) E-MOSFET amplifier ·J p98

[fig ·J p98] **Divider-biased E-MOSFET stage.** $R_1$ from the $V_{DD}$ rail to the gate node, $R_2$
from the gate node to ground, $R_D$ from the rail to the drain, $V_o$ out through $C_2$, $v_i$ in
through $C_1$ to the gate node, $R_S$ from source to ground bypassed by $C_S$ — the circuit of §7.16(b).

[fig ·J p98] **Its transfer characteristic with the signal.** $I_D$ vertical, $+V_{GS}$ horizontal,
origin 0, tick at $V_{GS(\text{th})}$. The curve lies on the axis until $V_{GS(\text{th})}$ then rises;
the **Q point is marked on the curve well above threshold**. A sinusoid below the axis, centred on the
Q-point gate voltage, is projected up onto the curve, and the resulting sinusoid is drawn against the
$I_D$ axis.

- The gate is biased with a **+ve voltage such that $V_{GS}$ is more than $V_{GS(\text{th})}$**. ·J p98
- The signal voltage produces a **swing in $V_{GS}$ below and above its Q-point value**. ·J p98
- That in turn causes a swing in $I_D$ and hence in $I_DR_D$. ·J p98

> ⚠ VERIFY **JC7.4** ·J p98 — in this figure **both** waveforms are labelled "Input signal". The
> upper one is drawn against the **$I_D$ axis** and is the **output signal** — the ·J p97 figure, which
> is otherwise identical in construction, labels the same pair correctly as "Output signal" and "Input
> signal". Cosmetic; the figure is still readable. See `_verification-log.md`.

> [added] **Where the Q point must sit, and why it differs between the two stages.** In the DE MOSFET
> stage the Q point is at $V_{GS}=0$, so the signal can swing symmetrically into depletion and
> enhancement. In the E-MOSFET stage it must sit **far enough above $V_{GS(\text{th})}$** that the
> negative half-cycle never drives $V_{GS}$ below threshold — otherwise the output is clipped flat at
> zero current. Neither figure marks how far; the practical rule is to place $V_{GSQ}$ at least a
> peak amplitude above threshold.

---

## 7.20 FET configurations ·J p98–p100

The notes treat the three configurations **descriptively**: for each, which terminal quantities are
the input and output, and the gains as **ratios of those quantities**. **No small-signal formula
appears** — see §7.23.

### a) Common source (CS) ·J p98–p99

[fig ·J p98] **Minimal CS topology.** A horizontal rail at the top marked $V_{DD}$; the **drain**
connects up to that rail, and the output $v_{out}$ is taken from a terminal on the drain lead. The
**gate** is driven from a terminal $v_{in}$ on the left. The **source** goes down to ground. No
resistors, no capacitors — a topology sketch only.

[table] **Common-source terminal parameters** ·J p98–p99

| | Input | Output |
|---|---|---|
| voltage | $V_{GS}$ | $V_{DS}$ |
| current | $I_G$ | $I_D$ |
| impedance | $V_{GS}/I_G$ | $V_{DS}/I_D$ |
| power | $I_GV_{GS}$ | $I_DV_{DS}$ |

[eq: cs-gains-j] ·J p99

$$\boxed{\;A_i = \frac{I_D}{I_G}, \qquad A_v = \frac{V_{DS}}{V_{GS}}\;}$$

> [added] **What those two ratios actually say.** Since $I_G \approx 0$, the CS **current gain is
> enormous** and its **input impedance $V_{GS}/I_G$ is enormous** — that is the FET's headline
> property, and this table is where the notes encode it. The CS stage is the FET's **general-purpose
> voltage amplifier**, and its voltage gain is **inverting**: a rise in $V_{GS}$ raises $I_D$, which
> raises $I_DR_D$ and therefore **lowers** $V_{DS}$. The notes' ratio $V_{DS}/V_{GS}$ carries no sign;
> the phase inversion is real and is worth writing next to it.

### b) Common drain (CD) ·J p99

[fig ·J p99] **Minimal CD topology.** A rail across the top labelled $V_{SS}$; the **source** connects
up to that rail and the output $v_{out}$ is taken from a terminal on the source lead. The **gate** is
driven from $v_{in}$ on the left. The **drain** goes down to ground. Note that the transistor symbol
is drawn **inverted relative to the CS sketch** — S at the top, D at the bottom.

[table] **Common-drain terminal parameters** ·J p99

| | Input | Output |
|---|---|---|
| voltage | $V_{DG}$ | $V_{DS}$ |
| current | $I_G$ | $I_S$ |
| impedance | $V_{DG}/I_G$ | $V_{DS}/I_S$ |
| power | $I_GV_{DG}$ | $I_SV_{DS}$ |

[eq: cd-gains-j] ·J p99

$$\boxed{\;A_i = \frac{I_S}{I_G}, \qquad A_v = \frac{V_{DS}}{V_{DG}}\;}$$

> ⚠ VERIFY **JC7.5** ·J p99 — **the double-subscript order is reversed throughout the common-drain
> table.** With the **drain** as the common terminal, the input is measured **gate-to-drain** and the
> output **source-to-drain**, so they should read $V_{GD}$ and $V_{SD}$, giving
> $A_v = V_{SD}/V_{GD}$. As printed, $V_{DG}$ and $V_{DS}$ are both measured *from* the drain, which
> reverses the sign of both and leaves the ratio unchanged — so nothing computed changes, but the
> convention $V_{XY} = V_X - V_Y$ used everywhere else in this document is broken.
> See `_verification-log.md`.

> ⚠ VERIFY **JC7.9** ·J p99 — **the common-drain supply rail is labelled $V_{SS}$**, while the
> common-source and common-gate sketches on ·J p98 and ·J p99 both use $V_{DD}$. $V_{SS}$ has already
> been used in this same document for the **negative source-bias supply** (·J p94) and **SS** for the
> **substrate terminal** (·J p88, ·J p90). Three meanings for the same letters inside seventeen pages.
> For an N-channel source follower the rail is the positive drain supply, $V_{DD}$.
> See `_nomenclature.md`.

> [added] **What a common-drain stage is for.** It is the **source follower** — voltage gain just
> under 1, no phase inversion, very high input impedance and **low output impedance**. It is a buffer,
> not an amplifier. Its purpose is to drive a low-impedance load from a high-impedance source without
> loading it.

### c) Common gate (CG) ·J p99–p100

[fig ·J p99] **Minimal CG topology.** Rail across the top marked $V_{DD}$; the **drain** connects up to
it and $v_{out}$ is taken from the drain lead. The **source** is driven from $v_{in}$, entering from
the left. The **gate** goes down to ground.

[table] **Common-gate terminal parameters** ·J p99–p100

| | Input | Output |
|---|---|---|
| voltage | $V_{GS}$ | $V_{DG}$ |
| current | $I_S$ | $I_D$ |
| impedance | $V_{GS}/I_S$ | $V_{DG}/I_D$ |
| power | $I_SV_{GS}$ | $I_DV_{DG}$ |

[eq: cg-gains-j] ·J p100

$$\boxed{\;A_i = \frac{I_D}{I_S}, \qquad A_v = \frac{V_{DG}}{V_{GS}}\;}$$

> [added] **The one number that falls straight out of that table.** Since $I_D \approx I_S$ (the gate
> takes nothing), the common-gate **current gain is $\approx 1$** — exactly as a BJT common-base stage
> has $A_i = \alpha \approx 1$. Its input impedance $V_{GS}/I_S$ is **low**, because the input now
> carries the full drain current, and its voltage gain is **non-inverting**. CG is the
> high-frequency / low-input-impedance configuration.

[table] **[added] The three configurations at a glance** — assembled from ·J p98–p100, with the
consequences the notes leave implicit

| | Common source | Common drain | Common gate |
|---|---|---|---|
| input at | gate | gate | **source** |
| output at | drain | **source** | drain |
| common terminal | source | drain | gate |
| $A_i$ (·J) | $I_D/I_G$ — very large | $I_S/I_G$ — very large | $I_D/I_S \approx 1$ |
| $A_v$ (·J) | $V_{DS}/V_{GS}$ | $V_{DS}/V_{DG} \approx 1$ | $V_{DG}/V_{GS}$ |
| input impedance | very high | very high | **low** |
| phase | **inverted** | in phase | in phase |
| BJT analogue | common emitter | common collector (emitter follower) | common base |
| use | general voltage amplifier | buffer / impedance converter | high-frequency stage |

---

## 7.21 Applications of FETs ·J p100 — and where the document stops

Five applications, and the reason given for each: ·J p100

1. **Input amplifiers in oscilloscopes, electronic voltmeters and other measuring and testing
   equipment** — because of the very high $R_{in}$, which **reduces the loading effect to a minimum**.
2. **Logic circuits** — kept **off** by a zero input and turned **on** with very little input power;
   the notes name **OR, NAND, AND and NOR** gates.
3. **Mixer operations** in FM and TV receivers.
4. **Voltage-variable resistors** in operational amplifiers.
5. **Large-scale-integration ICs and computer memories** — because they come in small sizes.

> ### ⚠ The document ends here
>
> **·J p100 is the last page.** The applications list finishes mid-page — "…because they come in small
> sizes." — and the remaining two-thirds of the page is blank. There is **no chapter summary, no
> tutorial problem set, no objective test, no reference list and no closing matter of any kind**. The
> FET material simply stops, in the middle of its own applications section, exactly as the BJT
> material before it ended on two unsolved problems (·J p83).
>
> **Consequence for revision:** this range supplies **three worked examples and one exercise** in
> total, all in the biasing section, and **no question bank at all**. For practice, use the tier-2
> file — see §7.23.

---

## 7.22 Formula summary for this range

Everything ·J p84–p100 needs for a numerical answer, in corrected form. Each entry names the flag
where the printed version differs.

[table]

| Quantity | Expression | Page | Flag |
|---|---|---|---|
| channel as a resistor | $I_D = V_{DS}/R_{DS}$ | ·J p85 | — |
| **Shockley's equation** | $I_D = I_{DSS}\left(1-\dfrac{V_{GS}}{V_{GS(\text{off})}}\right)^{2}$ | ·J p87 | **JV7.1** |
| cut-off and pinch-off | $\lvert V_P\rvert = \lvert V_{GS(\text{off})}\rvert$, $V_{GS(\text{off})} = -\lvert V_P\rvert$ (N-ch) | ·J p85–p87 | **JV7.1** |
| **E-MOSFET square law** | $I_D = K\left(V_{GS}-V_{GS(\text{th})}\right)^{2}$ | ·J p91, p92 | — |
| **$K$ from the ON point** | $K = \dfrac{I_{D(\mathrm{ON})}}{\left(V_{GS(\mathrm{ON})}-V_{GS(\text{th})}\right)^{2}}$ | ·J p97 | — |
| E-MOSFET saturation check | $V_{DS} \ge V_{GS} - V_{GS(\text{th})}$ | *[added]* | **JV7.8** |
| drain loop, any FET stage | $V_{DD} = I_DR_D + V_{DS} + I_SR_S$ | ·J p93 | — |
| node potentials | $V_D = V_{DD} - I_DR_D$, $\;V_S = I_SR_S$, $\;V_{DS} = V_D - V_S$ | ·J p93–p95 | — |
| **gate (separate-supply) bias** | $V_{GS} = -V_{GG} - I_SR_S$ | ·J p93 | **JV7.7** |
| **self bias** | $V_{GS} = -I_SR_S$ | ·J p93 | — |
| **source bias** | $V_{GS} = V_{SS} - I_SR_S$ ($V_{SS}$ = magnitude of the negative rail) | ·J p94 | — |
| **divider bias** | $V_{R_2} = \dfrac{V_{DD}R_2}{R_1+R_2}$, $\;V_{GS} = V_{R_2} - I_DR_S$ | ·J p94 | — |
| **drain-feedback bias** | $V_{GS} = V_{DS} = V_{DD}-I_DR_D$ | ·J p96 | **JV7.4** |
| E-MOSFET divider bias | as JFET divider, but $V_{GS} > V_{GS(\text{th})}$ and positive | ·J p96 | — |
| CS gains | $A_i = I_D/I_G$, $\;A_v = V_{DS}/V_{GS}$ (inverting) | ·J p98–p99 | — |
| CD gains | $A_i = I_S/I_G$, $\;A_v = V_{SD}/V_{GD} \approx 1$ | ·J p99 | **JC7.5** |
| CG gains | $A_i = I_D/I_S \approx 1$, $\;A_v = V_{DG}/V_{GS}$ | ·J p99–p100 | — |
| **[added]** square-law ratio shortcut | $\dfrac{I_{D2}}{I_{D1}} = \left(\dfrac{V_{GS2}-V_{GS(\text{th})}}{V_{GS1}-V_{GS(\text{th})}}\right)^{2}$ | *[added]* | — |

---

## 7.23 Cross-check against the tier-2 file `14-field-effect-transistors.md`

`14-field-effect-transistors.md` (source **L4**, 24 pp., a scanned run of a printed
electrical-technology textbook's **Chapter 63, "Field Effect Transistors"**, fully verified, 15
substantive and 21 cosmetic flags) covers the identical ground at greater length.

> ### The two documents are not independent
>
> **·J p95's first worked example is the textbook's Example 63.2** — same circuit, same
> $V_{DD} = 12\ \mathrm{V}$, $R = 1.5\ \mathrm{k\Omega}$, $R_S = 500\ \Omega$, $I_D = 4\ \mathrm{mA}$,
> same answer $V_{DS} = 4\ \mathrm{V}$.
> **·J p96–p97's E-MOSFET example is the textbook's Example 63.10** — same $25\ \mathrm{V}$, same
> $6\ \mathrm{k\Omega}$ / $9\ \mathrm{k\Omega}$ divider, same $1\ \mathrm{k\Omega}$ drain load, same
> $K = 0.16\ \mathrm{mA/V^2}$, same $V_{DS} = 9\ \mathrm{V}$.
> **·J p97's exercise is the textbook's Example 63.11** — identical wording, identical
> $1.44\ \mathrm{mA}$.
>
> The lecture notes are a **compilation from that chapter**. That is worth knowing for two reasons:
> the tier-2 file is a legitimate source of extra practice on exactly this syllabus, **and** where the
> two differ on a number, the tier-2 file usually shows what the lecture notes were transcribing —
> which is how **JV7.5**, **JV7.6** and **JV7.10** were confirmed.

### Where the two agree

[table]

| Point | This document (·J) | Tier 2 (·L4) | Verdict |
|---|---|---|---|
| **Shockley's equation** | printed twice on one page, once over $V_P$ and once over $V_{GS(\text{off})}$ ·J p87 | printed in the identical double form ·L4 p6 | **agree — including in the defect.** Both assert $V_P = V_{GS(\text{off})}$ |
| **The $V_P$ sign collision** | flagged **JV7.1**: $V_P$ defined on the $V_{DS}$ axis (·J p85–p86) but used as $V_{GS(\text{off})}$ (·J p87) | flagged **V4.2**: the same contradiction, spread over ·L4 p4–p8 and p15 | **agree — the same defect, inherited.** ·L4's exposure is worse (it puts *numbers* to a negative $V_P$ in three worked examples); ·J never puts a number to $V_P$ at all |
| **The corrected denominator** | §7.0 and §7.5: use $V_{GS(\text{off})}$, negative for N-channel | §4.4: use $V_{GS(\text{off})}$, negative for N-channel | **identical correction, arrived at independently** |
| **Self-bias** | $V_{GS} = -I_SR_S$ ·J p93 | $V_{GS} = -I_DR_S$ ·L4 p9 | **agree exactly** ($I_S = I_D$) |
| **Source bias** | $V_{GS} = V_{SS} - I_SR_S$ ·J p94 | $V_{GS} = V_{SS} - I_DR_S$ ·L4 p9 | **agree exactly**, and both take $V_{SS}$ as the *magnitude* of the negative rail |
| **Divider bias (JFET)** | $V_{R_2} = V_{DD}R_2/(R_1+R_2)$, $V_{GS} = V_{R_2}-I_DR_S$ ·J p94 | $V_{GS} = V_{DD}R_2/(R_1+R_2) - I_DR_S$ ·L4 p9 | **agree exactly** — same two-step form |
| **Drain-loop equation** | $V_{DD} = I_DR_D + V_{DS} + I_SR_S$ ·J p93 | same, as the load-line equation ·L4 p9 | agree |
| **E-MOSFET square law** | $I_D = K(V_{GS}-V_{GS(\text{th})})^2$ ·J p91, p92 | identical ·L4 p19 | **agree exactly** |
| **$K$ from the data sheet** | $K = I_D/(V_{GS}-V_{GS(\text{th})})^2$ ·J p97 | $K = I_{D(ON)}/(V_{GS}-V_{GS(\text{th})})^2$ ·L4 p19 | **agree on the formula**; ·L4's symbols are the better-labelled pair — see **JV7.9** |
| **Drain-feedback bias** | $V_{GS} = V_{DS}$ *(printed with a wrong minus sign — **JV7.4**)* | $V_{GS} = V_{DS}$, with the reason stated ·L4 p20 | **·L4 is right; ·J's sign is a slip** |
| **JFET construction and operation** | four cases, wedge-shaped depletion, pinch-off, cut-off ·J p84–p86 | four cases in the same order ·L4 p3–p5 | agree throughout |
| **DE MOSFET modes** | depletion by negative gate, enhancement by positive ·J p88–p89 | identical ·L4 p17 | agree |
| **Inversion layer / threshold** | "N-type inversion layer or virtual N-channel"; $V_{GS(\text{th})}$ is the minimum $V_{GS}$ that produces it ·J p90–p91 | identical account ·L4 p19 | agree |
| **Applications** | five items ·J p100 | the same five plus MOSFET handling ·L4 p23 | agree; ·L4 fuller |

### Where the two disagree

[table]

| Point | This document (·J) | Tier 2 (·L4) | Which to teach |
|---|---|---|---|
| **Separate-supply / gate-bias circuit** | rail $-V_{GG}$ on $R_G$ **and** an $R_S$ in the source ·J p93 | gate bias has **no source resistor** — source straight to ground ·L4 p9, Fig. 63.8(a) | **Different circuits, so different equations.** ·L4's gives $V_{GS} = -V_{GG}$; ·J's needs $V_{GS} = -V_{GG}-I_SR_S$, which is **not** what ·J prints — see **JV7.7** |
| **E-MOSFET divider circuit** | the ·J p96 figure draws an $R_S$ bypassed by $C_S$, but the example then sets $R_S = 0\ \Omega$ | Fig. 63.31(b) has **no source resistor at all**, and ·L4 says why: a source resistor would *fight* a positive $V_{GS}$ | **·L4's reasoning.** ·J's figure is the JFET divider redrawn; its own example neutralises the $R_S$ it draws |
| **E-MOSFET drain-loop symbol** | $V_{DS} = V_{DD} - I_SR_S$ (with $R_S = 0$!) ·J p97 — **JV7.6** | $V_{DS} = V_{DD} - I_DR_L$ ·L4 p20 | **·L4.** ·J's is a transcription slip on the same worked example |
| **The 5 V in the E-MOSFET exercise** | called $V_{GS(\text{off})}$ ·J p97 — **JV7.10** | called $V_{GS(th)}$ ·L4 p21 | **·L4.** Same problem, same answer, correct label |
| **E-only static characteristics** | the DE MOSFET figure reproduced unchanged, with $I_{DSS}$ and a depletion mode ·J p91 — **JV7.2**, **JV7.3** | Fig. 63.30: positive-$V_{GS}$ curves only, no $I_{DSS}$, no depletion mode ·L4 p20 | **·L4's figure, without qualification.** ·J p91's is wrong for the device it labels |
| **Common-source phase** | $A_v = V_{DS}/V_{GS}$, unsigned ·J p99 | $A_v = -g_m(r_d\parallel R_L)$ — inversion stated and drawn ·L4 p12 | **·L4.** The inversion is real and is examinable |
| **Common-drain subscripts** | $V_{DG}$, $V_{DS}$ ·J p99 — **JC7.5** | $V_o/V_i$ with an explicit a.c. equivalent ·L4 p13–p14 | **·L4.** ·J's ratio is numerically right, its subscript order is not |

### Where each source is the only one

[table]

| Topic | Only in | Note |
|---|---|---|
| **Small-signal parameters — $r_d$, $g_m$, $\mu$, $R_{DS}$** | **·L4** (§4.8) | **·J does not treat them at all.** ·J p92 names "the forward trans-conductance" once, in a shopping list of purchase parameters, and never defines it, gives its formula, or uses it. ·L4 gives $r_d = \delta V_{DS}/\delta I_D$, $g_m = \delta I_D/\delta V_{GS}$, the differentiated form $g_m = -\frac{2I_{DSS}}{V_P}(1-\frac{V_{GS}}{V_P})$, and $\mu = g_mr_d$, with a worked example (63.1) |
| **$g_{mo} = 2I_{DSS}/\lvert V_{GS(\text{off})}\rvert$** | **·L4** (§4.8) | **Absent from ·J entirely** — the symbol $g_{mo}$ never appears in ·J p84–p100. So is $g_m = g_{mo}\sqrt{I_D/I_{DSS}}$ |
| **Amplifier gain formulas** — $A_v = -g_m(r_d\parallel R_L)$ (CS), $\cong 1$ (CD), $+g_m(r_d\parallel R_L)$ (CG), $r_i = 1/g_m$ (CG) | **·L4** (§4.12) | **·J gives only ratios of terminal quantities** (§7.20): $V_{DS}/V_{GS}$, $V_{DS}/V_{DG}$, $V_{DG}/V_{GS}$. Those are definitions of gain, not expressions for it — **nothing in ·J lets you compute a number.** For any question asking for a gain in dB or in V/V, ·L4 is the only source |
| **The FET d.c. load line, the Q-point construction and mid-point bias** | **·L4** (§4.10) | **Absent from ·J.** ·J uses $V_{GSQ}$, $V_{DSQ}$ and $I_{DQ}$ as symbols in one example (·J p95) and never draws a load line. ·L4 gives both intercepts, mid-point bias ($V_{DSQ} = \frac12V_{DD}$, $V_{GS} = V_{GS(\text{off})}/4$, $I_D \cong I_{DSS}/2$) and three worked examples |
| **Input capacitance and the Miller effect** | **·L4** (§4.12) | $C_i = C_{gs} + (1-A_v)C_{gd}$, and why it is absent in CD and CG stages. ·J lists "input capacitance" as a purchase parameter and stops |
| **Inverse Shockley, $V_{GS} = V_{GS(\text{off})}(1-\sqrt{I_D/I_{DSS}})$** | **·L4** (§4.7) | ·J never inverts the square law |
| **$V_{DS(P)} = V_P + V_{GS}$ — pinch-off at any bias** | **·L4** (§4.6) | ·J states the *effect* in words ("as $V_{GS}$ is made more -ve, values of $V_P$ as well as breakdown voltage are decreased", ·J p86) but gives no relation |
| **Advantages and disadvantages of FETs; MOSFET handling precautions** | **·L4** (§4.13, §4.23) | absent from ·J |
| **Practice questions** | **·L4** (§4.14, §4.24, §4.25) | two tutorial sets and an objective test, 25 questions, all recomputed. **·J has three worked examples and one exercise, and no question bank** |
| **Schematic symbols for the three- and four-terminal DE MOSFET** | **·L4** (§4.17) | ·J draws the four-terminal symbol only, inside the construction figures |
| **JFET purchase-parameter checklists** | **·J** (§7.12) | the nine-item JFET list and six-item MOSFET list are **not in ·L4** — this is one of the few places the lecture notes add material |
| **The three configurations as terminal-parameter tables** | **·J** (§7.20) | ·L4 derives gains from a.c. equivalents; ·J's input/output/impedance/power tables are its own presentation, and are the form an examination following these notes would most likely ask for |
| **A JFET divider-bias example with megohm resistors** | **·J** (§7.15) | $R_1 = 15.7\ \mathrm{M\Omega}$, $R_2 = 1\ \mathrm{M\Omega}$ — **not from ·L4**, whose divider examples use kilohms. This is the lecture notes' own numerical example |

> ### How to use the two together
>
> 1. **Learn the shape of the syllabus from ·J** — it is what the course teaches, and its
>    presentation (terminal-parameter tables, purchase checklists, four bias schemes) is what an
>    examination will mirror.
> 2. **Take every gain calculation, every small-signal parameter and all practice questions from
>    ·L4.** ·J simply does not contain them.
> 3. **Where a number differs, check ·L4 first** — three of this file's ten substantive flags were
>    confirmed by finding the same example printed correctly there.

---

## 7.24 Coverage, emphasis and exam triage

**What this range is.** Seventeen pages, and the balance is lopsided in a way that should set the
study balance: **·J p84–p92 is nine pages of descriptive device physics with two equations in it**
(Shockley, and the E-MOSFET square law); **·J p92–p97 is six pages of biasing, and every number in
the range lives there**; **·J p97–p100 is four pages of amplifier and configuration description with
no worked numbers at all.**

**Highest exam value — work these until they are automatic:**

1. **The four JFET bias schemes and their four equations** (§7.13). Stated as a list, drawn as four
   figures, then executed twice on numbers. This is the core of the range.
2. **The two worked bias examples** (§7.14, §7.15). Both are short, both have clean answers
   ($V_{DS} = 4\ \mathrm{V}$; $V_{GSQ} = -1.8\ \mathrm{V}$, $V_{DSQ} = 12.5\ \mathrm{V}$), and one of
   them is lifted verbatim from a past university paper via the textbook — precisely the shape of
   question a CAT reproduces.
3. **The E-MOSFET square law and the $K$-from-data-sheet step** (§7.10, §7.17, §7.18). Three
   appearances in two pages, one worked example and one exercise, and a two-line method. The single
   most efficient thing to learn in the MOSFET half.
4. **Redrawing the three transfer characteristics** (§7.6, §7.9, §7.11) and knowing which starts
   where. The comparison table in §7.11 is the whole answer to "distinguish between a JFET, a DE
   MOSFET and an E-only MOSFET", which is the most obviously examinable descriptive question here.
5. **The drain characteristic with its four regions named** (§7.4) — ohmic, pinch-off/saturation,
   breakdown, cut-off, with $V_P$ and $V_A$ on the $V_{DS}$ axis.

**Moderate value — know the statements and be able to sketch:**

6. **JFET operation in the four cases** (§7.3) and the origin of pinch-off. Descriptive, but it is
   nine pages of the range and it carries the definitions of $I_{DSS}$, $V_P$ and
   $V_{GS(\text{off})}$.
7. **MOSFET construction and the two modes** (§7.7, §7.8, §7.10) — four figures, and the "insulated
   gate ⇒ either polarity ⇒ capacitor" chain.
8. **The three configurations** (§7.20). Short, tabular, and the comparison table is quotable. But
   note that **no gain can be computed from what this document gives**.
9. **The two purchase-parameter checklists** (§7.12) — pure recall, one mark each, cheap to learn.

**Low value here:**

10. **·J p91's static-characteristic figure and its bullets** — they are wrong for the device they
    label (**JV7.2**, **JV7.3**). Learn ·J p92's transfer characteristic instead.
11. **The amplifier signal-swing figures** (§7.19) — they say only that the input swings $V_{GS}$
    and the output swings $I_D$. Worth one sketch each, no more.

**Three things this range does not teach at all:** the **small-signal parameters** ($r_d$, $g_m$,
$\mu$), the **FET load line and Q-point construction**, and **any expression from which an amplifier
gain can be calculated**. All three are in `14-field-effect-transistors.md`, and §7.23 says where.

---

## 7.25 Typography and word slips, collected

> ⚠ VERIFY **JC7.2** ·J p90, ·J p92 — **"MOSEFET" for "MOSFET"**, twice, both times in a heading:
> "ENHANCEMENT ONLY N-CHANNEL **MOSEFET** (NMOS)" and "Parameters considered when purchasing
> **MOSEFET**(s)". The correct expansion is **m**etal-**o**xide-**s**emiconductor **f**ield **e**ffect
> **t**ransistor. See `_verification-log.md`.

> ⚠ VERIFY **JC7.3** ·J p91, ·J p92 — the constant of the E-MOSFET square law is typeset **capital
> $K$** in the equation and **lower-case k** in the sentence beneath it: "Where **k** is constant
> which depends on a particular MOSFET." Both occurrences do this. Use **$K$**; lower-case $k$ is
> Boltzmann's constant elsewhere in this knowledge base (·J p35, `04-diodes.md` §4.6).
> See `_nomenclature.md`.

> ⚠ VERIFY **JC7.7** ·J p88 — "the gate is insulated from its conducting channel by an ultra thin
> **metal oxide** insulating film of silicon dioxide". **Silicon dioxide is not a metal oxide** —
> silicon is a metalloid. The "MOS" in MOSFET names the **sandwich** (metal gate / oxide /
> semiconductor), not the composition of the oxide. Read as: "…insulated by an ultra-thin film of
> silicon dioxide, the oxide layer of the metal-oxide-semiconductor sandwich". Nothing computed
> changes. See `_verification-log.md`.

> ⚠ VERIFY **JC7.8** — spelling and word-substitution slips across ·J p84–p100, gathered here because
> none of them changes anything computed. Listed so a reader meeting them on the page knows they are
> the source's, not a misreading.
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·J p84 | "an N-channel **JEET** is discussed" | JFET |
> | ·J p86 | "As $V_{GS}$ is **increased to the -ve**, a point is reached when the 2 depletion regions touch" | as $V_{GS}$ is made **more negative** — "increased" and "-ve" pull opposite ways |
> | ·J p86 | "the polarities of both $V_{DD}$ and **VGS** are reversed" | $V_{GS}$ — the subscript formatting is lost on this one occurrence only |
> | ·J p87 | "A transistor operated in this region **is a like** a switch which is on" (and again for the cut-off region) | is **like** |
> | ·J p90 | "This thin layer provides the channel with electrons hence **N-types material** referred to as N-type inversion layer" | N-type material |
> | ·J p90 | "It operates with the **+ve gates** only" | +ve **gate** |
> | ·J p92 | "The **switching consideration**" *(JFET purchase list, item 7)* | switching **characteristics** — the MOSFET list on the same page uses the correct term |
> | ·J p100 | "**Voltage variables resistors** in operational amplifiers" | voltage-**variable** resistors |
>
> See `_verification-log.md`.

---

## 7.26 Items needing a clean page

Listed for the record; everything else in ·J p84–p100 is fully recovered.

| Item | Page | Status |
|---|---|---|
| The chapter heading above the FET introduction | ·J p84 | **lost with the blank space** — not a redaction. Never fill it |
| The sub-heading **"a) When $V_{DS} = 0$"** | ·J p85 | **lost at the page break** — the sequence resumes at **b)** on the same page |
| The names of the **two MOSFET types** | ·J p87 | ⚠ REDACTED — **substance recovered with high confidence** (DE MOSFET and enhancement-only MOSFET, from the two headings that follow); **exact wording not recovered**. A screenshot would settle it |
| A construction bullet, two lines (≈139 characters) | ·J p88 | ⚠ REDACTED — **not recovered**; needs a screenshot of ·J p88 |
| A bullet under the DE MOSFET static characteristics, two lines (≈118 characters) | ·J p89 | ⚠ REDACTED — **not recovered**; needs a screenshot of ·J p89 |
| The sub-heading **"c) Source biasing"** | ·J p94 | **lost at the page break** — the sequence resumes at **d)** on the same page |
| The label **"Example"** above the first worked problem | ·J p95 | **lost at the page break** — the second problem on the page is labelled |
| The two numerators of the divider expression on the top line | ·J p97 | ⚠ ILLEGIBLE — **clipped by the page margin**; both recovered with certainty from ·J p96's data and from the arithmetic ($25\times9/15 = 15$). Logged as **JC7.6** |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
