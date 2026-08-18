---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "02 — Work, Heat and the First Law of Thermodynamics"
source: "FL — '3.01 First_Law_of_Thermodynamics.pdf', 37 slides"
slides: "1-37"
file_role: topic
subtopics:
  - "Joule equivalent of heat; heat as a form of energy"
  - "the piston-cylinder narrative: work on a gas, heat into a gas, internal energy"
  - "sign conventions for Q and W — the deck states two contradictory ones"
  - "formal statements of the first law; energy balance in total, rate, specific and differential form"
  - "closed-system energy balance"
  - "worked example: isobaric compression of a gas"
  - "constant-pressure processes and the definition of enthalpy"
  - "ideal-gas process equations; isothermal, isobaric, isochoric, adiabatic, polytropic"
  - "energy transfer by work; moving boundary (P dV) work; work as area on a P–V diagram"
  - "equations of state: ideal gas, specific gas constant, compressibility factor Z, reduced properties"
key_equations: [first-law-closed, energy-balance, boundary-work, enthalpy-def, mayer-relation, isothermal, isobaric, isochoric, adiabatic-pv, adiabatic-work, ideal-gas-specific, compressibility-z]
prerequisites: ["01-temperature-thermometry (absolute temperature)"]
leads_to: ["03-second-law-and-cycles", "exercises/ga1-topic1-part1-equations-of-state", "exercises/ga2-topic1-part2-first-law"]
verification_flags: 10
tags: [first-law, work, heat, internal-energy, sign-convention, energy-balance, enthalpy, boundary-work, polytropic, adiabatic, ideal-gas, compressibility-factor, equations-of-state]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered slide · [hist] historical/biographical note ·
  [added] supplied here, NOT in the source ·
  ·FL sN = provenance (which slide the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 02 — Work, Heat and the First Law of Thermodynamics

Scope: the whole of FL, 37 slides. Builds the first law from a piston-cylinder narrative, states it
formally, develops the closed-system energy balance in four forms, defines enthalpy, works the four
elementary ideal-gas processes plus the polytropic family, treats boundary work, and closes with
equations of state — ideal gas, the specific gas constant, and the compressibility factor $Z$.

> ## ⚠ Read §2.3 before using anything else in this file
>
> **FL states two mutually contradictory sign conventions for $W$**, both explicitly, seventeen slides
> apart — and its single worked example mixes them, producing **an answer wrong by a factor
> of five** (5.01×). Four of this file's ten flags come from that one fault line. §2.3 sets out which
> convention to use and how to tell which one a given slide is written in.

**Syllabus note.** `00-index.md` registers FL against Topic 1 §1.3 (Work, Heat & First Law). That is
right for slides 1–33, but **slides 34–37 are §1.2 (Equations of State)** — ideal gas, specific gas
constant, $Z$, reduced properties. FL spans both sections.

---

## 2.1 Heat is a form of energy ·FL s2–s3

[hist ·FL s2] **James Joule** showed that mechanical energy could be converted to heat, and concluded
that **heat was another form of energy**.

[eq] **The Joule equivalent of heat** ·FL s2

$$\boxed{\;1\ \mathrm{cal} = 4.184\ \mathrm{J}\;}$$

Mechanical energy comes in the familiar forms — **KE**, **PE**, total $E$ — and **work is done by
energy transfer**. Since heat is also energy, the conservation-of-energy principle has to be
**expanded to accommodate thermal systems**. That expansion is the first law. ·FL s3

---

## 2.2 Building the first law from a piston and cylinder ·FL s4–s12

FL develops the law in three stages, changing one thing at a time. This is the clearest part of the
deck and worth following exactly.

[fig ·FL s4] A vertical cylinder with a piston and rod, enclosing a **dilute gas** drawn as scattered
dots, **characterised by $P$, $V$, $T$ and $n$**.

### Stage 1 — work only, no heat ·FL s5–s8

[fig ·FL s5–s6] The piston is pushed **inward**; the gas occupies a smaller volume, dots more closely
spaced.

If the container is **insulated**, pushing the piston in makes the temperature rise, the atoms move
faster and the pressure rises. FL then asks: *is there more internal energy in the gas?* ·FL s6

[derivation] The external agent did work in pushing the piston inward: ·FL s7

$$W = Fd = (PA)\,\Delta x \quad\Longrightarrow\quad W = P\,\Delta V$$

> ⚠ VERIFY **V5** ·FL s7 — printed as $W = P\Delta V$. For a **compression** $\Delta V<0$, so
> $P\Delta V$ is **negative**, contradicting the slide's own sentence that the external agent *did
> work on* the gas. The deck's own worked example (·FL s20) writes the same quantity as
> $W = -P\Delta V$. Correct form for work done **on** the gas:
> $$\boxed{\;W_{\text{on}} = -P\,\Delta V\;}$$
> See `_verification-log.md`.

[eq] With no heat transfer, all that work goes into internal energy: ·FL s8

$$\boxed{\;W = \Delta U\;}\qquad\text{(insulated, work done \textbf{on} the gas)}$$

### Stage 2 — heat only, no work ·FL s9–s10

[fig ·FL s9–s10] The piston is **held fixed** at its original location and the cylinder is placed on a
**hot plate** (drawn as a red bar beneath).

Heat flows into the gas, the atoms move faster, the internal energy increases. ·FL s10

- $Q$ — heat, in joules
- $\Delta U$ — change in internal energy, in joules

$$\boxed{\;Q = \Delta U\;}\qquad\text{(constant volume, no work)}$$

### Stage 3 — both at once ·FL s11–s12

[fig ·FL s11–s12] Both together: a force $F$ arrow pressing down on the piston rod **and** the hot
plate beneath.

"Work is done on the gas, heat is added to the gas and the internal energy of the gas increases!" ·FL s12

The slide then prints:

$$Q = W + \Delta U \qquad \text{⚠ V6 — wrong for this deck's stated convention}$$

> ⚠ VERIFY **V6** ·FL s12 — **this is the deck's central fault.** $Q = W + \Delta U$ rearranges to
> $\Delta U = Q - W$, which is the **engineering** convention ($W$ positive when done **by** the
> system). But ·FL s13, the very next slide, states *"work done on the gas is positive"*. Under that
> convention the first law is
> $$\boxed{\;\Delta U = Q + W \quad\Longleftrightarrow\quad Q = \Delta U - W\;}\qquad (W = W_{\text{on}})$$
>
> **One-line self-check.** Set $Q=0$. The slide gives $\Delta U = -W$ — the gas *cools* when you
> compress it. But s6 says the temperature **rises** and s8 says $W = \Delta U$. Three slides
> contradict s12. See `_verification-log.md`.

---

## 2.3 ⚠ Sign conventions — the deck states two, and they conflict ·FL s13, s30

This is the single most important thing in the document. **Both statements below are explicit, in
this one deck.**

**Statement A** ·FL s13 — "Some conventions. For the gases perspective:"

- heat **added** is positive, heat removed is negative;
- **work done ON the gas is positive**, work done by the gas is negative;
- temperature increase means internal energy change is positive.

**Statement B** ·FL s30 — "Energy Transfer by Work":

$$W < 0:\ \text{work done \textbf{on} the system}\qquad W > 0:\ \text{work done \textbf{by} the system}$$

**These are exact opposites.** $Q$ is positive **into** the system in both, so heat is never the
problem — only $W$.

### Which slides use which

| Convention | First law | Slides |
|---|---|---|
| **A — physics** ($W>0$ = work **on**) | $\Delta U = Q + W$ | s7–s8, **s13**, s19–s20 (the example), s23–s28 |
| **B — engineering** ($W>0$ = work **by**) | $\Delta U = Q - W$ | s12, s15–s18, s21, s22, **s30**, s31–s33 |

> ### [added] The working rule — this is what to do in an exam
>
> **Never read a first-law equation without first deciding which convention it is written in.** Two
> tells, either of which settles it in seconds:
>
> 1. **The boundary-work sign.** $W_b = +\int P\,dV$ ⇒ convention **B**. $W = -P\Delta V$ ⇒ **A**.
> 2. **The first law as written.** $\Delta U = Q - W$ ⇒ **B**. $\Delta U = Q + W$ ⇒ **A**.
>
> Then state which one you are using at the top of your answer, and do not change it mid-question.
> **The deck's own example fails precisely by changing it mid-question** (§2.6).
>
> **What the assessed exercises use.** GA2 states *"Q positive into the system; W positive done BY the
> system"* and writes $\Delta U = Q - W$ — **convention B**. So the exercises agree with FL's *second
> half* and disagree with s13. When answering a GA or CAT question, **default to B** unless the
> question says otherwise. Full clash entry in `_nomenclature.md` clash 1.

Also from s30: **heat and work are directional quantities** — a complete description needs magnitude
*and* direction. And **work is a path function**, an inexact differential:

$$\int_1^2 \delta W = W_{12} \quad(\textbf{not }\Delta W), \qquad \delta W \neq W_2 - W_1$$

[fig ·FL s30] Box with $W = 30\ \mathrm{kJ}$, $m = 2\ \mathrm{kg}$, $\Delta t = 5\ \mathrm{s}$, arrow
out marked "30 kJ work", giving $\dot W = 6\ \mathrm{kW}$ and $w = 15\ \mathrm{kJ/kg}$.
*[added] Verified: $30/5 = 6\ \mathrm{kW}$ ✓; $30/2 = 15\ \mathrm{kJ/kg}$ ✓.*

---

## 2.4 Formal statements of the first law ·FL s14

[def] The **first law of thermodynamics** (the conservation of energy principle) provides a sound
basis for studying the relationships among the various forms of energy and energy interactions.

[def] **Energy can be neither created nor destroyed during a process; it can only change forms.** In
other words, the internal energy of an **isolated** system is conserved under any thermodynamical
change.

[def] **The First Law (adiabatic form).** For all adiabatic processes between two specified states of a
closed system, **the net work done is the same** regardless of the nature of the closed system and the
details of the process.

Two consequences FL draws from it:

- the net work must depend on the **end states only**, represented by the total energy $E$;
- the change in total energy during an adiabatic process must equal the net work done.

> [added] **Why the adiabatic statement matters.** It is what licenses $E$ as a **property**: if the
> work between two states is path-independent when $Q=0$, then it defines a state function. That is
> the logical route to $\Delta U$ being well defined, and it is why s15 flags "Energy is a Property".

---

## 2.5 Energy balance ·FL s15–s18

[def] The net change in the total energy of a system during a process equals the difference between
the total energy entering and the total energy leaving. ·FL s15

$$\Delta E_{\text{system}} = E_{\text{final}} - E_{\text{initial}} = E_2 - E_1$$

[eq] The three contributions: ·FL s15

$$\boxed{\;\Delta E = \Delta U + \Delta\mathrm{KE} + \Delta\mathrm{PE}\;}$$

$$\Delta U = m(u_2 - u_1),\qquad
\Delta \mathrm{KE} = \tfrac12 m\left(V_2^2 - V_1^2\right),\qquad
\Delta \mathrm{PE} = mg\left(z_2 - z_1\right)$$

- $m$ — mass, kg · $u$ — **specific** internal energy, J·kg⁻¹ · $V$ — velocity, m·s⁻¹ ·
  $z$ — elevation, m · $g$ — gravitational acceleration, m·s⁻²

$u_1$ and $u_2$ can be read **directly from the property tables** or from thermodynamic property
relations. ·FL s15

> ⚠ VERIFY **C3** ·FL s15 — $V$ is used for **velocity** here, while most of the deck uses $V$ for
> **volume**. (s18 and s30 also use $V$ for velocity, s18 in bold $\mathbf{V}$.) Substituting a volume
> into $\tfrac12 m V^2$ is a whole-answer error. See `_nomenclature.md`.

### The four forms of the balance ·FL s16

$$E_{\text{in}} - E_{\text{out}} = \Delta E_{\text{system}}\quad(\mathrm{kJ})
\qquad\text{any system, any process}$$

$$\dot E_{\text{in}} - \dot E_{\text{out}} = \frac{dE_{\text{system}}}{dt}\quad(\mathrm{kW})
\qquad\text{rate form}$$

$$e_{\text{in}} - e_{\text{out}} = \Delta e_{\text{system}}\quad(\mathrm{kJ/kg})
\qquad\text{per unit mass}$$

$$\delta E_{\text{in}} - \delta E_{\text{out}} = dE_{\text{system}}
\qquad\text{differential form}$$

For a constant rate, $Q = \dot Q\,\Delta t$, $W = \dot W\,\Delta t$, $\Delta E = (dE/dt)\Delta t$.

[eq] **For a cycle** — the result the whole of Topic 3 rests on: ·FL s16

$$\boxed{\;W_{\text{net,out}} = Q_{\text{net,in}}\;}\qquad\text{since }\Delta E = 0\text{ over a cycle}$$

### Closed system ·FL s17–s18

[def] Change in energy contained within the system = net energy transferred **in** by heat transfer −
net energy transferred **out** by work. ·FL s17

The slide then prints:

$$E_1 + W_{1-2} - Q_{1-2} = E_2 \qquad \text{⚠ V7}$$

> ⚠ VERIFY **V7** ·FL s17 — the braces label $W_{1-2}$ as *"Energy gain"* and $Q_{1-2}$ as
> *"Energy loss"*, giving the boxed result above. That is **swapped** relative to the descriptive
> boxes at the top of the same slide (in by heat, out by work) and relative to s18's
> $\Delta E = Q - W$. Correct form:
> $$\boxed{\;E_1 + Q_{1-2} - W_{1-2} = E_2\;}$$
> See `_verification-log.md`.

[eq: first-law-closed] The clean closed-system statement — **use this one**: ·FL s18

$$\boxed{\;\Delta \mathrm{KE} + \Delta \mathrm{PE} + \Delta U = Q - W\;}$$

$$U_2 - U_1 + \tfrac12 m\left(\mathbf{V}_2^2 - \mathbf{V}_1^2\right) + mg\left(Z_2 - Z_1\right)
= {}_1Q_2 - {}_1W_2$$

Differential and rate forms: ·FL s18

$$dE = \delta Q - \delta W, \qquad
\frac{dE}{dt} = \dot Q - \dot W, \qquad
\frac{d\mathrm{KE}}{dt} + \frac{d\mathrm{PE}}{dt} + \frac{dU}{dt} = \dot Q - \dot W$$

All in **convention B**. For a stationary closed system ($\Delta\mathrm{KE} = \Delta\mathrm{PE} = 0$)
this reduces to $\Delta U = Q - W$ — the form the group activities use.

---

## 2.6 [ex] Worked example — isobaric compression ·FL s19–s20

**Statement** ·FL s19

> 25 L of gas is enclosed in a cylinder/piston apparatus at 2 atm of pressure and 300 K. If 100 kg of
> mass is placed on the piston causing the gas to compress to 20 L at constant pressure. This is done
> by allowing heat to flow out of the gas. What is the work done on the gas? What is the change in
> internal energy of the gas? How much heat flowed out of the gas? NB: $PV = nRT$.

**Data as the slide sets it** ·FL s20

$$P_0 = 202{,}600\ \mathrm{Pa},\quad V_0 = 0.025\ \mathrm{m^3},\quad T_0 = 300\ \mathrm{K},$$
$$P_f = 202{,}600\ \mathrm{Pa},\quad V_f = 0.020\ \mathrm{m^3},\quad T_f = \;?$$

> ⚠ VERIFY **C4** ·FL s20 — the data line ends "$T_f =$" with **no value printed**. It must be
> obtained from $PV = nRT$: $T_f = 240\ \mathrm{K}$. Not an error, but the slide cannot be followed as
> printed.

**Method as the slide sets it** ·FL s20

$$n = \frac{PV}{RT},\qquad W = -P\,\Delta V,\qquad \Delta U = \tfrac32 nR\,\Delta T,\qquad Q = W + \Delta U$$

Note $W = -P\Delta V$ — **convention A**, correct for "work done on the gas", and inconsistent with
s7 (V5).

**The slide's working** ·FL s20

$$W = -P\Delta V = -202{,}600\,(0.020 - 0.025) = 1013\ \mathrm{J}\ \text{“energy added to the gas”}$$
$$\Delta U = \tfrac32 nR\Delta T = 1.5(2.03)(8.31)(-60) = -1518\ \mathrm{J}$$
$$Q = W + \Delta U = 1013 - 1518 = -505\ \mathrm{J}\ \text{heat out}\qquad\text{⚠ V8}$$

> ### ⚠ VERIFY **V8** ·FL s20 — the final answer is wrong. $Q = -2532\ \mathrm{J}$, not $-505$.
>
> **What went wrong:** the example takes $W = -P\Delta V$ (convention **A**) and substitutes it into
> $Q = W + \Delta U$ (convention **B**, from V6). Mixing the two inside one calculation flips the sign
> of the work term.
>
> $$\boxed{\;Q = \Delta U - W_{\text{on}} = -1519.5 - 1013.0 = -2532\ \mathrm{J}\;}$$
>
> **Independent confirmation, no first law needed.** For an isobaric process on a monatomic ideal gas,
> $Q = n c_p \Delta T$ with $c_p = \tfrac52 R$:
> $$Q = 2.0317 \times \tfrac52 (8.31)(-60) = -2532\ \mathrm{J}$$
> Exact agreement with the corrected first-law route.
>
> The printed error is $+2026\ \mathrm{J} = 2 \times 1013\ \mathrm{J} = 2W$ — the arithmetic signature
> of a sign flip on $W$. The printed answer is **one fifth** of the correct magnitude.
>
> See `_verification-log.md`.

**[added] The example recomputed in full, corrected:**

| Step | Working | Result |
|---|---|---|
| Moles | $n = P V_0/(R T_0) = 202600(0.025)/(8.31 \times 300)$ | $n = 2.0317\ \mathrm{mol}$ ✓ *(slide: 2.03)* |
| Final temperature | $T_f = P V_f/(nR) = 202600(0.020)/(2.0317 \times 8.31)$ | $T_f = 240.0\ \mathrm{K}$ *(slide: blank)* |
| Temperature change | $\Delta T = 240 - 300$ | $\Delta T = -60\ \mathrm{K}$ ✓ |
| Work **on** the gas | $W = -P\Delta V = -202600(-0.005)$ | $W = +1013\ \mathrm{J}$ ✓ |
| Internal energy | $\Delta U = \tfrac32 nR\Delta T$ | $\Delta U = -1519.5\ \mathrm{J}$ ✓ *(slide: −1518)* |
| **Heat** | $Q = \Delta U - W$ | $\boxed{Q = -2532\ \mathrm{J}}$ ✗ *(slide: −505)* |

Every intermediate quantity on the slide is right. **Only the final step is wrong**, and it is wrong
because of V6.

> **Sanity check worth internalising.** Compress a gas *and* cool it, and both effects remove energy
> relative to the internal-energy change — so the heat out must **exceed** $|\Delta U|$ in magnitude,
> not fall short of it. The printed $|{-505}| < |{-1519}|$ fails that check on sight.

---

## 2.7 Constant-pressure processes and enthalpy ·FL s21

FL is explicit here that **"$Q$ is to the system and $W$ is from the system"** — convention **B**.

[derivation] Closed system, quasi-equilibrium constant-pressure process, $\Delta\mathrm{KE} =
\Delta\mathrm{PE} = 0$: ·FL s21

$$Q - W = \Delta U$$
$$Q - W_{\text{other}} - W_b = U_2 - U_1$$
$$Q - W_{\text{other}} - P_0\left(V_2 - V_1\right) = U_2 - U_1$$
$$Q - W_{\text{other}} = \left(U_2 + P_2V_2\right) - \left(U_1 + P_1V_1\right)$$

[eq: enthalpy-def] The bracket is worth a name — **enthalpy**: ·FL s21

$$\boxed{\;H = U + PV\;}\qquad\text{specific form}\quad h = u + Pv$$

$$\boxed{\;Q - W_{\text{other}} = H_2 - H_1\;}$$

- $H$ — enthalpy, J · $h$ — specific enthalpy, J·kg⁻¹ · $W_b$ — moving-boundary work, J ·
  $W_{\text{other}}$ — all work that is not boundary work (electrical, shaft, …), J

[eq] Boxed on the slide, for a constant-pressure expansion or compression: ·FL s21

$$\boxed{\;\Delta U + W_b = \Delta H\;}$$

[ex ·FL s21] Constant-pressure example: $\mathrm{H_2O}$ in a piston-cylinder, $m = 25\ \mathrm{g}$,
$P_1 = P_2 = 300\ \mathrm{kPa}$, saturated vapour, electrical resistance heating at
$0.2\ \mathrm{A}$ and $120\ \mathrm{V}$ for $5\ \mathrm{min}$, with $Q_{\text{out}} =
3.7\ \mathrm{kJ}$.

$$W_{e,\text{in}} - Q_{\text{out}} - W_b = \Delta U, \qquad
W_{e,\text{in}} - Q_{\text{out}} = \Delta H = m\left(h_2 - h_1\right)$$

[fig ·FL s21] The piston-cylinder with the resistance coil, plus a $P$–$v$ diagram showing the process
$1 \to 2$ as a **horizontal line at 300 kPa**, with state **1 on the saturated-vapour (right) branch of
the dome** and state **2 well to its right in the superheated region**. The process runs *along* the
300 kPa line outside the dome — it does **not** cross the two-phase region. That matches the problem
statement, which starts from saturated vapour and superheats it.

*[added] The slide does not complete the arithmetic. $W_{e,\text{in}} = VI\,\Delta t =
120 \times 0.2 \times 300 = 7200\ \mathrm{J} = 7.2\ \mathrm{kJ}$, so
$\Delta H = 7.2 - 3.7 = 3.5\ \mathrm{kJ}$ and $h_2 - h_1 = 3.5/0.025 = 140\ \mathrm{kJ/kg}$. Solving
for the end state needs steam tables, which FL does not supply.*

> **Why enthalpy exists.** At constant pressure the boundary work is not free information — it is
> fixed by $P\Delta V$. Folding it into $U$ gives a property whose change *is* the heat transferred
> (when $W_{\text{other}} = 0$). That is the entire motivation, and it is why $h$ rather than $u$
> appears in every flow-device analysis.

---

## 2.8 Ideal-gas process equations ·FL s22

Slides 22–28 switch to **molar** quantities: $C_v$, $C_p$ and $R$ per mole, with no $n$ or $m$
multiplying them.

[derivation] For an ideal gas in any **mechanically reversible closed-system process** with
$W_{\text{other}} = 0$: ·FL s22

$$dQ - dW = C_V\,dT \qquad\text{with}\qquad dW = P\,dV \qquad\text{⚠ V9}$$

$$dQ = C_V\,dT + P\,dV \qquad\Longrightarrow\qquad dQ = C_V\,dT + RT\,\frac{dV}{V}$$

Alternatively, with $V = RT/P$:

$$dQ = C_V\,dT + P\,d\!\left(\frac{RT}{P}\right)
= C_V\,dT + P\left(\frac{R}{P}dT - \frac{RT}{P^2}dP\right)$$

$$\boxed{\;dQ = \left(C_v + R\right)dT - RT\,\frac{dP}{P}\;}$$

> ⚠ VERIFY **V9** ·FL s22 — the first two lines are in **convention B** ($dQ - dW = C_V dT$ with
> $dW = P\,dV$), but slides 23–28 that follow are all in **convention A** ($W$ = work on: isothermal
> $W = -RT\ln(V_2/V_1)$, isobaric $W = -R(T_2-T_1)$, adiabatic $W = \Delta U$). Under convention A
> these two lines must read $dQ + dW = C_V\,dT$ and $dW = -P\,dV$. The **third** line
> ($dQ = C_V dT + P dV$) and everything after it are correct in both readings, because the two slips
> cancel. See `_verification-log.md`.

[added] Side note on the slide: the ideal gas constant $R = 8.314\,462\,618\ \mathrm{J\,K^{-1}mol^{-1}}$
is the proportionality constant in $PV = nRT$, $n$ = number of moles.

---

## 2.9 The four elementary processes ·FL s23–s28

All in **convention A** ($W$ = work done **on** the gas), all **molar**. Every one of the four was
checked for internal consistency — all four pass.

### Isothermal ($T$ constant) ·FL s23

$$\Delta U = \Delta H = 0$$
$$\boxed{\;Q = RT\ln\frac{V_2}{V_1} = -RT\ln\frac{P_2}{P_1}\;}$$
$$\boxed{\;W = -RT\ln\frac{V_2}{V_1} = RT\ln\frac{P_2}{P_1}\;}$$
$$Q = -W \qquad (\text{const } T)$$

*[added] Consistent: $\Delta U = Q + W = 0$ ✓, as required when $T$ is constant.*

### Isobaric ($P$ constant) ·FL s24

$$\Delta U = \int C_V\,dT, \qquad \Delta H = \int C_P\,dT$$
$$\boxed{\;Q = \Delta H = \int C_P\,dT\;}, \qquad \boxed{\;W = -R\left(T_2 - T_1\right)\;}$$

*[added] Consistent: $\Delta U = Q + W = \int C_P dT - R\Delta T = \int (C_P - R)\,dT = \int C_V dT$ ✓
— which silently uses the Mayer relation below.*

### Isochoric ($V$ constant) ·FL s25

$$\Delta U = \int C_V\,dT, \qquad \Delta H = \int C_P\,dT$$
$$\boxed{\;Q = \Delta U = \int C_V\,dT\;}, \qquad W = 0 \qquad (\text{const } V)$$

### Adiabatic ($Q = 0$) ·FL s26–s28

[derivation] With $dQ = 0$: ·FL s26

$$\frac{dT}{T} = -\frac{R}{C_V}\frac{dV}{V}$$

Integrating at constant $C_V$:

$$\frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{R/C_V},\qquad
\frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{R/C_P},\qquad
\frac{P_2}{P_1} = \left(\frac{V_1}{V_2}\right)^{C_P/C_V}$$

[eq: adiabatic-pv] In terms of $\gamma$: ·FL s27

$$\boxed{\;TV^{\gamma-1} = \text{constant},\qquad
TP^{(1-\gamma)/\gamma} = \text{constant},\qquad
PV^{\gamma} = \text{constant}\;}$$

$$\gamma \equiv \frac{C_P}{C_V}$$

- $\gamma$ — ratio of the specific heat at constant pressure to that at constant volume,
  dimensionless

Applies to an ideal gas with constant heat capacities undergoing a mechanically reversible adiabatic
process. ·FL s27

**The work of an adiabatic process** ·FL s27

$$dW = dU = C_V\,dT \qquad\Longrightarrow\qquad \boxed{\;W = \Delta U = C_V\,\Delta T\;}$$

[eq: mayer-relation] From $\gamma$ ·FL s28. *[added] The slide prints only the $\gamma$ chain; $C_P - C_V = R$ follows from it in one step but is **never written on the slide**:*

$$\gamma = \frac{C_P}{C_V} = \frac{C_V + R}{C_V} = 1 + \frac{R}{C_V}
\qquad\Longrightarrow\qquad \boxed{\;C_P - C_V = R\;}$$

$$\boxed{\;C_V = \frac{R}{\gamma - 1}\;}$$

> ⚠ VERIFY **C5** ·FL s28 — the third term is printed "$I + R/C_V$" with a capital letter **I** in
> place of the digit **1**. A font/scan artefact, not a physics error.

[eq: adiabatic-work] Therefore ·FL s28

$$W = C_V\,\Delta T = \frac{R\,\Delta T}{\gamma - 1}
= \frac{RT_2 - RT_1}{\gamma - 1} = \frac{P_2V_2 - P_1V_1}{\gamma - 1}$$

$V_2$ is usually not known, and is eliminated:

$$\boxed{\;W = \frac{P_1V_1}{\gamma-1}\left[\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} - 1\right]
= \frac{RT_1}{\gamma-1}\left[\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} - 1\right]\;}$$

*[added] All of §2.9's equations were checked against standard forms — no substantive errors. Note
$C_P - C_V = R$ here is the **molar** Mayer relation; the mass-specific version $c_p - c_v = R_{\text{sp}}$
uses the specific gas constant of §2.12. The group activities assess the specific form.*

---

## 2.10 Polytropic processes ·FL s29

FL uses **$\delta$** for the polytropic index:

| Process | Index |
|---|---|
| Isobaric (constant pressure) | $\delta = 0$ |
| Isothermal | $\delta = 1$ |
| Adiabatic | $\delta = \gamma$ |
| Isochoric (constant volume) | $\delta = \infty$ |

For the isochoric case FL gives $dV/dP = V/(P\delta)$; constant $V$ then requires $\delta \to \infty$.

[fig ·FL s29] $P$–$V$ diagram, four paths from a common initial point: horizontal to the right
($\delta=0$), a shallow curve ($\delta=1$), a steeper curve ($\delta=\gamma$), and vertically
downward ($\delta=\infty$). Caption: "Paths of polytropic processes characterized by specific values
of $\delta$."

> ⚠ VERIFY **C6** ·FL s29 — using $\delta$ for the polytropic index **collides with $\delta$ as the
> inexact-differential operator** ($\delta Q$, $\delta W$) on s16, s18, s30 and s32 of the same deck.
> Most texts write $n$ for the polytropic index — which in this deck collides with $n$ = number of
> moles instead. No symbol is safe here; read from context. See `_nomenclature.md`.

---

## 2.11 Energy transfer by work; boundary work ·FL s30–s33

[eq] ·FL s30

$$W = \int_{t_1}^{t_2} \dot W\,dt = \int_{t_1}^{t_2} \mathbf{F}\cdot\mathbf{V}\,dt$$

(Sign convention as Statement B — see §2.3.)

[def] **Moving boundary work** ($P\,dV$ work) — the expansion and compression work in a
piston-cylinder device. ·FL s32

$$\delta W_b = F\,ds = PA\,ds = P\,dV
\qquad\Longrightarrow\qquad \boxed{\;W_b = \int_1^2 P\,dV \quad(\mathrm{kJ})\;}$$

$P$ is **the pressure at the inner face of the piston**. ·FL s32

- $W_b$ is **positive** → expansion
- $W_b$ is **negative** → compression

[def] **Quasi-equilibrium process** — a process during which the system remains nearly in equilibrium
at all times. ·FL s32

[fig ·FL s32] Piston-cylinder with gas at pressure $P$ pushing up on a piston of area $A$ through
displacement $ds$, force $F$ arrow upward; a second sketch labels "the moving boundary" as the dashed
outline round the gas. Title is printed **"Moving Boundary Woek"** — typo for "Work" (C7).

[def] For simple compressible substances in reversible processes, the work done is **the area under
the curve on a $P$–$V$ diagram**. ·FL s31, s33

$$\text{Area} = A = \int_1^2 dA = \int_1^2 P\,dV$$

[fig ·FL s31] Three panels: measured $P$–$V$ data with a curve fit; a $P$–$V$ plot with two different
paths A and B from state 1 to state 2, shaded "Area = work for process A"; and a $P$–$V$ plot with the
shaded strip $\delta W = p\,dV$ between $V_1$ and $V_2$, alongside a piston-cylinder with the piston
travelling from $x_1$ to $x_2$.

[fig ·FL s33] Three panels. **Left:** the $dA = P\,dV$ area strip with a piston sketch. **Upper right:**
three paths between the same two states with $W_A = 10\ \mathrm{kJ}$, $W_B = 8\ \mathrm{kJ}$,
$W_C = 5\ \mathrm{kJ}$ — the boundary work depends on **the path followed as well as the end states**.
**Lower right:** a closed loop, state **2 upper-left** and state **1 lower-right**, traversed
$2 \to A \to 1 \to B \to 2$, with the enclosed area shaded $W_{\text{net}}$ — the net work of a cycle is
the difference between the work done **by** and the work done **on** the system.

> **The two results to carry into Topic 3.** Work is a *path* function (three different answers between
> the same two states), and the **enclosed area of a closed loop on a $P$–$V$ diagram is the net work
> of the cycle**. Every engine cycle in `04-` and `05-` is read off a diagram this way.

---

## 2.12 Equations of state ·FL s34–s37

*(Syllabus §1.2 — assessed in GA1 Part B.)*

[def] An **equation of state** is any equation that relates the pressure, temperature and **specific
volume** of a substance. The simplest and best known is the ideal-gas equation of state, which
predicts $P$–$v$–$T$ behaviour quite accurately within a properly selected region. ·FL s34

[eq: ideal-gas-specific] ·FL s34

$$P = R\left(\frac{T}{v}\right) \qquad\Longleftrightarrow\qquad \boxed{\;Pv = RT\;}$$

$$\boxed{\;R = \frac{R_u}{M}\;}\qquad (\mathrm{kJ\,kg^{-1}K^{-1}}\ \text{or}\ \mathrm{kPa\,m^3\,kg^{-1}K^{-1}})$$

- $R$ — **specific** gas constant of the substance
- $R_u$ — **universal** gas constant
- $M$ — molar mass, kg·kmol⁻¹
- $v$ — specific volume, m³·kg⁻¹

**The universal gas constant in six unit systems** ·FL s34

$$R_u = \begin{cases}
8.31447\ \mathrm{kJ\,kmol^{-1}K^{-1}}\\
8.31447\ \mathrm{kPa\,m^3\,kmol^{-1}K^{-1}}\\
0.0831447\ \mathrm{bar\,m^3\,kmol^{-1}K^{-1}}\\
1.98588\ \mathrm{Btu\,lbmol^{-1}R^{-1}}\\
10.7316\ \mathrm{psia\,ft^3\,lbmol^{-1}R^{-1}}\\
1545.37\ \mathrm{ft\,lbf\,lbmol^{-1}R^{-1}}
\end{cases}$$

**Specific gas constants** ·FL s34 — "Different substances have different gas constants."

| Substance | $R$, kJ·kg⁻¹·K⁻¹ |
|---|---|
| Air | 0.2870 |
| Helium | 2.0769 |
| Argon | 0.2081 |
| Nitrogen | 0.2968 |

> **This resolves the gas-constant clash.** The group activities' $R = 0.297\ \mathrm{kJ\,kg^{-1}K^{-1}}$
> for $\mathrm{N_2}$ is exactly this table's 0.2968 rounded. So $PV = mRT$ in the exercises and
> $PV = nR_uT$ in §2.8 are the same equation in different bases — **not** a contradiction. Full entry
> in `_nomenclature.md` clash 2. *[added] Check: $R_u/M = 8.31447/28.013 = 0.2968$ ✓.*

### Compressibility factor $Z$ ·FL s35–s36

[def] The **compressibility factor** $Z$ accounts for the deviation of real gases from ideal-gas
behaviour at a given temperature and pressure. ·FL s35

$$\boxed{\;Pv = ZRT\;}\qquad
Z = \frac{Pv}{RT} = \frac{v_{\text{actual}}}{v_{\text{ideal}}}$$

- $Z = 1$ — ideal gas
- $Z > 1$, $Z = 1$, $Z < 1$ — real gases
- **the farther $Z$ is from unity, the more the gas deviates from ideal behaviour**

Gases behave ideally at **low densities** — low pressure, high temperature. ·FL s35

[exercise ·FL s35] **Question:** what is the criterion for low pressure and high temperature?
**Answer** (given on the slide): the pressure or temperature of a gas is high or low **relative to its
critical temperature or pressure**. At very low pressures all gases approach ideal-gas behaviour,
regardless of their temperature.

[eq] **Reduced properties** ·FL s36

$$P_R = \frac{P}{P_{cr}}, \qquad T_R = \frac{T}{T_{cr}}, \qquad
v_R = \frac{v_{\text{actual}}}{RT_{cr}/P_{cr}}$$

$v_R$ is the **pseudo-reduced specific volume**. $Z$ follows from $P_R$ and $T_R$ — or from $P_R$ and
$v_R$ — read off the generalised compressibility chart (the slide cites **Fig. A–15**). ·FL s36

[fig ·FL s36] The generalised compressibility chart: $Z = Pv/RT$ on the vertical axis against reduced
pressure $P_R$ from 0 to 7 horizontally, with isotherm curves labelled $T_R = 1.00,\ 1.10,\ 1.20,\
1.30,\ 1.50,\ 2.00$ and scattered data points for ten substances (methane, ethylene, ethane, propane,
$n$-butane, iso-pentane, $n$-heptane, nitrogen, carbon dioxide, water), noted as an average curve
based on hydrocarbon data. Caption: "Comparison of $Z$ factors for various gases." A second sketch, $T$
against $v$, marks the region round the critical point as "Nonideal-gas behavior" with "Ideal-gas
behavior" far from it — **gases deviate most in the neighbourhood of the critical point**.

> **Do not read the chart off this file.** The chart is third-party material and is not reproduced
> here (`docs/kb-format.md` § What never gets committed). Use the slide, or any standard
> generalised compressibility chart.

### Other equations of state ·FL s37

FL gives three. Beattie-Bridgeman and Benedict-Webb-Rubin are in molar form ($\bar v$ = molar specific volume); the virial is printed with plain $v$:

**Beattie-Bridgeman**

$$P = \frac{R_uT}{\bar v^2}\left(1 - \frac{c}{\bar v T^3}\right)\left(\bar v + B\right) - \frac{A}{\bar v^2}$$
$$A = A_0\left(1 - \frac{a}{\bar v}\right), \qquad B = B_0\left(1 - \frac{b}{\bar v}\right)$$

Constants in Table 3–4; reasonably accurate for densities up to about $0.8\rho_{cr}$.

**Benedict-Webb-Rubin**

$$P = \frac{R_uT}{\bar v} + \left(B_0R_uT - A_0 - \frac{C_0}{T^2}\right)\frac{1}{\bar v^2}
+ \frac{bR_uT - a}{\bar v^3} + \frac{a\alpha}{\bar v^6}
+ \frac{c}{\bar v^3T^2}\left(1 + \frac{\gamma}{\bar v^2}\right)e^{-\gamma/\bar v^2}$$

Constants in Table 3–4; handles densities up to about $2.5\rho_{cr}$.

**Virial**

$$P = \frac{RT}{v} + \frac{a(T)}{v^2} + \frac{b(T)}{v^3} + \frac{c(T)}{v^4} + \frac{d(T)}{v^5} + \cdots$$

The coefficients $a(T)$, $b(T)$, $c(T)$, … , functions of temperature alone, are the **virial
coefficients**. ·FL s37

> ### ⚠ **Van der Waals is NOT in FL.** This is a real, examinable gap.
>
> `00-index.md`'s gap map asked whether the "Other Equations of State" slide taught Van der Waals,
> since **GA1 Part B assesses it** — including the constants $a$ and $b$. It does not. The slide
> jumps from the ideal gas straight to Beattie-Bridgeman, Benedict-Webb-Rubin and the virial
> expansion, none of which the exercises use.
>
> **Nothing anywhere in FL states the Van der Waals equation.** It must be supplied from outside the
> deck. Standard form, `[added]`:
>
> $$\left(P + \frac{a}{v^2}\right)\left(v - b\right) = RT
> \qquad\text{with}\qquad a = \frac{27R^2T_{cr}^2}{64P_{cr}},\quad b = \frac{RT_{cr}}{8P_{cr}}$$
>
> $a$ corrects for intermolecular attraction, $b$ for the finite volume of the molecules. Note
> $\gamma$ appears in the Benedict-Webb-Rubin constants on this slide **and** as $C_P/C_V$ on s27, and
> $a$, $b$, $c$ appear as Beattie-Bridgeman/virial constants **and** as Van der Waals constants in
> GA1 — see `_nomenclature.md`.

---

### Cross-references

- Absolute temperature, required by every equation in this file → **01-temperature-thermometry**.
- $W_{\text{net,out}} = Q_{\text{net,in}}$ for a cycle (§2.5) and the $P$–$V$ enclosed-area result
  (§2.11) are the foundation of **03-second-law-and-cycles** and the engine cycles in **04-**, **05-**.
- Enthalpy (§2.7) is what the steady-flow energy equation is written in — assessed in GA2, and the
  SFEE itself is **not** in FL.
- The sign-convention clash is the headline entry of `_nomenclature.md`; all nine flags are in
  `_verification-log.md`.
- $Z$, reduced properties and Van der Waals are assessed in
  **exercises/ga1-topic1-part1-equations-of-state**; the first law in
  **exercises/ga2-topic1-part2-first-law**.

### Verification notes for this section

All 37 slides read from **170 dpi renders**. Every numerical claim recomputed independently. **10 flags
— 5 substantive, 5 cosmetic** — of which four (V5–V8) are the same underlying fault: the deck does not
hold one sign convention.

| ID | Slide | Class | Summary |
|---|---|---|---|
| **V5** | s7 | substantive | $W = P\Delta V$ for work done **on** the gas; should be $-P\Delta V$ |
| **V6** | s12 | substantive | $Q = W + \Delta U$ contradicts s13's stated convention and s6/s8 |
| **V7** | s17 | substantive | $Q$ and $W$ swapped vs the slide's own boxes; should be $E_1 + Q - W = E_2$ |
| **V8** | s20 | substantive | worked example gives $Q = -505\ \mathrm{J}$; correct is $-2532\ \mathrm{J}$ |
| **V9** | s22 | substantive | $dQ - dW = C_VdT$ with $dW = P\,dV$, inconsistent with s23–s28 |
| **C3** | s15 | cosmetic | $V$ used for velocity where the deck elsewhere uses $V$ for volume |
| **C4** | s20 | cosmetic | $T_f$ left blank in the data; must be computed ($240\ \mathrm{K}$) |
| **C5** | s28 | cosmetic | "$I + R/C_V$" — capital I for the digit 1 |
| **C6** | s29 | cosmetic | $\delta$ as polytropic index collides with $\delta$ as inexact differential |
| **C7** | s32 | cosmetic | title printed "Moving Boundary **Woek**" *(noted inline at the s32 figure)* |

**Verified sound, no flag:**

- $1\ \mathrm{cal} = 4.184\ \mathrm{J}$ ✓ · the four energy-balance forms (s16) ✓ ·
  $W_{\text{net,out}} = Q_{\text{net,in}}$ ✓ · $\Delta\mathrm{KE}+\Delta\mathrm{PE}+\Delta U = Q-W$ (s18) ✓
- Enthalpy derivation s21, all four algebraic steps ✓ · $H = U + PV$ ✓ · $\Delta U + W_b = \Delta H$ ✓
- $dQ = (C_v + R)dT - RT\,dP/P$ (s22, third line onward) ✓ — algebra correct
- All four elementary processes (s23–s28) — each checked for internal consistency against
  $\Delta U = Q + W$; **all four pass**
- Adiabatic relations $TV^{\gamma-1}$, $TP^{(1-\gamma)/\gamma}$, $PV^\gamma$ ✓ ·
  $C_V = R/(\gamma-1)$ ✓ · $C_P - C_V = R$ ✓ · the eliminated-$V_2$ adiabatic work expression ✓
- Polytropic index values $\delta = 0, 1, \gamma, \infty$ ✓
- $W_b = \int P\,dV$, path dependence, cycle-area result ✓
- $\dot W = 6\ \mathrm{kW}$, $w = 15\ \mathrm{kJ/kg}$ from $30\ \mathrm{kJ}$, $2\ \mathrm{kg}$,
  $5\ \mathrm{s}$ (s30) ✓ recomputed
- $Pv = RT$, $R = R_u/M$, all six $R_u$ unit forms, all four specific gas constants ✓ recomputed
  ($8.31447/28.013 = 0.2968$ for $\mathrm{N_2}$)
- $Pv = ZRT$, $Z$ definitions, reduced properties, Beattie-Bridgeman / Benedict-Webb-Rubin / virial
  forms ✓ all match standard references
- **Example s20 intermediates** — $n = 2.03$, $\Delta T = -60\ \mathrm{K}$, $W = +1013\ \mathrm{J}$,
  $\Delta U = -1518\ \mathrm{J}$ all ✓. Only the final $Q$ is wrong (V8).

**Gap-map rows resolved by this build:**

| Row | Verdict |
|---|---|
| Van der Waals equation, constants $a$, $b$ | ❌ **NOT taught.** s37 gives Beattie-Bridgeman, Benedict-Webb-Rubin, virial. Assessed in GA1 Part B — real gap, supplied `[added]` in §2.12. |
| Compressibility factor $Z$, $Z \gtrless 1$ | ✅ **taught in full**, s35–s36, with reduced properties and the chart |
| Specific heats, $c_p - c_v = R$ | ✅ **taught**, s28 (molar form, via $\gamma$) |
| Enthalpy $h = u + Pv$ | ✅ **taught and derived**, s21 |
| Steady-flow energy equation | ❌ **not in FL** — still outstanding, assessed in GA2 |
| Property / steam tables | referenced (s15, s21) but **not reproduced** |

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
