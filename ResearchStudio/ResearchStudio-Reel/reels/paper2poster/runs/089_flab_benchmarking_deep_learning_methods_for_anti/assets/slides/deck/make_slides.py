#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video (FLAb, NeurIPS 2023).

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

# ---- theme -----------------------------------------------------------------
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
RED     = "#F2708A"   # danger / failure

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
    # chunk 1: ML promises to accelerate antibody design (kicker)
    a0, k0 = anchor(sid, 0)
    body = []
    body.append(tick(72, 82, h=30, w=6, fill=ACCENT))
    body.append(T(92, 94, "MACHINE LEARNING  ·  THERAPEUTIC ANTIBODY DESIGN", 15, ACCENT, 700, SANS, spacing=2.5))
    body.append(T(92, 124, "Machine learning can accelerate antibody design only if models can read the fitness landscape.", 16, SUB, 400))
    b.append(cue(a0, k0, "Machine learning promises to accelerate therapeutic antibody design if models read fitness.", "\n".join(body)))
    # title block
    b.append(T(72, 196, "FLAb", 66, INK, 800))
    b.append(T(250, 194, "The Fitness Landscape for Antibodies", 26, SUB, 500))
    b.append(T(72, 238, "Benchmarking deep learning methods for antibody fitness prediction", 19, MUT, 500))
    # chunk 2: introduces FLAb, largest benchmark (name card, left)
    a1, k1 = anchor(sid, 1)
    body = []
    body.append(rrect(72, 268, 600, 128, CARD, STROKE, rx=16))
    body.append(tick(92, 292, h=80, w=6, fill=TEAL))
    body.append(T(112, 306, "FLAb", 30, TEAL, 800))
    body.append(T(200, 306, "Fitness Landscape for Antibodies", 16, INK, 600))
    body.append(T(112, 338, "The largest therapeutic antibody design benchmark", 15, SUB))
    body.append(T(112, 360, "assembled to date, released openly for the community.", 15, SUB))
    b.append(cue(a1, k1, "Introduces FLAb the fitness landscape for antibodies largest therapeutic antibody benchmark to date.", "\n".join(body)))
    # chunk 3: gathers measurements for six properties, stress-tests six models vs Rosetta (hero card, right)
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(712, 268, 496, 128, CARD2, ACCENT, rx=16, sw=1.4))
    body.append(T(736, 322, "13,384", 52, "url(#warmg)", 800))
    body.append(T(902, 306, "experimental", 15, SUB))
    body.append(T(902, 328, "fitness measurements", 15, INK, 600))
    body.append(T(736, 366, "6 developability properties  ·  6 models  vs  Rosetta", 14.5, INK, 500))
    b.append(cue(a2, k2, "Gathers experimental measurements for six developability properties stress-tests six models against Rosetta.", "\n".join(body)))
    # chunk 4: headline finding sobering (band)
    a3, k3 = anchor(sid, 3)
    body = []
    body.append(rrect(72, 414, W-144, 58, CARD, WARM, rx=14, sw=1.2))
    body.append(tick(92, 432, h=22, fill=WARM))
    body.append(T(114, 450, "Headline finding: no single model correlates well with all six properties, and performance swings sharply across datasets.", 15.5, INK, 600))
    b.append(cue(a3, k3, "Headline finding sobering no single model correlates well all six properties performance swings.", "\n".join(body)))
    # authors / venue footer
    b.append(f'<line x1="72" y1="512" x2="{W-72}" y2="512" stroke="{STROKE}" stroke-width="1.2" />')
    b.append(T(72, 550, "Michael Chungyoun   ·   Jeffrey Ruffolo   ·   Jeffrey Gray", 21, INK, 700))
    b.append(T(72, 578, "Johns Hopkins University", 15, SUB))
    b.append(T(72, 612, "NeurIPS 2023  ·  Machine Learning for Structural Biology Workshop", 14, ACCENT, 700, SANS, spacing=1.2))
    b.append(T(72, 638, "biorxiv.org/content/10.1101/2024.01.13.575504    ·    github.com/Graylab/FLAb", 14, MUT, 500, MONO))
    write("01_title.svg", "\n".join(b))

# ===========================================================================
# Slide 2 - Problem
# ===========================================================================
def s02():
    sid = "problem"
    head, y0 = frame("Problem", "No systematic benchmark for antibody fitness", idx="02 / 10")
    b = [head]
    # chunk 1: ML only speeds design if models understand fitness (intro band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 92, CARD, STROKE)]
    body.append(tick(76, y0+22, h=48))
    body.append(T(96, y0+38, "Machine learning speeds antibody design only if models truly understand fitness", 20, INK, 700))
    body.append(T(96, y0+66, "what makes an antibody good  —  yet there is no principled way to test whether a model captures it", 15, SUB))
    b.append(cue(a0, k0, "Machine learning can only speed antibody design if models truly understand what makes antibody good.", "\n".join(body)))
    cy = y0 + 112
    cw = (W - 112 - 2*24) / 3
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    ch = 300
    # chunk 2: benchmarks (CAFA, TAPE, FLIP) exclude antibody data
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+80, "Benchmarks skip antibodies", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "The major protein fitness benchmarks either leave antibody data out entirely or include only a sliver.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+196, cw-44, 76, "#301B27", RED, rx=12, sw=1.2))
    body.append(T(x+38, cy+232, "CAFA   ·   TAPE   ·   FLIP", 17, RED, 800))
    body.append(T(x+38, cy+256, "little to no antibody coverage", 13, SUB))
    b.append(cue(a1, k1, "Yet major protein fitness benchmarks like CAFA TAPE FLIP either exclude antibody data.", "\n".join(body)))
    # chunk 3: no principled way to check a model
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=WARM))
    body.append(T(x+22, cy+80, "No principled check", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Researchers have no systematic way to verify whether a deep learning model actually captures antibody fitness.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+204, cw-44, 68, "#332A18", WARM, rx=12, sw=1.2))
    body.append(T(x+38, cy+238, "no shared yardstick", 16, WARM, 800))
    body.append(T(x+38, cy+260, "for antibody models", 13, SUB))
    b.append(cue(a2, k2, "That leaves researchers no principled way to check whether deep learning actually captures fitness.", "\n".join(body)))
    # chunk 4: weak proxies (native sequence recovery)
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=ACCENT))
    body.append(T(x+22, cy+80, "Weak proxies persist", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "The field falls back on proxies like native sequence recovery, which say little about real therapeutic potential.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+204, cw-44, 68, "#16283F", ACCENT, rx=12, sw=1.2))
    body.append(T(x+38, cy+238, "sequence recovery", 16, ACCENT, 800))
    body.append(T(x+38, cy+260, "not therapeutic fitness", 13, SUB))
    b.append(cue(a3, k3, "Today the field often falls back weak proxies such as native sequence recovery.", "\n".join(body)))
    write("02_problem.svg", "\n".join(b))

# ===========================================================================
# Slide 3 - Motivation
# ===========================================================================
def s03():
    sid = "motivation"
    head, y0 = frame("Motivation", "Antibodies must satisfy competing demands", idx="03 / 10")
    b = [head]
    lw = 616; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 1: many demands at once (left card with six chips)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, lw, 168, CARD, STROKE)]
    body.append(tick(76, y0+22, h=30))
    body.append(T(96, y0+40, "A therapeutic antibody must satisfy many demands at once", 17, INK, 700))
    props = ["Express well", "Stay stable", "Low immunogenicity",
             "Bind tightly", "Resist aggregation", "Avoid polyreactivity"]
    cols3 = [ACCENT, TEAL, WARM, GREEN, RED, "#B98CF0"]
    cw3 = (lw - 40 - 2*16) / 3; chh = 40
    for i, (p, col) in enumerate(zip(props, cols3)):
        cxx = 96 + (i % 3) * (cw3 + 16)
        cyy = y0 + 66 + (i // 3) * (chh + 14)
        body.append(chip(cxx, cyy, cw3, chh, p, col))
    b.append(cue(a0, k0, "Therapeutic antibody must satisfy many demands at once express stay stable bind resist.", "\n".join(body)))
    # chunk 2: properties pull against each other (left lower card)
    a1, k1 = anchor(sid, 1)
    yy = y0+188
    body = [rrect(56, yy, lw, 120, CARD2, RED, rx=14, sw=1.2)]
    body.append(tick(76, yy+24, h=72, fill=RED))
    body.append(T(96, yy+44, "These properties pull against each other", 18, INK, 700))
    body.append(paragraph(96, yy+72, "Improving one can hurt another, so no single objective describes what makes a good therapeutic antibody.", 14.5, SUB, maxchars=64))
    b.append(cue(a1, k1, "These properties often pull against each other improving one can hurt another.", "\n".join(body)))
    # chunk 3: reliable scoring could replace wet-lab screening (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, y0, rw, 168, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(tick(rx0+20, y0+22, h=30, fill=GREEN))
    body.append(T(rx0+40, y0+40, "A reliable model could replace screening", 16, GREEN, 700))
    body.append(paragraph(rx0+20, y0+72, "If a model scored candidates across all of these axes, it could stand in for slow, expensive wet-lab screening.", 14.5, SUB, maxchars=46))
    body.append(rrect(rx0+20, y0+128, rw-40, 30, BG2, "", rx=8))
    body.append(T(rx0+34, y0+148, "in silico scoring  →  fewer wet-lab experiments", 13.5, GREEN, 600))
    b.append(cue(a2, k2, "If model could reliably score candidates across all these axes could replace wet-lab screening.", "\n".join(body)))
    # chunk 4: field needs one shared benchmark (right lower)
    a3, k3 = anchor(sid, 3)
    yy = y0+188
    body = [rrect(rx0, yy, rw, 120, CARD, ACCENT, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+24, h=30, fill=ACCENT))
    body.append(T(rx0+40, yy+42, "The field needs a shared benchmark", 16, ACCENT, 700))
    body.append(paragraph(rx0+20, yy+72, "As new antibody design methods keep appearing, one antibody-focused benchmark is needed to judge them fairly.", 14.5, SUB, maxchars=46))
    b.append(cue(a3, k3, "As new antibody design methods keep appearing field needs one shared antibody-focused benchmark.", "\n".join(body)))
    write("03_motivation.svg", "\n".join(b))

# ===========================================================================
# Slide 4 - Contribution
# ===========================================================================
def s04():
    sid = "contribution"
    head, y0 = frame("Contribution", "What FLAb delivers", idx="04 / 10")
    b = [head]
    cw = (W - 112 - 24) / 2; ch = 172
    xs = [56, 56+cw+24]; ys = [y0, y0+ch+22]
    specs = [
        (0, xs[0], ys[0], "01", ACCENT, "The FLAb benchmark",
         "The largest therapeutic antibody design benchmark assembled so far, built to fill the antibody gap."),
        (1, xs[1], ys[0], "02", TEAL, "17 landscapes, 13,384 metrics",
         "Curates seventeen mutational landscapes with more than thirteen thousand experimental fitness measurements."),
        (2, xs[0], ys[1], "03", GREEN, "Six models vs. Rosetta",
         "Evaluates six widely adopted pretrained protein models and compares them to physics-based Rosetta."),
        (3, xs[1], ys[1], "04", WARM, "Open, growing data",
         "All FLAb data are released openly so the community can keep expanding the benchmark."),
    ]
    for ci, x, y, num, col, title, txt in specs:
        a, k = anchor(sid, ci)
        body = [rrect(x, y, cw, ch, CARD, STROKE)]
        body.append(tick(x+24, y+28, h=34, fill=col))
        body.append(T(x+cw-24, y+54, num, 40, col, 800, MONO, anchor="end", opacity=0.55))
        body.append(T(x+44, y+50, title, 21, INK, 700))
        body.append(paragraph(x+44, y+86, txt, 15, SUB, maxchars=56))
        b.append(cue(a, k, txt, "\n".join(body)))
    write("04_contribution.svg", "\n".join(b))

# ===========================================================================
# Slide 5 - Method
# ===========================================================================
def s05():
    sid = "method"
    head, y0 = frame("Method", "Perplexity as an antibody fitness score", idx="05 / 10")
    b = [head]
    # chunk 1: perplexity averaged over residues (equation band)
    a0, k0 = anchor(sid, 0)
    eqh = 116
    body = [rrect(56, y0, W-112, eqh, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(76, y0+30, "Score each antibody by model perplexity, averaged over all heavy- and light-chain residues", 15, ACCENT, 700))
    body.append(T(76, y0+80, "PPL(s) = exp( - 1/N  Sum_i  log p(x_i | x_<i) )", 26, INK, 700, MONO))
    b.append(cue(a0, k0, "Core idea simple every antibody sequence or structure fed model reports perplexity averaged residues.", "\n".join(body)))
    cy = y0 + eqh + 22
    cw = (W - 112 - 2*22) / 3; ch = 214
    xs = [56, 56+cw+22, 56+2*(cw+22)]
    # chunk 2: low perplexity = high confidence
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "1  Low perplexity = confidence", 16, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "Perplexity measures how surprised a model is. A well-behaved model should be confident about high-fitness antibodies.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+162, cw-44, 34, BG2, "", rx=9))
    body.append(T(x+36, cy+184, "low PPL  <->  high fitness", 13.5, TEAL, 600, MONO))
    b.append(cue(a1, k1, "Perplexity measures how surprised well-behaved model should be confident low perplexity high fitness.", "\n".join(body)))
    # chunk 3: correlate with three coefficients
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "2  Correlate with fitness", 16, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "Correlate model scores against real experimental fitness using three coefficients:", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+140, cw-44, 56, BG2, "", rx=9))
    body.append(T(x+36, cy+164, "Pearson r  ·  Spearman rho", 13.5, INK, 600, MONO))
    body.append(T(x+36, cy+184, "Kendall tau", 13.5, INK, 600, MONO))
    b.append(cue(a2, k2, "Authors correlate these scores against real experimental fitness three coefficients Pearson Spearman Kendall.", "\n".join(body)))
    # chunk 4: models used as-released across architectures
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "3  Models used as released", 16, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "No additional fine-tuning. Three architecture families are compared exactly as published:", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+152, cw-44, 44, "#14261F", GREEN, rx=9, sw=1.1))
    body.append(T(x+36, cy+180, "decoder · encoder · inverse-folding", 12.5, GREEN, 600, MONO))
    b.append(cue(a3, k3, "Crucially models used exactly released no additional fine-tuning decoder-only encoder-only inverse-folding.", "\n".join(body)))
    write("05_method.svg", "\n".join(b))

# ===========================================================================
# Slide 6 - Dataset / Benchmark
# ===========================================================================
def s06():
    sid = "dataset-benchmark"
    head, y0 = frame("Benchmark", "Seventeen antibody fitness landscapes", idx="06 / 10")
    b = [head]
    # chunk 1: 17 landscapes, 8 studies, 13,384 measurements (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 66, CARD, STROKE)]
    body.append(tick(76, y0+18, h=30, fill=TEAL))
    body.append(T(96, y0+42, "17 mutational landscapes from distinct antibody families  ·  8 studies  ·  13,384 measurements", 18, INK, 700))
    b.append(cue(a0, k0, "FLAb pulls together seventeen mutational landscapes distinct antibody families drawn eight studies.", "\n".join(body)))
    cy = y0 + 86
    lw = 596; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 2: six developability properties (left card, chips)
    a1, k1 = anchor(sid, 1)
    body = [rrect(56, cy, lw, 300, CARD, STROKE)]
    body.append(tick(76, cy+24, h=28, fill=ACCENT))
    body.append(T(94, cy+44, "Six developability properties", 18, INK, 700))
    props = [("Expression", ACCENT), ("Thermostability", TEAL), ("Immunogenicity", WARM),
             ("Aggregation", GREEN), ("Polyreactivity", RED), ("Binding affinity", "#B98CF0")]
    pcw = (lw - 40 - 20) / 2; pch = 58
    for i, (p, col) in enumerate(props):
        px = 76 + (i % 2) * (pcw + 20)
        py = cy + 74 + (i // 2) * (pch + 14)
        body.append(rrect(px, py, pcw, pch, CARD2, col, rx=10, sw=1.1))
        body.append(tick(px+14, py+16, h=26, fill=col))
        body.append(T(px+30, py+35, p, 15.5, INK, 700))
    b.append(cue(a1, k1, "Together they cover six developability properties expression thermostability immunogenicity aggregation polyreactivity binding.", "\n".join(body)))
    # chunk 3: each property has its own experimental unit (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD, STROKE)]
    body.append(tick(rx0+20, cy+22, h=28, fill=WARM))
    body.append(T(rx0+38, cy+42, "Each grounded in a real unit", 16, WARM, 700))
    rows = [("Expression", "ug/mL"), ("Thermostability", "melting temp Tm"), ("Binding", "dissociation constant K_D")]
    ry = cy+70
    for lab, val in rows:
        body.append(T(rx0+22, ry, lab, 14, SUB, 600))
        body.append(T(rx0+rw-22, ry, val, 14, INK, 700, MONO, anchor="end"))
        ry += 24
    b.append(cue(a2, k2, "Each property grounded its own real experimental unit micrograms per milliliter melting temperature dissociation.", "\n".join(body)))
    # chunk 4: diversity tests generalization (right lower)
    a3, k3 = anchor(sid, 3)
    yy = cy+158
    body = [rrect(rx0, yy, rw, 142, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(rx0+20, yy+22, h=30, fill=TEAL))
    body.append(T(rx0+40, yy+42, "Built to test generalization", 16, TEAL, 700))
    body.append(paragraph(rx0+22, yy+72, "This diversity is what lets FLAb test whether a model generalizes across the many facets of antibody fitness.", 14, SUB, maxchars=42))
    b.append(cue(a3, k3, "Diversity what lets FLAb test whether model generalizes across many facets antibody fitness.", "\n".join(body)))
    write("06_dataset-benchmark.svg", "\n".join(b))

# ===========================================================================
# Slide 7 - Key Result
# ===========================================================================
def s07():
    sid = "key-result"
    head, y0 = frame("Key Result", "No model wins across the board", idx="07 / 10")
    b = [head]
    # chunk 1: reality check (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD2, WARM, rx=12, sw=1.2)]
    body.append(T(76, y0+37, "The headline result is a reality check for antibody fitness models.", 18, INK, 700))
    b.append(cue(a0, k0, "The headline result is a reality check.", "\n".join(body)))
    cy = y0 + 80
    # chunk 2: no model correlates with all six; swings across datasets (left chart card)
    a1, k1 = anchor(sid, 1)
    cw1 = 596; ch = 296; x = 56
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(T(x+24, cy+40, "Correlation swings across datasets", 17, INK, 700))
    body.append(T(x+cw1-24, cy+40, "|PCC|", 13, MUT, 700, MONO, anchor="end"))
    # scattered bars: same property, different datasets => varying PCC
    gx, gy, gw, gh = x+40, cy+70, cw1-80, 150
    vals = [0.84, 0.31, 0.72, 0.18, 0.63, 0.42, 0.77]
    bw = gw / (len(vals)*1.6)
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    # 0.6 reference line
    y06 = gy + (1-0.6)*gh
    body.append(f'<line x1="{gx}" y1="{y06:.1f}" x2="{gx+gw}" y2="{y06:.1f}" stroke="{TEAL}" stroke-width="1" stroke-dasharray="5 4"/>')
    body.append(T(gx+gw, y06-6, "0.6", 11.5, TEAL, 700, anchor="end"))
    for i, v in enumerate(vals):
        bx = gx + i*(gw/len(vals)) + (gw/len(vals)-bw)/2
        bh = v*gh
        col = GREEN if v >= 0.6 else (WARM if v >= 0.4 else RED)
        body.append(rrect(bx, gy+gh-bh, bw, bh, col, "", rx=4))
        body.append(T(bx+bw/2, gy+gh+16, f"D{i+1}", 11, MUT, 600, anchor="middle"))
    body.append(T(x+24, cy+ch-16, "No model correlates well with all six properties; even one property swings dataset to dataset.", 13, SUB))
    b.append(cue(a1, k1, "No model correlates well all six properties even single property performance swings widely dataset.", "\n".join(body)))
    # chunk 3: ProGen2-Small most frequent winner (right upper)
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD2, ACCENT, rx=14, sw=1.4)]
    body.append(T(rx0+24, cy+38, "Most frequent winner", 13, ACCENT, 700, SANS, spacing=1))
    body.append(T(rx0+24, cy+78, "ProGen2-Small", 22, INK, 800))
    body.append(T(rx0+24, cy+104, "top on 7 datasets", 15, TEAL, 700))
    body.append(T(rx0+24, cy+126, "Medium, OAS, ESM-IF, Rosetta tie at 6", 12.5, SUB))
    b.append(cue(a2, k2, "ProGen2-Small most frequent winner coming out top seven datasets Medium OAS ESM-IF Rosetta tie six.", "\n".join(body)))
    # chunk 4: sequence beats structure (right lower)
    a3, k3 = anchor(sid, 3)
    yy = cy + 158
    body = [rrect(rx0, yy, rw, 138, CARD, STROKE)]
    body.append(tick(rx0+22, yy+22, h=30, fill=GREEN))
    body.append(T(rx0+42, yy+42, "Sequence beats structure", 16, INK, 700))
    body.append(paragraph(rx0+22, yy+72, "Sequence-based models beat structure-based ones across every landscape, with the biggest gap on thermostability.", 14, SUB, maxchars=42))
    b.append(cue(a3, k3, "Notably sequence-based models average beat structure-based ones across every landscape biggest thermostability.", "\n".join(body)))
    write("07_key-result.svg", "\n".join(b))

# ===========================================================================
# Slide 8 - Ablation Study
# ===========================================================================
def s08():
    sid = "ablation-study"
    head, y0 = frame("Ablation", "What actually drives performance", idx="08 / 10")
    b = [head]
    # chunk 1: parameter count matters more than architecture (left card)
    a0, k0 = anchor(sid, 0)
    cw1 = 596; ch = 296; x = 56
    cy = y0
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=28, fill=ACCENT))
    body.append(T(x+40, cy+44, "Parameter count > architecture or data", 18, INK, 700))
    body.append(paragraph(x+24, cy+76, "Encoder-only AntiBERTy and decoder-only IgLM, trained on the same 558M antibody sequences, behave almost identically.", 14.5, SUB, maxchars=58))
    # two model chips side by side, equal
    mcw = (cw1 - 48 - 40) / 2; my = cy + 148; mch = 92
    body.append(rrect(x+24, my, mcw, mch, CARD2, TEAL, rx=12, sw=1.2))
    body.append(T(x+24+mcw/2, my+34, "AntiBERTy", 17, INK, 800, anchor="middle"))
    body.append(T(x+24+mcw/2, my+56, "encoder-only", 13, SUB, anchor="middle"))
    body.append(T(x+24+mcw/2, my+78, "558M OAS seqs", 12.5, TEAL, 600, anchor="middle"))
    body.append(T(x+24+mcw+20, my+mch/2+6, "≈", 34, WARM, 800, anchor="middle"))
    body.append(rrect(x+24+mcw+40, my, mcw, mch, CARD2, TEAL, rx=12, sw=1.2))
    body.append(T(x+24+mcw+40+mcw/2, my+34, "IgLM", 17, INK, 800, anchor="middle"))
    body.append(T(x+24+mcw+40+mcw/2, my+56, "decoder-only", 13, SUB, anchor="middle"))
    body.append(T(x+24+mcw+40+mcw/2, my+78, "558M OAS seqs", 12.5, TEAL, 600, anchor="middle"))
    b.append(cue(a0, k0, "Digging what drives performance authors find parameter count matters more architecture training data.", "\n".join(body)))
    # right column: three stacked cards
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    rh = (ch - 2*12) / 3
    # chunk 2: scaling ProGen2 helped only 2 properties
    a1, k1 = anchor(sid, 1)
    yy = cy
    body = [rrect(rx0, yy, rw, rh, CARD, STROKE)]
    body.append(T(rx0+20, yy+32, "Scaling helps only two properties", 14.5, ACCENT, 700))
    body.append(paragraph(rx0+20, yy+56, "ProGen2 151M -> 6.4B improved only polyreactivity and thermostability.", 13, SUB, maxchars=46))
    b.append(cue(a1, k1, "Scaling ProGen2 one hundred fifty million over six billion parameters helped only polyreactivity thermostability.", "\n".join(body)))
    # chunk 3: evolutionary bias (golimumab)
    a2, k2 = anchor(sid, 2)
    yy = cy + rh + 12
    body = [rrect(rx0, yy, rw, rh, CARD2, RED, rx=14, sw=1.2)]
    body.append(T(rx0+20, yy+32, "An evolutionary bias", 14.5, RED, 700))
    body.append(paragraph(rx0+20, yy+56, "Language models rank wild-type golimumab above more thermostable mutants; Rosetta ranks them right.", 13, SUB, maxchars=46))
    b.append(cue(a2, k2, "They also uncover evolutionary bias several language models rank wild-type golimumab fitter mutants thermostable.", "\n".join(body)))
    # chunk 4: evolutionary likelihood != physical fitness
    a3, k3 = anchor(sid, 3)
    yy = cy + 2*(rh + 12)
    body = [rrect(rx0, yy, rw, rh, CARD, WARM, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+22, h=24, fill=WARM))
    body.append(T(rx0+38, yy+40, "Likelihood is not fitness", 15, WARM, 700))
    body.append(paragraph(rx0+20, yy+64, "Evolutionary likelihood and physical fitness are not the same thing.", 13, SUB, maxchars=46))
    b.append(cue(a3, k3, "Reminder evolutionary likelihood physical fitness not same thing.", "\n".join(body)))
    write("08_ablation-study.svg", "\n".join(b))

# ===========================================================================
# Slide 9 - Headline Numbers
# ===========================================================================
def s09():
    sid = "headline-numbers"
    head, y0 = frame("By the Numbers", "The scope and the gaps", idx="09 / 10")
    b = [head]
    # chunk 1: a few numbers capture scope (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 52, CARD, STROKE)]
    body.append(tick(76, y0+15, h=24, fill=WARM))
    body.append(T(96, y0+34, "A few numbers capture both the scope of FLAb and its findings", 18, INK, 700))
    b.append(cue(a0, k0, "A few numbers capture scope findings.", "\n".join(body)))
    # chunk 2: scope tiles
    a1, k1 = anchor(sid, 1)
    yy = y0 + 72
    tw = (W-112-3*20)/4; th = 150
    xs = [56 + i*(tw+20) for i in range(4)]
    tiles = [
        ("13,384", WARM, "fitness measurements"),
        ("17", ACCENT, "mutational landscapes"),
        ("6", TEAL, "developability properties"),
        ("6", GREEN, "models  vs  Rosetta"),
    ]
    body = []
    for (big, col, lab), x in zip(tiles, xs):
        body.append(rrect(x, yy, tw, th, CARD, STROKE))
        body.append(tick(x+22, yy+24, h=24, fill=col))
        body.append(T(x+tw/2, yy+96, big, 48, col, 800, anchor="middle"))
        body.append(T(x+tw/2, yy+126, lab, 13.5, SUB, 600, anchor="middle"))
    b.append(cue(a1, k1, "FLAb spans thirteen thousand three hundred eighty four measurements seventeen landscapes six properties six models.", "\n".join(body)))
    # chunk 3: intrinsic vs extrinsic
    a2, k2 = anchor(sid, 2)
    yy2 = yy + th + 24
    lw = 584; hh = 150
    body = [rrect(56, yy2, lw, hh, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(T(76, yy2+36, "Intrinsic properties are captured; extrinsic lag", 15.5, GREEN, 700))
    body.append(T(76, yy2+76, "|PCC| > 0.6", 26, INK, 800, MONO))
    body.append(T(240, yy2+70, "intrinsic properties", 13.5, SUB))
    body.append(T(240, yy2+90, "(driven by the antibody itself)", 12, MUT))
    body.append(T(76, yy2+120, "extrinsic:  binding < 0.4   ·   expression < 0.42   ·   immunogenicity < 0.5", 13, WARM, 600))
    b.append(cue(a2, k2, "Intrinsic properties ones driven antibody itself reach average absolute correlation above zero point six.", "\n".join(body)))
    # chunk 4: intra vs inter family
    a3, k3 = anchor(sid, 3)
    rx0 = 56 + lw + 24; rw = W - 56 - rx0
    body = [rrect(rx0, yy2, rw, hh, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(rx0+22, yy2+34, "Within a family vs. across families", 14.5, ACCENT, 700))
    body.append(T(rx0+22, yy2+92, "0.77", 44, GREEN, 800))
    body.append(T(rx0+140, yy2+86, "within one", 13.5, SUB))
    body.append(T(rx0+140, yy2+106, "family", 13.5, SUB))
    body.append(T(rx0+rw-22, yy2+92, "0.12", 44, RED, 800, anchor="end"))
    body.append(T(rx0+rw-22, yy2+120, "across families", 13, SUB, anchor="end"))
    b.append(cue(a3, k3, "Models far better telling apart mutants within one family zero point seven seven across zero point one two.", "\n".join(body)))
    write("09_headline-numbers.svg", "\n".join(b))

# ===========================================================================
# Slide 10 - Takeaway
# ===========================================================================
def s10():
    sid = "takeaway"
    head, y0 = frame("Takeaway", "Not there yet, but a clear path forward", idx="10 / 10")
    b = [head]
    # chunk 1: no model reliably predicts across all properties (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 96, CARD2, RED, rx=14, sw=1.3)]
    body.append(tick(76, y0+22, h=52, fill=RED))
    body.append(T(96, y0+44, "No current model reliably predicts antibody fitness across all properties", 20, INK, 800))
    body.append(T(96, y0+74, "so we cannot yet trust deep learning to filter therapeutic candidates on its own", 15, SUB))
    b.append(cue(a0, k0, "Takeaway honest useful no current deep learning reliably predicts antibody fitness across all properties.", "\n".join(body)))
    # chunk 2: good news, intrinsic captured (card)
    a1, k1 = anchor(sid, 1)
    yy = y0 + 116
    body = [rrect(56, yy, W-112, 92, CARD2, GREEN, rx=14, sw=1.2)]
    body.append(tick(76, yy+22, h=48, fill=GREEN))
    body.append(paragraph(96, yy+42, "The good news: intrinsic properties are already captured reasonably well, which points to the hardest remaining challenges.", size=16.5, fill=INK, maxchars=92, lh=26, weight=600))
    b.append(cue(a1, k1, "Good news intrinsic properties already captured reasonably well which points hardest remaining challenges.", "\n".join(body)))
    # chunk 3: path forward pillars
    a2, k2 = anchor(sid, 2)
    cy = yy + 112
    cw = (W-112-2*24)/3; ch = 148
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    pil = [
        ("Add structure", ACCENT, "enrich models with structural information"),
        ("Add antigen + physics", TEAL, "antigen context and physics-based priors"),
        ("Grow open data", GREEN, "keep expanding datasets like FLAb"),
    ]
    body = []
    for (t, col, d), x in zip(pil, xs):
        body.append(rrect(x, cy, cw, ch, CARD, STROKE))
        body.append(tick(x+22, cy+26, h=30, fill=col))
        body.append(T(x+22, cy+72, t, 17, INK, 700))
        body.append(paragraph(x+22, cy+100, d, 14, SUB, maxchars=36))
    b.append(cue(a2, k2, "Authors argue most promising path forward enrich these models structural antigen physics-based priors open datasets.", "\n".join(body)))
    # footer links
    b.append(f'<line x1="56" y1="{cy+ch+28}" x2="{W-56}" y2="{cy+ch+28}" stroke="{STROKE}" stroke-width="1.2"/>')
    b.append(T(56, cy+ch+56, "Open antibody fitness benchmark, released for the community", 15, SUB, 500))
    b.append(T(W-56, cy+ch+56, "github.com/Graylab/FLAb", 14, ACCENT, 600, MONO, anchor="end"))
    write("10_takeaway.svg", "\n".join(b))

for fn in [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10]:
    fn()
print("done")
