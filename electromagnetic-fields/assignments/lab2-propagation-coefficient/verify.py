"""
verify.py
=========
Numerical verification of the derived expressions.

BEE3102: Electromagnetic Fields and Waves - Lab 2

Checks performed:

  1. Equations 1 and 2 against gamma = sqrt(j*w*mu*(sigma + j*w*eps))
     evaluated directly in complex arithmetic.
  2. The identity  2*alpha*beta = w*mu*sigma   (equation B of the derivation).
  3. Each approximation against the exact result inside its own regime:
        good conductor    tan(theta) >> 1
        low-loss medium   tan(theta) << 1
        pure dielectric   sigma = 0
  4. The floating-point cancellation that defeats Equation 1 for a
     near-lossless medium, and the binomial form that survives it.
"""

import numpy as np

from propagation import (MU0, EPS0, medium_properties, loss_tangent,
                         alpha_exact, beta_exact, gamma_complex,
                         alpha_conductor, beta_conductor,
                         alpha_dielectric, beta_dielectric,
                         alpha_lossy, beta_lossy,
                         penetration_depth, phase_velocity, wavelength)
from material_class import (CONDUCTOR_THRESHOLD, INSULATOR_THRESHOLD,
                            classify_at, crossover_omega, transition_band,
                            classify_over_range)

C_LIGHT = 299792458.0            # exact by SI definition, m/s


def rel_err(a, b):
    """Relative error between two arrays, guarded against division by zero."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    denom = np.where(np.abs(b) > 0, np.abs(b), 1.0)
    return np.abs(a - b) / denom


def verdict(name, err, tol):
    """Report one check.  Returns True on pass."""
    err = np.asarray(err, float)
    if err.size == 0:
        print("  [SKIP] {:<52s} no samples in regime".format(name))
        return True
    worst = float(np.max(err))
    tag = "PASS" if worst <= tol else "FAIL"
    print("  [{}] {:<52s} worst error {:.3e}".format(tag, name, worst))
    return tag == "PASS"


def is_true(name, condition):
    """Report a boolean check."""
    tag = "PASS" if condition else "FAIL"
    print("  [{}] {:<52s} {}".format(tag, name, "ok" if condition else "WRONG"))
    return bool(condition)


def run():
    print("Verification of the derived expressions")
    print("=" * 78)

    results = []
    w = np.logspace(3, 10, 400)

    # ---- 1. Equations 1 and 2 vs direct complex arithmetic -----------
    # Equation 1 subtracts 1 from sqrt(1 + t^2).  As t -> 0 the two terms
    # agree to more and more digits, so the difference is formed by
    # cancellation and loses roughly eps_machine/t^2 in relative accuracy.
    # The alpha tolerance below is therefore looser than beta's, which
    # involves no such subtraction.  Check 4 shows the extreme case.
    print("\n  1.  Equations 1 and 2 against the complex square root")
    for name, sigma, eps_r in [("copper", 5.8e7, 1.0),
                               ("sea water", 4.0, 80.0),
                               ("damp soil", 1e-2, 10.0),
                               ("fresh water", 1e-3, 80.0)]:
        mu, eps = medium_properties(eps_r, 1.0)
        g = gamma_complex(sigma, w, mu, eps)
        results.append(verdict("alpha, {}".format(name),
                               rel_err(alpha_exact(sigma, w, mu, eps), g.real), 1e-6))
        results.append(verdict("beta,  {}".format(name),
                               rel_err(beta_exact(sigma, w, mu, eps), g.imag), 1e-12))

    # ---- 2. The identity 2*alpha*beta = w*mu*sigma -------------------
    print("\n  2.  Identity  2*alpha*beta = w*mu*sigma   (equation B)")
    for name, sigma, eps_r in [("copper", 5.8e7, 1.0),
                               ("sea water", 4.0, 80.0),
                               ("damp soil", 1e-2, 10.0)]:
        mu, eps = medium_properties(eps_r, 1.0)
        lhs = 2.0 * alpha_exact(sigma, w, mu, eps) * beta_exact(sigma, w, mu, eps)
        results.append(verdict(name, rel_err(lhs, w * mu * sigma), 1e-10))

    # ---- 3a. Good-conductor approximation ----------------------------
    print("\n  3a. Good-conductor limit, checked where tan(theta) > 1e4")
    sigma, eps_r = 5.8e7, 1.0
    mu, eps = medium_properties(eps_r, 1.0)
    m = loss_tangent(sigma, w, eps) > 1e4
    results.append(verdict("alpha = sqrt(w*mu*sigma/2), copper (deep regime)",
                           rel_err(alpha_conductor(sigma, w[m], mu),
                                   alpha_exact(sigma, w[m], mu, eps)), 1e-4))
    results.append(verdict("beta  = sqrt(w*mu*sigma/2), copper (deep regime)",
                           rel_err(beta_conductor(sigma, w[m], mu),
                                   beta_exact(sigma, w[m], mu, eps)), 1e-4))

    # Copper never leaves the conductor regime inside this band, so the
    # approximation is never tested near its edge.  Damp soil crosses
    # tan(theta) = 100 at 1.13e6 rad/s and does exercise the boundary.
    sigma, eps_r = 1e-2, 10.0
    mu, eps = medium_properties(eps_r, 1.0)
    m = loss_tangent(sigma, w, eps) > CONDUCTOR_THRESHOLD
    print("      edge case: damp soil, {} samples with tan(theta) > {:g}"
          .format(int(m.sum()), CONDUCTOR_THRESHOLD))
    results.append(verdict("alpha = sqrt(w*mu*sigma/2), at the regime edge",
                           rel_err(alpha_conductor(sigma, w[m], mu),
                                   alpha_exact(sigma, w[m], mu, eps)), 1e-2))

    # ---- 3b. Low-loss approximation ----------------------------------
    # Damp soil only reaches tan(theta) = 0.0113 at 1e10 rad/s, so the
    # low-loss regime is sampled on its own, wider band.
    print("\n  3b. Low-loss limit, checked where tan(theta) < 1e-2")
    w_lo = np.logspace(10, 14, 400)
    sigma, eps_r = 1e-2, 10.0
    mu, eps = medium_properties(eps_r, 1.0)
    m = loss_tangent(sigma, w_lo, eps) < 1e-2
    print("      {} of {} samples in regime, "
          "w from {:.2e} to {:.2e} rad/s".format(
              int(m.sum()), m.size, w_lo[m][0], w_lo[m][-1]))
    results.append(verdict("alpha = (sigma/2)*sqrt(mu/eps)",
                           rel_err(alpha_lossy(sigma, mu, eps, w_lo[m]),
                                   alpha_exact(sigma, w_lo[m], mu, eps)), 1e-4))
    results.append(verdict("beta  = w*sqrt(mu*eps)*(1 + t^2/8)",
                           rel_err(beta_lossy(sigma, w_lo[m], mu, eps),
                                   beta_exact(sigma, w_lo[m], mu, eps)), 1e-8))

    # ---- 3c. Pure dielectric -----------------------------------------
    print("\n  3c. Pure dielectric, sigma = 0")
    mu, eps = medium_properties(2.1, 1.0)
    results.append(verdict("alpha = 0",
                           np.abs(alpha_exact(0.0, w, mu, eps)
                                  - alpha_dielectric(w)), 1e-30))
    results.append(verdict("beta  = w*sqrt(mu*eps)",
                           rel_err(beta_dielectric(w, mu, eps),
                                   beta_exact(0.0, w, mu, eps)), 1e-12))

    # ---- 4. Cancellation in Equation 1 for a near-lossless medium ----
    print("\n  4.  Cancellation in Equation 1 -- teflon, sigma = 1e-15 S/m")
    sigma, eps_r = 1e-15, 2.1
    mu, eps = medium_properties(eps_r, 1.0)
    w_t = 1e9
    t = float(loss_tangent(sigma, w_t, eps))
    a_eq1 = float(alpha_exact(sigma, w_t, mu, eps))
    a_cpx = float(gamma_complex(sigma, w_t, mu, eps).real)
    a_bin = float(alpha_lossy(sigma, mu, eps))

    print("      tan(theta)              = {:.4e}".format(t))
    print("      tan(theta)^2            = {:.4e}   (below eps_machine = 2.2e-16)"
          .format(t ** 2))
    print("      alpha from Equation 1   = {:.6e} Np/m".format(a_eq1))
    print("      alpha from complex sqrt = {:.6e} Np/m".format(a_cpx))
    print("      alpha from binomial     = {:.6e} Np/m".format(a_bin))
    print("      Equation 1 loses the result to cancellation in")
    print("      sqrt(1 + t^2) - 1; the binomial form does not.")
    results.append(verdict("binomial alpha matches complex sqrt",
                           rel_err(a_bin, a_cpx), 1e-6))

    # ---- 5. External ground truth ------------------------------------
    # Checks 1-4 compare the code against itself: every one of them still
    # passes if MU0 or EPS0 is given a wrong value, because the same
    # constant appears on both sides.  These anchor to values known
    # independently of this code.
    print("\n  5.  External ground truth (anchors the physical constants)")
    results.append(verdict("1/sqrt(mu0*eps0) = c = 299792458 m/s",
                           rel_err(1.0 / np.sqrt(MU0 * EPS0), C_LIGHT), 1e-9))

    mu, eps = medium_properties(1.0, 1.0)
    results.append(verdict("free space: beta = w/c",
                           rel_err(beta_exact(0.0, w, mu, eps), w / C_LIGHT), 1e-9))

    mu, eps = medium_properties(2.1, 1.0)
    results.append(verdict("teflon: u = c/sqrt(2.1)",
                           rel_err(phase_velocity(w, beta_dielectric(w, mu, eps)),
                                   C_LIGHT / np.sqrt(2.1)), 1e-9))

    mu, eps = medium_properties(1.0, 1.0)
    d_cu = penetration_depth(alpha_conductor(5.8e7, 2.0 * np.pi * 1e6, mu))
    results.append(verdict("copper skin depth at 1 MHz = 66.09 um",
                           rel_err(d_cu, 6.6085e-5), 1e-4))

    # ---- 6. Derived quantities ---------------------------------------
    print("\n  6.  Derived quantities")
    mu, eps = medium_properties(10.0, 1.0)
    a = alpha_exact(1e-2, w, mu, eps)
    b = beta_exact(1e-2, w, mu, eps)
    results.append(verdict("penetration depth: alpha * delta = 1",
                           rel_err(a * penetration_depth(a), 1.0), 1e-12))
    results.append(verdict("phase velocity: u * beta = w",
                           rel_err(phase_velocity(w, b) * b, w), 1e-12))
    results.append(verdict("wavelength: lambda * beta = 2*pi",
                           rel_err(wavelength(b) * b, 2.0 * np.pi), 1e-12))
    b0 = beta_dielectric(w, mu, eps)
    results.append(verdict("lossless: u = 1/sqrt(mu*eps)",
                           rel_err(phase_velocity(w, b0),
                                   1.0 / np.sqrt(mu * eps)), 1e-12))

    # ---- 7. Material classification ----------------------------------
    print("\n  7.  Material classification")
    results.append(is_true("copper at 1e3 rad/s -> conductor",
                           classify_at(5.8e7, 1e3, 1.0)[0] == "conductor"))
    results.append(is_true("teflon at 1e10 rad/s -> insulator",
                           classify_at(1e-15, 1e10, 2.1)[0] == "insulator"))
    results.append(is_true("damp soil at 1e8 rad/s -> quasi-conductor",
                           classify_at(1e-2, 1e8, 10.0)[0] == "quasi-conductor"))

    for name, sigma, eps_r in [("copper", 5.8e7, 1.0), ("damp soil", 1e-2, 10.0)]:
        _, eps = medium_properties(eps_r, 1.0)
        results.append(verdict("{}: tan(theta) = 1 at w_c".format(name),
                               rel_err(loss_tangent(sigma,
                                                    crossover_omega(sigma, eps_r),
                                                    eps), 1.0), 1e-12))

    _, eps = medium_properties(10.0, 1.0)
    w_cond, w_ins = transition_band(1e-2, 10.0)
    results.append(verdict("transition_band lower end -> tan = 100",
                           rel_err(loss_tangent(1e-2, w_cond, eps),
                                   CONDUCTOR_THRESHOLD), 1e-12))
    results.append(verdict("transition_band upper end -> tan = 0.01",
                           rel_err(loss_tangent(1e-2, w_ins, eps),
                                   INSULATOR_THRESHOLD), 1e-12))
    results.append(is_true("damp soil over 1e3-1e10 rad/s -> both",
                           classify_over_range(1e-2, 1e3, 1e10,
                                               10.0)[0].startswith("both")))
    results.append(is_true("damp soil over 1e3-1e6 rad/s -> conductor only",
                           classify_over_range(1e-2, 1e3, 1e6,
                                               10.0)[0] == "conductor"))
    results.append(is_true("copper over 1e3-1e10 rad/s -> conductor only",
                           classify_over_range(5.8e7, 1e3, 1e10,
                                               1.0)[0] == "conductor"))

    print("\n" + "=" * 78)
    ok = all(results)
    print("  {} of {} checks passed".format(sum(results), len(results)))
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
