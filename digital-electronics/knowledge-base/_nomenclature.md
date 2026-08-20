---
kb: "Digital Electronics — BEE 3102"
lecturer: "withheld"
file_role: nomenclature
purpose: "Every symbol used across the six chapter decks, with meaning and units. Resolves symbol clashes. Consult when a topic file's notation is ambiguous."
---

# Nomenclature and symbols

Six decks, one alphabet. This unit reuses letters harder than any other in the year: the same
capital $A$ is a state variable, an accumulator, a ROM data output and a Boolean input, all within
about eighty slides of each other. The clash table below comes first because it is the reason this
file exists.

Citations follow the topic files: ·CH4 slide 34 is slide 34 of Chapter 4, ·EXC is the separate
one-page excitation-table handout. Flag IDs (V05-1, C07-4, …) point into the per-file flag lists in
`flags/`.

---

## ⚠ Symbol clashes and look-alikes — read first

### Tier 1 — these change the answer

Get one of these wrong and the number at the bottom of the page is wrong. Check the tier before
starting any numerical question.

| Symbol | Meaning A | Meaning B | Disambiguation rule |
|---|---|---|---|
| **$2^{n}$ vs $2^{n}-1$** | **divide by $2^{n}$** — height of one quantisation zone, ADC half ·CH4 slides 12, 13, 15 (file 05) | **divide by $2^{N}-1$** — spacing of adjacent code outputs, DAC half ·CH4 slides 34–37, 48 (file 06) | **The single most common way to lose marks in this unit.** Both halves are internally consistent; they are four slides apart in one chapter. Rule: if the quantity given is a **full-scale output** — the voltage actually produced at the top code — there are $2^{N}-1$ steps below it, so divide by $2^{N}-1$. If a continuous **span** is being cut into bins, there are $2^{n}$ bins, so divide by $2^{n}$. They differ by $2^{N}/(2^{N}-1)$: 33 % at $N=2$, 0.39 % at $N=8$. See V06-1, V06-5 |
| **$m$ and $n$** | ·CH5 slide 22 (file 07): $m$ = **flip-flops**, $n$ = **external inputs**, state table has $2^{\,m+n}$ rows | ·CH5 slides 73, 92 (file 09): $m$ = **states**, $n$ = **flip-flops (state variables)**, $n = \lceil\log_2 m\rceil$ | **The two letters swap roles inside one chapter.** Reading slide 73's $m$ into slide 22's row formula inflates the table catastrophically. Rule: if the letter appears in an **exponent of 2**, it counts *bits*; if it appears inside a $\log_2$ or is being counted off a state graph, it counts *states* |
| **$k$** | number of **memory address lines**, so words $= 2^{k}$ ·CH3 slide 12 (file 03) | number of **Hamming check bits**, so $2^{k} \ge n+k+1$ ·CH3 slides 27, 30 (file 03) | Same file, same glyph, **both inside a boxed $2^{k}$ formula**. Rule: if $n$ alongside it means *word length in bits*, $k$ is address lines; if $n$ means *data bits being protected*, $k$ is check bits. In file 04 the same letter is also the PLA **product-term count** ·CH3 slide 45 |
| **$N$ vs $n$** | upper-case $N$ = bit count ·CH4 slides 34–37 (file 06) | lower-case $n$ = the same bit count ·CH4 slides 15, 44, 47 (files 05, 06) | One quantity, two glyphs, swapping halfway through Chapter 4 — and on slide 15 it swaps **two lines apart**. See C05-5, C06-6. Treat $N$ and $n$ as identical in CH4; but note $N$ is an SRAM **internal node** in file 03 ·CH3 slide 17, which is unrelated |
| **$A'$ (prime)** | **complement** of $A$ — the meaning in almost every slide of Chapter 5 | **next state** of $A$ ·CH5 slide 33 state-table heading, and $s'$ ·CH5 slides 16–17 | **Safe reading rule: prime means complement unless it sits in a state-table column heading or beside an explicit "next state" label.** Slide 33 uses both meanings eight lines apart — $C = A'C'$ (complement) above a column headed $A'B'C'$ at $(t+1)$ (next state). See C07-4. Where the deck means complement inside a derivation it usually switches to an **overbar** ($\bar{a}$, $\bar{s}$), which is the safer glyph |
| **$\Delta$** | **quantisation step** — height of one zone, in volts ·CH4 slides 11–13 (file 05) | the **sigma-delta difference signal** at the summing point ·CH4 slide 26 (file 05) | Same file, same letter, fifteen slides apart. Rule: $\Delta$ with a voltage value attached is the step; $\Delta$ named beside $\Sigma$ in a block diagram is the difference. Separately $\Delta V$ is the **logic swing** $V_H - V_L$ ·CH2 slide 14 (file 02) but **one flash-ladder LSB step** ·CH4 slide 15 (file 05) |
| **$S$** | a **state name** — $S_0, S_1, \ldots$ throughout Chapters 5 and 6 (files 07–10) | the **SET input** of an SR flip-flop ·EXC and ·CH3 slide 24 | Rule: **subscripted $S_i$ is a state; bare $S$ beside a bare $R$ in a four-row table is the set input.** A third meaning: bare $S$ is the **start signal** in file 10 ·CH6 slides 24, 36, and $St$ is the multiplier's start ·CH6 slide 14. A fourth: $S$ is the MOSFET **source** terminal ·CH2 slide 38 |
| **$D$** | the **D flip-flop input** ·CH1 slide 11, ·EXC, ·CH5 slide 26 | the **decimal equivalent of a DAC input code** ·CH4 slide 31 (file 06) | Rule: $D$ in a flip-flop context is an input pin taking 0 or 1; $D$ in $\text{Analogue out} = K \times D$ is an integer $0 \ldots 2^{N}-1$. Also: $D_7$, $D_{711}$, $D_{2312}$ = "**the dice sum is** 7 / 7 or 11 / 2, 3 or 12" ·CH6 slides 15–16 (file 10); $D_1 D_2 D_3$ = **input diodes** ·CH2 slide 26; $D$ = MOSFET **drain** ·CH2 slide 38; $D_{\text{IN}}$, $D_{\text{OUT}}$ = memory data lines ·CH3 slide 19. ⚠ Slide 28 of CH5 also writes $D$ on the **left** of the JK and T characteristic equations where $Q(t+1)$ belongs — see C07-2 |
| **$A$, $B$, $C$** | **state variables** of the machine ·CH5 slides 21, 93–98; ·CH6 slides 15–22 | **registers** — $A$ = accumulator, $B$ = multiplicand, $C$ = carry ·CH6 slide 13 (file 10) | Nothing carries over between the two. A third meaning: **Boolean input variables** in the PLA and PAL examples ·CH3 slides 45–51 (file 04). A fourth: $A_7 \ldots A_0$ are PROM **data outputs**, not addresses ·CH3 slides 42–43. A fifth: $A$ is a **4-bit counter** ·CH6 slide 24, and $A,B,C,D,E$ are **state names** ·CH5 slides 65–71 (file 08) |
| **$R$** | a **resistor** — ladder rung, integrator input, R/2R series arm (files 02, 05, 06) | an **asynchronous reset** pin, active low ·CH5 slide 31 (file 07) | Two more: the weighing machine's **right-shift register** ·CH6 slides 36–38, and the **"reverse" input** of the arc-labelling example ·CH5 slides 117–118. Plus the **RESET input** of an SR flip-flop ·EXC, and $R$ as shorthand for $Reset$ on one slide only ·CH6 slide 22. Rule: an $R$ with an ohms value is a resistor; an $R$ on a state-graph arc or a flip-flop pin is a control signal |
| **$T$** | the **toggle input** of a T flip-flop ·EXC, ·CH5 slide 31 | a **decoded control-state signal** $T_0 \ldots T_3$ ·CH6 slides 31–38 (file 10) | Two more: the **sampling interval** $T$ (also written $T_s$) ·CH4 slides 5, 7 — see C05-4 — and the dual-slope integrate/de-integrate times $T_1$, $T_2$ ·CH4 slide 25. Plus $T_1 \ldots T_6$, the **six transistors** of the CMOS SRAM cell ·CH3 slide 17, and column header **T** = output taken *true* in a PLA table ·CH3 slide 45. Rule: subscripted $T_i$ in Chapter 6 is one-hot control state; subscripted $T_A$, $T_B$ in Chapter 5 is a flip-flop input |
| **$\tau_{PHL}$ / $\tau_{PLH}$** | $\tau_{PHL}$ = output falling **HIGH to LOW**; $\tau_{PLH}$ = output rising **LOW to HIGH** ·CH2 slide 10 | the slide's own parenthetical glosses are **interchanged** — see V02-3 | **Read the subscripts, not the words.** The waveform beside the text agrees with the subscripts; the prose does not. File 01 writes the same two quantities as $t_{PHL}$, $t_{PLH}$ ·CH1 slide 10 — Roman $t$ there, Greek $\tau$ in file 02, same quantity |
| **$C_1$, $C_2$** | **complementary storage nodes** of the six-transistor SRAM cell ·CH3 slide 17 | **Hamming check bits** $C_1, C_2, C_4, C_8$ computed on read-back ·CH3 slide 28 | Eleven slides apart in the same file. Rule: subscripts $1,2$ only → SRAM nodes; subscripts running $1,2,4,8$ (powers of two) → check bits. Bare $C$ is then the **syndrome** $C_8C_4C_2C_1$ read as a number ·CH3 slide 29. In file 02, $C_1$ is the DTL **speed-up capacitor** ·CH2 slide 26 |

### Tier 2 — these confuse rather than corrupt

Same-letter collisions that a careful reader resolves from context, but which cost time under exam
pressure.

| Symbol | Meanings | Where | Disambiguation rule |
|---|---|---|---|
| **the output** | $y$, $Y$, $Z$, $z$, $o$, $w$ — **six symbols, one quantity** | $y$ ·CH5 slides 21, 31, 71; $Y$ ·CH5 slide 21 (same slide as $y$); $Z$ ·CH5 slides 33, 56, 57, 63 and throughout files 08–10; $z$ ·CH5 slides 15–17; $o$ ·CH5 slide 37; $w$ ·CH5 slide 41 | There is no rule beyond "whatever the slide in front of you calls it". **$Z$ is the unit's dominant name** and the one to use in an answer. Slide 21 alone prints the symbol table's $y$ and the equation's $Y$ for the same signal; slide 71 heads the column $y$ where slides 56, 57 and 63 head it $Z$ |
| **$Q$** | flip-flop **output / stored state**; a **transistor designator** $Q_1, Q_2$; the multiplier **register** | flip-flop: everywhere; transistors ·CH2 slides 23, 38–40; register ·CH6 slide 13 | Rule: $Q$ in a schematic of npn or MOS devices is a device label; $Q$ with $\overline{Q}$ beside it is a flip-flop output. $Q_1, Q_2, Q_3$ are also **state variables** ·CH5 slides 99–101 |
| **$K$** | JK flip-flop **input**; DAC **proportionality factor**; multiplier **counter flag**; the prefix $2^{10} = 1024$ | ·CH1 slide 18 and ·EXC; ·CH4 slide 31; ·CH6 slide 14; ·CH3 slide 11 | Rule: $K$ next to a $J$ is a flip-flop input; $K$ with volts-per-step units is the DAC factor; $K$ attached to a memory size is 1024. Lower-case $k$ is never any of these — see Tier 1 |
| **$X$ and $\times$** | the machine **input** variable; a **don't-care** entry; **fuse intact**; "these two states are **not** equivalent"; "**required twice**" | input ·CH5 slides 75–118, ·CH6 slide 10; don't-care ·EXC, ·CH6 slide 22; fuse ·CH3 slides 39, 45, 49; implication table ·CH5 slides 84–88; multiplicity ·CH5 slides 95, 99 | Rule: **italic $X$ is a variable; upright X or $\times$ is a mark.** In a K-map or excitation table the mark means don't-care; in a fuse map it means intact; in an implication table it means incompatible. $X$ is also the absorption-identity dummy ·CH6 slide 9 |
| **$P$ / $p$** | Hamming **parity bit** $P_1, P_2, P_4, P_8$ and overall parity $P$; the multiplier's **shift counter**; a PLA **product term** $P_i$;  **power** $P_{D(\text{avg})}$; one of a **pair of states** $p, q$ | ·CH3 slides 27–30; ·CH6 slide 13; ·CH3 slide 39; ·CH2 slide 15; ·CH5 slide 82 | Also a **state name** in the fifteen-state example ·CH5 slides 75–81. Lower-case $p$ is the PLD **product-term count** ·CH3 slide 37 — the deck relabels the very same count $k$ on slide 45 |
| **$A$ and $I$ on a ROM** | $A_0 \ldots A_{n-1}$ = **data outputs**; $I_0 \ldots I_{k-1}$ = **address inputs** | ·CH3 slides 31, 42–43 (files 03, 04) | **Backwards from intuition** — $A$ looks like "address" and is not. The deck reuses $A$ without comment. Rule: on a ROM or PROM diagram, $I$ goes in and $A$ comes out |
| **$F$** | the **next-state logic** block; the **"forward" input**; a **flip-flop** in the datapath examples; $F_1, F_2$ = **Boolean output functions** | ·CH5 slide 5; ·CH5 slides 117–118; ·CH6 slides 24, 36; ·CH3 slides 46–49 | Rule: $F$ inside a block diagram of an FSM is the next-state function; $F$ on a state-graph arc is an input; $F$ in a register list is a flip-flop. Also a **state name** ·CH5 slides 77–81, 99–101 |
| **$Z$** | the machine **output**; the **zero flag** of the weighing machine; a PAL **output function** $z$ | output: everywhere; zero flag ·CH6 slides 36–38; PAL ·CH3 slide 51 | Rule: $Z$ produced by the control is an output; $Z$ consumed *by* the control as a branch condition is a status flag from the datapath |
| **$V_L$ vs $V_{IL}$** | $V_L$ = nominal low level **at the output**; $V_{IL}$ = maximum input voltage read as low | ·CH2 slide 8 | ⚠ The slide defines $V_L$ as being "at the **input**" — wrong, see V02-2. That reading collides with $V_{IL}$ and breaks $NM_L = V_{IL} - V_{OL}$ on the next slide |
| **$NM_L$, $NM_H$ vs $V_{NL}$, $V_{NH}$** | two names for the same two noise margins | ·CH2 slide 12 uses $NM$; slide 13 works the same example with $V_N$ | Identical quantities. See C02-1. Either name is acceptable in an answer; do not mix them in one working |
| **$C$** | **clock** pin label; **carry** out; **check bit**; **state variable**; **load capacitance** $C_L$; **hold capacitor** $C_H$; PLA column meaning *complement* | ·CH1 slide 14; ·CH6 slides 13–14; ·CH3 slide 28; ·CH5 slide 93; ·CH1 slide 10; ·CH4 slide 10; ·CH3 slide 45 | Rule: **$C$ with a farad value is a capacitor; $C$ as a column header in a PLA table means "output taken complemented", not the input variable $C$** — both appear on slide 45 |
| **$E$** | **error** in the full-scale-error formula; a **flip-flop** in the Example 1 datapath; $E_1 \ldots E_4$ = **map-entered variables**; a **state name** | ·CH4 slide 38; ·CH6 slides 24–35; ·CH6 slide 22; ·CH5 slides 65–81 | Rule: $E$ with a current or voltage value is an error; $E$ in a register list is a flip-flop |
| **$G$** | the **output logic** block of an FSM; MOSFET **gate** terminal; $G_1, G_0$ = **state flip-flops** of a controller; the prefix $2^{30}$ | ·CH5 slide 5; ·CH2 slide 38; ·CH6 slides 31–35; ·CH3 slide 11 | Rule: $G$ alone in a block diagram is the output function; subscripted $G_1, G_0$ in file 10 are flip-flops |
| **$M$** | the multiplier **bit** in the LSB position; the prefix $2^{20}$; a **MOSFET** designator $M_S$ | ·CH6 slide 14; ·CH3 slide 11; ·CH2 slide 7 | Also a **state name** ·CH5 slides 75–81 |
| **$L$** | number of **quantisation levels** $L = 2^{n}$; the subscript **L** meaning LOW ($V_L$, $NM_L$, $I_{IL}$, $R_L$, $C_L$) | ·CH4 slides 5, 11–13; throughout file 02 | Rule: standalone italic $L$ is a level count; $L$ as a subscript is the word "low" |
| **$W$** | the weighing machine's **up-counter**; the $\overline{W}$ of $R/\overline{W}$, meaning **write**; WL = **word line** | ·CH6 slides 36–38; ·CH3 slide 19; ·CH3 slide 17 | Rule: an overbarred or slashed $W$ is a control input; a bare italic $W$ in file 10 is a register |
| **$w$, $x$, $y$, $z$ in the PAL example** | four **output functions**, not inputs | ·CH3 slide 51 (file 04) | ⚠ $x$ was the **dummy variable** of the XOR polarity identity nine slides earlier, and $w$ also appears as a **column literal** in the same fuse map because the PAL feeds $w$ back into its own AND array |
| **$1$ in "1D" and "C1"** | a **pin identifier**, cross-referencing clock to data | ·CH1 slide 11 | **Not a logic level.** On slide 18 the digit tied to $J$ and $K$ *is* a genuine logic HIGH. Same glyph, one slide is labelling, the other is data |
| **$\delta$ / $\lambda$ vs $\Delta$ / $\Sigma$** | $\delta$ = next-state function, $\lambda$ = output function | ·CH5 slides 40, 82 (files 08, 09) | Lower-case Greek are FSM **functions**; upper-case Greek in file 05 are **signals** — $\Delta$ the difference, $\Sigma$ the summing junction |
| **$V_{\text{REF}}$ vs $V_{red}$** | converter **reference voltage** | ·CH4 slides 15, 19, 23 | ⚠ Slide 23 prints $V_{red}$, which is not a quantity defined anywhere. Read $V_{\text{REF}}$ — see C05-1 |

---

## Symbol tables by domain

Tables follow the teaching order of the topic files. The **file** column is the symbol's home; a
symbol listed twice has two homes and appears in the clash table above.

### 1. Recap symbols — flip-flops, registers, counters

·CH1 slides 6–20 · file 01

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $+V_s$ | positive supply rail; the voltage representing logic 1 | V | not given in CH1 |
| $D$ | data input of a D flip-flop, pin marked $1\text{D}$ | — | 0 or 1 |
| $Q$ | flip-flop output, i.e. the stored state | — | 0 or 1 |
| $Q(t)$ | present state, immediately before the active clock edge | — | 0 or 1 |
| $Q(t+1)$ | next state, immediately after the active clock edge | — | 0 or 1 |
| CLOCK | clock input, pin marked $\text{C}1$ | — | — |
| $J$, $K$ | the two control inputs of a JK flip-flop | — | 0 or 1 |
| $t_{pd}$ | clock-edge-to-output delay of one stage | ns | 1 |
| $t_{pd,\text{total}}$ | worst-case delay, clock edge to last stage settling | ns | 3 for $n = 3$ |
| $t_{PHL}$ | delay to the output going HIGH to LOW | ns | 4.5 (74AC00) |
| $t_{PLH}$ | delay to the output going LOW to HIGH | ns | 6.0 (74AC00) |
| $C_L$ | output load capacitance at which delays are quoted | pF | 30 |
| $n$ | number of bits, i.e. number of flip-flops or counter stages | — | 2, 3, 4, 8 |
| $D_i$ | parallel data input of bit $i$ | — | 0 or 1 |
| $Q_i$ | parallel data output of bit $i$ | — | 0 or 1 |
| $Q_A \ldots Q_D$ | the four stage outputs of the synchronous counter, $Q_A$ = l.s.b. | — | 0 or 1 |
| $SI$ | serial input of a shift register | — | 0 or 1 |
| $SO$ | serial output of a shift register | — | 0 or 1 |
| $N_{\text{shift}}$ | clock pulses needed to load a word serially | — | 4 for a nibble |

### 2. Logic levels, timing and loading

·CH2 slides 5–19 · file 02

| Symbol | Quantity | Units | Typical value (TTL) |
|---|---|---|---|
| $v_I$ | instantaneous input voltage | V | 0 to 5 |
| $v_O$ | instantaneous output voltage | V | 0 to 5 |
| $V_+$, $V_-$ | positive and negative supply rails | V | 5, 0 |
| $V_H$ | nominal high-logic voltage **at the output** | V | 3.4 |
| $V_L$ | nominal low-logic voltage **at the output** | V | 0.2 — ⚠ slide 8 says "at the input"; see V02-2 |
| $V_{OH}$ | guaranteed output voltage for an input of $V_{IL}$ | V | 2.4 min |
| $V_{OL}$ | guaranteed output voltage for an input of $V_{IH}$ | V | 0.4 max |
| $V_{IH}$ | minimum input voltage recognised as a high level | V | 2.0 |
| $V_{IL}$ | maximum input voltage recognised as a low level | V | 0.8 |
| $V_{REF}$ | switching threshold of the ideal inverter | V | 2.5 |
| $V_{50\%}$ | mid-swing reference level, $(V_H + V_L)/2$ | V | 1.8 |
| $V_{10\%}$, $V_{90\%}$ | rise/fall reference levels, $V_L + 0.1\Delta V$ and $V_L + 0.9\Delta V$ | V | — |
| $\Delta V$ | logic swing, $V_H - V_L$ | V | 3.2 |
| $\tau_{PHL}$ | propagation delay, output HIGH to LOW | s | 10 ns — ⚠ V02-3 |
| $\tau_{PLH}$ | propagation delay, output LOW to HIGH | s | 10 ns — ⚠ V02-3 |
| $\tau_P$ | average propagation delay, $(\tau_{PHL}+\tau_{PLH})/2$ | s | 10 ns |
| $t_r$ | rise time, 10 % to 90 % | s | 5 ns |
| $t_f$ | fall time, 90 % to 10 % | s | 5 ns |
| fan-in | number of inputs the gate provides | — | 2 to 8 |
| fan-out | number of driven inputs one output supports | — | 10 (standard TTL) |
| $NM_H$ | high-level noise margin, $V_{OH} - V_{IH}$ | V | 0.4 |
| $NM_L$ | low-level noise margin, $V_{IL} - V_{OL}$ | V | 0.4 |
| $V_{NH}$, $V_{NL}$ | the deck's alternative names for $NM_H$, $NM_L$ ·CH2 slide 13 | V | — |
| $V_{CC}$ | supply rail of a bipolar (TTL) part | V | 5 |
| $V_{DD}$ | supply rail of a MOS part | V | 5 or 3.3 |
| $I_{CCH}$ | supply current with the output HIGH | A | 2 mA |
| $I_{CCL}$ | supply current with the output LOW | A | 3.6 mA |
| $I_{CC(\text{avg})}$ | average supply current, $(I_{CCH}+I_{CCL})/2$ | A | 2.8 mA |
| $P_{D(\text{avg})}$ | average power dissipation, $V_{CC} I_{CC(\text{avg})}$ | W | 14 mW |
| $I_{IH}$ | current into a load input held HIGH | A | 40 µA |
| $I_{IL}$ | current out of a load input held LOW | A | 1.6 mA |

### 3. Device and circuit designators

·CH2 slides 21–42 · files 02, 05, 06

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $Q_1, Q_2, \ldots$ | switching transistors (npn in RTL, complementary pair in CMOS) | — | ⚠ not a flip-flop output here |
| $Q_S$ | the npn transistor standing in for the switch in the model inverter | — | — |
| $M_S$ | the n-channel MOSFET standing in for the same switch | — | — |
| $i_C$, $i_D$ | collector current, drain current of those devices | A | — |
| $D_1, D_2, D_3$ | input **diodes** of a DTL gate | — | — |
| $R_C$ | collector load resistor (RTL) | Ω | 640 |
| $R_1, R_2, R_3, R_4$ | base, phase-splitter, pull-up and emitter resistors (RTL, DTL, TTL) | Ω | 450 Ω – 4 kΩ |
| $R_L$ | collector load resistor (DTL) | Ω | 2 k |
| $C_1$ | speed-up capacitor across $R_2$ (DTL) | F | 100 pF |
| $-V_{BB}$ | negative bias rail holding the base off (DTL) | V | −2 |
| $V_{BE}$ | base-emitter drop of a conducting transistor | V | 0.7 |
| $V_{CE(\text{sat})}$ | collector-emitter voltage of a saturated transistor | V | 0.2 |
| $V_{GS}$ | gate-to-source voltage of a MOSFET | V | 0 to 5 |
| G, D, S | gate, drain, source terminals | — | ⚠ D here is a terminal, not a flip-flop input |
| $R_i$, $R_f$ | input and feedback resistors of an inverting op-amp stage | Ω | file 05 ·CH4 slide 14; file 06 ·CH4 slide 39 |
| $A_1$, $A_2$ | integrator op-amp and comparator op-amp of the dual-slope ADC | — | ·CH4 slide 25 |

### 4. Memory organisation

·CH3 slides 3–25, 31–33 · file 03

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $k$ | number of **address lines** on a memory unit | — (count) | 8 – 32 |
| $n$ | number of bits in one word (word length) | bit | 1, 8, 16 |
| $2^{k}$ | number of addressable words | word | 1024, 65536 |
| $2^{k} \times n$ | memory capacity, and the way a part is described | bit | $32 \times 8$ |
| K, M, G | the prefixes $2^{10}$, $2^{20}$, $2^{30}$ | — | 1024; 1 048 576; 1 073 741 824 |
| cell | one storage element holding a single 1 or 0 | — | — |
| address | location of a unit of data within the array | — | $0 \ldots 2^{k}-1$ |
| Memory Enable | chip-level enable input | logic level | 0 or 1 |
| Read/Write | direction-control input | logic level | 0 = write, 1 = read |
| $R/\overline{W}$ | the same control drawn as read HIGH / write LOW | logic level | 0 or 1 |
| Select | cell-select (row-select) input of an SRAM cell | logic level | 0 or 1 |
| $N$ | internal node at the select-gate output | logic level | ⚠ not the DAC bit count |
| $Q$, $\overline{Q}$ | the latch's complementary outputs | logic level | 0 or 1 |
| $C_1$, $C_2$ | complementary **storage nodes** of the six-transistor cell | logic level | ⚠ not Hamming check bits |
| $T_1 \ldots T_6$ | the six transistors of the CMOS SRAM cell | — | — |
| WL | word line — the address line of the cell | logic level | 0 or 1 |
| BL, $\overline{\text{BL}}$ | complementary bit lines | logic level | 0 or 1 |
| Row, Column | word line and bit line of a DRAM cell | logic level | 0 or 1 |
| $D_{\text{IN}}$, $D_{\text{OUT}}$ | data in to the input buffer, data out of the sense amplifier | logic level | 0 or 1 |
| Refresh | refresh-buffer enable | logic level | 0 or 1 |
| BC | binary cell — the one-bit storage block of a decoded array | — | — |
| $S$, $R$ | set and reset inputs of the binary cell's internal latch | logic level | 0 or 1 |
| EN | decoder enable, driven by Memory enable | logic level | 0 or 1 |
| $\overline{\text{RAS}}$ | row address strobe, active low | logic level | 0 or 1 |
| $\overline{\text{CAS}}$ | column address strobe, active low | logic level | 0 or 1 |
| $A_0 \ldots A_{n-1}$ | ROM **data outputs** | logic level | ⚠ outputs, not addresses |
| $I_0 \ldots I_{k-1}$ | ROM **address inputs** | logic level | ⚠ inputs |

### 5. Hamming codes and error control

·CH3 slides 26–30 · file 03

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $n$ | number of **data** bits in the word | bit | 8 |
| $k$ | number of **check (parity)** bits added | bit | 4 |
| $2^{k} \ge n+k+1$ | the condition fixing $k$ for a given $n$ | — | $n=8 \Rightarrow k=4$ |
| $n_{\max} = 2^{k}-k-1$ | largest data word a given $k$ protects | bit | $k=4 \Rightarrow 11$ |
| $P_1, P_2, P_4, P_8$ | parity bits, at the power-of-two positions | bit | 0 or 1 |
| $C_1, C_2, C_4, C_8$ | **check bits** computed on read-back | bit | ⚠ not SRAM nodes |
| $C$ | the syndrome, $C_8C_4C_2C_1$ read as a binary number | — | $0 \ldots 12$; 0 = no error |
| $P$ | overall parity bit for SEC-DED | bit | 0 or 1 |

### 6. Programmable logic

·CH3 slides 34–66 · file 04

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $n$ | number of input lines to the PLD | — (count) | 3 – 16 |
| $p$ | number of product-term lines the AND array produces | — (count) | 4 – 64 |
| $k$ | the deck's alternative letter for $p$ ·CH3 slide 45 | — (count) | 4 |
| $m$ | number of output lines the OR array produces | — (count) | 2 – 8 |
| $A, B, C, D$ | Boolean **input** variables | — (0/1) | — |
| $a, b, c, d$ | Boolean input literals feeding one gate | — (0/1) | — |
| $F_1, F_2$ | Boolean **output** functions | — (0/1) | — |
| $P_i$ | the $i$-th product term on a product-term line | — (0/1) | — |
| $c_{ij}$ | crosspoint state joining product $i$ to output $j$; 1 = link intact | — (0/1) | 0 or 1 |
| $\times$ | fusible link **intact** at that crosspoint | — | ⚠ a mark, not a variable |
| $+$ | fuse **blown** ·CH3 slide 45 | — | ⚠ slide 49 misprints this as "1"; see C04-1 |
| $\bullet$ | **hard-wired** connection, not fusible | — | — |
| $I_4 \ldots I_0$ | PROM address inputs | — (0/1) | five in the worked example |
| $A_7 \ldots A_0$ | PROM data outputs | — (0/1) | eight in the worked example |
| $2^{n}$ | number of words a decoder of $n$ inputs selects | — (count) | $2^5 = 32$ |
| T | output taken **true** — its XOR input tied to 0 | — | — |
| C | output taken **complemented** — its XOR input tied to 1 | — | ⚠ not the input variable $C$ |
| $\oplus$ | exclusive-OR | — | — |
| $w, x, y, z$ | the four PAL **output** functions | — (0/1) | ⚠ outputs, not inputs |
| $w'$ | complement of the fed-back output $w$ | — (0/1) | — |
| $X$ | output of the small three-gate PAL ·CH3 slide 50 | — (0/1) | — |
| CLK | common clock to every flip-flop in the device | — (0/1) | — |
| OE | output-enable controlling the three-state buffers | — (0/1) | ⚠ slide 58 prints "EO"; see C04-2 |
| $D$, $Q$ | macrocell flip-flop data input and output | — (0/1) | $Q$ also feeds back into the array |
| CLB | configurable logic block (also LAB, logic array block) | — (count) | not given in the deck |
| LUT | look-up table — a truth table stored in SRAM | bit | not given in the deck |

### 7. Signal conversion — analogue to digital

·CH4 slides 3–29 · file 05

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $x(t)$ | continuous-time (analogue) signal | V | — |
| $x[n]$ | discrete-time sample sequence | V | — |
| $t$ | time | s | — |
| $n$ | sample index in $x[n]$; elsewhere the bit count | — | $0, 1, 2, \ldots$ |
| $T$, $T_s$ | sampling interval — the deck uses both on one slide | s | 25 µs — see C05-4 |
| $f_s$, $f_{\text{sample}}$ | sampling rate | Hz (samples/s) | 40 kHz |
| $f_{\max}$ | highest frequency present in the signal | Hz | 20 kHz |
| $f_c$ | cut-off frequency of the anti-aliasing filter | Hz | — |
| $C_H$ | hold capacitor storing the sampled level | F | — |
| $L$ | number of quantisation levels (zones), $L = 2^{n}$ | — | 4, 16 |
| $n$ | bits per code word | — | 2, 3, 4, 8, 12 |
| $\Delta$ | **quantisation step** — the height of one zone | V | ⚠ also the sigma-delta difference |
| $\max$, $\min$ | upper and lower limits of the sampled amplitude range | V | — |
| $e_q$ | quantisation error | V | $\le \Delta/2$ |
| $V_{\text{in}}$ | held analogue input from the sample-and-hold | V | 0 to $V_{\text{REF}}$ |
| $V_{\text{out}}$ | op-amp output voltage | V | — |
| $V_{\text{REF}}$ | converter reference voltage, top of the ladder | V | +8 V; ⚠ printed $V_{red}$ on slide 23 |
| $\Delta V$ | resolution — one step of the flash ladder, $V_{\text{REF}}/2^{n}$ | V | 1 V |
| $R$ | one rung of the reference ladder | Ω | $2^{n}$ equal rungs give $2^{n}-1$ taps |
| $D_2 D_1 D_0$ | parallel binary output of the 3-bit flash converter | logic | — |
| $V_{\text{DAC}}$ | DAC output fed back to the SAR comparator | V | — |
| $T_{\text{CLK}}$ | clock period | s | 1 µs |
| $t_{\text{conv}}$ | conversion time, $n\,T_{\text{CLK}}$ for the SAR | s | 4 µs |
| $-V_{\text{REF}}$ | opposite-polarity reference, dual-slope phase 2 | V | — |
| $R$, $C$ | dual-slope integrator input resistor and feedback capacitor | Ω, F | — |
| $T_1$, $T_2$ | fixed integrate time, variable de-integrate time | s | ⚠ not control states |
| $\Sigma$ | the summing junction of the sigma-delta modulator | — | — |

### 8. Signal conversion — digital to analogue

·CH4 slides 30–49 · file 06

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $K$ | proportionality factor — the analogue change per LSB; the slide's "resolution" | V (or A) per step | 0.5 V |
| $D$ | **decimal equivalent** of the applied binary code | — | 0 to $2^{N}-1$ |
| $N$ | number of input bits | — | 4, 5, 8, 10, 12; lower-case $n$ on slides 44, 47 |
| $V_{\text{FS}}$ | full-scale output — the output at the largest code | V (or A) | 5 V, 9.99 V |
| $V_{\text{res}}$ | resolution — one step of the output, $V_{\text{FS}}/(2^{N}-1)$ | V (or A) | 4.888 mV |
| $2^{N}-1$ | number of **steps** from zero code to full-scale code | — | 255, 1023, 4095 |
| $2^{N}$ | number of **states** (distinct output levels) | — | 256, 1024, 4096 — ⚠ V06-1 |
| $\%\,\text{res}$ | resolution as a percentage of full scale, $100/(2^{N}-1)$ | % | 0.39 % |
| $E$ | error — actual output minus expected output | V or A | 0.38 mA |
| $V_{\text{exp}}$ | expected (original) value, taken at full scale | V or A | 2 mA |
| $\text{FSE}$ | full-scale error, $100\,E/V_{\text{exp}}$ | % | ±19 % |
| $V$ | input HIGH level applied to a weighted resistor | V | +5.0 V, +3.0 V |
| $V_S$ | input HIGH level driving the R/2R ladder | V | +5.0 V |
| $R$ | smallest input resistor (MSB), or the series arm of the ladder | Ω | 25 kΩ |
| $2R$ | the larger ladder value — input legs, terminator, feedback | Ω | 50 kΩ |
| $R_f$ | op-amp feedback resistor | Ω | 10 kΩ, or $2R$ |
| $R_{\text{EQ}}$ | equivalent resistance of the ladder seen from a node | Ω | $2R$ |
| $V_{\text{TH}}$, $R_{\text{TH}}$ | Thévenin voltage and resistance of the section left of a node | V, Ω | 2.5 V, $R$ |
| $I_i$ | current injected by bit $i$ | A | 0.025 mA |
| $I_f$ | total current through $R_f$ | A | 0.375 mA |
| $D_i$ | logic level on bit $i$; $D_0$ is the LSB | logic | 0 or 1 |
| $i$ | bit number, $i = 0$ for the LSB | — | 0 to $n-1$ |
| LSB | one least-significant-bit step of the output | V or A | — |
| accuracy | agreement between actual and expected output | % or LSB | $\pm\tfrac12$ LSB |

### 9. Finite state machines — structure and analysis

·CH5 slides 3–38 and ·EXC · file 07

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $n$ | number of storage bits (flip-flops) in the machine | — | 1 – 8 |
| $2^{n}$ | number of distinct states those bits can hold | — | 2, 4, 8, 256 |
| $Q_0 \ldots Q_{m-1}$ | flip-flop outputs — together, the current state | logic level | 0 or 1 |
| $m$ | number of **flip-flops** ·CH5 slides 5, 22 | — | 2 |
| $n$ | number of **external inputs** ·CH5 slide 22 | — | 1 |
| $2^{\,m+n}$ | rows a state table needs | — | 8 |
| $F$, $G$ | next-state logic and output logic (both combinational) | — | — |
| $F_1, G_1$ / $F_2, G_2$ | those two functions for the Mealy and Moore models | — | — |
| $A$, $B$, $C$ | flip-flop outputs — the state variables | logic level | 0 or 1 |
| $A'$, $B'$ | **complements** of $A$ and $B$ | logic level | ⚠ prime = complement |
| $A(t+1)$ | value of $A$ one clock edge later | logic level | 0 or 1 |
| $t$ | present clock-period index | — | — |
| $x$ | external input | logic level | 0 or 1 |
| $y$, $Y$, $Z$, $o$ | external output — four of the unit's six names for it | logic level | 0 or 1 |
| $x/y$ | state-diagram arc label: input, then output | — | e.g. $1/0$ |
| $a$, $b$ | the serial adder's two input bit streams, LSB first | logic level | 0 or 1 |
| $z$ | the serial adder's sum bit for the current column | logic level | 0 or 1 |
| $s$ | present state — the carry **into** the current column | logic level | 0 or 1 |
| $s'$ | **next state** — the carry **out** of the column | logic level | ⚠ prime = next state here |
| $S_0$, $S_1$ | the states "no carry in" and "carry in" | — | encoded $s = 0$, $s = 1$ |
| $S$, $R$ | **set** and **reset** inputs of an SR flip-flop | logic level | undefined when $S = R = 1$ |
| $D$ | data input of a D flip-flop | logic level | 0 or 1 |
| $J$, $K$ | the two inputs of a JK flip-flop | logic level | 0 or 1 |
| $T$ | toggle input of a T flip-flop | logic level | 0 or 1 |
| $D_A$, $J_A$, $K_A$, $T_A$ | the input(s) driving the flip-flop whose output is $A$ | logic level | subscript names the flip-flop |
| $Q(t)$, $Q(t+1)$ | present state and next state of a generic flip-flop | logic level | 0 or 1 |
| $Q'$ | complement of the present state | logic level | 0 or 1 |
| X | don't-care — either value works | — | excitation tables |
| $R$ | active-low **asynchronous reset** ·CH5 slide 31 | logic level | 0 or 1 |
| $S_0 \ldots S_3$ | named states of a Mealy machine | — | — |
| $\oplus$ | exclusive-OR | — | — |

### 10. FSM design, state reduction and state assignment

·CH5 slides 39–118 · files 08, 09

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $X$, $x$ | serial input bit applied once per clock | — | 0 or 1 |
| $Z$, $z$, $w$, $y$ | serial output bit — four more names for the same signal | — | 0 or 1 |
| $t$ | clock-period index | — | $0, 1, 2, \ldots$ |
| $S(t)$ | present state during period $t$ | — | $S_0, S_1, \ldots$ |
| $\delta$ | next-state function, $S(t+1) = \delta(S(t), X(t))$ | — | — |
| $\lambda$ | output function; Mealy $\lambda(S,X)$, Moore $\lambda(S)$ | — | — |
| $S_n/Z$ | Moore state label — state name, then the output produced *in* it | — | $S_3/1$ |
| $Z_{\text{Mealy}}(t)$, $Z_{\text{Moore}}(t)$ | the two outputs compared period by period | — | Moore lags Mealy by one clock |
| $A \ldots P$ | state names in the fifteen-state example (letter $O$ skipped) | — | ·CH5 slides 75–81 |
| $a \ldots h$ | state names in the implication-table example | — | ·CH5 slides 83–90 |
| $m$ | number of **states** in the state table ·CH5 slides 73, 92 | — | 3 to 20 |
| $n$ | number of **flip-flops** (state variables), $n = \lceil\log_2 m\rceil$ | — | 2 to 5 |
| $p$, $q$ | two states being compared for equivalence | — | — |
| $\lambda(p,X)$ | output produced in state $p$ with input $X$ | — | 0 or 1 |
| $\delta(p,X)$ | next state entered from $p$ with input $X$ | — | a state name |
| $\equiv$ | "is equivalent to" | — | — |
| square $i$-$j$ | the implication-chart cell for the pair of states $i$, $j$ | — | — |
| implied pair | a pair whose equivalence is *required* for the square's pair | — | — |
| $\times$ | "these two states are **not** equivalent" | — | ⚠ also written $\times 2$ for "required twice" |
| $A$, $B$, $C$ | state variables, present-state code $ABC$ | — | 0 or 1 |
| $A^{+}$, $B^{+}$, $C^{+}$ | next values of those variables | — | 0 or 1 |
| $Q_1, Q_2, Q_3$ | state variables in the six-state example | — | 0 or 1 |
| $D_1, D_2, D_3$ | the D flip-flop inputs driving them | — | 0 or 1 |
| adjacent | two state codes differing in exactly one bit | — | — |
| bit time | duration of one data bit on the line | s | $1/f_{\text{bit}}$ |
| $d^{-}$ | the previous level on the line | — | 0 or 1 |
| Clock2 | clock at **twice** the bit rate, for Manchester encoding | Hz | $2 f_{\text{bit}}$ |
| $F$ | the "forward" input of the arc-labelling example | — | 0 or 1 |
| $R$ | the "reverse" input of the same example | — | ⚠ not a resistor or a reset |
| $Z_1, Z_2, Z_3$ | the three outputs of that machine | — | 0 or 1 |

### 11. ASM charts and datapath control

·CH6 slides 2–40 · file 10

| Symbol | Quantity | Units | Typical value or note |
|---|---|---|---|
| $S_i$ | a state of the machine | — | $S_0, S_1, \ldots$ |
| $X_i$, $Z_i$ | an input to, and an output of, the machine | — | 0 or 1 |
| state name | the label written **inside** a state box | — | $S_0$, $T_1$ |
| state code | the assigned binary code, written **outside** the box at the top | — | 00, 011 |
| output list | outputs asserted for the whole clock period | — | Roll, Sp |
| condition | the Boolean expression tested by a decision box | — | $Rb$, $A + BC$ |
| entrance path | the single path by which control enters an SM block | — | 1 per block |
| exit path | a path by which control leaves an SM block | — | $n \ge 1$ per block |
| link path | a path from one state box's entrance to the next | — | — |
| $Q$ | any one state variable (flip-flop) | — | $A$, $B$, $C$ |
| $Q^{+}$ | the **next value** of that state variable | — | 0 or 1 |
| $Z_a, Z_b, Z_c$ | state (Moore) outputs, one per state | — | 0 or 1 |
| $Z_1, Z_2$ | conditional (Mealy) outputs, asserted in one state only | — | 0 or 1 |
| $X$, $Y$ | the dummy expressions of the absorption identity $X + X'Y = X + Y$ | — | ⚠ not the machine's input |
| multiplicand, multiplier | the number added repeatedly; the number selecting the additions | — | 1101, 1011 |
| ACC | accumulator, the upper part of the product register | — | 5 bits |
| $M$ | the multiplier bit currently in the LSB position | — | 0 or 1 |
| $St$ | start signal into the multiplier control | — | 0 or 1 |
| $K$ | counter flag, set to 1 just before the last shift | — | ⚠ not a JK input |
| $Load$, $Sh$, $Ad$, $Done$ | control outputs — load, shift right, add, finished | — | 0 or 1 |
| $C_4$ | carry out of the 4-bit adder | — | 0 or 1 |
| $B$, $Q$, $A$, $C$, $P$ | ·CH6 slide 13 only: multiplicand register, multiplier register, accumulator, carry, shift counter | — | ⚠ nothing carries over from slide 12 |
| $D_7$ | dice input — 1 if the sum of the dice is 7 | — | 0 or 1 |
| $D_{711}$ | dice input — 1 if the sum is 7 or 11 | — | 0 or 1 |
| $D_{2312}$ | dice input — 1 if the sum is 2, 3 or 12 | — | 0 or 1 |
| $Eq$ | 1 if the sum equals the number in the point register | — | 0 or 1 |
| $Rb$ | 1 when the roll button is pressed | — | 0 or 1 |
| $Reset$ | 1 when the reset button is pressed; shortened to $R$ ·CH6 slide 22 | — | 0 or 1 |
| $Roll$, $Sp$, $Win$, $Lose$ | outputs — enable counters, store point, win light, lose light | — | 0 or 1 |
| $ABC$ | the three dice-game state variables | — | 000 … 101 |
| — (dash) | a don't-care entry in the PLA table | — | ·CH6 slide 20 |
| $E_1 \ldots E_4$ | map-entered variables — expressions written into a K-map cell | — | ·CH6 slide 22 |
| X | a don't-care cell (states 110 and 111) | — | ·CH6 slide 22 |
| $A$ | a 4-bit binary counter | — | 0000 … 1111 |
| $A_4, A_3, A_2, A_1$ | the individual flip-flops of $A$, $A_4$ holding the MSB | — | ⚠ slide 30 renumbers them $A_3 \ldots A_0$; see C10-2 |
| $E$, $F$ | the two datapath flip-flops of Example 1 | — | 0 or 1 |
| $S$ | the start signal | — | 0 or 1 |
| $T_0, T_1, T_2$ | decoded control-state signals, one active at a time | — | ⚠ not toggle inputs |
| $G_1, G_0$ | the two state flip-flops of the Example 1 control | — | 0 or 1 |
| $D_{G1}, D_{G0}$ | the D inputs of those flip-flops | — | 0 or 1 |
| $R$ | the weighing machine's right-shift register | — | 1011 |
| $W$ | the weighing machine's up-counter (the running weight) | — | 0000 … 1111 |
| $F$ | flip-flop holding the bit just shifted out of $R$ | — | 0 or 1 |
| $Z$ | **zero flag** — 1 when $R = 0$ | — | ⚠ a status input, not an output |
| $T_0 \ldots T_3$ | the four weighing-machine control states | — | one active at a time |

---

## Conventions and abbreviations

### Subscript conventions

| Pattern | Reads as | Example |
|---|---|---|
| first letter **O** | measured at the **output** | $V_{OH}$, $V_{OL}$ |
| first letter **I** | measured at the **input** | $V_{IH}$, $V_{IL}$, $I_{IH}$, $I_{IL}$ |
| second letter **H** | the **HIGH** logic state | $V_{OH}$, $I_{CCH}$, $NM_H$ |
| second letter **L** | the **LOW** logic state | $V_{OL}$, $I_{CCL}$, $NM_L$ |
| **PHL**, **PLH** | **P**ropagation delay, output going **H**igh-to-**L**ow / **L**ow-to-**H**igh | $\tau_{PHL}$, $t_{PLH}$ |
| doubled letter | a **supply rail** at the named terminal | $V_{CC}$ (collector), $V_{DD}$ (drain), $V_{BB}$ (base) |
| $(\text{sat})$, $(\text{avg})$, $(\min)$, $(\max)$ | operating condition or statistic | $V_{CE(\text{sat})}$, $I_{CC(\text{avg})}$, $V_{IH(\min)}$ |

$V_H$ and $V_L$ without a first letter are the **nominal** output levels; $V_{OH}$ and $V_{OL}$ are
the **guaranteed** ones. The distinction is what makes the noise margins non-zero.

### Complement

Three glyphs, one meaning — the logical NOT of what they sit on.

$$\bar{A} \;=\; A' \;=\; \text{NOT } A$$

- **Overbar** $\bar{a}$ — the safer glyph, used inside the Chapter 5 derivations.
- **Prime** $A'$ — used everywhere else, and the one that collides with next-state notation.
- An overbar spanning **two letters** means the NOT of the whole product: $\overline{bs} = \bar b + \bar s$, **not** $\bar b\,\bar s$. ⚠ ·CH5 slide 17 prints a spanning bar where individual bars are meant, which turns a 4-minterm function into a 7-minterm one — see V07-1.
- On a signal name, an overbar means **active low**: $\overline{\text{RAS}}$, $\overline{\text{CAS}}$, $R/\overline{W}$, $\overline{\text{BL}}$.

### Next state — three notations, all in this unit

| Notation | Where | Note |
|---|---|---|
| $Q(t+1)$, $A(t+1)$ | ·CH1 slides 11–12; ·CH5 slides 21–33; ·EXC (files 01, 07) | the unambiguous one — **prefer this in written work** |
| $Q^{+}$, $A^{+}$, $B^{+}$ | ·CH5 slides 95–101; ·CH6 slides 18–22 (files 09, 10) | compact; no ambiguity, since a prime is never a plus |
| $A'$, $B'$, $C'$, $s'$ | ·CH5 slides 16–17 and the slide-33 table heading | ⚠ **collides with complement** — see C07-4 and the Tier 1 table |

Present state is written $Q(t)$, or bare $Q$ where no confusion arises.

### Marks in fuse maps, PLA tables and K-maps

| Mark | Means | Where |
|---|---|---|
| $\times$ | fusible link **intact** at that crosspoint | fuse maps ·CH3 slides 39, 45, 49 |
| $+$ | fuse **blown** | ·CH3 slide 45 — ⚠ slide 49 prints "1" for this; see C04-1 |
| $\bullet$ | **hard-wired** connection, not fusible | PLD notation ·CH3 slide 40 |
| **1** | in a PLA input column: the variable appears **uncomplemented** | ·CH3 slide 45 |
| **0** | in a PLA input column: the variable appears **complemented** | ·CH3 slide 45 |
| **—** (dash) | in a PLA input column: the variable is **absent** from that product term; in an output column, a **don't care** | ·CH3 slide 45; ·CH6 slide 20 |
| **T** / **C** | output polarity taken true / complemented | ·CH3 slide 45 |
| $\times$ | "not equivalent" | implication tables ·CH5 slides 84–88 |
| $\times 2$ | an adjacency requirement arising **twice**, so it takes priority | ·CH5 slides 95, 99 |

### Don't care

Written **X** (upright) in excitation tables and K-maps, and as an em-dash **—** in PLA tables.
Both mean "either value satisfies the requirement". Do not read the upright X as the italic input
variable $X$, and do not read the PLA dash as a minus sign.

### Abbreviations

| Short form | Expansion |
|---|---|
| SSI, MSI, LSI, SLSI, VLSI, ULSI | small / medium / large / super-large / very-large / ultra-large scale integration ·CH1 slide 2, ·CH2 slides 3–4 |
| RTL, DTL, TTL, ECL, CMOS | resistor-transistor, diode-transistor, transistor-transistor, emitter-coupled logic; complementary MOS |
| VTC | voltage transfer characteristic |
| RAM, ROM | random-access memory; read-only memory |
| SRAM, DRAM | static RAM; dynamic RAM |
| PROM, EPROM, UV EPROM, EEPROM | programmable / erasable / ultraviolet-erasable / electrically erasable ROM |
| RAS, CAS | row address strobe; column address strobe |
| SEC-DED | single-error correction, double-error detection |
| PLD, SPLD, CPLD | programmable logic device; simple PLD; complex PLD |
| PLA, PAL, FPLS | programmable logic array; programmable array logic; field-programmable logic sequencer |
| FPGA, CLB, LAB, LUT | field-programmable gate array; configurable logic block; logic array block; look-up table |
| ADC, DAC | analogue-to-digital converter; digital-to-analogue converter |
| SAR | successive-approximation register |
| S/H | sample-and-hold |
| FSE | full-scale error |
| MSB, LSB | most / least significant bit |
| FSM | finite state machine |
| ASM, SM | algorithmic state machine; state machine (as in SM chart, SM block) |
| ACC | accumulator |
| NRZ, NRZI, RZ | non-return-to-zero; NRZ-inverted; return-to-zero |
| CS | current state (K-map column label ·CH5 slide 17) |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026. Every symbol here was taken from a topic file's own symbol table or first-appearance definition; clash rows were re-checked against the cited slides.</i></sub>
