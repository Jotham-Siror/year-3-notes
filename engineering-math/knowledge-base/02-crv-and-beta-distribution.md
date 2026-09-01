---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
section: "02 — Continuous Random Variables and the Beta Distribution"
source: "CRV — 'Topic-2-CRV and Beta Distribution.pdf', 22 pp., handwritten, 300 dpi scan, no text layer."
file_role: topic
subtopics:
  - "continuous random variables: definition and examples"
  - "probability density function and its two validity conditions"
  - "cumulative distribution function and its relation to the pdf"
  - "using F(x) to find interval probabilities"
  - "expectation of a continuous random variable and its algebra"
  - "variance and standard deviation of a continuous random variable"
  - "the Beta distribution: definition, support and shape parameters"
  - "proof that the Beta pdf is legitimate"
  - "E(X), E(X²) and Var(X) for a Beta random variable"
  - "fitting m and n to a stated mean and standard deviation"
  - "obtaining Beta parameters from a binomial experiment"
key_equations:
  [pdf-conditions, cdf-def, interval-prob, expectation-crv, expectation-rules,
   variance-crv, beta-pdf, beta-mean, beta-second-moment, beta-variance,
   beta-from-moments, beta-from-binomial]
prerequisites: ["01 — Gamma and Beta Functions (the B(m,n) machinery)", "definite integration"]
leads_to: []   # a leaf — nothing later in the course depends on this file
verification_flags: 5   # 2 substantive (V3–V4) + 3 cosmetic (C5–C7); plus reading limits L1–L7
tags: [continuous-random-variable, pdf, cdf, expectation, variance,
       standard-deviation, beta-distribution, shape-parameters, binomial,
       method-of-moments, bayesian-prior, emt3101]
---

<!-- TAG LEGEND: [def] definition · [derivation] step-by-step · [eq] key equation ·
  [ex] worked example (lecturer's numbers) · [exercise] unsolved problem set in the notes ·
  [fig] figure described from the rendered page · [added] not in the notes — supplied here ·
  ·CRV pN provenance (scan page — these pages carry no printed numbers) ·
  ⚠ VERIFY = flagged suspected source error, see _verification-log.md -->

# 02 — Continuous Random Variables and the Beta Distribution

**Source:** CRV, 22 handwritten pages, read from 300 dpi page images. The pages carry **no printed
numbers**, so citations use the **scan page**.

**Why this is one file and not two.** The heading changes at p11, but the second half is built
entirely out of the first half's machinery — $E(X) = \int x f(x)dx$ and
$\mathrm{Var}(X) = E(X^2) - \mu^2$ are derived in §3 and then applied, unchanged, to the Beta pdf in
§5. Splitting would put the derivation and its only use in different files.

> **Reading the source.** Roughly half these pages have a **clipped right margin** — the scan is
> off-register. Where that costs something (pp. 9, 12, 18, 20, 21, 22) it is flagged inline and
> logged as `L…` in `_verification-log.md`. Red pen throughout is the lecturer's own later
> annotation; pages 5, 6, 20, 21 and 22 are entirely in red.

---

## 1. Continuous random variables

### 1.1 Definition ·CRV p1

[def] A **continuous random variable** (c.r.v.) is a random variable that can take an **infinite**
number of possible values — a continuum, or values within certain intervals.

Examples given on the page:

- the **mass** in grams of a bag of sugar packaged by a particular machine
- the **time** in minutes taken to perform a task
- the **height** in centimetres of a twenty-year-old student
- the **lifetime** in hours of a 100-watt light bulb

**The consequence worth internalising:** the probability that a c.r.v. takes on an *exact* value is
**0**. Probability lives in intervals, and therefore in areas under a curve.

### 1.2 The two functions that describe a c.r.v. ·CRV p1

[def] The **probability density function** $f(x)$ gives the probability that the variable falls
between a range of values. The **cumulative distribution function** $F(x)$ accumulates it.

> [added] **Read that first sentence carefully — as worded it is not quite right, and the page says
> so itself two lines earlier.** $f(x)$ is a *density*, not a probability: its units are the
> reciprocal of $x$'s, and $P(X = x) = 0$ for every single value. What gives a probability is the
> **area** under $f$ over an interval, which is what §1.4 states. The distinction is worth holding
> on to, because it is the reason a density may exceed 1 — the Beta density in §7.2 peaks at 2.94.

[eq] They are related by differentiation:

$$f(x) = \frac{d}{dx}\big[F(x)\big] = F'(x)$$

*(This line is struck through in red on p2 and moved to p5 — the lecturer reordered the material.)*

### 1.3 When a pdf is valid ·CRV p2

[eq: pdf-conditions] Two conditions, both required:

$$\textbf{i)}\quad \int_{-\infty}^{\infty} f(x)\,dx = 1 \qquad\qquad \textbf{ii)}\quad f(x) \ge 0$$

- (i) says the total area under the pdf is 1 — all the probability is somewhere.
- (ii) says a density cannot be negative.

[fig] ·CRV p2 — a bell-shaped curve on $f(x)$ vs $x$ axes, with the region between $x=a$ and $x=b$
shaded and labelled $P(a \le X \le b)$.

**Restricted to a finite range.** If $f(x)$ is valid on $a \le x \le b$, condition (i) becomes

$$\int_a^b f(x)\,dx = 1$$

### 1.4 Interval probability ·CRV p3

[eq: interval-prob] For $a \le x_1 \le x_2 \le b$,

$$\boxed{\;P\big(x_1 \le X \le x_2\big) = \int_{x_1}^{x_2} f(x)\,dx\;}$$

### 1.5 The cumulative distribution function ·CRV p3–4

[def] $F(x)$ is the probability that $X$ takes a value **less than or equal to** $x$. It is obtained
by integrating the pdf.

[eq: cdf-def] For a particular value $t$ in the range,

$$F(t) = P(X \le t) = \int_{-\infty}^{t} f(x)\,dx$$

The lower limit is written $-\infty$, but in practice it is the smallest $x$ for which $f$ is valid.
So on $a \le x \le b$:

$$F(t) = \int_a^t f(x)\,dx$$

and at the top of the range the two conditions meet:

$$F(b) = P(X \le b) = \int_a^b f(x)\,dx = 1$$

### 1.6 Using $F$ to get interval probabilities ·CRV p4

$$\textbf{1)}\ P(X \le x_2) = F(x_2) \qquad \textbf{2)}\ P(X \le x_1) = F(x_1)$$

$$\textbf{3)}\ \boxed{\;P(x_1 \le X \le x_2) = F(x_2) - F(x_1) = \int_{x_1}^{x_2} f(x)\,dx\;}$$

Each is drawn on the page as a shaded region.

> **(L1) — closed.** A two-line red note at the foot of p4 cannot be read: it is written over
> itself in several passes, and isolating the red channel at 600 dpi recovers only the word "and".
> **It is cancelled text** — confirmed on the reader's own inspection of the page, 2026-08-31 — so
> nothing is lost and no gap remains here. Recorded rather than guessed.

---

## 2. Worked example — the flight delay ·CRV p5–6

> [ex] **Example 1** *(pages 5 and 6 are entirely in red pen)*
>
> $X$ is the delay in hours of a flight from Chicago, with
> $$f(x) = 0.2 - 0.02x, \qquad 0 \le x \le 10$$
> Find (a) $P(\text{delay} < 4\ \mathrm{h})$ and (b) $P(2 \le X \le 6)$.
>
> [fig] The pdf is a straight line from $f(0) = 0.2$ down to $f(10) = 0$ — a right triangle. The
> notes make the point that you can read the answers off the geometry *or* integrate, and do both.
>
> **(a)** Trapezium, with $f(4) = 0.12$:
> $$\tfrac12(0.2 + 0.12)\times4 = 0.64$$
> Or by integration:
> $$P(0 \le X \le 4) = \int_0^4 (0.2 - 0.02x)\,dx = \Big[0.2x - 0.01x^{2}\Big]_0^4 = 0.64 \ ✓$$
>
> **(b)** Trapezium, with $f(2) = 0.16$ and $f(6) = 0.08$:
> $$\tfrac12(0.16 + 0.08)\times4 = 0.48$$
> $$P(2 \le X \le 6) = \Big[0.2x - 0.01x^{2}\Big]_2^6 = 0.48 \ ✓$$
>
> ⚠ **VERIFY (C5)** — the sketch on p6 labels the ordinate at $x=6$ as "**0.8**". It is
> $f(6) = 0.08$, which is what the arithmetic beside it actually uses. A dropped zero in the label
> only.
>
> **Total-area check** ·CRV p6 — the notes close by confirming condition (i) two ways:
> $$\tfrac12\times10\times0.2 = 1 \qquad\text{and}\qquad \int_0^{10}(0.2-0.02x)\,dx = 1 \ ✓$$

---

## 3. Mean and variance of a continuous random variable

### 3.1 Expectation ·CRV p7

[eq: expectation-crv]

$$\boxed{\;\mu = E(X) = \int_{\text{all }x} x\,f(x)\,dx = \int_{-\infty}^{\infty} x\,f(x)\,dx\;}$$

[def] The mean or expectation of a c.r.v. is its **weighted average value** — each value weighted by
its density.

> [ex] ·CRV p7–8 — $f(x) = \tfrac19 x^{2}$ on $0 \le x \le 3$. Find (a) $\mu$ and (b) $P(X < \mu)$.
>
> **(a)** $\displaystyle \mu = \int_0^3 x\cdot\tfrac19x^{2}\,dx = \tfrac19\left[\frac{x^{4}}{4}\right]_0^3 = 2.25$ ✓
>
> **(b)** $\displaystyle P(X < 2.25) = \int_0^{2.25}\tfrac19x^{2}dx = \tfrac19\left[\frac{x^{3}}{3}\right]_0^{2.25} = 0.4219 \to 0.42$ ✓
>
> Worth noticing: the mean sits at 2.25 but only 42 % of the probability lies below it — the density
> is right-weighted.

### 3.2 Expectation of a function, and the algebra ·CRV p8

[eq: expectation-rules] For any function $g$ of $X$,

$$E\big[g(X)\big] = \int_{\text{all }x} g(x)f(x)\,dx, \qquad\text{in particular}\qquad E\big[X^{2}\big] = \int_{\text{all }x} x^{2}f(x)\,dx$$

The discrete-case rules carry over unchanged ($a$, $b$ constants):

1. $E(a) = a$
2. $E(aX) = a\,E(X)$
3. $E(aX + b) = a\,E(X) + b$
4. $E\big[g(X) + h(X)\big] = E\big[g(X)\big] + E\big[h(X)\big]$

> ⚠ **VERIFY (C6)** — rule 4 is written on the page as $E[g(X) + b(X)]$, using $b$ for the second
> function while $b$ is already a constant two lines above. It is a second arbitrary function;
> standard notation is $h(X)$. Naming only — the rule itself is right.

> [ex] **Example 1** ·CRV p9 — $f(x) = \tfrac1{20}(x+3)$ on $0 \le x \le 4$. Find
> $E(X)$, $E(2X+5)$, $E(X^{2})$, $E(X^{2}+2X-3)$.
>
> **(i)** $\displaystyle E(X) = \tfrac1{20}\int_0^4 (x^{2}+3x)\,dx = \frac{34}{15} = 2.2\overline{6}$
>
> ⚠ **SCAN (L2)** — this value **runs off the right edge of the scan**; only "2.2" survives. It
> is recoverable because part (ii) below reuses it as 2.266…, and direct integration confirms
> $34/15 = 2.2667$. The number is certain; the *ink* is not.
>
> **(ii)** $E(2X+5) = 2E(X) + 5 = 9.533 \to 9.5$ ✓ &nbsp; *(rule 3)*
>
> **(iii)** $\displaystyle E(X^{2}) = \tfrac1{20}\left[\frac{x^{4}}{4} + x^{3}\right]_0^4 = 6.4$ ✓
>
> **(iv)** $E(X^{2}+2X-3) = 6.4 + 2(2.266) - 3 = 7.933 \to 7.9$ (2 s.f.) ✓ &nbsp; *(rule 4)*

### 3.3 Variance and standard deviation ·CRV p10

[eq: variance-crv] Definition, then the computational form:

$$\mathrm{Var}(X) = E\big[(X-\mu)^{2}\big] = E(X^{2}) - \big[E(X)\big]^{2} = \boxed{\,E(X^{2}) - \mu^{2}\,}$$

Written out for a continuous variable:

$$\mathrm{Var}(X) = \int_{\text{all }x} x^{2}f(x)\,dx - \mu^{2}, \qquad \mu = \int_{\text{all }x} x f(x)\,dx$$

and the standard deviation is

$$\sigma_X = \sqrt{\mathrm{Var}(X)}$$

**Use the computational form.** $E(X^{2}) - \mu^{2}$ needs one extra integral;
$E[(X-\mu)^{2}]$ needs the mean first and then a harder integrand.

---

## 4. The Beta distribution — what it is

### 4.1 Motivation ·CRV p11

[def] The Beta distribution is a **continuous probability distribution** used to model uncertainty
about the **probability of success** of an experiment. Points the page makes:

- it models random variables confined to a **finite interval**
- the **standard** Beta uses $[0,1]$ — which is exactly the range a probability lives in, so it is
  the natural distribution for "how likely is this likelihood?"
- typical uses: time to complete a task; the prior distribution for binomial proportions in
  **Bayesian analysis**
- unlike most distributions, which have a shape and a scale parameter, Beta has **two shape
  parameters** $m$ and $n$ (written $\alpha$ and $\beta$ in many books), both strictly positive

> ⚠ **VERIFY (C7)** — p12 repeats the p11 heading and its opening sentence, then strikes the
> duplicate out with large diagonal strokes and annotates it "(Next page)". Nothing is lost; it is
> a false start.

### 4.2 Definition ·CRV p12

[eq: beta-pdf] Let $X$ be a c.r.v. with support $R_X = [0,1]$, and let $m, n \in \mathbb{R}_{++}$.
Then $X$ has a **Beta distribution with shape parameters $m$ and $n$** iff

$$\boxed{\;f_X(x) = \begin{cases} \dfrac{1}{B(m,n)}\,x^{\,m-1}(1-x)^{\,n-1} & x \in R_X \\[3mm] 0 & x \notin R_X\end{cases}\;}$$

where $B(m,n)$ is the **Beta function** of file `01`, §5. A variable so distributed is called a
**Beta random variable**.

*(A red margin note records the alternative notation $f_X(x, m, n) \equiv f_X(x)$.)*

### 4.3 Proof that it is a legitimate pdf ·CRV p13

[derivation] Both conditions of §1.3, in turn.

**Non-negativity.** On $[0,1]$, $x^{m-1} \ge 0$ and $(1-x)^{n-1} \ge 0$ for $m,n > 0$, and
$B(m,n)$ is strictly positive. So $f_X \ge 0$.

**Unit area.** The normalising constant is chosen to make it so:

$$\int_{-\infty}^{\infty} f_X(x)\,dx = \frac{1}{B(m,n)}\int_0^1 x^{\,m-1}(1-x)^{\,n-1}dx = \frac{B(m,n)}{B(m,n)} = 1$$

using the integral definition $B(m,n) = \int_0^1 x^{m-1}(1-x)^{n-1}dx$ directly. **That is the whole
reason $1/B(m,n)$ sits in front** — it is not a fudge factor, it is the only constant that can
normalise this density.

---

## 5. Moments of a Beta random variable

### 5.1 Expected value ·CRV p13–14

[eq: beta-mean]

$$\boxed{\;E(X) = \frac{m}{m+n}\;}$$

[derivation] Push the extra $x$ into the exponent so the integral becomes another Beta function:

$$E(X) = \int_0^1 x\cdot\frac{1}{B(m,n)}x^{\,m-1}(1-x)^{\,n-1}dx = \frac{1}{B(m,n)}\int_0^1 x^{(m+1)-1}(1-x)^{\,n-1}dx$$

$$= \frac{B(m+1,\,n)}{B(m,n)}$$

Now write both Beta functions in Gamma form; the $\Gamma(n)$ cancels:

$$= \frac{\Gamma(m+n)}{\Gamma(m)\,\Gamma(n)}\cdot\frac{\Gamma(m+1)\,\Gamma(n)}{\Gamma(m+n+1)} = \frac{\Gamma(m+n)}{\Gamma(m+n+1)}\cdot\frac{\Gamma(m+1)}{\Gamma(m)}$$

Apply the recurrence $\Gamma(k+1) = k\Gamma(k)$ to both fractions:

$$= \frac{\Gamma(m+n)}{(m+n)\Gamma(m+n)}\cdot\frac{m\,\Gamma(m)}{\Gamma(m)} = \frac{m}{m+n}$$

> **Notation note.** These pages write the Gamma function in the older "bar" form
> $\overline{\lceil(x)}$. It is rendered as $\Gamma(x)$ throughout this knowledge base.

### 5.2 Second moment and variance ·CRV p14–15

[eq: beta-second-moment] The same trick with $x^{2}$:

$$E\big[X^{2}\big] = \frac{B(m+2,\,n)}{B(m,n)} = \frac{\Gamma(m+n)}{\Gamma(m+n+2)}\cdot\frac{\Gamma(m+2)}{\Gamma(m)}$$

Two applications of the recurrence on each factor —

$$\Gamma(m+2) = (m+1)\Gamma(m+1) = (m+1)m\,\Gamma(m)$$
$$\Gamma(m+n+2) = (m+n+1)\Gamma(m+n+1) = (m+n+1)(m+n)\Gamma(m+n)$$

— give

$$\boxed{\;E\big[X^{2}\big] = \frac{m(m+1)}{(m+n+1)(m+n)}\;}$$

[eq: beta-variance] Then $\mathrm{Var}(X) = E(X^{2}) - [E(X)]^{2}$:

$$= \frac{m(m+1)}{(m+n+1)(m+n)} - \frac{m^{2}}{(m+n)^{2}} = \frac{m(m+1)(m+n) - m^{2}(m+n+1)}{(m+n+1)(m+n)^{2}}$$

The numerator collapses: $m(m+1)(m+n) - m^{2}(m+n+1) = m\big[(m+1)(m+n) - m(m+n+1)\big] = mn$.

$$\boxed{\;\mathrm{Var}(X) = \frac{mn}{(m+n+1)(m+n)^{2}}\;} \tag{Eqn 1}$$

> **(L3)** — the marginal tag beside this line was previously unresolved. Read at 600 dpi against
> the "1" in $(m+n+1)$ on the same line, it is **"(Eqn 1)"**: the digit is identical to that 1 and
> nothing like this hand's 2. Settled.

**Sanity check** [added]: both formulae verified by direct numerical integration at $m=8$, $n=4$ —
$E(X) = 0.666667$, $E(X^{2}) = 0.461538$, $\mathrm{Var}(X) = 0.017094$, all matching the closed
forms to six decimals.

---

## 6. Fitting $m$ and $n$ to a mean and a standard deviation

> [ex] **Example 1** ·CRV p16 — A production plant produces items with probability $X$ of being
> defective. The manager does not know $X$ but expects it to be **4 %**, and quantifies her
> uncertainty by attaching a **standard deviation of 2 %**. She models $X$ with a Beta distribution.
> How should she set the two parameters to match her priors?
>
> **Set-up.**
> $$E(X) = 0.04 \qquad \mathrm{Var}(X) = (0.02)^{2} = 0.0004$$

> ⚠ **SCAN (L4)** — a red note at the foot of p16 is **struck through and then scribbled over
> repeatedly**; red-channel isolation at 600 dpi confirms it is unreadable. It is cancelled text,
> so no content is lost.

### 6.1 The derivation ·CRV p17–18

[derivation] Solve the two-equation system, writing $\mu = 0.04$ and $\sigma^{2} = 0.0004$:

$$\begin{cases} \dfrac{m}{m+n} = \mu & \cdots (1) \\[3mm] \dfrac{mn}{(m+n+1)(m+n)^{2}} = \sigma^{2} & \cdots (2)\end{cases}$$

**From (1)**, $m = \mu m + \mu n$, so

$$n = \frac{1-\mu}{\mu}\,m \qquad\cdots (3)$$

**Substitute (3) into (2).** Since $m + n = m/\mu$:

$$\frac{m^{2}\left(\dfrac{1-\mu}{\mu}\right)}{\left(\dfrac{m}{\mu} + 1\right)\left(\dfrac{m}{\mu}\right)^{2}} = \sigma^{2} \qquad\Longrightarrow\qquad \frac{m^{2}}{\left(\dfrac{m}{\mu} + 1\right)\left(\dfrac{m}{\mu}\right)^{2}} = \frac{\mu}{1-\mu}\,\sigma^{2}$$

Divide numerator and denominator on the left by $m^{2}$:

$$\frac{1}{\left(\dfrac{1}{\mu}\right)^{3}m + \left(\dfrac{1}{\mu}\right)^{2}} = \frac{\mu}{1-\mu}\,\sigma^{2}$$

Take reciprocals, then multiply through by $\mu^{3}$:

$$\left(\frac{1}{\mu}\right)^{3}m + \left(\frac{1}{\mu}\right)^{2} = \frac{1-\mu}{\mu}\cdot\frac{1}{\sigma^{2}} \qquad\Longrightarrow\qquad m + \mu = \frac{\mu^{2} - \mu^{3}}{\sigma^{2}}$$

[eq: beta-from-moments] The two results:

$$\boxed{\;m = \frac{\mu^{2} - \mu^{3}}{\sigma^{2}} - \mu\;}$$

$$n = \frac{1-\mu}{\mu}\,m = \frac{(1-\mu)(\mu-\mu^{2})}{\sigma^{2}} - (1-\mu) = \frac{\mu - 2\mu^{2} + \mu^{3}}{\sigma^{2}} - (1-\mu)$$

$$\boxed{\;n = \frac{\mu - 2\mu^{2} + \mu^{3}}{\sigma^{2}} - (1-\mu)\;}$$

> ⚠ **SCAN (L5)** — the trailing $-(1-\mu)$ on three consecutive lines of p18 **runs off the
> right edge of the scan**; only "$-\,(1-$" is visible. The form above is reconstructed from the
> algebra (it is what substituting $m$ into $n = \frac{1-\mu}{\mu}m$ must give) and confirmed
> numerically — but it was **not read off the ink**.

### 6.2 The numbers ·CRV p18

$$m = 3.8 \qquad n = 91.2 \qquad\Longrightarrow\qquad \boxed{m = 4,\quad n = 91}$$

Both verified: $\mu = 0.04$, $\sigma^{2} = 0.0004$ give $m = 3.8$ and $n = 91.2$ **exactly**, and
substituting those back reproduces $E(X) = 0.04$ and $\sigma = 0.02$.

> [added] **The rounding in the box is cosmetic, and it costs accuracy.** The exact solution is
> $m = 3.8$, $n = 91.2$; the integers $4$ and $91$ give
> $$E(X) = \frac{4}{95} = 0.04211 \qquad \sigma = 0.02050$$
> — about 5 % above the manager's stated mean. The page rounds because shape parameters are often
> quoted as integers, not because the fit requires it. **Quote 3.8 and 91.2 if the question asks
> you to match the priors**, and say why you have not rounded.

> ⚠ **VERIFY (V3)** — the red margin working on p18 writes the denominator as
> $$m = \frac{(0.04)^{2} - (0.04)^{3}}{(0.0004)^{\mathbf{2}}} - (0.04) = 3.8$$
> **The superscript 2 is there in the ink** (confirmed at 600 dpi) and it is wrong. $0.0004$ is
> *already* $\sigma^{2}$; squaring it again gives $m = 9599.96$, not 3.8. Unsquared:
> $$\frac{0.0016 - 0.000064}{0.0004} - 0.04 = 3.84 - 0.04 = 3.8 \ ✓$$
> Most likely $\sigma^{2}$ notation carried over onto its own numerical value.

---

## 7. Beta parameters from a binomial experiment

### 7.1 The shortcut ·CRV p19

The page notes that statistical software fits Beta parameters by **maximum likelihood**, but that a
binomial experiment gives them directly by arithmetic.

[eq] Binomial probability, in the notes' own notation:

$$P(k) = {}^{t}C_k\,p^{k}(1-p)^{\,t-k}, \qquad {}^{t}C_k = \frac{t!}{k!\,(t-k)!}$$

- $t$ — number of trials; $k$ — number of successes; $p$ — probability of a success

[eq: beta-from-binomial] The Beta parameters are then

$$\boxed{\;m = k + 1, \qquad n = t - k + 1\;}$$

**Notice** ·CRV p19 — as $m$ and $n$ increase the distribution **narrows**, reflecting the greater
precision of a larger sample. That is the whole point of the construction.

### 7.2 Worked example — the cereal test ·CRV p20–22

> [ex] *(pages 20–22 are entirely in red pen)*
>
> You sell breakfast cereal and run a simple experiment: 10 people try your cereal and a
> competitor's. A subject saying yours is better counts as a success. **Seven of 10 (70 %)** said
> yours is better. Two outcomes only, so it is a binomial experiment.
>
> [fig] ·CRV p20 — bar chart, "Probability P(k)" (0.00 to 0.30) against "Number of successes, k"
> (1 to 10). Bars rise from near zero to a peak at $k = 7$, then fall away.
>
> **The distribution**, with $t = 10$, $p = 0.7$:
> $$P(k) = {}^{10}C_k\,(0.7)^{k}(0.3)^{\,10-k}$$
>
> | $k$ | notes | recomputed |
> |---|---|---|
> | 1 | $1.3778\times10^{-4}$ | ✓ |
> | 2 | $1.4467\times10^{-3}$ | ✓ |
> | 3 | "$\ldots\times10^{-3}$" *(mantissa cut — L6)* | $9.00\times10^{-3}$ |
> | 4 | $0.03676$ | ✓ |
> | 5 | $0.1029$ | ✓ |
> | 6 | $0.200$ | ✓ |
> | 7 | $0.2668$ | ✓ |
> | 8 | $0.233$ | ✓ |
> | 9 | $0.121$ | ✓ |
> | 10 | $\mathbf{0.0228}$ | $\mathbf{0.0282}$ ❌ |
>
> ⚠ **VERIFY (V4)** — the $P(10)$ entry sits on the very bottom edge of the scan, but the surviving
> digit-tops were read at 600 dpi against the digits of $0.2668$ three lines above: the final glyph
> is a closed loop with a crossing stroke — **this hand's 8** — where a 2 in the same hand is an
> open hook. The page reads $\mathbf{0.0228}$. The correct value is $0.7^{10} = \mathbf{0.0282}$,
> so the digits have been transposed. *(Residual caveat: only the tops of the digits survive, so
> this is a partial-glyph reading — but the glyph forms are distinct and the correct value is not
> in doubt.)*
>
> **Fitting the Beta** ·CRV p21 — with $k = 7$, $t = 10$:
> $$m = k+1 = 8, \qquad n = t-k+1 = 4$$
>
> Dividing each success count by the number of trials converts the binomial's $k$-axis into the
> Beta's probability axis:
>
> | $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $x = k/10$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
>
> **The density** ·CRV p21 — with $m = 8$, $n = 4$:
> $$B(8,4) = \frac{\Gamma(8)\Gamma(4)}{\Gamma(12)} = \frac{7!\,3!}{11!} = \frac{1}{1320}$$
> $$f(x) = 1320\,x^{7}(1-x)^{3}$$
>
> **Evaluated** ·CRV p22 — every value recomputed and matching:
>
> | $x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $f(x)$ | 0 | $9.6228\times10^{-5}$ | 0.00865 | 0.099 | 0.467 | 1.289 | 2.36 | 2.935 | 2.2146 | 0.631 | 0 |
>
> [fig] ·CRV p22 — density $f(x)$ (axis marked 1, 2, 3) against probability $x$ (0.2 … 1.0). A
> smooth left-skewed hump rising from near zero at $x \approx 0.2$, peaking just above 2.9 at
> $x \approx 0.7$, falling to 0 at $x = 1$.
>
> **The closing observation** ·CRV p22 — both curves peak at **0.7** and are similarly left-skewed.
>
> [added] That is not a coincidence: the mode of a Beta$(m,n)$ density is
> $$\frac{m-1}{m+n-2} = \frac{7}{10} = 0.7$$
> which reproduces $k/t$ exactly under $m = k+1$, $n = t-k+1$. **This identity is ours, not the
> lecturer's** — but it is why the construction in §7.1 works.

---

## Flags raised in this file

| ID | Page | What the page shows | Correct form |
|---|---|---|---|
| **V3** | p18 | red working: denominator $(0.0004)^{2}$ | $\sigma^{2} = 0.0004$, unsquared — squared gives 9599.96, not 3.8 |
| **V4** | p20 | $P(10) = 0.0228$ | $0.7^{10} = 0.0282$ — digits transposed |
| C5 | p6 | sketch ordinate labelled "0.8" | $f(6) = 0.08$; the working uses 0.08 |
| C6 | p8 | $E[g(X) + b(X)]$ | $h(X)$ — $b$ is already a constant on the same line |
| C7 | p12 | heading and opening sentence duplicated from p11 | struck out on the page; a false start |
| L1 | p4 | red foot-note, several writing passes | **illegible** — only "and" recovered |
| L2 | p9 | $E(X)$ clipped at the right edge | $34/15 = 2.2667$, from part (ii) and by integration |
| L3 | p15 | marginal tag after Var(X) | **resolved: "(Eqn 1)"** |
| L4 | p16 | red foot-note, cancelled and scribbled over | **illegible**; cancelled, so nothing lost |
| L5 | p18 | trailing $-(1-\mu)$ clipped, 3 lines | reconstructed from the algebra, not read |
| L6 | p20 | $P(3)$ mantissa cut | $9.00\times10^{-3}$ |
| L7 | all | scan off-register; right margin clipped on ~half the pages | see pp. 9, 12, 18, 20, 21, 22 |

Full detail in `_verification-log.md`.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
