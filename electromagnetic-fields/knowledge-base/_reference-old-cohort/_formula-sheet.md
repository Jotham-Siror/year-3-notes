---
kb: "Electromagnetic Fields — Year 3"
file_role: formula-sheet
purpose: "All key equations in one place, verified, in canonical LaTeX. Each tagged to its topic file. For symbol meanings see _nomenclature.md; for page provenance see the topic files."
note: "Corrected/standard forms shown (some handout pages had labelling/exponent/unit slips — see _verification-log.md)."
constants: "μ₀=4π×10⁻⁷ H/m; ε₀=8.854×10⁻¹²≈10⁻⁹/36π F/m; c=1/√(μ₀ε₀)=3×10⁸ m/s; η₀=√(μ₀/ε₀)=120π≈377 Ω"
---

# Electromagnetic Fields — Consolidated formula sheet

## Constants (memorize)
- Free-space permeability $\mu_0 = 4\pi\times10^{-7}$ H/m; permittivity $\varepsilon_0 = 8.854\times10^{-12} \approx \dfrac{10^{-9}}{36\pi}$ F/m
- Speed of light $c = \dfrac{1}{\sqrt{\mu_0\varepsilon_0}} = 3\times10^{8}$ m/s
- Intrinsic impedance of free space $\eta_0 = \sqrt{\dfrac{\mu_0}{\varepsilon_0}} = 120\pi \approx 377\ \Omega$

## 01 — Maxwell's equations & the wave equation
- Ampère (+ Maxwell): $\nabla\times\mathbf H = \mathbf J_c + \dfrac{\partial\mathbf D}{\partial t} = \sigma\mathbf E + \varepsilon\dfrac{\partial\mathbf E}{\partial t}$
- Faraday: $\nabla\times\mathbf E = -\mu\dfrac{\partial\mathbf H}{\partial t}$;  Gauss: $\nabla\cdot\mathbf D=\rho$, $\nabla\cdot\mathbf B=0$
- Vector identity (key): $\nabla\times(\nabla\times\mathbf A) = \nabla(\nabla\cdot\mathbf A) - \nabla^2\mathbf A$
- Wave equation (lossy): $\nabla^2\mathbf E = \mu\sigma\dfrac{\partial\mathbf E}{\partial t} + \mu\varepsilon\dfrac{\partial^2\mathbf E}{\partial t^2}$ (same for H)
- Harmonic fields ($e^{j\omega t}$): $\partial_t\to j\omega$, $\partial_t^2\to-\omega^2$ ⇒ Helmholtz $\nabla^2\mathbf E=\gamma^2\mathbf E$
- Propagation constant: $\gamma = \sqrt{j\omega\mu(\sigma+j\omega\varepsilon)} = \alpha + j\beta$
- Exact split (general medium): $\alpha=\omega\sqrt{\tfrac{\mu\varepsilon}{2}}\Big[\sqrt{1+(\tfrac{\sigma}{\omega\varepsilon})^2}-1\Big]^{1/2}$, $\;\beta=\omega\sqrt{\tfrac{\mu\varepsilon}{2}}\Big[\sqrt{1+(\tfrac{\sigma}{\omega\varepsilon})^2}+1\Big]^{1/2}$ *(EMW p6 mislabels both as α & squares the bracket — see log)*

## 02 — Uniform plane wave (TEM)
- Coupled eqns: $\dfrac{\partial H_y}{\partial z}=-\varepsilon_0\dfrac{\partial E_x}{\partial t}$,  $\dfrac{\partial E_x}{\partial z}=-\mu_0\dfrac{\partial H_y}{\partial t}$
- Wave eqn: $\dfrac{\partial^2 E_x}{\partial z^2}=\varepsilon_0\mu_0\dfrac{\partial^2 E_x}{\partial t^2}$;  speed $v=\dfrac{1}{\sqrt{\varepsilon_0\mu_0}}=3\times10^8$ m/s
- General solution: $E_x=f_1(z-v_0t)+f_2(z+v_0t)$ (forward + reflected)
- Intrinsic impedance: $\eta=\dfrac{E_x}{H_y}=\sqrt{\dfrac{\mu}{\varepsilon}}$;  free space $\eta_0=120\pi\approx377\ \Omega$

## 03 — Plane waves in media
- Loss tangent: $\tan\theta=\dfrac{J_c}{J_{disp}}=\dfrac{\sigma}{\omega\varepsilon}$  (≪1 ⇒ dielectric; ≫1 ⇒ conductor)
- Complex permittivity: $\varepsilon^{*}=\varepsilon\Big(1-\dfrac{j\sigma}{\omega\varepsilon}\Big)$;  $\gamma=j\omega\sqrt{\mu\varepsilon^{*}}$
- **Lossy dielectric** (σ/ωε≪1): $\alpha\approx\dfrac{\sigma}{2}\sqrt{\dfrac{\mu}{\varepsilon}}$,  $\beta\approx\omega\sqrt{\mu\varepsilon}\Big[1+\tfrac18(\tfrac{\sigma}{\omega\varepsilon})^2\Big]$,  $\eta^{*}\approx\eta\Big(1+\dfrac{j\sigma}{2\omega\varepsilon}\Big)$
- **Perfect dielectric** (σ=0): $\alpha=0$,  $\beta=\omega\sqrt{\mu\varepsilon}$,  $v_p=\dfrac{1}{\sqrt{\mu\varepsilon}}$,  $\eta=\sqrt{\dfrac{\mu}{\varepsilon}}$
- **Good conductor** (σ/ωε≫1): $\alpha=\beta=\sqrt{\dfrac{\omega\mu\sigma}{2}}=\sqrt{\pi f\mu\sigma}$;  $v_p=\sqrt{\dfrac{2\omega}{\mu\sigma}}$;  $\eta^{*}=\sqrt{\dfrac{\omega\mu}{\sigma}}\angle45^\circ=\sqrt{\dfrac{\omega\mu}{2\sigma}}(1+j)$
- Phase velocity (general): $v_p=\dfrac{\omega}{\beta}$;  wavelength $\lambda=\dfrac{2\pi}{\beta}=\dfrac{v_p}{f}$

## 04 — Skin depth
- Depth of penetration: $\delta=\dfrac{1}{\alpha}=\sqrt{\dfrac{2}{\omega\mu\sigma}}=\dfrac{1}{\sqrt{\pi f\mu\sigma}}$  (attenuation to 1/e ≈ 37 %)
- ↓ with ↑ f, ↑ μ, ↑ σ

## 05 — Poynting vector & energy
- Poynting vector: $\mathbf P=\mathbf E\times\mathbf H$ (W/m²), direction = power flow, ⟂ to both E and H
- Poynting theorem: $-\oint(\mathbf E\times\mathbf H)\cdot d\mathbf s=\displaystyle\int\mathbf E\cdot\mathbf J_c\,dv+\int\dfrac{\partial}{\partial t}\Big(\dfrac{\varepsilon E^2}{2}+\dfrac{\mu H^2}{2}\Big)dv$  (in = dissipated + stored-rate)
- Average power (plane wave): $P_{av}=\dfrac{1}{2}\dfrac{E_{y0}^2}{\eta}$ (peak) $=\dfrac{E_{y0,rms}^2}{\eta}$;  through area S: $P_{av}=\tfrac12\tfrac{E_{y0}^2}{\eta}S$

## 06 — Polarization
- General field: $\mathbf E=(E_x\mathbf a_x+E_y\mathbf a_y)e^{-j\beta z}$, $E_x=|E_x|e^{ja}$, $E_y=|E_y|e^{jb}$ — phase diff $(a-b)$ sets the type
- **Linear** (a=b): direction fixed, $\tan\theta=E_x/E_y$; tip moves on a line
- **Circular** (equal amplitude, 90° = ±j): $E_y=E_a\cos\omega t$, $E_z=E_a\sin\omega t$ ⇒ $E_y^2+E_z^2=E_a^2$ (circle); +j left, −j right
- **Elliptical** (unequal amp / general phase): $\Big(\dfrac{E_y}{A_y}\Big)^2+\Big(\dfrac{E_z}{A_z}\Big)^2=1$ (linear & circular are its limits)
- *(POL p4 says "180°" for circular — should be 90°; see log)*

## 07 — Reflection & transmission (normal incidence)
- Boundary (z=0): $E_{m1}^{+}+E_{m1}^{-}=E_{m2}^{+}$;  $\dfrac{E_{m1}^{+}}{\eta_1}-\dfrac{E_{m1}^{-}}{\eta_1}=\dfrac{E_{m2}^{+}}{\eta_2}$
- Transmission coefficient: $T=\dfrac{2\eta_2}{\eta_1+\eta_2}$
- Reflection coefficient: $\Gamma=\dfrac{\eta_2-\eta_1}{\eta_2+\eta_1}$
- Relation: $1+\Gamma=T$;  matched (η₂=η₁) ⇒ Γ=0,T=1;  perfect conductor (η₂=0) ⇒ Γ=−1,T=0
