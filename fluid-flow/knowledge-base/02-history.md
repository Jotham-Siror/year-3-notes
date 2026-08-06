---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "02 — History of Fluid Mechanics"
slides: "11-29"
file_role: topic
subtopics:
  - "hydraulics as early empirical science (irrigation, city water, canals)"
  - "ships and accumulated hydraulic knowledge"
  - "Leonardo da Vinci's contributions"
  - "hydrodynamics as theoretical science (Euler, inviscid theory)"
  - "Navier–Stokes and the reconciliation of theory with data"
  - "Kirchhoff (1869) linking hydraulics and hydrodynamics"
key_equations: []
prerequisites: []
leads_to: ["03-fluid-properties", "06-energy-bernoulli", "08-viscous-flow"]
verification_flags: 2
tags: [history, hydraulics, hydrodynamics, davinci, euler, navier-stokes, kirchhoff]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] def · [derivation] · [eq] · [ex] · [exercise] · [fig] figure · [hist] historical ·
  ·slide N = provenance · ⚠ VERIFY = flagged suspected slide error (see _verification-log.md). -->

# 02 — History of Fluid Mechanics

Narrative/background section (no equations). Two threads: **hydraulics** (empirical, practice-first) and
**hydrodynamics** (theory-first), which diverged for centuries and were reconciled in the 19th century. Useful
context for why the course reintroduces empirical coefficients (C, Cd, Cv…) on top of ideal-flow theory.

## Hydraulics — the empirical science ·slides 12–17
- [hist] Prehistoric humans shifted from hunter-gatherers to settled farming communities, creating a need for a
  steady water supply and transport of food/materials. ·slide 12
- Solution: water channels and ships → the birth of **hydraulics**. Evidence: irrigation-canal relics in Egypt
  and Mesopotamia, more than 4000 years BC. ·slide 13
- City water: may have begun in **Jerusalem** (a storage reservoir + masonry guide channel). Canals also built in
  Greece; the **Romans** built channels across the Empire (some still visible). ·slides 14–15
- City systems guided water from afar to fountains and public buildings; citizens fetched from supply stations.
  Usage then ≈ **180 L/capita/day**; now ≈ **240 L/capita/day**. ·slide 16
- Designing conduit shape/size and adjusting inclination or supply pressure to overcome wall friction drove much
  invention. ·slide 17

## Ships ·slides 18–19
- [hist] Ship origin unclear: likely log → raft; manual propulsion → sails; rivers → ocean navigation. ·slide 18
- Phoenicians and Egyptians built large ships dating even before **2700 BC**; the Greeks also left records.
  Shipbuilding and navigation accumulated much fundamental hydraulic knowledge. ·slide 19

## Leonardo da Vinci ·slides 20–25
- [hist] Renaissance polymath — splendid artist and excellent scientist. ·slides 20–22
  > ⚠ VERIFY ·slide 21 — slide gives "14th April 1452 – 2nd May 1514". Correct dates: **born 15 April 1452,
  > died 2 May 1519** (both the birth day and the death year are wrong on the slide). See _verification-log.md.
- Before Newton's gravity, stated "a body tries to drop to earth by the shortest path"; and (action–reaction)
  "a body gives air the same force as the resistance which air gives the body." ·slides 22–23
- Described water motion: eddies, waves, falling water, destructive force, floating bodies, efflux, flow in
  conduits and hydraulic machinery. ·slide 23
- First to identify the least-resistive **"streamline" shape**; foresaw drag and jet/falling-water laws later
  formalized by others; advocated **flow visualization** by floating particles in water. ·slides 24–25

## Hydrodynamics — the theoretical science ·slides 26–29
- [hist] From the 18th century (Euler et al.): complete theoretical equations for **non-viscous (frictionless)
  fluid** flow. But computed results diverged from experiment, so hydrodynamics was long thought impractical. ·slide 26
- **19th century — Navier & Stokes**: derivation of the equation of motion for a *viscous* fluid finally matched
  data. Analytical solutions remained hard, obtainable only for special flows (laminar flow between parallel
  plates, and in a round tube). ·slides 27–28 *(full derivation in 08-viscous-flow)*
- **1869 — Kirchhoff**: paper connecting hydraulics and hydrodynamics; computed the contraction coefficient for a
  jet from a 2-D orifice as **0.611** (experimental ≈ 0.60). From then the two fields advanced together. ·slide 29
  *(0.611 = π/(π+2), the classical free-streamline result — verified correct.)*
  > ⚠ VERIFY ·slide 29 — slide prints "Kirchoff"; correct spelling **Kirchhoff** (Gustav Kirchhoff). Minor. See log.

### Verification notes for this section
- 2 flags logged: da Vinci dates (slide 21), Kirchhoff spelling (slide 29).
- Kirchhoff's 0.611 contraction coefficient and the Egypt/Mesopotamia >4000 BC irrigation claim are consistent
  with standard history — not flagged.

---

<sub><i>Compiled by Jotham-JS · 2026</i></sub>
