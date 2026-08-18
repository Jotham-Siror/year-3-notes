---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
file_role: formula-sheet
source: "Built incrementally, one lecture document per stage. Covers all five lecture documents."
coverage: "ALL FIVE lecture documents — 200 / 200. Group activities pending."
tags: [formula-sheet, equations, temperature, conversions, first-law, work, heat, equations-of-state]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Formula sheet — MEC 3105

Every equation in the course, **in corrected form**, tagged to its source page and to the topic file
that derives it. Where a source page prints a defective form, the corrected form is given here and the
defect is flagged — never silently fixed.

> **Build status.** Covers **all five lecture documents**. One section is added per build stage.
> Numbering in the *Eq.* column is **the lecturer's own**, so it can be quoted back in an exam.
>
> **⚠ Sign convention.** Every first-law equation on this sheet is written in **one** convention —
> $\Delta U = Q - W$, $W>0$ for work done **by** the system — because that is what the assessed
> exercises use. FL itself switches convention mid-deck; see `_nomenclature.md` clash 1 before
> reading any equation off a slide.

---

## §1.1 Temperature and thermometry ·TT

All four of TT's equations. All four verified sound; the corrections in this topic surround them, not
inside them.

| Eq. | Tag | Equation | Page |
|---|---|---|---|
| 1 | `celsius-kelvin` | $T_C = T - 273.15$ | ·TT p13 |
| 2a | `fahrenheit-from-celsius` | $T_F = \tfrac95 T_C + 32$ | ·TT p15 |
| 2b | `celsius-from-fahrenheit` | $T_C = \tfrac59\left(T_F - 32\right)$ | ·TT p15 |
| 3 | `delta-fahrenheit-celsius` | $\Delta T_F = \tfrac95 \Delta T_C$ | ·TT p15 |

### Equation 1 — Celsius from Kelvin ·TT p13

$$\boxed{\;T_C = T - 273.15\;}\qquad\Longleftrightarrow\qquad \boxed{\;T = T_C + 273.15\;}$$

- $T_C$ — Celsius temperature, $^\circ\mathrm{C}$
- $T$ — Kelvin (absolute) temperature, $\mathrm{K}$

TT's note on units: strictly $T_C = T\,(^\circ\mathrm{C}/\mathrm{K}) - 273.15\ ^\circ\mathrm{C}$;
the units are suppressed during calculation and restored in the final answer. ·TT p13

**Absolute zero:** $0\ \mathrm{K} = -273.15\ ^\circ\mathrm{C}$.
⚠ **V1, V2** — TT p13 prints this as $273.15\ ^\circ\mathrm{C}$, minus sign absent from the page.

### Equation 2a — Fahrenheit from Celsius ·TT p15

$$\boxed{\;T_F = \tfrac{9}{5}\,T_C + 32\;}$$

- $\tfrac95 = 1.8$ — ratio of degree sizes ($180\ \mathrm{F}^\circ$ per $100\ \mathrm{C}^\circ$)
- $32$ — the ice point on the Fahrenheit scale

### Equation 2b — Celsius from Fahrenheit ·TT p15

$$\boxed{\;T_C = \tfrac{5}{9}\left(T_F - 32\right)\;}$$

The exact inverse of 2a. **The bracket is not optional** — subtract the offset before scaling.
Check: $T_F = 32 \Rightarrow T_C = 0$ exactly.

### Equation 3 — differences between the Fahrenheit and Celsius scales ·TT p15

$$\boxed{\;\Delta T_F = \tfrac{9}{5}\,\Delta T_C\;}\qquad\Longleftrightarrow\qquad
\boxed{\;\Delta T_C = \tfrac{5}{9}\,\Delta T_F\;}$$

Follows from 2a by differencing: the $+32$ offset is identical at both temperatures and cancels, so
only the scale factor survives.

### [added] The Kelvin–Celsius difference identity

Not written as a numbered equation in TT, but stated in words on p14 ("the size of a Celsius degree is
the same as a kelvin… the two scales differ only in the choice of zero point") and **required** by
Example 1:

$$\boxed{\;\Delta T = \Delta T_C\;}\qquad\text{exactly}$$

⚠ **V4** — TT p17 prints $\Delta T = 7\ \mathrm{K}$ where $\Delta T_C = 6.7\ ^\circ\mathrm{C}$,
violating this identity. The correct value is $\Delta T = 6.7\ \mathrm{K}$.

### [added] Extending a two-point calibration to any linear scale

The general form behind Equations 2a/2b, recoverable from the two fixed points alone (·TT p18 Q2):

$$T_{\text{new}} = \underbrace{\frac{T_{\text{new,steam}} - T_{\text{new,ice}}}{T_{\text{old,steam}} - T_{\text{old,ice}}}}_{\text{gradient} \;=\; \text{ratio of degree sizes}}\left(T_{\text{old}} - T_{\text{old,ice}}\right) + T_{\text{new,ice}}$$

For Celsius → Fahrenheit: gradient $= (212-32)/(100-0) = \tfrac95$, intercept $= 32$, giving
Equation 2a. Worth knowing because it removes the need to memorise either conversion, and it handles
any invented scale a question cares to define.

---

## Quick-reference conversions ·TT p9, p14–p15

| From → To | Use |
|---|---|
| $^\circ\mathrm{C} \to \mathrm{K}$ | $T = T_C + 273.15$ |
| $\mathrm{K} \to {}^\circ\mathrm{C}$ | $T_C = T - 273.15$ |
| $^\circ\mathrm{C} \to {}^\circ\mathrm{F}$ | $T_F = \tfrac95 T_C + 32$ |
| $^\circ\mathrm{F} \to {}^\circ\mathrm{C}$ | $T_C = \tfrac59(T_F - 32)$ |
| $\mathrm{K} \to {}^\circ\mathrm{F}$ | $T_F = \tfrac95(T - 273.15) + 32$ |
| $^\circ\mathrm{F} \to \mathrm{K}$ | $T = \tfrac59(T_F - 32) + 273.15$ |
| **difference** $\mathrm{C}^\circ \leftrightarrow \mathrm{K}$ | $\Delta T = \Delta T_C$ — **equal** |
| **difference** $\mathrm{C}^\circ \to \mathrm{F}^\circ$ | $\Delta T_F = \tfrac95 \Delta T_C$ |

The last two rows are the ones examined. Converting a *difference* as though it were a *temperature*
is the standard trap.

### Fixed points, all three scales ·TT p9, p14

| | Celsius | Kelvin | Fahrenheit |
|---|---|---|---|
| Absolute zero | $-273.15\ ^\circ\mathrm{C}$ | $0\ \mathrm{K}$ | $-459.67\ ^\circ\mathrm{F}$ *[added]* |
| Ice point | $0\ ^\circ\mathrm{C}$ | $273.15\ \mathrm{K}$ | $32\ ^\circ\mathrm{F}$ |
| Triple point of water | $0.01\ ^\circ\mathrm{C}$ | $273.16\ \mathrm{K}$ | $32.018\ ^\circ\mathrm{F}$ *[added]* |
| Steam point | $100\ ^\circ\mathrm{C}$ | $373.15\ \mathrm{K}$ | $212\ ^\circ\mathrm{F}$ |

*The Fahrenheit column entries marked `[added]` do not appear in TT; computed from Equation 2a.*

---

## §1.3 Work, heat and the first law ·FL

> ### ⚠ Every equation below is written in **convention B** — $W > 0$ for work done **BY** the system
>
> $$\boxed{\;\Delta U = Q - W\;}$$
>
> This is the convention the **assessed exercises** use (GA2), and the one FL's second half uses.
> FL also states the opposite convention on s13; where a slide is written in that other convention
> (A, $\Delta U = Q + W$), it is marked. **Do not mix them** — see `_nomenclature.md` clash 1.

### First law, closed system ·FL s18

$$\boxed{\;\Delta \mathrm{KE} + \Delta \mathrm{PE} + \Delta U = Q - W\;}$$

Stationary system ($\Delta\mathrm{KE} = \Delta\mathrm{PE} = 0$) — **the form the exercises use**:

$$\boxed{\;\Delta U = Q - W\;}$$

Differential and rate forms:

$$dE = \delta Q - \delta W, \qquad \frac{dE}{dt} = \dot Q - \dot W$$

⚠ **V6** — FL s12 prints $Q = W + \Delta U$ in the middle of its *other* convention, where it should
read $Q = \Delta U - W$. ⚠ **V7** — FL s17 prints $E_1 + W_{1-2} - Q_{1-2} = E_2$; correct is
$E_1 + Q_{1-2} - W_{1-2} = E_2$.

### Energy balance ·FL s15–s16

$$\Delta E = \Delta U + \Delta\mathrm{KE} + \Delta\mathrm{PE}$$
$$\Delta U = m(u_2 - u_1),\quad \Delta\mathrm{KE} = \tfrac12 m(V_2^2 - V_1^2),\quad \Delta\mathrm{PE} = mg(z_2 - z_1)$$

⚠ **C3** — $V$ is **velocity** in $\Delta\mathrm{KE}$, volume everywhere else.

| Form | Equation | Units |
|---|---|---|
| Total | $E_{\text{in}} - E_{\text{out}} = \Delta E_{\text{system}}$ | kJ |
| Rate | $\dot E_{\text{in}} - \dot E_{\text{out}} = dE_{\text{system}}/dt$ | kW |
| Per unit mass | $e_{\text{in}} - e_{\text{out}} = \Delta e_{\text{system}}$ | kJ/kg |
| Differential | $\delta E_{\text{in}} - \delta E_{\text{out}} = dE_{\text{system}}$ | — |

**For a cycle** — the basis of all of Topic 3:

$$\boxed{\;W_{\text{net,out}} = Q_{\text{net,in}}\;}\qquad(\Delta E = 0)$$

### Boundary work ·FL s32–s33

$$\boxed{\;W_b = \int_1^2 P\,dV\;}\qquad
\delta W_b = F\,ds = PA\,ds = P\,dV$$

$W_b > 0$ expansion, $W_b < 0$ compression. $P$ is the pressure at the **inner face of the piston**.
Work is the **area under the process curve on a $P$–$V$ diagram**; the **enclosed area of a closed loop
is $W_{\text{net}}$ of the cycle**. Work is a **path function**: $\int_1^2 \delta W = W_{12}$, not
$\Delta W$.

Constant pressure: $W_b = P(V_2 - V_1) = P\,\Delta V$.
⚠ **V5** — FL s7 prints $W = P\Delta V$ for work done *on* the gas; that quantity is $-P\Delta V$.

### Enthalpy ·FL s21

$$\boxed{\;H = U + PV\;}\qquad\boxed{\;h = u + Pv\;}$$
$$\boxed{\;\Delta U + W_b = \Delta H\;}\qquad\boxed{\;Q - W_{\text{other}} = H_2 - H_1\;}$$

Constant pressure with no other work: $Q = \Delta H$.

### Mayer's relation ·FL s28

$$\boxed{\;C_P - C_V = R_u\;}\ \text{(molar)}\qquad
\boxed{\;c_p - c_v = R\;}\ \text{(mass-specific)}$$
$$\gamma \equiv \frac{C_P}{C_V} = 1 + \frac{R}{C_V}, \qquad \boxed{\;C_V = \frac{R}{\gamma-1}\;}$$

⚠ **C5** — FL s28 prints "$I + R/C_V$" (capital I for the digit 1).

### The four elementary ideal-gas processes ·FL s23–s28

**FL prints these in convention A** ($W$ = work **on**). Below they are converted to **convention B**
($W$ = work **by**) for consistency with the rest of this sheet — so every $W$ here is the **negative**
of FL's printed value. Molar quantities throughout.

| Process | Condition | $\Delta U$ | $Q$ | $W$ (by system) |
|---|---|---|---|---|
| **Isothermal** | $T$ const | $0$ | $R T\ln\dfrac{V_2}{V_1}$ | $R T\ln\dfrac{V_2}{V_1} = Q$ |
| **Isobaric** | $P$ const | $\int C_V\,dT$ | $\Delta H = \int C_P\,dT$ | $R(T_2 - T_1) = P\Delta V$ |
| **Isochoric** | $V$ const | $\int C_V\,dT$ | $\Delta U = \int C_V\,dT$ | $0$ |
| **Adiabatic** | $Q = 0$ | $C_V\Delta T$ | $0$ | $-C_V\Delta T = -\Delta U$ |

Isothermal also: $\Delta H = 0$, and $Q = -RT\ln(P_2/P_1)$.

### Adiabatic relations ·FL s26–s28

$$\boxed{\;PV^{\gamma} = \text{const},\qquad TV^{\gamma-1} = \text{const},\qquad
TP^{(1-\gamma)/\gamma} = \text{const}\;}$$

$$\frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{R/C_V}
= \left(\frac{P_2}{P_1}\right)^{R/C_P},\qquad
\frac{P_2}{P_1} = \left(\frac{V_1}{V_2}\right)^{\gamma}$$

Adiabatic work (FL's convention A, work **on** the gas — negate for work by):

$$W = C_V\,\Delta T = \frac{R\,\Delta T}{\gamma-1} = \frac{P_2V_2 - P_1V_1}{\gamma-1}$$

$$\boxed{\;W = \frac{P_1V_1}{\gamma-1}\left[\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} - 1\right]
= \frac{RT_1}{\gamma-1}\left[\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} - 1\right]\;}$$

### Polytropic index ·FL s29

$PV^{\delta} = $ const, with $\delta = 0$ isobaric, $\delta = 1$ isothermal, $\delta = \gamma$
adiabatic, $\delta = \infty$ isochoric.
⚠ **C6** — $\delta$ also means the inexact differential in this deck.

### General ideal-gas process relation ·FL s22

$$\boxed{\;dQ = C_V\,dT + P\,dV = C_V\,dT + RT\,\frac{dV}{V}\;}$$
$$\boxed{\;dQ = \left(C_v + R\right)dT - RT\,\frac{dP}{P}\;}$$

⚠ **V9** — s22's opening premises are in the other convention; these two results are correct in both.

### Joule equivalent ·FL s2

$$\boxed{\;1\ \mathrm{cal} = 4.184\ \mathrm{J}\;}$$

---

## §1.2 Equations of state ·FL s34–s37

### Ideal gas ·FL s34

$$\boxed{\;Pv = RT\;}\quad\text{(mass basis)}\qquad
\boxed{\;PV = mRT\;}\qquad\boxed{\;PV = nR_uT\;}\quad\text{(molar basis)}$$

$$\boxed{\;R = \frac{R_u}{M}\;}\qquad R_u = 8.31447\ \mathrm{kJ\,kmol^{-1}K^{-1}}$$

Other unit forms of $R_u$: $8.31447\ \mathrm{kPa\,m^3\,kmol^{-1}K^{-1}}$ ·
$0.0831447\ \mathrm{bar\,m^3\,kmol^{-1}K^{-1}}$ · $1.98588\ \mathrm{Btu\,lbmol^{-1}R^{-1}}$ ·
$10.7316\ \mathrm{psia\,ft^3\,lbmol^{-1}R^{-1}}$ · $1545.37\ \mathrm{ft\,lbf\,lbmol^{-1}R^{-1}}$.

Specific gas constants: Air 0.2870 · Helium 2.0769 · Argon 0.2081 · Nitrogen 0.2968 kJ·kg⁻¹K⁻¹.

### Compressibility factor ·FL s35–s36

$$\boxed{\;Pv = ZRT\;}\qquad Z = \frac{Pv}{RT} = \frac{v_{\text{actual}}}{v_{\text{ideal}}}$$

$Z = 1$ ideal; the farther from unity, the greater the deviation. Ideal behaviour at low density —
low $P$, high $T$, judged **relative to the critical point**.

$$P_R = \frac{P}{P_{cr}},\qquad T_R = \frac{T}{T_{cr}},\qquad
v_R = \frac{v_{\text{actual}}}{RT_{cr}/P_{cr}}$$

$Z$ from $(P_R, T_R)$ or $(P_R, v_R)$ on the generalised compressibility chart. Deviation is greatest
**near the critical point**.

### Other equations of state ·FL s37

**Virial:** $P = \dfrac{RT}{v} + \dfrac{a(T)}{v^2} + \dfrac{b(T)}{v^3} + \dfrac{c(T)}{v^4} + \cdots$

**Beattie-Bridgeman** and **Benedict-Webb-Rubin** — full forms in `02-first-law.md` §2.12; constants
from Table 3–4. Accurate to about $0.8\rho_{cr}$ and $2.5\rho_{cr}$ respectively.

### [added] Van der Waals — **NOT in FL, but assessed in GA1 Part B**

$$\boxed{\;\left(P + \frac{a}{v^2}\right)\left(v - b\right) = RT\;}$$

$$a = \frac{27R^2T_{cr}^2}{64P_{cr}}, \qquad b = \frac{RT_{cr}}{8P_{cr}}$$

$a$ corrects for intermolecular attraction, $b$ for the finite molecular volume. **This equation appears
nowhere in the lecture material** — FL s37 gives Beattie-Bridgeman, Benedict-Webb-Rubin and the virial
expansion instead. Supplied here because the exercises require it.

---

## Topic 2 & 3 — the second law, heat engines and cycles ·EPC, TC, HE

> **Sign convention is not an issue in this section.** EPC, TC and HE all use **magnitudes with
> directional subscripts** ($Q_H$, $Q_L$, $W_{net,out}$), which sidesteps the $\pm W$ problem entirely.
> Every $Q$ and $W$ below is a **positive number**. Adopt this style in exam work.

### Cycle energy balance ·EPC s48 · ·TC s17 · ·HE s9

$$\boxed{\;W_{net,out} = Q_{in} - Q_{out} = Q_H - Q_L\;}\qquad(\Delta U = 0\text{ over a cycle})$$

$$\boxed{\;W_{net,out} = Q_{net,in}\;}$$

### Thermal efficiency ·EPC s50 · ·TC s18 · ·HE s9

$$\boxed{\;\eta_{th} = \frac{W_{net,out}}{Q_H} = \frac{Q_H - Q_L}{Q_H} = 1 - \frac{Q_L}{Q_H}\;}$$

Always $\eta_{th} < 1$: $Q_L$ is never zero (Kelvin–Planck).

### Coefficient of performance ·EPC s54–s55 · ·TC s19

$$\boxed{\;\mathrm{COP}_R = \frac{Q_L}{W_{net,in}} = \frac{Q_L}{Q_H - Q_L}\;}\qquad
\boxed{\;\mathrm{COP}_{HP} = \frac{Q_H}{W_{net,in}} = \frac{Q_H}{Q_H - Q_L}\;}$$

$$\boxed{\;\mathrm{COP}_{HP} = \mathrm{COP}_R + 1\;}\qquad
\mathrm{EER} = 3.412\,\mathrm{COP}_R \quad(\text{Btu/Wh})$$

$W_{net,in} = Q_H - Q_L$. One ton of heating/cooling $= 12{,}000\ \mathrm{Btu/h} = 211\ \mathrm{kJ/min}$.

### Carnot — the reversible limit ·EPC s75–s77 · ·HE s10, s26

$$\boxed{\;\frac{Q_L}{Q_H} = \frac{T_L}{T_H}\;}\qquad\text{(reversible devices only)}$$

$$\boxed{\;\eta_{th,rev} = 1 - \frac{T_L}{T_H}\;}$$

$$\boxed{\;\mathrm{COP}_{R,rev} = \frac{T_L}{T_H - T_L}\;}\qquad
\boxed{\;\mathrm{COP}_{HP,rev} = \frac{T_H}{T_H - T_L}\;}$$

> ### ⚠ $T_H$ and $T_L$ MUST be in kelvin
>
> Stated on ·HE s10, s14, s26 and s30, and demonstrated on ·EPC s79–s82. **The denominator
> $T_H - T_L$ is a difference and is the same in °C and K — the numerator is not.**

**The three-way comparison** ·EPC s76, s78

$$\eta_{th} \begin{cases} < \eta_{th,rev} & \text{irreversible}\\ = \eta_{th,rev} & \text{reversible}\\ > \eta_{th,rev} & \textbf{impossible}\end{cases}
\qquad
\mathrm{COP}_R \begin{cases} < \mathrm{COP}_{R,rev} & \text{irreversible}\\ = \mathrm{COP}_{R,rev} & \text{reversible}\\ > \mathrm{COP}_{R,rev} & \textbf{impossible}\end{cases}$$

### Entropy — the only entropy equations in the course ·HE s28

$$\boxed{\;Q_H = T_H\,\Delta s\;}\qquad\boxed{\;Q_C = T_C\,\Delta s\;}\qquad
\boxed{\;W_{net} = \left(T_H - T_C\right)\Delta s\;}$$

Carnot-specific. Dividing gives $\eta_{Carnot} = 1 - T_C/T_H$ — the $\Delta s$ cancels, which is why the
working fluid and machine size drop out.

**[added] Not in any MEC 3105 document:**
$$dS = \frac{\delta Q_{rev}}{T}\qquad \Delta S_{\text{isolated}} \ge 0$$

### Enthalpy ·TC s12 · ·FL s21

$$H = U + PV \qquad (\text{·TC s12 writes } H = E + PV \text{ — C21})$$

---

## [added] Named-cycle efficiencies — **ABSENT FROM ALL FIVE DECKS**

Otto, Diesel, Brayton, Rankine and Stirling are **named and tabulated** (·TC s13, ·HE s12) but
**analysed nowhere**. Supplied here in standard form; **all marked `[added]`**.

$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}}
\qquad
\eta_{Diesel} = 1 - \frac{1}{r^{\gamma-1}}\left[\frac{r_c^{\gamma} - 1}{\gamma\left(r_c - 1\right)}\right]$$

$$\eta_{Brayton} = 1 - \frac{1}{r_p^{(\gamma-1)/\gamma}}
\qquad
\eta_{Rankine} = \frac{(h_1 - h_2) - (h_4 - h_3)}{h_1 - h_4}$$

$r = V_1/V_2$ compression ratio · $r_c = V_3/V_2$ cut-off ratio · $r_p = P_2/P_1$ pressure ratio.
$\eta_{Stirling} = \eta_{Carnot}$ with ideal regeneration.

**Check before using in an assessment** whether the lecturer expects these — they are not in the notes.

---

## Pending sections

| Section | Document | Stage |
|---|---|---|
| Steady-flow energy equation | **absent from all five decks** — assessed in GA2 | 1c |
| Group activity solutions | GA1, GA2 | 1c |

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
