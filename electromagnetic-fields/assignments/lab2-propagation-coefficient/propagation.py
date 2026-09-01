"""
Attenuation constant and phase shift coefficient for a plane wave.

    alpha = w*sqrt( (mu*eps/2)*( sqrt(1 + (sigma/(w*eps))^2) - 1 ) )
    beta  = w*sqrt( (mu*eps/2)*( sqrt(1 + (sigma/(w*eps))^2) + 1 ) )

w may be a scalar or a NumPy array.
"""

import numpy as np

# ----------------------------------------------------------------------
# Free-space constants
# ----------------------------------------------------------------------
MU0 = 4.0e-7 * np.pi            # permeability of free space   [H/m]
EPS0 = 8.8541878128e-12         # permittivity of free space   [F/m]


def medium_properties(eps_r=1.0, mu_r=1.0):
    """Absolute (mu, eps) of a medium from its relative values."""
    return mu_r * MU0, eps_r * EPS0


def loss_tangent(sigma, w, eps):
    """tan(theta) = sigma / (w * eps)   [dimensionless]."""
    w = np.asarray(w, dtype=float)
    return sigma / (w * eps)


# ----------------------------------------------------------------------
# Exact solutions -- Equations 1 and 2
# ----------------------------------------------------------------------
def alpha_exact(sigma, w, mu, eps):
    """Attenuation constant, Equation 1   [Np/m]."""
    w = np.asarray(w, dtype=float)
    t2 = loss_tangent(sigma, w, eps) ** 2
    return w * np.sqrt((mu * eps / 2.0) * (np.sqrt(1.0 + t2) - 1.0))


def beta_exact(sigma, w, mu, eps):
    """Phase shift coefficient, Equation 2   [rad/m]."""
    w = np.asarray(w, dtype=float)
    t2 = loss_tangent(sigma, w, eps) ** 2
    return w * np.sqrt((mu * eps / 2.0) * (np.sqrt(1.0 + t2) + 1.0))


def gamma_complex(sigma, w, mu, eps):
    """gamma = sqrt(j*w*mu*(sigma + j*w*eps)) in complex arithmetic."""
    w = np.asarray(w, dtype=float)
    return np.sqrt(1j * w * mu * (sigma + 1j * w * eps))


# ----------------------------------------------------------------------
# Case i -- pure (good) conductor        sigma >> w*eps
# ----------------------------------------------------------------------
def alpha_conductor(sigma, w, mu):
    """alpha = sqrt(w*mu*sigma/2)   [Np/m]."""
    w = np.asarray(w, dtype=float)
    return np.sqrt(w * mu * sigma / 2.0)


def beta_conductor(sigma, w, mu):
    """beta = alpha for a good conductor   [rad/m]."""
    return alpha_conductor(sigma, w, mu)


# ----------------------------------------------------------------------
# Case ii -- pure dielectric             sigma = 0
# ----------------------------------------------------------------------
def alpha_dielectric(w=None):
    """alpha = 0 for a lossless dielectric   [Np/m]."""
    if w is None:
        return 0.0
    return np.zeros_like(np.asarray(w, dtype=float))


def beta_dielectric(w, mu, eps):
    """beta = w*sqrt(mu*eps)   [rad/m]."""
    w = np.asarray(w, dtype=float)
    return w * np.sqrt(mu * eps)


# ----------------------------------------------------------------------
# Case iii -- lossy (low-loss) medium    sigma << w*eps
# ----------------------------------------------------------------------
def alpha_lossy(sigma, mu, eps, w=None):
    """alpha = (sigma/2)*sqrt(mu/eps)   [Np/m].

    Independent of frequency.
    """
    a = (sigma / 2.0) * np.sqrt(mu / eps)
    if w is None:
        return a
    return np.full_like(np.asarray(w, dtype=float), a)


def beta_lossy(sigma, w, mu, eps):
    """beta = w*sqrt(mu*eps)*(1 + sigma^2/(8*w^2*eps^2))   [rad/m]."""
    w = np.asarray(w, dtype=float)
    return w * np.sqrt(mu * eps) * (1.0 + (sigma ** 2) / (8.0 * w ** 2 * eps ** 2))


# ----------------------------------------------------------------------
# Derived quantities
# ----------------------------------------------------------------------
def penetration_depth(alpha):
    """Skin / penetration depth  delta = 1/alpha   [m]."""
    alpha = np.asarray(alpha, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(alpha > 0.0, 1.0 / alpha, np.inf)


def phase_velocity(w, beta):
    """u = w/beta   [m/s]."""
    w = np.asarray(w, dtype=float)
    beta = np.asarray(beta, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(beta > 0.0, w / beta, np.inf)


def wavelength(beta):
    """lambda = 2*pi/beta   [m]."""
    beta = np.asarray(beta, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(beta > 0.0, 2.0 * np.pi / beta, np.inf)
