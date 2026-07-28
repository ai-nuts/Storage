#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video.

Paper: Towards Reasoning-Aware Explainable VQA (NeurIPS 2022).

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
VIOLET  = "#B98CF0"   # 5th accent

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
# Slide 1 - Title  (3 chunks)
# ===========================================================================
def s01():
    sid = "title"; b = []
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}" />')
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bgv)" />')
    # chunk 1: most VQA models are black boxes (kicker band)
    a0, k0 = anchor(sid, 0)
    body = []
    body.append(tick(72, 74, h=30, w=6, fill=ACCENT))
    body.append(T(92, 86, "VISUAL QUESTION ANSWERING  ·  EXPLAINABILITY", 15, ACCENT, 700, SANS, spacing=2.5))
    body.append(T(92, 116, "Most VQA models are black boxes: they output an answer, but not the reasoning that produced it.", 16, SUB, 400))
    b.append(cue(a0, k0, "Most visual question answering models are black boxes outputting an answer but not the reasoning.", "\n".join(body)))
    # title block
    b.append(T(72, 194, "Reasoning-Aware", 60, INK, 800))
    b.append(T(72, 258, "Explainable VQA", 60, INK, 800))
    b.append(T(600, 190, "Towards", 26, ACCENT, 600, italic=True))
    # chunk 2: augments coarse-to-fine backbone with explanation generation (left card)
    a1, k1 = anchor(sid, 1)
    body = []
    body.append(rrect(72, 292, 600, 150, CARD, STROKE, rx=16))
    body.append(tick(92, 316, h=102, w=6, fill=TEAL))
    body.append(T(112, 332, "Answer  +  Explanation", 22, TEAL, 800))
    body.append(paragraph(112, 362, "Augments a state-of-the-art coarse-to-fine VQA backbone with an end-to-end explanation module, so it emits a human-readable explanation with every answer.", 15, SUB, maxchars=52, lh=22))
    b.append(cue(a1, k1, "Towards reasoning-aware explainable VQA augments coarse-to-fine backbone end-to-end explanation module human-readable.", "\n".join(body)))
    # chunk 3: compares LSTM/Transformer, human study shows BLEU/ROUGE unreliable (right card)
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(712, 292, 496, 150, CARD2, ACCENT, rx=16, sw=1.4))
    body.append(tick(732, 316, h=102, w=6, fill=WARM))
    body.append(T(752, 332, "The evaluation problem", 18, WARM, 800))
    body.append(paragraph(752, 362, "Compares LSTM vs Transformer explanation generators; a large human study shows BLEU and ROUGE are unreliable for judging explanations.", 14.5, SUB, maxchars=44, lh=22))
    b.append(cue(a2, k2, "Compares LSTM Transformer decoders explanation generator large human study shows BLEU ROUGE unreliable.", "\n".join(body)))
    # authors / venue footer
    b.append(f'<line x1="72" y1="486" x2="{W-72}" y2="486" stroke="{STROKE}" stroke-width="1.2" />')
    b.append(T(72, 524, "Rakesh Vaideeswaran   ·   Feng Gao   ·   Abhinav Mathur   ·   Govind Thattai", 20, INK, 700))
    b.append(T(72, 552, "University of Illinois, Urbana-Champaign   ·   Amazon Alexa AI", 15, SUB))
    b.append(T(72, 590, "NeurIPS 2022", 14, ACCENT, 700, SANS, spacing=1.5))
    b.append(T(72, 616, "arxiv.org/abs/2211.05190", 14, MUT, 500, MONO))
    write("01_title.svg", "\n".join(b))

# ===========================================================================
# Slide 2 - Problem  (4 chunks)
# ===========================================================================
def s02():
    sid = "problem"
    head, y0 = frame("Problem", "Right answers, but no visible reasoning", idx="02 / 10")
    b = [head]
    # chunk 1: classic VQA task; huge effort on accuracy (intro band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 92, CARD, STROKE)]
    body.append(tick(76, y0+22, h=48))
    body.append(T(96, y0+38, "Classic VQA: an image + a question in, an answer out", 20, INK, 700))
    body.append(T(96, y0+66, "The field has poured enormous effort into raising accuracy with large pre-trained vision-language models", 15, SUB))
    b.append(cue(a0, k0, "Classic visual question answering task takes image question returns answer field poured effort accuracy.", "\n".join(body)))
    cy = y0 + 112
    # chunk 2: result is a black box (left card)
    a1, k1 = anchor(sid, 1)
    lw = 380; x = 56; ch = 300
    body = [rrect(x, cy, lw, ch, CARD2, RED, rx=14, sw=1.3)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+80, "The result is a black box", 19, INK, 700))
    body.append(paragraph(x+22, cy+112, "The prediction may be right, yet there is no evidence explaining the reasoning behind it.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+200, lw-44, 78, "#301B27", RED, rx=12, sw=1.2))
    body.append(T(x+38, cy+236, "answer  ✓", 18, INK, 800, MONO))
    body.append(T(x+38, cy+262, "reasoning  ?", 16, RED, 800, MONO))
    b.append(cue(a1, k1, "Result black box prediction may be right yet no evidence explaining the reasoning behind it.", "\n".join(body)))
    # chunk 3: three kinds of models (middle+right wide card)
    a2, k2 = anchor(sid, 2)
    rx0 = x + lw + 24; rw = W - 56 - rx0
    body = [rrect(rx0, cy, rw, ch, CARD, STROKE)]
    body.append(tick(rx0+22, cy+26, h=30, fill=ACCENT))
    body.append(T(rx0+40, cy+46, "Three kinds of models", 19, INK, 700))
    rows = [
        ("Type 1", "Answer only", "no supporting evidence", MUT),
        ("Type 2", "Answer + generic caption", "describes the image, not the logic", WARM),
        ("Type 3", "Answer + self-contained explanation", "logically matches the answer", GREEN),
    ]
    ry = cy + 76; rowh = 66
    for tag, ti, desc, col in rows:
        body.append(rrect(rx0+22, ry, rw-44, rowh-12, CARD2, col, rx=10, sw=1.1))
        body.append(T(rx0+40, ry+34, tag, 14, col, 800, MONO))
        body.append(T(rx0+130, ry+30, ti, 16.5, INK, 700))
        body.append(T(rx0+130, ry+50, desc, 13, SUB))
        ry += rowh
    b.append(cue(a2, k2, "Authors distinguish three kinds models those give only answer those add generic caption rare third.", "\n".join(body)))
    # chunk 4: almost all SOTA fall into first two (band)
    a3, k3 = anchor(sid, 3)
    yy = cy + ch + 18
    body = [rrect(56, yy, W-112, 52, CARD2, WARM, rx=12, sw=1.2)]
    body.append(tick(76, yy+15, h=24, fill=WARM))
    body.append(T(96, yy+34, "Almost all state-of-the-art VQA models fall into the first two categories — this work targets the third.", 16, INK, 600))
    b.append(cue(a3, k3, "Almost all state-of-the-art VQA models fall into first two categories which motivates this work.", "\n".join(body)))
    write("02_problem.svg", "\n".join(b))

# ===========================================================================
# Slide 3 - Motivation  (4 chunks)
# ===========================================================================
def s03():
    sid = "motivation"
    head, y0 = frame("Motivation", "Two open questions — and a metric problem", idx="03 / 10")
    b = [head]
    lw = 596; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 1: Q1 can a model explain and stay accurate (left upper)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, lw, 200, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(76, y0+52, "Q1", 34, ACCENT, 800, MONO))
    body.append(T(140, y0+42, "Can a VQA model generate a", 19, INK, 700))
    body.append(T(140, y0+68, "human-readable explanation...", 19, INK, 700))
    body.append(paragraph(76, y0+118, "...while still maintaining its answer accuracy? The explanation should never cost the model its correctness.", 15, SUB, maxchars=58, lh=24))
    b.append(cue(a0, k0, "Two open questions drive first can VQA model generate human-readable explanation maintaining answer accuracy.", "\n".join(body)))
    # chunk 2: Q2 how good and how to evaluate (left lower)
    a1, k1 = anchor(sid, 1)
    yy = y0 + 222
    body = [rrect(56, yy, lw, 196, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(T(76, yy+52, "Q2", 34, TEAL, 800, MONO))
    body.append(T(140, yy+42, "How good are those explanations,", 19, INK, 700))
    body.append(T(140, yy+68, "and how do we even evaluate them?", 19, INK, 700))
    body.append(paragraph(76, yy+118, "Explanation quality has no agreed, reliable measure to judge whether it genuinely supports the answer.", 15, SUB, maxchars=58, lh=24))
    b.append(cue(a1, k1, "Second how good those generated explanations how should we even evaluate them.", "\n".join(body)))
    # chunk 3: existing metrics are string-matching (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, y0, rw, 270, CARD, RED, rx=14, sw=1.2)]
    body.append(tick(rx0+20, y0+26, h=32, fill=RED))
    body.append(T(rx0+42, y0+46, "BLEU / ROUGE were built for", 17, INK, 700))
    body.append(T(rx0+42, y0+70, "string matching, not reasoning", 17, INK, 700))
    body.append(paragraph(rx0+20, y0+112, "These metrics score overlapping n-grams; they say nothing about whether an explanation truly supports an answer.", 15, SUB, maxchars=44, lh=24))
    body.append(rrect(rx0+20, y0+212, rw-40, 40, "#301B27", RED, rx=10))
    body.append(T(rx0+38, y0+238, "n-gram overlap  is not  valid reasoning", 14.5, RED, 700, MONO))
    b.append(cue(a2, k2, "Existing explainable-VQA datasets suggest conventional natural language metrics BLEU ROUGE designed string matching n-grams.", "\n".join(body)))
    # chunk 4: interpretability is urgent (right lower)
    a3, k3 = anchor(sid, 3)
    yy = y0 + 292
    body = [rrect(rx0, yy, rw, 126, CARD2, WARM, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+26, h=74, fill=WARM))
    body.append(paragraph(rx0+42, yy+44, "As reasoning problems in VQA grow more complex, an interpretable, well-evaluated explanation is no longer optional but urgent.", 15.5, INK, maxchars=44, lh=26, weight=600))
    b.append(cue(a3, k3, "Authors argue reasoning problems VQA grow more complex interpretable well-evaluated explanation urgent.", "\n".join(body)))
    write("03_motivation.svg", "\n".join(b))

# ===========================================================================
# Slide 4 - Contribution  (4 chunks)
# ===========================================================================
def s04():
    sid = "contribution"
    head, y0 = frame("Contribution", "Two-fold: a method, and an evaluation warning", idx="04 / 10")
    b = [head]
    # chunk 1: contribution is two-fold (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 60, CARD, STROKE)]
    body.append(tick(76, y0+17, h=26, fill=ACCENT))
    body.append(T(96, y0+38, "The contribution is two-fold: a simple explanation method, and evidence that evaluation is the bottleneck.", 17.5, INK, 700))
    b.append(cue(a0, k0, "Contribution two-fold.", "\n".join(body)))
    cy = y0 + 84
    cw = (W - 112 - 24) / 2; ch = 292
    xs = [56, 56+cw+24]
    # chunk 2: simple methods maintain accuracy (left)
    a1, k1 = anchor(sid, 1)
    x = xs[0]
    body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+24, cy+30, h=36, fill=TEAL))
    body.append(T(x+cw-24, cy+62, "01", 46, TEAL, 800, MONO, anchor="end", opacity=0.5))
    body.append(T(x+44, cy+56, "A simple, drop-in method", 21, INK, 700))
    body.append(paragraph(x+44, cy+100, "Easy-to-implement modules sit on top of a state-of-the-art VQA framework and maintain VQA accuracy while generating human-readable textual explanations.", 15.5, SUB, maxchars=42, lh=26))
    body.append(rrect(x+24, cy+ch-62, cw-48, 44, CARD2, TEAL, rx=10, sw=1.1))
    body.append(T(x+cw/2, cy+ch-34, "accuracy kept  +  explanations added", 14.5, TEAL, 700, anchor="middle"))
    b.append(cue(a1, k1, "First authors present simple easy-to-implement methods top state-of-the-art VQA framework maintain accuracy human-readable.", "\n".join(body)))
    # chunk 3: experiments + human study (right)
    a2, k2 = anchor(sid, 2)
    x = xs[1]
    body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+24, cy+30, h=36, fill=WARM))
    body.append(T(x+cw-24, cy+62, "02", 46, WARM, 800, MONO, anchor="end", opacity=0.5))
    body.append(T(x+44, cy+56, "Quantitative + a human study", 21, INK, 700))
    body.append(paragraph(x+44, cy+100, "Both quantitative experimental results and a large human study of the proposed explainable VQA method give the evidence behind the claims.", 15.5, SUB, maxchars=42, lh=26))
    body.append(rrect(x+24, cy+ch-62, cw-48, 44, CARD2, WARM, rx=10, sw=1.1))
    body.append(T(x+cw/2, cy+ch-34, "14,205 human judgements", 14.5, WARM, 700, anchor="middle"))
    b.append(cue(a2, k2, "Second they provide both quantitative experimental results large human study proposed explainable VQA method.", "\n".join(body)))
    # chunk 4: urgency of new metrics (band)
    a3, k3 = anchor(sid, 3)
    yy = cy + ch + 18
    body = [rrect(56, yy, W-112, 58, CARD2, RED, rx=12, sw=1.2)]
    body.append(tick(76, yy+16, h=26, fill=RED))
    body.append(T(96, yy+37, "Together they show the urgency of new metrics: today's do not reliably reflect explanation quality.", 16.5, INK, 600))
    b.append(cue(a3, k3, "Together these illustrate urgency proposing new metrics evaluate predicted explanations vision-language reasoning.", "\n".join(body)))
    write("04_contribution.svg", "\n".join(b))

# ===========================================================================
# Slide 5 - Method  (4 chunks)
# ===========================================================================
def s05():
    sid = "method"
    head, y0 = frame("Method", "Coarse-to-fine reasoning + an explanation head", idx="05 / 10")
    b = [head]
    # chunk 1: two major parts + inputs (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 96, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(76, y0+30, "Two parts: coarse-to-fine visual-language reasoning for the answer + an explanation generator", 16, ACCENT, 700))
    body.append(T(76, y0+60, "Faster-RCNN region features & image predicates (GloVe)   ·   question via GloVe + GRU   ·   question predicates via stop-word filter", 13.5, SUB))
    body.append(T(76, y0+82, "f_I , p_I , f_Q , p_Q   ->   CFR backbone", 14, INK, 700, MONO))
    b.append(cue(a0, k0, "Architecture two major parts coarse-to-fine visual-language reasoning answer explanation generation Faster-RCNN GloVe GRU.", "\n".join(body)))
    cy = y0 + 116
    cw = (W - 112 - 2*22) / 3; ch = 176
    xs = [56, 56+cw+22, 56+2*(cw+22)]
    mods = [
        (0, "Information filtering", ACCENT, "Removes noisy region information before fusion."),
        (1, "Multimodal learning", TEAL, "Bilinear attention networks fuse image + question at coarse and fine granularity."),
        (2, "Semantic reasoning", VIOLET, "Combines both levels into one joint embedding."),
    ]
    # chunk 2: three modules -> joint embedding
    a1, k1 = anchor(sid, 1)
    body = []
    for i, ti, col, desc in mods:
        x = xs[i]
        body.append(rrect(x, cy, cw, ch, CARD, STROKE))
        body.append(tick(x+22, cy+26, h=28, fill=col))
        body.append(T(x+40, cy+46, f"{i+1}  {ti}", 16, col, 700))
        body.append(paragraph(x+22, cy+82, desc, 14, SUB, maxchars=38, lh=21))
    body.append(T(xs[0]+cw+11, cy+ch/2+6, "→", 24, MUT, 800, anchor="middle"))
    body.append(T(xs[1]+cw+11, cy+ch/2+6, "→", 24, MUT, 800, anchor="middle"))
    b.append(cue(a1, k1, "These signals flow through three modules information filtering multimodal learning bilinear attention semantic reasoning joint.", "\n".join(body)))
    cy2 = cy + ch + 20
    lw = 596; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 3: joint embedding -> MLP answer + explanation generator (left lower)
    a2, k2 = anchor(sid, 2)
    body = [rrect(56, cy2, lw, 120, CARD, STROKE)]
    body.append(T(76, cy2+34, "Joint embedding feeds two heads", 16, INK, 700))
    hcw = (lw - 40 - 20) / 2
    body.append(rrect(76, cy2+52, hcw, 50, CARD2, GREEN, rx=10, sw=1.1))
    body.append(T(76+hcw/2, cy2+74, "MLP  →  answer", 14.5, INK, 700, anchor="middle"))
    body.append(T(76+hcw/2, cy2+92, "answer prediction", 12, SUB, anchor="middle"))
    body.append(rrect(76+hcw+20, cy2+52, hcw, 50, CARD2, WARM, rx=10, sw=1.1))
    body.append(T(76+hcw+20+hcw/2, cy2+74, "2-layer LSTM  /  8-head Transformer", 12.5, INK, 700, anchor="middle"))
    body.append(T(76+hcw+20+hcw/2, cy2+92, "explanation generator", 12, SUB, anchor="middle"))
    b.append(cue(a2, k2, "Joint embedding sent both multi-layer perceptron answer prediction explanation generator two-layer LSTM eight-head Transformer.", "\n".join(body)))
    # chunk 4: end-to-end combined loss (right lower)
    a3, k3 = anchor(sid, 3)
    body = [rrect(rx0, cy2, rw, 120, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(rx0+20, cy2+34, "Trained end-to-end", 15, ACCENT, 700))
    body.append(T(rx0+20, cy2+74, "L = alpha * L_ans + (1 - alpha) * L_expl", 16, INK, 700, MONO))
    body.append(T(rx0+20, cy2+100, "answer term + explanation term, balanced by alpha", 12.5, SUB))
    b.append(cue(a3, k3, "Whole system trained end-to-end combined loss balances answer term explanation term factor alpha teacher forcing.", "\n".join(body)))
    write("05_method.svg", "\n".join(b))

# ===========================================================================
# Slide 6 - Dataset / Benchmark  (4 chunks)
# ===========================================================================
def s06():
    sid = "dataset-benchmark"
    head, y0 = frame("Benchmark", "Two datasets with annotated explanations", idx="06 / 10")
    b = [head]
    # chunk 1: very few datasets, chose the two largest (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 60, CARD, STROKE)]
    body.append(tick(76, y0+17, h=26, fill=TEAL))
    body.append(T(96, y0+38, "Very few datasets pair explanations with answers — the authors chose the two largest available.", 17.5, INK, 700))
    b.append(cue(a0, k0, "Because very few datasets provide annotated explanations alongside answers authors chose two largest available.", "\n".join(body)))
    cy = y0 + 84
    cw = (W - 112 - 24) / 2; ch = 356
    xs = [56, 56+cw+24]
    # chunk 2: GQA-REX stats (left upper metrics)
    a1, k1 = anchor(sid, 1)
    x = xs[0]
    body = [rrect(x, cy, cw, ch, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(x+22, cy+28, h=32, fill=ACCENT))
    body.append(T(x+42, cy+50, "GQA-REX", 23, ACCENT, 800))
    body.append(T(x+42, cy+76, "explanations for ~98% of GQA-balanced", 14.5, SUB))
    tiles = [("1.04M", "QA pairs"), ("82K", "images"), ("1", "explanation / pair")]
    tw = (cw - 44 - 2*16) / 3
    for i, (big, lab) in enumerate(tiles):
        tx = x + 22 + i*(tw+16)
        body.append(rrect(tx, cy+98, tw, 96, CARD, STROKE, rx=10))
        body.append(T(tx+tw/2, cy+148, big, 27, INK, 800, anchor="middle"))
        body.append(T(tx+tw/2, cy+174, lab, 11.5, SUB, anchor="middle"))
    body.append(rrect(x+22, cy+214, cw-44, 120, "#301B27", RED, rx=12, sw=1.2))
    b.append(cue(a1, k1, "GQA-REX contains explanations roughly ninety-eight percent GQA-balanced dataset 1.04 million question-answer pairs eighty-two thousand images.", "\n".join(body)))
    # chunk 3: GQA-REX limitation (overlay text on the red box)
    a2, k2 = anchor(sid, 2)
    body = [tick(x+40, cy+236, h=76, fill=RED)]
    body.append(T(x+58, cy+256, "But: reasoning-format, not fully", 15.5, RED, 700))
    body.append(T(x+58, cy+278, "human-readable", 15.5, RED, 700))
    body.append(paragraph(x+58, cy+306, "follows the reasoning-format of prior work, sometimes with grammatical inaccuracies.", 13.5, SUB, maxchars=48, lh=20))
    b.append(cue(a2, k2, "However its explanations follow reasoning-format prior work not fully human-readable grammatical inaccuracies.", "\n".join(body)))
    # chunk 4: VQA-E (right)
    a3, k3 = anchor(sid, 3)
    x = xs[1]
    body = [rrect(x, cy, cw, ch, CARD2, WARM, rx=14, sw=1.3)]
    body.append(tick(x+22, cy+28, h=32, fill=WARM))
    body.append(T(x+42, cy+50, "VQA-E", 23, WARM, 800))
    body.append(T(x+42, cy+76, "explanations for ~40% of VQA 2.0 QA pairs", 14.5, SUB))
    body.append(rrect(x+22, cy+98, cw-44, 96, CARD, STROKE, rx=10))
    body.append(T(x+cw/2, cy+150, "~40%", 32, INK, 800, anchor="middle"))
    body.append(T(x+cw/2, cy+176, "of VQA 2.0 question-answer pairs", 12.5, SUB, anchor="middle"))
    body.append(rrect(x+22, cy+214, cw-44, 120, "#332A18", WARM, rx=12, sw=1.2))
    body.append(tick(x+40, cy+236, h=76, fill=WARM))
    body.append(T(x+58, cy+256, "But: built by matching captions", 15.5, WARM, 700))
    body.append(paragraph(x+58, cy+286, "so they read more like image captions than genuine reasoning. Both datasets have acknowledged limitations.", 13.5, SUB, maxchars=48, lh=20))
    b.append(cue(a3, k3, "VQA-E provides explanations about forty percent question-answer pairs VQA 2.0 built matching captions read like image captions.", "\n".join(body)))
    write("06_dataset-benchmark.svg", "\n".join(b))

# ===========================================================================
# Slide 7 - Key Result  (4 chunks)
# ===========================================================================
def s07():
    sid = "key-result"
    head, y0 = frame("Key Result", "Explanations come essentially for free", idx="07 / 10")
    b = [head]
    # chunk 1: adding explanation does not cost accuracy (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD2, GREEN, rx=12, sw=1.3)]
    body.append(tick(76, y0+16, h=26, fill=GREEN))
    body.append(T(96, y0+37, "The central result: adding explanation generation does not cost answer accuracy.", 18, INK, 700))
    b.append(cue(a0, k0, "Central result adding explanation generation does not cost accuracy.", "\n".join(body)))
    cy = y0 + 80
    lw = 596; ch = 296; x = 56
    # chunk 2: VQA scores match baseline (left chart card)
    a1, k1 = anchor(sid, 1)
    body = [rrect(x, cy, lw, ch, CARD, STROKE)]
    body.append(T(x+24, cy+40, "VQA score matches the explanation-free baseline", 16.5, INK, 700))
    # grouped bars: GQA-REX and VQA-E, baseline vs ours
    gx, gy, gh = x+60, cy+72, 150
    groups = [("GQA-REX", 77.55, 77.49), ("VQA-E", 71.55, 71.48)]
    gwid = (lw-100)/2
    for gi, (lab, base, ours) in enumerate(groups):
        bx = gx + gi*gwid
        bw = 62
        for j,(v,col,nm) in enumerate([(base, MUT, "baseline"), (ours, ACCENT, "+ explain")]):
            h = (v-60)/20*gh
            xx = bx + j*(bw+22)
            body.append(rrect(xx, gy+gh-h, bw, h, col, "", rx=5))
            body.append(T(xx+bw/2, gy+gh-h-8, f"{v:.2f}", 12.5, INK, 700, anchor="middle"))
            body.append(T(xx+bw/2, gy+gh+16, nm, 11, MUT, 600, anchor="middle"))
        body.append(T(bx+bw+11, gy+gh+36, lab, 13.5, INK, 700, anchor="middle"))
    body.append(T(x+24, cy+ch-14, "Varying the balance factor alpha changes the trade-off only marginally.", 13, SUB))
    b.append(cue(a1, k1, "GQA-REX reaches VQA score seventy-seven point four nine percent VQA-E seventy-one point four eight matching baseline.", "\n".join(body)))
    rx0 = x + lw + 24; rw = W - 56 - rx0
    # chunk 3: explanation quality beats prior baseline on VQA-E (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 176, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(rx0+20, cy+22, h=28, fill=TEAL))
    body.append(T(rx0+40, cy+42, "CFRF + LSTM beats prior on VQA-E", 14.5, TEAL, 700))
    metr = [("BLEU-1", "0.268", "0.33"), ("ROUGE-L", "0.249", "0.325")]
    ry = cy+72
    body.append(T(rx0+20, ry, "metric", 12, MUT, 700, MONO))
    body.append(T(rx0+rw-110, ry, "prior", 12, MUT, 700, MONO, anchor="end"))
    body.append(T(rx0+rw-20, ry, "ours", 12, GREEN, 700, MONO, anchor="end"))
    ry += 26
    for nm, prior, ours in metr:
        body.append(T(rx0+20, ry, nm, 14.5, INK, 700))
        body.append(T(rx0+rw-110, ry, prior, 14.5, SUB, 600, MONO, anchor="end"))
        body.append(T(rx0+rw-20, ry, ours, 15.5, GREEN, 800, MONO, anchor="end"))
        ry += 30
    b.append(cue(a2, k2, "Explanations themselves CFRF-plus-LSTM outperforms prior baseline VQA-E BLEU-1 zero point three three ROUGE-L.", "\n".join(body)))
    # chunk 4: candid - only satisfactory (right lower)
    a3, k3 = anchor(sid, 3)
    yy = cy + 196
    body = [rrect(rx0, yy, rw, 100, CARD, WARM, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+22, h=30, fill=WARM))
    body.append(paragraph(rx0+40, yy+40, "The authors are candid: these absolute numbers are only satisfactory — which sets up their evaluation argument.", 14, INK, maxchars=46, lh=22, weight=600))
    b.append(cue(a3, k3, "Authors candid these absolute numbers only satisfactory sets up their argument about evaluation.", "\n".join(body)))
    write("07_key-result.svg", "\n".join(b))

# ===========================================================================
# Slide 8 - Ablation Study  (4 chunks)
# ===========================================================================
def s08():
    sid = "ablation-study"
    head, y0 = frame("Ablation", "Accuracy is stable under every sweep", idx="08 / 10")
    b = [head]
    # chunk 1: ablate alpha and generator choice (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 60, CARD, STROKE)]
    body.append(tick(76, y0+17, h=26, fill=ACCENT))
    body.append(T(96, y0+38, "Two knobs swept: the loss balance factor alpha, and the explanation generator (LSTM vs Transformer).", 17, INK, 700))
    b.append(cue(a0, k0, "Authors ablate two design choices balance factor alpha weights answer loss explanation loss choice generator.", "\n".join(body)))
    cy = y0 + 82
    lw = 596; ch = 300; x = 56
    # chunk 2: GQA-REX sweep (left chart)
    a1, k1 = anchor(sid, 1)
    body = [rrect(x, cy, lw, ch, CARD, STROKE)]
    body.append(T(x+24, cy+38, "GQA-REX — VQA score across alpha", 16.5, INK, 700))
    gx, gy, gw, gh = x+56, cy+66, lw-96, 168
    # baseline reference at 77.49
    body.append(f'<line x1="{gx}" y1="{gy}" x2="{gx+gw}" y2="{gy}" stroke="{MUT}" stroke-width="1"/>')
    lo, hi = 74.0, 78.0
    def yv(v): return gy + (hi-v)/(hi-lo)*gh
    # baseline dashed
    yb = yv(77.49)
    body.append(f'<line x1="{gx}" y1="{yb:.1f}" x2="{gx+gw}" y2="{yb:.1f}" stroke="{GREEN}" stroke-width="1.2" stroke-dasharray="5 4"/>')
    body.append(T(gx+gw, yb-6, "baseline 77.49", 11.5, GREEN, 700, anchor="end"))
    bars = [("0.3", 75.08, ACCENT), ("0.5", 77.06, ACCENT), ("0.7", 77.20, ACCENT), ("0.9", 77.49, ACCENT), ("T,0.5", 77.06, WARM)]
    bw = gw/(len(bars)*1.5)
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    for i,(lab,v,col) in enumerate(bars):
        bx = gx + i*(gw/len(bars)) + (gw/len(bars)-bw)/2
        h = (v-lo)/(hi-lo)*gh
        body.append(rrect(bx, gy+gh-h, bw, h, col, "", rx=4))
        body.append(T(bx+bw/2, gy+gh-h-7, f"{v:.1f}", 11, INK, 700, anchor="middle"))
        body.append(T(bx+bw/2, gy+gh+16, lab, 10.5, MUT, 600, anchor="middle"))
    body.append(T(x+24, cy+ch-14, "LSTM 75.08–77.49% across alpha; Transformer (alpha=0.5) reaches 77.06%.", 13, SUB))
    b.append(cue(a1, k1, "GQA-REX LSTM variant ranges about seventy-five seventy-seven half percent across alpha Transformer decoder reaches.", "\n".join(body)))
    rx0 = x + lw + 24; rw = W - 56 - rx0
    # chunk 3: VQA-E all within a fraction (right upper)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 176, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(rx0+20, cy+22, h=28, fill=TEAL))
    body.append(T(rx0+40, cy+42, "VQA-E: flat as a line", 16, TEAL, 700))
    body.append(T(rx0+20, cy+92, "71.32 – 71.55%", 30, INK, 800, MONO))
    body.append(T(rx0+20, cy+120, "every configuration", 13.5, SUB))
    body.append(paragraph(rx0+20, cy+144, "within a fraction of a percent of the 71.5% baseline.", 13.5, SUB, maxchars=42))
    b.append(cue(a2, k2, "VQA-E every configuration lands within fraction percent seventy-one half percent baseline.", "\n".join(body)))
    # chunk 4: takeaway - stable regardless (right lower)
    a3, k3 = anchor(sid, 3)
    yy = cy + 196
    body = [rrect(rx0, yy, rw, 104, CARD, GREEN, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+22, h=30, fill=GREEN))
    body.append(paragraph(rx0+40, yy+40, "Accuracy is remarkably stable regardless of loss weight or decoder — the explanation module is essentially free.", 14, INK, maxchars=46, lh=22, weight=600))
    b.append(cue(a3, k3, "Takeaway these sweeps answer accuracy remarkably stable no matter explanation loss weighted decoder added free.", "\n".join(body)))
    write("08_ablation-study.svg", "\n".join(b))

# ===========================================================================
# Slide 9 - Headline Numbers  (4 chunks)
# ===========================================================================
def s09():
    sid = "headline-numbers"
    head, y0 = frame("By the Numbers", "Impact and the human study", idx="09 / 10")
    b = [head]
    # chunk 1: four numbers + accuracy tiles
    a0, k0 = anchor(sid, 0)
    yy = y0
    tw = (W-112-3*20)/4; th = 150
    xs = [56 + i*(tw+20) for i in range(4)]
    tiles = [
        ("77.49%", ACCENT, "VQA score", "GQA-REX"),
        ("71.48%", TEAL, "VQA score", "VQA-E"),
        ("65.16%", WARM, "explanations judged", "to lead to the answer"),
        ("~60.5%", GREEN, "correct answer +", "valid explanation"),
    ]
    body = []
    for (big, col, lab, lab2), x in zip(tiles, xs):
        body.append(rrect(x, yy, tw, th, CARD, STROKE))
        body.append(tick(x+22, yy+24, h=24, fill=col))
        body.append(T(x+tw/2, yy+92, big, 40, col, 800, anchor="middle"))
        body.append(T(x+tw/2, yy+120, lab, 12.5, SUB, 600, anchor="middle"))
        body.append(T(x+tw/2, yy+138, lab2, 11.5, MUT, 500, anchor="middle"))
    b.append(cue(a0, k0, "Four numbers summarize paper impact achieves seventy-seven point four nine percent GQA-REX seventy-one point four eight VQA-E.", "\n".join(body)))
    cy = yy + th + 22
    lw = 584; hh = 152
    # chunk 2: human study 65.16% explanations lead to answer (left)
    a1, k1 = anchor(sid, 1)
    body = [rrect(56, cy, lw, hh, CARD2, WARM, rx=14, sw=1.3)]
    body.append(tick(76, cy+24, h=30, fill=WARM))
    body.append(T(96, cy+44, "Human study: do explanations lead to the answer?", 15.5, WARM, 700))
    body.append(T(96, cy+96, "65.16%", 42, INK, 800))
    body.append(paragraph(300, cy+82, "of generated explanations were judged by annotators to genuinely lead to the predicted answer.", 13.5, SUB, maxchars=40, lh=20))
    b.append(cue(a1, k1, "Human study sixty-five point one six percent generated explanations judged annotators genuinely lead predicted answer.", "\n".join(body)))
    # chunk 3: 60.5% both correct + valid (right)
    a2, k2 = anchor(sid, 2)
    rx0 = 56 + lw + 24; rw = W - 56 - rx0
    body = [rrect(rx0, cy, rw, hh, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(tick(rx0+22, cy+24, h=30, fill=GREEN))
    body.append(T(rx0+42, cy+44, "Both right, together", 15.5, GREEN, 700))
    body.append(T(rx0+22, cy+100, "~60.5%", 40, INK, 800))
    body.append(paragraph(rx0+210, cy+86, "of cases give a correct answer AND a valid explanation for it.", 13.5, SUB, maxchars=34, lh=20))
    b.append(cue(a2, k2, "Roughly sixty point five percent cases model both predicts correct answer generates valid explanation.", "\n".join(body)))
    # chunk 4: study scale (band)
    a3, k3 = anchor(sid, 3)
    yy2 = cy + hh + 18
    body = [rrect(56, yy2, W-112, 56, CARD, STROKE)]
    body.append(tick(76, yy2+16, h=24, fill=ACCENT))
    body.append(T(96, yy2+36, "A substantial study: 4,735 image-question pairs  ·  3 annotators each  ·  14,205 responses from 111 subjects", 16, INK, 700))
    b.append(cue(a3, k3, "Human study itself substantial four thousand seven hundred thirty-five unique image-question pairs three annotators fourteen thousand.", "\n".join(body)))
    write("09_headline-numbers.svg", "\n".join(b))

# ===========================================================================
# Slide 10 - Takeaway  (4 chunks)
# ===========================================================================
def s10():
    sid = "takeaway"
    head, y0 = frame("Takeaway", "Explanations are cheap; evaluation is the bottleneck", idx="10 / 10")
    b = [head]
    # chunk 1: message is twofold (band)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 52, CARD, STROKE)]
    body.append(tick(76, y0+15, h=24, fill=ACCENT))
    body.append(T(96, y0+34, "The lasting message is twofold — one practical, one methodological.", 18, INK, 700))
    b.append(cue(a0, k0, "Lasting message twofold.", "\n".join(body)))
    cy = y0 + 72
    cw = (W - 112 - 24) / 2; ch = 158
    xs = [56, 56+cw+24]
    # chunk 2: practically - explanations for free (left)
    a1, k1 = anchor(sid, 1)
    x = xs[0]
    body = [rrect(x, cy, cw, ch, CARD2, GREEN, rx=14, sw=1.3)]
    body.append(tick(x+22, cy+24, h=30, fill=GREEN))
    body.append(T(x+42, cy+44, "Practically", 16, GREEN, 700))
    body.append(paragraph(x+22, cy+80, "Explanation generation can be bolted onto a state-of-the-art VQA backbone with almost no loss in answer accuracy — a human-readable reason with every answer.", 14.5, SUB, maxchars=48, lh=22))
    b.append(cue(a1, k1, "Practically explanation generation added state-of-the-art VQA backbone almost no loss answer accuracy human-readable reason.", "\n".join(body)))
    # chunk 3: methodologically - metrics unreliable (right)
    a2, k2 = anchor(sid, 2)
    x = xs[1]
    body = [rrect(x, cy, cw, ch, CARD2, RED, rx=14, sw=1.3)]
    body.append(tick(x+22, cy+24, h=30, fill=RED))
    body.append(T(x+42, cy+44, "Methodologically", 16, RED, 700))
    body.append(paragraph(x+22, cy+80, "Concrete examples show BLEU and ROUGE can reward a wrong explanation and penalize a valid one — they are unreliable for this task.", 14.5, SUB, maxchars=48, lh=22))
    b.append(cue(a2, k2, "But methodologically shows through concrete examples string-matching metrics BLEU ROUGE reward wrong penalize valid unreliable.", "\n".join(body)))
    # chunk 4: the real bottleneck is evaluation (band)
    a3, k3 = anchor(sid, 3)
    yy = cy + ch + 18
    body = [rrect(56, yy, W-112, 96, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(76, yy+22, h=52, fill=ACCENT))
    body.append(T(96, yy+44, "The real bottleneck is not the generator — it is the evaluation.", 20, INK, 800))
    body.append(T(96, yy+74, "The authors urge the community to develop proper reasoning-aware metrics for judging explanations.", 15, SUB))
    b.append(cue(a3, k3, "Authors therefore argue real bottleneck explainable VQA not generator evaluation urge reasoning-aware metrics judging.", "\n".join(body)))
    # footer
    b.append(f'<line x1="56" y1="{yy+118}" x2="{W-56}" y2="{yy+118}" stroke="{STROKE}" stroke-width="1.2"/>')
    b.append(T(56, yy+146, "Towards Reasoning-Aware Explainable VQA  ·  NeurIPS 2022", 14.5, SUB, 500))
    b.append(T(W-56, yy+146, "arxiv.org/abs/2211.05190", 14, ACCENT, 600, MONO, anchor="end"))
    write("10_takeaway.svg", "\n".join(b))

for fn in [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10]:
    fn()
print("done")
