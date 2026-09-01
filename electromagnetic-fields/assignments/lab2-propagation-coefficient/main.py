"""
Lab 2 entry point.  Runs each task in order.

Run with:  python main.py
"""

import numpy as np

from propagation import (medium_properties,
                         alpha_exact, beta_exact,
                         alpha_conductor, beta_conductor,
                         alpha_dielectric, beta_dielectric,
                         alpha_lossy, beta_lossy,
                         penetration_depth, phase_velocity)
from material_class import report, classify_at, crossover_omega
import sweep_plot


def banner(text):
    print()
    print("=" * 72)
    print(text)
    print("=" * 72)


# ----------------------------------------------------------------------
# A (a)  Insulator, conductor, or both
# ----------------------------------------------------------------------
def part_a_classification():
    banner("A (a)   MATERIAL CLASSIFICATION   (band 1e3 - 1e10 rad/s)")
    print()
    report("Copper", 5.8e7, 1.0)
    report("Sea water", 4.0, 80.0)
    report("Damp soil", 1e-2, 10.0)
    report("Fresh water", 1e-3, 80.0)
    report("Teflon", 1e-15, 2.1)


# ----------------------------------------------------------------------
# A (b)  alpha and beta for the three idealised cases
# ----------------------------------------------------------------------
def part_a_coefficients():
    banner("A (b)   ATTENUATION AND PHASE SHIFT COEFFICIENTS")

    # ---- i. pure conductor : copper at 1 MHz -------------------------
    sigma, eps_r, mu_r = 5.8e7, 1.0, 1.0
    f = 1e6
    w = 2.0 * np.pi * f
    mu, eps = medium_properties(eps_r, mu_r)

    a_ap = alpha_conductor(sigma, w, mu)
    b_ap = beta_conductor(sigma, w, mu)
    a_ex = alpha_exact(sigma, w, mu, eps)
    b_ex = beta_exact(sigma, w, mu, eps)

    print("\n  i.  PURE CONDUCTOR  -- copper, f = 1 MHz")
    print("      sigma = {:.3g} S/m,  eps_r = {:g},  mu_r = {:g}".format(
        sigma, eps_r, mu_r))
    print("      alpha = beta = sqrt(w*mu*sigma/2)")
    print("      alpha (approx) = {:.6g} Np/m".format(float(a_ap)))
    print("      alpha (exact)  = {:.6g} Np/m".format(float(a_ex)))
    print("      beta  (approx) = {:.6g} rad/m".format(float(b_ap)))
    print("      beta  (exact)  = {:.6g} rad/m".format(float(b_ex)))
    print("      skin depth  delta = {:.6g} m".format(
        float(penetration_depth(a_ap))))

    # ---- ii. pure dielectric : teflon --------------------------------
    sigma, eps_r, mu_r = 0.0, 2.1, 1.0
    w = 1e9
    mu, eps = medium_properties(eps_r, mu_r)

    a_ap = alpha_dielectric()
    b_ap = beta_dielectric(w, mu, eps)

    print("\n  ii. PURE DIELECTRIC -- teflon, w = 1e9 rad/s")
    print("      sigma = 0,  eps_r = {:g},  mu_r = {:g}".format(eps_r, mu_r))
    print("      alpha = 0,  beta = w*sqrt(mu*eps)")
    print("      alpha = {:.6g} Np/m".format(float(a_ap)))
    print("      beta  = {:.6g} rad/m".format(float(b_ap)))
    print("      phase velocity u = {:.6g} m/s".format(
        float(phase_velocity(w, b_ap))))

    # ---- iii. lossy medium : damp soil -------------------------------
    # w = 1e11 rad/s: at 1e10 the loss tangent is still 0.0113, just
    # outside the low-loss regime.
    sigma, eps_r, mu_r = 1e-2, 10.0, 1.0
    w = 1e11
    mu, eps = medium_properties(eps_r, mu_r)

    a_ap = alpha_lossy(sigma, mu, eps)
    b_ap = beta_lossy(sigma, w, mu, eps)
    a_ex = alpha_exact(sigma, w, mu, eps)
    b_ex = beta_exact(sigma, w, mu, eps)

    print("\n  iii. LOSSY MEDIUM  -- damp soil, w = 1e11 rad/s")
    print("      sigma = {:g} S/m,  eps_r = {:g},  mu_r = {:g}".format(
        sigma, eps_r, mu_r))
    print("      alpha = (sigma/2)*sqrt(mu/eps)")
    print("      beta  = w*sqrt(mu*eps)*(1 + sigma^2/(8*w^2*eps^2))")
    print("      alpha (approx) = {:.6g} Np/m".format(float(a_ap)))
    print("      alpha (exact)  = {:.6g} Np/m".format(float(a_ex)))
    print("      beta  (approx) = {:.6g} rad/m".format(float(b_ap)))
    print("      beta  (exact)  = {:.6g} rad/m".format(float(b_ex)))
    print("      penetration depth  delta = {:.6g} m".format(
        float(penetration_depth(a_ex))))


# ----------------------------------------------------------------------
# B and C  frequency sweep for damp soil
# ----------------------------------------------------------------------
def part_b_sweep():
    banner("B and C   FREQUENCY SWEEP -- DAMP SOIL")
    print("\n  sigma = 1e-2 S/m,  eps_r = 10,  mu_r = 1")
    print("  w from 1e3 to 1e10 rad/s\n")

    d, figs = sweep_plot.run(sigma=1e-2, eps_r=10.0, mu_r=1.0)

    w_c = d["w_c"]
    a_low = d["alpha"][0]
    a_high = d["alpha"][-1]
    print("  changeover  w_c = sigma/eps = {:.4g} rad/s".format(w_c))
    print("  alpha at 1e3  rad/s = {:.4g} Np/m   ->  delta = {:.4g} m".format(
        a_low, 1.0 / a_low))
    print("  alpha at 1e10 rad/s = {:.4g} Np/m   ->  delta = {:.4g} m".format(
        a_high, 1.0 / a_high))
    print("  ratio alpha(high)/alpha(low) = {:.4g}".format(a_high / a_low))
    print()
    for p in figs:
        print("  figure written: {}".format(p))


if __name__ == "__main__":
    part_a_classification()
    part_a_coefficients()
    part_b_sweep()
    print()
