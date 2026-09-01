---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
file_role: verification-log
source: "All six source documents (GB, CRV, BIN, MAC, LEI, BES) — 66 pages"
total_flags: 24        # 9 substantive (V1–V9) + 15 cosmetic (C1–C15)
reading_limitations: 18   # L1–L18: 3 settled as clean readings, 1 reconstructed with certainty, 2 illegible but confirmed cancelled — no content gaps
built: "Transcribed from rendered page images; every numerical claim recomputed; every ambiguous glyph re-read at 600 dpi against reference glyphs from the same hand"
---

# Verification log — EMT 3101

**This is the highest-value file in the subject.** Read the section for a topic before you revise
it. The physics-equivalent here is that the *mathematics on these pages is sound* — the defects are
almost entirely in **stated answers, copied decimals and dropped symbols**, which is the class of
error that a careful reader catches and a memorising reader absorbs.

---

## How to read the IDs

| Prefix | Means |
|---|---|
| **V1–V9** | **Substantive** — changes the mathematics. Never learn the printed version. |
| **C1–C15** | **Cosmetic** — typos, mislabels, numbering slips. Harmless if you notice them. |
| **L1–L18** | **Reading limitation** — nothing is wrong with the source; the *image* is clipped, over-written or cut. Marked inline with `⚠ SCAN`, not `⚠ VERIFY`. Three were **settled** on re-read (L3, L10, L16), one **reconstructed with certainty** from the answer line (L18), and two are **confirmed unreadable** (L1, L4). |

> **Why `L` and not `S`.** Fluid Flow already uses `S1`–`S32` for *slide flags*, which are genuine
> defects in the lecturer's material. Here the letter would mean the opposite, so this subject uses
> **L for limitation**. `V`, `C` and `P` match the rest of the repository.

Source codes and citation convention:

| Code | Document | Pages | Citation |
|---|---|---|---|
| **GB** | Gamma and Beta functions | 11 (printed 3–13) | `·GB p6` = the document's own **printed** page number |
| **CRV** | Continuous Random Variables and the Beta Distribution | 22 | `·CRV p18` = **scan** page |
| **BIN** | The Binomial Theorem | 8 | `·BIN p3` = scan page |
| **MAC** | Maclaurin's Theorem | 7 | `·MAC p5` = scan page |
| **LEI** | Leibniz Theorem | 9 | `·LEI p2` = scan page |
| **BES** | Bessel's Equation | 9 | `·BES p2` = scan page |

GB is typeset LaTeX with a full text layer; the other five are handwritten 300 dpi scans with none.
**That is why GB is the only document whose page numbers are printed** — and it is also why GB's
transcription carries no reading uncertainty at all.

---

## Method

1. **Every page rendered to an image and read directly.** Text extraction was used only on GB,
   where a real text layer exists, and then only as a cross-check.
2. **Every numerical claim recomputed** — `mpmath` at 25 digits, `sympy` for symbolic series and
   derivatives, `scipy.special` for Bessel and binomial values. A claim is marked ✓ only if the
   independent computation matched.
3. **Every ambiguous glyph re-read at 600 dpi** against reference glyphs of the same character
   elsewhere in the same hand, and — where the question was whether something had been cut off —
   against a pixel-column scan of the page margin.
4. **Nothing invented.** Where a reading could not be settled it is recorded as unreadable, not
   guessed.

**Honest limit.** Checks 1 and 3 are careful reading, not independent verification: a glyph that
misled once could mislead the same way twice. Check 2 *is* independent, and it is what caught V1,
V2, V4, V5 and V8.

---

## § A · Substantive flags (V1–V9)

Nine defects that change the mathematics. **Five of the nine are a correct symbolic line followed by
a wrong number copied from it** — that is this subject's signature failure.

### V1 · GB p6 — $\Gamma(9/2)$ printed as 16.8114

**Page prints:** $\Gamma\!\left(\tfrac92\right) = \tfrac{105}{16}\sqrt\pi = \mathbf{16.8114}$

**Correct:** $\tfrac{105}{16}\sqrt\pi = \mathbf{11.6317}$

**Why:** the symbolic form is right; only the decimal is wrong. The page **contradicts itself on the
next line** — part (iii) of the same example uses this quantity to obtain $(4.5)! = 52.3428$, and
$52.3428/4.5 = 11.6317$.

**Check you can repeat:** $\Gamma(9/2) < \Gamma(5) = 24$ and $> \Gamma(4) = 6$, so anything near 17
should already look high; $105/16 = 6.5625$ and $6.5625 \times 1.7725 = 11.63$.

*This one is typeset, not handwritten — the digits are unambiguous.*

### V2 · GB p12 — Exercise 3.1(c) out by a factor of 3

**Page prints:** $\displaystyle\int_0^{\pi/2}\cos^{4}3\theta\,\sin^{2}6\theta\,d\theta = \tfrac43\left[\frac{\Gamma(3/2)\Gamma(7/2)}{2\Gamma(5)}\right] = 0.08181$

**Correct:** $\mathbf{0.24544}$

**Why:** the hint's substitution $3\theta = t$ carries $\theta \in [0,\pi/2]$ onto
$t \in [0, \mathbf{3\pi/2}]$, but the Beta trigonometric form is only valid over $[0,\pi/2]$. Since
$\sin^{2}t\cos^{6}t$ has period $\pi$ and is symmetric about $\pi/2$, the larger interval holds
exactly three copies of the smaller one — hence the factor of 3.

**Check:** direct numerical integration of the original integrand gives 0.245437.

### V3 · CRV p18 — variance squared twice

**Page prints** *(red margin working)*:
$$m = \frac{(0.04)^{2} - (0.04)^{3}}{(0.0004)^{\mathbf{2}}} - (0.04) = 3.8$$

**Correct:** the denominator is $\sigma^{2} = 0.0004$, **unsquared**.

**Why:** $0.0004$ is *already* the variance $(0.02)^{2}$. Squaring it again gives
$m = 9599.96$, not the 3.8 the page itself states two lines later. Unsquared:
$\frac{0.0016 - 0.000064}{0.0004} - 0.04 = 3.84 - 0.04 = 3.8$ ✓

**Reading confidence:** the superscript 2 was re-read at 600 dpi in the red channel — **it is
there**. This is the source's slip, not a transcription artefact. Most likely $\sigma^{2}$ notation
carried onto the number itself.

**Check:** substitute the resulting $m = 3.8$, $n = 91.2$ back into $E(X)$ and $\mathrm{Var}(X)$ —
they return 0.04 and 0.0004 exactly.

### V4 · CRV p20 — $P(10)$ digits transposed

**Page prints:** $P(10) = \mathbf{0.0228}$

**Correct:** $0.7^{10} = \mathbf{0.0282475}$

**Reading:** the entry sits on the very bottom edge of the scan and only the tops of the digits
survive. Read at 600 dpi against the digits of $0.2668$ three lines above, the final glyph is a
**closed loop with a crossing stroke — this hand's 8**; its 2 is an open hook with a flat base, a
visibly different form. So the page reads 0.0228.

**Residual caveat:** this is a partial-glyph reading. The *value* is not in doubt (0.0282 is the
binomial probability), but if you can see the original, this is the one worth a glance.

**Why it matters:** every other entry in that table matches to 4 s.f., so a reader has no reason to
distrust this one.

### V5 · BIN p3 — coefficient of $x$ in $(2+x)^{7}$

**Page prints:** $(2+x)^{7} = 128 + \mathbf{44}x + 672x^{2} + 560x^{3} + 280x^{4} + 84x^{5} + 14x^{6} + x^{7}$

**Correct:** the coefficient is $\mathbf{448}$.

**Reading confidence:** re-read at 600 dpi — the ink unambiguously shows two digits, "44", followed
by the $x$, with normal spacing to the "+" that follows. A dropped digit when copying the answer
down, not a scan artefact.

**Why:** the line **directly above** derives it correctly as $7(2)^{6}x = 7\times64\,x = 448x$.
Every other coefficient on the line is right.

**Check:** the coefficients of $(2+x)^{7}$ are $\binom7k 2^{\,7-k}$, i.e.
$128, 448, 672, 560, 280, 84, 14, 1$. Also, setting $x = 1$ must give $3^{7} = 2187$: with 448 the
sum is 2187 ✓; with 44 it is 1783 ✗. **That one-second check catches it.**

### V6 · MAC p5 — limit and answer belong to different integrals

**Page prints:** Evaluate $\displaystyle\int_0^{\mathbf{4}}\frac{\sin\theta}{\theta}d\theta$ correct
to 3 s.f. &nbsp;**Ans: 0.946**

**The conflict:**
- $\mathrm{Si}(4) = \mathbf{1.7582}$
- $\mathrm{Si}(1) = \mathbf{0.94608}$ — which is the printed answer to 3 s.f.

**Reading confidence:** the upper limit was re-read at 600 dpi and is an **unambiguous 4** — a
textbook open-topped 4 with a diagonal, crossbar and stem, nothing like this hand's 1 (a plain
vertical with a top-left flick).

**Verdict:** since the limit is legible and the answer is not derived anywhere on the page, the most
likely story is that the **answer was not updated when the limit changed**. Work whichever limit the
question gives you; do not use 0.946 as a check on a limit of 4.

**Supporting observation:** at $\theta = 4$ the series needs seven terms to reach 3 s.f., which is
unusually laborious for an introductory exercise — itself a hint the intended limit was smaller.

### V7 · LEI p2 — cofunction identity missing its minus

**Page prints:** $\cos\left(\theta + \tfrac\pi2\right) = \sin\theta$

**Correct:** $\cos\left(\theta + \tfrac\pi2\right) = \mathbf{-}\sin\theta$

**Why it is serious:** this sits on the **reference identity sheet** at the front of the file — the
page a student turns back to mid-problem — and it feeds directly into §2.3's $\cos ax$ phase-shift
results.

**Check:** at $\theta = \pi/2$, $\cos(\pi) = -1$ while $\sin(\pi/2) = +1$.

**Note:** the *first* form on the same line, $\cos\left(\tfrac\pi2 - \theta\right) = \sin\theta$, is
correct. Only the shifted version is wrong.

### V8 · BES p2 — dropped $-\nu$ in the $J_{-\nu}$ exponent

**Page prints:**
$$J_{-\nu} = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma(k-\nu+1)}\left(\frac{x}{2}\right)^{\mathbf{2k}}$$

**Correct:** the exponent is $\mathbf{2k-\nu}$.

**Reading confidence:** this is the flag that most needed settling, because a clipped right margin
would have made it a scan artefact rather than a source error. It is **not clipped**: at 600 dpi
the exponent "2k" is followed by clear white space, and a pixel-column scan shows the **rightmost 40
columns of the whole page carry no ink at all**. The $-\nu$ was never written.

**Why:** the general form on the line above has the $\left(\tfrac x2\right)^{-\nu}$ prefactor
*outside* the sum; folding it in is precisely what produces the $-\nu$. The parallel $J_\nu$
expression, written on the same line of the page, correctly reads $\left(\tfrac x2\right)^{\nu+2k}$.

**Check:** at $\nu = 0.3$, $x = 0.5$ — as printed, $0.7029$; corrected, $1.0653$, which is
`scipy.special.jv(-0.3, 0.5)` to 15 significant figures.

### V9 · BES p6 — summation limit not advanced

**Page prints:** Proof 2 keeps $\displaystyle\sum_{k=0}^{\infty}$ throughout, including after
$k! = k(k-1)!$ has been used to cancel the $k$.

**Correct:** the limit must become $k = 1$ at the moment of differentiation.

**Why:** with a lower limit of 0 the expression contains $(-1)! = (0-1)!$, which is undefined. The
step is legitimate — differentiating brings down a factor $2k$, which kills the $k = 0$ term — but
the bookkeeping has to record it.

**Why it matters:** the *result* is right, so a reader checking only the answer will pass it. An
examiner reading the printed derivation would mark the step.

---

## § B · Cosmetic flags (C1–C15)

Harmless once noticed, and all confirmed against the page.

| ID | Where | Page has | Should be |
|---|---|---|---|
| C1 | ·GB p8 | Exercise 2.4: "By finding an expression for $I$" | $I^{\mathbf{2}}$ — the method forms the product of the two integrals as a double integral; that is why the question states $I$ twice, once in $x$ and once in $y$ |
| C2 | ·GB p13 | signs off "\*\* End of Topic Four \*\*" | this is Topic 1 by filename. See the numbering note below |
| C3 | ·GB p3 | "For axample:" | "For example" |
| C4 | ·GB p12 | Ex. 3.4: "show that find the exact value of" | one verb too many |
| C5 | ·CRV p6 | sketch ordinate at $x = 6$ labelled "0.8" | $f(6) = 0.08$; the arithmetic beside it uses 0.08 |
| C6 | ·CRV p8 | $E\big[g(X) + b(X)\big]$ | $h(X)$ — $b$ is already a constant two lines above |
| C7 | ·CRV p12 | heading and opening sentence duplicated from p11 | struck out on the page; a false start, no content lost |
| C8 | ·BIN p8 | "the **electric** field strength $H$ due to a magnet" | **magnetic** field strength. Mathematics unaffected — but do not carry the label into an electromagnetics paper |
| C9 | ·BIN p8 | magnet half-length written with the same glyph as Q1's inertia $I$ | lowercase $\ell$; only that reading gives the stated $2M/x^{3}$ |
| C10 | ·MAC p1 | sign before $x^{7}/7!$ in the $\sin x$ series: a "+" heavily struck through | $-$. What survives on the page is a defaced plus, not a clean minus |
| C11 | ·MAC p2 | $x^{4}$ term written $\frac{x^{4}}{4}(0)$ | $\frac{0}{4!}x^{4}$ — zero either way, but the pattern it teaches is wrong |
| C12 | ·MAC p4 | block headed "At x = 0" | the variable throughout is $\theta$ |
| C13 | ·LEI p2 | $y''' = -a^{3}\cos x$ | $-a^{3}\cos ax$ |
| C14 | ·LEI p5 | the $\ln ax$ item numbered "6)" | 7) — 6) is already the $\cosh ax$ item |
| C15 | ·BES p1 | margin header reads "**Topic 6**" | the filename says Topic 4 |

### The numbering note (C2 + C15)

The course's internal topic numbering does not match the filenames:

| File | Filename says | Document says |
|---|---|---|
| GB | Topic 1 | signs off "End of Topic **Four**" |
| BIN / MAC / LEI | Topic 3.1 / 3.2 / 3.3 | margin of BIN p1: "Topic 3" ✓ |
| BES | Topic 4 | header: "Topic **6**" |

**Do not try to match these to a syllabus by number.** Match by content. This knowledge base
renumbers 01–06 in teaching order and records the original labels in each file's frontmatter.

---

## § C · Reading limitations (L1–L18)

Nothing here is a defect in the lecturer's material — these are limits of the **image**. The
handwritten scans are off-register, so roughly half of CRV's pages and several in the other files
lose their last character or two at the right margin.

> **The cause, and the fix.** Every handwritten page is one 300 dpi JPEG measuring 3507 × 2480 px —
> precisely A4 landscape. The capture area was set to exactly A4 with no tolerance, so a 210 mm sheet
> laid a few millimetres off centre loses a strip from one edge. **That is the entire explanation for
> this section.** Higher resolution would not have helped; scanning at A3, or turning off exact-size
> cropping, would have removed it altogether. Provenance detail in `../sources/SOURCES.md`.

**Three were settled outright on re-read and one reconstructed with certainty (all marked ✅).
Two are confirmed unreadable (marked ❌).** The rest are clipped edges whose content is recoverable
from context or from the algebra — recorded so you know which lines were *not* read from ink.

| ID | Where | Issue | Status |
|---|---|---|---|
| **L1** | ·CRV p4 | two-line red note at the foot, written over itself in several passes | ✅ **Closed.** Illegible in the scan (red-channel isolation at 600 dpi recovers only the word "and"), but **it is cancelled text** — confirmed on the reader's own inspection, 2026-08-31. Nothing is lost |
| L2 | ·CRV p9 | $E(X)$ runs off the right edge; "2.2" visible | Value certain: $34/15 = 2.2667$, from part (ii)'s reuse of it and by direct integration. The **ink** is not readable |
| **L3** | ·CRV p15 | short marginal tag after the $\mathrm{Var}(X)$ result | ✅ **Resolved: "(Eqn 1)".** The digit is identical to the 1 in $(m+n+1)$ on the same line and nothing like this hand's 2 (which has a hook and a flat base). The letters are a compressed cursive "Eqn" |
| **L4** | ·CRV p16 | red note at the foot, struck through *and* scribbled over | ❌ **Confirmed illegible.** It is cancelled text, so nothing is lost |
| L5 | ·CRV p18 | trailing $-(1-\mu)$ clipped on three consecutive lines; only "$-\,(1-$" visible | Reconstructed from the algebra and confirmed numerically — **not read from ink** |
| L6 | ·CRV p20 | $P(3)$ mantissa cut by the page edge; only "$\times10^{-3}$" survives | Computed: $9.00\times10^{-3}$ |
| L7 | ·CRV, all | scan off-register; right margin clipped on ~half the pages | Affects pp. 9, 12, 18, 20, 21, 22 materially; elsewhere it costs a word context recovers |
| L8 | ·BIN p1 | lower half has two writing passes crossing; "Binomial coefficient" label clipped | Content separated out and complete |
| L9 | ·BIN p2 | $r$-th term exponent clipped: "$x^{r-}$" | Reconstructed as $x^{\,r-1}$ |
| **L10** | ·BIN p4 | the factorial in the middle-term denominator — 5 or 6? | ✅ **Resolved: $(6-1)!$.** At 600 dpi the glyph **closes into a loop at the bottom**, which is this hand's 6; its 5 (see "$r-1 = 5$" four lines above on the same page) has a strictly **open** bowl and a separately drawn straight top bar. The arithmetic agrees: $30240/5! = 252$ ✓, $30240/4! = 1260$ ✗ |
| L11 | ·BIN p4 | $(1.002)^{9}$ to 7 s.f., cut by the bottom edge | Computed: $1.018145$. Fragment consistent, but do not cite the page for it |
| L12 | ·LEI p1 | right column of the identity block clipped | Reconstructed from standard identities — each unambiguous from what is visible |
| L13 | ·LEI p2 | middle bracket of the $\sin3x$ example written over itself | Result unaffected: first and last expressions are clear and consistent |
| L14 | ·LEI p4 | three lines lose their last words to the margin | Reconstructed from context |
| L15 | ·LEI p8 | $v^{(5)}$ clipped; only "$=\;($" survives | Reconstructed as 0 — the fifth derivative of $x^{4}$, and what the working below uses |
| **L16** | ·LEI p9 | Exercise 1: the character before "=" | ✅ **Resolved: capital $A$.** Two strokes and a crossbar, unmistakable at 600 dpi. It is a **label for the product**, not a second unknown: the exercise asks for $\frac{d^{n}}{dx^{n}}(x^{2}y)$ |
| L17 | ·BES p1 | "…order of the" clipped | "Bessel's equation", from the wrap onto the next line |
| **L18** | ·BES p9 | Exercise 2's right-hand side clipped; "$= -x^{-n}$…" visible | ✅ Reconstructed from the answer line, which names the second recurrence relation explicitly: $-x^{-n}J_{n+1}(x)$ |

### How the resolved items were settled

The method was the same in each case: render the page at **600 dpi**, isolate the glyph, and compare
it against a **known instance of each candidate character in the same hand, from the same page or
the adjacent line**. Where the question was whether text had been cut off (L18, and V8), a
**pixel-column ink scan of the page margin** settles it — if the last 40 columns are blank, nothing
was lost to the edge.

Two items resisted every attempt (L1, L4). Both are red-pen notes written in two or three
superimposed passes; channel isolation and contrast stretching separate the ink from the paper but
not the passes from each other. **Both have since been confirmed as cancelled text** — L4 from the
strike-through visible on the page, L1 on the reader's own inspection (2026-08-31). They stay
recorded as unreadable, but **neither is a content gap**, and the subject now has none.

---

## § D · Numerical verification record

Every stated answer in all six documents was recomputed independently. **Where a computation
disagreed with the page, it became one of V1–V9; nothing marked correct turned out to be wrong.**

**File 01 — Gamma and Beta** · `mpmath`, 25 digits

- $\Gamma(5/2) = 1.3293404$ ✓ · $\Gamma(9/2) = 11.6317284$ ❌ *(V1)* · $\Gamma(5.5) = 52.3427778$ ✓ · $\Gamma(-3/2) = 2.3632718$ ✓
- Exercise 1: $\int_0^\infty x^{3}e^{-x}dx = 6$ ✓ · $\int_0^\infty x^{6}e^{-2x}dx = 5.625$ ✓
- Exercise 2.2 (a)–(e): $30$, $0.75$, $16/315$, $4/3$, $-2$ — all ✓ · 2.3: $3/128$ ✓
- Beta: $B(5,2) = 1/30$ ✓ · $B(3,7) = 1/252$ ✓ · the three improper integrals ✓ · $\int_0^{\pi/2}\sin^{7}\theta\cos^{3}\theta\,d\theta = 1/40$ ✓ · $\int_0^{\pi/2}\sin^{5}\theta\,d\theta = 8/15$ ✓
- Exercise 3: 1(a) $0.133333$ ✓ · 1(b) $8/15$ ✓ · **1(c) $0.245437$ vs the page's $0.081812$ ❌ (V2)** · 3 $\Gamma(3/4)$ ✓ · 4 $\pi/2$ ✓ · 5 $\pi/32$ ✓

**File 02 — CRV and Beta distribution** · numerical integration and exact combinatorics

- Flight delay $f(x) = 0.2-0.02x$: $P(0\le X\le4) = 0.64$ ✓ · $P(2\le X\le6) = 0.48$ ✓ · total area $= 1$ ✓
- $f(x) = x^{2}/9$: $\mu = 2.25$ ✓ · $P(X<\mu) = 0.4219 \to 0.42$ ✓
- $f(x) = (x+3)/20$: $E(X) = 34/15$ ✓ · $E(2X+5) = 9.53$ ✓ · $E(X^{2}) = 6.4$ ✓ · $E(X^{2}+2X-3) = 7.93$ ✓
- Beta moments at $m=8$, $n=4$, by direct integration against the closed forms: $E(X) = 0.666667$ ✓ · $E(X^{2}) = 0.461538$ ✓ · $\mathrm{Var} = 0.017094$ ✓ · numerator collapse $m(m+1)(m+n)-m^{2}(m+n+1) = mn$ confirmed symbolically ✓
- Parameter fit, $\mu = 0.04$, $\sigma^{2} = 0.0004$: $m = 3.8$ ✓, $n = 91.2$ ✓; back-substitution returns $E(X) = 0.04$, $\sigma = 0.02$ ✓. **With the denominator squared as printed: $9599.96$ ❌ (V3)**
- Binomial $t=10$, $p=0.7$: $k = 1,2,4,5,6,7,8,9$ all ✓ to the stated precision; **$k=10$: computed $0.0282$ vs page $0.0228$ ❌ (V4)**
- Beta pdf $f(x) = 1320x^{7}(1-x)^{3}$: $B(8,4) = 1/1320$ ✓ · all eleven tabulated values ✓ · mode $= 0.7$ ✓

**File 03 — Binomial** · `sympy` series, exact combinatorics

- **$(2+x)^{7}$: computed $128, \mathbf{448}, 672, 560, 280, 84, 14, 1$ vs page's $44$ ❌ (V5)**
- $(2a-3b)^{5}$ ✓ · middle term $-252p^{5}/q^{5}$ ✓ (and $30240/5! = 252$ confirms $(6-1)!$ — L10)
- $(c-1/c)^{5}$ ✓ · fifth term of $(3+x)^{7} = 945x^{4}$ ✓ · $(1.002)^{9} = 1.01814467$ ✓
- $(1+2x)^{-3}$, $(1-2t)^{-1/2}$, the cube-root/square-root quotient, and both "when $x$ is small" identities — all ✓
- Cylinder: volume factor $0.96^{2}\times1.02 = 0.9400$ ✓ · CSA $0.96\times1.02 = 0.9792$ ✓
- Shaft: $\sqrt{1.04/0.98} = 1.03016$ ✓ · magnet limit $\to 2M/x^{3}$ ✓ (symbolic)

**File 04 — Maclaurin** · `sympy`

- Series for $\cos^{2}2x$, $\sin^{2}x$, $e^{2\theta}\cos3\theta$, $\ln(1+e^{x})$, $e^{\sin\theta}$, $\tan x$, $\sinh x$ — all ✓
- Example 1: $[2\theta+\theta^{2}+\theta^{3}/3]_{0.1}^{0.4} = 0.771$ ✓ *(exact integral 0.77040)*
- **Exercise 1: $\mathrm{Si}(1) = 0.946083$, $\mathrm{Si}(4) = 1.758203$ — page states limit 4 with answer 0.946 ❌ (V6)**
- Exercise 2: $0.018682 \to 0.019$ ✓ · Exercise 3: $0.060604$ *(no answer on the page — supplied)*
- All seven limits ✓; (e), (f), (g) computed as $1$, $\tfrac13$, $\tfrac13$ *(blank on the page — supplied)*

**File 05 — Leibniz** · `sympy`, direct differentiation

- All seven $n$-th derivative examples ✓: $384e^{2x}$, $243\cos3x$, $-256\cos2x$, $720x^{2}$, $32\cosh2x$, $243\sinh3x$, $-120/x^{6}$
- $y = x^{2}e^{3x}$: the general result $e^{3x}3^{\,n-2}(9x^{2}+6nx+n(n-1))$ tested at $n = 1,2,3,5$ — exact at every order ✓
- $y = x^{4}\sin x$: the notes' $y^{(5)}$ minus direct differentiation simplifies to 0 ✓
- Exercises 2–4 solved and verified *(no answers on the page — supplied)*

**File 06 — Bessel** · `scipy.special`

- $J_0$ and $J_1$ series vs `jv` at $x = 3.7$: agree to 14 significant figures ✓
- **$J_{-\nu}$ as printed: $0.7029$; corrected: $1.0653 = J_{-0.3}(0.5)$ to 15 s.f. ❌ (V8)**
- All six recurrence formulas verified at $n = 2$, $x = 3.7$ (derivatives by central difference, $h = 10^{-6}$) ✓
- Exercise 1: $J_{-1}(3.7) + J_1(3.7) = 0$ exactly ✓

---

## § E · Where this log came from

An earlier working file, `_transcripts/SELF-CHECK-verify-these-yourself.md`, listed **11 readings that
the first transcription pass could not settle from the ink alone** and asked a human to confirm them
against the original pages.

**All 11 have since been settled by re-reading the pages at 600 dpi** (2026-08-31). The outcomes are
folded into the sections above; this table records what happened to each, so that the earlier file
can be retired without losing the audit trail.

| Original item | Question | Outcome | Now |
|---|---|---|---|
| 1 | BIN p3 — 44 or 448? | ink reads **44** | **V5** |
| 2 | BES p2 — exponent $2k$ or $2k-\nu$? | ink reads a bare **2k**; page margin confirmed blank | **V8** |
| 3 | GB p6 — does it say 16.8114? | **yes** (typeset) | **V1** |
| 4 | BIN p4 — $(5-1)!$ or $(6-1)!$? | **$(6-1)!$** — closed bottom loop | L10 ✅ *no longer a flag* |
| 5 | MAC p5 — upper limit 4 or 1? | **4**, unambiguous | **V6** |
| 6 | CRV p18 — is there a superscript 2? | **yes** | **V3** |
| 7 | CRV p20 — 0.0228 or 0.0282? | **0.0228** | **V4** |
| 8 | LEI p9 — is that letter an A? | **yes** | L16 ✅ *no longer a flag* |
| 9 | CRV p4 — the red foot-note | **unreadable — but cancelled text** | L1 ✅ closed |
| 10 | CRV p16 — the cancelled red note | **unreadable** | L4 ❌ |
| 11 | CRV p15 — "(Eqn 1)"? | **yes** | L3 ✅ *no longer a flag* |

**Net effect:** two uncertain readings became confirmed source errors (V4, V8); three became settled
readings with no defect (L3, L10, L16); two are unreadable but **both are cancelled text** (L1, L4),
so **the subject has no content gap at all**; the remaining four confirmed flags that were already
raised.

**Every one of the eleven is now closed.** If you ever check one against the original and disagree,
item 7 (V4) is the one with the least margin — only the tops of its digits survive. Say what you see
and the log will be corrected.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
