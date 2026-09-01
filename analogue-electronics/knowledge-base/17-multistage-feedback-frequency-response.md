---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "17 — Multistage Amplifiers, Feedback and Frequency Response (supporting)"
source: "L7 — 'Lesson 7 Multistage Amplifier feedback and frequency response .pdf', 27 pp."
pages: "1-27"
tier: supporting
file_role: topic
subtopics:
  - "what a feedback amplifier is; positive versus negative feedback"
  - "the feedback equation A_f = A/(1 +/- beta A); loop gain, feedback factor, sacrifice factor"
  - "the beta clash: feedback fraction here, transistor current gain in Lesson 3"
  - "advantages of negative feedback; gain stability dA'/A'"
  - "reduction of harmonic distortion by the loop gain"
  - "feedback over several stages: per-stage loops versus one overall loop"
  - "increased bandwidth; f1' = f1/(1+beta A), f2' = f2(1+beta A); constant gain-bandwidth product"
  - "the four feedback topologies and their effect on Zi, Zo, bandwidth, distortion and noise"
  - "shunt-derived series-fed (voltage-series) feedback; current-series feedback; voltage-shunt; current-shunt"
  - "multistage amplifiers: overall gain as a product, overall dB gain as a sum"
  - "the four interstage couplings: RC, impedance, transformer, direct"
  - "impedance coupling and transformer coupling: advantages, disadvantages, frequency response"
  - "impedance matching with a coupling transformer; turns ratio from inductance"
  - "complementary-symmetry class-B, class-C and tuned amplifiers"
  - "distortion in amplifiers: non-linear versus linear, harmonic, intermodulation, frequency, phase"
  - "the decibel: 20 log for voltage/current, 10 log for power; zero reference levels; dBm"
  - "gain variation with frequency; half-power points, cut-off frequencies, bandwidth"
  - "causes of gain roll-off: series coupling/bypass capacitors low, shunt device/stray capacitances high"
  - "lower cut-off frequency of an RC-coupled stage from the resistance seen by each capacitor"
  - "Miller effect and the input capacitance of a CE stage; upper cut-off frequency"
  - "cut-off frequencies of n cascaded stages; bandwidth shrinkage"
  - "alpha and beta cut-off frequencies, f_T, and the gain-bandwidth product"
key_equations: [feedback-gain, feedback-gain-negative, feedback-gain-positive, high-loop-gain, sacrifice-factor, oscillation-condition, gain-stability, gain-stability-highloop, distortion-reduction, cascade-per-stage, cascade-overall, cascade-sensitivity-ratio, bandwidth-def, lower-cutoff-feedback, upper-cutoff-feedback, gbp-constant, rout-series, rin-series, beta-voltage-divider, beta-current-series, gain-current-series, beta-voltage-shunt, cascade-gain-product, cascade-gain-db, power-gain-db, one-db-ratio, dbm, half-power-voltage, half-power-power, lower-cutoff-rc, miller-capacitance, miller-input-capacitance-bjt, upper-cutoff-rc, cascade-lower-cutoff, cascade-upper-cutoff, alpha-cutoff, fbeta-ft, falpha-ft, gbp-ft]
prerequisites: ["03-bipolar-junction-transistor (beta as transistor current gain, r_e, h-parameters, CE stage, biasing)", "04-field-effect-transistors (small-signal gain of a single stage)"]
leads_to: ["oscillators (positive feedback, the beta A = 1 condition)", "operational amplifiers (the four feedback topologies applied to op-amps)"]
verification_flags: 48
tags: [feedback, negative-feedback, positive-feedback, loop-gain, sacrifice-factor, gain-stability, distortion, multistage, cascade, rc-coupling, impedance-coupling, transformer-coupling, direct-coupling, decibel, frequency-response, cut-off-frequency, bandwidth, half-power-point, miller-effect, gain-bandwidth-product, alpha-cutoff, beta-cutoff, ft]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·L7 pN = provenance (which PDF page of Lesson 7 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 07 — Multistage Amplifiers, Feedback and Frequency Response

Scope: the whole of L7, 27 PDF pages. Builds the feedback amplifier from first principles, derives
the closed-loop gain equation and everything that follows from it (gain stability, distortion
reduction, bandwidth extension), classifies the four feedback topologies, then turns to multistage
amplifiers and the four interstage couplings, and closes with the frequency-response material —
the decibel, the half-power points, the causes of roll-off, the Miller effect, cascade bandwidth
shrinkage and the transistor's own cut-off frequencies.

> ## ⚠ Read §7.2 before anything else in this file
>
> In this lesson **$\beta$ is the feedback fraction** — a dimensionless number, typically between
> $0.001$ and $0.2$. In **Lesson 3 it is the transistor's common-emitter current gain**, typically
> $50$–$300$. Both meanings appear **on the same printed page** here (·L7 p11: $\beta = 100$ beside
> the transistor and $\beta = 0.13$ for the divider). The source itself flags this in a footnote
> ·L7 p2. Getting them confused is the single most reliable way to produce a wrong answer in this
> topic.

---

## 7.1 What this document actually is ·L7 p1–p27

[def] L7 is **not a lecture handout**. It is a set of scanned pages from a printed
electrical-technology textbook, assembled out of chapter order. The pages carry their own printed
page numbers and their own section numbering (62.1, 61.9, 60.43, …), and those numbers are
what an exam question will quote.

**Citations in this file are the PDF page** (·L7 p7), because that is what the render filenames
and the page-image folder use. The table below maps PDF page → printed page → textbook section, so
either can be looked up.

[table] **Page map** ·L7 p1–p27

| PDF pp. | Printed pp. | Chapter | Textbook sections | Content |
|---|---|---|---|---|
| 1 | — | 62 | title page | "Feedback Amplifier" — learning objectives |
| 2–13 | 2344–2355 | 62 | 62.1 – 62.12 | feedback theory, the four topologies, Examples 62.1–62.16 |
| 14 | — | 61 | title page | "Multistage and Feedback Amplifiers" — learning objectives |
| 15–16 | 2316–2317 | 61 | 61.1 – 61.2 | cascading, dB addition, the four couplings |
| 17–19 | 2323–2325 | 61 | 61.6 – 61.10 | impedance and transformer coupling, Examples 61.5–61.6 |
| 20–21 | 2300–2301 | 60 | 60.27 – 60.31 | complementary symmetry, class C, tuned amplifier, distortion |
| 22–27 | 2307–2312 | 60 | 60.39 – 60.51 | decibels, frequency response, Miller effect, cut-off frequencies, Examples 60.20–60.23, Tutorial 60.1 |

### ⚠ Three page ranges are missing from the compilation

These are **gaps in the source PDF**, not gaps in this file's coverage. Nothing is invented to fill
them.

- **Printed 2318–2322** (§61.3–61.5, RC-coupled and impedance-coupled two-stage amplifiers,
  Examples 61.1–61.4). PDF p17 opens **mid-solution** of Example 61.4 — the fragment is transcribed
  in §7.17 and marked.
- **Printed 2302–2306** (§60.32–60.39, harmonic analysis of distortion, and the *definition* of the
  decibel). PDF p22 opens at point 2 of a numbered list about decibel properties.
- **Printed 2313 onwards** — PDF p27 ends **mid-question** at Tutorial Problem 60.1 Q7.

> ⚠ ILLEGIBLE ·L7 p17 — the statement and first half of the solution of **Example 61.4** are on
> printed page 2322, which is not in the PDF. Needs a screenshot of printed pp. 2318–2322 to
> complete §7.17.

> ⚠ ILLEGIBLE ·L7 p27 — **Tutorial Problem 60.1 Q7** is cut off after "…Calculate". Needs a
> screenshot of printed page 2313.

---

## 7.2 ⚠ The $\beta$ clash — this is the trap ·L7 p2, p11, p13

The source raises it itself, in a footnote at the bottom of the first content page:

> "It may please be noted that it is not the same as the $\beta$ of a transistor (Art. 57.9)"
> ·L7 p2

[table] **The two $\beta$'s**

| Symbol in context | Meaning | Units | Typical value | Where |
|---|---|---|---|---|
| $\beta$ (this lesson) | **feedback fraction** — the portion of the output fed back | dimensionless | $0.001$–$0.2$ | ·L7 p2 onwards |
| $\beta$ (Lesson 3) | **transistor CE current gain**, $I_C/I_B$ | dimensionless | $50$–$300$ | ·L7 p11, p13, p18, p24, p25 |

**How to tell them apart on sight.**

- A $\beta$ **next to a transistor symbol in a figure**, or multiplying a base current, or forming
  $\beta R_E$ or $\beta r_e$, is the **transistor** gain.
- A $\beta$ appearing inside $(1 + \beta A)$, or equal to a resistor **ratio** such as $R_E/R_C$ or
  $R_1/(R_1+R_2)$, is the **feedback fraction**.
- A **numerical** tell: feedback fractions are small (much less than 1); transistor $\beta$ is large.

**Worst offender.** Example 62.13 ·L7 p11 uses both in eight consecutive lines:

$$I_E = \beta I_B = 100 \times 10\ \mu\mathrm{A} = 1\ \mathrm{mA} \qquad (\beta = \text{transistor})$$

$$\beta = \frac{R_1}{R_1+R_2} = 0.13 \qquad (\beta = \text{feedback fraction})$$

[added] Where confusion is possible, this file writes the feedback fraction as $\beta$ and the
transistor gain as $\beta_{\text{tr}}$ or $h_{fe}$ **in commentary only** — the transcribed
equations keep the source's own symbols so the printed page stays recognisable.

**A third $\beta$** turns up at the end of the lesson: $f_\beta$, the **beta cut-off frequency**
·L7 p26. That subscript refers to the transistor gain, not the feedback fraction.

---

## 7.3 Feedback amplifiers — the idea ·L7 p2

[def] A **feedback amplifier** is one in which a fraction of the amplifier output is fed back to the
input circuit. This partial dependence of the output on itself is what allows the output to be
controlled. Every feedback amplifier has exactly two parts: **an amplifier** and **a feedback
circuit**. ·L7 p2

[def] **Positive feedback** ·L7 p2 — the fed-back voltage (or current) is applied so as to
**increase** the input, i.e. it is **in phase** with it. Also called *regenerative* or *direct*
feedback. It produces excessive distortion, so it is seldom used in amplifiers — but because it
increases the power of the original signal it is the basis of **oscillator** circuits.

[def] **Negative feedback** ·L7 p2 — the fed-back voltage (or current) is applied so as to
**reduce** the amplifier input, i.e. it is **$180^\circ$ out of phase** with it. Also called
*degenerative* or *inverse* feedback. This is the one used in amplifier circuits.

---

## 7.4 The feedback equation ·L7 p2–p3

**Symbols for this section** [table]

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_i$ | input signal voltage | V | mV |
| $V_o$ | output voltage, **no** feedback | V | 1–10 V |
| $V_o'$ | output voltage **with** feedback | V | 1–10 V |
| $A$ | open-loop voltage gain | dimensionless | $10^2$–$10^4$ |
| $A'$ (also written $A_f$) | closed-loop gain | dimensionless | $10$–$10^2$ |
| $\beta$ | **feedback fraction** | dimensionless | $0.001$–$0.2$ |
| $\beta A$ | feedback factor | dimensionless | $10$–$10^3$ |
| $1 \pm \beta A$ | loop gain | dimensionless | $>1$ for NFB |
| $S$ | sacrifice factor | dimensionless | $10$–$10^3$ |

[fig ·L7 p2, Fig. 62.1] The amplifier with no feedback: a plain rectangle labelled $A$, two input
terminals at the left carrying $V_i$, two output terminals at the right carrying $V_o$. Nothing
else. This fixes the definition

$$A = \frac{V_o}{V_i}$$

which the source calls the **open-loop gain**. ·L7 p2

[fig ·L7 p2, Fig. 62.2] The amplifier with feedback. A rectangle labelled "Amplifier $A$" sits
top-centre, $V_i$ entering at the left on two terminals, $V_o$ leaving at the right on two
terminals. Below it a smaller box labelled $\beta$ sits in a loop: a wire runs down from the
amplifier's output side, into the right-hand side of the $\beta$ box, out of its left-hand side and
back up to the amplifier's input side, where a magenta arrow labelled $\beta V_o$ points into the
input node. The whole lower loop is captioned "Feeback Loop".

> ⚠ VERIFY **C7.1** ·L7 p2 — Fig. 62.2's in-figure caption is printed "**Feeback** Loop"; it is
> **Feedback** Loop. Spelling only, and the figure is otherwise correct. See `_verification-log.md`.

### [derivation] Closing the loop ·L7 p2

A fraction $\beta$ of the output-with-feedback $V_o'$ is returned to the input, so the voltage
actually presented to the amplifier becomes $(V_i \pm \beta V_o')$ — plus if the returned signal is
in phase, minus if it is in antiphase. Taking the **positive** case first and amplifying it $A$
times:

$$A\,(V_i + \beta V_o') = V_o'$$

$$AV_i + A\beta V_o' = V_o'$$

$$V_o'\,(1 - \beta A) = A V_i$$

$$A' = \frac{V_o'}{V_i} = \frac{A}{1 - \beta A}$$

[eq: feedback-gain-positive] **Positive feedback** ·L7 p2

$$\boxed{\;A' = \frac{A}{1 - \beta A}\;}$$

[eq: feedback-gain-negative] **Negative feedback** — obtained by replacing $\beta$ with $-\beta$,
because the returned signal now subtracts: ·L7 p2

$$A' = \frac{A}{1 - (-\beta A)} = \boxed{\;\frac{A}{1 + \beta A}\;}$$

[eq: feedback-gain] **The two together.** The form worth memorising, with the sign convention
stated explicitly, is

$$\boxed{\;A_f = \frac{A}{1 \pm \beta A}\;}\qquad
\begin{cases}
\;+\; & \text{negative feedback} \;\Rightarrow\; A_f < A\\[2pt]
\;-\; & \text{positive feedback} \;\Rightarrow\; A_f > A
\end{cases}$$

[added] **The sign is the thing students get backwards.** The *plus* sign in the denominator is
*negative* feedback. Read it as: negative feedback makes the denominator bigger, so the gain gets
smaller. That is the whole content of the sign.

### The vocabulary ·L7 p2

| Term | Definition |
|---|---|
| **feedback factor** | the product $\beta A$ |
| **feedback ratio** | $\beta$ itself |
| **loop gain** | the expression $(1 \pm \beta A)$ |
| **closed-loop gain** | $A'$ — the gain once the loop is closed |
| **open-loop gain** | $A$ — the gain with the loop open |

[eq: sacrifice-factor] **Sacrifice factor** ·L7 p2

$$\boxed{\;S = \frac{A}{A'}\;}$$

It measures how much voltage gain was given up to buy the other improvements. For negative feedback
$S = 1 + \beta A$.

### (a) Negative feedback in numbers ·L7 p3

With $A = 90$ and $\beta = 1/10 = 0.1$:

$$A' = \frac{A}{1+\beta A} = \frac{90}{1 + 0.1 \times 90} = \frac{90}{10} = 9$$

Gain has fallen from 90 to 9 — hence *degenerative*. ·L7 p3

[eq: high-loop-gain] **The large-loop-gain limit.** When $|\beta A| \gg 1$: ·L7 p3

$$\boxed{\;A' \cong \frac{A}{\beta A} \cong \frac{1}{\beta}\;}$$

$A'$ then depends on $\beta$ **alone**. This is the whole reason negative feedback is used: $\beta$
is set by a resistor ratio, and resistors can be bought to close tolerance with near-zero
temperature coefficient, so the closed-loop gain becomes immune to temperature, device parameters,
supply voltage and component ageing. ·L7 p3

### (b) Positive feedback in numbers ·L7 p3

With $A = 90$ and $\beta = 1/100 = 0.01$:

$$A' = \frac{90}{1 - (0.01 \times 90)} = \frac{90}{0.1} = 900$$

[eq: oscillation-condition] **Condition for oscillation** ·L7 p3 — if $\beta A = 1$ the gain is
mathematically infinite, meaning output with no input. Electrically what happens is that the
amplifier **becomes an oscillator**, supplying its own input. The two necessary conditions are:

$$\boxed{\;\text{1. the feedback must be positive}\qquad\text{2. } \beta A = +1\;}$$

---

## 7.5 Advantages of negative feedback ·L7 p3

The numerous advantages outweigh the single disadvantage — reduced gain.

1. higher fidelity, i.e. more linear operation
2. highly stabilised gain
3. increased bandwidth, i.e. improved frequency response
4. less amplitude distortion
5. less harmonic distortion
6. less frequency distortion
7. less phase distortion
8. reduced noise
9. input and output impedances can be modified as desired

·L7 p3

---

## 7.6 Worked examples on the basic feedback equation ·L7 p3–p5

[ex 62.1 ·L7 p3–p4] *In the series–parallel (SP) feedback amplifier of Fig. 62.3, calculate*
*(a) open-loop gain, (b) gain of the feedback network, (c) closed-loop gain, (d) sacrifice factor $S$.*
(Applied Electronics-I, Punjab Univ. 1991)

[fig ·L7 p4, Fig. 62.3] A triangular amplifier symbol labelled $A$, its input terminal at the left
marked **1 mV**, its output at the right marked $V_o = 10\ \mathrm V$ (a red node dot sits on the
output line). Below the amplifier a rectangle labelled $\beta$ is driven from the output line; its
own output, marked **250 mV**, runs back to the amplifier's lower input terminal.

**(a)** 1 mV goes in, 10 V comes out:

$$A = \frac{10\ \mathrm V}{1\ \mathrm{mV}} = 10{,}000$$

**(b)** The feedback network is driven by the 10 V output and delivers 250 mV:

$$\beta = \frac{\text{output}}{\text{input}} = \frac{250\ \mathrm{mV}}{10\ \mathrm V} = 0.025$$

**(c)** As far as the *whole* feedback amplifier is concerned the input is
$(250 + 1) = 251\ \mathrm{mV}$ and the output is 10 V:

$$A' = \frac{10\ \mathrm V}{251\ \mathrm{mV}} = 39.84 \approx 40$$

> ⚠ VERIFY **C7.2** ·L7 p4 — printed as $A' = 10\ \mathrm{V}/251\ \mathbf{mA} = 40$. The 251 is a
> **voltage** (251 mV), as the line above it states. Unit typo only; the number 40 is right
> ($10/0.251 = 39.84$). See `_verification-log.md`.

**(d)** $\displaystyle S = \frac{A}{A'} = \frac{10{,}000}{40} = 250$

[added] Cross-check: $S$ should equal $1+\beta A = 1 + 0.025 \times 10{,}000 = 251$. The printed
250 is the same number to the rounding used. ✓

---

[ex 62.2 ·L7 p4] *Calculate the gain of a negative feedback amplifier whose gain without feedback is*
*1000 and $\beta = 1/10$. To what value should the input voltage be increased in order that the*
*output voltage with feedback equals the output voltage without feedback?*

**Solution as printed.** Since $|\beta A| \gg 1$,

$$A' \cong \frac{1}{\beta} \cong \frac{1}{1/10} = 10$$

$$V_i' = V_i(1+\beta A) = 50(1 + 0.04 \times 100) = 250\ \mathrm{mV}$$

> ⚠ VERIFY **V7.1** ·L7 p4 — the second line **is not this problem's**. It substitutes
> $\beta = 0.04$, $A = 100$, $V_i = 50$ mV — the data of **Example 62.3**, printed immediately
> below. This example's data are $A = 1000$, $\beta = 0.1$, and no $V_i$ is given at all. Correct
> working:
> $$1 + \beta A = 1 + 0.1 \times 1000 = 101 \quad\Longrightarrow\quad \boxed{\;V_i' = 101\,V_i\;}$$
> so the input must be raised **101-fold**, and a numerical answer is impossible without $V_i$.
> Check on the exact gain: $A' = 1000/101 = 9.90$, which the $1/\beta = 10$ approximation matches. See `_verification-log.md`.

[added] **Why $V_i' = V_i(1+\beta A)$.** Same output needs the same signal at the amplifier's own
input terminals. With feedback, the amplifier sees $V_i' - \beta V_o'$, so
$V_i' - \beta V_o' = V_i$, and with $V_o' = V_o = A V_i$ this gives
$V_i' = V_i(1 + \beta A)$. The input must be raised by exactly the loop gain.

---

[ex 62.3 ·L7 p4] *In a negative-feedback amplifier, $A = 100$, $\beta = 0.04$ and $V_i = 50$ mV. Find*
*(a) gain with feedback, (b) output voltage, (c) feedback factor, (d) feedback voltage.*
(Applied Electronics, AMIEE, London)

$$\textbf{(a)}\quad A' = \frac{A}{1+\beta A} = \frac{100}{1 + 0.04\times100} = \frac{100}{5} = 20$$

$$\textbf{(b)}\quad V_o' = A' V_i = 20 \times 50\ \mathrm{mV} = 1\ \mathrm V$$

$$\textbf{(c)}\quad \text{feedback factor} = \beta A = 0.04 \times 100 = 4$$

$$\textbf{(d)}\quad \text{feedback voltage} = \beta V_o' = 0.04 \times 1 = 0.04\ \mathrm V$$

[added] All four verified. ✓

---

[ex 62.4 ·L7 p4] *An amplifier having a gain of 500 without feedback has overall negative feedback*
*applied which reduces the gain to 100. Calculate the fraction of output voltage fed back. If due to*
*ageing of components the gain without feedback falls by 20%, calculate the percentage fall in gain*
*without feedback.* (Applied Electronics-II, Punjab Univ. 1993)

From $A' = A/(1+\beta A)$, rearranged as $1 + \beta A = A/A'$:

$$\beta = \frac{1}{A'} - \frac{1}{A} = \frac{1}{100} - \frac{1}{500} = 0.01 - 0.002 = 0.008$$

Gain without feedback after ageing $= 80\%$ of $500 = 400$:

$$A'_{\text{new}} = \frac{400}{1 + 0.008 \times 400} = \frac{400}{4.2} = 95.24$$

$$\text{fall} = 100 - 95.24 = 4.76 \quad\Longrightarrow\quad \frac{4.76}{100}\times100 = 4.76\%$$

> ⚠ VERIFY **V7.2** ·L7 p4 — the **question** asks for "the percentage fall in gain **without**
> feedback"; the solution computes the percentage fall in gain **with** feedback. Without feedback
> the fall is 20% by hypothesis — the question would be trivial. Correct wording: *percentage fall
> in gain with feedback*. See `_verification-log.md`.

> ⚠ VERIFY **C7.3** ·L7 p4 — printed $400/4.2 = 95.3$ and hence a fall of 4.7%. Exactly,
> $400/4.2 = 95.238$, giving 4.76%. Rounding only. See `_verification-log.md`.

[added] **The point of the example.** The open-loop gain moved 20%; the closed-loop gain moved
4.76%. The improvement factor is $20/4.76 = 4.2 = 1 + \beta A$ — exactly the loop gain, which is
what §7.7 proves in general.

---

[ex 62.5 ·L7 p5] *An amplifier with negative feedback has a voltage gain of 100. Without feedback an*
*input of 50 mV is required to produce a given output; with feedback the input must be 0.6 V for the*
*same output. Calculate the voltage gain without feedback and the feedback ratio.*
(Bangalore University 2001)

$$V_o' = A' V_i' = 100 \times 0.6 = 60\ \mathrm V$$

Since the two outputs must be equal, $60 = A \times 50\ \mathrm{mV}$:

$$A = \frac{60}{50\ \mathrm{mV}} = 1200$$

$$\beta = \frac{A - A'}{A A'} = \frac{1200 - 100}{1200 \times 100} = \frac{1100}{120{,}000} = 0.00917 \approx 0.009$$

[added] Verified: $1200/(1 + 0.00917\times1200) = 1200/12.0 = 100$ ✓. The relation
$\beta = (A-A')/AA'$ is just $\beta = 1/A' - 1/A$ from Example 62.4 put over a common denominator.

---

## 7.7 Gain stability ·L7 p5

[derivation] Start from the closed-loop gain and take natural logarithms: ·L7 p5

$$A' = \frac{A}{1+\beta A}$$

$$\log_e A' = \log_e A - \log_e(1+\beta A)$$

Differentiating both sides:

$$\frac{dA'}{A'} = \frac{dA}{A} - \frac{\beta\,dA}{1+\beta A}
= dA\left(\frac{1}{A} - \frac{\beta}{1+\beta A}\right)
= \frac{1}{1+\beta A}\cdot\frac{dA}{A}$$

[eq: gain-stability] **Fractional gain change with feedback** ·L7 p5

$$\boxed{\;\frac{dA'}{A'} = \frac{1}{1+\beta A}\cdot\frac{dA}{A}\;}$$

[eq: gain-stability-highloop] If $\beta A \gg 1$: ·L7 p5

$$\boxed{\;\frac{dA'}{A'} = \frac{1}{\beta A}\cdot\frac{dA}{A}\;}$$

[added] In words: **negative feedback divides any fractional drift in the open-loop gain by the loop
gain.** A 20% wander in $A$ becomes a $20/(1+\beta A)$ per-cent wander in $A'$.

[ex 62.6 ·L7 p5] *An amplifier has an open-loop gain of 400 and a feedback of 0.1. If the open-loop*
*gain changes by 20% due to temperature, find the percentage change in closed-loop gain.*
(Electronics-III, Bombay 1991)

$A = 400$, $\beta = 0.1$, $dA/A = 20\% = 0.2$:

$$\frac{dA'}{A'} = \frac{1}{\beta A}\cdot\frac{dA}{A} = \frac{1}{0.1 \times 400}\times 20\% = \frac{20\%}{40} = 0.5\%$$

The amplifier gain changes by 20%, the feedback gain by only 0.5% — an improvement of
$20/0.5 = 40$ times. ·L7 p5

[added] Verified. ✓ Note $40 = \beta A$, and the exact factor is $1+\beta A = 41$, so the exact
answer is $0.488\%$.

---

## 7.8 Decreased distortion ·L7 p5–p6

[derivation] Let the harmonic distortion voltage generated *inside* the amplifier change from $D$ to
$D'$ when negative feedback is applied. ·L7 p5

Suppose

$$D' = xD \tag{i}$$

The fraction of the output distortion voltage returned to the input is $\beta D' = \beta x D$. After
amplification this becomes $\beta x D A$, in antiphase with the original distortion $D$. Hence the
distortion that actually appears at the output is

$$D' = D - \beta x D A \tag{ii}$$

Equating (i) and (ii):

$$xD = D - \beta x D A$$

$$x(1 + \beta A) = 1 \quad\Longrightarrow\quad x = \frac{1}{1+\beta A}$$

[eq: distortion-reduction] Substituting back into (i): ·L7 p5–p6

$$\boxed{\;D' = \frac{D}{1+\beta A}\;}$$

> ⚠ VERIFY **C7.4** ·L7 p5 — printed "After amplification, it become $\beta x D_A$". The $A$ is a
> **factor**, not a subscript: the quantity is $\beta x D A$. A stray subscript in the typesetting;
> the next line uses it correctly. See `_verification-log.md`.

**Negative feedback reduces the amplifier's distortion by the loop gain**, i.e. by a factor
$(1+\beta A)$. ·L7 p6

[added] **The essential caveat, and it is examinable:** improvement is possible **only when the
distortion is produced by the amplifier itself** — not when it is already present in the input
signal. ·L7 p6 Feedback cannot remove what the source put in; it only suppresses what the amplifier
adds.

---

## 7.9 Feedback over several stages ·L7 p6–p7

**Symbols for this section** [table]

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $n$ | number of identical cascaded stages | — | 2–4 |
| $A$ | open-loop gain of **one** stage | dimensionless | 10–100 |
| $\beta_1$ | feedback ratio applied **per stage** | dimensionless | 0.01–0.2 |
| $\beta_2$ | feedback ratio of the **single overall** loop | dimensionless | $10^{-4}$–$10^{-2}$ |
| $A_1$ | overall gain, per-stage-feedback arrangement | dimensionless | — |
| $A_2$ | overall gain, single-overall-loop arrangement | dimensionless | — |

Multistage amplifiers exist to get more voltage gain, more current gain, or both. Given several
stages there is a **choice**: apply some feedback across *each* stage, or apply one loop across the
*whole* amplifier. ·L7 p6

[fig ·L7 p6, Fig. 62.4] Two block diagrams side by side on one pale-green panel.
**(a)** — the per-stage arrangement: two triangular amplifier blocks each labelled $A$, drawn left
and centre, joined by a dashed line labelled "n-stage" to indicate the omitted middle stages. Each
amplifier has its **own** feedback box labelled $\beta_1$ underneath it, wired from the amplifier's
output node back to its own input node (a small magenta arrowhead marks the return direction).
**(b)** — the overall-loop arrangement: two triangular blocks labelled $A$, again joined by a dashed
line for the omitted stages, with a **single** box labelled $\beta_2$ underneath spanning the whole
chain, wired from the last output back to the first input.

[eq: cascade-per-stage] **Overall gain, feedback round each stage** ·L7 p6

$$\boxed{\;A_1 = \left(\frac{A}{1 + A\beta_1}\right)^{\!n}\;}$$

[eq: cascade-overall] **Overall gain, one loop round everything** ·L7 p6

$$\boxed{\;A_2 = \frac{A^n}{1 + A^n\beta_2}\;}$$

> ⚠ VERIFY **V7.3** ·L7 p6 — equation (i) prints **both** results as $A_1$:
> "$A_1 = \left(\frac{A}{1+A\beta_1}\right)^n$ and $A_1 = \frac{A^n}{1+A^n\beta_2}$".
> The second is the *other* circuit's gain and must be $A_2$ — the text one line above defines
> $A_2$ as "the overall gain" of Fig. 62.4(b), and three lines below the page writes
> "$A_1 = A_2$", which is meaningless if both are already called $A_1$. Correct form:
> $$\boxed{\;A_2 = \frac{A^n}{1+A^n\beta_2}\;}$$
> See `_verification-log.md`.

Differentiating each: ·L7 p6

$$\frac{dA_1}{A_1} = \frac{n}{1+A\beta_1}\cdot\frac{dA}{A}
\qquad\text{and}\qquad
\frac{dA_2}{A_2} = \frac{n}{1+A^n\beta_2}\cdot\frac{dA}{A}$$

For the two circuits to deliver the **same** overall gain, set $A_1 = A_2$, which from the two gain
expressions requires

$$(1 + A\beta_1)^n = 1 + A^n\beta_2$$

> ⚠ VERIFY **V7.4** ·L7 p6 — printed as $(1 - 1\beta)^n = 1 + A^n\beta_2$. The left side is
> mangled twice: the sign is **minus** where it must be plus, and "$1\beta$" is a corrupted
> "$A\beta_1$". Correct form:
> $$\boxed{\;(1 + A\beta_1)^n = 1 + A^n\beta_2\;}$$
> One-line check: it is simply $A_1 = A_2$ with $A^n$ cancelled from both numerators. As printed
> the equality cannot even hold for $n=1$. See `_verification-log.md`.

[eq: cascade-sensitivity-ratio] Dividing the two fractional-change expressions and using that
condition: ·L7 p6

$$\boxed{\;\frac{dA_2/A_2}{dA_1/A_1} = \frac{1}{(1 + A\beta)^{\,n-1}}\;}$$

[added] Verified algebraically: the ratio is $(1+A\beta_1)/(1+A^n\beta_2)$, and substituting
$1+A^n\beta_2 = (1+A\beta_1)^n$ gives $(1+A\beta_1)^{1-n}$. ✓

**Reading the result** ·L7 p6

- $n = 1$ → denominator is unity, the two arrangements are equally stable, as expected.
- $n > 1$ with $(1+A\beta_1)$ large → $dA_2/A_2$ is **much smaller** than $dA_1/A_1$.

So **one overall loop stabilises the gain better than per-stage loops**, for the same overall gain.

---

### Worked examples on multistage feedback ·L7 p6–p8

[ex 62.7 ·L7 p6–p7] *An amplifier with 10% negative feedback has an open-loop gain of 50. If the*
*open-loop gain increases by 10%, what is the percentage change in the closed-loop gain?*
(Applied Electronics-I, Punjab Univ. 1991)

$$\textbf{(i)}\quad A_1' = \frac{A_1}{1+\beta A_1} = \frac{50}{1 + 0.1\times50} = \frac{50}{6} = 8.33$$

$$\textbf{(ii)}\quad A_2 = 50 + 0.1\times50 = 55 \quad\Longrightarrow\quad
A_2' = \frac{55}{1 + 0.1\times55} = \frac{55}{6.5} = 8.46$$

$$\text{percentage change} = \frac{A_2' - A_1'}{A_1'}\times100 = \frac{8.46 - 8.33}{8.33}\times100 = 1.56\%$$

[added] Verified: $8.4615$, $8.3333$, ratio $1.538\%$. Printed 1.56% comes from the rounded 8.46 and
8.33. ✓ A 10% open-loop change became a 1.5% closed-loop change — the loop gain here is only 6, so
the improvement is modest.

---

[ex 62.8 ·L7 p7] *Write down formulae for (i) gain (ii) harmonic distortion of a negative feedback*
*amplifier in terms of gain and distortion without feedback and the feedback factor. If gain without*
*feedback is 36 dB and harmonic distortion at normal output is 10%, what is (a) gain and*
*(b) distortion when negative feedback is applied, the feedback factor being 16 dB?*
(Electronic Engg. II, Warangal 1991)

The two formulae are §7.4 and §7.8:

$$A_f = A' = \frac{A}{1+\beta A} \qquad\qquad D' = \frac{D}{1+\beta A}$$

Converting the decibel figures — **voltage gain, so $20\log$**: ·L7 p7

$$36 = 20\log_{10}A \quad\Longrightarrow\quad A = 10^{1.8} = 63$$

$$16 = 20\log_{10}\beta A \quad\Longrightarrow\quad \beta A = 10^{0.8} = 6.3$$

$$\textbf{(a)}\quad A_f = \frac{63}{1+6.3} = \frac{63}{7.3} = 8.63 \quad\text{or}\quad 18.72\ \mathrm{dB}$$

> ⚠ VERIFY **V7.5** ·L7 p7 — printed as "$A_f = A/(1+\beta A) = 63/(1+6.3) =$ **6.63** or
> **18.72 dB**". $63/7.3 = 8.63$, not 6.63. The page's *own* decibel answer proves it:
> $20\log_{10}8.63 = 18.72$ dB, whereas $20\log_{10}6.63 = 16.43$ dB. Correct form:
> $$\boxed{\;A_f = \frac{63}{7.3} = 8.63 \equiv 18.72\ \mathrm{dB}\;}$$
> Second check: in decibels the closed-loop gain is simply $36 - 20\log_{10}(7.3) = 36 - 17.27 = 18.73$ dB. See `_verification-log.md`.

$$\textbf{(b)}\quad D' = \frac{10\%}{1+6.3} = 1.37\% \approx 1.4\ \text{per cent}$$

[added] Verified: $10/7.3 = 1.3699$. ✓

[added] **The dB rule this example turns on.** $\beta A$ is a *ratio of two voltages*, so it
converts with $20\log$, exactly like the gain. Using $10\log$ here would give $\beta A = 39.8$ and
a completely different answer. See §7.24 for when $10\log$ is the right choice.

---

[ex 62.9 ·L7 p7] *The overall gain of a two-stage amplifier is 150. The second stage has 10% of the*
*output voltage as negative feedback and has $-150$ as forward gain. Calculate (a) gain of the first*
*stage (b) the second harmonic distortion, if the second stage introduces 5% second harmonic without*
*feedback. Assume the first stage introduces no distortion.* (Electronics-II, Madras Univ. 1992)

For the second stage, $\beta = 0.1$, $A_2 = 150$, so $\beta A_2 = 15$:

**Second harmonic distortion**

$$D_2' = \frac{D_2}{1+\beta A_2} = \frac{0.05}{1 + 150\times0.1} = \frac{0.05}{16} = 0.003125 = 0.31\%$$

**Gain of the first stage**

$$A_2' = \frac{A_2}{1+\beta A_2} = \frac{150}{1 + 150\times0.1} = \frac{150}{16} = 9.38$$

$$A_1 \times A_2' = 150 \quad\Longrightarrow\quad A_1 = \frac{150}{9.38} = 16$$

[added] Verified: $0.05/16 = 0.3125\%$; $150/16 = 9.375$; $150/9.375 = 16.0$. ✓

> ⚠ VERIFY **C7.5** ·L7 p7 — the solution's **part labels are swapped** relative to the question.
> The question asks (a) gain of the first stage, (b) the second harmonic distortion; the solution
> labels the distortion "(a)" and the gain "(b)". Both answers are correct — only the labels are
> transposed. See `_verification-log.md`.

> ⚠ VERIFY **C7.6** ·L7 p7 — the statement gives the second stage's forward gain as **$-150$**;
> the solution uses $+150$ throughout. This is defensible — the minus sign is the CE stage's
> phase inversion, which is *what makes the feedback negative*, and the $(1+\beta A)$ form already
> assumes it — but the printed page never says so. Working with the signed value in
> $A/(1-\beta A)$ would give $150/(1+15)$, the same 9.38. See `_verification-log.md`.

---

[ex 62.10 ·L7 p7–p8] *Determine the effective gain of a feedback amplifier having an amplification*
*without feedback of $(-200 - j300)$ if the feedback circuit adds to the input signal a p.d. which is*
*0.5 per cent of the output p.d. and lags a quarter of a cycle behind it in phase. Explain whether*
*the feedback is positive or negative.* (Applied Electronics-II, Punjab Univ. 1992)

$$A = -200 - j300 = 360\angle{-123.7^\circ}$$

The feedback voltage $V_\beta$ is 0.5% of the output and lags it by $90^\circ$:

$$V_\beta = \left(\frac{0.5}{100}\angle{-90^\circ}\right)V_o
\quad\Longrightarrow\quad
\beta = \frac{V_\beta}{V_o} = 0.005\angle{-90^\circ} = -j\,0.005$$

$$\beta A = (-200 - j300)(-j\,0.005) = j\,1.0 + j^2 1.5 = -1.5 + j\,1.0$$

Because the feedback network **adds** to the input, the positive-feedback form applies:

$$A' = \frac{A}{1-\beta A} = \frac{360\angle{-123.7^\circ}}{1-(-1.5+j1.0)}
= \frac{360\angle{-123.7^\circ}}{2.69\angle{-21.8^\circ}} = 134\angle{-102^\circ}$$

**Verdict.** Both the magnitude and the phase shift have been **reduced** by the feedback, so the
feedback is **negative**. ·L7 p8

[added] All complex arithmetic verified: $|A| = 360.55$, $\angle A = -123.69^\circ$;
$1-\beta A = 2.5 - j1.0$, modulus $2.6926$, angle $-21.80^\circ$; $A' = 133.9\angle{-101.89^\circ}$. ✓

[added] **The lesson of this example.** "Negative feedback" is not a matter of which sign is written
in the denominator — it is a matter of whether the loop gain **reduces** the closed-loop gain. With
a complex $\beta A$ the classification has to be made from the answer, not the algebra.

---

[ex 62.11 ·L7 p8] *An amplifier has a gain of 100 and 5 per cent distortion with an input signal of*
*1 V. Calculate (i) output signal voltage, (ii) distortion voltage, (iii) output voltage.*

$$\textbf{(i)}\quad V_{os} = A V_i = 100 \times 1 = 100\ \mathrm V$$

$$\textbf{(ii)}\quad \text{distortion voltage} = D\,V_o = 0.05 \times 100 = 5\ \mathrm V$$

$$\textbf{(iii)}\quad V_o = V_{os} + D = 100 + 5 = 105\ \mathrm V$$

[added] Verified. ✓ Note the example uses no feedback at all — it is there to fix what "5 per cent
distortion" means numerically before the feedback formula is applied to it.

---

## 7.10 Increased bandwidth ·L7 p8–p9

**Symbols for this section** [table]

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $f_1$ | lower 3 dB (cut-off) frequency, no feedback | Hz | 20 Hz – 1 kHz |
| $f_2$ | upper 3 dB frequency, no feedback | Hz | 10 kHz – 1 MHz |
| $f_1'$, $f_2'$ | the same **with** feedback | Hz | — |
| $BW$ | bandwidth $= f_2 - f_1$ | Hz | — |
| $BW'$ | bandwidth with feedback | Hz | — |
| $A\times BW$ | gain–bandwidth product | Hz | constant |

[eq: bandwidth-def] ·L7 p8

$$\boxed{\;BW = f_2 - f_1\;}$$

The argument is short and worth reproducing exactly: negative feedback **reduces the gain**; the
**gain–bandwidth product must stay the same**; therefore the **bandwidth must increase** to
compensate. ·L7 p8

[eq: lower-cutoff-feedback] [eq: upper-cutoff-feedback] ·L7 p8

$$\boxed{\;f_1' = \frac{f_1}{1+\beta A}\qquad\text{and}\qquad f_2' = f_2\,(1+\beta A)\;}$$

The lower corner moves **down**, the upper corner moves **up**, both by the loop gain — a wider
separation at both ends.

[fig ·L7 p8, Fig. 62.5] Gain (vertical axis, labelled "Gain" with an upward magenta arrow) against
frequency (horizontal axis, unlabelled, origin marked 0). **Two** magenta band-pass curves are
drawn on the same axes:

- the **upper, taller, narrower** curve is the amplifier without feedback. Its flat top sits at the
  level marked **A** on the vertical axis (a dashed horizontal line runs from the axis label to the
  curve). Dashed vertical lines drop from its two shoulders to the frequency axis at $f_1$ and $f_2$.
- the **lower, shorter, wider** curve is the amplifier with feedback. Its flat top sits at the lower
  level marked **A′**. Dashed verticals drop from its shoulders to $f_1'$ and $f_2'$.

Along the frequency axis, left to right, the tick labels read $0$, $f_1'$, $f_1$, $f_2$, $f_2'$ —
so $f_1' < f_1$ and $f_2' > f_2$, which is the whole point of the figure. Below the axis, two
double-headed magenta arrows: the shorter, labelled **BW**, spans $f_1$ to $f_2$; the longer,
labelled **BW′**, spans $f_1'$ to $f_2'$.

[eq: gbp-constant] **Constancy of the gain–bandwidth product** ·L7 p8

$$\boxed{\;A \times BW = A' \times BW' \quad\Longleftrightarrow\quad A\,(f_2 - f_1) = A'\,(f_2' - f_1')\;}$$

> ⚠ VERIFY **V7.6** ·L7 p8 — printed as $A(f_2 - f_1') = A(f_2' - f_1')$. **Two** errors on one
> line: the left bracket should contain $f_1$, not $f_1'$ (it is the *no-feedback* bandwidth); and
> the right-hand gain should be $A'$, not $A$. As printed the equation says
> $A\times BW = A\times BW'$, which forces $BW = BW'$ — the exact opposite of the section's claim.
> Correct form:
> $$\boxed{\;A\,(f_2-f_1) = A'\,(f_2'-f_1')\;}$$
> See `_verification-log.md`.

[added] **Proof in one line.** Substituting the two corner-frequency results:

$$A'(f_2'-f_1') = \frac{A}{1+\beta A}\left[f_2(1+\beta A) - \frac{f_1}{1+\beta A}\right]$$

$$= A f_2 - \frac{A f_1}{(1+\beta A)^2}$$

For $f_2 \gg f_1$ — always true in an audio amplifier — this is $A f_2 \approx A(f_2-f_1)$. So the
product is constant to the same approximation the textbook uses in Example 62.12.

---

[ex 62.12 ·L7 p8–p9] *An RC-coupled amplifier has a mid-frequency gain of 200 and a frequency*
*response from 100 Hz to 20 kHz. A negative feedback network with $\beta = 0.02$ is incorporated.*
*Determine the new system performance.* (Electronic Circuits, Mysore Univ. 1990)

Loop gain first: $1 + \beta A = 1 + 0.02\times200 = 5$.

$$A' = \frac{A}{1+\beta A} = \frac{200}{5} = 40$$

$$f_1' = \frac{f_1}{1+\beta A} = \frac{100\ \mathrm{Hz}}{5} = 20\ \mathrm{Hz}$$

$$f_2' = f_2\,(1+\beta A) = 20\ \mathrm{kHz}\times5 = 100\ \mathrm{kHz}$$

$$BW' = f_2' - f_1' \cong 100\ \mathrm{kHz}$$

**Check on the gain–bandwidth product** ·L7 p9

$$BW = f_2 - f_1 \cong 20\ \mathrm{kHz}$$

$$A \times BW = 200 \times 20 = 4000\ \mathrm{kHz}$$

$$A' \times BW' = 40 \times 100 = 4000\ \mathrm{kHz}$$

As expected, the two are equal. ·L7 p9

> ⚠ VERIFY **C7.7** ·L7 p8 — printed "$A' = \frac{200}{1+0.02\times200} =$ **40 Hz**". A voltage
> gain is a pure number; the "Hz" is spurious, imported from the two lines of frequency working
> that follow. See `_verification-log.md`.

> ⚠ VERIFY **V7.7** ·L7 p9 — printed "$f_2' = f_0(1+\beta A) = 20(1+0.02\times200) =$ **100 Hz**".
> Two faults: the subscript should be $f_2$ (there is no $f_0$ in this problem), and the unit must
> be **kHz** — $f_2$ is 20 **kHz**, so $f_2' = 100$ kHz. The very next line, and the
> gain–bandwidth check below it, both use 100 kHz. Correct form:
> $$\boxed{\;f_2' = f_2(1+\beta A) = 20\ \mathrm{kHz}\times5 = 100\ \mathrm{kHz}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C7.8** ·L7 p9 — the bandwidth is written **$dW$** and **$dW'$** throughout this
> example. $dW$ is not a bandwidth symbol anywhere else in the chapter (§60.42 uses $\Delta f$ or
> $BW$). Read every $dW$ as $BW$. See `_verification-log.md`.

---

## 7.11 The four forms of negative feedback ·L7 p9–p10

This is the section most likely to appear as a bookwork question, and the summary table is the part
to memorise.

[def] The classification has **two independent binary choices**:

1. **What is sampled at the output** — the output **voltage**, or the output **current**.
2. **How it is returned at the input** — in **series** with the input, or in **shunt** (parallel).

That gives four combinations. The naming convention in this source is *(sampled quantity)–(return
connection)*: **voltage-series**, **voltage-shunt**, **current-series**, **current-shunt**. ·L7 p9

[fig ·L7 p9, Fig. 62.6] Four block diagrams stacked vertically on one panel, lettered (a) to (d) in
the left margin. Every one has the same skeleton: a large pale-yellow rectangle labelled $A$ in the
centre; two input terminals (small open circles) at the left carrying $V_i$; at the right, an output
node driving a zig-zag load resistor $R_L$ with the voltage across it labelled $V_o$; and a small
box labelled $\beta$ below the amplifier, wired between the output side and the input side. The
differences are exactly the connection points:

- **(a) Voltage-series.** The $\beta$ box's input taps the output **across** $R_L$ (parallel with
  the load), and its output returns **in series** with the lower input terminal. No solid junction
  dots at the input.
- **(b) Voltage-shunt.** Solid magenta junction dots appear at **both** the upper input terminal and
  the output node, and again at the lower input line — the $\beta$ box shunts the output *and*
  shunts the input.
- **(c) Current-series.** The output side has a **series** sensing path: below the $R_L$ branch a
  vertical wire carries a downward magenta arrowhead labelled $I_o$, and a second magenta arrowhead
  points up into the $\beta$ box's input. So the feedback network is driven by the output
  **current**; its output returns in series with the input.
- **(d) Current-shunt.** Same series current sensing on the output side as (c) — the $I_o$ arrow and
  the upward arrowhead into $\beta$ — but the return is **shunted** across the input, marked by
  solid junction dots on the input lines.

### (a) Voltage-series feedback ·L7 p9

Also called **shunt-derived series-fed** feedback; the amplifier and feedback circuit are connected
**series–parallel (SP)**.

A fraction of the output **voltage** is applied **in series** with the input voltage. The feedback
network's input is in **parallel** with the amplifier output, so as far as $V_o$ is concerned the
amplifier's output resistance is **reduced** by that shunting:

[eq: rout-series] ·L7 p9

$$\boxed{\;R_o' = \frac{R_o}{1+\beta A}\;}$$

At the input, $V_i$ sees two elements **in series** — (i) the input resistance of the amplifier and
(ii) the output resistance of the feedback network — so the input resistance is **increased**:

[eq: rin-series] ·L7 p9

$$\boxed{\;R_i' = R_i\,(1+\beta A)\;}$$

**Series feedback always increases the input impedance by a factor $(1+\beta A)$.** ·L7 p9

### (b) Voltage-shunt feedback ·L7 p9–p10

Also called **shunt-derived shunt-fed** feedback — a **parallel–parallel (PP)** prototype. A small
portion of the output voltage is coupled back in **parallel** with the input.

Because the feedback network shunts **both** the output and the input, it **decreases both**
impedances by the factor $1/(1+\beta A)$. ·L7 p10

**A shunt feedback always decreases input impedance.** ·L7 p10

### (c) Current-series feedback ·L7 p10

Also called **series-derived series-fed** feedback — a **series–series (SS)** circuit. Part of the
output **current** produces a proportional voltage fed back **in series** with the input. Series
pick-up and series feedback, so **both** input and output impedances are **increased**. ·L7 p10

### (d) Current-shunt feedback ·L7 p10

Also called **series-derived shunt-fed** feedback — a **parallel–series (PS)** prototype. The
feedback network picks up part of the output current and develops a feedback voltage in **parallel**
with the input. It shunts the input but is in series with the output, so the **output resistance is
increased** and the **input resistance is decreased** by the loop gain. ·L7 p10

### [table] Effects of negative feedback on amplifier characteristics ·L7 p10

| Characteristic | Voltage series | Voltage shunt | Current series | Current shunt |
|---|---|---|---|---|
| **Voltage gain** | decreases | decreases | decreases | decreases |
| **Bandwidth** | increases | increases | increases | increases |
| **Harmonic distortion** | decreases | decreases | decreases | decreases |
| **Noise** | decreases | decreases | decreases | decreases |
| **Input resistance** | **increases** | **decreases** | **increases** | **decreases** |
| **Output resistance** | **decreases** | **decreases** | **increases** | **increases** |

[added] **How to reconstruct this table under exam pressure without memorising 24 cells.** The
first four rows are all the same in all four columns — negative feedback always costs gain and
always buys bandwidth, linearity and noise. Only the last two rows differ, and each follows from
one word in the topology's name:

- **Input resistance** follows the **return** connection: *series* → up, *shunt* → down.
- **Output resistance** follows the **sampled** quantity: *voltage* sampled → down, *current*
  sampled → up.

A one-line mnemonic: **sample voltage, stabilise voltage → low $Z_o$; sample current, stabilise
current → high $Z_o$.** The same logic gives the input side: **series in → high $Z_i$; shunt in →
low $Z_i$.**

---

## 7.12 Shunt-derived series-fed voltage feedback ·L7 p10–p11

[fig ·L7 p10, Fig. 62.7] A pale-green panel. At the left, a magenta sine wave with $+$ above and
$-$ below marks the input; two terminals carry $V_i$ into a pale-yellow amplifier block $A$; a
second sine wave at the far right, **inverted relative to the input**, marks $V_o$ with $-$ above
and $+$ below (the $180^\circ$ inversion). Below the input line a second pair of terminals is
labelled $V_f$ with $-$ and $+$ signs. The feedback loop, captioned "Feedback Loop" at the lower
left, is a **two-resistor divider drawn vertically**: $R_1$ on top of $R_2$, connected across the
output, with the tapping point between them returned to the $V_f$ terminals. Solid magenta dots
mark the junctions on the output side.

The feedback voltage is the drop across $R_1$:

[eq: beta-voltage-divider] ·L7 p10

$$\boxed{\;V_f = V_o\,\frac{R_1}{R_1+R_2} = \beta V_o \quad\Longrightarrow\quad \beta = \frac{R_1}{R_1+R_2}\;}$$

---

[ex 62.13 ·L7 p10–p11] *In the voltage-controlled negative feedback amplifier of Fig. 62.8,*
*calculate (a) voltage gain without feedback (b) feedback factor (c) voltage gain with feedback.*
*Neglect $V_{BE}$ and use $r_e = 25\ \mathrm{mV}/I_E$.*

[fig ·L7 p11, Fig. 62.8] A single NPN common-emitter stage, emitter grounded. A supply rail across
the top is marked **15 V** at an open terminal on the right. **$R_1 = 1.5\ \mathrm{M}$** hangs from
that rail down to the base node — this is the base-bias resistor. From the base node a horizontal
line runs right through **$R_2 = 10\ \mathrm{M}$** and then through a coupling capacitor **$C$** to
the collector node. **$R_3 = 10\ \mathrm{K}$** hangs from the 15 V rail down to that same collector
node, and the output terminal (open circle) is taken from it. The input terminal (open circle) is on
the base line at the left. The transistor is annotated **$\beta = 100$** at its right, with a second
$\beta$ label pointing at the emitter arrow. So $R_2$ (with $C$) is the collector-to-base feedback
path and $R_1$ is the other arm of the divider, exactly as §7.12 requires.

**(a) Gain without feedback**

$$A = \frac{r_L}{r_e} = \frac{R_3}{r_e}$$

$$I_B = \frac{15\ \mathrm V}{1.5\ \mathrm M\Omega} = 10\ \mu\mathrm A$$

$$I_E = \beta_{\text{tr}} I_B = 100 \times 10\ \mu\mathrm A = 1\ \mathrm{mA}$$

$$r_e = \frac{25\ \mathrm{mV}}{1\ \mathrm{mA}} = 25\ \Omega$$

$$A = \frac{10\ \mathrm{k}\Omega}{25\ \Omega} = 400$$

**(b) Feedback factor**

$$\beta = \frac{R_1}{R_1+R_2} = \frac{1.5\times10^6}{(1.5+10)\times10^6} = 0.13$$

$$\beta A = 0.13 \times 400 = 52$$

**(c) Gain with feedback**

$$A' = \frac{A}{1+\beta A} = \frac{400}{1+52} = 7.55$$

[added] Verified. Exactly, $\beta = 1.5/11.5 = 0.13043$, $\beta A = 52.17$, $A' = 7.52$; with the
printed rounded $\beta = 0.13$ the answer is $400/53 = 7.547 \approx 7.55$. ✓

[added] ⚠ **This is the page where the two $\beta$'s collide.** Line 2 of part (a) uses
$\beta = 100$ (transistor); line 1 of part (b) uses $\beta = 0.13$ (feedback fraction). See §7.2.

---

## 7.13 Current-series feedback amplifier ·L7 p11–p12

[fig ·L7 p11, Fig. 62.9] A single CE stage drawn against the $V_{CC}$ rail. $R_B$ runs from the rail
to the base; $R_C$ runs from the rail to the collector; the output $V_o$ leaves the collector
through a coupling capacitor. The input $V_i$ (marked with $+$ at the top and $-$ at the bottom,
with a magenta arrow spanning them) enters through a coupling capacitor to the base. The emitter
goes to ground through **$R_E$, which is not bypassed**; the drop across it is marked $V_f$, again
with $+$ above and $-$ below and a magenta arrow.

**Why it is current-series feedback.** Because $R_E$ is unbypassed, the emitter current $I_E$
flowing through it develops $V_f = I_E R_E$, which appears **in phase opposition** to $V_i$ — a
voltage proportional to the **output current**, returned **in series** with the input. It reduces
$V_o$, and it disappears the moment $R_E$ is removed or bypassed. ·L7 p11

[eq: beta-current-series] [eq: gain-current-series] ·L7 p11

$$\boxed{\;\beta = \frac{R_E}{R_C}\;}\qquad
\boxed{\;A = \frac{R_C}{r_e}\;}\qquad
\boxed{\;A' = \frac{R_C}{r_e + R_E}\;}$$

[added] **These three are consistent, and it is worth checking once:**

$$\frac{A}{1+\beta A} = \frac{R_C/r_e}{1 + \dfrac{R_E}{R_C}\cdot\dfrac{R_C}{r_e}}
= \frac{R_C/r_e}{1 + R_E/r_e} = \frac{R_C}{r_e + R_E}\quad\checkmark$$

So the familiar "swamping" formula $A = R_C/(r_e+R_E)$ from Lesson 3 **is** the closed-loop gain of
a current-series feedback amplifier. The unbypassed emitter resistor was negative feedback all along.

---

[ex 62.14 ·L7 p11–p12] *For the current-series feedback amplifier of Fig. 62.10, calculate*
*(i) voltage gain without feedback, (ii) feedback factor, (iii) voltage gain with feedback.*
*Neglect $V_{BE}$ and use $r_e = 25\ \mathrm{mV}/I_E$.* (Electronics-I, Madras Univ. 1990)

[fig ·L7 p11, Fig. 62.10] The same topology as Fig. 62.9 with values: supply **10 V**;
$R_B = 0.9\ \mathrm M$ from the rail to the base; $R_C = 10\ \mathrm K$ from the rail to the
collector; output $V_o$ from the collector through a coupling capacitor; $V_i$ into the base through
a coupling capacitor; $R_E = 1\ \mathrm K$ from emitter to ground, **unbypassed**; transistor marked
$\beta = 100$.

**(i)**

$$I_E = \frac{V_{CC}}{R_E + R_B/\beta_{\text{tr}}} = \frac{10}{1 + 900/100}\ \mathrm{(k\Omega)} = \frac{10\ \mathrm V}{10\ \mathrm{k}\Omega} = 1\ \mathrm{mA}$$

$$r_e = \frac{25}{I_E} = 25\ \Omega \qquad\Longrightarrow\qquad A = \frac{10\ \mathrm k\Omega}{25\ \Omega} = 400$$

**(ii)**

$$\beta = \frac{R_E}{R_C} = \frac{1}{10} = 0.1 \qquad\Longrightarrow\qquad \beta A = 0.1\times400 = 40$$

**(iii)**

$$A' = \frac{R_C}{r_e+R_E} = \frac{10{,}000}{25 + 1000} = 9.756$$

$$\text{or}\qquad A' = \frac{A}{1+\beta A} = \frac{400}{1+40} = 9.756$$

> ⚠ VERIFY **V7.8** ·L7 p12 — the second route is printed as
> "$A' = \frac{A}{1+\beta A} = \frac{400}{1+400} = 9.756$". The denominator must be $1 + \beta A$,
> and $\beta A = 40$ was computed three lines earlier — not 400. As printed the expression evaluates
> to $400/401 = 0.998$, not 9.756. Correct form:
> $$\boxed{\;A' = \frac{400}{1+40} = 9.76\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C7.9** ·L7 p12 — the first route is printed as $10{,}000/(\mathbf{20}+1000)$. The
> value of $r_e$ established on the previous page is **25** $\Omega$, and $10{,}000/1025 = 9.756$,
> which is the printed answer; $10{,}000/1020$ would give 9.804. Digit typo; the answer is right.
> See `_verification-log.md`.

---

## 7.14 Voltage-shunt negative feedback amplifier ·L7 p12

[fig ·L7 p12, Fig. 62.11] A single CE stage. The $V_{CC}$ terminal is at the top right; $R_C$ hangs
from it to the collector node (marked with a solid magenta junction dot). From the collector node a
coupling capacitor runs right to an output terminal. **$R_F$** runs horizontally leftwards from the
collector node, then down and across to the **base** node (also marked with a solid dot), where the
input arrives through a coupling capacitor from a terminal labelled $V_i$ at the lower left. The
emitter goes to ground through $R_E$, which is bypassed by a capacitor to ground.

A portion of the output voltage is coupled back through $R_F$ **in parallel** with the input signal
at the base. This stabilises the overall gain while **decreasing both** the input and output
resistances. ·L7 p12

[eq: beta-voltage-shunt] ·L7 p12

$$\boxed{\;\beta = \frac{R_C}{R_F}\;}$$

> ⚠ VERIFY **V7.9** ·L7 p12 — the text reads "a portion of the output voltage is coupled through
> **$R_E$** in parallel with the input signal at the base". $R_E$ is the *emitter* resistor, which
> is bypassed to ground in this very figure and carries no feedback. The element drawn from
> collector to base — and the one that appears in the section's own result $\beta = R_C/R_F$ — is
> **$R_F$**. Correct: "coupled through $R_F$". See `_verification-log.md`.

> ⚠ VERIFY **V7.10** ·L7 p12 — Fig. 62.11 labels **both** terminals $V_i$: the one at the lower
> left (correct, the input) and the one at the upper right on the far side of the collector
> coupling capacitor, which is the **output** and must read $V_o$. Every other figure in the
> chapter labels that terminal $V_o$. See `_verification-log.md`.

---

## 7.15 Current-shunt negative feedback amplifier ·L7 p12

[fig ·L7 p12, Fig. 62.12] A **two-stage** CE amplifier on the $V_{CC}$ rail. Each stage has a
potential-divider bias pair labelled $R_1$ (upper, to the rail) and $R_2$ (lower, to ground), a
collector load $R_C$ to the rail, and an emitter resistor $R_E$ to ground. Input $V_1$ enters
through a coupling capacitor to $Q_1$'s base. $Q_1$'s collector couples through a capacitor to
$Q_2$'s base. $Q_2$'s collector couples through a capacitor to the output terminal $V_0$.

The distinguishing details:

- **$Q_1$'s $R_E$ is bypassed** by a capacitor to ground (drawn alongside it).
- **$Q_2$'s $R_E$ is unbypassed** — a solid junction dot sits at $Q_2$'s emitter node.
- The feedback path runs along the bottom of the figure: from $Q_2$'s **emitter** node, left through
  a capacitor **$C_F$**, then through a resistor **$R_F$**, and up to $Q_1$'s **base/input** node.

$R_F$ and $C_F$ **sample the output current** (via $Q_2$'s unbypassed emitter resistor, which does
the current sensing) and develop a feedback voltage **in parallel with the input voltage**. The
polarity is such that the feedback is negative. ·L7 p12

---

[ex 62.15 ·L7 p12–p13] *Calculate $A$, $r_{in(\text{stage})}$ and $r_{o(\text{stage})}$ of the*
*cascaded amplifier shown in Fig. 62.13 with and without voltage-series feedback. Transistor*
*parameters: $h_{fe} = 100$, $h_{ie} = 2\ \mathrm K$, $h_{oe} = 0$.* (Applied Electronics-I, Punjab Univ. 1992)

> ⚠ VERIFY **C7.10** ·L7 p12 — the question asks for "$I_{o(\text{stage})}$", a **current**; the
> solution computes $r_{o2f}$, an output **resistance** in ohms. Read it as
> $r_{o(\text{stage})}$. See `_verification-log.md`.

[fig ·L7 p12, Fig. 62.13] Two RC-coupled CE stages on a $V_{CC}$ rail.
**Stage 1 ($Q_1$)** — divider **200 K** (rail to base) and **50 K** (base to ground); collector load
**10 K**; source $V_S$ (a circled sine-wave symbol, grounded) drives the base through **$C_1$**.
**Stage 2 ($Q_2$)** — divider **150 K** and **50 K**; collector load **10 K**; $Q_1$'s collector
couples to $Q_2$'s base through **$C_2$**; output $V_o$ leaves $Q_2$'s collector through **$C_3$**.
**Emitter networks** — each emitter has a **5 K** resistor bypassed by a capacitor ($C_5$ for $Q_1$,
$C_6$ for $Q_2$); below $Q_1$'s emitter network sits **$R_1 = 250\ \Omega$** to ground, unbypassed.
**Feedback** — **$R_2 = 2\ \mathrm K$** runs from $Q_2$'s emitter node, through **$C_4$**, back to
the top of $R_1$ at $Q_1$'s emitter. So $R_1$ and $R_2$ form the feedback divider of §7.12.

### (i) Without feedback ·L7 p13

$$r_{in(\text{base})}\ \text{for}\ Q_1 = h_{ie} = 2\ \mathrm K \qquad\text{(same for } Q_2)$$

$$r_{i.1} = 200\ \mathrm K \,\|\, 50\ \mathrm K \,\|\, 2\ \mathrm K = 1.9\ \mathrm K$$

$$r_{o.2} = r_{L.2}\ \text{for}\ Q_2 = 10\ \mathrm K \,\|\, (2.0+0.25)\ \mathrm K = 1.83\ \mathrm K$$

$$r_{o.1} = r_{L.1}\ \text{for}\ Q_1 = 10\ \mathrm K \,\|\, 150\ \mathrm K \,\|\, 50\ \mathrm K \,\|\, 2\ \mathrm K = 1.6\ \mathrm K$$

$$A_{v1} = \frac{h_{fe.1}\,r_{L.1}}{h_{ie}} = \frac{100\times1.6}{2} = 80$$

$$A_{v2} = \frac{h_{fe.2}\,r_{L.2}}{h_{ie}} = \frac{100\times1.83}{2} = 92$$

$$A_v = A_{v1}\cdot A_{v2} = 80\times92 = 7360$$

### (ii) With feedback ·L7 p13

$$\beta = \frac{R_1}{R_1+R_2} = \frac{0.25}{0.25+2.0} = \frac{1}{9}$$

$$r_{o2f} = \frac{r_{o2}}{1+\beta A} = \frac{1.83\ \mathrm K}{1 + \tfrac19\times7360} = \frac{1.83\ \mathrm K}{819} = 2.2\ \Omega$$

$$r_{i.1f} = r_{i.1}\,(1+\beta A) = 1.9\ \mathrm K \times 819 = 1556\ \mathrm K$$

$$A_f = \frac{A}{1+\beta A} = \frac{7360}{819} = 8.99$$

[added] **Full recomputation.** $r_{i.1} = (1/200 + 1/50 + 1/2)^{-1} = 1.905$ K ✓;
$r_{o.2} = (1/10 + 1/2.25)^{-1} = 1.837$ K ✓; $r_{L.1} = (1/10+1/150+1/50+1/2)^{-1} = 1.596$ K ✓;
$A_{v1} = 79.8$, $A_{v2} = 91.8$, $A_v = 7327$ (the printed 7360 comes from the rounded 1.6 and
1.83). Loop gain $1 + 7360/9 = 818.8$ ✓; $r_{o2f} = 1830/818.8 = 2.235\ \Omega$ ✓;
$r_{i.1f} = 1555.7$ K ✓; $A_f = 7360/818.8 = 8.99$.

> ⚠ VERIFY **C7.11** ·L7 p13 — printed $A_f = 7360/819 = \mathbf{8.9}$. The quotient is
> $8.986$, which rounds to **9.0**, not 8.9. Arithmetic slip in the last digit only. See
> `_verification-log.md`.

[added] **What the numbers demonstrate.** Voltage-**series** feedback: $r_i$ went from 1.9 kΩ to
1.56 MΩ (**×819**, the loop gain) and $r_o$ from 1.83 kΩ to 2.2 Ω (**÷819**). Exactly what the
§7.11 table predicts for the voltage-series column, and the same factor in both directions.

---

[ex 62.16 ·L7 p13] *In the two-stage RC-coupled amplifier (Fig. 62.14) using emitter feedback, find*
*the overall gain. Neglect $V_{BE}$ and take $\beta_1 = \beta_2 = 100$.*

[fig ·L7 p13, Fig. 62.14] Two CE stages on a **30 V** rail.
**Stage 1 ($Q_1$)** — divider **80 K** / **40 K**; collector load **10 K**; input $V_i$ through a
coupling capacitor to the base.
**Stage 2 ($Q_2$)** — divider **80 K** / **40 K**; collector load **10 K**; $Q_1$'s collector
couples to $Q_2$'s base through a capacitor; output $V_o$ from $Q_2$'s collector through a coupling
capacitor into a **10 K** load resistor to ground.
**Emitter networks (both stages, identical)** — a **500 $\Omega$** resistor from the emitter, in
series with a **10 K** resistor to ground; the 10 K is bypassed by a capacitor, the **500 $\Omega$
is not**. That unbypassed 500 $\Omega$ is the emitter (current-series) feedback of the title.

**Solution** ·L7 p13 — the 500 $\Omega$ swamps out $r_e$, so $r_e + R_E \cong R_E$:

$$A_{v.2} = \frac{r_{L.2}}{r_e+R_E} \cong \frac{r_{L.2}}{R_E} = \frac{10\ \mathrm K \,\|\, 10\ \mathrm K}{500\ \Omega} = \frac{5000}{500} = 10$$

$$\beta_{\text{tr}} R_E = 100 \times 500 = 50\ \mathrm K$$

$$r_{i.2} = 80\ \mathrm K \,\|\, 40\ \mathrm K \,\|\, 50\ \mathrm K$$

$$r_{L.1} = R_{C.1} \,\|\, r_{i.2} = 10\ \mathrm K \,\|\, 80\ \mathrm K \,\|\, 40\ \mathrm K \,\|\, 50\ \mathrm K = 6.3\ \mathrm K$$

$$A_{v.1} = \frac{r_{L.1}}{R_E} = \frac{6.3\times10^3}{500} = 12.6$$

$$A = A_{v.1}\times A_{v.2} = 10 \times 12.6 = 126$$

[added] Verified: $r_{i.2} = (1/80+1/40+1/50)^{-1} = 17.39$ K; $r_{L.1} = 6.349$ K;
$A_{v.1} = 12.70$; $A = 127.0$ against the printed 126. ✓ (rounding of 6.349 to 6.3)

[added] Note the $\beta$ in "$\beta_1 = \beta_2 = 100$" and in "$\beta r_E$" is the **transistor**
gain — used to find the resistance looking into the base, $\beta(r_e+R_E) \cong \beta R_E$. There is
no feedback-fraction $\beta$ anywhere in this example.

---

## 7.16 Multistage amplifiers — the general picture ·L7 p14–p15

**Chapter 61 opens here.** ·L7 p14 is that chapter's **title page** — "MULTISTAGE AND FEEDBACK
AMPLIFIERS", a list of learning objectives, a photomicrograph of an integrated circuit die, and the
single-sentence summary "In a multistage amplifier, a number of single amplifiers are connected
in cascade arrangement, i.e. the output of the first stage is connected to the input of the second
stage." It carries no equations, figures or examples. Its **learning-objective list** maps the
chapter: general · amplifier coupling · RC-coupled two-stage · impedance-coupled two-stage ·
advantages of impedance coupling · transformer-coupled two-stage · advantages of transformer
coupling · frequency response · direct-coupled two-stage using similar transistors · direct-coupled
using complementary symmetry · Darlington pair · advantages of the Darlington pair · Darlington pair
versus emitter follower · special features of a differential amplifier · common-mode input ·
differential amplifier.

[added] Note that **only the first eight of those sixteen objectives appear in this PDF** (§61.1–§61.10).
Direct coupling beyond the block diagram, the Darlington pair and the differential amplifier are
listed on the title page but their sections are on printed pages that were not scanned.

(Likewise ·L7 p1 is **Chapter 62's** title page — "FEEDBACK AMPLIFIER", its own objective list,
a photograph of a heatsinked module, and the summary "A feedback amplifier is one in which a
fraction of the amplifier output is fed back to the input circuit." Its objectives run: feedback
amplifiers · principle of feedback amplifiers · advantages of negative feedback · gain stability ·
decreased distortion · feedback over several stages · increased bandwidth · forms of negative
feedback · shunt-derived series-fed voltage feedback · current-series feedback amplifier ·
voltage-shunt negative feedback amplifier · current-shunt negative feedback amplifier ·
non-inverting op-amp with negative feedback · effect of negative feedback on $R_{in}$ and $R_{out}$ ·
$R_{in}$ and $R_{out}$ of an inverting op-amp with negative feedback. The **last three
op-amp objectives have no sections in this PDF** — the scan stops at §62.12.)

A single stage often cannot supply the voltage amplification, power gain or frequency response a
composite circuit or a load device requires, so two or more stages are cascaded — the output of one
becoming the input of the next. ·L7 p15

[fig ·L7 p15, Fig. 61.1] Three triangular amplifier blocks in a row, labelled $A_{V1}$, $A_{V2}$,
$A_{V3}$, drawn on a common ground rail at the bottom. Each block has an open-circle terminal on its
input side and another on its output side; a magenta arrow runs from the ground rail up to each
terminal, labelled with the voltage there. Reading left to right the six labels are
$v_{i1}$, $v_{o1}$, $v_{o2}$, $v_{o2}$, $v_{i3}$, $v_{o3}$.

> ⚠ VERIFY **C7.12** ·L7 p15 — in Fig. 61.1 the **input** terminal of the second stage is labelled
> $v_{o2}$; by the figure's own pattern ($v_{i1}$ … $v_{i3}$) it must be **$v_{i2}$**. The label
> $v_{o2}$ then correctly appears again on that stage's output. The right-most label $v_{o3}$ is
> also clipped by the figure frame. See `_verification-log.md`.

[def] **Two categories** ·L7 p15

- **Cascaded amplifiers** — each stage, *and* the type of interstage coupling, are **identical**.
- **Compound amplifiers** — the stages may differ (one CE, one CC) and different couplings may be
  mixed.

### Gain of a cascade ·L7 p15

[eq: cascade-gain-product] The overall voltage gain is the **product** — not the sum — of the stage
gains:

$$\boxed{\;A_v = A_{v1}\times A_{v2}\times A_{v3}\times\dots\;}$$

[eq: cascade-gain-db] In decibels it becomes a **sum**:

$$\boxed{\;G = G_1 + G_2 + G_3 + \dots\;}$$

Similarly for current, and for power: ·L7 p15

$$A_i = A_{i1}\times A_{i2}\times A_{i3}\times\dots$$

[eq: power-gain-db]

$$\boxed{\;A_p = A_v \cdot A_i \qquad\text{and}\qquad G_p = 10\log_{10}A_p\ \ \mathrm{dB}\;}$$

[added] Note the **10** in the power-gain formula against the **20** used for voltage gain — this is
the whole $10\log$ vs $20\log$ distinction, and §7.24 gives the rule properly.

### The worked illustration ·L7 p15

A two-stage cascade: stage 1 has $A_{v1} = 2000$, stage 2 has $A_{v2} = 1000$.

$$G_1 = 20\log_{10}2000 = 66\ \mathrm{dB}\qquad G_2 = 20\log_{10}1000 = 60\ \mathrm{dB}$$

$$A_v = 1000\times2000 = 2\times10^6$$

$$G = 60 + 66 = 126\ \mathrm{dB} \qquad\text{and}\qquad 20\log_{10}(2\times10^6) = 20\times6.3 = 126\ \mathrm{dB}$$

[added] Verified: $20\log_{10}2000 = 66.02$, $20\log_{10}1000 = 60.00$,
$20\log_{10}(2\times10^6) = 126.02$. ✓

[added] **The caveat that makes this examinable.** The result holds **only if the loading of the
first stage by the second is neglected**. It is approximately true so long as the impedance looking
into the second stage's input is **much greater** than the output impedance of the first stage.
Otherwise the overall gain is **much less**. ·L7 p15 This is why Examples 62.15 and 62.16 compute
$r_{L.1} = R_{C.1}\,\|\,r_{i.2}$ rather than just $R_{C.1}$.

---

## 7.17 Amplifier coupling — the four methods ·L7 p16

All amplifiers need a coupling network; even a single stage must be coupled to its input and output
devices. In multistage systems there is **interstage** coupling as well, and the type used
determines the cascade's characteristics — amplifiers are in fact **classified** by their coupling
network. ·L7 p16

[fig ·L7 p16, Fig. 61.2] Four small two-transistor circuits on one panel, lettered (a)–(d), all
drawn with the supply rail at the top and grounds at the bottom, $v_i$ entering the first
transistor's base at the left and $v_o$ leaving the second transistor's collector at the right with
a magenta arrow.

- **(a) RC coupling.** First transistor's collector load $R_{C1}$; a series capacitor $C$ to the
  second transistor's base; $R_B$ from the rail to that base; second collector load $R_{C2}$.
- **(b) Impedance coupling.** The two collector loads are **inductors** $L_1$ and $L_2$ (drawn as
  coils) instead of resistors; a series capacitor $C$ links stage 1's collector to stage 2's base,
  with $R_B$ from the rail to that base.
- **(c) Transformer coupling.** Stage 1's collector drives the **primary of a transformer $T$**
  (drawn with a coil each side of a core); the **secondary** connects directly to stage 2's base.
  There is no coupling capacitor and no base resistor.
- **(d) Direct coupling.** Stage 1's collector connects **straight** to stage 2's base — no
  capacitor, no transformer, no resistor in between. Both collector loads are resistors to the rail.

### 1. Resistance–capacitance (RC) coupling ·L7 p16

Also **capacitive coupling**; amplifiers using it are **RC-coupled amplifiers**. The network is two
resistors $R_{C1}$, $R_{C2}$ and one capacitor $C$, and $C$ is the connecting link. Its function is
**two-fold**:

- (a) to **pass** the ac signal from one stage to the next;
- (b) to **block** the passage of dc voltages from one stage to the next.

### 2. Impedance (inductive) coupling ·L7 p16

Also **choke-capacitance coupling**. The network is $L_1$, $C$ and $R_B$. The coupling coil's
impedance depends on (i) its inductance and (ii) the signal frequency.

### 3. Transformer coupling ·L7 p16

Because the secondary conveys the ac signal directly to the second stage's base, there is **no need
for a coupling capacitor**; and because the secondary winding also provides a base return path,
there is **no need for a base resistance**.

### 4. Direct coupling ·L7 p16

Used where the load must be connected **directly in series** with the output terminal of the active
element.

> ⚠ VERIFY **C7.13** ·L7 p16 — the page's two photographs have **swapped captions**. The
> rack-mounted instrument (a video distribution amplifier) is captioned "Modern coupling
> transformer", and the tray of wound iron-cored components is captioned "R.C. Coupled two-stage
> amplifier". Neither caption belongs to the picture above it. See `_verification-log.md`.

---

## 7.18 Advantages of impedance coupling ·L7 p17

> **Note on continuity.** PDF p17 opens **part-way through the solution of Example 61.4**
> (impedance-coupled two-stage amplifier). Printed pages 2318–2322, which carry §61.3–61.5 and
> Examples 61.1–61.4, are **not in this PDF**. The surviving fragment is transcribed below for
> completeness; the problem statement is unavailable.

[ex 61.4 — **fragment only** ·L7 p17]

$$\dots \,\|\, \beta_2 r_{e.2} = 1.2\ \mathrm M \,\|\, 2500\ \Omega \cong 2500\ \Omega$$

Obviously $X_L \gg r_{i.2}$, which justifies the approximation.

$$A_{v.1} = \frac{2500}{25} = 100$$

$$\textbf{(iii)}\quad A_v = 100\times240 = 24{,}000 \qquad G_v = 20\log_{10}24{,}000 = 87.6\ \mathrm{dB}$$

[added] The decibel conversion checks out: $20\log_{10}24{,}000 = 87.60$ dB ✓. The stage-2 gain of
240 and the value of $r_{e.1} = 25\ \Omega$ come from the missing pages.

> ⚠ ILLEGIBLE ·L7 p17 — Example 61.4's statement, circuit and parts (i)–(ii) are on printed pages
> 2318–2322, absent from this PDF. Needs a screenshot of those pages.

### The advantage, and the disadvantages ·L7 p17

**Advantage.** There is **hardly any dc drop across $L$**, so a low collector supply voltage can be
used. (A resistor load drops $I_C R_C$ volts; an inductor drops only $I_C \times$ its winding
resistance.)

**Disadvantages:**

1. Larger, heavier and costlier than RC coupling.
2. To stop the coupling inductor's magnetic field affecting the signal, its turns must be wound on a
   **closed core** and **shielded**.
3. Because inductor impedance depends on frequency, the frequency characteristics are **not as good
   as RC coupling** — the flat part of the gain-versus-frequency curve is small.

> ⚠ VERIFY **C7.14** ·L7 p17 — disadvantage 3 prints "not as good as those of **BC** coupling".
> There is no "BC coupling"; it is **RC** coupling, as the same sentence's context and the rest of
> the section confirm. See `_verification-log.md`.

[fig ·L7 p17, Fig. 61.13] Gain (vertical, labelled "Gain" with an upward magenta arrow) against
frequency, origin marked 0. A single magenta curve rises steeply from near zero at the left,
flattens across a **short** plateau, then falls steeply at the right. The horizontal axis is
labelled **t**.

> ⚠ VERIFY **C7.15** ·L7 p17 — Fig. 61.13's horizontal axis is labelled **$t$**, but the curve is
> the **frequency**-versus-gain characteristic the text has just described ("The flat part of the
> frequency versus gain curve is small (Fig. 61.13)"). The axis must be **$f$**, and on a
> logarithmic scale. Read as gain against frequency. See `_verification-log.md`.

**Why the gain falls at each end** ·L7 p17

- **At low frequencies**, the coupling capacitor's reactance is large, dropping much of the signal.
- Gain then **increases with frequency** until it levels off in the middle of the audio range.
- **At relatively high frequencies**, gain drops off again because of the increased reactance.
- Hence impedance coupling is **rarely used beyond the audio range**.

> ⚠ VERIFY **V7.12** ·L7 p17 — printed "At low frequencies, the gain is low due to large
> **capacitance** offered by the coupling capacitor". A capacitor's **capacitance** is a fixed
> component value and does not depend on frequency; what is large at low frequency is its
> **reactance**,
> $$\boxed{\;X_C = \frac{1}{2\pi f C}\;}$$
> which is why the coupling capacitor drops a large part of the signal there. The same section
> uses "reactance" correctly two lines later for the high-frequency end. See `_verification-log.md`.

> ⚠ VERIFY **C7.16** ·L7 p17 — "gain drops **of** again" — a typo for "drops **off** again". See
> `_verification-log.md`.

---

## 7.19 Transformer-coupled two-stage amplifier ·L7 p17–p18

[fig ·L7 p17, Fig. 61.14] Two CE stages on a $V_{CC}$ rail, coupled by transformers.
**Stage 1 ($Q_1$)** — bias divider $R_1$ (rail to base) and $R_2$ (base to ground); emitter resistor
$R_3$ to ground, bypassed by $C_2$; input $v_1$ enters the base through **$C_1$**. The collector
drives the **primary of $T_1$** (drawn as a coil pair inside a dashed magenta box).
**Stage 2 ($Q_2$)** — the **secondary of $T_1$** connects to $Q_2$'s base; bias divider $R_4$ (rail)
and $R_5$ (ground), $R_5$ bypassed by $C_3$; emitter resistor $R_6$ to ground, bypassed by $C_4$.
$Q_2$'s collector drives the **primary of $T_2$** (again in a dashed box); $T_2$'s **secondary**
feeds the matched load **$R_7$**, which is grounded.

So $T_1$ is the **coupling** transformer and $T_2$ the **output** transformer; $C_1$ is the input
coupling capacitor and $C_2$, $C_3$, $C_4$ are bypass capacitors; $R_1$–$R_2$ and $R_4$–$R_5$ are
the two dividers; $R_3$ and $R_6$ are the emitter-stabilising resistors. ·L7 p17

### (i) Circuit operation ·L7 p17

The signal is coupled through $C_1$ to $Q_1$'s base, appears amplified in $T_1$'s primary, and is
passed to the secondary by magnetic induction — which also provides **dc isolation** between the
input and output circuits. $T_1$'s secondary applies the signal to $Q_2$'s base; the amplified
result appears in $T_2$'s primary, passes to $T_2$'s secondary by induction, and finally appears
across the matched load $R_7$.

### (ii) Voltage gain ·L7 p17–p18

**Symbols** [table]

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $a$ | turns ratio $N_1/N_2$ of a coupling transformer | dimensionless | 2–10 |
| $r_{o.1}$ | resistance seen at $Q_1$'s collector (reflected) | $\Omega$ | tens of kΩ |
| $r_{i.2}$ | input resistance of stage 2 | $\Omega$ | ~1 kΩ |
| $r_{e}$ | transistor ac emitter resistance $= 25$ or $50\ \mathrm{mV}/I_E$ | $\Omega$ | 10–100 |

$$A_{v.1} = \frac{r_{o.1}}{r_{e.1}} \qquad\text{where}\qquad r_{o.1} = a^2\,r_{i.2},\quad a = N_1/N_2 \text{ for } T_1$$

$$r_{i.2} = R_4 \,\|\, R_5 \,\|\, \beta_2 r_{e.2}$$

$$A_{v.2} = \frac{r_{o.2}}{r_{e.2}} \qquad\text{where}\qquad r_{o.2} = a^2 R_7$$

> ⚠ VERIFY **V7.11** ·L7 p17–p18 — printed as "$A_{e.2} = \dfrac{r_{0.2}}{r_{e.2}}$ where
> $\mathbf{r_{e.2}} = a^2R_7$". The quantity $a^2R_7$ is the load **reflected into $T_2$'s
> primary**, i.e. $r_{o.2}$ — it cannot also be $r_{e.2}$, which the *same page* computes as
> $33.3\ \Omega$ from $50\ \mathrm{mV}/I_E$, while $a^2R_7 = 25\ \mathrm{k}\Omega$. As printed the
> gain formula would read $A = r_{o.2}/r_{o.2} = 1$. Correct form:
> $$\boxed{\;r_{o.2} = a^2 R_7\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C7.17** ·L7 p18 — the same line prints the gain as **$A_{e.2}$**; every other
> occurrence in the section and the worked example writes **$A_{v.2}$**. See `_verification-log.md`.

---

[ex 61.5 ·L7 p18] *For the transformer-coupled two-stage amplifier of Fig. 61.15, calculate*
*(i) $A_{v.1}$ (ii) $A_{v.2}$ and (iii) $A_v$ in dB. Neglect $V_{BE}$ and use $r_e = 50\ \mathrm{mV}/I_E$.*
*Take $\beta_1 = \beta_2 = 50$ and treat the transformers as ideal.* (Electronics, Indore Univ.)

[fig ·L7 p18, Fig. 61.15] The Fig. 61.14 topology with values. Supply **9 V** at the top left,
$V_{CC}$ at the top right. **Stage 1** — $R_1 = 20\ \mathrm K$ (rail to base), $R_2 = 4\ \mathrm K$
(base to ground), $R_3 = 1\ \mathrm K$ emitter resistor bypassed; input $V_i$ through a coupling
capacitor. $Q_1$'s collector drives $T_1$, marked **5 : 1**. **Stage 2** — $T_1$'s secondary to
$Q_2$'s base; $R_4 = 20\ \mathrm K$, $R_5 = 4\ \mathrm K$ divider; $R_6 = 1\ \mathrm K$ emitter
resistor bypassed. $Q_2$'s collector drives $T_2$, also marked **5 : 1**, whose secondary feeds
$R_7 = 1\ \mathrm K$ to ground.

**Solution** — for each transformer $a = 5$. ·L7 p18

$$\text{Drop across } R_2 = 9\times\frac{4}{24} = 1.5\ \mathrm V$$

$$\text{Drop across } R_3 \cong 1.5\ \mathrm V \qquad\Longrightarrow\qquad I_{E.1} = \frac{1.5}{1\ \mathrm k\Omega} = 1.5\ \mathrm{mA}$$

$$r_{e.1} = \frac{50}{1.5} = 33.3\ \Omega \qquad\text{and}\qquad r_{e.2} = 33.3\ \Omega \ \text{(same)}$$

$$\beta_2\,r_{e.2} = 50\times33.3 = 1665\ \Omega$$

$$r_{i.2} = R_4 \,\|\, R_5 \,\|\, \beta_2 r_{e.2} = 20\ \mathrm K \,\|\, 4\ \mathrm K \,\|\, 1665\ \Omega = 1110\ \Omega$$

$$r_{o.1} = a^2 r_{i.2} = 5^2\times1110 = 27{,}750\ \Omega$$

$$\textbf{(i)}\quad A_{v.1} = \frac{r_{o.1}}{r_{e.1}} = \frac{27{,}750}{33.3} \cong 830$$

$$\textbf{(ii)}\quad A_{v.2} = \frac{r_{o.2}}{r_{e.2}} = \frac{25\times1000}{33.3} = 750$$

$$\textbf{(iii)}\quad A_v = 830\times750 = 622{,}500 \qquad G_v = 20\log_{10}622{,}500 = 116\ \mathrm{dB}$$

> ⚠ VERIFY **V7.13** ·L7 p18 — part (ii) is printed as
> $A_{v.2} = \dfrac{25\times\mathbf{100}}{33.3} = 750$. $25\times100 = 2500$, and $2500/33.3 = 75$,
> not 750. The numerator is $r_{o.2} = a^2R_7 = 25\times1000\ \Omega = 25{,}000\ \Omega$ (the
> exponent has dropped out of "$25\times10^3$"). Correct form:
> $$\boxed{\;A_{v.2} = \frac{25{,}000}{33.3} = 750\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C7.18** ·L7 p18 — part (i) prints "$\cong$ **830**"; $27{,}750/33.3 = 833.3$. The
> 830 is then carried into part (iii). Using 833 throughout gives $A_v = 625{,}000$ and
> $G_v = 115.9$ dB — the same 116 dB. Rounding only. See `_verification-log.md`.

[added] **Full recomputation from the given data.** $r_{e} = 50/1.5 = 33.33\ \Omega$;
$\beta_2 r_e = 1666.7\ \Omega$; $r_{i.2} = (1/20000 + 1/4000 + 1/1666.7)^{-1} = 1111.1\ \Omega$;
$r_{o.1} = 27{,}778\ \Omega$; $A_{v.1} = 833.3$; $r_{o.2} = 25{,}000\ \Omega$; $A_{v.2} = 750.0$;
$A_v = 625{,}000$; $G_v = 20\log_{10}625{,}000 = 115.9$ dB. ✓ The printed 116 dB is right.

---

## 7.20 Advantages and disadvantages of transformer coupling ·L7 p18

**Advantages** ·L7 p18

1. **More efficient**, because the primary in the collector circuit has a low **dc resistance** — no
   wasted supply volts.
2. It provides a **higher voltage gain**.
3. It provides **impedance matching** between stages, which is what maximum power transfer requires.
   A transistor stage's input impedance is typically lower than its output impedance, so the
   interstage transformer's secondary impedance is typically lower than its primary impedance.

This coupling is effective when the final output feeds a **low-impedance load**: a typical
loudspeaker is 4 $\Omega$ to 16 $\Omega$, while a transistor stage's output impedance is several
hundred ohms. An output audio transformer removes that mismatch. ·L7 p18

**Disadvantages** ·L7 p18

1. The coupling transformer is **costly and bulky**, particularly at audio frequencies because of
   its heavy iron core.
2. At radio frequencies the **inductance and winding capacitance** cause problems.
3. **Poor frequency response**, because the transformer is frequency sensitive; the frequency range
   is limited.
4. It tends to introduce **hum** in the output.

---

## 7.21 Frequency response of a transformer-coupled stage ·L7 p19

Three properties of a coupling transformer drive its frequency response: ·L7 p19

1. it introduces **inductance** into both the input and output circuits;
2. **leakage inductance** exists between primary and secondary;
3. both windings introduce **shunting (distributed) capacitance**, especially at high frequencies.

[fig ·L7 p19, Fig. 61.16] Voltage Gain (vertical, labelled "Voltage Gain" reading upwards) against
frequency $f$ (horizontal, origin 0, a magenta arrowhead marking the $f$ direction, with a second
tick further right labelled $f_o$). A single magenta curve: it rises steeply from near zero at the
left, flattens into a **short** mid-band plateau, then — instead of simply rolling off — **rises to
a pronounced peak** at $f_o$ before falling away steeply. A **dashed vertical line** marks $f_o$
under the peak, and a label "**Resonant Rise**" at the top with an arrow points at the peak.

**Reading the curve** ·L7 p19

- Gain **decreases at low frequencies**: the output voltage is the ac collector current times the
  **primary reactance**, and at low frequencies the primary reactance is small, so the gain is less.
- Gain **decreases at high frequencies** because the **distributed capacitance** between turns acts
  as a bypass capacitor, shunting the signal and reducing the output.
- The **peak** at $f_o$ is a **resonance** between the winding inductance and the distributed
  capacitance — they form a tuned circuit.
- There is therefore **frequency distortion**: not all frequencies are amplified equally, and the
  flat part of the curve is small compared with RC coupling. Transformer-coupled amplifiers *can*
  be designed for a flat response and excellent fidelity across the audio range.

### Applications ·L7 p19

Transformer coupling is often used in the **last stage** of a multistage amplifier, where the effort
goes into maximising power transfer by perfect impedance matching.

---

[ex 61.6 ·L7 p19] *In a multistage transformer-coupled amplifier, the output impedance of the first*
*stage is 5 K and the input impedance of the second stage is 1 K. Determine the primary and secondary*
*inductances of the transformer for perfect impedance matching at $f = 2000$ Hz. If one turn gives an*
*inductance of $10\ \mu\mathrm H$, find the number of primary and secondary turns.*
(Electronic Engg.-I, Osmania Univ. 1991)

**Principle** ·L7 p19 — the **primary** must match the output impedance of the first stage, the
**secondary** the input impedance of the second stage.

$$X_{Lp} = 5000\ \Omega \quad\Longrightarrow\quad 2\pi f L_p = 5000
\quad\Longrightarrow\quad L_p = \frac{5000}{2\pi\times2000} = 0.4\ \mathrm H$$

$$X_{Ls} = 1000\ \Omega \quad\Longrightarrow\quad 2\pi f L_s = 1000
\quad\Longrightarrow\quad L_s = \frac{1000}{2\pi\times2000} = 0.08\ \mathrm H$$

Inductance varies as the **square** of the turns:

$$L \propto N^2 = kN^2$$

$$N = 1,\ L = 10\ \mu\mathrm H \quad\Longrightarrow\quad 10\times10^{-6} = k\times1^2
\quad\Longrightarrow\quad k = 10^{-5}$$

$$\text{Primary:}\quad 0.4 = 10^{-5}N_p^2 \quad\Longrightarrow\quad N_p = \sqrt{4\times10^4} = 200$$

$$\text{Secondary:}\quad 0.08 = 10^{-5}N_s^2 \quad\Longrightarrow\quad N_s = \sqrt{8\times10^3} = 89$$

> ⚠ VERIFY **V7.14** ·L7 p19 — printed "For primary winding $0.4 = 10^{-5}N_p^2 \times 5$ or
> $N_p =$ **632**", and the example closes "As seen, it is a nearly **7 : 1** step-down
> transformer." Both are wrong.
> With the page's own $k = 10^{-5}$, $N_p = \sqrt{0.4/10^{-5}} = \mathbf{200}$; the printed 632 is
> $\sqrt{0.4/10^{-6}}$, i.e. it uses $k = 10^{-6}$ — inconsistent with the secondary, which was
> computed correctly from $k = 10^{-5}$ ($N_s = \sqrt{0.08/10^{-5}} = 89$). The stray "$\times 5$"
> in the printed expression has no meaning. Correct form:
> $$\boxed{\;N_p = 200,\quad N_s = 89,\quad \frac{N_p}{N_s} = 2.25\;}$$
> **Independent check that settles it:** a matching transformer's turns ratio is
> $\sqrt{Z_p/Z_s} = \sqrt{5000/1000} = \sqrt5 = 2.24$ — which is $200/89$, not $632/89 = 7.1$.
> The transformer is a **2.24 : 1** step-down, not 7 : 1. See `_verification-log.md`.

> ⚠ VERIFY **C7.19** ·L7 p19 — the constant is printed as "$10\times10^{-6} = k\times\mathbf{12^2}$".
> The turns number substituted is $N = 1$, so it must be $k\times1^2$; the printed "12" is a
> corrupted "1". The value $k = 10^{-5}$ that follows is right. See `_verification-log.md`.

[added] All four numbers verified: $L_p = 0.3979$ H, $L_s = 0.07958$ H, $N_p = 200.0$,
$N_s = 89.44$. ✓

---

## 7.22 Complementary-symmetry, class-C and tuned amplifiers ·L7 p20–p21

These pages come from **Chapter 60** and sit slightly outside the lesson's title, but they are in
the PDF and are transcribed here.

### Complementary-symmetry class-B push-pull ·L7 p20

The standard class-B push-pull amplifier has two drawbacks: it needs two **power transistors of the
same type** with closely matched parameters, and it needs **two out-of-phase input signals**, which
forces an input centre-tapped transformer or a phase inverter and complicates the driver circuitry.

The **complementary symmetry** amplifier removes both while keeping the push-pull advantages. Its
requirement is a pair of closely-matched but **oppositely-doped** power transistors — one PNP, one
NPN, made with the same material and technology and with the same maximum rating. That is what
"complementary" means. ·L7 p20

[fig ·L7 p20, Fig. 60.36] $v_{in}$ (with a magenta sine wave beside it) enters through a coupling
capacitor to the joined bases of two transistors: **A**, an **NPN** at the top, whose collector goes
to $+V_{CC1}$; and **B**, a **PNP** below it, whose collector goes to $-V_{CC2}$. Their emitters are
joined and drive the output node $v_o$, from which the load $R_L$ runs to ground. A resistor runs
from the base line to ground. At the right of the load, two half-sine waveforms are drawn and
labelled **A** (the positive half) and **B** (the negative half), showing which transistor supplies
which half-cycle.

**Operation** ·L7 p20

- With **no input**, neither transistor conducts, so the current through $R_L$ is zero.
- **Positive-going input** → transistor **A** conducts, **B** is driven into cut-off.
- **Negative-going input** → **A** is off, **B** conducts.

Turning one transistor ON turns the other OFF — that is what makes it push-pull.

Both devices work as **emitter followers**, so the circuit has the emitter-follower properties:
**unity voltage gain, no phase inversion, input impedance much higher than output impedance**. The
input is capacitively coupled; the output is **direct-coupled**. ·L7 p20

Two supply batteries are needed as drawn; only one would be needed with a **totem-pole**
configuration. Eliminating the transformer **extends both the high- and low-frequency responses**
and cuts cost and weight. ·L7 p20

### Class-C amplifier ·L7 p20

The transistor is biased **much beyond cut-off**. Hence:

1. output current flows only during **part of one half-cycle** of the input;
2. **no** output current flows during any part of the negative half-cycle;
3. the output signal hardly resembles the input — it is **short pulses**;
4. circuit efficiency is high, about **85 to 90%**.

Because of the distortion, class-C amplifiers are **not used for audio work**. They are used for
high-power output at **radio frequencies**, where the harmonic distortion can be removed by simple
circuits — in practice as high-frequency power **switches** in radio transmitters rather than as
amplifiers. ·L7 p20

> ⚠ VERIFY **C7.20** ·L7 p20 — "Because of **his** distortion" — a typo for "**this**". See
> `_verification-log.md`.

### Tuned amplifier ·L7 p20–p21

Gain depends directly on load impedance, and a high impedance can be got from a **high-$Q$ tuned
(resonant) $LC$ circuit as the load**. The amplifier's frequency-response curve then takes the same
shape as the tuned circuit's resonance curve, so only a **narrow band around $f_o$** is amplified
well and everything else is discriminated against. Non-linear distortion is eliminated by the load's
high selectivity, so the output is nearly sinusoidal — which in turn permits high efficiency by
operating the transistor in its non-linear region. ·L7 p20–p21

[fig ·L7 p21, Fig. 60.37] **Left:** a CE stage with $R_B$ from the $V_{CC}$ rail to the base,
$v_{in}$ entering the base through a coupling capacitor, an emitter resistor bypassed to ground, and
— in place of a collector resistor — a **parallel $LC$ tank**: a capacitor $C$ and an inductor $L$
side by side between the rail and the collector, with $V_o$ taken across a second coil at the right.
**Right:** the response — $V_o$ (vertical) against $f$ (horizontal, origin 0), a single narrow
magenta resonance peak centred on a dashed vertical line at $f_o$, falling away symmetrically on
both sides.

---

## 7.23 Distortion in amplifiers ·L7 p21

[def] An ideal amplifier's output differs from its input **only in amplitude**. In practice the
output always differs in **waveform** or in **frequency content** as well, and that difference is
called **distortion**. ·L7 p21

The categories depend on which region of the characteristic the transistor uses and on the circuit
and device reactances.

### (a) Non-linear distortion ·L7 p21

Occurs when the transistor operates in the **non-linear region** of its characteristic — i.e. with
**large-signal** inputs.

| Viewed in | Called |
|---|---|
| the **time** domain | **amplitude distortion** or waveform distortion |
| the **frequency** domain | **harmonic distortion** (input is one frequency, e.g. a pure sine) |
| with a **multi-frequency** input (e.g. speech) | **intermodulation (IM) distortion** |

### (b) Linear distortion ·L7 p21

Occurs **even when the device works on the linear part of its characteristic with small signals**.
It is due to the **frequency-dependent reactances** of the circuit or the device itself, and shows
up when the input is *composite* — several frequencies at once. Crucially, **the output contains no
frequencies other than those at the input**. Two sub-types:

- **frequency distortion** — unequal amplification of the different frequencies present;
- **phase (delay) distortion** — unequal phase shift of the various signal components.

### Non-linear distortion in the time domain ·L7 p21

[fig ·L7 p21, Fig. 60.38 — referenced but not on the pages supplied] The text describes it: the
**positive half-cycle of the input has been amplified more than the negative half-cycle**, so the
output waveshape differs from the input's. This is due to the appearance of **new frequencies
(harmonics)** at the output which were not present at the input.

> ⚠ ILLEGIBLE ·L7 p21 — Fig. 60.38 itself is on printed page 2302, absent from this PDF. Only the
> text description above is available.

[added] **Distinguishing the two categories in one line.** Non-linear distortion **creates new
frequencies**; linear distortion **only re-weights the ones already there**. That single test
separates them in any exam question.

---

## 7.24 The decibel ·L7 p22

> **Note on continuity.** Printed pages 2302–2306 (§60.32–60.39), which contain the *definition*
> of the decibel, are **not in this PDF**. Page 22 opens at item 2 of a list of decibel properties.

**Properties of the decibel** ·L7 p22

2. The decibel is **non-linear**: 20 dB is *not* twice as much power or voltage as 10 dB.
3. The log-based system compresses a huge range of power ratios into two-digit numbers — e.g.
   $1\ \mathrm{dB} = 1.26:1$ power ratio, while $50\ \mathrm{dB} = 100{,}000:1$.
4. The **total dB of a cascade is found by simply adding the stage dBs**.

[added] **The rule the whole topic depends on, stated once.** The decibel is defined on a **power**
ratio:

$$\boxed{\;G_p = 10\log_{10}\frac{P_2}{P_1}\ \mathrm{dB}\;}$$

For a **voltage** or **current** ratio into the *same* resistance, $P \propto V^2$, so the
logarithm picks up a factor of two:

$$\boxed{\;G_v = 20\log_{10}\frac{V_2}{V_1}\ \mathrm{dB}\qquad G_i = 20\log_{10}\frac{I_2}{I_1}\ \mathrm{dB}\;}$$

**So: $10\log$ for power, $20\log$ for voltage or current.** Every dB figure in this lesson obeys
this — $G_p = 10\log_{10}A_p$ ·L7 p15, $G_v = 20\log_{10}A_v$ ·L7 p15/p17/p18, and the feedback
factor in Example 62.8 ·L7 p7 (a voltage ratio, hence $20\log$).

### Value of 1 dB ·L7 p22

[eq: one-db-ratio]

$$1\ \mathrm{dB} = 10\log_{10}\frac{P_2}{P_1}
\quad\Longrightarrow\quad \log_{10}\frac{P_2}{P_1} = \frac{1}{10} = 0.1
\quad\Longrightarrow\quad \boxed{\;\frac{P_2}{P_1} = 10^{0.1} = 1.26\;}$$

Hence **+1 dB is an increase in power of 26%**. ·L7 p22

### Zero decibel reference level ·L7 p22

The decibel measures **no physical quantity** — only a **ratio** of two. To quote a *level* rather
than a *gain*, a reference power $P_0$ must be fixed, and levels are then $10\log_{10}(P_1/P_0)$ and
so on.

$P_0$ **cannot be 0 W**, because $10\log_{10}(P_1/0) = \infty$ — any power compared with zero power
is infinite. Decibels are simply undefined against a zero reference. ·L7 p22

**Three reference levels are in common use** ·L7 p22

| # | Reference | Corresponding reference voltage |
|---|---|---|
| 1 | 6 mW dissipated in **500 $\Omega$** | $6\times10^{-3} = V^2/500 \Rightarrow V = 1.73\ \mathrm V$ |
| 2 | 1 mW dissipated in **600 $\Omega$** | $1\times10^{-3} = V^2/600 \Rightarrow V = 0.774\ \mathrm V$ |
| 3 | **1 mW**, no specified impedance | written **dBm** |

[added] Both voltages verified: $\sqrt{6\times10^{-3}\times500} = 1.732$ V ✓;
$\sqrt{1\times10^{-3}\times600} = 0.7746$ V ✓.

[eq: dbm] The dBm reference **does not depend on any load impedance**, and levels are computed from
·L7 p22

$$\boxed{\;G_p = 10\log_{10}\frac{P_2}{0.001}\ \ \mathrm{dBm}\;}$$

> ⚠ VERIFY **C7.21** ·L7 p22 — the unit is printed "$\mathrm{dB_{in}}$". The line immediately
> above defines the abbreviation as **dBm** ("indicating that it uses 1 mW as a reference"). Read
> the subscript as m. See `_verification-log.md`.

---

## 7.25 Variation of amplifier gain with frequency ·L7 p22–p23

With the input voltage held constant and its frequency varied, the amplifier gain ·L7 p22

- (i) remains **practically constant** over a sizable range of **mid-frequencies**;
- (ii) **decreases** at low **and** at high frequencies.

Three frequency values matter: the **mid-frequency range**, the **lower cut-off frequency $f_1$**,
and the **upper cut-off frequency $f_2$**. ·L7 p22

### [def] The cut-off frequencies — three equivalent definitions ·L7 p23

The lower and upper cut-off frequencies are those frequencies:

[eq: half-power-voltage] **(a) In terms of voltage** — where the voltage gain falls to **0.707** of
the mid-frequency gain:

$$\boxed{\;A_v = \frac{1}{\sqrt2}A_{v(\text{mid})} = 0.707\,A_{v(\text{mid})}\;}$$

[eq: half-power-power] **(b) In terms of power** — where the power amplification falls to **half**
its mid-frequency value:

$$\boxed{\;A_{p.1} = A_{p.2} = \tfrac12 A_{p(\text{mid})}\;}$$

**(c) In terms of decibels** — where the **power gain falls by 3 dB**.

[added] The three are the same statement: $10\log_{10}(1/2) = -3.01$ dB, and
$20\log_{10}(0.707) = -3.01$ dB. The voltage falls by $\sqrt2$ precisely so that the power falls by
2.

That is why they are called ·L7 p23

- **–3 dB frequencies**, or
- **down 3 dB frequencies**, or
- **3 dB loss frequencies**.

The two points are the **3-dB points** (sometimes **minus 3 dB points**), marked **A** and **B** on
the figure. They are also called **roll-off frequencies**, because at them the gain starts rolling
down from its midband (maximum) value. ·L7 p23

[fig ·L7 p23, Fig. 60.43] Gain (vertical, labelled "Gain" with an upward magenta arrow) against
frequency $f$ (horizontal, magenta arrowhead). Two horizontal reference levels are ticked on the
vertical axis: **$A_{v.\text{mid}}$** at the top, and **$0.707\,A_{v.\text{mid}}$** below it, from
which a **dashed cyan horizontal line** runs right across the figure. A single magenta curve rises
from the lower left, flattens across the mid-band at $A_{v.\text{mid}}$, and falls at the right.
Solid dots mark where the curve crosses the 0.707 line — labelled **A** on the rising side and **B**
on the falling side. A short **double-headed vertical arrow** between the two levels is annotated
"**3 dB**". **Dashed cyan verticals** drop from A and B to the frequency axis at **$f_1$** and
**$f_2$**. Between them a long **double-headed horizontal arrow** is labelled "**Pass Band**".

[eq: bandwidth-def] **Bandwidth** ·L7 p23 — the frequency span between the two cut-offs is the
**passband** or **bandwidth**:

$$\boxed{\;\Delta f = f_2 - f_1 = \mathrm{BW} = \text{passband}\;}$$

> ⚠ VERIFY **C7.22** ·L7 p23 — printed "$f = f_2 - f_1 =$ band width (BW) = passband". The
> $\Delta$ has dropped out of the rendered glyph, leaving a plain $f$ on the left of an equation
> whose right-hand side is a *difference* of two $f$'s. Read as $\Delta f$. See
> `_verification-log.md`.

All frequencies between $f_1$ and $f_2$ are amplified almost equally. **For maximum bandwidth the
stray capacitances in the amplifier must be kept to a minimum.** ·L7 p23

---

## 7.26 Causes of amplifier gain variation ·L7 p23–p24

[def] The primary cause of gain variation is **capacitance** — some of it **in series** along the
signal path, some **in parallel** with it. ·L7 p23

| Type | Where | Typical size | Connected |
|---|---|---|---|
| **coupling and bypass** capacitors ($C_1$, $C_2$, $C_3$) | external to the device | **large** (µF) | **in series** with the signal path |
| **inter-element** capacitances ($C_{bc}$, $C_{be}$) | inside the transistor | **small** (pF) | **in parallel** (shunt) |
| **stray wiring** capacitance ($C_S$) | the layout | **small** (pF) | **in parallel** (shunt) |

[fig ·L7 p23, Fig. 60.44] Two circuits on one panel.
**(a)** A CE stage: a magenta sine source drives the base through the series coupling capacitor
$C_1$; the collector drives an output terminal through the series coupling capacitor $C_2$; the
emitter resistor is bypassed to ground by $C_3$. All three are drawn **in the signal path** or from
it to ground.
**(b)** The same transistor with its internal capacitances shown inside a **dashed magenta box**:
$C_{bc}$ from collector to base and $C_{be}$ from base to emitter; a magenta sine source drives the
base. On the output side, **$C_S$** (the stray wiring capacitance) is drawn from the collector node
to ground. These are all **shunt** elements.

**At mid-frequencies** ·L7 p23 — $C_1$, $C_2$, $C_3$ act almost as **shorts**, while $C_{bc}$ and
$C_{be}$ act as **opens**. Neither has any appreciable effect.

**At low frequencies** ·L7 p23 — the series-connected coupling and bypass capacitors offer
relatively **large reactance** and drop a large part of the signal, so the gain falls as frequency
is lowered.

**At high frequencies** ·L7 p24 — the small shunt capacitances, which were effective opens at low
frequency, have **falling reactance**; at very high frequencies they almost **short the signal to
ground** at both the input and output ends, so the gain falls.

**In summary** ·L7 p24

- (i) **series** coupling and bypass capacitors cause the **low-frequency** roll-off;
- (ii) **parallel** internal and stray capacitances cause the **high-frequency** roll-off.

[eq: lower-cutoff-rc] **Lower cut-off frequency contributed by one capacitor** ·L7 p24

$$\boxed{\;f_1 = \frac{1}{2\pi C R_{eq}}\;}$$

where $R_{eq}$ is the resistance **"seen" by that capacitor, looking both left and right**.

---

[ex 60.20 ·L7 p24] *For the RC-coupled circuit of Fig. 60.45, calculate the lower cut-off frequency*
*(i) at $C_1$ (ii) at $C_2$ and (iii) for the amplifier.*

[fig ·L7 p24, Fig. 60.45] A CE stage on a **20 V** rail. Divider **$R_1 = 90\ \mathrm K$** (rail to
base) and **$R_2 = 10\ \mathrm K$** (base to ground). Collector load **$R_C = 10\ \mathrm K$**.
Emitter resistor **$R_E = 1\ \mathrm K$** to ground. Signal source $V_S$ (circled sine, grounded)
behind **$R_S = 3\ \mathrm k$**, feeding the base through **$C_1 = 1\ \mu\mathrm F$**. The collector
drives **$R_L = 10\ \mathrm K$** (to ground) through **$C_2 = 0.2\ \mu\mathrm F$**; $v_o$ is taken
at that node. The transistor is marked **$\beta = 100$**.

### (i) $f_1$ at $C_1$ ·L7 p24

To find what $C_1$ sees, **short out the dc and ac sources** (they have negligible resistance).

[fig ·L7 p24, Fig. 60.46] The resulting equivalent: $C_1$ sits in the top horizontal wire. Hanging
from the node on its **left** is $R_S = 3\ \mathrm K$ to ground. Hanging from the node on its
**right** are three parallel branches to ground: $R_1$, $R_2$ and $r_{in(\text{base})}$.

$$R_{eq} = R_S + R_1 \,\|\, R_2 \,\|\, r_{in(\text{base})}$$

$$r_{in(\text{base})} = \beta_{\text{tr}}(r_e + R_E) \cong \beta_{\text{tr}}R_E = 100\times1\ \mathrm K = 100\ \mathrm K$$

$$R_{eq} = 3\ \mathrm K + 90\ \mathrm K \,\|\, 10\ \mathrm K \,\|\, 100\ \mathrm K = 3 + 8.26 = 11.26\ \mathrm K$$

$$f_1 = \frac{1}{2\pi\times11.26\times10^3\times1\times10^{-6}} = 14.1\ \mathrm{Hz}$$

> ⚠ VERIFY **V7.15** ·L7 p24 — part (i)'s answer is printed as **40 Hz**. With $R_{eq} = 11.26$ kΩ
> and $C_1 = 1\ \mu$F,
> $$f_1 = \frac{1}{2\pi(11{,}260)(10^{-6})} = 14.1\ \mathrm{Hz}$$
> The page contradicts itself: part (iii) states "cut-off for $C_1$ occurs way down at **14 Hz**".
> Correct form:
> $$\boxed{\;f_1\big|_{C_1} = 14.1\ \mathrm{Hz}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C7.23** ·L7 p24 — the resistance line is printed "$R_{er} = 3\mathrm K + \dots$"; the
> symbol defined and used everywhere else is $R_{eq}$. See `_verification-log.md`.

### (ii) $f_1$ at $C_2$ ·L7 p24

On one side $C_2$ sees $R_L = 10\ \mathrm K$ to ground; on the other it sees $R_C$ to ground in
parallel with the resistance looking into the collector. Since the collector–base junction is
reverse-biased its resistance is very high, so treat it as **open**.

[fig ·L7 p24, Fig. 60.47] The equivalent: $C_2$ in the top wire; on its **left** $R_C$ to ground,
drawn beside an **open switch symbol** (a small hinged line between two dots) representing the
open-circuited collector; on its **right** $R_L$ to ground.

$$R_{eq} = R_L + R_C = 10 + 10 = 20\ \mathrm K$$

$$f_1 = \frac{1}{2\pi\times20\times10^3\times0.2\times10^{-6}} = 39.8 \approx 40\ \mathrm{Hz}$$

> ⚠ VERIFY **V7.16** ·L7 p24 — part (ii)'s numerical answer is **missing from the page**: the line
> reads "$f_1 = \dfrac{1}{2\pi\times20\times10^3\times0.2\times10^{-6}} =$ **Hz**", with the
> number dropped. Correct value:
> $$\boxed{\;f_1\big|_{C_2} = 39.8\ \mathrm{Hz} \approx 40\ \mathrm{Hz}\;}$$
> See `_verification-log.md`.

### (iii) $f_1$ for the amplifier ·L7 p24

> ⚠ VERIFY **V7.17** ·L7 p24 — part (iii) is printed: "Since cut-off frequency for $C_2$ occurs at
> 40 Hz while cut-off for $C_1$ occurs way down at 14 Hz, $C_2$ determines the lower cut-off
> frequency for the amplifier i.e. **14 Hz**." The sentence contradicts itself — it names $C_2$ as
> the determining capacitor and then quotes $C_1$'s frequency. Correct form:
> $$\boxed{\;f_1(\text{amplifier}) = \max\{14.1,\ 39.8\} = 39.8\ \mathrm{Hz}\ \text{, set by } C_2\;}$$
> **Why the maximum, not the minimum:** each series capacitor is a high-pass section. Going down in
> frequency, the amplifier is already 3 dB down as soon as the **first** corner is met — which is
> the **highest** of the individual corner frequencies. See `_verification-log.md`.

[added] Full recomputation: $90\,\|\,10 = 9$ kΩ; $9\,\|\,100 = 8.257$ kΩ; $R_{eq} = 11.257$ kΩ;
$f_1|_{C_1} = 14.14$ Hz; $f_1|_{C_2} = 39.79$ Hz. **Amplifier $f_1 = 39.8$ Hz.** ✓

---

## 7.27 The Miller effect ·L7 p25

[def] **Miller effect** ·L7 p25 — viewed from the **input (base) terminal** of a CE-connected
transistor, the collector–base capacitance $C_{bc}$ appears **multiplied** by $(1+A_v)$. It is the
formal statement of the feedback from collector to base, and back, through $C_{bc}$.

### [derivation] Proof ·L7 p25

Apply $V_i$ to the base. The change in collector voltage is

$$\Delta V_C = -A_v V_i$$

the minus sign being the CE amplifier's inherent phase inversion. So while the base rises by $V_i$,
the collector **falls** by $A_v V_i$, and the total change in collector–base voltage is

$$\Delta V_{CB} = V_i + A_v V_i = V_i(1+A_v)$$

That is also the change across $C_{bc}$, since $C_{bc}$ is connected between collector and base.
Using $Q = CV$, the charge the input must supply is

$$Q = C_{bc}\,\Delta V_{CB} = C_{bc}(1+A_v)V_i = \left[(1+A_v)C_{bc}\right]V_i$$

[eq: miller-capacitance] Hence, looked at from the input, ·L7 p25

$$\boxed{\;C_{bc} \ \text{appears as}\ (1+A_v)\,C_{bc}\;}$$

[eq: miller-input-capacitance-bjt] **Total input capacitance of the transistor** ·L7 p25

$$\boxed{\;C_{in} = C_{be} \,\|\, (1+A_v)C_{bc} = C_{be} + (1+A_v)C_{bc}\;}$$

At high frequencies $C_{in}$ **reduces the input impedance** of the circuit and so shapes the
frequency response. ·L7 p25

[added] Note the "$\|$" and the "$+$" in the same line: capacitors **in parallel add**, so the two
notations agree.

---

[ex 60.21 ·L7 p25] *A CE-connected amplifier has $C_{bc} = 4$ pF, $C_{be} = 10$ pF and*
*$r_e = 50\ \Omega$. If the circuit load resistor is 10 K, calculate $C_{in}$.*

$$A_v \cong \frac{R_L}{r_e} = \frac{10\ \mathrm k\Omega}{50\ \Omega} = 200$$

$$C_{in} = C_{be} + (1+A_v)C_{bc} = 10 + (1+200)\times4 = 10 + 804 = 814\ \mathrm{pF}$$

> ⚠ VERIFY **V7.18** ·L7 p25 — printed as
> $A_v \cong \dfrac{\mathbf{R_E}}{r_e} = \dfrac{\mathbf{100\ K}}{50\ \Omega} = 200$.
> Two faults on one line: the numerator symbol should be $R_L$ (the question says "circuit **load**
> resistor"; $R_E$ is nowhere in the problem), and the value should be **10 K** as given, not
> 100 K. As printed the quotient is $100{,}000/50 = 2000$, ten times the printed answer.
> Correct form:
> $$\boxed{\;A_v \cong \frac{R_L}{r_e} = \frac{10\ \mathrm{k}\Omega}{50\ \Omega} = 200\;}$$
> The answer $C_{in} = 814$ pF is right, because it uses the correct $A_v = 200$. See `_verification-log.md`.

[added] **The size of the effect.** $C_{bc}$ is 4 pF; it appears as 804 pF — **201 times larger**,
and it swamps the 10 pF of $C_{be}$ completely. That is why the Miller effect, and not $C_{be}$,
sets the high-frequency limit of a CE stage.

---

[ex 60.22 ·L7 p25] *Calculate the upper cut-off frequency of the CE amplifier of Fig. 60.48. Given*
*input wiring capacitance $C_{wi} = 40$ pF, $C_{bc} = 8$ pF, $C_{be} = 10$ pF and $\beta = 100$.*
(Electronic Engg-I, Osmania Univ.)

[fig ·L7 p25, Fig. 60.48] A CE stage on a **20 V** rail. Divider **$R_1 = 45\ \mathrm K$** (rail to
base) and **$R_2 = 5\ \mathrm K$** (base to ground). Collector load **$R_C = 20\ \mathrm K$**;
output $v_o$ through a coupling capacitor to **$R_L = 20\ \mathrm K$** to ground. Emitter resistor
**$R_E = 400\ \Omega$** to ground. Source $V_S$ (circled sine, grounded) behind
**$R_S = 10\ \mathrm K$**, feeding the base through **$C_1$**. The transistor's internal
capacitances are drawn on it: **$C_{bc}$** from collector to base, **$C_{be}$** from base to
emitter. Marked **$\beta = 100$**.

[eq: upper-cutoff-rc] ·L7 p25

$$\boxed{\;f_2 = \frac{1}{2\pi R_{eq}C_{in}}\;}$$

$$A_v \cong \frac{R_C \,\|\, R_L}{R_E} = \frac{20\ \mathrm K \,\|\, 20\ \mathrm K}{400\ \Omega} = \frac{10{,}000}{400} = 25$$

$$C_{in} = C_{wi} + C_{be} + (1+A_v)C_{bc} = 40 + 10 + (1+25)\times8 = 258\ \mathrm{pF}$$

Looking **right** from $C_{in}$ one sees $\beta(r_e+R_E) \cong \beta R_E$; looking **left** one sees
$R_1 \,\|\, R_2 \,\|\, R_S$ — all in parallel:

$$R_{eq} = R_1 \,\|\, R_2 \,\|\, R_S \,\|\, \beta R_E = 45\ \mathrm K \,\|\, 5\ \mathrm K \,\|\, 10\ \mathrm K \,\|\, 40\ \mathrm K = 2.88\ \mathrm K$$

$$f_2 = \frac{1}{2\pi\times2.88\times10^3\times258\times10^{-12}} = 214\ \mathrm{kHz}$$

> ⚠ VERIFY **V7.19** ·L7 p25 — the gain line is printed
> $A_v \cong \dfrac{R_C \| R_L}{\mathbf{R_L}} = \dfrac{20\mathrm K\|20\mathrm K}{400\ \Omega} = 25$.
> The denominator symbol must be **$R_E$** — the 400 $\Omega$ used is the emitter resistor;
> $R_L$ is 20 K and already appears in the numerator, making the expression self-referential
> ($R_C\|R_L$ over $R_L$ would be 0.5, not 25). Correct form:
> $$\boxed{\;A_v \cong \frac{R_C \,\|\, R_L}{R_E} = \frac{10\ \mathrm{k}\Omega}{400\ \Omega} = 25\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **C7.24** ·L7 p25 — the question lists "$C_b = 10$ pF"; the quantity used in the
> solution, and defined in §60.44, is $C_{be}$. Missing subscript. See `_verification-log.md`.

[added] Every number verified: $\beta R_E = 40$ kΩ; $R_{eq} = (1/45+1/5+1/10+1/40)^{-1} = 2.880$ kΩ
exactly; $C_{in} = 258$ pF; $f_2 = 214.19$ kHz. ✓

---

## 7.28 Cut-off frequencies of cascaded amplifiers ·L7 p25–p26

[def] Cascading gives higher amplification but a **narrower bandwidth**, because the product of the
two stays almost constant. ·L7 p25

For $n$ **identical** stages: ·L7 p26

[eq: cascade-lower-cutoff]

$$\boxed{\;f_{1.n} = 1.1\sqrt{n}\times f_{1\,\text{per stage}} = \frac{f_{1\,\text{per stage}}}{\sqrt{2^{1/n}-1}}\;}$$

[eq: cascade-upper-cutoff]

$$\boxed{\;f_{2.n} = \frac{f_{2\,\text{per stage}}}{1.1\sqrt{n}} = \sqrt{2^{1/n}-1}\times f_{2\,\text{per stage}}\;}$$

The reduced bandwidth of the cascade is $f_{2.n} - f_{1.n}$. ·L7 p26

[added] **The two forms agree, and the $1.1\sqrt n$ version is the approximation.** The exact
**bandwidth-shrinkage factor** is $\sqrt{2^{1/n}-1}$:

| $n$ | $\sqrt{2^{1/n}-1}$ (exact) | $1/(1.1\sqrt n)$ (approx.) |
|---|---|---|
| 1 | 1.000 | 0.909 |
| 2 | 0.644 | 0.643 |
| 3 | 0.510 | 0.525 |
| 4 | 0.435 | 0.455 |

The approximation is excellent at $n=2$ and adequate to $n=4$; it is **not** valid at $n=1$, where
the exact factor must be 1 by definition. Use the $\sqrt{2^{1/n}-1}$ form when a question gives a
specific $n$.

[added] **What the shrinkage means physically.** Two identical stages each flat to 20 kHz do *not*
give a cascade flat to 20 kHz — the cascade is 3 dB down at $0.64\times20 = 12.8$ kHz, because each
stage is already 1.5 dB down there and the losses add in decibels.

---

## 7.29 Transistor cut-off frequencies ·L7 p26

Even with **no external stray capacitance** there is still an upper limit on frequency response, due
to ·L7 p26

- (i) the **internal (inter-element) capacitances** of the transistor, and
- (ii) the **transit time** of charge carriers across the junctions and through the semiconductor.

This limitation is expressed as the **alpha cut-off frequency $f_\alpha$** and the **beta cut-off
frequency $f_\beta$**.

**Symbols** [table]

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $f_\alpha$ | alpha cut-off frequency (CB) | Hz | 8–345 MHz |
| $f_\beta$ | beta cut-off frequency (CE) | Hz | 0.1–6 MHz |
| $f_T$ | frequency at which $\beta$ falls to unity | Hz | 6–300 MHz |
| $\alpha$ | CB current gain $I_C/I_E$ | dimensionless | 0.95–0.995 |
| $\beta$ | **CE current gain** $I_C/I_B$ (⚠ not the feedback fraction) | dimensionless | 50–300 |

### [def] Alpha cut-off frequency ·L7 p26

At high frequencies the transistor's $\alpha$ begins to fall, because of the **transit time** of the
carriers moving from emitter to collector. $f_\alpha$ is the high frequency at which the $\alpha$ of
a **CB**-connected transistor becomes **0.707** of its low-frequency (usually 1 kHz) value.

[eq: alpha-cutoff] **The worked illustration** ·L7 p26 — if $\alpha$ at 1 kHz is 0.98, then at
$f_\alpha$:

$$\alpha(f_\alpha) = 0.707\times0.98 = 0.693$$

so at $f_\alpha$ the collector current is only $0.693\,I_E$ instead of $0.98\,I_E$.

$f_\alpha$ is ·L7 p26

- (a) **inversely proportional to the square of the base width**;
- (b) **directly proportional to the minority-carrier mobility**.

NPN transistors are therefore superior to PNP, because **electrons have greater mobility than
holes**; and to reduce base transit time the base should be **as thin as possible**. ·L7 p26

### [def] Beta cut-off frequency ·L7 p26

The high frequency at which the $\beta$ of a **CE**-connected transistor drops to **0.707** of its
low-frequency (1 kHz) value.

$f_\alpha$ of any given transistor is **always greater** than its $f_\beta$; in fact ·L7 p26

$$f_\alpha \cong \beta f_\beta$$

### [def] $f_T$ ·L7 p26

The high frequency of a CE-connected transistor at which its $\beta$ **drops to unity**. It is much
larger than $f_\beta$ but less than $f_\alpha$. Typical values for one transistor:
$f_\beta = 6$ MHz, $f_T = 300$ MHz, $f_\alpha = 345$ MHz. ·L7 p26

### Relations between $f_\alpha$, $f_\beta$ and $f_T$ ·L7 p26

[eq: falpha-ft] [eq: fbeta-ft]

$$\boxed{\;f_\alpha = 1.2\,f_T\qquad\text{and}\qquad f_\beta = \frac{f_T}{\beta}\;}$$

where $\beta$ is the **low-frequency** value of the transistor current gain.

> ⚠ VERIFY **C7.26** ·L7 p26 — the section heading prints "Relation Between $f_a$, $f_b$ and
> $f_T$" with Latin **a** and **b** where the body text uses Greek $\alpha$ and $\beta$. Cosmetic
> substitution in the heading font. See `_verification-log.md`.

[added] **Internal consistency check on the quoted typical values.** From $f_\beta = f_T/\beta$ with
$f_T = 300$ MHz and $f_\beta = 6$ MHz, $\beta = 50$. Then $f_\alpha \cong \beta f_\beta = 300$ MHz,
while $f_\alpha = 1.2f_T = 360$ MHz. The quoted 345 MHz sits between the two estimates — the
relations are approximations, and the page presents them as such.

### [def] Gain–bandwidth product ·L7 p26–p27

[eq: gbp-ft] The product of gain and bandwidth. **For any amplifier the GBP is constant and equal to
$f_T$.** ·L7 p26

$$\boxed{\;\text{GBP} = \text{gain}\times\text{bandwidth} = f_T\;}$$

If, for example, $\beta = 1$ at 6 MHz, then $f_T = 6$ MHz and the GBP is 6 MHz. ·L7 p27

**Consequence.** For a given $f_T$, **increased gain is obtainable only at the expense of
bandwidth**. ·L7 p27

---

[ex 60.23 ·L7 p27] *A transistor has $f_\alpha = 8$ MHz and $\beta = 80$. Connected as an amplifier*
*it has a stray capacitance of 100 pF at the output terminal. Calculate its upper 3 dB frequency when*
*$R_L$ is (a) 10 K and (b) 100 K.*

**Principle** ·L7 p27 — the stray capacitance costs 3 dB when its **reactance equals the output
resistance**:

$$\frac{1}{2\pi f_S C_S} = R_L \quad\Longrightarrow\quad f_s = \frac{1}{2\pi C_S R_L}$$

First find $f_\beta$ for comparison with $f_s$:

$$f_\beta = \frac{f_\alpha}{\beta} = \frac{8\ \mathrm{MHz}}{80} = 100\ \mathrm{kHz}$$

> ⚠ VERIFY **V7.20** ·L7 p27 — printed as $f_\beta = \dfrac{\mathbf{f_1}}{80} = \dfrac{8\ \mathrm{MHz}}{80}$.
> The symbol $f_1$ is the **lower cut-off frequency** throughout this chapter (§60.42, §60.45,
> Ex 60.20). The quantity divided here is the **alpha cut-off frequency** $f_\alpha = 8$ MHz, the
> only 8 MHz in the problem. Correct form:
> $$\boxed{\;f_\beta = \frac{f_\alpha}{\beta} = \frac{8\ \mathrm{MHz}}{80} = 100\ \mathrm{kHz}\;}$$
> This is $f_\alpha \cong \beta f_\beta$ rearranged. See `_verification-log.md`.

> ⚠ VERIFY **C7.25** ·L7 p27 — the answer is printed "=100 **kHZ**" — capital Z. See
> `_verification-log.md`.

**(a) $R_L = 10$ K** ·L7 p27

$$f_s = \frac{1}{2\pi C_S R_L} = \frac{1}{2\pi\times100\times10^{-12}\times10\times10^3} = 159\ \mathrm{kHz}$$

Cut-off would have been reached at $f_\beta = 100$ kHz **before** 159 kHz. Hence

$$f_2 = f_\beta = 100\ \mathrm{kHz}$$

**(b) $R_L = 100$ K** ·L7 p27

$$f_s = \frac{10}{100}\times159 = 15.9\ \mathrm{kHz}$$

Cut-off is reached **much earlier**, at 15.9 kHz, before $f_\beta$. Hence

$$f_2 = 15.9\ \mathrm{kHz}$$

[added] Both verified: $1/(2\pi\times100\ \mathrm{pF}\times10\ \mathrm{k}\Omega) = 159.15$ kHz;
$1/(2\pi\times100\ \mathrm{pF}\times100\ \mathrm{k}\Omega) = 15.92$ kHz. ✓

[added] **The method in one sentence, because it is the examinable part:** compute *both* candidate
limits — the transistor's own $f_\beta$ and the circuit's $f_s$ — and take the **lower** of the two,
because whichever rolls off first sets the amplifier's upper cut-off.

---

## 7.30 Tutorial Problems No. 60.1 ·L7 p27

The source gives seven problems with answers but no working. Each is transcribed as printed, then
solved in an `[added]` block. **The solutions below are not the lecturer's.**

---

[exercise 60.1 Q1 ·L7 p27] *An amplifier raises the power level of its 5-$\mu$W input signal by*
*30 dB. What is the output power?* **[5 mW]**

[added] **Solution.** 30 dB on a **power** ratio is $10^{30/10} = 1000$:

$$P_{out} = 5\ \mu\mathrm W \times 1000 = 5000\ \mu\mathrm W = \boxed{5\ \mathrm{mW}}$$

Agrees with the printed answer. ✓

---

[exercise 60.1 Q2 ·L7 p27] *An attenuation network provides an output of 5 $\mu$W with an input of*
*5 mW. Calculate the decibel loss of the network.* **[–30 dB]**

[added] **Solution.** Power ratio, so $10\log$:

$$G_p = 10\log_{10}\frac{5\times10^{-6}}{5\times10^{-3}} = 10\log_{10}(10^{-3}) = \boxed{-30\ \mathrm{dB}}$$

Agrees. ✓ (The exact inverse of Q1, as intended.)

---

[exercise 60.1 Q3 ·L7 p27] *What is the decibel difference between a 100 kW and a 500 kW radio*
*transmitter?* **[6.98 dB]**

[added] **Solution.**

$$\Delta G = 10\log_{10}\frac{500}{100} = 10\log_{10}5 = \boxed{6.99\ \mathrm{dB}}$$

The printed 6.98 dB is a rounding of 6.990. ✓

---

[exercise 60.1 Q4 ·L7 p27] *The noise level of a certain tape recording is 30 dB below the signal*
*level. If the signal power is 5 mW, calculate the noise power.* **[5 mW]**

[added] **Solution.** 30 dB below on a power basis is a factor $10^{-3}$:

$$P_{noise} = \frac{5\ \mathrm{mW}}{1000} = \boxed{5\ \mu\mathrm W}$$

> ⚠ VERIFY **V7.21** ·L7 p27 — the printed answer key gives **[5 mW]**, which is the *signal*
> power, not the noise power — it would mean the noise is 0 dB below the signal, contradicting the
> question. Correct answer: **5 $\mu$W**. (Compare Q1, whose answer key correctly applies the same
> factor of 1000 in the other direction.) See `_verification-log.md`.

---

[exercise 60.1 Q5 ·L7 p27] *An amplifier rated at 72-W output is connected to an 8 $\Omega$ speaker.*
*(a) what input power is required for full power output if power gain is 30 dB, (b) what is the*
*input voltage for rated output if amplifier voltage gain is 40 dB.* **[(a) 72 $\mu$W (b) 240 mV]**

[added] **Solution (a).** 30 dB power gain is a factor 1000:

$$P_{in} = \frac{72\ \mathrm W}{1000} = 0.072\ \mathrm W = \boxed{72\ \mathrm{mW}}$$

> ⚠ VERIFY **V7.22** ·L7 p27 — the printed answer key gives **[72 $\mu$W]**, which is out by a
> factor of 1000. $72\ \mu$W would require a power gain of $10\log_{10}(72/72\times10^{-6}) = 60$
> dB, not 30 dB. Correct answer: **72 mW**. See `_verification-log.md`.

[added] **Solution (b).** Output voltage across the 8 $\Omega$ speaker at 72 W:

$$V_{out} = \sqrt{P R_L} = \sqrt{72\times8} = \sqrt{576} = 24\ \mathrm V$$

40 dB voltage gain is a factor $10^{40/20} = 100$:

$$V_{in} = \frac{24\ \mathrm V}{100} = \boxed{0.24\ \mathrm V = 240\ \mathrm{mV}}$$

Agrees with the printed answer. ✓ Note (a) used $10\log$ and (b) used $20\log$ — the same problem
exercises both conversions deliberately.

---

[exercise 60.1 Q6 ·L7 p27] *The characteristics of a certain audio amplifier are such that it gives*
*a voltage amplification of 10 at 100 Hz, 30 at 3 kHz and 60 at 10 kHz. Taking the amplification at*
*3 kHz as the reference level, calculate the loss or gain in decibels at the other two frequencies.*
**[–9.54 dB, 6.02 dB]**

[added] **Solution.** Voltage ratios, so $20\log$, referred to $A = 30$:

$$\text{At 100 Hz:}\quad 20\log_{10}\frac{10}{30} = 20\log_{10}(0.3333) = \boxed{-9.54\ \mathrm{dB}}$$

$$\text{At 10 kHz:}\quad 20\log_{10}\frac{60}{30} = 20\log_{10}2 = \boxed{+6.02\ \mathrm{dB}}$$

Both agree. ✓ The 6.02 dB is the classic "doubling the voltage is +6 dB" result.

---

[exercise 60.1 Q7 ·L7 p27] *An amplifier with full power rating of 100 W drives a speaker load of*
*16 $\Omega$. The hum-level rating of the amplifier is 80 dB below its full-power rating. Calculate*
… **[question truncated]**

> ⚠ ILLEGIBLE ·L7 p27 — Q7 is **cut off after the word "Calculate"** at the bottom of the page;
> the quantities asked for and the answer key are on printed page 2313, which is not in this PDF.
> Needs a screenshot of that page.

[added] **Partial solution** — for the two quantities such a question conventionally asks:

$$P_{hum} = \frac{100\ \mathrm W}{10^{80/10}} = \frac{100}{10^8} = 1\times10^{-6}\ \mathrm W = 1\ \mu\mathrm W$$

$$V_{hum} = \sqrt{P_{hum}R_L} = \sqrt{1\times10^{-6}\times16} = 4\times10^{-3}\ \mathrm V = 4\ \mathrm{mV}$$

Equivalently, from the full-power output voltage $\sqrt{100\times16} = 40$ V, an 80 dB voltage
reduction is a factor $10^{80/20} = 10^4$, giving $40/10^4 = 4$ mV — the same answer, and a check
that the $10\log$ / $20\log$ conversions were used consistently. These are **not** the source's
answers; they are supplied here.

---

## 7.31 What to carry into the exam ·L7 p1–p27

[added] The equations most likely to be needed, gathered.

**Feedback**

$$A_f = \frac{A}{1 \pm \beta A}\qquad (+ \text{ is negative feedback})$$

$$A_f \cong \frac{1}{\beta}\ \ (\beta A \gg 1)\qquad S = \frac{A}{A'} = 1+\beta A$$

$$\frac{dA'}{A'} = \frac{1}{1+\beta A}\frac{dA}{A}\qquad D' = \frac{D}{1+\beta A}$$

$$f_1' = \frac{f_1}{1+\beta A}\qquad f_2' = f_2(1+\beta A)\qquad A\cdot BW = A'\cdot BW'$$

$$R_i' = R_i(1+\beta A)\ \text{(series)}\qquad R_o' = \frac{R_o}{1+\beta A}\ \text{(voltage-sampled)}$$

**Feedback fractions of the standard circuits**

$$\beta = \frac{R_1}{R_1+R_2}\ \text{(voltage-series divider)}\qquad
\beta = \frac{R_E}{R_C}\ \text{(current-series)}\qquad
\beta = \frac{R_C}{R_F}\ \text{(voltage-shunt)}$$

**Cascades and decibels**

$$A_v = A_{v1}A_{v2}\dots\qquad G = G_1+G_2+\dots$$

$$G_v = 20\log_{10}A_v\qquad G_p = 10\log_{10}A_p$$

**Frequency response**

$$\Delta f = f_2 - f_1\qquad A(f_1) = A(f_2) = 0.707\,A_{\text{mid}} \equiv -3\ \mathrm{dB}$$

$$f_1 = \frac{1}{2\pi C R_{eq}}\qquad f_2 = \frac{1}{2\pi R_{eq}C_{in}}$$

$$C_{in} = C_{be} + (1+A_v)C_{bc}\ \ (+\,C_{wi}\ \text{if wiring capacitance is given})$$

$$f_{1.n} = \frac{f_1}{\sqrt{2^{1/n}-1}}\qquad f_{2.n} = \sqrt{2^{1/n}-1}\;f_2$$

$$f_\alpha \cong \beta f_\beta \qquad f_\beta = \frac{f_T}{\beta}\qquad f_\alpha = 1.2f_T\qquad \text{GBP} = f_T$$

**Three traps, in order of how often they cost marks**

1. **$\beta$**: feedback fraction here, transistor current gain in Lesson 3 — and both appear on
   ·L7 p11.
2. **$10\log$ versus $20\log$**: power takes 10, voltage and current take 20. The feedback factor
   $\beta A$ is a voltage ratio, so it takes 20 (·L7 p7, Example 62.8).
3. **The amplifier's lower cut-off is the *highest* of the individual capacitor corners**, and its
   upper cut-off is the *lowest* of the candidate high-frequency limits. Example 60.20 ·L7 p24 gets
   this wrong in print — see V7.17.

---

## 7.32 Verification flags in this file — summary

**22 substantive (V7.x) · 26 cosmetic (C7.x) · 48 total.** Full entries in
`_verification-log.md`; each is flagged inline at the point of use above.

| ID | Page | One line |
|---|---|---|
| **V7.1** | p4 | Ex 62.2's second part is solved with Example 62.3's data |
| **V7.2** | p4 | Ex 62.4 asks for the fall in gain "without feedback"; the solution gives it with feedback |
| **V7.3** | p6 | both cascade gains labelled $A_1$; the second is $A_2$ |
| **V7.4** | p6 | equal-gain condition printed $(1-1\beta)^n$; should be $(1+A\beta_1)^n$ |
| **V7.5** | p7 | Ex 62.8: $63/7.3$ printed as 6.63; it is 8.63 (the printed 18.72 dB proves it) |
| **V7.6** | p8 | GBP identity printed $A(f_2-f_1')=A(f_2'-f_1')$; should be $A(f_2-f_1)=A'(f_2'-f_1')$ |
| **V7.7** | p9 | $f_2' = f_0(\dots) = 100$ **Hz**; should be $f_2(\dots) = 100$ **kHz** |
| **V7.8** | p12 | Ex 62.14: $A' = 400/(1+400)$; should be $400/(1+40)$ |
| **V7.9** | p12 | §62.11 text says feedback is coupled through $R_E$; it is $R_F$ |
| **V7.10** | p12 | Fig. 62.11 labels the output terminal $V_i$; should be $V_o$ |
| **V7.11** | p17–18 | "$r_{e.2} = a^2R_7$"; that quantity is $r_{o.2}$ |
| **V7.12** | p17 | low-frequency loss attributed to "large capacitance"; it is large **reactance** |
| **V7.13** | p18 | Ex 61.5(ii): numerator printed $25\times100$; should be $25\times10^3$ |
| **V7.14** | p19 | Ex 61.6: $N_p$ printed 632 and "7:1"; correct 200 and 2.24:1 |
| **V7.15** | p24 | Ex 60.20(i): printed 40 Hz; correct 14.1 Hz |
| **V7.16** | p24 | Ex 60.20(ii): the numerical answer is missing; it is 39.8 Hz |
| **V7.17** | p24 | Ex 60.20(iii): self-contradictory; the amplifier's $f_1$ is 39.8 Hz, set by $C_2$ |
| **V7.18** | p25 | Ex 60.21: $A_v = R_E/r_e = 100\mathrm K/50\Omega$; should be $R_L/r_e = 10\mathrm K/50\Omega$ |
| **V7.19** | p25 | Ex 60.22: denominator labelled $R_L$; the 400 $\Omega$ used is $R_E$ |
| **V7.20** | p27 | Ex 60.23: $f_\beta = f_1/80$; should be $f_\alpha/80$ |
| **V7.21** | p27 | Tutorial Q4 answer key [5 mW]; correct 5 $\mu$W |
| **V7.22** | p27 | Tutorial Q5(a) answer key [72 $\mu$W]; correct 72 mW |

| ID | Page | One line |
|---|---|---|
| **C7.1** | p2 | Fig. 62.2 caption "Feeback Loop" |
| **C7.2** | p4 | Ex 62.1(c): "251 **mA**"; it is 251 mV |
| **C7.3** | p4 | Ex 62.4: $400/4.2$ printed 95.3 (95.24); fall printed 4.7% (4.76%) |
| **C7.4** | p5 | "$\beta x D_A$" — the $A$ is a factor, not a subscript |
| **C7.5** | p7 | Ex 62.9: solution's (a)/(b) labels swapped relative to the question |
| **C7.6** | p7 | Ex 62.9: statement gives $-150$, solution uses $+150$ without comment |
| **C7.7** | p8 | Ex 62.12: a voltage gain given the unit "Hz" |
| **C7.8** | p9 | bandwidth written $dW$, $dW'$ |
| **C7.9** | p12 | Ex 62.14: "$20+1000$" where $r_e = 25\ \Omega$ |
| **C7.10** | p12 | Ex 62.15 asks for "$I_{o(\text{stage})}$"; it is $r_{o(\text{stage})}$ |
| **C7.11** | p13 | Ex 62.15: $7360/819$ printed 8.9; it is 8.99 |
| **C7.12** | p15 | Fig. 61.1: stage-2 input labelled $v_{o2}$; should be $v_{i2}$ |
| **C7.13** | p16 | the two photograph captions are swapped |
| **C7.14** | p17 | "BC coupling" for RC coupling |
| **C7.15** | p17 | Fig. 61.13 horizontal axis labelled $t$; it is $f$ |
| **C7.16** | p17 | "gain drops **of** again" |
| **C7.17** | p18 | "$A_{e.2}$" for $A_{v.2}$ |
| **C7.18** | p18 | Ex 61.5(i): $27{,}750/33.3 = 833$, printed 830 |
| **C7.19** | p19 | "$k\times12^2$" for $k\times1^2$; spurious "$\times5$" in the $N_p$ line |
| **C7.20** | p20 | "Because of **his** distortion" |
| **C7.21** | p22 | "dB$_{in}$" for dBm |
| **C7.22** | p23 | "$f = f_2-f_1$" — the $\Delta$ has dropped out |
| **C7.23** | p24 | "$R_{er}$" for $R_{eq}$ |
| **C7.24** | p25 | "$C_b$" for $C_{be}$ |
| **C7.25** | p27 | "kHZ" |
| **C7.26** | p26 | heading uses Latin $f_a$, $f_b$ for $f_\alpha$, $f_\beta$ |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
