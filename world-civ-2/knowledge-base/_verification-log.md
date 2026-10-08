---
kb: "World Civilization II"
lecturer: "withheld"
file_role: verification-log
sources_audited: "FR pp.1-9 (complete); RNW ¶2-12 (complete); NW ¶2-14 (complete)"
substantive: 7
cosmetic: 25
discrepancies: 4
tags: [verification, errata, corrections]
---

<!-- Compiled by Jotham-JS, 2026. World Civilization II knowledge base. -->

# Verification log — World Civilization II

Every defect found in the source material, with **what the page prints**, **what it should be**, and **why**.
Nothing is silently corrected in the topic files: each entry is flagged inline at the point of use with
`⚠ VERIFY` and recorded here, so that the printed version is still recognisable if it appears in a tutorial
or an examination paper.

## Prefixes used in this subject

| Prefix | Means | A defect? |
|---|---|---|
| `V1`, `V2`, … | **substantive** error — changes a fact, a date, a sequence or a causal claim | yes |
| `C1`, `C2`, … | **cosmetic** error — typo, misspelling, garbled word, loose approximation | yes, harmless once seen |
| `D1`, `D2`, … | **cross-source discrepancy** — the two reference articles disagree | **no**, not by itself |

`D` is added for this subject because it has two overlapping secondary sources; it is not used elsewhere in
the repository. A `D` entry means the sources conflict, not that either is wrong — where one of them *is*
wrong, that is recorded as a `V` and cross-referenced. No `P` entries: there are no past papers yet. No `L`
entries: every source is digital text, nothing was read from a scan.

**Method.** The lecture handout was converted twice and independently — once with LibreOffice to plain text
and PDF, once by parsing the raw RTF control words — and the two extractions were compared before any topic
file was written, so nothing was lost in conversion. Page numbers were taken from the PDF render, so they are
the document's own printed pages. Every date, name, treaty and battle in all three documents was checked
individually.

---

## § Substantive errors

### V1 — France declared war on Austria alone, not on "Prussia and Austria" ·FR p9

- **Printed:** "In April 1792, France declared war against Prussia and Austria to forestall foreign
  intervention."
- **Should be:** France declared war on **20 April 1792 against Austria alone** — formally against "the King
  of Hungary and Bohemia". **Prussia entered afterwards**, in the following weeks, as Austria's ally under
  their defensive alliance of February 1792.
- **Why it matters:** the whole point of the passage is that France struck first to forestall a coalition.
  Naming both powers as the target erases the sequence — France split them, and then Prussia joined anyway.
  Also note that the reference article gets this right by saying only "France declared war in April 1792"
  ·RNW ¶4, so the knowledge base has an internal cross-check.
- **Used in:** `01` §1.5.5.

### V2 — the Tennis Court Oath: wrong name, wrong date, wrong order ·FR p3

- **Printed:** the deputies rejected the king's orders of 23 June "in the famous Tennis court resolution",
  deciding "to adjourn until a new constitution was drawn up" — placing the episode **after** the royal
  session of 23 June.
- **Should be:** the **Tennis Court Oath** (Serment du Jeu de Paume) was sworn on **20 June 1789**, three
  days *before* the royal session. The deputies, locked out of their hall, swore not to separate until a
  constitution was established. The defiance at the royal session of **23 June** is a **separate** episode.
- **Why it matters:** as printed, the Oath becomes a *response* to the king's dissolution order. It was not —
  it came first, and the king's session was the response to *it*. The causal direction is reversed, and the
  Oath is the single most cited moment of June 1789.
- **Also:** "resolution" for **Oath**. The deputies swore; they did not pass a motion.
- **Used in:** `01` §1.2.4.

### V3 — "costly but successful" contradicts the same sentence ·FR p2

- **Printed:** "During the 18th century, France pursued a costly but successful foreign policy. The country
  fought and lost the Austrian war of Succession (1740-48) and the Seven Years War (1756-63)."
- **Should be:** costly and **unsuccessful**. The second sentence contradicts the first.
- **Additionally:** the **War of the Austrian Succession was not a French defeat** in the way the Seven Years
  War was. It ended at **Aix-la-Chapelle (1748)** with conquests mutually restored — expensive and fruitless
  for France rather than lost. The **Seven Years War** genuinely was a defeat, costing France most of its
  North American and Indian possessions at the **Treaty of Paris (1763)**.
- **Why it matters:** the paragraph is building towards the debt that caused the financial crisis. "Costly
  and fruitless" makes that argument; "successful" undercuts it.
- **Used in:** `01` §1.2.3.

### V4 — the clergy crossed on 19 June, two days later ·FR p3

- **Printed:** "On 17th June 1789, the Third Estate seized political initiative by constituting itself into
  the National Assembly … and invited the first two orders to join them. **This day later**, the majority of
  the clergy voted to join them."
- **Should be:** **two days later — 19 June 1789** — a majority of the clergy voted to join.
- **Why it matters:** "This day later" is unreadable, and a reader repairing it silently will guess "the same
  day" or "the next day". The interval is the fact: the Third Estate acted alone for two days, which is what
  made the clergy's crossing decisive rather than simultaneous.
- **Used in:** `01` §1.2.4.

### V5 — Waterloo was fought on 18 June 1815 ·RNW ¶12

- **Printed:** "Napoleon's final defeat at Waterloo on **June 16-18, 1815**".
- **Should be:** the **Battle of Waterloo was fought on 18 June 1815**. **16 June** was **Ligny** (Napoleon
  against Blücher) and **Quatre Bras** (Ney against Wellington) — two different battles, at two different
  places, two days earlier.
- **Why it matters:** the range describes the **campaign**, not the battle, and a date question expects the
  battle. The other source avoids the problem by saying only "June 1815" ·NW ¶6 — see **D4**.
- **Used in:** `02` §2.5.

### V6 — the Parthenopean Republic was at Naples, not in Piedmont ·RNW ¶8

- **Printed:** French forces "established republican regimes in Rome, Switzerland (the Helvetic Republic),
  and the Italian Piedmont (**the Parthenopean**)".
- **Should be:** the **Parthenopean Republic** was the French client state at **Naples**, proclaimed in
  **January 1799** and suppressed in **June 1799**. The client state in **Piedmont** was the **Subalpine
  Republic**. Parthenope is the ancient Greek name for Naples, which is the check you can repeat.
- **Why it matters:** it relocates a real republic from the far south of Italy to the far north-west, and the
  north/south distinction matters for the campaigns of 1796-1800.
- **Used in:** `02` §2.3.

### V7 — "no Europe-wide conflict between 1815 and 1914" overstates ·NW ¶7

- **Printed:** "Not until a century later, when World War I started in 1914, would another Europe-wide
  military conflict break out."
- **Should be:** the **Crimean War (1853-56)** set **Britain, France, Sardinia and the Ottoman Empire against
  Russia**; the wars of **Italian unification (1859-71)** and **German unification (1864, 1866, 1870-71)**
  followed. The defensible version of the claim is that **no general war involving all the great powers**
  recurred until 1914.
- **Why it matters:** the sentence is being used to praise the Vienna settlement, and as printed it praises
  it for something it did not achieve. The accurate claim is still a strong one — Vienna prevented a
  *general* war for ninety-nine years — and is the one to make in an essay.
- **Used in:** `02` §2.6.

---

## § Cosmetic errors

### FR — the lecture handout

| ID | Page | Printed | Read |
|---|---|---|---|
| C1 | p1 | "advocated for political **eforms**" | reforms |
| C2 | p1 | "the ideas of **enlightment**" | the Enlightenment |
| C3 | p1 | "the **evens** of 1789" | events |
| C4 | p1 | "**Rosseau**" | Rousseau |
| C5 | p2 | "were weak **of** indecisive men" | weak **and** indecisive |
| C6 | p2 | "Louis XVI was incompetent, **negligible**" | negligent |
| C7 | p2 | "**Loius** XVI yielded" | Louis |
| C8 | p2 | "the **persons** and bourgeoisie were the most heavily taxes sections" | the **peasants** and bourgeoisie … most heavily **taxed** |
| C9 | p2 | "finance minister **Thurgot**" | **Turgot** (Anne Robert Jacques Turgot, Controller-General 1774-76) |
| C10 | p2 | "removal of aristocratic **task** exemptions" | tax exemptions |
| C11 | p2, p4 | "decided to **convince** the Estates-General" (twice) | **convene** |
| C12 | p2 | "an **initiation** to revolution" | an **invitation** to revolution |
| C13 | p3 | "in what had been **caused** the bourgeois revolution" | **called** |
| C14 | p4 | "in order **put** forestall counter-revolution" | in order **to** forestall |
| C15 | p5 | "**By 1789**, King Louis XVI had reluctantly assumed the role of a constitutional monarch" | true in practice from 1789, but **in law only from the constitution of 1791**; read as a description of his de facto position |
| C16 | p5 | "initiated and **implanted** a series of revolutionary reforms" | implemented |
| C17 | p6 | "Power to declare war **r** make peace" | or |
| C18 | p6 | "**Power or** suspend or delay legislation" | Power **to** suspend |
| C19 | p8 | "**Limited** at home, Louis XVI attempted to flee" | **thwarted** / frustrated at home |
| C20 | p8 | "the revolutionary land settlement **of** disrupted the economy" | stray word — delete "of" |

**Additional typography, not individually numbered:** "A more **contentions questions**" (contentious
question, p3); "voting should **by** orders" (should **be** by orders, p3); "the peasants were on the alert
armed with guns" reads as a run-on across two clauses (p5); "their properties destroyed Houses were set on
fire" is missing a full stop (p5). None changes a fact.

### RNW and NW — the reference articles

| ID | Source | Printed | Read |
|---|---|---|---|
| C21 | RNW ¶4 | "the Revolutionary government declared a **levy en masse**" | **levée en masse** |
| C22 | RNW ¶8 | Trafalgar (October 1805) narrated **before** "In 1805 a Third Coalition formed" | the **Third Coalition formed in spring/summer 1805**, before Trafalgar; Ulm was fought days before the battle. Sequence as printed is inverted |
| C23 | RNW ¶11 | "used first in the **Peninsular Campaign of 1811** by the duke of Wellington" | the Peninsular War began in **1808**; Wellington's supply-and-attrition strategy dates from the **Lines of Torres Vedras, 1810**. 1811 is late |
| C24 | NW ¶6 | "the throne that had been lost by Louis XVI just **twenty years** earlier" | **22 years** — Louis XVI was deposed August-September 1792, and this passage is set in 1814. Approximation; do not quote the figure |
| C25 | NW ¶10 | "the liberal ideals … spread to his opponents **to**" | too |

---

## § Cross-source discrepancies

Neither article is wrong in these four; they frame the subject differently. Recorded so that the topic file
can present both rather than silently choosing.

### D1 — when the wars begin: 1792 or 1799

- `RNW ¶2` dates the wars **1792-1815** and treats them as one continuous conflict that starts as a
  revolutionary war and becomes a war of conquest.
- `NW ¶1` titles itself **"Napoleonic Wars (1799-1815)"** and begins at the Consulate.
- **Consequence:** the first framing makes Napoleon the Revolution's heir; the second makes him its
  replacement. Both are defensible; an essay should state which it is using.

### D2 — why the Russian campaign failed

- `RNW ¶11` credits **Russian strategy** — Barclay de Tolly and Bagration withdrawing along parallel lines,
  stretching French supply lines past breaking point, with Borodino settling nothing.
- `NW ¶5` credits **the winter**: "the terrible Russian winter decimated Napoleon's Grand Army."
- **Consequence:** the first is an argument about generalship, the second about weather. The first is the
  better answer and the second is the popular version worth correcting; note that `RNW` mentions the winter
  too, but as an aggravating factor during a retreat that was already forced.

### D3 — what Trafalgar meant

- `RNW ¶8`: it **ended the French threat to invade England**.
- `NW ¶3`: it was **"just about the only blemish"** on Napoleon's record in the decade.
- **Consequence:** complementary rather than contradictory — one measures the strategic effect, the other the
  reputational one. Using both makes a fuller answer.

### D4 — the date of Waterloo

- `RNW ¶12`: **"June 16-18, 1815"**.
- `NW ¶6`: **"June 1815"**, no day given.
- **Resolution:** the battle was **18 June 1815**. See **V5** — this is a discrepancy in which one source is
  wrong, so it is logged in both sections.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
