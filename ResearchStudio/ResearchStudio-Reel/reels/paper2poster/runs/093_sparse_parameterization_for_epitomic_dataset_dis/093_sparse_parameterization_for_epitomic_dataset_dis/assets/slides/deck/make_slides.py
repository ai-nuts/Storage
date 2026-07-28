#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video (SPEED, NeurIPS 2023).

Each required narration chunk is wrapped in its own <g id="cue_..."> card whose
<title> carries the narration keywords, so the strict cue matcher resolves every
anchor from PPTX geometry. Zero <image> elements -> no image gates fire.
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CONTRACT = os.path.join(RUN, "assets", "meta", "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720

# ---- theme -----------------------------------------------------------------
BG      = "#0B1020"
BG2     = "#141232"
CARD    = "#181634"
CARD2   = "#211E44"
STROKE  = "#332F5E"
INK     = "#EEF0FB"
SUB     = "#B4B2D6"
MUT     = "#7C7AA6"
ACCENT  = "#7C6CF0"   # indigo-violet (sparse / dictionary identity)
TEAL    = "#37DCC0"   # secondary accent
WARM    = "#F7B84B"   # headline numbers
GREEN   = "#57D9A3"   # success
RED     = "#F2708A"   # danger / contrast
TINT_A  = "#211C3A"   # accent tint
TINT_R  = "#301B27"
TINT_W  = "#332A18"
TINT_G  = "#14261F"

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

def chip(x, y, w, h, label, col):
    seg = [rrect(x, y, w, h, CARD2, col, rx=10, sw=1.1)]
    seg.append(T(x+w/2, y+h/2+5, label, 14, INK, 700, anchor="middle"))
    return "\n".join(seg)

def dot_grid(x, y, cols, rows, gap, on_set, on_col, off_col=STROKE, r=3.2):
    """Small dictionary/sparse motif: a lattice of dots, a few lit."""
    seg = []
    for j in range(rows):
        for i in range(cols):
            cx = x + i*gap; cy = y + j*gap
            idx = j*cols + i
            col = on_col if idx in on_set else off_col
            op = "" if idx in on_set else ' opacity="0.5"'
            seg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"{op} />')
    return "\n".join(seg)

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
  <radialGradient id="bgv" cx="16%" cy="6%" r="100%">
    <stop offset="0%" stop-color="{BG2}" stop-opacity="0.95"/>
    <stop offset="62%" stop-color="{BG}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="warmg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{WARM}"/>
    <stop offset="100%" stop-color="#E8892E"/>
  </linearGradient>
  <linearGradient id="accg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{ACCENT}"/>
    <stop offset="100%" stop-color="#5B4BD6"/>
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
    # chunk 1: deep learning depends on huge datasets, distillation compresses (kicker)
    a0, k0 = anchor(sid, 0)
    body = []
    body.append(tick(72, 82, h=30, w=6, fill=ACCENT))
    body.append(T(92, 94, "DATASET DISTILLATION  ·  SPARSE PARAMETERIZATION", 15, ACCENT, 700, SANS, spacing=2.5))
    body.append(T(92, 124, "Deep learning depends on huge datasets; distillation compresses one into a tiny synthetic set.", 16, SUB, 400))
    b.append(cue(a0, k0, "Deep learning depends on huge datasets costly to store; distillation compresses into a tiny synthetic set.", "\n".join(body)))
    # title block
    b.append(T(72, 200, "SPEED", 70, INK, 800))
    b.append(T(300, 198, "Sparse Parameterization for", 24, SUB, 500))
    b.append(T(300, 228, "Epitomic Dataset Distillation", 24, SUB, 500))
    # chunk 2: rethinks parameterization instead of the matching objective (name card, left)
    a1, k1 = anchor(sid, 1)
    body = []
    body.append(rrect(72, 268, 600, 128, CARD, STROKE, rx=16))
    body.append(tick(92, 292, h=80, w=6, fill=TEAL))
    body.append(T(112, 306, "A new lever", 20, TEAL, 800))
    body.append(paragraph(112, 338, "Instead of tuning the matching objective like prior work, SPEED rethinks how the synthetic dataset is parameterized.", 15, SUB, maxchars=48, lh=22))
    b.append(cue(a1, k1, "Instead of tuning the matching objective like most prior work SPEED rethinks how synthetic dataset parameterized.", "\n".join(body)))
    # chunk 3: dictionary learning + sparse coding: tokens, codes, recurrent net (hero card, right)
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(712, 268, 496, 128, CARD2, ACCENT, rx=16, sw=1.4))
    body.append(T(736, 300, "Dictionary learning  +  sparse coding", 15, ACCENT, 800))
    body.append(T(736, 330, "epitomic tokens  ->  sparse codes  ->  recurrent synthesis", 13.5, INK, 600, MONO))
    body.append(dot_grid(742, 356, 8, 2, 20, {1, 4, 9, 13}, TEAL, r=4))
    body.append(T(920, 378, "shared token dictionary", 13, SUB, 500))
    b.append(cue(a2, k2, "Borrows ideas dictionary learning sparse coding shared pool spatial-agnostic epitomic tokens acts dictionary.", "\n".join(body)))
    # chunk 4: result SOTA on high-res, fraction of storage (band)
    a3, k3 = anchor(sid, 3)
    body = []
    body.append(rrect(72, 414, W-144, 58, CARD, WARM, rx=14, sw=1.2))
    body.append(tick(92, 432, h=22, fill=WARM))
    body.append(T(114, 450, "State-of-the-art distillation, especially on high-resolution ImageNet subsets, with only a fraction of the storage.", 15.5, INK, 600))
    b.append(cue(a3, k3, "Result state-of-the-art distillation especially high-resolution imagenet subsets fraction storage.", "\n".join(body)))
    # authors / venue footer
    b.append(f'<line x1="72" y1="512" x2="{W-72}" y2="512" stroke="{STROKE}" stroke-width="1.2" />')
    b.append(T(72, 550, "Xing Wei   ·   Anjia Cao   ·   Funing Yang   ·   Zhiheng Ma", 21, INK, 700))
    b.append(T(72, 578, "Xi'an Jiaotong University", 15, SUB))
    b.append(T(72, 612, "NeurIPS 2023", 14, ACCENT, 700, SANS, spacing=1.2))
    b.append(T(72, 638, "proceedings.neurips.cc/paper/2023    ·    github.com/MIV-XJTU/SPEED", 14, MUT, 500, MONO))
    write("01_title.svg", "\n".join(b))

# ===========================================================================
# Slide 2 - Problem
# ===========================================================================
def s02():
    sid = "problem"
    head, y0 = frame("Problem", "Parameterization is an afterthought", idx="02 / 08")
    b = [head]
    # chunk 1: goal is to shrink a dataset into a small synthetic set (intro band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 92, CARD, STROKE)]
    body.append(tick(76, y0+22, h=48))
    body.append(T(96, y0+38, "The goal of dataset distillation: shrink a big dataset into a small synthetic set that still trains models well", 19, INK, 700))
    body.append(T(96, y0+66, "but how the synthetic images are parameterized has been treated as an afterthought", 15, SUB))
    b.append(cue(a0, k0, "Goal dataset distillation shrink big dataset small synthetic set still trains models well.", "\n".join(body)))
    cy = y0 + 112
    cw = (W - 112 - 2*24) / 3
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    ch = 300
    # chunk 2: most work pours energy into the matching objective
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=ACCENT))
    body.append(T(x+22, cy+80, "All eyes on the objective", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Most existing work pours its energy into the matching objective, the loss that aligns synthetic and real data.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+206, cw-44, 66, TINT_A, ACCENT, rx=12, sw=1.2))
    body.append(T(x+38, cy+240, "matching objective", 16, ACCENT, 800))
    body.append(T(x+38, cy+262, "the well-studied lever", 13, SUB))
    b.append(cue(a1, k1, "Most existing work pours its energy into matching objective loss aligns synthetic real datasets.", "\n".join(body)))
    # chunk 3: standard approach optimizes each image independently, naive
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=WARM))
    body.append(T(x+22, cy+80, "Each image, on its own", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "The standard scheme optimizes every synthetic image independently, never exploiting structure images share.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+206, cw-44, 66, TINT_W, WARM, rx=12, sw=1.2))
    body.append(T(x+38, cy+240, "naive parameterization", 16, WARM, 800))
    body.append(T(x+38, cy+262, "no shared structure", 13, SUB))
    b.append(cue(a2, k2, "Standard approach optimizes each synthetic image independently naive scheme never exploits shared visual structure.", "\n".join(body)))
    # chunk 4: spatial redundancy wastes the tiny storage budget, worse at high res
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+80, "Wasted budget", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "That spatial redundancy silently wastes the already tiny storage budget, and it worsens as resolution grows.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+206, cw-44, 66, TINT_R, RED, rx=12, sw=1.2))
    body.append(T(x+38, cy+240, "spatial redundancy", 16, RED, 800))
    body.append(T(x+38, cy+262, "worse at high resolution", 13, SUB))
    b.append(cue(a3, k3, "Spatial redundancy silently wastes already tiny storage budget problem worse image resolution grows.", "\n".join(body)))
    write("02_problem.svg", "\n".join(b))

# ===========================================================================
# Slide 3 - Motivation
# ===========================================================================
def s03():
    sid = "motivation"
    head, y0 = frame("Motivation", "Images are highly redundant", idx="03 / 08")
    b = [head]
    lw = 616; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 1: images redundant, patches repeat, textures recur (left upper)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, lw, 168, CARD, STROKE)]
    body.append(tick(76, y0+22, h=30))
    body.append(T(96, y0+40, "The key insight: images repeat themselves", 17, INK, 700))
    body.append(paragraph(96, y0+70, "Patches repeat, textures recur, and similar structures appear across many different images.", 14.5, SUB, maxchars=62))
    body.append(dot_grid(96, y0+128, 14, 2, 22, {0, 3, 7, 10, 16, 19, 24}, TEAL, r=4.2))
    body.append(T(96+14*22+8, y0+120, "recurring", 12.5, SUB, 500))
    body.append(T(96+14*22+8, y0+138, "structure", 12.5, SUB, 500))
    b.append(cue(a0, k0, "Key insight images highly redundant patches repeat textures recur similar structures appear across images.", "\n".join(body)))
    # chunk 2: classical dictionary learning / sparse coding was built for this (left lower)
    a1, k1 = anchor(sid, 1)
    yy = y0+188
    body = [rrect(56, yy, lw, 120, CARD2, ACCENT, rx=14, sw=1.2)]
    body.append(tick(76, yy+24, h=72, fill=ACCENT))
    body.append(T(96, yy+44, "Classical representation learning fits perfectly", 18, INK, 700))
    body.append(paragraph(96, yy+72, "Dictionary learning and sparse coding were built to represent many signals as sparse combinations of a shared dictionary.", 14.5, SUB, maxchars=64))
    b.append(cue(a1, k1, "Classical representation learning dictionary learning sparse coding built represent many signals sparse combinations shared dictionary.", "\n".join(body)))
    # chunk 3: recent methods use inter-image relations, none spatially-agnostic (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, y0, rw, 168, CARD, STROKE)]
    body.append(tick(rx0+20, y0+22, h=30, fill=WARM))
    body.append(T(rx0+40, y0+40, "A gap remains", 16, WARM, 700))
    body.append(paragraph(rx0+20, y0+72, "A few recent methods exploit relationships between synthetic images, but none tackle redundancy in a spatially-agnostic way.", 14.5, SUB, maxchars=46))
    body.append(rrect(rx0+20, y0+134, rw-40, 24, BG2, "", rx=8))
    body.append(T(rx0+34, y0+151, "spatially-agnostic:  wherever a feature appears", 12.5, WARM, 600))
    b.append(cue(a2, k2, "Handful recent distillation methods started exploiting relationships between synthetic images none tackled redundancy spatially-agnostic.", "\n".join(body)))
    # chunk 4: SPEED spends almost none of the budget on dictionary + codes (right lower)
    a3, k3 = anchor(sid, 3)
    yy = y0+188
    body = [rrect(rx0, yy, rw, 120, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(tick(rx0+20, yy+24, h=30, fill=GREEN))
    body.append(T(rx0+40, yy+42, "The SPEED question", 16, GREEN, 700))
    body.append(paragraph(rx0+20, yy+72, "What if we spend almost none of the budget on a shared dictionary and sparse codes, and let a small net rebuild rich images?", 14.5, SUB, maxchars=46))
    b.append(cue(a3, k3, "SPEED asks what spend almost none storage budget shared dictionary per-image sparse codes small network reconstruct.", "\n".join(body)))
    write("03_motivation.svg", "\n".join(b))

# ===========================================================================
# Slide 4 - Contribution
# ===========================================================================
def s04():
    sid = "contribution"
    head, y0 = frame("Contribution", "Three pieces, one drop-in framework", idx="04 / 08")
    b = [head]
    cw = (W - 112 - 24) / 2; ch = 172
    xs = [56, 56+cw+24]; ys = [y0, y0+ch+22]
    specs = [
        (0, xs[0], ys[0], "01", ACCENT, "Spatial-agnostic epitomic tokens",
         "A shared dictionary of tokens (SAETs) reused by every image patch, with sparse coding matrices selecting the significant tokens per image."),
        (1, xs[1], ys[0], "02", TEAL, "Feature-recurrent network",
         "A compact transformer-style net (FReeNet) that recurrently assembles tokens into hierarchical, high-resolution images, reusing shared tokens and codes."),
        (2, xs[0], ys[1], "03", GREEN, "A drop-in module",
         "The parameterization plugs into gradient, distribution, and trajectory matching objectives alike, and improves all of them."),
        (3, xs[1], ys[1], "04", WARM, "New state of the art",
         "The framework sets new state-of-the-art distillation results and is especially strong on high-resolution data."),
    ]
    for ci, x, y, num, col, title, txt in specs:
        a, k = anchor(sid, ci)
        body = [rrect(x, y, cw, ch, CARD, STROKE)]
        body.append(tick(x+24, y+28, h=34, fill=col))
        body.append(T(x+cw-24, y+54, num, 40, col, 800, MONO, anchor="end", opacity=0.5))
        body.append(T(x+44, y+50, title, 20, INK, 700))
        body.append(paragraph(x+44, y+86, txt, 14.5, SUB, maxchars=60))
        b.append(cue(a, k, txt, "\n".join(body)))
    write("04_contribution.svg", "\n".join(b))

# ===========================================================================
# Slide 5 - Dataset / Benchmark
# ===========================================================================
def s05():
    sid = "dataset-benchmark"
    head, y0 = frame("Benchmark", "Tested broadly, budget for budget", idx="05 / 08")
    b = [head]
    # chunk 1: standard datasets CIFAR-10/100, TinyImageNet (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 66, CARD, STROKE)]
    body.append(tick(76, y0+18, h=30, fill=TEAL))
    body.append(T(96, y0+42, "Standard: CIFAR-10 and CIFAR-100 at 32x32  ·  TinyImageNet at 64x64", 18, INK, 700))
    b.append(cue(a0, k0, "SPEED tested broadly standard side CIFAR-10 CIFAR-100 thirty-two resolution TinyImageNet sixty-four.", "\n".join(body)))
    cy = y0 + 86
    lw = 596; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 2: six high-res ImageNet subsets (left card, chips)
    a1, k1 = anchor(sid, 1)
    body = [rrect(56, cy, lw, 300, CARD, STROKE)]
    body.append(tick(76, cy+24, h=28, fill=ACCENT))
    body.append(T(94, cy+44, "Six ImageNet subsets at 128x128, 10 classes each", 17, INK, 700))
    subsets = [("ImageNette", ACCENT), ("ImageWoof", TEAL), ("ImageFruit", WARM),
               ("ImageMeow", GREEN), ("ImageSquawk", RED), ("ImageYellow", "#B98CF0")]
    pcw = (lw - 40 - 20) / 2; pch = 58
    for i, (p, col) in enumerate(subsets):
        px = 76 + (i % 2) * (pcw + 20)
        py = cy + 74 + (i // 2) * (pch + 14)
        body.append(rrect(px, py, pcw, pch, CARD2, col, rx=10, sw=1.1))
        body.append(tick(px+14, py+16, h=26, fill=col))
        body.append(T(px+30, py+35, p, 15.5, INK, 700))
    b.append(cue(a1, k1, "Stress high-resolution performance six ImageNet subsets one-twenty-eight ten classes ImageNette ImageWoof ImageFruit ImageMeow ImageSquawk ImageYellow.", "\n".join(body)))
    # chunk 3: robustness on CIFAR-100-C (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD, STROKE)]
    body.append(tick(rx0+20, cy+22, h=28, fill=WARM))
    body.append(T(rx0+38, cy+42, "Robustness stress test", 16, WARM, 700))
    rows = [("Benchmark", "CIFAR-100-C"), ("Corruption types", "14"), ("Severity levels", "5")]
    ry = cy+72
    for lab, val in rows:
        body.append(T(rx0+22, ry, lab, 14, SUB, 600))
        body.append(T(rx0+rw-22, ry, val, 14, INK, 700, MONO, anchor="end"))
        ry += 24
    b.append(cue(a2, k2, "Robustness measured CIFAR-100-C fourteen corruption types five severity levels.", "\n".join(body)))
    # chunk 4: equal storage budget, ConvNet + trajectory, cross-arch (right lower)
    a3, k3 = anchor(sid, 3)
    yy = cy+158
    body = [rrect(rx0, yy, rw, 142, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(rx0+20, yy+22, h=30, fill=TEAL))
    body.append(T(rx0+40, yy+42, "Equal budgets, params per class", 15.5, TEAL, 700))
    body.append(T(rx0+22, yy+72, "IPC 1  ·  10  ·  50", 15, INK, 700, MONO))
    body.append(paragraph(rx0+22, yy+97, "Default ConvNet + trajectory matching; cross-arch eval on MLP, ResNet18, ViT.", 13.5, SUB, maxchars=46, lh=20))
    b.append(cue(a3, k3, "Default backbone ConvNet default matching objective trajectory matching generalization MLP ResNet18 ViT equal storage params per class.", "\n".join(body)))
    write("05_dataset-benchmark.svg", "\n".join(b))

# ===========================================================================
# Slide 6 - Key Result
# ===========================================================================
def s06():
    sid = "key-result"
    head, y0 = frame("Key Result", "A clean sweep of the state of the art", idx="06 / 08")
    b = [head]
    # chunk 1: SOTA across all 3 standard + all 6 high-res subsets (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD2, WARM, rx=12, sw=1.2)]
    body.append(T(76, y0+37, "New state-of-the-art across all three standard benchmarks and all six high-resolution ImageNet subsets.", 17.5, INK, 700))
    b.append(cue(a0, k0, "Headline clean sweep across all three standard benchmarks all six high-resolution ImageNet subsets new state-of-the-art.", "\n".join(body)))
    cy = y0 + 80
    # chunk 2: gains at 1 IPC (left chart card)
    a1, k1 = anchor(sid, 1)
    cw1 = 596; ch = 296; x = 56
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(T(x+24, cy+40, "Accuracy gain at the tightest 1 image/class", 17, INK, 700))
    body.append(T(x+cw1-24, cy+40, "+pts", 13, MUT, 700, MONO, anchor="end"))
    gx, gy, gw, gh = x+40, cy+72, cw1-90, 150
    bars = [("CIFAR-100", 6.0, "40.0%", ACCENT), ("TinyImageNet", 10.9, "26.9%", TEAL), ("ImageNet subsets", 11.2, "avg", GREEN)]
    vmax = 12.0
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    bw = gw / (len(bars)*1.7)
    for i, (lab, v, tag, col) in enumerate(bars):
        bx = gx + i*(gw/len(bars)) + (gw/len(bars)-bw)/2
        bh = v/vmax*gh
        body.append(rrect(bx, gy+gh-bh, bw, bh, col, "", rx=5))
        body.append(T(bx+bw/2, gy+gh-bh-10, f"+{v:g}", 17, col, 800, anchor="middle"))
        body.append(T(bx+bw/2, gy+gh+18, lab, 12.5, SUB, 600, anchor="middle"))
        body.append(T(bx+bw/2, gy+gh+36, tag, 12, MUT, 600, anchor="middle", family=MONO))
    body.append(T(x+24, cy+ch-14, "Up to +11 points over the previous best at the same storage budget.", 13, SUB))
    b.append(cue(a1, k1, "Tightest one-image-per-class budget reaches forty percent CIFAR-100 six point gain twenty-six point nine TinyImageNet ten point nine.", "\n".join(body)))
    # chunk 3: 1 IPC matches prior 10 IPC at ~10% storage (right upper)
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD2, ACCENT, rx=14, sw=1.4)]
    body.append(T(rx0+24, cy+36, "Ten times less storage", 13, ACCENT, 700, SANS, spacing=1))
    body.append(T(rx0+24, cy+78, "1 IPC  =  prior 10 IPC", 21, INK, 800))
    body.append(T(rx0+24, cy+106, "+11.2% avg on ImageNet subsets", 13.5, TEAL, 700))
    body.append(T(rx0+24, cy+126, "at only ~10% of their storage", 12.5, SUB))
    b.append(cue(a2, k2, "ImageNet subsets averages eleven point two percent improvement one-image results match prior ten images ten percent storage.", "\n".join(body)))
    # chunk 4: continual learning + robustness (right lower)
    a3, k3 = anchor(sid, 3)
    yy = cy + 158
    body = [rrect(rx0, yy, rw, 138, CARD, STROKE)]
    body.append(tick(rx0+22, yy+22, h=30, fill=GREEN))
    body.append(T(rx0+42, yy+42, "Best beyond accuracy too", 16, INK, 700))
    body.append(paragraph(rx0+22, yy+72, "Best at every continual-learning step, and under corruption on ResNet18 it nearly doubles the accuracy of prior methods.", 14, SUB, maxchars=42))
    b.append(cue(a3, k3, "Also stays best every step continual learning under corruption ResNet18 nearly doubles accuracy prior methods.", "\n".join(body)))
    write("06_key-result.svg", "\n".join(b))

# ===========================================================================
# Slide 7 - Ablation Study
# ===========================================================================
def s07():
    sid = "ablation-study"
    head, y0 = frame("Ablation", "Sparsification is essentially free", idx="07 / 08")
    b = [head]
    # chunk 1: sparsification essentially free -- left card with k=48 ~ full comparison
    a0, k0 = anchor(sid, 0)
    cw1 = 596; ch = 296; x = 56
    cy = y0
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=28, fill=ACCENT))
    body.append(T(x+40, cy+44, "Pruning the codes barely moves accuracy", 18, INK, 700))
    body.append(paragraph(x+24, cy+76, "Pruning each sparse coding matrix to just 48 non-zero elements meets the storage budget with almost no loss.", 14.5, SUB, maxchars=58))
    mcw = (cw1 - 48 - 40) / 2; my = cy + 148; mch = 116
    body.append(rrect(x+24, my, mcw, mch, CARD2, TEAL, rx=12, sw=1.2))
    body.append(T(x+24+mcw/2, my+34, "k = 48 non-zeros", 16, INK, 800, anchor="middle"))
    body.append(T(x+24+mcw/2, my+64, "73.5%", 30, TEAL, 800, anchor="middle"))
    body.append(T(x+24+mcw/2, my+92, "307K params", 12.5, SUB, anchor="middle", family=MONO))
    body.append(T(x+24+mcw+20, my+mch/2+6, "≈", 34, WARM, 800, anchor="middle"))
    body.append(rrect(x+24+mcw+40, my, mcw, mch, CARD2, STROKE, rx=12, sw=1.2))
    body.append(T(x+24+mcw+40+mcw/2, my+34, "full model", 16, INK, 800, anchor="middle"))
    body.append(T(x+24+mcw+40+mcw/2, my+64, "74.0%", 30, INK, 800, anchor="middle"))
    body.append(T(x+24+mcw+40+mcw/2, my+92, "15M params", 12.5, SUB, anchor="middle", family=MONO))
    b.append(cue(a0, k0, "Ablations show sparsification essentially free pruning meets storage budget keeping ConvNet accuracy.", "\n".join(body)))
    # right column: three stacked cards
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    rh = (ch - 2*12) / 3
    # chunk 2: 48 non-zeros ~ 307K params meets the budget
    a1, k1 = anchor(sid, 1)
    yy = cy
    body = [rrect(rx0, yy, rw, rh, CARD, STROKE)]
    body.append(T(rx0+20, yy+32, "About 50x smaller codes", 14.5, ACCENT, 700))
    body.append(paragraph(rx0+20, yy+56, "Roughly 307K parameters versus a 15M-parameter full model, at ~0.3% density.", 13, SUB, maxchars=46))
    b.append(cue(a1, k1, "Pruning sparse coding matrix just forty-eight non-zero elements about three hundred thousand parameters meets storage budget.", "\n".join(body)))
    # chunk 3: push k too low collapses; moderate best, improves generalization
    a2, k2 = anchor(sid, 2)
    yy = cy + rh + 12
    body = [rrect(rx0, yy, rw, rh, CARD2, RED, rx=14, sw=1.2)]
    body.append(T(rx0+20, yy+32, "Do not push k too far", 14.5, RED, 700))
    body.append(paragraph(rx0+20, yy+56, "At k=12 accuracy collapses to 57.8%. A moderate k is best for generalization.", 13, SUB, maxchars=46))
    b.append(cue(a2, k2, "Push k too low down twelve accuracy collapses moderate value best improves cross-architecture generalization.", "\n".join(body)))
    # chunk 4: R=2, H=3; before/after images look identical
    a3, k3 = anchor(sid, 3)
    yy = cy + 2*(rh + 12)
    body = [rrect(rx0, yy, rw, rh, CARD, WARM, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+22, h=24, fill=WARM))
    body.append(T(rx0+38, yy+40, "R=2 blocks, H=3 heads", 15, WARM, 700))
    body.append(paragraph(rx0+20, yy+64, "Samples before and after sparsifying to 0.3% density look almost identical.", 13, SUB, maxchars=46))
    b.append(cue(a3, k3, "Qualitatively synthetic images before after sparsification zero point three percent density look almost identical two recurrent blocks three heads.", "\n".join(body)))
    write("07_ablation-study.svg", "\n".join(b))

# ===========================================================================
# Slide 8 - Takeaway
# ===========================================================================
def s08():
    sid = "takeaway"
    head, y0 = frame("Takeaway", "Parameterization is a powerful lever", idx="08 / 08")
    b = [head]
    # chunk 1: parameterization deserves as much attention as the objective (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 96, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(76, y0+22, h=52, fill=ACCENT))
    body.append(T(96, y0+44, "Parameterization deserves as much attention as the matching objective", 20, INK, 800))
    body.append(T(96, y0+74, "the lasting message of SPEED, and where its gains come from", 15, SUB))
    b.append(cue(a0, k0, "Lasting message SPEED parameterization deserves much attention matching objective.", "\n".join(body)))
    # chunk 2: shared dictionary + sparse codes + small recurrent net removes redundancy (card)
    a1, k1 = anchor(sid, 1)
    yy = y0 + 116
    body = [rrect(56, yy, W-112, 92, CARD2, GREEN, rx=14, sw=1.2)]
    body.append(tick(76, yy+22, h=48, fill=GREEN))
    body.append(paragraph(96, yy+42, "A shared dictionary of spatial-agnostic epitomic tokens, sparse per-image coding matrices, and a small recurrent network remove the spatial redundancy naive methods leave on the table.", size=16, fill=INK, maxchars=98, lh=26, weight=600))
    b.append(cue(a1, k1, "Treating synthetic dataset shared dictionary spatial-agnostic epitomic tokens sparse per-image coding matrices small recurrent network removes spatial redundancy.", "\n".join(body)))
    # chunk 3: the payoff pillars
    a2, k2 = anchor(sid, 2)
    cy = yy + 112
    cw = (W-112-2*24)/3; ch = 148
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    pil = [
        ("Fraction of the storage", ACCENT, "state-of-the-art distillation, biggest on high-resolution images"),
        ("Generalizes better", TEAL, "stronger transfer to unseen architectures like ResNet and ViT"),
        ("More robust", GREEN, "sturdier under image corruption than prior methods"),
    ]
    body = []
    for (t, col, d), x in zip(pil, xs):
        body.append(rrect(x, cy, cw, ch, CARD, STROKE))
        body.append(tick(x+22, cy+26, h=30, fill=col))
        body.append(T(x+22, cy+72, t, 16.5, INK, 700))
        body.append(paragraph(x+22, cy+100, d, 13.5, SUB, maxchars=38))
    b.append(cue(a2, k2, "Payoff state-of-the-art distillation fraction storage biggest high-resolution images better generalization unseen architectures stronger robustness corruption.", "\n".join(body)))
    # chunk 4: closing line (footer band)
    a3, k3 = anchor(sid, 3)
    yy2 = cy + ch + 20
    body = [rrect(56, yy2, W-112, 44, CARD, WARM, rx=12, sw=1.1)]
    body.append(tick(76, yy2+12, h=20, fill=WARM))
    body.append(T(96, yy2+29, "Sparse, shared representation is a general lever for making tiny synthetic datasets do far more.", 15, INK, 700))
    b.append(cue(a3, k3, "Short sparse shared representation powerful general lever making tiny synthetic datasets do far more.", "\n".join(body)))
    b.append(T(W-56, yy2+29, "github.com/MIV-XJTU/SPEED", 13, ACCENT, 600, MONO, anchor="end"))
    write("08_takeaway.svg", "\n".join(b))

for fn in [s01, s02, s03, s04, s05, s06, s07, s08]:
    fn()
print("done")
