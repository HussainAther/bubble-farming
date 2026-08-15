# experiments/parameter_sweep_sources.py
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from src.physics.bubble_source import BubbleSource
from src.physics.transport import run_simulation
from src.metrics.dispersion import spatial_variance
from src.metrics.series import metric_over_time


def main():
    # Config
    H, W = 80, 120
    steps = 300
    D, dt = 0.15, 1.0

    rates = np.linspace(0.02, 0.16, 8)   # injection strength
    sigmas = np.linspace(1.0, 6.0, 8)    # spread

    # Two symmetric sources
    x1, x2 = W * 0.25, W * 0.75
    y = H * 0.6

    out_dir = Path("figures")
    out_dir.mkdir(exist_ok=True)

    # We’ll measure final variance as a simple score (lower is “more uniform”)
    final_var = np.zeros((len(sigmas), len(rates)), dtype=float)

    for i, sigma in enumerate(sigmas):
        for j, rate in enumerate(rates):
            sources = [
                BubbleSource(x=x1, y=y, rate=float(rate), sigma=float(sigma)),
                BubbleSource(x=x2, y=y, rate=float(rate), sigma=float(sigma)),
            ]
            stack = run_simulation((H, W), steps=steps, D=D, dt=dt, sources=sources)
            var_series = metric_over_time(stack, spatial_variance)
            final_var[i, j] = var_series[-1]

    # Save CSV
    csv_path = out_dir / "sweep_final_variance.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sigma\\rate"] + [f"{r:.4f}" for r in rates])
        for i, sigma in enumerate(sigmas):
            writer.writerow([f"{sigma:.4f}"] + [f"{v:.8f}" for v in final_var[i]])

    # Plot "heatmap" without seaborn (matplotlib only)
    plt.figure()
    plt.imshow(final_var, aspect="auto", origin="lower")
    plt.title("Final variance vs sigma (rows) and rate (cols)")
    plt.xlabel("rate index (low→high)")
    plt.ylabel("sigma index (low→high)")
    plt.colorbar(label="final var(C)")
    plt.tight_layout()
    fig_path = out_dir / "sweep_final_variance.png"
    plt.savefig(fig_path, dpi=160)
    plt.close()

    print(f"Saved: {csv_path}")
    print(f"Saved: {fig_path}")


if __name__ == "__main__":
    main()

