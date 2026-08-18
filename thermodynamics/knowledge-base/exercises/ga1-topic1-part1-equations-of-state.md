---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "GA1 — Group Discussion Exercises, Topic 1 Part 1"
source: "GA1 — 'MEC_3105_Group_Exercises_Topic1_Part1' (master brief) + 8 group submissions"
file_role: exercises
covers: "1.1 Temperature and Thermometry | 1.2 Equations of State (Ideal Gas Law and Van der Waals)"
groups: 8
solutions: "none — questions only, by design (see § How to use this file)"
maps_to: ["01-temperature-thermometry", "02-first-law"]
verification_flags: 0
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

> ### No solutions here — deliberately
>
> This file records **the questions and where the theory for them lives**. It contains no worked
> answers. Two reasons:
>
> 1. These are discussion exercises, not a problem bank. Their weight in the course is small; the
>    lecture material is what the CAT and exam assess.
> 2. The master brief carries a **"FACILITATOR / LECTURER NOTES (Not distributed to students)"**
>    section with model answers. That section is **not reproduced anywhere in this knowledge base** —
>    it is marked not for distribution, and this repository is public.
>
> Work each question from the linked section. If your answer disagrees with your group's, the linked
> section is the tie-breaker.

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
