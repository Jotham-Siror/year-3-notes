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

## § F · Exam papers

Defects in the **assessment papers themselves**, as distinct from the lecture documents. Entry IDs are
`P1`, `P2`, … and each is referenced by a `⚠ VERIFY` marker at the matching question in
`past-papers/<paper>.md`. **The full entry lives here only** — the paper file just points to it.

| IDs | Paper |
|---|---|
| **P1–P3** | Assignment 1, 10 Aug 2026 — *tabulated in `past-papers/00-past-papers-index.md`, not repeated here* |
| **P4–P8** | End of Semester Examination, **23 Oct 2024** |
| **P9–P12** | CAT 1, **20 Aug 2024** |
| **P13–P18** | End of Semester Examination, **27 Oct 2025** |

★ marks the worst defect on each paper.

> **Read this section beside § A.** Two of these papers set, verbatim, a worked example and an exercise
> out of the lecture documents — and the KB already flags a substantive error inside one of them (**V3**,
> ·CRV p18) and a reconstructed line beside it (**L5**). See P-entries and the "What this paper adds"
> sections of the two exam files.

---

### P4 · EMT 3101 End of Semester (23 Oct 2024), Q1(c) — the variance you are told to prove is the reciprocal of the right one ★
- **Paper:** "Show, by a detailed method, that $\mathrm{Var}(X) = \dfrac{1}{18a^{2}}$", for the density
  $f(x) = kx$ on $0 \le x \le a$, $a$ and $k$ positive constants.
- **Issue:** the variance of that density is $\dfrac{a^{2}}{18}$, not $\dfrac{1}{18a^{2}}$. Normalisation
  gives $k = 2/a^{2}$; then $E(X) = 2a/3$, $E(X^{2}) = a^{2}/2$ and
  $\mathrm{Var}(X) = \tfrac{a^{2}}{2} - \tfrac{4a^{2}}{9} = \tfrac{a^{2}}{18}$. **Recomputed symbolically
  with `sympy` on 2026-09-03.** The two expressions agree only at $a = 1$. It matters more than a
  misprint normally would because the question is a **show that**: the printed line is the target the
  candidate steers towards, so a student who trusts it spends five marks hunting an algebra slip that
  is not there.
- **Correct form:** $\mathrm{Var}(X) = \dfrac{a^{2}}{18}$.
- **How to handle:** derive it, get $a^{2}/18$, and **say in the script that the printed target is wrong
  and why** — one line, and it converts a trap into a mark. *(He caught it in the exam: on the
  photograph the printed right-hand side is struck through in blue ballpoint with "a²/18" written beside
  it. That is his own correction, not a mark scheme — the paper carries no answers.)*
- **Severity:** value.

### P5 · EMT 3101 End of Semester (23 Oct 2024), Q3(b)(i) — two numbering levels collide
- **Paper:** "**(i)** Calculate the value of: **(i)** $P(T > 3.5)$ and **(ii)** $P(T = 3)$. *[3 Marks]*"
- **Issue:** item (i) of Q3(b) contains its own (i) and (ii), so "(i)" names two different things one
  line apart. The four graded parts of Q3(b) are the outer (i)–(iv); the inner pair share the outer
  (i)'s three marks between them.
- **How to handle:** when setting this as a mock, relabel the inner pair (α)/(β) or "first"/"second" and
  say you have done so. Reprinted **unchanged** on the 2025 paper — see P18.
- **Severity:** structural.

### P6 · EMT 3101 End of Semester (23 Oct 2024), formula sheet (page 4) — the Gamma function's argument changes name inside its own definition
- **Paper:** $\Gamma(n) = \int_0^{\infty}t^{x-1}e^{-t}\,dt$
- **Issue:** the left-hand side is a function of $n$ and the right-hand side of $x$. Whichever letter was
  meant, one of them is wrong. The row also states **no convergence condition**, and the integral
  converges only for $x > 0$.
- **Correct form:** $\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}\,dt$, $x > 0$.
- **How to handle:** cosmetic in practice — nobody will lose a mark over it — but it is the *same*
  carelessness about $\Gamma$'s argument that produces the substantive P9 on the CAT, so it is worth
  naming when teaching either. The sheet is reprinted unchanged on the 2025 paper (P16).
- **Severity:** notation.

### P7 · EMT 3101 End of Semester (23 Oct 2024), Q2(a)(ii) — an integral with no differential
- **Paper:** "$\int_0^{0.1} e^{2x}\sin 3x.$" — no $dx$, closed with a full stop as though it were a
  sentence, and its "*[2 Marks]*" printed alone on the line below, level with nothing.
- **Issue:** intent is unambiguous ($dx$), but a displayed integral with no differential is exactly the
  habit the same course penalises in a script.
- **Severity:** notation. Reprinted unchanged on the 2025 paper — see P18.

### P8 · EMT 3101 End of Semester (23 Oct 2024), Q4 — a whole 15-mark question on a documented knowledge-base gap
- **Paper:** "Determine the power series solution of the differential equation $y'' + xy' + 2y = 0$ using
  **either** the **Leibniz-Maclaurin** method or the **Frobenius method**, given … $y = 1$ and
  $\frac{dy}{dx} = 2$." *[15 Marks]*
- **Issue:** not a defect in the paper's mathematics — a defect in what he can revise from, and it is the
  largest one in the subject. **Frobenius' method is a documented gap**: `00-index.md` § Gap map records
  that `06-bessels-equation.md` asserts the solution "is obtained by Frobenius' method" and that the
  lecturer's own margin reads *"Homework: show!! (Derive)"*. The derivation is on no page. The
  **Leibniz–Maclaurin** route from an ODE to a power series is not in `04` or `05` either; both files
  build the machinery and neither points it at a differential equation.
- **How to handle:** treat this as the **first gap to fill** if lecture notes ever arrive. It is not a
  one-off: the identical question, same ODE, same boundary conditions, was set on **CAT 1 (20 Aug 2024,
  7 marks, Leibniz–Maclaurin only)** and again on the **2025 final (27 Oct 2025, Q4(b), 11 marks)** —
  **33 marks across three papers**. Until then, say plainly that this material has not been supplied
  rather than teaching it from general knowledge.
- **Severity:** cataloguing.

---

### P9 · EMT 3101 CAT 1 (20 Aug 2024), Q2 stem — the Gamma integral given a domain it does not have ★
- **Paper:** "The Gamma function is defined as $\Gamma(x) = \int_0^{\infty}e^{-t}t^{x-1}dt$,
  $\;x \ne 0, -1, -2, -3, \cdots$"
- **Issue:** **the integral converges only for $x > 0$.** The excluded set $\{0,-1,-2,\dots\}$ is the set
  of *poles of the analytically continued* Gamma function — a different object, defined by continuation
  **precisely because the integral does not exist there**. As printed the definition claims, for
  instance, $x = -\tfrac12$, where the integrand behaves like $t^{-3/2}$ near the origin and the integral
  diverges.
- **Correct form:** $\Gamma(x) = \int_0^{\infty}e^{-t}t^{x-1}dt$ for $x > 0$; $\Gamma$ then extends to
  every $x \ne 0,-1,-2,\dots$ by analytic continuation, equivalently by iterating
  $\Gamma(x) = \Gamma(x+1)/x$.
- **How to handle:** quote the integral **with $x > 0$**, then add the one sentence about continuation.
  That is a mark gained, not lost — and it is exactly the kind of definitional line a memorising reader
  absorbs whole, which is why it is starred. Compare P6: the same casualness about $\Gamma$'s argument,
  on the exam formula sheet.
- **Severity:** value.

### P10 · EMT 3101 CAT 1 (20 Aug 2024), Q4 — a Maclaurin expansion of a function that has none
- **Paper:** "Use Maclaurin's theorem to expand $\sqrt{x}\ln(x+1)$ as a power series."
- **Issue:** Maclaurin's theorem needs $f$ and all its derivatives to exist at $x = 0$ (`04` §1 states the
  three conditions). Here $f'(x) = \dfrac{\ln(1+x)}{2\sqrt x} + \dfrac{\sqrt x}{1+x} \to -\infty$ as
  $x \to 0^{+}$, so **the product has no Maclaurin series at all**. What exists is
  $\sqrt x\left(x - \tfrac{x^{2}}{2} + \tfrac{x^{3}}{3} - \cdots\right)
  = x^{3/2} - \tfrac12 x^{5/2} + \tfrac13 x^{7/2} - \cdots$, a fractional-power (Puiseux) series.
- **Correct form:** "Expand $\ln(x+1)$ by Maclaurin's theorem and hence obtain a series for
  $\sqrt x\,\ln(x+1)$."
- **How to handle:** do exactly that, integrate term by term, and **write the one sentence saying why the
  product itself has no Maclaurin series**. The marks are unaffected and the sentence is free credit.
  The same looseness runs through this subject's assessments — Assignment 1 Q4 integrates
  $\theta^{-1/3}$ without mentioning that it is singular at the lower limit, and
  `past-papers/00-past-papers-index.md` already makes that point.
- **Severity:** ambiguity.

### P11 · EMT 3101 CAT 1 (20 Aug 2024), Q1 and Q2 — mark allocations that attach to the wrong thing, and no total
- **Paper:** Q1 prints a single "*[7 Marks]*" covering four sub-parts (a)–(d) with no split between them.
  Q2 prints "*[5 Marks]*" on the line carrying the **definition of $\Gamma(x)$** — the stem — above its
  two sub-parts (i) and (ii), so as laid out the definition itself appears to be worth five marks. **No
  total is printed anywhere on the sheet.**
- **Issue:** the paper's marks are therefore 7 + 5 + 7 + 5 = 24 only by inference, and two of the four
  allocations cannot be attributed to a specific task. This is why the paper file records
  `marks_reconcile: false` — there is nothing to reconcile *against*.
- **How to handle:** for a timed mock, mark Q1 out of 7 as a single whole, and split Q2 as 3 for (i) and
  2 for (ii) — (i) does the work — stating that the split is yours.
- **Severity:** structural.

### P12 · EMT 3101 CAT 1 (20 Aug 2024), throughout — notation and punctuation, collected
- **Paper:** "$E(T) = Var(T)$" with *Var* set in italic maths, so it reads as a product $V\!\cdot\!a\!\cdot\!r$
  (Q1(c)) — the house form is $\mathrm{Var}(T)$. "Hence evaluate, correct to 3 decimal places," closes
  with a **comma** before a displayed integral (Q4). "Show your workings" for "your working"
  (instructions).
- **Severity:** typo. None of it touches the mathematics; collected in one entry rather than three.

---

### P13 · EMT 3101 End of Semester (27 Oct 2025), Q3(b) — the Beta reduction formula printed without the $n$ it depends on ★
- **Paper:** "Show clearly that
  $\displaystyle\int_0^{1}x^{m-1}(1-x)^{p-1}dx = \frac{1}{n}B\!\left(\frac{m}{n},p\right), \; n \ne 0$.
  Hence, find the exact value of $\displaystyle\int_0^{1}x^{5}(1-x^{3})^{2}dx$."
- **Issue:** **no $n$ appears on the left-hand side at all.** As printed the left side is exactly
  $B(m,p)$, a number independent of $n$, while the right side changes with every $n$ — so the identity is
  false for all but one value of $n$, and it cannot be "shown". The "hence" is then unreachable: the
  integrand $x^{5}(1-x^{3})^{2}$ has a cube inside the bracket and the printed identity has no slot for
  it.
- **Correct form:** $\displaystyle\int_0^{1}x^{m-1}\left(1-x^{n}\right)^{p-1}dx
  = \frac{1}{n}B\!\left(\frac{m}{n},\,p\right)$.
- **Check (mine, `sympy`, 2026-09-03):** with the corrected identity, $m = 6$, $n = 3$, $p = 3$ give
  $\tfrac13 B(2,3) = \tfrac{1}{36}$; direct integration gives
  $\tfrac16 - \tfrac29 + \tfrac1{12} = \tfrac{1}{36}$. **They agree, which confirms the corrected form is
  the one the question was built on.**
- **How to handle:** write the identity with $(1-x^{n})$, prove it by $u = x^{n}$, and say the printed
  version is missing the exponent. *(On the photograph he has written a blue-pen "n" above the printed
  exponent — that is his own correction and it is right. **Reading caveat:** the blue ink partly
  obscures the printed characters; blue-channel isolation at 7× reads the printed glyph as $p$ in both
  places, and that reading is recorded as *partly obscured*, not clean.)*
- **Severity:** value.

### P14 · EMT 3101 End of Semester (27 Oct 2025), Q1(c) — a density with two unknowns and only one condition
- **Paper:** $f(x) = mx$ on $0 \le x \le 4$, $f(x) = k$ on $4 \le x \le 9$, zero otherwise, "where $m$ and
  $k$ are positive constants. Find as an exact simplified fraction the value of $E(X)$."
- **Issue:** normalisation gives $8m + 5k = 1$ — **one equation, two unknowns**. Every admissible $m$
  gives a different answer: $E(X) = \tfrac{13}{2} - \tfrac{92m}{3}$ (verified with `sympy`,
  2026-09-03). **As printed the question cannot be answered.**
- **Correct form:** add the missing condition — continuity of $f$ at $x = 4$, i.e. $4m = k$. That gives
  $m = \tfrac{1}{28}$, $k = \tfrac17$ and $E(X) = \tfrac{227}{42} \approx 5.4048$ — a single exact
  simplified fraction, which is precisely what the question demands. **The wording is the evidence for
  the intent.**
- **How to handle:** state the continuity assumption **in writing before using it**, and say why it is
  needed. Contrast the 2024 paper's Q3(a), which is the same idea done properly: there both pieces are
  fully specified and normalisation alone pins $k$ down (to exactly $7/2$, a repeated root).
- **Severity:** omission.

### P15 · EMT 3101 End of Semester (27 Oct 2025), Q1(a) — a Bessel series asserted over $\mathbb{Z}$ that only exists over $\mathbb{N}$
- **Paper:** $J_n(x) = \sum_{r=0}^{\infty}\left[\frac{(-1)^{r}}{(n+r)!\,r!}\left(\frac x2\right)^{2r+n}\right]$,
  "$n \in \mathbb{Z}$", and the limit $\lim_{x\to0}J_n(x)/x^{n} = 1/(2^{n}n!)$, "$n \in \mathbb{Z}$".
- **Issue:** for a **negative** integer $n$, $(n+r)!$ is undefined for every $r < -n$, and $n!$ on the
  right-hand side is undefined outright. Both statements need $n \ge 0$.
- **Correct form:** $n \in \mathbb{N}$ (equivalently $n \in \mathbb{Z}$, $n \ge 0$). For general order the
  factorials become Gamma functions, $\Gamma(n+r+1)$ and $\Gamma(n+1)$ — which is how
  `06-bessels-equation.md` writes it.
- **How to handle:** answer for $n \ge 0$ and note the restriction; it costs nothing and shows you read
  the statement. Read it beside **V8** in § A — the KB's own Bessel document drops the $-\nu$ from the
  exponent of $J_{-\nu}$, so negative order is shaky in the notes as well as on the paper.
- **Severity:** notation.

### P16 · EMT 3101 End of Semester (27 Oct 2025), formula sheet (page 4) — the 2024 sheet reprinted unchanged, defect included
- **Paper:** $\Gamma(n) = \int_0^{\infty}t^{x-1}e^{-t}\,dt$ — character for character the 2024 sheet.
- **Issue:** see **P6** for the substance. The reason for a separate ID is the fact of the reprint: the
  sheet went out again thirteen months later with nothing corrected, so **this is a stable feature of the
  paper, not a one-off typo**, and he will meet it again.
- **Severity:** notation.

### P17 · EMT 3101 End of Semester (27 Oct 2025), Q4(b) — the documented gap, for the third time
- **Paper:** "Determine the power series solution of the differential equation $y'' + xy' + 2y = 0$ using
  **either** the **Leibniz-Maclaurin** method or the **Frobenius method** …" *[11 Marks]*
- **Issue:** see **P8**. Recorded separately because of the pattern it completes:

  | Paper | Where | Marks | Method allowed |
  |---|---|---|---|
  | CAT 1, 20 Aug 2024 | Q3 | 7 | Leibniz–Maclaurin only |
  | End of Semester, 23 Oct 2024 | Q4 | 15 | either |
  | End of Semester, 27 Oct 2025 | Q4(b) | 11 | either |

  **Identical wording, identical ODE, identical boundary conditions, 33 marks across three papers — and
  the method is not in this knowledge base.**
- **Severity:** cataloguing.

### P18 · EMT 3101 End of Semester (27 Oct 2025), Q2(a)(ii) and Q3(a)(i) — 2024's defects reprinted verbatim
- **Paper:** Q2(a)(ii) prints "$\int_0^{0.1}e^{2x}\sin3x.$" with no $dx$ and an orphaned "*[2 Marks]*"
  below it — identical to **P7**. Q3(a)(i) prints "Calculate the value of: (i) $P(T>3.5)$ and (ii)
  $P(T=3)$" inside an item already labelled (i) — identical to **P5**.
- **Issue:** neither affects the mathematics. They are logged together because of what they show about
  how the 2025 paper was made: **the 2024 file was reused, the mark values edited, and the typography
  left untouched.** That is corroboration for the recurrence analysis in the two paper files — 70 of the
  2025 paper's 90 marks are 2024 questions, word for word.
- **Severity:** typo.

### P19 · EMT 3101 Tutorial 1 (31 Aug 2026), Q3 — duplicated item letter
- **Sheet:** the four items of Question 3 are labelled **(i)**, **(ii)**, **(ii)**, **(iv)**.
- **Issue:** the third item carries the same letter as the second. It should be **(iii)**.
- **How to handle:** cosmetic — the four items are distinct and unambiguous. Worth noting only because a
  student answering "part (ii)" has to say which one, and because the same class of slip
  (duplicated item letters) is already logged for this department at **P8** on the 2024 fluid paper.
- **Severity:** typo (structural). No effect on the mathematics.

### P20 · EMT 3101 Tutorial 1 (31 Aug 2026), Q4 — the symbol changes between the formula and the sentence
- **Sheet:** "The second moment of area of a rectangle through its centroid is given by $\frac{bl^3}{12}$.
  Determine the approximate change in the second moment of area if $b$ is increased by 3.5% and **$I$** is
  reduced by 2.5%."
- **Issue:** the formula uses a lower-case **$l$** (the rectangle's depth); the sentence then says **$I$**
  (capital i). Worse, $I$ is the standard symbol for the second moment of area *itself* — so as printed the
  question says the second moment is reduced by 2.5 % **while asking for the change in the second moment**.
  It is circular on its face.
- **Correct reading:** the depth $l$ is reduced by 2.5 %. This is not a guess: **the same question appears
  on both the 23 Oct 2024 and 27 Oct 2025 finals, and both print $l$ in the sentence.** The tutorial is the
  only one of the three that gets it wrong.
- **How to handle:** use $l$. Point out to him that a capital $I$ and a lower-case $l$ are near-identical in
  this serif face, which is exactly why the convention is to name the quantity in words the first time.
- **Severity:** notation. Recoverable, and settled by the two finals.

### P21 · EMT 3101 Tutorial 1 (31 Aug 2026), Q6(a) — the Beta reduction formula, missing its $x^n$ ★
- **Sheet:** "Show clearly that
  $\displaystyle\int_0^{1}x^{m-1}(1-x)^{p-1}dx = \frac{1}{n}B\!\left(\frac{m}{n},p\right),\; n \ne 0.$"
- **Issue:** **there is no $n$ on the left-hand side.** As printed the left side is exactly $B(m,p)$ — a
  number that does not depend on $n$ — while the right side changes with every $n$. The identity is false
  for all but one value of $n$, so it cannot be "shown". Part (b) is then unreachable: its integrand
  $x^{5}(1-x^{3})^{2}$ has a cube inside the bracket and the printed identity has nowhere to put it.
- **Correct form:** $\displaystyle\int_0^{1}x^{m-1}\left(1-x^{n}\right)^{p-1}dx
  = \frac{1}{n}B\!\left(\frac{m}{n},\,p\right)$, proved by the substitution $u = x^{n}$.
- **Check (mine, `sympy`, 2026-09-04):** with the corrected identity, $m=6$, $n=3$, $p=3$ give
  $\tfrac13 B(2,3) = \tfrac1{36}$, and direct integration of $x^5(1-x^3)^2$ over $[0,1]$ gives $\tfrac1{36}$.
  They agree, confirming the corrected form is the one part (b) was built on.
- **⚠ This is the SAME defect, in the SAME question, as P13** — the 27 Oct 2025 end-of-semester paper's
  Q3(b). **The lecturer has reissued the question to the 2026 cohort without fixing it.** That is worth
  telling him directly: it means the printed error is stable, and it will probably appear again.
- **Severity:** value. The question is unanswerable as printed.

### P22 · EMT 3101 Tutorial 1 (31 Aug 2026), Q5 — "Maclaurin's theorem" applied to a function that has no Maclaurin series
- **Sheet:** "Use Maclaurin's theorem to expand $\sqrt{x}\ln(x+1)$ as a power series."
- **Issue:** a Maclaurin series requires **all** derivatives at $x=0$. The expansion of
  $\sqrt{x}\ln(x+1)$ runs $x^{3/2} - \tfrac12 x^{5/2} + \tfrac13 x^{7/2} - \cdots$ — **half-integer
  powers**, a Puiseux series, not a Maclaurin one. The second derivative does not exist at 0.
- **Intended route, which is unambiguous:** expand $\ln(1+x)$, which *does* have a Maclaurin series, and
  multiply the result by $\sqrt{x}$. Then integrate term by term. The "hence" works perfectly.
- **How to handle:** teach the method as intended, but make the distinction out loud — it is a genuinely
  useful thing for him to know, and a good marker will not penalise a student who names it. Do **not**
  treat this as a blocker; it is a wording looseness the textbooks share.
- **Severity:** notation (wording). Method unaffected.

<!-- Later papers append their own P-numbered entries above this line. -->

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
