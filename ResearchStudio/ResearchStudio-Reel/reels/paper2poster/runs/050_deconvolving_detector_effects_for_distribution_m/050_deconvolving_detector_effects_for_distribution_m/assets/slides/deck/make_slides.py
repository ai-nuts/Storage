#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video (Moment Unfolding, NeurIPS ML4PS 2022).

Each required narration chunk is wrapped in its own <g id="cue_..."> card whose
<title> carries the narration keywords, so the strict cue matcher resolves every
anchor from PPTX geometry. Zero <image> elements -> no image gates fire.
"""
import json, os, html, math

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CONTRACT = os.path.join(RUN, "assets", "meta", "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720

# ---- theme (matches spec_lock.md) ------------------------------------------
BG      = "#0B1220"
BG2     = "#0E1A30"
CARD    = "#14223C"
CARD2   = "#1A2B49"
STROKE  = "#2B4068"
INK     = "#EAF1FB"
SUB     = "#A6BADB"
MUT     = "#6E85AC"
ACCENT  = "#4F9DF7"   # cobalt
TEAL    = "#37DCC0"   # secondary accent
WARM    = "#F7B84B"   # headline numbers
GREEN   = "#57D9A3"   # success
RED     = "#F2708A"   # danger

SANS = "Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO = "Consolas, 'SF Mono', 'Courier New', monospace"

# ---- contract --------------------------------------------------------------
_c = json.load(open(CONTRACT))
A = {}
for s in _c["slides"]:
    A[s["id"]] = s["chunks"]

def anchor(sid, ci):
    ch = A[sid][ci]
    return ch["anchor_id"], " ".join(ch["cue_keywords"])

# ---- svg helpers -----------------------------------------------------------
def esc(t):
    return html.escape(str(t), quote=True)

def T(x, y, s, size=16, fill=INK, weight=400, family=SANS, anchor="start",
      italic=False, spacing=None, opacity=None):
    a = [f'x="{x}"', f'y="{y}"', f'font-family="{family}"',
         f'font-size="{size}"', f'font-weight="{weight}"', f'fill="{fill}"',
         f'text-anchor="{anchor}"']
    if italic: a.append('font-style="italic"')
    if spacing is not None: a.append(f'letter-spacing="{spacing}"')
    if opacity is not None: a.append(f'opacity="{opacity}"')
    return f'<text {" ".join(a)}>{esc(s)}</text>'

def wrap(text, maxchars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxchars:
            cur = (cur + " " + w).strip()
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def paragraph(x, y, text, size=15, fill=SUB, maxchars=44, lh=21, weight=400,
              family=SANS, maxlines=None):
    ls = wrap(text, maxchars)
    if maxlines: ls = ls[:maxlines]
    return "\n".join(T(x, y + i * lh, ln, size, fill, weight, family)
                     for i, ln in enumerate(ls))

def rrect(x, y, w, h, fill=CARD, stroke=STROKE, rx=14, sw=1.2, opacity=None):
    op = f' opacity="{opacity}"' if opacity is not None else ""
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" fill="{fill}"{st}{op} />'

def tick(x, y, h=26, w=5, fill=ACCENT):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="{fill}" />'

def cue(anchor_id, keywords, desc, body):
    return (f'<g id="{anchor_id}">\n'
            f'  <title>{esc(keywords)}</title>\n'
            f'  <desc>{esc(desc)}</desc>\n'
            f'{body}\n</g>')

# ---- frame -----------------------------------------------------------------
def frame(eyebrow, title, sub=None, idx=None):
    b = []
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}" />')
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bgv)" />')
    b.append(tick(56, 50, h=22, w=6, fill=ACCENT))
    b.append(T(74, 68, eyebrow.upper(), 15, ACCENT, 700, SANS, spacing=3))
    b.append(T(56, 116, title, 40, INK, 800))
    if sub:
        b.append(T(58, 146, sub, 17, SUB, 400))
    if idx:
        b.append(T(W - 56, 68, idx, 14, MUT, 700, MONO, anchor="end", spacing=1))
    yline = 160 if sub else 138
    b.append(f'<line x1="56" y1="{yline}" x2="{W-56}" y2="{yline}" stroke="{STROKE}" stroke-width="1.2" />')
    return "\n".join(b), (yline + 22)

def svg_doc(body):
    defs = f'''<defs>
  <radialGradient id="bgv" cx="18%" cy="8%" r="100%">
    <stop offset="0%" stop-color="{BG2}" stop-opacity="0.9"/>
    <stop offset="60%" stop-color="{BG}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="warmg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{WARM}"/>
    <stop offset="100%" stop-color="#E8892E"/>
  </linearGradient>
</defs>'''
    return (f"<?xml version='1.0' encoding='UTF-8'?>\n"
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}">\n{defs}\n{body}\n</svg>\n')

def write(name, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg_doc(body))
    print("wrote", name)

# ===========================================================================
# Slide 1 - Title
# ===========================================================================
def s01():
    sid = "title"; b = []
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}" />')
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bgv)" />')
    # kicker (chunk 1: unfolding corrects detector distortions)
    a0, k0 = anchor(sid, 0)
    body = []
    body.append(tick(72, 92, h=30, w=6, fill=ACCENT))
    body.append(T(92, 104, "COLLIDER PHYSICS · UNFOLDING · MACHINE LEARNING", 15, ACCENT, 700, SANS, spacing=2.5))
    body.append(T(92, 134, "Comparing collider data with theory means undoing the distortions detectors imprint on the data.", 15.5, SUB, 400))
    b.append(cue(a0, k0, "Comparing collider measurements with theory requires unfolding detector distortions.", "\n".join(body)))
    # title block
    b.append(T(72, 208, "Moment Unfolding", 58, INK, 800))
    b.append(T(72, 250, "Deconvolving Detector Effects for Distribution Moments", 23, SUB, 500))
    # chunk 2: the mismatch card (histograms vs moments)
    a1, k1 = anchor(sid, 1)
    body = []
    body.append(rrect(72, 286, 596, 118, CARD, STROKE, rx=16))
    body.append(tick(92, 308, h=74, w=6, fill=WARM))
    body.append(T(112, 326, "The mismatch", 18, WARM, 800))
    body.append(T(112, 356, "Most unfolding methods first bin the data into", 15, SUB))
    body.append(T(112, 378, "histograms — but many theory predictions live at", 15, SUB))
    body.append(T(112, 400, "the level of statistical moments.", 15, SUB))
    b.append(cue(a1, k1, "Most unfolding methods first bin data into histograms while theory predictions live at moments.", "\n".join(body)))
    # chunk 3: method name card
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(692, 286, 516, 118, CARD2, ACCENT, rx=16, sw=1.4))
    body.append(tick(712, 308, h=74, w=6, fill=TEAL))
    body.append(T(732, 326, "Moment Unfolding", 20, TEAL, 800))
    body.append(T(732, 358, "A machine-learning method that directly", 15, INK, 500))
    body.append(T(732, 380, "unfolds distribution moments —", 15, INK, 500))
    body.append(T(732, 402, "without ever binning the data.", 15, INK, 600))
    b.append(cue(a2, k2, "This paper introduces Moment Unfolding directly unfolds distribution moments without binning.", "\n".join(body)))
    # chunk 4: inspiration + accuracy hero card
    a3, k3 = anchor(sid, 3)
    body = []
    body.append(rrect(72, 424, W-144, 96, CARD, STROKE, rx=16))
    body.append(tick(92, 446, h=52, w=6, fill=GREEN))
    body.append(T(112, 466, "Inspired by GANs and Boltzmann's statistical mechanics", 17, INK, 700))
    body.append(T(112, 496, "Recovers moments to sub-percent accuracy on both Gaussian toy data and simulated LHC jets.", 15, SUB))
    body.append(T(W-96, 470, "sub-%", 34, GREEN, 800, anchor="end"))
    body.append(T(W-96, 496, "moment accuracy", 12.5, SUB, anchor="end"))
    b.append(cue(a3, k3, "Inspired by generative adversarial networks and Boltzmann recovers moments sub-percent Gaussian LHC jets.", "\n".join(body)))
    # authors / venue footer band
    b.append(f'<line x1="72" y1="548" x2="{W-72}" y2="548" stroke="{STROKE}" stroke-width="1.2" />')
    b.append(T(72, 584, "Krish Desai   ·   Benjamin Nachman   ·   Jesse Thaler", 21, INK, 700))
    b.append(T(72, 610, "UC Berkeley  ·  Lawrence Berkeley National Laboratory  ·  MIT  ·  NSF AI Institute (IAIFI)", 14.5, SUB))
    b.append(T(72, 646, "NeurIPS 2022 · ML4PS Workshop", 14, ACCENT, 700, SANS, spacing=1.2))
    b.append(T(72, 670, "github.com/hep-lbdl/MomentUnfolding", 14, MUT, 500, MONO))
    write("01_title.svg", "\n".join(b))

# ===========================================================================
# Slide 2 - Problem
# ===========================================================================
def s02():
    sid = "problem"
    head, y0 = frame("Problem", "Binning gets in the way of moments", idx="02 / 10")
    b = [head]
    # chunk 1: unfolding = deconvolution intro (full-width card)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 92, CARD, STROKE)]
    body.append(tick(76, y0+22, h=48))
    body.append(T(96, y0+38, "Unfolding (deconvolution) corrects detector distortions", 20, INK, 700))
    body.append(T(96, y0+66, "so different experiments can be compared with one another — and with theory.", 15, SUB))
    b.append(cue(a0, k0, "Unfolding also known as deconvolution corrects distortions detector imprints compared theory.", "\n".join(body)))
    # three problem cards
    cy = y0 + 112
    cw = (W - 112 - 2*24) / 3
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    ch = 300
    # chunk 2: usual recipe (histogram then moments)
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=WARM))
    body.append(T(x+22, cy+80, "The usual recipe", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Unfold the entire spectrum after first discretizing it into a histogram, then compute moments from that histogram.", 15, SUB, maxchars=34))
    # mini histogram glyph
    hx, hy, hw = x+30, cy+250, cw-60
    for i, hh in enumerate([18, 30, 42, 34, 22, 14]):
        bx = hx + i*(hw/6.0)
        body.append(f'<rect x="{bx:.0f}" y="{hy-hh}" width="{hw/6.0-6:.0f}" height="{hh}" rx="2" fill="{WARM}" opacity="0.75"/>')
    body.append(T(x+22, cy+ch-14, "spectrum → histogram → moments", 12.5, MUT, 600, MONO))
    b.append(cue(a1, k1, "Usual recipe unfolds entire spectrum first discretizing histogram then computes moments.", "\n".join(body)))
    # chunk 3: binning artifacts + wasteful
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+80, "Binning hurts", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Discretization introduces artifacts, and it is wasteful when all you want is a small set of moments.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+204, cw-44, 68, "#301B27", RED, rx=12, sw=1.2))
    body.append(T(x+38, cy+238, "artifacts + wasted effort", 15, RED, 800))
    body.append(T(x+38, cy+260, "for just a few moments", 13, SUB))
    b.append(cue(a2, k2, "But binning step introduces discretization artifacts wasteful small set moments observable.", "\n".join(body)))
    # chunk 4: the gap closed
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(x+22, cy+26, h=30, fill=ACCENT))
    body.append(T(x+22, cy+80, "The gap", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Binned data on one side, moment-level theory predictions on the other. This paper closes that mismatch.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+204, cw-44, 68, "#16283F", ACCENT, rx=12, sw=1.2))
    body.append(T(x+38, cy+238, "binned data  ≠  moment theory", 13.5, ACCENT, 800))
    body.append(T(x+38, cy+260, "the gap this paper closes", 13, SUB))
    b.append(cue(a3, k3, "That mismatch between binned data moment-level theory predictions gap this paper closes.", "\n".join(body)))
    write("02_problem.svg", "\n".join(b))

# ===========================================================================
# Slide 3 - Motivation
# ===========================================================================
def s03():
    sid = "motivation"
    head, y0 = frame("Motivation", "Why unfold moments directly?", idx="03 / 10")
    b = [head]
    lw = 616; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # left: moments are tractable + predictable (chunks 1 & 2)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, lw, 168, CARD, STROKE)]
    body.append(tick(76, y0+22, h=30))
    body.append(T(96, y0+40, "A few moments make a distribution tractable", 18, INK, 700))
    body.append(paragraph(96, y0+70, "Summarizing a distribution by a handful of moments makes it easy to visualize and, crucially, to predict from first principles.", 14.5, SUB, maxchars=64))
    body.append(rrect(96, y0+118, lw-80, 34, BG2, "", rx=9))
    body.append(T(110, y0+140, "mean  ·  variance  ·  skewness  ·  …  →  visualize + predict", 14, TEAL, 600, MONO))
    b.append(cue(a0, k0, "Summarizing distribution few moments tractable visualize predict from first principles.", "\n".join(body)))
    a1, k1 = anchor(sid, 1)
    yy = y0+188
    body = [rrect(56, yy, lw, 120, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(76, yy+24, h=72, fill=TEAL))
    body.append(T(96, yy+44, "Hadronic jets: densities are out of reach", 18, INK, 700))
    body.append(paragraph(96, yy+72, "Full jet densities cannot be computed in perturbative QCD — but the energy dependence of their moments can be.", 14.5, SUB, maxchars=64))
    b.append(cue(a1, k1, "Full densities hadronic jets cannot computed perturbative QCD energy dependence moments can.", "\n".join(body)))
    # right: existing unbinned methods trade away precision (chunks 3 & 4)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, y0, rw, 168, CARD, RED, rx=14, sw=1.2)]
    body.append(tick(rx0+20, y0+22, h=30, fill=RED))
    body.append(T(rx0+40, y0+40, "Unbinned methods exist, but…", 17, RED, 700))
    body.append(paragraph(rx0+20, y0+72, "They avoid binning artifacts, yet are built to unfold entire spectra — so they may trade away precision on the few moments you want.", 14.5, SUB, maxchars=48))
    b.append(cue(a2, k2, "Unbinned unfolding methods already exist avoid binning artifacts entire spectra trade precision moments.", "\n".join(body)))
    a3, k3 = anchor(sid, 3)
    yy = y0+188
    body = [rrect(rx0, yy, rw, 120, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(rx0+20, yy+24, h=72, fill=ACCENT))
    body.append(T(rx0+40, yy+44, "A dedicated method", 17, ACCENT, 700))
    body.append(paragraph(rx0+40, yy+72, "This motivates unfolding the moments themselves, rather than reconstructing an entire spectrum first.", 14.5, SUB, maxchars=46))
    b.append(cue(a3, k3, "This motivates dedicated method unfolds moments themselves.", "\n".join(body)))
    write("03_motivation.svg", "\n".join(b))

# ===========================================================================
# Slide 4 - Contribution
# ===========================================================================
def s04():
    sid = "contribution"
    head, y0 = frame("Contribution", "What Moment Unfolding delivers", idx="04 / 10")
    b = [head]
    cw = (W - 112 - 24) / 2; ch = 170
    xs = [56, 56+cw+24]; ys = [y0, y0+ch+22]
    specs = [
        (0, xs[0], ys[0], "01", ACCENT, "Unbinned & non-iterative",
         "A new reweighting technique that never bins the data and does not iterate to convergence."),
        (1, xs[1], ys[0], "02", TEAL, "Boltzmann-form generator",
         "Learns a reweighting function — a GAN generator — whose trainable parameters ARE the moments."),
        (2, xs[0], ys[1], "03", GREEN, "Adversarial discriminator",
         "A discriminator pushes the reweighted simulation to match the target data."),
        (3, xs[1], ys[1], "04", WARM, "Trained once, not per-iteration",
         "Unlike OmniFold, which retrains a fresh network pair each iteration, this trains one pair a single time."),
    ]
    for ci, x, y, num, col, title, txt in specs:
        a, k = anchor(sid, ci)
        body = [rrect(x, y, cw, ch, CARD, STROKE)]
        body.append(tick(x+24, y+28, h=34, fill=col))
        body.append(T(x+cw-24, y+52, num, 40, col, 800, MONO, anchor="end", opacity=0.55))
        body.append(T(x+44, y+50, title, 21, INK, 700))
        body.append(paragraph(x+44, y+84, txt, 15, SUB, maxchars=54))
        b.append(cue(a, k, txt, "\n".join(body)))
    write("04_contribution.svg", "\n".join(b))

# ===========================================================================
# Slide 5 - Method
# ===========================================================================
def s05():
    sid = "method"
    head, y0 = frame("Method", "A GAN whose weights are the moments", idx="05 / 10")
    b = [head]
    # chunk 1: Boltzmann generator (equation band)
    a0, k0 = anchor(sid, 0)
    eqh = 116
    body = [rrect(56, y0, W-112, eqh, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(76, y0+30, "Boltzmann max-entropy generator — the coefficients ARE the moments", 15, ACCENT, 700))
    body.append(T(76, y0+80, "w(x) = exp( λ₁·x + λ₂·x² + … + λₙ·xⁿ )", 27, INK, 700, MONO))
    body.append(T(W-76, y0+80, "λ = moments", 16, TEAL, 700, MONO, anchor="end"))
    b.append(cue(a0, k0, "Method borrows Boltzmann idea building distribution maximizes entropy fixed moments exponential polynomial lambdas.", "\n".join(body)))
    # bottom: three step cards
    cy = y0 + eqh + 22
    cw = (W - 112 - 2*22) / 3; ch = 214
    xs = [56, 56+cw+22, 56+2*(cw+22)]
    # chunk 2: generator reweights, discriminator distinguishes
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "1  Generator reweights", 17, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "The generator reweights the simulated events; a discriminator network tries to tell reweighted simulation from real data.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+162, cw-44, 34, BG2, "", rx=9))
    body.append(T(x+36, cy+184, "sim · w(x)  vs.  real data", 13.5, TEAL, 600, MONO))
    b.append(cue(a1, k1, "This generator reweights simulated events discriminator neural network tell reweighted simulation apart real data.", "\n".join(body)))
    # chunk 3: adversarial weighted BCE loss
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "2  Adversarial training", 17, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "The two play a minimax game on a weighted binary cross-entropy loss: the discriminator minimizes it, the generator maximizes it.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+162, cw-44, 34, BG2, "", rx=9))
    body.append(T(x+36, cy+184, "min_D  max_G   weighted BCE", 13, INK, 600, MONO))
    b.append(cue(a2, k2, "Two trained against each other weighted binary cross-entropy discriminator minimizes generator maximizes.", "\n".join(body)))
    # chunk 4: detector emulation runs once
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD2, GREEN, rx=14, sw=1.2)]
    body.append(T(x+22, cy+40, "3  Emulate detector once", 17, GREEN, 700))
    body.append(paragraph(x+22, cy+70, "Reweighting changes only importance weights, not the event features — so the expensive detector emulation runs a single time.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+162, cw-44, 34, "#14261F", GREEN, rx=9, sw=1.1))
    body.append(T(x+36, cy+184, "detector sim  ×1  (not per step)", 12.5, GREEN, 600, MONO))
    b.append(cue(a3, k3, "Because reweighting only changes importance weights not event features expensive detector emulation runs single time.", "\n".join(body)))
    write("05_method.svg", "\n".join(b))

# ===========================================================================
# Slide 6 - Dataset / Benchmark
# ===========================================================================
def s06():
    sid = "dataset-benchmark"
    head, y0 = frame("Benchmarks", "Two problems: a toy and real jets", idx="06 / 10")
    b = [head]
    # chunk 1: two problems intro
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 62, CARD, STROKE)]
    body.append(tick(76, y0+16, h=30, fill=TEAL))
    body.append(T(96, y0+40, "The method is tested on two very different problems", 19, INK, 700))
    b.append(cue(a0, k0, "The method is tested on two problems.", "\n".join(body)))
    cy = y0 + 82
    # left big card: Gaussian toy (chunks 2 & 3)
    lw = 636; ch = 292; x = 56
    a1, k1 = anchor(sid, 1)
    body = [rrect(x, cy, lw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=30, fill=ACCENT))
    body.append(T(x+40, cy+44, "Gaussian toy", 20, INK, 800))
    body.append(T(x+40, cy+68, "truth N(0,1) · generation shifted to mean −½ · wide Gaussian detector noise", 13.5, ACCENT, 600))
    # native schematic: truth curve, shifted curve, smeared curve
    gx, gy, gw, gh = x+40, cy+96, lw-80, 96
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.1"/>')
    def gauss(mu, sig, col, dash="", peak=0.9):
        pts = []
        for i in range(61):
            u = -3 + 6*i/60.0
            v = math.exp(-0.5*((u-mu)/sig)**2)
            px = gx + (u+3)/6.0*gw
            py = gy + gh - v*gh*peak
            pts.append(f"{px:.1f},{py:.1f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.4"{d}/>'
    body.append(gauss(0.0, 0.62, GREEN))                 # truth
    body.append(gauss(-0.5, 0.62, ACCENT, dash="5 4"))   # shifted generation
    body.append(gauss(-0.5, 1.15, WARM, dash="2 4", peak=0.55))  # detector-smeared
    body.append(T(gx+4, cy+114, "truth N(0,1)", 12, GREEN, 700))
    body.append(T(gx+4, cy+132, "gen shifted −½", 12, ACCENT, 700))
    body.append(T(gx+4, cy+150, "+ detector noise", 12, WARM, 700))
    # chunk 3 sub-band: finitely many moments
    a2, k2 = anchor(sid, 2)
    body2 = [rrect(x+22, cy+ch-58, lw-44, 40, BG2, "", rx=9)]
    body2.append(T(x+38, cy+ch-32, "Gaussian → finitely many moments  ⇒  unfolding its moments = unfolding the whole density", 13.5, TEAL, 600))
    b.append(cue(a1, k1, "First Gaussian toy truth standard normal generation shifted mean detector wide Gaussian noise million samples.",
                 "\n".join(body) + "\n" + T(x+40, cy+206, "1,000,000 samples · 3 : 1 train / test split", 14, INK, 600)))
    b.append(cue(a2, k2, "Because Gaussian only finitely many moments unfolding moments equivalent unfolding whole density.", "\n".join(body2)))
    # right card: LHC jets (chunk 4)
    a3, k3 = anchor(sid, 3)
    rx0 = x+lw+24; rw = W-56-rx0
    body = [rrect(rx0, cy, rw, ch, CARD2, WARM, rx=14, sw=1.3)]
    body.append(tick(rx0+22, cy+24, h=30, fill=WARM))
    body.append(T(rx0+40, cy+44, "Hadronic LHC jets", 20, INK, 800))
    body.append(paragraph(rx0+22, cy+80, "Simulated LHC collisions, using the jet-width observable, drawn from the same Pythia and Herwig + Delphes datasets as the OmniFold paper.", 14, SUB, maxchars=40))
    body.append(rrect(rx0+22, cy+188, rw-44, 82, BG2, "", rx=10))
    body.append(T(rx0+38, cy+214, "observable:  jet width", 14, WARM, 700, MONO))
    body.append(T(rx0+38, cy+240, "Pythia = 'data'", 13.5, INK, 600))
    body.append(T(rx0+38, cy+260, "Herwig = synthetic reference", 13.5, INK, 600))
    b.append(cue(a3, k3, "Second hadronic jets simulated LHC collisions jet width Pythia Herwig Delphes OmniFold one simulation data other reference.", "\n".join(body)))
    write("06_dataset-benchmark.svg", "\n".join(b))

# ===========================================================================
# Slide 7 - Key Result
# ===========================================================================
def s07():
    sid = "key-result"
    head, y0 = frame("Key Result", "Moments recovered to sub-percent accuracy", idx="07 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD2, GREEN, rx=12, sw=1.2)]
    body.append(T(76, y0+37, "Strong results on both tasks — the loss peaks land exactly on the true moments.", 18, INK, 700))
    b.append(cue(a0, k0, "Results strong both tasks Gaussian loss function peaks exactly true mean discriminator converges ten epochs.", "\n".join(body)))
    cy = y0 + 80
    # left chart: loss scan peaking at true value
    a1, k1 = anchor(sid, 1)
    cw1 = 596; ch = 296; x = 56
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(T(x+24, cy+40, "Loss scanned over a candidate moment", 17, INK, 700))
    body.append(T(x+cw1-24, cy+40, "peak = true value", 13, GREEN, 700, anchor="end"))
    gx, gy, gw, gh = x+56, cy+70, cw1-96, 150
    body.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(T(gx-8, gy+6, "loss", 11.5, MUT, 600, anchor="end"))
    body.append(T(gx+gw, gy+gh+18, "candidate moment", 11.5, MUT, 600, anchor="end"))
    # inverted-parabola peak at center
    pts = []
    for i in range(61):
        t = i/60.0
        v = math.exp(-((t-0.5)**2)/(2*0.11**2))
        px = gx + t*gw
        py = gy + gh - v*(gh-12)
        pts.append(f"{px:.1f},{py:.1f}")
    body.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACCENT}" stroke-width="2.8"/>')
    # true-value marker
    mx = gx + 0.5*gw
    body.append(f'<line x1="{mx}" y1="{gy}" x2="{mx}" y2="{gy+gh}" stroke="{GREEN}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    body.append(f'<circle cx="{mx}" cy="{gy+12}" r="5" fill="{GREEN}"/>')
    body.append(T(mx+10, gy+16, "true mean", 12.5, GREEN, 700))
    body.append(T(x+24, cy+ch-16, "Gaussian: peak confirms recovery · discriminator converges in ~10 epochs.", 13.5, SUB))
    b.append(cue(a1, k1, "For jet width team unfolds first second moments simultaneously.", "\n".join(body)))
    # right column: chunk 2 (first+second moments) and chunk 3/4 (MAE)
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 92, CARD, STROKE)]
    body.append(tick(rx0+22, cy+22, h=48, fill=TEAL))
    body.append(T(rx0+42, cy+40, "Jet width", 17, INK, 700))
    body.append(T(rx0+42, cy+66, "first + second moments unfolded simultaneously", 14, SUB))
    b.append(cue(a2, k2, "Scanning loss function candidate moment produces curves peaks true values mean absolute error two hundredths percent.", "\n".join(body)))
    a3, k3 = anchor(sid, 3)
    yy = cy + 112
    body = [rrect(rx0, yy, rw, 184, CARD2, GREEN, rx=14, sw=1.4)]
    body.append(T(rx0+24, yy+44, "MEAN ABSOLUTE ERROR", 12, GREEN, 700, SANS, spacing=1.5))
    body.append(T(rx0+24, yy+104, "0.02%", 54, "url(#warmg)", 800))
    body.append(T(rx0+24, yy+140, "or better between unfolded", 14.5, INK, 600))
    body.append(T(rx0+24, yy+162, "and true moments — sub-percent.", 14.5, INK, 600))
    b.append(cue(a3, k3, "That is sub-percent agreement between unfolded and true moments.", "\n".join(body)))
    write("07_key-result.svg", "\n".join(b))

# ===========================================================================
# Slide 8 - Ablation Study
# ===========================================================================
def s08():
    sid = "ablation-study"
    head, y0 = frame("Ablation", "What controlling two moments does — and doesn't", idx="08 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD, STROKE)]
    body.append(tick(76, y0+16, h=26, fill=ACCENT))
    body.append(T(96, y0+37, "An instructive look at the limits of unfolding only a couple of moments", 18, INK, 700))
    b.append(cue(a0, k0, "One instructive observation concerns limits unfolding only couple moments.", "\n".join(body)))
    cy = y0 + 80
    # left chart: two distributions matched on mean+var but differing tails
    a1, k1 = anchor(sid, 1)
    cw1 = 596; ch = 300; x = 56
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=28, fill=WARM))
    body.append(T(x+40, cy+44, "Matched on 1st + 2nd moment — still not identical", 17, INK, 700))
    gx, gy, gw, gh = x+40, cy+80, cw1-80, 150
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.1"/>')
    def dist(col, sig, kurt, dash=""):
        pts = []
        for i in range(81):
            u = -3 + 6*i/80.0
            v = math.exp(-0.5*(u/sig)**2) * (1 + kurt*(u**2))
            px = gx + (u+3)/6.0*gw
            py = gy + gh - min(v, 1.25)*gh*0.72
            pts.append(f"{px:.1f},{py:.1f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.6"{d}/>'
    body.append(dist(GREEN, 0.85, 0.0))            # truth
    body.append(dist(ACCENT, 0.85, 0.10, dash="6 4"))  # reweighted gen: same mean/var, heavier tails
    body.append(T(gx+gw-6, gy+18, "truth", 12.5, GREEN, 700, anchor="end"))
    body.append(T(gx+gw-6, gy+36, "reweighted generation", 12.5, ACCENT, 700, anchor="end"))
    body.append(T(x+24, cy+ch-16, "Same mean and variance — but the full distributions differ in the tails.", 13.5, SUB))
    b.append(cue(a1, k1, "After Moment Unfolding matches first second moments jet width full distributions truth reweighted generation not statistically identical.", "\n".join(body)))
    # right: chunk 3 (higher moments) and chunk 4 (expected/by design)
    rx0 = x+cw1+24; rw = W-56-rx0
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD2, WARM, rx=14, sw=1.3)]
    body.append(tick(rx0+22, cy+24, h=30, fill=WARM))
    body.append(T(rx0+42, cy+44, "Higher moments still matter", 16, INK, 700))
    body.append(paragraph(rx0+22, cy+74, "The reason is simple: higher moments remain relevant, and they were never part of the fit.", 14, SUB, maxchars=40))
    b.append(cue(a2, k2, "Reason simply higher moments remain relevant were not part of the fit.", "\n".join(body)))
    a3, k3 = anchor(sid, 3)
    yy = cy+158
    body = [rrect(rx0, yy, rw, 142, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(tick(rx0+22, yy+24, h=30, fill=GREEN))
    body.append(T(rx0+42, yy+44, "By design, not a bug", 16, GREEN, 700))
    body.append(paragraph(rx0+22, yy+74, "Expected behavior: the technique deliberately controls the moments you ask for and leaves the rest free.", 14, SUB, maxchars=40))
    b.append(cue(a3, k3, "This expected behavior clarifies technique deliberately controls specific moments ask leaving rest free.", "\n".join(body)))
    write("08_ablation-study.svg", "\n".join(b))

# ===========================================================================
# Slide 9 - Headline Numbers
# ===========================================================================
def s09():
    sid = "headline-numbers"
    head, y0 = frame("By the Numbers", "The results that matter most", idx="09 / 10")
    b = [head]
    # chunk 1: intro strip
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 48, CARD, STROKE)]
    body.append(tick(76, y0+12, h=24, fill=WARM))
    body.append(T(96, y0+32, "A few numbers capture the impact", 18, INK, 700))
    b.append(cue(a0, k0, "A few numbers capture the impact.", "\n".join(body)))
    # top row: three tiles (chunks 2 & 3)
    a1, k1 = anchor(sid, 1)
    ty = y0 + 66
    tw = (W-112-2*24)/3; th = 176
    xs = [56, 56+tw+24, 56+2*(tw+24)]
    body = [rrect(xs[0], ty, tw, th, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(tick(xs[0]+24, ty+24, h=26, fill=GREEN))
    body.append(T(xs[0]+tw/2, ty+104, "0.02%", 54, GREEN, 800, anchor="middle"))
    body.append(T(xs[0]+tw/2, ty+138, "mean absolute error", 16, INK, 700, anchor="middle"))
    body.append(T(xs[0]+tw/2, ty+162, "unfolded vs. true moments", 12.5, SUB, 400, anchor="middle"))
    b.append(cue(a1, k1, "Unfolded moments agree true moments within two hundredths percent mean absolute error.", "\n".join(body)))
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(xs[1], ty, tw, th, CARD, STROKE))
    body.append(tick(xs[1]+24, ty+24, h=26, fill=ACCENT))
    body.append(T(xs[1]+tw/2, ty+104, "2", 56, ACCENT, 800, anchor="middle"))
    body.append(T(xs[1]+tw/2, ty+138, "moments unfolded at once", 16, INK, 700, anchor="middle"))
    body.append(T(xs[1]+tw/2, ty+162, "1st + 2nd of the jet width", 12.5, SUB, 400, anchor="middle"))
    body.append(rrect(xs[2], ty, tw, th, CARD, STROKE))
    body.append(tick(xs[2]+24, ty+24, h=26, fill=TEAL))
    body.append(T(xs[2]+tw/2, ty+104, "10", 56, TEAL, 800, anchor="middle"))
    body.append(T(xs[2]+tw/2, ty+138, "epochs to converge", 16, INK, 700, anchor="middle"))
    body.append(T(xs[2]+tw/2, ty+162, "discriminator convergence", 12.5, SUB, 400, anchor="middle"))
    b.append(cue(a2, k2, "Two moments jet width unfolded at once discriminator converges within ten epochs.", "\n".join(body)))
    # bottom row: reproducibility (chunk 4)
    a3, k3 = anchor(sid, 3)
    yy = ty + th + 22
    hw = (W-112-24)/2; hh = 128
    xs2 = [56, 56+hw+24]
    body = []
    body.append(rrect(xs2[0], yy, hw, hh, CARD2, ACCENT, rx=14, sw=1.3))
    body.append(T(xs2[0]+30, yy+78, "1M", 48, ACCENT, 800))
    body.append(T(xs2[0]+140, yy+66, "Gaussian samples", 16, INK, 700))
    body.append(T(xs2[0]+140, yy+90, "3 : 1 train / test split", 13.5, SUB))
    body.append(rrect(xs2[1], yy, hw, hh, CARD2, WARM, rx=14, sw=1.3))
    body.append(T(xs2[1]+30, yy+78, "< 5 min", 44, WARM, 800))
    body.append(T(xs2[1]+200, yy+66, "full reproduction", 16, INK, 700))
    body.append(T(xs2[1]+200, yy+90, "single Nvidia RTX6000 GPU", 13.5, SUB))
    b.append(cue(a3, k3, "Gaussian study million samples three-to-one train-test split entire notebooks reproduces under five minutes single Nvidia RTX6000 GPU.", "\n".join(body)))
    write("09_headline-numbers.svg", "\n".join(b))

# ===========================================================================
# Slide 10 - Takeaway
# ===========================================================================
def s10():
    sid = "takeaway"
    head, y0 = frame("Takeaway", "Unfold moments directly — no binning", idx="10 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 70, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(76, y0+20, h=30, fill=TEAL))
    body.append(T(96, y0+46, "You can unfold detector effects directly at the level of moments.", 21, INK, 800))
    b.append(cue(a0, k0, "Takeaway you can unfold detector effects directly level moments without ever binning data.", "\n".join(body)))
    a1, k1 = anchor(sid, 1)
    yy = y0 + 90
    body = [rrect(56, yy, W-112, 108, CARD, STROKE)]
    body.append(paragraph(80, yy+40, "Moment Unfolding does this with a GAN-like generator whose parameters ARE the moments, trains only once instead of iterating, and recovers the true moments to better than 0.01% on realistic LHC jet simulations.", size=18, fill=INK, maxchars=96, lh=27, weight=600))
    b.append(cue(a1, k1, "Moment Unfolding GAN-like generator parameters moments trains once rather iterating recovers true moments better hundredth percent realistic LHC jet.", "\n".join(body)))
    # chunk 3: beyond particle physics
    a2, k2 = anchor(sid, 2)
    cy = yy + 128
    cw = (W-112-2*24)/3; ch = 148
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    pil = [
        ("Moments, not bins", ACCENT, "unfold statistical moments without any histogram"),
        ("Train once", TEAL, "a single GAN-like network pair, no iteration"),
        ("Beyond particle physics", GREEN, "dataset-agnostic — any deconvolution problem"),
    ]
    body = []
    for (t, col, d), x in zip(pil, xs):
        body.append(rrect(x, cy, cw, ch, CARD, STROKE))
        body.append(tick(x+22, cy+26, h=30, fill=col))
        body.append(T(x+22, cy+72, t, 17, INK, 700))
        body.append(paragraph(x+22, cy+100, d, 14, SUB, maxchars=36))
    b.append(cue(a2, k2, "Because algorithm agnostic dataset same idea could carry over deconvolution problems well beyond particle physics.", "\n".join(body)))
    # footer links
    b.append(f'<line x1="56" y1="{cy+ch+26}" x2="{W-56}" y2="{cy+ch+26}" stroke="{STROKE}" stroke-width="1.2"/>')
    b.append(T(56, cy+ch+52, "Moment Unfolding · Desai, Nachman, Thaler · NeurIPS 2022 ML4PS", 15, SUB, 500))
    b.append(T(W-56, cy+ch+52, "github.com/hep-lbdl/MomentUnfolding", 14, ACCENT, 600, MONO, anchor="end"))
    write("10_takeaway.svg", "\n".join(b))

for fn in [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10]:
    fn()
print("done")
