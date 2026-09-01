---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
section: "01 — Gamma and Beta Functions"
source: "GB — 'Topic-1-Gamma-and-beta-functions.pdf', 11 pp. (printed pages 3–13). Typeset LaTeX, full text layer."
file_role: topic
subtopics:
  - "factorial function and its two-case definition"
  - "Gamma function: integral definition and domain"
  - "Gamma properties: Γ(1)=1, recurrence, relation to the factorial, Γ(1/2)=√π"
  - "evaluating Γ at half-integers and at negative arguments"
  - "Beta function: integral definition and relation to Gamma"
  - "Beta symmetry and the (1+x) improper-integral form"
  - "second (trigonometric) form of the Beta function"
  - "three exercise sets, all answers verified"
key_equations:
  [factorial-def, gamma-def, gamma-recurrence, gamma-factorial, gamma-half,
   beta-def, beta-gamma, beta-symmetry, beta-improper-form, beta-trig-form]
prerequisites: ["integration by parts", "improper integrals", "substitution"]
leads_to: ["02 — Continuous Random Variables and the Beta Distribution",
          "03 — The Binomial Theorem (factorials)",
          "06 — Bessel's Equation (the Gamma recurrence drives every proof)"]
verification_flags: 6   # 2 substantive (V1–V2) + 4 cosmetic (C1–C4)
tags: [gamma-function, beta-function, factorial, recurrence, half-integer,
       improper-integral, trigonometric-form, emt3101]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set in the notes ·
  [fig] figure described from the rendered page · [added] not in the notes — supplied here ·
  ·GB pN provenance (the document's own PRINTED page number, = PDF page + 2) ·
  ⚠ VERIFY = flagged suspected source error, see _verification-log.md -->

# 01 — Gamma and Beta Functions

**Source:** GB, 11 PDF pages carrying printed page numbers **3–13**. Citations below use the
**printed** number, which is what appears in the page footer.

This is the only typeset document in the subject — the other five are handwritten scans. It has a
complete text layer, so the transcription is exact and there is no reading uncertainty anywhere in
this file. What errors it has are the author's, not the scanner's.

The argument runs: extend the factorial to non-integers (Gamma), establish four properties, then
build a second function from it (Beta) and give three equivalent forms of that. Everything after
§2.2 leans on the recurrence $\Gamma(n+1) = n\Gamma(n)$.

> **Reliability note.** Two substantive defects, both **arithmetic in a stated answer while the
> symbolic working above it is correct** — see V1 and V2. That pattern is the thing to watch in this
> document: trust the algebra, re-check the decimal.

---

> **Equation numbers below — $(1)$, $(2)$, $(3)$, $(7)$, $(10)$, $(15)$ … — are the document's
> own.** They are not consecutive here because the source numbers every displayed line, including
> intermediate steps this file does not repeat. A gap is not a lost equation.

---

## 1. The factorial function

### 1.1 Definition ·GB p3

[def] [eq: factorial-def] For a non-negative integer $n$, the factorial $n!$ is

$$n! = n(n-1)(n-2)\times\cdots\times3\times2\times1, \qquad n > 0 \tag{1}$$

with $0! = 1$ and $1! = 1$ by definition. The notes mark the $0!=1$ case "to be proved later"; the
proof arrives in §2.2 as a corollary of the Gamma recurrence.

[eq] Written as two cases:

$$n! = \begin{cases} n(n-1)(n-2)\cdots3\times2\times1 & n = 1,2,3,4,\dots \\[1mm] 1 & n = 0\end{cases} \tag{2}$$

Worked values given on the page: $2! = 2$, $4! = 24$, $10! = 3\,628\,800$.

> ⚠ **VERIFY (C3)** — the page introduces them with "For **axample**:". Typo only.

### 1.2 Why it matters ·GB p3

The notes motivate the factorial through **permutations and combinations** — the number of ways of
arranging or selecting objects without listing them, and hence through to probability. The example
given: four pictures hung one after another admit $4! = 24$ orderings.

---

## 2. The Gamma function

### 2.1 Definition ·GB p4

[def] The Gamma function is the **continuous extension of the factorial**. Where $n!$ is defined
only on the non-negative integers, $\Gamma$ is defined for every complex argument except the
non-positive integers.

[eq: gamma-def]

$$\boxed{\;\Gamma(n) = \int_0^{\infty} e^{-x}x^{\,n-1}\,dx, \qquad n > 0\;} \tag{3}$$

- $n$ — the argument (dimensionless); $x$ — the integration variable
- The integral converges at the upper limit because $e^{-x}$ beats any power of $x$, and at the
  lower limit provided $n > 0$.

**Where it shows up** ·GB p4 — the notes list time-to-failure of equipment, telecommunication load
levels, rainfall, insurance claims and loan defaults: quantities that are always positive and
skewed. That is the shape a Gamma distribution has.

### 2.2 Property 1 — $\Gamma(1) = 1$ ·GB p4

[derivation] Put $n = 1$ in (3):

$$\Gamma(1) = \int_0^\infty e^{-x}x^{0}\,dx = \int_0^\infty e^{-x}\,dx = \big[-e^{-x}\big]_0^\infty$$

$$= -\left(\lim_{x\to\infty}\frac{1}{e^{x}}\right) + \frac{1}{e^{0}} = 0 + 1 = 1$$

The notes state that the companion result $\Gamma(0) = \infty$ is not proved here.

### 2.3 Property 2 — the recurrence ·GB p4–5

[eq: gamma-recurrence] The single most-used result in the whole topic:

$$\boxed{\;\Gamma(n+1) = n\,\Gamma(n), \qquad n > 0\;} \tag{4}$$

[derivation] From (3), $\Gamma(n+1) = \int_0^\infty e^{-x}x^{n}\,dx$. Integrate by parts with

$$u = x^{n} \Rightarrow du = n x^{\,n-1}dx, \qquad dv = e^{-x}dx \Rightarrow v = -e^{-x}$$

$$\Gamma(n+1) = \Big[-e^{-x}x^{n}\Big]_0^\infty + n\int_0^\infty e^{-x}x^{\,n-1}\,dx \tag{7}$$

The boundary term vanishes at both ends when $n > 0$: at $x = 0$ because $x^{n}\to 0$, and at
$x\to\infty$ because $e^{-x}$ decays faster than $x^{n}$ grows. What is left is the definition of
$\Gamma(n)$:

$$\Gamma(n+1) = n\underbrace{\int_0^\infty e^{-x}x^{\,n-1}dx}_{\Gamma(n)} = n\,\Gamma(n)$$

**Rearranged form**, used constantly for negative arguments in §2.6:

$$\Gamma(n) = \frac{\Gamma(n+1)}{n}$$

### 2.4 Property 3 — Gamma *is* the factorial, shifted ·GB p5

[eq: gamma-factorial]

$$\boxed{\;\Gamma(n+1) = n! \qquad n \ge 0,\ n \in \mathbb{Z}\;} \tag{10}$$

[derivation] For $n = 0$: $\Gamma(1) = 1 = 0!$ — which is where the "$0! = 1$ by definition" of §1.1
stops being a definition and becomes a consequence. For $n > 0$, apply (4) repeatedly:

$$\Gamma(n+1) = n\Gamma(n) = n(n-1)\Gamma(n-1) = n(n-1)(n-2)\Gamma(n-2) = \cdots$$
$$= n(n-1)(n-2)\cdots1\cdot\Gamma(1) = n!$$

**The off-by-one is the thing that costs marks.** $\Gamma(6) = 5!$, not $6!$.

> [ex] **Example 1.2.1** ·GB p5 — Evaluate $\Gamma(2)$, $\Gamma(3)$, $\Gamma(6)$.
>
> $$\Gamma(2) = 1! = 1 \qquad \Gamma(3) = 2! = 2 \qquad \Gamma(6) = 5! = 120$$
>
> All three verified.

### 2.5 Property 4 — the half-integer seed ·GB p6

[eq: gamma-half]

$$\boxed{\;\Gamma\!\left(\tfrac12\right) = \sqrt{\pi}\;}$$

The notes state this and say explicitly that the proof is not shown. Exercise 2.4 (§5.2) asks the
reader to produce it.

Combined with the recurrence, this generates every half-integer value.

> [ex] **Example 1.2.2** ·GB p6 — Determine (i) $\Gamma(5/2)$, (ii) $\Gamma(9/2)$, (iii) $(4.5)!$
>
> **(i)** $\displaystyle \Gamma\!\left(\tfrac52\right) = \tfrac32\Gamma\!\left(\tfrac32\right) = \tfrac32\cdot\tfrac12\Gamma\!\left(\tfrac12\right) = \tfrac34\sqrt\pi = 1.32934$ ✓
>
> **(ii)** $\displaystyle \Gamma\!\left(\tfrac92\right) = \tfrac72\cdot\tfrac52\cdot\tfrac32\cdot\tfrac12\sqrt\pi = \frac{105}{16}\sqrt\pi$
>
> ⚠ **VERIFY (V1)** — the page prints this as $\mathbf{16.8114}$. The symbolic form
> $\frac{105}{16}\sqrt\pi$ is **correct**; its value is $\mathbf{11.6317}$.
> The page contradicts itself one line later: part (iii) uses this same quantity to reach
> $52.3428$, and $52.3428 / 4.5 = 11.6317$. **Learn 11.6317.**
>
> **(iii)** $\displaystyle (4.5)! = \Gamma(5.5) = \tfrac92\cdot\tfrac72\cdot\tfrac52\cdot\tfrac32\cdot\tfrac12\sqrt\pi = 52.3428$ ✓

### 2.6 Negative arguments ·GB p7

Use the rearranged recurrence $\Gamma(n) = \Gamma(n+1)/n$ and step *upwards* until the argument is
positive.

> [ex] **Example 1.2.3** ·GB p7 — Evaluate (i) $\Gamma(-3/2)$, (ii) $\Gamma(-5/2)$.
>
> **(i)** First get $\Gamma(-1/2)$:
> $$\Gamma\!\left(-\tfrac12\right) = \frac{\Gamma\!\left(\tfrac12\right)}{-\tfrac12} = -2\sqrt\pi$$
> Then
> $$\Gamma\!\left(-\tfrac32\right) = \frac{\Gamma\!\left(-\tfrac12\right)}{-\tfrac32} = -\tfrac23\left(-2\sqrt\pi\right) = \frac{4\sqrt\pi}{3} = 2.36327 \ ✓$$
>
> **(ii)** Left as a class exercise on the page — **not worked in the notes**.
>
> [added] One further step of the same recurrence gives
> $$\Gamma\!\left(-\tfrac52\right) = \frac{\Gamma\!\left(-\tfrac32\right)}{-\tfrac52} = -\tfrac25\cdot\frac{4\sqrt\pi}{3} = -\frac{8\sqrt\pi}{15} = -0.945309$$
> Verified numerically. **This is ours, not the lecturer's.**

---

## 3. Exercise set 1 ·GB p7–8

[exercise] As printed, with the notes' own solutions where given.

**1.** Evaluate the following integrals.

&nbsp;&nbsp;**(a)** $\displaystyle\int_0^\infty x^{3}e^{-x}\,dx$

&nbsp;&nbsp;*Solution (notes).* Compare with (3): $n - 1 = 3 \Rightarrow n = 4$, so

$$\int_0^\infty x^{3}e^{-x}dx = \Gamma(4) = 3! = 6 \ ✓$$

&nbsp;&nbsp;**(b)** $\displaystyle\int_0^\infty x^{6}e^{-2x}\,dx$ &nbsp;**Ans:** $5.625$ ✓

&nbsp;&nbsp;[added] *Method for (b), which the page does not show:* substitute $t = 2x$ to get
$\frac{1}{2^{7}}\int_0^\infty t^{6}e^{-t}dt = \frac{\Gamma(7)}{128} = \frac{720}{128} = 5.625$.

&nbsp;&nbsp;**(c)** Verify 1(a) using integration by parts. *(Unworked on the page.)*

**2.** By letting $x = y^{2}$, show that $\displaystyle\Gamma(n) = 2\int_0^\infty e^{-y^{2}}y^{\,2n-1}dy$.

&nbsp;&nbsp;*Solution (notes).* $x = y^2 \Rightarrow dx = 2y\,dy$; the limits are unchanged
($0\to0$, $\infty\to\infty$). Substituting into (3):

$$\Gamma(n) = \int_0^\infty e^{-y^{2}}\left(y^{2}\right)^{n-1}2y\,dy = 2\int_0^\infty e^{-y^{2}}y^{\,2n-1}dy \ ✓$$

**3.** By letting $e^{-x} = y$, show that $\displaystyle\Gamma(n) = \int_0^1\left(\ln\tfrac1y\right)^{n-1}dy$. *(Unworked on the page.)*

---

## 4. Exercise set 2 ·GB p8

[exercise]

**1. (a)** Show clearly that $\Gamma(x+1) \equiv x\,\Gamma(x)$ for $x \neq 0$, $x \notin -\mathbb{N}$.
&nbsp;&nbsp;**(b)** Hence show that $\Gamma(n+1) \equiv n!$ for $n \in \mathbb{N}$.

*(Both are §2.3 and §2.4 above, restated as exercises.)*

**2.** Evaluate each of the following. All five answers verified:

| | Expression | Answer | |
|---|---|---|---|
| (a) | $\dfrac{\Gamma(6)}{2\,\Gamma(3)}$ | $30$ | ✓ |
| (b) | $\dfrac{\Gamma(5/2)}{\Gamma(1/2)}$ | $\tfrac34$ | ✓ |
| (c) | $\dfrac{\Gamma(3)\,\Gamma(2.5)}{\Gamma(5.5)}$ | $\tfrac{16}{315}$ | ✓ |
| (d) | $\dfrac{6\,\Gamma(8/3)}{5\,\Gamma(2/3)}$ | $\tfrac43$ | ✓ |
| (e) | $\dfrac{\Gamma(-1/2)}{\Gamma(1/2)}$ | $-2$ | ✓ |

**3.** Find the exact value of $\displaystyle\int_0^\infty x^{3}e^{-4x}dx$ in rational form.
&nbsp;**Ans:** $\tfrac{3}{128}$ ✓

**4.** Given $\displaystyle I = 2\int_0^\infty e^{-x^{2}}dx$ and $\displaystyle I = 2\int_0^\infty e^{-y^{2}}dy$,
by finding an expression for $I$, show that $\Gamma\!\left(\tfrac12\right) = \sqrt\pi$.

> ⚠ **VERIFY (C1)** — should read "an expression for $I^{\mathbf{2}}$". The method multiplies the
> two integrals into a double integral over the first quadrant and switches to polar coordinates;
> that is the only reason the question bothers to give the same integral twice, once in $x$ and once
> in $y$. A dropped superscript.

---

## 5. The Beta function

### 5.1 Definition ·GB p9

[def] A second definite integral built from the same family, with **two** parameters.

[eq: beta-def]

$$\boxed{\;B(m,n) = \int_0^1 x^{\,m-1}(1-x)^{\,n-1}dx, \qquad m > 0,\ n > 0\;} \tag{15}$$

The symbol $B$ is a Greek capital beta, not a Roman B. $m$ and $n$ are real, not necessarily
integers.

### 5.2 Property 1 — Beta in terms of Gamma ·GB p9

[eq: beta-gamma] The bridge between the two functions, and the way essentially every Beta problem is
actually evaluated:

$$\boxed{\;B(m,n) = \frac{\Gamma(m)\,\Gamma(n)}{\Gamma(m+n)}\;} \tag{16}$$

> [ex] ·GB p9 — $\displaystyle B(5,2) = \frac{\Gamma(5)\Gamma(2)}{\Gamma(7)} = \frac{4!\times1!}{6!} = \frac{1}{30}$
>
> Checked against the definition directly:
> $$B(5,2) = \int_0^1 x^{4}(1-x)\,dx = \left[\frac{x^{5}}{5} - \frac{x^{6}}{6}\right]_0^1 = \frac1{30} \ ✓$$

### 5.3 Property 2 — symmetry ·GB p9

[eq: beta-symmetry]

$$B(m,n) = B(n,m) \tag{17}$$

Immediate from (16), since $\Gamma(m)\Gamma(n)$ is symmetric and $\Gamma(m+n)$ is unchanged.
Illustrated on the page with $B(2,5) = \frac{1!\times4!}{6!} = \frac1{30} = B(5,2)$ ✓

### 5.4 Property 3 — the improper-integral form ·GB p9

[eq: beta-improper-form]

$$\boxed{\;B(m,n) = \int_0^\infty \frac{x^{\,m-1}}{(1+x)^{\,m+n}}\,dx, \qquad m,n > 0\;} \tag{18}$$

**How to use it:** read $m$ off the numerator exponent ($m-1$), then read $n$ off the denominator
exponent ($m+n$).

> [ex] **Example 1.3.1** ·GB p10 — Determine each integral.
>
> **(a)** $\displaystyle\int_0^\infty\frac{x^{2}}{(1+x)^{10}}dx$: &nbsp; $m-1 = 2 \Rightarrow m = 3$, and $m+n = 10 \Rightarrow n = 7$.
> $$= B(3,7) = \frac{\Gamma(3)\Gamma(7)}{\Gamma(10)} = \frac{2!\;6!}{9!} = \frac{1}{252} \ ✓$$
>
> **(b)** $\displaystyle\int_0^\infty\frac{x^{6}}{(1+x)^{10}}dx$: &nbsp; $m = 7$, $n = 3$.
> $$= B(7,3) = \frac{1}{252} = B(3,7) \ ✓ \quad\text{(symmetry, §5.3)}$$
>
> **(c)** $\displaystyle\int_0^\infty\frac{x^{2}\left(1+x^{4}\right)}{(1+x)^{10}}dx$ — split the numerator:
> $$= B(3,7) + B(7,3) = 2B(3,7) = \frac{1}{126} \ ✓$$

### 5.5 Property 4 — the trigonometric (second) form ·GB p11

[eq: beta-trig-form]

$$\boxed{\;\frac{B(m,n)}{2} = \int_0^{\pi/2}(\sin\theta)^{\,2m-1}(\cos\theta)^{\,2n-1}d\theta\;} \tag{19}$$

[derivation] Substitute $x = \sin^{2}\theta$, so $dx = 2\sin\theta\cos\theta\,d\theta$, and the
limits $x: 0 \to 1$ become $\theta: 0 \to \pi/2$. In (15):

$$B(m,n) = \int_0^{\pi/2}\left(\sin^{2}\theta\right)^{m-1}\left(\cos^{2}\theta\right)^{n-1}2\sin\theta\cos\theta\,d\theta$$

$$= 2\int_0^{\pi/2}(\sin\theta)^{\,2m-1}(\cos\theta)^{\,2n-1}d\theta$$

**Reading off $m$ and $n$:** if the integrand is $\sin^{p}\theta\cos^{q}\theta$ then
$p = 2m-1$ and $q = 2n-1$, i.e. $m = \frac{p+1}{2}$, $n = \frac{q+1}{2}$. Non-integer values are
fine — see example (b).

> [ex] ·GB p12 — Evaluate:
>
> **(a)** $\displaystyle\int_0^{\pi/2}\sin^{7}\theta\cos^{3}\theta\,d\theta$: &nbsp; $7 = 2m-1 \Rightarrow m = 4$; $3 = 2n-1 \Rightarrow n = 2$.
> $$= \tfrac12 B(4,2) = \frac{\Gamma(4)\Gamma(2)}{2\,\Gamma(6)} = \frac{1}{40} \ ✓$$
>
> **(b)** $\displaystyle\int_0^{\pi/2}\sin^{5}\theta\,d\theta$ — write it as $\sin^{5}\theta\cos^{0}\theta$, so $m = 3$ and $n = \tfrac12$.
> $$= \tfrac12 B\!\left(3,\tfrac12\right) = \frac{\Gamma(3)\,\Gamma(1/2)}{2\,\Gamma(7/2)} = \frac{8}{15} \ ✓$$

---

## 6. Exercise set 3 ·GB p12–13

[exercise]

**1.** Using the properties of the Beta and Gamma functions, evaluate:

&nbsp;&nbsp;**(a)** $\displaystyle\int_0^\infty\frac{x^{2}}{\left(1+x^{2}\right)^{7/2}}dx$ &nbsp;*Hint: let $x^{2} = t$.*
&nbsp;&nbsp;**Solution:** $\dfrac12\dfrac{\Gamma(3/2)\Gamma(2)}{\Gamma(7/2)} = 0.13333$ ✓

&nbsp;&nbsp;**(b)** $\displaystyle\int_0^{\pi/2}\cos^{5}\theta\,d\theta$ &nbsp;**Solution:** $\dfrac{8}{15}$ ✓

&nbsp;&nbsp;**(c)** $\displaystyle\int_0^{\pi/2}\cos^{4}3\theta\,\sin^{2}6\theta\,d\theta$
&nbsp;*Hint: let $3\theta = t$ and use $2\sin t\cos t = \sin 2t$.*

&nbsp;&nbsp;**Solution given:** $\dfrac43\left[\dfrac{\Gamma(3/2)\,\Gamma(7/2)}{2\,\Gamma(5)}\right] = 0.08181$

> ⚠ **VERIFY (V2)** — **the printed answer is one third of the true value.** The integral is
> $\mathbf{0.24544}$.
>
> The substitution $3\theta = t$ carries $\theta \in [0, \pi/2]$ onto
> $t \in [0, \mathbf{3\pi/2}]$, not $[0,\pi/2]$ — but the Beta form quoted is only valid over
> $[0,\pi/2]$. Since $\sin^{2}t\cos^{6}t$ has period $\pi$ and is symmetric about $\pi/2$, the
> interval $[0,3\pi/2]$ contains exactly **three** copies of $[0,\pi/2]$:
> $$\frac43\int_0^{3\pi/2}\sin^{2}t\cos^{6}t\,dt = 3\times 0.08181 = 0.24544$$
> Verified by direct numerical integration of the original integrand.

**2.** Using the second form of the Beta function, show that

$$\int_0^{\pi/2}\sin^{p}\theta\cos^{q}\theta\,d\theta = \frac12 B\!\left(\frac{p+1}{2},\ \frac{q+1}{2}\right)$$

*(This is §5.5's read-off rule, stated as an exercise. Unworked on the page.)*

**3.** Find the exact value of $\displaystyle\int_0^\infty 2\sqrt{x}\,e^{-x^{2}}dx$ in the form $\Gamma(k)$.
*Hint: let $t = x^{2}$.* &nbsp;**Ans:** $\Gamma\!\left(\tfrac34\right) = 1.22542$ ✓

**4.** *(as printed)* "Using Beta-function techniques, **show that find** the exact value of"
$\displaystyle\int_0^\infty\frac{1}{1+x^{2}}dx$. *Hint: let $u = x^{2}$.* &nbsp;**Ans:** $\dfrac\pi2$ ✓

> ⚠ **VERIFY (C4)** — "show that find" carries one verb too many; read it as "find". Quoted as
> printed here so you recognise it if the same wording reaches a paper.

**5.** Using Beta-function techniques, find the exact value of $\displaystyle\int_0^1 x^{4}\sqrt{1-x^{2}}\,dx$.
&nbsp;**Ans:** $\dfrac{\pi}{32}$ ✓

The document closes here with the line **"\*\* End of Topic Four \*\*"** ·GB p13.

> ⚠ **VERIFY (C2)** — this is Topic **1** by filename. The course's internal topic numbering does
> not match its filenames anywhere; see `00-index.md` § The topic numbering does not match the
> filenames. **Match by content, never by number.**

---

## Flags raised in this file

| ID | Page | What the page prints | Correct form |
|---|---|---|---|
| **V1** | p6 | $\Gamma(9/2) = 16.8114$ | $11.6317$ |
| **V2** | p12 | Exercise 3.1(c) $= 0.08181$ | $0.24544$ — three times larger |
| C1 | p8 | Exercise 2.4, "an expression for $I$" | $I^{2}$ |
| C2 | p13 | signs off "** End of Topic Four **" | this is Topic 1 by filename; the course's internal numbering does not match |
| C3 | p3 | "For axample:" | "For example" |
| C4 | p12 | Exercise 3.4, "show that find the exact value of" | one verb too many |

Full detail, with the reasoning, in `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
