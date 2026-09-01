---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
file_role: nomenclature
tiers: "1 — the course's own lecture notes, 100 pp., cited ·J p{page}, topic files 01-07. 2 — seven lesson documents, 169 pp., cited ·L1 p7 … ·L7 p27, topic files 11-17. 3 — four reference slide decks, 59 pp., cited ·RD2 p14, unverified."
source: "Extracted from the seven tier-1 topic files, the seven tier-2 topic files and the reference-deck page map. Every entry traces to a symbols table, a defined equation or a flagged notation clash in one of those files."
coverage: "Tier 1 (·J p2-p100) and tier 2 (·L1-·L7) complete. Reference-tier symbols are listed separately in section 7 and are unverified."
tags: [nomenclature, symbols, units, clashes, cross-tier-translation, subscript-conventions, glyph-hazards, aliases]
---

<!-- BEE 3103 Analogue Electronics I knowledge base. -->

# Nomenclature — BEE 3103

Every symbol used across the knowledge base, its meaning, its SI unit and the practical unit the
notes actually write, which files it belongs to, and — the section this file exists for — **where
one symbol carries two meanings, or one quantity carries two symbols**.

**This subject is the worst in the year for notation collisions, and it now has two independent
sources of them.** The course's own lecture notes (tier 1) and the seven lesson documents (tier 2)
were written to different conventions, and neither was written to sit beside the other. The clash
table comes first for that reason. Read it before the symbol list, and before any calculation that
moves between a `·J` file and an `·L` file.

## Provenance and file map

Citations are the topic files' own.

- **·J p47** — PDF page 47 of the 100-page primary lecture notes (**tier 1**). The document's own
  printed page number runs one behind the PDF page.
- **·L3 p14** — PDF page 14 of Lesson 3 (**tier 2**).
- **·RD2 p14** — page 14 of reference deck 2 (**tier 3**, unverified).

Anything marked **[added]** is supplied by this knowledge base and is not in the lecturer's
material. The "Where" columns below name **topic files**, using this map.

| Tier | Topic file | Source | Range |
|---|---|---|---|
| **1** | `01-matter-atoms-and-semiconductors.md` | ·J | p2–p9 |
| **1** | `02-resistors-and-dc-network-theorems.md` | ·J | p10–p23 |
| **1** | `03-capacitors-inductors-and-transformers.md` | ·J | p24–p32 |
| **1** | `04-diodes.md` | ·J | p33–p45 |
| **1** | `05-rectifiers-filters-and-regulation.md` | ·J | p46–p56 |
| **1** | `06-bipolar-junction-transistors.md` | ·J | p57–p83 |
| **1** | `07-field-effect-transistors.md` | ·J | p84–p100 |
| 2 | `11-diodes.md` | ·L1 | p1–p18 |
| 2 | `12-rectifiers.md` | ·L2 | p1–p26 |
| 2 | `13-bipolar-junction-transistor.md` | ·L3 | p1–p25 |
| 2 | `14-field-effect-transistors.md` | ·L4 | p1–p24 |
| 2 | `15-fabrication-and-integrated-circuits.md` | ·L5 | p1–p23 |
| 2 | `16-h-parameters-and-bjt-amplifiers.md` | ·L6 | p1–p26 |
| 2 | `17-multistage-feedback-frequency-response.md` | ·L7 | p1–p27 |

In the clash table, **T1** marks a usage from the primary lecture notes and **T2** one from the
lesson documents.

---

# 1 · ⚠ The clash table — read this first

Ranked by how much a mix-up costs. The last column is the one to use: it is the *tell*, the thing
visible on the page that settles which meaning is in play.

| # | Symbol | Meaning A | Meaning B (and C) | How to tell which is meant |
|---|---|---|---|---|
| **1** | turns ratio $n$ / $a$ / $K$ | **T1** $n = N_p/N_s$ — **primary over secondary** ·J p32. So a **step-up** transformer has $n < 1$ | **T2** $a = N_1/N_2$ ·L7 p17, p19 — **the same convention, different letter** · **T2** $K = N_2/N_1$ ·L2 p6 — **the reciprocal** | ⚠ **This one inverts answers.** Three definitions, two of them inverses. Never substitute a quoted "10 : 1" without checking which way up the formula wants it. **Anchor on ·J p32's own example:** $N_P = 400$, $N_S = 2000$ ⇒ $n = 0.2$, but $K$ for the same transformer is $5$. Sanity check by physics, not by letter — a step-up transformer must raise voltage and lower current |
| **2** | $V_P$ | **positive** pinch-off voltage, a tick on the $V_{DS}$ axis between the ohmic and saturation regions — **T1** ·J p85, p86 · **T2** ·L4 p4, p5, p7, p15 | **negative** — equated to $V_{GS(\mathrm{off})}$ inside Shockley's equation — **T1** ·J p87 · **T2** ·L4 p6–p8, p11, p15. Separately $V_p$ = **peak value** of a waveform **T1** ·J p2; $V_p$ = transformer **primary** voltage **T1** ·J p29–p32; $V_P$ = tunnel-diode **peak-point** voltage **T2** ·L2 §2.16 | ⚠ **JV7.1 / V4.2 — the same inherited defect in both tiers; nothing on either page resolves it.** Working rule: **in Shockley's equation the denominator is $V_{GS(\mathrm{off})}$, negative for N-channel.** On a drain characteristic $V_P$ is a positive value of $V_{DS}$. The two are equal in **magnitude** only. Self-check: with $\lvert V_P\rvert = 4\ \mathrm V$ and $V_{GS} = -1\ \mathrm V$, the right sign gives $I_D = 0.5625\,I_{DSS}$; the wrong one gives $1.5625\,I_{DSS}$, which exceeds $I_{DSS}$ and is impossible. ·J never puts a number to $V_P$; ·L4 does, in three worked examples |
| **3** | $\beta$ | **feedback fraction** — the portion of output returned to the input, dimensionless, $0.001$–$0.2$ — **T2** ·L7 p2 onwards | **BJT common-emitter current gain** $I_C/I_B$, dimensionless, $50$–$500$ — **T1** ·J p61–p63, p70–p83 · **T2** ·L3 p5, ·L6, and inside ·L7 itself at p11, p13, p18, p24, p25 | Inside $(1\pm\beta A)$, or equal to a **resistor ratio** ($R_1/(R_1+R_2)$, $R_E/R_C$, $R_C/R_F$) ⇒ feedback fraction. Multiplying $I_B$, sitting beside a transistor symbol, or forming $\beta R_E$ or $\beta r_e$ ⇒ current gain. **Numerical tell:** feedback fractions are far below 1; transistor $\beta$ is in the tens or hundreds. **The primary notes never use the feedback meaning at all** — in tier 1, $\beta$ is always the current gain |
| **4** | $\theta$ · $\gamma$ | **T1** ·J p62, p63 — the **common-collector forward current gain**, $\theta = I_E/I_B = \gamma = h_{FC} = 1+\beta$, dimensionless, 51–501 | **T1** ·J p47–p49 — $\theta$ is the **integration angle** $\omega t$ in the rectifier derivations, $i = I_m\sin\theta$ · **T1** ·J p48, p49 and **T2** ·L2 §2.6 — $\gamma$ is the **ripple factor**, 1.21 (HW), 0.48 (FW) | ⚠ **Read this row before opening the BJT file.** $\theta$ for $1+\beta$ is **unique to the primary notes** — no tier-2 file uses it, and a reader meeting $\theta$ in a CAT has nothing else to go on. Tell: dividing $I_E$ by $I_B$, or equal to $\beta/\alpha$ ⇒ CC current gain, a number in the tens or hundreds. Inside $\sin\theta$ or $\mathrm d\theta$ ⇒ an angle. Equal to $I_{ac}/I_{dc}$, or valued 1.21 or 0.48 ⇒ ripple factor |
| **5** | $R_C$ vs $R_L$ | **T1** ·J p70–p83 — $R_C$ is the **collector resistor**; $R_L$ is the **external load** hung on the output through the coupling capacitor. Two different components in one circuit | **T2** ·L3 — $R_L$ **is** the collector resistor (its circuits carry no external load); ·L4 uses $R_L$ for the **drain** resistor · **T2** ·L6, ·L7 — $R_L$ is the external load and $R_C$ the collector resistor, as in T1 | **The translation rule: reading a ·L3 or ·L4 formula against a ·J circuit, read their $R_L$ as ·J's $R_C$ (or $R_D$).** ·J p83 Problem 1 states **both** $R_L = 10\ \mathrm{k\Omega}$ and $R_C = 3.3\ \mathrm{k\Omega}$ for one circuit, and $R_{ac} = R_CR_L/(R_C+R_L)$ needs them apart. Tell: a resistor from the collector to the supply rail ⇒ $R_C$; a resistor beyond a coupling capacitor ⇒ the load. ⚠ **V7.18** turns on exactly this |
| **6** | $V_T$ | **thermal voltage** $kT/q$ — $26\ \mathrm{mV}$ at $300\ \mathrm K$ — **T1** ·J p35 · **T2** ·L1 p3, p6 ($25\ \mathrm{mV}$ at $293\ \mathrm K$) | **B:** terminal voltage of a **tunnel diode**, $0$–$1\ \mathrm V$ — **T2** ·L2 §2.16 · **C:** **threshold voltage** of an NMOS transistor — **T2** ·L5 p21 | Millivolt-scale and inside an exponential ⇒ thermal voltage. Plotted against $i_T$ on a peak-and-valley characteristic ⇒ tunnel diode. In an IC-fabrication or channel-stop context ⇒ threshold. **·J p90 and ·L4 avoid the problem entirely** by writing the threshold as $V_{GS(\mathrm{th})}$ — prefer that form in your own work |
| **7** | $\eta$ | **T1** ·J p35 · **T2** ·L1 p6 — diode **ideality (emission) factor**, 1 for Ge, 2 for Si, dimensionless | **T1** ·J p47, p49 · **T2** ·L2 §2.6 — **rectification efficiency** $P_{dc}/P_{ac}$, $40.5\%$ half-wave, $81.1\%$ full-wave · **T1** ·J p32 — **transformer efficiency** $P_s/P_p$, $90\%$ in the worked example | **Three meanings inside one document.** Inside an exponent ⇒ ideality factor. A percentage in a rectifier calculation ⇒ rectification efficiency. A percentage beside a transformer's turns ⇒ transformer efficiency. ⚠ **C2.5** — ·L2 prints the efficiency symbol as a roman **h** on p4 and p8, which hides the clash rather than resolving it |
| **8** | $V_{SS}$ · SS | **T1** ·J p94 · **T2** ·L4 p9 — the **negative source-bias supply**, quoted as a magnitude with the rail drawn $-V_{SS}$, in $V_{GS} = V_{SS} - I_SR_S$ | **T1** ·J p88, p90 · **T2** ·L4 §4.19 — **SS** is the MOSFET **substrate** terminal, the fourth lead · **T1** ·J p99 — the **supply rail label on the common-drain sketch**, where $V_{DD}$ is meant | ⚠ **JC7.9 — three meanings for the same letters inside seventeen pages.** On a device outline as a fourth lead returned to the source ⇒ substrate. In a bias equation beside $R_S$ ⇒ the negative source supply. At the top of a source-follower sketch ⇒ a mislabel; read it as $V_{DD}$, since an N-channel follower runs from the positive drain supply |
| **9** | $h_{OB}$, $h_{OE}$ | **T1** ·J p60, p61 print *"output resistance $= V_{CB}/I_C = h_{OB}$"* — treating $h_o$ as a **resistance**, in ohms | **T1** ·J p62 prints $h_{OE} = I_C/V_{CE} = 1/r_o$ — correctly an **admittance** · **T2** ·L6 p3–p8 — $h_o = h_{22}$, output admittance, µA/V throughout | ⚠ **JV6.2 — the two cannot both be right.** **$h_o$ is always an admittance, siemens, in every configuration.** The resistance is its reciprocal: $r_o = 1/h_{OE}$, $\ \text{CB output resistance} = 1/h_{OB}$. Dimensional check: in $I_o = h_fI_i + h_oV_o$ every term must come out in amperes, so $h_o$ must be $\mathrm{A/V}$ |
| **10** | $V_S$, $V_s$ | **supply or source emf** — **T1** ·J p16 (source emf of a practical voltage source), ·J p36, p39 (diode-circuit supply), ·J p51 (the voltage a capacitor charges towards), ·J p55 (unregulated supply to a zener regulator) | **secondary or source-node** — **T1** ·J p29–p32 transformer **secondary** voltage, ·J p93–p95 the FET **source node potential** to ground · **T2** ·L2 §2.4 rms secondary voltage; ·L6 §6.7, ·L7 signal-source open-circuit voltage | Flagged twice by the primary files themselves — `03` §3.20 (*"source voltage in §3.5–§3.6, secondary voltage from §3.16 onward, six pages apart"*) and `05` §5.21 (*"a filter time-constant voltage in §5.15, the supply from here on, one page apart"*). Tell: a transformer in the figure ⇒ secondary. A FET source lead ⇒ node potential. A battery symbol feeding a network ⇒ supply |
| **11** | $i_o$ vs $I_o$ | **T1** ·J p35 — $i_o$ is the **diode current** | **T1** ·J p35 — $I_o$ is the **saturation current** | ⚠ **JC4.1 — the same letter in two cases, on the two sides of one equation.** $i_o = I_o(e^{V_D/\eta V_T}-1)$. Tell by magnitude alone: milliamperes ⇒ the diode current; nanoamperes (Si) or microamperes (Ge) ⇒ saturation. Everywhere else in the same file the diode current is $i_D$ or $I_D$ — prefer that form in your own working |
| **12** | $V_R$ vs $V_{Rx}$ | **reverse voltage** across a diode, volts — **T1** ·J p34, p44 · **T2** ·L1 p7 (varactor law $C = K/\sqrt{V_R}$) | **T1** ·J p13, p16, p55, p94 — $V_{R1}$, $V_{RL}$, $V_{R_2}$ mean *the voltage **across** resistor $R_1$ / $R_L$ / $R_2$* · **T2** ·L2 §2.7.7 — $V_R$ = **voltage regulation** $R_0/R_L$, **dimensionless** | A second subscript naming a resistor ⇒ the voltage across that resistor, and the primary notes use this form constantly. A bare $V_R$ on a reverse-bias axis ⇒ reverse voltage. A bare ratio or a percentage such as "2.5 %" ⇒ regulation |
| **13** | $k$ / $K$ | $k$ = **Boltzmann constant**, $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ — **T1** ·J p35 · **T2** ·L1 p3, p6 | $K$ = **dielectric constant** ($=\varepsilon_r$) **T1** ·J p27 · $K$ = **E-MOSFET square-law constant**, mA V⁻² **T1** ·J p91, p92 and **T2** ·L4 §4.19 · **K** = the **BS 1852 kilohm marker** ("5K8", "4K54") **T1** ·J p11, p13 · $K$ = **kilohm** suffix ("30 K", "5 K") **T2** ·L1 p13, ·L3 p14, ·L7 p13 · $k$ = **cathode** lead **T2** ·L1 p15 · $k$ = **inductance constant**, $L = kN^2$ **T2** ·L7 p19 · $K$ = **kelvin** · $K$ = turns ratio $N_2/N_1$ **T2** ·L2 p6 · $K$ = **varactor constant** **T2** ·L1 p7 | Read the neighbours, not the letter. A digit in front of it inside a resistance ⇒ kilohm. A temperature in front of it ⇒ kelvin. $N^2$ beside it ⇒ inductance constant. A capacitance on the left ⇒ dielectric or varactor constant. $(V_{GS}-V_{GS(\mathrm{th})})^2$ beside it ⇒ E-MOSFET constant. ⚠ **JC7.3** — ·J p91 sets the E-MOSFET constant as capital $K$ in the equation and lower-case k in the sentence below it. ⚠ **C5.9** — ·L5 p9 prints "180 KV" for $180\ \mathrm{kV}$ |
| **14** | $Q$ | **electric charge**, coulombs, $Q = It$ — **T1** ·J p9, p10, p26 | **T1** ·J p27 — the **quality factor** of a capacitor, dimensionless · **T2** — the **quiescent operating point** $(V_{CE},I_C)$ or $(V_{DS},I_D)$ ·L3 §3.18, ·L4 §4.10, and $Q_1$, $Q_2$ = **transistor designators** ·L7 | ⚠ The first two sit **two pages apart** in one document, the second one four lines after a charge equation. Coulombs, or multiplying a current by a time ⇒ charge. Beside a dielectric's temperature stability ⇒ quality factor. Hyphenated "Q-point", or as a subscript ($I_{CQ}$, $V_{DSQ}$) ⇒ operating point |
| **15** | $H$ | the **henry**, unit of inductance — **T1** ·J p29 (*"measured in henries (H)"*) | the **magnetic field strength**, A m⁻¹ — **T1** ·J p29, in the permeability sentence | ⚠ **Four lines apart on one page.** Read $H$ from its position: **a unit after a number** ⇒ henry; **a field quantity inside prose or a formula** ⇒ magnetic field strength. Nothing else in either tier uses the letter |
| **16** | $\alpha$ | **common-base current gain** $I_C/I_E$, $0.95$–$0.99$ — **T1** ·J p60, p63 · **T2** ·L3, ·L6 | **T1** ·J p10 — the **proportionality sign ∝ typed as a Greek α**: the page reads *"R α L"*, *"R α ρ"* (⚠ **JC2.5**) · **T3** ·RD2 p14 — temperature coefficient of resistance, $0.0038\ \mathrm{^\circ C^{-1}}$ | Standing **between two quantities with no equals sign** ⇒ it is $\propto$, not a gain. A pure number just below 1 ⇒ current gain. A value near $0.004\ \mathrm{^\circ C^{-1}}$ ⇒ temperature coefficient, and that meaning is reference-tier only |
| **17** | $V_o$ | **T1** ·J p34, p38 — the **barrier (junction) potential**, also the turn-on voltage: $0.2$–$0.3\ \mathrm V$ (Ge), $0.6$–$0.7\ \mathrm V$ (Si) | **T1** ·J p75 — the **output signal** of the CE amplifier · **T2** ·L2 §2.13 clipper output; ·L6 §6.1 two-port output voltage; ·L7 §7.4 $V_o'$ output with feedback | A tenth-of-a-volt value inside a diode branch ⇒ barrier potential. A node at the far side of a coupling capacitor ⇒ output voltage. **Tier 2 calls the barrier potential $V_B$** ·L1 p3, ·L2 p3 — see the translation table |
| **18** | $N$ / $n$ / $m$ | **T1** ·J p5 — $N$ = the number of electrons a shell can hold, $N = 2n^2$; $n$ = the **shell number**; $m$ = the **sub-shell number** | **T1** ·J p29–p32 — $N$, $N_p$, $N_s$ = transformer **turns**; $n$ = the **transformation ratio** · **T1** ·J p11 — $m$ = the colour-code **multiplier exponent** · **T1** ·J p15 — $n$ = the number of identical resistors in a power-rating build · **T2** ·L7 §7.9 $n$ = number of cascaded stages; ·L5 $n$ = number of squares; ·L1 $n_i$, $N_a$, $N_d$ = carrier and doping densities · **T1** ·J p3 — **N** = nitrogen, and N-type doping throughout | ⚠ **JC1.4** — ·J p6 prints "N = 3" for the **shell number**, where ·J p5 makes $N$ the electron count and $n$ the shell number. Same page-pair, two meanings, and the letter that should be the answer used for the input. Elsewhere: subscript i, a or d ⇒ a carrier or doping density; beside a transformer ⇒ turns; a power of ten beside it ⇒ the colour-code multiplier |
| **19** | $P$ | **power** — $P_{dc}$, $P_{ac}$, $P_L$, $P_Z$, $P_{\max}$, $P_p$, $P_s$ — **T1** ·J p10, p32, p47, p55 · **T2** ·L1, ·L2, ·L3 | **T1** ·J p3, p6, p8, p9 — **P** = phosphorus (element 15, structure 2:8:5, the pentavalent dopant), and **P-type** doping · **T1** ·J p29–p32 — subscript $p$ = **primary** ($N_p$, $V_p$, $I_p$, $P_p$) · **T2** ·L2 §2.16 — subscript P = the tunnel diode's **peak point** ($I_P$, $V_P$) | A wattage value ⇒ power. An italic type label or a chemical formula ⇒ the element or the doping type. A subscript p beside a transformer ⇒ primary. Note that $P_p$ means *primary power* — the letter is doing both jobs in one symbol |
| **20** | $S$ | **stability factor** $\mathrm dI_C/\mathrm dI_{CO}$, 1 (CB) to $1+\beta$ (base bias) — **T1** ·J p81–p83 · **T2** ·L3 p16 | **T1** ·J p84 — **S** = the FET **source** terminal · **T1** ·J p88 — **SS** = substrate · **T1** ·J p3, p6 — **S** = sulphur ($Z = 16$) · **T1** ·J p29–p32 — subscript $s$ = **secondary** · **T2** ·L7 §7.4 — **sacrifice factor** $A/A' = 1+\beta A$ · the **siemens**, unit of $g_m$ and $h_o$ | A derivative of $I_C$, or a value between 1 and $1+\beta$ ⇒ stability factor. A ratio of two gains ⇒ sacrifice factor. Upright S on a device pin ⇒ source. Doubled, SS ⇒ substrate. Following a number ⇒ siemens. In a shell-structure line ⇒ sulphur |
| **21** | $C$ | **capacitance**, farads — **T1** ·J p24–p28, p51 · **T2** ·L1, ·L2, ·L4, ·L7 | **T1** ·J p57 — **C** = the **collector** terminal of a BJT · **T1** ·J p3, p6 — **C** = carbon (the atomic-weight reference, "carbon = 12") · the **coulomb**, unit of $Q$ | A value in µF or pF ⇒ capacitance. On a device pin between B and E ⇒ collector. After a charge value ⇒ the coulomb. In a shell-structure or atomic-weight line ⇒ carbon. $C_1$, $C_2$, $C_3$ on ·J p75 are the input coupling, output coupling and emitter bypass capacitors in that order |
| **22** | $B$ | **T1** ·J p57 — the **base** terminal of a BJT | **T1** ·J p3, p6 — **B** = boron ($Z = 5$, structure 2:3, the trivalent dopant) · **T1** ·J p18 — **A, B** = the two terminals a load is removed from in a Thevenin or Norton reduction | On a device pin ⇒ base. In a shell-structure line, or beside "trivalent" ⇒ boron. Paired with A on a pair of open terminals in a network figure ⇒ a node label, not a quantity at all |
| **23** | $I_S$, $I_s$ | **T1** ·J p84 — the FET **source current**, $I_S \cong I_D$ since $I_G \cong 0$ | **T1** ·J p30–p32 — transformer **secondary current** · **T1** ·J p64 · **T2** ·L1 §1.4 — the diode **reverse saturation current** · **T2** ·L6 §6.13 — the signal-source current in $A_{IS} = -I_2/I_s$ | **Case is not a guide** — both tiers write $I_S$ and $I_s$ interchangeably. A FET source lead ⇒ source current. A transformer ⇒ secondary current. Nanoamperes or picoamperes, opposite a diode ⇒ saturation current. A Norton signal source ⇒ source current |
| **24** | $\mu$ | **permeability** of a core or medium, H m⁻¹, $\mu_0 = 4\pi\times10^{-7}$ — **T1** ·J p29 | the SI prefix **micro** — µF, µA, µS, µm — used constantly in the same document · **T2** ·L4 p8 — the FET **amplification factor** $\mu = g_mr_d$, 100–300 · **T2** ·L5 §5.2 — $\mu_n$, $\mu_p$ carrier **mobilities** **[added]** | A unit immediately after it ⇒ prefix. $N^2$, $A$ or $l$ beside it ⇒ permeability. Standing alone, or equal to $g_mr_d$ ⇒ amplification factor. A subscript n or p ⇒ mobility. ⚠ See the glyph table: **µ set as m** is the commonest unit slip in the primary notes, and it is always a factor of $10^3$ |
| **25** | $E$ | **T1** ·J p57 — the **emitter** terminal of a BJT | **T1** ·J p27 — **energy stored** in a capacitor, joules · **T1** ·J p43 — **incident light intensity** on a photodiode, mW cm⁻² · **T1** ·J p5 — $E_i$, $E_f$ = initial and final energy levels in $hf = E_i - E_f$ · **T1** ·J p7 — $E_g$ = the band gap, eV · **T2** ·L1 p11 — $E_{in}$, $E_o$ = zener regulator input and output voltages | On a device pin ⇒ emitter. In joules, beside $\tfrac12CV^2$ ⇒ stored energy. Subscript g ⇒ band gap. Subscript i or f beside $hf$ ⇒ an energy level. **Subscript "in" or "o" in a zener circuit ⇒ a voltage, not an energy** — that usage is tier 2's alone |
| **26** | $D$ / $d$ | **T1** ·J p33–p45 · **T2** ·L2 — **D**, $D_1 \ldots D_4$ = **diode** designators in rectifier, clipper and multiplier circuits | **T1** ·J p84 · **T2** ·L4 p2 — **D** = the FET **drain** terminal · **T1** ·J p24 — $d$ = plate **separation** of a capacitor; ·J p44 — $d$ = depletion-layer width as the varactor's plate separation · **T1** ·J p11 — $d_1$, $d_2$ = the colour code's two significant **digits** · **T2** ·L7 §7.8 — $D$, $D'$ = **distortion** · **T2** ·L5 §5.16 — $d$ = depth of a diffused region | Numerically subscripted in a circuit diagram ⇒ a diode. On a device pin ⇒ drain. In metres, under an $\varepsilon A$ ⇒ a plate separation. Primed and divided by $(1+\beta A)$ ⇒ distortion |
| **27** | $A$ / $a$ | **area** — conductor cross-section in $R = \rho L/A$ **T1** ·J p10; capacitor plate area **T1** ·J p24; varactor junction area **T1** ·J p44 · **T2** ·L5 §5.16 $a = wd$ | **gain** — $A_p$, $A_v$, $A_i$ **T1** ·J p61, p98–p100 · **T2** $A_V$, $A_I$, $A_P$ ·L6, $A$ = open-loop gain ·L7 §7.4 · **T1** ·J p18 — **A** = a Thevenin terminal label · **T2** ·L7 p19 — $a$ = turns ratio $N_1/N_2$ | Square metres or square centimetres ⇒ an area. A subscript v, i or p ⇒ a gain. Paired with B on open terminals ⇒ a node label. ⚠ Note the reciprocal trap in row 1: ·L7's $a = N_1/N_2$ and ·L2's $K = N_2/N_1$ are inverses |
| **28** | $R_0$ · $R_N$ · $R$ | **T2** ·L2 p3 — $R_0 = R_S + r_d$, the total series resistance outside the load (half-wave and centre-tapped); $R_0 = R_S + 2r_d$ for the **bridge** ·L2 p12 | **T1** ·J p19, p20 — $R_N$ = the **Norton resistance**, $= R_{Th}$ · **T2** ·L2 §2.16 — $-R_N$ = the tunnel diode's **negative resistance**, $-10$ to $-200\ \Omega$ · **T1** — $R$ alone is the zener **dropping resistor** ·J p55, the **shunt** resistor of the diode Thevenin network ·J p36, and the **filter** time-constant resistance ·J p51 | For $R_0$, count the conducting diodes: one ⇒ $R_S+r_d$, two ⇒ $R_S+2r_d$. For $R_N$: a **positive** value equal to $R_{Th}$ ⇒ Norton; a **negative** value on a peak-and-valley characteristic ⇒ the tunnel diode. For bare $R$, read the circuit — the primary notes reuse the plain letter in three unrelated roles across six pages |
| **29** | $R_S$, $R_s$ | **T1** ·J p36 — the **source-side series resistance** of a diode network · **T2** ·L2 p3 — transformer **secondary resistance**; ·L2 §2.16 — tunnel-diode **series ohmic resistance**, 1–5 Ω | **T1** ·J p93 · **T2** ·L4 §4.9 — the FET **source bias resistor**, $0.5$–$3\ \mathrm{k\Omega}$ · **T2** ·L6 §6.7 — the **signal-source internal resistance** · **T2** ·L5 §5.16 — **sheet resistance**, Ω per square **[added]** | Case is not a reliable guide. A transformer in the figure ⇒ secondary resistance. A FET source lead ⇒ source resistor. A signal generator symbol ⇒ source resistance. The unit "$\Omega/\square$" ⇒ sheet resistance |
| **30** | $r_d$ · $r_f$ · $r_{ac}$ · $r_{dc}$ | **T1** ·J p37, p38 — $r_{dc} = V_{DQ}/I_{DQ}$ (static) and $r_{ac} = \Delta V_D/\Delta i_D$ (dynamic), both of a **diode** · **T2** ·L1 p7 — $r_d = r_{ac} = r_B + r_j$ | **T1** ·J p47 — $r_f$ = the diode **forward (bulk) resistance** in the rectifier loop, 20 Ω · **T2** ·L2 p3 — $r_d$ used for the same thing, 25 Ω · **T2** ·L4 p7 — $r_d$ = the **a.c. drain resistance of a FET**, $\approx 100\ \mathrm{k\Omega}$ | Order of magnitude settles it instantly: ohms to tens of ohms ⇒ a diode; a hundred kilohms ⇒ a FET drain. A $V_{DS}$ or $I_D$ anywhere nearby ⇒ FET. **The primary notes write the rectifier bulk resistance $r_f$; tier 2 writes $r_d$ for the same quantity** |
| **31** | subscript $f$ · $f_r$ | **forward** — $V_f$, $I_f$, $r_f$, $h_f$, $h_{FB}$ — **T1** ·J p34, p47, p54 · **T2** throughout | **frequency** — $f$ in $X_c = 1/2\pi fC$ **T1** ·J p27 · $f_r$ = **resonant** frequency of a varactor-tuned circuit **T1** ·J p45, **T3** ·RD3 p19 · $f_r$ = **ripple** frequency **T2** ·L2 §2.12 **[added]** · $E_f$ = **final** energy state **T1** ·J p5 · $K_f$ = **form** factor **T2** ·L2 §2.6 | The primary file flags this itself: *"$r_f$ is the diode's forward resistance; $f$ alone, when it appears in filter work, is frequency."* For $f_r$: $1/(2\pi\sqrt{LC})$ beside it ⇒ resonance, megahertz. Equal to the supply frequency or twice it (50 Hz, 100 Hz) ⇒ ripple frequency |
| **32** | $I_t$ · $i_T$ | **T1** ·J p13–p15, p20 — $I_t$ = the **total** current drawn from the source in a series-parallel network · **T1** ·J p55 — $I_t$ = the **total** current through the zener dropping resistor, $I_t = I_{RL} + I_Z$ | **T2** ·L2 §2.16 — $i_T$ = the **tunnel-diode current** plotted against $V_T$ | The primary file flags this itself: *"the subscript $t$ here means **total**, not 'at time $t$'."* On a peak-and-valley characteristic ⇒ tunnel-diode current. Splitting into two branch currents ⇒ total |
| **33** | $T$ / $t$ | **absolute temperature**, K — **T1** ·J p35 · **T2** ·L1 p3 | **T1** ·J p2 — $T$ = the **period** of a waveform; $t$ = time · **T1** ·J p11 — $T$ = the colour-code **tolerance**, per cent, in $R(1-T) \le R \le R(1+T)$ · **T2** ·L7 p17–p18 — $T_1$, $T_2$ = coupling and output **transformers** · **T3** ·RD2 p15 — $T$ = bar **thickness**, with $\Delta T$ a temperature change in the same equation | A kelvin value ⇒ temperature. A millisecond value beside a waveform or an $RC$ product ⇒ period. A percentage beside a fourth colour band ⇒ tolerance. A numeric subscript beside coils in a figure ⇒ a transformer |
| **34** | $L$ / $l$ | **inductance**, H — **T1** ·J p29 ($L = $ coil inductance), ·J p45 (tuning inductance), ·J p51 (filter choke) · **T2** ·L7 p19 $L_p$, $L_s$; ·L2 §2.16 $L_S$ lead inductance | **length** — **T1** ·J p10, the conductor length in $R = \rho L/A$ · **T2** ·L5 p16 $l$ = length of a diffused resistor; ·L5 p22 $L$ = NMOS **channel length**, µm | Henries anywhere ⇒ inductance. Metres, divided by an area ⇒ length. ·L5 keeps $l$ (resistor length) and $L$ (channel length) deliberately distinct — same physical dimension, different object |
| **35** | $R_1$, $R_2$ | **potential-divider arms** — **T1** ·J p18 (Thevenin reduction), ·J p94, p96 (FET divider bias) · **T2** ·L3 §3.25, ·L4 §4.9, §4.20. The primary BJT file writes them $R_{B1}$, $R_{B2}$ ·J p73 | **T2** ·L7 §7.12 — the **feedback divider** setting $\beta = R_1/(R_1+R_2)$ · **T2** ·L3 p8 — **rheostat and potentiometer** in the characteristic-measuring rig | A supply rail above and a base or gate below ⇒ bias divider. Appearing inside a $\beta$ expression ⇒ feedback divider. In a figure captioned as a test circuit with meters ⇒ the rig's controls, not circuit components at all |
| **36** | $R_i$ | **T1** ·J p16 — the **internal resistance of a practical source**, $0.005\ \Omega$; the source is a constant-voltage source when $R_i \ll R_L$ and a constant-current source when $R_i \gg R_L$ | **T2** ·L6 §6.9 — the **amplifier input resistance** at terminals 1–1′, 22 Ω to 144 kΩ; also written $Z_i$ | Milliohms, inside a battery symbol ⇒ internal resistance. Kilohms, at the input port of a two-port model ⇒ input resistance. The two never appear on the same page, but they read identically in a formula |
| **37** | $Z_L$ vs $R_L$ · $Z_i$ vs $R_i$ · $Y_o$ vs $R_o$ | **T2** ·L6 derives every result in **impedance/admittance** form — $Z_L$, $Z_i$, $Y_o$ | **T2** ·L6 p15 then tabulates the same quantities as **resistances** — $R_L$, $R_i$, $R_o$ | Identical quantities, purely resistive in every numerical problem the course sets. $Y_o = 1/R_o$ and $Y_L = 1/Z_L$. Use whichever the question uses; do not treat a switch from $Z_i$ to $R_i$ as a change of quantity. **T1** ·J p16 introduces $Z = \sqrt{R^2+X^2}$ once and never uses it again |
| **38** | $h_{xy}$ | **first** subscript = the **parameter**: i input, r reverse, f forward, o output | **second** subscript = the **configuration**: e common-emitter, b common-base, c common-collector | Read subscripts letter by letter, in that order. $h_{fe}$ is forward gain in CE; $h_{fb}$ is forward gain in CB. **T1** ·J p61 · **T2** ·L6 p3–p7. ⚠ **T1 writes the second subscript in upper case for everything** — $h_{IB}$, $h_{OB}$, $h_{FB}$, $h_{FE}$, $h_{OE}$, $h_{FC}$, $h_{RC}$ — which in the tier-2 convention would mark a **dc** parameter. See §6.4 |
| **39** | $R_E$ vs $R_F$ | $R_E$ = **emitter** resistor, emitter to ground — **T1** ·J p70–p83 · **T2** ·L3, ·L7 | $R_F$ = **feedback** resistor, collector back to base — **T2** ·L7 p12 | ⚠ **V7.9** — ·L7 p12 prints "$R_E$ … in parallel with the input signal at the base" where $R_F$ is meant. The section's own result, $\beta = R_C/R_F$, names the right one. A resistor running **between collector and base** is $R_F$, never $R_E$ |
| **40** | $f_1$ | **lower 3 dB cut-off frequency** of an amplifier — **T2** ·L7 throughout | printed for **$f_\alpha$**, the alpha cut-off frequency, in Ex 60.23 — **T2** ·L7 p27 | ⚠ **V7.20** — the page prints $f_\beta = f_1/80$ where it means $f_\beta = f_\alpha/\beta$. An 8 MHz value being divided by $\beta$ is $f_\alpha$; a value in tens or hundreds of hertz set by a coupling capacitor is $f_1$ |
| **41** | $W$ / $w$ | **depletion-layer thickness**, $\sim10^{-6}\ \mathrm m$ — **T2** ·L1 p1 | minimum **channel separation** at pinch-off ·L4 p4 · $w$ = **width** of a diffused resistor ·L5 p16 · the **watt** · and the glyph the **ohm sign degrades into** | A W after a resistance value is not watts and not width: it is $\Omega$. Logged for **T2** ·L2 p10 (**C2.13**) *and* for **T1** ·J p23 (**JC2.20**, "1 MW" for $1\ \mathrm{M\Omega}$) |
| **42** | $G$ | **T1** ·J p84 · **T2** ·L4 p2 — **G** = the FET **gate** terminal | **T2** ·L7 p22 — **gain in decibels**, $G_v = 20\log_{10}A_v$ · **T2** ·L2 p7 — the **centre tap** of a transformer secondary | On a device pin ⇒ gate. Followed by "dB" ⇒ decibel gain. A node label between M and N on a winding ⇒ centre tap. **T1** ·J p61 writes decibel gains longhand ("power gain (dB) $= 10\log_{10}A_p$") and never uses the letter $G$ |
| **43** | $V_B$ | **T1** ·J p73 · **T2** ·L3 §3.25 — the **base-to-ground voltage** of a biased transistor, a few volts | **T2** ·L1 p3, ·L2 p3 — the **barrier (junction) potential**, 0.3 V (Ge), 0.7 V (Si) | A few volts, measured to ground in a divider-bias circuit ⇒ base voltage. A tenth-of-a-volt value in a diode or rectifier context ⇒ barrier potential. **In tier 1 the ambiguity does not arise** — the primary notes write the barrier potential $V_o$ and reserve $V_B$ for the base node |
| **44** | $I_{CO}$ vs $I_{CBO}$ | $I_{CBO}$ — collector–base leakage, **emitter open**, the formal symbol — **T1** ·J p63 · **T2** ·L3 p6 | $I_{CO}$ — the shorthand for **the same quantity** — **T2** ·L3 p7 onwards | **Not a clash — an alias.** Treat them as identical. $I_{CEO}$ is the different one: collector–emitter leakage with the **base** open, and $I_{CEO} = (1+\beta)I_{CBO}$, derived in full on ·J p64 |
| **45** | $\lambda$ · $\tau$ | **T2** ·L2 §2.14 — $\lambda$ is the handout's own symbol for the **RC time constant** | **T1** ·J p25, p51 — the same quantity is written $\tau = RC$, or simply $RC$ | One quantity, three notations, no wavelength anywhere in this course. A value in milliseconds compared against a signal period ⇒ a time constant |
| **46** | $C_E$ | **T2** ·L3 p16 — prints as a subscripted symbol meaning **"common-emitter"** | reads as an **emitter bypass capacitance** — which is what **T1** ·J p75 calls $C_3$ | ⚠ **C3.30** — the configuration should be written CE upright, not $C_E$. Nothing computed changes, but in a circuit context the same string does mean a capacitor |
| **47** | $e$ vs $q$ | $e$ = electronic charge, $1.6\times10^{-19}\ \mathrm C$ — **T2** ·L1 p3 | $q$ = the same constant — **T1** ·J p35 · **T2** ·L5 | One quantity, two symbols. $V_T = kT/e = kT/q$. **Tier 1 uses $q$ exclusively** |

## 1.1 · $\beta$ — the single most dangerous symbol in the subject

The tier-2 source raises it against itself, in a footnote on its first content page:

> "It may please be noted that it is not the same as the $\beta$ of a transistor (Art. 57.9)" ·L7 p2

**Worst offender: Example 62.13 ·L7 p11**, which uses both meanings inside eight consecutive lines.

$$I_E = \beta I_B = 100 \times 10\ \mathrm{\mu A} = 1\ \mathrm{mA}\qquad (\beta = \text{transistor gain})$$

$$\beta = \frac{R_1}{R_1+R_2} = 0.13 \qquad (\beta = \text{feedback fraction})$$

**The working rule.** In anything about feedback, $\beta$ is the feedback fraction and is small. In
anything about transistor currents, $\beta$ is the current gain and is large. Where both appear,
write the transistor gain as $\beta_{\mathrm{tr}}$ or $h_{fe}$ in your own working — the topic files
do exactly this in commentary while leaving the transcribed equations in the source's own symbols,
so the printed page stays recognisable in an exam.

**A third $\beta$** appears at the end of ·L7: $f_\beta$, the **beta cut-off frequency** ·L7 p26.
That subscript refers to the **transistor** gain, not the feedback fraction.

**The primary notes are clean here.** Across ·J p2–p100 $\beta$ is only ever the CE current gain.
Feedback as a topic does not appear in tier 1 at all.

## 1.2 · $\theta$ — the symbol a reader will not otherwise recognise

$\theta$ (with $\gamma$ given as an alternative on the same line) is the primary notes' symbol for
the **common-collector forward current gain** ·J p62:

$$\theta = \frac{I_E}{I_B} = \gamma = h_{FC} = 1+\beta$$

It sits alongside the two familiar gains ·J p63:

$$\alpha = \frac{I_C}{I_E} \qquad \beta = \frac{I_C}{I_B} \qquad \theta = \frac{I_E}{I_B}$$

and the three are linked by

$$\alpha = \frac{\beta}{\beta+1} \qquad \beta = \frac{\alpha}{1-\alpha} \qquad \theta = 1+\beta = \frac{1}{1-\alpha}$$

**Why this needs flagging.** No tier-2 file uses $\theta$ for anything. A question set from these
notes can write $\theta$ with no gloss, and a reader who has revised only from the lesson documents
will not know the letter. Check with $\alpha = 0.98$: $\beta = 49$ and $\theta = 50$.

⚠ **JV6.5** — ·J p62 opens the derivation with $\theta = I_E/I_C$, which contradicts the definition
three lines above and does not produce $1+\beta$. The correct chain is

$$\theta = \frac{I_E}{I_B} = \frac{I_E}{I_C}\times\frac{I_C}{I_B} = \frac{\beta}{\alpha} = 1+\beta$$

**And $\theta$ is not $\theta$ everywhere.** In the rectifier range ·J p47–p49 the same letter is the
integration angle, $i = I_m\sin\theta$ with $\theta = \omega t$. Two meanings, fifteen pages apart,
in one document.

## 1.3 · $V_T$ — one symbol, three quantities, and two values for the first of them

| Where | $V_T$ means | Value |
|---|---|---|
| **T1** ·J p35 | thermal voltage $kT/q$ at $300\ \mathrm K$ | $26\ \mathrm{mV}$ (25.9 computed) |
| **T2** ·L1 p3 | thermal voltage $kT/e$ at $300\ \mathrm K$ | $26\ \mathrm{mV}$ |
| **T2** ·L1 p6, p18 | thermal voltage at $293\ \mathrm K$ ("room temperature", 20 °C) | $25\ \mathrm{mV}$ |
| **T2** ·L2 §2.16 | terminal voltage of a tunnel diode | $0$–$1\ \mathrm V$ |
| **T2** ·L5 p21 | threshold voltage of an NMOS transistor | not quoted numerically |

**Both temperature values are correct for their stated temperature** — read off which room
temperature a question intends before substituting. The 25 mV value is the one that produces the
exponent multipliers 40 (Ge) and 20 (Si), and it is the one $r_j = 25\ \mathrm{mV}/I_F$ (Ge) and
$50\ \mathrm{mV}/I_F$ (Si) are built from. **The primary notes give no numerical value for $V_T$ at
all** — only the formula ·J p35.

> **A correction to ·L5's own clash note.** ·L5 §5.0 states that `11-diodes` **and**
> `13-bipolar-junction-transistor` use $V_T$ for the thermal voltage. **·L3 never writes $V_T$ at
> all.** The thermal-voltage usage is ·L1's and ·J p35's; ·L2 and ·L5 supply the other two meanings.

---

# 2 · Cross-tier translation — the same quantity under two names

**This is the section to open when moving between a `·J` file and an `·L` file.** None of the rows
below is a clash: each is one physical quantity that the primary lecture notes and the lesson
documents happen to name differently. A question set from tier 1 and revised from tier 2 will run
straight into them.

## 2.1 Transistor gains and h-parameters

| Primary notes (tier 1) | Lesson documents (tier 2) | Note |
|---|---|---|
| $\beta = I_C/I_B = h_{FE}$ ·J p62 | $\beta_{dc} = h_{FE}$ and $\beta_{ac} = h_{fe}$ ·L3 p5, ·L6 | **Tier 1 makes no ac/dc distinction** — it writes one $\beta$ and one $h_{FE}$. Tier 2 splits them; numerically $\beta_{ac} \cong \beta_{dc}$ |
| $\alpha = I_C/I_E = h_{FB}$ ·J p60, p63 | $\alpha_{dc} = -h_{FB}$, $\alpha_{ac} = -h_{fb}$ ·L3 p4 | ⚠ **Note the sign.** Under the strict convention (all currents taken *into* the device) $h_{FB} = -\alpha$. The primary notes drop the sign and work in magnitudes; tier 2 keeps it. Nothing computed changes provided one convention is used throughout |
| $\theta = \gamma = h_{FC} = 1+\beta$ ·J p62 | $1+\beta$, written longhand; $h_{fc} = -51$ ·L6 p8 | **No tier-2 file uses the letter $\theta$.** Tier 2's tabulated $h_{fc}$ carries the sign, so $\lvert h_{fc}\rvert = \theta$ |
| $h_{IB}$, $h_{OB}$, $h_{FB}$, $h_{RB}$ ·J p60–p61 | $h_{ib}$, $h_{ob}$, $h_{fb}$, $h_{rb}$ ·L6 p3–p8 | **Case of the second subscript.** Tier 1 sets it upper case everywhere; in tier 2's convention upper case means the **dc** parameter and lower case the **ac** one. Read tier 1's as the small-signal parameters — that is what its own definitions describe |
| $h_o$, i.e. $h_{OB}$, $h_{OE}$ | $h_o = h_{22}$, output admittance, µA/V ·L6 p3 | **Always siemens, both tiers.** ·J p60–p61 equates $h_{OB}$ to a resistance; that is **JV6.2**, not a different convention |
| $r_o = 1/h_{OE}$ ·J p62 | $R_o = 1/Y_o$ ·L6 §6.11 | CE output resistance, $\approx 40\ \mathrm{k\Omega}$ |
| $A_p$, $A_v$, $A_i$ ·J p61 | $A_P$, $A_V$, $A_I$ ·L6 §6.8–§6.17 | Case only. Both tiers use $10\log_{10}$ for power and $20\log_{10}$ for voltage and current |
| $I_{CBO}$ ·J p63 | $I_{CBO}$, $I_{CO}$ ·L3 p6, p7 | Same quantity; tier 2 adds the shorthand |

## 2.2 Resistors — the swap that matters most

| Primary notes (tier 1) | Lesson documents (tier 2) | Note |
|---|---|---|
| $R_C$ — **collector** resistor ·J p70–p83 | $R_L$ ·L3; $R_C$ ·L6, ·L7 | ⚠ **The translation rule: ·L3's $R_L$ is ·J's $R_C$.** ·L3's circuits have no external load, so it uses the one symbol for the collector resistor; ·J always keeps both |
| $R_L$ — the **external load** beyond the coupling capacitor ·J p75, p83 | $R_L$ ·L2, ·L6, ·L7 (same meaning); ·L3, ·L4 (**different** — see above) | Both appear in ·J p83's Problem 1: $R_L = 10\ \mathrm{k\Omega}$ *and* $R_C = 3.3\ \mathrm{k\Omega}$ |
| $R_D$ — **drain** resistor ·J p93 | $R_L$ ·L4 p20 ($V_{DS} = V_{DD} - I_DR_L$) | Same component, and the same swap as the BJT case |
| $R_{B1}$, $R_{B2}$ — divider arms ·J p73 | $R_1$, $R_2$ ·L3 §3.25 | Identical; ·J p94 and ·J p96 revert to $R_1$, $R_2$ for the FET divider |
| $R_{Th}$, $V_{Th}$ ·J p18, p73 | $R_{th}$ ($= R_B' = R_1 \parallel R_2$), $V_{th}$ ($= V_{BB}'$) ·L3 §3.25 | Thevenin equivalent of the base divider |
| $R_{ac} = R_CR_L/(R_C+R_L)$ ·J p79 | $R_{ac}$, $r_L$ ·L3 §3.27 | ac load resistance seen by the collector — same formula, two names in tier 2 |
| $r_f$ — diode forward bulk resistance, 20 Ω ·J p47 | $r_d$, 25 Ω ·L2 p3 | Same quantity. Tier 2's $r_d$ is also its symbol for the diode's dynamic resistance ·L1 p7 and for the FET drain resistance ·L4 p7 |
| $r_{dc} = V_{DQ}/I_{DQ}$, $r_{ac} = \Delta V_D/\Delta i_D$ ·J p37–p38 | $r_{ac} = r_d = r_B + r_j$ ·L1 §1.6; $r_{dc}$ ·RD3 p8 | Static and dynamic diode resistance |

## 2.3 Passives, rectifiers and supplies

| Primary notes (tier 1) | Lesson documents (tier 2) | Note |
|---|---|---|
| $n = N_p/N_s$ ·J p32 | $a = N_1/N_2$ ·L7 p19 | **The same convention.** $n = a$ |
| $n = N_p/N_s$ ·J p32 | $K = N_2/N_1$ ·L2 p6 | ⚠ **The reciprocal.** $K = 1/n$. This inverts answers — see clash 1 |
| $K$ — dielectric constant ·J p27 | $\varepsilon_r$ ·J p24, ·L5 §5.17 | Same number; ·J uses both letters nine pages apart |
| $V_o$ — barrier / turn-on voltage ·J p34, p38 | $V_B$ ·L1 p3, ·L2 p3 | 0.3 V (Ge), 0.7 V (Si). ⚠ In tier 2 $V_o$ means an **output** voltage |
| $i_D$ (printed $i_o$) ·J p35 | $I$ ·L1 §1.5 | Diode current |
| $I_o$ ·J p35 | $I_0$, $I_s$ ·L1 §1.4 | Reverse saturation (leakage) current |
| $I_{dc}$, $I_{rms}$, $I_{ac}$ ·J p47 | $I_{L(dc)}$, $I_L$, $I_{L(ac)}$ ·L2 §2.5–§2.6 | Rectifier load currents. Same definitions, same constants: $0.318I_m$, $0.5I_m$, $0.385I_m$ half-wave |
| $V_m$ — peak of the rectified sinusoid ·J p47 | $V_{LM}$, $V_{sm}$, $V_{SM}$ ·L2 §2.4 | Tier 2 splits the peak secondary voltage from the peak load voltage; tier 1 uses one symbol |
| $\eta$ — rectification efficiency ·J p47 | $\eta$ ·L2 §2.6 | Same symbol, same quantity. ·J prints 40.5 % and 81.1 %, which are the better roundings |
| $\gamma$ — ripple factor ·J p48 | $\gamma$ ·L2 §2.6 | Same symbol, same quantity, 1.21 and 0.48 |
| $R$, $I_t$, $I_Z$, $I_{RL}$, $V_Z$ ·J p55 | $R$, $I$, $I_z$, $I_L$, $V_z$ ·L1 §1.8–§1.10 | Zener shunt regulator. Tier 2 writes the zener symbols in both cases indiscriminately |
| $\tau = RC$ ·J p25 **[added]**; the notes write $r_fC$ and $R_LC$ directly ·J p51 | $\lambda$ ·L2 §2.14 | RC time constant |

## 2.4 FET quantities

| Primary notes (tier 1) | Lesson documents (tier 2) | Note |
|---|---|---|
| $V_{GS(\mathrm{th})}$ ·J p90 | $V_{GS(\mathrm{th})}$ ·L4 §4.19; $V_T$ ·L5 p21 | E-MOSFET threshold voltage. **Prefer $V_{GS(\mathrm{th})}$** — ·L5's $V_T$ collides with the thermal voltage |
| $V_P$, and $\lvert V_P\rvert = \lvert V_{GS(\mathrm{off})}\rvert$ ·J p85–p87 | $V_P$, $V_{PO}$ ·L4 p5 | Pinch-off voltage. See clash 2 for the sign |
| $K$ — E-MOSFET square-law constant ·J p91 | $K$ ·L4 §4.19 | Same symbol and same law, $I_D = K(V_{GS}-V_{GS(\mathrm{th})})^2$ |
| $V_{SS}$ — magnitude of the negative source rail ·J p94 | $V_{SS}$ ·L4 p9 | **Both take it as a magnitude**, with the rail drawn $-V_{SS}$ |
| $I_S \cong I_D$ ·J p93 | $I_D$ ·L4 p9 | ·J writes source bias as $V_{GS} = -I_SR_S$, ·L4 as $V_{GS} = -I_DR_S$; identical because $I_G \cong 0$ |
| — | $g_m$, $g_{fs}$, $y_{fs}$, $r_d$, $\mu$, $g_{mo}$ ·L4 §4.8 | ⚠ **The small-signal FET parameters exist only in tier 2.** ·J p92 names "forward transconductance" once, in a purchase checklist, and never defines or uses it |

## 2.5 Relations that behave like identities

·L7 §7.29:

$$f_\alpha \cong \beta f_\beta \qquad f_\beta = \frac{f_T}{\beta} \qquad f_\alpha = 1.2\,f_T$$

·L7 §7.4:

$$S = \frac{A}{A'} = 1+\beta A \qquad A' = A_f$$

·J p63:

$$\theta = 1+\beta = \frac{1}{1-\alpha} \qquad \alpha = \frac{\beta}{\beta+1} \qquad \beta = \frac{\alpha}{1-\alpha}$$

---

# 3 · Glyph and render hazards

These are not symbol collisions but **rendering failures** — characters that vanish or mutate
between the printed page and the scan. Every one is logged in `_verification-log.md`; they are
gathered here because on the page they look like notation, not damage.

## 3.1 Tier 1 — the primary lecture notes

| What appears | What it is | Where |
|---|---|---|
| roman **W** after a resistance value | the ohm sign $\Omega$ | ·J p23 — "1 MW", "0.3 MW" for $1\ \mathrm{M\Omega}$ and $0.3\ \mathrm{M\Omega}$ (**JC2.20**) |
| a Greek **α** standing between two quantities | the proportionality sign $\propto$ | ·J p10 — "R α L", "R α ρ" for $R \propto L$, $R \propto \rho$ (**JC2.5**). ⚠ $\alpha$ is the common-base current gain elsewhere in the same document |
| capital **Π** | $\pi$ | ·J p24, p27 — $\varepsilon_0 = \frac{1}{36\Pi}\times10^{-9}\ \mathrm{F/m}$ and $X_c = 1/2\Pi fC$ (**JC3.2**); ·J p45 — $f_r = 1/2\Pi\sqrt{LC}$ (**JC4.12**) |
| **m** where the micro prefix belongs | µ | ·J p27 — "0.033 mF" for $0.033\ \mathrm{\mu F}$ (**JV3.2**). **The commonest unit slip in these notes, and always a factor of $10^3$** |
| **"ev"** | eV — capital V, for Volta | ·J p7 — "Eg = 0ev", "5ev", "1.1ev" (**JC1.15**) |
| **$180^{0}$** with a superscript zero | $180^\circ$ | ·J p31 (**JC3.11**) |
| an answer ending in **Ω** where a voltage belongs | V | ·J p39 — "$V_{Th} = 13.33\ \Omega$" (**JC4.5**) |
| an answer ending in **A** where a power belongs | W | ·J p55 — "$P_Z = 0.03125\times15 = 0.46875\ A$" for $0.469\ \mathrm W$ (**JC5.4**) |
| lower-case **k** in the prose beside capital $K$ in the equation | $K$, the E-MOSFET square-law constant | ·J p91, p92 (**JC7.3**) — lower-case $k$ is Boltzmann's constant on ·J p35 |
| **K** immediately after a digit inside a resistance | the **BS 1852** kilohm marker, not kelvin | ·J p11, p13 — "5K8" $= 5.8\ \mathrm{k\Omega}$, "4K54" $= 4.54\ \mathrm{k\Omega}$, "7M4" $= 7.4\ \mathrm{M\Omega}$, "900R" $= 900\ \Omega$. See §6.6 |
| **$1.38\times10^{-28}$** for Boltzmann's constant | $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ | ·J p35 (**JV4.2**) — wrong by $10^{5}$. ·RD3 p7 prints the identical error |
| a variable sitting **above** an exponential instead of inside it | $i_D = I_o(e^{V_D/\eta V_T}-1)$ | ·J p35 — printed $i_o = I_o(V_D/e^{\eta V_T}-1)$ (**JV4.3**). Dimensional tell: an exponent must be dimensionless |
| bold subscript **2** and **3** indistinguishable | read the equation, not the glyph | ·J p12, p18 — $V_{R3}$ reads as $V_{Ra}$ (**JC2.14**) |
| a decimal point set **outside** the fraction | inside | ·J p13–p15, p21 — "$\frac{200}{779}.022$" for $\frac{200}{779.022}$ (**JC2.10**) |
| solid **coloured bars** over text | a redaction — the text beneath is gone, not faint | ·J p35, p40, p41, p42, p44, p53, p55, p58 (green), p87, p88, p89 |
| **blue hyperlink colouring** on ordinary words | a web-copy artefact; the text is readable | ·J p23, p28 (**JC2.21**) |
| **red ink** on two items | emphasis, not a different quantity | ·J p49, p54 (**JC5.5**) |

## 3.2 Tier 2 — the lesson documents

| What appears | What it is | Where |
|---|---|---|
| roman **W** after a resistance value | the ohm sign $\Omega$ | ·L2 p10 — "a 1 k W load", "diode resistance is 25 W" (**C2.13**) |
| roman **h** where an efficiency belongs | $\eta$ | ·L2 p4, p8 — "If $R_0$ is neglected $h = 40.6\,\%$" (**C2.5**) |
| an equation with **no increment symbols** | $\Delta$ has dropped out | ·L3 p5, p8, p9, p10 — $\alpha_{ac}$ prints as $I_C/I_E$, making the ac definitions look identical to the dc ones (**C3.2**); ·L7 p23 — "$f = f_2-f_1$" for $\Delta f$ (**C7.22**) |
| a figure annotation reading **"=100"** | $\beta = 100$ | ·L3 p14, p15, p18, p19, p20 — the $\beta$ glyph does not render in figure annotations (**C3.3**) |
| **"200 A"** on a reverse-current axis | $200\ \mathrm{\mu A}$ | ·L1 p6, Fig. 52.4 — the µ prefix has dropped (**C1.5**) |
| **"mho"** | the siemens, S | ·L4 p8, ·L6 throughout — the obsolete name for the reciprocal ohm |
| capital **K** for kilo | $\mathrm k$ | ·L5 p9 — "180 KV" for $180\ \mathrm{kV}$, with "20 kV" correct two labels away (**C5.9**); and "5 K", "10 K", "30 K" for kilohms throughout ·L1 p13, ·L3 p14, ·L7 p13, p19 |
| **"kHZ"** | $\mathrm{kHz}$ | ·L7 p27 (**C7.25**) |
| **"In"** where a logarithm belongs | $\ln$ — a capital I for the letter l | ·L1 p8 (**C1.6**) |
| **"$/V_{GS(off)}/$"** | $\lvert V_{GS(\mathrm{off})}\rvert$ — modulus bars lost | ·L4 p6 (**C4.6**) |
| **"300°K"**, **"J/°K"** | $300\ \mathrm K$, $\mathrm{J\,K^{-1}}$ — the kelvin takes no degree sign | ·L1 p3, p6, p8, p18 (**C1.1**) |
| a peak-value line **missing its $\sqrt2$** | e.g. "$V_{pm} = 220 = 312$ V" for $220\sqrt2$ | ·L2 p9, p10, p22 — the answers are right, the expressions are not (**C2.8**) |
| **$K_B$** with an upright B | $K_\beta$, the beta sensitivity | ·L3 p17 |

**The two tiers share three of these faults** — the ohm sign degrading to a roman W, capital K used
for the kilo prefix, and the micro prefix dropping or turning into an m. They are properties of the
scanning and typesetting, not of either author.

---

# 4 · The symbol list

Units are given as the SI unit first, then the practical unit the notes actually use where it
differs. **"Where"** names the topic files by number — **01–07 are tier 1** (·J), **11–17 are tier
2** (·L1–·L7); see the file map at the top.

## 4.1 Voltages

| Symbol | Meaning | Unit (practical) | Where | Typical value |
|---|---|---|---|---|
| $V$ | voltage / electromotive force; also the pd across capacitor plates | V | 02, 03, 11 | 5–50 V |
| $V_p$, $V_{pp}$ | peak value and peak-to-peak value of an analogue waveform | V | 01 | 1–10 V; $2V_p$ |
| $V_o$ | barrier (junction) potential, also the turn-on voltage | V | 04 | 0.2–0.3 (Ge), 0.6–0.7 (Si) |
| $V_B$ | barrier (junction) potential — tier 2's symbol for the same thing | V | 11, 12 | 0.3 (Ge), 0.7 (Si) |
| $V_B$ | base-to-ground voltage of a biased transistor | V | 06, 13 | 4–6 V |
| $V_C$, $V_E$ | collector and emitter voltage to ground | V | 06, 13 | — |
| $V_D$ | diode terminal voltage | V | 04, RD3 | 0.7 V |
| $V_T$ | thermal voltage $kT/q$ | V (mV) | 04, 11 | 26 mV at 300 K; 25 mV at 293 K |
| $V_T$ | terminal voltage of a tunnel diode | V | 12 | 0–1 V |
| $V_T$ | threshold voltage of an NMOS transistor | V | 15 | not quoted |
| $V_f$, $V_R$ | forward and reverse voltage across a diode | V | 04, 05, 11 | 0–1 V; up to $V_{BR}$ |
| $V_{BR}$ | reverse breakdown voltage | V | 04, 11 | tens to hundreds |
| $V_Z$, $V_z$ | zener (breakdown) voltage — both cases used for the same quantity | V | 05, 11 | 15 V (·J p55); 2.4–200 V |
| $V_S$ | supply voltage of a bias, diode or regulator circuit | V | 02, 04, 05 | 20–40 V |
| $V_s$ | source emf of a practical voltage source | V | 02 | 6 V |
| $V_p$, $V_s$ | transformer primary and secondary voltage | V | 03 | 4 V, 20 V (worked example) |
| $V_s$ | rms transformer secondary voltage (tier 2's notation) | V | 12 | 12–240 V |
| $V_{sm}$, $V_{SM}$ | peak (maximum) secondary voltage — case varies inside ·L2 | V | 12 | $\sqrt2\,V_s$; 31 V |
| $V_m$ | peak value of the rectified sinusoid at the load | V | 05 | 25 V |
| $V_{LM}$, $V_{L(dc)}$ | peak and average (dc) load voltage | V | 12 | 31 V; $0.318V_{LM}$ (HW), $0.636V_{LM}$ (FW) |
| $V_{dc}$ | average (dc) load voltage — tier 1's notation | V | 05 | 7.76 V |
| $V_{L(ac)}$, $V_{r(rms)}$ | rms value of the ripple | V | 12 | $0.385V_{LM}$ (HW) |
| $V_{r(pp)}$ | peak-to-peak ripple after smoothing | V | 12 **[added]** | 2.7 V |
| $V_C$ | instantaneous capacitor voltage during charge or discharge | V | 03, 05 | $0 \to V_S$ |
| $V_{RL}$, $V_{R1}$, $V_{R_2}$ | the voltage **across** the named resistor | V | 02, 05, 07 | — |
| $V_{Th}$ | Thevenin (open-circuit) voltage | V | 02, 04, 06 | 13.33 V (·J p39) |
| $V_{th}$, $V_{BB}'$ | Thevenin voltage of the base divider — tier 2's notation | V | 13 | $= V_2$ |
| $V_2$ | dc voltage across the lower divider arm, i.e. the base node before $V_{BE}$ | V | 06, 13 | 1–6 V |
| $V_{MG}$, $V_{GN}$, $V_{MN}$ | half- and full-secondary peak voltages about the centre tap | V | 12 | 78, 78, 156 V |
| $V_{C1}$, $V_{C2}$ | capacitor voltages in a voltage multiplier | V | 12 | $V_m$, $2V_m$ |
| $V_{in}$, $V_o$ | input and output signal voltage of a clipper, clamper or amplifier | V | 06, 12 | ±30 V |
| $V_{in}$ ($E_{in}$), $V_{out}$ ($E_o$) | unregulated input and regulated output of a zener shunt regulator | V | 11 | 32–70 V; 10–30 V |
| $V_{bias}$ | supply voltage in an LED drive circuit | V | 11 | 5 V |
| $V_{CC}$, $V_{EE}$, $V_{BB}$ | dc collector, emitter and base supply voltages | V | 06, 13 | 9–20 V; 5–20 V |
| $V_{DD}$, $V_{SS}$, $V_{GG}$ | dc drain, source and gate supply voltages (FET) | V | 07, 14 | 12–25 V; 5–15 V; 1–5 V |
| $V_{BE}$, $V_{EB}$ | base–emitter junction voltage — first subscript is the more positive terminal | V | 06, 13 | 0.3 (Ge), **0.7 (Si)** |
| $V_{CB}$, $V_{BC}$ | collector–base voltage | V | 06, 13 | 5–20 V |
| $V_{CE}$ | collector–emitter voltage | V | 06, 13 | 3–15 V |
| $V_{CE(cut\text{-}off)}$ | $V_{CE}$ at cut-off — the $V_{CE}$-axis end of the dc load line, $= V_{CC}$ | V | 06, 13 | 10–20 V |
| $V_{CEQ}$ | quiescent collector–emitter voltage | V | 06, 13 | 6–12.7 V |
| $V_{DS}$, $V_{GS}$ | drain–source and gate–source voltage | V | 07, 14 | 5–20 V; 0 to −6 V (N-channel) |
| $V_D$, $V_S$ | drain and source **node potentials** with respect to ground | V | 07 | — |
| $V_{DS(P)}$ | value of $V_{DS}$ at which pinch-off occurs for a given $V_{GS}$ | V | 14 | 3 V |
| $V_P$, $V_{PO}$ | pinch-off voltage — **see clash 2, the sign is not consistent** | V | 07, 14 | 3–8 V in magnitude |
| $V_{GS(off)}$ | gate–source voltage that cuts drain current off | V | 07, 14 | −3 to −8 V (N-channel) |
| $V_{GS(th)}$ | threshold gate–source voltage of an enhancement-only MOSFET | V | 07, 14 | +2 to +5 V |
| $V_{GS(ON)}$ | the data-sheet gate voltage at which $I_{D(ON)}$ is quoted | V | 07 | 8–10 V |
| $V_{GSQ}$, $V_{DSQ}$ | quiescent gate–source and drain–source voltage | V | 07, 14 | −1.8 V, 12.5 V (·J p95) |
| $V_{SD}$, $V_{DG}$, $V_{GD}$ | terminal-pair voltages in the common-drain and common-gate gain ratios | V | 07 | — |
| $V_A$ | avalanche (breakdown) voltage on a JFET drain characteristic | V | 14 | — |
| $V_P$, $V_V$ · $V_p$, $V_v$ | tunnel-diode peak-point and valley-point voltage | V (mV) | 04, 12 | ≈50–100 mV; ≈300–500 mV |
| $V_i$, $V_1$ · $V_o$, $V_2$ | two-port input and output signal voltage | V (mV) | 16 | 1–20 mV; 0.1–2 V |
| $V_b$, $v_b$ · $V_c$, $v_c$ | base (input) and collector (output) signal voltage, CE model | V | 16 | mV; V |
| $v_s$ | signal-source voltage at an amplifier input | V (mV) | 06, 16, 17 | mV |
| $V_o'$, $V_f$ | output voltage **with** feedback; fed-back voltage | V | 17 | 1–10 V |
| $V_{pp}$ | peak-to-peak output swing available at the Q point | V | 06 | $\min(2I_{CQ}R_{ac},\,2V_{CEQ})$ |

## 4.2 Currents

| Symbol | Meaning | Unit (practical) | Where | Typical value |
|---|---|---|---|---|
| $I$ | current, generally; the current through a series network | A (mA) | 01, 02, 11 | mA |
| $i_D$ (printed $i_o$) | diode current | A (mA) | 04 | mA |
| $I_o$ | diode reverse saturation current — tier 1's symbol | A | 04 | nA (Si), µA (Ge) |
| $I_0$, $I_s$ | the same quantity — tier 2's symbols | A | 06, 11 | nA (Si), µA (Ge) |
| $I_f$, $I_R$ | forward and reverse (leakage) current of a diode | A (mA, µA) | 04, 05, 11 | 1–100 mA; nA–µA |
| $I_D$ | diode current from the Thevenin model, $V_{Th}/(R_L+R_{Th})$ | A | 04 | — |
| $I_L$ | load current | A (mA) | 11, 12, 16 | mA |
| $I_{RL}$ | load current in a zener regulator | A (mA) | 05 | 18.75 mA |
| $I_t$ | **total** current — in a network, or through a zener dropping resistor | A (mA) | 02, 05 | 0.257 A; 50 mA |
| $I_Z$, $I_z$ | zener current | A (mA) | 05, 11 | 31 mA |
| $I_{z\,\min}$, $I_{z\,\max}$ | minimum current to sustain breakdown; maximum set by power dissipation | A (mA) | 11 | mA |
| $I_N$ | Norton current — the short-circuit current at the output terminals | A | 02 | 1.6 A |
| $I_1$, $I_2$, $I_3$ | mesh / branch currents in a two-source loop | A | 02 | 0.45–1.27 A |
| $I_m$ | peak load current of a rectifier, $I_m = V_m/(R_L+r_f)$ | A (mA) | 05 | 30 mA |
| $I_{dc}$, $I_{rms}$, $I_{ac}$ | average, total rms, and rms-of-ripple load current | A (mA) | 05 | $0.318I_m$, $0.5I_m$, $0.385I_m$ (HW) |
| $I_{LM}$, $I_{L(dc)}$, $I_{L(ac)}$ | the same three quantities in tier 2's notation | A | 12 | — |
| $I_{L1}$, $I_{L2}$, $I_{L3}$ | rms of the fundamental and the 2nd and 4th harmonics | A | 12 | — |
| $I_{D(av)}$ | average current in **one** diode of a full-wave circuit | A | 12 | $I_{LM}/\pi$ |
| $i$ | instantaneous load current, $i = I_m\sin\theta$ | A | 05 | — |
| $i(t)$ | instantaneous capacitor charging current | A | 03 | $V/R \to 0$ |
| $I_P$, $I_V$ · $I_p$, $I_v$ | tunnel-diode peak and valley current | A (mA) | 04, 12 | mA; $I_P/3$ to $I_P/12$ |
| $i_T$ | tunnel-diode current | A (mA) | 12 | mA |
| $I_p$, $I_s$ | transformer primary and secondary current | A | 03 | 0.5 A, 0.1 A |
| $I_E$, $I_B$, $I_C$ | emitter, base and collector current | A (mA, µA) | 06, 13 | 1–10 mA; 10–100 µA; 1–10 mA |
| $i_e$, $i_b$, $i_c$ | the ac (small-signal) components of the same three | A | 06, 16 | µA–mA |
| $i_E$, $i_B$, $i_C$ | the total instantaneous values | A | 06 | — |
| $I_{CBO}$ ($I_{CO}$) | collector–base leakage, **emitter open** | A (µA, nA) | 06, 13 | 1–10 µA (Ge), nA (Si) |
| $I_{CEO}$ | collector–emitter leakage, **base open**, $= (1+\beta)I_{CBO}$ | A (µA) | 06, 13 | $(1+\beta)I_{CBO}$ |
| $I_{C(sat)}$ | collector current at saturation, the top of the dc load line | A (mA) | 06, 13 | $V_{CC}/(R_C+R_E)$ |
| $I_{CQ}$ | quiescent collector current | A (mA) | 06, 13 | 1.4–2 mA |
| $I_D$, $I_S$, $I_G$ | drain, source and gate current; $I_S \cong I_D$ because $I_G \cong 0$ | A (mA) | 07, 14 | 1–20 mA; ~0 (pA–nA) |
| $I_{DSS}$ | drain current with the gate shorted to the source, in saturation | A (mA) | 07, 14 | 5–20 mA |
| $I_{D(ON)}$ | data-sheet drain current quoted at a stated $V_{GS(ON)}$ | A (mA) | 07, 14 | 3–5 mA |
| $I_{DQ}$ | quiescent drain current | A (mA) | 07, 14 | 1–5 mA |
| $I_i$, $I_1$ · $I_o$, $I_2$ | two-port input and output signal current | A | 16 | 10–100 µA; 0.5–5 mA |
| $I_s$ | signal-source current (Norton form), used in $A_{IS} = -I_2/I_s$ | A | 16 | — |

## 4.3 Resistances, impedances and conductances

| Symbol | Meaning | Unit (practical) | Where | Typical value |
|---|---|---|---|---|
| $R$ | resistance, generally | Ω (kΩ) | 02, 11, 12 | 10 Ω – 10 MΩ |
| $R$ | zener dropping resistor · shunt resistor of a diode Thevenin network · filter time-constant resistance | Ω | 04, 05 | 200 Ω, 500 Ω |
| $\rho$ | resistivity of the conductor material | Ω m | 02, 15 | $1.7\times10^{-8}\ \Omega\,\mathrm m$ (Cu) |
| $R_t$ | total resistance of a series, parallel or combined network | Ω | 02 | 9.4 Ω – 7.4 MΩ |
| $R_a$, $R_b$, $R_c$, $R_d$ | intermediate combinations in the six-resistor reduction | Ω | 02 | 22–62 Ω |
| $R_i$ | internal resistance of a practical source | Ω | 02 | 0.005 Ω |
| $Z$, $X$ | impedance and reactance, $Z = \sqrt{R^2+X^2}$ | Ω | 02 | — |
| $R_{Th}$, $R_N$ | Thevenin and Norton resistance, $R_N = R_{Th}$ | Ω | 02, 04 | 16.67 Ω, 66.67 Ω |
| $r_{dc}$ | static (dc) resistance of a diode, $V_{DQ}/I_{DQ}$ | Ω | 04, RD3 | — |
| $r_{ac}$ | dynamic (ac) resistance of a diode, $\Delta V_D/\Delta i_D$ | Ω | 04, 11 | a few Ω to tens of Ω |
| $r_B = r_P + r_N$ · $r_j$ | bulk resistance and junction resistance of a diode, $r_{ac} = r_B + r_j$ | Ω | 11 | 25 Ω at 1 mA (Ge) |
| $r_f$ | diode forward (bulk) resistance in the rectifier loop | Ω | 05 | 20 Ω |
| $r_d$ | the same quantity in tier 2 — **and** the diode dynamic resistance, **and** the FET drain resistance | Ω | 11, 12, 14 | 25 Ω; 100 kΩ (FET) |
| $R_R$ | reverse dc resistance of a diode; dark resistance of a photodiode | Ω (MΩ) | 04, 11 | MΩ range |
| $Z_z$ | zener dynamic impedance | Ω | 11 | small |
| $R_L$ | **external load** resistance | Ω (kΩ) | 02, 04, 05, 06, 07, 12, 16, 17 | 100 Ω – 30 kΩ |
| $R_L$ | **collector or drain load** resistor — tier 2's usage in ·L3 and ·L4 | Ω (kΩ) | 13, 14 | 1–10 kΩ |
| $R_C$ | collector resistor | Ω (kΩ) | 06, 16, 17 | 2–3.3 kΩ |
| $R_D$ | drain resistor | Ω (kΩ) | 07 | 1–5 kΩ |
| $R_E$ | emitter resistor / total resistance on the emitter side | Ω (kΩ) | 06, 13, 17 | 0.8–2 kΩ |
| $R_B$ | total series-parallel resistance in the base | Ω (kΩ) | 06, 13 | 8 kΩ – 1 MΩ |
| $R_{B1}$, $R_{B2}$ | upper and lower divider arms of a BJT bias network | Ω (kΩ) | 06 | 10–56 kΩ |
| $R_1$, $R_2$ | divider arms — bias, feedback, or test-rig controls; **see clash 35** | Ω (kΩ) | 02, 06, 07, 13, 14, 17 | 6 kΩ – 15.7 MΩ |
| $R_{th}$, $R_B'$ | Thevenin resistance of the base divider, $R_1 \parallel R_2$ | Ω (kΩ) | 13 | 4.2–20 kΩ |
| $R_{ac}$, $r_L$ | ac load resistance seen by the collector, $R_CR_L/(R_C+R_L)$ | Ω (kΩ) | 06, 13 | 2.48 kΩ |
| $R_{dc}$ | dc resistance in the collector–emitter path, $R_C+R_E$ | Ω (kΩ) | 06 | 5.3 kΩ |
| $R_{in}$, $R_{out}$ | input and output resistance of a transistor stage, $\Delta V/\Delta I$ at the port | Ω | 13 | ≈50 Ω, ≈500 kΩ (CB) |
| $r_o$ | CE output resistance, $= 1/h_{OE}$ | Ω (kΩ) | 06 | 40 kΩ |
| $R_S$ | source-side series resistance of a diode network | Ω | 04 | 100 Ω |
| $R_S$ | transformer secondary resistance · tunnel-diode series ohmic resistance | Ω | 12 | ≪ $R_L$; 1–5 Ω |
| $R_S$ | FET **source bias** resistor | Ω (kΩ) | 07, 14 | 0.5–3 kΩ |
| $R_G$ | FET gate return resistor | Ω (MΩ) | 07, 14 | 1–10 MΩ |
| $R_{DS}$ | d.c. (static, ohmic) drain resistance, $V_{DS}/I_D$ | Ω | 07, 14 | — |
| $r_d$, $r_{ds}$ | a.c. (dynamic) drain resistance, $\delta V_{DS}/\delta I_D$ | Ω (kΩ) | 14 | 100 kΩ |
| $r_i$, $r_o'$ | input and output resistance of a FET stage | Ω | 14 | $1/g_m$; $\approx 1/g_m \parallel R_L$ |
| $R_0$ | total series resistance outside the load — **three meanings, see clash 28** | Ω | 12 | 0.25–25 Ω |
| $-R_N$ | negative resistance of a tunnel diode between peak and valley | Ω | 12 | −10 to −200 Ω |
| $Z_L$, $R_L$ · $Y_L = 1/Z_L$ | load impedance, resistance, admittance | Ω, S | 16 | 1–10 kΩ; 0.1–1 mS |
| $Z_i$, $R_i$ | amplifier input impedance at terminals 1–1′ | Ω | 16 | 22 Ω – 144 kΩ |
| $Y_o$, $R_o$ | amplifier output admittance / resistance at 2–2′ | S, Ω | 16 | µS; 80 Ω – 1.7 MΩ |
| $R_s$ | signal-source internal resistance | Ω (kΩ) | 16, 17 | 0.5–3 kΩ |
| $R_i'$, $R_o'$ | input and output resistance **with** feedback | Ω | 17 | $R_i(1+\beta A)$; $R_o/(1+\beta A)$ |
| $R_F$ | feedback resistor, collector back to base | Ω (kΩ) | 17 | — |
| $R_{eq}$ | equivalent resistance seen by a coupling or bypass capacitor | Ω (kΩ) | 17 | 2.9–20 kΩ |
| $r_e$ | transistor ac emitter resistance — **two conventions, see §6.7** | Ω | 17 | 10–100 Ω |
| $r_{o.1}$, $r_{i.2}$ | resistance at stage 1's collector (reflected); input resistance of stage 2 | Ω (kΩ) | 17 | tens of kΩ; ~1 kΩ |
| $R$ | resistance of a diffused IC resistor, $R = \rho\,l/a$ | Ω (kΩ) | 15 | 100 Ω to several kΩ |
| $R_s$ | sheet resistance, $\rho/d$ | Ω per square | 15 **[added]** | 100–200 Ω/□ |

## 4.4 Gains, ratios and figures of merit

| Symbol | Meaning | Unit | Where | Typical value |
|---|---|---|---|---|
| $\eta$ | diode ideality (emission) factor | — | 04, 11 | 1 (Ge), 2 (Si) |
| $\eta$ | rectification (conversion) efficiency $P_{dc}/P_{ac}$ | — (%) | 05, 12 | 40.5 % (HW), 81.1 % (FW) |
| $\eta$ | transformer efficiency $P_s/P_p$ | — (%) | 03 | 90 % |
| $\gamma$ | ripple factor, $I_{ac}/I_{dc}$ | — | 05, 12 | 1.21 (HW), 0.48 (FW) |
| $K_f$ | form factor, rms / average | — | 12 | 1.57 (HW), 1.11 (FW) |
| PIV | peak inverse voltage across a diode | V | 12 | $V_{sm}$ (HW), $2V_{sm}$ (CT) |
| TUF | transformer utilisation factor | — | 12 | 0.287 (HW) |
| $V_R$ | voltage regulation, $R_0/R_L$ | — (%) | 12 | 2.5 % |
| $n$ | transformation (turns) ratio $N_p/N_s = V_p/V_s = I_s/I_p$ | — | 03 | 0.2 |
| $a$ | turns ratio $N_1/N_2$ — the same convention as $n$ | — | 17 | 2–10 |
| $K$ | turns ratio $N_2/N_1$ — **the reciprocal** | — | 12 | 1/10 |
| $T$ | resistor tolerance, in $R(1-T) \le R \le R(1+T)$ | — (%) | 02 | ±1 % to ±20 % |
| $\alpha$, $h_{FB}$ | common-base forward current gain $I_C/I_E$ | — | 06, 13 | 0.95–0.99 |
| $\alpha_{dc}$, $\alpha_{ac}$ | its dc and ac forms; $\alpha_{ac} = -h_{fb}$ | — | 13 | $\approx$ equal |
| $\beta$, $h_{FE}$ | common-emitter forward current gain $I_C/I_B$ | — | 06, 13 | 50–500 |
| $\beta_{dc}$, $\beta_{ac}$ | its dc and ac forms; $\beta_{ac} = h_{fe}$ | — | 13 | $\approx$ equal |
| $\theta$, $\gamma$, $h_{FC}$ | common-collector forward current gain $I_E/I_B = 1+\beta$ | — | 06 | 51–501 |
| $S$ | current stability factor $\mathrm dI_C/\mathrm dI_{CO}$ | — | 06, 13 | 1 (CB) to $1+\beta$; 5–10 for a good divider |
| $K_\beta$ | beta sensitivity, $(\beta/I_C)(\mathrm dI_C/\mathrm d\beta)$ | — | 13 | 0 to 1 |
| $A_p$, $A_v$, $A_i$ | power, voltage and current gain (tier 1's case) | — | 06, 07 | — |
| $A_P$, $A_V$, $A_I$ | the same three (tier 2's case) | — | 16 | 47–6100; 1–131; 0.98–50 |
| $A_{VS}$, $A_{IS}$ | overall voltage gain $V_2/V_s$; overall current gain $-I_2/I_s$ | — | 16 | — |
| $A$ | open-loop gain of a stage or of the whole amplifier | — | 17 | $10^2$–$10^4$ |
| $A'$, $A_f$ | closed-loop (with-feedback) gain | — | 17 | $10$–$10^2$ |
| $\beta$ | feedback fraction | — | 17 | 0.001–0.2 |
| $\beta A$ | feedback factor; $1\pm\beta A$ is the loop gain | — | 17 | $10$–$10^3$ |
| $\beta_1$, $\beta_2$ | feedback ratio per stage; feedback ratio of the single overall loop | — | 17 | 0.01–0.2; $10^{-4}$–$10^{-2}$ |
| $S$ | sacrifice factor $A/A' = 1+\beta A$ | — | 17 | $10$–$10^3$ |
| $D$, $D'$ | distortion without and with feedback, $D' = D/(1+\beta A)$ | — (%) | 17 | — |
| $G_v$, $G_i$, $G_p$ | gain in decibels — $20\log_{10}$ for voltage and current, $10\log_{10}$ for power | dB | 17 | — |
| $\mu$ | FET amplification factor $g_mr_d$ | — | 14 | 100–300 |
| $n$ | number of identical cascaded stages | — | 17 | 2–4 |
| $n$ | number of identical resistors making up a power rating | — | 02 | 5 |

## 4.5 Capacitances and inductances

| Symbol | Meaning | Unit (practical) | Where | Typical value |
|---|---|---|---|---|
| $C$ | capacitance, $C = \varepsilon_0\varepsilon_r A/d$ | F (pF–mF) | 03 | pF to mF |
| $\varepsilon_r$ ($K$) | relative permittivity / dielectric constant | — | 03, 15 | 1 (air) to >3000 (high-K ceramic) |
| $\varepsilon_0$ | permittivity of free space | F m⁻¹ | 03, 15 | $8.854\times10^{-12}$ |
| $A$, $d$ | effective plate area and plate separation | m², m | 03, 04 | mm²–m²; µm |
| $E$ | energy stored in a capacitor, $\tfrac12CV^2 = \tfrac12QV = Q^2/2C$ | J | 03 | µJ to J |
| $X_c$ | capacitive reactance, $1/2\pi fC$ | Ω | 03 | — |
| $Q$ | quality factor of a capacitor | — | 03 | — |
| $C$ | junction capacitance of a varactor, $C = \varepsilon A/d$ or $K/\sqrt{V_R}$ | F (pF) | 04, 11 | 5–100 pF |
| $C_D$ · $C_T$, $C_{pn}$ | diffusion capacitance (forward bias); transition (depletion) capacitance (reverse bias) | F | 11 | — |
| $C$ | smoothing (reservoir) capacitance | F (µF) | 05 · 12 **[added]** | tens to thousands of µF |
| $C$ | tunnel-diode junction capacitance · coupling / clamping capacitor | F (pF, µF) | 12 | 1–10 pF; 1 µF |
| $C_1$, $C_2$, $C_3$ | input coupling, output coupling and emitter bypass capacitors | F (µF) | 06 | 1–100 µF |
| $C_1$, $C_2$, $C_S$ | FET input and output coupling capacitors; source bypass capacitor | F (µF) | 07 | µF |
| $C_{gs}$, $C_{gd}$, $C_{ds}$ | FET gate–source, gate–drain and drain–source capacitances | F (pF) | 14 | 1–3 pF |
| $C_i$ | Miller input capacitance of a FET stage, $C_{gs} + (1-A_v)C_{gd}$ | F (pF) | 14 | — |
| $C_{be}$, $C_{bc}$ · $C_{in}$ | BJT internal capacitances; Miller input capacitance $C_{be} + (1+A_v)C_{bc}$ | F (pF) | 17 | pF–nF |
| $C_{wi}$, $C_S$ | wiring (stray input) capacitance; stray capacitance at an output terminal | F (pF) | 17 | 100 pF |
| $C_F$ | feedback coupling capacitor | F (µF) | 17 | — |
| $L$ | inductance, $L = kN^2$ | H (µH–H) | 03, 17 | µH to H |
| $\mu$ | permeability of the core or medium | H m⁻¹ | 03 | $\mu_0 = 4\pi\times10^{-7}$ |
| $H$ | magnetic field strength | A m⁻¹ | 03 | — |
| $N$ | number of turns on a coil | — | 03 | tens to thousands |
| $M$ | mutual inductance between two coils | H | 03 | — |
| $N_p$, $N_s$ ($N_1$, $N_2$) | transformer primary and secondary turns | — | 03, 17 | 400 / 2000 |
| $L$ | choke (filter) inductance · varactor tuning inductance | H | 04, 05 | a few H |
| $L_p$, $L_s$ · $L_S$ | primary and secondary inductance; tunnel-diode series lead inductance | H, nH | 12, 17 | — |

## 4.6 Frequencies and time

| Symbol | Meaning | Unit | Where | Typical value |
|---|---|---|---|---|
| $f$ | frequency | Hz | 03, 05 | 0 (dc) to MHz |
| $\omega$ | angular frequency, $2\pi f$ | rad s⁻¹ | 05, 12 | $2\pi\times50$ |
| $\theta$ | angle, $\theta = \omega t$, in the rectifier integrals | rad | 05 | $0 \to 2\pi$ |
| $T$ | period of one complete cycle | s (ms) | 01, 12 | ms to µs |
| $t$ | time | s | 01, 02, 03, 05 | — |
| $\tau = RC$ | time constant of a charge or discharge path | s (ms) | 03 **[added]**, 05 | µs to s |
| $\lambda$ | the same quantity, in ·L2's own notation | s (ms) | 12 | 10 ms |
| $f_r$ | resonant frequency of a varactor-tuned circuit, $1/(2\pi\sqrt{LC})$ | Hz | 04, RD3 | MHz |
| $f_r$ | ripple frequency — $f$ half-wave, $2f$ full-wave | Hz | 05 · 12 **[added]** | 50, 100 Hz |
| $t_1 \ldots t_4$ | successive 120° conduction intervals in a three-phase rectifier | s | 12 | $T/3$ |
| $f_1$, $f_2$ | lower and upper 3 dB (cut-off) frequency, no feedback | Hz | 17 | 20 Hz – 1 kHz; 10 kHz – 1 MHz |
| $f_1'$, $f_2'$ | the same **with** feedback | Hz | 17 | $f_1/(1+\beta A)$; $f_2(1+\beta A)$ |
| $BW$, $BW'$, $\Delta f$ | bandwidth $f_2-f_1$, without and with feedback | Hz | 17 | — |
| $f_{1.n}$, $f_{2.n}$ | cut-off frequencies of $n$ identical cascaded stages | Hz | 17 | — |
| $f_s$ | frequency at which a stray capacitance costs 3 dB | Hz | 17 | 15.9–159 kHz |
| $f_\alpha$, $f_\beta$, $f_T$ | alpha and beta cut-off frequencies; gain–bandwidth product | Hz | 17 | 8–345 MHz; 0.1–6 MHz; 6–300 MHz |
| $f$ | frequency of an emitted photon, in $hf = E_i-E_f$ | Hz | 01 | — |

## 4.7 Device parameters

### h-parameters

| Symbol | Meaning | Unit | Typical value (CE) |
|---|---|---|---|
| $h_i = h_{11}$ | input resistance, output short-circuited | Ω | 1100 Ω |
| $h_r = h_{12}$ | reverse voltage transfer ratio, input open-circuited | — | $2.5\times10^{-4}$ |
| $h_f = h_{21}$ | forward current gain, output short-circuited | — | 50 |
| $h_o = h_{22}$ | output **admittance**, input open-circuited | S (µA/V, "mho") | 25 µA/V |
| $\Delta h$ | determinant of the hybrid matrix, $h_ih_o - h_fh_r$ | — (Ω × S = 1) | — |

Second subscript **e**, **b**, **c** selects the configuration. Typical CB and CC columns ·L6 p8:
$h_{ib} = 22\ \Omega$, $h_{rb} = 3\times10^{-4}$, $h_{fb} = -0.98$, $h_{ob} = 0.49\ \mathrm{\mu A/V}$;
$h_{ic} = 1100\ \Omega$, $h_{rc} = 1$, $h_{fc} = -51$, $h_{oc} = 25\ \mathrm{\mu A/V}$.

The primary notes name six of these directly ·J p60–p62: $h_{IB}$ (CB input resistance,
20–50 Ω), $h_{OB}$ (CB output admittance), $h_{FB} = \alpha$, $h_{RB}$ (CB reverse voltage gain),
$h_{IE}$ (CE input resistance, 1–4 kΩ), $h_{OE}$ (CE output admittance, 25 µA/V), $h_{FE} = \beta$,
$h_{FC} = \theta$, $h_{RC} \cong 1$. **See §6.4 on the case of the second subscript.**

### FET small-signal parameters — tier 2 only

| Symbol | Meaning | Unit | Where | Typical value |
|---|---|---|---|---|
| $r_d$, $r_{ds}$ | a.c. drain resistance, $\delta V_{DS}/\delta I_D$ at constant $V_{GS}$ | Ω | 14 | 100 kΩ |
| $y_{os}$ | output admittance, $1/r_d$ | S (µS) | 14 | 10 µS |
| $g_m$, $g_{fs}$, $y_{fs}$ | transconductance, $\delta I_D/\delta V_{GS}$ at constant $V_{DS}$ | S (mS, µS, "mho") | 14, 15 | 1–6 mS |
| $g_{mo}$ | transconductance at $V_{GS} = 0$; $g_{mo} = 2I_{DSS}/\lvert V_{GS(\mathrm{off})}\rvert$ | S | 14 | 3–6 mS |
| $\mu$ | amplification factor, $g_mr_d$ | — | 14 | 100–300 |

**The primary notes contain none of these.** ·J p92 lists "forward transconductance" once, as a
purchase parameter, and never defines it. Any question asking for a FET gain as a number must be
answered from `14-field-effect-transistors.md`.

### Square-law and channel parameters

| Symbol | Meaning | Unit | Where | Typical value |
|---|---|---|---|---|
| $K$ | constant of the E-MOSFET square law, $I_D = K(V_{GS}-V_{GS(\mathrm{th})})^2$ | A V⁻² (mA/V²) | 07, 14 | 0.1–0.3 mA/V² |
| $R_{DS}$ | d.c. drain resistance, $V_{DS}/I_D$ | Ω | 07, 14 | — |
| $\mathrm{SiO_2}$ | the gate insulator of a MOSFET | — | 07, 15 | film ~100 nm |

### Powers

| Symbol | Meaning | Unit | Where | Typical value |
|---|---|---|---|---|
| $P$ | power, $P = VI = I^2R = V^2/R$ | W | 02 | 0.125–2 W (a resistor) |
| $P_p$, $P_s$ | transformer primary (input) and secondary (output) power | W | 03 | — |
| $P_{dc}$, $P_{ac}$ | dc power delivered to the load; ac power drawn from the source | W (mW) | 05, 12 | 75.3 mW |
| $P_L$ | power absorbed by the load | W | 12 | 2.4 W |
| $P_Z$ | power dissipated in a zener, $P_Z = I_ZV_Z$ | W | 05 | 0.47 W |
| $P_{\max}$ | maximum power dissipation of a zener diode | W | 11 | 150 mW – 50 W |
| $P_{ac}$, $P_{dc}$ | ac and dc power dissipated in the collector load (load-line analysis) | W (mW) | 13 | 0.81 mW, 8 mW |

## 4.8 Semiconductor, atomic and process quantities

| Symbol | Meaning | Unit (practical) | Where | Typical value |
|---|---|---|---|---|
| $Q$ | electric charge, $Q = It$ | C | 01, 02, 03 | µC to mC |
| $N$ | number of electrons a shell can hold, $N = 2n^2$ | — (a count) | 01 | 2, 8, 18, 32 |
| $n$ | shell number, counted outwards from the nucleus | — | 01 | 1 to 7 |
| $m$ | sub-shell number within a shell; capacity $2+4(m-1)$ | — | 01 | 1 to 6 |
| $h$ | Planck's constant | J s | 01 | $6.626\times10^{-34}$ |
| $E_i$, $E_f$ | initial and final energy states in the Bohr transition $hf = E_i-E_f$ | J (eV) | 01 | — |
| $E_g$ | energy gap — the width of the forbidden band | eV | 01, RD2 | 0 (conductor), 1.1 (Si), 5 (insulator) |
| $Z$ | atomic number (the proton count) — the notes name it in words; the letter is ours | — | 01 **[added]** | 1–20 in the notes' table |
| $N_a$, $N_d$ | acceptor (P-side) and donor (N-side) doping density | m⁻³ | 11 | $10^{21}$, $10^{22}$ |
| $n_i$ | intrinsic carrier density | m⁻³ (cm⁻³) | 11, 15 | $1.4\times10^{16}\ \mathrm{m^{-3}}$ (Si) |
| $W$ | depletion-layer thickness | m | 11 | $\sim10^{-6}$ |
| $d$ | depletion-layer width, read as a capacitor plate separation | m (µm) | 04 | µm |
| $\varepsilon$ | permittivity of the junction material | F m⁻¹ | 04 | — |
| $\Delta t$ | temperature rise (signed) | °C | 11 | — |
| $\rho$ | resistivity of a diffused layer | Ω·m (Ω·cm) | 15 | 0.1–1 Ω·cm (epitaxial) |
| $l$, $w$, $d$ · $a = wd$ | length, width, depth and cross-section of a diffused resistive region | m (cm), m² | 15 | — |
| $R_s$ · $n = l/w$ | sheet resistance; number of squares | Ω/□ · — | 15 **[added]** | 100–200 Ω/□ |
| $L$ | channel length of a finished NMOS device | m (µm) | 15 | — |
| $\mu_n$, $\mu_p$ | electron and hole mobility | m²V⁻¹s⁻¹ (cm²V⁻¹s⁻¹) | 15 **[added]** | see §5.4 |
| $\sigma$ | conductivity, $q\,n_i(\mu_n+\mu_p)$ | S m⁻¹ | 15 **[added]** | see §5.4 |

## 4.9 Terminals, elements, devices and circuit labels

| Symbol | Meaning | Where |
|---|---|---|
| $E$, $B$, $C$ | emitter, base, collector terminals of a BJT | 06, 13 |
| $J_1$, $J_2$ | the emitter–base and collector–base junctions | 06 |
| D, S, G | drain, source, gate terminals of a FET | 07, 14 |
| SS | substrate — the fourth lead of a MOSFET | 07, 14 |
| a, k | anode and cathode leads of a diode or LED | 11 |
| $D$, $D_1 \ldots D_4$ | diode designators in rectifier, clipper and multiplier circuits | 04, 05, 12 |
| $Q_1$, $Q_2$ | transistor designators in a multistage amplifier | 17 |
| $T_1$, $T_2$ | coupling transformer and output transformer | 17 |
| $G$ | centre tap of a transformer secondary — the zero-voltage reference | 12 |
| A, B | the two terminals a load is removed from in a Thevenin or Norton reduction | 02 |
| $Q$-point | quiescent operating point, $(V_{CE},I_C)$ or $(V_{DS},I_D)$ with no signal | 04, 06, 07, 13, 14 |
| $d_1$, $d_2$, $m$ | the colour code's two significant digits and its multiplier exponent | 02 |
| H, He, Li, Be, **B**, **C**, **N**, O, F, Ne, Na, Mg, Al, **Si**, **P**, **S**, Cl, Ar, K, Ca | the first twenty elements, by chemical symbol | 01 |

---

# 5 · Constants and material values

## 5.1 Physical constants

| Constant | Symbol | Value | Where |
|---|---|---|---|
| Boltzmann constant | $k$ | $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ | ·L1 p3, p6. ⚠ ·J p35 prints $1.38\times10^{-28}$ (**JV4.2**) and ·RD3 p7 the same; **use $10^{-23}$** |
| Electronic charge | $q$ (also $e$) | $1.6\times10^{-19}\ \mathrm C$ (·L5 uses $1.602\times10^{-19}$) | ·J p35, ·L1 p3, ·L5 §5.2 |
| $e/k$ | — | $11{,}600\ \mathrm{K\,V^{-1}}$, so $V_T = T/11{,}600$ | ·L1 p6 |
| Planck's constant | $h$ | $6.626\times10^{-34}\ \mathrm{J\,s}$ | ·J p5 |
| Electron-volt | eV | $1\ \mathrm{eV} = 1.602\times10^{-19}\ \mathrm J$ | ·J p7 |
| Permittivity of free space | $\varepsilon_0$ | $8.854\times10^{-12}\ \mathrm{F\,m^{-1}}$; the notes also write $\frac{1}{36\pi}\times10^{-9}$, which is $0.14\,\%$ low | ·J p24, ·L5 §5.17 |
| Permeability of free space | $\mu_0$ | $4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ | ·J p29 |
| Resistivity of copper | $\rho$ | $1.7\times10^{-8}\ \Omega\,\mathrm m$ | ·J p10 |

*Verification: $1.6\times10^{-19}/1.38\times10^{-23} = 11{,}594 \approx 11{,}600$ ✓*

## 5.2 The thermal voltage at the two temperatures the notes use

| Temperature | $V_T = kT/q$ | Exponent multiplier $1/\eta V_T$ | Where |
|---|---|---|---|
| $300\ \mathrm K$ (27 °C) | $26\ \mathrm{mV}$ (25.875 computed) | — | ·J p35 (formula only), ·L1 p3, p8 |
| $293\ \mathrm K$ (20 °C) | $25\ \mathrm{mV}$ (25.26 computed) | **40** for Ge ($\eta=1$), **20** for Si ($\eta=2$) | ·L1 p6, p18 |

The $25\ \mathrm{mV}$ value is the one that generates the 40/20 shorthand, the junction resistances
$r_j = 25\ \mathrm{mV}/I_F$ (Ge) and $50\ \mathrm{mV}/I_F$ (Si), and — indirectly — the two $r_e$
conventions of ·L7. **Both values are right for their stated temperature; the error is substituting
one where the question intends the other.**

## 5.3 Junction, device and circuit values quoted by the notes

| Quantity | Value | Where |
|---|---|---|
| Turn-on / barrier voltage $V_o$ | $0.2$–$0.3\ \mathrm V$ (Ge), $0.6$–$0.7\ \mathrm V$ (Si) | ·J p34, p38 |
| Barrier potential $V_B$ at 300 K | $0.3\ \mathrm V$ (Ge), $0.7\ \mathrm V$ (Si) | ·L1 p3 |
| Temperature coefficient of $V_B$ | $\Delta V_B = -0.002\,\Delta t$, i.e. $-2\ \mathrm{mV\,^\circ C^{-1}}$, both materials | ·L1 p3 |
| Ideality factor $\eta$ | 1 (Ge), 2 (Si) | ·J p35, ·L1 p6 |
| Reverse saturation current | nanoamperes (Si), microamperes (Ge); doubles every 10 °C rise | ·J p34, ·L1 p5 |
| Zener/avalanche dividing line | Zener effect dominant **below 6 V**, avalanche **above 6 V** | ·L1 p8 |
| LED forward drop | $1$–$3\ \mathrm V$ at $I_f \approx 10$–$20\ \mathrm{mA}$ | ·J p41–p42, ·L1 §1.11 |
| Half-wave rectifier constants | $I_{dc} = 0.3183\,I_m$, $I_{rms} = 0.5\,I_m$, $\eta_{\max} = 4/\pi^2 = 40.5\,\%$, $\gamma = 1.21$ | ·J p47–p48 |
| Full-wave rectifier constants | $I_{dc} = 0.6366\,I_m$, $I_{rms} = 0.707\,I_m$, $\eta_{\max} = 8/\pi^2 = 81.1\,\%$, $\gamma = 0.48$ | ·J p48–p49 |
| CB / CE / CC current gains | $\alpha = 0.95$–$0.99$, $\beta = 50$–$500$, $\theta = 1+\beta$ | ·J p60–p63 |
| Intrinsic resistivity | $230{,}000\ \Omega\!\cdot\!\mathrm{cm}$ (Si), $47\ \Omega\!\cdot\!\mathrm{cm}$ (Ge) | ·L5 p2 |
| Melting point of silicon | $1685\ \mathrm K$ (furnace run at $1690\ \mathrm K$) | ·L5 §5.5 |
| Relative permittivity | $\approx 3.9$ (SiO$_2$), $\approx 7$ (Si$_3$N$_4$) — **[added]**, used to settle V5.6 | ·L5 §5.17 |

## 5.4 [added] Mobilities and intrinsic carrier densities

Used in the resistivity cross-check ·L5 §5.2. These are standard room-temperature values supplied by
this knowledge base, **not** quoted by any lesson:

$$\mathrm{Si:}\quad n_i = 1.5\times10^{10}\ \mathrm{cm^{-3}},\quad \mu_n = 1350,\ \mu_p = 480\ \mathrm{cm^2V^{-1}s^{-1}}$$

$$\mathrm{Ge:}\quad n_i = 2.5\times10^{13}\ \mathrm{cm^{-3}},\quad \mu_n = 3900,\ \mu_p = 1900\ \mathrm{cm^2V^{-1}s^{-1}}$$

> **Band-gap values.** $E_g \approx 1.1\ \mathrm{eV}$ for silicon, $\approx 5\ \mathrm{eV}$ for an
> insulator, $0$ for a conductor. **·J p7 states all three**, so unlike the position before the
> primary notes were added, these are now tier-1 content and examinable. ·RD2 p8 repeats them.
> ⚠ **JC1.15** — ·J p7 prints the unit as "ev"; it is eV.

---

# 6 · Subscript and case conventions

## 6.1 Double-subscript supply voltages

A **repeated** letter marks a **supply rail**, not a terminal-pair voltage:

$$V_{CC}\ \text{(collector supply)}\qquad V_{EE}\ \text{(emitter supply)}\qquad V_{BB}\ \text{(base supply)}$$

$$V_{DD}\ \text{(drain supply)}\qquad V_{SS}\ \text{(source supply)}\qquad V_{GG}\ \text{(gate supply)}$$

$V_{SS}$ and $V_{GG}$ are quoted as **magnitudes**, with the rail itself drawn $-V_{SS}$, $-V_{GG}$
·J p93–p94, ·L4 p9. See clash 8 for the two other things SS can mean.

## 6.2 Terminal-pair voltages

Two **different** letters mark the voltage **between two terminals**, and **the first subscript names
the more positive terminal** ·J p60, ·L3 §3.2:

$$V_{BE} = -V_{EB}\qquad V_{CB} = -V_{BC}\qquad V_{CE},\ V_{GS},\ V_{DS}$$

So $V_{BE} = +0.7\ \mathrm V$ on a forward-biased silicon NPN, and $V_{EB} = +0.7\ \mathrm V$ on a
PNP. Getting this backwards flips the sign of every bias calculation.

⚠ **JC7.5** — ·J p99 breaks the convention throughout the common-drain section, writing $V_{SD}$ and
$V_{DG}$ where $V_{DS}$ and $V_{GD}$ are meant. Both are measured *from* the drain, so the ratio
$A_v = V_{SD}/V_{GD}$ comes out numerically right; only the subscript order is wrong.

## 6.3 Voltage across a named resistor

The primary notes write **$V_{Rx}$ for the voltage across resistor $x$** — $V_{R1}$, $V_{R2}$,
$V_{R3}$, $V_{RL}$, $V_{R_2}$ ·J p13, p16, p55, p94. Read the second part of the subscript as a
component name, not as a quantity. Compare clash 12: a bare $V_R$ is a reverse voltage.

## 6.4 The $h$-parameter subscripts

| Position | What it names | Values |
|---|---|---|
| **First** | the parameter | **i** input · **r** reverse · **f** forward · **o** output |
| **Second** | the configuration | **e** common-emitter · **b** common-base · **c** common-collector |

Numeric equivalents: $h_{11} = h_i$, $h_{12} = h_r$, $h_{21} = h_f$, $h_{22} = h_o$.

**Dimensional signature.** The four parameters run $(\Omega,\ 1,\ 1,\ \mathrm S)$ — that mixture is
what "hybrid" means, and it is the fastest available check on any h-parameter expression: every term
in $V_i = h_iI_i + h_rV_o$ must come out in volts, every term in $I_o = h_fI_i + h_oV_o$ in amperes.
It is also what settles **JV6.2** (clash 9): $h_o$ cannot be a resistance.

⚠ **The two tiers set the second subscript differently.** Tier 2 uses case to separate dc from ac —
$h_{FE}$ dc, $h_{fe}$ ac. **Tier 1 sets everything upper case** ($h_{IB}$, $h_{OB}$, $h_{FB}$,
$h_{FE}$, $h_{OE}$, $h_{FC}$, $h_{RC}$) while describing small-signal quantities. Read tier 1's
symbols by what its definitions say, not by their case.

## 6.5 Upper case, lower case, and what each means

| Form | Means | Example |
|---|---|---|
| **Upper-case symbol, upper-case subscript** | a **dc** (quiescent, total average) quantity | $I_C$, $V_{CE}$, $h_{FE}$, $\beta_{dc}$ |
| **Upper-case symbol, lower-case subscript** | the **rms** value of a small-signal (ac) quantity | $I_c$, $V_b$, $h_{fe}$, $\beta_{ac}$ |
| **Lower-case symbol, lower-case subscript** | the **instantaneous** value of a small-signal quantity | $i_c$, $v_b$, $i_b$ |
| **Lower-case symbol, upper-case subscript** | total instantaneous (dc + signal) | $i_C$, $v_{BE}$ |

·J p61 tabulates exactly this scheme for $i_e/I_E/i_E$, $i_c/I_C/i_C$, $i_b/I_B/i_B$ and
$v_{be}/V_{BE}/v_{BE}$ — ⚠ **JC6.4**: its column headings are missing and its hybrid row prints
$h_{IB}$ twice where the total-instantaneous entry should be $h_{iB}$.

**Neither tier is perfectly disciplined about it.** ·L1 writes both $I_z$ and $I_Z$, and both $V_z$
and $V_Z$, for the same quantity; ·L2 writes both $V_{sm}$ and $V_{SM}$; ·J writes both $I_S$ and
$I_s$, and both $V_S$ and $V_s$. Treat a case change on a zener, rectifier or transformer symbol as
a typographical slip, and a case change on a transistor symbol as meaningful. ⚠ The one place the
case genuinely carries the meaning and is easy to miss is ·J p35's $i_o$ against $I_o$ (clash 11).

## 6.6 The BS 1852 letter-position notation ·J p11, p13

The primary notes write resistances with the multiplier letter standing in for the decimal point,
and never explain the convention:

| Written | The letter means | Value |
|---|---|---|
| 900R | R = ×1 (ohms) | $900\ \Omega$ |
| 5K8 | K = ×10³ | $5.8\ \mathrm{k\Omega}$ |
| 4K54 | K = ×10³ | $4.54\ \mathrm{k\Omega}$ |
| 7M4 | M = ×10⁶ | $7.4\ \mathrm{M\Omega}$ |

The point of it is that no decimal point can be lost in a photocopy. ⚠ It also means a **K** or an
**M** inside a resistance value is neither the kelvin nor the mutual inductance — see clash 13.
⚠ **JC2.7** — ·J p11 calls $4\mathrm K54$ "equivalent to $4.5\times10^3$"; that is a rounding to two
significant figures, not an equivalence.

## 6.7 The two $r_e$ conventions ·L7

The ac emitter resistance is quoted two ways in the same lesson, and **the question always states
which to use**:

$$r_e = \frac{25\ \mathrm{mV}}{I_E}\quad\text{·L7 p13, Ex 62.13, Ex 62.14}\qquad\qquad
r_e = \frac{50\ \mathrm{mV}}{I_E}\quad\text{·L7 p18, Ex 61.5}$$

Both come from $r_j = \eta V_T/I_E$ with $V_T = 25\ \mathrm{mV}$: the 25 mV form takes $\eta = 1$,
the 50 mV form $\eta = 2$. **Never choose one yourself** — the two differ by a factor of two, and
the gain $A = R_C/r_e$ differs by the same factor.

## 6.8 The rectifier value markers

Tier 2 marks every rectifier quantity with a bracketed suffix; **tier 1 writes the bare subscript
instead**, because its whole range concerns the load current and nothing else.

| Tier 2 marker | Tier 1 equivalent | Means |
|---|---|---|
| $(dc)$ — $V_{L(dc)}$, $I_{L(dc)}$ | $I_{dc}$, $V_{dc}$ | the **average** value over a cycle |
| $(rms)$ — $V_{r(rms)}$ | $I_{rms}$ | the root-mean-square value |
| $(ac)$ — $I_{L(ac)}$ | $I_{ac}$ | the rms of everything that is **not** dc |
| $(av)$ — $I_{D(av)}$ | — | the same as $(dc)$, used for per-diode currents |
| $(pp)$ — $V_{r(pp)}$ | $V_{pp}$ | peak-to-peak |
| upper-case **M** — $V_{LM}$, $I_{LM}$ | $V_m$, $I_m$ | the **peak** (maximum) value |
| lower-case **m** — $V_{sm}$, $V_{pm}$ | $V_m$ | also the peak value |

**M and m mean the same thing.** ·L2 uses both, sometimes on the same page. Read the letter before
them, not the case: $V_{sm}$ and $V_{SM}$ are both the peak secondary voltage.

## 6.9 Increments

Both tiers write small-signal definitions as ratios of increments, using $\Delta$ and $\delta$
interchangeably:

$$\beta_{ac} = \frac{\Delta I_C}{\Delta I_B} \qquad r_{ac} = \frac{\Delta V_D}{\Delta i_D}
\qquad g_m = \left.\frac{\delta I_D}{\delta V_{GS}}\right|_{V_{DS}}$$

They mean the same thing. **The increment symbols drop out of the render in several places** — see
the glyph tables, C3.2 and V4.3/V4.4 — and without them a slope definition reads as a ratio of
totals, which is a different and wrong quantity.

---

# 7 · Reference-tier symbols (RD1–RD4) — unverified

These come from the four lecturer-authored slide decks mapped in `_reference-decks.md`. **They are
not part of the authoritative material**, carry no verification flags, and must be labelled as
reference material whenever they are used.

| Symbol | Meaning | Unit | Where |
|---|---|---|---|
| $E_g$ | band gap | eV | ·RD2 p8 — 0 (conductor), 1.1 (Si), 5 (insulator); **also ·J p7, which is tier 1** |
| $\rho$ | resistivity of a conductor | Ω·m (µΩ·m) | ·RD2 p14, p16 — Cu 0.0172, Al 0.0265, Ag 0.0159 µΩ·m |
| $\alpha$ | **temperature coefficient of resistance** | °C⁻¹ | ·RD2 p14 — 0.0038 °C⁻¹ |
| $R_0$ | initial resistance in $R = R_0(1+\alpha\Delta T)$ | Ω | ·RD2 p14 |
| $L$, $A$ | conductor length and cross-sectional area in $R = \rho L/A$ | m, m² | ·RD2 p14; **also ·J p10** |
| $T$, $W$ | bar **thickness** and **width** in $A = T\times W$ | m | ·RD2 p15 |
| $q$, $\mu_n$, $N_D$ | electronic charge, electron mobility, donor concentration | C, m²V⁻¹s⁻¹, m⁻³ | ·RD2 p15 |
| $V_D$, $r_{dc}$ | diode terminal voltage; static dc forward resistance $V_{DQ}/I_{DQ}$ | V, Ω | ·RD3 p7, p8; **both also ·J p37** |
| $f_r$ | resonant frequency of a varactor-tuned circuit, $1/(2\pi\sqrt{LC})$ | Hz | ·RD3 p19; **also ·J p45** |

**Two cautions carried from that file:**

- ⚠ **·RD2 p15** uses $T$ for the bar **thickness** and $\Delta T$ for a **temperature** change
  **inside one equation**. Two meanings, one letter, one expression.
- ⚠ **·RD3 p7** prints Boltzmann's constant as $1.38\times10^{-28}\ \mathrm{J/K}$ — the same error
  ·J p35 makes (**JV4.2**). **Use $1.38\times10^{-23}$.**

**$\alpha$ in this course.** In the BJT and h-parameter material, $\alpha$ is **always** the
common-base current gain, $0.95$–$0.99$. The temperature-coefficient meaning belongs to **RD2 alone**
and appears in no lesson and no page of the primary notes — so the two never meet on an examinable
page. A value between 0 and 1 is a current gain; a value near $0.004\ \mathrm{^\circ C^{-1}}$ is a
temperature coefficient; and a Greek α sitting between two quantities with no equals sign is
neither — it is $\propto$ (·J p10, **JC2.5**).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
