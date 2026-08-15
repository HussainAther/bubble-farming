# experiments/tradeoff_variance_vs_energy.py
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from src.physics.bubble_source import BubbleSource
from src.physics.transport import run_simulation
from src.metrics.dispersion import spatial_variance
from src.metrics.series import metric_over_time
from src.metrics.energy import EnergyModel


def main():
    H, W = 80, 120
    steps = 300
    D, dt = 0.15, 1.0

    # Fix sigma, sweep rate
    sigma = 2.5
    rates = np.linspace(0.01, 0.20, 14)

    x1, x2 = W * 0.25, W * 0.75
    y = H * 0.6

    energy_model = EnergyModel(pressure_factor=1.0)

    energies = []
    final_vars = []

    for rate in rates:
        sources = [
            BubbleSource(x=x1, y=y, rate=float(rate), sigma=float(sigma)),
            BubbleSource(x=x2, y=y, rate=float(rate), sigma=float(sigma)),
        ]
        stack = run_simulation((H, W), steps=steps, D=D, dt=dt, sources=sources)
        var_series = metric_over_time(stack, spatial_variance)

        E = energy_model.total_energy(sources, steps=steps)
        energies.append(E)
        final_vars.append(var_series[-1])

    energies = np.array(energies, dtype=float)
    final_vars = np.array(final_vars, dtype=float)

    out_dir = Path("figures")
    out_dir.mkdir(exist_ok=True)

    plt.figure()
    plt.plot(energies, final_vars, marker="o")
    plt.title("Tradeoff: energy proxy vs final variance")
    plt.xlabel("total energy proxy")
    plt.ylabel("final var(C)")
    plt.tight_layout()
    fig_path = out_dir / "tradeoff_energy_vs_variance.png"
    plt.savefig(fig_path, dpi=160)
    plt.close()

    print(f"Saved: {fig_path}")


if __name__ == "__main__":
    main()

