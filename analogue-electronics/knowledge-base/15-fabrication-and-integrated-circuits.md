---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "15 — Fabrication of Transistors and Integrated Circuits (supporting)"
source: "L5 — 'Lesson 5 Fabrication of Transistors - Construction .pdf', 23 pp."
pages: "1-23"
tier: supporting
file_role: topic
subtopics:
  - "what an integrated circuit is; active vs passive components; IC vs discrete circuit"
  - "semiconductors used for IC fabrication — why silicon beats germanium and gallium arsenide"
  - "the four manufacturing stages: material preparation, crystal growth, wafer fabrication, packaging"
  - "material preparation: sand to electronic-grade polycrystalline silicon"
  - "crystal growing — the Czochralski puller; the float-zone alternative"
  - "wafer preparation: ingot grinding, primary and secondary flats, orientation and type coding"
  - "the seven wafer-fabrication processes and the planar process"
  - "oxidation — uses of SiO2, thermal oxidation system, dry vs wet oxide"
  - "etching — wet (isotropic) vs dry / reactive ion etching (anisotropic)"
  - "diffusion — pre-deposition and drive-in; doping profiles; diffusion furnace"
  - "ion implantation — equipment, six advantages and three disadvantages over diffusion"
  - "photomask generation — reticle vs mask, pattern generator, wafer stepper"
  - "photolithography — the six-step window-opening sequence; positive vs negative photoresist"
  - "epitaxy — VPE, LPE, MBE; what epitaxy can do that diffusion cannot"
  - "metallization — why aluminium; resistance heating, electron-beam heating, sputtering"
  - "testing, bonding and packaging; the through-hole and surface-mount package families"
  - "forming IC elements: diffused resistors and sheet resistance; junction, trench and stacked capacitors; diodes"
  - "the seven-mask NPN bipolar IC process, isolation tubs and the buried layer"
  - "the five-mask enhancement-mode NMOS process, LOCOS field oxide and the self-aligned poly gate"
  - "MOS vs bipolar IC technology — five comparison points and the speed caveat"
key_equations: [ic-diffused-resistor, sheet-resistance]
prerequisites: ["01-diodes (P-N junction, doping, depletion region)", "03-bipolar-junction-transistor (emitter/base/collector, NPN structure)", "04-field-effect-transistors (enhancement-mode NMOS, threshold voltage, transconductance)"]
leads_to: ["06-h-parameters-for-circuits", "operational amplifiers and analogue IC building blocks", "digital VLSI design"]
verification_flags: 21
tags: [integrated-circuits, fabrication, planar-process, czochralski, wafer, oxidation, etching, diffusion, ion-implantation, photolithography, photoresist, epitaxy, metallization, sputtering, packaging, dip, bga, sheet-resistance, buried-layer, isolation, locos, nmos, mos-vs-bipolar, descriptive]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·L5 pN = provenance (which PDF page of Lesson 5 the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be read from the render. -->

# 05 — Fabrication of Transistors and Integrated Circuits

Scope: the whole of L5, 23 PDF pages. Takes silicon from sand to a packaged chip: material
preparation, Czochralski crystal growth, wafer preparation, then the seven wafer-fabrication
processes (oxidation, etching, diffusion, ion implantation, photomask generation, photolithography,
epitaxy, metallization), then testing/bonding/packaging, and finally how each circuit element —
resistor, capacitor, diode, NPN bipolar transistor, enhancement NMOS — is actually built. Closes
with a MOS-versus-bipolar comparison, applications, and two objective-test questions.

> ## ⚠ Read this before anything else — what this lesson is, and is not
>
> **This is a descriptive lesson.** It contains **exactly one equation** (the diffused-resistor
> value, ·L5 p16), **no worked examples**, and **no tutorial problems**. The examinable content is
> therefore almost entirely: **ordered process sequences**, **definitions**, **classification
> trees**, and **advantage/disadvantage lists**. Those are reproduced here in full and in order.
>
> **Do not expect numbers to carry the marks here.** Expect "list the four stages of IC
> manufacture", "state six advantages of ion implantation over diffusion", "describe the function
> of each of the seven masks in the NPN process", "distinguish positive from negative photoresist".
> §5.24 collects every such list in one place.

**Provenance of this lesson.** L5 is not a lecture deck. Pages 1–2 are re-typeset extracts and
pages 3–23 are a scanned run of chapter pages from a printed electrical-technology textbook —
**Chapter 67, "Integrated Circuits"**, printed pages **2480–2500**, carrying its own article
numbering (67.1, 67.2, 67.13, 67.14, …), figure numbering (Fig. 67.4 … Fig. 67.29) and an
end-of-chapter objective test. Two consequences:

1. **Two page numbers exist.** Citations here use the **PDF page** (·L5 p12), which equals the
   render filename. The printed page number is given in the coverage map (§5.25) — printed page
   $= \text{PDF page} + 2477$ for PDF pages 3–23.
2. **The prose is the textbook's, so it is rewritten here in our own words.** Process step
   sequences, the lecturer's numerical values, figure content and list items are reproduced
   faithfully; long prose passages are not.

> ### ⚠ Coverage gap in the source itself — articles 67.3 to 67.12 are missing
>
> The lesson jumps from **§67.2 (·L5 p1)** straight to **§67.13 (·L5 p2)**. Articles **67.3–67.12
> are not in this PDF at all**, and **their content is therefore unknown to this file** — the pages
> that would carry them (before printed page 2480) were not supplied.
>
> **What that means in practice.** A lesson titled "Fabrication of Transistors / Integrated
> Circuits" would normally also cover **IC classification** (monolithic, hybrid, thin- and
> thick-film), the **scales of integration** (SSI, MSI, LSI, VLSI, ULSI) and the **advantages and
> disadvantages of ICs over discrete circuits**. **None of that is in L5**, and none of it is
> supplied here — the only trace is the passing mention of "LSI, VLSI and ULSI" on ·L5 p22 (§5.21,
> point 5), used but never defined. If those topics are examinable, **the missing pages are needed
> as a screenshot or scan**; nothing has been invented to fill the hole.

---

## 5.0 Symbols used in this lesson

Only §5.16 (resistors) is quantitative. Everything else is verbal, so the symbol list is short.

| Symbol | Meaning | Units | Typical value in L5 |
|---|---|---|---|
| $R$ | resistance of a diffused IC resistor | $\Omega$ | $100\ \Omega$ to several $\mathrm{k\Omega}$ ·L5 p17 |
| $\rho$ | resistivity of the diffused layer | $\Omega\!\cdot\!\mathrm{cm}$ (the lesson's unit; SI is $\Omega\!\cdot\!\mathrm{m}$) | $0.1$–$1\ \Omega\!\cdot\!\mathrm{cm}$ (epitaxial layer) ·L5 p20 |
| $l$ | length of the resistive region | cm | — |
| $w$ | width of the resistive region | cm | — |
| $d$ | depth of the resistive region | cm | — |
| $a$ | cross-sectional area of the resistive region, $a=wd$ | $\mathrm{cm}^2$ | — |
| $R_s$ | **[added]** sheet resistance, $R_s=\rho/d$ | $\Omega$ per square | $100$–$200\ \Omega/\square$ ·L5 p17 |
| $n$ | **[added]** number of squares, $n=l/w$ | dimensionless | — |
| $V_T$ | threshold voltage of the NMOS transistor | V | not numerically given ·L5 p21 |
| $g_m$ | transconductance | S (siemens) | not numerically given ·L5 p22 |
| $L$ | channel length of the finished NMOS device | m ($\mathrm{\mu m}$ in practice) | marked on Fig. 67.27 (g) ·L5 p22 |

### ⚠ Notation clashes to carry into `_nomenclature.md`

| Clash | Detail |
|---|---|
| $V_T$ | **Threshold voltage** here (·L5 p21). In `01-diodes` and `03-bipolar-junction-transistor` the same symbol is the **thermal voltage** $kT/q\approx 26\ \mathrm{mV}$, and `04-field-effect-transistors` writes threshold as $V_{GS(\mathrm{th})}$. Three files, two meanings, one symbol. |
| $l$ vs $L$ | $l$ = resistor length (·L5 p16); $L$ = MOSFET channel length (·L5 p22). Same physical dimension, different symbol, different object. |
| $a$ vs $A$ | $a$ = cross-sectional area of the resistor body (·L5 p16). Elsewhere in the KB $A$ is area and $a$ appears as an a.c. subscript. |
| $d$ | Depth of the resistive region (·L5 p16). In `04-field-effect-transistors` $d$/$D$ is the **drain** subscript. |
| $P$ | Doping type "P-type"; also the element **phosphorus** (POCl$_3$, P-glass, "P$^+$ islands"). Read from context: an italic type label vs a chemical symbol. |
| $N$ | Doping type "N-type"; also nitrogen in N$_2$ (·L5 p8). |
| LCC | Used for **two different packages** in one figure — see `C5.10`. |

---

## 5.1 What an integrated circuit is ·L5 p1 (§67.1, §67.2)

### 5.1.1 The size story, in four steps ·L5 p1

The lesson opens historically, and the sequence itself is the point.

1. **1907 — the triode** (Lee De Forest). Active components (the triode) and passive components
   (resistors, inductors, capacitors) were **separate and distinct units connected by soldered
   leads**.
2. **1948 — the transistor** (W.H. Brattain and I. Bardeen ⚠ `C5.1`). Cheaper, more reliable, less
   power-hungry and **much smaller** than an electron tube. Passive components were shrunk to match,
   making **the entire circuit very small**.
3. **Printed circuit boards (PCBs)** cut size further by removing bulky wiring and tie points.
4. **Early 1960s — microelectronics.** Driven primarily by a military requirement to cut equipment
   volume to roughly **one tenth**, this produced the **integrated circuit (IC)** — so small that
   construction is done by technicians under high-powered microscopes.

> ⚠ VERIFY **C5.1** ·L5 p1 — printed as "the invention of the transistor in 1948 by W.H. Brattain
> and **I. Bardeen**". The co-inventor is **J. Bardeen** (John Bardeen); the working point-contact
> device was demonstrated in **December 1947** and announced in 1948, which is why textbooks quote
> both years. Cosmetic: no physics depends on it, but the initial is wrong.
> See `_verification-log.md`.

### 5.1.2 Definitions ·L5 p1

[def] **Integrated circuit (IC)** — the short form the lesson gives first:

> an IC is **just a packaged electronic circuit**.

[def] **Integrated circuit (IC)** — the full form, and the one to reproduce in an exam:

> An IC is a **complete electronic circuit in which both the active and the passive components are
> fabricated on a tiny single chip of silicon**.

[def] **Active components** — those which **have the ability to produce gain**.
Examples given: **transistors and FETs**.

[def] **Passive components** — those which **do not have this ability**.
Examples given: **resistors, capacitors and inductors**.

[def] **Discrete circuit** — one **built by connecting separate components**: each component is
produced separately, then all are assembled together to make the circuit.

Two structural facts the lesson attaches to the IC definition ·L5 p1:

- ICs are produced by **the same processes used to manufacture individual transistors and diodes**.
- Inside an IC, components are **isolated from one another by isolation diffusion** within the
  crystal chip, and **interconnected by an aluminium layer that serves as the wiring**.

[table] **IC versus discrete circuit** ·L5 p1

| | Integrated circuit | Discrete circuit |
|---|---|---|
| Where components are made | all on one silicon chip, simultaneously | each component made separately |
| Assembly | none — fabricated in place | components assembled and soldered together |
| Isolation between components | isolation diffusion inside the chip | physical separation |
| Interconnection | an aluminium layer on the chip | soldered leads, PCB tracks |

### 5.1.3 Who made the first one ·L5 p1

- **J.S. Kilby**, of Texas Instruments, was **the first person to develop an integrated circuit, in
  1959** — a single monolithic silicon chip in which active and passive components were fabricated
  by successive **deposition, etching and diffusion**.
- He was **soon followed by Robert Noyce** of Fairchild, who successfully fabricated a complete IC
  **including the interconnections** on a single silicon chip.

This is directly examined — see the objective test in §5.23.

---

## 5.2 Which semiconductors are used, and why silicon wins ·L5 p2 (§67.13)

Silicon is the **premier** semiconductor for IC fabrication. The two others used are **germanium**
and **gallium arsenide (GaAs)**, and the lesson sets out exactly what each gets right and wrong.

[table] **Gallium arsenide against silicon** ·L5 p2

| GaAs advantages | GaAs problems |
|---|---|
| **Electron velocity larger than silicon** → GaAs devices are **faster** | Crystals have a **high density of defects**, limiting device performance |
| **Lower saturation electric field** → **lower power–delay product** | **More difficult to grow in single-crystal form** |
| **Lower parasitic capacitances** for devices on GaAs substrates (contributes to the speed advantage) | (silicon and germanium suffer from neither problem) |
| **Direct band gap** → makes possible functions silicon cannot do, namely **coherent and incoherent light emission** | |

[table] **Silicon against germanium** ·L5 p2

| Property | Silicon | Germanium |
|---|---|---|
| Native oxide | forms a **superior, stable SiO$_2$** with superb insulating properties — essential to device fabrication and protection | **germanium oxide is unsuited** for device applications |
| Intrinsic resistivity | $230{,}000\ \Omega\!\cdot\!\mathrm{cm}$ | $47\ \Omega\!\cdot\!\mathrm{cm}$ |
| Consequence of that resistivity | high-voltage rectifying devices and certain infrared sensing devices are practical | low resistivity **would have precluded** rectifiers with high breakdown voltages |
| Availability | abundant, as sand | — |
| Cost | cheaper | electronic-grade germanium is **now more costly than silicon** |

[added] **Numerical check on the two resistivities.** Both printed figures are consistent with the
standard room-temperature intrinsic parameters, which is a useful reassurance that the page is not
garbled. Using $\sigma = q\,n_i(\mu_n+\mu_p)$ and $\rho = 1/\sigma$:

$$\text{Si:}\quad \sigma = (1.602\times10^{-19})(1.5\times10^{10})(1350+480) = 4.40\times10^{-6}\ \mathrm{S/cm}$$

$$\rho_{\mathrm{Si}} = 2.27\times10^{5}\ \Omega\!\cdot\!\mathrm{cm} \approx 230{,}000\ \Omega\!\cdot\!\mathrm{cm}\ \checkmark$$

$$\text{Ge:}\quad \sigma = (1.602\times10^{-19})(2.5\times10^{13})(3900+1900) = 2.32\times10^{-2}\ \mathrm{S/cm}$$

$$\rho_{\mathrm{Ge}} = 43\ \Omega\!\cdot\!\mathrm{cm} \approx 47\ \Omega\!\cdot\!\mathrm{cm}\ \checkmark$$

- $q$ — electronic charge, $1.602\times10^{-19}\ \mathrm{C}$
- $n_i$ — intrinsic carrier concentration, $\mathrm{cm^{-3}}$
- $\mu_n,\ \mu_p$ — electron and hole mobilities, $\mathrm{cm^2\,V^{-1}s^{-1}}$

Both agree with the page to within the spread of published $n_i$ and mobility values. **The ratio is
the memorable part: intrinsic silicon is about 5000 times more resistive than intrinsic germanium.**

[table] **Other semiconductors named, and what they are used for** ·L5 p2

| Material | Used for |
|---|---|
| Gallium phosphide (GaP) | high-speed devices; light emission/absorption — lasers and LEDs |
| Gallium nitride (GaN) | high-speed devices; light emission/absorption — lasers and LEDs |
| Gallium arsenide (GaAs) | high-speed devices; light emission/absorption — lasers and LEDs |
| Zinc sulphide (ZnS) | **fluorescent material**, e.g. television screens |
| Indium antimonide (InSb) ⚠ `C5.2` | **light detectors** |
| Cadmium selenide (CdSe) | **light detectors** |

> ⚠ VERIFY **C5.2** ·L5 p2 — printed as "**In Sb** and CdSe are used as light detectors". The
> compound is **indium antimonide, InSb** — a stray space has split the formula, making it read as
> two separate elements (indium and antimony). Cosmetic typesetting fault.
> See `_verification-log.md`.

---

## 5.3 How ICs are made — the four stages ·L5 p2–p3 (§67.14, Fig. 67.4)

[fig ·L5 p3, Fig. 67.4] A single left-to-right chain of four boxes joined by arrows, no branches:

$$\boxed{\text{Material preparation}} \rightarrow \boxed{\text{Crystal growing and wafer preparation}} \rightarrow \boxed{\text{Wafer fabrication}} \rightarrow \boxed{\text{Testing, bonding and packaging}}$$

[table] **The four distinct stages of IC manufacture** ·L5 p2 (§67.14) — *learn this order*

| # | Stage | Covered in | Article |
|---|---|---|---|
| 1 | **Material preparation** | §5.4 | 67.15 |
| 2 | **Crystal growing and wafer preparation** | §5.5 | 67.16 |
| 3 | **Wafer fabrication** | §5.6–§5.14 | 67.17–67.25 |
| 4 | **Testing, bonding and packaging** | §5.15 | 67.26 |

---

## 5.4 Stage 1 — material preparation: sand to polysilicon ·L5 p3 (§67.15)

Silicon **is not found as an element in nature**. It is found abundantly as **silicon dioxide**,
commonly as **quartz or sand**, which the page says constitutes about **20 % of the earth's crust**
(⚠ `C5.3`).

[fig ·L5 p3, Fig. 67.5] A four-stage pictorial chain, left to right, on a single ground line:

1. a **mound of loose grains** — labelled *Silicon dioxide (Sand)*;
2. a **gas cylinder** with a valve on top — labelled *Silicon containing Gas*;
3. a **tall reactor vessel** — a rectangular housing with a rounded column inside and a small
   spherical vessel on a stalk above it — labelled *Silicon reactor*;
4. a **heap of irregular chunks** — labelled *Polycrystalline silicon*.

Heavy arrows link each stage to the next.

[table] **Material-preparation sequence** ·L5 p3

| Step | What happens | Result |
|---|---|---|
| 1 | Sand (SiO$_2$) is reacted with **a gas produced by burning carbon** — coal, coke and wood chips | silicon of **98 % purity** |
| 2 | That silicon is **further purified in a reactor** | **electronic-grade polycrystalline silicon** |

> ⚠ VERIFY **C5.3** ·L5 p3 — printed as "silicon dioxide, which constitutes about **20 %** of
> earth's crust". The standard crustal abundances by mass are oxygen $\approx 47\ \%$ and silicon
> $\approx 28\ \%$, which makes the **silica-equivalent share about 59 %**; **free silica** (quartz
> and its polymorphs, as opposed to silicates) is about **12 %**. The printed 20 % matches neither
> figure. Cosmetic: nothing else in the lesson depends on the number, but it should not be quoted
> as fact. See `_verification-log.md`.

---

## 5.5 Stage 2 — crystal growing and wafer preparation ·L5 p3–p5 (§67.16)

### 5.5.1 Why a single crystal is needed ·L5 p3

Polycrystalline silicon is made of **many small crystals of random orientation containing many
defects**. For IC fabrication the silicon must be **nearly perfect and crystalline**, so single
crystals must be produced. That is done by **crystal growth**.

[table] **The two crystal-growth methods** ·L5 p3

| Method | What it is used for |
|---|---|
| **Czochralski process** | prepares **virtually all** the silicon used for IC fabrication |
| **Float-zone process** (printed "flat zone" ⚠ `V5.1`) | prepares crystals for fabricating **high-power, high-voltage** semiconductor devices |

> ⚠ VERIFY **V5.1** ·L5 p3 — printed **twice** as the "**flat zone** process". The method is the
> **float-zone (FZ) process**: a narrow molten zone is *floated* along a vertical polycrystalline
> rod by an RF coil, with **no crucible touching the melt** — which is precisely why it yields the
> ultra-pure, high-resistivity silicon that high-voltage, high-power devices need. "Flat zone" is
> not the name of any process. Substantive because a reader who memorises the printed form learns
> the wrong term and loses the reason behind the method.
> $$\boxed{\;\text{float-zone (FZ) process: crucible-free, ultra-pure, high-power/high-voltage silicon}\;}$$
> See `_verification-log.md`.

### 5.5.2 The Czochralski puller ·L5 p3–p4, Fig. 67.6

[table] **The three main components of the puller** ·L5 p3

| # | Component | Contains |
|---|---|---|
| (i) | **Furnace** | quartz crucible, a **rotation mechanism (clockwise)**, and a **radio-frequency (RF) heating element** |
| (ii) | **Crystal pulling mechanism** | seed holder and a **rotation mechanism (counter-clockwise)** |
| (iii) | **Ambient control** | **argon gas source**, flow control, exhaust system |

In addition the puller carries a **computer system** controlling **temperature, crystal diameter,
pull rate and rotation speed**.

[fig ·L5 p4, Fig. 67.6] Vertical cross-section of the puller, drawn symmetrically about a vertical
axis. From the top down:

- an upward arrow at the very top labelled **"Pull direction"**, and beside it a circular arrow
  labelled **"Pull and rotate CCW"**;
- a **seed holder** — a small cup gripping the top of the crystal (arrow-labelled from the left);
- immediately below it the **seed** (arrow-labelled from the right) — a short narrow neck;
- the neck flares outward into a wide vertical cylinder labelled **"Solid single crystal"** (the
  ingot), whose lower end dips into the melt;
- the line where ingot meets melt is arrow-labelled **"Solid–liquid interface"** from the left;
- a **quartz crucible** drawn in hatched section (walls and base), holding **"Melted silicon"**
  shown as horizontal dashed lines;
- **RF heating coil** drawn as two vertical columns of small circles, one outside each crucible wall
  (arrow-labelled on the right);
- beneath the crucible, a stem with a circular arrow labelled **CW** and an arrow labelled
  **"Rotate and lift"**.

**Key geometry to reproduce: seed and crystal rotate counter-clockwise and are pulled up; the
crucible rotates clockwise, i.e. in the opposite direction, and is lifted.**

### 5.5.3 Growing the ingot — the ordered sequence ·L5 p3–p4

1. Polycrystalline silicon is placed in the crucible.
2. The furnace is heated to **1690 K**, slightly above silicon's melting point of **1685 K**.
3. A **precisely controlled amount of dopant — boron or phosphorus — is added to the melt**, making
   the silicon P-type or N-type.
4. A **suitably oriented seed crystal** (a small, highly perfect crystal) is suspended over the
   crucible in the seed holder.
5. The seed is **inserted into the melt** and a small portion of it is allowed to melt.
6. The seed is **rotated and pulled up very slowly** while the crucible **rotates in the opposite
   direction**.
7. Molten silicon attaches to the seed and **becomes identical to the seed in structure and
   orientation**; as the seed rises, the attached material **solidifies (freezes)** with the seed's
   crystal structure, and a larger crystal forms.
8. **Cylindrical single-crystal bars — ingots — are produced.**
9. **Diameter is set by controlling both the temperature and the pulling speed.**
10. In the **final step**, when the bulk of the melt has been grown, the **crystal diameter is
    decreased until there is only point contact with the melt**.
11. The ingot is **cooled and removed**, to be made into thin discs called **wafers**.

[table] **Ingot and melt data** ·L5 p3–p4

| Quantity | Value |
|---|---|
| Furnace temperature | $1690\ \mathrm{K}$ |
| Melting point of silicon | $1685\ \mathrm{K}$ ($\approx 1412\ ^\circ\mathrm{C}$) |
| Melt dopants | **boron** (→ P-type) or **phosphorus** (→ N-type) |
| Ambient gas | **argon** |
| Ingot diameter | **as large as 200 mm**, latest approaching **300 mm** |
| Ingot length | of the order of **1000 mm** |

> ⚠ VERIFY **C5.4** ·L5 p4 — printed as "The **seet** is rotated and pulled up very slowly". Reads
> **seed**. Cosmetic OCR/typesetting fault; the same sentence uses "seed" correctly twice.
> See `_verification-log.md`.

### 5.5.4 Wafer preparation ·L5 p4

Ordered steps as printed:

1. The **ingot surface is ground throughout to an exact diameter** (⚠ `C5.5`) and the **top and
   bottom portions are cut off**.
2. **One or more flat regions are ground along the length of the ingot.** These flats mark the
   **crystal orientation** and the **conductivity type** (P or N).
3. The ingot is **sliced into wafers by a high-speed diamond saw**. Wafer thickness after slicing:
   **0.4 to 1.0 mm**.
4. **Both sides are lapped** to a flatness uniformity **within 2 µm**.
5. Lapping leaves the surface and edges **damaged and contaminated**; this is removed by **chemical
   etching**.
6. The wafer surface is **polished to a mirror-like finish**.
7. The wafers are **cleaned, rinsed and dried** ready for IC fabrication.

The lesson notes the final wafer thickness is **about one-third less than after slicing**.

> ⚠ VERIFY **C5.5** ·L5 p4 — printed as "the ingot surface is **grounded** throughout to an exact
> diameter". The intended word is **ground** (machined down), not *grounded* (connected to earth) —
> an unfortunate homograph in an electronics text. Cosmetic.
> See `_verification-log.md`.

### 5.5.5 The flats code — orientation and type ·L5 p4–p5, Fig. 67.7

[def] **Primary flat** — the **larger** flat. It lets a **mechanical locator** in automatic
processing equipment **position the wafer and orient the devices relative to the crystal** in a
specific manner.

[def] **Secondary flat** — the **smaller** flat. Its **angular position relative to the primary flat
identifies the orientation and conductivity type** of the crystal.

[fig ·L5 p5, Fig. 67.7] Four circles (plan views of a wafer), each with a straight chord cut into
the **right-hand** edge — the **primary flat**, dimensioned by a vertical double arrow beside it.
The four panels differ only in where the **secondary flat** sits:

- **(a) {111} P-type** — **no secondary flat at all**; only the primary flat on the right.
- **(b) {111} N-type** — secondary flat on the **lower-right**, with a **45°** angle arc drawn from
  the primary flat, labelled *45°*; the secondary chord is arrow-labelled *Secondary flat*.
- **(c) {100} P-type** — secondary flat on the **bottom**, with a **90°** angle arc from the primary
  flat, labelled *90°*; secondary chord labelled below.
- **(d) {100} N-type** — secondary flat on the **left**, directly opposite the primary, with a
  **180°** arc drawn across the top of the circle, labelled *180°*.

[table] **⭑ The wafer flats code** ·L5 p4–p5 — *the single most quotable table in §5.5*

| Angle of secondary flat from primary | Orientation | Type | Fig. 67.7 panel |
|---|---|---|---|
| **none** (primary and secondary superimposed) | **{111}** | **P** | (a) |
| **45°** | **{111}** | **N** | (b) |
| **90°** | **{100}** | **P** | (c) |
| **180°** | **{100}** | **N** | (d) |

[table] **Which orientation goes with which technology** ·L5 p5

| Wafer orientation | Used for |
|---|---|
| **{111}** | ICs made with **bipolar transistor** technology |
| **{100}** | **metal-oxide semiconductor (MOS)** circuits |

The **choice of conductivity type** (P or N) depends on the **actual process** used to fabricate
the ICs. The page cross-refers to Art. 50.16 of the parent textbook for crystal orientation itself,
which **is not part of L5** — treat crystal-plane notation as assumed knowledge here.

> ⚠ VERIFY **C5.6** ·L5 p5 — in Fig. 67.7 the upper two panels are labelled "(a) {111} P-type" and
> "(b) {111} N-type", but the lower two are captioned only "{100} P-type" and "{100} N-type" — the
> **"(c)" and "(d)" panel letters are missing**, although the running text on ·L5 p4 refers to
> "Fig. 67.7 (c)" and "Fig. 67.7 (d)". Cosmetic, but it makes the cross-references dangle.
> See `_verification-log.md`.

---

## 5.6 Stage 3 — wafer fabrication: the seven processes ·L5 p5 (§67.17)

[table] **⭑ The seven categories of wafer-fabrication process** ·L5 p5 — *learn as a list*

| # | Process | Treated in |
|---|---|---|
| (i) | **Oxidation** | §5.7 |
| (ii) | **Etching** | §5.8 |
| (iii) | **Diffusion** | §5.9 |
| (iv) | **Ion implantation** | §5.10 |
| (v) | **Photolithography** | §5.12 (with photomask generation, §5.11) |
| (vi) | **Epitaxy** | §5.13 |
| (vii) | **Metallization and interconnections** | §5.14 |

[def] **Planar process** ·L5 p5 — the basic fabrication process: one **in which the introduction of
impurities and the metallic interconnections are carried out from the top of the wafer**.

**Major advantage of the planar process:** *each fabrication step is applied to all identical
circuits, and to each of many wafers, at the same time.* That single sentence is the economic
argument for the whole of IC manufacture.

Two environmental requirements stated up front ·L5 p5:

- an **extremely clean environment**;
- **precise control of temperature and humidity**.

---

## 5.7 Oxidation ·L5 p6–p7 (§67.18)

[def] **Oxidation** — **growing a thin film of silicon dioxide (SiO$_2$) on the surface of a silicon
wafer**.

[table] **⭑ The four uses of silicon dioxide** ·L5 p6 — *a standard list question*

| # | Use |
|---|---|
| 1 | to serve as a **mask** against implant or diffusion of dopant into silicon |
| 2 | to provide **surface passivation** |
| 3 | to **isolate one device from another** |
| 4 | to act as a **component in MOS structures** (the gate dielectric) |

**Why SiO$_2$ works as a mask** ·L5 p6: the common silicon dopants — **boron, phosphorus, arsenic
and antimony** — have **very low diffusion coefficients in silicon dioxide** (they diffuse through
it with great difficulty), while **the same dopants diffuse easily when the surface is silicon**.
So the oxide shields against dopant infiltration.

[fig ·L5 p6, Fig. 67.8] A three-dimensional block drawn in oblique projection. The block is
**silicon substrate** (labelled inside its body). Across the top sits a **thin slab labelled
SiO$_2$**. Two arrows point to the top region: one from the left to the **top face**, labelled
*SiO$_2$ surface*; one from the right, curving down to a **dashed line drawn part-way down inside
the oxide slab**, labelled *Original silicon surface*.

> **[added] Read that dashed line carefully — it is the whole point of the figure.** The original
> silicon surface lies **inside** the grown oxide, not at its top. Thermal oxidation **consumes
> silicon**: the wafer surface moves downwards as the oxide grows, so a grown oxide sits partly
> below and partly above the level the bare silicon started at. That is what distinguishes a
> *grown* oxide from a *deposited* one.

[table] **Techniques for forming oxide layers** ·L5 p6

| Technique | Note |
|---|---|
| **Thermal oxidation** | **the more commonly used technique in IC processing** |
| Vapour-phase technique — **chemical vapour deposition (CVD)** | — |
| **Plasma oxidation** | — |

### 5.7.1 The thermal oxidation system ·L5 p6, Fig. 67.9

[fig ·L5 p6, Fig. 67.9] Horizontal cross-section of a tube furnace. A long **quartz furnace tube**
runs left to right, tapering at both ends. **O$_2$ or H$_2$O + carrier gas** enters at the left
through a narrow neck (arrow in); a **vent** leaves at the right. Inside the wide central section a
**quartz boat** carries a row of **silicon wafers standing vertically**, drawn as a series of short
parallel vertical strokes. Above and below the central section run two long horizontal rows of small
circles, arrow-labelled **resistance heaters**.

**Sequence** ·L5 p6:

1. Silicon wafers are placed **vertically** into a **quartz boat** in a **quartz tube**.
2. The boat is **slowly passed through a resistance-heated furnace**, in the presence of oxygen,
   at about **1000 °C**.
3. The oxidising agent is either **dry** (dry oxygen) or **wet** (a mixture of water vapour and
   oxygen) (⚠ `C5.7`).
4. A **computer controls the whole operation** — gas-flow sequence, automatic insertion and removal
   of wafers, and furnace temperature.

[table] **⭑ Dry versus wet oxidation** ·L5 p6

| | **Dry oxidation** | **Wet oxidation** |
|---|---|---|
| Oxidising agent | dry oxygen | water vapour + oxygen |
| Growth rate | **much slower** | faster |
| Film quality | **excellent electrical properties** | — |
| Used for | **thin oxides**, e.g. MOSFET **gate oxide (typically 10 nm)** | **thicker oxides ($\geq 500$ nm)**, e.g. **field oxides** in MOS ICs and for **bipolar devices** |
| Purpose served | gate dielectric | provides both **isolation and passivation** |

> ⚠ VERIFY **C5.7** ·L5 p6 — printed as "The oxidizing agent may be *dry* by using dry oxygen **or
> be using** a mixture of water vapour and oxygen". The word **wet** has dropped out; it should read
> "or **wet** by using a mixture of water vapour and oxygen". The defect matters because **the
> dry/wet pair is then used two sentences later, and in the following paragraph, without ever being
> named** — a reader meeting "wet oxidation is used" has not been told what wet oxidation is.
> Cosmetic (a dropped word), but repair it when reading.
> See `_verification-log.md`.

### 5.7.2 After the oxide is grown ·L5 p7

- The oxide is **selectively removed (etched)** from those surfaces where impurities are to be
  introduced.
- It is **kept as a shield** over the silicon where **no dopants are to be allowed**.
- Oxide layers are **relatively free from defects** and give **stable, reliable electrical
  properties**.

---

## 5.8 Etching ·L5 p7 (§67.19)

[def] **Etching** — the **selective removal of regions of a semiconductor, metal or silicon
dioxide**. There are **two types: wet and dry**.

### 5.8.1 Wet etching ·L5 p7

- The wafers are **immersed in a chemical solution at a predetermined temperature**.
- Material is **removed equally in all directions — etching is isotropic**.
- **Consequence:** some material is etched away **from regions where it was meant to be left**.
- **This becomes a serious problem when dealing with small dimensions.**

### 5.8.2 Dry (plasma) etching ·L5 p7

Mechanism, in the order the page gives it:

1. The wafers are **immersed in a gaseous plasma** created by a **radio-frequency electric field**
   applied to a gas such as **argon**.
2. The gas **breaks down and becomes ionised**. **Electrons are initially released by field
   emission.**
3. Those electrons **gain kinetic energy from the field**, collide with gas molecules and transfer
   energy, **generating further ions and electrons**.
4. The newly generated electrons collide with more gas molecules — **the avalanche process
   continues throughout the gas, forming plasma**.
5. The wafer sits **on an electrode** and its surface is **bombarded by gas ions**.
6. **Transfer of momentum from the ions to the atoms removes atoms at or near the surface.**

[def] **Reactive ion etching (RIE)** — the other name for dry etching. It is **directional
(anisotropic)**: material is removed **only from those regions where removal is required**.

**Most modern processes use only dry etching**, to produce the **fine line patterns needed for VLSI
integrated circuits.**

[table] **⭑ Wet versus dry etching** ·L5 p7

| | **Wet etching** | **Dry (plasma) etching / RIE** |
|---|---|---|
| Medium | chemical solution, wafers immersed | gaseous plasma, RF field, e.g. argon |
| Directionality | **isotropic** — equal in all directions | **anisotropic** — directional |
| Removal mechanism | chemical dissolution | **momentum transfer** from ion bombardment |
| Side effect | undercuts; removes material where it should be left | pattern edges preserved |
| Suitability | poor at small dimensions | **fine line patterns for VLSI** |
| Current practice | — | **most modern processes use only dry etching** |

---

## 5.9 Diffusion ·L5 p7–p8 (§67.20)

[def] **Diffusion** — the **introduction of impurities into selected regions of a wafer to form
junctions**. It occurs in **two steps**.

[table] **⭑ The two steps of diffusion** ·L5 p7–p8

| Step | What it does | Temperature | Dopant introduced? | Result |
|---|---|---|---|---|
| **1. Pre-deposition** | a **high concentration of dopant atoms is introduced at the silicon surface** by a vapour containing the dopant | **1000 °C** | **yes** | a **shallow but heavily doped** layer near the surface |
| **2. Drive-in diffusion** | drives the impurity atoms **deeper**, **without adding any more impurities** | **about 1100 °C** | **no** | deeper junction, **lower** surface concentration |

The page notes that **ion implantation is now used as a more accurate method of pre-deposition**.

### 5.9.1 The doping-profile graph ·L5 p7, Fig. 67.10

[fig ·L5 p7, Fig. 67.10] A single set of axes. Vertical axis, arrow upward, labelled **"Impurity
concentration"**; horizontal axis, arrow rightward, labelled **"Depth into substrate"**. Origin
marked **O**. Two curves, both starting on the vertical axis and falling monotonically:

- the **upper starting point is A**; from A a **steep curve** falls quickly and meets the horizontal
  axis at **C**, close to the origin. It is arrow-labelled **"Predeposition"**.
- the **lower starting point is B** (below A on the same axis); from B a **shallower curve** falls
  gradually, **crossing the pre-deposition curve**, and meets the axis much further out at **D**.
  It is arrow-labelled **"Drive-in-diffusion"**.
- A **horizontal dashed line** runs across at a low concentration, arrow-labelled **"P-substrate"** —
  the background substrate doping level. The drive-in curve crosses it just before D.

[table] **⭑ Reading Fig. 67.10** ·L5 p7

| Segment | Meaning |
|---|---|
| $OA$ | surface impurity concentration **after pre-deposition** — the higher one |
| $OB$ | surface impurity concentration **after drive-in** — concentration has **dropped** from $OA$ to $OB$ |
| $OC$ | depth reached **after pre-deposition** — shallow |
| $OD$ | depth reached **after drive-in** — **increased** from $OC$ to $OD$, as required |

Two properties the page states about the profiles:

- **impurity concentration decreases monotonically from the surface** into the substrate;
- **the profile of the dopant distribution is determined mainly by the temperature and the diffusion
  time.**

> **[added] The one-sentence physics of drive-in.** No dopant is added, so the total dose is fixed;
> spreading that same dose over a greater depth must lower the surface concentration. That is why
> $OB < OA$ *and* $OD > OC$ happen together, and why the two curves in Fig. 67.10 must cross.

**Junction depth control** ·L5 p8: by **precise control of time and temperature**, junction depths
of **a fraction of a micron** can be obtained.

[table] **Common dopants** ·L5 p7

| Layer type | Dopants named |
|---|---|
| **P-type** | **boron** |
| **N-type** | **phosphorus, antimony, arsenic** |

The page adds that **diffusion is rarely performed using the pure elements**; **compounds** are used
instead, and impurities may be introduced from **solid, liquid or gaseous** substances.

### 5.9.2 The diffusion furnace ·L5 p8, Fig. 67.11

[fig ·L5 p8, Fig. 67.11] Horizontal cross-section, similar in layout to the oxidation furnace but
with a gas-source manifold on the left. From the left: two horizontal inlet pipes, the upper
arrow-labelled **N$_2$**, feeding a small **quartz tube** which dips into a rounded vessel of
**liquid impurity source** (drawn shaded, at the bottom left); a second riser labelled **O$_2$**
enters from below. These join the main **quartz furnace tube**, which widens into the hot zone and
narrows again to a **vent** at the right. **End caps** are arrow-labelled at the right. Inside the
hot zone a **quartz boat** carries **silicon wafers** standing vertically (a row of short vertical
strokes). **Resistance heaters** are drawn as two long rows of small circles above and below the hot
zone.

**Sequence for a phosphorus diffusion** ·L5 p8:

1. Wafers are placed in a **quartz boat inside a quartz furnace tube**; the furnace is **heated by
   resistance heaters** surrounding it.
2. **Phosphorus oxychloride, POCl$_3$**, is placed in a container **either inside the quartz tube in
   a relatively low-temperature region, or outside the furnace** at a temperature that keeps it
   **liquid**. (**For a P-type dopant, boron is used.**)
3. The **proper vapour pressure is maintained by controlling the temperature**.
4. **Nitrogen and oxygen gas are passed over the container.**
5. These gases **react with the silicon**, forming a surface layer **containing silicon, oxygen and
   phosphorus**.
6. At the furnace's high temperature, **phosphorus diffuses easily into the silicon**.
7. **Drive-in follows**, at about **1100 °C**, in a similar furnace **with no dopant introduced**.

### 5.9.3 Selective diffusion through an oxide window ·L5 p8, Fig. 67.12

[fig ·L5 p8, Fig. 67.12] Two stacked cross-sections.

- **Upper panel — before diffusion.** A thick hatched block labelled **P-type silicon**. On top of
  it, a **silicon dioxide layer drawn as two horizontal strips with a gap between them** — the
  window. A row of **dots** (the **phosphorus dopant atoms deposited**, arrow-labelled from above
  with three arrows) lies along the top of both oxide strips **and** down inside the window directly
  on the silicon.
- **Lower panel — after diffusion.** The same two oxide strips (labelled **SiO$_2$**), and beneath
  the window a **bowl-shaped (U-shaped) hatched region** that extends **downwards into the silicon
  and slightly sideways under both oxide edges**. Arrow-labelled **"Dopant atoms diffuse in silicon
  but not in SiO$_2$"**.

> **[added] Two things to redraw correctly.** (1) The diffused region is **rounded**, not
> rectangular, and it **undercuts the oxide edges** — lateral diffusion is roughly comparable to
> vertical diffusion, which is one reason diffused geometries cannot be made arbitrarily small.
> (2) Dopant lands everywhere, but only penetrates through the window; the oxide is the mask, which
> is use 1 of SiO$_2$ from §5.7.

---

## 5.10 Ion implantation ·L5 p8–p9 (§67.21)

[def] **Ion implantation** — introducing dopants into **selected areas of the wafer surface by
bombarding the surface with high-energy ions of the particular dopant**.

### 5.10.1 How the machine works ·L5 p8–p9, Fig. 67.13

**Sequence** ·L5 p8–p9:

1. To generate ions — of phosphorus, say — an **arc discharge** is struck in a gas containing the
   dopant, e.g. **phosphine (PH$_3$)**.
2. The ions are **accelerated in an electric field** to about **20 keV**.
3. They are **passed through a strong magnetic field** (the analysing magnet, which selects the
   wanted species).
4. They are **further accelerated** until their energy reaches **several hundred keV or MeV**.
5. They are **focused onto, and strike, the surface of the silicon wafer**.
6. As with diffusion, the beam reaches **only selected regions**, by **masking**.
7. On entering the wafer, the ions **collide with silicon atoms and lose their energy**.

[table] **Penetration data** ·L5 p9

| Quantity | Value / rule |
|---|---|
| Depth of penetration | **0.1 to 1 µm** |
| Depth increases with | **higher ion energy** and **smaller ion mass** |

[fig ·L5 p9, Fig. 67.13] A schematic beamline drawn left to right, with the beam envelope shown as
two lines converging and diverging about a horizontal dashed axis.

- Bottom left: a box labelled **Ion source**, fed from a supply box labelled **20 kV**, with a
  **terminal ground** symbol beside it.
- Above the source, a large quarter-circle bend arrow-labelled **90° analyzing magnet**; the beam
  turns from vertical to horizontal through it. A curved plate at the exit is labelled **Resolving
  aperture**.
- The horizontal beam then passes between **two horizontal cylinders drawn as stacks of rings** —
  the **acceleration tube** — driven by a supply box labelled **"180 KV"** with **+** on the left
  and **−** on the right (⚠ `C5.9`), with an **equipment ground** symbol arrow-labelled above.
- Next a vertical rectangle labelled **Focus**.
- Then a short tilted bar labelled **Neutral beam trap and beam gate**.
- Then a large tilted rectangle labelled **Y-axis scanner**, followed by a tilted plate labelled
  **Beam trap and gate plate**, and further tilted plates labelled **X-axis scanner**.
- The dashed straight-through path continues to the right, arrow-labelled **Neutral beam and beam
  path gated**; the deflected beam ends on a tilted plate at the far right labelled **Wafer in wafer
  process chamber**.
- A separate box at the bottom centre is labelled **Vacuum system**.

> **[added] Sanity check on the two voltages.** A **singly charged** ion falling through $V$ gains
> energy $qV$, i.e. $\;E[\mathrm{eV}] = V[\mathrm{volts}]$ numerically. So the source's **20 kV**
> gives the **20 keV** the text quotes — consistent. But $20\ \mathrm{kV} + 180\ \mathrm{kV}$ caps
> this particular machine at about **200 keV** for a singly charged ion. The text's "several hundred
> keV or **MeV**" is therefore a statement about implanters **in general**, not about the machine
> drawn — reaching MeV needs multiply charged ions or a much higher-voltage column. Not an error in
> the page; just do not quote the 180 kV and the MeV in the same sentence.

### 5.10.2 ⭑ Ion implantation versus diffusion ·L5 p9

**Six advantages of ion implantation over diffusion** ·L5 p9 — *reproduce in this order*:

1. **Doping levels can be precisely controlled**, because the incident ion beam **can be accurately
   measured as an electric current**.
2. **The depth of the dopant is easily regulated** by controlling the **incident ion velocity**; it
   is **capable of very shallow penetrations**.
3. **Extreme purity of the dopant is guaranteed.**
4. **Doping uniformity across the surface can be accurately controlled.**
5. The ions enter the solid **as a directed beam**, so there is **very little spread of the beam** —
   the **doping area can be clearly defined**.
6. It is **carried out at room temperature**, so **wafers do not face temperature stress**; in
   addition **photoresist can be used as the mask**, so **there is no need to grow thick masking
   oxides**.

**Three disadvantages of ion implantation over diffusion** ·L5 p9:

1. **Crystal damage.** High-energy ions colliding with silicon can create **considerable damage to
   the crystal structure**, giving **inferior IC performance**. If the damage is not extensive, the
   process of **annealing restores the structure**.
2. **Cost.** High initial investment and operating cost of the equipment — **> US \$1 million**.
3. **Toxicity.** Uses **very toxic gases** for some dopants, such as **phosphorus and arsenic**.

> **[added] Memory hook.** The advantages are all forms of *control* (dose, depth, purity,
> uniformity, lateral definition, thermal budget); the disadvantages are *damage, dollars, danger*.

> ⚠ VERIFY **C5.9** ·L5 p9 — Fig. 67.13 labels the accelerator supply "**180 KV**". The SI symbol
> for the kilovolt is **kV**: lower-case **k** is the prefix *kilo*, while capital **K** is the
> kelvin. The **same figure prints "20 kV" correctly** two labels away, so the page is internally
> inconsistent as well as wrong. Cosmetic.
> See `_verification-log.md`.

> ⚠ VERIFY **C5.8** ·L5 p7 — Fig. 67.10 labels its first curve "**Predeposition**" while the body
> text throughout uses "**pre-deposition**", and the horizontal axis is captioned "**Depth into-
> substrate**" with a stray hyphen after "into". Cosmetic typesetting faults in an otherwise clear
> figure. See `_verification-log.md`.

---

## 5.11 Photomask generation ·L5 p9–p10 (§67.22)

The framing sentence ·L5 p9: IC fabrication consists of **identifying selected regions of each
circuit on the wafer surface into which identical dopant or metallic interconnections are made,
while protecting other regions**. Therefore:

- **a separate mask is required for each operation**, whose function is to **expose the selected
  regions and protect the others**;
- there may be **hundreds of identical dies (ICs) on a wafer**, each circuit containing **hundreds
  of thousands or millions of devices**;
- **identical steps are carried out simultaneously for each process**, and **for each process a
  separate mask is needed**.

[table] **⭑ Mask production sequence** ·L5 p10

| Step | What happens |
|---|---|
| 1 | A **drawing** is made on a **computer-assisted graphics system**; all information is stored **in digital form** |
| 2 | Computer commands drive a **pattern generator**, which uses an **electron beam** to write the pattern — for one or several dies — on **a glass plate covered with a thin chromium film** |
| 3 | The finished glass plate is called a **reticle** |
| 4 | The reticle pattern is **projected onto the wafer**; a **wafer stepper** **reduces** the reticle circuit onto the photoresist-covered wafer and **steps across the surface** until the entire array of circuits is built up |

[def] **Reticle** — the prepared glass plate carrying the pattern for **one or several dies**.

[def] **Mask** — usually refers to a glass plate containing the pattern for **the whole wafer**.

**Limit on single masks** ·L5 p10: using a **single mask for all circuits on a wafer is not feasible
for printing very small (< 1 µm) features**, because of **alignment problems**. Single masks are
**still used for simple digital and analogue circuits such as light-emitting diodes (LEDs)**.

---

## 5.12 Photolithography ·L5 p10–p11 (§67.23)

[def] **Photolithography** — the process in which **the geometrical pattern on the glass plate
(reticle) is transferred to the surface of the wafer**, to **open identical windows** so that
diffusion (or ion implantation) can take place in **all identical regions of the same IC and in all
ICs on the wafer**.

[def] **Photoresist** — the **light-sensitive material** the wafer is coated with. About **1 ml** is
applied to the wafer surface and the wafer is **spun very rapidly**, forming a **uniform film about
1 µm thick** over the oxidised surface.

### 5.12.1 ⭑ The six-step window-opening sequence ·L5 p11

Reproduce these in order; they are numbered in the source.

1. The wafer is **baked at 100 °C** to **solidify the photoresist**.
2. The **glass plate is placed on the wafer and aligned by computer control**.
3. The glass plate is **exposed to ultraviolet (UV) light**; the **transparent parts pass the light
   on to the wafer**, while **the photoresist under the opaque regions is unaffected**. [Fig. 67.14 (c)]
4. The **exposed photoresist is chemically removed** by dissolving it in an **organic solvent**,
   **exposing the silicon dioxide underneath**. [Fig. 67.14 (d)]
5. The **exposed silicon dioxide is etched away using hydrofluoric acid**, which **dissolves silicon
   dioxide and not silicon**. Regions under the opaque part of the plate remain **covered by both
   the silicon dioxide and the photoresist**. [Fig. 67.14 (e)]
6. The **photoresist under the opaque regions is removed** with a **proper solvent**, exposing the
   silicon dioxide. [Fig. 67.14 (f)]

**Closing statement** ·L5 p11: after step 6, **all surfaces are protected except those covered by
silicon only**, and it is there that **diffusion or ion implantation takes place**. **Surfaces
covered by silicon dioxide do not permit any entry of dopants.**

### 5.12.2 The six-panel figure ·L5 p10, Fig. 67.14

[fig ·L5 p10, Fig. 67.14] Six stacked cross-sections, each captioned on the left, each drawn as a
wide rectangle labelled **P-Si substrate** with layers on top. Left-hand captions and what is drawn:

- **(a) "P silicon substrate and oxide film."** Substrate block; on top a thin plain rectangle
  arrow-labelled **SiO$_2$**.
- **(b) "Photoresist applied."** Same, plus a **hatched layer** across the whole top,
  arrow-labelled from the right **Positive photo Resist**.
- **(c) "Mask placed above photoresist and UV light directed at it."** Above the wafer floats a
  horizontal bar arrow-labelled **Mask**, with a **short opaque segment drawn beneath its centre**;
  a row of **downward arrows** covering the full width is arrow-labelled **Light energy**. The
  hatched resist and the oxide are still full width.
- **(d) "Photoresist etched away under transparent regions of mask."** Only a **small hatched block
  of resist remains, at the centre**, sitting on a still-full-width oxide layer.
- **(e) "SiO$_2$ etched away."** The oxide has gone everywhere **except directly under the resist
  block**, leaving a small two-layer island (oxide with resist on top) on bare substrate.
- **(f) "Remaining photoresist etched away."** Only a **small plain rectangle of SiO$_2$** remains
  on the bare P-Si substrate, arrow-labelled **SiO$_2$**.

> **[added] Read Fig. 67.14 as the *complement* of the usual window picture.** The mask drawn is
> **transparent almost everywhere with one small opaque bar**, so what survives is a **small oxide
> island** and what is opened is everything around it. Most textbook figures draw the opposite —
> an opaque mask with one small clear square, leaving a small oxide **window**. The physics and the
> six steps are identical either way; only the mask polarity differs. Compare **Fig. 67.24 (d)**
> on ·L5 p18, which *does* draw a mask with a central opening and produces a proper window. If a
> question asks you to sketch "opening a window", draw the Fig. 67.24 geometry.

### 5.12.3 ⭑ Positive versus negative photoresist ·L5 p11

[def] **Positive photoresist** — one which **allows the windows to be opened wherever the UV light
passes through the transparent parts of the mask**. (This is the type used in the explanation above
and in every figure in this lesson.)

[def] **Negative photoresist** — one which **remains on the surface when exposed to UV light**, so
that **windows are opened under the opaque parts of the mask**.

| | **Positive** | **Negative** |
|---|---|---|
| Behaviour on exposure | exposed resist **dissolves** | exposed resist **remains** |
| Window opens under | **transparent** parts of the mask | **opaque** parts of the mask |
| Resolution | **higher** | limited to **2 to 3 µm** |
| Price paid | **sacrifices adhesion and simplicity of development** to achieve that resolution | — |

### 5.12.4 The wavelength limit ·L5 p11

| Linewidth | Radiation used |
|---|---|
| **above 1 to 2 µm** | **UV light** — the practical limit of the UV method |
| **below 1 µm** | **very short wavelength radiation — electron beam or X-rays** |

[fig ·L5 p11, inset photograph] An unnumbered colour micrograph of a die: a **blue field crossed by
pale rectangular blocks and fine tracks, with orange bond pads around the edge**, captioned "The
photolithograph is used to add circuit elements to the wafer. The wafer is coated with layer of a
chemical called photoresist." **No image is reproduced in this repository** — this description is
all there is.

---

## 5.13 Epitaxy ·L5 p11–p12 (§67.24)

[def] **Epitaxy (epitaxial growth)** — the **controlled growth of a crystalline doped layer of
silicon on a single-crystal substrate**.

### 5.13.1 What epitaxy does that diffusion cannot ·L5 p12

The argument, in the order the page makes it:

- Diffusion and ion implantation **produce a surface layer of higher doping density than existed
  there before**.
- **It is not possible by those methods to produce, at the surface, a layer of *lower* concentration
  than exists there.**
- **Epitaxy can.** In diffusion and implantation, a dopant is **driven into** a doped substrate; in
  epitaxy, a layer of doped silicon is **deposited on top of** the substrate surface.
- **Normally this single-crystal layer has a different type of doping from the substrate.**

[table] **Uses of epitaxy named on the page** ·L5 p12

| Use | Detail |
|---|---|
| Deposit N or **N$^+$** (heavily doped N-type) silicon | ⚠ see `V5.3` |
| **Isolation between bipolar transistors** | **N$^-$** (lightly doped N-type) deposited on a **P-type** layer |
| **Improve the surface quality** of an N-type substrate | by depositing N-type material over it |

> ⚠ VERIFY **V5.3** ·L5 p12 — printed as "Epitaxy is used to deposit N or N$^+$ (i.e., heavily doped
> N-type) silicon, **which is impossible to accomplish by diffusion**". This **contradicts the
> paragraph immediately above it on the same page**, which correctly states that what diffusion
> cannot do is produce a surface layer of ***lower*** concentration. Heavily doped N$^+$ regions are
> made by diffusion routinely — **the N$^+$ emitter of the bipolar transistor on ·L5 p20 is diffused,
> not grown**. Correct statement:
> $$\boxed{\;\text{epitaxy is required when the new surface layer must be more \textit{lightly} doped than what lies beneath it, or doped independently of it}\;}$$
> Substantive: as printed it teaches a false capability boundary between the two processes.
> See `_verification-log.md`.

[table] **Methods of growing the epitaxial layer** ·L5 p12

| Method | Abbreviation as printed | Correct abbreviation |
|---|---|---|
| Vapour-phase epitaxy | **VPE** | VPE |
| Liquid-phase epitaxy | **LPE** | LPE |
| Molecular beam epitaxy | **MPE** ⚠ `V5.2` | **MBE** |

> ⚠ VERIFY **V5.2** ·L5 p12 — printed as "**molecular beam epitaxy (MPE)**". The accepted
> abbreviation is **MBE** — the initials of *Molecular Beam Epitaxy*. "MPE" corresponds to no
> deposition technique. Substantive in the exam sense: a student who writes MPE has written a
> non-existent process. Correct form: **MBE**.
> See `_verification-log.md`.

### 5.13.2 The vapour-phase epitaxy (VPE) system ·L5 p12, Fig. 67.15

**Construction and operation** ·L5 p12:

1. Silicon wafers are placed in a **long boat-shaped crucible made of graphite**.
2. The boat sits in a **long cylindrical quartz tube** with **inlets and outlets for the gases**.
3. The tube is **heated by induction**, using **heating coils wound around the tube**.
4. **All the chemicals introduced and reacting are gases** — hence the process is
   **chemical vapour deposition (CVD)**.
5. **The epitaxial layer is grown from the vapour phase onto the silicon, which is in the solid
   state.**
6. Because the layer is grown on the substrate, **epitaxy forms crystal without ever reaching the
   melting point of silicon** — contrast the Czochralski process of §5.5, which starts from a melt.

[table] **VPE process data** ·L5 p12

| Quantity | Value |
|---|---|
| Layer thickness | **3 to 30 µm** |
| Control accuracy (thickness and doping content) | **better than 2 %** |
| Reaction temperature | **approximately 1200 °C** |
| Why so hot | so dopant atoms **acquire enough energy to move into the crystal, form covalent bonds and become an extension of the single crystal** |

[fig ·L5 p12, Fig. 67.15] A gas-handling manifold on the left feeding a horizontal reactor on the
right.

- **Six vertical inlet lines** rise from the bottom, each through a circled-cross symbol (a **gas
  valve and flow gauge**, labelled once at the top left). Reading left to right the lines are
  labelled: **HCl**, **H$_2$ + B$_2$H$_6$**, **H$_2$ + PH$_3$**, **N$_2$**, **H$_2$**, **H$_2$**.
- The right-most H$_2$ line dips into a **U-shaped vessel** at the bottom labelled **SiCl$_4$**,
  standing in a **temperature bath** (arrow-labelled from the right).
- All lines join a horizontal header that runs right into the **reactor tube**, drawn as a long
  chamber that flares open, then narrows to a **vent** at the right.
- Inside the chamber, a **tilted rectangular slab** carries small blocks — arrow-labelled **Silicon
  wafers** — i.e. the graphite susceptor/boat.
- Above and below the chamber, two horizontal rows of **dots** represent the **RF heating coil**
  (arrow-labelled top).
- **Three long horizontal arrows** inside the chamber show gas flowing left to right over the
  wafers.

> **[added] What each gas line is for** — not stated on the page, given here so the figure makes
> sense: SiCl$_4$ is the **silicon source**; H$_2$ is the **carrier and reducing gas**; B$_2$H$_6$
> (diborane) is the **P-type dopant source** and PH$_3$ (phosphine) the **N-type dopant source**;
> HCl is used for **in-situ etching/cleaning** of the wafers before growth; N$_2$ **purges** the
> tube. Marked `[added]` because the lesson names the gases without explaining them.

---

## 5.14 Metallization and interconnections ·L5 p12–p14 (§67.25)

### 5.14.1 What the interconnections must do ·L5 p12–p13

- **Low resistance**, to minimise **voltage drops on the lines**.
- **Low capacitance between lines**, so as to **reduce delay times**.
- **Make ohmic contacts** to the semiconductor regions — the P and N regions of a PN junction diode,
  for example.

[def] **Ohmic contact** — one that exhibits a **very low resistance, allowing currents to pass
easily in both directions** through the contact.

[table] **Why aluminium** ·L5 p13

| # | Property |
|---|---|
| — | **High conductivity** — the reason it is the obvious choice, particularly in silicon-based devices |
| 1 | **easy to evaporate** |
| 2 | **can be easily etched** |
| 3 | **not expensive** |
| 4 | **adheres well to silicon dioxide** |

### 5.14.2 ⭑ The three deposition processes ·L5 p13–p14

**(1) Resistance heating** ·L5 p13

1. The **source** and the **silicon substrate** are both located in an **evacuated chamber**.
2. The source is a **small piece of aluminium attached to a coil of tungsten**, which serves as the
   **heater**.
3. The heated element, having a **high melting point, remains solid** while the **aluminium is
   vaporised**.
4. Aluminium atoms **travel to the substrate, condense**, and deposit an aluminium layer on the
   silicon surface.
5. **Photolithographic masking and etching** then remove the metal where it is not wanted.

**(1a) RF-induction variant** ·L5 p13 — the evaporation source is kept in a **boron nitride
crucible** heated by **radio-frequency induction**. **Advantage:** high deposition rates.
**Drawback:** **the crucible may contaminate the metal.**

**(2) Electron-beam heating** ·L5 p14

1. **Aluminium in a crucible** is placed in a **vacuum chamber together with the substrate**.
2. The aluminium is subjected to a **high-intensity electron beam formed by an electron gun**, which
   **vaporises** it.
3. The aluminium **travels to the wafer**.
4. **Mask and photolithography** define where the aluminium is deposited.

**(3) Sputtering** ·L5 p14

1. The material to be deposited is placed in a container held at **low pressure** in the vicinity of
   the substrate.
2. **The material to be deposited is the cathode (the target); the substrate is the anode.**
3. A **DC or radio-frequency high voltage** is applied between anode and cathode.
4. That voltage **ionises the inert gas** in the chamber.
5. The ions are **accelerated to the cathode** (**the anode is usually grounded**) where, **by impact
   with the aluminium target, atoms of aluminium are vaporised**.
6. A **gas of aluminium atoms** is generated and **deposited on the wafer surface**.

**After deposition** ·L5 p14: the wafers are **placed in a furnace to solidify the connections**, so
that **low-resistance metallic contacts are made**.

[table] **⭑ The three metallization methods at a glance** ·L5 p13–p14

| | Heat source | Where the metal sits | Distinguishing note |
|---|---|---|---|
| **Resistance heating** | current through a **tungsten coil** | small Al piece **on the coil** | simplest; heater stays solid, Al evaporates |
| (variant) **RF induction** | **RF induction coil** | **boron nitride crucible** | high deposition rate, **but crucible may contaminate** |
| **Electron-beam heating** | **electron gun / high-intensity electron beam** | crucible in vacuum chamber | beam vaporises the Al directly |
| **Sputtering** | **DC or RF high voltage ionising an inert gas** | **target = cathode**, substrate = anode | **momentum transfer**, not thermal evaporation |

### 5.14.3 The interconnection layer itself ·L5 p14

| Quantity | Value |
|---|---|
| Aluminium line thickness | **about 0.5 µm** |
| Where the lines lie | **on top of the silicon dioxide layer** covering the wafer |
| How contact is made to silicon | **photolithography opens windows in the SiO$_2$** so the aluminium reaches the silicon or its ohmic contact |
| Complicated ICs | **two or three vertically stacked layers of interconnections, separated by silicon dioxide layers** |
| Where the lines end | at aluminium pads called **bonding pads**, from which external connections are made |

### 5.14.4 The two metallization figures ·L5 p13

[fig ·L5 p13, Fig. 67.16] Two panels side by side.

- **(a)** A **tungsten heater** drawn as a small helical coil (arrow-labelled from above), with four
  small **Al** chips hanging on its lower turns (arrow-labelled *Al* from below).
- **(b)** A cross-section of a finished interconnection. A pale continuous **aluminium** layer runs
  across the top (two arrows label it **Al**), **dipping down into contact windows**. Between the
  windows, **hatched strips** of **SiO$_2$** (arrow-labelled at the right) separate the metal from
  the silicon. Two arrows from below label the **Diffusions** — the doped regions the metal dips
  down to contact. The picture shows **a typical interconnection between two diffused layers**.

[fig ·L5 p13, Fig. 67.17] Two panels.

- **(a)** A **tapered crucible** drawn in outline, labelled **Boron nitride crucible**, with
  **Al** shaded inside its mouth, and an **RF coil** drawn as loops wound around the outside
  (arrow-labelled from the right).
- **(b)** A rectangular chamber outline; inside its floor sits a **hatched trapezoidal crucible**
  labelled **Crucible**, holding the **Metal for deposition** (arrow-labelled from the left). Three
  arrows rise from the metal surface, labelled **Evaporate metal atoms**. From the right a **curved
  chain of dots** sweeps down and into the crucible, labelled **Electrons** at the top and
  **Electron heating beam** at the bottom — the electron gun's magnetically bent beam.

[fig ·L5 p13, inset photograph] An unnumbered photograph of **several square dies and round wafers
of different diameters standing and lying on a dark surface**, captioned "Several cycles of
photolithography etching and doping are performed producing multiple layers of circuit elements on
the wafer." Not reproduced in this repository.

---

## 5.15 Stage 4 — testing, bonding and packaging ·L5 p14–p16 (§67.26)

**Framing** ·L5 p14: the individual IC chip must be **connected to outside leads and packaged**
conveniently for use in a larger circuit or system. Because **the devices are handled individually
once separated from the wafer**, **bonding and packaging are expensive processes**.

### 5.15.1 Testing ·L5 p14

1. After the wafer of monolithic circuits has been processed and the **final metallization pattern
   defined**, it is **placed in a holder under a microscope** and **aligned for testing**.
2. The tester is a machine called a **multiple-point probe**.
3. The probe **contacts the various pads on an individual circuit** and **a series of tests verifies
   the electrical properties of the device in a very short time**.
4. After all circuits are tested, the wafer is **removed, sawed between the circuits, and broken
   apart**.
5. **Each die that passed the test is picked up and placed in the package.**

### 5.15.2 Bonding — two steps ·L5 p14

**Step 1 — die attach.** The **back of the die is mechanically attached** to an appropriate mount
medium: a **ceramic substrate**, a **multi-layer-ceramic package**, or a **metal lead frame**. The
**two common die-bonding methods are hard solders and polymers.**

**Step 2 — pad interconnection.** The **bond pads on the circuit side of the die are connected by
wires to the package**.

[table] **⭑ The three common interconnection schemes** ·L5 p14

| # | Scheme |
|---|---|
| (i) | **Wire bonding** — itself split into **thermosonic** and **thermocompression** processes |
| (ii) | **Tape-automated bonding (TAB)** |
| (iii) | **Flip-chip solder bonding** |

The source states that further detail of these processes is **beyond its scope**; nothing is added
here.

### 5.15.3 Packaging ·L5 p14–p15

**Purpose** ·L5 p14: package the device in a medium that **protects it from the environment of its
intended application**. In most cases this means:

- the **surface must be isolated from moisture and contaminants**;
- **the bonds and other elements must be protected from corrosion and mechanical shock**.

**One common construction** ·L5 p15: the chip is **mounted on a stamped metal lead frame**; **wire
bonding** connects chip to leads; the package is formed by **applying a ceramic or plastic case and
trimming away the unwanted parts of the lead frame**.

**General package facts** ·L5 p16:

- Most packages can be made in **ceramic or plastic**.
- ICs are **hermetically sealed** for protection from the environment.
- Pins may be on **one side** (single inline or zigzag), **two sides** (DIP), or **four sides**
  (quad package).
- The **most advanced packages have leads distributed over a large portion of the package surface** —
  **through-hole pin grid arrays (PGAs)** or **surface-mounted ball grid arrays (BGAs)**.

[fig ·L5 p14, Fig. 67.18] An isometric cutaway of a **ceramic dual-inline package**. The body is
drawn as a flat rectangular slab in perspective; its **lid is cut away** over the centre to reveal
the **Si chip** (arrow-labelled) sitting in a cavity, with **short bond wires fanning out from the
chip to the lead frame** on both sides. A line labelled **Ceramic package** points to the body; a
label **Sealing glass** points to the seam between lid and body at the front edge; **Leads** points
to the row of pins bending down from the near side. Two parallel rows of leads run along the two
long sides.

### 5.15.4 ⭑ The package classification tree ·L5 p15–p16, Fig. 67.19

[fig ·L5 p15, Fig. 67.19] A two-level bracket tree on the left, package names in the middle, and a
small isometric drawing of each package on the right, lettered (a) to (m). The tree structure is
exactly as tabulated below; the drawings show, in order: two tall thin bodies with a single row of
pins — straight for SIP and staggered for ZIP; a rectangular body with two rows of downward pins
(DIP); a square slab with a central cavity and pins over the underside (PGA); a thin card standing
on edge (SVP); flat bodies with gull-wing leads on two sides (SOP, TSOP); a body with J-shaped leads
curled under on two sides (SOJ); a flat square with gull-wing leads on all four sides (QFP); a flat
square with J-leads on all four sides (QFJ); a square with contacts around all four edges but no
protruding leads (LCC); a square with leads on all four sides (LCC SOJ); and a square whose entire
underside is covered by a grid of solder balls (BGA).

[table] **⭑ IC package classification (Fig. 67.19)** ·L5 p15 — *the whole tree, learn it*

| Category | Lead arrangement | Package | Abbreviation | Panel |
|---|---|---|---|---|
| **Through-hole mount** | Single side | Single Inline Package | **SIP** | (a) |
| | Single side | Zig-zag Inline Package | **ZIP** | (b) |
| | Dual side | Dual Inline Package | **DIP** | (c) |
| | Full surface | Pin Grid Array | **PGA** | (d) |
| **Surface mount** | Single side | Surface Vertical-Mount Package | **SVP** | (e) |
| | Dual side | Small-Outline Package | **SOP** | (f) |
| | Dual side | Thin-Small Outline Package | **TSOP** | (g) |
| | Dual side | Small Outline J-lead Package | **SOJ** | (h) |
| | Quadruple side | Quad Flat Package | **QFP** | (i) |
| | Quadruple side | Quad Flat J-lead Package | **QFJ** | (j) |
| | Quadruple side | Leadless Chip Carrier | **LCC** ⚠ `C5.10` | (k) |
| | Quadruple side | Leaded Chip Carrier, Small Outline J-lead Package | **LCC SOJ** ⚠ `C5.10` | (l) |
| | Full surface | Ball Grid Array | **BGA** | (m) |

[def] **Through-hole mount** ·L5 p16 — packages whose **pins are inserted through holes in the
printed circuit board (PCB) before soldering**. Fig. 67.19 **(a) through (d)**.

[def] **Surface mount** ·L5 p16 — packages whose **leads do not pass through holes in the PCB**;
instead the leads are **aligned to electrical contacts on the PCB and connected simultaneously by
solder reflow**. Fig. 67.19 **(e) through (m)**.

> ⚠ VERIFY **C5.10** ·L5 p15 — Fig. 67.19 uses the acronym **LCC for two different packages**:
> **"LCC (Leadless Chip Carrier)"** at (k) and **"LCC SOJ (Leaded Chip Carrier, Small Outline
> J-lead Package)"** at (l) — *leadless* and *leaded* sharing one abbreviation, one line apart.
> Industry practice reserves **LCC** for the leadless part and uses **LDCC** (or **PLCC** in
> plastic) for the leaded one. Cosmetic, but it is a genuine notation clash and belongs in
> `_nomenclature.md`. See `_verification-log.md`.

[fig ·L5 p16, Fig. 67.20] ⚠ ILLEGIBLE ·L5 p16 — a small photograph referenced from the surface-mount
paragraph ("As refer to the picture shown in Fig 67.20"). The render shows a heavily washed-out
close-up: a **pale grey annular/oval form** with a **blue-white curved sliver** at its centre and
**two dark metallic fittings with wires or leads entering from the left and the right**. **The
subject cannot be identified** — it is not recognisably any of the packages in Fig. 67.19.
**Needs a screenshot of printed page 2493 (PDF p16), the photograph at the top right, to caption
it correctly.** Nothing is guessed here.

---

## 5.16 Building the elements — 1. Resistors ·L5 p16–p17 (§67.27, item 1)

**Framing** ·L5 p16: there are **literally thousands** of different semiconductor device structures,
developed for specific performance either as discrete components or in ICs; but there are **basic
structures required for each of the major device and circuit types**. The lesson then builds five:
**resistor, capacitor, diode, bipolar transistor, MOSFET**.

**How an IC resistor is made** ·L5 p16: **most resistors in ICs are formed by the same processes
used to form devices** — a sequence of **oxidation, masking and doping**. Fig. 67.21 (a) shows a
resistor made of a **P-type region diffused into an N-type epitaxial layer**, with **metallic
contacts at the two ends of the diffused region** (⚠ `V5.5`). Because the shape is **dictated by the
diffusion**, the section is **very nearly rectangular**.

### 5.16.1 The resistance equation — the only equation in this lesson ·L5 p16

[eq: ic-diffused-resistor] **Value of a diffused IC resistor** ·L5 p16

$$\boxed{\;R \;=\; \rho\,\frac{l}{a} \;=\; \rho\,\frac{l}{w\,d}\;}$$

- $R$ — resistance, $\Omega$
- $\rho$ — **resistivity of the layer**, $\Omega\!\cdot\!\mathrm{cm}$ (the lesson's unit)
- $l$ — **length** of the resistive region, cm
- $a$ — **cross-sectional area** of the resistive region, $\mathrm{cm^2}$, with $a = w\,d$
- $w$ — **width** of the resistive region, cm
- $d$ — **depth** of the resistive region, cm

> ⚠ VERIFY **V5.4** ·L5 p16 — printed as $R = \rho.l/a$ **or** $\rho.l/w.d$. The second form has
> **no brackets in the denominator**: read literally, $\rho l/w.d$ parses as $(\rho l / w)\cdot d$,
> whose units are $\Omega\!\cdot\!\mathrm{cm^2}$, **not ohms**. The dimensional check settles it in
> one line.
> Correct form:
> $$\boxed{\;R = \frac{\rho\,l}{w\,d}\;}$$
> Substantive: the bracket is the difference between an answer in ohms and an answer in
> $\Omega\!\cdot\!\mathrm{cm^2}$. See `_verification-log.md`.

> ⚠ VERIFY **V5.5** ·L5 p16 — printed as "Notice the metallic contacts made **at the two ends of the
> epitaxial layer**". Fig. 67.21 (a) as rendered shows the **two contacts landing on the two ends of
> the diffused P-type region**; the N epitaxial layer around it is **not contacted at all** — if it
> were, the resistor would be short-circuited through the epi and the isolating junction would be
> defeated. Correct wording: *contacts are made at the two ends of the **diffused P-type resistor
> body***. Substantive: as printed it describes a structure that would not work.
> See `_verification-log.md`.

### 5.16.2 Sheet resistance ·L5 p17

[def] **Sheet resistance** — **the resistance of a square region having $w = l$**. Units: **ohms per
square** ($\Omega/\square$).

[eq: sheet-resistance] **[added] The sheet-resistance form of the same equation** — not written on
the page, but it is what makes the page's numbers usable:

$$R \;=\; \frac{\rho\,l}{w\,d} \;=\; \underbrace{\left(\frac{\rho}{d}\right)}_{R_s}\cdot\underbrace{\left(\frac{l}{w}\right)}_{n}$$

$$\boxed{\;R = R_s\, n\,,\qquad R_s = \frac{\rho}{d}\,,\qquad n = \frac{l}{w}\;}$$

- $R_s$ — sheet resistance, $\Omega$ per square
- $n$ — **number of squares** laid end to end along the resistor, dimensionless

Setting $l = w$ gives $n = 1$ and $R = R_s$ — which is exactly the definition the page states.
**Note that $R_s$ does not depend on how big the square is, only on how deep the layer is.**

[table] **Resistor data** ·L5 p17

| Quantity | Value |
|---|---|
| Assumed sheet resistance | **100 to 200 $\Omega$ per square** |
| Resulting practical resistor values | **100 $\Omega$ to several kilohms** |
| How to get higher values | a **meander pattern** — Fig. 67.21 (c) |
| Major problem with high values | **they occupy a large area of the chip** |
| Example given | a **50 kΩ** resistor uses an area **that could hold hundreds of transistors** |
| Alternative to diffusion | **ion implantation**, to make resistors **with precise values** |

[ex] **[added] Worked numbers for the sheet-resistance claims** — the lesson gives none, so these
are supplied and verified here, using only its own figures.

*(i) Does 100–200 $\Omega/\square$ really give "100 $\Omega$ to several kilohms"?*

$$R = R_s\,n \;=\; 200 \times 10 \;=\; 2000\ \Omega = 2\ \mathrm{k}\Omega \quad\text{for a 10-square strip}$$

A 10-square strip is, for example, $l = 100\ \mathrm{\mu m}$ by $w = 10\ \mathrm{\mu m}$. One square
gives $100$–$200\ \Omega$; a few tens of squares give a few kilohms. ✔ consistent with the page.

*(ii) Check against the full equation.* Take $\rho = 0.02\ \Omega\!\cdot\!\mathrm{cm}$ and
$d = 1\ \mathrm{\mu m} = 10^{-4}\ \mathrm{cm}$:

$$R_s = \frac{\rho}{d} = \frac{0.02}{10^{-4}} = 200\ \Omega/\square$$

$$R = \frac{\rho\,l}{w\,d} = \frac{0.02 \times 100\times10^{-4}}{10\times10^{-4} \times 10^{-4}} = 2000\ \Omega\ \checkmark$$

Both routes give $2\ \mathrm{k}\Omega$, confirming $R = R_s n$.

*(iii) Why 50 kΩ is expensive in area.*

$$n = \frac{R}{R_s} = \frac{50\,000}{200} = 250\ \text{squares}$$

At $w = 10\ \mathrm{\mu m}$ that is $l = 2500\ \mathrm{\mu m} = 2.5\ \mathrm{mm}$ of track — which is
why it must be **folded into a meander** and why it swallows the area of hundreds of transistors.
✔ consistent with the page's remark.

### 5.16.3 The resistor figure ·L5 p16, Fig. 67.21

[fig ·L5 p16, Fig. 67.21] Three panels.

- **(a) Cross-section.** From the top: a **hatched SiO$_2$ layer** spanning the width, broken by
  **two windows**; in each window a small **pale metal block** with a **lead rising to a terminal
  circle**. Below the oxide, a **shallow tub outlined in pink labelled P** whose two ends rise to
  meet the two contacts. The P tub sits inside a layer labelled **N** (the epitaxial layer), which
  in turn sits on a much thicker block labelled **P substrate**. Both sides of the drawing end in
  **wavy break lines**, showing the structure continues.
- **(b) The idealised resistor body.** A **3-D rectangular bar** drawn in perspective, with **$w$**
  marked on the top, side and front edges, **$d$** as the vertical dimension (double arrow at the
  left face), and **$l$** as the long dimension (arrow along the bar).
- **(c) Meander pattern.** A plan view: a **long narrow track folded back on itself** in a flat
  serpentine, with a **square contact pad at each end** (top-left and bottom-right).

> **[added] The isolation is free.** The stack in (a) is P (resistor) inside N (epi) on P
> (substrate). Both junctions are reverse-biased in normal operation, so the resistor is isolated
> from its neighbours by depletion regions — no extra process step. That is the "isolation
> diffusion" promised back in the definition of an IC on ·L5 p1.

---

## 5.17 Building the elements — 2. Capacitors ·L5 p17 (§67.27, item 2)

[table] **⭑ The three IC capacitor structures** ·L5 p17

| Type | How it is made | Key property |
|---|---|---|
| **Junction (diffused) capacitor** | uses the capacitance formed between the **P and N regions of a reverse-biased diode**; made by the **same diffusion processes used to form devices** | **Disadvantage: capacitance depends on the applied voltage** |
| **MOS capacitor** | **metal – insulator – N$^+$ (heavily doped) semiconductor** layers, as in MOS structures | **voltage-independent** |
| **Trench capacitor** | a **trench etched vertically into the wafer surface**; **walls oxidised**, **centre filled with deposited polysilicon**; wired from the surface | **conserves wafer surface area** |

**On junction capacitors** ·L5 p17: a **bipolar transistor has three regions, so either of its two
PN junctions may be used as a capacitor** — and **the breakdown voltage may vary considerably from
one to the other**.

**On dense circuits** ·L5 p17: an **oxide/nitride/oxide dielectric sandwich** is used; the page says
the combination film has a **lower dielectric constant, allowing a smaller capacitor area** (⚠
`V5.6`).

**On trench capacitors** ·L5 p17:

- Trenches are etched **either isotropically with wet etching or anisotropically with dry etching**.
- **Trench side walls are oxidised; the centre is filled with deposited polysilicon.**
- The final structure is **"wired" from the surface**, with **the silicon and the polysilicon as the
  two electrodes and silicon dioxide as the dielectric**.
- They are useful **when preservation of wafer surface [area] is the main criterion**.
- The alternative for conserving surface area is to build **stacked capacitors on the wafer
  surface**.
- The driver for both is the need for **small, high-dielectric capacitors for dynamic random access
  memory (DRAM) circuits**.

> ⚠ VERIFY **V5.6** ·L5 p17 — printed as "The combination film has a **lower** dielectric constant,
> allowing a capacitor area **smaller** than a conventional silicon dioxide capacitor." **These two
> halves contradict each other.** For a parallel-plate capacitor
> $$C = \frac{\varepsilon_0\varepsilon_r A}{t}\quad\Longrightarrow\quad A = \frac{C\,t}{\varepsilon_0\varepsilon_r}$$
> so for a given $C$ and thickness $t$, a **smaller area requires a *larger* $\varepsilon_r$**.
> Silicon nitride has $\varepsilon_r \approx 7$ against $\approx 3.9$ for silicon dioxide, so the
> oxide/nitride/oxide (ONO) stack does indeed have the **higher** dielectric constant — which is
> exactly why it is used. Correct form:
> $$\boxed{\;\text{the ONO film has a \textit{higher} dielectric constant, allowing a smaller capacitor area}\;}$$
> Substantive: as printed the sentence is dimensionally self-defeating and teaches the wrong sign of
> the effect. See `_verification-log.md`.

[fig ·L5 p17, Fig. 67.22] Cross-section of a junction capacitor. A **hatched SiO$_2$ layer** across
the top is broken by **two windows**, each holding a **pale metal contact with a lead rising to a
terminal circle**. Below the surface, nested tubs drawn in pink:

- an **outer, wider, deeper tub labelled P**, diffused into the body;
- an **inner, narrower, shallower tub labelled N$^+$** sitting inside the P tub;
- the body itself labelled **N substrate**;
- **wavy break lines** at both edges.

**Terminal geometry (read from the render):** the **left contact lands on the P region**, between
the left edge of the P tub and the left edge of the N$^+$ tub; the **right contact lands on the
N$^+$ region**, inboard of both right-hand edges. **The capacitor is therefore the N$^+$–P junction,
held in reverse bias; the surrounding N substrate isolates it via the P–N substrate junction.**

[fig ·L5 p17, Fig. 67.23] Cross-section of a trench capacitor. A block of **Silicon**
(arrow-labelled top left) with **wavy break lines** at both sides. A **deep, narrow vertical trench**
descends from the top surface, arrow-labelled **Trench** from the left. The trench is **lined on
both walls and the floor by a U-shaped layer of Silicon dioxide** (arrow-labelled top right), and
its **centre is filled by a narrow vertical column of Polysilicon** (arrow-labelled top centre) that
**projects slightly above the wafer surface** so it can be wired. **Electrodes: the surrounding
silicon and the central polysilicon; dielectric: the oxide liner.**

---

## 5.18 Building the elements — 3. Diodes ·L5 p17–p18 (§67.27, item 3)

### 5.18.1 Diodes inside an IC ·L5 p17

Because **all interconnections and device terminals are made at the surface**, a diode is formed in
**two ways**:

| | Circuit family | How the diode is made |
|---|---|---|
| **(a)** | **Bipolar circuits** | from a **bipolar transistor, by short-circuiting two of its three terminals** — **collector to base**, or **emitter to base**. This gives **emitter-base diodes** and **base-collector diodes**. |
| **(b)** | **MOS circuits** | **most diodes are formed with the source–drain doping step** |

### 5.18.2 The discrete PN junction diode — the eight-panel process ·L5 p18, Fig. 67.24

**Starting material** ·L5 p18: a **heavily doped N-type (N$^+$) substrate about 150 µm thick**.

[table] **⭑ Diode fabrication sequence** ·L5 p18 — panel by panel

| Panel | Step |
|---|---|
| **(a)** | A layer of **N-type silicon, 1 to 5 µm**, is **grown on the substrate by epitaxy** |
| **(b)** | A layer of **silicon dioxide (SiO$_2$) is deposited by oxidation** |
| **(c)** | The surface is **coated with positive photoresist** |
| **(d)** | A **mask is placed on the surface, aligned, and exposed to ultraviolet (UV) light** |
| **(e)** | **Mask removed, resist removed**, and the **silicon dioxide under the exposed resist is etched** |
| **(f)** | **Boron is diffused to form the P-type region** — note that **boron diffuses easily in silicon but not in silicon dioxide** |
| **(g)** | A **thin aluminium film is deposited over the surface** |
| **(h)** | The metallised area is **covered with resist; a second mask identifies where metal is to be preserved**; the surface is **etched to remove unwanted metal**; the **resist is dissolved** |
| **final** | **Contact metal is deposited on the back surface** and **ohmic contacts are made by heat treatment** |

[fig ·L5 p18, Fig. 67.24] Eight cross-sections in two columns of four. Every panel shows a wide
block labelled **N$^+$ substrate**, drawn with **wavy break marks at both ends**, and above it a
thinner layer labelled **N** — the epitaxial layer. Panel by panel:

- **(a)** substrate + N epitaxial layer only.
- **(b)** adds a **hatched SiO$_2$ layer** across the whole top, arrow-labelled **SiO$_2$**.
- **(c)** adds a **second, differently hatched layer** on top, arrow-labelled from the left
  **Positive photoresist**.
- **(d)** a **mask bar drawn above the wafer with a clear gap at its centre**, and a row of **downward
  arrows labelled UV Light** covering the full width; the resist and oxide are still continuous.
- **(e)** the resist has gone and the **oxide is broken into two hatched strips with a gap between
  them**, exposing the N layer through the window.
- **(f)** in that gap a **shallow tub labelled P** has appeared inside the N layer; the label **N**
  sits to the right of it.
- **(g)** a **continuous pale aluminium film** now covers the oxide strips and dips into the window.
- **(h)** the aluminium has been etched back to a **single contact block over the P region**,
  overlapping slightly onto the oxide on each side.

> **[added] Contrast this with Fig. 67.14.** Here the mask in (d) is drawn **with an opening at its
> centre**, so the positive resist is exposed only in the middle and a proper **window** is opened
> over the region to be diffused. This is the geometry to reproduce when asked to sketch "opening a
> window in the oxide".

> ⚠ VERIFY **C5.11** ·L5 p18 — printed as "Then boron is diffused to form P-type region **a** shown
> in Fig. 67.24 (f)". Reads **as shown**. Cosmetic. See `_verification-log.md`.

---

## 5.19 Building the elements — 4. The NPN bipolar transistor ·L5 p18–p21 (§67.27, item 4)

This is the longest and most examinable process in the lesson: **seven masks, in order.**

### 5.19.1 Starting material and the substrate ·L5 p18

- **A lightly doped P-type wafer.**
- [def] **Substrate** — **the base on which the transistor is made**; its function is to **act as
  mechanical support for the device**. (Note the unfortunate word: "base" here means *foundation*,
  not the transistor's base terminal.)
- **Why P-type for an NPN?** The page defers the answer to the discussion of **isolation** — see
  §5.19.3, mask 2.

| Substrate property | Value |
|---|---|
| Resistivity | **3–10 $\Omega\!\cdot\!\mathrm{cm}$** |
| Thickness | **500 to 700 µm**, for wafers of diameter **over 100 mm** |

### 5.19.2 ⭑ The seven-mask sequence ·L5 p20

| Mask | Purpose | What happens | Fig. 67.25 panel |
|---|---|---|---|
| — | — | **SiO$_2$ about 0.5 µm thick deposited by thermal oxidation** | (a) |
| **1st** | **buried layer** | windows opened in the oxide; the **N$^+$ buried layer is diffused to about 3 µm**. Afterwards the wafer is **stripped of all oxide** | (b) |
| — | — | **Phosphorus-doped N-type epitaxial layer deposited over the whole wafer**, then **SiO$_2$ 0.5–1 µm grown thermally** on it | (c) |
| **2nd** | **isolation** | windows etched, then **boron diffused from the surface down to the substrate**, forming the isolation walls. Followed by **oxidation of the surface** | (d) |
| **3rd** | **base** | window opened; **P-type diffusion or ion implantation** forms the base to **2–3 µm** depth. Followed by **deposition of an oxide layer** | (e) |
| **4th** | **N$^+$ emitter and collector contact** | windows opened; **phosphorus or arsenic diffusion driven to about 2 µm**. Followed by **oxidation over the entire surface** | (f) |
| **5th** | **metallic contact windows** | windows opened for contacts to the three terminals; then **aluminium film 0.5 to 1 µm** deposited by **evaporation or sputtering** | (g) |
| **6th** | **interconnection pattern** | the pattern is **etched into the deposited metal** | (g) |
| — | — | **Silicon nitride (Si$_3$N$_4$) passivation layer** deposited to protect the surface from **moisture and chemical contamination** | — |
| **7th** | **bonding holes** | defines the **bonding holes over the aluminium pads** for external connections | — |

**After the seven masks** ·L5 p20:

1. The circuits are **tested by a computer-controlled system**; **all faulty chips are identified
   and marked**.
2. The wafer is **sawed into chips**, which are **bonded onto IC packages**.
3. **Gold wires about 25 µm in diameter** connect the package leads to the bonding pads on the chip.

[table] **All the BJT process numbers in one place** ·L5 p20

| Layer / step | Value |
|---|---|
| First oxide | **0.5 µm** |
| Buried layer depth | **about 3 µm** |
| Epitaxial layer resistivity | **0.1 to 1 $\Omega\!\cdot\!\mathrm{cm}$** |
| Epitaxial layer thickness — **high-speed digital** | **0.5 to 5 µm** |
| Epitaxial layer thickness — **linear analogue** | **10 to 20 µm** |
| Oxide on the epitaxial layer | **0.5 to 1 µm** |
| Base depth | **about 2–3 µm** |
| N$^+$ emitter / collector-contact depth | **about 2 µm** |
| Aluminium film thickness | **0.5 to 1 µm** (⚠ `C5.12`) |
| Passivation layer | **silicon nitride, Si$_3$N$_4$** |
| Bond wire | **gold, about 25 µm diameter** |

> **[added] Read the base and emitter depths together.** The base is quoted at **2–3 µm** and the
> emitter at **about 2 µm**. The emitter junction must lie **above** the base–collector junction or
> there is no base left, so read this as base $\approx 3\ \mathrm{\mu m}$ with emitter
> $\approx 2\ \mathrm{\mu m}$, giving an electrical **base width of order 1 µm**. Taking both at
> exactly 2 µm would punch the emitter through the base — a useful consistency check to state if a
> question asks why the two diffusions must differ.

### 5.19.3 The two structural ideas: isolation and the buried layer ·L5 p20–p21

[def] **Isolation (the tub)** ·L5 p20 — the collector of an NPN transistor is N-type, **and so are
the collectors of all the adjacent transistors**, so **the collectors must be isolated from one
another**. Boron is diffused **from the surface right down to the P substrate**, walling off each
device. **An N-type epitaxial region separated by those walls serves as the tub in which each
transistor is formed.** *This is the answer to "why a P-type substrate for an NPN": the P walls and
P substrate together surround each N tub with a junction that is reverse-biased in operation.*

[def] **Buried layer (sub-collector)** ·L5 p20 — the **N$^+$ layer diffused before the epitaxial
layer is grown**. It **collects the carriers that have crossed the base on their way to the collector
terminal**, and its purpose is **to reduce the collector ohmic resistance**. The page notes that
**during subsequent high-temperature processing the buried layer tends to diffuse out**.

[def] **Parasitic resistance** ·L5 p20–p21 — the **collector series resistance**. In an IC
transistor the carrier path from emitter to collector contact is **considerably longer** than in a
discrete device, so this resistance is **of the order of hundreds of ohms**.

[table] **What the buried layer buys** ·L5 p21

| Quantity | Effect |
|---|---|
| Collector resistance | **reduced by as much as a factor of 20** |
| **Gain–bandwidth product** | **improved by the same factor** |

[def] **N$^+$ collector contact — why it is needed** ·L5 p20: **to form a good ohmic contact**, which
**permits easy current flow in both directions**. To make a good ohmic contact to N material, **an
N$^+$ region is needed between the metal on top and the N region**.

### 5.19.4 The BJT process figure ·L5 p19, Fig. 67.25

[fig ·L5 p19, Fig. 67.25] Seven stacked cross-sections, lettered (a)–(g) down the right-hand side.
The wafer body is a wide rectangle labelled **P substrate** — relabelled **P- substrate** from panel
(c) onward. Panel by panel:

- **(a)** the substrate with a **continuous hatched SiO$_2$ layer** across the top, arrow-labelled
  **SiO$_2$**.
- **(b)** the oxide is broken into **two hatched strips with a central window**; beneath the window,
  a **shallow tub labelled N$^+$**, its boundary drawn in pink — the **buried layer**.
- **(c)** all oxide has been stripped and **a new full-width hatched SiO$_2$ layer** grown. A **new
  horizontal layer labelled N** now spans the whole wafer above the substrate — the **epitaxial
  layer** — and the **N$^+$ buried layer is drawn as a flat pill straddling the epi/substrate
  interface**.
- **(d)** oxide broken into **three strips**. Two **P-isolation walls** run from the surface all the
  way down through the N epi to the substrate, each labelled **P**; a curved arrow from the right
  labels them **P-isolation**. Between the walls sits the N tub with the N$^+$ pill in its floor.
- **(e)** a **shallow tub labelled P** has been diffused into the top of the N tub — the **base** —
  and the oxide has been re-grown as two strips with a gap above it.
- **(f)** two **N$^+$ regions** appear at the top: the left one **inside the P base** (the
  **emitter**), the right one **outside the base, in the N epi** (the **collector contact**). The
  label row reads **N$^+$ | P | N$^+$** left to right. Oxide covers the surface with windows over
  the three regions.
- **(g)** three **metal contacts** are drawn as vertical plugs through the oxide topped by
  horizontal pads, labelled **E**, **B**, **C** left to right: **E** onto the emitter N$^+$, **B**
  onto the P base between emitter and base edge, **C** onto the collector-contact N$^+$.

**Vertical order of the finished device, top to bottom:** metal / SiO$_2$ / N$^+$ emitter inside
P base inside N epitaxial collector / N$^+$ buried layer / P$^-$ substrate, with P isolation walls
on both sides running the full depth.

### 5.19.5 The buried-layer comparison figure ·L5 p21, Fig. 67.26

[fig ·L5 p21, Fig. 67.26] Two cross-sections, one above the other, both with **E, B, C** contacts on
the top surface, a **hatched oxide layer**, and an **N$^+$ | P | N$^+$** group at the top centre
(emitter, base, collector contact).

- **(a)** — **no buried layer.** The regions flanking the device are labelled **N**. **Dashed pink
  arrows** trace the carrier path: down out of the emitter, through the base, then **a long sweep
  sideways and down through the N collector region and back up** to the C contact.
- **(b)** — **with the buried layer.** The flanking regions are now labelled **P** (isolation walls),
  and a **pale pill labelled N$^+$** lies beneath the N region. The dashed arrows now run **down into
  the N$^+$ pill, sideways along it, and up to the C contact** — a much shorter path through
  low-resistivity material.

> ⚠ VERIFY **V5.8** ·L5 p20 — printed as "This path is considerably longer than the path in **the
> discrete BJT shown in Fig. 67.26 (a)**." The render of Fig. 67.26 (a) shows a **planar integrated
> transistor**: E, B and C contacts all on the **top** surface, an N collector region sitting in a
> P substrate, and the **long lateral carrier path drawn in dashed arrows** — that is the *long*
> path the sentence is complaining about, not a short discrete-device path. (In a genuine discrete
> BJT the collector contact is the **back face of the die**, so the path is short and vertical, and
> no such drawing appears anywhere in L5.) Correct reading:
> $$\boxed{\;\text{Fig. 67.26 (a) = IC transistor \textit{without} a buried layer (long path); (b) = the same device \textit{with} the N}^+\text{ buried layer (short path)}\;}$$
> Substantive: as printed, the labels on the two panels invert the comparison the paragraph is
> making. See `_verification-log.md`.

> ⚠ VERIFY **C5.12** ·L5 p20 — printed as "an aluminium film **0.5 and 1 µm** thick". Should read
> **0.5 to 1 µm**, matching the range notation used for every other thickness on the page.
> Cosmetic. See `_verification-log.md`.

---

## 5.20 Building the elements — 5. The enhancement-mode NMOS transistor ·L5 p21–p22 (§67.27, item 5)

**Device:** an **enhancement-mode N-channel metal-oxide-semiconductor field-effect transistor**.
**Five masks**, against the bipolar's seven.

### 5.20.1 Starting material ·L5 p21

| Property | Value |
|---|---|
| Substrate | **lightly doped P-type silicon** |
| Resistivity | **about 5 $\Omega\!\cdot\!\mathrm{cm}$** |
| What sets the doping density | the **drain–substrate breakdown voltage of 20–30 V** |
| Stress-relief oxide ("pad oxide") | **about 20 nm** of SiO$_2$ over the substrate |
| Nitride layer | **about 20 nm** of Si$_3$N$_4$, deposited by **CVD**, on top of the oxide |
| Field oxide | **about 500 nm** |
| Gate oxide | **ultra-thin, about 5 to 10 nm** |
| Gate electrode | **heavily doped (typically N$^+$) polysilicon** |
| Final passivation | **phosphosilicate glass (P-glass)** |

### 5.20.2 ⭑ The five-mask sequence ·L5 p21–p22

| Mask | Purpose | What happens | Fig. 67.27 panel |
|---|---|---|---|
| — | — | pad **SiO$_2$ (20 nm)** then **Si$_3$N$_4$ (20 nm)** by CVD over the substrate | (a) |
| **1st** | **defines the FET areas** | oxide and nitride are **chemically etched away except where the transistor is formed**. Then **boron is diffused or implanted in the field regions to form P$^+$ islands**, and the **field oxide (~500 nm)** is grown over them | (b) |
| — | — | remaining nitride and pad oxide **etched away**; **ultra-thin SiO$_2$ (5–10 nm) grown over the transistor area only** (not over the field oxide) — this is the **gate oxide** | (c) |
| — | — | a layer of **heavily doped N$^+$ polysilicon** deposited over the **entire** wafer surface | (d) |
| **2nd** | **defines the gate region** | polysilicon **etched away except over the gate**. Then, **by ion implantation using the polysilicon gate and the field oxide as the mask**, the **N$^+$ source and drain are formed**. A **thin CVD SiO$_2$** is then grown over the wafer | (e) |
| **3rd** | **metal contact windows** | windows opened to the transistor regions; the thin oxide is **etched away** and **aluminium deposited by evaporation or sputtering** | (f) |
| **4th** | **interconnection pattern** | the pattern is **etched in the aluminium**; then a **protective passivation layer of phosphosilicate glass (P-glass)** is deposited over the whole surface | (g) |
| **5th** | **bonding windows** | "**just as with the BJT**", opens windows so **bonding wires can be connected to the pads on the IC chip** | — |

**Two important mechanisms stated in the text** ·L5 p21:

[def] **Function of the P$^+$ islands (channel stop)** — to **help increase the threshold voltage
$V_T$** and to **prevent the formation of "parasitic" transistors (electrical cross-talk) between
adjacent devices** on the wafer. **The field oxide layer also helps to increase $V_T$.**

[def] **Self-alignment** ·L5 p21 — because the **polysilicon gate and the field oxide are themselves
the implant mask**, the **N$^+$ layers diffuse just far enough to ensure proper alignment, so the
channel length is well defined**. The **dopants do not penetrate the field oxide.** The **heavily
doped polysilicon above the gate behaves electrically like a metal electrode.**

> ⚠ VERIFY **V5.7** ·L5 p21 — printed as "**The silicon dioxide** permits selective oxidation so
> that a thick oxide (about 500 nm) can be formed in the field region." It is the **silicon
> nitride** that permits selective oxidation. The **same paragraph** has already assigned the
> silicon dioxide its own job — *"to provide stress relief to the wafer"* — and in the LOCOS
> (local oxidation of silicon) scheme being described, **Si$_3$N$_4$ is the oxidation barrier**:
> oxygen cannot diffuse through it, so thick oxide grows **only where the nitride has been
> removed**. If the oxide were the barrier, the pad oxide would block oxidation everywhere and no
> field oxide could grow at all. Correct form:
> $$\boxed{\;\text{the silicon \textit{nitride} permits selective oxidation, so thick field oxide grows only where the nitride is removed}\;}$$
> Substantive: it misassigns the role of the two masking layers, which is the whole mechanism of
> the step. See `_verification-log.md`.

### 5.20.3 The NMOS process figure ·L5 p22, Fig. 67.27

[fig ·L5 p22, Fig. 67.27] Seven cross-sections, (a)–(f) in two columns and (g) large at the bottom.

- **(a)** A plain block labelled **P-Si**, with two thin full-width layers on top: the lower
  arrow-labelled **SiO$_2$** and the upper arrow-labelled **Silicon Nitride**.
- **(b)** The **field oxide** now appears at both ends as **thick humps that swell up and taper
  inward** (the classic bird's-beak profile), each arrow-labelled **SiO$_2$**; beneath each hump is
  a region arrow-labelled **P$^+$** (the channel-stop islands). Between the humps, the thin
  oxide/nitride stack still covers the transistor area over the **P-Si**.
- **(c)** The nitride and pad oxide between the humps have gone; a **thin new SiO$_2$** (the gate
  oxide) spans the transistor area, arrow-labelled **SiO$_2$** from below. Field oxide humps and
  **P$^+$** islands remain at both ends.
- **(d)** A **hatched layer arrow-labelled Poly-Silicon** now drapes over the **entire** surface,
  riding up and over both field-oxide humps.
- **(e)** The polysilicon has been etched back to a **small hatched block sitting on the gate oxide
  in the centre**. Two **N$^+$ regions** have appeared in the substrate, one each side of that block,
  arrow-labelled **N$^+$**; the label row reads **P$^+$ | N$^+$ | P-Si | N$^+$ | P$^+$**.
- **(f)** As (e), with the surface now covered by the thin CVD oxide and **contact windows opened**;
  the same label row **P$^+$ | N$^+$ | P-Si | N$^+$ | P$^+$**.
- **(g)** The finished device, drawn larger and fully labelled. From the left: **Field oxide**
  (arrow-labelled) rising into a hump; a **Metal source contact** arm coming in from the left and
  reaching down through the oxide to the left **N$^+$**; the centre occupied by the **Gate N-Type
  Polysilicon** block (hatched), sitting on the **Gate insulator** and capped by an **Insulator**;
  a **Metal drain contact** arm entering from the right and reaching down to the right **N$^+$**;
  field oxide hump at the right end. Below the surface the label row reads **P$^+$ | N$^+$ | P |
  N$^+$ | P$^+$**, with the letter **L** marked across the gap between the two N$^+$ regions — the
  **channel length**. Arrows from below label **Source** (left N$^+$), **Channel** (the P region
  under the gate), **Gate insulator**, and **Drain** (right N$^+$). Two **SiO$_2$** labels mark the
  oxide either side of the gate.

> **[added] Where the terminals sit, for redrawing.** Source and drain are the two N$^+$ regions,
> **symmetric about the gate**; the gate is the polysilicon block **between** them, separated from
> the channel only by the 5–10 nm gate oxide; the channel length $L$ is the **N$^+$-to-N$^+$ gap**,
> which is set by the width of the polysilicon block because the implant is self-aligned to it.
> The substrate (body) contact is not drawn in this figure.

---

## 5.21 MOS versus bipolar IC technology ·L5 p22–p23 (§67.28)

[table] **⭑ The five comparison points, in the source's order** ·L5 p22

| # | Point | Winner |
|---|---|---|
| **1** | **Cost.** MOS ICs are **less costly to fabricate**, because **MOS devices are self-isolating**. Bipolar transistors **require tubs** to isolate devices from one another; isolation in MOS is provided by **heavy doping and a thick oxide in the regions between adjacent devices** | **MOS** |
| **2** | **DC power.** MOS circuits **consume less DC power** than bipolar circuits | **MOS** |
| **3** | **Transconductance.** The MOS transistor has a **lower $g_m$** than the bipolar. This makes **bipolar ICs superior for analogue circuit applications** | **Bipolar** |
| **4** | **Cut-off frequency.** **For the same channel length and base width**, the **limiting cut-off frequency of the MOS transistor is better**, so it has **higher bandwidth** | **MOS** (⚠ `V5.9`) |
| **5** | **Packing density.** MOS packing density is **at least 10× that of bipolar**; a **MOS resistor occupies less than 1 % of the area of a conventional diffused resistor**. This suits MOS to **LSI, VLSI and ULSI** circuits | **MOS** |

**Main disadvantage of MOS ICs** ·L5 p23: **slower speed compared with bipolar ICs** — hence **they
do not compete with bipolar ICs in ultra-high-speed applications** (⚠ `V5.9`).

**Why MOS dominates anyway** ·L5 p23: because of **(i) low cost, (ii) low power consumption and
(iii) high packing density**, MOS ICs are widely produced, and are available as **calculator chips,
memory chips, microprocessors (µP) and single-chip computers**.

> ⚠ VERIFY **V5.9** ·L5 p22 / p23 — the article **states both sides of the speed question and does
> not reconcile them**. Point 4 (·L5 p22) says the MOS transistor has the **better cut-off frequency
> and higher bandwidth**; the paragraph that closes the same article (·L5 p23) says **"the main
> disadvantage of MOS ICs is their slower speed as compared to bipolar ICs"**, and that they do not
> compete in ultra-high-speed applications. The reconciliation is buried in point 4's own qualifier:
> $$\boxed{\;\text{point 4 compares \textit{devices at equal channel length and base width}; the closing paragraph compares \textit{circuits as actually built}}\;}$$
> Substantive for exam purposes: "Is MOS faster or slower than bipolar?" has two opposite answers in
> the source, one page apart, and a student must know which qualifier goes with which.
> See `_verification-log.md`.

> **[added] Why point 3 and point 4 are not in conflict.** $g_m$ sets **gain** per unit current;
> cut-off frequency sets **speed**. A bipolar transistor has the larger $g_m$ because its current is
> exponential in $V_{BE}$ while the MOSFET's is square-law in $V_{GS}$ (see
> `03-bipolar-junction-transistor` and `04-field-effect-transistors`). That is a statement about
> **analogue gain**, not about switching speed — which is why the source can put bipolar ahead on
> point 3 and MOS ahead on point 4 without contradicting itself.

---

## 5.22 Popular applications of ICs ·L5 p23 (§67.29)

Purely illustrative; no mechanism, no numbers. Kept because it is the last article of the chapter.

[table] **Applications named** ·L5 p23

| Group | Examples |
|---|---|
| Named as "widely accepted" | **digital watch** (hours, minutes, seconds, day, month); **electronic calculator** (add, subtract, multiply, divide), including **programmable scientific calculators that display graphs** |
| Modern products | **pocket PC, personal digital assistant (PDA), MP3 players, digital cameras, digital camcorders, mobile phones, digital dictionaries and translators, CD players, DVD players** |
| Games | **video games hooked to a home TV**; **handheld PCs and mobile phones with games needing no TV** |

[fig ·L5 p23, Fig. 67.28 and Fig. 67.29] Two product photographs, credited in the source to their
manufacturers. **Fig. 67.28** shows a **silver compact digital camera in three-quarter view, lens
barrel protruding at the right**. **Fig. 67.29** shows a **small clamshell handheld computer, open,
with a keyboard on the lower half and a lit screen on the upper half**. Neither image is reproduced
in this repository; the credits are omitted here in line with the repository's third-party-image
rule.

---

## 5.23 Objective test 67 ·L5 p23

The lesson ends mid-test: **only questions 1 and 2 are present** in the PDF. Both are transcribed
here, then answered in an `[added]` block.

[exercise ·L5 p23] **Objective Test 67, Q1.** First integrated circuit chip was developed by
(a) C.V. Raman  (b) W.H. Brattain  (c) J.S. Kilby  (d) Robert Noyce.

[exercise ·L5 p23] **Objective Test 67, Q2.** An integrated electronic circuit is
(a) a complicated circuit  (b) an integrating device  (c) much costlier than a single transistor
(d) fabricated on a tiny silicon chip.

### [added] Answers — supplied here, not in the source

**Q1 — (c) J.S. Kilby.**
·L5 p1 states it directly: *"J.S. Kilby of Texas Instruments was the first person to develop (in
1959) an integrated circuit."* Why the distractors are wrong:

- **(a) C.V. Raman** — a physicist known for the Raman effect in light scattering; no connection to
  ICs.
- **(b) W.H. Brattain** — co-invented the **transistor** (·L5 p1), not the IC.
- **(d) Robert Noyce** — the trap. ·L5 p1 says he **"was soon followed"** by Noyce, who fabricated a
  complete IC **including the interconnections**. Noyce made the first *practical monolithic* IC,
  but the question asks who was **first**, and the source's own wording gives Kilby.

**Q2 — (d) fabricated on a tiny silicon chip.**
This is the definition on ·L5 p1: *an IC is a complete electronic circuit in which both the active
and the passive components are fabricated on a tiny single chip of silicon.* Why the others fail:

- **(a)** "a complicated circuit" — an IC may be simple; complexity is not the defining property.
- **(b)** "an integrating device" — a pun on the word *integrate*; an integrator is an op-amp
  configuration, not what "integrated" means here.
- **(c)** "much costlier than a single transistor" — the opposite of the lesson's economics: the
  planar process applies **every step to every circuit on every wafer simultaneously** (·L5 p5),
  which is precisely what makes ICs **cheap per function**.

**There are no other exercises, tutorials or worked examples anywhere in L5.**

---

## 5.24 [added] Every list in this lesson, in one place

Everything below appears in the body with citations; this section is a revision sheet, not new
material.

**The four manufacturing stages** ·L5 p2
1. Material preparation → 2. Crystal growing and wafer preparation → 3. Wafer fabrication →
4. Testing, bonding and packaging.

**The seven wafer-fabrication processes** ·L5 p5
Oxidation · Etching · Diffusion · Ion implantation · Photolithography · Epitaxy ·
Metallization and interconnections.

**The four uses of SiO$_2$** ·L5 p6
Mask against implant/diffusion · surface passivation · device isolation · component in MOS
structures.

**The two diffusion steps** ·L5 p7
Pre-deposition (1000 °C, dopant supplied, shallow and heavy) → drive-in (1100 °C, no dopant, deeper
and lighter at the surface).

**Six advantages of ion implantation** ·L5 p9
Precise dose (measured as current) · regulated depth, very shallow possible · extreme dopant purity ·
uniform doping across the surface · directed beam, little lateral spread · room temperature, so no
thermal stress and photoresist may be the mask.

**Three disadvantages of ion implantation** ·L5 p9
Crystal damage (cured by annealing if not extensive) · equipment cost > US \$1 million · very toxic
dopant gases.

**The six photolithography steps** ·L5 p11
Bake at 100 °C → align plate → expose to UV → dissolve exposed resist in organic solvent → etch
exposed SiO$_2$ in hydrofluoric acid → strip remaining resist.

**Three metallization methods** ·L5 p13–p14
Resistance heating (tungsten coil) · electron-beam heating · sputtering. (Plus the RF-induction
variant with a boron nitride crucible.)

**Three chip-interconnection schemes** ·L5 p14
Wire bonding (thermosonic, thermocompression) · tape-automated bonding (TAB) · flip-chip solder
bonding.

**Two package categories** ·L5 p16
Through-hole mount (SIP, ZIP, DIP, PGA) · surface mount (SVP, SOP, TSOP, SOJ, QFP, QFJ, LCC, LCC
SOJ, BGA).

**The seven bipolar masks** ·L5 p20
1 buried layer · 2 isolation · 3 base · 4 N$^+$ emitter and collector contact · 5 contact windows ·
6 interconnection pattern · 7 bonding holes.

**The five NMOS masks** ·L5 p21–p22
1 FET areas (then P$^+$ channel stops and field oxide) · 2 gate region (then self-aligned N$^+$
source/drain) · 3 contact windows · 4 interconnection pattern · 5 bonding windows.

**Five MOS-vs-bipolar points** ·L5 p22
Cost (MOS) · DC power (MOS) · transconductance / analogue suitability (bipolar) · cut-off frequency
at equal geometry (MOS) · packing density (MOS). **Main MOS disadvantage: slower circuit speed.**

---

## 5.25 [added] Coverage map

| PDF page | Printed page | Content | Section here |
|---|---|---|---|
| p1 | — | §67.1 introduction; §67.2 what an IC is; Kilby and Noyce | §5.1 |
| p2 | — | §67.13 semiconductors used; §67.14 the four stages | §5.2, §5.3 |
| p3 | 2480 | Fig. 67.4 four-stage chain; §67.15 material preparation, Fig. 67.5; §67.16 crystal growth, Czochralski puller | §5.3, §5.4, §5.5 |
| p4 | 2481 | Fig. 67.6 puller; ingot growth sequence; wafer preparation; the flats code | §5.5 |
| p5 | 2482 | Fig. 67.7 four wafer-flat panels; slicing and polishing; §67.17 the seven processes; planar process | §5.5, §5.6 |
| p6 | 2483 | §67.18 oxidation, four uses; Fig. 67.8 oxide on substrate; Fig. 67.9 oxidation furnace; dry vs wet | §5.7 |
| p7 | 2484 | end of oxidation; §67.19 etching, wet vs dry/RIE; §67.20 diffusion; Fig. 67.10 doping profiles | §5.7, §5.8, §5.9 |
| p8 | 2485 | Fig. 67.11 diffusion furnace; drive-in; Fig. 67.12 diffusion through a window; §67.21 ion implantation | §5.9, §5.10 |
| p9 | 2486 | Fig. 67.13 ion implanter; six advantages, three disadvantages; §67.22 photomask generation | §5.10, §5.11 |
| p10 | 2487 | reticle, mask, wafer stepper; §67.23 photolithography; Fig. 67.14 six-panel sequence | §5.11, §5.12 |
| p11 | 2488 | the six numbered steps; positive vs negative photoresist; UV linewidth limit; §67.24 epitaxy begins | §5.12, §5.13 |
| p12 | 2489 | epitaxy vs diffusion; VPE/LPE/MBE; Fig. 67.15 VPE reactor; §67.25 metallization begins | §5.13, §5.14 |
| p13 | 2490 | ohmic contacts; why aluminium; resistance heating; Figs. 67.16, 67.17 | §5.14 |
| p14 | 2491 | electron-beam heating; sputtering; interconnection layer; §67.26 testing, bonding; Fig. 67.18 package cutaway | §5.14, §5.15 |
| p15 | 2492 | packaging construction; Fig. 67.19 full package classification tree | §5.15 |
| p16 | 2493 | through-hole vs surface mount; §67.27 element formation; resistors; the resistance equation; Fig. 67.21 | §5.15, §5.16 |
| p17 | 2494 | sheet resistance; capacitors — junction, MOS, trench; Figs. 67.22, 67.23; diodes in ICs | §5.16, §5.17, §5.18 |
| p18 | 2495 | discrete PN diode process; Fig. 67.24 eight panels; bipolar transistor starting material | §5.18, §5.19 |
| p19 | 2496 | Fig. 67.25 seven-panel NPN process | §5.19 |
| p20 | 2497 | the seven masks in full; isolation; buried layer; parasitic resistance | §5.19 |
| p21 | 2498 | Fig. 67.26 buried-layer comparison; §67.27 item 5 NMOS process begins; masks 1 and 2 | §5.19, §5.20 |
| p22 | 2499 | Fig. 67.27 seven-panel NMOS process; masks 3–5; §67.28 MOS vs bipolar, points 1–5 | §5.20, §5.21 |
| p23 | 2500 | MOS disadvantage and why MOS dominates; §67.29 applications; Objective Test 67 Q1–Q2 | §5.21, §5.22, §5.23 |

**Verification summary for this file:** **9 substantive flags (`V5.1`–`V5.9`)** and **12 cosmetic
flags (`C5.1`–`C5.12`)**, **21 in total**. The lesson contains **one equation**, which has been
dimensionally checked and found to be missing its denominator brackets (`V5.4`); **no worked
examples**; and **two objective-test questions**, both answered in §5.23. The two resistivity
figures on ·L5 p2 were recomputed from first principles and both check out. **One item is marked
⚠ ILLEGIBLE: the photograph Fig. 67.20 on ·L5 p16.**

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
