---
kb: "Engineering Mathematics III — EMT 3101"
course_code: "EMT 3101"
lecturer: "withheld"
file_role: index
source: "Six topic documents, 66 pages total: one typeset (11 pp.), five handwritten 300 dpi scans (55 pp.)"
built: "Transcribed from rendered page images; equations in canonical LaTeX; every numerical claim recomputed independently; every ambiguous glyph re-read at 600 dpi against reference glyphs from the same hand"
coverage: "66/66 pages mapped, contiguous, no gaps"
total_verification_flags: 24   # 9 substantive (V1–V9) + 15 cosmetic (C1–C15)
reading_limitations: 18        # L1–L18: 3 settled as clean readings, 1 reconstructed with certainty, 2 illegible but cancelled — no content gaps
past_papers: 1                 # Assignment 1, Aug 2026 — see past-papers/
---

# Engineering Mathematics III (EMT 3101) — Knowledge Base Index

**What this is.** A verified map of the EMT 3101 topic documents — every claim anchored to its
source page, every suspected error flagged and corrected. Start here, then open the topic file you
need rather than re-reading the raw PDFs.

**Status.** All six documents received and mapped. 66 of 66 pages covered.

> **Operating instructions** (how to navigate and teach from this KB) live in `CLAUDE.md` at the
> project root, not in this file.

---

## Document register

| Code | Document | Pages | Topic file |
|---|---|---|---|
| **GB** | *Gamma and Beta functions* | 11 (printed 3–13) | `01-gamma-and-beta-functions.md` |
| **CRV** | *Continuous Random Variable and the Beta Distribution* | 22 | `02-crv-and-beta-distribution.md` |
| **BIN** | *The Binomial Theorem / Binomial Series* (§3.1) | 8 | `03-binomial-theorem.md` |
| **MAC** | *Maclaurin's Theorem* (§3.2) | 7 | `04-maclaurin-theorem.md` |
| **LEI** | *Leibniz Theorem* (§3.3) | 9 | `05-leibniz-theorem.md` |
| **BES** | *Bessel's Equation and Bessel's Functions* | 9 | `06-bessels-equation.md` |

## ⚠ Citation convention — two different page numbers

This is the one piece of housekeeping that will trip you up if you skip it.

| Document | Type | `·CODE pN` means |
|---|---|---|
| **GB** | typeset LaTeX, full text layer | the document's own **printed** page number, in the footer. **Printed = PDF page + 2** (PDF p1 is printed p3) |
| CRV, BIN, MAC, LEI, BES | handwritten scans, no printed numbers | the **scan** page (= PDF page) |

So `·GB p6` is the *fourth* page of that PDF, while `·CRV p18` is the eighteenth. Cite what the
reader will see on the page.

**Why GB starts at printed page 3** — it is an extract. The PDF's own `hyperref` anchors show a
list-item counter beginning at 22, so about 21 list items preceded this content in a two-page
unnumbered front section that was stripped before circulation. The original page numbering survived.
Full working in `../sources/SOURCES.md` § How these files were made.

## Past-paper / assignment register

| Paper | Set | Questions | Solutions |
|---|---|---|---|
| Assignment 1 — EMT 3101 | 10 Aug 2026 | 5 | `past-papers/EMT3101-ASSIGNMENT1-2026-08-10.md` |

**What it tells us about examinable scope** — see `past-papers/00-past-papers-index.md` for the
full read. In one line: **file `01` carries the paper.** Four of the five questions are Gamma/Beta;
the fifth (Q4) is Maclaurin followed by term-by-term integration of a fractional power, and uses no
Gamma or Beta function at all.

---

## How the files are organised

- **Topic files `01`–`06`** — one per source document, in teaching order.
- **`_nomenclature.md`** — every symbol with meaning and units. **The clash table is the most
  consulted section in this subject** — read it before file `01`.
- **`_formula-sheet.md`** — every equation in one place, tagged to its source page, all in
  corrected form.
- **`_verification-log.md`** — every flagged source error with the correct form and why. Also
  §C, the scan-limitation register, and §E, the record of how eleven previously unsettled readings
  were resolved.
- **`past-papers/`** — assessed work, transcribed and solved. Start at `00-past-papers-index.md`.
- **`_transcripts/`** — the page-by-page extraction layer these files were built from. **Not
  tracked**, for the same reason `sources/` is not: it reproduces the lecturer's pages almost
  line for line, and this repository commits only what we authored. Kept locally because it is the
  fastest way to see a whole page in context when a citation needs checking. Where a transcript and
  a topic file disagree, **the topic file wins** — it carries the settled readings.
- **`../sources/`** — the raw PDFs. Not tracked; see `../sources/SOURCES.md`.

### Splitting rule

**One document = one topic file.** The house threshold (split only when a file covers two genuinely
independent themes *and* exceeds ~25 KB) was tested against two candidates and neither was split:

- **`02` (23 KB)** looks like two topics — continuous random variables, then the Beta distribution
  — but the second half is built entirely from the first half's machinery. $E(X) = \int xf(x)dx$
  and $\mathrm{Var}(X) = E(X^{2}) - \mu^{2}$ are derived in §3 and then applied unchanged to the
  Beta pdf in §5. Splitting would put a derivation and its only use in different files.
- **`03`/`04`/`05`** are the source's own §3.1, §3.2 and §3.3 under one heading, *Power Series
  Method of solving O.D.E.* They are kept as three files because they are three separate documents
  with three separate exercise sets, and combined they would run to 43 KB. **See § Section 3
  below** — the grouping is not lost, just recorded here rather than in the filenames.

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation (`[eq: name]` cross-references
the formula sheet) · `[ex]` worked example (lecturer's numbers) · `[exercise]` unsolved problem set
in the notes · `[fig]` figure described from the rendered page · `[added]` supplied here, **not** in
the notes · `·GB p6` provenance · `⚠ VERIFY` flagged suspected **source error** (`V`/`C`) ·
`⚠ SCAN` a **reading limitation** (`L`) — the source is fine, the image is not.

### Flag prefixes

| Prefix | Means |
|---|---|
| `V1`–`V9` | substantive source error — changes the mathematics |
| `C1`–`C15` | cosmetic source error — typo, mislabel, numbering slip |
| `L1`–`L18` | **reading limitation** — clipped, over-written or cut in the scan. **Not a defect in the notes.** Three were settled on re-read, one reconstructed with certainty, two are unreadable but confirmed cancelled — **no content gaps remain** |
| `P1`–`P3` | defect in an assessment paper — see `past-papers/` |

> **`L` is deliberately not `S`.** Fluid Flow already uses `S1`–`S32` for *slide flags*, which are
> real defects. Here the letter would have meant the opposite, so this subject uses `L` for
> *limitation*. |

---

## Coverage map

| File | Doc | Pages | Key content |
|---|---|---|---|
| `01-gamma-and-beta-functions.md` | GB | 3–13 | factorial → Gamma; four Gamma properties; half-integer and negative arguments; Beta function; Gamma form, symmetry, improper form, trigonometric form; three exercise sets |
| `02-crv-and-beta-distribution.md` | CRV | 1–22 | continuous random variables; pdf validity; cdf; interval probability; expectation and its algebra; variance; the Beta distribution and its legitimacy proof; $E(X)$, $E(X^{2})$, $\mathrm{Var}(X)$; fitting $m$, $n$ to a mean and standard deviation; Beta parameters from a binomial experiment |
| `03-binomial-theorem.md` | BIN | 1–8 | general expansion; finite vs infinite series; binomial coefficients; the $r$-th term; $(1+x)^{n}$ and its validity range; small-$x$ approximation; negative and fractional index; percentage-change problems |
| `04-maclaurin-theorem.md` | MAC | 1–7 | the series and its three conditions; building a series from derivatives at the origin; numerical integration by term-by-term expansion; indeterminate limits; L'Hôpital's rule |
| `05-leibniz-theorem.md` | LEI | 1–9 | trigonometric identity sheet; $n$-th derivatives of seven standard functions; the phase-shift trick; Leibniz theorem; choosing $u$ and $v$; two full worked products |
| `06-bessels-equation.md` | BES | 1–9 | Bessel's equation and its order; the Frobenius solution; $J_\nu$ and $J_{-\nu}$ in Gamma form; integer order, $J_0$ and $J_1$; six recurrence formulas with proofs |

*(Ranges are contiguous and cover every page of every document.)*

### Captioned, not redrawn

Five figures appear in the sources — the pdf sketches on ·CRV p2 and p5–6, the binomial bar chart
on ·CRV p20, the Beta density on ·CRV p22, and the $J_0$/$J_1$ graphs on ·BES p4. All five are
described as `[fig]` captions rather than redrawn as SVG, because **none of them carries information
that the surrounding text does not**: every plotted value is tabulated on the same page and
recomputed in this knowledge base, and the shapes are the standard ones. There is no `figures/`
folder for this subject and nothing is lost by its absence. *(Contrast Digital Electronics II, where
a schematic or state diagram must be reasoned from and is therefore redrawn.)*

### Section 3 — the source's own grouping

Files `03`, `04` and `05` are the three parts of one section in the lecturer's numbering:

> **3. Power Series Method of solving O.D.E**
> &nbsp;&nbsp;3.1 The Binomial Theorem / Binomial Series &nbsp;→ `03`
> &nbsp;&nbsp;3.2 Maclaurin Theorem &nbsp;→ `04`
> &nbsp;&nbsp;3.3 Leibniz Theorem &nbsp;→ `05`

The section heading explains what would otherwise look like an odd trio: all three exist to build
**power series**, which is what Frobenius' method — and therefore file `06` — runs on.

---

## Dependency / teaching order

```
                  ┌──► 02 CRV & Beta distribution        (leaf)
                  │
01 Gamma & Beta ──┼──► 03 Binomial ──┬──► 04 Maclaurin ──┐
                  │                  │                   │
                  │                  └──► 05 Leibniz     │  (leaf)
                  │                                      │
                  └──────────────────────────────────────┴──► 06 Bessel
```

*(The `prerequisites` and `leads_to` fields in each topic file's frontmatter are generated from this
graph — if you change one, change both.)*

- **`01` is load-bearing for both branches.** $\Gamma(n+1) = n\Gamma(n)$ is the only tool used in
  `02`'s moment derivations and in every one of `06`'s recurrence proofs.
- **`02` and `05` are leaves** — nothing later depends on either. `02` can be taught at any point after `01`; `05` at any point after `03`.
- **`03` → `05`** because Leibniz's theorem *is* the binomial expansion with the powers read as
  derivative orders. Teaching Leibniz without the binomial in hand throws away the one thing that
  makes it memorable.
- **`06` needs `01` and the series habit from `03`–`05`**, and assumes Frobenius' method from a
  previous section of the course that **is not in these documents**.

### Where the effort should go

| | |
|---|---|
| **Heaviest** | `02` — 22 pages, two full derivations and a parameter-fitting problem |
| **Most exam-weighted** | `01` — four of Assignment 1's five questions came straight out of it |
| **Most error-prone to revise from** | `01` and `06` — see the verification summary |
| **Shortest route to marks** | `01` §5.4–5.5, the Beta read-off rules. Three lines of pattern-matching turn an unfamiliar integral into a Gamma quotient |

---

## ⚠ Gap map — what these documents do not contain

- **Frobenius' method** — `06` says the solution is obtained by it and the margin carries the
  lecturer's own "Homework: show!! (Derive)". The derivation is not on any page here.
- **Bessel functions of the second kind** ($Y_\nu$), needed when $\nu$ is an integer and $J_{-\nu}$
  is no longer independent. `06` states the "not an integer" provisos without explaining them.
- **Proofs of $\Gamma(0) = \infty$ and $\Gamma(1/2) = \sqrt\pi$** — both explicitly deferred on the
  page. The second is set as Exercise 2.4 (·GB p8).

---

## Verification summary — 24 flags

Full detail in `_verification-log.md`. **9 substantive** (V1–V9), **15 cosmetic** (C1–C15), plus
18 reading-limitation entries (L1–L18), which are limits of the *scan*, not defects in the notes.

**The mathematics on these pages is sound.** The defects cluster in one place, and it is a
revealing one:

> **Five of the nine substantive errors are a correct symbolic line followed by a wrong number
> copied from it.** V1, V2, V4, V5 and — in a different way — V6. The algebra is right; the answer
> beside it is not.

That has a direct consequence for how to revise from this subject: **trust the derivation, re-derive
the decimal.**

### The four that would cost you most

| | |
|---|---|
| **V8** (·BES p2) | The $-\nu$ is missing from the exponent of $J_{-\nu}$. It is not a clipped edge — the page's right margin was confirmed blank. Every value the printed formula produces is wrong: at $\nu = 0.3$, $x = 0.5$ it gives 0.7029 instead of 1.0653 |
| **V5** (·BIN p3) | $(2+x)^{7}$'s $x$ coefficient printed as 44 instead of 448 — in the subject's very first worked example, with the correct value derived on the line above |
| **V1** (·GB p6) | $\Gamma(9/2) = 16.8114$ instead of 11.6317. **The single most likely thing to cost marks if memorised**, because it is a clean number in a typeset document with no reading doubt |
| **V7** (·LEI p2) | $\cos(\theta + \tfrac\pi2)$ written without its minus sign — on the reference identity sheet you go back to mid-problem |

### The rest

- **V2** (·GB p12) — Exercise 3.1(c) is out by a factor of 3; the substitution maps onto $[0,3\pi/2]$ but the Beta form quoted is only valid on $[0,\pi/2]$
- **V3** (·CRV p18) — the variance $0.0004$ is squared a second time; as printed it gives $m = 9600$, not 3.8
- **V4** (·CRV p20) — $P(10)$ printed 0.0228; the binomial value is 0.0282, digits transposed
- **V6** (·MAC p5) — an exercise whose stated limit (4) and stated answer (0.946 = Si(1)) belong to different integrals
- **V9** (·BES p6) — Proof 2 keeps its summation limit at $k = 0$ after $(k-1)!$ appears, which would need $(-1)!$

### Three habits that catch these independently

1. **Re-derive a printed decimal from the symbolic form beside it.** Catches V1, V2, V4, V5.
2. **Ask what a number already contains before substituting.** $0.0004$ *is* $\sigma^{2}$ — that is
   V3, and it is the only check needed.
3. **Sanity-substitute.** Setting $x = 1$ in $(2+x)^{7}$ must give $3^{7} = 2187$. With 448 it does;
   with 44 the sum is 1783. **One second, and V5 falls out.**

### ⚠ The topic numbering does not match the filenames

| Document | Filename says | The document itself says |
|---|---|---|
| GB | Topic 1 | signs off "End of Topic **Four**" |
| BIN | Topic 3.1 | margin: "Topic 3" ✓ |
| BES | Topic 4 | header: "Topic **6**" |

**Match by content, never by number.** This knowledge base renumbers `01`–`06` in teaching order and
records each document's original label in its frontmatter. See `_verification-log.md` C2 and C15.

---

## Provenance notes

- **All 66 pages were rendered to images and read directly.** GB is the only document with a text
  layer, and there it was used as a cross-check, not as the source.
- **Every numerical claim was recomputed independently** — `mpmath` at 25 digits, `sympy` for
  symbolic series and derivatives, `scipy.special` for Bessel and binomial values. §D of the
  verification log records every check.
- **Every ambiguous glyph was re-read at 600 dpi** against a known instance of each candidate
  character in the same hand, usually from the same page. Where the question was whether text had
  been cut off, a pixel-column ink scan of the page margin settled it.
- **The clipped margins have a known cause and a known fix.** Each handwritten page is a single
  300 dpi JPEG on a capture area set to exactly A4, so a sheet laid a few millimetres off centre
  loses a strip of one edge. That is the whole of L1–L18. Rescanning at A3, or with exact-size
  cropping off, would remove it — see `../sources/SOURCES.md` § How these files were made.
- **Two items are unreadable, and neither costs anything.** L1 and L4 are red-pen notes written in
  several superimposed passes. **Both are cancelled text** — L4 from the strike-through on the page,
  L1 confirmed on the reader's own inspection. **This subject has no content gap: every page is
  accounted for.**
- **Anything supplied by us is tagged `[added]`** — worked answers where the page leaves a blank
  (·MAC p5 Ex. 3; ·MAC p7 (e)–(g); ·LEI p9 Ex. 1–4; ·GB p7 Example 1.2.3(ii)), and standard results
  used as context. All were solved and numerically verified before being written down.
- **Nothing was invented.** Where a question needs content absent from these documents, the topic
  file says so — see § Not in these documents above.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
