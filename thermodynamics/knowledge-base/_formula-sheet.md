---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
file_role: formula-sheet
source: "Built incrementally, one lecture document per stage. Currently covers TT only."
coverage: "TT (Temperature and Thermometry) complete. FL, EPC, TC, HE pending."
tags: [formula-sheet, equations, temperature, conversions]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

# Formula sheet — MEC 3105

Every equation in the course, **in corrected form**, tagged to its source page and to the topic file
that derives it. Where a source page prints a defective form, the corrected form is given here and the
defect is flagged — never silently fixed.

> **Build status.** Currently covers **TT** only. One section is added per build stage.
> Numbering in the *Eq.* column is **the lecturer's own**, so it can be quoted back in an exam.

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

## Pending sections

| Section | Document | Stage |
|---|---|---|
| §1.2 Equations of state — ideal gas, Van der Waals, compressibility $Z$ | FL, GA1 | 1b / 1c |
| §1.3 Work, heat and the first law | FL, GA2 | 1b / 1c |
| Topic 2 Energy equations and phase changes | EPC | 2 |
| Topic 3 Power production and thermodynamic cycles | TC, HE | 3 |

⚠ Before the first-law equations are added, the **work sign convention** must be resolved — see
`_nomenclature.md` clash 1. Writing $Q = W + \Delta U$ and $\Delta U = Q - W$ on the same sheet
without stating which convention each belongs to would make the sheet actively misleading.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
