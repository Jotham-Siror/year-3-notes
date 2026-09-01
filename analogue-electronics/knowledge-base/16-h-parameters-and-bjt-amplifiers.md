---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "16 — h-Parameters and Small-Signal BJT Amplifiers (supporting)"
source: "L6 — 'Lesson 6 H parameters for circuits.pdf', 26 pp."
pages: "1-26"
tier: supporting
file_role: topic
subtopics:
  - "the transistor as a two-port network; dependent and independent variables"
  - "the two hybrid defining equations and the four h-parameters"
  - "definitions of h_i, h_r, h_f, h_o as short-circuit and open-circuit ratios, and their mixed dimensions"
  - "the hybrid equivalent circuit: which source is a voltage source, which a current source"
  - "advantages of the h-parameter description"
  - "the CE h-parameter model and the double-subscript notation hie, hre, hfe, hoe"
  - "hybrid models for all three configurations: CE, CB, CC"
  - "typical numerical values of the twelve h-parameters"
  - "the loaded amplifier: source resistance, load impedance, and the four quantities to be found"
  - "current gain A_I by substitution of the load constraint"
  - "input impedance Z_i and its dependence on the load through A_I"
  - "voltage gain: current gain times the load-to-input impedance ratio"
  - "output admittance Y_o with the source shorted"
  - "overall gains referred to the source: Avs and Ais"
  - "conversion formulae between CE, CB and CC h-parameters"
  - "characteristics and applications of CE, CB and CC amplifiers"
  - "the numerical comparison table for load and source both 3 kilohm"
  - "the simplified (approximate) CE hybrid model: when hre and hoe may be dropped"
  - "approximate analysis of the CE, CC and CB amplifiers"
  - "three fully worked numerical problems, exact and approximate"
key_equations: [two-port-h-equations, h-i-def, h-r-def, h-f-def, h-o-def, ce-h-equations, cb-h-equations, cc-h-equations, current-gain-ai, input-impedance-zi, voltage-gain-av, output-admittance-yo, voltage-gain-source-avs, current-gain-source-ais, avs-from-ais, power-gain-ap, conv-cb, conv-cc, approx-ce, approx-cc, approx-cb, ce-ri-correction, delta-h, zi-delta-h, yo-delta-h]
prerequisites: ["03-bipolar-junction-transistor (the three configurations, alpha and beta, dc biasing, the ac load line)", "two-port network algebra; Thevenin and Norton equivalents; current and voltage division"]
leads_to: ["multistage and cascaded amplifiers", "frequency response of BJT amplifiers", "feedback amplifiers"]
verification_flags: 12
tags: [h-parameters, hybrid-model, two-port-network, small-signal, bjt-amplifier, common-emitter, common-base, common-collector, emitter-follower, current-gain, voltage-gain, input-impedance, output-admittance, approximate-analysis, conversion-formulae]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·L6 pN = provenance (which PDF page of Lesson 6 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 06 — h-Parameters and Small-Signal BJT Amplifiers

Scope: the whole of L6, 26 PDF pages. Treats the transistor as a two-port network, builds the hybrid
(h-parameter) model, defines the four parameters and their double-subscript forms for CE, CB and CC,
derives the four figures of merit — $A_I$, $Z_i$, $A_V$, $Y_o$ — plus the two source-referred gains
$A_{VS}$ and $A_{IS}$, tabulates the conversion formulae between configurations, compares the three
configurations numerically, then develops the simplified (approximate) model and applies it to all
three configurations. It closes with three fully worked numerical problems, each done twice — once
exactly and once approximately.

---

## 6.0 What this document is, and how to read it

**L6 is a set of handwritten lecture notes**, scanned to PDF. Twenty-six pages:

- **·L6 p1** — the unit title page (UNIT III, BJT Amplifiers) with the five-item syllabus list.
- **·L6 p2** — **blank**. Nothing on it, not even a page number.
- **·L6 p3–p26** — the notes proper, in a single continuous hand.

Three consequences worth knowing before working from it:

1. **The PDF has no usable text layer.** Every page is an image. Everything in this file was read
   from the rendered page images, and where a subscript was ambiguous the region was magnified
   before being transcribed.
2. **·L6 p7 is rotated 90°** in the PDF — it is a landscape table of the three hybrid models. It has
   been read in its rotated orientation and is transcribed here in §6.6.
3. **The notes carry no printed page numbers and no section numbers.** All ·L6 pN citations are PDF
   page numbers, which equal the render filenames. The §6.x headings are this file's own.

**The lesson is roughly two-thirds algebra and one-third arithmetic.** Pages 3–22 are almost entirely
symbolic — two-port algebra, substitution, and tabulation of the same four results in three
configurations. Pages 23–26 are three worked numerical problems. There is **no unsolved exercise set
anywhere in L6**; every problem the notes state, they also solve. See §6.25.

**Notation warning that matters more here than anywhere else in the course.** This lesson runs three
parallel notations for the same four quantities:

| Generic | CE | CB | CC |
|---|---|---|---|
| $h_i$ or $h_{11}$ | $h_{ie}$ | $h_{ib}$ | $h_{ic}$ |
| $h_r$ or $h_{12}$ | $h_{re}$ | $h_{rb}$ | $h_{rc}$ |
| $h_f$ or $h_{21}$ | $h_{fe}$ | $h_{fb}$ | $h_{fc}$ |
| $h_o$ or $h_{22}$ | $h_{oe}$ | $h_{ob}$ | $h_{oc}$ |

The **second** subscript names the configuration (e for common-emitter, b for common-base, c for
common-collector); the **first** names the parameter (i input, r reverse, f forward, o output). Two of
this file's flags are exactly this: a CE parameter left standing inside a CC formula, and $i_c$ where
$v_c$ was meant. Read subscripts letter by letter.

---

## 6.1 The transistor as a two-port network ·L6 p3

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_i$, $I_1$ | input (signal) current to the amplifier | A | 10–100 µA (CE) |
| $V_i$, $V_1$ | input (signal) voltage to the amplifier | V | 1–20 mV |
| $I_o$, $I_2$ | output (signal) current of the amplifier | A | 0.5–5 mA |
| $V_o$, $V_2$ | output (signal) voltage of the amplifier | V | 0.1–2 V |

[def] A transistor amplifier can be treated as a **two-port network** — a box with one pair of input
terminals and one pair of output terminals, described entirely by what happens at those four
terminals. ·L6 p3

[fig ·L6 p3] A rectangle labelled **"Transistor Amplifier"**. On its left, two leads go out to a pair
of terminals; the upper terminal carries a **+** and the lower a **−**, and the port voltage between
them is labelled $V_i$. An arrow on the upper lead points **into** the box and is labelled $I_i$. On
its right, two leads go out to a second pair of open-circle terminals; the upper carries **+**, the
lower **−**, and the port voltage is $V_o$. An arrow on the upper right lead points **left, into the
box**, labelled $I_o$.

> [added] **The arrow direction on $I_o$ is not decoration — it is the whole sign convention of this
> lesson.** Both port currents are taken **positive when flowing into the network**. That is why the
> current gain later comes out as $A_I = -I_2/I_1$ rather than $+I_2/I_1$: the current delivered to
> the load flows *out* of the port, so $I_L = -I_2$.

[def] **The transistor is a current-operated device**, so the pair of variables treated as *given* is
chosen accordingly: ·L6 p3

- **Dependent** (found by the model): the input voltage $V_i$ and the output current $I_o$.
- **Independent** (imposed from outside): the input current $I_i$ and the output voltage $V_o$.

That choice is written first as a pair of unspecified functions ·L6 p3

$$V_i = f_1(I_i,\,V_o)$$

$$I_o = f_2(I_i,\,V_o)$$

and then, for small signals, linearised into two simultaneous equations. ·L6 p3

[eq: two-port-h-equations] **The two hybrid defining equations**, in numeric subscripts ·L6 p3

$$\boxed{\;V_i = h_{11}I_i + h_{12}V_o\;}$$

$$\boxed{\;I_o = h_{21}I_i + h_{22}V_o\;}$$

and, in the alphabetic subscripts used for the rest of the lesson, ·L6 p3–p4

$$\boxed{\;V_i = h_i I_i + h_r V_o\;}$$

$$\boxed{\;I_o = h_f I_i + h_o V_o\;}$$

- $h_i = h_{11}$ — input resistance, in ohms
- $h_r = h_{12}$ — reverse voltage transfer ratio, dimensionless
- $h_f = h_{21}$ — forward current gain, dimensionless
- $h_o = h_{22}$ — output admittance, in siemens (the notes write mho and µA/V)

> [added] **Why "hybrid".** Look at the units of the four coefficients: $\Omega$, none, none, S. They
> are of *mixed* dimension — that mixture is what the word hybrid refers to, and it is the fastest
> check available on any h-parameter expression. Every term in the first equation must come out in
> volts; every term in the second must come out in amperes. Two of the four flags in this file were
> found by that check alone.

---

## 6.2 The four h-parameters, defined ·L6 p4

Each parameter is a ratio taken with **one of the two independent variables forced to zero**. Forcing
$V_o = 0$ means **short-circuiting the output** to signals; forcing $I_i = 0$ means **open-circuiting
the input**. ·L6 p4

[eq: h-i-def] **Input resistance with the output short-circuited** ·L6 p4

$$\boxed{\;h_{11} = h_i = \left.\frac{V_i}{I_i}\right|_{V_o=0}\;}\qquad [\Omega]$$

[eq: h-r-def] **Reverse voltage transfer ratio with the input open-circuited** ·L6 p4

$$\boxed{\;h_{12} = h_r = \left.\frac{V_i}{V_o}\right|_{I_i=0}\;}\qquad\text{[dimensionless]}$$

> ⚠ VERIFY **V6.1** ·L6 p4 — printed as
> $$h_{12} = h_r = \left.\frac{V_i}{I_o}\right|_{I_i=0}$$
> with **$I_o$** in the denominator, where **$V_o$** is meant. Three independent checks:
> **(i) dimensions** — $V_i/I_o$ is in ohms, but $h_r$ must be dimensionless, because in
> $V_i = h_iI_i + h_rV_o$ the term $h_rV_o$ has to be a voltage. **(ii) the constraint** — the
> condition written alongside it is $I_i = 0$, i.e. the *input* open; a ratio taken to $I_o$ would be
> constrained at the output, not the input. **(iii) the page's own words** — it is called a
> *voltage* transfer ratio, and $V_i/I_o$ is not a ratio of two voltages. Correct form:
> $$\boxed{\;h_r = \left.\frac{V_i}{V_o}\right|_{I_i=0}\;}$$
> The page's other three definitions are all correct, so this is an isolated slip of one subscript.
> See `_verification-log.md`.

[eq: h-f-def] **Short-circuit forward current gain, output short-circuited** ·L6 p4

$$\boxed{\;h_{21} = h_f = \left.\frac{I_o}{I_i}\right|_{V_o=0}\;}\qquad\text{[dimensionless]}$$

> ⚠ VERIFY **C6.1** ·L6 p4 — the phrase on this line was written *"short circuit current gain"* and
> the word **"Forward"** then inserted above the line with a caret, giving *"short circuit forward
> current gain"*. Nothing computed changes; noted only because the inserted word sits above the line
> and is easy to miss when copying. See `_verification-log.md`.

[eq: h-o-def] **Output admittance with the input open-circuited** ·L6 p4

$$\boxed{\;h_{22} = h_o = \left.\frac{I_o}{V_o}\right|_{I_i=0}\;}\qquad [\mathrm{S}]$$

> [added] **A one-line way to remember which condition goes with which parameter.** The two
> parameters on the *left* of each defining equation's right-hand side ($h_i$, $h_f$) both multiply
> $I_i$, so they are measured with the *other* independent variable killed: $V_o = 0$, output
> shorted. The two that multiply $V_o$ ($h_r$, $h_o$) are measured with $I_i = 0$, input open.

---

## 6.3 The hybrid equivalent circuit ·L6 p5

[def] Reading the two defining equations as Kirchhoff statements gives the **hybrid model**: the
first equation is a KVL loop at the input, the second a KCL node at the output. ·L6 p5

[fig ·L6 p5] **The generic hybrid equivalent circuit.** Draw it as two disconnected halves sharing a
common bottom rail.

**Input half (a series loop).** From the **+** input terminal at top left, a resistor drawn as a
zigzag, labelled $h_i$, with the current arrow $I_i$ entering it from the left. Out of the resistor
the wire drops vertically into a **circle — a dependent *voltage* source** labelled $h_rV_o$, drawn
with **+ at its top and − at its bottom**. Below the source the wire meets the bottom rail, which
runs back left to the **−** input terminal.

**Output half (a parallel node).** A top rail runs from a node on the left across to the **+** output
terminal on the right, with an arrow labelled $I_o$ pointing **left** (into the node). Hanging from
that rail, in order left to right: a **circle — a dependent *current* source** labelled $h_fI_i$,
with **its internal arrow pointing downward**; then a zigzag element labelled $h_o$; then, at the far
right, a vertical arrow pointing **up** labelled $V_o$, whose head is at the **+** terminal. All
three hang onto the same bottom rail.

> ⚠ VERIFY **C6.2** ·L6 p5, p6, p7, p8 — the output element is drawn as a **resistor zigzag** but
> labelled **$h_o$** (or $h_{oe}$, $h_{ob}$, $h_{oc}$), which is an *admittance* in siemens. As drawn
> the label is the element's admittance, not its resistance; the resistance of that branch is
> $1/h_o$. ·L6 p16 draws the same element and labels it **$1/h_{oe}$**, which is the consistent
> form. Nothing computed changes — every formula in the lesson uses $h_o$ as an admittance
> throughout — but a reader redrawing the figure should write $1/h_o$ beside the zigzag.
> See `_verification-log.md`.

> [added] **The two sources are of different kinds, and that is the whole model.** The input carries
> a **voltage** source $h_rV_o$ in series (it adds a voltage to the input loop, representing the
> feedback of the output voltage into the input); the output carries a **current** source $h_fI_i$ in
> parallel (it injects a current at the output node, representing the transistor's amplification).
> Swapping their types is the commonest way to get this figure wrong.

### Advantages of the h-parameter description ·L6 p5

Six reasons the notes give for preferring h-parameters to the other two-port parameter sets: ·L6 p5

1. They are **real numbers at audio frequencies** — no complex arithmetic needed in this course.
2. They are **easy to measure**.
3. They **can be obtained from the transistor's static characteristic curves** (the input, output and
   transfer families of Lesson 3).
4. They are **convenient to use in circuit analysis and design**.
5. They are **easily converted from one configuration to another** — the conversion formulae are in
   §6.15.
6. **Most transistor manufacturers specify the h-parameters** on the data sheet.

---

## 6.4 The CE h-parameter model ·L6 p5–p6

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_b$, $i_b$ | base (input) current | A | 10–100 µA |
| $V_b$, $v_b$ | base–emitter (input) voltage | V | 1–20 mV signal |
| $I_c$, $i_c$ | collector (output) current | A | 0.5–5 mA |
| $V_c$, $v_c$ | collector–emitter (output) voltage | V | 0.1–2 V signal |
| $h_{ie}$ | CE input resistance, output shorted | $\Omega$ | 1100 $\Omega$ |
| $h_{re}$ | CE reverse voltage transfer ratio | — | $2.5\times10^{-4}$ |
| $h_{fe}$ | CE forward current gain | — | 50 |
| $h_{oe}$ | CE output admittance | S | 25 µA/V |
| $R_C$ | collector load resistor | $\Omega$ | 1–10 k$\Omega$ |
| $V_{CC}$ | collector supply | V | 5–20 V |

[fig ·L6 p5] **Simple common-emitter configuration** (the physical circuit, not the model). An NPN
transistor drawn with the base **B** at the left, the emitter **E** dropping to the bottom rail, and
the collector **C** rising from the top. The input source is on the left: a **+** terminal at top
left with the current arrow $I_b$ pointing right into the base, and the port voltage $V_b$ drawn as a
downward arrow from that terminal to the bottom rail. Across the top, an arrow labelled $I_c$ points
**left** into the collector. From the collector node a vertical arrow labelled $V_c$ points down to
the bottom rail. To the right of that, a resistor $R_C$ runs from the collector rail down to a
battery $V_{CC}$ drawn with **+ uppermost and − below**, whose negative plate sits on the bottom
rail.

The four terminal variables $I_b$, $I_c$, $V_b$ and $V_c$ **represent total instantaneous currents
and voltages**. ·L6 p5

- $I_b$ — input current; $V_b$ — input voltage. ·L6 p6
- $I_c$ — output current; $V_c$ — output voltage. ·L6 p6

[fig ·L6 p6] **The CE hybrid model.** Identical in topology to the generic figure of §6.3, with the
terminals named:

- Top left terminal marked **B** and **+**; bottom left marked **E** and **−**; the port voltage
  $V_b$ drawn as a downward arrow between them.
- Series input resistor labelled **$h_{ie}$**, with $I_b$ arrowed rightward through it.
- Dependent **voltage** source $h_{re}V_c$ in a circle, **+ at top, − at bottom**, closing the input
  loop to the bottom rail.
- Output: arrow $I_c$ pointing **left** along the top rail into node **C**; dependent **current**
  source $h_{fe}I_b$ in a circle with its **arrow pointing down**; a zigzag labelled **$h_{oe}$** in
  parallel; and $V_c$ as an upward arrow at the far right with its head at **C**. The bottom right
  terminal is marked **E**.

[eq: ce-h-equations] **The CE defining equations** ·L6 p6

$$\boxed{\;V_b = h_{ie}I_b + h_{re}V_c\;}$$

$$\boxed{\;I_c = h_{fe}I_b + h_{oe}V_c\;}$$

[def] The four CE parameters as partial derivatives about the Q-point, with the small-signal ratio
alongside each ·L6 p6

$$h_{ie} = \left.\frac{\Delta V_B}{\Delta I_B}\right|_{V_C\,=\,\text{const}} = \left.\frac{v_b}{i_b}\right|_{V_C\,=\,\text{const}}$$

$$h_{re} = \left.\frac{\Delta V_B}{\Delta V_C}\right|_{I_B\,=\,\text{const}} = \left.\frac{v_b}{v_c}\right|_{i_b\,=\,\text{const}}$$

$$h_{fe} = \left.\frac{\Delta I_C}{\Delta I_B}\right|_{V_C\,=\,\text{const}} = \left.\frac{i_c}{i_b}\right|_{V_C\,=\,\text{const}}$$

$$h_{oe} = \left.\frac{\Delta I_C}{\Delta V_C}\right|_{I_B\,=\,\text{const}} = \left.\frac{i_c}{v_c}\right|_{i_b\,=\,\text{const}}$$

> [added] **"Held constant" and "shorted" are the same instruction.** A dc quantity held constant has
> zero *signal* component, so $V_C$ constant means $v_c = 0$ — the output is an ac short. That is why
> §6.2's definitions say "output short-circuited" and this page says "$V_C$ = constant": same
> condition, two vocabularies.

> [added] **$h_{fe}$ is $\beta_{ac}$.** The ratio $i_c/i_b$ at constant $V_{CE}$ is exactly the
> small-signal current gain defined in Lesson 3. Likewise $h_{fb} = -\alpha_{ac}$ — the sign coming
> from the sign convention of §6.1, not from any new physics.

---

## 6.5 Hybrid models for all three configurations ·L6 p7

·L6 p7 is a **landscape page, rotated 90° in the PDF**. It is laid out as a three-row, three-column
table: the transistor symbol circuit on the left, its hybrid model in the middle, and the pair of
defining equations on the right. One row each for CE, CB and CC.

[fig ·L6 p7] **Column 1 — the symbol circuits.** All three are drawn as a rectangular loop with the
transistor inside, the input port on the left of the loop and the output port on the right.

- **CE row.** Base at the left with $i_b$ arrowed into it and $v_b$ measured downward at the input
  port; collector at the top with $i_c$ arrowed **left** along the top rail and $v_c$ measured
  downward at the output port; emitter to the common bottom rail. Output terminal marked **C**, and
  the bottom rail terminals marked **E**.
- **CB row.** Emitter at the left with $i_e$ arrowed **up** into it and $v_e$ at the input port;
  collector at the top with $i_c$ and $v_c$ at the output port; base on the common rail, the
  bottom-right terminal marked **B**.
- **CC row.** Base at the left with $i_b$ arrowed into it and $v_b$ at the input port; emitter at the
  right with $i_e$ arrowed and $v_e$ at the output port, the terminal marked **E**; collector on the
  common rail with $i_c$ across the top, the bottom-left terminal marked **C**.

[fig ·L6 p7] **Column 2 — the hybrid models.** All three have the identical topology of §6.3, and in
all three the **dependent current source's internal arrow points downward** and the output shunt
element is drawn as a **zigzag**. Only the labels change:

| Row | Series input resistor | Series voltage source (+ on top) | Shunt current source (arrow down) | Shunt output element |
|---|---|---|---|---|
| CE | $h_{ie}$ | $h_{re}v_c$ | $h_{fe}i_b$ | $h_{oe}$ |
| CB | $h_{ib}$ | $h_{rb}v_c$ | $h_{fb}i_e$ | $h_{ob}$ |
| CC | $h_{ic}$ | $h_{rc}v_e$ | $h_{fc}i_b$ | $h_{oc}$ |

The port labels change with the row: CE runs B → C with E common; CB runs E → C with B common;
CC runs B → E with C common.

[eq: ce-h-equations] **CE** ·L6 p7

$$v_b = h_{ie}i_b + h_{re}v_c \qquad\qquad i_c = h_{fe}i_b + h_{oe}v_c$$

[eq: cb-h-equations] **CB** ·L6 p7

$$v_e = h_{ib}i_e + h_{rb}v_c \qquad\qquad i_c = h_{fb}i_e + h_{ob}v_c$$

[eq: cc-h-equations] **CC** ·L6 p7

$$v_b = h_{ic}i_b + h_{rc}v_e \qquad\qquad i_e = h_{fc}i_b + h_{oc}v_e$$

> ⚠ VERIFY **V6.2** ·L6 p7 — the **output** equations of the **CE** and **CB** rows are both printed
> with $i_c$ as the last factor instead of $v_c$:
> $$i_c = h_{fe}i_b + h_{oe}\,i_c \qquad\text{(CE row, as printed)}$$
> $$i_c = h_{fb}i_e + h_{ob}\,i_c \qquad\text{(CB row, as printed)}$$
> The CC row on the same page is written correctly, with $v_e$. Three checks: **(i) dimensions** —
> $h_{oe}$ is in siemens, so $h_{oe}i_c$ has units $\mathrm{A^2/V}$, which cannot be added to a
> current. **(ii) self-reference** — the symbol on the left of the equals sign reappears on the
> right, which by itself makes the equation either trivial or inconsistent. **(iii) the model** —
> $h_o$ is the *output* branch's admittance and sits directly across the output port, so the current
> it carries is $h_o\times$(the port **voltage**). Correct forms:
> $$\boxed{\;i_c = h_{fe}i_b + h_{oe}v_c\;}\qquad\boxed{\;i_c = h_{fb}i_e + h_{ob}v_c\;}$$
> The same equations are printed correctly on ·L6 p6 (CE) and used correctly throughout ·L6 p9–p13,
> so this is a transcription slip confined to p7. See `_verification-log.md`.

> [added] **Note the CB input variable.** The CB row's input current is $i_e$, not $i_b$ — in a
> common-base stage the *emitter* is the input terminal. That is why $h_{fb}$ multiplies $i_e$ and
> why $h_{fb} \approx -\alpha$ rather than $\beta$.

---

## 6.6 Typical h-parameter values ·L6 p8

[table] **Typical h-parameter values for a transistor** ·L6 p8

| Parameter | CE | CC | CB |
|---|---|---|---|
| $h_i$ | 1100 $\Omega$ | 1100 $\Omega$ | 22 $\Omega$ |
| $h_r$ | $2.5\times10^{-4}$ | $1$ | $3\times10^{-4}$ |
| $h_f$ | $50$ | $-51$ | $-0.98$ |
| $h_o$ | 25 µA/V | 25 µA/V | 0.49 µA/V |

> [added] **This table is internally consistent — verified.** Applying the conversion formulae of
> §6.15 to the CE column reproduces the other two columns:
>
> | Converted from CE | Value computed | Table |
> |---|---|---|
> | $h_{ib} = h_{ie}/(1+h_{fe}) = 1100/51$ | $21.57\ \Omega$ | 22 $\Omega$ |
> | $h_{rb} = h_{ie}h_{oe}/(1+h_{fe}) - h_{re} = 0.0275/51 - 2.5\times10^{-4}$ | $2.892\times10^{-4}$ | $3\times10^{-4}$ |
> | $h_{fb} = -h_{fe}/(1+h_{fe}) = -50/51$ | $-0.9804$ | $-0.98$ |
> | $h_{ob} = h_{oe}/(1+h_{fe}) = 25/51$ µA/V | $0.4902$ µA/V | 0.49 µA/V |
> | $h_{ic} = h_{ie}$ | $1100\ \Omega$ | 1100 $\Omega$ |
> | $h_{rc} = 1$ | $1$ | $1$ |
> | $h_{fc} = -(1+h_{fe})$ | $-51$ | $-51$ |
> | $h_{oc} = h_{oe}$ | 25 µA/V | 25 µA/V |
>
> Every entry agrees to the printed precision. The table is one consistent transistor, not four
> unrelated numbers, and it is worth memorising as a sanity reference: **$h_i$ falls by a factor
> $\approx\beta$ going CE → CB, $h_o$ falls by the same factor, $h_f$ changes sign, and CC is CE with
> $h_r = 1$ and $h_f$ negated and bumped by one.**

> [added] **Orders of magnitude worth carrying.** $h_i$ is **kilohms** (CE, CC) or **tens of ohms**
> (CB). $h_r$ is **a few parts in ten thousand** — small enough that dropping it is the whole basis
> of the approximate model in §6.18. $h_f$ is **tens** (CE), **about $-1$** (CB), **minus tens**
> (CC). $h_o$ is **tens of microsiemens**, i.e. a shunt resistance $1/h_{oe} = 40\ \mathrm{k}\Omega$.

---

## 6.7 The loaded amplifier: what is actually being solved ·L6 p8

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_s$ | signal-source open-circuit voltage | V | mV |
| $R_s$ | signal-source internal resistance | $\Omega$ | 0.5–3 k$\Omega$ |
| $Z_L$, $R_L$ | load impedance / load resistance | $\Omega$ | 1–10 k$\Omega$ |
| $Y_L = 1/Z_L$ | load admittance | S | 0.1–1 mS |
| $I_L$ | current delivered to the load | A | mA |
| $Z_i$, $R_i$ | amplifier input impedance, looking into 1–1′ | $\Omega$ | 22 $\Omega$–144 k$\Omega$ |
| $Y_o$, $R_o$ | amplifier output admittance / resistance at 2–2′ | S, $\Omega$ | µS, tens of k$\Omega$ |
| $A_I$ | current gain $I_L/I_1$ | — | 0.98–50 |
| $A_V$ | voltage gain $V_2/V_1$ | — | 1–130 |
| $A_{VS}$ | overall voltage gain $V_2/V_s$ | — | — |
| $A_{IS}$ | overall current gain $-I_2/I_s$ | — | — |
| $A_P$ | power gain $A_VA_I$ | — | 47–6100 |

[def] A transistor amplifier is made by **connecting an external load and a signal source to the
two-port, and biasing the transistor properly**. ·L6 p8

[fig ·L6 p8, upper] **The loaded two-port.** On the left, a circle source labelled $V_s$ with **+
above and − below**, in series with a resistor $R_s$ running right to terminal **1**. Below it,
terminal **1′** on the return wire. Between 1 and 1′ a downward arrow labelled $V_1$; an arrow
labelled $I_1$ points **right, into terminal 1**. A hooked arrow under the input pair points into the
box and is labelled $Z_i$. The box is captioned **"Two port active network (transistor)"**. On the
right, terminals **2** and **2′**, with an arrow labelled $I_2$ pointing **left into terminal 2**, a
downward arrow $V_2$ between 2 and 2′, and the load $Z_L$ as a vertical zigzag on the far right with
its own current $I_L$ arrowed **downward** through it. A hooked arrow above 2′ points back into the
network and is labelled $Y_o$.

[fig ·L6 p8, lower] **"Transistor hybrid parameter model"** — the same circuit with the box replaced
by the hybrid model of §6.3. Left to right: $V_s$ (+ above), $R_s$, terminal 1, $I_1$ arrowed right
through the series resistor $h_i$, the dependent voltage source $h_rV_2$ (**+ on top, − below**)
closing to the bottom rail at 1′; then, hanging off the output rail, the dependent current source
$h_fI_1$ (**arrow down**), the shunt element $h_o$, the port voltage $V_2$ at terminal 2, and the
load $Z_L$ carrying $I_L$ downward. $I_2$ is arrowed **left into terminal 2**.

> [added] **The one relation that drives every derivation on the next four pages.** The load ties the
> two port variables together:
> $$V_2 = I_LZ_L = -I_2Z_L$$
> The minus sign is forced by the arrow directions in the figure: $I_2$ points *into* the port and
> $I_L$ points *out* of it, so $I_L = -I_2$. Every substitution in §6.8–§6.11 is this equation being
> used once.

---

## 6.8 Current gain $A_I$ ·L6 p9

[def] For a transistor amplifier the **current gain is the ratio of output current to input
current**. ·L6 p9

$$A_I = \frac{I_L}{I_1} = \frac{-I_2}{I_1}$$

[derivation] ·L6 p9

From the model, the output equation is

$$I_2 = h_fI_1 + h_oV_2 \tag{1}$$

and from the load,

$$V_2 = I_LZ_L = -I_2Z_L \tag{2}$$

Substituting (2) in (1),

$$I_2 = h_fI_1 - I_2Z_Lh_o$$

$$I_2 + I_2Z_Lh_o = h_fI_1$$

$$I_2\left(1 + Z_Lh_o\right) = h_fI_1 \quad\Longrightarrow\quad \frac{I_2}{I_1} = \frac{h_f}{1+Z_Lh_o}$$

[eq: current-gain-ai] **Current gain of the loaded amplifier** ·L6 p9

$$\boxed{\;A_I = \frac{-I_2}{I_1} = \frac{-h_f}{1 + Z_Lh_o}\;}$$

[table] **Written out per configuration** ·L6 p9

| | CE | CB | CC |
|---|---|---|---|
| $A_I$ | $\dfrac{-h_{fe}}{1+Z_Lh_{oe}}$ | $\dfrac{-h_{fb}}{1+Z_Lh_{ob}}$ | $\dfrac{-h_{fc}}{1+Z_Lh_{oc}}$ |

> [added] **Read the signs off the typical values.** CE: $h_{fe} = +50$, so $A_I \approx -50$ —
> **current inversion**. CB: $h_{fb} = -0.98$, so $A_I \approx +0.98$ — no inversion, gain below one.
> CC: $h_{fc} = -51$, so $A_I \approx +51$ — no inversion, gain slightly above $\beta$. The sign of
> $A_I$ is entirely the sign of $-h_f$; the denominator $1+Z_Lh_o$ is always a little over unity and
> only ever *reduces* the magnitude.

> ⚠ VERIFY **C6.3** ·L6 p9 — the heading is written *"Current Gain (or) Current Amplification
> $A_i$"* with a **lower-case italic subscript**, while every equation on the page and the eighteen
> pages that follow use **$A_I$**. Nothing computed changes. See `_verification-log.md`.

---

## 6.9 Input impedance $Z_i$ ·L6 p9–p10

[def] $R_s$ is the signal-source resistance; **the impedance seen looking into the amplifier
terminals 1–1′ is the amplifier input impedance $Z_i$**. ·L6 p9

$$Z_i = \frac{V_1}{I_1}$$

[derivation] ·L6 p9–p10

From the model's input equation, $V_1 = h_iI_1 + h_rV_2$, so

$$Z_i = \frac{h_iI_1 + h_rV_2}{I_1} = h_i + h_r\frac{V_2}{I_1} \tag{1}$$

The load relation, rewritten using $A_I = -I_2/I_1$, gives

$$V_2 = -I_2Z_L = A_II_1Z_L$$

Substituting into (1),

$$Z_i = h_i + h_r\frac{A_II_1Z_L}{I_1}$$

$$Z_i = h_i + h_rA_IZ_L$$

Now substituting $A_I = -h_f/(1+h_oZ_L)$,

$$Z_i = h_i - h_rZ_L\frac{h_f}{1+h_oZ_L}$$

Dividing numerator and denominator of the fraction by $Z_L$,

$$Z_i = h_i - \frac{h_fh_r}{\dfrac{1}{Z_L} + h_o}$$

[eq: input-impedance-zi] **Input impedance of the loaded amplifier**, with $Y_L = 1/Z_L$ ·L6 p10

$$\boxed{\;Z_i = h_i - \frac{h_fh_r}{Y_L + h_o}\;}$$

[table] **Written out per configuration** ·L6 p10

| | CE | CB | CC |
|---|---|---|---|
| $Z_i$ | $h_{ie} - \dfrac{h_{fe}h_{re}}{Y_L+h_{oe}}$ | $h_{ib} - \dfrac{h_{fb}h_{rb}}{Y_L+h_{ob}}$ | $h_{ic} - \dfrac{h_{fc}h_{rc}}{Y_L+h_{oc}}$ |

> ⚠ VERIFY **V6.3** ·L6 p10 — the **CC** entry of this table is printed with the leading term
> **$h_{ie}$**, a common-emitter parameter, inside an otherwise all-CC expression:
> $$Z_i\big|_{CC} = h_{ie} - \frac{h_{fc}h_{rc}}{Y_L+h_{oc}} \qquad\text{(as printed)}$$
> All four parameters in a configuration's formula must carry the same second subscript, and the
> general result of this same page is $Z_i = h_i - h_fh_r/(Y_L+h_o)$ with a single parameter set.
> Correct form:
> $$\boxed{\;Z_i\big|_{CC} = h_{ic} - \frac{h_{fc}h_{rc}}{Y_L + h_{oc}}\;}$$
> **In this instance the numbers happen not to move**, because $h_{ic} = h_{ie}$ exactly (§6.15) —
> but the expression as written is still wrong, and the same slip in a CB row would change the answer
> by a factor of about $\beta$. ·L6 p13 prints the CC result correctly with $h_{ic}$, so the two
> pages disagree. See `_verification-log.md`.

> [added] **Why the load appears in the input impedance at all.** It enters only through $h_r$: the
> output voltage feeds back into the input loop through the $h_rV_2$ source. Set $h_r = 0$ and
> $Z_i = h_i$ exactly, independent of the load — which is precisely the approximation §6.18 makes.

---

## 6.10 Voltage gain $A_V$ ·L6 p10

[def] The **ratio of output voltage $V_2$ to input voltage $V_1$** gives the voltage gain. ·L6 p10

$$A_V = \frac{V_2}{V_1}$$

[derivation] Substituting $V_2 = -I_2Z_L = A_II_1Z_L$, ·L6 p10

$$A_V = \frac{A_II_1Z_L}{V_1} = \frac{A_IZ_L}{V_1/I_1} = \frac{A_IZ_L}{Z_i}$$

[eq: voltage-gain-av] **Voltage gain of the loaded amplifier** ·L6 p10

$$\boxed{\;A_V = \frac{A_I\,Z_L}{Z_i}\;}$$

The same expression serves all three configurations — CE, CB and CC — because the configuration
dependence is already inside $A_I$ and $Z_i$. ·L6 p10

> [added] **Dimensional check.** $A_I$ is dimensionless, $Z_L/Z_i$ is a ratio of ohms to ohms, so
> $A_V$ is dimensionless. Good. And the physical reading is worth holding: **voltage gain is current
> gain multiplied by the impedance transformation ratio.** A CB stage has $A_I<1$ but $Z_L/Z_i$ of
> order $10^2$, which is exactly why its voltage gain is large.

[eq: power-gain-ap] **Power gain** — used in the comparison table of §6.17 though not derived
separately ·L6 p15

$$\boxed{\;A_P = A_V\,A_I\;}$$

---

## 6.11 Output admittance $Y_o$ ·L6 p11

[def] The output admittance is measured **with the signal source killed and the load removed**: ·L6 p11

$$Y_o = \frac{I_2}{V_2}\qquad\text{with } V_s = 0 \text{ and } R_L = \infty$$

[derivation] ·L6 p11

From the model's output equation,

$$I_2 = h_fI_1 + h_oV_2$$

Dividing throughout by $V_2$,

$$\frac{I_2}{V_2} = h_f\frac{I_1}{V_2} + h_o \tag{1}$$

With $V_s = 0$, KVL around the input loop — source resistance, then $h_i$, then the dependent voltage
source — gives

$$R_sI_1 + h_iI_1 + h_rV_2 = 0$$

$$I_1\left(R_s + h_i\right) + h_rV_2 = 0$$

Hence

$$\frac{I_1}{V_2} = \frac{-h_r}{R_s + h_i}$$

Substituting back into (1),

$$\frac{I_2}{V_2} = \frac{-h_fh_r}{R_s+h_i} + h_o$$

[eq: output-admittance-yo] **Output admittance of the loaded amplifier** ·L6 p11

$$\boxed{\;Y_o = h_o - \frac{h_fh_r}{R_s + h_i}\;}\qquad\qquad R_o = \frac{1}{Y_o}$$

[table] **Written out per configuration** ·L6 p11

| | CE | CB | CC |
|---|---|---|---|
| $Y_o$ | $h_{oe} - \dfrac{h_{fe}h_{re}}{R_s+h_{ie}}$ | $h_{ob} - \dfrac{h_{fb}h_{rb}}{R_s+h_{ib}}$ | $h_{oc} - \dfrac{h_{fc}h_{rc}}{R_s+h_{ic}}$ |

All three rows here are correctly subscripted, unlike the $Z_i$ table of ·L6 p10 (flag **V6.3**).

> [added] **$Y_o$ depends on $R_s$; $Z_i$ depends on $Z_L$.** That symmetry is worth naming: the two
> ports of a two-port with $h_r\neq0$ are not independent. Only when $h_r$ is dropped does $Z_i$ stop
> caring about the load and $Y_o$ stop caring about the source (at which point $Y_o \to h_o$, and in
> the fully approximate model $R_o\to\infty$; see §6.18).

> ⚠ VERIFY **C6.4** ·L6 p11 — the condition is written **"$R_L=\infty$"** on a page whose every
> other symbol for the load is $Z_L$; the same mixing recurs on ·L6 p12, where $A_{VS}$ is written
> with $R_L$ in the numerator two lines after $A_V$ was written with $Z_L$. The lesson treats
> $Z_L = R_L$ throughout (·L6 p12 states this explicitly in a bracket), so nothing computed changes.
> See `_verification-log.md`.

---

## 6.12 Voltage gain referred to the source, $A_{VS}$ ·L6 p11–p12

[def] $A_V$ is measured from the amplifier's *own* input terminals. The gain a user actually sees is
measured from the source's open-circuit voltage $V_s$, and is smaller because $R_s$ and $Z_i$ divide
the signal. ·L6 p11

$$A_{VS} = \frac{V_2}{V_s} = \frac{V_2}{V_1}\cdot\frac{V_1}{V_s} \quad\Longrightarrow\quad A_{VS} = A_V\frac{V_1}{V_s}$$

[fig ·L6 p11] A small auxiliary circuit: a circle source $V_s$ in series with a resistor $R_s$ across
a second resistor drawn as a vertical zigzag labelled $Z_i$, with $V_1$ measured across $Z_i$. It is
a plain potential divider.

[derivation] From the divider ·L6 p11

$$V_1 = \frac{V_sZ_i}{R_s+Z_i} \quad\Longrightarrow\quad \frac{V_1}{V_s} = \frac{Z_i}{R_s+Z_i}$$

[eq: voltage-gain-source-avs] **Overall voltage gain** ·L6 p11–p12

$$\boxed{\;A_{VS} = \frac{A_V\,Z_i}{R_s + Z_i}\;}$$

and substituting $A_V = A_IR_L/Z_i$, the $Z_i$ cancels: ·L6 p12

$$A_{VS} = \frac{A_IR_L}{Z_i}\times\frac{Z_i}{R_s+Z_i} = \boxed{\;\frac{A_I\,R_L}{R_s + Z_i}\;}$$

**Limiting case.** If $R_s = 0$ then ·L6 p12

$$A_{VS} = \frac{A_IR_L}{Z_i} = A_V$$

— an ideal voltage source sees the amplifier's own gain, as it must.

---

## 6.13 Current gain referred to the source, $A_{IS}$ ·L6 p12

[def] The same idea applied to a **current** source drive. ·L6 p12

$$A_{IS} = \frac{-I_2}{I_s} = \frac{-I_2}{I_1}\cdot\frac{I_1}{I_s} = A_I\frac{I_1}{I_s}$$

[fig ·L6 p12] **The modified input circuit, using Norton's equivalent for the source.** A circle
current source labelled $I_s$ with its **arrow pointing up**, in parallel with a vertical zigzag
$R_s$, in parallel with a second vertical zigzag $Z_i$. The top rail carries an arrow labelled $I_1$
pointing **right**, into the $Z_i$ branch; $V_1$ is measured at the right-hand side.

[derivation] [added] The notes state the result without the intermediate step; it is a plain current
divider between the two parallel branches $R_s$ and $Z_i$:

$$I_1 = I_s\frac{R_s}{R_s + Z_i}$$

[eq: current-gain-source-ais] **Overall current gain** ·L6 p12

$$\boxed{\;A_{IS} = \frac{A_I\,R_s}{R_s + Z_i}\;}$$

[eq: avs-from-ais] **And the bridge between the two overall gains** ·L6 p12

$$\boxed{\;A_{VS} = \frac{A_{IS}\,Z_L}{R_s}\;}$$

> [added] **Verified algebraically.** Substituting the two boxed results,
> $$\frac{A_{IS}Z_L}{R_s} = \frac{1}{R_s}\cdot\frac{A_IR_s}{R_s+Z_i}\cdot Z_L = \frac{A_IZ_L}{R_s+Z_i} = A_{VS}$$
> using $Z_L = R_L$. The identity holds exactly. Note also the mirror-image structure: $A_{VS}$ has
> **$Z_i$** in its numerator (voltage divider favours a *large* input impedance), $A_{IS}$ has
> **$R_s$** (current divider favours a *small* input impedance). Which of the two matters is decided
> by whether the driving stage behaves as a voltage or a current source.

---

## 6.14 The four results, written out per configuration ·L6 p12–p13

The notes now collect everything into three blocks. All of it follows from §6.8–§6.11; only the
subscripts change. Throughout, $Z_L = R_L$ and $Y_L = 1/Z_L = 1/R_L$. ·L6 p12

### Common emitter ·L6 p12

$$A_I = \frac{-h_{fe}}{1 + h_{oe}Z_L}$$

$$Z_i = h_{ie} - \frac{h_{fe}h_{re}}{Y_L + h_{oe}}$$

$$A_V = A_I\frac{Z_L}{Z_i}$$

$$Y_o = h_{oe} - \frac{h_{fe}h_{re}}{h_{ie} + R_s}$$

### Common base ·L6 p12

$$A_I = \frac{-h_{fb}}{1 + h_{ob}Z_L}$$

$$Z_i = h_{ib} - \frac{h_{fb}h_{rb}}{Y_L + h_{ob}}$$

$$A_V = A_I\frac{Z_L}{Z_i}$$

$$Y_o = h_{ob} - \frac{h_{fb}h_{rb}}{h_{ib} + R_s}$$

### Common collector ·L6 p13

$$A_I = \frac{-h_{fc}}{1 + h_{oc}Z_L}$$

$$Z_i = h_{ic} - \frac{h_{fc}h_{rc}}{Y_L + h_{oc}}$$

$$A_V = A_I\frac{Z_L}{Z_i}$$

$$Y_o = h_{oc} - \frac{h_{fc}h_{rc}}{h_{ic} + R_s}$$

This CC block is the correctly-subscripted version; the $Z_i$ row of the ·L6 p10 table is not
(flag **V6.3**).

---

## 6.15 Conversion formulae between configurations ·L6 p13

Data sheets quote the **CE** parameters. Everything else is derived from them. ·L6 p13

[eq: conv-cb] **CE → CB** ·L6 p13

$$\boxed{\;h_{ib} = \frac{h_{ie}}{1+h_{fe}}\;}\qquad\boxed{\;h_{rb} = \frac{h_{ie}h_{oe}}{1+h_{fe}} - h_{re}\;}$$

$$\boxed{\;h_{fb} = \frac{-h_{fe}}{1+h_{fe}}\;}\qquad\boxed{\;h_{ob} = \frac{h_{oe}}{1+h_{fe}}\;}$$

[eq: conv-cc] **CE → CC** ·L6 p13

$$\boxed{\;h_{ic} = h_{ie}\;}\qquad\boxed{\;h_{rc} = 1\;}$$

$$\boxed{\;h_{fc} = -(1+h_{fe})\;}\qquad\boxed{\;h_{oc} = h_{oe}\;}$$

> [added] **Reading them.** Three of the four CB formulas are simply "divide by $1+h_{fe}$", i.e.
> divide by $1+\beta$. That is the emitter-to-base current-ratio again: driving the emitter instead
> of the base multiplies the input current by $1+\beta$, so the input resistance and output
> admittance both shrink by that factor. $h_{rc}=1$ says that in an emitter follower essentially all
> of the output voltage appears in the input loop — which is another way of saying $A_V\approx1$.

> [added] **The reverse conversions, which the worked problem on ·L6 p26 needs.** Inverting the two
> that matter:
> $$\boxed{\;h_{fe} = \frac{-h_{fb}}{1+h_{fb}}\;}\qquad\boxed{\;h_{ie} = h_{ib}\left(1+h_{fe}\right)\;}$$
> The notes derive both in the margin of ·L6 p26 rather than listing them here.

---

## 6.16 Characteristics and applications of the three configurations ·L6 p13–p15

### Common emitter ·L6 p13–p14

**Characteristics** ·L6 p13

1. Current gain $A_I$ is high for $R_L < 10\ \mathrm{k}\Omega$.
2. Voltage gain is high for normal values of load resistance $R_L$.
3. The input resistance $R_i$ is **medium**.
4. The output resistance $R_o$ is **moderately high**.

**Applications** ·L6 p14

1. **Of the three configurations, the CE amplifier alone is capable of providing both voltage gain
   and current gain.**
2. Output resistance $R_o$ and input resistance $R_i$ are moderately high.
3. The CE amplifier is **widely used for amplification purposes**.

### Common base ·L6 p14

**Characteristics** ·L6 p14

1. Current gain is **less than unity**, and its magnitude **decreases** as $R_L$ increases.
2. Voltage gain $A_V$ is high for normal values of $R_L$.
3. The input resistance $R_i$ is **the lowest of all three configurations**.
4. The output resistance $R_o$ is **the highest of all three configurations**.

**Applications** — the CB amplifier is **not commonly used for amplification**. It is used for ·L6 p14

1. **matching a very low impedance source**;
2. as a **non-inverting amplifier with voltage gain exceeding unity**;
3. **driving a high impedance load**;
4. as a **constant current source**.

### Common collector ·L6 p14–p15

**Characteristics** ·L6 p14–p15

1. For low $R_L$ ($<10\ \mathrm{k}\Omega$) the current gain $A_I$ is high and **almost equal to that
   of a CE amplifier**.
2. The voltage gain $A_V$ is **less than unity**.
3. The input resistance is **the highest of all three configurations**.
4. The output resistance is **the lowest of all three configurations**.

**Applications** ·L6 p15

1. The CC amplifier is **widely used as a buffer stage between a high-impedance source and a
   low-impedance load**. **The CC amplifier is called the emitter follower.**

> [added] **The three-line summary the exam wants.** CE = the general-purpose amplifier (gain in both
> current and voltage, and the only one that inverts). CB = the impedance *step-up* stage (lowest
> $R_i$, highest $R_o$, voltage gain but no current gain). CC = the impedance *step-down* buffer
> (highest $R_i$, lowest $R_o$, current gain but no voltage gain).

---

## 6.17 The numerical comparison ·L6 p15

The characteristics of the three configurations are collected in one table. The five quantities
$A_I$, $A_V$, $R_i$, $R_o$ and $A_P$ (power gain) are computed **for $R_L = R_s = 3\ \mathrm{k}\Omega$**
using the typical h-parameters of §6.6. ·L6 p15

[table] **Comparison of transistor amplifier configurations, $R_L = R_s = 3\ \mathrm{k}\Omega$** ·L6 p15

| Quantity | CB | CC | CE |
|---|---|---|---|
| $A_I$ | 0.98 | 47.5 | $-46.5$ |
| $A_V$ | 131 | 0.989 | $-131$ |
| $A_P$ | 128.38 | 46.98 | 6091.5 |
| $R_i$ | 22.6 $\Omega$ | 144 k$\Omega$ | 1065 $\Omega$ |
| $R_o$ | 1.72 M$\Omega$ | 80.5 $\Omega$ | 45.5 k$\Omega$ |

> [added] **Recomputed from §6.6's parameters — every entry checks out.** Using
> $h_{ie}=1100\ \Omega$, $h_{re}=2.5\times10^{-4}$, $h_{fe}=50$, $h_{oe}=25\ \mu\mathrm{A/V}$, the
> exactly-converted CB and CC sets, and $R_L=R_s=3\ \mathrm{k}\Omega$, $Y_L=3.333\times10^{-4}\ \mathrm{S}$:
>
> | | CE computed | CE table | CB computed | CB table | CC computed | CC table |
> |---|---|---|---|---|---|---|
> | $A_I$ | $-46.51$ | $-46.5$ | $0.979$ | 0.98 | $47.44$ | 47.5 |
> | $A_V$ | $-131.0$ | $-131$ | $131.0$ | 131 | $0.992$ | 0.989 |
> | $A_P$ | $6093$ | 6091.5 | $128.2$ | 128.38 | $47.08$ | 46.98 |
> | $R_i$ | $1065\ \Omega$ | 1065 $\Omega$ | $22.4\ \Omega$ | 22.6 $\Omega$ | $143.4$ k$\Omega$ | 144 k$\Omega$ |
> | $R_o$ | $45.56$ k$\Omega$ | 45.5 k$\Omega$ | $1.712$ M$\Omega$ | 1.72 M$\Omega$ | $80.2\ \Omega$ | 80.5 $\Omega$ |
>
> Every difference is a rounding artefact — the table's $A_P$ entries are the products of the
> *rounded* $A_V$ and $A_I$ ($-46.5\times-131 = 6091.5$ exactly), and its $R_i$ and $R_o$ come from
> $h_{ib}$ rounded to 22 $\Omega$. **No flag.**

> [added] **What to take away from the table, in one line each.**
> - **$R_i$ spans close to four orders of magnitude** across the three configurations: 22 $\Omega$ → 1 k$\Omega$ → 144 k$\Omega$.
> - **$R_o$ spans more than four**, and in the opposite order: 80 $\Omega$ → 45 k$\Omega$ → 1.7 M$\Omega$.
> - **Only CE has both gains above unity**, and its power gain is therefore roughly 50× the other two.
> - **CE is the only inverting configuration** — both its $A_I$ and its $A_V$ are negative.

---

## 6.18 The simplified (approximate) CE hybrid model ·L6 p16–p19

[def] **Why approximate at all.** The h-parameters **themselves vary widely between samples of the
same transistor type**, so carrying four significant figures through the exact formulas is false
precision. It is therefore justified to make approximations and simplify the expressions for $A_I$,
$A_V$, $A_P$, $R_i$ and $R_o$. ·L6 p16

[fig ·L6 p16] **"Exact CE Hybrid Model"** — the full model with the source attached. From the bottom
left: a circle source $V_s$ with **+ above and − below**, its top going up through a **vertical**
resistor $R_s$ to the input node. From that node, rightward: the current arrow $I_b$ and a horizontal
zigzag $h_{ie}$, then down into the dependent **voltage** source $h_{re}V_c$ (**+ on top, − below**)
onto the bottom rail. Output side, hanging from the top output rail: the dependent **current** source
$h_{fe}I_b$ (**arrow down**); then a zigzag labelled **$1/h_{oe}$**; then a zigzag labelled $R_L$;
then $V_c$ as a vertical double-headed measure at the far right. $I_c$ is arrowed **left** along the
top rail.

Note that here — and only here — the output shunt element is labelled **$1/h_{oe}$**, a resistance,
rather than $h_{oe}$ (see flag **C6.2**).

### Step 1 — dropping $h_{oe}$ ·L6 p16

$1/h_{oe}$ sits **in parallel with $R_L$**. The parallel combination of two unequal impedances is
approximately equal to the **lower** of the two, i.e. $R_L$. Hence ·L6 p16

- **if $1/h_{oe} \gg R_L$, the term $h_{oe}$ may be neglected, provided $h_{oe}R_L \ll 1$.**

With $h_{oe}$ omitted the output node carries only the source, so ·L6 p16

$$I_c = h_{fe}I_b$$

The working criterion used from ·L6 p17 onward is **$h_{oe}R_L < 0.1$**.

> [added] **How restrictive is that?** With $h_{oe} = 25\ \mu\mathrm{A/V}$, $1/h_{oe} = 40\ \mathrm{k}\Omega$,
> and $h_{oe}R_L < 0.1$ means $R_L < 4\ \mathrm{k}\Omega$. That covers most CE stages met in this
> course, and it is exactly the condition under which ·L6 p13 says "$A_I$ is high for
> $R_L<10\ \mathrm{k}\Omega$" starts to soften.

### Step 2 — dropping $h_{re}$ ·L6 p17

Under the same condition, the voltage the dependent source injects into the input loop has magnitude ·L6 p17

$$h_{re}\lvert V_c\rvert = h_{re}I_cR_L = h_{re}h_{fe}I_bR_L$$

Since $h_{re}h_{fe} \approx 0.01$, this voltage may be neglected in comparison with the voltage drop
across $h_{ie}$, namely $h_{ie}I_b$, **provided $R_L$ is not too large**. ·L6 p17

So: **if the load resistance $R_L$ is small, it is possible to neglect both $h_{re}$ and $h_{oe}$**,
and the approximate equivalent circuit follows. ·L6 p17

> [added] **Verified.** With the §6.6 typical values, $h_{re}h_{fe} = 2.5\times10^{-4}\times50 = 0.0125$,
> so the notes' "$\approx0.01$" is right to the stated precision. Comparing the two input-loop terms
> directly: $h_{re}h_{fe}I_bR_L$ against $h_{ie}I_b$ — the ratio is $h_{re}h_{fe}R_L/h_{ie}$, which
> for $R_L = 3\ \mathrm{k}\Omega$ and $h_{ie}=1100\ \Omega$ is $0.0125\times3000/1100 = 0.034$, i.e.
> a 3.4 % correction. That is the whole justification, and it is a genuine one.

[fig ·L6 p17] **"Approximate CE Hybrid Model".** Both the $h_{re}V_c$ source and the $1/h_{oe}$
resistor are gone. What remains, left to right: the circle source $V_s$ (**+ above, − below**) with a
**vertical** $R_s$ above it; the input node with $V_b$ drawn as a downward arrow; a **vertical**
zigzag $h_{ie}$ from that node to the bottom rail; an explicit **ground symbol** on the bottom rail
between the input and output halves; then the dependent **current** source $h_{fe}I_b$ (**arrow
down**); then $R_L$ as a vertical zigzag; then $V_c$ as a downward arrow at the far right. $i_c$ is
arrowed **left** along the top output rail.

### Current gain ·L6 p17

$$A_I = \frac{-h_{fe}}{1 + h_{oe}R_L}\qquad\text{and if } h_{oe}R_L < 0.1,$$

[eq: approx-ce] **Approximate CE current gain** ·L6 p17

$$\boxed{\;A_I = -h_{fe}\;}$$

### Input resistance ·L6 p17–p18

[derivation] The notes do this one properly — they do not simply assert $R_i = h_{ie}$, they bound
the error. ·L6 p18

By exact analysis, $Z_i = R_i = V_1/I_1$ with $V_1 = h_{ie}I_1 + h_{re}V_2$, so

$$Z_i = \frac{h_{ie}I_1 + h_{re}V_2}{I_1} = h_{ie} + h_{re}\frac{V_2}{I_1}$$

With $V_2 = -I_2Z_L = -I_2R_L = A_II_1R_L$,

$$Z_i = h_{ie} + h_{re}\frac{A_II_1R_L}{I_1}$$

$$R_i = h_{ie} + h_{re}A_IR_L$$

$$R_i = h_{ie}\left[1 + \frac{h_{re}A_IR_L}{h_{ie}}\right]$$

Multiplying the bracket's second term above and below by $h_{fe}h_{oe}$,

$$R_i = h_{ie}\left[1 + \frac{h_{re}A_IR_L}{h_{ie}}\times\frac{h_{fe}h_{oe}}{h_{fe}h_{oe}}\right]$$

Using the typical h-parameter values, ·L6 p18

$$\frac{h_{re}h_{fe}}{h_{ie}h_{oe}} \simeq 0.5$$

so the bracket collapses to

$$R_i = h_{ie}\left[1 + \frac{0.5\,A_IR_Lh_{oe}}{h_{fe}}\right]$$

Now substituting $A_I = -h_{fe}$ (valid when $h_{oe}R_L<0.1$),

$$R_i = h_{ie}\left[1 - \frac{0.5\,h_{fe}R_Lh_{oe}}{h_{fe}}\right]$$

[eq: ce-ri-correction] **The first-order input resistance** ·L6 p18

$$\boxed{\;R_i = h_{ie}\left[1 - 0.5\,h_{oe}R_L\right]\;}$$

and if $h_{oe}R_L<0.1$, ·L6 p18

$$\boxed{\;R_i = h_{ie}\;}\qquad(R_i = Z_i)$$

> [added] **Verified.** The constant is $\dfrac{h_{re}h_{fe}}{h_{ie}h_{oe}} = \dfrac{2.5\times10^{-4}\times50}{1100\times25\times10^{-6}} = \dfrac{0.0125}{0.0275} = 0.4545$,
> so "$\simeq0.5$" is right. And the correction term tells you the size of the error you are
> accepting: at the limit $h_{oe}R_L = 0.1$, $R_i = 0.95\,h_{ie}$ — **a 5 % underestimate at worst**.
> That is the reason the criterion is set at 0.1 and not at 1.

### Voltage gain ·L6 p19

$$A_V = A_I\frac{R_L}{R_i} = \boxed{\;\frac{-h_{fe}R_L}{h_{ie}}\;}$$

### Output impedance ·L6 p19

[def] $R_o$ is the ratio of $V_c$ to $I_c$ with $V_s=0$ and $R_L$ excluded. ·L6 p19

**The simplified circuit has infinite output impedance**: with $V_s = 0$ and an external voltage
source applied at the output, it is found that $I_b = 0$, and hence $I_c = 0$. ·L6 p19

$$R_o = \frac{V_c}{I_c} = \infty \qquad (\text{since } I_c = 0)$$

> [added] **Why $I_b$ must be zero here.** In the approximate model the input loop contains only
> $V_s$, $R_s$ and $h_{ie}$ — there is **no path from the output back into the input**, because
> $h_{re}$ was deleted. So driving the output cannot produce any base current, the controlled source
> $h_{fe}I_b$ delivers nothing, and the output node is an ideal current source, i.e. infinite
> impedance. Compare the exact result, $Y_o = h_{oe} - h_{fe}h_{re}/(h_{ie}+R_s)$: dropping both
> $h_{oe}$ and $h_{re}$ sends $Y_o\to0$, so $R_o\to\infty$. **The two routes agree.**

[table] **Approximate analysis of the CE amplifier — the boxed summary** ·L6 p19

| Quantity | Approximate result |
|---|---|
| Current gain | $A_I = -h_{fe}$ |
| Input resistance | $R_i = h_{ie}$ |
| Voltage gain | $A_V = \dfrac{-h_{fe}R_L}{h_{ie}}$ |
| Output resistance | $R_o = \infty$ |

> ⚠ VERIFY **C6.5** ·L6 p17 — the sentence introducing the $h_{re}$ approximation reads *"the
> magnitude of voltage generated in the **emitter** circuit is $h_{re}\lvert V_c\rvert$…"*. The
> $h_{re}V_c$ source sits in the **base (input) loop** of the CE model, not in the emitter lead; the
> emitter is the common terminal and carries no such generator. The algebra that follows is correct
> and unaffected. See `_verification-log.md`.

---

## 6.19 Approximate analysis of the CC amplifier ·L6 p19–p20

[def] **Configuration.** The **collector is grounded**, the **input signal is applied between base
and ground**, and the **load is connected between emitter and ground**. ·L6 p19

[fig ·L6 p19] **"Simplified hybrid model for the CC circuit".** From the bottom left: circle source
$V_s$ (**+ above, − below**) with a **vertical** $R_s$ above it up to the base node. $V_b$ is drawn
as a downward arrow at that node. Rightward along the top: the current arrow $I_b$ and a horizontal
zigzag $h_{ie}$. After the resistor the rail continues right; hanging from it is the dependent
**current** source $h_{fe}I_b$ in a circle with its **arrow pointing UP** — the opposite sense to the
CE and CB figures. Continuing right: $V_e$ as a downward arrow, then $R_L$ as a vertical zigzag on the
far right. Two currents are marked along the top rail: **$I_e$ arrowed left**, and, to its right,
**$I_L = (1+h_{fe})I_b$ arrowed right** into the load branch.

> [added] **The up-arrow is the whole point of the CC model.** In the CE figure the controlled source
> pulls current *down*, away from the load; here it pushes current *up*, into the emitter node, so
> the base current and the source current **add** in the load instead of one being the only
> contributor. That is where the $(1+h_{fe})$ comes from, and it is the difference between a current
> gain of $-h_{fe}$ and one of $+(1+h_{fe})$.

### Current gain ·L6 p20

$$A_I = \frac{I_L}{I_b} = \frac{(1+h_{fe})I_b}{I_b}$$

[eq: approx-cc] **Approximate CC current gain** ·L6 p20

$$\boxed{\;A_I = 1 + h_{fe}\;}$$

### Input resistance ·L6 p20

[derivation] KVL from the base node: the input current crosses $h_{ie}$, then the *load* current
$(1+h_{fe})I_b$ crosses $R_L$. ·L6 p20

$$V_b = I_bh_{ie} + (1+h_{fe})I_bR_L$$

$$R_i = \frac{V_b}{I_b} = \boxed{\;h_{ie} + (1+h_{fe})R_L\;}$$

> [added] **This is the impedance-multiplying property that makes the emitter follower a buffer.**
> The load resistance is seen from the base **multiplied by $1+\beta$**. With $h_{fe}=50$ and
> $R_L=3\ \mathrm{k}\Omega$, $R_i = 1100 + 51\times3000 = 154\ \mathrm{k}\Omega$ — two orders of
> magnitude above the CE input resistance.

### Voltage gain ·L6 p20

[derivation] ·L6 p20

$$A_V = \frac{V_e}{V_b} = \frac{(1+h_{fe})I_bR_L}{\left[h_{ie}I_b + (1+h_{fe})I_bR_L\right]}$$

$$A_V = \frac{(1+h_{fe})R_L}{h_{ie}+(1+h_{fe})R_L} = \frac{h_{ie}+(1+h_{fe})R_L - h_{ie}}{h_{ie}+(1+h_{fe})R_L}$$

$$A_V = 1 - \frac{h_{ie}}{h_{ie}+(1+h_{fe})R_L}$$

and since $R_i = h_{ie}+(1+h_{fe})R_L$,

$$\boxed{\;A_V = 1 - \frac{h_{ie}}{R_i}\;}$$

> [added] **The trick in the middle step is worth naming**, because it recurs: the numerator was
> rewritten as *(denominator) minus $h_{ie}$*, turning a fraction into $1$ minus a small fraction.
> That is what makes it obvious at a glance that $A_V < 1$ but approaches 1 as $R_L$ grows — the
> defining behaviour of a **follower**.

### Output impedance ·L6 p20

[def] The notes take the **Norton route** — short-circuit current over open-circuit voltage. Note
that the quantity being built is an **admittance**: ·L6 p20

$$Y_o = \frac{\text{short-circuit current at the output terminals}}{\text{open-circuit voltage between the output terminals}}$$

**Short-circuit current at the output terminals** — with the output shorted, all of $V_s$ appears
across $R_s + h_{ie}$: ·L6 p20

$$I_{sc} = (1+h_{fe})I_b = (1+h_{fe})\frac{V_s}{R_s+h_{ie}}$$

**Open-circuit voltage between the output terminals** ·L6 p20

$$V_{oc} = V_s$$

Therefore ·L6 p20

$$Y_o = \frac{1+h_{fe}}{R_s + h_{ie}} \quad\Longrightarrow\quad \boxed{\;R_o = \frac{h_{ie}+R_s}{1+h_{fe}}\;}$$

and the output impedance **including the load** is ·L6 p20

$$R_o' = R_o \,\|\, R_L$$

> [added] **Why $V_{oc} = V_s$ exactly.** Open the load and no current flows in $R_L$, so $I_b\to0$
> and there is no drop across $R_s$ — the base sits at $V_s$. With $R_L=\infty$ the voltage gain of
> the follower is $A_V = 1 - h_{ie}/R_i \to 1$, so the emitter follows the base exactly. Hence
> $V_e = V_b = V_s$. Both statements are the same statement.

> ⚠ VERIFY **C6.6** ·L6 p20 — the heading is written *"output impedance $(Y_o)$"*, with the word
> **impedance struck through** and **admittance** written in above it. As left on the page the label
> and the symbol disagree unless the correction is noticed. The quantity computed is the
> **admittance** $Y_o$, in siemens; $R_o = 1/Y_o$ is given on the next line. Nothing computed
> changes. See `_verification-log.md`.

---

## 6.20 Approximate analysis of the CB amplifier ·L6 p21–p22

[def] **Configuration.** The **base is grounded**, the **input signal is applied between emitter and
base**, and the **load is connected between collector and base**. ·L6 p21

[fig ·L6 p21] **"Simplified hybrid model for the CB circuit".** A rectangular loop. Bottom rail is
the grounded base. Left branch: circle source $V_s$ (**+ above, − below**) with a **vertical** $R_s$
above it, rising to the top-left node marked **E**, at which an arrow labelled $I_E$ points **right**
along the top rail. Second branch from the left: a downward arrow $V_E$. Third branch: a **vertical**
zigzag $h_{ie}$ carrying an arrow labelled $I_b$ pointing **UP** through it. Along the top rail, to
the right of $h_{ie}$: the dependent **current** source drawn as a **horizontal ellipse in the rail
itself**, with its internal **arrow pointing LEFT**, labelled $h_{fe}I_b$ beneath it. Right of the
source, an arrow labelled $I_c$ points **left** toward node **C** at the top right. Right-hand
branches: a downward arrow $V_c$, then $R_L$ as a **vertical** zigzag on the far right.

> [added] **Note two things about that figure that are easy to get wrong when redrawing it.** First,
> the CB current source is drawn **in series in the top rail**, not shunted to ground as in the CE
> and CC figures — which is why it directly sets $I_c$. Second, its arrow points **left**, i.e.
> against the marked positive sense of $I_c$; that is what makes $I_c = -h_{fe}I_b$ come out with the
> sign it does in the algebra below.

### Current gain ·L6 p21

[derivation] ·L6 p21

$$A_I = \frac{-I_c}{I_e} = \frac{-h_{fe}I_b}{I_e}$$

From KCL at the transistor, with the marked directions,

$$I_e = -\left(I_b + I_c\right)$$

$$I_e = -\left(I_b + h_{fe}I_b\right) = -\left(1+h_{fe}\right)I_b$$

Therefore

$$A_I = \frac{-h_{fe}I_b}{-(1+h_{fe})I_b} = \frac{h_{fe}}{1+h_{fe}}$$

[eq: approx-cb] **Approximate CB current gain** ·L6 p21

$$\boxed{\;A_I = \frac{h_{fe}}{1+h_{fe}} = -h_{fb}\;}$$

> [added] **Consistent with §6.15**: $h_{fb} = -h_{fe}/(1+h_{fe})$, so $-h_{fb} = h_{fe}/(1+h_{fe})$.
> And numerically, with $h_{fe}=50$, $A_I = 50/51 = 0.980$ — **just under unity, as the CB
> characteristics of §6.16 say it must be.** This is $\alpha$ under another name.

### Input resistance ·L6 p21

$$R_i = \frac{V_e}{I_e}$$

From the figure, ·L6 p21

$$V_e = -I_bh_{ie}\qquad\qquad I_e = -(1+h_{fe})I_b$$

$$\boxed{\;R_i = \frac{h_{ie}}{1+h_{fe}} = h_{ib}\;}$$

> [added] Again consistent with §6.15's conversion formula, and numerically
> $1100/51 = 21.6\ \Omega$ — **the lowest input resistance of the three configurations**, as §6.16
> claims.

### Voltage gain ·L6 p21–p22

$$A_V = \frac{V_c}{V_e},\qquad V_c = -I_cR_L = -h_{fe}I_bR_L,\qquad V_e = -I_bh_{ie}$$

$$\boxed{\;A_V = \frac{h_{fe}R_L}{h_{ie}}\;}$$

> [added] **Positive — the CB stage does not invert.** Compare the CE result of §6.18, which is the
> same magnitude with a minus sign. That single sign is the whole difference between "widely used for
> amplification" and "used as a non-inverting stage", and it is a favourite one-mark exam question.

### Output impedance ·L6 p22

$$R_o = \frac{V_c}{I_c}\qquad\text{with } V_s=0,\ R_L=\infty$$

With $V_s = 0$: $I_e = 0$, and hence $I_b = 0$, and hence $I_c = 0$. Therefore ·L6 p22

$$R_o = \frac{V_c}{0} = \infty$$

[table] **Approximate analysis of the CB amplifier — the boxed summary** ·L6 p22

| Quantity | Approximate result |
|---|---|
| Current gain | $A_I = \dfrac{h_{fe}}{1+h_{fe}} = -h_{fb}$ |
| Input resistance | $R_i = \dfrac{h_{ie}}{1+h_{fe}} = h_{ib}$ |
| Voltage gain | $A_V = \dfrac{h_{fe}R_L}{h_{ie}}$ |
| Output resistance | $R_o = \infty$ |

[table] **Approximate analysis of the CC amplifier — the boxed summary** ·L6 p22

| Quantity | Approximate result |
|---|---|
| Current gain | $A_I = 1+h_{fe}$ |
| Input resistance | $R_i = h_{ie} + (1+h_{fe})R_L$ |
| Voltage gain | $A_V = 1 - \dfrac{h_{ie}}{R_i}$ |
| Output resistance | $R_o = \dfrac{h_{ie}+R_s}{1+h_{fe}}$ |

> [added] **Three boxes, one table — worth memorising as a block.** Note the pattern in $R_o$: **CE
> and CB both give $\infty$** in the approximate model (both have the controlled source facing the
> output with no feedback path), whereas **CC gives a small finite value** $(h_{ie}+R_s)/(1+h_{fe})$
> — because in the follower the source resistance is reflected *down* by $1+\beta$. That is the
> buffering property in one formula.

---

## 6.21 Worked problem 1 — CE amplifier, exact and approximate ·L6 p23–p24

[ex ·L6 p23] **Problem.** A CE amplifier is driven by a voltage source of internal resistance
$R_s = 800\ \Omega$ and the load impedance is a resistance $R_L = 1000\ \Omega$. The h-parameters are

$$h_{ie} = 1\ \mathrm{k}\Omega,\qquad h_{re} = 2\times10^{-4},\qquad h_{fe} = 50,\qquad h_{oe} = 25\ \mu\mathrm{A/V}$$

Compute the current gain $A_I$, input resistance $R_i$, voltage gain $A_V$ and output resistance
$R_o$ **using exact analysis and approximate analysis**.

### Exact analysis ·L6 p23–p24

**Current gain**

$$A_I = \frac{-h_{fe}}{1+h_{oe}R_L} = \frac{-50}{1 + (25\times10^{-6})(1000)} = \frac{-50}{1.025} = -48.78$$

**Input resistance**

$$R_i = h_{ie} - \frac{h_{fe}h_{re}}{h_{oe} + \dfrac{1}{R_L}} = 1000 - \frac{(50)(2\times10^{-4})}{25\times10^{-6} + 1\times10^{-3}}$$

$$R_i = 1000 - \frac{0.01}{1.025\times10^{-3}} = 1000 - 9.756 = 990.24\ \Omega$$

**Voltage gain**

$$A_V = A_I\frac{R_L}{R_i} = (-48.78)\frac{1000}{990.24} = -49.26$$

**Output resistance**

$$Y_o = h_{oe} - \frac{h_{fe}h_{re}}{h_{ie}+R_s} = 25\times10^{-6} - \frac{0.01}{1000+800} = 25\times10^{-6} - 5.556\times10^{-6}$$

$$R_o = \frac{1}{Y_o} = 51.42\ \mathrm{k}\Omega$$

> ⚠ VERIFY **V6.4** ·L6 p23 — the output admittance is printed as
> $$Y_o = 194\times10^{-5}\ \text{mho}$$
> which is $1.94\times10^{-3}\ \mathrm{S}$ — **a factor of 100 too large**. Recomputing from the
> page's own formula and numbers:
> $$Y_o = 25\times10^{-6} - \frac{(50)(2\times10^{-4})}{1800} = 25\times10^{-6} - 5.556\times10^{-6} = 1.944\times10^{-5}\ \mathrm{S}$$
> **The page contradicts itself on the very next line**: it gives $R_o = 1/Y_o = 51.42\ \mathrm{k}\Omega$,
> and $1/(1.94\times10^{-3}) = 515\ \Omega$, not 51.4 k$\Omega$. The value that reproduces the
> printed $R_o$ is $1.944\times10^{-5}$. Correct form:
> $$\boxed{\;Y_o = 1.944\times10^{-5}\ \mathrm{S} = 19.44\ \mu\mathrm{S}\;}$$
> A learner who carried $194\times10^{-5}$ forward into a power calculation would be out by
> $10^4$. See `_verification-log.md`.

> [added] **Every other number in the exact analysis verified.** Recomputed independently:
> $A_I = -48.7805$ (printed $-48.78$); $R_i = 990.244\ \Omega$ (printed 990.24); $A_V = -49.2611$
> (printed $-49.26$); $R_o = 1/(1.9444\times10^{-5}) = 51.429\ \mathrm{k}\Omega$. The printed
> $51.42\ \mathrm{k}\Omega$ is the truncation rather than the rounding of 51.4286 — a difference of
> 0.02 %, not worth a flag, but write **51.43 k$\Omega$** if a mark scheme wants three figures.

### Approximate analysis ·L6 p23–p24

$$A_I = -h_{fe} = -50$$

$$R_i = h_{ie} = 1\ \mathrm{k}\Omega$$

$$A_V = \frac{-h_{fe}R_L}{h_{ie}} = \frac{-50\times1000}{1000} = -50$$

$$R_o = \infty$$

> [added] **How good is the approximation here?** $h_{oe}R_L = 25\times10^{-6}\times1000 = 0.025$,
> comfortably inside the $<0.1$ criterion. The errors that buys:
>
> | Quantity | Exact | Approximate | Error |
> |---|---|---|---|
> | $A_I$ | $-48.78$ | $-50$ | $+2.5\ \%$ |
> | $R_i$ | 990.24 $\Omega$ | 1000 $\Omega$ | $+1.0\ \%$ |
> | $A_V$ | $-49.26$ | $-50$ | $+1.5\ \%$ |
> | $R_o$ | 51.43 k$\Omega$ | $\infty$ | — |
>
> Two points to take from that. **The gains are good to a few per cent** — better than the
> sample-to-sample spread of $h_{fe}$ itself, which is the argument of ·L6 p16. But **$R_o$ is not
> approximated, it is discarded**: the approximate model gives no output-resistance information at
> all, so any question asking for $R_o$ must be done exactly.

---

## 6.22 Worked problem 2 — CC amplifier (emitter follower), exact and approximate ·L6 p24–p25

[ex ·L6 p24] **Problem.** A voltage source of internal resistance $R_s = 900\ \Omega$ drives a CC
amplifier using load resistance $R_L = 2000\ \Omega$. The **CE** h-parameters are

$$h_{ie} = 1200\ \Omega,\qquad h_{re} = 2\times10^{-4},\qquad h_{fe} = 60,\qquad h_{oe} = 25\ \mu\mathrm{A/V}$$

Compute $A_I$, $R_i$, $A_V$ and $R_o$ using exact and approximate analysis.

### Step 0 — convert to CC parameters ·L6 p24

$$h_{ic} = h_{ie} = 1200\ \Omega$$

$$h_{fc} = -(1+h_{fe}) = -(1+60) = -61$$

$$h_{rc} = 1$$

$$h_{oc} = h_{oe} = 25\ \mu\mathrm{A/V}$$

> [added] **This step is the point of the problem.** The data sheet gives CE parameters; the circuit
> is CC. Skipping the conversion and putting $h_{fe}=60$ into the CC formulas would give
> $A_I = -57.1$ instead of $+58.1$ — wrong sign and wrong magnitude.

### Exact analysis ·L6 p24–p25

**Current gain**

$$A_I = \frac{-h_{fc}}{1+h_{oc}R_L} = \frac{61}{1+(25\times10^{-6})(2000)} = \frac{61}{1.05} = 58.095$$

**Input resistance**, with $Y_L = 1/2000 = 5\times10^{-4}\ \mathrm{S}$

$$R_i = h_{ic} - \frac{h_{fc}h_{rc}}{Y_L+h_{oc}} = 1200 - \frac{(-61)(1)}{5\times10^{-4}+25\times10^{-6}}$$

$$R_i = 1200 + \frac{61}{5.25\times10^{-4}} = 1200 + 116\,190.5 = 117.39\ \mathrm{k}\Omega$$

**Voltage gain**

$$A_V = A_I\frac{R_L}{R_i} = \frac{58.095\times2000}{117\,390.5} = 0.9897$$

**Output resistance**

$$Y_o = h_{oc} - \frac{h_{fc}h_{rc}}{h_{ic}+R_s}$$

$$R_o = \frac{1}{Y_o} = 34.396\ \Omega$$

> [added] **The intermediate $Y_o$ is not printed on ·L6 p25 — only $R_o$.** Supplying it:
> $$Y_o = 25\times10^{-6} + \frac{61}{1200+900} = 25\times10^{-6} + 0.029\,048 = 0.029\,073\ \mathrm{S}$$
> $$R_o = \frac{1}{0.029\,073} = 34.397\ \Omega$$
> which reproduces the printed 34.396 $\Omega$. Note the **plus** sign: $h_{fc}$ is negative, so
> $-h_{fc}h_{rc}$ is positive and the second term *adds* to $h_{oc}$ — the opposite of what happens
> in CE, and the reason the CC output resistance is small rather than large.

### Approximate analysis ·L6 p25

$$A_I = 1 + h_{fe} = 1+60 = 61$$

$$R_i = h_{ie} + (1+h_{fe})R_L = 1200 + 61\times2000 = 123.2\ \mathrm{k}\Omega$$

$$A_V = 1 - \frac{h_{ie}}{R_i} = 1 - \frac{1200}{123\,200} = 0.99$$

$$R_o = \frac{h_{ie}+R_s}{1+h_{fe}} = \frac{1200+900}{61} = 34.43\ \Omega$$

> [added] **All four verified**, and the comparison is instructive:
>
> | Quantity | Exact | Approximate | Error |
> |---|---|---|---|
> | $A_I$ | 58.095 | 61 | $+5.0\ \%$ |
> | $R_i$ | 117.39 k$\Omega$ | 123.2 k$\Omega$ | $+4.9\ \%$ |
> | $A_V$ | 0.9897 | 0.9903 | $+0.05\ \%$ |
> | $R_o$ | 34.396 $\Omega$ | 34.426 $\Omega$ | $+0.09\ \%$ |
>
> Recomputed exactly: $A_I = 58.0952$, $R_i = 117\,390.5\ \Omega$, $A_V = 0.98978$,
> $R_o = 34.3966\ \Omega$ (exact) and $34.4262\ \Omega$ (approximate). Here $h_{oe}R_L = 0.05$, still
> inside the criterion, and the two quantities that matter most for a buffer — **$A_V$ and $R_o$ —
> agree to better than 0.1 %**. Unlike the CE case of §6.21, the CC approximate model *does* give a
> finite $R_o$, and a very accurate one.

---

## 6.23 Worked problem 3 — CB amplifier, all seven quantities ·L6 p25–p26

[ex ·L6 p25] **Problem.** For a CB transistor amplifier driven by a voltage source of internal
resistance $R_s = 1200\ \Omega$, the load impedance is a resistor $R_L = 1000\ \Omega$. The
h-parameters are

$$h_{ib} = 22\ \Omega,\qquad h_{rb} = 3\times10^{-4},\qquad h_{fb} = -0.98,\qquad h_{ob} = 0.5\ \mu\mathrm{A/V}$$

Compute the current gain $A_I$, input impedance $R_i$, voltage gain $A_V$, overall voltage gain
$A_{VS}$, overall current gain $A_{IS}$, output impedance $R_o$ and power gain $A_P$, **using exact
and approximate analysis**.

### Exact analysis ·L6 p25–p26

**Current gain**

$$A_I = \frac{-h_{fb}}{1+h_{ob}R_L} = \frac{0.98}{1+(0.5\times10^{-6})(1000)} = \frac{0.98}{1.0005} = 0.98$$

**Input impedance**, with $Y_L = 1\times10^{-3}\ \mathrm{S}$

$$R_i = h_{ib} - \frac{h_{fb}h_{rb}}{Y_L+h_{ob}} = 22 + \frac{2.94\times10^{-4}}{1.0005\times10^{-3}} = 22.3\ \Omega$$

**Voltage gain**

$$A_V = \frac{A_IR_L}{R_i} = \frac{0.98\times1000}{22.3} = 43.94$$

**Overall voltage gain**

$$A_{VS} = \frac{A_VR_i}{R_i+R_s} = \frac{43.94\times22.3}{22.3+1200} = 0.802$$

**Overall current gain**

$$A_{IS} = \frac{A_IR_s}{R_i+R_s} = \frac{0.98\times1200}{22.3+1200} = 0.962$$

**Output admittance and resistance**

$$Y_o = h_{ob} - \frac{h_{fb}h_{rb}}{h_{ib}+R_s} = 0.5\times10^{-6} + \frac{2.94\times10^{-4}}{1222} = 0.74\times10^{-6}\ \text{mho}$$

$$R_o = \frac{1}{Y_o} = 1.35\ \mathrm{M}\Omega$$

**Power gain**

$$A_P = A_VA_I = 43.94\times0.98 = 43.06$$

> [added] **All eight numbers verified independently.** $A_I = 0.97951$ (printed 0.98);
> $R_i = 22.294\ \Omega$ (printed 22.3); $A_V = 43.936$ from unrounded inputs, $43.946$ from the
> page's own rounded 0.98 and 22.3 (printed 43.94); $A_{VS} = 0.8014$ (printed 0.802);
> $A_{IS} = 0.9616$ (printed 0.962); $Y_o = 7.406\times10^{-7}\ \mathrm{S}$ (printed
> $0.74\times10^{-6}$); $R_o = 1.350\ \mathrm{M}\Omega$ (printed 1.35 M$\Omega$); $A_P = 43.04$
> unrounded, 43.06 from the rounded factors (printed 43.06). **No discrepancy beyond rounding.**

> [added] **Read the three gains against each other.** $A_V = 43.9$ but $A_{VS} = 0.802$ — the CB
> stage has real voltage gain, and a 1.2 k$\Omega$ source throws essentially all of it away, because
> $R_i = 22\ \Omega$ divides the input signal by 55. Meanwhile $A_{IS} = 0.962$ is barely below
> $A_I$, because the same low $R_i$ makes the stage an *excellent* current-driven load. **This one
> problem is the whole "CB matches a very low impedance source" claim of §6.16 in numbers.**

### Approximate analysis ·L6 p26

$$A_I = -h_{fb} = 0.98$$

$$R_i = h_{ib} = 22\ \Omega$$

For the voltage gain the approximate CB formula is written in **CE** parameters, so the CB data must
be converted back. ·L6 p26

$$h_{fb} = \frac{-h_{fe}}{1+h_{fe}} \quad\Longrightarrow\quad h_{fe} = \frac{-h_{fb}}{1+h_{fb}} = \frac{0.98}{1-0.98} = 49$$

$$h_{ib} = \frac{h_{ie}}{1+h_{fe}} \quad\Longrightarrow\quad h_{ie} = h_{ib}(1+h_{fe}) = 22(1+49) = 1100\ \Omega$$

$$A_V = \frac{h_{fe}R_L}{h_{ie}} = \frac{49\times1000}{1100} = 44.54$$

$$R_o = \infty$$

and the notes state that **$A_{VS}$, $A_{IS}$ and $A_P$ are the same as in the exact analysis**. ·L6 p26

> [added] **Both back-conversions verified**: $h_{fe} = 0.98/0.02 = 49$ exactly, and
> $h_{ie} = 22\times50 = 1100\ \Omega$ exactly — which is also, reassuringly, the typical value of
> §6.6. $A_V = 49000/1100 = 44.545$, printed 44.54.

> ⚠ VERIFY **C6.7** ·L6 p26 — the closing statement *"$A_{VS}$, $A_{IS}$, $A_P$ are same as that of
> exact analysis"* holds for two of the three but **not for $A_P$**. Recomputing each with the
> approximate values ($A_V = 44.54$, $A_I = 0.98$, $R_i = 22\ \Omega$):
> $$A_{VS} = \frac{44.54\times22}{22+1200} = 0.802 \quad\text{(exact: 0.802)} \;\text{✓}$$
> $$A_{IS} = \frac{0.98\times1200}{22+1200} = 0.962 \quad\text{(exact: 0.962)} \;\text{✓}$$
> $$A_P = A_VA_I = 44.54\times0.98 = 43.65 \quad\text{(exact: 43.06)} \;-\ \textbf{1.4\% higher}$$
> The two overall gains genuinely are unchanged, because the approximation moves $A_V$ up by the same
> factor it moves $R_i$ down and the two effects cancel in $A_VR_i$. $A_P$ has no such cancellation.
> Correct closing statement: **$A_{VS}$ and $A_{IS}$ are the same; $A_P$ rises to 43.65.** Nothing
> else on the page changes. See `_verification-log.md`.

---

## 6.24 [added] $\Delta h$ and the compact forms

The notes never introduce the **determinant of the h-matrix**, but every standard text and most
formula sheets state $Z_i$ and $Y_o$ in terms of it, and CATs drawn from other sources may use it.
It is worth having the bridge.

[eq: delta-h] **Definition**

$$\boxed{\;\Delta h = h_ih_o - h_fh_r\;}$$

- $\Delta h$ — determinant of the hybrid matrix, dimensionless (ohm × siemens = 1)

[eq: zi-delta-h] **Input impedance in $\Delta h$ form** — algebraically identical to §6.9

$$\boxed{\;Z_i = \frac{h_i + \Delta h\,Z_L}{1 + h_oZ_L}\;}$$

[derivation] [added] Starting from the notes' own result and putting the two terms over a common
denominator:

$$Z_i = h_i - \frac{h_fh_r}{Y_L+h_o} = \frac{h_i(Y_L+h_o) - h_fh_r}{Y_L+h_o} = \frac{h_iY_L + (h_ih_o - h_fh_r)}{Y_L+h_o} = \frac{h_iY_L + \Delta h}{Y_L+h_o}$$

Multiplying numerator and denominator by $Z_L = 1/Y_L$ gives the boxed form.

[eq: yo-delta-h] **Output admittance in $\Delta h$ form** — algebraically identical to §6.11

$$\boxed{\;Y_o = \frac{h_oR_s + \Delta h}{R_s + h_i}\;}$$

[derivation] [added]

$$Y_o = h_o - \frac{h_fh_r}{R_s+h_i} = \frac{h_o(R_s+h_i) - h_fh_r}{R_s+h_i} = \frac{h_oR_s + \Delta h}{R_s+h_i}$$

> [added] **Numerical check on §6.21's data**, $h_{ie}=1000$, $h_{re}=2\times10^{-4}$, $h_{fe}=50$,
> $h_{oe}=25\times10^{-6}$, $R_s = 800\ \Omega$:
> $$\Delta h = (1000)(25\times10^{-6}) - (50)(2\times10^{-4}) = 0.025 - 0.010 = 0.015$$
> $$Y_o = \frac{(25\times10^{-6})(800) + 0.015}{800+1000} = \frac{0.02+0.015}{1800} = \frac{0.035}{1800} = 1.944\times10^{-5}\ \mathrm{S}$$
> — the same value as §6.21's corrected $Y_o$, reached by a completely different route. **This is the
> cleanest independent confirmation of flag V6.4.**

> [added] **A useful sanity number.** For a typical CE transistor $\Delta h \approx 0.015$–$0.02$,
> i.e. small but *not* negligible next to $h_oR_s$ — which is why $Y_o$ depends so strongly on the
> source resistance.

---

## 6.25 Exercises

**L6 sets no unsolved exercises.** All three "Problem" statements in the lesson (·L6 p23, ·L6 p24,
·L6 p25) are worked in full by the lecturer and are transcribed and verified above as §6.21, §6.22
and §6.23. There is nothing in the 26 pages left for the reader to solve, and nothing has been
invented here to fill that space.

> [added] **What that means for revision.** Because the lesson contains no problem set, the three
> worked problems carry the entire numerical burden of the topic, and a CAT can lift any of them
> verbatim with changed numbers. The pattern they establish is fixed and worth drilling:
>
> 1. **Identify the configuration** and convert the given h-parameters into it (§6.15) if they were
>    quoted in another.
> 2. **$A_I$ first** — it is the only one that needs nothing but $h_f$, $h_o$ and $R_L$.
> 3. **$R_i$ next**, because $A_V$ needs it.
> 4. **$A_V = A_IR_L/R_i$**, then $A_{VS}$ and $A_{IS}$ if asked.
> 5. **$Y_o$ last**, and always invert it to quote $R_o$.
> 6. **Then repeat with the approximate formulas** and comment on the difference — every one of the
>    three problems asks for both.

---

## 6.26 Cosmetic flags collected

> ⚠ VERIFY **C6.8** ·L6 p3, p5, p24, p26 — spelling and transcription slips in the handwriting.
> None changes anything computed.
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·L6 p3 | "Transistor" written **"Transiston"** throughout; "Two-port Network" capitalised mid-sentence | transistor |
> | ·L6 p3 | $V_i = f_1(I_l,\,V_o)$ — the subscript on the first argument reads as a letter **l** | $V_i = f_1(I_i,\,V_o)$ |
> | ·L6 p5 | "Advantages (or) **Benifits**" | Benefits |
> | ·L6 p5 | "**convinient** to use in circuit analysis" | convenient |
> | ·L6 p5 | "Easily **convertable** from one configuration to other" | convertible |
> | ·L6 p5 | "manufacturers **sepecify** the h-parameters" | specify |
> | ·L6 p24 | "**Convension** formulae" | Conversion |
> | ·L6 p26 | "**Convusion** formulae" | Conversion |
>
> See `_verification-log.md`.

---

## 6.27 What to carry out of this lesson

- **The two defining equations and the model that draws them.** $V_1 = h_iI_1+h_rV_2$ is a KVL loop
  with a **voltage** source; $I_2 = h_fI_1+h_oV_2$ is a KCL node with a **current** source. Every
  result in twenty-four pages is those two lines plus $V_2 = -I_2Z_L$.
- **The four exact results**, in the order they must be computed: $A_I$, then $Z_i$, then
  $A_V = A_IZ_L/Z_i$, then $Y_o$.
- **The dimensional signature** $(\Omega,\ 1,\ 1,\ \mathrm{S})$. Three of this file's four
  substantive flags were caught by it.
- **The conversion formulae**, especially "divide by $1+h_{fe}$" for CB and
  $h_{fc} = -(1+h_{fe})$, $h_{rc}=1$ for CC.
- **The three approximate boxes** of §6.18, §6.19 and §6.20, and the condition $h_{oe}R_L<0.1$ that
  licenses them.
- **The comparison table of §6.17** — the shape of it, not the digits: CB lowest $R_i$ and highest
  $R_o$; CC the reverse; CE alone with both gains and alone inverting.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
