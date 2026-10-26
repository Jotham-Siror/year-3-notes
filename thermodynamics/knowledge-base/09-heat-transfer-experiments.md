---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "09 — Practical Application and Experiments on Heat Transfer (Topic 5)"
source: "T5 — 'MEC_3105_Topic 5.pdf', 8 pages"
pages: "1-8"
file_role: topic
subtopics:
  - "specific heat by the method of mixtures; water equivalent"
  - "conduction experiment — thermal conductivity k"
  - "convection experiment — heat transfer coefficient h"
  - "Rankine cycle simulation in ANSYS vs steam-table hand calculation"
  - "error analysis and lab report structure"
key_equations: [method-of-mixtures, specific-heat-from-mixtures, water-equivalent, k-from-fourier, h-from-newton, percentage-error]
prerequisites: ["01b-thermal-expansion-heat-and-calorimetry", "06-vapour-and-combined-power-cycles", "07-heat-transfer-and-thermal-analysis"]
leads_to: []
verification_flags: 1
tags: [laboratory, calorimetry, specific-heat, water-equivalent, thermal-conductivity, convection-coefficient, rankine, ansys, error-analysis, co8]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND: [def] · [eq] · [ex] · [added] supplied here, NOT in the source ·
  ·T5 pN = PDF page N (footer "Page N of 8" matches) · ⚠ VERIFY = flagged. -->

# 09 — Practical Application and Experiments on Heat Transfer (Topic 5)

Scope: the whole of T5, 8 pages. Page 1 is a title page (academic year 2026/2027).

> **Exam value.** This is lab material. What can be examined on paper: the **method-of-mixtures
> calculation** (one full worked example), **back-calculating $k$ and $h$**, the **direction of an error**
> ("would $c$ be too high or too low?"), and **why the ANSYS Rankine result differs from the hand
> result**. The discussion questions at the end of each section are the likely question bank.

### Learning outcomes ·T5 p2

1. Use a calorimetric heat balance to find the specific heat of an unknown sample.
2. Use Fourier's law and Newton's law of cooling on lab data to find $k$ and $h$.
3. Identify sources of error and quantify them with percentage error.
4. Build an ANSYS Rankine-cycle simulation and extract $T$, $P$ and quality at each state.
5. Compare simulated and steam-table results and explain the differences — **Course Outcome 8 (CO8)**.

---

## 9.1 Specific heat — method of mixtures ·T5 p2–p4

### Symbols — §9.1

| Symbol | Meaning | Units |
|---|---|---|
| $m_s$, $m_w$ | mass of sample, water | $\mathrm{kg}$ |
| $c_s$, $c_w$ | specific heat of sample, water ($c_w = 4186$) | $\mathrm{J/(kg\,K)}$ |
| $T_{i,s}$, $T_{i,w}$ | initial temperature of sample, water | $^\circ\mathrm{C}$ |
| $T_f$ | common final (equilibrium) temperature | $^\circ\mathrm{C}$ |
| $C_{cal}$ | heat capacity of the calorimeter | $\mathrm{J/K}$ |
| $m_{cal}$ | water equivalent of the calorimeter | $\mathrm{kg}$ |

Theory: first law for an isolated system — heat lost by the hot body = heat gained by the cold ones.

[eq] Energy balance ·T5 p2

$$
m_s c_s (T_{i,s} - T_f) = m_w c_w (T_f - T_{i,w}) + C_{cal} (T_f - T_{i,w})
$$

[eq] Solved for the sample ·T5 p3

$$
c_s = \frac{m_w c_w (T_f - T_{i,w}) + C_{cal}(T_f - T_{i,w})}{m_s (T_{i,s} - T_f)}
$$

[def] **Water equivalent** — the mass of water that would absorb the same heat for the same rise as the
calorimeter:

$$
C_{cal} = m_{cal}\,c_w
$$

so the calorimeter folds into one effective water mass, $m_w + m_{cal}$.

**Apparatus:** copper calorimeter with stirrer and jacket; thermometer/thermocouple (±0.1 °C); heater or
boiling bath; balance (±0.01 g); metal sample; tongs.

**Procedure:** weigh sample → weigh calorimeter, add water, weigh → record $T_{i,w}$ → heat sample to a
steady $T_{i,s}$ (≈ 100 °C in a boiling bath) → transfer fast, cover, stir → read every 15–30 s until
steady ($T_f$) → tabulate, repeat.

### [ex] Specimen results and calculation ·T5 p3–p4

| Quantity | Symbol | Trial 1 | Trial 2 |
|---|---|---|---|
| Mass of sample (g) | $m_s$ | 50.20 | 50.20 |
| Initial sample temperature (°C) | $T_{i,s}$ | 99.5 | 99.4 |
| Mass of water (g) | $m_w$ | 150.00 | 150.00 |
| Water equivalent (g) | $m_{cal}$ | 12.00 | 12.00 |
| Initial water temperature (°C) | $T_{i,w}$ | 24.0 | 24.2 |
| Final temperature (°C) | $T_f$ | 28.6 | 28.7 |

Trial 1, effective water mass $150.00 + 12.00 = 162.00\ \mathrm{g}$:

$$
c_s = \frac{(0.162)(4186)(28.6 - 24.0)}{(0.05020)(99.5 - 28.6)}
$$

$$
c_s = \frac{(0.162)(4186)(4.6)}{(0.05020)(70.9)} = \frac{3119}{3.559} \approx 876\ \mathrm{J/(kg\,K)}
$$

(The page prints the numerator as 3118.6 — it is 3119.4. C37. The answer stands.)

[eq] Percentage error, against aluminium ≈ 900:

$$
\%\ \text{Error} = \frac{|876 - 900|}{900} \times 100\ \% \approx 2.7\ \%
$$

[added] Trial 2 for practice:

$$
c_s = \frac{(0.162)(4186)(28.7 - 24.2)}{(0.05020)(99.4 - 28.7)} = \frac{3051.6}{3.549} \approx 860\ \mathrm{J/(kg\,K)}
$$

error ≈ 4.4 %.

### Sources of error ·T5 p4

1. Heat lost during transfer — the biggest one in most student setups.
2. Calorimeter and stirrer heat capacity — must be included via water equivalent, or the sample's $c$ comes out **low**.
3. Thermometer calibration and lag.
4. Evaporation from the water surface.

### Discussion questions ·T5 p4

1. Why transfer quickly? Would heat lost in transfer make $c_s$ too high or too low?
2. If the water equivalent were ignored, would $c_s$ be over- or underestimated?
3. One change that would cut the main error.

[added] Answers from the balance equation: (1) the sample arrives cooler, so less heat reaches the water,
$T_f$ is lower, but the formula still uses the full drop $T_{i,s} - T_f$ — **$c_s$ too low**. (2) the
numerator loses the $C_{cal}$ term — **$c_s$ underestimated**. (3) e.g. heat the sample inside an
insulated transfer chute directly above the calorimeter.

---

## 9.2 Heat transfer experiments ·T5 p4–p6

### Symbols — §9.2

| Symbol | Meaning | Units |
|---|---|---|
| $q$ | heater power, $q = VI$ | $\mathrm{W}$ |
| $A$ | sample cross-section / heated surface area | $\mathrm{m^2}$ |
| $dT/dx$ | slope of $T$ vs position along the sample | $\mathrm{K/m}$ |
| $k$ | thermal conductivity | $\mathrm{W/(m\,K)}$ |
| $T_s$, $T_\infty$ | surface, free-stream air temperature | $^\circ\mathrm{C}$ |
| $h$ | convective coefficient | $\mathrm{W/(m^2\,K)}$ |

### Conduction — linear / guarded hot-plate apparatus ·T5 p5

Purpose: find $k$ from the steady temperature gradient at a known heat input.

[eq]

$$
q = -kA\,\frac{dT}{dx} \quad\Rightarrow\quad k = \frac{q}{A\,(dT/dx)}
$$

- A cylindrical sample with thermocouples along it, between heated and water-cooled sections.
- $q$ from the heater's $V$ and $I$; $dT/dx$ = slope of the best-fit line of $T$ vs distance.
- The **guard heater** is held at the heater's temperature so heat goes one way only — through the sample — cutting radial loss.

Procedure: clamp with thermal paste → fixed power, wait for steady readings → record $V$, $I$ and every
thermocouple → plot $T$ vs $x$ → slope → $k$ → compare with the book value.

### Convection — heated surface in natural or forced air ·T5 p5

[eq]

$$
q = hA\,(T_s - T_\infty) \quad\Rightarrow\quad h = \frac{q}{A\,(T_s - T_\infty)}
$$

Repeat at several fan speeds to show $h$ rising with air velocity; fan off = natural-convection limit.

### [ex] Specimen comparison ·T5 p6

| Condition | $q$ (W) | $T_s - T_\infty$ (°C) | $h$ (W/m²K) | Dominant mode |
|---|---|---|---|---|
| Natural (fan off) | 8.0 | 22.5 | 6.1 | natural convection + minor radiation |
| Forced, low fan | 8.0 | 11.2 | 12.3 | forced convection |
| Forced, high fan | 8.0 | 6.4 | 21.5 | forced convection |

Same 8 W rejected each time: as $h$ rises, the temperature difference needed falls.

[added] The plate area is not given. All three rows are consistent with
$A = q/[h(T_s - T_\infty)] \approx 0.058\ \mathrm{m^2}$, e.g.

$$
A = \frac{8.0}{(6.1)(22.5)} = 0.0583\ \mathrm{m^2}
$$

### Sources of error ·T5 p6

1. Side/back losses from the conduction sample → $k$ **overestimated** unless guarded or corrected.
2. Uneven fan velocity across the plate → $h$ is an area average.
3. Thermocouple not truly at the surface, or disturbing the boundary layer.
4. Meter drift in $V$ and $I$ → error in both $k$ and $h$.

### Discussion questions ·T5 p6

1. Why a guard heater, and what happens to $k$ without it?
2. Which mode dominates in each row of the table, and how can you tell from the data alone?
3. If radiation from the plate were significant but ignored, would $h$ be too high or too low?

[added] (1) Without it some heat leaks sideways, but $q$ is still taken as the full heater power — $k$ comes
out **too high**. (2) $h$ in the natural range (2–25) with fan off; trebling with fan speed shows forced
convection takes over. (3) **Too high** — the radiated part of $q$ is wrongly credited to convection.

---

## 9.3 Rankine cycle simulation in ANSYS ·T5 p6–p8

Link to Topic 3: the ideal Rankine cycle was done by hand from steam tables / Mollier chart
(`06-vapour-and-combined-power-cycles` §6.3). Here the same cycle runs in ANSYS so you can see property
distributions through each component and run parameter sweeps fast.

### Workflow ·T5 p7

1. Build the loop: boiler (evaporator) → turbine → condenser → feed pump.
2. Working fluid water/steam; set boiler $P$ and $T$ (or superheat) and condenser $P$ (or saturation $T$).
3. Turbine and pump isentropic efficiencies; boiler/condenser pressure drops (or zero, to match the hand case).
4. Steady-state solve → $T$, $P$, quality at every state, including along the turbine expansion.
5. Extract $\eta_{th} = w_{net}/q_{in}$ and turbine-exit quality.
6. Sweep boiler $P$/$T$ and condenser $P$.
7. Plot $\eta_{th}$ against each; compare the baseline with the hand result.

### [ex] Comparison ·T5 p7

| Parameter | Hand (steam tables) | ANSYS | Difference |
|---|---|---|---|
| Thermal efficiency $\eta$ | 34.8 % | 34.1 % | 0.7 percentage points |
| Turbine-exit quality $x$ | 0.88 | 0.86 | 0.02 |
| Net specific work (kJ/kg) | 955 | 938 | 1.8 % |

### Why they differ — the CO8 skill ·T5 p7–p8

Differences come from **assumptions**, rarely from computing mistakes:

- **Idealisations** — hand: no pressure drop in boiler/condenser piping; ANSYS may include a small one.
- **Heat losses** in piping and components — neglected by hand, possibly included in the simulation.
- **Property data** — table interpolation by hand vs continuous equations of state in the software.
- **Mesh fidelity** — if any component is spatially resolved (CFD-type), a coarse mesh shifts the exit state.
- **Component efficiencies** — 100 % isentropic by hand vs a realistic value in the model.

Assessment is on **which idealisation matters most and why** — not on getting a "right answer".

### Discussion questions ·T5 p8

1. ANSYS gives lower $\eta$ than the hand calculation: two plausible causes, and which matters more here?
2. Lower the condenser pressure — what happens to turbine-exit quality? Explain with the Mollier chart and say what you would look for in ANSYS.
3. Why would a plant designer value the parametric sweep more than the single-point match?

[added] (2) Quality **falls** — the expansion line goes further down into the dome (this is the side effect
on ·VC s8, `06` §6.5).

---

## Lab report structure ·T5 p8

1. **Objective** — one or two sentences.
2. **Theory** — governing equations, symbols defined.
3. **Apparatus and procedure** — concise, not copied from the sheet.
4. **Results** — raw data table, then calculated values.
5. **Error analysis** — % error against accepted value; main error sources.
6. **Discussion and conclusion** — answer the discussion questions; what was learned.

References ·T5 p8: Cengel & Boles; Incropera & DeWitt; steam tables / Mollier chart "as prescribed for
MEC 3105"; ANSYS Help.

---

### Verification notes for this section

| ID | Page | Issue |
|---|---|---|
| **C37** | p4 | numerator printed 3118.6; $0.162 \times 4186 \times 4.6 = 3119.4$. Answer 876 unaffected |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
