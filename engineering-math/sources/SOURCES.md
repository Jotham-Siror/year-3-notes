# Source material — Engineering Mathematics III (EMT 3101)

The files listed below are **lecturer-authored course material**. They are deliberately **not
tracked in version control** — they are the department's material, not ours, and this repository
carries only work we authored ourselves.

This manifest exists so anyone with the repository can reconstruct `sources/` from their own copies
of the same documents. Every `·CODE pN` citation in the knowledge base then resolves against the
same pages.

---

## Topic documents

| File | Pages | Size | Code | Notes |
|---|---|---|---|---|
| `Topic-1-Gamma-and-beta-functions.pdf` | 11 | 218 KB | **GB** | **The only typeset document** — LaTeX, Computer Modern, zero embedded images, full text layer. Carries **printed page numbers 3–13** in the footer; citations use those, so `·GB p6` is PDF page 4 |
| `Topic-2-CRV and Beta Distribution.pdf` | 22 | 6.1 MB | **CRV** | Handwritten, 300 dpi, no text layer. Scanned slightly off-register — the right margin is clipped on roughly half the pages. Pages 5, 6, 20, 21, 22 are entirely in red pen |
| `Topic-3.1-Binomial-Theorem.pdf` | 8 | 2.2 MB | **BIN** | Handwritten, 300 dpi. Page 1's lower half has two writing passes overlapping |
| `Topic-3.2-Maclaurin Theorem.pdf` | 7 | 2.0 MB | **MAC** | Handwritten, 300 dpi |
| `Topic-3.3-Leibniz Theorem.pdf` | 9 | 2.5 MB | **LEI** | Handwritten, 300 dpi. Opens with a trigonometric identity reference sheet |
| `Topic-4-Bessels equation and Bessels function.pdf` | 9 | 2.3 MB | **BES** | Handwritten, 300 dpi. Page header reads "Topic 6", not Topic 4 — see the numbering note below |

**Filenames matter.** The knowledge base cites page numbers, so a different scan or a re-paginated
copy will not line up. Keep the names exactly as written above, spacing and all.

## Assessed work

| File | Pages | Size | Notes |
|---|---|---|---|
| `Assignment-1-EMT-3101.pdf` | 1 | 115 KB | *Assignment 1, EMT 3101 Engineering Mathematics III*, dated 10 August 2026. Five questions, all to be answered. Transcribed and solved in `../knowledge-base/past-papers/` |

---

## ⚠ The topic numbering is inconsistent

Do not try to match these documents to a syllabus by their numbers.

| File | Filename says | The document itself says |
|---|---|---|
| Topic 1 (GB) | Topic 1 | signs off "\*\* End of Topic **Four** \*\*" on printed p13 |
| Topic 3.1 (BIN) | Topic 3.1 | margin of p1: "Topic 3" — consistent |
| Topic 4 (BES) | Topic 4 | header of p1: "Topic **6**" |

The knowledge base renumbers everything `01`–`06` in teaching order and records each document's
original label in the topic file's frontmatter. See `../knowledge-base/_verification-log.md`,
flags C2 and C15.

---

## How these files were made — provenance

*Read from the files themselves: metadata, embedded fonts, PDF anchors and image properties. Useful
because it explains several things that otherwise look like mistakes.*

### The typeset document (GB)

The Producer field says **iLovePDF**, which is a red herring — that was the *last* tool to touch the
file and it overwrote whatever wrote it. The embedded fonts give the real answer: **Computer Modern
Type 1 subsets with builtin encodings**, which is the pdfTeX signature, with no font package loaded
at all. Two extra faces are informative — **MSBM10** exists solely to print the ℕ in "n ∈ ℕ"
(`amssymb`), and **SFRM1095** is embedded, carrying an explicit `/Differences [36 /dollar,
136 /bullet]`, only to draw the bullets in the §1.1–1.2 lists (a TS1 text-companion font).

Measured page geometry: letter, 72 pt margins all round, text block 469 pt. The font sizes convert
(×72/72.27) to exactly **10.95 / 12 / 14.4 / 8 pt** — the LaTeX **11pt article** class sizes.

Reconstructed preamble:

```latex
\documentclass[11pt]{article}     % letterpaper is the class DEFAULT — no paper option was given
\usepackage{amsmath}              % the cases brace in eq (2)
\usepackage{amssymb}              % MSBM10
\usepackage{textcomp}             % TS1, for the bullet glyph
\usepackage[margin=1in]{geometry} % article's own default would be a 345 pt text block
\usepackage{hyperref}             % PDF bookmarks + 5 internal /Link cross-references
\newtheorem{example}{Example}[subsection]
\newtheorem{exercise}{Exercise}
```

### Why the printed pages start at 3

`hyperref` leaves a named destination for every numbered thing, and the 75 in this file map the
source exactly:

| Anchors | What they say |
|---|---|
| `section.1`, `subsection.1.1–1.3`, `subsubsection.1.2.1`, `1.3.1` | the section skeleton |
| `equation.1.1` … `equation.1.19` | **19 equations, contiguous** — nothing of section 1 is missing |
| `example.1.2.1–1.2.3`, `example.1.3.1` | a real `\newtheorem`, numbered `[subsection]` |
| `exercise.1–3` | a second `\newtheorem`, numbered globally |
| **`Item.22` … `Item.53`** | **the list-item counter starts at 22** |

`hyperref` numbers `\item` anchors on one running counter across the whole document. Equations start
at 1 but items start at 22 — so **21 list items preceded this content**, in material with no numbered
equations and no `\section`: an unnumbered front section of roughly two pages, which is exactly the
gap. **iLovePDF was used to strip those two pages before circulation**, leaving the original page
numbering (3–13) intact. That is why `·GB pN` cites printed pages, not PDF pages.

There are no `figure.` or `table.` anchors anywhere — not one float in thirteen pages.

### The handwritten five (CRV, BIN, MAC, LEI, BES)

| | |
|---|---|
| Every page | one JPEG, **3507 × 2480 px, RGB, 300 dpi** |
| MediaBox | A4 **landscape**, with `/Rotate 270` applied for viewing |
| Producer / Creator | **absent entirely** — no scanner app stamped these |

3507 × 2480 at 300 dpi is precisely A4 landscape, so the sheet was fed short-edge into a capture area
set to exactly A4.

> ### ⚠ This is the cause of the clipped right margins
>
> The scan window matches the paper size with **no tolerance**. A 210 mm sheet laid a few millimetres
> off a 210 mm capture area loses a strip from one edge — which is the entire explanation for flags
> **L1–L18**. It is not a resolution problem, and rescanning at higher dpi will not fix it.
> **Scanning at A3, or disabling exact-size cropping, would eliminate it.** Worth passing on if these
> pages are ever re-scanned.

Colour (RGB) rather than greyscale is the saving grace: it is why every red-pen correction survives
legibly.

**Timestamps** — one term's work, in batches. BIN and MAC were scanned **twenty seconds apart** (one
sitting, 24 May 2023); LEI and CRV on the evening of 25 May; BES two weeks later on 9 June, last,
matching teaching order. All carry a `+00'00'` offset — a device left on UTC rather than Nairobi time.

### Then versus now

Assignment 1 (Aug 2026) still has its banner intact:
**`pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026)`**. Same author, same default Computer Modern,
same `amssymb` — but a changed preamble: **A4** instead of letter, ~1.5 cm margins instead of 1 inch,
and **no `hyperref`**. Its timestamp offset is **−07'00'** (UTC−7), not Nairobi's UTC+3, which points
either to a cloud LaTeX service on US-west servers or to an unset clock.

### Why this matters for revision

**16.8114 is a typed literal.** Nothing in the source computes it — the symbolic form
$\frac{105}{16}\sqrt\pi$ is typeset correctly right beside it, and the decimal was worked out
elsewhere and keyed in.

That is the mechanism behind the pattern the verification log records: **the algebra is typeset, the
arithmetic is transcribed.** Five of the nine substantive errors are a correct symbolic line followed
by a hand-keyed number. LaTeX guarantees the mathematics is well-formed; nothing in this pipeline
ever checks whether the number beside it is true. Hence the log.

---

## Where to obtain these

They are distributed by the lecturer through the usual course channels — the class group and the
department's course page. Ask a classmate if you joined late.

## How to install them

Drop each PDF into the folder shown below, keeping the **exact filename**.

```
engineering-math/
└── sources/
    ├── SOURCES.md          ← this file (tracked)
    ├── Topic-1-Gamma-and-beta-functions.pdf
    ├── Topic-2-CRV and Beta Distribution.pdf
    ├── Topic-3.1-Binomial-Theorem.pdf
    ├── Topic-3.2-Maclaurin Theorem.pdf
    ├── Topic-3.3-Leibniz Theorem.pdf
    ├── Topic-4-Bessels equation and Bessels function.pdf
    └── Assignment-1-EMT-3101.pdf
```

## Do the notes work without them?

**Yes.** The knowledge base is self-contained — every equation, definition, figure description and
flagged error is transcribed into `../knowledge-base/`. You need these PDFs only to check a citation
against the original page, or to read the lecturer's own hand.

The page-by-page transcriptions these were built from are kept in
`../knowledge-base/_transcripts/` — **also untracked**, and for the same reason: they reproduce the
lecturer's pages almost line for line. They are the place to look when you want a whole page in
context rather than a topic as it is taught, and they do not ship with the repository.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
