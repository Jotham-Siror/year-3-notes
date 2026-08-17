---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "01 — Temperature and Thermometry"
source: "TT — '3.0Temperature and Thermometry 1.pdf', 17 pp. (printed footer pages 2–18)"
pages: "2-18 (printed footer numbering)"
file_role: topic
subtopics:
  - "temperature as an SI base quantity; the Kelvin scale and absolute zero"
  - "thermal contact, thermal equilibrium, and the definition of heat"
  - "the zeroth law of thermodynamics and the formal definition of temperature"
  - "thermometers — the six physical properties they exploit"
  - "liquid-in-glass thermometers and the Celsius scale; disagreement away from calibration points"
  - "the constant-volume gas thermometer; extrapolation to absolute zero"
  - "the triple point of water and the definition of the kelvin"
  - "Celsius, Kelvin and Fahrenheit conversions, including temperature differences"
  - "worked example — skin warming 72 °F to 84 °F"
key_equations: [celsius-kelvin, fahrenheit-from-celsius, celsius-from-fahrenheit, delta-fahrenheit-celsius]
prerequisites: []
leads_to: ["02-first-law", "exercises/ga1-topic1-part1-equations-of-state"]
verification_flags: 6
tags: [temperature, zeroth-law, thermal-equilibrium, thermometry, kelvin, celsius, fahrenheit, absolute-zero, triple-point, gas-thermometer]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [hist] historical/biographical note ·
  [added] supplied here, NOT in the source ·
  ·TT pN = provenance (which page the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 01 — Temperature and Thermometry

Scope: the whole of TT, the first document of Topic 1 (§1.1). Establishes temperature as a measurable
quantity — thermal contact and equilibrium, the zeroth law, the formal definition of temperature —
then the instruments that measure it (liquid-in-glass, constant-volume gas), the extrapolation that
fixes absolute zero, the triple point that fixes the kelvin, and the three scales with their
conversions. Ends with one worked example and two review questions.

Self-contained: TT assumes no prior thermodynamics and introduces no other topic's material.

---

## Reading this file

**Page citations are the document's own printed footer numbers**, which run **2 → 18** across the
17-page PDF. The footer starts at 2 on the title page, so a PDF viewer shows **one less** than the
citation: `·TT p13` is the page whose footer reads 13, i.e. **PDF page 12**.

> ### [added] The lecturer's highlighting is an examinable-content map
>
> Roughly twenty phrases across TT are highlighted in yellow, and **every one of them is a
> definition or a defining condition** — never an example, an aside, or a number. The highlighted
> span is usually exactly the predicate of a definition ("*energy can be exchanged between them*",
> "*variation of pressure with temperature of a fixed volume of gas*").
>
> Treat the highlights as the lecturer's own statement of what must be reproduced verbatim. Each
> `[def]` below corresponds to one.

---

## 1.1 Temperature as a base quantity ·TT p2–p4

[def] **Thermodynamics** is the *study and application of the thermal energy of systems*. ·TT p2
[def] **Thermal physics** is concerned with the *study of temperature, heat, and how they affect
matter*. ·TT p2

Quantitative work needs careful definitions of **temperature**, **heat** and **internal energy**;
heat changes internal energy, which changes temperature, which expands or contracts matter. ·TT p2

Temperature is one of the **seven SI base quantities**, measured on the **Kelvin scale** in units
called **kelvins**. ·TT p3

- A body's temperature has **no apparent upper limit** but does have a **lower limit**, and that
  limiting low temperature is taken as the zero of the Kelvin scale — **absolute zero**. ·TT p3
- Room temperature is about $290\ \mathrm{K}$, i.e. 290 kelvins above absolute zero. ·TT p3

[def] Temperature is commonly associated with *how hot or cold an object feels when we touch it* —
but the senses are **unreliable and often misleading**. ·TT p3

The notes' own illustration: a metal ice tray feels colder than a package of frozen vegetables **at
the same temperature**, because metal conducts thermal energy away from the hand more rapidly than
cardboard. Hence the need for a reproducible instrument. ·TT p3

[fig ·TT p4] **Figure 1** — a vertical logarithmic axis labelled *Temperature (K)*, decades marked
from $10^{-9}$ to $10^{39}$, with arrows to: universe just after beginning ($\sim10^{39}$), highest
laboratory temperature ($\sim10^{8}$), centre of the Sun, surface of the Sun and tungsten melts
(both $\sim10^{4}$), water freezes ($\sim10^{2}$), universe today and boiling helium-3
($\sim10^{0}$), record low temperature ($\sim10^{-9}$). The caption notes that $T=0$ **cannot be
plotted on a logarithmic scale**. The axis carries two break marks where decades are skipped.

*Figure 1 is orientation only — it fixes the sense of scale and carries no examinable number.*

---

## 1.2 Thermal contact, thermal equilibrium and heat ·TT p4–p5

The observation the whole topic rests on: [def] *two objects at different initial temperatures, placed
in contact, will eventually reach a common intermediate temperature*. ·TT p4

The notes' illustration: hot coffee cooled with an ice cube — the ice warms and melts while the
coffee cools. ·TT p4

Three definitions, in the order TT gives them: ·TT p5

[def] Two objects are in **thermal contact** if *energy can be exchanged between them*.

[def] Two objects are in **thermal equilibrium** if *they are in thermal contact and there is no net
exchange of energy*.

[def] **Heat** is the *exchange of energy between two objects because of differences in their
temperatures*.

> **The distinction that gets tested.** Thermal contact is about whether exchange is *possible*;
> thermal equilibrium is about whether the **net** exchange is zero. Two objects in equilibrium are
> still in contact and still exchanging — the flows simply cancel.
>
> And "no *net* exchange" is the phrase to reproduce. "No exchange" is a different, wrong claim.

---

## 1.3 The zeroth law and the formal definition of temperature ·TT p5–p7

[derivation] The operational argument TT builds the law from: ·TT p5–p6

1. Take two objects **A** and **B** that are *not* in thermal contact with each other, and a third
   object **C** that acts as a **thermometer** — a device calibrated to measure temperature.
2. Place C in thermal contact with A until equilibrium; record the reading. *(Figure 2a)*
3. Place C in thermal contact with B until equilibrium; record the reading. *(Figure 2b)*
4. If the two readings are the **same**, then A and B are in thermal equilibrium with each other.
5. Placing A and B in contact confirms it: **no net transfer of energy** occurs. *(Figure 2c)*

[eq] **The zeroth law of thermodynamics** (TT also calls it *the law of equilibrium*): ·TT p6

$$\boxed{\;\text{If A and B are separately in thermal equilibrium with a third object C,}\;}$$
$$\boxed{\;\text{then A and B are in thermal equilibrium with each other.}\;}$$

[fig ·TT p6] **Figure 2** — three panels. **(a)** block A with probe C into a hand-held digital meter
reading **22.5**. **(b)** block B with the same probe C, the meter again reading **22.5**; a callout
spanning both panels reads *"The temperatures of A and B are measured to be the same by placing them
in thermal contact with a thermometer (object C)."* **(c)** A and B pushed together face to face with
no thermometer, callout *"No energy will be exchanged between A and B when they are placed in thermal
contact with each other."* The identical 22.5 readings in (a) and (b) are the whole point of the
figure.

[def] The zeroth law licenses the formal definition — **temperature** is *the property that determines
whether or not an object is in thermal equilibrium with other objects*. ·TT p7

**Two objects in thermal equilibrium with each other are at the same temperature.** ·TT p7

> **Why the law comes first.** Without it, "same temperature" would be meaningless: nothing would
> guarantee that a thermometer reading transfers from one body to another. The zeroth law is what
> makes a thermometer a *thermometer* rather than a device that only ever describes itself.

[exercise ·TT p7] **QUESTION.** Two objects with different sizes, masses and temperatures are placed
in thermal contact. Choose the best answer: energy travels **(a)** from the larger object to the
smaller object, **(b)** from the object with more mass to the one with less mass, **(c)** from the
object at higher temperature to the object at lower temperature.

> [added] **Answer: (c).** By the definition of heat in §1.2, the exchange is driven by the
> **temperature difference** alone. Size and mass set *how much* energy moves and *how long* the
> approach to equilibrium takes — they do not set the **direction**. The distractors (a) and (b) are
> there precisely to test that separation.

---

## 1.4 Thermometers — the six properties they exploit ·TT p7–p8

[def] **Thermometers** are *devices used to measure the temperature of an object or a system*. When a
thermometer is in thermal contact with a system, *energy is exchanged until the thermometer and the
system are in thermal equilibrium with each other*. ·TT p7

**The accuracy condition:** the thermometer must be **much smaller than the system**, so that the
energy it gains or loses does not significantly alter the energy content of the system. ·TT p7

All thermometers exploit some physical property that **changes with temperature** and **can be
calibrated**. TT lists six: ·TT p8

| # | Physical property exploited | Instrument it gives |
|---|---|---|
| 1 | the volume of a liquid | liquid-in-glass (mercury, alcohol) |
| 2 | the length of a solid | bimetallic strip / rod thermometer |
| 3 | the pressure of a gas held at constant volume | **constant-volume gas thermometer** (§1.6) |
| 4 | the volume of a gas held at constant pressure | constant-pressure gas thermometer |
| 5 | the electric resistance of a conductor | resistance thermometer / RTD |
| 6 | the colour of a very hot object | optical / radiation pyrometer |

*The instrument column is `[added]` — TT names the property only, not the device, for rows 2, 4, 5, 6.*

> **Learn this list as a list.** Six numbered items with no equations attached is exactly the shape
> of a "state the physical properties used in thermometry" question, and rows 3 and 5 are the two the
> course goes on to use — row 3 in §1.6 below, row 5 in the group activities' RTD scenarios.

---

## 1.5 The liquid-in-glass thermometer and the Celsius scale ·TT p8–p10

[def] The **mercury (or alcohol) thermometer** consists of a mass of mercury or alcohol that expands
into a glass capillary tube as its temperature rises. ·TT p8

Its five defining features, as TT numbers them: ·TT p8–p9

1. the physical property that changes is the **volume of a liquid**;
2. the change in liquid volume with change in temperature *must be very nearly constant over the
   temperature ranges of interest*;
3. the change in volume of the liquid *varies linearly with its length* along the tube;
4. the temperature is defined in terms of the **length of the liquid column**;
5. it is **calibrated** by placing it in thermal contact with environments that remain at constant
   temperature — such as a mixture of water and ice in thermal equilibrium at atmospheric pressure.

Feature 2 is the assumption that makes the instrument linear; feature 3 is what lets a *length* stand
in for a *volume*; feature 4 is therefore the operational definition of the reading.

[def] The **Celsius temperature scale** ·TT p9

- The ice–water mixture is defined as **zero degrees Celsius**, $0\ ^\circ\mathrm{C}$ — the
  **ice point** or **freezing point** of water.
- The water–steam mixture is defined as $100\ ^\circ\mathrm{C}$ — the **steam point** or **boiling
  point** of water.
- The distance between the two marks is divided into **100 equal segments**, each one degree Celsius.

[fig ·TT p10] **Figure 3** — two beakers side by side, each with a thermometer standing in it. Left: a
beaker of water with ice cubes, the thermometer's mercury column low, labelled $0\ ^\circ\mathrm{C}$.
Right: a beaker of water over a lit Bunsen burner with steam rising, the mercury column high,
labelled $100\ ^\circ\mathrm{C}$. The caption states that the mercury level rises as the temperature
changes from $0\ ^\circ\mathrm{C}$ (the ice point) to $100\ ^\circ\mathrm{C}$ (the steam point).

### The limitation that motivates the gas thermometer ·TT p10

Because mercury and alcohol have **different thermal expansion properties**, when one reads
$50\ ^\circ\mathrm{C}$ the other may read a slightly different temperature — even though both were
calibrated at the same two points.

**The discrepancies are especially large when the measured temperature is far from the calibration
points.** ·TT p10

> **The logic to carry forward.** Two thermometers agree *exactly* at $0\ ^\circ\mathrm{C}$ and
> $100\ ^\circ\mathrm{C}$ because they were forced to. In between and beyond they diverge, because
> "divide the interval into 100 equal parts" bakes in an assumption about *that liquid's* expansion.
> A scale that depends on the working substance is not a fundamental definition of temperature — and
> that is the gap §1.6 closes.

---

## 1.6 The constant-volume gas thermometer, absolute zero and the Kelvin scale ·TT p11–p14

Mercury thermometers are practical but **do not define temperature in a fundamental way**. Gas
thermometers do, and relate temperature directly to internal energy. ·TT p11

[def] In a gas thermometer the *temperature readings are nearly independent of the substance used in
the thermometer*. ·TT p11

[def] In the **constant-volume gas thermometer** the behaviour observed is the *variation of pressure
with temperature of a fixed volume of gas*. ·TT p11

**How a measurement is made:** ·TT p11

1. Calibrate using the ice and steam points of water, giving the calibration curve of Figure 5.
2. To measure an unknown temperature, *place the gas flask in thermal contact with the substance and
   adjust the column of mercury until the level in column A returns to zero* — this is what holds the
   gas **volume** constant.
3. The **height of the mercury column** then gives the gas **pressure**.
4. Read the temperature off the calibration curve.

[fig ·TT p12] **Figure 4** — a constant-volume gas thermometer. A spherical flask of gas at pressure
$P$ sits in a beaker labelled *"Bath or environment to be measured"* (drawn containing ice). A tube
runs from the flask over to the top of mercury column **A**. A vertical graduated **scale** stands
beside column A with a mark labelled **0** at the mercury level. Column A connects through a
**flexible hose** at the bottom to column **B**, the taller open **mercury reservoir**, whose top
surface is at atmospheric pressure $P_0$. The height difference between the reservoir surface and the
0 mark is labelled $h$. A callout reads *"The volume of gas in the flask is kept constant by raising
or lowering reservoir B to keep the mercury level in column A constant."*

- $P$ — pressure of the trapped gas, Pa
- $P_0$ — pressure above the open mercury reservoir (atmospheric), Pa
- $h$ — mercury height difference read against the scale, m
- $A$, $B$ — the fixed-level column and the movable reservoir respectively

*TT does not write a manometer equation for this figure, so none is given here.*

[fig ·TT p12] **Figure 5** — a typical calibration graph: axes $P$ (vertical, unscaled) against
$T\ (^\circ\mathrm{C})$ (horizontal), gridded, with ticks at $0$ and $100$. A **single straight
orange line** rises from a filled black dot at $T=0$ to a filled black dot at $T=100$, with a dashed
vertical line dropping from the upper dot to the $100$ tick. Two green callouts label the dots:
*"Pressure at the freezing point of water"* → the $T=0$ dot, *"Pressure at the boiling point of
water"* → the $T=100$ dot. **The two green lines are callout leaders, not plotted data.**

> ⚠ VERIFY **C2** ·TT p12–p13 — the text refers to *"the **curves** in Figure 5"* (plural) and to
> results holding *"regardless of the type of gas or the value of the low starting pressure"*, which
> implies a **family** of calibration lines. Figure 5 as printed shows **one** line. The figure also
> stops at $T=0$, so the **extrapolation the text describes is not drawn**. Nothing is wrong with
> either the text or the figure alone — they simply do not depict the same thing. See
> `_verification-log.md`.

### The experimental result ·TT p12

Thermometer readings are nearly independent of the type of gas used, **as long as**: ·TT p12

- the gas **pressure is low**, and
- the temperature is **well above the point at which the gas liquefies**.

Both conditions matter: near liquefaction a gas stops behaving ideally, and the substance-independence
collapses.

### Extrapolation to absolute zero ·TT p12–p13

[derivation] Extend the calibration lines back toward negative temperatures. In every case —
**regardless of the type of gas or the value of the low starting pressure** — the pressure
extrapolates to **zero** at the same temperature. ·TT p12–p13

$$\boxed{\;P \to 0 \quad\text{as}\quad T_C \to -273.15\ ^\circ\mathrm{C}\;}$$

[def] That temperature is **absolute zero**. It is *universal in its importance, because it does not
depend on the substance used in the thermometer*. ·TT p13

> ⚠ VERIFY **V1** ·TT p13 — the page prints *"the pressure extrapolates to zero when the temperature
> is **273.15 °C**"*. The minus sign is **absent from the page itself** (confirmed on a 400 dpi
> render, not merely missing from the text layer). It must read $-273.15\ ^\circ\mathrm{C}$:
> $+273.15\ ^\circ\mathrm{C}$ is a temperature *above* the steam point, where gas pressure is high,
> not zero. See `_verification-log.md`.

[def] Absolute zero is the basis of the **Kelvin temperature scale**, which sets
$-273.15\ ^\circ\mathrm{C}$ as its zero point ($0\ \mathrm{K}$). ·TT p13

> ⚠ VERIFY **V2** ·TT p13 — the same missing minus, one paragraph later: *"the Kelvin temperature
> scale, which sets **273.15 °C** as its zero point (0 K)"*. Must read
> $-273.15\ ^\circ\mathrm{C}$. Two occurrences, so this is the page's own defect and not a stray
> character. See `_verification-log.md`.

[eq: celsius-kelvin] The relationship between the two scales — **TT's Equation 1**: ·TT p13

$$\boxed{\;T_C = T - 273.15\;}$$

- $T_C$ — **Celsius** temperature, $^\circ\mathrm{C}$
- $T$ — **Kelvin** (absolute) temperature, $\mathrm{K}$
- $273.15$ — the offset between the zeros of the two scales; a pure number here (see the units note
  below)

Rearranged for the direction actually used more often:

$$\boxed{\;T = T_C + 273.15\;}$$

**On the units.** TT notes that Equation 1 *technically* needs units on the right-hand side, reading

$$T_C = T\ (^\circ\mathrm{C}/\mathrm{K}) - 273.15\ ^\circ\mathrm{C}$$

and says the units are cumbersome in this context, so they are **suppressed in calculations and
restored in the final answer**. ·TT p13

> Follow that convention in the exam: work the arithmetic bare, then attach $^\circ\mathrm{C}$ or
> $\mathrm{K}$ to the answer. Writing $T_C = T - 273.15$ with units on every term is not wrong, just
> not what the notes model.

### The triple point and the definition of the kelvin ·TT p13–p14

Early gas thermometers used the ice and steam points, but those points are **experimentally difficult
to duplicate because they are pressure-sensitive**. A procedure based on two new points was adopted in
**1954**: the first point is **absolute zero**; the second is the triple point of water. ·TT p13

[def] The **triple point of water** is *the single temperature and pressure at which water, water
vapour and ice can coexist in equilibrium*. It is a convenient and reproducible reference for the
Kelvin scale. ·TT p13

| Triple-point value | As printed |
|---|---|
| Temperature (Celsius) | $0.01\ ^\circ\mathrm{C}$ |
| Pressure | $4.58\ \mathrm{mm}$ of mercury |
| Temperature (Kelvin) | $273.16\ \mathrm{K}$ |

[def] Therefore: **the SI unit of temperature, the kelvin, is defined as $1/273.16$ of the temperature
of the triple point of water.** ·TT p14

> ⚠ VERIFY **C1** ·TT p14 — this is the definition of the kelvin **as it stood from 1954 until May
> 2019**. In the current SI the kelvin is fixed instead by assigning an exact value to the Boltzmann
> constant, and $273.16\ \mathrm{K}$ became a measured quantity rather than a definition. Nothing in
> TT's reasoning or arithmetic is affected, and $273.16\ \mathrm{K}$ remains the triple-point
> temperature to well within any tolerance this course uses. **Reproduce the printed definition in
> the exam.** Recorded so the discrepancy is not mistaken for an error if met elsewhere. See
> `_verification-log.md`.

**Do not confuse the two 273s** — this is the most common slip in the whole topic:

| Value | What it is | Where it is used |
|---|---|---|
| $273.15$ | the **Celsius↔Kelvin offset**; absolute zero is $-273.15\ ^\circ\mathrm{C}$ | every conversion, Equation 1 |
| $273.16$ | the **triple point of water** in kelvins ($0.01\ ^\circ\mathrm{C}$) | the definition of the kelvin only |

They differ by exactly the $0.01\ ^\circ\mathrm{C}$ of the triple point. Using $273.16$ in a
conversion is a $0.01$ error — invisible in most answers, which is precisely why the habit survives.

---

## 1.7 Celsius, Kelvin and Fahrenheit ·TT p14–p16

Equation 1 shows $T_C$ is **shifted** from $T$ by $273.15$. Because **the size of a Celsius degree is
the same as a kelvin**, a temperature *difference* of $5\ ^\circ\mathrm{C}$ equals a temperature
difference of $5\ \mathrm{K}$ — the two scales differ **only in the choice of zero point**. ·TT p14

| Fixed point | Kelvin | Celsius |
|---|---|---|
| Ice point | $273.15\ \mathrm{K}$ | $0\ ^\circ\mathrm{C}$ |
| Steam point | $373.15\ \mathrm{K}$ | $100\ ^\circ\mathrm{C}$ |

·TT p14

**The Fahrenheit scale** — the most common scale in use in the United States — sets the ice point at
$32\ ^\circ\mathrm{F}$ and the steam point at $212\ ^\circ\mathrm{F}$. ·TT p14–p15

[eq: fahrenheit-from-celsius] **TT's Equation 2a** ·TT p15

$$\boxed{\;T_F = \tfrac{9}{5}\,T_C + 32\;}$$

- $T_F$ — **Fahrenheit** temperature, $^\circ\mathrm{F}$
- $T_C$ — Celsius temperature, $^\circ\mathrm{C}$
- $\tfrac{9}{5} = 1.8$ — the **ratio of degree sizes**: $180$ Fahrenheit degrees span the same
  interval as $100$ Celsius degrees
- $32$ — the **offset**: the ice point on the Fahrenheit scale

TT's check: $50\ ^\circ\mathrm{F}$ corresponds to $10\ ^\circ\mathrm{C}$ and an absolute temperature
of $283\ \mathrm{K}$. ·TT p15
*[added] Verified: $\tfrac59(50-32) = 10.0\ ^\circ\mathrm{C}$; $10 + 273.15 = 283.15 \approx
283\ \mathrm{K}$. ✓*

[eq: celsius-from-fahrenheit] **TT's Equation 2b** — Equation 2a inverted ·TT p15

$$\boxed{\;T_C = \tfrac{5}{9}\left(T_F - 32\right)\;}$$

> **Subtract before you scale.** $\tfrac59 T_F - 32$ is the single most common algebra slip here. The
> bracket is not optional: the offset lives on the Fahrenheit side, so it must be removed *first*.
> Sanity check on any answer: $32\ ^\circ\mathrm{F}$ must give exactly $0$.

[eq: delta-fahrenheit-celsius] **TT's Equation 3** — for *changes* in temperature ·TT p15

$$\boxed{\;\Delta T_F = \tfrac{9}{5}\,\Delta T_C\;}$$

- $\Delta T_F$ — a temperature **difference** on the Fahrenheit scale, $\mathrm{F}^\circ$
- $\Delta T_C$ — the same difference on the Celsius scale, $\mathrm{C}^\circ$

> **Why the $32$ disappears.** Subtract Equation 2a from itself at two temperatures: the offset is
> the same at both, so it cancels. Only the **scale factor** survives.
>
> This gives the three-line rule that governs every conversion question in the topic:
>
> - a **temperature** on the Celsius and Kelvin scales differs by an **offset** ($273.15$);
> - a **temperature** on the Celsius and Fahrenheit scales differs by **offset *and* scale factor**;
> - a **difference** in temperature: $\Delta T_C = \Delta T$ exactly (offset cancels, degree sizes
>   equal), while $\Delta T_F = \tfrac95 \Delta T_C$ (scale factor survives).
>
> Reading "convert $20\ ^\circ\mathrm{C}$" versus "convert a rise of $20\ ^\circ\mathrm{C}$" is
> therefore the entire question. §1.8 turns on exactly this.

[fig ·TT p16] **Figure 6** — three thermometers drawn side by side, each with a red column and the
same two graduations marked. Left, labelled *Celsius*: **steam point** $100^\circ$ at the upper mark,
**ice point** $0^\circ$ at the lower. Centre, *Fahrenheit*: $212^\circ$ and $32^\circ$. Right,
*Kelvin*: $373.15$ and $273.15$. The row labels *Steam point* and *Ice point* run across all three at
the same heights, making the point that one physical state has three numerical names.

---

## 1.8 [ex] Example 1 — skin warming during vasodilation ·TT p16–p17

**Statement** ·TT p16

> The temperature gradient between the skin and the air is regulated by cutaneous (skin) blood flow.
> If the cutaneous blood vessels are constricted, the skin temperature and the temperature of the
> environment will be about the same. When the vessels are dilated, more blood is brought to the
> surface. Suppose during dilation the skin warms from $72\ ^\circ\mathrm{F}$ to
> $84\ ^\circ\mathrm{F}$.
>
> **(a)** Convert these temperatures to Celsius and find the difference.
> **(b)** Convert the temperatures to Kelvin, again finding the difference.

### (a) Convert to Celsius, then difference ·TT p17

Convert the lower and higher temperatures using **Equation 2b**:

$$T_C = \tfrac{5}{9}\left(T_F - 32.0\right) = \tfrac{5}{9}\left(72.0 - 32.0\right) = 22.2\ ^\circ\mathrm{C}$$

$$T_C = \tfrac{5}{9}\left(T_F - 32.0\right) = \tfrac{5}{9}\left(84.0 - 32.0\right) = 28.9\ ^\circ\mathrm{C}$$

Find the difference between the two temperatures:

$$\Delta T_C = 28.9\ ^\circ\mathrm{C} - 22.2\ ^\circ\mathrm{C} = 6.7\ ^\circ\mathrm{C}$$

*[added] Verified: $\tfrac59(40) = 22.\overline{2}$ → $22.2$ ✓; $\tfrac59(52) = 28.\overline{8}$ →
$28.9$ ✓; exact difference $\tfrac59(12) = 6.\overline{6}$ → $6.7$ ✓.*

### (b) Convert to Kelvin, then difference ·TT p17

$$T_C = T - 273.15 \quad\longrightarrow\quad T = T_C + 273.15$$

$$T = 22.2 + 273.15 = 295\ \mathrm{K}$$

$$T = 28.9 + 273.15 = 302\ \mathrm{K}$$

Find the difference of the two temperatures:

$$\Delta T = 302\ \mathrm{K} - 295\ \mathrm{K} = 7\ \mathrm{K}$$

⚠ VERIFY **V4** — this printed result is wrong; see immediately below.

> ⚠ VERIFY **V3** ·TT p17 — part (b) is introduced *"Convert the lower and higher temperatures using
> **Equation 2a**"*, but the working that follows uses **Equation 1** ($T_C = T - 273.15$), which is
> correct for the task. Equation 2a is the Celsius→Fahrenheit relation
> $T_F = \tfrac95 T_C + 32$ and would give $72\ ^\circ\mathrm{F}$ and $84\ ^\circ\mathrm{F}$ straight
> back. **The printed working is right; only the equation reference is wrong.** See
> `_verification-log.md`.

> ⚠ VERIFY **V4** ·TT p17 — the printed $\Delta T = 7\ \mathrm{K}$ is a **rounding artefact and
> contradicts the notes' own physics**. Correct answer:
>
> $$\boxed{\;\Delta T = 6.7\ \mathrm{K}\;}$$
>
> Three independent confirmations, any one of which is enough in an exam:
>
> 1. **The unrounded conversion.** $295.37\ \mathrm{K}$ and $302.04\ \mathrm{K}$ give
>    $\Delta T = 6.67\ \mathrm{K}$. The $7$ appears only because $295.35$ and $302.05$ were each
>    rounded to three significant figures *before* subtracting — the classic error of rounding
>    mid-calculation.
> 2. **TT p14's own statement.** "The size of a Celsius degree is the same as a kelvin", so
>    $\Delta T_C = \Delta T$ **exactly**. Part (a) got $6.7\ ^\circ\mathrm{C}$; part (b) must
>    therefore give $6.7\ \mathrm{K}$. A $\Delta T_C$ of $6.7$ next to a $\Delta T$ of $7$ is
>    self-contradictory.
> 3. **TT's own Equation 3**, which the page then instructs the student to apply:
>    $\Delta T_F = 84 - 72 = 12\ \mathrm{F}^\circ$, so
>    $\Delta T_C = \tfrac59(12) = 6.67\ ^\circ\mathrm{C} = 6.67\ \mathrm{K}$.
>
> See `_verification-log.md`.

[exercise ·TT p17] The page closes with: **"Use Equation (3) to prove your results?"**

> [added] **The check, worked.** The Fahrenheit change is
> $\Delta T_F = 84.0 - 72.0 = 12.0\ \mathrm{F}^\circ$. Equation 3 rearranged:
>
> $$\Delta T_C = \tfrac{5}{9}\,\Delta T_F = \tfrac{5}{9}(12.0) = 6.67\ ^\circ\mathrm{C}$$
>
> which confirms part (a) — and, since a Celsius degree equals a kelvin, confirms
> $\Delta T = 6.67\ \mathrm{K}$ for part (b) too.
>
> **This is the intended lesson of the example.** Equation 3 converts the *difference* in one step,
> without converting either endpoint. Doing it the long way — convert both, subtract — is what
> exposed the rounding trap in V4. The exercise is a self-check the lecturer built in, and it
> disagrees with the printed $7\ \mathrm{K}$.

---

## 1.9 [exercise] Review questions ·TT p18

**1.** Which represents a larger temperature change, a Celsius degree or a Fahrenheit degree?

> [added] **A Celsius degree.** From Equation 3, $\Delta T_F = \tfrac95 \Delta T_C$: one Celsius
> degree of change equals $1.8$ Fahrenheit degrees of change. The same interval — ice point to steam
> point — is divided into $100$ Celsius degrees but $180$ Fahrenheit degrees, so each Fahrenheit
> degree must be the **smaller** step.
>
> Careful with the direction: the *bigger number* on the Fahrenheit scale means *smaller degrees*.

**2. True or False:** Finding the relationship between two temperature scales using knowledge of the
freezing and boiling point of water in each system is equivalent to finding the equation of a straight
line.

> [added] **True.** Both scales are linear in temperature, so the map between them is
> $T_F = m\,T_C + c$ — a straight line needing exactly two points to fix it. The freezing and boiling
> points of water are those two points:
>
> $$m = \frac{212 - 32}{100 - 0} = \frac{180}{100} = \frac{9}{5}$$
>
> $$c = T_F \text{ at } T_C = 0 = 32$$
>
> giving $T_F = \tfrac95 T_C + 32$ — **Equation 2a, recovered as the equation of a line** through
> $(0, 32)$ and $(100, 212)$. Gradient = ratio of degree sizes; intercept = offset of the zeros.
>
> This is worth being able to do from scratch: it means neither conversion formula has to be
> memorised, and it generalises to any two-point calibration.

---

### Cross-references

- Temperature as a **state variable** in the equation of state $PV = nRT$, and the absolute
  temperature this file defines, are used throughout → **02-first-law** and
  **exercises/ga1-topic1-part1-equations-of-state**.
- The Kelvin scale established here is the **only** scale admissible in gas-law and cycle-efficiency
  work; the unit traps that follow from ignoring it are collected in `_nomenclature.md`.
- Row 5 of the six properties (electric resistance of a conductor) is the basis of the **RTD**
  scenarios in the group activities.
- Absolute zero and the thermodynamic temperature scale are revisited from the second law in
  **03-second-law-and-cycles**.

### Verification notes for this section

Every page read from a **160 dpi render**, with the two suspect lines re-rendered at **400 dpi** to
settle whether the missing minus signs were page defects or text-extraction artefacts. **They are
page defects** — V1 and V2 below. Every number in the document was recomputed independently.

| ID | Page | Class | One-line summary |
|---|---|---|---|
| **V1** | p13 | substantive | absolute zero printed as $273.15\ ^\circ\mathrm{C}$; minus sign absent from the page |
| **V2** | p13 | substantive | Kelvin zero point printed as $273.15\ ^\circ\mathrm{C}$; same missing minus |
| **V3** | p17 | substantive | Example 1(b) cites "Equation 2a"; the working correctly uses Equation 1 |
| **V4** | p17 | substantive | $\Delta T = 7\ \mathrm{K}$ from rounding before subtracting; should be $6.7\ \mathrm{K}$ |
| **C1** | p14 | cosmetic | kelvin defined via the triple point — the pre-2019 SI definition, since superseded |
| **C2** | p12–13 | cosmetic | text says "curves" (plural) and describes an extrapolation Figure 5 does not draw |

**Verified sound, no flag:**

- Equations 1, 2a, 2b and 3 — all four match standard forms; 2b is the exact inverse of 2a, and 3
  follows from 2a by differencing.
- Fixed points: ice $273.15\ \mathrm{K}/0\ ^\circ\mathrm{C}$, steam $373.15\ \mathrm{K}/100\
  ^\circ\mathrm{C}$, $32\ ^\circ\mathrm{F}$ and $212\ ^\circ\mathrm{F}$. ✓
- Triple point: $0.01\ ^\circ\mathrm{C}$, $4.58\ \mathrm{mmHg}$, $273.16\ \mathrm{K}$. ✓
- The $50\ ^\circ\mathrm{F} = 10\ ^\circ\mathrm{C} = 283\ \mathrm{K}$ check on p15. ✓
- Example 1(a) in full: $22.2\ ^\circ\mathrm{C}$, $28.9\ ^\circ\mathrm{C}$, $6.7\ ^\circ\mathrm{C}$. ✓
- Example 1(b) endpoint conversions $295\ \mathrm{K}$ and $302\ \mathrm{K}$ — correct to three
  significant figures; only their **difference** is affected (V4).
- The zeroth-law statement, all definitions, and the six-property list — standard and internally
  consistent.

**Not a defect:** the text layer renders "hotness"/"coldness" on p3 as `―hotness‖`. The render shows
correct typographic quotation marks — a **text-extraction artefact only**, no ID assigned. Recorded
because it was flagged as a suspected defect before the render was available.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
