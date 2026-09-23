---
kb: "Engineering Mathematics IV — EMT 3201"
file_role: verification-log
purpose: "Suspected errors found in this unit's material. Currently exam papers only — there are no lecture notes for this unit."
sources_covered: "past papers only"
---

# Verification log — Engineering Mathematics IV (EMT 3201)

**How to use this.** Where a paper is wrong, the paper file keeps the wrong text in its `[q]` block and
carries a `⚠ VERIFY` marker; the correction lives here and nowhere else. Teach the corrected form, and tell
him the paper is wrong rather than silently fixing it.

There is **no lecture-note material for this unit**, so this log has no V-series (source) entries — only the
P-series below.

---

## Exam papers

Defects in the **assessment papers themselves**. Entry IDs are `P1`, `P2`, … and each is referenced by a
`⚠ VERIFY` marker at the matching question in `past-papers/<paper>.md`. **The full entry lives here only**
— the paper file just points to it.

> **⚠ This unit's P-series is its own.** `P1` here is *not* `P1` in EMT 3101, which numbers its papers
> separately in `../../engineering-math/knowledge-base/_verification-log.md` § F. Two different units, two
> independent numberings. Never quote a P-number without naming the unit.

| IDs | Paper |
|---|---|
| **P1–P7** | End of Semester Examination, **21 March 2025** |

★ marks the worst defect on each paper.

> **Standing caveat for this unit.** There are **no lecture notes for EMT 3201**, so nothing below can be
> checked against taught material — only against mathematics. Where an entry says a question is "standard",
> that is a judgement about statistics, not a claim about his syllabus. See `../README.md`.

---

### P1 · EMT 3201 End of Semester (21 Mar 2025), Q2(b) — "10% are travelling at less than 5.5 m.p.h." on a motorway ★
- **Paper:** "The speeds of cars passing through a certain point on a motorway can be taken to be normally
  distributed. Observations show that of cars passing the point, **95% are travelling at less than 85
  m.p.h** and **10% are travelling at less than 5.5 m.p.h.**"
- **Issue:** the two statements are solvable — this is not an unanswerable question — but the normal
  distribution they define is not a description of motorway traffic. **Fitted as printed** (mine, `scipy.stats`,
  2026-09-03, using $z_{0.95} = 1.6449$ and $z_{0.10} = -1.2816$):
  $$\mu = 40.32\ \text{m.p.h.}, \qquad \sigma = 27.17\ \text{m.p.h.}$$
  and that model assigns **6.9 % of the cars a negative speed** — $P(X < 0) = 0.0689$. A fitted
  distribution that says one car in fourteen is travelling backwards is the decisive check here, and it
  takes one line.
- **Correct form:** almost certainly **55 m.p.h.**, a plausible tenth-percentile motorway speed and one
  keystroke from 5.5. That gives $\mu = 68.14$, $\sigma = 10.25$, $P(X<0) = 1.5\times10^{-11}$ — and it
  changes part (ii)'s answer from **0.137** to **0.428**, so the two readings are not close.
- **How to handle:** **work it as printed** — the marks are for the method, and the method is identical
  either way — but write one sentence saying the data implies a mean of 40 m.p.h. and a non-negligible
  probability of negative speed, and that 55 m.p.h. was probably intended. That earns credit rather than
  losing it. Ask the lecturer before treating either number as settled.
- **Severity:** value.

### P2 · EMT 3201 End of Semester (21 Mar 2025), Q4(ii) — the summary statistics omit $\sum x$ and $\sum y$, and give away part (ii)'s answer
- **Paper:** "In all subsequent calculations this incorrect sample is ignored. The remaining data can be
  summarised as follows: $\sum x^{2} = 83.75$, $\sum y^{2} = 44622$, $\sum xy = 1883$, $n = 8$."
- **Issue (two, and they pull in opposite directions):**
  1. **$\sum x$ and $\sum y$ are not given**, and both parts (iii) — the product-moment correlation
     coefficient — and (v) — the regression line — need them. They are recoverable from the printed data
     table, but a candidate who reads "summarised as follows" as "here is everything you need" will stall.
     After dropping the damaged sample they are $\sum x = 23.5$ and $\sum y = 584$ (mine, 2026-09-03).
  2. **The three sums that *are* printed identify the damaged sample**, which is what part (ii) asks for
     and is worth 2 marks. For all nine samples $\sum x^{2} = 96.00$; $96.00 - 83.75 = 12.25 = 3.5^{2}$,
     so the dropped $x$ is 3.5 — **sample F**. Confirmed independently on the other two sums:
     $48718 - 64^{2} = 44622$ ✓ and $2107 - 3.5(64) = 1883$ ✓. **All three agree, so the paper's data is
     internally consistent** — but part (ii) can be answered by arithmetic on the summary rather than by
     looking at the scatter, which is not what it is testing.
- **How to handle:** tell him to compute $\sum x$ and $\sum y$ from the table first, as a habit, before
  reaching for a correlation formula. And when using this as a mock, cover the summary block until (ii)
  has been answered from the scatter diagram.
- **Severity:** omission.

### P3 · EMT 3201 End of Semester (21 Mar 2025), Q1(b) — an unstated divisor, and a population that does not matter
- **Paper:** "Random sample of 70 items were drawn with replacement from a finite population. If
  $\sum(x-\bar x)^{2} = 500$, determine the standard error of the mean."
- **Issue (three, all small):** (i) the question asks for **a number** but never says whether $s^{2}$ uses
  the $n-1$ or the $n$ divisor — $\mathrm{SE} = 0.3217$ against $0.3194$, a 0.7 % difference (mine,
  2026-09-03); (ii) "**with replacement**" makes the finite-population correction unnecessary, so the
  words "from a finite population" change nothing and read as a trap that is not one; (iii) "Random
  sample of 70 items **were** drawn" — *a* random sample … *was* drawn.
- **How to handle:** use the $n-1$ divisor, which is the estimator convention almost every course teaches,
  **and say which you used**. State in one line that sampling with replacement means no finite-population
  correction — that is very likely a mark.
- **Severity:** ambiguity.

### P4 · EMT 3201 End of Semester (21 Mar 2025), Q1(d) — the mark allocation is printed above the question
- **Paper:** "A thermostat set to $20°C$ operates at a range of temperatures having a mean of $20.4°C$ and
  a standard deviation of $1.3°C$. ***[4 Marks]*** / Determine the probability of its opening at
  temperatures between $19.5°C$ and $20.5°C$."
- **Issue:** the "[4 Marks]" sits between the data and the instruction, so it appears to price the
  *statement of the data* rather than the task. Every other part on the paper puts its marks at the end.
  Separately, "the probability of **its opening**" is loose for a thermostat that *switches*; and the
  $20°C$ set point plays no part in the calculation at all.
- **How to handle:** read it as 4 marks for the whole part. Do not go looking for a use for the $20°C$ —
  it is context or a distractor.
- **Severity:** structural.

### P5 · EMT 3201 End of Semester (21 Mar 2025), Q2(a)(i) — the Poisson distribution written $P_0$
- **Paper:** "$X \sim P_0(4.5)$" — a capital $P$ with a **subscript zero**.
- **Issue:** the standard notation is $\mathrm{Po}(4.5)$ or $\mathrm{Poisson}(4.5)$ — an upright "o", not a
  zero. As printed it reads as a family of functions indexed by 0. The intent is unambiguous from the
  words beside it ("the number of telephone calls made in an evening").
- **Correct form:** $X \sim \mathrm{Po}(4.5)$.
- **Severity:** notation.

### P6 · EMT 3201 End of Semester (21 Mar 2025), the whole paper — no statistical tables are supplied
- **Paper:** four pages. Page 4 ends with "END OF PAPER" and nothing follows it. **No normal table, no
  $t$-table, no percentage points, and no note saying tables are issued separately.**
- **Issue:** the paper cannot be worked without them. Twelve of its twenty-five parts need a normal or $t$
  quantile — Q1(d), (e), (f), (g), Q2(a)(i)–(iii), Q2(b)(i)–(ii), Q3(d) and the whole of Q5 — and four of
  those (Q1(f), Q1(g), Q2(b)(i) and Q5) need them **inversely**, which is exactly the direction a
  calculator is least likely to give.
- **Honest caveat:** *this may be a photography gap rather than a paper defect.* What is on file is four
  photographs of a four-page paper that numbers itself "1 of 4" … "4 of 4", so any tables would have been
  a **separate** booklet — normal practice, and it would not appear in this page count. **Recorded as
  missing material, not asserted as an error by the setter.**
- **How to handle:** supply standard normal and $t$ tables when setting this as a mock, and say they are
  yours. If he is revising, this is the one piece of "material" for this unit that is trivially obtainable
  and definitely needed.
- **Severity:** omission (missing material).

### P7 · EMT 3201 End of Semester (21 Mar 2025), throughout — punctuation and wording, collected
- **Paper:** "Explain briefly**,**" followed by a list (Q1(a), and again without the comma at Q3(a)).
  "**Your notes** should include a description of each method" (Q1(a)) — *your answer* is meant.
  "$n = 7$, $\sum x = 386$ $\sum y = 108$ **,**$\sum xy = 6403$ **,**$\sum x^{2} = 23058$" (Q1(h)) — two
  stray leading commas, and no comma between the first two sums. "(i) Clustering**,** (ii)
  Stratification**,**" (Q3(b)) — list items closed with commas before the sentence resumes. "the time it
  takes each machine to pack ten cartons **are** recorded" (Q5) — *is* recorded.
- **Severity:** typo. None of it touches the statistics; collected in one entry rather than six.

<!-- Later papers append their own P-numbered entries above this line. -->

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
