---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
file_role: verification-log
source: "Built incrementally, one lecture document per stage. Currently covers TT only."
coverage: "TT (Temperature and Thermometry), 17 pp., fully verified. FL, EPC, TC, HE pending."
substantive_flags: 4
cosmetic_flags: 2
total_flags: 6
tags: [verification, errata, corrections]
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

**Method** (per `../../docs/kb-format.md` § Verification): every page read from a **rendered image**,
never the PDF text layer; every numerical claim recomputed independently; every equation checked for
dimensional consistency, algebraic consistency, symbol slips, mislabelled results and self-reference.

**Page citations are the document's own printed footer numbers.** TT's footer starts at 2 on the title
page, so a PDF viewer shows one less: `p13` = PDF page 12.

---

## Summary

| ID | Doc | Page | Class | Defect |
|---|---|---|---|---|
| **V1** | TT | p13 | substantive | absolute zero printed as $273.15\ ^\circ\mathrm{C}$ — minus sign absent |
| **V2** | TT | p13 | substantive | Kelvin zero point printed as $273.15\ ^\circ\mathrm{C}$ — same missing minus |
| **V3** | TT | p17 | substantive | Example 1(b) cites "Equation 2a"; working correctly uses Equation 1 |
| **V4** | TT | p17 | substantive | $\Delta T = 7\ \mathrm{K}$ — rounded before subtracting; should be $6.7\ \mathrm{K}$ |
| **C1** | TT | p14 | cosmetic | kelvin defined via triple point — pre-2019 SI definition, superseded |
| **C2** | TT | p12–13 | cosmetic | text says "curves" (plural); Figure 5 draws one line and no extrapolation |

**TT: 17 pages, 4 substantive + 2 cosmetic.** Equations 1, 2a, 2b and 3 are all sound — every
substantive flag concerns the prose or arithmetic *around* them.

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
$100$. **One** straight orange line joins a black dot at $T=0$ to a black dot at $T=100$. Two green
callouts label those dots ("Pressure at the freezing point of water", "Pressure at the boiling point of
water") — **the green lines are callout leaders, not plotted data**. The horizontal axis begins at $0$,
so no part of the negative-temperature extrapolation is drawn.

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

## Carried forward — observations awaiting verification

Read from PDF text layers during Stage 0, **before any render**. None has an ID and none may be relied
on until its document is built. Full statements in `00-index.md` § Early observations.

| # | Observation | Document | Resolved at |
|---|---|---|---|
| 1 | **Work sign convention conflicts between FL and GA2** — $Q = W + \Delta U$ vs $\Delta U = Q - W$ | FL, GA2 | Stage 1b / 1c |
| 2 | Two forms of the gas constant — $PV=nRT$ with $\bar R$ vs $PV=mRT$ with specific $R$ | FL, GA | Stage 1b / 1c |
| 3 | FL's worked example arithmetic recomputed and sound; only the convention is inconsistent between slides | FL | Stage 1b |
| 4 | Carnot's dates printed "1769–1832"; Sadi Carnot was born **1796** | EPC | Stage 2 |
| 5 | Diesel slide lists "less expensive" as an advantage and "initial high cost" as a disadvantage | EPC | Stage 2 |

Item 1 is the highest-value item found in the subject so far and is pre-registered in
`_nomenclature.md` clash 1.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
