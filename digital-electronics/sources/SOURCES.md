# Digital Electronics — source manifest

Raw source material for this subject. **Nothing in this folder is committed** — `.gitignore`
excludes `**/sources/*` and `*.pdf` globally. This manifest is committed; the files it describes
are not.

Unit code **BEE 3102**. The chapter decks title the unit **Digital Electronics II** in their own
footers.

---

## Files

| File | Type | Pages | Description |
|---|---|---|---|
| `BEE 3102 Chapter 1 - Introduction.pdf` | PowerPoint export, 4:3 | 32 | Evolution of electronic devices, a recap of Digital Electronics I, and a roadmap of the unit |
| `BEE 3102 Chapter 2 - Digital Logic Families.pdf` | PowerPoint export, 16:9 | 43 | Logic-family characteristics, then DL → RTL → DTL → TTL → CMOS |
| `BEE 3102 Chapter 3 - Memory and Programmable Logic Devices.pdf` | PowerPoint export, 16:9 | 66 | Semiconductor memory, Hamming codes, ROM, and PROM/PLA/PAL/CPLD/FPGA |
| `BEE 3102 Chapter 4 - Signal Conversion (ADC  DAC).pdf` | PowerPoint export, 16:9 | 49 | ADC methods and DAC methods, example-dense throughout |
| `BEE 3102 Chapter 5 - Finite State Machines  Sequential Circuit Design.pdf` | PowerPoint export, 16:9 | 118 | FSM structure and analysis, sequence detectors, state reduction, state assignment |
| `BEE 3102 Chapter 6 - Algorithmic State Machines.pdf` | PowerPoint export, 4:3 | 40 | ASM charts, SM blocks, PLA realisation, and two datapath-control worked examples |
| `Excitation Table.pdf` | single sheet, A4 | 1 | Characteristic and excitation tables for the SR, D, JK and T flip-flops |
| `lab-01-ttl-nand-nor-gates.pdf` | scanned PDF, image-only | 14 | *Experiment 4 — TTL NAND/NOR Gates: Definitions and Operation.* Printed pages 31–44 of a commercial digital-electronics laboratory manual. Blank worksheet copy |

Total: **348 slides**, one A4 reference sheet, and a 14-page lab manual.

---

## Handout codes

The knowledge base cites these decks by code. Define new codes here before using them.

| Code | File |
|---|---|
| `CH1` | Chapter 1 — Introduction |
| `CH2` | Chapter 2 — Digital Logic Families |
| `CH3` | Chapter 3 — Memory and Programmable Logic Devices |
| `CH4` | Chapter 4 — Signal Conversion (ADC/DAC) |
| `CH5` | Chapter 5 — Finite State Machines & Sequential Circuit Design |
| `CH6` | Chapter 6 — Algorithmic State Machines |
| `EXC` | Excitation Table |

**In every deck the printed footer number equals the PDF page number.** So `·CH4 slide 16` is
page 16 of the Chapter 4 PDF. This was checked deck by deck; it is what makes the citations in the
topic files directly resolvable.

---

## Notes on the chapter decks

- **The text layer is present but is not the source.** Every deck exports text, and that text is
  unreliable: it reorders columns, drops overbars, and flattens equations. The knowledge base was
  built from **200 dpi page renders**, per `docs/kb-format.md` § "Verification". Do not rebuild
  from `pdftotext` output.
- **Eleven slides carry no text beyond the footer** and exist as images: CH1 4; CH3 20–21;
  CH4 45–46; CH6 13, 17, 37–40. CH6 37–40 are the whole weighing-machine worked example. Anything
  working from extracted text will silently miss them.
- **Embedded images are numerous** — 399 across the six decks — and a large fraction are scanned or
  redrawn textbook figures. They are third-party material. See "Provenance" below.
- **The footers carry authoring credit and a social handle.** Neither appears anywhere in the
  knowledge base, per rule 1 and rule 2 of `docs/kb-format.md` § "What never gets committed".
- **Chapter 4 sets homework with printed due dates in August 2025**, so these decks are the previous
  run of the unit. The questions are transcribed in the knowledge base and left unsolved; the dates
  are recorded as historical.

## Notes on `lab-01-ttl-nand-nor-gates.pdf`

- **No text layer.** All 14 pages return zero characters from text extraction; the whole document
  is a page scan. Everything in the knowledge base was read from rendered page images at 200 dpi.
- **Scan quality.** Pages 35 and 40 (PDF pages 5 and 10) are noticeably degraded. Both were
  resolved by re-cropping and upscaling rather than by inference — see the reading log in
  `../knowledge-base/labs/lab-01-ttl-nand-nor.md`.

---

## Provenance

The chapter decks are the lecturer's own teaching material. The laboratory manual is a published
commercial work. Neither is ours, and neither is committed.

Three consequences, all of which the knowledge base already observes:

1. **Figures are redrawn, never screenshotted.** The 142 SVGs in `../knowledge-base/figures/` are
   hand-authored. Where a slide's figure is plainly lifted from a textbook or a published paper —
   CH1 slides 2, 4, 6, 8, 9, 17, 26, 30; CH3 slides 6, 11, 20, 21, 31; CH6 slides 30, 35, among
   others — it is described in a `[fig]` caption and **not** reproduced.
2. **No names, no contact details**, in this manifest or anywhere else.
3. **The lab file is the outstanding exception.** It quotes the manual's procedure text and
   discussion questions verbatim and keeps page crops in `../knowledge-base/labs/figures/scan/`.
   That was acceptable while this subject was excluded from git. It is **not** acceptable now that
   the subject is tracked. See the open questions in `../knowledge-base/00-index.md`.

---

## Page maps

### CH1 — Introduction (32)

| Slides | Contents |
|---|---|
| 1–4 | Title; evolution of electronic devices; scales of integration |
| 5–20 | Recap of Digital Electronics I — digital systems, D flip-flops, registers, shift registers (worked example, 15–16), counters, ripple vs synchronous |
| 21–32 | Roadmap of the unit — memory and PLDs, logic families, sequential analysis, state machines, ADC/DAC, Verilog |

### CH2 — Digital Logic Families (43)

| Slides | Contents |
|---|---|
| 1–2 | Title, outline |
| 3–19 | Characteristics — integration scales, logic levels, propagation delay, fan-in/fan-out, noise margins (example, 13), dynamic response, power (example, 17), sourcing and sinking, unused inputs |
| 20–34 | Classification; diode logic; RTL; DTL (example, 27); TTL — inverter, gate, 3-input NAND, open collector, tri-state (examples, 34) |
| 35–42 | CMOS — enhancement MOSFETs, inverter, NAND, NOR, family evolution, CMOS vs TTL |
| 43 | Homework |

### CH3 — Memory and Programmable Logic Devices (66)

| Slides | Contents |
|---|---|
| 1–2 | Title, outline |
| 3–25 | Memory — array, write/read, RAM vs ROM, organisation, SRAM, DRAM (20–21 image-only), decoding, 4 × 4 RAM, address multiplexing |
| 26–30 | Error detection and correction; Hamming code; SEC-DED |
| 31–33 | ROM — construction and types |
| 34–52 | PLDs — structure, ROM/PAL/PLA comparison, notation, PROM (examples, 42–43), PLA (examples, 45–49), PAL (50–52) |
| 53–63 | Sequential programmable devices, FPLS, SPLD, macrocell, CPLD, gate array, FPGA |
| 64–66 | Homework |

### CH4 — Signal Conversion (49)

| Slides | Contents |
|---|---|
| 1–2 | Title, outline |
| 3–13 | Signal types, the conversion process, sampling, anti-aliasing, sample-and-hold, quantisation and encoding |
| 14–29 | ADC methods — flash (examples, 16–17), SAR (19–22), dual slope (25), sigma-delta (26–27), comparison and summary |
| 30–48 | DAC — transfer relation (examples, 32–33), resolution (examples, 35–37), full-scale error, binary-weighted DAC (examples, 40–43), R/2R ladder (44–47, with 45–46 image-only), resolution and accuracy |
| 18, 23, 24, 49 | Homework |

### CH5 — Finite State Machines & Sequential Circuit Design (118)

| Slides | Contents |
|---|---|
| 1–2 | Title, topics |
| 3–17 | FSM structure, Mealy and Moore, the four steps, binary counter, serial adder worked through |
| 18–38 | Analysis — state equations, tables and diagrams; D, JK and T flip-flops; characteristic equations; equivalent states; mixed outputs |
| 39–71 | Design — procedure, formulation, sequence detectors, and six fully worked Mealy/Moore machines |
| 72–90 | State reduction — minimisation, equivalence, implication tables worked pass by pass |
| 91–112 | State assignment — guidelines, next-state maps, and worked Cases I–IV |
| 113–118 | State-graph construction guidelines, serial data transmission, alphanumeric notation, completeness tests |

### CH6 — Algorithmic State Machines (40)

| Slides | Contents |
|---|---|
| 1–11 | Introduction; the three chart elements; the SM block; equivalent blocks and charts; rules; conversion from a state graph |
| 12–17 | Worked example — binary multiplier (13 image-only); SM chart for an electronic dice game (17 image-only) |
| 18–22 | Realisation of SM charts; PLA realisation and PLA table for the dice game; derived maps |
| 23–40 | Appendix — Example 1 counter/datapath control (24–35); ASM for a weighing machine (36–40, of which 37–40 are image-only) |

### EXC — Excitation Table (1)

Characteristic and excitation tables for the SR, D, JK and T flip-flops on one A4 sheet. Folded into
`../knowledge-base/07-fsm-fundamentals-and-analysis.md` § 7.15.

### lab-01 — TTL NAND/NOR Gates (14)

| PDF page | Printed page | Contents |
|---|---|---|
| 1 | 31 | Title, Object, start of Introductory Theory |
| 2 | 32 | Fig. 4-1(a) 7400 and 4-1(b) 7403 schematics; unit load, fan-out, threshold analysis |
| 3 | 33 | Fig. 4-2 capacitive load; Fig. 4-3 gate driving gate; noise-immunity theory |
| 4 | 34 | Fig. 4-4 transfer characteristic; equations (4-1), (4-2); Equipment Required; part-number table |
| 5 | 35 | Fig. 4-5 logic diagram/pinout; Fig. 4-6 inverter; Table 4-1E |
| 6 | 36 | Fig. 4-7 2-input gate; Tables 4-2E, 4-3E; start of Part 3 |
| 7 | 37 | Fig. 4-8 UL determination; Fig. 4-9 output voltage; start of Part 4 |
| 8 | 38 | Fig. 4-10 transfer rig; Table 4-4E; Fig. 4-11 plot grid |
| 9 | 39 | Fig. 4-12 capacity loading; Part 5 (a)–(d) |
| 10 | 40 | Fig. 4-13 eight blank waveform sheets; Required Results 1, Table 4-1R |
| 11 | 41 | Tables 4-2Ra, 4-2Rb, 4-3R; Discussion 1, 2(a) |
| 12 | 42 | Discussion 2(b), 3, 4, 5, 6, 7(a) |
| 13 | 43 | Discussion 7(b)–(e), 8(a)–(b) |
| 14 | 44 | Discussion 8(c)–(g), 9 |

---

## Still needed

- The **lab brief / handout** for the laboratory unit — what the department requires for the
  simulation phase and the practical phase. Scope is still unknown; the manual is indexed in full so
  that any scope is covered.
- Confirmation of which **simulator** the lab's phase 1 uses.
- Whether the current run of the unit issues **different decks** from these. These carry 2025 due
  dates, so they are last year's. If newer versions arrive, re-verify rather than assuming the
  corrections in `_verification-log.md` still apply to the same slide numbers.
- Any **past papers or CATs** for BEE 3102. None held.
