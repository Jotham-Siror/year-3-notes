---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "12 — Rectification and Power Supplies (supporting)"
source: "L2 — 'Lesson 2 Rectifiers.pdf', 26 pp."
pages: "1-26"
tier: supporting
file_role: topic
subtopics:
  - "the dc power supply as five stages: transformer, rectifier, filter, regulator, divider"
  - "the eight rectifier circuits the handout names, and which of them it actually delivers"
  - "single-phase half-wave rectifier: working, waveforms, average and rms values"
  - "rectification efficiency, the Fourier series of the rectified wave, and its harmonics"
  - "ripple factor and form factor — three equivalent definitions"
  - "peak inverse voltage (PIV) and transformer utilisation factor (TUF)"
  - "single-phase full-wave centre-tapped rectifier and its full parameter set"
  - "full-wave bridge rectifier, its four advantages and its one disadvantage"
  - "three-phase half-wave rectifier with a C-L-C filter; conduction intervals"
  - "full-wave rectification of three-phase currents (six-diode, interphase transformer)"
  - "voltage regulation of a rectifier, and worked regulator arithmetic"
  - "clippers: series, parallel, biased and double-ended limiting"
  - "clampers (dc restorers): the RC time-constant rule and the four standard circuits"
  - "voltage multipliers: half-wave and full-wave doublers, tripler, quadrupler"
  - "the tunnel diode: construction, negative resistance, tunnelling theory, applications"
key_equations: [hw-peak-current, hw-vdc, hw-vrms, hw-efficiency, hw-fourier, ripple-factor, form-factor, ripple-from-form-factor, hw-ripple, hw-piv, hw-tuf, fw-vdc, fw-vrms, fw-efficiency, fw-fourier, fw-ripple, fw-piv, fw-tuf, bridge-peak-current, bridge-efficiency, bridge-piv, voltage-regulation, three-phase-hw-vdc, clamper-time-constant, doubler-output, multiplier-piv, tunnel-negative-resistance, ripple-voltage-shunt-c, ripple-factor-shunt-c, smoothing-capacitor]
prerequisites: ["01-diodes (the p-n junction, forward drop, dynamic resistance, PIV, ideal-diode model)", "ac circuit theory: rms and average values, Fourier series, transformer turns ratio", "RC transient response and the time constant"]
leads_to: ["filters and smoothing circuits (capacitor-input, choke-input, pi-filter)", "Zener and series voltage regulators", "03-bipolar-junction-transistor (transistor-based regulators and amplifiers)"]
verification_flags: 43
tags: [rectifier, half-wave, full-wave, centre-tap, bridge-rectifier, three-phase, ripple-factor, form-factor, rectification-efficiency, transformer-utilisation-factor, piv, voltage-regulation, fourier-series, clipper, limiter, clamper, dc-restorer, voltage-multiplier, voltage-doubler, tunnel-diode, negative-resistance]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] table of data or comparisons ·
  [added] supplied here, NOT in the source ·
  ·L2 pN = provenance (which PDF page of Lesson 2 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = a page or figure that could not be read.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 02 — Rectification and Power Supplies

Scope: the whole of L2, 26 pages. Builds the dc power supply from its five stages, works the
half-wave rectifier through its complete parameter set — $V_{dc}$, $V_{rms}$, efficiency, Fourier
series, ripple factor, PIV, TUF — then repeats that set for the centre-tapped full-wave rectifier
and the bridge, adds two three-phase circuits, and closes with three wave-shaping topics
(clippers, clampers, voltage multipliers) and the tunnel diode.

> ## ⚠ Read §2.6 before quoting any half-wave figure of merit
>
> **The half-wave parameter derivations on pages 4–6 carry four separate constant errors**, and
> three of them are factors of $\pi$ or $\sqrt2$ in results that are pure examination fodder: the
> printed efficiency reads **409.6 %**, the printed second-harmonic rms is short by $\sqrt2$, and
> the TUF derivation loses a $\pi$ twice (arriving at the right final number by two compensating
> slips). The full-wave pages repeat two of the same faults. Every constant in this file has been
> re-derived and recomputed; the boxed forms are the corrected ones.

> ## ⚠ The figure printed as "Fig. 55.6(a)" is the wrong circuit
>
> Article 55.7 announces *"the full-wave rectifier circuit using two diodes and a centre-tapped
> transformer shown in 55.6(a)"* — but the figure printed under that label is a **four-diode
> bridge**, and its waveform panel is labelled *"Output of $D_1$ & $D_3$"* / *"Output of $D_2$ &
> $D_4$"*. The bridge belongs to Article 55.8 — whose own Fig. 55.10 is missing from the handout.
> The genuine centre-tapped circuit does appear, one figure later, as **Fig. 55.7**. See V2.9.

**What the p1 outline promises and the 26 pages do not deliver.** The topic line on p1 lists
*"Half wave and full wave rectifier circuits; Ripple factor; **smoothing**; Voltage regulation,
Clipping, Clamping, Voltage Multiplier/doublers, **Limiter**."* There is **no filter/smoothing
section anywhere in the document** — smoothing is named in the p1 block diagram and a C-L-C filter
is drawn in passing on p12, and that is all. "Limiter" never appears as a word; it is the clipper
work of §52.16–52.17 under another name. §2.12 supplies an `[added]` smoothing-capacitor primer,
clearly marked as not the lecturer's.

**Why this file is not split.** It exceeds the ~25 KB threshold, but the rectifier chain is one
continuous argument — the half-wave parameter set of §2.6 is the template that §2.7 (centre-tap),
§2.8 (bridge) and §2.9–§2.10 (three-phase) each re-instantiate, and the clipper/clamper/multiplier
sections are all diode-application material tied to the same topic line on p1. Per
`../../docs/kb-format.md`, one lesson stays one topic file.

---

## 2.1 How this file maps onto the handout ·L2 p1–p26

The handout is a compiled photocopy of textbook articles under a Strathmore/BEE 3103 header. Three
consequences for navigation:

- **The article numbers are the parent textbook's, and they run badly out of order.** The sequence
  is 55.1–55.10 (p1–p13), then a jump *backwards* to **52.15–52.19** (p14–p20, clippers and
  clampers), then *forward* to **55.25–55.28** (p21–p23, voltage multipliers), then *backwards
  again* to **54.7** (p23–p26, the tunnel diode). Citations in this file are to the **PDF page**,
  which is the only reliable coordinate.
- **Figures and one example are missing.** Figures 55.5, 55.10 and everything from 55.15 to
  55.30 never appear; **Example 55.2 is absent** although Example 55.5 on p10 depends on its data
  (§2.7.7 reconstructs it). No page carries a printed page number of its own.
- **There are no unsolved exercises anywhere in these 26 pages.** Every problem is a fully worked
  example. Two questions are *posed inside* worked examples and left unanswered — "what happens if
  diode and resistor are interchanged?" (p14, answered on p15) and "how will it change if $R$ is
  made 100 Ω?" (p19, answered on p20) — so both are in fact answered. The `[exercise]`-tagged items
  below are therefore the two figure-only circuits the handout draws without analysing
  (Fig. 52.38 and Fig. 52.39); their solutions are supplied in `[added]` blocks.

**Where the work is.** Roughly a quarter of the document is worked numbers: **six examples**
(55.1, 55.3, 55.4, 55.5, 52.19–52.23 counting the clipper set) plus the parameter derivations. The
formula-dense pages 3–13 are the exam core; pages 23–26 (tunnel diode) are descriptive and carry no
arithmetic at all.

**Triage.** Pages 3–12 — half-wave, centre-tap and bridge parameter sets — are where a CAT will
live. Pages 12–13 (three-phase) are worth knowing to the level of three numbers each. Pages 14–20
(clippers and clampers) are drawing questions: the reasoning is always *"decide when the diode is
forward-biased, then replace it by a short or an open"*. Pages 21–23 (multipliers) reduce to two
sentences and one KVL. Pages 23–26 (tunnel diode) are pure recall.

---

## 2.2 The dc power supply — five stages ·L2 p1–p2

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_s$ | rms transformer secondary voltage | V | 12–240 |
| $V_{sm}$ | peak (maximum) transformer secondary voltage | V | $\sqrt2\,V_s$ |
| $V_L$ | rms load voltage | V | — |
| $V_{LM}$ | peak load voltage | V | $V_{sm}$ minus drops |
| $V_{L(dc)}$ | average (dc) load voltage | V | $0.318V_{LM}$ (HW) |

[def ·L2 p1] **Rectification.** The process of converting an ac voltage — usually the 220 V rms
domestic supply — into a dc voltage, usually smaller in value. It is accomplished by three things
in cascade: a **rectifier**, a **filter** and a **voltage-regulator circuit**. Together these
constitute a **dc power supply**.

The handout's motivation is economic: dry cells and batteries are portable and ripple-free, but
their voltages are low, they need frequent replacement, and they are expensive compared with a
mains-derived supply. ·L2 p1

[def ·L2 p1] **Unregulated power supply** — one whose dc terminal voltage is affected significantly
by the amount of load. As the load draws more current, the dc terminal voltage falls.

[def ·L2 p1] **Regulated power supply** — one whose terminal voltage remains almost constant
regardless of the current drawn from it. An unregulated supply becomes regulated by adding a
voltage-regulating circuit.

[fig ·L2 p1] **Fig. 55.1 — block diagram of a typical dc power supply.** Left to right, five boxes
in a row, each joined to the next by a right-pointing arrow:

$$\text{AC Input}\ \longrightarrow\ \boxed{\text{Transformer}}\ \longrightarrow\ \boxed{\text{Rectifier}}\ \longrightarrow\ \boxed{\text{Filter}}\ \longrightarrow\ \boxed{\text{Voltage Regulator}}\ \longrightarrow\ \boxed{\text{Voltage Divider}}\ \longrightarrow\ \text{DC Output}$$

At the far left a small sine wave is drawn against a horizontal axis, labelled **AC Input**; at the
far right a **flat horizontal line**, labelled **DC Output**. The contrast between the two traces
is the whole point of the figure.

[fig ·L2 p1] A photograph captioned **"Single filament Rectifier"** — a dark blue moulded body with
a helical copper winding around a light-coloured rectangular core and two orange lead-out wires.
Being a third-party photograph it is described, never reproduced.

### The five stages ·L2 p1–p2

1. **Transformer** — steps the ac supply up or (mostly) **down** to suit the solid-state devices
   fed by the supply. It also **provides isolation from the supply line**, which the handout
   flags as an important safety consideration.
2. **Rectifier** — a circuit employing one or more diodes to convert ac voltage into **pulsating
   dc** voltage.
3. **Filter** — removes the fluctuations (**ripples**) present in the rectifier output. No
   practical filter gives an output as ripple-free as a dc battery, but a good one approaches it
   closely enough.
4. **Voltage regulator** — keeps the dc terminal voltage constant when (i) the ac input to the
   transformer varies (deviations from 220 V are common), or (ii) the load varies. Zener diodes
   and transistors are the usual regulating elements. 100 % constancy is impossible; minor
   variation is acceptable.
5. **Voltage divider** — a chain of series resistors across the regulator output, providing the
   several different dc voltages different sub-circuits need. It removes the need for a separate
   supply per dc level.

[def ·L2 p2] **The handout's own comment on stages 3–5.** Strictly, ac→dc conversion needs only a
transformer and a rectifier — and even the transformer can go if no voltage transformation is
wanted. **Filter, regulator and divider are refinements**, essential for most applications but not
for battery charging or running small dc motors.

**Polarity.** Only *positive* dc supplies are analysed. A positive supply becomes a negative one by
reversing its two output leads, exactly as one reverses a dry cell. Where an IC needs both
polarities about a common ground, every **polarised** component in the negative half — rectifier,
filter capacitor, regulating devices — must be reversed relative to the positive half. ·L2 p2

---

## 2.3 The eight rectifier circuits the handout names ·L2 p2

[table ·L2 p2] Article 55.4 lists eight circuits. Only six are actually developed in these 26 pages.

| # | Circuit | Delivered? | Where |
|---|---|---|---|
| 1 | single-phase half-wave rectifier | ✔ | §55.5–55.6, p2–p7 |
| 2 | single-phase full-wave rectifier (centre-tap) | ✔ | §55.7, p7–p10 |
| 3 | full-wave bridge circuit | ✔ | §55.8, p11–p12 |
| 4 | three-phase half-wave rectifier | ✔ | §55.9, p12–p13 |
| 5 | three-phase full-wave rectifier | ✔ | §55.10, p13 |
| 6 | six-phase half-wave rectifier | ✘ | **never appears** |
| 7 | three-phase bridge circuit | ✘ | **never appears** |
| 8 | voltage multiplier circuits | ✔ | §55.25–55.28, p21–p23 |

> ⚠ VERIFY **C2.1** ·L2 p2, p10 — the handout promises eight rectifier circuits and delivers six;
> **items 6 (six-phase half-wave) and 7 (three-phase bridge) never appear**. Related gaps: Figs.
> 55.5, 55.10 and 55.15–55.30 are absent, and **Example 55.2 is missing** although Example
> 55.5 (p10) is built entirely on its data. Not an error of physics — a compilation gap — but a
> reader hunting for a promised circuit needs to know it is not there. See §2.7.7 for a
> reconstruction of Example 55.2 and `_verification-log.md`.

---

## 2.4 Single-phase half-wave rectifier — working ·L2 p2–p3

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $v_s$ | instantaneous secondary voltage | V | $V_{sm}\sin\omega t$ |
| $V_{sm}$ | peak secondary voltage | V | 31 (Ex 55.1) |
| $V_{LM}$ | peak load voltage $=V_{sm}-$ diode drop $-$ secondary-resistance drop | V | 31 |
| $I_{LM}$ | peak load current | A | 0.31 |
| $i_L$ | instantaneous load current | A | — |
| $R_L$ | load resistance | Ω | 100 |
| $R_S$ | transformer secondary resistance | Ω | ≪ $R_L$ |
| $r_d$ | diode forward (bulk) resistance | Ω | 25 |
| $R_0$ | $R_S+r_d$ — total series resistance outside the load | Ω | 25 |
| $V_B$ | diode barrier (knee) voltage | V | 0.7 (Si), 0.3 (Ge) |
| $\omega$ | angular frequency of the supply | rad s⁻¹ | $2\pi\times50$ |

[eq] **The input.** The alternating secondary voltage is taken as

$$\boxed{\;v_s = V_{sm}\sin\omega t\;}$$

> ⚠ VERIFY **V2.1** ·L2 p2 — printed as $V_s = V_{sm}\,wt$. Two defects in one line: the **$\sin$
> is missing**, and $\omega$ is set as a roman "w". As printed the right-hand side has units of
> volt-radians and grows without bound, so it cannot be a supply voltage. Correct form:
> $$\boxed{\;v_s = V_{sm}\sin\omega t\;}$$
> See `_verification-log.md`.

[fig ·L2 p3] **Fig. 55.2(a) — the half-wave rectifier circuit.** Reading left to right:

- A circular **ac source symbol** (circle enclosing a sine) drives the transformer **primary**
  (drawn as a vertical coil), with the return wire running round the outside of the diagram.
- The transformer **secondary** is a second vertical coil; its **top terminal is A**, marked
  $\pm$, and its **bottom terminal is B**, marked $\mp$. The secondary voltage is labelled
  $V_{SM}$ alongside the winding.
- From **A**, the **diode D** lies in the top wire with its **anode at A and cathode at E** (the
  triangle points right, the bar is on the right).
- From **E**, the load $R_L$ (vertical zig-zag) runs down to **F** on the bottom wire; the load
  current $i_L$ is arrowed **downward** through $R_L$.
- The top wire continues from E to the open output terminal **M** (top right); the bottom wire
  runs F to **N** (bottom right). The output voltage $V_L$ is measured **between M and N**, with
  the arrow drawn upward (+ at M).
- **B connects to F**, closing the loop.

[fig ·L2 p3] **Fig. 55.2(b) — the two waveforms, one above the other on a common time axis.**

- **Upper, labelled "Input", ordinate $V_s$:** a **complete sinusoid**, peak $V_{SM}$ marked on the
  ordinate by a tick, symmetric positive and negative half-cycles, crossing zero at $O$.
- **Lower, labelled "Output", ordinate $V_L$:** **half-wave rectified sinusoids of peak
  $V_{LM}$** — a positive hump for each positive input half-cycle, and a **flat run along the zero
  axis** for each negative half-cycle. The humps are separated by gaps exactly as wide as the humps.

### Working ·L2 p2–p3

- **Positive input half-cycle** — the diode is **forward-biased (ON)** and conducts. While
  conducting it behaves as a short-circuit, so the positive half-cycle appears across $R_L$; this
  is the output voltage $V_L$.
- **Negative input half-cycle** — the diode is **reverse-biased (OFF)** and does not conduct.
  There is no current, hence no drop across $R_L$: $i_L=0$ and $V_L=0$. The negative half-cycle is
  **suppressed** — not used for delivering power to the load.
- The output is therefore **not steady dc but pulsating dc**, with a **ripple frequency equal to
  the input frequency**. An oscilloscope across $R_L$ shows the pulses; a dc meter shows their
  **average** positive value, for both voltage and current.
- Only one half-cycle of the input is used — hence *half-wave*.

**Modelling assumption.** The above neglects the diode's forward voltage drop: it assumes an
**ideal diode** — zero forward resistance and infinite reverse resistance. The formulas of §2.5
then re-introduce the drop through $V_B$ and $r_d$. ·L2 p3

---

## 2.5 Half-wave rectifier — average and rms values ·L2 p3

[eq: hw-peak-current] **Peak load current.** The peak secondary voltage less the diode's barrier
voltage, divided by the total series resistance:

$$\boxed{\;I_{LM}=\frac{V_{sm}-V_B}{(R_S+r_d)+R_L}=\frac{V_{sm}-V_B}{R_0+R_L}\;}\qquad R_0\equiv R_S+r_d$$

and the peak load voltage follows by Ohm's law:

$$\boxed{\;V_{LM}=I_{LM}R_L\;}$$

> ⚠ VERIFY **C2.2** ·L2 p3 — $V_B$ appears in the boxed $I_{LM}$ formula but is **not in the "Let"
> list** immediately above it, which defines every other symbol on the page. $V_B$ is the diode's
> **barrier (knee) voltage** — 0.7 V for silicon, 0.3 V for germanium, per L1 §1.3. Purely a
> missing definition; the formula is right. See `_verification-log.md`.

[derivation ·L2 p3] **Average (dc) values.** Over a full period the half-wave output is
$V_{LM}\sin\omega t$ for $0\le\omega t\le\pi$ and zero for $\pi\le\omega t\le2\pi$, so

$$V_{L(dc)}=\frac{1}{2\pi}\int_0^{\pi}V_{LM}\sin\theta\,d\theta=\frac{V_{LM}}{2\pi}\Big[-\cos\theta\Big]_0^{\pi}=\frac{V_{LM}}{2\pi}(2)$$

[eq: hw-vdc]

$$\boxed{\;V_{L(dc)}=\frac{V_{LM}}{\pi}=0.318\,V_{LM}\;}\qquad\boxed{\;I_{L(dc)}=\frac{I_{LM}}{\pi}=0.318\,I_{LM}\;}$$

[eq: hw-vrms] **RMS values.** Squaring and averaging over the *whole* period — the zero half
counts towards the mean square — halves the usual $V_{LM}^2/2$:

$$V_L^2=\frac{1}{2\pi}\int_0^{\pi}V_{LM}^2\sin^2\theta\,d\theta=\frac{V_{LM}^2}{4}$$

$$\boxed{\;V_L=\frac{V_{LM}}{2}=0.5\,V_{LM}\;}\qquad\boxed{\;I_L=\frac{I_{LM}}{2}=0.5\,I_{LM}=0.5\,\frac{V_{LM}}{R_L}\;}$$

> ⚠ VERIFY **C2.3** ·L2 p3 — the rms-current line prints as $I_L = I_L M_n/2 = 0.5I_{LM}$. The
> first token is a typesetting garble of $I_{LM}/2$ (the subscript has broken apart and picked up a
> stray "n"). The rest of the line is correct. See `_verification-log.md`.

[added] **Why the half-wave rms is $V_{LM}/2$ and not $V_{LM}/\sqrt2$.** A full sinusoid has
$V_{rms}=V_m/\sqrt2$. The half-wave output is that sinusoid for half the time and zero for the
other half, so its **mean square is halved**, and the rms falls by $\sqrt2$:
$\dfrac{V_{LM}}{\sqrt2}\cdot\dfrac{1}{\sqrt2}=\dfrac{V_{LM}}{2}$. This one factor is the origin of
almost every half-wave-versus-full-wave difference that follows.

---

## 2.6 Half-wave rectifier — the figures of merit ·L2 p4–p6

This is the section that produces exam questions, and the section with the errors. Every constant
below has been re-derived and recomputed.

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $\eta$ | rectification (conversion) efficiency | — | 0.405 max (HW) |
| $P_{dc}$ | dc power delivered to the load | W | — |
| $P_{in}$ | ac input power from the secondary | W | — |
| $I_{L(ac)}$ | rms value of all ac (ripple) components of load current | A | $0.385I_{LM}$ (HW) |
| $I_{L1},I_{L2},I_{L3}$ | rms values of the fundamental, 2nd, 4th harmonic | A | — |
| $\gamma$ | ripple factor | — | 1.21 (HW) |
| $K_f$ | form factor | — | 1.57 (HW) |
| PIV | peak inverse voltage across the diode | V | $V_{sm}$ (HW) |
| TUF | transformer utilisation factor | — | 0.287 (HW) |

### (c) Rectification efficiency ·L2 p4

[def ·L2 p4] **Efficiency of rectification** — the ratio of the output dc power to the total ac
input power supplied to the circuit. Also called the **conversion efficiency**.

[derivation ·L2 p4]

$$\eta=\frac{P_{dc}}{P_{in}}=\frac{\text{power in the load}}{\text{input power}}$$

$$P_{dc}=I_{L(dc)}^2R_L=\left(\frac{I_{LM}}{\pi}\right)^{2}R_L=\frac{I_{LM}^{2}}{\pi^{2}}R_L$$

$$P_{in}=I_L^2(R_L+R_0)=\left(\frac{I_{LM}}{2}\right)^{2}(R_L+R_0)=\frac{I_{LM}^{2}}{4}(R_L+R_0)$$

$$\eta=\frac{P_{dc}}{P_{in}}=\left(\frac{4}{\pi^{2}}\right)\frac{R_L}{R_L+R_0}$$

[eq: hw-efficiency]

$$\boxed{\;\eta_{\text{HW}}=\frac{4}{\pi^{2}}\cdot\frac{1}{1+R_0/R_L}=\frac{40.5\,\%}{1+R_0/R_L}\;}$$

With $R_0$ neglected, $\eta_{\max}=4/\pi^2=0.4053=\mathbf{40.5\,\%}$ (the handout, and most
textbooks, quote **40.6 %**).

**Meaning.** Under the best possible conditions — a diode with no internal resistance — only about
40 % of the ac input power is converted into dc power. The remainder stays in the load as **ac
power**. ·L2 p4

> ⚠ VERIFY **V2.2** ·L2 p4 — the last step of the efficiency chain prints
> $$\eta=\frac{0.406}{1+R_0/R_L}=\frac{409.6\,\%}{(1+R_0/R_L)}$$
> **409.6 % is impossible** — a rectifier cannot deliver ten times the power put into it, and the
> preceding expression $0.406$ *is* 40.6 %, not 409.6 %. A stray digit. Correct form:
> $$\boxed{\;\eta=\frac{4}{\pi^{2}}\cdot\frac{R_L}{R_L+R_0}=\frac{40.5\,\%}{1+R_0/R_L}\;}$$
> Recomputed: $4/\pi^2 = 0.405285$. See `_verification-log.md`.

> ⚠ VERIFY **C2.4** ·L2 p4, p8 — the quoted maxima **40.6 %** (half-wave) and **81.2 %**
> (full-wave) are each rounded *up* from the exact values $4/\pi^2 = 40.53\,\%$ and
> $8/\pi^2 = 81.06\,\%$. The 0.1-point discrepancy is inherited from the parent textbook and is
> the number an examiner will expect, so **use 40.6 % / 81.2 % in a CAT** — but know that a
> question asking for $4/\pi^2$ to three figures wants 0.405, not 0.406. Recomputed:
> $4/\pi^2=0.405285$, $8/\pi^2=0.810569$. See `_verification-log.md`.

> ⚠ VERIFY **C2.5** ·L2 p4, p8 — the sentence "If $R_0$ is neglected $h=40.6\,\%$" sets the
> efficiency symbol as a roman **"h"** rather than $\eta$; the same substitution recurs on p8. On
> the same line "effficiency" is misspelt with three f's. Font/typo only. See
> `_verification-log.md`.

### (d) Frequency components of the rectified wave ·L2 p4–p5

[fig ·L2 p4] **Fig. 55.3 — the dc and ac content of the load current.** Ordinate $I_L$, abscissa
$t$, origin marked 0. **Three half-wave humps** are drawn, each shaded pale yellow beneath the
curve, separated by flat runs along the axis. The peak is ticked on the ordinate as $I_{LM}$. **Two
closely spaced dashed horizontal lines** cross the whole plot: the **upper** one is arrowed and
labelled $I_L$ (the rms value, $0.5I_{LM}$), the **lower** one is the top of a short double-headed
vertical arrow from the axis labelled $I_L$ (dc) (the average, $0.318I_{LM}$). A separate arrow
labelled $I_L$ (ac) points at the rising flank of the first hump. The figure's message: the load
current is a dc level with a large ac content sitting on top of it.

[eq: hw-fourier] **Fourier series of the half-wave rectified current** ·L2 p4

$$\boxed{\;i_L=I_{LM}\left(\frac{1}{\pi}+\frac{1}{2}\sin\omega t-\frac{2}{3\pi}\cos2\omega t-\frac{2}{15\pi}\cos4\omega t+\ \cdots\right)\;}$$

Term by term — this is the standard bookwork and each rms value is peak$/\sqrt2$:

| Term | Component | Frequency | Peak | RMS |
|---|---|---|---|---|
| 1st | dc | 0 | — | $I_{L(dc)}=I_{LM}/\pi=0.318I_{LM}$ |
| 2nd | fundamental (1st harmonic) | $f$ | $I_{LM}/2$ | $I_{L1}=\dfrac{I_{LM}}{2\sqrt2}=0.354I_{LM}$ |
| 3rd | 2nd harmonic | $2f$ | $\dfrac{2I_{LM}}{3\pi}$ | $I_{L2}=\dfrac{\sqrt2\,I_{LM}}{3\pi}=0.150I_{LM}$ |
| 4th | 4th harmonic | $4f$ | $\dfrac{2I_{LM}}{15\pi}$ | $I_{L3}=\dfrac{\sqrt2\,I_{LM}}{15\pi}=0.030I_{LM}$ |

Note that the series contains **only even harmonics** above the fundamental — there is no
$\cos3\omega t$ term — which is why the third row of the table jumps from $2f$ to $4f$.

> ⚠ VERIFY **V2.3** ·L2 p4 — the second-harmonic rms is printed as
> $$I_{L2}=\text{peak value}/\sqrt2=\frac{2I_{LM}}{3\pi\sqrt2}=\frac{I_{LM}}{3\pi}$$
> The middle expression is right; **the final one has lost a $\sqrt2$**, since
> $2/\sqrt2=\sqrt2$, not 1. Correct form:
> $$\boxed{\;I_{L2}=\frac{2I_{LM}}{3\pi\sqrt2}=\frac{\sqrt2\,I_{LM}}{3\pi}=0.1501\,I_{LM}\;}$$
> **Two independent checks.** (i) The very next page prints the *voltage* version correctly as
> $V_{L2}=\sqrt2\,V_{LM}/3\pi$. (ii) The printed total $I_{L(ac)}=0.385I_{LM}$ only comes out if
> the $\sqrt2$ is present: with it, $\sqrt{0.125+0.022516+0.000901}=0.38525$ ✓; without it,
> $\sqrt{0.125+0.011258+0.000901}=0.3702$ ✗. The printed value $I_{LM}/3\pi=0.1061I_{LM}$ is
> **29 % low**. See `_verification-log.md`.

> ⚠ VERIFY **C2.6** ·L2 p4 — the fourth term is called "**the third harmonic component** whose
> frequency is **four times** the supply frequency", one sentence after the third term was called
> "the second harmonic ... double the supply frequency". A component at $4f$ is the **fourth**
> harmonic on the naming used one line above; the handout has slipped from harmonic-numbering to
> term-numbering mid-paragraph. The physics and the coefficient are right. See
> `_verification-log.md`.

**Voltage form of the same series** ·L2 p5 — the handout gives the rms voltage harmonics directly:

$$V_{L(dc)}=\frac{V_{LM}}{\pi},\qquad V_{L1}=\frac{V_{LM}}{2\sqrt2},\qquad V_{L2}=\frac{\sqrt2\,V_{LM}}{3\pi},\qquad V_{L3}=\frac{\sqrt2\,V_{LM}}{15\pi}$$

> ⚠ VERIFY **V2.4** ·L2 p5 — the fundamental is printed as $V_{L1}=V_{LM}/\sqrt2$. The
> fundamental's **peak** is $V_{LM}/2$ (from the $\tfrac12\sin\omega t$ term of the series), so its
> rms is that divided by $\sqrt2$ — the printed form has **lost the factor 2**. Correct form:
> $$\boxed{\;V_{L1}=\frac{V_{LM}}{2\sqrt2}=0.354\,V_{LM}\;}$$
> **Check.** The same page prints the current version correctly as $I_{L1}=I_{LM}/2\sqrt2$, and
> $V_{LM}/\sqrt2=0.707V_{LM}$ would on its own exceed the *whole* rms output $V_L=0.5V_{LM}$ —
> impossible for one harmonic. See `_verification-log.md`.

### (e) Ripple factor ·L2 p5

[def ·L2 p5] **Ripple factor $\gamma$** — the ratio of the rms value of the ac (ripple) components
of the output to its dc value. It measures how far the output departs from pure dc: **smaller is
better**, and $\gamma=0$ is a perfect battery.

[eq: ripple-factor]

$$\boxed{\;\gamma=\frac{I_{L(ac)}}{I_{L(dc)}}=\frac{\sqrt{I_L^{2}-I_{L(dc)}^{2}}}{I_{L(dc)}}=\sqrt{\left(\frac{I_L}{I_{L(dc)}}\right)^{2}-1}\;}$$

- $I_{L(ac)}=\sqrt{I_L^2-I_{L(dc)}^2}$ — rms of everything that is not dc, in A
- $I_L$ — total rms load current, in A
- $I_{L(dc)}$ — dc (average) load current, in A

[def ·L2 p5] [eq: form-factor] **Form factor** $K_f$ — rms divided by average:

$$\boxed{\;K_f=\frac{I_L}{I_{L(dc)}}=\frac{V_L}{V_{L(dc)}}\;}$$

[eq: ripple-from-form-factor]

$$\boxed{\;\gamma=\sqrt{K_f^{2}-1}\;}$$

[derivation ·L2 p5] **For the half-wave rectifier:**

$$K_f=\frac{I_{LM}/2}{I_{LM}/\pi}=\frac{\pi}{2}=1.571$$

$$\gamma_{\text{HW}}=\sqrt{K_f^2-1}=\sqrt{\left(\frac{\pi}{2}\right)^{2}-1}=\sqrt{1.4674}$$

[eq: hw-ripple]

$$\boxed{\;\gamma_{\text{HW}}=\sqrt{\frac{\pi^{2}}{4}-1}=1.211\;}$$

**Interpretation** ·L2 p5 — the ripple content of a half-wave rectifier's output is **1.21 times
its dc content**. There is more ac in the output than dc. This is why a half-wave rectifier is
almost never used without a filter.

**The harmonic route to the same number** ·L2 p5 — summing the ac harmonics in quadrature:

$$I_{L(ac)}=\sqrt{I_{L1}^{2}+I_{L2}^{2}+I_{L3}^{2}+\cdots}=I_{LM}\sqrt{\left(\frac{1}{2\sqrt2}\right)^{2}+\left(\frac{\sqrt2}{3\pi}\right)^{2}+\left(\frac{\sqrt2}{15\pi}\right)^{2}}=0.385\,I_{LM}$$

$$\gamma=\frac{0.385\,I_{LM}}{0.318\,I_{LM}}=1.21\quad\checkmark$$

[added] **Verified.** $0.125+0.0225157+0.00090064=0.1484163$, whose square root is $0.38525$ ✓ (printed
0.385). $0.385/0.318=1.2107$ ✓. The exact all-harmonic value is
$\sqrt{0.25-1/\pi^2}=0.38559\,I_{LM}$, so three terms already capture 99.9 % of the ripple.

> ⚠ VERIFY **V2.5** ·L2 p5 — the ripple-factor chain opens
> $$\gamma=\frac{I_{L(ac)}}{I_{L(ac)}}=\frac{\sqrt{I_L^2-I_{L(dc)}^2}}{I_{L(dc)}}$$
> The first fraction has **the same symbol above and below the line** and is therefore
> identically 1, contradicting the expression immediately to its right. The denominator should be
> the **dc** value. Correct form:
> $$\boxed{\;\gamma=\frac{I_{L(ac)}}{I_{L(dc)}}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **V2.6** ·L2 p5, p9 — the voltage form is printed
> $$\gamma=\frac{V_{L(ac)}}{V_{L(dc)}}=\frac{V_{r(ms)}}{V_{L(ms)}}$$
> Two faults: "(ms)" is a dropped-"r" rendering of "(rms)", and — the substantive part — the
> **denominator of the second fraction is an rms value where the first fraction has a dc value**.
> Ripple factor is ac-rms over **dc**; dividing by the total rms instead would cap $\gamma$ at 1
> and make it meaningless for the half-wave case, where the true answer is 1.21. The same defect
> recurs on p9 for the full-wave rectifier. **p10 prints it correctly** as
> $\gamma=V_{r(rms)}/V_{L(dc)}$, which settles which form is intended. Correct form:
> $$\boxed{\;\gamma=\frac{V_{L(ac)}}{V_{L(dc)}}=\frac{V_{r(rms)}}{V_{L(dc)}}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C2.7** ·L2 p5 — the quadrature sum prints as
> $I_{L(ac)}=\sqrt{I_{L1}^2+I_{L2}^2+I_{L3}^3+\cdots}$ — the **third term carries a cube**, not a
> square. The arithmetic that follows uses squares throughout and lands on the correct 0.385.
> See `_verification-log.md`.

### (f) Peak inverse voltage ·L2 p5

[def ·L2 p5] **PIV** — the maximum reverse voltage a diode must withstand before it breaks down.
It is the figure to check against the diode's data-sheet reverse rating.

[eq: hw-piv] For the half-wave rectifier the whole secondary appears across the non-conducting
diode:

$$\boxed{\;\mathrm{PIV}_{\text{HW}}=V_{sm}\;}$$

### (g) Transformer utilisation factor ·L2 p6

[def ·L2 p6] **TUF** — the ratio of the dc power delivered to the load to the **ac power rating**
of the transformer secondary. It measures how well the rectifier uses the transformer it is bolted
to. A transformer's rating is set by its rms voltage and rms current, so a rectifier that draws a
peaky, low-duty-cycle current uses the transformer badly.

[derivation ·L2 p6] Neglecting $R_0$ so that $V_{LM}=V_{sm}$:

$$P_{dc}=V_{L(dc)}\,I_{L(dc)}=\frac{V_{LM}}{\pi}\cdot\frac{V_{LM}}{\pi R_L}=\frac{V_{LM}^{2}}{\pi^{2}R_L}$$

$$P_{ac,\text{rated}}=\frac{V_{sm}}{\sqrt2}\cdot\frac{I_{LM}}{2}=\frac{V_{sm}}{\sqrt2}\cdot\frac{V_{LM}}{2R_L}=\frac{V_{sm}^{2}}{2\sqrt2\,R_L}$$

[eq: hw-tuf]

$$\mathrm{TUF}=\frac{V_{sm}^{2}/\pi^{2}R_L}{V_{sm}^{2}/2\sqrt2\,R_L}=\frac{2\sqrt2}{\pi^{2}}$$

$$\boxed{\;\mathrm{TUF}_{\text{HW}}=\frac{2\sqrt2}{\pi^{2}}=0.287\;}$$

**In practice it is worse.** The dc load current also flows through the secondary and **saturates
the transformer core**, so the practical half-wave TUF falls to about **0.2**: a 1 kVA transformer
in a half-wave rectifier delivers only about **200 W** of dc power. ·L2 p6

> ⚠ VERIFY **V2.7** ·L2 p6 — **the TUF derivation loses a factor $\pi$, twice, and the two slips
> cancel in the final number.** The page prints
> $$P_{dc}=\frac{V_{LM}}{\pi}\cdot\frac{V_{LM}}{R_L}=\frac{V_{LM}^{2}}{\pi R_L}\qquad\text{then}\qquad\mathrm{TUF}=\frac{V_{sm}^2/\pi R_L}{V_{sm}^2/2\sqrt2 R_L}=\frac{2\sqrt2}{\pi}=0.287$$
> Two problems. (i) $V_{LM}/R_L$ is $I_{LM}$, **not** $I_{L(dc)}$ — the dc current is
> $V_{LM}/\pi R_L$, so $P_{dc}=V_{LM}^2/\pi^2R_L$. (ii) $2\sqrt2/\pi = 0.900$, not 0.287; the
> quoted 0.287 is $2\sqrt2/\pi^{2}=0.28658$, which is what the corrected $P_{dc}$ gives. Correct
> forms:
> $$\boxed{\;P_{dc}=\frac{V_{LM}^{2}}{\pi^{2}R_L}\;}\qquad\boxed{\;\mathrm{TUF}_{\text{HW}}=\frac{2\sqrt2}{\pi^{2}}=0.2866\;}$$
> Recomputed: $2\sqrt2=2.82843$; $/\pi^2=0.28658$ ✓ matches the printed answer; $/\pi=0.90032$ ✗.
> See `_verification-log.md`.

### [added] Summary card — half-wave rectifier

| Quantity | Symbol | Value |
|---|---|---|
| dc output voltage | $V_{L(dc)}$ | $V_{LM}/\pi=0.318V_{LM}$ |
| rms output voltage | $V_L$ | $V_{LM}/2=0.5V_{LM}$ |
| form factor | $K_f$ | $\pi/2=1.571$ |
| ripple factor | $\gamma$ | $\sqrt{\pi^2/4-1}=1.211$ |
| max efficiency | $\eta_{\max}$ | $4/\pi^2=40.5\,\%$ (quoted 40.6 %) |
| PIV | — | $V_{sm}$ |
| TUF | — | $2\sqrt2/\pi^2=0.287$ (≈0.2 in practice) |
| ripple frequency | $f_r$ | $f$ (same as supply) |
| diodes needed | — | 1 |

### [ex] Example 55.1 — the complete half-wave parameter set ·L2 p6–p7

**Statement** ·L2 p6. In the half-wave rectifier circuit of Fig. 55.4, determine (i) maximum and
rms values of load voltage, (ii) peak and rms values of load current, (iii) power absorbed by the
load, (iv) PIV of the diode, (v) rms value of ripple voltage. **Neglect resistance of transformer
secondary and that of the diode.**

[fig ·L2 p6] **Fig. 55.4.** A circular ac source marked **220 V** drives the primary of a
transformer marked **10 : 1** (polarity dots on the upper end of each winding). The secondary's
upper terminal is marked **+** and carries $V_{sm}$; from it the **diode D** runs rightwards with
its **anode on the left, cathode on the right**; the right-hand vertical rail carries
**$R_L=100\ \Omega$** down to the secondary's lower terminal, marked **−**. A single loop, one
diode, one resistor.

[derivation ·L2 p6–p7] **Solution.**

Turns ratio $K = N_2/N_1 = 1/10$, so the peak primary voltage is

$$V_{pm}=220\sqrt2=310\ \mathrm{V}\qquad\Longrightarrow\qquad V_{sm}=K\,V_{pm}=\frac{310}{10}=31\ \mathrm{V}$$

**(i)** With both resistances neglected, $V_{LM}=V_{sm}=31\ \mathrm{V}$, and

$$V_L=\frac{V_{LM}}{2}=\frac{31}{2}=15.5\ \mathrm{V}$$

**(ii)**

$$I_{LM}=\frac{V_{LM}}{R_L}=\frac{31}{100}=0.31\ \mathrm{A}\qquad I_L=\frac{I_{LM}}{2}=0.155\ \mathrm{A}$$

**(iii)**

$$P_L=V_L\,I_L=15.5\times0.155=2.4\ \mathrm{W}$$

**(iv)** PIV $=2V_{sm}=2\times31=62\ \mathrm{V}$ — **as printed; see V2.8.**

**(v)**

$$V_{L(ac)}=\sqrt{V_L^{2}-V_{L(dc)}^{2}}=V_{LM}\sqrt{\left(\tfrac12\right)^2-\left(\tfrac1\pi\right)^2}=0.385\,V_{LM}=0.385\times31=11.9\ \mathrm{V}$$

> ⚠ VERIFY **V2.8** ·L2 p7 — part (iv) prints **PIV $=2V_{sm}=2\times31=62$ V** for a **half-wave**
> rectifier. $2V_{sm}$ is the PIV of a **centre-tapped full-wave** rectifier, where the idle diode
> sees both half-secondaries in series. In a half-wave rectifier the reverse-biased diode has only
> the one secondary winding across it, and **p5 of this same handout states PIV $=V_{sm}$**.
> Correct answer:
> $$\boxed{\;\mathrm{PIV}=V_{sm}=31\ \mathrm{V}\;}$$
> See `_verification-log.md`.

[added] **Arithmetic verified.** $220\sqrt2=311.13$ (printed 310 — rounded down, 0.4 % low);
$310/10=31.0$ ✓; $31/2=15.5$ ✓; $31/100=0.31$ ✓; $0.31/2=0.155$ ✓;
$15.5\times0.155=2.4025$ → 2.4 W ✓; $\sqrt{0.25-1/\pi^2}=0.385589$, $\times31=11.953$ → 11.9 V ✓
(the page's 0.385 rounding gives 11.935). Carrying the exact $V_{sm}=31.11$ V instead would give
15.56 V, 0.311 A, 0.156 A, 2.42 W and 12.0 V — all within a rounding step of the printed answers.

> ⚠ VERIFY **C2.8** ·L2 p6, p9, p10, p22 — **the $\sqrt2$ and the 220 keep dropping out of peak-value
> lines.** p6 prints it correctly ($V_{pm}=220\sqrt2=310$ V); but p9 prints
> "$V_{pm}=220=312$ V", p10 prints "$V_{sm}=300=424$ V", and p22 prints
> "$V_{dc}=2V_m=2\times\sqrt2=620$ V" (where the 220 has gone instead). In every case **the
> numerical answer is right** — $220\sqrt2=311.1$, $300\sqrt2=424.3$, $2\times220\sqrt2=622.3$ —
> so this is a typesetting drop, not an arithmetic error. Note the two roundings, though: 310 V on
> p6 and 312 V on p9 are the *same* quantity rounded in opposite directions. See
> `_verification-log.md`.

---

## 2.7 Single-phase full-wave centre-tapped rectifier ·L2 p7–p10

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{MG},V_{GN}$ | peak voltage of each half-secondary about the centre tap | V | 78 (Ex 55.3) |
| $V_{MN}$ | peak voltage across the whole secondary | V | 156 |
| $G$ | centre tap — the zero-voltage (ground) reference | — | — |
| $I_{D(av)}$ | average current in **one** diode | A | $I_{LM}/\pi$ |
| $V_R$ | voltage regulation | — | $R_0/R_L$ |

[def ·L2 p7] **Full-wave rectification.** Both half-cycles of the input are used, by two diodes
working alternately. **A transformer is essential** for full-wave rectification (it is optional for
half-wave), because the two diodes need two supplies in antiphase.

The centre-tapped version splits the secondary into two equal halves about a tap $G$, which is
**usually taken as the ground or zero-voltage reference point**. ·L2 p7

[fig ·L2 p7] **Fig. 55.7 — the centre-tapped circuit, drawn two ways.** In both:

- The secondary runs from **M** (top, marked $\pm$) through the **centre tap G** to **N** (bottom,
  marked $\mp$). $V_{SM}$ is the peak voltage of **each half**, M-to-G and G-to-N.
- **$D_1$** takes the top wire out of M — **anode at M, cathode to the right**.
- **$D_2$** takes the bottom wire out of N — **anode at N, cathode to the right**.
- The two cathodes join at **C**, the positive output terminal. $R_L$ returns from C to G.
- **(a)** shows $R_L$ connected to G **via the earth symbol** (both G and the bottom of $R_L$ are
  earthed); **(b)** shows $R_L$ connected **directly to G**, no earth. Electrically identical.

[fig ·L2 p7] **Fig. 55.6(b) — the four waveform panels, stacked on a common time axis.**

1. **$V_s$** — a complete sinusoid of peak $V_{SM}$.
2. **"Output of $D_1$ & $D_3$"** — positive humps occupying the **positive** half-cycles only,
   flat zero in between.
3. **"Output of $D_2$ & $D_4$"** — positive humps occupying the **negative** half-cycles, i.e.
   interleaved with panel 2, filling exactly the gaps.
4. **$V_L$, captioned "Totol Output"** — the two interleaved trains superposed: a **continuous
   run of positive humps of peak $V_{LM}$ with no gaps**, touching zero only instantaneously at
   each supply zero-crossing. The ripple frequency is **twice** the supply frequency.

> ⚠ VERIFY **V2.9** ·L2 p7, p11 — **the figure printed as Fig. 55.6(a) is the wrong circuit.**
> Article 55.7 announces "the full-wave rectifier circuit using **two diodes and a centre-tapped
> transformer** shown in 55.6(a)", but the figure under that label shows a **four-diode bridge**:
> a diamond of $D_1$–$D_4$ between nodes E (top), A (right), F (bottom), C (left), with the
> secondary M–N feeding E and F and the load hung between A and C. Its own waveform panels are
> labelled "Output of $D_1$ & $D_3$" and "Output of $D_2$ & $D_4$" — four diodes, not two. That
> circuit belongs to Art. 55.8, whose figure (Fig. 55.10) is **missing** from the handout. The
> genuine centre-tapped circuit appears one figure later as **Fig. 55.7**. A reader working from
> Fig. 55.6(a) will draw a bridge when asked for a centre-tap rectifier — and will then get the
> PIV wrong, since bridge PIV is $V_{sm}$ but centre-tap PIV is $2V_{sm}$. See
> `_verification-log.md`.

> ⚠ VERIFY **C2.9** ·L2 p7, p8 — a cluster of small typographic faults on these two pages: the
> Fig. 55.6(b) caption reads "**Totol** Output"; the sentence introducing Fig. 55.7(b) ends
> mid-clause ("...whereas in Fig. 55.7 (b). It is connected directly to G"); p8 cites "**Fig.
> 5.8**" for Fig. 55.8; and p8 opens a sentence "As proved earlier in and now shown in
> Fig. 5.8..." with the cross-reference missing. None affects the physics. See
> `_verification-log.md`.

### 2.7.1 Working ·L2 p7–p8

- **Positive half-cycle** — M is positive with respect to G, so $D_1$ is forward-biased and
  conducts; $D_2$ is reverse-biased. Current path: **M → $D_1$ → C → $R_L$ → G → back to M**
  (the handout writes it $M\,D_1\,C\,A\,B\,G$).
- **Negative half-cycle** — N is positive with respect to G, so $D_2$ conducts and $D_1$ is off.
  Current path: **N → $D_2$ → C → $R_L$ → G → back to N** ($N\,D_2\,C\,A\,B\,G$).
- **In both half-cycles the load current flows in the same direction**, from C through $R_L$ to G.
  That is the whole trick of full-wave rectification.

### 2.7.2 Average and rms values ·L2 p8

[derivation] The output is now $|V_{LM}\sin\omega t|$ — the sine's magnitude, present for the
*whole* period. Averaging over a half-period (which is a full output period):

$$V_{L(dc)}=\frac{1}{\pi}\int_0^{\pi}V_{LM}\sin\theta\,d\theta=\frac{2V_{LM}}{\pi}$$

[eq: fw-vdc][eq: fw-vrms]

$$\boxed{\;V_{L(dc)}=\frac{2V_{LM}}{\pi}=0.636\,V_{LM}\;}\qquad\boxed{\;V_L=\frac{V_{LM}}{\sqrt2}=0.707\,V_{LM}\;}$$

$$\boxed{\;I_{L(dc)}=\frac{2I_{LM}}{\pi}=0.636\,I_{LM}\;}\qquad\boxed{\;I_L=\frac{I_{LM}}{\sqrt2}=0.707\,I_{LM}\;}$$

with $I_{LM}=V_{LM}/R_L$ and, as before,

$$I_{L(ac)}=\sqrt{I_L^{2}-I_{L(dc)}^{2}}=I_{r(rms)}$$

**Every dc quantity is exactly twice its half-wave value**, because the same charge is delivered
twice as often; the rms value rises by $\sqrt2$, because the mean square doubles.

> ⚠ VERIFY **C2.10** ·L2 p8 — the dc line prints "$V_{L(dc)}=2V_{LM}/\pi=0.636$ **V**". The
> trailing "V" is the remains of "$V_{LM}$" with its subscript lost, so the line reads as though
> the answer were 0.636 volts. Correct: $V_{L(dc)}=0.636\,V_{LM}$. See `_verification-log.md`.

[fig ·L2 p8] **Fig. 55.8 — the dc and ac content of the full-wave output, two panels.**

- **(a)** ordinate $V_L$, abscissa $t$: a **continuous train of positive humps of peak $V_{LM}$**,
  each touching zero at its ends, with **no flat gaps**. A **dashed horizontal line** at
  $0.636V_{LM}$ is labelled $V_L$ (dc); the region between that line and the curve is **shaded**
  and labelled $V_L$ (ac); a separate arrow labelled $V_L$ points at the curve itself.
- **(b)** the identical picture for current, ordinate $i_L$, peak $I_{LM}$, dc line at
  $0.636I_{LM}$ labelled $I_L$ (dc).

> ⚠ VERIFY **C2.11** ·L2 p8 — in **Fig. 55.8(b)**, the *current* graph, the shaded ripple region
> is labelled "$V_L$ **(ac)**" — the voltage symbol on a current axis. It should read $I_L$ (ac),
> as the neighbouring $I_L$ (dc) label on the same panel does. See `_verification-log.md`.

### 2.7.3 Rectification efficiency ·L2 p8

[derivation ·L2 p8]

$$P_{in}=I_L^{2}(R_0+R_L)=\left(\frac{I_{LM}}{\sqrt2}\right)^{2}(R_0+R_L)=\frac{I_{LM}^{2}}{2}(R_0+R_L)$$

$$P_{dc}=I_{L(dc)}^{2}R_L=\left(\frac{2I_{LM}}{\pi}\right)^{2}R_L=\frac{4I_{LM}^{2}}{\pi^{2}}R_L$$

[eq: fw-efficiency]

$$\boxed{\;\eta_{\text{FW}}=\frac{8}{\pi^{2}}\cdot\frac{R_L}{R_0+R_L}=\frac{81.1\,\%}{1+R_0/R_L}\;}$$

With $R_0$ neglected, $\eta_{\max}=8/\pi^2=0.8106=\mathbf{81.1\,\%}$ (the handout quotes
**81.2 %** — see C2.4). **Exactly twice the half-wave figure**, which is the single most useful
sanity check on this whole section.

> ⚠ VERIFY **V2.10** ·L2 p8 — the dc-power line prints
> $$P_{dc}=I_{L(dc)}^{2}(R_0+R_L)$$
> with the **total** series resistance where the **load** resistance belongs. $P_{dc}$ is by
> definition the dc power *delivered to the load*, so it must be $I_{L(dc)}^2R_L$ — and the very
> next line's result, $\eta=\dfrac{8}{\pi^2}\dfrac{R_L}{R_0+R_L}$, can only be reached that way:
> with $(R_0+R_L)$ in both numerator and denominator the ratio would collapse to the constant
> $8/\pi^2$ and the $R_L/(R_0+R_L)$ factor would vanish. Correct form:
> $$\boxed{\;P_{dc}=I_{L(dc)}^{2}R_L\;}$$
> See `_verification-log.md`.

### 2.7.4 Frequency components ·L2 p9

[eq: fw-fourier] **Fourier series of the full-wave rectified voltage** ·L2 p9

$$\boxed{\;V_L=V_{LM}\left(\frac{2}{\pi}-\frac{4}{3\pi}\cos2\omega t-\frac{4}{15\pi}\cos4\omega t-\frac{4}{35\pi}\cos6\omega t-\cdots\right)\;}$$

- **There is no fundamental**, and no odd harmonic: the lowest ac component is at $2f$. That is
  why a full-wave rectifier is so much easier to filter than a half-wave one.
- dc term: $V_{L(dc)}=2V_{LM}/\pi=0.636V_{LM}$ ✓
- lowest ripple harmonic, rms: $V_{L1}=\dfrac{4V_{LM}}{3\pi\sqrt2}=0.300\,V_{LM}$
- next, rms: $V_{L2}=\dfrac{4V_{LM}}{15\pi\sqrt2}=0.0600\,V_{LM}$

> ⚠ VERIFY **V2.11** ·L2 p9 — the third ripple term is printed $-\dfrac{4}{35}\cos6\omega t$; every
> other term of the series carries a $\pi$ in the denominator and this one **must too**. The
> general term of the full-wave series is $-\dfrac{4}{\pi(n^2-1)}\cos n\omega t$ for even $n$,
> giving $4/3\pi$, $4/15\pi$, $4/35\pi$. As printed the coefficient is $\pi=3.14$ times too large:
> $4/35=0.1143$ against the correct $4/35\pi=0.0364$. Correct form:
> $$\boxed{\;-\frac{4}{35\pi}\cos6\omega t\;}$$
> See `_verification-log.md`.

### 2.7.5 Ripple factor ·L2 p9

[derivation ·L2 p9] Summing the two quoted harmonics in quadrature:

$$V_{L(ac)}=\sqrt{V_{L1}^{2}+V_{L2}^{2}}=V_{LM}\sqrt{0.300^{2}+0.0600^{2}}=0.306\,V_{LM}$$

$$\gamma_{\text{FW}}=\frac{V_{L(ac)}}{V_{L(dc)}}=\frac{0.306}{0.636}=0.48$$

[eq: fw-ripple] and exactly, from the form factor $K_f=0.707/0.636=\pi/2\sqrt2=1.1107$:

$$\boxed{\;\gamma_{\text{FW}}=\sqrt{\frac{\pi^{2}}{8}-1}=0.483\;}$$

**Interpretation.** The ripple content falls from **1.21** (half-wave) to **0.48** (full-wave) —
a factor of 2.5 improvement, and the second reason full-wave is preferred.

> ⚠ VERIFY **C2.12** ·L2 p9 — three small numerical/typographic slips in the ripple paragraph.
> (i) The second harmonic is written "$4V_{IM}$" — subscript **IM** for **LM**. (ii) The quadrature
> sum is printed $0.305\,V_{LM}$; recomputing, $\sqrt{0.300105^2+0.0600211^2}=0.30605$, so
> **0.306**. (iii) The ripple factor is then printed **0.482**, but $0.305/0.636=0.4796$ and
> $0.306/0.636=0.4811$ — neither is 0.482. The **exact** value, from all harmonics, is
> $\sqrt{\pi^2/8-1}=0.4834$, which is the number to quote. See `_verification-log.md`.

### 2.7.6 PIV and TUF ·L2 p9

[eq: fw-piv] While one diode conducts, the other has **both half-secondaries in series** across it:

$$\boxed{\;\mathrm{PIV}_{\text{centre-tap}}=2V_{sm}\;}$$

where $V_{sm}$ is the peak of **one half** of the secondary. This is the centre-tap circuit's chief
drawback: the diodes must be rated at twice the peak they rectify.

[eq: fw-tuf]

$$\boxed{\;\mathrm{TUF}_{\text{centre-tap}}=0.693\;}$$

Better than the half-wave 0.287, but still not 1, because each half of the secondary works for only
half the time. ·L2 p9

### [ex] Example 55.3 — full parameter set for a centre-tap rectifier ·L2 p9–p10

**Statement** ·L2 p9. With reference to the full-wave rectifier of Fig. 55.9, determine (i) peak,
dc component, rms and ac component of load voltage, (ii) the same four for load current,
(iii) ripple factor, (iv) peak and average diode currents, (v) total power supplied to the load.
**Neglect diode and secondary winding resistances.**

[fig ·L2 p9] **Fig. 55.9.** A circular ac source marked **220 V** feeds a **2 : 1** transformer.
The secondary runs **M** (top) — **centre tap** — **N** (bottom), with a $V_{SM}$ arrow **upward**
from the tap to M and a second $V_{SM}$ arrow **downward** from the tap to N. From M, **$D_1$**
runs right (anode left, cathode right) with a current arrow pointing right; from N, **$D_2$** runs
right in the same orientation. Both cathodes meet the right-hand vertical rail, which comes back
leftwards to node **C**. **$R_L=100\ \Omega$** is drawn **horizontally from the centre tap to C**,
with a leftward current arrow at C. Two curved pink arrows at the tap show the two conduction
paths.

[derivation ·L2 p9–p10] **Solution.** $K=1/2$, so

$$V_{pm}=220\sqrt2=312\ \mathrm{V},\qquad V_{MN}=\frac{312}{2}=156\ \mathrm{V},\qquad V_{MG}=V_{GN}=\frac{156}{2}=78\ \mathrm{V}$$

**(i)** $V_{sm}=V_{LM}=78\ \mathrm{V}$

$$V_{L(dc)}=0.636\times78=49.6\ \mathrm{V}\qquad V_L=0.707\times78=55\ \mathrm{V}$$

$$V_{L(ac)}=\sqrt{V_L^2-V_{L(dc)}^2}=\sqrt{55^{2}-49.6^{2}}=23.8\ \mathrm{V}$$

**(ii)**

$$I_{LM}=\frac{78}{100}=0.78\ \mathrm{A},\qquad I_{L(dc)}=0.636\times0.78=0.496\ \mathrm{A},\qquad I_L=0.707\times0.78=0.55\ \mathrm{A}$$

$$I_{L(ac)}=\sqrt{I_L^2-I_{L(dc)}^2}=\sqrt{0.55^{2}-0.496^{2}}=0.238\ \mathrm{A}$$

**(iii)**

$$\gamma=\frac{I_{r(rms)}}{I_{L(dc)}}=\frac{0.238}{0.496}=0.48$$

**(iv)** Peak diode current = peak load current = **0.78 A**. Each diode carries current for **one
half-cycle only**, so its average is the *half-wave* average of the peak:

$$I_{D(av)}=\frac{I_{D(\max)}}{\pi}=0.318\times0.78=0.25\ \mathrm{A}$$

**(v)** $P_L=V_L I_L=55\times0.55=30.25\ \mathrm{W}$

> ⚠ VERIFY **V2.12** ·L2 p9 — part (ii) prints
> $$I_{L(ac)}=\sqrt{0.55^{2}-49.6^{2}}=0.238\ \mathrm{A}$$
> The second term is the **voltage** 49.6 V, not the current 0.496 A — the decimal point has moved
> two places. As printed the radicand is $0.3025-2460.2=-2459.9$, so the expression has **no real
> value**; the quoted answer 0.238 A is the one the correct radicand gives. Correct form:
> $$\boxed{\;I_{L(ac)}=\sqrt{0.55^{2}-0.496^{2}}=\sqrt{0.0565}=0.2377\ \mathrm{A}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **V2.13** ·L2 p9 — part (iii) prints the ripple factor as
> $\gamma = I_{L(ac)}/I_{L(dc)} = I_{r(\mathbf{max})}/I_{L(\mathbf{max})}$. Both subscripts are
> wrong: the numerator is the **rms** ripple current and the denominator the **dc** load current —
> which is exactly what the numbers 0.238 and 0.496 are. Using peak values instead would give
> $I_{LM}/I_{LM}=1$. Correct form:
> $$\boxed{\;\gamma=\frac{I_{r(rms)}}{I_{L(dc)}}\;}$$
> See `_verification-log.md`.

[added] **Arithmetic verified.** $220\sqrt2=311.13$ (printed 312 — rounded up); $312/2=156$ ✓;
$156/2=78$ ✓; $0.636\times78=49.61$ ✓; $0.707\times78=55.15$ → 55 ✓;
$\sqrt{55^2-49.6^2}=23.77$ → 23.8 ✓; $78/100=0.78$ ✓; $0.636\times0.78=0.4961$ ✓;
$0.707\times0.78=0.5515$ → 0.55 ✓; $\sqrt{0.55^2-0.496^2}=0.23766$ → 0.238 ✓;
$0.238/0.496=0.4798$ → 0.48 ✓ (exact $\gamma=0.4834$); $0.318\times0.78=0.2480$ → 0.25 ✓;
$55\times0.55=30.25$ ✓. Every printed answer is right; only the two symbolic slips above are wrong.

### [ex] Example 55.4 — regulation-style arithmetic with diode resistance ·L2 p10

**Statement** ·L2 p10. A 1-$\phi$ full-wave rectifier supplies power to a **1 kΩ** load. The ac
voltage applied to the diodes is **300-0-300 V (rms)**. If diode resistance is **25 Ω** and that of
the transformer secondary is negligible, determine (i) average load current, (ii) average value of
load voltage, (iii) rms value of ripple, (iv) efficiency.
*(Applied Electronics, Bombay Univ.)*

[derivation ·L2 p10] **Solution.** The rms voltage across **each secondary half** is 300 V, so

$$V_{sm}=300\sqrt2=424\ \mathrm{V}$$

**(i)**

$$I_{LM}=\frac{V_{sm}}{r_d+R_L}=\frac{424}{25+1000}=\frac{424}{1025}=0.414\ \mathrm{A}$$

$$I_{L(dc)}=\frac{2I_{LM}}{\pi}=\frac{2\times0.414}{\pi}=0.263\ \mathrm{A}$$

**(ii)** $V_{L(dc)}=I_{L(dc)}R_L=0.263\times1000=263\ \mathrm{V}$

**(iii)**

$$\gamma=\frac{V_{L(ac)}}{V_{L(dc)}}=\frac{V_{r(rms)}}{V_{L(dc)}}\quad\Longrightarrow\quad V_{r(rms)}=\gamma\,V_{L(dc)}=0.482\times263=126.8\ \mathrm{V}$$

**(iv)**

$$\eta=\frac{81.2\,\%}{1+r_d/R_L}=\frac{81.2\,\%}{1+25/1000}=\frac{81.2}{1.025}=79.2\,\%$$

> ⚠ VERIFY **V2.14** ·L2 p10 — part (i) prints the symbolic step as
> $$I_{L(dc)}=\frac{I_{LM}}{\pi}=\frac{2\times0.414}{\pi}=0.263\ \mathrm{A}$$
> **The symbolic form has lost its factor 2** while the arithmetic beside it keeps it. For a
> full-wave rectifier $I_{L(dc)}=2I_{LM}/\pi$; $I_{LM}/\pi$ is the *half-wave* result and would
> give 0.132 A, half the printed answer. Correct form:
> $$\boxed{\;I_{L(dc)}=\frac{2I_{LM}}{\pi}=0.636\,I_{LM}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C2.13** ·L2 p10 — the statement reads "supplies power to a **1 k W** load" and "diode
> resistance is **25 W**". The **ohm sign Ω has been substituted by a roman W** by the font — a
> load specified in watts and a resistance in watts are both meaningless, and the solution uses
> $R_L=1000\ \Omega$ and $r_d=25\ \Omega$ throughout. Read every stray "W" after a resistance value
> in this handout as Ω. The statement also ends "determine\"" with a stray closing quote for a
> colon. See `_verification-log.md`.

[added] **Arithmetic verified.** $300\sqrt2=424.26$ ✓; $424/1025=0.41366$ → 0.414 ✓;
$2\times0.414/\pi=0.26355$ → 0.263 ✓; $\times1000=263$ V ✓; $0.482\times263=126.77$ → 126.8 ✓
(with the exact $\gamma=0.4834$ it would be 127.1 V); $81.2/1.025=79.22$ → 79.2 % ✓ (with the
exact $8/\pi^2$ it would be 79.08 %).

### 2.7.7 [ex] Example 55.5 — and the missing Example 55.2 ·L2 p10

**Statement** ·L2 p10. A full-wave rectifier is built up using **the same components as in
Ex. 55.2**. Determine (i) dc load current, (ii) dc load voltage, (iii) voltage regulation,
(iv) circuit efficiency, (v) diode PIV and current rating.

> ⚠ VERIFY **C2.14** ·L2 p10 — **Example 55.2 does not exist in this handout.** The pages run
> 55.1 (p6) → 55.3 (p9) → 55.4 (p10) → 55.5 (p10). Example 55.5 is therefore unsolvable as
> printed: its solution silently uses $I_{LM}=1.88$ A, $R_L=10\ \Omega$, $R_0=0.25\ \Omega$ and
> $V_{sm}=20$ V, none of which appears anywhere in the 26 pages. See the reconstruction below and
> `_verification-log.md`.

[derivation ·L2 p10] **Solution as printed.**

$$I_{L(dc)}=0.636\times1.88=1.2\ \mathrm{A}$$
$$V_{L(dc)}=I_{L(dc)}R_L=1.2\times10=12\ \mathrm{V}$$
$$V_R=\frac{R_0}{R_L}=\frac{0.25}{10}=0.025\ \text{or}\ 2.5\,\%$$
$$\eta=\frac{81.2\,\%}{1+R_0/R_L}=\frac{81.2\,\%}{1+0.25/10}=79.2\,\%$$
$$\mathrm{PIV}=2V_{sm}=2\times20=40\ \mathrm{V}$$

With a safety factor of 1.5, PIV $=40\times1.5=60$ V, and a dc current rating of about **2 A**
would be satisfactory.

[added] **Reconstruction of Example 55.2 — supplied here, NOT in the handout.** The four data the
solution uses are mutually consistent with exactly one half-wave circuit, and it can be recovered:

$$I_{LM}=\frac{V_{sm}-V_B}{R_0+R_L}\quad\Longrightarrow\quad 1.88=\frac{20-V_B}{0.25+10}\quad\Longrightarrow\quad V_B=20-1.88\times10.25=0.73\ \mathrm{V}$$

$V_B\approx0.7$ V is the **silicon** barrier voltage, and with it exactly

$$I_{LM}=\frac{20-0.7}{10.25}=1.883\ \mathrm{A}\quad\checkmark$$

So **Example 55.2 was a rectifier with a silicon diode, a peak secondary voltage of 20 V, a load
of 10 Ω and a total series resistance $R_0=R_S+r_d=0.25\ \Omega$**, giving $I_{LM}=1.88$ A. (Note
that $20/10.25=1.95$ A — dropping $V_B$ does *not* reproduce 1.88 A, so the silicon drop must have
been in the original.) Example 55.5 then re-uses those components in a full-wave circuit.

[added] **The voltage-regulation formula, derived.** The handout uses $V_R=R_0/R_L$ without
proof. For a full-wave rectifier,

$$V_{L(dc)}=\frac{2I_{LM}}{\pi}R_L=\frac{2V_{sm}}{\pi}\cdot\frac{R_L}{R_0+R_L}$$

so the no-load value ($R_L\to\infty$) is $V_{NL}=2V_{sm}/\pi$ and

[eq: voltage-regulation]

$$V_R=\frac{V_{NL}-V_{FL}}{V_{FL}}=\frac{\dfrac{2V_{sm}}{\pi}-\dfrac{2V_{sm}}{\pi}\dfrac{R_L}{R_0+R_L}}{\dfrac{2V_{sm}}{\pi}\dfrac{R_L}{R_0+R_L}}=\frac{R_0+R_L}{R_L}-1$$

$$\boxed{\;V_R=\frac{R_0}{R_L}\;}$$

A **perfect** supply has $V_R=0$; the smaller $R_0$ is compared with $R_L$, the stiffer the supply.

[added] **Arithmetic verified.** $0.636\times1.88=1.1957$ → 1.2 A ✓ (exact $2\times1.88/\pi=1.1968$);
$1.2\times10=12$ V ✓; $0.25/10=0.025=2.5\,\%$ ✓; $81.2/1.025=79.22$ → 79.2 % ✓;
$2\times20=40$ V ✓; $40\times1.5=60$ V ✓.

### [added] Summary card — centre-tapped full-wave rectifier

| Quantity | Symbol | Value | vs half-wave |
|---|---|---|---|
| dc output voltage | $V_{L(dc)}$ | $2V_{LM}/\pi=0.636V_{LM}$ | ×2 |
| rms output voltage | $V_L$ | $V_{LM}/\sqrt2=0.707V_{LM}$ | ×$\sqrt2$ |
| form factor | $K_f$ | $\pi/2\sqrt2=1.111$ | better |
| ripple factor | $\gamma$ | $\sqrt{\pi^2/8-1}=0.483$ | 2.5× better |
| max efficiency | $\eta_{\max}$ | $8/\pi^2=81.1\,\%$ (quoted 81.2 %) | ×2 |
| PIV | — | $2V_{sm}$ | ×2 **worse** |
| TUF | — | 0.693 | 2.4× better |
| ripple frequency | $f_r$ | $2f$ | ×2 (easier to filter) |
| diodes needed | — | 2 | ×2 |

---

## 2.8 Full-wave bridge rectifier ·L2 p11–p12

[def ·L2 p11] **The bridge rectifier** is the most frequently used circuit for electronic dc power
supplies. It needs **four diodes**, but the transformer is **not centre-tapped** and its peak
voltage is only $V_{sm}$. It comes in three physical forms:

1. four discrete diodes;
2. one device inside a **four-terminal case**;
3. as part of a **diode array in an IC**.

[fig ·L2 p7, p11] **The bridge circuit** — described from the figure printed as Fig. 55.6(a) on p7
and repeated as Fig. 55.11 on p11 (see V2.9 for the labelling fault).

Draw a **diamond** with four corners:

- **E** at the top, **A** at the right, **F** at the bottom, **C** at the left.

Place one diode in each arm, all pointing "towards A and away from C":

| Arm | Diode | Anode | Cathode |
|---|---|---|---|
| C → E | $D_4$ | C | E |
| E → A | $D_1$ | E | A |
| C → F | $D_3$ | C | F |
| F → A | $D_2$ | F | A |

So **A is the common-cathode node** (of $D_1$ and $D_2$) and **C the common-anode node** (of $D_3$
and $D_4$).

- The transformer secondary **M** (top, $\pm$) connects to **E**; **N** (bottom, $\mp$) connects to
  **F**. These are the **ac input corners**.
- The load $R_L$ hangs from **A** down to **B**; **B runs along the bottom to C**, its wire
  **hopping over** the N–F wire (a semicircular jump marks the crossing — no connection there).
  A and C are the **dc output corners**, A positive.

In Fig. 55.11 the four diodes are redrawn as **switch symbols** — closed (bar bridging the two
contacts) for the conducting pair, open (bar lifted) for the blocking pair.

### Working ·L2 p11

- **Positive half-cycle** — M positive, N negative [Fig. 55.11(a)]. $D_1$ and $D_3$ are
  **forward-biased (ON)**; $D_2$ and $D_4$ **reverse-biased (OFF)**. Current flows
  $$M\to E\to D_1\to A\to R_L\to B\to C\to D_3\to F\to N$$
  which the handout writes **$MEABCFN$**.
- **Negative half-cycle** — N positive, M negative [Fig. 55.11(b)]. $D_2$ and $D_4$ conduct:
  $$N\to F\to D_2\to A\to R_L\to B\to C\to D_4\to E\to M$$
  written **$NFABCEM$**.
- In both half-cycles the load current runs **A → B**, i.e. always the same way through $R_L$.
- Output ripple frequency is **twice** the supply frequency. ·L2 p11

> ⚠ VERIFY **C2.15** ·L2 p11 — the summary sentence reads "point A of the bridge rectifier always
> acts as an **anode** and point C as **cathode**." In diode-terminal language this is **the
> opposite way round**: A is where the *cathodes* of $D_1$ and $D_2$ meet, and C is where the
> *anodes* of $D_3$ and $D_4$ meet. What the sentence means is that **A is the positive dc output
> terminal and C the negative** — true, and the useful thing to remember. Also on this page:
> "three distinct **physics** forms" for *physical* forms, and two references to the missing
> Fig. 55.10 (V2.9). See `_verification-log.md`.

### Parameters ·L2 p11–p12

**(b) Average and rms values** — identical to the centre-tapped full-wave rectifier of §2.7.

**(c)** [eq: bridge-efficiency] Efficiency, with **two** diodes in series at every instant:

$$\boxed{\;\%\eta=\frac{81.2\,\%}{1+2r_d/R_L}\;}$$

**(d)** Ripple factor: the same as any full-wave rectifier, $\gamma=0.482$ (exactly 0.483).

**(e)** [eq: bridge-piv] PIV:

$$\boxed{\;\mathrm{PIV}_{\text{bridge}}=V_{sm}\;}$$

— the entire secondary voltage, and **half** the centre-tap circuit's requirement for the same
output. This is the bridge's main technical advantage.

**When secondary and diode resistances are considered** ·L2 p12 — note the **2** in front of both
$V_B$ and $r_d$, because two diodes are always in series:

[eq: bridge-peak-current]

$$\boxed{\;I_{LM}=\frac{V_{sm}-2V_B}{(R_S+2r_d)+R_L}=\frac{V_{sm}-2V_B}{R_0+R_L}\;}\qquad V_{LM}=I_{LM}R_L$$

$$\eta=\left(\frac{8}{\pi^{2}}\right)\frac{R_L}{R_S+2r_d+R_L}=\left(\frac{8}{\pi^{2}}\right)\frac{R_L}{R_0+R_L}\qquad V_R=\frac{R_S+2r_d}{R_L}=\frac{R_0}{R_L}$$

> **Notation warning.** $R_0$ is **redefined** on p12. For the half-wave rectifier (p3)
> $R_0=R_S+r_d$; for the bridge (p12) $R_0=R_S+2r_d$. The symbol always means "everything in series
> apart from the load", but the number of diode resistances inside it depends on the circuit.
> Check which circuit a given $R_0$ belongs to before substituting.

### (f) Advantages and the one disadvantage ·L2 p12

Since low-cost, highly reliable, small silicon diodes became available, the bridge has become far
more popular than the centre-tapped full-wave rectifier. The main reason: **a much smaller
transformer** does the same job, because the bridge **uses the secondary continuously**, whereas
the two-diode circuit uses each half of the secondary only alternately. It is therefore the circuit
of choice in **high-power applications**.

1. no centre-tap is required on the transformer;
2. much smaller transformers are required;
3. it is suitable for **high-voltage** applications;
4. it has **less PIV rating per diode**.

**Disadvantage** — it needs **twice as many diodes** as the centre-tapped version, and **two of
them conduct in series at every instant**, so the total forward voltage drop is doubled (this is
why the $2V_B$ appears in $I_{LM}$ above). Cheap silicon diodes have made it economical
nonetheless. ·L2 p12

---

## 2.9 Three-phase half-wave rectifier ·L2 p12–p13

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{sm}$ | peak phase voltage of the star-connected secondary | V | — |
| $V_s$ | rms phase voltage | V | $V_{sm}/\sqrt2$ |
| $t_1\ldots t_4$ | the successive 120° conduction intervals | s | $T/3$ |

[def ·L2 p12] **Three-phase half-wave rectification.** One diode per phase, all cathodes tied
together; each diode conducts for the third of a cycle during which its own phase voltage is the
highest of the three. The output is the **upper envelope** of the three phase voltages.

[fig ·L2 p12] **Fig. 55.12 — the circuit.** Left to right:

- a **delta-connected primary** — three windings drawn as the three sides of a triangle, with
  three supply terminals;
- a **star-connected secondary** — three windings meeting at a common **neutral N**, which is
  earthed;
- from each secondary phase end, a diode — **$D_1$, $D_2$, $D_3$**, each drawn inside a small
  circle, **anode at the winding, cathode to the common positive rail**;
- from the positive rail, a **C-L-C ($\pi$) filter**: capacitor **$C_1$** to the earthed rail, then
  a series **choke** in the top wire, then capacitor **$C_2$** to the earthed rail;
- the dc output terminals at the far right, **+ at the top**, **− at the bottom** (the neutral).

[fig ·L2 p12] **Fig. 55.13 — the output waveform.** Three sinusoids **120° apart**, drawn on one
pair of axes A–B (horizontal) with the vertical axis at the left. Each sinusoid's positive crest is
labelled **$D_1$, $D_2$, $D_3$** in turn. The portion of each sinusoid that is **the highest of the
three** is drawn **solid**; the rest is **dashed** (including the negative excursions). The solid
segments join at the crossover points to form a **scalloped envelope** that never falls to zero.
**Vertical dashed lines** mark the crossover instants, and the intervals between them are labelled
**$t_1$, $t_2$, $t_3$, $t_4$** by double-headed arrows along the bottom, each **120° wide**.

### Working ·L2 p13

- During $t_1$ only $D_1$ conducts; at the end of $t_1$ it stops and $D_2$ takes over for $t_2$;
  at the end of $t_2$, $D_3$ takes over for $t_3$; and so on cyclically.
- Each diode conducts for **one-third of a cycle**, i.e. **120°**.

> ⚠ VERIFY **C2.16** ·L2 p13 — the conduction narrative is printed "It will cease conducting at
> $t_2$ and then $D_2$ will conduct current **upto $t_2$** after which **$D_2$** will take over and
> will supply anode current till $t_3$." As printed, $D_2$ conducts up to the instant it starts,
> and then hands over to itself. The intended reading is "$D_2$ will conduct up to $t_3$ after
> which **$D_3$** will take over and will supply anode current till $t_4$." Purely a substitution
> slip; the 120°-per-diode physics is standard and correct. See `_verification-log.md`.

### The three numbers ·L2 p13

- **Output swing.** The output never falls to zero: it varies between $V_{sm}$ (at each crest) and
  $0.5V_{sm}$ (at each crossover, where two phases are equal at $V_{sm}\cos60°$).
- [eq: three-phase-hw-vdc] **Mean output**

  $$\boxed{\;V_{L(dc)}=\frac{3\sqrt3}{2\pi}V_{sm}=0.83\,V_{sm}=1.17\,V_s\;}$$

- **Rectification efficiency** ≈ **96.5 %** as printed (exactly 96.8 % — see C2.17).
- **Ripple factor** $\gamma\approx$ **0.17** as printed (0.177 counting only the lowest ripple
  harmonic; 0.183 counting all — see C2.17).
- The pulsations are **smaller than for a single-phase full-wave rectifier because the current
  never touches zero**, and a **C-L-C filter** (Fig. 55.12) smooths them further. ·L2 p13
- **Transformer saturation.** The direct current of each diode appears in its own secondary phase
  winding, which **saturates the transformer core and causes a large primary current**. The cure is
  a **zig-zag secondary**. ·L2 p13

[added] **Both constants derived.** The output is $V_{sm}\cos\theta$ over
$-\pi/3\le\theta\le\pi/3$, repeating three times per supply cycle:

$$V_{L(dc)}=\frac{3}{2\pi}\int_{-\pi/3}^{\pi/3}V_{sm}\cos\theta\,d\theta=\frac{3V_{sm}}{2\pi}\cdot 2\sin\frac{\pi}{3}=\frac{3\sqrt3}{2\pi}V_{sm}=0.8270\,V_{sm}$$

$$V_{L}^{2}=\frac{3}{2\pi}\int_{-\pi/3}^{\pi/3}V_{sm}^{2}\cos^{2}\theta\,d\theta=\frac{3V_{sm}^{2}}{2\pi}\left(\frac{\pi}{3}+\frac{\sqrt3}{4}\right)\quad\Longrightarrow\quad V_L=0.8407\,V_{sm}$$

$$\eta=\left(\frac{V_{L(dc)}}{V_L}\right)^{2}=\left(\frac{0.8270}{0.8407}\right)^{2}=0.9677,\qquad \gamma=\sqrt{\left(\frac{V_L}{V_{L(dc)}}\right)^{2}-1}=0.1827$$

Also $0.8270\times\sqrt2=1.1695$, confirming the printed $1.17\,V_s$ ✓, and
$V_{sm}\cos60°=0.5V_{sm}$ confirming the printed swing ✓.

> ⚠ VERIFY **C2.17** ·L2 p13 — the two figures of merit are printed as **η = 96.5 %** and
> **γ = 0.17**. Recomputing exactly for an ideal three-pulse rectifier with a resistive load gives
> **η = 96.8 %** and **γ = 0.183**. The printed γ is recoverable if only the **lowest ripple
> harmonic** is counted — for a $p$-pulse rectifier that gives
> $\gamma_1=\sqrt2/(p^2-1)=\sqrt2/8=0.177$ — which is the same truncated convention the handout
> used for the single-phase cases, so 0.17 is defensible. The efficiency figure has no such
> explanation; **96.8 %** is the correct value. See `_verification-log.md`.

---

## 2.10 Full-wave rectification of three-phase currents ·L2 p13

[def ·L2 p13] For **high powers** this six-diode arrangement is preferred. The transformer carries
**six secondary windings**, arranged as **two three-phase groups 180° out of phase**, feeding six
diodes; the two star points are joined through an **interphase transformer**, and the combined
output feeds a choke and the load.

[fig ·L2 p13] **Fig. 55.14 — the circuit and its waveforms.**

*Circuit (left).* Two terminals marked **3-Phase Supply** feed a **delta-connected primary** (three
windings drawn as a triangle). The secondary block is **two star-connected groups**, one above the
other. The upper star's three ends go to diodes **1, 2, 3**; the lower star's to diodes **4, 5, 6**
— each diode drawn **inside a circle**, anode at its winding, cathode to that group's common rail.
The two star points are joined by the **interphase transformer** (a vertical coil pair on a common
core, drawn between the two groups). $V_1$ is arrowed across the upper unit's output, $V_2$ across
the lower unit's, and $V_3$ across the combination. From there a series **Choke** feeds the
**LOAD** (a tall rectangle), across which $V_L$ appears, **+ at the top, − at the bottom**.

*Waveforms (right).* Three stacked panels on a common **Time** axis:

- **$V_1$** — the 3-pulse output of the upper unit: a scalloped ripple, **three humps per supply
  cycle**, with a bracket labelled **"1 Cycle"** spanning three humps.
- **$V_2$** — the same shape for the lower unit, **displaced by half a supply cycle**.
- **$V_3$** — the combined output: the same mean level, but **six shallow humps per cycle** —
  visibly smaller ripple.

**The three numbers** ·L2 p13:

- the interphase transformer **lets the two rectifier units operate independently of each other**,
  and adding their two outputs **cancels the lowest-frequency ripple component**;
- mean output voltage $=0.83\,V_{sm}$ — the same as the three-phase half-wave circuit, because the
  interphase transformer *averages* the two 3-pulse outputs rather than adding them;
- the ripple has a **fundamental frequency six times the supply frequency**, so it is far easier to
  filter;
- the arrangement is preferred at high powers because
  1. **each secondary winding carries current for only $\tfrac13$ of a cycle**,
  2. **each primary winding carries current for $\tfrac23$ of a cycle**, and
  3. the **copper loss is correspondingly lower** for a given dc output.

---

## 2.11 [added] The five rectifiers side by side

Not printed as a table in the handout — assembled here from §§55.5–55.10 and verified against the
derivations above. $V_{sm}$ is the peak of **one** secondary winding (for the centre-tap circuit,
one half of the secondary).

| | Half-wave | Centre-tap FW | Bridge FW | 3-φ half-wave | 3-φ full-wave |
|---|---|---|---|---|---|
| diodes | 1 | 2 | 4 | 3 | 6 |
| centre tap needed | no | **yes** | no | no | (two star points) |
| $V_{L(dc)}$ | $0.318V_{LM}$ | $0.636V_{LM}$ | $0.636V_{LM}$ | $0.83V_{sm}$ | $0.83V_{sm}$ |
| $V_L$ (rms) | $0.5V_{LM}$ | $0.707V_{LM}$ | $0.707V_{LM}$ | $0.841V_{sm}$ | — |
| form factor $K_f$ | 1.571 | 1.111 | 1.111 | 1.017 | — |
| ripple factor $\gamma$ | **1.211** | 0.483 | 0.483 | 0.183 | ≪0.183 |
| $\eta_{\max}$ | 40.5 % | 81.1 % | 81.1 % | 96.8 % | — |
| PIV per diode | $V_{sm}$ | $2V_{sm}$ | $V_{sm}$ | — | — |
| TUF | 0.287 | 0.693 | **0.811** `[added]` | — | — |
| ripple frequency | $f$ | $2f$ | $2f$ | $3f$ | $6f$ |
| series diode drops | $1V_B$ | $1V_B$ | $2V_B$ | $1V_B$ | $1V_B$ |

**How to read it.** Every row that matters improves left to right, except **PIV in the centre-tap
column** — which is the one thing the bridge fixes at the price of two extra diodes.

⚠ **The bridge TUF is `[added]`, not the handout's.** L2 quotes a TUF for the half-wave and
centre-tap circuits only; its bridge section (·L2 p11–p12) has no TUF item at all. It is **not**
0.693. The bridge secondary conducts on both half-cycles, so its VA rating is
$(V_{sm}/\sqrt2)(I_{LM}/\sqrt2) = V_{sm}I_{LM}/2$ while $P_{dc} = (2V_{LM}/\pi)(2I_{LM}/\pi)$:

$$\boxed{\;\mathrm{TUF}_{\text{bridge}} = \frac{8}{\pi^{2}} = 0.811\;}$$

The centre-tap's 0.693 is the average of a 0.573 secondary figure — each half of the winding works
only on alternate half-cycles — and a 0.811 primary figure. That penalty is precisely what §2.8(f)
means by the bridge "using the secondary continuously" and needing "a much smaller transformer",
and quoting 0.693 for the bridge contradicts it.

---

## 2.12 [added] Smoothing — supplied here, NOT in the handout

The p1 topic line promises **smoothing**, and the 26 pages never deliver a filter section. This
block fills the gap. **Everything in §2.12 is added material** and carries no `·L2` citation
because it is not in the source.

### Why a filter is needed

From §2.6 and §2.7, an *unfiltered* rectifier has $\gamma = 1.21$ (half-wave) or $0.48$
(full-wave) — that is, more than a third of the output is ripple even in the best case. A shunt
capacitor across the load turns the rectified humps into a small sawtooth riding on a large dc
level.

### The capacitor-input (shunt-C) filter

Place $C$ directly across $R_L$. The diode conducts only near each peak, topping the capacitor up
to $V_{LM}$; between peaks the capacitor discharges into $R_L$ with time constant $CR_L$.

- If $CR_L \gg T$, the discharge is nearly **linear**, and the output is a sawtooth of
  peak-to-peak amplitude $V_{r(pp)}$.
- Charge balance over one discharge interval $T_d$:

$$Q = I_{L(dc)}\,T_d = C\,V_{r(pp)}$$

[eq: ripple-voltage-shunt-c]

$$\boxed{\;V_{r(pp)}=\frac{I_{L(dc)}}{f_r C}\;}\qquad f_r=\begin{cases}f & \text{half-wave}\\ 2f & \text{full-wave}\end{cases}$$

- $V_{r(pp)}$ — peak-to-peak ripple voltage, V
- $I_{L(dc)}$ — dc load current, A
- $f_r$ — ripple frequency, Hz
- $C$ — smoothing capacitance, F

A linear sawtooth of peak-to-peak $V_{r(pp)}$ has rms $V_{r(pp)}/2\sqrt3$, so

[eq: ripple-factor-shunt-c]

$$\boxed{\;\gamma=\frac{V_{r(rms)}}{V_{L(dc)}}=\frac{1}{2\sqrt3\,f_r\,C\,R_L}\;}$$

and, rearranged for design,

[eq: smoothing-capacitor]

$$\boxed{\;C=\frac{1}{2\sqrt3\,\gamma\,f_r\,R_L}\;}$$

### [added] Worked sizing example — verified numerically

*Take the Example 55.3 circuit (§2.7): full-wave, $V_{LM}=78$ V, $R_L=100\ \Omega$, 50 Hz supply.
Size $C$ for 1 % ripple.*

$$f_r = 2\times50 = 100\ \mathrm{Hz}$$

$$C=\frac{1}{2\sqrt3\times0.01\times100\times100}=\frac{1}{346.4}=2.89\times10^{-3}\ \mathrm{F}=2890\ \mu\mathrm{F}$$

Check the ripple this gives. $I_{L(dc)}\approx V_{LM}/R_L = 0.78$ A, so

$$V_{r(pp)}=\frac{0.78}{100\times2.89\times10^{-3}}=2.70\ \mathrm{V}\quad\Longrightarrow\quad V_{r(rms)}=\frac{2.70}{2\sqrt3}=0.779\ \mathrm{V}$$

and with $V_{L(dc)}\approx V_{LM}-\tfrac12V_{r(pp)}=76.6$ V, $\gamma=0.779/76.6=0.0102\approx1\,\%$ ✓.

**The lesson.** Getting from the unfiltered $\gamma=0.48$ down to 1 % costs nearly 3000 µF at this
load — smoothing capacitors are large, and the half-wave case needs **twice** as much for the same
result because $f_r$ is halved. This is the practical reason full-wave rectification is standard.

### The choke-input and $\pi$ (C-L-C) filters

- A **series choke** opposes changes in current, so it smooths the *current* waveform; a
  choke-input filter gives poorer no-load voltage ($0.636V_{LM}$ rather than $V_{LM}$) but far
  better regulation, because the diode conducts continuously.
- The **C-L-C ($\pi$) filter** drawn in Fig. 55.12 combines both: the first capacitor gives the
  high output voltage, the choke and second capacitor attack what ripple remains. This is why the
  three-phase supply on p12 uses one.

---

## 2.13 Clippers (limiters) ·L2 p14–p18

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{in}$ | input signal voltage | V | ±30 |
| $V_o$ | output signal voltage | V | — |
| $V$ | dc bias battery that sets the clipping level | V | 5–10 |
| $R$ | series resistor | Ω | 100 |
| $R_L$ | load resistor | Ω | 1 k |

[def ·L2 p14] **Clippers and clampers are diode wave-shaping circuits** — circuits meant to control
the **shape** of a voltage or current waveform. Each does what its name says:

- a **clipper's** output looks as though a portion of the input signal had been **clipped off**;
- a **clamper** simply **lifts the whole signal up or down to a different dc level**.

[def ·L2 p14] **A clipping circuit needs a minimum of two components — a diode and a resistor.**
Often a **dc battery** is added to fix the clipping level. The waveform can be clipped at different
levels simply by changing the battery voltage and by interchanging the positions of the elements.

**The modelling rule used throughout §52.16–52.17.** The diode is **ideal**: a **closed switch when
forward-biased**, an **open switch when reverse-biased**. Every clipper problem then reduces to:
*decide for each half-cycle whether the diode is forward-biased; replace it by a short or an open;
read off $V_o$.*

**Applications** ·L2 p14 — radars and digital computers, where signal voltages above or below a
specified level must be removed; and radio receivers, where **noise pulses rising well above the
signal amplitude are clipped down** to the wanted level.

> ⚠ VERIFY **C2.18** ·L2 p14, p15 — two garbles in the introductory prose: "clamper circuits simply
> **clams** (i.e. lift up or down)" for *clamp*, and on p15 "it is **forward-biases B** which acts
> as a short" for *forward-biased, and B acts as a short*. Wording only. See
> `_verification-log.md`.

### 2.13.1 [ex] Example 52.19 — the simple parallel clipper ·L2 p14–p15

**Statement** ·L2 p14. For the simple parallel clipper of Fig. 52.31, find the shape of the output
voltage $V_o$ **across the diode** if the input sine-wave signal is as shown in Fig. 52.31(a). What
will happen when **diode and resistor are interchanged**?

[fig ·L2 p14] **Fig. 52.31.**
**(a)** the input: a sine wave, first half-cycle positive to **+30 V**, second half-cycle negative
to **−30 V**, plotted against $t$.
**(b)** the circuit: terminal **A** at the top left; a **resistor $R$** in the top wire from A to
the output node; the **diode D** from that node down to the bottom wire at **B**, drawn with the
**triangle pointing up and the bar on top** — i.e. **anode at the bottom (B side), cathode at the
top**. $V_o$ is measured **across the diode**, + at the top.
**(c)** the output: a **single positive half-sine of peak 30 V**, then a **flat run at zero** for
the whole negative half-cycle. Marked **30 V** on the ordinate.

[derivation ·L2 p14–p15] **Solution.**

- **Positive half-cycle** — A positive with respect to B, so the top node is positive and the
  diode (cathode uppermost) is **reverse-biased**: an **open switch**. No current flows, so no drop
  across $R$, and the **entire input appears across the diode**: $V_o = V_{in}$, a positive
  half-sine to +30 V.
- **Negative half-cycle** — B positive with respect to A; the diode is **forward-biased** and acts
  as a **short**. $V_o = 0$.
- The negative half of the signal is removed: this is a **negative clipper**.

### 2.13.2 When diode and resistor are interchanged ·L2 p15

[fig ·L2 p15] **Fig. 52.32(b).** From **A**, the **diode D** now lies in the top wire with the
**bar (cathode) on the left, at A**, and the anode on the right; the **resistor $R_0$** runs from
that node down to **B**; $V_o$ is taken **across $R_0$**.

**(c)** the output: **flat at zero** through the positive half-cycle, then a **negative half-sine
to −30 V**. (A small stray digit "2" sits beside the time axis.)

[derivation ·L2 p15]

- **Positive half-cycle** — A positive, so the diode (cathode at A) is **reverse-biased**, an open
  circuit; no current in $R_0$, so $V_o = 0$.
- **Negative half-cycle** — B positive with respect to A; the diode is **forward-biased** and acts
  as a short, putting the whole input across $R_0$: $V_o = V_{in}$, a negative half-sine to −30 V.
- The positive half is removed: this is a **positive clipper**. Interchanging the two elements has
  inverted which half survives.

> **Notation clash.** The resistor in Fig. 52.32(b) is labelled $R_0$, the same symbol the
> rectifier sections use for $R_S+r_d$. Here it is just the clipper's load resistor. Read $R_0$ by
> its context.

### 2.13.3 [ex] Example 52.20 — a parallel clipper with a real diode drop ·L2 p15–p16

**Statement** ·L2 p15. Find the output waveform for the clipper circuit shown in Fig. 52.33 if
$v_{in} = 15\sin\omega t$. The diode is silicon with a forward drop of 0.7 V, $R=100\ \Omega$ and
$R_L=1\ \mathrm{k}\Omega$; an oscilloscope is connected across $R_L$.

[fig ·L2 p15] **Fig. 52.33.** **A** is the top-left node; $R=100\ \Omega$ runs from A rightwards to
the top rail. The source $V_{in}$ sits between A and **B**, the bottom rail. **D** hangs from the
top rail to the bottom rail, drawn with the **triangle pointing up, bar on top** — **anode at the
bottom (grounded) rail, cathode at the top**. **$R_L=1\ \mathrm{k}\Omega$** is in parallel with D
between the same two rails, and the **oscilloscope** is drawn across $R_L$.

[derivation ·L2 p15–p16] **Solution.**

- **Negative half-cycle** (B positive with respect to A, so the top rail is driven negative) — the
  diode becomes **forward-biased once the applied voltage exceeds 0.7 V**. D and $R_L$ are in
  parallel, so **the voltage across them cannot exceed 0.7 V**; everything beyond that is clipped.
  $$V_o = -0.7\ \mathrm{V}\ \text{(flat)}$$
  This is a **negative clipper**.
- **Positive half-cycle** — A positive, diode **reverse-biased**, an open circuit; $R$ and $R_L$
  form a **potential divider**:
  $$V_o = V_{in}\cdot\frac{R_L}{R+R_L}=15\times\frac{1000}{100+1000}=13.64\ \mathrm{V}$$

[fig ·L2 p16] **Fig. 52.33(c) — the output.** Positive half-sines of peak **13.64 V**, alternating
with **flat runs at −0.7 V**. The zero line is drawn, with the clipped level marked just below it
as "0.7 V".

[added] **Arithmetic verified.** $15\times1000/1100=13.6364$ → 13.64 V ✓.

> ⚠ VERIFY **C2.19** ·L2 p16 — in Fig. 52.33(c) the clipped level is labelled "**0.7 V**" although
> it is drawn **below** the zero line and the text calls it the negative clipping level. It should
> read **−0.7 V**. Missing sign only. See `_verification-log.md`.

### 2.13.4 [ex] Example 52.21 — the biased series clipper ·L2 p16

**Statement** ·L2 p16. Find the output waveform of the biased series clipper of Fig. 52.34 when the
input is $20\sin\omega t$ and the series battery is 10 V.

[fig ·L2 p16] **Fig. 52.34.**
**(a)** the input: a sine wave of peak **±20 V**, with a **dashed horizontal line at +10 V**
marking the bias level.
**(b)** the circuit: from **A**, in series along the top wire, a **10 V battery**, then the
**diode D**, then to the output node; **$R=10\ \mathrm{k}\Omega$** runs from that node down to
**B**; $V_o$ is taken across $R$.
**(c)** the output as drawn: a curve rising from the **−10 V** level at $t=0$, crossing zero,
peaking a little above the zero line, falling back to zero and then **flat at zero** to the end of
the plot (the abscissa tick "2" marks the end of the second half-cycle). **See V2.15.**

[derivation ·L2 p16] **Solution as the text gives it.** The battery **opposes** conduction, so **no
current flows until $v_{in}$ exceeds 10 V**. Hence only the **upper part of the positive signal**
passes through and appears as $V_o$ across $R$. In the handout's words, *"the entire input is
clipped off except the positive peak portions."*

[added] **The output, worked out.** With an ideal diode,

$$V_o=\begin{cases}v_{in}-10\ \mathrm{V}, & v_{in}>10\ \mathrm{V}\\[2pt] 0, & v_{in}\le10\ \mathrm{V}\end{cases}$$

$v_{in}=20\sin\omega t$ exceeds 10 V for $30°<\omega t<150°$, so the output is a **single hump per
cycle, of peak $20-10=10$ V, occupying one third of the cycle**, and **zero everywhere else** —
including the whole negative half-cycle.

> ⚠ VERIFY **V2.15** ·L2 p16 — **Fig. 52.34(c) is drawn wrongly.** The plotted output **starts at
> −10 V** at $t=0$ and rises through zero to its peak. A *series* clipper whose diode is blocking
> passes no current, so **$V_o$ across $R$ must be exactly zero** whenever $v_{in}<10$ V — it
> cannot be negative at $v_{in}=0$, and the battery cannot drive current because it is the element
> reverse-biasing the diode. What appears to have happened is that the whole of $v_{in}-10$ has
> been plotted on the rising flank (which is $-10$ V at $t=0$) while the falling flank was
> correctly flattened to zero. Correct waveform:
> $$\boxed{\;V_o=\max\!\left(v_{in}-10,\ 0\right)\;}$$
> — zero from $\omega t=0$ to $30°$, a hump of peak 10 V from $30°$ to $150°$, zero thereafter.
> Compare **Fig. 52.35(c) on the same page**, which *is* drawn correctly for the reversed battery.
> See `_verification-log.md`.

### 2.13.5 The same clipper with the battery reversed ·L2 p16

[fig ·L2 p16] **Fig. 52.35.** The circuit of Fig. 52.34 with the **battery polarity reversed**, so
that it now **aids** conduction. **(c)** the output: the trace starts at the **+10 V** dashed level
at $t=0$, rises to a peak of about **+30 V**, falls back through +10 V and continues down to
**zero**, runs **flat at zero** through the deepest part of the negative half-cycle, then returns
to +10 V.

[derivation ·L2 p16] With the battery aiding, the diode conducts as long as $v_{in}+10>0$:

$$V_o=\begin{cases}v_{in}+10\ \mathrm{V}, & v_{in}>-10\ \mathrm{V}\\[2pt] 0, & v_{in}\le-10\ \mathrm{V}\end{cases}$$

The handout puts it as: during the positive half-cycle the output is the **signal lifted by 10 V**;
during the negative half-cycle the **lower peaks are clipped off** because of the 10 V battery.
Peak output $=20+10=30$ V ✓, consistent with the drawn trace.

### 2.13.6 [ex] Example 52.22 — the double-ended (biased parallel) clipper ·L2 p16–p17

**Statement** ·L2 p16. Find the output waveform of the clipper of Fig. 52.36 for the triangular
input shown, of peak ±30 V.

[fig ·L2 p16] **Fig. 52.36.**
**(a)** the input: a **triangular wave**, rising linearly to **+30 V**, falling linearly to
**−30 V**, repeating.
**(b)** the circuit: from **A**, a series **$R$** to node **C**; from C, **two shunt branches** go
down to the bottom rail **D**:
 - branch 1 — **$D_1$** drawn with the **triangle pointing down, bar at the bottom** (anode at C,
   cathode downward) **in series with a 10 V battery**;
 - branch 2 — **$D_2$** drawn with the **triangle pointing up, bar on top** (cathode at C, anode
   downward) **in series with a 5 V battery**.
 $V_o$ is taken across C–D.
**(c)** the output: a **trapezoid** — rising linearly from 0, **flat-topped at +10 V**, falling
linearly through zero, **flat-bottomed at −5 V**, then rising again. Levels marked **10 V** and
**−5 V**.

[derivation ·L2 p16–p17] **Solution.**

- **Positive half** — $D_1$ conducts, $D_2$ is an open circuit. With $D_1$ shorted, C and D are
  connected across the **10 V battery**, so $V_o$ **cannot exceed 10 V**; signal voltage above
  10 V is clipped off.
- **Negative half** — $D_2$ conducts, $D_1$ is open, and C–D sits across the **5 V battery** with
  the opposite polarity, so $V_o$ **cannot go below −5 V**.
- Between $-5$ V and $+10$ V neither diode conducts, no current flows in $R$, and the output
  follows the input exactly — which is why the sloping parts of the trapezoid are straight.

**This is the "limiter" of the p1 topic outline**: a circuit that limits a signal to a chosen
window, here $[-5,+10]$ V.

### 2.13.7 Some clipping circuits — the reference set ·L2 p17–p18

[fig ·L2 p17] **Fig. 52.37 — the common input** used for all of Fig. 52.38 and Fig. 52.39: one
complete sine cycle, positive half then negative half, plotted against $t$.

#### (a) Biased series clippers — Fig. 52.38 ·L2 p17

[exercise ·L2 p17] The handout **draws these two circuits and their output waveforms but gives no
analysis**: "The output voltage has the waveform as shown."

[fig ·L2 p17] **Fig. 52.38 — two circuits, side by side, identical except for battery polarity.**
Each: the source $V_{in}$ on the left; in series along the top, a **battery $V$** and then a
**diode D whose bar (cathode) is on the left**, i.e. anode towards the load; then **$R$** down to
the bottom rail, with $V_o$ across it.

- **(a)** the battery's plates read **short-left, long-right**. Output plot: the level **$-V$** is
  ticked on the ordinate. The trace is **solid** where it lies **below** the zero axis and
  **dashed** where it lies above — the dashed positive hump being the part that is clipped away.
  Solid portions run from $-V$ up to the axis at the start, then from the axis down through a deep
  negative excursion and back.
- **(b)** the battery is **reversed** (long-left, short-right). Output plot: the level **$V$** is
  ticked **above** zero, the dashed hump reaches higher, and the solid part is a **shallower
  negative bowl** between the zero crossings.

[added] **What the two waveforms mean — supplied here, NOT in the handout.** Both plots are the
same construction: **plot the shifted input $v_{in}\mp V$, draw it dashed where it is positive and
solid where it is negative, and take the output to be the solid part plus zero elsewhere.** That
is:

$$\textbf{(a)}\quad V_o=\min\!\left(v_{in}-V,\ 0\right)\qquad\qquad\textbf{(b)}\quad V_o=\min\!\left(v_{in}+V,\ 0\right)$$

- In **(a)** the output is non-zero for almost the whole cycle and reaches $-(V_m+V)$; the circuit
  removes everything **above** $+V$.
- In **(b)** the output is zero except where $v_{in}<-V$, reaching $-(V_m-V)$; the circuit passes
  only the **negative peaks beyond $-V$**.

**A reading caution.** The $V_{in}$ and $V_o$ markers in Fig. 52.38 are **double-headed span
arrows, not polarity arrows** — they say *"this is the voltage across here"*, not which end is
positive. Taking the + reference at the **lower** terminal of each pair makes the two plotted
waveforms follow from the two drawn battery polarities; taking it at the upper terminal reverses
both. Since the handout gives no algebra, the waveform is the definitive statement of what the
circuit does, and the formulas above reproduce it.

#### (b) Biased parallel clippers — Fig. 52.39 ·L2 p18

[exercise ·L2 p18] Again drawn without analysis. Four circuits (a)–(d), all of the same shape:
$V_{in}$ on the left, **$R$** in series along the top, and a **shunt branch of one diode in series
with a battery $V$** down to the bottom rail; $V_o$ is taken across that shunt branch.

[fig ·L2 p18] **The four cases, exactly as drawn:**

| | Diode | Battery | Behaviour drawn |
|---|---|---|---|
| **(a)** | triangle **down**, bar at bottom → **anode at top** | **+ at top** (long plate up) | positive peaks **flattened at $+V$**; whole negative half passes unchanged; the removed positive cap shown dashed |
| **(b)** | triangle **down**, bar at bottom → **anode at top** | **+ at bottom** (reversed) | output held **flat at $-V$** for almost the whole cycle, following the input only where $v_{in}<-V$; everything above $-V$ shown dashed |
| **(c)** | triangle **up**, bar on top → **cathode at top** | **+ at top** | whole positive half passes unchanged; negative peaks **flattened at $-V$**; the removed negative cap shown dashed |
| **(d)** | triangle **up**, bar on top → **cathode at top** | **+ at bottom** | output held **flat at $+V$** for almost the whole cycle, following the input only where $v_{in}>+V$ |

[added] **The one rule that generates all four — supplied here, NOT in the handout.** In a parallel
(shunt) clipper the diode branch **holds the output at the branch's turn-on level whenever it
conducts, and is invisible otherwise**:

$$\boxed{\;V_o=\begin{cases}V_{\text{clip}} & \text{when the diode branch is forward-biased}\\ v_{in} & \text{otherwise}\end{cases}}$$

- The **clip level $V_{\text{clip}}$** is the battery voltage, signed by the battery's polarity.
- The **diode's direction decides which side is clipped**: anode-to-the-signal (triangle down)
  clips **everything above** $V_{\text{clip}}$; cathode-to-the-signal (triangle up) clips
  **everything below** it.

Applying it: (a) clips above $+V$; (b) clips above $-V$; (c) clips below $-V$; (d) clips below
$+V$ — exactly the four waveforms drawn. Case (a) with $V=0$ collapses to Example 52.19's simple
parallel clipper, and Example 52.22 is (a) and (c) in parallel.

---

## 2.14 Clampers (dc restorers) ·L2 p17–p20

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $C$ | coupling/clamping capacitor | F | 1 µF |
| $R$ | shunt resistor | Ω | 10 k |
| $\lambda$ | RC time constant (the handout's symbol for $\tau$) | s | 10 ms |
| $T$ | period of the input signal | s | 1 ms |
| $V_1$ | clamping-level battery | V | — |

[def ·L2 p17] **Clamping** is the process of **introducing a dc level into a signal**. A signal
swinging between $+5$ V and $-5$ V, passed through a **positive dc clamper** that introduces $+5$ V,
comes out swinging between **0 V and $+10$ V**. A **negative dc clamper** gives an output swinging
between **0 V and $-10$ V**. Clampers are also called **dc restorers** or **dc reinserters**.

[fig ·L2 p18] **Fig. 52.40 — three waveform panels.**
**(a)** the input: a sine wave symmetric about zero, marked **+5 V**, **0**, **−5 V**.
**(b)** positively clamped: the *same* sine now running between **0** and **+10 V**, with a
**dashed horizontal line at +5 V labelled "D C Level"**.
**(c)** negatively clamped: the same sine running between **0** and **−10 V**, with the dc level
dashed at −5 V. The three ordinates are all labelled $V_{in}$, although (b) and (c) are outputs;
the middle level in (c) is labelled "5 V" without its minus sign.

> ⚠ VERIFY **C2.20** ·L2 p18 — in **Fig. 52.40**, all three ordinates are labelled $V_{in}$ even
> though panels (b) and (c) are **outputs**; and in panel (c) the dc level is labelled "**5 V**"
> where **−5 V** is meant (the peak below it does carry its "−10 V"). Labelling only. See
> `_verification-log.md`.

[def ·L2 p18] **A clamping circuit needs a minimum of three elements** — **1. a diode, 2. a
capacitor, 3. a resistor** — and will generally need a **dc battery** as well.

### Five things to remember about clampers ·L2 p18–p19

1. **Both $R$ and $C$ affect the waveform.**
2. [eq: clamper-time-constant] The values of $R$ and $C$ must give a time constant large enough
   that **the capacitor stays almost fully charged over a period of the signal**:
   $$\boxed{\;\lambda = CR \gg \frac{T}{2}\;}$$
   For good clamping action the $RC$ time constant should be **at least ten times the period of
   the input signal**.
3. It is **advantageous to first find the condition under which the diode becomes forward-biased**
   — that one decision drives the whole analysis.
4. [added: emphasis] **For all clamping circuits the voltage swing of the input and output
   waveforms is the same.** A clamper shifts a waveform; it never squeezes it. (Contrast a clipper,
   which changes the swing but not the level.)
5. **Application: TV receivers, as dc restorers.** The incoming composite video signal passes
   through **capacitively coupled amplifiers**, which strip out the dc component and with it the
   **black and white reference levels and the blanking level**. Those references must be
   **restored** before the signal reaches the picture tube.

> **Notation.** The handout writes the time constant as $\lambda$, not the usual $\tau$. Also
> $\lambda$ is *not* a wavelength anywhere in this lesson.

### 2.14.1 [ex] Example 52.23 — a clamper with a rectangular input ·L2 p19–p20

**Statement** ·L2 p19. The input signal of Fig. 52.41(a) is applied to the clamper circuit of
Fig. 52.41(b). Draw the waveform of the output voltage $V_o$. **How will it change if $R$ is made
100 Ω?** *(Electronic circuits, Bangalore Univ.)*

[fig ·L2 p19] **Fig. 52.41 — four panels.**
**(a)** the input: a **rectangular wave of frequency 1000 Hz**, sitting at **+5 V** for half of
each period and **−10 V** for the other half; the switching instants are labelled $t_1$, $t_2$,
$t_3$.
**(b)** the circuit: **A** at the top left; the capacitor **$C=1\ \mu\mathrm{F}$** in the top wire
from A to the next node; **$R=10\ \mathrm{k}\Omega$** from that node down to the bottom rail; then
the output terminals **E** (top) and **F** (bottom), with the **diode D** across them drawn with
the **triangle pointing down, bar at the bottom** — anode at E, cathode at F. So **$R$ and $D$ are
in parallel**, and $V_o$ is the voltage across that parallel pair. B is the input's bottom
terminal.
**(c)** the equivalent circuit for the positive input half-cycle: $V_{in}=5$ V, D replaced by a
**short**, and $R$ shown shorted out with it.
**(d)** the same, redrawn with $C$ charged to **5 V** (+ on the A side) and the output marked
**zero**.

[derivation ·L2 p19] **Solution.**

$$T=\frac{1}{1000}\ \mathrm{s}=1\ \mathrm{ms}\qquad\Longrightarrow\qquad 0\to t_1=t_1\to t_2=t_2\to t_3=\frac{T}{2}=0.5\ \mathrm{ms}$$

$$\lambda = CR = 1\times10^{-6}\times10\times10^{3}=10\ \mathrm{ms}$$

Since $\lambda\gg T/2$ (10 ms against 0.5 ms), **once charged the capacitor has hardly any time to
discharge before the signal polarity reverses**.

**(a) Positive input half-cycle.** Terminal A goes positive with respect to B, so **D acts like a
short** [Fig. 52.41(c)]. A steady +5 V is applied to A for 0.5 ms; **$R$ is also shorted**, being in
parallel with D. The capacitor therefore **charges rapidly to 5 V**, + on the A side. Being across
a short,

$$V_o = 0\quad\text{throughout the positive half-cycle}$$

**(b) Negative input half-cycle.** B becomes positive, the diode is **reverse-biased** and acts as
an **open circuit** [Fig. 52.42(a)]. Now $R$ and $C$ are in series, with
$\lambda = CR = 10$ ms; **full discharge would need $5\lambda = 50$ ms**, but the half-cycle allows
only **0.5 ms**, so $C$ stays essentially fully charged at 5 V.

The output is then the voltage from E round to F through the source and the capacitor:

$$V_o = -(V_C + |V_{in}|) = -(5+10) = -15\ \mathrm{V}$$

with **E negative**.

[fig ·L2 p19] **Fig. 52.42(a)** shows this state: **A** marked **−**, the capacitor drawn charged
with **+ on the left plate** and its 5 V labelled, $V_{in}=10$ V with **B marked +**, $R=10$ kΩ,
and the diode replaced by an **open switch symbol**; $V_o$ arrowed downward between E and F.

[fig ·L2 p19] **Fig. 52.42(b) — the output waveform.** A rectangular wave: **0 V** during
$t_1$ (0–0.5 ms), **−15 V** during $t_2$ (0.5–1.0 ms), 0 V during $t_3$, −15 V during $t_4$, and so
on; the time axis is ticked at **0.5, 1.0, 1.5, 2.0, 2.5, 3.0 ms** with the intervals labelled
$t_1$ to $t_6$.

**Check against rule 4** ·L2 p20 — input swing $=5-(-10)=15$ V; output swing $=0-(-15)=15$ V. **The
same**, as it must be, and the frequency is unchanged; only the level has moved, downward. The
signal has been **negatively clamped to 0 V**.

> ⚠ VERIFY **V2.16** ·L2 p19 — the negative-half-cycle paragraph states that B going positive
> "**reverse-biases D by 10 V**". The diode has the *whole output* across it, and p20 derives that
> output as $5+10=15$ V. So the diode's reverse voltage is **15 V, not 10 V** — the capacitor's
> stored 5 V adds to the 10 V input. This matters: a diode chosen on the printed figure would be
> under-rated by 50 %. Correct value:
> $$\boxed{\;V_{R,\text{diode}}=V_C+|V_{in}|=5+10=15\ \mathrm{V}\;}$$
> See `_verification-log.md`.

### 2.14.2 The same circuit with $R = 100\ \Omega$ ·L2 p20

[derivation ·L2 p20]

$$\lambda = CR = 1\times10^{-6}\times100 = 10^{-4}\ \mathrm{s}=0.1\ \mathrm{ms}$$

$$5\lambda = 0.5\ \mathrm{ms}=\frac{T}{2}$$

Now the **full discharge time equals the half-period**. The capacitor discharges essentially
completely within each negative half-cycle, so the output can no longer hold its clamped level:
$V_o$ jumps **momentarily to −15 V at the start of each negative half-cycle and decays almost to
zero before the polarity reverses**.

[fig ·L2 p20] **Fig. 52.43 — the degraded output.** The zero line runs along the top of the plot;
the level **−15 V** is ticked below it (printed "15 V", without the sign). Three **negative
spikes** are drawn, at $t=0.5$, 1.5 and 2.5 ms, each jumping straight down to −15 V and then
**decaying exponentially back towards zero** within its half-period. The time axis is ticked
0.5–3.0 ms with intervals $t_1$–$t_6$.

**The lesson.** Clamping works only while $CR\gg T/2$. Reduce $R$ by a factor of 100 and the
clamper turns into a **differentiator**, producing spikes instead of a level shift.

[added] **Arithmetic verified.** $1\ \mu\mathrm{F}\times10\ \mathrm{k}\Omega=10^{-2}$ s $=10$ ms ✓;
$5\lambda=50$ ms ✓; $1\ \mu\mathrm{F}\times100\ \Omega=10^{-4}$ s $=0.1$ ms ✓; $5\lambda=0.5$ ms
$=T/2$ ✓; output level $-(5+10)=-15$ V ✓; swing 15 V in and 15 V out ✓.

> ⚠ VERIFY **C2.21** ·L2 p19, p20 — a cluster of small faults across this worked example:
> the interval list prints "$0\to t_1=t_1\to t_2=t_2\to t_2=T/2$" (the third should be
> $t_2\to t_3$); the time constant is set as "$\lambda = C_R$" with $R$ as a subscript instead of
> $\lambda = CR$; the capacitor is labelled "**1 F**" in Fig. 52.41(b) and "**$C=1.0$ F**" in
> Fig. 52.42(a), the µ prefix having dropped in both; p20 cites "Fig. 52.40(a)" where **Fig.
> 52.42(a)** is meant; p20 writes "$\lambda = 100\times1\times10^{-6}$ **ms** = 0.1 ms" (the first
> quantity is in **seconds**); p20 says $5\lambda$ "equals the half time-period (**0.5 s**)" where
> **0.5 ms** is meant; and Fig. 52.43's level is ticked "**15 V**" for **−15 V**. All the numbers
> used are right. See `_verification-log.md`.

### 2.14.3 Summary of clamping circuits ·L2 p20

**The standing assumption** ·L2 p20: $5\lambda = 5RC \gg T/2$ throughout.

[fig ·L2 p20] **Fig. 52.44 — the common input**: a **square wave** of peak value $V$, alternating
between $+V$ and $-V$ with equal half-periods; the levels $V$, 0 and $-V$ are marked and the period
$T$ is bracketed. Peak-to-peak swing $=2V$.

All four circuits below share the same skeleton: **$V_{in}$ → series $C$ → node; $R$ shunt to the
bottom rail; a branch of diode + battery $V_1$ also shunt to the bottom rail; $V_o$ across the
diode-and-battery branch.** Only the diode direction and the battery polarity change.

[fig ·L2 p20] [table] **The four standard clampers.**

| Fig. | Diode | Battery $V_1$ | Output waveform as drawn |
|---|---|---|---|
| **52.45** | triangle **down**, bar at bottom (anode uppermost) | one way round | square wave whose **upper level is $V_1$**, swinging **down** by $2V$ to $V_1-2V$ — **negative clamping to $V_1$** |
| **52.46** | **reversed** (cathode uppermost) | same as 52.45 | square wave whose **lower level is $V_1$**, swinging **up** by $2V$ to $V_1+2V$ — **positive clamping to $V_1$** |
| **52.47** | triangle **down** | **reversed** | square wave whose **upper level is $-V_1$**, swinging **down** by $2V$ |
| **52.48** | **reversed** | **reversed** | square wave whose **lower level is $-V_1$**, swinging **up** by $2V$ |

**The two rules this table encodes** ·L2 p20:

- **Reversing the diode turns negative clamping into positive clamping** (compare Fig. 52.45 with
  Fig. 52.46).
- **Reversing the battery moves the clamping level from $+V_1$ to $-V_1$** (compare Fig. 52.45 with
  Fig. 52.47).

In every case the **swing stays $2V$** — rule 4 again.

> ⚠ VERIFY **C2.22** ·L2 p20 — three labelling faults in the summary. (i) The text reads "It is
> seen from **Fig. 52.44 and 52.45** that negative clamping has changed to positive clamping when
> the diode connections are reversed" — but Fig. 52.44 is the *input* waveform; the comparison is
> between **Fig. 52.45 and Fig. 52.46**. (ii) In **Fig. 52.47(b)** the ordinate is labelled
> **$V_{in}$** where $V_o$ is meant. (iii) In the same panel the clamping level, drawn **below**
> zero, is labelled **$V_1$**; Fig. 52.48(b) labels the corresponding level **$-V_1$**, which is
> the consistent form. See `_verification-log.md`.

---

## 2.15 Voltage multipliers ·L2 p21–p23

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_m$ | peak input (secondary) voltage | V | 311 |
| $V_{C1},V_{C2}$ | voltage on the first, second capacitor | V | $V_m$, $2V_m$ |
| $V_L$ | dc output (load) voltage | V | $2V_m$ |

[def ·L2 p21] **A voltage multiplier** is a circuit which produces a **greater dc output voltage
than the ac input voltage** to its rectifiers. It is used wherever **high voltages at low currents**
are wanted — the classic case being **electron acceleration in a cathode-ray tube (CRT)**.

The handout treats four: **1. half-wave voltage doubler, 2. full-wave voltage doubler, 3. voltage
tripler, 4. voltage quadrupler.** ·L2 p21

### 2.15.1 Half-wave (cascade) voltage doubler ·L2 p21–p22

[fig ·L2 p21] **Fig. 55.31(a) — the circuit.** A transformer secondary marked $V_m$, **+ at the
top, − at the bottom**. Then, reading along the top wire:

- **$C_1$** in series, **+ on its left plate, − on its right**;
- at the node after $C_1$, **$D_1$** drops to the bottom rail, drawn **triangle down, bar at the
  bottom** — **anode at the top node, cathode on the bottom rail**;
- continuing right, **$D_2$** lies in the top wire drawn **triangle pointing left, bar on the
  left** — **cathode at the $D_1$ node, anode at the output node**;
- **$C_2$** hangs from the output node to the bottom rail, **− at the top, + at the bottom**;
- the output terminals take $V_L=2V_m$ across $C_2$, **− at the top, + at the bottom**.

[fig ·L2 p21] **Fig. 55.31(b) — the waveforms.** Upper: $v_i$, a complete sinusoid of peak $V_m$.
Lower: $V_L$, the **capacitor-filtered half-wave shape** — a fast rise to a peak once per input
cycle, then a slow, nearly linear **discharge droop** until the next peak, drawn solid over a
dashed sinusoidal reference, with the level **$2V_m$** arrowed at a peak.

[fig ·L2 p21] **Fig. 55.32** repeats the same circuit, redrawn to show the **outer KVL loop** used
in the analysis.

[derivation ·L2 p21] **Circuit analysis.**

- **Positive half-cycle** — $D_1$ conducts (not $D_2$) and charges **$C_1$ to the peak secondary
  voltage $V_m$**, with the polarity shown.
- **Negative half-cycle** — $D_2$ conducts (not $D_1$) and charges **$C_2$**. The voltage on $C_2$
  is the **sum of the peak supply voltage and the voltage already on $C_1$**. Applying KVL round
  the outer loop, starting at the bottom of the secondary and going clockwise:

$$-V_m-V_m+V_{C2}=0$$

[eq: doubler-output]

$$\boxed{\;V_{C2}=2V_m=2\times\text{peak input voltage}\;}$$

- **Next positive half-cycle** — $D_2$ is open and **$C_2$ discharges through the load** if one is
  connected.
- **On no load** both capacitors stay charged: $C_1$ to $V_m$ and $C_2$ to $2V_m$. **With a load**,
  $C_2$ discharges a little and its voltage drops slightly, but it is **recharged on the next
  half-cycle** — which is exactly the droop drawn in Fig. 55.31(b).

**Properties** ·L2 p21:

- the output waveform is that of a **half-wave rectifier filtered by a shunt capacitor**;
- **PIV across each diode** — the same for every multiplier in §2.15:

[eq: multiplier-piv]

$$\boxed{\;\mathrm{PIV}_{\text{multiplier}}=2V_m\;}$$

- **ripple frequency $=$ the supply frequency** (it is a half-wave circuit);
- **very poor regulation** and **high ripple content**;
- there is a **common connection between the supply line and the load** — which the full-wave
  doubler avoids.

### 2.15.2 Full-wave voltage doubler ·L2 p22

[fig ·L2 p22] **Fig. 55.33(a) — the circuit.** The ac source $V_m$ sits on the left between a top
terminal and a middle terminal.

- **$D_1$** lies in the top wire from the top source terminal, **anode left, cathode right**.
- **$C_1$** hangs from $D_1$'s cathode down to the **middle node**, where the source's second
  terminal joins; **+ at the top plate, − at the bottom**.
- **$C_2$** continues from the middle node down to the bottom node, **+ at the top, − at the
  bottom**.
- **$D_2$** lies in the bottom wire, **cathode on the left, anode on the right**, returning the
  bottom node to the source's top rail.
- The output is taken across the **series pair $C_1+C_2$**, **+ at the top, − at the bottom**,
  and equals $V_L=2V_m$.

[fig ·L2 p22] **Fig. 55.33(b) — the waveforms.** Upper: $V_i$, a full sinusoid of peak $V_m$.
Lower: $V_L$, a nearly flat level with a **small sawtooth ripple at twice the input frequency**
(two ripple cycles per input cycle), with the mean marked $V_{dc}=2V_m$.

[derivation ·L2 p22]

- **Positive half-cycle** — $D_1$ conducts (not $D_2$) and charges **$C_1$ to $V_m$**.
- **Negative half-cycle** — $D_2$ conducts (not $D_1$) and charges **$C_2$ to $V_m$**.
- **As far as the load is concerned the two capacitor voltages are series-aiding**, so with no
  load

$$\boxed{\;V_L=2V_m\;}$$

**Worked figure** ·L2 p22 — for a 220 V, 50 Hz supply,

$$V_{dc}=2V_m=2\times220\sqrt2=620\ \mathrm{V}$$

With a load connected, $V_L$ would be **less than $2V_m$**.

[added] **Verified.** $2\times220\sqrt2=622.25$ V; the printed 620 V follows from the same
$V_m\approx310$ V rounding used in Example 55.1. (See C2.8 for the dropped "220" in the printed
expression.)

**Properties** ·L2 p22:

- **PIV of each diode $=2V_m$**;
- **ripple frequency $=$ twice the supply frequency** — the advantage over the half-wave doubler;
- there is **no common connection between the supply line and the load**;
- **where the expense of a line transformer is justified, the conventional full-wave rectifier of
  Art. 55.7 is superior** and should be used instead.

### 2.15.3 Voltage tripler and quadrupler ·L2 p22–p23

[def ·L2 p22–p23] **(a) General.** The **half-wave doubler of Fig. 55.31 can be extended** to give
any multiple of the peak input voltage — $3V_m$, $4V_m$, $5V_m$, and so on. **Theoretically there
is no upper limit**, but in practice the total capacitance needed becomes **unmanageably large** if
the dc output is to hold up under anything but an **extremely light load**.

[fig ·L2 p23] **Fig. 55.34 — the cascade multiplier.** An ac source of peak $V_m$ (its sinusoid
sketched at the far left) with **+ at the top terminal, − at the bottom**. Then:

- **Top row:** $C_1$ (+ left, − right) in series from the + terminal to a node; then $C_3$
  (+ left, − right) in series to the next node.
- **Bottom row:** from the − terminal, a wire to a node; then $C_2$ (+ left, − right) in series;
  then $C_4$ (+ left, − right).
- **Four vertical diodes** bridge the two rows, alternating in direction:
  **$D_1$** (triangle down — anode on the top rail), **$D_2$** (triangle up — anode on the bottom
  rail), **$D_3$** (triangle down), **$D_4$** (triangle up).
- Three output spans are bracketed across the ladder: **"Doubler ($2V_m$)"** along the bottom,
  **"Tripler ($3V_m$)"** across the top, and **"Quadrupler ($4V_m$)"** across the full width.
- The capacitors are labelled with the voltages they reach: $C_1$ to $V_m$, and $C_2$, $C_3$ and
  $C_4$ to $2V_m$ each.

[derivation ·L2 p23] **(c) Analysis.**

1. **First positive half-cycle** — $D_1$ conducts and **$C_1$ charges to $V_m$**.
2. **Negative half-cycle** — $C_2$ is charged through $D_2$ to **$2V_m$**, i.e. to the sum of the
   voltage on $C_1$ and the peak input (this is Art. 55.26 again).
3. **Second positive half-cycle** — $D_3$ conducts and the voltage across $C_2$ charges **$C_3$ to
   the same $2V_m$**.
4. **Negative half-cycle** — $D_2$ and $D_4$ conduct, allowing $C_3$ to charge **$C_4$ to $2V_m$**.

Reading the ladder off Fig. 55.34:

$$V_{C_2}=2V_m,\qquad V_{C_1}+V_{C_3}=3V_m,\qquad V_{C_2}+V_{C_4}=4V_m$$

**With additional diodes and capacitors, every further capacitor is charged to $2V_m$** and the
multiplication continues.

**Properties** ·L2 p23:

- **PIV of each diode $=2V_m$**;
- ripple frequency stated as **twice the line frequency** — **see V2.17**;
- these circuits are used **where both the supply voltage and the load are held constant**.

> ⚠ VERIFY **V2.17** ·L2 p21, p23 — the multiplier section states two different ripple frequencies
> for the **same topology**. p21 says of the half-wave (cascade) doubler: "**Ripple frequency is
> equal to the supply frequency**" — correct, because each output capacitor is refilled once per
> input cycle. p23 then says of Fig. 55.34, which §55.28(a) has just described as *"the half-wave
> voltage doubler circuit (Fig. 55.31) extended"*, that "ripple frequency is **twice** the line
> frequency". The two cannot both be right for one circuit. The correct statement for a cascade
> (Cockcroft–Walton) multiplier built from the half-wave doubler is
> $$\boxed{\;f_{\text{ripple}}=f_{\text{supply}}\;}$$
> — the "twice" belongs to the **full-wave** doubler of §55.27 (p22), where it is correctly
> stated. See `_verification-log.md`.

> ⚠ VERIFY **C2.23** ·L2 p22, p23 — typographic faults in the multiplier pages: Fig. 55.33(a)
> prints an overstruck "**−**" above the "**+**" on $C_1$'s upper plate (the "+" is the correct
> mark — the two capacitors must be series-**aiding** for the output to be $2V_m$); p23 writes
> "voltage across **$C_2$\***" with a stray asterisk, "**If** is seen from Fig. 55.34" for *It is
> seen*, and "$D_3$ **conduct**" for *conducts*. None changes the circuit. See
> `_verification-log.md`.

---

## 2.16 The tunnel diode ·L2 p23–p26

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_T$ | voltage across the tunnel diode | V | 0–1 |
| $i_T$ | tunnel-diode current | A | mA |
| $I_P$ | peak current (at $V_P$) | A | mA |
| $I_V$ | valley current (at $V_V$) | A | $I_P/3$ to $I_P/12$ |
| $V_P$ | peak-point voltage | V | ~0.05 |
| $V_V$ | valley-point voltage | V | ~0.3 |
| $-R_N$ | negative resistance in the A–B region | Ω | −10 to −200 |
| $L_S$ | series lead inductance | H | 0.1–4 nH |
| $R_S$ | series ohmic resistance | Ω | 1–5 |
| $C$ | junction capacitance | F | 1–10 pF |

[def ·L2 p23] **The tunnel diode** (Esaki diode) was first introduced by **Dr. Leo Esaki in 1958**.

### (a) Construction ·L2 p23–p24

It is a **high-conductivity two-terminal p-n junction diode** whose **doping density is about 1000
times that of an ordinary junction diode**. That extreme doping produces **three unusual effects**:

1. it **reduces the depletion-layer width** to an extremely small value — about
   $0.00001\ \mathrm{mm}$, i.e. $10^{-8}$ m $=10$ nm;
2. it **reduces the reverse breakdown voltage to nearly zero**, so the diode appears to be
   **broken down for any reverse voltage**;
3. it **produces a negative-resistance section** on the V/I characteristic.

**Why "tunnel".** Because of the extremely thin depletion layer, **charge carriers can punch
through the junction with the speed of light rather than climb over the potential barrier**; the
transit is called **tunnelling** and requires **less than 0.05 V of forward bias**. Tunnel diodes
are usually fabricated from **germanium, gallium arsenide (GaAs) and gallium antimonide (GaSb)**.
·L2 p24

[fig ·L2 p23] A photograph captioned **"Discrete commercial Si tunnel diode"** — a
micrograph-style image of a small rectangular die with a rounded contact. Third-party image;
described, never reproduced.

[fig ·L2 p24] **Fig. 54.18 — three representations, side by side.**

1. **Left:** a rectangular block divided horizontally, upper part labelled **N**, lower part
   labelled **P**. The **upper terminal is marked −**, the **lower + **; $V_T$ is marked across the
   device and $i_T$ is arrowed **upward** alongside — i.e. conventional current flows from the
   P-side up through the device, as forward bias requires.
2. **Middle:** the **tunnel-diode symbol** — an **unfilled triangle pointing up** with a bar across
   its apex whose **ends turn downward** at both sides. Cathode uppermost.
3. **Right:** the alternative symbol — a **filled half-disc (semicircle)** on the line.

> ⚠ VERIFY **C2.24** ·L2 p24 — in **Fig. 54.18** the **middle symbol has both of its terminals
> marked "−"**. The left and right symbols are each marked **− at the top, + at the bottom**, and
> the middle one must match. A two-terminal device with two negative terminals has no defined bias.
> Also on p23, the inventor's name is printed "**Dr. Leo Easki**" for **Leo Esaki**. See
> `_verification-log.md`.

### (b) V/I characteristic ·L2 p24

[fig ·L2 p24] **Fig. 54.19 — the characteristic.** Ordinate $i_T$, abscissa $V_T$. From the origin
the current **rises very steeply** to a maximum at point **A** $(V_P,\,I_P)$; it then **falls** to
a minimum at point **B** $(V_V,\,I_V)$; beyond B it **rises steeply again** towards point **C**.
Dashed horizontal lines mark $I_P$ and $I_V$; ticks on the abscissa mark $V_P$ and $V_V$. The band
of the plot between $V_P$ and $V_V$ is **hatched and labelled "Negative Resistance"**. A second,
much lower curve rising from the origin shows the ordinary-diode (non-tunnelling) current for
comparison.

[derivation ·L2 p24] **Reading the curve.**

- **Forward bias produces immediate conduction** — current begins to flow at once, and rises to
  the **peak current $I_P$** at the **peak voltage $V_P$** (point A).
- **Increasing the voltage past $V_P$ makes the current *decrease*** until it reaches the **valley
  current $I_V$** at the **valley voltage $V_V$** (point B).
- **Beyond $V_V$ the current rises again**, exactly as in an ordinary diode.
- Between **A and B** the current falls as the voltage rises. The diode therefore possesses a
  **negative resistance $-R_N$** over that span.

**Why negative resistance matters** ·L2 p24 — a positive resistance consumes power; **a negative
resistance produces power**. Placed in a tank circuit, it **offsets the losses in the L and C** and
so **permits sustained oscillations**. This makes the tunnel diode a **very-high-frequency
oscillator**.

> ⚠ VERIFY **V2.18** ·L2 p24 — the page argues that "this resistance **increases as we go from
> point A to B** because as voltage is increased, current keeps decreasing which means that diode
> negative resistance keeps increasing." **This is not true of the negative resistance.** The
> negative resistance is the **slope** quantity
> $$R_N=-\frac{dV_T}{di_T}$$
> and at **both** A and B the curve is flat ($di_T/dV_T=0$), so $R_N$ is **infinite at A, infinite
> at B, and passes through a minimum somewhere in between** — it is not monotonic. What *does*
> increase monotonically from A to B is the **static (chord) ratio $V_T/i_T$**, which is a positive
> quantity and is not the negative resistance at all. Correct statement:
> $$\boxed{\;R_N=-\frac{dV_T}{di_T}\ \text{is least in the middle of AB and unbounded at both ends}\;}$$
> This matters for §54.7(f): the Q-point for an amplifier or oscillator is placed **near the middle
> of AB**, precisely because that is where $|R_N|$ is smallest and most nearly constant. See
> `_verification-log.md`.

### (c) Tunnelling theory ·L2 p24

The mechanism, in energy-band terms:

1. **At zero forward bias** the **conduction-band electron levels in the N-region are slightly out
   of alignment** with the **valence-band hole levels in the P-region**.
2. **A slight forward voltage brings the levels into alignment**, and **some electrons cross over**
   — that crossing is the tunnelling.
3. **At $V_P$ the two bands are exactly aligned**, so **all the conduction-band electrons of the
   N-region can cross into the valence band of the P-region**: the current is at its **maximum,
   $I_P$**.
4. **Past $V_P$ the bands gradually go out of alignment again** and the current falls, reaching its
   **minimum (valley) current $I_V$** when they are **totally out of alignment**, at $V_V$.
5. **Beyond $V_V$** the device conducts like an **ordinary p-n diode**.

**Speed.** Tunnelling is **much faster than ordinary carrier crossing**, which gives the device its
very **short switching time** — hence its use in **high-speed computer memories** and
**high-frequency oscillators**. ·L2 p24

### (d) Diode parameters ·L2 p25

**(i) Negative resistance $-R_N$** — the resistance offered in the negative-resistance region,
**equal to the reciprocal of the slope of the characteristic there**:

[eq: tunnel-negative-resistance]

$$\boxed{\;R_N=-\frac{dV}{dI}\;}$$

Its value depends on the semiconductor material and ranges from about **−10 Ω to −200 Ω**.

**(ii) The ratio $I_P/I_V$** ·L2 p25 — the figure of merit that separates the materials:

[table ·L2 p25]

| Material | $I_P/I_V$ | Negative resistance | Noted for |
|---|---|---|---|
| **Si** | 3 : 1 | $R_N=-200/I_P$ | switching at **high ambient temperature** |
| **Ge** | 6 : 1 | $R_N=-120/I_P$ | general purpose |
| **GaAs** | ≈10 : 1 | ≈ that of Si | used **exclusively in oscillators** |
| **GaSb** | ≥12 : 1 | $R_N=-60/I_P$ | **lowest resistance of all → lowest noise** |

> ⚠ VERIFY **C2.25** ·L2 p25 — the expressions $R_N=-200/I_P$, $-120/I_P$, $-60/I_P$ are printed
> **without stating the units of $I_P$**. Dimensionally the numerators must be voltages, and for
> the results to land inside the page's own quoted range of −10 Ω to −200 Ω, **$I_P$ must be in
> milliamperes** (numerators in mV): $I_P=1\ \mathrm{mA}$ gives $R_N=-200\ \Omega$ for silicon and
> $I_P=10\ \mathrm{mA}$ gives $-20\ \Omega$, both inside the range. Read in amperes the same
> formula would give −200 kΩ, a thousandfold outside it. See `_verification-log.md`.

### (e) Equivalent circuit ·L2 p25

[fig ·L2 p25] **Fig. 54.20.** From the left terminal, **$L_S$** in series along the top wire to a
node; **$C$** and **$-R_N$** hang from that node to the bottom rail **in parallel** with each
other; **$R_S$** is in series in the bottom wire back to the right terminal.

- **$C$** — the **junction diffusion capacitance**, 1–10 pF.
- **$-R_N$** — the negative resistance.
- **$L_S$** — series inductance, **due mainly to the terminal leads**, 0.1–4 nH.
- **$R_S$** — series resistance, **due to the leads, the ohmic contact and the semiconductor
  material**, 1–5 Ω.

These four parasitics between them **limit the frequency at which the diode can be used, and set
its switching-speed limit**. ·L2 p25

### (f) Biasing ·L2 p25

A dc bias sets the **Q-point** when the diode is used as an **amplifier**, or as an **oscillator
and modulator**.

[fig ·L2 p25] **Fig. 54.21 — two characteristics with different Q-points.**
**(a)** the Q-point is placed **on the falling branch**, i.e. **in the negative-resistance region**
between the peak and the valley; a dashed vertical line drops from Q to the abscissa where the
bias voltage is marked, and the valley is labelled.
**(b)** the Q-point is placed **on the first rising branch, near the peak** — the
**positive-resistance region nearest zero** — with its bias voltage marked "Bias V".

- **(a)** is the usual choice.
- **(b)** is used in **mixer and relaxation-oscillator applications**.

### (g) Applications ·L2 p26

1. **Ultrahigh-speed switch** — tunnelling "essentially takes place at the speed of light", giving
   switching times of **nanoseconds or even picoseconds**;
2. **logic memory storage device** — because the curve is **triple-valued for current** (for a
   current between $I_V$ and $I_P$ there are three possible voltages, two of them stable);
3. **microwave oscillator at about 10 GHz** — because of its **extremely small capacitance and
   inductance and its negative resistance**;
4. **relaxation-oscillator circuits** — again the negative resistance. In this respect it is **very
   similar to the unijunction transistor**.

### (h) Advantages and disadvantages ·L2 p26

**Advantages:** 1. **low noise**, 2. **ease of operation**, 3. **high speed**, 4. **low power**,
5. **insensitivity to nuclear radiation**.

**Disadvantages:**

1. the **voltage range over which it operates properly is 1 V or less**;
2. being a **two-terminal device it provides no isolation between input and output circuits**.

> **Cross-reference.** L1's p1 topic outline promised **tunnel diodes** and never delivered them
> (see `11-diodes.md` §1.14). They are here, in Lesson 2, as Art. 54.7. Anyone following L1's gap
> map should be sent to §2.16 of this file.

---

## 2.17 Coverage and gap map

### What the p1 outline promises versus what the 26 pages deliver

| p1 topic line | Delivered? | Where |
|---|---|---|
| half-wave rectifier circuits | ✔ fully | §55.5–55.6, p2–p7 → §2.4–§2.6 |
| full-wave rectifier circuits | ✔ fully (three of them) | §55.7–55.10, p7–p13 → §2.7–§2.10 |
| ripple factor | ✔ fully, three equivalent definitions | p5, p9, p12 → §2.6, §2.7 |
| **smoothing** | ✘ **never delivered** — only a C-L-C filter drawn in passing on p12 and a block in the p1 diagram | `[added]` §2.12 |
| voltage regulation | ✔ but only as the formula $V_R=R_0/R_L$ and two numbers | p10, p12 → §2.7.7, §2.8 |
| clipping | ✔ fully, five worked examples plus six reference circuits | §52.16–52.17, p14–p18 → §2.13 |
| clamping | ✔ fully, one worked example plus four reference circuits | §52.18–52.19, p17–p20 → §2.14 |
| voltage multiplier / doublers | ✔ fully | §55.25–55.28, p21–p23 → §2.15 |
| **limiter** | ✔ under another name — the word never appears, but Examples 52.22 and Fig. 52.39 are limiters | §2.13.6–§2.13.7 |
| *(not on the outline)* tunnel diode | ✔ — 4 pages of it | §54.7, p23–p26 → §2.16 |

**Two rectifier circuits are promised in §55.4 and never drawn**: the **six-phase half-wave**
rectifier and the **three-phase bridge**. Neither appears anywhere in the 26 pages.

**One example and one figure are missing outright**: **Example 55.2** (its data is needed by
Example 55.5 — reconstructed in §2.7.7) and **Fig. 55.10** (the bridge circuit, whose figure has
been printed under the wrong number as Fig. 55.6 — V2.9). Figs. 55.5 and 55.15–55.30 are also
absent, being parts of the parent textbook's articles that this compilation skipped.

### Article ordering — for anyone trying to follow the PDF

| PDF pages | Articles | Topic |
|---|---|---|
| 1–13 | 55.1 → 55.10 | power supplies and rectifiers |
| 14–20 | **52.15 → 52.19** | clippers and clampers *(numbering jumps backwards)* |
| 21–23 | **55.25 → 55.28** | voltage multipliers *(jumps forward)* |
| 23–26 | **54.7** | tunnel diode *(jumps backwards again)* |

### Verification summary

**43 flags: 18 substantive, 25 cosmetic.**

| ID | Page | Kind | One line |
|---|---|---|---|
| **V2.1** | p2 | substantive | $V_s=V_{sm}\,wt$ — the $\sin$ has dropped out of the input definition |
| **V2.2** | p4 | substantive | half-wave efficiency printed **409.6 %**; it is 40.6 % ($4/\pi^2=40.53\,\%$) |
| **V2.3** | p4 | substantive | $I_{L2}=2I_{LM}/3\pi\sqrt2$ reduced to $I_{LM}/3\pi$ — a $\sqrt2$ lost |
| **V2.4** | p5 | substantive | $V_{L1}=V_{LM}/\sqrt2$; should be $V_{LM}/2\sqrt2$ |
| **V2.5** | p5 | substantive | $\gamma=I_{L(ac)}/I_{L(ac)}$ — self-referential; denominator is $I_{L(dc)}$ |
| **V2.6** | p5, p9 | substantive | $\gamma=V_{r(ms)}/V_{L(ms)}$ — denominator must be the **dc** value |
| **V2.7** | p6 | substantive | TUF chain drops a $\pi$ twice: $P_{dc}=V_{LM}^2/\pi R_L$, TUF $=2\sqrt2/\pi$ |
| **V2.8** | p7 | substantive | Ex 55.1(iv) gives half-wave PIV as $2V_{sm}=62$ V; it is $V_{sm}=31$ V |
| **V2.9** | p7, p11 | substantive | the figure labelled Fig. 55.6(a) is a **bridge**, not the centre-tap circuit |
| **V2.10** | p8 | substantive | $P_{dc}=I_{L(dc)}^2(R_0+R_L)$; should be $I_{L(dc)}^2R_L$ |
| **V2.11** | p9 | substantive | full-wave Fourier sixth-harmonic term $4/35$; should be $4/35\pi$ |
| **V2.12** | p9 | substantive | Ex 55.3: $\sqrt{0.55^2-49.6^2}$ — should be $0.496^2$; radicand negative as printed |
| **V2.13** | p9 | substantive | Ex 55.3: $\gamma=I_{r(max)}/I_{L(max)}$; should be $I_{r(rms)}/I_{L(dc)}$ |
| **V2.14** | p10 | substantive | Ex 55.4: symbolic $I_{L(dc)}=I_{LM}/\pi$ where $2I_{LM}/\pi$ is used |
| **V2.15** | p16 | substantive | Fig. 52.34(c) draws the series-clipper output starting at −10 V; it must be 0 |
| **V2.16** | p19 | substantive | "reverse-biases D by 10 V"; the diode sees $5+10=15$ V |
| **V2.17** | p23 | substantive | cascade multiplier's ripple frequency given as $2f$; p21 correctly gives $f$ |
| **V2.18** | p24 | substantive | claims the tunnel diode's negative resistance rises monotonically A→B |
| **C2.1** | p2, p10 | cosmetic | two of the eight promised rectifier circuits, Fig. 55.10, Fig. 55.5 and Ex. 55.2 are absent |
| **C2.2** | p3 | cosmetic | $V_B$ used in the $I_{LM}$ formula but omitted from the "Let" list |
| **C2.3** | p3 | cosmetic | $I_L = I_L M_n/2$ — subscript garble for $I_{LM}/2$ |
| **C2.4** | p4, p8 | cosmetic | 40.6 % and 81.2 % are rounded up from $4/\pi^2=40.53\,\%$, $8/\pi^2=81.06\,\%$ |
| **C2.5** | p4, p8 | cosmetic | efficiency symbol set as roman "h" for $\eta$; "effficiency" misspelt |
| **C2.6** | p4 | cosmetic | the $\cos4\omega t$ term called the "third harmonic ... four times the supply frequency" |
| **C2.7** | p5 | cosmetic | $\sqrt{I_{L1}^2+I_{L2}^2+I_{L3}^3}$ — cube instead of square |
| **C2.8** | p6, p9, p10, p22 | cosmetic | dropped $\sqrt2$ / dropped "220" in peak-value lines; answers still right |
| **C2.9** | p7, p8 | cosmetic | "Totol Output"; truncated Fig. 55.7(b) sentence; "Fig. 5.8" for 55.8 |
| **C2.10** | p8 | cosmetic | $V_{L(dc)}=0.636$ **V** — the $V_{LM}$ subscript has dropped |
| **C2.11** | p8 | cosmetic | Fig. 55.8(b), a current graph, labels its ac area "$V_L$(ac)" |
| **C2.12** | p9 | cosmetic | "$4V_{IM}$" for $4V_{LM}$; 0.305 for 0.306; $\gamma$ printed 0.482 vs 0.4796 computed / 0.4834 exact |
| **C2.13** | p10 | cosmetic | "1 k W load", "25 W" — the ohm sign rendered as W |
| **C2.14** | p10 | cosmetic | Ex 55.5 uses data from Ex 55.2, which is not in the handout |
| **C2.15** | p11 | cosmetic | "point A ... acts as an anode and point C as cathode" — reversed terminology |
| **C2.16** | p13 | cosmetic | three-phase conduction narrative: "$D_2$ ... upto $t_2$ after which $D_2$ will take over" |
| **C2.17** | p13 | cosmetic | three-phase η = 96.5 % and γ = 0.17; exact 96.8 % and 0.183 (0.177 fundamental-only) |
| **C2.18** | p14, p15 | cosmetic | "clams" for clamps; "it is forward-biases B which acts as a short" |
| **C2.19** | p16 | cosmetic | Fig. 52.33(c) labels the clipped level "0.7 V" where −0.7 V is meant |
| **C2.20** | p18 | cosmetic | Fig. 52.40: all three ordinates labelled $V_{in}$; panel (c) level "5 V" for −5 V |
| **C2.21** | p19, p20 | cosmetic | Ex 52.23: "$t_2\to t_2$"; "$C_R$" for $CR$; "1 F" for 1 µF; wrong figure cite; ms/s unit slips; "15 V" for −15 V |
| **C2.22** | p20 | cosmetic | "Fig. 52.44 and 52.45" for 52.45 and 52.46; Fig. 52.47(b) axis labelled $V_{in}$; level $V_1$ for $-V_1$ |
| **C2.23** | p22, p23 | cosmetic | overstruck −/+ on $C_1$ in Fig. 55.33(a); "$C_2$*"; "If is seen"; "$D_3$ conduct" |
| **C2.24** | p23, p24 | cosmetic | Fig. 54.18 middle symbol has both terminals marked "−"; "Leo Easki" for Leo Esaki |
| **C2.25** | p25 | cosmetic | $R_N=-200/I_P$ etc. quoted without units; $I_P$ must be in mA |

### Verified sound, no flag

- Half-wave: $V_{L(dc)}=V_{LM}/\pi=0.318V_{LM}$ ✓ · $V_L=V_{LM}/2$ ✓ · $K_f=\pi/2=1.571$ ✓ ·
  $\gamma=\sqrt{1.57^2-1}=1.2103$ ✓ (exact $\sqrt{\pi^2/4-1}=1.2114$) · PIV $=V_{sm}$ ✓ ·
  TUF final answer 0.287 ✓ ($2\sqrt2/\pi^2=0.28658$) · practical TUF 0.2 and $0.2\times1000=200$ W ✓
- Half-wave Fourier series coefficients $1/\pi$, $1/2$, $2/3\pi$, $2/15\pi$ ✓ all four
- $I_{L(ac)}=0.385I_{LM}$ from three harmonics ✓ (recomputed 0.38525; exact 0.38559) and
  $0.385/0.318=1.2107$ ✓
- Full-wave: $2/\pi=0.636$ ✓ · $1/\sqrt2=0.707$ ✓ · $\eta=8/\pi^2$ ✓ · PIV $=2V_{sm}$ (centre-tap)
  and $V_{sm}$ (bridge) ✓ · TUF 0.693 ✓ · $\gamma$ exact $\sqrt{\pi^2/8-1}=0.4834$ ✓
- Bridge: $I_{LM}=(V_{sm}-2V_B)/(R_0+R_L)$ ✓ · $\eta=81.2\,\%/(1+2r_d/R_L)$ ✓ ·
  $V_R=(R_S+2r_d)/R_L$ ✓ — the factor 2 is right in all three
- Example 55.1: 31 V, 15.5 V, 0.31 A, 0.155 A, 2.4 W, 11.9 V ✓ all (only the PIV is wrong, V2.8)
- Example 55.3: 156 V, 78 V, 49.6 V, 55 V, 23.8 V, 0.78 A, 0.496 A, 0.55 A, 0.238 A, 0.48,
  0.25 A, 30.25 W ✓ **every printed answer**
- Example 55.4: 424 V, 0.414 A, 0.263 A, 263 V, 126.8 V, 79.2 % ✓ all
- Example 55.5: 1.2 A, 12 V, 2.5 %, 79.2 %, 40 V, 60 V ✓ all — and the reconstructed Ex 55.2 data
  is self-consistent to 0.2 % with a 0.7 V silicon drop
- Example 52.20: $15\times1000/1100=13.64$ V ✓
- Example 52.23: $T=1$ ms ✓ · $\lambda=10$ ms ✓ · $5\lambda=50$ ms ✓ · $V_o=-15$ V ✓ ·
  with $R=100\ \Omega$, $\lambda=0.1$ ms and $5\lambda=0.5$ ms $=T/2$ ✓ · swing 15 V in and out ✓
- Three-phase half-wave: $0.83V_{sm}$ ✓ (exactly $3\sqrt3/2\pi=0.8270$) · $1.17V_s$ ✓ ·
  swing $V_{sm}$ down to $0.5V_{sm}$ ✓
- Three-phase full-wave: mean $0.83V_{sm}$ ✓ · ripple at $6f$ ✓ · $\tfrac13$ / $\tfrac23$ cycle
  conduction ✓
- Voltage doublers: $V_{C2}=2V_m$ from the outer-loop KVL ✓ · $2\times220\sqrt2=622$ V (printed
  620 V from $V_m=310$) ✓ · PIV $=2V_m$ for every multiplier diode ✓ · full-wave doubler ripple at
  $2f$ ✓
- Cascade multiplier ladder: $C_1\to V_m$, $C_2,C_3,C_4\to2V_m$ each, and hence $2V_m$, $3V_m$,
  $4V_m$ at the three tapping points ✓ — the arithmetic of the ladder is right even though the
  ripple-frequency claim is not (V2.17)
- Fig. 52.36 double-ended clipper: clipping at +10 V and −5 V ✓ matches the drawn trapezoid
- Fig. 52.39(a)–(d) diode/battery orientations ✓ all four waveforms follow from the drawn circuits
- Fig. 52.45–52.48 clamping levels and the $2V$ swing ✓ all four
- Tunnel diode: depletion width $10^{-5}$ mm $=10$ nm ✓ plausible · tunnelling below 0.05 V ✓ ·
  $I_P/I_V$ ratios and the 1 V operating ceiling ✓ · $L_S$ 0.1–4 nH, $C$ 1–10 pF, $R_S$ 1–5 Ω ✓

**No page of this document was illegible.** All 26 pages were read in the render at full
resolution, and every figure described above was inspected directly — several at 6–14× zoom to
resolve diode orientations, battery plate lengths and capacitor polarity marks. Two figures needed
that treatment and are recorded as read-with-difficulty rather than illegible:

- **Fig. 52.38 (p17)** — the battery plate lengths *are* legible at 14× (short-left/long-right in
  (a), reversed in (b)), but the $V_{in}$ and $V_o$ markers are **span arrows carrying no polarity
  information**, so the circuits alone do not fix the sign of the output. The plotted waveforms do;
  §2.13.7 states the resulting formulas and says so explicitly.
- **Fig. 55.33(a) (p22)** — $C_1$'s upper plate carries an **overstruck "−" on top of the "+"**
  (C2.23). The "+" is the physically correct mark, since the two capacitors must be series-aiding
  to give $2V_m$.

The four photographic figures (p1 "Single filament Rectifier", p23 "Discrete commercial Si tunnel
diode") are described but, being third-party photographs, are never reproduced.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
