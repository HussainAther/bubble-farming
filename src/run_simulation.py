from __future__ import annotations
import argparse
import numpy as np
import matplotlib.pyplot as plt

from src.physics.bubble_source import BubbleSource
from src.physics.transport import run_simulation
from src.metrics.dispersion import spatial_variance


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Bubble-field diffusion simulation (2D).")
    p.add_argument("--H", type=int, default=80)
    p.add_argument("--W", type=int, default=120)
    p.add_argument("--steps", type=int, default=400)
    p.add_argument("--D", type=float, default=0.15)
    p.add_argument("--dt", type=float, default=1.0)
    p.add_argument("--uptake_k", type=float, default=0.0)
    p.add_argument("--out", type=str, default="out_stack.npy")
    p.add_argument("--plot", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    shape = (args.H, args.W)

    sources = [
        BubbleSource(x=args.W * 0.25, y=args.H * 0.6, rate=0.08, sigma=2.5),
        BubbleSource(x=args.W * 0.75, y=args.H * 0.6, rate=0.08, sigma=2.5),
    ]

    stack = run_simulation(
        shape, steps=args.steps, D=args.D, dt=args.dt, sources=sources, uptake_k=args.uptake_k
    )
    np.save(args.out, stack)

    var_series = np.array([spatial_variance(stack[t]) for t in range(stack.shape[0])])
    print(f"Saved: {args.out}")
    print(f"Final mean={stack[-1].mean():.6f}, final var={var_series[-1]:.6f}")

    if args.plot:
        plt.figure()
        plt.imshow(stack[-1], aspect="auto")
        plt.title("Final concentration field")
        plt.colorbar()
        plt.show()

        plt.figure()
        plt.plot(var_series)
        plt.title("Spatial variance vs time")
        plt.xlabel("t")
        plt.ylabel("var(C)")
        plt.show()


if __name__ == "__main__":
    main()
