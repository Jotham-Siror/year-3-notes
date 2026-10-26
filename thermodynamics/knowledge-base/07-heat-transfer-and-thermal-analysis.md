---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "07 — Heat Transfer and Thermal Analysis (Topic 4)"
source: "HT — 'MEC_3105_Topic4_Lecture_Notes1.pdf', 26 pages"
pages: "1-26"
file_role: topic
subtopics:
  - "conduction (Fourier), convection (Newton), radiation (Stefan-Boltzmann)"
  - "thermal resistance networks — the Ohm's-law analogy"
  - "heat exchangers: flow arrangements, LMTD method, effectiveness-NTU method"
  - "insulation: critical radius, composite layers, insulated pipe"
  - "EE applications: transformers, cables, busbars, heat sinks, motors, overhead lines"
  - "ANSYS thermal analysis: heat equation, seven-step workflow, steady vs transient, validation"
key_equations: [fourier, plane-wall, r-cond, r-cond-cyl, newton-cooling, r-conv, stefan-boltzmann, r-series-parallel, lmtd, overall-u, ntu, critical-radius, insulated-pipe, arrhenius, cable-ampacity, busbar-balance, junction-temperature, fin-efficiency, heat-equation]
prerequisites: ["01b-thermal-expansion-heat-and-calorimetry"]
leads_to: ["08-ansys-icepak", "09-heat-transfer-experiments"]
verification_flags: 5
tags: [heat-transfer, conduction, convection, radiation, thermal-resistance, heat-exchanger, lmtd, ntu, insulation, critical-radius, transformer, cable-ampacity, busbar, heat-sink, fin, ansys, fea, mesh-convergence]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND: [def] · [eq] · [ex] worked example (lecturer's numbers) · [fig] ·
  [added] supplied here, NOT in the source · ·HT pN = PDF page N (the document prints no page numbers) ·
  ⚠ VERIFY = flagged; detail in _verification-log.md. -->

# 07 — Heat Transfer and Thermal Analysis (Topic 4)

Scope: the whole of HT, 26 pages — sub-topics **4.1** (mechanisms, heat exchangers, insulation),
**4.2** (EE applications) and **4.3** (ANSYS). Sub-topics 4.4–4.10 (Icepak) are in `08-ansys-icepak`.

> **New this year.** HT and the Icepak notes are not in the earlier course material, and **none of the
> six past papers examines heat transfer**. Exam weight is unknown. Use the lecturer's own list on ·HT
> p25 (§7.5 below) as the best guide to what he will ask.

> **What carries marks.** Every equation in the summary table (§7.5) has a worked number in the notes.
> 4.3 (ANSYS) is descriptive — expect "explain the workflow" and "how would you validate" questions,
> not calculations.

---

## 7.1 Mechanisms of heat transfer ·HT p1–p4

### Symbols — §7.1

| Symbol | Meaning | Units | Typical |
|---|---|---|---|
| $q$ | heat transfer rate | $\mathrm{W}$ | |
| $k$ | thermal conductivity | $\mathrm{W/(m\,K)}$ | Cu 385, Al 205, steel 50 |
| $A$ | area normal to heat flow (conduction) / in contact with fluid (convection) | $\mathrm{m^2}$ | |
| $dT/dx$ | temperature gradient | $\mathrm{K/m}$ | |
| $L$ | wall thickness, or cylinder length | $\mathrm{m}$ | |
| $T_1$, $T_2$ | hot face, cold face | $^\circ\mathrm{C}$ or $\mathrm{K}$ | |
| $r_1$, $r_2$ | inner, outer radius | $\mathrm{m}$ | |
| $R$ | thermal resistance | $\mathrm{K/W}$ (= $^\circ\mathrm{C/W}$) | |
| $h$ | convective (film) coefficient | $\mathrm{W/(m^2\,K)}$ | air natural 2–25 |
| $T_s$, $T_\infty$ | surface, bulk fluid temperature | $^\circ\mathrm{C}$ or $\mathrm{K}$ | |
| $\varepsilon$ | emissivity, $0 \le \varepsilon \le 1$ (black body = 1) | — | 0.7–0.9 |
| $\sigma$ | Stefan–Boltzmann constant $5.67 \times 10^{-8}$ | $\mathrm{W/(m^2\,K^4)}$ | |
| $T_{sur}$ | surroundings temperature | **$\mathrm{K}$ only** | |

### A. Conduction ·HT p1–p2

[def] Transfer of thermal energy through a stationary medium by molecular interaction, with no bulk motion.

[eq] Fourier's law

$$
q = -kA\,\frac{dT}{dx}
$$

The minus sign: heat flows from hot to cold (second law).

[eq] Plane wall, steady state

$$
q = \frac{kA\,(T_1 - T_2)}{L}
$$

[eq] As a resistance — the Ohm's-law analogy, $V = IR$

$$
q = \frac{\Delta T}{R_{cond}}, \qquad R_{cond} = \frac{L}{kA}
$$

[eq] Cylindrical layer (cables, pipes), length $L$

$$
R_{cond,cyl} = \frac{\ln(r_2/r_1)}{2\pi k L}
$$

Key values ·HT p2, W/(m·K): copper ≈ 385 · aluminium ≈ 205 · steel ≈ 50 · glass ≈ 1.0 · PVC ≈ 0.19 ·
XLPE ≈ 0.28 · air ≈ 0.026 · SF₆ ≈ 0.013.

### [ex] Copper busbar ·HT p2

$k = 385$, centre $85\ ^\circ\mathrm{C}$, surface $72\ ^\circ\mathrm{C}$, path $40\ \mathrm{mm}$, area $800\ \mathrm{mm^2}$.

$$
q = \frac{kA\,\Delta T}{L} = \frac{(385)(0.0008)(85 - 72)}{0.04}
$$

$$
q = \frac{(385)(0.0008)(13)}{0.04} = 100.1\ \mathrm{W}
$$

### B. Convection ·HT p2–p3

[def] Heat transfer between a surface and a moving fluid touching it: conduction at the interface plus
bulk fluid motion carrying the energy away.

[eq] Newton's law of cooling

$$
q = hA\,(T_s - T_\infty)
$$

$$
R_{conv} = \frac{1}{hA}
$$

| Type | Driven by | Typical $h$, $\mathrm{W/(m^2\,K)}$ |
|---|---|---|
| Natural (free) | buoyancy — density differences | 2–25 (air) |
| Forced | fan, pump, wind | 25–250 (air); 500–15 000 (liquids — transformer oil, water) |

Raising $h$ is the main lever for cooling electrical equipment.

### [ex] Transformer radiator fin ·HT p3

$T_s = 75\ ^\circ\mathrm{C}$, air at $35\ ^\circ\mathrm{C}$, $A = 0.8\ \mathrm{m^2}$, $h = 12$.

$$
q = hA\,(T_s - T_\infty) = (12)(0.8)(75 - 35) = 384\ \mathrm{W}
$$

per fin.

### C. Radiation ·HT p3–p4

[def] Energy carried by electromagnetic waves (infrared). Needs no medium. Every body above absolute zero emits.

[eq] Emission from a real surface

$$
q = \varepsilon \sigma A T^{4}
$$

[eq] Net exchange with an enclosure

$$
q_{net} = \varepsilon \sigma A\,(T_s^{4} - T_{sur}^{4})
$$

> ⚠ **Kelvin, always.** Using °C in $T^4$ gives a completely wrong answer. Below about 300 °C radiation is
> usually secondary to convection on electrical equipment; at high temperature (heating elements, arcs,
> a core under severe fault) it matters.

### D. Resistance networks ·HT p4

[eq] Series and parallel

$$
R_{total} = R_1 + R_2 + R_3 + \dots \quad \text{(series)}
$$

$$
\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots \quad \text{(parallel)}
$$

[eq] Overall rate

$$
q = \frac{\Delta T_{overall}}{R_{total}} = \frac{T_{hot} - T_{cold}}{R_{total}}
$$

| Thermal | Electrical |
|---|---|
| temperature difference $\Delta T$ | voltage $V$ |
| heat rate $q$ | current $I$ |
| thermal resistance $R$ | resistance $R$ |

EE application ·HT p4: a cable conductor's $I^2R$ heat conducts through the XLPE ($R_{cond,cyl}$) then
convects away ($R_{conv}$) — two resistances in series:

$$
T_{conductor} = T_{ambient} + q\,R_{total}
$$

This is the basis of IEC 60287 cable ampacity.

---

## 7.2 Heat exchangers ·HT p5–p7

[def] A device that transfers heat between two fluids at different temperatures **without letting them
mix** — power-station condensers and feedwater heaters, transformer coolers, generator air/hydrogen
coolers, inverter liquid cooling, HVAC.

### Symbols — §7.2

| Symbol | Meaning | Units |
|---|---|---|
| $Q$ | total heat transfer rate | $\mathrm{W}$ |
| $U$ | overall heat transfer coefficient | $\mathrm{W/(m^2\,K)}$ |
| $A$ | heat transfer area | $\mathrm{m^2}$ |
| $\Delta T_1$, $\Delta T_2$ | hot − cold temperature difference at each end | $\mathrm{K}$ |
| $\Delta T_{LM}$ | log mean temperature difference | $\mathrm{K}$ |
| $h_i$, $A_i$ / $h_o$, $A_o$ | inner / outer film coefficient and area | |
| $R_{wall}$ | wall conduction resistance | $\mathrm{K/W}$ |
| $\varepsilon$ | **effectiveness** (⚠ not emissivity) | — |
| $C = \dot m c_p$ | heat capacity rate; $C_{min}$, $C_{max}$ | $\mathrm{W/K}$ |
| $c = C_{min}/C_{max}$ | heat capacity ratio | — |
| $\mathrm{NTU}$ | number of transfer units | — |
| $T_{h,in}$, $T_{c,in}$ | hot and cold inlet temperatures | $^\circ\mathrm{C}$ |

### A. Flow arrangements ·HT p5

| Type | Description | Use |
|---|---|---|
| **Parallel-flow** | both enter at the same end, same direction; $\Delta T$ large at inlet, small at outlet | less efficient than counter-flow |
| **Counter-flow** | opposite directions; more uniform $\Delta T$ | more efficient for the same area — preferred in power engineering |
| **Cross-flow** | one fluid perpendicular to the other | air-cooled radiators, fin-and-tube condensers for inverters |
| **Shell-and-tube** | one fluid in many tubes, the other across them inside a shell | most common industrially — station condensers, transformer oil coolers |
| **Plate** | stacked corrugated plates, alternate passages | compact, high effectiveness, easy to clean — district heating, data centres |

### B. The LMTD method ·HT p5–p7

[eq] Design equation

$$
Q = U A\,\Delta T_{LM}
$$

[eq] Log mean temperature difference

$$
\Delta T_{LM} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}
$$

[eq] Overall coefficient from the resistances ·HT p6

$$
\frac{1}{UA} = \frac{1}{h_i A_i} + R_{wall} + \frac{1}{h_o A_o}
$$

$U$ lumps both films, the wall, and any fouling layers into one number.

**When to use LMTD:** all four terminal temperatures are known (or follow from energy balances). If an
outlet temperature is unknown you would have to iterate — use NTU instead.

[added] Which ends? **Counter-flow:** $\Delta T_1 = T_{h,in} - T_{c,out}$, $\Delta T_2 = T_{h,out} - T_{c,in}$.
**Parallel-flow:** $\Delta T_1 = T_{h,in} - T_{c,in}$, $\Delta T_2 = T_{h,out} - T_{c,out}$. The lecturer's
summary (p25) says you must do both; the notes work only counter-flow.

### [ex] Transformer oil cooler ·HT p6–p7

Oil $80 \to 55\ ^\circ\mathrm{C}$; water $25 \to 40\ ^\circ\mathrm{C}$; counter-flow; $U = 350$; $Q = 60\ \mathrm{kW}$.

(a)

$$
\Delta T_1 = 80 - 40 = 40\ \mathrm{K} \quad \text{(oil inlet end)}
$$

$$
\Delta T_2 = 55 - 25 = 30\ \mathrm{K} \quad \text{(oil outlet end)}
$$

$$
\Delta T_{LM} = \frac{40 - 30}{\ln(40/30)} = \frac{10}{0.2877} = 34.8\ \mathrm{K}
$$

(b)

$$
A = \frac{Q}{U\,\Delta T_{LM}} = \frac{60\,000}{(350)(34.8)} = \frac{60\,000}{12\,180} = 4.93\ \mathrm{m^2}
$$

[added] Same temperatures in **parallel flow**: $\Delta T_1 = 80 - 25 = 55$, $\Delta T_2 = 55 - 40 = 15$,
$\Delta T_{LM} = 40/\ln(55/15) = 30.8\ \mathrm{K}$, $A = 5.57\ \mathrm{m^2}$ — 13 % more area. That is why
counter-flow is preferred.

### C. The effectiveness–NTU method ·HT p7

Use when outlet temperatures are unknown — the usual design case.

[eq] Effectiveness

$$
\varepsilon = \frac{Q_{actual}}{Q_{max}}
$$

[eq] Maximum possible rate — an infinitely long counter-flow exchanger, where the fluid with the smaller
$C$ swings through the full inlet difference:

$$
Q_{max} = C_{min}\,(T_{h,in} - T_{c,in})
$$

[eq] Number of transfer units

$$
\mathrm{NTU} = \frac{UA}{C_{min}}
$$

$\varepsilon$ is linked to NTU and $c = C_{min}/C_{max}$ by charts or equations that depend on the
exchanger type. **The notes give none of those relations**, so no numerical NTU question can be set from
them alone.

[fig] p7: mind-map — NTU calculation, minimum heat capacity rate, maximum heat rate, inlet temperatures,
effectiveness, heat transfer rate, around "heat exchanger performance".

EE application: generator hydrogen coolers and transformer water coolers are sized by NTU — rated heat
and inlet coolant known, area and outlet temperatures wanted.

---

## 7.3 Thermal insulation ·HT p8–p10

[def] A low-$k$ material applied to cut unwanted heat gain or loss — efficiency, equipment safety,
personnel protection.

Adding insulation raises $R_{cond}$. On a **cylinder** it also raises the outer area, which lowers
$R_{conv}$ — so the net effect is not obvious.

### Symbols — §7.3

| Symbol | Meaning | Units |
|---|---|---|
| $r_1$ | bare (base) radius | $\mathrm{m}$ |
| $r$ | outer radius of insulation | $\mathrm{m}$ |
| $r_c$ | critical radius | $\mathrm{m}$ |
| $k_{ins}$ | insulation conductivity | $\mathrm{W/(m\,K)}$ |
| $h$ | outside film coefficient | $\mathrm{W/(m^2\,K)}$ |

### B. Critical radius ·HT p8–p9

[eq] Total resistance of an insulated cylinder, length $L$

$$
R_{total} = \frac{\ln(r/r_1)}{2\pi k_{ins} L} + \frac{1}{h\,2\pi r L}
$$

This passes through a **minimum** — maximum heat loss — at

$$
r_c = \frac{k_{ins}}{h}
$$

- $r_1 < r_c$: adding insulation first **increases** heat loss, until the outer radius reaches $r_c$.
- $r_1 > r_c$: any insulation reduces heat loss.
- Small pipes and cables often have $r_1 < r_c$.

### [ex] Power cable ·HT p9

$r_1 = 8\ \mathrm{mm}$, PVC $k_{ins} = 0.19$, $h = 10$.

$$
r_c = \frac{k_{ins}}{h} = \frac{0.19}{10} = 0.019\ \mathrm{m} = 19\ \mathrm{mm}
$$

$8 < 19$, so PVC up to $r = 19\ \mathrm{mm}$ **increases** heat loss. Thin insulation on a small cable is
there for electrical insulation, not thermal.

> ⚠ **V32 — the page's last step is wrong.** It says "only insulation thicker than 11 mm ($r > 19$ mm)
> will reduce heat loss below the bare-cable value." Past $r_c$ the loss starts to **fall**, but it is
> still **above** the bare value. It only drops back to the bare value at $r \approx 64\ \mathrm{mm}$ — about
> **56 mm** of PVC.

[added] Working, per metre ($L = 1$):

$$
R_{bare} = \frac{1}{h\,2\pi r_1} = \frac{1}{(10)(2\pi)(0.008)} = 1.99\ \mathrm{K\,m/W}
$$

$$
R(r_c) = \frac{\ln(19/8)}{2\pi(0.19)} + \frac{1}{(10)(2\pi)(0.019)} = 0.725 + 0.838 = 1.56\ \mathrm{K\,m/W}
$$

Lower $R$ than bare — more heat lost. Set $R(r) = R_{bare}$ and solve numerically:

$$
r \approx 0.064\ \mathrm{m}
$$

### C. Composite insulation ·HT p9–p10

Real systems: conductor → primary insulation → metallic screen → outer sheath → soil.

[eq] Heat loss through an insulated pipe ·HT p9

$$
Q = \frac{2\pi L\,(T_i - T_o)}{\dfrac{1}{r_1 h_i} + \dfrac{\ln(r_2/r_1)}{k_{pipe}} + \dfrac{\ln(r_3/r_2)}{k_{insulation}} + \dfrac{1}{r_3 h_c}}
$$

| Symbol | Meaning | Units |
|---|---|---|
| $T_i$, $T_o$ | fluid inside, environment outside | $^\circ\mathrm{C}$ |
| $r_1$, $r_2$, $r_3$ | pipe inside, pipe outside, insulation outside radius | $\mathrm{m}$ |
| $h_i$, $h_c$ | inside film, outside convective coefficient | $\mathrm{W/(m^2\,K)}$ |
| $k_{pipe}$, $k_{insulation}$ | conductivities | $\mathrm{W/(m\,K)}$ |

[eq] General layered form ·HT p10 — written on the page **without a summation sign** (C33):

$$
R_{total} = \sum_n \frac{\ln(r_{n+1}/r_n)}{2\pi k_n L} + R_{contact} + R_{conv}
$$

$R_{contact}$: imperfect contact and trapped air between layers — matters in transformer windings and
busbar joints.

---

## 7.4 Heat transfer in electrical engineering ·HT p11–p17

### 4.2.1 Power transformers ·HT p11–p12

Heat sources: copper losses ($I^2R$ in windings) and iron losses (hysteresis, eddy currents).

[eq] Arrhenius ageing of paper/pressboard insulation — each sustained $6$–$10\ ^\circ\mathrm{C}$ over rating
roughly **halves** insulation life:

$$
k = A\,e^{-E_a/(RT)}
$$

| Symbol | Meaning | Value |
|---|---|---|
| $k$ | ageing rate (e.g. fall in degree of polymerisation per hour) | |
| $A$ | pre-exponential factor | |
| $E_a$ | activation energy | 110–128 kJ/mol, cellulose in mineral oil (IEC 60076-7, IEEE C57.91) |
| $R$ | gas constant | 8.314 J/(mol·K) |
| $T$ | absolute temperature | K |

⚠ $k$ here is a rate, not conductivity; $A$ is a factor, not area; $R$ is the gas constant, not resistance.

Cooling classes (IEC 60076-2):

| Class | Meaning | Notes |
|---|---|---|
| **ONAN** | Oil Natural Air Natural | no pumps or fans; thermosiphon; simplest, most reliable |
| **ONAF** | Oil Natural Air Forced | fans on radiators; $h$ ~12 → ~30 W/(m²·K) |
| **OFAF** | Oil Forced Air Forced | pumps and fans; large units, 100 MVA+ |
| **OFWF** | Oil Forced Water Forced | oil-to-water exchanger; compact — offshore, ships, indoors |

Thermal model: copper losses → $R_{winding\text{-}oil}$ → $R_{oil\text{-}tank}$ → $R_{tank\text{-}air}$.
**Hot-spot** temperature (≈ 20–25 °C above top-oil) decides insulation life.

[ex] 40 MVA ONAN transformer ·HT p12 — losses 180 kW, $R_{total} = 0.17\ ^\circ\mathrm{C/kW}$, ambient 40 °C:

$$
\Delta T = (180)(0.17) = 30.6\ ^\circ\mathrm{C}
$$

$$
T_{top\text{-}oil} = 40 + 30.6 = 70.6\ ^\circ\mathrm{C}
$$

With ONAF fans, $R_{total} = 0.10$:

$$
\Delta T = (180)(0.10) = 18\ ^\circ\mathrm{C}, \qquad T_{top\text{-}oil} = 58\ ^\circ\mathrm{C}
$$

### 4.2.2 Cables — ampacity ·HT p12–p13

Ampacity: the largest continuous current whose $I^2R$ heat can get out without the conductor exceeding
the insulation's rated temperature.

[eq] Cable in air, steady state

$$
I^2 R_{dc}\,(1 + \lambda) = \frac{T_{max} - T_{amb}}{R_T}
$$

| Symbol | Meaning | Units |
|---|---|---|
| $I$ | rated current (ampacity) | $\mathrm{A}$ |
| $R_{dc}$ | DC resistance per unit length | $\Omega/\mathrm{m}$ |
| $\lambda$ | dielectric loss factor (extra losses in insulation and screen) | — |
| $T_{max}$ | max conductor temperature (90 °C for XLPE) | $^\circ\mathrm{C}$ |
| $T_{amb}$ | ambient | $^\circ\mathrm{C}$ |
| $R_T$ | total thermal resistance per unit length, conductor to ambient | $^\circ\mathrm{C\,m/W}$ |

$R_T$ = cylindrical layers (insulation, bedding, sheath, soil) + outside convection, from §7.1. IEC 60287
gives the full method.

[ex] Derating ·HT p13 — 33 kV XLPE cable, 400 A at 25 °C ambient, used at 40 °C. Allowed rise falls from
$90 - 25 = 65\ \mathrm{K}$ to $90 - 40 = 50\ \mathrm{K}$. Since $I^2 \propto \Delta T$:

$$
\frac{I_{new}}{I_{old}} = \sqrt{\frac{50}{65}} = \sqrt{0.769} = 0.877
$$

$$
I_{new} = 400 \times 0.877 \approx 351\ \mathrm{A}
$$

### 4.2.3 Busbars and switchgear ·HT p13–p14

[eq] Exposed rectangular busbar, natural convection plus radiation

$$
I^2 R = q_{conv} + q_{rad} = hA\,(T_s - T_{amb}) + \varepsilon \sigma A\,(T_s^{4} - T_{amb}^{4})
$$

- IEC 62271 / IEC 61439 limits: about **35 K** rise for silver/tin-plated joints, **70 K** for bare copper.
- Radiation is **20–30 %** of the total from a bare busbar at rated rise — do not drop it.

[ex] ·HT p14 — copper busbar, 415 V board, 1000 A, $h = 10$, $\varepsilon = 0.7$, $A = 0.3\ \mathrm{m^2}$. The
page writes "$I^2R = 1000^2 \times 20 \times 10^{-6} = 20\ \mathrm{W/m^2} \times$ area (illustrative)" and
stops; it says engineers find $T_s$ by iteration or software. **No answer is given, and the units are
muddled (C34)** — $1000^2 \times 20\ \mu\Omega = 20\ \mathrm{W}$.

[added] Finishing it with $I^2R = 20\ \mathrm{W}$ and $T_{amb} = 35\ ^\circ\mathrm{C}$ (308 K): solve
$20 = 10(0.3)(T_s - 308) + 0.7(5.67 \times 10^{-8})(0.3)(T_s^4 - 308^4)$ by trial —
$T_s \approx 312.5\ \mathrm{K} \approx 39.4\ ^\circ\mathrm{C}$, a $4.4\ \mathrm{K}$ rise, with radiation carrying
about 32 % of the 20 W — consistent with the page's "20–30 %, don't neglect it".

### 4.2.4 Power electronics — heat sinks ·HT p14–p16

Max junction temperature $T_{j,max}$: typically 125 or 150 °C.

[eq] Junction temperature — series network junction → case → sink → air

$$
T_j = T_{amb} + P_{loss}\,(R_{jc} + R_{cs} + R_{sa})
$$

| Symbol | Meaning | Units |
|---|---|---|
| $T_j$ | junction temperature | $^\circ\mathrm{C}$ |
| $P_{loss}$ | switching + conduction losses | $\mathrm{W}$ |
| $R_{jc}$ | junction-to-case (datasheet) | $^\circ\mathrm{C/W}$ |
| $R_{cs}$ | case-to-heatsink (interface material) | $^\circ\mathrm{C/W}$ |
| $R_{sa}$ | heatsink-to-ambient (geometry and $h$) | $^\circ\mathrm{C/W}$ |

Lower $R_{sa}$ with more fin area and higher $h$ (fans, liquid).

[eq] Fin efficiency — the fin cools along its length, so not all of it is at base temperature:

$$
\eta_f = \frac{\tanh(mL)}{mL}, \qquad m = \sqrt{\frac{hP}{kA_c}}
$$

| Symbol | Meaning | Units |
|---|---|---|
| $m$ | fin parameter | $\mathrm{m^{-1}}$ |
| $L$ | fin length | $\mathrm{m}$ |
| $P$ | fin perimeter (⚠ not power, not pressure) | $\mathrm{m}$ |
| $A_c$ | fin cross-section | $\mathrm{m^2}$ |
| $k$ | fin conductivity | $\mathrm{W/(m\,K)}$ |

[ex] IGBT in a 500 kW inverter ·HT p16 — 800 W, $R_{jc} = 0.04$, $R_{cs} = 0.02\ ^\circ\mathrm{C/W}$,
$T_j \le 125\ ^\circ\mathrm{C}$ at $T_{amb} = 40\ ^\circ\mathrm{C}$:

$$
R_{sa,max} = \frac{T_{j,max} - T_{amb}}{P_{loss}} - R_{jc} - R_{cs}
$$

$$
R_{sa,max} = \frac{125 - 40}{800} - 0.04 - 0.02 = 0.1063 - 0.06 = 0.046\ ^\circ\mathrm{C/W}
$$

This target sets the minimum heat-sink size and whether air or liquid cooling is needed.

IGBT vs MOSFET ·HT p16: IGBT — high voltage, high current, lower conduction loss (EVs, motor drives,
HVAC). MOSFET — low voltage, fast switching (switch-mode supplies, DC-DC converters).

### 4.2.5 Rotating machines ·HT p16–p17

Heat from copper ($I^2R$), iron (eddy and hysteresis) and bearings. Limits: Class F **155 °C**,
Class H **180 °C**.

| Code | Method | Mechanism |
|---|---|---|
| IC01 | open drip-proof (ODP) | internal fan pulls outside air through |
| IC411 | totally enclosed fan-cooled (TEFC) | external fan over ribbed frame |
| IC81W | water jacket | liquid convection, high $h$ |
| — | hydrogen (generators > 100 MW) | H₂ has $k \approx 8\times$ and density $\approx 0.07\times$ air |

[ex] 250 kW induction motor, efficiency 94 % ·HT p16–p17:

$$
P_{loss} = \frac{(1 - 0.94)(250)}{0.94} \approx 15.96\ \mathrm{kW}
$$

$$
T_{frame} = T_{amb} + P_{loss}\,R_{frame\text{-}air}, \qquad R_{frame\text{-}air} = \frac{1}{hA_{frame}}
$$

### 4.2.6 Overhead lines ·HT p17

Rating is thermal: steady balance between $I^2R$ heating and loss to wind (convection) and radiation.
Hotter conductor → more sag ($\alpha\,\Delta T$ per unit length) → ground clearance limit.

As printed:

$$
I^2 R_{ac} = q_{conv(wind)} + q_{rad(solar)}
$$

> ⚠ **V33 — solar radiation is a heat gain, not a loss.** The standard balance (IEEE 738 / CIGRE) is
> heating = cooling:
>
> $$
> I^2 R_{ac} + q_{solar} = q_{conv} + q_{rad}
> $$
>
> with $q_{rad}$ the conductor's own radiated loss.

Dynamic thermal rating (DTR): use live wind data (which drives $h$) to carry more than nameplate current
when conditions allow.

ACSR — aluminium strands on a steel core: stronger, less sag, long spans, wind and ice. AAAC — aluminium
alloy 6201-T81: better strength-to-weight and corrosion resistance, coastal and high-wind lines.

---

## 7.5 Thermal simulation with ANSYS ·HT p17–p24

Hand formulas are exact only for simple shapes (plane walls, long cylinders, single fins). Real kit —
windings, busbar joints, IGBT modules, cable joints, end-turns — needs **finite element analysis**.
ANSYS modules: Mechanical Steady-State Thermal, Transient Thermal, Fluent (CFD).

### 4.3.1 The heat conduction equation ·HT p18

| Symbol | Meaning | Units |
|---|---|---|
| $\rho$ | density | $\mathrm{kg/m^3}$ |
| $c_p$ | specific heat | $\mathrm{J/(kg\,K)}$ |
| $\partial T/\partial t$ | rate of temperature change | $\mathrm{K/s}$ |
| $\nabla \cdot (k \nabla T)$ | net conduction into a point | $\mathrm{W/m^3}$ |
| $\dot q_{gen}$ | volumetric heat generation (e.g. $I^2R$ per volume) | $\mathrm{W/m^3}$ |

[eq] Transient

$$
\rho c_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + \dot q_{gen}
$$

[eq] Steady state ($\partial T/\partial t = 0$)

$$
\nabla \cdot (k \nabla T) + \dot q_{gen} = 0
$$

ANSYS solves this on the mesh; you do not solve it by hand.

### 4.3.2 The seven-step workflow ·HT p18–p21

1. **Geometry** — build in SpaceClaim or import (STEP, IGES, Parasolid). **Defeature** (remove small chamfers, holes). Use symmetry — model half or a quarter.
2. **Materials** — steady state needs $k$ only; transient also $\rho$ and $c_p$. Can be temperature-dependent. Check library values against maker's data.
3. **Mesh** — elements SOLID87 (10-node tet), SOLID90 (20-node hex), SHELL131/132 (thin plates). Coarse = fast, fine = accurate. Refine locally at hot spots, thin layers, fin tips. Quality: skewness < 0.9, aspect ratio < 20:1.
4. **Boundary conditions** — temperature (Dirichlet); heat flux (W/m²); **convection** ($h$ and $T_{bulk}$ — the most common); internal heat generation (W/m³); radiation. **Choosing $h$ is the biggest judgement call** — take it from correlations, experiment, or a CFD run.
5. **Solve** — steady: $[K]\{T\} = \{Q\}$ (conductance matrix, nodal temperatures, heat loads). Transient: time-step from an initial temperature. Nonlinear cases iterate to a convergence criterion (default 0.1 % on temperature).
6. **Post-process** — temperature contours (hot spot), heat-flux vectors (heat paths), probes, **reaction heat flow** (energy balance check), transient animation.
7. **Mesh convergence study** — refine and plot the peak temperature against element count; converged when successive results change by less than **1–2 %**. **The step beginners skip most.**

### 4.3.3 Steady-state vs transient ·HT p22

| | Steady-state | Transient |
|---|---|---|
| Solves | equilibrium temperatures under constant conditions | how temperature changes with time |
| When | continuous duty at rated load | start-up/shut-down, faults, cyclic load, time constants |
| Material data | $k$ only | $k$, $\rho$, $c_p$ |
| Solve time | minutes | longer — depends on time steps |
| EE example | 33 kV cable joint at rated current | IGBT during a 10-second overload |

### 4.3.4 Lab session — busbar joint ·HT p22–p23

1. SpaceClaim: two overlapping copper bars with a contact interface.
2. Copper $k = 385$; contact conductance at the joint.
3. Heat generation $\dot q = I^2\rho/A^2$ W/m³ ($\rho$ here = **electrical resistivity**, ⚠ not density).
4. Convection $h = 10$–$15$, $T_{amb} = 35\ ^\circ\mathrm{C}$ on exposed faces.
5. Mesh, solve, find the hot spot at the joint.
6. Mesh convergence: coarse → medium → fine.
7. Compare with a Newton's-law hand estimate.
8. Raise contact conductance (better joint) and see the hot spot fall.

Mirrors switchgear makers' checks against IEC 62271-1 before type-testing. The lab work itself is in
`../ansys/lab3-busbar-joint/`.

### 4.3.5 Is the result right? ·HT p23–p24

| Check | What to do |
|---|---|
| **Energy balance** | heat generated ≈ heat leaving by convection/radiation, within 1–2 %; use the reaction tool. Big gap = missing or wrong BC. |
| **Hand calculation** | simple features (one insulation layer, one fin) should match §7.1 formulas within a few %. |
| **Physical sense** | hot to cold; hottest at the source; more insulation → hotter source. |
| **Mesh convergence** | hot spot shown converged before use. |
| **Sensitivity** | vary $h$, contact conductance, ambient by ±20–30 %; a sensitive input needs better data. |

---

## 7.6 The lecturer's summary ·HT p25

| Concept | Equation | Key parameter |
|---|---|---|
| Conduction, plane wall | $q = kA\,\Delta T/L$ | $k$ |
| Conduction resistance, plane | $R = L/(kA)$ | higher $L$ or lower $k$ → higher $R$ |
| Conduction resistance, cylinder | $R = \ln(r_2/r_1)/(2\pi k L)$ | cables, pipes |
| Convection | $q = hA\,(T_s - T_\infty)$ | $h$ |
| Convection resistance | $R = 1/(hA)$ | lower $h$ → higher $R$ |
| Radiation | $q = \varepsilon\sigma A\,(T_s^4 - T_{sur}^4)$ | **kelvin** |
| Overall | $q = \Delta T_{overall}/R_{total}$ | series add; parallel add reciprocals |
| Heat exchanger | $Q = UA\,\Delta T_{LM}$ | all four temperatures known |
| Critical radius | $r_c = k_{ins}/h$ | $r < r_c$ → insulation may increase $q$ |
| Semiconductor | $T_j = T_{amb} + P(R_{jc} + R_{cs} + R_{sa})$ | $R$ in °C/W |

**"Key concepts to master for assessment"** — the lecturer's own list:

1. Identify and distinguish the three mechanisms in any system.
2. Apply Fourier, Newton and Stefan–Boltzmann to plane walls and cylinders.
3. Build and solve a series resistance network — overall rate **and intermediate temperatures**.
4. LMTD for **parallel and counter-flow**; use $Q = UA\,\Delta T_{LM}$ for area or duty.
5. Explain the critical radius and calculate $r_c$.
6. Junction-temperature network; find max $R_{sa}$.
7. Explain the ANSYS workflow in order (geometry → mesh → BCs → solution → post-processing → convergence).
8. Steady vs transient, with an EE example of each.
9. Critically evaluate an ANSYS result: energy balance, hand check, mesh convergence.
10. Apply all of it to transformer cooling, cable ampacity, busbar rating, heat-sink sizing.

Reading ·HT p26: Borgnakke & Sonntag (2019); Incropera et al. (2011) ch. 2, 3, 11; Anders (1997) *Rating
of Electric Power Cables*; ANSYS Thermal Analysis Guide; IEC 60076-2; IEC 60287-1.

---

### Cross-references

- Introductory conduction, convection, radiation → `01b` §1b.6
- Icepak (sub-topics 4.4–4.10) → `08-ansys-icepak`
- Lab experiments on $k$ and $h$ → `09-heat-transfer-experiments` §9.2

### Verification notes for this section

| ID | Page | Issue |
|---|---|---|
| **V32** | p9 | critical-radius example: "insulation thicker than 11 mm will reduce heat loss below the bare value" — wrong; that needs $r \approx 64$ mm (≈ 56 mm of PVC) |
| **V33** | p17 | overhead-line balance puts solar radiation on the loss side; it is a gain |
| **C32** | p7 | "Where UAUA is…" — duplicated text |
| **C33** | p10 | layered $R_{total}$ written without its summation sign |
| **C34** | p14 | busbar example: "$1000^2 \times 20 \times 10^{-6} = 20\ \mathrm{W/m^2} \times$ area" — unit muddle, and no answer reached |

Every worked number above was recomputed and agrees with the page except where flagged.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
