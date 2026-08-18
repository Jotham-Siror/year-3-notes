---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "04 — Thermodynamic Cycles: Concepts, Analysis and Selection"
source: "TC — '3.1 MEC 3105 Power production and Thermodynamic Cycles.pdf', 24 slides"
slides: "1-24"
file_role: topic
subtopics:
  - "what a thermodynamic cycle is; the closed-loop concept"
  - "state points and the processes that connect them"
  - "cycle diagrams: P-V, T-s and P-h"
  - "entropy and enthalpy, as this deck defines them"
  - "engineering applications: which cycle models which machine"
  - "factors that control real cycle performance"
  - "cycle-level analysis equations: net work, thermal efficiency, COP"
  - "cycle selection workflow and checklist"
  - "deviations from ideal analysis; common mistakes"
key_equations: [net-work-cycle, thermal-efficiency, cop-refrigerator, enthalpy-def]
prerequisites: ["02-first-law", "03b-second-law-and-cycles"]
leads_to: ["05-heat-engines-and-carnot"]
verification_flags: 12
tags: [thermodynamic-cycles, state-points, p-v-diagram, t-s-diagram, p-h-diagram, thermal-efficiency, cop, cycle-selection, common-mistakes, entropy, enthalpy]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered slide · [hist] historical/biographical note ·
  [added] supplied here, NOT in the source ·
  ·TC sN = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md. -->

# 04 — Thermodynamic Cycles: Concepts, Analysis and Selection

Scope: the whole of TC, 24 slides. A **qualitative and definitional** deck. It frames what a cycle is,
how state points and processes build one, how the three diagram types are read, which cycle models which
machine, what controls real performance, and — uniquely in the whole course — **how cycle analysis goes
wrong in practice**.

> ### ⚠ Read this before citing any TC slide — the numbering is not what the outline suggests
>
> **TC slide 2 is a full-bleed image with no text layer at all** (0 characters; verified). It carries no
> title, and nothing in the deck refers to it. Every title therefore sits **one slide later** than a
> text-only outline of the deck implies.
>
> All `·TC sN` citations in this file are **true PDF page numbers**, checked against the rendered
> images. If a reference looks one off from a contents listing, this is why.
>
> **This also corrects `../sources/SOURCES.md`**, which records TC as having no image-only pages. It has
> one: slide 2.

> ### ⚠ What TC does NOT contain — read this before relying on it
>
> | Expected | Present? |
> |---|---|
> | Efficiency formula for **Otto, Diesel, Brayton, Rankine** | ❌ **none** |
> | **Stirling** cycle | ❌ never mentioned in TC at all |
> | Carnot efficiency $\eta = 1 - T_L/T_H$ | ❌ not written (asserted in words only) |
> | **Process sequences** for any named cycle | ❌ none |
> | **Entropy equation** of any kind | ❌ words only in the body — the only symbolic entropy statements are the *third-law* annotations on the orphan slide 2 (§4.11) |
> | $\mathrm{COP}_{HP}$ formula | ❌ described in prose, never written |
> | **Worked example / any arithmetic** | ❌ **zero numbers in 24 slides** |
> | Mass-flow or power forms ($\dot Q$, $\dot W$, $\dot m$) | ❌ none |
>
> **TC contains four equations in its body** (slides 12, 17, 18, 19), plus the third-law annotations on the decorative slide 2. The Diesel-efficiency gap left open by
> EPC is **still open after TC** — see the gap map in `00-index.md`.

---

## 4.1 What a thermodynamic cycle is ·TC s3–s7

[def] A **thermodynamic cycle** is a repeating path of processes that returns a system to its starting
state after exchanging heat and work. ·TC s3

[def] Understood as a **closed loop**: the working fluid changes *pressure, temperature, volume, or
phase, exchanges heat and work*, and then returns to the same starting state. ·TC s5

> **The caution TC attaches to its own metaphor** ·TC s5 — *"the important idea is not that every part
> of the system is physically moving in a circle, but that the thermodynamic state repeats after one
> full operating sequence."*

**What returns and what does not** ·TC s6 — because the initial and final states are the same, the
**state properties** ($P$, $T$, $v$, $u$, $h$, $s$) all return to their starting values after one
complete cycle. The cycle can still produce a useful result:

- a **power cycle** converts part of the heat input into net work output;
- a **refrigeration or heat pump cycle** uses work input to move heat **against its natural direction**.

[def] **Core engineering idea** ·TC s7

> **Over a complete cycle the system returns to the same state, but the surroundings do not.** The
> useful engineering result comes from the net heat and work exchanged with the surroundings during that
> loop.

> **That is the sharpest single sentence in the deck.** It explains why $\Delta U = 0$ over a cycle
> (`02-first-law` §2.5) yet a cycle still does something: the bookkeeping closes for the *system*, not
> for the *universe*. Everything a cycle achieves is recorded in the surroundings.

**Engineering use** ·TC s3–s4 — cycles are the foundation for engines, power plants, refrigeration
systems, heat pumps, gas turbines and many HVAC systems. ·TC s4 restates the same idea: cycles are
*"repeated sequences of heat and work interactions that return a system to its initial state"*, and they
explain how engines produce power, how refrigerators move heat from cold spaces to warm surroundings,
and how engineers compare **efficiency, losses and operating limits** of real energy systems.

**Practical check** ·TC s3 — ideal cycle diagrams are useful for learning, but real equipment loses
performance through *friction, pressure drop, heat leakage, non-ideal compression, and finite
heat-transfer rates*.

**What controls it** ·TC s3 — temperature limits, pressure ratios, working-fluid properties, component
efficiencies, heat-transfer limits and irreversibilities control real cycle performance.

---

## 4.2 State points and processes ·TC s8–s10

[def] A **state point** describes the condition of the working fluid at a specific location or stage in
the cycle. ·TC s9

TC's two examples of where the state points sit: ·TC s9

| System | State points tracked |
|---|---|
| Vapour-compression refrigeration | compressor inlet, compressor outlet, condenser outlet, expansion-device outlet, evaporator outlet |
| Gas turbine | around the compressor, combustor, turbine and exhaust |

[def] A cycle is built from individual **processes**; each changes the state of the working fluid in a
controlled way — *compression, expansion, heating, cooling, evaporation, condensation, throttling, or
heat rejection*. Engineers connect those processes into a loop and then evaluate the heat and work
transfer **across the system boundary**. ·TC s8

**What each process type does** ·TC s10

- **Compression** usually requires **work input**.
- **Expansion through a turbine** can produce **work output**.
- **Heat addition** raises the energy of the working fluid.
- **Heat rejection** removes energy **so the cycle can return to its initial condition**.

> **Note the last one.** Heat rejection is not waste to be engineered away — it is *what closes the
> loop*. That is the same result as EPC's "Can we save $Q_{out}$?" (·EPC s52): a firm no, because without
> it the cycle cannot be completed. See `03b-second-law-and-cycles` §3b.5.

[fig ·TC s9, s10, s11] A **$P$–$v$ diagram of the Carnot cycle**, reproduced identically on all three
slides. Axes $P$ (vertical) and $v$ (horizontal). Four numbered states: **1** upper left, **2** to its
right, **3** lower right, **4** lower left. Path 1→2 along a shallow curve labelled
"$T_H$ = const."; 2→3 falling steeply; 3→4 leftward along a curve labelled "$T_L$ = const."; 4→1 rising.
Circulation **clockwise**. The enclosed area is shaded pink and labelled $W_{net,out}$. Two thick block
arrows cross the boundary: $Q_H$ **in** across 1–2, $Q_L$ **out** across 3–4.

*This is the same figure as ·EPC s70 (top). See `03b` §3b.8 for the four processes in full.*

> ⚠ VERIFY **C24** ·TC s9, s10 — the identical figure appears on two consecutive slides with no change
> or added annotation, and both carry **stray artefacts**: two thin blue leader arrows entering
> from off-slide and pointing at states 1 and 2 — these are **PowerPoint shapes overlaid on s9 and
> s10**, not part of the imported graphic — plus a truncated "…" mark at the right end of the $T_L$
> isotherm, which **is** inside the source image. Cosmetic only.

---

## 4.3 Cycle diagrams ·TC s11

[def] Cycles are shown on **pressure–volume ($P$–$V$)**, **temperature–entropy ($T$–$S$)** or
**pressure–enthalpy ($P$–$H$)** diagrams. These plots help engineers see **work areas, heat transfer
trends, compression behaviour, phase changes, and departures from ideal performance**. ·TC s11

[fig ·TC s11] Three figures on one slide.

**(1)** The Carnot $P$–$v$ diagram of §4.2.

**(2)** A **$T$–$s$ diagram**, captioned "T - s diagram". Vertical axis *Temperature*, horizontal axis
*Entropy*. Two dashed horizontal guides label $T_1 = T_2$ (upper) and $T_3 = T_4$ (lower). Four states:
**1** upper left, **2** upper right, **3** lower right, **4** lower left. Legs: 1→2 **horizontal
rightward**; 2→3 **vertical downward**; 3→4 **horizontal leftward**; 4→1 drawn as a **curve rising up-and-to-the-right** — entropy *increases* along it. Circulation clockwise. Additional curves beyond the cycle suggest a saturation dome.

**(3)** A **pressure–enthalpy chart** of the ideal refrigeration cycle, titled "The Ideal Refrigeration
Cycle graphed onto a Pressure Enthalpy Chart". Vertical axis *PRESSURE (Abs)*, horizontal axis
*ENTHALPY (BTU/Lb.)*. A saturation dome with three labelled regions — *Sub-cooled Liquid* (left),
*Liquid - Vapour mixture* (inside), *Superheated Vapour* (right). A red four-sided cycle runs
**counter-clockwise** with its legs named rather than numbered: **Condensation** (top, leftward),
**Expansion** (left, downward), **Evaporization** (bottom, rightward), **Compression** (right, rising).

> ⚠ VERIFY **V23** ·TC s11 — in the $T$–$s$ figure, **2→3 is drawn as a straight vertical line but 4→1
> is drawn as a curve**. With the state numbering shown — matched to the adjacent Carnot $P$–$v$
> diagram, where 2→3 and 4→1 are the two **isentropes** — *both* legs must be vertical. An isentropic
> process is by definition a vertical line on $T$–$s$; the drawn 4→1 leg changes $s$. The two
> "isentropes" of one figure are inconsistent with each other. **See `05-heat-engines-and-carnot` for
> the correct Carnot rectangle.** See `_verification-log.md`.

> ⚠ VERIFY **C22** ·TC s11 — the $P$–$h$ chart is in **imperial units** (BTU/Lb.) in an otherwise SI
> deck, and prints **"Evaporization"** for *Evaporation*. Two faint rotated grey labels on the
> saturation dome are **illegible at the render resolution** — they are not transcribed here rather than
> guessed. They appear to be region annotations, not data.

> **How to read the counter-clockwise direction.** A **clockwise** loop on $P$–$V$ or $T$–$s$ is a
> **power** cycle (net work out); **counter-clockwise** is a **refrigeration/heat-pump** cycle (net work
> in). Figure (3) is counter-clockwise and is correctly a refrigeration cycle. This matches ·EPC s70 —
> see `03b` §3b.8.

---

## 4.4 Entropy and enthalpy, as TC defines them ·TC s12

This slide carries **the only definitions of entropy and enthalpy in the deck**, and three of the file's
five substantive flags. Treat it with care.

**Entropy — printed verbatim:** ·TC s12

> "A thermodynamic quantity representing the unavailability of a system's thermal energy for conversion
> into mechanical work, often interpreted as the degree of disorder or randomness in the system"
>
> *"the second law of thermodynamics says that entropy always increases with time"*
> *"the sum of the entropies of all the bodies taking part in the process"*

> ⚠ VERIFY **V19** ·TC s12 — *"entropy always increases with time"* is **wrong as stated**. It is the
> entropy of an **isolated** system that never decreases:
> $$\Delta S_{\text{isolated}} \ge 0$$
> The entropy of a *system* can and routinely does decrease — that is what heat rejection does.
>
> **The check is on TC's own slide.** In the $T$–$s$ figure on ·TC s11, process **3→4 runs leftward —
> entropy decreasing**. The deck contradicts itself one slide earlier. See `_verification-log.md`.

**Enthalpy — printed verbatim:** ·TC s12

$$H = E + PV$$

> "It is a thermodynamic state function that represents the total heat content of a system. It depends
> only on the system's temperature, pressure, and composition — not on the path taken to reach that
> state."

> ⚠ VERIFY **V20** ·TC s12 — enthalpy is **not "the total heat content of a system"**. $H = U + PV$ is a
> **state function**; heat is a **path-dependent transfer across a boundary**, not a stored property.
> The phrase is a well-known misconception and the deck states it as a definition.
>
> **The check:** a throttling process has $\Delta H = 0$ with $Q = 0$, yet a real temperature change.
> "Heat content" cannot account for that. Note also that TC's own ·s24 lists conflating quantities like
> this among the **common mistakes**.

> ⚠ VERIFY **V21** ·TC s12 — *"depends only on the system's temperature, pressure, and composition"* is
> **false in the two-phase region**, where $T$ and $P$ are **not independent**. Specific enthalpy is
> fixed by **two independent** intensive properties; inside the dome you also need the **quality**.
>
> **The check:** at $100\ ^\circ\mathrm{C}$ and $101.325\ \mathrm{kPa}$ water can be saturated liquid
> ($h \approx 419\ \mathrm{kJ/kg}$) or saturated vapour ($h \approx 2676\ \mathrm{kJ/kg}$) — same $T$,
> same $P$, same composition, enthalpy differing by a factor of about **6.4**. Total $H$ also scales
> with mass, which the statement omits.

> ⚠ VERIFY **C21** ·TC s12 — writes $H = E + PV$ using **$E$** for internal energy, where
> `02-first-law` and the rest of the course use **$U$** ($E$ is reserved there for *total* energy
> $U + \mathrm{KE} + \mathrm{PE}$). Use $H = U + PV$; see `_nomenclature.md`.

> ### [added] What a correct entropy definition would say
>
> TC gives **no entropy equation**, and neither does EPC. Since the course never supplies one:
>
> $$dS = \frac{\delta Q_{\text{rev}}}{T} \qquad\text{and}\qquad \Delta S_{\text{isolated}} \ge 0$$
>
> For the Carnot cycle specifically, $\Delta S = Q_H/T_H$ on 1–2 and $-Q_L/T_L$ on 3–4, and these are
> equal in magnitude — which is exactly why $Q_L/Q_H = T_L/T_H$ (·EPC s76, see `03b` §3b.9).
> **Marked `[added]`: this is not in any MEC 3105 document.**

---

## 4.5 Which cycle models which machine ·TC s13

The deck's cycle→application map, printed as bullets: ·TC s13

| Application | Cycle(s) named | Equipment |
|---|---|---|
| **Power generation** | Rankine · Brayton | steam power plants · gas turbines and jet engines |
| **Internal combustion** | Otto · Diesel | spark-ignition and compression-ignition engines |
| **Cooling and heat pumping** | Vapour-compression | refrigerators, air conditioners, chillers, heat pumps |
| **Performance benchmarking** | Carnot | ideal upper limit for heat-engine efficiency between two reservoirs |
| **Waste-heat recovery** | *(none named)* | evaluating whether rejected heat can be recovered for power, heating or process use |

*(TC prints these as five prose bullets; the table is a `[added]` reformatting for navigation. No table
of cycles against their process sequences exists anywhere in TC.)*

**Why engineers use cycles** ·TC s13 — to predict how much useful output can be obtained from heat, how
much work is required to move heat, and **where real equipment wastes energy**.

> **This is the map to memorise, and it is all TC gives on the named cycles.** Each is named and matched
> to a machine; **none is analysed**, and no process sequence or efficiency formula is supplied. The
> Carnot bullet asserts the upper-limit property without ever writing the bound.

---

## 4.6 What controls real cycle performance ·TC s14–s15

**The framing** ·TC s14 — real performance is controlled by more than the ideal diagram: temperature
limits, pressure levels, working-fluid behaviour, component losses, heat-exchanger performance and
operating constraints all affect efficiency and reliability.

The deck's table, reproduced faithfully: ·TC s15

| Factor | Why it matters | Engineering implication |
|---|---|---|
| **Temperature limits** | Hot and cold reservoir temperatures strongly influence the maximum possible efficiency or COP. | Higher source temperatures can improve power-cycle efficiency, while smaller temperature lifts improve refrigeration and heat pump performance. |
| **Pressure ratio** | Affects compressor work, turbine work, temperature rise and component stress. | An aggressive pressure ratio may improve ideal output but increase real losses, material demands, leakage and operating risk. |
| **Working fluid** | Controls phase-change behaviour, property tables, safety, environmental impact and equipment compatibility. | Steam, air, refrigerants, combustion gases and organic working fluids each lead to different cycle layouts and constraints. |
| **Component efficiency** | Compressors, pumps, turbines, nozzles and heat exchangers do not behave ideally. | Small drops in component efficiency can noticeably reduce net work output, cooling capacity or overall system COP. |
| **Irreversibilities** | Friction, turbulence, heat transfer across finite temperature differences, throttling and mixing generate entropy. | Irreversibilities reduce the useful work available and move real performance away from ideal predictions. |

> **Row 1 is the quantitative one and TC leaves it qualitative.** "Temperature limits strongly influence
> the maximum possible efficiency" *is* $\eta = 1 - T_L/T_H$ — the formula EPC supplies (·EPC s75) and
> TC does not. The "smaller temperature lifts improve refrigeration performance" clause is
> $\mathrm{COP}_R = T_L/(T_H - T_L)$, likewise from EPC. **Use `03b` §3b.9–3b.10 for the numbers.**
>
> Row 5 connects to EPC's itemised irreversibility list (·EPC s66) — see `03b` §3b.2.

---

## 4.7 Cycle analysis equations ·TC s16–s19

### Symbols, as the deck defines them ·TC s16

The slide is titled *"Cycle Analysis Equations"* and carries a **KEY VARIABLES** panel — and **no
equation**.

| Symbol | Definition (verbatim) | Units as printed |
|---|---|---|
| $W_{net}$ | Net work over one cycle, usually in kJ, Btu, kW, or hp depending on whether energy or power rate is being evaluated. | kJ, Btu, kW, hp |
| $Q_{in}$ | Heat added to the cycle from a high-temperature source, such as combustion, a boiler, solar heat, or an external heat exchanger. | — |
| $Q_{out}$ | Heat rejected from the cycle to a lower-temperature sink, such as ambient air, cooling water, a condenser, or exhaust stream. | — |
| $\mathrm{COP}_R$ | Refrigeration coefficient of performance, a ratio of cooling effect to work input. | — |

> ⚠ VERIFY **V22** ·TC s16 — the units given for $W_{net}$ mix **energy and power in one symbol**. Work
> per cycle is energy (**kJ, Btu**); **kW and hp are power** and belong to a rate quantity
> $\dot W_{net}$, which the deck never introduces.
>
> **The check is dimensional:** $\mathrm{kJ} = \mathrm{J}$, $\mathrm{kW} = \mathrm{J\,s^{-1}}$. One
> symbol cannot carry both. And TC's own ·s24 lists **"Confusing energy and power"** as the first common
> mistake — which ·s16 then commits. See `_verification-log.md`.

> ⚠ VERIFY **C25** ·TC s16, s19 — $Q_L$, $Q_H$ and $W_{in}$ appear in the ·s19 equation and in the
> ·s9–s11 figures but are **never defined** anywhere in TC. $\eta_{th}$ and $\mathrm{COP}_{HP}$ are
> **absent from the glossary**, and **no $\mathrm{COP}_{HP}$ formula is given** although ·s19's prose
> promises the heat-pump case and ·s24 requires the student to use it. Take the definitions from
> `03b` §3b.6 and `_nomenclature.md`.

### The three equations

[eq: net-work-cycle] ·TC s17

$$\boxed{\;W_{net} = Q_{in} - Q_{out}\;}$$

For a heat engine operating in a cycle, the net work output equals the heat added minus the heat
rejected. **This relationship is useful because the internal energy returns to its starting value after
one complete cycle.** ·TC s17

*[added] ✓ Verified — this is `02-first-law` §2.5's $W_{net,out} = Q_{net,in}$ with $\Delta U = 0$, and
identical to ·EPC s48. Consistent across all three documents.*

[eq: thermal-efficiency] ·TC s18

$$\boxed{\;\eta_{th} = \frac{W_{net}}{Q_{in}} = 1 - \frac{Q_{out}}{Q_{in}}\;}$$

Used for **power-producing** cycles — steam power cycles, gas turbine cycles, idealised internal
combustion cycles. ·TC s18

*[added] ✓ Verified as an identity by substituting ·s17: $(Q_{in}-Q_{out})/Q_{in} = 1 - Q_{out}/Q_{in}$.
Internally consistent, and identical to ·EPC s50's form.*

[eq: cop-refrigerator] ·TC s19

$$\boxed{\;\mathrm{COP}_R = \frac{Q_L}{W_{in}}\;}$$

For a refrigerator, the COP compares the desired cooling effect $Q_L$ to the required work input.
**A heat pump uses a similar idea, but the desired output is the heat delivered to the warm space.**
·TC s19

*[added] ✓ Verified; matches ·EPC s54. With $W_{in} = Q_H - Q_L$ it gives EPC's
$\mathrm{COP}_R = Q_L/(Q_H - Q_L)$. The heat-pump counterpart, which TC never writes, is
$\mathrm{COP}_{HP} = Q_H/W_{in} = \mathrm{COP}_R + 1$ — see `03b` §3b.6.*

[eq: enthalpy-def] ·TC s12 — $H = E + PV$ (read as $H = U + PV$; see C21 above).

> **That is the complete equation inventory of TC: four equations in 24 slides**, on slides 12, 17, 18
> and 19. All four are correct. None is cycle-specific.

---

## 4.8 Cycle selection ·TC s20–s22

**Define the objective first** ·TC s20 — a system designed to produce shaft work, cool a space, pump
heat, or recover waste heat will use **different performance metrics and different practical
constraints**.

**The practical workflow, as printed** ·TC s20

> desired output → identify the heat source and heat sink → choose a working fluid → map the major state
> points → estimate ideal performance → add component losses → check temperatures, pressures, materials,
> safety and controllability

The deck's selection checklist: ·TC s21

| Check or decision | What to look for | Why it matters |
|---|---|---|
| **Define the objective** | Power output, cooling capacity, heating capacity, waste-heat recovery, or efficiency improvement. | Determines whether efficiency, COP, net work, heat rate or capacity is the main performance metric. |
| **Identify temperature reservoirs** | Available source temperature, required sink temperature, ambient conditions, process temperature limits. | Temperature limits set the theoretical ceiling for performance and strongly influence equipment size. |
| **Choose the working fluid** | Steam, air, refrigerant, combustion gas, organic fluid, or another process-specific fluid. | Fluid properties control phase change, pressure levels, safety, materials compatibility and property-data needs. |
| **Estimate real component losses** | Compressor efficiency, pump work, turbine efficiency, pressure drop, heat-exchanger approach temperature, leakage. | Real equipment performance can differ significantly from ideal cycle diagrams. |
| **Check operating range** | Startup, part-load operation, seasonal conditions, fouling, cycling, control stability. | A cycle that looks good at one design point may perform poorly or become unreliable across the real operating envelope. |

**Why cycles at all** ·TC s22 — ideal cycles are **learning tools and starting points for engineering
estimates**. Real systems operate with non-ideal equipment, imperfect controls, changing ambient
conditions, fouled heat exchangers, pressure losses and material limits.

> **The judgement TC asks for** ·TC s22 — *"Engineers should be able to separate cycle efficiency from
> system usefulness. A slightly less efficient cycle may be the better design if it is safer, cheaper,
> easier to control, more reliable at part load, compatible with available fluids, or easier to
> maintain."*
>
> This is the deck's real contribution. Nothing in EPC or HE makes this point, and it is the kind of
> claim a discussion-type exam question rewards.

---

## 4.9 Deviations from ideal analysis ·TC s23

Simplified cycle analysis becomes **less reliable when the assumptions no longer match the real
system** — especially when a textbook cycle is used to estimate performance for actual equipment. ·TC s23

| Deviation | What it does |
|---|---|
| **Large pressure drops** | Piping, valves, heat exchangers, filters and fittings shift state points away from the ideal cycle. |
| **Non-constant properties** | Real gases, refrigerants, steam and mixtures may need **property tables or software** instead of simple ideal-gas assumptions. |
| **Transient operation** | Startup, shutdown, cycling and part-load behaviour may not match steady-state assumptions. |
| **Heat leakage** | Unwanted heat gain or loss changes the balance between $Q_{in}$, $Q_{out}$ and useful work. |
| **Control limitations** | Expansion valves, compressors, burners, pumps and turbines must operate within stable and safe control ranges. |

> ⚠ VERIFY **C23** ·TC s23 — the final bullet **ends with a comma**, not a full stop: *"…must operate
> within stable and safe control ranges,"*. A clause or a sixth bullet appears to have been dropped.
> Nothing can be recovered from the slide, so nothing is supplied here.

---

## 4.10 Common mistakes ·TC s24

Most mistakes come from **mixing ideal theory with real equipment assumptions without stating where each
applies**. TC's stated remedy: **define the boundary, label every heat and work interaction, and keep
sign conventions consistent.** ·TC s24

| Mistake | The correction |
|---|---|
| **Confusing energy and power** | Heat and work per cycle are **energy**; power depends on the rate at which the cycle repeats or mass flows through the system. |
| **Using the wrong performance metric** | Heat engines use **thermal efficiency**; refrigerators and heat pumps use **coefficient of performance**. |
| **Ignoring pressure drop** | Pressure losses in heat exchangers and piping materially change compressor work, turbine work and capacity. |
| **Assuming reversible behaviour** | Real compression, expansion, heat transfer and throttling **generate entropy** and reduce useful performance. |
| **Forgetting the working fluid** | A cycle diagram is incomplete without fluid properties, phase behaviour and safe operating limits. |

> ### This slide is the most examinable thing in TC
>
> A "state three common errors in cycle analysis" question is answerable directly from here, and the
> content appears in **no other MEC 3105 document**.
>
> **Note the irony worth remembering:** TC's advice to *"keep sign conventions consistent"* is precisely
> what FL fails to do (`02-first-law` §2.3, flags V5–V8), and its warning about *"confusing energy and
> power"* is what ·TC s16 itself commits (V22). The advice is sound; the deck does not always follow it.

---

## 4.11 [added] The Third Law — the deck's orphan slide ·TC s2

·TC s2 is a full-bleed decorative infographic, untitled, with **no text layer**, in a deck about power
production and cycles. Nothing refers to it. Recorded here because **it is the only place in the entire
MEC 3105 course where the third law appears**.

[fig ·TC s2] Blueprint-style infographic headed **"Third Law of Thermodynamics"**, sub-labelled
"ABSOLUTE ZERO LIMIT". Centre panel: an ice crystal beside a cubic crystal lattice, captioned *"NEAR
ABSOLUTE ZERO: Molecular motion is minimized; order is maximized."* A temperature bar runs from **0 K /
ABSOLUTE ZERO** (left, blue) to **HIGHER T** (right, red). A call-out reads *"As temperature approaches
0 K, entropy approaches a minimum constant value."* A boxed equation gives

$$S \rightarrow \text{minimum constant as } T \rightarrow 0\ \mathrm{K}
\qquad\text{equivalently}\qquad \lim_{T \to 0} S = \text{constant minimum}$$

Faint background watermarks include a $P$–$V$ axis pair, $dU = \delta Q - \delta W$, $S \ge 0$, and a
thermometer graduated 300 / 200 / 100 K down to 0 K.

*[added] ✓ The statement is a correct **Nernst-form** third law. (The stronger **Planck** form sets
$S \to 0$ for a perfect crystal.) The watermark $dU = \delta Q - \delta W$ matches `02-first-law` §2.5's
convention B ✓.*

> ⚠ VERIFY **C19** ·TC s2 — off-topic, untitled and unreferenced, and because it carries no text layer
> it **shifts every subsequent slide number by one** relative to a text-based contents listing. That is
> the citation hazard flagged at the top of this file, and it also means
> `../sources/SOURCES.md` is wrong to list TC as having no image-only pages.

---

### Cross-references

- $W_{net} = Q_{in} - Q_{out}$ and $\Delta U = 0$ over a cycle → **02-first-law** §2.5.
- **Everything quantitative about efficiency, COP and Carnot lives in `03b-second-law-and-cycles`**,
  which is authoritative for those concepts. TC states them qualitatively; do not derive from TC.
- The correct Carnot $T$–$s$ rectangle (cf. V23) → **05-heat-engines-and-carnot**.
- Irreversibilities, itemised → **03b** §3b.2. Reversibility as a benchmark → **03b** §3b.2.
- Enthalpy, derived properly → **02-first-law** §2.7.
- $H = E + PV$ symbol clash, and the undefined $Q_H$/$Q_L$/$W_{in}$ → **`_nomenclature.md`**.

- **⚠ V20** (§4.4 — enthalpy called "total heat content") is the exact confusion
  **exercises/ga2-topic1-part2-first-law** Part A Q2 asks students to unpick.

### Verification notes for this section

All 24 slides read from **170 dpi renders**, including the image-only slide 2. The
**KEY VARIABLES** panel (s16) and both equation slides (s18, s19) were additionally re-read directly
against the source to confirm the transcription.

**There is no arithmetic anywhere in TC** — no worked example, no substituted number, no computed
result. The only numerals of any kind are the unit "1" in s18's efficiency equation, "MEC 3105" on the
title slide, and the annotations on the decorative slide 2; the last of these check out (0 K as
absolute zero; monotonic 100 / 200 / 300 K ticks; a correct Nernst statement).

**All four equations are correct**, and all four agree with EPC and FL where they overlap.

| ID | Slide | Class | Summary |
|---|---|---|---|
| **V19** | s12 | substantive | "entropy always increases with time" — true only for an **isolated** system; contradicted by TC's own $T$–$s$ figure |
| **V20** | s12 | substantive | enthalpy called "the total heat content of a system" — $H$ is a state function, heat is a path function |
| **V21** | s12 | substantive | "depends only on $T$, $P$ and composition" — fails in the two-phase region |
| **V22** | s16 | substantive | $W_{net}$ given both energy and power units; the deck's own s24 names this as a top mistake |
| **V23** | s11 | substantive | $T$–$s$ figure draws 2→3 vertical but 4→1 curved; both are isentropes and must be vertical |
| **C19** | s2 | cosmetic | off-topic untitled Third Law infographic; shifts all slide numbering; contradicts `SOURCES.md` |
| **C21** | s12 | cosmetic | $H = E + PV$ uses $E$ where the course uses $U$ |
| **C22** | s11 | cosmetic | "Evaporization"; imperial BTU/Lb in an SI deck; two illegible dome labels |
| **C23** | s23 | cosmetic | final bullet ends with a comma — clause apparently dropped |
| **C24** | s9, s10 | cosmetic | identical figure on consecutive slides; stray blue leader arrows from the source graphic |
| **C25** | s16, s19 | cosmetic | $Q_L$, $Q_H$, $W_{in}$ never defined; $\eta_{th}$ and $\mathrm{COP}_{HP}$ absent from the glossary; no $\mathrm{COP}_{HP}$ formula |
| **C26** | s3, s12, s19 | cosmetic | template drift — s3 in a serif face unlike every other slide; s12's quotation marks close with low/German-style glyphs; s19's title overflows two lines; inconsistent ellipsis lengths across s16–s19 titles |

**Gap-map consequences of this build:**

| Row | Verdict after TC |
|---|---|
| Worked Otto / Diesel / Brayton / Rankine analysis | ❌ **still absent.** TC names the cycles (s13) and never analyses one. No efficiency formula, no process sequence. |
| Entropy as a property | ❌ **still absent.** Words only (s12), and that wording is itself wrong (V19). The only quantitative entropy statement is on the orphan slide 2, and it is a *third-law* statement. |
| $\mathrm{COP}_{HP}$ | ❌ not in TC. Available in `03b` §3b.6 from EPC. |
| Selection workflow, common mistakes | ✅ **TC is authoritative** — s20–s24, content found nowhere else. |
| Cycle → application map | ✅ **TC is authoritative** — s13. |
| $P$–$h$ diagram | ✅ **TC only** — s11 is the sole $P$–$h$ chart in the course. |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
