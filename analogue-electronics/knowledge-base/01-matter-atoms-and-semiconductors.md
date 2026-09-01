---
kb: "Analogue Electronics I — BEE 3103"
course_code: "BEE 3103"
lecturer: "withheld"
section: "01 — Matter, Atomic Structure and Semiconductor Materials"
source: "J — 'Analogue Electronics I Lecture Notes', 100 pp. (primary), pp. 2-9"
pages: "J p2-p9"
tier: primary
file_role: topic
subtopics:
  - "what electronics is; the two words the notes derive it from"
  - "analogue signals: waveform, peak value, peak-to-peak value, period, characteristics"
  - "digital signals: pulse train, characteristics, analogue-to-digital conversion"
  - "applications of electronics across nine fields"
  - "physical states of matter: solid, liquid, gas"
  - "chemical states of matter: elements, compounds, mixtures"
  - "the first twenty elements with symbols and atomic numbers"
  - "molecule, atom, electric charge"
  - "the electron theory: nucleus, electron, proton, neutron, shell, sub-shell, forbidden gap"
  - "the Bohr model and the two Bohr postulates; hf = Ei - Ef"
  - "the exclusion principle; shell capacity 2n^2 and sub-shell capacity 2 + 4(m-1)"
  - "worked example: maximum electrons in the third shell"
  - "atomic number and atomic weight; shell-structure notation"
  - "valence electrons, free electrons, cations, anions, ions"
  - "energies that change electrical balance"
  - "conduction in a gas by ionisation; conduction in a vacuum"
  - "conductors, insulators and semiconductors: valence count, bonding, band gap, band diagrams"
  - "intrinsic semiconductors and the silicon covalent lattice"
  - "extrinsic semiconductors: P-type by trivalent doping, N-type by pentavalent doping"
  - "majority and minority carriers; acceptor and donor; direction of carrier motion"
  - "charge and the relation Q = It"
key_equations: [shell-electrons, subshell-electrons, bohr-transition, charge-current-time]
prerequisites: ["none — this is the entry point of the course"]
leads_to: ["diodes (the P-N junction formed by joining the P-type and N-type material defined here)", "semiconductor device fabrication", "conduction, resistivity and the temperature coefficient (reference tier RD2)"]
verification_flags: 22
tags: [electronics, analogue-signal, digital-signal, matter, elements, atom, electron-theory, bohr-model, exclusion-principle, shells, sub-shells, forbidden-gap, valence-electrons, ionisation, conductors, insulators, semiconductors, energy-bands, band-gap, intrinsic, extrinsic, doping, p-type, n-type, majority-carriers, charge]
---

<!-- Compiled by Jotham-JS, 2026. BEE 3103 Analogue Electronics I knowledge base. -->

<!-- TAG LEGEND (shared across all topic files):
  [def] definition · [derivation] step-by-step derivation · [eq] key equation ·
  [ex] worked example (with the lecturer's numbers) · [exercise] unsolved problem set for the student ·
  [fig] figure/diagram described from the rendered page · [table] tabulated data or comparison ·
  [added] supplied here, NOT in the source ·
  ·J pN = provenance (which PDF page of the lecture notes the item comes from) ·
  ⚠ VERIFY = flagged suspected error in the source; detail in _verification-log.md ·
  ⚠ ILLEGIBLE = page or figure that could not be interpreted ·
  ⚠ REDACTED = text destroyed by an opaque block in the source PDF.
  Equations are written in canonical LaTeX; where the printed form was garbled or shorthand,
  the canonical form is given and any real discrepancy is flagged (not silently changed). -->

# 01 — Matter, Atomic Structure and Semiconductor Materials

Scope: ·J p2 to ·J p9, the opening block of the course's own lecture notes. It defines electronics,
separates analogue from digital signals, lists where electronics is applied, then descends through
matter → elements → atoms → electrons → shells → energy bands → conductors, insulators and
semiconductors → doped silicon, and closes on the definition of charge.

This is the foundational block. It is **almost entirely definitions, classifications and diagrams** —
there is exactly one piece of arithmetic in eight pages. Read it for vocabulary and for the four
diagrams that get re-used for the rest of the course.

---

## 1.0 What this document is, and how it is cited

**Citation.** Claims carry `·J pN`, meaning **PDF page N** of the lecture notes.

The document's own printed page number runs **one behind the PDF page** — PDF p2 shows printed "1",
PDF p9 shows printed "8" — and the offset holds unbroken to the end of the document. **This file
cites PDF pages only.** Where a tutorial or exam works from a printed copy, subtract one.

·J p1 is a document-sharing cover sheet and carries no course content. The notes begin on ·J p2.

[table] **Page map for this file**

| ·J page | Printed | What is on it |
|---|---|---|
| p2 | 1 | What electronics is; analogue signal with waveform; digital signal with pulse train; characteristics of each |
| p3 | 2 | Applications of electronics (list continues from a lost heading); physical and chemical states of matter; element defined; the first-twenty-elements table |
| p4 | 3 | Tail of the compounds definition; mixtures; molecule; atom; electric charge; **THE ELECTRON THEORY**; the shell / sub-shell / forbidden-gap atom diagram |
| p5 | 4 | Bohr; nucleus, electron, proton, neutron, shell, sub-shell, forbidden gap defined; the two Bohr postulates and $hf = E_i - E_f$; **THE EXCLUSION PRINCIPLE**; sub-shell capacity list |
| p6 | 5 | Worked example — maximum electrons in the third shell; **ATOMIC NUMBER & ATOMIC WEIGHT**; **VALENCE ELECTRONS**, ions; energies that change electrical balance; conduction in a gas with the discharge-tube figure |
| p7 | 6 | Conduction in a vacuum (one line); **Material used in electrical & electronic circuits**; conductors with band diagram; insulators with band diagram; semiconductors |
| p8 | 7 | Semiconductor band diagram (part); intrinsic semiconductors and the silicon covalent lattice; extrinsic semiconductors; P-type opening |
| p9 | 8 | P-type lattice with the hole; N-type with the free-electron lattice; **Terms and concepts** — charge, $Q = It$ |

### Gaps to know about before working from this file

Five places in this range where the source itself is incomplete. **Nothing below is invented to
paper over them.**

1. **·J p2 opens with no heading.** The notes begin directly with "Electronics is the study of…".
   Whatever section title stood above it is not in the document.
2. **·J p2 → ·J p3: the applications heading and the first items of the list are absent.**
   ·J p2 ends after the digital-signal characteristics with the rest of the page blank; ·J p3 opens
   mid-list at "Communication – satellites". §1.3 lists what survives, in order.
3. **·J p3 → ·J p4: the *Compounds* definition is absent.** ·J p3 ends with the elements table;
   ·J p4 opens with the fragment "MgO, H₂O etc.", which is the tail of a compounds bullet. A
   standard definition is supplied in §1.5 and is clearly marked `[added]`.
4. **·J p6 → ·J p7: the conduction-in-a-vacuum heading and its opening are absent.** ·J p7 begins
   with the bare sentence "A vacuum can only conduct electromagnetic waves e.g. light". **Conduction
   in liquids is never treated at all**, although ·J p2 names liquids as one of the four media.
5. **·J p7 → ·J p8: the semiconductor energy-band diagram is cut by the page break.** Only the
   forbidden band and the valence band survive at the top of ·J p8; the conduction-band rectangle
   and its label are not in the document. See **JC1.11**.

**No opaque redaction blocks and no illegible passages occur anywhere in ·J p2–p9.** Every word and
every figure in this range was readable.

### Where this sits against the reference tier

Reference deck **RD2, *Materials Used in Electrical & Electronic Circuits*** (`_reference-decks.md`
§2), covers the same ground as ·J p7–p9 slide for slide. §1.16 sets out exactly where the two agree,
where RD2 adds material these notes lack, and the one place they pull apart. Read §1.16 before
revising the materials half of this file.

---

## 1.1 What electronics is ·J p2

[def] **Electronics** is the study of **conduction current in solids, gases, vacuum and liquids**.
·J p2

The notes give three further framings, all on ·J p2:

- It is a branch of engineering formed from two words — **electron**, the negatively charged particle
  in an atom, and **mechanics**, the study of the motion of an electron.
- It is the study of electrons and how they can be used to perform different functions.
- **The ability to control the movement of electrons — electron flow — is the basis of electronics.**

The notes name four fields it specialises in: **digital computers, audio systems, communication
systems and automatic control**. ·J p2

> ⚠ VERIFY **JC1.13** ·J p2 — the etymology is printed as "comes from the 2 words: Electrons … ,
> Mechanics – Study of motion of an electron". *Mechanics* is the study of motion in general, not of
> electrons in particular, and the accepted derivation of *electronics* is **electron + -ics**, not
> a compound of *electron* and *mechanics*. Harmless as a mnemonic; wrong as etymology.
> See `_verification-log.md`.

Note the deliberate breadth of the definition: **all four media** — solid, gas, vacuum, liquid.
Conduction in a solid occupies §1.12 onwards, conduction in a gas §1.11. Vacuum gets one line.
Liquids are promised here and never delivered (gap 4 above).

---

## 1.2 Analogue and digital signals ·J p2

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $V_p$ | peak value — axis to crest | V | 1–10 V |
| $V_{pp}$ | peak-to-peak value — crest to trough | V | $2V_p$ |
| $T$ | period of one complete cycle | s | ms to µs |
| $t$ | time (horizontal axis of both waveforms) | s | — |

*(The notes label the waveform in words — "Peak Value", "Peak to Peak value", "Period cycle" — and
attach no symbols to them. The symbols above are `[added]` for use later in the course.)*

### The analogue signal

[def] An **analogue signal** is one whose **amplitude changes with time continuously**. ·J p2

[fig] **·J p2 — the analogue waveform.** One complete sine cycle drawn on a pair of axes.

- Vertical axis of amplitude, marked **0** at the origin where it meets the horizontal axis.
  Horizontal axis of time running to the right, arrowhead at the far right.
- The curve starts on the vertical axis at zero, rises to a rounded **positive crest** in the first
  quarter, falls back through the axis at the half-way point, drops to a **negative trough**, then
  turns back up towards the axis at the right-hand end. One full cycle, no more.
- A **single-headed vertical arrow** runs from the time axis up to the crest, labelled
  **"Peak Value"**.
- A **double-headed vertical arrow** stands over the second half of the cycle, its upper head level
  with the crest and its lower head at the trough, labelled **"Peak to Peak value"**.
- A **double-headed horizontal arrow** runs below the whole waveform from the start of the cycle to
  its end, labelled **"Period cycle"**.

Three quantities are therefore defined off this one picture: **peak value** (axis to crest),
**peak-to-peak value** (crest to trough) and **period** (one complete cycle along the time axis).

[table] **Characteristics of analogue signals** ·J p2

| # | Characteristic |
|---|---|
| 1 | Varies **continuously** with time |
| 2 | **Typical of nature** — e.g. light, waves, voice |
| 3 | Has been in use for **the last 100 years** |

### The digital signal

[fig] **·J p2 — the digital waveform.** A rectangular pulse train on the same pair of axes.

- Vertical axis at the left; horizontal axis labelled **"time"** with an arrowhead at the right. The
  vertical axis is drawn long, extending well below the horizontal axis.
- Five cells sit in a row along the axis, read left to right as **1, 0, 1, 0, 1**.
- The **1** cells are drawn as raised rectangular boxes standing on the time axis; the **0** labels
  sit between them at the lower level. The result is a two-level square wave alternating high-low-
  high-low-high.
- No amplitude scale, no time scale — the figure carries only the bit values.

[table] **Characteristics of digital signals** ·J p2

| # | Characteristic |
|---|---|
| 1 | **Do not vary with time** — occur in **discrete** form |
| 2 | **Typical of technology**; produced from analogue signals by **analogue-to-digital conversion** |
| 3 | Have been in use for **about 50 years**, since the invention of vacuum tubes and transistors |

[added] The contrast the notes are drawing, in one line: **analogue is continuous and comes from
nature; digital is discrete and is manufactured from analogue by conversion.** Characteristic 1 for
digital is loosely worded — a digital signal obviously changes *value* with time; what it does not do
is take a *continuum* of values. The intended contrast is continuous versus discrete amplitude.

---

## 1.3 Applications of electronics ·J p3

The list below begins where the document begins — the heading and any items above
"Communication – satellites" are not in the PDF (gap 2 in §1.0).

[table] **Fields of application, in the notes' own order** ·J p3

| Field | Example given |
|---|---|
| Communication | satellites |
| Medicine | — |
| Entertainment | "3 stereos", HIFI systems, iPod |
| Industrial applications | assembly lines |
| Transport | autopilot, tracking systems, missile guiding |
| Military / defence / security | biometrics |
| Astronomy | — |
| Instrumentation | electronic pianos |
| Radar | radio detection and ranging — "can be used for all the above, e.g. in medicine to detect cancer" |

Radar is printed as running text below the list rather than as a list item, and is given a
cross-cutting role: it serves every field above it.

> ⚠ VERIFY **JC1.14** ·J p3 — the entertainment entry prints "**3** stereos, HIFI systems, Ipod".
> The bare "3" is a stray token; the item is a list of three consumer audio products and the digit
> does not belong to any of them. Nothing computed depends on it.
> See `_verification-log.md`.

---

## 1.4 Physical and chemical states of matter ·J p3

[def] **Matter** is anything that **occupies space and has weight**. ·J p3

[def] The **basic building block of matter is an atom**. ·J p3

### The three physical states

Matter exists in **three physical states** ·J p3 —

1. **Solid**
2. **Liquid**
3. **Gas**

and the notes attach one consequence:

- When matter exists as a **liquid or a gas, its dimensions are determined by the container**. ·J p3

[added] The implication for a solid, which the notes leave unstated, is that a solid holds its own
shape and dimensions independently of any container.

### The three chemical states

**Chemical states of matter** ·J p3 —

1. **Elements**
2. **Compounds**
3. **Mixtures**

Keep the two triples apart. *Solid / liquid / gas* is a **physical** classification — the same
substance moves between them. *Element / compound / mixture* is a **chemical** classification — it
is about what the substance is made of.

---

## 1.5 Elements, compounds, mixtures, molecules, atoms and charge ·J p3–p4

[def] An **element** is a substance that **cannot be broken into simpler substances**. It has **only
one kind of atom** — e.g. Mg, K, Na, oxygen. ·J p3

[def] A **mixture** is a combination of substances in which **the individual elements possess the
same properties as when they were alone** — e.g. air. ·J p4

[added] **The compounds definition is missing from the document** (gap 3 in §1.0). ·J p3 ends with
the elements table and ·J p4 opens with the bare fragment "MgO, H₂O etc." — the tail of a compounds
bullet whose opening was lost. The examples make the subject certain but not the wording, so the
following is **ours, not the notes'**: a **compound** is a substance formed when two or more elements
combine **chemically** in fixed proportion; the product has properties different from those of its
constituent elements, which is precisely what separates it from a mixture. Both of the notes'
examples fit — magnesium oxide, MgO, and water, H₂O.

### The two "smallest particle" definitions

These two sit one after the other on ·J p4 and are the pair most often confused.

[def] The **smallest particle into which a compound can be divided and still retain its physical
properties** is a **molecule**. ·J p4

[def] The **smallest particle into which an element can be divided and still retain its chemical
properties** is an **atom**. ·J p4

All matter is composed of atoms and molecules. ·J p4

[added] Note the asymmetry in the notes' phrasing — *compound → molecule → physical properties* but
*element → atom → chemical properties*. That is how the page prints it and it is worth memorising in
that shape, because it is the form a definition question would be marked against.

### Electric charge

[def] **Electric charge** is the **quantity of electricity in a body**. ·J p4

A second, looser definition of charge appears at the very end of this range, on ·J p9, together with
$Q = It$ — see §1.15.

### The first twenty elements

[table] **·J p3 — the first twenty elements: name, symbol, atomic number.** Reproduced in full and in
the notes' own order.

| Element | Symbol | Atomic number |
|---|---|---|
| Hydrogen | H | 1 |
| Helium | He | 2 |
| Lithium | Li | 3 |
| Beryllium | Be | 4 |
| Boron | B | 5 |
| Carbon | C | 6 |
| Nitrogen | N | 7 |
| Oxygen | O | 8 |
| Fluorine | F | 9 |
| Neon | Ne | 10 |
| Sodium | Na | 11 |
| Magnesium | Mg | 12 |
| Aluminium | Al | 13 |
| Silicon | Si | 14 |
| Phosphorous | P | 15 |
| Sulphur | S | 16 |
| Chlorine | Cl | 17 |
| Argon | Ar | 18 |
| Potassium | K | 19 |
| Calcium | Ca | 20 |

Every symbol and every atomic number in the table was checked against the periodic table and **all
twenty are correct**. The table carries no column headings in the source; the three columns are
name, symbol and atomic number.

> ⚠ VERIFY **JC1.6** ·J p3 — element 15 is printed **"Phosphorous"**. The element is
> **phosphorus**; *phosphorous* is the adjective (and names the P(III) acid, H₃PO₃). The same
> spelling recurs on ·J p9 in the N-type doping list. Cosmetic only.
> See `_verification-log.md`.

**Three of these twenty carry the rest of the course.** Silicon (14) is the semiconductor of §1.13,
boron (5) is the P-type dopant of §1.14 and phosphorus (15) is the N-type dopant. Their positions in
this table are what fix their valence, and their valence is what makes the doping work.

---

## 1.6 The electron theory ·J p4–p5

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $N$ | number of electrons a shell can hold | — (a count) | 2, 8, 18, 32 |
| $n$ | shell number, counted outwards from the nucleus | — | 1 to 7 |
| $m$ | sub-shell number within a shell | — | 1 to 6 |
| $h$ | Planck's constant | J·s | $6.626\times10^{-34}$ |
| $f$ | frequency of the emitted photon | Hz | — |
| $E_i$ | energy of the initial state | J (or eV) | — |
| $E_f$ | energy of the final state | J (or eV) | — |

**Watch $N$ against $n$.** ·J p5 uses capital $N$ for the *count of electrons* and lower-case $n$ for
the *shell number*. The worked example on ·J p6 then writes "N = 3" for the shell number, swapping
the two. Flagged as **JC1.4**; the file uses $n$ for the shell number throughout.

### The picture the notes start from

Five statements, all ·J p4:

- Every atom has **one or more electrons and one nucleus**. The nucleus contains the **protons and
  neutrons**.
- The **simplest atom is hydrogen** — one electron orbiting the nucleus.
- The **charge on an electron is negative**, on a **proton positive**, and a **neutron is neutral**.
- A **normal atom is electrically neutral**: it contains equal numbers of positive and negative
  charges.
- Therefore the **charge per electron and per proton is equal in magnitude but opposite in
  polarity**.

> ⚠ VERIFY **JV1.1** ·J p4 — the page prints *"The nucleus has only one proton apart. In a simple
> hydrogen atom the nucleus is made of protons and neutrons of approximately equal numbers."*
> **The ordinary hydrogen atom has one proton and no neutron at all** — that is what makes it the
> simplest atom, as the bullet above it says. The sentence has been split in the wrong place. It
> should read:
> $$\boxed{\;\text{hydrogen nucleus} = 1\ \text{proton},\ 0\ \text{neutrons};\quad
> \text{heavier nuclei} \approx \text{equal numbers of protons and neutrons}\;}$$
> Check: the "approximately equal numbers" claim is true of light-to-medium nuclei generally
> (carbon-12 is 6 p, 6 n) — it is only its attachment to *hydrogen* that is wrong.
> See `_verification-log.md`.

> ⚠ VERIFY **JC1.5** ·J p4 — the neutrality bullet prints "an equal number of **+vely charged
> atoms** and –vely charged electrons". It should read **+vely charged protons**. The next clause of
> the same sentence — "the charge per electron and proton is equal but opposite" — corrects it, so
> nothing downstream is affected.
> See `_verification-log.md`.

### [fig] ·J p4 — the shell, sub-shell and forbidden-gap atom diagram

The single most re-usable picture in this range. Described in enough detail to redraw.

**Rings.** **Eight concentric rings** about a common centre — **five solid and three dashed**, and
**not** in a strictly alternating order. Counting **outwards from the nucleus**, the sequence is:

$$\text{solid} \to \text{dashed} \to \text{solid} \to \text{solid} \to \text{dashed} \to
\text{dashed} \to \text{solid} \to \text{solid (outermost and largest)}$$

(Ring radii were measured off the render along a clean downward ray to fix this order; the rings are
hand-drawn and not exactly concentric, so their spacing is uneven.)

**Centre.** Inside the innermost solid circle sit two marks —

- a **small open circle**, roughly at the centre, and
- a **filled black oval** immediately above and to the right of it.

**Electrons.** Two **×** marks are drawn, one sitting on a dashed ring in the upper part of the
figure and one just to the right of the black oval. The **×** is the notes' symbol for an electron
throughout this document — it reappears on every lattice diagram in §1.13 and §1.14.

**Labels and their leader lines** (six labels, seven leaders):

| Label | Position | Where its arrow lands |
|---|---|---|
| **Electron** | top centre | down onto the **×** on the upper dashed ring |
| **Sub Shells** | upper left | **two** arrows — one long vertical arrow down into the annulus between the two outermost circles, one diagonal arrow onto a dashed ring |
| **Forbidden gap** | left | horizontally right, into the annulus between a dashed ring and the solid ring inside it |
| **Nucleus** | upper right | diagonally down-left, into the innermost solid circle beside the black oval |
| **Proton** | right | horizontally left, onto the **filled black oval** |
| **Neutron** | right | horizontally left, onto the **small open circle** |
| **Shell** | lower right | up and to the left, onto the **second ring out from the nucleus — a dashed one** |

> ⚠ VERIFY **JC1.12** ·J p4 — the figure's leader lines **do not separate the solid rings from the
> dashed rings**: the "Shell" arrow terminates on a **dashed** ring while one of the two "Sub Shells"
> arrows terminates in the annulus between the two outermost rings, which are **both solid**. The
> line styles themselves do not alternate either — the order outwards is solid, dashed, solid,
> solid, dashed, dashed, solid, solid. The picture alone therefore does not
> establish which line style means *shell* and which means *sub-shell*. Take it from the text
> instead — ·J p5 defines a shell as containing several sub-shells, so the **solid rings are shells
> and the dashed rings the sub-shells inside them**, with the forbidden gap in between.
> See `_verification-log.md`.

> ⚠ VERIFY **JV1.3** ·J p5 — the text below the figure states *"The figure above shows the structure
> of a carbon atom."* **It does not.** Carbon is element 6, shell structure **2:4** — **two**
> shells and **six** electrons. The figure draws **eight rings** — five solid, three dashed — and
> only **two × marks**. Neither count fits carbon on any reading. It is a generic
> shell / sub-shell / forbidden-gap schematic, and reading it as carbon will produce the wrong shell
> count and the wrong electron count in any question that asks for them. Correct carbon:
> $$\boxed{\;\mathrm{C}:\ Z = 6,\quad \text{shells } 2\!:\!4,\quad 4\ \text{valence electrons}\;}$$
> Check: $2 + 4 = 6 = Z$. That four-valence-electron structure is exactly what §1.12 needs when it
> classifies carbon-family materials as semiconductors.
> See `_verification-log.md`.

### The Bohr model ·J p5

The notes credit the shell model to Bohr and give the two postulates.

- He **restricted the orbits of atomic electrons to well-defined shells or levels** — electrons do
  not crowd together in a mass, they move round in different orbits. ·J p5
- An **atomic level of such orbits is a shell**, defined as **the spherical orbit of an electron or
  electrons**. ·J p5

> ⚠ VERIFY **JC1.1** ·J p5 — the physicist is printed **"Neil Bohrls"** in the first bullet and
> **"Bohrl"** twice below it. The name is **Niels Bohr**. Cosmetic; the physics is unaffected.
> See `_verification-log.md`.

**First postulate** ·J p5 — an electron in an atom can revolve in **certain specified orbits without
the emission of radiant energy**. This is what explains **the stability of the atom**.

**Second postulate** ·J p5 — an electron may make a **transition from one specified non-radiating
orbit to another of lower energy**. When it does so a single quantum of light is emitted, whose
energy is the difference between the initial and final states and whose frequency $f$ follows:

[eq: bohr-transition] ·J p5

$$\boxed{\;h f = E_i - E_f\;}$$

- $h$ — Planck's constant, J·s ($6.626\times10^{-34}$ J·s)
- $f$ — frequency of the emitted radiation, Hz
- $E_i$ — energy of the initial state, J
- $E_f$ — energy of the final state, J

> ⚠ VERIFY **JV1.2** ·J p5 — the sentence introducing this equation prints *"a single **proton** is
> emitted"*. It is a **photon** — a quantum of electromagnetic radiation. A proton is a nuclear
> particle and cannot be emitted by an orbital transition; if one were, the atom would change
> element. The equation itself is right and is the giveaway: $hf$ is a photon energy.
> $$\boxed{\;\text{a single photon is emitted, of energy } E_i - E_f \text{ and frequency } f = (E_i - E_f)/h\;}$$
> See `_verification-log.md`.

[added] Two consequences worth carrying forward, neither stated on the page. First, $E_i > E_f$
always, since $f > 0$ — the transition is downward. Second, this is the same $hf$ that reappears
later in the course for photodiodes and LEDs, where the band gap $E_g$ of §1.12 replaces
$E_i - E_f$.

### The six structural definitions ·J p5

Learn these six as a block. They are the vocabulary the rest of the course assumes.

[def] **Nucleus** — the **innermost part of an atom**. It contains **protons and neutrons**.

[def] **Electron** — a **negatively charged particle revolving in specified orbits called quantum
energy levels**.

[def] **Proton** — a **positively charged particle in the nucleus**.

[def] **Neutron** — a **particle with no charge in the nucleus**.

[def] **Shell** — the **section where electrons orbit**. It has **sub-shells and quantum energy
levels**. The number of electrons a shell can hold is

[eq: shell-electrons] ·J p5

$$\boxed{\;N = 2n^{2}\;}$$

- $N$ — number of electrons in the shell (a count)
- $n$ — the shell number, counted outwards from the nucleus

[def] **Sub-shell** — a **section with electrons inside a shell**; **several sub-shells make a
shell**. The number of electrons in a sub-shell is

[eq: subshell-electrons] ·J p5

$$\boxed{\;N_{\text{sub}} = 2 + 4(m-1)\;}$$

- $N_{\text{sub}}$ — number of electrons in that sub-shell (a count)
- $m$ — the sub-shell number within the shell

[def] **Forbidden gap** — the **section where electrons cannot orbit**. It lies **between two
sub-shells**.

The forbidden gap is the single most important idea on this page. Widen it and the material becomes
an insulator; close it and the material becomes a conductor. That is the whole of §1.12.

---

## 1.7 The exclusion principle ·J p5

[def] **The exclusion principle** — **no two electrons can occupy the same quantum-mechanical state**,
since different states correspond to different distances from the nucleus. ·J p5

> ⚠ VERIFY **JC1.2** ·J p5 — printed as **"Paul's exclusion principle"**. It is the **Pauli**
> exclusion principle, after Wolfgang Pauli. Cosmetic.
> See `_verification-log.md`.

The consequence the notes draw ·J p5:

- In a **complex atom there is no room for all the electrons in states near the nucleus**.
- Some are therefore **forced into states further away, having higher energies**.

That is why atoms have a shell structure at all, and why the outermost electrons — the ones §1.9
calls valence electrons — are the loosest bound.

The page then restates the two capacity formulas:

- **Maximum electrons per shell** $= 2n^2$, where $n$ is the shell number counting outwards from the
  nucleus.
- **Sub-shell electrons** $= 2 + 4(m-1)$, where $m$ is the sub-shell number.

[table] **·J p5 — the sub-shell capacities, shell by shell.** Reproduced exactly as printed. The
notes write "é" for *electron*.

| Shell | Sub-shell capacities, in order |
|---|---|
| 1st | 2é |
| 2nd | 2é, 6é |
| 3rd | 2é, 6é, 10é |
| 4th | 2é, 6é, 10é, 14é |
| 5th | 2é, 6é, 10é, 14é, 18é |
| 6th | 2é, 6é, 10é, 14é, 18é, 22é |

[added] **The table and the $2n^2$ rule are consistent — verified.** Summing each row must reproduce
$2n^2$ for that shell, and it does:

$$2 + 4(m-1) \text{ for } m = 1,2,3,4,5,6 \;\Rightarrow\; 2,\;6,\;10,\;14,\;18,\;22$$

$$\text{running totals} \;=\; 2,\;8,\;18,\;32,\;50,\;72$$

$$2n^{2} \text{ for } n = 1,2,3,4,5,6 \;=\; 2,\;8,\;18,\;32,\;50,\;72 \quad\checkmark$$

Every row agrees. The $n$th shell contains exactly $n$ sub-shells, and the capacities of those $n$
sub-shells sum to $2n^2$. This is the internal check to run in an exam if either formula is
half-remembered.

---

## 1.8 [ex] Maximum electrons in the third shell ·J p6

The one worked calculation in ·J p2–p9. It sits at the top of ·J p6, directly continuing the
exclusion-principle material of ·J p5.

**Problem.** Determine the maximum number of electrons in the 3rd shell. ·J p6

**As the notes work it** ·J p6:

$$\text{Max No} = 2^{n}$$
$$N = 3$$
$$= 2 \times 3^{2}$$
$$= 18\ \text{es}$$

("es" is the notes' abbreviation for *electrons*.)

**The answer, 18 electrons, is correct.** The formula written above it is not.

> ⚠ VERIFY **JV1.4** ·J p6 — the first line prints **"Max No $= 2^{n}$"**, with $n$ as an exponent.
> The rule stated twice on ·J p5 is $N = 2n^{2}$ — the shell number is **squared and multiplied by
> two**, not used as an exponent of two. The printed formula **contradicts its own next line**: the
> working substitutes $2 \times 3^{2}$, which is $2n^2$, not $2^n$. Correct form:
> $$\boxed{\;N = 2n^{2}\;}$$
> Check: with $n = 3$, the printed $2^{n}$ gives $2^{3} = 8$, while $2n^{2}$ gives
> $2 \times 9 = 18$ — the answer the page itself prints. The two rules only ever agree at $n = 1$
> (both give 2); at $n = 2$ they give 4 against 8, at $n = 4$ 16 against 32.
> See `_verification-log.md`.

> ⚠ VERIFY **JC1.4** ·J p6 — the second line prints **"N = 3"**, using capital $N$ for the **shell
> number**. On ·J p5 capital $N$ is the **number of electrons** and lower-case $n$ is the shell
> number. Same page-pair, two meanings, and here the letter that should be the *answer* is used for
> the *input*. Should read $n = 3$. Nothing computed changes.
> See `_verification-log.md`.

[added] **The calculation done cleanly.**

$$N = 2n^{2}$$
$$n = 3$$
$$N = 2 \times 3^{2}$$
$$N = 2 \times 9$$
$$\boxed{\;N = 18\ \text{electrons}\;}$$

Cross-check against §1.7: the third shell's sub-shells hold $2 + 6 + 10 = 18$ electrons. Agreed.

[exercise] [added] The obvious companions, since a CAT can lift this example verbatim with a
different shell number. Worked here so the pattern is visible.

- **4th shell:** $N = 2 \times 4^{2} = 2 \times 16 = \boxed{32}$. Sub-shell check:
  $2+6+10+14 = 32$. ✓
- **5th shell:** $N = 2 \times 5^{2} = 2 \times 25 = \boxed{50}$. Sub-shell check:
  $2+6+10+14+18 = 50$. ✓
- **2nd shell:** $N = 2 \times 2^{2} = \boxed{8}$ — the octet, and the reason §1.9's "full at 8"
  rule works for the second shell.

---

## 1.9 Atomic number and atomic weight ·J p6

[def] The **atomic number** of an element is determined by the **number of protons in each of its
atoms**. ·J p6

[def] The **atomic weight** of an element is determined by comparing the weight of its atoms with
that of **carbon = 12**. ·J p6

> ⚠ VERIFY **JC1.9** ·J p6 — the atomic-weight sentence prints *"determined by comparing the weight
> of it's atoms of carbon = 12"* — the object of the comparison has been dropped, leaving a sentence
> that says nothing. It should read *"…by comparing the weight of its atoms **with that of an atom
> of** carbon, taken as 12"*. The definition is standard once the missing words are restored.
> See `_verification-log.md`.

The page gives two examples of **shell-structure notation** — the atomic number, then the electron
count in each shell from the innermost outwards.

[table] **·J p6 — shell structures as printed**

| Element | Atomic number | Shell structure as printed | Sum | Correct? |
|---|---|---|---|---|
| B (boron) | 5 | 2 : 3 | 5 | ✓ |
| S (sulphur) | 16 | 2 . 3 . 6 | 11 | ✗ — see JV1.5 |

> ⚠ VERIFY **JV1.5** ·J p6 — sulphur's structure is printed **"S = 16  2.3.6"**. The three shell
> occupancies must sum to the atomic number, and $2 + 3 + 6 = 11 \neq 16$. The middle figure is
> wrong: the second shell holds **8**, not 3. Correct form:
> $$\boxed{\;\mathrm{S}:\ Z = 16,\quad 2\,.\,8\,.\,6\;}$$
> Check: $2 + 8 + 6 = 16 = Z$. ✓ The boron line on the same page is right — $2 + 3 = 5$ — so the
> notation itself is sound; only the sulphur figure slipped. Note also that the correct second-shell
> occupancy 8 is exactly the $2n^2$ capacity computed in §1.8, and that ·J p8 and ·J p9 both print
> silicon as **2:8:4** and phosphorus as **2:8:5** — an 8 in the middle in every other instance in
> the document.
> See `_verification-log.md`.

[added] The three structures the rest of this file needs, all verified against $Z$:

$$\mathrm{B}:\ 2\!:\!3 \;(Z=5)\qquad \mathrm{Si}:\ 2\!:\!8\!:\!4 \;(Z=14)\qquad
\mathrm{P}:\ 2\!:\!8\!:\!5 \;(Z=15)$$

Boron's outer shell holds **3** — trivalent. Silicon's holds **4** — tetravalent. Phosphorus's holds
**5** — pentavalent. Those three numbers are the entire mechanism of doping in §1.14.

---

## 1.10 Valence electrons and ions ·J p6

[def] **Valence electrons** are those electrons **in the outermost shell of an atom**. ·J p6

The number of valence electrons **determines the atom's stability or instability, both electrically
and chemically**. ·J p6

> ⚠ VERIFY **JC1.3** ·J p6 — the heading is printed **"VALENCE ELECTORNS (State electron)"**. Two
> problems, both cosmetic. **"ELECTORNS"** is a transposition of **ELECTRONS**. The parenthetical
> **"(State electron)"** does not resolve — the likeliest reading is *stable electron*, but the
> surrounding text does not make it certain and it is **not** supplied here. Treat the parenthesis as
> unreadable intent, not as content.
> See `_verification-log.md`.

### The stability rule ·J p6

- For atoms with **more than one shell**, the outermost shell is **full when it holds 8 electrons**.
- If the atom has **fewer than 8** electrons in the outermost shell, it is **electrically and
  chemically unstable and active**.

> ⚠ VERIFY **JC1.7** ·J p6 — printed as *"For all the atoms with two **shall** the outermost shell
> is full when it has 8 es if the atom if the atom has fewer than 8es…"*. Two slips in one sentence:
> **"shall" for "shells"**, and **"if the atom" printed twice**. The rule itself is the standard
> octet rule and is stated correctly once the typing is cleaned up.
> See `_verification-log.md`.

[added] **This rule and the $2n^2$ rule of §1.8 are both true and they are not in conflict** — the
notes simply never reconcile them, and the clash trips students every year.

- $N = 2n^2$ is the **physical capacity** of a shell: the third shell *can* hold 18 electrons.
- The **octet rule** governs **chemical stability of the outermost shell**: a shell that is
  *currently outermost* behaves as full at 8.

So the third shell of, say, argon holds 8 and argon is inert; the third shell of a transition metal
part-way through filling holds more. Both statements stand.

### Free electrons and ions ·J p6

- **Electrically, valence electrons can be moved out of their own atoms** and are then sometimes
  called **free electrons**.
- It is possible to **detach an orbital electron from an atom**, leaving the atom with an **excess
  positive charge**. The atom in this state is a **positive ion**, or **cation**.
- Alternatively a neutral atom may be **given an additional orbital electron**, in which case it
  assumes a **negative charge**. This is a **negative ion**, or **anion**.

[def] An **ion** is **any atom that is not electrically balanced** — one that has **gained or lost
electrons**. ·J p6

> ⚠ VERIFY **JC1.8** ·J p6 — the cation bullet prints *"leaving the atom with an **access the
> charge**"*. Read **"an excess positive charge"** — losing a negative electron leaves net positive.
> The next sentence naming it a "+ve ion or cation" confirms the sign, so nothing is ambiguous.
> See `_verification-log.md`.

[table] **Ion summary** — the notes' content, tabulated `[added]` for revision

| Process | Charge left on the atom | Name | Also called |
|---|---|---|---|
| Loses an electron | positive | positive ion | **cation** |
| Gains an electron | negative | negative ion | **anion** |

### Energies that change electrical balance ·J p6

Five energy forms are listed, lettered a–e in the source:

| | Energy | Example given |
|---|---|---|
| a | **Chemical** | dry cells, batteries |
| b | **Mechanical** | generators |
| c | **Light** | — |
| d | **Heat** | friction |
| e | **Magnetic** | — |

These are the agents that detach or supply electrons, i.e. that make ions and free carriers. The
list is short and closed — it is exactly the kind of item a definitions question lifts whole.

---

## 1.11 Conduction in a gas, and in a vacuum ·J p6–p7

[fig] **·J p6 — the gas discharge tube.** A long horizontal capsule, drawn as a rectangle with
**rounded ends** (a lozenge), representing the sealed low-pressure tube.

- **Both electrodes are drawn as short vertical bars inside the capsule**, one near each end.
- The **left-hand bar** is labelled **Cathode** by a leader running up from below-left outside the
  tube.
- Immediately to the right of the cathode sits a **loose cluster of about eight short horizontal
  dashes**, scattered over four rough rows, labelled **Space Charge** by a leader from below that
  splits into **two arrowheads**. The dashes are the accumulated electrons.
- The **right-hand bar** is labelled **Anode** by a horizontal leader running in from the right,
  outside the tube.
- Immediately to the left of the anode sits a **cluster of about nine small open circles**, labelled
  **Gas Molecules** by a leader from below that also splits into **two arrowheads**.
- **The middle of the tube is empty.** The space charge sits at the cathode end and the gas
  molecules at the anode end, with a clear span between them — the drift region the electrons are
  accelerated across.

**The mechanism** ·J p6:

- **Conduction in gases takes place through ionisation.**
- **Accelerating electrons strike the molecules and ionise them.**
- **The gas must be at low pressure.** It **cannot conduct at normal pressure**.

[added] Read the figure with the mechanism: electrons leave the cathode, pile up as a **space
charge** near it, are accelerated down the tube by the cathode-anode field, and collide with the gas
molecules at the far end hard enough to knock electrons off them. The low-pressure requirement is
what gives each electron a long enough free run between collisions to pick up the energy needed to
ionise. The notes state the requirement but not the reason.

**Conduction in a vacuum** ·J p7 — the whole treatment is one sentence, and its heading is missing
(gap 4 in §1.0):

- **A vacuum can only conduct electromagnetic waves, e.g. light.** ·J p7

**Conduction in liquids is never covered**, despite being named in the ·J p2 definition. Recorded as
a gap; nothing is supplied here.

---

## 1.12 Materials used in electrical and electronic circuits ·J p7–p8

[table] **Symbols for this section**

| Symbol | Meaning | Units | Typical value |
|---|---|---|---|
| $E_g$ | energy gap — width of the forbidden band | eV | 0, 1.1, 5 |
| eV | electron-volt, the unit energy gaps are quoted in | — | $1\ \mathrm{eV} = 1.602\times10^{-19}\ \mathrm{J}$ |

*(The notes print the gap as "Eg" and the unit as "ev". The correct unit symbol is **eV** — capital
V, for Volta. Rolled into the typo table at the end of this file.)*

The notes head this section **"Material used in electrical & electronic circuits"** and open with
**Solids**, then **Types of solids** — three of them, printed across the page ·J p7:

1. **Conductors**
2. **Insulators**
3. **Semiconductors**

### Conductors ·J p7

[def] **Conductors** are materials that **allow current to pass through**. ·J p7

Properties, in the notes' order ·J p7:

1. **1 to 3 electrons in the outermost shell**
2. **Metallic bond**
3. **Free electrons present**
4. **Low resistance**
5. **The conduction band and the valence band overlap**, and the gap is very small
6. **Resistance increases with an increase in temperature**
7. $E_g = 0\ \mathrm{eV}$

**Examples: all metals.** ·J p7

[fig] **·J p7 — conductor energy-band diagram.** A single rectangle, taller than it is wide, divided
into **three horizontal strips** by two full-width lines, with a labelled arrow into each strip from
the right:

| Strip | Depth | Shading | Label |
|---|---|---|---|
| Top | thick | **hatched** with diagonal lines | **Conduction Band** |
| Middle | **thin** — a narrow band | **clear** (unhatched) | **Forbidden Band** |
| Bottom | thick | **hatched** with diagonal lines | **Valence Band** |

Hatching means the band is occupied; the clear strip is the forbidden band.

> ⚠ VERIFY **JV1.6** ·J p7 — the figure and the text on the same page contradict each other. The
> text says the conduction and valence bands **overlap** and states $E_g = 0\ \mathrm{eV}$; the
> figure draws a **distinct, clear forbidden band between them**. A gap that is drawn is not a gap of
> zero width. Redraw it as:
> $$\boxed{\;\text{conductor: conduction and valence bands touch or overlap},\quad E_g = 0\ \mathrm{eV},\quad \text{no forbidden band}\;}$$
> Why it matters: the three band diagrams in this section are distinguished from each other **only**
> by the width of the middle strip, so a conductor drawn with a visible gap is indistinguishable
> from a narrow-gap semiconductor. Note that the same defect appears in the reference deck — see
> §1.16.
> See `_verification-log.md`.

> ⚠ VERIFY **JC1.10** ·J p7 — property 5 prints *"The conduction band and valence band overlap and
> are very small."* What is very small is **the gap between them**, not the bands. Read: *"the
> conduction and valence bands overlap; the forbidden gap is very small — effectively zero."*
> See `_verification-log.md`.

### Insulators ·J p7

[def] **Insulators** are materials that **do not allow current to pass through**. ·J p7

Properties, in the notes' order ·J p7:

1. **5 to 8 electrons in the outermost shell**
2. A structure with **covalent bonding**, which **results in no free electrons** to carry a current
3. A **very large energy gap** between the conduction band and the valence band
4. $E_g = 5\ \mathrm{eV}$

[fig] **·J p7 — insulator energy-band diagram.** The same three-strip rectangle as the conductor
figure, with the proportions changed:

| Strip | Depth | Shading | Label |
|---|---|---|---|
| Top | thin | **hatched** | **Conduction Band** |
| Middle | **deep** — occupies most of the rectangle | **clear** | **Forbidden Band** |
| Bottom | thin | **hatched** | **Valence Band** |

The picture is the definition: a wide clear strip means electrons in the valence band cannot reach
the conduction band, so there is no conduction.

**The notes give no examples of insulators.** RD2 does — see §1.16.

### Semiconductors ·J p7–p8

[def] **Semiconductors** are materials that have **poor conductivity at low temperatures and good
conductivity at high temperatures**. ·J p7

**Characteristics of semiconductors**, in the notes' order ·J p7–p8:

1. **4 electrons in the outermost shell / band**
2. Their atomic structure has **covalent bonds**
3. They have a **moderate number of free electrons**
4. $E_g = 1.1\ \mathrm{eV}$
5. They have a **moderately sized forbidden band**
6. There are **two types: intrinsic and extrinsic**

[fig] **·J p8 (top) — semiconductor energy-band diagram, incomplete.** What survives at the head of
·J p8 is a rectangle bounded left and right by short vertical lines, divided into two visible parts:

| Strip | Depth | Shading | Label |
|---|---|---|---|
| Upper | moderate | **clear** | **Forbidden Band** |
| Lower | thick | **hatched** | **Valence Band** |

> ⚠ VERIFY **JC1.11** ·J p8 — **the conduction band of the semiconductor band diagram is not in the
> document.** The figure is split by the ·J p7 / ·J p8 page break and only the forbidden band and the
> valence band survive; there is no hatched strip and no "Conduction Band" label above the clear
> strip, though the two vertical side lines continue upwards past it. Redraw it with the conduction
> band restored, hatched, above a **moderate** forbidden band — narrower than the insulator's,
> wider than nothing:
> $$\boxed{\;\text{semiconductor: hatched conduction band}\;/\;\text{moderate clear forbidden band } (E_g = 1.1\ \mathrm{eV})\;/\;\text{hatched valence band}\;}$$
> See `_verification-log.md`.

> ⚠ VERIFY **JC1.14** ·J p8 — characteristic 5 prints *"They have a moderately sized **of** forbidden
> band"*. Stray "of". Reads *"a moderately sized forbidden band"*.
> See `_verification-log.md`.

### [table] The three-way classification — learn this

Assembled from ·J p7–p8. This table is the single highest-value item in the whole file.

| | **Conductor** | **Semiconductor** | **Insulator** |
|---|---|---|---|
| Definition | allows current to pass | poor conduction cold, good conduction hot | does not allow current to pass |
| Outermost-shell electrons | **1 to 3** | **4** | **5 to 8** |
| Bonding | metallic | covalent | covalent |
| Free electrons | present, many | moderate number | none |
| Band gap $E_g$ | $0\ \mathrm{eV}$ | $1.1\ \mathrm{eV}$ | $5\ \mathrm{eV}$ |
| Forbidden band | none — bands overlap | moderate | very large |
| Resistance | low | — (not stated) | — (not stated) |
| Resistance vs temperature | **increases** with $T$ | — (not stated; implied to fall) | — (not stated) |
| Examples | all metals | — (Si and Ge named in §1.13) | — (none given) |

The valence-electron count is the spine of the table: **1–3 / 4 / 5–8**. Everything else follows from
it. Four valence electrons is the special case — too many to give away freely, too few to complete an
octet — and that is why the whole of electronics is built on the column in the middle.

[added] The notes state that a **conductor's resistance rises with temperature** but never state the
opposite behaviour for a semiconductor. It follows directly from their own definition — poor
conduction at low temperature, good conduction at high temperature means **resistance falls as
temperature rises**. Heat frees carriers across a 1.1 eV gap; there is no such gap to bridge in a
metal, where heating only increases lattice scattering. The two temperature coefficients therefore
have **opposite signs**, and that is the fact exam questions turn on.

---

## 1.13 Intrinsic semiconductors ·J p8

[def] **Intrinsic semiconductors** are semiconductors **in their pure form** — e.g. **silicon,
germanium**. **Conduction takes place through holes and electrons.** ·J p8

The page prints the structure it will use throughout:

$$\text{Silicon structure} = 2\!:\!8\!:\!4$$

Four valence electrons, as the classification in §1.12 requires. ($2 + 8 + 4 = 14 = Z_{\mathrm{Si}}$
— checked.)

[fig] **·J p8 — the silicon covalent lattice.** A five-atom cross, the standard two-dimensional
picture of the diamond lattice.

- **One central circle labelled Si**, with **four further circles labelled Si** placed directly
  **above, below, left and right** of it. Nothing on the diagonals.
- Between the centre atom and each neighbour is a **long narrow ellipse** — a **covalent bond**. Four
  ellipses: two vertical (up and down), two horizontal (left and right).
- Each bond ellipse carries **two × marks**, one near each end — **one electron contributed by each
  of the two atoms it joins**. That is the shared pair.
- Each **outer** Si circle carries **three further × marks** on its outward-facing side (top, bottom
  and outer edge), representing its remaining valence electrons, which would bond to atoms further
  out that are not drawn.
- The central Si shows **no × of its own outside the bonds** — all four of its valence electrons are
  committed to the four bonds.

Count the centre atom's electrons: **four bonds × two electrons shared = eight electrons around the
central atom**. That is the completed octet of §1.10, and it is why pure silicon at low temperature
conducts badly — every valence electron is locked in a bond.

[added] The notes say conduction is by "holes and electrons" but do not say how the carriers appear
in a pure crystal. They appear thermally: heat breaks a covalent bond, freeing an electron into the
conduction band and leaving a vacancy — a **hole** — behind. In an intrinsic material the two are
**created in pairs and are therefore equal in number**. This is the fact that makes §1.14's doping
asymmetry visible.

---

## 1.14 Extrinsic semiconductors ·J p8–p9

[def] **Extrinsic semiconductors** are semiconductors **to which impurities have been added through
the process of doping**. ·J p8

**Two types** ·J p8:

1. **P-type**
2. **N-type**

### P-type ·J p8–p9

[def] **P-type** is formed by **adding trivalent impurities into the crystal structure of silicon**.
·J p8

**Trivalent impurities include boron.** ·J p8

The two structures the page sets side by side ·J p8:

$$\mathrm{Boron} = 2\!:\!3 \qquad \mathrm{Silicon} = 2\!:\!8\!:\!4$$

Boron brings **three** valence electrons to a site that needs **four**. One bond cannot be completed.

[fig] **·J p9 — the P-type lattice.** The same five-atom cross as §1.13, with one substitution.

- The **central circle is labelled B** (boron). The four surrounding circles are still **Si**, placed
  above, below, left and right.
- Four **bond ellipses** join the boron to its four silicon neighbours, exactly as before.
- **Three of the four bonds carry two × marks** — a completed shared pair each: the **upper**,
  **lower** and **right-hand** bonds.
- The **left-hand bond carries only one ×**, at the silicon end. The boron end of that ellipse is
  **empty**.
- A leader labelled **"Hole"** comes down from the upper left and its arrowhead lands **exactly on
  that empty position** in the left-hand bond.
- Each outer Si circle carries three further × marks on its outward side, as in §1.13.

That single missing × is the whole of P-type doping. Three electrons where four are needed leaves one
vacancy per boron atom.

**What the notes conclude** ·J p9:

- **Holes are the majority carriers in P-type semiconductors**, so P-type is an **acceptor
  semiconductor**.
- **Conduction is by movement of holes.**
- **Holes move in the direction of conventional current.**

### N-type ·J p9

[def] **N-type** is formed by **adding pentavalent impurities** — e.g. **phosphorus, arsenic,
antimony**. ·J p9

The two structures ·J p9:

$$\mathrm{Silicon} = 2\!:\!8\!:\!4 \qquad \mathrm{Phosphorus} = 2\!:\!8\!:\!5$$

Phosphorus brings **five** valence electrons to a site that needs **four**. One is left over.

[fig] **·J p9 — the N-type lattice.** Again the five-atom cross, with a second difference.

- The **central circle is labelled P** (phosphorus); the four neighbours are **Si**, above, below,
  left and right.
- **All four bond ellipses carry two × marks** — every bond is complete.
- A **dashed circle** is drawn around the central P atom, larger than the atom itself and cutting
  across the inner ends of all four bond ellipses. It marks the orbit of the surplus electron.
- A **fifth ×** sits **on that dashed circle**, in the upper right, outside all four bonds.
- A leader labelled **"Free electron"** comes in from the upper right, and its arrowhead lands on
  that fifth ×.
- Each outer Si circle carries three further × marks on its outward side.

**What the notes conclude** ·J p9:

- **Majority charge carriers are electrons**, so conduction is **by electron flow**.
- **Electron flow is opposite to the direction of conventional current.**

*(The notes do not use the word "donor" for N-type, although they do use "acceptor" for P-type. RD2
supplies it — see §1.16.)*

### [table] P-type against N-type — the comparison to memorise

Built from ·J p8–p9. `[added]` rows are marked; everything else is the notes'.

| | **P-type** | **N-type** |
|---|---|---|
| Dopant valence | **trivalent** (3 valence electrons) | **pentavalent** (5 valence electrons) |
| Dopant named | boron, $2\!:\!3$ | phosphorus $2\!:\!8\!:\!5$, arsenic, antimony |
| What the lattice ends up with | one **incomplete bond** per dopant atom | one **surplus electron** per dopant atom |
| Majority carrier | **holes** | **electrons** |
| Minority carrier `[added]` | electrons | holes |
| Called | **acceptor** | *(donor — not named in these notes; `[added]` from RD2)* |
| Conduction by | movement of holes | electron flow |
| Carrier direction | **with** conventional current | **opposite to** conventional current |

The last row is the one that gets marked. Holes are positive, so they drift the way conventional
current is defined to flow; electrons are negative and drift against it. Both produce current in the
same direction — only the carrier's sign differs.

[added] Neither the P nor the N lattice figure is drawn with more than one dopant atom, which can
give the impression that a doped crystal is mostly impurity. It is not — doping levels are of the
order of one impurity atom in $10^{6}$ to $10^{8}$ silicon atoms. The figure shows one dopant site
in isolation, magnified.

---

## 1.15 Terms and concepts — charge ·J p9

The notes close this block with a short "Terms and concepts" entry.

[def] **Charge** — the notes give two lines ·J p9:

- "Amount of current passing through a given point for a given time."
- "It is the ability to attract or repel electrons."

and then the relation

[eq: charge-current-time] ·J p9

$$\boxed{\;Q = I\,t\;}$$

- $Q$ — electric charge, **coulombs (C)**
- $I$ — current, **amperes (A)**
- $t$ — time, **seconds (s)**

> ⚠ VERIFY **JV1.7** ·J p9 — charge is defined as *"Amount of current passing through a given point
> for a given time"*. **Charge is not an amount of current** — the two are different quantities with
> different units (C against A), and the sentence as printed would put charge in amperes. The second
> line, *"the ability to attract or repel electrons"*, describes an **effect** of charge rather than
> defining it. The correct statements — one of which the notes themselves give on ·J p4 — are:
> $$\boxed{\;\text{charge is the quantity of electricity in a body; } Q = It \text{ is the charge transported by a steady current } I \text{ in time } t\;}$$
> Check by units: $[Q] = \mathrm{A}\cdot\mathrm{s} = \mathrm{C}$. ✓ The equation is right; only the
> words above it are wrong. Note ·J p4's own definition — "the quantity of electricity in a body" —
> is the sound one, so the document contradicts itself five pages apart.
> See `_verification-log.md`.

[added] **A numerical check on $Q = It$**, since the notes give none. A steady current of
$I = 2\ \mathrm{A}$ flowing for $t = 5\ \mathrm{s}$ transports

$$Q = I\,t$$
$$Q = 2 \times 5$$
$$Q = 10\ \mathrm{C}$$

and, rearranged, the two forms that get used later in the course:

$$I = \frac{Q}{t} \qquad\text{and}\qquad t = \frac{Q}{I}$$

$I = Q/t$ is the definition of current — **charge per unit time** — and is the form that reappears
whenever a capacitor charging current or a diode carrier flow has to be written down.

---

## 1.16 Cross-check against the reference tier — RD2

Reference deck **RD2, *Materials Used in Electrical & Electronic Circuits*** (18 pp., mapped in
`_reference-decks.md` §2) covers **·J p7–p9 almost slide for slide**. RD2 is tier 3 — mapped, not
verified — so where the two differ, **these notes win**; but RD2 is materially fuller in three
places and those additions are worth knowing.

### Where the two agree — completely

Every one of these appears in both, with the same numbers:

| Item | ·J | RD2 |
|---|---|---|
| Conductor: 1–3 outer electrons, metallic bond, free electrons, low resistance, bands overlap, $E_g = 0$ eV, resistance rises with $T$, examples "all metals" | p7 | p2 |
| Insulator: 5–8 outer electrons, covalent bonding, no free electrons, very large gap, $E_g = 5$ eV | p7 | p5 |
| Semiconductor: poor cold / good hot, 4 outer electrons, covalent bonds, moderate free electrons, $E_g = 1.1$ eV, moderate forbidden band, two types | p7–p8 | p8 |
| Intrinsic: pure form, silicon and germanium, conduction by holes and electrons | p8 | p9 |
| The silicon covalent-lattice figure — central Si, four Si neighbours, crosses for electrons | p8 | p9 |
| Extrinsic: impurities added by doping; two types P and N | p8 | p11 |
| P-type: trivalent, boron $2\!:\!3$, silicon $2\!:\!8\!:\!4$, hole, majority carrier holes, acceptor, holes move with conventional current | p8–p9 | p12 |
| P-type lattice figure with the missing bond arrowed "Hole" | p9 | p12 |
| N-type: pentavalent, phosphorus $2\!:\!8\!:\!5$, arsenic, antimony, majority carrier electrons, electrons move against conventional current | p9 | p13 |
| N-type lattice figure with the labelled "Free electron" | p9 | p13 |

The overlap is close enough that RD2 can be used directly as revision slides for §1.12–§1.14. The
wording of several definitions is near-identical.

### Where RD2 adds what these notes lack

Seven additions, in descending order of exam value:

1. **The resistance law and its temperature correction** — $R = \rho L/A$ and
   $R = R_0(1 + \alpha\,\Delta T)$, with resistivity defined, plus **four fully worked resistance
   calculations** (copper, aluminium, silver at two temperatures). ·RD2 p14, p16. **·J p2–p9 contains
   no resistance calculation at all** — the only arithmetic in this whole range is §1.8's shell
   count. If a CAT asks for a numerical resistance, RD2 is where the pattern lives.
2. **The semiconductor resistance formula** in terms of doping and mobility,
   $R = \left[\,q\mu_n N_D (1+\alpha\Delta T)\right]^{-1}(L/WT)$. ·RD2 p15. Nothing comparable here.
3. **Minority carriers named explicitly** — electrons in P-type, holes in N-type. ·RD2 p12–p13.
   These notes name only the *majority* carrier for each type.
4. **"Donor" for N-type.** ·RD2 p13. ·J p9 gives **acceptor** for P-type but leaves the N-type
   counterpart unnamed — an asymmetry that reads as an omission rather than a choice.
5. **More dopants by name** — aluminium, gallium and indium as trivalent alternatives to boron.
   ·RD2 p12. ·J p8 names boron only. (For pentavalent the two agree: phosphorus, arsenic, antimony.)
6. **Examples of insulators** — air, plastic, glass, wood, ceramic. ·RD2 p5. **·J p7 gives none**,
   which is a real gap in a section that gives examples for the other two classes.
7. **A quantitative p-n junction picture** — depletion widths $D_N$, $D_P$, field $E$, donor and
   acceptor concentrations $N_D$, $N_A$. ·RD2 p13. These notes stop at the doped lattice and do not
   join the two materials in this range.

RD2 also states outright that **a semiconductor's resistance decreases with temperature** ·RD2 p8,
where ·J p7 only implies it. §1.12 supplies that inference as `[added]`; RD2 confirms it.

### Where these notes add what RD2 lacks

Everything on ·J p2–p6 has **no RD2 counterpart at all**: the definition of electronics, analogue and
digital signals, the applications list, the states of matter, the twenty-element table, the whole of
the electron theory and the Bohr model, the exclusion principle, the $2n^2$ and $2 + 4(m-1)$
capacity rules and the worked shell calculation, atomic number and weight, valence electrons and
ions, and conduction in a gas with its discharge-tube figure. RD2 begins at the materials
classification; this file begins four pages earlier.

Within the shared material, ·J p7 also has **one property RD2 does not** — it makes the
sub-shell/forbidden-gap structure of the *atom* (§1.6) continuous with the forbidden *band* of the
solid, which is the conceptual bridge between the two halves of this file.

### Where they genuinely disagree

**One place, and these notes are the safer of the two.**

- **·RD2 p5 states that "temperature does not affect resistance" for insulators.** That is wrong —
  insulator resistance also falls as temperature rises, and `_reference-decks.md` already carries a
  caution against it. **·J p7 makes no temperature claim about insulators at all.** Follow ·J p7:
  say nothing, or say that insulator resistance falls with temperature. Do not repeat RD2's claim.

**And one shared defect, present identically in both.**

- The **conductor band diagram is drawn with a visible forbidden band** in ·J p7 *and* in ·RD2 p2,
  while both state $E_g = 0$ eV. Flagged here as **JV1.6**. It is the same figure, inherited by
  both documents from a common ancestor, so finding it in RD2 is **not** independent confirmation —
  it is the same error twice.

---

## 1.17 Verification flags in this range — summary

**Seven substantive, fifteen cosmetic.** Every one is stated in full at its point of use above; this
is the index.

[table] **Substantive — would mislead a learner or produce a wrong answer**

| ID | Page | What the page prints | What it should be |
|---|---|---|---|
| **JV1.1** | ·J p4 | "In a simple hydrogen atom the nucleus is made of protons and neutrons of approximately equal numbers" | Hydrogen's nucleus is a single proton with no neutron; the equal-numbers statement belongs to heavier nuclei |
| **JV1.2** | ·J p5 | "a single **proton** is emitted" on an electron transition | a single **photon**, of energy $E_i - E_f$ |
| **JV1.3** | ·J p5 | "The figure above shows the structure of a **carbon atom**" | a generic shell/sub-shell schematic; carbon is $Z = 6$, structure $2\!:\!4$, two shells, six electrons |
| **JV1.4** | ·J p6 | "Max No $= 2^{n}$" | $N = 2n^{2}$ — the page's own next line computes $2\times3^2$ |
| **JV1.5** | ·J p6 | "S = 16   2.3.6" | $\mathrm{S}: 2\,.\,8\,.\,6$ — the printed digits sum to 11, not 16 |
| **JV1.6** | ·J p7 | conductor band figure drawn with a clear forbidden band | no forbidden band; conduction and valence bands overlap, $E_g = 0$ eV |
| **JV1.7** | ·J p9 | "Charge — amount of current passing through a given point for a given time" | charge is the quantity of electricity in a body; $Q = It$ is the charge a steady current transports |

[table] **Cosmetic — typo, notation slip, figure defect; the physics is unaffected**

| ID | Page | What the page prints | What it should be |
|---|---|---|---|
| **JC1.1** | ·J p5 | "Neil Bohrls", "Bohrl" | Niels Bohr |
| **JC1.2** | ·J p5 | "Paul's exclusion principle" | Pauli exclusion principle |
| **JC1.3** | ·J p6 | "VALENCE ELECTORNS (State electron)" | VALENCE ELECTRONS; the parenthetical does not resolve and is not guessed at |
| **JC1.4** | ·J p6 | "N = 3" for the shell number | $n = 3$; ·J p5 uses $N$ for the electron count |
| **JC1.5** | ·J p4 | "equal number of +vely charged **atoms**" | +vely charged **protons** |
| **JC1.6** | ·J p3, p9 | "Phosphorous" | phosphorus |
| **JC1.7** | ·J p6 | "for all the atoms with two **shall**"; "if the atom" printed twice | "with two **shells**"; single occurrence |
| **JC1.8** | ·J p6 | "leaving the atom with an **access the charge**" | "an **excess positive** charge" |
| **JC1.9** | ·J p6 | "comparing the weight of it's atoms of carbon = 12" | "…with that of an atom of carbon, taken as 12" — the comparison object is missing |
| **JC1.10** | ·J p7 | "The conduction band and valence band overlap and **are very small**" | the **gap between them** is very small |
| **JC1.11** | ·J p8 | semiconductor band figure: conduction band absent, lost at the page break | hatched conduction band above a moderate forbidden band |
| **JC1.12** | ·J p4 | atom-figure leaders: "Shell" lands on a dashed ring, one "Sub Shells" leader between solid rings | solid rings are shells, dashed rings sub-shells (from the ·J p5 text) |
| **JC1.13** | ·J p2 | "comes from the 2 words: Electrons …, Mechanics – Study of motion of an electron" | *electronics* = electron + -ics; mechanics is the study of motion generally |
| **JC1.14** | ·J p3, p8 | "Entertainment - **3** stereos"; "a moderately sized **of** forbidden band" | stray tokens; delete |
| **JC1.15** | various | see the typo table below | — |

> ⚠ VERIFY **JC1.15** ·J p2–p9 — residual typographic slips, none affecting the physics:
>
> | Page | Printed | Should read |
> |---|---|---|
> | ·J p3 | "When **is** exists in liquid or gas its dimension are determined by the container" | "When it exists…; its dimensions are…" |
> | ·J p3 | "the individual elements **poses** the same properties" | possess |
> | ·J p4 | "consists **on** one electron orbiting around the nucleus" | consists **of** |
> | ·J p5 | "well defined shells **of** levels" | shells **or** levels |
> | ·J p5 | "the general **formulae** $N = 2n^2$" | formula (singular) |
> | ·J p5 | "**plank's** constant" | Planck's constant |
> | ·J p5 | "In a complex atom there's no room for all the electrons in **state** near the nucleus" | in **states** near |
> | ·J p6 | "determines **it'd** stability" | its stability |
> | ·J p6 | "an **addition** orbit/electron" | an **additional** orbital electron |
> | ·J p6 | "ionize **it.The** gas should have low pressure" | missing space |
> | ·J p7 | "Eg = 0**ev**", "5**ev**", "1.1**ev**" | eV — capital V, for Volta |
> | ·J p7 | "**Material** used in electrical & electronic circuits" (heading) | Materials |
> | ·J p8 | "**semi conductors**", "e. g silicon" | semiconductors; e.g. |
>
> See `_verification-log.md`.

---

## 1.18 What to take from this file

**Six things carry forward into the rest of BEE 3103:**

1. **The three-way classification table** in §1.12 — 1–3 / 4 / 5–8 valence electrons, and
   $E_g$ = 0 / 1.1 / 5 eV. Everything about diodes and transistors starts here.
2. **The three band diagrams** — they differ only in the width of the middle strip. Redraw the
   conductor one **without** a gap (JV1.6).
3. **Silicon $2\!:\!8\!:\!4$, boron $2\!:\!3$, phosphorus $2\!:\!8\!:\!5$** — three numbers that
   explain all of doping.
4. **The P-type and N-type lattices** — one missing × against one surplus ×. Join a P block to an N
   block and the next topic file has its P-N junction.
5. **Majority carrier and direction** — holes with conventional current, electrons against it.
6. **$Q = It$**, and its rearrangement $I = Q/t$.

**Triage.** The Bohr postulates and $hf = E_i - E_f$ (§1.6) are stated but never used again anywhere
in ·J p2–p9, and no calculation in this range depends on them; learn the statement, not the
application, unless a past paper says otherwise. The exclusion principle and the $2n^2$ rule **are**
assessed — §1.8 is a worked example and worked examples get lifted verbatim. The applications list
(§1.3) and the energy list (§1.10) are pure recall items and cost nothing to memorise.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
