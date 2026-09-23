# Source material — Electromagnetic Fields (EEE3202)

The files listed below are **lecturer-authored course material**. They are deliberately **not
tracked in version control** — they are the department's material, not ours, and this repository
carries only work we authored ourselves.

This manifest exists so anyone with the repository can reconstruct `sources/` from their own copies
of the same documents. Every `·WC1 pN` citation in the knowledge base then resolves against the same
pages.

---

## `current/` — this cohort

| File | Pages | Size | Code | Notes |
|---|---|---|---|---|
| `ELECTROMAGNEIC WAVE CHARACTERISTICS I.pdf` | 18 | 779 KB | **WC1** | Course lecturer. Title typo (*ELECTROMAGNEIC*) is in the original filename — do not silently correct it, or citations stop matching |
| `Transmission lines.pdf` | 16 | 1.05 MB | **TL** | Course lecturer, same author as WC1. Added 10 Sep 2026. **The most error-dense document in the set** — read `../knowledge-base/_verification-log.md` § T before quoting any equation from it. Note the space in the filename |
| `TransmissionLineTheory.pdf` | 22 | 1.50 MB | **TLT** | ⚠ **Not the lecturer's own writing.** A slide deck he distributed, compiled from Sadiku 5e, Ida 3e and Pozar 4e (cited on its own p2). Added 3 Sep 2026. Cleaner than TL, and the **only** source in the repository for the Smith chart and for $Z_0$ in terms of R, L, G, C |

> **⚠ TL and TLT are one topic across two documents.** Both are current-cohort and both are
> examinable, but only TL is the lecturer's own writing.
> `../knowledge-base/02-transmission-lines.md` merges them into a single topic file and tags every
> line `·TL pN` or `·TLT pN` so the distinction survives. See that file's header for who covers what.

> **·TLT p20 is a full blank Smith chart** — resistance/reactance grid, both perimeter wavelength
> scales, angle of reflection coefficient, and the radially scaled SWR / return-loss rule. Print that
> page before attempting the 1 Oct 2025 CAT Q1(b) or the 23 Oct 2025 exam Q2(b); 11 marks each are
> unattemptable without it. This closes errata P22 and P27.

**Expected:** further material in the same series (*Wave Characteristics II*), and — still absent
from the repository — **rectangular waveguides** and **computational electromagnetics / the
finite-difference method**, both of which are examined every year. Add a row as each arrives, and a
matching entry in the document register in `../knowledge-base/00-index.md`.

## `old-cohort/` — previous cohort, reference only

Retained for cross-checking and for filling syllabus gaps until this year's equivalent handout is
issued. See `../knowledge-base/00-index.md` § Gap map.

| File | Pages | Size | Code | Notes |
|---|---|---|---|---|
| `ELECTROMAGNETIC WAVES.pdf` | 31 | 841 KB | EMW | The fullest of the three — Maxwell through to reflection and transmission |
| `THE UNIFORM PLANE WAVE.pdf` | 16 | 647 KB | UPW | Largely a subset of EMW, but uniquely holds two worked examples |
| `POLARIZATION OF WAVES.pdf` | 4 | 562 KB | POL | Signed by the lecturer. Currently the **only** coverage of syllabus objective (iv) |

---

## Where to obtain these

They are distributed by the lecturer through the usual course channels — the class group and the
department's course page. Ask a classmate if you joined late.

## How to install them

Drop each PDF into the folder shown above, keeping the **exact filename**. The knowledge base cites
page numbers, so a different edition or a re-paginated scan will not line up.

```
electromagnetic-fields/
└── sources/
    ├── SOURCES.md          ← this file (tracked)
    ├── current/
    │   ├── ELECTROMAGNEIC WAVE CHARACTERISTICS I.pdf
    │   ├── Transmission lines.pdf
    │   └── TransmissionLineTheory.pdf
    └── old-cohort/
        ├── ELECTROMAGNETIC WAVES.pdf
        ├── THE UNIFORM PLANE WAVE.pdf
        └── POLARIZATION OF WAVES.pdf
```

## Do the notes work without them?

**Yes.** The knowledge base is self-contained — every equation, definition, figure description and
flagged error is transcribed into `../knowledge-base/`. You need these PDFs only to check a citation
against the original page or to read the lecturer's own wording.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
