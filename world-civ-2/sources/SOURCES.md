# World Civilization II — source manifest

Raw source material for this subject. **None of these files is committed** — they are excluded by the
repository-wide `*.docx` rule and by `**/sources/*`. This manifest records what they are so the
knowledge base can cite them without reproducing them.

## Register

| Code | File | Kind | Length | Cited as |
|---|---|---|---|---|
| `FR` | `THE FRENCH REVOLUTION .rtf.doc` | lecture notes | 2,948 words, 9 pp. | `·FR p1` … `·FR p9` |
| `RNW` | `French revolutionary and Napoleonic wars.docx` | reference article | 1,309 words, 12 blocks | `·RNW ¶2` … `·RNW ¶12` |
| `NW` | `THE NAPOLEONIC WARS.docx` | reference article | 1,403 words, 14 blocks | `·NW ¶1` … `·NW ¶14` |

## FR — the lecture notes

Rich Text Format saved with a `.doc` extension. Handout-style: dash bullets, numbered causes,
lecturer's own section headings, and two set questions embedded in the body (p5).

**Coverage.** The Old Regime through to the declaration of war of April 1792. Structured as
interpretations → five causes → the progress of the Revolution → the moderate phase 1789–91 →
five reasons for radicalization. It stops at the outbreak of war; the Terror is named in the final
line but never treated.

**Page numbers are real.** The document carries printed page numbers 1–9. Citations in the topic
files were taken from a PDF render, not from the text stream, so `·FR p7` is that document's own
page 7.

**Extraction method.** Converted with LibreOffice to both plain text and PDF, and independently
re-parsed from the raw RTF control words. The two extractions were compared before writing; they
agree, so no content was lost to the conversion.

## RNW and NW — the two reference articles

Both are prose articles on the same subject, downloaded rather than authored, and **their origin is
not recorded in the files themselves**. Style and structure suggest general-reference encyclopaedia
prose for `RNW` and a study-guide publisher for `NW`, but neither carries a citation, byline or URL,
so no attribution is asserted here. If the original sources are identified later, record them in
this table.

**Consequence for the knowledge base.** Because provenance is unconfirmed and this repository is
public, `02-revolutionary-and-napoleonic-wars.md` is written as our own reorganisation of what these
two documents say, with each claim cited to its block. Their wording is not reproduced.

**They overlap heavily** — roughly 60% of their factual content is common — and they are not
independent witnesses in the places where they agree, since both appear to descend from the same
standard account. Where they *disagree*, the topic file says so rather than picking one.

**Block numbering.** Counted as pandoc plain-text blocks including headings, so `RNW ¶3` is the
heading "Monarchies at war with the French Republic" and `RNW ¶4` the paragraph under it. `NW ¶1` is that
document's title block, "Napoleonic Wars (1799-1815)", which is cited because the date range in the title is
itself a claim about the subject's scope — see `D1`.

## Not yet held

- No past papers for this unit. `knowledge-base/past-papers/` will be created when the first one arrives.
- No course outline or syllabus, so the index cannot yet show a gap map against the examinable scope.
- No handout covering the Terror, Thermidor, the Directory, or the period after 1815.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
