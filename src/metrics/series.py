# src/metrics/series.py
from __future__ import annotations
import numpy as np
from typing import Callable


def metric_over_time(stack: np.ndarray, metric_fn: Callable[[np.ndarray], float]) -> np.ndarray:
    """
    stack: (T, H, W)
    Returns: (T,) metric values
    """
    T = stack.shape[0]
    out = np.zeros(T, dtype=float)
    for t in range(T):
        out[t] = float(metric_fn(stack[t]))
    return out


def time_to_threshold(series: np.ndarray, threshold: float) -> int | None:
    """Return first index where series <= threshold."""
    idx = np.where(series <= threshold)[0]
    return int(idx[0]) if idx.size else None

