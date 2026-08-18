---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "05 — Heat Engines and the Carnot Cycle"
source: "HE — '3.2 MEC 3105 Power production and Thermodynamic Cycles.pdf', 30 slides"
slides: "1-30"
file_role: topic
subtopics:
  - "what a heat engine is; the three roles every heat engine needs"
  - "heat engine efficiency equations"
  - "Carnot efficiency and the absolute-temperature requirement"
  - "types of heat engines: Otto, Diesel, Brayton, Rankine, Stirling, Carnot"
  - "heat engine analysis checklist"
  - "the Carnot cycle: four processes, P-V and T-s diagrams"
  - "the Carnot process table with entropy behaviour"
  - "reversed Carnot cycle for refrigerators and heat pumps"
  - "why Carnot efficiency depends only on temperature"
  - "the T-s rectangle and the course's only entropy equations"
  - "Carnot cycle analysis workflow and checks"
key_equations: [heat-engine-work, heat-engine-efficiency, carnot-efficiency, carnot-heat-ratio, carnot-entropy]
prerequisites: ["01-temperature-thermometry", "02-first-law", "03b-second-law-and-cycles"]
leads_to: []
verification_flags: 6
tags: [heat-engine, thermal-efficiency, carnot, carnot-efficiency, t-s-diagram, entropy, reversed-carnot, cop, absolute-temperature, unit-traps]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered slide · [hist] historical/biographical note ·
  [added] supplied here, NOT in the source ·
  ·HE sN = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md. -->

# 05 — Heat Engines and the Carnot Cycle

Scope: the whole of HE, 30 slides. The course's closing document, and — despite being the shortest
treatment — **the one that supplies three things found nowhere else**: the Carnot efficiency formula,
the correct Carnot $T$–$s$ rectangle, and the only entropy equations in MEC 3105.

> ### ⚠ HE uses $Q_C$ and $T_C$ where EPC uses $Q_L$ and $T_L$
>
> Same quantities, different subscript. **C for cold, L for low.** HE is consistent within itself;
> `03b-second-law-and-cycles` is consistent within itself; they simply disagree with each other. Read
> $Q_C \equiv Q_L$ and $T_C \equiv T_L$ throughout. Registered in `_nomenclature.md`.

> ### ✅ HE's figures are the trustworthy ones
>
> Its $P$–$V$ diagram (·HE s18) and $T$–$s$ rectangle (·HE s28) are both correct and mutually
> consistent — and they are the **only correct $T$–$s$ Carnot rectangle in the course**. ·TC s11's
> $T$–$s$ figure draws one isentrope vertical and the other slanted (V23), and **this deck's own title
> infographic (·HE s2) gets it wrong twice** (V25, V27). **When a Carnot diagram is needed, use s18 and
> s28 — not s2.**

> ### ⚠ HE contains no worked example and no arithmetic
>
> Like TC, and unlike EPC. **`03b-second-law-and-cycles` remains the only source of worked numbers in
> the entire course** — nine examples, all verified correct.

---

## 5.1 What a heat engine is ·HE s3–s5

[def] A **heat engine** is a system that repeatedly goes through a thermodynamic cycle to convert
thermal energy into useful work. The working fluid may be combustion gas, steam, air, refrigerant or
another fluid depending on the engine type. During the cycle the system **receives heat, expands or
otherwise produces work, rejects heat, and returns to its starting state**. ·HE s3

> **The engineering framing HE adds** ·HE s3 — *"The key engineering question is not simply whether heat
> can become work, but how much work can be extracted reliably, safely, and economically from a given
> temperature difference."*

[def] **The three roles every heat engine needs** ·HE s4

1. a **high-temperature energy source**;
2. a **working device or fluid** that produces work;
3. a **lower-temperature sink** that receives rejected heat.

The engine **repeats** this process so it can deliver continuous or repeated work output rather than a
single one-time expansion. ·HE s4

- $Q_H$ — heat supplied by the hot reservoir. In a gasoline engine this comes from combustion inside
  the cylinder; in a steam plant, fuel or another heat source produces steam that expands through a
  turbine. ·HE s4
- $W_{out}$ — the useful work output, the part of the incoming energy that becomes mechanical output.
- $Q_C$ — the remainder, rejected to a cold sink: atmosphere, cooling water, exhaust stream, radiator,
  condenser or surrounding environment. ·HE s4

> **A practical engine must manage both sides** ·HE s4 — extracting useful work **and** removing waste
> heat without overheating equipment. Heat rejection is a design requirement, not an afterthought.

**Applications** ·HE s5

| Sector | Machines |
|---|---|
| **Power plants** | steam turbines and gas turbines driving generators |
| **Transportation** | gasoline, diesel, jet and marine engines converting fuel energy into propulsion |
| **Industrial systems** | turbines, engines and waste-heat recovery supporting pumps, compressors, generators and mechanical drives |

[fig ·HE s2] A full-bleed "Heat Engines — Converting Heat Into Useful Work" infographic on a blueprint
background. Centre: a hot reservoir at $T_H$ feeding $Q_H$ into a cutaway turbine labelled *Heat
Engine*, which emits $W_{out}$ (*Useful Work*) to the right and $Q_C$ downward into a cold reservoir at
$T_C$. Right panel prints $W_{out} = Q_H - Q_C$ and
$\eta = W_{out}/Q_H = 1 - Q_C/Q_H$. Left, two small insets: a **$T$–$s$ diagram** with states 1, 2, 3, 4
and dashed guides at $T_H$ and $T_C$; and a **$p$–$V$ diagram** with a shaded area labelled $W_{out}$.
Bottom strip: three *Common Examples* — internal combustion engine, gas turbine, steam power plant.

> ⚠ VERIFY **V24** ·HE s2 — in the **$p$–$V$ inset**, the lower-left and lower-right states are **both
> labelled "4"**. There is no state 3. The states should run 1 (upper left) → 2 (upper right) → **3**
> (lower right) → 4 (lower left), as they correctly do in the $T$–$s$ inset directly above it and in
> ·HE s18. See `_verification-log.md`.

> ⚠ VERIFY **V25** ·HE s2 — in the **$T$–$s$ inset**, the **upper isotherm 1→2 is drawn descending**:
> state 2 sits well below the $T_H$ guide line, about 14° off horizontal. On a $T$–$s$ diagram an
> isothermal process is by definition a **horizontal** line, so state 2 is not at $T_H$ as drawn.
> *(The lower isotherm 3→4 **is** drawn correctly — both 3 and 4 sit on the $T_C$ guide.)* This
> contradicts ·HE s28 of the same deck, which draws the rectangle correctly and says in words that it
> **is** a rectangle. See `_verification-log.md`.

> ⚠ VERIFY **V27** ·HE s2 — in the same **$T$–$s$ inset**, the **arrows do not form a traversable
> loop**. The left leg's arrowhead points **downward (1→4)** while the bottom leg points leftward
> (3→4): **two arrows converge on state 4 and none leaves it**, and state 1 has two outgoing arrows.
> A cycle must have exactly one arrow in and one out at every state. The left leg should point
> **upward, 4→1**. ·HE s18 and ·HE s28 both draw the directions correctly. See
> `_verification-log.md`.

---

## 5.2 What controls heat engine performance ·HE s6–s7

A heat engine is controlled by more than its fuel source: efficiency and power output depend on
**temperature limits, pressure ratios, working-fluid behaviour, heat-transfer rates, component losses**,
and how closely the actual cycle follows the ideal cycle used in analysis. ·HE s6

The deck's factors table: ·HE s7

| Factor | Why it matters | Engineering implication |
|---|---|---|
| **Hot-side temperature** | A higher source temperature increases the theoretical opportunity to convert heat into work. | Engineers seek higher combustion, steam or turbine inlet temperatures, but **materials and cooling limits become critical**. |
| **Cold-side temperature** | A lower sink temperature improves the theoretical efficiency limit. | Condensers, radiators, cooling towers and ambient conditions strongly affect real performance. |
| **Irreversibility** | Friction, turbulence, pressure drops, heat leakage and non-ideal combustion **destroy useful work potential**. | Requires better component design, tighter tolerances, improved heat exchangers and better controls. |
| **Cycle type** | Different cycles add and reject heat in different ways. | Otto, Diesel, Brayton, Rankine, Stirling and combined cycles are selected for different fuels, scales and operating goals. |
| **Operating load** | Engines rarely operate at their ideal design point all the time. | Part-load operation, transient duty, startup losses and cycling reduce real-world efficiency below rated values. |

> **Rows 1 and 2 are $\eta = 1 - T_C/T_H$ in words**, and HE — unlike TC — goes on to write the formula
> (§5.3). Note the engineering constraint the table adds: raising $T_H$ helps, but **materials limit how
> far you can go**. That trade-off is the reason real plants sit far below Carnot.

---

## 5.3 Heat engine efficiency equations ·HE s8–s10

### Symbols, as HE defines them ·HE s8

| Symbol | Definition (verbatim) |
|---|---|
| $Q_H$ | Heat absorbed from the hot reservoir, usually in joules, kilojoules, Btu, or kJ/kg for specific cycle analysis. |
| $Q_C$ | Heat rejected to the cold reservoir, condenser, exhaust, radiator, cooling water, or surrounding environment. |
| $W_{out}$ | Useful net work output from the cycle, often measured as shaft work, brake work, turbine work, or specific work. |
| $\eta$ | Thermal efficiency, usually reported as a decimal or percentage. |

*[added] Note the contrast with ·TC s16, which gives $W_{net}$ the units "kJ, Btu, kW, or hp" and so
mixes energy with power (V22). **HE's glossary is clean** — it keeps $Q_H$ in energy or specific-energy
units and does not confuse the two.*

### The two equations ·HE s9

[eq: heat-engine-work]

$$\boxed{\;W_{out} = Q_H - Q_C\;}$$

[eq: heat-engine-efficiency]

$$\boxed{\;\eta = \frac{W_{out}}{Q_H} = 1 - \frac{Q_C}{Q_H}\;}$$

*[added] ✓ Verified as an identity: $(Q_H - Q_C)/Q_H = 1 - Q_C/Q_H$. Identical in content to ·EPC s50
and ·TC s18, with $Q_C$ in place of $Q_L$/$Q_{out}$. All three documents agree.*

> **The caution printed beside it** ·HE s9 — *"The equation shows why reducing rejected heat or
> increasing useful work improves efficiency, but it does not mean rejected heat can be reduced to
> zero. A cyclic heat engine must reject heat to operate between two reservoirs."*
>
> That is the Kelvin–Planck statement restated as a design fact — see `03b` §3b.5.

### Carnot efficiency ·HE s10

[eq: carnot-efficiency]

$$\boxed{\;\eta_{Carnot} = 1 - \frac{T_C}{T_H}\;}$$

The Carnot efficiency gives the **maximum possible** efficiency for any heat engine operating between a
hot and a cold reservoir. **It is an upper bound, not a prediction of real engine performance.** ·HE s10

> ### ⚠ The unit trap — HE states it twice, and it is the clearest statement in the course
>
> ·HE s10: *"The reservoir temperatures $T_H$ and $T_C$ **must be absolute temperatures, normally
> Kelvin**. Using Celsius or Fahrenheit in this equation is **one of the most common heat engine
> calculation errors**."*
>
> ·HE s26 repeats it: *"$T_H$ and $T_C$ must be absolute temperatures. Use **Kelvin** in SI work or
> **Rankine** in US customary work. **Do not use degrees Celsius or degrees Fahrenheit directly in the
> ratio.**"*
>
> The lecturer prints this warning on **two separate slides**, and ·HE s14 and ·HE s30 list it again as
> a checklist item. **Treat that repetition as a signal about what gets marked.** This is the payoff of
> `01-temperature-thermometry` §1.6–1.7.

---

## 5.4 Types of heat engines ·HE s11–s12

Heat engines can be grouped by **where combustion occurs**, **what working fluid is used**, and **which
thermodynamic cycle best represents the process**. The ideal cycle is a model; the real machine
includes losses, controls, hardware limits and operating constraints. ·HE s11

The deck's six-cycle table: ·HE s12

| Engine or cycle | Common example | Useful engineering idea |
|---|---|---|
| **Otto cycle** | Spark-ignition gasoline engine | Understanding compression ratio, combustion timing, and piston engine efficiency. |
| **Diesel cycle** | Compression-ignition diesel engine | Heavy vehicles, generators, marine engines, high-torque applications. |
| **Brayton cycle** | Gas turbine or jet engine | Propulsion, power generation, combined-cycle power plants. |
| **Rankine cycle** | Steam turbine power plant | Steam power generation, boilers, condensers, pumps, turbine analysis. |
| **Stirling cycle** | External combustion engine | External heat addition, regeneration, temperature-difference engines. |
| **Carnot cycle** | Ideal reference engine | Defines the theoretical efficiency limit between two reservoirs. |

> ### ⚠ This table settles the course's biggest gap — negatively
>
> Six cycles are named and characterised. **Not one efficiency formula is given for any of them except
> Carnot.** Combined with EPC (which analyses none) and TC (which names them on ·TC s13 and analyses
> none), this is now confirmed across all five lecture documents:
>
> **No MEC 3105 document supplies an efficiency formula for the Otto, Diesel, Brayton, Rankine or
> Stirling cycle.** The standard forms are supplied `[added]` in `_formula-sheet.md`; see also
> `03b` §3b.12 for the Diesel case.
>
> HE is also the **only** document that mentions the **Stirling** cycle at all — TC never does.

---

## 5.5 Heat engine analysis checklist ·HE s13–s14

**The practical workflow** ·HE s13

> Start with the energy flows: identify $Q_H$, $Q_C$ and $W_{out}$. Then confirm the cycle type,
> reservoir temperatures, working fluid, units, and whether the result is **ideal, indicated, brake, net
> or overall system** efficiency. Finally, compare the result against the **Carnot limit** and look for
> real losses that explain the gap.

The checklist table: ·HE s14

| Check or decision | What to look for | Why it matters |
|---|---|---|
| **Define the system boundary** | Engine only, turbine only, full plant, vehicle powertrain, or combined-cycle system. | Efficiency changes depending on what losses are inside the boundary. |
| **Confirm the heat reservoirs** | Hot source temperature, cold sink temperature, condenser temperature, radiator conditions, ambient temperature. | The temperature difference sets the theoretical opportunity for work production. |
| **Check units and temperature scale** | **Use Kelvin for Carnot efficiency** and consistent units for heat and work. | Unit mistakes can produce **impossible efficiencies** or misleading comparisons. |
| **Identify the efficiency type** | Thermal, indicated, brake, cycle, component, or overall plant efficiency. | Two engines can appear different simply because the calculation boundary is different. |
| **Look for rejected heat recovery** | Exhaust heat, condenser heat, recuperators, regenerators, combined-cycle steam bottoming. | Recovering waste heat can improve total system performance even when base engine efficiency is limited. |

> **"Unit mistakes can produce impossible efficiencies"** is the practical tell. If you substitute
> Celsius into $1 - T_C/T_H$ you can get a negative number, or a value above the true limit — either is
> a sign you skipped the conversion.

---

## 5.6 The Carnot cycle ·HE s15–s20

[def] **Core idea** ·HE s15 — the Carnot cycle is an **ideal reversible heat-engine cycle** that gives
the **upper efficiency limit** for any engine operating between two temperature reservoirs.

- **Engineering use:** a benchmark for heat engines, power cycles, refrigeration cycles, heat pumps and
  second-law performance limits.
- **What controls it:** Carnot efficiency depends **only on the absolute hot- and cold-reservoir
  temperatures**.
- **Practical check:** real equipment cannot reach Carnot efficiency because finite heat-transfer rates,
  friction, pressure loss, leakage and non-ideal components create irreversibility.

[def] It is a theoretical heat-engine cycle made of **four internally reversible processes**. ·HE s17

[hist ·HE s17] Named after **Sadi Carnot**, whose work established a theoretical limit for converting
heat into mechanical work. *(HE gives no dates — which avoids the error at ·EPC s68, where they are
printed as 1769–1832 instead of 1796–1832. See `03b` §3b.8, V10.)*

> **The core engineering idea** ·HE s17 — *"A real engine can be well-designed and still be far below
> Carnot efficiency because real heat transfer and real components generate entropy."* And: in the
> Carnot cycle *"all processes are reversible, no entropy is generated, and the only performance limit
> comes from the hot and cold reservoir temperatures."*

[fig ·HE s16] **Carnot Cycle Overview** — a block diagram. A red *Hot Reservoir ($T_H$)* bar at the top
sends a red arrow $Q_H$ (*Heat Input*) down into a dark *Carnot Engine* block, annotated *"Ideal
reversible heat engine"*. A green arrow leaves to the right as $W_{net}$ (*Useful Work*); a blue arrow
$Q_C$ (*Heat Rejected*) goes down into a blue *Cold Reservoir ($T_C$)* bar.

### The four processes ·HE s19

| Process | What happens |
|---|---|
| **1→2 Isothermal expansion at $T_H$** | The fluid absorbs $Q_H$ from the hot reservoir while remaining at $T_H$, expands and performs work. For an ideal gas, internal energy depends only on temperature, **so the heat added is converted into boundary work**. |
| **2→3 Adiabatic expansion** | No heat crosses the boundary. The fluid continues expanding and doing work; temperature drops from $T_H$ to $T_C$. **Also isentropic**, because reversible and adiabatic. |
| **3→4 Isothermal compression at $T_C$** | The fluid rejects $Q_C$ to the cold reservoir while remaining at $T_C$. Work is done on the fluid, but **at a lower pressure level than the expansion**, so the cycle still produces net work overall. |
| **4→1 Adiabatic compression** | No heat transfer; temperature rises from $T_C$ back to $T_H$. **Also isentropic.** The system returns to its initial state. |

> **The sentence that explains why a Carnot engine works at all** ·HE s19 — the compression happens *"at
> a lower pressure level than the expansion"*. Both isothermals involve work, but the expansion is done
> against higher pressure than the compression is done at, so the areas do not cancel. That is what the
> enclosed area on the $P$–$V$ diagram represents.

[fig ·HE s18] **Carnot Cycle $P$–$V$ Diagram.** Axes *Pressure, P* (vertical) and *Volume, V*
(horizontal). Four circled states: **1** upper left, **2** upper right (labelled $T_H$), **3** lower
right (labelled $T_C$), **4** lower left. Legs, all curved: **1→2 Isothermal Expansion** (red, arrow
rightward); **2→3 Adiabatic Expansion** (blue, arrow down-right); **3→4 Isothermal Compression** (blue,
arrow leftward); **4→1 Adiabatic Compression** (red, arrow upward). The enclosed area is shaded pale
blue and labelled **Net Work Output**. Circulation is **clockwise** — correct for a power cycle.

### The process table ·HE s20

| Process | Type | Heat transfer | Work interaction | Temperature behaviour | Entropy behaviour |
|---|---|---|---|---|---|
| **1→2** | Isothermal expansion | Heat added, $Q_H$ | Work produced by expansion | Constant at $T_H$ | **Entropy increases** |
| **2→3** | Reversible adiabatic expansion | No heat transfer | Work produced by expansion | Drops from $T_H$ to $T$ ⚠ | **Entropy remains constant** |
| **3→4** | Isothermal compression | Heat rejected, $Q_C$ | Work input to compress fluid | Constant at $T_C$ | **Entropy decreases** |
| **4→1** | Reversible adiabatic compression | No heat transfer | Work input to compress fluid | Rises from $T_C$ to $T$ ⚠ | **Entropy remains constant** |

*[added] ✓ **The entropy column is correct on all four rows** — increases, constant, decreases,
constant. Checked against $dS = \delta Q_{rev}/T$: heat in at constant $T$ raises $s$; reversible
adiabatic means $\delta Q = 0$ so $s$ is constant; heat out at constant $T$ lowers $s$. This table is
the clearest statement of Carnot entropy behaviour in the course.*

> ⚠ VERIFY **V26** ·HE s20 — **two cells have truncated subscripts.** Row 2→3 reads *"Drops from $T_H$
> to $T$"* and row 4→1 reads *"Rises from $T_C$ to $T$"*. They should read **"to $T_C$"** and **"to
> $T_H$"** respectively. The bare "$T$" is undefined. The correct temperatures are given on ·HE s19 and
> in the $T$–$s$ diagram on ·HE s28, so the intent is unambiguous — but as printed the table's
> temperature column does not close the cycle. See `_verification-log.md`.

---

## 5.7 Why the Carnot cycle matters ·HE s21

Engineers do not design machines to physically follow a perfect Carnot cycle. They use it as a
**limiting case** answering one question: *how much work could a heat engine possibly produce between
two temperature levels if all losses were removed?* ·HE s21

- It gives the **upper thermal-efficiency limit** between $T_H$ and $T_C$.
- It explains **why raising the hot side or lowering the cold side improves theoretical efficiency**.
- It lets real cycles — Rankine, Brayton, Otto, Diesel, vapour-compression — be **compared against a
  reversible benchmark**.
- It reinforces **why waste heat is unavoidable** in a cyclic heat engine.

---

## 5.8 The reversed Carnot cycle ·HE s22–s23

The same ideal processes can be run in reverse. A **forward** Carnot cycle produces net work by
receiving heat from a hot reservoir and rejecting heat to a cold one. A **reversed** Carnot cycle
**requires net work input** to move heat from a cold region to a warmer one. ·HE s22

This reversed direction is the **ideal model behind refrigerators and heat pumps**. Instead of thermal
efficiency, engineers use the **coefficient of performance (COP)**. The reversed Carnot cycle gives the
**best possible COP** between two reservoirs, just as the forward cycle gives the best possible
heat-engine efficiency. ·HE s22

| Cycle direction | Energy objective | Work interaction | Common engineering interpretation |
|---|---|---|---|
| **Forward Carnot cycle** | Convert part of heat input into work | Net work **output** | Ideal heat engine |
| **Reversed Carnot cycle** | Move heat from cold to hot | Net work **input** | Ideal refrigerator or heat pump |

·HE s23

> **HE gives no COP formula.** It states the concept and stops. The expressions —
> $\mathrm{COP}_{R,rev} = T_C/(T_H - T_C)$ and $\mathrm{COP}_{HP,rev} = T_H/(T_H - T_C)$, together with
> $\mathrm{COP}_{HP} = \mathrm{COP}_R + 1$ — are in **`03b-second-law-and-cycles` §3b.10**, from
> ·EPC s77. Use those.

---

## 5.9 What controls Carnot performance ·HE s24–s25

Carnot cycle performance is controlled by **reservoir temperatures, reversibility, and the direction of
heat and work interactions**. The most important practical lesson: **temperature levels matter more than
the amount of working fluid or the mechanical layout**. ·HE s24

| Factor | Why it matters | Engineering implication |
|---|---|---|
| **Hot-reservoir temperature, $T$** ⚠ | A higher $T_H$ increases the theoretical fraction of heat input that can become work. | Gas turbines, boilers and engines benefit from higher allowable operating temperatures, but **materials and emissions often limit the hot side**. |
| **Cold-reservoir temperature, $T_C$** | A lower $T_C$ reduces the required heat-rejection temperature and improves the theoretical efficiency limit. | Condensers, cooling towers, ambient air, river water or seawater strongly affect actual plant efficiency. |
| **Reversibility** | The Carnot limit assumes **no entropy generation** from friction, turbulence, mixing or finite-temperature heat transfer. | Real equipment always departs from the ideal, so Carnot efficiency is **an upper bound, not a target operating value**. |
| **Heat-transfer temperature difference** | Perfectly reversible heat transfer requires an **infinitesimal** temperature difference. | Real heat exchangers need finite $\Delta T$ to transfer heat at useful rates, **which creates irreversibility**. |
| **Cycle direction** | The same ideal processes run forward as a heat engine or reversed as a refrigerator/heat pump. | Clockwise diagrams **usually** represent net work output; reversed cycles require net work input to move heat from cold to hot. |

> ⚠ VERIFY **C27** ·HE s25 — the first row's label reads *"Hot-reservoir temperature, $T$"* with the
> **$H$ subscript dropped**, while the row directly below correctly reads *"Cold-reservoir temperature,
> $T_C$"*. Same truncation class as V26. Cosmetic — the row body uses $T_H$ correctly.

> **Row 4 is the deepest idea in the deck.** Reversible heat transfer needs an infinitesimal $\Delta T$,
> but an infinitesimal $\Delta T$ transfers heat infinitely slowly. **A truly reversible engine would
> produce zero power.** That is why Carnot efficiency is unreachable in principle, not merely in
> practice — and it connects to ·EPC s67's "20.000…1 °C" reservoir (see `03b` §3b.2).

---

## 5.10 Why Carnot efficiency depends only on temperature ·HE s27

[derivation] ·HE s27

Thermal efficiency is the ratio of net work output to heat input; for a complete cycle the net work
output equals heat added minus heat rejected:

$$\eta = \frac{W_{net}}{Q_H} = \frac{Q_H - Q_C}{Q_H} = 1 - \frac{Q_C}{Q_H}$$

[eq: carnot-heat-ratio] For a **reversible** Carnot cycle, the heat-transfer ratio equals the absolute
temperature ratio:

$$\boxed{\;\frac{Q_C}{Q_H} = \frac{T_C}{T_H}\;}$$

Substituting gives the Carnot efficiency expression. ·HE s27

*[added] The slide says in words that substituting "gives the Carnot efficiency expression" but **does
not print it**. Carrying the substitution through:*

$$\eta = 1 - \frac{Q_C}{Q_H} \;=\; \boxed{\;1 - \frac{T_C}{T_H}\;}$$

*The formula itself is printed on ·HE s10 and ·HE s26.*

> **The conclusion HE draws** ·HE s27 — *"That is why **no details about engine size, piston geometry,
> working-fluid mass, or mechanical layout** appear in the final ideal efficiency equation."*
>
> This is the same result derived at length in `03b` §3b.9 from Carnot's principles and Kelvin's
> absolute scale (·EPC s74–s76). **HE gives the short version; EPC gives the justification.** If a
> question asks *why* $Q_C/Q_H = T_C/T_H$, the answer is in `03b`, not here.

---

## 5.11 The $T$–$s$ rectangle — and the course's only entropy equations ·HE s28

[fig ·HE s28] **Carnot Cycle $T$–$s$ Diagram.** Axes *Temperature, T* (vertical) and *Entropy, s*
(horizontal), with dotted guides at $T_H$ and $T_C$. Four circled states: **1** upper left, **2** upper
right, **3** lower right, **4** lower left.

- **1→2 Isothermal Heat Addition at $T_H$** — the **top horizontal** line, red, arrow rightward,
  labelled $Q_H$.
- **2→3 Isentropic Expansion** — the **right vertical** line, blue, arrow downward.
- **3→4 Isothermal Heat Rejection at $T_C$** — the **bottom horizontal** line, blue, arrow leftward,
  labelled $Q_C$.
- **4→1 Isentropic Compression** — the **left vertical** line, red, arrow upward.

The enclosed rectangle is shaded and labelled **Net Work $= Q_H - Q_C$**.

**On a $T$–$s$ diagram the ideal Carnot cycle forms a rectangle.** The top line represents heat addition
at $T_H$, the bottom line heat rejection at $T_C$, and **the vertical lines are isentropic processes**.
·HE s28

> **How to read it** ·HE s28 — *"For an internally reversible process, heat transfer can be represented
> on a $T$–$s$ diagram. In the Carnot cycle, the entropy change during heat addition and heat rejection
> **has the same magnitude**, so the diagram becomes a rectangle."*

[eq: carnot-entropy] **The only entropy equations in MEC 3105** ·HE s28

$$\boxed{\;Q_H = T_H\,\Delta s\;}\qquad\boxed{\;Q_C = T_C\,\Delta s\;}$$

$$\boxed{\;W_{net} = Q_H - Q_C = \left(T_H - T_C\right)\Delta s\;}$$

> ### Why these three equations matter more than they look
>
> **EPC contains no entropy equation. TC contains none.** These are the only ones in the course, and
> they are enough to **derive** Carnot efficiency instead of asserting it:
>
> $$\eta_{Carnot} = \frac{W_{net}}{Q_H} = \frac{(T_H - T_C)\,\Delta s}{T_H\,\Delta s}
> = \frac{T_H - T_C}{T_H} = 1 - \frac{T_C}{T_H}$$
>
> *[added] ✓ Verified — $\Delta s$ cancels exactly, which is the algebraic reason the working fluid and
> the machine size drop out of the answer (§5.10). It also shows immediately why the two isotherms span
> the **same** $\Delta s$: they must, or the cycle would not close.*
>
> **This derivation is the single most useful thing in HE** and it is not written out on the slide —
> only the ingredients are. Marked `[added]`.
>
> **What is still missing:** these are Carnot-**specific**. There is no general definition
> ($dS = \delta Q_{rev}/T$), no Clausius inequality, no entropy generation term, and no $T\,ds$
> relation anywhere in the course. See `00-index.md` § Gap map.

---

## 5.12 Carnot cycle analysis workflow ·HE s29–s30

**The workflow** ·HE s29 — use when reviewing a Carnot problem, comparing an ideal engine to a real
cycle, or checking whether a proposed efficiency claim is thermodynamically reasonable:

> Define the two reservoirs → **convert both temperatures to an absolute scale** → identify the cycle
> direction → calculate the ideal Carnot limit → compare against the real equipment efficiency.
> **If the real efficiency exceeds the Carnot limit, the inputs, units, or interpretation are wrong.**

The checks table: ·HE s30

| Check or decision | What to look for | Why it matters |
|---|---|---|
| **Temperature basis** | Use **Kelvin or Rankine** for both $T_H$ and $T_C$. | Carnot efficiency is a ratio of absolute temperatures; non-absolute units distort the result. |
| **Reservoir definition** | Confirm the hot and cold reservoirs are the **actual** heat-addition and heat-rejection temperature levels. | Using flame temperature, room temperature, or working-fluid temperature at the wrong state can overstate or understate the limit. |
| **Cycle direction** | Check whether the diagram is a heat engine or a reversed cycle. | A forward Carnot cycle produces net work; a reversed Carnot cycle requires work input **for refrigeration or heat pumping**. |
| **Realistic comparison** | Compare actual equipment efficiency to the **Carnot limit, not to 100 %**. | A low-looking real efficiency may be reasonable if the reservoir temperature difference gives a modest theoretical limit. |
| **Loss mechanism review** | Friction, pressure drop, heat leakage, non-isothermal heat transfer, finite-rate processes. | These are the practical reasons real engines fall below the ideal reversible benchmark. |

> ### This is the exam procedure, and it matches EPC's three inventor-claim examples exactly
>
> ·EPC s80, s81 and s82 (see `03b` §3b.10) are all instances of this workflow: convert to kelvin,
> compute the reversible limit, compare, conclude. **HE gives the method; EPC gives the worked
> instances.** Read them together.
>
> The "reservoir definition" row is a subtler trap than the unit one: the reservoirs are the
> temperatures at which heat is **actually** added and rejected, not the flame temperature or the
> ambient.

---

### Cross-references

- **`03b-second-law-and-cycles` is authoritative** for the second law, heat engines, efficiency, COP and
  the Carnot principles, and holds **all nine worked numerical examples**. This file adds the Carnot
  efficiency formula, the correct diagrams, and the entropy relations.
- Absolute temperature, and why Celsius fails in a ratio → **01-temperature-thermometry** §1.6–1.7.
- $W_{net} = Q_{in} - Q_{out}$ over a cycle → **02-first-law** §2.5.
- Cycle selection, deviations and common mistakes → **04-thermodynamic-cycles** §4.8–4.10.
- COP formulas for the reversed Carnot cycle → **03b** §3b.10.

- The heat-engine framing of §5.1 and the named cycles of §5.4 are what
  **exercises/ga2-topic1-part2-first-law** Part A Q2 and Q5 reach for; the Rankine scale named in §5.3
  is the one **exercises/ga1-topic1-part1-equations-of-state** asks four groups to convert into.

### Verification notes for this section

**Method.** All 30 slides covered. Every slide **containing an embedded image or a typeset equation** was
read from a **170 dpi render** — confirmed by enumerating the PDF's image XObjects, which occur on
exactly slides **2, 8, 9, 10, 16, 18, 26, 27 and 28**; all nine were opened and read, plus the native
table on s20. The remaining 20 slides carry **no embedded images** and are native text or native
PowerPoint tables, extracted in full and cross-read. So no figure or equation in this deck is described
without having been looked at.

**There is no arithmetic in HE** — no worked example, no substituted number. Every *relation* was checked
instead: the efficiency identity (s9), the Carnot derivation (s27), the entropy relations and the
efficiency they imply (s28), and the entropy column of the four-process table (s20). **All correct.**

| ID | Slide | Class | Summary |
|---|---|---|---|
| **V24** | s2 | substantive | $p$–$V$ inset labels **two states "4"**; the lower-right should be **3** |
| **V25** | s2 | substantive | $T$–$s$ inset draws the isotherms **slanted**, so the cycle is a parallelogram; contradicts s28's correct rectangle |
| **V26** | s20 | substantive | two cells truncate the subscript — "Drops from $T_H$ to $T$", "Rises from $T_C$ to $T$" |
| **V27** | s2 | substantive | $T$–$s$ inset arrows converge on state 4; loop not traversable |
| **C27** | s25 | cosmetic | "Hot-reservoir temperature, $T$" — $H$ subscript dropped |
| **C28** | deck-wide | cosmetic | HE uses $Q_C$/$T_C$ where EPC uses $Q_L$/$T_L$ — consistent internally, inconsistent with `03b` |

**Verified sound, no flag:**

- $W_{out} = Q_H - Q_C$ and $\eta = 1 - Q_C/Q_H$ (s9) ✓ — agree with ·EPC s50 and ·TC s18
- $\eta_{Carnot} = 1 - T_C/T_H$ (s10, s26) ✓ — printed twice, both times with the absolute-temperature warning
- $Q_C/Q_H = T_C/T_H$ (s27) ✓ — agrees with ·EPC s76
- The full Carnot derivation (s27) ✓ — algebra correct at every step
- $Q_H = T_H\Delta s$, $Q_C = T_C\Delta s$, $W = (T_H-T_C)\Delta s$ (s28) ✓ — mutually consistent, and they reproduce $\eta_{Carnot}$ exactly
- The **$P$–$V$ diagram (s18)** ✓ and the **$T$–$s$ rectangle (s28)** ✓ — both correct, both consistent with each other and with the s19/s20 process descriptions
- The four-process descriptions (s19) and the process table (s20) ✓ — including all four entropy cells
- The **Carnot Cycle Overview** block diagram (s16) ✓
- All five factor/checklist tables (s7, s14, s25, s23, s30) ✓ — no defects
- HE's symbol glossary (s8) ✓ — **cleaner than TC's**, which mixes energy and power units (V22)
- No dates given for Carnot, so ·EPC s68's 1769/1796 error is not repeated here ✓

**Gap-map consequences of this build — the course is now fully mapped:**

| Row | Final verdict across all five documents |
|---|---|
| **Otto / Diesel / Brayton / Rankine / Stirling efficiency** | ❌ **CONFIRMED ABSENT.** Named in ·TC s13 and tabulated in ·HE s12; **analysed nowhere**. Supplied `[added]`. |
| **Entropy** | ⚠ **PARTIAL.** No general definition anywhere. ·HE s28 supplies the **Carnot-specific** relations $Q = T\Delta s$ — the only entropy equations in the course. |
| **$T$–$s$ diagram** | ✅ **HE is authoritative** — s28's rectangle is the only correct one in the course. |
| **Carnot efficiency formula** | ✅ **HE (s10, s26)**, with the absolute-temperature warning. EPC ·s75 also gives it. |
| **Unit traps / Celsius-vs-kelvin** | ✅ **HE is authoritative** — stated on s10, s26, s14 and s30. |
| **COP formulas** | ✅ **`03b` §3b.10** (from EPC). HE describes COP but writes no formula. |
| **Worked numerical examples** | ✅ **`03b` only** — nine of them. TC and HE have none. |
| **Steady-flow energy equation** | ❌ **still absent from all five decks.** Assessed in GA2 — must be supplied at Stage 1c. |
| **Van der Waals** | ❌ **still absent from all five decks.** Assessed in GA1 — supplied `[added]` in `02-first-law` §2.12. |

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
