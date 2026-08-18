---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "03a — Phase Behaviour, Vapour Pressure and Equilibrium"
source: "EPC — '3.02 - Energy Equations and Phase Changes.pdf', slides 1–21 of 92"
slides: "1-21"
file_role: topic
subtopics:
  - "matter and the three phases; particle-level description of solid, liquid, gas"
  - "evaporation, the Maxwell–Boltzmann speed distribution and escape from a liquid"
  - "vapour pressure and dynamic equilibrium in a closed vessel"
  - "boiling as the condition p_vap = p_atm; boiling under vacuum"
  - "liquid nitrogen — boiling point, latent heat, safety, heat ingress"
  - "atmospheric composition; sublimation of CO2"
  - "mechanical, chemical and thermal equilibrium; thermodynamic equilibrium"
key_equations: []
prerequisites: ["01-temperature-thermometry"]
leads_to: ["03b-second-law-and-cycles"]
verification_flags: 5
tags: [phases-of-matter, vapour-pressure, boiling, evaporation, liquid-nitrogen, equilibrium, thermodynamic-equilibrium, sublimation]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered slide · [hist] historical/biographical note ·
  [added] supplied here, NOT in the source ·
  ·EPC sN = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md. -->

# 03a — Phase Behaviour, Vapour Pressure and Equilibrium

Scope: EPC slides 1–21, the first of the document's two independent halves. Qualitative,
particle-level treatment of the three phases, evaporation and vapour pressure, boiling, liquid
nitrogen as a worked physical case, atmospheric composition, and the several kinds of equilibrium that
the second law then builds on.

> **Why EPC is split into 03a and 03b.** `docs/kb-format.md` splits a document into `NNa`/`NNb` when it
> covers **two genuinely independent themes** *and* exceeds ~25 KB. EPC does both. Slides 1–21 are
> phase behaviour and equilibrium — qualitative, no equations at all. Slides 22–92 are the second law,
> heat engines, Carnot and the Diesel cycle — quantitative, and the spine the Topic 3 decks (TC, HE)
> build on. They share no equations and only one concept (thermal equilibrium). Keeping them in one
> file would bury the second law behind twenty slides of particle pictures.
>
> *(EPC's own title page calls the whole document **Topic 2**. The `03a`/`03b` numbering is this
> knowledge base's file ordering, not the lecturer's topic numbering.)*

> ### ⚠ There is not a single equation in this entire half
>
> Slides 1–21 contain **no formulae and no symbols to substitute into**. That is a deliberate scoping
> observation, not an omission in this file: everything here is definitional or descriptive, and the
> examinable content is the **vocabulary** and the **physical reasoning**, not any calculation.

> ### ⚠ Every figure in this half is a third-party textbook scan
>
> Slides 8, 10, 11 and 13 reproduce scanned pages from **Silberberg, *Chemistry: The Molecular Nature
> of Matter and Change*, 2nd ed., McGraw-Hill** — each carries the three-line credit, and halftone dots
> and show-through text from the reverse of the page are visible. **Slide 19's figure is also plainly a
> book scan** (halftone screen, show-through text) but carries **no credit**, so its source is
> unidentified. `docs/kb-format.md` § What never gets committed forbids reproducing them, so
> they are **described here, never copied**. Consult the slides for the images themselves.

---

## 3a.1 Matter and the three phases ·EPC s3–s7

[def] **Matter** occupies space and has mass. It is composed predominantly of atoms, which consist of
protons, neutrons and electrons. ·EPC s3 *(attributed on the slide to Wikipedia)*

The three phases, as EPC characterises them: ·EPC s4–s7

| | **Solid** ·s5 | **Liquid** ·s6 | **Gas** ·s7 |
|---|---|---|---|
| Shape | holds its own shape | takes the shape of the container | takes the shape of the container |
| Volume | fixed | fixed | no fixed volume |
| Spacing | packed close together | close together | — |
| Position | fixed relative to neighbours | — | completely disordered state |
| Motion | vibrate (not visible) | vibrate and rotate | rotating and translating |
| Exists | below melting temperature | between freezing and vaporising temperatures | above condensation temperature |

> ⚠ VERIFY **V17** ·EPC s7 — the slide prints *"No forces holing molecules together"*. Beyond the
> `holing`/`holding` typo, **zero intermolecular force is a physically wrong claim** and contradicts
> the same slide's last bullet: a gas with no attractive forces could never condense, yet the slide
> says a gas "can only exist above condensation temperature". Slide 10's own figure is labelled
> "intermolecular forces in liquid". Should read **negligible (very weak) forces**. See
> `_verification-log.md`.

> ⚠ VERIFY **C11** ·EPC s6 — liquid particles are described as able to "vibrate and rotate", omitting
> **translation**. But the same slide's first bullet says a liquid takes the shape of its container,
> which requires molecules to slide past one another. The standard three-tier picture is: solid =
> vibrate only; liquid = vibrate + rotate + hindered translation; gas = free translation.

---

## 3a.2 Evaporation and the speed distribution ·EPC s8–s10

**The mechanism** ·EPC s8

- The particles are bouncing into each other and transferring energy.
- When the particles at the surface have enough energy they **escape**.
- In an open container this continues until all the liquid is gone.

[def] **Temperature and particle speed** ·EPC s9

- At a given temperature there are particles moving at **every** speed.
- **The temperature describes the most probable speed.**

That second statement is the load-bearing one: temperature is not "the speed of the molecules" but the
peak of a distribution, which is why evaporation happens well below the boiling point.

[fig ·EPC s10] Maxwell–Boltzmann speed distribution (Silberberg scan). Vertical axis *"Fraction of
molecules with a given speed"*, horizontal axis *"Speed"*, **neither axis carrying numbers**. Two
curves: a taller, narrower **blue** curve labelled $T_1$ peaking at $u_1$; a lower, broader **red**
curve labelled $T_2 > T_1$ peaking at $u_2 > u_1$, with dashed verticals dropping to each peak. A
threshold line to the right of $u_2$ is annotated *"Kinetic energy needed to overcome intermolecular
forces in liquid"*; the areas beyond it are shaded and annotated *"Molecules moving fast enough to
vaporize at $T_1$ and $T_2$"* — the $T_2$ area is visibly much larger. Two inset boxes show more
fast-moving molecules in the vapour space above the liquid at $T_2$ than at $T_1$.

> **What to take from Figure s10.** Raising the temperature shifts the peak only modestly but
> multiplies the **tail area** beyond the escape threshold. That non-linear tail growth is why vapour
> pressure rises steeply with temperature (§3a.3) rather than linearly.

> ⚠ VERIFY **C17a** ·EPC s8 — the title and bullets describe an **open** container ("Glass of water
> left on a table", "In an open container…"), but the figure shows a **stoppered flask with a closed
> stopcock**. The arrows (upward only) are right for net evaporation; the vessel drawn is not the
> vessel described. The same artwork is reused correctly on s11, where a closed vessel *is* the point.

---

## 3a.3 Vapour pressure ·EPC s11–s12

[def] **Cover the container.** The pressure exerted by the gas at equilibrium is called the **vapour
pressure**. ·EPC s11

[fig ·EPC s11] The same flask, now at dynamic equilibrium: the vapour space is tinted and holds ~10
molecules in motion, and **four arrows cross the liquid surface — two down, two up** — depicting equal
rates of evaporation and condensation.

**Vapour pressure depends on temperature.** EPC then poses three questions it does not answer: ·EPC s12

- What will happen if all the gas is removed?
- What will happen if more gas is added?
- What will happen when the temperature is increased?

> [added] **Answers, since the slide leaves them open.** Remove the gas and evaporation resumes until
> the vapour pressure is re-established — the *equilibrium* value is a property of the liquid and
> temperature, not of how much vapour is present. Add more vapour and the excess condenses, again
> returning to the same value. Raise the temperature and the vapour pressure **rises steeply**, by the
> tail-area argument of §3a.2.
>
> The general principle: **vapour pressure at equilibrium is a function of temperature alone** (for a
> pure substance), independent of the container volume or the amount of liquid present.

---

## 3a.4 Boiling ·EPC s13

[def] A substance will **boil when the vapour pressure is equal to the atmospheric pressure**. ·EPC s13

Water boils at $100\ ^\circ\mathrm{C}$ — *at standard atmospheric pressure*; see the flag below.

[exercise ·EPC s13] **What will happen to cool water in a vacuum?**

> [added] **It boils.** Lower the ambient pressure far enough and the condition
> $p_{\text{vap}} = p_{\text{amb}}$ is met at room temperature — water boils at about
> $23\ ^\circ\mathrm{C}$ under $2.8\ \mathrm{kPa}$. Boiling is set by the *pressure* condition, not by
> reaching any particular temperature. This is the single most useful idea on the slide.

[fig ·EPC s13] Vapour-pressure curves for three liquids (Silberberg scan). Vertical axis *"Vapor
pressure"* in **kPa** — the tick labels and the unit are **white-box overlays pasted over the book's
original torr labels**, reading 13.33, 26.66, 39.99, 53.32, 66.66, 79.99, 93.32, 101.32 (arrowed),
106.65, 119.99. Horizontal axis *"Temperature (°C)"* from 0 to 100. Three steeply rising curves:
**diethyl ether** (leftmost), **ethanol**, **water** (rightmost). A **horizontal dashed line at
$101.32\ \mathrm{kPa}$** crosses them at the printed normal boiling points **34.5 °C**, **78.5 °C**
and **100.0 °C**. Dashed construction lines at 20 °C show each liquid's vapour pressure at room
temperature.

*[added] Every number on this figure was verified. The torr→kPa overlay is faithful:
$100\ \mathrm{torr} = 13.332\ \mathrm{kPa}$, … , $760\ \mathrm{torr} = 101.325\ \mathrm{kPa}$ ✓. The
three boiling points match literature values (34.6, 78.37, 100.0 °C) ✓.*

> ⚠ VERIFY **C11b** ·EPC s13 — "Water boils at 100ºC." is printed without its condition, and is then
> contradicted by the slide's own third bullet about water in a vacuum. Should read *at standard
> atmospheric pressure*. No number changes.

---

## 3a.5 Liquid nitrogen ·EPC s14–s16

The course's worked physical case for phase change. ·EPC s14

- Nitrogen is normally a **gas** at room temperature and pressure.
- Its vapour pressure equals atmospheric pressure at $-195.79\ ^\circ\mathrm{C}$ — i.e. that is its
  **normal boiling point**.
- **A liquid cannot exceed its boiling temperature.**
- **All heat added to a boiling liquid is used to change phase.**

*[added] Verified: $-195.79\ ^\circ\mathrm{C} = 77.36\ \mathrm{K}$, the accepted normal boiling point
of $\mathrm{N_2}$ ✓.*

> **The two bolded bullets are the examinable physics.** They are the statement that a phase change
> happens at **constant temperature**, with the energy going into **latent heat** rather than into
> raising $T$. That is the idea EPC's later phase-change material and the steam tables both rest on.

**Where does liquid nitrogen take heat from?** All three modes: ·EPC s15

- **Radiation** — infrared light.
- **Conduction** — through the container it is in.
- **Convection** — air around the material cools, becomes more dense and falls, and warm air moves in
  to fill the space.

**Safety** ·EPC s16 — do not touch liquid nitrogen or any object cooled by it (cold enough to cause
frostbite very quickly); wear goggles; know where it is.

---

## 3a.6 Atmospheric composition ·EPC s17

| Gas | Fraction |
|---|---|
| Nitrogen $\mathrm{N_2}$ | 78.084 % |
| Oxygen $\mathrm{O_2}$ | 20.946 % |
| Argon $\mathrm{Ar}$ | 0.934 % |
| Carbon dioxide $\mathrm{CO_2}$ | 0.039 % |
| Water vapour | "maybe some" |

- **Carbon dioxide does not turn to liquid at standard pressure** — it *sublimes*.
- Water is solid below $0\ ^\circ\mathrm{C}$.

*[added] The CO₂ claim verified: the $\mathrm{CO_2}$ triple point is at $5.11\ \mathrm{atm}$
($518\ \mathrm{kPa}$), **above** atmospheric, so at $101.325\ \mathrm{kPa}$ solid goes directly to gas
at $-78.5\ ^\circ\mathrm{C}$ ✓. This is why dry ice smokes rather than puddles — a good exam example of
a triple point above 1 atm.*

> ⚠ VERIFY **C10** ·EPC s17 — two small issues with the table. **(a)** The four figures sum to
> $100.003\ \%$, slightly over 100 % and leaving no room for the trace gases (Ne, He, CH₄, Kr); tables
> using $\mathrm{CO_2} = 0.036\ \%$ sum to exactly 100. **(b)** $0.039\ \% = 390\ \mathrm{ppm}$ is the
> atmospheric $\mathrm{CO_2}$ level of about 2010; it is now nearer $0.043\ \%$. Neither affects any
> calculation in this course. Reproduce the printed values.

---

## 3a.7 Equilibrium ·EPC s19–s21

[exercise ·EPC s18] **What happens when the pressure is increased?**

> [added] **The vapour condenses.** Raising the pressure above the vapour pressure at that temperature
> pushes the substance across its phase boundary — the condition for equilibrium between liquid and
> vapour is $p_{\text{applied}} = p_{\text{vap}}(T)$, so exceeding it drives net condensation until the
> pressure falls back. This is the pressure-side mirror of §3a.4's boiling condition, and it is why
> gases liquefy under compression at constant temperature.

[def] **Equilibrium** — a state in which opposing forces or influences are balanced; a state of
physical balance. ·EPC s19

[fig ·EPC s19] Vapour pressure (at constant $T$) against time: a red curve rises steeply, bends over
and flattens onto a plateau. A vertical dashed line divides the plot — to its left
$\text{Rate}_{\text{vap}} > \text{Rate}_{\text{cond}}$, to its right
$\text{Rate}_{\text{vap}} = \text{Rate}_{\text{cond}}$, labelled **Equilibrium**. No numbers on either
axis.

**The three criteria** ·EPC s20

| Type of equilibrium | Criterion |
|---|---|
| **Mechanical** | equality of **pressures** |
| **Chemical** | equality of **chemical potentials** |
| **Thermal** | equality of **temperatures** |

*[added] EPC omits **phase equilibrium** (equality of chemical potential of each component across
phases), which the standard list includes. Not an error — just an incomplete list.*

[def] **Thermodynamic equilibrium** ·EPC s21

- A thermodynamic system exists in a state of thermodynamic equilibrium when **no change in any
  macroscopic property** is registered if the system is isolated from its surroundings.
- An isolated system always reaches, in the course of time, a state of thermodynamic equilibrium **and
  can never depart from it spontaneously**.

> **That second sentence is the second law in disguise.** "Can never depart from it spontaneously" is
> a directional claim — the kind the first law cannot make. It is the bridge into **03b**, which opens
> by asking exactly why direction exists.
>
> Note also how this completes the chain from `01-temperature-thermometry`: the **zeroth** law gave
> thermal equilibrium its meaning; here it becomes one of three coordinate conditions; in 03b the
> failure of a system to leave equilibrium becomes the second law.

---

### Cross-references

- Thermal equilibrium and the zeroth law → **01-temperature-thermometry** §1.2–1.3.
- Latent heat and the constant-temperature phase change (§3a.5) are the physical basis for the steam
  tables referenced in **02-first-law** §2.7.
- Direction, spontaneity and the second law → **03b-second-law-and-cycles**.

### Verification notes for this section

All 21 slides read from **165 dpi renders**. **There is no arithmetic in this half beyond the figure
annotations**, and every number that does appear was recomputed and checks out — the torr→kPa axis
overlay on s13, the three boiling points, nitrogen's $-195.79\ ^\circ\mathrm{C}$, and the
$\mathrm{CO_2}$ sublimation claim.

| ID | Slide | Class | Summary |
|---|---|---|---|
| **V17** | s7 | substantive | "No forces holding molecules together" — contradicts condensation, and s7's own last bullet |
| **C10** | s17 | cosmetic | composition sums to 100.003 %; $\mathrm{CO_2}$ at 0.039 % is a ~2010 value |
| **C11** | s6 | cosmetic | liquid particle motion omits translation |
| **C11b** | s13 | cosmetic | "Water boils at 100 ºC" lacks its pressure condition, and is contradicted by the same slide's vacuum question |
| **C17a** | s8 | cosmetic | open-container text, closed-flask figure |

**Slide coverage:** all 21 slides are represented. Slide 2 is a divider ("Effects of Temperature and Pressure on Phases of Matter"); slide 18 carries the open question now recorded in §3a.7.

**Also noted, not flagged:** a cluster of spelling and grammar slips — `it's` for `its` (s5, s15),
`holing` (s7), `until the all the liquid` (s8) — collected in `_verification-log.md` rather than here.
Slide 17 and slide 13 carry **no title**. Slides 2 and 18 are dividers only. Slide 10 is image-only.

**Every figure in this half is a textbook scan** — four credited to Silberberg (s8, s10, s11, s13) and one uncredited (s19). All are described, never reproduced.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
