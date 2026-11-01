---
kb: "MEC 3104 Fluid Theory"
file_role: formula-sheet
purpose: "All key equations in one place, verified, in canonical LaTeX. Each tagged to its topic file/section. For symbol meanings see _nomenclature.md; for slide provenance see the topic files."
note: "Corrected/standard forms shown (some deck slides had errors — see _verification-log.md)."
---

<!-- Compiled by Jotham-JS, 2026. MEC 3104 Fluid Theory knowledge base. -->

# MEC 3104 — Consolidated formula sheet

## 03 — Fluid properties
- Newton's law of viscosity: $\tau = \mu\dfrac{du}{dy}$;  Couette: $\tau = \mu U/h$
- Kinematic viscosity: $\nu = \mu/\rho$
- Specific gravity: $SG = \rho/\rho_{ref}$;  specific volume $v=1/\rho$
- Surface tension, drop pressure: $\Delta P = 4\sigma/d = 2\sigma/r$
- Capillary rise: $h = \dfrac{4\sigma\cos\theta}{\rho g d}$
- Bulk modulus: $K = -V\dfrac{dP}{dV} = \rho\dfrac{dP}{d\rho}$;  compressibility $\beta=1/K$;  wave speed $a=\sqrt{K/\rho}$
- Perfect gas: $pv = RT$;  polytropic $pv^n=$const;  adiabatic $n=\gamma=C_p/C_v$

## 04 — Fluid statics
- Pressure: $p=P/A$;  gauge $=$ absolute $-$ atmospheric
- Hydraulic press: $F_2 = F_1 A_2/A_1$
- Depth: $dP=-\rho g\,dz \Rightarrow p = p_0 + \rho g h$
- Polytropic atmosphere: $\dfrac{p(z)}{p_0}=\Big[1-\dfrac{n-1}{n}\dfrac{\rho_0 g}{p_0}z\Big]^{n/(n-1)}$;  lapse $\dfrac{dT}{dz}=-\dfrac{n-1}{n}\dfrac{g}{R}$
- Manometer: $p=p_0+\rho g H$;  U-tube $p=p_0+\rho' g H'-\rho g H$;  inclined $H=L\sin\alpha$
- Force on submerged plane: $P=\rho g\,h_G A$;  centre of pressure $y_c=y_G+\dfrac{I_G}{Ay_G}$
- $I_G$: rectangle $\tfrac{1}{12}bh^3$, circle $\tfrac{\pi}{64}d^4$
- Thin cylinder hoop tension: $T=pd/2$
- Buoyancy: $F=\rho g V$ (Archimedes)
- Relative equilibrium: linear $\tan\theta=\alpha/g$;  rotation $z-h_0=\dfrac{\omega^2 r^2}{2g}$

## 05 — Flow fundamentals
- Streamline (2-D): $dx/u = dy/v$
- Reynolds number: $Re=\rho vd/\mu = vd/\nu$;  pipe $Re_{c,lower}\approx2320$
- Vorticity: $\zeta=\dfrac{\partial v}{\partial x}-\dfrac{\partial u}{\partial y}=2\omega$;  irrotational $\zeta=0$
- Circulation: $\Gamma=\oint_s v_s\,ds=\iint_A\zeta\,dA$ (Stokes)
- Continuity: $\rho A v=$const;  incompressible $Av=$const;  $\dot m=\rho Av$

## 06 — Energy & Bernoulli
- Euler (1-D, steady, inviscid): $v\dfrac{\partial v}{\partial s}=-\dfrac1\rho\dfrac{\partial p}{\partial s}-g\dfrac{dz}{ds}$
- Bernoulli (head): $\dfrac{v^2}{2g}+\dfrac{p}{\rho g}+z=H$;  (pressure): $\tfrac12\rho v^2+p+\rho gz=$const
- Stagnation: $p_t=p_s+\tfrac12\rho v^2$
- Venturi: $Q=C\dfrac{A_2}{\sqrt{1-(A_2/A_1)^2}}\sqrt{2gH}$
- Pitot: $v=\sqrt{2gH}=\sqrt{2(p_B-p_C)/\rho}$;  real $v=C_v\sqrt{2gH}$
- Torricelli (orifice): $v=\sqrt{2gH}$;  discharge $Q=C_d\,a\sqrt{2gH}$,  $C_d=C_cC_v$
- Tank drain (falling head): $t_2-t_1=\dfrac{2A}{C_d a\sqrt{2g}}(\sqrt{H_1}-\sqrt{H_2})$;  constant descent vessel $H\propto r^4$
- Weir: $Q=\tfrac23 C b\sqrt{2g}\,H^{3/2}$

## 07 — Momentum
- Impulse–momentum: $F=\dot m(v_2-v_1)$
- Bend force (resultant): $F=\sqrt{F_x^2+F_y^2}$ *(NOT −; slide 263 error)*
- Jet on plate: $F=\rho Q v\sin\theta$;  split $Q_1=\tfrac Q2(1+\cos\theta)$, $Q_2=\tfrac Q2(1-\cos\theta)$
- Moving plate: $F=\rho\dfrac{Q(v-u)^2\sin\theta}{v}$ *(denominator v, not v²; slide 263 error)*
- Sudden expansion (Borda–Carnot): $h_s=\dfrac{(v_1-v_2)^2}{2g}=(1-\tfrac{A_1}{A_2})^2\dfrac{v_1^2}{2g}$
- Propeller: thrust $T=\tfrac\pi4 D^2\rho u(U+\tfrac u2)$;  efficiency $\eta=\dfrac{2}{2+u/U}$
- Angular momentum $=Mrv$;  Euler turbomachine: $T=\dot m(r_2 v_2\cos\alpha_2 - r_1 v_1\cos\alpha_1)$, $L=T\omega$ *(absolute v, not u; slides 284/288 error)*

## 08 — Viscous flow
- Continuity (diff): $\dfrac{\partial\rho}{\partial t}+\dfrac{\partial(\rho u)}{\partial x}+\dfrac{\partial(\rho v)}{\partial y}=0$;  incompr. $\nabla\!\cdot\!\mathbf V=0$
- Navier–Stokes (2-D): $\rho\dfrac{Du}{Dt}=\rho X-\dfrac{\partial p}{\partial x}+\mu\nabla^2 u$  (and y)
- Vorticity transport: $\dfrac{D\zeta}{Dt}=\nu\nabla^2\zeta$;  non-dim RHS $=\tfrac{1}{Re}\nabla^{*2}\zeta^*$
- Plane Poiseuille: $u=-\tfrac{1}{2\mu}\tfrac{dp}{dx}(h-y)y$;  $u_{max}=-\tfrac{1}{8\mu}\tfrac{dp}{dx}h^2$;  $Q=-\tfrac{1}{12\mu}\tfrac{dp}{dx}h^3$;  $v_{mean}=\tfrac23 u_{max}$
- Couette+Poiseuille: $Q=\dfrac{\Delta P}{12\mu l}h^3\pm\dfrac{Uh}{2}$
- Hagen–Poiseuille: $u=-\tfrac{1}{4\mu}\tfrac{dp}{dx}(r_0^2-r^2)$;  $Q=-\tfrac{\pi r_0^4}{8\mu}\tfrac{dp}{dx}$;  $v_{mean}=\tfrac12 u_{max}$;  $\Delta P=\dfrac{128Q\mu l}{\pi d^4}=\dfrac{32\mu lv}{d^2}$
- Turbulence: Reynolds stress $\tau_t=-\rho\overline{u'v'}$;  mixing length $\tau_t=\rho l^2(d\bar u/dy)^2$, $l=0.4y$
- Log law: $\dfrac{\bar u}{v^*}=5.75\log\dfrac{v^*y}{\nu}+5.5$;  1/7-power $\dfrac{\bar u}{\bar u_{max}}=(y/r_0)^{1/n}$, $n=7$ at $Re=10^5$
- Boundary layer: $U\delta^*=\int_0^\infty(U-u)dy$;  $\rho U^2\theta=\rho\int_0^\infty u(U-u)dy$
- Prandtl BL eqns: $\rho(u u_x+v u_y)=-p_x+\mu u_{yy}$, $p_y=0$, $u_x+v_y=0$
- Lubrication: $Q=\dfrac{Uh}{2}-\dfrac{h^3}{12\mu}\dfrac{dp}{dx}$;  $P_{max}\approx0.16\dfrac{\mu U l^2}{h_2^2}$ at $h_1/h_2=2.2$

## 09 — Pipe flow
- Darcy–Weisbach: $h=\lambda\dfrac{l}{d}\dfrac{v^2}{2g}$
- Laminar: $\lambda=64/Re$;  KE-correction ζ=2 (laminar), 1.09 (turbulent)
- Turbulent smooth: Blasius $\lambda=0.3164Re^{-1/4}$;  Kármán–Nikuradse $1/\sqrt\lambda=2\log(Re\sqrt\lambda)-0.8$
- Rough: $\lambda=1/[1.74-2\log(2\varepsilon/d)]^2$
- Hydraulic diameter: $d=4m$, $m=A/s$;  rectangle $4m=\tfrac{2ab}{a+b}$, annulus $4m=d_2-d_1$
- Minor loss: $h_s=\zeta\dfrac{v^2}{2g}$;  contraction $(\tfrac1{C_c}-1)^2\dfrac{v_2^2}{2g}$
- Throttle: $Q=C\tfrac{\pi d^2}{4}\sqrt{2\Delta P/\rho}$;  $\sigma=Q/(\nu l)$;  rounded $C=\tfrac{1}{1.16+6.25\sigma^{-0.61}}$;  not-rounded $C=\tfrac{1}{1+5.3/\sqrt\sigma}$
- Diffuser efficiency: $\eta=1-\zeta\dfrac{1-A_1/A_2}{1+A_1/A_2}$
- Bend/elbow: $h_b=(\zeta+\lambda\tfrac ld)\dfrac{v^2}{2g}$
- Total loss: $h=(\lambda\tfrac ld+\sum\zeta)\dfrac{v^2}{2g}$  (+1 for exit)
- Pump: $H=H_a+h$;  water power $L_w=\rho gQH$;  $\eta=L_w/L_s$

## 10 — Open-channel flow
- Uniform flow: $\tau_0=\rho g m i$
- Chézy: $v=c\sqrt{mi}$;  Manning $v=\tfrac1n m^{2/3}i^{1/2}$ (SI), $\tfrac{1.486}{n}m^{2/3}i^{1/2}$ (BG)
- Discharge: $Q=\tfrac1n A m^{2/3}i^{1/2}$
- Best rectangular section: $H/B=1/2$
- Circular partial: $m=\tfrac r2(1-\tfrac{\sin\theta}{\theta})$;  $\tfrac{v}{v_{full}}=(1-\tfrac{\sin\theta}\theta)^{2/3}$
- Specific energy: $E=h+\dfrac{Q^2}{2gA^2}=h+\dfrac{v^2}{2g}$
- Critical: $Q^2=gA_c^3/B$;  rect. $h_c=(q^2/g)^{1/3}$, $E_c=1.5h_c$, $v_c=\sqrt{gh_c}$
- Froude: $Fr=v/\sqrt{gh}$ (<1 subcritical, >1 supercritical)

## 11 — Drag & lift
- Stagnation: $p_0=p_\infty+\tfrac12\rho U^2$
- Drag: $D=C_D A\tfrac12\rho U^2$;  form drag $D_p=\int p\,dA\cos\theta$, friction $D_f=\int\tau\,dA\sin\theta$
- Flat plate: $C_f=0.074Re^{-1/5}$ (turbulent);  $C_f=\tfrac{0.074}{Re^{1/5}}-\tfrac{1700}{Re}$;  laminar $\delta=5.48\sqrt{\nu x/U}$, $\tau_0\approx0.33\sqrt{\rho\mu U^3/x}$
- Ideal cylinder: $v_\theta=2U\sin\theta$;  $p-p_\infty=\tfrac{\rho U^2}{2}(1-4\sin^2\theta)$;  d'Alembert: zero drag
- Cylinder drag crisis: $C_D\approx1$–1.2 → 0.3 at $Re\approx3.8\times10^5$
- Strouhal: $f=0.198\tfrac Ud(1-\tfrac{19.7}{Re})$, $St=fd/U$
- Sphere: $C_D\approx0.44$ (subcritical);  Stokes $D=3\pi\mu Ud$, $C_D=24/Re$ (Re<1)
- Revolving disc: $T=\pi f\rho\omega^2 r_0^4(\tfrac25 r_0+b)$, $L=T\omega$
- Kutta–Joukowski lift: $L=\rho U\Gamma$;  rotating cylinder $\Gamma=2\pi r_0^2\omega$
- Wing: aspect ratio $=b^2/A=b/l$;  $L=C_L\,l\,\tfrac12\rho U^2$ **per unit span** (N/m);  cascade lift $=\rho v_\infty\Gamma$
- Cavitation number: $k_d=\dfrac{p_\infty-p_u}{\tfrac12\rho U^2}$

## Oct 2026 edition — additions

Equations that are new, newly stated or corrected in the October 2026 edition, by topic group. Each is also in its topic file. Slide numbers are the new edition.

### Topics 01–03 (slides 1–65)

- Dimensional homogeneity, example ·slide 61 (§3.10):
  $$P + \tfrac{1}{2}\rho V^{2} + \rho g Z = \text{constant}\qquad\text{each term has units of pressure}$$
- Weight and mass in BG units ·slides 63–65 (§3.10):
  $$W = mg,\qquad F = ma,\qquad 1\ \text{lbf} = 1\ \text{slug}\cdot\text{ft/s}^{2}$$
  (the last identity is [added], not printed on the slides).
- Bulk modulus — no change to the sheet's form, but note S35: the slide now prints it without the minus sign.
  Correct form stays $K = -V\,dP/dV = \rho\,dP/d\rho$ ·slide 56.
- Wave speed, intermediate step now shown ·slide 57:
  $$a = \sqrt{\frac{dP}{d\rho}} = \sqrt{\frac{K\,d\rho/\rho}{d\rho}} = \sqrt{\frac{K}{\rho}}$$
- Conversion constant correction for any units table on the sheet: 1 ft·lbf = 1.35582 J (S33).

### Topic 04 — Fluid Statics (slides 66–156)

- Parallel-axis theorem ·slides 123–124: $I_x = I_G + A\,y_G^2$
- Centre-of-pressure offset on an inclined plane [added standard form, used to correct ·slides 128–131]: $l = y_C - y_G = \dfrac{I_G\sin\theta}{h_G A}$, with y measured along the plane from the free surface
- Force on a plane with specific weight ·slide 127: $F = p_{CG}A = \gamma h_{CG} A$
- Buoyancy with specific weight ·slide 143: $F_B = \gamma V$ (weight in air − weight in liquid)
- Metacentric height ·slide 146: $\overline{MG} = \dfrac{I_o}{V_{\text{sub}}} - \overline{GB}$; stable if $\overline{MG} > 0$
- Rectangular barge (width 2L, draft H, G at waterline) ·slide 148: $\overline{MG} = \dfrac{L^2}{3H} - \dfrac{H}{2}$
- Linear acceleration, surface rise at the wall ·slide 153: $\Delta z = R\tan\theta$, $\tan\theta = a/g$
- Polytropic integration step ·slide 83: $dz = -\dfrac{1}{g}\dfrac{P_0}{\rho_0}\Big(\dfrac{P_0}{P}\Big)^{1/n} d\Big(\dfrac{P}{P_0}\Big)$
- Troposphere index from lapse rate ·slide 90: $\dfrac{dT}{dz} = -\dfrac{n-1}{n}\dfrac{\rho_0 g T_0}{p_0}$ ⇒ n = 1.235
- Existing formula-sheet line "Pressure: $p=P/A$" — the Oct 2026 edition writes $p = F/A$ ·slide 68.

### Topics 05–06 (slides 157–255)

- [eq: kinematic-viscosity] $\nu = \dfrac{\mu}{\rho}$ ·slide 172 (now stated on the slide)
- [eq: hagen-poiseuille-Q] $Q = \dfrac{\pi R^{4}\,\Delta P}{8\mu L} \;\Leftrightarrow\; \Delta P = \dfrac{8\mu L Q}{\pi R^{4}}$ ·slides 176, 178 (given as data in topic 05; derived in 08)
- [eq: pumping-power] $\text{Power} = Q\,\Delta P$ ·slides 176, 178
- Laminar sizing [added]: $Re = \dfrac{4Q}{\pi d\,\nu}$ for a full circular pipe, so $d \ge \dfrac{4Q}{\pi\nu Re_c}$ for laminar flow ·slide 179 (exercise)
- Circulation of fluid in contact with a cylinder turning at $N$ rpm: $\Gamma = (\pi d)\Big(\dfrac{\pi d N}{60}\Big) = 2\pi R^{2}\omega$ ·slide 194
- [eq: bernoulli-loss] $\dfrac{v_1^{2}}{2g}+\dfrac{p_1}{\rho g}+z_1 = \dfrac{v_2^{2}}{2g}+\dfrac{p_2}{\rho g}+z_2 + h_L$ ·slides 220, 225, 226
- Pressure under a liquid layer: $p = \gamma h = \rho g h$ (used for the oil layer) ·slide 225
- [eq: venturi-manometer] $p_1 - p_2 = (\gamma_{m} - \gamma)\,y$, so $\dfrac{p_1-p_2}{\gamma} = (S_m - 1)\,y$ (mercury under water: $12.6\,y$) ·slide 233 (corrected form — slide prints 13.6, S55)
- Venturi in terms of the head difference: $Q = C A_2\sqrt{\dfrac{2g\,(p_1-p_2)/\gamma}{1-(A_2/A_1)^{2}}}$ ·slide 233
- [eq: orifice-jet-diameter] $a_{jet} = C_c\,a$, $D_{jet} = d\sqrt{C_c}$ ·slide 248
- Actual jet velocity $v_{act} = C_v\sqrt{2gH} = Q/a_{jet}$ ·slides 243, 249

### Topics 07–08 (slides 256–375)

- Bend force components, rearranged (·slide 263):
  $$F_x = \dot m(v_1\cos\alpha_1 - v_2\cos\alpha_2) + A_1p_1\cos\alpha_1 - A_2p_2\cos\alpha_2$$
  $$F_y = \dot m(v_1\sin\alpha_1 - v_2\sin\alpha_2) + A_1p_1\sin\alpha_1 - A_2p_2\sin\alpha_2$$
- Sudden-expansion momentum step (·slide 270): $\rho Q(v_2-v_1) = (p_1-p_2)A_2$.
- Moving-plate force — citation now ·slide 268: $F = \rho Q(v-u)^2\sin\theta/v$.
- Jet pump — citation now ·slides 274–275 (keep the $p_2-p_1$ form; note S67):
  $$p_2 - p_1 = \rho\,\frac{d^2}{D^2}\,\frac{D^2-d^2}{D^2}\,(v_0-v_1)^2$$
- Navier–Stokes, cylindrical/axisymmetric (·slides 309, 310, 314 — standard form, printed versions flagged S70):
  $$\rho\Big(\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial r}\Big) = \rho X - \frac{\partial p}{\partial x} + \mu\Big(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial r^2}+\frac{1}{r}\frac{\partial u}{\partial r}\Big)$$
  $$\rho\Big(\frac{\partial v}{\partial t}+u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial r}\Big) = \rho R - \frac{\partial p}{\partial r} + \mu\Big(\frac{\partial^2 v}{\partial x^2}+\frac{\partial^2 v}{\partial r^2}+\frac{1}{r}\frac{\partial v}{\partial r}-\frac{v}{r^2}\Big)$$
- Eddy (turbulent) viscosity (·slide 337): $\tau = \rho(\nu+\nu_t)\,\dfrac{d\bar u}{dy}$.
- Turbulent BL x-momentum (·slide 359, with S20 corrected):
  $\rho\big(\bar u\,\partial\bar u/\partial x + \bar v\,\partial\bar u/\partial y\big) = -\partial\bar p/\partial x + \partial\tau/\partial y$.
- Lubrication pressure distribution (·slide 368):
  $$p = \frac{6\mu U}{\alpha(h_1-\alpha x)} - \frac{6\mu Q}{\alpha(h_1-\alpha x)^2} - \frac{6\mu U}{\alpha(h_1+h_2)},\qquad Q = \frac{h_1h_2}{h_1+h_2}U$$
- Lubrication load per unit width (·slide 369, corrected per S77):
  $$W = \frac{6\mu U l^2}{(h_1-h_2)^2}\Big[\ln\frac{h_1}{h_2} - \frac{2(h_1-h_2)}{h_1+h_2}\Big],\qquad W_{max} \approx 0.16\,\frac{\mu Ul^2}{h_2^2}\ \ (h_1/h_2 \approx 2.2)$$
- Parallel plates, pressure drop from flow (per unit width) (·slides 322–324): $\Delta P = \dfrac{12\mu l\,Q}{h^3}$.
- Citation updates: Navier–Stokes ·slide 308; laminar BL equations ·slide 358 (no longer hidden).

### Topics 09–11 (slides 376–561)

- Itaya, smooth pipe ·slide 393: $$\lambda = \frac{0.314}{0.7 - 1.65\log_{10}Re + (\log_{10}Re)^2}$$
- Pump head between two reservoirs ·slide 456: $$h_p = z_2 - z_1 + h_f + \sum h_m = (z_2 - z_1) + \frac{v^2}{2g}\Big(\frac{fL}{d} + \sum\zeta\Big)$$
- Power given to the water ·slide 458: $P = \rho g Q h_p$ (1 hp = 550 ft·lbf/s) — same as $L_w = \rho g Q H$ (·slide 451).
- Critical condition, rectangular channel width $b$ ·slide 497: $gA_c^3 = bQ^2$ (the §10.6 form $Q^2 = gA_c^3/B$).
- Minimum specific energy ·slide 497: $$E_{\min} = \frac{A_c}{2b} + h_c = 1.5\,h_c$$
- Disc rim torque ·slide 531 (corrected, S85): $T_2 = \pi f'\rho\omega^2 r_0^4\,b$.
- Rotating cylinder, surface pressure ·slide 538: $$\frac{p - p_\infty}{\rho U^2/2} = 1 - \Big(\frac{2U\sin\theta + r_0\omega}{U}\Big)^2$$
- Lift per unit width ·slide 540: $$L = -r_0\rho U^2\int_{-\pi/2}^{\pi/2}\Big[1 - \Big(\frac{r_0\omega}{U}\Big)^2 - \frac{4r_0\omega}{U}\sin\theta - 4\sin^2\theta\Big]\sin\theta\,d\theta = 2\pi r_0^2\omega\rho U = \rho U\Gamma$$

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
