---
kb: "World Civilization II"
unit_code: "unknown — see 'Unit code' below"
lecturer: "withheld"
file_role: index
source: "FR — lecture handout, 9 pp.; RNW and NW — two reference articles"
built: "extracted and verified from all three documents; the handout converted twice independently and diffed before writing"
coverage: "FR pp.1-9, RNW ¶2-12, NW ¶1-14 — complete, no gaps within the sources"
total_verification_flags: 32   # 7 substantive (V1-V7) + 25 cosmetic (C1-C25); plus 4 cross-source discrepancies D1-D4
past_papers: 0
---

<!-- Compiled by Jotham-JS, 2026. World Civilization II knowledge base. -->

# World Civilization II — Knowledge Base Index

**What this is.** A verified map of the three World Civilization II documents — a nine-page lecture handout
on the French Revolution and two reference articles on the Revolutionary and Napoleonic Wars — reorganised
into two topic files plus a chronology, a glossary and a verification log. Every claim is anchored to the
page or block it came from. Where a source appears to contain an error it is flagged inline (⚠ VERIFY),
corrected against standard reference, and logged in `_verification-log.md`; the source's own wording is never
silently overwritten.

**How to use it.** Find your topic in the coverage map and open that file. `_chronology.md` collects every
date in one place; `_glossary.md` resolves the term clashes and is the section most worth reading before an
exam. Revision material — essay skeletons, quizzes, flashcards and comparison tables — lives in
`study-guides/` beside this knowledge base, not in it.

> Operating instructions — how to navigate and teach from this knowledge base — live in `CLAUDE.md` at the
> repository root, and the format specification in `docs/kb-format.md`.

## Two format substitutions

This is the repository's first **non-technical** subject, and two of the standard cross-cutting files have no
meaning here. They are replaced, not dropped:

| Standard file | Replaced by | Why |
|---|---|---|
| `_nomenclature.md` — symbols, units, clashes | **`_glossary.md`** — terms, definitions, **clash table** | there are no symbols, but there are confusable terms, and they behave exactly like symbol clashes |
| `_formula-sheet.md` — every equation in one place | **`_chronology.md`** — every date in one place | the single-sheet reference you actually carry into a history exam is the timeline |

Frontmatter follows the same logic: topic files carry **`key_dates`** where a technical subject carries
`key_equations`. The verification log adds one prefix, **`D`**, for cross-source discrepancies — it is not
used elsewhere in the repository and is defined at the top of that file.

Both substitutions and the `D` prefix are now written into **`docs/kb-format.md` § Non-technical subjects**
as the standard for any humanities subject added after this one, with this knowledge base named as the
worked example. They are no longer a local exception.

## Unit code

**Still not known** — none of the three documents prints one, and no course outline has been supplied. Every
other subject in this repository keys its frontmatter to a unit code; this one stays `unit_code: "unknown"`
until the code is confirmed.

The subject is nonetheless **registered at repository level** as of 7 September 2026: it has its row in
`README.md` and `CLAUDE.md`, its card in `index.html`, and its format substitutions are written into
`docs/kb-format.md` as the rule for any non-technical subject added later. Withholding the registration was
the wrong call — a subject missing from those three files is invisible to anyone starting a session, and an
unknown code is a fact to record, not a reason to hide the subject.

**When the code is confirmed**, update the frontmatter of this file, `01`, `02`, `_glossary.md`,
`_chronology.md` and `_verification-log.md`, then replace *not confirmed* in the `README.md` and `CLAUDE.md`
tables, the `CODE NOT CONFIRMED` label in `index.html`, and the bullet in `CLAUDE.md`'s unit-code warning.

## Source register

| Code | What it is | Length | Cited as |
|---|---|---|---|
| `FR` | the lecture handout — French Revolution | 2,948 words, 9 printed pages | `·FR p1` … `·FR p9` |
| `RNW` | reference article — the Revolutionary and Napoleonic Wars | 1,309 words, 12 blocks | `·RNW ¶2` … `·RNW ¶12` |
| `NW` | reference article — the Napoleonic Wars | 1,403 words, 14 blocks | `·NW ¶1` … `·NW ¶14` |

`FR` page numbers are the document's own printed pages, taken from a PDF render rather than the text stream.
`RNW` and `NW` block numbers are pandoc plain-text blocks, headings included — `NW ¶1` is that document's
title block, cited for the date range it asserts. Full details, and the reason
neither article is attributed to a named publication, are in `sources/SOURCES.md`.

## Tag legend (used in both topic files)

`[def]` definition · `[hist]` historical note · `[ex]` worked or expanded example · `[exercise]` a question
set in the source · `[added]` **not in the source — supplied by us** · `·FR pN` / `·RNW ¶N` / `·NW ¶N`
provenance · `⚠ VERIFY` a flagged suspected error, with an ID into the verification log.

## Coverage map

| File | Source range | Size | Topic | Key content |
|---|---|---|---|---|
| `01-french-revolution.md` | FR pp.1-9 | 30 KB | The French Revolution | interpretations; five causes; the 1789 breakthrough; the moderate phase 1789-91; five reasons for radicalization; the two set questions |
| `02-revolutionary-and-napoleonic-wars.md` | RNW ¶2-12, NW ¶1-14 | 26 KB | The Revolutionary and Napoleonic Wars | seven coalitions; Valmy to Waterloo; Napoleon's rise and rule; the Continental System; the Peninsular War; Russia 1812; the Congress of Vienna and the legacy |

**Sections inside the files.** `01` runs §1.1 interpretations, §1.2 causes (five numbered sub-sections),
§1.3 the progress of the Revolution, §1.4 the moderate phase, §1.5 radicalization (five numbered
sub-sections). `02` runs §2.1 the wars in outline, §2.2 monarchies at war 1792-95, §2.3 the rise of Napoleon,
§2.4 the Continental System and the Peninsular War, §2.5 the defeat 1812-15, §2.6 Vienna and the legacy.

### Why only two topic files

`docs/kb-format.md` gives two rules that decide this. For material **issued progressively**, the rule is one
file per handout, and it warns against splitting by theme because the course's final topic map is not knowable
until the course is over. The **split threshold** then permits a break only when a file covers two genuinely
independent themes *and* exceeds roughly 25 KB.

`01` is **30 KB and stays whole.** It exceeds the size threshold but fails the independence test: the handout
is one continuous argument running from the old regime to the declaration of war, in which the moderate phase
is intelligible only as the settlement the causes produced, and the radicalization only as that settlement
failing. Splitting it at §1.3 would put the cause of a thing in one file and its effect in another. Recorded
here, per the specification, so the reasoning is not undone by accident.

The two reference articles are **merged into `02`** rather than kept as one file each. They are not
successive handouts — they are two accounts of the same subject, overlapping by roughly 60%, and holding them
apart would duplicate most of their content while hiding the four places where they disagree.

**If more handouts arrive**, they append as `03`, `04` and so on, and nothing renumbers.

## Dependency / teaching order

`01` → `02`. The handout ends with the declaration of war of April 1792 and the sentence that it "inaugurated
the reign of terror" ·FR p9; `02` opens on the wars that followed and picks Napoleon up in 1799. `02`
assumes `01`'s account of why revolutionary France went to war, and refers back to it explicitly in §2.2.

Within `01`, §1.4 and §1.5 both depend on §1.2 — the moderate phase answers the causes, and the radicalization
undoes the moderate phase.

## Gap map — what your material does not cover

This is the most important section of this index. Three gaps, in order of seriousness:

1. **1793-1799 is missing entirely.** The **Terror**, **Thermidor** and the **Directory** are named in
   passing — the Terror in the handout's final line ·FR p9, Thermidor and the Directory in ·NW ¶2 — and
   **explained nowhere**. This is a gap of six years between the two topic files, and it covers the
   Revolution's most heavily examined phase. Nothing in this knowledge base can answer a question on it.
2. **Coalitions four, five and six are undescribed.** The sources say seven coalitions opposed France
   ·RNW ¶4 and detail the first, second, third and seventh. A question asking you to trace all seven is not
   answerable from this material.
3. **No syllabus, and no past papers.** Without a course outline there is no way to show what the examinable
   scope is, so this gap map is a map of the *sources'* silences, not of the *course's*. `past-papers/` does
   not exist yet; create it on the standard layout when the first paper arrives.

**Under no circumstances fill these gaps from memory when teaching from this base.** Say the material is not
held and offer to build it from a handout that covers it.

## Verification summary

**32 flags: 7 substantive, 25 cosmetic. Plus 4 cross-source discrepancies.** Full entries, each with what the
page prints and a check the reader can repeat, are in `_verification-log.md`.

**The seven substantive errors — do not absorb these from the raw sources:**

| ID | Source | Printed | Correct |
|---|---|---|---|
| **V1** | FR p9 | France declared war on "Prussia and Austria", April 1792 | on **Austria alone**, 20 April 1792; Prussia entered afterwards |
| **V2** | FR p3 | the "Tennis court resolution", placed **after** the royal session of 23 June | the **Tennis Court Oath**, sworn **20 June 1789**, *before* that session |
| **V3** | FR p2 | eighteenth-century foreign policy "costly but **successful**" | costly and **unsuccessful** — the same sentence names two lost wars |
| **V4** | FR p3 | the clergy joined "**This day later**" | **19 June 1789**, two days after the 17th |
| **V5** | RNW ¶12 | Waterloo "June **16-18**, 1815" | **18 June 1815**; the 16th is Ligny and Quatre Bras |
| **V6** | RNW ¶8 | the **Parthenopean** Republic in **Piedmont** | Parthenopean = **Naples**; Piedmont = **Subalpine** Republic |
| **V7** | NW ¶7 | no Europe-wide conflict between 1815 and **1914** | the **Crimean War (1853-56)** and the unification wars; only a *general* great-power war was avoided |

**The cosmetic 25** are typos and garbled words, concentrated in the handout: `Thurgot` for Turgot, `convince`
for convene twice, `task exemptions` for tax exemptions, `persons` for peasants, `enlightment`, `Rosseau`,
`levy en masse`, and others. Individually harmless — but **C8** (`persons` for `peasants`) and **C11**
(`convince` for `convene`) obscure the meaning of their sentences, and are worth knowing before you read the
handout cold.

**The four discrepancies (D1-D4)** are places where the two reference articles disagree: when the wars begin;
why the Russian campaign failed; what Trafalgar meant; and the date of Waterloo. Only the last is an error;
the other three are framing differences, and `02` presents both sides rather than choosing.

**Method.** The handout was converted twice independently — LibreOffice to plain text and to PDF, and a
separate parse of the raw RTF control words — and the two extractions were diffed before any topic file was
written, so nothing was lost in conversion. Every date, name, treaty and battle in all three documents was
checked individually. No source required a screenshot; nothing was left unreadable.

## Study guides

Human-facing revision material, built from this knowledge base rather than from the raw sources:

| File | What it is |
|---|---|
| `study-guides/question-bank.md` | 10 questions with full essay skeletons — claim, paragraph order, evidence with citations, and the trap each question is set to catch — plus 10 more to attempt cold. The two questions marked **[SET]** are the lecturer's own ·FR p5 |
| `study-guides/quizzes.md` | 60 questions in five sets, answers at the foot. Seven are marked **[trap]** — one per substantive flag |
| `study-guides/flashcards.md` | 108 cards in 11 decks, each carrying its citation. Deck 11 is the seven source errors |
| `study-guides/flashcards.csv` | the same 108 cards as Front / Back / Deck, for Anki. Generated together with the markdown, so the two always agree |
| `study-guides/comparison-tables.md` | 11 tables — the interpretations sorted on two axes, causes with their limits, the phases side by side, the four revolts, coalitions, treaties, battles, method against counter-method, the Continental System's intent against its outcome, what survived 1815, and the two reference sources compared |

## Provenance notes

- Text extracted directly from the source files; the handout's page numbers taken from a PDF render so they
  are its own printed pages. Nothing was inferred from formatting alone.
- Neither reference article records its origin, so **no attribution is asserted** and **neither one's wording
  is reproduced** — `02` is a reorganisation with per-claim citations. See `sources/SOURCES.md`.
- Where the sources were ambiguous, the ambiguity is recorded rather than resolved. Nothing was invented.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
