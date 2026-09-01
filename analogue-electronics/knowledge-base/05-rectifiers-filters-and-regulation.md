---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "05 — Rectifiers, Filters and Voltage Regulation"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 46-56"
pages: "J p46-p56"
tier: primary
file_role: topic
subtopics:
  - "the dc power supply as a four-block chain: transformer, rectifier, smoothing, stabilising"
  - "what a rectifier diode is: high power rating, high peak inverse voltage, silicon"
  - "half-wave rectifier: circuit, input and output waveforms, operation, ripple frequency"
  - "half-wave average value I_dc = I_m/pi = 0.3183 I_m by integration"
  - "half-wave rms value I_rms = I_m/2, and the dc and ac powers"
  - "half-wave rectification efficiency 4/pi^2 = 40.5 %"
  - "half-wave ripple factor sqrt(pi^2/4 - 1) = 1.21, and the effective-rms identity"
  - "centre-tapped full-wave rectifier: circuit, waveforms, operation, doubled ripple frequency"
  - "full-wave average 2I_m/pi and rms I_m/sqrt2"
  - "full-wave rectification efficiency 8/pi^2 = 81.1 %"
  - "full-wave ripple factor sqrt(pi^2/8 - 1) = 0.48"
  - "bridge rectifier: circuit, diode pairs, waveforms"
  - "unsolved half-wave problem: 10:1 transformer, 250 V peak input, r_f = 20 ohm, R_L = 800 ohm"
  - "smoothing circuits: why a filter is needed and the three kinds"
  - "capacitor filter: circuit, charge and discharge exponentials, half-wave and full-wave waveforms"
  - "choke-input filter: circuit, waveforms, how the inductor and capacitor share the work"
  - "capacitor-input (Pi) filter: C-L-C circuit and waveforms"
  - "zener diode: symbol, construction, operation, V-I characteristic"
  - "zener equivalent circuits: on state as a battery, off state as an open circuit"
  - "zener shunt-regulator analysis: off-state divider test and on-state currents"
  - "worked regulator: 40 V supply, 15 V zener, R = 500 ohm, R_L = 800 ohm"
  - "zener voltage clipping: one-sided and two-sided circuits with waveforms"
key_equations: [rectifier-idc-general-j, hw-idc-j, hw-irms-j, rectifier-powers-j, hw-efficiency-j, irms-dc-ac-j, hw-ripple-j, fw-idc-j, fw-irms-j, fw-efficiency-j, fw-ripple-j, capacitor-charge-j, capacitor-discharge-j, zener-off-divider-j, zener-on-currents-j, zener-power-j]
prerequisites:
  - "the junction diode, forward and reverse bias, the forward drop and breakdown (·J p33-p45; 04-diodes.md)"
  - "transformers and turns ratio (·J p29-p32; 03-capacitors-inductors-and-transformers.md)"
  - "rms and average values of a sinusoid; the RC time constant"
leads_to:
  - "clippers, clampers and voltage multipliers (12-rectifiers.md §2.13-§2.15 — not in this range)"
  - "transistor series regulators (·J p53 names the transistor regulator and never returns to it)"
  - "the bipolar junction transistor (·J p57 onward)"
verification_flags: 18
tags: [rectifier, half-wave, full-wave, centre-tap, bridge-rectifier, rectification-efficiency, ripple-factor, smoothing, capacitor-filter, choke-input-filter, pi-filter, zener-diode, voltage-regulator, shunt-regulator, voltage-clipping, limiter, power-supply]
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
  ⚠ ILLEGIBLE = page, line or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 05 — Rectifiers, Filters and Voltage Regulation

Scope: **·J p46–p56**, eleven pages of the course's own lecture notes. It is the second half of the
power-supply story: the block diagram of a dc supply, then each block in turn — **rectifier**
(half-wave, centre-tapped full-wave, bridge), **smoothing filter** (capacitor, choke-input,
capacitor-input Π), and **stabiliser** (the zener shunt regulator). It closes on zener **voltage
clipping**.

**This range is mostly derivation and arithmetic.** Four figures of merit are derived from first
principles by integration — $I_{dc}$, $I_{rms}$, $\eta$, ripple factor — once for the half-wave
circuit and again for the full-wave circuit. That is where the exam marks are.

**This is tier 1.** `12-rectifiers.md` (tier 2, a textbook compilation) covers the same rectifier
ground more fully and adds PIV, TUF and Fourier content this range never mentions. But **this
document is the only *primary* source in the knowledge base for smoothing filters and for zener
regulation as the course teaches them** — see §5.26.

---

## 5.0 Citation, and where this range's gaps are

**Citation.** `·J p47` means **PDF page 47**. The document's own printed page number runs **one
behind the PDF page** — PDF p47 shows printed "46" — and that offset holds unbroken across the
whole document. Everything below cites **PDF pages only**.

### The section starts without a heading ⚠

**·J p46 opens with the power-supply block diagram and no heading above it.** The page begins
directly with the figure. The whole lower half of ·J p45 is blank — the varactor section ends
part-way down it — so a section heading ("Power supplies", or similar) was almost certainly present
and has been lost with that blank space, exactly as happened at ·J p31, ·J p33 and ·J p57. **No
heading is invented here.** The **RECTIFIERS** heading further down ·J p46 *is* on the page and is
genuine.

### Redaction map for ·J p46–p56

Two pages in this range carry **opaque yellow blocks** over text. Contrast recovery finds nothing
underneath — the text is destroyed, not merely hidden. Each is marked `⚠ REDACTED` at the point of
use.

[table]

| Page | Where | Block width | Approx. characters | Recovered? |
|---|---|---|---|---|
| ·J p53 | first line of **Construction** (zener) | 552 px | ≈ 45–50 | **No** — subject inferable, wording not |
| ·J p53 | first line of **Operation** (zener) | 384 px | ≈ 30–35 | **No** — subject inferable, wording not |
| ·J p55 | a label above the regulator data block | 105 px | ≈ 8–9 | **No**, but the pattern is unambiguous: it is the word **Example** |

Character counts are estimated from the page's own body-text metric of about 11.8 px per character.

### Lines lost at the page break

Three pages open with a text line **clipped by the top page margin** — only the descenders survive.
These are not redactions; the PDF's page box cuts them.

[table]

| Page | What survives | Reading |
|---|---|---|
| ·J p48 | bottom pixel-rows of $I_{rms} = \sqrt{I_{dc}^{2} + I_{ac}^{2}}$ | **recoverable** — the identical trio is printed in full on ·J p49 |
| ·J p49 | four glyph fragments: $\pi$ … 0 … $\pi$ … $\pi$ … | **partly** — it is the evaluation line of the full-wave average; see §5.9 |
| ·J p52 | "first circuit." (tops of letters clipped) | the **tail** of a sentence whose earlier line is gone entirely |

The p52 case is a genuine **content gap**: ·J p51 ends "…has more d.c component than the half
waveform rectifier", and ·J p52 opens "first circuit." — at least one full line between them is
absent. Nothing here fills it.

---

## 5.1 The dc power supply — the four blocks ·J p46

[fig ·J p46] **Block diagram of a dc power supply, drawn left to right, four boxes in a chain.**

- Far left, an arrow labelled **input** feeds the chain. Beneath it a small graph: vertical axis
  $V$, horizontal axis $t$, origin marked 0, carrying **one full sinusoid** — a positive hump then
  a negative hump. This is the mains waveform.
- **Box 1 — Transformer** → **Box 2 — Rectifier** → **Box 3 — Smoothing circuit** → **Box 4 —
  Stabilising circuit**, each pair joined by a right-pointing arrow.
- The word **filter** is printed above Box 3, naming it.
- Far right, an arrow labelled **output**, with a second small graph beneath: axes $V$ and $t$,
  origin 0, carrying a **flat horizontal line** at a positive level — pure dc.

[def] Read the diagram as a job list. Each block removes one defect of the block before it:

1. **Transformer** — scales the mains sinusoid to the peak the circuit needs; also isolates it.
2. **Rectifier** — makes the waveform one-sided. It is still not dc: it is a train of humps.
3. **Smoothing circuit (filter)** — removes most of the ac content left in those humps.
4. **Stabilising circuit** — holds the output constant against changes in supply and in load.

Blocks 2, 3 and 4 are §5.2–§5.13, §5.14–§5.17 and §5.18–§5.22 respectively.

---

## 5.2 What a rectifier is ·J p46

[def ·J p46] A **rectifier** is built from **rectifier diodes** — diodes with a high power rating
and a high peak inverse voltage / breakdown voltage. The usual material is **silicon**.

> ⚠ VERIFY **JC5.11** ·J p46 — printed: *"…diodes which have a high power rating and peak inverse
> voltage/ breakdown voltage."* The slash equates two different things. **Peak inverse voltage** is
> a *circuit* quantity — the largest reverse voltage the diode actually sees in the circuit it is
> wired into. **Breakdown voltage** is a *device* rating. A diode is chosen so that
> $\mathrm{PIV} < V_{BR}$; they are never the same number. The same conflation was flagged at
> ·J p35 as **JV4.4** in `04-diodes.md`. Nothing computed here changes.
> See `_verification-log.md`.

[def ·J p46] The notes name **two types**:

- **(a)** Half-wave rectifier — §5.3
- **(b)** Full-wave rectifier — §5.8 (centre-tapped) and §5.12 (bridge)

Silicon is preferred because it tolerates the higher junction temperature and the higher reverse
voltage that rectification demands. [added]

---

## 5.3 The half-wave rectifier (HWR) ·J p46

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_m$ | peak value of the rectified sinusoid at the load | V | 25 V (§5.13) |
| $I_m$ | peak load current, $I_m = V_m/(R_L + r_f)$ | A | 30 mA |
| $i$ | instantaneous load current, $i = I_m\sin\theta$ | A | — |
| $\theta$ | angle, $\theta = \omega t$ | rad | $0 \to 2\pi$ |
| $I_{dc}$ | average (dc) load current | A | $0.318\,I_m$ |
| $I_{rms}$ | total rms load current | A | $0.5\,I_m$ |
| $I_{ac}$ | rms value of the ac (ripple) content | A | $0.385\,I_m$ |
| $R_L$ | load resistance | Ω | 800 Ω |
| $r_f$ | diode forward (bulk) resistance | Ω | 20 Ω |
| $P_{dc}$ | dc power delivered to the load | W | — |
| $P_{ac}$ | ac power drawn from the source | W | — |
| $\eta$ | rectification efficiency | — | 0.405 max |

> **Notation clash — $\eta$.** This range uses $\eta$ for **rectification efficiency**. ·J p35
> (`04-diodes.md` §4.6) uses the *same letter* for the diode equation's **ideality factor**
> ($\eta = 1$ for Ge, $\eta = 2$ for Si). Two unrelated quantities, one symbol, in the same set of
> notes. Check which chapter you are in. [added]

> **Notation clash — the subscript $f$.** $r_f$ is the diode's **forward** resistance; $f$ alone,
> when it appears in filter work, is **frequency**. [added]

[fig ·J p46] **Half-wave rectifier circuit.** A transformer on the left: two input terminals (small
circles) feed the primary; primary and secondary are drawn as two coil stacks separated by the
vertical core bars, the primary side labelled **Input**. From the **top** of the secondary a wire
runs right through a **diode D**, drawn with its triangle pointing right (anode left, cathode
right). Beyond D the wire reaches the top output terminal. A resistor **$R_L$**, drawn as a
vertical box, hangs from that wire down to the bottom rail, which returns to the bottom of the
secondary and to the bottom output terminal. The output is taken across $R_L$ and labelled
**Output**. One diode, one load — that is the whole circuit.

[fig ·J p46] **Half-wave waveforms, two graphs stacked on a shared time axis.**

- **Upper — input.** Vertical axis $I$ (current), horizontal axis **time**. Three full sinusoids:
  positive hump, negative hump, repeating.
- **Lower — output.** Same axes. **Only the positive humps survive**, separated by flat runs along
  the axis where the negative humps were. The time axis is ticked at $\pi$, $2\pi$, $3\pi$, $4\pi$,
  $5\pi$ — the humps sit in $0\!-\!\pi$, $2\pi\!-\!3\pi$, $4\pi\!-\!5\pi$.

**Operation** ·J p46

- **First half cycle** — the diode is **forward biased**, current passes, an output appears across
  $R_L$.
- **Second half cycle** — the diode is **reverse biased**, no current passes, there is no output at
  $R_L$.

Only the positive half cycles reach the output. They are called **ripples**, and their frequency is
**the same as** the input frequency.

$$f_{\text{ripple, HW}} = f_{\text{in}}$$

*[added] That single fact is the half-wave circuit's biggest practical weakness: the lowest ripple
component sits at the mains frequency itself, which is the hardest frequency to filter out. The
full-wave circuits of §5.8 and §5.12 double it, and the filter's job gets easier by the same factor.*

---

## 5.4 Half-wave: the average (dc) value ·J p47

[derivation ·J p47] The average is taken over a **whole period**, $0$ to $2\pi$, but the current
exists only over $0$ to $\pi$:

[eq: rectifier-idc-general-j]

$$I_{dc} = \frac{1}{2\pi}\int_{0}^{\pi} i\,d\theta \qquad \text{where } i = I_m\sin\theta$$

$$I_{dc} = \frac{1}{2\pi}\int_{0}^{\pi} I_m\sin\theta\,d\theta$$

$$I_{dc} = \frac{I_m}{2\pi}\Big[-\cos\theta\Big]_{0}^{\pi} = \frac{I_m}{2\pi}\big[-\cos\pi + \cos 0\big] = \frac{I_m}{2\pi}(2)$$

[eq: hw-idc-j]

$$\boxed{\;I_{dc} = \frac{I_m}{\pi} = 0.3183\,I_m\;}$$

**Verified.** $1/\pi = 0.31830989$ ✓ — the page's 0.3183 is right to four figures.

*[added] The $2\pi$ in the denominator against the $\pi$ in the upper limit is the whole story of
the half-wave circuit. Average the same hump over half the period and you get $2I_m/\pi$ — which is
exactly the full-wave answer in §5.9.*

> ⚠ VERIFY **JC5.1** ·J p47 — the evaluation line prints
> $$\frac{I_m}{2\pi}\Big[-\cos\theta\Big]_{0}^{\pi}\,d\theta = \frac{I_m}{2\pi}\big[-\cos\pi + \cos 0\big]$$
> with a **stray $d\theta$ after the integral has already been evaluated**. The $d\theta$ belongs
> with the integral sign on the line above; once the antiderivative is in square brackets it is
> gone. The line also drops its "$I_{dc} =$" label and starts straight at the fraction. Nothing
> computed changes. See `_verification-log.md`.

[eq: rectifier-powers-j] **The dc power in the load** ·J p47:

$$\boxed{\;P_{dc} = I_{dc}V_{dc} = I_{dc}^{2}R_L\;}$$

- $V_{dc} = I_{dc}R_L$ — the average load voltage, in V

---

## 5.5 Half-wave: the rms value ·J p47

[derivation ·J p47] Square, average over the whole period, take the root. Use
$\sin^{2}\theta = (1-\cos 2\theta)/2$:

$$I_{rms}^{2} = \frac{1}{2\pi}\int_{0}^{\pi} i^{2}\,d\theta = \frac{1}{2\pi}\int_{0}^{\pi}\big(I_m\sin\theta\big)^{2} d\theta$$

$$I_{rms}^{2} = \frac{I_m^{2}}{2\pi}\int_{0}^{\pi}\frac{1-\cos 2\theta}{2}\,d\theta = \frac{I_m^{2}}{4}$$

[eq: hw-irms-j]

$$\boxed{\;I_{rms} = \frac{I_m}{2}\;}$$

**Verified numerically.** Sampling $i = \sin\theta$ on $[0,\pi]$ and zero on $[\pi,2\pi]$ over two
million points gives mean $= 0.3183099$ and rms $= 0.5000000$ — both exactly as printed. ✓

*[added] Note that this is **not** $I_m/\sqrt2$. A full sinusoid has rms $I_m/\sqrt2$; the
half-wave output is that sinusoid for half the time and zero for the other half, so its **mean
square is halved** and the rms falls by a further $\sqrt2$:*

$$\frac{I_m}{\sqrt2}\cdot\frac{1}{\sqrt2} = \frac{I_m}{2}$$

*Almost every half-wave-versus-full-wave difference in this file traces back to that one factor.*

[eq] **The ac power drawn from the source** ·J p47 — the current flows through the diode as well as
the load, so both resistances take power:

$$\boxed{\;P_{ac} = I_{rms}^{2}\left(R_L + r_f\right) = \left(\frac{I_m}{2}\right)^{2}\left(R_L + r_f\right)\;}$$

---

## 5.6 Half-wave: rectification efficiency ·J p47

[def ·J p47] **Rectification efficiency** $\eta$ is the dc power delivered to the load divided by
the ac power supplied to the circuit.

[derivation ·J p47]

$$\eta = \frac{P_{dc}}{P_{ac}} = \frac{I_{dc}^{2}R_L}{I_{rms}^{2}\left(R_L + r_f\right)} = \frac{\left(\dfrac{I_m}{\pi}\right)^{2} R_L}{\left(\dfrac{I_m}{2}\right)^{2}\left(R_L + r_f\right)}$$

$$\eta = \frac{4}{\pi^{2}}\cdot\frac{R_L}{R_L + r_f}$$

[eq: hw-efficiency-j]

$$\boxed{\;\eta_{\text{HW}} = \frac{4}{\pi^{2}\left(1 + \dfrac{r_f}{R_L}\right)} = \frac{0.405}{1 + \dfrac{r_f}{R_L}}\;}$$

**With $r_f \ll R_L$** ·J p47:

$$\boxed{\;\eta_{\text{HW,max}} = \frac{4}{\pi^{2}} = 0.405 = 40.5\,\%\;}$$

**Verified.** $4/\pi^{2} = 0.40528473$, i.e. **40.53 %**. The page's 40.5 % is the correct rounding
to three figures. ✓

*[added] Read the number properly: **even with a perfect diode, under 41 % of the ac power becomes
dc power.** The rest stays in the load as ac — which is exactly the ripple that §5.7 measures and
§5.15 filters out.*

> ⚠ VERIFY **JV5.1** ·J p47 — the efficiency fraction is printed with **the exponent on the wrong
> bracket**:
> $$\eta = \frac{\left(\dfrac{I_m}{\pi}\right)^{2} R_L}{\left(\dfrac{I_m}{2}\right)\left(R_L + r_f\right)^{2}}$$
> The denominator is $P_{ac} = I_{rms}^{2}(R_L+r_f)$, so the square belongs on $I_m/2$, **not** on
> $(R_L+r_f)$. Two checks: (i) **dimensionally** the printed denominator is
> $\mathrm{A}\cdot\Omega^{2}$ against a numerator of $\mathrm{A}^{2}\Omega$, so the ratio is not
> dimensionless; (ii) **algebraically** the printed form does not reduce to the $4/\pi^{2}$ the
> very next line states — only the corrected form does. Correct form:
> $$\boxed{\;\eta = \frac{\left(\dfrac{I_m}{\pi}\right)^{2} R_L}{\left(\dfrac{I_m}{2}\right)^{2}\left(R_L + r_f\right)}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **JC5.2** ·J p47, repeated ·J p49 — the last step is typeset as
> $$\eta = 0.\frac{405}{\left(1 + \dfrac{r_f}{R_L}\right)}$$
> with **"0." stranded outside the fraction**. It is a broken decimal, not a coefficient: the
> intended reading is $\dfrac{0.405}{1 + r_f/R_L}$. The full-wave version on ·J p49 breaks the same
> way, as $0.\dfrac{811}{(\cdots)}$. Nothing computed changes. See `_verification-log.md`.

---

## 5.7 Half-wave: ripple factor ·J p47–p48

[def ·J p47] **Ripple factor** is the ratio of the ac current to the dc current in the output.
Smaller is better; zero would be a perfect battery.

[fig ·J p47] **What "ac content" means, two graphs stacked.**

- **Upper.** Axis $I$ (current) against **time**, origin 0. The plain half-wave train: humps in
  $0\!-\!\pi$, $2\pi\!-\!3\pi$, $4\pi\!-\!5\pi$, ticked at $\pi \ldots 5\pi$.
- **Lower.** The *same* train redrawn with a **horizontal dashed line** across it labelled **dc**,
  and the wavy part above and below that line labelled **ac**. The picture is the definition: the
  output is a dc level with an ac wave riding on it.

[derivation ·J p47–p48] The rms of the whole waveform contains both parts, in quadrature:

[eq: irms-dc-ac-j]

$$\boxed{\;I_{rms}^{2} = I_{dc}^{2} + I_{ac}^{2} \qquad\Longrightarrow\qquad I_{ac} = \sqrt{I_{rms}^{2} - I_{dc}^{2}}\;}$$

Divide through by $I_{dc}$:

$$\frac{I_{ac}}{I_{dc}} = \sqrt{\frac{I_{rms}^{2}}{I_{dc}^{2}} - 1} = \sqrt{\frac{\left(I_m/2\right)^{2}}{\left(I_m/\pi\right)^{2}} - 1} = \sqrt{\frac{\pi^{2}}{4} - 1}$$

[eq: hw-ripple-j]

$$\boxed{\;\gamma_{\text{HW}} = \frac{I_{ac}}{I_{dc}} = \sqrt{\frac{\pi^{2}}{4} - 1} = 1.21\;}$$

- $\gamma$ — ripple factor, dimensionless. *The notes use no symbol for it; $\gamma$ is added here
  to match `12-rectifiers.md`.* [added]

**Verified.** $\pi^{2}/4 = 2.4674011$; $\sqrt{2.4674011 - 1} = 1.2113633$. The page's 1.21 is the
correct rounding. ✓ And $(I_m/2)^2 / (I_m/\pi)^2 = \pi^2/4$ ✓.

*[added] **1.21 means there is 21 % more ac in the output than dc.** An unfiltered half-wave
rectifier is not a dc supply at all — which is why §5.15 exists.*

> ⚠ VERIFY **JC5.3** ·J p47, repeated ·J p49 — the ripple-factor definition is printed
> *"the ratio of ac to dc current ( $I_1 ac / I_1 dc$ )"* — a **spurious subscript 1** attached to
> both currents, and "ac"/"dc" set as italic variables rather than subscripts. It should read
> $I_{ac}/I_{dc}$. A font artefact; nothing computed changes. See `_verification-log.md`.

> ⚠ ILLEGIBLE ·J p48 — the **first line of the page is clipped by the top page margin**; only the
> bottom pixel rows of the glyphs survive, showing $I_{rms}$, a radical sign, and the subscripts
> "dc" and "ac". It is $I_{rms} = \sqrt{I_{dc}^{2} + I_{ac}^{2}}$ — the same line ·J p49 prints in
> full in its own ripple-factor block, in the same three-line order. Recovered with high
> confidence; recorded because it is an inference, not a reading.

---

## 5.8 The centre-tapped full-wave rectifier ·J p48

[fig ·J p48] **Circuit — "(a) Centre-Tapped Rectifier".** A transformer on the left, input
terminals at far left labelled **Input**. The secondary is **tapped at its centre**; the tap is the
return rail. Polarity marks are drawn on the secondary: **$+\,-$** at the top end, **$-\,+$** at the
bottom end, showing that the two halves are in antiphase.

- From the **top** of the secondary a wire runs right through diode **$D_1$** (triangle pointing
  right).
- From the **bottom** of the secondary a wire runs right through diode **$D_2$** (triangle also
  pointing right).
- The two diode cathodes join at a common node on the right.
- **$R_L$**, drawn as a horizontal box labelled **Output**, sits between that common node and the
  **centre tap**. Arrowheads on the connecting wires show both diode currents entering $R_L$ from
  the same side.

[fig ·J p48] **Waveforms, two graphs stacked.**

- **Upper — input.** $I$ (current) against **time**: three full sinusoids.
- **Lower — output.** A **continuous train of positive humps with no flat gaps**, ticked at $\pi$,
  $2\pi$, $3\pi$, $4\pi$, $5\pi$. Each hump is labelled with the diode that produced it, in order:
  **$D_1$, $D_2$, $D_1$, $D_2$, $D_1$**.

**Operation** ·J p48

- **Positive-going first half cycle** — $D_1$ is forward biased, $D_2$ reverse biased. Output at
  $R_L$ comes from $D_1$.
- **Second half cycle** — $D_2$ is forward biased, $D_1$ reverse biased. Output at $R_L$ comes from
  $D_2$.

Because the two currents flow through $R_L$ **in the same direction**, both appear on the positive
side of the time line. Their frequency is **twice** the input frequency:

$$f_{\text{ripple, FW}} = 2f_{\text{in}}$$

*[added] The centre tap is doing the polarity inversion. Each half-secondary is a separate source,
180° out of phase with the other, and each drives the load through its own diode — so the load sees
the magnitude of the sine, $|V_m\sin\omega t|$, for the whole cycle.*

---

## 5.9 Full-wave: average and rms values ·J p48–p49

[derivation ·J p48–p49] Because the output now repeats every $\pi$, the averaging period is $\pi$,
not $2\pi$ — that is the only change:

$$I_{dc} = \frac{1}{\pi}\int_{0}^{\pi} i\,d\theta \qquad \text{where } i = I_m\sin\theta$$

$$I_{dc} = \frac{1}{\pi}\int_{0}^{\pi} I_m\sin\theta\,d\theta = \frac{I_m}{\pi}\Big[-\cos\theta\Big]_{0}^{\pi} = \frac{I_m}{\pi}(2)$$

[eq: fw-idc-j]

$$\boxed{\;I_{dc} = \frac{2I_m}{\pi} = 0.6366\,I_m\;}$$

**Verified.** $2/\pi = 0.63661977$ ✓, and numerical integration of $\sin\theta$ over $[0,\pi]$
divided by $\pi$ returns 0.6366198. ✓ **Exactly twice the half-wave value** — the same charge is
delivered twice as often.

> ⚠ ILLEGIBLE ·J p49 — the **evaluation line of this average is clipped by the top page margin**.
> Only about 14 pixel rows survive, showing a $\pi$, a subscript 0, a second $\pi$, a third $\pi$
> and a short trailing group of digits. The surviving glyph positions match
> $\frac{I_m}{\pi}\left[-\cos\theta\right]_{0}^{\pi} = \frac{I_m}{\pi}\left[-\cos\pi + \cos 0\right] = \frac{2I_m}{\pi} = 0.6366\,I_m$,
> which is also the form the half-wave section prints in full on ·J p47, but **the line itself
> cannot be read**. The result $2I_m/\pi$ is confirmed independently: ·J p49 uses it in the
> efficiency numerator as $\left(2I_m/\pi\right)^{2}$ and again in the ripple denominator.
> Needs a screenshot of ·J p49 if the exact printed line matters.

[derivation ·J p49] **The rms value.** Same integrand, same $\pi$ period:

$$I_{rms}^{2} = \frac{1}{\pi}\int_{0}^{\pi} i^{2}\,d\theta = \frac{1}{\pi}\int_{0}^{\pi}\big(I_m\sin\theta\big)^{2} d\theta = \frac{I_m^{2}}{\pi}\int_{0}^{\pi}\frac{1-\cos 2\theta}{2}\,d\theta = \frac{I_m^{2}}{2}$$

[eq: fw-irms-j]

$$\boxed{\;I_{rms} = \frac{I_m}{\sqrt2} = 0.707\,I_m\;}$$

**Verified numerically.** rms of $\sin\theta$ over $[0,\pi]$ = 0.70710678 = $1/\sqrt2$ ✓.

*[added] The rms goes up by $\sqrt2$ while the average goes up by 2. That asymmetry is exactly why
the full-wave ripple factor (§5.11) falls so much further than the efficiency (§5.10) rises.*

[eq ·J p49] **The two powers**, as before:

$$P_{dc} = I_{dc}V_{dc} = I_{dc}^{2}R_L \qquad\qquad P_{ac} = I_{rms}^{2}R_L$$

and, with the diode resistance included,

$$P_{ac} = I_{rms}^{2}\left(R_L + r_f\right) = \left(\frac{I_m}{\sqrt2}\right)^{2}\left(R_L + r_f\right) = \frac{I_m^{2}}{2}\left(R_L + r_f\right)$$

> ⚠ VERIFY **JV5.2** ·J p49 — printed:
> $$P_{ac} = I_{rms}^{2}\left(R_L + r_f\right) = \left(\frac{I_m}{2}\right)^{2}\left(R_L + r_f\right)$$
> The substituted rms is $I_m/2$ — **the half-wave value**, carried over verbatim from ·J p47. Two
> lines above, the same page has just derived $I_{rms} = I_m/\sqrt2$ for this circuit. Substituting
> $I_m/2$ gives $P_{ac} = I_m^{2}(R_L+r_f)/4$, which would make
> $\eta = 8/\pi^{2}\times\tfrac{1}{2} = 4/\pi^{2} = 40.5\,\%$ — the half-wave answer, not the
> $81.1\,\%$ the next line states. Correct form:
> $$\boxed{\;P_{ac} = \left(\frac{I_m}{\sqrt2}\right)^{2}\left(R_L + r_f\right) = \frac{I_m^{2}}{2}\left(R_L + r_f\right)\;}$$
> See `_verification-log.md`.

---

## 5.10 Full-wave: rectification efficiency ·J p49

[derivation ·J p49]

$$\eta = \frac{P_{dc}}{P_{ac}} = \frac{I_{dc}^{2}R_L}{I_{rms}^{2}\left(R_L + r_f\right)} = \frac{\left(\dfrac{2I_m}{\pi}\right)^{2} R_L}{\left(\dfrac{I_m}{\sqrt2}\right)^{2}\left(R_L + r_f\right)}$$

$$\eta = \frac{4I_m^{2}/\pi^{2}}{I_m^{2}/2}\cdot\frac{R_L}{R_L+r_f} = \frac{8}{\pi^{2}}\cdot\frac{R_L}{R_L + r_f}$$

[eq: fw-efficiency-j]

$$\boxed{\;\eta_{\text{FW}} = \frac{8}{\pi^{2}\left(1 + \dfrac{r_f}{R_L}\right)} = \frac{0.811}{1 + \dfrac{r_f}{R_L}}\;}$$

**With $r_f \ll R_L$** ·J p49:

$$\boxed{\;\eta_{\text{FW,max}} = \frac{8}{\pi^{2}} = 0.811 = 81.1\,\%\;}$$

**Verified.** $8/\pi^{2} = 0.81056947$, i.e. **81.06 %**; the page's 81.1 % is the correct rounding
to three figures. ✓ It is **exactly twice** the half-wave figure — the single best sanity check on
this whole section.

·J p49 draws the conclusion in one line: *the full-wave rectifier thus has very high efficiency.*

> ⚠ VERIFY **JV5.3** ·J p49 — the same misplaced exponent as **JV5.1**. Printed:
> $$\eta = \frac{\left(\dfrac{2I_m}{\pi}\right)^{2} R_L}{\left(\dfrac{I_m}{\sqrt2}\right)\left(R_L + r_f\right)^{2}}$$
> The square belongs on $I_m/\sqrt2$, not on $(R_L + r_f)$. Dimensional check: the printed
> denominator is $\mathrm{A}\cdot\Omega^{2}$ against a numerator of $\mathrm{A}^{2}\Omega$.
> Algebraic check: only the corrected form collapses to the $8/\pi^{2}$ printed on the next line.
> Correct form:
> $$\boxed{\;\eta = \frac{\left(\dfrac{2I_m}{\pi}\right)^{2} R_L}{\left(\dfrac{I_m}{\sqrt2}\right)^{2}\left(R_L + r_f\right)}\;}$$
> See `_verification-log.md`.

---

## 5.11 Full-wave: ripple factor ·J p49

[derivation ·J p49] The same three-line identity as §5.7:

$$I_{rms}^{2} = I_{dc}^{2} + I_{ac}^{2} \qquad I_{rms} = \sqrt{I_{dc}^{2} + I_{ac}^{2}} \qquad I_{ac} = \sqrt{I_{rms}^{2} - I_{dc}^{2}}$$

$$\frac{I_{ac}}{I_{dc}} = \sqrt{\frac{I_{rms}^{2}}{I_{dc}^{2}} - 1} = \sqrt{\frac{\left(I_m/\sqrt2\right)^{2}}{\left(2I_m/\pi\right)^{2}} - 1} = \sqrt{\frac{\pi^{2}}{8} - 1}$$

[eq: fw-ripple-j]

$$\boxed{\;\gamma_{\text{FW}} = \sqrt{\frac{\pi^{2}}{8} - 1} = 0.48\;}$$

**Verified.** $\left(I_m/\sqrt2\right)^{2} / \left(2I_m/\pi\right)^{2} = \frac{I_m^{2}/2}{4I_m^{2}/\pi^{2}} = \frac{\pi^{2}}{8}$ ✓.
$\pi^{2}/8 = 1.2337006$; $\sqrt{0.2337006} = 0.4834258$. The page's 0.48 is right to two figures;
**quote 0.483 if three are wanted.** ✓

*[added] Compare the two circuits directly: ripple falls from **1.21** to **0.48**, a factor of
2.5, while efficiency doubles. Those two numbers together are the entire case for full-wave
rectification, and they are the two most likely single-mark questions in this range.*

·J p52 states the comparison in its own words: **ripple factor HWR > FWR**. ✓ Correct as printed —
$1.21 > 0.48$.

---

## 5.12 The bridge rectifier ·J p50

> ⚠ VERIFY **JC5.6** ·J p50 — **the bridge-rectifier section has no heading.** The centre-tapped
> circuit on ·J p48 is properly headed *"(a) Centre-Tapped Rectifier"*, so a matching
> *"(b) Bridge Rectifier"* is expected here and is simply absent: ·J p50 opens with the circuit
> figure at normal body position, and the blank space at the foot of ·J p49 shows nothing was
> pushed over the page break. Unlike ·J p46, this is not a lost-blank-space case — the heading was
> never typed. Nothing computed changes. See `_verification-log.md`.

[fig ·J p50] **Bridge-rectifier circuit.** Transformer at the left, **Input** at the far-left
terminals; **no centre tap**. Polarity marks $+\,-$ at the top of the secondary and $-\,+$ at the
bottom. From the two secondary ends, two wires run right into a **diamond of four diodes** drawn
rotated 45°, labelled around the diamond as **$D_1$** (upper left), **$D_2$** (upper right),
**$D_3$** (lower left), **$D_4$** (lower right). **$R_L$** sits horizontally **across the
diamond's other diagonal**, labelled **Output**, with arrowheads on both connecting wires showing
that current enters $R_L$ from the same side on both half cycles.

[fig ·J p50] **Waveforms, two graphs stacked.**

- **Upper — input.** $I$ (current) against **time**: three full sinusoids.
- **Lower — output.** A continuous train of positive humps, no gaps, ticked $\pi$ to $5\pi$. Each
  hump carries the **conducting pair**: **D2D3, D1D4, D2D3, D1D4, D2D3**.

**Operation** ·J p50

- **First half cycle** — $D_2$ and $D_3$ are forward biased; $D_1$ and $D_4$ are reverse biased.
  Output appears at $R_L$ from $D_2$ and $D_3$.
- **Second half cycle** — $D_1$ and $D_4$ are forward biased; $D_2$ and $D_3$ are reverse biased.
  Output appears at $R_L$ from $D_1$ and $D_4$.

The currents flow through $R_L$ **in the same direction** on both half cycles, so they appear on
the positive side of the time line, as ripples at **twice** the input frequency.

**The three circuits at a glance** [added]

| | Diodes | Transformer | Ripple frequency | $\eta_{\max}$ | $\gamma$ |
|---|---|---|---|---|---|
| Half-wave | 1 | plain | $f$ | 40.5 % | 1.21 |
| Centre-tap full-wave | 2 | **centre-tapped** | $2f$ | 81.1 % | 0.48 |
| Bridge full-wave | 4 | plain | $2f$ | 81.1 % | 0.48 |

*The bridge buys you the full-wave figures without a centre-tapped transformer, at the cost of two
extra diodes and one extra forward drop in the conduction path — **two diodes are in series at
every instant**. ·J never mentions that extra drop, nor the peak inverse voltage of any of the
three circuits; both are in `12-rectifiers.md` §2.8.*

---

## 5.13 [exercise] The unsolved rectifier problem ·J p50

**Statement, as printed** ·J p50:

> A half-wave rectifier with transformer of transformation ratio of 10:1 has the following
> parameters.
> $V_{in} = 250\sin\omega t$ V, $r_f = 20\ \Omega$, $R_L = 800\ \Omega$.
> **Calculate** $V_m$, $I_{dc}$, $I_{ac}$, $P_{dc}$, $\eta$, $V_{dc}$, ripple factor.

**No solution is given.** The page moves straight on to the smoothing section.

> **Note on the count.** The list asks for **seven** quantities, not six: $V_m$, $I_{dc}$,
> $I_{ac}$, $P_{dc}$, $\eta$, $V_{dc}$ and the ripple factor. All seven are worked below.

### [added] Full solution — every step verified with python3

*This solution is **not** in the notes.*

**Reading the transformer.** A transformation ratio of $10\!:\!1$ is a **step-down**: the secondary
carries one tenth of the primary voltage. $V_{in} = 250\sin\omega t$ is the **primary** waveform,
so its peak is 250 V and the secondary peak is

$$V_m = \frac{250}{10} = \boxed{25\ \mathrm{V}}$$

*(If instead you read $V_{in}$ as already being the secondary voltage, every current below scales
by 10 and $P_{dc}$ by 100. The step-down reading is the one that makes the given $r_f$ and $R_L$
produce sensible milliamp currents, and it is the standard convention.)*

**Step 1 — peak load current.** The diode's forward resistance is in series with the load:

$$I_m = \frac{V_m}{R_L + r_f} = \frac{25}{800 + 20} = \frac{25}{820} = 0.030488\ \mathrm{A} = 30.49\ \mathrm{mA}$$

**Step 2 — dc current**, from [eq: hw-idc-j]:

$$I_{dc} = \frac{I_m}{\pi} = \frac{0.030488}{3.14159} = \boxed{9.70\ \mathrm{mA}}$$

**Step 3 — rms current**, from [eq: hw-irms-j]:

$$I_{rms} = \frac{I_m}{2} = \frac{0.030488}{2} = 15.24\ \mathrm{mA}$$

**Step 4 — ac (ripple) current**, from [eq: irms-dc-ac-j]:

$$I_{ac} = \sqrt{I_{rms}^{2} - I_{dc}^{2}} = \sqrt{15.244^{2} - 9.705^{2}}\ \mathrm{mA} = \sqrt{232.4 - 94.2}\ \mathrm{mA}$$

$$I_{ac} = \boxed{11.76\ \mathrm{mA}}$$

*Cross-check by the other route: $I_{ac} = \gamma_{\text{HW}}\,I_{dc} = 1.21136 \times 9.7046 = 11.756$ mA ✓ — the two agree to five figures.*

**Step 5 — dc power in the load**, from [eq: rectifier-powers-j]:

$$P_{dc} = I_{dc}^{2}R_L = \left(9.7046\times10^{-3}\right)^{2}\times 800 = \boxed{75.3\ \mathrm{mW}}$$

**Step 6 — efficiency**, from [eq: hw-efficiency-j]:

$$\eta = \frac{4}{\pi^{2}\left(1 + r_f/R_L\right)} = \frac{0.40528}{1 + 20/800} = \frac{0.40528}{1.025} = 0.3954$$

$$\eta = \boxed{39.5\,\%}$$

*Cross-check from the powers directly: $P_{ac} = I_{rms}^{2}(R_L + r_f) = (15.244\ \mathrm{mA})^{2}\times 820 = 190.5$ mW, and $75.34/190.55 = 0.3954$ ✓.*

**Step 7 — dc load voltage.** The notes define $P_{dc} = I_{dc}V_{dc} = I_{dc}^{2}R_L$, so
$V_{dc} = I_{dc}R_L$:

$$V_{dc} = I_{dc}R_L = 9.7046\times10^{-3}\times 800 = \boxed{7.76\ \mathrm{V}}$$

*If the diode resistance is neglected the shortcut $V_{dc} = V_m/\pi = 25/\pi = 7.96$ V is used
instead; the 2.4 % difference is exactly the $r_f$ drop. Quote 7.76 V, since the question supplies
$r_f$.*

**Step 8 — ripple factor**, from [eq: hw-ripple-j]:

$$\gamma = \frac{I_{ac}}{I_{dc}} = \frac{11.756}{9.7046} = \boxed{1.21}$$

*It has to be: the ripple factor of a half-wave rectifier is $\sqrt{\pi^{2}/4 - 1}$ whatever the
component values. If your answer is not 1.21, an earlier step is wrong.*

[table] **[added] Answer summary — all seven**

| Quantity | Value |
|---|---|
| $V_m$ (secondary peak) | **25 V** |
| $I_m$ (peak, working value) | 30.49 mA |
| $I_{dc}$ | **9.70 mA** |
| $I_{rms}$ (working value) | 15.24 mA |
| $I_{ac}$ | **11.76 mA** |
| $P_{dc}$ | **75.3 mW** |
| $\eta$ | **39.5 %** |
| $V_{dc}$ | **7.76 V** |
| ripple factor $\gamma$ | **1.21** |

*[added] Two extras the question does not ask for but a fuller version might:
$\mathrm{PIV} = V_m = 25$ V, and the ripple frequency equals the supply frequency.*

---

## 5.14 Smoothing circuits (filters) ·J p50

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $C$ | smoothing capacitance | F | tens to thousands of µF |
| $L$ | choke (filter) inductance | H | a few H |
| $V_C$ | instantaneous capacitor voltage | V | — |
| $V_S$ | the voltage the capacitor is charging towards | V | — |
| $t$ | time from the start of the interval | s | — |
| $RC$ | time constant of the charge or discharge path | s | — |
| $R_L$ | load resistance | Ω | — |

[def ·J p50] A **smoothing circuit (filter)** is the section of the power supply that **removes the
ac component present in the output of a rectifier**. It is built from capacitors and inductors, or
a combination of both.

Three kinds are named ·J p50:

- **(a) Capacitor filter** — §5.15
- **(b) Choke input (inductor)** — §5.16
- **(c) Capacitor input filter** — §5.17

---

## 5.15 (a) The capacitor filter ·J p51

[fig ·J p51] **Circuit.** Two input terminals on the left labelled **Input**; a **capacitor** drawn
as two parallel plates sits vertically across the line; to its right a **$R_L$** box, also across
the line; two output terminals on the right labelled **output**. That is all of it: **a capacitor
and a resistor in parallel.**

> ⚠ VERIFY **JC5.7** ·J p51 — **the figure comes before its heading.** The page order is: capacitor
> circuit, then the heading *"Half-wave rectifier"*, then the waveforms, then the heading
> *"Capacitor filter"* with the charge and discharge equations. So the circuit that the "Capacitor
> filter" heading names appears **two headings earlier**, and the "Half-wave rectifier" heading
> sits between a circuit and the waveforms it belongs to. Layout only; nothing computed changes.
> The same page also charges the capacitor towards **$V_S$** in the equation while the prose
> beneath says it charges to a maximum **$V_m$** — two symbols for one quantity.
> See `_verification-log.md`.

[fig ·J p51] **Half-wave waveforms with the filter fitted, two graphs stacked.**

- **Upper.** $I$ (current) against **time**, origin 0, ticked $\pi$ to $5\pi$: the **unfiltered**
  half-wave train — humps with flat gaps between them.
- **Lower.** The **filtered** output. A short steep rise, then a **long slow decay**, then another
  short steep rise picking up from wherever the decay had reached, and so on. Beneath the trace the
  time axis is divided by **× marks** into alternating intervals labelled **a** (short) and **b**
  (long), repeating: a, b, a, b. The trace never returns to zero.

[def ·J p51] The two intervals:

- **a — Charging**

[eq: capacitor-charge-j]

$$\boxed{\;V_C = V_S\left(1 - e^{-t/RC}\right)\;}$$

- **b — Discharging**

[eq: capacitor-discharge-j]

$$\boxed{\;V_C = V_S\,e^{-t/RC}\;}$$

**Operation, in the notes' own sequence** ·J p51:

1. The circuit is a capacitor and a resistor in parallel.
2. When the **first ripple** arrives, the capacitor charges to a maximum $V_m$.
3. The ripple then **collapses very fast**, leaving the capacitor to discharge.
4. Because the capacitor **takes a longer time to discharge**, the **second ripple** finds it still
   discharging and **picks up from there**, charging it again to $V_m$.
5. The process continues for as long as there is an input to the filter.

The result is an output with **more dc component than the input waveform** had. ·J p51

[fig ·J p51] **Full-wave waveforms with the filter fitted, two graphs stacked.**

- **Upper — input.** A continuous train of humps, no gaps, ticked $\pi$ to $5\pi$.
- **Lower — output.** The same charge–decay sawtooth, but with the **decay intervals visibly
  shorter** and the trace correspondingly flatter. The a / b marks appear again, closer together.

·J p51: *the operation is the same as that of a half-wave rectifier, the only difference being that
the output of the full-wave rectifier filter has **more dc component** than the half-wave one.*

> ⚠ VERIFY **JV5.5** ·J p51 — **the two exponentials are printed with the same time constant $RC$,
> and they cannot be.** The page's own argument in the paragraph beneath turns on the capacitor
> "taking a longer time to discharge" than to charge — which is only true if the two paths have
> different resistances, and they do:
> - **charging** is through the conducting **diode and transformer**, resistance $r_f$ (tens of ohms);
> - **discharging** is through the **load**, resistance $R_L$ (hundreds of ohms or more).
>
> Correct forms:
> $$\boxed{\;V_C = V_S\left(1 - e^{-t/r_f C}\right)\ \text{(charging)}\qquad V_C = V_S\,e^{-t/R_L C}\ \text{(discharging)}\;}$$
> With the values of §5.13, $r_f C = 20C$ against $R_L C = 800C$ — a factor of **40** between the two
> intervals, which is precisely why the drawn waveform has a short **a** and a long **b**. Written
> with one $RC$ the equations describe a symmetric wave that the same page then draws asymmetrically.
> See `_verification-log.md`.

*[added] **What the filter actually buys you, in one line.** Between peaks the capacitor supplies
the load on its own, so the output falls by $\Delta V \approx I_{dc}\,T_d/C$ over the discharge
interval $T_d$. Halving $T_d$ — which is exactly what going from half-wave to full-wave does —
halves the ripple for the same capacitor. That is the quantitative version of the sentence ·J p51
states qualitatively. The design formulas ($V_{r(pp)} = I_{dc}/f_r C$ and
$C = 1/2\sqrt3\,\gamma f_r R_L$) are in `12-rectifiers.md` §2.12, where they are also `[added]` —
neither source states them.*

---

## 5.16 (b) The choke-input filter ·J p52

[fig ·J p52] **Circuit.** Input terminals at the left, the upper marked **+** and the lower **−**,
labelled **Input**. An **inductor $L$** sits **in series** in the top rail. Beyond it, a
**capacitor $C$** hangs from the top rail to the bottom rail; to its right an **$R_L$** box also
spans top rail to bottom rail. Output terminals at the far right, labelled **output**. So: **an
inductor in series with a parallel combination of a capacitor and a resistor** — an L-section, with
the inductor first.

[fig ·J p52] **Waveforms, two graphs stacked.**

- **Upper — input.** $I$ (current) against **time**, origin 0, ticked $\pi$ to $5\pi$: a continuous
  train of full-wave humps.
- **Lower — output.** A **nearly flat line carrying a small residual wobble** — visibly much
  smoother than the capacitor filter's sawtooth of §5.15, with no steep charging edges at all.

**Operation** ·J p52, in four steps:

1. The **inductor opposes** some of the ac component present in the input.
2. Whatever ac still gets through the inductor is **bypassed by the capacitor $C$**.
3. There is therefore a **minimised ac** at the output.
4. The **dc passes through the inductor without opposition** and goes straight to the output, since
   it cannot pass through the capacitor.

*[added] The division of labour is a frequency argument. The inductor's reactance $X_L = 2\pi fL$
is zero at dc and large at the ripple frequency, so it blocks ripple and passes dc. The capacitor's
reactance $X_C = 1/2\pi fC$ is infinite at dc and small at the ripple frequency, so it shorts
ripple to the return rail and does nothing to the dc. The two are the same filter viewed from
opposite ends.*

---

## 5.17 (c) The capacitor-input (Π) filter ·J p52–p53

[fig ·J p52] **Circuit — "Capacitor input filter (Π filter)".** Input terminals at the left, upper
**+**, lower **−**, labelled **Input**. Then, left to right along the top rail:

- **$C_1$** from top rail to bottom rail, immediately at the input;
- **$L$** in series in the top rail;
- **$C_2$** from top rail to bottom rail, after the inductor;
- **$R_L$** from top rail to bottom rail;
- output terminals at the far right, labelled **output**.

**C–L–C**: two shunt capacitors with a series choke between them. Drawn on the page the three
components make the shape of the letter Π, which is where the name comes from. [added]

[fig ·J p53] **Waveforms, two graphs stacked** (this figure runs over the page break onto ·J p53).

- **Upper — input.** $I$ (current) against **time**, origin 0, ticked $\pi$ to $5\pi$: a continuous
  train of full-wave humps.
- **Lower — output.** An almost **straight horizontal line** with only a faint ripple on it —
  visibly flatter than the choke-input output of §5.16.

**Operation** ·J p53, in four steps:

1. The first capacitor **$C_1$ bypasses** the ac component present at the input.
2. Whatever is left is **blocked by the inductor $L$**.
3. Whatever passes through the inductor is **bypassed by $C_2$**.
4. The **dc component passes through the inductor to the output**.

The result is a **more refined dc component**, and ·J p53 adds that **several such sections in
combination produce a still more refined dc**.

*[added] **Order of merit, from these three sections:** capacitor filter (cheapest, biggest ripple,
highest output voltage) → choke-input (flattest current, best regulation, lowest output voltage) →
Π filter (best ripple rejection, needs both parts). The notes state the ranking only by drawing
progressively flatter output traces; the ranking is the examinable point.*

---

## 5.18 Stabilising circuit / voltage regulator ·J p53

[def ·J p53] The **stabilising circuit** — the fourth block of §5.1 — is **constructed using a
zener diode, or a transistor, or both**.

*[added] ·J names the transistor regulator here and never returns to it. Everything from this point
to the end of the range is the **zener** version.*

[fig ·J p53] **Zener diode circuit symbol.** Drawn horizontally in a plain wire. A **triangle
pointing right** (the anode), its apex meeting a **vertical cathode bar**. The bar's **top end is
bent forward to the upper right and its bottom end back to the lower left**, so that the cathode
reads as a letter **Z**. Anode on the left, cathode on the right.

[def ·J p53] A **zener diode uses the principle of reverse breakdown to provide a constant output
voltage.**

### Construction ·J p53

> ⚠ REDACTED ·J p53 — **the opening sentence of the Construction sub-section is covered by an
> opaque yellow block** (552 px, roughly 45–50 characters). The text under it is destroyed; there
> is nothing to recover. The paragraph resumes:
>
> *"… This will make it to breakdown without getting damaged. It breaks down earlier than the other
> diodes depending on the reverse voltage rating. It has a higher power rating."*

*[added] **What the covered sentence must have said, and what it cannot be assumed to have said.**
The three surviving sentences require the missing one to describe **how the junction is built so
that it breaks down at a low, well-defined reverse voltage without destroying itself** — in
standard terms, that **both sides of the junction are heavily doped**, which narrows the depletion
layer and lowers the breakdown voltage. That is the physics the paragraph needs and it is what
every textbook treatment says. **The lecturer's actual wording is gone and is not reconstructed
here.** A screenshot of ·J p53 would settle it.*

### Operation ·J p53

> ⚠ REDACTED ·J p53 — **the opening sentence of the Operation sub-section is covered by a second
> opaque yellow block** (384 px, roughly 30–35 characters). The paragraph resumes:
>
> *"… If the voltage is increased beyond breakdown voltage the diode breaks down. Any further
> increment of voltage will still give a constant output voltage as shown in the diagram below."*

*[added] **What the covered sentence must have said.** The sentence that follows begins "If the
voltage is increased beyond breakdown voltage", so the missing one must establish the **bias
condition** — that the zener is **connected in reverse bias**. The block is about the right length
for a sentence of that form. Again, **the exact wording is destroyed** and is not reconstructed
here.*

*[added] Both inferences are about the **subject** of the missing sentences, which the surrounding
text fixes beyond reasonable doubt. Neither is a reconstruction of the lecturer's words, and
neither should be quoted as the notes' text.*

---

## 5.19 The zener V–I characteristic ·J p54

### Symbols

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_Z$ | zener (breakdown) voltage | V | 15 V (§5.22) |
| $I_Z$ | zener current | A | 31 mA |
| $P_Z$ | power dissipated in the zener, $P_Z = I_ZV_Z$ | W | 0.47 W |
| $V_S$ | unregulated supply voltage | V | 40 V |
| $R$ | series (dropping) resistor | Ω | 500 Ω |
| $R_L$ | load resistance | Ω | 800 Ω |
| $I_t$ | **total** current through $R$ | A | 50 mA |
| $I_{RL}$ | load current | A | 18.75 mA |
| $V_{RL}$ | voltage across the load | V | 15 V (on state) |
| $V_f$, $V_R$ | forward and reverse axis voltages | V | — |
| $I_f$, $I_R$ | forward and reverse axis currents | A | — |

> **Notation clash — the subscript $t$.** $I_t$ here means **total**, not "at time $t$". It is the
> current in the series resistor, and it splits into $I_Z$ and $I_{RL}$. [added]

> **Notation clash — $R$ and $V_S$.** In §5.15 $R$ was a filter time-constant resistance and $V_S$
> the voltage a capacitor charges towards; from here on $R$ is the zener **dropping resistor** and
> $V_S$ the **supply**. Same letters, one page apart. [added]

[fig ·J p54] **Zener static characteristic, all four quadrants on one pair of axes.**

- Vertical axis upward labelled $I_f$ (clipped at the very top of the page); vertical axis downward
  labelled $I_R$. Horizontal axis right labelled $V_f$; horizontal axis left labelled $V_R$.
- **First quadrant (forward):** the curve leaves the origin, hugs the $V_f$ axis for a short
  distance and then **rises steeply** — an ordinary diode forward characteristic.
- **Second/third quadrant (reverse):** from the origin the curve runs **flat and just below the
  horizontal axis** leftward, a tiny current labelled **Leakage current** with an arrow pointing at
  it, then, at a definite negative voltage, it **turns and drops almost vertically**.
- The knee of that vertical drop is arrowed and labelled **Zener Breakdown Voltage**.

[def ·J p54] Reading the curve:

- **In forward bias** the zener behaves like any other diode and conducts at **0.7 V (Si)** or
  **0.3 V (Ge)**.
- **In reverse bias** the diode **breaks down** once the voltage rises past the breakdown voltage.
- Below breakdown only a small **leakage current** flows.

[def ·J p54] The zener is **connected together with an external resistor to limit the amount of
current**, related to the diode's rating.

*[added] That external resistor is $R$ in every circuit from here on. Without it the near-vertical
breakdown characteristic means an arbitrarily small increase in supply voltage produces an
arbitrarily large current, and the diode dissipates itself. $R$ is what converts a vertical curve
into a usable operating point.*

> ⚠ VERIFY **JC5.5** ·J p49, ·J p54 — **two items are printed in red ink** while everything around
> them is black: the heading *"Rms value of a.c output current"* on ·J p49 (the identical heading
> on ·J p47 is black), and the parenthesis *"(Si – 0.7V, Ge- 0.3V)"* on ·J p54. Colour carries no
> meaning anywhere else in the document and both items are ordinary content. A reader working from
> a monochrome print sees no difference; a reader working from the colour PDF should not read
> emphasis into it. Nothing computed changes. See `_verification-log.md`.

---

## 5.20 Equivalent circuits of the zener diode ·J p54

[fig ·J p54] **Three panels side by side, each a two-terminal box with a $+$ terminal top left and
a $-$ terminal bottom left, and the device in the right-hand leg.**

- **Panel 1 — the device.** The right leg carries the **zener symbol**, drawn vertically with the
  **cathode bar (with its two bent ends) uppermost** and the triangle pointing down to it, labelled
  **Z**. Cathode to the $+$ rail: the diode is **reverse connected**.
- **Panel 2 — the on state.** The right leg carries a **battery** (long and short bars, positive
  plate uppermost). An arrow along the top rail is labelled **$I_z$**. The left of the panel is
  labelled **V**.
- **Panel 3 — the off state.** The right leg is **broken**: two small open circles with a gap
  between them — an open circuit. Labelled **$I_z = 0$**. The left of the panel is labelled **V**.

[def ·J p54] The rule, in the notes' own words:

- **In the on state** the zener diode is replaced by the **zener voltage** (breakdown voltage).
- **In the off state** it is replaced by an **open circuit**, assuming the leakage current
  $I_z = 0$.

> ⚠ VERIFY **JC5.9** ·J p54 — in **panel 2** the battery that replaces the diode **carries no
> label**. The reader must take the value from the sentence below the figure. The neighbouring
> panels both label their device ($Z$, and $I_z = 0$), and the same battery **is** labelled $V_Z$
> when the circuit is redrawn on ·J p55. Add "$V_Z$" beside the battery. Nothing computed changes.
> See `_verification-log.md`.

*[added] These two replacements are the whole analysis method. There is no third case and no
in-between: you decide which state the diode is in, swap in the corresponding element, and solve
the resulting **resistive** circuit. §5.21 gives the test that decides.*

---

## 5.21 Zener circuit analysis — the two states ·J p54–p55

[fig ·J p54] **The circuit — "Zener Diode circuits Analysis".** Source terminals on the left, upper
**+**, lower **−**, labelled **$V_s$**. A resistor **$R$** in the top rail, with an arrowhead just
after it labelled **$I_t$**. From the node beyond $R$, two shunt branches drop to the bottom rail:

- the **zener**, cathode uppermost, labelled **$V_Z$** on its left and **$Z$** on its right, with a
  downward arrow labelled **$I_z$**;
- the **load $R_L$**, drawn as a zigzag resistor, with a downward arrow labelled **$I_{RL}$**.

Output terminals at the far right, across $R_L$, labelled **output**.

### The off state ·J p55

[fig ·J p55] The same circuit with the **zener branch replaced by an open gap** — two small circles
with the voltage across them labelled **V**. $R$, $I_t$, $V_s$ and $R_L$ are unchanged.

With no current in the zener branch, $R$ and $R_L$ form a plain potential divider:

[eq: zener-off-divider-j]

$$\boxed{\;V_{RL} = \frac{V_S R_L}{R + R_L}\;}$$

and to its right the page prints the test that ends the off state:

$$\boxed{\;V > V_Z \;\Longrightarrow\; \text{on state}\;}$$

*[added] Read those two lines as **one procedure**, because that is how every zener question is
worked:*

1. *Remove the zener and compute the divider voltage $V_{RL}$.*
2. *If $V_{RL} \le V_Z$, the diode never breaks down: it stays open, $I_Z = 0$, and the divider
   answer stands.*
3. *If $V_{RL} > V_Z$, the diode conducts, clamps the node to $V_Z$, and you switch to the on-state
   equations below.*

> ⚠ VERIFY **JC5.8** ·J p55 — **the off-state circuit has no heading.** The page opens with it, and
> the matching heading **On state** appears only above the *second* circuit. The reader has to
> deduce from the open gap in the figure which state the first block describes. ·J p54 ends with
> blank space, so nothing was lost at the page break. Nothing computed changes.
> See `_verification-log.md`.

### The on state ·J p55

[fig ·J p55] The same circuit with the **zener replaced by a battery labelled $V_Z$**, positive
plate uppermost. $R$ carries $I_t$; $R_L$ hangs beside the battery.

The node is now clamped at $V_Z$, so:

[eq: zener-on-currents-j]

$$\boxed{\;I_{RL} = \frac{V_Z}{R_L}\;}\qquad\qquad\boxed{\;I_t = \frac{V_S - V_Z}{R} = I_{RL} + I_Z\;}$$

and therefore

$$\boxed{\;I_Z = I_t - I_{RL}\;}$$

[eq: zener-power-j] The power the diode must dissipate:

$$\boxed{\;P_Z = I_Z V_Z\;}$$

*[added] Note what the three equations say physically. The load current is fixed by $V_Z$ alone —
that is the regulation. The total current is fixed by $V_S$ and $R$ alone. **The zener absorbs the
difference**, and that is its entire job: it is a current sink of exactly the size needed to keep
the node at $V_Z$. If $V_S$ rises, $I_t$ rises and the extra all goes into $I_Z$; if the load
draws more, $I_Z$ falls by the same amount. Check $P_Z$ against the diode's rating every time.*

---

## 5.22 [ex] The 40 V supply with a 15 V zener ·J p55

> ⚠ REDACTED ·J p55 — a **small opaque yellow block** (105 px, about 8–9 characters) sits alone on
> the line immediately above the data block, in exactly the position and at the size the word
> **Example** occupies elsewhere in these notes (compare ·J p40 and ·J p50). It is a label, not
> content: nothing in the worked solution depends on it.

**Given** ·J p55:

$$R = 500\ \Omega \qquad R_L = 800\ \Omega \qquad V_s = 40\ \mathrm{V} \qquad V_Z = 15\ \mathrm{V}$$

**Required** ·J p55: $I_{RL}$, $I_t$, $I_Z$ and $P_Z$ **in the on state**, and $I_t$ **in the off
state**.

### Solution, as the notes give it ·J p55

**On state**

$$I_{RL} = \frac{V_Z}{R_L} = \frac{15}{800} = 0.01875\ \mathrm{A}$$

$$I_t = \frac{V_S - V_Z}{R} = \frac{40 - 15}{500} = \frac{25}{500} = 0.05\ \mathrm{A}$$

$$I_Z = I_t - I_{RL} = 0.05 - 0.01875 = 0.03125\ \mathrm{A}$$

$$P_Z = I_ZV_Z = 0.03125 \times 15 = 0.46875\ \mathrm{W}$$

**Off state**

$$I_t = \frac{V_S}{R + R_L} = \frac{40}{500 + 800} = \frac{40}{1300} = 0.031\ \mathrm{A}$$

**Closing remark** ·J p55: $I_t$ **differs between the two states**. In the on state the diode
bypasses most of the current, shorting out the resistor $R_L$.

### [added] Every number checked

| Quantity | Notes' value | Recomputed | ✓ |
|---|---|---|---|
| $I_{RL} = 15/800$ | 0.01875 A | 0.01875 A = **18.75 mA** | ✓ |
| $I_t = 25/500$ | 0.05 A | 0.05 A = **50 mA** | ✓ |
| $I_Z = 0.05 - 0.01875$ | 0.03125 A | 0.03125 A = **31.25 mA** | ✓ |
| $P_Z = 0.03125\times15$ | 0.46875 | 0.46875 **W** = 469 mW | ✓ value, ✗ unit — see **JC5.4** |
| $I_t$ off $= 40/1300$ | 0.031 A | 0.030769 A = **30.8 mA** | ✓ answer; ✗ printed fraction — see **JV5.4** |

**Power balance check** [added] — a check worth doing on every regulator question:

$$P_R = I_t^{2}R = 0.05^{2}\times500 = 1.25\ \mathrm{W}$$

$$P_{RL} = I_{RL}^{2}R_L = 0.01875^{2}\times800 = 0.28125\ \mathrm{W}$$

$$P_R + P_Z + P_{RL} = 1.25 + 0.46875 + 0.28125 = 2.00\ \mathrm{W} = V_SI_t = 40\times0.05 \quad\checkmark$$

**[added] Two things the notes do not say about this example.**

1. **The off-state answer is hypothetical for these numbers.** Run the §5.21 test on them:
   $$V_{RL} = \frac{V_SR_L}{R+R_L} = \frac{40\times800}{1300} = 24.6\ \mathrm{V} > V_Z = 15\ \mathrm{V}$$
   so with this supply and this load **the zener is on**, and 30.8 mA is not a current that ever
   flows here. It is the answer to "what would $I_t$ be if the diode were not conducting" — useful
   as drill, and useful as the number to compare against, but not an operating condition of this
   circuit. Quote it with that caveat.
2. **"Shorting out $R_L$" is loose.** The zener does not short the load — the load still carries
   18.75 mA at 15 V. What it does is **clamp the node**, so the load's share of the current stops
   depending on $V_S$. The extra current the higher node current implies is taken by the diode
   (31.25 mA), not by $R_L$.

> ⚠ VERIFY **JV5.4** ·J p55 — the off-state line prints
> $$I_t = \frac{V_S}{R+R_L} = \frac{40}{500+800} = \frac{400}{1300} = 0.031\ \mathrm{A}$$
> The third fraction has **an extra zero in the numerator**. $40/1300 = 0.03077$, which is the
> 0.031 A stated; $400/1300 = 0.3077$, ten times larger. A learner copying the printed fraction
> gets 0.31 A and a tenfold error in everything downstream. Correct form:
> $$\boxed{\;I_t = \frac{40}{1300} = 0.0308\ \mathrm{A} \approx 31\ \mathrm{mA}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **JC5.4** ·J p55 — printed: *"$P_Z = I_ZV_Z = 0.03125 \times 15 = 0.46875\ A$"*. The
> answer is a **power** and its unit is the **watt**: 0.46875 W, or 469 mW. The number itself is
> correct. Correct form:
> $$\boxed{\;P_Z = 0.46875\ \mathrm{W}\;}$$
> Worth noticing because $P_Z$ is the quantity compared against the diode's wattage rating, and
> "0.46875 A" invites the wrong comparison. See `_verification-log.md`.

---

## 5.23 Zener voltage clipping — one side ·J p56

[fig ·J p56] **Circuit (its top rail is clipped by the page margin — see the note below).** An
**ac source**, drawn as a sine symbol, on the left. A resistor **$R$** in series in the top rail,
with an arrowhead after it. From the node beyond $R$, a shunt branch drops to the bottom rail
carrying a **battery symbol labelled $25\,\mathrm{V}$ and $V_Z$**, positive plate uppermost. To its
right, **$R_L$** drawn as a zigzag resistor, also from top rail to bottom rail. Caption beneath:
**Voltage Clipping one side**.

[fig ·J p56] **Waveforms, two graphs stacked.**

- **Upper — input.** Vertical axis $V$, ticked **50 V** and labelled **input**; horizontal axis
  **time**. Three full sinusoids of peak 50 V.
- **Lower — output.** Vertical axis ticked **25 V** and labelled **output**; time axis ticked
  $\pi$, $2\pi$, $3\pi$, $4\pi$, $5\pi$. The **positive half cycles are flat-topped at 25 V**, with
  steep sides. The **negative half cycles are drawn as full rounded half-sines** dipping to roughly
  −25 V — that is, unclipped and simply scaled down.

> ⚠ ILLEGIBLE ·J p56 — the **top rail of this circuit is cut off by the page margin**: only the
> lower half of the resistor zigzag, part of the current arrowhead and the top of the source symbol
> survive. The upper input terminal and any label on it are gone. What the branch elements are is
> unambiguous; how the source connects to the top rail is inferred from the other three circuits on
> the same page, which are all drawn the same way.

> ⚠ VERIFY **JV5.7** ·J p56 — **the shunt element is drawn as a battery, and the output waveform
> does not follow from any single two-terminal element in that position.** Two separate problems:
>
> 1. **The symbol.** A plain 25 V **battery** across the load would hold the output at exactly
>    +25 V for the **whole** cycle — a flat dc line, not the drawn waveform. What the caption and
>    the waveform describe is a **zener diode**, cathode to the top rail. The battery is the diode's
>    *on-state equivalent* from ·J p54, substituted into the circuit diagram itself.
> 2. **The negative half cycle.** With a real single zener, cathode to the top rail, the negative
>    half-cycle **forward biases** it. It then conducts heavily and clamps the output at about
>    **−0.7 V**, so the lower graph should show a nearly flat line just below the axis — not the
>    full −25 V half-sine drawn. The drawn waveform is what a **zener in series with an ordinary
>    diode** would give, or what you get by (incorrectly) applying the "off state = open circuit"
>    model of ·J p54 to a reverse-polarity input.
>
> Correct behaviour of the circuit the caption names:
> $$\boxed{\;v_{out} = \begin{cases} +V_Z \approx +25\ \mathrm{V}, & v_{in}\ \text{large and positive}\\ v_{in}\dfrac{R_L}{R+R_L}, & \text{between the limits}\\ -V_F \approx -0.7\ \mathrm{V}, & v_{in}\ \text{negative}\end{cases}\;}$$
> See `_verification-log.md`.

*[added] The reason the notes' two-state model breaks here is worth stating plainly: **"off" means
reverse-biased below breakdown, not "open in both directions".** A zener has three regimes, not
two — forward conduction, reverse blocking, reverse breakdown — and an ac input visits all three.
The dc regulator of §5.21 never leaves the last two, which is why the same model works perfectly
there.*

---

## 5.24 Zener voltage clipping — both sides ·J p56

[fig ·J p56] **Two circuits drawn one above the other, sharing the caption "Voltage Clipping both
sides" printed below the pair.** Both have the same skeleton: input terminals at the left, upper
**+**, lower **−**; a resistor **$R$** in series in the top rail with an arrowhead after it; then a
shunt branch of **two 25 V zeners in series** dropping to the bottom rail; then **$R_L$** as a
vertical box from top rail to bottom rail; then output terminals at the far right labelled
**output**.

They differ **only** in how the second zener is turned:

- **Upper circuit.** The **top** zener has its cathode bar uppermost (triangle apex up); the
  **bottom** zener has its cathode bar lowermost (triangle apex down). The two **anodes meet in the
  middle** — the correct back-to-back arrangement.
- **Lower circuit.** **Both** zeners are drawn the same way up, cathode bar uppermost. The upper
  diode's **anode** meets the lower diode's **cathode** — the two are in series *aiding*, both
  pointing the same way.

[fig ·J p56] **Waveforms, two graphs stacked, beneath the caption.**

- **Upper — input.** Three full sinusoids about the time axis, with a peak tick on the vertical
  axis (unlabelled).
- **Lower — output.** A **symmetrically clipped, near-square wave**: flat tops at the positive tick
  level and flat bottoms at the same distance below the axis, with steep transitions at $\pi$,
  $2\pi$, $3\pi$, $4\pi$. Time axis ticked $\pi$ to $5\pi$.

[def] **How the back-to-back pair works** (upper circuit) ·J p56 + [added] mechanism:

- On the **positive** half cycle the upper diode is reverse biased and **breaks down at $V_Z$**,
  while the lower diode is forward biased and adds its small forward drop. The node is held at
  about $V_Z + V_F$.
- On the **negative** half cycle the roles swap and the node is held at about $-(V_Z + V_F)$.
- Between the two limits neither diode conducts and the output follows the input through the
  $R$–$R_L$ divider.

[eq] **[added] Clip level for a symmetric zener limiter:**

$$\boxed{\;v_{out(\max)} = \pm\left(V_Z + V_F\right) \approx \pm\left(25 + 0.7\right) = \pm25.7\ \mathrm{V}\;}$$

- $V_F$ — forward drop of the *other* diode of the pair, in V (0.7 V for silicon)

*The notes draw the flats at exactly ±25 V, i.e. they neglect $V_F$. That is the usual
approximation and it is fine to quote ±25 V; know where the extra 0.7 V comes from.* [added]

> ⚠ VERIFY **JV5.6** ·J p56 — **the lower of the two "both sides" circuits has its second zener the
> wrong way round.** As drawn, both diodes point the same way (upper anode to lower cathode), so:
> - for a **positive** input, both are reverse biased and the branch does not conduct until the
>   node reaches $2V_Z = 50$ V, not 25 V;
> - for a **negative** input, both are forward biased and the branch clamps at about $-1.4$ V.
>
> That is a **strongly asymmetric** limiter, +50 V against −1.4 V, and it cannot produce the
> symmetric waveform drawn directly beneath it. The **upper** circuit of the pair is drawn
> correctly. Correct form — the two zeners must be joined **anode to anode** (as in the upper
> circuit) or **cathode to cathode**; either works, and both give
> $$\boxed{\;v_{out} = \pm\left(V_Z + V_F\right)\;}$$
> Two zeners in series *aiding*, as drawn in the lower circuit, are the **voltage-reference divider**
> arrangement (two levels from one supply), a different circuit for a different purpose — see
> `11-diodes.md` §1.10, Fig. 54.8. See `_verification-log.md`.

*[added] **Why anyone would want this.** A symmetric zener limiter is the standard input-protection
and waveform-squaring circuit: it protects a following stage from over-voltage, and with a large
enough input it turns a sinusoid into an approximate square wave, which is exactly what the drawn
output shows. It is the last circuit in this range and the natural bridge to the clipper material
in `12-rectifiers.md` §2.13.*

---

## 5.25 [table] Everything in ·J p46–p56 worth carrying into an exam

All in **corrected** form; the flag column says where the page differs.

| Quantity | Formula | Page | Flag |
|---|---|---|---|
| HW average current | $I_{dc} = \dfrac{1}{2\pi}\displaystyle\int_0^{\pi} I_m\sin\theta\,d\theta = \dfrac{I_m}{\pi} = 0.3183\,I_m$ | ·J p47 | JC5.1 |
| HW rms current | $I_{rms} = \dfrac{I_m}{2}$ | ·J p47 | — |
| dc power | $P_{dc} = I_{dc}V_{dc} = I_{dc}^{2}R_L$ | ·J p47 | — |
| ac power | $P_{ac} = I_{rms}^{2}\left(R_L + r_f\right)$ | ·J p47 | — |
| HW efficiency | $\eta = \dfrac{4}{\pi^{2}\left(1 + r_f/R_L\right)}$; max $\dfrac{4}{\pi^{2}} = 40.5\,\%$ | ·J p47 | ⚠ JV5.1, JC5.2 |
| ac/dc split | $I_{rms}^{2} = I_{dc}^{2} + I_{ac}^{2}$ | ·J p47–p48 | — |
| HW ripple factor | $\gamma = \sqrt{\dfrac{\pi^{2}}{4} - 1} = 1.21$ | ·J p48 | JC5.3 |
| FW average current | $I_{dc} = \dfrac{1}{\pi}\displaystyle\int_0^{\pi} I_m\sin\theta\,d\theta = \dfrac{2I_m}{\pi} = 0.6366\,I_m$ | ·J p48–p49 | ⚠ ILLEGIBLE (p49 line 1) |
| FW rms current | $I_{rms} = \dfrac{I_m}{\sqrt2} = 0.707\,I_m$ | ·J p49 | ⚠ JV5.2 |
| FW efficiency | $\eta = \dfrac{8}{\pi^{2}\left(1 + r_f/R_L\right)}$; max $\dfrac{8}{\pi^{2}} = 81.1\,\%$ | ·J p49 | ⚠ JV5.3, JC5.2 |
| FW ripple factor | $\gamma = \sqrt{\dfrac{\pi^{2}}{8} - 1} = 0.48$ | ·J p49 | — |
| Ripple frequency | $f$ (half-wave), $2f$ (full-wave) | ·J p46, p48, p50 | — |
| Capacitor charging | $V_C = V_S\left(1 - e^{-t/r_f C}\right)$ | ·J p51 | ⚠ JV5.5 |
| Capacitor discharging | $V_C = V_S\,e^{-t/R_L C}$ | ·J p51 | ⚠ JV5.5 |
| Zener off-state test | $V_{RL} = \dfrac{V_SR_L}{R + R_L}$; on if $V_{RL} > V_Z$ | ·J p55 | — |
| Zener on-state load current | $I_{RL} = \dfrac{V_Z}{R_L}$ | ·J p55 | — |
| Zener on-state total current | $I_t = \dfrac{V_S - V_Z}{R} = I_{RL} + I_Z$ | ·J p55 | — |
| Zener current | $I_Z = I_t - I_{RL}$ | ·J p55 | — |
| Zener power | $P_Z = I_ZV_Z$ (watts) | ·J p55 | JC5.4 |
| Symmetric clip level | $v_{out} = \pm\left(V_Z + V_F\right)$ | ·J p56 | ⚠ JV5.6, JV5.7 |

---

## 5.26 How this range compares with the tier-2 file `12-rectifiers.md`

`12-rectifiers.md` is built from **·L2**, a 26-page textbook extract, and is fully verified with 43
flags of its own. The two documents were compared item by item on every constant this range
derives.

[table] **Where the two agree — all four constants, both efficiencies, both ripple factors**

| Point | This document (·J) | Tier 2 (·L2) | Verdict |
|---|---|---|---|
| **HW average** | $I_{dc} = I_m/\pi = 0.3183\,I_m$ ·J p47 | $I_{L(dc)} = I_{LM}/\pi = 0.318\,I_{LM}$ ·L2 p3 | **agree exactly** |
| **HW rms** | $I_{rms} = I_m/2$ ·J p47 | $I_L = I_{LM}/2 = 0.5\,I_{LM}$ ·L2 p3 | **agree exactly** |
| **FW average** | $I_{dc} = 2I_m/\pi$ ·J p48–p49 | $I_{L(dc)} = 2I_{LM}/\pi = 0.636\,I_{LM}$ ·L2 p8 | **agree exactly** |
| **FW rms** | $I_{rms} = I_m/\sqrt2$ ·J p49 | $I_L = I_{LM}/\sqrt2 = 0.707\,I_{LM}$ ·L2 p8 | **agree exactly** |
| **HW ripple factor** | $\sqrt{\pi^{2}/4 - 1} = 1.21$ ·J p48 | $\sqrt{\pi^{2}/4 - 1} = 1.211$ ·L2 p5 | **agree**; ·L2 also reaches it from the form factor $K_f = \pi/2$ and from the harmonic sum |
| **FW ripple factor** | $\sqrt{\pi^{2}/8 - 1} = 0.48$ ·J p49 | $\sqrt{\pi^{2}/8 - 1} = 0.483$ ·L2 p9 | **agree**; ·L2's page prints 0.482, flagged **C2.12** |
| **The ripple identity** | $I_{rms}^{2} = I_{dc}^{2} + I_{ac}^{2}$ ·J p47, p49 | same, plus $\gamma = \sqrt{K_f^{2}-1}$ ·L2 p5 | agree; ·L2 fuller |
| **$P_{dc} = I_{dc}^{2}R_L$** | ·J p47, p49 | ·L2 p4 — but ·L2 p8 misprints it as $I_{dc}^{2}(R_0+R_L)$, flagged **V2.10** | **·J is right; ·L2's full-wave page is wrong** |

[table] **Where they disagree on a number**

| Point | This document (·J) | Tier 2 (·L2) | Which to teach |
|---|---|---|---|
| **HW efficiency** | **40.5 %** ·J p47 | handout prints **40.6 %**, and one line prints **409.6 %** (flagged **V2.2**); the file corrects to 40.5 % | **·J.** $4/\pi^{2} = 40.53\,\%$, so ·J's rounding is the right one; ·L2's parent textbook rounds up, flagged **C2.4** |
| **FW efficiency** | **81.1 %** ·J p49 | handout prints **81.2 %**; the file corrects to 81.1 % | **·J.** $8/\pi^{2} = 81.06\,\%$ |
| **FW ripple factor, printed** | **0.48** ·J p49 | **0.482** ·L2 p9, flagged **C2.12** as unreachable from either quoted intermediate | **either**; the exact value is 0.483 |

*The headline: on the eight constants this range derives, **the two independent sources agree
everywhere, and where their printed roundings differ ·J is the more accurate of the two.** That is
a strong mutual confirmation — the ·J derivations survive an independent check.*

[table] **Peak inverse voltage — ·J is silent, ·L2 is the only source**

| Circuit | This document (·J) | Tier 2 (·L2) |
|---|---|---|
| Half-wave | **not mentioned** | $\mathrm{PIV} = V_{sm}$ ·L2 p5 |
| Centre-tap full-wave | **not mentioned** | $\mathrm{PIV} = 2V_{sm}$ ·L2 p9 — the circuit's chief drawback |
| Bridge | **not mentioned** | $\mathrm{PIV} = V_{sm}$ ·L2 p11–p12 — **half** the centre-tap requirement, and the bridge's main advantage |

**·J mentions PIV once, on ·J p46, only as a diode *rating*** ("rectifier diodes … have a high power
rating and peak inverse voltage / breakdown voltage" — see **JC5.11**), and never computes it for a
circuit. **Take PIV from `12-rectifiers.md`.** Note that without it, ·J p50 gives no reason to
prefer the bridge over the centre-tap circuit at all.

[table] **Where each source is the only one**

| Topic | Only in | Note |
|---|---|---|
| **Smoothing: capacitor filter, choke-input filter, Π filter** | **·J** (§5.15–§5.17) | **This is the important one.** `12-rectifiers.md` §2.12 is headed *"[added] Smoothing — supplied here, NOT in the handout"* — its whole smoothing section is our own material, written because ·L2 promises smoothing on its p1 and never delivers it. **·J p50–p53 is therefore the knowledge base's only *primary* source for filters**, and the only place the course's own three circuits, waveforms and charge/discharge equations appear. |
| **The zener as the supply's stabiliser block** | **·J** (§5.18–§5.22) | ·L2 has no zener material at all; `11-diodes.md` §1.8–§1.10 has it from ·L1, but as a *diode* topic, not as the fourth block of a power supply |
| **The off-state / on-state two-circuit method** | **·J** (§5.20–§5.21) | ·L1's version is the three-point bias checklist (`11-diodes.md` §1.8); ·J's is the "swap in a battery or an open circuit" method, which is more directly usable |
| **Zener voltage clipping** | **·J** (§5.23–§5.24) | ·L2 §2.13 has clippers built from **ordinary** diodes and batteries, never from zeners |
| **PIV, TUF, form factor** | **·L2** | see the table above; TUF 0.287 (HW), 0.693 (centre-tap) |
| **Fourier content of the rectified wave** | **·L2** (§2.6(d), §2.7.4) | the harmonic route to the same ripple factors, and why full-wave has no fundamental |
| **Three-phase rectifiers, clampers, voltage multipliers** | **·L2** (§2.9–§2.10, §2.14–§2.15) | absent from ·J entirely |
| **Ripple-design formulas $V_{r(pp)} = I_{dc}/f_r C$, $C = 1/2\sqrt3\gamma f_r R_L$** | **neither** | both are `[added]` in `12-rectifiers.md` §2.12; no source in this knowledge base states them |
| **Zener regulator design ($R$ from $I_{z\max}$), $I_{z\min}$/$I_{z\max}$ band, dynamic impedance** | **·L1** | `11-diodes.md` §1.9–§1.10, with four worked regulator examples |

**No genuine disagreement on the physics was found between ·J and ·L2 anywhere in this range.**
Every difference is one of scope or of printed rounding.

---

## 5.27 Coverage, emphasis and exam triage

**What this range is.** Eleven pages, and unusually **derivation-heavy for these notes**: ·J p47,
p48 and p49 are almost nothing but integration and algebra, and ·J p55 is a fully worked numerical
example. Set against that, ·J p50–p53 is descriptive (filters) and ·J p53–p54 is descriptive
(zener construction and characteristic). Roughly **five pages of mathematics to six of prose and
figures** — a much higher mathematical density than ·J p33–p45, and the balance of study time
should follow it.

**Highest exam value — work these until they are automatic:**

1. **The four-integral derivation set** (§5.4–§5.7 and §5.9–§5.11). Average, rms, efficiency,
   ripple factor — done twice, once per circuit. It is the most heavily worked material in the
   whole of ·J p33–p56, and *"derive the efficiency of a half-wave rectifier"* is the single most
   predictable question in this range. Memorise the four results and be able to reproduce the two
   integrals.
2. **The unsolved problem on ·J p50** (§5.13). An unsolved question in a set of lecture notes is
   the likeliest of all CAT questions to be lifted verbatim. Seven quantities, clean numbers,
   one transformer step. Work it until it takes five minutes.
3. **The zener two-state method and the ·J p55 example** (§5.21–§5.22). Four equations, one test,
   one worked set of numbers — and the test ($V_{RL} > V_Z$?) is the step candidates skip.
4. **Redrawing all five circuits from memory** — half-wave, centre-tap, bridge, and the three
   filters — with their waveforms. Every one of them is a plausible "sketch and explain" question.

**Moderate value — know the statements and the pictures:**

5. **The three filters** (§5.15–§5.17): what each is made of, which component does what, and the
   ranking. Short descriptive answers; the charge/discharge exponentials are quotable.
6. **The zener characteristic and equivalent circuits** (§5.19–§5.20). Four labels on one curve.
7. **The two clipping circuits** (§5.23–§5.24), as sketches with their output waveforms — but see
   **JV5.6** and **JV5.7** before reproducing either figure.

**Low value here:**

8. The block diagram (§5.1) — one mark, and it is the same four boxes everywhere.
9. The half-wave *operation* paragraph (§5.3) — three sentences, already implied by the waveform.

**Three things this range does not teach at all:** **peak inverse voltage** for any circuit,
**transformer utilisation factor**, and **any quantitative filter design**. The first two are in
`12-rectifiers.md`; the third is in no source here.

---

## 5.28 Word and typography slips, collected

> ⚠ VERIFY **JC5.10** — grammar and word-substitution slips across ·J p46–p56, gathered here
> because none of them changes anything computed. Listed so a reader meeting them on the page knows
> they are the source's, not a misreading.
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·J p46 | "therefore an output can be **from** the resistor $R_L$" | can be **taken from** |
> | ·J p50 | "there will be an output at $R_L$ **is** as a result of $D_1$ and $D_4$" | strike the "is" |
> | ·J p50 | "It is made **using of** capacitors and inductors" | made **using** / made **use of** |
> | ·J p51 | "This will result **to** an output with more of DC component" | result **in** |
> | ·J p52 | "Ripple factor is less than **of** half – wave rectifier" | less than **that of** |
> | ·J p52 | "there will be a minimized a.c at the output" (for *minimised*) | spelling only |
> | ·J p53 | "This results **to** a more refined d.c component" | results **in** |
> | ·J p54 | "In forward bias it behaves like any other diode **conducts** at…" | diode **and conducts** at |
> | ·J p54 | "to limit amount of current related to diode **the rating**" | **the diode rating** — words transposed |
>
> See `_verification-log.md`.

**Naming note, not an error.** ·J p52 heads the C–L–C section *"Capacitor input filter (Π filter)"*
with a **capital** Greek Pi. That is legitimate here — the name comes from the **shape** of the
C-L-C network, which resembles the letter Π — and is different from the misuse of capital Π for the
constant $\pi$ flagged at ·J p45 as **JC4.12**. Most textbooks write it "π-filter"; both are in use.

---

## 5.29 Items needing a clean page

Listed for the record; everything else in ·J p46–p56 is fully recovered.

| Item | Page | Status |
|---|---|---|
| Section heading above the power-supply block diagram | ·J p46 | **lost with the blank space at the foot of ·J p45** — not a redaction. Never fill it |
| Opening sentence of *Construction* (zener) | ·J p53 | ⚠ REDACTED — **not recovered**. Subject inferable (heavy doping); wording destroyed. Needs a screenshot of ·J p53 |
| Opening sentence of *Operation* (zener) | ·J p53 | ⚠ REDACTED — **not recovered**. Subject inferable (reverse-bias connection); wording destroyed. Needs a screenshot of ·J p53 |
| Label above the regulator data block | ·J p55 | ⚠ REDACTED — **not recovered**, but the size and position make it the word **Example**; nothing depends on it |
| First line of the page, $I_{rms} = \sqrt{I_{dc}^{2}+I_{ac}^{2}}$ | ·J p48 | ⚠ ILLEGIBLE — clipped by the page margin; **recovered with high confidence** from the identical line printed in full on ·J p49 |
| First line of the page, the full-wave average evaluation | ·J p49 | ⚠ ILLEGIBLE — clipped by the page margin; only about 14 pixel rows survive. The **result** $2I_m/\pi$ is confirmed from its two later uses on the same page, but the printed line itself cannot be read |
| A whole line of text before "first circuit." | ·J p52 | **content gap** — the line is absent, not merely clipped. Not reconstructed |
| Top rail of the one-sided clipping circuit | ·J p56 | ⚠ ILLEGIBLE — cut by the page margin; the branch elements are all legible |
| "(b) Bridge Rectifier" heading | ·J p50 | **never typed** — see **JC5.6**. Not a redaction and not a page-break loss |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
