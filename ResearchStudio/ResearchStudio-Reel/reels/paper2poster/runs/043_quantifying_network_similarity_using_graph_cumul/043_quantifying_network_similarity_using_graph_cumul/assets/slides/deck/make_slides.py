#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 043.
Quantifying Network Similarity using Graph Cumulants (JMLR 2023).
Each narration chunk -> its own <g id="cue_..."> card with <title>=keywords.
No <image>, no gradients. viewBox 0 0 1280 720. Dark cobalt/teal theme."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
AMAP = json.load(open(os.path.join(HERE, "_anchor_map.json")))
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
BG = "#0B1B2B"
CARD = "#10263B"
CARD2 = "#12314A"
STROKE = "#1E3A52"
TEXT = "#E8F0F7"
MUTED = "#9DB2C4"
TEAL = "#35D0BA"
BLUE = "#4C8DFF"
GOLD = "#F5B841"
RED = "#FF6B6B"
GREEN = "#48D597"
FF = "Arial, 'Helvetica Neue', sans-serif"
MONO = "'DejaVu Sans Mono', 'Courier New', monospace"

def esc(s): return html.escape(str(s), quote=True)

def rect(x, y, w, h, fill=CARD, stroke=STROKE, sw=1.5, rx=14, op=1.0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"/>')

def line(x1, y1, x2, y2, stroke=STROKE, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def circ(cx, cy, r, fill, stroke="#0B1B2B", sw=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def T(x, y, s, size=18, fill=TEXT, weight="normal", anchor="start", ff=FF, spacing=None):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{ff}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}>{esc(s)}</text>')

def wrap(s, maxchars):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxchars:
            cur = (cur + " " + w).strip()
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def para(x, y, s, size=17, fill=MUTED, width=520, lh=None, weight="normal", ff=FF):
    lh = lh or int(size * 1.42)
    maxchars = max(8, int(width / (size * 0.53)))
    out = []
    yy = y
    for ln in wrap(s, maxchars):
        out.append(T(x, yy, ln, size=size, fill=fill, weight=weight, ff=ff))
        yy += lh
    return "\n".join(out), yy

def chip(x, y, w, txt, fill, tcol="#08131F"):
    return (rect(x, y, w, 26, fill=fill, stroke=fill, sw=0, rx=13) +
            T(x + w / 2, y + 18, txt, size=14, fill=tcol, weight="bold", anchor="middle"))

def header(kicker, title, idx):
    s = []
    s.append(rect(64, 44, 6, 40, fill=TEAL, stroke=TEAL, sw=0, rx=3))
    s.append(T(86, 62, kicker, size=15, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(86, 90, title, size=30, fill=TEXT, weight="bold"))
    s.append(T(1216, 68, f"{idx:02d} / 10", size=15, fill=MUTED, anchor="end", weight="bold"))
    s.append(line(64, 104, 1216, 104, stroke=STROKE, sw=1.5))
    return "\n".join(s)

def group(aid, kw, body):
    title = " ".join(kw) if isinstance(kw, list) else str(kw)
    return f'<g id="{esc(aid)}"><title>{esc(title)}</title>\n{body}\n</g>'

def chunks(sid):
    return AMAP[sid]["chunks"]

def svg_wrap(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>\n{inner}\n</svg>\n')

# small graph glyph helpers -------------------------------------------------
def mini_triangle(cx, cy, r, ecol=TEAL, ncol=BLUE):
    pts = [(cx, cy - r), (cx - r * 0.9, cy + r * 0.6), (cx + r * 0.9, cy + r * 0.6)]
    s = []
    for i in range(3):
        a = pts[i]; bpt = pts[(i + 1) % 3]
        s.append(line(a[0], a[1], bpt[0], bpt[1], stroke=ecol, sw=3))
    for p in pts:
        s.append(circ(p[0], p[1], 7, ncol))
    return "\n".join(s)

# ------------------------------------------------------------------ slides
def s_title(sid):
    c = chunks(sid); s = []
    s.append(rect(64, 44, 6, 40, fill=TEAL, stroke=TEAL, sw=0, rx=3))
    s.append(T(86, 66, "JMLR 2023  ·  UCL · GOOGLE RESEARCH · JOHNS HOPKINS", size=16, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(84, 150, "Quantifying Network Similarity", size=54, fill=TEXT, weight="bold"))
    s.append(T(84, 212, "using Graph Cumulants", size=54, fill=TEXT, weight="bold"))
    s.append(T(84, 256, "A stronger, free two-sample test for networks", size=23, fill=GOLD))
    s.append(T(84, 298, "Gecia Bravo-Hermsdorff · Lee M. Gunderson · Pierre-Andre Maugis · Carey E. Priebe", size=17, fill=MUTED))
    labels = [
        ("THE QUESTION", "Were two collections of networks drawn from the same distribution? Compare them through subgraph counts."),
        ("TWO TESTS", "Graph moments (raw subgraph densities) versus graph cumulants — the network analogue of mean, variance, and skew."),
        ("THE EVIDENCE", "Theory, simulation, and real gene networks: cumulants give markedly higher power, at no extra cost, even from one graph."),
        ("THE ADVICE", "Analyzing networks with motif densities? Convert them to the corresponding graph cumulants instead."),
    ]
    accents = [BLUE, TEAL, GOLD, GREEN]
    x0, y0, cw, gap = 64, 360, 278, 18
    for i, ch in enumerate(c):
        x = x0 + i * (cw + gap)
        b = [rect(x, y0, cw, 250, fill=CARD)]
        b.append(rect(x, y0, cw, 6, fill=accents[i], stroke=accents[i], sw=0, rx=3))
        b.append(T(x + 20, y0 + 44, labels[i][0], size=14, fill=accents[i], weight="bold", spacing="1"))
        p, _ = para(x + 20, y0 + 76, labels[i][1], size=16, fill=TEXT, width=cw - 40, lh=24)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(84, 648, "arxiv.org/abs/2107.11403   ·   Journal of Machine Learning Research, 2023", size=16, fill=MUTED))
    return svg_wrap("\n".join(s))

def s_problem(sid):
    c = chunks(sid); s = [header("PROBLEM", "Two-sample testing for unlabeled networks", AMAP[sid]["index"])]
    # c1 top-left: same process or different?
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Same process, or different?", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "You are handed two collections of networks, each sampled from some unknown distribution. Were they generated by the same process or by different ones?", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    # two little stacks of graph icons with a '?'
    b.append(mini_triangle(x + 120, y + 208, 20, ecol=BLUE, ncol=TEAL))
    b.append(mini_triangle(x + 400, y + 208, 20, ecol=GOLD, ncol=TEAL))
    b.append(T(x + cw / 2, y + 214, "= ?", size=30, fill=GOLD, anchor="middle", weight="bold"))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: no shared labels
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Nodes carry no shared labels", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "You cannot match nodes one to one across networks. All you can use are the statistics of their edges.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(rect(x + 26, y + 176, cw - 52, 52, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 208, "signal  =  subgraph-count statistics only", size=17, fill=TEAL, ff=MONO, weight="bold"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom wide: where it matters
    x, y, cw2 = 64, 400, 1152
    b = [rect(x, y, cw2, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 28, y + 44, "The two-sample testing problem for networks", size=21, fill=TEXT, weight="bold"))
    p, _ = para(x + 28, y + 84, "This deceptively simple question underlies many tasks: deciding whether two distributions of graphs differ, using only their exchangeable, unlabeled edges.", size=18, fill=MUTED, width=cw2 - 56, lh=26)
    b.append(p)
    b.append(chip(x + 28, y + 190, 300, "comparing brain connectomes", BLUE))
    b.append(chip(x + 344, y + 190, 380, "distinguishing biological interaction networks", TEAL))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def two_by_two(sid, kicker, title, cards, accents=None):
    c = chunks(sid); s = [header(kicker, title, AMAP[sid]["index"])]
    accents = accents or [TEAL, BLUE, GOLD, GREEN]
    pos = [(64, 122), (656, 122), (64, 400), (656, 400)]
    cw, chh = 560, 258
    for i, ch in enumerate(c):
        x, y = pos[i]; head, body = cards[i]
        b = [rect(x, y, cw, chh, fill=CARD)]
        b.append(rect(x, y, 6, chh, fill=accents[i % len(accents)], stroke=accents[i % len(accents)], sw=0, rx=3))
        b.append(T(x + 26, y + 42, head, size=21, fill=TEXT, weight="bold"))
        b.append(line(x + 26, y + 56, x + cw - 26, y + 56, stroke=STROKE, sw=1))
        p, _ = para(x + 26, y + 88, body, size=17, fill=MUTED, width=cw - 52, lh=25)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_motivation(sid):
    c = chunks(sid); s = [header("MOTIVATION", "Raw motif densities are entangled", AMAP[sid]["index"])]
    # c1 top-left
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Networks summarized by motifs", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "Analysts routinely characterize a network by counting small substructures — subgraphs, or motifs — such as edges, wedges, and triangles.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(mini_triangle(x + 120, y + 214, 16, ecol=TEAL, ncol=BLUE))
    b.append(T(x + 200, y + 220, "edge   wedge   triangle", size=14, fill=MUTED))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: entangled densities diagram
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "But their densities are entangled", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "The density of an edge is strongly correlated with the density of a wedge, and so on across orders.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    # correlation link
    b.append(rect(x + 40, y + 168, 150, 46, fill=CARD2, stroke=BLUE, sw=2))
    b.append(T(x + 115, y + 197, "edge density", size=15, fill=TEXT, anchor="middle", weight="bold"))
    b.append(T(x + 245, y + 197, "≈", size=26, fill=RED, anchor="middle", weight="bold"))
    b.append(rect(x + 300, y + 168, 165, 46, fill=CARD2, stroke=GOLD, sw=2))
    b.append(T(x + 382, y + 197, "wedge density", size=15, fill=TEXT, anchor="middle", weight="bold"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Weak tests, costly workarounds", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "This redundancy weakens any test built directly on the densities. Many existing methods resort to costly resampling just to judge whether a difference is significant.", size=17, fill=MUTED, width=cw - 52, lh=26)
    b.append(p)
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The question", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "Is there a better set of coordinates — one that removes lower-order redundancy — that makes these tests both stronger and cheaper?", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    b.append(chip(x + 26, y + 200, 280, "stronger  +  cheaper, at once", TEAL))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_contribution(sid):
    c = chunks(sid); s = [header("CONTRIBUTION", "Swap moments for cumulants", AMAP[sid]["index"])]
    pos = [(64, 122), (656, 122), (64, 400), (656, 400)]
    cw, chh = 560, 258
    nums = ["1", "2", "3", "4"]
    accents = [TEAL, BLUE, GOLD, GREEN]
    heads = ["A drop-in swap", "More power, same cost", "Analytic chi-squared null", "Works with a single graph"]
    bodies = [
        "The central contribution is a simple, drop-in two-sample test for networks that swaps graph moments for graph cumulants — nothing else in the pipeline changes.",
        "Across theory, controlled simulation, and real biological networks, this swap consistently increases statistical power without changing the computational cost.",
        "The cumulant test statistic tracks a known chi-squared distribution remarkably well, even with only a handful of graphs, so false-positive rates can be controlled analytically.",
        "Strikingly, the cumulant test even works when just one graph is observed per sample — a regime where the moment test is entirely undefined.",
    ]
    for i, ch in enumerate(c):
        x, y = pos[i]
        b = [rect(x, y, cw, chh, fill=CARD)]
        b.append(circ(x + 42, y + 44, 20, accents[i], stroke="none", sw=0))
        b.append(T(x + 42, y + 51, nums[i], size=22, fill="#08131F", weight="bold", anchor="middle"))
        b.append(T(x + 78, y + 51, heads[i], size=21, fill=TEXT, weight="bold"))
        b.append(line(x + 26, y + 66, x + cw - 26, y + 66, stroke=STROKE, sw=1))
        p, _ = para(x + 26, y + 98, bodies[i], size=16, fill=MUTED, width=cw - 52, lh=24)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_method(sid):
    c = chunks(sid); s = [header("METHOD", "Same recipe, better coordinates", AMAP[sid]["index"])]
    # c1 top-left: three-step recipe pipeline
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "A shared three-step recipe", size=20, fill=TEXT, weight="bold"))
    def pbox(px, py, pw, txt, col):
        return rect(px, py, pw, 74, fill=CARD2, stroke=col, sw=2) + \
               T(px + pw / 2, py + 44, txt, size=15, fill=TEXT, weight="bold", anchor="middle")
    steps = [("1. choose max\nsubgraph order", BLUE), ("2. estimate each\ndistribution", GOLD), ("3. measure the\ndistance", TEAL)]
    pw = 152; py = y + 96
    for i, (txt, col) in enumerate(steps):
        px = x + 26 + i * (pw + 14)
        l1, l2 = txt.split("\n")
        b.append(rect(px, py, pw, 84, fill=CARD2, stroke=col, sw=2))
        b.append(T(px + pw / 2, py + 36, l1, size=14, fill=TEXT, weight="bold", anchor="middle"))
        b.append(T(px + pw / 2, py + 56, l2, size=14, fill=TEXT, weight="bold", anchor="middle"))
        if i < 2:
            b.append(T(px + pw + 7, py + 48, ">", size=22, fill=MUTED, anchor="middle", weight="bold"))
    b.append(T(x + 26, y + 224, "Identical for both tests — only the coordinates differ.", size=15, fill=MUTED))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: Mahalanobis distance + coordinates
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Squared Mahalanobis distance", size=20, fill=TEXT, weight="bold"))
    b.append(rect(x + 26, y + 62, cw - 52, 52, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 94, "d^2 = (k_A - k_B)^T (S_A + S_B)^-1 (k_A - k_B)", size=16, fill=TEAL, ff=MONO, weight="bold"))
    p, _ = para(x + 26, y + 140, "It weights differences by an analytically computed covariance. The only choice: raw graph moments (injective-homomorphism densities) versus graph cumulants.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: Mobius transform
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Cumulants via a Mobius transform", size=20, fill=TEXT, weight="bold"))
    b.append(rect(x + 26, y + 62, cw - 52, 48, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 92, "mu_g  =  sum over partitions pi   product_b  k_(g_b)", size=15, fill=GOLD, ff=MONO, weight="bold"))
    p, _ = para(x + 26, y + 134, "A combinatorial sum over all connectivity-respecting partitions of a subgraph's edges. Cumulants capture the excess propensity of a structure beyond what its smaller pieces predict.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: same complexity
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The swap is free", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "Computing the covariances only needs subgraph counts up to twice the chosen order. So both tests share the same computational complexity.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(rect(x + 26, y + 180, cw - 52, 52, fill=CARD2, stroke=STROKE))
    b.append(T(x + cw / 2, y + 212, "moments  and  cumulants :  same  O(n^w)", size=17, fill=GREEN, ff=MONO, weight="bold", anchor="middle"))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_dataset(sid):
    c = chunks(sid); s = [header("DATASET / BENCHMARK", "Synthetic block models, then real gene networks", AMAP[sid]["index"])]
    # c1 top-left: controlled competition
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "A controlled competition first", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "To compare the two tests fairly, the authors begin on synthetic data where the ground-truth distributions are known exactly.", size=17, fill=MUTED, width=cw - 52, lh=26)
    b.append(p)
    b.append(chip(x + 26, y + 196, 260, "known ground-truth distribution", TEAL))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: SBM matchup
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Heterogeneous vs assortative SBM", size=19, fill=TEXT, weight="bold"))
    b.append(T(x + 26, y + 64, "same edge density, so genuinely hard to tell apart", size=13, fill=MUTED))
    # left icon: hub
    hx, hy = x + 130, y + 168
    for dx, dy in [(-55, 20), (-30, 55), (25, 55), (55, 20), (-5, -50)]:
        b.append(line(hx, hy, hx + dx, hy + dy, stroke=MUTED, sw=2))
    for dx, dy in [(-55, 20), (-30, 55), (25, 55), (55, 20), (-5, -50)]:
        b.append(circ(hx + dx, hy + dy, 7, BLUE))
    b.append(circ(hx, hy, 12, GOLD))
    b.append(T(hx, y + 246, "uneven degrees", size=13, fill=MUTED, anchor="middle"))
    # right icon: two communities
    ax = x + 400
    comm1 = [(ax - 40, hy - 30), (ax - 20, hy), (ax - 45, hy + 25)]
    comm2 = [(ax + 40, hy - 25), (ax + 22, hy + 5), (ax + 48, hy + 30)]
    for grp in (comm1, comm2):
        for i in range(len(grp)):
            for j in range(i + 1, len(grp)):
                b.append(line(grp[i][0], grp[i][1], grp[j][0], grp[j][1], stroke=MUTED, sw=1.5))
    b.append(line(comm1[1][0], comm1[1][1], comm2[1][0], comm2[1][1], stroke=STROKE, sw=1.5, dash="3 3"))
    for p_ in comm1: b.append(circ(p_[0], p_[1], 7, TEAL))
    for p_ in comm2: b.append(circ(p_[0], p_[1], 7, GREEN))
    b.append(T(ax, y + 246, "two communities", size=13, fill=MUTED, anchor="middle"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: size sweep
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Sweeping size and sample count", size=20, fill=TEXT, weight="bold"))
    kpis = [("128 - 256", "nodes per graph n"), ("s", "graphs per sample, varied")]
    for i, (v, l) in enumerate(kpis):
        px = x + 26 + i * 262; py = y + 78
        b.append(rect(px, py, 246, 84, fill=CARD2, stroke=STROKE))
        b.append(T(px + 18, py + 46, v, size=30, fill=GOLD, weight="bold"))
        b.append(T(px + 18, py + 70, l, size=14, fill=MUTED))
    b.append(T(x + 26, y + 210, "Two graph sizes and a range of sample sizes s per test.", size=15, fill=MUTED))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: real data FunCoup
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Real genetic-interaction networks", size=19, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "Gene networks from the FunCoup repository, again matched in edge density so that separating them demands higher-order structure.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    orgs = ["Arabidopsis", "Mouse", "Human", "Rat"]
    cols = [TEAL, BLUE, GOLD, RED]
    for i, o in enumerate(orgs):
        px = x + 26 + (i % 2) * 265; py = y + 168 + (i // 2) * 40
        b.append(chip(px, py, 250, o + "  ·  FunCoup", cols[i]))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_keyresult(sid):
    c = chunks(sid); s = [header("KEY RESULT", "Cumulants win on synthetic and real data", AMAP[sid]["index"])]
    # c1 top-left: framing
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The results are decisive", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "Across every setting tested, the test built on graph cumulants matches or beats the moment test — and the gap grows exactly where testing is hardest.", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    b.append(chip(x + 26, y + 200, 300, "cumulants  >=  moments, everywhere", TEAL))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: ROC mini chart
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Higher area under the ROC curve", size=19, fill=TEXT, weight="bold"))
    # axis box
    ox, oy, side = x + 60, y + 80, 150
    b.append(rect(ox, oy, side, side, fill="#0C1E30", stroke=STROKE, sw=1.5, rx=6))
    b.append(line(ox, oy + side, ox + side, oy, stroke=MUTED, sw=1.5, dash="4 3"))  # chance diagonal
    # cumulant curve hugs upper-left (teal)
    b.append(f'<polyline points="{ox},{oy+side} {ox+18},{oy+40} {ox+70},{oy+14} {ox+side},{oy}" fill="none" stroke="{TEAL}" stroke-width="3"/>')
    # moment curve middling (blue)
    b.append(f'<polyline points="{ox},{oy+side} {ox+50},{oy+95} {ox+100},{oy+55} {ox+side},{oy}" fill="none" stroke="{BLUE}" stroke-width="3"/>')
    b.append(T(ox + side / 2, oy + side + 22, "false positive rate", size=12, fill=MUTED, anchor="middle"))
    # legend
    lx = x + 250
    b.append(rect(lx, y + 96, 14, 14, fill=TEAL, stroke=TEAL, sw=0, rx=3)); b.append(T(lx + 22, y + 108, "cumulants", size=15, fill=TEAL, weight="bold"))
    b.append(rect(lx, y + 126, 14, 14, fill=BLUE, stroke=BLUE, sw=0, rx=3)); b.append(T(lx + 22, y + 138, "moments", size=15, fill=BLUE, weight="bold"))
    b.append(T(lx, y + 176, "chance = diagonal", size=13, fill=MUTED))
    b.append(T(lx, y + 200, "The gap widens as the", size=13, fill=MUTED))
    b.append(T(lx, y + 218, "graphs per sample s shrink.", size=13, fill=MUTED))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: moment breaks at s<4
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The moment test breaks down", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + 26, y + 66, "below four graphs per sample its covariance is singular", size=13, fill=MUTED))
    # two KPI panels
    b.append(rect(x + 26, y + 88, 246, 120, fill=CARD2, stroke=RED, sw=1.5))
    b.append(T(x + 149, y + 150, "s >= 4", size=34, fill=RED, weight="bold", anchor="middle"))
    b.append(T(x + 149, y + 182, "moment test to be defined", size=14, fill=MUTED, anchor="middle"))
    b.append(rect(x + 288, y + 88, 246, 120, fill=CARD2, stroke=GREEN, sw=1.5))
    b.append(T(x + 411, y + 150, "s = 1", size=34, fill=GREEN, weight="bold", anchor="middle"))
    b.append(T(x + 411, y + 182, "cumulant test still works", size=14, fill=MUTED, anchor="middle"))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: real data too
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Same story on real networks", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "With edge density held equal, adding more subgraph orders steadily sharpens the cumulant test — while it makes the moment test overfit and perform worse.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 196, 200, "cumulants: sharpen", GREEN))
    b.append(chip(x + 236, y + 196, 200, "moments: overfit", RED))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_ablation(sid):
    c = chunks(sid); s = [header("ABLATION STUDY", "Sweeping subgraph order r on real data", AMAP[sid]["index"])]
    # helper mini AUC bar pair
    def auc_panel(px, py, pw, title_txt, mom, cum, note, col):
        out = [rect(px, py, pw, 258, fill=CARD), rect(px, py, 6, 258, fill=col, stroke=col, sw=0, rx=3)]
        out.append(T(px + 26, py + 42, title_txt, size=20, fill=TEXT, weight="bold"))
        out.append(T(px + 26, py + 68, note, size=13, fill=MUTED))
        base = py + 228; chart_top = py + 100; maxh = base - chart_top
        scale = maxh / 0.45  # AUC 0.5 (chance) .. 0.95 (near-perfect) fills the panel
        yax = px + 70; bw = 140
        out.append(line(yax, chart_top, yax, base, stroke=STROKE, sw=1.5))
        out.append(line(yax, chart_top, px + pw - 34, chart_top, stroke=STROKE, sw=1, dash="4 4"))
        out.append(T(yax - 12, chart_top + 5, "1.0", size=12, fill=MUTED, anchor="end"))
        out.append(line(yax, base, px + pw - 34, base, stroke=STROKE, sw=1.5))
        out.append(T(yax - 12, base + 4, "0.5", size=12, fill=MUTED, anchor="end"))
        for i, (lab, val, bcol) in enumerate([("moments", mom, BLUE), ("cumulants", cum, TEAL)]):
            bxx = px + 150 + i * 210
            bh = max(5, (val - 0.5) * scale)
            out.append(rect(bxx, base - bh, bw, bh, fill=bcol, stroke=bcol, sw=0, rx=5))
            out.append(T(bxx + bw / 2, base + 22, lab, size=14, fill=bcol, anchor="middle", weight="bold"))
        return out
    y0 = 122
    # c1 r=1 (top-left)
    panel = auc_panel(64, y0, 560, "Order r = 1  (edges only)", 0.52, 0.52, "AUC axis 0.5 (chance) to 1.0 - schematic of the trend", TEAL)
    b = panel + [T(64 + 320, y0 + 132, "neither test can separate", size=14, fill=RED, anchor="middle"),
                 T(64 + 320, y0 + 150, "the density-matched networks", size=14, fill=RED, anchor="middle")]
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 r=2 (top-right)
    b = auc_panel(656, y0, 560, "Order r = 2  (add wedges)", 0.63, 0.80, "cumulants already tip the balance", GOLD)
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 r=3 (bottom-left)
    y0 = 400
    b = auc_panel(64, y0, 560, "Order r = 3  (add triangles)", 0.56, 0.90, "cumulants pull further ahead; moments overfit and slip back", BLUE)
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 robustness text (bottom-right)
    x, y, cw = 656, 400, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "A robust, qualitative feature", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "Sweeping the block-model parameters and the sample size confirms the advantage is not a quirk of one setting, but a stable, qualitative property of using cumulants.", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    b.append(chip(x + 26, y + 202, 300, "holds across every regime swept", GREEN))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_headline(sid):
    c = chunks(sid); s = [header("HEADLINE NUMBERS", "The impact in four numbers", AMAP[sid]["index"])]
    tiles = [
        ("s: 4 -> 1", "The moment test needs at least four graphs per sample to be defined; the cumulant test works with as few as one.", RED),
        ("free", "Both use connected subgraphs up to three edges and share the same O(n^w) complexity, so the extra power costs nothing.", GREEN),
        ("chi^2, 5 df", "Under the null, the cumulant statistic hugs a chi-squared with five degrees of freedom even for small samples; the moment statistic visibly deviates.", TEAL),
        ("11k - 16k", "Real gene networks tested span about eleven to sixteen thousand nodes and hundreds of thousands of edges, all density-matched.", GOLD),
    ]
    tw, gap = 273, 20
    for i, ch in enumerate(c):
        x = 64 + i * (tw + gap); y = 140
        v, l, col = tiles[i]
        b = [rect(x, y, tw, 470, fill=CARD)]
        b.append(rect(x, y, tw, 8, fill=col, stroke=col, sw=0, rx=4))
        b.append(T(x + tw / 2, y + 160, v, size=50, fill=col, weight="bold", anchor="middle"))
        b.append(line(x + 28, y + 196, x + tw - 28, y + 196, stroke=STROKE, sw=1))
        p, _ = para(x + 26, y + 240, l, size=17, fill=TEXT, width=tw - 52, lh=26)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_takeaway(sid):
    c = chunks(sid); s = [header("TAKEAWAY", "Use graph cumulants", AMAP[sid]["index"])]
    # c1 top banner
    x, y, cw = 64, 122, 1152
    b = [rect(x, y, cw, 70, fill=CARD), rect(x, y, 6, 70, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 28, y + 44, "The bottom line is a practical one - and it costs you nothing.", size=21, fill=TEXT, weight="bold"))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    tiles = [
        ("Convert densities to cumulants", "Whenever you analyze networks through subgraph or motif densities, take one extra step and convert them into the corresponding graph cumulants.", TEAL),
        ("Gain power for free", "You lose nothing in computational cost, but gain sharply higher statistical power, a trustworthy chi-squared null for controlling error, and the ability to test even a single observed graph.", GREEN),
        ("A more natural feature set", "Graph cumulants offer a principled, more natural first layer of features for comparing the local structure of networks.", GOLD),
    ]
    tw, gap = 368, 24
    for i, ch in enumerate(c[1:]):
        x = 64 + i * (tw + gap); y = 214
        head, body, col = tiles[i]
        b = [rect(x, y, tw, 400, fill=CARD)]
        b.append(rect(x, y, tw, 8, fill=col, stroke=col, sw=0, rx=4))
        b.append(circ(x + 42, y + 58, 18, col, stroke="none", sw=0))
        b.append(T(x + 42, y + 65, str(i + 1), size=20, fill="#08131F", weight="bold", anchor="middle"))
        hp, hy = para(x + 74, y + 52, head, size=21, fill=TEXT, width=tw - 100, lh=27, weight="bold")
        b.append(hp)
        p, _ = para(x + 34, y + 150, body, size=18, fill=MUTED, width=tw - 68, lh=27)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(64, 660, "Quantifying Network Similarity using Graph Cumulants  ·  JMLR 2023  ·  arxiv.org/abs/2107.11403", size=15, fill=MUTED))
    return svg_wrap("\n".join(s))

BUILDERS = {
    "title": s_title, "problem": s_problem, "motivation": s_motivation,
    "contribution": s_contribution, "method": s_method, "dataset-benchmark": s_dataset,
    "key-result": s_keyresult, "ablation-study": s_ablation,
    "headline-numbers": s_headline, "takeaway": s_takeaway,
}

order = sorted(AMAP.items(), key=lambda kv: kv[1]["index"])
for sid, meta in order:
    svg = BUILDERS[sid](sid)
    fn = f"{meta['index']:02d}_{sid}.svg"
    open(os.path.join(OUT, fn), "w").write(svg)
    print("wrote", fn)
print("done ->", OUT)
