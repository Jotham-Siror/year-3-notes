---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "Reference decks — page map"
file_role: reference-index
source: "RD1 'Analogue Electronics — Introduction', 4 pp. · RD2 'Materials Used in Electrical & Electronic Circuits', 18 pp. · RD3 'Semiconductor Diodes', 20 pp. · RD4 'The Electronic System', 17 pp."
pages: "RD1 1-4 · RD2 1-18 · RD3 1-20 · RD4 1-17 (59 pp. total)"
coverage: "59/59 pages mapped from rendered page images; no page illegible"
tier: reference
verified: false
tags: [reference-tier, slide-decks, page-map, introduction, materials, band-gap, conductors, insulators, semiconductors, resistivity, diodes, tunnel-diode, photodiode, diode-models, electronic-system, adc, dac, sensors, actuators, nyquist, von-neumann]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (as used in this file):
  [def] definition · [eq] formula worth carrying · [table] classification table ·
  [fig] the page is mostly or wholly a figure · [added] supplied here, NOT in the deck ·
  ·RD{n} p{page} = provenance (which PDF page of which reference deck) ·
  ⚠ CAUTION = something on the page that would mislead if taken at face value ·
  ⚠ ILLEGIBLE = a page that could not be read.
  These decks are NOT verified. No ⚠ VERIFY flags are issued from this file and none of
  its contents enter _verification-log.md. Notes marked ⚠ CAUTION are advisory only. -->

# Reference decks — page map

Four lecturer-authored slide decks sit alongside the seven lesson PDFs. This file makes them
**findable**. It is a map, not a transcription.

---

## 0 · How to use this file

### 0.1 These decks are reference tier

- **Lessons 1–7 are the source of truth.** Where a deck and a lesson cover the same ground, the
  lesson wins.
- **These four decks are not part of the authoritative lesson series.** They have been **mapped and
  indexed only** — not fully transcribed, **not verified**, no arithmetic re-computed, no error log.
- **Anything taught from them must be labelled as such** — "this is from the reference deck RD3, not
  from Lesson 1" — every time, without exception.
- Provenance is cited as **·RD2 p7**, meaning page 7 of reference deck RD2. Page numbers are PDF
  page numbers and match the render filenames.
- Where a page carries something that would mislead a learner if taken at face value, it is marked
  **⚠ CAUTION** at that row. Those notes are advisory. They are **not** verification flags, they
  carry no **V**/**C** identifier, and they do **not** belong in `_verification-log.md`.

### 0.2 Deck register

| Code | Deck | Pages | Overlaps a lesson? |
|---|---|---|---|
| **RD1** | *Analogue Electronics — Introduction* | 4 | No — nothing in L1–L7 covers this |
| **RD2** | *Materials Used in Electrical & Electronic Circuits* | 18 | No — supplies L1's stated prerequisite |
| **RD3** | *Semiconductor Diodes* | 20 | **Yes — same ground as Lesson 1**, see §0.3 |
| **RD4** | *The Electronic System* | 17 | No — nothing in L1–L7 covers this |

For orientation, the lesson series runs: **L1** Diodes · **L2** Rectification, clipping, clamping,
multipliers · **L3** Bipolar junction transistor · **L4** Field-effect transistors · **L5**
Fabrication of transistors / integrated circuits · **L6** BJT amplifiers (h-parameter model) ·
**L7** Feedback amplifiers.

### 0.3 The overlap with Lesson 1 — RD3 versus `11-diodes.md`

RD3 covers the same territory as Lesson 1. Read this before using either alongside the other.

**Where they agree.** On the physics that carries marks, the two are consistent:

- **The junction.** A diode conducts one way; it is p-type and n-type joined; the depletion layer is
  the same object as the potential barrier ·RD3 p1–p2 ↔ L1 §1.2.
- **Why diffusion stops.** Both say the fixed charge left behind at the junction eventually repels
  further carriers and the process self-limits ·RD3 p2 ↔ L1 §1.2.
- **Forward bias.** Anode to +, cathode to −, barrier overcome, current flows; germanium conducts at
  roughly 0.2–0.3 V, silicon at 0.6–0.7 V ·RD3 p3, p20 ↔ L1 §1.4. RD3 p20's Zener slide gives
  exactly L1's pair — silicon 0.7 V, germanium 0.3 V.
- **Reverse bias.** Depletion layer widens, only minority carriers cross, current is microamp-scale
  leakage ·RD3 p4 ↔ L1 §1.4.
- **The static characteristic.** Same shape — flat then a sharp forward knee, a flat reverse leakage
  plateau, then breakdown ·RD3 p5 ↔ L1 Fig. 52.4.
- **The diode equation.** Same equation, same ideality factor convention ($\eta = 1$ for germanium,
  $\eta = 2$ for silicon), same thermal voltage $V_T = kT/q$ ·RD3 p7 ↔ L1 §1.5.
- **The LED.** A forward-biased junction that converts electrical energy to light, built from gallium
  arsenide and gallium phosphide ·RD3 p15 ↔ L1 §1.11.
- **The Zener diode.** Uses reverse breakdown to hold a constant voltage and needs a series resistor
  to limit current ·RD3 p20 ↔ L1 §1.8.
- **The varactor.** Reverse bias widens the depletion layer, which lowers the capacitance, which is
  how it tunes ·RD3 p19 ↔ L1 §1.7.

**One agreement worth singling out.** RD3 p7 prints the diode equation with the $-1$ **outside** the
bracket:

$$i_0 = I_0\left(e^{\,V_D/\eta V_T}-1\right)$$

Lesson 1's own handout prints the $-1$ **inside** the exponent in five separate places, which
`11-diodes.md` flags as **V1.3**. RD3 is an independent corroboration that L1's correction is the
right one.

**Where RD3 adds something Lesson 1 lacks.** This is the genuine value of the deck:

1. **The tunnel diode** ·RD3 p18. Lesson 1's own gap map names tunnel diodes as a p1 syllabus item
   that **never appears in the 18 pages**. RD3 supplies definition, construction, operation and
   applications. This is the single most useful thing in any of the four decks.
2. **The photodiode** ·RD3 p13–p14. Absent from Lesson 1 entirely.
3. **The three diode models** — approximate, simplified, ideal ·RD3 p9. Lesson 1 has an equivalent
   circuit (§1.13) but no three-way model classification.
4. **A route to the operating point** ·RD3 p8. Lesson 1's gap map records that the **load line is
   missing from L1 altogether**. RD3 p8 gives the algebraic equivalent — Thévenin the circuit seen by
   the diode, then $I_D = V_{Th}/(R_L + R_{Th})$. It is not a load-line construction, but it answers
   the same question.
5. **Static (dc) forward resistance** $r_{dc} = V_{DQ}/I_{DQ}$ ·RD3 p8. Lesson 1 gives bulk, junction
   and ac resistance and a *reverse* dc resistance, but not this one.
6. **The rectifier diode as a named device type**, with the dc-output formulas ·RD3 p11–p12. That
   material belongs to Lesson 2, not Lesson 1.
7. **Two named terms Lesson 1 never uses** — **knee voltage** ·RD3 p5 and **peak inverse voltage
   (PIV)** ·RD3 p6.
8. **The varactor's other two formulas** — the parallel-plate origin $C = \varepsilon A/d$ and the
   resonance $f_r = 1/(2\pi\sqrt{LC})$ ·RD3 p19. Lesson 1 gives only the voltage law
   $C = K/\sqrt{V_R}$. The two treatments are complementary rather than competing.

**Where they appear to disagree.** In every case below, **teach Lesson 1's version**:

| # | RD3 says | Lesson 1 says | Take |
|---|---|---|---|
| 1 | Boltzmann's constant is $1.38\times10^{-28}\ \mathrm{J/K}$ ·RD3 p7 | $1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$ ·L1 p6 | **L1.** RD3's exponent is off by five orders. Used literally it gives $V_T \approx 2.6\times10^{-7}\ \mathrm{V}$ at 300 K and wrecks every diode-equation answer |
| 2 | "The movement of ions process is called diffusion" ·RD3 p2 | The ions are **fixed** lattice sites; what diffuses is the **carriers**, electrons and holes ·L1 §1.2 | **L1.** RD3's sentence inverts which population moves |
| 3 | Under forward bias "the depletion layer disappears" ·RD3 p3 | The barrier is **neutralised** and the layer **narrows** ·L1 §1.4 | **L1.** The layer thins under normal forward bias; it does not vanish |
| 4 | Breakdown is explained solely as high-speed minority electrons knocking bonded electrons loose, and the breakdown point is called PIV ·RD3 p6 | **Two** mechanisms: **Zener effect** — the field breaking covalent bonds — dominant **below 6 V**; **avalanche** — collision — dominant **above 6 V** ·L1 p8 | **L1.** RD3 describes only the avalanche half and never gives the 6 V dividing line. A question asking to distinguish the two mechanisms cannot be answered from RD3 |
| 5 | Luminosity versus forward current is drawn as a **straight line through the origin** ·RD3 p16 | Fig. 53.3(b) is a **saturating, concave-down** curve, and the handout's "directly proportional" wording is flagged as **V1.6** ·L1 p14 | **L1.** RD3's figure reproduces exactly the error L1 corrects |
| 6 | Germanium knee marked at **0.2 V** on the characteristic ·RD3 p5 | Germanium barrier **0.3 V** throughout ·L1 p5, and RD3's own p3 and p20 say 0.2–0.3 V and 0.3 V | **L1's 0.3 V**, unless a printed question says otherwise |
| 7 | Diode current written $i_0$, saturation current written $I_0$ ·RD3 p7 | Diode current $I$, saturation current $I_0$ ·L1 §1.5 | **L1.** RD3's pair differs only by letter case and is a notation trap |
| 8 | A Zener diode is "constructed by use of silicon or germanium" ·RD3 p20 | Makes no material claim | Neither states it, but practical Zeners are silicon. Do not quote RD3's germanium |

**On depth.** Where both cover a topic, **Lesson 1 is far the fuller treatment.** RD3's Zener page is
one slide; L1 §1.8–§1.10 runs to the $I_{z\,\min}$/$I_{z\,\max}$ band, the 2.4–200 V range, the
150 mW–50 W power ratings, the three-point biasing check and **seven fully worked regulator
circuits**. RD3 has no worked example anywhere in its twenty pages. Use RD3 for the devices L1 omits;
use L1 for everything L1 has.

### 0.4 RD1, RD2 and RD4 touch no lesson at all

These three sit outside the lesson series entirely — they are not thin versions of a lesson, they
are ground the seven lessons never cover:

- **RD1** defines what electronics is, contrasts an analogue signal with a digital one, and lists the
  sectors electronics is applied in. Nothing in L1–L7 does any of this; the lessons open directly at
  the p-n junction.
- **RD2** classifies materials as conductors, insulators and semiconductors by energy band gap, and
  develops the resistance law with worked numbers. **This is the prerequisite `11-diodes.md` itself
  declares** — its frontmatter lists "intrinsic and extrinsic semiconductors; donors and acceptors;
  majority and minority carriers" as assumed knowledge, and no lesson supplies it. RD2 does.
- **RD4** builds the whole signal chain — sensor, pre-filter, ADC, processor, DAC, post-filter,
  actuator — plus the Nyquist criterion, sensor and actuator taxonomies, and the von Neumann computer
  model. L5 is the nearest lesson and it starts from the integrated circuit, not the system.

**Consequence.** If a CAT asks "define an analogue signal", "state the Nyquist sampling criterion",
"classify these materials by band gap" or "sketch the blocks of an electronic system", **there is no
lesson to answer from.** These decks are the only source in the repository.

### 0.5 Legibility

**All 59 pages were legible.** No page requires a screenshot. Every page is mapped below; there are
no gaps.

---

## 1 · RD1 — *Analogue Electronics — Introduction*

**What it covers.** A four-page opener: what electronics is, the analogue/digital signal distinction,
and where electronics is applied. Definitional throughout; no mathematics, no worked numbers.

**Pages.** 4. **Cite as** ·RD1 p2.

*Note: RD1's renders are named with a single digit — `p-1.png` … `p-4.png`.*

### 1.1 Page map

| p | Heading | What is on the page |
|---|---|---|
| 1 | ANALOGUE ELECTRONICS | Definition — electronics as the study of conduction current in solids, gases, vacuum and liquids; the word split into "electron" plus "mechanics"; the ability to control electron flow given as the basis of the subject; fields named — digital computers, audio systems, communication systems, automatic control |
| 2 | Analogue Signal | [def] a signal whose amplitude changes continuously with time; characteristics — continuous, typical of nature (light, waves, voice), in use for the last 100 years. **figure: one full sine cycle on time axes, with Peak Value, Peak-to-Peak value and Period cycle arrowed and labelled, zero marked on the vertical axis** |
| 3 | Digital signal | Characteristics — does not vary with time, occurs in discrete form; produced from analogue signals by analogue-to-digital conversion; "typical of technology"; dated to about 50 years, from the invention of vacuum tubes and transistors, 1947–1950. **figure: a two-level pulse train against a time axis, the levels annotated 1, 0, 1, 0, 1** |
| 4 | Applications of electronics | Eleven sectors, each with examples — communication (satellites, robots, routers); medicine (CT, MRI); entertainment (stereos, hi-fi, mobile phones); industrial (assembly lines, 3-D printing); transport (autopilot, tracking); military (drones, missile guidance); astronomy; instrumentation; training; biometrics (fingerprint, voice, eye). Closes with a YouTube link |

⚠ CAUTION ·RD1 p3 — "They do not vary with time" is a loose way of saying a digital signal takes
discrete levels rather than a continuum of values. A digital signal plainly does change with time —
the figure on the same page shows it doing so. Read the bullet as *discrete-valued*, not *constant*.

### 1.2 Not covered anywhere in Lessons 1–7

- The definition of electronics as a discipline, and the etymology.
- **Analogue signal versus digital signal** — definition, characteristics and the two waveform
  figures. Nowhere in L1–L7.
- **Peak value, peak-to-peak value and period** as named features of a waveform.
- Analogue-to-digital conversion named as the bridge between the two (developed further in RD4).
- The application sectors of electronics.

### 1.3 Examinable-looking material

[def ·RD1 p1] **Electronics** — the study of conduction current in solids, gases, vacuum and liquids;
equivalently, the study of electrons and how they are used to perform functions. The ability to
control electron flow is the basis of the subject.

[def ·RD1 p2] An **analogue signal** is one whose amplitude changes continuously with time.

[def ·RD1 p3] A **digital signal** takes discrete values rather than a continuum, and is obtained from
an analogue signal by analogue-to-digital conversion.

[table ·RD1 p2–p3] The contrast, as the deck draws it:

| | Analogue | Digital |
|---|---|---|
| Amplitude | continuous in time | discrete levels |
| Typical of | nature — light, waves, voice | technology |
| In use for | about 100 years | about 50 years, from 1947–1950 |
| Obtained from | — | analogue, via ADC |

[fig ·RD1 p2] The three quantities labelled on the sine wave — **peak value** (zero to crest),
**peak-to-peak value** (crest to trough) and **period** (one complete cycle along the time axis).

---

## 2 · RD2 — *Materials Used in Electrical & Electronic Circuits*

**What it covers.** The three-way classification of materials — conductor, insulator, semiconductor —
by valence-electron count and energy band gap; the intrinsic/extrinsic split; p-type and n-type
doping; and the factors that set the resistance of a conductor and of a semiconductor, with four
worked resistance calculations. Alternating text slides and photo-montage slides.

**Pages.** 18. **Cite as** ·RD2 p14.

### 2.1 Page map

| p | Heading | What is on the page |
|---|---|---|
| 1 | MATERIALS USED IN ELECTRICAL & ELECTRONIC CIRCUITS | Title slide. The three types named — conductors, insulators, semiconductors. One empty bullet below |
| 2 | Conductors | [def] materials that allow current to pass. Properties — 1 to 3 electrons in the outermost shell; metallic bond; free electrons present; low resistance; conduction and valence bands overlap; $E_g = 0$ eV; resistance **increases** with temperature. Examples: all metals. **figure: energy band diagram, hatched Conduction Band and Valence Band separated by a hairline Forbidden Band** |
| 3 | Images | **figure only: photo montage of conducting materials** — aluminium, copper, graphite, steel, tap water in the upper strip; brass, aluminium, cast iron, bronze, metal sludge, steel, copper in the lower. Carries a YouTube link |
| 4 | CONDUCTORS AS APPLIED IN THE COMPUTER | **figure only: photo montage** — copper wire, PSU, motherboard, memory, mouse, printer, HDD, heat sink, CPU cooler, and a row of component terminals (resistor, electrolytic capacitor, diode, transistor, ICs, toroidal inductor, switches, LED, transformer, fuse) |
| 5 | Insulators | [def] materials that do not allow current to pass. Properties — 5 to 8 electrons in the outermost shell; covalent bonding leaving no free electrons; very large gap between conduction and valence bands; $E_g = 5$ eV; "temperature does not affect resistance". Examples: air, plastic, glass, wood, ceramic. **figure: energy band diagram with a wide clear Forbidden Band** |
| 6 | Images | **figure only: photo montage of insulators** — air, glass, wood, rubber, paper, plastic |
| 7 | INSULATORS AS APPLIED IN THE COMPUTER | **figure only: photo montage**, sub-headed "ceramic and plastic — motherboards" and "component system bodies — packaging"; same computer parts as p4 plus a laptop shell |
| 8 | Semiconductors | [def] materials with poor conductivity at low temperature and good conductivity at high temperature. Properties — 4 electrons in the outermost shell/band; covalent bonds; a moderate number of free electrons; $E_g = 1.1$ eV; medium-sized forbidden band; resistance **decreases** with temperature. Two types named: intrinsic and extrinsic. **figure: energy band diagram with a narrow Forbidden Band** |
| 9 | Intrinsic semiconductors | [def] semiconductors in their pure form, e.g. silicon, germanium; conduction by holes and electrons. **figure: covalent-bond lattice — a central Si atom sharing four electron pairs with four neighbouring Si atoms, valence electrons drawn as crosses** |
| 10 | Images | **figure only: photographs of silicon, germanium and carbon samples** |
| 11 | Extrinsic Semiconductors | [def] semiconductors to which impurities have been added by doping. Two types — p-type and n-type; the letters glossed as P = positive, N = negative |
| 12 | *P*-Type | Formed by adding **trivalent** impurities to the silicon lattice — boron (2:3 electron structure), also aluminium, gallium, indium; silicon given as 2:8:4; three boron electrons pair with four silicon electrons, leaving a deficit — a **hole**. Holes are the majority carriers, hence an **acceptor** semiconductor; electrons are minority carriers; conduction is by hole movement; holes move in the direction of conventional current; forms a negative ion on gaining electrons. **figure: lattice with a central boron atom, the missing bond arrowed "Hole"** |
| 13 | *N*-Type | Formed by adding **pentavalent** impurities — phosphorus (2:8:5), also arsenic and antimony; four of the five electrons pair with silicon, leaving one spare. Electrons are the majority carriers, hence a **donor** semiconductor; holes are minority carriers; conduction is by electron movement; electrons move opposite to conventional current; forms positive ions on losing electrons. **figures: lattice with a central phosphorus atom and a labelled Free electron; and a coloured p-n junction diagram showing neutral n-region, neutral p-region, the depletion widths $D_N$ and $D_P$, total width $D$, field $E$, and the donor/acceptor concentrations $N_D$, $N_A$** |
| 14 | Factors Affecting Resistance of a Conductor | Length ($R \propto L$), cross-sectional area ($R \propto 1/A$), resistivity $\rho$ (defined and given in $\Omega\cdot\mathrm{m}$), temperature. The relations $R = R_0(1+\alpha\Delta T)$, $R = \rho L/A$ and $R = \rho(L/A)(1+\alpha\Delta T)$. **Worked example** — $L = 10$ cm, $A = 10\ \mathrm{mm^2}$, copper and aluminium, giving $1.72\times10^{-4}\ \Omega$ and $2.65\times10^{-4}\ \Omega$. **figure: a cylindrical conductor with Area and Length dimensioned** |
| 15 | Factors Affecting Resistance of a semiconductor | The n-type resistance written as a single expression in doping and mobility (see §2.3). **figure: a rectangular slab dimensioned thickness $T$, width $w$, length $l$, beside a derivation panel — $R = \rho L/A$, $A = T\times W$, $\rho = 1/\sigma = 1/(q\mu_n N_D)$, resistivity as the reciprocal of conductivity, resistance as the reciprocal of conductance** |
| 16 | EXAMPLE | **Two worked resistance problems on silver**, $\rho_{\mathrm{ag}} = 0.0159$ in the deck's units. (i) $L = 60$ cm, $A = 0.1\ \mathrm{cm^2}$ at 20 °C giving $9.54\times10^{-4}\ \Omega$, then repeated at 100 °C with $\alpha = 0.0038$ giving $1.244\times10^{-3}\ \Omega$. (ii) $L = 30$ cm, $A = 10\ \mathrm{cm^2}$ giving $4.77\times10^{-6}\ \Omega$, then at 50 °C giving $5.68\times10^{-6}\ \Omega$ |
| 17 | SEMICONDUCTORS AS APPLIED IN THE COMPUTER | **figure only: photo montage**, sub-headed "carbon, silicon and germanium as well as p and n-type" and "component system bodies — packaging — SiO2"; same computer parts as p4 and p7 |
| 18 | SEMICONDUCTOR DEVICES | **figure only: a labelled poster of diode types** — signal, LED, IR LED, photodiode, transient voltage suppression, Zener, constant current, Schottky, Shockley, step recovery, super barrier, tunnel, varactor, PIN, point contact, gunn, crystal, avalanche, silicon controlled rectifier, LASER, vacuum, peltier. Captioned "Types of Diode" |

⚠ CAUTION ·RD2 p5 — "Temperature does not affect resistance" for insulators. Insulator resistance
also falls as temperature rises; the honest contrast the slide is reaching for is that a conductor's
resistance rises with temperature while a semiconductor's falls.

⚠ CAUTION ·RD2 p14, p16 — resistivity is printed as "$\Omega\mathbf{\mu}$m", which reads as
ohm-micrometre. The arithmetic on both pages substitutes $0.0172\times10^{-6}$, i.e. the values are
**micro-ohm-metres**, $\mu\Omega\cdot\mathrm{m}$. Same number, transposed prefix.

⚠ CAUTION ·RD2 p16 — the second problem applies $(1+\alpha\Delta T)$ with $\Delta T = 50$, treating
50 °C as the temperature *rise*, whereas the first problem correctly uses $\Delta T = 100-20 = 80$.
Check which reference temperature a question intends before copying the pattern.

### 2.2 Not covered anywhere in Lessons 1–7

Effectively the whole deck. Specifically:

- **The three-way classification of materials** — conductor / insulator / semiconductor — by valence
  electron count, bonding type and band gap.
- **Energy band diagrams** and the numerical band gaps (0 eV, 1.1 eV, 5 eV).
- **The opposite temperature coefficients** of conductors and semiconductors.
- **Intrinsic versus extrinsic semiconductors**; the covalent-bond lattice picture.
- **p-type and n-type doping** — trivalent and pentavalent impurities by name, majority and minority
  carriers, acceptor and donor terminology. *This is precisely the prerequisite `11-diodes.md`
  declares and no lesson supplies.*
- **The resistance law** $R = \rho L/A$ with the temperature correction, and its **semiconductor**
  form in terms of doping density and carrier mobility.
- **Four worked resistance calculations** — the only worked numbers in any of the four decks.
- The p-n junction drawn with $N_D$, $N_A$, $D_N$, $D_P$ ·RD2 p13 — a quantitative depletion picture
  Lesson 1 does not have.

### 2.3 Examinable-looking material

[table ·RD2 p2, p5, p8] **The classification. Learn this table.**

| | Conductor | Semiconductor | Insulator |
|---|---|---|---|
| Outer-shell electrons | 1–3 | 4 | 5–8 |
| Bonding | metallic | covalent | covalent |
| Band gap $E_g$ | $0\ \mathrm{eV}$ | $1.1\ \mathrm{eV}$ | $5\ \mathrm{eV}$ |
| Bands | conduction and valence **overlap** | narrow forbidden band | very wide forbidden band |
| Free electrons | many | moderate | none |
| Resistance with rising $T$ | **increases** | **decreases** | stated as unaffected (see caution) |
| Examples | all metals | Si, Ge, C | air, plastic, glass, wood, ceramic |

[def ·RD2 p9] **Intrinsic semiconductor** — a semiconductor in its pure form; conduction is by holes
and electrons in equal measure.

[def ·RD2 p11] **Extrinsic semiconductor** — a semiconductor to which impurities have been added by
**doping**.

[table ·RD2 p12–p13] **p-type versus n-type.**

| | p-type | n-type |
|---|---|---|
| Impurity valence | trivalent | pentavalent |
| Named dopants | boron, aluminium, gallium, indium | phosphorus, arsenic, antimony |
| Majority carrier | holes | electrons |
| Minority carrier | electrons | holes |
| Called | **acceptor** | **donor** |
| Carrier motion | with conventional current | against conventional current |

[eq ·RD2 p14] **Resistance of a conductor.**

$$R \propto L,\qquad R \propto \frac{1}{A}$$

$$\boxed{\;R = \rho\,\frac{L}{A}\;}\qquad\text{and with temperature}\qquad
\boxed{\;R = \rho\,\frac{L}{A}\left(1+\alpha\,\Delta T\right) = R_0\left(1+\alpha\,\Delta T\right)\;}$$

- $R$ — resistance, Ω · $R_0$ — initial resistance, Ω · $L$ — length, m · $A$ — cross-sectional
  area, m² · $\rho$ — resistivity, Ω·m · $\alpha$ — temperature coefficient of resistance, °C⁻¹ ·
  $\Delta T$ — temperature change, °C or K

[table ·RD2 p14, p16] **The resistivity values the deck uses** (as micro-ohm-metres):

$$\rho_{\mathrm{Cu}} = 0.0172\ \mu\Omega\cdot\mathrm{m},\qquad
\rho_{\mathrm{Al}} = 0.0265\ \mu\Omega\cdot\mathrm{m},\qquad
\rho_{\mathrm{Ag}} = 0.0159\ \mu\Omega\cdot\mathrm{m},\qquad
\alpha = 0.0038\ \mathrm{°C^{-1}}$$

and the ordering it draws from them, $R_{\mathrm{Al}} > R_{\mathrm{Cu}}$ for the same geometry.

[eq ·RD2 p15] **Resistance of an n-type semiconductor bar.**

$$\boxed{\;R = \left(\frac{1}{q\,\mu_n N_D\left(1+\alpha\,\Delta T\right)}\right)\left(\frac{L}{WT}\right)\;}$$

- $q$ — electronic charge, C · $\mu_n$ — electron mobility, m²V⁻¹s⁻¹ · $N_D$ — donor concentration,
  m⁻³ · $W$ — bar width, m · $T$ — bar thickness, m · $L$ — bar length, m

built from the two relations the same page prints:

$$\rho = \frac{1}{\sigma} = \frac{1}{q\,\mu_n N_D},\qquad A = T \times W$$

⚠ CAUTION ·RD2 p15 — $T$ is used for the bar **thickness** in the geometry and $\Delta T$ for a
**temperature** change in the same expression. Two meanings, one letter, one equation.

---

## 3 · RD3 — *Semiconductor Diodes*

**What it covers.** The p-n junction, biasing, the V/I characteristic, the diode equation, diode
parameters, three diode models, then six device types treated to a fixed template — definition,
symbol, construction, features, operation, applications. **Same ground as Lesson 1 for roughly half
its length; see §0.3 before using it.**

**Pages.** 20. **Cite as** ·RD3 p18.

### 3.1 Page map

| p | Heading | What is on the page |
|---|---|---|
| 1 | SEMICONDUCTOR DIODES | [def] a diode allows current in one direction only; made from p-type and n-type joined; the depletion layer, p-n junction and potential barrier given as three names for one thing. **figure: the diode circuit symbol with Anode and Cathode labelled, beside a P\|N block with the Depletion Layer arrowed** |
| 2 | Formation of the depletion layer | How the layer forms — electrons from the n-side fill holes on the p-side at the junction, creating positive and negative ions with no charge carriers; that region is the depletion layer, also called the potential barrier since the n-side ions sit at higher potential; the process is called diffusion; it stops when the ions repel further carriers. **figure: two block diagrams of holes and electrons either side of the junction, with the barrier potential drawn as a step and marked $V_o = 0.3\ \mathrm{V}$** |
| 3 | Biasing of a Diode — Forward bias | Anode to the supply, cathode to the negative terminal; continuous supply of electrons and holes at the junction; current flows and a bulb lights. Germanium conducts at 0.2–0.3 V, silicon at 0.6–0.7 V. **figures: two forward-bias circuits — one with the diode symbol, one with the P\|N block — each a source $V_S$ in series with the diode and a bulb** |
| 4 | Reverse Bias | Anode to negative, cathode to positive; depletion layer widens as majority carriers move away from the junction; only minority-carrier **leakage current** flows, of order microamps, too small to light the bulb. **figures: the same two circuits with the source reversed** |
| 5 | VI characteristics of a diode | Germanium conducts at 0.2 V, silicon at 0.7 V; beyond the knee, further voltage gives proportionally more current and the diode behaves as a normal conductor; the voltage at which conduction starts is the **knee voltage**; in reverse, a small **leakage current**. **figures: (i) the measurement circuit — source $V_S$, potentiometer $R_1$, series $R_2$, ammeter, voltmeter across the diode; (ii) the full four-quadrant V/I curve with separate Ge and Si forward knees at 0.2 V and 0.7 V, the reverse leakage plateau, and the breakdown voltage arrowed** |
| 6 | CONT.. | Within the diode's rating, more voltage does not change the reverse current; current is temperature-dependent; beyond the rating the diode breaks down; high-speed minority electrons detach bonded electrons, breaking down the junction; that point is the **breakdown voltage** or **peak inverse voltage (PIV)**; the electrons are called avalanche electrons; the current can destroy the diode |
| 7 | CONT.. | **Diode static equation**, with every symbol defined — diode current, temperature-dependent saturation current, diode terminal voltage, empirical constant $\eta$ (Ge = 1, Si = 2), thermal voltage $V_T = kT/q$, Boltzmann's constant, absolute temperature, electronic charge $1.6\times10^{-19}$ C. **⚠ CAUTION: $k$ is printed as $1.38\times10^{-28}\ \mathrm{J/K}$ — Lesson 1 p6 has $1.38\times10^{-23}$, which is correct** |
| 8 | DIODE PARAMETERS | dc and ac resistance named as the main parameters. **figure: circuit — source $V_S$, series $R_S$, shunt $R$, then the diode $D$ in series with load $R_L$, with $I_D$ arrowed.** Beside it, five expressions: Thévenin voltage, Thévenin resistance, diode current, static resistance $r_{dc}$, and ac resistance as change in $V_D$ over change in $i_D$ |
| 9 | DIODE MODELS | Three models named and defined — **approximate** (conducts above a given voltage, then behaves as a resistor obeying Ohm's law), **simplified** (conducts at a given voltage, behaving as a closed switch), **ideal** (conducts from 0 V) |
| 10 | Types of Diodes | Six types listed — rectifier, Zener, photodiode, LED, tunnel, varactor. States the template each will be treated to: definition, symbol, construction, features, operation, applications |
| 11 | Rectifier diode | [def] a diode that changes AC to DC. Construction — p-type and n-type, robust for high power, large in size. Operation — doping lighter than other diodes to raise power handling; always operated in forward bias. **figure: the plain diode circuit symbol** |
| 12 | Cont.. | Features — silicon, lightly doped, large. Two dc-output formulas. Applications — power supplies, receivers for demodulation. **figures: (i) half-wave rectifier — sinusoidal supply, diode, load $R_L$, with the rectified output showing no negative half-cycle; (ii) an AM detector — diode, shunt capacitor, load — with RF input, rectified signal and demodulated signal waveforms below** |
| 13 | PHOTODIODE | [def] a diode of photoconducting material such as germanium that converts light energy to electrical energy; therefore a transducer. Construction — light-sensitive p and n material, large surface area, heavily doped. Operation — always reverse-biased; a reverse voltage moves electrons from valence to conduction band, raising conductivity; these are minority carriers. **figure: the photodiode symbol — a diode with two arrows pointing in** |
| 14 | Cont.. | Factors affecting the current — light intensity, angle of incidence, applied voltage, material, surface area, doping level. Dark current defined. Applications — automatic switching, alarm circuits, fibre-optic networks, counting. **figures: reverse current against light intensity (a straight line); reverse current against reverse voltage as a family of curves at increasing light intensity; an IR-LED-and-lens intruder-beam sketch; a plastic-optical-fibre LED-to-photodiode link; a photodiode symbol and package poster** |
| 15 | LIGHT EMITTING DIODE (LED) | [def] a diode that emits light under forward voltage; a transducer converting electrical energy to light energy. Construction — gallium arsenide and gallium phosphide; colour depends on material; **gallium arsenide → red, gallium phosphide → green**. **figure: the LED symbol — a diode with two arrows pointing out** |
| 16 | CONT… | Operation — forward-bias mode; electrons in the conduction band drop to the valence band to fill holes, emitting light. Ratings — voltage 1–3 V, current given as "20 – 10 mA". Applications — digital displays such as seven-segment, power indicators, fibre-optic networks. **figure: Luminosity (mW) against forward current (mA) drawn as a straight line through the origin — ⚠ CAUTION, see §0.3 item 5** |
| 17 | Applications | **figure only: photo montage of LED applications** — coloured 5 mm LEDs, RGB strip, 100 W grow lamp, vehicle accent lighting, a full-colour matrix sign, an LED-versus-LCD graphic, a nixie-style clock |
| 18 | **TUNNEL DIODE** | [def] a diode exhibiting **negative resistance** between two points of forward voltage. Construction — very heavily doped, making the depletion layer very small, so electrons cross with minimal or no applied voltage — the **tunnelling effect**. Operation — current rises to a **peak point**, then the tunnelling effect falls off and current drops to a **valley point**, after which it rises again and the device behaves as a normal diode. Applications — oscillators, e.g. in tuning circuits; fast switches. **⚠ CAUTION: the symbol drawn is the plain diode symbol, not the standard tunnel-diode symbol** |
| 19 | VARACTOR DIODE | [def] a diode that behaves as a variable capacitor. Construction — the p and n regions act as the plates, the junction as the dielectric, the junction length as the plate separation. Operation — reverse bias only; raising the reverse voltage thickens the depletion layer and so **reduces** the capacitance, and vice versa. Applications — tuning circuits with inductors. Two formulas — parallel-plate capacitance and resonant frequency. **figures: the varactor symbol; a P\|N block with Plate, Dielectric materials and Depletion Layer labelled; capacitance falling steeply with reverse voltage** |
| 20 | Zener diode | Built from silicon or germanium; uses reverse breakdown to give a constant output voltage. Construction — doping higher than a normal diode so it breaks down without damage, and earlier, depending on its reverse rating; higher power rating. Operation — reverse-bias mode; beyond breakdown the output voltage stays constant however far the voltage rises; in forward bias it behaves as an ordinary diode (Si 0.7 V, Ge 0.3 V); needs an external series resistor to limit current. Applications — power supplies and voltage regulators. **figures: the Zener symbol with the bent cathode bar; the Zener V/I characteristic with breakdown voltage and leakage current arrowed** |

### 3.2 Not covered anywhere in Lessons 1–7

Ranked by value:

1. **Tunnel diode** ·RD3 p18 — named in Lesson 1's p1 outline, absent from all 18 of its pages, and
   absent from L2–L7. **RD3 is the only source in the repository.**
2. **Photodiode** ·RD3 p13–p14, including the dark-current relation and the six factors that set the
   photocurrent. Absent from every lesson.
3. **The three diode models** — approximate, simplified, ideal ·RD3 p9.
4. **Thévenin reduction to find the diode current** ·RD3 p8 — the algebraic counterpart of the load
   line Lesson 1 never supplies.
5. **Static forward resistance** $r_{dc} = V_{DQ}/I_{DQ}$ ·RD3 p8.
6. **"Knee voltage"** ·RD3 p5 and **"peak inverse voltage (PIV)"** ·RD3 p6 as named terms.
7. **The varactor's parallel-plate and resonance formulas** ·RD3 p19.
8. The **rectifier diode treated as a device type** with dc-output formulas ·RD3 p11–p12 — Lesson 2
   ground, not Lesson 1.

Everything else in RD3 duplicates Lesson 1, usually far more thinly.

### 3.3 Examinable-looking material

[eq ·RD3 p7] **The diode static equation**, in the deck's own notation:

$$i_0 = I_0\left(e^{\,V_D/\eta V_T}-1\right),\qquad V_T = \frac{kT}{q}$$

- $i_0$ — diode current, A *(Lesson 1 writes this $I$ — prefer that)* · $I_0$ — temperature-dependent
  saturation current, A · $V_D$ — diode terminal voltage, V · $\eta$ — empirical constant, 1 for
  germanium, 2 for silicon · $V_T$ — thermal voltage, V · $k$ — Boltzmann's constant, J K⁻¹ · $T$ —
  absolute temperature, K · $q = 1.6\times10^{-19}$ C

⚠ CAUTION ·RD3 p7 — the page prints $k = 1.38\times10^{-28}$ J/K. Use Lesson 1's
$1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$.

[eq ·RD3 p8] **Finding the operating point** — Thévenin the network the diode sees, then divide:

$$V_{TH} = V_S\,\frac{R}{R_S+R},\qquad
R_{Th} = \frac{R_S R}{R+R_S},\qquad
\boxed{\;I_D = \frac{V_{Th}}{R_L+R_{Th}}\;}$$

[eq ·RD3 p8] **The two resistances:**

$$r_{dc} = \frac{V_{DQ}}{I_{DQ}}\qquad\text{(static, at the operating point)}$$

$$r_{ac} = \frac{\Delta V_D}{\Delta i_D} = \frac{V_{D2}-V_{D1}}{i_{D2}-i_{D1}}\qquad\text{(dynamic, from two points)}$$

[def ·RD3 p9] **The three diode models.**

| Model | Behaviour |
|---|---|
| **Approximate** | conducts above a given voltage, then behaves as a **resistor** obeying Ohm's law |
| **Simplified** | conducts at a given voltage, behaving as a **closed switch** |
| **Ideal** | conducts from **0 V** |

[def ·RD3 p5] **Knee voltage** — the voltage at which a diode starts to conduct.

[def ·RD3 p6] **Peak inverse voltage (PIV)** — the reverse voltage at which the junction breaks down.

[def ·RD3 p18] **Tunnel diode** — a diode exhibiting **negative resistance** between two points of
forward voltage. Very heavily doped, so the depletion layer is very thin and carriers cross it at
minimal or zero applied voltage — the **tunnelling effect**. Its forward characteristic rises to a
**peak point**, falls to a **valley point** as tunnelling dies away, then rises again as an ordinary
diode. Used in oscillators and fast switches.

[eq ·RD3 p12] **Rectifier dc output**, as printed:

$$V_{dc} = \frac{V_{\max}}{\pi}\qquad\text{and}\qquad V_{dc} = \frac{2V_{\max}}{\pi}$$

⚠ CAUTION ·RD3 p12 — the slide does not say which is which. The first is **half-wave**, the second
**full-wave**. Confirm against Lesson 2, which owns this material.

[eq ·RD3 p14] **Photodiode dark current** — the reverse current flowing with no illumination:

$$I_R = \frac{V_R}{R_R}$$

- $I_R$ — dark current, A · $V_R$ — reverse voltage, V · $R_R$ — dark resistance, Ω

[eq ·RD3 p19] **Varactor** — the parallel-plate origin of the capacitance, and what it is used for:

$$C = \frac{\varepsilon A}{d}\qquad\text{and}\qquad \boxed{\;f_r = \frac{1}{2\pi\sqrt{LC}}\;}$$

- $C$ — junction capacitance, F · $\varepsilon$ — permittivity of the junction material, F/m · $A$ —
  effective plate area, m² · $d$ — depletion-layer width, m · $f_r$ — resonant frequency, Hz · $L$ —
  tuning inductance, H

*Raising the reverse voltage increases $d$, which lowers $C$, which raises $f_r$. Lesson 1's
$C = K/\sqrt{V_R}$ is the same physics expressed against the controlling voltage.*

[table ·RD3 p3, p5, p20] **Conduction thresholds as this deck gives them** — germanium 0.2–0.3 V,
silicon 0.6–0.7 V, with p20 settling on **Si 0.7 V, Ge 0.3 V**, which is Lesson 1's pair.

[def ·RD3 p13, p15] **Two transducers, opposite directions.** A **photodiode** converts light energy
to electrical energy and is **always reverse-biased**. An **LED** converts electrical energy to light
energy and is **always forward-biased**. Both are described as transducers on their own slides.

[table ·RD3 p15] **LED colour by material** — gallium arsenide gives red, gallium phosphide gives
green. *(Lesson 1's table ·L1 p14 is fuller and differs: it gives gallium arsenide as
**infrared/invisible**, gallium phosphide as red or green, and gallium arsenide phosphide as red or
amber. Prefer Lesson 1's.)*

---

## 4 · RD4 — *The Electronic System*

**What it covers.** The electronic system as a signal chain — sensor, pre-filter, ADC, processor,
DAC, post-filter, actuator — each block defined in turn, with taxonomies of sensors and actuators,
the Nyquist sampling criterion, worked examples of digital systems, and the von Neumann computer
model with its hardware and software breakdown. Block diagrams throughout; no circuit analysis.

**Pages.** 17. **Cite as** ·RD4 p6.

### 4.1 Page map

| p | Heading | What is on the page |
|---|---|---|
| 1 | Components of an electronic system | **figure: the master block diagram — analogue in → sensor → pre-filter → analogue-digital converter (ADC) → processor → digital-analogue converter (DAC) → post-filter → actuator → analogue out.** The whole deck expands this one chain |
| 2 | Sensors | [def] devices that detect a signal or form of energy and transform it into electrical (analogue) energy. Signal types listed — audio; electromagnetic (gamma, X-ray, UV, visible, infrared, microwave, radio); seismic; chemical (pH, battery, fuel cell); mechanical; bio-signals, electric and magnetic; water waves |
| 3 | Sensors — cont. (Tinkercad and PT) | The matching sensor for each signal type — gamma detector, X-ray detector, photodiode / LDR / phototransistor for visible, IR detector, seismometer, chemical sensors, vibration and expansion for mechanical, hydrophone for underwater sound, quartz crystal for mechanical-to-electrical; bio-signals expanded to ECG, MCG, EEG, heart rate, flow rate, ultrasonic, audio. **figure: a sensor block with a clean signal plus noise at the input and a noisy signal at the output, both labelled** |
| 4 | Other sensors | Seventeen instruments each with the quantity it measures — pressure sensor, barometer, altimeter, liquid flow sensor, gas flow sensor, accelerometer, ohmmeter, voltmeter, galvanometer, watt-hour meter, oxygen sensor, carbon dioxide detector, speedometer, Geiger counter, piezoelectric, thermocouple and thermistor |
| 5 | Pre-filter | [def] the filter at the input stage; removes noise; may be hardware (resistors, capacitors, inductors) or software (mathematical modelling of the same components). **figure: a noisy input into a FILTER block, a clean pulse out** |
| 6 | Analogue to digital converter (ADC) | [def] transforms the analogue signal to digital form by **sampling**. **Nyquist sampling theorem** stated — the sampling rate should be twice the maximum input frequency — with the formula. Consequence if not followed: the sampled signal may not be recoverable. Worked illustration of quantisation with 3 bits, maximum level 7, sample sequence 0-5-7-5-0 encoded as 000\|101\|111\|101\|000. **figures: an analogue pulse into a block, discrete samples out; the resulting binary pulse train** |
| 7 | Processor | [def] a device that performs manipulation on the digital signal; hardware or software based. Manipulations — arithmetic and logical, listed under working names: compress (scaling down), amplify (add or multiply), remove noise, compare, encode, decode, select. **figure: a sample train of amplitudes into a PROCESSOR block and a larger set out, annotated 10, 14, 10** |
| 8 | Digital to Analogue Converter (DAC) | [def] transforms the processed digital signal back to analogue; hardware or software based. Uses — signal processing, multimedia. **figure: discrete samples into a DAC block, a staircase waveform out** |
| 9 | Post filter | [def] removes the **quantization noise** introduced by the system; mostly a low-pass filter; hardware or software. **figure: a POST FILTER block with a ragged waveform above it and a smooth pulse below, annotated "If signal is strong"** |
| 10 | Actuators | [def] transforms the analogue electrical signal into another form of energy according to the application. Eleven listed with their output — speaker and buzzer (audio), ultrasonic, antenna (microwave and radio), vibrator (vibration, seismic), LED / bulb / laser / CRT (light), bio-signals, IR emitter, motor (motion), chemical actuators such as an insulin pump, galvanometer (deflection) |
| 11 | More actuators | Eight more — bimetallic strip, switches, relay, electric jack, electric hammer, comb drive, piezoelectric (artificial muscles), heating element |
| 12 | Digital System examples | Eighteen examples — mobile phone, computer, camera, gaming console, smart watch, TV, radio, smart car, robots (teacher, doctor, soldier, footballer, waiter, assistant), drone, aeroplane, wireless body network, smart city, smart building, smart home, washing machine, smart appliances. Closes with the class task, in red: **pick one system and discuss its sensors and actuators** |
| 13 | A mobile phone as an audio processing system | **figure only: the master chain instantiated** — sound (air pressure) → microphone → ADC → memory → DAC → speaker → sound (air pressure), with the signal named at each stage: air pressure, voltage, numbers, numbers, voltage, air pressure, and a small waveform drawn under each |
| 14 | Components of a Computer | The **von Neumann model**. **figure: block diagram — Input and Output either side of Memory; a Storage device above Memory with arrows both ways; below, the CPU bracket containing the ALU and the Control unit, with solid data paths and dotted control paths** |
| 15 | *(untitled)* | **figure only: a photograph of an opened desktop computer case** — PSU with its ratings label, motherboard, CPU cooler and fan, RAM slots, drive bays, ribbon and power cabling |
| 16 | Hardware | Four categories — **input devices** (mouse, keyboard, joystick, touch screen, stylus, light pen, microphone, scanner, trackball, camera); **output devices** (printers, monitors — CRT, LCD, LED — speakers, cameras, plotters); **system unit devices** (CPU with processor, ALU and control unit; motherboard, buses, memory, PSU, casing, interface cards, cables, fan and heat sink, switches, reset, LED); **storage devices** (floppy, CD-ROM, DVD-ROM, zip disk, memory card, flash disk) |
| 17 | Software | **System software** — operating systems: Windows, Linux, Unix, Mac, Novell, OS/2, Apple. **Mobile operating systems** — Android, Symbian, Apple, Windows CE; operating system and utility programs. **Application software** — interfaces the user and the operating system: SPSS, Excel, MATLAB, Access |

⚠ CAUTION ·RD4 p6 — "3 bits, max number to have is 7" is right ($2^3-1 = 7$), but the sample list is
printed as the run-together string "05750"; read it as the five samples 0, 5, 7, 5, 0, which is what
the binary line beneath encodes.

### 4.2 Not covered anywhere in Lessons 1–7

The entire deck. Specifically:

- **The electronic system as a signal chain** — the seven-block diagram ·RD4 p1 and its instantiation
  as a mobile phone ·RD4 p13. Nothing in L1–L7 takes a system-level view at all.
- **Sensors** — definition, signal-type taxonomy, and the instrument-to-quantity table ·RD4 p2–p4.
- **Actuators** — definition and taxonomy ·RD4 p10–p11.
- **The ADC and the DAC** as blocks, and **the Nyquist sampling criterion** ·RD4 p6, p8.
- **Quantisation, bit depth and quantisation noise** ·RD4 p6, p9.
- **Pre-filter versus post-filter**, and the hardware/software distinction that runs through every
  block ·RD4 p5, p9.
- **The von Neumann computer model**, and the hardware and software taxonomies ·RD4 p14, p16–p17.

L5 (*Fabrication of Transistors / Integrated Circuits*) is the nearest lesson in spirit, but it opens
at the integrated circuit and never treats the system the ICs sit in.

### 4.3 Examinable-looking material

[def ·RD4 p1] **The electronic system**, as the deck's master chain — memorise the order:

$$\text{analogue in} \to \text{sensor} \to \text{pre-filter} \to \text{ADC} \to \text{processor}
\to \text{DAC} \to \text{post-filter} \to \text{actuator} \to \text{analogue out}$$

[def ·RD4 p2] **Sensor** — a device that detects a signal or form of energy and transforms it into
electrical (analogue) energy.

[def ·RD4 p10] **Actuator** — a device that transforms the analogue electrical signal into another
form of energy, chosen to suit the application. *(Sensor and actuator are therefore the two ends of
the chain, converting in opposite directions.)*

[eq ·RD4 p6] **Nyquist sampling theorem** — the sampling rate must be at least twice the highest
frequency present in the input:

$$\boxed{\;F_s = 2f\;}$$

- $F_s$ — sampling frequency, Hz · $f$ — maximum frequency component of the input signal, Hz

If the criterion is not met, the sampled signal may not be recoverable.

[eq ·RD4 p6] **Quantisation levels from bit depth** — with $n$ bits the largest representable level is

$$2^{n}-1,\qquad\text{e.g. } n = 3 \Rightarrow 7$$

with the deck's worked encoding: samples $0,\,5,\,7,\,5,\,0$ become $000\,|\,101\,|\,111\,|\,101\,|\,000$.

[table ·RD4 p5, p9] **The two filters — know which noise each one removes.**

| | Pre-filter | Post-filter |
|---|---|---|
| Position | input stage, before the ADC | output stage, after the DAC |
| Removes | noise picked up with the signal | **quantization noise** introduced by the system itself |
| Type | hardware (R, L, C) or software | mostly **low-pass**; hardware or software |

[def ·RD4 p7] **Processor** — a device that performs arithmetic and logical manipulation on the
digital signal. The manipulations named: compress (scale down), amplify (add or multiply), remove
noise, compare, encode, decode, select.

[def ·RD4 p14] **The von Neumann model** — input and output either side of memory; a storage device
attached to memory; and a CPU comprising the **arithmetic logic unit (ALU)** and the **control unit**.

[table ·RD4 p16] **Hardware, four categories** — input devices, output devices, system unit devices,
storage devices.

[table ·RD4 p17] **Software, two categories** — **system software** (operating systems, including
mobile operating systems, plus utility programs) and **application software** (interfaces the user to
the operating system).

---

## 5 · Provenance

- **All 59 pages** — RD1 4, RD2 18, RD3 20, RD4 17 — were **rendered to images and read directly**,
  in order, one page at a time. Coverage is complete; nothing was skipped.
- **No page was illegible.** No screenshot is required. If one ever is, it will be listed here.
- **Nothing was invented.** Where a slide is a photo montage with no text, the row says so and
  describes what is shown. Where a slide carries a stray empty bullet (·RD2 p1, ·RD3 p12, ·RD3 p14,
  ·RD3 p16, ·RD3 p19), no content has been supplied to fill it.
- **No arithmetic was re-computed and no equation was verified.** This is a reference-tier index. The
  ⚠ CAUTION notes record what a page prints against what the authoritative Lesson 1 file prints; they
  are not verification flags and carry no **V**/**C** identifier.
- **Lesson 1 comparison basis.** §0.3 was written against `11-diodes.md` — its section headings, its
  symbol tables, its `[eq:]` list and its verification summary — not from memory.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
