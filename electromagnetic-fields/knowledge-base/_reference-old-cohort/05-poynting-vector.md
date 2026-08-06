---
kb: "Electromagnetic Fields — Year 3"
lecturer: "withheld"
section: "05 — The Poynting Vector & Energy"
source_pages: "EMW p17–23"
file_role: topic
subtopics:
  - "Poynting vector P = E × H (power flow per unit area)"
  - "Poynting theorem: derivation from Ampère's law + a vector identity"
  - "the three terms: source, ohmic dissipation, stored-energy rate"
  - "receiver vs transmitter interpretation"
  - "P normal to both E and H"
  - "average (time-mean) Poynting vector, Pav = ½ E₀²/η"
key_equations: [poynting-vector, poynting-theorem, poynting-average]
prerequisites: ["02-uniform-plane-wave (η)", "01-maxwell-wave-equations"]
leads_to: ["07-reflection-transmission"]
verification_flags: 0
tags: [poynting-vector, poynting-theorem, power-flow, energy-density, average-power, dissipation, stored-energy]
---

<!-- TAG LEGEND: [def] · [derivation] · [eq] · [ex] · [exercise] · [fig] · ·EMW/UPW/POL pN provenance ·
  ⚠ VERIFY = flagged suspected handout error (see _verification-log.md). -->

# 05 — The Poynting Vector & Energy Considerations

Scope: an EM wave carries energy. The **Poynting vector** P = E × H gives the power flowing per unit area and its
direction; **Poynting's theorem** is the energy-conservation bookkeeping (power in = dissipation + rate of stored
energy). Ends with the time-average power a plane wave delivers.

---

## 5.1 The Poynting vector ·EMW p17

[def] An EM wave carries energy as it travels. Through any imaginary surface in space there is a net power flow
per unit area. ·EMW p17

[eq: poynting-vector]
$$\boxed{\;\mathbf P = \mathbf E \times \mathbf H \quad (\text{W/m}^2)\;}$$
- $\mathbf P$ = **Poynting vector** (after John H. Poynting, 1884); its **direction is the direction of power
  flow**, and it is **perpendicular to both E and H**. ·EMW p17, p20
- Total power through a surface = $\displaystyle\oint \mathbf P\cdot d\mathbf s$.
- [fig ·EMW p20] For a wave with $E_y$ and $H_z$ propagating in +x: $E_y\mathbf a_y \times H_z\mathbf a_z =
  P_x\mathbf a_x$ — power flows along x, normal to both fields.

---

## 5.2 Poynting's theorem — derivation ·EMW p18–19

[derivation] Start from Ampère's law and dot both sides with E: ·EMW p18
$$\mathbf E\cdot(\nabla\times\mathbf H) = \mathbf E\cdot\!\left(\mathbf J_c + \frac{\partial\mathbf D}{\partial t}\right)$$
Use the **vector identity** $\nabla\cdot(\mathbf E\times\mathbf H) = \mathbf H\cdot(\nabla\times\mathbf E) - \mathbf E\cdot(\nabla\times\mathbf H)$
and Faraday's law $\nabla\times\mathbf E = -\mu\,\partial\mathbf H/\partial t$. With the energy-density identities
$$\varepsilon\mathbf E\cdot\frac{\partial\mathbf E}{\partial t} = \frac{\partial}{\partial t}\!\left(\frac{\varepsilon E^2}{2}\right),\qquad
  \mu\mathbf H\cdot\frac{\partial\mathbf H}{\partial t} = \frac{\partial}{\partial t}\!\left(\frac{\mu H^2}{2}\right)$$
one obtains, after integrating over a volume and applying the divergence theorem: ·EMW p18–19

[eq: poynting-theorem]
$$\boxed{\;-\oint(\mathbf E\times\mathbf H)\cdot d\mathbf s = \int \mathbf E\cdot\mathbf J_c\,dv
   + \int \frac{\partial}{\partial t}\!\left(\frac{\varepsilon E^2}{2} + \frac{\mu H^2}{2}\right)dv\;}$$

[def] Reading the three terms ·EMW p19:
- **LHS** $-\oint(\mathbf E\times\mathbf H)\cdot d\mathbf s$ = net **power flowing into** the volume.
- **1st RHS term** $\int\mathbf E\cdot\mathbf J_c\,dv$ = **ohmic power dissipated** inside ($\mathbf E\cdot\mathbf J_c=\sigma E^2$).
- **2nd RHS term** = time **rate of change of the total stored energy** (electric $\tfrac{\varepsilon E^2}{2}$ +
  magnetic $\tfrac{\mu H^2}{2}$).

This is conservation of energy for EM fields: power entering a region either heats it or is stored in the fields.

---

## 5.3 Receiver vs transmitter interpretation ·EMW p20–22

[def] The sign of the Poynting surface integral distinguishes two cases ·EMW p20–22:
- **Receiver** — sources are *outside* the volume; net power flows **in** ($-\oint\mathbf P\cdot d\mathbf s>0$),
  supplying the dissipation ($EJ_c=\sigma E^2$) and the stored energy inside. ·EMW p21
- **Transmitter** — a source ($-EJ_c$, e.g. a battery/antenna) sits *inside* and power flows **out** through the
  surface. ·EMW p22

---

## 5.4 Average (time-mean) Poynting vector ·EMW p22–23

[def] For sinusoidal fields the **average** power flow per cycle matters more than the instantaneous value:
$$P_{av} = \frac{1}{T}\int_0^{T} P(t)\,dt, \qquad T = \frac{1}{f} = \frac{2\pi}{\omega}$$

[derivation] For a plane wave in a lossless dielectric, $E_y = E_{y0}\sin(\omega t-\beta x)$ and
$H_z = \dfrac{E_{y0}}{\eta}\sin(\omega t-\beta x)$, so $P_x = \dfrac{E_{y0}^2}{\eta}\sin^2(\omega t-\beta x)$.
Averaging $\sin^2$ over a cycle gives ½: ·EMW p23

[eq: poynting-average]
$$\boxed{\;P_{av} = \frac{1}{2}\frac{E_{y0}^2}{\eta}\quad(\text{W/m}^2)\;}\qquad
  \big(\text{rms fields: } P_{av} = E_{y0,\text{rms}}^2/\eta\big)$$
- $E_{y0}$ = **peak** E-field amplitude; η = intrinsic impedance of the medium.
- Power through an area S normal to the flow: $P_{x,av} = \dfrac{1}{2}\dfrac{E_{y0}^2}{\eta}\,S$. ·EMW p23

---

### Cross-references
- η comes from → **02-uniform-plane-wave**; for a lossy medium use the complex η* of → **03-waves-in-media**.
- The reflected/transmitted power at a boundary uses P together with Γ, T → **07-reflection-transmission**.

### Verification notes for this section
- 0 flags. Verified correct: P = E×H (W/m²), the Poynting-theorem three-term form, and the average power
  $P_{av}=\tfrac12 E_{y0}^2/\eta$ (standard; the ½ is the cycle-average of sin²).
- Minor spelling typos on these pages ("Poyting", "ca", "I space") noted once in the index; no physics impact.
