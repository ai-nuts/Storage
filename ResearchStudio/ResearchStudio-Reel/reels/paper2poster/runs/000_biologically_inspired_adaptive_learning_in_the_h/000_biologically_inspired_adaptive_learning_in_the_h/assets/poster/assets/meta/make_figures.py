#!/usr/bin/env python3
"""Generate clean conceptual schematic figures for the paper2blog article.

The source paper is a conceptual/position piece with ZERO figures. These are
original explanatory diagrams of the framework the paper *describes* (biology ->
SO-model modifications). They contain no fabricated experimental data — only the
schematic relationships and equations the paper states in prose.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Restrained editorial palette: dark ink + one cool accent + warm accent.
INK = "#1b2430"
MUTED = "#5b6673"
BIO = "#2f6f8f"      # cool teal — biology
BIO_BG = "#eaf2f6"
MOD = "#b4632a"      # warm ochre — model modification
MOD_BG = "#f7efe6"
LINE = "#9aa6b2"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "svg.fonttype": "none",
    "figure.dpi": 200,
})


def rbox(ax, x, y, w, h, text, face, edge, tcolor, fs=12, bold=False, align="center"):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.03",
        linewidth=1.4, edgecolor=edge, facecolor=face, zorder=2,
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2, y + h / 2, text,
        ha="center", va="center", fontsize=fs, color=tcolor,
        fontweight="bold" if bold else "normal", zorder=3, wrap=True,
    )


def arrow(ax, x0, y0, x1, y1, color=LINE, lw=1.8, style="-|>"):
    ax.add_patch(FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle=style, mutation_scale=15,
        linewidth=lw, color=color, zorder=1,
        connectionstyle="arc3,rad=0.0",
    ))


# ---------------------------------------------------------------------------
# Figure 1 — Overview: three biological mechanisms -> three SO-model levers
# ---------------------------------------------------------------------------
def fig_overview():
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.6)
    ax.axis("off")

    ax.text(2.15, 5.28, "Mechanisms in living systems", ha="center",
            fontsize=12.5, color=BIO, fontweight="bold")
    ax.text(7.85, 5.28, "Modifications to the SO model", ha="center",
            fontsize=12.5, color=MOD, fontweight="bold")

    bio = [
        ("Metaplasticity", "how much a synapse\nis allowed to change"),
        ("Homeostasis", "regulation around\na set point"),
        ("Inhibition & forgetting", "damping and\ncontrolled resets"),
    ]
    mod = [
        ("Adaptive learning rate", r"$\alpha=f(w)$  or  $\alpha=f(\Delta E)$"),
        ("Modified activation rule", "oscillatory (e.g.\ntrigonometric) functions"),
        ("Enhanced modularity", "adaptive intra-/inter-\nmodule connections"),
    ]

    ys = [3.7, 2.15, 0.6]
    bw, bh = 3.1, 1.15
    lx, rx = 0.6, 6.3
    for (t, s), y in zip(bio, ys):
        rbox(ax, lx, y, bw, bh, "", BIO_BG, BIO, INK)
        ax.text(lx + bw / 2, y + bh - 0.34, t, ha="center", va="center",
                fontsize=12.5, color=INK, fontweight="bold")
        ax.text(lx + bw / 2, y + 0.36, s, ha="center", va="center",
                fontsize=10, color=MUTED)
    for (t, s), y in zip(mod, ys):
        rbox(ax, rx, y, bw, bh, "", MOD_BG, MOD, INK)
        ax.text(rx + bw / 2, y + bh - 0.34, t, ha="center", va="center",
                fontsize=12.5, color=INK, fontweight="bold")
        ax.text(rx + bw / 2, y + 0.36, s, ha="center", va="center",
                fontsize=10.5, color=MUTED)

    for y in ys:
        arrow(ax, lx + bw + 0.12, y + bh / 2, rx - 0.12, y + bh / 2,
              color=LINE, lw=2.0)

    ax.text(5.0, 5.02, "translate", ha="center", fontsize=9.5,
            color=MUTED, style="italic")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.02)
    p = OUT / "fig1_overview.png"
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    print(p)


# ---------------------------------------------------------------------------
# Figure 2 — Two flavors of metaplasticity: local (weight) vs network (energy)
# ---------------------------------------------------------------------------
def fig_metaplasticity():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.4))
    for ax in axes:
        ax.axis("off")

    # -- Panel (a): local metaplasticity, alpha = f(w) --
    a = axes[0]
    a.set_xlim(0, 10)
    a.set_ylim(0, 10)
    a.text(5, 9.5, "(a) Local metaplasticity", ha="center",
           fontsize=12.5, color=INK, fontweight="bold")
    a.text(5, 8.7, r"learning rate follows the weight:  $\alpha=f(w_{ij})$",
           ha="center", fontsize=11, color=MOD)
    # two nodes i, j with a weighted edge
    for cx, lab in [(3.0, "$s_i$"), (7.0, "$s_j$")]:
        a.add_patch(plt.Circle((cx, 5.2), 0.7, facecolor=BIO_BG,
                    edgecolor=BIO, linewidth=1.6, zorder=3))
        a.text(cx, 5.2, lab, ha="center", va="center", fontsize=13,
               color=INK, zorder=4)
    a.plot([3.7, 6.3], [5.2, 5.2], color=MOD, linewidth=3.0, zorder=2)
    a.text(5.0, 5.85, r"$w_{ij}$", ha="center", fontsize=12, color=MOD)
    a.text(5.0, 3.35,
           r"$\mathrm{d}w_{ij}=f(w_{ij})\,s_i s_j$",
           ha="center", fontsize=13.5, color=INK)
    a.text(5.0, 2.15,
           "the update strength depends\non the current weight itself",
           ha="center", fontsize=10, color=MUTED)

    # -- Panel (b): network-level metaplasticity, alpha = f(dE) --
    b = axes[1]
    b.set_xlim(0, 10)
    b.set_ylim(0, 10)
    b.text(5, 9.5, "(b) Network-level metaplasticity", ha="center",
           fontsize=12.5, color=INK, fontweight="bold")
    b.text(5, 8.7, r"learning rate follows the energy slope:  $\alpha=f(\Delta E)$",
           ha="center", fontsize=11, color=MOD)
    # energy landscape curve
    x = np.linspace(0.6, 9.4, 400)
    y = (1.35 * np.sin(0.72 * x + 0.4) + 0.35 * np.sin(1.9 * x)
         - 0.10 * x) + 4.6
    y = y + 0.9
    b.plot(x, y, color=BIO, linewidth=2.4, zorder=2)
    b.fill_between(x, y, 2.4, color=BIO_BG, zorder=1)
    # steep point (fast) and shallow point (slow)
    def yv(xx):
        return (1.35 * np.sin(0.72 * xx + 0.4) + 0.35 * np.sin(1.9 * xx)
                - 0.10 * xx) + 4.6 + 0.9
    for xx, note, col in [(2.35, "steep slope\n$\\rightarrow$ fast", MOD),
                          (6.55, "shallow\n$\\rightarrow$ slow", MUTED)]:
        b.plot([xx], [yv(xx)], "o", color=col, markersize=8, zorder=4)
        b.text(xx, yv(xx) + 1.05, note, ha="center", fontsize=9.5, color=col)
    b.text(5.0, 1.15, "learning speeds up on steep slopes,\n"
                     "slows in flat regions to avoid local minima",
           ha="center", fontsize=10, color=MUTED)

    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.03, wspace=0.12)
    p = OUT / "fig2_metaplasticity.png"
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    print(p)


# ---------------------------------------------------------------------------
# Figure 3 — Constraints scaffold degrees of freedom
# ---------------------------------------------------------------------------
def fig_constraints():
    fig, ax = plt.subplots(figsize=(9.4, 4.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.55, 5.2)
    ax.axis("off")

    ax.text(6.0, 4.85, "Constraints give shape to added degrees of freedom",
            ha="center", fontsize=13, color=INK, fontweight="bold")

    # left: unconstrained freedom -> noise (scatter)
    rng = np.random.default_rng(7)
    lx, ly, lw, lh = 0.5, 0.7, 4.4, 3.2
    ax.add_patch(FancyBboxPatch((lx, ly), lw, lh,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 linewidth=1.3, edgecolor=LINE, facecolor="#f3f4f6", zorder=1))
    px = rng.uniform(lx + 0.4, lx + lw - 0.4, 90)
    py = rng.uniform(ly + 0.4, ly + lh - 0.5, 90)
    ax.scatter(px, py, s=12, color=MUTED, alpha=0.55, zorder=2)
    ax.text(lx + lw / 2, ly - 0.66, "freedom without constraint\n"
            "$\\rightarrow$ collapses into noise",
            ha="center", fontsize=10.5, color=MUTED)

    # arrow
    arrow(ax, 5.15, 2.3, 6.85, 2.3, color=BIO, lw=2.4)
    ax.text(6.0, 2.62, "SO-model\narchitecture", ha="center", fontsize=9.5,
            color=BIO, fontweight="bold")

    # right: constrained -> channeled adaptive behavior (structured basins)
    rxb, ry, rw, rh = 7.1, 0.7, 4.4, 3.2
    ax.add_patch(FancyBboxPatch((rxb, ry), rw, rh,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 linewidth=1.4, edgecolor=BIO, facecolor=BIO_BG, zorder=1))
    xs = np.linspace(rxb + 0.35, rxb + rw - 0.35, 300)
    base = ry + 1.9
    for k, amp, col in [(0, 0.0, None)]:
        pass
    curve = base + 0.75 * np.sin(2.1 * (xs - rxb)) * np.exp(-0.02 * (xs - rxb))
    ax.plot(xs, curve, color=MOD, linewidth=2.2, zorder=3)
    # attractor markers at the minima
    for cx in [rxb + 1.15, rxb + 2.65, rxb + 4.0]:
        yy = base + 0.75 * np.sin(2.1 * (cx - rxb)) * np.exp(-0.02 * (cx - rxb))
        ax.plot([cx], [yy], "o", color=INK, markersize=6, zorder=4)
    ax.text(rxb + rw / 2, ry - 0.66, "constraint channels freedom\n"
            "$\\rightarrow$ useful adaptive behavior",
            ha="center", fontsize=10.5, color=BIO)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.06)
    p = OUT / "fig3_constraints.png"
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    print(p)


if __name__ == "__main__":
    fig_overview()
    fig_metaplasticity()
    fig_constraints()
