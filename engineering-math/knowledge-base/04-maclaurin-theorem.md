---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
section: "04 — Maclaurin's Theorem"
source: "MAC — 'Topic-3.2-Maclaurin Theorem.pdf', 7 pp., handwritten, 300 dpi scan, no text layer. Marked '3.2' in the notes."
file_role: topic
subtopics:
  - "functions as power series in ascending powers of the variable"
  - "the Maclaurin series and its three validity conditions"
  - "building a series from successive derivatives at the origin"
  - "numerical integration by expanding the integrand"
  - "evaluating indeterminate limits from series"
  - "L'Hôpital's rule as the fallback"
key_equations: [maclaurin-series, maclaurin-conditions, lhopital]
prerequisites: ["03 — The Binomial Theorem", "repeated differentiation", "standard series for e^x, sin x, cosh x"]
leads_to: ["06 — Bessel's Equation (series solutions of ODEs)"]
verification_flags: 4   # 1 substantive (V6) + 3 cosmetic (C10–C12)
tags: [maclaurin-series, power-series, taylor, numerical-integration,
       indeterminate-form, lhopital, limits, emt3101]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set in the notes ·
  [fig] figure described from the rendered page · [added] not in the notes — supplied here ·
  ·MAC pN provenance (scan page — these pages carry no printed numbers) ·
  ⚠ VERIFY = flagged suspected source error, see _verification-log.md -->

# 04 — Maclaurin's Theorem

**Source:** MAC, 7 handwritten pages, numbered **3.2** — the second part of section 3, *Power Series
Method of solving O.D.E*.

Three uses, in order: **represent** a function as a series (§1–2), **integrate** something that has
no analytic antiderivative (§3), and **evaluate an indeterminate limit** (§4). The theorem itself is
four lines; everything else is application.

> **Reliability note.** One substantive defect (V6) — an exercise whose stated limit and stated
> answer do not belong to the same integral. It matters because it is a *checkable* answer you would
> otherwise trust.

---

## 1. The Maclaurin series

### 1.1 Why power series ·MAC p1

Some functions can be written as power series in ascending powers of the variable. The notes give
three:

$$e^{x} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots$$

$$\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \cdots$$

$$\cosh x = 1 + \frac{x^{2}}{2!} + \frac{x^{4}}{4!} + \cdots$$

> ⚠ **VERIFY (C10)** — in the $\sin x$ line the sign before $x^{7}/7!$ was written **+** and then
> heavily struck through. A minus is what the series requires, and the strike-through reads as a
> correction — but what is on the page is a defaced plus, not a clean minus. Learn the minus.

**Why bother** ·MAC p1 — a mixed function containing algebraic, trigonometric and exponential parts
becomes a purely algebraic one, and differentiation and integration are then often far quicker.

### 1.2 The theorem ·MAC p1

[def] Let $f(x)$ be **infinitely differentiable at the origin** — that is, $f^{(n)}(0)$ exists for
every positive integer $n$.

[eq: maclaurin-series]

$$\boxed{\;f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^{2} + \frac{f'''(0)}{3!}x^{3} + \cdots\;}$$

**The whole method in one sentence:** differentiate repeatedly, evaluate each derivative at
$x = 0$, divide the $k$-th by $k!$, and that is the coefficient of $x^{k}$.

### 1.3 The three conditions ·MAC p1–2

[eq: maclaurin-conditions] A function may be represented this way provided that at $x = 0$:

&nbsp;&nbsp;**i)** $f(0) \neq \infty$
&nbsp;&nbsp;**ii)** $f'(0),\ f''(0),\ f'''(0),\ \ldots \neq \infty$
&nbsp;&nbsp;**iii)** the resulting series is **convergent**

(i) and (ii) rule out anything singular at the origin — $\ln x$ and $1/x$ fail immediately.
(iii) is what bounds the range over which the series may be used.

---

## 2. Building a series

> [ex] **Example** ·MAC p2 — Develop a series for $\sinh x$.
>
> The derivatives cycle with period 2, which makes the table short:
>
> | derivative | at $x = 0$ |
> |---|---|
> | $f(x) = \sinh x$ | $0$ |
> | $f'(x) = \cosh x$ | $1$ |
> | $f''(x) = \sinh x$ | $0$ |
> | $f'''(x) = \cosh x$ | $1$ |
> | $f^{(\mathrm{iv})}(x) = \sinh x$ | $0$ |
> | $f^{(\mathrm{v})}(x) = \cosh x$ | $1$ |
>
> Substituting into the series:
>
> $$\sinh x = 0 + x(1) + \frac{0}{2!}x^{2} + \frac{1}{3!}x^{3} + \frac{0}{4!}x^{4} + \frac{1}{5!}x^{5} + \cdots$$
>
> $$\boxed{\;\sinh x = x + \frac{x^{3}}{3!} + \frac{x^{5}}{5!} + \cdots\;} \ ✓$$
>
> ⚠ **VERIFY (C11)** — the $x^{4}$ term is written on the page as $\frac{x^{4}}{4}(0)$: the
> factorial has lost its exclamation mark and the zero has been moved behind the power. It should be
> $\frac{f^{(\mathrm{iv})}(0)}{4!}x^{4} = \frac{0}{4!}x^{4}$. The term is zero either way, so the
> result is unaffected — but the pattern it teaches is wrong.
>
> **Compare with $\sin x$ in §1.1:** identical terms, except that $\sinh$ has all plus signs and
> $\sin$ alternates. That is the whole difference between the two.

### 2.1 Exercise ·MAC p2–3

[exercise] All four answers verified.

**1)** Produce a power series for $\cos^{2}2x$ as far as the term in $x^{6}$.
&nbsp;**Solution:** $1 - 4x^{2} + \dfrac{16}{3}x^{4} - \dfrac{128}{45}x^{6} + \cdots$ ✓

**2)** Determine the first three terms of the series for $\sin^{2}x$.
&nbsp;**Ans:** $x^{2} - \dfrac{x^{4}}{3} + \dfrac{2}{45}x^{6}$ ✓

**3)** Expand $e^{2\theta}\cos3\theta$ as far as the term in $\theta^{2}$.
&nbsp;**Ans:** $1 + 2\theta - \dfrac52\theta^{2}$ ✓

**4)** Determine the first three terms of the power series for $\ln(1+e^{x})$.
&nbsp;**Ans:** $\ln 2 + \dfrac{x}{2} + \dfrac{x^{2}}{8}$ ✓

&nbsp;[added] Note that (4) passes condition (i) only because of the $+1$: $f(0) = \ln 2$, finite.
$\ln(x)$ alone has no Maclaurin series at all.

---

## 3. Numerical integration by series ·MAC p3

**The problem:** many integrals have no antiderivative in closed form.

**The method** — an alternative to the Trapezoidal, mid-ordinate and Simpson's rules: expand the
integrand as a Maclaurin series, then integrate **term by term** with the power rule

$$\int a x^{n}\,dx = \frac{a x^{\,n+1}}{n+1} + c$$

> [ex] **Example 1** ·MAC p4–5 — Evaluate $\displaystyle\int_{0.1}^{0.4} 2e^{\sin\theta}\,d\theta$
> correct to 3 s.f.
>
> **Step 1 — expand $e^{\sin\theta}$.**
>
> $$f(\theta) = e^{\sin\theta}$$
> $$f'(\theta) = \cos\theta\,e^{\sin\theta}$$
> $$f''(\theta) = e^{\sin\theta}\left(\cos^{2}\theta - \sin\theta\right) \quad\text{(product rule)}$$
> $$f'''(\theta) = e^{\sin\theta}\cos\theta\left[\cos^{2}\theta - \sin\theta - 2\sin\theta - 1\right]$$
>
> At the origin:
> $$f(0) = 1,\qquad f'(0) = 1,\qquad f''(0) = 1,\qquad f'''(0) = 0$$
>
> $$e^{\sin\theta} = 1 + \theta + \frac{\theta^{2}}{2} + 0\cdot\theta^{3} + \cdots \ ✓$$
>
> ⚠ **VERIFY (C12)** — the page heads this block "**At x = 0**" while the variable throughout is
> $\theta$. Label only.
>
> **Step 2 — integrate term by term.**
>
> $$\int_{0.1}^{0.4} 2\left(1 + \theta + \frac{\theta^{2}}{2}\right)d\theta = \int_{0.1}^{0.4}\left(2 + 2\theta + \theta^{2}\right)d\theta$$
>
> $$= \left[2\theta + \theta^{2} + \frac{\theta^{3}}{3}\right]_{0.1}^{0.4} = 0.98133 - 0.21033 = \boxed{0.771}\ \text{(3 s.f.)} \ ✓$$
>
> [added] The exact integral is $0.77040$, so truncating after $\theta^{2}$ costs nothing at 3 s.f.
> here — but that is because the interval is short and close to the origin, not a general guarantee.

### 3.1 Exercise ·MAC p5

[exercise]

**1)** Evaluate $\displaystyle\int_0^{4}\frac{\sin\theta}{\theta}\,d\theta$ using Maclaurin series,
correct to 3 s.f. &nbsp;**Ans given:** $0.946$

> ⚠ **VERIFY (V6)** — **the stated limit and the stated answer do not belong to the same integral.**
>
> - The upper limit was re-read at 600 dpi and is an **unambiguous 4** — a textbook open-topped
>   4, nothing like this hand's 1.
> - $\displaystyle\int_0^{4}\frac{\sin\theta}{\theta}d\theta = \mathrm{Si}(4) = \mathbf{1.7582}$
> - $\displaystyle\int_0^{1}\frac{\sin\theta}{\theta}d\theta = \mathrm{Si}(1) = \mathbf{0.94608}$ — which is the printed answer, to 3 s.f.
>
> So the answer is the one for an upper limit of **1**. Since the limit is legible and the answer is
> not derived anywhere on the page, the most likely reading is that the **answer** was not updated
> when the limit changed. **Work it for whichever limit the exam gives you, and do not trust 0.946
> as a check on a limit of 4.**
>
> [added] *Term by term, for the limit as printed:*
> $$\int_0^{4}\left(1 - \frac{\theta^{2}}{3!} + \frac{\theta^{4}}{5!} - \frac{\theta^{6}}{7!} + \cdots\right)d\theta = 4 - \frac{4^{3}}{18} + \frac{4^{5}}{600} - \frac{4^{7}}{35280} + \cdots \to 1.7582$$
> The series converges slowly at $\theta = 4$ — seven terms to reach 3 s.f. — which is itself a
> reason to suspect the intended limit was smaller.

**2)** Evaluate $\displaystyle\int_0^{0.4} x\ln(1+x)\,dx$ correct to 3 decimal places.
&nbsp;**Ans:** $0.019$ ✓ *(exact 0.018682)*

**3)** Expand $\sqrt{x}\,\ln(x+1)$ as a power series; hence evaluate
$\displaystyle\int_0^{0.5}\sqrt{x}\,\ln(x+1)\,dx$ correct to 3 decimal places.

&nbsp;[added] **The page gives no answer.** To the 3 decimal places the question asks for, the
value is $\mathbf{0.061}$; in full it is $0.0606036$. From
$\sqrt{x}\ln(1+x) = x^{3/2} - \tfrac12 x^{5/2} + \tfrac13 x^{7/2} - \cdots$ integrated term by term.
**Ours, not the lecturer's.**

---

## 4. Limiting values ·MAC p6

**The problem:** direct substitution gives the indeterminate form $\tfrac00$.

**The series method:** replace the offending function by its series; the troublesome factor cancels.

> [ex] **Example 1** ·MAC p6 — $\displaystyle\lim_{x\to0}\frac{\tan x - x}{x^{3}}$
>
> Direct substitution gives $\tfrac00$. But $\tan x = x + \tfrac13x^{3} + \cdots$, so
>
> $$\lim_{x\to0}\frac{x + \tfrac13x^{3} + \cdots - x}{x^{3}} = \lim_{x\to0}\frac{\tfrac13x^{3} + \cdots}{x^{3}} = \boxed{\tfrac13} \ ✓$$

> [ex] **Example 2** ·MAC p6 — $\displaystyle\lim_{x\to0}\frac{\sinh x}{x}$
>
> $$= \lim_{x\to0}\frac{x + \frac{x^{3}}{3!} + \frac{x^{5}}{5!} + \cdots}{x} = \lim_{x\to0}\left(1 + \frac{x^{2}}{3!} + \frac{x^{4}}{5!} + \cdots\right) = \boxed{1} \ ✓$$

### 4.1 L'Hôpital's rule ·MAC p6–7

[eq: lhopital] Where the series method fails:

$$\boxed{\;\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}, \qquad g'(a) \neq 0\;}$$

If the result is still $\tfrac00$, differentiate numerator and denominator **again** (and again)
until the denominator is non-zero.

> [added] **The two lines above cannot both be read literally.** If $g'(a) \neq 0$ the new quotient
> is not $\tfrac00$, so there would never be anything to differentiate a second time — yet exercise
> (a) below does exactly that. The condition the theorem actually needs is $g'(x) \neq 0$ on a
> punctured neighbourhood of $a$ (and $\lim f'/g'$ existing). Quote the page's version if you are
> asked to state the rule; use the neighbourhood version when you apply it twice.

### 4.2 Exercise ·MAC p7

[exercise]

**a)** $\displaystyle\lim_{x\to0}\frac{\sin x - x}{x^{2}}$ — worked on the page.
Direct substitution gives $\tfrac00$; one application of L'Hôpital gives $\dfrac{\cos x - 1}{2x}$,
still $\tfrac00$; a second gives

$$\lim_{x\to0}\frac{-\sin x}{2} = \boxed{0} \ ✓$$

**b)** $\displaystyle\lim_{x\to0}\frac{x - \sin x}{x - \tan x} = -\tfrac12$ ✓

**c)** $\displaystyle\lim_{t\to0}\frac{\sec t - 1}{t\sin t} = \tfrac12$ ✓

**d)** $\displaystyle\lim_{t\to1}\frac{\ln t}{t^{2}-1} = \tfrac12$ ✓

**e)** $\displaystyle\lim_{x\to0}\frac{\ln(1+x)}{x} = \ $ &nbsp;[added] $= \mathbf{1}$

**f)** $\displaystyle\lim_{\theta\to0}\frac{\sin\theta - \theta\cos\theta}{\theta^{3}} = \ $ &nbsp;[added] $= \mathbf{\tfrac13}$

**g)** $\displaystyle\lim_{x\to0}\frac{\sinh x - \sin x}{x^{3}} = \ $ &nbsp;[added] $= \mathbf{\tfrac13}$

> **(e), (f) and (g) are left blank on the page** — they sit in a right-hand column with the "="
> written and nothing after it, so they are set as unworked exercises, not lost to the scan. The
> three values above are **our computation, not the lecturer's**.
>
> [added] (g) is the cleanest illustration of why the series method beats L'Hôpital here:
> $$\sinh x - \sin x = \left(x + \tfrac{x^{3}}{6} + \cdots\right) - \left(x - \tfrac{x^{3}}{6} + \cdots\right) = \tfrac{x^{3}}{3} + \cdots$$
> so the limit is $\tfrac13$ by inspection, where L'Hôpital needs three rounds of differentiation.

---

## Flags raised in this file

| ID | Page | What the page shows | Correct form |
|---|---|---|---|
| **V6** | p5 | Exercise 1: $\int_0^{4}\frac{\sin\theta}{\theta}d\theta$, Ans 0.946 | limit **4** (confirmed in ink) gives $1.7582$; **0.946** is the answer for a limit of **1** |
| C10 | p1 | sign before $x^{7}/7!$ written "+", then struck through | $-$ |
| C11 | p2 | $x^{4}$ term written $\frac{x^{4}}{4}(0)$ | $\frac{0}{4!}x^{4}$ — term is zero either way |
| C12 | p4 | block headed "At x = 0" | the variable is $\theta$ |

Full detail in `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
