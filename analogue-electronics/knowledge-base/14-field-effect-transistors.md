---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "14 — Field Effect Transistors (supporting)"
source: "L4 — 'Lesson 4 Field Effect Transistors.pdf', 24 pp."
pages: "1-24"
tier: supporting
file_role: topic
subtopics:
  - "what a FET is; the FET family tree — JFET, DE MOSFET, E-only MOSFET, N- and P-channel"
  - "JFET construction, terminal notation and schematic symbols"
  - "JFET theory of operation: depletion regions, wedge shape, pinch-off, cut-off"
  - "the V_P sign trap — the chapter uses V_P with two opposite signs"
  - "JFET drain characteristic with V_GS = 0: ohmic, curve AB, pinch-off/saturation, breakdown"
  - "JFET characteristics with external bias; Shockley's square-law equation"
  - "transfer characteristic and its inverse form"
  - "small-signal parameters: r_d, g_m, g_mo, mu, R_DS"
  - "d.c. biasing: gate bias, self-bias, source bias, voltage-divider bias"
  - "d.c. load line, mid-point bias and the Q-point"
  - "common-source JFET amplifier: working and phase inversion"
  - "amplifier gains in all three modes: common source, common drain, common gate"
  - "input capacitance and the Miller effect"
  - "advantages and disadvantages of FETs"
  - "MOSFET / IGFET: DE MOSFET construction, working, symbols, static characteristics"
  - "enhancement-only N-channel MOSFET (NMOS): inversion layer, threshold voltage, the K equation"
  - "biasing the E-only MOSFET: drain-feedback bias and voltage-divider bias"
  - "DE MOSFET and E-MOSFET amplifiers"
  - "FET applications and MOSFET handling"
key_equations: [shockley, shockley-inverse, vp-vgsoff, pinchoff-general, ac-drain-resistance, transconductance, gmo, gm-from-gmo, amplification-factor, dc-drain-resistance, self-bias, source-bias, divider-bias, load-line, midpoint-bias, av-common-source, miller-input-capacitance-fet, av-common-drain, ro-common-drain, av-common-gate, ri-common-gate, emosfet-k, emosfet-gm]
prerequisites: ["01-semiconductor-fundamentals (P-N junction, depletion region, reverse bias)", "03-bipolar-junction-transistors (biasing, load line, Q-point, small-signal gain)"]
leads_to: ["FET switching and digital logic", "multistage and feedback amplifiers", "operational amplifiers"]
verification_flags: 36
tags: [fet, jfet, mosfet, nmos, de-mosfet, e-mosfet, igfet, shockley-equation, pinch-off, transconductance, biasing, load-line, common-source, common-drain, common-gate, miller-effect, square-law, unipolar]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·L4 pN = provenance (which PDF page of Lesson 4 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 04 — Field Effect Transistors

Scope: the whole of L4, 24 PDF pages. Covers the junction FET end to end — construction, operation,
both static characteristics, Shockley's square law, the small-signal parameters, four biasing
schemes, the load line, and gain expressions for all three amplifier configurations — then the whole
MOSFET family: DE MOSFET and enhancement-only MOSFET, their construction, characteristics, biasing
and amplifiers. Closes with applications, handling, two tutorial problem sets and an objective test.

**Provenance of this lesson.** L4 is not a lecture deck. It is a scanned run of chapter pages from a
printed electrical-technology textbook — **Chapter 63, "Field Effect Transistors"**, printed pages
**2364–2386**, carrying its own article numbering (63.1, 63.2, …), figure numbering (Fig. 63.1 …
Fig. 63.38) and numbered worked examples (Example 63.1 … Example 63.14). Two consequences:

- **Citations here give the PDF page** — `·L4 p7` is the seventh page image, which is printed page
  2369. Add 2362 to a PDF page number to get the printed page number (p2 → 2364, p24 → 2386).
- **The article and figure numbers are the textbook's own** and are quoted so a printed copy can be
  followed alongside. The prose below is written fresh; only equations, standard results and the
  chapter's own example numbers are carried over. No scanned figure is reproduced — every figure is
  described in words, in enough detail to redraw.

The scan carries OCR noise (stray glyph codes, overstruck characters, lost modulus bars). Those are
rendering artefacts of the scan, not defects in the teaching, and are logged as cosmetic `C4.x` only
where a reader could be misled by them.

---

> ## ⚠ Read §4.4 before working any numerical problem
>
> **The chapter uses the symbol $V_P$ with two opposite signs**, and both usages appear within two
> pages of each other. Substituted into Shockley's equation, the wrong one does not give a slightly
> wrong answer — it gives an $I_D$ **larger** than $I_{DSS}$, which is physically impossible.
> §4.4 sets out which sign belongs where, and gives a one-line self-check.

---

## 4.0 What the chapter sets out to cover ·L4 p1

The opening page lists the chapter's own objectives, in teaching order. They map one-to-one onto the
article numbers, and are worth reading as a syllabus for the lesson: ·L4 p1

what a FET is · junction FET (JFET) · static characteristics of a JFET · JFET drain characteristic
with $V_{GS}=0$ · characteristics with external bias · transfer characteristic · small-signal JFET
parameters · d.c. biasing of a JFET · d.c. load line · common-source JFET amplifier · JFET amplifier
gains · advantages of FETs · MOSFET or IGFET — DE MOSFET · schematic symbols for a DEMOSFET · static
characteristics of a DEMOSFET · enhancement-only N-channel MOSFET · biasing E-only MOSFET — FET
amplifiers · FET applications · MOSFET handling.

[fig ·L4 p1] The opener carries a decorative photograph captioned "Field Effect Transistor as an
Electronic Flute" — a beach scene beside a sketched FET structure. Nothing technical is stated in it.

> ⚠ VERIFY **C4.1** ·L4 p1 — the eighth objective is printed "D.C. **Baising** of a JFET" for
> **Biasing**. The article itself (§63.8, ·L4 p9) spells it correctly. See `_verification-log.md`.

---

## 4.1 What a FET is ·L4 p2

[def] **FET** — *field effect transistor*. A **three-terminal, unipolar, solid-state** device in
which the current is controlled **by an electric field**, in the way a vacuum tube's current is.
·L4 p2

Two words carry the weight:

- **Unipolar** — conduction is by **one** carrier type only (electrons in an N-channel device, holes
  in a P-channel one). A BJT is *bipolar*: it uses both. ·L4 p5
- **Field effect** — the controlling electrode draws essentially no current; it acts through the
  field it sets up, not through carriers it injects.

[fig ·L4 p2] **The FET family tree.** A tree with FET at the root, branching to:

- **Junction FET (JFET)** → N-channel, P-channel
- **Metal-Oxide-Semiconductor FET (MOSFET / IGFET)** → **DE MOSFET** → N-channel, P-channel; and
  **E-only MOSFET** → N-channel, P-channel

Under each of the six leaves the tree draws the device symbol with its drain supply polarity:
N-channel devices take $+V_{DD}$ at the drain, P-channel devices take $-V_{DD}$. The gate of the
N-channel JFET is marked $-$, that of the P-channel JFET $+$; the E-only N-channel MOSFET is marked
$+$ at the gate and the E-only P-channel $-$.

[table] The two subdivisions the page names explicitly ·L4 p2

| Family | Also called | Subdivisions |
|---|---|---|
| Junction FET | JFET | N-channel · P-channel |
| Metal-oxide semiconductor FET | MOSFET, **IGFET** (insulated-gate FET) | depletion-enhancement (**DEMOSFET**) · enhancement-only (**E-only MOSFET**), each N- or P-channel |

---

## 4.2 JFET construction and terminal notation ·L4 p2–p3

### Symbols used from here on

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{DS}$ | drain-to-source voltage | V | 0–30 V |
| $V_{GS}$ | gate-to-source voltage | V | 0 to −8 V (N-channel) |
| $I_D$ | drain current | A (usually mA) | 0.5–20 mA |
| $I_S$ | source current; $I_S \simeq I_D$ because $I_G \simeq 0$ | A | as $I_D$ |
| $I_G$ | gate current | A | ~0 (a few nA) |
| $I_{DSS}$ | drain current with the gate shorted to the source ($V_{GS}=0$), in saturation | A (mA) | 5–20 mA |
| $V_P$, $V_{PO}$ | pinch-off voltage — **see §4.4, the sign is not consistent in this chapter** | V | 3–8 V |
| $V_{GS(off)}$ | gate-source voltage that cuts the drain current off | V | −3 to −8 V (N-channel) |
| $V_{DD}$ | drain supply voltage | V | 12–25 V |
| $R_L$ | drain load resistor | Ω | 0.45–12 kΩ |
| $R_S$ | source (bias) resistor | Ω | 150 Ω–5 kΩ |
| $R_G$ | gate resistor | Ω | 1–10 MΩ |

### (a) Basic construction ·L4 p2–p3

An **N-channel JFET** is built from a narrow bar of **N-type** semiconductor. Two **P-type** regions
are diffused into opposite sides of its middle, forming two P-N junctions — the **gates**. The
region between them is the **channel**. The two P-regions are joined internally and one lead is
brought out as the **gate terminal**. Ohmic (direct, non-rectifying) contacts at the two ends of the
bar give the **source** $S$ and the **drain** $D$. ·L4 p2

A **P-channel JFET** is the same construction with the types interchanged: a P-type bar with two
N-type gate regions, its majority carriers being holes. ·L4 p3

[fig ·L4 p2] **Cutaway of an N-channel JFET.** A rectangular slab drawn in perspective: a light
central column (the N-type channel) sandwiched between two heavily shaded blocks marked "P type
(gate)"; the narrow bands flanking the channel are shaded as "Depletion Zone". The gate lead comes
off the left block; the drain contact is at the top of the channel and the source at the bottom,
with $0.0\ \mathrm{V}$ marked at the gate and $+0.0\ \mathrm{V}$ at the drain. Beneath, the caption
"Electrons flow" marks the direction of carrier travel from source to drain.

[fig ·L4 p3] **Fig. 63.1 — three-row figure, N-channel in the left column, P-channel in the right.**

- **Row (a), perspective view.** A flat slab drawn in isometric. The N-channel version has the gate
  diffusion drawn as a shaded rectangle on the top face with a matching magenta strip on the
  underside (the two internally-connected gates), leads coming off for Drain (upper left), Gate
  (top) and Source (lower right), and the arrow into the front edge labelled "N-Channel". The
  P-channel version is identical with the labels swapped: the bar face is marked P and the gate
  diffusion N.
- **Row (b), cross-section.** A vertical rectangle, D at the top and S at the bottom. For the
  N-channel device the bar is marked N with two small P blocks let into its sides, both wired to the
  gate lead G on the left. The P-channel device has a P bar with two N blocks.
- **Row (c), schematic symbols.** D at the top, S at the bottom, G entering from the left as a
  horizontal line meeting the vertical channel line, with an arrowhead on the gate lead. The
  N-channel symbol's arrow points **into** the channel; the P-channel symbol's arrow points **out**.

> [added] **The one rule that fixes both symbols:** *the gate arrow always points towards N-type
> material.* In an N-channel JFET the channel is the N material, so the arrow points inwards; in a
> P-channel JFET the gates are the N material, so it points outwards. ·L4 p3 states this rule
> explicitly.

> ⚠ VERIFY **V4.1** ·L4 p3 — in Fig. 63.1 (*a*), the **N-channel** drawing labels the bar itself
> **P** and the gate diffusion **P**. The P-channel drawing beside it labels the bar **P** and the
> gate diffusion **N**, so the outer label is the bar material. Correct labelling for the N-channel
> device — and the labelling the text of ·L4 p2 requires ("a narrow bar of N-type semiconductor…two
> P-type junctions are diffused on opposite sides") — is
> $$\boxed{\;\text{bar} = N,\qquad \text{both gate diffusions} = P\;}$$
> See `_verification-log.md`.

### The four terms ·L4 p3

[def] **Source $S$** — the terminal through which majority carriers **enter** the bar. The carriers
come from it, hence the name.

[def] **Drain $D$** — the terminal through which majority carriers **leave** the bar. The
drain-to-source voltage $V_{DS}$ drives the drain current $I_D$.

[def] **Gate** — the two internally-connected, **heavily doped** impurity regions forming the two
P-N junctions. The gate-source voltage $V_{GS}$ **reverse-biases** them.

[def] **Channel** — the space between the two gates, through which majority carriers pass from
source to drain when $V_{DS}$ is applied.

---

## 4.3 JFET theory of operation ·L4 p3–p5

Two standing facts govern everything that follows: ·L4 p3

1. **The gates are always reverse-biased**, so the gate current $I_G$ is practically zero.
2. **The source is connected to whichever end of the drain supply provides the carriers.** In an
   N-channel JFET, $S$ goes to the **negative** end (it needs electrons); in a P-channel JFET, $S$
   goes to the **positive** end (it needs holes).

The discussion below is for an N-channel device, and works through four cases.

### (i) $V_{GS} = 0$ and $V_{DS} = 0$ ·L4 p3

$I_D = 0$, because $V_{DS} = 0$. The depletion regions around the two P-N junctions are of **equal
thickness and symmetrical**.

### (ii) $V_{GS} = 0$, $V_{DS}$ increased from zero ·L4 p3–p4

Electrons (the majority carriers) flow from $S$ to $D$; conventional drain current $I_D$ therefore
flows through the channel from $D$ to $S$.

[eq] The gate-to-channel bias at any point along the channel is the **numerical sum** of the two
voltages: ·L4 p3

$$\text{gate-to-channel bias} = |V_{DS}| + |V_{GS}|$$

With $V_{GS}=0$ the reverse bias is supplied by $V_{DS}$ alone. $V_{DS}$ falls progressively along
the channel from drain to source, so the reverse bias is **largest at the drain end and smallest at
the source end** — which is why **the depletion regions become wedge-shaped**, biting deeper into
the channel near the drain. ·L4 p4

Then, as $V_{DS}$ is raised: ·L4 p4

1. **At small $V_{DS}$** the depletion regions are too small to affect the channel cross-section, so
   the channel behaves as a **resistor of constant value** and $I_D$ rises **linearly** with
   $V_{DS}$ (Ohm's law).
2. **At a critical $V_{DS}$ — the pinch-off voltage $V_{PO}$** — the drain current stops rising and
   settles at its maximum value $I_{DSS}$. The separation between the two depletion regions at the
   drain end has reached a minimum $W$.
3. **Beyond $V_{PO}$**, $I_D$ stays at $I_{DSS}$. Further increase in $V_{DS}$ makes **more of the
   channel** (extending towards the source) reach the minimum width: the channel width does not
   shrink further, its **length $L$ of narrowed region grows**. Channel resistance $R_{DS}$ then
   rises at the same rate as $V_{DS}$, so $I_D = V_{DS}/R_{DS}$ is unchanged.
4. **At $V_{DSO}$** the device breaks down and $I_D$ climbs steeply.

[def] $I_{DSS}$ — the **zero-gate-voltage drain current**. The "SS" records that the gate is
**shorted to the source**, guaranteeing $V_{GS}=0$. ·L4 p4

> **Pinch-off does not mean current-off.** ·L4 p4 states this twice, in bold. At pinch-off $I_D$ is
> at its **maximum**, not zero.

[fig ·L4 p4] **Fig. 63.2 — four cross-sections showing the depletion regions growing.** Each panel
draws the JFET as an upright rectangle: N material top and bottom, two P gate regions let into the
sides, their depletion regions drawn as pale rounded envelopes. Drain lead at the top, source at the
bottom, gate lead from the left P region.

- **(a)** $V_{DS}=0$, gate-source voltage zero: no external supply attached; both depletion envelopes
  are symmetrical rectangular-cornered shapes of equal thickness.
- **(b)** $V_{DS} < V_{PO}$: a supply $V_{DD}$ (drawn as a variable battery) feeds the drain through
  a series resistor, with $V_{DS}$ marked as the double arrow across drain-to-source and $I_D$ as a
  downward arrow inside the channel. The depletion envelopes are now **wedge-shaped**, thicker at the
  drain (top) end.
- **(c)** $V_{DS} = V_{PO}$, captioned **"Pinch-off"**: the two wedges have closed to a minimum
  separation $W$, marked by opposing arrows across the top of the channel; $L$ marks the short
  pinched length and the current arrow is labelled $I_S$.
- **(d)** $V_{DS} > V_{PO}$: same picture with $L$ visibly longer — the pinched region has extended
  towards the source — and $W$ unchanged.

> ⚠ VERIFY **C4.2** ·L4 p4 — all four panels of Fig. 63.2 label the gate-to-source voltage
> **$V_{SS} = 0$**. The quantity meant is $V_{GS}$; $V_{SS}$ is used later in the same chapter
> (Fig. 63.8 *c*, ·L4 p9) for the **source supply voltage**, a different thing. Read the figure as
> $V_{GS} = 0$. See `_verification-log.md`.

> ⚠ VERIFY **C4.3** ·L4 p4 — Fig. 63.2 labels the resistor in series with $V_{DD}$ and the **drain**
> as $R_S$. From §63.8 onwards $R_S$ is consistently the **source** resistor, and the drain resistor
> is $R_L$. The same figure also calls the channel current $I_D$ in panel (*b*) but $I_S$ in panels
> (*c*) and (*d*) — harmless here, since $I_S = I_D$ when $I_G = 0$, but worth noticing.
> See `_nomenclature.md`.

### (iii) $V_{DS} = 0$, $V_{GS}$ made negative ·L4 p4–p5

Making $V_{GS}$ more negative increases the gate reverse bias, which **thickens the depletion
regions**. At a sufficiently negative $V_{GS}$ the two depletion regions **touch**: the channel is
**cut off**. ·L4 p4

[def] $V_{GS(off)}$ — the value of $V_{GS}$ that cuts off the channel and hence the drain current.
It is **negative for an N-channel JFET and positive for a P-channel JFET**. ·L4 p5 (footnote)

> ⚠ VERIFY **C4.4** ·L4 p5 — that footnote is printed "It has negative value for an N-channel JFET
> but a positive value **or** a P-channel JFET" — **or** for **for**. The sense required is the one
> given above, and it is the sign convention the whole chapter depends on.
> See `_verification-log.md`.

[fig ·L4 p4] **Fig. 63.3 — cut-off.** The same cross-section as Fig. 63.2 (a) but with a variable
supply $V_{GG}$ in the gate lead: the two depletion envelopes have expanded until they meet in the
middle of the channel, closing it. $+$ is marked at the drain terminal $D$ and the source $S$ is at
the bottom.

[eq: vp-vgsoff] The magnitude relation the chapter states ·L4 p5

$$\boxed{\;V_{GS(off)} = -V_{PO}\qquad\text{equivalently}\qquad |V_{PO}| = |V_{GS(off)}|\;}$$

For the device drawn in Fig. 63.6, $V_{PO} = 4\ \mathrm{V}$ and $V_{GS(off)} = -4\ \mathrm{V}$.
·L4 p5

### (iv) $V_{GS}$ negative and $V_{DS}$ increased ·L4 p5

As $V_{GS}$ is made more and more negative, **both** the pinch-off voltage **and** the breakdown
voltage come down.

[fig ·L4 p5] **Fig. 63.4 — the common-source test circuit.** The N-channel JFET symbol sits in the
middle: drain at the top, connected through the drain load $R_L$ to $+V_{DD}$ (a variable battery)
and back to a common rail; source at the bottom, tied to the common rail, which is earthed. The gate
is fed from a variable supply $V_{GG}$ through a gate resistor $R_g$. Curved arrows inside the
circuit mark $V_{DS}$ (drain to source) and $V_{GS}$ (gate to source); $I_D$ is marked flowing in
the drain lead.

### Summary of the four cases ·L4 p5

1. Hold $V_{GS}$ fixed (zero or negative) and raise $V_{DS}$: $I_D$ rises, flattens at pinch-off,
   then runs away at breakdown. Making $V_{GS}$ more negative lowers **both** $V_P$ and the
   breakdown voltage.
2. Hold $V_{DS}$ fixed and make $V_{GS}$ more negative: $I_D$ falls, reaching zero at $V_{GS(off)}$.

[def] Because the **gate voltage** controls the **drain current**, a JFET is a
**voltage-controlled** device. A P-channel JFET works identically, with holes as carriers and the
polarities of both $V_{DD}$ and $V_{GS}$ reversed. ·L4 p5


---

## 4.4 ⚠ The $V_P$ sign trap — read this before any calculation ·L4 p4–p8, p15

The chapter uses the symbol $V_P$ (also written $V_{PO}$) for **two different quantities of opposite
sign**, and both appear inside three pages of each other.

**Usage A — the drain-axis pinch-off voltage, positive.**

- ·L4 p4: $V_{PO}$ is "the critical value of $V_{DS}$ when drain current becomes constant"; it is a
  point on the **horizontal ($V_{DS}$) axis** of Fig. 63.5 and Fig. 63.6, at $+4\ \mathrm{V}$.
- ·L4 p5: $V_{GS(off)} = -V_{PO}$, so $V_{PO}$ is the **positive** number.
- ·L4 p6 (footnote): "$V_p$ is numerically equal to $V_{GS(off)}$", i.e. $V_p = |V_{GS(off)}|$.
- ·L4 p7: $V_P = V_{DS(P)} - V_{GS}$, which for $V_{DS(P)} = 3\ \mathrm{V}$, $V_{GS} = -5\ \mathrm{V}$
  gives $V_P = +8\ \mathrm{V}$.
- ·L4 p15, tutorial problem 2: "$V_P = 8\ \mathrm{V}$", positive.

**Usage B — the gate cut-off voltage, negative.**

- ·L4 p6, Shockley's equation is printed as
  $I_D = I_{DSS}\left(1 - V_{GS}/V_P\right)^2 = I_{DSS}\left(1 - V_{GS}/V_{GS(off)}\right)^2$,
  which asserts $V_P = V_{GS(off)}$ — i.e. **negative** for an N-channel device.
- ·L4 p6, Fig. 63.6 carries the label $V_{GS} = -4\ \mathrm{V} = V_p$.
- ·L4 p7: "when $I_D = 0$, $V_{GS} = V_P$", and Fig. 63.7 prints $V_P$ under the $-4\ \mathrm{V}$
  tick of the $V_{GS}$ axis.
- ·L4 p8, Example 63.1: "$V_P = -3\ \mathrm{V}$"; ·L4 p11, Example 63.5: "$V_P = -5\ \mathrm{V}$";
  ·L4 p15, tutorial problem 6: "$V_P = -3.0\ \mathrm{V}$".

> ⚠ VERIFY **V4.2** ·L4 p6–p7 (and p4, p5, p8, p15) — **$V_P$ is used with both signs in one
> chapter.** Fig. 63.5, Fig. 63.6 and the p6 footnote place $V_P$ on the $V_{DS}$ axis as a positive
> voltage; Shockley's equation, Fig. 63.7, the statement "$I_D=0$ when $V_{GS}=V_P$" and every
> worked example use $V_P$ as the **negative** $V_{GS(off)}$. Nothing on the page resolves it.
> **The safe form of Shockley's equation — the one to write in an exam — names the cut-off voltage
> explicitly:**
> $$\boxed{\;I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_{GS(off)}}\right)^{2},\qquad
> V_{GS(off)} < 0 \text{ for an N-channel JFET}\;}$$
> **One-line self-check.** Put $V_{GS} = -1\ \mathrm{V}$ into a device with $|V_P| = 4\ \mathrm{V}$.
> With the negative value, $I_D = I_{DSS}(1 - 0.25)^2 = 0.56\,I_{DSS}$ — sensible. With the positive
> value, $I_D = I_{DSS}(1 + 0.25)^2 = 1.56\,I_{DSS}$ — **larger than $I_{DSS}$, impossible**.
> See `_verification-log.md`.

> ### [added] The working rule
>
> 1. **In Shockley's equation, the denominator is always $V_{GS(off)}$** — a negative number for an
>    N-channel device, positive for a P-channel one. If a question quotes "$V_P = 8\ \mathrm{V}$",
>    substitute $-8\ \mathrm{V}$.
> 2. **On a drain characteristic, $V_P$ is a positive point on the $V_{DS}$ axis.** Keep the two
>    readings apart by asking which axis the number belongs to.
> 3. The bridge between them, for any $V_{GS}$, is the chapter's own general relation (§4.6).

---

## 4.5 Static characteristics of a JFET ·L4 p5–p6

Two characteristics are studied, both taken with the JFET in the **common-source** connection of
Fig. 63.4: ·L4 p5

[def] **Drain characteristic** — $I_D$ against $V_{DS}$, for a family of values of $V_{GS}$ (the
"running variable").

[def] **Transfer characteristic** — $I_D$ against $V_{GS}$, for a constant $V_{DS}$.

### The drain characteristic with $V_{GS} = 0$ ·L4 p5–p6

[fig ·L4 p6] **Fig. 63.5 — the $V_{GS}=0$ drain characteristic, divided into four regions.**
Vertical axis $I_D$, horizontal axis $V_{DS}$, origin at 0. The curve rises steeply and linearly out
of the origin, bends over at a knee marked **A**, flattens to a horizontal plateau through point
**B**, runs flat at the level marked $I_{DSS}$ (a dashed horizontal line to the $I_D$ axis) as far as
point **C**, then turns sharply upward as a dashed curve. Dashed verticals drop from B and C to the
$V_{DS}$ axis at $V_P$ and $V_A$ respectively. Above the plot, three labelled spans: "Ohmic Region"
(with an arrow to the initial rise), "Pinch off (Saturation) Region" (the span from $V_P$ to $V_A$)
and "Breakdown Region" (beyond $V_A$). The plateau is labelled $V_{GS}=0$.

**1. Ohmic region OA** ·L4 p5 — linear; $I_D$ follows Ohm's law and the JFET behaves as an
**ordinary resistor** up to the knee A.

**2. Curve AB** ·L4 p6 — $I_D$ still rises but at a decreasing (inverse square-law) rate, up to
point B, the **pinch-off point**. The slowing is caused by the square-law growth of the depletion
regions. At B the two depletion regions are as close as they get **without touching**. The $V_{DS}$
at B is the pinch-off voltage $V_P$.

**3. Pinch-off region BC** ·L4 p6 — also called the **saturation** or **"amplified"** region. The
JFET acts as a **constant-current device**: as $V_{DS}$ rises the channel resistance rises in
proportion, holding $I_D$ at $I_{DSS}$. The reverse bias the gate-channel junction needs is supplied
**entirely by the voltage drop along the channel** caused by $I_{DSS}$ — none by external bias,
because $V_{GS}=0$. **This is the normal operating region for amplification.**

[eq: shockley] **Shockley's equation** — drain current in the pinch-off region ·L4 p6

$$\boxed{\;I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^{2}
= I_{DSS}\left(1 - \frac{V_{GS}}{V_{GS(off)}}\right)^{2}\;}$$

- $I_D$ — drain current, A
- $I_{DSS}$ — drain current at $V_{GS}=0$ in saturation, A
- $V_{GS}$ — gate-source voltage, V
- $V_{GS(off)}$ — gate-source cut-off voltage, V (negative for N-channel) — **see §4.4**

The squared term is why JFETs and MOSFETs are called **square-law devices** ·L4 p8 (footnote).

> ⚠ VERIFY **C4.5** ·L4 p6 — the second bracket of the printed equation begins with an italic
> capital **$I$** instead of the digit **1**: it reads $I_{DSS}\left(I - V_{GS}/V_{GS(off)}\right)^2$.
> The identical equation on ·L4 p7 prints the digit 1 correctly. Scan artefact; the digit is meant.
> See `_verification-log.md`.

> ⚠ VERIFY **C4.6** ·L4 p6 — the footnote is printed as "$V_p = /V_{GSC(off)}/$": the modulus bars
> have come through as forward slashes and the subscript has an extra C. It should read
> $V_p = |V_{GS(off)}|$. See `_verification-log.md`.

**4. Breakdown region** ·L4 p6 — beyond point C (the **avalanche breakdown voltage**) the
reverse-biased gate-channel junction avalanches and small changes in $V_{DS}$ produce very large
changes in $I_D$.

> **The three faces of a JFET, in order of increasing $V_{DS}$** ·L4 p6 — first a **resistor**
> (ohmic region), then a **constant-current source** (pinch-off region), finally a
> **constant-voltage source** (breakdown region).

---

## 4.6 Characteristics with external bias ·L4 p6–p7

[fig ·L4 p6] **Fig. 63.6 — the drain characteristic family.** Five curves of $I_D$ against $V_{DS}$,
one for each of $V_{GS} = 0,\,-1,\,-2,\,-3,\,-4\ \mathrm{V}$, stacked downwards in that order. Each
curve rises out of the origin, knees over and runs flat, then turns sharply upward at its own
breakdown voltage — and those breakdown voltages step **inwards** (to lower $V_{DS}$) as $V_{GS}$
goes more negative. The $V_{GS}=0$ plateau sits at $I_{DSS}$ (dashed line to the axis); dashed lines
mark each lower plateau. The $V_{DS}$ axis is ticked 1, 2, 3, 4 V, with $V_P$ marked near 4 V. The
bottom curve is labelled $V_{GS} = -4\ \mathrm{V} = V_p$ and lies flat along the axis — cut off.

As the negative gate bias is increased: ·L4 p6

1. **pinch-off is reached at a lower $I_D$** than when $V_{GS}=0$;
2. **the breakdown value of $V_{DS}$ falls.**

**Why.** ·L4 p7 With, say, $V_{GS} = -1\ \mathrm{V}$ applied, the junctions are already partly
depleted before any current flows. The channel therefore has to supply $1\ \mathrm{V}$ less of
reverse bias to reach pinch-off, so a **smaller channel drop — and hence a smaller $I_D$** — does the
job. With $V_P = 4\ \mathrm{V}$ the gate-channel junction always needs $4\ \mathrm{V}$ in total:

| $V_{GS}$ | drop needed along the channel | ·L4 p7 |
|---|---|---|
| $0$ | 4 V | $I_D = I_{DSS}$ |
| $-1\ \mathrm{V}$ | 3 V | reduced $I_D$ |
| $-2\ \mathrm{V}$ | 2 V | further reduced |
| $-3\ \mathrm{V}$ | 1 V | further reduced |
| $-4\ \mathrm{V}$ | 0 V | $I_D = 0$ (cut off) |

And the breakdown voltage falls because $V_{GS}$ **adds** to the reverse bias already produced by the
current flow. ·L4 p7

[eq: pinchoff-general] **The general pinch-off relation** ·L4 p7

$$\boxed{\;V_P = V_{DS(P)} - V_{GS}\;}$$

- $V_{DS(P)}$ — the value of $V_{DS}$ at which pinch-off occurs **for that $V_{GS}$**, V
- $V_P$ — the (positive) pinch-off voltage of the device, V

Rearranged for use: $V_{DS(P)} = V_P + V_{GS} = |V_P| - |V_{GS}|$ for an N-channel device. Check
against the table: $V_{GS} = -1\ \mathrm{V}$ gives $V_{DS(P)} = 3\ \mathrm{V}$ ✓.

---

## 4.7 Transfer characteristic ·L4 p7

[def] A plot of $I_D$ against $V_{GS}$ at **constant $V_{DS}$** — the same idea as the
transconductance characteristic of a vacuum tube or a BJT. ·L4 p7

Its two anchor points:

- at $V_{GS} = 0$, $\;I_D = I_{DSS}$
- at $I_D = 0$, $\;V_{GS} = V_P$ (read: $V_{GS(off)}$ — see §4.4)

[fig ·L4 p7] **Fig. 63.7 — transfer characteristic.** The $I_D$ axis is drawn on the **right**, with
$I_{DSS}$ marked at its top; the horizontal axis is $V_{GS}$, running **negative to the left** with
ticks at $-2\ \mathrm{V}$ and $-4\ \mathrm{V}$, the latter also labelled $V_P$. The curve leaves the
axis at $-4\ \mathrm{V}$ (zero current) and rises with increasing steepness to $I_{DSS}$ at
$V_{GS}=0$ — a parabola, concave upward. "$V_{DS}$ Constant" is printed inside the plot.

[eq: shockley-inverse] Inverting Shockley's equation for $V_{GS}$ ·L4 p7

$$\boxed{\;V_{GS} = V_{GS(off)}\left(1 - \sqrt{\frac{I_D}{I_{DSS}}}\right)\;}$$

[derivation added] Straight from §4.5's equation:

$$\frac{I_D}{I_{DSS}} = \left(1 - \frac{V_{GS}}{V_{GS(off)}}\right)^2$$

$$\sqrt{\frac{I_D}{I_{DSS}}} = 1 - \frac{V_{GS}}{V_{GS(off)}}$$

$$\frac{V_{GS}}{V_{GS(off)}} = 1 - \sqrt{\frac{I_D}{I_{DSS}}}$$

$$V_{GS} = V_{GS(off)}\left(1 - \sqrt{\frac{I_D}{I_{DSS}}}\right)$$

The transfer characteristic can also be **constructed from the drain characteristics**, by reading
off the saturated $I_D$ for each $V_{GS}$ curve at a fixed $V_{DS}$. ·L4 p7

---

## 4.8 Small-signal JFET parameters ·L4 p7–p8

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $r_d$ (or $r_{ds}$) | a.c. (dynamic) drain resistance | Ω | 100 kΩ |
| $y_{os}$ | output admittance, $= 1/r_d$ | S | 10 µS |
| $g_m$ (or $g_{fs}$, $y_{fs}$) | transconductance | S (siemens, formerly mho) | 1–6 mS |
| $g_{mo}$ | transconductance measured at $I_{DSS}$ (i.e. at $V_{GS}=0$) | S | 3–6 mS |
| $\mu$ | amplification factor | dimensionless | 100–300 |
| $R_{DS}$ | d.c. (static, ohmic) drain resistance | Ω | — |

### (i) A.C. drain resistance $r_d$ ·L4 p7

[def] The a.c. resistance between drain and source **with the JFET in the pinch-off region** — the
**slope** (strictly, the reciprocal slope) of the drain characteristic there. Also called the
**dynamic drain resistance**, and written $r_{ds}$. ·L4 p7–p8

[eq: ac-drain-resistance]

$$\boxed{\;r_d = \left.\frac{\Delta V_{DS}}{\Delta I_D}\right|_{V_{GS}\ \text{constant}}\;}$$

Since $r_d$ is the output resistance of the JFET, it is also quoted as an **output admittance**
$y_{os} = 1/r_d$, which is very small because $r_d$ is very large. ·L4 p8

> ⚠ VERIFY **V4.3** ·L4 p7 — the second form is printed as $r_d = \dfrac{V_{DS}}{I_D}\,|\,V_{GS}$,
> with no increment symbols, and the "constant" qualifier of the first form is printed as
> "$-V_{GS}$ constant" (a lost vertical bar). As printed, $V_{DS}/I_D$ is the **d.c.** drain
> resistance $R_{DS}$ — which the same chapter defines separately on ·L4 p8. Correct form:
> $$\boxed{\;r_d = \left.\frac{\delta V_{DS}}{\delta I_D}\right|_{V_{GS}}\;\neq\;\frac{V_{DS}}{I_D}\;}$$
> A ratio of totals is a chord; a ratio of increments is a slope, and only the slope is the
> small-signal parameter. See `_verification-log.md`.

### (ii) Transconductance $g_m$ ·L4 p8

[def] The **slope of the transfer characteristic**. Its unit is the **siemens (S)**, formerly the
mho. Also called **forward transconductance $g_{fs}$** or **forward transadmittance $y_{fs}$**. The
value measured at $I_{DSS}$ is written $g_{mo}$. ·L4 p8

[eq: transconductance]

$$\boxed{\;g_m = \left.\frac{\Delta I_D}{\Delta V_{GS}}\right|_{V_{DS}\ \text{constant}}\;}$$

> ⚠ VERIFY **V4.4** ·L4 p8 — the same increment loss occurs twice more on this page:
> $g_m$ is printed with a second form $\dfrac{I_D}{V_{GS}}\,|\,V_{DS}$, and the amplification factor
> as $\mu = \dfrac{V_{DS}}{V_{GS}}\,|\,I_D$. Both are ratios of **totals**, not increments; taken
> literally they give the wrong number (for Example 63.1's device evaluated at $V_{GS} = -2\ \mathrm{V}$ — the example itself is worked at $-1\ \mathrm{V}$ — the ratio of totals gives
> $0.967\ \mathrm{mA}/2\ \mathrm{V} = 0.48\ \mathrm{mS}$ where the true $g_m$ is
> $1.93\ \mathrm{mS}$ — out by a factor of four). Correct forms:
> $$\boxed{\;g_m = \left.\frac{\delta I_D}{\delta V_{GS}}\right|_{V_{DS}},\qquad
> \mu = \left.\frac{\delta V_{DS}}{\delta V_{GS}}\right|_{I_D}\;}$$
> See `_verification-log.md`.

[derivation] **Mathematical expression for $g_m$** ·L4 p8 — differentiate Shockley's equation with
respect to $V_{GS}$:

$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^{2}$$

$$\frac{dI_D}{dV_{GS}} = 2I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)\left(-\frac{1}{V_P}\right)$$

[eq] $$\boxed{\;g_m = -\frac{2I_{DSS}}{V_P}\left(1 - \frac{V_{GS}}{V_P}\right)\;}$$

[eq: gmo] At $V_{GS} = 0$, $g_m$ takes its largest value $g_{mo}$: ·L4 p8

$$\boxed{\;g_{mo} = -\frac{2I_{DSS}}{V_P} = \frac{2I_{DSS}}{|V_{GS(off)}|}\;}$$

[eq: gm-from-gmo] Dividing the two: ·L4 p8

$$\boxed{\;g_m = g_{mo}\left(1 - \frac{V_{GS}}{V_P}\right) = g_{mo}\sqrt{\frac{I_D}{I_{DSS}}}\;}$$

> ⚠ VERIFY **V4.5** ·L4 p8 — the differentiation line is printed with the left-hand side
> $\dfrac{dI_D}{dI_{DSS}}$. Shockley's equation is being differentiated **with respect to $V_{GS}$**
> (the right-hand side carries the chain-rule factor $-1/V_P$, which can only come from
> $d(V_{GS}/V_P)/dV_{GS}$), and the result is then named $g_m$, which is $\delta I_D/\delta V_{GS}$
> by definition. Correct form:
> $$\boxed{\;\frac{dI_D}{dV_{GS}} = 2I_{DSS}\left(1-\frac{V_{GS}}{V_P}\right)\left(-\frac{1}{V_P}\right)\;}$$
> A derivative with respect to $I_{DSS}$ would carry units of A/A, not A/V. See `_verification-log.md`.

> ⚠ VERIFY **V4.6** ·L4 p8 — the combined result is printed as
> $g_m = g_{mo}\left(1 - \dfrac{V_{DSS}}{V_P}\right) = g_{mo}\sqrt{I_D/I_{DSS}}$. **There is no
> quantity $V_{DSS}$** anywhere in the chapter; the symbol required is $V_{GS}$, as the two equations
> being combined both show, and as Example 63.1 (iii) confirms by substituting $V_{GS}=-1\ \mathrm{V}$.
> Correct form:
> $$\boxed{\;g_m = g_{mo}\left(1 - \frac{V_{GS}}{V_P}\right)\;}$$
> See `_verification-log.md`.

### (iii) Amplification factor $\mu$ ·L4 p8

[def] The change in $V_{DS}$ needed to offset a change in $V_{GS}$ at constant $I_D$.

[eq: amplification-factor]

$$\boxed{\;\mu = \left.\frac{\delta V_{DS}}{\delta V_{GS}}\right|_{I_D}
\qquad\text{and}\qquad \mu = g_m \times r_d = g_{fs}\times r_d\;}$$

[added] The product form is worth a sanity check: $g_m$ in S multiplied by $r_d$ in Ω is
dimensionless ✓, as an amplification factor must be.

### (iv) D.C. drain resistance $R_{DS}$ ·L4 p8

[def] The **static** or **ohmic** resistance of the channel — a ratio of totals, not increments.

[eq: dc-drain-resistance]

$$\boxed{\;R_{DS} = \frac{V_{DS}}{I_D}\;}$$

---

### [ex] Example 63.1 ·L4 p8

> For an N-channel JFET, $I_{DSS} = 8.7\ \mathrm{mA}$, $V_P = -3\ \mathrm{V}$,
> $V_{GS} = -1\ \mathrm{V}$. Find (i) $I_D$, (ii) $g_{mo}$, (iii) $g_m$.
> *(Basic Electronics, Bombay Univ., 1985)*

**(i)** Shockley's equation, with $V_P$ used in its **negative** (cut-off) sense — see §4.4:

$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^{2}
= 8.7\left(1 - \frac{-1\ \mathrm{V}}{-3\ \mathrm{V}}\right)^{2}$$

$$I_D = 8.7\,(1 - 0.3333)^2 = 8.7\times 0.4444 = 3.87\ \mathrm{mA}$$

**(ii)** $$g_{mo} = -\frac{2I_{DSS}}{V_P} = \frac{-2\times 8.7}{-3} = 5.8\ \mathrm{mS}$$

**(iii)** $$g_m = g_{mo}\left(1 - \frac{V_{GS}}{V_P}\right) = 5.8\left(1 - \frac{-1}{-3}\right)
= 5.8\times 0.6667 = 3.87\ \mathrm{mS}$$

*[added] Verified: $8.7\times(2/3)^2 = 3.8667\ \mathrm{mA}$ ✓; $2\times 8.7/3 = 5.8\ \mathrm{mS}$ ✓;
$5.8\times 2/3 = 3.8667\ \mathrm{mS}$ ✓. Note the coincidence that (i) and (iii) share the digits
3.87 — different quantities, different units.*

> ⚠ VERIFY **V4.7** ·L4 p8 — part (i) prints the answer as **3.87 A**. The data are in
> milliamperes ($I_{DSS} = 8.7\ \mathrm{mA}$) and Shockley's equation is linear in $I_{DSS}$, so the
> answer inherits the unit. Correct:
> $$\boxed{\;I_D = 3.87\ \mathrm{mA}\;}$$
> A JFET passing 3.87 A would dissipate tens of watts. See `_verification-log.md`.


---

## 4.9 D.C. biasing of a JFET ·L4 p9

Four schemes are given. ·L4 p9

[fig ·L4 p9] **Fig. 63.8 — the four bias circuits, drawn side by side.** In all four the JFET sits
with its drain at the top through the drain load $R_L$ to $+V_{DD}$, the input $v_{in}$ entering at
the gate, and $V_{GS}$ marked across gate-to-source with its polarity signs.

- **(a) Gate bias** — the gate returns through $R_G$ to a separate negative supply $-V_{GG}$; the
  source goes straight to ground. No source resistor.
- **(b) Self-bias** — the gate returns through $R_G$ to ground; the source goes to ground through
  $R_S$, across which $V_S$ is marked.
- **(c) Source bias** — as (b), but the bottom of $R_S$ goes to a negative supply $-V_{SS}$ instead
  of ground.
- **(d) Voltage-divider bias** — $R_1$ from $+V_{DD}$ and $R_2$ to ground form a divider feeding the
  gate, with $V_2$ marked across $R_2$; the source again returns through $R_S$.

### Self-bias ·L4 p9

The bias is generated by the JFET's **own drain current** flowing through $R_S$.

[eq: self-bias]

$$V_S = I_D R_S \qquad\Longrightarrow\qquad \boxed{\;V_{GS} = -I_D R_S\;}$$

- $V_S$ — source-to-ground voltage, V
- $R_S$ — source resistor, Ω

The gate sits at this much **negative** potential with respect to the source. ·L4 p9

**Why $R_G$ does not disturb the bias, and why it must be there anyway** ·L4 p9 — no gate current
flows through $R_G$ (gate leakage is almost zero), so it drops no voltage and the gate is
essentially at **d.c. ground**. Its three jobs:

1. without it the gate would **float**, collect charge and eventually cut the JFET off;
2. it stops the a.c. input $v_{in}$ from being **short-circuited** to ground;
3. it gives any leakage current an **escape route** — otherwise leakage would build up a static
   voltage at the gate that could shift the bias or destroy the device.

### Source bias ·L4 p9

[eq: source-bias]

$$V_{SS} = I_D R_S + V_{GS} \qquad\Longrightarrow\qquad \boxed{\;V_{GS} = V_{SS} - I_D R_S\;}$$

- $V_{SS}$ — magnitude of the negative source supply, V

*[added] Sign check: the gate is at 0 V, so $V_S = -V_{GS}$; the source node also sits at
$-V_{SS} + I_D R_S$ above the negative rail. Equating gives the boxed result, and $V_{GS}$ comes out
negative whenever $I_D R_S > V_{SS}$, which is the normal design condition.*

### Voltage-divider bias ·L4 p9

[eq: divider-bias]

$$V_2 = V_{DD}\frac{R_2}{R_1+R_2},\qquad V_2 = V_{GS} + I_D R_S$$

$$\boxed{\;V_{GS} = V_{DD}\frac{R_2}{R_1+R_2} - I_D R_S\;}$$

---

### [ex] Example 63.2 ·L4 p9

> Find the values of $V_{DS}$ and $V_{GS}$ in Fig. 63.9 for $I_D = 4\ \mathrm{mA}$.
> *(Applied Electronics-I, Punjab Univ. 1992)*

[fig ·L4 p10] **Fig. 63.9** — self-bias circuit: $V_{DD} = 12\ \mathrm{V}$ at the top,
$R_L = 1.5\ \mathrm{k\Omega}$ in the drain, the JFET below it, $R_S = 500\ \Omega$ from source to
ground, gate returned through $R_G$ to ground ($V_G = 0$). $V_D$, $V_S$ and $V_{DS}$ are marked as
vertical arrows against the ground rail.

$$V_S = I_D R_S = 4\times10^{-3}\times 500 = 2.0\ \mathrm{V}$$

$$V_D = V_{DD} - I_D R_L = 12 - 4\times 1.5 = 6\ \mathrm{V}$$

$$V_{DS} = V_D - V_S = 6 - 2 = 4\ \mathrm{V}$$

$$V_{GS} = V_G - V_S = 0 - 2.0 = -2.0\ \mathrm{V}$$

*[added] Verified: $4\ \mathrm{mA}\times 500\ \Omega = 2\ \mathrm{V}$ ✓;
$4\ \mathrm{mA}\times1.5\ \mathrm{k\Omega} = 6\ \mathrm{V}$ so $V_D = 6\ \mathrm{V}$ ✓;
$V_{DS} = 4\ \mathrm{V}$ ✓; $V_{GS} = -2\ \mathrm{V}$ ✓. All four values consistent.*

---

## 4.10 The d.c. load line and the Q-point ·L4 p9–p11

[eq: load-line] The two end points of the d.c. load line ·L4 p9

$$\boxed{\;\text{at } I_D = 0:\; V_{DS} = V_{DD};\qquad \text{at } V_{DS}=0:\; I_D = \frac{V_{DD}}{R_L}\;}$$

> [added] **Caution.** These two points assume the **only** resistance in the drain-source loop is
> $R_L$ — true for Fig. 63.8 (*a*), but not when a source resistor is present. With $R_S$ in circuit
> the current intercept is $V_{DD}/(R_L+R_S)$, which is exactly what the chapter's own $I_{DSQ}$
> formula below uses. ·L4 p9 vs ·L4 p10

For **class-A** operation the Q-point is put at the middle of the load line: ·L4 p10

[eq: midpoint-bias]

$$\boxed{\;V_{DSQ} = \tfrac12 V_{DD},\qquad I_{DSQ} = \frac{\tfrac12 V_{DD}}{R_S + R_L}\;}$$

[fig ·L4 p10] **Fig. 63.10 — load line on the drain characteristics.** The $I_D$ axis is vertical,
$V_{DS}$ horizontal. A straight line runs from $V_{DD}/R_L$ on the $I_D$ axis down to $V_{DD}$ on the
$V_{DS}$ axis. Two drain-characteristic curves rise and flatten beneath it. The load line crosses the
upper curve at **Q**, from which a horizontal dashed line runs left to $I_{DQ}$ on the current axis
and a vertical dashed line runs down to $V_{DSQ}$ on the voltage axis.

---

### [ex] Example 63.3 ·L4 p10

> For the circuit of Fig. 63.11, find $V_{DSQ}$ and $V_{GS}$ assuming a centrally-located Q-point and
> zero gate current.

[fig ·L4 p10] **Fig. 63.11** — self-bias: $12\ \mathrm{V}$ supply, $R_L = 450\ \Omega$ in the drain,
$R_S = 150\ \Omega$ in the source, $R_G = 10\ \mathrm{M\Omega}$ from gate to ground, $V_{GS}$ marked
across the gate-source with the source positive.

Since $I_G = 0$, the d.c. circuit is undisturbed by $R_G$.

$$V_{DS} = \tfrac12 V_{DD} = \frac{12}{2} = 6\ \mathrm{V}$$

The remaining 6 V is dropped across $R_L$ and $R_S$ in series:

$$I_D = \frac{6}{150+450} = 10\ \mathrm{mA}$$

$$V_{GS} = -I_D R_S = -10\ \mathrm{mA}\times150\ \Omega = -1.5\ \mathrm{V}$$

The gate is 1.5 V negative with respect to the source. ·L4 p10 adds the general remark that **in a
common-source JFET the gate is the most negative point in the whole circuit.**

*[added] Verified: $6/600 = 0.01\ \mathrm{A} = 10\ \mathrm{mA}$ ✓;
$10\ \mathrm{mA}\times150\ \Omega = 1.5\ \mathrm{V}$ ✓.*

> ⚠ VERIFY **V4.8** ·L4 p10 — the last line is printed as
> $V_{GS} = -I_D R_S = -10\times150 = \mathbf{1.5\ V}$ — the bold answer has **lost its minus sign**,
> though the left-hand side of the same line carries it and the sentence underneath says the gate is
> "1.5 V negative". Correct:
> $$\boxed{\;V_{GS} = -1.5\ \mathrm{V}\;}$$
> A positive $V_{GS}$ on an N-channel JFET would forward-bias the gate junction. See
> `_verification-log.md`.

---

### [ex] Example 63.4 ·L4 p10–p11

> What values of $R_S$ and $R_L$ are required for the circuit of Fig. 63.12 to set up approximate
> mid-point bias? The JFET parameters are $I_{DSS} = 16\ \mathrm{mA}$, $V_{GS(off)} = -8\ \mathrm{V}$
> and $V_D = \tfrac12 V_{DD}$.

[fig ·L4 p10] **Fig. 63.12** — self-bias skeleton: $+V_{DD} = 16\ \mathrm{V}$, $R_L$ (value to be
found) in the drain, $I_D$ marked downward in the drain lead, $R_G$ from gate to ground, $R_S$ (value
to be found) from source to ground.

**The mid-point bias conditions** ·L4 p11

$$I_D \cong \frac{I_{DSS}}{2}, \qquad V_{GS} = \frac{V_{GS(off)}}{4}$$

$$I_D \cong \frac{16}{2} = 8\ \mathrm{mA}$$

$$V_{GS} = \tfrac14 V_{GS(off)} = -\frac{8}{4} = -2\ \mathrm{V}$$

$$R_S = \frac{|V_{GS}|}{I_D} = \frac{2\ \mathrm{V}}{8\ \mathrm{mA}} = 250\ \Omega$$

$$V_D = V_{DD} - I_D R_L \quad\Longrightarrow\quad
R_L = \frac{V_{DD} - V_D}{I_D} = \frac{16-8}{8\ \mathrm{mA}} = 1000\ \Omega$$

*[added] Verified: $2/0.008 = 250\ \Omega$ ✓; $8/0.008 = 1000\ \Omega$ ✓.*

> [added] **Where the mid-point rule comes from.** Put $V_{GS} = V_{GS(off)}/4$ into Shockley's
> equation:
> $$I_D = I_{DSS}\left(1 - \tfrac14\right)^2 = 0.5625\,I_{DSS}$$
> which is why the chapter writes $I_D \cong I_{DSS}/2$ with a "congruent" sign, not an equals sign.
> The rule is a **design approximation**, good to about 12 %.

---

### [ex] Example 63.5 ·L4 p11

> Determine the quiescent values of $V_{GS}$, $I_D$ and $V_{DS}$ for the JFET circuit of Fig. 63.13,
> given $I_{DSS} = 10\ \mathrm{mA}$, $R_S = 5\ \mathrm{k\Omega}$ and $V_P = -5\ \mathrm{V}$.
> *(Electronic Devices & Circuits, Pune Univ. 1991)*

[fig ·L4 p11] **Fig. 63.13** — a complete common-source stage: $12\ \mathrm{V}$ rail at the top,
$R_L$ in the drain (**no value printed on the figure**), coupling capacitor $C_2$ from the drain to
the output $V_o$, input $V_i$ through $C_1$ to the gate, $R_G$ from gate to ground (no value
printed), $R_S = 5\ \mathrm{k\Omega}$ from source to ground bypassed by $C_3$, and $I_D$ arrowed
downward in the drain lead.

Because $I_G \cong 0$, $I_S \cong I_D$ and self-bias gives

$$V_{GS} = -I_D R_S = -5000\,I_D$$

Substituting Shockley's equation with $V_P = -5\ \mathrm{V}$:

$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2
= 10\times10^{-3}\left(1 - \frac{V_{GS}}{-5}\right)^2
= 10\times10^{-3}\left(1 + 0.2\,V_{GS}\right)^2$$

$$V_{GS} = -5000\left(10\times10^{-3}\right)\left(1 + 0.2V_{GS}\right)^2 = -50\left(1+0.2V_{GS}\right)^2$$

Expanding and rearranging:

$$2V_{GS}^{2} + 21V_{GS} + 50 = 0$$

$$V_{GS} = -3.65\ \mathrm{V}\quad\text{or}\quad -6.85\ \mathrm{V}$$

The second root is rejected: it is **beyond $V_P$**, where the device is already cut off. So

$$V_{GS} = -3.65\ \mathrm{V}$$

$$-3.65 = -5000\,I_D \quad\Longrightarrow\quad I_D = 0.73\ \mathrm{mA}$$

$$V_D = V_{DD} - I_D R_L = 12 - 0.73\times 2 = 10.54\ \mathrm{V}$$

$$V_S = I_D R_S = 0.73\times 5 = 3.65\ \mathrm{V}$$

$$V_{DS} = V_D - V_S = 10.54 - 3.65 = 6.89\ \mathrm{V}$$

*[added] Verified. Expansion:
$V_{GS} = -50(1 + 0.4V_{GS} + 0.04V_{GS}^2) = -50 - 20V_{GS} - 2V_{GS}^2$,
giving $2V_{GS}^2 + 21V_{GS} + 50 = 0$ ✓. Roots
$\left(-21 \pm \sqrt{441-400}\right)/4 = -3.649$ and $-6.851$ ✓. Then
$3.65/5000 = 0.73\ \mathrm{mA}$ ✓, $0.73\times5 = 3.65\ \mathrm{V}$ ✓,
$10.54 - 3.65 = 6.89\ \mathrm{V}$ ✓.*

> ⚠ VERIFY **V4.9** ·L4 p11 — the drain-voltage line prints
> $V_D = 12 - 0.73\times 2 = \mathbf{1.54\ V}$. The arithmetic gives $12 - 1.46 = 10.54\ \mathrm{V}$,
> and the **very next line of the same solution uses 10.54 V** to get $V_{DS} = 6.89\ \mathrm{V}$.
> Correct:
> $$\boxed{\;V_D = 10.54\ \mathrm{V}\;}$$
> A leading digit has been dropped in typesetting. See `_verification-log.md`.

> ⚠ VERIFY **V4.10** ·L4 p11 — the same line uses $R_L = 2\ \mathrm{k\Omega}$, a value that appears
> **nowhere in the question and nowhere on Fig. 63.13**, where the drain resistor is drawn unlabelled.
> The example cannot be reproduced from the data as printed. Take
> $$\boxed{\;R_L = 2\ \mathrm{k\Omega}\;\text{(inferred from the working, not given)}\;}$$
> $V_{GS}$ and $I_D$ do not depend on $R_L$ and are unaffected; $V_D$ and $V_{DS}$ do.
> See `_verification-log.md`.

---

## 4.11 Common-source JFET amplifier ·L4 p11

[fig ·L4 p11] **Fig. 63.14 — the CS amplifier.** $+V_{DD}$ at the top; drain load $R_L$ down to the
drain; output coupling capacitor $C_2$ from drain to $V_{out}$; input $V_{in}$ through $C_1$ to the
gate; $R_G$ from gate to ground; $R_S$ from source to ground, bypassed by $C_3$. Small square
waveforms are drawn at input and output, **inverted** with respect to each other.

Component roles ·L4 p11

| Part | Job |
|---|---|
| $R_G$ | provides a leakage path for the gate current; sets the gate at d.c. ground |
| $R_S$ | develops the gate bias ($V_{GS} = -I_D R_S$) |
| $C_3$ | provides an a.c. ground at the source, so the bias is not degenerated by the signal |
| $R_L$ | acts as the drain load — converts the signal current into a signal voltage |

**Working — a negative-going input, step by step** ·L4 p11

1. gate bias is increased (more negative),
2. depletion regions widen,
3. channel resistance increases,
4. $I_D$ decreases,
5. the drop across $R_L$ decreases,
6. so the drain voltage **rises** — a **positive-going** output appears through $C_2$.

A positive-going input does the reverse. Hence a common-source amplifier produces
**phase inversion** between gate and drain. ·L4 p11

---

## 4.12 JFET amplifier gains ·L4 p12–p15

[fig ·L4 p12] **Fig. 63.15 — the JFET's internal capacitances.** The device symbol is drawn inside a
dashed circle. $C_{gd}$ bridges gate to drain, $C_{gs}$ bridges gate to source, and a third capacitor
bridges drain to source on the right-hand side.

> ⚠ VERIFY **C4.7** ·L4 p12 — the drain-to-source capacitor in Fig. 63.15 is labelled **$C_{dl}$**.
> Every other capacitance in the figure is named by its two terminals, and this one connects **d** to
> **s**; the label required is $C_{ds}$, which is what Example 63.14 (·L4 p22) calls it.
> See `_verification-log.md`.

### (a) Common-source amplifier ·L4 p12

[fig ·L4 p12] **Fig. 63.16.** (*a*) the CS circuit again, with $r'_i$ arrowed at the gate terminal,
$r_i$ arrowed into $R_G$ and $r'_o$ arrowed back into the drain. (*b*) its a.c. equivalent: gate G at
the top left, source S at the bottom rail, drain D at the top right. Across the input, $V_i$ and
$R_G$; on the output side, a current source $-g_m v_i$ (drawn as a diamond, arrow upward) in parallel
with $r_d$ and $R_L$, with $V_o$ taken across them and the drain current $i_d$ marked at the top.

**(i) Input resistance** ·L4 p12

$$r'_i = R_G \parallel R_{GS} \cong R_G$$

$R_{GS}$ is infinite in an ideal JFET (since $I_G = 0$) and about $100\ \mathrm{M\Omega}$ in a real
one — far larger than $R_G$, so $R_G$ dominates.

**(ii) Output resistance** ·L4 p12

$$r'_o = r_d \parallel R_L \cong R_L \quad\text{when } r_d \gg R_L$$

**(iii) Voltage gain** ·L4 p12

[derivation]

$$V_o = i_d\times\left(r_d\parallel R_L\right), \qquad i_d = -g_m v_i$$

$$V_o = -g_m V_i \left(r_d\parallel R_L\right)$$

[eq: av-common-source]

$$\boxed{\;A_v = \frac{V_o}{V_i} = -g_m\left(r_d\parallel R_L\right)
= \frac{-g_m r_d R_L}{r_d + R_L} = \frac{-\mu R_L}{r_d+R_L}\;}$$

The chapter also writes it with the data-sheet symbol: $A_v = -g_{fs}\left(r_d\parallel R_L\right)$.
The minus sign **is** the phase inversion of §4.11.

**(iv) Input capacitance** ·L4 p12

The input capacitance is $C_{gs}$, **increased by the Miller effect**:

[eq: miller-input-capacitance-fet]

$$\boxed{\;C_i = C_{gs} + \left(1 - A_v\right)C_{gd}\;}$$

Because $A_v$ is negative, $(1-A_v)$ is larger than 1 — for a gain of $-27$ the multiplier is 28.
It is this **magnified** $C_{gd}$ that limits high-frequency work. ·L4 p12

---

### [ex] Example 63.6 ·L4 p12

> The common-source amplifier of Fig. 63.16 (*a*) has $r_d = 100\ \mathrm{k\Omega}$,
> $R_L = 10\ \mathrm{k\Omega}$, $g_m = 3000\ \mathrm{\mu S}$, $C_{gs} = 3\ \mathrm{pF}$ and
> $C_{gd} = 1.5\ \mathrm{pF}$. Compute (i) $A_v$ and (ii) $C_i$.

**(i)**

$$A_v = \frac{-g_m r_d R_L}{r_d + R_L}
= \frac{-3000\times10^{-6}\times100\times10^{3}\times10\times10^{3}}
{\left(100\times10^{3}\right)+\left(10\times10^{3}\right)} = -27.3$$

**(ii)**

$$C_i = C_{gs} + \left(1 - A_v\right)C_{gd} = 3 + \left(1+27.3\right)\times1.5 = 45.5\ \mathrm{pF}$$

*[added] Verified: $r_d\parallel R_L = 10^{9}/1.1\times10^{5} = 9.09\ \mathrm{k\Omega}$, so
$A_v = -3\times10^{-3}\times9.09\times10^{3} = -27.27$ ✓ (quoted as $-27.3$);
$3 + 28.3\times1.5 = 45.45\ \mathrm{pF}$ ✓ (quoted as 45.5 pF). Note the input capacitance comes out at
**thirty times** $C_{gd}$, and fifteen times $C_{gs}$ — the Miller effect in one number.*

---

### [ex] Example 63.7 ·L4 p13

> The JFET of Fig. 63.17 has $g_m = 3000\ \mathrm{\mu S}$ and $r_{ds} = 100\ \mathrm{k\Omega}$.
> Calculate the voltage gain of the CS amplifier circuit.
> *(Basic Electronics, Bombay Univ. 1992)*

[fig ·L4 p12] **Fig. 63.17** — CS stage: $18\ \mathrm{V}$ rail, $10\ \mathrm{k\Omega}$ drain
resistor, output through $C_2$ into a $10\ \mathrm{k\Omega}$ external load, signal source (drawn as a
sine generator) through $C_1$ to the gate, $10\ \mathrm{M\Omega}$ gate resistor to ground,
$500\ \Omega$ source resistor bypassed by $C_3$.

$$A_v = -g_m\left(r_{ds}\parallel r_L\right)$$

$$r_L = 10\ \mathrm{k\Omega}\parallel 10\ \mathrm{k\Omega} = 5\ \mathrm{k\Omega}$$

$$r_{ds}\parallel r_L = 100\ \mathrm{k\Omega}\parallel 5\ \mathrm{k\Omega} = 4.76\ \mathrm{k\Omega}$$

$$A_v = -3000\times10^{-6}\times 4.76\times10^{3} = -14.3$$

*[added] Verified: $100\times5/105 = 4.762\ \mathrm{k\Omega}$ ✓;
$3\times10^{-3}\times4762 = 14.29$ ✓. Note that the a.c. load is the **parallel** combination of the
drain resistor and the external load — the coupling capacitor $C_2$ puts them in parallel for
signals.*

> ⚠ VERIFY **C4.8** ·L4 p13 — the final line is printed
> $A_v = -3000\times10^{-6}\times 4.76 = -14.3$, dropping the factor $10^{3}$ that turns
> $4.76\ \mathrm{k\Omega}$ into ohms. As printed the arithmetic gives $-0.0143$. The intended
> substitution is $4.76\times10^{3}\ \Omega$. See `_verification-log.md`.

### (b) Common-drain amplifier (source follower) ·L4 p13–p14

The load is in **series with the source**; there is **no drain resistor**. Input at the gate through
$C_1$, output from the source through $C_2$. ·L4 p13

[fig ·L4 p13] **Fig. 63.18.** (*a*) circuit: $+V_{DD}$ at the top with the drain connected
**directly** to it; a divider $R_1$ (to $+V_{DD}$) and $R_2$ (to ground) biases the gate, fed by
$V_i$ through $C_1$; $R_L$ from source to ground with $V_o$ taken from the source through $C_2$;
input and output square waveforms drawn **in phase**. (*b*) a.c. equivalent: G at the top left, **D
at the bottom rail** and **S at the top right** (the drain is the common terminal); $V_i$ across
$R_1\parallel R_2$; a current source $g_m V_{gs}$ feeding $r_d$ and $R_L$ in parallel, with $V_o$
across them and $i_d$ marked at the top.

The controlling voltage is no longer the input voltage, because the source moves with the output:

$$v_{gs} = V_i - V_o, \qquad R_G = R_1\parallel R_2$$

> ⚠ VERIFY **C4.9** ·L4 p13 — the sentence introducing the equivalent circuit reads "The current
> generator is $g_m,\ V_{gs}$" — a comma where a multiplication is meant. Read
> $g_m V_{gs}$, as Fig. 63.18 (*b*) itself labels the source. See `_verification-log.md`.

[derivation] **(i) Voltage gain** ·L4 p13

$$V_o = i_d\left(r_d\parallel R_L\right), \qquad i_d = g_m v_{gs} = g_m\left(V_i - V_o\right)$$

$$V_o = g_m\left(V_i-V_o\right)\frac{r_d R_L}{r_d+R_L}$$

$$V_o\left[1 + \frac{g_m r_d R_L}{r_d+R_L}\right] = g_m V_i \frac{r_d R_L}{r_d + R_L}$$

$$V_o = g_m V_i \frac{r_d R_L}{r_d + R_L + g_m r_d R_L} \qquad \ldots(i)$$

[eq: av-common-drain]

$$\boxed{\;A_v = \frac{V_o}{V_i} = \frac{g_m r_d R_L}{r_d + R_L + g_m r_d R_L}\;\cong\;1
\quad\text{when } g_m r_d R_L \gg \left(r_d + R_L\right)\;}$$

> ⚠ VERIFY **V4.11** ·L4 p13 — the boxed gain is printed **without $g_m$ in the numerator**:
> $A_v = \dfrac{r_d R_L}{r_d + R_L + g_m r_d R_L}$. Two reasons this cannot stand: (1) the numerator
> then has units of $\Omega^2$ while the denominator has units of $\Omega$, so the "gain" would carry
> units of ohms; (2) it does not follow from the chapter's own equation (i) one line above, which
> carries the factor $g_m$. **Example 63.8 on the next page uses the correct form with $g_m$.**
> Correct:
> $$\boxed{\;A_v = \frac{g_m r_d R_L}{r_d+R_L+g_m r_d R_L}\;}$$
> See `_verification-log.md`.

**(ii) Input resistance** ·L4 p13 — for the circuit of Fig. 63.18 (*a*) only:

$$\boxed{\;r'_{in} = R_1 \parallel R_2\;}$$

[derivation] **(iii) Output resistance** ·L4 p13 — in equation (i), $g_m V_i$ is a current
proportional to $V_i$, so everything multiplying it is a resistance:

$$r'_o = \frac{r_d R_L}{r_d + R_L\left(1 + g_m r_d\right)}
= \frac{\left[r_d/(1+g_m r_d)\right]\times R_L}{\left[r_d/(1+g_m r_d)\right] + R_L}$$

[eq: ro-common-drain]

$$\boxed{\;r'_o = \frac{r_d}{1+g_m r_d}\;\parallel\;R_L \;\cong\; \frac{1}{g_m}\parallel R_L\;}$$

the approximation holding when $g_m r_d \gg 1$ — which it always is, since $g_m r_d = \mu$.

[fig ·L4 p13] **Fig. 63.19 — modified common-drain equivalent circuit.** A current source $g_m V_i$
on the left, in parallel with a resistor labelled $\dfrac{r_d}{1+g_m r_d}$ and with $R_L$; $V_o$ is
taken across the pair on the right and $r'_o$ is arrowed back into the network.

---

### [ex] Example 63.8 ·L4 p14

> The common-drain circuit of Fig. 63.18 (*a*) uses a JFET with $r_d = 100\ \mathrm{k\Omega}$,
> $g_m = 3000\ \mathrm{\mu S}$ and $R_L = 10\ \mathrm{k\Omega}$. Calculate (i) $A_v$ and (ii) $r'_o$.

**(i)**

$$A_v = g_m\frac{r_d R_L}{r_d+R_L+g_m r_d R_L}
= 3000\times10^{-6}\times
\frac{100\times10^{3}\times10\times10^{3}}
{\left(100\times10^{3}\right)+\left(10\times10^{3}\right)+\left(3000\times10^{-6}\times100\times10^{3}\times10\times10^{3}\right)}$$

$$A_v = 0.965$$

**(ii)**

$$\frac{r_d}{1+g_m r_d} = \frac{100\times10^{3}}{1 + 3000\times10^{-6}\times100\times10^{3}} = 330\ \Omega$$

$$r'_o = 10\ \mathrm{k\Omega}\parallel 330\ \Omega \cong 320\ \Omega$$

*[added] Verified: denominator $= 110\times10^{3} + 3\times10^{6} = 3.11\times10^{6}$; numerator
$= 10^{9}$; ratio $= 321.5$; $\times 3\times10^{-3} = 0.9646$ ✓ (quoted 0.965).
$100\,000/301 = 332\ \Omega$ (quoted 330 Ω, rounded);
$10\,000\times330/10\,330 = 319.5\ \Omega$ ✓ (quoted 320 Ω). **The point of the example:** gain just
under unity and an output resistance of a few hundred ohms — the source follower buffers, it does not
amplify.*

### (c) Common-gate amplifier ·L4 p14–p15

Input at the **source**, output from the **drain**, gate **grounded**. $R_L$ is in series with the
drain and a source resistance $R_S$ carries the input. ·L4 p14

[fig ·L4 p14] **Fig. 63.20.** (*a*) circuit: input $V_i$ through $C_1$ to the source (with a square
waveform drawn at the input), $R_S$ from source to ground, the gate taken to ground, $R_L$ from the
drain up to $V_{DD}$, output $V_o$ through $C_2$ from the drain, with an **in-phase** output waveform
drawn. (*b*) a.c. equivalent: **S at the top left, D at the top right, G along the bottom rail**;
$V_i$ across $R_S$; the current source $g_m v_{gs}$ (diamond) drawn between source and drain — "the
current source is connected between the drain and the source terminals as always", but since source
and drain are now input and output, it appears **between input and output**; $r_d$ and $R_L$ in
parallel at the output with $V_o$ across them and $r'_o$ arrowed in.

**(i) Voltage gain** ·L4 p14

$$V_o = i_d\left(r_d\parallel R_L\right) = i_d\frac{r_d R_L}{r_d+R_L},
\qquad i_d = g_m V_{gs} = g_m V_i$$

[eq: av-common-gate]

$$\boxed{\;A_v = \frac{V_o}{V_i} = \frac{g_m r_d R_L}{r_d+R_L} = +g_m\left(r_d\parallel R_L\right)\;}$$

Same magnitude as the common-source gain but **positive**: $V_o$ and $V_i$ are **in phase**. ·L4 p14

> ⚠ VERIFY **C4.10** ·L4 p14 — the step "$i_d = g_m V_{gs} = g_m V_i$" is written as though
> $V_{gs} = V_i$. With the gate grounded and the signal applied to the source,
> $V_{gs} = V_g - V_s = -V_i$. The published result is nevertheless the standard one, because
> Fig. 63.20 (*b*) draws the current-source arrow **reversed** relative to the common-source
> equivalent, which absorbs the sign. Written out with both conventions explicit:
> $$\boxed{\;i_d = -g_m V_{gs} = +g_m V_i\quad\Longrightarrow\quad A_v = +g_m\left(r_d\parallel R_L\right)\;}$$
> See `_verification-log.md`.

**(ii) Input resistance** ·L4 p14–p15 — ignoring the current through $R_S$, the input current *is*
the drain current, $i_d = g_m V_i$:

[eq: ri-common-gate]

$$\boxed{\;r_i = \frac{V_i}{i_d} = \frac{V_i}{g_m V_i} = \frac{1}{g_m}\;}$$

and for the circuit as a whole

$$r'_i = r_i\parallel R_S = \frac{1}{g_m}\parallel R_S$$

$r_d$ and $R_L$ also enter $r'_i$, but negligibly. ·L4 p15

**(iii) Output resistance** ·L4 p15

$$r'_o = r_d\parallel R_L$$

**Input capacitance** ·L4 p15 — only $C_{gs}$ matters here, so the common-gate stage has a **low
input capacitance** compared with the common-source stage, whose input capacitance is magnified by
the Miller effect. The footnote makes the reason explicit: **the Miller effect only arises where the
output is in antiphase with the input**, as in a CS amplifier. ·L4 p15

> [added] **The three configurations at a glance.**
>
> | | Common source | Common drain | Common gate |
> |---|---|---|---|
> | input at | gate | gate | source |
> | output from | drain | source | drain |
> | $A_v$ | $-g_m(r_d\parallel R_L)$, large | $\cong 1$ | $+g_m(r_d\parallel R_L)$, large |
> | phase | inverted | in phase | in phase |
> | $r_{in}$ | very high ($\cong R_G$) | very high ($R_1\parallel R_2$) | **low** ($1/g_m$) |
> | $r_{out}$ | $r_d\parallel R_L$ | low ($\cong 1/g_m \parallel R_L$) | $r_d\parallel R_L$ |
> | Miller effect | yes | no | no |
>
> All six rows are stated or derived on ·L4 p12–p15; the table only gathers them.

---

## 4.13 Advantages and disadvantages of FETs ·L4 p15

FETs combine advantages of both BJTs and vacuum tubes. ·L4 p15

**Advantages** — 1. high input impedance · 2. small size · 3. ruggedness · 4. long life ·
5. high frequency response · 6. low noise · 7. **negative temperature coefficient**, hence better
thermal stability · 8. high power gain · 9. high immunity to radiation · 10. **no offset voltage**
when used as a switch or chopper · 11. square-law characteristics.

**Disadvantages** — 1. small gain-bandwidth product · 2. greater susceptibility to damage in
handling.


---

## 4.14 Tutorial Problems No. 63.1 ·L4 p15

The chapter prints seven problems with **answers only**. Each is transcribed below as `[exercise]`,
with a full worked solution supplied in the `[added]` block that follows it. Every answer has been
recomputed independently.

[exercise 1 ·L4 p15] For a particular N-channel JFET, $V_{GS(off)} = -4\ \mathrm{V}$. What would be
the value of $I_D$ when $V_{GS} = -6\ \mathrm{V}$? **[zero]**

> **[added] Solution.** $V_{GS} = -6\ \mathrm{V}$ is **more negative than** the cut-off voltage
> $-4\ \mathrm{V}$, so the depletion regions have already closed the channel.
> $$\boxed{\;I_D = 0\;}$$
> Shockley's equation is **not** valid past cut-off: substituting blindly gives
> $I_{DSS}(1-1.5)^2 = 0.25\,I_{DSS}$, which is wrong. The equation only applies for
> $V_{GS(off)} \le V_{GS} \le 0$. Printed answer confirmed ✓.

[exercise 2 ·L4 p15] For the N-channel JFET of Fig. 63.21, $V_P = 8\ \mathrm{V}$ and
$I_{DSS} = 12\ \mathrm{mA}$. What is (i) the $V_{DS}$ at which pinch-off begins and (ii) the value of
$I_D$ when $V_{DS}$ is above pinch-off but below breakdown? **[3 V ; 12 mA]**

[fig ·L4 p15] **Fig. 63.21** — an N-channel JFET with the drain taken up and across to a drain
resistor $R_L$ returning to a $12\ \mathrm{V}$ battery, the source to ground, and the gate wired to a
$5\ \mathrm{V}$ battery whose other terminal is grounded, so that $V_{GS} = -5\ \mathrm{V}$.

> **[added] Solution.**
> **(i)** Using the chapter's own general relation (§4.6), $V_P = V_{DS(P)} - V_{GS}$:
> $$V_{DS(P)} = V_P + V_{GS} = 8 + (-5) = 3\ \mathrm{V}$$
> $$\boxed{\;V_{DS(P)} = 3\ \mathrm{V}\;}$$
> Printed answer confirmed ✓.
> **(ii)** Above pinch-off the current saturates at the value Shockley's equation gives for that
> $V_{GS}$, using $V_{GS(off)} = -8\ \mathrm{V}$ (§4.4):
> $$I_D = I_{DSS}\left(1-\frac{V_{GS}}{V_{GS(off)}}\right)^2
> = 12\left(1 - \frac{-5}{-8}\right)^2 = 12\left(\tfrac38\right)^2 = 12\times\frac{9}{64}$$
> $$\boxed{\;I_D = 1.69\ \mathrm{mA}\;}$$

> ⚠ VERIFY **V4.12** ·L4 p15 — the printed answer to part (ii) is **12 mA**, i.e. $I_{DSS}$. That is
> the saturated current for $V_{GS} = 0$ only. The same problem's part (i) can only give 3 V if
> $V_{GS} = -5\ \mathrm{V}$, and with $V_{GS} = -5\ \mathrm{V}$ Shockley's equation gives
> $$\boxed{\;I_D = 12\left(1-\tfrac58\right)^2 = 1.69\ \mathrm{mA}\;}$$
> The two printed answers are mutually inconsistent: 3 V requires a bias of $-5\ \mathrm{V}$, 12 mA
> requires a bias of 0 V. See `_verification-log.md`.

[exercise 3 ·L4 p15] The data sheet of a JFET indicates $I_{DSS} = 15\ \mathrm{mA}$ and
$V_{GS(off)} = -5\ \mathrm{V}$. Calculate $I_D$ when $V_{GS}$ is (i) 0, (ii) $-1\ \mathrm{V}$ and
(iii) $-4\ \mathrm{V}$. **[(i) 15 mA (ii) 9.6 mA (iii) 0.6 mA]**

> **[added] Solution.** $I_D = 15\left(1 - V_{GS}/(-5)\right)^2$ mA.
> $$\text{(i)}\quad I_D = 15(1-0)^2 = 15\ \mathrm{mA} = I_{DSS}$$
> $$\text{(ii)}\quad I_D = 15\left(1-\tfrac15\right)^2 = 15\times0.64 = 9.6\ \mathrm{mA}$$
> $$\text{(iii)}\quad I_D = 15\left(1-\tfrac45\right)^2 = 15\times0.04 = 0.6\ \mathrm{mA}$$
> All three printed answers confirmed ✓. Notice the square law at work: 80 % of the way to cut-off,
> only 4 % of the current is left.

[exercise 4 ·L4 p15] The data sheet of a JFET gives $I_{DSS} = 20\ \mathrm{mA}$,
$V_{GS(off)} = -8\ \mathrm{V}$ and $g_{mo} = 4000\ \mathrm{\mu S}$. Calculate $I_D$ and $g_m$ for
$V_{GS} = -4\ \mathrm{V}$. **[5 mA ; 2000 µS]**

> **[added] Solution.**
> $$I_D = 20\left(1-\frac{-4}{-8}\right)^2 = 20\times(0.5)^2 = 5\ \mathrm{mA}$$
> $$g_m = g_{mo}\left(1-\frac{V_{GS}}{V_{GS(off)}}\right) = 4000\times0.5 = 2000\ \mathrm{\mu S}$$
> Both printed answers confirmed ✓. Consistency check:
> $g_{mo} = 2I_{DSS}/\lvert V_{GS(off)}\rvert = 2\times20/8 = 5000\ \mathrm{\mu S}$,
> not the 4000 µS quoted — the data sheet value is a measured
> one and need not match the ideal square-law figure exactly, and the question intends the quoted
> 4000 µS to be used.

[exercise 5 ·L4 p15] For a JFET, $I_{DSS} = 5\ \mathrm{mA}$ and $g_{mo} = 4000\ \mathrm{\mu S}$.
Calculate (i) $V_{GS(off)}$ and (ii) $g_m$ at mid-point bias.
**[(i) −5 V (ii) 3000 µS]**

> **[added] Solution.**
> **(i)** Invert the definition of $g_{mo}$:
> $$g_{mo} = \frac{2I_{DSS}}{|V_{GS(off)}|}\quad\Longrightarrow\quad
> |V_{GS(off)}| = \frac{2I_{DSS}}{g_{mo}} = \frac{2\times5\times10^{-3}}{4\times10^{-3}} = 2.5\ \mathrm{V}$$
> $$\boxed{\;V_{GS(off)} = -2.5\ \mathrm{V}\;}$$
> **(ii)** At mid-point bias $V_{GS} = V_{GS(off)}/4$, so
> $$g_m = g_{mo}\left(1-\tfrac14\right) = 0.75\times4000 = 3000\ \mathrm{\mu S}$$
> confirming the printed answer to (ii) ✓ — and note this part is independent of $V_{GS(off)}$.

> ⚠ VERIFY **V4.13** ·L4 p15 — the printed answer to part (i) is **−5 V**. From the data given
> ($I_{DSS} = 5\ \mathrm{mA}$, $g_{mo} = 4000\ \mathrm{\mu S}$) the chapter's own relation
> $g_{mo} = -2I_{DSS}/V_P$ (·L4 p8) gives
> $$\boxed{\;V_{GS(off)} = -\frac{2\times 5\ \mathrm{mA}}{4000\ \mathrm{\mu S}} = -2.5\ \mathrm{V}\;}$$
> The printed −5 V would require $I_{DSS} = 10\ \mathrm{mA}$. Cross-check with tutorial problem 6,
> which uses the same relation correctly: $2\times8.4/3 = 5600\ \mathrm{\mu S}$ ✓.
> See `_verification-log.md`.

[exercise 6 ·L4 p15] At a certain point on the transfer characteristic of an N-channel JFET the
following values are read: $I_{DSS} = 8.4\ \mathrm{mA}$, $V_{GS} = -0.5\ \mathrm{V}$ and
$V_P = -3.0\ \mathrm{V}$. Calculate (i) $g_{mo}$ and (ii) $g_m$ at that point.
**[(i) 5600 µS (ii) 4670 µS]**

> **[added] Solution.**
> $$g_{mo} = -\frac{2I_{DSS}}{V_P} = \frac{-2\times8.4\ \mathrm{mA}}{-3.0\ \mathrm{V}}
> = 5.6\ \mathrm{mA/V} = 5600\ \mathrm{\mu S}$$
> $$g_m = g_{mo}\left(1-\frac{V_{GS}}{V_P}\right) = 5600\left(1-\frac{-0.5}{-3.0}\right)
> = 5600\times0.8333 = 4667\ \mathrm{\mu S}$$
> Both printed answers confirmed ✓ (4670 µS to three figures).

[exercise 7 ·L4 p15] For the JFET circuit of Fig. 63.22, $I_{DSS} = 9\ \mathrm{mA}$ and
$V_P = -3\ \mathrm{V}$. Find the value of $R_L$ that sets $V_{DS}$ to $7\ \mathrm{V}$.
*(Hint: $V_{GS} = -2\ \mathrm{V}$ as $I_G = 0$.)* **[5 K]**

[fig ·L4 p15] **Fig. 63.22** — a CS stage with a **fixed negative gate supply**: $12\ \mathrm{V}$
rail, $R_L$ in the drain, output $V_o$ through $C_2$, input $V_i$ through $C_1$ to the gate,
$R_G = 1\ \mathrm{M\Omega}$ from the gate down to a $-2\ \mathrm{V}$ supply, and the source taken
directly to ground.

> **[added] Solution.** No gate current flows in $R_G$, so it drops nothing and the gate sits at the
> supply value: $V_{GS} = -2\ \mathrm{V}$ (this is the hint). The source is grounded, so
> $V_{DS} = V_D$.
> $$I_D = I_{DSS}\left(1-\frac{V_{GS}}{V_P}\right)^2 = 9\left(1-\frac{-2}{-3}\right)^2
> = 9\times\left(\tfrac13\right)^2 = 1\ \mathrm{mA}$$
> $$V_{DS} = V_{DD} - I_D R_L \quad\Longrightarrow\quad
> R_L = \frac{V_{DD}-V_{DS}}{I_D} = \frac{12-7}{1\ \mathrm{mA}}$$
> $$\boxed{\;R_L = 5\ \mathrm{k\Omega}\;}$$
> Printed answer confirmed ✓.

> ⚠ VERIFY **C4.11** ·L4 p15 — problems 4 and 5 both spell the device **"JEET"** for JFET, and
> problem 5 prints "$I_{DSS}$ 5 mA" with the equals sign missing. Scan/typesetting noise; no physics
> is affected. See `_verification-log.md`.

---

## 4.15 MOSFET or IGFET — the family ·L4 p16

[def] A **MOSFET** (metal-oxide-semiconductor FET), also called an **IGFET** (insulated-gate FET),
has its gate **insulated from the channel** by an ultra-thin film of silicon dioxide. Two kinds:
·L4 p16

**(i) Depletion-enhancement MOSFET (DE MOSFET)** — operates in **both** modes by changing the
polarity of $V_{GS}$. A channel exists in the structure as built, so $I_D$ flows even at
$V_{GS} = 0$. Negative $V_{GS}$ depletes it, positive $V_{GS}$ enhances it. Hence
**normally-ON MOSFET**.

**(ii) Enhancement-only MOSFET (E-only MOSFET)** — **no channel exists structurally** between drain
and source. It does not conduct at $V_{GS}=0$ and works with **large positive** gate voltages only.
Hence **normally-OFF MOSFET**.

[table] The two, side by side ·L4 p16

| | DE MOSFET | E-only MOSFET |
|---|---|---|
| channel as built | present | absent |
| $I_D$ at $V_{GS}=0$ | flows, $= I_{DSS}$ | zero |
| operating polarity of $V_{GS}$ (N-channel) | either sign | positive only, above $V_{GS(th)}$ |
| modes | depletion **and** enhancement | enhancement only |
| nickname | normally-ON | normally-OFF |
| cut-off / turn-on parameter | $V_{GS(off)}$ | $V_{GS(th)}$ |

In a DE MOSFET, $I_D$ falls as $V_{GS}$ is made more negative and ceases at $V_{GS} = V_{GS(off)}$;
in an E-only MOSFET, $I_D$ flows only once $V_{GS}$ exceeds $V_{GS(th)}$. ·L4 p16

---

## 4.16 DE MOSFET — construction and working ·L4 p16–p17

### Symbols added here

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{GS(th)}$ | threshold gate-source voltage of an E-only MOSFET | V | 2–5 V |
| $I_{D(ON)}$ | drain current quoted on a data sheet at a stated $V_{GS}$ | A (mA) | 3–5 mA |
| $K$ | constant of the E-MOSFET square law | A·V⁻² (usually mA/V²) | 0.1–0.3 mA/V² |
| SS | substrate terminal (the fourth lead) | — | — |

### Construction ·L4 p16–p17

Like a JFET it has source, gate and drain, but its **gate is insulated** from the conducting channel
by an ultra-thin metal-oxide film, usually $\mathrm{SiO_2}$ — hence the alternative name IGFET.
·L4 p16–p17

Because the gate is insulated, **voltages of either polarity may be applied to it**: there is no
junction to forward-bias. The gate, the $\mathrm{SiO_2}$ layer and the channel together form a
**parallel-plate capacitor**. ·L4 p17

Unlike a JFET, a DE MOSFET has **only one** P-region (or N-region), called the **substrate**, which
is normally shorted to the source internally. ·L4 p17

[fig ·L4 p16] **Fig. 63.23 — DE MOSFET construction and symbols, N-channel left, P-channel right.**
The N-channel drawing is an upright rectangle: an N region at the top with the **Drain** lead, an N
region at the bottom with the **Source** lead, the bulk of the block marked **P** and arrowed
"P-Substrate" with its own lead taken out to the right, and down the **left-hand face** a narrow
strip arrowed "Conducting N-Channel". Between that channel and the gate lead on the left is a thin
dark bar arrowed **$\mathrm{SiO_2}$**. The P-channel version has every type letter interchanged and
is arrowed "Conducting P-Channel" and "N-Substrate". Below each is the schematic symbol: drain at the
top, source at the bottom joined by a **solid** vertical channel line, the gate drawn as a separate
plate to the left (no contact — it is insulated), and the substrate arrow pointing **in** for the
N-channel device and **out** for the P-channel device.

> ⚠ VERIFY **C4.12** ·L4 p16 — in Fig. 63.23 the **substrate** lead is labelled **S** and the
> **source** lead immediately below it is labelled **s** / "Source" — the same letter for two
> different terminals in one drawing. ·L4 p17–p18 calls the substrate terminal **SS**, which is the
> label to use. See `_nomenclature.md`.

### (i) Depletion mode, N-channel ·L4 p17

At $V_{GS}=0$ electrons flow freely from source to drain through the channel that already exists.
Making the gate **negative** repels electrons from the channel — it **depletes** the channel of
electrons by inducing positive charge in it. The more negative the gate, the fewer electrons remain
and the lower the conductivity. Enough negative gate voltage — $V_{GS(off)}$ — **cuts the channel
off** altogether. In this mode a DE MOSFET behaves like a JFET. ·L4 p17

### (ii) Enhancement mode, N-channel ·L4 p17

Drain current flows even at zero gate bias. Applying a **positive** gate voltage makes the input gate
capacitor **create free electrons in the channel** by capacitor action; these add to the electrons
already there, so conductivity **increases** and $I_D$ rises with $V_{GS}$. ·L4 p17

[fig ·L4 p17] **Fig. 63.24 — the two modes, with the gate capacitor enlarged.** Each half shows the
same cross-section as Fig. 63.23 (N at drain and source ends, P substrate, gate plate on the left,
substrate lead marked SS) wired into a circuit: $R_L$ from drain to $V_{DD}$, $V_{DS}$ marked across
drain-source, the gate fed from $V_{GG}$ through $R_G$ with $V_{GS}$ marked, and the drain current
arrowed at the top. In (*a*) the gate supply is connected **negative to the gate** (depletion mode);
in (*b*) **positive to the gate** (enhancement mode). Beneath each is an enlarged view of the gate
capacitor drawn as three columns of charge: in (*a*) the metal gate carries **−**, the
$\mathrm{SiO_2}$ block shows **+** on its gate-side face and **−** on its channel-side face, and the
channel carries **+**; in (*b*) every sign is reversed, so the channel carries the induced **−**
(free electrons) that enhance conduction.

> ⚠ VERIFY **C4.14** ·L4 p17 — the drain current in Fig. 63.24 (*b*) is labelled **$I_B$**, whereas
> panel (*a*) labels the same current $I_D$. There is no base terminal in a MOSFET; read $I_D$.
> See `_verification-log.md`.

> ⚠ VERIFY **C4.13** ·L4 p17 — two words are corrupted in this paragraph: "the gate, $\mathrm{SiO_2}$
> insulator and channel **from** a parallel-plate capacitor" (should be **form**), and "Normally, it
> is shorted **the source** internally" (should be **shorted to the source**). Scan noise; the
> physics is unaffected. See `_verification-log.md`.

**Input resistance.** Because the gate current is negligible in **both** modes, a MOSFET's input
resistance is enormous — $10^{10}$ to $10^{14}\ \Omega$. The residual input current is the **leakage
current of a capacitor**, whereas a JFET's is the leakage current of a **reverse-biased P-N
junction**. ·L4 p17

---

## 4.17 Schematic symbols for a DE MOSFET ·L4 p18

The gate is drawn as a **metal plate** standing off the channel line (it touches nothing — it is
insulated). The **arrow is on the substrate** and points **towards the N-channel**. ·L4 p18

[fig ·L4 p18] **Fig. 63.25 — three symbols.**
(*a*) **Four-terminal N-channel DE MOSFET**: D at the top, S at the bottom, gate plate to the left,
and the substrate lead **SS brought out separately** to the right — used when the substrate is taken
to an external load.
(*b*) **Three-terminal N-channel DE MOSFET**: the same symbol with the substrate arrow tied
internally to the source, drain marked $+V_{DD}$.
(*c*) **P-channel DE MOSFET**: same again with the substrate arrow pointing **outward** and the drain
marked $-V_{DD}$.

---

## 4.18 Static characteristics of a DE MOSFET ·L4 p18–p19

[fig ·L4 p18] **Fig. 63.26 — drain and transfer characteristics of a common-source N-channel DE
MOSFET.**
(*a*) **Drain characteristics**: $I_D$ vertical, $V_{DS}$ horizontal; a family of curves each rising
from the origin, kneeing over and running flat, labelled from the top downwards
$V_{GS} = +2\ \mathrm{V}$, $+1\ \mathrm{V}$, $0\ \mathrm{V}$, $-1\ \mathrm{V}$, $-2\ \mathrm{V}$, with
the bottom curve marked $V_{GS(off)}$ lying along the axis. A double-headed arrow at the right marks
the curves above $V_{GS}=0$ as **Enhancement Mode** and those below it as **Depletion Mode**.
(*b*) **Transfer characteristic**: $I_D$ vertical with the axis drawn through $V_{GS}=0$, the
horizontal $V_{GS}$ axis ticked $-4, -3, -2, -1, 0, 1, 2, 3, 4\ \mathrm{V}$ with $-V_{GS}$ to the
left and $+V_{GS}$ to the right. The curve is a rising parabola crossing the vertical axis at the
level marked $I_{DSS}$, labelled **Depletion Mode** to the left of the axis and **Enhancement Mode**
to the right.

**The one structural difference from a JFET's transfer characteristic:** it does not stop at
$V_{GS}=0$. It continues into positive $V_{GS}$, where $I_D$ exceeds $I_{DSS}$. ·L4 p18

- **enhancement mode** when the gate is **positive** with respect to the source;
- **depletion mode** when the gate is **negative**; $I_D$ falls to zero at $V_{GS} = V_{GS(off)}$.

·L4 p18

---

### [ex] Example 63.9 ·L4 p18–p19

> For the N-channel **zero-biased** DE MOSFET circuit of Fig. 63.27, calculate $V_{DS}$ if
> $I_{DSS} = 10\ \mathrm{mA}$ and $V_{GS(off)} = -6\ \mathrm{V}$.
> *(Electronics-I, Bangalore Univ. 1992)*

[fig ·L4 p18] **Fig. 63.27** — $18\ \mathrm{V}$ rail, $R_L = 800\ \Omega$ from the rail to the drain,
the DE MOSFET below it with its gate returned to ground through a $10\ \mathrm{M\Omega}$ resistor and
its source taken straight to ground. Zero bias: $V_{GS} = 0$.

$$I_D = I_{DSS} = 10\ \mathrm{mA}$$

$$V_{DS} = V_{DD} - I_{DSS}R_L = 18 - 10\times10^{-3}\times800 = 10\ \mathrm{V}$$

*[added] Verified: $10\ \mathrm{mA}\times800\ \Omega = 8\ \mathrm{V}$, so
$V_{DS} = 18-8 = 10\ \mathrm{V}$ ✓. $V_{GS(off)}$ is not needed — it is there to confirm the device is
a depletion type, for which zero bias is a legitimate operating point. **This is the reason zero-bias
circuits exist only for DE MOSFETs:** a JFET would need $V_{GS} < 0$ and an E-MOSFET would be off.*


---

## 4.19 Enhancement-only N-channel MOSFET (NMOS) ·L4 p19–p20

Widely used in **digital circuitry**. ·L4 p19

**Construction.** The **P-type substrate extends all the way to the metal-oxide layer**: structurally
**there is no channel** between source and drain. ·L4 p19

[fig ·L4 p19] **Fig. 63.28 — NMOS construction.** An upright rectangle: an N region at the top with
the **Drain** lead, an N region at the bottom with the **Source** lead (marked S), and between them
the **P Substrate** filling the whole width right up to the left-hand face. Against that face is a
thin light bar (the $\mathrm{SiO_2}$ film) with the **Gate** lead on its left. Nothing joins the two
N regions — that gap is the point of the figure.

**Why it cannot take a negative gate voltage** ·L4 p19 — a negative gate would induce **positive**
charge in the space between drain and source, which blocks the passage of electrons. It therefore
operates with **positive gate voltage only**.

**How conduction starts** ·L4 p19 — a sufficiently large positive gate voltage produces a **thin
layer of free electrons** hugging the metal-oxide film and stretching all the way from source to
drain. That thin layer of P-substrate which has been turned into an electron path behaves like N-type
material and is called the **N-type inversion layer** or **virtual N-channel**.

[def] $V_{GS(th)}$ — the **threshold voltage**: the minimum gate-source voltage that produces the
inversion layer and hence any drain current. ·L4 p19

- $V_{GS} < V_{GS(th)}$: $I_D = 0$
- $V_{GS} > V_{GS(th)}$: current flows, and deepens with $V_{GS}$

[eq: emosfet-k] **The E-MOSFET square law** ·L4 p19

$$\boxed{\;I_D = K\left(V_{GS} - V_{GS(th)}\right)^{2}\;}$$

- $K$ — a constant for the particular MOSFET, A·V⁻² (usually quoted in mA/V²)

$K$ is found from the data sheet by taking the quoted $I_{D(ON)}$ at its stated $V_{GS}$ and
substituting: ·L4 p19

$$\boxed{\;K = \frac{I_{D(ON)}}{\left(V_{GS} - V_{GS(th)}\right)^{2}}\;}$$

> ⚠ VERIFY **C4.15** ·L4 p19 — the equation is printed inline with its exponent stranded outside the
> bracket: "$I_D = \mathrm{K}(V_{GS} - V_{GS(th)})2$". The squared form above is what is meant, as
> ·L4 p20's differentiation and Examples 63.10–63.13 all confirm. See `_verification-log.md`.

[fig ·L4 p19] **Fig. 63.29 — biasing polarities.** (*a*) N-channel: the cross-section of Fig. 63.28
with $V_{GG}$ connected **positive to the gate** (the gate capacitor's charge columns drawn beside
it, $+$ on the metal plate and $-$ induced in the substrate face), $R_L$ from drain to $+V_{DD}$,
$V_{DS}$ marked, $I_D$ arrowed at the top. (*b*) P-channel: identical with every polarity and type
letter reversed.

### Transfer and drain characteristics ·L4 p20

[fig ·L4 p20] **Fig. 63.30 — three panels.**
(*a*) the **schematic symbol** of an E-only N-channel MOSFET: drain at the top, source at the bottom,
gate plate to the left, substrate arrow pointing **in** (towards N material), and — the identifying
feature — the **vertical channel line drawn broken into three segments**, a reminder that the device
is **normally OFF**.
(*b*) **drain characteristics**: $I_D$ against $V_{DS}$, three curves labelled $V_{GS} = +5$, $+10$,
$+15\ \mathrm{V}$ (higher $V_{GS}$, higher curve), each rising then flattening; spans marked
**Ohmic Region** and **Saturation Region** across the top; the horizontal axis itself is labelled
$V_{GS(th)}$ — at and below threshold there is no curve at all, only the axis.
(*c*) **transfer characteristic**: $I_D$ against $V_{GS}$, flat along the axis from the origin out to
$V_{GS(th)}$, then curving steeply upward — the parabola of the K equation, offset to start at
threshold.

**A P-channel E-only MOSFET (PMOS)** is built like an NMOS with all P and N regions interchanged, and
operates with **negative** gate voltage only. ·L4 p20

[eq: emosfet-gm] Differentiating the K equation with respect to $V_{GS}$: ·L4 p20

$$\boxed{\;g_m = \frac{dI_D}{dV_{GS}} = 2K\left(V_{GS} - V_{GS(th)}\right)\;}$$

**An E-MOSFET has no $I_{DSS}$ parameter**, unlike the JFET and the DE MOSFET — at $V_{GS}=0$ it
passes nothing. ·L4 p20

> ⚠ VERIFY **C4.16** ·L4 p20 — "A P-channel E-only MOSFET (PMOS) is constructed like **NOMS**" —
> transposed letters for NMOS. See `_verification-log.md`.

---

## 4.20 Biasing an E-only MOSFET ·L4 p20–p21

The whole job is to make the gate **more positive than the source by more than $V_{GS(th)}$**.
·L4 p20

[fig ·L4 p20] **Fig. 63.31 — two bias methods.**
(*a*) **Drain-feedback bias**: $R_G$ is connected from the **drain** back to the **gate**. Since no
gate current flows, $R_G$ drops no voltage and therefore $V_{GS} = V_{DS}$ — marked on the figure.
$R_L$ runs from $+V_{DD}$ to the drain; the source is grounded.
(*b*) **Voltage-divider bias**: $R_1$ from $+V_{DD}$ to the gate node and $R_2$ from that node to
ground, with $V_2$ marked across $R_2$; $R_L$ in the drain; source grounded.

[eq] For the voltage-divider circuit of Fig. 63.31 (*b*): ·L4 p20

$$\boxed{\;V_{GS} = V_2 = V_{DD}\frac{R_2}{R_1+R_2}\;}$$

$$\boxed{\;V_{DS} = V_{DD} - I_D R_L,\qquad I_D = K\left(V_{GS}-V_{GS(th)}\right)^{2}\;}$$

> [added] Note the difference from JFET voltage-divider bias (§4.9): here there is **no source
> resistor**, so $V_{GS}$ **is** the divider voltage, not the divider voltage minus $I_D R_S$. An
> E-MOSFET needs a **positive** $V_{GS}$, so a source resistor would fight the bias rather than
> create it.

---

### [ex] Example 63.10 ·L4 p20–p21

> The data sheet of the E-MOSFET of Fig. 63.32 gives $I_{D(ON)} = 4\ \mathrm{mA}$ at
> $V_{GS} = 10\ \mathrm{V}$ and $V_{GS(th)} = 5\ \mathrm{V}$. Calculate $V_{GS}$ and $V_{DS}$.
> *(Applied Electronics, Punjab Univ. 1991)*

[fig ·L4 p20] **Fig. 63.32** — voltage-divider bias: $25\ \mathrm{V}$ rail; $R_1 = 6\ \mathrm{k\Omega}$
from rail to the gate node and $R_2 = 9\ \mathrm{k\Omega}$ from that node to ground;
$R_L = 1\ \mathrm{k\Omega}$ in the drain; source grounded; $V_{DS}$ marked as a vertical arrow from
drain to ground.

$$V_{GS} = V_2 = 25\times\frac{9}{15} = 15\ \mathrm{V}$$

$$K = \frac{I_{D(ON)}}{\left(V_{GS}-V_{GS(th)}\right)^2} = \frac{4}{\left(10-5\right)^2}
= 0.16\ \mathrm{mA/V^2}$$

$$I_D = K\left(V_{GS}-V_{GS(th)}\right)^2 = 0.16\left(15-5\right)^2 = 16\ \mathrm{mA}$$

$$V_{DS} = V_{DD}-I_D R_L = 25 - 16\times1 = 9\ \mathrm{V}$$

*[added] Verified: divider $9/(6+9) = 0.6$, $\times 25 = 15\ \mathrm{V}$ ✓; $4/25 = 0.16$ ✓;
$0.16\times100 = 16\ \mathrm{mA}$ ✓; $25-16 = 9\ \mathrm{V}$ ✓. Note the two different $V_{GS}$
values in play: $10\ \mathrm{V}$ is the data-sheet test condition used to extract $K$;
$15\ \mathrm{V}$ is the actual operating bias.*

---

### [ex] Example 63.11 ·L4 p21

> An N-channel E-MOSFET has $I_{D(ON)} = 4\ \mathrm{mA}$ at $V_{GS} = 10\ \mathrm{V}$ and
> $V_{GS(th)} = 5\ \mathrm{V}$. Calculate its drain current for $V_{GS} = 8\ \mathrm{V}$.

$$K = \frac{4\ \mathrm{mA}}{\left(10\ \mathrm{V}-5\ \mathrm{V}\right)^2} = 0.16\ \mathrm{mA/V^2}$$

$$I_D = K\left(V_{GS}-V_{GS(th)}\right)^2 = 0.16\left(8-5\right)^2 = 1.44\ \mathrm{mA}$$

*[added] Verified: $0.16\times9 = 1.44\ \mathrm{mA}$ ✓.*

---

## 4.21 FET amplifiers ·L4 p21–p22

### (i) DE MOSFET amplifier ·L4 p21–p22

[fig ·L4 p21] **Fig. 63.33.** (*a*) a **zero-biased** N-channel DE MOSFET with an a.c. source
capacitively coupled to the gate: $+V_{DD}$ at the top, $R_L$ to the drain, output $v_o$ through
$C_2$, the signal generator $v_i$ through $C_1$ to the gate, $R_G$ from gate to ground, source
grounded. (*b*) its transfer characteristic with the signal drawn on it: $I_D$ vertical,
$V_{GS}$ horizontal with negative to the left; the parabola passes through the operating point **Q**
on the $I_D$ axis (because $V_{GS}=0$); a sine wave labelled **Input Signal** is drawn along the
$V_{GS}$ axis below, and the resulting sine labelled **Output Signal** is projected horizontally from
Q, larger on the positive half.

Since the gate is at 0 V d.c. and the source is grounded, $V_{GS} = 0$ and the Q-point sits at
$I_{DSS}$. The input swings $V_{GS}$ **above and below zero**: ·L4 p21–p22

- the **negative** half-cycle drives the device into **depletion mode** and $I_D$ falls;
- the **positive** half-cycle drives it into **enhancement mode** and $I_D$ rises;
- the resulting swing in the drop across $R_L$ is the output, taken through $C_2$.

**This is what a DE MOSFET buys:** an amplifier that needs no bias network at all — the only device
of the three for which zero bias is a valid class-A operating point. ·L4 p21

### (ii) E-MOSFET amplifier ·L4 p22

[fig ·L4 p21] **Fig. 63.34.** (*a*) a voltage-divider-biased N-channel E-MOSFET: $V_{DD}$ at the top;
$R_1$ and $R_2$ forming the gate divider; $R_L$ in the drain; output through $C_2$; input $v_i$
through $C_1$; $R_S$ in the source bypassed by $C_3$. (*b*) transfer characteristic: the curve leaves
the axis at $V_{GS(th)}$ and rises; the Q-point sits well up the curve at $(V_{GSQ}, I_{DQ})$, both
marked by dashed lines; the input sine is drawn along the $V_{GS}$ axis about $V_{GSQ}$ and the
output sine is projected out to the left about $I_{DQ}$.

The gate must be biased **positive enough that $V_{GS}$ exceeds $V_{GS(th)}$**; the signal then
swings $V_{GS}$ above and below that Q-point value, swinging $I_D$ and hence $I_D R_L$. ·L4 p22

---

### [ex] Example 63.12 ·L4 p22

> The N-channel E-MOSFET used in the common-source amplifier of Fig. 63.35 has
> $I_{D(ON)} = 4\ \mathrm{mA}$ at $V_{DS} = 10\ \mathrm{V}$, $V_{GS(th)} = 4\ \mathrm{V}$ and
> $g_m = 5000\ \mathrm{\mu S}$. Calculate $V_{GS}$, $I_D$, $V_{DS}$ and $v_o$.
> *(Elect. and Electronic Engg., Annamalai Univ. 1992)*

[fig ·L4 p22] **Fig. 63.35** — $16\ \mathrm{V}$ rail; gate divider $R_1 = 50\ \mathrm{k\Omega}$ (to
the rail) and $R_2 = 30\ \mathrm{k\Omega}$ (to ground); drain resistor $5\ \mathrm{k\Omega}$; output
$V_o$ through $C_2$; a $100\ \mathrm{mV}$ generator through $C_1$ into the gate; source grounded.

**The chapter's working** ·L4 p22

$$V_{GS} = V_{DD}\frac{R_2}{R_1+R_2} = 16\times\frac{30}{80} = 6\ \mathrm{V}$$

$$K = \frac{I_{D(ON)}}{\left(V_{GS}-V_{GS(th)}\right)^2} = \frac{4}{\left(10-5\right)^2}
= 0.16\ \mathrm{mA/V^2}$$

$$I_D = K\left(V_{GS}-V_{GS(th)}\right)^2 = 0.16\left(6-4\right)^2 = 0.64\ \mathrm{mA}$$

$$V_{DS} = V_{DD}-I_D R_L = 16 - 0.64\times5 = 12.8\ \mathrm{V}$$

$$A_v = g_m\left(r_d\parallel R_L\right)\cong g_m R_L = 5000\times10^{-6}\times5\times10^{3} = 25$$

$$V_o = A_v v_i = 25\times100\ \mathrm{mV} = 2500\ \mathrm{mV} = 2.5\ \mathrm{V}$$

> ⚠ VERIFY **V4.14** ·L4 p22 — **the $K$ line does not match this example's own data.** The question
> gives $V_{GS(th)} = 4\ \mathrm{V}$, but $K$ is evaluated as $4/(10-5)^2$, i.e. with
> $V_{GS(th)} = 5\ \mathrm{V}$ — the value belonging to Example 63.11 on the previous page. The
> question also quotes $I_{D(ON)}$ "at $V_{DS} = 10\ \mathrm{V}$", where $K$ requires the $V_{GS}$ at
> which $I_{D(ON)}$ was measured. Reading the data as $I_{D(ON)} = 4\ \mathrm{mA}$ at
> $V_{GS} = 10\ \mathrm{V}$ with $V_{GS(th)} = 4\ \mathrm{V}$:
> $$\boxed{\;K = \frac{4}{\left(10-4\right)^2} = 0.111\ \mathrm{mA/V^2},\quad
> I_D = 0.111\left(6-4\right)^2 = 0.444\ \mathrm{mA},\quad V_{DS} = 16-2.22 = 13.8\ \mathrm{V}\;}$$
> $A_v = 25$ and $v_o = 2.5\ \mathrm{V}$ are unaffected, since they depend only on $g_m$ and $R_L$.
> See `_verification-log.md`.

> ⚠ VERIFY **C4.17** ·L4 p22 — the numerator of the $K$ expression is printed **$I_{D(NO)}$** for
> $I_{D(ON)}$, and in Example 63.13 below the quadratic's denominator prints as **".2"** for 2.
> Scan noise. See `_verification-log.md`.

*[added] Arithmetic as printed is self-consistent apart from the $K$ defect:
$16\times30/80 = 6\ \mathrm{V}$ ✓; $0.16\times4 = 0.64\ \mathrm{mA}$ ✓;
$16 - 3.2 = 12.8\ \mathrm{V}$ ✓; $5\times10^{-3}\times5\times10^{3} = 25$ ✓;
$25\times100\ \mathrm{mV} = 2.5\ \mathrm{V}$ ✓.*

---

### [ex] Example 63.13 ·L4 p22

> The parameters of the enhancement-only NMOS shown in Fig. 63.36 are $V_{GS(th)} = 2\ \mathrm{V}$
> and $K = 2\times10^{-4}\ \mathrm{A/V^2}$. Calculate $I_D$ and $V_{DS}$.

[fig ·L4 p22] **Fig. 63.36 — two circuits.** (*a*) $12\ \mathrm{V}$ rail, $R_L = 5\ \mathrm{k\Omega}$
down to the drain, source to ground, $I_D$ arrowed beside the drain lead — and **the gate lead is
drawn going nowhere**: no connection to it appears in the panel (see the flag below). (*b*) the same
circuit with a link taken from the gate out to the left, down and back to the **source/ground** rail,
so that $V_{GS}=0$.

> ⚠ VERIFY **C4.21** ·L4 p22 — panel (*a*) of Fig. 63.36 **does not show the drain-feedback
> connection** that the solution assumes ("Since drain is directly returned to gate,
> $V_{GS} = V_{DS}$"). Panel (*b*) draws its gate link explicitly, and Fig. 63.38 (*a*) on ·L4 p23
> draws the same drain-feedback link properly, so the omission is in this panel alone. Read panel
> (*a*) as
> $$\boxed{\;\text{gate wired directly to the drain, } V_{GS}=V_{DS}\;}$$
> The computed answers are unaffected — the text states the connection. See `_verification-log.md`.

**Circuit (a) — drain-feedback bias.** Since the drain is returned directly to the gate,
$V_{GS} = V_{DS}$.

$$V_{DS} = V_{DD} - I_D R_L = 12 - 5\times10^{3}I_D
\quad\Longrightarrow\quad I_D = \frac{12-V_{DS}}{5\times10^{3}}\ \mathrm{A}$$

$$I_D = K\left(V_{GS}-V_{GS(th)}\right)^2 = K\left(V_{DS}-2\right)^2$$

$$\frac{12-V_{DS}}{5\times10^{3}} = 2\times10^{-4}\left(V_{DS}-2\right)^2$$

$$V_{DS}^{2} - 3V_{DS} - 8 = 0$$

$$V_{DS} = \frac{3\pm\sqrt{9+32}}{2} = \frac{3\pm\sqrt{41}}{2} = 4.7\ \mathrm{V}$$

$$I_D = \frac{12-4.7}{5\times10^{3}} = 1.5\ \mathrm{mA}$$

**Circuit (b) — gate returned to ground.** $V_{GS} = 0$, which is far below $V_{GS(th)}$, so

$$I_D = 0,\qquad V_{DS} = V_{DD} = 12\ \mathrm{V}$$

*[added] Verified: $5\times10^{3}\times2\times10^{-4} = 1$, so
$12-V_{DS} = (V_{DS}-2)^2 = V_{DS}^2-4V_{DS}+4$,
giving $V_{DS}^2-3V_{DS}-8=0$ ✓. Roots $(3\pm6.403)/2 = 4.70$ and $-1.70$;
the negative root is discarded ✓. $7.3/5000 = 1.46\ \mathrm{mA}$ ✓ (quoted 1.5 mA).*

---

### [ex] Example 63.14 ·L4 p22

> A MOSFET has a drain resistance $R_L$ of $44\ \mathrm{k\Omega}$ and operates at
> $20\ \mathrm{kHz}$. Calculate the voltage gain of this device as a single-stage amplifier. The
> MOSFET parameters are $g_m = 1.6\ \mathrm{mA/V}$, $r_d = 100\ \mathrm{k\Omega}$,
> $C_{gs} = 3.0\ \mathrm{pF}$, $C_{ds} = 1.0\ \mathrm{pF}$ and $C_{gd} = 2.8\ \mathrm{pF}$.
> *(U.P.S.C. Engg. Services, 1996)*

$$A_v = g_m\left(r_d\parallel R_L\right)
= 1.6\times10^{-3}\left(100\times10^{3}\parallel 44\times10^{3}\right)$$

$$= 1.6\times10^{-3}\times30.56\times10^{3} = 48.9$$

*[added] Verified: $100\times44/144 = 30.56\ \mathrm{k\Omega}$ ✓;
$1.6\times10^{-3}\times30\,560 = 48.9$ ✓. The three capacitances and the 20 kHz are **not needed** —
at 20 kHz the reactances are megohms and play no part. They are there to see whether the reader
knows that.*

> ⚠ VERIFY **C4.18** ·L4 p22 — the gain is quoted as $+48.9$. This is a **common-source** stage, and
> the chapter's own expression (·L4 p12) is $A_v = -g_m(r_d\parallel R_L)$. Correct:
> $$\boxed{\;A_v = -48.9\;}$$
> i.e. 48.9 with phase inversion. See `_verification-log.md`.

---

## 4.22 FET applications ·L4 p23

FETs can do almost anything a bipolar transistor can. Five uses are **exclusive to them**: ·L4 p23

1. **input amplifiers** in oscilloscopes, electronic voltmeters and other measuring/testing gear,
   because their high $r_{in}$ **reduces the loading effect to a minimum**;
2. **logic circuits** — held OFF at zero input and turned ON with very little input power;
3. **mixers** in FM and TV receivers;
4. **voltage-variable resistors (VVR)** in operational amplifiers and tone controls;
5. **large-scale integration (LSI)** and computer memories, because of very small size.

---

## 4.23 MOSFET handling ·L4 p23

MOSFETs need careful handling **out of circuit**; in circuit they are as rugged as any comparable
solid-state device. ·L4 p23

**The failure mechanism.** The gate-channel structure is a capacitor of extremely high resistance, so
**only a few electrons are needed to produce a high voltage across it** — and that voltage ruptures
the ultra-thin $\mathrm{SiO_2}$ layer. **Even picking a MOSFET up by its leads can destroy it.**

**The precautions** ·L4 p23

- **Grounding (shorting) rings** short all leads together so no voltage can build up between them.
  They are removed **only after** the device is securely wired into the circuit.
- **Conducting foam** between the leads does the same job.
- Some MOSFETs have **back-to-back Zener diodes formed internally** between gate and source to clamp
  stray voltages.

[fig ·L4 p23] **Fig. 63.37 — a protected MOSFET.** The E-MOSFET symbol (D at top, S at bottom, gate
plate at left, substrate arrow inward) with **two Zener diodes drawn back to back** (cathode to
cathode) inside the device outline, connected from the gate line to the source line.

> ⚠ VERIFY **C4.19** ·L4 p23 — the text says "As shown in **Fig. 13.37**, some MOSFETs have
> back-to-back Zener diodes". The figure meant is **Fig. 63.37**, on the same page. Chapter-number
> typo. See `_verification-log.md`.


---

## 4.24 Tutorial Problems No. 63.2 ·L4 p23–p24

Eight problems, printed with answers only. Transcribed as `[exercise]`, each followed by an
independently worked `[added]` solution.

[fig ·L4 p23] **Fig. 63.38 — the four circuits used by problems 4, 5 and 6.**
(*a*) $15\ \mathrm{V}$ rail, $5\ \mathrm{k\Omega}$ drain resistor, E-MOSFET with source grounded and
the **gate linked back to the drain** (drain-feedback bias).
(*b*) the same, but the gate link goes **down to the source/ground rail** instead.
(*c*) $24\ \mathrm{V}$ rail, $1\ \mathrm{k\Omega}$ drain resistor, gate divider $10\ \mathrm{k\Omega}$
(upper) and $15\ \mathrm{k\Omega}$ (lower), source grounded, $I_D$ arrowed in the drain lead.
(*d*) $15\ \mathrm{V}$ rail, $3\ \mathrm{k\Omega}$ drain resistor, output $v_o$ through $C_2$, gate
divider $30\ \mathrm{k\Omega}$ (upper) and $20\ \mathrm{k\Omega}$ (lower), a $50\ \mathrm{mV}$
generator through $C_1$ into the gate, source grounded (**no source resistor**).

[exercise 1 ·L4 p23] For a certain DE MOSFET, $I_{DSS} = 10\ \mathrm{mA}$ and
$V_{GS(off)} = -8\ \mathrm{V}$. Calculate $I_D$ when $V_{GS}$ is (i) $-4\ \mathrm{V}$ and
(ii) $+4\ \mathrm{V}$. **[(i) 2.5 mA (ii) 22.5 mA]**

> **[added] Solution.** Shockley's equation applies to a DE MOSFET on **both** sides of zero.
> $$\text{(i)}\quad I_D = 10\left(1-\frac{-4}{-8}\right)^2 = 10\left(0.5\right)^2 = 2.5\ \mathrm{mA}
> \quad\text{(depletion mode)}$$
> $$\text{(ii)}\quad I_D = 10\left(1-\frac{+4}{-8}\right)^2 = 10\left(1.5\right)^2 = 22.5\ \mathrm{mA}
> \quad\text{(enhancement mode)}$$
> Both printed answers confirmed ✓. **This pair of numbers is the whole difference between a JFET and
> a DE MOSFET in one line:** part (ii) — a current more than twice $I_{DSS}$ — is impossible for a
> JFET, whose gate junction would be forward-biased at $+4\ \mathrm{V}$.

[exercise 2 ·L4 p23] The data sheet of a certain zero-biased DE MOSFET gives $I_{DSS} = 15\ \mathrm{mA}$
and $V_{GS(off)} = 5\ \mathrm{V}$. What is the drain current? **[15 mA]**

> **[added] Solution.** Zero-biased means $V_{GS}=0$, and at $V_{GS}=0$ the drain current is by
> definition $I_{DSS}$:
> $$\boxed{\;I_D = I_{DSS} = 15\ \mathrm{mA}\;}$$
> Printed answer confirmed ✓. $V_{GS(off)}$ is not needed.

> ⚠ VERIFY **C4.20** ·L4 p23 — this problem quotes $V_{GS(off)} = 5\ \mathrm{V}$, **positive**. For
> an N-channel depletion device $V_{GS(off)}$ is negative (·L4 p5 footnote, and every other problem
> in both tutorial sets); $-5\ \mathrm{V}$ is meant. The answer does not depend on it.
> See `_verification-log.md`.

[exercise 3 ·L4 p23] A certain E-only N-channel MOSFET has $I_{D(on)} = 4\ \mathrm{mA}$ at
$V_{GS} = 8\ \mathrm{V}$ and $V_{GS(th)} = 2\ \mathrm{V}$. Calculate $I_D$ for
$V_{GS} = 6\ \mathrm{V}$. **[1.78 mA]**

> **[added] Solution.**
> $$K = \frac{4}{\left(8-2\right)^2} = \frac{4}{36} = 0.1111\ \mathrm{mA/V^2}$$
> $$I_D = 0.1111\left(6-2\right)^2 = 0.1111\times16 = 1.78\ \mathrm{mA}$$
> Printed answer confirmed ✓.

[exercise 4 ·L4 p24] The parameters of the E-only N-channel MOSFET of Fig. 63.38 (*a*) are
$V_{GS(th)} = 2\ \mathrm{V}$ and $K = 0.3\ \mathrm{mA/V^2}$. Determine $I_D$ and $V_{DS}$. If the gate
is connected as in Fig. 63.38 (*b*), what are the new values?
**[(i) 2.07 mA (ii) 4.63 V ; 0 A, 15 V]**

> **[added] Solution.** **Circuit (a), drain-feedback bias:** $V_{GS} = V_{DS}$, so with all
> currents in mA and resistances in kΩ,
> $$I_D = \frac{15-V_{DS}}{5} = 0.3\left(V_{DS}-2\right)^2$$
> $$15 - V_{DS} = 1.5\left(V_{DS}^2 - 4V_{DS} + 4\right)$$
> $$1.5V_{DS}^{2} - 5V_{DS} - 9 = 0$$
> $$V_{DS} = \frac{5\pm\sqrt{25+54}}{3} = \frac{5\pm 8.888}{3} = 4.63\ \mathrm{V}
> \quad\text{(the negative root } -1.30\ \mathrm{V}\text{ is discarded)}$$
> $$I_D = \frac{15-4.63}{5} = 2.07\ \mathrm{mA}$$
> **Circuit (b), gate grounded:** $V_{GS} = 0 < V_{GS(th)}$, so
> $$I_D = 0,\qquad V_{DS} = V_{DD} = 15\ \mathrm{V}$$
> All four printed answers confirmed ✓.

[exercise 5 ·L4 p24] The data sheet for the E-only N-channel MOSFET of Fig. 63.38 (*c*) gives
$I_{D(on)} = 3\ \mathrm{mA}$ at $V_{GS} = 10\ \mathrm{V}$ and $V_{GS(th)} = 5\ \mathrm{V}$. Calculate
$V_{GS}$ and $V_{DS}$. **[14.4 V ; 13.4 V]**

> **[added] Solution.**
> $$V_{GS} = V_{DD}\frac{R_2}{R_1+R_2} = 24\times\frac{15}{25} = 14.4\ \mathrm{V}$$
> $$K = \frac{3}{\left(10-5\right)^2} = 0.12\ \mathrm{mA/V^2}$$
> $$I_D = 0.12\left(14.4-5\right)^2 = 0.12\times88.36 = 10.6\ \mathrm{mA}$$
> $$V_{DS} = 24 - 10.6\times1 = 13.4\ \mathrm{V}$$
> Both printed answers confirmed ✓.

[exercise 6 ·L4 p24] The amplifier of Fig. 63.38 (*d*) uses an E-only N-channel MOSFET with
$I_{D(on)} = 5\ \mathrm{mA}$ at $V_{GS} = 10\ \mathrm{V}$, $V_{GS(th)} = 4\ \mathrm{V}$ and
$g_m = 5500\ \mathrm{\mu S}$. Calculate $V_{GS}$, $I_D$, $V_{DS}$ and $v_o$.
**[6 V ; 0.556 mA ; 12.2 V ; 0.825 V]**

> **[added] Solution.**
> $$V_{GS} = 15\times\frac{20}{50} = 6\ \mathrm{V}$$
> $$K = \frac{5}{\left(10-4\right)^2} = \frac{5}{36} = 0.1389\ \mathrm{mA/V^2}$$
> $$I_D = 0.1389\left(6-4\right)^2 = 0.556\ \mathrm{mA}$$
> $$V_{DS} = V_{DD} - I_D R_L = 15 - 0.556\times3 = 13.3\ \mathrm{V}$$
> $$v_o = g_m R_L v_i = 5500\times10^{-6}\times3\times10^{3}\times50\ \mathrm{mV}
> = 16.5\times50\ \mathrm{mV} = 825\ \mathrm{mV} = 0.825\ \mathrm{V}$$
> $V_{GS}$, $I_D$ and $v_o$ confirmed ✓; $V_{DS}$ does not agree — see the flag.

> ⚠ VERIFY **V4.15** ·L4 p24 — the printed $V_{DS}$ answer is **12.2 V**. With the drain resistor
> that Fig. 63.38 (*d*) actually shows, $3\ \mathrm{k\Omega}$,
> $$\boxed{\;V_{DS} = 15 - 0.556\times3 = 13.3\ \mathrm{V}\;}$$
> 12.2 V is what a $5\ \mathrm{k\Omega}$ drain resistor would give ($15 - 2.78$). The same answer
> line's own $v_o = 0.825\ \mathrm{V}$ can only come from $R_L = 3\ \mathrm{k\Omega}$
> ($5500\ \mathrm{\mu S}\times5\ \mathrm{k\Omega}\times50\ \mathrm{mV}$ would give 1.375 V), so the
> answer set is internally inconsistent and $3\ \mathrm{k\Omega}$ is the right reading.
> See `_verification-log.md`.

[exercise 7 ·L4 p24] A field-effect transistor has a small-signal equivalent circuit with input
resistance $1000\ \mathrm{M\Omega}$, forward transfer conductance $4\ \mathrm{mS}$ and output
conductance $100\ \mathrm{\mu S}$ at the operating point $V_{DS} = +4\ \mathrm{V}$,
$I_D = 2\ \mathrm{mA}$, $V_{GS} = -2\ \mathrm{V}$. Draw the circuit you would use for a single-stage
voltage amplifier. Describe the use and specify the value of as many components as possible if a
$30\ \mathrm{V}$ supply were available. What voltage gain would you expect when the output is
unloaded? Give reasons which might account for not getting this gain exactly.
**[Drain load = 12 kΩ, Source bias resistor = 1 kΩ, −21.8]**

> **[added] Solution.**
> **Circuit.** A common-source stage with self-bias: $+30\ \mathrm{V}$ rail; drain load $R_L$ from
> the rail to the drain; output taken from the drain through a coupling capacitor; input applied
> through a coupling capacitor to the gate; gate resistor $R_G$ (a few MΩ — it need not be small,
> since $I_G$ is negligible, and it sets the input resistance of the stage) from gate to ground;
> source resistor $R_S$ from source to ground, **bypassed by a large capacitor**.
> **Translating the data.**
> $$g_m = 4\ \mathrm{mS};\qquad r_d = \frac{1}{g_{os}} = \frac{1}{100\ \mathrm{\mu S}} = 10\ \mathrm{k\Omega}$$
> **Source bias resistor** — it must produce $V_{GS} = -2\ \mathrm{V}$ at $I_D = 2\ \mathrm{mA}$:
> $$R_S = \frac{|V_{GS}|}{I_D} = \frac{2\ \mathrm{V}}{2\ \mathrm{mA}} = 1\ \mathrm{k\Omega}$$
> **Drain load** — the supply must cover $V_{DS}$, the drop in $R_S$ and the drop in $R_L$:
> $$V_{R_L} = V_{DD} - V_{DS} - I_D R_S = 30 - 4 - 2 = 24\ \mathrm{V}$$
> $$R_L = \frac{24\ \mathrm{V}}{2\ \mathrm{mA}} = 12\ \mathrm{k\Omega}$$
> **Unloaded gain**:
> $$A_v = -g_m\left(r_d\parallel R_L\right) = -4\times10^{-3}\times\frac{10\times12}{22}\ \mathrm{k\Omega}
> = -4\times10^{-3}\times 5.455\ \mathrm{k\Omega} = -21.8$$
> All three printed answers confirmed ✓.
> **Why the measured gain would fall short:** (1) any external load placed on the output appears in
> parallel with $R_L$ and reduces the a.c. load; (2) if $R_S$ is left **unbypassed**, negative
> feedback reduces the gain to roughly $-g_mR_L/(1+g_mR_S)$; (3) at high frequency, $C_{gd}$
> multiplied by the Miller effect shunts the input and $C_{ds}$ shunts the output; (4) $g_m$ and
> $r_d$ are strong functions of the operating point and spread widely between samples.

[exercise 8 ·L4 p24] A field-effect transistor is used as a voltage amplifier: with a load resistor
of $40\ \mathrm{k\Omega}$ a gain of 40 is obtained; when the load resistance is halved, the gain
drops to 30. Calculate the output resistance and the mutual conductance of the transistor. Briefly
compare the advantages and limitations of the FET with the bipolar transistor. **[20 kΩ, 3 mS]**

> **[added] Solution.** "Mutual conductance" is $g_m$; "output resistance" is $r_d$. Use
> $A_v = \mu R_L/(r_d+R_L)$ in magnitude, with $\mu = g_m r_d$, and work in kΩ.
> $$40 = \frac{\mu\times 40}{r_d+40}\quad\Longrightarrow\quad \mu = r_d + 40$$
> $$30 = \frac{\mu\times 20}{r_d+20}\quad\Longrightarrow\quad \mu = 1.5\left(r_d+20\right)$$
> Equating:
> $$r_d + 40 = 1.5r_d + 30 \quad\Longrightarrow\quad 0.5\,r_d = 10$$
> $$\boxed{\;r_d = 20\ \mathrm{k\Omega}\;}$$
> $$\mu = 20+40 = 60,\qquad g_m = \frac{\mu}{r_d} = \frac{60}{20\ \mathrm{k\Omega}} = 3\ \mathrm{mS}$$
> Both printed answers confirmed ✓. Check:
> $A_v = 3\times10^{-3}\times(20\parallel40)\ \mathrm{k\Omega} = 40$ ✓ and
> $A_v = 3\times10^{-3}\times(20\parallel20)\ \mathrm{k\Omega} = 30$ ✓.
> **FET versus BJT** (from §4.13, ·L4 p15, plus the contrasts made through the chapter): the FET has
> far higher input impedance, is **unipolar** (no minority-carrier storage), has lower noise, a
> **negative** temperature coefficient of drain current so it will not thermally run away or hog
> current when paralleled, no offset voltage as a switch, smaller size for integration, and is
> voltage-controlled; against that it has a **small gain-bandwidth product**, a much lower
> transconductance than a BJT at the same current (so less voltage gain per stage), and it is easily
> damaged by static in handling.

---

## 4.25 Objective test 63 ·L4 p24

Ten multiple-choice questions are printed. **No answer key is printed in this extract**, so every
answer below is `[added]` — worked out here, with the reasoning and the page that settles it.

[exercise ·L4 p24] **1.** A FET consists of a — (*a*) source (*b*) drain (*c*) gate (*d*) all of the
above.

> **[added] (d).** A FET is a three-terminal device: source, drain and gate. ·L4 p3

[exercise ·L4 p24] **2.** FETs have similar properties to — (*a*) PNP transistors (*b*) NPN
transistors (*c*) thermionic valves (*d*) unijunction transistors.

> **[added] (c) thermionic valves.** ·L4 p2 opens by defining a FET as a device "in which current is
> controlled by an electric field **as is done in vacuum tubes**", and ·L4 p15 says FETs combine the
> advantages of BJTs **and** vacuum tubes. Both are voltage-controlled with a very high input
> impedance. (The page prints "thermonic" for thermionic.)

[exercise ·L4 p24] **3.** For small values of drain-to-source voltage, a JFET behaves like a —
(*a*) resistor (*b*) constant-current source (*c*) constant-voltage source (*d*) negative resistance.

> **[added] (a) resistor.** That is the definition of the ohmic region OA. ·L4 p5–p6

[exercise ·L4 p24] **4.** In a JFET, the *primary* control on drain current is exerted by —
(*a*) channel resistance (*b*) size of depletion regions (*c*) voltage drop across channel
(*d*) gate reverse bias.

> **[added] (b) size of the depletion regions.** The chain of causation on ·L4 p4 and ·L4 p11 runs:
> gate reverse bias → **size of the depletion regions** → channel cross-section and resistance →
> $I_D$. The depletion regions are the immediate control, and they respond to $V_{DS}$ as well as to
> $V_{GS}$ — which is why a JFET pinches off even with the gate shorted to the source, where option
> (*d*) is zero. Option (*d*) is the *external* control; if a question's key gives (*d*), it is
> reading "primary control" as "what the user adjusts".

[exercise ·L4 p24] **5.** After $V_{DS}$ reaches the pinch-off value $V_P$ in a JFET, drain current
$I_D$ becomes — (*a*) zero (*b*) low (*c*) saturated (*d*) reversed.

> **[added] (c) saturated.** ·L4 p6 is emphatic: "pinch-off does not mean current-off" — beyond
> pinch-off, $I_D$ holds constant at its maximum.

[exercise ·L4 p24] **6.** In a JFET, as the external bias applied to the gate is increased —
(*a*) channel resistance is decreased (*b*) drain current is increased (*c*) pinch-off voltage is
reached at lower values of $I_D$ (*d*) size of depletion regions is reduced.

> **[added] (c).** ·L4 p6 lists exactly this as the first consequence of increasing the negative gate
> bias. The other three options are each the reverse of what happens: the depletion regions **grow**,
> channel resistance **rises** and $I_D$ **falls**.

[exercise ·L4 p24] **7.** In a JFET, drain current is maximum when $V_{GS}$ is — (*a*) zero
(*b*) negative (*c*) positive (*d*) equal to $V_p$.

> **[added] (a) zero.** $I_D = I_{DSS}$ at $V_{GS}=0$, and $I_{DSS}$ is the largest current the JFET
> passes. ·L4 p4. (Option (*c*) is a trap: a positive $V_{GS}$ would forward-bias the gate junction of
> a JFET — it is legitimate only for a **DE MOSFET**.)

[exercise ·L4 p24] **8.** The voltage gain of a given common-source JFET amplifier depends on its —
(*a*) input impedance (*b*) amplification factor (*c*) dynamic drain resistance (*d*) drain load
resistance.

> **[added] (d) drain load resistance** is the intended single answer — it is the one quantity the
> circuit designer chooses. In strict truth the chapter's own formula
> $$A_v = \frac{-\mu R_L}{r_d + R_L}$$
> contains (*b*), (*c*) and (*d*), and only the input impedance (*a*) is absent. ·L4 p12

[exercise ·L4 p24] **9.** A JFET has the disadvantage of — (*a*) being noisy (*b*) having a small
gain-bandwidth product (*c*) possessing a positive temperature coefficient (*d*) having low input
impedance.

> **[added] (b) small gain-bandwidth product.** It is the first of the two disadvantages listed on
> ·L4 p15. The other options are the opposites of the listed **advantages** — FETs are low-noise, have
> a *negative* temperature coefficient and a *high* input impedance.

[exercise ·L4 p24] **10.** A JFET can be cut off with the help of — (*a*) $V_{GS}$ (*b*) $V_{DS}$
(*c*) $V_{DG}$ (*d*) $V_{DD}$.

> **[added] (a) $V_{GS}$.** Cut-off is defined by $V_{GS(off)}$ — the gate-source voltage at which
> the two depletion regions meet and close the channel. ·L4 p4–p5. Raising $V_{DS}$ produces
> *pinch-off*, which is emphatically **not** cut-off.

---

## 4.26 [added] Formula recap

Everything needed for a numerical question on this lesson, in one place. Every entry appears in the
body above with its page citation; the corrected form is given where the chapter's print is defective.

| Quantity | Expression | Where |
|---|---|---|
| Shockley's equation | $I_D = I_{DSS}\left(1 - V_{GS}/V_{GS(off)}\right)^2$ | §4.5 |
| inverse form | $V_{GS} = V_{GS(off)}\left(1-\sqrt{I_D/I_{DSS}}\right)$ | §4.7 |
| pinch-off and cut-off | $\lvert V_{PO}\rvert = \lvert V_{GS(off)}\rvert$, $V_{GS(off)} = -V_{PO}$ | §4.3 |
| pinch-off at any bias | $V_{DS(P)} = V_P + V_{GS}$ | §4.6 |
| a.c. drain resistance | $r_d = \left.\delta V_{DS}/\delta I_D\right\rvert_{V_{GS}}$ | §4.8 |
| transconductance | $g_m = \left.\delta I_D/\delta V_{GS}\right\rvert_{V_{DS}}$ | §4.8 |
| $g_m$ from device data | $g_m = -\dfrac{2I_{DSS}}{V_P}\left(1-\dfrac{V_{GS}}{V_P}\right)$ | §4.8 |
| $g_{mo}$ | $g_{mo} = 2I_{DSS}/\lvert V_{GS(off)}\rvert$ | §4.8 |
| $g_m$ from $g_{mo}$ | $g_m = g_{mo}\left(1-V_{GS}/V_P\right) = g_{mo}\sqrt{I_D/I_{DSS}}$ | §4.8 |
| amplification factor | $\mu = g_m r_d$ | §4.8 |
| d.c. drain resistance | $R_{DS} = V_{DS}/I_D$ | §4.8 |
| self-bias | $V_{GS} = -I_D R_S$ | §4.9 |
| source bias | $V_{GS} = V_{SS} - I_D R_S$ | §4.9 |
| divider bias (JFET) | $V_{GS} = V_{DD}\dfrac{R_2}{R_1+R_2} - I_D R_S$ | §4.9 |
| load line | $V_{DS}=V_{DD}$ at $I_D=0$; $I_D = V_{DD}/R_L$ at $V_{DS}=0$ | §4.10 |
| mid-point bias | $V_{DSQ} = \tfrac12 V_{DD}$, $I_{DSQ} = \tfrac12 V_{DD}/(R_S+R_L)$, $V_{GS}=V_{GS(off)}/4$, $I_D\cong I_{DSS}/2$ | §4.10 |
| CS gain | $A_v = -g_m\left(r_d\parallel R_L\right) = -\mu R_L/(r_d+R_L)$ | §4.12 |
| Miller input capacitance | $C_i = C_{gs} + (1-A_v)C_{gd}$ | §4.12 |
| CD (source follower) gain | $A_v = \dfrac{g_m r_d R_L}{r_d+R_L+g_m r_d R_L}\cong 1$ | §4.12 |
| CD output resistance | $r'_o = \dfrac{r_d}{1+g_m r_d}\parallel R_L \cong \dfrac{1}{g_m}\parallel R_L$ | §4.12 |
| CG gain and input resistance | $A_v = +g_m\left(r_d\parallel R_L\right)$, $r_i = 1/g_m$ | §4.12 |
| E-MOSFET drain current | $I_D = K\left(V_{GS}-V_{GS(th)}\right)^2$ | §4.19 |
| E-MOSFET $K$ | $K = I_{D(ON)}/\left(V_{GS}-V_{GS(th)}\right)^2$ | §4.19 |
| E-MOSFET $g_m$ | $g_m = 2K\left(V_{GS}-V_{GS(th)}\right)$ | §4.19 |
| E-MOSFET divider bias | $V_{GS} = V_{DD}R_2/(R_1+R_2)$; $V_{DS} = V_{DD}-I_DR_L$ | §4.20 |
| E-MOSFET drain-feedback bias | $V_{GS} = V_{DS}$ | §4.20 |

---

## 4.27 [added] Coverage map

| PDF pages | Printed pages | Content | Section here |
|---|---|---|---|
| p1 | — | chapter opener, learning objectives | §4.0 |
| p2 | 2364 | §63.1 what is a FET; family tree; §63.2 (a) construction | §4.1, §4.2 |
| p3 | 2365 | terminal notation; symbols; §63.2 (b) theory of operation | §4.2, §4.3 |
| p4 | 2366 | wedge-shaped depletion regions; pinch-off; cut-off | §4.3 |
| p5 | 2367 | $V_{GS(off)}$; summary; §63.3 static characteristics; §63.4 ohmic region | §4.3, §4.5 |
| p6 | 2368 | four regions of the drain characteristic; Shockley; §63.5 external bias | §4.5, §4.6 |
| p7 | 2369 | why $V_P$ falls with bias; §63.6 transfer characteristic; §63.7 $r_d$ | §4.6, §4.7, §4.8 |
| p8 | 2370 | $g_m$, $g_{mo}$, $\mu$, $R_{DS}$; **Example 63.1** | §4.8 |
| p9 | 2371 | §63.8 four bias circuits; **Example 63.2**; §63.9 load line | §4.9, §4.10 |
| p10 | 2372 | Q-point; **Examples 63.3, 63.4**; Figs 63.9–63.12 | §4.10 |
| p11 | 2373 | **Example 63.5**; §63.10 CS amplifier working | §4.10, §4.11 |
| p12 | 2374 | §63.11 gains — CS input/output resistance, gain, Miller; **Example 63.6** | §4.12 |
| p13 | 2375 | **Example 63.7**; common-drain amplifier | §4.12 |
| p14 | 2376 | **Example 63.8**; common-gate amplifier | §4.12 |
| p15 | 2377 | CG input/output resistance; §63.12 advantages; **Tutorial 63.1** | §4.12–§4.14 |
| p16 | 2378 | §63.13 MOSFET family; §63.14 DE MOSFET construction | §4.15, §4.16 |
| p17 | 2379 | DE MOSFET depletion and enhancement modes | §4.16 |
| p18 | 2380 | §63.15 symbols; §63.16 static characteristics; **Example 63.9** | §4.17, §4.18 |
| p19 | 2381 | §63.17 enhancement-only NMOS; threshold; K equation | §4.18, §4.19 |
| p20 | 2382 | E-MOSFET characteristics; $g_m$; §63.18 biasing; **Example 63.10** | §4.19, §4.20 |
| p21 | 2383 | **Example 63.11**; §63.19 FET amplifiers — DE MOSFET stage | §4.20, §4.21 |
| p22 | 2384 | E-MOSFET amplifier; **Examples 63.12, 63.13, 63.14** | §4.21 |
| p23 | 2385 | §63.20 applications; §63.21 handling; **Tutorial 63.2** (1–3) | §4.22–§4.24 |
| p24 | 2386 | **Tutorial 63.2** (4–8); **Objective test 63** | §4.24, §4.25 |

**Verification summary for this file:** 15 substantive flags (`V4.1`–`V4.15`) and 21 cosmetic flags
(`C4.1`–`C4.21`), 36 in total. Every one of the 14 worked examples and all 25 tutorial/objective
questions has been recomputed independently; five printed answers disagree with the recomputation
(`V4.7`, `V4.9`, `V4.12`, `V4.13`, `V4.15`) and one worked example is unreproducible from its own data
(`V4.10`).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
