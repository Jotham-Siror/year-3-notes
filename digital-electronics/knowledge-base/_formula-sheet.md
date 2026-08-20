---
kb: "Digital Electronics — BEE 3102"
lecturer: "withheld"
file_role: formula-sheet
purpose: "Every equation in the unit, in corrected form, tagged to its source slide. Corrections are marked; the printed version is given alongside so it is recognisable in an exam."
---

# Formula sheet — Digital Electronics (BEE 3102)

Every equation below is the **corrected** form. A ⚠ marks one the deck prints differently: the
corrected form is boxed, and the line beneath gives what the slide actually prints, with the flag ID.
Recognise the printed version — it is the one that will appear on an examination paper.

Handout codes: **CH1**–**CH6** are the six chapter decks; **EXC** is the one-page excitation-table
handout. Symbol clashes are catalogued in `_nomenclature.md`; the two that change answers are the
$2^{n}$ / $2^{n}-1$ split (§4) and the bit-numbering in the R/2R formula (§5).

---

## 0 · Scaling laws and recap timing

·CH1. Four relations; the flip-flop equations CH1 introduces are collected in §6 instead.

**Moore's Law** — transistor density on a chip doubles every 18 months. The deck states it in words
only, so the growth law is supplied.

$$\boxed{\;N(t) = N_0\,2^{\,t/T_M}, \qquad T_M = 1.5\ \text{years}\;}$$

- $N(t)$ — transistors per integrated circuit at time $t$ (count)
- $N_0$ — transistors per integrated circuit at the reference time (count)
- $t$ — time elapsed from the reference, in years
- $T_M$ — Moore doubling period, 1.5 years

[eq: moores-law] [added] ·CH1 slide 3

**Rock's Law** — the capital cost of the plant needed to build them doubles every four years.

$$\boxed{\;C(t) = C_0\,2^{\,t/T_R}, \qquad T_R = 4\ \text{years}\;}$$

- $C(t)$ — capital cost of a fabrication plant at time $t$ (currency)
- $C_0$ — that cost at the reference time (currency)
- $T_R$ — Rock doubling period, 4 years

[eq: rocks-law] [added] ·CH1 slide 3

**Ripple-counter settling time** — how long a change takes to reach the last stage of an
asynchronous counter. This is the architecture's defining weakness: the time grows linearly with
word length.

$$\boxed{\;t_{pd,\text{total}} = n\,t_{pd}\;}$$

- $n$ — number of stages the change ripples through (count)
- $t_{pd}$ — clock-to-output delay of one stage, in s; the deck's figure is 1 ns, giving 3 ns for
  three stages

[eq: ripple-counter-total-delay] ·CH1 slide 19

**Serial load time of a shift register** — how many clock pulses it takes to load a word one bit at
a time.

$$\boxed{\;N_{\text{shift}} = n\;}$$

- $n$ — word length in bits; the pattern is irrelevant, one pulse per bit

[eq: shift-register-load-time] [added] ·CH1 slide 16

**Also in CH1:** the D and JK characteristic equations, tagged [eq: d-flip-flop-characteristic]
·CH1 slide 12 and [eq: jk-flip-flop-characteristic] ·CH1 slide 18. Both are given in §6, where the
full set lives.

---

## 1 · Logic-family characteristics

·CH2. Seven equations, all off slides 10 to 15.

### The six logic levels

Not equations, but nothing in this section parses without them. The ordering
$V_{OL} < V_{IL} < V_{IH} < V_{OH}$ is what makes both noise margins positive.

| Symbol | Meaning | Units | TTL | +5 V CMOS |
|---|---|---|---|---|
| $V_H$ | nominal HIGH at the **output** | V | 3.4 | — |
| $V_L$ | nominal LOW at the **output** | V | 0.2 | — |
| $V_{IH}$ | minimum input voltage read as HIGH | V | 2.0 | 3.5 |
| $V_{IL}$ | maximum input voltage read as LOW | V | 0.8 | 1.5 |
| $V_{OH}$ | guaranteed output for an input of $V_{IL}$ | V | 2.4 min | 4.4 |
| $V_{OL}$ | guaranteed output for an input of $V_{IH}$ | V | 0.4 max | 0.33 |

⚠ **The slide prints** (V02-2): $V_L$ as the low-logic voltage "**at the input** of a logic gate for
$v_i = V_H$". $V_L$ is an **output** level — the entry one line below it, for $V_H$, says "at the
output" correctly ·CH2 slide 8.

$V_{IL}$ and $V_{IH}$ are not chosen: they are the inputs at which the transfer characteristic has
slope $-1$ ·CH2 slide 8.

### Propagation delay

**The 50% reference level** — propagation delay is measured between the 50% point of the input edge
and the 50% point of the output edge, so the level has to be fixed first.

$$V_{50\%} = \frac{V_H + V_L}{2}$$

- $V_{50\%}$ — mid-swing reference level, in V

[eq: fifty-percent-point] ·CH2 slide 10

**Rise- and fall-time reference levels** — rise and fall are read between 10% and 90% of the swing,
*not* at 50%.

$$V_{10\%} = V_L + 0.1\,\Delta V$$

$$V_{90\%} = V_L + 0.9\,\Delta V = V_H - 0.1\,\Delta V$$

- $\Delta V$ — logic swing $V_H - V_L$, in V
- $t_r$ — rise time, 10% to 90%, in s; $t_f$ — fall time, 90% to 10%, in s

[eq: rise-fall-reference-levels] ·CH2 slide 14

**Average propagation delay** — the two edges are not equally fast, so one averaged figure is quoted.

$$\boxed{\;\tau_P = \frac{\tau_{PHL} + \tau_{PLH}}{2}\;}$$

- $\tau_{PHL}$ — delay with the **output** going HIGH to LOW, in s
- $\tau_{PLH}$ — delay with the **output** going LOW to HIGH, in s
- $\tau_P$ — average propagation delay, in s; typically 10 ns

[eq: average-propagation-delay] ·CH2 slide 10

⚠ **The slide prints** (V02-3) the two parenthetical glosses **interchanged** — "$\tau_{PHL}$, delay
time in going from logical 0 to logical 1 state (LOW to HIGH)" and the mirror image for
$\tau_{PLH}$. Read the subscripts, not the words: the waveform beside them marks $\tau_{PHL}$ on the
falling output edge ·CH2 slide 10.

### Noise margins

How much noise an input can carry before the receiving gate misreads it. Defined separately at the
two levels, and both must be positive.

$$\boxed{\;NM_L = V_{IL} - V_{OL}\;}$$

$$\boxed{\;NM_H = V_{OH} - V_{IH}\;}$$

- $NM_L$ — low-level noise margin, in V; the deck also calls it $V_{NL}$
- $NM_H$ — high-level noise margin, in V; also $V_{NH}$

[eq: noise-margin-low], [eq: noise-margin-high] ·CH2 slide 12 · both names on ·CH2 slide 13 (C02-1)

Worked values ·CH2 slide 13 — TTL: $NM_H = 2.4 - 2.0 = 0.4$ V and $NM_L = 0.8 - 0.4 = 0.4$ V.
5 V CMOS: $NM_H = 4.4 - 3.5 = 0.9$ V and $NM_L = 1.5 - 0.33 = 1.17$ V.

### Power

**Average supply current** — a TTL gate draws different current in its two output states, so the
data sheet quotes the mean.

$$\boxed{\;I_{CC(\text{avg})} = \frac{I_{CCH} + I_{CCL}}{2}\;}$$

- $I_{CCH}$ — supply current with the output HIGH, in A
- $I_{CCL}$ — supply current with the output LOW, in A

[eq: average-supply-current] ·CH2 slide 15

**Average power dissipation** — the figure quoted per gate.

$$\boxed{\;P_{D(\text{avg})} = I_{CC(\text{avg})} \times V_{CC}\;}$$

- $V_{CC}$ — supply rail, in V ($V_{DD}$ on a MOS part)
- $P_{D(\text{avg})}$ — average power dissipation, in W

[eq: average-power-dissipation] ·CH2 slide 15

Valid **only at a 50% duty cycle** — output HIGH half the time — which is the condition the
manufacturer specifies ·CH2 slide 15. Worked example ·CH2 slide 17: 2 mA and 3.6 mA give
$I_{CC(\text{avg})} = 2.8$ mA and $P_{D(\text{avg})} = 2.8\ \text{mA} \times 5\ \text{V} = 14$ mW.

---

## 2 · Memory organisation and Hamming codes

·CH3 slides 1–33. Seven equations.

### Organisation

**Addressable words** — the address bus width fixes how many words the part holds.

$$\boxed{\;\text{number of words} = 2^{k}\;}$$

- $k$ — number of address lines (count); addresses run $0$ to $2^k - 1$

[eq: address-lines-to-words] ·CH3 slide 12

**Capacity** — words times word length.

$$\boxed{\;\text{capacity} = 2^{k} \times n \ \text{bits}\;}$$

- $n$ — word length, in bits
- with $K = 2^{10}$, $M = 2^{20}$, $G = 2^{30}$: a 64K part needs $k = 16$, a 2M part $k = 21$, a
  4G part $k = 32$ ·CH3 slide 12

[eq: memory-capacity-bits] ·CH3 slide 12

**ROM organisation** — what a ROM is made of, which is also the reason it is the first of the three
programmable configurations in §3.

$$\boxed{\;2^{k} \times n \ \text{ROM} \;=\; \text{a } k \times 2^{k} \text{ decoder} \;+\; n \ \text{OR gates}\;}$$

- decoder side — **fixed** AND gates, one per address combination
- OR side — **programmable** connections; that is what gets burned
- a ROM has no data inputs, because it has no write operation

[eq: rom-organisation] ·CH3 slide 31

### Hamming code

**How many check bits** — the inequality that decides $k$ before anything else can be laid out.

$$\boxed{\;2^{k} \ \ge\ n + k + 1\;}$$

- $n$ — data bits (count)
- $k$ — check bits (count); parity bits sit in the power-of-two positions $1, 2, 4, 8, \ldots$ and
  positions are numbered from 1, never 0

[eq: hamming-check-bit-count] [added — the standard condition; the deck prints only the resulting
table] ·CH3 slide 30

For $n = 8$: $k = 4$ gives $16 \ge 13$ ✓, while $k = 3$ gives $8 \ge 12$ ✗ — hence the 12-bit code
word the deck uses.

**Parity generation** — each parity bit is the XOR of the **data** positions it covers, its own
position excluded.

$$P_1 = \text{XOR}(3,5,7,9,11)$$

$$P_2 = \text{XOR}(3,6,7,10,11)$$

$$P_4 = \text{XOR}(5,6,7,12)$$

$$P_8 = \text{XOR}(9,10,11,12)$$

- $P_j$ — parity bit stored at position $j$ (logic 0/1); the rule is that $P_{2^i}$ covers every
  position whose binary index has bit $i$ set

[eq: hamming-parity-equations] ·CH3 slide 28 *(correct as printed)*

Data word $11000100$ gives $P_1 P_2 P_4 P_8 = 0,0,1,1$ and the code word $001110010100$
·CH3 slides 27–28.

**Syndrome** — recomputed on read-back, this time **including** the parity position itself.

$$C_1 = \text{XOR}(1,3,5,7,9,11)$$

$$C_2 = \text{XOR}(2,3,6,7,10,11)$$

$$C_4 = \text{XOR}(4,5,6,7,12)$$

$$C_8 = \text{XOR}(8,9,10,11,12)$$

$$\boxed{\;\text{syndrome} = C_8C_4C_2C_1 = \text{position of the faulty bit}, \quad 0000 = \text{no error}\;}$$

- $C_j$ — check bit recomputed at read time (logic 0/1)

[eq: hamming-syndrome-equations] ·CH3 slide 28

⚠ **The slide prints** (V03-4) the last row of the syndrome table — an error in **position 12** — as
$C_8C_4C_2C_1 = 1000$, a duplicate of the position-8 row. It must be $1100$: position 12 appears in
both $C_8$ and $C_4$, so flipping it flips both. The check is the one the whole scheme rests on —
$1100_2 = 12$, while $1000_2 = 8$ ·CH3 slide 29.

**SEC-DED** — one further parity bit over the whole code word upgrades single-error correction to
single-error correction *plus* double-error detection.

$$\boxed{\;P_{13} = \text{XOR}(\text{all 12 code bits})\;}$$

- $P_{13}$ — overall even-parity bit appended to the code word (logic 0/1)

[eq: sec-ded-parity-bit] ·CH3 slide 30

Read-back logic ·CH3 slide 30: overall parity wrong and syndrome non-zero → single error, correct
it. Overall parity right and syndrome non-zero → double error, flag it. Both zero → no error.

---

## 3 · Programmable logic

·CH3 slides 34–66. Five equations. All three device types are the same two arrays, differing only in
which set of crosspoints the manufacturer lets the designer set.

**The general PLD output** — every PLD, without exception, computes a sum of products.

$$F_j \;=\; \sum_{i=1}^{p} c_{ij}\,P_i , \qquad P_i \;=\; \prod_{k=1}^{n} \ell_{ik}$$

- $n$ — input lines (count); $p$ — product-term lines (count); $m$ — output lines (count)
- $P_i$ — the $i$-th product term (logic 0/1)
- $\ell_{ik}$ — either $x_k$, $\bar{x}_k$, or absent, as programmed in the AND array
- $c_{ij}$ — OR-array crosspoint, 1 = link intact (logic 0/1)

[eq: pld-sum-of-products] [added] ·CH3 slide 37

| Device | AND array | OR array |
|---|---|---|
| PROM | fixed (a decoder) | programmable |
| PLA | programmable | programmable |
| PAL | programmable | fixed |

**PROM decoder size** — the fixed AND array of a PROM is a full decoder, so it produces one line per
input combination.

$$\boxed{\;2^{n}\ \text{words}\;}$$

- $n$ — address inputs (count); the deck's example uses a $5 \times 32$ decoder for five inputs

[eq: prom-decoder-size] ·CH3 slides 41, 43. Programming convention on ·CH3 slide 43:
$0 \rightarrow$ no connection, $1 \rightarrow$ connection.

⚠ Related (C04-1): the fuse legend on ·CH3 slide 49 prints "**1** Fuse blown" where slide 45 prints
"$+$ Fuse blown" — and slide 43 defines 1 as a *connection*, the opposite sense.

**XOR output polarity** — each PLA output passes through an XOR whose second input is itself a fuse,
so a function can be built in whichever polarity needs fewer product terms.

$$x \oplus 1 = \bar{x} \qquad\text{(output inverted — column marked C)}$$

$$x \oplus 0 = x \qquad\;\;\text{(output unchanged — column marked T)}$$

- T, C — the deck's programming-table markings for true and complemented output
- careful: the column header **C** means *complement*, not the input variable $C$, and both appear on
  ·CH3 slide 45

[eq: xor-polarity-control] ·CH3 slide 44

**PLA size** — how many crosspoints a given PLA contains, which is what a "how big is the fuse map"
question wants.

$$\text{AND-array crosspoints} = 2nk, \qquad
\text{OR-array crosspoints} = km, \qquad
\text{polarity crosspoints} = 2m$$

- $k$ — product terms; the deck writes this count as $p$ on slide 37 and as $k$ on slide 45, same
  quantity
- two polarity fuses per output, of which exactly one is left intact
- for slide 45's PLA, $n = 3$, $k = 4$, $m = 2$ gives 24, 8 and 4 — exactly what the figure draws

[eq: pla-fuse-count] [added] ·CH3 slide 45

**An unused product term** — a PAL product line with every fuse left intact sees both polarities of
every variable, so it is permanently 0 and contributes nothing.

$$P \;=\; A\cdot A' \cdot B\cdot B' \cdot C\cdot C' \cdot D \cdot D' \cdot w \cdot w' \;=\; 0$$

[eq: unused-product-term] ·CH3 slide 52 — which annotates two such gates "all fuses intact
(always = 0)".

⚠ Related (V04-1): the same fuse map labels its ten columns twice, and the **bottom** row prints
column 3 as $B'$ where it carries $B$. Use the top label row, or product term 5 reads $B'CD$ instead
of $BCD$ ·CH3 slide 52.

---

## 4 · Analogue-to-digital conversion

·CH4 slides 1–29. Twelve tagged equations, plus the comparison-table clock counts.

### ⚠ Read first — the $2^{n}$ against $2^{n}-1$ split

This is the single most common way to lose marks in this unit, and both conventions appear inside
Chapter 4.

$$\boxed{\;\text{levels, states, codes, zones, decoder words} \;=\; 2^{\,n} \qquad\qquad \text{steps between the extreme codes} \;=\; 2^{\,n}-1\;}$$

**The selection rule.** Ask what the number you are dividing by actually *is*.

- If it is a reference sitting **one step above the largest code** — a ladder spanning $V_{\text{REF}}$
  cut into $2^n$ equal zones — divide by $2^{n}$.
- If it is a full-scale output that the largest code **actually produces**, divide by $2^{n}-1$,
  because the top code is $2^n - 1$ steps up from zero.

Where each convention is used:

| Relation | Convention | Source |
|---|---|---|
| Flash step, $\Delta V = V_{\text{REF}}/2^{n}$ | $2^{n}$ | ·CH4 slide 15 |
| Quantisation step, $\Delta = (\max-\min)/L$ with $L = 2^{n}$ | $2^{n}$ | ·CH4 slides 12, 13 |
| SAR tree, step $= V_{\text{REF}}/2^{n}$ (0.625 V on a 10 V reference) | $2^{n}$ | ·CH4 slide 22 |
| Flash comparator count, $2^{n}-1$ | $2^{n}-1$ | ·CH4 slide 15 |
| ADC transfer, $(V_{\text{in}}/V_{\text{REF}})(2^{n}-1)$ | $2^{n}-1$ | ·CH4 slide 23 |
| **DAC resolution, $V_{\text{FS}}/(2^{N}-1)$** | $2^{N}-1$ | ·CH4 slides 34, 48 |

Both are defensible; what loses marks is mixing them **inside one question**. On a 3-bit flash with
$V_{\text{REF}} = 8$ V the step is 1 V and the seven taps sit at 1 V to 7 V — so $2^n$ zones and
$2^n - 1$ comparators are both right, and neither figure is a typo for the other ·CH4 slide 15.
See `_nomenclature.md` for the full clash entry, including the $n$ / $N$ case slip (C05-5, C06-6)
that sits on top of it.

### Sampling

**Sampling rate** — samples taken per second, the reciprocal of the interval.

$$\boxed{\;f_s = \frac{1}{T_s}\;}$$

- $f_s$ — sampling rate, in samples/s (Hz for this purpose)
- $T_s$ — sampling interval, in s; the same slide also calls it $T$ (C05-4)
- the sampled sequence is $x[n] = x(nT_s)$

[eq: sampling-rate] ·CH4 slide 7

**Nyquist criterion** — the condition for the analogue signal to be recoverable from its samples.

$$\boxed{\;f_s \;\ge\; 2 f_{\max} \qquad\Longleftrightarrow\qquad T_s \;\le\; \frac{1}{2 f_{\max}}\;}$$

- $f_{\max}$ — highest frequency present in the signal, in Hz
- $2f_{\max}$ — the **Nyquist rate**

[eq: nyquist-rate] ·CH4 slide 8

⚠ **The slide prints** (C05-3) prose saying the rate must be "**greater than** twice the maximum
frequency" directly above the formula $f_s \ge 2f_{\max}$. Reproduce the printed $\ge$, but know
that the strict $f_s > 2f_{\max}$ is the safe statement: at exactly $2f_{\max}$ a component on
$f_{\max}$ can be sampled at its zero crossings every time and vanish.

Worked: $f_{\max} = 20$ kHz gives $f_s \ge 40$ kHz and $T_s \le 25\ \mu$s ·CH4 slide 8.

**Anti-aliasing filter cut-off** — everything above this must be removed *before* sampling, or it
comes back as an alias.

$$\boxed{\;f_c < \tfrac{1}{2} f_{\text{sample}}\;}$$

- $f_c$ — filter cut-off frequency, in Hz
- $f_{\text{sample}}$ — sampling rate, in Hz; the same quantity as $f_s$

[eq: anti-alias-cutoff] ·CH4 slide 9

### Quantisation

**Quantisation step** — the amplitude span is cut into $L$ equal zones and each zone gets one code.

$$\boxed{\;\Delta = \frac{\max - \min}{L}\;}$$

- $\Delta$ — quantisation step, the height of one zone, in V
- $\max - \min$ — the full amplitude span converted, in V
- $L$ — number of zones, equal to the number of quantisation levels

[eq: quantisation-step] ·CH4 slide 12

**Levels from bits** — the link between the code width and the number of zones.

$$\boxed{\;L = 2^{\,n}\;}$$

- $n$ — bits per code word (count); slide 12 is the $n = 2$ case, slide 13 the $n = 4$ case

[eq: quantisation-levels] [added — the slides work both cases but never write the relation]
·CH4 slides 12–13

**Quantisation error** — the irreversible part. Sampling can be undone; this cannot.

$$\boxed{\;|e_q| \le \frac{\Delta}{2}\;}$$

- $e_q$ — difference between the true sampled amplitude and the level assigned to it, in V

[eq: quantisation-error] [added] ·CH4 slide 11

### Converters

**Inverting-amplifier gain** — the op-amp result the deck opens the converter section with. Remove
the feedback and the same op-amp is the comparator every converter below contains.

$$\boxed{\;\frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_f}{R_i}\;}$$

- $R_f$ — feedback resistor, in $\Omega$; $R_i$ — input resistor, in $\Omega$
- the inverting input sits at a **virtual ground**, 0 V

[eq: inverting-gain] ·CH4 slide 14

**Flash comparator count** — why flash converters stop at 8 bits: the hardware doubles per bit.

$$\boxed{\;N_{\text{comp}} = 2^{\,n} - 1\;}$$

- $N_{\text{comp}}$ — comparators in an $n$-bit flash converter (count); $n = 3$ needs 7

[eq: flash-comparators] ·CH4 slide 15

**Flash resolution** — one step of the reference ladder, i.e. one LSB.

$$\boxed{\;\Delta V = \frac{V_{\text{REF}}}{2^{\,n}}\;}$$

- $\Delta V$ — one LSB step, in V
- $V_{\text{REF}}$ — converter reference, top of the ladder, in V

[eq: flash-resolution] ·CH4 slide 15 · see the boxed split above · the same slide writes the bit
count as $n$ then $N$ two lines apart (C05-5)

**SAR conversion time** — fixed, whatever the input, at one clock per bit. That fixed time is the
SAR's selling point.

$$\boxed{\;t_{\text{conv}} = n \, T_{\text{CLK}}\;}$$

- $n$ — bits, and equally the number of clock periods (count)
- $T_{\text{CLK}}$ — clock period, in s

[eq: sar-conversion-time] ·CH4 slide 19

The decision rule that goes with it: $V_{\text{in}} > V_{\text{DAC}}$ ⇒ comparator HIGH ⇒ **keep**
the trial bit; otherwise clear it ·CH4 slides 19, 21.

⚠ **The slide prints** (V05-1) the reverse on its annotation box — "Vin > VDAC: Comparator output
goes low. The bit in the SAR goes low as well." That contradicts slide 19's own rule, slide 21's
flowchart, and slide 20's drawn polarity, which puts $V_{\text{in}}$ on the **+** input ·CH4 slide 20.

**ADC transfer relation** — code out for a given input, the form the set homework hands you.

$$\boxed{\;\text{Digital out} = \left(\frac{V_{\text{in}}}{V_{\text{REF}}}\right)\left(2^{\,n}-1\right)\;}$$

- $V_{\text{in}}$ — analogue input, in V; $V_{\text{REF}}$ — reference, in V
- result truncated to an integer code

[eq: adc-transfer] ·CH4 slide 23

⚠ **The slide prints** (C05-1) the denominator as $V_{red}$ — a symbol defined nowhere in the
chapter. The question's own opening line names it $V_{REF}$ and gives it as 5 V ·CH4 slide 23.

**Dual-slope count** — the count latched at the zero crossing, which is what makes the reading
proportional to the input while $R$ and $C$ cancel between the two phases.

$$\boxed{\;n_{\text{count}} = 2^{\,n}\,\frac{V_{\text{in}}}{V_{\text{REF}}}\;}$$

- $n_{\text{count}}$ — count latched at the zero crossing (count)
- $2^{\,n}$ — the fixed count of the integrate phase, for an $n$-stage counter

[eq: dual-slope-count] [added — the deck states the mechanism, not the formula] ·CH4 slide 25

**Converter clock counts** — the comparison table, worst case, one row per architecture.

| Converter | Clocks | Conversion time |
|---|---|---|
| Dual slope | $2^{\,n+1}$ ⚠ | $2^{\,n+1}\,T_{\text{CLK}}$ ⚠ |
| Counter type / digital ramp | $2^{\,n}-1$ | $(2^{\,n}-1)\,T_{\text{CLK}}$ |
| Flash | $1$ | $T_{\text{CLK}}$ |
| Successive approximation | $n$ | $n\,T_{\text{CLK}}$ |
| Sigma-delta | $2^{\,n}$ | $2^{\,n}\,T_{\text{CLK}}$ |

[eq: dual-slope-clock-count] — *proposed tag; the row is untagged in file 05* ·CH4 slide 28

⚠ **The slide prints** (V05-4) the dual-slope row as $2^{n}+1$ clocks and $(2^{n}+1)T_{\text{CLK}}$.
The exponent has lost its bracket: the converter integrates for a full $2^{n}$ counts, then
de-integrates for up to $2^{n}$ more, so the worst case is $2 \times 2^{n} = 2^{\,n+1}$. At $n = 12$
that is 4097 against 8192 ·CH4 slide 28.

---

## 5 · Digital-to-analogue conversion

·CH4 slides 30–49. Nine equations, and the chapter with the most defects in the unit — 15 flags.
Note the convention change from §4: **every resolution formula in this section divides by
$2^{N}-1$**, because $V_{\text{FS}}$ here is the output the largest code actually produces.

**The transfer relation** — a DAC's output is simply proportional to the decimal value of its input
code.

$$\boxed{\;\text{Analogue output} = K \times \text{digital value}\;}$$

- $K$ — proportionality factor, in V (or A) per step; the slide names it the **resolution** — it is
  the step size
- $D$ — decimal equivalent of the applied code (count), $0$ to $2^N-1$
- $N$ — number of input bits (count)

[eq: dac-transfer] ·CH4 slide 31

One measured (code, output) pair pins down $K$; everything else follows. Worked ·CH4 slide 31: a
4-bit converter with $K = 0.5$ V and code $0110 = 6$ gives 3.0 V.

**Resolution** — the smallest output change one code step can produce.

$$\boxed{\;\text{Resolution} = \frac{V_{\text{FS}}}{2^{\,N}-1}\;}$$

- $V_{\text{FS}}$ — full-scale output, in V or A
- $2^{N}-1$ — number of **steps** from the zero code to the full-scale code (count)
- $2^{N}$ — number of **states**, i.e. distinct output levels (count)

[eq: dac-resolution] ·CH4 slide 34

⚠ **The slide prints** (V06-1) the gloss "$2^{N}-1$ = no of states, $N$ = no of bits". The formula
is right; the label under it is not. $2^{N}$ is the state count and $2^{N}-1$ the step count —
slide 48 says so itself, defining resolution as "the reciprocal of the number of **steps** in the
output" ·CH4 slides 34, 48. Related: slide 37 heads a line "Step size $= 2^{N}-1 = 4095$" (V06-5) —
a step size is a voltage, not a count.

**Percentage resolution** — the step as a fraction of full scale, so a pure number independent of
what the full-scale output happens to be.

$$\boxed{\;\%\ \text{resolution} = \frac{1}{2^{\,N}-1}\times 100\,\%\;}$$

[eq: dac-percentage-resolution] [added — used on slides 37 and 48 but never written out]
·CH4 slides 37, 48

Worked ·CH4 slide 48, 8-bit: $255$ steps, $\%\ \text{res} = 100/255 = 0.39\,\%$, and the
$\pm\tfrac{1}{2}$ LSB accuracy that goes with it is $\pm 0.196 \approx \pm 0.2\,\%$.

⚠ **The slide prints** (V06-6) "$= 0.00244 = 0.244\,\%$" on slide 37 — restating a step in volts as
a percentage by multiplying by 100. On the slide's own binary route the answer is
$\tfrac{1}{4095}\times100\,\% = 0.0244\,\%$; on the corrected BCD route (V06-4: a 12-bit BCD word is
three decades, so 999 steps, not 4095) it is $0.1\,\%$ ·CH4 slide 37.

**Bits for a required resolution** — invert the resolution formula when the question fixes the step
and asks for $N$.

$$N \ge \left\lceil \log_2\!\left(\frac{V_{\text{FS}}}{V_{\text{res}}} + 1\right)\right\rceil$$

- $V_{\text{res}}$ — required resolution (one step), in V or A

[eq: bits-for-resolution] [added — the general form of the deck's worked chain] ·CH4 slide 36

Worked ·CH4 slide 36: $V_{\text{FS}} = 10$ mA, step $< 40\ \mu$A gives $2^N - 1 > 250$, so $N = 8$.
Confirm directly, which is the exam-worthy check: $10\ \text{mA}/127 = 78.7\ \mu$A is too coarse,
$10\ \text{mA}/255 = 39.2\ \mu$A meets it.

⚠ **The slide prints** (V06-3) every inequality in that chain the wrong way round — opening with
$40\times10^{-6} < 10\times10^{-3}/(2^N-1)$ and reaching $2^N < 251$, which forces $N \le 7$ — then
writes $N = 7.97 \approx 8$ bits anyway. The answer is right; the printed reasoning is inverted
·CH4 slide 36.

**Full-scale error** — the maximum deviation of the actual output from the expected one, quoted as
$\pm$ a percentage.

$$\boxed{\;\text{Full-scale error} = \frac{\text{Error}}{\text{Original value}}\times 100\,\%\;}$$

- Error $E$ — deviation of the actual output from the ideal, in V or A
- "Original value" — the deck's wording for the expected output at that code, in V or A

[eq: full-scale-error] ·CH4 slide 38

⚠ **The slide prints** (V06-8), rearranging for $E$ on a 2 mA converter at $\pm19\,\%$:
$E = (2\ \text{mA} \times 0.19)/100 = 3.8\ \mu$A. The percentage is applied twice — $0.19$ already
*is* $19/100$. The answer is $E = 0.19 \times 2\ \text{mA} = 0.38\ \text{mA} = 380\ \mu$A
·CH4 slide 38.

**Binary-weighted-input DAC, branch currents** — each input drives its own resistor into a virtual
ground, so the currents are independent and binary-weighted.

$$I_0 = \frac{V}{8R},\qquad I_1 = \frac{V}{4R},\qquad I_2 = \frac{V}{2R},\qquad I_3 = \frac{V}{R}$$

$$\boxed{\;I_i = \frac{V}{2^{\,n-1-i}\,R}\;}$$

- $V$ — input HIGH level, in V; $R$ — smallest resistor, on the MSB, in $\Omega$
- $i$ — bit number, $i = 0$ the LSB; $n$ — number of bits
- the resistor on bit $i$ is $2^{\,n-1-i}R$, so an 8-bit version needs a matched 128:1 spread —
  which is the topology's weakness

[eq: binary-weighted-current] ·CH4 slide 39 · the four-bit currents are printed, the general form is
[added]

**Binary-weighted-input DAC, output** — the summing amplifier turns the total current into a voltage.

$$\boxed{\;V_{\text{out}} = -R_f \sum_{i} I_i \;}$$

- $R_f$ — feedback resistor, in $\Omega$; $I_i$ — current injected by bit $i$, in A

[eq: binary-weighted-output] ·CH4 slide 39

⚠ **The slide prints** (C06-5) $V_{\text{out}} = I_f R_f$, with **no minus sign**, although the
amplifier is inverting — and slide 41 then relies on the output being negative while slide 42
tabulates sixteen negative values ·CH4 slide 39.

**R/2R ladder, one bit at a time** — each HIGH input contributes independently, so superposition
gives the whole answer. **This is the formula the deck gets wrong.**

$$\boxed{\;V_{\text{out}}(D_i) = -\frac{V_S}{2^{\,n-1-i}}\;}$$

- $V_S$ — input HIGH level, in V
- $n$ — number of bits; $i$ — bit number, $i = 0$ the LSB, matching the deck's own $D_0 \ldots D_3$
- valid for the standard ladder with $R_f = 2R$

[eq: r2r-bit-contribution] ·CH4 slide 44, **corrected**

⚠ **The slide prints** (V06-9):

$$V_{\text{out}}(D_i) = -\frac{V_S}{2^{\,n-i}} \qquad \text{— out by one power of two}$$

Two independent checks. The deck contradicts itself: slides 45(a) and 46 analyse the same network
from the circuit and get $-5$ V for the MSB alone, where the printed formula gives $-2.5$ V. And a
nodal solution of the ladder returns the single-bit weights $-0.625$, $-1.25$, $-2.5$, $-5$ V —
exactly twice every value the printed form produces. The printed exponent would be right only if the
bits were numbered $1$ to $n$; the deck numbers them $0$ to $n-1$ in its own figures
·CH4 slides 44, 47.

**R/2R ladder, whole transfer characteristic** — sum the corrected contributions over every HIGH bit
and the ladder collapses to one line.

$$\boxed{\;V_{\text{out}} = -\frac{V_S}{2^{\,n-1}}\,D\;}$$

- $D$ — decimal value of the input code (count)
- step $= -V_S/2^{\,n-1}$; full scale $= -V_S(2^n-1)/2^{\,n-1}$, which for $n = 4$, $V_S = 5$ V is
  $-9.375$ V

[eq: r2r-full-transfer] [added] ·CH4 slides 44–47

Worked ·CH4 slide 47, input $1011$ with $V_S = 5$ V: $-5 - 1.25 - 0.625 = -6.875$ V, and the one-line
check is $1011_2 = 11$, so $-\tfrac{5}{8}\times 11 = -6.875$ V.

⚠ **The slide prints** $-3.4375$ V for that example — exactly half — because it applies the
off-by-one formula throughout (V06-9). Also read every "50 kW" and "25 kW" on slides 44 and 47 as
$50\ \text{k}\Omega$ and $25\ \text{k}\Omega$ (C06-3); the ohm sign has been replaced by a W.

---

## 6 · Flip-flop characteristic and excitation equations

·EXC and ·CH5 slides 28, 31. **The most-consulted content in the unit.** Characteristic equations
answer "given the inputs, what does the flip-flop do?"; excitation tables answer "given the
transition I want, what inputs do I apply?" — the design direction.

### The four characteristic equations

$$\boxed{\;Q(t+1) = S + R'Q \qquad\text{(SR, valid for } SR = 0\text{)}\;}$$

[eq: sr-characteristic] [added — the handout gives the SR table but not its equation] ·EXC

$$\boxed{\;Q(t+1) = D \qquad\text{(D)}\;}$$

[eq: d-characteristic] ·EXC, ·CH1 slide 12 [eq: d-flip-flop-characteristic]

$$\boxed{\;Q(t+1) = J\,Q' + K'\,Q \qquad\text{(JK)}\;}$$

[eq: jk-characteristic] ·EXC, ·CH5 slide 28, ·CH6 slide 40, ·CH1 slide 18
[eq: jk-flip-flop-characteristic]

$$\boxed{\;Q(t+1) = T \oplus Q = T'Q + TQ' \qquad\text{(T)}\;}$$

[eq: t-characteristic] ·EXC, ·CH5 slides 28 and 31

- $Q(t)$ — present state of the flip-flop (logic 0/1)
- $Q(t+1)$ — state one active clock edge later (logic 0/1)
- $S$, $R$, $D$, $J$, $K$, $T$ — the flip-flop control inputs (logic 0/1)

⚠ **The slide prints** (C07-2) the JK and T equations with $D$ on the left: "$D = JQ' + K'Q$" and
"$D = T \oplus Q$". The left-hand side is the **next state**. Writing $D$ there only means "the
equivalent D input", and neither a JK nor a T flip-flop has a $D$ input; slide 31 prints the T
relation correctly ·CH5 slide 28.

### The four characteristic tables

**SR** ·EXC

| $S$ | $R$ | $Q(t+1)$ | |
|---|---|---|---|
| 0 | 0 | $Q(t)$ | no change |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | ? | undefined |

**D** ·EXC

| $D$ | $Q(t+1)$ |
|---|---|
| 0 | 0 |
| 1 | 1 |

**JK** ·EXC

| $J$ | $K$ | $Q(t+1)$ | |
|---|---|---|---|
| 0 | 0 | $Q(t)$ | no change |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | $Q'(t)$ | toggle |

**T** ·EXC

| $T$ | $Q(t+1)$ | |
|---|---|---|
| 0 | $Q(t)$ | no change |
| 1 | $Q'(t)$ | toggle |

⚠ **The handout prints** (V07-3) the T characteristic table with its input column headed **$D$**,
although the section is titled "T Flip-flop" and the rows describe toggling. Read as printed it says
a D flip-flop complements its output when $D = 1$, which is wrong. The column is $T$ ·EXC.

### The four excitation tables — one grid

$$\boxed{\begin{array}{cc|cc|c|cc|c}
Q(t) & Q(t+1) & S & R & D & J & K & T \\ \hline
0 & 0 & 0 & \text{X} & 0 & 0 & \text{X} & 0\\
0 & 1 & 1 & 0 & 1 & 1 & \text{X} & 1\\
1 & 0 & 0 & 1 & 0 & \text{X} & 1 & 1\\
1 & 1 & \text{X} & 0 & 1 & \text{X} & 0 & 0
\end{array}}$$

·EXC, consolidated [added]. X is a don't-care. Half the JK entries are don't-cares, which is exactly
why JK-based designs often need less gating than D-based ones — and why the D column, which is
simply the wanted next state, makes design easiest.

### The four excitation rules

The algebra behind the grid — use these when the transition is known and the input is wanted.

$$\boxed{\;D = Q(t+1)\;}$$

$$\boxed{\;T = Q(t) \oplus Q(t+1)\;}$$

$$\boxed{\;S = Q'(t)\,Q(t+1), \qquad R = Q(t)\,Q'(t+1)\;}$$

$$\boxed{\;J = Q(t+1)\ \text{when}\ Q(t) = 0, \qquad K = Q'(t+1)\ \text{when}\ Q(t) = 1\;}$$

[eq: excitation-rules] — *proposed tag; these four are untagged in file 07 §7.15* · [added] ·EXC

Set $T$ to 1 exactly when the state must change. The SR and JK forms reproduce the tabulated entries
with the don't-cares filled in as 0.

---

## 7 · Finite state machine relations

·CH5 slides 3–38 (file 07) and 39–71 (file 08). The definitions first, then the analysis results.

### Structure

**How many states the storage allows** — the ceiling on any machine built from $n$ bits of memory.

$$\boxed{\;\text{number of possible states} = 2^{\,n}\;}$$

- $n$ — bits of storage, i.e. flip-flops (count); three flip-flops give at most eight states

[eq: fsm-state-count] ·CH5 slide 4

**How many rows a state table needs** — one row per combination of present state and input.

$$\boxed{\;\text{rows} = 2^{\,m+n}\;}$$

- $m$ — number of flip-flops (count); $n$ — number of external inputs (count)
- $m = 2$, $n = 1$ gives eight rows

[eq: state-table-rows] ·CH5 slide 22

**Mealy model** — output depends on state *and* input, so it can respond within the same clock
period, and it appears on the **arc** of the state diagram.

$$\text{next state} = F_1(\text{current state},\,\text{inputs})$$

$$\text{output} = G_1(\text{current state},\,\text{inputs})$$

[eq: mealy-model] ·CH5 slide 8

**Moore model** — output depends on the state alone, so it is written **inside the state** and is
safe from input glitches.

$$\text{next state} = F_2(\text{current state},\,\text{inputs})$$

$$\text{output} = G_2(\text{current state})$$

[eq: moore-model] ·CH5 slide 8

The next-state function is identical in form; only the output function differs. That is the whole of
the Mealy/Moore distinction.

**The same three relations, formally** — the notation used throughout file 08.

$$\boxed{\;S(t+1)=\delta\big(S(t),X(t)\big)\;}$$

[eq: next-state-function] [added] ·CH5 slide 40

$$\boxed{\;Z(t)=\lambda\big(S(t),X(t)\big) \qquad\text{(Mealy)}\;}$$

[eq: mealy-output-function] [added] ·CH5 slide 67

$$\boxed{\;Z(t)=\lambda\big(S(t)\big) \qquad\text{(Moore)}\;}$$

[eq: moore-output-function] [added] ·CH5 slide 54

- $S(t)$ — present state during clock period $t$
- $X(t)$ — input sampled at the end of that period (logic 0/1)
- $Z(t)$ — output present during period $t$ (logic 0/1)
- $\delta$ — next-state function; $\lambda$ — output function

**The one-clock delay** — the relation that decides marks whenever a question asks for both machines.

$$\boxed{\;Z_{\text{Moore}}(t+1)=Z_{\text{Mealy}}(t)\;}$$

[eq: moore-mealy-delay] [added] ·CH5 slides 57, 63, 70

- verified exhaustively for all three worked specifications, over every input string up to 16 bits
- if a Mealy and a Moore answer to the same specification differ by anything **other** than this
  shift, one of them is wrong
- the Moore machine also needs more states — 4 against 3 for the 101 detector, 8 against 6 for
  010/1001, 5 against 4 for 1101 ·CH5 slide 70

⚠ **The slide prints** (V08-1) the Moore specification for 101 with the Mealy phrase "coincident with
the last 1 input". A Moore machine cannot do that: the state meaning "101 received" is only
*entered* on the edge that samples the last 1, so $Z$ rises during the **following** period
·CH5 slide 53.

### Analysis results worth carrying

These are the deck's own worked circuits. They recur, and two are printed wrongly.

**Serial adder — sum output** ·CH5 slide 17:

$$\boxed{\;z = \bar{a}\,b\,\bar{s} \;+\; a\,\bar{b}\,\bar{s} \;+\; \bar{a}\,\bar{b}\,s \;+\; a\,b\,s \;=\; a \oplus b \oplus s\;}$$

- $a$, $b$ — the two serial input bits; $s$ — the stored carry (all logic 0/1)

[eq: serial-adder-sum]

⚠ **The slide prints** (V07-1) the second and third terms with a **single continuous overbar
spanning two letters**: $z = \bar{a}b\bar{s} + a\overline{bs} + \overline{ab}s + abs$. Read
literally, $\overline{bs} = \bar b + \bar s$, and the expression is 1 for seven of the eight input
combinations instead of four ·CH5 slide 17.

**Serial adder — carry (next state)** ·CH5 slide 17:

$$\boxed{\;s' = ab + bs + as\;}$$

The familiar full-adder carry — a carry out whenever at least two of $a$, $b$, $s$ are 1.

[eq: serial-adder-carry] [added — minimised]

⚠ **The slide prints** (C07-1) the unminimised canonical sum
$s' = ab\bar{s} + \bar{a}bs + a\bar{b}s + abs$, although the K-map immediately above it is grouped
into the three overlapping pairs that give the minimal form. Same function, longer expression
·CH5 slide 17.

**Two-D-flip-flop circuit** ·CH5 slide 21 — the running example of the whole analysis chapter:

$$\boxed{\;A(t+1) = A x + B x\;}$$

[eq: state-equation-a]

$$\boxed{\;B(t+1) = A' x\;}$$

[eq: state-equation-b]

$$\boxed{\;Y(t) = (A + B)\,x'\;}$$

[eq: output-equation-y] — slide 22 prints the same output multiplied out as $Y = Ax' + Bx'$;
identical.

- $A$, $B$ — the two state variables (logic 0/1); $x$ — external input; $Y$ — output

**Single-D-flip-flop circuit** ·CH5 slide 27 — two XORs and one flip-flop:

$$\boxed{\;A(t+1) = A \oplus x \oplus y\;}$$

[eq: d-analysis-state-equation] — *proposed tag; untagged in file 07 §7.12*

**JK analysis** ·CH5 slide 30 — substitute the flip-flop inputs into the JK characteristic equation,
then expand:

$$\boxed{\;A(t+1) = A'B + AB' + Ax\;}$$

[eq: jk-state-equation], from $J_A = B$, $K_A = Bx'$

$$\boxed{\;B(t+1) = B'x' + ABx + A'Bx'\;}$$

from $J_B = x'$, $K_B = A \oplus x$ ·CH5 slide 30

⚠ **The slide prints** (C07-3) the starting equations with **unsubscripted** $J$ and $K$ —
"$A(t+1) = JA' + K'A$ and $B(t+1) = JB' + K'B$" — although the two flip-flops have different inputs.
They must read $A(t+1) = J_A A' + K_A' A$ and $B(t+1) = J_B B' + K_B' B$. The substitution two lines
later uses the right values, so only the notation is at fault ·CH5 slide 30.

**T analysis** ·CH5 slide 31, with $T_A = Bx$ and $T_B = x$:

$$\boxed{\;A(t+1) = AB' + Ax' + A'Bx\;}$$

[eq: t-state-equation]

$$\boxed{\;B(t+1) = x \oplus B\;}$$

**Three-D-flip-flop circuit** ·CH5 slide 33 — a free-running machine with no data input:

$$\boxed{\;D_A = BC \;\Longleftrightarrow\; A(t+1) = BC\;}$$

$$\boxed{\;D_B = B'C + BC' = B \oplus C \;\Longleftrightarrow\; B(t+1) = B \oplus C\;}$$

$$\boxed{\;D_C = A'C' \;\Longleftrightarrow\; C(t+1) = A'C'\;}$$

$$\boxed{\;Z = A\;}$$

[eq: three-d-analysis-equations] — *proposed tag; untagged in file 07 §7.17*

⚠ **The slide prints** (V07-2) these as $A = BC$, $B = B'C + BC'$, $C = A'C'$, $Z = A$. Two are
**self-referential** — $B$ on both sides of the second, $C$ on both sides of the third — so as
ordinary Boolean equations they have no solution. What is meant is the flip-flop *input* equations,
equivalently the next-state equations. Only $Z = A$ is well formed as printed, because $Z$ is a
combinational output and not a state variable ·CH5 slide 33.

⚠ Related (C07-4): the state table on the same slide heads its next-state columns $A'B'C'$, using a
prime to mean "next state" eight lines from equations that use a prime to mean "complement". Write
$A(t+1)$ ·CH5 slide 33.

---

## 8 · State reduction and state assignment

·CH5 slides 72–118. Eight equations.

**State equivalence** — the test that licenses merging two rows of a state table. Both conditions
must hold for **every** value of the input.

$$\boxed{\;p \equiv q \iff \lambda(p, X) = \lambda(q, X) \ \text{ and } \ \delta(p, X) \equiv \delta(q, X) \quad \forall X\;}$$

- $p$, $q$ — the two states being compared
- $\lambda(p,X)$ — output in state $p$ with input $X$ (logic 0/1)
- $\delta(p,X)$ — next state entered from $p$ with input $X$

[eq: state-equivalence] ·CH5 slide 82

The definition is **recursive** — "the next states are equivalent" is the same question one level
down — which is exactly why the mechanical procedures exist: inspection, partitioning, and the
implication table ·CH5 slide 82.

⚠ Related (C09-1): slide 86 boxes the conclusion "a ≡ d iff a ≡ d and c ≡ e", which is circular and
states nothing. Once the self-redundant pair $a$-$d$ is struck out of its own square the surviving
condition is $c \equiv e$ alone ·CH5 slide 86.

**Minimum flip-flop count** — how many state variables the reduced table needs.

$$\boxed{\;n \ \geq\ \log_2 m \qquad\Longleftrightarrow\qquad 2^{\,n} \ \geq\ m\;}$$

- $m$ — number of states in the reduced table (count)
- $n$ — number of state variables, i.e. flip-flops (count); being a bit count, take the smallest
  **integer** satisfying the inequality

[eq: min-state-bits] ·CH5 slide 92

Assignments using **more** than the minimum are legitimate — one-hot coding is the obvious case
·CH5 slide 92. Choosing an optimal assignment exhaustively is NP-complete, hence the three
guidelines ·CH5 slide 91 (printed "n-p complete", C09-2).

**Unused codes** — every one of them becomes a don't-care in every next-state map, which is where
most of the minimisation comes from.

$$\boxed{\;\text{unused states} = 2^{\,n} - m\;}$$

[eq: unused-states] ·CH5 slide 92 — $m = 7$, $n = 3$ leaves one unused code

**The three assignment guidelines**, in priority order ·CH5 slide 91 — give **adjacent** codes
(differing in one bit) to states that: (1) have the same next state for a given input; (2) are the
next states of the same state; (3) have the same output for a given input. Satisfy guideline 1
first, then any guideline-2 adjacency required twice or more ·CH5 slide 95. Assign the **starting
state to the all-zero code**, so the flip-flop clear inputs can initialise and reset it
·CH5 slides 93–94.

**Seven-state machine — flip-flop input equations** ·CH5 slide 98:

$$A^{+} \;=\; X'$$

$$B^{+} \;=\; X'C' + A'C + A'B$$

$$C^{+} \;=\; A + XB'$$

- $A$, $B$, $C$ — state variables; $X$ — input; $Q^{+}$ — next value of state variable $Q$
- with D flip-flops these are $D_A$, $D_B$, $D_C$ directly

[eq: seven-state-flipflop-equations] ·CH5 slide 98

⚠ **The slide prints** (V09-2) the equations correctly but its $B^{+}$ **K-map** wrongly: the cell at
$XA = 10$, $BC = 00$ holds **1** and must be **0**. That cell is $ABC = 000 = S_0$ with $X = 1$,
whose next state is $S_2 = 001$. Left as printed, the row becomes all 1s and invites the grouping
$B^{+} = B'C' + A'C + A'B$, which sends $S_0$ to $S_4$ instead of $S_2$ ·CH5 slide 98.

**Six-state machine — flip-flop input and output equations** ·CH5 slide 101:

$$D_1 = Q_1^{+} \;=\; X'Q_1Q_2' + XQ_1'$$

$$D_2 = Q_2^{+} \;=\; Q_3$$

$$D_3 = Q_3^{+} \;=\; XQ_1'Q_2 + X'Q_3$$

$$\boxed{\;Z \;=\; XQ_2Q_3 + X'Q_2'Q_3 + X'Q_2Q_3'\;}$$

- $Q_1Q_2Q_3$ — the three state variables; cost as built: 10 gates, 26 gate inputs ·CH5 slide 101

[eq: six-state-flipflop-equations] ·CH5 slide 101

⚠ **The slide prints** (V09-3) the third term of $Z$ as $XQ_2Q_3'$, **without the prime on $X$**. Two
cells of its own map prove the prime belongs: at $XQ_1 = 00$, $Q_2Q_3 = 10$ the map holds 1 and the
printed equation gives 0; at $XQ_1 = 10$, $Q_2Q_3 = 10$ the map holds 0 and the printed equation
gives 1. The K-map loop drawn on the slide covers $X = 0$, so only the transcription slipped
·CH5 slide 101.

**Case II — overlapping 101 detector, two variables** ·CH5 slide 106, with $S_0 = 00$, $S_1 = 01$,
$S_2 = 10$ and $11$ unused:

$$\boxed{\;A^{+} = X'B, \qquad B^{+} = X, \qquad Z = XA\;}$$

[eq: case2-flipflop-equations] ·CH5 slide 106 — all three fall out immediately because the unused
code 11 is a don't-care in every map.

**State-graph completeness** — OR the input labels on all arcs leaving a state; the result must
reduce to 1, or some input combination has no defined transition.

$$\boxed{\;\sum_{\text{arcs out of a state}} (\text{input label}) \;=\; 1\;}$$

Worked ·CH5 slide 118: $F + F'R + F'R' = F + F'(R + R') = F + F' = 1$.

[eq: graph-completeness] ·CH5 slide 118

**State-graph mutual exclusion** — AND any *pair* of labels on arcs leaving a state; the result must
be 0, or two arcs are valid at once and the machine is non-deterministic.

$$\boxed{\;(\text{label}_i)\cdot(\text{label}_j) \;=\; 0 \quad \text{for every pair } i \ne j\;}$$

Worked ·CH5 slide 118: $F \cdot F'R = 0$, $F \cdot F'R' = 0$, $F'R \cdot F'R' = 0$.

[eq: graph-mutual-exclusion] ·CH5 slide 118

Together these are the by-eye check "one arc out for each input combination, no more and no less",
done algebraically — and they are the two tests to run on any graph before building from it.

---

## 9 · ASM charts and next-state derivation

·CH6 slides 1–40. Nine equations.

**Next state from link paths** — the whole realisation procedure in one line. An ASM chart is read by
collecting the paths that *arrive* at a state, not the ones that leave it.

$$\boxed{\;Q^{+} \;=\; \sum_{\text{link paths into a state with } Q=1} (\text{state term}) \cdot (\text{exit condition})\;}$$

- $Q$ — one state variable (flip-flop); $Q^{+}$ — its next value (logic 0/1)
- **state term** — the product that is 1 only in the source state $S_i$
- **exit condition** — the product of the decision-box outcomes taken on the way from $S_i$ to $S_j$

[eq: link-path-next-state] ·CH6 slide 18

Worked ·CH6 slide 18, with $S_0 = 00$, $S_1 = 01$, $S_2 = 11$ in the order $AB$:

$$B^{+} = A'B'X + A'BX + ABX = A'X + BX$$

$$A^{+} = A'BX + ABX = BX$$

⚠ Related (C10-1): steps 2 and 3 of the printed procedure have lost their symbols — "for a link path
from to, the term will be 1 if the machine is in state and the conditions for existing to are
satisfied". Read "exiting" for "existing"; the mathematics is unaffected ·CH6 slide 18.

**Equivalent SM charts** — two charts with different decision boxes are equivalent when they produce
the same outputs for every input combination.

$$Z_1 = A + A'BC = A + BC$$

[eq: sm-chart-combinational-output] ·CH6 slide 8 — chart (a) tests $A + BC$ in one box; chart (b)
tests $A$, then $C$, then $B$. Both were evaluated over all eight input combinations and agree.

**The absorption identity** — the simplification the chapter leans on twice.

$$\boxed{\;X + X'Y = X + Y\;}$$

- $X$, $Y$ — any Boolean expressions

[eq: absorption-identity] ·CH6 slides 8, 22

**The two rules for a valid SM chart** ·CH6 slide 9, both printed correctly:
(1) for every valid combination of input variables there must be **exactly one** exit path;
(2) **no internal feedback** within an SM block.

**Dice-game controller** ·CH6 slide 22, three state variables $A$, $B$, $C$:

$$A^{+} = A\,C' + A\,Rb + A\,D_7'\,Eq' + A'B'C\,Rb'\,D_{711}'\,D_{2312}'$$

[eq: dice-next-state-a]

$$B^{+} = B\,Reset' + A\,C\,Rb'\,(Eq + D_7) + A'B'C\,Rb'\,(D_{711} + D_{2312})$$

[eq: dice-next-state-b]

$$C^{+} = B'Rb + BC\,Reset' + A'B'C\,Rb'\,D_{711}'\,D_{2312} + AB'C\,Rb'\,Eq'\,D_7$$

[eq: dice-next-state-c] [added — not mapped on the slide]

$$Win = B\,C' \qquad Lose = B\,C \qquad Roll = B'\,C\,Rb$$

[eq: dice-outputs] ·CH6 slide 22

- $Rb$ — roll button; $D_7$, $D_{711}$, $D_{2312}$ — dice-sum decodes; $Eq$ — point-equals-sum flag
- the four map-entered variables the deck prints are $E_1 = D_{711}'D_{2312}'$, $E_2 = D_7'Eq'$,
  $E_3 = D_{711} + D_{2312}$ and $E_4 = Eq + D_7$, the last two by the absorption identity above
- all four expressions checked against the PLA table over every used state and all 64 input
  combinations

⚠ Related (V10-2): rows 7 and 8 of the row-5 expansion on ·CH6 slide 21 duplicate rows 5 and 6;
$D_7$ should be 1 in them.

**Appendix Example 1 — control next-state equations** ·CH6 slide 33, assignment $T_0 = 00$,
$T_1 = 01$, $T_2 = 11$ (code 10 unreachable, hence a don't-care):

$$D_{G1} = T_1\,A_3\,A_4$$

$$D_{G0} = T_0\,S + T_1$$

[eq: example1-next-state] ·CH6 slide 33

⚠ **The slide draws** (V10-3) the gate forming $D_{G1}$ as an **OR** on the logic diagram, where the
equation requires an **AND** ·CH6 slide 34.

**Appendix Example 1 — state decoding** ·CH6 slide 33:

$$T_0 = G_0' \qquad T_1 = G_1'\,G_0 \qquad T_2 = G_1$$

[eq: example1-state-decode] ·CH6 slide 33 — minimal only because code 10 is unreachable and
therefore a don't-care.

---

## One-page revision list

The equations most likely to be needed under examination conditions. No commentary.

**Flip-flops**

$$Q(t+1) = S + R'Q \qquad Q(t+1) = D \qquad Q(t+1) = JQ' + K'Q \qquad Q(t+1) = T \oplus Q$$

[eq: sr-characteristic] · [eq: d-characteristic] · [eq: jk-characteristic] · [eq: t-characteristic]

| $Q(t)$ | $Q(t+1)$ | $S$ | $R$ | $D$ | $J$ | $K$ | $T$ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | X | 0 | 0 | X | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 | X | 1 |
| 1 | 0 | 0 | 1 | 0 | X | 1 | 1 |
| 1 | 1 | X | 0 | 1 | X | 0 | 0 |

$$D = Q(t+1) \qquad T = Q(t) \oplus Q(t+1) \qquad S = Q'(t)Q(t+1),\ R = Q(t)Q'(t+1)$$

[eq: excitation-rules]

**FSM**

$$2^{\,n} \ \geq\ m \qquad \text{rows} = 2^{\,m+n} \qquad Z_{\text{Moore}}(t+1) = Z_{\text{Mealy}}(t)$$

[eq: min-state-bits] · [eq: state-table-rows] · [eq: moore-mealy-delay]

$$p \equiv q \iff \lambda(p,X) = \lambda(q,X) \ \text{ and } \ \delta(p,X) \equiv \delta(q,X) \quad \forall X$$

[eq: state-equivalence]

$$Q^{+} = \sum_{\text{link paths in}} (\text{state term})\cdot(\text{exit condition})$$

[eq: link-path-next-state]

**Memory**

$$2^{k} \ \text{words} \qquad \text{capacity} = 2^{k} \times n \ \text{bits} \qquad 2^{k} \ge n + k + 1$$

[eq: address-lines-to-words] · [eq: memory-capacity-bits] · [eq: hamming-check-bit-count]

$$\text{syndrome } C_8C_4C_2C_1 = \text{position of the faulty bit}$$

[eq: hamming-syndrome-equations]

**Conversion**

$$f_s \ge 2f_{\max} \qquad L = 2^{\,n} \qquad \Delta = \frac{\max-\min}{L} \qquad |e_q| \le \frac{\Delta}{2}$$

[eq: nyquist-rate] · [eq: quantisation-levels] · [eq: quantisation-step] · [eq: quantisation-error]

$$N_{\text{comp}} = 2^{\,n}-1 \qquad \Delta V = \frac{V_{\text{REF}}}{2^{\,n}} \qquad t_{\text{conv}} = n\,T_{\text{CLK}}$$

[eq: flash-comparators] · [eq: flash-resolution] · [eq: sar-conversion-time]

$$\text{Resolution} = \frac{V_{\text{FS}}}{2^{\,N}-1} \qquad V_{\text{out}}(D_i) = -\frac{V_S}{2^{\,n-1-i}} \qquad V_{\text{out}} = -\frac{V_S}{2^{\,n-1}}\,D$$

[eq: dac-resolution] · [eq: r2r-bit-contribution] · [eq: r2r-full-transfer]

**Logic families**

$$NM_L = V_{IL} - V_{OL} \qquad NM_H = V_{OH} - V_{IH} \qquad \tau_P = \frac{\tau_{PHL} + \tau_{PLH}}{2} \qquad P_{D(\text{avg})} = I_{CC(\text{avg})}V_{CC}$$

[eq: noise-margin-low] · [eq: noise-margin-high] · [eq: average-propagation-delay] ·
[eq: average-power-dissipation]

---

## The corrections at a glance

Every equation on this sheet whose corrected form differs from what the deck prints.

| ID | Where | Printed | Corrected |
|---|---|---|---|
| V06-9 | ·CH4 slides 44, 47 | $V_{\text{out}}(D_i) = -V_S/2^{\,n-i}$ | $V_{\text{out}}(D_i) = -V_S/2^{\,n-1-i}$ |
| V05-4 | ·CH4 slide 28 | dual slope $2^{n}+1$ clocks | $2^{\,n+1}$ clocks |
| V03-4 | ·CH3 slide 29 | syndrome for position 12 $= 1000$ | $1100$ |
| V07-2 | ·CH5 slide 33 | $A = BC$, $B = B'C+BC'$, $C = A'C'$ | $A(t+1) = BC$, $B(t+1) = B \oplus C$, $C(t+1) = A'C'$ |
| V07-1 | ·CH5 slide 17 | $z = \bar{a}b\bar{s} + a\overline{bs} + \overline{ab}s + abs$ | each literal separately barred; $z = a \oplus b \oplus s$ |
| V09-3 | ·CH5 slide 101 | $Z = XQ_2Q_3 + X'Q_2'Q_3 + XQ_2Q_3'$ | third term $X'Q_2Q_3'$ |
| V09-2 | ·CH5 slide 98 | $B^{+}$ map cell at $XA=10$, $BC=00$ is 1 | 0 |
| V06-1 | ·CH4 slide 34 | "$2^{N}-1$ = no of states" | $2^{N}$ states, $2^{N}-1$ steps |
| V06-3 | ·CH4 slide 36 | inequality chain reversed, $2^{N} < 251$ | $2^{N} > 251$, $N = 8$ |
| V06-8 | ·CH4 slide 38 | $E = (2\ \text{mA}\times0.19)/100 = 3.8\ \mu$A | $E = 0.38$ mA $= 380\ \mu$A |
| V06-6 | ·CH4 slide 37 | $0.00244 = 0.244\,\%$ | $0.0244\,\%$ binary route, $0.1\,\%$ BCD route |
| V05-1 | ·CH4 slide 20 | $V_{\text{in}} > V_{\text{DAC}}$ ⇒ bit cleared | ⇒ bit **kept** |
| V02-3 | ·CH2 slide 10 | $\tau_{PHL}$ glossed "LOW to HIGH" | glosses interchanged; read the subscripts |
| V02-2 | ·CH2 slide 8 | $V_L$ "at the input" | $V_L$ is an **output** level |
| V07-3 | ·EXC | T characteristic table headed $D$ | headed $T$ |
| C07-2 | ·CH5 slide 28 | $D = JQ' + K'Q$, $D = T \oplus Q$ | $Q(t+1) = \ldots$ on both |
| C07-3 | ·CH5 slide 30 | $A(t+1) = JA' + K'A$ | $A(t+1) = J_A A' + K_A'A$ |
| C07-1 | ·CH5 slide 17 | $s' = ab\bar{s}+\bar{a}bs+a\bar{b}s+abs$ | $s' = ab + bs + as$ |
| C05-1 | ·CH4 slide 23 | $V_{red}$ in the denominator | $V_{REF}$ |
| C05-3 | ·CH4 slide 8 | prose "greater than", formula $\ge$ | $f_s > 2f_{\max}$ is the safe form |
| C06-5 | ·CH4 slide 39 | $V_{\text{out}} = I_f R_f$ | $V_{\text{out}} = -I_f R_f$ |
| V10-3 | ·CH6 slide 34 | $D_{G1}$ gate drawn as OR | AND |
| V04-1 | ·CH3 slide 52 | fuse-map column 3 labelled $B'$ below | $B$ — use the top label row |
| V06-4/5 | ·CH4 slide 37 | 12-bit BCD treated as $2^{12}-1 = 4095$ steps | 999 steps; step $= 10$ mV |

Full entries, with the reasoning for each, are in the verification log.
