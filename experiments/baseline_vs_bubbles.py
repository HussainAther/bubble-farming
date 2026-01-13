from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt

from src.physics.bubble_source import BubbleSource
from src.physics.transport import run_simulation
from src.metrics.dispersion import spatial_variance


def main():
    H, W = 80, 120
    steps = 400
    D, dt = 0.15, 1.0

    baseline = run_simulation((H, W), steps=steps, D=D, dt=dt, sources=[])

    sources = [
        BubbleSource(x=W * 0.25, y=H * 0.6, rate=0.08, sigma=2.5),
        BubbleSource(x=W * 0.75, y=H * 0.6, rate=0.08, sigma=2.5),
    ]
    bubble = run_simulation((H, W), steps=steps, D=D, dt=dt, sources=sources)

    base_var = np.array([spatial_variance(baseline[t]) for t in range(baseline.shape[0])])
    bub_var = np.array([spatial_variance(bubble[t]) for t in range(bubble.shape[0])])

    plt.figure()
    plt.plot(base_var, label="baseline (no bubbles)")
    plt.plot(bub_var, label="bubble field")
    plt.title("Variance comparison")
    plt.xlabel("t")
    plt.ylabel("var(C)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.imshow(bubble[-1], aspect="auto")
    plt.title("Final field (bubble)")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()
