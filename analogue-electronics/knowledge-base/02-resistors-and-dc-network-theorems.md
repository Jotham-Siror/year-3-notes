---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "02 — Resistors, DC Circuit Analysis and Network Theorems"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 10-23"
pages: "J p10-p23"
tier: primary
file_role: topic
subtopics:
  - "terms and concepts: charge, current, voltage, potential difference, power"
  - "what a resistor is; passive versus active components; the two circuit symbols"
  - "the four factors that fix the resistance of a conductor; resistivity and R = rho L / A"
  - "the four-band colour code: full colour/digit/multiplier/tolerance table"
  - "decoding colour bands to a resistance and a tolerance range"
  - "encoding a resistance and tolerance back into colour bands"
  - "reading bands from the wrong end: the two reverse-order exercises"
  - "the BS 1852 letter notation (900R, 5K8, 7M4, 4K54)"
  - "Ohm's law, the V-I-R triangle and the three power forms"
  - "resistors in series: same current, voltages add, resistances add"
  - "resistors in parallel: same voltage, currents add, conductances add"
  - "a six-resistor combined series-parallel network reduced and back-substituted in full"
  - "power rating: building a 1000 ohm 10 W resistor out of 2 W parts, in series and in parallel"
  - "the practical voltage source: internal resistance, Ri << RL, two load cases"
  - "the constant-current source: Ri >> RL, two load cases"
  - "Thevenin's theorem: statement, three-step procedure, general case worked symbolically"
  - "Norton's theorem: statement, procedure, the current-divider form, a 40 V four-resistor example"
  - "mesh analysis of a two-source, three-branch loop"
  - "factors considered when selecting a resistor"
  - "resistor types: wire-wound, composition, metal-film, potentiometer, rheostat, integrated-circuit"
key_equations: [charge-current, power-vi, resistivity, colour-code-value, tolerance-range, ohms-law, power-forms, series-resistance, series-current, voltage-divider, parallel-resistance, parallel-voltage, product-over-sum, current-divider, source-droop, impedance-polar, thevenin-resistance, thevenin-voltage, thevenin-load-current, norton-current, norton-resistance, norton-load-current, mesh-kvl, mesh-kcl, power-rating-series, power-rating-parallel]
prerequisites: ["the preceding tier-1 file — semiconductor fundamentals and terms (·J p1-p9): charge, conventional current, Q = It"]
leads_to: ["the next tier-1 file — capacitors and the reactive components (·J p24 onward)", "every biasing calculation in 03-bipolar-junction-transistor (voltage dividers, Thevenin equivalents, load lines)", "06-h-parameters-and-bjt-amplifiers (Norton source, current division in the input circuit)"]
verification_flags: 28
tags: [resistor, resistivity, colour-code, tolerance, ohms-law, power-rating, series, parallel, voltage-divider, current-divider, thevenin, norton, mesh-analysis, kirchhoff, voltage-source, current-source, internal-resistance, potentiometer, rheostat, wire-wound, metal-film, dc-analysis]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·J pN = provenance (which PDF page of the lecture notes the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 02 — Resistors, DC Circuit Analysis and Network Theorems

Scope: **·J p10–p23** of the course's own lecture notes — the passive-component and dc-circuit
block. It runs from the definitions of voltage and power, through resistors and the colour code,
Ohm's law, series/parallel/combined networks, power rating, the two source models, Thevenin's and
Norton's theorems, mesh analysis, and finishes on how resistors are chosen and how they are made.

**Citation.** Page references are to the **PDF page**: `·J p14`. The document's own printed page
number runs **one behind** the PDF page — PDF p14 prints "13" in its footer — and the offset holds
unbroken across the whole document. Only PDF pages are cited below.

---

## 2.0 Why this file matters more than most

> ### This is the **only** source in the knowledge base for everything in it
>
> The seven tier-2 lesson documents (`·L1`–`·L7`, 169 pp.) contain **no treatment of dc network
> theory or of passive components at all**. A search of all seven turns up:
>
> - **Thevenin** — used in `03-bipolar-junction-transistor` only to *apply* an equivalent to a
>   voltage-divider bias network (·L3 p22); the theorem itself is assumed, never stated or derived.
> - **Norton** — used in `06-h-parameters-and-bjt-amplifiers` only as one algebraic step inside an
>   input-circuit transformation (·L6 p12); again assumed.
> - **Colour coding, resistivity, series/parallel reduction, mesh analysis, power rating, source
>   models** — absent entirely.
>
> So there is no second opinion to fall back on and no fuller derivation to consult. Everything in
> ·J p10–p23 is transcribed here, every number is recomputed, and every gap is marked rather than
> filled.

**Weighting.** This is the most arithmetic-dense stretch of the whole document: roughly a dozen
worked examples in fourteen pages, and almost no derivation. Teach it the way the notes do — set up
the rule in two lines, then work numbers.

> ### ⚠ Gaps in these pages — none of them filled in
>
> 1. **·J p10, first line.** The "Terms and concepts" list that began on ·J p9 continues, but the
>    entry label is lost at the page break: only the formula $I = Q/t$ survives at the top of p10.
>    The term being defined is plainly **current**, and ·J p9 gives $Q = It$ immediately above.
> 2. **·J p12, first line.** The stem of the colour-band exercise is truncated to the two words
>    *"left are."* — see §2.3.5. The rest of the sentence is not on ·J p11 either; it is lost at the
>    page break.
> 3. **·J p14, first line.** The opening line of part (d) of the parallel example is clipped by the
>    page edge; only *"(d) … $R_1$   900"* survives (§2.8). ⚠ ILLEGIBLE.
> 4. **·J p20, first line.** Clipped in the same way; only *"$R_t$"* survives of what must be
>    $I_t = V_s/R_t$ (§2.14). ⚠ ILLEGIBLE.
> 5. **No section headings for the two source models.** ·J p16 and ·J p17 present the
>    voltage-source and constant-current-source material with **no heading of any kind** — the
>    figures simply start. The headings appear to have been lost with the white space above them,
>    the same failure the notes show on ·J p31, p33 and p57. The section titles used below
>    (§2.11, §2.12) are this file's own.
> 6. **·J p23 is not the end of the resistor material.** The "Resistor Types" section runs three
>    paragraphs into ·J p24 (the rest of the potentiometer, the rheostat, integrated-circuit
>    resistors) before the **CAPACITORS** heading begins the next topic. Those three paragraphs are
>    included in §2.17 and cited `·J p24`; everything on ·J p24 from **CAPACITORS** onward belongs
>    to the next file.
>
> There are **no opaque redaction blocks** anywhere in ·J p10–p23. The first of those is on ·J p35.

---

## 2.1 Terms and concepts — charge, current, voltage, power ·J p10

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $Q$ | electric charge | C (coulomb) | — |
| $I$ | current | A | mA in signal circuits |
| $t$ | time | s | — |
| $V$ | voltage / electromotive force | V | 5–50 V here |
| $P$ | power | W | 0.125–2 W for a resistor |

[eq: charge-current] Charge and current are two views of the same thing. ·J p9–p10

$$\boxed{\;Q = It \qquad\Longleftrightarrow\qquad I = \frac{Q}{t}\;}$$

- $Q$ — charge, in coulombs (C)
- $I$ — current, in amperes (A)
- $t$ — time, in seconds (s)

The notes define charge as *"the amount of current passing through a given point for a given
time"*, and add *"it is the ability to attract or repel electrons"*. ·J p9

[def] **Voltage** — the energy which drives charge **across a circuit**. Also called
**electromotive force (emf)**. SI unit: the volt (V). ·J p10

[def] **Potential difference** — the energy which drives charge **across a component** in a
circuit. Same unit. ·J p10

> ⚠ VERIFY **JC2.3** ·J p10 — voltage is defined as *"the energy which drives charge"*. Energy is
> not voltage: voltage is **energy per unit charge**,
> $$V = \frac{W}{Q}\ \ \left[\frac{\mathrm{J}}{\mathrm{C}}\right]$$
> Nothing computed later depends on it, but the definition as printed is dimensionally wrong — a
> volt is a joule per coulomb, not a joule. See `_verification-log.md`.

*[added] The distinction the notes are drawing is the useful one: **emf** is what the source
supplies to the whole loop, **p.d.** is what appears across one component in it. Both are measured
in volts, and in §2.11 the difference between the two — the drop across the source's own internal
resistance — is exactly what the worked example is about.*

[def] **Power** — the rate of energy dissipation in a component. ·J p10

[eq: power-vi]

$$\boxed{\;P = \text{Voltage} \times \text{Current} = VI\;}$$

- $P$ — power, in watts (W)

> ⚠ VERIFY **JC2.2** ·J p10 — the entry reads *"Power … Is the amount of energy dissipated in a
> conductor carrying a current of 1A. If the p.d across the conductor 1V"*. Two slips in one
> sentence: **(i)** power is a **rate** of energy conversion, not an amount — the page's own first
> line says so; **(ii)** the sentence with the 1 A and 1 V in it is the definition of the **watt**,
> not of power. Correct reading: *one watt is the power dissipated in a conductor carrying 1 A when
> the p.d. across it is 1 V*. See `_verification-log.md`.

---

## 2.2 Resistors, and what fixes a resistance ·J p10

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $R$ | resistance | Ω | 10 Ω – 10 MΩ |
| $\rho$ | resistivity of the material | Ω m | $1.7\times10^{-8}$ Ω m (copper) |
| $L$ | length of the conductor | m | — |
| $A$ | cross-sectional area | m² | — |

[def] A **resistor** is a **passive component** which opposes the flow of current in a circuit.
·J p10

> ⚠ VERIFY **JC2.1** ·J p10 — printed as *"A resistor is a passive component which **apposes** the
> flow of current in **Q** circuit"*. Two typing slips: **apposes** → *opposes*, and the stray **Q**
> → *a*. See `_verification-log.md`.

[fig ·J p10] **The two resistor symbols.** Drawn side by side on one line: on the left the
**zig-zag** (US/ANSI) symbol — a horizontal lead, four or five sharp triangular peaks, a horizontal
lead out; on the right the **rectangular box** (IEC/BS) symbol — a horizontal lead into a plain
open rectangle lettered **R**, and a lead out. No values are marked on either. Both symbols are
used interchangeably in the rest of the notes: ·J p12–p13 use the box, ·J p16–p22 use the zig-zag.

[def] **Passive component** — two properties: ·J p10

1. It **does not add strength to a signal**.
2. It **does not require power to operate**.

[def] **Active components** — e.g. diodes, transistors — **do** require power to operate and **do**
add strength to a signal. ·J p10

[def] **Resistance** ($R$), measured in **ohms** $[\Omega]$, is the opposition to the flow of
current. ·J p10

### The four factors that fix a conductor's resistance ·J p10

[fig ·J p10] **A cylindrical conductor.** A long horizontal capsule (a cylinder drawn in
perspective, rounded at both ends). A short leader line on the left points to the shaded elliptical
end face and is labelled **Area**; a double-headed dimension arrow runs the full length underneath
and is labelled **Length**.

| # | Factor | Dependence as printed ·J p10 |
|---|---|---|
| (a) | Length, $L$ (m) | $R \propto L$ |
| (b) | Cross-sectional area, $A$ | $R \propto \dfrac{L}{A}$ |
| (c) | Resistivity, $\rho$ (Ω m) | $R \propto \rho$ |
| (d) | Temperature | *(stated as a factor; no relation given)* |

> ⚠ VERIFY **JC2.4** ·J p10 — factor (b) is headed *"Cross sectional Area"* but the relation printed
> beside it is $R \propto L/A$, which is the **combined** dependence on length *and* area. Taken on
> its own the area factor is
> $$R \propto \frac{1}{A}$$
> — resistance **falls** as the conductor gets fatter. The final formula on the same page is
> correct, so nothing computed changes. See `_verification-log.md`.

> ⚠ VERIFY **JC2.5** ·J p10 — the proportionality sign is typed as a Greek **alpha**: the page reads
> *"R α L"*, *"R α ρ"*. It means $\propto$. Worth knowing because **$\alpha$ is the common-base
> current gain** throughout the transistor topics of this same course, and the two look identical on
> the page. See `_verification-log.md` and `_nomenclature.md`.

[eq: resistivity] Combining (a)–(c): ·J p10

$$\boxed{\;R = \rho\,\frac{L}{A}\;}$$

- $R$ — resistance, in ohms (Ω)
- $\rho$ — resistivity of the material, in ohm-metres (Ω m)
- $L$ — length, in metres (m)
- $A$ — cross-sectional area, in square metres (m²)

*[added] Unit check, since the notes do not do one:
$\Omega\,\mathrm{m} \times \mathrm{m} / \mathrm{m^2} = \Omega$ ✓. The temperature factor (d) is
listed but no coefficient is given anywhere in ·J p10–p23, so nothing in this file uses it.*

---

## 2.3 Colour coding ·J p10–p12

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| band 1, band 2 | first and second significant digits | — | 0–9 |
| band 3 | multiplier (number of zeros) | — | $10^{-2}$ … $10^{9}$ |
| band 4 | tolerance | % | ±1 % … ±20 % |

[def] **Resistor colour coding** is the process of representing the resistance of a resistor using
**colour bands**, marked on the surface of the resistor. ·J p11

Colour coding comes in **2 types**: **4-colour** resistors and **5-colour** resistors. ·J p11

[fig ·J p10] **The four-band resistor.** A horizontal lead enters a long open rectangle (the
resistor body) and a lead leaves the far side. Inside the body are **four narrow hatched bands**,
evenly spaced, the fourth sitting a little further right with a wider gap of plain body after it.
Four leader lines drop from the bands to arrowed labels: from band 1 to **1ˢᵗ No** (arrow pointing
left), from band 2 to **2ⁿᵈ No** (arrow pointing left, drawn lower), from band 3 to **Multiplier**
(arrow pointing right, drawn lower), and from band 4 to **Tolerance** (arrow pointing right).
Caption underneath: *"4 colour Band resistor"*.

### 2.3.1 The colour table ·J p11

[table] **The complete four-band code, exactly as ·J p11 prints it**

| Number | Colour | Multiplier | Tolerance |
|---|---|---|---|
| 0 | Black | $10^{0}$ | — |
| 1 | Brown | $10^{1}$ | ±1 % |
| 2 | Red | $10^{2}$ | ±2 % |
| 3 | Orange | $10^{3}$ | — |
| 4 | Yellow | $10^{4}$ | — |
| 5 | Green | $10^{5}$ | — |
| 6 | Blue | $10^{6}$ | — |
| 7 | Violet | $10^{7}$ | — |
| 8 | Grey | $10^{8}$ | — |
| 9 | White | $10^{9}$ | — |
| — | Gold | $10^{-1}$ | ±5 % |
| — | Silver | $10^{-2}$ | ±10 % |
| — | **No band** | — | ±20 % |

> ⚠ VERIFY **JC2.6** ·J p11 — the last row of the table is printed *"No. band"*, which reads as
> *"number band"*. It means **no band at all** — a resistor with only three bands, whose tolerance
> is therefore ±20 %. The page's own exercise (ii) in §2.3.5 uses exactly that case.
> See `_verification-log.md`.

*[added] Two working rules that make the table easier to hold: the ten digit colours run in
spectrum order from black through the rainbow to white, and the multiplier is simply
$10^{\text{digit}}$ — so the multiplier column carries no extra information once the digit column is
known. Gold and silver are the only two colours that appear in **both** the multiplier and the
tolerance column, which is why they are also the two that mark which end of the resistor to read
from.*

### 2.3.2 How the bands are read ·J p11

**Four-band resistor:** ·J p11

- 1ˢᵗ colour band → the **1ˢᵗ number**
- 2ⁿᵈ colour band → the **2ⁿᵈ number**
- 3ʳᵈ colour band → the **multiplier**, i.e. the **number of zeros**
- last colour band → the **tolerance**

**Five-band resistor:** the first **3** bands are the numbers, the **fourth** is the multiplier, the
**last** is the tolerance. ·J p11

[def] **Tolerance** is the deviation from the exact value, expressed as a **percentage**. ·J p11

[eq: colour-code-value]

$$\boxed{\;R = \big(10 d_1 + d_2\big)\times 10^{\,m} \;\pm\; T\,\%\;}$$

- $d_1, d_2$ — the digits carried by bands 1 and 2
- $m$ — the exponent carried by the multiplier band
- $T$ — the tolerance percentage carried by the last band

### 2.3.3 [ex] Converting from colour bands to resistance ·J p11

**Statement.** Decode **Orange, Brown, Blue, Silver**.

**Solution** (the page's own)

$$\begin{array}{cccc}
\text{Orange} & \text{Brown} & \text{Blue} & \text{Silver}\\
3 & 1 & \times 10^{6} & \pm 10\,\%
\end{array}$$

$$R = 31\times10^{6}\ \Omega \;\pm\; 10\,\%$$

[eq: tolerance-range] The range that tolerance allows: ·J p11

$$31\times10^{6} \;\pm\; 31\times10^{5}$$

$$= 27.9\times10^{6}\ \text{to}\ 34.1\times10^{6}\ \Omega$$

*[added] Verified: $10\,\%$ of $31\times10^{6}$ is $3.1\times10^{6} = 31\times10^{5}$ ✓;
$31 - 3.1 = 27.9$ ✓ and $31 + 3.1 = 34.1$ ✓. In plain units the resistor is **31 MΩ**, guaranteed to
lie between **27.9 MΩ and 34.1 MΩ**. Note the page's neat trick of writing the tolerance as
$31\times10^{5}$ rather than $3.1\times10^{6}$ — same number, and it keeps the arithmetic in whole
digits.*

### 2.3.4 [ex] Converting from resistance to colour bands ·J p11

Three parts, all solved on the page.

**(i)** $36\times10^{6}\ \Omega \pm 1\,\%$

**Printed answer:** *Orange, Blue, Yellow, Brown*

> ### ⚠ VERIFY **JV2.1** ·J p11 — the multiplier band of part (i) is the wrong colour
>
> The page prints **Orange, Blue, Yellow, Brown** for $36\times10^{6}\ \Omega \pm 1\,\%$.
>
> **Correct form:**
> $$\boxed{\;\text{Orange},\ \text{Blue},\ \textbf{Blue},\ \text{Brown}\;}$$
>
> **Why.** Bands 1 and 2 are right — Orange = 3, Blue = 6. The third band is the multiplier and must
> carry $10^{6}$, which the page's own table gives as **Blue**. **Yellow is $10^{4}$**, so the
> printed code decodes to
> $$36\times10^{4} = 360\ \mathrm{k\Omega}$$
> — a hundred times too small. Brown = ±1 % is correct. See `_verification-log.md`.

**(ii)** $845678 \pm 10\,\%$

**Solution** (the page's own)

$$845678 \;\approx\; 850000 \pm 10\,\% \;=\; 85\times10^{4} \pm 10\,\%$$

$$\Rightarrow\quad \text{Grey},\ \text{Green},\ \text{Yellow},\ \text{Silver}$$

*[added] Verified: Grey = 8, Green = 5, Yellow = $10^{4}$, Silver = ±10 %, giving
$85\times10^{4} = 850\ \mathrm{k\Omega}$ ✓.
The rounding from 845 678 to 850 000 is legitimate and is the point of the
exercise: a four-band code carries only **two** significant figures, so anything beyond the second
digit has to be rounded away. The rounding error here is
$4322/845678 = 0.51\,\%$, comfortably inside the ±10 % the last band promises.*

**(iii)** $4\mathrm{K}54 \pm 2\,\%$

**Solution** (the page's own)

$$4\mathrm{K}54 \;=\; 4.5\times10^{3} \pm 2\,\% \;=\; 45\times10^{2} \pm 2\,\%$$

$$\Rightarrow\quad \text{Yellow},\ \text{Green},\ \text{Red},\ \text{Red}$$

*[added] Verified: Yellow = 4, Green = 5, Red = $10^{2}$, Red = ±2 %, giving
$45\times10^{2} = 4500\ \Omega$ ✓.
Note that the **third and fourth bands are both red** and mean different things —
the third is a multiplier, the fourth a tolerance.*

> ⚠ VERIFY **JC2.7** ·J p11 — part (iii) states *"4K54 … This is **equivalent** to $4.5\times10^{3}$"*.
> $4\mathrm{K}54$ means $4.54\ \mathrm{k\Omega}$, so $4.5\ \mathrm{k\Omega}$ is a **rounding**, not an
> equivalence — the same two-significant-figure truncation part (ii) performs explicitly. The colour
> code that follows is right. See `_verification-log.md`.

> ### [added] The letter-position notation used throughout these pages
>
> The notes write resistances as **900R**, **5K8**, **7M4**, **4K54** without ever explaining the
> convention (BS 1852). The letter marks the **multiplier and the decimal point at the same time**:
>
> | Written | Letter means | Value |
> |---|---|---|
> | 900R | R = ×1 (ohms) | 900 Ω |
> | 5K8 | K = ×10³ | 5.8 kΩ = 5800 Ω |
> | 4K54 | K = ×10³ | 4.54 kΩ = 4540 Ω |
> | 7M4 | M = ×10⁶ | 7.4 MΩ = 7 400 000 Ω |
>
> The point of it is that there is no decimal point to be lost in a photocopy or a fault report. It
> is used in the series and parallel examples on ·J p13 and in part (iii) above.

### 2.3.5 [ex] Reading the bands from the wrong end ·J p12

**Statement** — as it survives. The stem is truncated by the page break; the only words on the page
are:

> *"… left are."*

> ⚠ VERIFY **JC2.8** ·J p12 — the stem of this exercise is **truncated**: the sentence begins on no
> page. ·J p11 ends with part (iii) of the previous exercise and white space; ·J p12 opens with the
> two words *"left are."* The opening — which would have said what is given and from which end to
> read it — is lost at the page break. See **JV2.2** below and `_verification-log.md`.

followed by two parts, each with the page's own solution:

**i.** Brown, Orange, Black, Red

**Solution** (the page's own)

$$\begin{array}{cccc}
\text{Red} & \text{Black} & \text{Orange} & \text{Brown}\\
2 & 0 & 10^{3} & 1\,\%
\end{array}$$

$$R = 20\times10^{3} \pm 1\,\% \;=\; 20\ \mathrm{k\Omega} \pm 1\,\%$$

**ii.** Yellow, brown, Green

**Solution** (the page's own)

$$\begin{array}{cccc}
\text{Green} & \text{Brown} & \text{Yellow} & \\
5 & 1 & 10^{4} & 20\,\%
\end{array}$$

$$R = 51\times10^{4} \pm 20\,\% \;=\; 510\ \mathrm{k\Omega} \pm 20\,\%$$

> ### ⚠ VERIFY **JV2.2** ·J p12 — both solutions silently reverse the order of the bands
>
> **What the page shows.** Part i is *given* as **Brown, Orange, Black, Red** and *solved* as
> **Red, Black, Orange, Brown**. Part ii is given as **Yellow, brown, Green** and solved as
> **Green, Brown, Yellow**. In both cases the solution reads the list backwards, and the page never
> says why.
>
> **What the surviving text supports.** Read left-to-right exactly as listed, the two answers are
> $$\text{i:}\quad 1,\ 3,\ \times10^{0},\ \pm2\,\% \;=\; 13\ \Omega \pm 2\,\%$$
> $$\text{ii:}\quad 4,\ 1,\ \times10^{5},\ \pm20\,\% \;=\; 4.1\ \mathrm{M\Omega} \pm 20\,\%$$
> — neither of which is the printed answer.
>
> **Most likely explanation.** The truncated stem almost certainly read *"…whose colour bands from
> **right to** left are."* — which makes the reversal in both solutions correct, and makes the
> exercise a deliberate test of *which end to start from*. Two independent parts reversing the same
> way is not a slip. **This is an inference from the surviving fragment, not the notes' words**, and
> it cannot be confirmed from the pages supplied.
>
> **What to do in an exam.** State the reading direction you are using before you decode. Both
> readings above are defensible codes; only the direction distinguishes them.
> See `_verification-log.md`.

*[added] Why the ambiguity is real, and how it is resolved in practice. A four-band resistor is read
starting from the band **nearest an end**, with the **tolerance band last** — and in practice the
tolerance band is gold or silver, which settles it instantly. Here neither list contains gold or
silver, so nothing in the colours themselves fixes the direction. Part ii gives the other half of
the clue: it lists only **three** colours, and a three-band resistor is a ±20 % part
(**JC2.6** above), so its tolerance "band" is the empty space — which must sit at the end the
reading finishes at.*

*[added] Verification of the printed answers, in the reversed reading:
part i — Red = 2, Black = 0, Orange = $10^{3}$, Brown = ±1 % → $20\times10^{3} = 20\ \mathrm{k\Omega}$ ✓;
part ii — Green = 5, Brown = 1, Yellow = $10^{4}$, no band = ±20 %, giving
$51\times10^{4} = 510\ \mathrm{k\Omega}$ ✓, tolerance band
$510\ \mathrm{k\Omega}\pm102\ \mathrm{k\Omega}$, i.e. 408 kΩ to 612 kΩ.*

---

## 2.4 Ohm's law and the three power forms ·J p12

[def] **Ohm's law.** The current passing through a conductor is **proportional to the voltage
applied across it**, provided all external factors are constant. ·J p12

$$I \propto V$$

[fig ·J p12] **The V–I–R triangle.** A plain triangle divided by one horizontal line. The top
compartment holds **V**; the bottom compartment is split by an implied vertical into **I** and
**R**, printed as "I X R". Cover the quantity you want with a finger and the remaining two show the
formula: cover $V$ → $I\times R$; cover $I$ → $V$ over $R$; cover $R$ → $V$ over $I$.

[eq: ohms-law] ·J p12

$$\boxed{\;I = \frac{V}{R} \qquad V = IR \qquad R = \frac{V}{I}\;}$$

- $V$ — voltage across the component, in volts (V)
- $I$ — current through it, in amperes (A)
- $R$ — its resistance, in ohms (Ω)

[eq: power-forms] Substituting Ohm's law into $P = VI$ twice gives the three forms: ·J p12

$$\boxed{\;P = IV = I^{2}R = \frac{V^{2}}{R}\;}$$

*[added] Which form to reach for: use $I^{2}R$ when the **current** through the part is the known
quantity (series strings), and $V^{2}/R$ when the **voltage** across it is known (parallel banks).
§2.10 uses one of each.*

---

## 2.5 Resistors in series ·J p12

[fig ·J p12] **The series circuit.** A single rectangular loop. Along the top rail, left to right:
box resistor $\mathbf{R_1}$, then a solid arrowhead on the wire labelled $\mathbf{I_{R1}}$, then
box resistor $\mathbf{R_2}$, another arrowhead, then box resistor $\mathbf{R_3}$. Beneath each resistor a
double-headed dimension arrow between two short end-bars marks its voltage drop, labelled
$\mathbf{V_{R1}}$, $\mathbf{V_{R2}}$, $\mathbf{V_{R3}}$. The bottom rail carries a battery
symbol (long plate marked **+**, short plate marked **−**) labelled $\mathbf{V_{s}}$.

[eq: series-current] The same current flows in every element: ·J p12

$$\boxed{\;I = I_{R1} = I_{R2} = I_{R3}\;}$$

[derivation] Kirchhoff's voltage law round the loop, then Ohm's law on each resistor: ·J p12

$$V_s = V_{R1} + V_{R2} + V_{R3}$$

$$V_s = I_{R1}R_1 + I_{R2}R_2 + I_{R3}R_3$$

$$V_s = I\,(R_1 + R_2 + R_3)$$

[eq: series-resistance]

$$\boxed{\;R_t = R_1 + R_2 + R_3\;}$$

- $R_t$ — total (equivalent) resistance of the string, in ohms (Ω)

[eq: voltage-divider] *[added] The corollary the notes use without stating it — dividing
$V_{Rk} = IR_k$ by $V_s = IR_t$ gives the **voltage-divider rule**:*

$$\boxed{\;V_{Rk} = V_s\,\frac{R_k}{R_t}\;}$$

*It is exactly what §2.6 part (c) computes term by term, and it is the form used for $V_{Th}$ in
§2.13.*

*[added] Two consequences worth stating plainly: $R_t$ is always **larger than the largest**
resistor in the string, and the **largest resistor takes the largest share of the supply** — which
is the whole story of the next example.*

## 2.6 [ex] Three resistors in series across 200 V ·J p13

**Statement.** Three resistors $R_1 = 900\mathrm{R}$, $R_2 = 5\mathrm{K}8$, $R_3 = 7\mathrm{M}4$ are
connected in **series** across a voltage supply of 200 V. ·J p13

(a) Calculate the total resistance. (b) Calculate the total current. (c) Determine the current
passing through each of the resistors. (e) Voltage across each resistor.

> ⚠ VERIFY **JC2.9** ·J p13 — the parts are lettered **(a) (b) (c) (e)** — there is no (d). And the
> solution's part (c) answers *"Voltage across each resistor"* (part e) rather than the currents it
> asks for. Since the circuit is a series string, the answer to (c) as asked is a single number, and
> it is part (b)'s: **the same $27.0\ \mathrm{\mu A}$ flows through all three**.
> See `_verification-log.md`.

**Solution** (the page's own)

**(a)**

$$R_t = 900 + 5800 + 7.4\times10^{6} = 7\,406\,700\ \Omega = 7.407\times10^{6}\ \Omega$$

**(b)**

$$I = \frac{V_s}{R_t} = \frac{200}{7\,406\,700} = 2.700\times10^{-5}\ \mathrm{A}$$

**(c)** using $V = IR$

$$V_1 = \frac{200}{7\,406\,700}\times 900 = 0.0243\ \mathrm{V}$$

$$V_2 = \frac{200}{7\,406\,700}\times 5.8\times10^{3} = 0.1566\ \mathrm{V}$$

$$V_3 = \frac{200}{7\,406\,700}\times 7.4\times10^{6} = 199.8\ \mathrm{V}$$

*[added] Every number verified:*

| Quantity | Recomputed | Printed | ✓ |
|---|---|---|---|
| $R_t$ | 7 406 700 Ω = 7.4067 MΩ | 7 406 700 Ω = 7.407×10⁶ | ✓ |
| $I$ | $2.70026\times10^{-5}$ A | $2.700\times10^{-5}$ A | ✓ |
| $V_1$ | 0.024302 V | 0.0243 V | ✓ |
| $V_2$ | 0.156615 V | 0.1566 V | ✓ |
| $V_3$ | 199.819 V | 199.8 V | ✓ |
| $\sum V$ | **200.000 V** | — | ✓ KVL closes |

*[added] The physical point of the numbers: $R_3$ is 1276 times $R_1$, so it takes 1276 times the
voltage — 199.8 V of the 200 V supply, leaving 24 mV for $R_1$. **In a series string the biggest
resistor dominates**, and the small ones can usually be ignored. Compare §2.8, where the same three
resistors in parallel behave the other way round.*

---

## 2.7 Resistors in parallel ·J p13

[fig ·J p13] **The parallel circuit.** A rectangular outline with a battery (**+** upper plate,
**−** lower) on the left rail labelled $\mathbf{V_{s}}$. Three vertical branches hang between the
top and bottom rails, each containing a box resistor $\mathbf{R_1}$, $\mathbf{R_2}$,
$\mathbf{R_3}$. Beside each resistor a
vertical double-headed arrow marks its voltage, labelled $\mathbf{V_{R1}}$, $\mathbf{V_{R2}}$,
$\mathbf{V_{R3}}$; below each resistor a solid downward arrowhead on the branch wire marks its
current, labelled $\mathbf{I_{R1}}$, $\mathbf{I_{R2}}$, $\mathbf{I_{R3}}$.

> ### ⚠ VERIFY **JV2.3** ·J p13 — the parallel derivation opens with the series rule
>
> The first line under the figure prints
> $$I = I_{R1} = I_{R2} = I_{R3}$$
> That is the **series** result (§2.5), copied over. It is false for the circuit drawn: three
> different resistors across the same supply carry three different currents — the page's own
> worked numbers in §2.8 are 0.222 A, 0.034 A and 0.000027 A.
>
> **Correct form:** in parallel the *voltages* are common and the *currents* add —
> $$\boxed{\;V_s = V_{R1} = V_{R2} = V_{R3}, \qquad I_t = I_{R1} + I_{R2} + I_{R3}\;}$$
>
> **Why.** The page's own next two lines say exactly this, so the opening line contradicts the two
> beneath it. See `_verification-log.md`.

[eq: parallel-voltage] Every branch sees the whole supply: ·J p13

$$\boxed{\;V_s = V_{R1} = V_{R2} = V_{R3}\;}$$

[derivation] Kirchhoff's current law at the top node, then Ohm's law on each branch: ·J p13

$$I_t = I_{R1} + I_{R2} + I_{R3}$$

$$I_t = \frac{V_{R1}}{R_1} + \frac{V_{R2}}{R_2} + \frac{V_{R3}}{R_3}$$

$$I_t = V_s\left(\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}\right)$$

[eq: parallel-resistance]

$$\boxed{\;\frac{1}{R_t} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}\;}$$

[eq: product-over-sum] *[added] For exactly **two** resistors the same statement rearranges to the
product-over-sum form, which is what ·J p18–p21 uses in every Thevenin and Norton calculation:*

$$\boxed{\;R_t = \frac{R_1R_2}{R_1+R_2}\;}$$

*[added] Two consequences: $R_t$ is always **smaller than the smallest** branch resistor, and the
**smallest resistor carries the largest current**. Both are visible in the next example.*

## 2.8 [ex] The same three resistors in parallel across 200 V ·J p13–p14

**Statement.** $R_1 = 900\ \Omega$, $R_2 = 5800\ \Omega$, $R_3 = 7.4\ \mathrm{M\Omega}$, all across
200 V. ·J p13

**Solution** (the page's own)

**(a)**

$$\frac{1}{R_t} = \left(\frac{1}{900} + \frac{1}{5800} + \frac{1}{7.4\times10^{6}}\right)$$

$$R_t = 779.022\ \Omega$$

**(b)**

$$I_t = \frac{V_s}{R_t} = \frac{200}{779.022} = 0.257\ \mathrm{A}$$

**(c)**

$$V_{Rt} = V_{R1} = V_{R2} = V_{R3} = 200\ \mathrm{V}$$

**(d)** — the branch currents, on ·J p14

$$I_{R1} = \frac{V_{R1}}{R_1} = \frac{200}{900} = \ \text{⚠ ILLEGIBLE}$$

$$I_{R2} = \frac{V_{R2}}{R_2} = \frac{200}{5800} = 0.034\ \mathrm{A}$$

$$I_{R3} = \frac{V_{R3}}{R_3} = \frac{200}{7.4\times10^{6}} = 2.703\times10^{-5}\ \mathrm{A}$$

> ⚠ ILLEGIBLE **JC2.11** ·J p14 — the first line of part (d) is **clipped by the top edge of the
> page**. Only the lower halves of the characters *"(d)   …   $R_1$   900"* survive; the result is
> cut off entirely. Needs a screenshot of the top 2 cm of ·J p14 to recover the printed value.
> *[added] The missing value is not in doubt arithmetically:
> $I_{R1} = 200/900 = 0.2222\ \mathrm{A}$ — but that is our computation, not the notes'.*

*[added] Every number verified:*

| Quantity | Recomputed | Printed | ✓ |
|---|---|---|---|
| $R_t$ | 779.0225 Ω | 779.022 Ω | ✓ |
| $I_t$ | 0.256732 A | 0.257 A | ✓ |
| $I_{R1}$ | 0.22222 A | *(clipped)* | — |
| $I_{R2}$ | 0.034483 A | 0.034 A | ✓ |
| $I_{R3}$ | $2.7027\times10^{-5}$ A | $2.703\times10^{-5}$ A | ✓ |
| $\sum I$ | **0.256732 A** | — | ✓ matches $I_t$ |

*[added] The contrast with §2.6 is the lesson. The same three resistors:*

| | Series | Parallel |
|---|---|---|
| $R_t$ | 7.41 MΩ — **bigger than the biggest** | 779 Ω — **smaller than the smallest** |
| Dominated by | $R_3$ = 7.4 MΩ (takes 199.8 V of 200 V) | $R_1$ = 900 Ω (takes 0.222 A of 0.257 A) |
| $R_3$'s role | carries the whole story | carries 0.01 % of the current — negligible |

> ⚠ VERIFY **JC2.10** ·J p13, p14, p15, p21 — a typesetting fault that runs through every worked
> example in these pages: the **decimal point in a bold numeral is set as a separate mid-line dot
> after the digit group**, so fractions print as two numbers. ·J p13 shows
> $\frac{200}{779}.022$ for $\frac{200}{779.022}$; ·J p14 shows $\frac{1}{62}.22$ for
> $\frac{1}{62.22}$, $\frac{1}{25}.135$ for $\frac{1}{25.135}$ and $\frac{50}{9}.39$ for
> $\frac{50}{9.39}$; ·J p15 shows $30.\frac{104}{20}$ for $\frac{30.104}{20}$; ·J p21 shows
> $\frac{40}{16}.67$ for $\frac{40}{16.67}$. Every affected result is arithmetically correct once
> the decimal point is put back. See `_verification-log.md`.

---

## 2.9 [ex] A six-resistor combined series–parallel network ·J p14–p15

The single largest worked example in these pages, and the one most likely to be lifted straight into
a CAT. It is worth learning as a **procedure**, not as a set of numbers.

**Statement.** For the circuit below, find (a) total resistance, (b) total current, (c) current
through each resistor, (d) voltage through each resistor. ·J p14

> ⚠ VERIFY **JC2.12** ·J p14 — part (d) is printed *"Voltage **through** each resistor"*. Voltage is
> **across** a component; current is **through** it. The series example on ·J p13 gets it right
> (*"Voltage across each resistor"*). Nothing computed changes. See `_verification-log.md`.

[fig ·J p14] **The combined network.** A rectangular outline. On the **left rail**, a battery
(**+** upper plate, **−** lower plate) labelled $\mathbf{V_{s} = 50\ \mathrm{V}}$.

- The **top rail** leaves the battery's + terminal and runs right to **node A**.
- From **node A** a vertical branch drops to the bottom rail through box resistor
  $\mathbf{R_{1} = 15\ \Omega}$, with a solid downward arrowhead below it.
- Continuing right along the top rail from node A: box resistor $\mathbf{R_{2} = 10\ \Omega}$ (drawn
  horizontally, with $10\ \Omega$ printed above the box and $R_2$ inside it) with an arrowhead
  pointing right after it,
  reaching **node B**.
- From **node B** a vertical branch drops to the bottom rail through box resistor
  $\mathbf{R_{3} = 20\ \Omega}$, again with a downward arrowhead below it.
- Continuing right along the top rail from node B: box resistor $\mathbf{R_{4} = 40\ \Omega}$ with an
  arrowhead pointing right after it, reaching **node C** at the top-right corner.
- From **node C** a vertical branch drops to the bottom rail through box resistor
  $\mathbf{R_{6} = 50\ \Omega}$, with a downward arrowhead just below node C.
- Also from **node C**, a **diagonal branch** runs down-and-left across the middle of the figure to
  the bottom rail, meeting it directly below node B. It contains box resistor
  $\mathbf{R_{5} = 40\ \Omega}$ drawn slanted along the diagonal, with an arrowhead partway up pointing
  **down-left**, i.e. current flowing from node C down to the bottom rail.
- The **bottom rail** returns to the battery's − terminal; every downward branch lands on it, so it
  is a single node.

**Topology in one line:** $R_5$ and $R_6$ are in parallel between node C and the bottom rail; that
pair is in series with $R_4$ between node B and node C; that combination is in parallel with $R_3$;
that is in series with $R_2$; and the whole thing is in parallel with $R_1$ across the source.

### Step-by-step reduction — the order matters ·J p14

**Solution (a)** (the page's own working)

**Step 1 — the pair furthest from the source.** $R_5 \parallel R_6$:

$$\frac{1}{R_a} = \left(\frac{1}{R_5} + \frac{1}{R_6}\right) = \left(\frac{1}{40} + \frac{1}{50}\right) = \frac{9}{200}$$

$$R_a = \frac{200}{9} = 22.22\ \Omega$$

**Step 2 — add the resistor in series with it.** $R_4$ sits between node B and that pair:

$$R_b = R_a + R_4 = 22.22\ \Omega + 40\ \Omega = 62.22\ \Omega$$

**Step 3 — the parallel branch at node B.** $R_3$ hangs from node B to the bottom rail:

$$\frac{1}{R_c} = \left(\frac{1}{R_b} + \frac{1}{R_3}\right) = \left(\frac{1}{62.22} + \frac{1}{20}\right) \qquad\text{Thus } R_c = 15.135\ \Omega$$

**Step 4 — add the next series resistor.** $R_2$ sits between node A and node B:

$$R_d = R_2 + R_c = 10\ \Omega + 15.135\ \Omega = 25.135\ \Omega$$

**Step 5 — the last parallel branch.** $R_1$ hangs from node A to the bottom rail:

$$\frac{1}{R_t} = \left(\frac{1}{R_1} + \frac{1}{R_d}\right) = \left(\frac{1}{15} + \frac{1}{25.135}\right) \qquad\text{Thus } R_t = 9.39\ \Omega$$

**Solution (b)**

$$I_t = \frac{V_s}{R_t} = \frac{50}{9.39} = 5.32\ \mathrm{A}$$

**Solution (c)** — the voltages and currents, walking back **out** from the source

$$V_{R1} = V_{Rd} = V_{Rt} = 50\ \mathrm{V}$$

$$I_{R1} = \frac{V_{R1}}{R_1} = \frac{50}{15} = 3.33\ \mathrm{A}$$

$$I_{Rd} = \frac{V_{Rd}}{R_d} = \frac{50}{25.135} = 1.989\ \mathrm{A}$$

*(continued on ·J p15)*

$$V_{R2} = I_{R2}\times R_2 = 1.989 \times 10 = 19.89\ \mathrm{V}$$

$$V_{Rc} = I_{Rc}\times R_c = 1.989 \times 15.135 = 30.104\ \mathrm{V}$$

$$V_{R3} = V_{R6} = V_{Rc} = 30.104\ \mathrm{V}$$

> ### ⚠ VERIFY **JV2.4** ·J p15 — $R_6$ is not across $R_c$
>
> The page prints
> $$V_{R3} = V_{R6} = V_{Rc} = 30.104\ \mathrm{V}$$
>
> **Correct form:**
> $$\boxed{\;V_{R3} = V_{Rb} = V_{Rc} = 30.104\ \mathrm{V}\;}$$
>
> **Why.** $R_c$ is the parallel combination of $R_3$ and $R_b$, so the two things across it are
> $R_3$ and $R_b$ — not $R_6$. $R_6$ sits inside $R_a$, two levels further down the ladder, and
> **the page itself computes $V_{R6} = 10.754\ \mathrm{V}$ six lines later**, contradicting this
> line. Substituting $V_{R6} = 30.104\ \mathrm{V}$ would give
> $I_{R6} = 30.104/50 = 0.602\ \mathrm{A}$ instead of the correct 0.215 A, and the branch currents
> would no longer sum to $I_{R4}$. See `_verification-log.md`.

$$I_{R3} = \frac{V_{R3}}{R_3} = \frac{30.104}{20} = 1.505\ \mathrm{A}$$

$$I_{Rb} = \frac{V_{Rb}}{R_b} = \frac{30.104}{62.22} = 0.484\ \mathrm{A}$$

$$I_{R4} = I_{Ra} = I_{Rb} = 0.484\ \mathrm{A}$$

$$V_{R4} = I_{R4}\times R_4 = 0.484 \times 40 = 19.35\ \mathrm{V}$$

$$V_{Ra} = I_{Ra}\times R_a = 0.484 \times 22.22 = 10.754\ \mathrm{V}$$

$$V_{R6} = V_{Ra} = V_{R5} = 10.754\ \mathrm{V}$$

$$I_{R5} = \frac{V_{R5}}{R_5} = \frac{10.754}{40} = 0.269\ \mathrm{A}$$

$$I_{R6} = \frac{V_{R6}}{R_6} = \frac{10.754}{50} = 0.215\ \mathrm{A}$$

### [added] Full numerical verification

*Every value recomputed from the resistor values alone, carrying full precision:*

| Quantity | Exact | Printed ·J p14–p15 | ✓ |
|---|---|---|---|
| $R_a = R_5\parallel R_6$ | 22.2222 Ω | 22.22 Ω | ✓ |
| $R_b = R_a + R_4$ | 62.2222 Ω | 62.22 Ω | ✓ |
| $R_c = R_b\parallel R_3$ | 15.13514 Ω | 15.135 Ω | ✓ |
| $R_d = R_2 + R_c$ | 25.13514 Ω | 25.135 Ω | ✓ |
| $R_t = R_1\parallel R_d$ | 9.39394 Ω | 9.39 Ω | ✓ |
| $I_t$ | 5.32258 A | 5.32 A | ✓ |
| $I_{R1}$ | 3.33333 A | 3.33 A | ✓ |
| $I_{Rd}$ | 1.98925 A | 1.989 A | ✓ |
| $V_{R2}$ | 19.8925 V | 19.89 V | ✓ |
| $V_{Rc}$ | 30.1075 V | 30.104 V | ✓ |
| $I_{R3}$ | 1.50538 A | 1.505 A | ✓ |
| $I_{Rb}$ | 0.48387 A | 0.484 A | ✓ |
| $V_{R4}$ | 19.3548 V | 19.35 V | ✓ |
| $V_{Ra}$ | 10.7527 V | 10.754 V | ✓ |
| $I_{R5}$ | 0.26882 A | 0.269 A | ✓ |
| $I_{R6}$ | 0.21505 A | 0.215 A | ✓ |

*Three independent closure checks, all of which the notes leave to the reader:*

$$I_{R1} + I_{Rd} = 3.333 + 1.989 = 5.322\ \mathrm{A} = I_t \quad\checkmark$$

$$I_{R3} + I_{Rb} = 1.505 + 0.484 = 1.989\ \mathrm{A} = I_{Rd} \quad\checkmark$$

$$I_{R5} + I_{R6} = 0.269 + 0.215 = 0.484\ \mathrm{A} = I_{R4} \quad\checkmark$$

$$V_{R2} + V_{Rc} = 19.89 + 30.104 = 49.99 \approx 50\ \mathrm{V} = V_s \quad\checkmark$$

$$V_{R4} + V_{Ra} = 19.35 + 10.754 = 30.10\ \mathrm{V} = V_{Rb} \quad\checkmark$$

*One line to be careful with: $V_{R4} = 0.484\times40$ is printed as **19.35 V**, but
$0.484\times40 = 19.36$. The printed answer is the **correct** one — it comes from the unrounded
current 0.48387 A, which gives 19.3548 V. This is rounding, not an error.*

### [added] The procedure, abstracted from the numbers

The reduction is what an exam question asks for, and its **order** is the whole of it:

1. **Start at the branch furthest from the source** and collapse it — here $R_5\parallel R_6$.
2. **Work back toward the source**, alternating: add anything in **series**, then combine anything
   in **parallel**, then series, then parallel… Each step replaces two elements with one.
3. Stop when one resistor $R_t$ remains; get $I_t = V_s/R_t$.
4. **Now walk back out**, in the reverse order, using two facts only: elements in **parallel share
   the voltage** you just computed; elements in **series share the current** you just computed.
5. **Check as you go**: at every node the branch currents must sum to the current entering it, and
   round every loop the voltages must sum to the source.

The naming convention the page uses — $R_a$, $R_b$, $R_c$, $R_d$ for the successive combinations —
is worth copying. It keeps the back-substitution honest, because each intermediate resistance
carries its own $V$ and $I$ which you can check against its parts.

---

## 2.10 [ex] Power rating — a 1000 Ω 10 W resistor built from 2 W parts ·J p15

**Statement.** Obtain the **number** of 2-watt resistors and **their resistance value** needed to
yield an equivalent **1000 Ω 10-watt** resistor. ·J p15

**Solution — series** (the page's own)

$$\text{No. of resistors} = \frac{\text{Total wattage}}{\text{Wattage for one resistor}} = \frac{10}{2} = 5\ \text{resistors}$$

$$R_t = R_1 + R_2 + R_3 + R_4 + R_5 = 5R$$

$$1000 = 5R$$

$$R = \frac{1000}{5} = 200\ \Omega$$

> ⚠ VERIFY **JC2.13** ·J p15 — both the series and the parallel working print the denominator as
> *"Wattage for one **reisistor**"*. Read *resistor*. See `_verification-log.md`.

**Solution — parallel** (the page's own)

$$\text{No. of resistors} = \frac{\text{Total wattage}}{\text{Wattage for one resistor}} = \frac{10}{2} = 5\ \text{resistors}$$

$$\frac{1}{R_t} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \frac{1}{R_4} + \frac{1}{R_5} = \frac{5}{R} = \frac{1}{1000}$$

$$R = 1000 \times 5 = 5000\ \Omega$$

[eq: power-rating-series] [eq: power-rating-parallel] **The two answers:**

$$\boxed{\;\text{five } 200\ \Omega\ \text{2 W resistors in series} \;=\; 1000\ \Omega,\ 10\ \mathrm{W}\;}$$

$$\boxed{\;\text{five } 5\ \mathrm{k\Omega}\ \text{2 W resistors in parallel} \;=\; 1000\ \Omega,\ 10\ \mathrm{W}\;}$$

*[added] Verified from first principles — this is the check the notes omit, and it is the check an
examiner wants:*

*Series case. At the full 10 W rating the bank carries*
$$I = \sqrt{\frac{P}{R_t}} = \sqrt{\frac{10}{1000}} = 0.1\ \mathrm{A}$$
*and each 200 Ω element then dissipates*
$$P_1 = I^{2}R = (0.1)^{2}\times200 = 2\ \mathrm{W} \quad\checkmark$$

*Parallel case. At the full rating the bank stands at*
$$V = \sqrt{P R_t} = \sqrt{10\times1000} = 100\ \mathrm{V}$$
*and each 5 kΩ element dissipates*
$$P_1 = \frac{V^{2}}{R} = \frac{100^{2}}{5000} = 2\ \mathrm{W} \quad\checkmark$$

*[added] Why the "total wattage ÷ one resistor's wattage" shortcut works — and when it does not. It
works **only because all $n$ resistors are identical and therefore equally stressed**: identical
resistors in series carry the same current, identical resistors in parallel stand at the same
voltage, so each takes exactly $1/n$ of the total dissipation. Mix values and the rule collapses —
in a series string the **largest** resistor takes the most power ($P = I^2R$), in a parallel bank
the **smallest** does ($P = V^2/R$), and the bank's safe rating is then set by whichever single
resistor reaches its limit first, not by the sum of the ratings.*

---

## 2.11 The practical voltage source — internal resistance ·J p16

> **Heading supplied.** ·J p16 opens straight into a figure with no heading of any kind (gap 5 in
> §2.0). The material is unambiguously the **constant-voltage source**, defined by $R_i \ll R_L$.

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_s$ | source emf (the ideal internal voltage) | V | 6 V here |
| $R_i$ | internal resistance of the source | Ω | 0.005 Ω here |
| $R_L$ | load resistance | Ω | 0.595 Ω / 5.995 Ω here |
| $V_{RL}$ | voltage actually delivered to the load | V | ≈ $V_s$ |
| $Z$ | impedance (ac generalisation of $R$) | Ω | — |
| $X$ | reactance | Ω | — |

[fig ·J p16] **The loaded voltage source.** A single rectangular loop. On the **left rail**, from
the top down: a zig-zag resistor labelled $\mathbf{R_{i} = 0.005\ \Omega}$, then a battery symbol
(**+** upper, **−** lower) labelled $\mathbf{V_{s} = 6\ \mathrm{V}}$. On the **right rail**, a zig-zag
resistor drawn with a **diagonal arrow through it** (the variable-resistor symbol) carrying two
alternative values on two lines: $\mathbf{R_{L1} = 0.595\ \Omega}$ and $\mathbf{R_{L2} = 5.995\ \Omega}$. The
loop is closed top and bottom.

[def] $R_i$ — **internal resistance**; $R_L$ — **load resistance**. ·J p16

[def] A **constant-voltage source** is a voltage source whose internal resistance / impedance is
**very low compared with** the external impedance / load resistance: ·J p16

$$\boxed{\;R_i \ll R_L\;}$$

**Impedance, in passing.** The page notes the ac generalisation: ·J p16

$$Z = R + jX$$

> ### ⚠ VERIFY **JV2.5** ·J p16 — the polar form of the impedance is printed with the magnitude in the denominator
>
> The page prints
> $$Z = \frac{R + jX}{\sqrt{R^{2}+X^{2}}}\ \angle\,\tan^{-1}\frac{X}{R}$$
>
> (the page draws the angle in the British style, as a slash with an underline beneath the
> $\tan^{-1}$ term; it means $\angle$.)
>
> **Correct form:** [eq: impedance-polar]
> $$\boxed{\;Z = R + jX = \sqrt{R^{2}+X^{2}}\ \angle\,\tan^{-1}\frac{X}{R}\;}$$
>
> **Why.** $\sqrt{R^{2}+X^{2}}$ **is** the magnitude of $R + jX$, so the printed quotient has
> modulus exactly **1** for every $R$ and $X$ — it is a unit phasor, not an impedance, and it is
> dimensionless where an impedance must be in ohms. The likely origin is a layout accident: the two
> halves of *"$Z = R + jX = \sqrt{R^2+X^2}\,\angle\,\tan^{-1}(X/R)$"* have been stacked into a
> fraction. Nothing else on the page uses it — everything that follows is purely resistive.
> See `_verification-log.md`.

### [ex] Two loads on the same 6 V source ·J p16

**1ˢᵗ case** — $R_{L1} = 0.595\ \Omega$ (the page's own working)

$$R_t = R_i + R_{L1} = 0.005 + 0.595 = 0.6\ \Omega$$

$$I_t = \frac{V_s}{R_t} = \frac{6}{0.6} = 10\ \mathrm{A}$$

$$V_{RL} = I_tR_L = 10 \times 0.595 = 5.95\ \mathrm{V}$$

**2ⁿᵈ case** — $R_{L2} = 5.995\ \Omega$

$$R_t = R_i + R_{L2} = 0.005 + 5.995 = 6\ \Omega$$

$$I_t = \frac{V_s}{R_t} = \frac{6}{6} = 1\ \mathrm{A}$$

$$V_{RL} = I_tR_L = 10 \times 5.995 = 5.995\ \mathrm{V}$$

> ### ⚠ VERIFY **JV2.6** ·J p16 — the second case multiplies by the first case's current
>
> The last line prints $V_{RL} = I_tR_L = \mathbf{10} \times 5.995 = 5.995\ \mathrm{V}$.
>
> **Correct form:**
> $$\boxed{\;V_{RL} = I_tR_L = 1 \times 5.995 = 5.995\ \mathrm{V}\;}$$
>
> **Why.** The line immediately above it computes $I_t = 6/6 = \mathbf{1\ A}$ for this case; the
> **10 A** belongs to the 1ˢᵗ case. The printed *answer* is right, but the printed *step* is not —
> worked as it stands it gives $59.95\ \mathrm{V}$, ten times the source emf, from a 6 V battery.
> See `_verification-log.md`.

*[added] Verified: case 1 — $6/0.6 = 10\ \mathrm{A}$ ✓, $10\times0.595 = 5.95\ \mathrm{V}$ ✓;
case 2 — $6/6 = 1\ \mathrm{A}$ ✓, $1\times5.995 = 5.995\ \mathrm{V}$ ✓.*

[eq: source-droop] *[added] The general statement the two cases illustrate — the source is just a
voltage divider between $R_i$ and $R_L$:*

$$\boxed{\;V_{RL} = V_s\,\frac{R_L}{R_i + R_L}\;}$$

*and the fractional droop below the ideal emf is $R_i/(R_i+R_L)$:*

| Case | $R_L$ | $R_L/R_i$ | $V_{RL}$ | Droop from 6 V |
|---|---|---|---|---|
| 1 | 0.595 Ω | 119× | 5.95 V | 0.83 % |
| 2 | 5.995 Ω | 1199× | 5.995 V | 0.083 % |

***The lesson.** Ten times the load resistance means ten times less droop. A source is "constant
voltage" to the extent that $R_i/R_L$ is small — the load current changed by a factor of ten between
the two cases (10 A → 1 A) and the terminal voltage moved by 45 mV.*

[fig ·J p16] **The generic voltage-source model** (bottom of the page, uncaptioned). A rectangular
loop. On the left rail, from the top: a zig-zag resistor $\mathbf{R_{i}}$, below it a **circle**
containing **+** over **−** and labelled **DC** to its left — the ideal source. On the right rail, a
zig-zag resistor $\mathbf{R_{L}}$. This is the model every later section assumes: an ideal emf in
**series** with $R_i$.

---

## 2.12 The constant-current source ·J p17

> **Heading supplied.** ·J p17 opens straight into a figure with no heading (gap 5 in §2.0). By its
> content — $R_i \gg R_L$ — the section is the **constant-current source**.

[fig ·J p17] **The loaded current source, drawn as a voltage source.** The same rectangular loop as
§2.11 but with different values: left rail carries a zig-zag $\mathbf{R_{i} = 950\ \mathrm{k\Omega}}$ above a
battery $\mathbf{V_{s} = 1000\ \mathrm{V}}$; the right rail carries a variable-resistor zig-zag with two
alternative values, $\mathbf{R_{L1} = 50\ \mathrm{k\Omega}}$ and $\mathbf{R_{L2} = 150\ \mathrm{k\Omega}}$.

[def] A **constant-current source** has a **very high internal resistance / impedance compared with
the external / load resistance**: ·J p17

$$\boxed{\;R_i \gg R_L\;}$$

### [ex] Two loads on the same 1000 V, 950 kΩ source ·J p17

**1ˢᵗ case** — $R_{L1} = 50\ \mathrm{k\Omega}$ (the page's own working)

$$R_t = R_i + R_{L1} = 950 + 50 = 1000\ \mathrm{k\Omega}$$

$$I_t = I_{RL} = \frac{V_s}{R_t} = \frac{1000}{1000\times10^{3}} = 1\times10^{-3}\ \mathrm{A}$$

**2ⁿᵈ case** — $R_{L2} = 150\ \mathrm{k\Omega}$

$$R_t = R_i + R_{L2} = 950 + 150 = 1100\ \mathrm{k\Omega}$$

$$I_t = I_{RL} = \frac{V_s}{R_t} = \frac{1000}{1100\times10^{3}} = 0.909\times10^{-3}\ \mathrm{A}$$

*[added] Verified: $1000/10^{6} = 1.000\ \mathrm{mA}$ ✓;
$1000/(1.1\times10^{6}) = 0.9091\ \mathrm{mA}$ ✓.*

***The lesson,** stated numerically since the page leaves it implicit: **tripling** the load
(50 kΩ → 150 kΩ) changes the current by only **9 %** (1.000 mA → 0.909 mA), because the load is a
small part of a circuit whose resistance is dominated by $R_i$. Compare §2.11, where the source
held its **voltage** constant instead. The two models are the two extremes of the same divider.*

[fig ·J p17] **The current-source model.** A rectangular outline with **three** vertical branches.
On the left rail, a **circle containing a solid upward arrowhead** — the constant-current source
symbol — with **+** above and **−** below it. A middle vertical branch carries a zig-zag
$\mathbf{R_{i}}$; the right branch carries a zig-zag $\mathbf{R_{L}}$. Note the difference from
§2.11: here $R_i$ is in **parallel** with the source, not in series with it.

> ### ⚠ VERIFY **JV2.7** ·J p17 — the source-transformation sentence, as printed, is not true
>
> The page prints: *"If you short circuit constant voltage source get a constant current source"*.
>
> **Correct form** — the source transformation it is compressing:
> $$\boxed{\;I_N = \frac{V_s}{R_i}\;}$$
> *A constant-voltage source $V_s$ in **series** with $R_i$ is equivalent, at its terminals, to a
> constant-current source of value $I_N = V_s/R_i$ in **parallel** with the same $R_i$ — where
> $I_N$ is the current that flows when the **terminals** are short-circuited.*
>
> **Why the printed sentence misleads.** It is the **terminals** that are shorted to *measure* $I_N$,
> not the source that is shorted to *become* a current source; short-circuiting a real voltage source
> simply collapses its terminal voltage to zero (and, at 6 V into 0.005 Ω in §2.11, would draw
> 1200 A). The transformation also requires $R_i$ to be carried across in parallel — dropping it
> leaves an ideal current source, which is a different circuit. This is the same transformation
> §2.14 uses to get from the Thevenin form to the Norton form.
>
> *[added] For the numbers on this page,
> $I_N = 1000\ \mathrm{V}/950\ \mathrm{k\Omega} = 1.053\ \mathrm{mA}$ — the ideal current that
> the two load cases (1.000 mA, 0.909 mA) approach as $R_L \to 0$.*
> See `_verification-log.md`.

---

## 2.13 Thevenin's theorem ·J p17–p19

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_{Th}$ | Thevenin (open-circuit) voltage at A–B | V | — |
| $R_{Th}$ | Thevenin (looking-in) resistance at A–B | Ω | — |
| $R_L$ | the load removed to find the equivalent | Ω | — |
| A, B | the two terminals the load was connected to | — | — |

[fig ·J p17] **Thevenin's theorem, before and after.** *Left:* a plain rectangle lettered
**Complex Network** with two leads leaving its right-hand side to two small open circles, the upper
labelled **A** and the lower **B**; a zig-zag $\mathbf{R_{L}}$ bridges A to B. *Right:* the
equivalent — a rectangular loop whose left rail carries a zig-zag $\mathbf{R_{Th}}$ above a circle
source marked **DC** labelled $\mathbf{V_{Th}}$, and whose right rail carries the same zig-zag
$\mathbf{R_{L}}$.

[def] **Thevenin's theorem.** A complex network of resistances and voltage sources can be converted
to a **single resistor $R_{Th}$ in series with a single voltage source $V_{Th}$**, where ·J p17–p18

- **$R_{Th}$** is the total resistance obtained when the sources are replaced by their **internal
  resistances or short circuits**, with terminals **A and B open**;
- **$V_{Th}$** is the voltage across the two terminals **A and B when the load resistance is
  removed**.

### 2.13.1 The procedure ·J p18

$$\boxed{\;
\begin{aligned}
&\textbf{Step 1.}\ \ \text{Open } R_L,\ \text{short-circuit the source, look into A--B} \Rightarrow R_{Th}\\
&\textbf{Step 2.}\ \ \text{Restore the source, leave A--B open, find the voltage across them} \Rightarrow V_{Th}\\
&\textbf{Step 3.}\ \ \text{Reconnect } R_L \text{ to the series pair } (V_{Th},R_{Th}) \Rightarrow I_{RL}
\end{aligned}\;}$$

### 2.13.2 [ex] The general case, worked symbolically ·J p18–p19

**Statement.** Convert the circuit below to Thevenin's equivalent circuit. ·J p18

[fig ·J p18] **The network.** A rectangular outline. Left rail: a **circle** source labelled
$\mathbf{V_{s}}$. Top rail from the source: zig-zag $\mathbf{R_{1}}$, reaching a node from which a
vertical branch drops through zig-zag $\mathbf{R_{2}}$ to the bottom rail. Continuing right along
the top from the same node: zig-zag $\mathbf{R_{3}}$, reaching the top-right corner, from which
zig-zag $\mathbf{R_{L}}$ drops to the bottom rail. So $R_2$ shunts the mid-node, $R_3$ feeds the
load, and $R_L$ is the element to be removed.

**Step 1 — get $R_{Th}$.** *"Open $R_L$, short circuit the source and look into the network then get
$R_{Th}$."* ·J p18

[fig ·J p18] **The Step-1 circuit.** The same network with the source replaced by a **plain wire**
down the left rail, $R_L$ removed, and the two terminals now open: a small circle marked **A**
(with a **+** above it) at the right end of the top rail beyond $R_3$, and a small circle marked
**B** at the right end of the bottom rail. A bold arrow in the empty right-hand space points
**left**, into the network — the direction you are "looking in" from.

[eq: thevenin-resistance]

$$\boxed{\;R_t = R_{Th} = R_3 + \frac{R_1R_2}{R_1+R_2}\;}$$

> ⚠ VERIFY **JC2.14** ·J p18 (and ·J p12) — two rendering quirks of the notes' equation font, worth
> knowing before reading any equation in these pages. **(i)** The line above is set as
> "$R_t = R_{Th\underline{=}}R_3 + \dots$", with the second equals sign dropped to subscript level
> so that it looks like part of the symbol. **(ii)** Bold subscript **2** and **3** are nearly
> identical glyphs, so $V_{R3}$ on ·J p12 and $V_{R2}$ here both read as "$V_{Ra}$" at first glance;
> the context — which resistor the divider is across — is what settles it. Nothing computed changes.
> See `_verification-log.md`.

*[added] Read the topology off the figure: with the source shorted, $R_1$ runs from the mid-node to
the bottom rail, exactly as $R_2$ does, so the two are in **parallel**; $R_3$ carries that
combination out to terminal A, so it is in **series**. The product-over-sum form is the two-resistor
special case of [eq: parallel-resistance].*

**Step 2 — get $V_{Th}$.** ·J p18

[fig ·J p18] **The Step-2 circuit.** The source is back — a circle marked **DC** labelled
$\mathbf{V_{s}}$ on the left rail — $R_1$, $R_2$ and $R_3$ as before, and terminals **A** (with
**+**) and **B** still open, with the same leftward arrow beside them.

*"No current flow through terminals AB thus no current flow through $R_3$."* ·J p18

[eq: thevenin-voltage]

$$\boxed{\;V_{R2} = V_s\,\frac{R_2}{R_1+R_2} = V_{Th}\;}$$

*[added] The step the sentence compresses: with A–B open, $R_3$ carries **no current**, so it drops
**no voltage** ($V = IR = 0$). Terminal A therefore sits at exactly the potential of the $R_2$
node, and the circuit reduces to the plain $R_1$–$R_2$ voltage divider of [eq: voltage-divider].
This is why $R_3$ appears in $R_{Th}$ but **not** in $V_{Th}$ — a favourite exam trap.*

**Step 3 — reconnect the load.** ·J p19

[fig ·J p19] **The Thevenin equivalent, loaded.** Left branch: zig-zag $\mathbf{R_{Th}}$ above a
circle source $\mathbf{V_{Th}}$. Right branch: zig-zag $\mathbf{R_{L}}$. Top and bottom rails
close the loop.

[eq: thevenin-load-current]

$$\boxed{\;I_{RL} = \frac{V_{Th}}{R_{Th}+R_L}\;}$$

*[added] What the theorem buys you: once $V_{Th}$ and $R_{Th}$ are known, **any** value of $R_L$
costs one division. Sweeping a load across a network of six resistors otherwise means redoing the
whole reduction of §2.9 for every value.*

---

## 2.14 Norton's theorem ·J p19–p21

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_N$ | Norton current — the short-circuit current at A–B | A | 1.6 A in the example |
| $R_N$ | Norton resistance, $= R_{Th}$ | Ω | 16.67 Ω in the example |
| $I_t$ | total current drawn from the source with the load shorted | A | 2.4 A in the example |

[def] **Norton's theorem.** A complex network with several resistances and several voltage sources
can be converted to a **single current source $I_N$ in parallel with a single resistor $R_N$**.
·J p19

> ⚠ VERIFY **JC2.15** ·J p19 — the heading is printed **"NORTONS THEOREM"**, without the
> apostrophe (Thevenin's, two pages earlier, has one). Cosmetic only.
> See `_verification-log.md`.

[fig ·J p19] **Norton's theorem, before and after.** *Left:* the same **Complex Network** rectangle
as §2.13 with terminals **A** (upper) and **B** (lower) and a zig-zag $\mathbf{R_{L}}$ across them.
*Right:* the equivalent — a rectangular outline with **three** vertical branches: on the left a
**circle containing an upward arrowhead** labelled $\mathbf{I_{N}}$, in the middle a zig-zag
$\mathbf{R_{N}}$, on the right a zig-zag $\mathbf{R_{L}}$.

### 2.14.1 The procedure ·J p19–p20

$$\boxed{\;
\begin{aligned}
&\textbf{Step 1.}\ \ \textbf{Short } R_L\ \text{and calculate the current through the short} \Rightarrow I_N\\
&\textbf{Step 2.}\ \ \text{Open } R_L,\ \text{short the source, look in} \Rightarrow R_N \;(= R_{Th})\\
&\textbf{Step 3.}\ \ \text{Reconnect } R_L \text{ across } (I_N \parallel R_N),\ \text{divide the current} \Rightarrow I_{RL}
\end{aligned}\;}$$

[eq: norton-resistance] **Note the one thing that carries straight over from Thevenin:** ·J p19

$$\boxed{\;R_N = R_{Th}\;}$$

*[added] Step 1 is the **opposite** of the Thevenin step-2: Thevenin **opens** the load and reads a
voltage, Norton **shorts** the load and reads a current. Step 2 is identical in both theorems.*

### 2.14.2 [ex] The general case, worked symbolically ·J p19–p20

**Statement.** The same network as §2.13.2 — $V_s$, $R_1$ along the top, $R_2$ shunting the
mid-node, $R_3$ feeding the load $R_L$. ·J p19

[fig ·J p19] **The Step-1 circuit.** The network redrawn with **$R_L$ replaced by a plain wire**
(short-circuited). Three current arrows are marked: a solid arrowhead after $R_1$ labelled
$\mathbf{I_{t}}$, a downward arrowhead in the $R_2$ branch, and a solid arrowhead after $R_3$
labelled $\mathbf{I_{N}}$ — the current through the short.

With $R_L$ shorted, $R_3$ is thrown across $R_2$: ·J p19

$$R_t = R_1 + \frac{R_2R_3}{R_2+R_3}$$

$$I_t = \frac{V_s}{R_t}$$

> ⚠ ILLEGIBLE **JC2.16** ·J p20 — the top line of ·J p20 is **clipped by the page edge**; only the
> lower half of *"$R_t$"* survives. From the equation immediately below it — which begins
> $I_N = I_tR_2/(R_2+R_3) = V_sR_2/[R_t(R_2+R_3)]$ — the clipped line can only be
> $I_t = V_s/R_t$, and it is written that way above. A screenshot of the top 2 cm of ·J p20 would
> confirm it.

*"Using current divider theorem the value for $I_N$ can be calculated as shown below."* ·J p20

[derivation] [eq: current-divider] The short-circuit current is the fraction of $I_t$ that takes the
$R_3$ path rather than the $R_2$ path: ·J p20

$$I_N = \frac{I_tR_2}{R_2+R_3} = \frac{V_sR_2}{R_t\,(R_2+R_3)} = \frac{V_s}{R_1 + \dfrac{R_2R_3}{R_2+R_3}} \times \frac{R_2}{R_2+R_3}$$

[eq: norton-current] and clearing the compound fraction:

$$\boxed{\;I_N = \frac{V_sR_2}{R_1R_2 + R_1R_3 + R_2R_3}\;}$$

*[added] Verified algebraically. Writing $R_t = \dfrac{R_1(R_2+R_3)+R_2R_3}{R_2+R_3}$,*

$$I_N = \frac{V_s}{R_t}\cdot\frac{R_2}{R_2+R_3} = \frac{V_s(R_2+R_3)}{R_1(R_2+R_3)+R_2R_3}\cdot\frac{R_2}{R_2+R_3} = \frac{V_sR_2}{R_1R_2+R_1R_3+R_2R_3}\ \checkmark$$

*Note the denominator's pleasing symmetry — it is the sum of all three pairwise products, so it
cannot hide a slip: if your expansion is missing a term or has $R_1^2$ in it, it is wrong.*

***Watch the current-divider direction.*** *The branch that takes the larger share of the current is
the one with the **smaller** resistance, so the fraction multiplying $I_t$ carries the **other**
branch's resistance on top: $I_{R3} = I_t\,R_2/(R_2+R_3)$, not $R_3/(R_2+R_3)$. This is the mirror
image of the voltage divider, where the fraction carries its **own** resistance on top.*

**Step 2 — $R_N$.** ·J p20

[fig ·J p20] **The Step-2 circuit.** Identical to the Thevenin Step-1 figure: source replaced by a
wire, load removed, terminals **A** (with **+**) and **B** open, bold arrow pointing left into the
network.

$$R_N = R_{Th} = R_3 + \frac{R_1R_2}{R_1+R_2}$$

**Step 3 — reconnect the load.** ·J p20

[fig ·J p20] **The Norton equivalent, loaded.** A rectangular outline with three vertical branches:
circle-with-upward-arrowhead $\mathbf{I_{N}}$ on the left, zig-zag $\mathbf{R_{N}}$ in the middle,
zig-zag $\mathbf{R_{L}}$ on the right.

[eq: norton-load-current]

$$\boxed{\;I_{RL} = \frac{I_NR_N}{R_N+R_L}\;}$$

*[added] Same current-divider rule again, and the same warning: the numerator carries $R_N$ — the
resistance of the **other** branch — not $R_L$.*

### 2.14.3 [ex] Norton applied to a 40 V four-resistor network ·J p20–p21

**Statement.** Calculate the current passing through $R_4$ using Norton's theorem. ·J p20

[fig ·J p20] **The network.** A rectangular outline. Left rail: a **circle** source labelled
**40 v** (**+** upper, **−** lower). Top rail: zig-zag $\mathbf{R_{1} = 10\ \Omega}$ to a mid-node; from
that node a vertical zig-zag $\mathbf{R_{2} = 20\ \Omega}$ drops to the bottom rail; the top rail
continues through zig-zag $\mathbf{R_{3} = 10\ \Omega}$ to the top-right **terminal** (drawn as a small
open circle). The right branch, between the two open-circle terminals, carries zig-zag
$\mathbf{R_{4} = 10\ \Omega}$. The values are printed to the left of each vertical resistor and above
each horizontal one.

**Solution — Step 1: short-circuit $R_4$** ·J p20–p21

[fig ·J p21] **The Step-1 circuit.** The same network with the right-hand branch replaced by a
**plain wire**. Current arrows: solid arrowhead after $R_1$, downward arrowhead in the $R_2$ branch,
solid arrowhead after $R_3$.

$$R_t = 10 + \left(20 \parallel 10\right) = 10 + \frac{20\times10}{20+10} = 16.67\ \Omega$$

*(the page writes the parallel combination as "20//10"; $\parallel$ is used for it throughout this
file)*

$$I_t = \frac{V_s}{R_t} = \frac{40}{16.67} = 2.4\ \mathrm{A}$$

$$I_{R3} = I_N = \frac{I_tR_2}{R_2+R_3} = \frac{2.4\times20}{(20+10)} = \frac{48}{30} = 1.6\ \mathrm{A}$$

**Step 2: find $R_N$ — short-circuit the source** ·J p21

[fig ·J p21] **The Step-2 circuit.** $R_1$, $R_2$ and $R_3$ with the source replaced by a wire down
the left rail and the load branch open at two small circles; the bold arrow points left into the
network.

$$R_N = 10 + \frac{10\times20}{10+20} = 16.67\ \Omega$$

**Step 3: the final circuit** ·J p21

[fig ·J p21] **The Norton equivalent for this network.** Three vertical branches between two rails:
circle-with-upward-arrowhead labelled $\mathbf{I_{N} = 1.6\ \mathrm{A}}$, zig-zag
$\mathbf{R_{N} = 16.67\ \Omega}$, zig-zag $\mathbf{R_{4} = 10\ \Omega}$, the last pair between the two open
terminals.

$$\boxed{\;I_{R4} = \frac{1.6\times16.67}{10+16.67} = 1\ \mathrm{A}\;}$$

*[added] Every step verified, and the answer confirmed by two independent routes:*

| Step | Recomputed | Printed | ✓ |
|---|---|---|---|
| $R_2\parallel R_3$ | 6.6667 Ω | — | — |
| $R_t$ (load shorted) | 16.6667 Ω | 16.67 Ω | ✓ |
| $I_t$ | 2.4000 A | 2.4 A | ✓ |
| $I_N$ | 1.6000 A | 1.6 A | ✓ |
| $I_N$ from [eq: norton-current] | $\dfrac{40\times20}{200+100+200} = \dfrac{800}{500} = 1.6$ A | 1.6 A | ✓ |
| $R_N = R_3 + R_1\parallel R_2$ | 16.6667 Ω | 16.67 Ω | ✓ |
| $I_{R4}$ | 1.0000 A | 1 A | ✓ |

***Cross-check 1 — by Thevenin.** $V_{Th} = 40\times20/(10+20) = 26.67\ \mathrm{V}$,
$R_{Th} = 10 + 10\!\parallel\!20 = 16.67\ \Omega$, so*
$$I_{R4} = \frac{26.67}{16.67+10} = 1.00\ \mathrm{A} \quad\checkmark$$
*and note $V_{Th} = I_NR_N = 1.6\times16.67 = 26.67\ \mathrm{V}$ ✓ — the source transformation of
§2.12 in action.*

***Cross-check 2 — by plain series–parallel reduction, no theorem at all.** With $R_4$ in place,
$R_3+R_4 = 20\ \Omega$ sits across $R_2 = 20\ \Omega$, giving 10 Ω; plus $R_1$ gives 20 Ω total, so
$I_t = 40/20 = 2\ \mathrm{A}$, which splits equally between two 20 Ω paths:*
$$I_{R4} = 1.00\ \mathrm{A} \quad\checkmark$$

***Why $R_t$ and $R_N$ come out equal here (16.67 Ω both times) is a coincidence of the numbers**,
not a rule: $R_t = R_1 + R_2\!\parallel\!R_3$ with the load shorted, $R_N = R_3 + R_1\!\parallel\!R_2$
with the source shorted, and they agree only because $R_1 = R_3 = 10\ \Omega$. Do not carry one over
into the other in a problem where the two are different.*

---

## 2.15 Mesh analysis — a circuit with more than one voltage source ·J p22

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $I_1$ | current in the left branch, flowing **into** the top node | A | 0.4545 A |
| $I_2$ | current **down** through the middle branch | A | 1.273 A |
| $I_3$ | current in the right branch, flowing **into** the top node | A | 0.8182 A |

[fig ·J p22] **The general two-source circuit.** A rectangular outline divided into two windows by a
middle vertical branch. Left rail: circle source $\mathbf{V_{s}}$. Top-left: zig-zag
$\mathbf{R_{1}}$ with a solid arrowhead pointing **right**, labelled $\mathbf{I_{1}}$, arriving at
the top-middle node. Middle branch: zig-zag $\mathbf{R_{2}}$ with a solid arrowhead pointing
**down**, labelled $\mathbf{I_{2}}$, running from the top-middle node to the bottom rail.
Top-right: zig-zag $\mathbf{R_{3}}$ with a solid arrowhead pointing **left**, labelled
$\mathbf{I_{3}}$, arriving at the same top-middle node from the right. Right rail: a second circle
source $\mathbf{V_{s}}$. Both sources drive current **toward** the middle node; both branch
currents leave it downward through $R_2$.

### [ex] Two sources, three branches ·J p22

**Statement.** Calculate the values for $I_1$, $I_2$ and $I_3$ in the circuit shown. ·J p22

[fig ·J p22] **The worked circuit.** The same topology with values: left source **30 V**, top-left
resistor **10R**, middle resistor **20R**, top-right resistor **30R**, right source **50 V**. Two
curved arrows inside the windows mark the loops: **Loop 1** in the left window and **Loop 2** in the
right window, both drawn **clockwise**. $I_1$ points right into the node, $I_3$ points left into the
node, $I_2$ points down through the 20 Ω.

**Solution** (the page's own)

[eq: mesh-kvl] Taking each loop in turn: ·J p22

$$10I_1 + 20I_2 = 30$$

$$30I_3 + 20I_2 = 50$$

[eq: mesh-kcl] and at the top node

$$I_1 + I_3 = I_2$$

> ⚠ VERIFY **JC2.17** ·J p22 — the line introducing the two loop equations reads *"Using
> **Kirchoff's current law** the two loops have the following expressions"*. The two loop equations
> are **Kirchhoff's voltage law** (KVL) — sum of the $IR$ drops round a closed loop equals the emf
> in it. Kirchhoff's **current** law is the third line, $I_1 + I_3 = I_2$, at the node. The surname
> is also spelled **Kirchoff** for **Kirchhoff**. Nothing computed changes.
> See `_verification-log.md`.

**Substituting $I_2 = I_1 + I_3$ into both loop equations:** ·J p22

$$10I_1 + 20I_1 + 20I_3 = 30I_1 + 20I_3 = 30$$

$$30I_3 + 20I_1 + 20I_3 = 50I_3 + 20I_1 = 50$$

*"Simplifying and eliminating $I_3$ results in"* ·J p22

$$4I_1 + 10I_3 = 10$$

$$15I_1 + 10I_3 = 15$$

$$I_1 = 0.4545\ \mathrm{A},\quad I_2 = 1.273\ \mathrm{A},\quad I_3 = 0.8185\ \mathrm{A}$$

> ⚠ VERIFY **JC2.18** ·J p22 — the two lines are introduced as *"eliminating $I_3$"*, but $I_3$ is
> still in both of them. They are the previous pair **scaled**: $50I_3+20I_1 = 50$ divided by 5
> gives $4I_1+10I_3 = 10$, and $30I_1+20I_3 = 30$ divided by 2 gives $15I_1+10I_3 = 15$. The
> scaling is chosen so that **subtracting** them eliminates $I_3$ — which is the step the page
> performs silently. Nothing computed changes. See `_verification-log.md`.

> ⚠ VERIFY **JC2.19** ·J p22 — the printed $I_3 = 0.8185\ \mathrm{A}$ is a rounding slip. Exactly,
> $$I_3 = \frac{9}{11} = 0.8182\ \mathrm{A}$$
> The error is $3\times10^{-4}$ A and changes nothing, but it is worth knowing the exact values are
> elevenths. See `_verification-log.md`.

*[added] The elimination, done explicitly — this is the line the page leaves out:*

$$(15I_1 + 10I_3) - (4I_1 + 10I_3) = 15 - 10$$

$$11I_1 = 5 \qquad\Longrightarrow\qquad I_1 = \frac{5}{11} = 0.4545\ \mathrm{A}$$

$$10I_3 = 10 - 4(0.4545) = 8.1818 \qquad\Longrightarrow\qquad I_3 = \frac{9}{11} = 0.8182\ \mathrm{A}$$

$$I_2 = I_1 + I_3 = \frac{5}{11} + \frac{9}{11} = \frac{14}{11} = 1.2727\ \mathrm{A}$$

*[added] Substituted back into the original loop equations:*

$$10(0.4545) + 20(1.2727) = 4.545 + 25.455 = 30.000\ \mathrm{V} \quad\checkmark$$

$$30(0.8182) + 20(1.2727) = 24.545 + 25.455 = 50.000\ \mathrm{V} \quad\checkmark$$

*[added] The sign convention the page is using, since it never states it: **both** sources are taken
to drive current **into** the top node, and both branch currents leave it through $R_2$. That is why
the two loop equations both come out with **plus** signs on the $20I_2$ term, and why the node
equation is $I_1 + I_3 = I_2$ rather than a difference. If a problem draws a source the other way
round, one of those signs flips — write the current directions on the figure **before** writing any
equation.*

*[added] A quick plausibility check on the answer: the 50 V source pushes harder than the 30 V one,
so it should deliver more current — and $I_3 = 0.82\ \mathrm{A}$ against $I_1 = 0.45\ \mathrm{A}$ ✓.
The shared 20 Ω carries their sum, 1.27 A, and stands at $20\times1.2727 = 25.45\ \mathrm{V}$ —
between the two source voltages, as it must be.*

---

## 2.16 Factors considered when selecting a resistor ·J p22–p23

The notes give a plain list. ·J p22–p23

- **Resistance value**
- **Power rating**
- **Tolerance**
- **Accuracy**
- **Durability**
- **Stability**
- **Quality** *(the seventh bullet, carried over to the top of ·J p23)*

*[added] The list is short on definitions, and three of the seven are easily confused:*

| Factor | What it actually asks | Where it is fixed in these pages |
|---|---|---|
| **Tolerance** | how far the part may be from its marked value **when new** | the fourth colour band, §2.3 |
| **Accuracy** | how closely the marked value matches the value you need | your choice of nominal value |
| **Stability** | how far it **drifts** over time and temperature | §2.17 — precision vs general-purpose grades |
| **Power rating** | the dissipation it can stand without damage | §2.10 — and it is the factor most often forgotten |

---

## 2.17 Resistor types ·J p23–p24

[def] Resistors are broadly categorised as **fixed**, **variable** and **special-purpose**. ·J p23

### 2.17.1 Fixed resistors ·J p23

[def] **Fixed resistors** are those whose value **cannot be varied after manufacture**. They are
classified into **composition**, **wire-wound** and **metal-film** resistors. ·J p23

**Wire-wound resistors** ·J p23

- Made by **winding nickel-chromium alloy wire** on a **ceramic tube**, covered with a **vitreous
  coating**.
- The **spiral winding has inductive and capacitive characteristics**, which make it **unsuitable
  for operation above 50 kHz**.
- The frequency limit can be raised by **non-inductive winding**, so that the magnetic fields
  produced by the two parts of the winding **cancel**.

**Composition resistors** ·J p23

- **Carbon particles mixed with a binder**, moulded into a cylinder and hardened by **baking**.
- Leads attached **axially** at each end; the assembly is **encapsulated** in a protective coating.
- **Colour bands** on the outer surface give the value and tolerance (§2.3).
- **Economical**, and exhibit **low noise levels for resistances above 1 MΩ**.
- Usually rated for temperatures **around 70 °C**, for powers ranging from **1/8 W to 2 W**.
- Have **end-to-end shunted capacitance** that may be noticed at frequencies **around 100 kHz**,
  especially for resistance values **above 0.3 MΩ**.

> ⚠ VERIFY **JC2.20** ·J p23 — the two resistance values in the composition-resistor paragraph are
> printed **"1 MW"** and **"0.3 MW"**. They are **1 MΩ** and **0.3 MΩ**; the ohm symbol has been
> replaced by a **W** — the classic symbol-font substitution ($\Omega$ and W occupy the same slot in
> some legacy symbol fonts). A megawatt is not a resistance. Nothing computed changes.
> See `_verification-log.md`.

**Metal-film resistors** ·J p23

- Commonly made of **nichrome, tin-oxide or tantalum nitride**, either **hermetically sealed** or in
  **moulded-phenolic cases**.
- **Not as stable as wire-wound resistors.**

**The four grades of fixed resistor**, by application ·J p23

| Grade | Characteristics | Used for |
|---|---|---|
| **Precision** | low voltage and power coefficients; excellent temperature and time stabilities; low noise; very low reactance. Available in metal-film or wire construction | circuits needing very close resistance tolerances |
| **Semiprecision** | smaller than precision types; long-term temperature stability | current-limiting, voltage-dropping |
| **General-purpose** | initial resistance variation ≈ **5 %**; variation under full-rated power may approach **20 %**; high coefficient of resistance; high noise | circuits with no tight tolerance or long-term stability requirement |
| **Power** | available in wire-wound and film constructions; film types are stable at high frequencies and give higher resistance values than wire-wound for a given size | power supplies, control circuits, voltage dividers where **5 %** operational stability is acceptable |

> ⚠ VERIFY **JC2.21** ·J p23 — two words in this paragraph, *"time stabilities"*, are printed in
> **blue hyperlink colouring** — a web-copy artefact carried into the document (the same thing
> happens to *"doped"* on ·J p24). Text is fully readable; cosmetic only.
> See `_verification-log.md`.

### 2.17.2 Variable resistors ·J p23–p24

**Potentiometers** ·J p23–p24

- A **special form of variable resistor with three terminals**.
- **Two terminals connect to the opposite ends of the resistive element**; the **third** connects to
  a **movable contact**.
- The element is **usually circular**, with the movable contact attached to a **rotating shaft**.
- Manufactured as **carbon composition, metallic film and wire-wound** types, in **single-turn or
  multiturn** units.
- The movable contact **does not travel all the way to the end** of the resistive element: a small
  residual resistance, the **hop-off resistance**, is left in to **prevent accidental burning** of
  the element.

**Rheostat** ·J p24

- A **current-setting device**: **one** terminal connects to the resistive element and the **second**
  to a **movable contact**, so that a **selected section** of the element is placed **into the
  circuit**.
- Typically **wire-wound**.
- Used as **speed controls for motors**, in **ovens and heater controls**, and wherever adjustment of
  voltage and current levels is needed — **voltage dividers and bleeder circuits**.

*[added] The distinction in one line: a **potentiometer** is a three-terminal device used to divide a
**voltage**; a **rheostat** is the same element wired with two terminals to set a **current**.*

### 2.17.3 Special-purpose: integrated-circuit resistors ·J p24

[def] **Integrated-circuit resistors** fall into **two general categories**: ·J p24

1. **Semiconductor resistors** — use the **bulk resistivity of doped semiconductor regions** to
   obtain the desired resistance value. Four types: **diffused, bulk, pinched and ion-implanted**.
   - **Diffused** semiconductor resistors use the resistivity of a **diffused region** in the
     semiconductor substrate; **both n-type and p-type diffusions** are used.
2. **Deposited-film resistors** — formed by **depositing resistance films on an insulating
   substrate**, then **etching and patterning** them into the desired resistive network. By film
   thickness and dimensions they are classed as **thick-film** and **thin-film** resistors.

*[added] This is the one paragraph in these pages that connects forward: the same bulk-resistivity
idea, $R = \rho L/A$ from §2.2, is what sets sheet resistance in an integrated circuit — picked up
again in `05-fabrication-and-integrated-circuits`.*

> **Range note.** ·J p24 continues past this point into **CAPACITORS**, which belongs to the next
> topic file. Section 2.17 stops where that heading begins.

---

## 2.18 Formula summary — the whole file on one page

| Quantity | Formula | Source |
|---|---|---|
| Charge / current | $Q = It$, $I = Q/t$ | ·J p9–p10 |
| Power | $P = VI = I^{2}R = V^{2}/R$ | ·J p10, p12 |
| Resistivity | $R = \rho L/A$ | ·J p10 |
| Colour code | $R = (10d_1+d_2)\times10^{m} \pm T\%$ | ·J p11 |
| Tolerance range | $R(1-T) \le R \le R(1+T)$ | ·J p11 |
| Ohm's law | $I = V/R$, $V = IR$, $R = V/I$ | ·J p12 |
| Series — current | $I = I_{R1} = I_{R2} = I_{R3}$ | ·J p12 |
| Series — resistance | $R_t = R_1+R_2+R_3$ | ·J p12 |
| Voltage divider *[added]* | $V_{Rk} = V_s R_k/R_t$ | ·J p18 (used, not stated) |
| Parallel — voltage | $V_s = V_{R1} = V_{R2} = V_{R3}$ | ·J p13 |
| Parallel — resistance | $1/R_t = 1/R_1+1/R_2+1/R_3$ | ·J p13 |
| Two in parallel | $R_t = R_1R_2/(R_1+R_2)$ | ·J p18–p21 |
| Current divider | $I_{R3} = I_t R_2/(R_2+R_3)$ | ·J p20 |
| Source with internal resistance | $V_{RL} = V_s R_L/(R_i+R_L)$ | ·J p16 |
| Constant-voltage source | $R_i \ll R_L$ | ·J p16 |
| Constant-current source | $R_i \gg R_L$ | ·J p17 |
| Source transformation | $I_N = V_s/R_i$ | ·J p17 (garbled — **JV2.7**) |
| Impedance, polar | $Z = \sqrt{R^2+X^2}\,\angle\tan^{-1}(X/R)$ | ·J p16 (**JV2.5**) |
| Thevenin resistance | $R_{Th} = R_3 + R_1R_2/(R_1+R_2)$ | ·J p18 |
| Thevenin voltage | $V_{Th} = V_sR_2/(R_1+R_2)$ | ·J p18 |
| Thevenin load current | $I_{RL} = V_{Th}/(R_{Th}+R_L)$ | ·J p19 |
| Norton current | $I_N = V_sR_2/(R_1R_2+R_1R_3+R_2R_3)$ | ·J p20 |
| Norton resistance | $R_N = R_{Th}$ | ·J p19 |
| Norton load current | $I_{RL} = I_NR_N/(R_N+R_L)$ | ·J p20 |
| Mesh (KVL) | $10I_1+20I_2 = 30$, $30I_3+20I_2 = 50$ | ·J p22 |
| Node (KCL) | $I_1 + I_3 = I_2$ | ·J p22 |
| Power rating, $n$ identical parts | $n = P_{\text{total}}/P_{\text{one}}$; series $R = R_t/n$, parallel $R = nR_t$ | ·J p15 |

---

## 2.19 Triage — what to study, in what order

**Highest value — these are what a CAT lifts verbatim**

1. **§2.9, the six-resistor combined network.** A full page of the notes, worked in fourteen steps.
   Learn the *order* of the reduction and the back-substitution, not the numbers.
2. **§2.14.3, the 40 V Norton example.** The only fully worked network theorem in the notes, and the
   standard exam shape: short the load, find $I_N$, kill the source, find $R_N$, divide the current.
3. **§2.3, the colour code.** The table has to be known cold, and the four decode/encode exercises
   on ·J p11–p12 are exactly the form a question takes. Note **JV2.1** (a wrong multiplier colour)
   and **JV2.2** (the reversed reading) before you revise from the page.
4. **§2.6 and §2.8, series and parallel with the same three resistors.** Cheap marks, and the two
   examples together carry the "biggest dominates / smallest dominates" insight.

**Medium value**

5. **§2.13, Thevenin.** Stated and worked **symbolically only** — the notes give no numerical
   Thevenin example. Use the cross-check in §2.14.3, which works the same network both ways.
6. **§2.15, mesh analysis.** One example, cleanly solved; the risk in an exam is the sign
   convention, not the algebra.
7. **§2.10, power rating.** Short, and the "how many 2 W resistors" question is a standard one.
8. **§2.11–§2.12, the two source models.** Four small numerical cases; the ideas ($R_i \ll R_L$ vs
   $R_i \gg R_L$) matter more than the arithmetic and reappear in every amplifier topic.

**Lower value, but do not skip**

9. **§2.2, resistivity and the four factors.** One formula, occasionally asked as bookwork.
10. **§2.16–§2.17, choosing a resistor and resistor types.** Pure recall, and the only bookwork in
    these pages that cannot be re-derived. Worth one reading pass before the exam.

**Present in the notes but never assessed here**

- The impedance line $Z = R + jX$ on ·J p16 — introduced and never used again; everything in these
  pages is purely resistive. (It is also printed wrongly — **JV2.5**.)
- The temperature factor (d) in §2.2 — listed as a factor, with no coefficient given anywhere.
- The **5-band** colour code — stated in one sentence on ·J p11, never exercised.

---

## 2.20 Typography and notation slips, collected

> ⚠ VERIFY — the purely cosmetic defects of ·J p10–p23, gathered here because none of them changes
> anything computed. Listed so that a reader meeting them on the page knows they are the source's,
> not a misreading. Each is also flagged inline at the point of use.
>
> | ID | Page | Printed | Should read |
> |---|---|---|---|
> | **JC2.1** | ·J p10 | "which **apposes** the flow of current in **Q** circuit" | opposes … in **a** circuit |
> | **JC2.2** | ·J p10 | "Power … the **amount** of energy dissipated …" | the **rate**; the 1 A/1 V sentence defines the **watt** |
> | **JC2.3** | ·J p10 | "Voltage … is the **energy** which drives charge" | energy **per unit charge**, $V = W/Q$ (J/C) |
> | **JC2.4** | ·J p10 | "(b) Cross sectional Area $R \propto L/A$" | the area factor alone is $R \propto 1/A$ |
> | **JC2.5** | ·J p10 | proportionality typed as Greek **α**: "R α L" | $R \propto L$ — and α is the CB current gain elsewhere in BEE 3103 |
> | **JC2.6** | ·J p11 | table row "**No. band**" | **no band** (a three-band resistor), tolerance ±20 % |
> | **JC2.7** | ·J p11 | "4K54 … is **equivalent** to $4.5\times10^{3}$" | 4K54 = 4.54 kΩ; 4.5 kΩ is a **rounding** to two significant figures |
> | **JC2.8** | ·J p12 | the exercise stem truncated to "**left are.**" | the opening of the sentence is lost at the p11/p12 break; the reversal in both solutions implies "…from **right to** left are" (**JV2.2**) |
> | **JC2.9** | ·J p13 | parts lettered "(a) (b) (c) **(e)**"; part (c) answered with voltages | there is no (d); (c) asks for currents — all three are the same 27.0 µA |
> | **JC2.10** | ·J p13, p14, p15, p21 | decimal point set as a separate dot: "$\frac{200}{779}.022$", "$\frac{1}{62}.22$", "$\frac{50}{9}.39$", "$30.\frac{104}{20}$", "$\frac{40}{16}.67$" | $\frac{200}{779.022}$, $\frac{1}{62.22}$, $\frac{50}{9.39}$, $\frac{30.104}{20}$, $\frac{40}{16.67}$ |
> | **JC2.11** | ·J p14 | first line of part (d) clipped by the page edge | $I_{R1} = V_{R1}/R_1 = 200/900$ — result not recoverable from the render (⚠ ILLEGIBLE) |
> | **JC2.12** | ·J p14 | "(d) Voltage **through** each resistor" | voltage **across** each resistor (current is *through*, voltage is *across*) |
> | **JC2.13** | ·J p15 | "Wattage for one **reisistor**" (twice) | resistor |
> | **JC2.14** | ·J p12, p18 | bold subscript digits **2** and **3** render almost identically, so $V_{R3}$ reads as $V_{Ra}$; and "$R_t = R_{Th\underline{=}}R_3 + \dots$" sets the second equals sign at subscript level | $V_{R3}$; $R_t = R_{Th} = R_3 + \frac{R_1R_2}{R_1+R_2}$ |
> | **JC2.15** | ·J p19 | heading "**NORTONS THEOREM**" | Norton's theorem |
> | **JC2.16** | ·J p20 | first line clipped; only "$R_t$" survives | $I_t = V_s/R_t$ (⚠ ILLEGIBLE) |
> | **JC2.17** | ·J p22 | "Using **Kirchoff's current law** the two loops …" | Kirchhoff's **voltage** law for the loops; KCL is the node equation $I_1+I_3 = I_2$ |
> | **JC2.18** | ·J p22 | "Simplifying and **eliminating $I_3$**" | $I_3$ is still present; the two lines are the pair **scaled** so that subtracting them eliminates it |
> | **JC2.19** | ·J p22 | $I_3 = 0.8185$ A | $I_3 = 9/11 = 0.8182$ A |
> | **JC2.20** | ·J p23 | "1 **MW**", "0.3 **MW**" | 1 MΩ, 0.3 MΩ — the ohm symbol lost to a font substitution |
> | **JC2.21** | ·J p23 | "time stabilities" in **blue hyperlink colouring** (also "doped" on ·J p24) | a web-copy artefact; text readable |
>
> See `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
