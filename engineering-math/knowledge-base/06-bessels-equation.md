---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
section: "06 — Bessel's Equation and Bessel Functions"
source: "BES — 'Topic-4-Bessels equation and Bessels function.pdf', 9 pp., handwritten, 300 dpi scan, no text layer. Filename says Topic 4; the page header says 'Topic 6'."
file_role: topic
subtopics:
  - "Bessel's equation and the meaning of its order ν"
  - "the Frobenius series solution in two branches"
  - "rewriting the solution with Gamma functions: J_ν and J_−ν"
  - "the general summation forms"
  - "integer order: J_n, and the special cases J_0 and J_1"
  - "the six recurrence formulas and their proofs"
key_equations:
  [bessel-equation, frobenius-solution, j-nu-series, j-minus-nu-series,
   j-n-series, j0-series, j1-series, recurrence-1, recurrence-2,
   recurrence-3, recurrence-4, recurrence-5, recurrence-6]
prerequisites:
  - "01 — Gamma and Beta Functions (Γ(n+1) = nΓ(n) is used in every proof)"
  - "04 — Maclaurin's Theorem (the power-series habit; and 03 behind it)"
  - "Frobenius' method (previous section of the course, not in these notes)"
leads_to: []
verification_flags: 3   # 2 substantive (V8–V9) + 1 cosmetic (C15); plus scan limits L17–L18
tags: [bessel-equation, bessel-function, frobenius, series-solution,
       gamma-function, recurrence-relation, j0, j1, ode, emt3101]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set in the notes ·
  [fig] figure described from the rendered page · [added] not in the notes — supplied here ·
  ·BES pN provenance (scan page — these pages carry no printed numbers) ·
  ⚠ VERIFY = flagged suspected source error, see _verification-log.md -->

# 06 — Bessel's Equation and Bessel Functions

**Source:** BES, 9 handwritten pages. The margin of p1 reads **"Topic 6"** while the filename says
Topic 4 — see C15.

The route: state the equation, quote its Frobenius solution as two series, rewrite those series with
Gamma functions so they close into a single summation, specialise to integer order, then spend five
pages proving six recurrence formulas — all six from the first two.

> **Reliability note.** Two substantive defects (V8, V9). V8 is a **dropped $-\nu$ in an exponent**
> and it silently changes every value the formula produces. Every one of the six recurrences and
> both series were checked numerically against SciPy and all are correct as stated.

---

## 1. Bessel's equation ·BES p1

[def] One of the most important differential equations in applied mathematics.

[eq: bessel-equation]

$$\boxed{\;x^{2}\frac{d^{2}y}{dx^{2}} + x\frac{dy}{dx} + \left(x^{2} - \nu^{2}\right)y = 0\;} \tag{1}$$

or, compactly, $x^{2}y'' + xy' + \left(x^{2} - \nu^{2}\right)y = 0$.

- $\nu$ — a real constant, called the **order** of the equation
- Applications the notes name: **electric fields**, **vibrations**, **heat conduction**

It is solved by **Frobenius' method**, from the previous section of the course. *(The margin carries
the lecturer's own instruction: "Homework: show!! (Derive)" — the derivation is not on these pages.)*

> ⚠ **SCAN (L17)** — the end of the sentence defining $\nu$ runs off the right edge; "…order of
> the" is visible and "Bessel's equation" is reconstructed from the wrap onto the next line.

### 1.1 The Frobenius solution ·BES p1

[eq: frobenius-solution] Two independent series, one for each root of the indicial equation:

$$y = A\,x^{\nu}\left\{1 - \frac{x^{2}}{2^{2}(\nu+1)} + \frac{x^{4}}{2^{4}\cdot2!\,(\nu+1)(\nu+2)} - \frac{x^{6}}{2^{6}\cdot3!\,(\nu+1)(\nu+2)(\nu+3)} + \cdots\right\}$$

$$+\ B\,x^{-\nu}\left\{1 + \frac{x^{2}}{2^{2}(\nu-1)} + \frac{x^{4}}{2^{4}\cdot2!\,(\nu-1)(\nu-2)} + \frac{x^{6}}{2^{6}\cdot3!\,(\nu-1)(\nu-2)(\nu-3)} + \cdots\right\} \tag{2}$$

✓ Both series verified correct. **The all-positive signs in the second brace are not a typo** — the
factors $(\nu-1)(\nu-2)\cdots$ each carry a sign that cancels the $(-1)^{k}$ of the first brace. If
you expect alternating signs there, that is the thing to check rather than "correct".

*(A margin arrow labels this "called **Bessel's function**".)*

---

## 2. Bessel functions in Gamma form ·BES p2

The point of the rewrite: those denominators $(\nu+1)(\nu+2)\cdots(\nu+k)$ are exactly
$\Gamma(\nu+k+1)/\Gamma(\nu+1)$, so the whole brace collapses into one summation.

$$y = A\,J_{\nu}(x) + B\,J_{-\nu}(x)$$

[eq: j-nu-series]

$$J_{\nu}(x) = \left(\frac{x}{2}\right)^{\nu}\left\{\frac{1}{\Gamma(\nu+1)} - \frac{x^{2}}{2^{2}(1!)\,\Gamma(\nu+2)} + \frac{x^{4}}{2^{4}(2!)\,\Gamma(\nu+3)} - \cdots\right\}$$

&nbsp;&nbsp;provided $\nu$ is **not a negative integer**

[eq: j-minus-nu-series]

$$J_{-\nu}(x) = \left(\frac{x}{2}\right)^{-\nu}\left\{\frac{1}{\Gamma(1-\nu)} - \frac{x^{2}}{2^{2}(1!)\,\Gamma(2-\nu)} + \frac{x^{4}}{2^{4}(2!)\,\Gamma(3-\nu)} - \cdots\right\}$$

&nbsp;&nbsp;provided $\nu$ is **not a positive integer**

**Notice** ·BES p2 — $J_{\nu}$ and $J_{-\nu}$ are two **independent** solutions; $A$ and $B$ are the
arbitrary constants.

> [added] **They are independent only when $\nu$ is not an integer**, and the page's two provisos do
> not quite say that. At integer order $\nu = n$ the two collapse into one function,
> $$J_{-n}(x) = (-1)^{n}J_n(x)$$
> — including $\nu = 0$, which neither proviso excludes, where they are literally identical. The
> second solution is then a **Bessel function of the second kind**, $Y_n(x)$, which these notes do
> not cover. §6 of this file uses the $J_{-n} = (-1)^{n}J_n$ identity, so the two statements have to
> be read together. See `00-index.md` § Not in these documents.

*(A first attempt at the $J_{-\nu}$ line, using $\Gamma(\nu+1)$, $\Gamma(\nu+2)$, $\Gamma(\nu+4)$, is
struck through with a wavy line on the page and rewritten correctly. Cancelled text.)*

### 2.1 General summation form ·BES p2

$$J_{\nu}(x) = \left(\frac{x}{2}\right)^{\nu}\sum_{k=0}^{\infty}\frac{(-1)^{k}x^{2k}}{2^{2k}(k!)\,\Gamma(\nu+k+1)} \qquad J_{-\nu}(x) = \left(\frac{x}{2}\right)^{-\nu}\sum_{k=0}^{\infty}\frac{(-1)^{k}x^{2k}}{2^{2k}(k!)\,\Gamma(k-\nu+1)}$$

**OR**, folding the prefactor inside — and **this is the form used in every proof in §5**:

$$\boxed{\;J_{\nu}(x) = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma(\nu+k+1)}\left(\frac{x}{2}\right)^{\nu+2k}\;}$$

$$\boxed{\;J_{-\nu}(x) = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma(k-\nu+1)}\left(\frac{x}{2}\right)^{\,2k-\nu}\;}$$

> ⚠ **VERIFY (V8)** — the page writes the second exponent as a bare $\mathbf{2k}$, with the
> $\mathbf{-\nu}$ missing.
>
> **This is not a clipped edge.** The ink was re-read at 600 dpi: the exponent "2k" is followed by
> clear white space, and the rightmost 40 pixel-columns of the entire page carry no ink at all.
>
> **It changes every value the formula produces.** At $\nu = 0.3$, $x = 0.5$:
> $$\text{as printed} \to 0.7029 \qquad \text{corrected} \to 1.0653 = J_{-0.3}(0.5)$$
> The page contradicts itself: the general form directly above it has the $(x/2)^{-\nu}$ prefactor
> outside the sum, and folding it in is what produces the $-\nu$. The parallel $J_{\nu}$ line on the
> same line of the page correctly reads $(x/2)^{\nu+2k}$.

---

## 3. Integer order ·BES p3

For **order $n$** (an integer), $\Gamma(n+1) = n!$ and the Gammas become factorials:

[eq: j-n-series]

$$J_n(x) = \left(\frac{x}{2}\right)^{n}\left\{\frac{1}{n!} - \frac{1}{(n+1)!}\left(\frac{x}{2}\right)^{2} + \frac{1}{(2!)(n+2)!}\left(\frac{x}{2}\right)^{4} - \cdots\right\}$$

$$= \left(\frac{x}{2}\right)^{n}\left\{\frac{1}{\Gamma(n+1)} - \frac{x^{2}}{2^{2}(1!)\,\Gamma(n+2)} + \frac{x^{4}}{2^{4}(2!)\,\Gamma(n+3)} - \cdots\right\}$$

Two special cases follow.

### 3.1 $J_0(x)$ ·BES p3

[eq: j0-series]

$$J_0(x) = 1 - \frac{x^{2}}{2^{2}(1!)^{2}} + \frac{x^{4}}{2^{4}(2!)^{2}} - \frac{x^{6}}{2^{6}(3!)^{2}} + \cdots$$

$$\text{or}\qquad = 1 - \frac{x^{2}}{2^{2}} + \frac{x^{4}}{2^{2}4^{2}} - \frac{x^{6}}{2^{2}4^{2}6^{2}} + \cdots$$

✓ Verified against `scipy.special.jv` — agrees to 14 significant figures at $x = 3.7$.

### 3.2 $J_1(x)$ ·BES p3

[eq: j1-series]

$$J_1(x) = \frac{x}{2}\left\{\frac{1}{1!} - \frac{1}{(1!)(2!)}\left(\frac{x}{2}\right)^{2} + \frac{1}{(2!)(3!)}\left(\frac{x}{2}\right)^{4} - \cdots\right\}$$

$$= \frac{x}{2} - \frac{x^{3}}{2^{3}(1!)(2!)} + \frac{x^{5}}{2^{5}(2!)(3!)} - \frac{x^{7}}{2^{7}(3!)(4!)} + \cdots$$

✓ Verified against SciPy to 14 significant figures.

### 3.3 The graphs ·BES p4

[fig] $y$-axis marked 1, 0.5, 0, −0.5; $x$-axis marked 2, 4, 6, 8, 10, 12, 14.
$J_0(x)$ starts at 1 and oscillates with decaying amplitude; $J_1(x)$ starts at 0, rises to a first
maximum near $x \approx 1.8$, and oscillates behind it. Both damp out as $x$ grows.

**The notes' own mnemonic:** $J_0$ "looks similar to a **cosine**", $J_1$ "looks similar to a
**sine**". The decay is the difference — Bessel functions are damped oscillations, not periodic
ones.

---

## 4. The six recurrence formulas ·BES p4

All six, as stated on the page. **Every one verified numerically at $n = 2$, $x = 3.7$.**

| | Formula | tag | |
|---|---|---|---|
| **1** | $\dfrac{d}{dx}\Big[x^{n}J_n(x)\Big] = x^{n}J_{n-1}(x)$ | `[eq: recurrence-1]` | ✓ |
| **2** | $\dfrac{d}{dx}\Big[x^{-n}J_n(x)\Big] = -x^{-n}J_{n+1}(x)$ | `[eq: recurrence-2]` | ✓ |
| **3** | $J_n(x) = \dfrac{x}{2n}\Big[J_{n-1}(x) + J_{n+1}(x)\Big]$ | `[eq: recurrence-3]` | ✓ |
| **4** | $J_n'(x) = \dfrac12\Big[J_{n-1}(x) - J_{n+1}(x)\Big]$ | `[eq: recurrence-4]` | ✓ |
| **5** | $J_n'(x) = \dfrac{n}{x}J_n(x) - J_{n+1}(x)$ | `[eq: recurrence-5]` | ✓ |
| **6** | $J_{n+1}(x) = \dfrac{2n}{x}J_n(x) - J_{n-1}(x)$ | `[eq: recurrence-6]` | ✓ |

**The dependency structure, which is the thing to remember:** 1 and 2 are proved from the series;
3, 4, 5 and 6 are all algebra on the two intermediate results

$$\frac{n}{x}J_n + J_n' = J_{n-1} \quad\cdots① \qquad\qquad -\frac{n}{x}J_n + J_n' = -J_{n+1} \quad\cdots②$$

which come from applying the product rule to 1 and 2. **Learn ① and ②; the last four fall out in one
line each.**

---

## 5. The proofs

### 5.1 Proof 1 — $\frac{d}{dx}\big[x^{n}J_n\big] = x^{n}J_{n-1}$ ·BES p5

[derivation] Multiply the series by $x^{n}$:

$$x^{n}J_n(x) = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma(n+k+1)}\cdot\frac{x^{2n+2k}}{2^{n+2k}}$$

Differentiate term by term:

$$\frac{d}{dx}\big[x^{n}J_n\big] = \sum_{k=0}^{\infty}(-1)^{k}\,\frac{2(n+k)}{2^{n+2k}}\cdot\frac{x^{2n+2k-1}}{(k!)\,\Gamma(n+k+1)}$$

**The key step** — use $\Gamma(t+1) = t\Gamma(t)$ on the denominator so the $(n+k)$ cancels:

$$\Gamma(n+k+1) = (n+k)\,\Gamma(n+k)$$

$$= \sum_{k=0}^{\infty}(-1)^{k}\,\frac{x^{2n+2k-1}}{2^{\,n+2k-1}}\cdot\frac{1}{(k!)\,\Gamma(n+k)}$$

Extract $x^{n}$ and recognise what is left:

$$= x^{n}\sum_{k=0}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma\big((n-1)+k+1\big)}\left(\frac{x}{2}\right)^{(n-1)+2k} = x^{n}J_{n-1}(x) \ ✓$$

**Notice what did the work:** the Gamma recurrence of file `01` §2.3. That is the only tool used.

### 5.2 Proof 2 — $\frac{d}{dx}\big[x^{-n}J_n\big] = -x^{-n}J_{n+1}$ ·BES p6

[derivation] Multiply by $x^{-n}$ — this time the $x^{n}$ cancels and only $x^{2k}$ survives:

$$x^{-n}J_n(x) = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma(n+k+1)}\cdot\frac{x^{2k}}{2^{\,n+2k}}$$

Differentiate; the $k = 0$ term dies because of the factor $2k$:

$$= \sum_{k=1}^{\infty}\frac{(-1)^{k}}{(k!)\,\Gamma(n+k+1)}\cdot\frac{(2k)\,x^{2k-1}}{2^{\,n+2k}}$$

Use $k! = k(k-1)!$ to cancel the $k$, then absorb one sign to shift $(-1)^{k} \to -(-1)^{k-1}$:

$$= -x^{-n}\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{(k-1)!\,\Gamma\big((n+1)+(k-1)+1\big)}\left(\frac{x}{2}\right)^{(n+1)+2(k-1)} = -x^{-n}J_{n+1}(x) \ ✓$$

> ⚠ **VERIFY (V9)** — **the page keeps the lower limit at $k = 0$ throughout.** Once $(k-1)!$
> appears that is not defined: the $k = 0$ term would need $(-1)!$. The limit must become $k = 1$ at
> the moment of differentiation, which is legitimate precisely because the factor $2k$ kills the
> $k = 0$ term. The final result is right; the index bookkeeping as written is not — and **an
> examiner reading the printed version would mark the step**. The corrected limits are used above.

### 5.3 Proofs 3–6 — all algebra ·BES p7–9

[derivation] **First, the two workhorses.** Apply the product rule to formula 1:

$$n x^{\,n-1}J_n + x^{n}J_n' = x^{n}J_{n-1} \qquad\xrightarrow{\ \div\,x^{n}\ }\qquad \frac{n}{x}J_n + J_n' = J_{n-1} \quad\cdots①$$

and to formula 2:

$$-n x^{-n-1}J_n + x^{-n}J_n' = -x^{-n}J_{n+1} \qquad\xrightarrow{\ \div\,x^{-n}\ }\qquad -\frac{n}{x}J_n + J_n' = -J_{n+1} \quad\cdots②$$

**Proof 3** ·BES p7 — subtract ② from ①; the $J_n'$ terms cancel:

$$\frac{2n}{x}J_n = J_{n-1} + J_{n+1} \qquad\Longrightarrow\qquad J_n = \frac{x}{2n}\big[J_{n-1} + J_{n+1}\big] \ ✓$$

**Proof 4** ·BES p8 — add ① and ②; the $J_n$ terms cancel:

$$2J_n' = J_{n-1} - J_{n+1} \qquad\Longrightarrow\qquad J_n' = \tfrac12\big[J_{n-1} - J_{n+1}\big] \ ✓$$

**Proof 5** ·BES p8 — rearrange ② alone:

$$J_n' = \frac{n}{x}J_n - J_{n+1} \ ✓$$

**Proof 6** ·BES p9 — equate 4 and 5:

$$\tfrac12\big[J_{n-1} - J_{n+1}\big] = \frac{n}{x}J_n - J_{n+1} \qquad\Longrightarrow\qquad \tfrac12 J_{n+1} = \frac{n}{x}J_n - \tfrac12 J_{n-1}$$

$$J_{n+1} = \frac{2n}{x}J_n - J_{n-1} \ ✓$$

*(6 is 3 rearranged — the notes derive it independently, which is a useful consistency check.)*

---

## 6. Exercise ·BES p9

[exercise]

**1)** Find the value of $J_{-1}(x) + J_1(x)$.

&nbsp;*Solution (notes).* From recurrence 3, rearranged:

$$J_{n-1}(x) + J_{n+1}(x) = \frac{2n}{x}J_n(x)$$

Setting $n = 0$ makes the right-hand side zero:

$$\boxed{\;J_{-1}(x) + J_1(x) = 0\;} \ ✓$$

&nbsp;[added] Verified exactly — $J_{-1} = -J_1$ for integer order, which is the $n = 1$ case of the
general identity $J_{-n} = (-1)^{n}J_n$. **That identity is ours, not the lecturer's**, but it is
why the answer is 0 rather than merely small.

**2)** Prove that $\dfrac{d}{dx}\left[x^{-n}J_n(x)\right] = -x^{-n}J_{n+1}(x)$.

&nbsp;*Answer (notes):* the proof of the second recurrence formula — §5.2 above.

> ⚠ **SCAN (L18)** — the right-hand side of this question is **clipped by the page edge**; only
> "$= -x^{-n}$…" survives. Reconstructed from the answer line, which names the second recurrence
> relation explicitly.

**END** *(the document closes here)*

---

## Flags raised in this file

| ID | Page | What the page shows | Correct form |
|---|---|---|---|
| **V8** | p2 | $J_{-\nu} = \sum\frac{(-1)^{k}}{k!\,\Gamma(k-\nu+1)}\left(\frac x2\right)^{\mathbf{2k}}$ | exponent $\mathbf{2k-\nu}$ — nothing was clipped; changes every value |
| **V9** | p6 | Proof 2 keeps the lower limit $k = 0$ after $(k-1)!$ appears | must be $k = 1$; $(-1)!$ is undefined |
| C15 | p1 | margin header reads "Topic 6" | the filename says Topic 4, and file `01`'s document signs off "End of Topic Four" — the course's internal numbering is inconsistent |
| L17 | p1 | "…order of the" clipped | "Bessel's equation", from the wrap |
| L18 | p9 | Exercise 2's right-hand side clipped | $-x^{-n}J_{n+1}(x)$, from the answer line |

Full detail in `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
