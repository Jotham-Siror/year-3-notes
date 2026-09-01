---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
section: "05 — Higher Derivatives and Leibniz Theorem"
source: "LEI — 'Topic-3.3-Leibniz Theorem.pdf', 9 pp., handwritten, 300 dpi scan, no text layer. Marked '3.3' in the notes."
file_role: topic
subtopics:
  - "trigonometric identity reference sheet"
  - "nth derivative of e^{ax}, sin ax, cos ax, x^a, sinh ax, cosh ax, ln ax"
  - "the phase-shift trick that makes sin and cos differentiable n times"
  - "Leibniz theorem for the nth derivative of a product"
  - "choosing which factor is u and which is v"
  - "worked products: x²e^{3x} and x⁴ sin x"
key_equations:
  [nth-exp, nth-sin, nth-cos, nth-power, nth-sinh, nth-cosh, nth-log,
   leibniz-theorem]
prerequisites: ["03 — The Binomial Theorem (the coefficients are the same ones)", "product rule", "trigonometric identities"]
leads_to: []   # a leaf — nothing later in the course depends on this file
verification_flags: 3   # 1 substantive (V7) + 2 cosmetic (C13–C14); plus scan limits L12–L16
tags: [higher-derivatives, nth-derivative, leibniz-theorem, product-rule,
       binomial-coefficients, hyperbolic-functions, trigonometric-identities,
       emt3101]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set in the notes ·
  [fig] figure described from the rendered page · [added] not in the notes — supplied here ·
  ·LEI pN provenance (scan page — these pages carry no printed numbers) ·
  ⚠ VERIFY = flagged suspected source error, see _verification-log.md -->

# 05 — Higher Derivatives and Leibniz Theorem

**Source:** LEI, 9 handwritten pages, numbered **3.3** — the third part of section 3, *Power Series
Method of solving O.D.E*.

Two halves. **§2 is a catalogue**: the $n$-th derivative of seven standard functions, each found by
differentiating three times and spotting the pattern. **§3 is the theorem** that lets you do the
same for a *product*, and it turns out to be the binomial expansion of file `03` with the powers
reinterpreted as derivatives.

> **Reliability note.** One substantive defect (V7) — a cofunction identity written without its
> minus sign, on the reference page you would go back to. Every worked example in this file was
> re-derived by direct symbolic differentiation and all seven match.

---

## 1. Trigonometric identity sheet ·LEI p1–2

The notes open with a reference block. Reproduced here in corrected form; the one discrepancy is
flagged.

**Reciprocal**

$$\sin\theta = \frac{1}{\csc\theta} \qquad \cos\theta = \frac{1}{\sec\theta} \qquad \tan\theta = \frac{1}{\cot\theta}$$

**Quotient**

$$\tan\theta = \frac{\sin\theta}{\cos\theta} \qquad \cot\theta = \frac{\cos\theta}{\sin\theta}$$

**Pythagorean**

$$\sin^{2}\theta + \cos^{2}\theta = 1 \qquad \sec^{2}\theta - \tan^{2}\theta = 1 \qquad \csc^{2}\theta - \cot^{2}\theta = 1$$

**Even and odd**

$$\sin(-\theta) = -\sin\theta \qquad \cos(-\theta) = \cos\theta \qquad \tan(-\theta) = -\tan\theta$$
$$\cot(-\theta) = -\cot\theta \qquad \csc(-\theta) = -\csc\theta \qquad \sec(-\theta) = \sec\theta$$

**Sum and difference** ·LEI p2

$$\sin(\theta \pm \phi) = \sin\theta\cos\phi \pm \cos\theta\sin\phi$$
$$\cos(\theta \pm \phi) = \cos\theta\cos\phi \mp \sin\theta\sin\phi$$
$$\tan(\theta \pm \phi) = \frac{\tan\theta \pm \tan\phi}{1 \mp \tan\theta\tan\phi}$$

**Cofunction** ·LEI p2 &nbsp;*(where $\tfrac\pi2$ rad = 90°)*

$$\sin\left(\tfrac\pi2 - \theta\right) = \cos\theta \qquad\text{or}\qquad \sin\left(\theta + \tfrac\pi2\right) = \cos\theta$$
$$\cos\left(\tfrac\pi2 - \theta\right) = \sin\theta \qquad\text{or}\qquad \cos\left(\theta + \tfrac\pi2\right) = \boxed{-\sin\theta}$$
$$\tan\left(\tfrac\pi2 - \theta\right) = \cot\theta \qquad \cot\left(\tfrac\pi2 - \theta\right) = \tan\theta$$
$$\csc\left(\tfrac\pi2 - \theta\right) = \sec\theta \qquad \sec\left(\tfrac\pi2 - \theta\right) = \csc\theta$$

> ⚠ **VERIFY (V7)** — the page writes the second cofunction identity as
> $\cos\left(\theta + \tfrac\pi2\right) = \sin\theta$. **It is $-\sin\theta$.** Check it at
> $\theta = 0$: $\cos(\pi/2) = 0$, fine; at $\theta = \pi/2$: $\cos(\pi) = -1$ while
> $\sin(\pi/2) = +1$. This is the reference sheet you would return to mid-problem, and the sign
> propagates straight into §2's $\cos ax$ results — so learn the minus.
>
> The first form on the same line, $\cos\left(\tfrac\pi2 - \theta\right) = \sin\theta$, **is
> correct**. Only the shifted version is wrong.

> ⚠ **SCAN (L12)** — the right-hand column of the p1 identity block sits at the edge of the scan
> and loses the last character or two of each line. The entries above are reconstructed from the
> standard identities — each unambiguous from what is visible, but not fully read from ink.

---

## 2. $n$-th derivatives of standard functions ·LEI p1–5

**The method throughout:** differentiate three times, look for the trend, write the general term.

### 2.1 $y = e^{ax}$ ·LEI p1

$$y' = ae^{ax}, \qquad y'' = a^{2}e^{ax}, \qquad y''' = a^{3}e^{ax}, \ \dots$$

[eq: nth-exp]

$$\boxed{\;y^{(n)} = a^{n}e^{ax}\;}$$

> [ex] $y = 3e^{2x} \Rightarrow y^{(7)} = 3\left(2^{7}\right)e^{2x} = 384\,e^{2x}$ ✓

### 2.2 $y = \sin ax$ ·LEI p2

The trick is to write each derivative as a **phase shift** rather than as an alternating sign:

$$y' = a\cos ax = a\sin\left(ax + \frac{\pi}{2}\right)$$
$$y'' = -a^{2}\sin ax = a^{2}\sin\left(ax + \frac{2\pi}{2}\right)$$
$$y''' = -a^{3}\cos ax = a^{3}\sin\left(ax + \frac{3\pi}{2}\right)$$

[eq: nth-sin]

$$\boxed{\;y^{(n)} = a^{n}\sin\left(ax + \frac{n\pi}{2}\right)\;}$$

**Each differentiation advances the phase by $\pi/2$.** That is the whole content of the result, and
it is why the $-1$'s disappear.

> ⚠ **VERIFY (C13)** — the $y'''$ line is written $-a^{3}\cos x$, dropping the $a$ inside the
> cosine. The equivalent phase form on the same line and the general result below are both correct.

> [ex] $y = \sin3x \Rightarrow y^{(5)} = 3^{5}\sin\left(3x + \frac{5\pi}{2}\right) = 243\cos3x$ ✓
>
> **(L13)** — a middle bracket in this line is written over itself and its numerator cannot be read.
> The first and last expressions are clear and consistent, so the result stands.

### 2.3 $y = \cos ax$ ·LEI p3

$$y' = -a\sin ax = a\cos\left(ax + \frac{\pi}{2}\right)$$
$$y'' = -a^{2}\cos ax = a^{2}\cos\left(ax + \frac{2\pi}{2}\right)$$
$$y''' = a^{3}\sin ax = a^{3}\cos\left(ax + \frac{3\pi}{2}\right)$$

[eq: nth-cos]

$$\boxed{\;y^{(n)} = a^{n}\cos\left(ax + \frac{n\pi}{2}\right)\;}$$

> [ex] $y = 4\cos2x \Rightarrow y^{(6)} = 4\left(2^{6}\right)\cos\left(2x + 3\pi\right) = -256\cos2x$ ✓

### 2.4 $y = x^{a}$ ·LEI p3

$$y' = ax^{\,a-1}, \qquad y'' = a(a-1)x^{\,a-2}, \qquad y''' = a(a-1)(a-2)x^{\,a-3}, \ \dots$$

$$y^{(n)} = a(a-1)(a-2)\cdots\underbrace{(a-n+1)}_{[a-(n-1)]}\,x^{\,a-n}$$

[eq: nth-power] which for a positive integer $a$ closes into

$$\boxed{\;y^{(n)} = \frac{a!}{(a-n)!}\,x^{\,a-n}\;}$$

> [ex] $y = 2x^{6} \Rightarrow y^{(4)} = 2\cdot\frac{6!}{2!}x^{2} = 720x^{2}$ ✓ &nbsp;*(margin: $a=6$, $n=4$)*

### 2.5 $y = \sinh ax$ ·LEI p4

$$y' = a\cosh ax, \qquad y'' = a^{2}\sinh ax, \qquad y''' = a^{3}\cosh ax, \ \dots$$

Because $\sinh ax$ is **not periodic**, the phase-shift trick of §2.2 is unavailable. The notes
instead use a parity switch:

[eq: nth-sinh]

$$\boxed{\;y^{(n)} = \frac{a^{n}}{2}\Big\{\big[1 + (-1)^{n}\big]\sinh ax + \big[1 - (-1)^{n}\big]\cosh ax\Big\}\;}$$

**How to read it:** the bracket $[1 + (-1)^n]$ is 2 for even $n$ and 0 for odd $n$; the other is the
reverse. So the formula is just "even derivatives give $\sinh$, odd give $\cosh$" written as one
expression.

> [ex] $y = \sinh2x$, $n = 5$:
> $$y^{(5)} = \frac{2^{5}}{2}\Big\{[0]\sinh2x + [2]\cosh2x\Big\} = 32\cosh2x \ ✓$$

> ⚠ **SCAN (L14)** — three lines of the surrounding paragraph lose their last two or three words
> to the clipped right margin. The reading is reconstructed from context — unambiguous, but not read
> from ink.

### 2.6 $y = \cosh ax$ ·LEI p4–5

$$y' = a\sinh ax, \qquad y'' = a^{2}\cosh ax, \qquad y''' = a^{3}\sinh ax, \ \dots$$

[eq: nth-cosh] The same formula with the brackets swapped:

$$\boxed{\;y^{(n)} = \frac{a^{n}}{2}\Big\{\big[1 - (-1)^{n}\big]\sinh ax + \big[1 + (-1)^{n}\big]\cosh ax\Big\}\;}$$

> [ex] $y = \tfrac19\cosh3x$, $n = 7$:
> $$y^{(7)} = \frac19\cdot\frac{3^{7}}{2}\Big\{[2]\sinh3x + [0]\cosh3x\Big\} = \frac{3^{7}}{9}\sinh3x = 243\sinh3x \ ✓$$

### 2.7 $y = \ln ax$ ·LEI p5

$$y' = \frac1x, \qquad y'' = -\frac{1}{x^{2}}, \qquad y''' = \frac{2}{x^{3}}, \ \dots$$

[eq: nth-log]

$$\boxed{\;y^{(n)} = (-1)^{\,n-1}\frac{(n-1)!}{x^{n}}\;}$$

**Note that $a$ has vanished** — it drops out at the very first derivative, since
$\ln ax = \ln a + \ln x$ and $\ln a$ is a constant.

> [ex] $y = \ln5x \Rightarrow y^{(6)} = (-1)^{5}\frac{5!}{x^{6}} = -\frac{120}{x^{6}}$ ✓

> ⚠ **VERIFY (C14)** — this item is numbered **6)** on the page, repeating the number of the
> $\cosh ax$ item above it. It should be 7).

---

## 3. Leibniz theorem

### 3.1 The pattern ·LEI p6

[derivation] If $y = uv$ with $u$ and $v$ both functions of $x$, apply the product rule repeatedly:

$$y' = u'v + uv'$$
$$y'' = u''v + 2u'v' + uv''$$
$$y''' = u'''v + 3u''v' + 3u'v'' + uv'''$$
$$y^{(4)} = u^{(4)}v + 4u^{(3)}v^{(1)} + 6u^{(2)}v^{(2)} + 4u^{(1)}v^{(3)} + uv^{(4)}$$

Three observations the notes draw out:

&nbsp;&nbsp;**i)** the order of the derivative on $u$ **decreases** by 1 from left to right
&nbsp;&nbsp;**ii)** the order on $v$ **increases** by 1 from left to right
&nbsp;&nbsp;**iii)** the coefficients $1, 4, 6, 4, 1$ are the ordinary **binomial coefficients**

⇒ So $(uv)^{(n)}$ may be obtained by expanding $(u+v)^{n}$ by the **binomial theorem**, with the
"powers" reinterpreted as **derivatives**.

[eq: leibniz-theorem]

$$\boxed{\;y^{(n)} = (uv)^{(n)} = u^{(n)}v + n\,u^{(n-1)}v^{(1)} + \frac{n(n-1)}{2!}u^{(n-2)}v^{(2)} + \frac{n(n-1)(n-2)}{3!}u^{(n-3)}v^{(3)} + \cdots\;}$$

**This is file `03`'s equation (1) with $a \to u$, $x \to v$ and every exponent read as a derivative
order.** If you can expand a binomial you can apply Leibniz.

### 3.2 Choosing $u$ and $v$ ·LEI p7

The rule that makes the series terminate:

- **$u$** — the factor whose $n$-th derivative is **readily known** (from §2's catalogue)
- **$v$** — the factor whose derivative **reduces to zero** after a few stages

Get this the wrong way round and the series never ends.

> [ex] **Example 1** ·LEI p7 — Determine $y^{(n)}$ for $y = x^{2}e^{3x}$.
>
> Take $u = e^{3x}$ (its $n$-th derivative is $3^{n}e^{3x}$) and $v = x^{2}$ (its third derivative is
> zero), so $v^{(1)} = 2x$, $v^{(2)} = 2$, $v^{(3)} = 0$ — and the series stops after three terms.
>
> $$y^{(n)} = \left(3^{n}e^{3x}\right)x^{2} + n\left(3^{n-1}e^{3x}\right)(2x) + \frac{n(n-1)}{2!}\left(3^{n-2}e^{3x}\right)(2) + 0$$
>
> Factor out $3^{n-2}e^{3x}$:
>
> $$\boxed{\;y^{(n)} = e^{3x}\,3^{\,n-2}\Big(9x^{2} + 6nx + n(n-1)\Big)\;}$$
>
> ✓ Verified against direct differentiation at $n = 1, 2, 3, 5$ — exact match at every order.
>
> **Check at $n = 1$:** $y^{(1)} = e^{3x}3^{-1}\left(9x^{2} + 6x\right) = e^{3x}\left(3x^{2} + 2x\right)$ ✓

> [ex] **Example 2** ·LEI p8–9 — Find the fifth derivative of $y = x^{4}\sin x$.
>
> Take $u = \sin x$ (use §2.2 with $a = 1$) and $v = x^{4}$, so
> $v^{(1)} = 4x^{3}$, $v^{(2)} = 12x^{2}$, $v^{(3)} = 24x$, $v^{(4)} = 24$, $v^{(5)} = 0$.
>
> $$y^{(n)} = x^{4}\sin\left(x + \frac{n\pi}{2}\right) + 4nx^{3}\sin\left(x + \frac{(n-1)\pi}{2}\right) + \frac{n(n-1)}{2!}\,12x^{2}\sin\left(x + \frac{(n-2)\pi}{2}\right)$$
> $$+ \frac{n(n-1)(n-2)}{3!}\,24x\,\sin\left(x + \frac{(n-3)\pi}{2}\right) + \frac{n(n-1)(n-2)(n-3)}{4!}\,24\,\sin\left(x + \frac{(n-4)\pi}{2}\right)$$
>
> At $n = 5$ the coefficients are $1, 20, 120, 240, 120$ and the phases reduce ·LEI p9 by
>
> $$\sin\left(x + \tfrac{5\pi}{2}\right) = \cos x, \qquad \sin(x + 2\pi) = \sin x, \qquad \sin\left(x + \tfrac{3\pi}{2}\right) = -\cos x$$
> $$\sin(x+\pi) = -\sin x, \qquad \sin\left(x + \tfrac{\pi}{2}\right) = \cos x$$
>
> *(The page lists only the first four; the fifth is needed for the $k = 4$ term and is used in the
> answer below. Added here.)*
>
> $$y^{(5)} = x^{4}\cos x + 20x^{3}\sin x - 120x^{2}\cos x - 240x\sin x + 120\cos x$$
>
> $$\boxed{\;y^{(5)} = \left(x^{4} - 120x^{2} + 120\right)\cos x + \left(20x^{3} - 240x\right)\sin x\;}$$
>
> ✓ Verified by direct symbolic differentiation — the difference simplifies to zero.
>
> ⚠ **SCAN (L15)** — $v^{(5)}$ sits at the clipped right edge; only "$=\;($" survives before the
> cut. Reconstructed as $0$, which is what the fifth derivative of $x^{4}$ is and what the working
> below it uses.

---

## 4. Exercise ·LEI p9

[exercise] Use Leibniz's theorem. **No answers are given on the page.**

**1)** Obtain the $n$-th derivative of $A = x^{2}y$.

> **(L16) — settled.** The character before the "=" was previously uncertain. Re-read at 600 dpi it
> is an unmistakable **capital $A$** — the two strokes and a crossbar, quite distinct from anything
> else in this hand. It is a **label for the product**, not a second unknown: the exercise asks for
> $\dfrac{d^{n}}{dx^{n}}\left(x^{2}y\right)$ where $y$ is an arbitrary function of $x$.
>
> [added] With $u = y$ and $v = x^{2}$ (so $v' = 2x$, $v'' = 2$, $v''' = 0$):
> $$A^{(n)} = x^{2}y^{(n)} + 2nx\,y^{(n-1)} + n(n-1)\,y^{(n-2)}$$
> **Ours, not the lecturer's.**

**2)** If $y = x^{3}\cos x$, determine the fifth derivative.

> [added] $u = \cos x$, $v = x^{3}$ (so $v' = 3x^{2}$, $v'' = 6x$, $v''' = 6$, $v^{(4)} = 0$):
> $$y^{(5)} = x^{3}\cos\!\left(x + \tfrac{5\pi}{2}\right) + 15x^{2}\cos\!\left(x + 2\pi\right) + 60x\cos\!\left(x + \tfrac{3\pi}{2}\right) + 60\cos\!\left(x + \pi\right)$$
> $$\boxed{\;y^{(5)} = \left(15x^{2} - 60\right)\cos x + \left(60x - x^{3}\right)\sin x\;}$$
> Verified against direct differentiation.

**3)** Find an expression for $y^{(4)}$ if $y = e^{-t}\sin t$.

> [added] Leibniz works but does not terminate here — neither factor has a vanishing derivative.
> Do it instead by combining the phase shifts: $\frac{d}{dt}\left(e^{-t}\sin t\right)$ multiplies by
> $-1 + i = \sqrt2\,e^{i3\pi/4}$, so
> $$y^{(n)} = 2^{\,n/2}\,e^{-t}\sin\!\left(t + \tfrac{3n\pi}{4}\right) \qquad\Longrightarrow\qquad \boxed{\;y^{(4)} = -4\,e^{-t}\sin t\;}$$
> Verified against direct differentiation.

**4)** If $y = \left(x^{3} + 2x^{2}\right)e^{2x}$, determine an expansion for $y^{(5)}$.

> [added] $u = e^{2x}$, $v = x^{3} + 2x^{2}$ (so $v' = 3x^{2}+4x$, $v'' = 6x+4$, $v''' = 6$, $v^{(4)} = 0$):
> $$y^{(5)} = 2^{5}e^{2x}v + 5\cdot2^{4}e^{2x}v' + 10\cdot2^{3}e^{2x}v'' + 10\cdot2^{2}e^{2x}v'''$$
> $$\boxed{\;y^{(5)} = 16\left(2x^{3} + 19x^{2} + 50x + 35\right)e^{2x}\;}$$
> Verified against direct differentiation.

> **All three solutions above are ours, not the lecturer's** — the page sets them without answers.
> Work them yourself first; each is Example 1 or Example 2 with different numbers.

---

## Flags raised in this file

| ID | Page | What the page shows | Correct form |
|---|---|---|---|
| **V7** | p2 | $\cos\left(\theta + \tfrac\pi2\right) = \sin\theta$ | $-\sin\theta$ |
| C13 | p2 | $y''' = -a^{3}\cos x$ | $-a^{3}\cos ax$ |
| C14 | p5 | the $\ln ax$ item numbered "6)" | 7) — 6) is already used |
| L12 | p1 | identity block's right column clipped | reconstructed from standard identities |
| L13 | p2 | middle bracket of the $\sin3x$ example over-written | result unaffected |
| L14 | p4 | three lines lose their last words to the margin | reconstructed from context |
| L15 | p8 | $v^{(5)}$ clipped | $0$ |
| L16 | p9 | Exercise 1, character before "=" | **resolved: capital $A$** |

Full detail in `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
