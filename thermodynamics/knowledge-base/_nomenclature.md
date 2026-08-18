---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
file_role: nomenclature
source: "Built incrementally, one lecture document per stage. Covers all five lecture documents."
coverage: "ALL FIVE lecture documents — 200 / 200. Group activities pending."
tags: [nomenclature, symbols, units, clashes, sign-conventions]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Nomenclature — MEC 3105

Every symbol used in the knowledge base, its meaning, its SI units, and — the section that gets
consulted most — **where two sources use the same symbol for different things**.

> **Build status.** This file grows one document per stage. It now covers **all five lecture
> documents** in full. Entries drawn from documents not yet transcribed are marked **⧗ not yet verified** and carry no
> `V`/`C` ID; they were read from a PDF text layer only and must be confirmed against a render before
> they are relied on.

---

## ⚠ Clash table — read this first

The symbol collisions that actually cost marks, most damaging first.

| # | Symbol | Meaning A | Meaning B | Status |
|---|---|---|---|---|
| **1** | $W$ | $W > 0$ = work done **ON** the gas ⇒ $\Delta U = Q + W$ | $W > 0$ = work done **BY** the system ⇒ $\Delta U = Q - W$ | ✅ **VERIFIED — FL states BOTH. See below.** |
| **2** | $V$ | **volume**, $\mathrm{m^3}$ — everywhere in FL except s15/s18 | **velocity**, $\mathrm{m\,s^{-1}}$ — in $\Delta\mathrm{KE} = \tfrac12 m(V_2^2 - V_1^2)$ | ✅ verified, FL s15, s18 (C3) |
| **3** | $\delta$ | **inexact differential** operator: $\delta Q$, $\delta W$ | **polytropic index**: $\delta = 0, 1, \gamma, \infty$ | ✅ verified, FL (C6) |
| **4** | $273.15$ vs $273.16$ | $273.15$ — the **Celsius↔Kelvin offset**; absolute zero is $-273.15\ ^\circ\mathrm{C}$ | $273.16$ — the **triple point of water** in kelvins ($=0.01\ ^\circ\mathrm{C}$) | ✅ verified, TT |
| **5** | $T$ | **unsubscripted $T$ always means the KELVIN temperature** | $T_C$ Celsius, $T_F$ Fahrenheit — never bare $T$ | ✅ verified, TT |
| **6** | $R$ | **universal** $R_u = 8.31447\ \mathrm{kJ\,kmol^{-1}K^{-1}}$, used with $PV = nR_uT$ and molar $C_p$, $C_v$ | **specific** $R = R_u/M$, e.g. $0.2968\ \mathrm{kJ\,kg^{-1}K^{-1}}$ for $\mathrm{N_2}$, used with $PV = mRT$ | ✅ **verified — NOT a conflict.** See below. |
| **7** | $a$, $b$, $c$ | **FL s37**: Beattie-Bridgeman / Benedict-Webb-Rubin / virial constants | **GA1**: **Van der Waals** constants $a$, $b$ | ✅ verified — different equations entirely |
| **8** | $\gamma$ | **FL s27**: $\gamma = C_P/C_V$, the heat-capacity ratio | **FL s37**: a Benedict-Webb-Rubin constant, same slide deck | ✅ verified, FL |
| **9** | $h$ | **TT Fig. 4**: mercury column height difference, $\mathrm{m}$ | **FL s21**: **specific enthalpy** $h = u + Pv$, $\mathrm{J\,kg^{-1}}$ | ✅ verified, TT + FL |
| **10** | $P$ | pressure, $\mathrm{Pa}$ — the only use in every document | power — **never actually used for power anywhere in the course** | ✅ resolved — no clash |
| **11** | $T_C$ | **TT** (`01`): **Celsius temperature**, $^\circ\mathrm{C}$ | **HE** (`05`): **cold-reservoir temperature**, and it must be in **kelvin** | ⚠️ **verified — DANGEROUS COLLISION, see below** |
| **11b** | $Q_L$, $T_L$ | **EPC** (`03b`): low-temperature reservoir heat and temperature | **HE** (`05`): the same quantities written $Q_C$, $T_C$ | ✅ verified — same quantities, different subscript |
| **12** | $\eta$ | **HE** writes bare $\eta$ for thermal efficiency | **EPC, TC** write $\eta_{th}$; **HE** also uses $\eta_{Carnot}$ | ✅ verified — read from context |
| **13** | $E$ | **TC s12**: internal energy, in $H = E + PV$ | **FL s15**: *total* energy $E = U + \mathrm{KE} + \mathrm{PE}$ | ✅ verified — TC's usage is the odd one (C21) |
| **14** | $W_{net}$ | **TC s16** assigns it units "kJ, Btu, **kW, hp**" — energy *and* power | correct: work per cycle is **energy**; the rate is $\dot W_{net}$ | ✅ verified — **TC s16 is wrong** (V22) |

### 1 · The sign convention for work — the single highest-risk item in the unit

✅ **VERIFIED at Stage 1b, and it is worse than Stage 0 recorded.** The conflict is **not** merely
between the deck and the exercises — **FL contradicts itself**, stating both conventions explicitly,
twenty slides apart:

> **FL s13** — "Some conventions. For the gases perspective: … **Work done on the gas is positive**,
> work done by the gas is negative."

> **FL s30** — "$W < 0$: work done **on** the system.  $W > 0$: work done **by** the system."

Exact opposites. $Q$ is positive **into** the system in both, so heat is never the problem — only $W$.

| Convention | First law | Boundary work | FL slides |
|---|---|---|---|
| **A** — physics ($W>0$ = **on**) | $\Delta U = Q + W$ | $W = -P\,\Delta V$ | s7–s8, **s13**, s19–s20, s23–s28 |
| **B** — engineering ($W>0$ = **by**) | $\Delta U = Q - W$ | $W_b = +\int P\,dV$ | s12, s15–s18, s21–s22, **s30**, s31–s33 |

**GA2 uses convention B** ("Q positive into the system; W positive done BY the system",
$\Delta U = Q - W$) — so the **assessed exercises agree with FL's own second half**.

#### The working rule

**Default to convention B for anything assessed.** Then:

1. **Identify the convention before substituting anything.** Two tells, either sufficient:
   $W_b = +\int P\,dV$ ⇒ **B**;  $W = -P\Delta V$ ⇒ **A**. Or: $\Delta U = Q - W$ ⇒ **B**;
   $\Delta U = Q + W$ ⇒ **A**.
2. **State which one you are using** at the top of the answer.
3. **Never change it mid-question.** FL's worked example fails by exactly this — it takes
   $W = -P\Delta V$ from A and substitutes into $Q = W + \Delta U$ from B, and its answer comes out
   **wrong by a factor of five** (V8 in `_verification-log.md`).

The same compression gives $W = +1013\ \mathrm{J}$ under A and $W = -1013\ \mathrm{J}$ under B. Both are
"right"; mixing them is not.

### 11 · ⚠ $T_C$ means two different things, and mixing them is catastrophic

**This is the worst symbol collision in the course**, because both readings are temperatures and neither
looks wrong on the page.

| Document | $T_C$ means | Units |
|---|---|---|
| **TT** (`01-temperature-thermometry`) | **Celsius** temperature | $^\circ\mathrm{C}$ |
| **HE** (`05-heat-engines-and-carnot`) | **cold-reservoir** temperature | $\mathrm{K}$ — **must be absolute** |

TT writes $T_C = T - 273.15$, so its $T_C$ is *never* absolute. HE writes
$\eta_{Carnot} = 1 - T_C/T_H$, where $T_C$ **must** be absolute. **The same symbol, with opposite
requirements about the very thing it must not get wrong.**

**Working rule:** in anything about heat engines, cycles or efficiency, $T_C$ is the **cold reservoir in
kelvin**. In anything about temperature scales and conversion, $T_C$ is **Celsius**. `03b` sidesteps the
problem entirely by writing $T_L$ — **prefer $T_L$ in your own work** and the collision disappears.

### 6 · The two gas constants — dissolved, not a conflict

Stage 0 recorded this as a suspected clash. **It is not one.** FL s34 teaches the relation explicitly:

$$R = \frac{R_u}{M} \qquad (\mathrm{kJ\,kg^{-1}K^{-1}})$$

and tabulates $\mathrm{N_2}$ at $0.2968\ \mathrm{kJ\,kg^{-1}K^{-1}}$ — which is exactly the group
activities' $0.297$. So $PV = nR_uT$ (molar, used in FL s22–s28) and $PV = mRT$ (mass-specific, used in
the exercises) are **the same equation in different bases**.

*Check: $R_u/M = 8.31447/28.013 = 0.2968$ ✓*

**The practical rule:** match the basis to the quantity you were given. Mass in kg → specific $R$ from
the table. Moles → $R_u$. Molar $C_p$, $C_v$ pair with $R_u$; mass-specific $c_p$, $c_v$ pair with
specific $R$ — and **Mayer's relation takes whichever basis you are in**:
$C_P - C_V = R_u$ (molar, FL s28) or $c_p - c_v = R$ (specific, assessed in GA2).

### 4 · The two 273s

Differ by exactly the $0.01\ ^\circ\mathrm{C}$ of the triple point, which is why the habit of
substituting the wrong one survives — the error is usually invisible in the final answer.

- **Converting a temperature:** always $273.15$.
- **$273.16$ appears once in the entire course**, in the definition of the kelvin (·TT p14). Nowhere
  else.

### 5 · Which scale a bare $T$ means

TT is disciplined about this: $T$ **never** means Celsius. Every Celsius quantity carries the
subscript $C$, every Fahrenheit quantity the subscript $F$. Read a bare $T$ as kelvins on sight.

This matters beyond notation: gas-law and efficiency formulas require **absolute** temperature, and
substituting a Celsius value into $PV = nRT$ or $\eta = 1 - T_L/T_H$ is a whole-answer error rather
than a small one.

---

## Symbols — temperature and thermometry (TT)

| Symbol | Meaning | SI unit | Typical value | Source |
|---|---|---|---|---|
| $T$ | thermodynamic (absolute / Kelvin) temperature | $\mathrm{K}$ | $290\ \mathrm{K}$ room temp | ·TT p3 |
| $T_C$ | Celsius temperature | $^\circ\mathrm{C}$ | $0$ ice point, $100$ steam point | ·TT p9, p13 |
| $T_F$ | Fahrenheit temperature | $^\circ\mathrm{F}$ | $32$ ice point, $212$ steam point | ·TT p14–p15 |
| $\Delta T$ | a **difference** of absolute temperature | $\mathrm{K}$ | — | ·TT p17 |
| $\Delta T_C$ | a **difference** of Celsius temperature | $\mathrm{C}^\circ$ | — | ·TT p15 |
| $\Delta T_F$ | a **difference** of Fahrenheit temperature | $\mathrm{F}^\circ$ | — | ·TT p15 |
| $P$ | pressure of the trapped gas (gas thermometer) | $\mathrm{Pa}$ | — | ·TT p12 fig. 4 |
| $P_0$ | pressure above the open mercury reservoir (atmospheric) | $\mathrm{Pa}$ | $\approx101.3\ \mathrm{kPa}$ | ·TT p12 fig. 4 |
| $h$ | mercury column height difference, read against the scale | $\mathrm{m}$ | — | ·TT p12 fig. 4 |

### Constants and fixed points (TT)

| Quantity | Value | Source |
|---|---|---|
| Absolute zero | $0\ \mathrm{K} = -273.15\ ^\circ\mathrm{C}$ | ·TT p13 **⚠ V1, V2 — minus sign absent from the page** |
| Celsius↔Kelvin offset | $273.15$ | ·TT p13 |
| Ice point | $0\ ^\circ\mathrm{C} = 273.15\ \mathrm{K} = 32\ ^\circ\mathrm{F}$ | ·TT p9, p14 |
| Steam point | $100\ ^\circ\mathrm{C} = 373.15\ \mathrm{K} = 212\ ^\circ\mathrm{F}$ | ·TT p9, p14 |
| Triple point of water | $0.01\ ^\circ\mathrm{C} = 273.16\ \mathrm{K}$, at $4.58\ \mathrm{mmHg}$ | ·TT p13 |
| Degree-size ratio | $\tfrac95 = 1.8$ Fahrenheit degrees per Celsius degree | ·TT p15 |

---

## Notation conventions used in this knowledge base

Where TT is silent on notation, these choices are `[added]` and applied consistently:

- **$^\circ\mathrm{C}$ versus $\mathrm{C}^\circ$.** A *temperature* is written
  $25\ ^\circ\mathrm{C}$; an *interval* is written $6.7\ \mathrm{C}^\circ$. TT does not make this
  distinction typographically — it writes $^\circ\mathrm{C}$ for both — but the distinction is exactly
  what V4 turns on, so it is marked here. **Reproduce TT's own style in the exam**; use this one when
  reasoning about which rule applies.
- **A difference in kelvins carries no degree sign** — $\Delta T = 6.7\ \mathrm{K}$, never
  $6.7\ ^\circ\mathrm{K}$. The kelvin has taken no degree sign since 1967.
- **Provenance.** `·TT p13` is the document's own **printed footer** page number. TT's footer starts
  at 2 on the title page, so a PDF viewer shows one less: `·TT p13` = PDF page 12.

---

## Symbols — work, heat and the first law (FL)

| Symbol | Meaning | SI unit | Source |
|---|---|---|---|
| $Q$ | heat transferred; **positive INTO the system** in every FL slide | $\mathrm{J}$ | ·FL s10, s13 |
| $W$ | work — **sign convention varies, see clash 1** | $\mathrm{J}$ | ·FL s7, s13, s30 |
| $W_b$ | moving-boundary ($P\,dV$) work; $+$ expansion, $-$ compression | $\mathrm{J}$ | ·FL s32 |
| $W_{\text{other}}$ | all non-boundary work — electrical, shaft | $\mathrm{J}$ | ·FL s21 |
| $\dot W$, $\dot Q$ | power, heat-transfer rate | $\mathrm{W}$ | ·FL s16, s30 |
| $w$ | work per unit mass | $\mathrm{J\,kg^{-1}}$ | ·FL s30 |
| $U$, $\Delta U$ | internal energy (extensive) | $\mathrm{J}$ | ·FL s8, s10 |
| $u$ | **specific** internal energy | $\mathrm{J\,kg^{-1}}$ | ·FL s15 |
| $E$, $\Delta E$ | total energy $= U + \mathrm{KE} + \mathrm{PE}$ | $\mathrm{J}$ | ·FL s15 |
| $e$ | total energy per unit mass | $\mathrm{J\,kg^{-1}}$ | ·FL s16 |
| $H$, $h$ | enthalpy, specific enthalpy; $H = U + PV$, $h = u + Pv$ | $\mathrm{J}$, $\mathrm{J\,kg^{-1}}$ | ·FL s21 |
| $C_V$, $C_P$ | **molar** heat capacities at constant $V$, $P$ | $\mathrm{J\,mol^{-1}K^{-1}}$ | ·FL s22–s28 |
| $c_v$, $c_p$ | **mass-specific** heat capacities | $\mathrm{J\,kg^{-1}K^{-1}}$ | GA2 |
| $\gamma$ | $C_P/C_V$, heat-capacity ratio | — | ·FL s27 |
| $\delta$ | polytropic index (**also** the inexact-differential operator — clash 3) | — | ·FL s29 |
| $v$ | specific volume | $\mathrm{m^3\,kg^{-1}}$ | ·FL s34 |
| $\bar v$ | **molar** specific volume | $\mathrm{m^3\,kmol^{-1}}$ | ·FL s37 |
| $R_u$ | universal gas constant, $8.31447\ \mathrm{kJ\,kmol^{-1}K^{-1}}$ | — | ·FL s34 |
| $R$ | **specific** gas constant $= R_u/M$ | $\mathrm{kJ\,kg^{-1}K^{-1}}$ | ·FL s34 |
| $M$ | molar mass | $\mathrm{kg\,kmol^{-1}}$ | ·FL s34 |
| $n$, $m$ | number of moles, mass | $\mathrm{mol}$, $\mathrm{kg}$ | ·FL s4, s15 |
| $Z$ | compressibility factor, $Pv = ZRT$ | — | ·FL s35 |
| $P_R$, $T_R$, $v_R$ | reduced pressure, reduced temperature, pseudo-reduced specific volume | — | ·FL s36 |
| $P_{cr}$, $T_{cr}$, $\rho_{cr}$ | critical pressure, temperature, density | $\mathrm{Pa}$, $\mathrm{K}$, $\mathrm{kg\,m^{-3}}$ | ·FL s35–s37 |
| $V$ (velocity) | velocity in $\Delta\mathrm{KE}$ — **clash 2** | $\mathrm{m\,s^{-1}}$ | ·FL s15, s18 |
| $z$, $Z$ (elevation) | elevation in $\Delta\mathrm{PE}$ | $\mathrm{m}$ | ·FL s15, s18 |

### Specific gas constants ·FL s34

| Substance | $R$, kJ·kg⁻¹·K⁻¹ |
|---|---|
| Air | 0.2870 |
| Helium | 2.0769 |
| Argon | 0.2081 |
| Nitrogen | 0.2968 |

---

## Symbols — the second law, heat engines and cycles (EPC, TC, HE)

| Symbol | Meaning | SI unit | Source |
|---|---|---|---|
| $Q_H$ | heat from the high-temperature reservoir (magnitude) | $\mathrm{J}$ | ·EPC s48 · ·HE s8 |
| $Q_L$ / $Q_C$ | heat to the low-temperature reservoir — **EPC writes $Q_L$, HE writes $Q_C$** (clash 11) | $\mathrm{J}$ | ·EPC s48 · ·HE s8 |
| $T_H$ | hot-reservoir temperature — **must be ABSOLUTE** | $\mathrm{K}$ | ·EPC s76 · ·HE s10 |
| $T_L$ / $T_C$ | cold-reservoir temperature — **must be ABSOLUTE** (clash 11) | $\mathrm{K}$ | ·EPC s76 · ·HE s10 |
| $W_{net,out}$ | net work delivered per cycle | $\mathrm{J}$ | ·EPC s47 |
| $W_{net,in}$ | net work absorbed per cycle (refrigerator, heat pump) | $\mathrm{J}$ | ·EPC s54 |
| $\eta_{th}$ / $\eta$ | thermal efficiency, $W_{net,out}/Q_H$ | — | ·EPC s48 · ·TC s18 · ·HE s9 |
| $\eta_{th,rev}$, $\eta_{Carnot}$ | reversible (Carnot) efficiency, $1 - T_L/T_H$ | — | ·EPC s75 · ·HE s10, s26 |
| $\mathrm{COP}_R$ | refrigerator coefficient of performance, $Q_L/W_{net,in}$ | — | ·EPC s54 · ·TC s19 |
| $\mathrm{COP}_{HP}$ | heat-pump coefficient of performance, $Q_H/W_{net,in}$ | — | ·EPC s55 |
| $\mathrm{EER}$ | energy efficiency rating, $3.412\,\mathrm{COP}_R$ | Btu/Wh | ·EPC s62 |
| $\Delta s$ | specific entropy change across an isotherm of the Carnot cycle | $\mathrm{J\,kg^{-1}K^{-1}}$ | ·HE s28 |
| $s$ | specific entropy (axis label only; never defined quantitatively) | $\mathrm{J\,kg^{-1}K^{-1}}$ | ·TC s11 · ·HE s28 |
| $\delta$ | polytropic index — **also** the inexact-differential operator (clash 3) | — | ·FL s29 |
| $P_{cr}$, $T_{cr}$, $\rho_{cr}$ | critical pressure, temperature, density | $\mathrm{Pa}$, $\mathrm{K}$, $\mathrm{kg\,m^{-3}}$ | ·FL s35–s37 |

### ⚠ The absolute-temperature rule — the most-tested unit trap in the course

$T_H$ and $T_L$ (or $T_C$) must be in **kelvin** in every efficiency and COP formula. **HE states this on
four separate slides** (s10, s14, s26, s30) and EPC demonstrates it three times (s79, s80–s82).

The one exception, and the reason people get it wrong: **a temperature *difference* is the same number in
°C and in K**, so $T_H - T_L$ may be computed either way — but the **numerator is not a difference**. In
·EPC s81, $T_L$ in the numerator must be $275\ \mathrm{K}$, never $2$. See `01-temperature-thermometry`
§1.7.

---

## Pending — symbols expected from documents not yet transcribed

Registered so the clash table can be completed rather than rebuilt. **None of these is verified.**

| Symbol | Expected meaning | From | Clash risk |
|---|---|---|---|
| $a$, $b$ | **Van der Waals** constants — **not defined anywhere in the five decks** | GA1 only | clash 7 |
| $c_p$, $c_v$ | mass-specific heat capacities; $c_p - c_v = R$ | GA2 | basis — see clash 6 |
| $h_1$, $h_2$ | inlet/exit specific enthalpy in the **steady-flow energy equation** — **the SFEE appears in no lecture document** | GA2 only | — |

*All lecture-document symbols are now recorded. Only the group activities remain.*

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
