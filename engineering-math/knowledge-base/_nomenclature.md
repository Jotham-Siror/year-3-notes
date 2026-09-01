---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
file_role: nomenclature
source: "All six source documents (GB, CRV, BIN, MAC, LEI, BES)"
covers: "every symbol used in files 01–06, with the clash table first"
---

# Nomenclature — EMT 3101

**Read the clash table before anything else.** This subject reuses a small alphabet across six
topics that were written independently. One clash sits *inside a single equation*, and three more
appear within a few lines of each other on one page.

**Units:** the *Files 01–02* table below carries a units column because probability densities and
their moments have them. Everything in the *File 03*, *Files 04–05* and *File 06* tables is
**dimensionless** — pure mathematics with no physical quantities — so the column is dropped there
rather than filled with "dimensionless" eighteen times.

---

## ⚠ Clash table — symbols that mean different things in different files

| Symbol | Meaning A | Meaning B | Where it bites |
|---|---|---|---|
| **$n$** | argument of $\Gamma(n)$ (file 01) | **second Beta parameter** in $B(m,n)$ (01, 02) | **Both appear in equation (16) of file 01**: $B(m,n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}$. The $n$ in $\Gamma(n)$ *is* the $n$ of $B(m,n)$ here — but two lines earlier $\Gamma(n)$ meant a free argument. Read $B(m,n)$'s parameters as a pair and never substitute into them independently. |
| **$n$** | index/power in $(a+x)^{n}$ (file 03) | **order of a derivative** $y^{(n)}$ (04, 05) | The Leibniz theorem (05 §3.1) uses both meanings **in the same sentence** — "expand $(u+v)^{n}$ with the powers read as derivatives". That is deliberate, and it is the one place the collision is a feature rather than a hazard. |
| **$n$** | derivative order (05) | **integer order of a Bessel function** $J_n$ (06) | In 06 §5, $J_n'$ is the *first* derivative of the *$n$-th order* function. Two different $n$-like roles in one symbol. |
| **$\nu$ vs $n$** | $\nu$ — **real** order of Bessel's equation | $n$ — **integer** order | $J_\nu$ and $J_{-\nu}$ are independent solutions only when $\nu$ is **not** an integer. Once $\nu = n$ they collapse ($J_{-n} = (-1)^n J_n$) and you need a second solution of a different kind. The notes state the "not a negative/positive integer" provisos but do not explain them. |
| **$B$** | the **Beta function** $B(m,n)$ — a Greek capital beta (01, 02) | an **arbitrary constant** in $y = A J_\nu + B J_{-\nu}$ (06) | Different files, but both are "B" on a page. Context: if it has two arguments it is the function. |
| **$m, n$ vs $\alpha, \beta$** | this course's Beta shape parameters | most textbooks' names for the same two | Expect $\alpha, \beta$ in any outside reference. Same quantities, no conversion needed. |
| **$a$** | first term of the binomial $(a+x)^n$ (03) | constant inside $e^{ax}$, $\sin ax$, $\cosh ax$ (05 §2) | And in 05 §2.4 **$a$ is the exponent** of $x^{a}$ — a third meaning, four lines from the second. |
| **$x$** | the independent variable, everywhere | the **second term of the binomial** (03) | File 03's Example 2 literally sets "$a = 2a$, $x = -3b$" — the formula's placeholders are being reused as themselves. Substitute mechanically and it works; read it as the independent variable and it does not. |
| **$k$** | summation index (01 §1.3, 06 §2.1) | **number of successes** in a binomial experiment (02 §7) | File 02 §7 has both on facing pages. |
| **$t$** | dummy upper limit of the c.d.f. $F(t)$ (02 §1.5) | **number of trials** (02 §7) | Both inside file 02. Also a substitution variable in 01's exercises and the independent variable in 05's exercise 3. |
| **$l$ vs $I$** | $\ell$ — magnet half-length (03 p8 Q2) | $I$ — inertia (03 p8 Q1) | **Written with the same glyph on the same page.** See C9. Only the $\ell$ reading gives the stated limit $2M/x^{3}$. |
| **$\sigma$, $\sigma^{2}$** | standard deviation | variance | In file 02 §6 the *number* 0.0004 **is already** $\sigma^{2}$. Squaring it again is exactly the source's error V3. Whenever you see $\sigma^{2}$ beside a number, ask which one the number is. |
| **$H$** | magnetic field strength (03 p8 Q2) | — | The page calls it "electric" field strength. See C8. |
| **$y$** | dependent variable (03–06) | an **arbitrary function of $x$** inside a product (05 exercise 1: $A = x^{2}y$) | If $y$ appears on both sides of a Leibniz problem, the one being differentiated is the product. |

---

## Symbols by file

### Files 01–02 — Gamma, Beta, probability

| Symbol | Meaning | Units / range |
|---|---|---|
| $n!$ | factorial of a non-negative integer | dimensionless |
| $\Gamma(n)$ | Gamma function, $\int_0^\infty e^{-x}x^{n-1}dx$ | dimensionless; defined for all complex $n$ except non-positive integers |
| $B(m,n)$ | Beta function, $\int_0^1 x^{m-1}(1-x)^{n-1}dx$ | dimensionless; $m, n > 0$ |
| $m$ | first Beta shape parameter | real, $> 0$ |
| $n$ | second Beta shape parameter | real, $> 0$ |
| $X$ | a random variable (capital) | — |
| $x$ | a value the random variable takes (lower case) | — |
| $f(x)$, $f_X(x)$ | probability density function | reciprocal of $x$'s units |
| $F(x)$, $F(t)$ | cumulative distribution function | dimensionless, $0 \le F \le 1$ |
| $R_X$ | support of $X$ — the set of values it can take | $[0,1]$ for the standard Beta |
| $E(X)$, $\mu$ | expectation / mean | units of $x$ |
| $E(X^{2})$ | second moment | units of $x^{2}$ |
| $\mathrm{Var}(X)$, $\sigma^{2}$ | variance | units of $x^{2}$ |
| $\sigma$, $\sigma_X$ | standard deviation | units of $x$ |
| $P(k)$ | binomial probability of $k$ successes | dimensionless |
| $t$ | number of trials (binomial) | integer $\ge 1$ |
| $k$ | number of successes (binomial) | integer, $0 \le k \le t$ |
| $p$ | probability of a success | $0 \le p \le 1$ |
| ${}^{t}C_k$ | binomial coefficient $\dfrac{t!}{k!(t-k)!}$ | dimensionless |
| $\mathbb{R}_{++}$ | the strictly positive reals | — |

**Notation the notes use that others do not:**

- $E^{2}(X)$ means $\big[E(X)\big]^{2}$, not $E(X^{2})$. **These are different numbers** — their
  difference is the variance. File 02 p10 writes both on one line.
- The Gamma function is drawn in an older **"bar" form**, $\overline{\lceil(x)}$. Rendered $\Gamma(x)$ throughout this knowledge base.
- $\int_{\text{all }x}$ is used interchangeably with $\int_{-\infty}^{\infty}$.

### File 03 — binomial

| Symbol | Meaning |
|---|---|
| $(a+x)^{n}$ | the binomial being expanded; $a$ is the first term, $x$ the second |
| $n$ | the index (any real: positive integer → finite series; negative or fractional → infinite) |
| $r$ | term number; the $r$-th term carries $x^{\,r-1}$ |
| ${}^{n}C_k$ | binomial coefficient $\dfrac{n!}{(n-k)!\,k!}$ |
| $\delta$ *(ours)* | a small fractional change, as in $(1 \pm \delta)$ |

### Files 04–05 — series and derivatives

| Symbol | Meaning |
|---|---|
| $f^{(n)}(0)$ | $n$-th derivative evaluated at the origin |
| $y'$, $y''$, $y'''$ | first, second, third derivatives, $\dfrac{dy}{dx}$ etc. |
| $y^{(n)}$ | $n$-th derivative, $\dfrac{d^{n}y}{dx^{n}}$ |
| $u$, $v$ | the two factors of a product in Leibniz's theorem |
| $a$ | constant in $e^{ax}$, $\sin ax$, $\cosh ax$ — **and** the exponent in $x^{a}$ |
| $\mathrm{Si}(z)$ *(ours)* | the sine integral $\int_0^{z}\frac{\sin\theta}{\theta}d\theta$ — not named in the notes, but it is what exercise 3.1 of file 04 computes |

**The choice that makes Leibniz work:** $u$ is the factor whose $n$-th derivative is known;
$v$ is the factor whose derivatives **terminate**. Reversed, the series never ends.

### File 06 — Bessel

| Symbol | Meaning |
|---|---|
| $\nu$ | order of Bessel's equation — **real**, not necessarily an integer |
| $n$ | order when it *is* an integer |
| $J_\nu(x)$ | Bessel function of the first kind, order $\nu$ |
| $J_{-\nu}(x)$ | the second independent solution (only independent for non-integer $\nu$) |
| $J_0$, $J_1$ | the two commonly tabulated integer-order functions |
| $A$, $B$ | arbitrary constants of the general solution |
| $k$ | summation index |

---

## Constants and standard values used across the subject

| Quantity | Value |
|---|---|
| $\Gamma\!\left(\tfrac12\right)$ | $\sqrt\pi = 1.772454$ |
| $\Gamma\!\left(\tfrac32\right)$ | $\tfrac12\sqrt\pi = 0.886227$ |
| $\Gamma\!\left(\tfrac52\right)$ | $\tfrac34\sqrt\pi = 1.329340$ |
| $\Gamma\!\left(\tfrac92\right)$ | $\tfrac{105}{16}\sqrt\pi = \mathbf{11.631728}$ &nbsp;*(the notes print 16.8114 — V1)* |
| $\Gamma\!\left(-\tfrac12\right)$ | $-2\sqrt\pi = -3.544908$ |
| $\Gamma\!\left(-\tfrac32\right)$ | $\tfrac43\sqrt\pi = 2.363272$ |
| $(4.5)! = \Gamma(5.5)$ | $52.342778$ |
| $\Gamma(n+1)$ for integer $n$ | $n!$ — **note the shift**: $\Gamma(6) = 5!$, not $6!$ |
| $\mathrm{Si}(1)$ | $0.946083$ |
| $\mathrm{Si}(4)$ | $1.758203$ &nbsp;*(relevant to V6)* |

---

## Three habits that catch this subject's errors

1. **Check the shift on every Gamma.** $\Gamma(n+1) = n!$ is the single most common place to lose a
   mark. Half the exercise answers in file 01 turn on it.
2. **Ask what a number already contains.** V3 exists because $0.0004$ was $\sigma^{2}$ and got
   squared again. Before substituting a decimal, name the quantity it is.
3. **Re-derive a printed decimal from the symbolic form beside it.** V1, V2, V4 and V5 are all
   cases where the algebra on the page is right and the number copied from it is wrong. The symbolic
   line is the trustworthy one.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
