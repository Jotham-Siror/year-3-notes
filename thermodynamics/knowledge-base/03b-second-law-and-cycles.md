---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "03b — The Second Law, Heat Engines, Carnot and the Diesel Cycle"
source: "EPC — '3.02 - Energy Equations and Phase Changes.pdf', slides 22–92 of 92"
slides: "22-92"
file_role: topic
subtopics:
  - "why a second law is needed; direction and spontaneity"
  - "reversible and irreversible processes; quasi-static processes; irreversibilities"
  - "thermal energy reservoirs, work reservoirs, thermodynamic cycles"
  - "heat engines; the steam power plant; thermal efficiency"
  - "the Kelvin-Planck statement"
  - "refrigerators and heat pumps; coefficient of performance"
  - "the Clausius statement; equivalence of the two statements; perpetual-motion machines"
  - "the Carnot cycle and its four processes; Carnot principles"
  - "the absolute (Kelvin) temperature scale; Carnot efficiency"
  - "reversed Carnot device; maximum COP"
  - "quality of energy"
  - "the Diesel cycle"
key_equations: [thermal-efficiency, kelvin-planck, cop-refrigerator, cop-heatpump, cop-relation, clausius, carnot-efficiency, absolute-scale, carnot-cop, eer]
prerequisites: ["01-temperature-thermometry", "02-first-law", "03a-phase-behaviour-and-equilibrium"]
leads_to: ["04-thermodynamic-cycles", "05-heat-engines-and-carnot"]
verification_flags: 11
tags: [second-law, entropy, kelvin-planck, clausius, heat-engine, thermal-efficiency, refrigerator, heat-pump, cop, carnot, reversibility, absolute-temperature, diesel-cycle, perpetual-motion]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered slide · [hist] historical/biographical note ·
  [added] supplied here, NOT in the source ·
  ·EPC sN = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md. -->

# 03b — The Second Law, Heat Engines, Carnot and the Diesel Cycle

Scope: EPC slides 22–92. **This is the quantitative spine of the whole subject** — the only document
in the set with worked numerical examples, and the file that `04-` and `05-` will reference rather than
repeat (see `00-index.md` § Overlap map).

Sourced largely from **Çengel & Boles, *Thermodynamics: An Engineering Approach*, 8th ed. (SI)**,
credited on ·EPC s22.

> ### ✅ Every number in this document is correct
>
> **Nine worked examples, a five-row efficiency table and several unit conversions — all recomputed
> independently, all correct.** That is worth stating plainly, because `02-first-law.md` is not in that
> position: FL's single worked example is wrong by a factor of five (V8). **Trust EPC's arithmetic.**
> Its eleven flags are all in wording, figures, a date, and one derivation step — never in a result.

> ### ⚠ What is NOT here
>
> **There is no entropy equation anywhere in EPC.** No Clausius inequality, no $S_{\text{gen}}$, no
> $dS \ge \delta Q/T$, no $\Delta S_{\text{univ}}$. Entropy appears **once**, qualitatively, on ·EPC s27.
> The $T$–$s$ diagram appears only as an imported Diesel-cycle figure (·EPC s92). Since the gap map
> lists entropy as absent from the whole course, **it must be supplied from outside if a question
> demands it.**

---

## 3b.1 Why a second law is needed ·EPC s23–s30, s39–s40

[def] The **spontaneous** direction of change is the direction that does not require work to be done to
bring the change about. ·EPC s23

EPC's three examples of spontaneity: a gas expands to fill the available volume; a hot body cools to
the temperature of its surroundings; a chemical reaction runs in one direction rather than another.
·EPC s23

> ⚠ VERIFY **V15** ·EPC s23 — the slide, titled *"Second law of Thermodynamics"*, ends with
> *"Internal energy lets us access whether a change is permissible. Only those changes occurs for which
> the internal energy of an isolated system remains constant."* That criterion —
> $\Delta U_{\text{isolated}} = 0$ — **is the first law, not the second**, and the slide does not say
> so. EPC s39 confirms it ("The first law of thermodynamics gives no information about direction").
> A student revising from s23 alone would attribute $\Delta U = 0$ to the second law. (Also: *access*
> → *assess*; *changes occurs* → *changes occur*.) See `_verification-log.md`.

[def] **The second law, as EPC first states it** ·EPC s25

> **"No process is possible in which the sole result is the absorption of heat from a reservoir and its
> complete conversion into work."**

[fig ·EPC s25] A "Hot source" block; a thick arrow labelled *Heat* / *Flow of energy* runs down into a
grey disc labelled *Engine* and turns to exit horizontally as *Work*. **There is no cold reservoir and
no rejected-heat arrow** — the figure depicts the forbidden 100 %-conversion device.

**Is it internal energy that tends to a minimum?** ·EPC s24 — EPC tests and rejects that idea:

$$dU < 0\ \text{(system)},\qquad dU > 0\ \text{(surroundings)},\qquad dU = 0\ \text{(perfect gas into vacuum)}$$

A perfect gas expands spontaneously into a vacuum with $dU = 0$ — so a **spontaneous process need not
lower the internal energy**. Energy alone cannot supply direction.

[def] **Entropy** is a measure of randomness/disorder. **The total entropy of the system and its
surroundings increases in the course of a spontaneous change.** ·EPC s27

[fig ·EPC s27] Two boxes: spheres clustered in one corner (top), spread uniformly (bottom), with a
downward arrow labelled *Spontaneous* and an upward arrow labelled *Non-spontaneous* between them.

**The directional statement** ·EPC s28

> "The second law of thermodynamics states that **processes occur in a certain direction, not in just
> any direction.**"

Physical processes proceed toward equilibrium spontaneously: water flows down a waterfall; gases expand
from high to low pressure; heat flows from high to low temperature. ·EPC s28

**Reversal costs something** ·EPC s29 — a spontaneous process can be reversed, but not
spontaneously: *"Some external inputs, energy, must be expended to reverse the process."* The example is a cup of hot coffee
in a cooler room. The reverse — coffee spontaneously getting hotter — **would not violate the first
law**, provided the air lost what the coffee gained; it simply never happens.

[ex ·EPC s30] **Heating a room with a resistor.** The first law dictates that the electrical energy
supplied to the resistance wires equals the energy transferred to the room air as heat. Reverse it:
transferring heat to the wires does **not** generate an equivalent amount of electrical energy.
Figure annotation: $I = 0$.

*[added] This example is entirely qualitative — there is nothing to compute. The forward balance
$\dot W_{\text{elec,in}} = \dot Q_{\text{to air}}$ is correct at steady state, and $I = 0$ correctly
expresses that heating the wire produces no current.*

**The summary** ·EPC s39–s40

- The first law gives **no information about direction**; it says only that identical quantities of
  energy are involved, regardless of the feasibility of the process.
- Joule's experiments showed that heat **could not be completely converted into work**, whereas work
  **can** be completely converted into heat.
- Heat and work are therefore **not completely interchangeable**, and energy transfer often involves
  **degradation into a less useful form**.
- **A process will not occur unless it satisfies both the first and the second laws.**

[fig ·EPC s40] Çengel Figure 6–5 — a process arrow must pass through two gates in series, labelled
*1st law* and *2nd law*.

---

## 3b.2 Reversible and irreversible processes ·EPC s31–s38, s65–s67

[def] A **reversible process** can be reversed without leaving any trace on the surroundings — both the
system **and** the surroundings return to their initial states. This is possible only if the net heat
and net work exchange for the combined (original and reverse) process is **zero**. ·EPC s65

Reversible processes **do not occur in nature**; they are idealisations, approachable but never
achievable. ·EPC s31, s66

**Why engineers care** ·EPC s66 — work-**producing** devices (engines, turbines) **deliver the most
work**, and work-**consuming** devices (compressors, fans, pumps) **consume the least work**, when the
processes are reversible. Reversibility is the benchmark, not a design target.

[def] **Irreversibilities** — the factors that make a process irreversible. EPC's list: ·EPC s66, s36

- friction
- unrestrained expansion of gases
- heat transfer through a finite temperature difference
- mixing of two different substances
- hysteresis effects
- $I^2R$ losses in electrical circuits
- any deviation from a quasi-static process

*(·EPC s36 gives a shorter version: relative motion with friction, throttling, heat transfer,
diffusion, electricity flow through a resistance.)*

[def] **Internally reversible** — no irreversibilities occur *within* the system boundary.
**Externally reversible** — none occur *outside* it; heat transfer between a reservoir and a system is
externally reversible if the outer surface of the system is at the reservoir temperature.
**Totally reversible** (or simply reversible) — no irreversibilities within the system **or** its
surroundings. ·EPC s67

[fig ·EPC s67] Two piston-cylinders at 20 °C: (a) *totally reversible*, its reservoir at
"20.000…1 °C" — infinitesimally above, so the heat transfer is across a vanishing $\Delta T$;
(b) *internally reversible*, reservoir at 30 °C, boundary at 20 °C — the finite $\Delta T$ makes it
externally irreversible.

[def] **Quasi-static (quasi-equilibrium) process** — at every instant the system's deviation from
thermodynamic equilibrium is infinitesimal, so each state may be treated as an equilibrium state.
·EPC s38

[fig ·EPC s37] Hand-drawn four-panel sketch: a piston-cylinder with **stops** at the top, the piston
carrying a stack of weights that reduces 4 → 3 → 2 → 0 as the piston rises to the stops. States
labelled $P_i, v_i$ (initial) → intermediate → $P_2, v_2$ (final), with handwritten increments.

> ⚠ VERIFY **V14** ·EPC s37 — two problems in the handwritten increments.
> **(a)** The second panel writes $v_i' = v_i + dp$ — incrementing a **volume** by a **pressure**
> differential. Dimensionally impossible, and the third panel writes the same relation correctly as
> $v_i'' = v_i' + dv$.
> **(b)** Both panels write $P' = P + dp$, i.e. pressure **increasing**, alongside volume increasing.
> **Count the weights** — 4 → 3 → 2 → 0 as the piston rises. Removing weight *lowers* the pressure. $P$
> and $v$ cannot both increase under progressive weight removal. Should be $P' = P - dp$, or $dp$ must
> be declared a signed (negative) increment. See `_verification-log.md`.

---

## 3b.3 Reservoirs, cycles and heat engines ·EPC s41–s46

[def] **Heat (thermal) reservoir** — a system large enough in stable equilibrium that finite amounts of
heat can be transferred to or from it **without any change in its temperature**. ·EPC s41

- a high-temperature reservoir **from** which heat is transferred is a **heat source**;
- a low-temperature reservoir **to** which heat is transferred is a **heat sink**. ·EPC s41

[fig ·EPC s41] Çengel Fig. 6–6 — atmosphere, river, lake and ocean as bodies with large thermal
masses; Fig. 6–7 — a source cloud emitting heat, a sink cloud absorbing it.

[def] **Work reservoir** — a system large enough in stable equilibrium that finite amounts of work can
be transferred **adiabatically** to or from it without any change in its pressure. ·EPC s42

[def] **Thermodynamic cycle** — a system has completed a cycle when it undergoes a series of processes
and returns to its original state, so that its properties at the end equal those at the beginning:
·EPC s42

$$P_f = P_i,\quad T_f = T_i,\quad u_f = u_i,\quad v_f = v_i,\ \text{etc.}$$

[def] **Heat engine** — a thermodynamic system operating in a thermodynamic cycle **to which net heat
is transferred and from which net work is delivered**. ·EPC s42

**The asymmetry that motivates the whole topic** ·EPC s43: work can be converted to heat **directly and
completely**, but converting heat to work **requires special devices**. Stirring water with a paddle
raises its temperature; heating the water does not turn the paddle.

**The four characteristics of every heat engine** ·EPC s44

1. They receive heat from a **high-temperature source** (solar energy, oil furnace, nuclear reactor…).
2. They convert **part** of this heat to work (usually a rotating shaft).
3. They **reject the remaining waste heat** to a low-temperature sink (the atmosphere, rivers…).
4. They **operate on a cycle**.

[def] The fluid to and from which heat is transferred is the **working fluid**. ·EPC s44

[fig ·EPC s45] The steam power plant, the device that best fits the definition — an
**external-combustion engine**. Boiler ($Q_{in}$ from a furnace) → turbine ($W_{out}$) → condenser
($Q_{out}$ to the atmosphere or a river) → pump ($W_{in}$) → back to the boiler, all inside a marked
system boundary.

[def] **Turbine** — a rotary steady-state steady-flow machine whose purpose is the production of shaft
power **at the expense of the pressure of the working fluid**. Changes in potential energy and inlet
kinetic energy are usually negligible; the process is normally **adiabatic**, so the work output
reduces to the **decrease in enthalpy** from inlet to exit. ·EPC s46

*[added] EPC states that last result in words only. In symbols it is $w = h_1 - h_2$ — which is where
`02-first-law.md` §2.7's enthalpy is used, and the reason $h$ rather than $u$ appears in flow-device
analysis.*

---

## 3b.4 Thermal efficiency ·EPC s47–s50

[def] **Thermal efficiency** is the index of performance of a work-producing device: the ratio of the
net work output (the desired result) to the heat input (the cost of obtaining it). ·EPC s47

$$\eta_{th} = \frac{\text{Desired Result}}{\text{Required Input}}$$

$$W_{net,out} = W_{out} - W_{in}\quad(\mathrm{kJ}) \qquad
W_{net,out} = Q_{in} - Q_{out}\quad(\mathrm{kJ})$$

[derivation] For a closed system undergoing a cycle, $\Delta U = 0$, so ·EPC s48

$$Q_{net,in} - W_{net,out} = \underbrace{\Delta U}_{=\,0\ \text{(cyclic)}}
\qquad\Longrightarrow\qquad \boxed{\;W_{net,out} = Q_{net,in}\;}$$

[eq: thermal-efficiency] ·EPC s48–s50

$$\boxed{\;\eta_{th} = \frac{W_{net,out}}{Q_{in}}
= \frac{Q_{in}-Q_{out}}{Q_{in}} = 1 - \frac{Q_{out}}{Q_{in}}
= 1 - \frac{Q_L}{Q_H}\;}$$

- $Q_H$ — magnitude of heat transfer with the high-temperature medium at $T_H$, J
- $Q_L$ — magnitude of heat transfer with the low-temperature medium at $T_L$, J
- $W_{net,out}$ — net work delivered per cycle, J

**On the subscripts** ·EPC s48 — *"the use of the* in *and* out *subscripts means to use the magnitude
(take the positive value) of either the work or heat transfer and let the minus sign in the net
expression take care of the direction."*

> **This is EPC's answer to the FL sign-convention mess.** By using magnitudes with directional
> subscripts, EPC sidesteps the $\pm W$ problem entirely. `_nomenclature.md` clash 1 does **not** apply
> to this file — every $Q$ and $W$ here is a positive magnitude. Adopt this style in exam work.

·EPC s48 also prints the caution $Q_{in} \neq Q_{net}$ — a deliberate warning (verified, it really is a
"not equal") that $\eta_{th}$ divides by the heat **input**, not the net heat.

**$Q_{out}$ is never zero**, so the net work output is always less than the heat input, and
$\eta_{th} < 1$ always. ·EPC s47–s48

[ex ·EPC s50] **Example 6-1.** A steam power plant produces 50 MW of net work while burning fuel to
produce 150 MW of heat at the high temperature. Find the cycle thermal efficiency and the heat rejected.

$$\eta_{th} = \frac{50\ \mathrm{MW}}{150\ \mathrm{MW}} = 0.333\ (33.3\%)
\qquad Q_L = Q_H - W_{net,out} = 150 - 50 = 100\ \mathrm{MW}$$

*[added] ✓ Verified. Cross-check with the other form: $1 - 100/150 = 0.333$ ✓ self-consistent.*

[ex ·EPC s59] **Çengel Example 6–1.** Heat to an engine from a furnace at 80 MW, waste heat to a river
at 50 MW.
$\dot W_{net,out} = 80 - 50 = 30\ \mathrm{MW}$; $\eta_{th} = 30/80 = 0.375\ (37.5\%)$. *✓ Verified.*

[ex ·EPC s64] **Çengel Example 6–2.** A car engine of 65 hp output at 24 % thermal efficiency; fuel
heating value 19,000 Btu/lbm. Find the fuel consumption rate.

$$\dot Q_H = \frac{65\ \mathrm{hp}}{0.24}\left(\frac{2545\ \mathrm{Btu/h}}{1\ \mathrm{hp}}\right)
= 689{,}270\ \mathrm{Btu/h}
\qquad \dot m = \frac{689{,}270}{19{,}000} = 36.3\ \mathrm{lbm/h}$$

*[added] ✓ Verified: $65/0.24 \times 2545 = 689{,}271$; $/19{,}000 = 36.28$.*

---

## 3b.5 The Kelvin–Planck statement ·EPC s51–s52, s63

[eq: kelvin-planck] ·EPC s51

$$\boxed{\;\text{It is impossible for any device that operates on a cycle to receive heat from a
\textbf{single reservoir} and produce a net amount of work.}\;}$$

Equivalently: **no heat engine can have a thermal efficiency of 100 percent**, $\eta_{th} < 100\%$.
A heat engine must exchange heat with a low-temperature **sink** as well as a high-temperature
**source** to keep operating. ·EPC s51

[fig ·EPC s51] The forbidden engine: a single reservoir supplying $\dot Q_H = 100\ \mathrm{kW}$ to an
engine delivering $\dot W_{net,out} = 100\ \mathrm{kW}$, with $\dot Q_L = 0$ and **no rejection arrow
drawn**. *[added] It satisfies the first law exactly ($100 - 100 - 0 = 0$) and violates the second —
which is the whole point of the figure.*

**Can we save $Q_{out}$?** ·EPC s52 — *"a firm no for the simple reason that without a heat rejection
process in a condenser, the cycle cannot be completed."*

> ⚠ VERIFY **C16** ·EPC s63 — the summary slide restates Kelvin–Planck as *"No cyclic process is
> possible whose sole result is the complete conversion of heat into work"*, dropping the
> **single-reservoir** qualifier that s51 correctly includes. As printed it is the Planck phrasing and
> is defensible, but the single-reservoir condition is the operative restriction — every Carnot engine
> converts *part* of its heat to work. **Quote s51's wording in an exam, not s63's.**

---

## 3b.6 Refrigerators, heat pumps and the COP ·EPC s52–s55, s60–s62

[def] A **heat pump** is a thermodynamic system operating in a cycle that removes heat from a
low-temperature body and delivers heat to a high-temperature body, receiving external energy as work or
heat to do so. A **refrigerator** extracts heat from a low-temperature medium; a **heat pump** rejects
heat to the high-temperature medium. Same device, different objective. ·EPC s52

[def] The most common refrigeration cycle is the **vapour-compression refrigeration cycle**, with four
components: a **compressor**, a **condenser**, an **expansion valve** and an **evaporator**. ·EPC s53

[fig ·EPC s53] The cycle drawn with typical states *(the slide says only "refrigerant" — the fluid is **not** named; these are R-134a-like values)*: condenser exit 800 kPa / 30 °C → expansion
valve → evaporator inlet 120 kPa / −25 °C → (absorbs $Q_L$ from the refrigerated space) → evaporator
exit 120 kPa / −20 °C → compressor ($W_{net,in}$) → 800 kPa / 60 °C → condenser (rejects $Q_H$ to the
kitchen air). *[added] Internally consistent: two states on each pressure level, discharge hotter than
condenser exit, low-side temperatures below the cold space and high-side above the kitchen ✓.*

[def] **Coefficient of performance** — the ratio of desired result to input. **It may be larger than
1**, and larger is better. ·EPC s54

[eq: cop-refrigerator] ·EPC s54–s55

$$\boxed{\;\mathrm{COP}_R = \frac{Q_L}{W_{net,in}} = \frac{Q_L}{Q_H - Q_L}\;}$$

[eq: cop-heatpump] ·EPC s55

$$\boxed{\;\mathrm{COP}_{HP} = \frac{Q_H}{W_{net,in}} = \frac{Q_H}{Q_H - Q_L}\;}$$

[derivation] First law applied to the cyclic refrigerator ·EPC s55:

$$\left(Q_L - Q_H\right) - \left(0 - W_{in}\right) = \Delta U_{cycle} = 0
\qquad\Longrightarrow\qquad W_{in} = W_{net,in} = Q_H - Q_L$$

*[added] This line looks odd but is correct. It is the same template as s48,
$Q_{net,in} - W_{net,out} = \Delta U$, with $Q_{net,in} = Q_L - Q_H$ and
$W_{net,out} = W_{out} - W_{in} = 0 - W_{in}$. Expanding gives $W_{in} = Q_H - Q_L$ ✓. The "$0-$" is
$W_{out} = 0$, not a stray minus sign.*

[eq: cop-relation] ·EPC s55

$$\boxed{\;\mathrm{COP}_{HP} = \mathrm{COP}_R + 1\;}$$

*[added] Verified exactly:
$\dfrac{Q_L}{Q_H-Q_L} + 1 = \dfrac{Q_L + Q_H - Q_L}{Q_H-Q_L} = \dfrac{Q_H}{Q_H-Q_L}$ ✓. Note the
consequence: **a heat pump's COP always exceeds a refrigerator's by exactly 1**, and can therefore
never be less than 1.*

[ex ·EPC s60] **Çengel Example 6–3.** Food compartment at 4 °C, heat removed at 360 kJ/min, power input
2 kW.
$\mathrm{COP}_R = (360/60)/2 = 3$ — 3 kJ removed per kJ of work.
$\dot Q_H = 360 + 2(60) = 480\ \mathrm{kJ/min}$. *✓ Verified.*

[ex ·EPC s61] **Çengel Example 6–4.** House at 20 °C, outdoor air −2 °C, heat loss 80,000 kJ/h,
$\mathrm{COP}_{HP} = 2.5$.
$\dot W_{net,in} = 80{,}000/2.5 = 32{,}000\ \mathrm{kJ/h} = 8.9\ \mathrm{kW}$;
$\dot Q_L = 80{,}000 - 32{,}000 = 48{,}000\ \mathrm{kJ/h}$. *✓ Verified.*

[eq: eer] **Energy efficiency rating** ·EPC s62 — heat removed in Btu per Wh of electricity. Since
$1\ \mathrm{kWh} = 3412\ \mathrm{Btu}$:

$$\boxed{\;\mathrm{EER} = 3.412\,\mathrm{COP}_R\;}$$

**One ton** of heating or cooling $= 12{,}000\ \mathrm{Btu/h} = 211\ \mathrm{kJ/min}$. ·EPC s62
*[added] ✓ Both verified: $3600/1.055056 = 3412$; $12{,}000 \times 1.055056/60 = 211.0$.*

---

## 3b.7 The Clausius statement and equivalence ·EPC s56–s58, s63

[eq: clausius] ·EPC s56

$$\boxed{\;\text{It is impossible to construct a device that operates in a cycle and produces no effect
other than the transfer of heat from a lower-temperature body to a higher-temperature body.}\;}$$

Equivalently $\mathrm{COP} < \infty$: a refrigerator cannot operate unless its compressor is driven by
an external power source. ·EPC s56

[fig ·EPC s56] The forbidden refrigerator: $Q_L = 5\ \mathrm{kJ}$ in from the cold space,
$Q_H = 5\ \mathrm{kJ}$ out to the warm environment, $W_{net,in} = 0$. *[added] Satisfies the first law
($5 = 5 + 0$) and gives $\mathrm{COP}_R = 5/0 \to \infty$, contradicting $\mathrm{COP} < \infty$ ✓.*

[derivation] **Equivalence of the two statements** ·EPC s57–s58. A violation of either implies a
violation of the other:

1. Assume a heat engine with $\eta_{th} = 100\%$ (violating Kelvin–Planck). It converts all of $Q_H$
   into work $W_{net} = Q_H$.
2. Feed that work to a refrigerator, which removes $Q_L$ from the cold reservoir and rejects
   $Q_L + Q_H$ to the hot one.
3. Net effect on the hot reservoir: $-Q_H + (Q_L + Q_H) = +Q_L$.
4. The combination is therefore a device that moves $Q_L$ from cold to hot **with no work input** —
   **a violation of the Clausius statement**.

> ⚠ VERIFY **V16** ·EPC s57–s58 — **two dropped glyphs make this argument unfollowable as printed.**
> On s57 the figure arrow from the refrigerator to the hot reservoir is labelled **"$Q_H + Q$"** — the
> subscript $L$ is clipped off, and a bare "$Q$" is defined nowhere in the deck. On s58 the prose reads
> *"the difference between QL  QH and QH"* — the **"+" is missing** (a blank gap, not a faint plus).
> As printed a student could read $Q_L - Q_H$, which gives the wrong sign. Should be
> $Q_H + Q_L$ and *"the difference between $Q_L + Q_H$ and $Q_H$"*. See `_verification-log.md`.

[def] **Perpetual-motion machines** ·EPC s58

- **PMM1** — a device that violates the **first** law (by *creating* energy).
- **PMM2** — a device that violates the **second** law.

[fig ·EPC s58] Çengel Fig. 6–29 — a steam plant with a boiler, pump and turbine but **no condenser and
no $\dot Q_{out}$**: a PMM2.

---

## 3b.8 The Carnot cycle ·EPC s68–s70

[hist ·EPC s68] French military engineer **Nicolas Sadi Carnot** was among the first to study the
principles of the second law, the first to introduce the concept of cyclic operation, and devised a
reversible cycle composed of four reversible processes — **two isothermal and two adiabatic**.

> ⚠ VERIFY **V10** ·EPC s68 — the slide prints **"Nicolas Sadi Carnot (1769-1832)"**. Sadi Carnot was
> born **1796**, not 1769 — a digit transposition. Confirmed at 4× zoom; the digits are unambiguous.
> As printed he would have been **63** at death and would have published *Réflexions sur la puissance
> motrice du feu* (1824) at **55** rather than 28. *(1769 is close to his father Lazare Carnot's
> era — Lazare was born 1753.)* See `_verification-log.md`.

[def] **The four processes of the Carnot cycle** ·EPC s68

| Process | Description |
|---|---|
| **1–2** | Reversible **isothermal heat addition** at high temperature $T_H$ to the working fluid in a piston-cylinder, which does boundary work |
| **2–3** | Reversible **adiabatic expansion**; the system does work as the temperature falls $T_H \to T_L$ |
| **3–4** | Reversible **isothermal heat rejection** at $T_L$ while work of compression is done on the system |
| **4–1** | Reversible **adiabatic compression**; the temperature rises $T_L \to T_H$ |

[fig ·EPC s69] Four piston-cylinder panels: (a) 1→2 with an energy source at $T_H$ supplying $Q_H$,
head marked "$T_H$ = const."; (b) 2→3 with the head **insulated**, $T_H \to T_L$; (c) 3→4 with an
energy sink at $T_L$ receiving $Q_L$, head marked "$T_L$ = const."; (d) 4→1 **insulated**,
$T_L \to T_H$.

[fig ·EPC s70] Two $P$–$v$ diagrams. **Top — the power cycle:** states 1 (upper left) → 2 along
"$T_H$ = const." → 3 → 4 along "$T_L$ = const." → 1, traversed **clockwise**, enclosed area shaded
$W_{net,out}$, with $Q_H$ entering across the 1–2 isotherm and $Q_L$ leaving across 3–4.

**Bottom — the reversed cycle (refrigerator):** ⚠ **the states are renumbered — 2 and 4 swap places.**
Here 1 is upper left, **2 lower left**, 3 lower right, **4 upper right** on the "$T_H$ = const." curve.
The four arrows run 1→2 down the left curve, 2→3 rightward along the $T_L$ isotherm, 3→4 up the right
curve, 4→1 leftward along the $T_H$ isotherm — a complete **counter-clockwise** loop, exactly as the
slide's text says. The enclosed area is labelled $W_{net,in}$, with $Q_L$ absorbed across the lower
isotherm and $Q_H$ rejected across the upper.

> **Read the lower diagram's own labels, not the upper one's.** The renumbering is easy to miss and
> makes the arrows look inconsistent if you carry the top diagram's numbering down. Both diagrams are
> drawn correctly.

**Power cycles run clockwise on a process diagram; the reversed (refrigeration) cycle runs
counter-clockwise.** ·EPC s70

---

## 3b.9 Carnot principles and the absolute temperature scale ·EPC s71–s76

[def] **The two Carnot principles** ·EPC s71, s73

**(a)** The efficiency of an **irreversible** heat engine is always **less than** the efficiency of a
**reversible** one operating between the same two reservoirs.

$$\eta_{th} < \eta_{th,\,Carnot}$$

**(b)** The efficiencies of **all reversible** heat engines operating between the same two
constant-temperature reservoirs are **the same**.

[fig ·EPC s71] Three engines between the same reservoirs — one irreversible, two reversible — annotated
$\eta_{th,1} < \eta_{th,2}$ and $\eta_{th,2} = \eta_{th,3}$.

[fig ·EPC s72] Çengel Fig. 6–42, the **proof of principle (a)**: assume the irreversible engine is more
efficient, so $Q_{L,irrev} < Q_{L,rev}$; run the reversible engine backwards as a refrigerator driven by
the irreversible engine; the combination becomes a single-reservoir engine delivering
$W_{irrev} - W_{rev}$ while drawing $Q_{L,rev} - Q_{L,irrev}$ from the cold reservoir alone —
**violating Kelvin–Planck**.

[fig ·EPC s73] Two reversible engines between 1000 K and 300 K, both at
$\eta_{th,A} = \eta_{th,B} = 70\%$. *[added] ✓ Verified: $1 - 300/1000 = 0.70$.*

[derivation] **The absolute temperature scale** ·EPC s73–s76. The slide states: *"Lord Kelvin in 1848
used energy as a thermodynamic property to define temperature and devised a temperature scale that is
independent of the thermodynamic substance."* ·EPC s73

*[added] The slide's phrasing is loose — energy does not define temperature. What Kelvin actually used
is **Carnot principle (b)**: because all reversible engines between the same two reservoirs have the
same efficiency, the heat ratio $Q_L/Q_H$ depends on the reservoir temperatures **alone** and on nothing
about the working substance. That ratio is what defines the scale, and ·EPC s76 supplies it.*

$$\eta_{th} = 1 - \frac{Q_L}{Q_H} \qquad\Longrightarrow\qquad
\eta_{th} = g(T_L, T_H) = 1 - f(T_L, T_H)$$

Chaining two engines in series through an intermediate reservoir at $T_2$: ·EPC s75

$$\frac{Q_1}{Q_3} = \frac{Q_1}{Q_2}\,\frac{Q_2}{Q_3}
\qquad\Longrightarrow\qquad f(T_1,T_3) = f(T_1,T_2)\,f(T_2,T_3)$$

which is satisfied by $f(T_a,T_b) = \theta(T_b)/\theta(T_a)$, and **the simplest form of $\theta$ is
the absolute temperature itself**.

[eq: absolute-scale] ·EPC s76

$$\boxed{\;\frac{Q_L}{Q_H} = \frac{T_L}{T_H}\;}\qquad\text{(reversible devices only)}$$

[eq: carnot-efficiency] ·EPC s75

$$\boxed{\;\eta_{th,\,rev} = 1 - \frac{T_L}{T_H}\;}$$

> **⚠ The temperatures must be ABSOLUTE.** EPC says so twice — s75 *"Note that the temperatures are
> absolute temperatures"* and s76 *"where $T_H$ and $T_L$ are the absolute temperatures"* — and
> demonstrates it on s79 by converting 30 °C and 652 °C to kelvins before dividing. Substituting
> Celsius here is a whole-answer error. This is the payoff of `01-temperature-thermometry`.

**The validity limits** ·EPC s76 — this result holds only for heat exchange across an engine operating
between **two constant-temperature reservoirs**. It does **not** apply when the source or sink changes
temperature during the process.

[eq] **The three-way comparison** ·EPC s76

$$\eta_{th} \begin{cases}
< \eta_{th,rev} & \text{irreversible heat engine}\\
= \eta_{th,rev} & \text{reversible heat engine}\\
> \eta_{th,rev} & \textbf{impossible heat engine}
\end{cases}$$

> ⚠ VERIFY **V13** ·EPC s75 — a derivation inconsistency. The slide identifies $f(T_1,T_3)$ with
> $Q_1/Q_3$ (hot-side over cold-side) but then concludes $f(T_1,T_3) = T_3/T_1$, which gives
> $Q_1/Q_3 = T_3/T_1$ — **the inverse of s76's own result** $Q_L/Q_H = T_L/T_H$. Either the chain
> should be written $Q_3/Q_1 = (Q_3/Q_2)(Q_2/Q_1)$, or $f$ should be $\theta(T_1)/\theta(T_3)$.
> **The final result $\eta_{th,rev} = 1 - T_L/T_H$ is correct** — only the intermediate step is
> inverted. See `_verification-log.md`.

---

## 3b.10 The reversed Carnot device ·EPC s77–s79

[eq: carnot-cop] Maximum possible COPs between $T_H$ and $T_L$: ·EPC s77

$$\boxed{\;\mathrm{COP}_{R,\,rev} = \frac{Q_L}{Q_H - Q_L} = \frac{T_L}{T_H - T_L}
= \frac{1}{\dfrac{T_H}{T_L} - 1}\;}$$

$$\boxed{\;\mathrm{COP}_{HP,\,rev} = \frac{Q_H}{Q_H - Q_L} = \frac{T_H}{T_H - T_L}
= \frac{\dfrac{T_H}{T_L}}{\dfrac{T_H}{T_L} - 1}\;}$$

*[added] All four forms verified as identities (divide through by $Q_L$ or $T_L$) ✓. Note
$\mathrm{COP}_{HP,rev} = \mathrm{COP}_{R,rev} + 1$ holds here too ✓.*

$$\mathrm{COP}_R \begin{cases}
< \mathrm{COP}_{R,rev} & \text{irreversible refrigerator}\\
= \mathrm{COP}_{R,rev} & \text{reversible refrigerator}\\
> \mathrm{COP}_{R,rev} & \textbf{impossible refrigerator}
\end{cases}$$

·EPC s78. The same relation holds for heat pumps with $\mathrm{COP}_{HP}$ throughout.

[ex ·EPC s78–s79] **Carnot engine, 652 °C → 30 °C, 500 kJ per cycle.** Find (a) the thermal efficiency
and (b) the heat rejected.

$$\eta_{th,rev} = 1 - \frac{(30+273)\ \mathrm{K}}{(652+273)\ \mathrm{K}} = 0.672\ (67.2\%)$$
$$\frac{Q_L}{Q_H} = \frac{303}{925} = 0.328 \qquad Q_L = 500(0.328) = 164\ \mathrm{kJ}$$

*[added] ✓ Verified: $303/925 = 0.3276$; $1 - 0.3276 = 0.6724$; $500 \times 0.3276 = 163.8 \to 164$ kJ.*

### The three inventor-claim examples — the exam pattern

[ex ·EPC s80] **Example 6-3.** An inventor claims a heat engine of **80 %** thermal efficiency between
**1000 K** and **300 K**. Evaluate the claim.

$$\eta_{th,rev} = 1 - \frac{300\ \mathrm{K}}{1000\ \mathrm{K}} = 0.70\ (70\%)$$

**The claim is false**, since no heat engine may be more efficient than a Carnot engine operating
between the same reservoirs. *[added] ✓ Verified. $80\% > 70\%$.*

[ex ·EPC s81] **Example 6-4.** An inventor claims a refrigerator maintaining **2 °C** in a **25 °C**
room with a **COP of 13.5**. Any truth?

$$\mathrm{COP}_{R,rev} = \frac{T_L}{T_H - T_L} = \frac{(2+273)\ \mathrm{K}}{(25-2)\ \mathrm{K}} = 11.96$$

**The claim is false**, since no refrigerator may have a COP larger than the reversed Carnot device.
*[added] ✓ Verified: $275/23 = 11.957$. $13.5 > 11.96$.*

[ex ·EPC s82–s83] **Example 6-5.** A heat pump heats a building held at **21 °C**, losing heat at
**135,000 kJ/h** when the outside temperature drops to **−5 °C**. Find the **minimum** power required.

The heat lost by the building must be supplied by the heat pump, so $\dot Q_H = \dot Q_{Lost}$:

$$\mathrm{COP}_{HP} = \frac{T_H}{T_H - T_L} = \frac{(21+273)\ \mathrm{K}}{(21-(-5))\ \mathrm{K}}
= \frac{294}{26} = 11.31$$

$$\dot W_{net,in} = \frac{\dot Q_H}{\mathrm{COP}_{HP}}
= \frac{135{,}000\ \mathrm{kJ/h}}{11.31}\cdot\frac{1\ \mathrm{h}}{3600\ \mathrm{s}}
= 3.316\ \mathrm{kW}$$

*[added] ✓ Verified: $294/26 = 11.308$; $135{,}000/11.31/3600 = 3.3156$ kW.*

> **The pattern all three share, and the reason they are the likeliest CAT questions.** Each gives a
> claimed performance and two temperatures. The method is always: **convert both temperatures to
> kelvin**, compute the reversible limit ($1 - T_L/T_H$, or $T_L/(T_H-T_L)$, or $T_H/(T_H-T_L)$),
> compare, conclude. The word **"minimum"** in Example 6-5 is the tell that the reversible limit is
> wanted rather than an actual device.
>
> Watch the two traps: **$T_H - T_L$ is the same in °C and in K** (a *difference*, per
> `01-temperature-thermometry` §1.7) but the **numerator is not** — Example 6-4's $T_L$ must be
> $275\ \mathrm{K}$, never $2$. And choose the right COP: refrigerator → $T_L$ on top, heat pump →
> $T_H$ on top.

---

## 3b.11 The quality of energy ·EPC s84

[fig ·EPC s84] Çengel Figures 6–49 and 6–50. A reversible engine rejecting to $T_L = 303\ \mathrm{K}$,
with a table of $\eta_{th}$ against source temperature; and a $T$-axis showing that **the higher the
temperature of thermal energy, the higher its quality**.

| $T_H$, K | $\eta_{th}$, % |
|---|---|
| 925 | 67.2 |
| 800 | 62.1 |
| 700 | 56.7 |
| 500 | 39.4 |
| 350 | 13.4 |

*[added] All five rows verified against $\eta = 1 - 303/T_H$ ✓. The relation is not printed on the
slide; the table is generated by it.*

> **The engineering point.** Work is not recoverable from heat in proportion to its quantity but to its
> **temperature**. Heat at 350 K is nearly worthless — 13 % recoverable — while the same joules at
> 925 K yield 67 %. This is why waste-heat recovery targets high-temperature streams, and it is the
> qualitative claim behind every efficiency comparison in `04-` and `05-`.

---

## 3b.12 The Diesel cycle ·EPC s85–s92

[hist ·EPC s88] **1892 — Rudolf Diesel invented the Diesel engine.** Main goal: **high efficiency**.

**What distinguishes it** ·EPC s85

- The Diesel engine takes in **JUST air**.
- The **compression ratio is higher**, thus higher efficiency.
- Diesel engines use **direct fuel injection**.
- **No spark plug** required.

> ⚠ VERIFY **V11** ·EPC s88 — the definition slide reads *"the burning of fuel is triggered by heat
> generated in compressing **fuel-air mixture**"*. **A Diesel engine compresses air alone**; fuel is
> injected into the already-hot compressed air. Compressing a fuel-air mixture is the **Otto**
> (spark-ignition) arrangement. The slide contradicts **s85** ("takes in JUST air") and **s91**
> ("Piston compresses air upwards. Fuel injected."). See `_verification-log.md`.

**Advantages and disadvantages** ·EPC s86 — printed exactly as follows:

| Advantages | Disadvantages |
|---|---|
| There is no KNOCKING in the diesel engine | Pollution |
| Higher efficiency | Heavy |
| **Less expensive** | **Initial high cost** |

> ⚠ VERIFY **V18** ·EPC s86 — **the two lists contradict each other.** "Less expensive" and "Initial
> high cost" occupy the *same position* in each list, with no qualifier anywhere on the slide to
> reconcile them. The distinction the slide is reaching for is **running cost vs capital cost**: a
> diesel has **lower fuel/running cost** but **higher initial cost**. Write it that way in an answer.
>
> Also on the same slide: *"There is no KNOCKING in the diesel engine"* is **not right as stated** —
> diesels do exhibit combustion knock ("diesel knock", from ignition delay). The true advantage is
> that they are **not knock-limited in compression ratio** the way petrol engines are, which is
> precisely what permits the higher compression ratio of s85. See `_verification-log.md`.

**Vehicles using diesel engines** ·EPC s87 — cars, trucks, submarines, locomotives.

**How it works — the four mechanical strokes** ·EPC s91

1. **Intake** — inlet valve opens, exhaust closed.
2. **Compression** — both valves closed. Piston compresses air upwards. Fuel injected.
3. **Power** — fuel ignites. Gas forces piston downwards.
4. **Exhaust** — inlet valve closed, exhaust valve opens, piston travels upward.

[fig ·EPC s89] A four-panel engine cutaway: 1—INTAKE (air drawn in past the intake valve), 2—COMPRESSION
AND INJECTION (piston at top, injection valve), 3—EXPANSION (burning gas driving the piston down),
4—EXHAUST (gases leaving past the exhaust valve).

> **Do not confuse the four strokes with the four thermodynamic processes.** ·EPC s91's list is the
> *mechanical* cycle of a four-stroke engine; ·EPC s92's list below is the *air-standard thermodynamic*
> cycle. They are different four-item lists and an exam will ask for one or the other.

[def] **The air-standard Diesel cycle** ·EPC s92

| Process | Description |
|---|---|
| **1–2** | **Isentropic compression** |
| **2–3** | **Constant-pressure heat addition** |
| **3–4** | **Isentropic expansion** |
| **4–1** | **Constant-volume heat rejection** |

[fig ·EPC s90] $P$–$V$ line diagram: states 2 and 3 joined by a **horizontal** line at constant
pressure, labelled $Q_H$ *injection*; curves 1→2 and 3→4 both labelled "$S$ = const"; states 4 and 1
joined by a **vertical** line at constant volume, labelled $Q_L$.

[fig ·EPC s92] Imported colour figure (watermarked `©2017mechanicalbooster.com`) showing both diagrams.
**$P$–$V$:** 2→3 horizontal at $P_2 = P_3$ with $Q_{in}$; 3→4 curve with $W_{out}$; 4→1 vertical at
$V_1 = V_4$ with $Q_{out}$; 1→2 curve with $W_{in}$. **$T$–$s$:** 1→2 vertical at $S_1 = S_2$
($W_{in}$); 2→3 curve rising with $Q_{in}$; 3→4 vertical at $S_3 = S_4$ ($W_{out}$); 4→1 curve falling
with $Q_{out}$.

> ### ⚠ The Diesel thermal efficiency is NOT given anywhere in EPC
>
> No $\eta_{th}$ expression, no compression ratio $r$, no cut-off ratio $r_c$, and no numerical
> efficiency value appears in slides 85–92. The deck asserts "higher efficiency" **qualitatively only**.
>
> [added] The standard air-standard result, supplied because the deck does not:
>
> $$\eta_{th,\,Diesel} = 1 - \frac{1}{r^{\gamma-1}}
> \left[\frac{r_c^{\gamma} - 1}{\gamma\left(r_c - 1\right)}\right]$$
>
> with compression ratio $r = V_1/V_2$ and cut-off ratio $r_c = V_3/V_2$. **Check whether `04-` or
> `05-` supplies this before relying on the added form** — those decks tabulate the cycles and may
> print it.

> ⚠ VERIFY **C15** ·EPC s84 — slide 84 sits immediately before the Diesel block but is **not Diesel
> content**; it is the Carnot quality-of-energy material treated in §3b.11. Recorded so the slide is
> not filed under the wrong topic. The Diesel block genuinely begins at s85.

---

### Cross-references

- $W_{net,out} = Q_{net,in}$ for a cycle and the $P$–$V$ enclosed-area result → **02-first-law** §2.5, §2.11.
- **Absolute temperature** — required by every Carnot relation here → **01-temperature-thermometry** §1.6.
- Enthalpy, used by the turbine result of §3b.3 → **02-first-law** §2.7.
- **This file is authoritative for the second law, heat engines, efficiency, COP and Carnot.**
  `04-thermodynamic-cycles` and `05-heat-engines-and-carnot` cover the same ground qualitatively and
  should **reference this file rather than restate it** — see `00-index.md` § Overlap map.
- Entropy as a property is **absent from the entire course** — see the gap map.

- The cyclic result $\Delta U = 0 \Rightarrow Q_{net} = W_{net}$ (§3b.3) and thermal efficiency (§3b.4)
  are what **exercises/ga2-topic1-part2-first-law** Part A Q2 and Q5 turn on; the second-law reason the
  waste heat cannot be recovered is §3b.5 and §3b.11.

### Verification notes for this section

All 71 slides read from **165 dpi renders**, including the 17 image-only slides. **Every numerical
claim was recomputed independently and every one is correct** — nine worked examples, the five-row
quality-of-energy table, the EER and ton conversions, the R-134a state consistency, and the
$\mathrm{COP}_{HP} = \mathrm{COP}_R + 1$ identity.

| ID | Slide | Class | Summary |
|---|---|---|---|
| **V10** | s68 | substantive | Carnot's dates printed 1769–1832; he was born **1796** |
| **V11** | s88 | substantive | Diesel definition says the **fuel-air mixture** is compressed; it is air alone |
| **V13** | s75 | substantive | $f(T_1,T_3) = T_3/T_1$ inverts s76's own $Q_L/Q_H = T_L/T_H$ (result unaffected) |
| **V14** | s37 | substantive | $v_i' = v_i + dp$ (should be $dv$); and $P$ increasing contradicts the weights being removed |
| **V15** | s23 | substantive | the **first** law's criterion presented, unlabelled, on a slide titled "Second law" |
| **V16** | s57–s58 | substantive | equivalence proof: subscript clipped from "$Q_H + Q$" and "+" dropped from the prose |
| **V18** | s86 | substantive | "Less expensive" vs "Initial high cost"; and "no KNOCKING" is wrong as stated |
| **C15** | s84 | cosmetic | Carnot quality-of-energy slide sits immediately before the Diesel block, which begins at s85 |
| **C16** | s63 | cosmetic | Kelvin–Planck restated without the single-reservoir qualifier |
| **C17b** | s35 | cosmetic | figure shows free expansion; the only bullet is about mixing |
| **C18** | various | cosmetic | typo cluster — "vaccum", "chaosness", "Air-Conditions", "Comprises of", dropped "=" in "(COP  1)", "The diesel Cycle", duplicated sentence s31/s32, example-numbering clash s64/s78 |

**Checked and cleared — the items that looked wrong but are not:**

- **s55** $(Q_L - Q_H) - (0 - W_{in}) = \Delta U_{cycle} = 0$ — correct; it is the s48 template with
  $W_{out} = 0$. Expands to $W_{in} = Q_H - Q_L$ ✓
- **s48** $Q_{in} \neq Q_{net}$ — a deliberate caution, not a typo (verified at 3× zoom)
- **s67** "20.000…1 °C" — intentional textbook notation for infinitesimally above 20 °C
- Kelvin–Planck (s51) and Clausius (s56) wordings match the canonical phrasing exactly
- Both Carnot principles, worded exactly as printed, are correct
- The absolute-temperature requirement **is** stated, twice (s75, s76), and demonstrated (s79)

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
