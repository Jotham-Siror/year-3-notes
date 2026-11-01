---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "10 — Flow in Open Channels"
source: "MEC 3104 FLUID THEORY - newlypasted.pdf (561 pp., Oct 2026 edition)"
slides: "459-497"
file_role: topic
subtopics:
  - "open-channel flow; uniform flow force balance"
  - "Chézy formula; Ganguillet–Kutter, Bazin, Manning coefficients"
  - "discharge; best (most efficient) section shape"
  - "circular channel partial-flow relations"
  - "rectangular optimal section"
  - "specific energy; critical depth & critical velocity"
  - "subcritical (tranquil) vs supercritical (rapid) flow; Froude number"
  - "hydraulic jump"
  - "further problems: semicircular channel Q, tranquil-or-rapid check, minimum specific energy (new in the Oct 2026 edition)"
key_equations: [uniform-flow, chezy, manning, discharge-oc, best-section, specific-energy, critical-depth, min-specific-energy, froude, hydraulic-jump]
prerequisites: ["06-energy-bernoulli", "09-pipe-flow (hydraulic diameter, friction)"]
leads_to: []
verification_flags: 3   # slide 472 n=0.12 still printed + new S82–S83 (Oct 2026 edition); S28, S29 still printed; S27 dropped with old slide 495
tags: [open-channel, chezy, manning, hydraulic-radius, specific-energy, critical-depth, froude, subcritical, supercritical, hydraulic-jump, weir]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · [hist] · ·slide N provenance ·
  ⚠ VERIFY = flagged suspected slide error (see _verification-log.md).
  NOTE: m = A/s = hydraulic mean depth (= hydraulic radius R); i = bed slope = tan θ ≈ sin θ. -->

# 10 — Flow in Open Channels

Free-surface, gravity-driven flow (rivers, sewers, aqueducts). Because hydraulic radii are large, Re is large
and flow is turbulent with a roughly constant, roughness-set friction factor — hence empirical uniform-flow
formulas (Chézy/Manning) rather than Moody. Then energy methods give specific energy, critical depth, and the
subcritical/supercritical distinction, culminating in the hydraulic jump.

## 10.1 Uniform flow — force balance ·slides 459–464
- [def] Open channel = stream with a free surface open to air. Roman aqueducts reached 578 km total. ·slide 460
- [derivation] For constant depth & velocity down a slope, hydrostatic end-forces cancel, so the gravity
  component along the flow balances wall friction: $\rho g\,A\,l\sin\theta = \tau_0\,s\,l$. ·slides 462–464
- [eq: uniform-flow] With small slope $i = \tan\theta \approx \sin\theta$ and $m = A/s$ (hydraulic mean depth):
  $$\tau_0 = \rho g\,\frac{A}{s}\,i = \rho g\,m\,i$$

## 10.2 Chézy & Manning formulas ·slides 465–467
- [derivation] With friction coefficient $f = \lambda/4$ and $\tau_0 = f\rho v^2/2$: $v = \sqrt{2gmi/f}$, i.e.
  $v \propto \sqrt{mi}$. ·slide 465
- [eq: chezy] **Chézy's formula:**
  $$\boxed{\,v = c\sqrt{mi}\,}\qquad (c = \text{Chézy coefficient})$$
  Coefficient forms ·slide 465:
  - **Ganguillet–Kutter:** $c = \dfrac{23 + \frac1n + \dfrac{0.00155}{i}}{1 + \big(23 + \dfrac{0.00155}{i}\big)\dfrac{n}{\sqrt m}}$
  - **Bazin:** $c = \dfrac{87}{1 + \alpha/\sqrt{m}}$ *(slide 465 prints $\sqrt{mi}$ — S29, still printed in the
    Oct 2026 edition)*
  - **Manning:** $v = \dfrac1n\,m^{2/3}\,i^{1/2}$ (SI); $v = \dfrac{1.486}{n}\,m^{2/3}\,i^{1/2}$ (BG/ft units).
    n = roughness coefficient (tabulated by wall condition, slide 466).
- [eq: discharge-oc] Discharge: $Q = A v = A c\sqrt{mi} = \dfrac1n A\,m^{2/3}\,i^{1/2}$. Velocity is non-uniform:
  max at 10–40 % depth below the surface, mean v at 50–70 % depth. ·slide 467

## 10.3 Best (most efficient) section ·slides 468, 473
- [def] For fixed area A (and fixed c, i), $v$ and $Q$ are **maximized by minimizing the wetted perimeter s**.
  A **circle** has the least perimeter for a given area ⇒ the round channel is the most efficient. ·slide 468
- [eq: best-section] Rectangular channel: $s = B + 2H = A/H + 2H$; $ds/dH = 0 \Rightarrow A = 2H^2$, i.e.
  $\boxed{H/B = 1/2}$ — optimal depth is half the width. ·slide 473

## 10.4 Circular channel — partial-flow relations ·slides 469–472 (and old slides 494–495, not in the Oct 2026 edition)
- [eq] For a round channel radius $r$ filled to a subtended angle θ:
  $A = \dfrac{r^2(\theta - \sin\theta)}{2}$, $s = r\theta$, $m = \dfrac{r}{2}\Big(1 - \dfrac{\sin\theta}{\theta}\Big)$. ·slide 469
  $$\frac{v}{v_{full}} = \Big(1-\frac{\sin\theta}{\theta}\Big)^{2/3},\qquad
  \frac{Q}{Q_{full}} = \frac{\theta}{2\pi}\Big(1-\frac{\sin\theta}{\theta}\Big)^{5/3}$$ ·slides 470–471
- [ex ·slide 472 (solution: old slides 494–495, not in the Oct 2026 edition)] 24-in cast-iron pipe, slope 1/400,
  depth 5.6 in, n = 0.012: half-angle arccos(6.4/12)=57.77°; A = 80.23 in², wetted perimeter 24.20 in,
  m = 0.2763 ft; $v = \frac{1.486}{0.012}(0.2763)^{2/3}(1/400)^{1/2} = 2.63$ ft/s; **Q = 1.46 cfs**. ✓
  *(The Oct 2026 edition keeps only the question, on slide 472; the worked solution is gone. Old slide 495 also
  printed "m = 80.23/24.20 = 3.15 in" for 3.32 in — S27, dropped with the slide.)*
  > ⚠ VERIFY ·slide 472 — problem statement prints "n = 0.12"; the worked solution (old slide 495) correctly used
  > **n = 0.012** (concrete). "0.12" is a typo (10× too large). **Still printed in the Oct 2026 edition** — and with
  > the solution dropped, the wrong value is now the only one the deck shows. The new Problem 5 (slide 494) uses
  > n = 0.012 for finished concrete, which supports the correction. See _verification-log.md.

## 10.5 Cross-section geometry example ·slides 474–475
- [ex] Area / wetted perimeter / hydraulic radius m: (a) semicircle d=4 m → A=6.283, s=6.283, m=**1.000** m;
  (b) rectangle 5×2.5 → A=12.5, s=10, m=**1.25** m; (c) trapezoid → A=7.44, s=8.394, m=**0.886** m. ✓
  *(475(c) prints "s = 5.0 + [(1.2)(√2)] = 8.394 m"; 8.394 needs both sides, 5.0 + 2(1.2√2) — S28, still printed in
  the Oct 2026 edition, where the slide is titled "Solution (1)".)*
- [exercise ·slide 474] *(part 2 is new in the Oct 2026 edition; no solution given)* "Using the parameters of the
  channel in example 1, calculate the velocity and the flow rate in the pipes."
  - [added] Reading it as: Manning with Example 1's slope $i = 1/400$ and the corrected $n = 0.012$, applied to
    each section (a)–(c) above. The sections are in metres, so use the SI form:
    $$v = \frac{1}{n}\,m^{2/3}\,i^{1/2},\qquad Q = A\,v$$

    | Section | $m$ (m) | $v$ (m/s) | $Q$ (m³/s) |
    |---|---|---|---|
    | (a) semicircle | 1.000 | 4.17 | 26.2 |
    | (b) rectangle | 1.250 | 4.83 | 60.4 |
    | (c) trapezoid | 0.886 | 3.84 | 28.6 |

    *(Python-checked. With the printed n = 0.12, every v and Q is 10× smaller.)*
  > ⚠ VERIFY S82 ·slide 474 — ambiguous question. "The parameters of the channel in example 1" does not say which
  > (slope, n, or both); Example 1 is in feet but these sections are in metres; "in the pipes" for open sections;
  > and Example 1 prints the wrong n (0.12). The reading above is one defensible choice — confirm with the
  > lecturer before relying on it.

## 10.6 Specific energy & critical depth ·slides 476–484
- [eq: specific-energy] Energy per unit weight relative to the channel bottom: ·slides 476–477
  $$E = h + \frac{v^2}{2g} = h + \frac{Q^2}{2gA^2}$$
  (three variables E, h, Q; fix one to relate the other two.)
- [derivation] **Constant Q**: minimum-energy (critical) point where $dE/dh = 0$, giving $dA/dh = gA^3/Q^2$. With
  free-surface width B ($dA = B\,dh$): ·slides 478–479
- [eq: critical-depth] Critical conditions:
  $$Q^2 = \frac{gA_c^3}{B},\quad A_c = \Big(\frac{BQ^2}{g}\Big)^{1/3},\quad v_c = \frac{Q}{A_c} = \sqrt{\frac{gA_c}{B}}$$
  **Rectangular channel** (discharge per unit width q = Q/B): ·slide 480
  $$\boxed{\,h_c = \Big(\frac{q^2}{g}\Big)^{1/3},\qquad E_c = 1.5\,h_c,\qquad v_c = \sqrt{g h_c}\,}$$
- [ex ·slides 483–484] 10-ft channel, 180 cfs: $h_c = ((18)^2/32.2)^{1/3} = 2.16$ ft; $v_c = \sqrt{32.2\cdot2.16}
  = 8.34$ ft/s. ✓

## 10.7 Subcritical vs supercritical flow ·slides 481–488
- [def] Critical velocity equals the small-depth (long) wave speed $a = \sqrt{gh}$. ·slide 481
  - deeper than $h_c$ ⇒ $v < a$ ⇒ **tranquil / subcritical** flow;
  - shallower than $h_c$ ⇒ $v > a$ ⇒ **rapid / supercritical** flow. ·slides 481–482
- [eq: froude] **Froude number** $Fr = \dfrac{v}{\sqrt{gh}}$: $Fr<1$ tranquil, $Fr>1$ rapid — the open-channel
  analogue of subsonic/supersonic gas flow. ·slide 491
- [ex ·slides 487–488] 30-ft channel, 270 cfs, 3.0 ft deep: v=3.0 ft/s, E=**3.14 ft**; $h_c=1.36$ ft < 3.0 ft ⇒
  **subcritical**. ✓
- [note ·slides 485–486] Constant-E and constant-h plots both show the critical point at $E/h = 1.5$ (i.e. E_c=1.5h_c).

## 10.8 Hydraulic jump ·slides 489–492 (and old slides 516–519, not in the Oct 2026 edition)
- [def] A **hydraulic jump** occurs when unstable rapid (supercritical) flow abruptly decelerates to tranquil
  (subcritical) flow — e.g. a steep dam apron meeting a gentle downstream bed. It **dissipates energy**,
  protecting the downstream bed from erosion. ·slides 489–492
- [ex ·old slides 516–517] *(not in the Oct 2026 edition)* Fixed mass flow: $Fr \propto h^{-3/2}$; reducing depth by ¾ raises Fr by
  $(3/4)^{-3/2} = (4/3)^{3/2} = 1.54\times$. ✓
- [ex ·old slides 518–519] *(not in the Oct 2026 edition)* 10-ft channel (n=0.014), 340 cfs, slope break 0.0016→0.0150: $h_c = 3.30$ ft; normal
  depth upstream $h_n = 4.50$ ft (>h_c ⇒ **subcritical**), downstream $h_n = 2.04$ ft (<h_c ⇒ **supercritical**)
  — the depth passes through critical, so a **drawdown** occurs at the break, NOT a hydraulic jump (a jump is supercritical→subcritical, the opposite transition; old slide 519 concludes only "subcritical before, supercritical after"). ⚠ KB-FIX 2026-08-03. ✓ (uses Manning with $m = 10h_n/(10+2h_n)$.)

## 10.9 Further problems ·slides 493–497 (new in the Oct 2026 edition)
- [ex ·slides 493–494] **Problem 5 — semicircular channel.** Finished-concrete channel: a semicircular bottom of
  radius 10 ft with vertical sides, water surface 3 ft above the centre [fig ·493]; bed slope $i = 0.0016$. Find Q.
  - Flow area = half-circle + rectangle $3 \times 20$:
    $$A = \tfrac12\pi(10)^2 + 3(10+10) = 217.1\ \text{ft}^2$$
  - Wetted perimeter = semicircular arc + two 3-ft sides (the free surface is not wetted):
    $$m = \frac{A}{s} = \frac{217.1}{\pi(10) + 3 + 3} = 5.802\ \text{ft}$$
  - Manning, BG form, with $n = 0.012$ (finished concrete — introduced in the solution, not the question):
    $$Q = A\,\frac{1.486}{n}\,m^{2/3}\,i^{1/2} = 217.1\Big(\frac{1.486}{0.012}\Big)(5.802)^{2/3}(0.0016)^{1/2} = \mathbf{3472\ ft^3/s}$$
    ✓ *(Python: $A = 217.08$, $s = 37.42$, $m = 5.802$, $Q = 3471.8$ ft³/s; mean $v = 16.0$ ft/s.)*
- [exercise ·slide 495] **Problem 6 — tranquil or not?** Rectangular channel 50 ft wide, water 10 ft deep
  [fig ·495], average velocity 28.28 ft/s. Is the flow tranquil?
  - [added] Froude number (§10.7):
    $$Fr = \frac{v}{\sqrt{gh}} = \frac{28.28}{\sqrt{32.2 \times 10}} = \frac{28.28}{17.94} = 1.58 > 1$$
    ⇒ **rapid (supercritical), not tranquil.** The width does not enter.
  - [added] Cross-check by critical depth: $q = vh = 282.8$ ft²/s, so
    $$h_c = \Big(\frac{q^2}{g}\Big)^{1/3} = \Big(\frac{282.8^2}{32.2}\Big)^{1/3} = 13.54\ \text{ft} > 10\ \text{ft}$$
    — the flow is shallower than critical ⇒ rapid. ✓ *(Python-checked.)*
- [ex ·slides 496–497] **Example 7 — minimum specific energy.** 8-ft-wide channel, $Q = 150$ ft³/s.
  - Critical (minimum-E) condition, from §10.6 with $A_c = b\,h_c$ ($b$ = channel width):
    $$gA_c^3 = bQ^2 \;\Rightarrow\; (32.2)(8h_c)^3 = (8)(150)^2 \;\Rightarrow\; h_c = 2.218\ \text{ft}$$
  - [eq: min-specific-energy] Since $v_c^2 = gA_c/b$, the velocity head at critical is $A_c/(2b)$:
    $$E_{\min} = \frac{A_c}{2b} + h_c = \frac{8(2.218)}{2(8)} + 2.218 = \mathbf{3.327\ ft}$$
    — i.e. $E_{\min} = 1.5\,h_c$, as in §10.6. ✓ *(Python: $h_c = 2.2184$ ft, $E_{\min} = 3.3277$ ft.)*
  - Same data as MEC 3104 CAT 2 (7 Oct 2025), Q2(1)(a) — see `past-papers/MEC3104-CAT2-2025-10-07.md`.
  - *Rendering note: some PDF viewers drop the ³ and ² here and show "gA = bQ" and "(32.2)(8hc) = (8)(150)"; the
    text layer reads gA³ = bQ² and (32.2)(8hc)³ = (8)(150)².*
  > ⚠ VERIFY S83 ·slide 497 — cosmetic. "Emin = Ac/2b + hc" has no brackets; read as written it is
  > $(A_c/2)\,b$. It means $A_c/(2b)$ — the next line's arithmetic, 8(2.218)/[(2)(8)], confirms it. (The 2025 CAT
  > prints the same unbracketed form — erratum P29.)

### Cross-references
- Uses the energy equation (**06**) and hydraulic radius / friction ideas from **09-pipe-flow**.
- Weir discharge (over a channel) is derived in **06-energy-bernoulli** §6.9.

### Verification notes for this section
- Verified correct: uniform-flow τ₀=ρgmi; Chézy v=c√(mi); Manning; circular partial-flow relations; specific
  energy; critical depth $h_c=(q^2/g)^{1/3}$, $E_c=1.5h_c$, $v_c=\sqrt{gh_c}$; Froude relations; all worked
  examples (Q=1.46 cfs; h_c=2.16/1.36/3.30 ft; E=3.14 ft; Fr factor 1.54; h_n 4.50/2.04 ft) and the new ones
  (Q = 3472 ft³/s; h_c = 2.218 ft, E_min = 3.327 ft; Problem 6 Fr = 1.58).
- 1 typo logged: slide 472 n=0.12 → 0.012 — **still printed** in the Oct 2026 edition, which also drops the
  worked solution that showed 0.012. Bazin shown in standard √m (hydraulic-radius) form.
- Oct 2026 edition (rechecked on rendered pages 459–497): S28 (475) and S29 (465) **still printed**; S27 went
  with old slide 495 (not in the new edition). New flags S82 (474, ambiguous new part 2) and S83 (497, brackets).

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
