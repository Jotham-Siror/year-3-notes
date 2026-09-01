# Knowledge-base format specification

Read this before adding a subject or editing an existing one. Consistency is what makes these
knowledge bases usable by both a person and a model — a file that drifts from the format still
*reads* fine but stops being reliably navigable.

---

## Folder layout

```
<subject-kebab-case>/
├── knowledge-base/
│   ├── 00-index.md            # entry point — always start here
│   ├── 01-<topic>.md          # topic files, in teaching order
│   ├── 02-<topic>.md
│   ├── _nomenclature.md       # every symbol, meaning, SI units, clashes
│   ├── _formula-sheet.md      # every equation, tagged to its source
│   ├── _verification-log.md   # every flagged error in the source material
│   ├── _transcripts/          # optional, UNTRACKED — see below
│   └── past-papers/           # optional
│       ├── 00-past-papers-index.md
│       ├── <CODE>-<TYPE>-<YYYY-MM-DD>.md
│       └── figures/*.svg      # redrawn, never screenshotted
├── assignments/               # optional — lab and assignment work we authored
├── study-guides/              # optional, human-facing HTML
└── sources/
    └── SOURCES.md             # manifest; the files themselves are untracked
```

Everything **kebab-case**. Leading `_` marks a cross-cutting file rather than a topic.

**`past-papers/` lives inside `knowledge-base/`**, not beside it — it is part of the verified
material and its index cross-references the topic files. `assignments/` and `study-guides/` sit at
subject level, because they are outputs rather than knowledge.

### `_transcripts/` — the extraction layer, never committed

Some subjects are built in two passes: a page-by-page transcription first, then the topic files.
Where that intermediate layer is kept, it goes in `knowledge-base/_transcripts/` and is **excluded
in `.gitignore`**.

We typed those files, but most of what is *in* them is the lecturer's page copied out line for line
— one transcript matched 481 of 485 source lines on a programmatic diff. That is the same thing
`sources/` holds, so it gets the same treatment. The authored product is the knowledge base beside
it: reorganised, corrected, analysed.

Keep them locally — they are the fastest way to check a citation without opening a PDF. Say in
`SOURCES.md` that they exist. **Where a transcript and a topic file disagree, the topic file wins**:
it carries the readings settled last.

## How to split topic files

Two different source shapes, two different rules:

| Source shape | Rule | Example |
|---|---|---|
| **One large deck** delivered up front | Split by **major course section**, in teaching order | Fluid Flow — 594 slides → 11 topic files |
| **Handouts issued progressively** | **One file per handout** | EEE3202 — WC1 → `01-wave-characteristics-1.md` |

For the progressive case, resist splitting a handout by theme. You cannot know the course's final
topic map until it is over, and theme-numbering forces a renumber every time a handout lands
out of order.

**Split threshold:** break a file up only when it covers **two genuinely independent themes** *and*
exceeds ~25 KB. A long file that is one continuous argument stays whole — state the reasoning in
`00-index.md` so the next person doesn't undo it.

## Frontmatter

Every file opens with YAML.

```yaml
---
kb: "Subject — COURSE CODE"
lecturer: "withheld"                      # always — see "What never gets committed"
section: "01 — Human-readable title"     # topic files
source: "CODE — 'Original Filename.pdf', N pp."
file_role: topic | index | nomenclature | formula-sheet | verification-log
subtopics: [...]                          # one line per teachable chunk
key_equations: [tag, tag, ...]
prerequisites: ["..."]
leads_to: ["..."]
verification_flags: 43
tags: [...]
---
```

## Tag vocabulary

Used inline throughout topic files. Do not invent new ones without adding them here.

| Tag | Means |
|---|---|
| `[def]` | a definition |
| `[derivation]` | step-by-step working |
| `[eq]` | a key equation — add `[eq: name]` to cross-reference the formula sheet |
| `[ex]` | worked example using the lecturer's own numbers |
| `[exercise]` | an unsolved problem set in the source material |
| `[fig]` | a figure, described from the **rendered** page |
| `[added]` | **not in the source** — supplied by us |
| `⚠ VERIFY` | a flagged suspected error, with an ID into the verification log |

`[added]` is not optional. Anything we supply that a reader might mistake for the lecturer's
material — a worked solution, a standard form, extra context — carries it.

## Citations

Every substantive claim carries its provenance inline:

- Slide-based source → `·slide 256`
- Page-based source → `·WC1 p7` (the handout code, then the page)

Define the code in `00-index.md`'s handout register and in `sources/SOURCES.md`.

## Mathematics

- **LaTeX throughout.** `$...$` inline, `$$...$$` display.
- **Never** put maths in backticks or fenced code blocks.
- Brace multi-character subscripts: `p_{\max}`, not `p_\max`. One malformed token dumps the whole
  block as raw markup.
- Every symbol defined underneath its first appearance, with units.
- Box the results worth memorising: `$$\boxed{\;...\;}$$`

## Verification — the part that matters most

This is what distinguishes these knowledge bases from a transcription.

**Method.** Work from **rendered page images**, not the PDF or PowerPoint text layer. Text
extraction mangles mathematics and silently hides defects — in EEE3202 a missing bracket in the
$\alpha$/$\beta$ formulas was invisible in the text layer and obvious in the render.

**Check every equation for:**

1. **Dimensional consistency** — catches roughly half of all real errors on sight
2. **Algebraic consistency** — does each step follow from the last?
3. **Symbol slips** — a variable silently swapped mid-derivation
4. **Mislabelled results** — a result labelled $\alpha$ that is actually $\beta$
5. **Self-reference** — if the symbol left of the equals sign also appears on the right, the label
   is wrong
6. **Numerical claims** — recompute every one

**Recording.** Four prefixes, and they mean different things. Keep them distinct — a reader who
cannot tell "the notes are wrong" from "the scan is unreadable" cannot trust either.

| Prefix | Means | Is it a defect? |
|---|---|---|
| `V1`, `V2`, … | **substantive** error in the source — changes the mathematics | yes |
| `C1`, `C2`, … | **cosmetic** error — typo, mislabel, numbering slip | yes, harmless once seen |
| `P1`, `P2`, … | defect in an **assessment paper** rather than the teaching material. IDs run across the whole `past-papers/` folder, not per paper | yes |
| `L1`, `L2`, … | **reading limitation** — the page is clipped, over-written or cut in the scan | **no.** The source is fine; the image is not |

`L` is for subjects built from scans, where "I could not read this" must never be filed alongside
"the lecturer got this wrong". Mark it `⚠ SCAN` inline, not `⚠ VERIFY`, and record whether each one
was later settled, reconstructed, or is genuinely unreadable.

**Do not reuse a letter across meanings.** MEC 3104 already uses `S1`–`S32` for *slide* flags, which
are real defects; a scan-limitation `S` in another subject would mean the opposite. EMT 3101 uses
`L` for exactly that reason.

Each `V` / `C` entry gives:

- what the page **prints**, verbatim
- what it **should be**
- **why**, in one line — ideally a check the reader can repeat

Flag inline at the point of use *and* collect in the log. Never silently correct: the reader must be
able to recognise the printed version when they meet it in an exam.

**Never invent.** If a figure or equation cannot be interpreted, say so and ask for a screenshot.
A gap honestly marked is worth more than a plausible guess.

## Voice

Neutral. No names, no personal detail, no second-person address to a specific student. Anything
personal belongs in `_personal/`, which is untracked.

Operating instructions belong in `CLAUDE.md` at the repository root, not in the knowledge base.

## What never gets committed

**This repository is public.** Four rules, and none of them is optional.

1. **No lecturer names, ever.** Not in frontmatter, not in prose, not in `SOURCES.md`. Write
   `lecturer: "withheld"` and refer to "the lecturer" or "the handout" in the text. The verification
   logs catalogue errors in the teaching material; attaching a named individual to that turns a
   claim about a *document* into a claim about a *person*. Cite the slide or page instead — it is
   also more useful.
2. **No contact details.** No email addresses, phone numbers, office locations or staff IDs.
3. **No third-party images.** No textbook scans, no web figures, no stock photos — regardless of
   watermark. Redraw as SVG (`figures/*.svg`) or write a caption describing what the figure showed.
   The rule is *commit what we authored*, and an image is the easiest place to break it.
4. **No verbatim reproductions of examination papers.** Transcribe the questions into Markdown and
   work the solutions; do not commit photographs or scans of the paper itself.

Before any push that adds material, re-run the safety checks in the README, and grep the staged
diff for names and digit runs.

## Adding a subject — checklist

1. `mkdir <subject>/knowledge-base <subject>/sources`
2. Move raw material into `sources/`, write `SOURCES.md`
3. Render every page to images; read them
4. Write topic files with full frontmatter, tags and citations
5. Extract `_nomenclature.md` — get the clash table right, it is the most-consulted section
6. Extract `_formula-sheet.md` in corrected form
7. Write `_verification-log.md` as you go, not afterwards
8. Write `00-index.md` last — coverage map, dependency order, verification summary, gap map
9. Add the subject to the table in `README.md` and `CLAUDE.md`
10. Verify: re-read pages against the file, recompute every number, confirm cross-references
    resolve, grep for personal detail

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
