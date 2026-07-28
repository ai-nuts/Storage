#!/usr/bin/env python3
"""Generate faithful illustrative figures for the paper2blog article.

Every figure is drawn directly from the paper's own mathematics or its own
named examples — nothing is fabricated:

  fig_landscapes.png  : the two non-convex loss examples the paper names on
                        p.8, y = sin^2(x) and y = (x-1)(x-2)(x-3)(x-4), with
                        their stationary sets marked. Illustrates the setting
                        the convergence theorems cover.
  fig_momentum.png    : the momentum-dependent multiplier 1/(1-alpha)^2 that
                        controls the exponent of the mSGD rate
                        O(T^{-s/(p(1-alpha)^2)}); equals 1 at alpha=0 (recovers
                        SGD) and grows as alpha -> 1 (faster decay). This is the
                        paper's analytic "ablation" on momentum.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#1b2431"
GRID = "#d9dee6"
BLUE = "#2f6fb0"
AMBER = "#c8791f"
RED = "#b23b3b"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 1.0,
    "figure.dpi": 200,
})


def fig_landscapes() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.5))

    # y = sin^2(x)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1200)
    y = np.sin(x) ** 2
    ax = axes[0]
    ax.plot(x, y, color=BLUE, lw=2.2)
    # stationary points of sin^2: where sin(2x)=0 -> x = k*pi/2
    ks = np.arange(-4, 5)
    sx = ks * np.pi / 2
    sy = np.sin(sx) ** 2
    ax.scatter(sx, sy, color=RED, s=28, zorder=5)
    ax.set_title(r"$y=\sin^2(x)$", fontsize=13, pad=8)
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"$g(\theta)$")
    ax.set_ylim(-0.15, 1.25)

    # y = (x-1)(x-2)(x-3)(x-4)
    x2 = np.linspace(0.4, 4.6, 1200)
    y2 = (x2 - 1) * (x2 - 2) * (x2 - 3) * (x2 - 4)
    ax = axes[1]
    ax.plot(x2, y2, color=AMBER, lw=2.2)
    # stationary points: derivative roots (two minima ~ 1.38,3.62 and a local max ~2.5)
    roots = [1.3820, 2.5, 3.6180]
    rx = np.array(roots)
    ry = (rx - 1) * (rx - 2) * (rx - 3) * (rx - 4)
    ax.scatter(rx, ry, color=RED, s=28, zorder=5)
    ax.set_title(r"$y=(x-1)(x-2)(x-3)(x-4)$", fontsize=13, pad=8)
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"$g(\theta)$")

    for ax in axes:
        ax.grid(True, color=GRID, lw=0.8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.axhline(0, color=INK, lw=0.8, alpha=0.5)

    # single shared legend for the stationary markers
    handle = axes[0].scatter([], [], color=RED, s=28, label="stationary points")
    fig.legend(handles=[handle], loc="lower center", ncol=1, frameon=False,
               bbox_to_anchor=(0.5, -0.02), fontsize=11)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(OUT / "fig_landscapes.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def fig_momentum() -> None:
    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    a = np.linspace(0.0, 0.95, 500)
    mult = 1.0 / (1.0 - a) ** 2
    ax.plot(a, mult, color=BLUE, lw=2.4)

    # anchor markers: alpha=0 (SGD) and alpha=0.9 (common practice)
    for av, label, col in [(0.0, r"$\alpha=0$ (SGD), $\times1$", RED), (0.9, r"$\alpha=0.9$, $\times100$", AMBER)]:
        mv = 1.0 / (1.0 - av) ** 2
        ax.scatter([av], [mv], color=col, s=48, zorder=6)
        ax.annotate(label, (av, mv), textcoords="offset points",
                    xytext=(12, 12) if av == 0 else (-12, -6), fontsize=11, color=col,
                    ha="left" if av == 0 else "right", va="bottom" if av == 0 else "top")

    ax.set_xlabel(r"momentum coefficient  $\alpha$")
    ax.set_ylabel(r"rate-exponent multiplier  $1/(1-\alpha)^2$")
    ax.set_title(r"Larger $\alpha$ enlarges the exponent of the mSGD rate", fontsize=12.5, pad=8)
    ax.set_xlim(0, 0.96)
    ax.set_ylim(0, 120)
    ax.grid(True, color=GRID, lw=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axhline(1.0, color=INK, lw=0.9, ls="--", alpha=0.6)
    ax.text(0.02, 4, "baseline = 1 (SGD rate)", fontsize=9.5, color=INK, alpha=0.7)
    fig.tight_layout()
    fig.savefig(OUT / "fig_momentum.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig_landscapes()
    fig_momentum()
    print("wrote:", sorted(p.name for p in OUT.glob("fig_*.png")))
