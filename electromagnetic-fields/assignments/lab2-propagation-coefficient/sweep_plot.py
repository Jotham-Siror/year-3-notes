"""
Frequency sweep and plots for damp soil.

    sigma = 1e-2 S/m, eps_r = 10, mu_r = 1
    w from 1e3 to 1e10 rad/s
"""

import os

import numpy as np
import matplotlib
matplotlib.use("Agg")            # write files without needing a display
import matplotlib.pyplot as plt

from propagation import (medium_properties, loss_tangent,
                         alpha_exact, beta_exact,
                         alpha_conductor, alpha_lossy, beta_lossy,
                         beta_dielectric, penetration_depth, phase_velocity)
from material_class import crossover_omega

# ----------------------------------------------------------------------
# Plot styling
# ----------------------------------------------------------------------
C_ALPHA = "#2a78d6"      # series 1 -- blue   : attenuation constant
C_BETA = "#eb6834"       # series 2 -- orange : phase shift coefficient
C_GRID = "#e1e0d9"
C_AXIS = "#c3c2b7"
C_INK = "#0b0b0b"
C_MUTED = "#898781"
C_SURFACE = "#fcfcfb"

plt.rcParams.update({
    "figure.facecolor": C_SURFACE,
    "axes.facecolor": C_SURFACE,
    "axes.edgecolor": C_AXIS,
    "axes.labelcolor": C_INK,
    "axes.titlecolor": C_INK,
    "axes.linewidth": 0.8,
    "xtick.color": C_MUTED,
    "ytick.color": C_MUTED,
    "grid.color": C_GRID,
    "grid.linewidth": 0.7,
    "font.family": "sans-serif",
    "font.size": 10,
    "legend.frameon": False,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
})


def _style(ax, title, xlabel, ylabel):
    ax.set_title(title, loc="left", fontsize=12, pad=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, which="major", alpha=0.9)
    ax.grid(True, which="minor", alpha=0.35)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


# ----------------------------------------------------------------------
# The sweep
# ----------------------------------------------------------------------
def sweep(sigma=1e-2, eps_r=10.0, mu_r=1.0, w_min=1e3, w_max=1e10, n=1000):
    """Evaluate every quantity of interest across the frequency band."""
    mu, eps = medium_properties(eps_r, mu_r)
    w = np.logspace(np.log10(w_min), np.log10(w_max), n)

    d = {
        "w": w, "mu": mu, "eps": eps, "sigma": sigma,
        "eps_r": eps_r, "mu_r": mu_r,
        "tan": loss_tangent(sigma, w, eps),
        "alpha": alpha_exact(sigma, w, mu, eps),
        "beta": beta_exact(sigma, w, mu, eps),
        "alpha_cond": alpha_conductor(sigma, w, mu),
        "alpha_low": alpha_lossy(sigma, mu, eps, w),
        "beta_low": beta_lossy(sigma, w, mu, eps),
        "beta_diel": beta_dielectric(w, mu, eps),
        "w_c": crossover_omega(sigma, eps_r, mu_r),
    }
    d["delta"] = penetration_depth(d["alpha"])
    d["u"] = phase_velocity(w, d["beta"])
    return d


# ----------------------------------------------------------------------
# Figures
# ----------------------------------------------------------------------
def plot_alpha(d, outdir="."):
    """Figure 1 -- attenuation constant with its two limiting forms."""
    w = d["w"]
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.loglog(w, d["alpha_cond"], ls="--", lw=1.3, color=C_MUTED,
              label=r"good-conductor limit  $\sqrt{\omega\mu\sigma/2}$")
    ax.loglog(w, d["alpha_low"], ls=":", lw=1.3, color=C_MUTED,
              label=r"low-loss limit  $(\sigma/2)\sqrt{\mu/\varepsilon}$")
    ax.loglog(w, d["alpha"], lw=2.0, color=C_ALPHA,
              label=r"$\alpha$  exact (Eq. 1)")

    ax.axvline(d["w_c"], color=C_AXIS, lw=1.0, ls="-", zorder=1)
    ax.annotate(r"$\tan\theta = 1$" + "\n{:.2e} rad/s".format(d["w_c"]),
                xy=(d["w_c"], ax.get_ylim()[0]), xytext=(4, 6),
                textcoords="offset points", color=C_MUTED, fontsize=9)

    _style(ax, "Attenuation constant vs angular frequency",
           r"angular frequency  $\omega$  (rad/s)",
           r"attenuation constant  $\alpha$  (Np/m)")
    ax.legend(loc="upper left", fontsize=9)

    path = os.path.join(outdir, "fig1_alpha_vs_omega.png")
    fig.savefig(path)
    plt.close(fig)
    return path


def plot_alpha_beta(d, outdir="."):
    """Figure 2 -- alpha and beta on the same axes (lab part C)."""
    w = d["w"]
    fig, ax = plt.subplots(figsize=(8, 5))

    # alpha drawn thicker and underneath so it stays visible where the
    # two curves coincide
    ax.loglog(w, d["alpha"], lw=4.5, color=C_ALPHA, solid_capstyle="round",
              zorder=3, label=r"$\alpha$  (Np/m)")
    ax.loglog(w, d["beta"], lw=2.0, color=C_BETA,
              zorder=4, label=r"$\beta$  (rad/m)")

    ax.axvline(d["w_c"], color=C_AXIS, lw=1.0, zorder=1)

    i = int(0.18 * len(w))
    ax.annotate(r"$\alpha \approx \beta$", xy=(w[i], d["alpha"][i]),
                xytext=(2, -26), textcoords="offset points",
                color=C_MUTED, fontsize=10)
    ax.annotate(r"$\tan\theta = 1$" + "\n{:.2e} rad/s".format(d["w_c"]),
                xy=(d["w_c"], ax.get_ylim()[0]), xytext=(4, 6),
                textcoords="offset points", color=C_MUTED, fontsize=9)

    ax.annotate(r"$\beta$", xy=(w[-1], d["beta"][-1]), xytext=(6, -2),
                textcoords="offset points", color=C_BETA,
                fontsize=12, fontweight="bold")
    ax.annotate(r"$\alpha$", xy=(w[-1], d["alpha"][-1]), xytext=(6, -2),
                textcoords="offset points", color=C_ALPHA,
                fontsize=12, fontweight="bold")

    _style(ax, "Attenuation constant and phase shift coefficient",
           r"angular frequency  $\omega$  (rad/s)",
           r"$\alpha$  (Np/m)   and   $\beta$  (rad/m)")
    ax.legend(loc="upper left", fontsize=9)

    path = os.path.join(outdir, "fig2_alpha_beta.png")
    fig.savefig(path)
    plt.close(fig)
    return path


def plot_penetration_depth(d, outdir="."):
    """Figure 3 -- penetration depth delta = 1/alpha."""
    w = d["w"]
    fig, ax = plt.subplots(figsize=(8, 5))

    floor = float(np.min(d["delta"]))
    ax.loglog(w, d["delta"], lw=2.0, color=C_ALPHA, zorder=3)
    ax.axvline(d["w_c"], color=C_AXIS, lw=1.0, zorder=1)
    ax.axhline(floor, color=C_AXIS, lw=1.0, ls="--", zorder=1)

    ax.annotate(r"$\delta \rightarrow {:.3g}$ m".format(floor),
                xy=(w[-1], floor), xytext=(-8, 10),
                textcoords="offset points", ha="right",
                color=C_MUTED, fontsize=10)
    ax.annotate(r"$\tan\theta = 1$", xy=(d["w_c"], ax.get_ylim()[1]),
                xytext=(5, -16), textcoords="offset points",
                color=C_MUTED, fontsize=9)

    _style(ax, r"Penetration depth  $\delta = 1/\alpha$",
           r"angular frequency  $\omega$  (rad/s)",
           r"penetration depth  $\delta$  (m)")

    path = os.path.join(outdir, "fig3_penetration_depth.png")
    fig.savefig(path)
    plt.close(fig)
    return path


# ----------------------------------------------------------------------
# Tabulated output
# ----------------------------------------------------------------------
def table(d, decades=None):
    """Print alpha, beta, delta and tan(theta) at one point per decade."""
    if decades is None:
        decades = np.logspace(3, 10, 8)

    mu, eps, sigma = d["mu"], d["eps"], d["sigma"]
    a = alpha_exact(sigma, decades, mu, eps)
    b = beta_exact(sigma, decades, mu, eps)
    t = loss_tangent(sigma, decades, eps)
    dep = penetration_depth(a)

    print("  {:>10s}  {:>12s}  {:>12s}  {:>12s}  {:>12s}".format(
        "w (rad/s)", "tan(theta)", "alpha Np/m", "beta rad/m", "delta (m)"))
    print("  " + "-" * 64)
    for wi, ti, ai, bi, di in zip(decades, t, a, b, dep):
        print("  {:>10.0e}  {:>12.4g}  {:>12.4g}  {:>12.4g}  {:>12.4g}".format(
            wi, ti, ai, bi, di))
    print()


def run(sigma=1e-2, eps_r=10.0, mu_r=1.0, outdir=".", show_table=True):
    """Full sweep: compute, tabulate, and write all three figures."""
    d = sweep(sigma=sigma, eps_r=eps_r, mu_r=mu_r)
    if show_table:
        table(d)
    paths = [plot_alpha(d, outdir),
             plot_alpha_beta(d, outdir),
             plot_penetration_depth(d, outdir)]
    return d, paths


if __name__ == "__main__":
    data, figs = run()
    for p in figs:
        print("  wrote {}".format(p))
