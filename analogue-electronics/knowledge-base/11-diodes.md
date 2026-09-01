---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "11 — Semiconductor Diodes (supporting)"
source: "L1 — 'Lesson 1 Notes Diodes.pdf', 18 pp."
pages: "1-18"
tier: supporting
file_role: topic
subtopics:
  - "the p-n junction: depletion layer, fixed ions, diffusion and drift"
  - "junction (barrier) voltage, its doping dependence and its temperature coefficient"
  - "forward and reverse bias; the static V/I characteristic and reverse breakdown"
  - "the diode equation (Boltzmann/Shockley form), the ideality factor and the thermal voltage"
  - "diode parameters: bulk, junction and dynamic ac resistance; forward drop; reverse dc resistance"
  - "applications of the junction diode, including the varactor capacitance law"
  - "the Zener diode: breakdown mechanisms, characteristic, symbol and equivalent circuits"
  - "Zener biasing checks and the shunt voltage regulator, with six worked circuits"
  - "the light-emitting diode: theory, materials, construction, working and applications"
  - "seven-segment displays, multicoloured and blinking LEDs, LEDs in fax machines"
  - "equivalent circuit of a forward- and a reverse-biased p-n junction"
key_equations: [barrier-voltage, thermal-voltage, barrier-temp-coeff, diode-equation, diode-eta, diode-40-20, diode-voltage-from-current, diode-current-ratio, bulk-resistance, junction-resistance, ac-resistance, forward-drop, reverse-dc-resistance, varactor-capacitance, zener-node, zener-series-r, zener-series-r-max, zener-power, io-temperature]
prerequisites: ["intrinsic and extrinsic semiconductors; donors and acceptors; majority and minority carriers", "Ohm's law, KCL/KVL, series-parallel resistive analysis"]
leads_to: ["rectifiers and power supplies", "clippers, clampers and wave-shaping", "bipolar junction transistors and their biasing"]
verification_flags: 17
tags: [pn-junction, depletion-layer, barrier-voltage, diode-equation, ideality-factor, thermal-voltage, diode-resistance, zener-diode, breakdown, voltage-regulator, led, seven-segment, varactor, equivalent-circuit]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] table of data or comparisons ·
  [added] supplied here, NOT in the source ·
  ·L1 pN = provenance (which PDF page of Lesson 1 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = a page or figure that could not be read.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 01 — Semiconductor Diodes

Scope: the whole of L1, 18 pages. Builds the p-n junction from first principles, derives the barrier
voltage and its temperature dependence, develops the static V/I characteristic and the diode
equation, lists the diode's small-signal parameters, then treats the two special diodes the course
names — the **Zener diode** (with six fully worked regulator circuits) and the **LED** — and closes
with the equivalent circuit of the junction.

> ## ⚠ Read §1.5 before using the diode equation for anything
>
> **The handout writes the diode equation out in six places, and three of those printings are
> defective.** The highlighted "master" form on p6 drops the ideality factor $\eta$; all four
> highlighted forms on p7 put the $-1$ **inside** the exponent, as does the opening line of Example
> 52.2 on p8. The equation is printed correctly on p6 (the Ge/Si and $11{,}600$ forms) and on p18.
> Three of this file's six substantive flags come from that one fault line.

**Two things the p1 outline promises that the 18 pages never deliver:** **tunnel diodes** and the
**load line**. Both are named in the topic outline; neither appears anywhere in the document. See
§1.14 for the gap map and an `[added]` load-line primer.

**Why this file is not split.** It exceeds the ~25 KB threshold, but it is **one continuous
argument** — the junction physics of §1.2 produces the barrier voltage of §1.3, which produces the
characteristic of §1.4, which produces the diode equation of §1.5, on which the Zener work of
§1.8–§1.10 and the LED work of §1.11 both depend. Splitting would sever the diode equation from the
examples that use it. Per `../../docs/kb-format.md`, one lesson stays one topic file.


---

## 1.1 How this file maps onto the handout ·L1 p1–p18

The handout is a compiled photocopy of textbook articles, reproduced under a Strathmore/BEE 3103
header. Two consequences for navigation:

- **The article numbers are the parent textbook's, and they run out of order** — 51.38, 51.39, 51.40
  (p1–p4), then 52.x (p5–p8), then 54.1, 54.2 (p8–p13), then 53.2, 53.3 (p13–p16), then back to 52.5
  (p17) and Examples 52.6–52.8 (p17–p18). Citations in this file are to the **PDF page**, which is
  the reliable coordinate.
- **There are internal jumps.** Page 5 opens at sub-heading *(d) V/I Characteristic*, so parts
  (a)–(c) of that article are not in the handout; and the statement of the example whose solution
  opens p11 is missing (C1.7).

**There are no unsolved exercises or tutorial questions anywhere in these 18 pages.** Every problem
set is a fully worked example. The `[added]` blocks below are therefore verification of the
lecturer's arithmetic and supplied gap-filling, not solutions to unsolved questions.

**Where the work is.** Roughly a third of the document is worked numbers: eleven examples in all
(51.13, 51.14, 52.1, 52.2, 52.6, 52.7, 52.8, 54.1, 54.2, 54.3, 54.5, 54.6, 54.7 — thirteen if the
un-numbered Fig. 54.6 example is counted). Nine of them are Zener or diode-equation arithmetic. That
weighting is the exam signal.

---

## 1.2 The p-n junction and the depletion layer ·L1 p1–p3

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $N_a$ | acceptor (P-side) doping density | m⁻³ | $10^{21}$ |
| $N_d$ | donor (N-side) doping density | m⁻³ | $10^{22}$ |
| $n_i$ | intrinsic carrier density | m⁻³ | $1.4\times10^{16}$ (Si) |
| $W$ | depletion-layer thickness | m | $\sim 10^{-6}$ |
| $V_B$ | barrier (junction) potential | V | 0.3 (Ge), 0.7 (Si) |

[def ·L1 p1] **The p-n junction.** A single piece of semiconductor is doped P-type over one half and
N-type over the other. The plane dividing the two zones is the **junction**; theoretically it lies
where the donor and acceptor densities are equal. This junction is the basis of diodes, transistors
and every other solid-state device.

[fig ·L1 p1] **Opening photograph.** A cylindrical bar with metal end leads. The left half is orange,
labelled **P-type**, filled with small open circles labelled **Holes**; the right half is blue,
labelled **N-type**, filled with dots labelled **Electrons**, each carrying a leftward arrow. The
boundary between the halves is arrowed and labelled **JUNCTION**; the end leads are labelled
**METAL**.

[fig ·L1 p1] **Fig. 51.32.** A rectangle divided by a vertical line. Left half headed **P**, filled
with three rows of $+$ signs; right half headed **N**, filled with three rows of $-$ signs. An arrow
from below points at the dividing line, labelled **Junction**.

### The three things that happen at a junction ·L1 p1

1. A thin **depletion layer** (also *space-charge region*, *transition region*) forms on both sides
   of the junction, so called because it is depleted of **free charge carriers**. Its thickness is
   about $10^{-6}\ \mathrm{m}$.
2. A **barrier potential** (junction potential) is developed across the junction.
3. The depletion layer gives rise to **junction and diffusion capacitances** (see §1.14).

### Why the layer forms ·L1 p2

[derivation] The mechanism in four steps:

1. At the instant the junction is formed, holes are still in the P-region and electrons in the
   N-region.
2. Hole concentration is far higher in P than in N (where holes are *minority* carriers), and
   electron concentration far higher in N than in P. This concentration difference is a **density
   gradient** across the junction.
3. The gradient drives **diffusion**: holes diffuse P→N, electrons diffuse N→P, and they terminate
   their existence by **recombination**.
4. That recombination clears a narrow region at the junction of mobile carriers — the depletion
   layer.

> ⚠ VERIFY **V1.1** ·L1 p2 — printed as *"there being present only **positive ions** which are not
> free to move."* The depletion layer contains **both** signs of fixed ion: **negative acceptor ions
> on the P side** and **positive donor ions on the N side**. Correct form:
> $$\boxed{\;\text{depletion layer} = \text{fixed } \ominus \text{ acceptor ions (P side)} \;+\; \text{fixed } \oplus \text{ donor ions (N side)}\;}$$
> **One-line disproof:** the page's own Fig. 51.33(b) draws $\ominus$ on the P side and $\oplus$ on
> the N side, and p3 states both rows explicitly. With one sign only there is no charge separation,
> hence no barrier potential and no diode. See `_verification-log.md`.

[fig ·L1 p2] **Photograph, top right.** A biased junction: a rectangular bar with the left region
holding open circles labelled **HOLES** and the right region holding dashes labelled **ELECTRONS**,
separated by a hatched band. Callipers at the top mark the widened **DEPLETION REGION** against the
narrower **ORIGINAL BARRIER** marked below. A battery sits under the bar; a long arrow beneath is
labelled **ELECTRON FLOW**.

[fig ·L1 p2] **Fig. 51.33 — three panels, the core figure of the section.**

- **(a) Diffusion.** P block of $+$ signs, N block of $-$ signs. Two curved arrows cross the junction
  in opposite directions — one carrying $+$ from P into N, one carrying $-$ from N into P.
- **(b) Depletion layer.** The same block, but now a narrow band straddling the junction contains a
  column of circled $\ominus$ on the **P side** and a column of circled $\oplus$ on the **N side**.
  These are labelled **Fixed Ions**; the $+$ and $-$ populations outside the band are labelled
  **Mobile Charges**. A brace under the band labels it **Depletion Layer**.
- **(c) Capture at the edge.** The same picture with a curved arrow showing a mobile carrier
  approaching the depletion layer from the N side and being neutralised at the row of fixed ions.

### Why diffusion stops ·L1 p3

The impurity atoms that supplied the migrating carriers are left behind **ionised**, carrying a
charge opposite to that of the departed carrier, and — like the host lattice atoms — they are
**fixed in the crystal**. They form parallel rows of opposite charge facing each other across the
depletion layer:

- **fixed positive ions in the N-region**, produced by electrons migrating N→P;
- **fixed negative ions in the P-region**, produced by holes migrating P→N.

A majority carrier that tries to cross then meets one of two fates ·L1 p3:

- **(i)** it is **trapped** by the row of fixed ions of opposite sign guarding its own region — a
  hole approaching from P is neutralised by the fixed negative ions at the P-side edge, and likewise
  for an electron from N [Fig. 51.33(c)]; or
- **(ii)** it **enters** the depletion layer, is repelled by the similarly-charged ions guarding the
  far region, and is cut short by **recombination** with an opposite carrier that entered from the
  other half.

Equilibrium is reached when the layer has widened so far that **no electrons or holes can cross**.

[fig ·L1 p3] **Stray picture, right column.** A cut-away dome-shaped LED package containing two chips
drawn as opposed triangles about a common central post, with light-emission arrows, and leads
labelled **a1**, **a2** and **k**. Nothing on p3 refers to it — it belongs with the multicoloured-LED
discussion, where the same picture reappears (C1.10, §1.13).

---

## 1.3 Junction or barrier voltage ·L1 p3–p4, p17–p18

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_B$ | barrier (junction) potential | V | 0.3 (Ge), 0.7 (Si) at 300 K |
| $V_T$ | thermal voltage, $kT/e$ | V | 26 mV at 300 K |
| $k$ | Boltzmann constant | J·K⁻¹ | $1.38\times10^{-23}$ |
| $T$ | absolute temperature | K | 300 |
| $e$ | electronic charge | C | $1.6\times10^{-19}$ |
| $\Delta t$ | temperature **rise** | °C | — |

[def ·L1 p3] Because the depletion layer is cleared of carriers but carries oppositely-charged rows
of fixed ions on its two sides, an electric potential difference $V_B$ exists across the junction
**even when the junction is externally isolated**. It is the **junction** or **barrier potential**,
and it stops further carrier flow unless energy is supplied from outside.

At a room temperature of 300 K: $V_B \approx 0.3\ \mathrm{V}$ for **Ge** and $0.7\ \mathrm{V}$ for
**Si**. ·L1 p3

[eq: barrier-voltage] **The barrier voltage from the doping** ·L1 p3

$$\boxed{\;V_B = V_T\,\ln\!\left(\frac{N_a N_d}{n_i^{2}}\right)\;}$$

[eq: thermal-voltage] **The thermal voltage** ·L1 p3

$$V_T = V_{300} = \frac{kT}{e} = \frac{1.38\times10^{-23}\times 300}{1.6\times10^{-19}} = 26\ \mathrm{mV}$$

*[added] Recomputed: $1.38\times10^{-23}\times300/1.6\times10^{-19} = 25.875\ \mathrm{mV}$ ✓ — the
printed 26 mV is that rounded.*

Combining the two gives the working form the examples use ·L1 p3:

$$\boxed{\;V_B = 26\,\ln\!\left(\frac{N_a N_d}{n_i^{2}}\right)\ \mathrm{mV}\;}\qquad\text{(at 300 K)}$$

> **Caution — $V_T$ takes two different values in this one document.** p3 uses $26\ \mathrm{mV}$ at
> $300\ \mathrm{K}$; p6 and p18 use $25\ \mathrm{mV}$ at $293\ \mathrm{K}$ ("room temperature" of
> 20 °C). Both are correct for their stated temperature. **Always read off which room temperature a
> question intends before substituting.** Full entry in `_nomenclature.md`.

### Temperature dependence ·L1 p3

Barrier voltage depends on doping density, electronic charge and temperature. For a given junction
the first two are fixed, so $V_B$ is a function of temperature alone. As temperature rises, more
minority carriers are produced, their drift across the junction increases, and equilibrium is
reached at a **lower** barrier.

[eq: barrier-temp-coeff] For **both** Ge and Si, $V_B$ falls by about $2\ \mathrm{mV}$ per °C:

$$\boxed{\;\Delta V_B = -0.002\,\Delta t\;}\qquad \Delta t \text{ = temperature rise, °C};\ \Delta V_B \text{ in V}$$

> ⚠ VERIFY **C1.1** ·L1 p3, p6, p8, p18 — temperatures are printed throughout as **"300°K"**,
> "293°K", "398°K", "343°K", and Boltzmann's constant as **"J/°K"**. The kelvin takes no degree
> sign: $300\ \mathrm{K}$, $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$. Nothing computed changes.
> See `_verification-log.md`.

### [ex] Example 51.13 — barrier potential of a silicon junction ·L1 p4

**Statement.** Calculate the barrier potential at room temperature for a P-N junction in silicon
doped to a carrier density of $10^{21}\ \mathrm{m^{-3}}$ on the P-side and $10^{22}\ \mathrm{m^{-3}}$
on the N-side. The intrinsic carrier density for silicon is $1.4\times10^{16}\ \mathrm{m^{-3}}$.
*(Electronics-I, Bangalore Univ. 1992)*

**Solution as printed** ·L1 p4

$$V_B = 26\ln\!\left(\frac{N_a N_d}{n_i^{2}}\right)\ \mathrm{mV}
= 26\ln\frac{10^{21}\times10^{22}}{(1.4\times10^{16})^{2}} = 641\ \mathrm{mV} = \mathbf{0.641\ V}$$

*[added] Verified step by step:*

| Step | Working | Result |
|---|---|---|
| Denominator | $(1.4\times10^{16})^{2}$ | $1.96\times10^{32}\ \mathrm{m^{-6}}$ |
| Argument | $10^{43}/1.96\times10^{32}$ | $5.102\times10^{10}$ |
| Logarithm | $\ln(5.102\times10^{10})$ | $24.656$ |
| Result | $26\times24.656$ | $641.0\ \mathrm{mV}$ ✓ |

*Sanity check: 0.641 V sits just below the quoted 0.7 V rule-of-thumb for silicon, which is what
moderate doping should give.*

> ⚠ VERIFY **C1.2** ·L1 p4, p10, p18 — three cross-references point at articles that do not exist.
> p4 cites "Art. 1.40" for the barrier-voltage relation (it is **Art. 51.40**, p3); p10 cites
> "Art 4.1" for the Zener biasing criteria (**Art. 54.1**, p9); p18 cites "Art. 1.38" for
> $\Delta V_B = -0.002\Delta t$ (**Art. 51.40**, p3). The leading 5 has dropped in each case.
> See `_verification-log.md`.

### [ex] Example 51.14 — change in barrier potential with doping ·L1 p4

**Statement.** Calculate the change in barrier potential of a P-N junction at 300 K if doping on the
N-side is increased 1000 times while doping on the P-side is unchanged.

**Solution as printed** ·L1 p4

$$V_{B1} = 26\ln\!\left(\frac{N_{a1}N_{d1}}{n_i^{2}}\right),\qquad
V_{B2} = 26\ln\!\left(\frac{N_{a2}N_{d2}}{n_i^{2}}\right)$$

$$V_{B2}-V_{B1} = 26\ln\!\left(\frac{N_{a2}N_{d2}}{N_{a1}N_{d1}}\right)
= 26\ln\!\left(\frac{N_{d2}}{N_{d1}}\right) = 26\ln 1000 = \mathbf{179\ mV}$$

*[added] Recomputed: $\ln 1000 = 6.9078$, so $26\times6.9078 = 179.6\ \mathrm{mV}$. The printed
**179 mV** is that truncated rather than rounded (180 mV would be the rounded value). The method is
exact — because $N_a$ cancels, only the **ratio** of the changed doping survives, which is why the
answer needs no absolute doping figures at all. That cancellation is the point of the question.*

> ⚠ VERIFY **C1.3** ·L1 p4 — Example 51.14's first line prints $V_B = 26\log_e(N_a N_d/n^{2})$,
> dropping the subscript **i** from $n_i$. $n$ alone is the free-electron concentration, a different
> quantity; the two later lines restore $n_i^2$. See `_verification-log.md`.

### [ex] Example 52.6 — barrier potential at two temperatures ·L1 p17–p18

**Statement.** Calculate the barrier potential for a Si junction at (a) 100 °C and (b) 0 °C if its
value at 25 °C is 0.7 V. ·L1 p17

**Solution as printed** ·L1 p18

$$\Delta V = -0.002\,\Delta t = -0.002\,(t_2-t_1)$$

**(a)** $\Delta t = 100-25 = 75\ \text{°C}\;\Rightarrow\;\Delta V = -0.002\times75 = -0.15\ \mathrm{V}$

$$V_B(100\,\text{°C}) = 0.7 + (-0.15) = \mathbf{0.55\ V}$$

**(b)** $\Delta t = 0-25 = -25\ \text{°C}\;\Rightarrow\;\Delta V = -0.002\times(-25) = +0.05\ \mathrm{V}$

$$V_B(0\,\text{°C}) = 0.7 + 0.05 = \mathbf{0.75\ V}$$

*[added] Both verified ✓. Note the sign discipline: $\Delta t$ is a signed **rise**, so cooling gives
a positive $\Delta V_B$. The physical check is that a **hotter** junction has a **lower** barrier —
0.55 V at 100 °C — which matches §1.3's minority-carrier argument.*

---

## 1.4 Bias, and the static V/I characteristic ·L1 p4–p6

### Equilibrium: drift balances diffusion ·L1 p4

The strong field set up by $V_B$ drives **drift** of carriers through the depletion layer: holes
drift **N→P** and electrons drift **P→N** (minority carriers in each case, swept by the field). At
equilibrium with no external supply, this drift current must be **equal and opposite** to the
diffusion current, because the net current through the crystal is zero.

[fig ·L1 p4] **Fig. 51.34 — the potential barrier.** Top: the P|N block with the two columns of fixed
ions at the junction, annotated $V_B = 0.3\ \mathrm{V}$ for Ge, $=0.7\ \mathrm{V}$ for Si. Below it,
aligned to the same horizontal scale, a potential profile: a flat line at the P-side level, a ramp
rising across the junction, and a flat line at the higher N-side level, with the step marked by a
vertical double-headed arrow labelled $V_B$ and a zero reference marked **0**. Caption beneath:
**Potential Barrier**.

[fig ·L1 p4] **Fig. 51.35 — diffusion versus drift, two panels.**

- **(a) Diffusion Currents.** A P|N rectangle. An arrow pointing **right** across the junction,
  labelled **Holes Diffuse**; an arrow pointing **left**, labelled **Electrons Diffuse**.
- **(b) Drift Current.** The same rectangle with a **hatched band** at the junction (the depletion
  layer). Three arrows: **Electric Field** pointing **left**; **Holes Drift** pointing **left**
  (N→P); **Electrons Drift** pointing **right** (P→N).

*[added] Read the two panels together and the equilibrium is visible: each carrier type moves one way
by diffusion and the other way by drift, so both net currents vanish.*

> ⚠ VERIFY **C1.4** ·L1 p4 — the caption of Fig. 51.35(a) is printed **"Difusion Currents"**
> (one *f*). The same class of typo recurs: p8 "Silicon is **perferred** to Ge"; p11 "This
> **increases** in I will be absorbed" (for *increase*) and "thus **againt** keeping $V_{out}$
> constant"; p15 "To **chose** emitting diodes" and "Each of **this** segments". Nothing computed
> changes. See `_verification-log.md`.

**Summary of Arts. 51.39–51.40, as the handout states it** ·L1 p4

1. As soon as the P-N junction is formed, free electrons and holes start diffusing across the
   junction and recombining.
2. Their recombination produces a depletion layer containing **no mobile carriers, only immobile
   ions**.
3. Those immobile ions set up a barrier potential, hence an electric field, hence a drift current
   equal and opposite to the diffusion current at final equilibrium.

### Forward characteristic ·L1 p5

- With the diode **forward-biased** and the applied voltage raised from zero, **hardly any current
  flows at first**, because the external voltage is opposed by the internal barrier $V_B$
  ($0.7\ \mathrm{V}$ Si, $0.3\ \mathrm{V}$ Ge).
- Once $V_B$ is **neutralised**, current rises rapidly with applied voltage.
- As little as $1.0\ \mathrm{V}$ produces a forward current of about $50\ \mathrm{mA}$.
- Beyond a safe limit, **burnout** follows.

[fig ·L1 p5] **Forward-biased diode, colour panel.** A bar in three colour blocks: blue **N** on the
**left** with a $-$ terminal outside, a yellow depletion band in the middle, red **P** on the
**right** with a $+$ terminal outside. Five arrows cross the yellow band: white arrows carrying
$\oplus$ symbols travel **right→left** (holes injected P→N); black arrows carrying $\ominus$ symbols
travel **left→right** (electrons injected N→P).

> **Orientation warning.** This panel and the reverse-bias panel below put **N on the left**, the
> mirror image of Figs. 51.32–51.35 and 51.33, which put **P on the left**. Check which way round a
> figure is drawn before reading current directions off it.

### Reverse characteristic ·L1 p5

- Majority carriers are blocked; only a small current flows, carried by **minority carriers**.
- Raising the reverse voltage from zero, this current very quickly reaches its **saturation value
  $I_0$**, also called the **leakage current**.
- Order of magnitude: **nanoamperes for Si**, **microamperes for Ge**.
- $I_0$ (also written $I_s$) is **independent of the applied reverse voltage** but depends on
  **(a)** temperature, **(b)** degree of doping and **(c)** physical size of the junction.
- Beyond a certain reverse voltage — the **break-down voltage $V_{BR}$**, or **Zener voltage $V_z$**
  — the leakage current increases suddenly and sharply, the curve indicating **zero resistance** at
  that point. Further increase produces burnout unless a **current-limiting resistor** protects the
  diode.
- Diodes employed primarily for this breakdown property, as voltage regulators, are **Zener diodes**
  (§1.9).

[fig ·L1 p5] **Reverse-biased diode, colour panel.** Same bar, blue **N** left with a $+$ terminal,
red **P** right with a $-$ terminal. The yellow depletion band is **noticeably wider** and carries a
dashed centre line. Electrons ($\ominus$) are bunched at the far left of the N block and holes
($\oplus$) at the far right of the P block — both pulled **away** from the junction by the external
supply.

### The combined static characteristic ·L1 p6

[def] These are called **static** characteristics because they describe the **d.c.** behaviour of the
diode. ·L1 p5

[fig ·L1 p6] **Fig. 52.4 — the full V/I characteristic. Learn to redraw this from memory.**

- **Axes.** Vertical up: current in **mA**, ticked 25, 50, 75. Horizontal right: **$+V$** in volts,
  ticked 1 and 2. Horizontal left: **$-V$** in volts, ticked 25, 50, 75, 100. Vertical down: reverse
  current, ticked 50, 100, 150, 200, with the unit printed at the bottom (see C1.5).
- **First quadrant — Forward Characteristic.** The curve leaves the origin flat, stays on the axis
  to roughly 0.6–0.7 V, then knees sharply upward and rises almost vertically, passing 75 mA a
  little past 1 V. Labelled **Forward Characteristic** and **Current due to Majority Carriers**.
- **Third quadrant — Reverse Characteristic.** From the origin the curve drops a hair below the axis
  to a small constant value marked $I_0$ and runs **flat and horizontal** leftward, all the way past
  $-75\ \mathrm{V}$. Labelled **Current due to Minority Carriers**.
- **Breakdown.** At about $-90\ \mathrm{V}$ the curve turns and plunges **vertically downward** off
  the bottom of the frame. Labelled **Break Down** with two arrows onto the knee, and **Reverse
  Characteristic**.
- **Two inset circuits.** Upper right: a diode in series with a battery $V$, current $I$ arrowed —
  the forward-bias measurement. Lower left: the same loop with the diode reversed and the current
  labelled $I_0$ — the reverse-bias measurement.
- Two large arrows label the axis senses: $-V$ to the left, $+V$ to the right, $i$ downward.

> ⚠ VERIFY **C1.5** ·L1 p6 — the bottom of the reverse-current axis in Fig. 52.4 is labelled
> **"200 A"**. The µ prefix has dropped: it is **200 µA**, as the same page's text
> ("nanoamperes for Si, microamperes for Ge") requires. Read literally, the figure claims a leakage
> current of 200 amperes. See `_verification-log.md`.

---

## 1.5 The diode equation ·L1 p6–p7 — **the section with three defects**

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I$ | diode current | A | mA range forward |
| $I_0$ (also $I_s$) | reverse saturation / leakage current | A | nA (Si), µA (Ge) |
| $V$ | voltage across the junction (+ forward, − reverse) | V | 0.2–0.7 |
| $\eta$ | ideality (emission) factor | — | 1 (Ge), 2 (Si) |
| $V_T$ | thermal voltage $kT/e = T/11{,}600$ | V | 25 mV at 293 K |

[def ·L1 p6] The handout calls the analytical description of the characteristic the **Boltzmann diode
equation**. *(It is more widely known as the Shockley diode equation — worth knowing if a textbook or
paper uses that name instead. [added])*

**As printed, highlighted, on p6:**

$$I = I_0\left(e^{\,eV/kT}-1\right)\ \text{ampere}\qquad\text{⚠ V1.2 — the } \eta \text{ is missing}$$

with, immediately below ·L1 p6:

- $I_0$ = diode reverse saturation current
- $V$ = voltage across the junction — **positive for forward bias, negative for reverse bias**
- $k$ = Boltzmann constant $=1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$
- $T$ = crystal temperature in K
- $\eta = 1$ for **germanium**, $\eta = 2$ for **silicon**

> ⚠ VERIFY **V1.2** ·L1 p6 — the highlighted master equation prints $I = I_0(e^{eV/kT}-1)$ with
> **no ideality factor**, and yet $\eta$ is defined three lines below it and appears in every
> subsequent form on p6 and p7. Correct general form:
> $$\boxed{\;I = I_0\left(e^{\,eV/\eta kT}-1\right) = I_0\left(e^{\,V/\eta V_T}-1\right)\;}$$
> **Why it matters numerically:** for **silicon** ($\eta = 2$) the printed box doubles the exponent.
> At $V = 0.2\ \mathrm{V}$, $V_T = 25\ \mathrm{mV}$: printed gives $e^{8} = 2981$, correct gives
> $e^{4} = 54.6$ — the current is out by a factor of **55**. The very next lines of the same page
> give the two special cases correctly, which is what confirms the box is the defective one.
> See `_verification-log.md`.

[eq: diode-equation] **The corrected master form — the one to carry into every question** ·L1 p6

$$\boxed{\;I = I_0\left(e^{\,V/\eta V_T}-1\right),\qquad V_T = \frac{kT}{e} = \frac{T}{11{,}600}\;}$$

[eq: diode-eta] The material-specific forms the page then prints ·L1 p6

$$I = I_0\left(e^{\,eV/kT}-1\right)\quad\text{— for germanium }(\eta=1)$$
$$I = I_0\left(e^{\,eV/2kT}-1\right)\quad\text{— for silicon }(\eta=2)$$

[eq] **The 11,600 shortcut** ·L1 p6

$$\frac{e}{k} = 11{,}600\ \mathrm{K\,V^{-1}},\qquad \boxed{\;V_T = \frac{T}{11{,}600}\;}$$

$$I = I_0\left(e^{\,11{,}600\,V/\eta T}-1\right) = I_0\left(e^{\,V/\eta V_T}-1\right)\ \text{ampere}$$

*[added] Verified: $1.6\times10^{-19}/1.38\times10^{-23} = 11{,}594 \approx 11{,}600$ ✓.*

At a room temperature of $(273+20) = 293\ \mathrm{K}$ ·L1 p6:

$$V_T = \frac{293}{11{,}600} = 0.025\ \mathrm{V} = 25\ \mathrm{mV}$$

*[added] Recomputed: $293/11{,}600 = 25.26\ \mathrm{mV}$ ✓.*

### The numerical forms ·L1 p7

Substituting $\eta$ and $V_T = 25\ \mathrm{mV}$, the page prints four highlighted lines:

$$I = I_0\left(e^{\,40V}-1\right)\ \text{— for Ge};\qquad \cong I_0\,e^{\,40V}\ \text{— if } V > 1\ \mathrm{volt}$$
$$I = I_0\left(e^{\,20V}-1\right)\ \text{— for Si};\qquad \cong I_0\,e^{\,20V}\ \text{— if } V > 1\ \mathrm{volt}$$

[eq: diode-40-20] and the general shorthand ·L1 p7

$$\boxed{\;I = I_0\left(e^{\,V_f/\eta V_T}-1\right)\ \text{forward bias},\qquad
I = I_0\left(e^{\,V_R/\eta V_T}-1\right)\ \text{reverse bias}\;}$$

*[added] Where 40 and 20 come from: $1/(\eta V_T)$ with $V_T = 25\ \mathrm{mV}$ gives $1/0.025 = 40$
for Ge and $1/(2\times0.025) = 20$ for Si. Both carry units of V⁻¹, so the exponent is
dimensionless ✓.*

> ⚠ VERIFY **V1.3** ·L1 p7 (and again p8) — **all four highlighted forms on p7 print the $-1$
> INSIDE the exponent**: $I_0(e^{40V-1})$, $I_0(e^{20V-1})$, $I_0(e^{V_f/\eta V_T-1})$,
> $I_0(e^{V_R/\eta V_T-1})$. The same slip recurs at the top of Example 52.2 ·L1 p8, printed
> $I = I_0\exp(eV/kT-1)$. The $-1$ belongs **outside** the bracket:
> $$\boxed{\;I = I_0\left(e^{\,V/\eta V_T}\right)-I_0 \;=\; I_0\left(e^{\,V/\eta V_T}-1\right)\;}$$
> **Three independent disproofs, any one of which settles it:**
> 1. **Zero bias.** As printed, $V=0$ gives $I = I_0e^{-1} = 0.368\,I_0 \neq 0$ — an unbiased diode
>    passing a third of its saturation current, from nothing.
> 2. **The next line contradicts it.** $I_0(e^{40V-1}) \cong I_0e^{40V}$ is only true if the $-1$ is
>    outside; inside, the two differ by the constant factor $e^{-1}$ at *every* voltage.
> 3. **The handout gets it right elsewhere.** Example 52.7 ·L1 p18 prints $I = I_0(e^{40V}-1)$, and
>    Example 52.2's own next step, $(I/I_0)+1 = \exp(eV/kT)$, only follows from the outside form.
>
> See `_verification-log.md`.

*[added] Two further notes on these forms.*

- *The condition "if $V > 1$ volt" is far stronger than needed. $e^{x}-1 \approx e^{x}$ to better
  than 1% once $x > 5$, i.e. once $V > 0.125\ \mathrm{V}$ for Ge. No real Ge diode ever sees 1 V
  forward — it would pass $I_0e^{40} \approx 2\times10^{17}I_0$ and be destroyed. Treat the
  approximation as valid for any $V$ more than a few tenths of a volt.*
- *In the reverse-bias form, $V_R$ must be substituted as a **negative** number. If $V_R$ is quoted
  as a magnitude, write $I = I_0(e^{-V_R/\eta V_T}-1) \to -I_0$ for $V_R$ of even a few hundred
  millivolts — which is exactly the "saturation at $I_0$" seen in Fig. 52.4.*

### [ex] Example 52.1 — voltage change to double the forward current ·L1 p8

**Statement.** Using the approximate Boltzmann diode equation, find the change in forward bias for
doubling the forward current of a germanium semiconductor at 290 K. *(Basic Electronics, Osmania
Univ. 1993)*

**Solution as printed** ·L1 p8

$$I_1 = I_0\exp\!\left(\frac{eV_1}{kT}\right),\qquad I_2 = I_0\exp\!\left(\frac{eV_2}{kT}\right)$$

$$\frac{I_2}{I_1} = \exp\!\left[\frac{e}{kT}(V_2-V_1)\right]$$

[eq: diode-current-ratio]

$$\boxed{\;V_2-V_1 = \frac{kT}{e}\,\ln\!\left(\frac{I_2}{I_1}\right) = 25\ln\!\left(\frac{I_2}{I_1}\right)\ \mathrm{mV}\;}$$

With $I_2 = 2I_1$:

$$V_2-V_1 = 25\ln 2 = 25\times0.693 = \mathbf{17.3\ mV}$$

*[added] Verified: $kT/e$ at 290 K $= 1.38\times10^{-23}\times290/1.6\times10^{-19} = 25.01\ \mathrm{mV}$ ✓ (which is why 25 mV is the right constant here, not 26); $25\times\ln2 = 17.33\ \mathrm{mV}$ ✓. $\eta = 1$ for Ge, so $\eta V_T = V_T$ and the ideality factor never appears — this
example would give **34.7 mV** for silicon.*

> **The result worth memorising.** For $\eta = 1$, every **doubling** of forward current costs
> $\approx 18\ \mathrm{mV}$, and every **decade** costs $V_T\ln 10 \approx 58\ \mathrm{mV}$. That is
> the "60 mV per decade" rule of thumb. [added]

### [ex] Example 52.2 — junction voltage at two temperatures ·L1 p8

**Statement.** A certain P-N junction diode has a leakage current of $10^{-14}\ \mathrm{A}$ at a room
temperature of 27 °C and $10^{-9}\ \mathrm{A}$ at 125 °C. The diode is forward-biased with a
constant-current source of 1 mA at room temperature. If the current is assumed to remain constant,
calculate the junction barrier voltage at room temperature and at 125 °C.

**Method as printed** ·L1 p8

$$\left(\frac{I}{I_0}\right)+1 = \exp\!\left(\frac{eV}{kT}\right)$$

[eq: diode-voltage-from-current] Taking logarithms and solving for $V$:

$$\boxed{\;V = \frac{kT}{e}\,\ln\!\left(\frac{I}{I_0}+1\right)\;}$$

**At 27 °C, i.e. 300 K** ·L1 p8

$$\frac{kT}{e} = \frac{1.38\times10^{-23}\times300}{1.6\times10^{-19}} = 26\ \mathrm{mV}$$

$$V_B = 26\ln\!\left(\frac{10^{-3}}{10^{-14}}+1\right) = 660\ \mathrm{mV} = \mathbf{0.66\ V}$$

*[added] Verified: $\ln(10^{11}) = 25.328$, $26\times25.328 = 658.5\ \mathrm{mV}$ ✓ — printed
660 mV, rounded.*

**At 125 °C, i.e. 398 K** — the page prints

$$\frac{kT}{e} = 1.38\times10^{-23}\times398\times(1.6\times10^{-19}) = 36\ \mathrm{mV}\qquad\text{⚠ V1.4, C1.6}$$

$$V_B = 36\ln\!\left(\frac{10^{-3}}{10^{-9}}+1\right) = 500\ \mathrm{mV} = \mathbf{0.5\ V}\qquad\text{⚠ V1.4}$$

> ### ⚠ VERIFY **V1.4** ·L1 p8 — $kT/e$ at 398 K is **34.3 mV**, not 36 mV, and the final answer is **0.47 V**, not 0.5 V
>
> $$\frac{kT}{e}\bigg|_{398\ \mathrm{K}} = \frac{1.38\times10^{-23}\times398}{1.6\times10^{-19}} = 34.33\ \mathrm{mV}$$
>
> **One-line check needing no calculator:** $kT/e$ is **linear in $T$**, and the same page has just
> computed 26 mV at 300 K. So the 398 K value must be $26\times398/300 = 34.5\ \mathrm{mV}$.
> 36 mV cannot be right.
>
> Propagating the correct constant:
> $$\boxed{\;V_B(125\,\text{°C}) = 34.33\times\ln(10^{6}+1) = 34.33\times13.8155 = 474\ \mathrm{mV} = 0.47\ \mathrm{V}\;}$$
>
> The printed 0.5 V is high by about 5%. See `_verification-log.md`.

> ⚠ VERIFY **C1.6** ·L1 p8 — the same line prints the division by $e$ as a **multiplication**:
> "$1.38\times10^{-23}\times398\times(1.6\times10^{-19})$". Evaluated as printed that is
> $8.8\times10^{-40}$, not a voltage at all. The 300 K line one row above uses "/" correctly. The
> closing bracket also has no opening partner. A second cosmetic slip sits four lines below: the
> final result is written "$36\,\mathbf{In}(\ldots)$" — a capital **I** where the **l** of $\ln$
> belongs. See `_verification-log.md`.

*[added] The example's physics, corrected and restated:* the forward voltage needed to sustain a
**fixed** 1 mA falls with temperature — from 0.66 V at 27 °C to **0.47 V** at 125 °C — because
$I_0$ has risen five decades. Both effects push the same way, which is why the drop is large
(≈ 190 mV over 98 °C, roughly $-1.9\ \mathrm{mV\,°C^{-1}}$ — recognisably the same $-2\ \mathrm{mV\,°C^{-1}}$ coefficient as §1.3).

### [ex] Example 52.7 — finding $I_0$ from a measurement ·L1 p18

**Statement.** A germanium diode draws 40 mA with a forward bias of 0.25 V. The junction is at a room
temperature of 293 K. Calculate the reverse saturation current of the diode.

**Solution as printed** ·L1 p18

$$I = I_0\left(e^{40V}-1\right)\quad\text{or}\quad 40\times10^{-3} = I_0\left(e^{40\times0.25}-1\right)$$

$$I_0 = \frac{40\times10^{3}}{22{,}027-1} = \mathbf{1.82\ \mu A}\qquad\text{⚠ V1.5}$$

> ⚠ VERIFY **V1.5** ·L1 p18 — the numerator is printed $40\times10^{\mathbf{3}}$; it must be
> $40\times10^{\mathbf{-3}}$, exactly as written on the line above. Correct form:
> $$\boxed{\;I_0 = \frac{40\times10^{-3}}{e^{10}-1} = \frac{0.04}{22{,}025.5} = 1.816\times10^{-6}\ \mathrm{A} = 1.82\ \mu\mathrm{A}\;}$$
> **The printed expression evaluates to 1.816 A** — a factor $10^{6}$ from the (correct) stated
> answer, and dimensionally absurd for a saturation current. Note the final answer is right; only
> the middle line is wrong, which is what makes it easy to copy into a CAT unnoticed.
> See `_verification-log.md`.

*[added] Verified: $e^{10} = 22{,}026.47$ (the page rounds to 22,027 here and to 22,026 in the very
next example — harmless but inconsistent); $0.04/22{,}025.5 = 1.816\ \mu\mathrm{A}$ ✓. Sanity check:
µA-scale leakage is the **germanium** order of magnitude quoted on p5 ✓ — a silicon answer should
have come out in nanoamperes.*

### [ex] Example 52.8 — how forward current and $I_0$ each respond to heat ·L1 p18

**Statement.** Calculate the forward current in a Ge diode at 20 °C when the forward voltage is
0.3 V. Compare this value with that after a temperature rise of 50 °C. Assume that the reverse
saturation current doubles for every 10 °C rise in temperature. *(Electronics-I, Mysore Univ. 1991)*

**Solution as printed** ·L1 p18

At 20 °C ($V_T = 25\ \mathrm{mV}$, $\eta = 1$, so the multiplier is 40):

$$I_{20} = I_0\left(e^{40V}-1\right) = I_0\left(e^{40\times0.3}-1\right) = I_0\left(e^{12}-1\right) = 162{,}755\,I_0$$

At $t = 20+50 = 70$ °C, i.e. $T = 343\ \mathrm{K}$:

$$V_T = \frac{343}{11{,}600} = 0.0296\ \mathrm{V} \cong 0.03\ \mathrm{V},\qquad
\frac{V}{\eta V_T} = \frac{0.3}{1\times0.03} = 10$$

[eq: io-temperature] $I_0$ doubles every 10 °C, so a 50 °C rise is **five** doublings:

$$\boxed{\;I_0' = 2^{5}I_0 = 32\,I_0\;}$$

$$I_{70} = I_0'\left(e^{10}-1\right) = 32\,I_0\,(22{,}026-1) = 704{,}800\,I_0$$

$$\frac{I_{70}}{I_{20}} = \frac{704{,}800}{162{,}755} = \mathbf{4.3}$$

**Conclusion as the page states it:** the forward current has increased only **4.3 times**, whereas
$I_0$ has increased **32 times**, for the same rise in temperature.

*[added] Every step verified:*

| Step | Working | Result |
|---|---|---|
| $e^{12}$ | — | $162{,}754.8$; $e^{12}-1 = 162{,}753.8$ *(page: 162,755 — rounded up, 0.001% high)* |
| $V_T(343\ \mathrm{K})$ | $343/11{,}600$ | $0.02957\ \mathrm{V}$ ✓ |
| exponent | $0.3/0.02957$ | $10.15$, rounded to 10 ✓ |
| $32(e^{10}-1)$ | $32\times22{,}025.5$ | $704{,}816\,I_0$ *(page: 704,800)* ✓ |
| ratio | $704{,}816/162{,}754$ | $4.331$ ✓ |

*The point of the example — and the reason it is a favourite exam question — is the **competition
between two temperature effects**: $I_0$ multiplies by 32, but the exponent shrinks from 12 to 10
because $V_T$ grows with $T$, dividing the exponential by $e^{2} = 7.4$. Net effect
$32/7.4 = 4.3$ ✓. Neither effect alone gives the answer.*

---

## 1.6 Diode parameters ·L1 p7

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $r_B$ | bulk resistance | Ω | a few Ω |
| $r_P,\ r_N$ | resistance of the P and N regions | Ω | — |
| $r_j$ | junction resistance | Ω | 25 Ω at 1 mA (Ge) |
| $r_{ac}$ (also $r_d$) | dynamic / ac resistance | Ω | — |
| $R_R$ | reverse dc resistance | Ω | MΩ range |
| $V_F,\ I_F$ | forward voltage, forward current | V, A | 0.7 V, mA |

**1. Bulk resistance** ·L1 p7 — the sum of the resistances of the P- and N-type material the diode
is made of. Usually very small, and offered in the **forward** direction only.

[eq: bulk-resistance]

$$\boxed{\;r_B = r_P + r_N = \frac{V_F - V_B}{I_F}\;}$$

It is the resistance the diode offers **well above the barrier voltage**, i.e. when the current is
large.

**2. Junction resistance** ·L1 p7 — its value for a forward-biased junction depends on the magnitude
of the forward **dc** current. It is a **variable** resistance.

[eq: junction-resistance]

$$\boxed{\;r_j = \frac{25\ \mathrm{mV}}{I_F(\mathrm{mA})}\ \text{— for Ge},\qquad
r_j = \frac{50\ \mathrm{mV}}{I_F(\mathrm{mA})}\ \text{— for Si}\;}$$

*[added] Both are the one relation $r_j = \eta V_T/I_F$ with $V_T = 25\ \mathrm{mV}$: $\eta = 1$ gives
25 mV, $\eta = 2$ gives 50 mV. Units check: $\mathrm{mV/mA} = \Omega$ ✓. It follows directly from
differentiating the diode equation — $r_j = dV/dI = \eta V_T/I$ — which is why it is called the
**dynamic** junction resistance.*

**3. Dynamic or ac resistance** ·L1 p7

[eq: ac-resistance]

$$\boxed{\;r_{ac} = r_d = r_B + r_j\;}$$

- For **large** forward current, $r_j$ is negligible, hence $r_{ac} \approx r_B$.
- For **small** forward current, $r_B$ is negligible compared with $r_j$, hence $r_{ac} \approx r_j$.

**4. Forward voltage drop** ·L1 p7

[eq: forward-drop]

$$\boxed{\;\text{forward voltage drop} = \frac{\text{power dissipated}}{\text{forward dc current}}\;}$$

*[added] Dimensionally $\mathrm{W/A} = \mathrm{V}$ ✓.*

**5. Reverse saturation current $I_0$** — already covered in §1.4. ·L1 p7

**6. Reverse breakdown voltage $V_{BR}$** — covered under the Zener diode, §1.9. ·L1 p7

**7. Reverse dc resistance** ·L1 p7

[eq: reverse-dc-resistance]

$$\boxed{\;R_R = \frac{\text{reverse voltage}}{\text{reverse current}}\;}$$

[fig ·L1 p7] **Fig. 52.5 — where the resistances live, two panels.**

- **(a)** Upper: a rectangle split into a **P** half and an **N** half, each containing a resistor
  symbol — $r_p$ in the P half, $r_N$ in the N half — wired in series between two terminals. Lower:
  the equivalent single resistor labelled $r_B$.
- **(b)** Upper: the same P|N rectangle, but with a **variable-resistor arrow** drawn across the
  junction boundary and labelled $r_j$, with $r_p$ in the P half and $r_N$ in the N half. Lower: the
  series equivalent — a variable resistor $r_j$ followed by a fixed resistor $r_B$.

*[added] Note the case slip between text and figure: the text writes $r_P$ (capital) and the figure
$r_p$ (lower case) for the same quantity.*

---

## 1.7 Applications of the junction diode ·L1 p7–p8

The handout lists five ·L1 p7–p8:

1. **Power or rectifier diodes** — converting ac to dc for dc power supplies.
2. **Signal diodes** — modulation and demodulation of small signals in communication circuits.
3. **Zener diodes** — voltage stabilising circuits.
4. **Varactor diodes** — voltage-controlled tuning circuits in radio and TV receivers. The diode is
   deliberately made to have a certain range of junction capacitance.
5. **Logic circuits** used in computers.

[eq: varactor-capacitance] The capacitance of the reverse-biased diode ·L1 p7

$$\boxed{\;C = \frac{K}{\sqrt{V_R}}\;}$$

- $C$ — junction capacitance, F · $K$ — a constant fixed by geometry and doping, F·V$^{1/2}$ ·
  $V_R$ — reverse voltage, V

*[added] Why the square root: reverse bias widens the depletion layer as $\sqrt{V_R}$ for an abrupt
junction, and the junction behaves as a parallel-plate capacitor whose plate separation is that
width, so $C \propto 1/\sqrt{V_R}$. Increasing the reverse voltage therefore **lowers** the
capacitance — which is how a varactor tunes a resonant circuit.*

---

## 1.8 The Zener diode ·L1 p8–p10

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_z$ | Zener breakdown voltage | V | 2.4–200 |
| $I_z$ | Zener current | A | mA range |
| $I_{z\,\min}$ | minimum current to sustain breakdown | A | — |
| $I_{z\,\max}$ | maximum Zener current, set by power dissipation | A | — |
| $Z_z$ | Zener dynamic impedance | Ω | small |
| $P_{\max}$ | maximum power dissipation | W | 150 mW – 50 W |

[def ·L1 p8] A **Zener diode** is a reverse-biased, **heavily doped** silicon (or germanium) P-N
junction diode operated in the **breakdown region**, where the current is limited by both the
external resistance and the power dissipation of the diode. **Silicon is preferred to germanium**
because of its higher temperature and current capability.

### The two breakdown mechanisms ·L1 p8

When a diode breaks down, **both** Zener and avalanche effects are present, but one usually
predominates depending on the reverse voltage:

| Reverse voltage | Dominant mechanism | Strictly called |
|---|---|---|
| **less than 6 V** | Zener effect | Zener diode |
| **above 6 V** | avalanche effect | avalanche diode |

General practice is to call **both** types Zener diodes. ·L1 p8

[def ·L1 p8] **Zener breakdown** occurs by the **breaking of covalent bonds by the strong electric
field** set up in the depletion region by the reverse voltage. It produces an extremely large number
of electrons and holes, which constitute the reverse saturation current — now called the **Zener
current $I_z$** — whose value is limited **only by the external resistance in the circuit**. It is
**independent of the applied voltage**.

[def ·L1 p8] **Avalanche breakdown** occurs at higher reverse voltages, when thermally-generated
electrons acquire enough energy to produce more carriers **by collision**.

### (a) V/I characteristic ·L1 p9

[fig ·L1 p9] **Fig. 54.1 — the Zener characteristic. The whole of Zener operation is in this
figure.**

- Axes: $I_F$ upward, $V_F$ to the right; the action is in the **third quadrant** (negative $V$,
  negative $I$) — the handout calls it "the negative quadrant".
- **Forward branch:** a dashed curve in the first quadrant hugging the $V_F$ axis then rising
  steeply — "simply that of an ordinary forward-biased junction diode".
- **Reverse branch:** from the origin the curve runs **flat and just below the horizontal axis**
  leftward at a tiny leakage current, then at $-V_Z$ it **turns and drops almost vertically**.
- $V_Z$ is labelled on the negative-$V$ axis, with a dashed vertical line dropping from it.
- Two dashed horizontal lines cut the vertical part of the curve: the upper marks
  $\mathbf{I_{Z\ min.}}$, the lower marks $\mathbf{I_{Z\ max.}}$. A downward arrow between them is
  labelled $I_Z$ — the usable operating band.

Three points define the reverse characteristic ·L1 p9:

- $V_z$ = Zener breakdown voltage
- $I_{z\,\min}$ = minimum current to **sustain** breakdown
- $I_{z\,\max}$ = maximum Zener current, **limited by maximum power dissipation**

[def ·L1 p9] Because the reverse characteristic is not *exactly* vertical, the diode has some
resistance, called the **Zener dynamic impedance**. The handout **neglects it**, assuming an
**ideal Zener diode** for which the voltage **does not change once it goes into breakdown**: $V_z$
stays constant even when $I_z$ increases considerably. *All the worked examples in §1.10–§1.11 use
this ideal assumption.*

### The symbol and the equivalent circuits ·L1 p9–p10

[def ·L1 p9] The schematic symbol is that of a normal diode except that **the cathode line is bent at
both ends**, so that with a little imagination the cathode looks like the letter **Z** for Zener.

[fig ·L1 p10] **Fig. 54.2 — symbol and equivalent circuits, four panels, drawn vertically with
Cathode at the top and Anode at the bottom.**

- **(a)** The schematic **symbol**: the triangle pointing up to a horizontal bar whose two ends are
  bent, cathode above, anode below.
- **(b)** The **complete equivalent circuit**: from cathode down, a resistor labelled $Z_z$ (the
  Zener dynamic impedance) in **series** with a battery labelled $V_z$, then the anode.
- **(c)** The **approximate equivalent circuit**: just the battery $V_z$ between cathode and anode —
  "it looks like a battery of $V_z$ volts".
- **(d)** A photograph of a physical zener diode — a small cylindrical glass-bodied component with
  colour bands and axial leads. The text identifies it as a $V_z = 4.7\ \mathrm{V}$ device.

### (b) Zener voltages ·L1 p9

- Available with Zener voltages from **2.4 V to 200 V**.
- The voltage is **temperature dependent**.
- Power dissipation is the product $V_z I_z$; maximum ratings run from **150 mW to 50 W**.

### (c) Zener biasing — the three-point check ·L1 p9–p10

For proper working of a Zener diode in any circuit it **must**:

1. be **reverse-biased**;
2. have a voltage across it **greater than $V_z$**;
3. be in a circuit where the current is **less than $I_{z\,\max}$**.

> **This checklist is the marking scheme for Examples 54.1–54.3.** Each of those questions is exactly
> "which of the three conditions fails?". [added]

### (d) Diode identification ·L1 p10

Physically a Zener diode looks like any other diode and is recognised by its part number, such as
"IN 750" (quoted as 10 W) or "IN 4000" (high power). Fig. 54.2(d) shows a Zener with
$V_z = 4.7\ \mathrm{V}$.

> ⚠ VERIFY **C1.8** ·L1 p10 — printed **"IN 750"** and **"IN 4000"**. The JEDEC part prefix is the
> **digit one** followed by N: **1N750**, **1N4000**-series. Reading it as the letter I makes the
> part unsearchable in any catalogue. *Caution, unverified against a datasheet here: the standard
> 1N750 is a 4.7 V, ~0.5 W device — consistent with the 4.7 V quoted two lines later, but not with
> the bracketed "(10 W power)". Treat that power figure with suspicion.*
> See `_verification-log.md`.

### (e) Uses ·L1 p10

1. as **voltage regulators**;
2. as a **fixed reference voltage** in a network, for biasing and comparison purposes and for
   calibrating voltmeters;
3. as **peak clippers** or **voltage limiters**;
4. for **meter protection** against damage from accidental application of excessive voltage;
5. for **reshaping a waveform**.

---

## 1.9 Zener biasing — worked examples ·L1 p10–p11

### [ex] Example 54.1 — a Zener that is biased but not broken down ·L1 p10

[fig ·L1 p10] **Fig. 54.3.** A single loop: a **6 V** battery on the left; from its positive terminal
the top rail runs right to a resistor $R = 500\ \Omega$ drawn vertically on the right-hand side; below
it a Zener with $V_Z = 10\ \mathrm{V}$, cathode uppermost; the bottom rail returns to the battery.
Annotation: $I_{Z\ \max} = 6\ \mathrm{mA}$.

**Statement.** Determine whether the ideal Zener diode of Fig. 54.3 is properly biased. Explain why.

**Solution as printed** ·L1 p10

- The **positive** battery terminal is connected to its **cathode**, so the diode is **reverse-biased**
  — condition 1 ✓.
- The applied voltage (6 V) is **less than $V_z$** (10 V), so the diode is **not properly
  voltage-biased** — condition 2 ✗.

*[added] Consequence: with no breakdown the Zener is an open circuit, so no current flows and the
whole 6 V appears across the diode. The circuit does nothing.*

### [ex] Example 54.2 — a correctly biased Zener ·L1 p10

[fig ·L1 p10] **Fig. 54.4.** Identical topology to Fig. 54.3 but with a **12 V** source;
$R = 500\ \Omega$; $V_Z = 10\ \mathrm{V}$; $I_{Z\ \max} = 6\ \mathrm{mA}$; the loop current $I$ is
arrowed along the top rail.

**Statement.** Find out if the Zener diode of Fig. 54.4 is properly biased. If so, find the diode
current assuming it to be an ideal one.

**Solution as printed** ·L1 p10

- Polarity-wise the diode is properly biased ✓, and the applied voltage exceeds $V_z$ ✓.

$$\text{drop across } R = 12-10 = 2\ \mathrm{V}\qquad\Longrightarrow\qquad
I = \frac{2}{500} = \mathbf{4\ mA}$$

- $4\ \mathrm{mA} < I_{z\,\max} = 6\ \mathrm{mA}$ ✓ — all three criteria of Art. 54.1(c) are met.

*[added] Verified: $2/500 = 4\ \mathrm{mA}$ ✓. Power in the diode $= 10\times4 = 40\ \mathrm{mW}$;
power in $R = 2\times4 = 8\ \mathrm{mW}$.*

### [ex] Example 54.3 — Zener with a parallel load ·L1 p10

[fig ·L1 p10] **Fig. 54.5.** An **18 V** battery on the left. The top rail carries current $I$ to the
right and turns down through $R_1 = 600\ \Omega$ to node **A**. From A, two parallel branches drop to
the bottom rail **B**: $R_2 = 1800\ \Omega$ carrying $I_1$ (arrow down), and a Zener
$V_Z = 12\ \mathrm{V}$, $I_{Z\ \max} = 6\ \mathrm{mA}$, carrying $I_Z$ (arrow right then down),
cathode uppermost.

**Statement.** Determine if the Zener diode of Fig. 54.5 is biased properly. If so, find $I_z$ and
the power dissipated by the diode.

**Solution as printed** ·L1 p10

Its anode is connected to the negative battery terminal, so it is correctly reverse-biased ✓.

$$V_{AB} = V_Z = 12\ \mathrm{V}\qquad\Longrightarrow\qquad \text{drop across } R_1 = 18-12 = 6\ \mathrm{V}$$
$$I = \frac{6}{600} = 0.01\ \mathrm{A} = 10\ \mathrm{mA}$$
$$I_1 = \frac{12}{1800} = 6.7\times10^{-3}\ \mathrm{A} = 6.7\ \mathrm{mA}$$
$$I_z = I - I_1 = 10-6.7 = 3.3\ \mathrm{mA}$$

$I_z < I_{z\,\max}$ ✓, so the diode is properly biased in every respect.

$$\text{Power dissipated} = V_z I_z = 12\times3.3 = \mathbf{39.6\ mW}$$

*[added] Recomputed exactly: $I_1 = 12/1800 = 6.667\ \mathrm{mA}$, so $I_z = 3.333\ \mathrm{mA}$ and
$P = 12\times3.333 = \mathbf{40.0\ mW}$. The printed 39.6 mW comes from carrying the rounded 3.3 mA
into the last step — a 1% rounding artefact, not an error. **Carry full precision to the last line
and round once.***

*[added] The structure worth extracting: this is the shunt-regulator topology of §1.11 in disguise.
$R_1$ is the series resistor, $R_2$ is the load, $I = I_z + I_L$ is the node equation, and the Zener
absorbs whatever the load does not take.*

### [ex] The un-numbered example — a **series** Zener ·L1 p10–p11

[fig ·L1 p11] **Fig. 54.6.** Input terminals on the left across which $E_{in}$ is marked
(arrow up). The top rail runs right through a **series 10 V Zener** — the symbol drawn with its
**cathode toward the input** — to a node; from that node a **100 Ω** resistor drops to the bottom
rail; output terminals on the right, across which $E_o$ is marked. The 100 Ω resistor is thus in
parallel with the output.

**Solution as printed** ·L1 p11 — *the question statement itself is missing (C1.7).*

- **When $E_{in} = 6\ \mathrm{V}$:** the diode acts like an **open circuit**, because 6 V is not
  enough to cause Zener breakdown, which needs $E_{in}$ to exceed 10 V. Hence
  $$E_0 = \mathbf{0}$$
- **When $E_{in} = 20\ \mathrm{V}$:** breakdown occurs but the voltage across the diode remains
  constant at 10 V. The balance $(20-10) = 10\ \mathrm{V}$ appears across the 100 Ω resistor. Hence
  $$E_0 = \text{drop across } R = \mathbf{10\ V}$$

> ⚠ VERIFY **C1.7** ·L1 p10–p11 — **the statement of this example is absent.** The solution opens
> p11 with no question above it, and the example numbering jumps from **54.3** (p10) to **54.5**
> (p12), so **Example 54.4's question text is missing** from the compilation. The solution can be
> reconstructed (it evidently asks for $E_o$ in Fig. 54.6 when $E_{in}$ is 6 V and 20 V) but the page
> cannot be followed as printed. See `_verification-log.md`.

*[added] Verified and worth noting: this is a **series** Zener, not the shunt regulator of §1.11.
With $E_{in} = 20\ \mathrm{V}$ the loop current is $10/100 = 100\ \mathrm{mA}$, which dissipates
$10\times0.1 = 1\ \mathrm{W}$ in the diode — well above the 150 mW low end of the rating range quoted
on p9. The circuit is a **level shifter / threshold detector**, not a regulator: it subtracts a fixed
10 V from anything above 10 V and outputs zero below it.*

> ⚠ VERIFY **C1.9** ·L1 p11 — the first line of §54.2 ("It is a measure of a circuit's ability to
> maintain a constant output") is printed **twice, overlapping**, one copy laid over a fainter copy;
> the "Fig. 54.6" caption is doubled the same way. A compilation artefact — retyped text placed over
> the scan. Nothing computed changes. See `_verification-log.md`.

---

## 1.10 Zener voltage regulation ·L1 p11–p13

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{in}$ ($E_{in}$) | unregulated input voltage | V | 32–70 |
| $V_{out}$ ($E_o$) | regulated output voltage $=V_z$ | V | 10–30 |
| $R$ | series (line) resistance | Ω | 0.3–3 kΩ |
| $R_L$ | load resistance | Ω | 1.2–30 kΩ |
| $I$ | total current through $R$ | A | mA |
| $I_L$ | load current | A | mA |
| $I_z$ | Zener current | A | mA |

[def ·L1 p11] **Voltage regulation** is a measure of a circuit's ability to maintain a constant
output voltage even when **either the input voltage or the load current varies**. A Zener diode
working in the breakdown region can serve as a voltage regulator.

[fig ·L1 p11] **Fig. 54.7 — the shunt regulator. The one circuit to be able to draw from memory.**

- Input terminals on the left, $V_{in}$ marked with $+$ at the top.
- From the $+$ terminal, current $I$ (arrowed) flows right through the **series resistor $R$** to a
  node.
- From that node a **Zener** drops to the bottom rail, **cathode uppermost** (reverse-connected),
  carrying $I_Z$ (arrow down), labelled $V_Z$.
- To the right of the node, current $I_L$ (arrowed) flows to the **load $R_L$**, drawn as a vertical
  rectangle labelled **Load**, also across the bottom rail.
- $V_{out}$ is marked across the load on the far right.

### The governing relations ·L1 p11

The Zener is reverse-connected across $V_{in}$; when the p.d. across it exceeds $V_z$ it conducts and
draws a relatively large current through $R$. The load, across which the constant voltage is
required, sits in **parallel with the diode**.

[eq: zener-node] Node and loop equations:

$$\boxed{\;I = I_z + I_L,\qquad V_{out} = V_z,\qquad V_{in} = IR + V_{out} = IR + V_z\;}$$

**Case 1 — $R_L$ fixed, $V_{in}$ varies** ·L1 p11

- $V_{in}$ up ⟹ $I$ up. The **increase in $I$ is absorbed by the Zener**, without affecting $I_L$.
- The increase in $V_{in}$ is dropped across $R$, keeping $V_{out}$ constant.
- Conversely, $V_{in}$ down ⟹ the diode takes a smaller current, the drop across $R$ reduces, and
  $V_{out}$ is again held constant.
- In short: when $V_{in}$ changes, $I$ and the $IR$ drop change in just the way that keeps
  $V_{out}(=V_z)$ constant.

**Case 2 — $V_{in}$ fixed, load varies** ·L1 p11

- $I_L$ up ⟹ $I_z$ **down**, keeping $I$ and hence the $IR$ drop constant, so $V_{out}$ is unaffected.
- $I_L$ down ⟹ $I_z$ **up**, for the same reason.

$$V_{out} = V_{in} - IR = V_{in} - (I_z + I_L)R$$

[eq: zener-series-r] Rearranged for design:

$$\boxed{\;R = \frac{V_{in}-V_{out}}{I_z + I_L}\;}$$

[eq: zener-series-r-max] The worst case is **no load**, when the diode carries everything ·L1 p11:

$$\boxed{\;R = \frac{V_{in}-V_{out}}{I_{Z\max}}\;}\qquad\text{(when } I_L = 0 \text{)}$$

*[added] Read that as the **design rule**: size $R$ so that with the load disconnected and the input
at its highest, the Zener still does not exceed $I_{z\max}$. Everything the load then draws is
current the diode does **not** have to absorb, so the diode is always safe.*

### Two reference levels ·L1 p11–p12

In Fig. 54.7 only **one** reference level is available. Two Zeners of different $V_z$ connected in
**series** provide two. ·L1 p11

[fig ·L1 p12] **Fig. 54.8.** A **50 V** battery on the left; $R$ in series along the top rail to a
node; from the node a series chain drops to the bottom rail — an upper Zener $V_Z = 10\ \mathrm{V}$
then a lower Zener $V_Z = 20\ \mathrm{V}$, both cathode-uppermost. Three terminals are brought out on
the right: the **top node** marked $+$, the **mid-point tap** between the two diodes (marked $-$ on
its upper side and $+$ on its lower side), and the **bottom rail** marked $-$ and grounded.

*[added] The two levels are therefore **30 V** (top terminal to ground, the two Zeners in series) and
**20 V** (mid tap to ground, the lower Zener alone); the drop across the upper diode alone is 10 V.
The mid tap serves as the negative terminal of the upper reference and the positive terminal of the
lower one, which is what the two polarity marks in the figure are saying.*

### [ex] Example 54.5 — regulator with a varying input ·L1 p12

[fig ·L1 p12] **Fig. 54.9.** A variable **40–70 V** source on the left; series **3 K** resistor along
the top rail carrying $I$ to node **A**; from A a Zener $V_Z = 10\ \mathrm{V}$,
$P_{\max} = 0.5\ \mathrm{W}$ drops to the bottom rail **B**, carrying $I_Z$; also from A, $I_L$ flows
right into $R_L = 2\ \mathrm{K}$, also across to B.

**Statement.** Calculate the battery current $I$, $I_z$ and $I_L$ in the circuit of Fig. 54.9. How
will these values be affected if the source voltage increases to 70 V? Neglect Zener resistance.
*(Industrial Electronics, Pune Univ.)*

**(a) When $V_{in} = 40\ \mathrm{V}$** ·L1 p12

$$V_{AB} = V_z = 10\ \mathrm{V}$$
$$\text{drop across the 3 K line resistor} = 40-10 = 30\ \mathrm{V}$$
$$I = \frac{30}{3\ \mathrm{k\Omega}} = \mathbf{10\ mA}$$
$$I_L = \frac{V_z}{R_L} = \frac{V_{AB}}{R_L} = \frac{10}{2\ \mathrm{k\Omega}} = \mathbf{5\ mA}$$
$$I_z = I - I_L = 10-5 = \mathbf{5\ mA}$$

[eq: zener-power] The rating check ·L1 p12:

$$\boxed{\;P_{\max} = V_z I_{z(\max)}\;}\qquad 0.5 = 10\times I_{z(\max)}
\qquad\Longrightarrow\qquad I_{z(\max)} = \frac{0.5}{10} = 0.05\ \mathrm{A} = \mathbf{50\ mA}$$

A diode current of 5 mA is "very much within the current range of the diode" ✓.

**(b) When $V_{in} = 70\ \mathrm{V}$** ·L1 p12

$$\text{drop across } R = 70-10 = 60\ \mathrm{V}\qquad\Longrightarrow\qquad I = \frac{60}{3\ \mathrm{k\Omega}} = \mathbf{20\ mA}$$
$$I_L = \mathbf{5\ mA}\ \text{(as before)},\qquad I_z = I - I_L = 20-5 = \mathbf{15\ mA}$$

*[added] All six numbers verified ✓. The teaching point is in the pattern: **$I_L$ did not move** —
the whole $75\%$ increase in input voltage was absorbed by the Zener ($5 \to 15\ \mathrm{mA}$). That
is regulation. Headroom check: even at 70 V, $I_z = 15\ \mathrm{mA} \ll 50\ \mathrm{mA}$ ✓; the input
could rise to $10 + 3\mathrm{k}\times(50+5)\mathrm{mA} = 175\ \mathrm{V}$ before the diode is at
risk.*

*[added] Presentation note: the page prints the result "$I = 30/3\ \mathrm{K} = 10\ \mathrm{mA}$"
**one line above** the line that establishes the 30 V drop it depends on. The logical order is the
one used here.*

### [ex] Example 54.6 — regulator with a varying load ·L1 p12–p13

[fig ·L1 p13] **Fig. 54.10.** A **60 V** source; $R = 3\ \mathrm{K}$ in series along the top rail,
carrying $I$ to node **A**; a Zener $V_Z = 30\ \mathrm{V}$ from A down to rail **B**, carrying $I_Z$;
a **variable** load $R_L = 3\text{–}30\ \mathrm{K}$ (drawn as a resistor with an arrow through it)
from A to B, carrying $I_L$.

**Statement.** Using the ideal Zener approximation, find the current through the diode of Fig. 54.10
when the load resistance $R_L$ is (i) 30 K (ii) 5 K (iii) 3 K. *(Electronics, Madurai Kamraj Univ.)*

**Common to all three parts** ·L1 p12

$$V_{AB} = V_z = 30\ \mathrm{V},\qquad \text{drop across } R = 60-30 = 30\ \mathrm{V},
\qquad I = \frac{30}{3\ \mathrm{k\Omega}} = 10\ \mathrm{mA}$$

| Part | $R_L$ | $I_L = V_{AB}/R_L$ | $I_z = I - I_L$ |
|---|---|---|---|
| (i) | 30 K | $30/30\ \mathrm{k} = 1\ \mathrm{mA}$ | $10-1 = \mathbf{9\ mA}$ |
| (ii) | 5 K | $30/5\ \mathrm{k} = 6\ \mathrm{mA}$ | $10-6 = \mathbf{4\ mA}$ |
| (iii) | 3 K | $30/3\ \mathrm{k} = 10\ \mathrm{mA}$ | $10-10 = \mathbf{0}$ |

At $R_L = 3\ \mathrm{K}$ the diode is **just on the verge of coming out of the breakdown region**. If
$R_L$ is reduced further, the diode comes out of breakdown and **no longer acts as a voltage
regulator**. ·L1 p12

*[added] All nine numbers verified ✓. Note that $I$ is the **same 10 mA in all three parts** — with
$V_{in}$ and $V_z$ both fixed, the current through $R$ cannot change. The Zener simply mops up the
difference, and the regulator dies exactly when there is no difference left to mop up. The condition
is $R_{L(\min)} = R\,V_z/(V_{in}-V_z) = 3\mathrm{k}\times30/30 = 3\ \mathrm{k\Omega}$ ✓ — a useful
general formula.*

### [ex] Example 54.7 — designing the series resistor ·L1 p13

[fig ·L1 p13] **Fig. 54.11.** A **32 V** source on the left; **$R$** in series along the top rail; a
Zener $V_Z = 24\ \mathrm{V}$, $P_{\max} = 0.6\ \mathrm{W}$ from the node down to the bottom rail,
current arrowed downward into it; a variable load $R_L$ (resistor with an arrow) in parallel to its
right.

**Statement.** A 24 V, 600 mW Zener diode is to be used for providing a 24 V stabilized supply to a
variable load (Fig. 54.11). If the input voltage is 32 V, calculate (i) the series resistance $R$
required (ii) the diode current when $R_L = 1200\ \Omega$. *(Applied Electronics, Punjab Univ. 1991)*

**(i) The series resistance** ·L1 p13

$$V_z I_{z(\max)} = 600\ \mathrm{mW}\qquad\Longrightarrow\qquad I_{z(\max)} = \frac{600}{24} = 25\ \mathrm{mA}$$

$$R = \frac{V_{in}-V_{out}}{I_{z(\max)}} = \frac{32-24}{25\times10^{-3}} = \mathbf{320\ \Omega}$$

**(ii) The diode current at $R_L = 1200\ \Omega$** ·L1 p13

$$I_L = \frac{V_z}{R_L} = \frac{24}{1200} = 20\ \mathrm{mA},\qquad
I_z = 25-20 = \mathbf{5\ mA}$$

*[added] All verified ✓: $600/24 = 25\ \mathrm{mA}$; $8/0.025 = 320\ \Omega$; $24/1200 = 20\ \mathrm{mA}$; $25-20 = 5\ \mathrm{mA}$. Note **why part (i) uses $I_{z\max}$**: $R$ is sized for
the **no-load** worst case (the design rule of §1.10), so the total current through $R$ is fixed at
25 mA whatever the load does. Part (ii) then just splits that 25 mA between load and diode. Power
check: $P_R = 8\ \mathrm{V}\times25\ \mathrm{mA} = 200\ \mathrm{mW}$, so a quarter-watt resistor is
marginal — a half-watt part should be specified. [added]*

---

## 1.11 The light-emitting diode ·L1 p13–p16

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_F$ | forward current through the LED | A | 20 mA |
| $V_F$ | forward voltage across the LED | V | 1.2–3.3 |
| $V_{bias}$ | supply voltage in the drive circuit | V | 5 |
| $R$ | series current-limiting resistor | Ω | — |

### (a) Theory ·L1 p13

[def ·L1 p13] An **LED** is a **forward-biased P-N junction which emits visible light when
energised**.

[derivation] The mechanism ·L1 p13:

1. Charge-carrier **recombination** takes place when electrons from the N-side cross the junction and
   recombine with holes on the P-side.
2. Electrons sit in the **higher conduction band** on the N-side; holes sit in the **lower valence
   band** on the P-side.
3. During recombination some of the **energy difference** is given up as **heat** and as **light**
   (photons).
4. For **Si and Ge** junctions the greater percentage goes to **heat**, so the light emitted is
   insignificant.
5. For **GaAs**, **GaP** and **GaAsP**, a greater percentage of the released energy comes out as
   **light**.
6. If the semiconductor is **translucent**, the light escapes and the junction becomes a light
   source — an LED.

[fig ·L1 p13] **Fig. 53.1 — three panels.** *(left)* A P|N block with leads returning to a battery,
i.e. the junction forward-biased. *(centre)* The same circuit with the block replaced by the **LED
schematic symbol** — the diode triangle-and-bar with **two arrows pointing away** from it,
representing emitted light. *(right)* The symbol alone as a two-terminal device, $+$ on the anode
side, $-$ on the cathode side, with the two emission arrows.

[fig ·L1 p13] **Photograph, lower left, captioned "Light emitting diode".** A cut-away of the die: a
horizontal layered sandwich with a thin upper layer labelled **p** and a lower layer labelled **n**;
open circles in the p layer and filled circles in the n layer with arrows converging on the junction;
wavy red arrows leave the top surface, labelled **Light Emission**. The right-hand contact goes to a
$+$ terminal with the current $I$ arrowed, and the lower contact goes through a series resistor $R$
to a $-$ terminal. Coloured panels at the left of the frame depict the two carrier populations.

### The materials table ·L1 p14

[table ·L1 p14]

| Material | Light emitted |
|---|---|
| **GaAs** (gallium arsenide) | infrared radiation (**invisible**) |
| **GaP** (gallium phosphide) | red or green |
| **GaAsP** (gallium arsenide phosphide) | red or yellow (amber) |

- **Blue** LEDs are also available, but **red is the most common**.
- LEDs emit **no light when reverse-biased**; in fact operating them in the reverse direction will
  **quickly destroy them**.

[fig ·L1 p14] **LED package drawing, top right.** A bullet-shaped red LED body seen from the side,
with two leads emerging left: the upper, longer one labelled **a** (anode) and the lower, shorter one
labelled **k** (cathode). An arrow points to a **Flat** on the rim of the package body — the
moulded flat that identifies the cathode side.

### (b) Construction ·L1 p14

[def ·L1 p14] Two categories of LED structure:

1. **Surface-emitting LEDs** — emit light in a direction **perpendicular** to the PN junction plane.
2. **Edge-emitting LEDs** — emit light in a direction **parallel** to the PN junction plane.

The construction of a **surface-emitting** LED ·L1 p14:

- An **N-type layer is grown on a substrate** and a **P-type layer deposited on it by diffusion**.
- Since carrier recombination takes place in the **P-layer**, that layer is kept **uppermost**.
- The metal **anode connections are made at the outer edges of the P-layer**, so as to leave the
  central surface area free for light to escape.
- LEDs are manufactured with **domed lenses** to lessen the **reabsorption** problem.
- A **metal (gold) film** is applied to the **bottom of the substrate**, both to reflect as much
  light as possible back to the surface and to provide the **cathode connection**.
- LEDs are **always encased** to protect their delicate wires.
- Being semiconductor devices they are **rugged**, with a life of more than **10,000 hours**.

[fig ·L1 p14] **Fig. 53.2 — surface-emitting LED, in cross-section.** A rectangular slab divided by a
horizontal line into an upper region labelled **P** and a lower region labelled **N**. Along the top
surface, two short thick metal strips at the **left and right edges only**, arrowed **Metal Contact
(+)**, leaving the centre of the top face clear. The entire bottom face is a thick metal layer,
arrowed **Metal Contact (−)**. Inside, five vertical arrows run **upward**, each starting at a filled
dot (an **electron**) in the N region and ending at a small open circle (a **hole**) just above the
junction line; an arrow labelled **Charge Carrier Combination** points at the junction line. Above the
slab, five arrows point up, labelled **Emitted Light**. Legend: **• Electrons, ○ Holes**.

### (c) Working ·L1 p14

- The **forward voltage** across an LED is **considerably greater** than for a silicon PN junction
  diode.
- Typically the maximum forward voltage is between **1.2 V and 3.2 V** depending on the device.
- **Reverse breakdown** voltage for an LED is of the order of **3 V to 10 V** — very low, which is
  why reverse operation destroys them.
- The LED emits light in response to a sufficient **forward current**; the greater the forward
  current, the greater the light output.

[fig ·L1 p14] **Fig. 53.3 — two panels.**

- **(a)** A simple drive circuit: a battery $V_{bias}$ at the bottom, a series resistor $R$ on the
  left leg, and the LED symbol (with emission arrows) across the top, the forward current $I_F$
  arrowed along the branch.
- **(b)** A graph. Vertical axis **Light output power (mW)**, ticked 1, 2, 3. Horizontal axis
  **Forward Current (mA)**, ticked 50, 100, 150. The curve leaves the origin steeply, bends over
  progressively and flattens toward about 3.5 mW near 175 mA. Approximate readings: ≈1.8 mW at
  50 mA, ≈2.8 mW at 100 mA, ≈3.4 mW at 150 mA.

> ⚠ VERIFY **V1.6** ·L1 p14 — printed: *"The amount of power output translated into light is
> **directly proportional** to the forward current as shown in Fig. 53.3(b)."* The figure the
> sentence points at shows a **distinctly concave-down, saturating curve**, not a straight line
> through the origin. Correct statement:
> $$\boxed{\;\text{light output rises \textbf{monotonically but sub-linearly} with } I_F,\ \text{saturating at high current}\;}$$
> **One-line disproof from the figure's own numbers:** proportionality requires that doubling
> $I_F$ from 50 mA to 100 mA doubles the output, 1.8 → 3.6 mW. The graph reads ≈2.8 mW. The following
> sentence — "greater the forward current, the greater the light output" — is the correct, weaker
> claim. See `_verification-log.md`.

### (d) Applications ·L1 p15

**Selection criteria** — one or more of: wavelength of light emitted, input power required, output
power, efficiency, turn-on and turn-off time, mounting arrangement, light intensity and brightness.

Since LEDs operate at voltage levels from **1.5 V to 3.3 V**, they are highly compatible with
solid-state circuitry. ·L1 p15

*[added] Mild internal inconsistency: p14 gives the maximum forward voltage as 1.2–3.2 V, p15 the
operating range as 1.5–3.3 V. Both are "typical" statements; treat **≈2 V** as the working figure for
a red LED and size the series resistor from the supply, not from the LED.*

**Uses, as listed** ·L1 p15:

1. burglar-alarm systems;
2. solid-state video displays, rapidly replacing cathode-ray tubes (CRT);
3. image-sensing circuits used for 'picturephone';
4. optical fibre communication systems, where high-radiance **GaAs** diodes are matched into the
   silica-fibre optical cable;
5. data links and remote controllers;
6. arrays for displaying alphanumerics, supplying input power to lasers, or entering information into
   optical computer memories;
7. numeric displays in hand-held or pocket calculators.

### Seven-segment displays ·L1 p15–p16

[def ·L1 p15] A seven-segment display consists of **seven rectangular LEDs** which can form the
digits **0 to 9**. The segments are labelled **'a' to 'g'**, and each is controlled through one of
the display LEDs.

[fig ·L1 p15] **Fig. 53.4 — three panels.**

- **(a)** The display drawn as a 3-D block, its face carrying the seven segments in the familiar
  figure-8: **a** across the top, **f** upper-left, **b** upper-right, **g** across the middle,
  **e** lower-left, **c** lower-right, **d** across the bottom. Light rays are drawn leaving the
  right-hand face.
- **(b)** The **schematic**: seven LED symbols stacked vertically, each with its own input terminal
  on the left labelled **a** down to **g**, and **all their cathodes tied to a common vertical rail**
  on the right, which runs to a **ground** symbol — i.e. the **common-cathode** connection.
- **(c)** A photograph of a physical seven-segment display module showing a red digit.

**The two types** ·L1 p16:

| Type | Common terminal | How a segment is lit |
|---|---|---|
| **Common-cathode** | all cathodes tied together, to ground | apply **+5 V** to the anode of that segment |
| **Common-anode** | all anodes tied together, to +5 V | apply **ground** to the cathode of that segment |

**Worked illustration** ·L1 p16 — to display the number **5**, segments **a, f, g, c** and **d** must
be forward-biased.

*[added] Verified against the segment map of Fig. 53.4(a): the digit 5 needs the top bar (a), the
upper-left (f), the middle (g), the lower-right (c) and the bottom (d) ✓ — segments b and e stay
dark.*

> [added] **Safety point the handout omits.** "Only 5 volt is to be applied to the anode of these
> segments" describes the **logic level**, not the drive circuit. An LED connected directly across
> 5 V with no **series current-limiting resistor** is destroyed: 5 V minus a ≈2 V forward drop across
> essentially zero resistance is an unbounded current. Every practical seven-segment drive puts a
> resistor of a few hundred ohms in series with each segment.

### (e) Multicoloured and blinking LEDs ·L1 p16

LEDs are available that give out light in **two or three colours**, and there are also **blinking**
LEDs. ·L1 p16

**Two-colour LED — a three-terminal device** ·L1 p16:

- The **longest lead is the cathode**; the remaining two leads are the **anodes**.
- Forward-biasing leads **R and C** gives **red** light.
- Forward-biasing leads **G and C** gives **green** light.

**Tricolour LED — two leads** ·L1 p16:

- Looks like an ordinary LED but emits **red, green or yellow** depending on operating conditions.
- It has **two leads, each acting as both anode and cathode**.
- **dc one way** → red; **dc the other way** → green; **ac** → **yellow**.

*[added] Why ac gives yellow: the two anti-parallel chips alternate faster than the eye can follow,
so red and green are perceived together as yellow. There is no third chip.*

**Blinking LED** ·L1 p16:

- An **oscillator and an LED in one package**; since it has an anode and a cathode lead it looks like
  an ordinary LED.
- Blinking frequency usually **3 Hz** when the diode forward bias is **5 V**.
- It conducts about **20 mA when ON** and **0.9 mA when OFF**.

[fig ·L1 p16] **Fig. 53.5.** A two-colour LED package drawn face-on: a dome above a rectangular body,
with **three** leads emerging from the base, labelled left to right **R**, **C**, **G**.

[fig ·L1 p16] **Cut-away picture, right column** *(the same image that appears stranded on p3)*. A
dome-shaped LED package in cross-section containing **two chips** drawn as opposed triangles meeting
at a common central post, each with light-emission arrows. Three leads run down from the base,
labelled **a1** and **a2** (the two anodes) and **k** (the common cathode) on the central post.

[fig ·L1 p16] **Photograph, top left, captioned "LED".** A red bullet-shaped LED enlarged, with
callouts to the **Light Beam**, the **Diode** chip on its reflector cup, and the two **Leads**.

> ⚠ VERIFY **C1.10** ·L1 p3, p16 — the two-chip cut-away picture is placed on **p3**, beside the
> junction-barrier-voltage text, where nothing refers to it; it belongs to the multicoloured-LED
> discussion, where it reappears on **p16**. A compilation misplacement. See `_verification-log.md`.

> ⚠ VERIFY **C1.11** ·L1 p16 — printed "*a three-terminal device as shown in **Fig. 3.5***". The
> figure is **Fig. 53.5**, on the same page. The leading 5 has dropped, exactly as in C1.2.
> See `_verification-log.md`.

---

## 1.12 Use of LEDs in facsimile machines ·L1 p16–p17

[def] The signal path in a fax machine ·L1 p16–p17:

1. Light from the **LED array** is focussed on the **document paper**.
2. The light **reflected** at the paper is focussed on a **charge-coupled device (CCD)** by a
   combination of **mirror** and **lens**.
3. This converts the **optical information into electrical information**.
4. The electrical information is sent through the **data-processing unit** to its destination via the
   **telephone line**.

[fig ·L1 p17] **Fig. 53.6 — simplified schematic of a fax machine.** A large rectangular machine
outline. Top right: a stack of sheets labelled **Document paper** feeding in on a slope; a dashed
optical path runs from it down and left. Two pairs of small blocks with dots are arrowed **Sensors for
detecting document paper**. At the centre-left, a solid block labelled **LED array** sends a fan of
rays up to the paper path; below it a tilted rectangle labelled **Mirror** folds the reflected beam to
the right. The folded beam passes through a lens-shaped element labelled **Lens**, converges onto a
narrow vertical element labelled **CCD**, which feeds a box labelled **Data-processing unit**; from
that box an arrow exits right, labelled **Telephone line**. A wide box across the bottom of the
machine is labelled **Printing unit**. Output paper leaves at the lower left.

---

## 1.13 Equivalent circuit of a p-n junction ·L1 p17

### Symbols

| Symbol | Meaning | Units |
|---|---|---|
| $C_D$ | diffusion capacitance (forward bias) | F |
| $C_T$ (also $C_{pn}$) | transition capacitance (reverse bias) | F |
| $R_R$ | reverse resistance | Ω |
| $r_{ac}$ | dynamic ac resistance | Ω |

[def ·L1 p17] A **forward-biased** junction offers ac resistance $r_{ac}$ and possesses **diffusion
capacitance $C_D$**, which comes into the picture only when the frequency of the applied voltage is
**very high**. An **opposing battery $V_B$** is put in series with $r_{ac}$ to account for the
junction barrier potential.

[def ·L1 p17] A **reverse-biased** junction is simply a **reverse resistance $R_R$ in parallel with a
capacitance $C_T$** (also written $C_{pn}$).

[fig ·L1 p17] **Fig. 52.10 — two panels, each drawn between a P terminal on the left and an N terminal
on the right.**

- **(a) Forward-biased.** Two parallel branches. The upper branch contains a **battery $V_B$** in
  series with a **resistor $r_{ac}$**; the lower branch contains a **capacitor $C_D$**.
- **(b) Reverse-biased.** Two parallel branches. The upper branch is a single **resistor $R_R$**; the
  lower branch is a single **capacitor $C_T$**.

*[added] The two capacitances are physically different and it is worth keeping them apart:
**$C_T$** (transition, or depletion, capacitance) is the charge stored on the two rows of fixed ions,
falls as $1/\sqrt{V_R}$ (§1.7, the varactor law) and dominates in **reverse** bias; **$C_D$**
(diffusion, or storage, capacitance) is the stored charge of injected minority carriers, grows
roughly in proportion to forward current, and dominates in **forward** bias. Both are named — but not
distinguished — back on p1, item 3.*

---

## 1.14 Coverage and gap map

### What the p1 outline promises versus what the 18 pages deliver

| Outline item ·L1 p1 | Verdict |
|---|---|
| Operation and characteristics of p-n junction diodes | ✅ **fully covered**, p1–p8 |
| Breakdown diodes: **Zener** type | ✅ **fully covered**, p8–p13, with seven worked circuits |
| Breakdown diodes: **avalanche** type | ⚠ **one paragraph only**, p8 — the mechanism is stated and the 6 V dividing line given, but there is no avalanche characteristic, no worked example |
| **LEDs** | ✅ **fully covered**, p13–p17 |
| **Tunnel diodes** | ❌ **NOT in the handout at all.** No article, no figure, no mention |
| Diode **equivalent circuit** | ✅ covered, p17 (Fig. 52.10) |
| **Load line** | ❌ **NOT in the handout at all.** No load-line figure, no Q-point, no worked example |

**Two named syllabus items are therefore missing from L1 entirely: tunnel diodes and the load line.**
Both should be expected in a CAT regardless. A short `[added]` load-line primer follows; a tunnel
diode is **not** supplied here, because inventing an entire device treatment would breach the
never-invent rule — it should be requested from the lecturer or taken from a nominated textbook.

### [added] The dc load line — supplied here, NOT in the handout

The load line is what turns the diode's V/I curve into an answer for a specific circuit.

**The setup.** A source $V_S$ in series with a resistor $R$ and a diode. The diode's own curve
(Fig. 52.4) gives one relation between $V_D$ and $I$; **KVL** gives the other:

$$V_S = I R + V_D \qquad\Longrightarrow\qquad \boxed{\;I = \frac{V_S - V_D}{R} = -\frac{1}{R}V_D + \frac{V_S}{R}\;}$$

- $V_S$ — source voltage, V · $R$ — series resistance, Ω · $V_D$ — voltage across the diode, V ·
  $I$ — circuit current, A

**Drawing it.** That is a straight line on the same axes as the diode characteristic; two points fix
it:

$$V_D = 0 \;\Rightarrow\; I = \frac{V_S}{R}\ \text{(the $I$-axis intercept)},\qquad
I = 0 \;\Rightarrow\; V_D = V_S\ \text{(the $V$-axis intercept)}$$

Its slope is $-1/R$.

**Reading it.** The **operating point (Q-point)** is where the load line crosses the diode curve.
That intersection is the only $(V_D, I)$ pair that satisfies both the device and the circuit
simultaneously.

*[added] Worked illustration, using this handout's own numbers.* Take $V_S = 5\ \mathrm{V}$,
$R = 500\ \Omega$ and a silicon diode:

$$\text{Intercepts: } I|_{V_D=0} = \frac{5}{500} = 10\ \mathrm{mA};\qquad V_D|_{I=0} = 5\ \mathrm{V}$$

$$\text{With the 0.7 V approximation: } I = \frac{5-0.7}{500} = 8.6\ \mathrm{mA}$$

Cross-check against §1.6: at 8.6 mA the junction resistance is
$r_j = 50/8.6 = 5.8\ \Omega$ — negligible beside the 500 Ω series resistor, which is exactly why the
constant-0.7 V approximation is safe here.

### Verification notes for this section

All 18 pages read from **200 dpi renders**, with eleven regions re-cropped and magnified 2.4–5× to
settle specific readings (p2 depletion-layer sentence; p4 Fig. 51.35 arrow directions; p5 forward-bias
carrier arrows; p6 boxed equation and the axis unit; p7 the four exponent forms and Fig. 52.5;
p8 both $kT/e$ lines; p10 the part-number sentence and Fig. 54.5; p11 Figs. 54.6 and 54.7 and the
overlapping text; p12 Fig. 54.8; p14 Fig. 53.2 and the LED output curve; p18 the Example 52.7 lines).
Every numerical claim was recomputed independently.

**17 flags — 6 substantive, 11 cosmetic.** Three of the six substantive flags (V1.2, V1.3, V1.5) are
defects in how the **diode equation** is typeset, and one more (V1.4) is arithmetic inside an example
that uses it.

| ID | Page | Class | Summary |
|---|---|---|---|
| **V1.1** | p2 | substantive | depletion layer said to contain "only positive ions"; it contains fixed negative **and** positive ions |
| **V1.2** | p6 | substantive | the highlighted diode equation omits the ideality factor $\eta$, which is defined three lines below and used thereafter |
| **V1.3** | p7, p8 | substantive | the $-1$ is printed **inside** the exponent in five places; at $V=0$ that gives $I = 0.368\,I_0 \neq 0$ |
| **V1.4** | p8 | substantive | $kT/e$ at 398 K given as 36 mV; it is 34.3 mV, and $V_B(125\,°\mathrm{C})$ is 0.47 V, not 0.5 V |
| **V1.5** | p18 | substantive | Example 52.7 prints $40\times10^{3}$ for $40\times10^{-3}$; expression evaluates to 1.816 A, not 1.82 µA |
| **V1.6** | p14 | substantive | light output claimed "directly proportional" to $I_F$; the adjacent figure is a saturating curve |
| **C1.1** | p3, p6, p8, p18 | cosmetic | temperatures written "°K" and $k$ as "J/°K"; the kelvin takes no degree sign |
| **C1.2** | p4, p10, p18 | cosmetic | cross-references "Art. 1.40", "Art 4.1", "Art. 1.38" — the leading 5 dropped in each |
| **C1.3** | p4 | cosmetic | Example 51.14 writes $n^2$ for $n_i^2$ |
| **C1.4** | p4 | cosmetic | Fig. 51.35 caption "Difusion Currents"; recurring spelling typos elsewhere |
| **C1.5** | p6 | cosmetic | Fig. 52.4 reverse-current axis labelled "200 A"; the µ prefix has dropped |
| **C1.6** | p8 | cosmetic | $kT/e$ at 398 K printed with "×" where "÷ e" is meant; and "In" for "ln" four lines below |
| **C1.7** | p10–p11 | cosmetic | the statement of Example 54.4 is missing; only its solution is printed |
| **C1.8** | p10 | cosmetic | Zener part numbers printed "IN 750"/"IN 4000" for 1N750/1N4000 |
| **C1.9** | p11 | cosmetic | first line of §54.2 and the Fig. 54.6 caption printed twice, overlapping |
| **C1.10** | p3, p16 | cosmetic | the two-chip LED cut-away is stranded on p3, where nothing refers to it |
| **C1.11** | p16 | cosmetic | "Fig. 3.5" for Fig. 53.5 |

**Verified sound, no flag:**

- $V_T = kT/e = 25.875\ \mathrm{mV}$ at 300 K ✓ · $e/k = 11{,}594 \approx 11{,}600$ ✓ ·
  $V_T = 293/11{,}600 = 25.3\ \mathrm{mV}$ ✓ · $V_T = 343/11{,}600 = 29.6\ \mathrm{mV}$ ✓
- Example 51.13: $641.0\ \mathrm{mV}$ ✓ exactly as printed
- Example 51.14: $26\ln1000 = 179.6\ \mathrm{mV}$ (printed 179 mV — truncated, not an error)
- Example 52.1: $kT/e = 25.01\ \mathrm{mV}$ at 290 K ✓, $25\ln2 = 17.33\ \mathrm{mV}$ ✓
- Example 52.2 at 27 °C: $26\ln(10^{11}+1) = 658.5\ \mathrm{mV}$ ✓ (printed 660 mV, rounded)
- Example 52.6: 0.55 V and 0.75 V ✓ both
- Example 52.7 final answer $1.816\ \mu\mathrm{A}$ ✓ (only the middle line is wrong — V1.5)
- Example 52.8: $e^{12}-1 = 162{,}754$ ✓, $32(e^{10}-1) = 704{,}816$ ✓, ratio $4.33$ ✓
- Examples 54.1–54.3: 4 mA ✓, 10 mA ✓, 6.67 mA ✓, 3.33 mA ✓ — printed power 39.6 mW is 40.0 mW to
  full precision (rounding, not an error)
- Fig. 54.6 example: $E_o = 0$ and $E_o = 10\ \mathrm{V}$ ✓ both
- Example 54.5: 10 mA, 5 mA, 5 mA, $I_{z\max} = 50\ \mathrm{mA}$, then 20 mA / 5 mA / 15 mA ✓ all
- Example 54.6: 9 mA, 4 mA, 0 ✓ all three parts
- Example 54.7: 25 mA, 320 Ω, 20 mA, 5 mA ✓ all
- $r_j = 25\ \mathrm{mV}/I_F$ (Ge) and $50\ \mathrm{mV}/I_F$ (Si) ✓ — both are $\eta V_T/I_F$
- The 40 and 20 multipliers ✓ — both are $1/(\eta V_T)$ at 25 mV
- Fig. 51.35 drift and diffusion arrow directions ✓ all four correct
- Fig. 53.4(b) common-cathode wiring ✓; digit "5" = segments a, f, g, c, d ✓
- Fig. 54.8 two-Zener series stack — the 30 V and 20 V references follow correctly ✓

**No page of this document was illegible.** Every figure described above was looked at in the render;
the four photographic figures (p1, p2, p10(d), p13, p16) are described but, being third-party
photographs, are never reproduced.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
