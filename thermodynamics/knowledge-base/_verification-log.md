---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
file_role: verification-log
source: "Built incrementally, one lecture document per stage. Covers all five lecture documents."
coverage: "ALL FIVE lecture documents verified — 200 / 200. GA1 and GA2 extracted AND solved; one substantive flag (V28) arises from GA1."
substantive_flags: 27
cosmetic_flags: 24
total_flags: 51
withdrawn_flags: 1
tags: [verification, errata, corrections, sign-conventions]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Verification log — MEC 3105

Every suspected defect found in the course material, with what the page **prints**, what it **should**
say, and **why** — stated as a check that can be repeated.

**Never silently corrected.** The printed version is recorded verbatim so it can be recognised when it
appears in a CAT, an exam, or a handout worked from the page.

| Class | Prefix | Meaning |
|---|---|---|
| Substantive | `V1`, `V2`, … | changes an answer, a sign, or a physical claim |
| Cosmetic | `C1`, `C2`, … | typography, a stale definition, a figure/text mismatch — nothing computed changes |

**Method** (per `../../docs/kb-format.md` § Verification): every numerical claim recomputed
independently; every equation checked for dimensional consistency, algebraic consistency, symbol slips,
mislabelled results and self-reference.

**Exactly how each document was read** — stated precisely, because the standard matters:

| Doc | Render coverage |
|---|---|
| **TT** | all 17 pages at 160 dpi; p13's two suspect lines re-rendered at **400 dpi** (V1, V2); Figure 5 at **300 dpi** (C2) |
| **FL** | all 37 slides at 170 dpi |
| **EPC** | all 92 slides at 165 dpi, including all 17 image-only slides |
| **TC** | all 24 slides at 170 dpi, including the image-only slide 2 |
| **HE** | **every slide carrying an embedded image or a typeset equation** read at 170 dpi — verified by enumerating the PDF's image XObjects, which occur on exactly slides **2, 8, 9, 10, 16, 18, 26, 27, 28**; all nine read, plus the native table on s20. The other 20 slides contain **no embedded images** and are native text or native PowerPoint tables, extracted in full and cross-read. |

**No figure or equation anywhere in this knowledge base is described without having been looked at.**

**Page citations are the document's own printed footer numbers.** TT's footer starts at 2 on the title
page, so a PDF viewer shows one less: `p13` = PDF page 12.

---

## Summary — all five lecture documents

| Doc | Pages | Substantive `V` | Cosmetic `C` | Status |
|---|---|---|---|---|
| **TT** — Temperature and Thermometry | 17 | 4 | 2 | ✅ |
| **FL** — First Law | 37 | 5 | 5 | ✅ |
| **EPC** — Energy Equations & Phase Changes | 92 | 8 | 8 | ✅ |
| **TC** — Thermodynamic Cycles | 24 | 5 | 7 | ✅ |
| **HE** — Heat Engines & Carnot | 30 | 4 | 2 | ✅ |
| **Total (lecture documents)** | **200 / 200** | **26** | **24** | **50 flags** |
| **GA1** — group activity | — | **1** *(V28)* | 0 | ✅ complete |
| **Grand total** | — | **27** | **24** | **51 flags** |

**Numbering note.** IDs are issued in build order, one document at a time, and are **not contiguous** —
`C12`, `C13`, `C14` and `C20` were never issued. Every ID matches the inline flag in the topic file that
raised it; none has been renumbered.

> ### ⚠ V12 was WITHDRAWN — it was a false flag
>
> **V12 claimed that ·EPC s70's reversed-Carnot $P$–$v$ diagram had a mis-pointing arrow that made the
> loop untraversable. It does not. The figure is correct.**
>
> What was missed: the **lower diagram renumbers its states** — 2 and 4 swap places relative to the
> upper diagram (1 upper-left, **2 lower-left**, 3 lower-right, **4 upper-right**). Carrying the upper
> diagram's numbering down makes the correct leftward 4→1 arrow look like a wrong 3→2 arrow. Re-checked
> at **400 dpi**: the arrowhead on the lower isotherm points **right, 2→3**, and all four arrows form a
> complete counter-clockwise loop.
>
> **Withdrawn rather than renumbered**, so that anyone who read the earlier version can see what
> changed. `V12` is now a retired ID and is not reused.
>
> *Recorded because the failure mode matters: a false entry in an errata log tells a student a correct
> textbook figure is broken. This was caught by an independent verification pass over the finished
> knowledge base — see § Verification of the knowledge base itself.*

### The three findings that matter most

1. **FL does not hold one sign convention** (V5–V8). It states both, seventeen slides apart, and its only
   worked example mixes them — giving an answer **wrong by a factor of five**.
2. **No lecture document gives an efficiency formula for Otto, Diesel, Brayton, Rankine or Stirling.**
   Confirmed across all five. They are named and tabulated, never analysed.
3. **Entropy is almost absent.** No general definition anywhere. ·HE s28 supplies the only entropy
   equations in the course, and they are Carnot-specific.

### Where the arithmetic stands

| Doc | Numerical content | Verdict |
|---|---|---|
| TT | 1 worked example + fixed points | ✓ except V4 (rounding before subtracting) |
| FL | 1 worked example | ✗ **final answer wrong** (V8) |
| **EPC** | **9 worked examples + a 5-row table + unit conversions** | ✅ **every number correct** |
| TC | none — zero arithmetic in 24 slides | — |
| HE | none — zero arithmetic in 30 slides | — |

**EPC is the only source of worked numbers in the course, and all of them check out.**

---

## TT — Temperature and Thermometry

### V1 · Absolute zero printed without its minus sign ·TT p13

**Printed:**

> "…**the pressure extrapolates to zero when the temperature is 273.15°C.** This particular
> temperature is universal in its importance, because it doesn't depend on the substance used in the
> thermometer. We define this temperature as **absolute zero.**"

**Should read:** $-273.15\ ^\circ\mathrm{C}$.

**Why.** Absolute zero is $-273.15\ ^\circ\mathrm{C}$ by the definition of the Celsius scale relative
to the Kelvin scale — TT's own Equation 1 on the same page gives $T_C = T - 273.15$, so $T = 0$ yields
$T_C = -273.15$. As printed, the claim places absolute zero **above the steam point**
($100\ ^\circ\mathrm{C}$), where a gas has high pressure and is nowhere near liquefying. The
extrapolation described runs *backwards* toward negative temperatures — the page says so two sentences
earlier ("extended back toward negative temperatures").

**Confirmed a page defect, not a text-extraction artefact.** The line was re-rendered at 400 dpi
specifically to settle this: the character before "273.15" is a space, and the sentence begins
"extrapolates to zero when the temperature is 273.15°C". Nothing was lost in extraction.

**Impact:** high if learnt from the page, because a sign error in absolute zero propagates into every
Kelvin conversion. Low in practice because Equation 1, one line below, is printed correctly.

---

### V2 · The same missing minus, in the definition of the Kelvin zero ·TT p13

**Printed:**

> "Absolute zero is used as the basis for the **Kelvin temperature scale,** which sets 273.15°C as its
> zero point (0 K)."

**Should read:** "…which sets $-273.15\ ^\circ\mathrm{C}$ as its zero point (0 K)."

**Why.** Same reasoning as V1, and the sentence is internally self-contradictory as printed: it
equates $273.15\ ^\circ\mathrm{C}$ with $0\ \mathrm{K}$, whereas Equation 1 on the same page gives
$T_C = 273.15 \Rightarrow T = 546.30\ \mathrm{K}$. A statement of the form "$X\ ^\circ\mathrm{C}$ is
$0\ \mathrm{K}$" can be checked against Equation 1 in one step — do that whenever the value looks
ambiguous.

**Confirmed a page defect** at 400 dpi, as V1.

**Recorded separately from V1** rather than merged: two occurrences in adjacent paragraphs establish
that this is the page's own defect rather than a single stray character, which is why neither is
treated as an artefact.

---

### V3 · Example 1(b) cites the wrong equation ·TT p17

**Printed:**

> "**(b)** Convert the lower and higher temperatures using Equation 2a:
> $T_C = T - 273.15 \rightarrow T = T_C + 273.15$"

**Should read:** "using **Equation 1**".

**Why.** Equation 2a is $T_F = \tfrac95 T_C + 32$, the Celsius→Fahrenheit relation. The working that
follows is $T = T_C + 273.15$, which is **Equation 1** rearranged — and is the correct tool for part
(b), which asks for Kelvin. Applying Equation 2a as instructed would convert the Celsius answers from
part (a) straight back to $72\ ^\circ\mathrm{F}$ and $84\ ^\circ\mathrm{F}$, answering nothing.

Part (a) is introduced identically ("using Equation 2b") and **is** correct there, so the label in (b)
looks like a copy-and-edit slip that was not updated.

**The printed working and both printed endpoint answers are correct.** Only the cross-reference is
wrong.

**Impact:** low when reading the worked solution, since the correct equation is written out on the
next line. Higher when working from the instruction alone — for instance when re-deriving the example
from the question, or when a CAT lifts the phrasing.

---

### V4 · $\Delta T = 7\ \mathrm{K}$ — rounded before subtracting ·TT p17

**Printed:**

> $T = 22.2 + 273.15 = \boxed{295\ \mathrm{K}}$
> $T = 28.9 + 273.15 = \boxed{302\ \mathrm{K}}$
> "Find the difference of the two temperatures:"
> $\Delta T = 302\ \mathrm{K} - 295\ \mathrm{K} = \boxed{7\ \mathrm{K}}$

**Should read:** $\Delta T = 6.7\ \mathrm{K}$.

**Why — three independent checks, any one sufficient.**

**1. The unrounded arithmetic.** From $72\ ^\circ\mathrm{F}$ and $84\ ^\circ\mathrm{F}$:

$$T_C = \tfrac59(72-32) = 22.\overline{2}\ ^\circ\mathrm{C} \;\Rightarrow\; T = 295.37\ \mathrm{K}$$
$$T_C = \tfrac59(84-32) = 28.\overline{8}\ ^\circ\mathrm{C} \;\Rightarrow\; T = 302.04\ \mathrm{K}$$
$$\Delta T = 302.04 - 295.37 = 6.67\ \mathrm{K}$$

The printed $7$ arises **only** because $295.35$ and $302.05$ were each rounded to three significant
figures *before* the subtraction. Rounding two nearby numbers and then differencing them destroys
precisely the digits the difference depends on.

**2. TT's own statement, p14.** "Because the size of a Celsius degree is the same as a kelvin, a
temperature difference of $5\ ^\circ\mathrm{C}$ is equal to a temperature difference of
$5\ \mathrm{K}$." Hence $\Delta T = \Delta T_C$ **exactly**. Part (a) of the same example gives
$\Delta T_C = 6.7\ ^\circ\mathrm{C}$, so part (b) must give $6.7\ \mathrm{K}$. As printed, the example
reports $6.7\ ^\circ\mathrm{C}$ and $7\ \mathrm{K}$ for the same physical change — contradicting the
principle stated three pages earlier.

**3. TT's own Equation 3, which the page then instructs the student to apply.** The page closes with
"Use Equation (3) to prove your results?":

$$\Delta T_F = 84.0 - 72.0 = 12.0\ \mathrm{F}^\circ \;\Rightarrow\;
\Delta T_C = \tfrac59(12.0) = 6.67\ ^\circ\mathrm{C} = 6.67\ \mathrm{K}$$

**The exercise the page sets disproves the answer the page gives.** This is the strongest form of the
check, and it needs no external reference — the whole disagreement is internal to TT.

**Impact:** high, and higher than it looks. The example is the document's only worked calculation, so
it is the most likely thing to be lifted into a CAT. It also teaches a method error (round early, then
subtract) rather than only a wrong digit — and the correct value, $6.7\ \mathrm{K}$, is the one that
demonstrates the Celsius-degree-equals-kelvin identity the topic exists to establish.

**Note:** the two printed **endpoint** values, $295\ \mathrm{K}$ and $302\ \mathrm{K}$, are correct to
three significant figures. Only their difference is affected.

---

### C1 · The kelvin defined via the triple point — superseded definition ·TT p14

**Printed:**

> "**The SI unit of temperature, the kelvin, is defined as 1/273.16 of the temperature of the triple
> point of water**"

**Status.** This was the SI definition of the kelvin **from 1954 until 20 May 2019**. In the current
SI the kelvin is defined by fixing the Boltzmann constant at
$k = 1.380\,649\times10^{-23}\ \mathrm{J\,K^{-1}}$ exactly, and the triple-point temperature became a
*measured* quantity ($273.16\ \mathrm{K}$ with a small experimental uncertainty) rather than a
definition.

**Why it is cosmetic, not substantive.** Nothing computed anywhere in this course changes.
$273.16\ \mathrm{K}$ remains the triple point of water to far better precision than any figure MEC
3105 uses, TT's own 1954 framing is stated correctly and in context ("a procedure based on two new
points was adopted in 1954"), and the definition is not used in any calculation.

**How to handle it.** **Reproduce the printed definition** — it is what the course teaches and what an
exam will mark. Logged only so that meeting the modern definition elsewhere is not mistaken for
contradicting the notes.

---

### C2 · Figure 5 shows one calibration line; the text describes several, plus an extrapolation ·TT p12–13

**Printed** (p12, immediately below the figure):

> "If the **curves** in Figure 5 are extended back toward negative temperatures, we find a startling
> result: In every case, regardless of the type of gas or the value of the low starting pressure, **the
> pressure extrapolates to zero when the temperature is 273.15°C.**"

**What Figure 5 actually shows.** Axes $P$ against $T\ (^\circ\mathrm{C})$, gridded, ticked at $0$ and
$100$. **One** straight orange line joins a black dot at $T=0$ to a black dot at $T=100$, with a dashed
vertical dropping from the upper dot to the $100$ tick. Two green callout boxes label those dots
("Pressure at the freezing point of water", "Pressure at the boiling point of water"). The horizontal
axis begins at $0$, so no part of the negative-temperature extrapolation is drawn.

**The green lines are callout leaders, not plotted data** — confirmed at 300 dpi: both are drawn in the
callout boxes' own green, and both terminate in the boxes' speech-bubble tails. Worth stating explicitly
because the **left** leader runs steeply and diagonally *through* the plot area from the $T=0$ dot up to
its box, so at a glance it reads as a second, steeper calibration line. It is not one. Anyone
reconciling the "curves" plural by counting that leader as a second gas's line is being misled by the
layout.

**Two mismatches.**

1. "**Curves**" (plural), and "regardless of the type of gas or the value of the low starting
   pressure", imply a **family** of lines converging on a common intercept. One line cannot exhibit
   substance-independence — the convergence *is* the startling result being described.
2. The **extrapolation to absolute zero is not drawn**, so the figure cannot support the sentence that
   cites it.

**Why cosmetic.** The text is correct; the figure is correct; they simply do not depict the same
thing, and the reader is sent to a figure that does not contain the evidence. Nothing computed
changes.

**How to handle it.** Sketch the missing version when studying this section: two or three lines of
different slope from different gases, all extended leftwards as dashed lines to meet the $T$-axis at
the same point, $-273.15\ ^\circ\mathrm{C}$. That sketch is the examinable content, and it is a
plausible "sketch and explain" question. Do not expect to find it on the page.

*(This flag is deliberately conservative: without a render of the source Figure 5 was described from,
it cannot be told whether a multi-line figure was reduced to one line, or the text was adapted around
a single-line figure. Either way the reader needs the warning.)*

---

## Not defects — checked and cleared

Recorded so they are not re-flagged, and because two were suspected before renders were available.

| Item | Page | Finding |
|---|---|---|
| `―hotness‖` / `―coldness‖` | p3 | **Text-extraction artefact only.** The render shows correct typographic quotation marks. No ID. |
| Equation 1, $T_C = T - 273.15$ | p13 | Correct as printed. ✓ |
| Equation 2a, $T_F = \tfrac95 T_C + 32$ | p15 | Correct; reproduces $32\ ^\circ\mathrm{F}$ at $0\ ^\circ\mathrm{C}$ and $212\ ^\circ\mathrm{F}$ at $100\ ^\circ\mathrm{C}$. ✓ |
| Equation 2b, $T_C = \tfrac59(T_F-32)$ | p15 | Exact inverse of 2a, bracket correctly placed. ✓ |
| Equation 3, $\Delta T_F = \tfrac95\Delta T_C$ | p15 | Follows from 2a by differencing; offset correctly cancelled. ✓ |
| $50\ ^\circ\mathrm{F} = 10\ ^\circ\mathrm{C} = 283\ \mathrm{K}$ | p15 | Recomputed: $\tfrac59(18)=10.0$; $283.15 \to 283$. ✓ |
| Triple point $0.01\ ^\circ\mathrm{C}$, $4.58\ \mathrm{mmHg}$, $273.16\ \mathrm{K}$ | p13 | All three standard and mutually consistent. ✓ |
| Ice/steam points across all three scales | p9, p14 | $0/100\ ^\circ\mathrm{C}$, $273.15/373.15\ \mathrm{K}$, $32/212\ ^\circ\mathrm{F}$. ✓ |
| Example 1(a): $22.2$, $28.9$, $6.7\ ^\circ\mathrm{C}$ | p17 | All three recomputed. ✓ |
| Example 1(b) endpoints: $295\ \mathrm{K}$, $302\ \mathrm{K}$ | p17 | Correct to 3 s.f. Only the difference is wrong — V4. ✓ |
| Zeroth-law statement | p6 | Standard form, correctly stated. ✓ |
| Definitions of thermal contact / equilibrium / heat | p5 | Standard; "no **net** exchange" correctly qualified. ✓ |
| The six physical properties used in thermometry | p8 | Standard list, all six physically valid. ✓ |
| Figure 1 order-of-magnitude labels | p4 | Consistent with the logarithmic axis as drawn. ✓ |
| Blank yellow highlight shape | p18 | Empty annotation below the questions. Contains nothing; no content is hidden. No ID. |

---

## FL — First Law of Thermodynamics

### ⚠ The FL sign-convention fault — root cause of V5, V6, V7, V8

**FL states two mutually contradictory sign conventions for $W$, both explicitly.**

> **s13** — "Some conventions. For the gases perspective: … **Work done on the gas is positive**, work
> done by the gas is negative."

> **s30** — "$W < 0$: work done **on** the system.  $W > 0$: work done **by** the system."

These are exact opposites. $Q$ is positive into the system on both, so heat is never at issue.

| Convention | First law | Boundary work | Slides |
|---|---|---|---|
| **A** — physics ($W>0$ = on) | $\Delta U = Q + W$ | $W = -P\Delta V$ | s7–s8, **s13**, s19–s20, s23–s28 |
| **B** — engineering ($W>0$ = by) | $\Delta U = Q - W$ | $W_b = +\int P\,dV$ | s12, s15–s18, s21–s22, **s30**, s31–s33 |

**What this means for the Stage 0 note.** The Stage 0 observation recorded a clash between FL and GA2.
That understates it: the clash is **internal to FL first**, and GA2 agrees with FL's own second half.
**Default to convention B** for assessed work.

**How to tell which convention a slide is in, in two seconds:** $W_b = +\int P\,dV$ ⇒ B;
$W = -P\Delta V$ ⇒ A. Or: $\Delta U = Q - W$ ⇒ B; $\Delta U = Q + W$ ⇒ A.

---

### V5 · $W = P\Delta V$ for work done *on* the gas ·FL s7

**Printed:** "External agent did work in pushing the piston inward. $W = Fd$, $=(PA)\Delta x$,
**$W = P\Delta V$**"

**Should read:** $W_{\text{on}} = -P\,\Delta V$.

**Why.** For a compression $\Delta V < 0$, so $P\Delta V$ is **negative** — contradicting the slide's
own sentence that the external agent did work *on* the gas, and contradicting s8's $W = \Delta U$ with
s6's "the temperature will rise". The deck's own worked example writes the same quantity correctly as
$W = -P\Delta V$ (s20), so the deck is internally inconsistent between s7 and s20.

---

### V6 · The first law written in the wrong convention for this deck ·FL s12

**Printed:** "Work is done on the gas, heat is added to the gas and the internal energy of the gas
increases!  **$Q = W + \Delta U$**"

**Should read:** $Q = \Delta U - W$, i.e. $\Delta U = Q + W$, given s13's stated convention.

**Why — a one-line check.** Set $Q = 0$ (insulated). The printed form gives $\Delta U = -W$: the gas
**cools** when work is done on it. But s6 says the temperature **rises**, and s8 states $W = \Delta U$.
Three slides contradict s12.

$Q = W + \Delta U$ is the correct **engineering-convention** form. Its appearance here, one slide before
s13 declares the physics convention, is the origin of the whole fault line — and it propagates directly
into the worked example (V8).

**Impact: high.** This is the slide a student will copy as "the first law".

---

### V7 · $Q$ and $W$ swapped against the slide's own descriptive boxes ·FL s17

**Printed:** the braces read "Initial Energy $E_1$" $+$ "**Energy gain $W_{1-2}$**" $-$
"**Energy loss $Q_{1-2}$**" $=$ "Final Energy $E_2$", boxed as

$$E_1 + W_{1-2} - Q_{1-2} = E_2$$

**Should read:** $E_1 + Q_{1-2} - W_{1-2} = E_2$.

**Why.** The descriptive boxes across the **top of the same slide** say: change in energy = net energy
transferred **in by heat transfer** − net energy transferred **out by work**. That is $\Delta E = Q - W$,
which is also exactly what s18 prints. The braces and the boxed result invert both.

**Impact:** moderate. The correct form is on the next slide, but s17 is the one with the memorable
picture.

---

### V8 · The worked example's final answer is wrong ·FL s20

**Printed:** $Q = W + \Delta U = 1013 - 1518 = \boxed{-505\ \mathrm{J}}$ heat out

**Should read:** $\boxed{Q = -2532\ \mathrm{J}}$.

**Why.** The example mixes both conventions inside one calculation: it correctly uses
$W = -P\Delta V = +1013\ \mathrm{J}$ for work done **on** the gas (convention A) and then substitutes
that into $Q = W + \Delta U$ (convention B, from V6). The work term enters with the wrong sign.

$$Q = \Delta U - W_{\text{on}} = -1519.5 - 1013.0 = -2532\ \mathrm{J}$$

**Independent confirmation, using no first law at all.** Isobaric heat for a monatomic ideal gas is
$Q = n c_p \Delta T$ with $c_p = \tfrac52 R$:

$$Q = 2.0317 \times \tfrac52 \times 8.31 \times (-60) = -2532\ \mathrm{J}$$

Exact agreement. The printed error is $+2026\ \mathrm{J} = 2 \times 1013 = 2W$ — the arithmetic
signature of a flipped sign on $W$. **The printed answer is one fifth of the correct magnitude.**

**Every intermediate value on the slide is correct:**

| Quantity | Slide | Recomputed |
|---|---|---|
| $n$ | 2.03 mol | 2.0317 mol ✓ |
| $\Delta T$ | −60 K | −60.00 K ✓ |
| $W$ on gas | +1013 J | +1013.0 J ✓ |
| $\Delta U$ | −1518 J | −1519.5 J ✓ |
| **$Q$** | **−505 J** | **−2532 J** ✗ |

**A sanity check that catches it on sight.** The gas is compressed *and* cooled, so the heat leaving
must be **larger** in magnitude than $|\Delta U|$, not smaller. $|-505| < |-1519|$ is impossible.

**Impact: highest in the subject so far.** This is FL's only worked example, so it is the likeliest
thing for a CAT to reuse, and the error is in the answer a student would memorise.

---

### V9 · Process-equation derivation opens in the wrong convention ·FL s22

**Printed:** "For an ideal gas in any mechanically reversible closed-system process (if
$W_{\text{other}} = 0.0$): $dQ - dW = C_V dT$.  Since $dW = P\,dV$ …"

**Should read**, to match s23–s28: $dQ + dW = C_V\,dT$ with $dW = -P\,dV$.

**Why.** Slides 23–28 that follow are all in convention **A** — isothermal $W = -RT\ln(V_2/V_1)$,
isobaric $W = -R(T_2-T_1)$, adiabatic $W = \Delta U = C_V\Delta T$. s22's opening two lines are in
convention **B**.

**Mitigating.** The **third** line, $dQ = C_V\,dT + P\,dV$, and everything derived from it — including
$dQ = (C_v + R)dT - RT\,dP/P$ — are correct **in both readings**, because the two sign slips cancel. So
the usable output of the slide is sound; only the stated premises are inconsistent with what follows.

---

### C3 · $V$ used for velocity ·FL s15, s18

$\Delta\mathrm{KE} = \tfrac12 m(V_2^2 - V_1^2)$ uses $V$ for **velocity**, while the rest of the deck
uses $V$ for **volume** — and s18 writes bold $\mathbf{V}$ for velocity next to plain $V$ for volume in
the same line. Cosmetic in origin but a whole-answer error if substituted wrongly. Registered in
`_nomenclature.md`.

### C4 · $T_f$ left blank ·FL s20

The example's data line ends "$T_f =$" with no value. Must be obtained from $PV = nRT$:
$T_f = 240\ \mathrm{K}$. Not an error, but the slide cannot be followed as printed.

### C5 · Capital I for the digit 1 ·FL s28

$\gamma = C_P/C_V = (C_V+R)/C_V$ is printed as equal to "$I + R/C_V$" — a capital letter **I** where
the digit **1** belongs. Font or scan artefact; the physics ($\gamma = 1 + R/C_V$, hence
$C_P - C_V = R$) is correct.

### C6 · $\delta$ overloaded ·FL s29

$\delta$ is used for the **polytropic index** ($\delta = 0, 1, \gamma, \infty$) while the same deck uses
$\delta$ for the **inexact-differential operator** ($\delta Q$, $\delta W$) on s16, s18, s30 and s32.
Most texts write $n$ for the polytropic index — which in this deck collides with $n$ = number of moles.
No symbol is safe; read from context. Registered in `_nomenclature.md`.

### C7 · Title typo ·FL s32

"Moving Boundary **Woek**" — for "Work".

---

## FL — checked and cleared

| Item | Slide | Finding |
|---|---|---|
| $1\ \mathrm{cal} = 4.184\ \mathrm{J}$ | s2 | ✓ |
| Four forms of the energy balance | s16 | ✓ all standard |
| $W_{\text{net,out}} = Q_{\text{net,in}}$ for a cycle | s16 | ✓ |
| $\Delta\mathrm{KE}+\Delta\mathrm{PE}+\Delta U = Q-W$, $dE = \delta Q - \delta W$ | s18 | ✓ |
| Enthalpy derivation, all four steps; $H = U+PV$; $\Delta U + W_b = \Delta H$ | s21 | ✓ |
| $dQ = (C_v+R)dT - RT\,dP/P$ | s22 | ✓ algebra correct |
| Isothermal, isobaric, isochoric, adiabatic relations | s23–s26 | ✓ **all four internally consistent** against $\Delta U = Q+W$ |
| $TV^{\gamma-1}$, $TP^{(1-\gamma)/\gamma}$, $PV^\gamma$; $\gamma = C_P/C_V$ | s27 | ✓ |
| $C_P - C_V = R$; $C_V = R/(\gamma-1)$; eliminated-$V_2$ adiabatic work | s28 | ✓ |
| Polytropic index values $0, 1, \gamma, \infty$ | s29 | ✓ |
| $\dot W = 6\ \mathrm{kW}$, $w = 15\ \mathrm{kJ/kg}$ from 30 kJ / 2 kg / 5 s | s30 | ✓ recomputed |
| $W_b = \int P\,dV$; path dependence; cycle enclosed area | s31–s33 | ✓ |
| $Pv = RT$; $R = R_u/M$; six $R_u$ unit forms; four specific gas constants | s34 | ✓ recomputed: $8.31447/28.013 = 0.2968$ for N₂ |
| $Pv = ZRT$; $Z$ definitions; reduced properties | s35–s36 | ✓ |
| Beattie-Bridgeman, Benedict-Webb-Rubin, virial forms | s37 | ✓ match standard references |

---

## EPC — Energy Equations and Phase Changes

Full detail in `03a-phase-behaviour-and-equilibrium.md` and `03b-second-law-and-cycles.md`.

### V10 · Carnot's dates ·EPC s68
**Printed:** "French military engineer Nicolas Sadi Carnot (**1769**-1832)…"
**Should read:** **1796**–1832.
**Why.** Sadi Carnot was born 1 June 1796 and died 24 August 1832, aged 36. As printed he would have
lived 63 years and published *Réflexions* (1824) at 55 rather than 28. Digit transposition 1796→1769.
Confirmed at 4× zoom; the digits are unambiguous.

### V11 · Diesel described as compressing a fuel-air mixture ·EPC s88
**Printed:** "the burning of fuel is triggered by heat generated in compressing **fuel-air mixture**"
**Should read:** compressing **air**; fuel is injected into the already-hot compressed air.
**Why.** Compressing a fuel-air mixture is the **Otto** (spark-ignition) arrangement. The slide
contradicts ·EPC s85 ("takes in JUST air") and ·EPC s91 ("Piston compresses air upwards. Fuel injected.")
in the same deck.

### V13 · The $f$-function is inverted mid-derivation ·EPC s75
**Printed:** $f(T_1,T_3)$ is identified with $Q_1/Q_3$, then concluded to equal $T_3/T_1$.
**Should read:** either the chain as $Q_3/Q_1 = (Q_3/Q_2)(Q_2/Q_1)$, or $f = \theta(T_1)/\theta(T_3)$.
**Why.** As printed it gives $Q_1/Q_3 = T_3/T_1$, the **inverse** of ·EPC s76's own result
$Q_L/Q_H = T_L/T_H$ ($Q_1$ is hot-side, $Q_3$ cold-side). **The final $\eta_{th,rev} = 1 - T_L/T_H$ is
correct** — only the intermediate step is inverted.

### V14 · Dimensionally impossible increment, and a sign that contradicts the drawing ·EPC s37
**Printed:** $v_i' = v_i + dp$ … and $P' = P + dp$.
**Should read:** $v_i' = v_i + dv$, and $P' = P - dp$.
**Why.** (a) A **volume** cannot be incremented by a **pressure** differential; the very next panel writes
the same relation correctly as $v_i'' = v_i' + dv$. (b) **Count the weights** — they reduce 4 → 3 → 2 → 0
as the piston rises. Removing weight *lowers* the pressure, so $P$ and $v$ cannot both increase.

### V15 · The first law's criterion presented on a "Second law" slide ·EPC s23
**Printed:** "Internal energy lets us access whether a change is permissible. Only those changes occurs
for which the internal energy of an isolated system remains constant." — on a slide titled *Second law
of Thermodynamics*.
**Should read:** labelled as the **first** law; $\Delta U_{\text{isolated}} = 0$ is not a second-law
criterion.
**Why.** ·EPC s39 of the same deck says "The first law of thermodynamics gives no information about
direction". A student revising from s23 alone would attribute $\Delta U = 0$ to the second law.
(Also *access*→*assess*, *changes occurs*→*changes occur*.)

### V16 · Two dropped glyphs make the equivalence proof unfollowable ·EPC s57–s58
**Printed:** the s57 figure arrow is labelled "**$Q_H + Q$**" (subscript $L$ clipped); the s58 prose reads
"the difference between **QL  QH** and QH" (the **+** is missing — a blank gap, not a faint plus).
**Should read:** $Q_H + Q_L$, and "the difference between $Q_L + Q_H$ and $Q_H$".
**Why.** A bare "$Q$" is defined nowhere in the deck, and as printed a reader could take $Q_L - Q_H$,
which reverses the sign and destroys the argument that the combination violates Clausius.

### V17 · "No forces holding molecules together" ·EPC s7
**Printed:** "No forces holing molecules together" (gas).
**Should read:** **negligible** (very weak) intermolecular forces.
**Why.** Zero attractive force means a gas could never condense — yet the same slide's last bullet says a
gas "can only exist above condensation temperature", and ·EPC s10's figure is captioned "intermolecular
forces in liquid". (Also `holing`→`holding`.)

### V18 · The Diesel advantages and disadvantages contradict each other ·EPC s86
**Printed:** Advantages — "There is no KNOCKING in the diesel engine", "Higher efficiency",
"**Less expensive**". Disadvantages — "Pollution", "Heavy", "**Initial high cost**".
**Should read:** lower **running** cost but higher **capital** cost; and diesels are **not
knock-limited in compression ratio**, rather than free of knock.
**Why.** (a) "Less expensive" and "Initial high cost" occupy the same position in each list with no
qualifier anywhere on the slide to reconcile them. (b) Diesels do exhibit combustion knock ("diesel
knock", from ignition delay); the real advantage is the absence of a knock limit on compression ratio,
which is exactly what permits ·EPC s85's higher ratio.

### EPC cosmetic flags

| ID | Slide | Defect |
|---|---|---|
| **C10** | s17 | atmospheric composition sums to 100.003 %; $\mathrm{CO_2}$ at 0.039 % is a ~2010 value |
| **C11** | s6, s13 | liquid particle motion omits translation; "Water boils at 100 ºC" lacks its pressure condition |
| **C15** | s84 | the Carnot quality-of-energy slide sits inside the Diesel block |
| **C16** | s63 | Kelvin–Planck restated without the **single-reservoir** qualifier that s51 correctly includes |
| **C17a** | s8 | open-container text, closed-flask figure |
| **C17b** | s35 | figure shows free expansion; the only bullet is about mixing |
| **C18** | various | typo cluster — "vaccum", "chaosness", "Air-Conditions", "Comprises of", the dropped "=" in "(COP  1)", "The diesel Cycle", a duplicated sentence at s31/s32, and an example-numbering clash between s64 and s78 (both "Example 6-2") |

---

## TC — Thermodynamic Cycles

Full detail in `04-thermodynamic-cycles.md`. **TC contains four equations in 24 slides and no arithmetic
at all.** All four equations are correct; every substantive flag is in the prose or a figure.

### V19 · "Entropy always increases with time" ·TC s12
**Printed:** "the second law of thermodynamics says that entropy always increases with time"
**Should read:** the entropy of an **isolated** system never decreases, $\Delta S_{\text{isolated}} \ge 0$.
**Why.** The entropy of a *system* can and routinely does decrease — that is what heat rejection does.
**The check is on TC's own slide:** in the $T$–$s$ figure one slide earlier (·TC s11), process 3→4 runs
leftward, entropy decreasing.

### V20 · Enthalpy called "the total heat content of a system" ·TC s12
**Printed:** "It is a thermodynamic state function that represents the total heat content of a system."
**Should read:** enthalpy is the state function $H = U + PV$; it is **not** heat content.
**Why.** Heat is a path-dependent transfer across a boundary, not a stored property. A throttling process
has $\Delta H = 0$ with $Q = 0$ yet a real temperature change — "heat content" cannot account for it.

### V21 · "Depends only on temperature, pressure, and composition" ·TC s12
**Printed:** as quoted, of enthalpy.
**Should read:** specific enthalpy is fixed by **two independent** intensive properties; inside the
two-phase region $T$ and $P$ are **not** independent, so quality is also needed. Total $H$ scales with mass.
**Why.** At $100\ ^\circ\mathrm{C}$ and $101.325\ \mathrm{kPa}$ water can be saturated liquid
($h \approx 419\ \mathrm{kJ/kg}$) or saturated vapour ($h \approx 2676\ \mathrm{kJ/kg}$) — same $T$,
same $P$, same composition, enthalpy differing by a factor of ~6.4.

### V22 · Energy and power units on one symbol ·TC s16
**Printed:** "$W_{net}$  Net work over one cycle, usually in kJ, Btu, **kW, or hp**…"
**Should read:** work per cycle is energy (kJ, Btu); kW and hp are **power** and belong to a rate quantity
$\dot W_{net}$, which the deck never introduces.
**Why.** Dimensional: $\mathrm{kJ} = \mathrm{J}$, $\mathrm{kW} = \mathrm{J\,s^{-1}}$. One symbol cannot
carry both. **TC's own s24 lists "Confusing energy and power" as the first common mistake.**

### V23 · One isentrope drawn vertical, the other curved ·TC s11
**Printed:** in the $T$–$s$ figure, 2→3 is a straight vertical line but **4→1 is a curve** following the
saturation boundary.
**Should read:** both vertical.
**Why.** With the numbering shown — matched to the adjacent Carnot $P$–$v$ diagram, where 2→3 and 4→1 are
the two isentropes — an isentropic process is **by definition** a vertical line on $T$–$s$. The drawn 4→1
leg changes $s$, so the figure's two "isentropes" are inconsistent with each other. **·HE s28 draws the
rectangle correctly.**

### TC cosmetic flags

| ID | Slide | Defect |
|---|---|---|
| **C19** | s2 | off-topic, untitled, image-only Third Law infographic — **shifts every subsequent slide number by one**, and contradicts `SOURCES.md`, which lists TC as having no image-only pages |
| **C21** | s12 | $H = E + PV$ uses $E$ where the course uses $U$ |
| **C22** | s11 | "Evaporization"; imperial BTU/Lb in an otherwise SI deck; two dome labels illegible at render resolution |
| **C23** | s23 | final bullet ends with a comma — a clause appears to have been dropped |
| **C24** | s9, s10 | identical figure on consecutive slides; stray blue leader arrows from the source graphic |
| **C25** | s16, s19 | $Q_L$, $Q_H$, $W_{in}$ used but never defined; $\eta_{th}$ and $\mathrm{COP}_{HP}$ absent from the glossary; **no $\mathrm{COP}_{HP}$ formula** though two slides rely on it |
| **C20** | s16 | titled "Cycle Analysis Equations" but contains no equation |
| **C26** | s3, s12, s19 | template drift — serif face on s3 alone; low/German-style closing quotes on s12; s19's title overflows two lines; inconsistent ellipsis lengths across s16–s19 |

---

## HE — Heat Engines and the Carnot Cycle

Full detail in `05-heat-engines-and-carnot.md`. **HE has no arithmetic**, but every *relation* was checked
and all are correct. **Its two Carnot diagrams are the only correct ones in the course.**

### V24 · Two states labelled "4" ·HE s2
**Printed:** in the $p$–$V$ inset of the title infographic, the lower-left **and** lower-right states are
both labelled **4**. There is no state 3.
**Should read:** 1 (upper left) → 2 (upper right) → **3** (lower right) → 4 (lower left).
**Why.** The $T$–$s$ inset directly above it, and ·HE s18, both number the states correctly. A cycle
cannot have two state 4s.

### V25 · Carnot $T$–$s$ inset drawn as a parallelogram ·HE s2
**Printed:** the $T$–$s$ inset draws both isotherms **slanted**, so the cycle is a parallelogram.
**Should read:** a **rectangle** — isotherms horizontal.
**Why.** On a $T$–$s$ diagram an isothermal process is by definition a horizontal line. **·HE s28 of the
same deck draws it correctly and states in words that it is a rectangle**, so the deck contradicts itself.

### V26 · Truncated subscripts break the temperature column ·HE s20
**Printed:** row 2→3 "Drops from $T_H$ to **$T$**"; row 4→1 "Rises from $T_C$ to **$T$**".
**Should read:** "to $T_C$" and "to $T_H$".
**Why.** A bare "$T$" is undefined, and as printed the table's temperature column does not close the
cycle. The correct values are given on ·HE s19 and in the $T$–$s$ diagram on ·HE s28, so the intent is
unambiguous. *(The **entropy** column of the same table is correct on all four rows.)*

### V27 · $T$–$s$ inset arrows do not form a traversable loop ·HE s2
**Printed:** in the title infographic's $T$–$s$ inset, the **left leg's arrowhead points downward (1→4)**
while the bottom leg points leftward (3→4).
**Should read:** the left leg must point **upward, 4→1**.
**Why.** Two arrows converge on state 4 and none leaves it; state 1 has two outgoing arrows. A cycle
must have exactly one arrow in and one out at every state, or it cannot be traversed. ·HE s18 and
·HE s28 both draw the directions correctly.

*Found by the independent verification pass, not during the original build.*

### HE cosmetic flags

| ID | Slide | Defect |
|---|---|---|
| **C27** | s25 | "Hot-reservoir temperature, $T$" — the $H$ subscript is dropped, while the row below correctly reads $T_C$ |
| **C28** | deck-wide | HE uses $Q_C$/$T_C$ where EPC uses $Q_L$/$T_L$ — internally consistent, inconsistent with `03b`. Registered in `_nomenclature.md` |

---

## Verification of the knowledge base itself

`docs/kb-format.md` step 10 requires the finished files to be re-checked against the sources, not just
written from them. That pass was run over all seven topic files: an **independent reader per file**,
comparing every citation, quotation, figure description, number and `[added]` tag back against the
rendered slides.

**What it found:**

| Outcome | Count |
|---|---|
| Headline claims **confirmed** (V8's factor-of-five, EPC's nine examples all correct, HE's entropy equations, the absence claims) | all |
| **False flag withdrawn** | 1 — **V12** |
| **New defect found and flagged** | 1 — **V27** (·HE s2) |
| Figure descriptions corrected | 5 — ·FL s21, ·FL s33, ·EPC s70, ·TC s11, ·HE s2 |
| Quotations made verbatim | 5 |
| `[added]` tagging corrected | 3 |
| Miscounts, stale cross-references and loose claims fixed | 12 |

**The two that mattered:**

1. **V12 was wrong** (see the box above) — a correct figure was reported as broken.
2. **·HE s2 had a real defect nobody had flagged** — the $T$–$s$ inset's arrows converge on state 4.
   Now V27.

Everything else was accuracy-of-description rather than physics: a $P$–$v$ process described as
crossing the vapour dome when it runs outside it (·FL s21); a three-panel figure described as two, with
the cycle direction reversed (·FL s33); a $T$–$s$ leg described as rising left when it rises right
(·TC s11); and several quotations that had been lightly re-punctuated inside blocks labelled verbatim.

**No number in any topic file was wrong.** Every recomputation in the knowledge base was independently
reproduced and agreed.

---

## Corrections to `../sources/SOURCES.md` — ✅ **applied 2026-08-18**

The manifest recorded **"TT, TC, HE | none"** under *Pages with no text layer*. Verified by enumerating
each PDF's image XObjects and per-page character counts, that was **wrong for two of the three**. The
manifest has since been corrected; this section records what was wrong and how it was found.

| Doc | SOURCES.md says | Actually |
|---|---|---|
| TT | none | ✅ correct — none |
| **TC** | none | ❌ **slide 2 is image-only** (0 characters) |
| **HE** | none | ❌ **slides 2, 16 and 18 are image-only**; s8, s9, s10, s26, s27, s28 also carry their equations as images |

Consequence for TC: because slide 2 carries no text, **every title sits one slide later** than a
text-based contents listing implies. All `·TC sN` citations in `04-thermodynamic-cycles.md` are true PDF
page numbers.

---

## Carried forward — observations awaiting verification

Read from PDF text layers during Stage 0, **before any render**. None has an ID and none may be relied
on until its document is built. Full statements in `00-index.md` § Early observations.

| # | Observation | Document | Status |
|---|---|---|---|
| 1 | Work sign convention conflicts between FL and GA2 | FL, GA2 | ✅ **RESOLVED — V6, and worse than stated: the conflict is internal to FL.** See § The FL sign-convention fault. |
| 2 | Two forms of the gas constant — $PV=nRT$ vs $PV=mRT$ | FL, GA | ✅ **RESOLVED — not a conflict.** FL s34 teaches $R = R_u/M$ and tabulates N₂ as 0.2968 kJ·kg⁻¹K⁻¹, which is GA's 0.297. Same equation, different basis. No flag. |
| 3 | "FL's worked example arithmetic recomputed and sound" | FL | ❌ **OVERTURNED — V8.** The intermediates are sound; the **final answer is wrong by a factor of five**. The Stage 0 note was read from the text layer and did not include the final line. |
| 4 | Carnot's dates printed "1769–1832"; Sadi Carnot was born **1796** | EPC | ✅ **CONFIRMED — V10.** Verified at 4× zoom on the render; the digits are unambiguous. |
| 5 | Diesel slide lists "less expensive" as an advantage and "initial high cost" as a disadvantage | EPC | ✅ **CONFIRMED — V18**, and the same slide's "no knocking" claim is wrong too. |

**Item 3 is the cautionary one.** A text-layer reading concluded the example "checks out". It does not.
Nothing recorded from a text layer should be treated as verified — that is exactly what this log is for.

**All five are now closed.** Two were confirmed as flags, one was overturned into the most serious flag
in the log, and two were resolved as non-issues.

---

## Group activities — GA1 and GA2

**One substantive flag — V28 — and it only surfaced when the questions were actually solved.**

**What was checked.** Both activities are transcribed into `exercises/` with **worked solutions**,
every one computed from scratch and tagged `[added]`. The brief supplies no answers to students, so
there is no printed result to recompute against; verification here means checking that the data is
internally coherent, that the units are as stated, and that the physics the questions assume is sound.
Solving them is what exposed V28.

### V28 · Van der Waals constant $a$ — the printed units are wrong by a factor of ten ·GA1 Part B (ii)

**Printed:** `a = 3.658 J·m³/mol²` for CO₂, and the same unit for all eight gases.

**Should read:** $a = 3.658\ \mathrm{L^2\,bar\,mol^{-2}}$, i.e. $\mathbf{0.3658\ Pa\,m^6\,mol^{-2}}$
in SI. Every printed $a$ must be **divided by 10** before substitution.

**Why.** $\mathrm{J\,m^3} = \mathrm{Pa\,m^6}$, so the printed unit asserts SI. But all eight values are
the standard tabulated figures in $\mathrm{L^2\,bar\,mol^{-2}}$, and
$1\ \mathrm{L^2\,bar\,mol^{-2}} = 0.1\ \mathrm{Pa\,m^6\,mol^{-2}}$:

| Gas | Brief prints | Standard table ($\mathrm{L^2\,bar\,mol^{-2}}$) |
|---|---|---|
| CO₂ | 3.658 | 3.640 |
| H₂O | 5.537 | 5.536 |
| N₂ | 1.370 | 1.370 |
| CH₄ | 2.283 | 2.283 |
| NH₃ | 4.225 | 4.225 |
| C₂H₆ | 5.570 | 5.562 |
| SO₂ | 6.865 | 6.803 |
| H₂ | 0.2476 | 0.2476 |

**What it costs.** Substituting the printed value literally, the cubic
$P\bar{V}^3 - (Pb + \bar{R}T)\bar{V}^2 + a\bar{V} - ab = 0$ has **exactly one real root above $b$**:
for CO₂ at 5 MPa and 320 K it is $\bar{V} = 4.43\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$ — barely above
$b$ itself — giving $Z = 0.083$. **That is a liquid-like molar volume for a gas**, and it is the answer
every group would have written down. With $a$ corrected, $\bar{V} = 4.178\times10^{-4}$ and
$\mathbf{Z = 0.785}$, which agrees with published compressibility data for CO₂ at that state.

**Three independent confirmations of the correction:**

1. **Dimensional** — the numbers match the standard $\mathrm{L^2\,bar\,mol^{-2}}$ table to within 1 %
   for all eight gases, and match nothing in SI.
2. **Physical** — the corrected $Z$ values (0.74–0.93 for seven gases) sit in the range compressibility
   charts give for those states; the literal reading gives 0.02–0.25 for all eight, which no chart
   supports.
3. **Internal to the brief** — the corrected reading is the only one that makes **H₂ come out at
   $Z = 1.096 > 1$**, which is exactly the repulsion-dominated result the brief's own discussion
   question sets up. Read literally, H₂ gives $Z = 0.25$ and the discussion question has no answer.

**Note what is *not* wrong.** The brief converts $b$ correctly and spells that conversion out inline
every time ($0.04286\ \mathrm{L\,mol^{-1}} = 0.04286\times10^{-3}\ \mathrm{m^3\,mol^{-1}}$), and the
pressure conversion likewise. Only $a$'s unit label is wrong. **Class: substantive** — it changes every
Part (ii) answer by roughly a factor of three in $Z$.

**Where it is recorded for students:** a flag box in
`exercises/ga1-topic1-part1-equations-of-state.md` § Part B (ii), immediately above the data table, and
again at the head of § Solutions.

| Check | Result |
|---|---|
| **GA1 Van der Waals constant $a$ — printed units** | ❌ **V28 — wrong by a factor of ten.** See above. |
| GA1 specific gas constants ($R$) against $\bar{R}/M$ | ✅ all 8 consistent; N₂ at 0.297 matches FL s34's tabulated 0.2968 |
| GA1 Van der Waals constants $a$, $b$ against standard tables | ✅ all 8 gases plausible; magnitudes and ordering correct ($a$ largest for SO₂ and NH₃, smallest for H₂) |
| GA1 unit handling, $b$ and $P$ | ✅ **the brief warns of its own two traps inline** — $b$ in L·mol⁻¹ needing $\times 10^{-3}$, and $P$ in kPa needing $\times 10^{3}$. Not errors. Only $a$ (V28) is wrong. |
| GA2 specific heats $c_v$ against standard values | ✅ all 9 consistent on a **mass** basis; He 3.116, H₂ 10.18, Ar 0.312 are the correct monatomic/diatomic values |
| GA2 $c_v$ against GA1's $R$ via Mayer's relation | ✅ spot-checked — N₂ (0.743 + 0.297 = 1.040) and CO₂ (0.657 + 0.189 = 0.846) both give correct $c_p$ |
| GA2 G9's stray $R = 0.189$ in Task 2 | ⚠ **unused, not wrong.** $W = P\,\Delta V$ needs no gas constant. The value is correct for propane ($M = 44.1$) and coincides with GA1's CO₂ figure ($M = 44.01$) — a coincidence of molar masses, not a copy error. |

**Three hazards were recorded in the exercise files** — not as flags, because they are hazards in
*applying* the questions rather than defects in them:

1. **GA2 states the engineering sign convention** ($\Delta U = Q - W$, $W$ positive done *by* the
   system) — which is FL's *second* convention. Tasks phrased *"receives electrical energy (work
   input)"* therefore need a negative $W$. See § The FL sign-convention fault.
2. **GA2 Task 1's nine scenarios are not the same shape.** Three give heat + boundary work; two give
   electrical work in + heat out; **four give two heat terms and no work at all**. Treating a cooling
   system's heat removal as $W$ is a sign-convention error the wording invites. **G9's brief states
   $W = 0$ outright**, which independently confirms the reading for the other three.
3. **GA2's specific heats are per kg; FL s28 states the relations per mol** via $\gamma$. The basis
   must be converted.

**GA2's Group 9 file was authored separately from the other eight.** Every group's Part B stem was
diffed against every other's, not sampled. Groups 1–8 are identical apart from the substituted gas
name; **G9 has a completely different Task 1** (three unrelated sub-questions, including an IGBT
junction-temperature calculation), an added polytropic clause in Task 2, a re-framed Task 3 part 3,
and the set's only numerical Task 4. It is transcribed in full in
`exercises/ga2-topic1-part2-first-law.md` § Group 9 so no G9 member works from the wrong stem.

**A numeric cross-check was run in both directions.** Every value in both exercise files was matched
back against the source `.docx` text programmatically — GA1's 8 groups (R, P, V, T, P₂, a, b, M) and
GA2's 9 (all Task 1–4 quantities). **All present, none altered.** That check is what surfaced the G9
discrepancy: a stray `180 kJ` in G9's Task 1 that the common stem could not account for.

**An independent adversarial review was run over both exercise files** after they were written, with
the source text and every cross-reference target available to it. Twelve findings were raised; **eleven
were confirmed and fixed**, and **one was rejected** — a claimed broken-link base in
`thermodynamics/README.md`, which assumed the file sat at the repository root rather than in the
subject folder. A scripted link check resolves all of its links. The eleven fixes were: a property
table mis-attributed to TC instead of FL s34; "solve all four tasks" where the brief says three;
a Mayer cross-check that matched group numbers instead of gases; "byte-identical across all nine" when
G9's Part A carries two rewordings; a Rankine-scale gap claimed to be in the gap map when it was not
(now added); a Rankine citation to HE s8–s10 instead of s26; a Kelvin-shift relation attributed to
§1.7 instead of §1.6; a cyclic-work pointer to §3b.3 instead of §3b.4; a reflection block quoting G9's
wording as the common one; and two overstatements about how uniform the briefs are. **Rejecting a
finding is as much the job as accepting one** — the same standard that withdrew V12.

### GA1's facilitator answer key was read but is not reproduced — audited

The master brief's final section is headed *"FACILITATOR / LECTURER NOTES (Not distributed to
students)"*. It is marked not for distribution and this repository is public, so **nothing from it is
quoted or paraphrased**, and the published solutions were computed independently from the question
data alone. Audited by script rather than asserted:

| Test | Result |
|---|---|
| Longest shared word sequence between the key and the published GA1 file | **zero shared 6-word sequences** — no prose overlap at all |
| The key's eight indicative $Z$ values | **none appears** in the published file |
| The key's seven indicative Van der Waals roots | **none appears** |

**What does coincide, unavoidably:** values that any correct solution must produce — $341.15$ K as the
Kelvin equivalent of $68\ ^\circ\mathrm{C}$, $95.04$ as $0.297 \times 320$, $154.4\ ^\circ\mathrm{F}$,
and so on. Two people converting the same temperature get the same number; that is arithmetic
agreeing with itself, not copying. **The distinguishing test is Part (ii)**, where the answer depends
on a judgement call rather than a formula — and there the published values differ from the key's in
**six cases of eight**, because the key gives approximate iterative estimates while the solutions here
give exact roots of the cubic.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
