# Year 3 Engineering — Knowledge Bases

Verified, machine-readable knowledge bases for Year 3 electrical-engineering coursework at
Strathmore University. Built to be used **with Claude** as a study tutor that already knows the
course — but perfectly readable on their own.

**📖 Read them online: <https://jotham-siror.github.io/year-3-notes/>** — no clone, no GitHub
account, works on a phone. That's also the only place the interactive study guides actually render;
GitHub shows `.html` files as source code.

| Subject | Code | Source material | Status |
|---|---|---|---|
| [Fluid Flow](fluid-flow/knowledge-base/00-index.md) | MEC 3104 | 594-slide lecture deck | 11 topics, 50 flags, 2 past papers |
| [Electromagnetic Fields](electromagnetic-fields/knowledge-base/00-index.md) | EEE3202 | Lecture handouts, issued progressively | 1 handout, 43 flags |
| [Thermodynamics](thermodynamics/README.md) | MEC 3105 | 5 lecture documents (200 pp.) + assessed group activities | 7 topic files, 50 flags, both group activities |

## What this actually is

Each subject's lecture material has been transcribed into structured Markdown: every equation in
LaTeX, every claim anchored to the slide or page it came from, every figure described, and **every
suspected error in the original flagged and corrected**.

That last part is the reason this exists. Across the three subjects there are **143 documented
defects** in the lecture material — wrong constants, mislabelled results, broken derivations. A few
examples:

- MEC 3104 slide 256: the Torricelli derivation drops the elevation term, and its own algebra yields
  $v = 0$
- EEE3202 p8: $\mu_0$ printed as $4\pi\times10^{-12}$ H/m, which makes the speed of light come out
  317× too fast — contradicted three lines later on the same page
- EEE3202 pp. 9–16: $\sigma$ used for both conductivity *and* the attenuation constant, leaving six
  equations self-referential and unsolvable as printed
- MEC 3105, First Law slide 20: the deck's only worked example flips the sign of the work term, so
  its printed answer of $-505\ \mathrm{J}$ should be $-2532\ \mathrm{J}$ — wrong by a factor of five

Every one is logged with the correct form and the reasoning. **Revise from the corrected versions.**

## Using it with Claude

```bash
git clone <this-repo>
cd year-3-notes
claude          # or open the folder in Claude Desktop / Cowork
```

`CLAUDE.md` loads automatically and tells Claude how to navigate the knowledge bases, which errors
to correct silently, and how to teach from them. Then just ask:

> *"Tutor me through fluid statics"* · *"Quiz me on skin depth"* · *"Work through CAT 1 2025 with me"*

## Using it without Claude

Open any subject's `knowledge-base/00-index.md` and follow the coverage map. Each file is plain
Markdown with LaTeX maths — GitHub renders it directly.

Read `_verification-log.md` before revising a topic. It is the highest-value file in each subject.

## The source PDFs are not here

Lecture decks, handouts and textbooks are the lecturer's and publishers' material, not ours — this
repository carries only what we wrote. Each subject has a `sources/SOURCES.md` listing exactly which
files belong there and where to get them.

**Everything still works without them.** The knowledge bases are self-contained; you need the
originals only to check a citation against the original page.

## Before you use this

These are **unofficial student notes.** Nobody has endorsed, reviewed or approved them — not the
lecturers, not the university. They are a study aid, not a substitute for attending the course and
reading the source material.

- **Don't submit any of it as your own work.** Your institution's rules on collaboration, plagiarism
  and permitted materials apply to you, whatever you found here.
- **Don't treat a correction as authoritative.** The verification logs record errors believed to
  exist in the teaching material and give corrected forms. That analysis is careful and checked, but
  it is one student's. Where a mark depends on it, confirm against a standard textbook or ask your
  lecturer.
- **Check before an assessment.** Course content changes between cohorts. Anything here reflects the
  material as issued when it was written.

## What is deliberately left out

This repository is public, so four things are withheld on purpose. Please don't add them back.

- **Lecturer names and contact details.** Every file says `lecturer: "withheld"`. The verification
  logs record errors in the *teaching material*, and that is a claim about a document — naming an
  individual alongside it makes it a claim about a person. Citations point at the slide or page,
  which is more useful anyway.
- **Third-party figures** — textbook scans, web diagrams, stock photos. Where one has been removed
  from a study guide, a caption describes what it showed. The hand-drawn SVG figures are unaffected.
- **Scans of examination papers.** The past-paper questions are transcribed to Markdown and worked
  through; the photographed papers themselves are not here.
- **Anything personal**, which lives in the untracked `_personal/`.

`docs/kb-format.md` states these as rules for anyone adding a subject.

## Layout

```
├── CLAUDE.md                    # how to operate the knowledge bases
├── docs/
│   ├── kb-format.md             # the format spec — read before adding a subject
│   ├── tutoring-style-prompt.md # portable: paste into any tutoring session
│   ├── presentation-style-prompt.md
│   └── study-assistant-instructions.md
├── fluid-flow/
│   ├── knowledge-base/          # 11 topic files + nomenclature, formulas, log
│   │   └── past-papers/         # transcribed CATs + redrawn SVG figures
│   ├── study-guides/            # human-facing interactive HTML
│   └── sources/SOURCES.md       # manifest (files themselves untracked)
└── electromagnetic-fields/
    ├── knowledge-base/
    │   └── _reference-old-cohort/   # previous cohort — reference only
    └── sources/SOURCES.md
└── thermodynamics/
    ├── knowledge-base/          # 7 topic files + nomenclature, formulas, log
    │   └── exercises/           # assessed group activities — questions only
    └── sources/SOURCES.md
```

## Portable prompts

Two files in `docs/` are subject-agnostic and work anywhere, with or without this repository:

- [`tutoring-style-prompt.md`](docs/tutoring-style-prompt.md) — paste at the start of any tutoring
  session, on any subject. Sets pacing, worked-example emphasis, and the no-auto-advance rule.
- [`presentation-style-prompt.md`](docs/presentation-style-prompt.md) — formatting only. LaTeX
  rules, symbol definitions, diagram-first.

## Contributing

Fixing an error, or adding a subject? Read [`docs/kb-format.md`](docs/kb-format.md) first — it
specifies the file structure, the tag vocabulary, and the citation format. Consistency is what makes
the whole thing usable.

If you spot an error **in the knowledge base itself** (as opposed to in the source material), that's
the most valuable possible contribution. Open an issue.

Two things will be rejected on sight: adding a lecturer's name or contact details, and adding a
third-party image or an exam-paper scan. See *What is deliberately left out* above.

## Licence

[CC BY-NC-SA 4.0](LICENSE) — share and adapt freely for non-commercial use, with attribution, under
the same terms.

This covers **our** work: the transcription, organisation, error analysis and study guides. It does
not and cannot cover the underlying lecture content, which remains the lecturers' and the
university's.

---

<sub>Compiled by Jotham-JS · 2026</sub>
