---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "GA1 — Group Discussion Exercises, Topic 1 Part 1"
source: "GA1 — 'MEC_3105_Group_Exercises_Topic1_Part1' (master brief) + 8 group submissions"
file_role: exercises
covers: "1.1 Temperature and Thermometry | 1.2 Equations of State (Ideal Gas Law and Van der Waals)"
groups: 8
solutions: "worked and verified — § Solutions. All tagged [added]; the brief supplies none."
maps_to: ["01-temperature-thermometry", "02-first-law"]
verification_flags: 1
tags: [exercises, group-activity, thermometry, temperature-conversion, ideal-gas-law, van-der-waals, compressibility-factor]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (exercises files):
  [exercise] question as set · [added] supplied here, NOT in the source ·
  → §x.y = cross-link into the topic file that covers the required theory ·
  ·GA1 G3 Part B (ii) = provenance (which group's brief, which part). -->

# GA1 — Topic 1 Part 1: Thermometry and Equations of State

**Assessed group activity.** 8 groups, 8–9 students each. ~55 min guided discussion + 5 min
presentation per group. Targets **CO1** (define key thermodynamic concepts) and **CO3** (explain EOS
relationships); WA graduate attributes **PO1, PO2, PO9, PO10**.

The brief is built in two halves. **Part A** — the guided discussion guide and the concept questions —
is **identical for every group**. **Part B** is mixed: its **Sub-Topic 1.1** gives each group a
*different* measurement scenario with *different* short-answer parts, while its **Sub-Topic 1.2 Parts
(i) and (ii)** use the **same wording for every group** with only the numbers and the assigned gas
changing. This file therefore tabulates Sub-Topic 1.1 group by group, and states 1.2's stems **once**
with a per-group data table, rather than repeating eight near-identical copies.

---

## How to use this file

> ### The questions come first, the solutions are at the end
>
> **§ Solutions** at the bottom of this file works every numerical part and gives answer points for
> the short-answer parts. It is deliberately at the end so you can attempt a question before seeing
> the answer — scroll past it, or work from the linked topic sections first.
>
> **Every solution is `[added]`.** The brief itself supplies no answers to students. These were
> **computed from scratch and independently verified**, not transcribed from anywhere.
>
> The master brief does carry a **"FACILITATOR / LECTURER NOTES (Not distributed to students)"**
> section. It is marked not for distribution and this repository is public, so **nothing from it is
> reproduced, quoted or paraphrased** — not a number, not a phrase. The solutions below are our own
> working, and they stand or fall on the method shown with them.
>
> ⚠ **One correction was needed before Part (ii) could be solved at all** — see the flag immediately
> below.

**Reading the cross-links.** `→ 01 §1.7` means *the theory you need is in
`01-temperature-thermometry.md`, section 1.7*. Everything you need for GA1 is in **01** and **02**,
with three exceptions flagged in § Gaps below.

---

## Part A — Guided discussion guide ·GA1 Part A *(common to all 8 groups)*

The session runs to a fixed six-step structure. Appoint a timekeeper and a recorder at the start.

| Step | Time | What the group does | Theory |
|---|---|---|---|
| **1** Ice-breaker | 5 min | Each member names a device that measures temperature (clinical thermometer, thermocouple in an oven, IR sensor in a phone). Identify the underlying **principle** of each and link it to the **zeroth law**. | → **01** §1.3, §1.4 |
| **2** Thermometry | 10 min | Why must **absolute** scales (Kelvin, Rankine) be used in thermodynamic property equations rather than Celsius or Fahrenheit? Each member gives one example where the wrong scale causes an engineering error. | → **01** §1.6, §1.7 |
| **3** Equations of state | 10 min | Compare the **ideal gas law** and the **Van der Waals equation** — when is each appropriate? Identify **two** conditions under which a real gas deviates significantly from ideal behaviour, linking to the compressibility factor $Z$. | → **02** §2.12 |
| **4** Numerical problem | 20 min | Solve the group's assigned Part B set. All members contribute; one records the working for presentation. | → Part B below |
| **5** Real-world link | 5 min | Where in **electrical power engineering** would accurate knowledge of gas $P$–$v$–$T$ behaviour be critical? (Brief's hint: SF₆ GIS switchgear, generator hydrogen cooling, transformer oil.) Agree on ONE example. | → **02** §2.12 |
| **6** Summary | 5 min | Elect a spokesperson; prepare a 2-minute summary covering (a) the key concept(s), (b) the numerical answer with steps, (c) the real-world EE example. | — |

---

## Part A — Common concept discussion questions ·GA1 Part A *(all groups)*

Discussion starters — the brief states that formal written answers are not required.

**[exercise] Q1 — The zeroth law as the foundation of thermometry.**
The zeroth law states that if body A is in thermal equilibrium with body C, and body B is also in
thermal equilibrium with body C, then A and B are in thermal equilibrium with each other. **Why is
this law considered the foundation of thermometry?** Give an example from electrical engineering
where this principle is implicitly relied upon.
→ **01 §1.3** — the zeroth law and the formal definition of temperature. §1.3 states explicitly that
the law is what licenses a thermometer to stand in for direct contact between the two bodies.

**[exercise] Q2 — When Kelvin is mandatory and when Celsius will do.**
A reading of $27\ ^\circ\mathrm{C}$ is used in two calculations: one with the ideal gas law
($PV = mRT$) and one with Newton's law of cooling ($q = hA\,\Delta T$). **In which is conversion to
Kelvin essential, and in which can Celsius be used directly? Why?**
→ **01 §1.7** — the ratio-vs-difference distinction: a Celsius *difference* equals a kelvin
difference, but a Celsius *value* is not proportional to a kelvin value. → also **01 §1.6** for why the
absolute scale has a true zero.

**[exercise] Q3 — Ideal gas vs Van der Waals; the critical point.**
Compare the two equations. **Under what two conditions does a real gas deviate most significantly
from ideal-gas behaviour?** Sketch (or describe) the shape of a $P$–$v$ diagram near the **critical
point** and explain what the critical point represents.
→ **02 §2.12** — including the FL s36 figure discussion, which marks the region round the critical
point as non-ideal. The Van der Waals equation itself is `[added]` there and on `_formula-sheet.md`.

**[exercise] Q4 — What $Z \gtrless 1$ physically means.**
$Z = Pv/RT$; for an ideal gas $Z = 1$. **Discuss what $Z > 1$ and $Z < 1$ physically mean for a real
gas.** In what practical situation might a substation engineer need to account for a $Z$
significantly different from 1?
→ **02 §2.12** → *Compressibility factor $Z$*.

**[exercise] Q5 — Ranking four instrument families.**
Thermocouples, RTDs, liquid-in-glass thermometers and pyrometers each exploit a different physical
property. **Rank the four by (a) temperature-range capability and (b) response speed**, with brief
justification.
→ **01 §1.4** — the six physical properties table (rows 1, 5 and 6 map to liquid-in-glass, RTD and
pyrometer respectively). ⚠ **The thermocouple is not in TT's list of six** and the thermoelectric
effect is not taught in any deck — see § Gaps.

---

## Part B — Sub-Topic 1.1: Temperature and thermometry ·GA1 Part B

Each group is given a **different electrical-engineering measurement scenario**, then asked for
conversions plus two short-answer parts. The conversion targets differ: odd-numbered scenarios ask
for **Fahrenheit**, even-numbered for **Rankine**.

→ Theory for every row: **01 §1.7** (conversions), **01 §1.4–1.5** (instruments), **01 §1.6**
(absolute zero, why the Kelvin scale exists).

| Group | Scenario as set | Reading | Convert to | Short-answer parts (b), (c) |
|---|---|---|---|---|
| **G1** | Thermocouple in a **33 kV transformer oil-cooling circuit** | $68\ ^\circ\mathrm{C}$ | K, °F | (b) explain the **Seebeck effect** as the operating principle; (c) one reason a thermocouple beats liquid-in-glass here |
| **G2** | **RTD** embedded in a **generator stator winding** | $95\ ^\circ\mathrm{C}$ | K, °R | (b) why RTDs are more accurate than thermocouples for winding monitoring; (c) name the law that lets any thermometer compare two separate bodies |
| **G3** | **Infrared pyrometer** on a **busbar**, load survey | $112\ ^\circ\mathrm{C}$ | K, °F | (b) why non-contact rather than contact measurement here; (c) one limitation of a pyrometer vs an RTD |
| **G4** | **Fibre-optic sensor** at a **transformer winding hot-spot** | $78\ ^\circ\mathrm{C}$ | K, °R | (b) one advantage of fibre-optic over thermocouple inside an HV winding; (c) express the $85\ ^\circ\mathrm{C}$ cooling-fan alarm threshold in K |
| **G5** | **Liquid-in-glass** thermometer calibrating a **substation weather station** | $38\ ^\circ\mathrm{C}$ | K, °F | (b) compare thermocouple vs RTD as replacements and recommend one for ambient measurement; (c) convert $-40\ ^\circ\mathrm{C}$ to K — *what is notable about this result?* |
| **G6** | **Pt-100 RTD** in a **power cable joint** at rated current | $55\ ^\circ\mathrm{C}$ | K, °R | (b) express the $90\ ^\circ\mathrm{C}$ insulation limit in K; (c) why cable ampacity ratings depend on **absolute** temperature, not Celsius differences alone |
| **G7** | **Thermocouple** on a **steam turbine-generator exhaust flange** | $210\ ^\circ\mathrm{C}$ | K, °F | (b) why a thermocouple beats an RTD at this temperature; (c) convert the manufacturer's $480\ ^\circ\mathrm{F}$ limit to °C and say whether the reading exceeds it |
| **G8** | **Digital pyrometer**, thermal imaging survey of **MV switchgear**, hot-spot on a cable lug | $74\ ^\circ\mathrm{C}$ | K, °R | (b) IEC allows a $50\ \mathrm{K}$ rise above a $40\ ^\circ\mathrm{C}$ ambient — give the maximum permissible lug temperature in °C and K and say whether the hot-spot is within limits; (c) why standards specify temperature *rise* in K rather than °C |

**Conversion relations supplied in the brief.** The first three are TT's own equations — the
Kelvin shift is boxed in **01 §1.6** (TT Eq. 1) and the two Fahrenheit relations in **01 §1.7**
(TT Eqs. 2a, 2b):

$$T(\mathrm{K}) = T(^\circ\mathrm{C}) + 273.15 \qquad
T(^\circ\mathrm{F}) = 1.8\,T(^\circ\mathrm{C}) + 32 \qquad
T(^\circ\mathrm{C}) = \frac{T(^\circ\mathrm{F}) - 32}{1.8}$$

The brief additionally supplies the Rankine relation and the degree-size identity in its hint lines.
**Rankine is not in TT** (see § Gaps); the identity is **01 §1.7**:

$$T(^\circ\mathrm{R}) = 1.8 \times T(\mathrm{K}) \qquad\text{and}\qquad \Delta T\;\text{of }1\ \mathrm{K} = \Delta T\;\text{of }1\ ^\circ\mathrm{C}$$

> ⚠ **Symbol clash — read this before answering.** In **TT** (and therefore in **01**), $T_C$ means
> **Celsius temperature**. In **HE** (and therefore in **05**), $T_C$ means the **cold-reservoir
> temperature** of a heat engine. GA1 uses the TT sense throughout. See `_nomenclature.md` **clash 11**.

---

## Part B — Sub-Topic 1.2 Part (i): Ideal gas law ·GA1 Part B (i)

**Common stem, all 8 groups.** A sealed tank contains the assigned gas at the given $P$, $V$, $T$.

1. Using $PV = mRT$, determine the **mass** of gas in the tank.
2. The gas is then heated **at constant volume until the pressure doubles**. Determine the **new
   temperature**.
3. Verify the result is consistent with **Gay-Lussac's law**, $P_1/T_1 = P_2/T_2$ at constant volume.
4. Briefly explain **one** practical electrical-engineering situation where that gas is encountered
   and its $P$–$v$–$T$ behaviour matters.

→ **02 §2.12** — the ideal gas law in specific form $Pv = RT$ / $PV = mRT$, and the specific gas
constant $R = \bar{R}/M$. → **02 §2.9** *Isochoric* for the constant-volume process.

| Group | Gas | $R$ (kJ·kg⁻¹·K⁻¹) | $P$ (kPa) | $V$ (m³) | $T$ (K) | $P_2$ (kPa) |
|---|---|---|---|---|---|---|
| **G1** | Nitrogen, N₂ | 0.297 | 180 | 1.2 | 320 | 360 |
| **G2** | Air | 0.287 | 250 | 0.9 | 310 | 500 |
| **G3** | Hydrogen, H₂ | 4.124 | 300 | 0.5 | 290 | 600 |
| **G4** | SF₆ | 0.0561 | 400 | 2.0 | 300 | 800 |
| **G5** | Oxygen, O₂ | 0.260 | 150 | 2.5 | 350 | 300 |
| **G6** | Argon, Ar | 0.208 | 200 | 1.8 | 330 | 400 |
| **G7** | Helium, He | 2.077 | 500 | 0.3 | 280 | 1000 |
| **G8** | Carbon dioxide, CO₂ | 0.189 | 350 | 0.8 | 340 | 700 |

> **Unit consistency.** With $P$ in kPa, $V$ in m³, $R$ in kJ·kg⁻¹·K⁻¹ and $T$ in K, $m = PV/(RT)$
> comes out in **kg** directly — no conversion factor. This is the reason the specific-gas-constant
> form is quoted in kJ rather than J. → **02 §2.12**.
>
> **Cross-check on G1's $R$.** **FL s34**'s specific-gas-constant table gives N₂ at
> $R = 0.2968\ \mathrm{kJ\,kg^{-1}K^{-1}}$, which rounds to the $0.297$ used here — the deck and the
> brief agree, and $R_u/M = 8.31447/28.013 = 0.2968$ confirms it. → **02 §2.12** and
> `_nomenclature.md` **clash 2**.

---

## Part B — Sub-Topic 1.2 Part (ii): Van der Waals and deviation from ideal behaviour ·GA1 Part B (ii)

**Common stem, all 8 groups.** $\bar{R} = 8.314\ \mathrm{J\,mol^{-1}K^{-1}}$ throughout. Each group is
assigned a *different* gas from its Part (i) gas.

1. Write the **Van der Waals equation for one mole** of the assigned gas, substitute $P$, $T$, $a$,
   $b$, and solve for the **molar volume** $\bar{V}$ (m³·mol⁻¹). The brief notes this is a **cubic** and
   directs groups to solve it by **trial-and-error / iterative substitution**, not by formula.
2. Using $\bar{P}\bar{V} = \bar{R}T$, calculate the **ideal-gas molar volume** at the same $P$ and $T$.
3. Compute $Z = P\bar{V}/(\bar{R}T)$ using the **Van der Waals** molar volume. **Is $Z$ greater than,
   less than, or equal to 1?** What does this indicate about the dominant effect?
4. Discuss: at what two general conditions — in terms of $T$ and $P$ **relative to the critical
   point** — does a real gas most closely approximate an ideal gas? Is the given state likely to show
   strong deviation?

→ **02 §2.12** *Other equations of state* for the `[added]` Van der Waals equation, and
*Compressibility factor $Z$* for parts 3–4. → `_formula-sheet.md` § `[added]` Van der Waals.

| Group | Gas | $M$ (g·mol⁻¹) | $a$ (J·m³·mol⁻²) | $b$ (L·mol⁻¹) | $P$ (kPa) | $T$ (K) |
|---|---|---|---|---|---|---|
| **G1** | CO₂ | 44 | 3.658 | 0.04286 | 5 000 | 320 |
| **G2** | Steam, H₂O | 18 | 5.537 | 0.03049 | 3 000 | 450 |
| **G3** | N₂ | 28 | 1.370 | 0.03870 | 8 000 | 200 |
| **G4** | Methane, CH₄ | 16 | 2.283 | 0.04278 | 6 000 | 250 |
| **G5** | Ammonia, NH₃ | 17 | 4.225 | 0.03713 | 4 000 | 370 |
| **G6** | Ethane, C₂H₆ | 30 | 5.570 | 0.06499 | 3 500 | 310 |
| **G7** | SO₂ | 64 | 6.865 | 0.05679 | 2 500 | 500 |
| **G8** | Hydrogen, H₂ | 2 | 0.2476 | 0.02661 | 10 000 | 150 |

> ### ⚠ VERIFY **V28** ·GA1 Part B (ii) — the units printed for $a$ are wrong by a factor of ten
>
> **Printed:** $a = 3.658\ \mathrm{J\,m^3\,mol^{-2}}$ for CO₂ (and similarly for all eight gases).
>
> **Should read:** $a = 3.658\ \mathrm{L^2\,bar\,mol^{-2}}$ — equivalently
> $\mathbf{0.3658\ J\,m^3\,mol^{-2}}$ in SI. **Divide every printed $a$ by 10 before substituting.**
>
> **Why.** $\mathrm{J\,m^3} = \mathrm{Pa\,m^6}$, so the printed unit claims SI. But all eight numbers
> are the **standard tabulated values in $\mathrm{L^2\,bar\,mol^{-2}}$** — CO₂ 3.658 vs the reference
> 3.640, N₂ 1.370 vs 1.370, CH₄ 2.283 vs 2.283, H₂ 0.2476 vs 0.2476, and so on for all eight. The
> conversion is $1\ \mathrm{L^2\,bar\,mol^{-2}} = 0.1\ \mathrm{Pa\,m^6\,mol^{-2}}$.
>
> **What it costs you if you miss it.** Substituting the printed value literally, the cubic has
> **exactly one real root above $b$**: $v = 4.43\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$, barely larger
> than $b$ itself, giving $Z = 0.083$. That is a **liquid-like molar volume for a gas at 5 MPa and
> 320 K** — physically impossible, and it would be the answer eight groups out of eight wrote down.
> With the corrected $a$, $Z = 0.785$, which matches published compressibility-chart data for CO₂ at
> that state. The same check passes for all eight gases, including H₂'s $Z > 1$ — the very result the
> brief's own discussion question expects.
>
> Note the brief converts $b$ correctly and spells that conversion out inline every time; only $a$'s
> unit is wrong. Full entry in `_verification-log.md`.

> ⚠ **Two unit traps in this table, both stated in the brief itself.**
>
> 1. **$b$ is given in L·mol⁻¹, not m³·mol⁻¹.** The brief spells the conversion out inline every time:
>    $0.04286\ \mathrm{L\,mol^{-1}} = 0.04286 \times 10^{-3}\ \mathrm{m^3\,mol^{-1}}$. Substituting the
>    litre figure directly into an SI equation is wrong by a factor of $10^{3}$.
> 2. **$P$ is given in kPa** and must go in as **Pa** ($5000\ \mathrm{kPa} = 5000\times10^{3}\ \mathrm{Pa}$)
>    to pair with $\bar{R}$ in J·mol⁻¹·K⁻¹.
>
> ⚠ **Symbol clash — $a$ and $b$.** FL s37 uses $a$, $b$, $c$ for the **Beattie–Bridgeman**,
> **Benedict–Webb–Rubin** and **virial** constants — entirely different equations with entirely
> different constants. GA1's $a$, $b$ are **Van der Waals**. See `_nomenclature.md` **clash 7**.

---

## Group reflection block ·GA1 Part B *(common to all groups)*

Every group brief closes with the same three prompts:

1. Agree on the concept the group understands most clearly, and one that remains unclear — raise the
   latter at plenary.
2. Confirm the spokesperson's 2-minute summary covers (a) a key insight from the discussion questions,
   (b) numerical results from Parts (i) and (ii), (c) the real-world EE example.
3. **Record any disagreements within the group and how they were resolved** — the brief notes that
   resolving a technical disagreement is itself an engineering competency.

---

## Gaps — what GA1 assesses that no lecture deck teaches

Three items are needed to answer GA1 in full. **Two are absent from all five lecture documents**; the
third is named in one deck but never given as a formula. All three are recorded in
`00-index.md` § Gap map.

| Item | Asked in | Status |
|---|---|---|
| **Van der Waals equation** and its constants $a$, $b$ | Part B (ii), all groups; Part A Q3 | ❌ absent from all five decks. Supplied `[added]` in **02 §2.12** and on `_formula-sheet.md`. FL s37 gives Beattie–Bridgeman, Benedict–Webb–Rubin and virial **instead**. |
| **Seebeck effect** / thermoelectric measurement | Part B, G1 (b); implied in Part A Q5 | ❌ absent. **TT's list of six properties (01 §1.4) does not include thermoelectric emf** — the thermocouple is not derivable from it. Outside the lecture syllabus. |
| **Rankine scale** conversion $T(^\circ\mathrm{R}) = 1.8\,T(\mathrm{K})$ | Part B, G2/G4/G6/G8 (a) | ⚠ partial. **TT (01 §1.6–§1.7) covers Celsius, Kelvin and Fahrenheit only.** Rankine is *named* once as the US absolute scale — inside the ·HE s26 quotation in **05 §5.3** — but **no conversion is given anywhere**; the brief supplies the relation in its own hint line. |

**Not a gap, despite the name:** *Gay-Lussac's law* is nowhere named in the decks, but it is not new
content — it is the ideal gas law at constant $V$ and $m$, i.e. $P/T = mR/V = \text{constant}$.
→ **02 §2.9** *Isochoric*.

---

## [added] Solutions

**None of this is in the brief.** Every value below was computed from scratch and verified — the
arithmetic independently, and the physics against published compressibility data. Method is shown so
you can check the working rather than trust the number.

> **Before Part (ii): apply V28.** Divide every printed $a$ by 10. The values used below are in SI,
> $\mathrm{Pa\,m^6\,mol^{-2}}$. See the flag box in the Part (ii) section above.

---

### S1 — Sub-Topic 1.1: temperature conversions ·GA1 Part B

$$T(\mathrm{K}) = T(^\circ\mathrm{C}) + 273.15 \qquad
T(^\circ\mathrm{F}) = 1.8\,T(^\circ\mathrm{C}) + 32 \qquad
T(^\circ\mathrm{R}) = 1.8\,T(\mathrm{K})$$

| Group | Reading | Kelvin | Second scale |
|---|---|---|---|
| **G1** | $68\ ^\circ\mathrm{C}$ | $341.15\ \mathrm{K}$ | $154.4\ ^\circ\mathrm{F}$ |
| **G2** | $95\ ^\circ\mathrm{C}$ | $368.15\ \mathrm{K}$ | $662.67\ ^\circ\mathrm{R}$ |
| **G3** | $112\ ^\circ\mathrm{C}$ | $385.15\ \mathrm{K}$ | $233.6\ ^\circ\mathrm{F}$ |
| **G4** | $78\ ^\circ\mathrm{C}$ | $351.15\ \mathrm{K}$ | $632.07\ ^\circ\mathrm{R}$ |
| **G5** | $38\ ^\circ\mathrm{C}$ | $311.15\ \mathrm{K}$ | $100.4\ ^\circ\mathrm{F}$ |
| **G6** | $55\ ^\circ\mathrm{C}$ | $328.15\ \mathrm{K}$ | $590.67\ ^\circ\mathrm{R}$ |
| **G7** | $210\ ^\circ\mathrm{C}$ | $483.15\ \mathrm{K}$ | $410.0\ ^\circ\mathrm{F}$ |
| **G8** | $74\ ^\circ\mathrm{C}$ | $347.15\ \mathrm{K}$ | $624.87\ ^\circ\mathrm{R}$ |

**The extra numeric parts:**

- **G4 (c)** — alarm threshold $85\ ^\circ\mathrm{C} = \mathbf{358.15\ K}$.
- **G5 (c)** — $-40\ ^\circ\mathrm{C} = \mathbf{233.15\ K}$. *What is notable:* $-40\ ^\circ\mathrm{C}$
  is also $-40\ ^\circ\mathrm{F}$ — the one temperature where the two scales read the same, because
  $T_F = 1.8T_C + 32$ has the fixed point $T_C = T_F = -40$.
- **G6 (b)** — insulation limit $90\ ^\circ\mathrm{C} = \mathbf{363.15\ K}$.
- **G7 (c)** — $480\ ^\circ\mathrm{F} = (480-32)/1.8 = \mathbf{248.9\ ^\circ C}$. The reading of
  $210\ ^\circ\mathrm{C}$ is **below** the limit — **within spec**, with $\approx 39\ ^\circ$ margin.
- **G8 (b)** — maximum lug temperature $= 40 + 50 = \mathbf{90\ ^\circ C} = \mathbf{363.15\ K}$. The
  measured $74\ ^\circ\mathrm{C}$ is **within limits**, $16\ ^\circ$ below.

**Short-answer parts — the points that earn the marks:**

| | Answer points |
|---|---|
| **G1 (b)** Seebeck effect | Two dissimilar conductors joined at both ends; a **temperature difference between the junctions** drives a small emf (µV/K). The measuring junction sits in the oil; the reference junction is at a known temperature. Voltage → temperature by calibration. **Not in any lecture deck** — see § Gaps. |
| **G1 (c)** thermocouple over liquid-in-glass | Remote electrical readout (no line of sight into a live 33 kV enclosure), small thermal mass so fast response, wide range, rugged, and the output can be fed to a **protection or SCADA system**. A glass thermometer can only be read by eye, on site. |
| **G2 (b)** RTD over thermocouple | RTD measures **absolute** resistance against a well-characterised, near-linear $R$–$T$ curve; no reference-junction compensation and no µV-level signal, so better accuracy and repeatability (typically ±0.1 °C vs ±1 °C) over the modest 0–150 °C winding range. |
| **G2 (c)** the law | **The zeroth law.** → **01 §1.3**. |
| **G3 (b)** non-contact on a busbar | The busbar is **live at high potential** — no safe way to attach a contact sensor without an outage. IR measurement is made from a safe distance, on load, during a survey. |
| **G3 (c)** pyrometer limitation | It reads **surface** radiance and depends on **emissivity**; a shiny/oxidised or reflective surface, or an intervening window, biases the reading. It also cannot see inside the conductor. An RTD in contact has no emissivity dependence. |
| **G4 (b)** fibre-optic over thermocouple | The fibre is a **dielectric** — it carries no metallic path into the HV winding, so it neither distorts the electric field nor provides a fault path, and it is **immune to EMI** from the winding. A thermocouple is a metallic loop in a high-field region. |
| **G5 (b)** thermocouple vs RTD for a weather station | **Recommend the RTD.** Ambient measurement needs accuracy and stability over a narrow range (say −10 to 50 °C), which is exactly the RTD's strength; response speed and extreme range — the thermocouple's advantages — are irrelevant for air temperature. |
| **G6 (c)** why ampacity depends on absolute temperature | Because the **loss and heat-transfer physics are not linear in Celsius**: conductor resistance rises with absolute temperature, radiation goes as $T^4$ in kelvin, and the insulation ageing rate is an Arrhenius function of **absolute** temperature. Only the *rise* $\Delta T$ is scale-independent. → **01 §1.7**. |
| **G8 (c)** why rise is specified in K | A **temperature rise is a difference**, and $1\ \mathrm{K} \equiv 1\ ^\circ\mathrm{C}$ by size of degree. Writing it in K makes it unambiguous that a **difference** is meant, not a temperature on the Celsius scale — a 50 K rise added to any ambient is well defined; "50 °C" invites being read as an absolute limit. → **01 §1.7**. |

---

### S2 — Sub-Topic 1.2 Part (i): ideal gas law ·GA1 Part B (i)

**Method.** With $P$ in kPa, $V$ in m³, $R$ in kJ·kg⁻¹K⁻¹ and $T$ in K, $m = PV/(RT)$ comes out in kg
with no conversion factor. Constant volume and constant mass make $P/T$ constant, so **doubling the
pressure doubles the absolute temperature**:

$$m = \frac{PV}{RT} \qquad\qquad \frac{P_1}{T_1} = \frac{P_2}{T_2} \;\Rightarrow\; T_2 = T_1\frac{P_2}{P_1} = 2T_1$$

| Group | Gas | Substitution | $m$ | $T_2$ |
|---|---|---|---|---|
| **G1** | N₂ | $(180 \times 1.2)/(0.297 \times 320) = 216/95.04$ | $\mathbf{2.273\ kg}$ | $\mathbf{640\ K}$ |
| **G2** | Air | $(250 \times 0.9)/(0.287 \times 310) = 225/88.97$ | $\mathbf{2.529\ kg}$ | $\mathbf{620\ K}$ |
| **G3** | H₂ | $(300 \times 0.5)/(4.124 \times 290) = 150/1195.96$ | $\mathbf{0.125\ kg}$ | $\mathbf{580\ K}$ |
| **G4** | SF₆ | $(400 \times 2.0)/(0.0561 \times 300) = 800/16.83$ | $\mathbf{47.534\ kg}$ | $\mathbf{600\ K}$ |
| **G5** | O₂ | $(150 \times 2.5)/(0.260 \times 350) = 375/91.0$ | $\mathbf{4.121\ kg}$ | $\mathbf{700\ K}$ |
| **G6** | Ar | $(200 \times 1.8)/(0.208 \times 330) = 360/68.64$ | $\mathbf{5.245\ kg}$ | $\mathbf{660\ K}$ |
| **G7** | He | $(500 \times 0.3)/(2.077 \times 280) = 150/581.56$ | $\mathbf{0.258\ kg}$ | $\mathbf{560\ K}$ |
| **G8** | CO₂ | $(350 \times 0.8)/(0.189 \times 340) = 280/64.26$ | $\mathbf{4.357\ kg}$ | $\mathbf{680\ K}$ |

**Part 3 — the Gay-Lussac check.** It is not a separate calculation. $P/T$ is constant at fixed $V$
and $m$, so $T_2 = 2T_1$ **is** Gay-Lussac's law; verified for all eight groups
($P_1/T_1 = P_2/T_2$ exactly, since $P_2 = 2P_1$ and $T_2 = 2T_1$). Gay-Lussac is just the ideal gas
law with $V$ and $m$ held fixed. → **02 §2.9** *Isochoric*.

> **The sanity check worth doing.** Every $m$ scales the way intuition says it should — SF₆
> ($M = 146$) gives 47.5 kg from 2 m³, while H₂ ($M = 2$) gives 0.125 kg from half a cubic metre.
> A specific gas constant is $R_u/M$, so **a heavy gas has a small $R$ and a large mass**. If your
> hydrogen answer came out heavier than your SF₆ answer, you inverted something.

**Part 4 — where each gas is met in electrical engineering:**

- **N₂ (G1)** — transformer conservator blanketing and cable-pressurisation systems; nitrogen fire
  suppression in transformer vaults.
- **Air (G2)** — air-blast circuit breakers, forced-air cooling of transformers and machines, and the
  ambient itself in every rating calculation.
- **H₂ (G3)** — **hydrogen cooling of large turbo-generators**: chosen for low density (windage loss)
  and high thermal conductivity; casing pressure and purity are monitored continuously.
- **SF₆ (G4)** — **GIS switchgear and SF₆ circuit breakers**; density (not just pressure) is monitored
  because interrupting capability depends on it, and it must be temperature-compensated.
- **O₂ (G5)** — dissolved-gas analysis of transformer oil; oxygen ingress drives insulation ageing.
- **Ar (G6)** — arc-welding shielding in steelwork and busbar fabrication; also fills some lamps.
- **He (G7)** — leak-testing sealed HV equipment and cryogenic cooling of superconducting plant.
- **CO₂ (G8)** — gaseous fire suppression in switch rooms; also a decomposition product tracked in DGA.

---

### S3 — Sub-Topic 1.2 Part (ii): Van der Waals and $Z$ ·GA1 Part B (ii)

**The equation, for one mole:**

$$\left(P + \frac{a}{\bar{V}^2}\right)\left(\bar{V} - b\right) = \bar{R}T$$

**How to solve it by hand, as the brief asks.** Do **not** expand the cubic. Rearrange it into a
fixed-point form and iterate from the ideal-gas volume:

$$\boxed{\;\bar{V}_{n+1} = b + \frac{\bar{R}T}{P + a/\bar{V}_n^{\,2}}\;,\qquad \bar{V}_0 = \frac{\bar{R}T}{P}\;}$$

Worked for **G1** (CO₂, $P = 5\times10^6$ Pa, $T = 320$ K, $a = 0.3658$, $b = 4.286\times10^{-5}$),
all volumes in $10^{-4}\ \mathrm{m^3\,mol^{-1}}$:

$$\bar{V}_0 = 5.321 \;\to\; 4.657 \;\to\; 4.407 \;\to\; 4.294 \;\to\; 4.238 \;\to\; 4.209 \;\to\; \cdots \;\to\; \mathbf{4.178}$$

It converges monotonically from above — about **12 passes** to four figures for G1, and **5** for G8.
Two or three passes are enough to see where it is heading in a 20-minute session.

**Then:**

$$\bar{V}_{\text{ideal}} = \frac{\bar{R}T}{P} \qquad\qquad Z = \frac{P\bar{V}}{\bar{R}T} = \frac{\bar{V}}{\bar{V}_{\text{ideal}}}$$

| Group | Gas | $a$ (SI) | $b\times10^{3}$ | $\bar{V}_{\mathrm{vdW}}\times10^{4}$ | $\bar{V}_{\text{ideal}}\times10^{4}$ | $Z$ | |
|---|---|---|---|---|---|---|---|
| **G1** | CO₂ | $0.3658$ | $0.0429$ | $\mathbf{4.178}$ | $5.321$ | $\mathbf{0.785}$ | $< 1$ |
| **G2** | H₂O | $0.5537$ | $0.0305$ | $\mathbf{11.168}$ | $12.471$ | $\mathbf{0.896}$ | $< 1$ |
| **G3** | N₂ | $0.1370$ | $0.0387$ | $\mathbf{1.681}$ | $2.079$ | $\mathbf{0.809}$ | $< 1$ |
| **G4** | CH₄ | $0.2283$ | $0.0428$ | $\mathbf{2.709}$ | $3.464$ | $\mathbf{0.782}$ | $< 1$ |
| **G5** | NH₃ | $0.4225$ | $0.0371$ | $\mathbf{6.538}$ | $7.690$ | $\mathbf{0.850}$ | $< 1$ |
| **G6** | C₂H₆ | $0.5570$ | $0.0650$ | $\mathbf{5.436}$ | $7.364$ | $\mathbf{0.738}$ | $< 1$ |
| **G7** | SO₂ | $0.6865$ | $0.0568$ | $\mathbf{15.488}$ | $16.628$ | $\mathbf{0.931}$ | $< 1$ |
| **G8** | H₂ | $0.0248$ | $0.0266$ | $\mathbf{1.367}$ | $1.247$ | $\mathbf{1.096}$ | $\mathbf{> 1}$ |

*(Units: $a$ in $\mathrm{Pa\,m^6\,mol^{-2}}$, $b$ and both volumes in $\mathrm{m^3\,mol^{-1}}$.
$\bar{R} = 8.314\ \mathrm{J\,mol^{-1}K^{-1}}$ throughout.)*

**Part 3 — what $Z$ means, and why G8 is the interesting one.**

- **$Z < 1$ (seven groups)** — the real molar volume is *smaller* than ideal. **Intermolecular
  attraction dominates**: molecules pull on each other, so the gas is easier to compress than an ideal
  gas. The $a/\bar{V}^2$ term is doing the work.
- **$Z > 1$ (G8, H₂)** — the real molar volume is *larger* than ideal. **Finite molecular volume —
  repulsion — dominates**: at 10 MPa the molecules are packed close enough that the excluded volume
  $b$ matters more than the very weak attraction. Hydrogen has the smallest $a$ of the eight by more
  than an order of magnitude, which is exactly why it is the one that goes above 1.
- **In practice:** a substation engineer sizing an **SF₆** compartment, or setting a density alarm on
  a **hydrogen-cooled generator**, cannot use $PV = mRT$ at rated pressure without a $Z$ correction —
  the mass of gas actually in the vessel differs from the ideal-gas figure by the same 10–25 % seen in
  the table.

**Part 4 — when a real gas behaves ideally.** **Low pressure and high temperature, judged relative to
the critical point** — i.e. high reduced temperature $T_R = T/T_c$ and low reduced pressure
$P_R = P/P_c$. Physically: low pressure means large $\bar{V}$, so $b \ll \bar{V}$ and
$a/\bar{V}^2 \ll P$; high temperature means kinetic energy swamps the attractive well depth.
**All eight states here are chosen to deviate** — every one sits at several MPa, and several
(N₂ at 200 K, NH₃ at 370 K, C₂H₆ at 310 K) sit near their critical point, which is why the group's
answer to part 4 should be *"yes, strong deviation is expected here"*. → **02 §2.12**.

---

### Cross-references

- Temperature scales, conversions, absolute zero → **01-temperature-thermometry** §1.6–§1.7.
- The zeroth law and thermal equilibrium → **01-temperature-thermometry** §1.2–§1.3.
- Thermometer types and the six exploited properties → **01-temperature-thermometry** §1.4–§1.5.
- Ideal gas law, specific gas constant, $Z$, other equations of state → **02-first-law** §2.12.
- Constant-volume (isochoric) processes → **02-first-law** §2.9.
- Van der Waals `[added]` → **02-first-law** §2.12 and `_formula-sheet.md`.
- Symbol clashes 7 ($a$, $b$) and 11 ($T_C$) → `_nomenclature.md`.
- Part 2 of the same topic → **ga2-topic1-part2-first-law.md**.

### Extraction notes for this file

Extracted from the **master brief** (`MEC_3105_Group_Exercises_Topic1_Part1`, 579 paragraphs) rather
than from the eight group submissions, so the wording is the version as set, not as re-typed by any
group. All eight groups' Part B blocks were read individually and the Part A text was confirmed
identical across them.

**Deliberately excluded:** the master's **"FACILITATOR / LECTURER NOTES (Not distributed to
students)"** section — model answers for every group plus general facilitator guidance. It is marked
not for distribution and is not reproduced, quoted or paraphrased anywhere in this knowledge base.

**No student names.** The eight submission files carry group member lists and document metadata; none
of it is reproduced. Groups are identified by number only.

**No verification flags.** Nothing in the GA1 question set is arithmetically checkable without solving
it, and this file states no results. The two unit traps noted above are **the brief's own inline
warnings**, not errors.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
