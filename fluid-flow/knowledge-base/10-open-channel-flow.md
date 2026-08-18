---
kb: "MEC 3104 Fluid Theory"
lecturer: "withheld"
section: "10 — Flow in Open Channels"
slides: "479-519"
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
key_equations: [uniform-flow, chezy, manning, discharge-oc, best-section, specific-energy, critical-depth, froude, hydraulic-jump]
prerequisites: ["06-energy-bernoulli", "09-pipe-flow (hydraulic diameter, friction)"]
leads_to: []
verification_flags: 1
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

## 10.1 Uniform flow — force balance ·slides 480–485
- [def] Open channel = stream with a free surface open to air. Roman aqueducts reached 578 km total. ·slide 480
- [derivation] For constant depth & velocity down a slope, hydrostatic end-forces cancel, so the gravity
  component along the flow balances wall friction: $\rho g\,A\,l\sin\theta = \tau_0\,s\,l$. ·slides 482–485
- [eq: uniform-flow] With small slope $i = \tan\theta \approx \sin\theta$ and $m = A/s$ (hydraulic mean depth):
  $$\tau_0 = \rho g\,\frac{A}{s}\,i = \rho g\,m\,i$$

## 10.2 Chézy & Manning formulas ·slides 486–488
- [derivation] With friction coefficient $f = \lambda/4$ and $\tau_0 = f\rho v^2/2$: $v = \sqrt{2gmi/f}$, i.e.
  $v \propto \sqrt{mi}$. ·slide 486
- [eq: chezy] **Chézy's formula:**
  $$\boxed{\,v = c\sqrt{mi}\,}\qquad (c = \text{Chézy coefficient})$$
  Coefficient forms ·slide 486:
  - **Ganguillet–Kutter:** $c = \dfrac{23 + \frac1n + \dfrac{0.00155}{i}}{1 + \big(23 + \dfrac{0.00155}{i}\big)\dfrac{n}{\sqrt m}}$
  - **Bazin:** $c = \dfrac{87}{1 + \alpha/\sqrt{m}}$
  - **Manning:** $v = \dfrac1n\,m^{2/3}\,i^{1/2}$ (SI); $v = \dfrac{1.486}{n}\,m^{2/3}\,i^{1/2}$ (BG/ft units).
    n = roughness coefficient (tabulated by wall condition, slide 487).
- [eq: discharge-oc] Discharge: $Q = A v = A c\sqrt{mi} = \dfrac1n A\,m^{2/3}\,i^{1/2}$. Velocity is non-uniform:
  max at 10–40 % depth below the surface, mean v at 50–70 % depth. ·slide 488

## 10.3 Best (most efficient) section ·slides 489, 496
- [def] For fixed area A (and fixed c, i), $v$ and $Q$ are **maximized by minimizing the wetted perimeter s**.
  A **circle** has the least perimeter for a given area ⇒ the round channel is the most efficient. ·slide 489
- [eq: best-section] Rectangular channel: $s = B + 2H = A/H + 2H$; $ds/dH = 0 \Rightarrow A = 2H^2$, i.e.
  $\boxed{H/B = 1/2}$ — optimal depth is half the width. ·slide 496

## 10.4 Circular channel — partial-flow relations ·slides 490–495
- [eq] For a round channel radius $r$ filled to a subtended angle θ:
  $A = \dfrac{r^2(\theta - \sin\theta)}{2}$, $s = r\theta$, $m = \dfrac{r}{2}\Big(1 - \dfrac{\sin\theta}{\theta}\Big)$. ·slide 490
  $$\frac{v}{v_{full}} = \Big(1-\frac{\sin\theta}{\theta}\Big)^{2/3},\qquad
  \frac{Q}{Q_{full}} = \frac{\theta}{2\pi}\Big(1-\frac{\sin\theta}{\theta}\Big)^{5/3}$$ ·slides 491–492
- [ex ·slides 493–495] 24-in cast-iron pipe, slope 1/400, depth 5.6 in, n = 0.012:
  half-angle arccos(6.4/12)=57.77°; A = 80.23 in², wetted perimeter 24.20 in, m = 0.2763 ft;
  $v = \frac{1.486}{0.012}(0.2763)^{2/3}(1/400)^{1/2} = 2.63$ ft/s; **Q = 1.46 cfs**. ✓
  > ⚠ VERIFY ·slide 493 — problem statement prints "n = 0.12"; the worked solution (slide 495) correctly uses
  > **n = 0.012** (concrete). "0.12" is a typo (10× too large). See _verification-log.md.

## 10.5 Cross-section geometry example ·slides 497–498
- [ex] Area / wetted perimeter / hydraulic radius m: (a) semicircle d=4 m → A=6.283, s=6.283, m=**1.000** m;
  (b) rectangle 5×2.5 → A=12.5, s=10, m=**1.25** m; (c) trapezoid → A=7.44, s=8.394, m=**0.886** m. ✓

## 10.6 Specific energy & critical depth ·slides 499–507
- [eq: specific-energy] Energy per unit weight relative to the channel bottom: ·slides 499–500
  $$E = h + \frac{v^2}{2g} = h + \frac{Q^2}{2gA^2}$$
  (three variables E, h, Q; fix one to relate the other two.)
- [derivation] **Constant Q**: minimum-energy (critical) point where $dE/dh = 0$, giving $dA/dh = gA^3/Q^2$. With
  free-surface width B ($dA = B\,dh$): ·slides 501–502
- [eq: critical-depth] Critical conditions:
  $$Q^2 = \frac{gA_c^3}{B},\quad A_c = \Big(\frac{BQ^2}{g}\Big)^{1/3},\quad v_c = \frac{Q}{A_c} = \sqrt{\frac{gA_c}{B}}$$
  **Rectangular channel** (discharge per unit width q = Q/B): ·slide 503
  $$\boxed{\,h_c = \Big(\frac{q^2}{g}\Big)^{1/3},\qquad E_c = 1.5\,h_c,\qquad v_c = \sqrt{g h_c}\,}$$
- [ex ·slides 506–507] 10-ft channel, 180 cfs: $h_c = ((18)^2/32.2)^{1/3} = 2.16$ ft; $v_c = \sqrt{32.2\cdot2.16}
  = 8.34$ ft/s. ✓

## 10.7 Subcritical vs supercritical flow ·slides 504–511
- [def] Critical velocity equals the small-depth (long) wave speed $a = \sqrt{gh}$. ·slide 504
  - deeper than $h_c$ ⇒ $v < a$ ⇒ **tranquil / subcritical** flow;
  - shallower than $h_c$ ⇒ $v > a$ ⇒ **rapid / supercritical** flow. ·slides 504–505
- [eq: froude] **Froude number** $Fr = \dfrac{v}{\sqrt{gh}}$: $Fr<1$ tranquil, $Fr>1$ rapid — the open-channel
  analogue of subsonic/supersonic gas flow. ·slide 514
- [ex ·slides 510–511] 30-ft channel, 270 cfs, 3.0 ft deep: v=3.0 ft/s, E=**3.14 ft**; $h_c=1.36$ ft < 3.0 ft ⇒
  **subcritical**. ✓
- [note ·slides 508–509] Constant-E and constant-h plots both show the critical point at $E/h = 1.5$ (i.e. E_c=1.5h_c).

## 10.8 Hydraulic jump ·slides 512–519
- [def] A **hydraulic jump** occurs when unstable rapid (supercritical) flow abruptly decelerates to tranquil
  (subcritical) flow — e.g. a steep dam apron meeting a gentle downstream bed. It **dissipates energy**,
  protecting the downstream bed from erosion. ·slides 512–515
- [ex ·slides 516–517] Fixed mass flow: $Fr \propto h^{-3/2}$; reducing depth by ¾ raises Fr by
  $(3/4)^{-3/2} = (4/3)^{3/2} = 1.54\times$. ✓
- [ex ·slides 518–519] 10-ft channel (n=0.014), 340 cfs, slope break 0.0016→0.0150: $h_c = 3.30$ ft; normal
  depth upstream $h_n = 4.50$ ft (>h_c ⇒ **subcritical**), downstream $h_n = 2.04$ ft (<h_c ⇒ **supercritical**)
  — the depth passes through critical, so a **drawdown** occurs at the break, NOT a hydraulic jump (a jump is supercritical→subcritical, the opposite transition; slide 519 concludes only "subcritical before, supercritical after"). ⚠ KB-FIX 2026-08-03. ✓ (uses Manning with $m = 10h_n/(10+2h_n)$.)

### Cross-references
- Uses the energy equation (**06**) and hydraulic radius / friction ideas from **09-pipe-flow**.
- Weir discharge (over a channel) is derived in **06-energy-bernoulli** §6.9.

### Verification notes for this section
- Verified correct: uniform-flow τ₀=ρgmi; Chézy v=c√(mi); Manning; circular partial-flow relations; specific
  energy; critical depth $h_c=(q^2/g)^{1/3}$, $E_c=1.5h_c$, $v_c=\sqrt{gh_c}$; Froude relations; all worked
  examples (Q=1.46 cfs; h_c=2.16/1.36/3.30 ft; E=3.14 ft; Fr factor 1.54; h_n 4.50/2.04 ft).
- 1 typo logged: slide 493 n=0.12 → 0.012 (solution uses 0.012). Bazin shown in standard √m (hydraulic-radius) form.

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
