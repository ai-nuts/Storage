#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video (USBS, ICML 2024).

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
RED     = "#F2708A"   # danger / CGAL fails

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
    # subtle inset gradient panel band (not touching edges)
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bgv)" />')
    # header
    b.append(tick(56, 50, h=22, w=6, fill=ACCENT))
    b.append(T(74, 68, eyebrow.upper(), 15, ACCENT, 700, SANS, spacing=3))
    b.append(T(56, 116, title, 40, INK, 800))
    if sub:
        b.append(T(58, 146, sub, 17, SUB, 400))
    if idx:
        b.append(T(W - 56, 68, idx, 14, MUT, 700, MONO, anchor="end", spacing=1))
    # thin divider under header
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
    # kicker (chunk 1: SDP powerful tool)
    a0, k0 = anchor(sid, 0)
    body = []
    body.append(tick(72, 96, h=30, w=6, fill=ACCENT))
    body.append(T(92, 108, "SEMIDEFINITE PROGRAMMING · COMBINATORIAL OPTIMIZATION", 15, ACCENT, 700, SANS, spacing=2.5))
    body.append(T(92, 138, "Powerful in theory, long dismissed as too expensive at real-world scale.", 16, SUB, 400))
    b.append(cue(a0, k0, "SDP is a powerful tool for combinatorial optimization but considered too expensive.", "\n".join(body)))
    # title block
    b.append(T(72, 214, "Fast, Scalable, Warm-Start", 58, INK, 800))
    b.append(T(72, 278, "Semidefinite Programming", 58, INK, 800))
    b.append(T(72, 320, "with Spectral Bundling and Sketching", 24, SUB, 500))
    # chunk 2: USBS name card
    a1, k1 = anchor(sid, 1)
    body = []
    body.append(rrect(72, 356, 620, 128, CARD, STROKE, rx=16))
    body.append(tick(92, 380, h=80, w=6, fill=TEAL))
    body.append(T(112, 392, "USBS", 30, TEAL, 800))
    body.append(T(210, 392, "Unified Spectral Bundling with Sketching", 17, INK, 600))
    body.append(T(112, 424, "A provably correct solver that is fast, scales to billions of", 15, SUB))
    body.append(T(112, 446, "decision variables, and reuses a previous solution as a warm start.", 15, SUB))
    b.append(cue(a1, k1, "USBS: unified spectral bundling with sketching, provably correct, warm-start.", "\n".join(body)))
    # chunk 3: hero stat card (500x / 2B vars)
    a2, k2 = anchor(sid, 2)
    body = []
    body.append(rrect(736, 356, 472, 128, CARD2, ACCENT, rx=16, sw=1.4))
    body.append(T(772, 410, "500", 62, "url(#warmg)", 800))
    body.append(T(902, 410, "×", 40, WARM, 700))
    body.append(T(940, 388, "faster than the prior", 15, SUB))
    body.append(T(940, 410, "state of the art (CGAL)", 15, SUB))
    body.append(T(772, 452, "on a MaxCut instance with over 2 billion decision variables", 14.5, INK, 500))
    b.append(cue(a2, k2, "MaxCut instance over two billion variables 500x speedup warm start.", "\n".join(body)))
    # authors / venue footer band
    b.append(f'<line x1="72" y1="536" x2="{W-72}" y2="536" stroke="{STROKE}" stroke-width="1.2" />')
    b.append(T(72, 574, "Rico Angell   ·   Andrew McCallum", 21, INK, 700))
    b.append(T(72, 600, "Manning College of Information & Computer Sciences, UMass Amherst", 15, SUB))
    b.append(T(72, 636, "ICML 2024", 14, ACCENT, 700, SANS, spacing=1.5))
    b.append(T(72, 660, "arXiv:2312.11801    ·    github.com/rangell/usbs", 14, MUT, 500, MONO))
    write("01_title.svg", "\n".join(b))

# ===========================================================================
# Slide 2 - Problem
# ===========================================================================
def s02():
    sid = "problem"
    head, y0 = frame("Problem", "Why SDPs are dismissed at scale", idx="02 / 10")
    b = [head]
    # chunk 1: SDPs model enormous range (full-width intro card)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 92, CARD, STROKE)]
    body.append(tick(76, y0+22, h=48))
    body.append(T(96, y0+38, "SDPs model an enormous range of practical problems", 20, INK, 700))
    body.append(T(96, y0+66, "combinatorial optimization  ·  neural-network verification  ·  control  —  yet solving them at scale is hard", 15, SUB))
    b.append(cue(a0, k0, "Semidefinite programs model an enormous range of practical problems.", "\n".join(body)))
    # three problem cards
    cy = y0 + 112
    cw = (W - 112 - 2*24) / 3
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    ch = 300
    # chunk 2: classic approaches (cubic eigendecomposition)
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=RED))
    body.append(T(x+22, cy+80, "Classic SDP solvers", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Project onto the semidefinite cone at every iteration, requiring a full eigendecomposition.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+188, cw-44, 84, "#301B27", RED, rx=12, sw=1.2))
    body.append(T(x+38, cy+228, "O(n³)", 30, RED, 800, MONO))
    body.append(T(x+38, cy+254, "cubic per-iteration cost", 13.5, SUB))
    b.append(cue(a1, k1, "Classic approaches require projecting onto the semidefinite cone full eigendecomposition cubic.", "\n".join(body)))
    # chunk 3: sketching methods (CGAL) scale but slow
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=WARM))
    body.append(T(x+22, cy+80, "Sketching (CGAL)", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "Avoids storing the full matrix and scales much further — but pays a price as size grows.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+188, cw-44, 84, "#332A18", WARM, rx=12, sw=1.2))
    body.append(T(x+38, cy+222, "more iterations", 17, WARM, 800))
    body.append(T(x+38, cy+248, "convergence slows at scale", 13.5, SUB))
    b.append(cue(a2, k2, "Recent sketching methods like CGAL avoid storing full matrix scale further need more iterations.", "\n".join(body)))
    # chunk 4: iteration-dependent schedules block warm start
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+26, h=30, fill=ACCENT))
    body.append(T(x+22, cy+80, "No warm-starting", 18, INK, 700))
    body.append(paragraph(x+22, cy+112, "They rely on iteration-dependent parameter schedules that block reusing a previous solution.", 15, SUB, maxchars=34))
    body.append(rrect(x+22, cy+188, cw-44, 84, "#16283F", ACCENT, rx=12, sw=1.2))
    body.append(T(x+38, cy+222, "schedules ≠ reuse", 16, ACCENT, 800))
    body.append(T(x+38, cy+248, "warm start unreliable", 13.5, SUB))
    b.append(cue(a3, k3, "Worse they rely on iteration-dependent parameter schedules prevent reusing previous solution warm start.", "\n".join(body)))
    write("02_problem.svg", "\n".join(b))

# ===========================================================================
# Slide 3 - Motivation
# ===========================================================================
def s03():
    sid = "motivation"
    head, y0 = frame("Motivation", "You never solve just one SDP", idx="03 / 10")
    b = [head]
    lw = 616; rx0 = 56 + lw + 24; rw = W - 56 - rx0
    # left: sequence of related SDPs (chunks 1 & 2)
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, lw, 168, CARD, STROKE)]
    body.append(tick(76, y0+22, h=30))
    body.append(T(96, y0+40, "A sequence of closely-related problems", 18, INK, 700))
    body.append(paragraph(96, y0+70, "Data arrives incrementally, or you solve related subproblems inside a mixed-integer or interactive loop.", 14.5, SUB, maxchars=64))
    # mini chain SDP1 -> SDP2 -> SDP3
    bx, by, bw, bh, gap = 96, y0+118, 118, 40, 60
    for i in range(3):
        x = bx + i*(bw+gap)
        body.append(rrect(x, by, bw, bh, CARD2, ACCENT, rx=9, sw=1.1))
        body.append(T(x+bw/2, by+26, f"SDP {i+1}", 15, INK, 700, anchor="middle"))
        if i < 2:
            ax = x+bw+8
            body.append(f'<line x1="{ax}" y1="{by+bh/2}" x2="{ax+gap-16}" y2="{by+bh/2}" stroke="{TEAL}" stroke-width="2"/>')
            body.append(f'<polygon points="{ax+gap-16},{by+bh/2-4} {ax+gap-10},{by+bh/2} {ax+gap-16},{by+bh/2+4}" fill="{TEAL}"/>')
            body.append(T(ax+ (gap-16)/2, by-6, "warm", 11.5, TEAL, 700, anchor="middle"))
    b.append(cue(a0, k0, "In practice you rarely solve a single SDP data arrives incrementally mixed-integer loop.", "\n".join(body)))
    a1, k1 = anchor(sid, 1)
    yy = y0+188
    body = [rrect(56, yy, lw, 120, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(76, yy+24, h=72, fill=TEAL))
    body.append(T(96, yy+44, "Each new problem is nearly identical to the last", 18, INK, 700))
    body.append(paragraph(96, yy+72, "So warm-starting from the previous solution should give a huge speedup — exactly what real applications need.", 14.5, SUB, maxchars=64))
    b.append(cue(a1, k1, "All these settings each new problem nearly identical warm-start previous solution huge speedup.", "\n".join(body)))
    # right: spectral bundle promise & gap (chunks 3 & 4)
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, y0, rw, 168, CARD, STROKE)]
    body.append(tick(rx0+20, y0+22, h=30, fill=GREEN))
    body.append(T(rx0+40, y0+40, "Spectral bundle methods", 17, GREEN, 700))
    body.append(paragraph(rx0+20, y0+72, "An appealing framework: low per-iteration cost and fast empirical convergence.", 14.5, SUB, maxchars=48))
    body.append(rrect(rx0+20, y0+118, rw-40, 34, BG2, "", rx=9))
    body.append(T(rx0+34, y0+140, "✓ cheap steps    ✓ fast in practice", 14, GREEN, 600))
    b.append(cue(a2, k2, "Spectral bundle methods appealing framework low per-iteration cost fast empirical convergence.", "\n".join(body)))
    a3, k3 = anchor(sid, 3)
    yy = y0+188
    body = [rrect(rx0, yy, rw, 120, CARD, RED, rx=14, sw=1.2)]
    body.append(tick(rx0+20, yy+24, h=30, fill=RED))
    body.append(T(rx0+40, yy+42, "But prior versions fell short", 17, RED, 700))
    body.append(paragraph(rx0+20, yy+72, "Handled only equality OR only inequality constraints, with no efficient standalone implementation for massive SDPs.", 14.5, SUB, maxchars=48))
    b.append(cue(a3, k3, "But previous spectral bundle methods handled only equality or inequality no standalone implementation massive.", "\n".join(body)))
    write("03_motivation.svg", "\n".join(b))

# ===========================================================================
# Slide 4 - Contribution
# ===========================================================================
def s04():
    sid = "contribution"
    head, y0 = frame("Contribution", "What USBS delivers", idx="04 / 10")
    b = [head]
    cw = (W - 112 - 24) / 2; ch = 170
    xs = [56, 56+cw+24]; ys = [y0, y0+ch+22]
    specs = [
        (0, xs[0], ys[0], "01", ACCENT, "Unified general SDPs",
         "One spectral bundle method that handles both equality and inequality constraints — unlike prior methods."),
        (1, xs[1], ys[0], "02", TEAL, "Optional matrix sketching",
         "Dramatically improves scalability to massive instances while keeping convergence fast."),
        (2, xs[0], ys[1], "03", GREEN, "Provable + tunable",
         "Non-asymptotic convergence guarantees, plus parameters trading per-iteration cost against convergence speed."),
        (3, xs[1], ys[1], "04", WARM, "Standalone pure-JAX",
         "An open implementation that runs efficiently on CPUs, GPUs, and TPUs."),
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
    head, y0 = frame("Method", "A proximal spectral bundle method", idx="05 / 10")
    b = [head]
    # chunk 1: penalized dual objective (equation band)
    a0, k0 = anchor(sid, 0)
    eqh = 116
    body = [rrect(56, y0, W-112, eqh, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(76, y0+30, "Rewrite the dual SDP as one unconstrained penalized objective", 15, ACCENT, 700))
    body.append(T(76, y0+78, "f(y) = α·[ λₘₐₓ(C − 𝒜*y) ]₊ + ⟨ b, y ⟩ + ι_Y(y)", 27, INK, 700, MONO))
    b.append(cue(a0, k0, "How USBS works starts from dual semidefinite program rewrites penalized objective largest eigenvalue.", "\n".join(body)))
    # bottom: three step cards
    cy = y0 + eqh + 22
    cw = (W - 112 - 2*22) / 3; ch = 214
    xs = [56, 56+cw+22, 56+2*(cw+22)]
    # chunk 2: proximal bundle + low-dim model
    a1, k1 = anchor(sid, 1)
    x = xs[0]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "1  Build a cheap model", 17, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "Minimize with a proximal bundle method: build a lower model over a low-dimensional subspace of current and past eigenvectors.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+162, cw-44, 34, BG2, "", rx=9))
    body.append(T(x+36, cy+184, "Vₜ = k_c current ⊕ k_p past", 13.5, TEAL, 600, MONO))
    b.append(cue(a1, k1, "Penalized objective minimized proximal bundle method low-dimensional subspace eigenvectors.", "\n".join(body)))
    # chunk 3: proximal step + descent/null
    a2, k2 = anchor(sid, 2)
    x = xs[1]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "2  Propose a step", 17, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "Take a proximal step against the model, solving a small minimax problem for the candidate iterate.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+152, cw-44, 44, BG2, "", rx=9))
    body.append(T(x+36, cy+180, "ỹₜ₊₁ = argmin f̂ₜ(y) + ½ρ‖y−yₜ‖²", 13, INK, 600, MONO))
    b.append(cue(a2, k2, "Proposes candidate iterate taking proximal step model small minimax problem.", "\n".join(body)))
    # chunk 4: descent/null test + storage -> scale
    a3, k3 = anchor(sid, 3)
    x = xs[2]; body = [rrect(x, cy, cw, ch, CARD, STROKE)]
    body.append(T(x+22, cy+40, "3  Accept or refine", 17, ACCENT, 700))
    body.append(paragraph(x+22, cy+70, "Descent step if the true decrease clears a fraction of the model's; else a null step that still refines it.", 14, SUB, maxchars=36))
    body.append(rrect(x+22, cy+152, cw-44, 44, "#14261F", GREEN, rx=9, sw=1.1))
    body.append(T(x+36, cy+180, "few eigenvectors + sketch → scale", 12.5, GREEN, 600, MONO))
    b.append(cue(a3, k3, "Because only small set eigenvectors optionally low-rank sketch primal matrix scales enormous.", "\n".join(body)))
    write("05_method.svg", "\n".join(b))

# ===========================================================================
# Slide 6 - Dataset / Benchmark
# ===========================================================================
def s06():
    sid = "dataset-benchmark"
    head, y0 = frame("Benchmarks", "Three very different problem families", idx="06 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 66, CARD, STROKE)]
    body.append(tick(76, y0+18, h=30, fill=TEAL))
    body.append(T(96, y0+42, "USBS is evaluated across three very different application areas", 19, INK, 700))
    b.append(cue(a0, k0, "The method is tested across three very different application areas.", "\n".join(body)))
    cy = y0 + 86
    cw = (W - 112 - 2*24) / 3; ch = 300
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    cards = [
        (1, xs[0], "MaxCut", ACCENT, "10 DIMACS10 graphs", [
            ("n", "16K → 3.7M vertices"),
            ("scale", "> 10¹³ decision variables"),
            ("data", "25.9M Laplacian nonzeros"),
        ]),
        (2, xs[1], "Quadratic Assignment", WARM, "QAPLIB + TSPLIB", [
            ("n", "up to 198"),
            ("relaxation", "O(n⁴) variables"),
            ("scale", "1.5 billion at n = 198"),
        ]),
        (3, xs[2], "Entity Resolution", TEAL, "∃-constraints, interactive", [
            ("datasets", "PubMed · QIAN"),
            ("", "SCAD-zbMATH"),
            ("task", "author coreference"),
        ]),
    ]
    for ci, x, name, col, sub, rows in cards:
        a, k = anchor(sid, ci)
        body = [rrect(x, cy, cw, ch, CARD, STROKE)]
        body.append(tick(x+22, cy+26, h=30, fill=col))
        body.append(T(x+22, cy+78, name, 20, INK, 800))
        body.append(T(x+22, cy+102, sub, 14, col, 600))
        ry = cy+140
        for lab, val in rows:
            if lab:
                body.append(T(x+22, ry, lab.upper(), 11.5, MUT, 700, SANS, spacing=1))
            body.append(T(x+22, ry+20, val, 15.5, INK, 600))
            ry += 50
        b.append(cue(a, k, f"{name} benchmark {sub}", "\n".join(body)))
    b.append(T(56, cy+ch+30, "Warm starts are built naturally from a slightly smaller, closely-related instance.", 14, SUB, 400, SANS))
    write("06_dataset-benchmark.svg", "\n".join(b))

# ===========================================================================
# Slide 7 - Key Result
# ===========================================================================
def s07():
    sid = "key-result"
    head, y0 = frame("Key Result", "USBS vs. CGAL, the prior state of the art", idx="07 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD2, WARM, rx=12, sw=1.2)]
    body.append(T(76, y0+37, "The results are striking — across every setting, the gap grows with problem size.", 18, INK, 700))
    b.append(cue(a0, k0, "The results are striking.", "\n".join(body)))
    cy = y0 + 80
    # chunk 2: MaxCut solved chart (10/10 vs 3/10)
    a1, k1 = anchor(sid, 1)
    cw1 = 596; ch = 296
    x = 56
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(T(x+24, cy+40, "MaxCut instances solved to target accuracy", 17, INK, 700))
    # two horizontal bar tracks out of 10
    track_x, track_w = x+150, cw1-150-40
    def bar(yb, label, n, col, note):
        seg = []
        seg.append(T(x+24, yb+6, label, 15, INK, 700))
        seg.append(rrect(track_x, yb-14, track_w, 26, BG2, "", rx=6))
        seg.append(rrect(track_x, yb-14, track_w*(n/10.0), 26, col, "", rx=6))
        seg.append(T(track_x+track_w+6, yb+6, f"{n}/10", 16, col, 800, anchor="start"))
        seg.append(T(x+24, yb+28, note, 12.5, MUT, 500))
        return "\n".join(seg)
    body.append(bar(cy+96, "USBS", 10, GREEN, "all 10 in ≤ 28 hours, even cold-start"))
    body.append(bar(cy+176, "CGAL", 3, RED, "fails on 7 of 10 within 72 hours"))
    # gridline ticks
    for i in range(1,10):
        gx = track_x + track_w*i/10.0
        body.append(f'<line x1="{gx}" y1="{cy+70}" x2="{gx}" y2="{cy+206}" stroke="{STROKE}" stroke-width="0.6" opacity="0.5"/>')
    body.append(T(x+24, cy+266, "USBS reaches an accurate solution on all instances; CGAL cannot.", 13.5, SUB))
    b.append(cue(a1, k1, "On MaxCut USBS reaches accurate solution all ten instances twenty-eight hours CGAL fails seven.", "\n".join(body)))
    # right column: chunk 3 (500x) and chunk 4 (QAP + ER)
    rx0 = x + cw1 + 24; rw = W - 56 - rx0
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD2, ACCENT, rx=14, sw=1.4)]
    body.append(T(rx0+24, cy+40, "2-BILLION-VARIABLE INSTANCE", 12, ACCENT, 700, SANS, spacing=1.5))
    body.append(T(rx0+24, cy+104, "500×", 56, "url(#warmg)", 800))
    body.append(T(rx0+168, cy+92, "faster than", 15, SUB))
    body.append(T(rx0+168, cy+114, "CGAL", 15, INK, 700))
    b.append(cue(a2, k2, "On an instance over two billion decision variables USBS five hundred times faster than CGAL.", "\n".join(body)))
    a3, k3 = anchor(sid, 3)
    yy = cy + 158
    body = [rrect(rx0, yy, rw, 138, CARD, STROKE)]
    body.append(tick(rx0+22, yy+22, h=30, fill=TEAL))
    body.append(T(rx0+42, yy+42, "QAP + entity resolution", 16, INK, 700))
    body.append(paragraph(rx0+22, yy+72, "Lower relative gaps and cumulative solve times — and USBS reliably exploits warm starts where CGAL cannot.", 14, SUB, maxchars=42))
    b.append(cue(a3, k3, "On quadratic assignment entity-resolution tasks USBS reaches better relative gaps lower solve times.", "\n".join(body)))
    write("07_key-result.svg", "\n".join(b))

# ===========================================================================
# Slide 8 - Ablation Study
# ===========================================================================
def s08():
    sid = "ablation-study"
    head, y0 = frame("Ablation", "What actually drives convergence", idx="08 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 58, CARD, STROKE)]
    body.append(tick(76, y0+16, h=26, fill=ACCENT))
    body.append(T(96, y0+37, "Two ablations are especially informative", 18, INK, 700))
    b.append(cue(a0, k0, "Two ablations are especially informative.", "\n".join(body)))
    cy = y0 + 80
    # chunk 2: warm-start convergence curve + >100x
    a1, k1 = anchor(sid, 1)
    cw1 = 596; ch = 300; x = 56
    body = [rrect(x, cy, cw1, ch, CARD, STROKE)]
    body.append(tick(x+22, cy+24, h=28, fill=GREEN))
    body.append(T(x+40, cy+44, "Warm-starting", 18, INK, 700))
    body.append(T(x+cw1-24, cy+52, "> 100×", 34, GREEN, 800, anchor="end"))
    body.append(T(x+cw1-24, cy+74, "faster convergence", 12.5, SUB, anchor="end"))
    # mini convergence chart: cold (slow) vs warm (fast) - relative gap vs time
    gx, gy, gw, gh = x+40, cy+96, cw1-80, 150
    body.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{MUT}" stroke-width="1.2"/>')
    body.append(T(gx-6, gy+6, "gap", 11.5, MUT, 600, anchor="end"))
    body.append(T(gx+gw, gy+gh+18, "time", 11.5, MUT, 600, anchor="end"))
    # cold curve: slow exponential decay
    import math
    def curve(k, col, dash=""):
        pts = []
        for i in range(41):
            t = i/40.0
            v = math.exp(-k*t)          # 1 -> 0
            px = gx + t*gw
            py = gy + (1-v)*gh          # top=high gap at t=0, decays downward
            pts.append(f"{px:.1f},{py:.1f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.6"{d}/>'
    body.append(curve(1.4, RED, dash="6 5"))
    body.append(curve(6.0, GREEN))
    body.append(T(gx+gw-6, gy+gh-8, "warm start", 12.5, GREEN, 700, anchor="end"))
    body.append(T(gx+gw-6, gy+42, "cold start", 12.5, RED, 700, anchor="end"))
    body.append(T(x+24, cy+ch-16, "USBS realizes the warm-start benefit; CGAL usually cannot.", 13.5, SUB))
    b.append(cue(a1, k1, "First warm-starting USBS initializing previous solution speed up convergence one hundred times CGAL cannot.", "\n".join(body)))
    # right: kc (chunk 3) and kp (chunk 4)
    rx0 = x+cw1+24; rw = W-56-rx0
    a2, k2 = anchor(sid, 2)
    body = [rrect(rx0, cy, rw, 138, CARD2, ACCENT, rx=14, sw=1.3)]
    body.append(T(rx0+22, cy+38, "k_c  current eigenvectors", 16, ACCENT, 700, MONO))
    body.append(paragraph(rx0+22, cy+66, "Matters a lot — larger values give better convergence.", 14, SUB, maxchars=40))
    body.append(T(rx0+22, cy+120, "vs. original method fixed at k_c = 1", 12.5, MUT, 600, MONO))
    b.append(cue(a2, k2, "Second parameters number current eigenvectors kc matters larger better convergence fixed one.", "\n".join(body)))
    a3, k3 = anchor(sid, 3)
    yy = cy+158
    body = [rrect(rx0, yy, rw, 142, CARD, STROKE)]
    body.append(T(rx0+22, yy+38, "k_p  past spectral vectors", 16, WARM, 700, MONO))
    body.append(paragraph(rx0+22, yy+66, "Much less helpful — and can even hurt convergence.", 14, SUB, maxchars=40))
    body.append(rrect(rx0+22, yy+96, rw-44, 32, BG2, "", rx=8))
    body.append(T(rx0+34, yy+117, "recommended: large k_c, small k_p", 13, INK, 600, MONO))
    b.append(cue(a3, k3, "Number past spectral vectors kp less helpful can even harm keep kc large kp small.", "\n".join(body)))
    write("08_ablation-study.svg", "\n".join(b))

# ===========================================================================
# Slide 9 - Headline Numbers
# ===========================================================================
def s09():
    sid = "headline-numbers"
    head, y0 = frame("By the Numbers", "The results that matter most", idx="09 / 10")
    b = [head]
    # chunk 1: top row of three tiles
    a0, k0 = anchor(sid, 0)
    tw = (W-112-2*24)/3; th = 188
    xs = [56, 56+tw+24, 56+2*(tw+24)]
    tiles = [
        ("500×", WARM, "speedup over CGAL", "on a 2-billion-variable MaxCut instance"),
        ("> 100×", GREEN, "warm-start speedup", "vs. cold-starting USBS"),
        ("10 / 10", ACCENT, "MaxCut solved by USBS", "vs. only 3 / 10 by CGAL"),
    ]
    body = []
    for (big, col, lab, sub), x in zip(tiles, xs):
        body.append(rrect(x, y0, tw, th, CARD, STROKE))
        body.append(tick(x+24, y0+26, h=26, fill=col))
        body.append(T(x+tw/2, y0+108, big, 56, col, 800, anchor="middle"))
        body.append(T(x+tw/2, y0+142, lab, 16, INK, 700, anchor="middle"))
        body.append(T(x+tw/2, y0+166, sub, 12.5, SUB, 400, anchor="middle"))
    b.append(cue(a0, k0, "Five-hundred-times speedup over prior state art more than hundred-times warm-starting ten out of ten CGAL three.", "\n".join(body)))
    # chunk 2: bottom row - scale numbers
    a1, k1 = anchor(sid, 1)
    yy = y0 + th + 24
    hw = (W-112-24)/2; hh = 150
    xs2 = [56, 56+hw+24]
    body = []
    b2 = [
        ("> 10¹³", ACCENT, "decision variables", "largest MaxCut instance (333SP, n ≈ 3.7M)"),
        ("1.5 B", TEAL, "variables at n = 198", "QAP relaxation solved via r = n sketching"),
    ]
    for (big, col, lab, sub), x in zip(b2, xs2):
        body.append(rrect(x, yy, hw, hh, CARD2, col, rx=14, sw=1.3))
        body.append(T(x+30, yy+92, big, 50, col, 800))
        body.append(T(x+30, yy+124, lab, 16, INK, 700))
        body.append(T(x+hw-24, yy+124, sub, 12.5, SUB, 400, anchor="end"))
    b.append(cue(a1, k1, "USBS scales problems over ten-to-the-thirteenth decision variables quadratic-assignment 1.5 billion.", "\n".join(body)))
    write("09_headline-numbers.svg", "\n".join(b))

# ===========================================================================
# Slide 10 - Takeaway
# ===========================================================================
def s10():
    sid = "takeaway"
    head, y0 = frame("Takeaway", "Large-scale SDP, made practical", idx="10 / 10")
    b = [head]
    a0, k0 = anchor(sid, 0)
    body = [rrect(56, y0, W-112, 70, CARD2, TEAL, rx=14, sw=1.3)]
    body.append(tick(76, y0+20, h=30, fill=TEAL))
    body.append(T(96, y0+46, "The takeaway is simple.", 22, INK, 800))
    b.append(cue(a0, k0, "The takeaway is simple.", "\n".join(body)))
    a1, k1 = anchor(sid, 1)
    yy = y0 + 90
    body = [rrect(56, yy, W-112, 96, CARD, STROKE)]
    body.append(paragraph(80, yy+40, "USBS shows that large-scale semidefinite programming does not have to be slow, or restricted to a narrow class of problems.", size=19, fill=INK, maxchars=88, lh=28, weight=600))
    b.append(cue(a1, k1, "USBS shows large-scale semidefinite programming does not have to be slow restricted narrow class.", "\n".join(body)))
    # chunk 3: three pillars
    a2, k2 = anchor(sid, 2)
    cy = yy + 116
    cw = (W-112-2*24)/3; ch = 150
    xs = [56, 56+cw+24, 56+2*(cw+24)]
    pil = [
        ("Unified constraints", ACCENT, "equality + inequality in one spectral bundle method"),
        ("Optional sketching", TEAL, "scales to billions of decision variables"),
        ("Working warm-starts", GREEN, "reuse a solution where prior solvers cannot"),
    ]
    body = []
    for (t, col, d), x in zip(pil, xs):
        body.append(rrect(x, cy, cw, ch, CARD, STROKE))
        body.append(tick(x+22, cy+26, h=30, fill=col))
        body.append(T(x+22, cy+72, t, 17, INK, 700))
        body.append(paragraph(x+22, cy+100, d, 14, SUB, maxchars=36))
    b.append(cue(a2, k2, "By unifying equality inequality constraints single spectral bundle sketching warm-starting practical JAX.", "\n".join(body)))
    # footer links
    b.append(f'<line x1="56" y1="{cy+ch+28}" x2="{W-56}" y2="{cy+ch+28}" stroke="{STROKE}" stroke-width="1.2"/>')
    b.append(T(56, cy+ch+56, "Open, hardware-flexible JAX implementation", 15, SUB, 500))
    b.append(T(W-56, cy+ch+56, "arXiv:2312.11801   ·   github.com/rangell/usbs", 14, ACCENT, 600, MONO, anchor="end"))
    write("10_takeaway.svg", "\n".join(b))

for fn in [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10]:
    fn()
print("done")
