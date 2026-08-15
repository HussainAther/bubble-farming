from __future__ import annotations
import numpy as np


def spatial_variance(C: np.ndarray) -> float:
    return float(np.var(C))


def coeff_of_variation(C: np.ndarray, eps: float = 1e-12) -> float:
    mu = float(np.mean(C))
    sigma = float(np.std(C))
    return float(sigma / (mu + eps))
