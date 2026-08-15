from __future__ import annotations
import numpy as np
from typing import Iterable
from .bubble_source import BubbleSource


def laplacian_2d(C: np.ndarray) -> np.ndarray:
    """5-point Laplacian with edge padding (reflective-ish boundaries)."""
    Cp = np.pad(C, pad_width=1, mode="edge")
    return (
        Cp[1:-1, 0:-2] + Cp[1:-1, 2:] + Cp[0:-2, 1:-1] + Cp[2:, 1:-1]
        - 4.0 * Cp[1:-1, 1:-1]
    )


def step_diffusion(
    C: np.ndarray,
    D: float,
    dt: float,
    uptake_k: float = 0.0,
    sources: Iterable[BubbleSource] = (),
) -> np.ndarray:
    """
    Explicit Euler step:
      dC/dt = D ∇²C + Σ S_i(x) - uptake_k * C
    """
    dC = D * laplacian_2d(C)

    S = np.zeros_like(C, dtype=float)
    for src in sources:
        S += src.source_term(C.shape)

    uptake = -uptake_k * C if uptake_k > 0 else 0.0

    C_next = C + dt * (dC + S + uptake)
    return np.clip(C_next, 0.0, None)


def run_simulation(
    shape: tuple[int, int],
    steps: int,
    D: float,
    dt: float,
    sources: Iterable[BubbleSource] = (),
    uptake_k: float = 0.0,
    C0: np.ndarray | None = None,
) -> np.ndarray:
    """Returns (steps+1, H, W) concentration stack."""
    C = np.zeros(shape, dtype=float) if C0 is None else C0.astype(float, copy=True)

    stack = np.zeros((steps + 1, shape[0], shape[1]), dtype=float)
    stack[0] = C
    for t in range(1, steps + 1):
        C = step_diffusion(C, D=D, dt=dt, uptake_k=uptake_k, sources=sources)
        stack[t] = C
    return stack
