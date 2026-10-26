---
kb: "Thermodynamics — MEC 3105"
course_code: "MEC 3105"
lecturer: "withheld"
section: "08 — Ansys Icepak for Electro-Thermal Analysis (Topic 4, sub-topics 4.4–4.10)"
source: "IP — 'MEC_3105_Topic4_2_Lecture_Notes_Ansys_Icepak.pdf', 8 pages"
pages: "1-8"
file_role: topic
subtopics:
  - "the three heat transfer modes as Icepak boundary conditions"
  - "Icepak inside Ansys Electronics Desktop; why CFD rather than conduction-only"
  - "governing equations: continuity, Navier-Stokes, energy"
  - "electro-thermal coupling workflow"
  - "classroom tutorial: heat-sinked MOSFET on a PCB"
  - "discussion and sample exam questions"
key_equations: [continuity, navier-stokes, energy-equation, junction-to-ambient]
prerequisites: ["07-heat-transfer-and-thermal-analysis"]
leads_to: []
verification_flags: 2
tags: [ansys, icepak, aedt, cfd, conjugate-heat-transfer, electro-thermal, navier-stokes, mosfet, heat-sink, pcb]
---

<!-- Compiled by Jotham-JS, 2026. MEC 3105 Thermodynamics knowledge base. -->

<!-- TAG LEGEND: [def] · [eq] · [ex] · [added] supplied here, NOT in the source ·
  ·IP pN = PDF page N (the footer "Page N of 8" matches) · ⚠ VERIFY = flagged. -->

# 08 — Ansys Icepak for Electro-Thermal Analysis

Scope: the whole of IP, 8 pages — Topic 4 sub-topics **4.4 to 4.11**, carrying on from `07`.
Page 1 is a title page.

> **Exam value.** Mostly descriptive. The notes end with **four sample exam questions** (§8.7) — the
> clearest signal in the whole course of what an Icepak question looks like. Three are "explain", one is
> a one-line calculation.

---

## 8.1 Recap — the three modes as Icepak sees them ·IP p2

| Mode | Law | Where it acts in Icepak |
|---|---|---|
| Conduction | $q = -kA\,\dfrac{dT}{dx}$ | PCB substrate, copper traces, die-attach, heat-sink base |
| Convection | $q = hA\,(T_s - T_\infty)$ | Icepak **computes $h$ itself** from the airflow (natural or forced) — you do not enter it |
| Radiation | $q = \varepsilon\sigma A\,(T_s^4 - T_{surr}^4)$ | toggled on per surface; matters at high $T$ or in still-air enclosures |

[eq] The energy balance Icepak enforces on every control volume, at steady state:

$$
\text{Power dissipated} = \text{heat conducted} + \text{heat convected} + \text{heat radiated}
$$

"Icepak is, at its core, a numerical energy-balance solver applied to complex electronic geometries."

---

## 8.2 What Icepak is ·IP p2–p3

[def] A **CFD** tool for electronics cooling. It runs the **Fluent** solver behind an electronics-focused
interface inside **Ansys Electronics Desktop (AEDT)**.

| Tool | Physics | Typical use |
|---|---|---|
| HFSS | high-frequency EM | antennas, RF, signal integrity |
| Maxwell | low-frequency EM | motors, transformers, actuators, power electronics |
| Q3D Extractor | parasitic extraction (R, L, C, G) | power modules, busbars, PCB interconnects |
| SIwave | signal/power integrity | PCB and package power delivery |
| **Icepak** | **conjugate heat transfer (CFD)** | ICs, PCBs, enclosures, power modules |

Icepak takes losses from HFSS / Maxwell / Q3D / SIwave and returns temperatures, which can go back to
update temperature-dependent properties such as resistivity — **two-way electro-thermal simulation**.

### Why CFD, not just conduction? ·IP p3

ANSYS Mechanical thermal needs you to **specify $h$**. Icepak **solves the air flow** together with the
solid conduction. That matters because:

- layout and enclosure shape change the local airflow, so a single fixed $h$ can be badly wrong;
- fans, vents, heat sinks and buoyancy must be modelled explicitly;
- ready-made libraries (packages, PCBs, fans, heat sinks) speed up model building.

---

## 8.3 Why EEs care ·IP p3–p4

| Application | Thermal concern | If unmanaged |
|---|---|---|
| IGBT/MOSFET modules | junction rise from switching + conduction loss | shorter life, thermal runaway, failure |
| PCBs | trace $I^2R$, hot spots | delamination, solder fatigue, analogue drift |
| Transformers, inductors | core and winding loss | insulation breakdown, lower efficiency |
| Motors | winding and bearing heat | insulation ageing, magnet demagnetisation |
| Battery packs / EV | uneven cell heating, high discharge current | capacity fade, thermal runaway |

---

## 8.4 The equations Icepak solves ·IP p4–p5

Conservation of mass, momentum and energy in the fluid, plus conduction in the solids — a **conjugate
heat transfer (CHT)** formulation.

| Symbol | Meaning | Units |
|---|---|---|
| $\rho$ | density | $\mathrm{kg/m^3}$ |
| $\mathbf{V}$ (also $\mathbf{u}$) | velocity vector | $\mathrm{m/s}$ |
| $p$ | pressure | $\mathrm{Pa}$ |
| $\mu$ | dynamic viscosity | $\mathrm{Pa\,s}$ |
| $\mathbf{g}$ | gravity | $\mathrm{m/s^2}$ |
| $c_p$ | specific heat | $\mathrm{J/(kg\,K)}$ |
| $k$ | thermal conductivity | $\mathrm{W/(m\,K)}$ |
| $Q$ | volumetric heat source | $\mathrm{W/m^3}$ |

> The page writes the velocity as $V$ in the equations and calls it $u$ in the text (C35). Same thing.

[eq] Continuity (mass) ·IP p4

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0
$$

First term: local accumulation. Second: net outflow per unit volume. Incompressible: $\nabla \cdot \mathbf{u} = 0$.
Same form as charge conservation $\partial \rho_q/\partial t + \nabla \cdot \mathbf{J} = 0$.

[eq] Momentum (Navier–Stokes) ·IP p4

$$
\rho \left( \frac{\partial \mathbf{V}}{\partial t} + \mathbf{V} \cdot \nabla \mathbf{V} \right) = -\nabla p + \mu \nabla^2 \mathbf{V} + \rho \mathbf{g}
$$

Newton's second law on a fluid element: density × acceleration = pressure-gradient + viscous + body
forces. The $(\mathbf{u} \cdot \nabla)\mathbf{u}$ term makes it nonlinear — the source of turbulence.

[eq] Energy ·IP p5

$$
\rho c_p \left( \frac{\partial T}{\partial t} + \mathbf{V} \cdot \nabla T \right) = \nabla \cdot (k \nabla T) + Q
$$

$Q$ is where the electrical loss ($I^2R$, core loss, switching loss) enters. With $\mathbf{V} = 0$ this is
`07`'s heat conduction equation.

---

## 8.5 Electro-thermal coupling ·IP p5

1. Compute losses in the source tool — HFSS (RF/dielectric), Maxwell (core/copper), Q3D ($I^2R$).
2. Map the loss distribution onto the Icepak geometry (surface or volume).
3. Solve the CHT problem in Icepak → temperature field.
4. *(Two-way)* Send temperatures back to the EM solver to update properties (copper resistivity rises with $T$); re-solve losses.
5. Repeat 1–4 until temperature and loss converge.

Why iterate: loss and temperature feed each other (hotter → more resistive → more loss) — the route to
**thermal runaway** if not designed against.

---

## 8.6 Classroom tutorial — heat-sinked MOSFET on a PCB ·IP p5–p7

Scenario: a MOSFET at known power on a PCB with an extruded heat sink, natural convection in still air.
Predict junction and sink temperatures; compare with a resistance-network hand calculation.
One 2–3 hour lab, free Ansys Student licence.

1. **Setup** — AEDT → Project → Insert Icepak Design; solution type Icepak Steady-State Thermal (CFD).
2. **Geometry** — PCB block $100 \times 80 \times 1.6\ \mathrm{mm}$, FR-4; MOSFET package block (library or block with junction-to-case properties); extruded heat sink on top.
3. **Materials and power** — FR-4 $k \approx 0.3\ \mathrm{W/(m\,K)}$ in-plane (anisotropic if copper layers are modelled); aluminium sink $k \approx 200$; MOSFET fixed at e.g. **5 W**.
4. **Enclosure and BCs** — wrap in an open "cabinet"; natural convection, ambient **25 °C (298 K)**; **gravity on** (needed for buoyancy); optional radiation, $\varepsilon \approx 0.85$ for painted/anodised surfaces.
5. **Mesh** — mesher-HD, refine on fins and package.
6. **Solve** — steady state; watch residuals and monitor-point temperatures converge.
7. **Post-process** — temperature contour, peak (junction) temperature; velocity vectors / streamlines of the rising plume; junction-to-ambient resistance:

[eq]

$$
R_{ja} = \frac{T_j - T_\infty}{P}
$$

Compare with the datasheet, or with $R_{jc} + R_{cs} + R_{sa}$ from `07` §4.2.4.

### Discussion questions ·IP p7

1. Peak temperature if the enclosure were sealed? Relate to the convection BC.
2. Radiation switched off — does predicted temperature rise or fall, and why?
3. Hand network vs CFD — what does the lumped method ignore?
4. If the MOSFET's power doubles, does junction temperature double? (The page says "see Section 5" — C36.)

[added] Short answers: (1) rises — no fresh air, $h$ collapses. (2) rises — one heat path removed.
(3) spreading in the board and sink, non-uniform local $h$, plume interaction, radiation. (4) the
**temperature rise** above ambient roughly doubles (linear network), not the junction temperature itself;
and not exactly, because natural-convection $h$ grows with $\Delta T$ and radiation goes as $T^4$.

---

## 8.7 Assignments and sample exam questions ·IP p7

- **Individual:** take a real IGBT/MOSFET datasheet, model it in Icepak, check the maker's maximum safe power at a given ambient.
- **Group:** a 3–5 component PCB; propose a cooling strategy (sink size, fan, placement) keeping every junction under a limit.

**Sample examination questions** — as printed:

1. State the three modes of heat transfer and, for each, identify a specific boundary condition in Icepak that represents it.
2. Explain, with reference to the energy equation, how Icepak determines the convective heat transfer coefficient rather than requiring the user to input it directly.
3. Describe the data exchanged between Ansys Maxwell and Ansys Icepak in a two-way electro-thermal coupling analysis of an electric motor, and explain why the coupling needs to be iterative.
4. A power module dissipates 40 W and has a measured junction-to-ambient thermal resistance of 2.5 °C/W. Using the first-law energy balance, estimate the steady-state junction temperature for an ambient of 35 °C, and state two design changes that would reduce this temperature.

[added] Q4:

$$
T_j = T_{amb} + P\,R_{ja} = 35 + (40)(2.5) = 135\ ^\circ\mathrm{C}
$$

Two changes: a bigger or finned heat sink / forced air (lowers $R_{sa}$), and a better interface material
(lowers $R_{cs}$). Lowering the loss itself also works.

References ·IP p7–p8: Icepak User's Guide; Ansys Innovation Courses ("Electro-Thermal Analysis with HFSS,
Maxwell, and Q3D"; "Topics in Heat Transfer Analyses"); Incropera & DeWitt; Ansys Student.

---

### Verification notes for this section

| ID | Page | Issue |
|---|---|---|
| **C35** | p4 | velocity written $V$ in the equations, called $u$ in the text |
| **C36** | p7–p8 | cross-references to "Section 5", "Sections 2 and 5", "Section 7" use an older numbering; the sections are now 4.4–4.10 |

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
