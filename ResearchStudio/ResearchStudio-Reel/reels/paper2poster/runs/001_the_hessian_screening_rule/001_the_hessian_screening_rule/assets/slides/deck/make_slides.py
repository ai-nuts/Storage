#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video.

Paper: The Hessian Screening Rule (Larsson & Wallin, NeurIPS 2022).

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
GREEN   = "#57D9A3"   # success / Hessian rule
RED     = "#F2708A"   # baselines / cost

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
    b.append(T(56, 116, title, 38, INK, 800))
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
    # chunk 1: kicker + title block + authors
    a0, k0 = anchor(sid, 0)
    body = []
    body.append(tick(72, 92, h=30, w=6, fill=ACCENT))
    body.append(T(92, 104, "LASSO  ·  REGULARIZATION PATH  ·  SCREENING RULES", 15, ACCENT, 700, SANS, spacing=2.5))
    body.append(T(92, 134, "NeurIPS 2022  ·  a faster way to fit the whole lasso path", 16, SUB, 400))
    body.append(T(72, 210, "The Hessian Screening Rule", 60, INK, 800))
    body.append(T(72, 252, "Second-order screening and warm starts for sparse regression", 22, SUB, 500))
    b.append(cue(a0, k0, "This work NeurIPS 2022 Johan Larsson Jonas Wallin Lund introduces Hessian Screening Rule speed lasso path.", "\n".join(body)))
    # chunk 2: screening rules discard predictors card
    a1, k1 = anchor(sid, 1)
    body = []
    body.append(rrect(72, 300, 560, 118, CARD, STROKE, rx=16))
    body.append(tick(92, 324, h=70, w=6, fill=TEAL))
    body.append(T(112, 338, "What a screening rule does", 18, TEAL, 800))
    body.append(T(112, 368, "Discards predictors before the model is fit,", 15, SUB))
    body.append(T(112, 390, "shrinking each subproblem the solver has to touch.", 15, SUB))
    b.append(cue(a1, k1, "Screening rules discard predictors before model fit shrinking problem.", "\n".join(body)))
    # chunk 3: hero card - second-order Hessian, two wins, high correlation
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(660, 300, 548, 118, CARD2, ACCENT, rx=16, sw=1.4))
    body.append(T(684, 338, "SECOND-ORDER HESSIAN INFORMATION", 12.5, ACCENT, 700, SANS, spacing=1.5))
    body.append(T(684, 372, "Far tighter screening", 18, GREEN, 700))
    body.append(T(684, 398, "+ much more accurate warm starts", 16, INK, 600))
    body.append(T(1184, 372, "even under", 13, SUB, anchor="end"))
    body.append(T(1184, 392, "high correlation", 14, WARM, 700, anchor="end"))
    b.append(cue(a2, k2, "Authors show second-order Hessian information tighter screening accurate warm starts highly correlated struggle.", "\n".join(body)))
    # chunk 4: fastest stat card
    a3, k3 = anchor(sid, 3)
    body = []
    body.append(rrect(72, 440, W-144, 96, CARD, STROKE, rx=16))
    body.append(tick(92, 462, h=52, w=6, fill=WARM))
    body.append(T(112, 486, "Fastest", 30, "url(#warmg)", 800))
    body.append(T(250, 486, "across nearly every simulated and real benchmark tested", 18, INK, 600))
    body.append(T(112, 516, "lasso and l1-regularized logistic regression paths", 14.5, SUB))
    b.append(cue(a3, k3, "Result method fastest across nearly every simulated real benchmark tested.", "\n".join(body)))
    # footer
    b.append(f'<line x1="72" y1="566" x2="{W-72}" y2="566" stroke="{STROKE}" stroke-width="1.2" />')
    b.append(T(72, 602, "Johan Larsson   ·   Jonas Wallin", 21, INK, 700))
    b.append(T(72, 628, "Department of Statistics, Lund University", 15, SUB))
    b.append(T(W-72, 602, "NeurIPS 2022", 14, ACCENT, 700, SANS, spacing=1.5, anchor="end"))
    b.append(T(W-72, 628, "arXiv:2104.13026   ·   github.com/jolars/HessianScreening", 13.5, MUT, 500, MONO, anchor="end"))
    write("01_title.svg", "\n".join(b))

# ===========================================================================
# Slide 2 - Problem
# ===========================================================================
def s02():
    sid = "problem"
    head, y0 = frame("Problem", "Fitting the lasso path is expensive", idx="02 / 09")
    b = [head]
    # chunk 1: intro band
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 84, CARD, STROKE)]
    body.append(tick(76, y0+20, h=44))
    body.append(T(96, y0+38, "The lasso is a workhorse for high-dimensional sparse regression", 20, INK, 700))
    body.append(T(96, y0+64, "but actually fitting it is computationally expensive", 15, SUB))
    b.append(cue(a0, k0, "Sparse regression lasso workhorse high-dimensional data fitting expensive.", "\n".join(body)))
    cy = y0 + 104
    cw = (W - 112 - 2*24) / 3
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    ch = 306
    # chunk 2: unknown penalty -> whole path + CV
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+82, "The penalty is unknown", 18, INK, 700))
    body.append(paragraph(x+22, cy+114, "The best penalty strength is never known in advance, so you fit an entire path of models and tune by cross-validation.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+214, cw-44, 68, "#301B27", RED, rx=12, sw=1.2))
    body.append(T(x+38, cy+248, "refit again and again", 17, RED, 800))
    body.append(T(x+38, cy+270, "many penalty values x CV folds", 12.5, SUB))
    b.append(cue(a1, k1, "Best penalty strength never known fit entire path cross-validation refitting again.", "\n".join(body)))
    # chunk 3: screening rules help
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=TEAL))
    body.append(T(x+22, cy+82, "Screening rules help", 18, INK, 700))
    body.append(paragraph(x+22, cy+114, "They discard predictors before the solver even runs, shrinking each subproblem it has to solve.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+214, cw-44, 68, "#12312B", TEAL, rx=12, sw=1.2))
    body.append(T(x+38, cy+248, "fewer predictors", 17, TEAL, 800))
    body.append(T(x+38, cy+270, "smaller problem per solve", 12.5, SUB))
    b.append(cue(a2, k2, "Screening rules help discarding predictors before solver runs shrinking subproblem.", "\n".join(body)))
    # chunk 4: trouble - conservative under correlation
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=WARM))
    body.append(T(x+22, cy+82, "But they break down", 18, INK, 700))
    body.append(paragraph(x+22, cy+114, "The widely used rules turn conservative and inefficient exactly when predictors are strongly correlated.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+214, cw-44, 68, "#332A18", WARM, rx=12, sw=1.2))
    body.append(T(x+38, cy+248, "high correlation", 17, WARM, 800))
    body.append(T(x+38, cy+270, "the regime where speed matters most", 12, SUB))
    b.append(cue(a3, k3, "Trouble widely used rules become conservative inefficient predictors strongly correlated speed matters.", "\n".join(body)))
    write("02_problem.svg", "\n".join(b))

# ===========================================================================
# Slide 3 - Motivation
# ===========================================================================
def s03():
    sid = "motivation"
    head, y0 = frame("Motivation", "First-order estimates are the bottleneck", idx="03 / 09")
    b = [head]
    lw = 616; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # chunk 1: unifying observation (left top)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, lw, 176, CARD, STROKE)]
    body.append(tick(76, y0+22, h=30))
    body.append(T(96, y0+40, "A unifying observation", 18, INK, 700))
    body.append(paragraph(96, y0+70, "The popular strong rule and the working-set strategy are both estimates of the correlation (the negative gradient) at the next step of the path.", 14.5, SUB, maxchars=62))
    # tiny path axis with next-step marker
    bx, by, bw = 96, y0+140, lw-140
    body.append(f'<line x1="{bx}" y1="{by}" x2="{bx+bw}" y2="{by}" stroke="{MUT}" stroke-width="1.4"/>')
    for i,(fx,lab) in enumerate([(0.0,"lambda_k"),(0.62,"lambda_k+1"),(1.0,"")]):
        px = bx+fx*bw
        body.append(f'<circle cx="{px}" cy="{by}" r="4" fill="{ACCENT if i==0 else (TEAL if i==1 else MUT)}"/>')
        if lab: body.append(T(px, by+20, lab, 12.5, SUB, 600, MONO, anchor="middle"))
    body.append(T(bx+0.62*bw, by-12, "estimate correlation here", 12, TEAL, 700, anchor="middle"))
    b.append(cue(a0, k0, "Authors start unifying observation strong rule working-set strategy estimates gradient correlation next step.", "\n".join(body)))
    # chunk 2: first-order crude -> two costs (right top)
    a1, k1 = anchor(sid, 1)
    body = [rrect(rx0, y0, rw, 176, CARD2, WARM, rx=14, sw=1.3)]
    body.append(tick(rx0+20, y0+22, h=30, fill=WARM))
    body.append(T(rx0+40, y0+40, "First-order = crude", 17, WARM, 700))
    body.append(paragraph(rx0+20, y0+72, "Leaning only on first-order information makes these estimates crude, especially under high correlation.", 14.5, SUB, maxchars=44))
    body.append(rrect(rx0+20, y0+130, rw-40, 30, BG2, "", rx=8))
    body.append(T(rx0+34, y0+150, "one weak estimate -> two costs", 13.5, INK, 700, MONO))
    b.append(cue(a1, k1, "When lean only first-order information estimates crude high correlation two costs.", "\n".join(body)))
    # chunk 3: two costs card (full width)
    a2, k2 = anchor(sid, 2)
    yy = y0 + 196
    body = [rrect(56, yy, W-112, 118, CARD, STROKE)]
    hw = (W-112-24)/2
    body.append(tick(76, yy+22, h=30, fill=RED))
    body.append(T(96, yy+42, "Cost 1  ·  conservative screening", 17, RED, 700))
    body.append(paragraph(96, yy+72, "The rule keeps far more predictors than necessary, so each subproblem stays large.", 14.5, SUB, maxchars=48))
    body.append(f'<line x1="{56+hw+12}" y1="{yy+18}" x2="{56+hw+12}" y2="{yy+100}" stroke="{STROKE}" stroke-width="1"/>')
    body.append(tick(56+hw+36, yy+22, h=30, fill=RED))
    body.append(T(56+hw+56, yy+42, "Cost 2  ·  inaccurate warm starts", 17, RED, 700))
    body.append(paragraph(56+hw+56, yy+72, "The starting point that seeds each solve is off, so the solver needs many more passes to converge.", 14.5, SUB, maxchars=48))
    b.append(cue(a2, k2, "Screening becomes conservative keeping more predictors warm starts inaccurate solver many more passes converge.", "\n".join(body)))
    # chunk 4: same fix band
    a3, k3 = anchor(sid, 3)
    yy2 = yy + 138
    body = [rrect(56, yy2, W-112, 70, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(76, yy2+20, h=30, fill=TEAL))
    body.append(T(96, yy2+34, "Both problems point to the same fix", 19, INK, 800))
    body.append(T(96, yy2+58, "richer curvature information from the Hessian", 15, TEAL, 600))
    b.append(cue(a3, k3, "Both problems point same fix richer curvature information Hessian.", "\n".join(body)))
    write("03_motivation.svg", "\n".join(b))

# ===========================================================================
# Slide 4 - Contribution
# ===========================================================================
def s04():
    sid = "contribution"
    head, y0 = frame("Contribution", "One Hessian, used twice", idx="04 / 09")
    b = [head]
    # chunk 1: intro band
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 66, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(76, y0+18, h=30, fill=ACCENT))
    body.append(T(96, y0+42, "The Hessian Screening Rule exploits second-order information in two complementary ways", 18, INK, 700))
    b.append(cue(a0, k0, "Their contribution Hessian Screening Rule exploits second-order information two complementary ways.", "\n".join(body)))
    cy = y0 + 86
    cw = (W - 112 - 24) / 2; ch = 176
    xs = [56, 56+cw+24]
    # chunk 2: sharper estimate -> tighter screening
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+cw-24, cy+56, "1", 44, GREEN, 800, MONO, anchor="end", opacity=0.5))
    body.append(tick(x+24, cy+28, h=34, fill=GREEN))
    body.append(T(x+44, cy+52, "Sharper next-step estimate", 20, INK, 700))
    body.append(paragraph(x+44, cy+86, "The Hessian gives a much better estimate of the correlation at the next penalty value, which translates into far tighter screening.", 15, SUB, maxchars=52))
    body.append(T(x+44, cy+ch-22, "-> far fewer predictors kept", 14, GREEN, 700))
    b.append(cue(a1, k1, "First Hessian gives sharper estimate correlation next penalty value tighter screening.", "\n".join(body)))
    # chunk 3: warm start near-exact
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+cw-24, cy+56, "2", 44, TEAL, 800, MONO, anchor="end", opacity=0.5))
    body.append(tick(x+24, cy+28, h=34, fill=TEAL))
    body.append(T(x+44, cy+52, "Near-exact warm start", 20, INK, 700))
    body.append(paragraph(x+44, cy+86, "The same Hessian and its inverse give a warm start that is nearly exact whenever the active set does not change.", 15, SUB, maxchars=52))
    body.append(T(x+44, cy+ch-22, "-> solver passes cut dramatically", 14, TEAL, 700))
    b.append(cue(a2, k2, "Second same Hessian inverse yield warm start nearly exact active set unchanged cutting solver passes.", "\n".join(body)))
    # chunk 4: extras band
    a3, k3 = anchor(sid, 3)
    yy = cy + ch + 22
    body = [rrect(56, yy, W-112, 92, CARD, STROKE)]
    cw3 = (W-112)/3
    items = [
        ("Efficient updates", "low-rank updates keep the Hessian and its inverse current"),
        ("General losses", "extends to smooth convex losses like logistic regression"),
        ("Open C++ / R", "a full, released implementation"),
    ]
    for i,(t,d) in enumerate(items):
        xx = 56 + i*cw3 + 20
        body.append(tick(xx, yy+22, h=26, fill=[ACCENT,GREEN,WARM][i]))
        body.append(T(xx+18, yy+40, t, 16, INK, 700))
        body.append(paragraph(xx+18, yy+64, d, 12.5, SUB, maxchars=38, lh=17))
    b.append(cue(a3, k3, "Authors also show update Hessian inverse efficiently active set changes general smooth convex losses logistic C++ R implementation.", "\n".join(body)))
    write("04_contribution.svg", "\n".join(b))

# ===========================================================================
# Slide 5 - Method
# ===========================================================================
def s05():
    sid = "method"
    head, y0 = frame("Method", "Linearity in lambda unlocks the Hessian", idx="05 / 09")
    b = [head]
    # chunk 1: key fact + linearity, equation band
    a0, k0 = anchor(sid, 0)
    eqh = 122
    body = [rrect(56, y0, W-112, eqh, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(76, y0+30, "On any interval where the active set is fixed, the lasso solution is linear in the penalty lambda", 15.5, ACCENT, 700))
    body.append(T(76, y0+72, "beta(lambda) is piecewise-linear   ->   the same slope drives both screening and the warm start", 15, INK, 600))
    body.append(T(76, y0+102, "active set A = { j : beta_j != 0 }   fixed on the interval", 13.5, SUB, 500, MONO))
    b.append(cue(a0, k0, "Method rests simple fact any interval active set nonzero coefficients unchanged lasso solution linear function penalty lambda.", "\n".join(body)))
    cy = y0 + eqh + 20
    cw = (W - 112 - 2*22) / 3; ch = 214
    xs = [56, 56+cw+22, 56+2*(cw+22)]
    # chunk 2: second-order correlation estimate
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "1  Second-order screen", 17, GREEN, 700))
    body.append(paragraph(x+22, cy+70, "Write a second-order estimate of the next-step correlation using the Hessian of the active predictors.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+150, cw-44, 46, BG2, "", rx=9))
    body.append(T(x+36, cy+172, "c_H = c + dl · X^T X_A", 12.5, TEAL, 600, MONO))
    body.append(T(x+36, cy+190, "         (X_A^T X_A)^-1 sign(b_A)", 12.5, TEAL, 600, MONO))
    b.append(cue(a1, k1, "That linearity lets authors write second-order estimate correlation next penalty value Hessian active predictors.", "\n".join(body)))
    # chunk 3: keep cheap + exact warm start
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "2  Keep it cheap", 17, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "Restrict the expensive inner products to the strong-rule set, plus a small unit-bound safety margin. The Hessian inverse also gives the warm start.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+178, cw-44, 24, "#14261F", GREEN, rx=8, sw=1.1))
    body.append(T(x+36, cy+195, "exact -> often one solver pass", 12.5, GREEN, 700, MONO))
    b.append(cue(a2, k2, "Keep cheap restrict expensive inner products strong-rule set unit bound margin Hessian inverse warm start exact single pass.", "\n".join(body)))
    # chunk 4: updates + homotopy
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "3  Stay current", 17, WARM, 700))
    body.append(paragraph(x+22, cy+70, "Efficient low-rank updates keep the Hessian and its inverse current as predictors enter and leave.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+150, cw-44, 46, BG2, "", rx=9))
    body.append(T(x+36, cy+172, "approximate homotopy", 13, WARM, 700))
    body.append(T(x+36, cy+190, "adaptively places the lambda grid", 12, SUB, 500))
    b.append(cue(a3, k3, "Efficient low-rank updates keep Hessian inverse current predictors enter leave approximate-homotopy scheme penalty grid.", "\n".join(body)))
    write("05_method.svg", "\n".join(b))

# ===========================================================================
# Slide 6 - Dataset / Benchmark
# ===========================================================================
def s06():
    sid = "dataset-benchmark"
    head, y0 = frame("Benchmarks", "Simulated sweeps and twelve real data sets", idx="06 / 09")
    b = [head]
    # chunk 1: intro band
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 60, CARD, STROKE)]
    body.append(tick(76, y0+16, h=28, fill=TEAL))
    body.append(T(96, y0+38, "The evaluation covers both carefully controlled simulations and real high-dimensional data", 18, INK, 700))
    b.append(cue(a0, k0, "Experiments cover both simulated real data.", "\n".join(body)))
    cy = y0 + 80
    cw = (W - 112 - 2*24) / 3; ch = 300
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    # chunk 2: simulated designs
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=ACCENT))
    body.append(T(x+22, cy+78, "Simulated Gaussian", 19, INK, 800))
    body.append(T(x+22, cy+102, "two regimes, three correlations", 13.5, ACCENT, 600))
    rows = [("LOW-DIM", "n = 10,000   p = 100"),
            ("HIGH-DIM", "n = 400   p = 40,000"),
            ("CORRELATION", "rho in { 0, 0.4, 0.8 }"),
            ("REPEATS", "averaged over 20 runs")]
    ry = cy+138
    for lab,val in rows:
        body.append(T(x+22, ry, lab, 11, MUT, 700, SANS, spacing=1))
        body.append(T(x+22, ry+19, val, 15, INK, 600))
        ry += 42
    b.append(cue(a1, k1, "Simulated Gaussian designs low-dimensional ten thousand hundred predictors high-dimensional four hundred forty thousand correlation levels twenty repetitions.", "\n".join(body)))
    # chunk 3: twelve real sets
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=WARM))
    body.append(T(x+22, cy+78, "12 real data sets", 19, INK, 800))
    body.append(T(x+22, cy+102, "two problem types", 13.5, WARM, 600))
    body.append(T(x+22, cy+140, "l1 least-squares", 15, INK, 600))
    body.append(T(x+22, cy+162, "bcTCGA · e2006 · scheetz · YearPredMSD", 12.5, SUB))
    body.append(T(x+22, cy+198, "l1 logistic regression", 15, INK, 600))
    body.append(T(x+22, cy+220, "colon-cancer · madelon · news20 · rcv1", 12.5, SUB))
    body.append(rrect(x+22, cy+240, cw-44, 42, "#332A18", WARM, rx=10, sw=1.1))
    body.append(T(x+36, cy+267, "up to millions of features", 14, WARM, 700))
    b.append(cue(a2, k2, "Test twelve real data sets l1-regularized least-squares logistic regression gene-expression millions features news20 rcv1.", "\n".join(body)))
    # chunk 4: baselines
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+78, "Baselines", 19, INK, 800))
    body.append(T(x+22, cy+102, "strong state-of-the-art solvers", 13.5, RED, 600))
    bl = [("Working-set", "the strong-rule working set strategy"),
          ("Celer", "dual-extrapolation safe screening"),
          ("Blitz", "working-set with safe bounds")]
    ry = cy+140
    for name,d in bl:
        body.append(rrect(x+22, ry, cw-44, 44, CARD2, STROKE, rx=10))
        body.append(T(x+36, ry+20, name, 15, INK, 700))
        body.append(T(x+36, ry+38, d, 11.5, SUB))
        ry += 54
    b.append(cue(a3, k3, "Baselines working-set strategy Celer Blitz.", "\n".join(body)))
    write("06_dataset-benchmark.svg", "\n".join(b))

# ===========================================================================
# Slide 7 - Key Result
# ===========================================================================
def s07():
    sid = "key-result"
    head, y0 = frame("Key Result", "Fastest everywhere, by a wide margin", idx="07 / 09")
    b = [head]
    # chunk 1: decisive band
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 76, CARD2, GREEN, rx=12, sw=1.3)]
    body.append(tick(76, y0+18, h=40, fill=GREEN))
    body.append(T(96, y0+36, "Across every simulated configuration, the Hessian rule takes the least time", 18, INK, 700))
    body.append(T(96, y0+62, "the advantage is largest exactly where rivals struggle: high-correlation, low-dimensional", 14, GREEN, 600))
    b.append(cue(a0, k0, "Results decisive across every simulated configuration Hessian rule least time advantage largest high-correlation low-dimensional.", "\n".join(body)))
    cy = y0 + 96
    # chunk 4 chart: runtime bars (left, wide) -- placed here so it spans
    cw1 = 700; ch = 300; x = 56
    a3, k3 = anchor(sid, 3)
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(T(x+24, cy+40, "Full-path fit time  ·  Hessian vs. working-set runner-up", 17, INK, 700))
    body.append(T(x+cw1-24, cy+40, "lower is better", 12.5, MUT, 600, anchor="end"))
    # two dataset pairs, per-row normalized bars
    tx = x+220; tw = cw1-220-70
    def pair(yb, name, hess, base, unit="s"):
        seg = []
        seg.append(T(x+24, yb-6, name, 14.5, INK, 700))
        mx = float(base)
        # base bar (red)
        seg.append(rrect(tx, yb-18, tw, 22, BG2, "", rx=6))
        seg.append(rrect(tx, yb-18, tw*(base/mx), 22, RED, "", rx=6))
        seg.append(T(tx+tw*(base/mx)-8, yb-2, f"{base:g}{unit}", 13.5, "#0B1220", 800, anchor="end"))
        seg.append(T(x+24, yb+16, "working-set", 11.5, RED, 600))
        # hess bar (green)
        yb2 = yb+40
        seg.append(rrect(tx, yb2-18, tw, 22, BG2, "", rx=6))
        hb = max(tw*(hess/mx), 12)
        seg.append(rrect(tx, yb2-18, hb, 22, GREEN, "", rx=6))
        seg.append(T(tx+hb+8, yb2-2, f"{hess:g}{unit}", 13.5, GREEN, 800, anchor="start"))
        seg.append(T(x+24, yb2+16, "Hessian rule", 11.5, GREEN, 700))
        return "\n".join(seg)
    body.append(pair(cy+96, "YearPredictionMSD", 78.8, 541))
    body.append(pair(cy+206, "e2006-tfidf", 14.3, 143))
    body.append(T(x+24, cy+ch-16, "roughly 7x to 10x faster than the next-best method", 13.5, SUB))
    b.append(cue(a3, k3, "YearPredictionMSD fits full path seventy-nine seconds five hundred forty-one runner-up e2006-tfidf fourteen one hundred forty-three seven ten times.", "\n".join(body)))
    # right column: chunk 2 and chunk 3
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    a1, k1 = anchor(sid, 1)
    body = [rrect(rx0, cy, rw, 138, CARD2, ACCENT, rx=14, sw=1.4)]
    body.append(T(rx0+24, cy+40, "REAL DATA", 12, ACCENT, 700, SANS, spacing=1.5))
    body.append(T(rx0+24, cy+96, "11 / 12", 46, "url(#warmg)", 800))
    body.append(T(rx0+24, cy+122, "wins on nearly all twelve sets", 13.5, SUB))
    b.append(cue(a1, k1, "On real data wins nearly all twelve sets.", "\n".join(body)))
    a2, k2 = anchor(sid, 2)
    yy = cy + 158
    body = [rrect(rx0, yy, rw, 142, CARD, STROKE)]
    body.append(tick(rx0+22, yy+22, h=30, fill=GREEN))
    body.append(T(rx0+42, yy+42, "Least-squares: 5 / 5", 16, INK, 700))
    body.append(paragraph(rx0+22, yy+72, "Fastest on all five least-squares sets, and in all but one it finishes in under half the runner-up's time.", 14, SUB, maxchars=40))
    b.append(cue(a2, k2, "For l1-regularized least-squares fastest all five all but one under half time working-set strategy.", "\n".join(body)))
    write("07_key-result.svg", "\n".join(b))

# ===========================================================================
# Slide 8 - Ablation Study
# ===========================================================================
def s08():
    sid = "ablation-study"
    head, y0 = frame("Ablation", "Where the two gains come from", idx="08 / 09")
    b = [head]
    # chunk 1: intro band
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD, STROKE)]
    body.append(tick(76, y0+16, h=26, fill=ACCENT))
    body.append(T(96, y0+37, "Two component studies isolate the warm start and the screening", 18, INK, 700))
    b.append(cue(a0, k0, "Two component studies show where gains come from.", "\n".join(body)))
    cy = y0 + 80
    cw = (W - 112 - 24) / 2; ch = 320
    xs = [56, 56+cw+24]
    # chunk 2: warm start passes bar chart
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=28, fill=GREEN))
    body.append(T(x+40, cy+44, "Warm start in isolation", 18, INK, 700))
    body.append(T(x+22, cy+74, "coordinate-descent passes per path step  ·  colon-cancer, YearPredictionMSD", 12.5, SUB))
    # two vertical bars: standard warm start (many) vs Hessian (~1)
    gx, gy, gh = x+70, cy+104, 118
    body.append(f'<line x1="{gx-14}" y1="{gy}" x2="{gx-14}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(f'<line x1="{gx-14}" y1="{gy+gh}" x2="{x+cw-30}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    bw = 96
    # standard: tall red
    body.append(rrect(gx+20, gy+10, bw, gh-10, RED, "", rx=6))
    body.append(T(gx+20+bw/2, gy+2, "many", 14, RED, 800, anchor="middle"))
    body.append(T(gx+20+bw/2, gy+gh+22, "standard", 13, SUB, 600, anchor="middle"))
    body.append(T(gx+20+bw/2, gy+gh+40, "warm start", 13, SUB, 600, anchor="middle"))
    # hessian: tiny green
    hx = gx+20+bw+90
    body.append(rrect(hx, gy+gh-18, bw, 18, GREEN, "", rx=5))
    body.append(T(hx+bw/2, gy+gh-26, "≈ 1 pass", 14, GREEN, 800, anchor="middle"))
    body.append(T(hx+bw/2, gy+gh+22, "Hessian", 13, GREEN, 700, anchor="middle"))
    body.append(T(hx+bw/2, gy+gh+40, "warm start", 13, GREEN, 700, anchor="middle"))
    body.append(T(x+22, cy+ch-16, "Near-exact when the active set is stable, so each step often needs a single pass.", 13, SUB))
    b.append(cue(a1, k1, "Warm start isolation colon-cancer YearPredictionMSD Hessian warm start collapses coordinate-descent passes single pass active set exact.", "\n".join(body)))
    # chunk 3: screening line chart - retained predictors vs correlation
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=28, fill=TEAL))
    body.append(T(x+40, cy+44, "Screening in isolation", 18, INK, 700))
    body.append(T(x+22, cy+74, "predictors retained vs. correlation  (log scale)", 12.5, SUB))
    gx, gy, gw, gh = x+64, cy+100, cw-64-40, 150
    body.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(T(gx-8, gy+6, "many", 11, MUT, 600, anchor="end"))
    body.append(T(gx-8, gy+gh, "floor", 11, MUT, 600, anchor="end"))
    for i,lab in enumerate(["0","0.4","0.8"]):
        px = gx + gw*i/2.0
        body.append(T(px, gy+gh+18, lab, 11.5, MUT, 600, anchor="middle"))
    body.append(T(gx+gw/2, gy+gh+38, "correlation rho", 12, SUB, 600, anchor="middle"))
    # rivals rising line (red)
    rivals = [(0,0.42),(1,0.66),(2,0.90)]
    pr = " ".join(f"{gx+gw*i/2.0:.1f},{gy+(1-v)*gh:.1f}" for i,v in rivals)
    body.append(f'<polyline points="{pr}" fill="none" stroke="{RED}" stroke-width="2.6"/>')
    for i,v in rivals: body.append(f'<circle cx="{gx+gw*i/2.0:.1f}" cy="{gy+(1-v)*gh:.1f}" r="3.5" fill="{RED}"/>')
    body.append(T(gx+gw-4, gy+(1-0.90)*gh-8, "Celer, Blitz, Strong,", 11.5, RED, 700, anchor="end"))
    body.append(T(gx+gw-4, gy+(1-0.90)*gh+8, "EDPP, Gap Safe, Sasvi", 11.5, RED, 700, anchor="end"))
    # hessian flat near floor (green)
    hess = [(0,0.10),(1,0.12),(2,0.15)]
    ph = " ".join(f"{gx+gw*i/2.0:.1f},{gy+(1-v)*gh:.1f}" for i,v in hess)
    body.append(f'<polyline points="{ph}" fill="none" stroke="{GREEN}" stroke-width="2.6"/>')
    for i,v in hess: body.append(f'<circle cx="{gx+gw*i/2.0:.1f}" cy="{gy+(1-v)*gh:.1f}" r="3.5" fill="{GREEN}"/>')
    body.append(T(gx+8, gy+(1-0.10)*gh+16, "Hessian rule (near the active-set floor)", 11.5, GREEN, 700))
    b.append(cue(a2, k2, "Screening isolation Hessian rule keeps retained predictors close true active-set floor Celer Blitz strong EDPP Gap Safe Sasvi orders magnitude more gap widens correlation.", "\n".join(body)))
    write("08_ablation-study.svg", "\n".join(b))

# ===========================================================================
# Slide 9 - Takeaway
# ===========================================================================
def s09():
    sid = "takeaway"
    head, y0 = frame("Takeaway", "One idea that pays off twice", idx="09 / 09")
    b = [head]
    # chunk 1: headline band
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 74, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(76, y0+22, h=32, fill=TEAL))
    body.append(T(96, y0+40, "A single idea, reusing second-order Hessian information,", 21, INK, 800))
    body.append(T(96, y0+64, "pays off twice over", 16, TEAL, 700))
    b.append(cue(a0, k0, "Takeaway single idea reusing second-order Hessian information pays off twice over.", "\n".join(body)))
    # chunk 2: two-payoff cards
    a1, k1 = anchor(sid, 1)
    cy = y0 + 96
    cw = (W-112-24)/2; ch = 140
    xs = [56, 56+cw+24]
    body = []
    pay = [("Tighter screening", GREEN, "the solver sees far fewer predictors on every subproblem"),
           ("Accurate warm starts", TEAL, "so accurate that many path steps converge in a single pass")]
    for (t,col,d),x in zip(pay, xs):
        body.append(rrect(x, cy, cw, ch, CARD, STROKE))
        body.append(tick(x+22, cy+26, h=30, fill=col))
        body.append(T(x+42, cy+48, t, 19, INK, 700))
        body.append(paragraph(x+42, cy+80, d, 15, SUB, maxchars=46))
    b.append(cue(a1, k1, "Tightens screening solver sees far fewer predictors supplies warm starts accurate many path steps converge one pass.", "\n".join(body)))
    # chunk 3: closing band
    a2, k2 = anchor(sid, 2)
    yy = cy + ch + 22
    body = [rrect(56, yy, W-112, 118, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(tick(76, yy+22, h=32, fill=ACCENT))
    body.append(T(96, yy+44, "The fastest way to fit lasso and l1-logistic regularization paths", 19, INK, 800))
    body.append(paragraph(96, yy+72, "with the biggest edge in the high-correlation regime that has historically been hardest for screening rules.", 15, SUB, maxchars=90, lh=22))
    b.append(cue(a2, k2, "Together make Hessian Screening Rule fastest fitting lasso l1-regularized logistic regression paths benchmarks biggest edge high-correlation historically hardest.", "\n".join(body)))
    # footer links
    b.append(f'<line x1="56" y1="{yy+140}" x2="{W-56}" y2="{yy+140}" stroke="{STROKE}" stroke-width="1.2"/>')
    b.append(T(56, yy+168, "Open C++ / R implementation", 15, SUB, 500))
    b.append(T(W-56, yy+168, "arXiv:2104.13026   ·   github.com/jolars/HessianScreening", 13.5, ACCENT, 600, MONO, anchor="end"))
    write("09_takeaway.svg", "\n".join(b))

for fn in [s01, s02, s03, s04, s05, s06, s07, s08, s09]:
    fn()
print("done")
