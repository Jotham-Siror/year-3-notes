"""
Classify a material as conductor, insulator or both, using the loss
tangent tan(theta) = sigma/(w*eps).

    tan(theta) > 100    conductor
    tan(theta) < 0.01   insulator
    otherwise           quasi-conductor

tan(theta) falls as 1/w, so a material can be a conductor at low
frequency and an insulator at high frequency.  The changeover where
tan(theta) = 1 is at w_c = sigma/eps.
"""

import numpy as np

from propagation import medium_properties, loss_tangent

CONDUCTOR_THRESHOLD = 100.0
INSULATOR_THRESHOLD = 0.01


def classify_at(sigma, w, eps_r=1.0, mu_r=1.0):
    """Classify a material at one angular frequency.

    Returns (label, loss_tangent).
    """
    _, eps = medium_properties(eps_r, mu_r)
    tan_theta = float(loss_tangent(sigma, w, eps))

    if tan_theta > CONDUCTOR_THRESHOLD:
        label = "conductor"
    elif tan_theta < INSULATOR_THRESHOLD:
        label = "insulator"
    else:
        label = "quasi-conductor"

    return label, tan_theta


def crossover_omega(sigma, eps_r=1.0, mu_r=1.0):
    """Angular frequency at which tan(theta) = 1, i.e. w_c = sigma/eps."""
    _, eps = medium_properties(eps_r, mu_r)
    return sigma / eps


def transition_band(sigma, eps_r=1.0, mu_r=1.0):
    """The two angular frequencies bounding the quasi-conductor region.

    Returns (w_conductor_limit, w_insulator_limit): below the first the
    material is a conductor, above the second it is an insulator.
    """
    _, eps = medium_properties(eps_r, mu_r)
    return sigma / (CONDUCTOR_THRESHOLD * eps), sigma / (INSULATOR_THRESHOLD * eps)


def classify_over_range(sigma, w_min, w_max, eps_r=1.0, mu_r=1.0):
    """Classify a material across a frequency band.

    Returns (verdict, tan_at_w_min, tan_at_w_max).  The verdict is 'both'
    when the material changes character inside the band.
    """
    low, t_low = classify_at(sigma, w_min, eps_r, mu_r)
    high, t_high = classify_at(sigma, w_max, eps_r, mu_r)
    _, w_ins = transition_band(sigma, eps_r, mu_r)

    w_cond, _ = transition_band(sigma, eps_r, mu_r)

    # The material counts as BOTH when the band starts in the conductor
    # region and crosses w_c, so conduction current stops dominating
    # somewhere inside the range swept.
    if low == "conductor" and t_high < 1.0:
        verdict = ("both (conductor below {:.3g} rad/s, "
                   "insulator above {:.3g} rad/s)".format(w_cond, w_ins))
    elif low == high:
        verdict = low
    else:
        verdict = "{} at {:.2e} rad/s -> {} at {:.2e} rad/s".format(
            low, w_min, high, w_max)

    return verdict, t_low, t_high


def report(name, sigma, eps_r=1.0, mu_r=1.0, w_min=1e3, w_max=1e10):
    """Print a one-material classification summary over a frequency band."""
    verdict, t_low, t_high = classify_over_range(sigma, w_min, w_max, eps_r, mu_r)
    w_c = crossover_omega(sigma, eps_r, mu_r)
    w_cond, w_ins = transition_band(sigma, eps_r, mu_r)

    print("  {:<16s} sigma = {:<9.3g} S/m   eps_r = {:<6.3g}".format(
        name, sigma, eps_r))
    print("      tan(theta) at {:.0e} rad/s : {:.4g}".format(w_min, t_low))
    print("      tan(theta) at {:.0e} rad/s : {:.4g}".format(w_max, t_high))
    print("      w_c (tan = 1)             : {:.4g} rad/s".format(w_c))
    print("      conductor below           : {:.4g} rad/s".format(w_cond))
    print("      insulator above           : {:.4g} rad/s".format(w_ins))
    print("      VERDICT                   : {}".format(verdict))
    print()
    return verdict


if __name__ == "__main__":
    print("Material classification over 1e3 - 1e10 rad/s")
    print("=" * 66)
    report("Copper", 5.8e7, 1.0)
    report("Sea water", 4.0, 80.0)
    report("Damp soil", 1e-2, 10.0)
    report("Fresh water", 1e-3, 80.0)
    report("Teflon", 1e-15, 2.1)
