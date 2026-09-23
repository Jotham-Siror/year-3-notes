---
kb: "MEC 3104 Fluid Theory"
file_role: verification-log
purpose: "Every flagged discrepancy between a slide and an independently checked standard form. Spot-check basis (suspicious items only), per user instruction. Slide-faithful content is preserved in the topic files; nothing is silently 'corrected'."
scale: "started with section 06; grows as remaining sections are processed"
covers: "lecture slides (§ Section NN blocks) AND assessment papers (§ Exam papers, IDs P1, P2, …)"
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

# Verification log

Format per entry: **·slide N** — what the slide says → the issue → checked standard form → source.
Severity: `error` (wrong result), `notation` (dimensionally/typographically loose but intent clear),
`typo` (trivial), `ok-nonstandard` (unusual but defensible).

---

## Section 06 — Energy & Bernoulli

### ·slide 249 — Pitot velocity, notation
- **Slide:** $v_A=\sqrt{2g\,(p_B - p_A/\rho g)}$.
- **Issue:** mixes a pressure ($p_B$) and a head ($p_A/\rho g$) inside the same root — dimensionally
  inconsistent as written.
- **Standard form:** $v_A=\sqrt{2g\,(p_B/\rho g - p_A/\rho g)} = \sqrt{2(p_B-p_A)/\rho} = \sqrt{2gH}$. The
  lecturer's surrounding steps (slides 249–250) use the correct $\sqrt{2gH}$, so this is a transcription slip
  in one line, not a wrong result.
- **Severity:** notation.
- **Source:** Engineering ToolBox, "Pitot Tubes" — $v=\sqrt{2(p_t-p_s)/\rho}$
  (https://www.engineeringtoolbox.com/pitot-tubes-d_612.html); Pitot tube, Wikipedia
  (https://en.wikipedia.org/wiki/Pitot_tube).

### ·slide 230 — Daniel Bernoulli dates, typo
- **Slide:** "Daniel Bernoulli 1700 – 1783".
- **Issue:** death year. Daniel Bernoulli died 17 March **1782**.
- **Severity:** typo (biographical). Source: standard biographical record.

### ·slide 238 — units typo
- **Slide:** velocity $v_2$ printed as "4.59 m/2".
- **Issue:** "m/2" is a typo for "m/s". Value 4.59 m/s is correct for the given data.
- **Severity:** typo.

## Section 02 — History

### ·slide 21 — Leonardo da Vinci dates, error
- **Slide:** "Leonardo da Vinci 14th April 1452 – 2nd May 1514".
- **Issue:** birth day and death year both wrong.
- **Correct:** born **15 April 1452** (Vinci), died **2 May 1519** (Amboise).
- **Severity:** error (factual/biographical) — worth correcting since a learner would otherwise memorize 1514.
- **Source:** Britannica (https://www.britannica.com/biography/Leonardo-da-Vinci); Wikipedia
  (https://en.wikipedia.org/wiki/Leonardo_da_Vinci); MacTutor
  (https://mathshistory.st-andrews.ac.uk/Biographies/Leonardo/).

### ·slide 29 — Kirchhoff spelling, typo
- **Slide:** "Kirchoff".
- **Correct:** **Kirchhoff** (Gustav Robert Kirchhoff). His 1869 free-streamline value 0.611 = π/(π+2) is correct.
- **Severity:** typo.

## Section 03 — Fluid Properties

### ·slide 33 — molecular mean free path, unit error
- **Slide:** mean free path "about 0.06 pm".
- **Issue:** 0.06 pm = 6×10⁻¹⁴ m (nuclear scale) — physically impossible for a molecular mean free path.
- **Correct:** air at STP ≈ **68 nm ≈ 0.068 µm**; intended unit is **µm**, not pm.
- **Severity:** error (unit, ~6 orders of magnitude).
- **Source:** Mean free path, Wikipedia (https://en.wikipedia.org/wiki/Mean_free_path).

### ·slide 45 — "liquids 3× denser than gases", likely order-of-magnitude slip
- **Slide:** "liquids are 3 times denser than gases at 1 atm".
- **Issue:** water (~1000 kg/m³) vs air (~1.2 kg/m³) ≈ 800–1000×. "3 times" is wrong if literal.
- **Read as:** ~**3 orders of magnitude** (≈10³×). Severity: error/ambiguous wording.

### ·slide 44 — units-table minor typos
- 1 m³ printed as "35.335 ft³" → standard **35.315 ft³**; BG viscosity "slug/m/s" → **slug/(ft·s)**;
  "Lbg/ft²" → **lbf/ft²**. Severity: typo (do not memorize the 35.335 value).

## Section 04 — Fluid Statics

### ·slide 102 — standard-atmosphere structure, errors
- **Slide:** "0.65 °C/100 m lapse in the troposphere up to ≈1 km; constant −50.5 °C from 1 km to 10 km."
- **Issue:** boundaries and the isothermal temperature are wrong.
- **Correct (International Standard Atmosphere):** the 6.5 °C/km lapse continues through the whole troposphere to
  ≈**11 km**, reaching ≈ **−56.5 °C** at the tropopause; the isothermal −56.5 °C layer is the lower stratosphere,
  ≈**11–20 km**. Slide's 1/10/−50.5 look like digit errors for 11/20/−56.5.
- **Severity:** error (consistent with the deck's own troposphere index n=1.235, which uses the full-troposphere lapse).
- **Source:** International Standard Atmosphere, Wikipedia
  (https://en.wikipedia.org/wiki/International_Standard_Atmosphere); Lapse rate, Wikipedia
  (https://en.wikipedia.org/wiki/Lapse_rate).

## Section 07 — Momentum (several confirmed slide errors)

### ·slide 266 — impulse–momentum sign
- **Slide:** $F = (Mv_1 - Mv_2)/t$. **Correct:** $F = (Mv_2 - Mv_1)/t = \dot m(v_2-v_1)$ (final − initial).
- **Severity:** error (sign). Confirmed on rendered slide.

### ·slide 271 — resultant force sign
- **Slide:** $F = \sqrt{F_x^2 - F_y^2}$. **Correct:** $F = \sqrt{F_x^2 + F_y^2}$.
- **Severity:** error. Confirmed on rendered slide (viewed PDF page 271).

### ·slide 277 — moving-plate jet force, wrong power of v
- **Slide:** $F = \rho Q(v-u)^2\sin\theta / v^2$. **Correct:** $/v$ (i.e. $\rho Q(v-u)^2\sin\theta/v$).
- **Reason:** the slide's own $Q'=Q(v-u)/v$ with $F=\rho Q'(v-u)\sin\theta$ gives $/v$; and $/v^2$ is
  dimensionally not a force (yields kg/s).
- **Severity:** error. Confirmed on rendered slide (viewed PDF page 277).

### ·slides 291 & 295 — impeller torque uses peripheral u instead of absolute v
- **Slide:** $T = \dot m(r_2 u_2\cos\alpha_2 - r_1 u_1\cos\alpha_1)$.
- **Correct (Euler turbomachine eqn):** $T = \dot m(r_2 v_2\cos\alpha_2 - r_1 v_1\cos\alpha_1)$ — the moment of
  momentum uses the tangential component of the **absolute** velocity $v\cos\alpha$ (α defined on slide 293 as
  the angle of the absolute velocity $v$ to the peripheral velocity $u$). The linear-momentum version on slide
  271 correctly uses $v$.
- **Severity:** error. Confirmed on rendered slides (viewed PDF pages 291, 295).
- **Source (standard form):** Euler's turbomachine equation, e.g. White, *Fluid Mechanics*; Wikipedia
  (https://en.wikipedia.org/wiki/Euler%27s_pump_and_turbine_equation).

## Section 08 — Viscous Flow

### ·slide 382 — sinusoidal BL profile sin vs cos
- **Slide:** velocity profile "$v = v_{max}\cos(\pi y/2\delta)$".
- **Issue:** the slide's own $dv/dy$ and its numerical answers (τ max at wall y=0, ≈0 at edge y=δ) correspond to
  $v = v_{max}\sin(\pi y/2\delta)$ (zero at wall, peak at edge — the physical BL shape). "cos" is a typo for "sin".
- **Severity:** notation/typo; the numbers (0.0366/0.0259/~1e-4 Pa) are consistent with the sin profile.

## Section 10 — Open-Channel Flow

### ·slide 493 — Manning n typo
- **Slide (problem):** "n = 0.12 (relatively smooth concrete)". **Correct:** **n = 0.012** — used in the worked
  solution on slide 495 (concrete ≈ 0.012–0.015). "0.12" is 10× too large.
- **Severity:** typo. (Bazin coefficient shown here in the standard hydraulic-radius form $c=87/(1+\alpha/\sqrt m)$.)

## Section 11 — Drag and Lift

### ·slide 531 — flat-plate wall shear coefficient
- **Slide:** $\tau_0 = 3.65\sqrt{\mu\rho U^3/x}$.
- **Issue:** coefficient 3.65 is physically implausible (implies $C_f\approx7$). Standard laminar flat-plate
  wall shear is $\tau_0 = 0.332\sqrt{\rho\mu U^3/x}$ (Blasius; momentum-integral estimates ≈0.33–0.37).
- **Read as:** decimal-point slip → **≈0.33–0.365**. Severity: error (numeric). (δ=5.48√(νx/U) is a defensible
  form and kept.)

### ·slide 560 — flat-plate C_D constant
- **Slide (problem):** "$C_D = 0.31/Re^{1/7}$". **Correct:** $C_D = 0.031\,Re^{-1/7}$ — used in the worked
  solution (slide 561, giving C_D=0.00249). "0.31" is 10× too large. Severity: typo.

### ·slide 572 — moment coefficient label
- **Slide:** third force line printed as "$L = C_M\,l\,\rho U^2/2$". Should be **$M$** (moment), not L.
  Severity: typo/label.

<!-- Later sections append their own "## Section NN" blocks below. -->

---

## Exam papers

Defects in the actual assessment papers (not the lecture deck). Entry IDs are `P1`, `P2`, … and are
referenced by a `⚠ VERIFY` marker at the matching question in `past-papers/<paper>.md`. Per his instruction the
full entry lives here only — the paper file just points to it.

### P1 · MEC 3104 CAT 1 (19 Aug 2025), Q3 and Q5 — specific weight, wrong units
- **Paper:** "Take specific weight, γ, of water as **9.79 N m/s²**" (Q3), and "γ_w = **9.79 N m/s²**" (Q5).
- **Issue:** specific weight is weight per unit volume, so its units are **N/m³**, not "N m/s²" (which is not a
  unit of anything standard). The *value* 9.79 is the kN/m³ figure for water near 20 °C.
- **Correct form:** $\gamma_w = 9.79\ \text{kN/m}^3 = 9790\ \text{N/m}^3$ — consistent with
  $\gamma = \rho g = 998 \times 9.81 \approx 9790\ \text{N/m}^3$.
- **How to handle:** use 9790 N/m³ and say the printed unit is a slip. Answers in newtons come out sensible;
  taking "9.79 N/m³" literally gives forces ~1000× too small.
- **Severity:** notation (unit). Affects Q3 and Q5 numerically if copied blindly.

### P2 · MEC 3104 CAT 1 (19 Aug 2025), Q6(c) — statement missing
- **Paper:** Q6 is worth 3 marks and lists items **a.**, **b.**, **c.** — but **c. is blank**; no statement is printed.
- **Issue:** with 1 mark per true/false item, (c) was clearly meant to carry text. Confirmed blank on two separate
  photographs of the page, so this is a defect in the printed paper, not a cropped photo.
- **How to handle:** answer (a) and (b); flag (c) to the lecturer. When setting this as a mock, mark Q6 out of 2
  or substitute a comparable true/false item and say so.
- **Severity:** omission (paper defect).

### P3 · MEC 3104 CAT 1 (19 Aug 2025), Q8(b) — truncated instruction
- **Paper:** "State, with reason(s) whether the flow is **laminar**".
- **Issue:** as printed the question presupposes its own answer. Standard phrasing is "whether the flow is laminar
  **or turbulent**", judged against the pipe-flow transition (Re ≲ 2300 laminar, ≳ 4000 turbulent).
- **Severity:** notation (wording). Intent unambiguous.

### P4 · MEC 3104 CAT 1 (19 Aug 2025), Q9 — vorticity notation and axis label
- **Paper:** "Vorticity, ζ, **along the x-axis** … $\zeta = (\delta v/\delta x - \delta u/\delta y)$".
- **Issue (two):** (i) δ is used where the **partial derivative ∂** is meant; (ii) $\partial v/\partial x -
  \partial u/\partial y$ is the **z-component** of vorticity (rotation in the x–y plane), not a component
  "along the x-axis".
- **Correct form:** $\zeta_z = \dfrac{\partial v}{\partial x} - \dfrac{\partial u}{\partial y}$; flow is
  irrotational where this vanishes everywhere.
- **How to handle:** the intended working is unaffected — use the expression as given, but teach the correct
  symbol and the correct axis. Cross-ref `05-flow-fundamentals` (vorticity & circulation).
- **Severity:** notation.
- **Refinement (2026-08-03, from tracing the paper to its slides):** the two halves of this erratum have
  different owners. The **δ-for-∂ slip is inherited from the deck** — slide 195 also prints
  "ζ = (δv/δx − δu/δy)". But the **axis label is the paper's own error**: slide 195 says
  "ζ = vorticity **for z-axis**", which is correct; the CAT changed it to "along the x-axis", which is not.
  So when teaching this, say the notation slip came from the slides but the axis error did not.

### P5 · MEC 3104 CAT 1 (19 Aug 2025), Q5(b) — datum for X not defined
- **Paper:** "the center of pressure is given by $-I_{xx}\sin\theta / h_{cg}A$" and asks for "the position, **X**,
  of its center of pressure"; the figure marks X with an arrow running along the gate from near **A**.
- **Issue:** the printed formula returns the offset **from the centroid** of the gate (negative = below it), but the
  figure appears to measure X **from A**. The two differ by half the gate length (0.5 m here). The question never
  states the datum.
- **How to handle:** compute the centroid offset from the given formula, then state the answer **both ways**
  ("… below the centroid, i.e. … from A") and name the datum explicitly. That earns the marks under either reading.
- **Severity:** ambiguity (question defect). Also note the printed formula lacks brackets: read as
  $-I_{xx}\sin\theta/(h_{cg}A)$.

### P6 · MEC 3104 CAT 1 (19 Aug 2025), Q6(b) and Q7 — spelling
- **Paper:** "**Langrarian** flow" (Q6b) → **Lagrangian** (after Joseph-Louis Lagrange). "**Reynold's** number"
  (Q7, Q8a) → **Reynolds** number (after Osborne Reynolds — no apostrophe).
- **Severity:** typo. No effect on the physics; worth knowing so he spells them correctly in an answer script.

### P7 · SCE 3104 CAT 1 (14 Aug 2024), Q2 stem — Reynolds number written as vd/μ
- **Paper:** "the factor **vd/μ** (later known as Reynold's number) gave a constant figure in his experiments."
- **Issue:** $vd/\mu$ is not Reynolds number and is not dimensionless — the density is missing. Reynolds number is
  $Re = \rho v d/\mu$ (μ = **dynamic** viscosity) or equivalently $Re = vd/\nu$ (ν = **kinematic** viscosity).
- **Correct form:** $Re = \dfrac{\rho v d}{\mu} = \dfrac{v d}{\nu}$.
- **How to handle:** the data supplied is a **kinematic** viscosity (7.5 × 10⁻⁵ m²/s), so the form actually needed
  is $Re = vd/\nu$ — no density required. Worth showing alongside the 2025 CAT's Q7, which states it correctly
  as ρvd/μ: same quantity, two valid forms, and the symbol is the whole trap.
- **Severity:** error as written; intent recoverable from the data given.
- **Source:** Reynolds number, Wikipedia (https://en.wikipedia.org/wiki/Reynolds_number).

### P8 · SCE 3104 CAT 1 (14 Aug 2024), Q2 — duplicated item letter
- **Paper:** Question Two's stem is labelled "a.", and the two sub-parts below it are then labelled "a." and "b."
  as well — two items called "a." in one question.
- **How to handle:** the stem is context, not a graded part. The graded parts are the 5-mark Re calculation and
  the 1-mark laminar/turbulent statement (6 marks total, which is what the reconciliation to 40 assumes).
- **Severity:** typo (structural). No effect on the physics.

### P9 · SCE 3104 CAT 1 (14 Aug 2024), Q4(a) — a velocity called a flow rate
- **Paper:** "into water in a larger pipe of radius 8 cm **whose flow rate is 6.3 m/s**".
- **Issue:** m/s is a velocity; a volumetric flow rate would be m³/s or L/min. The printed expression
  $P_2-p_1 = \rho\frac{d^2}{D^2}\frac{(D^2-d^2)}{D^2}(v_0-v_1)^2$ takes a **velocity** $v_1$ at that station.
- **Correct reading:** $v_1 = 6.3$ m/s is the velocity of the surrounding stream in the larger pipe;
  $v_0 = 8.9$ m/s is the jet velocity. Note also that **radii** are given but the formula takes **diameters**.
- **Severity:** notation (wrong word, unambiguous value).

### P10 · SCE 3104 CAT 1 (14 Aug 2024), Q4(b) — a 5 cm hole in a question about a weir
- **Paper:** "In the Weir below, water gushes out from a **hole of diameter 5 cm** in the wall. The width of the
  water wall is 1 meter and the height 70 cm."
- **Issue:** three mutually inconsistent descriptions. The figure shows a **rectangular sharp-crested weir** (a
  full-width overflow); the supplied integrand $dQ = C\,b\,(2gz)^{1/2}\,dz$ is the **weir** strip equation with
  width $b$; neither involves a 5 cm circular orifice. An orifice would need $Q = C_d A\sqrt{2gh}$ instead, and
  the 1 m width would then be irrelevant.
- **Correct reading:** treat it as the weir the figure and the integral describe — $b = 1$ m, $H = 0.70$ m. The
  5 cm diameter appears to be left over from a different question.
- **How to handle:** integrating the given strip equation from $z=0$ to $z=H$ gives
  $Q = \tfrac{2}{3}\,C\,b\,\sqrt{2g}\,H^{3/2}$. Show him the contradiction rather than quietly picking a reading —
  this is one to raise with the lecturer.
- **Severity:** error (contradictory data).

### P11 · SCE 3104 CAT 1 (14 Aug 2024), Q4(b) — "coefficient of discharge as 3.2"
- **Paper:** "Take the coefficient of discharge as **3.2**".
- **Issue:** a coefficient of discharge is **dimensionless and less than 1** — about 0.60–0.65 for a sharp-crested
  rectangular weir. 3.2 is the magnitude of an **imperial weir coefficient** (Francis: $Q = 3.33\,b\,H^{3/2}$ with
  $b$, $H$ in feet, $Q$ in ft³/s), a constant that has already absorbed $\tfrac{2}{3}\sqrt{2g}$.
- **Consequence:** substituting 3.2 as $C$ into $Q=\tfrac{2}{3}Cb\sqrt{2g}H^{3/2}$ **double-counts** gravity, and
  the result is not dimensionally meaningful in SI.
- **How to handle:** work it symbolically, state the assumption about $C$ explicitly, and say plainly that the
  constant as given is inconsistent with the SI data elsewhere on the paper. Needs the lecturer to resolve.
- **Severity:** error / ambiguity — unresolved.
- **Source:** Chow, *Open-Channel Hydraulics*, ch. 14 (weir coefficients); Engineering ToolBox, "Weirs".

### P12 · SCE 3104 CAT 1 (14 Aug 2024), Note block — units of g
- **Paper:** "Gravity (g) = **9.81 N**".
- **Issue:** g is an acceleration, so **9.81 m/s²**. A newton is a force.
- **Severity:** typo (unit).
- **Pattern worth naming to him:** this is the same class of slip as **P1** on the 2025 CAT (specific weight
  printed as "N m/s²"). Both papers misprint a unit in the data block. Check units before substituting.

### P13 · SCE 3104 CAT 1 (14 Aug 2024), Q2 and Q3 — names and notation
- **Paper:** "**Osborne Reynold**" and "**Reynold's** number" (Q2); Euler's equation printed as
  $v\frac{\partial v}{\partial s} = -\frac{1}{\rho}\frac{\delta P}{\delta s} - g\frac{dz}{ds}$ (Q3).
- **Correct:** **Osborne Reynolds**; **Reynolds number** (no apostrophe). In the equation, δ is used where the
  partial derivative **∂** is meant, and both $P$ and $p$ appear for pressure between the equation and its figure.
- **Severity:** typo / notation. No effect on the result. (Same ∂/δ slip as **P4** on the 2025 CAT, and the same
  "Reynold's" as **P6**.)


### P14 · MEC 3104 CAT 1 (19 Aug 2025), Q6(b) — tests a term that is not in the course notes
- **Paper:** "In a Langrarian flow, one particle is followed along the flow." (true/false, 1 mark)
- **Finding:** all 594 slides of the lecture deck were searched for **Lagrang** and **Euleri** — **zero hits for
  both**. The deck teaches streamline, streakline, pathline and stream tube (slides 172–174) and defines steady
  flow (175), but never introduces the Lagrangian/Eulerian pair of descriptions. "Control volume" appears
  (s6, 267, 268, 273) but only in the momentum context, never contrasted with a particle-following description.
- **Status of the statement itself:** as printed it is **true** in standard fluid mechanics — the Lagrangian
  description follows an individual fluid particle along its path, while the Eulerian description watches fixed
  points in space. (Separate from the "Langrarian" → **Lagrangian** spelling already logged as P6.)
- **How to handle:** teach the Lagrangian/Eulerian distinction explicitly before setting this paper — it cannot
  be revised from his notes. Worth raising with the lecturer that it was examined without being taught.
- **Severity:** out-of-syllabus (question defect).

### P15 · MEC 3104 CAT 1 (19 Aug 2025), Q1 — method not taught in the deck
- **Paper:** "Given that this relationship is dimensionally consistent, determine the dimensions of α." (2 marks)
- **Finding:** the deck supplies the **ingredients** — primary dimensions {M},{L},{T} on slide 41 and a table of
  secondary dimensions with their formulas (Area {L²}, Pressure {ML⁻¹T⁻²}, Energy {ML²T⁻²}) on slides 43–44 —
  but a search of all 594 slides for *dimensional homogeneity*, *dimensionally consistent*, *dimensional
  analysis*, *Buckingham*, *Rayleigh* and *π theorem* returns **zero hits**. The technique of balancing
  dimensions across an equation to solve for an unknown coefficient is never demonstrated.
- **How to handle:** unlike P14 this is answerable from the notes, but only by a student who invents the method.
  Teach the method from slides 41–44 rather than assuming it.
- **Severity:** partial gap (teachable from the notes, but not taught in them).

### P16 · MEC 3104 CAT 2 (9 Oct 2024), Q1(b) — dimensions marked in feet, note says inches
- **Paper:** the Pitot figure carries "**15.5′**" and "**18.6′**"; the line printed under it reads
  "Note that the dimensions are given in **inches**."
- **Issue:** ′ is the foot mark (inches take ″). As drawn the two readings claim to be 15.5 ft and 18.6 ft,
  while the note says inches — the figure and its own caption disagree.
- **Correct reading:** **inches**, per the explicit note. The head is then a few inches, which is what gives an
  ordinary pipe velocity; taking the readings as feet inflates the velocity by √12 ≈ **3.46×**.
- **How to handle:** convert to feet before substituting either way, because the only g offered in imperial
  units is 32.2 ft/s². Say plainly that the tick marks on the figure are wrong, not the note.
- **Severity:** notation (unit symbol). Changes the answer by a factor of 3.46 if read literally.

### P17 · MEC 3104 CAT 2 (9 Oct 2024), Q1(b) — the head *h* is never defined
- **Paper:** "The velocity is given by: $C_f\sqrt{2gh}$" — and the figure labels two column heights, 15.5 and
  18.6, both measured from the pipe centreline. The symbol **h appears nowhere on the drawing**.
- **Issue:** in a Pitot–static measurement $h$ is the **difference** between the stagnation column and the
  static column, not either reading on its own. The paper never says so.
- **Correct reading:** $h = 18.6 - 15.5$ in the units of P16. The shared datum (the pipe centreline) cancels
  in the subtraction, which is precisely why measuring both columns from it is legitimate.
- **How to handle:** ask him what $h$ is *before* he substitutes. Reaching for 18.6 directly is the trap this
  question sets, and it is the single most likely way to lose all three marks.
- **Severity:** omission (undefined symbol). Recoverable, but only from the physics.

### P18 · MEC 3104 CAT 2 (9 Oct 2024), Q2(c)(ii) — "Show that λ = 64/Re" with no laminar condition
- **Paper:** "Show that: $\lambda = \frac{64}{Re}$." *(4 marks)*
- **Issue:** $\lambda = 64/Re$ is the **laminar** friction factor. It drops out of equating the
  Hagen–Poiseuille law the question itself supplies ($\Delta p = 32\mu l v/d^2$) to Darcy–Weisbach — and
  Hagen–Poiseuille holds for laminar flow only. Neither the question nor the stem states the restriction.
- **Note on the part that follows:** Q2(c)(iii) then hands over λ = 0.016 for a flow that is firmly
  **turbulent**. Within one question λ is derived from a laminar-only result and then used at a turbulent
  Reynolds number. The two parts stay consistent only because (iii) supplies λ instead of asking for it —
  which is also why the printed 0.016 is a reasonable wrought-iron value and not itself an erratum.
- **How to handle:** make "for laminar flow" the first line of his derivation. Markers routinely give a mark
  for stating the condition, and it is the one line that shows he knows why the result is not general.
- **Severity:** omission (missing condition).

### P19 · MEC 3104 CAT 2 (9 Oct 2024), Q2(c) — the loss head changes symbol mid-sentence
- **Paper:** "The loss head, **hs** is given by: hs = λ(l/d)(v²/2g), Δp = 32μlv/d² and that **h** = (p1−p2)/ρg".
- **Issue:** the head is $h_s$ in the first expression and $h$ in the third; "hs" is set with an inline s
  rather than a subscript, and $p1$, $p2$ are set upright while ρ and μ are italic.
- **Correct form:** one symbol throughout — $h_f$ is the usual name for the friction head loss, and
  $h_f = (p_1-p_2)/\rho g$ is the same quantity as $h_s$, not a different one.
- **Severity:** notation (cosmetic). No effect on the physics, but it makes the three-equation chain in
  (c)(ii) harder to follow than it needs to be.

### P20 · MEC 3104 CAT 2 (9 Oct 2024), Q3(a) — Manning coefficient printed as 1.4228
- **Paper:** "$V = \frac{1.4228}{n}\,m^{2/3}\,i^{1/2}$".
- **Issue:** the US-customary form of Manning's equation is $V = \frac{1.486}{n}R^{2/3}S^{1/2}$, the constant
  being $3.2808^{1/3} = 1.4859$ — the conversion of the SI constant (1.0) into ft^(1/3)/s. **1.4228 is not a
  recognised value for it**, and is about 4.3 % low. The paper's own units confirm the imperial form is meant:
  the conduit in (a)(ii) is 7 ft.
- **Not an error:** the symbols $m$ (hydraulic mean depth, $m = A/P$) and $i$ (bed slope) are the standard
  **British-textbook** names for what US texts call $R$ and $S$. Part (a)(i) is asking exactly for that —
  $m = A/P$ and why it, rather than the depth, is the length scale that governs the flow.
- **How to handle:** work it with the printed 1.4228 for the marks, then show him the same calculation with
  1.486 so he sees the ≈4 % gap. Worth asking the lecturer where 1.4228 came from.
- **Severity:** value (unverified constant). Affects the numerical answer by ≈4 %.

### P21 · MEC 3104 CAT 2 (9 Oct 2024), Q3(b) — "still air (ρ = 1200 kg/m³)" ★ most serious on this paper
- **Paper:** "Calculate the drag force on the plate if it is moving through **still air (ρ = 1200 kg/m³)**."
- **Issue:** air at room conditions is **≈1.2 kg/m³**. 1200 kg/m³ is a liquid — denser than water. The printed
  figure is **1000× too large**, and since $D_f \propto \rho$ the drag force computed from it is 1000× too
  large as well.
- **Correct value:** $\rho_{air} \approx 1.2\ \text{kg/m}^3$ (1.225 kg/m³ at 15 °C and 101.325 kPa).
- **How to handle:** work it **both** ways in a mock — once with 1200 for the marks, once with 1.2 so he sees
  what a real 0.1 m × 0.1 m plate at 5 m/s actually feels. Tell him which is which; the examiner's mark scheme
  will almost certainly want the printed number.
- **Severity:** value (wrong by 10³). This is the defect most likely to teach him something false.

### P22 · MEC 3104 CAT 2 (9 Oct 2024), foot of the paper — units of g
- **Paper:** "Take g = **9.8 m/s** or g = 32.2 ft/s²".
- **Issue:** acceleration is m/s², not m/s. The imperial value printed alongside carries its exponent
  correctly, so this is a dropped superscript rather than a misunderstanding.
- **Correct form:** $g = 9.8\ \text{m/s}^2 = 32.2\ \text{ft/s}^2$.
- **Severity:** notation (unit). He pencilled the missing "2" onto his own copy.
- **Related:** the 2024 CAT 1 carries the same defect in its Note block — see **P12**. Two papers, same slip.

### P23 · MEC 3104 CAT 2 (7 Oct 2025), head of the paper — units of g, both of them
- **Paper:** "Take g = **9.8 m/s** or g = **32.2 ft/s**".
- **Issue:** acceleration is m/s² and ft/s². The 2024 CAT 2 dropped the exponent from the metric value only
  (**P22**) and kept it on the imperial one; this paper drops it from **both**.
- **Correct form:** $g = 9.8\ \text{m/s}^2 = 32.2\ \text{ft/s}^2$.
- **Confirmation from the paper itself:** Q2(1)(a)(ii) reprints "Take g = 32.2 ft/s²" **with** its exponent.
  So the head of the paper is a typesetting slip, not a different convention the paper is following.
- **Severity:** notation (unit).
- **Related:** the same slip on the 2024 CAT 1 Note block (**P12**) and the 2024 CAT 2 (**P22**). Three papers,
  four instances. Tell him plainly that this examiner drops that exponent, so he never copies it into a script.

### P24 · MEC 3104 CAT 2 (7 Oct 2025), Q1(3)(b)(iii) — "Take f = 0.00026 m" ★ most serious on this paper
- **Paper:** "Determine the headloss in the pipe. **Take f = 0.00026 m**" — for water at 20 °C in a **new cast
  iron** pipe, 400 m long, 150 mm bore, at 4.2 m/s, ν = 1.02 × 10⁻⁶ m²/s, with the head loss defined two lines
  earlier as $h_f = f(L/d)(v^2/2g)$.
- **Issue:** the $f$ in Darcy–Weisbach is **dimensionless**. A friction factor cannot be quoted in metres. The
  number quoted, 0.00026 m = 0.26 mm, is the standard absolute **roughness** ε of new cast iron — a wall
  dimension, not a friction factor. The paper has handed over the wrong quantity under the right symbol.
- **Checked here (2026-09-03, Python):** $Re = 4.2 \times 0.150 / 1.02\times10^{-6} = 6.18\times10^{5}$, firmly
  turbulent, so $\lambda = 64/Re$ does not apply. Reading 0.00026 m as ε gives ε/d = 0.00173, and Colebrook at
  that relative roughness and that Re returns **λ ≈ 0.0229**. Head loss: **0.62 m** using the printed value as
  $f$, **54.9 m** using the Colebrook value — the printed number understates the loss by a factor of **88**.
- **Correct form:** either "take ε = 0.26 mm and read λ off the Moody chart", or supply a dimensionless λ of
  about 0.023 directly. As printed it is neither.
- **How to handle:** work it **both** ways in a mock. Substituting 0.00026 straight in is almost certainly what
  the mark scheme wants, and it takes one line; then show him the 54.9 m and ask which of the two a 400 m cast
  iron main actually loses. This is the defect on this paper most likely to teach him something false — a
  student who accepts it learns that a 400 m main at 4.2 m/s costs him 60 cm of head.
- **Severity:** value (wrong quantity, wrong by ~10²) — and notation, since it carries a unit it cannot have.

### P25 · MEC 3104 CAT 2 (7 Oct 2025), Q1(3) — the Darcy coefficient is printed as *f*, which this KB defines as λ/4
- **Paper:** "The headloss in a pipe is given by the expression: $hf = (f)(L/d)(v^2/2g)$".
- **Issue:** the equation is right; the symbol collides. The deck, all eleven topic files and the 2024 CAT 2
  write this coefficient as **λ**, and `_nomenclature.md` explicitly reserves **f** for the **Fanning**
  coefficient, $f = \lambda/4$. A student who reads the paper's $f$ against the KB's $f$ is out by a factor
  of **4**.
- **Correct form:** read the paper's $f$ as the KB's **λ**. The Darcy form $h = \lambda(l/d)(v^2/2g)$ and the
  Fanning form $h = 4f(l/d)(v^2/2g)$ are the same equation; only one of them may be called $f$.
- **How to handle:** say this out loud the first time he opens the paper, and check which convention any
  supplied friction factor belongs to before he substitutes. It is also worth noting that the end-of-semester
  exam three weeks later uses **f** as well, in its useful-information block — so on 2025 papers, f means λ.
- **Severity:** notation (symbol clash between paper and knowledge base).
- **Related:** **P19**, where the 2024 CAT 2 changed the same head loss from $h_s$ to $h$ inside one sentence.

### P26 · MEC 3104 CAT 2 (7 Oct 2025), Q2 — an orphaned item letter, and two numbering levels used as one
- **Paper:** Question Two runs "**1.** The following expressions ... **a.** Water is flowing at 150 ft³/s ...
  **i.** ... **ii.** ..." and then "**2.** A rectangular channel ...", "**3.**", "**4.**", "**5.**".
- **Issue:** two things. The "a." under item 1 has **no matching "b."** — it is a single lettered sub-item.
  And items 2 to 5 are set at the same level as item 1, so the reader has to decide whether they hang off the
  three expressions quoted under 1 or stand alone. (They stand alone: 3, 4 and 5 have nothing to do with
  critical depth.) The same paper's Question One numbers its parts 1., 2., 3. and then a., b., i., ii., iii.,
  which is consistent; Question Two is not.
- **How to handle:** cite parts of this question as Q2(1)(a)(i), Q2(2), Q2(3) … as this KB does, and say which
  scheme you are using. When setting it as a mock, mark items 2–5 independently of item 1.
- **Severity:** structural (cataloguing). No effect on the physics.

### P27 · MEC 3104 CAT 2 (7 Oct 2025), Q2(3) — a depth compared with a "flow"
- **Paper:** "In a subcritical flow, the height of water at a channel is deeper (greater) than the **critical
  flow**." (true/false, 2 marks)
- **Issue:** a height cannot be greater than a *flow*. The comparison the statement is reaching for is with the
  **critical depth** $h_c$ — that is the definition of subcritical (tranquil) flow at
  `10-open-channel-flow.md` §10.7: deeper than $h_c$ ⇒ $v < \sqrt{gh}$ ⇒ $Fr < 1$.
- **Correct form:** "… is greater than the critical **depth**."
- **How to handle:** the intent is unambiguous, so mark it as set — but make him say the corrected sentence
  back, because "critical depth", "critical flow" and "critical velocity" are three different things and this
  question blurs two of them in nine words.
- **Severity:** notation (wording). Also a small ambiguity: "the height of water **at** a channel" should be
  "in".

### P28 · MEC 3104 CAT 2 (7 Oct 2025), Q3(2)(ii) — the density of water is never supplied
- **Paper:** "Determine the drag force of one side of a plate, which is 2.0 m wide and 10.0 m long and is being
  towed lengthwise through **still water at 20 °C** and at a velocity of 5.0 m/s. Take C_D = 0.0023." The
  formula supplied one line above is $D_f = C_D\rho(v^2/2)A$.
- **Issue:** ρ appears in the formula and nowhere else on the paper. The constants line at the head of the
  paper offers only g. The question cannot be answered from the data given.
- **Correct form:** water at 20 °C is **998 kg/m³** — the value this examiner supplied on the 2024 CAT 1 and
  again on the 2025 end-of-semester exam.
- **How to handle:** have him write "taking ρ = 998 kg/m³ for water at 20 °C" as a stated assumption before he
  substitutes. Markers give the mark for the assumption; leaving the number to appear from nowhere loses it.
- **Not an error:** C_D = 0.0023 **is** plausible. Checked here 2026-09-03: $Re_L = 5\times10/1.004\times10^{-6}
  = 5\times10^{7}$, and the turbulent flat-plate correlation $0.074/Re^{1/5}$ gives 0.0021. The 2024 CAT 2's
  drag question misprinted its density by 10³ (**P21**); this one simply omits it.
- **Severity:** omission (question not answerable from the data given).

### P29 · MEC 3104 CAT 2 (7 Oct 2025), Q1 and Q2 — spelling and notation, collected
- **Paper:** "Reynold's number" (Q1(3)(b)(i)) for **Reynolds**; "$E_{min} = A_c/2b + y_c$" (Q2(1)) set without
  brackets, where $A_c/(2b)$ is meant, and read strictly left to right the printed form means $(A_c/2)\cdot b$;
  "the height of water **at** a channel" (Q2(3)).
- **Issue:** cosmetic. None of it changes an answer, but the missing brackets would if a student took them
  literally — for a rectangular section $A_c/(2b) = y_c/2$, which is what makes $E_{min} = 1.5\,y_c$ come out.
- **Correct form:** Reynolds; $E_{min} = \dfrac{A_c}{2b} + y_c$.
- **Severity:** notation (cosmetic).
- **Related:** "Reynold's" also on the 2024 CAT 1 (**P13**) and the 2025 CAT 1 (**P6**), and again on the 2025
  end-of-semester exam (**P32**). Four papers out of five.

### P30 · MEC 3104 EXAM (29 Oct 2025), Q1(d)(ii) — "Take I₀ = b(L)³/12", with b and L never defined ★ most serious on this paper
- **Paper:** "A rectangular boat, 7ft high, **18 ft wide** and **32 ft long** carrying garbage has its center of
  gravity 2 ft above the water line … Obtain the metacentre for the boat *(3 marks)*. Indicate, with reason(s)
  whether the boat is stable **Take I₀ = b(L)³/12** *(2 marks)*", with $\overline{GM} = I_o/v_{sub} -
  \overline{GB}$ supplied at the head of part (d).
- **Issue:** $I_o$ is the second moment of the **waterplane** area, and which second moment you want depends on
  the axis the vessel heels about. A stability question about a barge means **rolling**, about the longitudinal
  axis, for which $I_o = L\,b^3/12$ with $b$ the beam. The paper's own words make $b$ = 18 ft (wide) and
  $L$ = 32 ft (long), so $b(L)^3/12$ is the **pitching** second moment — the other one. Neither $b$ nor $L$ is
  defined anywhere in the question, and no heel axis is stated, so the student cannot tell which is meant.
- **Checked here (2026-09-03, Python):** $v_{sub} = 18\times32\times5 = 2880$ ft³ (draft 5 ft = 7 ft height −
  2 ft freeboard, confirmed by Figure 3, which dimensions 5 ft below the water line and 2 ft above it).
  $\overline{GB} = 2 + 2.5 = 4.5$ ft. Then
  · $I = b(L)^3/12 = 49\,152$ ft⁴ ⇒ BM = 17.07 ft ⇒ **GM = 12.57 ft**
  · $I = L\,b^3/12 = 15\,552$ ft⁴ ⇒ BM = 5.40 ft ⇒ **GM = 0.90 ft**
  The two second moments differ by a factor of 3.16 and the metacentric heights by a factor of **14**.
- **Correct form:** state the axis, then $I_o = \dfrac{L\,b^3}{12}$ with $b$ the beam (18 ft) and $L$ the
  length (32 ft) — i.e. the printed expression is right only if you read its $b$ as the boat's *length* and its
  $L$ as the boat's *width*, which is the opposite of the words in the question.
- **How to handle:** this is the one to slow him down on. Make him name the axis **before** he picks an $I$,
  and work it both ways so he sees that the verdict (stable) survives but the margin does not — 0.9 ft of
  metacentric height on a loaded garbage barge is a very different vessel from 12.6 ft. Worth asking the
  lecturer which was intended; the mark scheme will want the printed expression substituted literally.
- **Severity:** ambiguity (undefined symbols) with a value consequence of 14×.

### P31 · MEC 3104 EXAM (29 Oct 2025), Q1(g) — the columns headed RHS and LHS are printed the wrong way round
- **Paper:** "Match the terms on the **RHS** with ONE corresponding term on the **LHS**, as used in Fluid
  Theory. Note, if more than one match is given, the answer is marked as incorrect," *(6 marks)*. Below it, the
  column headed **RHS** (Euler, Bourdon, Couette flow, Darcy-Weissberg) is printed on the **left-hand side** of
  the page, and the column headed **LHS** (Coarseness, Weir, Pipe friction, Uniform velocity, Turbulence,
  Pressure measurement) on the **right-hand side**.
- **Issue:** the labels are swapped relative to the page. Every other matching question in this folder — 2024
  CAT 1 Q1(c), 2024 CAT 2 Q1(a), 2025 CAT 1 Q4, 2025 CAT 2 Q3(1) — puts the names on the left and the fields on
  the right and labels them accordingly. Anyone answering by position rather than by heading will still be
  right; anyone following the headings literally writes their answer against the wrong column.
- **Secondary:** the question gives four names against six fields but never says that two are distractors, and
  6 marks over 4 pairs is 1.5 marks a pair. Do not conclude from the odd arithmetic that two names have been
  lost off the page — the 2024 CAT 2 did the same thing with 9 marks over 6 pairs.
- **How to handle:** tell him to answer by writing the pairs out in full ("Bourdon — pressure measurement")
  rather than by column position or by drawing lines. That is immune to the swap.
- **Severity:** structural (labels reversed).

### P32 · MEC 3104 EXAM (29 Oct 2025), throughout — names, spelling and notation, collected
- **Paper:** "**Darcy-Weissberg**" (Q1(g)) for **Darcy–Weisbach**; "Reynold's number" (Q5(d)(i)) for
  **Reynolds**; "(1 **marks**)" twice (Q3(a)(ii), Q5(d)(ii)); "a **head flow** of 0.8 m" (Q4(c)) for a *head*;
  "the circulation of a fluid **turning** around a cylinder … **is turning** counterclockwise" (Q1(f)), which
  carries two main verbs and then calls the cylinder a "**column**" in the next sentence; and Figure 6 labels
  the moving surface **U** where the question text calls its speed **v** (Q3(b)).
- **Issue:** cosmetic, with one exception worth naming: **"Darcy-Weissberg" is not a searchable form of the
  name.** A student revising from it finds nothing. It is Julius **Weisbach**.
- **Correct form:** Darcy–Weisbach; Reynolds; (1 mark); "a head of 0.8 m"; and read Figure 6's $U$ as the
  question's $v$.
- **Severity:** notation (cosmetic), except the surname, which is worth correcting out loud.
- **Related:** Reynolds misspelt on **P6** (2025 CAT 1), **P13** (2024 CAT 1) and **P29** (2025 CAT 2).

### P33 · MEC 3104 EXAM (29 Oct 2025), Q2(c) — the jet-pump pressure change is printed with the subtraction reversed
- **Paper:** "The change in pressure is given by:
  $p_1 - p_2 = \rho\frac{d^2}{D^2}\frac{D^2-d^2}{D^2}(v_0-v_1)^2$", under Figure 5.
- **Issue:** the right-hand side is a square multiplied by positive quantities, so it can never be negative. But
  a jet pump **raises** the pressure between Section 1 and Section 2 — that is what it is for — so $p_2 > p_1$
  and the printed left-hand side is negative. The **same expression, with the same figure**, is printed on the
  2024 CAT 1 (Q4(a)) as "$P2 - p1 = \rho\ldots$". One of the two papers has the subtraction the wrong way
  round, and it is this one.
- **Correct form:** $p_2 - p_1 = \rho\dfrac{d^2}{D^2}\dfrac{D^2-d^2}{D^2}(v_0-v_1)^2$, matching
  `07-momentum.md` §7.6 (·slides 280–282).
- **Checked here (2026-09-03):** with ρ = 998 kg/m³, d = 6 cm, D = 20 cm, v₀ = 40 m/s and 3 m/s for the
  annulus velocity, the right-hand side is **+111.9 kPa**. As a value of $p_1 - p_2$ that would mean the pump
  drops the pressure by 112 kPa.
- **How to handle:** have him quote the magnitude and then say in words which section is at the higher
  pressure. That earns the mark either way and shows he knows what a jet pump does. Set the two papers side by
  side — the same formula printed two ways, three semesters apart, is a good lesson in not trusting a printed
  sign.
- **Severity:** value (sign).

### P34 · MEC 3104 EXAM (29 Oct 2025), Q2(c)(ii) — an exit velocity supplied for a formula that takes v₁
- **Paper:** "Determine the change in pressure in a jet pump in which water (density 998 kg/m³) is flowing at
  40 m/s through a 6-cm pipe and **exits the pump through a 20-cm pipe at 3 m/s**."
- **Issue:** the supplied expression contains $(v_0 - v_1)^2$, where — per Figure 5 and `07-momentum` §7.6 —
  $v_0$ is the jet velocity at the nozzle and $v_1$ is the velocity of the **surrounding stream at Section 1**,
  in the annulus around the jet. "Exits the pump" names $v_2$, the mixed velocity at Section 2, which is a
  different quantity and does not appear in the formula at all.
- **Correct reading:** the 3 m/s has to be taken as $v_1$ for the question to be a 4-mark substitution. Read as
  $v_2$, the printed formula cannot be used until $v_1$ is recovered from continuity, which is a longer
  question than the marks allow.
- **How to handle:** ask him which velocity the formula wants **before** he substitutes — the same discipline
  P17 asks for on the 2024 Pitot question. Then have him say what he assumed. The 2024 CAT 1 version of this
  question described the same quantity as "a larger pipe **whose flow rate is** 6.3 m/s" (**P9**), which was
  wrong in a different way. Neither paper has yet named $v_1$ correctly.
- **Severity:** ambiguity (a symbol identified by the wrong physical description).

### P35 · MEC 3104 EXAM (29 Oct 2025), Q2(c)(i) — angular momentum inside a linear-momentum question
- **Paper:** the stem reads "One of the applications of **conservation of momentum** is the jet pump …", the
  supplied formula is the jet-pump pressure rise, and part (i) then asks: "State the law of conservation of
  **angular** momentum *(2 marks)*".
- **Issue:** the jet pump is a **linear** momentum problem — a control-volume force balance along the pipe
  axis. Angular momentum plays no part in it, in the formula, or in Figure 5. As printed, part (i) either
  belongs to a different question or should read "linear momentum".
- **Correct form:** unresolved. It may be a deliberate free-standing recall item (the KB does teach angular
  momentum, `07-momentum` §7.8, ·slides 286–288), or it may be a slip for "linear". The paper gives no way to
  tell.
- **How to handle:** answer it as printed — state conservation of angular momentum — and do **not** try to
  connect it to the jet pump; there is no connection to find. Worth asking the lecturer which was intended.
- **Severity:** ambiguity (a sub-part that does not follow from its own stem).

### P36 · MEC 3104 EXAM (29 Oct 2025), Q3(a) — the velocity field does not satisfy continuity
- **Paper:** "The flow velocity of a certain system is given by the following equation for a two dimensional
  flow. $v = ky(x+y);\ u = -kx(x+y)$" — then: obtain the streamline equation (3 marks), and state whether the
  flow is rotational or irrotational (1 mark).
- **Checked here (2026-09-03, sympy):** $\dfrac{\partial u}{\partial x} + \dfrac{\partial v}{\partial y} =
  -k(2x+y) + k(x+2y) = k(y-x)$, which vanishes only on the line $y = x$.
- **Issue:** an incompressible two-dimensional flow must satisfy $\partial u/\partial x + \partial v/\partial y
  = 0$ everywhere (`08-viscous-flow` §8.1, ·slides 304–307). This field does not, so it is not a physically
  admissible incompressible flow — the paper calls it "the flow velocity of a certain system" when no such
  system exists.
- **Does it break the question?** No. Both parts are still answerable exactly as set: the streamline equation
  follows from $dy/dx = v/u$ whatever the divergence is, and part (ii) is a direct evaluation of the printed
  operator. Nothing is unanswerable; the physics behind it is simply not real.
- **How to handle:** let him answer it as set for the marks, then ask him to test continuity on it as a
  five-line extra. It is the cheapest way to make the continuity equation stick, and it teaches him that a
  velocity field handed to him in an exam is not automatically a flow.
- **Severity:** value (an unphysical data set), not omission — the question still works.

### P37 · MEC 3104 EXAM (29 Oct 2025), Q1(d) and Q3(b) — sub-part labels that do not pair up
- **Paper:** two places. **Q1(d)** prints "**ii)** Obtain the metacentre for the boat *(3 marks)*" and then, on
  the next line and with no label of its own, "Indicate, with reason(s) whether the boat is stable Take I₀ =
  b(L)³/12 *(2 marks)*" — two separately marked tasks under one roman numeral. **Q3(b)** prints an unlettered
  descriptive part ("briefly describe the theory of lubrication …", 3 marks) and then a part labelled "**ii)**"
  with no "i)" anywhere above it.
- **Issue:** cataloguing. A reader tallying parts by label undercounts Q1(d) and cannot place Q3(b)(ii).
- **How to handle:** cite them as this KB does — Q1(d)(ii) for the metacentre and Q1(d)(ii) *continued* for the
  stability mark; Q3(b) for the description and Q3(b)(ii) for the viscosity calculation. Say which scheme you
  are using whenever you quote a part number back to him.
- **Severity:** structural (cataloguing). No effect on the physics or on the marks total, which still reaches
  30 and 15 respectively.

### P38 · MEC 3104 EXAM (29 Oct 2025), Q3(b)(ii) — γ = 53.7 with no units
- **Paper:** "Take: $(p_1-p_2)/\gamma = 32\mu Lv/\gamma d^2$; **γ = 53.7**; 1 ft = 12 in."
- **Issue:** a bare number. γ is a specific weight, and in the imperial system this question is set in it is
  **lb/ft³**. Without the unit the student cannot tell whether to convert the 30.0 psi to lb/ft² before
  dividing (he must: 30.0 psi × 144 = 4320 lb/ft²).
- **Checked here (2026-09-03):** the oil's stated specific gravity is 0.860, so
  $\gamma = 0.860 \times 62.4 = 53.66\ \text{lb/ft}^3$. The printed **value is right; only its unit is
  missing** — and, incidentally, it is redundant, since the SG already gives it.
- **How to handle:** write "γ = 53.7 lb/ft³" onto his copy. Then note that γ cancels from both sides of the
  printed relation anyway, so it is needed only to convert the pressure drop into a head.
- **Not an error — the data is sound:** checked here, $v = Q/A = 0.0436/0.0218 = 2.00$ ft/s, and the resulting
  Reynolds number is **≈ 296**, so the question's own "assume laminar flow" is consistent with its own numbers
  and the viscosity that falls out is an ordinary lubricating-oil value.
- **Severity:** notation (missing unit).
- **Related:** **P1**, where the 2025 CAT 1 printed a specific weight with an impossible unit rather than none.

### P39 · MEC 3104 EXAM (29 Oct 2025), Q3(c) — a head loss with no unit, and no length for the capillary
- **Paper:** "Take the loss of head (h_f) to be equal to **0.32**" and "Take $h_f = 128\mu LQ/\pi\rho gd^4$",
  with Figure 7 dimensioning 0.1 m, 0.22 m and 0.08 m and marking the tube $d_1 = 1$ mm.
- **Issue:** two omissions. (i) 0.32 carries no unit. (ii) The supplied formula needs **L**, the length of the
  capillary tube, and the figure never dimensions it — it dimensions the two water surfaces and the tank floors
  instead.
- **Checked here (2026-09-03):** 0.1 m + 0.22 m = **0.32 m** — the figure's own surface-to-surface elevation
  difference is exactly the printed h_f, which settles the unit as metres. The tube length is **not** settled:
  reading it from tank A's floor to the tube's open lower end gives 0.22 + 0.08 = 0.30 m, but reading it to
  tank B's free surface gives 0.22 m, and the two differ by 36 % in the answer.
- **How to handle:** give him the unit (metres — and show him where it comes from, because the figure proving
  it is a nice piece of reasoning). Then make him **state** which length he is taking for L before he
  substitutes. Do not resolve L for him silently; the drawing genuinely does not say.
- **Severity:** omission (missing unit + a quantity the printed formula requires and the figure does not give).

### P40 · MEC 3104 EXAM (29 Oct 2025), Q4(c) — "Take the value of C to be 1.69"
- **Paper:** part (b) asks him to show that $Q = \frac{2}{3}C\,b\sqrt{2g}\,H^{3/2}$, defining **C** as "the
  coefficient of discharge of a weir". Part (c) then says: "A sharp crested rectangular weir 0.8 m wide carries
  water at a head flow of 0.8 m. Calculate the volumetric flow rate. **Take the value of C to be 1.69**".
- **Issue:** 1.69 is the **dimensional** SI constant of the engineering weir formula $Q = 1.69\,b\,H^{3/2}$
  (units m^½/s), in which the $\frac{2}{3}\sqrt{2g}$ and the discharge coefficient are **already multiplied
  in**. A dimensionless coefficient of discharge for a sharp-crested weir is about **0.62**. Substituting 1.69
  into the part-(b) formula applies $\frac{2}{3}\sqrt{2g}$ twice.
- **Checked here (2026-09-03):** the part-(b) formula with C = 1.69 gives **2.857 m³/s**; $Q = 1.69bH^{3/2}$
  gives **0.967 m³/s**. The ratio is **2.953**, which is exactly $\frac{2}{3}\sqrt{2g}$ at g = 9.81 — the group
  that has been counted twice.
- **Correct form:** either $Q = \frac{2}{3}\,C_d\,b\sqrt{2g}\,H^{3/2}$ with $C_d \approx 0.62$, or
  $Q = 1.69\,b\,H^{3/2}$ — not the two combined.
- **How to handle:** work it both ways and say which is which. The mark scheme will want 1.69 substituted
  straight into part (b)'s formula, exactly as the 2024 CAT 1 wanted 3.2 substituted into its integral.
- **Severity:** value (a dimensional constant presented as a dimensionless coefficient).
- **Related:** **P11** — the identical defect on the 2024 CAT 1 with the imperial constant 3.2. **Two papers,
  the same weir, the same mistake in two unit systems.** This is now a pattern, not an accident: whenever this
  examiner writes "coefficient of discharge", check its dimensions before substituting.

### P41 · MEC 3104 EXAM (29 Oct 2025), Question Five heading — no mark allocation printed
- **Paper:** the heading reads "**Question Five**" and nothing else. Question One is headed "(30 marks)",
  Questions Two, Three and Four "(15 marks)" each.
- **Issue:** the reader has no printed figure to check Question Five's parts against. Its parts do sum to 15
  (2+2+2+3+2+1+3), which matches the other optional questions, but that is an inference, not something the
  paper states. **No overall total is printed on the paper either**, so this is the one question in the folder
  whose marks cannot be reconciled against anything printed — hence `marks_reconcile: false` on
  `MEC3104-EXAM-2025-10-29.md`, even though Questions One to Four reconcile exactly.
- **How to handle:** mark Question Five out of 15 in a mock and say that you are doing so. If he ever sits a
  paper where a question heading has no total, the safest move is to answer every part and flag it to the
  invigilator.
- **Severity:** omission (paper defect).

### P42 · MEC 3104 EXAM (29 Oct 2025), page 3 — a stray section heading above item (h)
- **Paper:** page 3 opens with a centred line, "**One dimensional fluid flows**", set above item **h.** of
  Question One and belonging to no question. It is not numbered, carries no marks, and nothing on the paper
  refers to it.
- **Issue:** it reads like a section title left in from whatever document the questions were assembled from.
  A candidate could reasonably take it as an instruction — "assume one-dimensional flow" — for everything that
  follows, which would be a different paper. Item (h) is the Pitot question and the two questions after it are
  not one-dimensional in any useful sense.
- **How to handle:** ignore it, and say so out loud the first time he reads the page, so that he does not
  spend exam minutes trying to work out what it governs.
- **Severity:** structural (stray text).

<!-- Later papers append their own P-numbered entries above this line. -->

---

# § Second-pass audit — 3 August 2026

Independent re-verification of all 11 topic files against the source deck. All 594 slides were re-extracted
from the .pptx XML **including equation objects** — the first pass read text boxes only, which is why four of
its own flags could not be re-found until this pass. Scope: ~200 `·slide N` citations sampled, every worked
example re-computed, every named coefficient checked against standard values.

**Headline results**
- The **18 previously logged slide flags are all re-confirmed verbatim** in the deck — including s271, s493,
  s531 and s560, whose text lives inside equation objects. Nothing in the first pass was invented.
- **Provenance is the KB's strongest feature:** ~200 citations sampled, only **2 wrong** (both fixed).
- Every worked example re-computed in sections 05, 08, 09, 10 and 11 **agrees**. `_formula-sheet.md` is clean:
  no equation mis-transcribed, none dimensionally inconsistent.
- The deck contains **~30 further errors the first pass missed**, listed below as `S`-entries. They are NOT yet
  marked `⚠ VERIFY` in the topic files — treat this list as the authority until they are.
- **Four errors were in the KB itself, not the deck.** All four fixed, tagged `⚠ KB-FIX 2026-08-03` in place.

## KB corrections applied (errors the KB introduced)

| # | File | Was | Now |
|---|---|---|---|
| K1 | `10-open-channel-flow.md` §10.8 | "a jump/drawdown occurs at the break" | a **drawdown**. A hydraulic jump is supercritical→subcritical; a mild→steep slope break is the opposite transition. The KB had it backwards. |
| K2 | `04-fluid-statics.md` §relative equilibrium | "β = resultant accel/mass" | β = resultant **force** per unit mass (slide 159: β = F/m) — numerically the acceleration. "accel/mass" is meaningless. |
| K3 | `11-drag-and-lift.md` §11.4 | Strouhal attributed to "Taylor/Roshko" | slide 548 names **G. I. Taylor only**. Roshko was the KB's addition. |
| K4 | `_formula-sheet.md` wing lift | `L = C_L l ½ρU²` | same, now marked **per unit span (N/m)** — without it the equation reads as a total force but yields N/m. |

Mis-citations fixed: Manning worked solution is on **slide 495**, not 494 (also corrected in the Section 10
entry above); Kutta–Joukowski boxed equation is on **slide 566**, with the spinning-ball prose on 567–568.
Frontmatter `verification_flags: 0` corrected to `1` in `08-viscous-flow.md` and `10-open-channel-flow.md`.

## S-entries — slide errors found in the second pass

### Section 03 — Fluid Properties
- **·S1 slide 46 — arithmetic.** "SG(Hg) = 13500/1000 = 13.6". 13500/1000 = **13.5**. The answer 13.6 is right;
  the numerator is the typo (slide 45 gives ρ_Hg = 13,580). A student copying this learns 13500/1000 = 13.6.

### Section 04 — Fluid Statics
- **·S2 slide 116 — inclined manometer, statement backwards.** "H = L sin α. The smaller the α, the larger the
  H." False as written: with H = L sinα, a smaller α gives a **smaller** H for a given L. The real point — why
  inclined manometers are sensitive — is that for a **given H**, a smaller α gives a **longer, more readable
  travel L**. Worth teaching explicitly; it is the whole purpose of the instrument.
- **·S3 slides 99, 100 — missing ρ₀/P₀.** Brackets printed `[1 − ((n−1)/n)·P₀·g·z]`; should be
  `[1 − ((n−1)/n)(ρ₀g/P₀)z]`. "P₀gz" is dimensionally garbage; the pressure ratio one line above has it right.
- **·S4 slide 104 — lapse rate.** "dT/dz = 0.0065 K/100" contradicts slide 103's correct 0.0065 K/m. The
  slide's own n = 1.235 requires K/m.
- **·S5 slide 92 — p₀ dropped.** "P = p₀ + ρg(z₀−z) = ρgh"; the last expression should be p₀ + ρgh.
- **·S6 slide 107 — missing minus sign.** Isothermal "P ≈ P₀e^{gZ/RT}"; the slide's own arithmetic uses
  exp(−0.5929), so it must be e^{−gz/RT}.
- **·S7 slide 134 — sinθ dropped.** "Force on a minute area dA = ρg·y_G·dA" must be ρg·y·sinθ·dA (strip depth,
  not centroid). The omission also makes the following line valid only for a vertical surface.
- **·S8 slide 140 — invalid substitution.** "h_G is substituted for y_G" is legitimate only when θ = 90°, yet
  slides 130–140 set up an inclined bank.
- **·S9 slide 163 — centripetal vs centrifugal.** In vessel-fixed rotating axes the body force producing the
  paraboloid is the outward **centrifugal** inertial force. A centripetal force points inward and would tilt
  the free surface the other way.

### Section 06 — Energy & Bernoulli
- **·S10 slide 256 — Torricelli derivation loses the elevation term. THE MOST SUBSTANTIVE FINDING.** The slide
  sets p_A = p_B = atmospheric, writes `p_A/ρg + 0 = p_B/ρg + v_B²/2g`, then `v_B²/2g = (p_A − p_B)/ρg` — which
  by its own algebra gives **v_B = 0** — and yet concludes v_B = √(2gH). The term z_A = H was dropped from the
  left-hand side. The correct statement is v_B²/2g = (p_A − p_B)/ρg **+ H**, which with p_A = p_B gives
  v_B = √(2gH). Do not learn this derivation from the slide as printed.
- **·S11 slide 229 — head definitions.** "p/ρ = pressure head" must be **p/ρg** (the boxed equation on the same
  slide has it right). And "velocity head (K.E./unit **mass**)" — a head is in metres, i.e. energy per unit
  **weight** (J/N); per unit mass gives J/kg = m²/s².
- **·S12 slide 231 — symbol reuse and a broken line.** "ρV²/2 + P + ρgz = H" reuses H (defined in metres on
  slide 229) for a quantity in pascals; and "ρV²/2 + Ps = ρV²/2 = dynamic pressure" should end = P_t.
- **·S13 slides 243–244 — Venturi radical misplaced.** Printed "Q = C[A₂/{1 − √(A₂/A₁)²}·√2gH": the square root
  sits on the area ratio instead of on the whole (1 − (A₂/A₁)²), and the outer bracket never closes. *(Relevant:
  the 2024 CAT Q3b prints the same formula in its correct form — compare them.)*
- **·S14 slide 259 — symbol clash.** A used for both the orifice area and the tank cross-section in one line
  ("−dH·A = −dH·πr²"), after slide 258 used a for the hole.

### Section 07 — Momentum
- **·S15 slide 279 — dimensionally impossible.** "ρQ(v₂²−v₁²) = (p₁−p₂)A₂": LHS is watts, RHS is newtons.
  Correct: **ρQ(v₂−v₁) = (p₁−p₂)A₂**. The boxed Borda–Carnot result that follows is right; only this
  intermediate is wrong.
- **·S16 slide 282 — sign statement contradicts the slide's own result. Read this before the 2024 CAT Q4a.**
  The slide's algebra gives p₂ − p₁ = ρ(d²/D²)((D²−d²)/D²)(v₀−v₁)² > 0, i.e. **p₂ > p₁** — which is precisely
  what makes a jet pump work. The prose then says "p₁ − p₂ is always positive", which is backwards.
- **·S17 slide 271 (second pair of equations) — signs and lost velocities.** Rearranging the slide's own first
  pair gives +Fx and +Fy, not −Fx/−Fy (the pressure terms' signs were not flipped when moved across), and the
  Fx line has lost v₁ and v₂ entirely. *(This is a second, separate defect on the slide already flagged for
  √(Fx²−Fy²).)*
- **·S18 slide 238 — rounding, inherited by section 07.** 800 L/min truncated to 0.013 m³/s instead of 0.01333,
  making every velocity ≈2.5 % low. Correct: v₁ = 6.79, v₂ = 4.72, v₃ = 1.70 m/s (slide prints 6.62 / 4.59).

### Section 08 — Viscous Flow
- **·S19 slides 323, 324 — spurious ρ.** The non-dimensional vorticity-transport equation is printed with a
  leading ρ; the RHS is dimensionless, so the ρ must not be there.
- **·S20 slide 370 — spurious μ.** Turbulent BL written "… = −∂p/∂x + μ ∂τ/∂y". τ already contains μ, so
  μ ∂τ/∂y has units Pa²·s/m. Correct: ∂τ/∂y.
- **·S21 slide 382 — unit.** dv/dy given as "2020 **m³/s**"; a velocity gradient is s⁻¹. *(Separate from the
  sin/cos flag already logged on this slide.)*
- **·S22 slide 320 — wrong velocity component.** The y-momentum equation's LHS is written with u where v is
  required (slide 310 has the same slip). The deck self-corrects on slide 321.

### Section 09 — Flow in Pipes
- **·S23 slides 405, 408 — smooth/rough criteria inverted.** Printed "ε ≤ 5 v*/ν" and "ε ≥ 70 v*/ν". v*/ν has
  units of 1/m and cannot bound a length. Correct: **ε ≤ 5ν/v\*** (hydraulically smooth) and **ε ≥ 70ν/v\***
  (fully rough) — equivalently ε⁺ = εv\*/ν ≤ 5 and ≥ 70.
- **·S24 slide 409 — Nikuradse criterion inverted.** "Re > 900(ε/d)" must be **Re > 900(d/ε)**. As printed,
  ε/d = 0.01 would make every flow above Re = 9 "fully rough".
- **·S25 slide 411 — slug units labelled lb.** "μ = 3.11×10⁻² lb/ft·s" and "ρ = 2.44 lb/ft³" are **slug**-based
  values. Glycerin is 1260 kg/m³ = 2.44 slug/ft³ (78.6 lbm/ft³). Re = 392 is unaffected, but the labels are
  wrong — the same defect class already logged for slide 44.
- **·S26 slide 404 — "Assume laminar flow" with λ = 0.0230.** At 70 °C water, v = 9.7 ft/s, d = 6 in gives
  Re ≈ 1.1×10⁶ — firmly **turbulent**, and 0.023 is the correct *turbulent* cast-iron value. The stated
  assumption contradicts both the data and the coefficient used.

### Section 10 — Open-Channel Flow
- **·S27 slide 495 — arithmetic.** "m = 80.23/24.20 = 3.15 in = 0.2763 ft". 80.23/24.20 = **3.3153 in**
  (and 0.2763 ft = 3.3156 in). "3.15" is a typo for 3.32; downstream results are unaffected.
- **·S28 slide 498(c) — missing factor 2.** "s = 5.0 + [(1.2)(√2)] = 8.394 m" evaluates to 6.697. The answer
  8.394 requires **both** sloping sides: 5.0 + 2(1.2√2).
- **·S29 slide 486 — Bazin coefficient.** Printed c = 87/(1 + α/√(mi)); the standard form is **87/(1 + α/√m)**.
  The KB body already prints the standard form — previously disclosed only in a trailing footnote, now logged.

### Section 11 — Drag and Lift
- **·S30 slide 572 — moment equation dimensionally inconsistent.** Beyond the L→M label already logged: per unit
  span, lift and drag are forces per unit length, so C·l·½ρU² = N/m ✓. But **moment** per unit span is N·m/m = N,
  so it needs **l²**: M = C_M·**l²**·½ρU².
- **·S31 slides 534, 555 — density in slug/ft³ labelled lb/ft³.** Slide 534: "ρ = 1.93 lb/cft" for water at
  70 °F — water is 62.4 lb/ft³; 1.93 is its **slug**/ft³ value. Slide 555: "ρ = 0.00242 lb/cft" for air.
  Since D = C_D·ρv²A/2 needs **mass** density, taking the labels literally makes both answers wrong by
  g ≈ 32.2. The values used are right; only the labels are wrong.
  *Secondary:* 0.00242 slug/ft³ is air at ≈10 °C, not the stated 50 °C (≈0.00212) — the datum contradicts the
  problem statement.

## Known coverage gaps (content in the deck, absent from the KB)

Not errors — but a future chat should not assume the topic files are exhaustive.

| Section | Missing |
|---|---|
| 03 | **slide 43** dropped entirely (the deck's definition of a *dimension*); slide 44's angular-velocity row and two conversions |
| 08 | slide 360 (definition of a **wake**); slide 361 (ground boundary layer ≈1 m) |
| 09 | **Itaya's smooth-pipe correlation** (slide 406); **slide 442** (convergent pipe/contraction) dropped entirely; slide 432's ζ≈1 for θ=50–60° and the Coandă wall-attachment note; slide 465's needle/ball throttle-area formula. Also §9.3's worked example omits the pipe length l = 120 ft, so its h_f = 60.9 ft cannot be reproduced from the data given |
| 11 | slides 591 (saturation-pressure / air-solubility table) and 592 (hydrofoil pressure distribution) |
| `_formula-sheet.md` | Ganguillet–Kutter and Bazin (§10); moment coefficient and interference coefficient k = L/L₀ (§11) |


### Addendum (found 2026-08-03 while answering a question about Venturi tubes)
- **·S32 slide 440 — "venturi flame".** The hump-in-a-channel example calls the arrangement a "venturi
  **flame**"; it is a venturi **flume**. `09-pipe-flow.md` §(·440–441) already writes "flume" — a silent
  correction, now logged. *(Note also that 440–441 is open-channel content sitting inside the deck's pipe-flow
  block; the KB follows the deck's slide order, so it is filed under `09-pipe-flow.md` rather than `10`.)*
- **Venturi cross-reference:** the tube itself is slides **240–244** (Topic 06, `06-energy-bernoulli.md` §6.6),
  not near slide 230 — 230 is Daniel Bernoulli's biography. Erratum **S13** applies to 243–244; the 2024 CAT
  Q3b prints the same formula correctly, so the two are worth comparing side by side.

Also unverifiable from text alone (content lives in slide **images**, not text): slide 56's rheological
diagram curves (03) and slide 428's l/d ≈ 1–99 experimental range (09). Neither is disputed — flagged as
unaudited rather than wrong.


---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
