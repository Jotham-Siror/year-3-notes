---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "03 — Capacitors, Inductors and Transformers"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 24-32"
pages: "J p24-p32"
tier: primary
file_role: topic
subtopics:
  - "what a capacitor is; capacitance, the farad, and the three factors that set it"
  - "the parallel-plate formula and the permittivity constants"
  - "capacitor circuit symbols: non-polarised and electrolytic"
  - "charging and discharging — the two pages the document has lost"
  - "capacitors in series: common charge, reciprocal-sum capacitance"
  - "capacitors in parallel: common voltage, direct-sum capacitance"
  - "energy stored in a capacitor in its three equivalent forms"
  - "capacitive reactance and why a capacitor blocks dc"
  - "what capacitors are used for"
  - "non-electrolytic types: ceramic, film, mica, paper-foil"
  - "electrolytic types: aluminium and tantalum (foil, wet-slug, solid)"
  - "inductors: circuit symbol, the henry, and the four factors that set inductance"
  - "self-inductance and mutual inductance as the notes define them"
  - "transformers: construction, mutual induction, the 180-degree phase claim"
  - "ideal versus practical transformer; efficiency and the four loss mechanisms"
  - "step-up and step-down construction"
  - "the transformation ratio and the 400:2000-turn worked example"
key_equations: [parallel-plate-capacitance, charge-voltage, capacitors-series, capacitors-parallel, capacitor-energy, capacitive-reactance, rc-charging, rc-discharging, ideal-transformer-power, transformer-efficiency, transformation-ratio, self-inductance-emf, inductor-energy, inductive-reactance]
prerequisites: ["basic circuit theory: charge, potential difference, Kirchhoff's laws", "ac quantities: frequency, rms, phase", "02 — resistors and the passive-component catalogue (·J p18-p24)"]
leads_to: ["the diode section, which begins without a heading on ·J p33", "02-rectifiers (the reservoir capacitor, the smoothing filter and the supply transformer all assume this material)", "07-multistage-feedback-frequency-response (coupling and bypass capacitors, transformer coupling)"]
verification_flags: 20
tags: [capacitor, capacitance, permittivity, dielectric, series-capacitors, parallel-capacitors, capacitor-energy, capacitive-reactance, ceramic-capacitor, film-capacitor, mica-capacitor, electrolytic-capacitor, tantalum-capacitor, inductor, inductance, self-inductance, mutual-inductance, transformer, turns-ratio, transformation-ratio, transformer-efficiency, step-up, step-down, missing-pages]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·J pN = provenance (which PDF page of the lecture notes the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted, or content physically absent.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 03 — Capacitors, Inductors and Transformers

Scope: **·J p24–p32**, nine PDF pages of the course's own lecture notes. It defines capacitance and
the parallel-plate formula, gives the two combination rules, the stored-energy expression and
capacitive reactance, then runs a catalogue of capacitor types; it introduces the inductor in half a
page; and it closes on transformers — construction, phase, efficiency, step-up/step-down, the
transformation ratio and one worked example.

**This is the shortest self-contained block in the notes and the most damaged.** Three of the nine
pages have lost most or all of their body text, and the losses fall precisely on charging,
discharging and the opening of the transformer section. Read §3.0 before anything else.

---

## 3.0 What this file is, where the gaps are, and how to cite it

### Citation and the page offset

Citations are to the **PDF page**: ·J p27. The document's own printed page number runs **one
behind** — PDF p27 shows printed "26" — and the offset holds unbroken from PDF p2 (printed 1) to
PDF p100 (printed 99). Everything below cites PDF pages only.

### This is the only source for this material

[table] **Coverage of this topic across the three tiers**

| Tier | Documents | Covers capacitors / inductors / transformers as components? |
|---|---|---|
| 1 — primary | these notes, ·J p24–p32 | **Yes — and only here** |
| 2 — supporting | the seven lesson documents, L1–L7 | **No.** They *use* capacitors and transformers, but never teach them |
| 3 — reference | the four slide decks | not mapped to this topic |

**None of the seven tier-2 lesson documents covers capacitors, inductors or transformers as
components.** L2 puts a supply transformer in front of every rectifier and quotes a turns ratio; L7
uses coupling and bypass capacitors and a transformer-coupled amplifier stage; both assume the
reader already knows what these parts are and how they combine. Nothing in tiers 2 or 3 defines
capacitance, derives the series or parallel rule, gives the stored energy, defines inductance, or
sets out the transformer relations.

That matters because of the gaps below: **where these nine pages have lost content, there is no
second source in this knowledge base to fall back on.** Everything supplied to bridge a gap is
marked `[added]` and is standard textbook theory, not the lecturer's material.

### ⚠ The gap map — read this first

The losses were measured from the rendered pages, not guessed: the figures below are the actual
inked and blank bands on each page image.

[table] **What is physically missing from ·J p24–p32**

| Where | What survives | What is gone | Severity |
|---|---|---|---|
| ·J p25 | the sub-heading **"Charging"** and nothing else | the **entire body** of the page — roughly 57 text lines | severe |
| ·J p26 upper | nothing above the mid-page | the **top ~62 % of the text block** — the discharging figure and its explanation | severe |
| ·J p27 top | the parallel-capacitor figure | the section's **heading** | cosmetic |
| ·J p28 top | the first line of a paragraph in progress | the **"Film Capacitors" heading** | cosmetic |
| ·J p28 foot → p29 top | p29 opens mid-sentence at *"300 V dc."* | ~3 lines introducing **foil tantalum capacitors** | minor |
| ·J p29 foot | text stops ~10 lines short of the footer | whatever closed the inductor section | moderate |
| **·J p30** | **the footer alone — no body ink whatsoever** | **the whole of printed page 29** | **severe** |
| ·J p31 top | a transformer figure | the **`TRANSFORMERS` heading and its opening paragraph** | severe |
| ·J p32 foot | blank below the worked example | most likely the **`DIODES` heading** that ·J p33 lacks | cosmetic (next file) |

> ### ⚠ ILLEGIBLE ·J p25 — the charging page is empty
>
> The page carries the bold sub-heading **Charging** at the normal top-of-text position and then
> nothing at all until the footer. There is no faint ink under threshold: the body was not printed.
>
> **What is missing:** the capacitor charging circuit (a dc source, a series resistor, a switch and
> a capacitor), the charging curve of $v_C$ against time, and the explanation of the exponential
> approach to the supply voltage.
>
> **A screenshot would need to show:** printed page 24 in full, from the "Charging" heading down to
> the footer — the circuit diagram, the waveform with both axes labelled, and every line of text
> between them.
>
> §3.3 supplies the standard charging result in a clearly marked `[added]` block. It is **not** the
> notes' content.

> ### ⚠ ILLEGIBLE ·J p26 — the discharging half-page is empty
>
> The top of the text block down to about 62 % of its height carries **no ink of any kind**. The
> first mark on the page is the heading "Series Connection of Capacitors", roughly two-thirds of the
> way down.
>
> **What is missing:** the discharging sub-heading, the discharge circuit, the decay curve, and the
> text explaining it. The heading "Charging" on ·J p25 implies a matching "Discharging" heading,
> and it is not on either page.
>
> **A screenshot would need to show:** printed page 25 from the top margin down to the "Series
> Connection of Capacitors" heading.
>
> §3.4 supplies the standard discharging result in a clearly marked `[added]` block.

> ### ⚠ ILLEGIBLE ·J p30 — the page is blank
>
> **·J p30 carries no body ink at all.** Only the page footer is printed. Printed page 29 is missing
> outright — a full page of the course's notes.
>
> **What was almost certainly on it:** the `TRANSFORMERS` heading and the section's opening
> paragraph. Two independent pieces of evidence point that way. First, ·J p29's inductor section
> stops about ten lines short of its footer, so the following section began on a fresh page.
> Second, **·J p31 opens with a transformer construction diagram and no heading**, then launches
> straight into *"A transformer is a device which…"* — the heading that should sit above that figure
> is not on p31 either.
>
> Whether the lost page held only the heading and a paragraph, or a further half-page of inductor
> material (inductance formula, inductors in series and parallel, inductive reactance — none of
> which appears anywhere in these notes), **cannot be determined from the render.**
>
> **A screenshot would need to show:** printed page 29 in full.

**Nothing in this file is invented to paper over those gaps.** Where a value or a standard result is
needed downstream and the page that would have carried it is gone, it appears in an `[added]` block
that says so.

---

## 3.1 What a capacitor is ·J p24

[table] **Symbols for the capacitor sections**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $C$ | capacitance | F (farad) | pF to mF — see the note below |
| $Q$ | charge stored | C (coulomb) | µC to mC |
| $V$ | potential difference across the plates | V | 1–450 V |
| $\varepsilon_r$ | relative permittivity of the dielectric | dimensionless | 1 (air) to >3000 (high-K ceramic) |
| $\varepsilon_0$ | permittivity of free space | F/m | $8.854\times10^{-12}$ |
| $A$ | effective area of the plates | m$^2$ | mm$^2$ to m$^2$ (rolled foil) |
| $d$ | separation between the plates | m | µm or less |
| $E$ | energy stored | J | µJ to J |
| $X_c$ | capacitive reactance | $\Omega$ | see §3.9 |
| $f$ | frequency | Hz | 0 (dc) to MHz |

[def] A **capacitor** is a component built from conducting plates with a **dielectric** between
them, and it stores charge. **Capacitance** is a capacitor's ability to store charge, and it is
measured in **farads (F)**. ·J p24

The notes give **three factors** that set the capacitance. ·J p24

**(a) The dielectric material**, through its permittivity $\varepsilon$.

**(b) The plate area** — capacitance is directly proportional to the effective area of the plates:

$$C \propto A$$

**(c) The plate separation** — capacitance is inversely proportional to the distance between the
plates:

$$C \propto \frac{1}{d}$$

[eq: parallel-plate-capacitance] Putting the three together gives the parallel-plate formula the
notes print: ·J p24

$$\boxed{\;C = \varepsilon_r\,\varepsilon_0\,\frac{A}{d}\;}$$

**Reading it as an engineer.** Big plates, thin dielectric, high-permittivity filling — all three
push $C$ up. Every construction in the catalogue of §3.10–§3.12 is an attempt to win on one of
these three at acceptable cost: rolled foil buys area, etched foil buys more area still, and the
oxide film of an electrolytic buys an extremely small $d$.

### The permittivity constants ·J p24

$$\varepsilon_0 = 8.854\times10^{-12}\ \mathrm{F/m}
\qquad\text{or}\qquad
\varepsilon_0 \approx \frac{1}{36\pi}\times 10^{-9}\ \mathrm{F/m}$$

$\varepsilon_r$ is the **relative permittivity** — the factor by which a dielectric multiplies the
capacitance compared with a vacuum. It is dimensionless. The capacitor catalogue calls the same
number the **dielectric constant $K$** (·J p27); they are the same quantity under two names.

> ### ⚠ VERIFY **JV3.1** ·J p24 — permittivity is said to act on the magnetic field
>
> The page prints: *"Dielectric material (ε)- Permittivity is the ability of material to allow an
> electronic field to pass through, the extent to which a material affects magnetic field."*
>
> **Correct form.** Permittivity is an **electric** quantity:
>
> $$\varepsilon = \varepsilon_r\varepsilon_0 : \quad \mathbf{D} = \varepsilon\,\mathbf{E}$$
>
> The property that measures how a material affects the **magnetic** field is **permeability**
> $\mu$, and the notes themselves define it correctly five pages later, on ·J p29, in almost the
> same words: *"Permeability is the ability of a material to affect the magnetic field H."*
>
> **Why it matters.** A student who learns the p24 sentence will answer "permittivity" when asked
> which property governs a magnetic circuit, and will have no distinct idea left for $\mu$ when the
> inductor section arrives. The two sentences are five pages apart and say the same thing about two
> opposite quantities. See `_verification-log.md`.

> ⚠ VERIFY **JC3.1** ·J p24 — the same sentence prints *"electronic field"* where it means
> **electric field**. An electronic field is not a thing. See `_verification-log.md`.

> ⚠ VERIFY **JC3.2** ·J p24 — $\varepsilon_0$ is printed as $\dfrac{1}{36\Pi}\times\dfrac{10^{-9}\,\mathrm F}{\mathrm m}$, with a **capital $\Pi$** where $\pi$ is meant. The same substitution recurs in the reactance formula on ·J p27. Separately, the page joins the two values with "or" as though they were equal: $\frac{1}{36\pi}\times10^{-9} = 8.8419\times10^{-12}$, which is $0.14\,\%$ below $8.854\times10^{-12}$. It is the standard convenience approximation, not an identity. See `_verification-log.md`.

### [added] The defining relation the notes never state

The notes use $Q = CV$ twice — on ·J p26 to write $V = Q/C$ for each series capacitor, and on
·J p27 to write $Q_t = V_s(C_1+C_2+C_3)$ — but they never write it down as a definition. For
completeness:

[eq: charge-voltage]

$$\boxed{\;Q = C\,V\;}$$

- $Q$ — charge stored on either plate, C
- $C$ — capacitance, F
- $V$ — potential difference across the plates, V

**[added]** — this is standard theory supplied here; the notes assume it.

---

## 3.2 Capacitor circuit symbols ·J p24

[fig ·J p24] **Two symbols, drawn side by side beneath the permittivity line.**

**Left — labelled "Ceramic capacitor".** A horizontal lead comes in from the left and stops at a
**short vertical bar**; a small gap; a **second identical vertical bar**; a horizontal lead leaves
to the right. Two straight plates, perfectly symmetrical, no polarity marking.

**Right — labelled "electrolytic capacitor".** A horizontal lead comes in from the left and stops at
a **straight vertical bar**; a small gap; then a **curved bar, bowing away** from the straight one
(concave towards the right-hand lead); a horizontal lead leaves to the right. A **plus sign** sits at
the lower left, against the **straight** plate.

**How to read it.** The curved plate is the negative side; the straight plate carries the plus. An
electrolytic must be connected the right way round — reverse it and the oxide dielectric that makes
it work is destroyed. The two-straight-bar symbol carries no polarity and can go in either way.

> ⚠ VERIFY **JC3.3** ·J p24 — the two-straight-plate symbol is captioned **"Ceramic capacitor"**.
> It is the **general non-polarised fixed-capacitor** symbol, used for ceramic, film, mica, paper
> and any other unpolarised type; nothing about it is specific to ceramic. The caption is not wrong
> for a ceramic capacitor, but it is far narrower than the symbol's meaning, and a reader who takes
> it literally will look for a different symbol when a film capacitor appears in a circuit.
> See `_verification-log.md`.

---

## 3.3 Charging ·J p25 — the missing page

The page prints one word — the sub-heading **Charging** — and then nothing. See the gap map in
§3.0.

What follows is standard theory, supplied so that the rest of the course has something to stand on.
**It is not what the notes say, because the notes say nothing here.**

### [added] The RC charging transient

[table] **Extra symbols for this block** — none of these appear in the notes

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $R$ | series resistance in the charging path | $\Omega$ | 1 k$\Omega$–1 M$\Omega$ |
| $\tau$ | time constant, $\tau = RC$ | s | µs to s |
| $v_C(t)$ | instantaneous capacitor voltage | V | 0 → $V$ |
| $i(t)$ | instantaneous charging current | A | $V/R$ → 0 |
| $V$ | supply voltage | V | — |

A dc supply $V$ charges $C$ through a series resistor $R$ from a switch. The capacitor voltage
rises exponentially towards $V$; the current starts at its largest and decays to zero.

[eq: rc-charging]

$$\boxed{\;v_C(t) = V\left(1 - e^{-t/RC}\right)\;}$$

$$i(t) = \frac{V}{R}\,e^{-t/RC}$$

with the **time constant**

$$\tau = RC \qquad [\mathrm{s}] = [\Omega][\mathrm F]$$

**The two numbers worth memorising.**

$$t = \tau: \quad v_C = V\left(1 - e^{-1}\right) = 0.632\,V \quad (63.2\,\%)$$

$$t = 5\tau: \quad v_C = V\left(1 - e^{-5}\right) = 0.9933\,V \quad (99.3\,\% \text{ — "fully charged"})$$

**Both figures verified numerically.** $1-e^{-1}=0.6321$, $1-e^{-5}=0.99326$.

**Why it matters downstream.** The reservoir capacitor of a power supply discharges and recharges
on exactly this law; the $5\tau$ rule is what decides whether a smoothing capacitor is big enough.
02-rectifiers uses the result repeatedly and cites this as a prerequisite.

**[added]** — standard theory, supplied because ·J p25 is blank. Do not attribute it to the notes.

---

## 3.4 Discharging ·J p26 — the missing half-page

The top ~62 % of ·J p26 carries no ink. The discharging heading, figure and text are absent. See the
gap map in §3.0.

### [added] The RC discharging transient

The charged capacitor, now disconnected from the supply, drives its charge out through $R$. Both
$v_C$ and $i$ decay from their initial values towards zero on the same time constant.

[eq: rc-discharging]

$$\boxed{\;v_C(t) = V_0\,e^{-t/RC}\;}$$

$$i(t) = \frac{V_0}{R}\,e^{-t/RC}$$

- $V_0$ — the voltage on the capacitor at the instant discharge begins, V

**The number worth memorising.**

$$t = \tau: \quad v_C = V_0\,e^{-1} = 0.368\,V_0 \quad (36.8\,\%)$$

**Verified numerically.** $e^{-1}=0.36788$, $e^{-5}=0.00674$ — so after $5\tau$ less than $0.7\,\%$
of the initial voltage remains.

**Symmetry worth noticing.** Charging climbs to $63.2\,\%$ in one time constant; discharging falls
to $36.8\,\%$ in one time constant. The two numbers add to $100\,\%$, and they are the same
exponential seen from opposite ends.

**[added]** — standard theory, supplied because the relevant half-page is blank.

---

## 3.5 Capacitors in series ·J p26

[fig ·J p26] **Series connection.** A rectangular loop. On the **left-hand vertical** sits a battery
symbol labelled $V_s$, a plus at the top plate and a minus below it. Along the **top horizontal**, three
capacitors in a row: $C_1$, then $C_2$, then $C_3$, each drawn as two short vertical plates with a
gap, each labelled above the symbol. Beneath each capacitor a **double-headed horizontal arrow
between two vertical end-stops** spans the component, and under that arrow two labels stacked:
$V_{c1}$ then $Q_{c1}$ for the first, $V_{c2}$/$Q_{c2}$ and $V_{c3}$/$Q_{c3}$ for the others. The
loop closes down the right-hand side and back along the bottom.

**One current path, so one charge.** Charge cannot accumulate anywhere except on the plates, and
the same current flows through every element, so every capacitor carries the *same* charge:

$$Q_t = Q_{c1} = Q_{c2} = Q_{c3}$$

**Kirchhoff's voltage law round the loop.** The source voltage is shared out among the three:

$$V_s = V_{c1} + V_{c2} + V_{c3}$$

[derivation ·J p26] Substituting $V = Q/C$ for each capacitor, with the same $Q_t$ throughout:

$$V_s = \frac{Q_t}{C_1} + \frac{Q_t}{C_2} + \frac{Q_t}{C_3} = Q_t\left(\frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}\right)$$

And since $V_s = Q_t/C_t$ by the same definition applied to the whole string:

[eq: capacitors-series]

$$\boxed{\;\frac{1}{C_t} = \frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}\;}$$

**Sanity checks worth doing every time.**

- The series total is always **smaller than the smallest** member. Putting capacitors in series
  is equivalent to increasing $d$, and $C \propto 1/d$.
- Capacitors in series behave like **resistors in parallel** — reciprocal sum. The reversal catches
  people out; it comes straight from $C$ sitting in the denominator of $V = Q/C$.
- The **largest voltage appears across the smallest capacitor**, since $V_i = Q_t/C_i$ with $Q_t$
  common. That is a real design hazard, not a curiosity — see the worked numbers in §3.7.

---

## 3.6 Capacitors in parallel ·J p27

> ⚠ VERIFY **JC3.4** ·J p27 — **the parallel section has no heading.** ·J p26 gives its series
> section the bold heading "Series Connection of Capacitors"; the matching parallel section opens
> at the very top of ·J p27 with the figure and no title at all. The first ink on the page is the
> circuit drawing, below the normal heading position. The heading appears to have been lost with the
> blank space above it, exactly as on ·J p31. See `_verification-log.md`.

[fig ·J p27] **Parallel connection.** A rectangular outline. On the **left-hand vertical**, the
battery symbol $V_s$ with a plus above and a minus below. Three **vertical branches** run between the top
and bottom rails, dividing the rectangle into panels. Each branch carries a capacitor drawn as two
short horizontal plates: $C_1$, $C_2$, $C_3$, labelled to the left of each symbol. Beside each
capacitor a **vertical double-headed arrow** spans the branch, labelled $V_{c1}$ above and $Q_{c1}$
below (and correspondingly for branches 2 and 3).

**One node pair, so one voltage.** Every capacitor sits directly across the source:

$$V_s = V_{c1} = V_{c2} = V_{c3}$$

**Charge adds.** Each capacitor draws its own charge from the same voltage:

$$Q_t = Q_{c1} + Q_{c2} + Q_{c3} = V_s C_1 + V_s C_2 + V_s C_3 = V_s\left(C_1+C_2+C_3\right)$$

[eq: capacitors-parallel] and since $Q_t = V_s C_t$:

$$\boxed{\;C_t = C_1 + C_2 + C_3\;}$$

**Sanity checks.**

- The parallel total is always **larger than the largest** member. Paralleling plates is equivalent
  to increasing $A$, and $C \propto A$.
- Capacitors in parallel behave like **resistors in series** — direct sum.
- Every capacitor in the group sees the **full** source voltage, so all of them must be rated for it.

> ⚠ VERIFY **JC3.5** ·J p27 — the charge line is printed *"$Q_t = = Q_{c1} + Q_{c2} + Q_{c3}$"*,
> with a **doubled equals sign**. Typographic only; the equation is correct as read. See
> `_verification-log.md`.

---

## 3.7 [added] Working the two combination rules on one set of numbers

The notes give no numerical example for either rule. This one is supplied so the rules can be
practised, and every figure below has been computed and checked.

**[added] — not in the notes.**

Take three capacitors: $C_1 = 4.7\ \mathrm{\mu F}$, $C_2 = 10\ \mathrm{\mu F}$,
$C_3 = 22\ \mathrm{\mu F}$, across a $12\ \mathrm V$ supply.

**In parallel.**

$$C_t = 4.7 + 10 + 22 = 36.7\ \mathrm{\mu F}$$

Larger than the largest member ($22\ \mathrm{\mu F}$) — as it must be.

**In series.**

$$\frac{1}{C_t} = \frac{1}{4.7} + \frac{1}{10} + \frac{1}{22} = 0.21277 + 0.10000 + 0.04545 = 0.35822\ \mathrm{\mu F^{-1}}$$

$$C_t = \frac{1}{0.35822} = 2.79\ \mathrm{\mu F}$$

Smaller than the smallest member ($4.7\ \mathrm{\mu F}$) — as it must be.

**How the series string shares the 12 V.** The common charge is

$$Q_t = C_t V_s = 2.7916\ \mathrm{\mu F}\times 12\ \mathrm V = 33.50\ \mathrm{\mu C}$$

and each capacitor takes $V_i = Q_t/C_i$:

| Capacitor | $C_i$ | $V_i = Q_t/C_i$ |
|---|---|---|
| $C_1$ | 4.7 µF | **7.13 V** |
| $C_2$ | 10 µF | 3.35 V |
| $C_3$ | 22 µF | 1.52 V |
| | | sum = 12.00 V ✔ |

**The lesson.** The $4.7\ \mathrm{\mu F}$ capacitor — the smallest — carries $59\ \%$ of the applied
voltage. Series strings do **not** share voltage equally, and the smallest member is the one that
breaks down first.

---

## 3.8 Energy stored in a capacitor ·J p27

[eq: capacitor-energy] The notes give the stored energy in three equivalent forms on one line:
·J p27

$$\boxed{\;E = \frac{CV^{2}}{2} = \frac{QV}{2} = \frac{Q^{2}}{2C}\;}$$

- $E$ — energy stored in the electric field of the dielectric, J
- $C$ — capacitance, F
- $V$ — voltage across the plates, V
- $Q$ — charge stored, C

**All three are the same statement.** Substitute $Q = CV$ into any one and the other two drop out:

$$\frac{QV}{2} = \frac{(CV)V}{2} = \frac{CV^2}{2}
\qquad\text{and}\qquad
\frac{Q^2}{2C} = \frac{(CV)^2}{2C} = \frac{CV^2}{2}$$

**Which form to use.** Whichever avoids an extra step:

- $V$ known → $\tfrac12 CV^2$
- $Q$ known → $Q^2/2C$
- both known → $\tfrac12 QV$

**Dimensional check.** $[\mathrm F][\mathrm V^2] = (\mathrm{C/V})(\mathrm V^2) = \mathrm{C\cdot V} = \mathrm J$ ✔

**[added] worked figure.** The $36.7\ \mathrm{\mu F}$ parallel bank of §3.7 at $12\ \mathrm V$ holds

$$E = \tfrac12 \times 36.7\times10^{-6} \times 12^{2} = 2.64\ \mathrm{mJ}$$

and the same three capacitors in *series* at the same voltage hold only

$$E = \tfrac12 \times 2.7916\times10^{-6} \times 12^{2} = 0.201\ \mathrm{mJ}$$

— a factor of thirteen less, because $C_t$ fell by that factor. **Both verified numerically**, and
cross-checked against $QV/2$ and $Q^2/2C$, which agree to the digits shown.

**Note the quadratic.** Energy goes as $V^2$: doubling the working voltage quadruples the stored
energy. It is why a charged high-voltage electrolytic is genuinely dangerous long after the supply
is switched off.

---

## 3.9 Capacitive reactance — the effect of a capacitor on alternating current ·J p27

[def] **Capacitive reactance $X_c$** is the opposition a capacitor offers to the flow of ac. It is
measured in ohms ($\Omega$). ·J p27

[eq: capacitive-reactance]

$$\boxed{\;X_c = \frac{1}{2\pi f C}\quad [\Omega]\;}$$

- $X_c$ — capacitive reactance, $\Omega$
- $f$ — frequency of the applied ac, Hz
- $C$ — capacitance, F

**Dimensional check.** $\dfrac{1}{[\mathrm{Hz}][\mathrm F]} = \dfrac{1}{(1/\mathrm s)(\mathrm{C/V})} = \dfrac{\mathrm{s\,V}}{\mathrm C} = \dfrac{\mathrm V}{\mathrm A} = \Omega$ ✔

**The consequence the notes draw.** $X_c$ depends on frequency, so at **dc**, where $f = 0$:

$$f \to 0 \;\Longrightarrow\; X_c \to \infty$$

and **no current passes**. ·J p27

**This one sentence is the reason capacitors are everywhere in this course.** A capacitor blocks dc
and passes ac, and the higher the frequency the more freely it passes. Every coupling capacitor,
every bypass capacitor and every smoothing capacitor in the amplifier and rectifier chapters is an
application of it.

**[added] worked figures**, verified: a $10\ \mathrm{\mu F}$ capacitor presents

$$f = 50\ \mathrm{Hz}:\quad X_c = \frac{1}{2\pi(50)(10\times10^{-6})} = 318\ \Omega$$

$$f = 1\ \mathrm{kHz}:\quad X_c = \frac{1}{2\pi(1000)(10\times10^{-6})} = 15.9\ \Omega$$

Twenty times the frequency, one-twentieth the reactance.

> ⚠ VERIFY **JC3.6** ·J p27 — two slips in this short section. (i) The formula prints
> $X_c = \dfrac{1}{2\Pi f C}$ with a **capital $\Pi$** for $\pi$, the same substitution as in the
> $\varepsilon_0$ line on ·J p24. (ii) The sentence below reads *"the formula is dependent **of**
> frequency"* where it means **on** frequency. Neither changes the physics. See
> `_verification-log.md`.

---

## 3.10 What capacitors are for ·J p27

The notes list the jobs a capacitor does, and it is a useful checklist because almost every one of
them recurs later in the course: ·J p27

- **filter** (smoothing a rectified supply)
- **couple** (passing signal between stages while blocking their dc levels)
- **tune** (setting a resonant frequency)
- **block dc**, **pass ac**
- **bypass** (shorting an emitter resistor to signal)
- **shift phase**
- **compensate**
- **feed through**
- **isolate**
- **store energy**
- **suppress noise**
- **start motors**

Alongside the electrical duty the notes name the mechanical requirements: capacitors must be
**small, lightweight, reliable, and able to withstand adverse conditions**. ·J p27

[def] Capacitors are grouped by **dielectric material** and **mechanical configuration** — which is
exactly how §3.11 and §3.12 are organised. ·J p27

---

## 3.11 Non-electrolytic capacitors ·J p27–p28

### Ceramic ·J p27

- **Most often used for bypass and coupling.** ·J p27
- Available across a wide range of **K values** (dielectric constant).
- **High K → small size, less stability.** High-K types with $K > 3000$ are physically small and
  run from $0.001\ \mathrm{\mu F}$ up to several microfarads. ·J p27
- **Good temperature stability needs $K$ between 10 and 200.** If high $Q$ is wanted as well, the
  capacitor gets physically larger. ·J p27
- **NPO** — "negative-positive-zero" — is the ceramic with essentially **zero temperature
  coefficient**, made from $1.0\ \mathrm{pF}$ to $0.033\ \mathrm{\mu F}$. ·J p27
- **N750** is a **temperature-compensating** type for accurate capacitance over a wide temperature
  range. The "750" means a **750 ppm decrease in capacitance per $1\,^\circ\mathrm C$ rise**
  ($750\ \mathrm{ppm}/^\circ\mathrm C$). Values run 4.0 to 680 pF. ·J p27

**The one arithmetic claim in this section, checked.** The notes say $750\ \mathrm{ppm}/^\circ\mathrm C$
"equates to a $1.5\,\%$ decrease in capacitance for a $20\,^\circ\mathrm C$ temperature increase":

$$750\ \frac{\mathrm{ppm}}{^\circ\mathrm C}\times 20\,^\circ\mathrm C = 15{,}000\ \mathrm{ppm} = \frac{15{,}000}{10{,}000}\,\% = 1.5\,\%$$

**Correct.** ✔

> ### ⚠ VERIFY **JV3.2** ·J p27 — the NPO ceramic range is out by a factor of 1000
>
> The page prints: *"…come in a capacitance range of 1.0 pF to 0.033 **mF**."*
>
> **Correct form:**
>
> $$\boxed{\;1.0\ \mathrm{pF}\ \text{to}\ 0.033\ \mathrm{\mu F}\;}$$
>
> **Why.** $0.033\ \mathrm{mF} = 33\ \mathrm{\mu F}$. A $33\ \mathrm{\mu F}$ NPO ceramic does not
> exist — the same paragraph has just said that even *high-K* ceramics (which trade away all their
> stability for size) reach only "several microfarads", and NPO is the least dense ceramic
> dielectric of all. The intended unit is the microfarad; the µ has been set as m. The neighbouring
> N750 range (4.0–680 pF) confirms the order of magnitude.
>
> **The general hazard.** µ set as m is the single commonest unit slip in these notes, and it is
> always a factor of $10^3$. See `_verification-log.md`.

**Note on $K$ and $Q$ in this paragraph.** $K$ here is the dielectric constant — the same number
called $\varepsilon_r$ on ·J p24. $Q$ here is the **quality factor** of the capacitor, *not* the
charge in coulombs used four lines earlier on ·J p26–p27. Both meanings of $Q$ sit within two pages
of each other. See the clash table in `_nomenclature.md`.

### Film ·J p28

- Built from **alternate layers of metal foil and one or more layers of a flexible plastic
  insulating material** as the dielectric, in ribbon form, **rolled and encapsulated**. ·J p28

> ⚠ VERIFY **JC3.7** ·J p28 — **the "Film Capacitors" heading is missing.** ·J p28 opens straight
> into *"Film capacitors consist of alternate layers…"* at the normal top-of-text position, with no
> bold heading above it, while every neighbouring type — Mica, Paper-Foil-Filled, Electrolytic —
> has one. ·J p27 ends with the N750 paragraph, so the heading is not on the preceding page either.
> Lost, like the parallel-capacitor heading on ·J p27 and the transformer heading on ·J p31. See
> `_verification-log.md`.

### Mica ·J p28

- **Small capacitance values**, used in **high-frequency circuits**.
- Two constructions: **stacked** alternate layers of metal foil and mica insulation, encapsulated;
  or **silvered mica**, where a silver electrode is screened directly onto the mica. ·J p28

### Paper-foil-filled ·J p28

- Often used as **motor capacitors**, and **rated at 60 Hz**.
- **Alternate layers of aluminium and oil-saturated paper**, rolled together.
- Mounted in an **oil-filled, hermetically sealed metal case**. ·J p28

**[added] note for local use.** The 60 Hz rating is a North American mains figure. Kenya's supply is
**50 Hz**; a motor capacitor specified at 60 Hz is not automatically correct on a 50 Hz supply,
because $X_c = 1/2\pi fC$ makes the current through it frequency-dependent. The notes do not raise
this.

---

## 3.12 Electrolytic capacitors ·J p28–p29

### What they are, and what they cost you ·J p28

[def] Electrolytic capacitors give **high capacitance in a tolerable size**. They are made by
**electrochemically forming an oxide film on a metal surface**: ·J p28

- the **metal** carrying the oxide is the **anode**, the **positive** terminal;
- the **oxide film** is the **dielectric** — and it is extremely thin, which is where the large $C$
  comes from, via $C \propto 1/d$;
- the **cathode**, the **negative** terminal, is a **conducting liquid or a gel**.

**The drawbacks the notes list.** ·J p28

- **Low temperatures reduce performance**; **high temperatures dry them out**.
- The **electrolytes can leak and corrode** the surrounding equipment.
- **Repeated surges above the rated working voltage**, **excessive ripple current** and **high
  operating temperature** all shorten life.

**The structural point.** Everything that makes an electrolytic good — a wet chemistry and a film a
few tens of nanometres thick — is also what makes it the least reliable part in most equipment.
Electrolytics are the components that fail first in an ageing power supply.

### Aluminium electrolytic ·J p28

- **Aluminium** is the base metal.
- The surface is **etched to increase its area by as much as 100×** compared with unetched foil,
  giving far higher capacitance in the same volume — $C \propto A$ again.
- Will withstand up to **1.5 V of reverse voltage** without damage. **Higher reverse voltages
  applied for extended periods cause loss of capacitance**; excess reverse voltage for **short**
  periods changes the capacitance but does not destroy the part. ·J p28
- **Large values are used to filter dc power supplies.** After the capacitor charges, the rectifier
  stops conducting and the capacitor discharges into the load until the next cycle, then recharges
  to the peak voltage. The resulting ripple is a **complex wave containing many harmonics of the
  fundamental ripple frequency**, and it causes **noticeable heating** of the capacitor. ·J p28

**This paragraph is the bridge into 02-rectifiers.** The discharge-and-recharge cycle it describes
is precisely the shunt-capacitor filter analysed there, and the "many harmonics" remark is why that
file's ripple analysis needs a Fourier series.

> ⚠ VERIFY **JC3.8** ·J p28 — the sentence prints *"The **De** is equal to the total peak-to-peak
> ripple voltage and is a complex wave…"*. **"De" is defined nowhere** in the notes and is not a
> standard symbol.
>
> **[added] inference, offered as ours and not the notes':** the term is almost certainly
> $\Delta E$ — the *change* in capacitor voltage between one recharge and the next — with the
> Symbol-font $\Delta$ having dropped to a Latin "D". The sentence itself supplies the definition
> ("is equal to the total peak-to-peak ripple voltage"), so the meaning is recoverable even though
> the glyph is not. **The reading is probable, not certain**, and nothing downstream depends on it.
> See `_verification-log.md`.

### Tantalum electrolytic ·J p28–p29

**Why tantalum.** ·J p28

- **Preferred where high reliability and long service life matter most.**
- **Up to three times better capacitance per unit volume** than aluminium electrolytics, because
  **tantalum pentoxide has a dielectric constant about three times that of aluminium oxide** —
  again straight from $C = \varepsilon_r\varepsilon_0 A/d$.
- The notes restate the general rule here: capacitance is set by **plate area**, **plate
  separation** and **dielectric constant**. In a tantalum electrolytic the separation *is* the
  thickness of the pentoxide film. ·J p28

**Electrolyte: liquid or solid.** ·J p28

- **Liquid electrolyte** — in *wet-slug* and *foil* capacitors, generally **sulphuric acid**, which
  forms the **cathode (negative) plate**.
- **Solid electrolyte** — a dry material, **manganese dioxide**, forms the cathode plate.

**The three tantalum constructions.** ·J p28–p29

| Type | Electrolyte | Notes |
|---|---|---|
| **Foil** | liquid | **Lowest capacitance per unit volume** of the three; suited to the **higher voltages** found in older equipment. Expensive, used only where neither solid nor wet-slug will do. Operating range **−55 to +125 °C** (−67 to +257 °F). Found mainly in **industrial and military** equipment. ·J p29 |
| **Solid-electrolyte sintered-anode** | manganese dioxide | Encased in **plastic resins such as epoxy** — excellent reliability, high stability, low cost, for consumer and commercial electronics. Other designs use **plastic film or sleeving**, or **metal shells backfilled with epoxy resin**; there are also **small tubular and rectangular moulded plastic** encasements. ·J p29 |
| **Wet-electrolyte sintered-anode ("wet-slug")** | liquid | Uses a **pellet of sintered tantalum powder** with a lead attached; the anode has an **enormous surface area for its size**. Manufactured in a voltage range **to 125 V dc**. ·J p29 |

**The temperature conversion, checked.** $-55\,^\circ\mathrm C \to \tfrac95(-55)+32 = -67\,^\circ\mathrm F$ ✔ and $125\,^\circ\mathrm C \to \tfrac95(125)+32 = 257\,^\circ\mathrm F$ ✔.

> ### ⚠ ILLEGIBLE ·J p28 foot → ·J p29 top — a truncated sentence
>
> ·J p28 ends cleanly ("…manganese dioxide, forms the cathode plate.") with about three blank lines
> before its footer. **·J p29 then opens mid-sentence: "300 V dc. Of the three types of tantalum
> electrolytic capacitors, the foil design has the lowest…"**
>
> **What is missing:** the beginning of that sentence — almost certainly a statement that **foil
> tantalum capacitors are manufactured in a voltage range up to 300 V dc**, by symmetry with the
> wet-slug sentence that closes the same section ("manufactured in a voltage range to 125 V dc").
> The figure **300 V dc** is legible; only its subject is lost.
>
> **A screenshot would need to show:** the last four lines of printed page 27 and the first line of
> printed page 28.
>
> The reading above is our inference from the surviving fragment and the parallel construction; it
> is **not** presented as the notes' words.

---

## 3.13 Inductors ·J p29

[table] **Symbols for the inductor and transformer sections**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $L$ | inductance | H (henry) | µH to H |
| $N$ | number of turns on a coil | dimensionless | tens to thousands |
| $\mu$ | permeability of the core/medium | H/m | $\mu_0 = 4\pi\times10^{-7}$ |
| $H$ | magnetic field strength | A/m | — |
| $M$ | mutual inductance between two coils | H | — |
| $N_p$, $N_s$ | primary and secondary turns | dimensionless | 400 / 2000 in the worked example |
| $V_p$, $V_s$ | primary and secondary voltage | V | — |
| $I_p$, $I_s$ | primary and secondary current | A | — |
| $P_p$, $P_s$ | primary (input) and secondary (output) power | W | — |
| $\eta$ | efficiency | % | 90 % in the worked example |
| $n$ | transformation ratio | dimensionless | 0.2 in the worked example |

> **Two symbol clashes live in this table.** $\mu$ is the permeability here and the micro prefix
> everywhere in the capacitor sections (µF); and $H$ is the **henry** in "measured in henries (H)"
> and the **magnetic field strength** in the permeability sentence — **both on ·J p29, four lines
> apart.** Read $H$ from its position: a unit after a number, a field quantity in prose.

[def] An **inductor** is a device that can **store magnetic energy**. It is made from a **coiled
wire**. ·J p29

[def] **Inductance** is the ability to store magnetic energy. It is measured in **henries (H)**.
·J p29

[fig ·J p29] **Circuit symbol.** A straight horizontal lead from the left, then **three or four
small semicircular humps** rising above the line in a row (the coil), then a straight horizontal
lead continuing to the right. No core bars are drawn — this is the air-cored form. The caption
below reads "Circuit symbol".

**The four factors that set inductance.** ·J p29

| | Factor | Why |
|---|---|---|
| (a) | **Number of turns** | more turns, more flux linkage |
| (b) | **The medium round the coil / the core, through its permeability $\mu$** | a ferromagnetic core multiplies the flux for the same current |
| (c) | **Geometry of the conductor** | how the turns are arranged, long and thin against short and fat |
| (d) | **Cross-sectional area** | a wider flux path links more flux |

[def] **Permeability** is described on this page as *the ability of a material to affect the
magnetic field $H$*. ·J p29

> ⚠ VERIFY **JC3.9** ·J p29 — two small slips. (i) The page spells the plural of the unit
> **"Henrys"**; the SI plural is **henries**, and the unit name is lower-case (henry) with the
> symbol upper-case (H) because it honours a person. (ii) Permeability is glossed as the ability to
> "affect the magnetic field $H$" — strictly, $\mu$ is the constant of proportionality between the
> flux density and the field strength, $B = \mu H$, so it is $B$ that the material affects for a
> given $H$. Neither changes an answer. See `_verification-log.md`.

---

## 3.14 Self-inductance and mutual inductance ·J p29

The notes give one sentence to each.

**Self-inductance**, as printed: *"the ability of material / coil to induce emf at the
surroundings."* ·J p29

**Mutual inductance**, as printed: *"the process by which changing voltage in a conductor induces
emf in a second conductor which is in the opposite direction (Lenz's Law)."* ·J p29

Both need correcting before they are learned.

> ### ⚠ VERIFY **JV3.3** ·J p29 — the definition of self-inductance describes mutual inductance
>
> The page prints: *"Self –Inductance: This is the ability of material / coil to induce emf at the
> surroundings."*
>
> **Correct form.** Self-inductance is the property by which a coil induces an emf **in itself**
> when the current **through itself** changes:
>
> $$\boxed{\;e = -L\,\frac{\mathrm di}{\mathrm dt}\;}$$
>
> **Why.** The whole distinction between *self* and *mutual* is whether the emf appears in the
> same circuit or a different one. "Inducing emf at the surroundings" is inducing it in a
> neighbouring conductor — which is the definition of **mutual** inductance given three lines
> below. As printed, the two definitions say the same thing, and the reader is left with no way to
> tell them apart. See `_verification-log.md`.

> ### ⚠ VERIFY **JV3.4** ·J p29 — mutual inductance is driven by changing current, not changing voltage
>
> The page prints: *"Mutual inductance: This is the process by which changing **voltage** in a
> conductor induces emf in a second conductor which is in the opposite direction (Lenz's Law)."*
>
> **Correct form.** It is the changing **current** — and therefore the changing magnetic flux it
> produces — that induces the emf in the second coil:
>
> $$\boxed{\;e_2 = -M\,\frac{\mathrm di_1}{\mathrm dt}\;}$$
>
> where $M$ is the mutual inductance in henries.
>
> **Why it matters.** Faraday's law is about flux linkage, and flux is set by current, not by
> terminal voltage. Two circuits can have identical voltages and completely different couplings.
> A learner who memorises "changing voltage" will be unable to explain why a transformer's core
> material matters at all.
>
> **A second slip in the same sentence.** "…which is in the opposite direction (Lenz's Law)" is
> loosely put. Lenz's law says the induced emf acts to **oppose the change in flux that produced
> it** — the minus sign above. It does not say that the second conductor's emf points opposite to
> the first conductor's. See `_verification-log.md`.

### [added] What the inductor section does not contain

**The notes give no inductance equations at all** — no expression for $L$, no energy, no reactance.
The blank ·J p30 may have carried some of them; that cannot be established. The three standard
results are supplied here so the rest of the course has them, and they are **ours, not the notes'**:

[eq: self-inductance-emf]

$$e = -L\,\frac{\mathrm di}{\mathrm dt}$$

[eq: inductor-energy]

$$E = \tfrac12 L I^{2}$$

[eq: inductive-reactance]

$$X_L = 2\pi f L\quad [\Omega]$$

**The mirror image of the capacitor.** $X_c = 1/2\pi fC$ falls with frequency; $X_L = 2\pi fL$ rises
with it. A capacitor blocks dc and passes ac; an inductor passes dc and blocks ac. The energy
expressions are the same shape — $\tfrac12 CV^2$ against $\tfrac12 LI^2$ — with the capacitor
storing in an electric field and the inductor in a magnetic one.

**[added]** — standard theory, supplied because the notes give none.

---

## 3.15 The lost opening of the transformer section ·J p29 foot – ·J p31 top

Before the transformer material itself, the boundary must be stated plainly, because a reader who
does not know about it will assume the section simply starts abruptly.

> ### ⚠ ILLEGIBLE ·J p30 — a whole page of the notes is missing
>
> - **·J p29** stops about ten text lines short of its footer, after the mutual-inductance
>   sentence.
> - **·J p30 has no body ink whatsoever** — footer only. Printed page 29 is gone.
> - **·J p31 opens with a transformer construction diagram, then body text, with no heading of any
>   kind.**
>
> **What is missing, with the reasoning:** the `TRANSFORMERS` heading and the section's opening
> paragraph almost certainly stood on the blank page. Every other major topic in these notes gets a
> bold, underlined, upper-case heading — `CAPACITORS` on ·J p24, `INDUCTORS` on ·J p29 — and the
> transformer section has none. The pattern repeats at ·J p33, where the diode section likewise
> begins with a figure and no `DIODES` heading; there the blank lower half of ·J p32 is the likely
> place it was lost.
>
> **Whether anything else was on the page cannot be determined.** Candidates, none of them
> verifiable from the render: the closing of the inductor section (an inductance formula, inductors
> in series and parallel, inductive reactance), or a fuller transformer introduction.
>
> **A screenshot would need to show:** printed page 29 in full, and the top third of printed page
> 30 above the first transformer figure.

---

## 3.16 What a transformer is ·J p31

[def] A **transformer** is a device that can **change the level of a voltage** — high to low or low
to high. It is made from **two coils wound on a core**, close to each other and sometimes one on
top of the other. **It works by mutual induction.** ·J p31

[fig ·J p31] **Transformer construction diagram** (the figure that opens the section, above the
text).

- **Left-hand side — the primary.** A terminal circle at the top left; from it a lead runs right,
  carrying an **arrowhead pointing right** labelled $I_p$ (current flowing *into* the winding). The
  lead turns down and becomes a **coil of about four semicircular turns** drawn against a vertical
  line, labelled $N_p$. A long **vertical double-headed arrow** to the left of the winding spans
  top to bottom, labelled $V_p$. The winding's bottom lead runs left to a second terminal circle,
  under which is printed $R_p$.
- **Centre — the core.** **Two closely spaced parallel vertical lines** between the two windings,
  with an **upward arrow** below them labelled "core".
- **Right-hand side — the secondary.** A mirror image: a **coil labelled $N_s$** against the core,
  a **vertical double-headed arrow** labelled $V_s$, a top lead to a terminal circle with an
  **arrowhead pointing left** labelled $I_s$ (again drawn *into* the winding), and a bottom
  terminal circle with $R_s$ printed beneath it.

**How to read the arrows.** Both currents are drawn pointing *into* the device. That is a reference
convention, not a claim about which way current actually flows; in use, $I_s$ leaves the secondary
into the load.

> ⚠ ILLEGIBLE / **JC3.10** ·J p31 — **the labels $R_p$ and $R_s$ cannot be interpreted.** They are
> printed beneath the lower terminals of the primary and secondary loops, but **no resistor symbol
> is drawn at either place**, the body text never mentions them, and the two later figures on the
> same page (step-up and step-down) are the same drawing with these two labels removed. They may
> denote winding resistances, a source and a load resistance whose symbols were lost, or simply the
> primary and secondary circuits. **This is not determinable from the page and nothing is inferred
> here.**
>
> **A screenshot would need to show:** the top figure of printed page 30 at full resolution,
> including both lower terminals.

---

## 3.17 The 180° phase relationship ·J p31

The notes state: **the phase difference between the primary and secondary coil voltage is 180°.**
·J p31

[fig ·J p31] **Two stacked waveform axes**, one above the other, sharing the same time base.

- **Upper axis, ordinate labelled $V_s$, abscissa "time".** The trace lies **flat on the zero line
  for the first half-period**, then rises into a **positive half-cycle**, then falls through a
  **negative half-cycle**, and ends.
- **Lower axis, ordinate labelled $V_p$, abscissa "time".** The trace leaves the **origin
  immediately** with a **positive half-cycle**, then a **negative half-cycle**, then runs flat.

**What the figure is showing.** $V_s$ is drawn displaced by exactly half a period from $V_p$: when
$V_p$ is at its positive peak, $V_s$ is at zero and about to rise; when $V_p$ goes negative, $V_s$
goes positive. Half a period *is* 180°, so the picture matches the sentence.

**A drawing caution.** Because the shift is drawn as a *delay* — with $V_s$ flat at the start —
the figure looks like a transient. In steady state both waveforms run continuously and the 180°
appears as a permanent inversion, not a late start.

> ### ⚠ VERIFY **JV3.5** ·J p31 — the flat 180° claim needs a qualifier
>
> The page prints: *"The phase difference between the primary coil and secondary coil voltage is
> $180^0$ as shown in the diagram below."*
>
> **Correct form.** The phase relationship between primary and secondary voltage is **not a fixed
> property of transformers**. It is set by the **relative sense of the two windings** and by which
> terminal of each winding you take as the reference:
>
> $$\boxed{\;\text{like-marked (dotted) terminals} \Rightarrow V_p \text{ and } V_s \text{ in phase};\quad \text{opposite marking} \Rightarrow 180^\circ\;}$$
>
> **Why.** Both windings link the *same* core flux, so both induced emfs follow the same
> $-\mathrm d\Phi/\mathrm dt$. Whether the secondary terminal voltage comes out in phase or
> antiphase depends purely on which way the secondary is wound relative to the primary — which is
> exactly what the dot convention exists to record. Reverse the secondary's two leads and the same
> transformer gives the opposite answer. The centre-tapped rectifier in 02-rectifiers depends on
> this: its two half-secondaries are deliberately in antiphase with each other.
>
> **What to write in an exam.** These notes are the course's own material and they state 180°
> without qualification, so a CAT question lifted from this page expects **180°**. Give it, and add
> the one-line qualifier — it is correct and it costs nothing.
>
> See `_verification-log.md`.

> ⚠ VERIFY **JC3.11** ·J p31 — the angle is typeset $180^{0}$, with a **superscript zero** instead
> of the degree sign: $180^\circ$. Cosmetic, but it recurs. See `_verification-log.md`.

---

## 3.18 Ideal and practical transformers: efficiency and losses ·J p31

**The ideal transformer.** Input power equals output power, because there is no loss: ·J p31

[eq: ideal-transformer-power]

$$\boxed{\;P_p = P_s\;}$$

**The practical transformer.** Some power is always lost in the device itself, so

$$P_p > P_s$$

and that gap is what makes an efficiency figure necessary.

[def] [eq: transformer-efficiency] **Efficiency** is the ratio of output power to input power:
·J p31

$$\boxed{\;\eta = \frac{P_s}{P_p}\times 100\ \ [\%]\;}$$

- $P_s$ — output (secondary) power, W
- $P_p$ — input (primary) power, W
- $\eta$ — efficiency, %

**The four losses the notes list.** ·J p31

| | Loss | What it is |
|---|---|---|
| (a) | **Heat losses** | $I^2R$ in the resistance of the copper windings |
| (b) | **Eddy currents** and **leakage** | circulating currents induced in the core itself, and flux that fails to link both windings |
| (c) | **Hysteresis** | energy spent re-magnetising the core every cycle |
| (d) | **Mechanical losses** | e.g. **sound** — the hum of a mains transformer |

**Note that (a)–(c) are the three losses that matter numerically**, and that only (a) depends on
load current; (b) and (c) are core losses and are roughly constant once the transformer is
energised. The notes do not draw that distinction.

> ⚠ VERIFY **JC3.12** ·J p31 — item (b) prints as a single run-on entry, **"Eddy currents leakage
> current"**, with no conjunction. These are **two different loss mechanisms** — eddy currents
> circulating in the core, and leakage flux failing to link the secondary — and the missing "and"
> makes them read as one. See `_verification-log.md`.

---

## 3.19 Step-up and step-down ·J p31

[fig ·J p31] **Two transformer diagrams side by side**, each the construction diagram of §3.16
without the $R_p$/$R_s$ labels, and captioned above.

- **"Step-up transformer" (left).** The primary winding $N_p$ is drawn **short — about four turns**;
  the secondary $N_s$ is drawn **tall — about ten turns**. $V_p$ and $I_p$ on the left, $V_s$ and
  $I_s$ on the right, core bars between.
- **"Step-down transformer" (right).** The mirror case: **$N_p$ tall (about ten turns)**, **$N_s$
  short (about four turns)**.

**The rule the pictures encode.**

$$N_s > N_p \;\Longrightarrow\; V_s > V_p \quad(\textbf{step-up})$$

$$N_s < N_p \;\Longrightarrow\; V_s < V_p \quad(\textbf{step-down})$$

**And what you pay for it.** For an ideal transformer $P_p = P_s$, so voltage gained is current
lost:

$$V_p I_p = V_s I_s$$

A step-up transformer raises the voltage and lowers the available current in exactly the same
proportion. There is no free power anywhere in the device.

---

## 3.20 The transformation ratio ·J p32

[def] [eq: transformation-ratio] The **transformation ratio** $n$ is *the ratio by which the voltage
is transformed*: ·J p32

$$\boxed{\;n = \frac{V_p}{V_s} = \frac{N_p}{N_s} = \frac{I_s}{I_p}\;}$$

- $n$ — transformation ratio, dimensionless
- $V_p$, $V_s$ — primary and secondary voltage, V
- $N_p$, $N_s$ — primary and secondary turns
- $I_p$, $I_s$ — primary and secondary current, A

**Why the current ratio is inverted.** It follows from the ideal-transformer power balance and is
worth being able to reproduce in one line:

$$V_p I_p = V_s I_s \;\Longrightarrow\; \frac{I_s}{I_p} = \frac{V_p}{V_s} = \frac{N_p}{N_s}$$

**Read the ratio carefully — it is primary over secondary.** With $n$ defined this way, a **step-up**
transformer has $n < 1$ and a **step-down** transformer has $n > 1$. Many textbooks define the
turns ratio the other way up, and the two tier-2 files in this knowledge base disagree with each
other about it:

| Source | Symbol | Definition | So for the same transformer |
|---|---|---|---|
| **these notes ·J p32** | $n$ | $N_p/N_s$ | $n = 0.2$ in §3.21 |
| **·L7 p17** (transformer coupling) | $a$ | $N_1/N_2$ = primary/secondary | same as $n$ |
| **·L2 p6** (rectifier supply) | $K$ | $N_2/N_1$ = secondary/primary | the **reciprocal** |

**Always check which way up a turns ratio is defined before substituting.** A quoted "10 : 1" is
ambiguous on its own; the surrounding formula tells you which.

**Note the $V_s$ clash.** In §3.5–§3.6, $V_s$ was the **source** voltage driving a capacitor
network. From §3.16 onward it is the **secondary** voltage of a transformer. Same symbol, two
meanings, six pages apart, in one document.

---

## 3.21 [ex] The 400 : 2000-turn transformer ·J p32

This is the only worked example in the whole range, and it is the one a CAT can lift verbatim.

**Statement, as set.** *A transformer has the following parameters:* ·J p32

$$N_P = 400,\qquad N_S = 2000,\qquad V_S = 20\ \mathrm V,\qquad I_p = 0.5\ \mathrm A,\qquad \eta = 90\,\%$$

***Find $I_s$.***

**Orientation before any algebra.** $N_S > N_P$, so this is a **step-up** transformer: the
secondary voltage (20 V) is higher than the primary voltage, and the secondary current will be
lower than the 0.5 A drawn by the primary.

### Step 1 — the ideal secondary current

From $I_s/I_p = N_p/N_s$: ·J p32

$$I_s = \frac{N_p}{N_s}\,I_p = \frac{400\times0.5}{2000} = \frac{200}{2000} = 0.1\ \mathrm A$$

**Verified.** ✔ — but hold on to it: this is the **lossless** answer, and the question specifies
$\eta = 90\,\%$. Step 3 supersedes it.

### Step 2 — the primary voltage

From $V_p/V_s = N_p/N_s$: ·J p32

$$V_p = \frac{N_p\,V_s}{N_s} = \frac{400\times 20}{2000} = \frac{8000}{2000} = 4\ \mathrm V$$

**Verified.** ✔ A 4 V primary and a 20 V secondary — consistent with the 5 : 1 step-up.

> ### ⚠ VERIFY **JV3.6** ·J p32 — a digit is dropped from the denominator of $V_p$
>
> The page prints: $V_p = \dfrac{N_p\times V_s}{N_s} = \dfrac{400\times 20}{\mathbf{200}} = 4\ \mathrm V$.
>
> **Correct form:**
>
> $$\boxed{\;V_p = \frac{400\times 20}{2000} = 4\ \mathrm V\;}$$
>
> **Why.** $N_s = 2000$, not 200 — the statement says so two lines above, and the step immediately
> before it divides by 2000 correctly. As printed the arithmetic is false: $8000/200 = 40$, not 4.
> The printed *answer* (4 V) is right; only the printed denominator is wrong, so a reader who
> re-does the sum as written gets **40 V** and then cannot reproduce the final answer.
> See `_verification-log.md`.

### Step 3 — bring the efficiency in

$$\eta = \frac{P_s}{P_p}\times100 = 90 \qquad\Longrightarrow\qquad \frac{I_s V_s}{I_p V_p} = 0.9$$

Substituting $V_s = 20\ \mathrm V$, $V_p = 4\ \mathrm V$, $I_p = 0.5\ \mathrm A$: ·J p32

$$\frac{I_s \times 20}{4\times 0.5} = 0.9$$

$$\frac{20\,I_s}{2} = 0.9 \;\Longrightarrow\; 10\,I_s = 0.9$$

$$\boxed{\;I_s = 0.09\ \mathrm A\;}$$

**Verified, and cross-checked through the powers.**

$$P_p = V_p I_p = 4\times0.5 = 2\ \mathrm W$$

$$P_s = \eta P_p = 0.9\times 2 = 1.8\ \mathrm W$$

$$I_s = \frac{P_s}{V_s} = \frac{1.8}{20} = 0.09\ \mathrm A \quad ✔$$

$$\text{check: } \eta = \frac{0.09\times20}{0.5\times4} = \frac{1.8}{2} = 0.9 = 90\,\% \quad ✔$$

> ### ⚠ VERIFY **JV3.7** ·J p32 — a digit is added to the denominator of the efficiency step
>
> The page prints: $\dfrac{I_s\times V_s}{I_p\times V_p} = \dfrac{I_s\times 20}{\mathbf{40}\times 0.5} = 0.9$.
>
> **Correct form:**
>
> $$\boxed{\;\frac{I_s\times 20}{4\times 0.5} = 0.9 \;\Longrightarrow\; I_s = 0.09\ \mathrm A\;}$$
>
> **Why.** The slot holds $V_p$, which the line above has just established as **4 V**, not 40. As
> printed the denominator is $40\times0.5 = 20$, which gives $I_s = 0.9\ \mathrm A$ — **ten times**
> the answer the page then states. The printed final answer (0.09 A) is the correct one, so the
> defect is confined to that one intermediate line — but a reader following the working arrives at
> a different number from the one boxed underneath.
>
> **Note the pattern.** JV3.6 drops a zero and JV3.7 adds one, in consecutive lines of the same
> example. Both are transcription slips around a correct result. See `_verification-log.md`.

> ### ⚠ VERIFY **JV3.8** ·J p32 — the example produces two different answers for $I_s$ and does not say which stands
>
> Step 1 obtains $I_s = 0.1\ \mathrm A$ from $I_s/I_p = N_p/N_s$; step 3 obtains
> $I_s = 0.09\ \mathrm A$ from $\eta = 90\,\%$. **Both are printed, neither is withdrawn, and the
> question asked for one number.**
>
> **Correct reading:**
>
> $$\boxed{\;I_s\big|_{\text{ideal}} = 0.1\ \mathrm A \quad\text{is superseded by}\quad I_s\big|_{\eta=90\%} = 0.09\ \mathrm A\;}$$
>
> **Why.** The relation $I_s/I_p = N_p/N_s$ is a **consequence of $P_p = P_s$** and therefore holds
> only for a *lossless* transformer. Once $\eta = 90\,\%$ is imposed, it fails by exactly that
> factor:
>
> $$\frac{I_s}{I_p} = \frac{0.09}{0.5} = 0.18 \qquad\text{whereas}\qquad n = \frac{N_p}{N_s} = 0.2$$
>
> $$0.18 = 0.9\times 0.2 = \eta\, n$$
>
> The voltage relation $V_p/V_s = N_p/N_s$ **does** survive — it comes from flux linkage, not from
> power balance — which is why step 2 is still legitimate. The general form is:
>
> $$\boxed{\;\frac{I_s}{I_p} = \eta\,\frac{N_p}{N_s}\;}$$
>
> **Why it matters.** A reader who stops at step 1 answers 0.1 A. The notes give the answer as
> 0.09 A. Both numbers appear on the page with no word distinguishing them. See
> `_verification-log.md`.

### The method in four lines, for reuse

1. Turns give the **voltage** ratio: $V_p = V_s N_p/N_s$. Efficiency does not touch it.
2. Input power: $P_p = V_p I_p$.
3. Output power: $P_s = \eta P_p$.
4. Output current: $I_s = P_s/V_s$.

Any transformer question that quotes an efficiency yields to those four steps in that order.

---

## 3.22 Triage — what to revise, and what this range cannot give you

**Highest exam value.**

1. **The 400 : 2000 worked example, §3.21.** It is the only worked example in nine pages, and a CAT
   can lift it whole. Know the four-step method, and know why 0.1 A is not the answer.
2. **The two combination rules, §3.5–§3.6.** Series is reciprocal-sum, parallel is direct-sum, and
   the reversal against resistors is the standard trap.
3. **$E = \tfrac12 CV^2$ and $X_c = 1/2\pi fC$, §3.8–§3.9**, with the dc consequence:
   $f=0 \Rightarrow X_c = \infty \Rightarrow$ no current.
4. **$n = V_p/V_s = N_p/N_s = I_s/I_p$ and $\eta = (P_s/P_p)\times100$, §3.18 and §3.20.**
5. **$C = \varepsilon_r\varepsilon_0 A/d$ and the three factors, §3.1.**

**Worth reading once, unlikely to be examined numerically.** The capacitor-type catalogue,
§3.10–§3.12 — six pages of descriptive material with no equations. It is the sort of content that
becomes a short "list three types of capacitor and state one application of each" question, so
learn the *headings* and one distinguishing fact for each type rather than the paragraphs.

**What this range does not give you, and no other file in this knowledge base does either:**

- **the charging and discharging curves** (·J p25 and the top of ·J p26 are blank — §3.3, §3.4
  supply the standard results as `[added]`);
- **any inductance formula whatsoever** — no $L$, no $\tfrac12LI^2$, no $X_L$ (§3.14 supplies them
  as `[added]`);
- **the transformer section's opening** (·J p30 is blank — §3.15);
- **any exercise or unsolved problem.** There are none in ·J p24–p32, so §3.7 and the `[added]`
  figures in §3.8–§3.9 are the only practice available; work them before the worked example.

**Balance of the range.** Roughly one page of equations, six pages of descriptive prose, and one
page of worked numbers. It is the least quantitative block in the notes — and the three blank pages
fall on the only parts that would have been otherwise.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
