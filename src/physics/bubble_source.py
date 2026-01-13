from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class BubbleSource:
    """Smooth (Gaussian) bubble injection source term."""
    x: float
    y: float
    rate: float
    sigma: float = 2.0

    def field(self, shape: tuple[int, int]) -> np.ndarray:
        h, w = shape
        yy, xx = np.mgrid[0:h, 0:w]
        dx2 = (xx - self.x) ** 2
        dy2 = (yy - self.y) ** 2
        kernel = np.exp(-(dx2 + dy2) / (2.0 * self.sigma ** 2))
        s = kernel.sum()
        return kernel / s if s > 0 else np.zeros(shape, dtype=float)

    def source_term(self, shape: tuple[int, int]) -> np.ndarray:
        return self.rate * self.field(shape)
