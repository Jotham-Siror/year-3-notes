---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
file_role: formula-sheet
tiers:
  tier_1_primary: "The course's own lecture notes, 100 pp. Cited ·J p{page}. Flags JV{n}.{m} / JC{n}.{m}. Topic files 01–07."
  tier_2_supporting: "Seven lesson handouts, 1–27 pp. each. Cited ·L{n} p{page}. Flags V{n}.{m} / C{n}.{m}. Topic files 11–17."
source: "Part A — 01-matter-atoms-and-semiconductors.md … 07-field-effect-transistors.md · Part B — 11-diodes.md … 17-multistage-feedback-frequency-response.md"
purpose: "Every key equation from both tiers in one place, each tagged to its source page. All forms given here are the CORRECTED forms; where the printed page differs, the flag ID is noted. Where the two tiers give the same result, the row says so."
scope: "Tier 1 complete (·J p2–p100). Tier 2 complete (L1–L7). Extend if further material arrives."
tags: [formula-sheet, analogue-electronics, atoms, semiconductors, resistors, network-theorems, capacitors, inductors, transformers, diodes, rectifiers, filters, regulation, bjt, fet, mosfet, fabrication, h-parameters, amplifiers, feedback, frequency-response, reference]
---

# Formula sheet — Analogue Electronics I (BEE 3103)

Both tiers of the knowledge base, in one file.

- **Part A** is **tier 1**: the course's own lecture notes, cited **·J p{page}**, flagged
  `JV{n}.{m}` (substantive) and `JC{n}.{m}` (cosmetic). This is what the course actually teaches.
- **Part B** is **tier 2**: the seven lesson handouts, cited **·L{n} p{page}**, flagged `V{n}.{m}`
  and `C{n}.{m}`. Fuller textbook treatment, and the *only* source for several topics.

Three rules govern this file.

1. **Every equation below is given in its corrected form.** Where the printed page differs, the
   flag ID is appended in the last column — e.g. ⚠ JV4.3, ⚠ V2.2 — and the entry points into
   `_verification-log.md`, which records what the page actually prints. Never assume a source
   agrees with a flagged row.
2. **Anything marked `[added]` is not in any source.** It is standard material supplied to fill a
   gap the notes leave open, and it is labelled so that it is never mistaken for course material.
3. **Where the two tiers give the same result, the row says so.** Agreement between two
   independent sources is itself information: it raises confidence in the result, and it is what
   settles a question when one source's page is defective. The pairings are collected in the
   **concordance** after Part B; individual rows carry a **⇄** marker pointing at their opposite
   number.

A dagger † in the tag column marks a result that is boxed in its topic file but carries no
`[eq:]` tag of its own.

Citations follow the repository scheme. **·J p{page}** is the PDF page of the lecture notes — the
document's own printed number runs one behind, so PDF p33 shows printed "32". **·L{n} p{page}** is
the PDF page of lesson handout $n$.

---

# Part A — tier 1, the lecture notes ·J

Seven topic files, ·J p2–p100. One section per file, in order.

---

## A1 · Matter, atoms and semiconductors ·J p2–p9

`01-matter-atoms-and-semiconductors.md`. Eight pages, almost all descriptive: **four** tagged
equations in the whole range.

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: bohr-transition]` | $hf = E_i - E_f$ | Energy, and so frequency, of the photon emitted when an electron drops to a lower orbit. The same $hf$ returns for the LED and the photodiode | ·J p5 | ⚠ JV1.2 (page says a *proton* is emitted) |
| `[eq: shell-electrons]` | $N = 2n^{2}$ | Electron capacity of shell $n$: 2, 8, 18, 32, 50 | ·J p5 | — |
| `[eq: subshell-electrons]` | $N_{\text{sub}} = 2 + 4(m-1)$ | Electron capacity of the $m$-th sub-shell: 2, 6, 10, 14 | ·J p5 | — |
| `[eq: charge-current-time]` | $Q = I\,t$ | Charge transported by a steady current $I$ in time $t$ | ·J p9 | ⚠ JV1.7 (charge defined in words as "an amount of current") |
| † band-gap classification | $E_g = 0\ \mathrm{eV}$ (conductor), $E_g = 1.1\ \mathrm{eV}$ (semiconductor), $E_g = 5\ \mathrm{eV}$ (insulator) | The one number that separates the three material classes. Everything about diodes and transistors starts here | ·J p7–p8 | ⚠ JV1.6 (the conductor band figure is drawn *with* a forbidden band) |

> The valence-electron counts that go with those gaps — 1–3 (conductor), 4 (semiconductor), 5–8
> (insulator) — are not equations but are examined as often as any formula on this sheet.

---

## A2 · Resistors and dc network theorems ·J p9–p24

`02-resistors-and-dc-network-theorems.md`. The densest equation file in tier 1, and the only
source in the whole knowledge base for the network theorems.

### A2.1 Charge, power and resistance

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: charge-current]` | $Q = It \iff I = \dfrac{Q}{t}$ | Charge and current are two views of the same thing | ·J p9–p10 | — |
| `[eq: power-vi]` | $P = VI$ | Power dissipated in a component | ·J p10 | JC2.2 (power called an *amount* of energy) |
| `[eq: resistivity]` | $R = \rho\,\dfrac{L}{A}$ | Resistance from geometry and material. $\rho$ in Ω m, $L$ in m, $A$ in m² | ·J p10 | JC2.5 (the page types $\propto$ as a Greek $\alpha$) |
| `[eq: ohms-law]` | $I = \dfrac{V}{R}$, $\;V = IR$, $\;R = \dfrac{V}{I}$ | The three rearrangements of Ohm's law | ·J p12 | — |
| `[eq: power-forms]` | $P = IV = I^{2}R = \dfrac{V^{2}}{R}$ | The three power forms — pick the one whose two quantities you already have | ·J p12 | — |

### A2.2 The colour code

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: colour-code-value]` | $R = \big(10 d_1 + d_2\big)\times 10^{\,m} \;\pm\; T\,\%$ | Resistance from a four-band code: two digits, a multiplier, a tolerance | ·J p11 | — |
| `[eq: tolerance-range]` | $R\left(1-\tfrac{T}{100}\right) \le R_{\text{actual}} \le R\left(1+\tfrac{T}{100}\right)$ | The band the manufacturer guarantees — e.g. $31\ \mathrm{M\Omega} \pm 10\,\%$ gives 27.9 to 34.1 MΩ | ·J p11 | — |

> A five-band resistor uses the **first three** bands as digits, the fourth as the multiplier and
> the fifth as the tolerance. ·J p11

### A2.3 Series, parallel and the two dividers

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: series-current]` | $I = I_{R1} = I_{R2} = I_{R3}$ | The same current flows in every series element | ·J p12 | — |
| `[eq: series-resistance]` | $R_t = R_1 + R_2 + R_3$ | Series total — always larger than the largest member | ·J p12 | — |
| `[eq: voltage-divider]` | $V_{Rk} = V_s\,\dfrac{R_k}{R_t}$ | Voltage across one series element. Its fraction carries **its own** resistance on top | **[added]** — used at ·J p18, never stated | — |
| `[eq: parallel-voltage]` | $V_s = V_{R1} = V_{R2} = V_{R3}$ | Every parallel branch sees the whole supply | ·J p13 | — |
| `[eq: parallel-resistance]` | $\dfrac{1}{R_t} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3}$ | Parallel total — always smaller than the smallest member | ·J p13 | — |
| `[eq: product-over-sum]` | $R_t = \dfrac{R_1R_2}{R_1+R_2}$ | The two-resistor special case, used constantly in §A2.5 | **[added]** — used at ·J p18–p21 | — |
| `[eq: current-divider]` | $I_{R3} = I_t\,\dfrac{R_2}{R_2+R_3}$ | Current into one of two parallel branches. Its fraction carries the **other** branch's resistance on top — the mirror image of the voltage divider | ·J p20 | — |
| `[eq: power-rating-series]` `[eq: power-rating-parallel]` | $n = \dfrac{P_{\text{total}}}{P_{\text{one}}}$; then series $R_{\text{each}} = \dfrac{R_t}{n}$, parallel $R_{\text{each}} = nR_t$ | Builds a high-wattage resistor out of $n$ identical low-wattage parts | ·J p15 | — |

### A2.4 Practical sources

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: source-droop]` | $V_{RL} = V_s\,\dfrac{R_L}{R_i + R_L}$ | Terminal voltage of a real source — it is just a divider between $R_i$ and $R_L$ | **[added]** — the general statement behind ·J p16–p17 | — |
| † constant-voltage source | $R_i \ll R_L$ | The condition that makes a source behave as a fixed emf | ·J p16 | — |
| † constant-current source | $R_i \gg R_L$ | The condition that makes a source behave as a fixed current | ·J p17 | — |
| † source transformation | $I_N = \dfrac{V_s}{R_i}$ | $V_s$ in **series** with $R_i$ is equivalent to $I_N$ in **parallel** with the same $R_i$ | ·J p17 | ⚠ JV2.7 (the printed sentence shorts the *source*, not the terminals) |
| `[eq: impedance-polar]` | $Z = R + jX = \sqrt{R^{2}+X^{2}}\ \angle\,\tan^{-1}\dfrac{X}{R}$ | The ac generalisation of resistance, in polar form | ·J p16 | ⚠ JV2.5 (printed as a quotient, giving modulus 1) |

### A2.5 Thevenin, Norton and mesh analysis

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: thevenin-resistance]` | $R_{Th} = R_3 + \dfrac{R_1R_2}{R_1+R_2}$ | Step 1: open the load, short the source, look in | ·J p18 | JC2.14 (the second equals sign drops to subscript level) |
| `[eq: thevenin-voltage]` | $V_{Th} = V_s\,\dfrac{R_2}{R_1+R_2}$ | Step 2: restore the source, leave the terminals open, read the voltage | ·J p18 | — |
| `[eq: thevenin-load-current]` | $I_{RL} = \dfrac{V_{Th}}{R_{Th}+R_L}$ | Step 3: reconnect the load to the series pair | ·J p19 | — |
| `[eq: norton-resistance]` | $R_N = R_{Th}$ | The one thing that carries straight over between the two theorems | ·J p19 | — |
| `[eq: norton-current]` | $I_N = \dfrac{V_sR_2}{R_1R_2 + R_1R_3 + R_2R_3}$ | Short-circuit current of the standard three-resistor network. The denominator is the sum of all three pairwise products — it cannot hide a slip | ·J p20 | JC2.16 (·J p20's top line is clipped) |
| `[eq: norton-load-current]` | $I_{RL} = \dfrac{I_NR_N}{R_N+R_L}$ | Step 3 for Norton — the current divider again, numerator $R_N$ | ·J p20 | — |
| `[eq: mesh-kvl]` | Sum of the $IR$ drops round each closed loop equals the emf in it — for ·J p22's network, $10I_1+20I_2 = 30$ and $30I_3+20I_2 = 50$ | The loop equations of a two-source network | ·J p22 | JC2.17 (called Kirchhoff's *current* law) |
| `[eq: mesh-kcl]` | $I_1 + I_3 = I_2$ | The node equation that closes the system | ·J p22 | JC2.18 ("eliminating $I_3$" leaves $I_3$ in both lines) |

> **Thevenin against Norton, in one line.** Thevenin **opens** the load and reads a **voltage**;
> Norton **shorts** the load and reads a **current**. Step 2 is identical in both.

---

## A3 · Capacitors, inductors and transformers ·J p24–p32

`03-capacitors-inductors-and-transformers.md`. Note that ·J p25, ·J p26 and ·J p30 are blank or
lost in the source, so several standard results here are `[added]`.

### A3.1 The capacitor

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: parallel-plate-capacitance]` | $C = \varepsilon_r\,\varepsilon_0\,\dfrac{A}{d}$ | Capacitance from geometry. Big plates, thin dielectric, high permittivity all push $C$ up | ·J p24 | ⚠ JV3.1 (permittivity said to act on the *magnetic* field); JC3.2 ($\Pi$ for $\pi$ in $\varepsilon_0$) |
| `[eq: charge-voltage]` | $Q = C\,V$ | The defining relation. The notes use it twice and never state it | **[added]** at ·J p26–p27 | — |
| `[eq: capacitors-series]` | $\dfrac{1}{C_t} = \dfrac{1}{C_1}+\dfrac{1}{C_2}+\dfrac{1}{C_3}$ | Series total — always **smaller than the smallest** member. Note it is the resistor rule inverted | ·J p26 | JC3.5 (a doubled equals sign in the charge line) |
| `[eq: capacitors-parallel]` | $C_t = C_1 + C_2 + C_3$ | Parallel total — always **larger than the largest** member | ·J p27 | JC3.4 (the parallel section has no heading) |
| `[eq: capacitor-energy]` | $E = \dfrac{CV^{2}}{2} = \dfrac{QV}{2} = \dfrac{Q^{2}}{2C}$ | Energy stored in the dielectric, three ways | ·J p27 | — |
| `[eq: capacitive-reactance]` | $X_c = \dfrac{1}{2\pi f C}\ \ [\Omega]$ | Opposition a capacitor offers to ac. It **falls** as frequency rises | ·J p27 | JC3.6 ($\Pi$ for $\pi$ again) |
| `[eq: rc-charging]` | $v_C(t) = V\left(1 - e^{-t/RC}\right)$, $\;i(t) = \dfrac{V}{R}e^{-t/RC}$, $\;\tau = RC$ | The charging transient | **[added]** — ·J p25 is blank | — |
| `[eq: rc-discharging]` | $v_C(t) = V_0\,e^{-t/RC}$, $\;i(t) = \dfrac{V_0}{R}e^{-t/RC}$ | The discharging transient | **[added]** — ·J p26 is a lost half-page | — |

### A3.2 The inductor — all `[added]`

The notes give **no inductance equations at all**. The three standard results are supplied so the
rest of the course has them.

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: self-inductance-emf]` | $e = -L\,\dfrac{\mathrm di}{\mathrm dt}$ | The self-induced emf; the minus sign is Lenz's law | **[added]** at ·J p29 | ⚠ JV3.3 (the printed *definition* describes mutual inductance) |
| † mutual inductance | $e_2 = -M\,\dfrac{\mathrm di_1}{\mathrm dt}$ | The emf induced in a second coil by a changing current in the first | **[added]** at ·J p29 | ⚠ JV3.4 (the page says changing *voltage*) |
| `[eq: inductor-energy]` | $E = \tfrac12 L I^{2}$ | Energy stored in the magnetic field — the mirror of $\tfrac12CV^2$ | **[added]** | — |
| `[eq: inductive-reactance]` | $X_L = 2\pi f L\ \ [\Omega]$ | Opposition an inductor offers to ac. It **rises** as frequency rises | **[added]** | — |

### A3.3 The transformer

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ideal-transformer-power]` | $P_p = P_s$ | The ideal transformer — no loss. In practice $P_p > P_s$ | ·J p31 | — |
| `[eq: transformer-efficiency]` | $\eta = \dfrac{P_s}{P_p}\times 100\ \ [\%]$ | Efficiency of a practical transformer | ·J p31 | JC3.12 (the loss list runs two items together) |
| `[eq: transformation-ratio]` | $n = \dfrac{V_p}{V_s} = \dfrac{N_p}{N_s} = \dfrac{I_s}{I_p}$ | The whole of transformer arithmetic. Voltage up means current down, in the same proportion | ·J p32 | ⚠ JV3.6, JV3.7 (digit slips in the worked example) |
| † lossy current ratio | $\dfrac{I_s}{I_p} = \eta\,\dfrac{N_p}{N_s}$ | The current relation once efficiency is included — the voltage relation is unaffected, because it comes from flux linkage, not power balance | ·J p32 (reconstructed) | ⚠ JV3.8 (the example gives two answers for $I_s$ and does not say which stands) |
| † phase | Like-marked (dotted) terminals give $V_p$ and $V_s$ **in phase**; opposite marking gives $180^\circ$ | The phase relation is set by the winding sense, not by the device | ·J p31 | ⚠ JV3.5 (the page states a flat $180^\circ$) |

---

## A4 · Diodes ·J p33–p45

`04-diodes.md`. Thirteen pages, roughly half circuit analysis with numbers.

### A4.1 The junction and the diode law

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: diode-turn-on-voltages]` | $V_o(\mathrm{Ge}) = 0.2\text{–}0.3\ \mathrm{V}$; $\;V_o(\mathrm{Si}) = 0.6\text{–}0.7\ \mathrm{V}$ | The forward voltage at which conduction begins, and the drop the models then assume | ·J p34, p38 | — ⇄ agrees with ·L1 p5 |
| `[eq: diode-static-equation-j]` | $i_D = I_o\left(e^{\,V_D/\eta V_T} - 1\right)$, with $V_T = \dfrac{kT}{q}$ | **The diode law.** $\eta = 1$ (Ge), $\eta = 2$ (Si) | ·J p35 | ⚠ JV4.3 (the exponent is printed as a *denominator*) |
| `[eq: thermal-voltage-j]` | $V_T = \dfrac{kT}{q} = \dfrac{1.38\times10^{-23}\times300}{1.6\times10^{-19}} = 25.9 \approx 26\ \mathrm{mV}$ at 300 K | Thermal voltage. The notes give no numerical value | ·J p35 | ⚠ JV4.2 ($k$ printed as $1.38\times10^{-28}$ — out by $10^{5}$) |
| † breakdown against PIV | $V_{BR}$ is the voltage at which breakdown physically occurs; PIV is the manufacturer's **rating**, specified below $V_{BR}$ with margin | Design to the PIV, not to the breakdown voltage | ·J p35 | ⚠ JV4.4 (the page treats them as synonyms) |

### A4.2 Thevenin reduction and the load line

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: thevenin-vth-diode]` | $V_{Th} = V_S\,\dfrac{R}{R_S + R}$ | Step 1 of the standard diode-circuit reduction | ·J p36 | ⚠ JV4.5 (printed with $R_L$ in the denominator) |
| `[eq: thevenin-rth-diode]` | $R_{Th} = \dfrac{R_S R}{R_S + R}$ | Step 2: kill the source and look in — $R_S$ parallel $R$ | ·J p36 | — |
| `[eq: diode-current-thevenin]` | $I_D = \dfrac{V_{Th}}{R_L + R_{Th}}$ | Step 3, ideal-diode model ($V_D = 0$). Carrying the drop gives $I_D = \dfrac{V_{Th}-V_D}{R_{Th}+R_L}$ | ·J p36 | — |
| `[eq: dc-load-line-intercepts]` | $V_D$-intercept $= V_{Th}$; $\;I_D$-intercept $= \dfrac{V_{Th}}{R_{Th} + R_L}$ | The two end points of the diode load line; the Q point is where it cuts the characteristic | ·J p36, p40 | ⚠ JV4.6 ($R_L$ missing from the current intercept) |

### A4.3 The two resistances

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: r-dc-static]` | $r_{dc} = \dfrac{V_{DQ}}{I_{DQ}}$ | Static resistance — the reciprocal slope of the **chord from the origin** to the Q point | ·J p36–p37 | — |
| `[eq: r-ac-dynamic]` | $r_{ac} = \dfrac{\Delta V_D}{\Delta i_D}$ | Dynamic resistance — the reciprocal slope of the **curve at** the Q point. Always the smaller of the two | ·J p38 | — |

### A4.4 Special diodes

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: photodiode-dark-current]` | $I_R = \dfrac{V_R}{R_R}$ | Dark current: the reverse current with no illumination, set by the dark resistance | ·J p43 | — |
| `[eq: varactor-plate-capacitance]` | $C = \dfrac{\varepsilon A}{d}$ | Junction capacitance from geometry. Read it with $V_R\uparrow \Rightarrow d\uparrow \Rightarrow C\downarrow$ | ·J p44 | — ⇄ same law as ·L1 p7's $C = K/\sqrt{V_R}$, in geometry form |
| `[eq: varactor-resonant-frequency]` | $f_r = \dfrac{1}{2\pi\sqrt{LC}}$ | Resonance of the tuned circuit the varactor controls — electronic tuning with no moving parts | ·J p45 | JC4.12 |

> The tunnel diode is covered descriptively at ·J p43–p44 and carries **no equation**; the negative
> resistance $R_N = -\mathrm dV/\mathrm dI$ is tier 2 only (·L2 p25, Part B §B2.7).

---

## A5 · Rectifiers, filters and regulation ·J p46–p56

`05-rectifiers-filters-and-regulation.md`. The most derivation-heavy range in tier 1: ·J p47–p49
is almost nothing but integration and algebra.

### A5.1 The half-wave rectifier

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: rectifier-idc-general-j]` | $I_{dc} = \dfrac{1}{2\pi}\displaystyle\int_{0}^{\pi} I_m\sin\theta\,\mathrm d\theta$ | The integral the average is derived from — the $2\pi$ below against the $\pi$ above is the whole story of the half-wave circuit | ·J p47 | JC5.1 |
| `[eq: hw-idc-j]` | $I_{dc} = \dfrac{I_m}{\pi} = 0.3183\,I_m$ | The dc (average) output | ·J p47 | — ⇄ agrees exactly with ·L2 p3 |
| `[eq: hw-irms-j]` | $I_{rms} = \dfrac{I_m}{2}$ | The rms output — **half** the peak, not $1/\sqrt2$ of it | ·J p47 | — ⇄ agrees exactly with ·L2 p3 |
| `[eq: rectifier-powers-j]` | $P_{dc} = I_{dc}V_{dc} = I_{dc}^{2}R_L$ | dc power delivered to the load | ·J p47, p49 | — ⇄ ·L2 p8 misprints this (V2.10); ·J is right |
| † ac power | $P_{ac} = I_{rms}^{2}\left(R_L + r_f\right)$ | ac power drawn from the source — the current flows through the diode as well as the load | ·J p47 | ⚠ JV5.2 (·J p49 substitutes the half-wave rms into the full-wave case) |
| `[eq: hw-efficiency-j]` | $\eta_{\text{HW}} = \dfrac{4}{\pi^{2}\left(1 + r_f/R_L\right)} = \dfrac{0.405}{1 + r_f/R_L}$; maximum $\dfrac{4}{\pi^{2}} = 40.5\,\%$ | Rectification efficiency | ·J p47 | ⚠ JV5.1 (exponent on the wrong bracket); JC5.2 |
| `[eq: irms-dc-ac-j]` | $I_{rms}^{2} = I_{dc}^{2} + I_{ac}^{2} \Longrightarrow I_{ac} = \sqrt{I_{rms}^{2} - I_{dc}^{2}}$ | Splits the output into its dc and ac parts — the step every ripple factor comes from | ·J p47–p48 | — ⇄ agrees with ·L2 p5 |
| `[eq: hw-ripple-j]` | $\gamma_{\text{HW}} = \dfrac{I_{ac}}{I_{dc}} = \sqrt{\dfrac{\pi^{2}}{4} - 1} = 1.21$ | Half-wave ripple — 21 % more ac than dc, hence the filter | ·J p48 | JC5.3 |

### A5.2 The full-wave rectifier

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: fw-idc-j]` | $I_{dc} = \dfrac{2I_m}{\pi} = 0.6366\,I_m$ | dc output — exactly twice the half-wave value | ·J p48–p49 | ⚠ ILLEGIBLE (·J p49 line 1 clipped) ⇄ agrees with ·L2 p8 |
| `[eq: fw-irms-j]` | $I_{rms} = \dfrac{I_m}{\sqrt2} = 0.707\,I_m$ | rms output — up by $\sqrt2$, not by 2 | ·J p49 | — ⇄ agrees exactly with ·L2 p8 |
| `[eq: fw-efficiency-j]` | $\eta_{\text{FW}} = \dfrac{8}{\pi^{2}\left(1 + r_f/R_L\right)} = \dfrac{0.811}{1 + r_f/R_L}$; maximum $\dfrac{8}{\pi^{2}} = 81.1\,\%$ | Efficiency — **exactly twice** the half-wave figure, which is the best single check on the section | ·J p49 | ⚠ JV5.3, JC5.2 |
| `[eq: fw-ripple-j]` | $\gamma_{\text{FW}} = \sqrt{\dfrac{\pi^{2}}{8} - 1} = 0.48$ | Full-wave ripple. Quote **0.483** if three figures are wanted | ·J p49 | — ⇄ ·L2 p9 prints 0.482 (C2.12) |
| † ripple frequency | $f$ (half-wave), $2f$ (full-wave) | Sets the filter design and identifies the circuit from a scope trace | ·J p46, p48, p50 | — |

> **PIV is absent from tier 1.** ·J mentions it once as a diode *rating* (·J p46, JC5.11) and never
> computes it for a circuit. Take PIV from Part B §B2 — and note that without it ·J p50 gives no
> reason to prefer the bridge over the centre-tap circuit.

### A5.3 The capacitor filter

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: capacitor-charge-j]` | $V_C = V_S\left(1 - e^{-t/r_f C}\right)$ | Charging, through the conducting diode and transformer — a **short** time constant | ·J p51 | ⚠ JV5.5 (page prints $RC$ for both) |
| `[eq: capacitor-discharge-j]` | $V_C = V_S\,e^{-t/R_L C}$ | Discharging, through the load — a **long** time constant. The asymmetry is what flattens the output | ·J p51 | ⚠ JV5.5 |

> **This is the knowledge base's only *primary* source for filters.** Part B §B2.6's smoothing
> formulas — $V_{r(pp)} = I_{L(dc)}/f_rC$ and $C = 1/2\sqrt3\,\gamma f_r R_L$ — are `[added]` there,
> in no source. The choke-input and Π filters (·J p52–p53) are descriptive and carry no equations.

### A5.4 The zener regulator — the two-state method

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: zener-off-divider-j]` | $V_{RL} = \dfrac{V_S R_L}{R + R_L}$, then test $V_{RL} > V_Z \Rightarrow$ **on state** | **Step 1 of every zener question:** replace the diode by an open circuit and see whether it would break down | ·J p54–p55 | — |
| `[eq: zener-on-currents-j]` | $I_{RL} = \dfrac{V_Z}{R_L}$; $\;I_t = \dfrac{V_S - V_Z}{R} = I_{RL} + I_Z$; $\;I_Z = I_t - I_{RL}$ | Step 2: the node is clamped at $V_Z$. The load current is fixed by $V_Z$, the total by $V_S$ and $R$ — **the zener absorbs the difference** | ·J p55 | — |
| `[eq: zener-power-j]` | $P_Z = I_Z V_Z$ | Check it against the diode's rating every time | ·J p55 | JC5.4 |
| † symmetric zener limiter | $v_{out} = \pm\left(V_Z + V_F\right)$ | Clip level of a back-to-back zener pair. The notes draw the flats at $\pm V_Z$, neglecting $V_F$ | ·J p56 | ⚠ JV5.6 (the lower circuit's second zener is drawn reversed), JV5.7 |

---

## A6 · Bipolar junction transistors ·J p57–p83

`06-bipolar-junction-transistors.md`. The largest file in tier 1 and the most heavily examined
range in the course.

### A6.1 Currents and the three gains

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: j-ie-ic-ib]` | $I_E = I_C + I_B$, in the ratio $100\,\% : 95\,\% : 5\,\%$ | The most-used relation in the topic — everything else follows from it | ·J p58, p60 | JC6.2 (collector share printed "95 % /98 %") ⇄ agrees with ·L3 p3 |
| `[eq: j-alpha]` | $\alpha = \dfrac{I_C}{I_E} = h_{FB}$, so $I_C = \alpha I_E$ and $I_B = (1-\alpha)I_E$ | Common-base dc current gain; always just under 1. It **measures the quality of the transistor** | ·J p60, p63 | — ⇄ **·J prints it correctly; ·L3 p4 prints it inverted (V3.1)** |
| `[eq: j-beta]` | $\beta = \dfrac{I_C}{I_B} = h_{FE}$ | Common-emitter dc current gain; tens to hundreds | ·J p62 | ⚠ ILLEGIBLE (·J p62 line 1) ⇄ agrees with ·L3 p5 |
| `[eq: j-theta]` | $\theta = \dfrac{I_E}{I_B} = \gamma = h_{FC} = 1+\beta$ | Common-collector current gain | ·J p62 | ⚠ JV6.5 (the chain opens with $I_E/I_C$) ⇄ agrees with ·L3 p6 |
| `[eq: j-alpha-beta]` | $\alpha = \dfrac{\beta}{\beta+1}$ and $\beta = \dfrac{\alpha}{1-\alpha}$ | Converts between the two gains — the cheapest marks in the topic | ·J p63 | — ⇄ agrees exactly with ·L3 p6 |
| † CB output admittance | $h_{OB} = \dfrac{I_C}{V_{CB}}\ [\mathrm S]$, so $R_{out} = \dfrac{1}{h_{OB}}$ | The CB output parameter, and its correct sense | ·J p60–p61 | ⚠ JV6.2 (page equates a *resistance* to $h_{OB}$) |
| † CE output admittance | $h_{OE} = \dfrac{I_C}{V_{CE}} = \dfrac{1}{r_o}$ | The CE output parameter | ·J p62 | — |
| † CC voltage gain | $A_v = \dfrac{V_{CE}}{V_{CB}} \cong 1$ | The emitter follower does not amplify voltage — that is the point of it | ·J p62 | — |
| `[eq: j-power-gain-db]` | $A_p = \dfrac{V_{CB}I_C}{V_{BE}I_E}$; $\;G_p = 10\log_{10}A_p$ dB; $\;G_v = 20\log_{10}A_v$ dB; $\;G_i = 20\log_{10}A_i$ dB | Power gain and the decibel forms. **10 for power, 20 for voltage or current** | ·J p61 | ⚠ JV6.3 (CE input power printed $I_EV_{BE}$; it is $I_BV_{BE}$) ⇄ agrees with ·L7 p15, p22 |

### A6.2 Leakage and thermal behaviour

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: j-ic-leakage-cb]` | $I_C = \alpha I_E + I_{CBO}$ | Collector current with leakage, common base | ·J p63 | — ⇄ agrees with ·L3 p7 |
| `[eq: j-ic-with-leakage]` | $I_C = \beta I_B + (1+\beta)\,I_{CBO}$ | The same thing in common emitter — the form every leakage example uses | ·J p63 | ⚠ JV6.6 (the middle step loses its $\alpha$) ⇄ agrees with ·L3 p16 |
| † base current with leakage | $I_B = (1-\alpha)\,I_E - I_{CBO}$ | The complement of the row above | ·J p63 | — |
| `[eq: j-iceo]` | $I_{CEO} = \dfrac{I_{CBO}}{1-\alpha} = (1+\beta)\,I_{CBO}$ | CE leakage is $(1+\beta)$ times the CB leakage — why CE is the thermally dangerous configuration | ·J p64 | — ⇄ **·J derives it on the page; ·L3's derivation pages are missing and the tier-2 row is `[added]`** |
| † leakage forms | $I_C = \beta I_B + I_{CEO}$; $\;I_E = (1+\beta)\,I_B + I_{CEO}$ | The compact pair once $I_{CEO}$ is in hand | ·J p64 | ⚠ JV6.7 (the last line double-counts $1/(1-\alpha)$) |
| † thermal doubling | Ge: $I_{CBO}$ doubles per 10 °C. Si: $I_{CBO}$ doubles per 6 °C | Thermal runaway, quantified | ·J p64 | ⚠ JV6.8 (the page swaps the two materials) |
| `[eq: j-cc-vce]` | $V_{CE} = V_{CB} + V_{BE}$ | Ties the three terminal voltages together; governs the whole CC input plot | ·J p69 | — |

### A6.3 The six bias circuits

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: j-base-bias]` | $V_{CC} = I_CR_C + V_{CE}$; $\;V_{CC} = I_BR_B + V_{BE}$; $\;I_C = \dfrac{V_{CC}-V_{CE}}{R_C}$; $\;I_B = \dfrac{V_{CC}-V_{BE}}{R_B}$; $\;I_{C(sat)} = \dfrac{V_{CC}}{R_C}$; $\;V_{CE(\max)} = V_{CC}$; $\;S = 1+\beta$ | The complete base-bias set. Worst stability of the six: $I_C = \beta I_B$ tracks $\beta$ exactly | ·J p70 | — ⇄ agrees with ·L3 p14, p17 |
| `[eq: j-emitter-feedback]` | $V_{CC} = I_CR_C + V_{CE} + I_ER_E$; $\;V_{CC} = I_BR_B + V_{BE} + I_ER_E$; $\;I_C = \dfrac{V_{CC}-V_{CE}}{R_C + R_E/\alpha}$; $\;I_B = \dfrac{V_{CC}-V_{BE}}{R_B + (1+\beta)R_E}$; $\;V_E = I_ER_E$, $V_B = V_{BE}+V_E$, $V_C = V_{CE}+V_E$ | Base bias with emitter feedback — and this is the **exact** $I_B$, where tier 2 gives the approximate $I_C$ | ·J p71 | — ⇄ equivalent to ·L3 p18 to within $1/\beta$ |
| `[eq: j-collector-feedback]` | $V_{CC} = (I_C+I_B)R_C + I_BR_B + V_{BE}$; $\;V_C = V_{CC} - (I_C+I_B)R_C = I_BR_B + V_{BE}$; and **[added]** $I_C \cong \dfrac{V_{CC}-V_{BE}}{R_C + R_B/\beta}$ | Base bias with collector feedback. The notes give the loops only; the solved form is supplied | ·J p72 | — ⇄ the solved form matches ·L3 p19 |
| `[eq: j-both-feedbacks]` | $V_{CC} = (I_C+I_B)R_C + V_{CE} + I_ER_E$; $\;V_{CC} = (I_C+I_B)R_C + I_BR_B + V_{BE} + I_ER_E$; node voltages $V_E = I_ER_E$, $V_C = V_{CE}+V_E$ | Both feedbacks together | ·J p72 | — |
| `[eq: j-ic-sat]` | $I_{C(sat)} = \dfrac{V_{CC}}{R_C+R_E}\cdot\dfrac{\beta}{1+\beta} \cong \dfrac{V_{CC}}{R_C+R_E}$; $\;V_{CE(\text{cut-off})} = V_{CC}$ | Saturation and cut-off with an emitter resistor present | ·J p72 | JC6.11 (an approximation printed as an exact equality) |
| `[eq: j-two-supply]` | $V_{EE} = I_ER_E + I_BR_B + V_{BE}$; $\;V_{CC}+V_{EE} = I_CR_C + V_{CE} + I_ER_E$; $\;V_{CC} = I_CR_C + V_{CB} - I_BR_B$; and **[added]** $I_E = \dfrac{V_{EE}-V_{BE}}{R_E + R_B/\beta} \cong \dfrac{V_{EE}}{R_E}$ | Emitter bias from two supplies — $\beta$ vanishes from the bias equation | ·J p73 | ⚠ JV6.9, JV6.10 (two of the three loops printed with sign errors) ⇄ the solved $I_E$ matches ·L3 p21 |
| `[eq: j-divider-thevenin]` | $V_{Th} = \dfrac{V_{CC}R_{B2}}{R_{B1}+R_{B2}}$; $\;R_{Th} = \dfrac{R_{B1}R_{B2}}{R_{B1}+R_{B2}}$; then $V_{CC} = I_CR_C+V_{CE}+I_ER_E$ and $V_{BB} = I_BR_B+V_{BE}+I_ER_E$; and **[added]** $I_B = \dfrac{V_{BB}-V_{BE}}{R_B+(1+\beta)R_E}$, $\;I_E = \dfrac{V_{BB}-V_{BE}}{R_E+R_B/(1+\beta)}$ | Voltage-divider bias by the Thevenin route — the only method ·J gives | ·J p73–p74 | ⚠ JV6.11 (the collector-to-base line has two reversed signs) ⇄ agrees exactly with ·L3 p22 |
| † divider base condition | $V_2 = V_{BE} + I_ER_E$ | The dc condition at the base of the CE amplifier | ·J p75 | ⚠ JV6.12 (the page assigns a junction to each divider resistor) |

> **·J gives the Thevenin route only.** Method 1 (by inspection) and Method 3 (the $\beta$-rule),
> and the $\beta$-sensitivity $K_\beta$, are **tier 2 only** — Part B §B3.6, §B3.7.

### A6.4 Load lines, the Q point and signal swing

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: j-dc-load-line]` | slope $m = \dfrac{-1}{R_C+R_E}$, intercept $c = \dfrac{V_{CC}}{R_C+R_E}$; end points $V_{CE(\text{cut-off})} = V_{CC}$ and $I_{C(sat)} = \dfrac{V_{CC}}{R_C+R_E}$ | The dc load line, read straight off $y = mx+c$ | ·J p76 | — ⇄ agrees with ·L3 p24 |
| `[eq: j-q-point]` | $I_{CQ} = \tfrac12 I_{C(sat)}$; $\;V_{CEQ} = \tfrac12 V_{CC}$ | Mid-point bias, for the largest possible undistorted swing | ·J p77 | — |
| `[eq: j-vpp]` | $V_{pp} = 2V_{CEQ}$; on the current side the limit is $2I_{CQ}$ | Peak-to-peak swing before clipping. Saturation clipping when $I_{C(sat)}-I_{CQ} < I_{CQ}$; cut-off clipping otherwise | ·J p78 | — |
| `[eq: j-rac]` | $R_{ac} = \dfrac{R_C R_L}{R_C+R_L}$, and $R_{ac} < R_{dc}$ always | The ac load — $R_C$ and $R_L$ in parallel once the coupling capacitor is a short | ·J p79 | — |
| `[eq: j-ac-load-line]` | $I_{C(sat)}\big|_{ac} = I_{CQ} + \dfrac{V_{CEQ}}{R_{ac}}$; $\;V_{CE(\text{cut-off})}\big|_{ac} = V_{CEQ} + I_{CQ}R_{ac}$ | The ac load line — same Q point, steeper slope | ·J p79–p80 | — ⇄ agrees exactly with ·L3 p25 |
| † maximum swing | $V_{pp(\max)} = \min\!\left(2I_{CQ}R_{ac},\ 2V_{CEQ}\right)$ | Largest undistorted output: the shorter arm of the ac load line clips first | ·J p80 | — ⇄ ·L3 p25 states the same thing as a **peak**, i.e. halved |

### A6.5 Stability

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: j-stability-factor]` | $S = \dfrac{\mathrm dI_C}{\mathrm dI_{CBO}}$ at constant $I_B$, $\beta$; $\;S = \dfrac{1+\beta}{1 - \beta\,\mathrm dI_B/\mathrm dI_C}$; circuit form $S = \dfrac{1 + R_B/R_E}{1 + R_B/(1+\beta)R_E}$; equivalently $S = (1+\beta)\dfrac{1 + R_B/R_E}{1 + \beta + R_B/R_E}$ | How far the Q point moves when leakage moves. $R_B$ is the total resistance on the **base** side, $R_E$ on the **emitter** side. Larger $S$ means worse stability | ·J p81, p83 | — ⇄ **agrees exactly with ·L3 p16–p17**; all three expressions are algebraically identical |

> **$\beta$ or $1+\beta$ in the $S$ denominator? $1+\beta$.** Tier 1 prints $(1+\beta)$ on both
> ·J p81 and ·J p83, and tier 2's general form $S = \dfrac{1+R_B/R_E}{1+(1-\alpha)R_B/R_E}$ gives
> the same thing, since $1-\alpha = 1/(1+\beta)$. Two independent sources, one answer — this is the
> clearest case on the sheet of the concordance settling a question that tier 2 alone left open.

---

## A7 · Field-effect transistors ·J p84–p100

`07-field-effect-transistors.md`. Note what is **not** here: no $g_m$, no $r_d$, no $\mu$, no gain
expression that yields a number, and no FET load line. All of that is tier 2 only.

### A7.1 The device equations

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: jfet-channel-ohm-j]` | $I_D = \dfrac{V_{DS}}{R_{DS}}$ | The channel below pinch-off, behaving as a plain resistor | ·J p85 | — |
| `[eq: shockley-j]` | $I_D = I_{DSS}\left(1 - \dfrac{V_{GS}}{V_{GS(\text{off})}}\right)^{2}$, with $V_{GS(\text{off})} < 0$ for an N-channel JFET | **Shockley's equation** — drain current in the pinch-off region. The square is why the JFET is a square-law device | ·J p87 | ⚠ JV7.1 ($V_P$ and $V_{GS(\text{off})}$ used interchangeably) ⇄ **agrees with ·L4 p6 including in the defect** |
| † pinch-off and cut-off | $\lvert V_P\rvert = \lvert V_{GS(\text{off})}\rvert$, and $V_{GS(\text{off})} = -\lvert V_P\rvert$ for N-channel | Same magnitude, opposite sign, different axes: $V_P$ lives on the $V_{DS}$ axis, $V_{GS(\text{off})}$ on the $V_{GS}$ axis | ·J p85–p87 | ⚠ JV7.1 ⇄ same defect flagged V4.2 in tier 2 |
| `[eq: emosfet-square-law-j]` | $I_D = K\left(V_{GS} - V_{GS(\text{th})}\right)^{2}$, valid only for $V_{GS} > V_{GS(\text{th})}$ | The enhancement-MOSFET square law. Below threshold $I_D = 0$ | ·J p91, p92 | — ⇄ agrees exactly with ·L4 p19 |
| `[eq: emosfet-k-from-idon-j]` | $K = \dfrac{I_{D(\mathrm{ON})}}{\left(V_{GS(\mathrm{ON})} - V_{GS(\text{th})}\right)^{2}}$ | Gets $K$ off a data sheet from the one quoted ON point | ·J p97 | — ⇄ agrees with ·L4 p19; ·J's subscripts are the better-labelled pair |
| † square-law ratio shortcut | $\dfrac{I_{D2}}{I_{D1}} = \left(\dfrac{V_{GS2}-V_{GS(\text{th})}}{V_{GS1}-V_{GS(\text{th})}}\right)^{2}$ | Two operating points without ever computing $K$ | **[added]** | — |

### A7.2 The bias circuits — one loop equation, four gate equations

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: fet-supply-loop-j]` | $V_{DD} = I_DR_D + V_{DS} + I_SR_S$ | The **drain loop, common to every FET stage**. With it, $V_D = V_{DD}-I_DR_D$, $V_S = I_SR_S$, $V_{DS} = V_D - V_S$ | ·J p93 | — ⇄ agrees with ·L4 p9 |
| `[eq: gate-bias-j]` | $V_{GS} = -V_{GG} - I_SR_S$ ($V_{GG}$ the **magnitude** of the negative rail) | Separate-supply (gate) bias, for the circuit ·J p93 actually draws — a $-V_{GG}$ rail **and** a source resistor | ·J p93 | ⚠ JV7.7 (printed $V_{GG} = V_{GS}+I_SR_S$, which makes $V_{GS}$ positive) — **see the concordance: ·L4's gate-bias circuit is a different circuit** |
| `[eq: self-bias-j]` | $V_{GS} = -I_SR_S$ | Self-bias: the drain current makes its own negative gate bias. The equation to have automatic | ·J p93 | — ⇄ agrees exactly with ·L4 p9 |
| `[eq: source-bias-j]` | $V_{GS} = V_{SS} - I_SR_S$ ($V_{SS}$ the **magnitude** of the negative rail) | Source bias — the most stable scheme: make $V_{SS} \gg \lvert V_{GS}\rvert$ and $I_S \approx V_{SS}/R_S$ | ·J p94 | — ⇄ agrees exactly with ·L4 p9 |
| `[eq: divider-bias-j]` | $V_{R_2} = \dfrac{V_{DD}R_2}{R_1+R_2}$, then $V_{GS} = V_{R_2} - I_DR_S$ | Voltage-divider bias. The divider sets a **positive** gate node; the negative $V_{GS}$ comes from making $I_DR_S$ larger than $V_{R_2}$ | ·J p94 | — ⇄ agrees exactly with ·L4 p9 |
| `[eq: drain-feedback-bias-j]` | $V_{GS} = V_{DS} = V_{DD} - I_DR_D$ | Drain-feedback bias of an E-MOSFET. Guarantees saturation, so the stage cannot be biased into the ohmic region | ·J p96 | ⚠ JV7.4 (page prints $V_{GS} = -V_{DS}$, which cuts the device off) |
| † drain-loop with both resistors | $V_{DS} = V_{DD} - I_D\left(R_D + R_S\right)$ | The form the E-MOSFET worked example actually performs | ·J p97 | ⚠ JV7.6 (page prints $V_{DD}-I_SR_S$ for a circuit with $R_S = 0$) |
| † E-MOSFET saturation check | $V_{DS} \ge V_{GS} - V_{GS(\text{th})}$ | Confirms the device is in saturation, where the square law is valid | **[added]** | ⚠ JV7.8 |

### A7.3 The three configurations

·J gives gains only as **ratios of terminal quantities** — definitions, not expressions. Nothing
in tier 1 lets you compute a number; for that, go to Part B §B4.4.

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: cs-gains-j]` | $A_i = \dfrac{I_D}{I_G}$, $\;A_v = \dfrac{V_{DS}}{V_{GS}}$ | Common source. $I_G \approx 0$, so $A_i$ and the input impedance $V_{GS}/I_G$ are both enormous. **The stage inverts**, though ·J's unsigned ratio does not say so | ·J p98–p99 | — |
| `[eq: cd-gains-j]` | $A_i = \dfrac{I_S}{I_G}$, $\;A_v = \dfrac{V_{SD}}{V_{GD}} \approx 1$ | Common drain — the source follower, a buffer | ·J p99 | ⚠ JC7.5 (·J prints $V_{DG}$, $V_{DS}$: the subscript order is reversed throughout the table) |
| `[eq: cg-gains-j]` | $A_i = \dfrac{I_D}{I_S} \approx 1$, $\;A_v = \dfrac{V_{DG}}{V_{GS}}$ | Common gate — low input impedance, non-inverting, the high-frequency configuration. $A_i \approx 1$ exactly as a BJT common base has $A_i = \alpha \approx 1$ | ·J p99–p100 | — |

---

# Part B — tier 2, the lesson documents ·L1–·L7

Seven lesson handouts, 1–27 pp. each, cited **·L{n} p{page}**. The 193 rows below are unchanged
from the previous edition of this sheet apart from their section numbering (now `B1`…`B7`) and
the file names they point to. Tier 2 is the **only** source for $h$-parameters, feedback,
frequency response, IC fabrication, PIV, TUF, the Fourier content of a rectified wave, and the
small-signal FET parameters $g_m$, $r_d$ and $\mu$ — none of which appear in tier 1 at all.

---

## B1 · Semiconductor diodes ·L1

### B1.1 The junction and the diode law

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: barrier-voltage]` | $V_B = V_T\ln\!\left(\dfrac{N_aN_d}{n_i^{2}}\right)$ | Barrier (junction) potential from the two doping densities | ·L1 p3 | — |
| `[eq: barrier-voltage]` (working form) | $V_B = 26\ln\!\left(\dfrac{N_aN_d}{n_i^{2}}\right)\ \mathrm{mV}$ at 300 K | The form the handout's own examples substitute into | ·L1 p3 | — |
| `[eq: thermal-voltage]` | $V_T = \dfrac{kT}{e} = \dfrac{T}{11{,}600}$ | Thermal voltage: 26 mV at 300 K, 25 mV at 293 K | ·L1 p3, p6 | — |
| `[eq: barrier-temp-coeff]` | $\Delta V_B = -0.002\,\Delta t$ | Barrier falls about 2 mV per °C, for both Ge and Si | ·L1 p3 | — |
| `[eq: diode-equation]` | $I = I_0\left(e^{\,V/\eta V_T}-1\right)$ | **The diode law.** Current from applied voltage, either polarity | ·L1 p6 | ⚠ V1.2 |
| `[eq: diode-eta]` | $\eta = 1$ (Ge) $\Rightarrow I = I_0(e^{\,eV/kT}-1)$; $\eta = 2$ (Si) $\Rightarrow I = I_0(e^{\,eV/2kT}-1)$ | Picks the ideality factor for the material in the question | ·L1 p6 | — |
| `[eq: diode-40-20]` | $I = I_0\left(e^{\,V_f/\eta V_T}-1\right)$ forward; $I = I_0\left(e^{\,V_R/\eta V_T}-1\right)$ reverse. With $V_T = 25$ mV the exponent coefficient is $40\ \mathrm{V^{-1}}$ (Ge), $20\ \mathrm{V^{-1}}$ (Si) | The shorthand the examples use | ·L1 p7 | ⚠ V1.3 |
| `[eq: diode-current-ratio]` | $V_2-V_1 = \dfrac{kT}{e}\ln\!\left(\dfrac{I_2}{I_1}\right) = 25\ln\!\left(\dfrac{I_2}{I_1}\right)\ \mathrm{mV}$ | Voltage change needed for a given current change; doubling costs 17.3 mV at $\eta = 1$ | ·L1 p8 | — |
| `[eq: diode-voltage-from-current]` | $V = \dfrac{kT}{e}\ln\!\left(\dfrac{I}{I_0}+1\right)$ | Diode voltage when the current and $I_0$ are known | ·L1 p8 | — |
| `[eq: io-temperature]` | $I_0' = 2^{5}I_0 = 32\,I_0$ for a 50 °C rise — $I_0$ doubles every 10 °C | How leakage scales with temperature | ·L1 p18 | — |

### B1.2 Diode parameters

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: bulk-resistance]` | $r_B = r_P + r_N = \dfrac{V_F - V_B}{I_F}$ | Ohmic resistance of the P and N material, well above the knee | ·L1 p7 | — |
| `[eq: junction-resistance]` | $r_j = \dfrac{25\ \mathrm{mV}}{I_F(\mathrm{mA})}$ (Ge); $r_j = \dfrac{50\ \mathrm{mV}}{I_F(\mathrm{mA})}$ (Si) | Dynamic junction resistance; both are $r_j = \eta V_T/I_F$ | ·L1 p7 | — |
| `[eq: ac-resistance]` | $r_{ac} = r_d = r_B + r_j$ | Total small-signal resistance; $\approx r_j$ at low current, $\approx r_B$ at high | ·L1 p7 | — |
| `[eq: forward-drop]` | $\text{forward voltage drop} = \dfrac{\text{power dissipated}}{\text{forward dc current}}$ | Forward drop from a quoted dissipation | ·L1 p7 | — |
| `[eq: reverse-dc-resistance]` | $R_R = \dfrac{\text{reverse voltage}}{\text{reverse current}}$ | Static reverse resistance — very large | ·L1 p7 | — |
| `[eq: varactor-capacitance]` | $C = \dfrac{K}{\sqrt{V_R}}$ | Voltage-controlled junction capacitance; more reverse bias means less capacitance | ·L1 p7 | — |

### B1.3 Zener diode and the shunt regulator

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: zener-node]` | $I = I_z + I_L$; $V_{out} = V_z$; $V_{in} = IR + V_z$ | The three equations every Zener regulator question starts from | ·L1 p11 | — |
| `[eq: zener-series-r]` | $R = \dfrac{V_{in}-V_{out}}{I_z + I_L}$ | Series dropping resistor for a stated diode and load current | ·L1 p11 | — |
| `[eq: zener-series-r-max]` | $R = \dfrac{V_{in}-V_{out}}{I_{Z\max}}$ when $I_L = 0$ | The design case — no load, diode carrying everything | ·L1 p11 | — |
| `[eq: zener-power]` | $P_{\max} = V_z I_{z(\max)}$ | Converts a wattage rating into a current limit | ·L1 p12 | — |

### B1.4 Load line — supplied here

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| † dc load line | $I = \dfrac{V_S - V_D}{R} = -\dfrac{1}{R}V_D + \dfrac{V_S}{R}$; intercepts $I = V_S/R$ and $V_D = V_S$ | Q-point of a diode in a resistive circuit | **[added]** — not in L1 | — |

> The handout contains **no load-line article and no tunnel-diode article**, though both are named
> in its own p1 outline. The load line above is `[added]`; no tunnel-diode treatment is supplied
> here for L1 (L2 §2.16 covers the device).

---

## B2 · Rectifiers, filters and wave-shaping ·L2

### B2.1 Half-wave rectifier

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: hw-peak-current]` | $I_{LM} = \dfrac{V_{sm}-V_B}{(R_S+r_d)+R_L} = \dfrac{V_{sm}-V_B}{R_0+R_L}$, with $R_0 \equiv R_S+r_d$; $V_{LM} = I_{LM}R_L$ | Peak load current and voltage — the starting point of every half-wave calculation | ·L2 p3 | C2.2 ($V_B$ left undefined on the page) |
| `[eq: hw-vdc]` | $V_{L(dc)} = \dfrac{V_{LM}}{\pi} = 0.318\,V_{LM}$; $I_{L(dc)} = \dfrac{I_{LM}}{\pi}$ | The dc (average) output | ·L2 p3 | — |
| `[eq: hw-vrms]` | $V_L = \dfrac{V_{LM}}{2} = 0.5\,V_{LM}$; $I_L = \dfrac{I_{LM}}{2}$ | The rms output — **half** the peak, not $1/\sqrt2$ of it | ·L2 p3 | ⚠ C2.3 |
| `[eq: hw-efficiency]` | $\eta_{\text{HW}} = \dfrac{4}{\pi^{2}}\cdot\dfrac{1}{1+R_0/R_L} = \dfrac{40.5\,\%}{1+R_0/R_L}$ | Rectification efficiency; maximum $4/\pi^2 = 40.5\,\%$ | ·L2 p4 | ⚠ V2.2, C2.4 (page quotes 40.6 %) |
| `[eq: hw-fourier]` | $i_L = I_{LM}\left(\dfrac{1}{\pi}+\dfrac{1}{2}\sin\omega t-\dfrac{2}{3\pi}\cos2\omega t-\dfrac{2}{15\pi}\cos4\omega t+\cdots\right)$ | The harmonic content: dc, a fundamental at $f$, then even harmonics | ·L2 p4 | ⚠ V2.3, V2.4 (harmonic rms values) |
| `[eq: hw-piv]` | $\mathrm{PIV}_{\text{HW}} = V_{sm}$ | Reverse rating the single diode must survive | ·L2 p5 | — |
| `[eq: hw-tuf]` | $\mathrm{TUF}_{\text{HW}} = \dfrac{2\sqrt2}{\pi^{2}} = 0.287$ | How badly the circuit uses its transformer (about 0.2 in practice) | ·L2 p6 | ⚠ V2.7 |

### B2.2 Ripple and form factor — general

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ripple-factor]` | $\gamma = \dfrac{I_{L(ac)}}{I_{L(dc)}} = \dfrac{\sqrt{I_L^{2}-I_{L(dc)}^{2}}}{I_{L(dc)}} = \sqrt{\left(\dfrac{I_L}{I_{L(dc)}}\right)^{2}-1}$ | How much ac survives in the output; smaller is better | ·L2 p5 | ⚠ V2.5, V2.6 |
| `[eq: form-factor]` | $K_f = \dfrac{I_L}{I_{L(dc)}} = \dfrac{V_L}{V_{L(dc)}}$ | rms divided by average | ·L2 p5 | — |
| `[eq: ripple-from-form-factor]` | $\gamma = \sqrt{K_f^{2}-1}$ | The quick route to $\gamma$ once $K_f$ is known | ·L2 p5 | — |
| `[eq: hw-ripple]` | $\gamma_{\text{HW}} = \sqrt{\dfrac{\pi^{2}}{4}-1} = 1.211$ | Half-wave ripple — more ac than dc, hence the filter | ·L2 p5 | — |

### B2.3 Full-wave centre-tapped rectifier

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: fw-vdc]` | $V_{L(dc)} = \dfrac{2V_{LM}}{\pi} = 0.636\,V_{LM}$; $I_{L(dc)} = \dfrac{2I_{LM}}{\pi}$ | dc output — exactly twice the half-wave value | ·L2 p8 | ⚠ C2.10 |
| `[eq: fw-vrms]` | $V_L = \dfrac{V_{LM}}{\sqrt2} = 0.707\,V_{LM}$; $I_L = \dfrac{I_{LM}}{\sqrt2}$ | rms output — up by $\sqrt2$, not by 2 | ·L2 p8 | — |
| `[eq: fw-efficiency]` | $\eta_{\text{FW}} = \dfrac{8}{\pi^{2}}\cdot\dfrac{R_L}{R_0+R_L} = \dfrac{81.1\,\%}{1+R_0/R_L}$ | Efficiency; maximum $8/\pi^2 = 81.1\,\%$, exactly twice half-wave | ·L2 p8 | ⚠ V2.10, C2.4 (page quotes 81.2 %) |
| `[eq: fw-fourier]` | $V_L = V_{LM}\left(\dfrac{2}{\pi}-\dfrac{4}{3\pi}\cos2\omega t-\dfrac{4}{15\pi}\cos4\omega t-\dfrac{4}{35\pi}\cos6\omega t-\cdots\right)$ | No fundamental and no odd harmonic — lowest ripple component at $2f$ | ·L2 p9 | ⚠ V2.11 |
| `[eq: fw-ripple]` | $\gamma_{\text{FW}} = \sqrt{\dfrac{\pi^{2}}{8}-1} = 0.483$ | Full-wave ripple, from $K_f = \pi/2\sqrt2 = 1.111$ | ·L2 p9 | ⚠ C2.12 |
| `[eq: fw-piv]` | $\mathrm{PIV}_{\text{centre-tap}} = 2V_{sm}$ | The centre-tap circuit's chief drawback | ·L2 p9 | — |
| `[eq: fw-tuf]` | $\mathrm{TUF}_{\text{centre-tap}} = 0.693$ | Transformer utilisation — better than half-wave, still not 1 | ·L2 p9 | — |
| `[eq: voltage-regulation]` | $V_R = \dfrac{V_{NL}-V_{FL}}{V_{FL}} = \dfrac{R_0}{R_L}$ | Stiffness of the supply; a perfect supply has $V_R = 0$ | ·L2 p10 | — |

### B2.4 Bridge rectifier

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: bridge-peak-current]` | $I_{LM} = \dfrac{V_{sm}-2V_B}{(R_S+2r_d)+R_L} = \dfrac{V_{sm}-2V_B}{R_0+R_L}$, here $R_0 \equiv R_S+2r_d$ | Peak current with **two** diodes always in series | ·L2 p12 | — |
| `[eq: bridge-efficiency]` | $\%\eta = \dfrac{81.2\,\%}{1+2r_d/R_L}$ | Efficiency with the doubled diode resistance | ·L2 p11–p12 | C2.4 (81.1 % exactly) |
| `[eq: bridge-piv]` | $\mathrm{PIV}_{\text{bridge}} = V_{sm}$ | Half the centre-tap requirement — the bridge's main advantage | ·L2 p11–p12 | — |

Average and rms values and the ripple factor are the same as the centre-tap circuit.

**TUF is not.** ⚠ `[added]` L2 gives no TUF for the bridge — the handout's bridge section runs
(b) average and rms → (c) efficiency → (d) ripple factor → (e) PIV → (f) advantages, with no TUF
item anywhere. It is **not** the centre-tap's 0.693:

$$\boxed{\;\mathrm{TUF}_{\text{bridge}} = \frac{8}{\pi^{2}} = 0.811\;}$$

The bridge secondary carries current on **both** half-cycles, so its VA rating is
$(V_{sm}/\sqrt2)(I_{LM}/\sqrt2) = V_{sm}I_{LM}/2$ against $P_{dc} = 4V_{sm}I_{LM}/\pi^{2}$. The
centre-tap's 0.693 is the *average* of a 0.573 secondary figure — each half-winding conducts only on
alternate half-cycles — and a 0.811 primary figure. Removing that penalty is exactly what L2 §2.8(f)
means when it says the bridge "uses the secondary continuously" and needs "a much smaller
transformer".

### B2.5 Three-phase

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: three-phase-hw-vdc]` | $V_{L(dc)} = \dfrac{3\sqrt3}{2\pi}V_{sm} = 0.83\,V_{sm} = 1.17\,V_s$ | Mean output of the three-phase half-wave rectifier | ·L2 p13 | C2.17 ($\eta$ and $\gamma$ figures) |

Efficiency $\approx 96.8\,\%$ and $\gamma \approx 0.18$; ripple frequency $3f$ (half-wave) or $6f$
(full-wave). The output never falls to zero — it swings between $V_{sm}$ and $0.5V_{sm}$.

### B2.6 Smoothing — supplied here

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ripple-voltage-shunt-c]` | $V_{r(pp)} = \dfrac{I_{L(dc)}}{f_r C}$, with $f_r = f$ (half-wave) or $2f$ (full-wave) | Peak-to-peak ripple across a capacitor-input filter | **[added]** §2.12 | — |
| `[eq: ripple-factor-shunt-c]` | $\gamma = \dfrac{V_{r(rms)}}{V_{L(dc)}} = \dfrac{1}{2\sqrt3\,f_r C R_L}$ | Ripple factor of the smoothed supply | **[added]** §2.12 | — |
| `[eq: smoothing-capacitor]` | $C = \dfrac{1}{2\sqrt3\,\gamma\,f_r R_L}$ | Sizes the reservoir capacitor for a target ripple | **[added]** §2.12 | — |

> The handout's own p1 outline promises smoothing; the 26 pages never deliver a filter section.
> The three results above are standard and carry **no ·L2 citation** because they are not in the
> source.

### B2.7 Clippers, clampers and multipliers

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| † parallel-clipper rule | $V_o = V_{\text{clip}}$ while the diode branch is forward-biased, $V_o = v_{in}$ otherwise | The single rule that generates all four biased-clipper waveforms | **[added]** ·L2 p18 | — |
| `[eq: clamper-time-constant]` | $\lambda = CR \gg \dfrac{T}{2}$; in practice $CR \ge 10T$ | Condition for the capacitor to hold its charge over a period | ·L2 p18–p19 | — |
| `[eq: doubler-output]` | $V_{C2} = 2V_m$ | Output of the half-wave (cascade) voltage doubler | ·L2 p21–p22 | — |
| † full-wave doubler | $V_L = 2V_m$ | Output of the full-wave doubler, capacitors series-aiding | ·L2 p22 | — |
| `[eq: multiplier-piv]` | $\mathrm{PIV}_{\text{multiplier}} = 2V_m$ | Diode rating for every multiplier in §2.15 | ·L2 p21–p22 | — |
| `[eq: tunnel-negative-resistance]` | $R_N = -\dfrac{dV}{dI}$, typically $-10$ to $-200\ \Omega$ | Negative resistance of the tunnel diode in its NDR region | ·L2 p25 | ⚠ C2.25 ($I_P$ must be read in mA) |

For a clamper the **voltage swing of input and output is the same** — a clamper shifts a waveform,
a clipper reshapes it.

---

## B3 · The bipolar junction transistor ·L3

### B3.1 Currents, $\alpha$ and $\beta$

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ie-ib-ic]` | $I_E = I_B + I_C$ | The most-used relation in the topic — everything else follows from it | ·L3 p3 | — |
| `[eq: alpha-dc]` | $\alpha = \dfrac{I_C}{I_E}$, so $I_C = \alpha I_E$ | Common-base dc current gain; always just under 1 | ·L3 p4–p5 | ⚠ V3.1 (printed inverted) |
| `[eq: beta-dc]` | $\beta = \dfrac{I_C}{I_B}$, so $I_C = \beta I_B$ | Common-emitter dc current gain $h_{FE}$; up to about 500 | ·L3 p5 | — |
| `[eq: alpha-beta]` | $\beta = \dfrac{\alpha}{1-\alpha}$ and $\alpha = \dfrac{\beta}{1+\beta}$ | Converts between the two gains — the cheapest marks in the topic | ·L3 p6 | — |
| `[eq: cc-current-gain]` | $\dfrac{I_E}{I_B} = 1+\beta$ | Common-collector current gain | ·L3 p6 | — |
| `[eq: current-relations]` | $I_C = \beta I_B = \alpha I_E = \dfrac{\beta}{1+\beta}I_E$; $\;I_B = \dfrac{I_C}{\beta} = \dfrac{I_E}{1+\beta} = (1-\alpha)I_E$; $\;I_E = \dfrac{I_C}{\alpha} = \dfrac{1+\beta}{\beta}I_C = (1+\beta)I_B = \dfrac{I_B}{1-\alpha}$ | Any one current from any other — the §57.11 table | ·L3 p6 | — |
| `[eq: current-ratio]` | $I_E : I_B : I_C \;::\; 1 : (1-\alpha) : \alpha$ | The three dc currents always stand in this ratio | ·L3 p6 | — |

### B3.2 Leakage

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: icbo-iceo]` | $I_{CEO} = (1+\beta)\,I_{CBO} = \dfrac{I_{CBO}}{1-\alpha}$ | CE leakage is $(1+\beta)$ times the CB leakage — why CE is the thermally dangerous configuration | **[added]** at ·L3 p7 (printed pages missing); printed at ·L3 p11 as $I_{CEO} = (1+\beta)I_{CO}$ | — |
| `[eq: ic-with-leakage]` | $I_C = \alpha I_E + I_{CBO}$ (common-base) | Collector current with leakage, CB | **[added]** at ·L3 p7 | — |
| `[eq: ic-with-leakage]` | $I_C = \beta I_B + (1+\beta)\,I_{CBO}$ (common-emitter) | Collector current with leakage, CE — the form Examples 57.4–57.7 all use | ·L3 p16 (printed); reconstructed at ·L3 p7 | — |

The notes write $I_{CO}$ for $I_{CBO}$ throughout the examples; treat the two as one symbol.

### B3.3 Static characteristics — resistances read off the curves

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: cb-rin]` | $R_{in} = \dfrac{\Delta V_{BE}}{\Delta I_E}$ at constant $V_{CB}$ | CB input resistance — about 50 Ω on the linear part | ·L3 p8 | C3.2 ($\Delta$ does not render) |
| `[eq: cb-rout]` | $R_{out} = \dfrac{\Delta V_{CB}}{\Delta I_C}$ | CB output resistance — typically 500 kΩ | ·L3 p8 | — |
| `[eq: ce-rin]` | $R_{in} = \dfrac{\Delta V_{BE}}{\Delta I_B}$ | CE input resistance — 4 kΩ near the origin, 600 Ω on the linear part | ·L3 p10 | — |
| `[eq: beta-ac-graph]` | $\beta_{ac} = \dfrac{\Delta I_C}{\Delta I_B}$ at a stated $I_B$ and $V_{CE}$ | Reads ac beta off the CE output family | ·L3 p10–p11 | — |
| `[eq: ce-rout]` | $R_{out} = \dfrac{\Delta V_{CE}}{\Delta I_C}$ | CE output resistance — 10 kΩ to 50 kΩ, far below the CB figure | ·L3 p11 | — |

### B3.4 Single-configuration dc analysis

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: cb-emitter-current]` | $I_E = \dfrac{V_{EE}-V_{BE}}{R_E}$, with $V_{BE} = 0.3$ V (Ge) or 0.7 V (Si) | Emitter current of the CB stage; simplifies to $V_{EE}/R_E$ when $V_{EE} \gg V_{BE}$ | ·L3 p13 | — |
| `[eq: cb-vcb]` | $V_{CB} = V_{CC} - I_C R_L$ | Collector–base voltage from the collector loop | ·L3 p13 | ⚠ V3.11 ($R_L$ dropped) |
| `[eq: ce-base-current]` | $I_B = \dfrac{V_{BB}-V_{BE}}{R_B} \cong \dfrac{V_{BB}}{R_B}$ | Base current of the base-bias (CE) stage | ·L3 p14 | — |
| `[eq: ce-vce]` | $V_{CE} = V_{CC} - I_C R_L$ | Collector–emitter voltage — the other half of the Q-point | ·L3 p14 | — |
| `[eq: cc-formulas]` | $I_E = \dfrac{V_{CC}-V_{BE}}{R_E+R_B/\beta}$; $\;V_{CC} = V_{CE}+I_ER_E$; $\;I_C = \beta I_B$ | The common-collector (emitter-follower) bias set | ·L3 p15 | ⚠ V3.12 |

### B3.5 Stability

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: stability-factor]` | $S = \dfrac{dI_C}{dI_{CO}}$ at constant $\beta$ and $I_B$ | How much the Q-point moves when leakage moves. Larger $S$ means worse stability | ·L3 p16 | — |
| `[eq: stability-factor-general]` | $S = \dfrac{1+R_B/R_E}{1+(1-\alpha)(R_B/R_E)}$ | The general result that specialises to every bias circuit | ·L3 p16–p17 | — |
| `[eq: beta-sensitivity]` | $\dfrac{dI_C}{I_C} = K_\beta\dfrac{d\beta}{\beta}$, i.e. $K_\beta = \dfrac{\beta}{I_C}\dfrac{dI_C}{d\beta}$ | How much the Q-point moves when the transistor is swapped. $0 \le K_\beta \le 1$ | ·L3 p17 | ⚠ V3.13 |
| `[eq: s-cb]` | $S = 1$ (common base) | The best possible stability | ·L3 p17 | — |
| `[eq: s-ce]` | $S = 1+\beta$ (common emitter) | $\beta = 100$ gives $S = 101$ — the reason every biasing scheme below exists | ·L3 p17 | — |
| † base bias | $S = (1+\beta) \cong \beta$, $K_\beta = 1$ | Plain base bias: the worst case on both counts | ·L3 p17 | — |

### B3.6 The five bias circuits

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ic-sat-general]` | $I_{C(sat)} = \dfrac{V_{CC}}{R_E+R_L}$ | Saturation current when both $R_E$ and $R_L$ are present | ·L3 p18 | — |
| `[eq: emitter-feedback-ic]` | $I_C \cong \dfrac{V_{CC}-V_{BE}}{R_E+R_B/\beta} \cong \dfrac{V_{CC}}{R_E+R_B/\beta}$ | Collector current, base bias with emitter feedback | ·L3 p18 | — |
| `[eq: kbeta-emitter-feedback]` | $K_\beta = \dfrac{1}{1+\beta R_E/R_B}$ | Beta sensitivity of the emitter-feedback stage; small when $\beta R_E \gg R_B$ | ·L3 p18 | — |
| † emitter-feedback node voltages | $V_C = V_{CC}-I_CR_L$; $V_E = I_ER_E \cong I_CR_E$; $S = \dfrac{1+R_B/R_E}{1+R_B/(1+\beta)R_E}$ | The rest of the emitter-feedback set | ·L3 p18 | — |
| `[eq: collector-feedback-ic]` | $I_C = \dfrac{V_{CC}-V_{BE}}{R_L+R_B/\beta}$; $I_{C(sat)} = \dfrac{V_{CC}}{R_L}$ | Collector current, base bias with collector feedback | ·L3 p19 | — |
| `[eq: kbeta-collector-feedback]` | $K_\beta = \dfrac{1}{1+\beta R_L/R_B} = 1-\dfrac{I_C}{I_{C(sat)}}$; $\;S = \dfrac{1+R_B/R_L}{1+R_B/(1+\beta)R_L}$ | Stability of the collector-feedback stage | ·L3 p19 | ⚠ V3.15 |
| `[eq: both-feedbacks-ic]` | $I_C = \dfrac{V_{CC}-V_{BE}}{R_E+R_L+R_B/\beta}$; $I_{C(sat)} = \dfrac{V_{CC}}{R_E+R_L}$; $V_C = V_{CC}-(I_C+I_B)R_L \cong V_{CC}-I_CR_L$; $V_E \cong I_CR_E$; $V_{CE} \cong V_{CC}-I_C(R_L+R_E)$ | Base bias with both feedbacks | ·L3 p20 | — |
| `[eq: kbeta-both-feedbacks]` | $K_\beta = \dfrac{1}{1+\beta(R_E+R_L)/R_B} = 1-\dfrac{I_C}{I_{C(sat)}}$; $\;S = \dfrac{1+R_B/(R_E+R_L)}{1+R_B/\beta(R_E+R_L)}$ | Stability with both feedbacks | ·L3 p20 | — |
| `[eq: two-supply-ie]` | $I_E = \dfrac{V_{EE}-V_{BE}}{R_E+R_B/\beta} \cong \dfrac{V_{EE}}{R_E}$ | Emitter bias with two supplies — $\beta$ vanishes from the bias equation | ·L3 p14, p21 | ⚠ V3.18 |
| † two-supply node voltage and stability | $V_E = -\left(V_{BE}+\dfrac{I_CR_B}{\beta}\right) \cong -V_{BE}$; $S = \dfrac{1+R_B/R_E}{1+R_B/\beta R_E}$; $K_\beta = \dfrac{1}{1+\beta R_E/R_B}$ | The rest of the two-supply set | ·L3 p21 | ⚠ V3.20, V3.21 |

**The pattern across all four feedback circuits:** $K_\beta = \dfrac{1}{1+\beta R_{\text{fb}}/R_B}$
and $S = \dfrac{1+R_B/R_{\text{fb}}}{1+R_B/(1+\beta)R_{\text{fb}}}$, where $R_{\text{fb}}$ is $R_E$
(emitter feedback), $R_L$ (collector feedback) or $R_E+R_L$ (both).

> ⚠ **$\beta$ or $1+\beta$ in the $S$ denominator?** **$1+\beta$.** L3 is inconsistent about this —
> ·L3 p19 prints $(1+\beta)$, ·L3 p20 and ·L3 p21 print a bare $\beta$ — and the rows above
> transcribe each page as printed. The general result the source itself derives settles it:
> $S = \dfrac{1+R_B/R_E}{1+(1-\alpha)R_B/R_E}$ with $1-\alpha = \dfrac{1}{1+\beta}$. At
> $\beta = 100$ the two forms differ by about 1 %, so a worked answer will not visibly fail — which
> is exactly why it is worth knowing which one is right.

### B3.7 Voltage-divider bias — the three methods

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: divider-v2]` | $V_2 = V_{CC}\dfrac{R_2}{R_1+R_2}$; $V_E = V_2 - V_{BE}$ | Method 1, by inspection: the base voltage set by the divider alone | ·L3 p21–p22 | — |
| `[eq: divider-ie]` | $I_E = \dfrac{V_E}{R_E} = \dfrac{V_2-V_{BE}}{R_E} \cong \dfrac{V_2}{R_E}$; $V_C = V_{CC}-I_CR_L$ | Emitter current and collector node voltage | ·L3 p22 | — |
| `[eq: divider-vce]` | $V_{CE} \cong V_{CC}-I_C(R_L+R_E)$; $I_{C(sat)} \cong \dfrac{V_{CC}}{R_L+R_E}$ | Completes the Q-point. **$\beta$ is never used** | ·L3 p22 | — |
| `[eq: kbeta-divider]` | $K_\beta = \dfrac{1}{1+\beta R_E/(R_1\parallel R_2)}$; $\;S = \dfrac{1+(R_1\parallel R_2)/R_E}{1+(R_1\parallel R_2)/(1+\beta)R_E}$ | Stability of the divider stage, with $R_B = R_1\parallel R_2$ | ·L3 p22 | C3.22 |
| `[eq: thevenin-divider]` | $V_{th} = V_{CC}\dfrac{R_2}{R_1+R_2}$; $R_{th} = R_1\parallel R_2 = \dfrac{R_1R_2}{R_1+R_2}$ | Method 2, step 1: the equivalent source | ·L3 p22 | — |
| `[eq: thevenin-ib]` | $I_B = \dfrac{V_{BB}'-V_{BE}}{R_B'+(1+\beta)R_E}$ | Method 2 solved for base current | ·L3 p22 | — |
| `[eq: thevenin-ie]` | $I_E = \dfrac{V_{BB}'-V_{BE}}{R_E+R_B'/(1+\beta)}$; $V_{CE} \cong V_{CC}-I_C(R_L+R_E)$ | Method 2 solved for emitter current — the accurate route | ·L3 p22 | — |
| `[eq: beta-rule-vb]` | $V_B = V_{CC}\dfrac{R_2\parallel(1+\beta)R_E}{R_1+R_2\parallel(1+\beta)R_E}$; $V_E = V_B-V_{BE}$; $I_E = V_E/R_E$ | Method 3, the $\beta$-rule: $R_E$ referred to the base becomes $(1+\beta)R_E$ in parallel with $R_2$ | ·L3 p22–p23 | C3.23 (both cross-references broken) |

### B3.8 Load lines and signal handling

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: dc-load-line]` | $I_{C(sat)} = \dfrac{V_{CC}}{R_L}$ (or $\dfrac{V_{CC}}{R_L+R_E}$ with an emitter resistor); $V_{CE(\text{cut-off})} = V_{CC}$ | The two end points of the dc load line | ·L3 p24 | ⚠ C3.29 ($R_1$ printed for $R_L$) |
| `[eq: ac-load-line]` | $V_{CE(\text{cut-off})} = V_{CEQ}+I_{CQ}R_{ac}$; $I_{C(sat)} = I_{CQ}+\dfrac{V_{CEQ}}{R_{ac}}$; slope $= -\dfrac{1}{R_{ac}}$ | The ac load line, which passes through the same Q-point but is steeper | ·L3 p25 | ⚠ C3.27 |
| `[eq: signal-handling]` | maximum positive swing $= I_{CQ}R_{ac}$; maximum negative swing $= V_{CEQ}$; capacity $= \min\!\left(I_{CQ}R_{ac},\,V_{CEQ}\right)$ | Largest undistorted output the stage can give | ·L3 p25 | — |
| `[eq: power-in-load]` | $P_{total} = P_{dc} + P_{ac} = I_C^2R_L + \dfrac{V_{rms}^2}{R_L}$ | Total power in the collector load | ·L3 p25 | C3.26 |

---

## B4 · Field-effect transistors ·L4

### B4.1 The JFET characteristic

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: vp-vgsoff]` | $V_{GS(off)} = -V_{PO}$, equivalently $\lvert V_{PO}\rvert = \lvert V_{GS(off)}\rvert$ | Pinch-off voltage and cut-off voltage are the same magnitude, opposite sign | ·L4 p5 | V4.2 ($V_P$ used with both signs across the chapter) |
| `[eq: shockley]` | $I_D = I_{DSS}\left(1-\dfrac{V_{GS}}{V_P}\right)^{2} = I_{DSS}\left(1-\dfrac{V_{GS}}{V_{GS(off)}}\right)^{2}$ | **Shockley's equation** — drain current in the pinch-off region. The square is why the JFET is a square-law device | ·L4 p6 | C4.5, C4.6 |
| `[eq: pinchoff-general]` | $V_P = V_{DS(P)} - V_{GS}$ | The $V_{DS}$ at which pinch-off occurs for a given gate bias | ·L4 p7 | — |
| `[eq: shockley-inverse]` | $V_{GS} = V_{GS(off)}\left(1-\sqrt{\dfrac{I_D}{I_{DSS}}}\right)$ | Gate voltage needed for a target drain current | ·L4 p7 | — |

### B4.2 JFET small-signal parameters

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ac-drain-resistance]` | $r_d = \dfrac{\delta V_{DS}}{\delta I_D}$ at constant $V_{GS}$; output admittance $y_{os} = 1/r_d$ | Dynamic drain resistance $r_{ds}$ — the output resistance of the device | ·L4 p7–p8 | ⚠ V4.3 |
| `[eq: transconductance]` | $g_m = \dfrac{\delta I_D}{\delta V_{GS}}$ at constant $V_{DS}$ | Transconductance, in siemens. Also written $g_{fs}$ or $y_{fs}$ | ·L4 p8 | ⚠ V4.4 |
| † $g_m$ from Shockley | $g_m = -\dfrac{2I_{DSS}}{V_P}\left(1-\dfrac{V_{GS}}{V_P}\right)$ | $g_m$ at any bias, by differentiating Shockley with respect to $V_{GS}$ | ·L4 p8 | ⚠ V4.5 |
| `[eq: gmo]` | $g_{mo} = -\dfrac{2I_{DSS}}{V_P} = \dfrac{2I_{DSS}}{\lvert V_{GS(off)}\rvert}$ | The largest value of $g_m$, at $V_{GS} = 0$ | ·L4 p8 | — |
| `[eq: gm-from-gmo]` | $g_m = g_{mo}\left(1-\dfrac{V_{GS}}{V_P}\right) = g_{mo}\sqrt{\dfrac{I_D}{I_{DSS}}}$ | $g_m$ from the data-sheet $g_{mo}$ — the form the examples use | ·L4 p8 | ⚠ V4.6 |
| `[eq: amplification-factor]` | $\mu = \dfrac{\delta V_{DS}}{\delta V_{GS}}$ at constant $I_D$; $\;\mu = g_m r_d = g_{fs}r_d$ | Amplification factor, dimensionless | ·L4 p8 | ⚠ V4.4 |
| `[eq: dc-drain-resistance]` | $R_{DS} = \dfrac{V_{DS}}{I_D}$ | The **static** channel resistance — a ratio of totals, not increments | ·L4 p8 | — |

### B4.3 JFET biasing and the load line

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: self-bias]` | $V_S = I_DR_S \Rightarrow V_{GS} = -I_DR_S$ | Self-bias: the drain current makes its own gate bias | ·L4 p9 | — |
| `[eq: source-bias]` | $V_{GS} = V_{SS} - I_DR_S$ | Source bias, from a negative source supply | ·L4 p9 | — |
| `[eq: divider-bias]` | $V_{GS} = V_{DD}\dfrac{R_2}{R_1+R_2} - I_DR_S$ | Voltage-divider bias | ·L4 p9 | — |
| `[eq: load-line]` | At $I_D = 0$: $V_{DS} = V_{DD}$. At $V_{DS} = 0$: $I_D = \dfrac{V_{DD}}{R_L}$ | The two end points of the dc load line | ·L4 p9 | Caution: use $R_L+R_S$ when a source resistor is present |
| `[eq: midpoint-bias]` | $V_{DSQ} = \tfrac12 V_{DD}$; $I_{DSQ} = \dfrac{\tfrac12 V_{DD}}{R_S+R_L}$ | Class-A Q-point at the middle of the load line | ·L4 p10 | — |

### B4.4 The three FET amplifier configurations

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: av-common-source]` | $A_v = -g_m\left(r_d\parallel R_L\right) = \dfrac{-g_mr_dR_L}{r_d+R_L} = \dfrac{-\mu R_L}{r_d+R_L}$ | Common-source voltage gain. The minus sign is the phase inversion | ·L4 p12 | — |
| `[eq: miller-input-capacitance-fet]` | $C_i = C_{gs} + \left(1-A_v\right)C_{gd}$ | Input capacitance, magnified by the Miller effect; $(1-A_v) > 1$ because $A_v$ is negative | ·L4 p12 | — |
| `[eq: av-common-drain]` | $A_v = \dfrac{g_mr_dR_L}{r_d+R_L+g_mr_dR_L} \cong 1$ when $g_mr_dR_L \gg (r_d+R_L)$ | Common-drain (source follower) gain — just under unity | ·L4 p13 | ⚠ V4.11 |
| † CD input resistance | $r'_{in} = R_1\parallel R_2$ | Input resistance of the source follower as drawn in Fig. 63.18(a) | ·L4 p13 | — |
| `[eq: ro-common-drain]` | $r'_o = \dfrac{r_d}{1+g_mr_d}\parallel R_L \cong \dfrac{1}{g_m}\parallel R_L$ | Output resistance of the follower — low, which is the point of it | ·L4 p13 | — |
| `[eq: av-common-gate]` | $A_v = \dfrac{g_mr_dR_L}{r_d+R_L} = +g_m\left(r_d\parallel R_L\right)$ | Common-gate gain: same magnitude as CS but **positive** — no inversion | ·L4 p14 | C4.10 |
| `[eq: ri-common-gate]` | $r_i = \dfrac{V_i}{i_d} = \dfrac{1}{g_m}$; and for the whole circuit $r'_i = \dfrac{1}{g_m}\parallel R_S$ | Common-gate input resistance — low, which is why it matches low-impedance sources | ·L4 p14–p15 | — |

### B4.5 MOSFETs

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: emosfet-k]` | $I_D = K\left(V_{GS}-V_{GS(th)}\right)^{2}$; $\;K = \dfrac{I_{D(ON)}}{\left(V_{GS}-V_{GS(th)}\right)^{2}}$ | The enhancement-MOSFET square law, and how to get $K$ off a data sheet | ·L4 p19 | C4.15 |
| `[eq: emosfet-gm]` | $g_m = \dfrac{dI_D}{dV_{GS}} = 2K\left(V_{GS}-V_{GS(th)}\right)$ | Transconductance of an E-MOSFET | ·L4 p20 | — |

An E-MOSFET has **no $I_{DSS}$**: at $V_{GS} = 0$ it passes nothing. Shockley's equation does not
apply to it — use the $K$ equation instead.

---

## B5 · Fabrication and integrated circuits ·L5

L5 is a descriptive lesson. It contains **exactly one equation**.

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ic-diffused-resistor]` | $R = \rho\dfrac{l}{a} = \dfrac{\rho\,l}{w\,d}$ | Value of a diffused IC resistor from its geometry. $\rho$ in $\Omega\!\cdot\!$cm, $l$, $w$, $d$ in cm | ·L5 p16 | ⚠ V5.4 (denominator printed unbracketed) |
| `[eq: sheet-resistance]` | $R = R_s\,n$, with $R_s = \dfrac{\rho}{d}$ ($\Omega$ per square) and $n = \dfrac{l}{w}$ (number of squares) | The same equation in the form that makes the page's sheet-resistance numbers usable | **[added]** at ·L5 p17 | — |

---

## B6 · $h$-parameters and BJT amplifiers ·L6

### B6.1 The hybrid model

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: two-port-h-equations]` | $V_i = h_{11}I_i + h_{12}V_o$; $\;I_o = h_{21}I_i + h_{22}V_o$ — alphabetically $V_i = h_iI_i + h_rV_o$ and $I_o = h_fI_i + h_oV_o$ | The two defining equations of the hybrid two-port | ·L6 p3–p4 | — |
| `[eq: h-i-def]` | $h_{11} = h_i = \dfrac{V_i}{I_i}$ with $V_o = 0$ — units Ω | Input resistance, output short-circuited | ·L6 p4 | — |
| `[eq: h-r-def]` | $h_{12} = h_r = \dfrac{V_i}{V_o}$ with $I_i = 0$ — dimensionless | Reverse voltage transfer ratio, input open-circuited | ·L6 p4 | ⚠ V6.1 |
| `[eq: h-f-def]` | $h_{21} = h_f = \dfrac{I_o}{I_i}$ with $V_o = 0$ — dimensionless | Short-circuit forward current gain | ·L6 p4 | C6.1 |
| `[eq: h-o-def]` | $h_{22} = h_o = \dfrac{I_o}{V_o}$ with $I_i = 0$ — units S | Output admittance, input open-circuited | ·L6 p4 | — |

Memory hook: the two parameters that multiply $I_i$ ($h_i$, $h_f$) are measured with $V_o = 0$;
the two that multiply $V_o$ ($h_r$, $h_o$) are measured with $I_i = 0$.

### B6.2 The three configurations

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: ce-h-equations]` | $v_b = h_{ie}i_b + h_{re}v_c$; $\;i_c = h_{fe}i_b + h_{oe}v_c$ | Common-emitter model: B → C, E common | ·L6 p6, p7 | ⚠ V6.2 (the ·L6 p7 table row) |
| `[eq: cb-h-equations]` | $v_e = h_{ib}i_e + h_{rb}v_c$; $\;i_c = h_{fb}i_e + h_{ob}v_c$ | Common-base model: E → C, B common | ·L6 p7 | ⚠ V6.2 (the ·L6 p7 table row) |
| `[eq: cc-h-equations]` | $v_b = h_{ic}i_b + h_{rc}v_e$; $\;i_e = h_{fc}i_b + h_{oc}v_e$ | Common-collector model: B → E, C common | ·L6 p7 | — |

Typical CE values ·L6 p8: $h_{ie} = 1100\ \Omega$, $h_{re} = 2.5\times10^{-4}$, $h_{fe} = 50$,
$h_{oe} = 25\ \mathrm{\mu S}$ (so $1/h_{oe} = 40\ \mathrm{k}\Omega$).

### B6.3 The exact loaded-amplifier results

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: current-gain-ai]` | $A_I = \dfrac{-I_2}{I_1} = \dfrac{-h_f}{1+Z_Lh_o}$ | Current gain of the loaded amplifier | ·L6 p9 | C6.3 |
| `[eq: input-impedance-zi]` | $Z_i = h_i - \dfrac{h_fh_r}{Y_L+h_o}$, with $Y_L = 1/Z_L$ | Input impedance seen by the source | ·L6 p10 | ⚠ V6.3 (CC row of the table) |
| `[eq: voltage-gain-av]` | $A_V = \dfrac{A_I\,Z_L}{Z_i}$ | Voltage gain — current gain times the impedance transformation ratio. Serves all three configurations | ·L6 p10 | — |
| `[eq: power-gain-ap]` | $A_P = A_V A_I$ | Power gain | ·L6 p15 | — |
| `[eq: output-admittance-yo]` | $Y_o = h_o - \dfrac{h_fh_r}{R_s+h_i}$, with $R_o = \dfrac{1}{Y_o}$ | Output admittance, source killed and load removed | ·L6 p11 | C6.4 |
| `[eq: voltage-gain-source-avs]` | $A_{VS} = \dfrac{A_V Z_i}{R_s+Z_i} = \dfrac{A_I R_L}{R_s+Z_i}$ | Overall gain referred to the **source** voltage. Reduces to $A_V$ when $R_s = 0$ | ·L6 p11–p12 | — |
| `[eq: current-gain-source-ais]` | $A_{IS} = \dfrac{A_I R_s}{R_s+Z_i}$ | Overall gain referred to the source current | ·L6 p12 | — |
| `[eq: avs-from-ais]` | $A_{VS} = \dfrac{A_{IS}Z_L}{R_s}$ | The bridge between the two overall gains | ·L6 p12 | — |

Note the mirror-image structure: $A_{VS}$ carries $Z_i$ in its numerator, $A_{IS}$ carries $R_s$.

### B6.4 Converting between configurations

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: conv-cb]` | $h_{ib} = \dfrac{h_{ie}}{1+h_{fe}}$; $\;h_{rb} = \dfrac{h_{ie}h_{oe}}{1+h_{fe}} - h_{re}$; $\;h_{fb} = \dfrac{-h_{fe}}{1+h_{fe}}$; $\;h_{ob} = \dfrac{h_{oe}}{1+h_{fe}}$ | CE data-sheet parameters converted to CB. Three of the four are "divide by $1+\beta$" | ·L6 p13 | — |
| `[eq: conv-cc]` | $h_{ic} = h_{ie}$; $\;h_{rc} = 1$; $\;h_{fc} = -(1+h_{fe})$; $\;h_{oc} = h_{oe}$ | CE converted to CC. $h_{rc} = 1$ is another way of saying the follower has $A_V \approx 1$ | ·L6 p13 | — |

### B6.5 Approximate analysis — the block worth memorising

The approximate model deletes $h_r$ and $h_o$; it is valid when $h_{oe}R_L < 0.1$.

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: approx-ce]` | $A_I = -h_{fe}$; $\;R_i = h_{ie}$; $\;A_V = \dfrac{-h_{fe}R_L}{h_{ie}}$; $\;R_o = \infty$ | The complete approximate CE set | ·L6 p17–p19 | C6.5 |
| `[eq: ce-ri-correction]` | $R_i = h_{ie}\left[1-0.5\,h_{oe}R_L\right]$ | First-order correction to $R_i$; at the limit $h_{oe}R_L = 0.1$ it is a 5 % underestimate | ·L6 p18 | — |
| `[eq: approx-cc]` | $A_I = 1+h_{fe}$; $\;R_i = h_{ie}+(1+h_{fe})R_L$; $\;A_V = 1-\dfrac{h_{ie}}{R_i}$; $\;R_o = \dfrac{h_{ie}+R_s}{1+h_{fe}}$ (and $R_o' = R_o\parallel R_L$) | The complete approximate CC set — the only one with a finite $R_o$ | ·L6 p20, p22 | C6.6 |
| `[eq: approx-cb]` | $A_I = \dfrac{h_{fe}}{1+h_{fe}} = -h_{fb}$; $\;R_i = \dfrac{h_{ie}}{1+h_{fe}} = h_{ib}$; $\;A_V = \dfrac{h_{fe}R_L}{h_{ie}}$; $\;R_o = \infty$ | The complete approximate CB set. The gain is positive — no inversion | ·L6 p21–p22 | — |

CE = the general-purpose amplifier (gain in both current and voltage, and the only inverter).
CB = the impedance step-up stage (lowest $R_i$, highest $R_o$). CC = the impedance step-down
buffer (highest $R_i$, lowest $R_o$).

### B6.6 $\Delta h$ compact forms — supplied here

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: delta-h]` | $\Delta h = h_ih_o - h_fh_r$ | Determinant of the hybrid matrix; dimensionless, typically 0.015–0.02 for a CE transistor | **[added]** §6.24 | — |
| `[eq: zi-delta-h]` | $Z_i = \dfrac{h_i + \Delta h\,Z_L}{1+h_oZ_L}$ | Input impedance in the form other textbooks and formula sheets use | **[added]** §6.24 | — |
| `[eq: yo-delta-h]` | $Y_o = \dfrac{h_oR_s + \Delta h}{R_s+h_i}$ | Output admittance in the same form | **[added]** §6.24 | — |

> The notes never introduce $\Delta h$. These three are algebraically identical to §6.3's results
> and are supplied because a CAT drawn from another source may state them this way.

---

## B7 · Multistage amplifiers, feedback and frequency response ·L7

> **Symbol clash, stated once.** In this lesson $\beta$ is the **feedback fraction** (dimensionless,
> typically 0.01–0.1). In Lesson 3 and Lesson 6 $\beta$ is the **transistor current gain** (tens to
> hundreds). Both meanings appear on ·L7 p11. Read which one a formula wants before substituting.

### B7.1 The feedback equation

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: feedback-gain-positive]` | $A' = \dfrac{A}{1-\beta A}$ | Closed-loop gain with **positive** feedback | ·L7 p2 | — |
| `[eq: feedback-gain-negative]` | $A' = \dfrac{A}{1+\beta A}$ | Closed-loop gain with **negative** feedback | ·L7 p2 | — |
| `[eq: feedback-gain]` | $A_f = \dfrac{A}{1\pm\beta A}$; the $+$ sign is **negative** feedback ($A_f < A$), the $-$ sign is positive feedback ($A_f > A$) | The single form worth memorising | ·L7 p2 | — |
| `[eq: sacrifice-factor]` | $S = \dfrac{A}{A'}$, which for negative feedback is $1+\beta A$ | How much gain was traded for stability, bandwidth and low distortion | ·L7 p2 | — |
| `[eq: high-loop-gain]` | $A' \cong \dfrac{1}{\beta}$ when $\lvert\beta A\rvert \gg 1$ | The whole reason for using negative feedback: gain set by a resistor ratio alone | ·L7 p3 | — |
| `[eq: oscillation-condition]` | Feedback must be **positive** and $\beta A = +1$ | The two conditions for the amplifier to become an oscillator | ·L7 p3 | — |

### B7.2 What negative feedback buys

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: gain-stability]` | $\dfrac{dA'}{A'} = \dfrac{1}{1+\beta A}\cdot\dfrac{dA}{A}$ | Fractional drift in $A$ divided by the loop gain | ·L7 p5 | — |
| `[eq: gain-stability-highloop]` | $\dfrac{dA'}{A'} = \dfrac{1}{\beta A}\cdot\dfrac{dA}{A}$ when $\beta A \gg 1$ | The working approximation | ·L7 p5 | — |
| `[eq: distortion-reduction]` | $D' = \dfrac{D}{1+\beta A}$ | Distortion divided by the loop gain | ·L7 p5–p6 | C7.4 |
| `[eq: rin-series]` | $R_i' = R_i\,(1+\beta A)$ | **Series** feedback always raises the input impedance | ·L7 p9 | — |
| `[eq: rout-series]` | $R_o' = \dfrac{R_o}{1+\beta A}$ | **Voltage-sampled** feedback always lowers the output impedance | ·L7 p9 | — |
| `[eq: bandwidth-def]` | $BW = f_2 - f_1$; also written $\Delta f = f_2-f_1$ | Bandwidth, the span between the two half-power corners | ·L7 p8, p23 | ⚠ C7.22 |
| `[eq: lower-cutoff-feedback]` | $f_1' = \dfrac{f_1}{1+\beta A}$ | Lower corner moves **down** by the loop gain | ·L7 p8 | — |
| `[eq: upper-cutoff-feedback]` | $f_2' = f_2\,(1+\beta A)$ | Upper corner moves **up** by the loop gain | ·L7 p8 | — |
| `[eq: gbp-constant]` | $A\times BW = A'\times BW'$, i.e. $A(f_2-f_1) = A'(f_2'-f_1')$ | The gain–bandwidth trade: gain lost is bandwidth bought | ·L7 p8 | ⚠ V7.6 |

### B7.3 Feedback over several stages

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: cascade-per-stage]` | $A_1 = \left(\dfrac{A}{1+A\beta_1}\right)^{\!n}$ | Overall gain when each of $n$ stages has its own loop | ·L7 p6 | — |
| `[eq: cascade-overall]` | $A_2 = \dfrac{A^{n}}{1+A^{n}\beta_2}$ | Overall gain with one loop round the whole chain | ·L7 p6 | ⚠ V7.3 |
| `[eq: cascade-sensitivity-ratio]` | $\dfrac{dA_2/A_2}{dA_1/A_1} = \dfrac{1}{(1+A\beta)^{\,n-1}}$ | For equal overall gain, one loop round everything is far more stable than $n$ separate loops | ·L7 p6 | ⚠ V7.4 |

### B7.4 The four feedback topologies

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: beta-voltage-divider]` | $V_f = V_o\dfrac{R_1}{R_1+R_2} = \beta V_o$, so $\beta = \dfrac{R_1}{R_1+R_2}$ | Feedback fraction of the voltage-series (shunt-derived series-fed) amplifier | ·L7 p10 | — |
| `[eq: beta-current-series]` | $\beta = \dfrac{R_E}{R_C}$ | Feedback fraction of the current-series amplifier (an unbypassed $R_E$) | ·L7 p11 | — |
| `[eq: gain-current-series]` | $A = \dfrac{R_C}{r_e}$ and $A' = \dfrac{R_C}{r_e+R_E}$ | Open- and closed-loop gain of that stage; consistent with $A/(1+\beta A)$ | ·L7 p11 | — |
| `[eq: beta-voltage-shunt]` | $\beta = \dfrac{R_C}{R_F}$ | Feedback fraction of the voltage-shunt amplifier ($R_F$ from collector to base) | ·L7 p12 | V7.9 (text names $R_E$ for $R_F$) |

Series feedback raises $R_i$; shunt feedback lowers it. Voltage (shunt-derived) sampling lowers
$R_o$; current sampling raises it.

### B7.5 Cascades and the decibel

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: cascade-gain-product]` | $A_v = A_{v1}\times A_{v2}\times A_{v3}\times\cdots$ | Overall gain of a cascade is the **product** of the stage gains | ·L7 p15 | — |
| `[eq: cascade-gain-db]` | $G = G_1 + G_2 + G_3 + \cdots$ | In decibels the same thing becomes a **sum** | ·L7 p15 | — |
| `[eq: power-gain-db]` | $A_p = A_v\cdot A_i$; $\;G_p = 10\log_{10}A_p\ \mathrm{dB}$ | Power gain and its decibel form | ·L7 p15 | — |
| † decibel definitions | $G_p = 10\log_{10}\dfrac{P_2}{P_1}$ dB; $\;G_v = 20\log_{10}\dfrac{V_2}{V_1}$ dB; $\;G_i = 20\log_{10}\dfrac{I_2}{I_1}$ dB | **$10\log$ for power, $20\log$ for voltage or current** | **[added]** at ·L7 p22 | — |
| `[eq: one-db-ratio]` | $\dfrac{P_2}{P_1} = 10^{0.1} = 1.26$ | 1 dB is a 26 % increase in power | ·L7 p22 | — |
| `[eq: dbm]` | $G_p = 10\log_{10}\dfrac{P_2}{0.001}\ \mathrm{dBm}$ | Absolute level referred to 1 mW; independent of load impedance | ·L7 p22 | ⚠ C7.21 |

### B7.6 Frequency response

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: half-power-voltage]` | $A_v = \dfrac{1}{\sqrt2}A_{v(\text{mid})} = 0.707\,A_{v(\text{mid})}$ | Definition of a cut-off frequency, in voltage terms | ·L7 p23 | — |
| `[eq: half-power-power]` | $A_{p.1} = A_{p.2} = \tfrac12 A_{p(\text{mid})}$ | The same definition in power terms — and $-3$ dB in decibels | ·L7 p23 | — |
| `[eq: lower-cutoff-rc]` | $f_1 = \dfrac{1}{2\pi C R_{eq}}$ | Lower corner contributed by one coupling or bypass capacitor. $R_{eq}$ is what that capacitor sees, looking both ways | ·L7 p24 | — |
| `[eq: miller-capacitance]` | $C_{bc}$ appears at the input as $(1+A_v)\,C_{bc}$ | The Miller effect: the collector–base capacitance is magnified by the stage gain | ·L7 p25 | — |
| `[eq: miller-input-capacitance-bjt]` | $C_{in} = C_{be} + (1+A_v)C_{bc}$, plus $C_{wi}$ if a wiring capacitance is given | Total input capacitance — what sets the high-frequency limit of a CE stage | ·L7 p25 | V7.18 (the example's $A_v$ line, not this formula) |
| `[eq: upper-cutoff-rc]` | $f_2 = \dfrac{1}{2\pi R_{eq}C_{in}}$ | Upper corner from the input capacitance | ·L7 p25 | V7.19 (the example's $A_v$ line, not this formula) |
| `[eq: cascade-lower-cutoff]` | $f_{1.n} = 1.1\sqrt{n}\,f_1 = \dfrac{f_1}{\sqrt{2^{1/n}-1}}$ | Lower corner of $n$ identical stages — it rises | ·L7 p26 | — |
| `[eq: cascade-upper-cutoff]` | $f_{2.n} = \dfrac{f_2}{1.1\sqrt{n}} = \sqrt{2^{1/n}-1}\;f_2$ | Upper corner of $n$ identical stages — it falls. Cascading always narrows the band | ·L7 p26 | — |

> **Two Miller forms, one idea.** The tag is split by device — `[eq: miller-input-capacitance-fet]` and `[eq: miller-input-capacitance-bjt]` — because the two lessons use opposite sign conventions for $A_v$: here for
> the BJT, $C_{in} = C_{be}+(1+A_v)C_{bc}$ ·L7 p25, and in L4 for the JFET,
> $C_i = C_{gs}+(1-A_v)C_{gd}$ ·L4 p12. They are the same physical effect written with opposite
> sign conventions — L4 keeps $A_v$ signed (negative), L7 uses its magnitude. Check which device
> the question is about before substituting.

### B7.7 Transistor cut-off frequencies

| Tag | Equation | What it gives you | Source | Flag |
|---|---|---|---|---|
| `[eq: alpha-cutoff]` | $\alpha(f_\alpha) = 0.707\,\alpha_{\text{low-}f}$ | Definition of $f_\alpha$: where CB current gain has fallen to 0.707 of its 1 kHz value | ·L7 p26 | — |
| `[eq: falpha-ft]` | $f_\alpha = 1.2\,f_T$ | Relates the alpha cut-off to the transition frequency | ·L7 p26 | C7.26 |
| `[eq: fbeta-ft]` | $f_\beta = \dfrac{f_T}{\beta}$, with $\beta$ the low-frequency current gain | Relates the beta cut-off to $f_T$ | ·L7 p26 | C7.26 |
| `[eq: gbp-ft]` | $\text{GBP} = \text{gain}\times\text{bandwidth} = f_T$ | For any amplifier the gain–bandwidth product equals $f_T$: more gain costs bandwidth | ·L7 p26–p27 | — |


---

# The concordance — results that appear in both tiers

Twenty-eight results are derived independently by both a lecture-note page and a lesson handout.
Every pairing below was checked equation against equation in the two topic files before being
asserted here; the verdict column says what the check found.

**Why this table matters.** Two sources that were compiled separately, agreeing on a constant, is
a much stronger warrant than either page alone — and where one page is defective, the other
settles it. Four of the rows below are the reason a tier-2 flag can be stated with confidence.

### C1 · Rectifiers

| Result | Tier 1 ·J | Tier 2 ·L | Verdict |
|---|---|---|---|
| Half-wave average | $I_{dc} = \dfrac{I_m}{\pi} = 0.3183\,I_m$ ·J p47 | $V_{L(dc)} = \dfrac{V_{LM}}{\pi} = 0.318\,V_{LM}$ ·L2 p3 | **Agree exactly.** Same constant, one stated as a current, one as a voltage |
| Half-wave rms | $I_{rms} = \dfrac{I_m}{2}$ ·J p47 | $V_L = \dfrac{V_{LM}}{2} = 0.5\,V_{LM}$ ·L2 p3, ⚠ C2.3 | **Agree exactly** — and ·J prints it cleanly where ·L2's page needed a flag |
| Full-wave average | $I_{dc} = \dfrac{2I_m}{\pi} = 0.6366\,I_m$ ·J p48–p49 | $V_{L(dc)} = \dfrac{2V_{LM}}{\pi} = 0.636\,V_{LM}$ ·L2 p8, ⚠ C2.10 | **Agree exactly.** Exactly twice the half-wave value in both |
| Full-wave rms | $I_{rms} = \dfrac{I_m}{\sqrt2} = 0.707\,I_m$ ·J p49 | $V_L = \dfrac{V_{LM}}{\sqrt2} = 0.707\,V_{LM}$ ·L2 p8 | **Agree exactly** |
| Half-wave efficiency | $\dfrac{4}{\pi^{2}} = 40.5\,\%$, divided by $(1+r_f/R_L)$ ·J p47 | $\dfrac{4}{\pi^{2}} = 40.5\,\%$, divided by $(1+R_0/R_L)$ ·L2 p4 | **Agree on the constant.** Printed roundings differ: ·J p47 prints 40.5 %, the ·L2 handout prints 40.6 % (C2.4). $4/\pi^2 = 40.53\,\%$, so **·J's rounding is the accurate one** |
| Full-wave efficiency | $\dfrac{8}{\pi^{2}} = 81.1\,\%$ ·J p49 | $\dfrac{8}{\pi^{2}} = 81.1\,\%$ ·L2 p8 | **Agree on the constant.** ·L2's handout prints 81.2 % (C2.4); $8/\pi^2 = 81.06\,\%$, so again **·J's rounding is right.** Both sources make it exactly twice the half-wave figure |
| Half-wave ripple factor | $\sqrt{\dfrac{\pi^{2}}{4}-1} = 1.21$ ·J p48 | $\sqrt{\dfrac{\pi^{2}}{4}-1} = 1.211$ ·L2 p5 | **Agree.** ·L2 reaches it by two further routes — from the form factor $K_f = \pi/2$ and from the harmonic sum |
| Full-wave ripple factor | $\sqrt{\dfrac{\pi^{2}}{8}-1} = 0.48$ ·J p49 | $\sqrt{\dfrac{\pi^{2}}{8}-1} = 0.483$ ·L2 p9 | **Agree.** ·L2's page prints 0.482 (C2.12); the exact value is 0.4834 |
| The ac/dc split | $I_{rms}^{2} = I_{dc}^{2}+I_{ac}^{2}$ ·J p47–p49 | Same, plus $\gamma = \sqrt{K_f^{2}-1}$ ·L2 p5 | **Agree**; tier 2 is fuller |
| dc power | $P_{dc} = I_{dc}^{2}R_L$ ·J p47, p49 | $P_{dc} = I_{L(dc)}^{2}R_L$ ·L2 p4 | **Agree** — but ·L2 p8 misprints it as $I_{dc}^{2}(R_0+R_L)$, flagged V2.10. **·J is right** |

### C2 · Diodes

| Result | Tier 1 ·J | Tier 2 ·L | Verdict |
|---|---|---|---|
| Shockley's diode equation | $i_D = I_o\!\left(e^{V_D/\eta V_T}-1\right)$ ·J p35, ⚠ JV4.3 | $I = I_0\!\left(e^{V/\eta V_T}-1\right)$ ·L1 p6, ⚠ V1.2, V1.3 | **Agree on the corrected form — and each source gets one half right.** ·J places the $-1$ correctly outside the bracket where ·L1 puts it inside the exponent four times (V1.3); ·L1 forms the exponent correctly where ·J typesets it as a denominator (JV4.3). The corrected equation is ·L1's exponent with ·J's $-1$ |
| Ideality factor | $\eta = 1$ (Ge), $\eta = 2$ (Si) ·J p35 | Same values ·L1 p6, though $\eta$ is dropped from the highlighted master form (V1.2) | **Agree on the values**; ·J's equation is the better-formed one |
| Thermal voltage | $V_T = \dfrac{kT}{q}$, evaluated 25.9 ≈ 26 mV at 300 K ·J p35 | $V_T = \dfrac{kT}{e} = \dfrac{T}{11{,}600}$; 26 mV at 300 K, 25 mV at 293 K ·L1 p3, p6 | **Agree** ($q \equiv e$). ·J p35 prints $k = 1.38\times10^{-28}$, out by $10^{5}$ (JV4.2) — **take the constant from ·L1** |
| Ge / Si turn-on voltage | 0.2–0.3 V and 0.6–0.7 V ·J p34, p38 | $V_B = 0.3$ V (Ge), 0.7 V (Si) ·L1 p5 | **Agree** |
| Varactor capacitance | $C = \dfrac{\varepsilon A}{d}$ ·J p44 | $C = \dfrac{K}{\sqrt{V_R}}$ ·L1 p7 | **Same law, two forms** — geometry form against voltage form. Not the same equation, and both are worth having: ·J explains *why* $C$ falls, ·L1 lets you compute it from $V_R$ |
| dc load line | $V_D$-intercept $= V_{Th}$, $I_D$-intercept $= \dfrac{V_{Th}}{R_{Th}+R_L}$ ·J p36, p40 | The same construction, but supplied as **[added]** — ·L1 names the load line in its own outline and never draws it | **·J closes a tier-2 gap from the primary source** |

### C3 · The BJT

| Result | Tier 1 ·J | Tier 2 ·L | Verdict |
|---|---|---|---|
| $I_E = I_C + I_B$ | ·J p58, p60 | ·L3 p3 | **Agree** |
| $\alpha = \dfrac{I_C}{I_E}$ | printed correctly **twice**, ·J p60 and ·J p63 | printed **inverted** as $I_E/I_C$, ·L3 p4, ⚠ V3.1 | **·J is right.** This is the clearest case of the primary source confirming a tier-2 flag independently |
| $\beta = \dfrac{\alpha}{1-\alpha}$ and $\alpha = \dfrac{\beta}{1+\beta}$ | both derived, ·J p63 | both derived, ·L3 p6 | **Agree exactly** |
| $\theta = \dfrac{I_E}{I_B} = 1+\beta$ | ·J p62, with a symbol slip in the first term (JV6.5) | ·L3 p6, same chain, no slip | **Agree on the result** |
| $I_C = \alpha I_E + I_{CBO}$ | ·J p63 | ·L3 p7, but supplied as **[added]** — the printed page is missing from the extract | **Agree.** ·J is the only source that prints it |
| $I_{CEO} = (1+\beta)I_{CBO} = \dfrac{I_{CBO}}{1-\alpha}$ | **derived on the page**, ·J p64 | present but **reconstructed** — the ·L3 pages carrying the derivation are missing from the extract | **Agree.** ·J is fuller: it has the derivation tier 2 had to supply as `[added]` |
| $I_C = \beta I_B + (1+\beta)I_{CBO}$ | ·J p63, ⚠ JV6.6 | ·L3 p16 | **Agree** |
| Base bias | $I_B = \dfrac{V_{CC}-V_{BE}}{R_B}$, $I_{C(sat)} = \dfrac{V_{CC}}{R_C}$, $S = 1+\beta$ ·J p70 | Same three, ·L3 p14, p17 | **Agree** |
| Divider bias, Thevenin route | $V_{Th}$, $R_{Th}$ and the two loops, ·J p73–p74 | $V_{th}$, $R_{th}$, $I_B$ and $I_E$ solved, ·L3 p22 | **Agree exactly** on $V_{Th}$ and $R_{Th}$; tier 2 also carries the solved $I_B$ and $I_E$, and two further methods ·J does not give |
| Stability factor | $S = \dfrac{\mathrm dI_C}{\mathrm dI_{CBO}}$; $S = \dfrac{1+R_B/R_E}{1+R_B/(1+\beta)R_E}$ ·J p81; also $(1+\beta)\dfrac{1+R_B/R_E}{1+\beta+R_B/R_E}$ ·J p83 | $S = \dfrac{\mathrm dI_C}{\mathrm dI_{CO}}$; $S = \dfrac{1+R_B/R_E}{1+(1-\alpha)R_B/R_E}$ ·L3 p16–p17 | **Agree exactly.** All three expressions are algebraically identical, since $1-\alpha = \dfrac{1}{1+\beta}$. Two independent sources therefore settle the $\beta$-versus-$(1+\beta)$ question in the denominator: it is **$1+\beta$** |
| dc load-line intercepts | $I_{C(sat)} = \dfrac{V_{CC}}{R_C+R_E}$, $V_{CE(\text{cut-off})} = V_{CC}$ ·J p76 | $I_{C(sat)} = \dfrac{V_{CC}}{R_L}$, $V_{CE(\text{cut-off})} = V_{CC}$ ·L3 p24, ⚠ C3.29 | **Agree** — the same formula; tier 2's worked circuit simply has $R_E = 0$ |
| ac load-line intercepts | $I_{CQ}+\dfrac{V_{CEQ}}{R_{ac}}$ and $V_{CEQ}+I_{CQ}R_{ac}$ ·J p79–p80 | The identical pair, plus slope $=-\dfrac{1}{R_{ac}}$ ·L3 p25, ⚠ C3.27 | **Agree exactly** |
| Signal handling | $V_{pp(\max)} = \min\!\left(2I_{CQ}R_{ac},\,2V_{CEQ}\right)$ ·J p80 | $\min\!\left(I_{CQ}R_{ac},\,V_{CEQ}\right)$ ·L3 p25 | **Agree — same result, different convention.** ·J states it peak-to-peak, tier 2 as a peak. Check which the question wants before quoting a number |
| Decibels | $10\log_{10}A_p$, $20\log_{10}A_v$, $20\log_{10}A_i$ — all three printed, ·J p61 | $A_p = A_vA_i$ and $G_p = 10\log_{10}A_p$ ·L7 p15; the two $20\log$ forms are supplied as **[added]** at ·L7 p22 | **Agree** — and **·J is the primary source for the $10$-versus-$20$ rule**, which tier 2 uses throughout (·L7 p7) without ever stating |

### C4 · FETs

| Result | Tier 1 ·J | Tier 2 ·L | Verdict |
|---|---|---|---|
| Shockley's equation | printed **twice on one page**, once over $V_P$ and once over $V_{GS(\text{off})}$, ·J p87 | printed in the **identical** double form, ·L4 p6 | **Agree — including in the defect.** Both assert $V_P = V_{GS(\text{off})}$, flagged JV7.1 and V4.2. Both files reach the same correction independently: use $V_{GS(\text{off})}$, negative for N-channel. Tier 2's exposure is worse, because it puts *numbers* to a negative $V_P$ in three worked examples |
| Self bias | $V_{GS} = -I_SR_S$ ·J p93 | $V_{GS} = -I_DR_S$ ·L4 p9 | **Agree exactly** ($I_S = I_D$) |
| Source bias | $V_{GS} = V_{SS}-I_SR_S$ ·J p94 | $V_{GS} = V_{SS}-I_DR_S$ ·L4 p9 | **Agree exactly**, and both take $V_{SS}$ as the *magnitude* of the negative rail |
| Divider bias | $V_{R_2} = \dfrac{V_{DD}R_2}{R_1+R_2}$, $V_{GS} = V_{R_2}-I_DR_S$ ·J p94 | $V_{GS} = V_{DD}\dfrac{R_2}{R_1+R_2}-I_DR_S$ ·L4 p9 | **Agree exactly** — tier 1 splits it into two steps, tier 2 into one line |
| Gate (separate-supply) bias | $V_{GS} = -V_{GG}-I_SR_S$ ·J p93, ⚠ JV7.7 | $V_{GS} = -V_{GG}$ ·L4 p9, Fig. 63.8(a) | **They do not agree, and should not.** The two sources draw **different circuits**: ·J's gate-bias stage carries a source resistor, ·L4's takes the source straight to ground. Match the equation to the figure in front of you; do not memorise the two as one formula |
| Drain-loop equation | $V_{DD} = I_DR_D+V_{DS}+I_SR_S$ ·J p93 | Same, used as the load-line equation ·L4 p9 | **Agree** |
| E-MOSFET square law | $I_D = K\left(V_{GS}-V_{GS(\text{th})}\right)^{2}$ ·J p91, p92 | Identical, ·L4 p19 | **Agree exactly** |
| The constant $K$ | $K = \dfrac{I_{D(\mathrm{ON})}}{\left(V_{GS(\mathrm{ON})}-V_{GS(\text{th})}\right)^{2}}$ ·J p97 | $K = \dfrac{I_{D(ON)}}{\left(V_{GS}-V_{GS(\text{th})}\right)^{2}}$ ·L4 p19 | **Agree on the formula.** ·J's subscript pair $\left(I_{D(\mathrm{ON})},V_{GS(\mathrm{ON})}\right)$ is the better-labelled one — both refer to the same data-sheet ON point |
| Drain-feedback bias | $V_{GS} = V_{DS}$ ·J p96, but **printed with a wrong minus sign** (JV7.4) | $V_{GS} = V_{DS}$, with the reason stated, ·L4 p20 | **Tier 2 is right; ·J's printed sign is a slip.** The corrected forms then agree |

>  **Two of the C4 rows have no Part B row of their own.** Tier 2's gate-bias form
> ($V_{GS} = -V_{GG}$, ·L4 p9 Fig. 63.8(a)) and its drain-feedback form ($V_{GS} = V_{DS}$,
> ·L4 p20) are in `14-field-effect-transistors.md` but were never lifted into the tier-2 half of
> this sheet. They are cited here from that file.

### C5 · Where a topic exists in one tier only

| Topic | Tier | Note |
|---|---|---|
| Atoms, band structure, resistors, network theorems, capacitors, inductors, transformers | **Tier 1 only** (A1–A3) | No lesson handout covers ·J p2–p32 at all |
| Filters — capacitor, choke-input, Π — and their charge/discharge equations | **Tier 1 only** (A5.3) | Part B §B2.6's smoothing formulas are `[added]`, in **no** source |
| The zener two-state analysis method, zener clipping | **Tier 1** (A5.4) | Tier 2's zener material is in `11-diodes.md` from ·L1, as a *diode* topic |
| Photodiode, tunnel diode, the three diode models, Thevenin reduction of a diode circuit | **Tier 1 only** (A4) | Absent from ·L1 |
| PIV, TUF, form factor, Fourier content, three-phase, clampers, multipliers | **Tier 2 only** (B2) | ·J never computes a PIV |
| $\beta$-sensitivity $K_\beta$, the $\beta$-rule for divider bias, solved bias formulas | **Tier 2 only** (B3.6, B3.7) | ·J gives loop equations where tier 2 gives solved results |
| $g_m$, $r_d$, $\mu$, $g_{mo}$, $R_{DS}$, the FET load line, mid-point bias, inverse Shockley, Miller capacitance | **Tier 2 only** (B4.2, B4.3, B4.4) | **·J does not treat small-signal FET behaviour at all.** No gain in tier 1 yields a number |
| IC fabrication and diffused resistors | **Tier 2 only** (B5) | ·L5 |
| $h$-parameters, exact and approximate amplifier analysis, configuration conversion | **Tier 2 only** (B6) | ·J p61 names the $h$-symbols; ·L6 develops them |
| Feedback, multistage cascades, decibels beyond the definition, frequency response, $f_\alpha$, $f_\beta$, $f_T$ | **Tier 2 only** (B7) | ·L7 |

---

# These are the ones to memorise

Twenty-five results, chosen on the evidence in the topic files: which equations the worked examples
actually use, how often they recur, and where each source puts its own weight. The list is
**weighted towards tier 1**, because that is what the course teaches and what an examination will
mirror — but the last three blocks are **tier 2 only**, and are here because the primary notes
never cover that material at all. Everything else on this sheet can be looked up; these have to be
in the head.

## dc circuits — tier 1 only

**1 · Ohm's law and the three power forms** — $V = IR$, and
$P = IV = I^{2}R = \dfrac{V^{2}}{R}$; resistance from geometry $R = \rho\dfrac{L}{A}$.
*Reach for it* in the opening line of almost every question in the course.
*The trap:* pick the power form whose **two** quantities you already have. Computing a current you
did not need, to use $P = IV$, is where arithmetic slips enter.

**2 · Series, parallel and the two dividers** — $R_t = \sum R$; $\dfrac{1}{R_t} = \sum\dfrac{1}{R}$;
$R_t = \dfrac{R_1R_2}{R_1+R_2}$ for two; $V_{Rk} = V_s\dfrac{R_k}{R_t}$;
$I_{R3} = I_t\dfrac{R_2}{R_2+R_3}$.
*Reach for it* to reduce any network before a theorem is even needed.
*The trap:* the **two dividers carry opposite resistances on top.** The voltage divider carries its
**own** resistance; the current divider carries the **other** branch's, because the smaller
resistance takes the larger share of the current.

**3 · Thevenin and Norton** — $R_{Th} = R_N$ (open the load, short the source, look in);
$I_{RL} = \dfrac{V_{Th}}{R_{Th}+R_L}$; $I_{RL} = \dfrac{I_NR_N}{R_N+R_L}$; source transformation
$I_N = \dfrac{V_s}{R_i}$.
*Reach for it* whenever one branch current is wanted from a network with two or more sources.
*The trap:* **Thevenin opens the load and reads a voltage; Norton shorts it and reads a current.**
Step 2 is identical in both, which is why $R_N = R_{Th}$ and why the fastest route is often to find
one equivalent and transform.

## Capacitors, inductors and transformers — tier 1 only

**4 · The capacitor** — $C = \varepsilon_r\varepsilon_0\dfrac{A}{d}$; $Q = CV$;
$\dfrac{1}{C_t} = \sum\dfrac{1}{C}$ in series, $C_t = \sum C$ in parallel.
*Reach for it* for any capacitance value or combination.
*The trap:* the combination rules are the **resistor rules inverted**. Series capacitors give less
than the smallest; parallel capacitors give more than the largest. Getting this backwards is the
single commonest slip in the topic.

**5 · Energy and reactance** — $E = \tfrac12CV^{2} = \dfrac{QV}{2} = \dfrac{Q^{2}}{2C}$;
$E = \tfrac12LI^{2}$; $X_c = \dfrac{1}{2\pi fC}$; $X_L = 2\pi fL$.
*Reach for it* for stored energy and for any frequency-dependent opposition.
*The trap:* the two reactances move in **opposite** directions with frequency. A capacitor blocks
dc and passes ac; an inductor passes dc and blocks ac. Note also that the notes give **no**
inductance equations at all — the three above are `[added]`.

**6 · The transformer** — $n = \dfrac{V_p}{V_s} = \dfrac{N_p}{N_s} = \dfrac{I_s}{I_p}$;
$\eta = \dfrac{P_s}{P_p}\times100\,\%$; and with loss, $\dfrac{I_s}{I_p} = \eta\dfrac{N_p}{N_s}$.
*Reach for it* in every transformer question — the whole topic is this one line.
*The trap:* the **current ratio is inverted** relative to the voltage ratio, and it is the only
part of the relation that efficiency spoils. The voltage relation comes from flux linkage and
survives; the current relation comes from power balance and does not (JV3.8).

## Diodes

**7 · The diode static equation** — $i_D = I_o\!\left(e^{\,V_D/\eta V_T}-1\right)$, with
$V_T = \dfrac{kT}{q} \approx 26$ mV at 300 K and $\eta = 1$ (Ge), $\eta = 2$ (Si).
*Reach for it* whenever a diode current or voltage is wanted from first principles.
*The trap:* **both sources get part of it wrong, in different places.** The $-1$ sits outside the
exponential (·L1 p7 puts it inside four times, V1.3) and the exponent is an exponent, not a
denominator (·J p35 prints $V_D/e^{\eta V_T}$, JV4.3). Take the exponent from tier 2 and the $-1$
from tier 1. And $k = 1.38\times10^{-23}$, not $10^{-28}$ (JV4.2).

**8 · Turn-on voltages and the two resistances** — $V_o = 0.3$ V (Ge), $0.6$–$0.7$ V (Si);
$r_{dc} = \dfrac{V_{DQ}}{I_{DQ}}$; $r_{ac} = \dfrac{\Delta V_D}{\Delta i_D}$; tier 2 adds
$r_j = \dfrac{\eta V_T}{I_F}$ and $r_{ac} = r_B + r_j$.
*Reach for it* for any small-signal or Q-point diode resistance.
*The trap:* $r_{dc}$ is the chord **from the origin**, $r_{ac}$ the slope **at** the point, and
$r_{ac}$ is always the smaller. In tier 2's $r_j$, $I_F$ must be in **milliamps** for the answer to
come out in ohms.

**9 · Thevenin reduction and the diode load line** — $V_{Th} = V_S\dfrac{R}{R_S+R}$,
$R_{Th} = \dfrac{R_SR}{R_S+R}$, $I_D = \dfrac{V_{Th}}{R_L+R_{Th}}$; intercepts $V_D = V_{Th}$ and
$I_D = \dfrac{V_{Th}}{R_{Th}+R_L}$.
*Reach for it* for every "find the Q point" diode question — this is tier 1's own method and it is
worked twice in ·J p36–p41.
*The trap:* **$R_L$ belongs in the current intercept** (JV4.6) and **$R_S$, not $R_L$, belongs in
the $V_{Th}$ denominator** (JV4.5). The notes get one of these wrong on each of two consecutive
pages, so check both against the figure.

**10 · The zener regulator, two-state method** — off state: $V_{RL} = \dfrac{V_SR_L}{R+R_L}$, and
if $V_{RL} > V_Z$ the diode is on. On state: $I_{RL} = \dfrac{V_Z}{R_L}$,
$I_t = \dfrac{V_S-V_Z}{R}$, $I_Z = I_t - I_{RL}$, $P_Z = I_ZV_Z$.
*Reach for it* in every regulator question — the two-state test is the method the course teaches.
*The trap:* **the zener absorbs the difference.** If $V_S$ rises, all of the extra current goes
into $I_Z$; if the load draws more, $I_Z$ falls by the same amount. Always finish by checking $P_Z$
against the diode's rating — the design case is **no load**, where the diode carries everything.

## Rectifiers

**11 · The four average and rms values** — half-wave $I_{dc} = \dfrac{I_m}{\pi} = 0.318\,I_m$,
$I_{rms} = \dfrac{I_m}{2}$; full-wave $I_{dc} = \dfrac{2I_m}{\pi} = 0.636\,I_m$,
$I_{rms} = \dfrac{I_m}{\sqrt2} = 0.707\,I_m$.
*Reach for it* first in every rectifier question — everything else is built on these four numbers,
and both tiers agree on all four.
*The trap:* the half-wave rms is $\dfrac{I_m}{2}$, **not** $\dfrac{I_m}{\sqrt2}$. The zero
half-cycle counts towards the mean square, which halves it. Note the asymmetry: going full-wave
doubles the average but multiplies the rms only by $\sqrt2$.

**12 · The two efficiencies** — $\eta_{\text{HW}} = \dfrac{4}{\pi^{2}} = 40.5\,\%$,
$\eta_{\text{FW}} = \dfrac{8}{\pi^{2}} = 81.1\,\%$; with diode resistance, divide by
$\left(1+\dfrac{r_f}{R_L}\right)$.
*Reach for it* whenever "rectification efficiency" appears — and be able to **derive** it, since
that is the single most predictable question in the range.
*The trap:* the full-wave figure is **exactly twice** the half-wave one; that ratio is the fastest
check on a whole answer. Quote 40.5 % and 81.1 %; the tier-2 handout's 40.6 % and 81.2 % are the
looser roundings (C2.4).

**13 · Ripple factor** — $I_{rms}^{2} = I_{dc}^{2}+I_{ac}^{2}$, so
$\gamma = \dfrac{I_{ac}}{I_{dc}} = \sqrt{\left(\dfrac{I_{rms}}{I_{dc}}\right)^{2}-1}$;
$\gamma_{\text{HW}} = 1.21$, $\gamma_{\text{FW}} = 0.483$; ripple frequency $f$ or $2f$.
*Reach for it* for any ripple question and to justify a filter.
*The trap:* the denominator is the **dc** value, not the total rms (V2.5, V2.6). Dividing by rms
caps $\gamma$ at 1 and makes the half-wave answer of 1.21 impossible.

**14 · PIV — tier 2 only** — half-wave $V_{sm}$, centre-tap $2V_{sm}$, bridge $V_{sm}$.
*Reach for it* whenever a diode rating is asked for.
*The trap:* it is the **centre-tap** circuit that needs $2V_{sm}$, because the non-conducting diode
sees both half-secondaries in series. **·J never computes a PIV at all** — without this row there
is no reason in tier 1 to prefer the bridge over the centre-tap.

## The BJT

**15 · The current relations** — $I_E = I_C+I_B$; $\alpha = \dfrac{I_C}{I_E}$;
$\beta = \dfrac{I_C}{I_B}$; $\theta = \dfrac{I_E}{I_B} = 1+\beta$;
$\beta = \dfrac{\alpha}{1-\alpha}$; $\alpha = \dfrac{\beta}{1+\beta}$.
*Reach for it* in every single BJT question. Both tiers derive the conversions; they are the
cheapest marks in the course.
*The trap:* $\alpha$ is **collector over emitter**. ·L3 p4 prints it upside down (V3.1), which
gives $\alpha > 1$ and a negative $\beta$ — and **·J p60 prints it correctly**, which is how that
flag was confirmed. Cross-check with $\alpha = 0.99 \Rightarrow \beta = 99$.

**16 · Leakage** — $I_C = \alpha I_E + I_{CBO}$ (CB); $I_C = \beta I_B + (1+\beta)I_{CBO}$ (CE);
$I_{CEO} = (1+\beta)I_{CBO} = \dfrac{I_{CBO}}{1-\alpha}$.
*Reach for it* in every leakage and thermal-runaway question.
*The trap:* the leakage term is multiplied by $(1+\beta)$ in **common emitter** but stands alone in
**common base** — a factor of about 100. That is why CE is the thermally dangerous configuration.
$I_{CBO}$ doubles every **10 °C** for germanium and every **6 °C** for silicon (·J p64 swaps them,
JV6.8).

**17 · The bias equations** — base bias $I_B = \dfrac{V_{CC}-V_{BE}}{R_B}$; emitter feedback
$I_B = \dfrac{V_{CC}-V_{BE}}{R_B+(1+\beta)R_E}$; divider bias by Thevenin,
$V_{Th} = \dfrac{V_{CC}R_{B2}}{R_{B1}+R_{B2}}$, $R_{Th} = R_{B1}\parallel R_{B2}$,
$I_E = \dfrac{V_{Th}-V_{BE}}{R_E + R_{Th}/(1+\beta)}$; and always
$V_{CE} \cong V_{CC}-I_C(R_C+R_E)$.
*Reach for it* for the most-examined circuit set in the course.
*The trap:* the two-supply and divider circuits are designed so that **$\beta$ drops out**. If
$\beta$ dominates a divider-bias answer, either the exact Thevenin route was genuinely needed or
something has gone wrong. Watch the sign conventions on the two-supply loops — ·J p73 prints two of
its three loop equations with sign errors (JV6.9, JV6.10).

**18 · The stability factor** — $S = \dfrac{\mathrm dI_C}{\mathrm dI_{CBO}}$; $S = 1$ (CB),
$S = 1+\beta$ (base bias); general circuit form
$S = \dfrac{1+R_B/R_E}{1+R_B/(1+\beta)R_E}$.
*Reach for it* whenever bias stability, thermal runaway or transistor substitution is mentioned.
*The trap:* the denominator carries **$1+\beta$, not $\beta$** — both tiers say so independently,
which settles a question ·L3's own pages leave inconsistent. And $S$ is **dimensionless**: ·L3 p19
offers an "approximation" to $S$ that is a current (V3.16).

**19 · The two load lines and the swing** — dc: $I_{C(sat)} = \dfrac{V_{CC}}{R_C+R_E}$,
$V_{CE(\text{cut-off})} = V_{CC}$. ac: $R_{ac} = R_C\parallel R_L$,
$I_{C(sat)} = I_{CQ}+\dfrac{V_{CEQ}}{R_{ac}}$, $V_{CE(\text{cut-off})} = V_{CEQ}+I_{CQ}R_{ac}$;
$V_{pp(\max)} = \min\!\left(2I_{CQ}R_{ac},\,2V_{CEQ}\right)$; mid-point bias
$I_{CQ} = \tfrac12I_{C(sat)}$, $V_{CEQ} = \tfrac12V_{CC}$.
*Reach for it* for Q-point, clipping and maximum-undistorted-output questions.
*The trap:* the **ac** load line is the steeper one, and both pass through the same Q point. Using
$R_C$ where $R_{ac}$ belongs collapses the swing answer. And note the convention clash: ·J quotes
the swing **peak-to-peak** ($2I_{CQ}R_{ac}$), tier 2 as a **peak** ($I_{CQ}R_{ac}$).

## FETs

**20 · Shockley's equation** — $I_D = I_{DSS}\left(1-\dfrac{V_{GS}}{V_{GS(\text{off})}}\right)^{2}$,
with $V_{GS(\text{off})} < 0$ for N-channel; tier 2 adds the inverse
$V_{GS} = V_{GS(\text{off})}\left(1-\sqrt{I_D/I_{DSS}}\right)$.
*Reach for it* for any JFET or depletion-MOSFET drain current.
*The trap:* $V_P$ and $V_{GS(\text{off})}$ have **equal magnitude and opposite sign**, and live on
different axes — and **both sources print the equation twice, once over each symbol, as though they
were equal** (JV7.1, V4.2). Decide the sign convention once at the top of the answer and hold it.

**21 · The four bias equations** — drain loop $V_{DD} = I_DR_D+V_{DS}+I_SR_S$ for every stage;
then self bias $V_{GS} = -I_SR_S$; source bias $V_{GS} = V_{SS}-I_SR_S$; divider bias
$V_{GS} = V_{R_2}-I_DR_S$ with $V_{R_2} = \dfrac{V_{DD}R_2}{R_1+R_2}$; drain feedback
$V_{GS} = V_{DS} = V_{DD}-I_DR_D$.
*Reach for it* for every FET Q-point question — the four schemes are the spine of ·J p93–p96.
*The trap:* **the gate-bias equation depends on which branch the negative rail is in**, and the two
sources draw different circuits (see the concordance). ·J p93's own printed form makes $V_{GS}$
positive, which an N-channel JFET does not survive (JV7.7); ·J p96 prints the drain-feedback sign
negative, which cuts the MOSFET off (JV7.4). For an N-channel JFET, $V_{GS}$ must come out
**negative** — that is the check.

**22 · The E-MOSFET square law** — $I_D = K\left(V_{GS}-V_{GS(\text{th})}\right)^{2}$, with
$K = \dfrac{I_{D(\mathrm{ON})}}{\left(V_{GS(\mathrm{ON})}-V_{GS(\text{th})}\right)^{2}}$; tier 2
adds $g_m = 2K\left(V_{GS}-V_{GS(\text{th})}\right)$.
*Reach for it* for every enhancement-MOSFET question. Both tiers agree on it exactly.
*The trap:* an E-MOSFET has **no $I_{DSS}$** — it passes nothing at $V_{GS} = 0$, so Shockley's
equation does not apply to it. Below threshold $I_D = 0$ outright.

**23 · $g_m$, $r_d$, $\mu$ and the three FET gains — tier 2 only** —
$g_m = \dfrac{\delta I_D}{\delta V_{GS}}$, $g_{mo} = \dfrac{2I_{DSS}}{\lvert V_{GS(\text{off})}\rvert}$,
$g_m = g_{mo}\sqrt{\dfrac{I_D}{I_{DSS}}}$, $r_d = \dfrac{\delta V_{DS}}{\delta I_D}$,
$\mu = g_mr_d$; CS $A_v = -g_m(r_d\parallel R_L)$, CD $A_v \cong 1$,
CG $A_v = +g_m(r_d\parallel R_L)$ with $r_i = \dfrac{1}{g_m}$.
*Reach for it* before **any** FET gain calculation. **None of this is in the primary notes** — ·J
names "forward trans-conductance" once, in a purchase checklist, and never defines or uses it. Its
own configuration tables give only ratios such as $V_{DS}/V_{GS}$, which are definitions of gain,
not expressions for it: nothing in tier 1 lets you compute a number.
*The trap:* $g_m$ is a ratio of **increments**, not of totals — taking $I_D/V_{GS}$ was out by a
factor of four in ·L4's own Example 63.1 (V4.4). And only the **common-source** stage inverts.

## $h$-parameters, feedback and frequency response — tier 2 only

**24 · The $h$-parameter set** — definitions $h_i = \dfrac{V_i}{I_i}$ at $V_o = 0$ (Ω),
$h_r = \dfrac{V_i}{V_o}$ at $I_i = 0$ (dimensionless), $h_f = \dfrac{I_o}{I_i}$ at $V_o = 0$
(dimensionless), $h_o = \dfrac{I_o}{V_o}$ at $I_i = 0$ (S); the exact loaded set
$A_I = \dfrac{-h_f}{1+Z_Lh_o}$, $Z_i = h_i-\dfrac{h_fh_r}{Y_L+h_o}$, $A_V = \dfrac{A_IZ_L}{Z_i}$,
$Y_o = h_o-\dfrac{h_fh_r}{R_s+h_i}$; and the approximate block, valid when $h_{oe}R_L < 0.1$ —
CE: $-h_{fe}$, $h_{ie}$, $\dfrac{-h_{fe}R_L}{h_{ie}}$, $\infty$; CC: $1+h_{fe}$,
$h_{ie}+(1+h_{fe})R_L$, $1-\dfrac{h_{ie}}{R_i}$, $\dfrac{h_{ie}+R_s}{1+h_{fe}}$;
CB: $\dfrac{h_{fe}}{1+h_{fe}}$, $\dfrac{h_{ie}}{1+h_{fe}}$, $\dfrac{h_{fe}R_L}{h_{ie}}$, $\infty$.
*Reach for it* for any small-signal BJT amplifier question. **·J p61 names the $h$-symbols and
stops** — the model, the analysis and all three worked problems are tier 2 only.
*The trap:* $h_r$ is a **voltage** ratio (·L6 p4 prints $V_i/I_o$, V6.1). In the exact set,
$Y_L = 1/Z_L$ appears in $Z_i$ and $R_s$ — not $R_L$ — appears in $Y_o$. In the approximate set,
**CE and CB both give $R_o = \infty$; only CC is finite**, and CB's voltage gain is positive where
CE's is negative.

**25 · Feedback, decibels and the corner frequencies** — $A_f = \dfrac{A}{1\pm\beta A}$ (the $+$
sign is **negative** feedback), $A_f \cong \dfrac{1}{\beta}$ at high loop gain,
$D' = \dfrac{D}{1+\beta A}$, $R_i' = R_i(1+\beta A)$, $R_o' = \dfrac{R_o}{1+\beta A}$,
$f_1' = \dfrac{f_1}{1+\beta A}$, $f_2' = f_2(1+\beta A)$, $A\times BW$ constant;
$G_p = 10\log_{10}A_p$, $G_v = 20\log_{10}A_v$, $G = G_1+G_2+\cdots$;
$f_1 = \dfrac{1}{2\pi CR_{eq}}$, $C_{in} = C_{be}+(1+A_v)C_{bc}$,
$f_2 = \dfrac{1}{2\pi R_{eq}C_{in}}$, $f_\beta = \dfrac{f_T}{\beta}$, GBP $= f_T$.
*Reach for it* across the whole of ·L7 — every feedback result is $(1+\beta A)$ applied to a
different quantity. **None of this material exists in tier 1.**
*The trap:* the **plus** sign in the denominator is **negative** feedback, and $\beta$ here is the
**feedback fraction**, not the transistor's current gain — both meanings appear on ·L7 p11. Second
trap: an amplifier's lower cut-off is the **highest** of the individual capacitor corners and its
upper cut-off the **lowest** of the candidate high-frequency limits (·L7 p24 has this backwards,
V7.17).

---

# Dimensional sanity checks

Nine one-line tests. Between them they catch most of the recurring errors in this unit — and they
caught a large fraction of the flags recorded in `_verification-log.md`, in **both** tiers.

**1 · The four $h$-parameter units.**

$$h_i\ [\Omega] \qquad h_r\ [\text{dimensionless}] \qquad h_f\ [\text{dimensionless}] \qquad h_o\ [\mathrm{S}]$$

Read down the defining equation $V_i = h_iI_i + h_rV_o$: the first term is Ω × A and the second must
also be a volt, so $h_r$ carries no units. Likewise in $I_o = h_fI_i + h_oV_o$ the second term must
be an ampere, so $h_o$ is in siemens. An $h_r$ that comes out in ohms means a current was written
where a voltage belongs (V6.1); an $h_o$ multiplying a current gives $\mathrm{A^2/V}$, which cannot
be added to an ampere (V6.2). The determinant $\Delta h = h_ih_o - h_fh_r$ is dimensionless because
$\Omega\times\mathrm{S} = 1$.

**The same test works on the primary notes.** ·J p60–p61 equates an output *resistance* to
$h_{OB}$; but $h_{OB} = I_C/V_{CB}$ is in **siemens**, so the resistance is $1/h_{OB}$ (JV6.2). The
same reading confirms ·J p62's $h_{OE} = I_C/V_{CE} = 1/r_o$ as correctly formed.

**2 · $\alpha < 1 < \beta$.**

$$\alpha = \frac{I_C}{I_E} < 1 \qquad\qquad \beta = \frac{I_C}{I_B} \gg 1 \qquad\qquad \theta = 1+\beta > \beta$$

$\alpha$ is a fraction of the emitter current, so it is always just under unity — 0.95 to 0.99 in
practice. $\beta$ is collector over base, so it is tens to hundreds. An $\alpha$ above 1, or a
$\beta$ below 1, means the ratio has been inverted (V3.1 — and ·J p60 prints it the right way up,
which is how that flag was confirmed). Cross-check with $\beta = \alpha/(1-\alpha)$: $\alpha = 0.99$
must give $\beta = 99$, not 1.09 (V3.3). The same magnitude test catches JV6.5, where a chain
opening $\theta = I_E/I_C$ would give about 1.02 against its own stated answer of $1+\beta \approx 51$.

**3 · $g_m$ is in siemens, $K$ is in A V$^{-2}$.**

$$g_m = \frac{\delta I_D}{\delta V_{GS}}\ \left[\mathrm{A/V} = \mathrm{S}\right] \qquad \mu = g_m r_d\ \left[\mathrm{S}\times\Omega = 1\right] \qquad K\left(V_{GS}-V_{GS(\text{th})}\right)^{2}\ \left[\mathrm{A\,V^{-2}}\times\mathrm{V^{2}} = \mathrm{A}\right]$$

$g_m$ is a ratio of **increments**, not of totals: a printed $I_D/V_{GS}$ is the wrong quantity
(V4.4). The product $g_mr_d$ must come out dimensionless, which is what makes it a valid
amplification factor. The E-MOSFET constant $K$ is quoted in mA/V², and the square law only returns
an ampere because of it. The same check works on $r_j = \eta V_T/I_F$: mV/mA is ohms.

**4 · Ripple factor and efficiency are dimensionless.**

$$\eta_{\text{HW}} = \frac{4}{\pi^{2}} = 0.405 \qquad\qquad \eta_{\text{FW}} = \frac{8}{\pi^{2}} = 0.811 \qquad\qquad \gamma = \frac{\text{ac rms}}{\text{dc}}$$

Both are ratios of like quantities, so neither can carry volts, amps or watts. Two consequences
worth using: **$\eta_{\text{FW}}$ is exactly twice $\eta_{\text{HW}}$**, and $\gamma$ must be
divided by the **dc** value — dividing by the total rms would cap it at 1 and make the half-wave
answer of 1.21 impossible (V2.5, V2.6). An efficiency above 100 % or a negative ripple factor means
a step was inverted.

This is exactly the test that catches JV5.1 and JV5.3, where the primary notes put the exponent on
the wrong bracket: the printed denominator is $\mathrm{A}\cdot\Omega^{2}$ against a numerator of
$\mathrm{A}^{2}\Omega$, so the ratio is not dimensionless, and only the corrected form collapses to
the $4/\pi^2$ and $8/\pi^2$ the very next lines state.

**5 · Gain is dimensionless.**

$$A_V = \frac{V_o}{V_i} \qquad A_I = \frac{I_o}{I_i} \qquad A_P = A_VA_I \qquad \text{all dimensionless}$$

A "gain" that carries ohms is wrong. This is the check that catches the printed common-drain gain
on ·L4 p13, whose numerator was $\Omega^2$ over a denominator of $\Omega$ (V4.11), and it settles
$A_V = A_IZ_L/Z_i$ — the ohms cancel between $Z_L$ and $Z_i$. Stability factor $S$ and beta
sensitivity $K_\beta$ are dimensionless for the same reason, which is why an "approximation" to $S$
with units of current cannot stand (V3.16). The same test applied to a **power** ratio catches
JV6.3: a CE input power written $I_EV_{BE}$ overstates the input, and so understates the gain, by a
factor of $1+\beta$.

**6 · The exponent must be dimensionless.**

$$\frac{V}{\eta V_T} \quad\text{— volts over volts} \qquad\qquad \frac{e}{k} = 11{,}600\ \mathrm{K\,V^{-1}}$$

Everything above the line in $e^{\,V/\eta V_T}$ has to cancel. **The primary notes print one that
does not:** ·J p35 typesets the diode law as

$$i_o = I_o\left(\frac{V_D}{e^{\eta V_T}} - 1\right) \quad\text{✗ (JV4.3)}$$

whose exponent $\eta V_T$ is a **voltage**, not a pure number — and which has moved the whole
$V_D$ dependence out of the exponential into a linear numerator, destroying the exponential
behaviour the rest of the page describes. The corrected form is

$$i_D = I_o\left(e^{\,V_D/\eta V_T} - 1\right) \quad\text{✓}$$

The same check shows the $-1$ belongs **outside** the bracket, since $e^{40V-1}$ subtracts a pure
number from a voltage coefficient (V1.3), and it confirms that 40 and 20 carry units of
$\mathrm{V^{-1}}$. And a $k$ of $1.38\times10^{-28}$ (JV4.2) would put $V_T$ at 0.26 µV, making the
exponent $10^{5}$ times too large.

**7 · Self-reference: if the symbol left of the equals sign also appears on the right, the label
is wrong.**

$$I_{CEO} = \frac{I_C}{1-\alpha} \quad\text{✗} \qquad\qquad I_{CEO} = \frac{I_{CO}}{1-\alpha} \quad\text{✓}$$

This single test caught V2.5 ($\gamma = I_{L(ac)}/I_{L(ac)}$), V3.5, V3.20 ($S$ with $R_B/\beta R_B$
in the denominator, deleting $R_E$ entirely), V6.2 ($i_c$ on both sides of the CE output equation),
V7.19 ($A_v = (R_C\parallel R_L)/R_L$), JV6.5 ($\theta = I_E/I_C$ opening a chain that cancels to
$I_E/I_B$) and JV6.7 (an $I_{CEO}$ that carries a second $1/(1-\alpha)$ already inside it). Run it
on every result before using it.

**8 · A divider ratio lies strictly between 0 and 1.**

$$\frac{R_2}{R_1+R_2} \in (0,1) \qquad\qquad \frac{R}{R_S+R} \in (0,1)$$

Every voltage-divider output must be **smaller than its input**. This catches JV4.5, where the
primary notes print $V_{Th} = V_SR/(R_L+R)$ — a denominator built from a resistor that carries no
current at that step — and it catches JV3.6 and JV3.7, a dropped and an added zero in consecutive
lines of the same transformer example, one of which returns a secondary voltage ten times the
source emf. The related check on JV2.5: the printed polar impedance
$(R+jX)/\sqrt{R^{2}+X^{2}}$ has modulus exactly 1 for every $R$ and $X$, and is dimensionless where
an impedance must be in ohms.

**9 · Sign conventions hold for a whole answer.**

$$\text{N-channel JFET: } V_{GS} \le 0 \qquad V_{GS(\text{off})} < 0 \qquad\qquad \text{N-channel E-MOSFET: } V_{GS} > V_{GS(\text{th})} > 0$$

A depletion-mode N-channel device is biased **negative** at the gate; an enhancement-only device is
biased **positive**, above threshold. Any bias equation that returns the wrong sign has an error in
it, whatever the arithmetic says. This is the check on JV7.7 (a printed gate-bias form that makes
$V_{GS}$ positive on a JFET, forward-biasing a gate the device does not survive) and on JV7.4 (a
printed $V_{GS} = -V_{DS}$ that would cut an E-MOSFET off entirely, so the circuit could not work
at all). Decide the convention at the top of the answer and hold it to the end.

---

# Where the flags live

Every ⚠ in this file points into `_verification-log.md`, which records for each ID what the page
prints verbatim, what it should be, and why.

- **Tier 1 (·J):** substantive **JV{file}.{n}**, cosmetic **JC{file}.{n}**, where *file* is the
  topic-file number 1–7.
- **Tier 2 (·L):** substantive **V{lesson}.{n}**, cosmetic **C{lesson}.{n}**. Flag counts by
  lesson: L1 — 6 substantive, 11 cosmetic; L2 — 18 and 25; L3 — 22 and 30; L4 — 15 and 21; L5 — 9
  and 12; L6 — 4 and 8; L7 — 22 and 26.

The two namespaces cannot collide, which is why a row can carry a flag from either tier without
ambiguity.

**Related files.** `_nomenclature.md` for symbols, units and the clash table. The tier-1 topic
files `01-matter-atoms-and-semiconductors.md` through `07-field-effect-transistors.md`, and the
tier-2 files `11-diodes.md` through `17-multistage-feedback-frequency-response.md`, for the
derivations, worked examples and figures behind every equation here. `00-index.md` maps the two
tiers onto each other topic by topic.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
