# Source material — Analogue Electronics I (BEE 3103)

The files listed below are **course material we did not write**. They are deliberately **not tracked
in version control** — this repository carries only work we authored ourselves.

This manifest exists so anyone with the repository can reconstruct `sources/` from their own copies.
Every citation in the knowledge base then resolves against the same page.

> **A second reason these must never be committed.** Four of the seven lesson documents are
> **photographs of a printed textbook** — a publisher's copyright, not ours — and the primary
> lecture notes were obtained through a document-sharing service and carry that service's branding
> plus a third party's name and email address in the footer of every page. All of it is ignored twice
> over, by the `*.pdf` extension rule and by the `**/sources/*` rule. The knowledge base carries the
> physics rewritten in our own words, every figure described rather than reproduced, and **no names
> or contact details from any source**.

Three tiers, **328 pages**, in descending order of authority.

---

## `lecture-notes-jkuat/` — TIER 1, the primary source

**The course's own lecture notes. 100 pages. This is what BEE 3103 actually teaches**, and it sets
the scope and emphasis of the whole knowledge base.

| Code | File | Pages | Size | Format |
|---|---|---|---|---|
| **J** | `Analogue Electronics I Lecture Notes - JKUAT.pdf` | 100 | 14.8 MB | **image-only, no text layer at all** |

Provenance is cited as **·J p33** — the **PDF** page.

**Page numbering.** PDF page 1 is a download-service cover sheet with no course content. The
document's own printed page number runs **one behind the PDF page** — PDF p33 shows printed 32 — and
the offset holds unbroken from PDF p2 (printed 1) to PDF p100 (printed 99). All citations use the PDF
page.

**Known damage in this copy**, all recorded in `../knowledge-base/00-index.md` § Gap map:

- **Opaque blocks over text on eleven pages** — ·J p35, p40, p41, p42, p44, p53, p55, p58, p87, p88,
  p89. Contrast recovery was tested on each; **nothing survives underneath**. Seven of the covered
  terms were inferred with certainty from the surrounding text and are labelled `[added]`; the rest
  are marked `⚠ REDACTED` and left open.
- **·J p25** body absent, **·J p26** upper half absent, **·J p30 entirely blank** (printed page 29
  gone outright).
- **Twelve section headings absent**, lost with blank space above them.
- **No contents page, no syllabus, no reference list**, and the document **ends mid-topic** on ·J p100.

**What it does not cover.** The notes stop at the FET. There is no $h$-parameter analysis, no
feedback theory, no frequency response, no fabrication, and $g_m$ is named once and never defined.
Those four topics come from tier 2 — see the topic map in `../knowledge-base/00-index.md`.

## `lecture-notes/` — TIER 2, the supporting lesson documents

Seven documents, **169 pages**. Fuller textbook treatment of diodes, rectifiers, BJTs and FETs, and
the **only** source in the unit for four topics tier 1 omits.

| Code | File | Pages | Size | Format | Topic |
|---|---|---|---|---|---|
| **L1** | `Lesson 1 Notes Diodes.pdf` | 18 | 2.7 MB | textbook articles, reset and re-typed | Diodes |
| **L2** | `Lesson 2 Rectifiers.pdf` | 26 | 3.0 MB | textbook articles, reset and re-typed | Rectification |
| **L3** | `Lesson 3 Notes Bipolar Junction Transistor .pdf` | 25 | 544 KB | scanned textbook, ch. 57–58 | BJT and biasing |
| **L4** | `Lesson 4 Field Effect Transistors.pdf` | 24 | 890 KB | scanned textbook, ch. 63 | JFET and MOSFET |
| **L5** | `Lesson 5 Fabrication of Transistors - Construction .pdf` | 23 | 683 KB | scanned textbook, ch. 67 | **Sole source** — fabrication and ICs |
| **L6** | `Lesson 6 H parameters for circuits.pdf` | 26 | 595 KB | **image-only**, no text layer | **Sole source** — $h$-parameters |
| **L7** | `Lesson 7 Multistage Amplifier feedback and frequency response .pdf` | 27 | 420 KB | scanned textbook, ch. 60–62 | **Sole source** — feedback, frequency response |

Provenance is cited as **·L3 p12** — the lesson code, then the **PDF** page.

### Two filename traps

1. **Lessons 3, 5 and 7 have a trailing space before `.pdf`.** It is in the original filenames. Do
   not silently tidy it, or a shell glob written against the tidy names will miss them.
2. **`Lesson 5 ... - Construction .pdf`** also carries a space either side of the hyphen. Same rule.

### PDF page numbers versus printed page numbers

**L3, L4, L5 and L7 are photographs of printed textbook pages** and carry the book's own page numbers
(in the 2100–2500 range) and its own section numbering (57.1, 63.4, 67.12, 60.42 …). Those numbers do
**not** match the PDF pages. **All citations use the PDF page**; each topic file states its printed
range once, near the top.

## `reference-decks/` — TIER 3, reference only

Four slide decks, **59 pages**. Mapped page by page in `../knowledge-base/_reference-decks.md`, but
**not verified and not authoritative**.

| Code | File | Pages | Size | Covers |
|---|---|---|---|---|
| RD1 | `ANALOGUE ELECTRONICS INTRODUCTION.pdf` | 4 | 166 KB | What electronics is; analogue vs digital signals |
| RD2 | `MATERIALS USED IN ELECTRICAL & ELECTRONIC CIRCUITS.pdf` | 18 | 1.3 MB | Conductors, insulators, semiconductors; band gaps; doping |
| RD3 | `SEMICONDUCTOR DIODES.pdf` | 20 | 934 KB | Junction diodes and six device types |
| RD4 | `The Electronic System.pdf` | 17 | 904 KB | The signal chain: sensors, ADC/DAC, processor, actuators |

RD4 covers ground **no other source touches** — the electronic system end to end. RD3 overlaps both
tier 1 and tier 2 on diodes and **disagrees with them in three places, in each of which they are
right**; see `../knowledge-base/00-index.md` § Reference decks before teaching from it.

---

## Text layers — why every page was read from a render

| Code | Text layer | Consequence |
|---|---|---|
| **J** | **None at all — zero characters on all 100 pages** | Extraction returns an empty document |
| L1, L2 | **Header only** — about 65 characters per page, the running title and nothing else | The body is an image |
| L3, L4, L5, L7 | OCR of a scan, ~2 000 characters per page | Prose extracts, **mathematics does not** — subscripts, $\Delta$, $\beta$ and brackets are silently mangled |
| L6 | **None at all — zero characters on all 26 pages** | Extraction returns an empty document |
| RD1–RD4 | Present and usable | Read from renders anyway, for consistency |

All 328 pages were rendered to images and read from the render, as `../../docs/kb-format.md`
§ Verification requires. This subject is a good argument for that rule: several logged defects — a
missing bracket, a dropped µ prefix, a minus set as $\times$, an exponent typeset as a denominator —
are invisible in a text layer and obvious in the render.

## Where to obtain these

The lesson documents and slide decks are distributed through the usual course channels — the class
group and the department's course page. Ask a classmate if you joined late.

## How to install them

Drop each PDF into the folder shown below, keeping the **exact filename, trailing spaces included**.
The knowledge base cites page numbers, so a different edition or a re-paginated scan will not line up.

```
analogue-electronics/
├── knowledge-base/
└── sources/
    ├── SOURCES.md                       ← this file (tracked)
    ├── lecture-notes-jkuat/             ← TIER 1
    │   └── Analogue Electronics I Lecture Notes - JKUAT.pdf
    ├── lecture-notes/                   ← TIER 2
    │   ├── Lesson 1 Notes Diodes.pdf
    │   ├── Lesson 2 Rectifiers.pdf
    │   ├── Lesson 3 Notes Bipolar Junction Transistor .pdf
    │   ├── Lesson 4 Field Effect Transistors.pdf
    │   ├── Lesson 5 Fabrication of Transistors - Construction .pdf
    │   ├── Lesson 6 H parameters for circuits.pdf
    │   └── Lesson 7 Multistage Amplifier feedback and frequency response .pdf
    └── reference-decks/                 ← TIER 3
        ├── ANALOGUE ELECTRONICS INTRODUCTION.pdf
        ├── MATERIALS USED IN ELECTRICAL & ELECTRONIC CIRCUITS.pdf
        ├── SEMICONDUCTOR DIODES.pdf
        └── The Electronic System.pdf
```

## Do the notes work without them?

**Yes.** The knowledge base is self-contained — every equation, definition, figure description, worked
example and flagged defect is transcribed into `../knowledge-base/`. You need these PDFs only to check
a citation against the original page, or to read a source's own wording.

**Three exceptions**, the only pages in 328 that could not be read:

1. **·J p30** — entirely blank in this copy. Printed page 29 of the lecture notes is missing.
2. **·J p41** — two opaque blocks over the LED semiconductor material names.
3. **·L5 p16, Fig. 67.20** — a washed-out photograph that cannot be identified at any resolution.

A clean copy of any of the three would close the last gaps.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
