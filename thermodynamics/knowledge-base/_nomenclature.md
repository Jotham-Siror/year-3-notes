---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
file_role: nomenclature
source: "Built incrementally, one lecture document per stage. Currently covers TT only."
coverage: "TT (Temperature and Thermometry) complete. FL, EPC, TC, HE pending."
tags: [nomenclature, symbols, units, clashes, sign-conventions]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Nomenclature — MEC 3105

Every symbol used in the knowledge base, its meaning, its SI units, and — the section that gets
consulted most — **where two sources use the same symbol for different things**.

> **Build status.** This file grows one document per stage. It currently covers **TT** in full.
> Entries drawn from documents not yet transcribed are marked **⧗ not yet verified** and carry no
> `V`/`C` ID; they were read from a PDF text layer only and must be confirmed against a render before
> they are relied on.

---

## ⚠ Clash table — read this first

The symbol collisions that actually cost marks, most damaging first.

| # | Symbol | Meaning A | Meaning B | Status |
|---|---|---|---|---|
| **1** | $W$ | **FL**: work done **ON** the gas is positive, so $Q = W + \Delta U$ | **GA2**: work done **BY** the system is positive, so $\Delta U = Q - W$ | ⧗ **not yet verified** |
| **2** | $R$ | **FL**: universal gas constant $\bar R = 8.314\ \mathrm{J\,mol^{-1}K^{-1}}$ with $PV = nRT$ | **GA**: *specific* gas constant, e.g. $0.297\ \mathrm{kJ\,kg^{-1}K^{-1}}$ for $\mathrm{N_2}$, with $PV = mRT$ | ⧗ **not yet verified** |
| **3** | $273.15$ vs $273.16$ | $273.15$ — the **Celsius↔Kelvin offset**; absolute zero is $-273.15\ ^\circ\mathrm{C}$ | $273.16$ — the **triple point of water** in kelvins ($=0.01\ ^\circ\mathrm{C}$) | ✅ verified, TT |
| **4** | $T$ | **unsubscripted $T$ in TT always means the KELVIN temperature** | $T_C$ Celsius, $T_F$ Fahrenheit — never bare $T$ | ✅ verified, TT |
| **5** | $h$ | **TT Fig. 4**: mercury column height difference, $\mathrm{m}$ | later documents: **specific enthalpy**, $\mathrm{J\,kg^{-1}}$ | partial — TT verified |
| **6** | $P$ | pressure, $\mathrm{Pa}$ — TT's only use | power in later cycle work, $\mathrm{W}$ | partial — TT verified |

### 1 · The sign convention for work — the single highest-risk item in the unit

⧗ **Not yet verified — awaiting the FL build (Stage 1b).** Recorded now because it was found during
Stage 0 and would be expensive to rediscover late.

The lecture deck and the **assessed** exercises appear to define $W$ with **opposite signs**:

$$\text{FL:}\quad Q = W + \Delta U \qquad\text{with }W>0\text{ for work done ON the gas}$$

$$\text{GA2:}\quad \Delta U = Q - W \qquad\text{with }W>0\text{ for work done BY the system}$$

Both are internally consistent and both are standard in the literature (FL's is the older
physics-textbook convention, GA2's is the engineering-thermodynamics convention). The hazard is
meeting them **in the same unit**: the same compression gives $W = +1013\ \mathrm{J}$ under FL's
convention and $W = -1013\ \mathrm{J}$ under GA2's.

**Working rule until this is verified:** read the convention off the question before substituting
anything, and state which one is in use at the top of the answer. $Q$ is positive **into** the system
in both.

### 3 · The two 273s

Differ by exactly the $0.01\ ^\circ\mathrm{C}$ of the triple point, which is why the habit of
substituting the wrong one survives — the error is usually invisible in the final answer.

- **Converting a temperature:** always $273.15$.
- **$273.16$ appears once in the entire course**, in the definition of the kelvin (·TT p14). Nowhere
  else.

### 4 · Which scale a bare $T$ means

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

## Pending — symbols expected from documents not yet transcribed

Registered so the clash table can be completed rather than rebuilt. **None of these is verified.**

| Symbol | Expected meaning | From | Clash risk |
|---|---|---|---|
| $Q$ | heat transferred | FL, EPC, GA2 | sign convention — see clash 1 |
| $W$ | work | FL, EPC, GA2 | **sign convention — clash 1** |
| $U$, $\Delta U$, $u$ | internal energy, specific internal energy | FL, EPC | $u$ vs $U$ — extensive vs specific |
| $\bar R$, $R$ | universal vs specific gas constant | FL, GA | **clash 2** |
| $n$, $m$ | number of moles, mass | FL, GA | pairs with clash 2 — $PV=nRT$ vs $PV=mRT$ |
| $c_p$, $c_v$ | specific heats at constant pressure / volume | GA2 | $c_p - c_v = R$ — which $R$? see clash 2 |
| $h$ | specific enthalpy, $h = u + Pv$ | TC, GA2 | **clash 5** — TT uses $h$ for a height |
| $v$, $V$ | specific volume vs volume | EPC, GA | extensive vs specific |
| $Z$ | compressibility factor | FL, GA1 | — |
| $a$, $b$ | Van der Waals constants | FL, GA1 | — |
| $\eta_{th}$ | thermal efficiency | EPC, TC, HE | requires **absolute** $T$ — see clash 4 |
| $T_H$, $T_L$ | hot / cold reservoir temperatures | EPC, HE | requires **absolute** $T$ — see clash 4 |
| $\mathrm{COP}$ | coefficient of performance | EPC | — |
| $s$ | specific entropy | HE | — |

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
