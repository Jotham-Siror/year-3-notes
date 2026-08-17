# Source material — Thermodynamics (MEC 3105)

The files listed below are **lecturer-authored course material**. They are deliberately **not
tracked in version control** — we did not write them, and this repository carries only work we
authored ourselves.

This manifest exists so anyone with the repository can reconstruct `sources/` from their own copies.
Every citation in the knowledge base then resolves against the same document.

> **Additional reason these must never be committed.** The group-activity files are per-group
> worksheets and carry the **names of every student in each group**. This repository is public.
> They are ignored twice over — by the `*.docx` extension rule and by the `**/sources/*` rule — and
> the transcriptions in `../knowledge-base/exercises/` refer to groups by **number only**.

---

## `lecture-notes/` — the knowledge base is built from these

Five documents, 200 pages total. The **Code** column is what the knowledge base cites.

| Code | File | Pages | Size | Format | Course topic |
|---|---|---|---|---|---|
| **TT** | `3.0Temperature and Thermometry 1.pdf` | 17 | 0.9 MB | typed notes (Nitro Pro) | Topic 1 — 1.1 Temperature & Thermometry |
| **FL** | `3.01 First_Law_of_Thermodynamics.pdf` | 37 | 3.0 MB | PowerPoint → Print to PDF | Topic 1 — 1.3 Work, Heat & First Law |
| **EPC** | `3.02 - Energy Equations and Phase Changes.pdf` | 92 | 5.0 MB | PowerPoint → Print to PDF | Topic 2 — Energy Equations & Phase Changes |
| **TC** | `3.1 MEC 3105 Power production and Thermodynamic Cycles.pdf` | 24 | 1.7 MB | PowerPoint → Print to PDF | Topic 3 — Power Production & Cycles (part 1) |
| **HE** | `3.2 MEC 3105 Power production and Thermodynamic Cycles.pdf` | 30 | 1.4 MB | PowerPoint → Print to PDF | Topic 3 — Power Production & Cycles (part 2) |

Provenance is cited as **·TT p7** for the page-based document and **·EPC s68** for the slide decks.

**Letter codes, not the file numbers.** The lecturer's `3.0 / 3.01 / 3.02 / 3.1 / 3.2` prefixes are
one keystroke apart (`·3.1 s12` vs `·3.01 s12`) and do not match the decks' own internal topic
numbering — EPC's title page reads "Topic 2". Letters remove both hazards.

### Pages with no text layer

A large share of the equation slides are **images**, invisible to text extraction:

| Code | Image-only pages | Of total |
|---|---|---|
| FL | 15–18, 21, 23–26, 28–37 | 19 / 37 |
| EPC | 1–2, 4, 18, 20–21, 31–38, 59–61, 64, 72, 84, 89–90, 92 | 23 / 92 |
| TT, TC, HE | none | — |

Every page is read from a **render**, never the text layer — `../../docs/kb-format.md` § Verification
requires it, and these two decks are why.

## `group-activities/` — assessed exercises

Both sets belong to **Topic 1**. GA numbering is not topic numbering.

| Code | Folder | Files | Covers |
|---|---|---|---|
| **GA1** | `ga-1/` | 8 per-group sheets + 1 master | Topic 1 Part 1 — 1.1 Thermometry, 1.2 Equations of State (ideal gas, Van der Waals, Z) |
| **GA2** | `ga-2/` | 9 per-group sheets | Topic 1 Part 2 — 1.3 Work, Heat and the First Law |

`ga-1/MEC_3105_Group_Exercises_Topic1_Part1 - Copy.docx` is the **master**: it contains every
group's problem set plus a facilitator note, so GA1 is one document to transcribe rather than nine.
The per-group sheets are near-identical slices of it — diff rather than assume.

Each sheet is **Part A** (a guided discussion sequence, identical across all groups) and **Part B**
(a numerical problem set, values varied per group). **No answers are supplied**; every solution in
the knowledge base is therefore tagged `[added]`.

`GA 1.zip` and `GA 2.zip` are the archives the folders were extracted from, kept as received.

Cited as **·GA1 G3 Part B Q2**.

---

## Where to obtain these

Through the usual course channels.

## How to install them

```
thermodynamics/
└── sources/
    ├── SOURCES.md                          ← this file (tracked)
    ├── lecture-notes/
    │   ├── 3.0Temperature and Thermometry 1.pdf
    │   ├── 3.01 First_Law_of_Thermodynamics.pdf
    │   ├── 3.02 - Energy Equations and Phase Changes.pdf
    │   ├── 3.1 MEC 3105 Power production and Thermodynamic Cycles.pdf
    │   └── 3.2 MEC 3105 Power production and Thermodynamic Cycles.pdf
    └── group-activities/
        ├── ga-1/   (9 .docx)
        ├── ga-2/   (9 .docx)
        ├── GA 1.zip
        └── GA 2.zip
```

Keep the **exact filenames**, odd spacing included, and do not re-order slides — the knowledge base
cites page and slide numbers throughout.

### A duplicate was found

A second copy of the temperature notes sat at the subject-folder root as
`Temperature and Thermometry 1.pdf` (876 KB, vs 915 KB for `3.0…`). Different bytes, but **17 pages
and identical extracted text** — a re-save, not a revision. Both redundant copies were moved to
`../_to_delete/`. Only the `3.0…` copy is authoritative.

## Do the notes work without them?

Not yet — the knowledge base is under construction. See `../knowledge-base/00-index.md` for build
status. Once complete, the sources are needed only to check a citation against the original page.

**Total not tracked: ~12.9 MB.**

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
