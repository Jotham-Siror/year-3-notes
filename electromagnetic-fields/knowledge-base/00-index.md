---
kb: "Electromagnetic Fields — Year 3"
course_code: "EEE3202"
lecturer: "withheld"
file_role: index
source: "Current-cohort lecture handouts, issued progressively. 1 received so far (18 pp.)"
built: "Transcribed from rendered page images; equations in canonical LaTeX; suspected errors flagged inline and collected in _verification-log.md; both tutorial questions solved and numerically verified"
coverage: "18/18 pages of WC1 mapped, no gaps"
total_verification_flags: 43
---

# Electromagnetic Fields (EEE3202) — Knowledge Base Index

**What this is.** A verified map of the EEE3202 lecture handouts — every claim anchored to its
source page, every suspected error flagged and corrected. Start here, then open the topic file you
need rather than re-reading the raw PDFs.

**Status.** The course is delivered as a **series of handouts, released progressively**. One has
been issued so far. This index is the register — update it as each new handout arrives.

> **Operating instructions** (how to navigate and teach from this KB) live in `CLAUDE.md` at the
> project root, not in this file.

---

## Handout register

| Code | Handout | Pages | Received | Topic file |
|---|---|---|---|---|
| **WC1** | *Electromagnetic Wave Characteristics I* | 18 | ✅ | `01-wave-characteristics-1.md` |
| WC2 | *Electromagnetic Wave Characteristics II* (expected) | — | ⏳ not yet issued | — |

Provenance is cited as **·WC1 p7** in the topic files.

## How the files are organised

- **Topic files `01`, `02`, …** — **one file per handout**, in the order issued.
- **`_nomenclature.md`** — every symbol with meaning and SI units; resolves the notation clashes,
  which are severe in this subject.
- **`_formula-sheet.md`** — every equation in one place, each tagged to its source page, all in
  corrected form.
- **`_verification-log.md`** — every flagged handout error with the correct form and why.
- **`_reference-old-cohort/`** — the previous cohort's knowledge base. **Not authoritative.** See
  § Old-cohort reference below.
- **`../sources/`** — the raw handout PDFs. Not tracked; see `../sources/SOURCES.md`.

### Splitting rule

**One handout = one topic file.** Split a handout into `NNa` / `NNb` only when it covers **two
genuinely independent themes** *and* exceeds ~25 KB. Otherwise keep it whole.

WC1 was kept as one file despite covering six sections: it is a single continuous argument
(wave equation → plane wave → media → skin depth), each section leans on the one before, and its
tutorial questions span the whole thing.

## Tag legend

`[def]` definition · `[derivation]` step-by-step · `[eq]` key equation · `[ex]` worked example
(lecturer's numbers) · `[exercise]` unsolved problem set on the handout · `[fig]` figure described
from the rendered page · `[added]` supplied here, **not** in the handout · `·WC1 pN` provenance ·
`⚠ VERIFY` flagged suspected handout error.

---

## Coverage map

| File | Handout | Pages | Key content |
|---|---|---|---|
| `01-wave-characteristics-1.md` | WC1 | 1–18 | Maxwell → wave equation (general / conducting / dielectric / free space); uniform plane waves; d'Alembert solution; phasor form; E–H relationship and $\eta$; propagation constant $\gamma = \alpha + j\beta$; loss tangent and $\varepsilon^*$; lossy / perfect-dielectric / conductor cases; skin depth; 2 tutorial questions |

### Section map within WC1

| § | Pages | Content |
|---|---|---|
| 1 | 1–4 | The wave equation and its four specialisations |
| 2 | 4–6 | Uniform plane waves, 1-D reduction, d'Alembert, **Figure 1** |
| 3 | 6–7 | Sinusoidal / phasor form |
| 4 | 7–8 | E–H relationship, intrinsic impedance, $\eta_0 = 377\ \Omega$ |
| 5 | 8–11 | Propagation constant, derivation of $\alpha$ and $\beta$, general $\eta$ |
| 6 | 11–13 | Loss tangent, **Figure 2**, complex permittivity, classification |
| 7 | 13–17 | Plane waves in lossy / perfect-dielectric / conducting media |
| 8 | 17–18 | Depth of penetration and skin depth |
| 9 | 18 | Tutorial questions (solved and verified here) |

## Dependency / teaching order

Within WC1 the order is strictly sequential — §1 → §2 → §3 → §4 → §5 → §6 → §7 → §8. Nothing can be
taught out of order without forward references.

**Heaviest and most exam-relevant:** §5 (the $\alpha$/$\beta$ derivation) and §7 (the four media),
which is also where the handout's errors cluster. §8 is a short corollary of §7's good-conductor
case. §4 supplies the one number most likely to appear in a question, $\eta_0 = 377\ \Omega$.

---

## ⚠ Gap map — syllabus topics with no current-cohort handout

WC1's page 1 lists four learning objectives but delivers only three.

| Syllabus objective | Status | Interim source | Warning |
|---|---|---|---|
| i. Wave equation in different media | ✅ WC1 §1 | — | — |
| ii. Uniform plane wave and wave propagation | ✅ WC1 §2, §5 | — | — |
| iii. Characterization of conductors and dielectrics | ✅ WC1 §6, §7 | — | — |
| **iv. Types of polarization** | ❌ **absent from WC1** | `_reference-old-cohort/06-polarization.md` | **Axis convention differs — see below** |

### Using the polarization gap-filler

The old-cohort material covers linear, elliptical and circular polarization in complex notation.
It is usable, with two cautions:

1. **Axis convention.** The old polarization handout propagates along **$x$** with transverse
   components $(E_y, E_z)$. WC1 propagates along **$z$** with $(E_x, E_y)$. Same physics, different
   labels. **Teach in WC1's $z$-convention** and translate, rather than quoting the old axes.
2. **A known error in that file's source.** The old handout states circular polarization needs a
   **180°** phase difference; the correct condition — and its own mathematics — is **90°**. See
   `_reference-old-cohort/_verification-log.md`.

Flag clearly when teaching from this that it is **old-cohort material pending this year's handout**,
not this year's notes.

---

## Old-cohort reference

`_reference-old-cohort/` holds a complete knowledge base built from **three handouts belonging to a
previous cohort** (EMW 31 pp., UPW 16 pp., POL 4 pp. — same lecturer, same course).

**It is not authoritative.** Two legitimate uses only:

1. **Filling a gap** where this cohort's handout has not yet been issued (currently: polarization,
   Poynting vector, reflection and transmission).
2. **Cross-checking** a derivation that appears in both.

Anything taught from it must be labelled as such. When the corresponding current-cohort handout
arrives, the new topic file supersedes it.

**Where the two sets overlap**, the physics agrees — WC1's §1–§8 maps onto old files `01`–`04`. WC1
is the fuller and better-organised treatment of that ground.

---

## Verification summary — 43 flags

Full detail in `_verification-log.md`. **20 substantive** (V1–V20), **23 cosmetic** (C1–C23).

The physics is sound; the transcription is not. Two failure modes dominate:

**1 · A wrong constant.** WC1 p8 prints $\mu_0 = 4\pi\times10^{-12}$ H/m. It is
$4\pi\times10^{-7}$. With the printed value $\eta_0 = 1.19\ \Omega$ — not the 377 Ω on the very next
line — and $c = 9.49\times10^{10}$ m/s, some **317× the speed of light**. *(V1, re-computed.)*

**2 · A symbol collision.** $\sigma$ is the conductivity, but the handout also uses it for the
attenuation constant $\alpha$, corrupting **six equations** across pp. 9–11 and 16. In three of them
$\sigma$ appears on *both* sides, making the equation self-referential and unsolvable as printed.
*(V9, V12, V14, V15, V19.)*

Other substantive errors a learner should **not** absorb:

- **p5** — the Laplacian printed without its squares (V2)
- **p6** — harmonic Ampère's law as $j\omega\varepsilon E + j\omega\sigma E$; the conduction term is
  not time-differentiated (V3)
- **p6** — Figure 1's horizontal axis labelled $t$; it is $z$ (V8)
- **p1** — $\sigma$ replaced by $\varepsilon$ twice in the curl-of-curl step (V4)
- **pp. 2–4** — three boxed wave equations written for the identity's dummy vector $\bar{A}$ instead
  of $\bar{H}$ (V5)
- **p3** — $\rho_s$ for $\rho_v$, inside an invalid chain of equalities (V6)
- **p4** — plane-wave definition says fields are constant "across any chosen direction", which is
  false along the propagation direction (V7)
- **pp. 9, 10, 16** — missing brackets in $\alpha$ and $\beta$: the $\mp 1$ must sit inside, not
  outside (V10). *Invisible in the PDF text layer — only the rendered page shows it*
- **p11** — $|\eta|$ with $\sigma$ for $\sigma^2$ and $(j\omega\varepsilon)^2$ for
  $(\omega\varepsilon)^2$ (V16)
- **p12** — $\gamma^2$ written where $\gamma$ is meant (V17)
- **p15** — lossy phase velocity: $\omega$ cancelled from the denominator but left in the numerator
  (V18). *The line at the bottom of p14 is correct; only the version carried onto p15 is broken*
- **p16** — $\varepsilon^* \approx -j\omega/\sigma$; it is $-j\sigma/\omega$ (V20)

**Two habits worth teaching from this**, both of which catch these errors independently:

1. **Check dimensions before substituting.** $\alpha$ and $\beta$ are m⁻¹; $\sigma$ is S/m. Half the
   flagged errors fail a dimensional check on sight.
2. **Distrust any equation whose left-hand symbol also appears on the right.** That single test
   catches V15 and V19.

### Cross-cohort pattern

The old-cohort handouts carry the same class of defect — results that are $\beta$ labelled $\alpha$.
**Treat every $\alpha$/$\beta$/$\sigma$ label in propagation-constant material from this course as
suspect until dimensionally checked.** See `_verification-log.md` § D.

---

## Provenance notes

- All 18 pages were **rendered to images and read directly**. The PDF text layer mangles
  mathematics — V10 in particular is invisible without the render.
- Both figures (p6, p12) were legible at full resolution and are described in the topic file. No
  page currently requires a screenshot; if one ever does, it will be listed here.
- Both tutorial questions were solved and **numerically verified**. The solutions are tagged
  `[added]` — they are not the lecturer's.
- Nothing was invented. If a question needs content absent from the handouts, say so and ask rather
  than filling the gap.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
