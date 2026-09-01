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
| [Electromagnetic Fields](electromagnetic-fields/knowledge-base/00-index.md) | EEE3202 | Lecture handouts, issued progressively | 1 handout, 43 flags, 1 past paper, 1 lab |
| [Thermodynamics](thermodynamics/knowledge-base/00-index.md) | MEC 3105 | 5 lecture documents (200 pp.) + assessed group activities | 7 topic files, 51 flags, both group activities |
| [Analogue Electronics I](analogue-electronics/knowledge-base/00-index.md) | BEE 3103 | Lecture notes (100 pp.) + 7 lesson documents (169 pp.) + 4 reference decks | 14 topic files, 388 flags, 3 tiers |
| [Digital Electronics II](digital-electronics/knowledge-base/00-index.md) | BEE 3102 | 6 chapter decks (348 slides) + excitation-table sheet | 10 topic files, 81 flags, 144 figures, 1 past paper |
| [Engineering Mathematics III](engineering-math/knowledge-base/00-index.md) | EMT 3101 | 6 topic documents (66 pp.) — one typeset, five handwritten scans | 6 topic files, 24 flags, 1 assignment |

## What this actually is

Each subject's lecture material has been transcribed into structured Markdown: every equation in
LaTeX, every claim anchored to the slide or page it came from, every figure described, and **every
suspected error in the original flagged and corrected**.

That last part is the reason this exists. Across the six subjects there are **637 documented
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
- BEE 3103, Lesson 2 p4: half-wave rectification efficiency printed as **409.6 %**. It is
  $4/\pi^{2} = 40.5\,\%$, and the correct decimal 0.406 sits on the line above it
- BEE 3103, Lesson 7 p11: $\beta$ means the feedback fraction and the transistor current gain within
  eight lines of each other — 0.02 versus 50, in equations that look identical
- BEE 3103, lecture notes p35: Boltzmann's constant printed as $1.38\times10^{-28}$ J/K, which puts
  the thermal voltage at 0.26 µV instead of 26 mV — caught because the *other* source has it right
- BEE 3102, Chapter 4 slide 44: the R/2R ladder transfer function is off by one in the exponent, so
  **every voltage the deck gives for that converter is half what the circuit produces** — slide 47's
  printed $-3.4375$ V should be $-6.875$ V, and the deck's own nodal analysis two slides earlier
  contradicts its formula
- BEE 3102, Chapter 3 slide 29: the Hamming syndrome for an error in bit 12 is printed $1000$, which
  is the code for bit 8 — the one property the whole scheme exists to provide
- EMT 3101, Bessel p2: the $-\nu$ is missing from the exponent of $J_{-\nu}$, so **every value the
  printed series produces is wrong** — 0.7029 instead of 1.0653 at $\nu = 0.3$, $x = 0.5$; the page's
  own line above it implies the missing term
- EMT 3101, Gamma and Beta printed p6: $\Gamma(9/2) = 16.8114$. It is **11.6317** — and the next line
  on the same page uses the correct value to reach $(4.5)! = 52.3428$

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
└── analogue-electronics/
    ├── knowledge-base/          # 14 topic files in 3 tiers + nomenclature, formulas, log
    │   └── _reference-decks.md  # 4 slide decks — mapped, not verified
    └── sources/SOURCES.md
└── digital-electronics/
    ├── knowledge-base/          # 10 topic files + nomenclature, formulas, log
    │   ├── figures/             # 142 redrawn SVGs
    │   ├── flags/               # per-file verification working
    │   └── past-papers/         # transcribed CATs, worked; figures redrawn
    └── sources/SOURCES.md
└── engineering-math/
    ├── knowledge-base/          # 6 topic files + nomenclature, formulas, log
    │   └── past-papers/         # transcribed assignment, worked
    └── sources/SOURCES.md       # (a local _transcripts/ layer sits beside the
                                 #  knowledge base, untracked — see SOURCES.md)
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

<sub>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</sub>
