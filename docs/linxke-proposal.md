# linxke — platform proposal

**Status: proposal, awaiting a go-ahead. Nothing in this document has been built.**
Written 5 November 2026 against the repository as it stood that day. Every decision below is
made; the decision log in § 10 lists them so any one can be reversed individually.

---

## 1. Verdict

Yes, this can be built, and the hard part is already done. A notes platform lives or dies on
two things: whether it has content, and whether that content has a consistent shape that software
can rely on. This repository has both. The work is a web application around material that exists.

### What exists today

| | Count |
|---|---|
| Units | 8 (7 with a knowledge base; EMT 3201 has one paper only) |
| Topic files | 75, median 28 KB |
| Notes, total Markdown | 4.3 MB, roughly 1.1 million tokens |
| Past papers transcribed | 34 (5 fully solved, 3 partially solved, 26 questions only) |
| Papers, total Markdown | 0.8 MB |
| Redrawn SVG figures | 155 |
| Documented corrections to lecture material | over 700 |
| Interactive study guides | 3 |
| Content specification | `docs/kb-format.md`, YAML frontmatter on every file |

The frontmatter is the reason this is a short project rather than a long one. Every file already
declares its unit, role, source, section and flag count, so the whole corpus can be imported by a
script with no manual re-tagging. The format spec becomes the platform's content spec on day one.

### What is hard

1. **Past-paper PDFs are the university's copyright.** Hosting them is normal practice for student
   platforms and still carries exposure. § 6 makes the call and sets the conditions.
2. **Markdown versions of papers cannot be fully automated.** Text-layer PDFs extract cleanly;
   scanned or handwritten maths does not. The Markdown twin of a paper is a human artefact with a
   machine draft to start from, and the platform must make that workflow fast rather than pretend it
   is automatic.
3. **Unit codes collide.** One unit here is examined as EEE 3202, BEE 3102 and BEE 3101 across
   cohorts, and BEE 3102 is also the 2024 Digital Electronics code. A unit must be identified by
   name, with codes as dated aliases. Most student sites get this wrong and silently merge units.
4. **Cold start.** With one class of content it is a very good website, not a platform. It needs
   two or three other classes seeded before anyone outside Year 3 EEE has a reason to come back.
5. **Moderation scales with uploads.** Trust tiers (§ 6) keep the queue short.

### What I would not do

- Build a mobile app first. A fast, offline-capable website covers phones and costs a third as much.
- Build a chat tutor first. The reader, papers and upload flow are the platform; tutoring is a
  feature on top of it later.
- Use an off-the-shelf CMS or wiki. None of them can serve a Markdown twin of every page, show token
  counts, or model errata, and those are the point.

---

## 2. Brand

### Name

**linxke.** Always lowercase, in the wordmark, in the interface and in prose. Said *links-kay*.

The name reads as two parts. *linx* is links: notes linked to the papers that examine them, papers
linked to their solutions, students in one class linked to students in the next. *ke* is `.ke`, the
country the platform starts in. Rooted there, not limited to it.

- **Tagline:** *Every unit, linked.*
- **Site headline:** *Checked notes. Real papers. Worked solutions.*
- **The promise in one line:** material that has been checked before you revise from it.

### Voice

Plain, specific, student to student. The platform says *unsolved* when a paper is unsolved, shows
where every claim came from, and never writes like a university or a start-up. It uses the words
students use (CAT, past paper, unit, sat) and not the words a product team would invent.

### Wordmark and mark

- **Wordmark:** `linxke` set in Bricolage Grotesque ExtraBold, tight tracking, with the **x** in
  Marker red. Nothing else in the lockup.
- **Mark:** two chain links crossed into an **x**, one in Ink and one in Marker. It reads at
  favicon size and works as a single colour.
- **Rule:** the wordmark never gets a gradient, a shadow or a second colour.

### Colour

Named tokens. Light values first, dark values second.

| Token | Light | Dark | Used for |
|---|---|---|---|
| Paper | `#F6F7F3` | `#0F1418` | page background; a faint engineering-pad grid in the hero |
| Card | `#FFFFFF` | `#161C22` | panels, rows |
| Grid | `#DCE2D8` | `#27313A` | rules and borders (1 px, no shadows) |
| Ink | `#141B22` | `#E7ECE4` | text |
| Ink 2 | `#4A5560` | `#9AA6B0` | secondary text |
| **Marker** | `#D1313F` | `#FF5F6D` | the brand accent: the x, primary buttons, active tab. One place per screen |
| Highlighter | `#FFE07A` | `#4A3E0E` | token badges, selected states, search hits |
| Verified | `#1E8E5A` | `#46C38A` | solved, verified, approved |
| Flag | `#D97A12` | `#F3A24A` | errata callouts, pending review |

Marker is the red pen that made the 700 corrections. It is deliberately the only strong colour, and
it is rationed: one primary action per screen. The engineering-pad grid is the one piece of
decoration, and it only appears in the home hero.

Deliberately avoided: teal and blue gradients, cream with a serif, purple, and anything that
looks like every other education site.

### Type

| Role | Face | Why |
|---|---|---|
| Display | Bricolage Grotesque | characterful without being a joke; variable weight and optical size |
| Body and interface | IBM Plex Sans | built for dense technical reading; pairs with its own mono |
| Code, Markdown, unit codes, token counts | IBM Plex Mono | |
| Mathematics | KaTeX | renders the LaTeX already in every file, server side |

All free, all on Google Fonts. Reading width is capped at 68 characters. Radius is 4 px everywhere:
this is a document tool, and sharp corners read as one.

### Domain

`linxke.com` first choice, `linxke.co.ke` second, ideally both with one redirecting. Availability
has not been checked.

---

## 3. Product

### Who it is for

Students revising for a unit. First the Strathmore BSc Electrical and Electronics Engineering Year 3
class whose material is here, then any unit at any institution. They use it in two ways, and the
product treats both as first class: reading on a phone, often on mobile data, and feeding the
material to an AI assistant.

### The three objects

| Object | What it holds | Formats |
|---|---|---|
| **Notes** | a unit's knowledge base: topic files, nomenclature, formula sheet, errata log | Markdown |
| **Papers** | CATs, end-of-semester exams, assignments, tutorials, each dated | PDF and Markdown |
| **Solutions** | worked answers attached to a paper, with a status | PDF and Markdown |

A fourth, secondary object is **Guides**: the interactive HTML study guides, hosted as they are.

Every text object has a canonical Markdown version. Where a scan exists, the PDF sits beside it with
a toggle. Every Markdown view shows its approximate token count.

### Information architecture

Institution → Programme → Year and semester → **Unit**. The unit is the home page of everything.

Programme and year are browse filters, not URL segments, because one unit serves several
programmes: Fluid Flow (MEC 3104) is a mechanical unit that EEE students take. Codes redirect to
the unit they belong to for the cohort they were used in.

```
/                                                     search and browse
/strathmore                                           institution: programmes, units
/strathmore/electromagnetic-fields                    unit home, tabbed
/strathmore/eee3202                                   code alias → redirects to the unit
/strathmore/electromagnetic-fields/notes/01-wave-characteristics-1
/strathmore/electromagnetic-fields/notes/01-wave-characteristics-1.md     raw Markdown
/strathmore/electromagnetic-fields/papers/2025-08-13-cat1
/strathmore/electromagnetic-fields/papers/2025-08-13-cat1.pdf
/strathmore/electromagnetic-fields/papers/2025-08-13-cat1.md
/strathmore/electromagnetic-fields/papers/2025-08-13-cat1/solutions      (.pdf | .md)
/strathmore/electromagnetic-fields/errata
/strathmore/electromagnetic-fields/llms.txt                               index for AI clients
/strathmore/electromagnetic-fields/bundle.md                              the whole unit, one file
/upload   /me   /mod   /takedown   /llms.txt
```

### Key screens

**Home.** A search box is the hero: unit code, topic or paper. Under it, browse chips for the
institutions and programmes that have content, then unit cards showing topic, paper and correction
counts. A stat strip at the bottom shows the live totals.

**Unit.** Name, every code it has been examined under with the cohort beside each, institution and
programmes. Tabs: Notes, Papers, Guides, Errata, About. A right rail labelled *Use with AI* holds
the `llms.txt` link, the bundle download with its token count, and a copy button for the unit
header. A *Save offline* button stores the unit's Markdown in the browser.

**Topic reader.** Table of contents on the left. Mathematics rendered. Provenance chips (`·WC1 p8`)
inline. Every `⚠ VERIFY` becomes a callout showing what the source prints and the corrected form.
`[added]` material is badged. Top bar: *Copy as Markdown*, token count, *Flag an error*.

**Paper.** Title and date sat, marks, duration, question count, status chips. A segmented toggle,
PDF or Markdown, for the paper. Below it, *Solutions* with the same toggle and its own status line,
for example *solved · worked and numerically verified 2026-08-18 · not the lecturer's*. Errata for
the paper itself appear as callouts.

**Upload.** Three steps. *Where:* pick or create institution and unit. *What:* past paper,
solutions, notes or guide, with the fields that type needs. *Review:* a preview, a declaration, and
submit. A PDF upload offers a machine-drafted Markdown twin to edit before or after submission.

**Moderation.** A queue for the institution's moderators: preview, approve, request changes,
reject, with one-click checks for names and student numbers in the text layer.

### AI-first features

These are the reason the platform is not just a file host.

- Every page has a Markdown twin at the `.md` suffix, and answers `Accept: text/markdown`.
- `/llms.txt` at the root and per unit list every file with a token count.
- One-file bundles per unit, and later per programme-year, as `.md` and `.zip`.
- Token counts on every item, labelled approximate.
- *Copy for AI* copies the Markdown with a short header: unit, source, licence, and the one-line
  errata summary, so an assistant knows what it is holding.
- Phase 3: an MCP server and a public read API, so an assistant can search units and fetch a topic
  or paper directly instead of being pasted a file.

### Verification as a product feature

The errata log is the thing no other notes site has, so it becomes a first-class object rather than
a file. Every unit has an Errata tab. Every flag appears inline where it applies. Any signed-in
reader can *Flag an error*; it enters as pending, a moderator confirms it, and it appears. Unit cards
show the count. The existing prefix scheme (V substantive, C cosmetic, P paper, L scan limitation,
D cross-source discrepancy) is kept exactly as `docs/kb-format.md` defines it.

---

## 4. Content model

### Entities

| Entity | Key fields |
|---|---|
| Institution | slug, name, country |
| Programme | institution, slug, name, award |
| Unit | institution, slug, canonical name, description |
| Unit code | unit, code, cohort or year range, note (so EEE 3202 / BEE 3102 / BEE 3101 all resolve) |
| Offering | unit, programme, year, semester |
| Knowledge base | unit, source summary, coverage, flag total |
| Topic | knowledge base, order, slug, title, Markdown, frontmatter as JSON, token estimate |
| Paper | unit, type (CAT 1, CAT 2, CAT, exam, assignment, tutorial), date sat, marks, duration, code as printed, PDF key, Markdown, Markdown status (none, machine, human, verified) |
| Solution | paper, PDF key, Markdown, status (unsolved, partial, solved), verified on, author |
| Erratum | unit, target (topic or paper), prefix and ID, prints, correct, why, status (pending, confirmed, rejected) |
| Guide | unit, title, HTML key |
| User | id, display name, role (reader, contributor, trusted, moderator, admin), institution |
| Contribution | user, object, status (pending, approved, changes requested, rejected), reviewer, notes |
| Report | user, object, reason, status |

### linxke Markdown

The platform's content spec is `docs/kb-format.md` as it stands, renamed. Four frontmatter keys are
added so a file is self-describing outside this repository:

```yaml
linxke: 1
institution: strathmore
unit: electromagnetic-fields
licence: CC-BY-NC-SA-4.0
```

The paper filename convention, `CODE-TYPE-YYYY-MM-DD.md`, is kept and parsed on import. The tag
vocabulary (`[def]`, `[ex]`, `[added]`, `⚠ VERIFY`) and the provenance form (`·WC1 p7`) are what the
renderer turns into badges, callouts and chips. Nothing in the existing 181 files needs to change.

---

## 5. Architecture

### Stack

| Layer | Choice | Why this one |
|---|---|---|
| Application | Next.js 15, TypeScript, App Router | server-rendered Markdown, auth, API routes and static pages in one codebase; the framework Claude Code builds fastest |
| Hosting | Vercel | zero-config deploys and edge caching; free until the project is well past its first few thousand users |
| Database and auth | Supabase (Postgres, Auth, row-level security) | one vendor for data and sign-in; Google sign-in plus email magic link covers students |
| Files | Cloudflare R2 | S3-compatible object storage with no egress fees, which matters for PDFs; direct browser uploads via presigned URLs |
| Markdown rendering | remark and rehype, with KaTeX and three custom plugins | the plugins turn `⚠ VERIFY`, `[added]` and `·WC1 p7` into callouts, badges and chips |
| Search | Postgres full text (`tsvector` plus `pg_trgm`) | enough to tens of thousands of documents; Meilisearch if it ever is not |
| Background jobs | Supabase edge functions or a small worker on Fly.io | PDF text extraction, token counting, bundle building |
| Tokens | a local tokenizer, labelled approximate | no API call per page view |
| Analytics | Plausible or Umami, self-hostable | no cookies, no consent banner |

### Diagram

```
 browser ──► Next.js on Vercel ──► Postgres + Auth (Supabase)
                 │     ▲                 ▲
                 │     │                 │  import CLI reads this repository's
                 │     │                 │  frontmatter and loads it (Phase 1)
                 ▼     │                 │
            R2 object storage ◄── presigned upload ◄── contributor (Phase 2)
            (PDFs, bundles, guides)       │
                                          ▼
                              worker: pdftotext / OCR → Markdown draft,
                                      token counts, bundle rebuild
 AI client ──► /llms.txt, *.md, bundle.md (Phase 1) · MCP server + API (Phase 3)
```

### Pipelines

**Import, Phase 1.** A command-line tool reads this repository, validates every file against the
spec, and upserts units, topics, papers, solutions and errata into Postgres. It runs on every push to
`main`. This repository stays the maintainer's authoring environment; the platform is where people
read it.

**Upload, Phase 2.** The browser gets a presigned URL and sends the PDF straight to R2. A job
extracts the text layer with `pdftotext`; if the text density is low the file is treated as a scan
and OCR runs. The result is saved as a Markdown draft with status *machine*. The contributor edits it
in a web editor with live KaTeX preview, or skips it. Moderators see the PDF and the Markdown side
by side.

**Search.** Units, topics, paper questions and errata are indexed. A code query (`eee3202`) resolves
through the alias table before full-text search runs.

**Performance.** Markdown is rendered on the server and cached at the edge. A unit page should
transfer under 100 KB without the PDF. The whole corpus of notes is 4.3 MB, so *Save offline* for a
unit is a few hundred kilobytes. Figures are SVG. KaTeX CSS is inlined. The site is a progressive
web app so saved units open with no connection.

---

## 6. Policy decisions

These are the four that carry risk. They are decided here, and § 10 lists them for veto.

### Hosting past-paper PDFs

This reverses rule 4 of `docs/kb-format.md`, which exists because the repository is a public Git
history where nothing can be taken down. A platform can take things down, so the rule changes
there, under conditions:

1. A PDF is the **paper as set**. Never a marked script, never a scan with a student's name or
   number, never lecture notes or textbook pages.
2. **Downloading a PDF requires sign-in.** Reading the Markdown does not. This keeps bulk scraping
   out and makes every download attributable.
3. The uploader declares the paper carries no personal data; moderators spot-check the text layer
   for names and digit runs, as the repository already does before a push.
4. A **takedown page** with a response commitment of 72 hours, and a log of every notice.
5. Lecturer names stay withheld everywhere, as now.

The Markdown transcription remains the primary artefact. The PDF is there because students want
the paper as it looked.

### Licence

Notes, solutions, errata and guides contributed to linxke are published under **CC BY-NC-SA 4.0**,
matching this repository and protecting students' work from being resold by someone else.
Contributors additionally grant linxke a licence to host, display and transform their uploads (the
Markdown draft, the bundle). Past papers are not licensed by linxke; they are hosted under notice
and takedown with their copyright acknowledged on the page.

### Personal data

The rules in `docs/kb-format.md` § *What never gets committed* become platform policy: no lecturer
names or contact details, no third-party images, no student-identifying content. Sign-in collects an
email and a display name and nothing else. No advertising trackers.

### Trust tiers and moderation

| Role | Can |
|---|---|
| Reader | read everything, download Markdown, save offline |
| Contributor (signed in) | download PDFs, upload, flag errors; uploads enter a queue |
| Trusted (three approved uploads) | publish immediately, reviewed afterwards |
| Moderator (per institution) | approve, request changes, reject, confirm errata, handle reports |
| Admin | everything, plus institutions and roles |

### Sustainability

Notes, papers and solutions are free to read and will stay free; a paywall on contributed content
kills contribution. If the platform needs money later, the honest options are tools for tutors and
lecturers, sponsored units, or a tip jar for contributors. None of that is in scope now, and none of
it is decided.

---

## 7. Roadmap

### Phase 1 — Read (weeks 1 to 4)

Public site with the eight units here. Unit pages, topic reader with mathematics and errata
callouts, paper pages with Markdown, errata tab, search, `.md` twins, `llms.txt`, bundles, token
counts, dark mode, offline saving. No accounts. Content comes from this repository through the
import tool. Launch to the class.

*Done when:* every file in this repository is reachable at a stable URL, renders correctly on a
phone, and has a Markdown twin.

### Phase 2 — Contribute (weeks 5 to 10)

Sign-in. Upload flow for papers (PDF, optional Markdown), solutions, notes in linxke Markdown, and
guides. Machine-drafted Markdown from PDFs. Moderation queue, trust tiers, *Flag an error*, R2
storage, takedown page, contributor profiles. Open to every programme and year at Strathmore.

*Done when:* someone from another class has uploaded a paper and it is live without the
maintainer touching it.

### Phase 3 — Scale (months 3 to 6)

Any institution. Programme and year browsing. Web Markdown editor with live preview. Assisted
transcription for moderators, clearly labelled as a draft. MCP server and public read API. Bundles
per programme-year. Contributor reputation. Meilisearch if Postgres search is no longer enough.

*Done when:* a second institution has a unit with notes, papers and at least one solved paper.

### Later, not committed

A tutor mode that answers from a unit's knowledge base the way `CLAUDE.md` does here. Quiz
generation from past papers. Spaced repetition over formula sheets. A native app, only if the web
app's data shows a reason.

### Repository relationship

The platform gets its own repository, `linxke`. This one is unchanged: it is the first seed pack
and the maintainer's authoring environment, imported on every push. Over time the web upload flow
may replace it for new material; nothing forces that.

---

## 8. Costs

| Phase | Monthly, roughly | What is paid for |
|---|---|---|
| 1 | the domain only | Vercel, Supabase and R2 free tiers cover a site this size |
| 2 | under US$10 | R2 storage once PDFs are in; still inside free tiers otherwise |
| 3 | US$50 to 100 | paid tiers of the app host and database once traffic and storage grow |

Prices are list prices at the time of writing and should be checked before committing. Build
effort is the real cost: with Claude Code doing the implementation, Phase 1 is one to two focused
weeks, Phase 2 three to four, Phase 3 open-ended.

---

## 9. Risks

| Risk | Mitigation |
|---|---|
| Copyright complaint about a hosted paper | sign-in gated downloads, takedown page, 72-hour response, log; Markdown stays up |
| Markdown transcriptions of uploaded papers are poor | status badges (machine, human, verified) so nobody mistakes a draft for a checked file; the editor makes fixing fast |
| Units merged or duplicated across cohorts and programmes | identity by name, codes as dated aliases, offerings as a separate table |
| Nobody uploads | a *claim your unit* flow and a direct ask to two or three other classes before Phase 2 ships |
| Moderation backlog | trust tiers; trusted contributors publish first and are reviewed after |
| Low bandwidth users | server-rendered Markdown, SVG figures, PDFs on demand, offline saving |
| Scope creep into tutoring and apps | the roadmap commits only through Phase 3 |

---

## 10. Decision log

Every decision made in this document, so any one can be reversed on its own.

| # | Decision |
|---|---|
| 1 | Name: linxke, lowercase always, said *links-kay* |
| 2 | Tagline *Every unit, linked.*; headline *Checked notes. Real papers. Worked solutions.* |
| 3 | Marker red as the single accent; Paper, Ink and Grid neutrals; Highlighter yellow for tokens and selection |
| 4 | Bricolage Grotesque display, IBM Plex Sans body, IBM Plex Mono code, KaTeX maths |
| 5 | 4 px radius, 1 px rules, no shadows; engineering-pad grid only in the home hero |
| 6 | Domain linxke.com, fallback linxke.co.ke |
| 7 | Unit is the home object; identified by name; codes are dated aliases that redirect |
| 8 | Programme and year are filters, not URL segments |
| 9 | Every text page has a `.md` twin; `llms.txt` at root and per unit; one-file bundles; token counts everywhere |
| 10 | Errata are a first-class object with the existing V, C, P, L, D prefixes |
| 11 | Content spec is `docs/kb-format.md` plus four frontmatter keys |
| 12 | Stack: Next.js, Vercel, Supabase, Cloudflare R2, remark and rehype with KaTeX, Postgres search |
| 13 | Past-paper PDFs are hosted, downloads behind sign-in, takedown within 72 hours |
| 14 | Licence CC BY-NC-SA 4.0 for contributed work; papers under notice and takedown |
| 15 | No lecturer names, no third-party images, no student-identifying content, no trackers |
| 16 | Trust tiers: reader, contributor, trusted, moderator, admin |
| 17 | Free to read, no paywall on content; sustainability undecided and out of scope |
| 18 | Three phases: Read, Contribute, Scale; tutoring and apps deferred |
| 19 | Platform code in a new repository; this repository is the seed pack, imported on push |

---

## 11. Questions

None. Two things could not be looked up from here and neither changes the design: whether
`linxke.com` is available, and whether the scans behind the 34 transcribed papers are still kept
locally. If the scans are gone, Phase 1 ships papers as Markdown only and the PDFs arrive through
the Phase 2 upload flow.

## 12. When the go-ahead comes

1. Create the `linxke` repository and scaffold Next.js, Supabase and R2.
2. Write the content spec as `SPEC.md` from `docs/kb-format.md` plus the four keys.
3. Write the import tool and run it against this repository; fix anything the validator rejects.
4. Build the unit page and topic reader, including the three Markdown plugins and KaTeX.
5. Build paper pages, `.md` twins, `llms.txt`, bundles and token counts.
6. Search, dark mode, offline saving, deploy, launch Phase 1 to the class.
