---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
file_role: formula-sheet
source: "All six source documents (GB, CRV, BIN, MAC, LEI, BES)"
note: "Every equation in CORRECTED form, each tagged to its source page. Where the page differs, the flag ID is given."
---

# Formula sheet — EMT 3101

Every equation from the six topics, in **corrected** form. A ⚠ marks a formula where the page and
this sheet differ; the ID resolves in `_verification-log.md`.

Citations: `·GB p6` uses the document's own **printed** page number (the only typeset source);
`·CRV`, `·BIN`, `·MAC`, `·LEI`, `·BES` use the **scan** page.

---

## 1 · Gamma function &nbsp;→ file `01`

| | Formula | Source |
|---|---|---|
| definition | $\displaystyle \Gamma(n) = \int_0^{\infty} e^{-x}x^{\,n-1}dx, \quad n>0$ | ·GB p4 |
| value at 1 | $\Gamma(1) = 1$ | ·GB p4 |
| **recurrence** | $\displaystyle \Gamma(n+1) = n\,\Gamma(n)$ | ·GB p4 |
| rearranged | $\displaystyle \Gamma(n) = \frac{\Gamma(n+1)}{n}$ — use for negative arguments | ·GB p7 |
| factorial link | $\displaystyle \Gamma(n+1) = n!\quad (n \ge 0 \text{ integer})$ | ·GB p5 |
| half-integer seed | $\displaystyle \Gamma\!\left(\tfrac12\right) = \sqrt\pi$ | ·GB p6 |
| substitution form | $\displaystyle \Gamma(n) = 2\int_0^\infty e^{-y^{2}}y^{\,2n-1}dy \quad (x = y^{2})$ | ·GB p8 |
| log form | $\displaystyle \Gamma(n) = \int_0^1\left(\ln\tfrac1y\right)^{n-1}dy \quad (e^{-x} = y)$ | ·GB p8 |

## 2 · Beta function &nbsp;→ file `01`

| | Formula | Source |
|---|---|---|
| definition | $\displaystyle B(m,n) = \int_0^1 x^{\,m-1}(1-x)^{\,n-1}dx, \quad m,n>0$ | ·GB p9 |
| **Gamma form** | $\displaystyle B(m,n) = \frac{\Gamma(m)\,\Gamma(n)}{\Gamma(m+n)}$ | ·GB p9 |
| symmetry | $B(m,n) = B(n,m)$ | ·GB p9 |
| improper form | $\displaystyle B(m,n) = \int_0^\infty\frac{x^{\,m-1}}{(1+x)^{\,m+n}}dx$ | ·GB p9 |
| **trigonometric form** | $\displaystyle \frac{B(m,n)}{2} = \int_0^{\pi/2}(\sin\theta)^{2m-1}(\cos\theta)^{2n-1}d\theta$ | ·GB p11 |
| read-off rule | $\displaystyle \int_0^{\pi/2}\sin^{p}\theta\cos^{q}\theta\,d\theta = \tfrac12 B\!\left(\tfrac{p+1}{2},\tfrac{q+1}{2}\right)$ | ·GB p12 |

> ⚠ **The trigonometric form is valid only over $[0,\pi/2]$.** Ignoring that is exactly V2:
> substituting $3\theta = t$ maps the interval onto $[0,3\pi/2]$, and the printed answer is a third
> of the true value.

## 3 · Continuous random variables &nbsp;→ file `02`

| | Formula | Source |
|---|---|---|
| pdf validity | $\displaystyle \int_{-\infty}^{\infty} f(x)\,dx = 1$ &nbsp;and&nbsp; $f(x) \ge 0$ | ·CRV p2 |
| pdf from cdf | $f(x) = F'(x)$ | ·CRV p1 |
| **cdf** | $\displaystyle F(t) = P(X \le t) = \int_{-\infty}^{t} f(x)\,dx$ | ·CRV p3 |
| interval probability | $\displaystyle P(x_1 \le X \le x_2) = \int_{x_1}^{x_2} f(x)\,dx = F(x_2) - F(x_1)$ | ·CRV p3–4 |
| **expectation** | $\displaystyle \mu = E(X) = \int_{\text{all }x} x\,f(x)\,dx$ | ·CRV p7 |
| function of $X$ | $\displaystyle E\big[g(X)\big] = \int_{\text{all }x} g(x)f(x)\,dx$ | ·CRV p8 |
| second moment | $\displaystyle E\big[X^{2}\big] = \int_{\text{all }x} x^{2}f(x)\,dx$ | ·CRV p8 |
| **variance** | $\displaystyle \mathrm{Var}(X) = E(X^{2}) - \mu^{2}$ | ·CRV p10 |
| standard deviation | $\sigma_X = \sqrt{\mathrm{Var}(X)}$ | ·CRV p10 |

**Expectation algebra** ·CRV p8 &nbsp;($a$, $b$ constants):

$$E(a) = a \qquad E(aX) = a\,E(X) \qquad E(aX+b) = a\,E(X) + b \qquad E\big[g(X)+h(X)\big] = E\big[g(X)\big] + E\big[h(X)\big]$$

⚠ the page writes the last as $E[g(X) + b(X)]$ — C6.

## 4 · Beta distribution &nbsp;→ file `02`

| | Formula | Source |
|---|---|---|
| **pdf** | $\displaystyle f_X(x) = \frac{1}{B(m,n)}x^{\,m-1}(1-x)^{\,n-1}, \quad x \in [0,1]$ | ·CRV p12 |
| **mean** | $\displaystyle E(X) = \frac{m}{m+n}$ | ·CRV p13 |
| second moment | $\displaystyle E\big[X^{2}\big] = \frac{m(m+1)}{(m+n+1)(m+n)}$ | ·CRV p15 |
| **variance** | $\displaystyle \mathrm{Var}(X) = \frac{mn}{(m+n+1)(m+n)^{2}}$ | ·CRV p15 |
| fit to $\mu$, $\sigma^{2}$ | $\displaystyle m = \frac{\mu^{2}-\mu^{3}}{\sigma^{2}} - \mu$ | ·CRV p18 |
| | $\displaystyle n = \frac{\mu - 2\mu^{2} + \mu^{3}}{\sigma^{2}} - (1-\mu)$ | ·CRV p18 |
| relation between them | $\displaystyle n = \frac{1-\mu}{\mu}\,m$ | ·CRV p17 |
| **from a binomial trial** | $m = k+1, \qquad n = t-k+1$ | ·CRV p19 |
| binomial pmf | $\displaystyle P(k) = {}^{t}C_k\,p^{k}(1-p)^{\,t-k}$ | ·CRV p19 |
| mode *(ours)* | $\displaystyle \frac{m-1}{m+n-2}$ — equals $k/t$ under the rule above | [added] |

> ⚠ In the fit formulas, $\sigma^{2}$ is the **variance** — do not square the number you substitute.
> That is V3.

## 5 · Binomial theorem &nbsp;→ file `03`

| | Formula | Source |
|---|---|---|
| **general expansion** | $\displaystyle (a+x)^{n} = a^{n} + na^{\,n-1}x + \frac{n(n-1)}{2!}a^{\,n-2}x^{2} + \frac{n(n-1)(n-2)}{3!}a^{\,n-3}x^{3} + \cdots$ | ·BIN p1 |
| sigma form | $\displaystyle (a+x)^{n} = \sum_{k=0}^{n}{}^{n}C_k\,a^{\,n-k}x^{k}, \quad {}^{n}C_k = \frac{n!}{(n-k)!\,k!}$ | ·BIN p1 |
| **$r$-th term** | $\displaystyle \frac{n(n-1)\cdots\text{to }(r-1)\text{ terms}}{(r-1)!}\,a^{\,n-(r-1)}x^{\,r-1}$ | ·BIN p2 |
| unit form | $\displaystyle (1+x)^{n} = 1 + nx + \frac{n(n-1)}{2!}x^{2} + \cdots, \quad \lvert x\rvert < 1$ | ·BIN p2 |
| **small-$x$** | $(1+x)^{n} \approx 1 + nx$ | ·BIN p2 |
| validity for $(1+kx)^n$ | $\lvert kx \rvert < 1$ | ·BIN p5 |

**When the series terminates:** $n$ a positive integer → finite. $n$ negative or fractional →
infinite, and a validity range is required.

## 6 · Maclaurin &nbsp;→ file `04`

| | Formula | Source |
|---|---|---|
| **the series** | $\displaystyle f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^{2} + \frac{f'''(0)}{3!}x^{3} + \cdots$ | ·MAC p1 |
| conditions | $f(0) \neq \infty$; all $f^{(n)}(0) \neq \infty$; the series converges | ·MAC p1–2 |
| **L'Hôpital** | $\displaystyle \lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$ &nbsp;— the page states $g'(a) \neq 0$; to apply it twice you need $g' \neq 0$ on a punctured neighbourhood of $a$ (file `04` §4.1) | ·MAC p6 |
| power rule | $\displaystyle \int ax^{n}dx = \frac{ax^{\,n+1}}{n+1} + c$ | ·MAC p3 |

**Standard series used in the notes**

$$e^{x} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots \qquad\qquad \cosh x = 1 + \frac{x^{2}}{2!} + \frac{x^{4}}{4!} + \cdots$$

$$\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \cdots \qquad \sinh x = x + \frac{x^{3}}{3!} + \frac{x^{5}}{5!} + \cdots$$

$$\tan x = x + \tfrac13 x^{3} + \tfrac{2}{15}x^{5} + \cdots$$

⚠ the $\sin x$ line's fourth sign is a struck-through "+" on the page — C10.

## 7 · $n$-th derivatives &nbsp;→ file `05`

| $y$ | $y^{(n)}$ | Source |
|---|---|---|
| $e^{ax}$ | $a^{n}e^{ax}$ | ·LEI p1 |
| $\sin ax$ | $\displaystyle a^{n}\sin\left(ax + \frac{n\pi}{2}\right)$ | ·LEI p2 |
| $\cos ax$ | $\displaystyle a^{n}\cos\left(ax + \frac{n\pi}{2}\right)$ | ·LEI p3 |
| $x^{a}$ &nbsp;($a$ a positive integer) | $\displaystyle \frac{a!}{(a-n)!}x^{\,a-n}$ | ·LEI p3 |
| $\sinh ax$ | $\displaystyle \frac{a^{n}}{2}\Big\{\big[1+(-1)^{n}\big]\sinh ax + \big[1-(-1)^{n}\big]\cosh ax\Big\}$ | ·LEI p4 |
| $\cosh ax$ | $\displaystyle \frac{a^{n}}{2}\Big\{\big[1-(-1)^{n}\big]\sinh ax + \big[1+(-1)^{n}\big]\cosh ax\Big\}$ | ·LEI p5 |
| $\ln ax$ | $\displaystyle (-1)^{\,n-1}\frac{(n-1)!}{x^{n}}$ &nbsp;— independent of $a$ | ·LEI p5 |

**Leibniz theorem** ·LEI p6

$$\boxed{\;(uv)^{(n)} = u^{(n)}v + n\,u^{(n-1)}v^{(1)} + \frac{n(n-1)}{2!}u^{(n-2)}v^{(2)} + \frac{n(n-1)(n-2)}{3!}u^{(n-3)}v^{(3)} + \cdots\;}$$

$u$ = the factor with a known $n$-th derivative; $v$ = the factor whose derivatives terminate.

**Trigonometric identities used** ·LEI p1–2 — see file `05` §1 for the full sheet. The one to watch:

$$\cos\left(\theta + \tfrac\pi2\right) = -\sin\theta \qquad\text{⚠ the page omits the minus — V7}$$

## 8 · Bessel &nbsp;→ file `06`

| | Formula | Source |
|---|---|---|
| **the equation** | $\displaystyle x^{2}y'' + xy' + \left(x^{2}-\nu^{2}\right)y = 0$ | ·BES p1 |
| general solution | $y = A\,J_\nu(x) + B\,J_{-\nu}(x)$ &nbsp;— **only for $\nu \notin \mathbb{Z}$**; at integer order $J_{-n} = (-1)^{n}J_n$ and the second solution is $Y_n$ | ·BES p2 |
| **$J_\nu$** | $\displaystyle J_\nu(x) = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{k!\,\Gamma(\nu+k+1)}\left(\frac{x}{2}\right)^{\nu+2k}$ | ·BES p2 |
| **$J_{-\nu}$** | $\displaystyle J_{-\nu}(x) = \sum_{k=0}^{\infty}\frac{(-1)^{k}}{k!\,\Gamma(k-\nu+1)}\left(\frac{x}{2}\right)^{\,2k-\nu}$ | ·BES p2 ⚠ **V8** |
| $J_0$ | $\displaystyle 1 - \frac{x^{2}}{2^{2}} + \frac{x^{4}}{2^{2}4^{2}} - \frac{x^{6}}{2^{2}4^{2}6^{2}} + \cdots$ | ·BES p3 |
| $J_1$ | $\displaystyle \frac{x}{2} - \frac{x^{3}}{2^{3}(1!)(2!)} + \frac{x^{5}}{2^{5}(2!)(3!)} - \cdots$ | ·BES p3 |

**Recurrence formulas** ·BES p4 — all six verified

$$\textbf{1)}\ \frac{d}{dx}\Big[x^{n}J_n\Big] = x^{n}J_{n-1} \qquad\qquad \textbf{2)}\ \frac{d}{dx}\Big[x^{-n}J_n\Big] = -x^{-n}J_{n+1}$$

$$\textbf{3)}\ J_n = \frac{x}{2n}\big[J_{n-1} + J_{n+1}\big] \qquad\qquad \textbf{4)}\ J_n' = \tfrac12\big[J_{n-1} - J_{n+1}\big]$$

$$\textbf{5)}\ J_n' = \frac{n}{x}J_n - J_{n+1} \qquad\qquad \textbf{6)}\ J_{n+1} = \frac{2n}{x}J_n - J_{n-1}$$

**The two intermediates everything else comes from** ·BES p7:

$$\frac{n}{x}J_n + J_n' = J_{n-1} \quad\cdots① \qquad\qquad -\frac{n}{x}J_n + J_n' = -J_{n+1} \quad\cdots②$$

Subtract for 3, add for 4, rearrange ② for 5, combine 4 and 5 for 6.

---

## Corrections at a glance

Nine formulas or values on the pages differ from what is written above.

| ID | Where | Page prints | Correct |
|---|---|---|---|
| V1 | ·GB p6 | $\Gamma(9/2) = 16.8114$ | $11.6317$ |
| V2 | ·GB p12 | $0.08181$ | $0.24544$ |
| V3 | ·CRV p18 | $(0.0004)^{2}$ | $0.0004$ |
| V4 | ·CRV p20 | $P(10) = 0.0228$ | $0.0282$ |
| V5 | ·BIN p3 | $128 + 44x + \cdots$ | $128 + 448x + \cdots$ |
| V6 | ·MAC p5 | limit 4, answer 0.946 | 0.946 belongs to limit 1; limit 4 gives 1.7582 |
| V7 | ·LEI p2 | $\cos(\theta+\tfrac\pi2) = \sin\theta$ | $-\sin\theta$ |
| V8 | ·BES p2 | $\left(\tfrac x2\right)^{2k}$ | $\left(\tfrac x2\right)^{2k-\nu}$ |
| V9 | ·BES p6 | $\sum_{k=0}$ after $(k-1)!$ appears | $\sum_{k=1}$ |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
