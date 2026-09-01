---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
section: "03 — The Binomial Theorem and Binomial Series"
source: "BIN — 'Topic-3.1-Binomial-Theorem.pdf', 8 pp., handwritten, 300 dpi scan, no text layer. Marked '3.1' in the notes, under the heading '3. Power Series Method of solving O.D.E'."
file_role: topic
subtopics:
  - "the general binomial expansion of (a+x)^n"
  - "when the series terminates and when it does not"
  - "binomial coefficients and the sigma form"
  - "the rth term of an expansion"
  - "the (1+x)^n form and its range of validity"
  - "the small-x approximation (1+x)^n ≈ 1 + nx"
  - "expansions with negative and fractional index"
  - "percentage-change problems and approximate error analysis"
key_equations:
  [binomial-general, binomial-sigma, rth-term, binomial-unit, small-x-approx,
   validity-range]
prerequisites: ["01 — Gamma and Beta Functions (factorials, §1)"]
leads_to: ["04 — Maclaurin's Theorem", "05 — Leibniz Theorem"]
verification_flags: 3   # 1 substantive (V5) + 2 cosmetic (C8–C9); plus scan limits L8–L11
tags: [binomial-theorem, binomial-series, binomial-coefficient, rth-term,
       negative-index, fractional-index, approximation, percentage-error,
       power-series, emt3101]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set in the notes ·
  [fig] figure described from the rendered page · [added] not in the notes — supplied here ·
  ·BIN pN provenance (scan page — these pages carry no printed numbers) ·
  ⚠ VERIFY = flagged suspected source error, see _verification-log.md -->

# 03 — The Binomial Theorem and Binomial Series

**Source:** BIN, 8 handwritten pages. The top-left margin of p1 is marked "Topic 3"; the material is
numbered **3.1** beneath the section heading *3. Power Series Method of solving O.D.E*. Files `03`,
`04` and `05` are that section's three parts — see `00-index.md` § Section 3.

Two halves: pp. 1–6 are the algebra (expansion, rth term, validity, negative and fractional
indices); pp. 7–8 are the engineering use — approximate percentage change when several quantities
each move a little.

> **Reliability note.** One substantive defect (V5) and it is in the *stated answer* of the very
> first worked example, with the correct value derived one line above it. That pattern — the
> working right, the copied-down answer wrong — recurs across this subject.

---

## 1. The binomial expansion

### 1.1 What it is for ·BIN p1

[def] The **binomial series** (or binomial theorem) is a formula for raising a binomial expression to
any power **without lengthy multiplication**.

### 1.2 The general expansion ·BIN p1

[eq: binomial-general]

$$\boxed{\;(a+x)^{n} = a^{n} + n a^{\,n-1}x + \frac{n(n-1)}{2!}a^{\,n-2}x^{2} + \frac{n(n-1)(n-2)}{3!}a^{\,n-3}x^{3} + \cdots\;} \tag{1}$$

where $3! = 3\times2\times1$, "factorial 3".

**What $n$ is allowed to be** ·BIN p1 — this is the point of the topic:

| $n$ | Series |
|---|---|
| positive integer | **finite** — it comes to an end |
| negative integer | **infinite** |
| fraction / decimal fraction | **infinite** |

### 1.3 Sigma form and the binomial coefficient ·BIN p1

[eq: binomial-sigma]

$$(a+x)^{n} = \sum_{k=0}^{n}\frac{n!}{(n-k)!\,k!}\,a^{\,n-k}x^{k}, \qquad {}^{n}C_k = \frac{n!}{(n-k)!\,k!}$$

$^{n}C_k$ is the **binomial coefficient**.

> ⚠ **SCAN (L8)** — the lower half of p1 carries **two passes of writing crossing each other**,
> and the "called Binomial coefficient" label runs off the right edge. The content above is what
> could be separated out; it is complete and internally consistent.

### 1.4 The rth term ·BIN p2

[eq: rth-term] The notes reason from the pattern: in the fourth term of $(a+x)^n$ the number 3 is
"very evident" — it appears as $3!$, as $a^{n-3}$ and as $x^{3}$. So for the **rth** term the
recurring number is $(r-1)$:

$$\boxed{\;\text{rth term} = \frac{n(n-1)(n-2)\cdots\text{to }(r-1)\text{ terms}}{(r-1)!}\;a^{\,n-(r-1)}\,x^{\,r-1}\;}$$

> ⚠ **SCAN (L9)** — the final exponent sits at the right edge of the scan: "$x^{r-}$" is visible
> with the trailing character clipped. Reconstructed as $x^{\,r-1}$, which is what the rest of the
> line and the standard form both require.

### 1.5 The $(1+x)^n$ form ·BIN p2

[eq: binomial-unit] Setting $a = 1$ in (1):

$$(1+x)^{n} = 1 + nx + \frac{n(n-1)}{2!}x^{2} + \frac{n(n-1)(n-2)}{3!}x^{3} + \cdots$$

[eq: validity-range] valid for

$$\boxed{\;-1 < x < 1 \quad\text{i.e.}\quad |x| < 1\;}$$

[added] **The range is only needed when the series is infinite** — that is, when $n$ is negative or
fractional (§1.2). For a non-negative integer $n$ the expansion terminates and holds for every $x$,
which is why Examples 1–3 substitute freely.

[eq: small-x-approx] And when $x$ is small compared with 1:

$$\boxed{\;(1+x)^{n} \approx 1 + nx\;}$$

**This one approximation carries the whole of §4.** Every percentage-change problem is an
application of it.

---

## 2. Worked examples — positive integer index

> [ex] **Example 1** ·BIN p2–3 — Expand $(2+x)^{7}$.
>
> With $a = 2$, $n = 7$ in (1):
>
> $$(2+x)^{7} = 2^{7} + 7(2)^{6}x + \frac{(7)(6)}{2!}(2)^{5}x^{2} + \frac{(7)(6)(5)}{3!}(2)^{4}x^{3}$$
> $$+ \frac{(7)(6)(5)(4)}{4!}(2)^{3}x^{4} + \frac{(7)(6)(5)(4)(3)}{5!}(2)^{2}x^{5} + \frac{(7)(6)(5)(4)(3)(2)}{6!}(2)x^{6} + \frac{7!}{7!}x^{7}$$
>
> **Correct result:**
> $$\boxed{\;(2+x)^{7} = 128 + 448x + 672x^{2} + 560x^{3} + 280x^{4} + 84x^{5} + 14x^{6} + x^{7}\;}$$
>
> ⚠ **VERIFY (V5)** — the page prints the coefficient of $x$ as **44**. It is **448**. The ink was
> re-read at 600 dpi and unambiguously shows two digits, "44", followed by the $x$ — so this is the
> source's error, not a transcription slip. The line **directly above** derives it correctly as
> $7(2)^{6}x = 7\times64\,x = 448x$; only the copied-down answer is wrong. Every other coefficient
> on that line is right.

> [ex] **Example 2** ·BIN p3 — Expand $(2a - 3b)^{5}$.
>
> Here the "$a$" of the formula is $2a$, the "$x$" is $-3b$, and $n = 5$:
>
> $$(2a-3b)^{5} = (2a)^{5} + 5(2a)^{4}(-3b) + \frac{(5)(4)}{2!}(2a)^{3}(-3b)^{2} + \frac{(5)(4)(3)}{3!}(2a)^{2}(-3b)^{3}$$
> $$+ \frac{(5)(4)(3)(2)}{4!}(2a)(-3b)^{4} + \frac{5!}{5!}(-3b)^{5}$$
>
> $$= 32a^{5} - 240a^{4}b + 720a^{3}b^{2} - 1080a^{2}b^{3} + 810ab^{4} - 243b^{5} \ ✓$$
>
> **Watch the signs.** They alternate because the second term is negative; carrying $(-3b)$ as a
> whole through each power is what keeps them right.

> [ex] **Example 3** ·BIN p4 — Find the middle term of $\left(2p - \dfrac{1}{2q}\right)^{10}$.
>
> $(a+x)^{10}$ has $10+1 = 11$ terms, so the middle one is the **sixth**: $r = 6$, hence
> $r - 1 = 5$. With $a = 2p$, $x = -\dfrac{1}{2q}$, $n = 10$:
>
> $$\frac{(10)(9)(8)(7)(6)}{(6-1)!}\,(2p)^{10-5}\left(-\frac{1}{2q}\right)^{5} = 252\left(32p^{5}\right)\left(-\frac{1}{32q^{5}}\right)$$
>
> $$= \boxed{\;-252\,\frac{p^{5}}{q^{5}}\;} \ ✓$$
>
> **(L10) — settled.** The denominator glyph was previously flagged as ambiguous between 5 and 6.
> Re-read at 600 dpi it closes into a **loop at the bottom**, which is this hand's 6; its 5 (see
> "$r-1 = 5$" four lines above on the same page) has a strictly **open** bowl and a separate
> straight top bar. It reads **$(6-1)!$**, and the arithmetic agrees: $30240/5! = 252$, whereas
> $30240/4! = 1260$. No flag needed.

---

## 3. Negative and fractional index

> [ex] **Exercise 4** ·BIN p5 — (a) Expand $\dfrac{1}{(1+2x)^{3}}$ in ascending powers of $x$ as far
> as $x^{3}$. (b) State the limits of $x$ for which it is valid.
>
> **(a)** Rewrite as a negative power, then use §1.5 with $n = -3$ and $x \to 2x$:
>
> $$(1+2x)^{-3} = 1 + (-3)(2x) + \frac{(-3)(-4)}{2!}(2x)^{2} + \frac{(-3)(-4)(-5)}{3!}(2x)^{3} + \cdots$$
>
> $$= \boxed{\;1 - 6x + 24x^{2} - 80x^{3} + \cdots\;} \ ✓$$
>
> **(b)** The expansion of $(1+X)^{n}$ needs $|X| < 1$, and here $X = 2x$:
>
> $$|2x| < 1 \Rightarrow 2|x| < 1 \Rightarrow |x| < \tfrac12 \qquad\text{i.e.}\qquad -\tfrac12 < x < \tfrac12$$
>
> *(The page works this out in the right margin, step by step.)*

**The pattern to carry forward:** with a negative index the numerator factors
$n(n-1)(n-2)\cdots$ are all negative, so the signs alternate and the series never terminates —
which is exactly why a validity range is needed.

---

## 4. Exercise sets

### 4.1 Exercise — expansions ·BIN p4

[exercise]

**1)** Expand $\left(c - \dfrac1c\right)^{5}$ using the binomial series.
&nbsp;**Solution:** $c^{5} - 5c^{3} + 10c - \dfrac{10}{c} + \dfrac{5}{c^{3}} - \dfrac{1}{c^{5}}$ ✓

**2)** Without fully expanding $(3+x)^{7}$, determine the fifth term.
&nbsp;**Ans:** $945x^{4}$ ✓ &nbsp;*(This is the rth-term formula with $r = 5$: $\binom74 3^{3}x^{4}$.)*

**3)** Evaluate $(1.002)^{9}$ using the binomial theorem, correct to (a) 3 decimal places and
(b) 7 significant figures.
&nbsp;**Solution:** (a) $1.018$ ✓ &nbsp; (b) *see flag*

> ⚠ **SCAN (L11)** — the (b) answer sits **on the bottom edge of the page**; only the tops of the
> digits survive. The visible fragment is consistent with **1.018145**, which is the correct value
> ($(1.002)^{9} = 1.01814467\ldots$), but it cannot be read off the ink. Use 1.018145; do not cite
> the page for it.

### 4.2 Exercise — approximations ·BIN p6

[exercise]

**1)** Expand $\dfrac{1}{\sqrt{1-2t}}$ in ascending powers of $t$ as far as $t^{3}$, and state the
limits of $t$ for which it is valid.
&nbsp;**Solution:** $1 + t + \tfrac32t^{2} + \tfrac52t^{3} + \cdots$, valid for
$|2t| < 1$, i.e. $-\tfrac12 < t < \tfrac12$ ✓

**2)** Simplify $\dfrac{\sqrt[3]{1-3x}\;\sqrt{1+x}}{\left(1 + \frac{x}{2}\right)^{3}}$, given that
powers of $x$ above the first may be neglected.
&nbsp;**Ans:** $1-2x$ ✓

&nbsp;&nbsp;[added] *Why:* each factor collapses under $(1+X)^n \approx 1+nX$ —
$1 - x$, $1 + \tfrac{x}{2}$ and $1 + \tfrac{3x}{2}$ respectively — and
$(1-x)(1+\tfrac x2)(1+\tfrac{3x}{2})^{-1} \approx 1 - 2x$ to first order.

**3)** When $x$ is very small, show that
&nbsp;**i)** $\dfrac{1-2x}{(1-3x)^{4}} \approx 1 + 10x$ ✓ &nbsp;&nbsp;
**ii)** $\dfrac{1}{(1-x)^{2}\sqrt{1-x}} \approx 1 + \tfrac52 x$ ✓

&nbsp;&nbsp;[added] (ii) is $(1-x)^{-5/2}$; the first-order term is $-\tfrac52(-x) = \tfrac52 x$.

---

## 5. Practical problems ·BIN p7–8

*(A blue pen mark at the top-left of p7 appears to read "Stop"/"Stopped" — a lecture bookmark.)*

Binomial expansions are used for **numerical approximations**, for **calculations with small
variations**, and in **probability theory**.

> [ex] **Example 1** ·BIN p7 — The radius of a cylinder is reduced by 4 % and its height increased
> by 2 %. Find the approximate percentage change in (a) its volume and (b) its curved surface area,
> neglecting products of small quantities.
>
> **(a)** $V = \pi r^{2}h$. New values $(1-0.04)r$ and $(1+0.02)h$:
>
> $$V_{\text{new}} = \pi r^{2}h(1-0.04)^{2}(1+0.02)$$
>
> Expand the square and drop the $x^{2}$ term:
> $$(1-0.04)^{2} = 1 - 2(0.04) + (0.04)^{2} \approx 1 - 0.08$$
>
> $$V_{\text{new}} \approx \pi r^{2}h(1-0.08)(1+0.02) \approx \pi r^{2}h(1 - 0.08 + 0.02) = 0.94\,\pi r^{2}h$$
>
> **94 % of the original — a reduction of about 6 %.** ✓
>
> [added] The exact factor is $0.96^{2}\times1.02 = 0.9400$, so here the approximation is not just
> close, it is exact to four decimals.
>
> **(b)** Curved surface area $= 2\pi rh$:
>
> $$A_{\text{new}} = 2\pi rh(1-0.04)(1+0.02) \approx 2\pi rh(1 - 0.04 + 0.02) = 0.98(2\pi rh)$$
>
> **98 % of the original — a reduction of about 2 %.** ✓ *(Exact: $0.96\times1.02 = 0.9792$.)*
>
> **The method in one line:** turn each percentage change into $(1 \pm \delta)$, raise it to the
> power that appears in the formula, keep only first-order terms, and add the $\delta$'s.

### Exercise ·BIN p8

[exercise]

**1)** The resonant frequency of a vibrating shaft is

$$f = \frac{1}{2\pi}\sqrt{\frac{k}{I}}$$

where $k$ is the stiffness and $I$ the inertia. Use the binomial theorem to find the approximate
percentage error in $f$ when the measured $k$ is **4 % too large** and the measured $I$ is
**2 % too small**.

&nbsp;**Ans:** $f_1 \approx 1.03f$ — i.e. **3 % too large** ✓

&nbsp;[added] *Working:* $f_1/f = \sqrt{1.04/0.98} = (1.04)^{1/2}(0.98)^{-1/2} \approx (1+0.02)(1+0.01) \approx 1.03$.
Exact value 1.03016.

**2)** The **electric** field strength $H$ due to a magnet of length $2l$ and moment $M$, at a point
on its axis a distance $x$ from the centre, is

$$H = \frac{M}{2l}\left\{\frac{1}{(x-l)^{2}} - \frac{1}{(x+l)^{2}}\right\}$$

Show that if $l$ is very small compared with $x$, then $H \approx \dfrac{2M}{x^{3}}$ ✓

> ⚠ **VERIFY (C8)** — the question says "**electric** field strength $H$ due to a magnet". A magnet
> produces a **magnetic** field, and $H$ is the standard symbol for magnetic field strength (A/m).
> The mathematics is unaffected, but do not carry the label into an electromagnetics paper.

> ⚠ **VERIFY (C9)** — the magnet half-length in this question is written with a glyph
> **identical to the capital $I$ used for inertia in question 1** on the same page. It is a
> lowercase $\ell$: $2l$ is the magnet's length, and only that reading gives the stated limit
> $2M/x^{3}$. A notation clash inside one exercise set — see `_nomenclature.md`.

&nbsp;[added] *Sketch of the limit:* expand each bracket by the binomial series,
$(x\mp l)^{-2} = x^{-2}\left(1 \mp \tfrac lx\right)^{-2} \approx x^{-2}\left(1 \pm \tfrac{2l}{x}\right)$;
the difference is $4l/x^{3}$, and $\frac{M}{2l}\cdot\frac{4l}{x^{3}} = \frac{2M}{x^{3}}$.
Confirmed symbolically.

---

## Flags raised in this file

| ID | Page | What the page shows | Correct form |
|---|---|---|---|
| **V5** | p3 | $(2+x)^{7} = 128 + \mathbf{44}x + \cdots$ | $\mathbf{448}x$ — derived correctly one line above |
| C8 | p8 | "the **electric** field strength $H$ due to a magnet" | magnetic field strength |
| C9 | p8 | magnet half-length $l$ written like the capital $I$ of Q1 | lowercase $\ell$ |
| L8 | p1 | two writing passes overlap; "Binomial coefficient" label clipped | content recovered |
| L9 | p2 | rth-term exponent clipped: "$x^{r-}$" | $x^{\,r-1}$, reconstructed |
| L10 | p4 | factorial glyph, 5 vs 6 | **resolved: $(6-1)!$** |
| L11 | p4 | $(1.002)^{9}$ to 7 s.f., cut by the bottom edge | $1.018145$, computed not read |

Full detail in `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
