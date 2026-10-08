---
kb: "Electromagnetic Fields — Year 3"
course_code: "EEE3202"
lecturer: "withheld"
file_role: topic
section: "04 — Computational electromagnetics and the finite-difference method"
source: "CEM — 'COMPUTATIONAL ELECTOMAGNETICS.pdf', 9 pp., lecturer-authored. Received 8 Oct 2026. Title typo (ELECTOMAGNETICS) is in the original filename and title"
built: "Transcribed from pages rendered at 130 dpi and read directly; equations in canonical LaTeX; suspected errors flagged inline and collected in _verification-log.md § F; the ODE example completed and checked against the exact solution; the iteration example re-run in full and matched to the handout's printed five-iteration values"
coverage: "9/9 pages mapped, no gaps"
subtopics:
  - "What computational electromagnetics is, and why it is needed"
  - "Taylor series for f(x + Δx) and f(x − Δx)"
  - "Second-order (central) difference for f''"
  - "First-order differences for f': forward, backward, central"
  - "FDM on an ODE: y'' − y' + y = 0"
  - "FDM for Poisson's and Laplace's equations — the five-node molecule"
  - "The iteration method"
  - "Example 1 — eight free nodes, five iterations"
  - "Revision questions"
key_equations: [fd-second-difference, fd-forward, fd-backward, fd-central, fd-poisson, fd-laplace, fd-molecule]
prerequisites: ["Poisson's and Laplace's equations from electrostatics", "Taylor series"]
leads_to: []
verification_flags: 21
tags: [computational-electromagnetics, cem, finite-difference, fdm, taylor-series, laplace, poisson, five-node-molecule, iteration, gauss-seidel]
---

# Computational Electromagnetics — CEM

**What this is.** The computational-electromagnetics topic, built from the lecturer's own handout
*Computational Electomagnetics* (9 pp., cited **·CEM pN**; the missing R is in the original). Until
this arrived the finite-difference method was absent from the knowledge base while being **asked in
every paper on file from 2024 on** — 15 marks on the 2024 exam, 15 on the 1 Oct 2025 CAT, 15 on the
23 Oct 2025 exam. See `00-index.md` § Gap map.

## Exam weight — read first

This handout is short and the papers track it closely. Three question types, all recurring:

| Question type | Marks seen | Handout section | Papers |
|---|---|---|---|
| Define CEM / explain the need / describe its application | 2–5 | § 1 | 2024 exam Q5a · 2025 CAT Q2a · 2025 exam Q5a |
| Derive the second difference from the Taylor series | 3 | § 2 | 2025 exam Q5b |
| Potentials at free nodes by iteration | 6–12 | §§ 5–7 | 2024 exam Q5b · 2025 CAT Q2b · 2025 exam Q5c |

> **The 2024 exam's Q5(b) is this handout's Example 1** — same figure, same 20 V / 30 V / 0 V, same
> eight nodes. And the handout's revision question (c) is that same figure a third time. **The
> 2025 exam's Q5(b) copies this handout's Taylor series, error included** (F1 / erratum P29).

**Teach in this order:** § 7 Example 1 (the marks), then § 5's five-node formula, then § 2's
second-difference derivation, then § 1. The ODE example (§ 4) and the first-order differences
(§ 3) have **not been examined**.

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example
(lecturer's numbers) · `[exercise]` problem stated but **not solved** in the source · `[fig]` figure
described from the rendered page · `[added]` supplied here, **not** in the source · `·CEM pN`
provenance · `⚠ VERIFY` flagged suspected source error.

## Symbols used in this file

| Symbol | Meaning | Units | Notes |
|---|---|---|---|
| $\Delta x$, $\Delta y$ | grid spacing (step size) | m | — |
| $h$ | **mesh size** when $\Delta x = \Delta y$ | m | Example 1: 0.5 m |
| $f^{(k)}(x)$ | $k$-th derivative of $f$ | – | the handout writes $f^k$ — not a power |
| $O(\Delta x^n)$ | truncation error of order $\Delta x^n$ | – | halving $\Delta x$ cuts the error by $2^n$ |
| $y_i$ | value of $y$ at grid node $i$ | – | ODE example |
| $V$ | electric potential | V | — |
| $V_{i,j}$ | potential at node $(i, j)$ | V | $i$ counts along $x$, $j$ along $y$ |
| $V_0$; $V_1$–$V_4$ | centre and four neighbours of the five-node molecule | V | ⚠ in the examples $V_1$, $V_2$, … are **node numbers** instead — see clash below |
| $\rho_v$ | volume charge density | C/m³ | ⚠ the handout writes $\rho_s$ — F6 |
| $\varepsilon$ | permittivity | F/m | — |

> ⚠ **Clash — $V_1$ means two different things.** In the molecule formula (§ 5) $V_1$–$V_4$ are the
> four **neighbours** of a centre $V_0$ (top, left, bottom, right). In Example 1 (§ 7) $V_1$–$V_8$
> are **node numbers** on a grid. The 2025 CAT and exam use the second meaning. When applying the
> molecule to node 3 of a grid, its "$V_1$" is whatever sits above node 3 — not node 1.

---

## § 1 · What CEM is, and why it is needed

·CEM p1

**[def]** ·CEM p1 · **Computational electromagnetics (CEM)** is the procedure for **modelling and
simulating the behaviour of electromagnetic fields** in devices or around structures. It uses
**numerical techniques** to solve Maxwell's equations **instead of** obtaining analytical solutions.

**[def]** ·CEM p1 · **Why it is needed.** Very often exact analytical solutions, or even good
approximate ones, are not available. A numerical technique can solve virtually any electromagnetic
problem of interest.

**[def]** ·CEM p3 · The **finite-difference method (FDM)** gives a **numerical** solution to a
differential equation. It does **not** give a symbolic solution.

**[def]** ·CEM p1 · The learning objectives the handout sets:

1. Define CEM and describe why it is important.
2. Derive the second- and first-order difference equations for approximating derivatives.
3. Derive the finite-difference approximation of the Laplace equation.
4. Use it to solve problems by the iteration method.

> **[added] Exam note.** The papers ask this for 2, 3 and 5 marks. The handout gives two sentences,
> which covers 2–3 marks. For a 5-mark "describe the application", add in your own words: CEM turns
> a field problem into a grid of unknowns; it handles **irregular shapes and boundaries** where no
> closed-form answer exists; it is how antennas, waveguides, transmission-line cross-sections and
> shielding are designed in practice. Those points are **not in the handout** — keep them short.

---

## § 2 · The second-order (central) difference

·CEM pp. 1–2

**[eq]** ·CEM p1 · The Taylor series about $x$:

$$f(x + \Delta x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x)\,(\Delta x)^k}{k!}$$

$$f(x - \Delta x) = \sum_{k=0}^{\infty} \frac{(-1)^k f^{(k)}(x)\,(\Delta x)^k}{k!}$$

**[derivation]** ·CEM pp. 1–2 · Written out term by term:

$$f(x - \Delta x) = f(x) - \Delta x\,f'(x) + \frac{\Delta x^2}{2!}f''(x) - \frac{\Delta x^3}{3!}f'''(x) + \cdots \qquad(1)$$

$$f(x + \Delta x) = f(x) + \Delta x\,f'(x) + \frac{\Delta x^2}{2!}f''(x) + \frac{\Delta x^3}{3!}f'''(x) + \cdots \qquad(2)$$

> ⚠ **VERIFY (F1) ★ — the $(-1)^k$ series is labelled $f(x + \Delta x)$.** ·CEM p2 prints
> $f(x+\Delta x) = \sum (-1)^k f^k(x)(\Delta x)^k/k!$. The $(-1)^k$ alternates the signs, which is
> the expansion of $f(x - \Delta x)$ — exactly what equation (1) on the page before writes out.
> **p2's label should read $f(x - \Delta x)$.** ·CEM p1's plain series is correctly labelled; it just
> sits above the written-out $f(x-\Delta x)$ expansion, which makes the page order confusing.
>
> **This error reached an exam.** The 23 Oct 2025 paper, Q5(b), prints the same mislabelled series
> and asks for the second difference from it (erratum P29). In the exam: say the series as printed
> is $f(x-\Delta x)$, write both expansions correctly, and proceed.

> ⚠ **VERIFY (C51)** — ·CEM p2 ends equation (2) with a stray "$\pm$" before the dashes; it is
> "$+\cdots$". ·CEM pp. 1–2 write the $k$-th derivative as $f^k$, which reads as a power (C50).

**[derivation]** ·CEM p2 · **Add (1) and (2).** The odd terms cancel:

$$f(x + \Delta x) + f(x - \Delta x) = 2f(x) + \Delta x^2 f''(x) + O(\Delta x^4)$$

Rearrange for $f''$:

$$\boxed{f''(x) \approx \frac{f(x + \Delta x) - 2f(x) + f(x - \Delta x)}{\Delta x^2}}$$

**[def]** ·CEM p2 · This is the derivative **at the central point**, and it needs the values on
**both sides** of it.

> ⚠ **VERIFY (F2) — the remainder is printed as $O(\Delta x)$.** ·CEM p2. The first term dropped is
> $\dfrac{2\Delta x^4}{4!}f^{(4)}(x)$, so the remainder is $O(\Delta x^4)$; after dividing by
> $\Delta x^2$ the second difference has error $O(\Delta x^2)$. As printed, $O(\Delta x)$ divided by
> $\Delta x^2$ would grow without bound as the grid is refined — the approximation would get
> **worse**, not better.

> **This derivation is a 3-mark exam question** (2025 exam Q5b). The marks are for: writing both
> expansions, adding them, noting the odd terms cancel, rearranging.

---

## § 3 · First-order differences — forward, backward, central

·CEM pp. 2–3

**[derivation]** ·CEM p2 · From (2), move $f(x)$ across and divide by $\Delta x$:

$$\frac{f(x + \Delta x) - f(x)}{\Delta x} = f'(x) + \frac{\Delta x}{2!}f''(x) + \cdots$$

**[eq]** ·CEM p2 · **Forward difference:**

$$\boxed{f'(x) \approx \frac{f(x + \Delta x) - f(x)}{\Delta x}}$$

**[eq]** ·CEM p2 · **Backward difference:**

$$\boxed{f'(x) \approx \frac{f(x) - f(x - \Delta x)}{\Delta x}}$$

> ⚠ **VERIFY (F3) ★ — the backward difference is printed with $+\Delta x$.** ·CEM p2 prints
> $f'(x) \approx \dfrac{f(x) - f(x+\Delta x)}{\Delta x}$. That is the **negative** of the forward
> difference: for $f = x^2$ at $x = 1$ it gives $-(2 + \Delta x)$, about $-2$, when the slope is $+2$. "Backward" means the
> point **behind**, $x - \Delta x$.

**[def]** ·CEM p2 · Both one-sided differences have error $O(\Delta x)$. This sets the accuracy.

**[derivation]** ·CEM p2 · To improve it, **subtract (1) from (2)**. The even terms cancel:

$$f(x + \Delta x) - f(x - \Delta x) = 2\Delta x\,f'(x) + \frac{2\Delta x^3}{3!}f'''(x) + \cdots$$

**[eq]** ·CEM p3 · **Central difference:**

$$\boxed{f'(x) \approx \frac{f(x + \Delta x) - f(x - \Delta x)}{2\Delta x}}\qquad \text{truncation error } O(\Delta x^2)$$

> ⚠ **VERIFY (C52)** — ·CEM p2 says "subtract equation 2 from equation 1". The result it prints,
> $f(x+\Delta x) - f(x-\Delta x)$, is (2) minus (1). The printed result is right; the instruction is
> backwards.

---

## § 4 · FDM on an ordinary differential equation

·CEM pp. 3–4 · `[ex]`, left unfinished in the source — **not examined so far**.

**[ex]** ·CEM p3 · Solve

$$\frac{d^2y}{dx^2} - \frac{dy}{dx} + y = 0$$

with $y = 1$ at the left end and $y = 5$ at the right end.

**[def]** ·CEM p3 · The FDM fills the gap between the differential equation and a **matrix**
version of it:

$$[A][y] = [b] \qquad\Longrightarrow\qquad [y] = [A]^{-1}[b]$$

**[fig]** ·CEM p3 — a horizontal number line from $x = 0$ at the left to $X = 5$ at the right, with
11 ticks numbered 1 to 11 below it and "N=11" at the far left.

**[derivation]** ·CEM p4 · The grid spacing:

$$\Delta x = \frac{x_b - x_a}{N - 1} = \frac{5}{11 - 1} = 0.5$$

> ⚠ **VERIFY (F5) — the domain is stated twice and the two disagree.** ·CEM p3 states
> $0 \le x \le 10$ with $y(10) = 5$. The grid drawn directly below runs from $x = 0$ to $X = 5$, and
> ·CEM p4 computes $\Delta x = 5/10 = 0.5$ from it. **Follow the grid** — the rest of the working
> uses $\Delta x = 0.5$. *[added] Check:* on $0 \le x \le 10$ with 11 nodes, $\Delta x = 1$ and the
> difference solution is wildly unstable — values reach about $-910$ against an exact solution that
> stays between about $-17$ and $+105$. The 0.5 reading is the one that works.

> ⚠ **VERIFY (C53, C54)** — ·CEM p3 calls the end values "initial equations"; they are **boundary
> conditions** (one at each end, not two at the start). ·CEM p4 writes the numerator as
> $x_b - x_b$, which is zero; it is $x_b - x_a$.

**[derivation]** ·CEM p4 · Replace each derivative with its difference form — central for both:

$$\left(\frac{y_{i+1} - 2y_i + y_{i-1}}{\Delta x^2}\right) - \left(\frac{y_{i+1} - y_{i-1}}{2\Delta x}\right) + y_i = 0$$

Collect like terms:

$$\left(\frac{1}{\Delta x^2} + \frac{1}{2\Delta x}\right)y_{i-1} + \left(1 - \frac{2}{\Delta x^2}\right)y_i + \left(\frac{1}{\Delta x^2} - \frac{1}{2\Delta x}\right)y_{i+1} = 0$$

With $\Delta x = 0.5$: $\;1/\Delta x^2 = 4$, $\;1/(2\Delta x) = 1$:

$$\boxed{5y_{i-1} - 7y_i + 3y_{i+1} = 0}$$

> ⚠ **VERIFY (F4) — the $y_{i+1}$ coefficient is printed with a plus.** ·CEM p4 prints
> $\left(\dfrac{1}{\Delta x^2} + \dfrac{1}{2\Delta x}\right)y_{i+1}$. The first-derivative term enters
> with $-y_{i+1}$, so it is $\dfrac{1}{\Delta x^2} - \dfrac{1}{2\Delta x}$. **The numerical line is
> right**: $4 - 1 = 3$. With the printed plus it would be $4 + 1 = 5$.

**[def]** ·CEM p4 · "Write the finite difference equations at each point." **The handout stops here.**

**[added] Completing it.** Nodes 1 and 11 are fixed ($y_1 = 1$, $y_{11} = 5$); nodes 2–10 are
unknown. One equation per unknown node:

$$i = 2:\quad -7y_2 + 3y_3 = -5$$

$$i = 3, \ldots, 9:\quad 5y_{i-1} - 7y_i + 3y_{i+1} = 0$$

$$i = 10:\quad 5y_9 - 7y_{10} = -15$$

In matrix form, $[A]$ is $9 \times 9$ with $-7$ on the diagonal, $5$ below it and $3$ above it, and
$[b] = [-5, 0, 0, 0, 0, 0, 0, 0, -15]^T$. Solving:

| Node | $x$ | FDM $y_i$ | Exact $y(x)$ |
|---|---|---|---|
| 1 | 0.0 | 1 (fixed) | 1.0000 |
| 2 | 0.5 | 0.7790 | 0.7106 |
| 3 | 1.0 | 0.1510 | 0.0076 |
| 4 | 1.5 | −0.9461 | −1.1537 |
| 5 | 2.0 | −2.4591 | −2.7020 |
| 6 | 2.5 | −4.1611 | −4.3962 |
| 7 | 3.0 | −5.6107 | −5.7929 |
| 8 | 3.5 | −6.1566 | −6.2554 |
| 9 | 4.0 | −5.0141 | −5.0306 |
| 10 | 4.5 | −1.4386 | −1.4131 |
| 11 | 5.0 | 5 (fixed) | 5.0000 |

**Verified** — the exact column is the analytical solution
$y = e^{x/2}\left(A\cos\tfrac{\sqrt{3}}{2}x + B\sin\tfrac{\sqrt{3}}{2}x\right)$ fitted to the same two
end values `[added]`. The FDM tracks it to within about 0.25 everywhere on a coarse 11-node grid.

---

## § 5 · FDM for Poisson's and Laplace's equations

·CEM pp. 5–6

**[fig]** ·CEM p5 *(a)* — an irregular closed region (a blob) overlaid with a rectangular grid.
Vertical grid lines are labelled $i-1$, $i$, $i+1$ along the top and $x_0 - \Delta x$, $x_0$,
$x_0 + \Delta x$ along the bottom; horizontal lines $j+1$, $j$, $j-1$ on the right and
$y_0 + \Delta y$, $y_0$, $y_0 - \Delta y$ on the left. Five dots mark $V_{i,j}$ at the centre and
$V_{i-1,j}$, $V_{i+1,j}$, $V_{i,j+1}$, $V_{i,j-1}$ around it.

**[fig]** ·CEM p5 *(b)* — the **five-node molecule**: a cross with $V_0$ at the centre, $V_1$ above,
$V_2$ to the left, $V_3$ below, $V_4$ to the right, each arm of length $h$.

> ⚠ **VERIFY (C59)** — the text refers to "Figure (a)" and "Figure (b)", but neither drawing carries
> a label. (a) is the upper drawing, (b) the cross.

**[def]** ·CEM p5 · **Step 1.** Divide the solution region into rectangular meshes. The
intersections are **grid points** or **nodes**.
- A node on the boundary, where the potential is given, is a **fixed node**.
- An interior node, where the potential is unknown, is a **free node**.

**[derivation]** ·CEM p6 · **Step 2.** Poisson's equation:

$$\nabla^2 V = -\frac{\rho_v}{\varepsilon}$$

In two dimensions, $\partial V/\partial z = 0$:

$$\frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = -\frac{\rho_v}{\varepsilon} \qquad(1)$$

> ⚠ **VERIFY (F6) — the handout switches to $\rho_s$ for the 2-D case.** ·CEM p6: "$\rho_v$ is
> replaced by $\rho_s$". Fails the dimensional check: $\partial^2V/\partial x^2$ is V/m², and
> $\rho_v/\varepsilon$ is (C/m³)/(F/m) = V/m² ✓, but $\rho_s/\varepsilon$ is (C/m²)/(F/m) = **V/m** ✗.
> A 2-D problem still has a volume charge density — it just doesn't vary with $z$. **Harmless in
> practice:** every example and exam question is charge-free (Laplace), where $\rho = 0$ either way.

> ⚠ **VERIFY (C55)** — ·CEM p6 prints Poisson's equation as $V^2V = -\rho_v/\varepsilon$. The first
> $V$ is $\nabla$.

**[derivation]** ·CEM p6 · Apply § 2's second difference in each direction at $(x_0, y_0)$:

$$\frac{\partial^2 V}{\partial x^2} \approx \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{(\Delta x)^2} \qquad(2)$$

$$\frac{\partial^2 V}{\partial y^2} \approx \frac{V_{i,j+1} - 2V_{i,j} + V_{i,j-1}}{(\Delta y)^2} \qquad(3)$$

> ⚠ **VERIFY (C56, C57)** — ·CEM p6 prints the left side of (2) and (3) as $\dfrac{d^2V}{\partial x}$
> and $\dfrac{d^2V}{\partial y}$ — the denominator has lost its square, and $d$ and $\partial$ are
> mixed. The subscripts are printed $V_{i+1.j}$ and $V_{i.j+1}$ with a full stop for the comma.

Substitute (2) and (3) into (1) with $\Delta x = \Delta y = h$:

$$\frac{V_{i+1,j} + V_{i,j+1} - 4V_{i,j} + V_{i-1,j} + V_{i,j-1}}{h^2} = -\frac{\rho_v}{\varepsilon}$$

$$V_{i+1,j} + V_{i,j+1} - 4V_{i,j} + V_{i-1,j} + V_{i,j-1} = -\frac{h^2\rho_v}{\varepsilon}$$

**[eq]** ·CEM p6 · **Finite-difference form of Poisson's equation:**

$$\boxed{V_{i,j} = \frac{1}{4}\left(V_{i+1,j} + V_{i,j+1} + V_{i-1,j} + V_{i,j-1} + \frac{h^2\rho_v}{\varepsilon}\right)}\qquad(4)$$

$h$ is the **mesh size**.

**[eq]** ·CEM p6 · In a **charge-free** region ($\rho_v = 0$) this is **Laplace's equation**:

$$\boxed{V_{i,j} = \frac{1}{4}\left(V_{i+1,j} + V_{i,j+1} + V_{i-1,j} + V_{i,j-1}\right)}\qquad(5)$$

> ⚠ **VERIFY (C58)** — ·CEM p6 writes the charge-free condition as "$(ps = 0)$"; it is $\rho_s$
> (or, correctly, $\rho_v$) $= 0$.

**[eq]** ·CEM p6 · Applied to the five-node molecule of figure (b):

$$\boxed{V_0 = \frac{1}{4}\left(V_1 + V_2 + V_3 + V_4\right)}\qquad(6)$$

**[def]** ·CEM p7 · This is the **average-value property** of Laplace's equation: the potential at
a point is the **average of the potentials at its four neighbours**.

> **This is the revision question (b) and the formula the 2024 exam Q5(b) rests on.** The
> derivation is §§ 2 + 5: two second differences, added, $\Delta x = \Delta y = h$, $\rho = 0$,
> rearrange.

---

## § 6 · The iteration method

·CEM p7

**[def]** ·CEM p7 · Equation (5) or (6) is solved by **iteration** (or by a block/matrix method):

1. Set the potentials at all free nodes to **zero**, or to any reasonable guess.
2. Keep the fixed nodes unchanged throughout.
3. Apply (6) to **every free node in turn**. That is one iteration. The values are approximate.
4. Repeat, sweeping every free node again.
5. Stop when a set accuracy is reached, or when old and new values at every node are close enough.

> ⚠ **VERIFY (F7) — the method is described one way and worked another, and the two give different
> answers.** ·CEM p7 says each sweep uses "**old values** to determine new ones". ·CEM p8, working
> Example 1, says it uses "**the newest** surrounding potentials each time" — so $V_2$ uses the $V_1$
> computed a moment earlier in the same sweep.
>
> These are two different methods (Jacobi and Gauss–Seidel `[added]` — the handout names neither).
> After five iterations of Example 1 they differ by up to 1.3 V at a node. **The handout's printed
> answers are the "newest values" version** — re-run both here, only that one matches. **Use the
> newest value as soon as you have it.**

> **[added] Exam technique.** Present the work as a table — one row per iteration, one column per
> node — and work the nodes in number order every sweep. Write every substitution in the first
> iteration in full; the marks are there.

---

## § 7 · Example 1 — eight free nodes, five iterations

·CEM pp. 7–8 · `[ex]` · **Identical to the 25 Oct 2024 exam Q5(b) (10 marks) and to this handout's
revision question (c).**

> *Determine the potential at the free nodes in the potential system of Fig. 1 using finite
> difference method. Use the iteration method.*

**[fig]** ·CEM p7 *Fig. 1* — an L-shaped region on a square grid, 2 m wide and 2.5 m tall.
- Grid: 4 columns × 5 rows of cells, so $h = 0.5$ m (not printed; follows from the dimensions).
- The top three rows span the full width. Below that only the right-hand two columns continue,
  for two more rows.
- **20 V** — arrow down onto the top edge.
- **30 V** — arrow left onto the right edge.
- **0 V** — arrow up onto the bottom edge of the left portion.
- Short diagonal strokes cut the top-left, top-right and bottom-right corners.
- Free nodes, as $(x, \text{depth below top})$ in m:

| Node | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $x$ | 0.5 | 0.5 | 1.0 | 1.0 | 1.5 | 1.5 | 1.5 | 1.5 |
| depth | 0.5 | 1.0 | 0.5 | 1.0 | 0.5 | 1.0 | 1.5 | 2.0 |

**Boundary values — settled by the handout's own arithmetic.** The figure labels only three edges.
The first-iteration lines take the left edge and the step under nodes 2 and 4 as **0 V**, and the
printed $V_8 = 11.25$ is reproduced only with the left wall and floor of the lower limb at **0 V**
too. So: **20 V on the top, 30 V on the right, 0 V on everything else.** *(This settles the
2024 exam's erratum P13, which flagged exactly this ambiguity on the same figure.)*

**[added] The neighbours of each node** — what goes into each average:

| Node | Up | Left | Down | Right |
|---|---|---|---|---|
| 1 | 20 | 0 | $V_2$ | $V_3$ |
| 2 | $V_1$ | 0 | 0 | $V_4$ |
| 3 | 20 | $V_1$ | $V_4$ | $V_5$ |
| 4 | $V_3$ | $V_2$ | 0 | $V_6$ |
| 5 | 20 | $V_3$ | $V_6$ | 30 |
| 6 | $V_5$ | $V_4$ | $V_7$ | 30 |
| 7 | $V_6$ | 0 | $V_8$ | 30 |
| 8 | $V_7$ | 0 | 0 | 30 |

**[ex]** ·CEM p8 · **First iteration**, starting from all free nodes at zero, using the newest
values:

$$V_1 = \tfrac{1}{4}(0 + 20 + 0 + 0) = 5$$

$$V_2 = \tfrac{1}{4}(5 + 0 + 0 + 0) = 1.25$$

$$V_3 = \tfrac{1}{4}(5 + 20 + 0 + 0) = 6.25$$

$$V_4 = \tfrac{1}{4}(1.25 + 6.25 + 0 + 0) = 1.875$$

> ⚠ **VERIFY (C60)** — ·CEM p8 prints $V_4 = 1.873$. $7.5/4 = 1.875$, and the handout itself uses
> 1.875 in the second iteration.

The handout stops at $V_4$ ("and so on"). **[added]** The rest of the first sweep:

$$V_5 = \tfrac{1}{4}(20 + 6.25 + 0 + 30) = 14.0625$$

$$V_6 = \tfrac{1}{4}(14.0625 + 1.875 + 0 + 30) = 11.4844$$

$$V_7 = \tfrac{1}{4}(11.4844 + 0 + 0 + 30) = 10.3711$$

$$V_8 = \tfrac{1}{4}(10.3711 + 0 + 0 + 30) = 10.0928$$

**[ex]** ·CEM p8 · **Second iteration** begins at node 1:

$$V_1 = \tfrac{1}{4}(0 + 20 + 1.25 + 6.25) = 6.875$$

$$V_2 = \tfrac{1}{4}(6.875 + 0 + 0 + 1.875) = 2.1875$$

**[added] All five iterations** (newest-value method; re-computed, 4 d.p.):

| Iteration | $V_1$ | $V_2$ | $V_3$ | $V_4$ | $V_5$ | $V_6$ | $V_7$ | $V_8$ |
|---|---|---|---|---|---|---|---|---|
| 1 | 5.0000 | 1.2500 | 6.2500 | 1.8750 | 14.0625 | 11.4844 | 10.3711 | 10.0928 |
| 2 | 6.8750 | 2.1875 | 10.7031 | 6.0938 | 18.0469 | 16.1279 | 14.0552 | 11.0138 |
| 3 | 8.2227 | 3.5791 | 13.0908 | 8.1995 | 19.8047 | 18.0148 | 14.7572 | 11.1893 |
| 4 | 9.1675 | 4.3417 | 14.2929 | 9.1624 | 20.5769 | 18.6241 | 14.9534 | 11.2383 |
| **5** | **9.659** | **4.705** | **14.85** | **9.545** | **20.87** | **18.84** | **15.02** | **11.25** |

**[ex]** ·CEM p8 · The handout's printed values after five iterations:

$$V_1 = 9.659\quad V_2 = 4.707\quad V_3 = 14.85\quad V_4 = 9.545\quad V_5 = 20.87\quad V_6 = 18.84\quad V_7 = 15.02\quad V_8 = 11.25$$

**Verified** — seven of eight match exactly.

> ⚠ **VERIFY (C61)** — ·CEM p8 prints $V_2 = 4.707$; re-computed it is **4.705** (unrounded
> 4.7053). It stays 4.705 whether intermediate values are carried in full or rounded to 3 d.p.

**[added] For reference** — iterated to convergence, the values settle at $V_1 = 10.04$,
$V_2 = 4.96$, $V_3 = 15.22$, $V_4 = 9.79$, $V_5 = 21.05$, $V_6 = 18.97$, $V_7 = 15.06$,
$V_8 = 11.26$. Five iterations get every node within 0.4 V.

**[added] Sanity checks you can do in an exam:**
- Every value lies between 0 and 30 V — the lowest and highest boundary values. A Laplace solution
  can never exceed its boundary.
- Nodes near the 30 V wall (5, 6, 7, 8) are highest; nodes near the 0 V corner (2, 4) lowest.

---

## § 8 · Revision questions

·CEM pp. 8–9

**(a)** *Describe the application of computational electromagnetics to solving electromagnetic
problems.* — `[exercise]`. Answer from § 1. *(Also the 2024 exam Q5a, 5 marks.)*

**(b)** *Derive the finite difference approximation of the Laplace equation
$V_0 = \tfrac{1}{4}(V_1 + V_2 + V_3 + V_4)$.* — `[exercise]`. Answer: § 2 then § 5.

**(c)** *Use the equation in (b) to determine the potential at the free nodes in the potential
system of the figure below using finite difference method. Use the iteration method. (Use 5
iterations)* — `[exercise]`.

**[fig]** ·CEM p9 — **the same figure as Example 1**, line for line: 2 m × 2.5 m, 20 V / 30 V / 0 V,
nodes 1–8 in the same places.

**Answer:** identical to § 7. The revision question is Example 1 repeated, and the 2024 exam set
it a third time.

---

## § 9 · Exam map

| Paper | Part | Marks | What it asks | Here |
|---|---|---|---|---|
| 25 Oct 2024 exam | Q5(a) | 5 | Application of CEM | § 1 |
| 25 Oct 2024 exam | Q5(b) | 10 | **Example 1, verbatim** | § 7 — solved |
| 1 Oct 2025 CAT | Q2(a) | 3 | Need for CEM | § 1 |
| 1 Oct 2025 CAT | Q2(b) | 12 | 4 free nodes, 3 × 3 mesh, 60 / 40 / 20 / 0 V, five iterations | **solved** in the paper file — converges to 40, 35, 25, 20 V |
| 23 Oct 2025 exam | Q5(a) | 2 | Define CEM, one application | § 1 |
| 23 Oct 2025 exam | Q5(b) | 3 | Second difference from the Taylor series — **with F1's error** | § 2 |
| 23 Oct 2025 exam | Q5(c) | 10 | Node expressions + four iterations, stepped mesh | **solved** in the paper file, corner taken as 20 V (P33) |

**45 marks across three papers**, every one answerable from this handout.

---

## Verification summary — 21 flags

Full entries in `_verification-log.md` § F.

| Type | IDs | Count |
|---|---|---|
| Substantive | F1–F7 | 7 |
| Cosmetic | C49–C62 | 14 |

**Two of the substantive errors matter for marks.**

- **F1** — the mislabelled Taylor series on p2. It was copied into the 23 Oct 2025 exam (P29).
- **F7** — "old values" against "newest values". The two give different five-iteration answers; the
  handout's own answers use the newest.

**F3** (the backward difference) is the error most likely to be learnt wrongly, because it looks
plausible. F4 and F6 are self-limiting: the numbers that follow them are right.

## Provenance notes

- All 9 pages rendered and read directly. Every figure is described above. **No page requires a
  screenshot.**
- ·CEM pp. 5–8 change typeface (serif body, red italic "Step 1:", "Step 2:") and refer to
  "eq. (4)" and "Figure (a)" in a different style from pp. 1–4. Recorded as an observation only.
- **The iteration example was re-run in full** and reproduces seven of the eight printed values
  exactly (C61 is the eighth).
- **The ODE example (§ 4) is unfinished in the handout.** The completion is `[added]` and was checked
  against the exact analytical solution.
- The handout has no worked example of a **mesh with a re-entrant corner node**, which the 23 Oct 2025
  exam Q5(c) needs (erratum P33). Its worked solution in the paper file takes the corner as 20 V and
  shows how far the answers move under other readings.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
