---
kb: "Electromagnetic Fields — Year 3"
course_code: "EEE3202"
lecturer: "withheld"
file_role: topic
source: "Two current-cohort documents. TL = *Transmission lines* (16 pp., lecturer-authored). TLT = *Transmission Line Theory* (22 pp., a distributed slide deck compiled from Sadiku 5e, Ida 3e and Pozar 4e)"
built: "Transcribed from pages rendered at 200 dpi; equations in canonical LaTeX; suspected errors flagged inline and collected in _verification-log.md § T; every worked example and exercise solved and numerically verified here"
coverage: "16/16 pages of TL and 22/22 pages of TLT mapped, no gaps"
total_verification_flags: 24
---

# Transmission Lines — TL + TLT

**What this is.** The transmission-line topic, built from **both** current-cohort documents. Until
these arrived this territory was absent from the knowledge base entirely while being examined for
roughly a third of the marks; see `00-index.md` § Gap map.

> **Read the provenance tags.** Two sources sit in this file and they are not equal in standing.
>
> | Tag | Document | What it is |
> |---|---|---|
> | **·TL pN** | *Transmission lines* (16 pp.) | **The lecturer's own handout.** Same author as WC1. This is the spine — it sets the scope and it is what the exam questions track |
> | **·TLT pN** | *Transmission Line Theory* (22 pp.) | A **slide deck distributed by the lecturer**, compiled from Sadiku, Ida and Pozar (its own p2 says so). Course material, but not the lecturer's own writing |
>
> Where the two overlap the physics agrees. Where they differ in *form*, TLT is the cleaner
> document and has been used to settle TL's typography — see § Verification.

**Why one file and not two.** The house rule is one handout per topic file. These two are the
exception the rule anticipates: they are **one topic split across two documents**, overlapping
heavily for their first third and complementary after it. Splitting them would mean transcribing
the telegrapher's derivation twice, in two mutually inconsistent notations, and then
cross-referencing between them on every question. Kept whole, TL's errors are caught by TLT on the
page where they occur.

## Who covers what

| Content | TL | TLT |
|---|---|---|
| RLGC circuit model, primary line constants | ✅ p1 | ✅ pp. 3–5 |
| Telegrapher's equations from KVL/KCL | ✅ pp. 1–2 | ✅ pp. 6–7 |
| Wave equation — **lossy** (R, G retained) | ❌ | ✅ pp. 8–9 |
| Wave equation — lossless, $u_p$, d'Alembert | ✅ pp. 2–3 | ✅ p. 10 |
| Phasor form, $\gamma$, $\alpha$, $\beta$ | ✅ pp. 3–4 | ✅ pp. 11–13, 16 |
| Characteristic impedance $Z_0$ in terms of R, L, G, C | ❌ | ✅ p. 15 |
| Reflection coefficient $\Gamma$ | ✅ pp. 4–5 | ✅ p. 17 |
| Standing waves, positions of maxima/minima | ✅ pp. 7–9 | ❌ |
| VSWR | ✅ p. 9 | ✅ p. 17 |
| Return loss | ❌ | ✅ p. 17 |
| Slotted-line measurement | ✅ pp. 10–11 | ❌ |
| $Z_{in}(-z)$ analytical expression | ✅ p. 12 | ❌ |
| Short-circuit and open-circuit stubs | ✅ pp. 12–14 | ❌ |
| Quarter-wave transformer | ✅ pp. 14–15 | ❌ |
| **Smith chart** — method, blank chart, example | ❌ | ✅ pp. 18–22 |

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example
(lecturer's numbers) · `[exercise]` problem stated but **not solved** in the source · `[fig]` figure
described from the rendered page · `[added]` supplied here, **not** in either source · `·TL pN` /
`·TLT pN` provenance · `⚠ VERIFY` flagged suspected source error.

---

## § 1 · The line as a circuit — the four primary line constants

·TL p1 · ·TLT pp. 3–5

**[def]** On a transmission line the input voltage and current are **not** equal to the output
values; both depend on **position and time**. ·TL p1

**[fig]** ·TLT p3 *Figure 1* — a short section of two-wire line of length $\Delta\ell$, with
$\Delta\ell \ll \lambda$ ("electrically small"), annotated *"this wire has some inductance"* and
*"this gap has some capacitance"*. *Figure 2* zooms one $\Delta\ell$ cell out of a source–line–load
circuit into a series $L\Delta\ell$ with a shunt $C\Delta\ell$.

**[fig]** ·TLT p4 *Figure 3* — the same cell with losses added: series $R\Delta\ell$ then
$L\Delta\ell$, shunt $G\Delta\ell$ and $C\Delta\ell$. Boxed notes: the total capacitance of the
length $\Delta\ell$ is $C\Delta\ell$ and the total inductance $L\Delta\ell$; the total series
resistance is $R\Delta\ell$ and the total shunt conductance $G\Delta\ell$.

**[def]** The four primary line constants, each **per unit length**, and what each represents ·TL p1:

| Constant | Represents | SI unit |
|---|---|---|
| $L$ | Energy stored in the **magnetic field**. The interaction between the current and the conductor is modelled as an inductor | H/m |
| $R$ | The line's own resistance — **ohmic loss** in the conductors. Modelled as a resistor | Ω/m |
| $C$ | Energy stored in the **dielectric** between the two conductors that form the line | F/m |
| $G$ | **Charge leakage** through the insulating material. Modelled as a conductance | S/m |

> **Exam note.** This table *is* the answer to a recurring bookwork question: the 1 Oct 2025 CAT
> Q1(a) asks for "the four primary line constants and their significance" for **4 marks**, and the
> 23 Oct 2025 exam Q1(g) asks the same thing for the same 4 marks three weeks later. One mark each,
> and the marks are for the *significance*, not the names.

---

## § 2 · The telegrapher's equations

·TL pp. 1–2 · ·TLT pp. 6–7

**[derivation]** ·TL p1 · Applying **KVL** around the cell:

$$v(z,t) - v(z+\Delta z, t) = i(z,t)R\,\Delta z + L\,\Delta z\,\frac{\partial i(z,t)}{\partial t}$$

Dividing by $\Delta z$ and letting $\Delta z \to 0$:

$$\lim_{\Delta z \to 0}\frac{v(z,t)-v(z+\Delta z,t)}{\Delta z} = i(z,t)R + L\,\frac{\partial i(z,t)}{\partial t}$$

$$\boxed{-\frac{\partial v(z,t)}{\partial z} = R\,i(z,t) + L\,\frac{\partial i(z,t)}{\partial t}}\qquad(1)$$

**[derivation]** ·TL pp. 1–2 · Applying **KCL** at the node, by the identical argument:

$$\boxed{-\frac{\partial i(z,t)}{\partial z} = G\,v(z,t) + C\,\frac{\partial v(z,t)}{\partial t}}\qquad(2)$$

> ⚠ **VERIFY (T1, T2) — the handout prints both of these with $\partial/\partial t$ on the left.**
> ·TL p1 eq 1 and ·TL p2 eq 2 read $-\dfrac{dv(z,t)}{dt}$ and $-\dfrac{di(z,t)}{dt}$. The left-hand
> side **must be the derivative with respect to $z$** — it is the limit of a difference in $z$
> divided by $\Delta z$, as the line immediately above each one shows. Written as printed, equation
> (1) says a time-derivative equals a quantity built from the same time-derivative, which is not
> solvable. The handout **silently corrects itself** on ·TL p2 ("for simplicity of notation we may
> write") where it prints $-\frac{dv}{dz} = L\frac{di}{dt}$ with the $z$ restored. TLT p7 prints the
> correct $z$-form throughout. **Learn the boxed form above.**

**[eq]** ·TLT p7 · The same pair in the deck's sign convention — the form the deck calls
**the telegrapher's equations**:

$$\frac{\partial V(z,t)}{\partial z} + L\,\frac{\partial I(z,t)}{\partial t} + R\,I(z,t) = 0\qquad\text{·TLT p7 (1)}$$

$$\frac{\partial I(z,t)}{\partial z} + C\,\frac{\partial V(z,t)}{\partial t} + G\,V(z,t) = 0\qquad\text{·TLT p7 (2)}$$

These are algebraically identical to (1) and (2) — everything moved to one side.

**[fig]** ·TLT p5 *Figure 4*, p6 *Figure 5* (KVL loop circled in red), p7 *Figure 6* (KCL node
circled in red) — the same $\Delta\ell$ cell three times, each with the loop or node being applied
highlighted. Use these if the derivation's bookkeeping is unclear; see § 1 of your study guide for
the figures themselves rather than redrawing them.

---

## § 3 · The wave equations

**[derivation]** ·TLT p8 · Differentiating TLT (1) with respect to $t$ and (2) with respect to $z$,
then eliminating the cross-derivative, gives the **full lossy wave equations**:

$$\boxed{\frac{\partial^2 V(z,t)}{\partial z^2} = LC\,\frac{\partial^2 V(z,t)}{\partial t^2} + (LG+RC)\,\frac{\partial V(z,t)}{\partial t} + RG\,V(z,t)}$$

$$\boxed{\frac{\partial^2 I(z,t)}{\partial z^2} = LC\,\frac{\partial^2 I(z,t)}{\partial t^2} + (LG+RC)\,\frac{\partial I(z,t)}{\partial t} + RG\,I(z,t)}$$

**[def]** ·TLT p8 · A **wave equation** relates a quantity's second derivative **in time** to its
second derivative **in space**.

**[def]** ·TLT p9 · The wave equations for voltage and current are **identical**, so they have
**identical solutions**. Everything derived for $V$ carries over to $I$ unchanged.

> **This lossy form appears only in TLT.** TL drops to the lossless case before forming the wave
> equation and never writes the general version.

---

## § 4 · The lossless line

·TL pp. 2–3 · ·TLT p10

**[def]** On a **lossless** line the series resistance vanishes ($R=0$) and the shunt conductance
vanishes ($G=0$). ·TLT p10

**[eq]** The telegrapher's equations reduce to ·TL p2 · ·TLT p10:

$$-\frac{\partial v}{\partial z} = L\,\frac{\partial i}{\partial t}\qquad\qquad -\frac{\partial i}{\partial z} = C\,\frac{\partial v}{\partial t}$$

**[derivation]** ·TL pp. 2–3 · Differentiating the first with respect to $z$ and the second with
respect to $t$:

$$-\frac{\partial^2 v}{\partial z^2} = L\,\frac{\partial^2 i}{\partial t\,\partial z}\qquad(4)\qquad\qquad -\frac{\partial^2 i}{\partial z\,\partial t} = C\,\frac{\partial^2 v}{\partial t^2}\qquad(5)$$

Eliminating the mixed derivative between (4) and (5):

$$-\frac{1}{L}\frac{\partial^2 v}{\partial z^2} = -C\,\frac{\partial^2 v}{\partial t^2}$$

$$\boxed{\frac{\partial^2 v}{\partial z^2} = LC\,\frac{\partial^2 v}{\partial t^2}}\qquad(6)$$

**[eq]** ·TL p3 · Written in standard wave form:

$$\frac{\partial^2 v}{\partial z^2} = \frac{1}{u_p^{2}}\,\frac{\partial^2 v}{\partial t^2}\qquad(7)
\qquad\text{where}\qquad \boxed{u_p = \frac{1}{\sqrt{LC}}}$$

$u_p$ is the **phase velocity** — the speed at which the wave travels along the line, in m/s.

**[def]** ·TL p3 · Equation (7) is the **lossless telegraphic equation**. Its solution has the form

$$v(z,t) = V^{+}\!\left(t - \frac{z}{u_p}\right) + V^{-}\!\left(t + \frac{z}{u_p}\right)$$

**Observation** ·TL p3 — *"Voltages and currents along the lines are waves along a transmission
line."* The $V^{+}$ term travels in $+z$, the $V^{-}$ term in $-z$.

---

## § 5 · Phasor form and the propagation constant

·TL pp. 3–4 · ·TLT pp. 11–13, 16

**[def]** ·TL p3 · Any pulse can be written as a sum of sinusoids (Fourier), and

$$V_0\cos(\omega t + \theta) = \mathrm{Re}\left\{V_0 e^{j(\omega t+\theta)}\right\}$$

For $V = V_0 e^{j\omega t}$, $\;\dfrac{dV}{dt} = j\omega V_0 e^{j\omega t} = j\omega V$ — so
**differentiating in time is equivalent to multiplying the phasor by $j\omega$.**

**[eq]** ·TL p4 · In phasor form the telegrapher's equations become

$$-\frac{dV}{dz} = (R + j\omega L)\,I\qquad(8)\qquad\qquad -\frac{dI}{dz} = (G + j\omega C)\,V\qquad(9)$$

> ⚠ **VERIFY (T3) — the handout prints a minus sign in both.** ·TL p4 reads
> $-\frac{dV}{dz} = RI - j\omega LI$ and $-\frac{dI}{dz} = GV - j\omega CV$. Both must be **plus**.
> The error does not propagate: the very next line of the handout multiplies out to
> $(R+j\omega L)(G+j\omega C)$, which is what the corrected form gives.

**[derivation]** ·TL p4 · Differentiating (8) with respect to $z$ and substituting (9):

$$\frac{d^2 V}{dz^2} = (R+j\omega L)(G+j\omega C)\,V \;=\; \gamma^2 V$$

**[eq]** ·TL p4 · The **complex propagation constant**:

$$\boxed{\gamma^2 = (R+j\omega L)(G+j\omega C)}\qquad\qquad\boxed{\gamma = \sqrt{(R+j\omega L)(G+j\omega C)}}$$

**[eq]** ·TLT p12, p16 · The deck writes the same thing multiplied out:

$$\gamma = \sqrt{RG + j\omega(LG+RC) - \omega^2 LC}$$

**[added]** The two forms are identical — expanding TL's product gives
$RG + j\omega RC + j\omega LG + j^2\omega^2 LC = RG + j\omega(LG+RC) - \omega^2 LC$. Either may be
quoted.

**[def]** ·TLT p12, p16 · $\gamma$ splits into real and imaginary parts:

$$\gamma = \alpha + j\beta\qquad\qquad \alpha = \mathrm{Re}\{\gamma\}\;\;(\text{Np/m})\qquad \beta = \mathrm{Im}\{\gamma\} = \frac{2\pi}{\lambda}\;\;(\text{rad/m})$$

$\alpha$ is the **attenuation constant**, $\beta$ the **phase constant** (TLT calls it the *lossless
propagation constant*).

**[eq]** ·TLT p12 · **In the lossless case** ($R=G=0$):

$$\gamma = j\omega\sqrt{LC}\quad\Longrightarrow\quad \boxed{\alpha = 0}\qquad\boxed{\beta = \omega\sqrt{LC}}$$

**[eq]** ·TLT p13 · The solutions, in complex exponentials:

$$V(z) = V_0^{+}e^{-\gamma z} + V_0^{-}e^{+\gamma z}\qquad\qquad I(z) = I_0^{+}e^{-\gamma z} + I_0^{-}e^{+\gamma z}$$

> ⚠ **VERIFY (T4) — the deck prints the backward term as $e^{j\gamma}$.** ·TLT p13 writes
> $V_0^{-}e^{j\gamma}$ and $I_0^{-}e^{j\gamma}$ — wrong symbol *and* the $z$ is missing. It must be
> $e^{+\gamma z}$. The deck's own p14 confirms it: *"the terms including $e^{+\gamma z}$ [propagate]
> in the $-z$ direction."*

**[def]** ·TLT p14 · Terms in $e^{-\gamma z}$ propagate in **$+z$** (forward); terms in
$e^{+\gamma z}$ propagate in **$-z$** (backward). The total voltage is the sum of the two, and
likewise the total current.

**[fig]** ·TLT p14 — a two-conductor line with a blue wave packet at the left labelled *forward
propagating wave* with an arrow to the right, and a red packet at the right labelled *backward
propagating wave*.

> ⚠ **VERIFY (C24)** — ·TLT p14's body text is clipped off the left edge of the page ("ach f",
> "hese solutions", "n the +z direction"). Nothing is lost that cannot be reconstructed, but the page
> is not readable as printed.

---

## § 6 · Characteristic impedance $Z_0$

·TLT p15 — **this section exists only in TLT.**

**[def]** The ratio of voltage to current at any point along a line is fixed by the line itself.
This is the **characteristic impedance**:

$$\boxed{Z_0 = \frac{V_0^{+}}{I_0^{+}} = \sqrt{\frac{R+j\omega L}{G+j\omega C}}}$$

**[eq]** For a **lossless** line:

$$\boxed{Z_0 = \sqrt{\frac{L}{C}}}$$

**[def]** The characteristic impedance of a lossless line is **purely real**.

**[eq]** Repeating the derivation with the backward wave gives

$$Z_0 = \sqrt{\frac{R+j\omega L}{G+j\omega C}} = \frac{\text{forward voltage}}{\text{forward current}} = -\,\frac{\text{backward voltage}}{\text{backward current}}$$

> **Note the negative sign on the backward terms** (the deck emphasises this). It is why the current
> in § 7 carries a minus on its reflected term while the voltage carries a plus.

---

## § 7 · Reflection coefficient

·TL pp. 4–5 · ·TLT p17

**[eq]** ·TL p4 · On a lossless line, taking $z=0$ **at the load** and $z=-l$ at the generator, the
voltage is the phasor sum of the wave travelling right and the wave travelling left:

$$V(z) = V_0^{+}e^{-j\beta z} + V_0^{-}e^{+j\beta z}$$

and the current is

$$I(z) = \frac{V_0^{+}}{Z_0}e^{-j\beta z} - \frac{V_0^{-}}{Z_0}e^{+j\beta z}$$

> ⚠ **VERIFY (T5) — the handout prints $V_0^{+}$ in both terms of the current.** ·TL p4 writes
> $I(z) = \frac{V_0^{+}}{Z_0}e^{-j\beta z} - \frac{V_0^{+}}{Z_0}e^{+j\beta z}$. The reflected term
> must carry $V_0^{-}$. The minus sign is correct and comes from § 6.

**[derivation]** ·TL p5 · At the load ($z=0$):

$$V_L = V_0^{+} + V_0^{-}\qquad\qquad I_L = \frac{V_0^{+}}{Z_0} - \frac{V_0^{-}}{Z_0}$$

$$Z_L = \frac{V_L}{I_L} = \left(\frac{V_0^{+}+V_0^{-}}{V_0^{+}-V_0^{-}}\right)Z_0$$

> ⚠ **VERIFY (T6, T7) — two errors in three lines on ·TL p5.**
> 1. The load-current line is **labelled $V(l)$** when it is the load *current* $I_L$, and it is
>    printed as $\frac{V_0^{+}}{Z_0} - \frac{V_0^{+}}{Z_0}$ — which is **identically zero**.
> 2. The $Z_L$ expression is printed with a **plus in the denominator**:
>    $Z_L = \left(\frac{V_0^{+}+V_0^{-}}{V_0^{+}+V_0^{-}}\right)Z_0$, which makes $Z_L = Z_0$ for
>    every load and destroys the result the next line depends on.
>
> Both are the same underlying slip. Use the corrected forms above — they are what produce the
> reflection coefficient the handout then correctly states.

**[eq]** ·TL p5 · Solving for the backward-travelling voltage and forming the ratio gives the
**voltage reflection coefficient**:

$$\boxed{\Gamma = \frac{V_0^{-}}{V_0^{+}} = \frac{Z_L - Z_0}{Z_L + Z_0}}\qquad\qquad V_{ref} = \Gamma\,V_{in}$$

·TLT p17 states it identically.

**[def]** ·TL p5 · $\Gamma$ can be complex, $\Gamma = |\Gamma|e^{j\theta_r}$, in which case there is
a **phase shift** on reflection as well as a change of amplitude.

**[def]** ·TLT p17 · On a lossless line with a **passive** load ($\mathrm{Re}\,Z_L \ge 0$), the
magnitude of the reflection coefficient satisfies $0 \le |\Gamma| \le 1$.

**[eq]** ·TL pp. 5–6 · The three cases worth memorising:

| Termination | $Z_L$ | $\Gamma$ | Consequence |
|---|---|---|---|
| **Matched** | $Z_L = Z_0$ | $0$ | **No reflection.** No standing wave |
| **Open circuit** | $Z_L \to \infty$ | $+1$ | $V_{ref} = V_{in}$ — total reflection, in phase |
| **Short circuit** | $Z_L = 0$ | $-1$ | $V_{ref} = -V_{in}$ — total reflection, inverted |

---

## § 8 · Standing waves, VSWR and return loss

·TL pp. 7–9 · ·TLT p17

**[derivation]** ·TL p7 · With $V_0^{-} = \Gamma V_0^{+}$,

$$V(z) = V_0^{+}\left(e^{-j\beta z} + \Gamma e^{+j\beta z}\right) = V_0^{+}\left(e^{-j\beta z} + |\Gamma|e^{j\theta_r}e^{+j\beta z}\right)$$

This is a complex number, so its magnitude is the square root of the product with its complex
conjugate:

$$\boxed{|V(z)| = |V_0^{+}|\Big[\,1 + |\Gamma|^2 + 2|\Gamma|\cos(2\beta z + \theta_r)\Big]^{1/2}}$$

> ⚠ **VERIFY (T8, T9) — the handout's version of this equation is broken twice on ·TL p7.**
> 1. **The brackets are missing.** It prints
>    $|V(z)| = |V_0^{+}|1 + |\Gamma|^2 + 2|\Gamma|\cos(2\beta z+\theta)^{\frac{1}{2}}$ — the
>    exponent $\tfrac12$ attaches to the cosine alone instead of to the whole sum. *This is the same
>    defect class as WC1's V10 and it is invisible in the PDF text layer; only the rendered page
>    shows it.*
> 2. **The square root is missing entirely** from the line above, which prints the product
>    $[\,V(z)\,][\,V(z)^{*}\,]$ set equal to $|V(z)|$ — despite the prose one line earlier saying
>    *"must take square root of product with complex conjugate."*
> 3. Minor, same line: $\Gamma$ is written twice in $|\Gamma|e^{j\theta}\Gamma e^{+i\beta z}$;
>    $|\Gamma|e^{j\theta}$ **is** $\Gamma$.
>
> **The correct bracketed form is printed on ·TL p11**, in the photographed slide, as
> $|\tilde{V}(d)| = |V_0^{+}|\big[1+|\Gamma|^2+2|\Gamma|\cos(2\beta d - \theta_r)\big]^{1/2}$.
> That page settles it.

**[fig]** ·TL p7 — a photographed slide (University of Utah ECE), hand-annotated *"Figure 2.11"* and
*"VSWR = $V_{max}/|V_{min}|$"*, showing $|\tilde V(z)|$ against $z$ above $|\tilde I(z)|$ against
$z$, marked at $-\lambda$, $-3\lambda/4$, $-\lambda/2$, $-\lambda/4$, $0$.

**[fig]** ·TL p8 — three textbook standing-wave patterns of $|V(z)|$ against $z$: **(A) Short
Circuit** (zero at the load, peaks of $2|V_0^{+}|$ at $\lambda/4$, $3\lambda/4$), **(B) Open
Circuit** (peak at the load, zeros at $\lambda/4$, $3\lambda/4$), **(C) Matched Termination** (a flat
line at $|V_0^{+}|$ — no standing wave at all).

**[derivation]** ·TL pp. 8–9 · **Where the maxima fall.** A maximum needs
$\cos(2\beta z + \theta_r) = 1$, so $2\beta z + \theta_r = -2n\pi$ and

$$-z_{max} = \frac{\theta_r + 2n\pi}{2\beta} = \frac{\theta_r \lambda}{4\pi} + \frac{n\lambda}{2}$$

**Where the minima fall.** A minimum needs $\cos(2\beta z + \theta_r) = -1$, so
$2\beta z + \theta_r = -(2n+1)\pi$ and

$$-z_{min} = \frac{\theta_r + (2n+1)\pi}{2\beta} = \frac{\theta_r \lambda}{4\pi} + \frac{(2n+1)\lambda}{4}$$

> ⚠ **VERIFY (T10) — the handout labels the minimum result $-z_{max}$.** ·TL p9 prints
> $-z_{max}$ on *both* results, so the same symbol names two different positions a quarter
> wavelength apart. The second one is $-z_{min}$. This is exactly the $\alpha$-labelled-$\beta$
> failure mode the index warns about for this course — **check the label against the condition that
> produced it, never against the symbol.**

**[def]** ·TL pp. 8–9 · Consequences worth holding:

- Successive **maxima** are $\lambda/2$ apart; successive **minima** are $\lambda/2$ apart.
- A maximum and its neighbouring minimum are $\lambda/4$ apart.
- **Voltage maxima coincide with current minima**, and voltage minima with current maxima.
- With no reflected signal there is **no standing wave** at all (i.e. under impedance matching).

> ⚠ **VERIFY (C25)** — ·TL p8 says *"Maximum and minima separated by half a wavelength"*, which is
> true of max-to-max and min-to-min but **false of a maximum and its adjacent minimum**, which are
> $\lambda/4$ apart. The figure directly above it on the same page shows the $\lambda/4$ spacing.

**[eq]** ·TL p9 · ·TLT p17 · The **voltage standing wave ratio**:

$$\boxed{S = \text{VSWR} = \frac{|V|_{max}}{|V|_{min}} = \frac{1+|\Gamma|}{1-|\Gamma|}}$$

**[added]** Inverted, for reading a measured VSWR back into $|\Gamma|$ — needed in every
slotted-line problem:

$$|\Gamma| = \frac{S-1}{S+1}$$

**[eq]** ·TLT p17 · The **return loss**:

$$\boxed{\text{RL} = -20\log_{10}|\Gamma|\quad\text{dB}}$$

**[def]** ·TLT p17 · $\Gamma$, SWR and RL are three expressions of **the same thing** — reflection.
Given any one you can get the other two.

---

## § 9 · Slotted-line measurement

·TL pp. 10–11 — **this section exists only in TL.**

**[fig]** ·TL p10 — a photograph of a laboratory slotted measuring line (*Messleitung / Slotted
Measuring Line*): a rigid air line with a longitudinal slit, a sliding probe carriage on a
centimetre scale, an N-type connector and a BNC detector output marked *max 10V DC*.

**[fig]** ·TL p11 — a photographed slide showing the measurement schematic: generator $V_g$ with
source impedance $Z_g$, feeding a coaxial line with a **slit**, a **sliding probe** whose **probe
tip** samples the field and runs *to detector*, a scale reading 40/30/20/10 cm, and the load $Z_L$
at the far end. Beside it, the $S$ and $\Gamma$ formulas and the correctly-bracketed
$|\tilde V(d)|$ expression.

**[added] The method.** Neither source states the procedure in steps, but both exercises below need
it, and it is the method the figures imply:

1. Read the **VSWR** $S$ off the detector → $|\Gamma| = \dfrac{S-1}{S+1}$.
2. Read the **spacing of successive minima** (or maxima) → that spacing is $\lambda/2$, so
   $\lambda = 2\times$ spacing, and $\beta = 2\pi/\lambda$.
3. Read the distance $d_{min}$ **from the load to the first minimum**. A minimum requires
   $2\beta d_{min} - \theta_r = \pi$, so $\;\theta_r = 2\beta d_{min} - \pi$.
4. Assemble $\Gamma = |\Gamma|e^{j\theta_r}$ and invert the reflection coefficient:
   $$Z_L = Z_0\,\frac{1+\Gamma}{1-\Gamma}$$
5. **Check** by recomputing $\Gamma$ from your $Z_L$ and confirming it returns the measured $S$.

Both worked instances are in § 15.

---

## § 10 · The analytical expression for transmission-line impedance

·TL p12 — **this section exists only in TL.**

**[def]** The **total impedance** looking into a lossless line of characteristic impedance $Z_0$,
terminated in $Z_L$, at a distance $z$ back from the load. The argument is written $-z$ because the
distance is measured **from the load**:

$$\boxed{Z_{in}(-z) = Z_0\,\frac{Z_L\cos\beta z + jZ_0\sin\beta z}{Z_0\cos\beta z + jZ_L\sin\beta z}}\qquad(1)$$

**[added]** Dividing top and bottom by $\cos\beta z$ gives the form most textbooks and most exam
mark schemes use:

$$Z_{in}(-z) = Z_0\,\frac{Z_L + jZ_0\tan\beta z}{Z_0 + jZ_L\tan\beta z}$$

Equation (1) is the parent of the whole of §§ 11–13: each is (1) with a particular $Z_L$ or a
particular $z$ substituted.

---

## § 11 · Short-circuit termination — the shorted stub

·TL pp. 12–13

**[derivation]** ·TL p12 · Set $Z_L = 0$ in (1). The first term of the numerator vanishes:

$$Z_{in}(-z) = \frac{jZ_0\sin\beta z}{\cos\beta z} = \boxed{jZ_0\tan\beta z}\qquad(2)$$

> ⚠ **VERIFY (C26)** — ·TL p12 prints the denominator as $\cos\beta$, dropping the $z$. The result
> $jZ_0\tan\beta z$ is right, so it is a typesetting slip, but it makes the middle step
> dimensionally meaningless as written.

**[def]** ·TL p12 · $Z_{in}$ is **purely reactive** — zero resistive part. By varying the length of
a shorted line you can synthesise **any reactance you like**:

| Length | Reactance obtained |
|---|---|
| $0 \to \lambda/4$ | **Inductive**, $X$ from $0$ to $+\infty$ |
| $\lambda/4 \to \lambda/2$ | **Capacitive**, $X$ from $-\infty$ to $0$ |

The pattern then repeats every $\lambda/2$ along the line.

**[fig]** ·TL p13 *Figure 1(a)* — imaginary part of the input impedance plotted against length in
wavelengths, from 0 to 1. A $\tan$-shaped curve: zero at $0$, rising to $+\infty$ just below $0.25$,
jumping to $-\infty$ just above $0.25$, back through zero at $0.5$, and repeating.

> ⚠ **VERIFY (C27)** — ·TL p12 says the shorted line gives "any value of capacitive reactance
> (negative X) **from 0 to ∞**", and closes with "all possible values ... from X = 0 to X = −∞",
> dropping the inductive half it had just established. Read it as $0 \to +\infty$ inductive and
> $-\infty \to 0$ capacitive, which is what the table and the figure both show.

---

## § 12 · Open-circuit termination — the open stub

·TL pp. 13–14

**[derivation]** ·TL pp. 13–14 · Set $Z_L \to \infty$ in (1). Divide numerator and denominator
through by $Z_L$:

$$Z_{in}(-z) = Z_0\,\frac{\cos\beta z + j\frac{Z_0}{Z_L}\sin\beta z}{\frac{Z_0}{Z_L}\cos\beta z + j\sin\beta z}\qquad(4)$$

As $Z_L \to \infty$ every term carrying $1/Z_L$ goes to zero:

$$\boxed{Z_{in}(-z) = -jZ_0\cot\beta z}\qquad(5)$$

**[def]** ·TL p14 · Again **purely reactive**, but the two halves are **swapped** relative to the
shorted stub:

| Length | Reactance obtained |
|---|---|
| $0 \to \lambda/4$ | **Capacitive** |
| $\lambda/4 \to \lambda/2$ | **Inductive** |

**[fig]** ·TL p13 *Figure 1(b)* — the same axes, a $-\cot$-shaped curve: starting at $-\infty$ near
zero length, rising through zero at $0.25$, to $+\infty$ just below $0.5$, and repeating.

> **The one thing to remember about §§ 11–12.** Both stubs give you a pure reactance of any value
> you want. **Which half of the first quarter-wave gives inductance depends on the termination** —
> shorted starts inductive, open starts capacitive. Get that backwards and every stub answer
> inverts.

---

## § 13 · The quarter-wave transformer

·TL pp. 14–15

**[derivation]** ·TL p14 · Substitute $z = \lambda/4$ into (1). Then
$\beta z = \frac{2\pi}{\lambda}\cdot\frac{\lambda}{4} = \frac{\pi}{2}$, so $\cos\beta z = 0$ and
$\sin\beta z = 1$, and (1) collapses to

$$\boxed{Z_{in} = Z\!\left(-\tfrac{\lambda}{4}\right) = \frac{Z_0^{2}}{Z_L}}$$

> ⚠ **VERIFY (T11) — the handout prints the substitution as $\beta z = \lambda/2$.** ·TL p14 writes
> *"Substituting $z = \lambda/4$, or $\beta z = \lambda/2$"*. It must be $\beta z = \pi/2$. As
> printed it sets an angle equal to a length. The result that follows is correct.

**[added]** Rearranged for **design** — this is the form every matching question actually needs:

$$Z_0 = \sqrt{Z_{in}\,Z_L}$$

The quarter-wave section's characteristic impedance is the **geometric mean** of the two impedances
it sits between. Neither source writes this line, but ·TL p15's example uses it silently to produce
its $150\,\Omega$.

**[fig]** ·TL p15 — the matching schematic: a box marked **Radio Transmitter**, a feedline of
$Z_0 = 75\,\Omega$, then a red section of length $\tfrac14\lambda$ with $Z_0 = 150\,\Omega$ labelled
**Impedance "transformer"**, feeding a **Dipole antenna, 300 Ω**.

---

## § 14 · The Smith chart

·TLT pp. 18–22 — **this section exists only in TLT, and nothing else in the knowledge base covers
it.**

**[def]** ·TLT p18 · The impedance formula of § 10 is "cumbersome and not intuitive", so design
calculations and measurements are often made **graphically** on a **Smith chart**. The chart works
in **normalized** impedance and admittance, normalization being with respect to the characteristic
impedance of the line.

**[eq]** ·TLT pp. 18–19 · **Normalization** — always the first step:

$$\boxed{z_L = \frac{Z_L}{Z_0}}$$

**[ex]** ·TLT p18 · A load $Z_L = 73 + j42\,\Omega$ on a $50\,\Omega$ line normalizes to
$z_{LN} = 1.46 + j0.84$. *(Verified: $73/50 = 1.46$, $42/50 = 0.84$.)*

**[def]** ·TLT p18 · From the plotted point the chart yields the **input impedance as a function of
line length**, the **reflection coefficient**, the **power delivered to the load**, and the
**VSWR**.

**[fig]** ·TLT p19 — a schematic Smith chart: the outer circle, red **constant-resistance** circles
(labelled $\mathrm{Re}\{Z\text{ or }Y\}$) and blue **constant-reactance** arcs (labelled
$\mathrm{Im}\{Z\text{ or }Y\}$), with an arrow indicating a plotted point.

**[fig] ·TLT p20 — a full blank Smith chart.** It is a complete, usable printed chart: resistance
and reactance grid, the **WAVELENGTHS TOWARD GENERATOR** and **WAVELENGTHS TOWARD LOAD** perimeter
scales, **ANGLE OF REFLECTION COEFFICIENT IN DEGREES**, and the **RADIALLY SCALED PARAMETERS** rule
at the foot (SWR, return loss in dB, reflection coefficient — voltage and power).

> **This page closes a live blocker.** `00-index.md` records *"⚠ The Smith chart is missing — two
> 2025 papers need one and neither photograph set includes it"* (erratum P22). ·TLT p20 **is** that
> chart. Print this page before attempting the 1 Oct 2025 CAT Q1(b) or the 23 Oct 2025 exam Q2(b) —
> 11 marks each, unattemptable without it.

**[def]** ·TLT p19 · **The core procedure.** To find $Z$ along the line for a particular $Z_L$:

1. Compute $z_L = Z_L/Z_0$ and **plot it**.
2. **Draw a circle** through that point centred on $1 + j0$ (the centre of the chart). This is the
   constant-$|\Gamma|$ — equivalently constant-VSWR — circle; every impedance along the line lies on
   it.
3. Points on that circle give the impedance at each distance along the line, **read off the
   "wavelengths toward the generator" scale.**

**[ex]** ·TLT pp. 20–21 · **Smith chart example.** A half-wave dipole antenna,
$Z_L = 73 + j42\,\Omega$, is connected to a $50\,\Omega$ line. *How long must the line be before the
real part of the input impedance is $50\,\Omega$?*

The deck gives the method in three steps but **stops without a numerical answer**:

> **Step 1** — plot the normalized impedance $(1.46 + j0.84)$ on the chart.
> **Step 2** — draw a circle through that point with its centre at $1 + j0$.
> **Step 3** — move along that circle **towards the generator** until you intercept the
> $\mathrm{Re}\{z_N\} = 1$ circle. The distance moved, read from the *wavelengths toward generator*
> scale, is the length $\ell$.

**[added] Solved and verified** — see § 15 Example 5 for the numbers the chart should give you.

---

## § 15 · Worked examples and exercises

Two of the five below are worked in the sources; three are stated and left unsolved. **Every answer
here has been computed and numerically verified**; the solutions tagged `[added]` are not the
lecturer's.

### Example 1 · Reflection coefficient of a series RC load — `[ex]` ·TL p6

**[fig]** A line of $Z_0 = 100\,\Omega$ terminated in $50\,\Omega$ in series with $10\ \mathrm{pF}$.

Given: $Z_0 = 100\,\Omega$, $R_L = 50\,\Omega$, $C_L = 10\ \mathrm{pF}$, $f = 100\ \mathrm{MHz}$.

$$Z_L = R_L + \frac{1}{j\omega C_L} = R_L - \frac{j}{\omega C_L}$$

$$Z_L = 50 - \frac{j}{2\pi(10^{8})(10^{-11})} = (50 - j159)\,\Omega$$

$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = \frac{50 - j159 - 100}{50 - j159 + 100} = \frac{-50 - j159}{150 - j159}$$

Rationalizing the denominator:

$$\Gamma = 0.3721 - j0.6655 = 0.76\,\angle\,{-60.8}^{\circ}$$

**Verified** ·[added]: recomputing gives $Z_L = 50 - j159.15\,\Omega$ and
$\Gamma = 0.3728 - j0.6655 = 0.7628\,\angle\,{-60.74}^{\circ}$ — the handout's figures to rounding.

> ⚠ **VERIFY (T12) — the handout states $f = 100\ \mathrm{Hz}$ but substitutes $10^{8}$.** ·TL p6
> prints "$f = 100\ Hz$" and then uses $(2\pi)(10^{8})(10^{-11})$, i.e. **100 MHz**. The
> substitution is right and the label is wrong. *Checked [added]:* at a true 100 Hz,
> $Z_L = 50 - j1.59\times10^{8}\,\Omega$, giving $|\Gamma| = 1.0000$ — the load would look like an
> open circuit and the whole example would collapse. **Read it as 100 MHz.**

### Example 2 · Quarter-wave transformer, transmitter to antenna — `[ex]` ·TL p15

A radio transmitter has an output impedance of $75\,\Omega$; the antenna input is $300\,\Omega$. The
characteristic impedance of the quarter-wave transformer is chosen so that the input to the
transformer is $75\,\Omega$.

$$Z_{in} = \frac{Z_0^{2}}{Z_L} = \frac{150^{2}}{300} = 75\,\Omega$$

The system is therefore matched, since the transmitter output equals the transformer input.

**[added]** The handout produces $Z_0 = 150\,\Omega$ without showing where it comes from. It is the
design formula of § 13: $Z_0 = \sqrt{Z_{in}Z_L} = \sqrt{75 \times 300} = \sqrt{22500} = 150\,\Omega$.
**Verified**: $150^2/300 = 75.0\,\Omega$ exactly.

### Example 3 · Slotted line on a 50 Ω line — `[exercise]` ·TL p11 · **stated, not solved**

> *A slotted line probe is used to measure the voltage as a function of position on a $50\,\Omega$
> line. A standing wave ratio of 3 is found and successive minima were 30 cm apart and the first
> minimum was 12 cm from the load. Determine the load impedance.*

**[added] Solution** (method of § 9):

$$|\Gamma| = \frac{S-1}{S+1} = \frac{3-1}{3+1} = 0.5$$

Successive minima are $\lambda/2$ apart, so $\lambda = 2(0.30) = 0.60\ \mathrm{m}$ and

$$\beta = \frac{2\pi}{\lambda} = \frac{2\pi}{0.60} = 10.472\ \mathrm{rad/m}$$

$$\theta_r = 2\beta d_{min} - \pi = 2(10.472)(0.12) - \pi = 2.5133 - 3.1416 = -0.6283\ \mathrm{rad} = -36.0^{\circ}$$

$$\Gamma = 0.5\,\angle\,{-36.0}^{\circ} = 0.40451 - j0.29389$$

$$Z_L = Z_0\,\frac{1+\Gamma}{1-\Gamma} = 50\cdot\frac{1.40451 - j0.29389}{0.59549 + j0.29389}$$

$$\boxed{Z_L = 85.04 - j66.65\ \Omega}$$

**Verified**: substituting back, $\Gamma = (Z_L-50)/(Z_L+50)$ gives $|\Gamma| = 0.500000$ at
$-36.000^{\circ}$, hence $S = 3.000000$ — the measured value recovered exactly. The negative
reactance is consistent with the first minimum falling **closer to the load than $\lambda/4$**
(12 cm against 15 cm), i.e. a capacitive load.

### Example 4 · Slotted line on a 200 Ω line — `[exercise]` ·TL p11 · **stated, not solved**

From the photographed slide, *[Example 2-6] Find $Z_L$ of a Slotted Line*:

> *A slotted line of characteristic impedance $200\,\Omega$, $S = 2$. The distance between
> successive voltage maxima = 4 cm. The first voltage minimum is located at 3 cm from the load.*

**[added] Solution**:

$$|\Gamma| = \frac{2-1}{2+1} = \frac{1}{3} = 0.3333$$

Successive maxima are $\lambda/2$ apart, so $\lambda = 0.08\ \mathrm{m}$ and
$\beta = 2\pi/0.08 = 78.540\ \mathrm{rad/m}$.

$$\theta_r = 2\beta d_{min} - \pi = 2(78.540)(0.03) - \pi = 4.7124 - 3.1416 = 1.5708\ \mathrm{rad} = 90.0^{\circ}$$

$$\Gamma = \tfrac13\,\angle\,90^{\circ} = 0 + j0.33333$$

$$\boxed{Z_L = 160 + j120\ \Omega}$$

**Verified**: back-substitution returns $|\Gamma| = 0.333333$ at $90.000^{\circ}$ and
$S = 2.000000$. The exact round numbers are a good sign the reading of the slide is correct.

### Example 5 · Smith chart, dipole on a 50 Ω line — `[exercise]` ·TLT pp. 20–21 · **method given, no answer**

> *A half-wave dipole antenna ($Z = 73 + j42\,\Omega$) is connected to a $50\,\Omega$ transmission
> line. How long must that line be before the real part of the input impedance is $50\,\Omega$?*

**[added] Solution.** Normalize: $z_L = (73+j42)/50 = 1.46 + j0.84$ — the deck's own value.

The constant-VSWR circle through that point is characterised by

$$\Gamma = \frac{Z_L-Z_0}{Z_L+Z_0} = 0.3684\,\angle\,42.44^{\circ}\qquad S = \frac{1+0.3684}{1-0.3684} = 2.167\qquad \text{RL} = 8.67\ \mathrm{dB}$$

Moving toward the generator to the first intercept with the $\mathrm{Re}\{z_N\} = 1$ circle:

$$\boxed{\ell = 0.154\,\lambda}\qquad\text{at which}\qquad Z_{in} = 50 - j39.6\ \Omega$$

**Verified** by solving $\mathrm{Re}\left\{\dfrac{z_L + j\tan\beta\ell}{1 + jz_L\tan\beta\ell}\right\} = 1$
numerically: roots at $\ell = 0.15392\lambda$ ($Z_{in} = 50.000 - j39.630$) and
$\ell = 0.46397\lambda$ ($Z_{in} = 50.000 + j39.630$). The chart procedure as written — *first*
intercept moving toward the generator — gives the former. Reading $0.154\lambda$ off ·TLT p20's
scale to two decimal places is realistic; expect $\approx 0.15\lambda$ by hand.

> **Why this is the exam-shaped example.** Both 2025 Smith-chart questions are this task with
> different numbers, and both ask for VSWR, $\Gamma$ and $Z_{in}$ off one chart construction.

### Revision questions — `[exercise]` ·TL pp. 15–16 · **stated, not solved**

**1.** *Show how a transmission line can be used to realize each of the following components:*
*(i) a capacitor; (ii) an inductor; (iii) a quarter wave transformer.*

**[added] Answer sketch** — this is §§ 11–13 read back:

- **(i) A capacitor** — a **shorted** stub of length between $\lambda/4$ and $\lambda/2$, where
  $Z_{in} = jZ_0\tan\beta z$ is negative; *or* an **open** stub shorter than $\lambda/4$, where
  $Z_{in} = -jZ_0\cot\beta z$ is negative. Set $|X|$ to $1/(\omega C)$ and solve for the length.
- **(ii) An inductor** — the complements: a **shorted** stub shorter than $\lambda/4$, or an
  **open** stub between $\lambda/4$ and $\lambda/2$. Set $|X| = \omega L$.
- **(iii) A quarter-wave transformer** — a section exactly $\lambda/4$ long whose characteristic
  impedance is $Z_0 = \sqrt{Z_{in}Z_L}$, giving $Z_{in} = Z_0^2/Z_L$.

**2.** *A dipole antenna has an input impedance of $73\,\Omega$ at $400\ \mathrm{MHz}$. It is desired
to feed this antenna using coaxial cable of characteristic impedance $Z_0 = 50\,\Omega$. Determine
the impedance and the length of a quarter wavelength transformer that may be used to achieve
impedance matching between the antenna and the feedline.*

**[added] Solution**:

$$Z_0' = \sqrt{Z_{in}Z_L} = \sqrt{50 \times 73} = \sqrt{3650} = 60.42\ \Omega$$

$$\lambda = \frac{c}{f} = \frac{3\times10^{8}}{400\times10^{6}} = 0.75\ \mathrm{m}\qquad\Longrightarrow\qquad \frac{\lambda}{4} = 0.1875\ \mathrm{m} = 18.75\ \mathrm{cm}$$

$$\boxed{Z_0' = 60.4\ \Omega,\qquad \ell = 18.75\ \mathrm{cm}}$$

**Verified**: $60.4152^2/73 = 50.000\,\Omega$ — the transformer does present $50\,\Omega$ to the
feedline. Using $c = 2.998\times10^{8}$ gives $\lambda/4 = 18.74$ cm; the difference is immaterial.

> **[added] State the assumption.** The question gives no dielectric constant, so this assumes the
> wave travels at $c$ in the transformer section. A real coaxial transformer with
> $\varepsilon_r \approx 2.25$ would be shorter by $\sqrt{\varepsilon_r}$, i.e. $\approx 12.5$ cm.
> Say which you assumed — it is the kind of thing that earns or loses the last mark.

---

## Verification summary — 24 flags

Full detail in `_verification-log.md` **§ T**. **12 substantive** (T1–T12), **12 cosmetic**
(C24–C35).

**The physics in both documents is sound. TL's transcription is not** — it carries defects at a
higher rate than WC1 did, and they cluster in the same two places.

**1 · The wrong differential variable.** TL's telegrapher's equations (T1, T2) print
$\partial/\partial t$ where $\partial/\partial z$ is meant, in three equations across pp. 1–2. The
handout corrects itself silently a page later without comment; a reader who stops early learns the
wrong equation. **TLT p7 is the clean reference.**

**2 · Dropped and duplicated superscripts.** $V_0^{+}$ appears where $V_0^{-}$ belongs, three times
(T5, T6), each time producing an expression that is identically zero or identically $Z_0$ — that is,
each time destroying the very result being derived. ·TL p5's $Z_L$ expression is the worst: as
printed, every load is matched.

Other substantive defects a learner should **not** absorb:

- **·TL p4** — phasor equations 8 and 9 printed with $-j\omega L$ and $-j\omega C$; both are $+$ (T3)
- **·TL p7** — the standing-wave magnitude missing its brackets *and* its square root (T8, T9).
  *The bracket error is invisible in the PDF text layer — only the rendered page shows it, exactly as
  with WC1's V10*
- **·TL p9** — the voltage **minimum** position labelled $-z_{max}$ (T10)
- **·TL p14** — $\beta z = \lambda/2$ where $\beta z = \pi/2$ is meant (T11)
- **·TL p6** — $f = 100$ Hz stated, $10^{8}$ substituted; the example only works at 100 MHz (T12)
- **·TLT p13** — backward-wave term printed $e^{j\gamma}$ for $e^{+\gamma z}$ (T4)

### Cross-cohort pattern — this confirms the index's standing warning

`00-index.md` records, from WC1 and the old-cohort files: *"Treat every $\alpha$/$\beta$/$\sigma$
label in propagation-constant material from this course as suspect until dimensionally checked."*
**T10 is that same failure in a new document** — a position labelled $max$ that is a $min$. The
warning now extends to **every subscript label in this course's material**, not just the Greek ones.

**Two habits that catch most of the above**, both carried over from WC1:

1. **Check what the left-hand side is a derivative of before substituting.** T1, T2 and T11 all fail
   on sight.
2. **Distrust any expression whose two sides collapse to something trivial.** T5 and T6 give
   $I_L = 0$ and $Z_L = Z_0$ respectively — both absurd, both visible without any algebra.

---

## Provenance notes

- All 16 pages of TL and all 22 of TLT were **rendered at 200 dpi and read directly**. The PDF text
  layer mangles the mathematics in both; T8 in particular is invisible without the render.
- Every figure in both documents is described above from the rendered page. **No page currently
  requires a screenshot.**
- ·TL p7 and ·TL p11 are **photographs of other people's slides** pasted into the handout (one
  carries a University of Utah ECE logo, one is a phone photo of a printed page with "ld notes"
  visible at its foot). They are legible and their content is transcribed, but they are not the
  lecturer's own typesetting and should not be cited as such.
- ·TL p10 is a product photograph of a slotted line with no instructional content.
- **Five examples were solved and numerically verified here** (§ 15). Two are the lecturer's own
  worked examples; three were stated in the sources without solutions. All solutions are tagged
  `[added]` — they are not the lecturer's.
- Nothing was invented. Where a source is silent — the slotted-line procedure, the $Z_0 = \sqrt{Z_{in}Z_L}$
  design form, the dielectric assumption in Revision Q2 — it is tagged `[added]` and said out loud.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
