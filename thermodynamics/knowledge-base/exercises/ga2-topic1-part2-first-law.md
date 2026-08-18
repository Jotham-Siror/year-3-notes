---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "GA2 — Group Discussion Exercises, Topic 1 Part 2"
source: "GA2 — 'G2_1' … 'G2_9', nine per-group briefs (no separate master file)"
file_role: exercises
covers: "1.3 Work, Heat, and the First Law of Thermodynamics"
groups: 9
solutions: "none — questions only, by design (see § How to use this file)"
maps_to: ["02-first-law", "03b-second-law-and-cycles"]
verification_flags: 0
tags: [exercises, group-activity, first-law, sign-convention, boundary-work, internal-energy, enthalpy, specific-heats, isochoric, isobaric]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (exercises files):
  [exercise] question as set · [added] supplied here, NOT in the source ·
  → §x.y = cross-link into the topic file that covers the required theory ·
  ·GA2 G7 Task 3 = provenance (which group's brief, which task). -->

# GA2 — Topic 1 Part 2: Work, Heat and the First Law

**Assessed group activity.** 9 groups. Same six-step, ~55-minute structure as GA1.

GA2 is distributed as **nine separate per-group files** — there is no combined master. **Part A** (the
guided discussion guide and the five concept questions) is **identical across all nine** bar two
trivial rewordings in G9's copy. For **Groups 1–8**, Part B's four tasks have **fixed wording** with
only the scenario, gas and numbers varying — so this file states each stem **once** and tabulates the
per-group values.

> ### ⚠ Group 9's brief is a different document
>
> **G9's Part B was written separately and its Tasks 1–3 are not the common ones.** Task 1 is three
> entirely different sub-questions (and states $W = 0$ outright); Tasks 2 and 3 each add or re-frame a
> part; Task 4 is the only numerical Task 4 in the set. Every difference is set out in
> **§ Group 9 — Part B in full** below. **If you are in Group 9, work from that section, not from the
> common stems.**

---

## How to use this file

> ### No solutions here — deliberately
>
> This file records **the questions and where the theory for them lives**. It contains no worked
> answers, for the same reason as GA1: these are discussion exercises, and the lecture material is
> what the CAT and exam assess. Work each question from the linked section; if your answer disagrees
> with your group's, the linked section is the tie-breaker.
>
> Unlike GA1, **GA2 carries no facilitator answer key** — none of the nine files contains one.

**Reading the cross-links.** `→ 02 §2.5` means *the theory you need is in `02-first-law.md`,
section 2.5*. Almost everything for GA2 is in **02**. One item — the steady-flow energy equation —
is in no deck at all, and one is named but never analysed (§ Gaps).

---

## ⚠ Read this before anything else — the sign convention

GA2's Part A **Step 2** states the convention explicitly, and it is the one this knowledge base uses
as its default:

$$\boxed{\;\Delta U = Q - W\;}\qquad Q \;\text{positive INTO the system},\quad W \;\text{positive done BY the system}$$

> **Why this needs flagging.** The FL lecture deck states **two conflicting conventions** — s13 gives
> the physics convention ($W$ positive done *on* the system, $\Delta U = Q + W$) and s30 onward uses
> the engineering convention above. GA2 agrees with FL's **second half**. Any Part B task phrased as
> *"receives X kJ of electrical energy (work input)"* is therefore a **negative $W$**, not a positive
> one, and this catches groups out.
>
> Full treatment: **02 §2.3** — *Sign conventions — the deck states two, and they conflict*. Summary:
> `_nomenclature.md` **clash 1**.

---

## Part A — Guided discussion guide ·GA2 Part A *(common to all 9 groups)*

| Step | Time | What the group does | Theory |
|---|---|---|---|
| **1** Ice-breaker | 5 min | Each member names ONE electrical device or system that either **produces** heat as a by-product (transformer, motor, cable) or **requires** heat input to function (steam turbine). Identify whether heat and work cross the system boundary in each case, and **in which direction**. | → **02** §2.1, §2.5 |
| **2** Sign convention | 10 min | Discuss the convention above. Why must all members use the same one when applying $\Delta U = Q - W$? Give one example where getting the sign wrong causes a serious engineering error (the brief suggests **undersizing a cooling system**). | → **02** §2.3 |
| **3** Internal energy, enthalpy, specific heats | 10 min | Why is $h = u + Pv$ more convenient than $u$ for **flow devices** (boilers, turbines, pumps)? Then: for a **constant-volume** process which specific heat applies, and why? For **constant-pressure**? Agree a one-sentence explanation for each. | → **02** §2.7, §2.9 |
| **4** Numerical problem | 20 min | *"Solve **all three** numerical tasks in Part B"* — Tasks 1–3. Every member contributes at least one calculation step. State formula → substitution → answer with units for every part. **Task 4 belongs to Step 5, not here** *(except for G9, whose Task 4 is numerical)*. | → Part B below |
| **5** Real-world EE discussion | 5 min | Answer the group's Task 4 scenario, connecting the first law to a practical EE consequence: equipment sizing, protection setting, safety, or efficiency. | → Task 4 below |
| **6** Summary | 5 min | Elect a spokesperson; 2-minute summary covering (a) a concept insight, (b) all numerical results, (c) the real-world EE conclusion. | — |

---

## Part A — Common concept discussion questions ·GA2 Part A *(all groups)*

The brief states these are **not formally assessed** but support the numerical work and plenary.

**[exercise] Q1 — Heat and work are not the same thing.**
A student argues *"heat and work are the same thing since both involve energy"*. **Construct a clear
counterargument** using the definitions of heat and work, and give one specific EE example where the
distinction matters critically (the brief suggests: sizing a cooling system *versus* calculating
output shaft power).
→ **02 §2.1** (heat as a form of energy) and **02 §2.11** (energy transfer by work). → **02 §2.2**
builds both from the same piston-and-cylinder, which is the sharpest way to see the difference.

**[exercise] Q2 — Path functions versus point functions.**
$U$ is a **property** of a system; $Q$ and $W$ are not. **Explain what this means** in terms of path
functions versus point functions. Why does the distinction matter when analysing a **cycle** such as
the Rankine cycle in a steam power station?
→ **02 §2.3** — work as an inexact differential, $\delta W$. → **03b §3b.4** for the cyclic
consequence ($\Delta U = 0$ around a cycle, so $Q_{net} = W_{net}$); §3b.3 defines the cycle itself. → **04 §4.4** carries a
**⚠ VERIFY V20** on exactly this point: TC s12 calls enthalpy "the total heat content of a system",
conflating a state function with a path-dependent transfer.

**[exercise] Q3 — Is enthalpy "just a made-up convenience"?**
A group member says $H = U + PV$ adds nothing that $U$ does not already capture. **Do you agree?**
Justify by showing **step by step** why the **steady-flow energy equation** for a turbine or boiler is
more naturally written in enthalpy than in internal energy.
→ **02 §2.7** — *Constant-pressure processes and enthalpy*, which shows that at constant pressure the
boundary work is not free information but is absorbed into $H$. ⚠ **The SFEE itself is in no lecture
deck** — see § Gaps.

**[exercise] Q4 — Why $c_p > c_v$.**
For an ideal gas $c_p - c_v = R$. **Explain physically** what extra energy input constant-pressure
heating requires that constant-volume heating does not. How does this relate to **boundary work**?
→ **02 §2.9** (the four elementary processes) and **02 §2.11** (boundary work). Mayer's relation
$c_p - c_v = R$ is on `_formula-sheet.md`; FL states it in **molar** form via $\gamma$ at s28, so watch
the basis — see the unit note under Task 3.

**[exercise] Q5 — The 1000 MW / 350 MW power station.**
For a complete cycle $\Delta U = 0$, so $Q_{net} = W_{net}$. Using this, **explain why a station taking
1000 MW of thermal input and delivering 350 MW of electrical output must reject exactly 650 MW** as
waste heat. What does the first law tell us about **where that waste heat ultimately goes**?
→ **03b §3b.3–§3b.4** — the cyclic energy balance and thermal efficiency. → **05 §5.1** for the
heat-engine framing. Note the first law only accounts for the 650 MW; **why it cannot be recovered as
work is a second-law question** → **03b §3b.5** (Kelvin–Planck) and **03b §3b.11** (quality of energy).

---

## Part B — Task 1: First law for a closed system ·GA2 Part B Task 1

**Common stem, Groups 1–8** *(Group 9's Task 1 is different — see below).* Given the scenario's
two energy quantities:

1. Using $\Delta U = Q - W$, determine the **change in internal energy**. State whether it
   **increases or decreases**, and explain physically what that means for the system described.
2. **Classify the process**: heat addition or heat rejection? Work done BY or ON the system? Confirm
   the sign convention is consistently applied.
3. If the process repeats for **500 identical cycles**, what is the **total** change in internal
   energy? Comment on what that implies for the long-term thermal condition of the system.

→ **02 §2.4** (formal statements) and **02 §2.5** (energy balance, closed system).

| Group | Engineering context | Scenario as set |
|---|---|---|
| **G1** | Standby diesel generator set | The engine cylinder **receives 950 kJ** of heat from combustion and **does 620 kJ** of boundary work on the piston during one power stroke. |
| **G2** | Gas-insulated switchgear (GIS) compartment | During a fault arc, **1200 kJ** of heat is deposited into the SF₆ gas, and the gas **does 480 kJ** of expansion work against the enclosure walls. |
| **G3** | Li-ion battery cell, fast charging | The cell **receives 800 kJ of electrical energy (treated as work input)** and **rejects 180 kJ** of heat to the cooling system during a fast-charge cycle. |
| **G4** | Electric motor under load | The motor **receives 1500 kJ of electrical energy (work input)** and **rejects 420 kJ** as heat through cooling fins and housing. |
| **G5** | Power transformer under overload | Over a 30-minute overload, core and windings **absorb 2200 kJ** of heat from internal losses and **dissipate 1750 kJ** through cooling oil and radiators. |
| **G6** | Steam turbine-generator, load rejection | Steam trapped in the casing **releases 650 kJ** of heat through the casing walls and **does 280 kJ** of expansion work. |
| **G7** | Underground cable joint, short circuit | The joint **absorbs 1800 kJ** of I²R heating during a fault and **dissipates 400 kJ** by conduction to the soil before the relay clears. |
| **G8** | PV inverter enclosure | Over one hour at peak generation the electronics **dissipate 560 kJ** of heat internally while the cooling fans **remove 490 kJ** from the enclosure. |
| **G9** | Wind turbine nacelle | The nacelle **accumulates 1050 kJ** of heat from copper, core and switching losses; the cooling system **removes 870 kJ** to the external airstream over the same period. **⚠ G9's three sub-questions are different — see § Group 9.** |

> ⚠ **The scenarios are not all the same shape — read each one's second quantity carefully.**
>
> - **G1, G2, G6** are the textbook shape: a heat term and a **boundary-work** term. $Q$ and $W$ map
>   directly onto $\Delta U = Q - W$.
> - **G3, G4** give **electrical energy in, explicitly labelled "work input"**. Under the stated
>   convention ($W$ positive done *by* the system), work *into* the system is $W < 0$. The heat term is
>   also *out*, so $Q < 0$. Both signs must flip before substitution. → **02 §2.3**.
> - **G5, G7, G8** (and **G9**) give **two heat terms** — heat generated internally and heat removed by
>   a cooling system. **Neither is boundary work.** These are $Q_{in}$ and $Q_{out}$ in a closed system
>   doing no work, so the balance reduces to $\Delta U = Q_{net}$ with $W = 0$. Treating the
>   cooling-system term as $W$ is a sign-convention error, not a shortcut. → **02 §2.5**.
>
> For G5, G7 and G8 the brief leaves this for the group to make out; the wording *"dissipates"*,
> *"removes"*, *"rejects … through cooling"* is the tell. **G9's separately-written brief states
> $W = 0$ outright** — which is the confirmation that the same reading is right for the other three.

> **Part 3 of the stem is generic across Groups 1–8** — *"500 identical cycles (e.g., 500 power
> strokes, or 500 charge cycles)"* — and is worded for a reciprocating or charge-cycle system. For the
> continuous-dissipation scenarios (G5, G7, G8) read "cycle" as "repetition of the stated event".

---

## Part B — Task 2: Boundary work at constant pressure ·GA2 Part B Task 2

**Common stem, Groups 1–8.** A gas expands at constant pressure from $V_1$ to $V_2$. **G9 adds a
further clause to part 3** — see § Group 9.

1. Calculate the **boundary work** using $W = P(V_2 - V_1)$.
2. State whether the work is done **BY** or **ON** the gas, and explain how the **sign** of the answer
   reflects that.
3. Sketch (or describe) the process on a $P$–$V$ diagram and **shade the area** representing the
   boundary work. Explain **why the area under the $P$–$V$ curve represents work**.

→ **02 §2.11** — *Energy transfer by work; boundary work*, including the $\int P\,dV$ area argument.
→ **02 §2.9** *Isobaric*.

| Group | Gas | $P$ (kPa) | $V_1$ (m³) | $V_2$ (m³) |
|---|---|---|---|---|
| **G1** | Air | 300 | 0.10 | 0.35 |
| **G2** | Nitrogen, N₂ | 450 | 0.05 | 0.20 |
| **G3** | Hydrogen, H₂ | 200 | 0.08 | 0.30 |
| **G4** | Carbon dioxide, CO₂ | 500 | 0.06 | 0.25 |
| **G5** | Oxygen, O₂ | 250 | 0.12 | 0.40 |
| **G6** | Argon, Ar | 350 | 0.07 | 0.28 |
| **G7** | Helium, He | 150 | 0.15 | 0.45 |
| **G8** | Methane, CH₄ | 400 | 0.09 | 0.32 |
| **G9** | Propane, C₃H₈ *(brief also gives $R = 0.189\ \mathrm{kJ\,kg^{-1}K^{-1}}$)* | 280 | 0.11 | 0.38 |

> **Units.** $P$ in kPa times $V$ in m³ gives **kJ** directly. Every group's $V_2 > V_1$, so every
> group's answer is an **expansion** — positive $W$ under the stated convention, work done **by** the
> gas. Part 2 of the stem is asking you to say so, not to discover an exception.
>
> **G9's $R$ is not needed for Task 2** — $W = P\,\Delta V$ requires no gas constant. It appears to be
> carried over from the Task 3 data block. Propane's actual specific gas constant is
> $\approx 0.1886\ \mathrm{kJ\,kg^{-1}K^{-1}}$, so the value itself is right for propane; it is simply
> unused here. *(Note the coincidence with GA1's CO₂ figure — the same number, a different gas.)*

---

## Part B — Task 3: Constant-volume heating and the first law ·GA2 Part B Task 3

**Common stem, Groups 1–8.** **G9's part 3 is differently framed** — see § Group 9.

1. Calculate the heat supplied using $Q = m\,c_v\,(T_2 - T_1)$.
2. Since the volume is constant, **what is the boundary work**? Hence find $\Delta U$ from the first
   law and **verify it equals $Q$**.
3. In an EE context, explain ONE situation where a gas or fluid is heated at approximately constant
   volume, and why knowing the **internal energy rise** — not just the temperature rise — matters for
   safe equipment design.

→ **02 §2.9** *Isochoric* — where $W = 0$ and the first law collapses to $\Delta U = Q = m c_v \Delta T$.
→ **02 §2.5** for the closed-system balance.

| Group | Gas | $m$ (kg) | $c_v$ (kJ·kg⁻¹·K⁻¹) | $T_1$ (K) | $T_2$ (K) |
|---|---|---|---|---|---|
| **G1** | Air | 3.0 | 0.718 | 300 | 520 |
| **G2** | N₂ | 2.5 | 0.743 | 290 | 550 |
| **G3** | H₂ | 0.5 | 10.18 | 295 | 400 |
| **G4** | CO₂ | 4.0 | 0.657 | 310 | 480 |
| **G5** | O₂ | 5.0 | 0.658 | 305 | 460 |
| **G6** | Ar | 6.0 | 0.312 | 320 | 500 |
| **G7** | He | 1.0 | 3.116 | 300 | 600 |
| **G8** | CH₄ | 2.0 | 1.706 | 298 | 450 |
| **G9** | Propane, C₃H₈ | 3.5 | 1.490 | 308 | 490 |

> **Mass basis, not molar basis.** Every $c_v$ here is **specific** (per kg). FL states the
> specific-heat relations in **molar** form at s28 via $\gamma$, so converting basis is on you —
> $c$ (per kg) $= \bar{c}$ (per mol) $/\,M$. → **02 §2.9** *Adiabatic* and `_formula-sheet.md`.
>
> **Cross-check available — but match the *gas*, not the group number.** Mayer's relation
> $c_p - c_v = R$ lets you check a row against the specific gas constant for **the same gas** in GA1
> Part B (i). The group numbers do not line up: GA2's **G2 is N₂**, whose $R = 0.297$ comes from
> **GA1's G1**. That pair gives $0.743 + 0.297 = 1.040\ \mathrm{kJ\,kg^{-1}K^{-1}}$, the standard N₂
> $c_p$. Seven of the nine rows can be checked this way; **CH₄ (G8) and propane (G9) cannot** — neither
> gas has a specific gas constant in GA1 Part B (i). *(G9's own Task 2 header does supply propane's
> $R = 0.189$.)* → `_formula-sheet.md`.

---

## Part B — Task 4: Real-world electrical engineering application ·GA2 Part B Task 4

**Common prompts, Groups 1–8.** For the group's scenario:

- Identify the **system boundary** and state **what crosses it** — heat, work, or both.
- Write the first-law energy balance $\Delta U = Q - W$ for that specific EE system, **assigning
  correct signs**.
- State ONE practical engineering decision that depends directly on this balance — a cooling-system
  size, a protection relay setting, an insulation rating, or a safety clearance time.

→ **02 §2.5** (energy balance) and **02 §2.3** (signs). For the efficiency-framed scenarios (G4, G8,
G9) → **03b §3b.4** and **05 §5.1**.

| Group | Scenario |
|---|---|
| **G1** | The generator's cooling system must remove **22 kW** of waste heat continuously. Explain via the first law why not all combustion heat becomes electrical output, and why the cooling system must be sized for this load. |
| **G2** | After a fault arc the GIS enclosure temperature rises sharply. Explain why the enclosure must withstand **both** the pressure rise (gas expansion) and the temperature rise (internal energy), and why the two effects are **inseparable**. |
| **G3** | Battery thermal management and thermal runaway: explain why **fast** charging raises internal energy faster than slow charging, and why this is a thermal-management challenge for grid-scale BESS. |
| **G4** | A motor nameplate states **92 % efficiency**. Determine what happens to the remaining **8 %** of input electrical energy, and discuss the implications for enclosure ventilation and thermal protection relay settings. |
| **G5** | Transformer insulation life halves for every ~8 °C sustained rise above rated temperature. Explain how the net internal-energy increase during an overload translates into a temperature rise, and why **overload duration matters as much as magnitude**. |
| **G6** | During load rejection, overspeed protection must act within seconds. Explain how the sudden removal of electrical load (work output) affects the internal energy of the steam in the turbine, and why this can cause a dangerous temperature and pressure spike if steam supply is not simultaneously cut. |
| **G7** | Relay engineers set fault clearance times partly to limit the thermal energy deposited in cables and joints (the $I^2R\,t$ product). Explain how a **longer clearance time** increases the internal-energy rise in the joint, and why insulation or joint failure can follow **even after the fault is cleared**. |
| **G8** | PV inverter efficiency is typically 96–98 %, so 2–4 % of DC input is dissipated inside the enclosure. Explain how this accumulates as internal energy in the components (particularly **IGBT modules**), and why high ambient temperature reduces efficiency further through the feedback effect on **junction temperature**. |
| **G9** | Wind turbines in Kenya's Rift Valley (e.g. Lake Turkana Wind Power) run hot and dusty. Generator output **850 kW** from a mechanical shaft input of **910 kW**; ambient reaches **42 °C**. **The only numerical Task 4 in the set — see § Group 9.** |

---

## Group 9 — Part B in full ·GA2 G9

G9's file was authored separately from the other eight. Its **data** is the same shape, and the tables
above carry G9's numbers correctly — but **its questions are not the common ones**, so they are set out
here in full.

### G9 Task 1 — first law for a closed system

*Scenario as in the Task 1 table: 1050 kJ accumulated from generator copper, core and switching
losses; 870 kJ removed by the cooling system over the same period.*

1. Using $\Delta U = Q - W$, determine the **net change in internal energy of the nacelle thermal
   mass** over this period. **The brief states outright that the enclosure does no boundary work
   (rigid enclosure), so $W = 0$.** State whether internal energy — and hence the temperature of the
   equipment inside — is rising or falling, **and by how much**.
2. The **IGBT modules** are the most thermally sensitive components. If the net internal-energy rise
   from (1) raises the average nacelle air temperature by **6 °C**, and the IGBT junction sits
   **15 °C above** nacelle air temperature at rated load, determine the **new junction temperature**
   from a starting nacelle air temperature of **35 °C**. Comment on whether this approaches a typical
   IGBT maximum junction temperature of **150 °C**.
3. If this accumulation of **+180 kJ per period** continues over **8 consecutive periods** (8 hours of
   high wind), what is the **total internal-energy rise**? Discuss what operational action a wind-farm
   **SCADA** system should trigger once a temperature threshold is reached.

> **Two things to notice.** The brief **gives away part 1's answer inside part 3** — the $+180$ kJ is
> $1050 - 870$. And by stating $W = 0$ explicitly it confirms what the other two-heat-term scenarios
> (G5, G7, G8) leave implicit: **a cooling system's heat removal is $Q_{out}$, never $W$.**

### G9 Task 2 — boundary work

Parts 1 and 2 as the common stem. **Part 3 carries a clause the other groups do not have:** after
shading the area under the $P$–$V$ curve, explain **what would change on the diagram if the pressure
were not constant** — e.g. for a **polytropic** process. → **02 §2.10**.

### G9 Task 3 — constant-volume heating

Parts 1 and 2 as the common stem. **Part 3 is differently framed:** give one practical example of a
gas or fluid heated at approximately constant volume **inside sealed electrical equipment**, and
explain why the resulting **pressure rise** — from the ideal gas law at constant volume — is an
important **safety** design consideration. → **02 §2.12**, and **02 §2.9** *Isochoric*.

*(The other eight groups' part 3 asks about the internal-energy rise, not the pressure rise.)*

### G9 Task 4 — the only numerical Task 4 in the set

*Scenario as in the Task 4 table: Rift Valley siting, 42 °C ambient, 850 kW electrical out of 910 kW
mechanical shaft in.*

1. Apply the first law to the generator as a system: identify $Q$, $W$ and $\Delta U$ **per unit
   time, in kW**, with correct signs. **What is the rate of internal-energy accumulation if the
   cooling system removes heat at only 48 kW?**
2. Explain why the same generator that runs safely at a European site (ambient 15 °C) may overheat at
   42 °C **even at the same electrical output** — use the reduced $\Delta T$ between equipment surface
   and ambient air.
3. State ONE practical engineering measure (**other than reducing output**) that would restore
   $\Delta U \approx 0$ at high ambient temperature, and explain how it works thermodynamically.

> **Note on part 1.** It asks for a **rate** balance in kW — $\dot{Q}$, $\dot{W}$,
> $\mathrm{d}U/\mathrm{d}t$ — rather than the energy balance in kJ used in Tasks 1–3. FL states the
> balance in both forms. → **02 §2.5** → *The four forms of the balance*.

---

## Group reflection block ·GA2 Part B *(Groups 1–8)*

1. Agree on one aspect of the first law that initially seemed counter-intuitive, and how the group
   resolved it.
2. Confirm the numerical working **for all three tasks** is recorded as **formula → substitution →
   answer with units** at every step.
3. Prepare the spokesperson's 2-minute summary: (a) concept insight, (b) numerical results, (c) the
   real-world EE conclusion.

*G9's version names the parts explicitly — "(a) one concept insight **from Part A**, (b) all numerical
results from Part B **Tasks 1–3**, (c) your real-world EE conclusion **from Task 4**" — which is the
same content, spelled out.*

---

## Gaps — what GA2 assesses that no lecture deck teaches

| Item | Asked in | Status |
|---|---|---|
| **Steady-flow energy equation (SFEE)** | Part A Q3 — *"show step by step why the SFEE for a turbine or boiler is more naturally written in enthalpy"* | ❌ **absent from all five decks.** FL covers enthalpy (§2.7) and closed-system balances but never writes a flow-device energy equation. Symbols $h_1$, $h_2$ appear in `_nomenclature.md` marked GA2-only. Tracked in `00-index.md` § Gap map. |
| **Rankine cycle**, named as an example | Part A Q2 | ⚠ partial. **05 §5.4** lists the Rankine cycle as a machine type and **04 §4.5** maps it to steam plant, but **no deck gives a Rankine efficiency formula or a cycle analysis** — a course-wide gap that also covers Otto, Diesel, Brayton and Stirling. → **05 §5.4** § *No MEC 3105 document supplies an efficiency formula…* and `_formula-sheet.md` § `[added]` named-cycle efficiencies. |

**Not gaps.** Mayer's relation, the four elementary processes, boundary work, enthalpy, the cyclic
$\Delta U = 0$ result and the sign conventions are all taught — in **02** and **03b** — and linked from
the relevant question above.

---

### Cross-references

- The first law, its formal statements and the energy balance → **02-first-law** §2.4–§2.5.
- ⚠ The two conflicting sign conventions → **02-first-law** §2.3; `_nomenclature.md` **clash 1**.
- Boundary work and the $P$–$V$ area argument → **02-first-law** §2.11.
- Isochoric and isobaric processes; specific heats → **02-first-law** §2.9.
- Enthalpy → **02-first-law** §2.7; and **04-thermodynamic-cycles** §4.4 for **⚠ V20**.
- Cycles, $\Delta U = 0$, thermal efficiency → **03b-second-law-and-cycles** §3b.3–§3b.4.
- Why waste heat is unavoidable → **03b-second-law-and-cycles** §3b.5, §3b.11; **05-heat-engines-and-carnot** §5.1.
- Part 1 of the same topic → **ga1-topic1-part1-equations-of-state.md**.

### Extraction notes for this file

Extracted from all **nine** per-group files (`G2_1` … `G2_9`), and **every group's Part B stem was
diffed against every other's**, not sampled. Findings:

- **Part A is identical across Groups 1–8**, apart from the group number. **G9's copy carries two
  trivial rewordings** — Step 5 opens "Connect the First Law…" rather than "This should connect the
  First Law…", and its concept-questions header adds "(All Groups — …)". No question changes.
- **Groups 1–8's Part B stems are identical**, with only the assigned gas name substituted in.
- **Group 9's file was authored separately** — re-titled Part B header, a completely different Task 1,
  an added clause in Task 2, a re-framed Task 3 part 3, and the set's only numerical Task 4. All of it
  is transcribed in § Group 9 above. **No facilitator or model-answer section exists in any of the nine
files** — checked by search.

**No student names.** Group identification is by number only.

**No verification flags.** This file states no results, so there is nothing arithmetic to verify. The
three reading warnings above — the sign convention, the mixed scenario shapes in Task 1, and the
mass-vs-molar basis in Task 3 — are **hazards in applying the questions**, not errors in them.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
