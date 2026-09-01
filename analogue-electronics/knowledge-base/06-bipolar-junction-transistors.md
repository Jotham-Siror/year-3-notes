---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "06 — Bipolar Junction Transistors"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 57-83"
pages: "J p57-p83"
tier: primary
file_role: topic
subtopics:
  - "what a transistor is; BJT against FET; the transfer-resistor name"
  - "NPN construction, circuit symbol, two-diode analogue, doping levels of emitter, base and collector"
  - "NPN operation; the 5 % / 95 % division of emitter current; I_E = I_C + I_B"
  - "PNP construction and operation"
  - "the three modes of connection: common base, common emitter, common collector"
  - "CB parameter list and alpha; CE parameter list and beta; CC parameter list and unity voltage gain"
  - "h-parameter symbol conventions; power, voltage and current gain in decibels"
  - "relations between alpha, beta and theta"
  - "leakage currents I_CBO and I_CEO, their derivations, and I_C = beta.I_B + I_CEO"
  - "thermal runaway and the Si / Ge leakage-doubling temperatures"
  - "CB static characteristics: input, output and transfer"
  - "CE static characteristics: input, output (saturation, cut-off, active, breakdown) and transfer"
  - "CC static characteristics: input, output and transfer; V_CE = V_CB + V_BE"
  - "six methods of biasing: base bias, emitter feedback, collector feedback, both feedbacks, two supplies, voltage divider"
  - "voltage-divider bias and its Thevenin reduction"
  - "the CE amplifier: coupling and decoupling capacitors and the role of each component"
  - "dc equivalent circuit, I_C(sat) = V_CC/(R_C + R_E), dc load line and Q point"
  - "saturation clipping and cut-off clipping"
  - "ac equivalent circuit, R_ac = R_C.R_L/(R_C + R_L), the ac load line and peak-to-peak swing"
  - "causes of Q-point drift; the stability factor and its derivation"
  - "design of a single-stage low-power amplifier; germanium CE operating-point example"
key_equations: [j-ie-ic-ib, j-alpha, j-beta, j-theta, j-alpha-beta, j-power-gain-db, j-ic-leakage-cb, j-iceo, j-ic-with-leakage, j-cc-vce, j-base-bias, j-emitter-feedback, j-collector-feedback, j-both-feedbacks, j-two-supply, j-divider-thevenin, j-ic-sat, j-dc-load-line, j-q-point, j-rac, j-ac-load-line, j-vpp, j-stability-factor]
prerequisites: ["01-matter-atoms-and-semiconductors (doping, majority and minority carriers)", "04-diodes (P-N junction, forward and reverse bias, reverse saturation current, knee voltage)"]
leads_to: ["07 (field-effect transistors)", "16-h-parameters-and-bjt-amplifiers (small-signal models built on this file's h-parameter table)", "17-multistage-feedback-frequency-response"]
verification_flags: 29
tags: [bjt, transistor, npn, pnp, alpha, beta, common-base, common-emitter, common-collector, leakage-current, icbo, iceo, thermal-runaway, static-characteristics, biasing, voltage-divider-bias, thevenin, load-line, q-point, clipping, ac-load-line, stability-factor, amplifier-design]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's own numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·J pN = provenance (which PDF page of the primary lecture notes the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ REDACTED = text destroyed by an opaque block in the source PDF ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 06 — Bipolar Junction Transistors

Scope: **·J p57–p83**, twenty-seven pages — the largest single block of the primary lecture notes and
the most heavily examined. It runs the device end to end: what a transistor is, how an NPN and a PNP
are built and how each works, the three modes of connection with their parameter lists and current
gains, leakage and thermal runaway, all three families of static characteristics, the six methods of
biasing, the common-emitter amplifier with its capacitors, the dc and ac load lines, the Q point and
how it clips, the stability factor, and two worked design/analysis examples ending in two unsolved
problems.

**Citation and page offset.** `·J p57` means **PDF page 57**. The document's own printed page number
runs **one behind** the PDF page — PDF p57 is printed "56" — and the offset holds unbroken across
this whole range (PDF p83 is printed "82"). Only PDF pages are cited below.

---

## 6.0 What this range contains, and where its gaps are

This is one continuous argument — device physics → configurations → characteristics → biasing →
amplifier → load lines → design. **It is deliberately not split.** The tier-2 chapter covering the
same ground (`13-bipolar-junction-transistor.md`, 152 KB) stayed whole for the same reason.

[table] **Gaps and defects in the source pages, recorded before anything is taught from them**

| Page | What is wrong | Handled in |
|---|---|---|
| ·J p57 | the transistor section **opens with no heading** — lost with the blank space above it | §6.1 |
| ·J p57→p58 | the sentence broken by the page break repeats itself; a line looks lost or duplicated | **JC6.1** |
| ·J p58 | **two green opaque blocks** destroy roughly two lines stating the condition for effective operation | §6.4, **⚠ REDACTED** |
| ·J p61 | the h-parameter table's **column headings are absent** at the top of the page | §6.8, **JC6.4** |
| ·J p62 | the CE current-gain line has **dropped out of the render** | §6.9, **⚠ ILLEGIBLE** |
| ·J p65 | the static-characteristics section **opens with no heading** | §6.14 |
| ·J p73 | the two-supply emitter-bias circuit **appears with no heading** | §6.23 |
| ·J p79 | the ac-load-line section **opens with no heading** | §6.29 |
| ·J p81 | the stability-factor section **opens with no heading** | §6.31 |
| ·J p82 | the **first line is clipped by the page top**; only fragments survive | §6.32, **JC6.15** |

Nothing below is invented to paper over any of these. Where a value cannot be recovered, it says so.

---

## 6.1 What a transistor is ·J p57

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $E$, $B$, $C$ | emitter, base, collector terminals | — | — |
| $J_1$, $J_2$ | the emitter–base and collector–base junctions | — | — |
| $I_E$ | emitter current | A (usually mA) | 1–10 mA |
| $I_C$ | collector current | A (usually mA) | 1–10 mA |
| $I_B$ | base current | A (usually µA) | 10–100 µA |

> **Note on the heading.** ·J p57 begins the transistor material at the top of the page with **no
> visible heading**. The heading appears to have been lost with the blank space above it. The
> section title used here is ours.

[def] A **transistor** is an **active device** — one that can increase the strength of a signal. It
is made from p-type and n-type semiconductor material. ·J p57

The name is a contraction: **transistor = transfer resistor**. ·J p57

[table] **The two families** ·J p57

| Family | Full name | What the notes say it does |
|---|---|---|
| **BJT** | bipolar junction transistor | linear amplifier, to boost an electrical signal; also an **electronic switch** |
| **FET** | field-effect transistor | (named only; developed later in the course) |

### The bipolar junction transistor ·J p57

[def] A BJT is built by **sandwiching** one type of material between two of the other:

- an n-type layer between two p-type layers, **or**
- a p-type layer between two n-type layers.

It uses **both electrons and holes** as charge carriers — which is exactly what *bipolar* means. ·J p57

It has **two junctions**, $J_1$ and $J_2$, and **three terminals**: ·J p57

| Terminal | What it does ·J p57 |
|---|---|
| **emitter** | emits the majority charge carriers |
| **base** | controls the carriers moving from emitter to collector |
| **collector** | collects the charge carriers |

Two types exist: **PNP** and **NPN**. ·J p57

---

## 6.2 NPN construction ·J p57

[fig ·J p57] **Three drawings side by side.**

1. **Block diagram.** A horizontal rectangle split into three cells reading **N | P | N** left to
   right. A lead labelled **E** leaves the left cell, a lead labelled **C** leaves the right cell,
   and a lead labelled **B** drops vertically from the centre cell.
2. **Two-diode analogue.** The same three terminals, but the body replaced by two diode symbols in
   series: from **E** a diode whose **arrowhead points left, toward E**, then the **B** tap dropping
   from the mid-node, then a second diode whose **arrowhead points right, toward C**. Both diodes
   therefore have their **anodes at the base** — they are drawn **back to back**.
3. **Circuit symbol.** The standard NPN: **C** at the top, **E** at the bottom, **B** entering from
   the left; the emitter lead carries an **arrowhead pointing away from the base** (outward).

[def] An NPN is a **p-type layer sandwiched between two n-type layers**. It behaves like **two diodes
connected back to back**. The **arrow in the circuit symbol shows the direction of current** when the
transistor is operating. ·J p57

---

## 6.3 Why the three regions are doped and sized as they are ·J p57–p58

| Region | Size | Doping | Reason given in the notes |
|---|---|---|---|
| **emitter** | — | **heavily doped** | so that it can emit a **large** number of majority carriers (electrons in an NPN) ·J p57 |
| **base** | **very thin** | **very lightly doped** | so carriers cross from emitter to collector in the **minimum time**, and the base current is kept small ·J p57–p58 |
| **collector** | **larger than the other two** | **moderately doped** | large size lets it **dissipate a large amount of power without damage** ·J p58 |

The notes attach two formulas to the collector argument: ·J p58

$$P = I_C^{2}R$$

$$R = \rho\,\frac{L}{A}$$

where $P$ is the power dissipated in the collector region (W), $I_C$ the collector current (A), $R$
the resistance of that region ($\Omega$), $\rho$ the resistivity ($\Omega\,\mathrm{m}$), $L$ its
length (m) and $A$ its cross-sectional area (m²).

> ⚠ VERIFY **JV6.1** ·J p58 — the reason given for *moderate* collector doping is the wrong way round
>
> The page prints: *"Moderate doping also reduced the amount of power dissipated."*
>
> **Correct form:** it is the **large cross-sectional area** $A$, not the moderate doping, that lowers
> $R$ and therefore $P = I_C^{2}R$.
>
> **Why.** Read the page's own two formulas together. Lighter doping means **fewer carriers**, hence
> **larger** $\rho$, hence — at fixed $L$ and $A$ — **larger** $R$ and **larger** $I_C^{2}R$. So
> moderate doping *increases* the dissipation for a given current; only the large $A$ reduces it. The
> real reason collectors are moderately doped is different: a lightly doped collector lets the
> collector–base depletion layer spread into the collector, which **raises the reverse breakdown
> voltage** of that junction. See `_verification-log.md`.

> ⚠ VERIFY **JC6.1** ·J p57→p58 — the sentence across the page break repeats itself
>
> ·J p57 ends *"...and reduce the base current by"* and ·J p58 opens *"collector current and reduce
> the base current. (Transistor amplifier)"*.
>
> **What the sentence needs:** a clause of the form *"...by minimising recombination, which increases
> the collector current and reduces the base current."* A line appears to have been lost or
> duplicated at the page break. The physics is not in doubt — a thin, lightly doped base gives few
> recombination events, so nearly all the injected carriers reach the collector. See
> `_verification-log.md`.

---

## 6.4 NPN operation ·J p58

[fig ·J p58] **Two drawings side by side.**

1. **Symbol with bias polarities.** The NPN symbol upright. The **collector at the top** is annotated
   **"++ more positive"**, the **base at the left** is annotated **"+ve"**, the **emitter at the
   bottom** is annotated **"−ve"**.
2. **Block diagram with currents and batteries.** The **N | P | N** block, with junctions labelled
   **$J_1$** (between the first N and the P) and **$J_2$** (between the P and the second N). The
   **$J_1$ depletion layer is drawn solid black and narrow**; the **$J_2$ depletion layer is drawn
   hatched and wider**. **$I_E$** is arrowed leaving the emitter to the left, **$I_C$** arrowed
   entering from the right, **$I_B$** arrowed upward into the base from below. A battery sits in the
   emitter loop and another in the collector loop, both returning to the base node.

> ⚠ REDACTED **·J p58** — two green opaque blocks cover roughly two lines. The sentence reads:
> *"For a transistor to effectively operate the* ▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ *...* ▮▮▮▮▮▮▮▮▮▮▮ *This is done by
> connecting the emitter to negative potential, the base to positive potential and the collector to
> more positive potential."*
> **What the sentence needs: the bias condition on the two junctions.**

> [added] **The covered condition is certain, and it is this:**
>
> $$\boxed{\;\text{emitter–base junction FORWARD biased};\qquad \text{collector–base junction REVERSE biased}\;}$$
>
> Three independent confirmations, all inside this same range, make the inference safe:
> 1. the surviving second half of the very same sentence gives exactly the potentials that produce
>    those two conditions in an NPN — emitter negative, base positive (so $J_1$ forward), collector
>    more positive still (so $J_2$ reverse);
> 2. **·J p59** states the identical condition in full for the PNP: *"The B–E junction is forward
>    biased while the collector–base junction is reverse biased"*;
> 3. **·J p60** restates it as a rule for all three configurations: *"All the common connections
>    should maintain a forward bias for the B–E junction and a reverse bias for the C–B junction."*
>
> These are our words, not the lecturer's, and they are supplied only because three surviving
> passages say the same thing.

**How the current divides.** ·J p58

- The **negative potential at the emitter repels the electrons**, which are the majority carriers
  there.
- Reaching the base, **very few** recombine with holes — that recombination is the **base current**
  $I_B$, about **5 %**.
- The rest are pulled across by the **more positive collector**, passing through the base to form the
  **collector current**, about **95 %**.

**Base and collector cannot be interchanged**, because their doping levels differ. ·J p58

[eq: j-ie-ic-ib] By Kirchhoff's current law: ·J p58, restated with the percentages on ·J p60

$$\boxed{\;I_E = I_C + I_B\;}$$

$$\underbrace{I_E}_{100\,\%} = \underbrace{I_C}_{95\,\%} + \underbrace{I_B}_{5\,\%}$$

> ⚠ VERIFY **JC6.2** ·J p58 — the collector share is printed as two different numbers
>
> The page prints $I_B$ **(5 %)** and, one line later, the collector current as **"(95 % /98 %)"**.
>
> **Why it matters:** $5 + 95 = 100$ ✓ but $5 + 98 = 103$ ✗. The pair must sum to 100 %. ·J p59 gives
> the base share as **2 %–5 %** and the collector share as 95 %; ·J p60 tabulates 100 / 95 / 5.
>
> **Read the pair as $(\alpha,\ 1-\alpha)$:** either $(0.95,\ 0.05)$ or $(0.98,\ 0.02)$, never a
> mixture. See `_verification-log.md`.

> [added] **What each split implies for $\beta$.** With $\alpha = 0.95$, $\beta = 0.95/0.05 = 19$;
> with $\alpha = 0.98$, $\beta = 0.98/0.02 = 49$. A 3-point change in $\alpha$ multiplies $\beta$ by
> 2.6 — which is exactly why $\beta$ is the unreliable parameter and $\alpha$ the stable one.

---

## 6.5 PNP construction and operation ·J p59

[fig ·J p59] **Construction, three drawings.**

1. **Block diagram** **P | N | P**, with **E** left, **C** right, **B** dropping from the centre.
2. **Two-diode analogue:** from **E** a diode with its **arrowhead pointing right, into the base
   node**, then the **B** tap, then a diode with its **arrowhead pointing left, into the base node**.
   Both **cathodes at the base** — drawn **front to front**.
3. **Circuit symbol:** **C** top, **E** bottom, **B** from the left, the emitter arrowhead pointing
   **into the base** (inward).

[def] A PNP is an **n-type layer sandwiched between two p-type layers** — like **two diodes connected
front to front**. The arrow again gives the direction of current in operation. **The sizes and doping
levels of emitter, base and collector are the same as in the NPN.** ·J p59

[fig ·J p59] **Operation, two drawings.** The PNP symbol with **collector marked "−− more negative"**,
**base marked "−ve"**, **emitter marked "+ve"**; beside it a block diagram with junctions $J_1$ and
$J_2$ marked, $J_1$'s depletion layer solid black and $J_2$'s hatched.

> ⚠ VERIFY **JC6.3** ·J p59 — the PNP operation diagram is drawn as an NPN
>
> The block diagram in the **Operation** part of the PNP page reads **N | P | N**, copied from ·J p58.
> The construction diagram immediately above it on the same page correctly reads **P | N | P**.
>
> **Correct form:** the operation block diagram should read **P | N | P**, E on the left, C on the
> right. Nothing in the surrounding physics changes. See `_verification-log.md`.

**Operation as the page states it** ·J p59

- The **B–E junction is forward biased**; the **C–B junction is reverse biased**.
- This is arranged by putting the **emitter at positive potential**, the **base at negative
  potential**, and the **collector at a more negative potential**.
- The positive emitter **repels holes** (the majority carriers there); they move through the base,
  attracted by the more negative collector.
- A few recombine in the base to give **$I_B$ (2 %–5 %)**; the rest reach the collector as **$I_C$
  (95 %)**.

> [added] **The one-line contrast worth carrying into an exam.** NPN and PNP differ only in *which
> carrier does the work* and *which way every polarity points*. Every equation in the rest of this
> file — $I_E = I_C+I_B$, $\alpha$, $\beta$, the load lines — is identical for both.

---

## 6.6 The three modes of connection ·J p60

[def] A transistor has **three terminals**, but an input port needs two and an output port needs two.
So **one terminal is made common** to input and output, and that common terminal is **usually
grounded**. ·J p60

**Whichever terminal is made common, the bias rule does not change:** ·J p60

$$\boxed{\;\text{B–E junction forward biased},\qquad \text{C–B junction reverse biased}\;}$$

The three configurations are **common base (CB)**, **common emitter (CE)** and **common collector
(CC)**, each used for different applications. ·J p60

---

## 6.7 Common-base connection ·J p60

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{EE}$ | emitter-side supply | V | 1–5 V |
| $V_{CC}$ | collector-side supply | V | 9–20 V |
| $V_{BE}$ | base–emitter voltage (the CB **input** voltage here) | V | 0.7 V (Si), 0.3 V (Ge) |
| $V_{CB}$ | collector–base voltage (the CB **output** voltage) | V | 5–20 V |
| $\alpha$ | CB forward current gain, $=h_{FB}$ | dimensionless | 0.95–0.99 |
| $h_{IB}$ | CB input resistance | $\Omega$ | 20–50 $\Omega$ |

[fig ·J p60] **CB test circuit.** The transistor is drawn on its side with the **base dropping to
ground** through the arrow marked **$I_B$**. On the left, **$V_{EE}$** drives the emitter loop, which
is labelled **input**, with **$I_E$** arrowed into the emitter. On the right, a second battery drives
the collector loop, labelled **output**, with **$I_C$** arrowed into the collector. Both loops return
to the common base node, which carries the ground symbol.

*"Negative potential obtained by rectification on lower side of the time line. The base is common to
the input and the output."* ·J p60

[table] **The CB parameter list, exactly as the page sets it out** ·J p60

| | Input side | Output side |
|---|---|---|
| current | $I_E$ | $I_C$ |
| voltage | $V_{BE}$ | $V_{CB}$ |
| resistance | $\dfrac{V_{BE}}{I_E} = h_{IB}$ | $\dfrac{V_{CB}}{I_C} = h_{OB}$ |
| power | $I_E V_{BE}$ | $I_C V_{CB}$ |

[eq: j-alpha] **Current gain** ·J p60

$$\boxed{\;\frac{I_C}{I_E} = \alpha = h_{FB}\;}$$

$\alpha$ **measures the quality of a transistor** — the higher $\alpha$, the more closely $I_C$
equals $I_E$. ·J p60

$$I_C = \alpha I_E$$

$$I_B = I_E - I_C = I_E - \alpha I_E = (1-\alpha)I_E$$

> ⚠ VERIFY **JV6.2** ·J p60, ·J p61 — the output resistance is equated to $h_{OB}$, which is an
> *admittance*
>
> Both pages print: *"Output resistance $= \dfrac{V_{CB}}{I_C} = h_{OB}$."*
>
> **Correct form:**
> $$\boxed{\;h_{OB} = \frac{I_C}{V_{CB}}\ \ [\mathrm{S}],\qquad \text{output resistance} = \frac{V_{CB}}{I_C} = \frac{1}{h_{OB}}\;}$$
>
> **Why.** In the hybrid set, $h_o$ is the **output admittance**, measured in siemens; $V/I$ is a
> resistance in ohms. The two cannot be equal. The same document gets the CE version right two pages
> later — ·J p62 prints $h_{OE} = I_C/V_{CE} = 1/r_o$, current over voltage, which is the correct
> shape. See `_verification-log.md` and `16-h-parameters-and-bjt-amplifiers.md` §on the h-set.

> [added] **A second, smaller point about $h_{FB}$.** With the strict sign convention (all currents
> taken *into* the device) the CB forward transfer ratio is $h_{FB} = -\alpha$. The notes drop the
> sign, as almost all texts do in practice, and use magnitudes throughout. Nothing computed changes.

**Application of the CB connection: impedance matching.** ·J p61

---

## 6.8 h-parameter symbols, and gain in decibels ·J p61

[table] **Symbol conventions as the page tabulates them** ·J p61

| Quantity | ac (small-signal) | dc | total instantaneous |
|---|---|---|---|
| emitter current | $i_e$ | $I_E$ | $i_E$ |
| collector current | $i_c$ | $I_C$ | $i_C$ |
| base current | $i_b$ | $I_B$ | $i_B$ |
| base–emitter voltage | $v_{be}$ | $V_{BE}$ | $v_{BE}$ |
| hybrid parameter | $h_{ib}$ | $h_{IB}$ | $h_{IB}$ |

> ⚠ VERIFY **JC6.4** ·J p61 — the table has no column headings, and its last row repeats itself
>
> The table sits at the very top of ·J p61 and its **header row is absent** — the three symbol
> columns are unlabelled. The **"Hybrid"** row prints **$h_{IB}$ twice**, in both the third and
> fourth columns.
>
> **Correct form:** the columns are, by the universal convention the rest of the table obeys,
> **ac / dc / total instantaneous**; and the total-instantaneous hybrid entry should be $h_{iB}$
> (lower-case letter, upper-case subscript), not a second $h_{IB}$.
>
> **Why the convention is certain:** every other row already follows it — lower-case symbol with
> lower-case subscript for ac ($i_e$), upper-case with upper-case for dc ($I_E$), lower-case symbol
> with upper-case subscript for the total ($i_E$). Only the last row breaks the pattern.
> See `_verification-log.md`.

**The other CB ratios on the page** ·J p61

$$\text{reverse voltage gain} = \frac{V_{BE}}{V_{CB}} = h_{RB} \qquad\qquad
\text{voltage gain} = \frac{V_{CB}}{V_{BE}}$$

$$\text{input impedance} = h_I \qquad \text{output admittance} = h_o \qquad
\text{forward current gain} = h_f \qquad \text{reverse voltage gain} = h_r$$

*(the page writes the last of the four generic symbols as $h_{RB}$ — the CB-specific form — inside an
otherwise generic list; read it as $h_r$.)*

[eq: j-power-gain-db] **Power gain** ·J p61

$$\boxed{\;A_p = \frac{\text{output power}}{\text{input power}} = \frac{V_{CB}I_C}{V_{BE}I_E}\;}$$

with $A_v$ the voltage gain and $A_i$ the current gain, all three dimensionless. In decibels: ·J p61

$$\boxed{\;\text{power gain (dB)} = 10\log_{10}A_p\;}$$

$$\boxed{\;\text{voltage gain (dB)} = 20\log_{10}A_v\;}\qquad
\boxed{\;\text{current gain (dB)} = 20\log_{10}A_i\;}$$

> [added] **Why 10 for power and 20 for the other two.** Power goes as the square of voltage or
> current, and $\log(x^2) = 2\log x$ — so the factor 10 becomes 20 the moment the quantity being
> compared is an amplitude rather than a power.

---

## 6.9 Common-emitter connection ·J p61–p62

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{CE}$ | collector–emitter voltage (the CE **output** voltage) | V | 3–12 V |
| $\beta$ | CE forward current gain, $=h_{FE}$ | dimensionless | 50–500 |
| $h_{IE}$ | CE input resistance | $\Omega$ (k$\Omega$) | 1–4 k$\Omega$ |
| $h_{OE}$ | CE output admittance | S (µA/V) | 25 µA/V |
| $r_o$ | CE output resistance, $=1/h_{OE}$ | $\Omega$ (k$\Omega$) | 40 k$\Omega$ |

[fig ·J p61] **CE circuit.** The transistor upright with the **emitter at the bottom tied to the
common rail**. On the left, an **input** battery marked **5 V** drives the base. On the right, an
**output** battery marked **12 V** sits between the collector rail and the common rail. The base lead
is marked **B**, the collector **C**, the emitter **E**.

*"In this case the emitter is common to the input and output therefore it is grounded."* ·J p61

[table] **The CE parameter list, exactly as the page sets it out** ·J p61

| | Input side | Output side |
|---|---|---|
| current | $I_B$ | $I_C$ |
| voltage | $V_{BE}$ | $V_{CE}$ |
| resistance | $\dfrac{V_{BE}}{I_B} = h_{IE}$ | $\dfrac{V_{CE}}{I_C}$ |
| power | $I_E V_{BE}$ *(as printed — see JV6.3)* | $I_C V_{CE}$ |

> ⚠ VERIFY **JV6.3** ·J p61 — the CE input power is printed with the wrong current
>
> The page prints: *"Input power $= I_E V_{BE}$."*
>
> **Correct form:**
> $$\boxed{\;\text{CE input power} = I_B V_{BE}\;}$$
>
> **Why.** The page states two lines above that the CE **input current is $I_B$**. Power at a port is
> (port current) × (port voltage), so the input power must pair $V_{BE}$ with $I_B$. The $I_E V_{BE}$
> form is the **common-base** entry from ·J p60, carried over unchanged. With $\beta = 50$ it
> overstates the input power — and so understates the power gain — by a factor of 51.
> See `_verification-log.md`.

[eq: j-beta] **Current gain** ·J p62

$$\boxed{\;\beta = \frac{I_C}{I_B} = h_{FE}\;}\qquad\text{— the forward current gain of the CE configuration}$$

> ⚠ ILLEGIBLE **·J p62** — **needs a screenshot: the first line of the page.** The line renders as
> *"Current gain $= I_B$   ·   ··   – Forward current gain of common emitter configuration"*: the
> numerator of the fraction and the right-hand side have dropped out of the render, leaving the
> denominator $I_B$ and two faint marks. The trailing description names the quantity unambiguously —
> it is the CE forward current gain, i.e. $\beta = h_{FE} = I_C/I_B$ — and ·J p63 prints
> $\beta = I_C/I_B$ in full, so **the boxed equation above is safe**. The screenshot is wanted only to
> confirm which of $\beta$ and $h_{FE}$ the line actually names.

**Output admittance** ·J p62

$$\boxed{\;h_{OE} = \frac{I_C}{V_{CE}} = \frac{1}{r_o}\;}$$

**Reverse voltage gain** ·J p62

$$\text{reverse voltage gain} = \frac{V_{BE}}{V_{CE}}$$

*"This connection is used for impedance matching where the output has a lower impedance. It is mostly
applied where a gain is required."* ·J p62

---

## 6.10 Common-collector connection ·J p62

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $\theta$ (also $\gamma$) | CC forward current gain, $=h_{FC}$ | dimensionless | $1+\beta$, i.e. 51–501 |
| $h_{RC}$ | CC reverse voltage gain | dimensionless | $\cong 1$ |

[fig ·J p62] **CC circuit.** The transistor drawn with the **collector at the bottom tied to the
common rail** (grounded) and the **emitter at the top**. On the left an **input** battery marked
**$V_{CB}$** drives the base; on the right an **output** battery marked **$V_{CC}$** sits between the
emitter rail and the common rail.

[table] **The CC parameter list, exactly as the page sets it out** ·J p62

| | Input side | Output side |
|---|---|---|
| current | $I_B$ ($\cong$ µA) | $I_E$ |
| voltage | $V_{CB}$ ($\cong$ 20 V) | $V_{CE}$ |
| resistance | $\dfrac{V_{CB}}{I_B}$ ($\cong$ k$\Omega$) | $\dfrac{V_{CE}}{I_C}$ *(as printed — see JV6.4)* |
| power | $I_B V_{CB}$ | $I_E V_{CE}$ |

> ⚠ VERIFY **JV6.4** ·J p62 — the CC output resistance is printed with the wrong current
>
> The page prints: *"Output resistance $= \dfrac{V_{CE}}{I_C}$."*
>
> **Correct form:**
> $$\boxed{\;\text{CC output resistance} = \frac{V_{CE}}{I_E}\;}$$
>
> **Why.** The same column of the same table names the **CC output current as $I_E$**, and the output
> power on the line below is written $I_E V_{CE}$. A port's resistance must use that port's own
> current. Since $I_E = I_C/\alpha$, the printed version overstates the output resistance by
> $1/\alpha \approx 1.02$ — small numerically, wrong in principle, and it breaks the pattern that
> the CB and CE tables follow. See `_verification-log.md`.

[derivation] **The CC current gain** ·J p62

$$I_E = I_B + I_C = I_B + \beta I_B = (1+\beta)I_B$$

$$\boxed{\;\text{output current} = (1+\beta)\times\text{input current}\;}$$

[eq: j-theta]

$$\boxed{\;\theta = \frac{I_E}{I_B} = \gamma = h_{FC} = 1+\beta\;}$$

and the page's chain that gets there: ·J p62

$$\theta = \frac{I_E}{I_B} = \frac{I_E}{I_C}\times\frac{I_C}{I_B} = \frac{1}{\alpha}\cdot\beta = \frac{\beta}{\alpha}$$

$$= \frac{\beta}{\beta/(1+\beta)} = 1+\beta$$

> ⚠ VERIFY **JV6.5** ·J p62 — the CC gain chain opens with $I_E/I_C$ where $I_E/I_B$ belongs
>
> The page prints, as one line:
> $$\theta = \frac{I_E}{I_C} = \frac{I_E}{I_C}\times\frac{I_C}{I_B} = \frac{\beta}{\alpha} = \ldots = 1+\beta$$
>
> **Correct form:**
> $$\boxed{\;\theta = \frac{I_E}{I_B} = \frac{I_E}{I_C}\times\frac{I_C}{I_B} = \frac{\beta}{\alpha} = 1+\beta\;}$$
>
> **Why — three checks.** (i) Two lines above, the same page defines the CC current gain as
> $I_E/I_B = \theta$. (ii) The product on the right, $(I_E/I_C)(I_C/I_B)$, cancels to $I_E/I_B$, not
> to $I_E/I_C$. (iii) Numerically $I_E/I_C = 1/\alpha \approx 1.02$, whereas the line's own answer is
> $1+\beta \approx 51$ — a factor of 50 apart. Only the leading symbol is wrong; everything after it
> is right. See `_verification-log.md`.

**Voltage gain** ·J p62

$$\boxed{\;A_v = \frac{V_{CE}}{V_{CB}} \cong 1\;}$$

$$\text{reverse voltage gain} = h_{RC} = \frac{V_{CB}}{V_{CE}}$$

**Applications of the CC connection** ·J p62

1. in a **current-gain or power-gain** circuit;
2. for **impedance matching**, to isolate two circuits.

> [added] **The three configurations in one line each.** CB: current gain just under 1, big voltage
> gain, low input impedance — an impedance *step-up*. CE: current gain $\beta$, voltage gain, the
> workhorse amplifier. CC: voltage gain just under 1, current gain $1+\beta$, high input impedance and
> low output impedance — the buffer.

---

## 6.11 The relations between $\alpha$, $\beta$ and $\theta$ ·J p63

The three gains, side by side with the current law: ·J p63

$$\alpha = \frac{I_C}{I_E} \qquad \beta = \frac{I_C}{I_B} \qquad \theta = \frac{I_E}{I_B}
\qquad\text{with}\qquad I_E = I_C + I_B$$

[derivation] **(i) $\alpha$ in terms of $\beta$** ·J p63

$$\alpha = \frac{I_C}{I_E} = \frac{I_C}{I_C + I_B}$$

Divide top and bottom by $I_B$:

[eq: j-alpha-beta]

$$\boxed{\;\alpha = \frac{\beta}{\beta+1}\;}$$

[derivation] **(ii) $\beta$ in terms of $\alpha$** ·J p63

$$\beta = \frac{I_C}{I_B} = \frac{I_C}{I_E - I_C}$$

Divide top and bottom by $I_E$:

$$\boxed{\;\beta = \frac{\alpha}{1-\alpha}\;}$$

> [added] **Both are worth memorising, and each is the other's inverse.** Check with $\alpha = 0.98$:
> $\beta = 0.98/0.02 = 49$, and back again $\alpha = 49/50 = 0.98$ ✓. And the third gain follows for
> free: $\theta = 1+\beta = 1/(1-\alpha) = 50$.

---

## 6.12 Leakage currents ·J p63–p64

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_{CBO}$ | collector-to-base leakage, **emitter open** | A (µA, nA) | 1–10 µA (Ge), nA (Si) |
| $I_{CEO}$ | collector-to-emitter leakage, **base open** | A (µA) | $(1+\beta)I_{CBO}$ |
| $I_s$ | reverse saturation current of a diode | A | — |

[def] **Leakage current** is caused by the flow of **minority** charge carriers, and it flows in the
**reverse-biased collector–base junction** of the common-base connection. ·J p63

[fig ·J p63] **Two block diagrams.**

1. **$I_{CBO}$ with the emitter open.** The **N | P | N** block labelled **E | B | C** underneath. The
   emitter lead runs left to a **pair of open terminals** (two small circles, not connected). A
   battery in the collector loop drives **$I_{CBO}$**, arrowed **into the collector from the right**
   and **down out of the base** to the common rail, which is grounded.
2. **$I_{CBO}$ with the emitter connected.** The same block, but now a battery in the emitter loop
   too. **$I_E$** is arrowed to the right along the bottom rail, **$I_C$** to the right on the
   collector side, **$I_B$** upward into the base, and **$I_{CBO}$** downward out of the base — the
   two base-node arrows drawn in opposition.

[def] **$I_{CBO}$ is the current which flows from C to B when the emitter is open.** ·J p63

[eq: j-ic-leakage-cb] **Collector current including leakage** ·J p63

$$\boxed{\;I_C = \underbrace{\alpha I_E}_{\text{majority carriers}} + \underbrace{I_{CBO}}_{\text{minority carriers}}\;}$$

[derivation] **Turning it into the CE form** ·J p63

$$I_C = \alpha(I_C + I_B) + I_{CBO}$$

$$I_C - \alpha I_C = \alpha I_B + I_{CBO}$$

$$I_C = \frac{\alpha}{1-\alpha}\,I_B + \frac{1}{1-\alpha}\,I_{CBO}$$

[eq: j-ic-with-leakage]

$$\boxed{\;I_C = \beta I_B + (1+\beta)\,I_{CBO}\;}$$

> ⚠ VERIFY **JV6.6** ·J p63 — the middle step of the derivation loses its $\alpha$
>
> The page prints: *"$I_C - \alpha I_C = I_B + I_{CBO}$."*
>
> **Correct form:**
> $$\boxed{\;I_C - \alpha I_C = \alpha I_B + I_{CBO}\;}$$
>
> **Why.** Expand the line above it: $I_C = \alpha I_C + \alpha I_B + I_{CBO}$, so the $I_B$ term
> carries an $\alpha$. The page's own **next** line restores it —
> $I_C = \dfrac{\alpha}{1-\alpha}I_B + \dfrac{1}{1-\alpha}I_{CBO}$ — so the printed step contradicts
> both its neighbours. A student who reproduces the printed step gets
> $I_C = I_B/(1-\alpha) = (1+\beta)I_B$ instead of $\beta I_B$: with $\beta = 50$ that is a 2 % error
> in $I_C$ and, worse, the wrong formula. See `_verification-log.md`.

*[added] Verified: $\alpha/(1-\alpha) = \beta$ ✓ and $1/(1-\alpha) = 1+\beta$, since
$1-\alpha = 1/(1+\beta)$ ✓.*

[derivation] **Base current including leakage** ·J p64

$$I_C = \alpha I_E + I_{CBO}$$

$$I_E - I_B = \alpha I_E + I_{CBO}$$

$$I_B = \underbrace{I_E - \alpha I_E}_{I_{B(\text{majority})}} - I_{CBO}$$

$$\boxed{\;I_B = (1-\alpha)\,I_E - I_{CBO}\;}$$

**What $I_{CBO}$ is** ·J p64

- $I_{CBO}$ is the **collector-to-base leakage current**.
- It is **exactly like the reverse saturation current $I_s$ of a reverse-biased diode**.
- It is **extremely temperature dependent**: it **doubles for every 10 °C rise for germanium** and
  every **6 °C for silicon**.

### $I_{CEO}$ — leakage with the base open ·J p64

[fig ·J p64] **Two block diagrams, headed "Collector Emitter Open".**

1. **Base open.** A **vertical** N | P | N stack. The **base lead runs left to a pair of open
   terminals**. A battery on the right drives **$I_{CEO}$**, arrowed **into the top (collector) along
   the upper rail** and **down out of the bottom (emitter)** to the grounded rail.
2. **With the base driven.** The same vertical stack, now with a battery in the base loop.
   **$I_B$** is arrowed into the base from the left, **$I_C$** downward into the collector,
   **$I_{CEO}$** and **$I_E$** downward out of the emitter.

[derivation] Setting $I_B = 0$ in the CE collector-current equation: ·J p64

$$I_C = \frac{\alpha}{1-\alpha}\,I_B + \frac{1}{1-\alpha}\,I_{CBO}
\qquad\xrightarrow{\;I_B\,=\,0\;}\qquad
I_C = \frac{1}{1-\alpha}\,I_{CBO}$$

[eq: j-iceo]

$$\boxed{\;I_{CEO} = \frac{I_{CBO}}{1-\alpha} = (1+\beta)\,I_{CBO}\;}$$

**"$I_C$ is magnified by a factor of $1+\beta$."** ·J p64

$$\boxed{\;I_C = \beta I_B + I_{CEO}\;}$$

$$I_E = I_C + I_B = \beta I_B + I_{CEO} + I_B$$

$$\boxed{\;I_E = (1+\beta)\,I_B + I_{CEO}\;}$$

> ⚠ VERIFY **JV6.7** ·J p64 — the last line double-counts the $(1+\beta)$
>
> The page prints: *"$I_E = (1+\beta)I_B + I_{CEO} = (1+\beta)I_B + \dfrac{1}{1-\alpha}I_{CEO}$."*
>
> **Correct form:**
> $$\boxed{\;I_E = (1+\beta)I_B + I_{CEO},\qquad\text{with}\qquad I_{CEO} = \frac{1}{1-\alpha}\,I_{CBO}\;}$$
>
> **Why.** The factor $1/(1-\alpha) = 1+\beta$ is what converts $I_{CBO}$ **into** $I_{CEO}$; applying
> it a second time to $I_{CEO}$ multiplies the leakage term by $(1+\beta)$ twice over. The two halves
> of the printed equality differ by a factor of 51 for $\beta = 50$. The first half is correct.
> See `_verification-log.md`.

> [added] **Why this pair matters more than it looks.** $I_{CEO}$ is $(1+\beta)$ times $I_{CBO}$: the
> configuration that gives useful gain is the one that **amplifies its own leakage a hundredfold**.
> That single fact is the reason the whole biasing half of this file exists.

---

## 6.13 Thermal runaway ·J p64

[def] **Thermal runaway** is the situation where an increase of current raises the temperature of the
semiconductor, the higher temperature raises the current further, and the process **continues
cumulatively** — destroying the transistor if it is not controlled. ·J p64

The page's temperature figures, printed under this heading: ·J p64

- **Si**: a **10 °C** rise doubles the current
- **Ge**: a **6 °C** rise doubles the current

> ⚠ VERIFY **JV6.8** ·J p64 — the Si and Ge doubling temperatures are printed **both ways round on
> the same page**
>
> Half a page above, the notes state: *"$I_{CBO}$ ... doubles for every **10 °C** rise for
> **germanium** and **6 °C** for **silicon**."* Under **Thermal Runaway** they state the opposite:
> *"Si $=$ **10 °C** ... Ge $=$ **6 °C**."*
>
> **Correct form:**
> $$\boxed{\;\text{Ge: } I_{CBO}\text{ doubles per }10\ ^\circ\mathrm{C};\qquad \text{Si: } I_{CBO}\text{ doubles per }6\ ^\circ\mathrm{C}\;}$$
>
> **Why.** The first of the two statements is the standard one and the one used elsewhere in this
> knowledge base — `11-diodes.md` works an exam problem on the explicit assumption that a germanium
> diode's reverse saturation current doubles every 10 °C. Silicon's larger band gap makes its
> saturation current a **steeper** function of temperature in relative terms, so silicon doubles in
> **fewer** degrees, not more. See `_verification-log.md`.

> [added] **How to use whichever figure you are given.** A rise of $\Delta T$ multiplies the leakage
> by $2^{\Delta T/T_{2}}$, where $T_2$ is the doubling interval. A 30 °C rise multiplies a germanium
> transistor's $I_{CBO}$ by $2^{3} = 8$; the same rise multiplies a silicon transistor's by
> $2^{5} = 32$ — but from a starting value three orders of magnitude smaller, which is why silicon
> wins in practice.

---

## 6.14 The three families of static characteristics ·J p65

> **Note on the heading.** ·J p65 opens this material at the top of the page with **no heading**; the
> first line is *"There are VI characteristics of transistors connected in different configurations.
> They help in determining the optimal operation of a transistor."* The section title used here is
> ours.

[table] **What each family plots** ·J p65

| Family | Plot |
|---|---|
| **input characteristics** | input current against input voltage |
| **output characteristics** | output current against output voltage |
| **transfer characteristics** | output current against input current |

In every case the **third variable is held constant** and named on the graph.

---

## 6.15 Common-base characteristics ·J p65–p66

### (i) CB input characteristics ·J p65

[fig ·J p65] **Test circuit.** Left loop: **$V_{EE}$** across a **potentiometer $R_1$** whose wiper
feeds the emitter through an **ammeter (A)** reading $I_E$; a **voltmeter (V) marked $V_{EB}$** sits
across the base–emitter terminals. The transistor is drawn on its side with the **base to the common
rail**. Right loop: a **voltmeter (V) marked $V_{CB}$** across the collector–base terminals, an
**ammeter (A)** in the collector lead, a **potentiometer $R_2$**, and **$V_{CC}$**. The common rail is
grounded.

**Method.** $V_{CB}$ is held at a constant value; $V_{BE}$ is varied with $R_1$; the corresponding
$I_E$ is noted and the curve drawn. ·J p65

[fig ·J p65] **The curves.** Vertical axis **$I_E$ (mA)**, ticks at **2, 4, 6**. Horizontal axis
**$V_{BE}$ (V)**, ticks at **0.5** and **1**. The legend **"$V_{CB} =$ constant"** sits above.
**Two** curves are drawn, each flat then turning sharply upward: the left one labelled
**Germanium** (knee left of the 0.5 V tick), the right one labelled **Silicon** (knee near 0.7 V). A
small **slope triangle** is drawn against the silicon curve at about $I_E = 2$ mA.

**Reading it** ·J p65

- The curve behaves **exactly like a forward-biased diode**, because the input B–E junction *is* a
  forward-biased diode.
- Raising $V_{BE}$, the transistor **starts conducting at 0.7 V (Si)**.
- Further increase in $V_{BE}$ gives a corresponding increase in $I_E$.

$$\text{admittance} = \frac{I_E}{V_{BE}}$$

> ⚠ VERIFY **JC6.5** ·J p65 — the input admittance is written as a ratio, not a slope
>
> The page prints *"Admittance $= I_E/V_{BE}$"*, but the figure beside it draws a **slope triangle**
> on the curve.
>
> **Correct form:**
> $$\boxed{\;\text{input admittance} = \frac{\Delta I_E}{\Delta V_{BE}}\bigg|_{V_{CB}\text{ const}} = \frac{1}{h_{ib}}\;}$$
>
> **Why.** The characteristic is strongly non-linear, so the ratio $I_E/V_{BE}$ at a point and the
> slope at that point are different numbers. The document uses the $\Delta$ form correctly two pages
> later (·J p67 labels $\Delta I_B$ and $\Delta V_{BE}$ on the CE input curve). Units are unaffected.
> See `_verification-log.md`.

### (ii) CB output characteristics ·J p66

**Method.** $I_E$ is held constant while $V_{CB}$ is varied in discrete steps and $I_C$ measured. ·J p66

[fig ·J p66] **The curves.** Vertical axis **$I_C$ (mA)**, ticks at **2, 4, 6, 8**. Horizontal axis
**$V_{CB}$ (V)**, ticks at **5, 10, 15, 20**. A family of nearly horizontal curves, each labelled by
its emitter current — **$I_E = 2$ mA** for an upper curve and **$I_E = 0$ mA** for the lowest. Four
regions are marked:

- **Saturation region** — a brace at the far **left**, where the curves rise steeply out of the
  origin (i.e. where $V_{CB}$ is small or negative);
- **Active** — the broad flat middle, labelled inside the family;
- **Cutoff** — an arrow pointing at the region **below** the $I_E = 0$ curve;
- **Avalanche breakdown** — a brace at the far **right**, where the curves sweep sharply upward.

A short **double-headed arrow labelled $I_{CBO}$** marks the small residual height of the $I_E = 0$
curve above the axis.

> ⚠ VERIFY **JC6.6** ·J p66 — the breakdown region is labelled **"Avalacnhe Breakdown"** (letters
> transposed). Cosmetic only. See `_verification-log.md`.

**Reading it.** *"The graph can be used to get $\alpha$. $I_C$ is practically independent of $V_{CB}$
over the working range."* ·J p66

> [added] **Two things this graph tells you at a glance.** (i) The curves are flat, so the CB output
> looks like a **current source** — very high output resistance. (ii) They are almost equally spaced
> for equal steps of $I_E$, and the spacing is *slightly less* than the step: that shortfall is
> $1-\alpha$.

### (iii) CB transfer characteristic ·J p66

[fig ·J p66] Vertical axis **$I_C$**, horizontal axis **$I_E$**, legend **"$V_{CB} =$ constant"**. A
**straight line** rising from a small **non-zero intercept on the $I_C$ axis marked $I_{CBO}$**.

**Gain can be calculated from the curve** — the slope is $\alpha$. ·J p66

---

## 6.16 Common-emitter characteristics ·J p66–p68

[fig ·J p66] **Test circuit.** Left loop: **$V_{BB}$** across a **potentiometer $R_1$**, its wiper
feeding the base through an **ammeter (A)** reading $I_B$, with a **voltmeter (V)** across the
base–emitter terminals. The transistor is upright with its **emitter on the grounded common rail**.
Right loop: an **ammeter (A)** in the collector lead, a **voltmeter (V)** across the output
terminals, a **potentiometer $R_2$**, and the collector supply.

> ⚠ VERIFY **JC6.7** ·J p66 — the CE test circuit carries two wrong labels
>
> The page labels the node above the collector-side ammeter **$V_{EE}$** and the output voltmeter
> **$V_{CB}$**.
>
> **Correct form:** in a common-emitter test circuit the collector supply is **$V_{CC}$** and the
> voltmeter across the output port reads **$V_{CE}$**. (The circuit also shows $V_{CC}$ correctly at
> the far right, so $V_{EE}$ appears twice-over redundant.) The measurement procedure described in the
> text is right; only the two labels are wrong. See `_verification-log.md`.

### (i) CE input characteristics ·J p66–p67

**What it is:** a plot of **$I_B$ against $V_{BE}$ for constant $V_{CE}$**. $V_{CC}$ is held constant
while $V_{BE}$ is varied in steps and $I_B$ read off. ·J p66

[fig ·J p67] Vertical axis **$I_B$ (µA)**, ticks at **10, 20, 30, 40**. Horizontal axis **$V_{BE}$
(V)**, ticks at **0.5** and **1**. Legend **"$V_{CE}$ is constant"**. One diode-shaped curve, with a
**slope triangle** drawn on its rising part, its legs labelled **$\Delta I_B$** (vertical) and
**$\Delta V_{BE}$** (horizontal).

**Reading it** ·J p67

- With $V_{CE} = 0$ the base–emitter junction is forward biased and behaves as a **forward-biased
  diode**.
- At constant $V_{BE}$, **raising $V_{CE}$ widens the collector–base depletion region**, so the
  **effective base width shrinks**, so **$I_B$ falls** — the curve **shifts to the right** as $V_{CE}$
  increases.
- Conduction starts at **0.7 V (silicon)** or **0.2 V (Ge)**.
- The curve gives the **input admittance or impedance**: the resistance is **high (4 k$\Omega$)** in
  the early part of the curve and **falls as $V_{BE}$ increases**.

> [added] **The name for that shift.** Narrowing of the effective base as $V_{CE}$ grows is the
> **Early effect** (base-width modulation). The notes describe the mechanism correctly without naming
> it.

### (ii) CE output characteristics ·J p67

[fig ·J p67] Vertical axis **$I_C$ (mA)**, ticks at **2, 4, 6, 8**. Horizontal axis **$V_{CE}$ (V)**,
ticks at **5, 10, 15, 20**. Five curves rise steeply from the origin, knee, then run nearly flat,
each terminated on the right by an arrow and a label. Marked on the plot:

- **Saturation Region** — a label with an arrow to the steep left-hand rise, plus a **Saturation
  Line** drawn through the knees of the family;
- **Active Region** — a circle drawn around the flat middle of the family;
- **Cutoff Region** — an arrow pointing at the area **below the lowest curve**;
- **Breakdown Region** — a brace over the right-hand end where the curves sweep upward;
- a **double-headed arrow labelled $I_{CEO}$** measuring the height of the lowest curve above the
  axis.

> ⚠ VERIFY **JC6.8** ·J p67 — all five output curves are labelled **$I_B = 40$ µA**
>
> Every one of the five characteristics in the CE output family carries the identical annotation
> $I_B = 40\ \mathrm{\mu A}$.
>
> **Correct form:** the family must be a **ladder of different base currents** — conventionally
> $I_B = 10,\ 20,\ 30,\ 40,\ 50\ \mathrm{\mu A}$ from the bottom curve upward.
>
> **Why.** Curves of equal $I_B$ would coincide; and the same document draws the family correctly on
> ·J p77, where the load-line figure labels its curves 0, 10, 20, 30, 40, 50 µA. As printed the figure
> cannot be used to read $\beta = \Delta I_C/\Delta I_B$ off the page, which is its main purpose.
> See `_verification-log.md`.

**Reading it** ·J p67

- For **$I_B = 0$ and $V_{CE} \cong 0$**, the only current through the transistor is the leakage
  current $I_{CEO}$.
- As $V_{CE}$ is increased far enough, $I_C$ increases further, the transistor **cannot hold any
  more, and it breaks down**.
- Raising $I_B$ from zero at a few volts of $V_{CE}$ puts the transistor in **saturation**; those
  curves are similar in shape to the $I_B = 0$ one.

[table] **The four regions, as ·J p68 defines them**

| Region | $V_{CE}$ | Junction states | Behaviour |
|---|---|---|---|
| **Saturation** | $0$ up to a few volts ($\cong 0.5$ V) | **both** junctions forward biased | the collector collects **all** the electrons the emitter emits; the transistor is a **switch that is ON** |
| **Cut-off** | — ($I_B = 0$) | **both** junctions reverse biased | only the small leakage $I_{CEO}$ flows; the transistor is a **switch that is OFF** |
| **Active** | a few volts up to about **30 V**, $I_B$ slightly above 0 | C–B **reverse**, B–E **forward** | the normal bias; **most applications, e.g. amplification, use this region** |
| **Breakdown** | **beyond 30 V** | C–B reverse, B–E forward | the transistor breaks down and current flows uncontrollably — **avalanche breakdown** |

*(the ceiling of the active region and the floor of the breakdown region both "depend on the type of
transistor" ·J p68.)*

### (iii) CE transfer characteristic ·J p68

[fig ·J p68] Vertical axis **$I_C$ (mA)**, horizontal axis **$I_B$ (µA)**, legend **"$V_{CE}$ –
constant"**. A straight line rising from a small **intercept on the $I_C$ axis marked $I_{CEO}$**,
with a **slope triangle** whose legs are labelled **$\Delta I_C$** and **$\Delta I_B$**.

**Reading it.** It is a plot of $I_C$ against $I_B$. **When $I_B = 0$, $I_C$ still has a value** —
that is the leakage current $I_{CEO}$. The graph gives the **forward current gain of the
collector–emitter connection**, i.e. $\beta$ from the slope. ·J p68

---

## 6.17 Common-collector characteristics ·J p68–p70

[fig ·J p68] **Test circuit.** Left loop: **$V_{BB}$**, **potentiometer $R_1$**, an **ammeter (A)** in
the base lead and a **voltmeter (V)** at the input. The transistor is drawn with the **collector on
the grounded common rail**. Right: an **ammeter (A)** in the **emitter** lead at the top, a
**voltmeter (V) marked $V_{CB}$**, a **potentiometer $R_2$**, and **$V_{EE}$**.

> ⚠ VERIFY **JC6.9** ·J p68 — the CC test circuit's output labels belong to another configuration
>
> The output voltmeter is labelled **$V_{CB}$** and the output supply **$V_{EE}$**.
>
> **Correct form:** in a common-collector stage the **output port is collector-to-emitter**, so the
> voltmeter reads **$V_{CE}$** and the supply is **$V_{CC}$**. ($V_{CB}$ is the CC *input* voltage —
> the page's own parameter table on ·J p62 says so.) See `_verification-log.md`.

### (i) CC input characteristics ·J p69

[fig ·J p69] Vertical axis **$I_B$**, horizontal axis **$V_{CB}$ (V)**, ticks at **0, 2, 4**. **Two
straight lines sloping down to the right**, the left one labelled **$V_{CE} = 2$ V** and meeting the
axis at $V_{CB} = 2$, the right one labelled **$V_{CE} = 4$ V** and meeting the axis at $V_{CB} = 4$.

[eq: j-cc-vce] The relation that governs the whole plot: ·J p69

$$\boxed{\;V_{CE} = V_{CB} + V_{BE}\;}$$

**Reading it** ·J p69

- The plot is **$I_B$ against $V_{CB}$ with $V_{CE}$ held constant**.
- $V_{CE}$ depends on **both** $V_{CB}$ and $V_{BE}$ through the relation above.
- So with $V_{CE}$ fixed, **increasing $V_{CB}$ forces $V_{BE}$ down**, until $V_{CB} = V_{CE}$ — at
  which point $V_{BE} = 0$ and **$I_B$ is zero**. That is where each line meets the axis.
- The graph gives the **input impedance** and the **reverse voltage gain**.

> [added] **This is why the two lines cut the axis at 2 V and 4 V.** The intercept of each line is its
> own $V_{CE}$ — a direct visual reading of $V_{CE} = V_{CB} + V_{BE}$ at $V_{BE} = 0$.

### (ii) CC output characteristics ·J p69

[fig ·J p69] Vertical axis labelled **$I_C$ (mA)**, ticks at **2, 4, 6, 8**; horizontal axis
**$V_{CE}$ (V)**, ticks at **5, 10, 15, 20**. Four curves of the usual output shape, the **top one
labelled $I_B = 30$ µA** and the **lowest labelled $I_B = 0$ µA**. Marked: **Saturation Region**
(arrow to the steep left rise), **Active Region** (circled in the middle), **Cutoff Region** (arrow
below the lowest curve), **Breakdown Region** (brace at the right).

**Reading it.** It is a plot of **$I_E$ against $V_{CE}$ with $I_B$ constant**. It is *"exactly the
same as the output characteristics for the collector-emitter connection because $I_E$ is almost equal
to $I_C$."* It gives the **impedance or admittance** and the **forward current gain** of the CC
connection. ·J p69

> ⚠ VERIFY **JC6.10** ·J p69 — the CC output figure's vertical axis is labelled $I_C$, not $I_E$
>
> The text under the figure says the plot is **$I_E$ against $V_{CE}$**; the figure's vertical axis
> reads **$I_C$ (mA)**.
>
> **Correct form:** the axis should read **$I_E$ (mA)** — the CC output current. The page itself
> explains why the two look identical ($I_E \cong I_C$), so nothing quantitative changes, but the
> labelled axis contradicts the caption. See `_verification-log.md`.

### (iii) CC transfer characteristic ·J p70

[fig ·J p70] Vertical axis **$I_E$ (mA)**, horizontal axis **$I_B$ (µA)**, legend **"$V_{CE}$ –
constant"**. A straight line rising from a small **intercept on the $I_E$ axis marked $I_{CEO}$**,
with a **slope triangle** labelled **$\Delta I_E$** (vertical) and **$\Delta I_B$** (horizontal).

> [added] **The slope here is $\theta = 1+\beta$**, not $\beta$ — the only difference between this
> plot and the CE transfer characteristic of §6.16(iii) is which current is on the vertical axis.

---

## 6.18 Methods of transistor biasing ·J p70

[table] **Symbols for the whole biasing block**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{CC}$ | collector supply | V | 9–20 V |
| $V_{EE}$ | second (negative) supply, two-supply bias only | V | 5–20 V |
| $R_B$ | resistance in the base circuit | $\Omega$ (k$\Omega$) | 47–470 k$\Omega$ |
| $R_{B1}$, $R_{B2}$ | upper and lower divider resistors | $\Omega$ (k$\Omega$) | 10–56 k$\Omega$ |
| $R_C$ | collector resistor | $\Omega$ (k$\Omega$) | 2–3.3 k$\Omega$ |
| $R_E$ | emitter resistor | $\Omega$ (k$\Omega$) | 0.8–2 k$\Omega$ |
| $R_L$ | external load | $\Omega$ (k$\Omega$) | 10 k$\Omega$ |
| $V_B$, $V_C$, $V_E$ | base, collector and emitter voltages **to ground** | V | — |
| $V_{BE}$ | base–emitter drop | V | 0.7 (Si), 0.3 (Ge) |
| $I_{C(sat)}$ | collector current at saturation | A (mA) | 2–10 mA |
| $S$ | stability factor | dimensionless | 1 to $1+\beta$ |

[def] **Biasing** is connecting a transistor to voltage supplies together with resistors so that it
can **operate normally** — that is, with the **collector–base junction reverse biased and the
base–emitter junction forward biased**. ·J p70

[table] **The six methods the notes list** ·J p70

| # | Method | Section |
|---|---|---|
| (i) | base bias | §6.19 |
| (ii) | base bias with **emitter** feedback | §6.20 |
| (iii) | base bias with **collector** feedback | §6.21 |
| (iv) | base bias with **collector and emitter** feedback | §6.22 |
| (v) | emitter bias with **two supplies** | §6.23 |
| (vi) | **voltage-divider** bias | §6.24 |

---

## 6.19 Base bias ·J p70

[fig ·J p70] **Circuit.** The **$V_{CC}$ rail** across the top. **$R_B$** from the rail down to the
**base** (current **$I_B$** arrowed down through it); **$R_C$** from the rail down to the
**collector** (current **$I_C$** arrowed down). The NPN sits with its **emitter grounded**. Marked
with vertical arrows down the page: **$V_{BE}$** at the base terminal, **$V_B$** from base to ground,
**$V_C$** from collector to ground, **$V_{CE}$** from collector to emitter, and **$V_E$** from emitter
to ground (zero here, and the figure shows the emitter node crossed to ground).

Because the emitter is grounded, ·J p70

$$V_C = V_{CE}$$

[eq: j-base-bias] **The equations** ·J p70

$$I_C + I_B = I_E$$

$$\boxed{\;V_{CC} = I_C R_C + V_{CE}\;}\qquad\text{(collector loop)}$$

$$\boxed{\;V_{CC} = I_B R_B + V_{BE}\;}\qquad\text{(base loop)}$$

$$\boxed{\;I_C = \frac{V_{CC} - V_{CE}}{R_C}\;}\qquad\qquad
\boxed{\;I_B = \frac{V_{CC} - V_{BE}}{R_B}\;}$$

**At saturation**, where $V_{CE} \cong 0$ V: ·J p70

$$\boxed{\;I_{C(sat)} = \frac{V_{CC}}{R_C}\;}$$

**At cut-off**, where $I_C \cong 0$ A: ·J p70

$$\boxed{\;V_{CE(\max)} = V_{CC}\;}$$

**Stability factor** ·J p70

$$\boxed{\;S = 1+\beta\;}$$

> [added] **Why base bias is the worst of the six.** $I_B$ is fixed by $V_{CC}$ and $R_B$ alone, so
> $I_C = \beta I_B$ tracks $\beta$ **exactly**: replace the transistor with one of twice the gain and
> the Q point doubles. And $S = 1+\beta$ is the largest stability factor any of these circuits can
> have — with $\beta = 100$, $I_C$ moves 101 times as far as the leakage does. Every circuit that
> follows is an attempt to pull $S$ back toward 1.

---

## 6.20 Base bias with emitter feedback ·J p70–p71

[fig ·J p71] **Circuit.** As base bias, but with **$R_E$ inserted between the emitter and ground**.
**$R_B$** from the $V_{CC}$ rail to the base ($I_B$ down); **$R_C$** from the rail to the collector
($I_C$ down); the emitter goes through **$R_E$** to ground. **$V_{BE}$**, **$V_B$**, **$V_C$**,
**$V_{CE}$** and **$V_E$** are all marked with vertical arrows, $V_E$ now non-zero.

[eq: j-emitter-feedback] **The loop equations** ·J p71

$$\boxed{\;V_{CC} = I_C R_C + V_{CE} + I_E R_E\;}\qquad\text{(collector loop)}$$

$$\boxed{\;V_{CC} = I_B R_B + V_{BE} + I_E R_E\;}\qquad\text{(base loop)}$$

[derivation] **Solving the collector loop for $I_C$**, using $I_E = I_C/\alpha$: ·J p71

$$V_{CC} - V_{CE} = I_C R_C + \frac{I_C}{\alpha}R_E = I_C\left(R_C + \frac{R_E}{\alpha}\right)$$

$$\boxed{\;I_C = \frac{V_{CC} - V_{CE}}{R_C + R_E/\alpha}\;}
\qquad\text{and since }\frac{1}{\alpha} = \frac{1+\beta}{\beta}:\qquad
\boxed{\;I_C = \frac{V_{CC} - V_{CE}}{R_C + \dfrac{1+\beta}{\beta}R_E}\;}$$

[derivation] **Solving the base loop for $I_B$**, using $I_E = \theta I_B = (1+\beta)I_B$: ·J p71

$$\boxed{\;I_B = \frac{V_{CC} - V_{BE}}{R_B + (1+\beta)R_E}\;}$$

**The node voltages** ·J p71

$$\boxed{\;V_C = V_{CE} + V_E\;}\qquad
\boxed{\;V_B = V_{BE} + V_E\;}\qquad
\boxed{\;V_E = I_E R_E\;}$$

**"Negative feedback — output is fed back to input."** ·J p71

> [added] **How the feedback actually works, in four steps.** $I_C$ rises (heat, or a higher-$\beta$
> transistor) → $I_E R_E$ rises, so $V_E$ rises → with $V_B$ pinned by $R_B$, $V_{BE} = V_B - V_E$
> **falls** → $I_B$ falls, and with it $I_C$. The rise is opposed. That is the whole idea of
> degenerative emitter feedback, and it costs nothing but the resistor.

---

## 6.21 Base bias with collector feedback ·J p71–p72

[fig ·J p71] **Circuit.** **$V_{CC}$** at the top feeding **$R_C$**, whose current is labelled
**$I_C + I_B$**. At the bottom of $R_C$ is the **collector node**; from that node **$R_B$ runs
leftward and back into the base**, carrying **$I_B$** (arrowed toward the base). $I_C$ continues down
into the collector. The **emitter is grounded**. **$V_{BE}$**, **$V_B$**, **$V_{CE}$**, **$V_C$** and
**$V_E$** are marked.

[eq: j-collector-feedback] **The equations** ·J p72

$$\boxed{\;V_{CC} = (I_C + I_B)R_C + I_B R_B + V_{BE}\;}$$

$$V_C = V_{CE}$$

$$\boxed{\;V_C = V_{CC} - (I_C + I_B)R_C\;}\qquad\qquad \boxed{\;V_C = I_B R_B + V_{BE}\;}$$

> [added] **The collector current the notes stop short of writing.** Put $I_B = I_C/\beta$ into the
> first equation and solve:
> $$V_{CC} = \left(I_C + \frac{I_C}{\beta}\right)R_C + \frac{I_C}{\beta}R_B + V_{BE}$$
> $$\boxed{\;I_C = \frac{V_{CC} - V_{BE}}{R_C\left(1 + \dfrac{1}{\beta}\right) + \dfrac{R_B}{\beta}}
> \;\cong\; \frac{V_{CC} - V_{BE}}{R_C + R_B/\beta}\;}$$
> The right-hand form (dropping $R_C/\beta$ against $R_C$) is the one the tier-2 chapter prints; see
> §6.35. **Not in the source** — supplied because every numerical question on this circuit needs it.

> [added] **Why collector feedback stabilises.** $I_C$ rises → the drop across $R_C$ rises → the
> collector voltage $V_C$ **falls** → but $V_C$ is what feeds the base through $R_B$, so $I_B$ falls,
> and $I_C$ with it. Same negative-feedback logic as §6.20, taken from the other end of the transistor.

---

## 6.22 Base bias with collector and emitter feedbacks ·J p72

[fig ·J p72] **Circuit.** The collector-feedback circuit of §6.21 **plus $R_E$** between emitter and
ground. **$V_{CC}$** → **$R_C$** (current $I_C + I_B$) → collector node; **$R_B$** from the collector
node back to the base ($I_B$); **$R_E$** from the emitter to ground ($I_E$ down). **$V_{BE}$**,
**$V_B$**, **$V_{CE}$**, **$V_C$**, **$V_E$** all marked.

[eq: j-both-feedbacks] **The equations** ·J p72

$$I_E = I_C + I_B$$

$$\boxed{\;V_{CC} = (I_C + I_B)R_C + V_{CE} + I_E R_E\;}$$

$$\boxed{\;V_{CC} = (I_C + I_B)R_C + I_B R_B + V_{BE} + I_E R_E\;}$$

**The node voltages** ·J p72

$$V_E = I_E R_E \qquad V_C = V_{CE} + V_E \qquad V_C = V_{CC} - (I_C + I_B)R_C
\qquad V_C = I_B R_B + V_{BE} + I_E R_E$$

[derivation] **Saturation**, i.e. $V_{CE} = 0$: ·J p72

$$V_{CC} = (I_C + I_B)R_C + I_E R_E = I_E R_C + I_E R_E$$

$$V_{CC} = \frac{I_C}{\alpha}\left(R_C + R_E\right)$$

$$\frac{I_C}{\alpha} = \frac{V_{CC}}{R_C + R_E} \qquad\Longrightarrow\qquad I_C = \frac{V_{CC}}{R_C+R_E}\,\alpha$$

[eq: j-ic-sat]

$$\boxed{\;I_{C(sat)} = \frac{V_{CC}}{R_C+R_E}\cdot\frac{\beta}{1+\beta} \;\cong\; \frac{V_{CC}}{R_C+R_E}\;}$$

[derivation] **Cut-off**, i.e. $I_C = 0$: ·J p72

$$V_{CC} = (I_C + I_B)R_C + I_E R_E + V_{CE} \qquad\Longrightarrow\qquad
\boxed{\;V_{CE(cut\text{-}off)} = V_{CC}\;}$$

> ⚠ VERIFY **JC6.11** ·J p72 — an approximation is printed as an exact equality
>
> The page prints:
> $$I_{sat} = \frac{V_{CC}}{R_C+R_E}\left(\frac{\beta}{1+\beta}\right) = \frac{V_{CC}}{R_C+R_E}$$
>
> **Correct form:** the second equals sign must be **$\cong$**, because $\beta/(1+\beta) = \alpha$,
> which is 0.98, not 1.
>
> **Why it is harmless in practice:** the error is $(1-\alpha)$, i.e. 1–5 %, and every later use of
> $I_{C(sat)}$ in this document (·J p76, ·J p79) takes the approximate form deliberately. Flagged so
> the reader knows which of the two is exact. See `_verification-log.md`.

---

## 6.23 Emitter bias with two supplies ·J p73

> **Note on the heading.** ·J p73 opens with the circuit and no heading. The identification is not in
> doubt: the circuit has two supplies and the notes' own list on ·J p70 names method (v) *"Emitter
> Bias with two supplies"*.

[fig ·J p73] **Circuit.** **$+V_{CC}$** at the top over **$R_C$**, with **$I_C$** arrowed down into
the collector. The NPN's **base goes left to $R_B$, which runs down to ground**. The **emitter goes
down through $R_E$** (current **$I_E$** arrowed down) to a **second supply terminal marked $-V_{EE}$**
at the bottom.

[eq: j-two-supply] **The equations, corrected** ·J p73

$$\boxed{\;V_{EE} = I_E R_E + I_B R_B + V_{BE}\;}\qquad\text{(base loop — as printed, and correct)}$$

$$\boxed{\;V_{CC} + V_{EE} = I_C R_C + V_{CE} + I_E R_E\;}\qquad\text{(collector loop — see JV6.9)}$$

$$\boxed{\;V_{CC} = I_C R_C + V_{CB} - I_B R_B\;}\qquad\text{(collector-to-base — see JV6.10)}$$

> ⚠ VERIFY **JV6.9** ·J p73 — the collector loop puts $V_{EE}$ on the wrong side
>
> The page prints: *"$V_{CC} = I_C R_C + V_{CE} + I_E R_E + V_{EE}$."*
>
> **Correct form:**
> $$\boxed{\;V_{CC} + V_{EE} = I_C R_C + V_{CE} + I_E R_E\;}$$
>
> **Why.** Walk the collector loop from $+V_{CC}$ down to $-V_{EE}$. The total voltage traversed is
> $V_{CC} - (-V_{EE}) = V_{CC} + V_{EE}$, and it is dropped across $R_C$, the transistor and $R_E$.
> The page's own **base-loop** equation on the same line above uses $V_{EE}$ as a **positive
> magnitude** ($V_{EE} = I_E R_E + I_B R_B + V_{BE}$, which is correct), so the two equations as
> printed cannot both hold. With $V_{CC} = V_{EE} = 10$ V, $R_C = R_E = 2$ k$\Omega$ and
> $I_C \cong I_E = 4$ mA, the printed form gives $V_{CE} = -6$ V and the correct form $V_{CE} = +4$ V.
> See `_verification-log.md`.

> ⚠ VERIFY **JV6.10** ·J p73 — the collector-to-base equation has the wrong sign on $I_B R_B$
>
> The page prints: *"$V_{CC} = I_C R_C + I_B R_B + V_{CB}$."*
>
> **Correct form:**
> $$\boxed{\;V_{CC} = I_C R_C + V_{CB} - I_B R_B\;}$$
>
> **Why.** In this circuit the base current flows **from ground through $R_B$ into the base**, so the
> base sits **below** ground: $V_B = -I_B R_B$. Then
> $V_{CB} = V_C - V_B = (V_{CC} - I_C R_C) + I_B R_B$, which rearranges to the boxed form. The check
> that settles it: the corrected pair must satisfy $V_{CB} = V_{CE} - V_{BE}$, and they do —
> subtract the base loop from the corrected collector loop and $V_{CC} = I_C R_C + V_{CB} - I_B R_B$
> falls out exactly. The printed version does not. See `_verification-log.md`.

> [added] **The result this circuit is famous for, which the notes do not state.** Because the base
> sits within $I_B R_B$ of ground — usually a few tens of millivolts — $V_B \cong 0$, and the base
> loop collapses to
> $$\boxed{\;I_E = \frac{V_{EE} - V_{BE}}{R_E + R_B/\beta} \;\cong\; \frac{V_{EE}}{R_E}\;}$$
> when $V_{EE} \gg V_{BE}$ and $R_E \gg R_B/\beta$. The emitter current is then set by **two
> components and no transistor parameter at all**, which is the point of paying for the second supply.
> **Not in the source**; it is in the tier-2 chapter (§6.35).

---

## 6.24 Voltage-divider bias ·J p73–p74

[fig ·J p73] **Circuit.** **$+V_{CC}$** at the top. **$R_{B1}$** from the rail down to the **base
node**; **$R_{B2}$** from the base node down to the bottom rail. **$R_C$** from the rail to the
collector (**$I_C$** down); **$R_E$** from the emitter down to the bottom rail (**$I_E$** down). The
bottom rail carries a **ground symbol** and, beside it, the label **$-V_{EE}$**.

> ⚠ VERIFY **JC6.12** ·J p73 — the voltage-divider circuit is labelled with a second supply
>
> The bottom rail of the divider-bias figure carries **both a ground symbol and the label
> $-V_{EE}$**, carried over from the two-supply figure directly above it on the same page.
>
> **Correct form:** a voltage-divider-biased stage runs from **one supply**; $R_{B2}$ and $R_E$ return
> to **ground**. That is the whole selling point of the circuit and is how every subsequent figure in
> this range draws it (·J p74, ·J p75, ·J p76, ·J p80, ·J p82). See `_verification-log.md`.

[fig ·J p73] **The divider alone, "Look into the base".** $V_{CC}$ at the top over **$R_{B1}$**; the
junction of $R_{B1}$ and **$R_{B2}$** brought out to a terminal; the bottom of $R_{B2}$ brought out to
a second terminal and to ground. This is the two-terminal network to be Thevenised.

[eq: j-divider-thevenin] **Step 1 — the Thevenin source** ·J p73

$$\boxed{\;V_{Th} = \frac{V_{CC}\,R_{B2}}{R_{B1}+R_{B2}}\;}$$

**Step 2 — the Thevenin resistance** (·J p74; the divider is seen with $V_{CC}$ shorted, so
$R_{B1}\parallel R_{B2}$)

$$\boxed{\;R_{Th} = \frac{R_{B1}R_{B2}}{R_{B1}+R_{B2}}\;}$$

[fig ·J p74] **The equivalent source** — a battery **$V_{th}$** in series with a resistor
**$R_{th}$**, one end grounded.

[fig ·J p74] **The reduced amplifier.** **$+V_{CC}$** over **$R_C$** into the collector; the base fed
from **$R_{th} = R_B$** in series with **$V_{th} = V_{BB}$** (both returning to ground); **$R_E$**
from the emitter to ground.

**The equations of the reduced circuit** ·J p74

$$\boxed{\;V_{CC} = I_C R_C + V_{CE} + I_E R_E\;}$$

$$\boxed{\;V_{BB} = I_B R_B + V_{BE} + I_E R_E\;}$$

$$\boxed{\;V_C = V_{CC} - I_C R_C\;}\qquad\qquad \boxed{\;V_C = V_{CE} + I_E R_E\;}$$

$$\boxed{\;V_{CC} = I_C R_C + V_{CB} + V_{BB} - I_B R_B\;}\qquad\text{(see JV6.11)}$$

> ⚠ VERIFY **JV6.11** ·J p74 — the collector-to-base equation has $V_{BB}$ and $I_B R_B$ both
> reversed in sign
>
> The page prints: *"$V_{CC} = I_C R_C + V_{CB} + I_B R_B - V_{BB}$."*
>
> **Correct form:**
> $$\boxed{\;V_{CC} = I_C R_C + V_{CB} + V_{BB} - I_B R_B\;}$$
>
> **Why.** In the Thevenised circuit $V_B = V_{BB} - I_B R_B$ (the base current flows *out of* the
> equivalent source, dropping voltage across $R_B$), and $V_C = V_{CC} - I_C R_C$. Subtracting,
> $V_{CB} = V_{CC} - I_C R_C - V_{BB} + I_B R_B$, which rearranges to the boxed form.
> **A numerical check:** with $V_{CC} = 10$ V, $I_C R_C = 3$ V, $V_{BB} = 1.8$ V, $I_B R_B = 0.02$ V,
> the base sits at 1.78 V and the collector at 7 V, so $V_{CB} = 5.22$ V. The corrected equation
> returns $3 + 5.22 + 1.8 - 0.02 = 10.0$ V ✓; the printed one returns $3 + 5.22 + 0.02 - 1.8 = 6.44$ V
> ✗. See `_verification-log.md`.

> [added] **The two equations that finish the job**, obtained by putting $I_E = (1+\beta)I_B$ into the
> base loop:
> $$\boxed{\;I_B = \frac{V_{BB} - V_{BE}}{R_B + (1+\beta)R_E}\;}\qquad
> \boxed{\;I_E = \frac{V_{BB} - V_{BE}}{R_E + R_B/(1+\beta)}\;}$$
> These are what §6.34's solution uses. **Not in the source** in this form, though the notes' own base
> loop gives them in one line.

> [added] **Why this circuit is the one everybody actually builds.** If $R_B/(1+\beta) \ll R_E$ the
> second equation reduces to $I_E \cong (V_{BB} - V_{BE})/R_E$ — **$\beta$ has vanished**. The Q point
> is then set by two resistors and a supply, and is the same whichever transistor is dropped into the
> socket.

---

## 6.25 The common-emitter amplifier and its capacitors ·J p75

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $C_1$ | input coupling capacitor | F (µF) | 1–10 µF |
| $C_2$ | output coupling capacitor | F (µF) | 1–10 µF |
| $C_3$ | emitter decoupling (bypass) capacitor | F (µF) | 10–100 µF |
| $v_s$ | signal source | V | mV |
| $V_o$ | output signal | V | V |
| $i_b$, $i_c$, $i_e$ | ac components of the three currents | A | µA–mA |
| $V_2$ | dc voltage across $R_{B2}$ | V | 1–2 V |

[fig ·J p75] **The complete amplifier.** **$+V_{CC}$** across the top. **$R_{B1}$** from the rail to
the base node; **$R_{B2}$** from the base node to ground — the divider. **$R_C$** from the rail to the
collector, carrying **$I_C + i_c$**. The source **$v_s$** (a circled sine symbol, its other end
grounded) feeds the base through **$C_1$**, the current into the base marked **$i_b$** before $C_1$
and **$I_B + i_b$** after it. The collector connects through **$C_2$** (current **$i_c$**) to the
output node **$V_o$**, from which **$R_L$** runs to ground. The emitter goes through **$R_E$**
(current **$I_E$**) to ground, with **$C_3$** in parallel with $R_E$ (current **$i_e$**). A **dashed
oval encircles $R_E$ and $C_3$** with the caption **"Decoupling circuit"**.

[table] **What each component does, in the notes' own terms** ·J p75

| Component | Role |
|---|---|
| $R_{B1}$, $R_{B2}$ | the potential divider that biases the transistor |
| $R_C$, $R_L$ | *"facilitate the collection of the output signal"* |
| $R_E$ | *"feeds back any change in $I_C$ so as to stabilise the bias condition"* |
| $C_1$ | **blocks any direct current from the source** |
| $C_2$ | **blocks any direct current from appearing at the output** |
| $C_3$ | the **decoupling capacitor** — bypasses the alternating signal to ground, which would otherwise interfere with the bias condition if fed back |

The dc condition at the base ·J p75

$$\boxed{\;V_2 = V_{BE} + I_E R_E\;}$$

> ⚠ VERIFY **JV6.12** ·J p75 — the divider resistors are each given a junction to bias, which is not
> what they do
>
> The page prints: *"$R_{B1}$ is used to reverse bias the collector-base junction and $R_{B2}$ is use
> to forward bias the base-emitter junction."*
>
> **Correct form:** $R_{B1}$ and $R_{B2}$ **together** set one thing — the base voltage
> $V_B = V_{CC}R_{B2}/(R_{B1}+R_{B2})$. The **base–emitter junction is forward biased** because $V_B$
> exceeds $V_E$ by $V_{BE}$; the **collector–base junction is reverse biased** because
> $V_C = V_{CC} - I_C R_C$ is held above $V_B$ **by $V_{CC}$ acting through $R_C$**.
>
> **Why the printed version is not just loose but backwards:** raising $R_{B1}$'s pull-up raises $V_B$
> and therefore **reduces** the collector–base reverse bias. Neither resistor can be assigned to one
> junction; the divider is a single two-resistor network with a single output. See
> `_verification-log.md`.

> [added] **A word on $C_3$.** The notes describe it as bypassing *"high frequency"* signal to ground.
> Its real job is broader: it short-circuits $R_E$ **at every signal frequency in the passband**, so
> the emitter degeneration that stabilises the dc bias (§6.20) does **not** also cut the ac voltage
> gain. Without $C_3$ the stage's gain falls roughly from $R_C/r_e$ to $R_C/R_E$. The term used
> elsewhere in this knowledge base — and in most textbooks — is **bypass capacitor**; the notes' word
> is *decoupling*.

**The ac current relations, in lower case** ·J p75

$$i_C = \alpha i_E \qquad i_B = (1-\alpha)i_E \qquad \frac{i_C}{i_B} = \beta = \frac{\alpha}{1-\alpha}$$

*"Since $\alpha \cong 1$ then $\beta$ has a very large value, thus there is a large current gain from
the base to the collector in the common emitter configuration."* ·J p75

---

## 6.26 The dc equivalent circuit and the dc load line ·J p75–p76

[def] The **dc load line** is a line drawn on the output characteristics giving **all the possible
pairs of $I_C$ and $V_{CE}$** for the load the collector sees. It is developed by ·J p75

- **opening all the capacitors**, and
- **shorting all the ac sources**.

[fig ·J p76] **Two circuits, one above the other.** The upper one is the full amplifier of §6.25
again. The lower one is its **dc equivalent**: $V_{CC}$, $R_{B1}$, $R_{B2}$, $R_C$ and $R_E$ only —
$C_1$, $C_2$, $C_3$, $v_s$ and $R_L$ have all vanished, leaving the divider-bias circuit of §6.24.

[derivation] **Deriving the load line from the CE equation** ·J p76

$$V_{CC} = I_C R_C + V_{CE} + I_E R_E$$

$$V_{CC} = I_C R_C + V_{CE} + \frac{I_C}{\alpha}R_E \qquad (\alpha \cong 1)$$

$$I_C = \frac{V_{CC}-V_{CE}}{R_C + R_E/\alpha} \;\cong\; \frac{V_{CC}-V_{CE}}{R_C+R_E}$$

Split it into the straight-line form:

$$I_C = \frac{-V_{CE}}{R_C+R_E} + \frac{V_{CC}}{R_C+R_E}$$

[eq: j-dc-load-line] Comparing with $y = mx + c$: ·J p76

$$\boxed{\;m = \frac{-1}{R_C+R_E}\;}\qquad\qquad \boxed{\;c = \frac{V_{CC}}{R_C+R_E}\;}$$

**The two end points** ·J p76

$$\boxed{\;\text{$x$-intercept: } I_C \cong 0 \;\Rightarrow\; V_{CE} = V_{CE(cut\text{-}off)} = V_{CC}\;}$$

$$\boxed{\;\text{$y$-intercept: } V_{CE} \cong 0 \;\Rightarrow\; I_C = I_{C(sat)} = \frac{V_{CC}}{R_C+R_E}\;}$$

[fig ·J p77] **The dc load line alone.** Vertical axis $I_C$, horizontal axis $V_{CE}$. A straight
line from **$I_{C(sat)}$ on the $I_C$ axis** down to **$V_{CC}$ on the $V_{CE}$ axis**, labelled **"dc
loadline"**.

> [added] **Sanity check on the slope.** $m = -1/(R_C+R_E)$ has units of siemens, and the line falls
> from left to right — as it must, since every extra milliamp of collector current takes another
> $(R_C+R_E)$ millivolts away from $V_{CE}$.

---

## 6.27 The operating point ·J p77

[def] The **operating point** — also called the **Q point, quiescent point, silent point** or **quiet
point** — is the point at which the transistor operates **with no ac signal applied**. It is where the
**curve of the chosen $I_B$ crosses the load line**. ·J p77

**For optimum operation it is placed at the middle of the load line:** ·J p77

[eq: j-q-point]

$$\boxed{\;I_{CQ} = \tfrac{1}{2}I_{C(sat)}\;}\qquad\qquad \boxed{\;V_{CEQ} = \tfrac{1}{2}V_{CC}\;}$$

*"This way the maximum possible swing of an a.c signal can be obtained."* ·J p77

[fig ·J p77] **"D.C load and a.c signal" — the full graphical construction.** In the centre, the **CE
output characteristics** with the **dc load line** superimposed: the line runs from **$I_{C(sat)}$**
on the $I_C$ axis down to **$V_{CC}$** on the $V_{CE}$ axis. The curve family is labelled up the
right-hand side **$I_B = 0, 10, 20, 30, 40, 50\ \mathrm{\mu A}$**. **$I_{CQ}$** is marked on the $I_C$
axis and **$V_{CEQ}$** on the $V_{CE}$ axis, with dashed construction lines meeting at the Q point on
the load line. **To the left**, a **sinusoid drawn against the vertical ($I_C$) axis** — the collector
current swinging about $I_{CQ}$ between two dashed limits. **Below**, a **sinusoid drawn against the
horizontal ($V_{CE}$) axis**, swinging about $V_{CEQ}$ — the output voltage, and it is **inverted**
relative to the current waveform.

> [added] **The 180° phase inversion is visible in that figure and is worth naming.** As $I_C$ swings
> up, the working point slides **up the load line to the left**, so $V_{CE}$ swings **down**. That is
> why a CE stage inverts.

---

## 6.28 Clipping: saturation and cut-off ·J p78

[eq: j-vpp] The peak-to-peak output swing available on the voltage side: ·J p78

$$\boxed{\;V_{pp} = 2V_{CEQ}\;}$$

### Saturation clipping ·J p78

[fig ·J p78] The load line with **$I_{C(sat)}$** and **$I_{CQ}$** marked close together on the $I_C$
axis, and **$V_{CEQ}$** marked well to the left of **$V_{CC}$** — a Q point high up the line. To the
left, two waveforms against the $I_C$ axis: a **small undistorted sinusoid** and, further left, a
**large one whose positive peaks are flattened against the $I_{C(sat)}$ dashed line**.

**The condition** ·J p78

$$I_{C(sat)} - I_{CQ} < I_{CQ}$$

*"When the operating point is close to $I_{C(sat)}$ then clipping of the output waveform will occur
due to saturation."* ·J p78

### Cut-off clipping ·J p78

[fig ·J p78] The load line with **$I_{C(sat)}$** well above **$I_{CQ}$**, the **Q point marked low
down the line and close to $V_{CC}$**, and the horizontal axis annotated **$V_{CC} = V_{CE\,cutoff}$**.
Waveforms again to the left (current) and below (voltage); the large one is **clipped on the side that
runs into cut-off**, and the voltage waveform below is drawn **flattened where it reaches $V_{CC}$**.

**The condition** ·J p78

$$I_{C(sat)} - I_{CQ} > I_{CQ} \qquad\Longrightarrow\qquad \boxed{\;\text{max swing} = 2I_{CQ}\;}$$

*"When $I_C$ is increasing from the Q-point, $V_{CE}$ is decreasing since the load line has a negative
gradient. When the operating point is close to $V_{CE(cutoff)}$ clipping starts occurring due to the
cut-off value of $V_{CE}$."* ·J p78

> ⚠ VERIFY **JC6.13** ·J p78 — the sentence names $V_{CC}$ where $V_{CE}$ is meant
>
> The page prints: *"When $I_C$ is increasing from the Q – point, $V_{CC}$ is decreasing since the load
> line has a negative gradient."*
>
> **Correct form:** it is **$V_{CE}$** that decreases. $V_{CC}$ is the fixed supply and is by
> definition the $V_{CE}$-axis intercept of the load line — it cannot move. See
> `_verification-log.md`.

> [added] **The rule in one line.** Whichever of the two arms of the load line either side of $Q$ is
> **shorter** is the one that clips first. Put $Q$ at the centre and both arms are equal — which is
> exactly what §6.27's $I_{CQ} = \frac{1}{2}I_{C(sat)}$ says.

---

## 6.29 The ac equivalent circuit and the ac load line ·J p79–p80

> **Note on the heading.** ·J p79 opens with *"This is the line which give the different value of
> $i_c$ and $v_{ce}$ depending on the load as seen by $i_C$..."* — the **"A.C load line" heading is
> absent**, lost at the page break. The subject is unambiguous.

[def] The **ac load line** gives the values of $i_c$ and $v_{ce}$ for the load as seen by the **total**
collector current ·J p79

$$i_C = I_C(\mathrm{dc}) + i_c(\mathrm{ac})$$

It is *"obtained by adding a small signal to the already biased circuit."* ·J p79

[def] The **ac equivalent circuit** is obtained by ·J p79

- **shorting all capacitors**, and
- **grounding all dc sources**.

[fig ·J p79] **The ac equivalent.** The source **$v_s$** on the left, one end grounded, feeding the
base directly (no $C_1$ — it is a short). **$R_{B1}$ and $R_{B2}$ now both run from the base node to
ground**, side by side. The **emitter goes straight to ground** (through the shorted $C_3$), with the
ac emitter current **$i_e$** arrowed upward into the emitter and **$i_b$** arrowed into the base. At
the collector, the top rail is now a **ground rail**, so **$R_C$** and **$R_L$** hang from it in
**parallel**, carrying **$i_{c1}$** and **$i_{c2}$** respectively.

[eq: j-rac] **The ac load** ·J p79

$$\boxed{\;R_{ac} = \frac{R_C R_L}{R_C+R_L}\;}\qquad\qquad \boxed{\;R_{ac} < R_{dc}\ \text{(always)}\;}$$

[eq: j-ac-load-line] **The two end points of the ac load line** ·J p79–p80

$$\boxed{\;I_{C(sat)}\big|_{ac} = I_{CQ} + \frac{V_{CEQ}}{R_{ac}}\;}\qquad\qquad
\boxed{\;V_{CE(cut\text{-}off)}\big|_{ac} = V_{CEQ} + I_{CQ}R_{ac}\;}$$

[fig ·J p79] **The ac construction.** The load line drawn from $I_{C(sat)}$ to $V_{CC}$ with $I_{CQ}$
and $V_{CEQ}$ marked and dashed lines meeting at $Q$; below the horizontal axis, the **$V_{CE}$
waveform** swinging about $V_{CEQ}$ between dashed limits.

[fig ·J p80] **The ac load line.** Vertical axis $I_C$, horizontal axis $V_{CE}$. A straight line
labelled **"ac loadline"** from **$I_{CQ} + V_{CEQ}/R_{ac}$** on the $I_C$ axis down to
**$V_{CEQ} + I_{CQ}R_{ac}$** on the $V_{CE}$ axis, with a dashed construction to the Q point on it.

*"Since $R_{ac} < R_{dc}$ the gradient of the a.c load line is steeper."* ·J p80

**Peak-to-peak swing** ·J p80

$$\boxed{\;V_{pp} = 2I_{CQ}R_{ac}\;}\qquad\qquad \boxed{\;V_{pp} = 2V_{CEQ}\;}$$

*"For clipping not to occur, then the lesser value is considered."* ·J p80

$$\boxed{\;V_{pp(\max)} = \min\!\left(2I_{CQ}R_{ac},\ 2V_{CEQ}\right)\;}$$

> [added] **Reading that off the ac load line.** Moving right from $Q$ you run out of line after
> $I_{CQ}R_{ac}$ volts; moving left you run out after $V_{CEQ}$ volts. The shorter arm clips first, so
> the largest undistorted output is twice the shorter arm. A Q point chosen for **maximum undistorted
> swing** therefore satisfies $V_{CEQ} = I_{CQ}R_{ac}$ — the mid-point of the **ac** load line, not
> the dc one.

---

## 6.30 Causes of Q-point variation ·J p80

[fig ·J p80] The full CE amplifier of §6.25 redrawn — $V_{CC}$, $R_{B1}$, $R_{B2}$, $R_C$, $R_E$,
$C_1$, $C_2$, $C_3$, $v_s$ and $R_L$ — as the circuit whose faults are being discussed.

**(i) A faulty resistor.** *"When resistors go faulty they become open."* ·J p80

- If **$R_C$ or $R_E$ goes open**:
  $$I_C = \frac{V_{CC}}{R_C+R_E} = \frac{V_{CC}}{\infty} = 0 \qquad\Longrightarrow\qquad \text{the transistor is in cut-off}$$
- If **$R_{B2}$ goes open**, *"then the transistor is off"* — **but see JV6.13**.

**(ii) A faulty capacitor** — *"the capacitor becomes a short."* ·J p80

**(iii) High temperature** — can cause **thermal runaway**. ·J p80

**(iv) Change of transistor.** ·J p80

> ⚠ VERIFY **JV6.13** ·J p80 — an open $R_{B2}$ turns the transistor hard **on**, not off
>
> The page prints: *"If $R_{B2} = \infty$ then the transistor is off."*
>
> **Correct form:** with $R_{B2}$ open the base is fed only through $R_{B1}$, and the stage reverts to
> **base bias** with $R_B = R_{B1}$:
> $$I_B = \frac{V_{CC}-V_{BE}}{R_{B1}+(1+\beta)R_E}$$
> which is normally far more base current than the divider was supplying, driving the transistor
> **into saturation**. It is **$R_{B1}$ open** that removes the base drive and turns the transistor
> **off**.
>
> **Numerical check** with the §6.34 values ($V_{CC} = 20$ V, $R_{B1} = 47$ k$\Omega$,
> $R_{B2} = 10$ k$\Omega$, $R_E = 2$ k$\Omega$, $\beta = 200$): normally $I_C = 1.37$ mA. With
> $R_{B2}$ open, $I_B = 19.3/(47+402) = 43\ \mathrm{\mu A}$ and $\beta I_B = 8.6$ mA — far above
> $I_{C(sat)} = 3.77$ mA, so the transistor saturates. See `_verification-log.md`.

> ⚠ VERIFY **JC6.14** ·J p80 — *"thermal runway"* for **thermal runaway**. Cosmetic only.
> See `_verification-log.md`.

> [added] **Capacitors fail both ways.** The page lists only the short-circuit failure. An **open**
> coupling capacitor is at least as common and is easy to diagnose: the dc bias is untouched (so every
> dc voltage measures correctly) but the signal disappears. A **shorted $C_1$**, by contrast, drags
> the source's dc level onto the base and moves the Q point — which is the case the page has in mind.

---

## 6.31 The stability factor ·J p81

> **Note on the heading.** ·J p81 opens with *"This is the rate of change of $I_C$ with respect to
> $I_{CBO}$"* — the **"Stability factor" heading is absent**, lost at the page break. The definition
> that follows identifies it beyond doubt.

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $S$ | stability factor | dimensionless | 1 (CB) to $1+\beta$ (base bias); 5–10 for a good divider |
| $R_B$ | **total resistance on the base side** | $\Omega$ (k$\Omega$) | 8–15 k$\Omega$ |
| $R_E$ | **total resistance on the emitter side** | $\Omega$ (k$\Omega$) | 1–2 k$\Omega$ |

[def] The **stability factor** is the rate of change of collector current with respect to the leakage
current, **with $I_B$ and $\beta$ held constant**: ·J p81

$$\boxed{\;S = \frac{dI_C}{dI_{CBO}}\;}\qquad (I_B,\ \beta\ \text{constant})$$

[derivation] **The common-emitter case** ·J p81

Start from the collector current including leakage:

$$I_C = \beta I_B + (1+\beta)I_{CBO}$$

Differentiate throughout with respect to $I_C$:

$$\frac{dI_C}{dI_C} = \frac{d(\beta I_B)}{dI_C} + \frac{d\big[(1+\beta)I_{CBO}\big]}{dI_C}$$

$$1 = \beta\frac{dI_B}{dI_C} + (1+\beta)\frac{dI_{CBO}}{dI_C}$$

$$1 = \beta\frac{dI_B}{dI_C} + (1+\beta)\frac{1}{S}$$

$$(1+\beta)\frac{1}{S} = 1 - \beta\frac{dI_B}{dI_C}$$

[eq: j-stability-factor]

$$\boxed{\;S = \frac{1+\beta}{1 - \beta\,\dfrac{dI_B}{dI_C}}\;}$$

**And the circuit form the examples use** ·J p81

$$\boxed{\;S = \frac{1 + \dfrac{R_B}{R_E}}{1 + \dfrac{R_B}{(1+\beta)R_E}}\;}$$

with $R_B$ the resistance on the **base** side and $R_E$ the resistance on the **emitter** side. ·J p81

**·J p83 gives the same thing rearranged**, and it is the form the worked example evaluates:

$$\boxed{\;S = (1+\beta)\,\frac{1 + \dfrac{R_B}{R_E}}{1 + \beta + \dfrac{R_B}{R_E}}\;}$$

*[added] The two forms are identical: divide the numerator and denominator of the second by
$(1+\beta)$ and the first falls out. **Note that the denominator carries $(1+\beta)$, not $\beta$** —
the $\beta$-only version seen in some textbooks is the approximation $1+\beta \cong \beta$.*

> [added] **The two limiting cases, as a check on the formula.**
> - $R_E = 0$ (plain base bias): $R_B/R_E \to \infty$, both fractions are dominated by that term, and
>   $S \to 1+\beta$ — exactly the value ·J p70 gives for base bias ✓.
> - $R_B = 0$ (base held at a stiff voltage): $S \to 1$ — the best any circuit can do ✓.
>
> Everything in between is a trade: making $R_B$ small relative to $\beta R_E$ buys stability, at the
> cost of a low input impedance and wasted divider current.

---

## 6.32 Design of a single-stage low-power amplifier ·J p81–p82

[table] **The specifications the notes set** ·J p81

| Specification | Value | Reason given |
|---|---|---|
| divider current $I_1$ through $R_{B1}$, $R_{B2}$ | $I_1 \geq 10\,I_B$ | so the base loading does not disturb the divider |
| collector current $I_C$ | 2 mA | above 2 mA "clipping occurs", so this is the value for **faithful amplification** |
| absolute ceiling on $I_C$ | 15 mA | *"if $> 15$ mA then the transistor burns out"* |
| headroom | $I_C$ should exceed the ac signal by **20 %** | to avoid clipping if the Q point moves |

### [ex] Design example — find $R_{B1}$, $R_{B2}$ and $R_E$ ·J p81–p82

**Statement.** A common-emitter connection has $V_{CC} = 9$ V, $V_{CE} = 3$ V, $V_{BE} = 0.3$ V,
$I_1 = 10I_B$, $I_C = 2$ mA, $R_C = 2.2$ k$\Omega$ and $\beta = 50$. Determine $R_{B1}$, $R_{B2}$ and
$R_E$. ·J p81

**Solution as printed** ·J p81–p82

Using the common-emitter equation, with $I_E = \dfrac{1+\beta}{\beta}I_C$:

$$V_{CC} = I_C R_C + V_{CE} + I_E R_E = I_C R_C + V_{CE} + \frac{1+\beta}{\beta}I_C R_E$$

$$9 = 2\times2.2 + 3 + \frac{51}{50}\times2\times R_E$$

$$\boxed{\;R_E = 784\ \Omega\;}$$

$$I_B = \frac{I_C}{\beta} = \frac{2}{50} = 0.04\ \mathrm{mA}$$

$$I_1 = 10\,I_B = 10\times0.04 = 0.4\ \mathrm{mA}$$

$$R_{B1}+R_{B2} = \frac{V_{CC}}{I_1} = \frac{9}{0.4\times10^{-3}} = 22.5\ \mathrm{k\Omega}$$

$$V_B = V_{BE} + I_E R_E = 0.3 + \frac{51}{50}\times2\times784 = 0.3 + 1.6 = 1.9\ \mathrm{V}$$

$$R_{B2} = \frac{V_B}{I_1} = \frac{1.9}{0.4\times10^{-3}} = \boxed{4.75\ \mathrm{k\Omega}}$$

$$R_{B1} = 22.5 - 4.75 = \boxed{17.75\ \mathrm{k\Omega}}$$

*[added] **Every number recomputed.***

| Step | Working | Result | Page |
|---|---|---|---|
| $I_C R_C$ | $2\ \mathrm{mA}\times2.2\ \mathrm{k\Omega}$ | 4.4 V | ✓ |
| left for $R_E$ | $9 - 4.4 - 3$ | 1.6 V | ✓ |
| $I_E$ | $(51/50)\times2\ \mathrm{mA}$ | 2.04 mA | ✓ |
| $R_E$ | $1.6/2.04$ | **0.78431 k$\Omega$ = 784.3 $\Omega$** (page: 784 $\Omega$) | ✓ |
| $I_B$ | $2/50$ | 0.04 mA | ✓ |
| $I_1$ | $10\times0.04$ | 0.4 mA | ✓ |
| $R_{B1}+R_{B2}$ | $9/0.4\ \mathrm{mA}$ | 22.5 k$\Omega$ | ✓ |
| $I_E R_E$ | $2.04\ \mathrm{mA}\times784\ \Omega$ | 1.5994 V (page: 1.6 V) | ✓ |
| $V_B$ | $0.3+1.5994$ | **1.899 V** (page: 1.9 V) | ✓ |
| $R_{B2}$ | $1.9/0.4\ \mathrm{mA}$ | **4.75 k$\Omega$** | ✓ |
| $R_{B1}$ | $22.5-4.75$ | **17.75 k$\Omega$** | ✓ |

*Every figure on the page is confirmed. Nothing rounds badly enough to matter.*

> ⚠ VERIFY **JC6.15** ·J p82 — two typesetting defects in the printed solution
>
> (i) The **first line of ·J p82 is clipped by the page top**: only the fragments *"$R_{B1}$ … $R_{B2}$
> … $I_1$ … $0.4\times10^{-3}$"* survive, with the upper half of every glyph cut away. The line is
> recoverable with certainty from the numbers on either side of it: it is
> $R_{B1}+R_{B2} = V_{CC}/I_1 = 9/(0.4\times10^{-3}) = 22.5\ \mathrm{k\Omega}$ — the value the
> **very next equation subtracts 4.75 from to get 17.75**.
>
> (ii) The $R_{B2}$ line renders as *"$R_{B2} = \dfrac{V_B}{I_1} = 1.\dfrac{9}{0.4\times10^{-3}}$"* —
> the "9" of "1.9" has fallen into the numerator position. The intended line is
> $1.9/(0.4\times10^{-3}) = 4.75$ k$\Omega$, which is what the printed answer is.
> See `_verification-log.md`.

> [added] **Check the design closes.** With $R_{B1} = 17.75$ k$\Omega$ and $R_{B2} = 4.75$ k$\Omega$,
> $V_{Th} = 9\times4.75/22.5 = 1.9$ V ✓ and $R_{Th} = 17.75\parallel4.75 = 3.746$ k$\Omega$. Then
> $I_B = (1.9-0.3)/(3.746 + 51\times0.784) = 1.6/43.73\ \mathrm{k\Omega} = 36.6\ \mathrm{\mu A}$, so
> $I_C = 1.83$ mA against the 2 mA target — an 8 % shortfall, because the design assumed the base
> draws nothing from the divider. That is the price of the $I_1 = 10I_B$ rule of thumb, and it is why
> the rule is usually written $I_1 \geq 10I_B$ rather than $=$.

---

## 6.33 [ex] Worked example — germanium CE amplifier: operating point and stability factor ·J p82–p83

**Statement.** Determine the coordinates of the operating point and the stability factor $S$ in a
common-emitter **germanium** transistor amplifier circuit in which the bias is provided by **self
bias** — an emitter resistor with a potential divider. The parameters are ·J p82

$$V_{CC} = 16\ \mathrm{V},\quad R_C = 3\ \mathrm{k\Omega},\quad R_E = 2\ \mathrm{k\Omega},\quad
R_{B1} = 56\ \mathrm{k\Omega},\quad R_{B2} = 20\ \mathrm{k\Omega},\quad \alpha = 0.985$$

[fig ·J p82] **The circuit.** $V_{CC}$ across the top. **$R_{B1}$** from the rail to the base;
**$R_{B2}$** from the base to the bottom rail; **$R_C$** from the rail to the collector. The
transistor is labelled **$Q_1$**. The input **$v_i$** enters through **$C_1$** to the base; the output
**$v_o$** leaves the collector through **$C_2$**. **$R_E$** runs from the emitter to the bottom rail
with **$C_3$** across it. The bottom rail is grounded.

**Solution as printed** ·J p82–p83

For a germanium transistor $V_{BE} = 0.3$ V. From $\alpha = 0.985$:

$$\beta = \frac{\alpha}{1-\alpha} = \frac{0.985}{1-0.985} = 66$$

**Thevenin's voltage**

$$V_T = \frac{R_2}{R_1+R_2}V_{CC} = \frac{20\times10^{3}}{76\times10^{3}}\times16 = 4.21\ \mathrm{V}$$

**Thevenin's resistance**

$$R_B = \frac{R_1R_2}{R_1+R_2} = \frac{20\times10^{3}\times56\times10^{3}}{76\times10^{3}} = 14.737\ \mathrm{k\Omega}$$

**The loop equation around the base circuit**

$$V_T = I_B R_B + V_{BE} + (I_B+I_C)R_E
= \frac{I_C}{\beta}R_B + V_{BE} + \left(\frac{I_C}{\beta}+I_C\right)R_E$$

$$4.21 = \frac{I_C}{66}\times14.737\times10^{3} + 0.3 + I_C\left(\frac{1}{66}+1\right)\times2\times10^{3}$$

$$3.91 = I_C\,(0.223 + 2.03)\times10^{3}$$

$$I_C = \frac{3.91}{2.253\times10^{3}} = 1.73\ \mathrm{mA}$$

Since $I_B$ is very small, $I_C \cong I_E = 1.73$ mA, therefore

$$V_{CE} = V_{CC} - I_C R_C - I_E R_E = 16 - 1.73\times3 - 1.73\times2 = 7.35\ \mathrm{V}$$

$$\boxed{\;\text{Q point: } I_C = 1.73\ \mathrm{mA},\qquad V_{CE} = 7.35\ \mathrm{V}\;}$$

**The stability factor**

$$S = (1+\beta)\,\frac{1+\dfrac{R_B}{R_E}}{1+\beta+\dfrac{R_B}{R_E}}
= (1+66)\,\frac{1+\dfrac{14.737}{2}}{1+66+\dfrac{14.737}{2}} = 7.537$$

*[added] **Every number recomputed.***

| Step | Working | Result | Page |
|---|---|---|---|
| $\beta$ | $0.985/0.015$ | **65.667**, rounded to 66 | ✓ |
| $V_T$ | $20\times16/76$ | **4.2105 V** (page: 4.21) | ✓ |
| $R_B$ | $20\times56/76$ | **14.7368 k$\Omega$** (page: 14.737) | ✓ |
| $R_B/\beta$ | $14736.8/66$ | **223.29 $\Omega$** (page: 0.223 k$\Omega$) | ✓ |
| $(1/\beta+1)R_E$ | $(1/66+1)\times2000$ | **2030.3 $\Omega$** (page: 2.03 k$\Omega$) | ✓ |
| total coefficient | $223.29+2030.3$ | **2253.6 $\Omega$** (page: 2.253 k$\Omega$) | ✓ |
| $I_C$ | $3.9105/2253.6$ | **1.7352 mA** (page: 1.73 mA) | ✓ |
| $V_{CE}$ | $16 - 1.73\times5$ | **7.35 V** | ✓ |
| $S$ | $(67)(8.36842)/(74.36842)$ | **7.5393** — see JC6.16 | ⚠ |

*Two refinements worth knowing. (i) Carrying $I_C$ unrounded and keeping $I_E = I_C(1+1/\beta)$ gives
$V_{CE} = 7.27$ V rather than 7.35 V; taking $I_C = I_E$ but unrounded gives 7.32 V. The page's 7.35 V
comes from rounding $I_C$ to 1.73 mA first, which is what its own sentence says it is doing.
(ii) Sanity check on the Q point: the dc load line runs to
$I_{C(sat)} = 16/5\ \mathrm{k\Omega} = 3.2$ mA and $V_{CE(cut\text{-}off)} = 16$ V, so the
mid-point would be (8 V, 1.6 mA). The Q point
(7.35 V, 1.73 mA) sits almost exactly there — a well-centred design.*

> ⚠ VERIFY **JC6.16** ·J p83 — the stability factor is printed as 7.537; recomputation gives 7.539
>
> The page prints $S = 7.537$.
>
> **Recomputed both ways:**
> - with the page's own rounded $\beta = 66$ and $R_B = 14.737$ k$\Omega$: $S = 7.5393$;
> - with the unrounded $\beta = 65.667$ and $R_B = 14.7368$ k$\Omega$: $S = 7.5355$.
>
> **So 7.537 sits between the two and matches neither** — a rounding slip of about 0.03 %. Quote
> **$S \cong 7.54$**. Nothing downstream depends on the third decimal. See `_verification-log.md`.

> [added] **What $S = 7.54$ is telling you.** Plain base bias with this transistor would give
> $S = 1+\beta = 67$. The divider-plus-emitter-resistor arrangement has cut the leakage sensitivity by
> a factor of **nine**, at the cost of the 0.4 mA or so of divider current. That trade is the entire
> argument for method (vi).

---

## 6.34 Problems ·J p83

### [exercise] Problem 1 — load lines and Q point ·J p83

**Statement.** Given the following values for a common-emitter circuit:

$$R_{B1} = 47\ \mathrm{k\Omega},\quad R_L = 10\ \mathrm{k\Omega},\quad R_{B2} = 10\ \mathrm{k\Omega},
\quad R_C = 3.3\ \mathrm{k\Omega},\quad R_E = 2\ \mathrm{k\Omega},\quad \beta = 200,
\quad V_{CC} = 20\ \mathrm{V}$$

**(i)** Draw the dc and ac load lines and determine the operating point.
**(ii)** Determine whether the transistor is operating close to saturation or cut-off. ·J p83

> [added] **Solution — worked in full, and not in the source.**
>
> The problem does not state $V_{BE}$ or the material. **Assume silicon, $V_{BE} = 0.7$ V** — the
> value ·J p65 and ·J p67 both quote for silicon. (If germanium were intended, $V_{BE} = 0.3$ V and
> every current below rises by about 14 %; the conclusion in (ii) is unchanged.)
>
> **Step 1 — Thevenin the divider** (§6.24)
> $$V_{Th} = \frac{V_{CC}R_{B2}}{R_{B1}+R_{B2}} = \frac{20\times10}{57} = 3.509\ \mathrm{V}$$
> $$R_{Th} = \frac{R_{B1}R_{B2}}{R_{B1}+R_{B2}} = \frac{47\times10}{57} = 8.246\ \mathrm{k\Omega}$$
>
> **Step 2 — the Q point**
> $$I_B = \frac{V_{Th}-V_{BE}}{R_{Th}+(1+\beta)R_E} = \frac{3.509-0.7}{8.246 + 201\times2}
> = \frac{2.809}{410.25\ \mathrm{k\Omega}} = 6.85\ \mathrm{\mu A}$$
> $$I_{CQ} = \beta I_B = 200\times6.85\ \mathrm{\mu A} = 1.369\ \mathrm{mA}
> \qquad I_E = 201\,I_B = 1.376\ \mathrm{mA}$$
> $$V_{CEQ} = V_{CC} - I_C R_C - I_E R_E = 20 - 1.369\times3.3 - 1.376\times2 = 12.73\ \mathrm{V}$$
> $$\boxed{\;\text{Q point: } (V_{CEQ},\ I_{CQ}) = (12.73\ \mathrm{V},\ 1.37\ \mathrm{mA})\;}$$
> *(By the quicker approximation that ignores $I_B$ altogether: $V_B = 3.509$ V, $V_E = 2.809$ V,
> $I_E = 2.809/2 = 1.404$ mA, $V_{CE} = 20 - 1.404\times5.3 = 12.56$ V — within 1.4 %, which is the
> usual size of the error the $\beta$-independent shortcut costs.)*
>
> **Step 3 — the dc load line** (§6.26)
> $$I_{C(sat)} = \frac{V_{CC}}{R_C+R_E} = \frac{20}{5.3} = 3.774\ \mathrm{mA}
> \qquad V_{CE(cut\text{-}off)} = V_{CC} = 20\ \mathrm{V}$$
> So the dc load line runs from $(0,\ 3.77\ \mathrm{mA})$ to $(20\ \mathrm{V},\ 0)$, and $Q$ sits on
> it — check: $20 - 1.376\times5.3 = 12.71$ V ✓.
>
> **Step 4 — the ac load line** (§6.29)
> $$R_{ac} = \frac{R_C R_L}{R_C+R_L} = \frac{3.3\times10}{13.3} = 2.481\ \mathrm{k\Omega}$$
> $$I_{C(sat)}\big|_{ac} = I_{CQ}+\frac{V_{CEQ}}{R_{ac}} = 1.369 + \frac{12.73}{2.481} = 6.50\ \mathrm{mA}$$
> $$V_{CE(cut\text{-}off)}\big|_{ac} = V_{CEQ}+I_{CQ}R_{ac} = 12.73 + 1.369\times2.481 = 16.13\ \mathrm{V}$$
> So the ac load line runs from $(0,\ 6.50\ \mathrm{mA})$ to $(16.13\ \mathrm{V},\ 0)$, crossing the
> dc line at $Q$ and — as ·J p80 says it must — **steeper**, because
> $R_{ac} = 2.48\ \mathrm{k\Omega} < R_{dc} = 5.3\ \mathrm{k\Omega}$.
>
> **[fig — how to draw it]** One set of axes, $I_C$ (mA) vertical, $V_{CE}$ (V) horizontal. Mark
> **A** $(20,\ 0)$ and **B** $(0,\ 3.77)$ and join them — the **dc load line**. Mark **Q** on it at
> $(12.73,\ 1.37)$. Through $Q$ draw the **ac load line** to **C** $(16.13,\ 0)$ and **D**
> $(0,\ 6.50)$. Dashed construction lines drop from $Q$ to $V_{CEQ}$ and run left to $I_{CQ}$.
>
> **(ii) Saturation or cut-off?** Apply ·J p78's test on the **dc** line:
> $$I_{C(sat)} - I_{CQ} = 3.774 - 1.369 = 2.405\ \mathrm{mA} \;>\; I_{CQ} = 1.369\ \mathrm{mA}$$
> and equivalently $V_{CEQ} = 12.73$ V is well above $\tfrac{1}{2}V_{CC} = 10$ V.
> $$\boxed{\;\text{The Q point lies below the mid-point of the load line — the transistor is operating closer to CUT-OFF.}\;}$$
> **Cut-off clipping will therefore be the first limit reached.** On the ac load line the two arms are
> $$I_{CQ}R_{ac} = 1.369\times2.481 = 3.40\ \mathrm{V} \qquad\text{and}\qquad V_{CEQ} = 12.73\ \mathrm{V}$$
> so the maximum undistorted output is $V_{pp} = 2\times3.40 = \mathbf{6.80\ V}$ peak-to-peak, set by
> the **current** arm — i.e. by cut-off — exactly as the region test predicts.
>
> *All figures above were recomputed numerically; the load-line intercepts and the Q point are
> self-consistent to three significant figures.*

> [added] **Worth noticing:** this problem is a near-twin of the exercise the tier-2 chapter breaks
> off in the middle of (`13-bipolar-junction-transistor.md` §3.27, Example 58.12: $V_{CC} = 20$ V,
> collector-plus-emitter resistance 5 k$\Omega$, same question about maximum peak-to-peak swing).
> Working this one through gives the reader the method that file could not finish.

### [exercise] Problem 2 — essay ·J p83

**Statement.** *"Explain the operation of various biasing methods and their advantages and
disadvantages. Use suitable expressions where necessary."* ·J p83

> [added] **The answer plan this question wants** — six methods, §§6.19–6.24, each with its defining
> equation, its stability factor and one sentence of judgement.
>
> | Method | Key expression | Advantage | Disadvantage |
> |---|---|---|---|
> | base bias | $I_B = \dfrac{V_{CC}-V_{BE}}{R_B}$, $I_{C(sat)} = \dfrac{V_{CC}}{R_C}$ | simplest; one resistor | $S = 1+\beta$; $I_C$ tracks $\beta$ exactly — unusable for production |
> | emitter feedback | $I_B = \dfrac{V_{CC}-V_{BE}}{R_B+(1+\beta)R_E}$ | degeneration through $R_E$ opposes any rise in $I_C$ | costs voltage headroom across $R_E$; needs $C_3$ to recover the ac gain |
> | collector feedback | $V_C = I_B R_B + V_{BE}$, $I_C \cong \dfrac{V_{CC}-V_{BE}}{R_C+R_B/\beta}$ | self-correcting through $V_C$; only one supply, few parts | the feedback path also reduces the ac gain |
> | both feedbacks | $I_{C(sat)} = \dfrac{V_{CC}}{R_C+R_E}$ | best stability of the base-bias family | most components; both gain penalties |
> | two supplies | $I_E \cong \dfrac{V_{EE}-V_{BE}}{R_E+R_B/\beta}$, $V_B \cong 0$ | Q point almost independent of the transistor | needs a **second** supply |
> | voltage divider | $V_{Th} = \dfrac{V_{CC}R_{B2}}{R_{B1}+R_{B2}}$, $I_E \cong \dfrac{V_{Th}-V_{BE}}{R_E}$ | $\beta$ drops out; one supply; the standard choice | divider current is wasted; input impedance lowered by $R_{B1}\parallel R_{B2}$ |
>
> **Not in the source** — assembled from §§6.19–6.24 and §6.31 of this file.

---

## 6.35 How this file compares with the tier-2 chapter

The supporting file `13-bipolar-junction-transistor.md` covers the same ground from a printed
textbook chapter, fully verified. **This file is tier 1 — the course's own notes — and wins on scope
and emphasis.** Where the two differ in content, here is the map.

[table] **Agreements — checked item by item**

| Item | ·J (this file) | Tier-2 (`13-...`) | Verdict |
|---|---|---|---|
| $\alpha = I_C/I_E$ | ✔ printed correctly, twice (·J p60, ·J p63) | ✘ printed **inverted** as $I_E/I_C$; flagged **V3.1** | **·J is right.** Independent confirmation of the tier-2 flag |
| $\beta = \alpha/(1-\alpha)$ and $\alpha = \beta/(1+\beta)$ | ✔ ·J p63, both derived | ✔ same pair, both derived | agree exactly |
| $I_E = I_C + I_B$ | ✔ ·J p58, p60 | ✔ | agree |
| $\theta = I_E/I_B = 1+\beta$ | ✔ ·J p62 (with a symbol slip in the first term, **JV6.5**) | ✔ same chain, no slip | agree on the result |
| $I_C = \alpha I_E + I_{CBO}$ | ✔ ·J p63 | ✔ | agree |
| $I_{CEO} = (1+\beta)I_{CBO} = I_{CBO}/(1-\alpha)$ | ✔ **derived on the page**, ·J p64 | ✔ but **reconstructed** — the pages carrying the derivation are missing from the tier-2 extract | **·J is fuller**: it has the derivation the tier-2 file had to supply as `[added]` |
| $I_C = \beta I_B + I_{CEO}$ | ✔ ·J p64 | ✔ | agree |
| base bias: $I_B = (V_{CC}-V_{BE})/R_B$, $I_{C(sat)} = V_{CC}/R_C$, $S = 1+\beta$ | ✔ ·J p70 | ✔ | agree |
| emitter feedback | $I_B = \dfrac{V_{CC}-V_{BE}}{R_B+(1+\beta)R_E}$ — the **exact** form, ·J p71 | $I_C \cong \dfrac{V_{CC}-V_{BE}}{R_E+R_B/\beta}$ — the **approximate** form | equivalent to within $1/\beta$; **·J's is the exact one** |
| collector feedback | loop equations only, ·J p72 | solved through to $I_C \cong \dfrac{V_{CC}-V_{BE}}{R_L+R_B/\beta}$ | **tier-2 is fuller**; the solved form is supplied `[added]` in §6.21 |
| both feedbacks | $I_{C(sat)} = V_{CC}/(R_C+R_E)$, $V_{CE(cut\text{-}off)} = V_{CC}$, ·J p72 | also $I_C = \dfrac{V_{CC}-V_{BE}}{R_E+R_L+R_B/\beta}$, plus $S$ and $K_\beta$ | **tier-2 is fuller** |
| two-supply emitter bias | three loop equations, **two with sign errors** (JV6.9, JV6.10), ·J p73 | $I_E = \dfrac{V_{EE}-V_{BE}}{R_E+R_B/\beta} \cong \dfrac{V_{EE}}{R_E}$, correct | **tier-2 is fuller and cleaner**; the missing result is supplied `[added]` in §6.23 |
| voltage divider | $V_{Th}$, $R_{Th}$, loop equations, ·J p73–p74 | all **three** methods — by inspection, by Thevenin, and by the $\beta$-rule — plus $S$ and $K_\beta$ | **tier-2 is fuller**; ·J gives only the Thevenin route |
| stability factor $S$ | $\dfrac{1+R_B/R_E}{1+R_B/(1+\beta)R_E}$ (·J p81) **and** $(1+\beta)\dfrac{1+R_B/R_E}{1+\beta+R_B/R_E}$ (·J p83) | $\dfrac{1+R_B/R_E}{1+(1-\alpha)R_B/R_E}$, noted as equal to the $(1+\beta)$ form | **agree exactly** — all three expressions are algebraically identical |
| **does the $S$ denominator carry $\beta$ or $1+\beta$?** | **$1+\beta$** | **$1+\beta$**, with $\beta$ offered only as an explicit approximation | **agree**: the exact denominator is $(1+\beta)R_E$ |
| dc load-line intercepts | $I_{C(sat)} = V_{CC}/(R_C+R_E)$, $V_{CE(cut\text{-}off)} = V_{CC}$ | $I_{C(sat)} = V_{CC}/R_L$ (its worked circuit has **no** $R_E$), $V_{CE(cut\text{-}off)} = V_{CC}$ | **agree** — same formula, tier-2's example simply has $R_E = 0$ |
| ac load-line intercepts | $I_{CQ}+V_{CEQ}/R_{ac}$ and $V_{CEQ}+I_{CQ}R_{ac}$ | identical pair, plus **slope** $=-1/R_{ac}$ | **agree exactly** |
| peak-signal handling | $V_{pp} = \min(2I_{CQ}R_{ac},\ 2V_{CEQ})$ | $\min(I_{CQ}R_{ac},\ V_{CEQ})$ as a **peak**, i.e. the same thing halved | **agree** — ·J states it peak-to-peak, tier-2 as a peak |

**No genuine disagreement on the physics was found between the two documents.** Every difference is
one of completeness, of exact-versus-approximate form, or a printing defect in one source that the
other gets right.

[table] **Where each source is the better read**

| Topic | Better in |
|---|---|
| device construction, doping, NPN *and* PNP operation | **·J** — tier-2 is terse here |
| the three configurations' full parameter lists (input/output current, voltage, resistance, power) | **·J** — tier-2 has no equivalent table |
| $h$-parameter symbol conventions and gain in dB | **·J** (·J p61); developed much further in `16-h-parameters-and-bjt-amplifiers.md` |
| leakage derivations from first principles | **·J** — the tier-2 pages are missing |
| thermal runaway with the Si/Ge doubling temperatures | **·J** (but see **JV6.8**) |
| all three families of static characteristics with test circuits | **·J** — CB, CE **and** CC, each with input, output and transfer |
| $\beta$-sensitivity $K_\beta$ | **tier-2 only** — ·J does not mention it |
| the $\beta$-rule for divider bias | **tier-2 only** |
| solved bias formulas for collector feedback, both feedbacks and two supplies | **tier-2** |
| the CE amplifier's capacitors and component roles | **·J** — tier-2 does not itemise them |
| dc and ac equivalent circuits drawn side by side | **·J** |
| saturation- and cut-off-clipping constructions | **·J** — the clearest treatment in either source |
| worked amplifier **design** (choosing $R_{B1}$, $R_{B2}$, $R_E$) | **·J only** (§6.32) |
| a complete, self-contained divider-bias numerical example | **·J** (§6.33) — tier-2's equivalent breaks off mid-example |

---

## 6.36 Verification flags raised in this range

[table] **Substantive — would mislead a learner or produce a wrong answer**

| ID | Page | What the page prints | Correct form |
|---|---|---|---|
| **JV6.1** | ·J p58 | moderate collector doping *reduces* the power dissipated | the large **area** reduces $R = \rho L/A$; lighter doping raises $\rho$ |
| **JV6.2** | ·J p60, p61 | output resistance $= V_{CB}/I_C = h_{OB}$ | $h_{OB} = I_C/V_{CB}$ (siemens); resistance $=1/h_{OB}$ |
| **JV6.3** | ·J p61 | CE input power $= I_E V_{BE}$ | $I_B V_{BE}$ |
| **JV6.4** | ·J p62 | CC output resistance $= V_{CE}/I_C$ | $V_{CE}/I_E$ |
| **JV6.5** | ·J p62 | $\theta = I_E/I_C = \ldots = 1+\beta$ | $\theta = I_E/I_B$ |
| **JV6.6** | ·J p63 | $I_C - \alpha I_C = I_B + I_{CBO}$ | $I_C - \alpha I_C = \alpha I_B + I_{CBO}$ |
| **JV6.7** | ·J p64 | $I_E = (1+\beta)I_B + \frac{1}{1-\alpha}I_{CEO}$ | $I_E = (1+\beta)I_B + I_{CEO}$ |
| **JV6.8** | ·J p64 | Si doubles per 10 °C, Ge per 6 °C (contradicting the same page) | Ge per **10 °C**, Si per **6 °C** |
| **JV6.9** | ·J p73 | $V_{CC} = I_C R_C + V_{CE} + I_E R_E + V_{EE}$ | $V_{CC}+V_{EE} = I_C R_C + V_{CE} + I_E R_E$ |
| **JV6.10** | ·J p73 | $V_{CC} = I_C R_C + I_B R_B + V_{CB}$ | $V_{CC} = I_C R_C + V_{CB} - I_B R_B$ |
| **JV6.11** | ·J p74 | $V_{CC} = I_C R_C + V_{CB} + I_B R_B - V_{BB}$ | $V_{CC} = I_C R_C + V_{CB} + V_{BB} - I_B R_B$ |
| **JV6.12** | ·J p75 | $R_{B1}$ reverse-biases the C–B junction, $R_{B2}$ forward-biases the B–E junction | the divider sets $V_B$; $V_{CC}$ through $R_C$ reverse-biases the C–B junction |
| **JV6.13** | ·J p80 | *"If $R_{B2} = \infty$ then the transistor is off"* | an open $R_{B2}$ drives it into **saturation**; an open $R_{B1}$ turns it off |

[table] **Cosmetic — typo, notation slip, mislabelled figure**

| ID | Page | Defect |
|---|---|---|
| **JC6.1** | ·J p57→p58 | the sentence across the page break repeats *"reduce the base current"*; a line lost or duplicated |
| **JC6.2** | ·J p58 | collector share printed as "(95 % /98 %)" against $I_B = 5\ \%$; only $(95,5)$ or $(98,2)$ is consistent |
| **JC6.3** | ·J p59 | the **PNP** operation block diagram is drawn **N-P-N** |
| **JC6.4** | ·J p61 | the h-parameter table's **column headings are absent**; the "Hybrid" row prints $h_{IB}$ twice |
| **JC6.5** | ·J p65 | input admittance written as the ratio $I_E/V_{BE}$; it is the slope $\Delta I_E/\Delta V_{BE}$ |
| **JC6.6** | ·J p66 | *"Avalacnhe Breakdown"* |
| **JC6.7** | ·J p66 | CE test circuit labels the collector supply $V_{EE}$ and the output voltmeter $V_{CB}$ |
| **JC6.8** | ·J p67 | all five CE output curves labelled $I_B = 40\ \mathrm{\mu A}$ |
| **JC6.9** | ·J p68 | CC test circuit labels the output voltmeter $V_{CB}$ and the supply $V_{EE}$ |
| **JC6.10** | ·J p69 | CC output figure's vertical axis labelled $I_C$ where the caption says $I_E$ |
| **JC6.11** | ·J p72 | $I_{sat} = \frac{V_{CC}}{R_C+R_E}\frac{\beta}{1+\beta} = \frac{V_{CC}}{R_C+R_E}$ — an approximation as an equality |
| **JC6.12** | ·J p73 | the voltage-divider circuit's bottom rail carries **both** a ground symbol and a $-V_{EE}$ label |
| **JC6.13** | ·J p78 | *"$V_{CC}$ is decreasing"* where $V_{CE}$ is meant |
| **JC6.14** | ·J p80 | *"thermal runway"* |
| **JC6.15** | ·J p82 | the page's first line is clipped by the page top; and $R_{B2} = 1.\frac{9}{0.4\times10^{-3}}$ mis-sets $1.9$ |
| **JC6.16** | ·J p83 | $S$ printed 7.537; recomputes to 7.539 (with $\beta = 66$) or 7.536 (with $\beta = 65.67$) |

**Redactions and unreadable material**

| Kind | Page | Item | Recovered? |
|---|---|---|---|
| ⚠ REDACTED | ·J p58 | two green blocks over the condition for effective transistor operation | **Yes, with certainty** — emitter–base forward biased, collector–base reverse biased; confirmed three times over on ·J p58, p59 and p60 (§6.4) |
| ⚠ ILLEGIBLE | ·J p62 | the CE current-gain line has lost its numerator and right-hand side in the render | **Content certain** ($\beta = h_{FE} = I_C/I_B$, confirmed on ·J p63); a screenshot is wanted only to settle which symbol the line names |

**Sections opening with no heading** (recorded, never filled): ·J p57, ·J p65, ·J p73, ·J p79, ·J p81.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
