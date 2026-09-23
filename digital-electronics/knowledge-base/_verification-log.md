---
kb: "Digital Electronics — BEE 3102"
lecturer: "withheld"
file_role: verification-log
purpose: "Every defect found in the six chapter decks, with the printed form, the correction and the reasoning. Substantive defects are V-numbered, cosmetic ones C-numbered."
substantive: 36
cosmetic: 45
---

# Verification log — Digital Electronics (BEE 3102)

**How to use this.** Teach the corrected form. Mention the deck's own version only where the reader
needs to recognise it — working from the printed page in a tutorial, or meeting it in a CAT. Never
present a correction as though the slide already said it.

---

## 1. What was checked, and how

**348 slides across six chapter decks** — CH1 (32), CH2 (43), CH3 (66), CH4 (49), CH5 (118) and
CH6 (40) — plus the one-page excitation-table handout, `EXC`. Every page was read as a **200 dpi
image render**, never from the PDF text layer; the text dumps were used only to confirm the spelling
of a word already read off the picture. This is not a formality. Sixteen slides in these decks carry
**no text layer at all** (CH3 20 and 21, CH4 45 and 46, CH6 13, 17 and 37–40 among them), and two of
the defects below — V04-1 and V10-3 — are label and gate-symbol errors that exist only in the
drawing.

**Every worked example was recomputed in Python**, not checked by eye. Every state table, state
diagram, Karnaugh map, truth table, fuse map, programming table and excitation table was **rederived
from the deck's own specification and diffed cell by cell** against the print. Where a machine was
involved it was rebuilt in software and simulated — exhaustively over every input string up to
length 10 for the CH5 equivalence reduction, up to 16 bits for all six sequence detectors, over all
256 eight-bit inputs for the CH6 weighing machine, and over all $6 \times 64 = 384$ state-and-input
combinations for the CH6 dice-game PLA table. Every equation was additionally checked for
dimensional consistency, algebraic consistency, symbol slips, mislabelled results and
self-reference.

**The result: 81 defects — 36 substantive and 45 cosmetic.** The distribution is uneven and worth
knowing. The four decks of combinational and device material (CH1, CH2, CH3, CH6) are mostly sound;
the errors there are prose, labels and taxonomy. **The converter chapter, CH4, is the problem** — it
carries 14 of the 36 substantive defects on 49 slides, and nine of them are in the D/A half alone,
including one wrong formula that halves every answer it produces. The FSM material of CH5 is
structurally excellent: every one of the fifteen state machines in the deck was rebuilt and every one
is functionally correct. Its five substantive defects are all in the *surrounding* text, equations
and figures rather than in a machine.

---

## 2. ⚠ Read this before a CAT

The defects that would actually cost marks — because reproducing the printed version is wrong, or
because following it leads to a wrong number. Worst first.

| ID | Where | What goes wrong | What it costs |
|---|---|---|---|
| **V06-9** | CH4 slides 44, 47 | The R/2R bit-weight formula is off by one in the exponent: $V_S/2^{\,n-i}$ where the deck's own $D_0 \ldots D_{n-1}$ numbering requires $V_S/2^{\,n-1-i}$ | Every value the deck gives for that converter is a factor of two low; the printed answer $-3.4375$ V for 1011 should be $-6.875$ V. **A marking scheme built from the slide will mark the correct answer wrong** — know both numbers |
| **V05-1** | CH4 slide 20 | The SAR comparator decision rule is stated backwards — "$V_{\text{in}} > V_{\text{DAC}}$: output goes low, the bit goes low" | Every bit of every conversion inverted; the converter returns the ones-complement of the right code |
| **V03-4** | CH3 slide 29 | Hamming syndrome for an error at position 12 printed as $1000$ | $1000_2 = 8$, so positions 8 and 12 share a syndrome; the decoder "corrects" the wrong bit and injects a second error. Should be $1100$ |
| **V06-4** (with V06-5, V06-6, V06-7) | CH4 slide 37 | A **BCD**-coded DAC worked through the binary formula, $2^{12}-1 = 4095$ steps | Three numbers wrong on one slide: step $10$ mV not $2.44$ mV, resolution $0.1\,\%$ not $0.244\,\%$, output $6.95$ V not $1.6978$ V |
| **V06-3** | CH4 slide 36 | Every inequality in the bits-for-resolution derivation points the wrong way | The printed chain concludes $N \le 7$; the answer stated on the same line is 8 bits. A student reproducing the working answers 7 |
| **V10-3** | CH6 slide 34 | A gate drawn as **OR** where slide 33's own equation $D_{G1} = T_1A_3A_4$ requires a three-input **AND** | The drawn and required functions differ in 10 of 24 cases; the machine leaves $T_1$ after one clock and the counter stops at $0001$ instead of $1101$ |
| **V07-1** | CH5 slide 17 | In the serial-adder sum equation one overbar spans two literals: $a\overline{bs}$ for $a\bar b\bar s$ | $\overline{bs} = \bar b + \bar s$, so the printed line is a different function — 7 minterms instead of 4 |
| **V08-1** | CH5 slide 53 | The **Moore** sequence-detector specification, copy-pasted from the Mealy one, still claims an output "coincident with the last 1 input" | Impossible for a Moore machine; the timing diagram gets drawn one clock period early — the single most commonly lost mark in this topic |
| **V05-4** | CH4 slide 28 | Dual-slope clock count printed $2^{n}+1$ for $2^{\,n+1}$ — a lost bracket | Factor of two in the row most likely to be examined: at $n = 12$, 4097 against 8192 |
| **V05-2, V05-3** | CH4 slide 22 | Two wrong nodes in the SAR search tree — a duplicated sibling $0100$, and a fourth-trial outcome $1010/6.25$ V that is really the third trial's value | The drawn trace takes a step the algorithm cannot take; the lower half of the tree is unreachable |
| **V09-2** | CH5 slide 98 | One cell of the $B^{+}$ K-map printed $1$ where the slide's own encoded map and equation both give $0$ | Invites the grouping $B^{+} = B'C' + A'C + A'B$; that machine goes $S_0 \to S_4$ instead of $S_0 \to S_2$ |
| **V09-3** | CH5 slide 101 | A missing prime in the output equation read off the $Z$ map: $XQ_2Q_3'$ for $X'Q_2Q_3'$ | Two output errors — $Z$ asserted for state $f$ on input 1 where the table says 0, and not asserted for $f$ on input 0 where the table says 1 |
| **V02-4** | CH2 slide 17 | A worked answer given in µA and µW when the question's data are in mA and mW | Out by $10^3$: $14\ \mu\text{W}$ printed for $14$ mW. Only the prefixes are wrong, which is what makes it easy to copy |

---

## 3. The full log

Grouped by chapter deck, in slide order within each chapter. The IDs are the ones the topic files
cite inline and are globally unique by file number — **do not renumber them.**

---

### CH1 — Introduction and Recap (slides 1–32)

#### V01-1 · slide 7 · The system classification, one indent level out

**Prints:** under "Types of Systems", the list nests as

> - With state present
>   - State updated at discrete times (e.g. once per clock tick)
> - Synchronous sequential system
>   - State updated at any time
> - Asynchronous sequential system

**Should be:** state updated at **discrete** times → **synchronous** sequential system; state updated
at **any** time → **asynchronous** sequential system.

**Why:** the indentation has slipped by one level, so "State updated at any time" becomes the
sub-bullet of *synchronous* — which is the definition of *asynchronous*. "State updated at discrete
times" is left with no system name attached to it at all. Read the slide literally and the two
definitions are exchanged.

**Flagged in:** `01-introduction-and-recap.md` § 2.2 Types of system.

#### C01-3 · slides 10 and 27 · Two propagation delays for the same family

**Prints:** slide 10 — 74AC00 at a 30 pF load, $t_{PHL}$ typ 4.5 ns, $t_{PLH}$ typ 6.0 ns. Slide 27 —
"new ones (74AC) much faster (3ns)".

**Should be:** both slides quoting the same conditions, or slide 27 stating the conditions under
which 3 ns applies.

**Why:** propagation delay is a strong function of supply voltage and load capacitance, and only
slide 10 states its load, so the two figures are not necessarily inconsistent physically — but as
printed there is no way to reconcile them. Quote slide 10, which states its conditions.

**Flagged in:** `01-introduction-and-recap.md` § 3.2 The deck's worked device: 74AC00.

#### C01-1 · slide 14 · Bullets name signals the figure does not carry

**Prints:** "Data input, In, is called a *serial input*… Data output, Out… The vector (A, B, C, Out)
is called the *parallel output*."

**Should be:** the same statements expressed in the figure's own labels — $\text{In} = SI$,
$\text{Out} = SO$, and $A$, $B$, $C$ the outputs of the first three stages counting from the serial
input.

**Why:** the figure (reused on slides 15 and 16) labels only $SI$, $SO$, $D$ and $C$; the names In,
Out, A, B and C appear nowhere on it, so "the vector (A, B, C, Out)" cannot be resolved against the
drawing.

**Flagged in:** `01-introduction-and-recap.md` § 5.2 Shift register.

#### C01-2 · slide 16 · A truncated sentence and two directions that appear to conflict

**Prints:** "Since we have to store 1100 in the register, bits will be entered **LSB**"; and in the
remark column, "They are entered from the right" against "As they are shifted from left".

**Should be:** "…entered **LSB first**"; and the two remarks disambiguated — the *data word* is read
from its right-hand end, the *register* is filled from its left-hand end.

**Why:** the first sentence stops mid-phrase and never says in what order. The two remarks refer to
two different objects and only look contradictory. Feeding the bits the other way gives $0011$, not
$1100$. The numbers themselves are right: the printed table $0000, 0000, 0000, 1000, 1100$ was
reproduced row for row by simulating the register from cleared.

**Flagged in:** `01-introduction-and-recap.md` § 5.3 Worked example — storing a nibble.

---

### CH2 — Digital Logic Families (slides 1–43)

#### V02-1 · slides 3 and 4 · Two incompatible integration-scale tables

**Prints:** slide 3 — "SSI … fewer than 10 gates … LSI - 100 to thousands of gates … VLSI -
thousands to 100's of millions of gates". Slide 4, headed "Number of transistors (BJT or MOSFET)" —
"SSI - 0 to 10 … LSI - 100 to 1,000 … VLSI - 1,000 to 10,000 or thousands gates".

**Should be:** one set of boundaries in one unit. Teach slide 3's list as *gates per chip*, and take
from slide 4 only the two tiers slide 3 lacks — SLSI, $10^4$ to $10^5$ transistors, and ULSI, more
than $10^6$ transistors.

**Why:** the same term is given different upper limits on the two slides (LSI: "thousands" against
"1,000"; VLSI: "100's of millions" against "10,000"), and slide 4's fourth item mixes both units
inside one entry — "1,000 to 10,000 **or thousands gates**" — under a heading that says transistors.

**Flagged in:** `02-digital-logic-families.md` § 1 Integrated circuits and scale of integration.

#### V02-2 · slide 8 · $V_L$ defined at the input

**Prints:** "$V_L$ – The nominal voltage corresponding to a low-logic state **at the input** of a
logic gate for $v_i = V_H$"

**Should be:** at the **output** of a logic gate for $v_i = V_H$.

**Why:** $V_L$ and $V_H$ are the two *output* levels. The next bullet on the same slide defines $V_H$
"at the output of a logic gate for $v_i = V_L$", and the figure beside it plots both on the $v_O$
axis. As printed, $V_L$ collides with $V_{IL}$ and breaks $NM_L = V_{IL} - V_{OL}$ on the next slide.

**Flagged in:** `02-digital-logic-families.md` § 3.2 The real characteristic.

#### V02-3 · slide 10 · The two propagation-delay glosses swapped

**Prints:** "$\tau_{PHL}$, *delay time in going from logical 0 to logical 1 state (LOW to HIGH)*"
and "$\tau_{PLH}$, *delay time in going from logical 1 to logical 0 state (HIGH to LOW)*".

**Should be:** the two italicised glosses exchanged — $\tau_{PHL}$ is the delay on the output
transition HIGH to LOW, $\tau_{PLH}$ on LOW to HIGH.

**Why:** the subscripts already say so, and the waveform on the same slide (repeated on slide 14)
marks $\tau_{PHL}$ on the falling edge of $v_O$ and $\tau_{PLH}$ on the rising edge. The printed
words contradict the printed figure.

**Flagged in:** `02-digital-logic-families.md` § 4 Propagation delay and dynamic response.

#### C02-1 · slides 12 and 13 · Two names for the noise margins

**Prints:** slide 12 — $NM_L = V_{IL} - V_{OL}$, $NM_H = V_{OH} - V_{IH}$; slide 13 —
$V_{NH} = V_{OH(\min)} - V_{IH(\min)}$, $V_{NL} = V_{IL(\max)} - V_{OL(\max)}$.

**Should be:** one name per quantity.

**Why:** the same two quantities under two symbols, one slide apart, with no note that they are the
same. Both appear in the deck, so both belong in `_nomenclature.md` with a cross-link. The arithmetic
is identical either way.

**Flagged in:** `02-digital-logic-families.md` § 6 Noise margins.

#### V02-4 · slide 17 · Milliamps become microamps mid-solution

**Prints:** question — "draws **2 mA** when its output is HIGH and **3.6 mA** when its output is
LOW"; solution — $I_{CC} = \dfrac{2\ \mu\text{A} + 3.6\ \mu\text{A}}{2} = 2.8\ \mu\text{A}$ and
$P_D = 5v \times 2.8\ \mu\text{A} = 14\ \mu\text{W}$.

**Should be:** $I_{CC} = 2.8$ mA and $P_D = 5\ \text{V} \times 2.8\ \text{mA} = 14$ mW.

**Why:** the data are in milliamps and silently become microamps in the working — a factor of $10^3$
in both lines. Check the digits: $(2 + 3.6)/2 = 2.8$ and $5 \times 2.8 = 14$, so only the prefix
moved. 14 µW is also implausible for a bipolar gate on a 5 V rail.

**Flagged in:** `02-digital-logic-families.md` § 7 Power requirements, Example 2.

#### C02-6 · slides 17, 20, 28 and 37 · Spelling and typography, collected

**Prints:** slide 20 — "Schotkey TTL", and "CMOS Complimentary MOSFET"; slide 37 — "Complimentar y
MOS (CMOS)"; slide 28 — "First introduced **by in** 1964 (Texas Instruments)"; slide 17 — "$5v$" for
the supply.

**Should be:** *Schottky*; *complementary*, as slide 35 spells it correctly; a missing word on slide
28; and $5\ \text{V}$.

**Why:** typography only. No quantity or circuit is affected.

**Flagged in:** `02-digital-logic-families.md` §§ 7, 10, 15.1.

#### C02-2 · slide 24 · Four circuits, three of them distinct

**Prints:** four RTL circuits under "Determine the gates depicted in the following RTL circuits".

**Should be:** three. The bottom-left and bottom-right schematics are the same circuit, identical
down to the labels $R_1$–$R_4$, $Q_1$, $A$, $B$, $Q$, $V+$ and $V-$.

**Why:** compared region by region on the render; the two crops differ only in position on the
slide. Worth knowing, because a student counting four will hunt for a fourth answer that does not
exist.

**Flagged in:** `02-digital-logic-families.md` § 12 Resistor-transistor logic.

#### C02-3 · slide 27 · Truth-table heading

**Prints:** the blank truth table headed $A \mid A \mid Y$.

**Should be:** $A \mid B \mid Y$ — the circuit immediately to the left has two inputs, labelled $A$
and $B$.

**Why:** typographic slip.

**Flagged in:** `02-digital-logic-families.md` § 13 Diode-transistor logic, Example 3.

#### C02-5 · slide 29 · A node voltage 0.2 V low

**Prints:** in panel (a), input HIGH, the collector of $Q_2$ annotated "$\cong 0.7$ V".

**Should be:** $\approx 0.9$ V.

**Why:** with $Q_2$ saturated that node sits at $V_{BE3} + V_{CE(\text{sat})2} = 0.7 + 0.2 = 0.9$ V.
The argument the annotation supports — that $Q_4$ stays off, needing
$0.2 + 0.7 + 0.7 = 1.6$ V — is unaffected either way.

**Flagged in:** `02-digital-logic-families.md` § 14.1 The TTL inverter.

#### C02-4 · slides 29, 30 and 31 · Totem-pole transistor numbering moves

**Prints:** slides 29 and 30 label the pull-up $Q_4$ and the pull-down $Q_3$; slide 31 labels the
pull-up $Q_3$ and the pull-down $Q_4$.

**Should be:** one consistent numbering across the three figures.

**Why:** the circuits are otherwise the same totem-pole stage, so anyone carrying an answer from
slide 29 into slide 31 by transistor number names the wrong device.

**Flagged in:** `02-digital-logic-families.md` § 14.3 The standard 3-input TTL NAND.

#### V02-5 · slide 36 · The p-channel stage cannot turn on

**Prints:** the left-hand circuit headed "P-channel Enhancement", with $V_{DD}$ at the top through a
resistor to a node labelled DRAIN and $V_{out}$, the device below it, and SOURCE tied to ground;
caption "To Turn On, Gate Must Be Lower Than Source".

**Should be:** for a p-channel enhancement stage the **source goes to $V_{DD}$** and the drain to the
load resistor down to ground, with $V_{out}$ at the drain. The right-hand n-channel circuit as drawn
is correct.

**Why:** with the source at 0 V, "gate lower than source" demands a negative gate voltage, which a
0 V to +5 V logic system cannot produce — the device could never conduct. The deck connects the
device correctly two slides later, in the CMOS inverter of slide 38.

**Flagged in:** `02-digital-logic-families.md` § 15 CMOS.

---

### CH3 — Semiconductor Memory and Programmable Logic Devices (slides 1–66)

#### C03-1 · slide 8 · The two panels disagree on one row

**Prints:** two panels of the same $8 \times 8$ byte-organised array. The write panel shows address 3
holding $11111100$; the read panel shows address 3 holding $11000001$.

**Should be:** one value, consistently.

**Why:** the write operation touches address 5 only, so address 3 cannot change between the panels.
Rows 0, 1, 2, 4, 5, 6 and 7 are identical in both, and row 5 of the read panel is exactly the byte
written ($10001101$), so the two panels are unambiguously the same array before and after the write.
The procedures the slide teaches are unaffected.

**Flagged in:** `03-semiconductor-memory.md` § 3 Write and read operations.

#### V03-1 · slide 15 · The latch cell loses a stored 1

**Prints:** an SRAM latch cell built from one NAND gate (inputs Select and Data in), an inverter
driven by that NAND's output, and a cross-coupled NAND pair; the upper NAND's output labelled Data
out.

**Should be:** the inverter belongs on the **Data in** path, feeding a **second** gating NAND, so
that $\overline{S} = \overline{\text{Select}\cdot\text{Data in}}$ and
$\overline{R} = \overline{\text{Select}\cdot\overline{\text{Data in}}}$, with the cross-coupled pair
unchanged.

**Why:** as drawn, $\text{Select} = 0$ forces the two gating signals to $1$ and $0$; the lower NAND
is then pinned at $\overline{Q} = 1$ and the upper settles at $Q = 0$ whatever was stored. Repeat the
check by enumerating the four $(\text{Select}, \text{Data in})$ combinations from both latch start
states — all four rows with $\text{Select} = 0$ settle to $Q = 0$. A cell that holds a 0 but loses a
1 is not a memory cell. The figure is reused on slide 16 as the array's cell, so the defect
propagates.

**Flagged in:** `03-semiconductor-memory.md` § 7 Static RAM.

#### V03-2 · slide 17 · Box heading contradicts the transistor states beneath it

**Prints:** a box headed "**B = 1**", then "Address Line is activated (T5 = ON, T6 = ON)" and
"T2 = OFF, T3 = OFF, T1 = ON, T4 = ON".

**Should be:** $B = 0$ (equivalently $\overline{B} = 1$).

**Why:** the four listed transistor states are self-consistent, but only for $C_1 = 0$, $C_2 = 1$.
Tracing the cross-coupling on the render, $C_2$ drives the gates of $T_3$ and $T_1$, and $C_1$ the
gates of $T_4$ and $T_2$; $T_1$ ON needs $C_2 = 1$, $T_2$ OFF needs $C_1 = 0$, and bit line $B$
reaches $C_1$ through $T_5$, so $B = C_1 = 0$. If the heading is taken as authoritative instead, all
four transistor states must be inverted — the two halves of the box cannot both be right.

**Flagged in:** `03-semiconductor-memory.md` § 7 Static RAM.

#### V03-3 · slide 18 · "Write" describes the hold state

**Prints:** "**Write** — WL = 0; Data is held in Latch mode" and "**Read** — WL = 1; Access
Transistors are turned ON".

**Should be:** "**Hold (standby)** — WL = 0; data is held in latch mode" and "**Read or write** —
WL = 1; access transistors turned on".

**Why:** WL = 0 turns both access transistors off, isolating the cross-coupled inverters from the bit
lines. Nothing can be written into a cell that is disconnected — and the slide's own second clause,
"held in Latch mode", is the definition of hold. A write needs WL = 1 so the bit-line drivers can
overpower the feedback loop.

**Flagged in:** `03-semiconductor-memory.md` § 7 Static RAM.

#### V03-4 · slide 29 · Hamming syndrome for position 12

**Prints:** in the syndrome table, the row for an error at position 12 reads $C_8 = 1$, $C_4 = 0$,
$C_2 = 0$, $C_1 = 0$.

**Should be:** $C_8 = 1$, $C_4 = 1$, $C_2 = 0$, $C_1 = 0$.

**Why:** position 12 is covered by both $C_8 = \text{XOR}(8,9,10,11,12)$ and
$C_4 = \text{XOR}(4,5,6,7,12)$, so flipping bit 12 flips both check bits. The syndrome read as a
binary number *is* the error position, and $1100_2 = 12$ whereas the printed $1000_2 = 8$. As
printed, positions 8 and 12 share a syndrome, so the correction logic flips the wrong bit and
silently introduces a second error. The other twelve rows were regenerated by flipping one bit of
$001110010100$ at a time and are all correct.

**Flagged in:** `03-semiconductor-memory.md` § 11 Error detection and correction.

#### C03-2 · slide 33 · Four programming methods, five family members

**Prints:** the text lists **four** ways of programming a ROM (mask, PROM/fuse, EPROM/ultraviolet,
EEPROM/electrical); the tree beneath draws **five** siblings of ROM — Mask ROM, PROM, EPROM, UV
EPROM, EEPROM.

**Should be:** either four boxes, or a two-level tree with UV EPROM and EEPROM hanging below EPROM.

**Why:** item 3 of the text defines EPROM *as* the ultraviolet-erasable part, so EPROM and UV EPROM
are the same device listed twice; and an EEPROM is by construction an erasable PROM. It matters only
because "name the members of the ROM family" then has two defensible answers depending on which half
of the slide is used.

**Flagged in:** `03-semiconductor-memory.md` § 13 Read-only memory.

#### C04-5 · slide 40 · Figure lettering skips two panels

**Prints:** the PLD-notation figure lettered (a), (b), (c), (d), (g), (h).

**Should be:** (a)–(f), or the six panels relettered.

**Why:** parts (e) and (f) of the source figure were dropped without adjusting the lettering of what
remains. Nothing in the notation is missing — the six panels shown cover cross, no cross and
junction dot for both AND and OR arrays.

**Flagged in:** `04-programmable-logic-devices.md` § 4.4 Programming a PLD: fuses and notation.

#### C04-1 · slide 49 · Fuse legend contradicts the deck's own convention

**Prints:** the legend "$\times$ Fuse intact / **1** Fuse blown".

**Should be:** "$\times$ Fuse intact / $+$ Fuse blown", as the identical legend on slide 45 prints
it.

**Why:** the bullet glyph has been replaced by the digit 1 — actively misleading, because slide 43
defines $1 \rightarrow$ *connection*, the opposite sense. The crosses in the figure still carry their
normal meaning.

**Flagged in:** `04-programmable-logic-devices.md` § 4.8 Worked example 2.

#### C04-3 · slide 49 · Typing slip in the sentence that makes the example's point

**Prints:** "We **inclement** F1 Using the PLA then invert it , as this is more economical".

**Should be:** "We implement $\bar{F_1}$ using the PLA then invert it, as this is more economical."

**Flagged in:** `04-programmable-logic-devices.md` § 4.8 Worked example 2.

#### V04-1 · slide 52 · PAL fuse map, bottom label row

**Prints:** the ten AND-array columns labelled twice. The row above the array reads
$A\;A'\;B\;B'\;C\;C'\;D\;D'\;w\;w'$; the row **below** reads
$A\;A'\;\mathbf{B'}\;B'\;C\;C'\;D\;D'\;w\;w'$.

**Should be:** the third column is $B$, as the top row has it. The bottom row prints $B'$ twice.

**Why:** product term 5 must realise $x$'s second term $BCD$, and its cross sits in column 3. Read
from the bottom labels it would be $B'CD$ — a different function, $B'CD = \sum(3,11)$ against
$BCD = \sum(7,15)$, and only the latter completes $x = \sum(7,8,\ldots,15)$. Product term 7 ($A'B$)
has a cross in the same column and fails the same way. The top label row and the crosses together
make the intended reading unambiguous.

**Flagged in:** `04-programmable-logic-devices.md` § 4.9 Programmable array logic (PAL).

#### C04-2 · slide 58 · Two letters transposed

**Prints:** "…all three-state buffers are controlled by the **EO** input."

**Should be:** the **OE** (output enable) input, as the macrocell figure one slide earlier labels it.

**Flagged in:** `04-programmable-logic-devices.md` § 4.11 CPLD.

#### C04-6 · slides 62 and 63 · Duplicated slide

**Prints:** slide 62 (untitled) and slide 63 ("Cont…") carry the same figure — basic CLBs within the
global row/column interconnects — and the same sentence of body text.

**Should be:** one slide. Slide 62 has no title bar, which suggests 63 is the intended version.

**Flagged in:** `04-programmable-logic-devices.md` § 4.12 Gate arrays and FPGA.

#### C04-4 · slide 66 · Homework problem missing its noun

**Prints:** problem 4(a) — "a binary multiplier that multiplies two 4-bit,"

**Should be:** "…two 4-bit **numbers**".

**Why:** the clause has no object. The intended reading is unambiguous — two 4-bit operands, hence an
8-input, 8-output truth table — but the question asks for a ROM size, and the missing word is the
thing being sized.

**Flagged in:** `04-programmable-logic-devices.md` § 4.13 Homework set in the deck.

---

### CH4 — Signal Conversion, ADC and DAC (slides 1–49)

The worst-affected deck: fourteen substantive defects, nine of them in the D/A half.

#### C05-4 · slide 7 · Two symbols for the sampling interval

**Prints:** "Analog signal is sampled every $T_S$ secs", $f_s = 1/T_s$, then "x[n] is obtained by
extracting x(t) every $T$ s where $T$ is known as the sampling period".

**Should be:** $T_s$ throughout.

**Why:** one quantity introduced twice on one slide. Slide 8 then uses $T$ alone in
$T \le 1/(2f_{\max})$. Harmless until $T$ collides with $T_{\text{CLK}}$ and the dual-slope phase
times $T_1$, $T_2$ later in the chapter.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.3 Sampling and the Nyquist criterion.

#### C05-3 · slide 8 · Strict inequality in the prose, non-strict in the formula

**Prints:** prose "the sampling rate must be **greater than** twice the maximum frequency", then a
bullet saying "at least twice", then $f_s \ge 2f_{\max}$.

**Should be:** one or the other consistently; the strict recovery condition is $f_s > 2f_{\max}$.

**Why:** at exactly $f_s = 2f_{\max}$ a component at $f_{\max}$ can be sampled at its zero crossings
and vanish, so the strict inequality is the safe statement. The working rule — sample at twice the
highest frequency or more — is unaffected, but the two statements sit four lines apart.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.3 Sampling and the Nyquist criterion.

#### C05-5 · slide 15 · Bit count changes case mid-slide

**Prints:** "It uses $2^n - 1$ comparators for an n-bit resolution ADC", then two lines later
"Resolution $\Delta V = V_{ref}/2^{N}$".

**Should be:** the same case in both — $n$.

**Why:** $n$ and $N$ are the same bit count. The two formulas already differ in a way that *looks*
like a typo ($2^n - 1$ against $2^n$) but is not — see § 4 below — so a gratuitous case change on the
same slide is worth removing.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.8 The flash ADC.

#### V05-1 · slide 20 · The SAR decision rule, reversed

**Prints:** "Vin > VDAC: Comparator output goes low. The bit in the SAR goes low as well.
Vin < VDAC: Comparator output goes high. The SAR keeps that bit high."

**Should be:** $V_{\text{in}} > V_{\text{DAC}}$ → comparator output HIGH → the trial bit is **kept**;
$V_{\text{in}} < V_{\text{DAC}}$ → comparator output LOW → the trial bit is **cleared**.

**Why:** three independent checks in the same deck contradict the annotation. Slide 19 states "If the
input is larger, the bit is retained; otherwise it is reset (0)". Slide 21's flowchart routes the
**yes** branch of $V_{IN} > V_{DAC}$ to "set the bit". And slide 20's own schematic puts
$V_{\text{in}}$ on the non-inverting input and the DAC output on the inverting input, so the output
must be HIGH when $V_{\text{in}}$ is larger. Taken as printed, the converter returns the
ones-complement of the correct code.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.10 The successive-approximation ADC.

#### V05-2 · slide 22, right-hand tree · A duplicated sibling node

**Prints:** the second-level node on the "Vin>VDAC" branch as **0100**.

**Should be:** **1100**.

**Why:** $0100$ is already drawn as the node on the opposite ("VDAC>Vin") branch, so the tree has two
identical siblings; and the two children drawn beneath are $1010$ and $1110$, reachable only from
$1100$ (clear bit 2 and set bit 1 → 1010; keep bit 2 and set bit 1 → 1110). From $0100$ the children
would be $0010$ and $0110$. A trial that found the input **above** half scale cannot lead to a code
below half scale.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.10, the 4-bit search node by node.

#### V05-3 · slide 22, left-hand worked path · A fourth-trial outcome that cannot occur

**Prints:** the branch rejected at the fourth trial as **1010 / 6.25 V**.

**Should be:** **1001 / 5.625 V**.

**Why:** the fourth trial code is $1001$, whose only two outcomes are $1000$ (bit 0 cleared, 5.000 V)
and $1001$ (bit 0 kept, 5.625 V). $1010$ was the *third* trial and cannot recur. Recompute with the
step the slide's own circles imply, $5.000/8 = 0.625$ V: $1001_2 = 9 \times 0.625 = 5.625$ V, while
$1010_2 = 10 \times 0.625 = 6.250$ V is the trial-3 value already drawn one column to the left. The
slide's own right-hand tree confirms it — the two leaves under $1001$ are $1000$ and $1001$.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.10, the 4-bit search node by node.

#### C05-1 · slide 23 · An undefined symbol and a misnumbered list item

**Prints:** $\text{Digital out} = \left(\dfrac{V_{in}}{V_{red}}\right) \times (2^{n} - 1)$, and the
fourth list item numbered "i." after i, ii, iii.

**Should be:** $V_{REF}$ in the denominator; the fourth item numbered iv.

**Why:** $V_{red}$ is defined nowhere in the chapter, and the same question's opening line names the
reference voltage $V_{REF}$ and gives it as 5 V. The intent is unambiguous, but this is set homework,
so the symbol will be copied.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.11 Homework.

#### V05-5 · slide 26 · What the sigma-delta loop subtracts

**Prints:** "With sigma-delta conversion, the difference between two samples of the analog input
signal integrated and quantized."

**Should be:** the difference between the analogue input and the **fed-back analogue value of the
quantised output** is integrated and quantised.

**Why:** the slide's own block diagram shows the summing point with the analogue input on $+$ and the
1-bit DAC output on $-$. Nothing in the loop stores a previous input sample, so no input-to-input
difference can be formed. As printed the description is of a plain delta modulator without the
feedback DAC — a different converter.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.13 The sigma-delta ADC.

#### V05-4 · slide 28 · Dual-slope clock count, a lost bracket

**Prints:** dual slope — "No. of Clocks" $2^{n} + 1$, "Conversion Time"
$(2^{n} + 1) \times T_{\text{CLK}}$.

**Should be:** $2^{\,n+1}$ clocks and $2^{\,n+1} T_{\text{CLK}}$.

**Why:** $2^{(n+1)}$ has been set as $2^{n} + 1$. The dual-slope converter integrates the input for a
fixed $2^{n}$ clocks, then de-integrates for up to $2^{n}$ more, so the worst case is
$2 \times 2^{n} = 2^{\,n+1}$. Printed and correct diverge sharply at the resolutions the same row
quotes: at $n = 12$, $4097$ against $8192$; at $n = 16$, $65\,537$ against $131\,072$. The
neighbouring rows are unaffected and were confirmed correct.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.14 Comparing the converters.

#### C05-2 · slide 28 · Spelling

**Prints:** "Couter Type / Digital Ramp".

**Should be:** "Counter Type / Digital Ramp", as spelled correctly on slide 29.

**Flagged in:** `05-analogue-to-digital-conversion.md` § 5.14 Comparing the converters.

#### C06-1 · slides 32 and 33 · Heading copied from the previous example

**Prints:** "For 0110," as the heading of the final step, on both slides.

**Should be:** "For 0011," on slide 32 and "For 11101," on slide 33.

**Why:** copied from slide 31, where $0110$ *is* the code. The arithmetic underneath uses the right
code on both slides.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.2 The D/A transfer relation.

#### V06-1 · slide 34 · States confused with steps

**Prints:** "$2^{N} - 1$ = no of states, $N$ − no of bits".

**Should be:** $2^{N}$ is the number of states; $2^{N} - 1$ is the number of **steps** between them.

**Why:** an $N$-bit word has $2^N$ distinct codes, hence $2^N$ output levels with $2^N - 1$ gaps.
Slide 48 states the intended reading itself — resolution is "the reciprocal of the number of
**steps** in the output". The formula above the gloss is correct; the gloss teaches a wrong fact
about state counts that then carries into every later question.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3 Resolution.

#### C06-6 · slides 34–37 against 44 and 47 · Bit count changes case

**Prints:** upper-case $N$ on slides 34, 35, 36 and 37; lower-case $n$ on slides 44 and 47.

**Should be:** one symbol throughout.

**Why:** the same quantity under two glyphs within twenty slides — and the ADC half of the chapter
uses lower-case $n$ as well, so the DAC resolution slides are the odd ones out. For the clash table.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.7 Resolution and accuracy.

#### V06-2 · slide 35 · Leading-digit slip

**Prints:** $V_{res} = \dfrac{5}{1023} = 8.888 \times 10^{-3}\ \text{V}$.

**Should be:** $4.888 \times 10^{-3}\ \text{V} = 4.888$ mV.

**Why:** $5/1023 = 0.0048876$. Reverse check: $8.888\ \text{mV} \times 1023 = 9.09$ V, not the 5 V
full scale the question states.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 4.

#### V06-3 · slide 36 · Every inequality reversed

**Prints:** $40 \times 10^{-6}\,\text{A} < \dfrac{10\times10^{-3}\,\text{A}}{2^{N}-1}$, then
$2^{N} < \dfrac{10\times10^{-3}}{40\times10^{-6}} + 1$, then $2^{N} < 251$, then
$N = \dfrac{\log_{10}251}{\log_{10}2} = 7.97 \approx 8\ \text{bits}$.

**Should be:**
$$\frac{10\times10^{-3}}{2^{N}-1} < 40\times10^{-6} \;\Rightarrow\; 2^{N} > 251 \;\Rightarrow\; N > 7.97 \;\Rightarrow\; N = 8 \text{ bits}$$

**Why:** the requirement is that the step be *smaller* than 40 µA, which puts the resolution on the
small side of the inequality, not the large. As printed the chain gives $N \le 7$, contradicting the
answer stated on the same line. Direct check: at $N = 7$ the step is $10\ \text{mA}/127 = 78.7$ µA
(fails); at $N = 8$ it is $10\ \text{mA}/255 = 39.2$ µA (passes). The final answer is right; the
working that reaches it is not.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 5.

#### C06-2 · slide 36 · Typing slips in the question

**Prints:** "How may bit are required for a DAC so that its full scale output is 10mA and its
resolution is less than 40 µA."

**Should be:** "How many bits are required … less than 40 µA?"

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 5.

#### V06-4 · slide 37 · A BCD converter worked with the binary formula

**Prints:** the question states the DAC "uses a BCD input code", then
$2^{N}-1 = 2^{12}-1 = 4095$; $\text{Resolution} = 9.99/4095 = 0.00244$;
$V_{out} = 695 \times 0.00244 = 1.6978$.

**Should be:** a 12-bit BCD word is three decades, each stopping at $1001_2 = 9$, so it counts
$000$–$999$: **999** steps, not 4095. Step size $= 9.99/999 = 0.01\ \text{V} = 10$ mV; percentage
resolution $= (1/999) \times 100\,\% = 0.1\,\%$; $V_{out} = 695 \times 0.01 = 6.95$ V.

**Why:** the full-scale figure in the question is the confirmation — $9.99$ V is exactly
$999 \times 10\ \text{mV}$, a number with no meaning on the binary route. The BCD reading of the
input code, $0110\;1001\;0101 = 695$, is the slide's own. All three answers of the question change.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 6.

#### V06-5 · slide 37 · A count labelled as a step size

**Prints:** $\text{Step size} = 2^{N}-1 = 2^{12}-1 = 4095$.

**Should be:** the *number of steps* is 999 (BCD); the step **size** is a voltage,
$9.99\ \text{V}/999 = 10$ mV.

**Why:** dimensional check — a step size carries the units of the output, and 4095 is a pure count.
The line that follows then divides by that same count to obtain the step, so this label contradicts
the line beneath it.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 6.

#### V06-6 · slide 37 · A voltage restated as a percentage

**Prints:** $\text{Resolution} = \dfrac{9.99}{4095} = 0.00244 = 0.244\,\%$.

**Should be:** $0.00244$ is a step in **volts** and cannot be restated as a percentage. Percentage
resolution is $\dfrac{1}{2^N-1} \times 100\,\%$ — $0.0244\,\%$ on the slide's own binary route, and
$0.1\,\%$ on the corrected BCD route.

**Why:** the percentage form is the step divided by full scale,
$0.00244/9.99 = 2.44 \times 10^{-4}$, not the step multiplied by 100. Slide 48 performs exactly this
conversion correctly for the 8-bit case ($1/255 = 0.39\,\%$), so the two slides disagree. Off by a
factor of ten even before the BCD correction of V06-4.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 6.

#### V06-7 · slide 37 · Arithmetic slip in the output voltage

**Prints:** $V_{out} = 695 \times 0.00244 = 1.6978$.

**Should be:** $695 \times 0.00244 = 1.6958$; with the unrounded step $9.99/4095$ it is $1.6955$; the
corrected BCD answer is $6.95$ V.

**Why:** straight multiplication — the line is wrong on its own terms as well as on the corrected
route. No unit is printed on the result either.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.3, Example 6.

#### V06-8 · slide 38 · The percentage applied twice

**Prints:** $\text{Error} = \dfrac{2\ \text{mA} \times 0.19}{100} = 3.8\ \mu\text{A}$.

**Should be:** $E = 0.19 \times 2\ \text{mA} = 0.38\ \text{mA} = 380\ \mu\text{A}$.

**Why:** $0.19$ already **is** $19/100$; dividing by 100 again applies the percentage twice. The line
immediately above, $19\,\% = \dfrac{E}{2\ \text{mA}} \times 100\,\%$, rearranges to
$E = 19 \times 2\ \text{mA}/100$ — with 19, not 0.19, over the 100. The printed answer is 100 times
too small, and a full-scale error of a few microamps is not a $\pm 19\,\%$ specification.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.4 Full-scale error, Example 7.

#### C06-5 · slide 39 · A dropped minus sign

**Prints:** $V_{out} = I_f R_f$.

**Should be:** $V_{out} = -I_f R_f$.

**Why:** the amplifier is in the inverting configuration with the summing node at virtual ground.
Slide 41 states the output "is negative with respect to virtual ground" and slide 42 tabulates
sixteen negative values, so the minus is dropped only here. No number depends on it, but the sign is
the one thing students lose marks on.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.5 The binary-weighted-input DAC.

#### C06-4 · slide 43 · A voltage inside a sum of currents

**Prints:**
$$I_{out} = -\left(\frac{3.0\ \text{V}}{120\ \text{k}\Omega} + 0\ \text{V} + \frac{3.0\ \text{V}}{30\ \text{k}\Omega} + \frac{3.0\ \text{V}}{15\ \text{k}\Omega}\right) = -0.325\ \text{mA}$$

**Should be:** the second term is $\dfrac{0\ \text{V}}{60\ \text{k}\Omega} = 0$ mA.

**Why:** the total is unaffected because the term is zero, but as printed a voltage is being added to
three currents.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.5, Example 9.

#### V06-9 · slides 44 and 47 · The R/2R ladder formula, off by one in the exponent ★ most serious

**Prints:** $V_{out} = -\dfrac{V_S}{2^{\,n-i}}$, with "$n$ = number of bits, $i$ = bit number"
(slide 44), applied on slide 47 to give $V_{out}(D_0) = -5/2^{4-0} = -0.3125$ V,
$V_{out}(D_1) = -5/2^{4-1} = -0.625$ V, $V_{out}(D_3) = -5/2^{4-3} = -2.5$ V and, by superposition,
$V_{out} = -3.4375$ V for the input 1011.

**Should be:**
$$V_{out}(D_i) = -\frac{V_S}{2^{\,n-1-i}} \qquad \text{for inputs labelled } D_0 \ldots D_{n-1}$$
giving $-0.625$, $-1.25$, $-2.5$ and $-5$ V for $D_0$ to $D_3$, and
$$V_{out} = -5 - 1.25 - 0.625 = -6.875\ \text{V} \quad \text{for the input } 1011$$
Equivalently $V_{out} = -V_S D / 2^{\,n-1}$ with $D$ the decimal value of the code.

**Why:** two independent checks. **(1)** The deck contradicts itself — slides 45(a) and 46 analyse
the same network from the circuit and obtain $-5$ V for $D_3$ alone, where the printed formula gives
$-2.5$ V. **(2)** A nodal solution of the ladder with the slide-47 values ($R = 25$ kΩ,
$2R = 50$ kΩ, $R_f = 50$ kΩ, $V_S = 5$ V) returns $-6.875$ V for 1011 and the single-bit weights
$-0.625$, $-1.25$, $-2.5$, $-5$ V — exactly a factor of two above every value the printed formula
produces. The printed exponent would be correct only if the bits were numbered $1$ to $n$; the deck
numbers them $0$ to $n-1$ in its own figures.

This is the deck's only stated result for the R/2R ladder and it is carried into the worked example,
so it halves every answer. **A marking scheme derived from the slide will award the printed value —
know both.**

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.6 The R/2R ladder DAC.

#### C06-3 · slides 44 and 47 · Ohms printed as watts

**Prints:** "50 kW", "25 kW", "$R_f$ = 50 kW".

**Should be:** $50\ \text{k}\Omega$, $25\ \text{k}\Omega$, $R_f = 50\ \text{k}\Omega$.

**Why:** the ohm sign has been substituted by a W — a Symbol-font mapping lost in the file. It is in
the rendered page as well as the text layer, so it is in the slide itself and not an extraction
artefact. Slides 40, 41 and 43 print the same values with a correct Ω. Worth knowing, because "50 kW"
also reads as a power.

**Flagged in:** `06-digital-to-analogue-conversion.md` § 6.6, Example 10.

---

### CH5 — Finite State Machines and Sequential Circuit Design (slides 1–118)

Every one of the fifteen machines in this deck was rebuilt and simulated, and every one is correct.
All five substantive defects are in the surrounding equations, prose and figures.

#### V07-1 · slide 17 · One overbar spanning two literals

**Prints:** $z = \bar{a}b\bar{s} + a\overline{bs} + \overline{ab}s + abs$ — the second and third
terms carry a single continuous overbar spanning two letters.

**Should be:**
$$z = \bar{a}\,b\,\bar{s} + a\,\bar{b}\,\bar{s} + \bar{a}\,\bar{b}\,s + a\,b\,s = a \oplus b \oplus s$$

**Why:** $\overline{bs} = \bar b + \bar s \neq \bar b\,\bar s$. Evaluate the printed expression
literally over $(a,b,s) = 000 \ldots 111$ and it gives $0,1,1,1,1,1,1,1$ — seven minterms; the correct
sum gives $0,1,1,0,1,0,0,1$ — four, which is what the slide's own Karnaugh map and slide 16's state
table both show. The first and fourth terms on the same line use individual bars, so the slide is
internally inconsistent as well.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.6 Application example — a serial adder.

#### C07-1 · slide 17 · The carry equation is not the form the K-map derives

**Prints:** $s' = ab\bar{s} + \bar{a}bs + a\bar{b}s + abs$ — the canonical four-minterm sum — while
the Karnaugh map immediately above it is grouped into three overlapping pairs.

**Should be:** the three groupings read out as $s' = ab + bs + as$, the minimal form and the standard
full-adder carry expression.

**Why:** both forms describe the same function (evaluated over all eight combinations, they agree),
so nothing downstream is wrong; but the K-map working shown is the working for the minimal form and
the equation printed beneath it is not that form. Implemented literally it costs two extra gates. The
$z$ equation on the same slide *is* minimal, because an exclusive-OR admits no simplification.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.6, Step 5.

#### C07-2 · slide 28 · Characteristic equations with $D$ on the left

**Prints:** $D = JQ' + K'Q$ and $D = T \oplus Q = T'Q + TQ'$.

**Should be:** $Q(t+1) = JQ' + K'Q$ and $Q(t+1) = T \oplus Q = T'Q + TQ'$.

**Why:** these are the characteristic equations of the JK and T flip-flops, whose left-hand side is
the next state. Writing $D$ there is meaningful only as "the equivalent D input", and neither device
has a $D$ input. Slide 31 prints the same T relation correctly as $Q(t+1) = T \oplus Q$. The two
forms are numerically identical because $Q(t+1) = D$ for a D flip-flop; only the symbol is wrong.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.13 Analysis with JK flip-flops.

#### C07-3 · slide 30 · Unsubscripted $J$ and $K$ for two different flip-flops

**Prints:** $A(t+1) = JA' + K'A$ and $B(t+1) = JB' + K'B$.

**Should be:** $A(t+1) = J_A A' + K_A' A$ and $B(t+1) = J_B B' + K_B' B$.

**Why:** the two flip-flops have different inputs — $J_A = B$, $K_A = Bx'$, $J_B = x'$,
$K_B = A \oplus x$ — so unsubscripted $J$ and $K$ cannot stand for both. The substitution two lines
below uses the correct per-flip-flop values, and the derived results
$A(t+1) = A'B + AB' + Ax$ and $B(t+1) = B'x' + ABx + A'Bx'$ were both verified over all eight input
combinations.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.14 The characteristic equation.

#### V07-2 · slide 33 · Self-referential state equations

**Prints:** $A = BC$, $B = B'C + BC'$, $C = A'C'$, $Z = A$.

**Should be:** $D_A = BC$, $D_B = B'C + BC' = B \oplus C$, $D_C = A'C'$, $Z = A$ — equivalently
$A(t+1) = BC$, $B(t+1) = B \oplus C$, $C(t+1) = A'C'$.

**Why:** self-reference. $B$ appears on both sides of the second equation and $C$ on both sides of
the third, so as ordinary Boolean equations they have no solution — $B = B'C + BC'$ requires
$B = B \oplus C$, which forces $C = 0$. What is meant is the flip-flop **input** equations. Only
$Z = A$ is well-formed as printed, because $Z$ is a combinational output rather than a state
variable. The state table on the same slide is computed from the intended reading and is correct.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.17 Worked analysis example — three D
flip-flops.

#### C07-4 · slide 33 · The prime carrying two meanings eight lines apart

**Prints:** the state-table column heading $A'\,B'\,C'$ at $(t+1)$, using a prime to mean "next
state" — on the same slide whose equations use a prime to mean "complement" ($C = A'C'$,
$B = B'C + BC'$).

**Should be:** $A(t+1)\,B(t+1)\,C(t+1)$, with the prime reserved for complement.

**Why:** one mark, two meanings. The table's contents are correct under the "next state" reading; the
ambiguity is in the heading alone. This clash belongs in `_nomenclature.md`.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.17.

#### C08-1 · slide 42 · A malapropism in the procedure

**Prints:** step 4 of the sequence-recogniser procedure — "The final state represents the input
sequence occurrence (**feasibly** less the final input value)."

**Should be:** "(**possibly** less the final input value)."

**Why:** the intended point is that in a Mealy machine the final state represents the target sequence
*minus its last bit*, because the last bit is consumed by the arc that carries the output 1 — compare
$D$ on slide 68, which means 110, not 1101.

**Flagged in:** `08-sequential-circuit-design.md` § 8.4 The sequence-recogniser procedure.

#### C08-2 · slide 43 · Two typographic slips in the completeness rule

**Prints:** "Make sure **all state** have a transition for both a 0 and a 1 but only **1of** each!"

**Should be:** "Make sure all **states** have a transition for both a 0 and a 1, but only **1 of**
each."

**Why:** the rule itself is correct and is the completeness test used on all six machines in the
range.

**Flagged in:** `08-sequential-circuit-design.md` § 8.5 Guidelines for construction of state graphs.

#### C08-3 · slides 44 and 53 · "and" for "an", and a sentence cut off

**Prints:** "…will produce **and** output of $Z=1$…" on both slides; and on slide 44 the paragraph
stops mid-clause — "…so whenever a 101 is in the data stream a 1 is output coincident with the
**last**".

**Should be:** "…will produce **an** output of $Z=1$…", and the sentence completed as "…coincident
with the last **1**."

**Why:** the truncation is a text-box overflow; slide 53 repeats the paragraph and shows the missing
word. It leaves the overlap rule looking unfinished on the slide that first states it.

**Flagged in:** `08-sequential-circuit-design.md` § 8.6 Example 1a — Mealy machine for 101.

#### C08-4 · slide 46 · Typing slip

**Prints:** "On a 1 transition to a new state S1 with **an new** meaning."

**Should be:** "with **a new** meaning."

**Flagged in:** `08-sequential-circuit-design.md` § 8.6.

#### V08-1 · slide 53 · A Moore specification copied from the Mealy one

**Prints:** "Any sequence ending in 101 will produce and output of $Z=1$ **coincident with the last 1
input**." — as the specification for Example 1b, the **Moore** machine.

**Should be:** the output appears during the clock period **after** the one in which the last 1 is
applied. A Moore machine cannot assert $Z$ coincident with the last input.

**Why:** slide 53 is a verbatim copy of the Example 1a (Mealy) specification on slide 44, and the
phrase was not adjusted for the change of model. A Moore output is a function of the state alone,
$Z(t) = \lambda(S(t))$, and the state meaning "101 received" ($S_3/1$ on slide 56) is only entered on
the clock edge that samples the last 1. Checked over every input string up to sixteen bits: the Moore
machine of slide 56 produces exactly the output of the Mealy machine of slide 48 shifted one clock
period later, $Z_{\text{Moore}}(t+1) = Z_{\text{Mealy}}(t)$, with no other difference. The state
diagram and state table on slides 55–56 are correct; only the copied sentence is wrong.

**Flagged in:** `08-sequential-circuit-design.md` § 8.8 Example 1b — Moore machine for 101.

#### V08-2 · slide 54 · A bullet block attributed to the wrong state

**Prints:** a bullet headed "**Transitions from State 1**", whose first sub-bullet reads "On a 0 you
stay in **state 1**" and whose second reads "On a 1 you transition to state S1."

**Should be:** "Transitions from **State 0**", and "On a 0 you stay in **$S_0$**".

**Why:** the block describes the two arcs leaving the reset state $S_0$ — the diagram beside it on
the same slide shows the $S_0$ self-loop on 0 and the arc $S_0 \to S_1$ on 1. The next block on the
same slide starts again with "Transition from S1", so $S_1$ is covered separately and cannot also be
the subject of this one. Taken literally the printed text gives $S_1 \to S_1$ on both 0 and 1 — a
machine with no path to $S_2$, which detects nothing.

**Flagged in:** `08-sequential-circuit-design.md` § 8.8 Example 1b, constructing the graph.

#### C08-5 · slide 60 · Spelling

**Prints:** "Input is a 1 so the input is 011 – Go to S3 **where as** this is the first 1."

**Should be:** "**whereas** this is the first 1."

**Flagged in:** `08-sequential-circuit-design.md` § 8.10 Example 2b.

#### C08-6 · slide 68 · Missing plural

**Prints:** "**The state have** the following abstract meanings:"

**Should be:** "The **states have** the following abstract meanings:"

**Flagged in:** `08-sequential-circuit-design.md` § 8.12.1 Example 3a.

#### V09-1 · slides 77 and 78 · Two nodes named $D$, none named $E$

**Prints:** in both the partial and the complete state-tree figures, the node reached from $B$ on
$X = 1$ is labelled **$D$**, so the figure shows two distinct nodes both named $D$ and no node named
$E$.

**Should be:** that node is **$E$**.

**Why:** the state table on slide 76 gives row $B$ the next states $D$ (on $X = 0$) and $E$ (on
$X = 1$); the mislabelled node's own successors on slide 78 are $J$ and $K$, which is $E$'s row, not
$D$'s ($D$'s successors are $H$ and $I$); and the whole reduction on slides 79–81 depends on $E$
existing — it concludes $E \equiv F$ and keeps $E$ in the reduced table. The slide-77 bullet even
says "Now add D, E, F, G" while the figure beside it shows D, D, F, G. A state graph with two
identically named nodes is not a well-formed graph, and a reader working from the figure cannot
follow the next four slides.

**Flagged in:** `09-state-reduction-and-assignment.md` § 9.3.2 The full tree.

#### C09-1 · slide 86 · A circular conclusion

**Prints:** the boxed conclusion "a ≡ d iff a ≡ d and c ≡ e".

**Should be:** "a ≡ d iff c ≡ e".

**Why:** the slide's own heading is "Self Redundant Pairs" and its bullet says the self-redundant
pair in square $a$-$d$ is removed. Once $a$-$d$ is struck out of its own square, the surviving
condition is $c \equiv e$ alone. As printed the statement is circular and asserts nothing. The chart
itself carries the struck-out entry correctly.

**Flagged in:** `09-state-reduction-and-assignment.md` § 9.5.3 Entering the implied pairs.

#### C09-2 · slide 91 · Complexity-class name

**Prints:** "This is a n-p complete problem."

**Should be:** "This is an NP-complete problem."

**Why:** NP abbreviates *nondeterministic polynomial time* and is not hyphenated between the letters.

**Flagged in:** `09-state-reduction-and-assignment.md` § 9.6 State assignment — rules and guidelines.

#### C09-3 · slide 96 · Requirements described as solutions

**Prints:** "Two possible ways of satisfying the guidelines are:" followed by two sub-bullets headed
"Guideline 1:" and "Guideline 2:" listing adjacency sets.

**Should be:** those two sub-bullets are the **requirements** produced by the two guidelines, not two
ways of satisfying them. The two ways are the two assignment maps drawn beside the text.

**Why:** the adjacency sets themselves are correct — both were regenerated from the state table on
slide 93 and match, including the multiplicities on $(S_2,S_5)$ and $(S_1,S_6)$.

**Flagged in:** `09-state-reduction-and-assignment.md` § 9.8.3 Two possible assignment maps.

#### V09-2 · slide 98 · One wrong cell in the $B^{+}$ K-map

**Prints:** in the $B^{+}$ map, the cell at $XA = 10$, $BC = 00$ contains **1**.

**Should be:** **0**.

**Why:** that cell is present state $ABC = 000 = S_0$ with input $X = 1$. The state table on slide 93
sends $S_0$ to $S_2$ on a 1, and $S_2$ is coded 001, so $B^{+} = 0$. Two things on the *same slide*
confirm it: the encoded next-state map beside the K-maps prints $S_2/001$ in exactly that position,
and the slide's own equation $B^{+} = X'C' + A'C + A'B$ evaluates to 0 there. The $A^{+}$ and $C^{+}$
maps both have the right bits in that cell. Taken as printed, row $BC = 00$ becomes all 1s and
don't-cares, which invites the grouping $B^{+} = B'C' + A'C + A'B$; that machine goes from $S_0$ to
$S_4$ instead of $S_2$ on a 1 and no longer meets the state table.

**Flagged in:** `09-state-reduction-and-assignment.md` § 9.8.5 Choosing an assignment and reading the
equations.

#### V09-3 · slide 101 · A missing prime in the output equation

**Prints:** $Z = XQ_2Q_3 + X'Q_2'Q_3 + XQ_2Q_3'$.

**Should be:** $Z = XQ_2Q_3 + X'Q_2'Q_3 + X'Q_2Q_3'$ — the third term needs the prime on $X$.

**Why:** two cells of the slide's own $Z$ map contradict the printed equation. At $XQ_1 = 00$,
$Q_2Q_3 = 10$ (state $Q_1Q_2Q_3 = 010 = f$, input 0) the map holds 1 and the printed equation gives
0; at $XQ_1 = 10$, $Q_2Q_3 = 10$ (state $f$, input 1) the map holds 0 and the printed equation gives
1. The loop drawn on the map covers the two left-hand cells of row $Q_2Q_3 = 10$, i.e. $X = 0$, so
the grouping is correct and only the transcription slipped. The gate and gate-input counts on the
slide (10 and 26) are unaffected and are correct.

**Flagged in:** `09-state-reduction-and-assignment.md` § 9.9.4 The flip-flop input equations.

---

### EXC — the one-page excitation-table handout

#### V07-3 · T flip-flop section · Characteristic table headed $D$

**Prints:** the T flip-flop **characteristic table** with its input column headed **$D$**:
$D = 0 \Rightarrow Q(t+1) = Q(t)$ (no change), $D = 1 \Rightarrow Q(t+1) = Q'(t)$ (toggle).

**Should be:** the column is **$T$**.

**Why:** the section is headed "T Flip-flop", the excitation table beside it uses $T$, and the
behaviour described is toggling. A D flip-flop does not toggle: $Q(t+1) = D$, so $D = 1$ gives
$Q(t+1) = 1$, not $Q'(t)$. The D flip-flop's own characteristic table appears correctly two sections
higher on the same page, so the page prints two different tables both headed $D$. This is the
most-consulted table in the unit.

**Flagged in:** `07-fsm-fundamentals-and-analysis.md` § 7.15 Characteristic tables and excitation
tables.

---

### CH6 — Algorithmic State Machines (slides 1–40)

#### V10-1 · slide 13 · The loop-exit test, inverted

**Prints:** the loop-exit decision of the multiplier flowchart as "Is Count $n$ ?"

**Should be:** "Is Count $= 0$ ?"

**Why:** the initialisation box on the same flowchart sets $\text{Count} \leftarrow n$ and the loop
body does $\text{Count} \leftarrow \text{Count} - 1$, so the counter counts *down*. The table printed
on the left of the same slide confirms it — the Count column runs
$100\,(4) \to 011\,(3) \to 010\,(2) \to 001\,(1) \to 000\,(0)$ and the algorithm terminates at 000.
Taken as printed, the test is true on the very first pass, so the loop exits immediately and no
partial product is ever accumulated.

**Flagged in:** `10-algorithmic-state-machines.md` § 10.10 Worked example — design of a binary
multiplier.

#### C10-1 · slide 18 · State symbols dropped by the slide software

**Prints:** step 2 as "For each of these link paths that lead into the state." and step 3 as "For
each of these link paths, find a term that is1 when the link path is followed. That is, for a link
path from to, the term will be 1 if the machine is in state and the conditions for existing to are
satisfied".

**Should be:** step 2 — "For each of these **states**, find all of the link paths that lead into the
state." Step 3 — "…for a link path from $S_i$ to $S_j$, the term will be 1 if the machine is in state
$S_i$ and the conditions for **exiting** $S_i$ to $S_j$ are satisfied." Also "is1" needs a space.

**Why:** the state symbols have been dropped, leaving three dangling prepositions, and "existing" is
a typo for "exiting". The procedure is unreadable as printed, but the equations on the same slide,
$B^{+} = A'B'X + A'BX + ABX$ and $A^{+} = A'BX + ABX$, are both correct — verified against the
next-state table of the slide-10 chart.

**Flagged in:** `10-algorithmic-state-machines.md` § 10.8 Next-state equations straight from the link
paths.

#### V10-2 · slide 21 · Two rows of a don't-care expansion repeated

**Prints:** the last two of the eight rows that replace PLA row 5 as
$001\;\,0\;\,1\;\,0\;\,0\;\,1\;\,0$ and $001\;\,0\;\,1\;\,0\;\,0\;\,1\;\,1$
(columns $ABC$, $Rb$, $Reset$, $D_7$, $D_{711}$, $D_{2312}$, $Eq$).

**Should be:** $001\;\,0\;\,1\;\,1\;\,0\;\,1\;\,0$ and $001\;\,0\;\,1\;\,1\;\,0\;\,1\;\,1$ — that is,
$D_7 = 1$ in both.

**Why:** row 5 of the slide-20 table has three dashes, in the $Reset$, $D_7$ and $Eq$ columns, so its
expansion is the eight combinations of $(Reset, D_7, Eq)$ in the order 000, 001, 010, 011, 100, 101,
**110**, **111**. The slide's first six rows follow that order correctly; rows 7 and 8 repeat rows 5
and 6 byte for byte, printing 100 and 101 a second time instead of 110 and 111. The combinations
$Reset = 1$, $D_7 = 1$ are therefore left unprogrammed and the controller has no defined next state
for them — two of eight product terms missing from the programmed device, on the slide whose whole
purpose is to show how a don't-care row is expanded.

**Flagged in:** `10-algorithmic-state-machines.md` § 10.12 Realisation of the SM chart.

#### C10-2 · slide 30 · Counter bits renumbered mid-example

**Prints:** the counter bits as $A_3\,A_2\,A_1\,A_0$, with $A_2$ and $A_3$ fed back to the
controller.

**Should be (for consistency with the rest of the example):** $A_4\,A_3\,A_2\,A_1$, with $A_3$ and
$A_4$ fed back — the numbering used by the problem statement on slide 24 and by slides 25–29 and
31–34.

**Why:** slide 30 is a redraw of the same design from a different edition of the source textbook,
which indexes the counter from 0. The two figures describe the same two flip-flops — the MSB and the
bit below it — but a reader moving between slides 29 and 30 will read $A_3$ as two different bits. No
equation changes, but an exam question could quote one figure and the marking scheme the other.

**Flagged in:** `10-algorithmic-state-machines.md` § 10.14 Example 1 — the design problem and its ASM
chart.

#### V10-3 · slide 34 · An OR gate where the equation requires an AND

**Prints:** a two-input AND gate fed by $A_3$ and $A_4$, whose output goes into an **OR** gate whose
other input is $T_1$; the OR gate drives the D input of the $G_1$ flip-flop. As drawn,
$D_{G1} = A_3A_4 + T_1$.

**Should be:** a three-input **AND** on $T_1$, $A_3$ and $A_4$ — $D_{G1} = T_1A_3A_4$.

**Why:** slide 33, one slide earlier, prints $D_{G1} = T_1\,A_3\,A_4$ and derives it from the state
table, which has exactly one row with $G_1^{+} = 1$, namely $G_1G_0 = 01$ with $A_3A_4 = 11$. The
drawn and required functions were compared over all 24 combinations of control state and
$(S, A_3, A_4)$ and differ in **10** of them. The failure is immediate: with the printed circuit
$D_{G1} = 1$ throughout $T_1$, so the machine leaves $T_1$ for $T_2$ after a single clock period
regardless of the counter, $F$ is set, and the counter stops at $0001$ instead of $1101$. The OR gate
one row above, which correctly forms $D_{G0} = T_0S + T_1$, is what makes the error easy to miss —
the two gates are drawn with the same symbol.

**Flagged in:** `10-algorithmic-state-machines.md` § 10.15 Example 1 — the control logic.

#### C10-4 · slide 36 · Two typos in the sentence that defines "weight"

**Prints:** "The weight of a binary number is defined by as the number of 1's present in it binary
representation".

**Should be:** "The weight of a binary number is defined as the number of 1s present in its binary
representation."

**Flagged in:** `10-algorithmic-state-machines.md` § 10.16 ASM for a weighing machine.

#### C10-3 · slide 40 · Decision boxes with one exit and no branch labels

**Prints:** the $K$ decision box inside state $A$'s SM block, and the two $J$ decision boxes inside
state $B$'s SM block, each with a single exit path and no 0/1 branch labels.

**Should be:** either delete those boxes, or draw both branches, label them 0 and 1, and let them
merge into the same exit.

**Why:** slide 9's own rule 1 requires exactly one exit path for every valid combination of input
variables, and the deck's own definition gives a decision box a true branch and a false branch. In
state $A$ the next state depends on $J$ alone and in state $B$ on $K$ alone, so those three boxes
cannot change the outcome — which is why the original draughtsman merged their exits. The
**behaviour** of the chart is correct: both state tables on slides 39 and 40 were checked against
$Q^{+} = D$ and $Q^{+} = JQ' + K'Q$ and agree in all eight state-and-input combinations. But a
student copying the drawing into an exam answer loses the mark for a malformed decision box.

**Flagged in:** `10-algorithmic-state-machines.md` § 10.17 D and JK flip-flops written as ASM charts.

---

## 4. Checked and found correct

Recorded so that nobody re-checks them. Everything below was rederived or re-simulated
independently and **agrees with the print**.

**The two that look like errors and are not:**

- **CH4 slide 15 — the flash-ADC comparator count.** "$2^n - 1$ comparators" alongside
  "$\Delta V = V_{REF}/2^{n}$" is **consistent, not a levels-versus-steps slip**: $2^n$ equal ladder
  resistors give $2^n - 1$ internal taps. This was the specific confusion looked for; it is not
  present.
- **CH6 slides 17, 20 and 21 — the dice-game PLA table.** All sixteen specified rows were expanded to
  the full $6 \times 64 = 384$ state-and-input combinations and checked simultaneously for wrong
  entries, uncovered combinations and overlapping rows. There are none of any. (The one defect in
  this material, V10-2, is in the eight-row expansion of row 5 printed on slide 21, not in the table
  itself.)

**CH1.** The shift-register state table (15–16); the 2-bit JK ripple counter (18) and its function
table against $Q(t+1) = J\overline{Q} + \overline{K}Q$; the 3-bit D-type ripple counter sequence and
full modulus-8 cycle, and the $3 \times 1\ \text{ns}$ settling figure (19); the 4-bit synchronous
counter 0–15 (20); the seven-segment truth table and $\text{out}6$ equation (8); the state equations,
state table and state diagram (29); the decimal and binary next-state tables (30). Circuit topology
was traced from magnified renders on slides 18 and 19 — the second stage really is clocked from
$Q_0$, which is what makes it an up counter.

**CH2.** Both CMOS device-state tables (39, 40) rederived cell by cell from the gate connections — 32
entries, all agreeing; the worked examples on slides 13 and 27; every circuit schematic traced node
by node against its stated function; the TTL inverter node voltages of slide 29 rebuilt from
$V_{BE} = 0.7$ V and $V_{CE(\text{sat})} = 0.2$ V (with the single exception of C02-5).

**CH3, memory.** The address-size arithmetic (12); the capacity arithmetic (25); the whole Hamming
worked example and twelve of the thirteen syndrome rows, regenerated by flipping one bit of
$001110010100$ at a time (27–29); the SEC-DED parity bit and check-bit range table (30); the ROM
sizing (32); the binary cell re-simulated over its full input space (23); the DRAM cell traced net by
net (19).

**CH3, PLDs.** **All of the arithmetic and all of the logic in slides 34–66 is correct** — the PROM
truth table and fuse map (42–43, 8 words × 8 bits), the PLA example and its programming table (45),
both PLA worked examples (46–47 and 48–49) and the PAL example with its 12-row programming table and
10-column fuse map (51–52). Slide 48's apparently misplaced overbars are a font artefact: at 7×
magnification the terms resolve as $F_1 = \bar{A}\bar{B}C + \bar{A}B\bar{C} + A\bar{B}\bar{C}$ and
$\bar{F_1} = AB + AC + BC + \bar{A}\bar{B}\bar{C}$, both agreeing with the printed maps.

**CH4, ADC.** The slide-5 bit stream $100110101011001001010$ is exactly the seven levels 4, 6, 5, 3,
1, 1, 2 in three bits each — 21 bits, all matching; slide 12's thirteen two-bit codes and slide 13's
thirteen four-bit codes all reproduce and are mutually consistent interval by interval; the flash
example of slides 16–17 reproduces exactly, all twelve codes and all three output-bit waveforms, on a
step of $8/8 = 1$ V; every circle on slide 22 is consistent with a single step of 0.625 V and the
ticked path is a valid four-trial search for any input in
$5.000\ \text{V} \le V_{\text{in}} < 5.625\ \text{V}$; slide 26's density figure (4096 ones at
$+\text{MAX}$, 2048 at mid-scale, 0 at $-\text{MAX}$ over a 4096-clock window) is internally
consistent; and slide 28's four other rows — $2^n - 1$ (counter type), 1 (flash), $n$ (SAR), $2^n$
(sigma-delta) — are all correct.

**CH4, DAC.** Slides 45 and 46 carry no text layer and exist only as images; both were read from the
renders, and all four equivalent circuits they show were re-derived independently and agree with the
figures. The R/2R ladder was additionally re-solved by nodal analysis from the printed component
values rather than trusted to the printed formula — which is how V06-9 was caught.

**CH5, slides 1–38.** All eight rows of every state table; all thirty-two flip-flop-input entries on
slide 29 and both its next-state columns; both K-maps on slide 17; both characteristic-equation
expansions on slide 30; every transition in every state diagram; the equivalence reduction of slides
35–36, confirmed both by partition refinement and by exhaustive simulation of all 2046 input strings
up to length 10; and all four excitation tables on `EXC` against their own characteristic tables.

**CH5, slides 39–71.** **All six machines are functionally correct** — Mealy and Moore versions of
the 101, the 010/1001 and the 1101 detectors — rebuilt from their printed diagrams and tables,
compared cell by cell in both directions, simulated over every input string of length 1 to 16, and
checked for completeness and reachability. The printed input/output pairs on slides 45 and 49
regenerate exactly, including the six markers $a$ to $f$. Slide 65's claims hold (1111101 does
contain 1101; 1101101 contains it twice, sharing the middle 1), as does slide 70's claim that $E$ and
$B$ have identical future behaviour, and the claim on slides 57, 63 and 70 that the Moore model needs
more states than the Mealy — 4 against 3, 8 against 6, 5 against 4.

**CH5, slides 72–118.** The 15-state tree and state table agree and meet the specification for all
sixteen four-bit input groups (75–76); the equivalences
$H \equiv I \equiv K \equiv M \equiv N \equiv P$, $J \equiv L$, $D \equiv G$ and $E \equiv F$ are
correct, partition refinement returns exactly
seven classes, and "15 states reduced to 7" is right (79–81); the implication chart is correct at
**every** pass — the same sixteen output-incompatible squares at step 1, the same implied pairs in
all twelve surviving squares, the same seven crosses in pass 1 and three in pass 2, none in pass 3 —
and the six-state reduced table is correct (83–89); every adjacency claim under Guidelines 1 and 2,
including the multiplicities (95); all sixteen next-state map cells (97); $A^{+} = X'$,
$C^{+} = A + XB'$ and $B^{+} = X'C' + A'C + A'B$ as equations (98); all twenty-four transition-table
entries (99–100); all four K-maps, $D_1$, $D_2$, $D_3$ and the cost figures of 10 gates and 26 gate
inputs (101); Cases I–IV, each meeting its specification and producing its printed $Z$ string
(103–112); all four line-code waveforms (114); both Manchester conversion machines, with the Moore
output exactly one Clock2 period behind the Mealy (115–116); and the next-state table, completeness
and mutual-exclusion identities and both shorthand examples (117–118).

**CH6.** The two SM blocks on slide 7 and the two SM charts on slide 8, by exhaustive enumeration;
the state sequence, three Moore outputs and two conditional outputs of the slide-10 timing chart for
$X = 1,1,1,0,0,0$; the link-path expressions on slide 18 in all six reachable rows; the hand
multiplication and eleven-line 9-bit add–shift trace (12); the nine-line four-register trace
including the Count column (13); all 48 cells of the three K-maps on slide 22 and all four
map-entered variables including both absorption steps; the fifteen-row sequence-of-operations table
(26–27); the six-row state table and the four equations $D_{G1}$, $D_{G0}$, $T_0$, $T_1$, $T_2$
(32–33); the weighing-machine ASM chart simulated for all 256 eight-bit inputs against the population
count (37); and both flip-flop state tables against $Q^{+} = D$ and $Q^{+} = JQ' + K'Q$ (39–40).

---

## 5. Open questions for a human

### 5.1 Where the correction came from

This distinction matters, and it is recorded honestly.

**Derived from the deck itself** — the deck contradicts itself, or its own numbers, table or figure
settle the matter. No outside authority was needed, and the reader can repeat the check on the
printed page: V01-1, V02-2, V02-3, V02-4, V02-5, V03-1, V03-2, V03-3, V03-4, V04-1, V05-1, V05-2,
V05-3, V05-5, V06-2, V06-3, V06-4, V06-5, V06-6, V06-7, V06-8, V07-1, V07-2, V08-1, V08-2, V09-1,
V09-2, V09-3, V10-1, V10-2, V10-3 — and every cosmetic entry except C09-2.

**Supplied from a standard result**, because the deck does not contain the material needed to settle
it:

- **V02-1** — the deck gives two incompatible integration-scale tables and nothing internal decides
  between them. The recommendation (teach slide 3's boundaries as *gates per chip*, take SLSI and
  ULSI from slide 4 as *transistors*) is a judgement informed by standard usage, not forced by the
  deck. **A human should confirm which set the unit will examine.**
- **V05-4** — the correct dual-slope count $2^{\,n+1}$ comes from the converter's two-phase timing,
  which the deck never derives. The internal evidence is only typographic (a lost bracket).
- **V07-3** — the T flip-flop's characteristic table is a standard result. The deck's own excitation
  table beside it uses $T$, which supports the correction but does not by itself establish it.
- **V06-1 and C05-3** — the $2^N$-levels/$2^N-1$-steps distinction and the strict Nyquist inequality
  $f_s > 2f_{\max}$ are standard statements; slide 48 and the slide-8 prose respectively support them
  but do not prove them.
- **C09-2** — "NP-complete" is standard terminology.
- **V06-9** — worth noting separately: this one has **both**. The deck contradicts itself (slides
  45(a) and 46 against slide 44), *and* an independent nodal analysis of the printed component values
  confirms the corrected weights. It is the best-evidenced correction in the log.

### 5.2 Marking-scheme risk

Where a printed value is wrong and is the deck's only stated result, a marking scheme derived from
the slide will award the printed answer. Raise with the department before the CAT: **V06-9**
($-3.4375$ V against $-6.875$ V), **V06-4** and its companions (the BCD DAC), **V06-3** (the printed
chain answers 7 bits), **V05-4** (the dual-slope count), and **C10-2** (an exam question may quote
slide 30's counter numbering while the marking scheme uses slides 24–34's).

### 5.3 Figures that could not be read — none outstanding

**All 348 slides are read. No figure remains unresolved.**

One figure was outstanding when this log was first written and has since been settled:

- **CH2 slide 24 — resolved 19 Aug 2026.** Each RTL circuit in the deck's own drawing style carries
  a solid triangle on the base lead. It was recorded as an unidentified mark and omitted from the
  redrawn figure rather than guessed at. A higher-magnification screenshot shows the triangle
  followed by **its own cathode bar** before the lead reaches the transistor: it is a **diode in
  series with the base**, anode at the summing node, cathode at the base. The redrawn Fig. 2-5 now
  includes it, labelled $D$.

  It is there because $R_1$ returns the base to a negative rail $V-$, which would otherwise drive
  the base below the emitter when the inputs are LOW; emitter-base reverse breakdown is only about
  5 to 7 V, and the diode stands off that reverse voltage. The slide corroborates this itself —
  circuit (iii) runs from $+V_{CC}$ with no negative rail and carries no diode. The deck states none
  of this in words, so the explanation is tagged `[added]` in
  `02-digital-logic-families.md`.

### 5.4 Redrawings that would benefit from a second pair of eyes

- **CH5 slide 32** is a hand-drawn scan and has been redrawn. The redrawing was checked **against the
  equations printed on slide 33** rather than traced pixel by pixel. The electrical behaviour is
  fully determined by those four equations and they have been verified against the state table, but
  the gate-level detail is worth a second look.
- **CH5 slides 8 and 21** are lifted from a standard textbook and have been redrawn from scratch as
  SVG rather than reproduced, because a reader must reason from them.

### 5.5 Third-party material and the repository rules

- **CH1 slides 2, 4, 6, 8, 9, 17, 26 and 30** are photographs, textbook scans or tool screenshots.
  All are **captioned rather than reproduced**. Slide 4 in particular is a widely circulated
  microprocessor-trend chart and should not be reproduced under any circumstances.
- **CH3 slide 21** is a published DRAM-organisation diagram and is described in the topic file rather
  than reproduced.
- **The deck footer.** Every slide carries a social handle in the footer instead of a name. It has
  been treated as a contact detail under the repository's no-contact-details rule and appears nowhere
  in the topic files, the figures or this log. **No personal name appears on any slide in any deck.**

### 5.6 Two things noted and deliberately not flagged

- **CH1 slide 8.** The printed equation for $\text{out}6$ includes the term
  $\text{in}3 \cdot \text{in}2 \cdot \overline{\text{in}1} \cdot \overline{\text{in}0}$, which covers
  only input 1100 — a don't-care for a decimal seven-segment decoder. The equation is therefore
  correct over every specified row but **not minimal**. Not flagged, because the montage is
  illustrative third-party material and the redundancy changes no stated result.
- **CH5 slide 41.** The waveform does not state which sequence it is detecting. What can be read from
  the drawing without guessing is recorded in the topic file — $x$ samples to $0,1,1,0,0$ at the five
  marked rising edges, and $w$ is drawn as a registered output held for exactly one clock period
  after the fourth edge. **No target sequence has been inferred.** A gap, not a defect.

### 5.7 For `_nomenclature.md`

Three clashes surfaced by this log and worth an entry in the clash table:

1. **The prime.** CH5 uses $'$ for *complement* throughout, but also for *next state* — $s'$ on slide
   16, $A'B'C'$ on slide 33 — sometimes eight lines apart on the same page (C07-4).
2. **The bit count.** Upper-case $N$ on CH4 slides 34–37, lower-case $n$ on CH4 slides 15, 44 and 47
   and throughout the ADC half (C05-5, C06-6).
3. **The noise margins.** $NM_L$/$NM_H$ on CH2 slide 12 and $V_{NL}$/$V_{NH}$ on slide 13, for the
   same two quantities (C02-1).

---

## Exam papers

Defects in the actual assessment papers (not the chapter decks). Entry IDs are `P1`, `P2`, …
allocated continuously across the whole `past-papers/` folder, and referenced by a `⚠ VERIFY` marker
at the matching question in `past-papers/<paper>.md`. Per standing instruction the full entry lives
**here only** — the paper file just points to it. These are kept deliberately separate from the
`V`/`C` numbering above, which catalogues defects in the lecturer's slides.

> ⚠ **This section does not start at P1.** `P1`–`P3` belong to the **CAT 1 of 6 August 2024** and
> predate this section: they were written into `past-papers/BEE3102-CAT1-2024-08-06.md` itself, under
> its own "Errata" heading, before the folder-wide convention existed. They have **not** been moved,
> and they carry no entry here. This series is therefore not a complete list of every exam defect in
> the subject — for the 2024 CAT 1, read that file.

**Allocation:** `P1`–`P3` = CAT 1, 6 Aug 2024 *(in that paper's own file)* · `P4`–`P7` = CAT 2,
25 Aug 2024 · `P8`–`P14` = End of Semester, 28 Oct 2024 · `P15`–`P17` = CAT 1, 14 Aug 2025 ·
`P18`–`P21` = End of Semester, 3 Nov 2025. **Next paper starts at `P22`.**

**A note on recurrence.** Four of the entries below (`P14`, `P16`, `P19`, `P20`) record the *same*
defect reappearing on a *later* paper, unfixed. The question bank is plainly being reused without
re-typesetting. When a defect is met on one paper, check whether it also sits on the others.

### P4 · CAT 2 (25 Aug 2024), whole paper — printed part-marks sum to 29, header says 30 ★
- **Paper:** the header reads "**(30 Marks)**". The printed allocations are Q1 (½, 1, ½, 2, 1, ½, 5½, 3), Q2 (8) and Q3 (7).
- **Issue:** those sum to $14 + 8 + 7 = \mathbf{29}$. One mark is unaccounted for on a 30-mark CAT. Recomputed in Python in exact fractions, 2026 — the halves are not a rounding artefact.
- **Two readings, and the page does not choose between them:** either a part has lost its allocation in typesetting, or the header is simply wrong. **Question 3 is the suspect** — it prints a single "(7 Marks)" against the question stem and gives parts (a), (b) and (c) **no individual marks at all**, where Question 1 itemises all eight of its parts. Three parts sharing 7 marks does not divide evenly either.
- **Nothing is cropped:** both photographs are complete, the sheets are consecutive, and Table 1 runs continuously from the foot of page 1 to the top of page 2.
- **How to handle:** if setting this as a timed mock, mark it out of 29 and say so, or scale to 30 and say so. **Do not invent a missing part.** Worth raising with the lecturer.
- **Severity:** structural (marks). Affects grading, not what is taught.

### P5 · CAT 2 (25 Aug 2024), Q2 and Table 1 — the initial state is named S0 but the table has no S0
- **Paper:** "State **S0** is the initial state, and the circuit enters state **S0** after the fourth input." Table 1's first row is Input Pattern "-", Present State "**S1**", and its fifteen states run **S1 … S15**.
- **Issue:** there is no S0 anywhere in Table 1, and no S16 either — the reset state *is* S1. A candidate following the prose looks for a state that does not exist; a candidate following the table has to silently reinterpret the prose. The reduction in part (ii) turns on which state is the reset, because every leaf row returns to it.
- **Correct form:** either rename the table's S1 to S0 and shift every index down, or change the prose to "State **S1** is the initial state, and the circuit enters state S1 after the fourth input." The second is the smaller edit and matches the table as printed.
- **How to handle:** work from the **table**. It is internally consistent — fifteen states, one reset, eight leaves, all returning to S1. Say plainly that the prose is wrong.
- **Severity:** structural (naming). No effect on the reduction if the table is trusted; considerable effect on a candidate who trusts the prose.
- **Recurs:** the identical table with the identical prose is reprinted as Table 1 of the **End of Semester of 3 Nov 2025**, Q2(a) — see **P20**.

### P6 · CAT 2 (25 Aug 2024), Q1 and Figure 1 — no initial state marked on the state diagram
- **Paper:** Figure 1 draws four Moore states $S_0/0$, $S_1/0$, $S_2/0$, $S_3/1$ with eight arcs. There is **no reset arrow, no double circle and no "start" label** on any of them.
- **Issue:** parts (ii) and (iii) ask which sequence is detected and what the case of detection is. Both answers are read from the path that ends in the output-1 state **starting from the reset state**. With no reset marked, the candidate has to assume one.
- **Correct form:** mark $S_0$ with an incoming reset arrow. ($S_0$ is the only state the numbering, the left-to-right layout and the "hold on 0" self-loop all point to, and it is the convention every worked machine in `09-state-reduction-and-assignment.md` uses — but that is an inference, not something the figure says.)
- **How to handle:** state the assumption explicitly in the answer. The diagram is otherwise complete and deterministic — every state carries exactly one 0-arc and one 1-arc, checked arc by arc.
- **Severity:** omission. Low impact, because only one reading is sensible; worth a sentence in any model answer.

### P7 · CAT 2 (25 Aug 2024) — cosmetic: no rubric printed, and the letterhead omits "SCIENCE IN"
- **Paper:** the sheet carries **no instruction line at all** — no "Answer ALL questions", no time-per-question guidance, nothing between the "CAT 2 · 1 Hr 20 Min · 25th August, 2024" rule and Question 1. The two End of Semester papers in this folder both print a three-point Instructions block.
- **Paper:** the letterhead reads "BACHELOR OF ELECTRICAL AND ELECTRONICS ENGINEERING", omitting "SCIENCE IN".
- **Correct form:** *Bachelor of Science in Electrical and Electronics Engineering*. The same omission is on all four papers transcribed in this batch, and the Thermodynamics log records it on that subject's 2024 papers too — it is a departmental letterhead, not a one-off slip.
- **How to handle:** with three questions and every part marked, "answer all" is the only reading. Assume it, and say so when setting the paper as a mock.
- **Severity:** cosmetic.

### P8 · End of Semester (28 Oct 2024), Q1(d) and Figure 2 — the state-01 self-loop asserts the output ★
- **Paper:** Figure 2 (the four-state diagram on page 2) labels the self-loop on state **01** as "**1/1**". Q1(d) asks: "What is the sequence detected by the sequence detector in figure 2?"
- **Issue:** the machine, coded up and simulated in Python (2026), differs from the canonical **overlapping 1001 Mealy detector** — under the same 00/01/10/11 encoding — in **exactly one** of its eight edges, and that edge is this self-loop. All seven others match, next state *and* output. As printed, the machine asserts $Z = 1$ on the suffixes **11, 011, 111, 0011, 0111, 1001, 1011 and 1111** — that is, on any input 1 arriving while the low state bit is 1. **It is therefore not a detector for one sequence, and the question as asked has no single correct answer.**
- **Correct form:** the self-loop is `1/0`. With that one change the machine is exactly the overlapping 1001 detector: $00 \xrightarrow{1/0} 01 \xrightarrow{0/0} 10 \xrightarrow{0/0} 11 \xrightarrow{1/1} 01$, with $01 \xrightarrow{1/0} 01$, $10 \xrightarrow{1/0} 01$ and $11 \xrightarrow{0/0} 00$.
- **How to handle:** teach the corrected machine, answer "**1001**, overlapping", and say plainly that the figure as printed also fires on 11. **Then point at Question 3(a) of the same paper**, which asks the candidate to design an overlapping 1001 detector from scratch for 15 marks — the corrected Figure 2 *is* the answer to Q3(a)(i). Whether that was intended is unknowable; that it is true is worth knowing before a mock.
- **Severity:** value. The most serious defect on this paper.
- **Recurs:** the identical figure, defect included, is reprinted as **Figure 3** of the End of Semester of 3 Nov 2025, Q1(g) — see **P19**.

### P9 · End of Semester (28 Oct 2024) — two different figures are both captioned "Figure 2"
- **Paper:** page 2 captions a **four-state** Mealy diagram "*Figure 2*"; page 3 captions a completely different **seven-state** Mealy diagram "*Figure 2*" as well. Q1(d) says "the sequence detector in figure 2"; Q4(a) says "state diagram in Figure 2".
- **Issue:** the two questions mean different figures, and nothing on the page says so. A candidate answering Q4(a) — "reduce the number of states" — could reasonably open the four-state diagram, which has nothing worth reducing, and lose 8 marks.
- **Correct form:** the page-3 diagram should be **Figure 3**.
- **How to handle:** the seven-state diagram is printed immediately below Q4(a) on the same page, so context resolves it. This knowledge base disambiguates them as `q1d-figure2-p2` and `q4a-figure2-p3` and never writes bare "Figure 2" for this paper.
- **Severity:** cataloguing (figure numbering).

### P10 · End of Semester (28 Oct 2024), Q1(h)(iii) — "Combinational Box" is not an ASM element
- **Paper:** "Illustrate with block diagrams and discuss the following terms as used in Algorithmic State Machines … **iii. Combinational Box** *(2 Marks)*".
- **Issue:** an ASM chart has **three** elements and none of them is a "combinational box". They are the **state box**, the **decision box** and the **conditional output box** — parts (i) and (ii) name the first two correctly, so the third is a slip for the third.
- **Correct form:** *Conditional output box*. `10-algorithmic-state-machines.md` §10.2 is titled "The three elements of an ASM chart" and names all three; ·CH6 slides 4–8 draw them.
- **How to handle:** answer the conditional output box, and say the paper's term is wrong. **On the student's own copy the printed words are struck through in blue ink and "Conditional Box" written underneath** — almost certainly copied from an invigilator's announcement during the sitting, which suggests the department knew. That annotation is *his*, not the paper's; do not quote it as printed text.
- **Severity:** value (terminology). 2 marks depend on knowing which box is meant.

### P11 · End of Semester (28 Oct 2024), Q2 — the third part is lettered "i)" instead of "c)"
- **Paper:** Question Two runs "**a)** Realize a PROM … **b)** Design a 4-bit DAC … **i)** Draw a clearly labelled schematic diagram for a 2 input CMOS NAND gate."
- **Issue:** the letter sequence breaks. Parts (a) and (b) have no roman sub-parts, so "i)" cannot be a sub-part of anything; it is the question's third top-level part.
- **Correct form:** **c)**.
- **How to handle:** treat it as part (c). This knowledge base writes it as "Q2(i)" so the paper can still be quoted exactly, and says what it should be at the question.
- **Severity:** structural (labelling). No effect on the physics.

### P12 · End of Semester (28 Oct 2024), Q2(b) — the DAC question prints no resistor values
- **Paper:** "Design a 4-bit DAC using binary-weighted resistors and calculate the output voltage for an input code of 1101, given that the reference voltage is 5V. *(6 Marks)*"
- **Issue:** a binary-weighted DAC's output is $V_{\text{out}} = -R_f \sum_i V_i / R_i$. The reference voltage alone does not determine it — **the question supplies neither an input resistor value nor the feedback resistor**, so $V_{\text{out}}$ cannot be computed as printed. The design half of the question is answerable; the "calculate" half is not.
- **Correct form:** any $R_f$ and MSB resistor. On the student's copy "**MSB = 1kΩ**" and "**Rf = 1kΩ**" are written in blue ink in the right margin — again, almost certainly an invigilator's announcement. **Those values are not printed on the paper** and must never be presented as given data.
- **How to handle:** answer symbolically — derive $V_{\text{out}} = -(R_f/R_{\text{MSB}}) \times V_{\text{REF}} \times D/8$ for $D = 13$, then substitute whatever values the marker supplies. State that the paper omits them. If the pencilled 1 kΩ / 1 kΩ is used, say where it came from.
- **Severity:** omission. Half of a 6-mark question is unanswerable as set.

### P13 · End of Semester (28 Oct 2024), Q1(b) and Figure 1 — circuit 1b shorts Q₄'s base to its own emitter
- **Paper:** in Figure 1's right-hand circuit (1b), the wire leaving $Q_4$'s base runs right, down, then left and lands on the **same vertical conductor** that carries $Q_3$'s and $Q_4$'s emitters, $Q_2$'s collector, $Q_5$'s base and the top of $R_4$. Junction dots are printed at both ends of that conductor.
- **Issue:** as drawn, $Q_4$'s base is tied to $Q_4$'s own emitter, so $V_{BE} = 0$ and the device can never conduct. **$Q_4$ is inert**, and the circuit reduces to $Q_1$/$Q_2$ into a single follower $Q_3$ and an output inverter $Q_5$ — which makes the truth table the question asks for depend on a device the drawing has disabled.
- **Not a photograph artefact.** The figure is printed **twice** in this folder — here and as Figure 1 of the **CAT 1 of 14 August 2025** — and both printings show the junction identically, at every magnification checked.
- **A second, related observation on the same figure:** in **both** sub-circuits the output stage has **no collector pull-up**. $Q_4$ (in 1a) and $Q_5$ (in 1b) each have their emitter on the ground rail and their collector wired straight to the Output terminal, with nothing tying that terminal to $V_{CC}$. The LOW output level is defined; the HIGH level is not. That is consistent with an open-collector gate, but nothing on the figure says so.
- **Correct form:** unknown. Two readings are possible — the base wire is meant to reach some other node, or one printed junction is meant to be a crossing — and the drawing does not choose. **NOT RESOLVED. Do not silently redraw it.**
- **How to handle:** answer the truth table from the input stage and the pull-down path, and state that the figure disables $Q_4$ as drawn. Ask the lecturer. Note also that circuit 1b is **not** one of the four families whose circuits the decks draw (diode logic, RTL, DTL, TTL — `02-digital-logic-families.md` §11–§14) and is not the CMOS pair of §15, so naming it may fall on the **ECL / plain PMOS-NMOS** row of the gap map in `00-index.md`. **No identification is asserted anywhere in this knowledge base.**
- **Severity:** structural (topology) plus ambiguity.

### P14 · End of Semester (28 Oct 2024), Q1(e) — the 9.99 V BCD full scale, reprinted from the 2024 CAT 1
- **Paper:** "A 16-bit Digital-to-Analog Converter (DAC) using a Binary Coded Decimal (BCD) input code has a full-scale output of **9.99V**… for an input code of 0110100101010111."
- **Issue:** this is **CAT 1 of 6 August 2024, Question 5, reprinted word for word and digit for digit** — and the defect in it is already logged, as **P1 inside `past-papers/BEE3102-CAT1-2024-08-06.md`**. 16 bits of BCD is four digits, maximum code 9999; a 9.99 V full scale gives a step of $9.99/9999 = 0.999$ mV, where 9.999 V gives exactly 1.000 mV. 9.99 V is the correct full scale for the **three**-digit converter on ·CH4 slide 37, which the question appears to be adapted from.
- **Effect:** about 6 mV on the final answer. The percentage resolution is 0.01 % either way.
- **How to handle:** answer as printed, note the discrepancy, and read P1 in the CAT 1 file for the full arithmetic — it is not repeated here. **Also note the wider point:** two questions on this paper (Q1(e) and Q1(g)) are the 2024 CAT 1 verbatim, and Q2(a)'s first minterm list is that CAT's Q4 first function. Work the CAT 1 answers before this paper.
- **Severity:** cataloguing (a known defect reprinted unfixed). The underlying value defect is P1's.

### P15 · CAT 1 (14 Aug 2025), Q3 — one "percentage resolution" for a converter addressed in two codings ★
- **Paper:** "A **12-bit** Digital-to-Analog Converter (DAC) has a full-scale output of 5V. Calculate; **a.** The percentage resolution *(1 Mark)* **b.** The output voltage for an input **BCD** code of 001110010001 *(1½ Mark)* **c.** Determine the output voltage for an input **octal** code of 725 *(1½ Mark)*".
- **Issue (two, compounding):**
  1. Part (a) asks for *the* percentage resolution before any coding is named, and parts (b) and (c) then address the same converter in **two different codings**. 12 bits of BCD is three decimal digits, maximum code 999; 12 bits of octal is four octal digits, maximum $7777_8 = 4095$. Those are different full-scale codes and therefore **different resolutions and different step sizes** — $5/999$ V against $5/4095$ V. Nothing on the paper says which (a) means, and there is no binary reading offered.
  2. $725_8$ is **three** octal digits — nine bits. A 12-bit octal-coded converter holds four. Whether the code should be padded to $0725_8$ (giving 469 of 4095) or read as a three-digit converter in its own right is not stated.
- **Correct form:** state the coding in part (a), and print the octal code with all four digits.
- **How to handle:** answer (a) for **both** codings, say so, and pad the octal code to $0725_8$ with the assumption written down. The KB's transfer relation is `06-digital-to-analogue-conversion.md` §6.2 and its resolution treatment §6.3; the deck's own BCD example on ·CH4 slide 37 is itself defective (**V06-4**, **V06-6**, **V06-7**), so do not revise this from the slide.
- **Severity:** ambiguity. The most serious defect on this paper.
- **Recurs:** reprinted word for word as **Q1(b)** of the End of Semester of 3 Nov 2025, remarked 1 / 2 / 2.

### P16 · CAT 1 (14 Aug 2025), Q6 — the "Xm(a,b,c)" typo, reprinted a year later
- **Paper:** "$W(a,b,c) = \sum m(0,1,3,5,7)$, $\;\mathbf{Xm}(a,b,c) = \sum m(0,2,4,5)$, $\;Y(a,b,c) = \sum m(1,2,4,7)$, $\;Z(a,b,c) = \sum m(0,3,5,6,7)$".
- **Issue:** the output is named $X$, in sequence with $W$, $Y$ and $Z$; the $m$ has migrated from the $\sum m$ that follows. This is **CAT 1 of 6 August 2024, Question 4, reprinted word for word — typo included** — and that occurrence is already logged as **P2 inside `past-papers/BEE3102-CAT1-2024-08-06.md`**.
- **Correct form:** $X(a,b,c) = \sum m(0,2,4,5)$.
- **How to handle:** read it as $X$ and move on. **The reason this is logged separately is the recurrence, not the typo:** a cosmetic slip surviving verbatim into a second cohort a year later is direct evidence that the question bank is reused without re-typesetting. Treat every question on the 2024 papers as a live candidate for the next one.
- **Severity:** cataloguing. The underlying cosmetic defect is P2's.

### P17 · CAT 1 (14 Aug 2025) — cosmetic slips
- **"(30 arks)"** — the mark total in the top right of the header, missing the M of "Marks".
- **"Sampling , Quantization"** (Q1) — a space before the comma.
- **"R = R_f = 10 k"** (Q8) — the ohm is omitted from both values. The reference voltage on the same line carries its unit.
- **"Find V_o if S₀ and S₁ is 1 and S₃, S₂, are all 0."** (Q8) — "is" for "are", a stray comma after $S_2$, and "all" of two items.
- **Letterhead** — "BACHELOR OF ELECTRICAL AND ELECTRONICS ENGINEERING", omitting "SCIENCE IN"; see P7.
- **Severity:** cosmetic. None of these changes an answer. Logged as one entry per the folder convention, not one each.

### P18 · End of Semester (3 Nov 2025), Q2(b) and Figure 4 — the DAC's input lines carry no bit labels ★
- **Paper:** Figure 4 draws a four-branch binary-weighted-input DAC with **120 kΩ, 60 kΩ, 30 kΩ and 15 kΩ** (top to bottom) into an inverting summing amplifier with $R_f = 10\ \text{k}\Omega$. Each branch begins at a **bare open circle**. Q2(b) then asks for $V_{\text{out}}$ for the binary inputs **1101** and **1010**.
- **Issue:** there is **no $D_0 \ldots D_3$, no MSB, no LSB, no A/B/C/D** on the figure, and the question text never says which line carries which bit. The code 1101 cannot be applied to the network without inventing the mapping. Reading it the wrong way round turns 1101 into 1011 and changes the answer.
- **Correct form:** label the branches. The resistor values are a clean $8 : 4 : 2 : 1$ ratio, so the **15 kΩ** branch carries eight times the current of the 120 kΩ branch and is the MSB *by construction* — but the figure does not say so, and it is drawn at the **bottom**, opposite to the usual MSB-at-top convention, which is exactly the trap.
- **How to handle:** state the assumption (15 kΩ = MSB, 120 kΩ = LSB) in the first line of the answer and work it through. Note that this is the **only** thing separating the question from `06-digital-to-analogue-conversion.md` §6.5, which is otherwise a complete treatment.
- **Severity:** omission. The most serious defect on this paper.

### P19 · End of Semester (3 Nov 2025), Q1(g) and Figure 3 — the defective self-loop, reprinted
- **Paper:** Figure 3 is the four-state Mealy diagram of the **28 October 2024 exam's Figure 2**, redrawn identically — including the **1/1 self-loop on state 01**. Q1(g) asks the same question ("What is the sequence detected by the sequence detector in figure 3?"), remarked 3 → 2.
- **Issue and correct form:** see **P8**. The self-loop should be `1/0`; as printed the machine also fires on 11 and the question has no single answer. Both printings were compared arc by arc; they are identical.
- **How to handle:** as P8. Answer the corrected overlapping 1001 detector and say plainly that both printings are wrong.
- **Severity:** value (a known defect reprinted unfixed). The underlying entry is P8's.

### P20 · End of Semester (3 Nov 2025), Q2(a) and Table 1 — the S0 / S1 mismatch, reprinted
- **Paper:** "State **S0** is the initial state, and the circuit enters state **S0** after the fourth input", above a Table 1 whose fifteen states run **S1 … S15**. Identical, row for row, to Table 1 of the CAT 2 of 25 August 2024.
- **Issue and correct form:** see **P5**. Work from the table.
- **One thing did change, and it is worth noting.** The CAT 2 stem read "A state table, table 1, was constructed **as a Mealy table** using a sufficient number of states…"; here those three words are removed, and a new part (i) asks "Does the resulting table specify a Mealy or a Moore circuit? *(1 Mark)*". The same table has been re-cut into a three-part question and the answer to (i) was previously printed in the stem. Any tutor setting the CAT 2 version as practice should delete those three words first.
- **Severity:** structural (naming), reprinted unfixed. The underlying entry is P5's.

### P21 · End of Semester (3 Nov 2025) — cosmetic slips
- **"and is circuit is to be designed using J-K flip-flops"** (Q3(a) stem) — "is" for "its".
- **"Simply the flip-flop input equations and the output logic using K-Maps"** (Q5(a)(vi)) — "Simply" for "Simplify".
- **"Figure 6 show a state diagram of a Moore Machine."** (Q4(a)) — "show" for "shows".
- **"(2 Mark)"** twice in Q1(b) — singular where two marks are awarded.
- **"Find V_o if S₀ and S₁ is 1 and S₃, S₂, are 0's."** (Q1(d)) — as P17, with "are 0's" replacing "are all 0"; the rest of the sentence is identical to the 14 Aug 2025 CAT's Q8.
- **Letterhead** — "BACHELOR OF ELECTRICAL AND ELECTRONICS ENGINEERING", omitting "SCIENCE IN"; see P7.
- **One structural oddity, not an error:** the Q3(a) stem states that the circuit uses three flip-flops, and part (i) then asks the candidate to determine how many are required. The answer is in the question. Worth a mark to the alert candidate, so it is noted rather than corrected.
- **Severity:** cosmetic. None of these changes an answer.

<!-- Later papers append their own P-numbered entries above this line. -->
