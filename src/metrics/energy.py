# src/metrics/energy.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

from src.physics.bubble_source import BubbleSource


@dataclass(frozen=True)
class EnergyModel:
    """
    Simple proxy model for injection energy. This is intentionally lightweight:
    energy_per_step ≈ pressure_factor * total_rate

    Later upgrades could include compressor curves, depth/pressure dependence,
    diffuser losses, etc.
    """
    pressure_factor: float = 1.0

    def energy_per_step(self, sources: Iterable[BubbleSource]) -> float:
        total_rate = sum(float(s.rate) for s in sources)
        return self.pressure_factor * total_rate

    def total_energy(self, sources: Iterable[BubbleSource], steps: int) -> float:
        return steps * self.energy_per_step(sources)

