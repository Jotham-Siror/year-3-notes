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
- Bend force (resultant): $F=\sqrt{F_x^2+F_y^2}$ *(NOT −; slide 271 error)*
- Jet on plate: $F=\rho Q v\sin\theta$;  split $Q_1=\tfrac Q2(1+\cos\theta)$, $Q_2=\tfrac Q2(1-\cos\theta)$
- Moving plate: $F=\rho\dfrac{Q(v-u)^2\sin\theta}{v}$ *(denominator v, not v²; slide 277 error)*
- Sudden expansion (Borda–Carnot): $h_s=\dfrac{(v_1-v_2)^2}{2g}=(1-\tfrac{A_1}{A_2})^2\dfrac{v_1^2}{2g}$
- Propeller: thrust $T=\tfrac\pi4 D^2\rho u(U+\tfrac u2)$;  efficiency $\eta=\dfrac{2}{2+u/U}$
- Angular momentum $=Mrv$;  Euler turbomachine: $T=\dot m(r_2 v_2\cos\alpha_2 - r_1 v_1\cos\alpha_1)$, $L=T\omega$ *(absolute v, not u; slides 291/295 error)*

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

---

<sub><i>Compiled by Jotham-JS — Jotham Siror · Jesus Saves · 2026</i></sub>
