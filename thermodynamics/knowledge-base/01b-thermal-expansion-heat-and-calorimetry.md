---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "01b — Thermal Expansion, Heat, Calorimetry and Heat Transfer Basics"
source: "TT2 — 'Temperature and Thermometry 2.pdf', 52 pages (printed footers 18–69)"
pages: "18-69"
file_role: topic
subtopics:
  - "thermal expansion of solids: linear, area, volume"
  - "the unusual behaviour of water near 4 °C"
  - "heat vs internal energy; the calorie"
  - "specific heat and Q = mcΔT"
  - "calorimetry: two bodies, then three or more (ΣQ = 0)"
  - "latent heat and phase change; the ice-to-steam curve"
  - "energy transfer: conduction, convection, radiation (introductory)"
key_equations: [linear-expansion, area-expansion, volume-expansion, specific-heat, calorimetry, sum-q-zero, latent-heat, conduction-rod, stefan, net-radiation]
prerequisites: ["01-temperature-thermometry"]
leads_to: ["02-first-law", "07-heat-transfer-and-thermal-analysis", "09-heat-transfer-experiments"]
verification_flags: 5
tags: [thermal-expansion, specific-heat, calorimetry, latent-heat, phase-change, conduction, convection, radiation, sign-loss]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [eq] key equation · [ex] worked example (with the lecturer's numbers) ·
  [exercise] unsolved problem set · [fig] figure described from the rendered page ·
  [added] supplied here, NOT in the source · ·TT2 pN = provenance (printed footer page) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md. -->

# 01b — Thermal Expansion, Heat, Calorimetry and Heat Transfer Basics

Scope: the whole of TT2, the second half of the Temperature and Thermometry notes. Its printed page
numbers carry straight on from TT (which ends at 17): TT2 starts at **18**.

> **Citations use the printed footer.** `·TT2 p40` is the page whose footer reads 40 — **PDF page 23**.
> PDF page = footer − 17.

> ### ⚠ Read this before using any number in this document — V29
>
> TT2 was converted from a textbook layout, and **most minus signs came out as the digit 2**. The page
> says "ice at 230 °C" where it means **−30 °C**. Every case is listed in V29 and corrected below. The
> equation images themselves are fine — the damage is in the typed text.

> **Numbering.** The document's own headings jump: **1.2** → **1.3 Thermal Energy** → **3.1** → **3.3**
> (no 3.2). This file keeps them as printed. It is all Topic 1 material.

---

## 1b.1 Thermal expansion of solids ·TT2 p18–p21

**Why it happens.** Atoms in a solid vibrate about fixed positions (amplitude $\sim 10^{-11}\ \mathrm{m}$,
spacing $\sim 10^{-10}\ \mathrm{m}$). Hotter → bigger vibrations → bigger average spacing → the whole
solid expands. ·TT2 p18–p19

| Symbol | Meaning | Units |
|---|---|---|
| $L_0$, $A_0$, $V_0$ | original length, area, volume | $\mathrm{m}$, $\mathrm{m^2}$, $\mathrm{m^3}$ |
| $\Delta T$ | temperature change | $^\circ\mathrm{C}$ or $\mathrm{K}$ |
| $\alpha$ | coefficient of **linear** expansion | $(^\circ\mathrm{C})^{-1}$ |
| $\gamma$ | coefficient of **area** expansion, $\gamma = 2\alpha$ | $(^\circ\mathrm{C})^{-1}$ |
| $\beta$ | coefficient of **volume** expansion | $(^\circ\mathrm{C})^{-1}$ |

> ⚠ **$\gamma$ here is not $c_p/c_v$** (`02-first-law`), and **$\beta$ here is not anything in Topic 4**.
> See `_nomenclature.md`.

[eq] Linear expansion — Equation (4) ·TT2 p19

$$
\Delta L = \alpha L_0\,\Delta T
$$

$$
L - L_0 = \alpha L_0 (T - T_0)
$$

[derivation] Area — square of side $L_0$ ·TT2 p20

$$
L = L_0 + \alpha L_0\,\Delta T
$$

$$
A = L^2 = L_0^2 + 2\alpha L_0^2\,\Delta T + \alpha^2 L_0^2 (\Delta T)^2
$$

The last term is dropped because $\alpha\Delta T \ll 1$:

$$
A = A_0 + 2\alpha A_0\,\Delta T
$$

[eq] Equation (5)

$$
\Delta A = A - A_0 = \gamma A_0\,\Delta T, \qquad \gamma = 2\alpha
$$

[eq] Equation (6) — volume

$$
\Delta V = \beta V_0\,\Delta T
$$

[added] For a solid, $\beta \approx 3\alpha$ — the notes use exactly this in Example 3(b) (divide $\beta$ by 3).

### Table 1 — expansion coefficients ·TT2 p21

| Material | $\alpha\ [(^\circ\mathrm{C})^{-1}]$ | Material | $\beta\ [(^\circ\mathrm{C})^{-1}]$ |
|---|---|---|---|
| Aluminium | $24 \times 10^{-6}$ | Acetone | $1.5 \times 10^{-4}$ |
| Brass and bronze | $19 \times 10^{-6}$ | Benzene | $1.24 \times 10^{-4}$ |
| Concrete | $12 \times 10^{-6}$ | Ethyl alcohol | $1.12 \times 10^{-4}$ |
| Copper | $17 \times 10^{-6}$ | Gasoline | $9.6 \times 10^{-4}$ |
| Glass (ordinary) | $9 \times 10^{-6}$ | Glycerin | $4.85 \times 10^{-4}$ |
| Glass (Pyrex) | $3.2 \times 10^{-6}$ | Mercury | $1.82 \times 10^{-4}$ |
| Invar (Ni-Fe) | $0.9 \times 10^{-6}$ | Turpentine | $9.0 \times 10^{-4}$ |
| Lead | $29 \times 10^{-6}$ | Air at $0\ ^\circ\mathrm{C}$ | $3.67 \times 10^{-3}$ |
| Steel | $11 \times 10^{-6}$ | Helium | $3.665 \times 10^{-3}$ |

Gas values assume expansion at constant pressure.

### Applications ·TT2 p22–p23

1. **Pyrex glass** — $\alpha$ about one-third of ordinary glass, so smaller thermal stress when hot liquid is poured in.
2. **Bimetallic strip / thermostat** — brass expands more than steel; the bonded strip bends and makes or breaks a contact.
3. **Rising sea levels** — about half the expected rise comes from thermal expansion of water.

### [ex] Example 2 — steel rail ·TT2 p23

A steel track is $30\ \mathrm{m}$ long at $0\ ^\circ\mathrm{C}$. Length at $40\ ^\circ\mathrm{C}$?

$$
\Delta L = \alpha L_0 \Delta T = (11 \times 10^{-6})(30.0)(40.0) = 0.013\ \mathrm{m}
$$

$$
L = L_0 + \Delta L = 30.013\ \mathrm{m}
$$

### Questions ·TT2 p24

1. What happens to the tension of piano wires when the temperature falls?
2. For a very sensitive glass thermometer, which fluid: (a) mercury (b) alcohol (c) gasoline (d) glycerin?
3. Two spheres, same metal and radius, one hollow, one solid, same temperature rise — which expands more?

[added] Answers: (1) tension rises — the wire tries to shorten between fixed ends. (2) gasoline — largest
$\beta$ in Table 1 ($9.6 \times 10^{-4}$). (3) (c) the same — a hole expands as if it were filled with the
same material.

### [ex] Example 3 — Earth's oceans ·TT2 p24–p25

$\beta_{water} = 2.07 \times 10^{-4}\ (^\circ\mathrm{C})^{-1}$, $\Delta T = 1\ ^\circ\mathrm{C}$, mean depth $4000\ \mathrm{m}$.

(a) Fractional volume change:

$$
\frac{\Delta V}{V_0} = \beta\,\Delta T = (2.07 \times 10^{-4})(1) \approx 2 \times 10^{-4}
$$

(b) Depth change, using $\alpha = \beta/3$:

$$
\Delta L = \left(\frac{\beta}{3}\right) L_0\,\Delta T = (6.90 \times 10^{-5})(4000)(1) \approx 0.3\ \mathrm{m}
$$

### The unusual behaviour of water ·TT2 p25–p27

- From $0$ to $4\ ^\circ\mathrm{C}$ water **contracts** as it warms; above $4\ ^\circ\mathrm{C}$ it expands normally.
- Maximum density $1000\ \mathrm{kg/m^3}$ at $4\ ^\circ\mathrm{C}$ [fig 7, density vs temperature].
- A pond freezes **from the top down**: above $4\ ^\circ\mathrm{C}$ cooled surface water sinks (upwelling);
  below $4\ ^\circ\mathrm{C}$ it stays on top and freezes. Ice floats and insulates; the bottom stays at $4\ ^\circ\mathrm{C}$.

### [exercise] Problems ·TT2 p28

| # | Problem | Printed answer | Corrected reading |
|---|---|---|---|
| 1 | Body temperature $98.6\ ^\circ\mathrm{F} \to 107\ ^\circ\mathrm{F}$: convert to °C and K, find the differences | "37.08C, 41.78C, 4.78C; 310.2 K, 314.9 K, 4.7 K" | $37.0$, $41.7$, $4.7\ ^\circ\mathrm{C}$ — the "8" is a lost degree sign |
| 2 | Example 2's rail at $0\ ^\circ\mathrm{F}$ | $29.994\ \mathrm{m}$ | ✅ correct ($0\ ^\circ\mathrm{F} = -17.8\ ^\circ\mathrm{C}$) |
| 3 | Steel ring, hole $3.99\ \mathrm{cm^2}$; aluminium rod $4.00\ \mathrm{cm^2}$; both at $35\ ^\circ\mathrm{C}$. At what common temperature does the ring slip on? | "261 °C" | ⚠ **$-61\ ^\circ\mathrm{C}$ — cool both, don't heat. V30** |

[added] Problem 3 working. Use area expansion on both, $\gamma = 2\alpha$:

$$
3.99\,(1 + 2\alpha_{steel}\Delta T) = 4.00\,(1 + 2\alpha_{Al}\Delta T)
$$

$$
3.99 - 4.00 = \Delta T\,\big(4.00 \times 48 \times 10^{-6} - 3.99 \times 22 \times 10^{-6}\big)
$$

$$
\Delta T = \frac{-0.01}{1.042 \times 10^{-4}} = -96\ ^\circ\mathrm{C}
$$

$$
T = 35 - 96 = -61\ ^\circ\mathrm{C}
$$

Aluminium shrinks faster than steel, so cooling closes the gap. Heating would widen it.

---

## 1b.2 Heat and internal energy ·TT2 p29–p31

- [def] **Internal energy $U$** — energy of the atoms and molecules: random translational, rotational and
  vibrational KE plus intermolecular PE. For a monatomic ideal gas it is translational KE only.
- [def] **Heat** — "the transfer of energy between a system and its environment due to a temperature
  difference between them." Symbol $Q$.
- A body does not *contain* heat, just as it does not contain work.
- [hist] Joule (1818–1889): lost mechanical energy of an isolated system = gain in internal energy.

### Units of heat ·TT2 p32

[def] The calorie: energy to raise $1\ \mathrm{g}$ of water from $14.5$ to $15.5\ ^\circ\mathrm{C}$. A food
"Calorie" is a kilocalorie.

[eq] Equation (1) — mechanical equivalent of heat

$$
1\ \mathrm{cal} \equiv 4.186\ \mathrm{J}
$$

Application (p33): exercise — about three-quarters of the body's energy use leaves as heat.

---

## 1b.3 Specific heat ·TT2 p33–p37

| Symbol | Meaning | Units |
|---|---|---|
| $Q$ | energy transferred by heat | $\mathrm{J}$ |
| $m$ | mass | $\mathrm{kg}$ |
| $c$ | specific heat | $\mathrm{J/(kg\,^\circ C)}$ |
| $\Delta T = T_f - T_i$ | temperature change | $^\circ\mathrm{C}$ |

[eq] Equation (2) — definition

$$
c \equiv \frac{Q}{m\,\Delta T}
$$

[eq] Equation (3)

$$
Q = m c\,\Delta T
$$

Sign rule: $\Delta T > 0 \Rightarrow Q > 0$, energy **in**. $\Delta T < 0 \Rightarrow Q < 0$, energy **out**.

[ex] $0.5\ \mathrm{kg}$ of water raised $3\ ^\circ\mathrm{C}$ ·TT2 p34:

$$
Q = (0.5)(4186)(3) = 6.28 \times 10^{3}\ \mathrm{J}
$$

### Specific heats ·TT2 p35 (Table 1), repeated as Table 2 on p37 (C29)

| Substance | $\mathrm{J/(kg\,^\circ C)}$ | Substance | $\mathrm{J/(kg\,^\circ C)}$ |
|---|---|---|---|
| Aluminium | 900 | Ice | 2090 |
| Beryllium | 1820 | Iron | 448 |
| Cadmium | 230 | Lead | 128 |
| Copper | 387 | Mercury | 138 |
| Ethyl alcohol | 2430 | Silicon | 703 |
| Germanium | 322 | Silver | 234 |
| Glass | 837 | Steam | 2010 |
| Gold | 129 | Tin | 227 |
| Human tissue | 3470 | **Water** | **4186** |

### Applications ·TT2 p36–p38

1. Water's high $c$ moderates climate near large bodies of water. ⚠ The page prints "186 J/kg·°C" — the
   leading 4 is lost (V31). It is **4186**.
2. Sea breeze: sand (low $c$) heats faster than water; hot air over land rises, cool air flows in from
   the sea [fig 1].

---

## 1b.4 Calorimetry ·TT2 p38–p43

[def] A **calorimeter** is an insulated vessel; the system inside is treated as isolated.

[eq] Equation (4) — two bodies

$$
Q_{cold} = -Q_{hot}
$$

$Q_{cold} > 0$ (energy in), $Q_{hot} < 0$ (energy out); the minus sign makes the right side positive.

### [ex] Example 1 — unknown specific heat ·TT2 p40

$125\ \mathrm{g}$ block at $90\ ^\circ\mathrm{C}$ into $0.326\ \mathrm{kg}$ water at $20\ ^\circ\mathrm{C}$; equilibrium $22.4\ ^\circ\mathrm{C}$; cup neglected.

$$
m_w c_w (T - T_w) = -m_x c_x (T - T_x)
$$

$$
c_x = \frac{m_w c_w (T - T_w)}{m_x (T_x - T)}
$$

$$
c_x = \frac{(0.326)(4190)(22.4 - 20.0)}{(0.125)(90.0 - 22.4)}
$$

$$
c_x = 388\ \mathrm{J/(kg\,^\circ C)} \approx 390\ \mathrm{J/(kg\,^\circ C)}
$$

Note the example uses $c_w = 4190$, the table $4186$ — immaterial here.

### Three or more bodies — Equation (5) ·TT2 p41–p42

With three bodies you may not know which way the middle one goes. Write every term as
$Q = mc(T_f - T_i)$ and let the signs sort themselves out:

$$
\sum Q_k = 0
$$

### [ex] Example 2 — water, glass, aluminium ·TT2 p42–p43

$0.4\ \mathrm{kg}$ water at $40\ ^\circ\mathrm{C}$; $0.3\ \mathrm{kg}$ glass beaker at $25\ ^\circ\mathrm{C}$; $0.5\ \mathrm{kg}$ aluminium at $37\ ^\circ\mathrm{C}$; insulated.

| $Q$ | $m$ (kg) | $c$ | $T_f$ | $T_i$ |
|---|---|---|---|---|
| $Q_w$ | 0.400 | 4190 | $T$ | 40.0 |
| $Q_{al}$ | 0.500 | 900 | $T$ | 37.0 |
| $Q_g$ | 0.300 | 837 | $T$ | 25.0 |

$$
m_w c_w (T - T_w) + m_{al} c_{al} (T - T_{al}) + m_g c_g (T - T_g) = 0
$$

$$
(1.68 \times 10^{3})(T - 40.0) + (4.50 \times 10^{2})(T - 37.0) + (2.51 \times 10^{2})(T - 25.0) = 0
$$

$$
(1.68 \times 10^{3} + 4.50 \times 10^{2} + 2.51 \times 10^{2})\,T = 9.01 \times 10^{4}
$$

$$
T = 37.9\ ^\circ\mathrm{C}
$$

---

## 1b.5 Latent heat and phase change ·TT2 p44–p52

[def] During a phase change, energy goes into internal energy with **no change in temperature**.

| Symbol | Meaning | Units |
|---|---|---|
| $L$ | latent heat | $\mathrm{J/kg}$ |
| $L_f$ | latent heat of fusion (melting/freezing) | $\mathrm{J/kg}$ |
| $L_v$ | latent heat of vaporisation (boiling/condensing) | $\mathrm{J/kg}$ |

[eq] Equation (6)

$$
Q = \pm m L
$$

$+$ when energy is absorbed (melting, boiling); $-$ when removed (freezing, condensing).

Water at 1 atm: $L_f = 3.33 \times 10^{5}\ \mathrm{J/kg}$, $L_v = 2.26 \times 10^{6}\ \mathrm{J/kg}$.
Sublimation: solid straight to gas (dry ice) — its own latent heat.

### Table 3 — latent heats ·TT2 p46

| Substance | Melting pt (°C) | $L_f$ (J/kg) | Boiling pt (°C) | $L_v$ (J/kg) |
|---|---|---|---|---|
| Helium | −269.65 | $5.23 \times 10^{3}$ | −268.93 | $2.09 \times 10^{4}$ |
| Nitrogen | −209.97 | $2.55 \times 10^{4}$ | −195.81 | $2.01 \times 10^{5}$ |
| Oxygen | −218.79 | $1.38 \times 10^{4}$ | −182.97 | $2.13 \times 10^{5}$ |
| Ethyl alcohol | −114 | $1.04 \times 10^{5}$ | 78 | $8.54 \times 10^{5}$ |
| Water | 0.00 | $3.33 \times 10^{5}$ | 100.00 | $2.26 \times 10^{6}$ |
| Sulfur | 119 | $3.81 \times 10^{4}$ | 444.60 | $3.26 \times 10^{5}$ |
| Lead | 327.3 | $2.45 \times 10^{4}$ | 1750 | $8.70 \times 10^{5}$ |
| Aluminium | 660 | $3.97 \times 10^{5}$ | 2450 | $1.14 \times 10^{7}$ |
| Silver | 960.80 | $8.82 \times 10^{4}$ | 2193 | $2.33 \times 10^{6}$ |
| Gold | 1063.00 | $6.44 \times 10^{4}$ | 2660 | $1.58 \times 10^{6}$ |
| Copper | 1083 | $1.34 \times 10^{5}$ | 1187 | $5.06 \times 10^{6}$ |

### [ex] Ice at −30 °C to steam at 120 °C — Figure 2 ·TT2 p45–p49

$1.00\ \mathrm{g}$ of ice at **$-30\ ^\circ\mathrm{C}$** (printed "230 °C" — V29). [fig] Temperature vs energy
added: A (ice warms) → B (melts, flat at 0) → C (water warms) → D (boils, flat at 100) → E (steam warms).
Break points on the energy axis: 62.7, 396, 815, 3070, 3110 J.

Part A — ice $-30 \to 0\ ^\circ\mathrm{C}$:

$$
Q = m c_{ice} \Delta T = (1.00 \times 10^{-3})(2090)(30.0) = 62.7\ \mathrm{J}
$$

Part B — melt:

$$
Q = m L_f = (1.00 \times 10^{-3})(3.33 \times 10^{5}) = 333\ \mathrm{J}
$$

Part C — water $0 \to 100\ ^\circ\mathrm{C}$:

$$
Q = m c_{water} \Delta T = (1.00 \times 10^{-3})(4.19 \times 10^{3})(100) = 4.19 \times 10^{2}\ \mathrm{J}
$$

Part D — boil:

$$
Q = m L_v = (1.00 \times 10^{-3})(2.26 \times 10^{6}) = 2.26 \times 10^{3}\ \mathrm{J}
$$

Part E — steam $100 \to 120\ ^\circ\mathrm{C}$:

$$
Q = m c_{steam} \Delta T = (1.00 \times 10^{-3})(2.01 \times 10^{3})(20.0) = 40.2\ \mathrm{J}
$$

Total:

$$
Q_{total} = 62.7 + 333 + 419 + 2260 + 40.2 = 3.11 \times 10^{3}\ \mathrm{J}
$$

The same $3.11 \times 10^{3}\ \mathrm{J}$ must be removed to go back.

Molecular picture (p49–p50): $L_v$ is the work to pull liquid molecules apart; $L_f$ is the work to move
atoms from the ordered solid into the disordered liquid.

### [ex] Example 3 — ice into a cooler ·TT2 p50–p51

$6\ \mathrm{kg}$ of ice at **$-5.00\ ^\circ\mathrm{C}$** (printed "25 °C" — V29; the table on the same page
shows $-5.00$) into $30\ \mathrm{L}$ of water at $20\ ^\circ\mathrm{C}$.

$$
m_{water} = \rho V = (1.00 \times 10^{3})(30.0 \times 10^{-3}) = 30.0\ \mathrm{kg}
$$

$$
Q_{ice} + Q_{melt} + Q_{ice\text{-}water} + Q_{water} = 0
$$

| $Q$ | $m$ | $c$ | $L$ | $T_f$ | $T_i$ | Expression |
|---|---|---|---|---|---|---|
| $Q_{ice}$ | 6.00 | 2090 | | 0 | −5.00 | $m_{ice}c_{ice}(T_f - T_i)$ |
| $Q_{melt}$ | 6.00 | | $3.33 \times 10^{5}$ | 0 | 0 | $m_{ice}L_f$ |
| $Q_{ice\text{-}water}$ | 6.00 | 4190 | | $T$ | 0 | $m_{ice}c_{water}(T_f - T_i)$ |
| $Q_{water}$ | 30.0 | 4190 | | $T$ | 20.0 | $m_{water}c_{water}(T_f - T_i)$ |

$$
6.27 \times 10^{4} + 2.00 \times 10^{6} + (2.51 \times 10^{4})(T - 0) + (1.26 \times 10^{5})(T - 20.0) = 0
$$

$$
T = 3.03\ ^\circ\mathrm{C}
$$

([added] with unrounded coefficients $T = 3.01\ ^\circ\mathrm{C}$ — rounding only.)

### [ex] Example 4 — not all the ice melts ·TT2 p51–p52

$5.00\ \mathrm{kg}$ ice at $0\ ^\circ\mathrm{C}$ into $10\ \mathrm{kg}$ water at $15\ ^\circ\mathrm{C}$, insulated.

Energy to melt all the ice:

$$
Q_{melt} = m_{ice} L_f = (5.00)(3.33 \times 10^{5}) = 1.67 \times 10^{6}\ \mathrm{J}
$$

Most the water can give up before it starts to freeze:

$$
Q_{water} = (10.0)(4190)(0 - 15.0) = -6.29 \times 10^{5}\ \mathrm{J}
$$

$6.29 \times 10^{5} < 1.67 \times 10^{6}$, so (a) the mix ends as ice + water at $T = 0\ ^\circ\mathrm{C}$.

(b) Ice melted:

$$
6.29 \times 10^{5} = m L_f = m\,(3.33 \times 10^{5})
$$

$$
m = 1.89\ \mathrm{kg}
$$

**Method to keep:** when ice meets water, first check whether the water has enough energy to melt it all.

---

## 1b.6 Energy transfer: conduction, convection, radiation ·TT2 p52–p68

The introductory version. Topic 4 (`07-heat-transfer-and-thermal-analysis`) does the same three
mechanisms properly, with resistances.

### Conduction ·TT2 p53–p56

- Atomic picture: faster particles pass KE to slower ones by collision. Metals conduct well because of
  free electrons. Gases conduct poorly.
- A slab of thickness $\Delta x$, area $A$, faces at $T_h$ and $T_c$ with **$T_h > T_c$** (printed
  "$T_h - T_c$" — V29).

| Symbol | Meaning | Units |
|---|---|---|
| $P = Q/\Delta t$ | rate of energy transfer | $\mathrm{W}$ |
| $\Delta T/\Delta x$ | temperature gradient | $\mathrm{K/m}$ |
| $k$ | thermal conductivity | $\mathrm{J/(s\,m\,^\circ C)} = \mathrm{W/(m\,K)}$ |
| $L$ | rod length | $\mathrm{m}$ |

$$
P = \frac{Q}{\Delta t} \propto A\,\frac{\Delta T}{\Delta x}
$$

For an insulated rod at steady state, $\Delta T/\Delta x = (T_h - T_c)/L$:

[eq] Equation (7)

$$
P = kA\,\frac{T_h - T_c}{L}
$$

[fig 3] "In which case is the rate larger?" — two rods in series (a) vs in parallel (b). [added] Parallel
(b): each rod sees the full $T_h - T_c$ over a shorter path, so more flows.

Table 4 — $k$ in W/(m·K) ·TT2 p56: Al 238 · Cu 397 · Au 314 · Fe 79.5 · Pb 34.7 · Ag 427 ·
air 0.0234 · He 0.138 · H₂ 0.172 · N₂ 0.0234 · O₂ 0.0238 · asbestos 0.08 · concrete 0.8 · glass 0.8 ·
ice 2 · rubber 0.2 · water 0.6 · wood 0.08.

> Note Cu is 397 here and 385 in Topic 4 (·HT p2) — different sources, both fine.

### Convection ·TT2 p57–p60

- [def] "The transfer of energy by the movement of a substance."
- **Natural** convection — driven by density differences (fire, beach breeze).
- **Forced** convection — driven by a fan or pump.
- Applications: kettle; room radiator [fig 5]; car engine cooling (conduction into the coolant, forced
  convection to the radiator); body fat, feathers and wool trap low-$k$ air.

### Radiation ·TT2 p61–p68

| Symbol | Meaning | Units |
|---|---|---|
| $P$ | power radiated | $\mathrm{W}$ |
| $\sigma$ | Stefan–Boltzmann constant, $5.67 \times 10^{-8}$ | $\mathrm{W/(m^2\,K^4)}$ |
| $e$ | emissivity, $0 \le e \le 1$ | — |
| $T$, $T_0$ | body and surroundings temperature, **kelvin** | $\mathrm{K}$ |

> ⚠ TT2 writes emissivity as **$e$**; Topic 4 writes **$\varepsilon$**. Same quantity.

[eq] Equation (8) — Stefan's law

$$
P = \sigma A e T^{4}
$$

[eq] Equation (9) — net exchange with surroundings

$$
P_{net} = \sigma A e\,(T^{4} - T_0^{4})
$$

- About $1370\ \mathrm{J}$ of solar radiation crosses each $\mathrm{m^2}$ at the top of the atmosphere every second.
- **Black body**: ideal absorber and ideal emitter, $e = 1$. **Ideal reflector**: $e = 0$.
- Applications: light-coloured clothing; thermography; ear (infrared) thermometers; thermal night vision;
  the greenhouse and greenhouse effect.

### [exercise] Problems ·TT2 p69

| # | Problem (corrected) | Printed answer | Check |
|---|---|---|---|
| 1 | Steel strut, area **$5 \times 10^{-4}\ \mathrm{m^2}$** (printed "$5 \times 10^{24}$" — V29), length $2.5\ \mathrm{m}$, density as iron; absorbs $3 \times 10^{5}\ \mathrm{J}$. Find $\Delta T$ | $68.2\ ^\circ\mathrm{C}$ | ✅ with $\rho = 7860$, $c = 448$ |
| 2 | $255\ \mathrm{g}$ gold at $85.0\ ^\circ\mathrm{C}$ into $155\ \mathrm{g}$ water at $25.0\ ^\circ\mathrm{C}$; cup neglected | $27.9\ ^\circ\mathrm{C}$ | ✅ |
| 3 | $20.0\ \mathrm{kg}$ gold at $35.0$, $0.800\ \mathrm{kg}$ glass at $15.0$, $2.00\ \mathrm{kg}$ water at $25.0\ ^\circ\mathrm{C}$ | $26.6\ ^\circ\mathrm{C}$ | ✅ |
| 4 | $8.00\ \mathrm{kg}$ ice at **$-5.00\ ^\circ\mathrm{C}$** (printed "25.00") into $12.0\ \mathrm{kg}$ water at $20.0\ ^\circ\mathrm{C}$. Final $T$? Ice left? | "T = 5 0 °C; 5.23 kg" | ✅ **$T = 0\ ^\circ\mathrm{C}$**, $5.23\ \mathrm{kg}$ left |

[added] Problem 1 working:

$$
m = \rho A L = (7860)(5 \times 10^{-4})(2.5) = 9.83\ \mathrm{kg}
$$

$$
\Delta T = \frac{Q}{mc} = \frac{3 \times 10^{5}}{(9.83)(448)} = 68.2\ ^\circ\mathrm{C}
$$

[added] Problem 4 working — water can give $12.0 \times 4186 \times 20 = 1.005 \times 10^{6}\ \mathrm{J}$ before
freezing; warming the ice to 0 takes $8.00 \times 2090 \times 5 = 8.36 \times 10^{4}\ \mathrm{J}$; the rest melts

$$
m = \frac{1.005 \times 10^{6} - 8.36 \times 10^{4}}{3.33 \times 10^{5}} = 2.77\ \mathrm{kg}
$$

so $8.00 - 2.77 = 5.23\ \mathrm{kg}$ of ice remains, at $0\ ^\circ\mathrm{C}$.

---

### Verification notes for this section

| ID | Page | Issue |
|---|---|---|
| **V29** | p23–p69 | minus signs printed as "2" throughout (−30 → "230", −5.00 → "25.00", $10^{-4}$ → "$10^{24}$", $T_h > T_c$ → "$T_h - T_c$"); degree sign printed as "8" in p28 answers |
| **V30** | p28 | Problem 3 answer "261 °C" is **−61 °C** — the ring goes on by cooling, not heating |
| **V31** | p36 | specific heat of water printed "186 J/kg·°C" — is 4186 |
| **C29** | p35, p37 | Tables 1 and 2 are the same table printed twice; Table 1 caption has "J/kg?°C" |
| **C30** | p29–p38 | heading numbers jump 1.2 → 1.3 → 3.1 → 3.3 |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
