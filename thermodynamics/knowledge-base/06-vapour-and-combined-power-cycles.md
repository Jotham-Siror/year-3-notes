---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "06 — Vapour and Combined Power Cycles"
source: "VC — '3.3 MEC 3105 Vapour and Combined Power Cycles.pdf', 22 slides"
slides: "1-22"
file_role: topic
subtopics:
  - "reading the T-s diagram for water; quality and entropy"
  - "why the Carnot vapour cycle is impractical"
  - "the ideal Rankine cycle and its energy analysis (steady-flow energy equation)"
  - "actual cycle: pump and turbine isentropic efficiencies"
  - "raising efficiency: condenser pressure, superheat, boiler pressure"
  - "reheat Rankine cycle"
  - "regenerative Rankine cycle: open and closed feedwater heaters"
  - "second-law (exergy) analysis"
  - "cogeneration and the utilisation factor"
  - "combined gas-steam cycle"
key_equations: [sfee-per-unit-mass, rankine-pump, rankine-boiler, rankine-turbine, rankine-condenser, rankine-efficiency, heat-rate, isentropic-efficiency, reheat, open-fwh, exergy-destruction, stream-exergy, utilisation-factor]
prerequisites: ["03a-phase-behaviour-and-equilibrium", "04-thermodynamic-cycles", "05-heat-engines-and-carnot"]
leads_to: ["09-heat-transfer-experiments"]
verification_flags: 1
tags: [rankine, vapour-cycle, t-s-diagram, quality, steady-flow-energy-equation, isentropic-efficiency, reheat, regeneration, feedwater-heater, exergy, cogeneration, combined-cycle]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND: [def] · [eq] · [ex] · [fig] figure described from the rendered slide ·
  [added] supplied here, NOT in the source · ·VC sN = slide N (= PDF page N) ·
  ⚠ VERIFY = flagged; detail in _verification-log.md. -->

# 06 — Vapour and Combined Power Cycles

Scope: the whole of VC, 22 slides — Topic 3 part 3. **This deck closes three gaps the past papers
examined**: the Rankine cycle analysed (CAT 2 Q3A/B), the steady-flow energy equation (CAT 1 Q3,
Exam Q1F) in its enthalpy-only form, and exergy (CAT 2 Q1B).

> **Slide numbers are PDF page numbers.** The printed slide number matches on every slide.

> **Exam value.** The lecturer works **no numerical example** in this deck. Everything examinable is on
> **s6, s7, s11, s14, s17 and s19** — the equation slides. The rest is qualitative (how to raise
> efficiency, open vs closed heaters, cogeneration modes) and comes up as "explain" parts.

> **What you still need from outside the deck:** steam tables. The equations below give
> $\eta_{th}$ only once you have $h_1 \dots h_4$, and no table is reproduced anywhere in the course.

---

## Symbols — the whole deck

| Symbol | Meaning | Units | Typical |
|---|---|---|---|
| $q_{in}$, $q_{out}$ | heat in (boiler), heat out (condenser), per kg | $\mathrm{kJ/kg}$ | |
| $w_{in}$, $w_{out}$ | work in (pump), work out (turbine), per kg | $\mathrm{kJ/kg}$ | |
| $h$ | specific enthalpy; $h_i$ inlet, $h_e$ exit | $\mathrm{kJ/kg}$ | from steam tables |
| $s$ | specific entropy; $s_f$, $s_g$ sat. liquid, sat. vapour | $\mathrm{kJ/(kg\,K)}$ | |
| $x$ | quality (dryness fraction), vapour mass / total mass | — | 0 to 1 |
| $v$ | specific volume; $v_f$ sat. liquid | $\mathrm{m^3/kg}$ | $\approx 0.001$ for water |
| $P$ | pressure | $\mathrm{kPa}$ | |
| $\eta_{th}$ | thermal efficiency | — | 0.3–0.45 |
| $\eta_P$, $\eta_T$ | pump, turbine isentropic efficiency | — | 0.8–0.9 |
| subscript $s$ / $a$ | isentropic (ideal) / actual | | |
| $y$ | fraction of steam bled to a feedwater heater, $\dot m_6/\dot m_5$ | — | |
| $\dot X_{dest}$, $x_{dest}$ | exergy destroyed (rate, per kg) | $\mathrm{kW}$, $\mathrm{kJ/kg}$ | |
| $T_0$ | dead-state (environment) temperature | $\mathrm{K}$ | ≈ 298 |
| $\dot S_{gen}$, $s_{gen}$ | entropy generated | $\mathrm{kW/K}$, $\mathrm{kJ/(kg\,K)}$ | |
| $T_b$ | boundary temperature where heat crosses | $\mathrm{K}$ | |
| $\psi$ | stream (flow) exergy | $\mathrm{kJ/kg}$ | |
| $\epsilon_u$ | utilisation factor (cogeneration) | — | up to 0.8 actual |
| $\dot Q_p$ | process heat delivered | $\mathrm{kW}$ | |

> ⚠ **Three epsilons.** $\epsilon_u$ here = utilisation factor. In Topic 4, $\varepsilon$ = emissivity
> **and** heat-exchanger effectiveness. See `_nomenclature.md`.
> ⚠ **$E$ on s2** means internal energy ($H = E + PV$), as on TC s12 (C21). Everywhere else it is $U$.

---

## 6.1 The $T$–$s$ diagram for water ·VC s2–s3

[fig] s2: the vapour dome on $T$–$s$ axes. Critical point at the top. Left edge = saturated liquid line,
right edge = saturated vapour line. **Isobars run horizontal inside the dome.** Side notes define
enthalpy ($H = E + PV$) and entropy ("the unavailability of a system's thermal energy for conversion
into mechanical work").

How to read it ·VC s3:

1. **Subcooled (compressed) liquid** — left of the saturated liquid line. $T$ and $s$ rise with heating at nearly constant $P$.
2. **Two-phase region** (inside the dome) — $T$ constant at a given $P$; $s$ rises with quality.
3. **Superheated vapour** — right of the saturated vapour line. $T$ and $s$ both rise with heat at constant $P$.

[eq] Entropy of a wet mixture ·VC s3

$$
s = (1 - x)\,s_f + x\,s_g
$$

[added] The same rule holds for $h$ and $v$, and is the one you use with steam tables:

$$
h = h_f + x\,h_{fg}, \qquad h_{fg} = h_g - h_f
$$

Uses: Rankine analysis, finding steam quality, locating critical and saturation states.

---

## 6.2 Why not a Carnot vapour cycle? ·VC s4

[fig] Two Carnot cycles on $T$–$s$: (a) entirely inside the dome; (b) heat added partly in the
superheat region.

Cycle (a): 1-2 isothermal heat addition (boiler) → 2-3 isentropic expansion (turbine) → 3-4 isothermal
heat rejection (condenser) → 4-1 isentropic compression (compressor).

Why it is not used:

- **1-2:** keeping heat addition inside the two-phase region caps the top temperature at **374 °C** (water's critical point).
- **2-3:** the turbine gets very wet steam — droplets erode the blades.
- **4-1:** you cannot build a compressor that handles a liquid-vapour mix.
- Cycle (b) needs isentropic compression to extreme pressures and isothermal heat transfer at varying pressure — also impractical.

---

## 6.3 The ideal Rankine cycle ·VC s5–s6

[def] Superheat the steam in the boiler and condense it **completely** in the condenser. The result is
the **Rankine cycle** — the ideal cycle for vapour power plants, with no internal irreversibilities. ·VC s5

[fig] Four components in a loop: **1** sat. liquid → pump → **2** compressed liquid → boiler →
**3** superheated vapour → turbine → **4** wet mixture → condenser → back to 1.

| Process | Device | What happens |
|---|---|---|
| 1-2 | pump | isentropic compression |
| 2-3 | boiler | constant-$P$ heat addition |
| 3-4 | turbine | isentropic expansion |
| 4-1 | condenser | constant-$P$ heat rejection |

### [eq] The steady-flow energy equation, per unit mass ·VC s6

This is the course's first statement of the SFEE. KE and PE changes are neglected:

$$
(q_{in} - q_{out}) + (w_{in} - w_{out}) = h_e - h_i \qquad (\mathrm{kJ/kg})
$$

[added] The full form, with KE and PE, which the past papers ask for (CAT 1 Q3, Exam Q1F):

$$
q - w = (h_e - h_i) + \frac{V_e^2 - V_i^2}{2} + g\,(z_e - z_i)
$$

with $q$ net heat in, $w$ net work out, $V$ velocity (⚠ not volume), $z$ height. Divide the KE term by
1000 to get kJ/kg when $V$ is in m/s.

### [eq] Apply it to each device ·VC s6

**Pump** ($q = 0$):

$$
w_{pump,in} = h_2 - h_1
$$

$$
w_{pump,in} = v\,(P_2 - P_1)
$$

where

$$
h_1 = h_{f\,@\,P_1}, \qquad v \cong v_1 = v_{f\,@\,P_1}
$$

**Boiler** ($w = 0$):

$$
q_{in} = h_3 - h_2
$$

**Turbine** ($q = 0$):

$$
w_{turb,out} = h_3 - h_4
$$

**Condenser** ($w = 0$):

$$
q_{out} = h_4 - h_1
$$

**Cycle:**

$$
w_{net} = q_{in} - q_{out} = w_{turb,out} - w_{pump,in}
$$

$$
\eta_{th} = \frac{w_{net}}{q_{in}} = 1 - \frac{q_{out}}{q_{in}}
$$

[eq] Heat rate (US practice) ·VC s6 — heat supplied, in Btu, per kWh of electricity:

$$
\eta_{th} = \frac{3412\ (\mathrm{Btu/kWh})}{\text{Heat rate}\ (\mathrm{Btu/kWh})}
$$

On a $T$–$s$ diagram, $\eta_{th}$ = area enclosed by the cycle ÷ area under the heat-addition line.

### [added] How to work a Rankine question — the four steps

1. **State 1** — sat. liquid at condenser pressure: $h_1 = h_f$, $v_1 = v_f$ from tables.
2. **State 2** — $w_{pump} = v_1(P_2 - P_1)$ with $P$ in kPa gives kJ/kg; $h_2 = h_1 + w_{pump}$.
3. **State 3** — superheat table at boiler $P$ and $T$: read $h_3$, $s_3$.
4. **State 4** — $s_4 = s_3$; at condenser $P$, $x_4 = (s_4 - s_f)/s_{fg}$; $h_4 = h_f + x_4 h_{fg}$.

Then $q_{in}$, $w_{turb}$, $w_{net}$, $\eta_{th}$ from the device equations above.

---

## 6.4 Actual cycles — isentropic efficiencies ·VC s7

The actual cycle departs from the ideal because of **fluid friction** (pressure drops in boiler,
condenser and piping) and **heat loss to the surroundings**.

[fig] (a) actual vs ideal cycle: pressure drop in the boiler, pressure drop in the condenser,
irreversibility in pump and turbine. (b) Pump end point moves 2s → 2a; turbine end point 4s → 4a, both
to the right (higher entropy).

[eq] Pump — actual work is **more** than ideal:

$$
\eta_P = \frac{w_s}{w_a} = \frac{h_{2s} - h_1}{h_{2a} - h_1}
$$

[eq] Turbine — actual work is **less** than ideal:

$$
\eta_T = \frac{w_a}{w_s} = \frac{h_3 - h_{4a}}{h_3 - h_{4s}}
$$

> **The trap.** The fraction is flipped between pump and turbine. Both efficiencies must come out below 1.
> If yours is above 1, you have the fraction upside down.

---

## 6.5 Raising Rankine efficiency ·VC s8–s10

**One idea behind every method:** raise the **average temperature of heat addition** or lower the
**average temperature of heat rejection**.

| Method | Effect | Side effect / limit |
|---|---|---|
| **Lower condenser pressure** ·s8 | lowers $T_{low,avg}$ | more moisture at the last turbine stages; limited by cooling-water temperature. Condensers run well below atmospheric pressure. |
| **Superheat to higher temperature** ·s9 | raises $T_{high,avg}$; net work and heat input both rise, efficiency rises | **less** moisture at turbine exit (good). Limited by metallurgy — about **620 °C** at turbine inlet. |
| **Raise boiler pressure** ·s10 | raises $T_{high,avg}$ | at fixed turbine inlet $T$, **more** moisture at exit — fixed by reheating |

Supercritical plants ($P > 22.06\ \mathrm{MPa}$) reach about **40 %** (fossil) and **34 %** (nuclear). ·VC s10

---

## 6.6 The ideal reheat Rankine cycle ·VC s11–s12

Question: how to use high boiler pressure without wet steam at the turbine exit?

1. Superheat to very high temperature — limited metallurgically.
2. **Expand in two stages and reheat in between.**

[fig] Boiler → **3** → high-pressure turbine → **4** → reheater (at $P_4 = P_5 = P_{reheat}$) → **5** →
low-pressure turbine → **6** → condenser → **1** → pump → **2** → boiler.

[eq] ·VC s11

$$
q_{in} = q_{primary} + q_{reheat} = (h_3 - h_2) + (h_5 - h_4)
$$

$$
w_{turb,out} = w_{turb,I} + w_{turb,II} = (h_3 - h_4) + (h_5 - h_6)
$$

Facts ·VC s12:

- One reheat raises efficiency by **4 to 5 %**.
- More stages push the expansion-reheat towards isothermal at $T_{max}$, but **more than two reheats is not practical**; the second gives about half the gain of the first.
- Reheat temperature is very close or equal to turbine inlet temperature.
- **Optimum reheat pressure ≈ one-quarter of the maximum cycle pressure.**

---

## 6.7 The ideal regenerative Rankine cycle ·VC s13–s16

The first part of boiler heating (compressed liquid up to saturation) happens at low temperature, which
drags the average down. **Regeneration:** bleed steam from the turbine and use it to preheat the
feedwater. The device is a **regenerator** or **feedwater heater (FWH)** — mixing (**open**) or not
mixing (**closed**). ·VC s13

### Open feedwater heater ·VC s14

[def] A **mixing chamber**: bled steam mixes with the pumped feedwater; ideally the mixture leaves as
saturated liquid at the heater pressure.

[fig] Boiler → **5** → turbine; fraction $y$ bled at **6** to the open FWH; $1 - y$ continues to **7** →
condenser → **1** → pump I → **2** → open FWH → **3** → pump II → **4** → boiler.

[eq] Per kg of steam through the boiler:

$$
q_{in} = h_5 - h_4
$$

$$
q_{out} = (1 - y)(h_7 - h_1)
$$

$$
w_{turb,out} = (h_5 - h_6) + (1 - y)(h_6 - h_7)
$$

$$
w_{pump,in} = (1 - y)\,w_{pump\,I,in} + w_{pump\,II,in}
$$

with

$$
y = \dot m_6 / \dot m_5
$$

$$
w_{pump\,I,in} = v_1 (P_2 - P_1), \qquad w_{pump\,II,in} = v_3 (P_4 - P_3)
$$

[added] $y$ comes from an energy balance on the open heater (exit sat. liquid at 3):

$$
y\,h_6 + (1 - y)\,h_2 = h_3 \quad\Rightarrow\quad y = \frac{h_3 - h_2}{h_6 - h_2}
$$

### Closed feedwater heater ·VC s15–s16

[def] Heat passes from bled steam to feedwater **without mixing**, so the two streams can be at
different pressures.

[fig] s15: bled steam at **7** enters the closed FWH; its condensate is pumped (pump II) into a mixing
chamber with the heated feedwater; s16: a plant with one open and three closed heaters.

| | Open FWH | Closed FWH |
|---|---|---|
| How | mixes the streams | heat exchanger, no mixing |
| Cost | simple, cheap | complex tubing, expensive |
| Heat transfer | good | less effective |
| Pumps | one per heater | no separate pump per heater |

Most plants use **a combination of open and closed** heaters. ·VC s16

---

## 6.8 Second-law (exergy) analysis ·VC s17

[def] **Exergy** is the work potential of energy: the maximum useful work a system at a given state could
produce in a given environment, reached when it goes reversibly to the state of the environment.

[def] **Exergy efficiency** measures how close a process is to reversible — 100 % when there is zero
entropy generation, i.e. zero exergy destruction:

$$
X_{destroyed} = T_0\,S_{gen}
$$

[eq] Steady-flow system (rate):

$$
\dot X_{dest} = T_0 \dot S_{gen} = T_0 (\dot S_{out} - \dot S_{in}) = T_0 \left( \sum_{out} \dot m s + \frac{\dot Q_{out}}{T_{b,out}} - \sum_{in} \dot m s - \frac{\dot Q_{in}}{T_{b,in}} \right) \qquad (\mathrm{kW})
$$

[eq] Steady-flow, one inlet, one exit (per kg):

$$
x_{dest} = T_0 s_{gen} = T_0 \left( s_e - s_i + \frac{q_{out}}{T_{b,out}} - \frac{q_{in}}{T_{b,in}} \right) \qquad (\mathrm{kJ/kg})
$$

[eq] Whole cycle:

$$
x_{dest} = T_0 \left( \sum \frac{q_{out}}{T_{b,out}} - \sum \frac{q_{in}}{T_{b,in}} \right)
$$

[eq] Cycle exchanging heat only with a source at $T_H$ and a sink at $T_L$:

$$
x_{dest} = T_0 \left( \frac{q_{out}}{T_L} - \frac{q_{in}}{T_H} \right)
$$

[eq] Stream exergy:

$$
\psi = (h - h_0) - T_0 (s - s_0) + \frac{V^2}{2} + g z \qquad (\mathrm{kJ/kg})
$$

Subscript 0 = dead state (environment). All temperatures in **kelvin**.

Why bother: a second-law analysis shows **where** the largest irreversibilities are, so you know where
to start improving. [added] In a Rankine plant that is almost always the boiler.

---

## 6.9 Cogeneration ·VC s18–s20

[def] **Cogeneration:** producing more than one useful form of energy (process heat **and** electric
power) from the same source. Process steam is typically **5–7 atm, 150–200 °C**. ·VC s18

[fig] s18: a simple process-heating plant (boiler → process heater, no turbine).
[fig] s19: an ideal cogeneration plant — boiler takes in **120 kW**, turbine gives **20 kW**, process heater
delivers **100 kW**, pump work ≈ 0.

[eq] Utilisation factor ·VC s19

$$
\epsilon_u = \frac{\text{Net work output} + \text{Process heat delivered}}{\text{Total heat input}} = \frac{\dot W_{net} + \dot Q_p}{\dot Q_{in}}
$$

$$
\epsilon_u = 1 - \frac{\dot Q_{out}}{\dot Q_{in}}
$$

[added] Check with the s19 figure:

$$
\epsilon_u = \frac{20 + 100}{120} = 1.00 = 100\ \%
$$

- The ideal steam-turbine cogeneration plant: **100 %**.
- Actual plants: as high as **80 %**; some recent ones higher.

Adjustable-load plant ·VC s20 — three modes:

| Demand | Steam routing | Result |
|---|---|---|
| High process heat | all steam to process heaters, none to condenser ($\dot m_7 = 0$); if still short, throttle some boiler steam through the pressure-reducing valve to $P_6$ | zero waste heat |
| Maximum process heat | all boiler steam through the PRV ($\dot m_5 = \dot m_4$) | **no power** produced |
| No process heat | all steam through turbine and condenser ($\dot m_5 = \dot m_6 = 0$) | ordinary power plant |

---

## 6.10 Combined gas–vapour power cycles ·VC s21–s22

- A gas cycle **topping** a vapour cycle = the **combined cycle**.
- Most common: gas-turbine (**Brayton**) on top, steam-turbine (**Rankine**) below. Higher efficiency than either alone.
- The hot gas-turbine exhaust is the heat source for the steam cycle.
- Little extra capital cost, so many new plants are combined-cycle and many old ones are being converted.
- Thermal efficiencies **over 50 %** reported.

[fig] s22: combined gas–steam plant schematic (image only, no text layer).

> ⚠ **The Brayton cycle is named here but never analysed** — no efficiency equation in this deck or any
> other. Still on the gap map.

---

### Cross-references

- Carnot limit and $T$–$s$ rectangle → `05-heat-engines-and-carnot` §5.11
- Quality, saturation, phase diagrams → `03a-phase-behaviour-and-equilibrium`
- Rankine simulation in ANSYS → `09-heat-transfer-experiments` §9.3
- Past-paper questions this file now covers, as listed in `past-papers/00-past-papers-index.md` § Topic coverage: CAT 2 Q3A, Q3B (Rankine) · CAT 2 Q1B (exergy) · CAT 1 Q3 and Exam Q1F (SFEE)

### Verification notes for this section

| ID | Slide | Issue |
|---|---|---|
| **C31** | s2 | $E$ used for internal energy in $H = E + PV$ — same habit as TC s12 (C21) |

No substantive errors found. Every equation slide (s3, s6, s7, s11, s14, s17, s19) read from the render.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
