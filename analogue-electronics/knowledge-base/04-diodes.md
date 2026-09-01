---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "04 — Junction Diodes and Special Diode Types"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 33-45"
pages: "J p33-p45"
tier: primary
file_role: topic
subtopics:
  - "the diode: circuit symbol, P-N construction, what it does"
  - "formation of the depletion layer, the potential barrier and why diffusion stops"
  - "forward bias: circuit, mechanism, Ge and Si turn-on voltages"
  - "reverse bias: circuit, depletion widening, leakage current"
  - "the static V-I characteristic: test circuit, knee voltage, leakage, breakdown and PIV"
  - "the diode static equation, the ideality factor and the thermal voltage"
  - "Thevenin analysis of a diode circuit and the diode current I_D"
  - "static (dc) resistance r_dc"
  - "the dc load line, its two intercepts and the Q point"
  - "ac resistance r_ac read off the load line"
  - "the three diode models: approximate, simplified, ideal"
  - "worked example: load line of a 20 V two-resistor network (V_Th = 13.33 V, 0.2 A intercept)"
  - "worked example: multi-diode Ge/Si network, power in a 20 ohm resistor (6.66 W)"
  - "LED: symbol, construction, operation, luminosity curve, ratings, applications"
  - "photodiode: symbol, construction, operation, characteristics, dark current, applications"
  - "tunnel diode: heavy doping, tunnelling, the negative-resistance region, applications"
  - "varactor diode: symbol, construction as a parallel-plate capacitor, C against V_R, tuned circuits"
key_equations: [diode-static-equation-j, thermal-voltage-j, thevenin-vth-diode, thevenin-rth-diode, diode-current-thevenin, dc-load-line-intercepts, r-dc-static, r-ac-dynamic, diode-turn-on-voltages, photodiode-dark-current, varactor-plate-capacitance, varactor-resonant-frequency]
prerequisites:
  - "semiconductor material, doping, majority and minority carriers (·J p20s; 01-diodes §1.2)"
  - "Thevenin's theorem (network theorems)"
leads_to:
  - "rectifiers and power supplies (·J p46 onward; 12-rectifiers.md)"
  - "the bipolar junction transistor as two back-to-back junctions (13-bipolar-junction-transistor.md)"
  - "Zener diodes and voltage regulation — NOT in this range; see 11-diodes.md §1.8-§1.10"
verification_flags: 23
tags: [diode, pn-junction, depletion-layer, barrier-potential, forward-bias, reverse-bias, knee-voltage, piv, breakdown, diode-equation, ideality-factor, thermal-voltage, thevenin, load-line, q-point, dc-resistance, ac-resistance, diode-models, led, photodiode, tunnel-diode, varactor, negative-resistance]
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

# 04 — Junction Diodes and Special Diode Types

Scope: **·J p33–p45**, thirteen pages of the course's own lecture notes. Builds the junction diode
from the depletion layer up, fixes the two bias conditions and the Ge/Si turn-on voltages, reads the
static characteristic, states the diode equation, then spends most of its length on **circuit
analysis** — Thevenin reduction, the dc load line, the Q point, dc and ac resistance and the three
diode models — worked through two numerical examples. It closes with **Types of Diodes**: LED,
photodiode, tunnel diode and varactor.

**This is tier 1.** Where `11-diodes.md` (tier 2, a textbook compilation) covers the same ground, that
file is usually the fuller derivation, but *this* document is what the course teaches and what a CAT
will be set from. §4.18 compares the two point by point.

---

## 4.0 Citation, and where this range's gaps are

**Citation.** `·J p35` means **PDF page 35**. The document's own printed page number runs **one
behind the PDF page** — PDF p35 shows printed "34" — and that offset holds unbroken across the whole
document. Everything below cites **PDF pages only**.

### The section starts without a heading ⚠

**·J p33 opens the diode material with no visible heading.** The page begins directly with the
circuit-symbol figure; the space above it is blank. The preceding page, ·J p32, finishes a worked
transformer example — an unrelated topic — so a heading was certainly present and has been lost with
the blank space. **No heading is invented here.** This file's own title is editorial.

### Opaque redaction blocks in this range

Five pages in this range carry solid yellow blocks over text. **There is nothing underneath** — the
text is destroyed, not merely hidden. Each is marked `⚠ REDACTED` at the point of use. Where the
surrounding text makes the missing word certain, an inference is offered and labelled `[added]`;
where it does not, this file says so and stops.

[table] **Redaction map for ·J p33–p45**

| Page | Blocks | Block width (px, page = 1653 px wide) | What the sentence needs | Recovered? |
|---|---|---|---|---|
| ·J p35 | 1 | 148 (≈14 characters) | the name for the forward voltage at which conduction begins | **yes** — see §4.5 |
| ·J p40 | 1 | 106, at heading weight | the label introducing the second worked example | **yes, with high confidence** — see §4.12 |
| ·J p41 | 2 | 198 and 217 (≈19 and ≈21 characters) | two LED semiconductor material names | **no** — see §4.13 |
| ·J p42 | 1 | 301, at heading weight | a section heading between *Construction* and *Operation* | **no** — see §4.13 |
| ·J p44 | 2 | 118 and 134 (≈11 and ≈13 characters) | the names of the two turning points of the tunnel-diode curve | **yes** — see §4.15 |

### One clipped heading

⚠ ILLEGIBLE ·J p43 — the heading at the very top of the page is **clipped by the page margin**; only
the bottom two or three pixel rows of the glyphs survive. This is a page-break casualty, not a
redaction. The surviving word-shape is two words of roughly 14 and 5 characters, and the same
heading appears in the same position in the LED and varactor sections, so it is almost certainly
*Characteristic Curve*. Logged as **JC4.10**.

⚠ ILLEGIBLE ·J p40 — the top line of the page is a clipped fragment in which only two repetitions of
the symbol $R_{Th}$ survive. It is the tail of an equation that overflowed from ·J p39; the surviving
text on p39 and p40 makes the argument complete without it, so nothing is missing from the physics.
No screenshot needed.

---

## 4.1 What a diode is ·J p33

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_o$ | barrier (junction) potential, also the turn-on voltage | V | 0.3 (Ge), 0.7 (Si) |
| $V_S$ | supply voltage of the bias circuit | V | 5–20 |
| $D$ | the diode, as labelled on every circuit in this range | — | — |

[def] A **diode** is a device which allows current to flow in **one direction only**. It is made from
**P-type and N-type semiconductor joined together**, and it has a **depletion layer** — equivalently
a **P–N junction**, equivalently a **potential barrier**. ·J p33

[fig ·J p33] **Two figures side by side at the top of the page.**

- **Left — circuit symbol.** A horizontal wire with the standard diode symbol at its centre: a solid
  triangle pointing **right** into a vertical bar. The wire entering on the left is labelled
  **Anode**, the wire leaving on the right **Cathode**. Caption: *Circuit symbol*.
- **Right — physical construction.** The same horizontal wire, but the symbol is replaced by a
  rectangular block split into two labelled cells, **P** on the left and **N** on the right, with a
  narrow gap drawn between them. An arrow points up at that gap, labelled **Depletion Layer**.

**Read the two together:** the triangle is the P side (anode), the bar is the N side (cathode).
Conventional current flows in the direction the triangle points.

---

## 4.2 Formation of the depletion layer ·J p33

[derivation] What happens when the two materials are joined ·J p33:

1. A p-type and an n-type semiconductor are joined.
2. Electrons in the n-type material **adjacent to the junction** move across to fill holes on the
   p-side, which are also at the junction.
3. That leaves behind **positive and negative ions which have no charge carriers** — a layer swept
   clear of mobile charge.
4. This swept region is the **depletion layer**.
5. It is also called a **potential barrier**, because the positive ions on the **n-side** sit at a
   **higher potential** than the negative ions on the **p-side**.

**Why diffusion stops** ·J p33 — after a time the **positive ions repel the holes** and the
**negative ions repel the electrons**, and no further net crossing occurs.

> ⚠ VERIFY **JV4.1** ·J p33 — printed: *"The movement of ions process is called diffusion."*
> **The ions do not move.** The whole point of the two preceding sentences is that the depletion
> layer consists of **fixed, ionised dopant atoms locked in the crystal lattice**, stripped of their
> mobile carriers. Correct statement:
> $$\boxed{\;\text{diffusion is the movement of the \textbf{mobile charge carriers} — electrons and holes — across the junction}\;}$$
> **Why it matters.** A reader who believes ions migrate cannot explain why the barrier is
> *self-limiting*: it is precisely because the ions stay put that the field they create grows until
> it cancels the diffusion tendency. The same page's own next sentence — "the positive ions will
> repel the holes and the negative ions will repel the electrons" — only makes sense with the ions
> stationary. See `_verification-log.md`.

[fig ·J p33] **Depletion-layer formation, two stacked panels.**

- **Upper panel — before contact.** Two separate rectangular blocks, drawn apart. The **left** block
  is filled with rows of small circles marked $\ominus$ paired with open circles; a leader line from
  the top labels these **Holes**. The **right** block is filled with $\oplus$ symbols each carrying a
  small superscript **e**; a leader from the right labels these **Electrons**. (P material on the
  left, N material on the right.)
- **Lower panel — after contact.** The same two blocks now pushed together, with **two narrow
  columns inserted between them**: a column of $\ominus$ ions on the P side and a column of $\oplus$
  ions on the N side. A double-headed arrow beneath these two columns is labelled **Depletion
  Layer**, with dashed vertical lines marking its two edges.
- **Below that — the potential step.** A horizontal baseline runs in from the left, ramps **upward**
  across the width of the depletion layer, then continues flat to the right. A vertical
  double-headed arrow measures the step height and is labelled $V_o = 0.3\ \mathrm{V}$.

*[added] Note that the figure's $0.3\ \mathrm{V}$ is the **germanium** barrier. The page presents it
as if generic. For silicon the same step is $\approx 0.7\ \mathrm{V}$, as ·J p34 and ·J p38 both go
on to say.*

---

## 4.3 Forward bias ·J p33–p34

**Connection.** Anode to the **positive** terminal, cathode to the **negative** terminal. ·J p33–p34

**Mechanism** ·J p34 — this leads to a **continuous supply of electrons and a continuous supply of
holes at the junction**, so current flows and the bulb in the test circuit lights.

[eq: diode-turn-on-voltages] **Turn-on voltages** ·J p34

$$\boxed{\;V_o(\mathrm{Ge}) = 0.2\text{–}0.3\ \mathrm{V},\qquad V_o(\mathrm{Si}) = 0.6\text{–}0.7\ \mathrm{V}\;}$$

- $V_o$ — the forward voltage at which conduction begins, V

Once conducting, **the depletion layer disappears**. ·J p34

[fig ·J p33] **Forward-bias test circuit, drawn twice.** A single rectangular loop. On the left leg,
a battery $V_S$ with the **+ plate uppermost**. Along the top wire, the diode $D$ with its triangle
pointing **right**, i.e. **away from the +** terminal along the direction of current flow. On the
right leg, a lamp symbol (an oval with a leader) labelled **Bulb**. The second copy of the circuit
is identical except that the diode symbol is replaced by the **P | N** block, again with **P on the
left** — the side nearer the battery's positive plate.

**The rule to carry away:** forward bias means **P to +, N to −**.

---

## 4.4 Reverse bias ·J p34

**Connection.** The anode is connected to the **negative** terminal, the cathode to the
**positive** terminal of the supply. ·J p34

**What happens** ·J p34:

- The **width of the depletion layer is enlarged**, because the majority carriers are pulled **away**
  from the junction.
- Only a **minimal current** flows, carried by the **minority charge carriers**.
- That current is the **leakage current**. The page expresses it in **µA** — too small to light the
  bulb.

[fig ·J p34] **Reverse-bias test circuit, drawn twice.** Same rectangular loop and same lamp as the
forward figure, but the battery on the left leg now has its **− plate uppermost**, so the diode
triangle points *into* the supply's positive return. The right-hand copy again substitutes the
**P | N** block for the symbol.

> ⚠ VERIFY **JC4.2** ·J p34 — printed: *"the width of the depletion layer is enlarged due to majority
> charge carriers **(electrons)** moving away from the junction."* The parenthesis names only one
> carrier. **Both** majority species retreat: electrons withdraw into the N region and **holes**
> withdraw into the P region, and it takes both to widen the layer at both edges. Nothing computed
> changes. See `_verification-log.md`.

> ⚠ VERIFY **JC4.3** ·J p34 — the leakage current is given as *"expressed in terms of µA"* without
> qualification. Microamps is the **germanium** order of magnitude; for **silicon** the reverse
> saturation current is **nanoamps**, three orders smaller. `11-diodes.md` §1.4 states both. Nothing
> computed in this range changes. See `_verification-log.md`.

---

## 4.5 The static V–I characteristic ·J p34–p35

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_f$ | forward voltage across the diode | V | 0–1 |
| $I_f$ | forward current | A (usually mA) | 1–100 mA |
| $V_R$ | reverse voltage | V | up to $V_{BR}$ |
| $I_R$ | reverse (leakage) current | A (µA or nA) | nA (Si), µA (Ge) |
| $V_{BR}$ | breakdown voltage | V | tens to hundreds |

[fig ·J p34] **Measurement circuit.** A supply $V_S$ on the far left feeds a **potentiometer $R_1$**
drawn as a resistor with a wiper arrow — the wiper taps off a variable fraction of the supply. From
the wiper the circuit runs through a series resistor $R_2$ and an **ammeter (A)** along the top wire
to the diode $D$, which sits in the right-hand leg with its triangle pointing **downward**. A
**voltmeter (V)** is connected **across the diode**. So: $R_1$ sets the applied voltage, $R_2$ limits
the current, (A) reads $I$, (V) reads $V$.

[fig ·J p34] **The static characteristic — learn to redraw this.**

- **Axes.** Vertical up: $I_f$. Horizontal right: $V_f$. Horizontal left: $V_R$. Vertical down: $I_R$.
- **First quadrant.** Two curves, both flat along the axis and then kneeing sharply upward:
  the **left** curve is labelled **Germanium** and turns up at the tick marked **0.2 v**; the
  **right** curve is labelled **Silicon** and turns up at the tick marked **0.7 v**. A leader with
  an arrow points at the silicon knee and reads **Knee voltage**.
- **Third quadrant.** From the origin the trace runs just below the axis, essentially flat, leftward
  — labelled with a leader **Leakage current**. Two near-vertical plunges are drawn: the **left** one
  is labelled **Si** at its foot and the **right** one **Ge**, so silicon is shown breaking down at
  the **larger** reverse voltage. A leader labelled **Breakdown Voltage** points at the knee where
  the trace turns downward.

[def] **Knee voltage.** ·J p35 The characteristic stays essentially flat until the forward voltage
reaches the turn-on value — silicon "conducting at 0.7 V" — and beyond it **every further increment
of voltage produces a corresponding increment of current, and the diode behaves like a normal
conductor**.

> ⚠ REDACTED ·J p35 — a term is covered by an opaque block: the sentence reads *"The voltage at
> which the diodes start conducting current is called ▮"*, and the block (148 px, about 14
> characters) destroys the name being defined.
>
> *[added] The covered term is almost certainly **knee voltage**. The evidence is decisive: the
> figure on the facing page (·J p34) carries a leader labelled exactly "Knee voltage" pointing at the
> 0.7 V turn-up of the silicon curve, and the phrase is 12 characters plus a space — a match for the
> block width. This is our inference, not the notes' word.*

**Reverse behaviour** ·J p35:

- At **zero** applied reverse voltage there is already a very small current — the **leakage current**.
- **Increasing the reverse voltage does not affect that current**, as long as it stays within the
  limit the diode can withstand.
- The current in a diode is **affected by temperature**.

**Breakdown** ·J p35:

- Push the reverse voltage past what the diode can withstand and it **breaks down**.
- Mechanism as the page gives it: **minority electrons moving at high speed detach the electrons
  which are bonded**, breaking down the junction.
- The electrons at this point are called **avalanche electrons**.
- **This current can damage the diode.**

> ⚠ VERIFY **JV4.4** ·J p35 — printed: *"This point can be called breakdown voltage or peak inverse
> voltage (PIV)."* The two are **not the same number**, and treating them as synonyms is how
> rectifier diodes get destroyed in design work. Correct distinction:
> $$\boxed{\;V_{BR} = \text{the voltage at which breakdown physically occurs;}\quad \mathrm{PIV} = \text{the manufacturer's \textbf{rating} — the largest reverse voltage the diode may safely be subjected to}\;}$$
> **Why.** PIV is specified *below* $V_{BR}$, with margin. A 1N4007 is rated PIV = 1000 V; its actual
> avalanche point is higher. Design to the PIV, not to the breakdown voltage. Note also that ·J p46
> repeats the equation, describing rectifier diodes as having "high power rating and peak inverse
> voltage/ breakdown voltage". See `_verification-log.md`.

*[added] **This range covers only avalanche breakdown.** The second mechanism — **Zener (field)
breakdown**, which dominates below about 5 V — is never mentioned, and neither is the Zener diode or
voltage regulation. That material is entirely in the tier-2 file: `11-diodes.md` §1.8–§1.10. See
§4.18.*

---

## 4.6 The diode static equation ·J p35

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $i_o$ | diode current (the notes' own symbol — see JC4.1) | A | mA |
| $I_o$ | temperature-dependent saturation current | A | nA (Si), µA (Ge) |
| $V_D$ | diode terminal voltage | V | 0.7 |
| $\eta$ | empirical (ideality) constant | — | 1 for Ge, 2 for Si |
| $V_T$ | thermal voltage | V | 26 mV at 300 K |
| $k$ | Boltzmann's constant | J K$^{-1}$ | $1.38\times10^{-23}$ |
| $T$ | absolute temperature | K | 300 |
| $q$ | electronic charge | C | $1.6\times10^{-19}$ |

**What the page prints** ·J p35:

$$i_o = I_o\left(\frac{V_D}{e^{\eta V_T}} - 1\right)\qquad\text{⚠ JV4.3 — the exponent has become a denominator}$$

$$V_T = \frac{kT}{q},\qquad k = 1.38\times10^{-28}\ \mathrm{J/K}\quad\text{⚠ JV4.2}$$

[eq: diode-static-equation-j] **The equation in correct form**

$$\boxed{\;i_D = I_o\left(e^{\,V_D/\eta V_T} - 1\right),\qquad V_T = \frac{kT}{q}\;}$$

[eq: thermal-voltage-j] **The thermal voltage, evaluated**

$$V_T = \frac{kT}{q} = \frac{1.38\times10^{-23}\times300}{1.6\times10^{-19}} = 25.9\ \mathrm{mV}\ \approx 26\ \mathrm{mV\ at\ }300\ \mathrm{K}$$

*[added] Recomputed: $1.38\times10^{-23}\times300/1.6\times10^{-19} = 25.875\ \mathrm{mV}$ ✓. At
293 K the same expression gives $25.27\ \mathrm{mV}$, which is why textbooks quote either 25 mV or
26 mV depending on the room temperature assumed. The notes give **no numerical value for $V_T$** at
all.*

> ⚠ VERIFY **JV4.2** ·J p35 — printed: **"$k$ = Boltzmann's constant $= 1.38\times10^{-28}$ J/K"**.
> Correct form:
> $$\boxed{\;k = 1.38\times10^{-23}\ \mathrm{J\,K^{-1}}\;}$$
> **Why, in one line a reader can repeat:** with the printed exponent,
> $V_T = 1.38\times10^{-28}\times300/1.6\times10^{-19} = 2.6\times10^{-7}\ \mathrm{V}$ — a quarter of
> a **microvolt**. The printed constant is wrong by a factor of $10^5$, and every exponent computed
> from it would be $10^5$ too large. Nothing else on the page uses it numerically, so no result in
> this range is corrupted — but the constant is memorised from pages like this one.
> See `_verification-log.md`.

> ⚠ VERIFY **JV4.3** ·J p35 — the diode equation is typeset with $V_D$ as a **numerator over**
> $e^{\eta V_T}$, i.e. $i_o = I_o\!\left(V_D/e^{\eta V_T} - 1\right)$. $V_D$ belongs **in the
> exponent**, divided by $\eta V_T$:
> $$\boxed{\;i_D = I_o\left(e^{\,V_D/\eta V_T} - 1\right)\;}$$
> **Three checks the reader can repeat.**
> 1. **Dimensions.** As printed, $e^{\eta V_T}$ exponentiates a quantity in **volts** — an exponent
>    must be dimensionless. The correct form exponentiates $V_D/\eta V_T$, volts over volts. ✓
> 2. **Numbers.** Silicon, $\eta = 2$, $V_T = 25.85\ \mathrm{mV}$, $V_D = 0.7\ \mathrm{V}$,
>    $I_o = 1\ \mathrm{pA}$: the correct form gives $0.76\ \mathrm{µA}$; the printed form gives
>    $-3.4\times10^{-13}\ \mathrm{A}$ — a **negative** current for a **forward**-biased diode.
> 3. **Behaviour.** The printed form is linear in $V_D$; the whole point of the characteristic drawn
>    two pages earlier is that it is exponential.
>
> Almost certainly an equation-editor casualty rather than a misunderstanding — but it is what the
> page prints, and it is what a reader copying from the page will write in an exam.
> See `_verification-log.md`.

> ⚠ VERIFY **JC4.1** ·J p35 — **notation clash.** The page writes the **diode current** as $i_o$
> and the **saturation current** as $I_o$ — the same letter in two cases, distinguished only by
> capitalisation, on the two sides of one equation. This is exactly the situation the
> `_nomenclature.md` clash table exists for. The standard convention, and the one used everywhere
> else in this file, is $i_D$ (or $I_D$) for the diode current and $I_o$ (or $I_S$) for the
> saturation current. Nothing computed changes. See `_verification-log.md`.

**The ideality factor** ·J p35 — $\eta$ is described as an **empirical constant**, with

$$\eta = 1\ \text{for germanium},\qquad \eta = 2\ \text{for silicon}$$

*[added] This is exactly the assignment `11-diodes.md` §1.5 gives — see §4.18. It is worth knowing
that the $-1$ sits **outside** the bracket here, which is the correct placement and which the tier-2
handout gets wrong in four separate places.*

---

## 4.7 Thevenin analysis of a diode circuit ·J p35–p36

The notes head this **"Diode parameters"**, but the whole passage is one technique: **reduce
everything around the diode to a Thevenin source, then the diode sees a single loop.**

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_S$ | supply voltage | V | 20 |
| $R_S$ | source-side series resistance | Ω | 100 |
| $R$ | shunt resistance across the source branch | Ω | 200 |
| $R_L$ | load resistance, in series with the diode | Ω | 500 |
| $V_{Th}$ | Thevenin equivalent voltage seen by the diode branch | V | 13.33 |
| $R_{Th}$ | Thevenin equivalent resistance | Ω | 66.67 |
| $I_D$ | diode current | A | — |

[fig ·J p35] **The circuit to be reduced.** A supply $V_S$ on the left leg, + uppermost. Along the
top wire, a series resistor $R_S$. At node **A** a shunt resistor $R$ runs down to the bottom rail.
Continuing right from **A**, the current $I_D$ is arrowed into the diode $D$ (triangle pointing
right), and beyond it the load $R_L$ runs down to the bottom rail. So **$R$ is in parallel with the
series pair $D + R_L$.**

**Step 1 — open the diode branch and find $V_{Th}$.** ·J p36 With the diode removed,
**no current flows through $R_L$**, so $R_L$ drops nothing and the open-circuit voltage is just the
divider output at node A.

[eq: thevenin-vth-diode]

$$\boxed{\;V_{Th} = V_S\,\frac{R}{R_S + R}\;}$$

> ⚠ VERIFY **JV4.5** ·J p36 — printed: $V_{Th} = V_S\dfrac{R}{R_L + R}$. The denominator should be
> $R_S + R$, **not** $R_L + R$. Correct form:
> $$\boxed{\;V_{Th} = V_S\,\frac{R}{R_S + R}\;}$$
> **Why, three ways.**
> 1. **The page's own sentence.** The line immediately above reads "No current flows through $R_L$".
>    A resistor carrying no current cannot appear in a divider ratio.
> 2. **The page's own next equation.** $R_{Th} = R_S R/(R+R_S)$ — the parallel combination of $R_S$
>    and $R$. A Thevenin pair must be built from the same two elements.
> 3. **The worked example three pages later.** ·J p39 evaluates $20\times200/(100+200) = 13.33$ V,
>    using $R_S = 100$. As *printed* on p36, with $R_L = 500$, the same circuit would give
>    $20\times200/(500+200) = 5.71$ V — not the answer the notes themselves go on to use.
>
> See `_verification-log.md`.

**Step 2 — kill the source and find $R_{Th}$.** ·J p36

[eq: thevenin-rth-diode]

$$\boxed{\;R_{Th} = \frac{R_S R}{R_S + R}\;}$$

[fig ·J p36] **The $R_{Th}$ figure.** The supply has been replaced by a short (the left leg is a
plain wire). $R_S$ runs along the top from that short to the output terminal (small circle); $R$
hangs from the same node down to the bottom terminal (second small circle). Read directly: looking
in at the terminals, $R_S$ and $R$ are in **parallel**.

**Step 3 — the reduced loop, and the diode current.** ·J p36

[fig ·J p36] **The Thevenin equivalent.** A single loop: source $V_{Th}$ on the left leg, $R_{Th}$
along the top, the current $I_D$ arrowed into the diode $D$, and $R_L$ down the right leg.

[eq: diode-current-thevenin]

$$\boxed{\;I_D = \frac{V_{Th}}{R_L + R_{Th}}\;}$$

*[added] This is the **ideal-diode** answer — it assumes $V_D = 0$. Carrying the diode's own drop,
the same loop gives $I_D = (V_{Th} - V_D)/(R_{Th} + R_L)$, which is what §4.10's simplified model
produces. The notes use the ideal form here and the drop-carrying form in the second worked
example.*

---

## 4.8 The dc load line, the Q point and static resistance ·J p36–p37

**The construction, in words** ·J p36 — *plot a load line superimposed on the characteristic of a
diode*. The axes are the diode's own: **$V_D$ horizontal, $I_D$ vertical**.

[derivation] **[added] Where the load line comes from.** Apply KVL to the Thevenin loop of §4.7:

$$V_{Th} = I_D R_{Th} + V_D + I_D R_L$$

$$I_D = \frac{V_{Th} - V_D}{R_{Th} + R_L}$$

That is a **straight line** in the $(V_D,\,I_D)$ plane — the load line. Its two intercepts follow by
setting each variable to zero.

[eq: dc-load-line-intercepts] **The two intercepts as the notes state them** ·J p36, p40

$$\text{when } i_D = 0:\quad V_D = V_{Th}\qquad\text{(the } V_D\text{-axis intercept)}$$
$$\text{when } V_D = 0:\quad i_D = \frac{V_{Th}}{R_{Th}}\qquad\text{⚠ JV4.6 — } R_L \text{ is missing}$$

> ⚠ VERIFY **JV4.6** ·J p36, restated on ·J p40 and used numerically on ·J p39 — the current-axis
> intercept of the dc load line is given as $V_{Th}/R_{Th}$. For the circuit the notes are analysing,
> **$R_L$ is in series with the diode** and must appear in the total loop resistance. Correct form:
> $$\boxed{\;V_D\text{-intercept} = V_{Th};\qquad I_D\text{-intercept} = \frac{V_{Th}}{R_{Th} + R_L}\;}$$
> **Why, from the notes' own pages.** ·J p36 states, three lines above the load-line paragraph,
> $I_D = V_{Th}/(R_L + R_{Th})$. The short-circuit current of a loop and the current-axis intercept
> of its load line are **the same quantity** — set $V_D = 0$ in the KVL equation and you get the
> former. The two statements on one page cannot both be right.
>
> **The numerical size of the error.** For the worked example of §4.11 ($V_{Th} = 13.33\ \mathrm{V}$,
> $R_{Th} = 66.67\ \Omega$, $R_L = 500\ \Omega$):
> $$\text{notes: }\frac{13.33}{66.67} = 0.2\ \mathrm{A};\qquad \text{correct: }\frac{13.33}{566.67} = 23.5\ \mathrm{mA}$$
> — a factor of **8.5**, and it moves the Q point badly. Equivalently: if the Thevenin reduction is
> taken **at the diode's own two terminals**, then $R_L$ lies *between* those terminals and
> $R_{Th} = R_S\!\parallel\!R + R_L = 566.67\ \Omega$, giving the same correct intercept.
> The $V_D$-axis intercept, $V_{Th} = 13.33\ \mathrm{V}$, is right either way.
>
> See `_verification-log.md`.

[fig ·J p37] **Load line and Q point.** Axes $I_D$ (up) and $V_D$ (right). Two traces: the diode's
**VI characteristic**, flat along the axis and then kneeing steeply upward, labelled with a leader
*VI characteristics of a diode*; and a **straight line of negative slope** from high on the $I_D$
axis down to the $V_D$ axis, labelled *DC loadline*. They cross at a point labelled **Q point**.
Dashed construction lines drop from the crossing to $V_{DQ}$ on the horizontal axis and run left to
$I_{DQ}$ on the vertical axis.

[def] **Q point.** ·J p37 The **quiescent point** gives the **operating parameters** of a diode or a
transistor — the dc voltage and current the device actually sits at with no signal applied.

[eq: r-dc-static] **Static (dc) resistance** ·J p36–p37

$$\boxed{\;r_{dc} = \frac{V_{DQ}}{I_{DQ}}\;}$$

- $r_{dc}$ — static or dc resistance at the operating point, Ω
- $V_{DQ},\ I_{DQ}$ — the diode voltage and current **at the Q point**, V and A

*[added] $r_{dc}$ is the reciprocal slope of the **chord from the origin** to the Q point, not the
slope of the curve there. It is not a property of the diode alone — move the Q point and it changes.
For a silicon diode sitting at $V_{DQ} = 0.7\ \mathrm{V}$, $I_{DQ} = 10\ \mathrm{mA}$,
$r_{dc} = 70\ \Omega$; at $1\ \mathrm{mA}$ the same diode gives $r_{dc} \approx 650\ \Omega$.*

**Case convention** ·J p37 — worth memorising, because the rest of the course leans on it:

$$I_D \ \text{(upper case)} = \text{d.c. quantity};\qquad i_d \ \text{(lower case)} = \text{small-signal a.c. quantity}$$

[fig ·J p37] **DC level with a superimposed signal.** Vertical axis $I_{dc}$, horizontal axis
**time**. A horizontal solid line marks the dc level; a sinusoid of three cycles rides on it, its
peaks and troughs bounded by two dashed horizontal lines. An arrow points at the sinusoid, labelled
$I_d$ — the ac component about the dc operating current.

---

## 4.9 The ac resistance ·J p37–p38

[def] **$r_{ac}$ — a.c. resistance.** ·J p37 The resistance the diode presents to a **small signal**
riding on the dc operating point. It is read off the load line by perturbing the Q point.

[fig ·J p37] **The small-signal circuit.** The Thevenin loop again: $R_{Th}$ along the top with the
current $i_D$ arrowed into the diode $D$, $R_L$ down the right leg. The left leg now carries **two**
sources in series — the battery $V_{Th}$ above, and beneath it a **circle containing a downward
arrow**, labelled $i_D$ — the signal source superimposed on the dc supply.

> ⚠ VERIFY **JC4.4** ·J p37 — the small-signal source in this figure is drawn as a **circle with an
> arrow through it** — the standard symbol for an ideal **current** source — yet it is placed **in
> series** with the voltage source $V_{Th}$ and with $R_{Th}$, where a current source would fix the
> loop current and make $R_{Th}$ and $R_L$ irrelevant. It is also labelled $i_D$, the same symbol as
> the branch current arrowed at the top of the same figure. What the construction on the next page
> requires is a small-signal **voltage** source $v_d$ in series with $V_{Th}$, swinging the load line
> back and forth in parallel between the two positions $V_{D1}$ and $V_{D2}$. Nothing computed
> changes. See `_verification-log.md`.

[fig ·J p38] **Reading $r_{ac}$ off the load line.** The same load-line-and-characteristic diagram
as ·J p37, but now **three** operating points are marked on the diode curve, close together either
side of the Q point. Dashed lines carry them across to the current axis at $I_{D1}$, $I_{DQ}$,
$I_{D2}$ (bottom to top) and down to the voltage axis at $V_{D1}$, $V_{DQ}$, $V_{D2}$ (left to
right).

[eq: r-ac-dynamic] **Definition** ·J p38

$$r_{ac} = \frac{\text{change in } V_D}{\text{change in } i_D} = \frac{V_{D2}-V_{D1}}{i_{D2}-i_{D1}}$$

$$\boxed{\;r_{ac} = \frac{\Delta V_D}{\Delta i_D}\;}$$

- $r_{ac}$ — dynamic or ac resistance, Ω
- $\Delta V_D,\ \Delta i_D$ — the small excursions of diode voltage and current about the Q point,
  V and A

*[added] $r_{ac}$ is the reciprocal **slope of the characteristic at the Q point**, whereas $r_{dc}$
is the reciprocal slope of the chord from the origin. On the steep part of the curve
$r_{ac} \ll r_{dc}$. Differentiating the diode equation of §4.6 gives the closed form the tier-2
file uses instead: $r_{ac} = \eta V_T/I_{DQ}$, i.e. $25\ \mathrm{mV}/I_F$ for Ge and
$50\ \mathrm{mV}/I_F$ for Si with $I_F$ in mA. The two routes agree; this document teaches the
graphical one only.*

---

## 4.10 The three diode models ·J p38

The whole of the circuit work in this course rests on replacing the diode with one of three
equivalent circuits. **Know all three and know when each is legitimate.**

[table] **The three models** ·J p38

| Model | Equivalent circuit | Idealised characteristic | Use it when |
|---|---|---|---|
| **Approximate** | battery $V_o$ **+** forward resistance $r_f$ **+** ideal diode, all in series | a straight line rising from $V_o$ with finite slope $1/r_f$ | the bulk resistance matters — e.g. the multi-diode example of §4.12 |
| **Simplified** | battery $V_o$ **+** ideal diode in series | vertical line at $V_o$ | the usual working model — supply $\gg V_o$ but the drop is not negligible |
| **Ideal** | ideal diode alone | vertical line at the origin | first-pass analysis, switching logic, $V_o$ negligible against the supply |

[fig ·J p38] **Six panels, in three rows — circuit on the left, characteristic on the right.**

- **Approximate model.** Left: a two-terminal branch, $+$ at the left terminal and $-$ at the right,
  containing a battery labelled $V_o$ (its $+$ plate facing the left terminal), then a resistor
  labelled $r_f$, then the diode symbol $D$. Right: axes $I_f$ up, $V_f$ right, origin marked 0; a
  **straight sloping line** leaves the horizontal axis at the tick labelled $V_o$ and rises to the
  upper right. A leader arrow points at the take-off point.
- **Simplified model.** Left: the same branch with the resistor removed — battery $V_o$ then diode
  $D$. Right: the same axes with a **vertical line** erected at $V_o$.
- **Ideal model.** Left: the branch reduced to the diode symbol $D$ alone. Right: the same axes with
  a **heavy vertical line erected at the origin**, i.e. the diode conducts with zero drop.

[eq: diode-turn-on-voltages] **The turn-on voltages the models use** ·J p38

$$\boxed{\;V_o = 0.3\ \mathrm{V\ (germanium)},\qquad V_o = 0.6\text{–}0.7\ \mathrm{V\ (silicon)}\;}$$

- $V_o$ — turn-on voltage, V
- $r_f$ — forward (bulk) resistance of the conducting diode, Ω — 1 Ω for Ge and 2 Ω for Si in the
  worked example of §4.12

---

## 4.11 [ex] Worked example — the load line of a 20 V network ·J p39–p40

**Statement.** ·J p39 For the circuit shown, **draw the load line**.

[fig ·J p39] **The circuit.** Supply $V_S = 20\ \mathrm{V}$ on the left leg. Along the top wire a
series resistor $R_S = 100\ \Omega$. At the node beyond it, $R = 200\ \Omega$ runs down to the
bottom rail. Continuing right along the top wire, the diode (triangle pointing right), and then
$R_L = 500\ \Omega$ down to the bottom rail.

[fig ·J p39] **The open-circuit figure.** The same circuit with the **diode removed**, leaving two
small open terminals in the top wire between the $200\ \Omega$ node and the $500\ \Omega$ branch.

**Solution as the notes give it** ·J p39–p40

$$V_{Th} = \frac{20 \times 200}{100 + 200} = 13.33\ \Omega\qquad\text{⚠ JC4.5 — the unit is V}$$

$$R_{Th} = \frac{R_S R}{R_S + R} = \frac{200 \times 100}{200 + 100} = 66.67\ \Omega$$

$$\frac{V_{Th}}{R_{Th}} = \frac{13.33}{66.67} = 0.2\ \mathrm{A}$$

Then, stated as the rule for plotting ·J p40:

$$\text{when } i_D = 0,\ V_D = V_{Th};\qquad \text{when } V_D = 0,\ i_D = \frac{V_{Th}}{R_{Th}}$$

*[added] **Arithmetic verified.** $20\times200/300 = 13.3\overline{3}$ ✓ · $200\times100/300 = 66.6\overline{6}$ ✓ ·
$13.33/66.67 = 0.19999 \to 0.2$ ✓. The three numbers are internally consistent.*

> ⚠ VERIFY **JC4.5** ·J p39 — the Thevenin voltage is printed **"= 13.33 Ω"**. It is a **voltage**:
> $13.33\ \mathrm{V}$. The expression $20\ \mathrm{V}\times200\,\Omega/300\,\Omega$ has units of
> volts. Nothing computed changes; the same number is used correctly on the next page as the
> $V_D$-axis intercept. See `_verification-log.md`.

> **The physics flag on this example is JV4.6, §4.8.** The intercept $0.2\ \mathrm{A}$ omits the
> $500\ \Omega$ load. The correct current-axis intercept for **this** circuit is
> $$I_D\big|_{V_D=0} = \frac{13.33}{66.67 + 500} = 23.5\ \mathrm{mA}$$
> The $13.33\ \mathrm{V}$ intercept is unaffected.

[fig ·J p40] **The resulting plot.** Axes $I_D$ up, $V_D$ right. The vertical axis is ticked
**0.2** near the top, and the **DC loadline** runs from that tick down to the horizontal axis at the
tick **13.33**. The diode's VI characteristic rises steeply from near the origin and crosses the
load line at the marked **Q point**, with dashed construction lines to $V_{DQ}$ and $I_{DQ}$.
Finally $r_{dc} = V_{DQ}/I_{DQ}$ is restated beneath the figure.

**What the notes stop short of.** ·J p40 gives no diode characteristic with real numbers on it, so
**$V_{DQ}$ and $I_{DQ}$ are never evaluated** and neither is $r_{dc}$. The example teaches the
*construction*, not a number.

*[added] **What the Q point would actually be.** With the correct load line
($V_{Th} = 13.33\ \mathrm{V}$, total series resistance $566.67\ \Omega$) and a silicon diode
($I_o = 1\ \mathrm{pA}$, $\eta = 2$, $V_T = 25.85\ \mathrm{mV}$), solving the load line against the
diode equation numerically gives*

$$V_{DQ} = 1.23\ \mathrm{V},\qquad I_{DQ} = 21.4\ \mathrm{mA},\qquad r_{dc} = \frac{1.23}{0.0214} = 57.6\ \Omega$$

*Using the notes' $66.67\ \Omega$ load line instead gives $V_{DQ} = 1.34\ \mathrm{V}$,
$I_{DQ} = 180\ \mathrm{mA}$ — an operating current eight times larger, and past the rating of most
small-signal diodes. This is why JV4.6 matters. Both figures are ours, not the notes'.*

---

## 4.12 [ex] Worked example — power in the 20 Ω resistor ·J p40–p41

> ⚠ REDACTED ·J p40 — an opaque block (106 px, at heading weight) sits alone on the line immediately
> above this circuit, where an example label belongs.
>
> *[added] The covered word is **"Example"** with high confidence: the block is at heading weight,
> stands alone on its own line, is followed by a circuit and a question, and the matching bold
> **"Solution"** label appears below the circuit. The identical pattern — bold *Example* … bold
> *Solution* — is used on ·J p32 and elsewhere in the document. This is our inference, not the
> notes' word.*

**Statement.** ·J p40 **Calculate the dissipation of power in the 20 Ω resistor.**
Take germanium $r_f = 1\ \Omega$ and silicon $r_f = 2\ \Omega$.

[fig ·J p40] **The circuit.** A $20\ \mathrm{V}$ supply on the left leg. Along the top wire: a
$10\ \Omega$ resistor, then the current arrowed into a diode $D$ labelled **Ge**, then a
$20\ \Omega$ resistor, arriving at node **N**. From **N** two branches run down to the bottom rail
in parallel:

- the left branch is a silicon diode $D_2$ alone (triangle pointing **down**, so forward from N to
  the rail);
- the right branch is a silicon diode $D_3$ (also pointing down) **in series with a $50\ \Omega$
  resistor**.

**Solution** ·J p41 — each diode is replaced by its **approximate model**: a battery $V_o$ in series
with $r_f$.

[fig ·J p41] **Equivalent circuit, step 1.** The same topology with every diode expanded: the Ge
diode becomes $0.3\ \mathrm{V}$ + $1\ \Omega$ in the top wire; each Si branch becomes
$0.7\ \mathrm{V}$ + a forward resistance + an ideal diode, with the $50\ \Omega$ still below $D_3$.

> ⚠ VERIFY **JV4.7** ·J p41 — in this equivalent-circuit figure **both silicon forward resistances
> are labelled $20\ \Omega$**. The statement of the problem on ·J p40 gives $\mathrm{Si}: r_f = 2\ \Omega$,
> and the arithmetic immediately underneath the figure uses **2 Ω**. Correct label:
> $$\boxed{\;r_f(\mathrm{Si}) = 2\ \Omega\ \text{in both branches}\;}$$
> **Why, from the notes' own next line.** The page computes the parallel combination as
> $52\times2/(52+2)$ — that is the $D_3$ branch ($2 + 50 = 52\ \Omega$) in parallel with the $D_2$
> branch ($2\ \Omega$). Neither number is available if $r_f = 20\ \Omega$.
> **What the mislabel would cost:** with $20\ \Omega$ the branches become $20$ and $70\ \Omega$,
> the parallel value $15.56\ \Omega$, $R_t = 46.56\ \Omega$, $I_t = 0.408\ \mathrm{A}$ and
> $P_{20\Omega} = 3.33\ \mathrm{W}$ — exactly **half** the notes' own answer. Substantive, because a
> reader redrawing from the figure gets the wrong result. See `_verification-log.md`.

**Step 1 — combine the two silicon branches.** ·J p41

$$R_{D2\parallel D3} = \frac{52\times 2}{52+2} = 1.926\ \Omega$$

*[added] Verified: $104/54 = 1.9259$ ✓. Exactly $52/27\ \Omega$.*

**Step 2 — the equivalent potential drops.** ·J p41 The equivalent potential drop across the silicon
diodes is **0.7 V** — the two parallel branches share one node pair, so one $0.7\ \mathrm{V}$ step
appears once in the loop, not twice.

[fig ·J p41] **Equivalent circuit, step 2 — one series loop.** $20\ \mathrm{V}$ source; along the
top, $10\ \Omega$, then a battery $0.3\ \mathrm{V}$, then $1\ \Omega$, then $20\ \Omega$; down the
right leg a battery $0.7\ \mathrm{V}$ and then a resistor labelled $1.962\ \Omega$ (see JC4.6).

**Step 3 — solve the loop.** ·J p41

$$R_t = 10 + 1 + 20 + 1.926 = 32.926\ \Omega$$

$$V_{Rt} = 20 - 0.3 - 0.7 = 19\ \mathrm{V}$$

$$I_t = \frac{V_{Rt}}{R_t} = \frac{19}{32.926} = 0.577\ \mathrm{A}$$

$$P_{20\Omega} = I_t^{2}R = (0.577)^{2}\times 20 = \boxed{\;6.66\ \mathrm{W}\;}$$

*[added] **Every step recomputed and confirmed.***

- *$52\times2/54 = 1.92593\ \Omega$ ✓*
- *$10+1+20+1.92593 = 32.92593\ \Omega$ ✓ (exactly $889/27$)*
- *$19/32.92593 = 0.577053\ \mathrm{A}$ ✓ (exactly $513/889$)*
- *$0.577053^2 \times 20 = 6.6598\ \mathrm{W}$ ✓; using the notes' rounded $0.577$ gives
  $6.6586\ \mathrm{W}$. Either way **6.66 W**.*

*[added] **Independent check by node voltages**, without lumping anything. Let $V_N$ be the voltage
at node N above the bottom rail. Then*

$$\frac{20 - 0.3 - V_N}{10+1+20} = \frac{V_N - 0.7}{2} + \frac{V_N - 0.7}{52}$$

$$V_N = 1.8114\ \mathrm{V},\qquad I_t = 0.577053\ \mathrm{A},\qquad P_{20\Omega} = 6.6598\ \mathrm{W}\ ✓$$

*Both silicon branch currents come out positive — $I_{D2} = 555.7\ \mathrm{mA}$,
$I_{D3} = 21.4\ \mathrm{mA}$ — so the assumption that **all three diodes conduct** is self-consistent,
which is the check the notes never make and which is where marks are usually lost in this kind of
question. The drop across the $20\ \Omega$ resistor is $11.54\ \mathrm{V}$.*

> ⚠ VERIFY **JC4.6** ·J p41 — the second equivalent-circuit figure labels the combined branch
> resistance **1.962 Ω**; the value computed on the line above it, and used in $R_t = 32.926$, is
> **1.926 Ω**. A digit transposition in the figure only. Using 1.962 gives $R_t = 32.962\ \Omega$,
> $I_t = 0.5764\ \mathrm{A}$, $P = 6.645\ \mathrm{W}$ — the answer moves in the fourth significant
> figure and the printed 6.66 W is unaffected. See `_verification-log.md`.

> ⚠ VERIFY **JC4.7** ·J p41 — the current line is typeset as
> $I_t = \dfrac{V_{Rt}}{R_t} = \dfrac{19}{32}.926 = 0.577\,\mathrm{A}$: the equation editor has split
> the denominator, leaving $32$ under the bar and $.926$ stranded beside it. It should read
> $19/32.926$. Read literally, $19/32 = 0.594$, not $0.577$. Nothing in the result changes.
> See `_verification-log.md`.

**[exercise] [added] — the same circuit, one step further.** *Not in the notes.* Using the values
above, find the power dissipated in the $50\ \Omega$ resistor, and confirm the power balance.

*[added] **Solution.** $I_{D3} = (V_N - 0.7)/52 = 21.372\ \mathrm{mA}$, so*

$$P_{50\Omega} = I_{D3}^{2}\times 50 = (0.021372)^{2}\times 50 = 22.8\ \mathrm{mW}$$

*Power balance: source delivers $20 \times 0.577053 = 11.541\ \mathrm{W}$; the $10\ \Omega$ takes
$3.330\ \mathrm{W}$, the Ge model takes $0.3\times0.577 + 1\times0.577^2 = 0.506\ \mathrm{W}$, the
$20\ \Omega$ takes $6.660\ \mathrm{W}$, and the parallel silicon section takes
$0.7\times0.577 + 1.926\times0.577^2 = 1.045\ \mathrm{W}$. Sum $= 11.541\ \mathrm{W}$ ✓.*

---

## 4.13 Types of diodes — (a) the LED ·J p41–p42

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_f$ | forward current through the LED | A (mA) | 10–20 mA |
| — | forward voltage rating | V | 1–3 |
| — | luminosity (light output power) | mW | few mW |

[def] A **light-emitting diode (LED)** is a diode which **emits light when a forward voltage is
applied across it**. It is a **transducer**, converting **electrical** energy to light energy.
·J p41–p42

> ⚠ VERIFY **JC4.8** ·J p41 — printed: *"It is a transducer which changes **bacterial** energy to
> light energy."* Read **electrical**. The same page's application list on ·J p42 settles it —
> item 3 reads *"since it converts **electrical** energy to light energy"*. Nothing computed
> changes. See `_verification-log.md`.

[fig ·J p41] **LED circuit symbol.** The standard diode symbol — triangle pointing right into a
vertical bar — with **two short arrows above it pointing up and to the right, away from the
device**, indicating emitted light.

**Construction** ·J p41 — it is constructed from materials that produce **different colours
depending on the material used**.

> ⚠ REDACTED ·J p41 — **two** opaque blocks (198 px and 217 px, roughly 19 and 21 characters each)
> destroy the sentence *"It is constructed using materials such as ▮ and ▮."* The two covered items
> are LED semiconductor material names.
>
> **Not recovered.** The block widths rule out bare formula abbreviations (GaAs is four characters)
> and are consistent with spelled-out compound names, but **which** two cannot be determined. The
> tier-2 file `11-diodes.md` §1.11 gives the standard three — **gallium arsenide (GaAs)**, **gallium
> phosphide (GaP)** and **gallium arsenide phosphide (GaAsP)** — of which any two would fit. That is
> a different source, not a reconstruction of this sentence, and no guess is made here.
> **If this material is examined, ask for a clean copy of ·J p41.**

> ⚠ REDACTED ·J p42 — an opaque block (301 px, at heading weight) sits at the **very top of the
> page**, above the bold heading *Operation*, i.e. between *Construction* on the previous page and
> *Operation*.
>
> **Not recovered.** The photodiode, tunnel-diode and varactor sections that follow all run
> *Construction → Operation* with nothing between them, so there is no parallel passage to infer
> from, and the block is too wide (roughly two to three words at heading weight) to guess. **Ask for
> a clean copy of ·J p42.**

**Operation** ·J p42:

- The LED is operated in **forward-bias mode**.
- When forward voltage is applied, **electrons in the conduction band move to the valence band to
  fill the holes**.
- **In the process they emit light energy.**

[fig ·J p42] **Characteristic curve.** Vertical axis **Luminosity (mW)**, horizontal axis
$I_f\ \mathbf{(mA)}$, origin marked 0. The trace is a **single straight line rising from the origin**
at constant slope. No tick values on either axis, and no curvature or roll-off is drawn.

> ⚠ VERIFY **JV4.8** ·J p42 — the luminosity characteristic is drawn as an **exact straight line
> through the origin**, which asserts strict proportionality $L \propto I_f$ over the whole range.
> Real LED output is **sub-linear**: it rises close to linearly at low current, then flattens and
> ultimately **droops** as junction heating and non-radiative recombination take over. Correct
> statement:
> $$\boxed{\;L \text{ increases \textbf{monotonically but sub-linearly} with } I_f,\ \text{saturating at high current}\;}$$
> **Why it matters, and a check.** Proportionality would mean an LED run at 10× its rated current
> gives 10× the light — it gives rather less, and then fails. The tier-2 file's own figure
> (Fig. 53.3(b), ·L1 p14) plots the measured curve: ≈1.8 mW at 50 mA, ≈2.8 mW at 100 mA,
> ≈3.4 mW at 150 mA — doubling the current from 50 to 100 mA raises the output by a factor of 1.6,
> not 2. **This is a genuine disagreement between the two sources' figures**, and the tier-2 figure
> is the physical one; see §4.18. Within the LED's normal 10–20 mA operating window the straight
> line is a fair approximation, which is presumably the intent. See `_verification-log.md`.

**Ratings** ·J p42

$$\text{Voltage rating: } 1\text{–}3\ \mathrm{V};\qquad \text{Current rating: } 10\text{–}20\ \mathrm{mA}$$

> ⚠ VERIFY **JC4.9** ·J p42 — the current rating is printed **"20 – 10mA"**, written from the larger
> value to the smaller. Read it as **10–20 mA**. Nothing computed changes; both endpoints are the
> conventional ones. See `_verification-log.md`.

**Applications** ·J p42

1. **Digital displays**, e.g. seven-segment.
2. **Indicators** (power).
3. **Networks (fibre optics)**, since it converts electrical energy to light energy.

---

## 4.14 (b) The photodiode ·J p42–p43

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_R$ | reverse current (the photocurrent) | A (µA) | µA |
| $V_R$ | applied reverse voltage | V | 5–20 |
| $E$ | incident light intensity (irradiance) | mW cm$^{-2}$ | — |
| $R_R$ | dark resistance | Ω | MΩ range |

[def] A **photodiode** is a diode made from a **photoconducting material such as germanium** which
**changes light energy to electric energy**. It is therefore a **transducer** — the LED's inverse.
·J p42

[fig ·J p42] **Photodiode circuit symbol.** The diode symbol with **two short arrows above it
pointing down and to the left, in towards the device** — incident light. (Contrast the LED, whose
arrows point away.)

**Construction** ·J p42:

- Made from **p-type and n-type semiconductors which are sensitive to light energy**.
- They have a **large surface area** compared with normal diodes — more junction exposed to the
  light.

**Operation** ·J p42:

- The doping is **higher than other diodes**, stated as being to **increase the reverse-bias
  current**.
- It is **always operated in reverse bias**.
- When a reverse voltage is applied, **electrons move from the valence band to the conduction band**,
  increasing the conductivity of the material.
- **These are minority charge carriers.**

> ⚠ VERIFY **JV4.9** ·J p42 — printed: *"Doping is higher than other diodes to increase reverse bias
> current."* Real photodiodes go the other way. Correct statement:
> $$\boxed{\;\text{the active region of a photodiode is \textbf{lightly} doped — commonly an intrinsic layer (the PIN structure) — to \textbf{widen} the depletion region}\;}$$
> **Why.** The photocurrent is produced by electron–hole pairs generated **inside the depletion
> region**, where the field sweeps them apart before they recombine. Depletion width falls as doping
> rises, so heavy doping *shrinks* the light-collecting volume and cuts the responsivity. Heavy
> doping also raises the **dark current**, which is the photodiode's noise floor and the one number
> every datasheet minimises — so "increase reverse bias current" describes the parameter you want
> *smaller*, not larger. See `_verification-log.md`.

> ⚠ VERIFY **JV4.10** ·J p42 — printed: *"When a reverse voltage is applied electrons move from the
> valence band to the conduction band increasing the conductivity of the material."* As written, the
> **applied voltage** is the agent of band-to-band excitation, and **light is never mentioned in the
> operating mechanism at all** — in the description of a *photo*diode. Correct statement:
> $$\boxed{\;\text{\textbf{absorbed photons} of energy } h\nu \ge E_g \text{ generate the electron–hole pairs; the reverse bias merely \textbf{sweeps them out} as photocurrent}\;}$$
> **Why, from the notes' own next page.** ·J p43's first figure plots $I_R$ against **light
> intensity $E$** as a line through the origin: **zero light, zero photocurrent**, whatever the
> reverse voltage. If the applied voltage caused the excitation, that line would not pass through
> the origin. The page's own **dark current** — the current that flows *with no light* — is the small
> residue left when the photo-generation is switched off. See `_verification-log.md`.

[fig ·J p43] **Characteristic curve 1 — response to light.** Vertical axis $I_R\ \mathbf{(µA)}$,
horizontal axis $E$ **(light Intensity) (mW/cm²)**, origin marked 0. A **straight line rising from
the origin** — photocurrent proportional to irradiance.

[fig ·J p43] **Characteristic curve 2 — the reverse output family.** Vertical axis
$I_R\ \mathbf{(µA)}$, horizontal axis $V_R$, origin marked 0. **Four curves**, each rising steeply
from the origin and then **flattening to a horizontal plateau** at a level of its own. A separate
vertical arrow to the right of the family is labelled **light Intensity**, pointing **up**: higher
curves correspond to greater illumination.

**Read the family.** In the plateau region the photocurrent is set by the **light**, not by $V_R$ —
which is exactly what makes a reverse-biased photodiode a good light-controlled *current source*.

[eq: photodiode-dark-current] **Dark current** ·J p43

$$\boxed{\;I_R = \frac{V_R}{R_R}\;}$$

- $I_R$ — dark current, the reverse current flowing with **no illumination**, A
- $V_R$ — applied reverse voltage, V
- $R_R$ — **dark resistance**, Ω

**Applications** ·J p43

1. **Automatic switching systems**
2. **Alarm circuits**
3. **Fibre-optic networks**, to change light energy to electric energy
4. **Counting**

**Factors affecting the photodiode's reverse current** ·J p43

1. **Light intensity**
2. **Applied voltage**
3. **Material of the photodiode**
4. **Surface area**

> ⚠ VERIFY **JC4.11** ·J p43 — this list is headed *"Factors affecting light intensity"*, and its
> **first item is "Light intensity"**. A quantity cannot be a factor affecting itself. From the four
> items and their position — immediately after the dark-current equation and the $I_R$ curves — the
> heading should read **"Factors affecting the (reverse) photocurrent $I_R$"**. Nothing computed
> changes. *[added] Note also that item 2, "applied voltage", is only weakly true: the page's own
> second figure shows $I_R$ **flat** against $V_R$ across the whole plateau, so beyond the initial
> knee the applied voltage is very nearly irrelevant.* See `_verification-log.md`.

---

## 4.15 (c) The tunnel diode ·J p43–p44

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_p$ | peak current | A (mA) | mA |
| $I_v$ | valley current | A (mA) | a fraction of $I_p$ |
| $V_p$ | peak-point voltage | V | ≈ 50–100 mV |
| $V_v$ | valley-point voltage | V | ≈ 300–500 mV |

[def] A **tunnel diode** is a diode which **exhibits negative resistance between two points of
forward voltage**. ·J p43

[fig ·J p43] **Tunnel-diode circuit symbol.** A horizontal wire carrying a triangle pointing right
into a vertical cathode bar, with a **short stub bent back from the bar towards the anode** — the
standard tunnel-diode modification of the diode symbol.

**Construction** ·J p43:

- It is **very highly doped**.
- Heavy doping makes the **depletion layer very small**.
- As a result electrons can **move across the junction with minimal voltage applied, or none at
  all**.
- This is the **tunnelling effect**.

[fig ·J p44] **The negative-resistance characteristic — the figure this device exists for.** Vertical
axis $I_f$, horizontal axis unlabelled (forward voltage), origin marked 0. The trace rises steeply
from the origin to a **local maximum**, falls away to a **local minimum**, and then turns up again
and climbs steeply like an ordinary diode. Dashed construction lines mark the maximum at height
$I_p$ over abscissa $V_p$, and the minimum at height $I_v$ over abscissa $V_v$, with the four
labels on the axes. **Between $V_p$ and $V_v$ the current falls as the voltage rises** — that
descending stretch is the negative-resistance region.

**Operation** ·J p44:

1. Forward voltage applied — the **tunnelling effect** produces an **increment of current** up to
   the first turning point.
2. After that the **tunnelling effect reduces**, which leads to a **decrement of current** down to
   the second turning point.
3. Further increase of voltage from that point gives a **corresponding increment of current** — the
   diode now behaves like a **normal diode**.

> ⚠ REDACTED ·J p44 — **two** opaque blocks (118 px ≈ 11 characters, and 134 px ≈ 13 characters)
> destroy the names of the two turning points: *"…an increment of current up to a ▮. After that the
> tunneling effect reduced which leads to a decrement of current up to a ▮."*
>
> *[added] The covered terms are **peak point** and **valley point**, in that order. The inference is
> as certain as it can be without the page: the figure directly above the sentence labels its maximum
> $I_p$ over $V_p$ and its minimum $I_v$ over $V_v$ — the subscripts $p$ and $v$ **are** peak and
> valley — and the two phrases are 10 and 12 characters, matching the two block widths. These are
> our words, not the notes'.*

**Applications** ·J p44

1. **Oscillators**, e.g. in tuning circuits
2. **Fast switches**

*[added] **Why negative resistance gives an oscillator.** Over the descending stretch,
$\Delta I/\Delta V < 0$, so the device **supplies** power to a signal instead of absorbing it. Put it
across a tuned $LC$ circuit biased into that region and it cancels the tank's loss resistance,
sustaining oscillation. The same steep tunnelling current is what makes it fast — tunnelling has no
carrier transit delay, so tunnel diodes switch in picoseconds.*

---

## 4.16 (d) The varactor diode ·J p44–p45

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $C$ | junction capacitance | F (pF) | 5–100 pF |
| $\varepsilon$ | permittivity of the junction material | F m$^{-1}$ | — |
| $A$ | junction (plate) area | m² | — |
| $d$ | depletion-layer width — the plate separation | m | µm |
| $V_R$ | applied reverse voltage | V | 1–30 |
| $f_r$ | resonant frequency of the tuned circuit | Hz | — |
| $L$ | tuning inductance | H | — |

[def] A **varactor diode** is a diode which **behaves like a variable capacitor**. ·J p44

[fig ·J p44] **Varactor circuit symbol.** The diode triangle pointing right into its bar, with a
**second, curved plate drawn just beyond the bar**, facing it — the diode symbol with a capacitor
grafted onto the cathode.

**Construction** ·J p44 — the device *is* a parallel-plate capacitor:

- the **p-type and n-type semiconductors act as the plates**;
- the **P–N junction acts as the dielectric**;
- the **length of the junction** is the **distance between the plates**.

[fig ·J p44] **Construction diagram.** A horizontal wire through a rectangular block split into two
cells, **P** left and **N** right. A leader from above labels the cells **Plate**. A leader from
below left labels the boundary region **Dielectric materials**, and an arrow points up at the same
boundary labelled **Depletion Layer**.

**Operation** ·J p44:

- Operated in **reverse-bias mode**.
- **Increase the reverse-bias voltage → the depletion layer thickens → the effective capacitance
  falls**, and vice versa.

[eq: varactor-plate-capacitance] ·J p44

$$\boxed{\;C = \frac{\varepsilon A}{d}\;}$$

- $C$ — junction capacitance, F · $\varepsilon$ — permittivity of the junction material, F m$^{-1}$ ·
  $A$ — junction area, m² · $d$ — depletion-layer width, m

**Read it with the operation statement:** $V_R\uparrow \Rightarrow d\uparrow \Rightarrow C\downarrow$.

*[added] The tier-2 file gives the same physics in its voltage-explicit form,
$C = K/\sqrt{V_R}$ ·L1 p7 — because for an abrupt junction $d \propto \sqrt{V_R}$, and substituting
that into $C = \varepsilon A/d$ gives exactly $C \propto 1/\sqrt{V_R}$. The two expressions are the
same statement; this document gives the geometry, the tier-2 file gives the voltage law.*

[fig ·J p45] **Capacitance against reverse voltage — note the unusual orientation.** The **vertical
axis is drawn on the right-hand side** of the frame, labelled **(capacitance)** at its top. The
horizontal axis runs from that vertical axis **leftward**, terminating in an **arrowhead on the
left** labelled $V_R$ — so **reverse voltage increases to the left**. The curve is low and nearly
flat at the far left (large $V_R$) and **sweeps steeply upward** as it approaches the vertical axis
on the right (small $V_R$). Reading it in the ordinary sense: **capacitance falls, and falls
increasingly slowly, as reverse voltage rises.**

**Applications** ·J p45 — **(a) tuning circuits, along with inductors.**

[eq: varactor-resonant-frequency]

$$\boxed{\;f_r = \frac{1}{2\pi\sqrt{LC}}\;}$$

- $f_r$ — resonance frequency, Hz · $L$ — inductance, H · $C$ — the varactor's capacitance, F

*[added] Verified as the standard $LC$ resonance formula. This is the whole point of the device: a
**dc** control voltage sets $C$, which sets $f_r$ — electronic tuning with no moving parts, which is
how a radio or TV front end selects a station. The notes list only this one application and give no
worked number.*

---

## 4.17 Formula summary for this range

[table] Everything in ·J p33–p45 that is worth carrying into an exam, in corrected form.

| Quantity | Relation | Source | Flag |
|---|---|---|---|
| Turn-on voltage | $V_o = 0.3\ \mathrm{V}$ (Ge), $0.6$–$0.7\ \mathrm{V}$ (Si) | ·J p34, p38 | — |
| Diode static equation | $i_D = I_o\!\left(e^{V_D/\eta V_T}-1\right)$ | ·J p35 | JV4.3 |
| Thermal voltage | $V_T = kT/q$, $k = 1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ | ·J p35 | JV4.2 |
| Ideality factor | $\eta = 1$ (Ge), $\eta = 2$ (Si) | ·J p35 | — |
| Thevenin voltage | $V_{Th} = V_S R/(R_S+R)$ | ·J p36 | JV4.5 |
| Thevenin resistance | $R_{Th} = R_S R/(R_S+R)$ | ·J p36 | — |
| Diode current (ideal model) | $I_D = V_{Th}/(R_L+R_{Th})$ | ·J p36 | — |
| Load-line intercepts | $V_D = V_{Th}$; $I_D = V_{Th}/(R_{Th}+R_L)$ | ·J p36, p40 | JV4.6 |
| Static resistance | $r_{dc} = V_{DQ}/I_{DQ}$ | ·J p37 | — |
| ac resistance | $r_{ac} = \Delta V_D/\Delta i_D$ | ·J p38 | — |
| Dark current | $I_R = V_R/R_R$ | ·J p43 | — |
| Varactor capacitance | $C = \varepsilon A/d$ | ·J p44 | — |
| Tuned-circuit frequency | $f_r = 1/\!\left(2\pi\sqrt{LC}\right)$ | ·J p45 | JC4.12 |

---

## 4.18 Cross-check against the tier-2 file `11-diodes.md`

`11-diodes.md` (source L1, 18 pp., fully verified) covers the same junction-diode ground from a
textbook compilation. **Six specific comparisons, as checked page against page.**

[table] **Where the two sources agree**

| Point | This document (·J) | Tier 2 (·L1) | Verdict |
|---|---|---|---|
| **Position of the $-1$** | **outside** the bracket: $I_o(\ldots - 1)$ ·J p35 | printed **inside the exponent** in four highlighted forms, ·L1 p7–p8 — flagged **V1.3** | **·J is right, ·L1 is wrong.** Use this document's placement |
| **Ideality factor** | $\eta$ present in the master equation; $\eta = 1$ Ge, $\eta = 2$ Si ·J p35 | $\eta$ **dropped** from the highlighted master equation — flagged **V1.2** — but the same 1/2 assignment ·L1 p6 | **Values agree exactly; ·J's equation is the better-formed one** |
| **Thermal voltage — definition** | $V_T = kT/q$ ·J p35 | $V_T = kT/e = T/11{,}600$ ·L1 p3, p6 | agree ($q \equiv e$) |
| **Ge / Si turn-on** | 0.2–0.3 V and 0.6–0.7 V ·J p34; $V_o = 0.3$ V and 0.6–0.7 V ·J p38; figure ticked 0.2 V, 0.7 V ·J p34 | $V_B = 0.3$ V (Ge), 0.7 V (Si) ·L1 p5 | agree |
| **Reverse leakage** | flat with $V_R$, minority-carrier, temperature-sensitive ·J p34–p35 | $I_0$ independent of $V_R$; depends on temperature, doping, junction size ·L1 p5 | agree; ·L1 fuller |
| **Varactor** | $C = \varepsilon A/d$, $C$ falls as $V_R$ rises ·J p44 | $C = K/\sqrt{V_R}$ ·L1 p7 | agree — the same law, geometry form vs voltage form |

[table] **Where the two disagree**

| Point | This document (·J) | Tier 2 (·L1) | Which to teach |
|---|---|---|---|
| **Boltzmann's constant** | $1.38\times10^{-28}\ \mathrm{J/K}$ ·J p35 — **JV4.2** | $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ ·L1 p3, and evaluates $V_T$ | **·L1.** ·J is wrong by $10^5$ |
| **Value of $V_T$** | never evaluated | 26 mV at 300 K, 25 mV at 293 K ·L1 p3, p7 | **·L1** — the only source that gives a number |
| **The exponent itself** | typeset as a **denominator**, $V_D/e^{\eta V_T}$ ·J p35 — **JV4.3** | correct exponential form (its defect is the $-1$, not the exponent) | **·L1's exponent + ·J's $-1$** = the correct equation |
| **LED luminosity vs $I_f$** | drawn as an **exact straight line through the origin** ·J p42 — **JV4.8** | text claims "directly proportional" (flagged **V1.6**) but its **figure plots a saturating curve** ·L1 p14 | **·L1's figure.** The claim is wrong in both; only ·L1 draws it honestly |

[table] **Where each source is the only one**

| Topic | Only in | Note |
|---|---|---|
| **dc load line and Q point** | **·J** (this file, §4.8, §4.11) | ·L1 names the load line in its outline and **never draws it** — `11-diodes.md` §1.14 supplies one marked `[added]`. **This document closes that gap from the primary source.** |
| **Tunnel diode** | **·J** (§4.15) | ·L1 names tunnel diodes in its outline and never covers them — logged as an open gap in `00-index.md`. **Closed here.** |
| **Photodiode** | **·J** (§4.14) | absent from ·L1 entirely |
| **The three diode models** | **·J** (§4.10) | ·L1 has an "equivalent circuit of a p-n junction" (§1.13) but not the approximate/simplified/ideal hierarchy |
| **Thevenin reduction of a diode circuit** | **·J** (§4.7) | ·L1 has no such treatment |
| **Zener diode, Zener/avalanche mechanisms, voltage regulation** | **·L1** | **See below** |
| **Bulk resistance $r_B$, junction resistance $r_j = 25/I_F$ mV/mA** | **·L1** (§1.6) | ·J teaches $r_{ac}$ graphically only |
| **Barrier-voltage formula $V_B = V_T\ln\!\left(N_a N_d/n_i^{2}\right)$, temperature coefficient** | **·L1** (§1.3) | ·J gives the barrier qualitatively and one number, 0.3 V |
| **LED construction detail, materials table, seven-segment displays** | **·L1** (§1.11) | ·J's material names are destroyed by redaction — see §4.13 |

> ### ⚠ Breakdown and Zener regulation — go to the tier-2 file
>
> This range treats breakdown in **one paragraph** (·J p35): avalanche only, no Zener mechanism, no
> Zener diode, no regulator. It also equates breakdown voltage with PIV (**JV4.4**).
>
> **`11-diodes.md` §1.8–§1.10 is the fuller treatment and the only source for:** the two distinct
> breakdown mechanisms and the voltage at which each dominates; the Zener characteristic, symbol and
> equivalent circuits; the three-point Zener biasing check; the regulator relations; and **four
> worked regulator examples** (54.1, 54.2, 54.3, 54.5–54.7). Work from that file for anything
> involving a Zener.

---

## 4.19 Coverage, emphasis and exam triage

**What this range is.** Thirteen pages, of which **roughly half is circuit analysis with numbers**
(·J p35–p41) and half is descriptive device material (·J p33–p34 and p41–p45). That balance should
set the study balance.

**Highest exam value — work these until they are automatic:**

1. **The Thevenin-then-load-line procedure** (§4.7, §4.8, §4.11). It is set up over two pages, stated
   as a rule, and then executed on numbers. It is also the exact procedure reused for the BJT dc load
   line in `13-bipolar-junction-transistor.md`.
2. **The multi-diode network** (§4.12). A complete, self-contained numerical question with a clean
   answer (6.66 W) and a mixed Ge/Si population — the shape of question a CAT lifts verbatim.
3. **The three diode models and the two turn-on voltages** (§4.10). Every subsequent rectifier
   calculation picks one of the three.
4. **Redrawing the static characteristic** (§4.5) with both knees, the leakage region and breakdown
   labelled.

**Moderate value — know the statements, know the figures:**

5. The **four special diodes** (§4.13–§4.16). Each is a symbol, a construction sentence, an operating
   sentence, one characteristic curve and a two-to-four-item application list. Examinable as short
   descriptive questions; the **tunnel-diode negative-resistance curve** and the **varactor
   $C$–$V_R$ curve** are the two most likely to be asked for as sketches.
6. The **diode static equation** (§4.6) — quotable, but this document never uses it in a calculation.

**Low value here:**

7. The depletion-layer formation narrative (§4.2) — covered more carefully, and with the barrier
   formula, in `11-diodes.md` §1.2–§1.3.

**Two things this range does not teach at all:** the **Zener diode and voltage regulation**, and any
**numerical use of the diode equation**. Both are in the tier-2 file.

---

## 4.20 Typography and word slips, collected

> ⚠ VERIFY **JC4.13** — spelling and word-substitution slips across ·J p33–p45, gathered here because
> none of them changes anything computed. Listed so a reader meeting them on the page knows they are
> the source's, not a misreading.
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·J p33 | "electrons … adjacent to the p – type semi conductor **more** to fit in the holes" | move |
> | ·J p33 | "The movement of ions process is called diffusion" | see **JV4.1** — the carriers move, not the ions |
> | ·J p41 | "changes **bacterial** energy to light energy" | electrical (see **JC4.8**) |
> | ·J p43 | "A tunnel diode is a diode **exhibits** negative resistance" | a diode **which** exhibits |
> | ·J p44 | "there will **an** increment of current" | there will **be** an increment |
> | ·J p44 | "the diode **stars** behaving like a normal diode" | starts |
> | ·J p44 | "P – N junction as the **electric** material" | **dielectric** — the same figure's own label reads "Dielectric materials" |
> | ·J p45 | "Tuning circuit **log** with inductors" | **along** with inductors |
>
> See `_verification-log.md`.

> ⚠ VERIFY **JC4.12** ·J p45 — the resonance formula is printed $f_r = \dfrac{1}{2\Pi\sqrt{LC}}$
> with a **capital Greek Pi** where the constant $\pi$ is meant. Capital $\Pi$ is the product
> operator. Correct form:
> $$\boxed{\;f_r = \frac{1}{2\pi\sqrt{LC}}\;}$$
> Nothing computed changes. See `_verification-log.md`.

---

## 4.21 Items needing a clean page

Listed for the record; everything else in ·J p33–p45 is fully recovered.

| Item | Page | Status |
|---|---|---|
| The section heading above the diode symbol | ·J p33 | **lost with the blank space** — not a redaction. Never fill it |
| Two LED material names | ·J p41 | ⚠ REDACTED — **not recovered**; needs a screenshot of ·J p41 |
| A heading between *Construction* and *Operation* | ·J p42 | ⚠ REDACTED — **not recovered**; needs a screenshot of ·J p42 |
| "Characteristic Curve" heading | ·J p43 | ⚠ ILLEGIBLE — clipped by the page margin; inferred with high confidence, see **JC4.10** |

> ⚠ VERIFY **JC4.10** ·J p43 — the heading at the top of the page survives only as the bottom two or
> three pixel rows of its glyphs, clipped by the page break. Word-shape gives two words of roughly 14
> and 5 characters, and the same heading in the same position occurs in the LED section (·J p42) and
> the varactor section (·J p45), so it is **"Characteristic Curve"**. Recorded as an inference.
> Nothing computed changes. See `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
