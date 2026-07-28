#!/usr/bin/env python3
"""All-native SVG deck builder for Merlin (run 018 - Learning to Reach Goals
via Diffusion). Reads the anchor contract and wraps every narration chunk in
its own <g id="cue_..."> card with <title> keywords, so
--require-pptx-anchors resolves from PPTX geometry. Dark cobalt/teal theme,
zero <image>, zero gradients, ASCII-only equations."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = os.path.join(HERE, "..", "..", "meta", "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
BG = "#0B1B2B"
PANEL = "#122A40"
PANEL2 = "#0F2236"
STROKE = "#1E3E5A"
INK = "#EAF2FA"
MUTE = "#9FB6CC"
TEAL = "#2FB6A8"
BLUE = "#4C86F0"
GOLD = "#E0A93B"
RED = "#E0655B"
GREEN = "#49C08A"
VIOLET = "#9B7BE0"
SANS = "Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO = "'DejaVu Sans Mono', 'Courier New', monospace"

contract = json.load(open(CONTRACT))
CMAP = {}
for s in contract["slides"]:
    CMAP[s["id"]] = {
        "index": s["index"],
        "chunks": [{"aid": c["anchor_id"], "kw": " ".join(c.get("cue_keywords", []))}
                   for c in s["chunks"]],
    }


def esc(t):
    return html.escape(str(t), quote=True)


def T(x, y, t, size=17, fill=INK, weight="normal", anchor="start", family=SANS, spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{sp}>{esc(t)}</text>')


def wrap(t, maxc):
    words = t.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxc:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(x, y, t, size=16, fill=MUTE, maxc=52, lh=23, weight="normal"):
    out = []
    ls = wrap(t, maxc)
    for i, ln in enumerate(ls):
        out.append(T(x, y + i * lh, ln, size=size, fill=fill, weight=weight))
    return "".join(out), y + len(ls) * lh


def card(aid, kw, x, y, w, h, fill=PANEL, accent=TEAL):
    s = f'<g id="{aid}"><title>{esc(kw)}</title>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{STROKE}" stroke-width="1.2"/>'
    s += f'<rect x="{x}" y="{y+18}" width="5" height="30" rx="2.5" fill="{accent}"/>'
    return s


def endg():
    return "</g>"


def header(slide_no, title, kicker):
    s = []
    s.append(f'<rect x="56" y="52" width="7" height="34" rx="3" fill="{TEAL}"/>')
    s.append(T(78, 66, kicker, size=15, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(78, 104, title, size=34, fill=INK, weight="bold"))
    s.append(T(1224, 92, f"Merlin  ·  {slide_no:02d} / 09", size=15, fill=MUTE, anchor="end"))
    s.append(f'<line x1="56" y1="128" x2="1224" y2="128" stroke="{STROKE}" stroke-width="1"/>')
    return "".join(s)


def footer(txt):
    return T(56, 706, txt, size=13, fill="#6E869C")


def svg_open():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="{SANS}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>')


def svg_close():
    return "</svg>"


GX = [56, 654]
CW = 570
def row_y(r):
    return 168 + r * 268
CH = 250


def text_card(ci, sid, heading, body, x, y, w=CW, h=CH, accent=TEAL, maxc=54):
    c = CMAP[sid]["chunks"][ci]
    s = card(c["aid"], c["kw"], x, y, w, h, accent=accent)
    s += T(x + 26, y + 44, heading, size=21, fill=INK, weight="bold")
    p, _ = para(x + 26, y + 80, body, size=16, fill=MUTE, maxc=maxc, lh=24)
    s += p
    s += endg()
    return s


slides = {}

# ---------- Slide 1: title ----------
def s1():
    sid = "title"
    s = [svg_open()]
    s.append(f'<rect x="56" y="52" width="7" height="34" rx="3" fill="{TEAL}"/>')
    s.append(T(78, 66, "ICML 2024  ·  McGILL UNIVERSITY / MILA", size=15, fill=TEAL, weight="bold", spacing="1"))
    # c1 title banner
    c = CMAP[sid]["chunks"][0]
    s.append(f'<g id="{c["aid"]}"><title>{esc(c["kw"])}</title>')
    s.append(T(78, 150, "Learning to Reach Goals via Diffusion", size=50, fill=INK, weight="bold"))
    s.append(T(78, 196, "What if reaching a goal were just the reverse of a diffusion process?", size=21, fill=MUTE))
    s.append("</g>")
    cards = [
        (1, "Authors & venue", "Vineet Jain and Siamak Ravanbakhsh (McGill / Mila) reframe goal-conditioned RL through denoising diffusion. ICML 2024.", BLUE),
        (2, "Merlin, in one idea", "Build trajectories that drift away from goal states, then train a policy to reverse that drift, like a diffusion denoiser.", TEAL),
        (3, "Why it matters", "A value-function-free method that reaches goals from any start, using a single denoising step per environment step.", GOLD),
    ]
    xs = [56, 466, 876]
    for ci, hd, bd, ac in cards:
        c = CMAP[sid]["chunks"][ci]
        x = xs[ci - 1]
        s.append(card(c["aid"], c["kw"], x, 250, 348, 300, accent=ac))
        s.append(T(x + 24, 296, hd, size=20, fill=INK, weight="bold"))
        p, _ = para(x + 24, 334, bd, size=16, fill=MUTE, maxc=35, lh=25)
        s.append(p)
        s.append("</g>")
    s.append(footer("Jain & Ravanbakhsh — Learning to Reach Goals via Diffusion (ICML 2024)  ·  arXiv:2310.02505  ·  code: github.com/vineetjain96/merlin"))
    s.append(svg_close())
    return "".join(s)
slides["title"] = s1()

# ---------- Slide 2: problem ----------
def s2():
    sid = "problem"
    s = [svg_open(), header(2, "Offline goal-reaching breaks value estimates", "PROBLEM")]
    s.append(text_card(0, sid, "The goal", "Goal-conditioned RL trains one agent to reach any target state, with a sparse reward of 1 at the goal and 0 elsewhere.", GX[0], row_y(0), accent=BLUE))
    s.append(text_card(1, sid, "Offline constraint", "In the offline setting the agent learns purely from a fixed, pre-collected dataset, with no further environment interaction.", GX[1], row_y(0), accent=TEAL))
    s.append(text_card(2, sid, "The value-function trap", "Most methods estimate a value function — but offline, with sparse binary rewards, that estimate becomes fragile.", GX[0], row_y(1), accent=GOLD))
    s.append(text_card(3, sid, "Errors compound", "Policies pick actions absent from the data; value estimates for them are wrong, and the errors snowball until the policy diverges.", GX[1], row_y(1), accent=RED))
    s.append(footer("Sparse binary rewards make the value-estimation problem even harder, so stability, not capacity, is the bottleneck."))
    s.append(svg_close())
    return "".join(s)
slides["problem"] = s2()

# ---------- Slide 3: motivation ----------
def s3():
    sid = "motivation"
    s = [svg_open(), header(3, "Borrow the machinery of diffusion", "MOTIVATION")]
    s.append(text_card(0, sid, "Diffusion models", "A powerful generative family: a forward process destroys data into Gaussian noise, and a learned reverse process denoises it back — no value function.", GX[0], row_y(0), accent=BLUE, maxc=52))
    s.append(text_card(1, sid, "The key question", "What if we treat goal states as the data distribution we want to model, and learn to reverse a process that walks away from them?", GX[1], row_y(0), accent=TEAL, maxc=52))
    s.append(text_card(2, sid, "The analogy", "Noise walks away from the data manifold; in GCRL we can construct trajectories that walk away from potential goals.", GX[0], row_y(1), accent=GOLD))
    s.append(text_card(3, sid, "Why it helps", "Learning to reverse those deviations mirrors learning the score function — sidestepping the value estimation that plagues offline methods.", GX[1], row_y(1), accent=GREEN, maxc=52))
    s.append(footer("Prior fixes add policy constraints or conservative value updates, which compromise performance and hurt generalization."))
    s.append(svg_close())
    return "".join(s)
slides["motivation"] = s3()

# ---------- Slide 4: contribution ----------
def s4():
    sid = "contribution"
    s = [svg_open(), header(4, "Three contributions", "CONTRIBUTION")]
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 168, 1168, 78, fill=PANEL2, accent=TEAL))
    s.append(T(82, 216, "Merlin recasts goal-conditioned RL as reverse diffusion — with three main consequences.", size=20, fill=INK, weight="bold"))
    s.append("</g>")
    trip = [
        (1, "1 · A fresh perspective", "Merlin casts goal-conditioned RL as a reverse diffusion process operating directly over the environment's state space.", BLUE),
        (2, "2 · Just behavior cloning", "It proves the reverse process can be learned by goal-conditioned behavior cloning with hindsight relabeling — no value function.", TEAL),
        (3, "3 · Three variants", "Three ways to build the goal-departing trajectories: a fixed rule, a parametric forward model (Merlin-P), and Merlin-NP with stitching.", GOLD),
    ]
    xs = [56, 466, 876]
    for k, (ci, hd, bd, ac) in enumerate(trip):
        c = CMAP[sid]["chunks"][ci]
        x = xs[k]
        s.append(card(c["aid"], c["kw"], x, 270, 348, 280, accent=ac))
        s.append(T(x + 24, 316, hd, size=19, fill=INK, weight="bold"))
        p, _ = para(x + 24, 354, bd, size=16, fill=MUTE, maxc=35, lh=25)
        s.append(p)
        s.append("</g>")
    s.append(footer("Merlin is the first method to perform diffusion directly in the state space — one denoising iteration per environment step."))
    s.append(svg_close())
    return "".join(s)
slides["contribution"] = s4()

# ---------- Slide 5: method ----------
def s5():
    sid = "method"
    s = [svg_open(), header(5, "Reverse a goal-departing trajectory", "METHOD")]
    # c1: reverse-trajectory pipeline (top wide)
    c = CMAP[sid]["chunks"][0]
    x, y, w, h = 56, 168, 1168, 172
    s.append(card(c["aid"], c["kw"], x, y, w, h, accent=TEAL))
    s.append(T(x + 26, y + 40, "Read an offline trajectory backwards, starting from its goal state", size=19, fill=INK, weight="bold"))
    # trajectory dots: goal on right (green star), states drift left; green reverse arrows back to goal
    ty = y + 108
    gx0 = x + 60
    step = 168
    labels = ["s₀ (start)", "s₁", "s₂", "s_T", "goal g"]
    for i in range(5):
        cx = gx0 + i * step
        col = GREEN if i == 4 else (BLUE if i == 0 else MUTE)
        if i == 4:
            s.append(f'<polygon points="{cx},{ty-13} {cx+4},{ty-4} {cx+13},{ty-4} {cx+6},{ty+3} {cx+9},{ty+12} {cx},{ty+6} {cx-9},{ty+12} {cx-6},{ty+3} {cx-13},{ty-4} {cx-4},{ty-4}" fill="{GREEN}"/>')
        else:
            s.append(f'<circle cx="{cx}" cy="{ty}" r="10" fill="{PANEL2}" stroke="{col}" stroke-width="2"/>')
        s.append(T(cx, ty + 34, labels[i], size=13, fill=col, anchor="middle"))
        if i < 4:
            nx = cx + step
            # red forward (drift away): goal -> start, above
            s.append(f'<line x1="{nx-14}" y1="{ty-16}" x2="{cx+14}" y2="{ty-16}" stroke="{RED}" stroke-width="2" stroke-dasharray="5 4"/>')
            # green reverse (policy): start -> goal, below
            s.append(f'<line x1="{cx+14}" y1="{ty+16}" x2="{nx-14}" y2="{ty+16}" stroke="{GREEN}" stroke-width="2.4"/>')
            s.append(f'<polygon points="{nx-14},{ty+16} {nx-22},{ty+11} {nx-22},{ty+21}" fill="{GREEN}"/>')
    s.append(T(x + 26, y + 158, "red dashed = forward drift q(s_t | s_t+1)   ·   green = learned reverse policy πθ", size=13, fill=MUTE))
    s.append("</g>")
    # c2: forward-process card (mid-left)
    c = CMAP[sid]["chunks"][1]
    x2, y2 = 56, 360
    s.append(card(c["aid"], c["kw"], x2, y2, 570, 178, accent=GOLD))
    s.append(T(x2 + 26, y2 + 42, "Forward diffusion in state space", size=18, fill=INK, weight="bold"))
    p, _ = para(x2 + 26, y2 + 74, "Each forward step pushes states progressively away from the goal — exactly like adding noise in an image diffusion model. Merlin then learns to reverse the drift, one step at a time.", size=15, fill=MUTE, maxc=58, lh=23)
    s.append(p)
    s.append("</g>")
    # c3: equation card (mid-right)
    c = CMAP[sid]["chunks"][2]
    x3, y3 = 654, 360
    s.append(card(c["aid"], c["kw"], x3, y3, 570, 178, accent=BLUE))
    s.append(T(x3 + 26, y3 + 42, "Likelihood of goals  =  behavior cloning", size=18, fill=INK, weight="bold"))
    s.append(f'<rect x="{x3+24}" y="{y3+58}" width="522" height="46" rx="8" fill="{PANEL2}" stroke="{STROKE}"/>')
    s.append(T(x3 + 40, y3 + 87, "max_θ  E[ log πθ(a | s, g) ]", size=18, fill=TEAL, family=MONO))
    p, _ = para(x3 + 26, y3 + 128, "Maximizing the log-likelihood of goal states under the reverse process reduces to plain behavior cloning — so no value function is ever needed.", size=14, fill=MUTE, maxc=60, lh=21)
    s.append(p)
    s.append("</g>")
    # c4: three variants + single-step (bottom wide)
    c = CMAP[sid]["chunks"][3]
    x4, y4 = 56, 556
    s.append(card(c["aid"], c["kw"], x4, y4, 1168, 128, fill=PANEL2, accent=VIOLET))
    s.append(T(x4 + 26, y4 + 38, "Three ways to build the goal-departing trajectories  ·  one denoising step per environment step", size=17, fill=INK, weight="bold"))
    vs = [("Fixed", "a hand-designed construction rule"),
          ("Merlin-P", "a learned parametric forward model"),
          ("Merlin-NP", "non-parametric nearest-neighbor stitching in latent space")]
    vx = x4 + 26
    for i, (nm, dd) in enumerate(vs):
        bx = vx + i * 388
        s.append(f'<rect x="{bx}" y="{y4+58}" width="360" height="52" rx="8" fill="{PANEL}" stroke="{STROKE}"/>')
        s.append(T(bx + 16, y4 + 82, nm, size=16, fill=VIOLET, weight="bold"))
        p, _ = para(bx + 16, y4 + 100, dd, size=13, fill=MUTE, maxc=44, lh=16)
        s.append(p)
    s.append("</g>")
    s.append(svg_close())
    return "".join(s)
slides["method"] = s5()

# ---------- Slide 6: dataset-benchmark ----------
def s6():
    sid = "dataset-benchmark"
    s = [svg_open(), header(6, "Ten offline goal-conditioned tasks", "DATASET / BENCHMARK")]
    # c1 banner with task chips
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 168, 1168, 118, fill=PANEL2, accent=TEAL))
    s.append(T(82, 206, "Standard offline GCRL benchmark (Yang et al., 2021) — 10 control tasks, easy to hard", size=19, fill=INK, weight="bold"))
    chips = ["PointReach", "PointRooms", "Reacher", "SawyerReach", "SawyerDoor", "FetchReach",
             "FetchPush", "FetchPick", "FetchSlide", "HandReach"]
    cx = 82
    cyr = 232
    for i, ch in enumerate(chips):
        wch = 12 + len(ch) * 8.6
        if cx + wch > 1198:
            cx = 82; cyr += 34
        col = BLUE if i < 6 else GOLD
        s.append(f'<rect x="{cx}" y="{cyr}" width="{wch:.0f}" height="26" rx="13" fill="{PANEL}" stroke="{col}" stroke-width="1.3"/>')
        s.append(T(cx + wch / 2, cyr + 18, ch, size=13, fill=INK, anchor="middle"))
        cx += wch + 12
    s.append("</g>")
    dom = [
        (1, "Task setup", "Every task uses a sparse binary reward and a maximum trajectory length of T = 50 steps.", BLUE),
        (2, "Two dataset flavors", "An expert dataset from a trained policy (with noise for diversity), and a random dataset from random actions.", TEAL),
        (3, "State and pixels", "Both low-dimensional state observations and high-dimensional pixel observations, averaged over 10 seeds.", GOLD),
    ]
    xs = [56, 466, 876]
    for k, (ci, hd, bd, ac) in enumerate(dom):
        c = CMAP[sid]["chunks"][ci]
        x = xs[k]
        s.append(card(c["aid"], c["kw"], x, 308, 348, 250, accent=ac))
        s.append(T(x + 24, 352, hd, size=19, fill=INK, weight="bold"))
        p, _ = para(x + 24, 390, bd, size=16, fill=MUTE, maxc=35, lh=25)
        s.append(p)
        s.append("</g>")
    s.append(footer("Easier tasks (PointReach … FetchReach) use 2,000 trajectories each; harder tasks (FetchPush … HandReach) use 40,000."))
    s.append(svg_close())
    return "".join(s)
slides["dataset-benchmark"] = s6()

# ---------- Slide 7: key-result ----------
def s7():
    sid = "key-result"
    s = [svg_open(), header(7, "Best rank, an order of magnitude faster", "KEY RESULT")]
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 168, 1168, 66, fill=PANEL2, accent=TEAL))
    s.append(T(82, 208, "Base Merlin already beats most baselines; Merlin-P and Merlin-NP get the highest returns on most tasks.", size=18, fill=INK, weight="bold"))
    s.append("</g>")
    # c2: average-rank card (lower = better)
    c = CMAP[sid]["chunks"][1]
    x, y, w, h = 56, 250, 570, 292
    s.append(card(c["aid"], c["kw"], x, y, w, h, accent=BLUE))
    s.append(T(x + 26, y + 42, "Average rank across 10 methods (lower is better)", size=17, fill=INK, weight="bold"))
    bx, by, bmaxw = x + 150, y + 82, 300
    # rank 1..~5 scale; Merlin-NP best
    rows = [("Merlin-NP  state", 1.7, TEAL), ("Merlin-NP  pixel", 1.25, GREEN), ("Best baseline", 4.5, GOLD)]
    rmax = 6.0
    for i, (lb, rk, ac) in enumerate(rows):
        yy = by + i * 56
        s.append(T(x + 26, yy + 18, lb, size=14, fill=MUTE))
        s.append(f'<rect x="{bx}" y="{yy}" width="{bmaxw}" height="26" rx="5" fill="{PANEL2}" stroke="{STROKE}"/>')
        s.append(f'<rect x="{bx}" y="{yy}" width="{bmaxw*rk/rmax:.0f}" height="26" rx="5" fill="{ac}"/>')
        s.append(T(bx + bmaxw * rk / rmax + 12, yy + 19, f"{rk:.2f}", size=14, fill=ac, weight="bold"))
    s.append(T(x + 26, y + 262, "Merlin-NP takes the top average rank on both input types", size=14, fill=GREEN, weight="bold"))
    s.append("</g>")
    # c3: speed card (log inference/training time)
    c = CMAP[sid]["chunks"][2]
    x3, y3, w3, h3 = 654, 250, 570, 292
    s.append(card(c["aid"], c["kw"], x3, y3, w3, h3, accent=GOLD))
    s.append(T(x3 + 26, y3 + 42, "Single denoising step → ~10× faster", size=17, fill=INK, weight="bold"))
    gx, gy, gmax = x3 + 40, y3 + 84, 360
    speed = [("Merlin (1 step)", 0.1, TEAL), ("Decision Diffuser", 1.0, RED), ("BESO", 0.9, GOLD)]
    for i, (lb, frac, ac) in enumerate(speed):
        yy = gy + i * 56
        s.append(T(gx, yy - 6, lb, size=14, fill=MUTE))
        s.append(f'<rect x="{gx}" y="{yy}" width="{gmax}" height="24" rx="5" fill="{PANEL2}" stroke="{STROKE}"/>')
        s.append(f'<rect x="{gx}" y="{yy}" width="{gmax*frac:.0f}" height="24" rx="5" fill="{ac}"/>')
    s.append(T(x3 + 26, y3 + 264, "Log inference/training time vs other diffusion RL methods", size=13, fill=MUTE))
    s.append("</g>")
    # c4: pixel note, small card bottom band
    c = CMAP[sid]["chunks"][3]
    s.append(f'<g id="{c["aid"]}"><title>{esc(c["kw"])}</title>')
    s.append(f'<rect x="820" y="556" width="404" height="120" rx="10" fill="{PANEL2}" stroke="{STROKE}"/>')
    s.append(f'<rect x="820" y="574" width="5" height="30" rx="2.5" fill="{GREEN}"/>')
    s.append(T(842, 596, "Pixels: the gap widens", size=15, fill=INK, weight="bold"))
    p, _ = para(842, 624, "With high-dimensional pixel observations, the efficiency advantage over diffusion baselines becomes even more pronounced.", size=13, fill=MUTE, maxc=44, lh=19)
    s.append(p)
    s.append("</g>")
    s.append(footer("Baselines span GCRL (GCSL, WGCSL, AM, GoFAR) and diffusion methods (Decision Diffuser, g-DQL, BESO)."))
    s.append(svg_close())
    return "".join(s)
slides["key-result"] = s7()

# ---------- Slide 8: ablation-study ----------
def s8():
    sid = "ablation-study"
    s = [svg_open(), header(8, "The evaluation horizon matters", "ABLATION STUDY")]
    s.append(text_card(0, sid, "Two hyperparameters", "The study tunes the hindsight relabeling ratio and the evaluation time horizon h — how far ahead the policy aims each step.", GX[0], row_y(0), accent=BLUE, maxc=52))
    s.append(text_card(1, sid, "Task-dependent horizon", "Easier tasks like PointReach do best with a short horizon (h=1 or 5); harder tasks need longer horizons to reach the goal.", GX[1], row_y(0), accent=TEAL, maxc=52))
    # c3: HandReach sensitivity mini-bars
    c = CMAP[sid]["chunks"][2]
    x, y, w, h = GX[0], row_y(1), 570, CH
    s.append(card(c["aid"], c["kw"], x, y, w, h, accent=GOLD))
    s.append(T(x + 26, y + 42, "HandReach is especially sensitive", size=18, fill=INK, weight="bold"))
    groups = [("h=1", 0.95, GREEN), ("h=5", 0.45, GOLD), ("h=10", 0.25, RED), ("none", 0.15, MUTE)]
    gx0, gy0, gh = x + 46, y + 78, 108
    gap = 122
    for i, (lb, sc, ac) in enumerate(groups):
        cx = gx0 + i * gap
        s.append(f'<rect x="{cx}" y="{gy0+gh-sc*gh:.0f}" width="60" height="{sc*gh:.0f}" rx="4" fill="{ac}"/>')
        s.append(T(cx + 30, gy0 + gh + 20, lb, size=13, fill=MUTE, anchor="middle"))
    s.append(f'<line x1="{gx0-6}" y1="{gy0+gh}" x2="{gx0+4*gap-40}" y2="{gy0+gh}" stroke="{STROKE}"/>')
    s.append(T(x + 26, y + 236, "Returns collapse as the horizon grows — h=1 is dramatically best", size=13, fill=MUTE))
    s.append("</g>")
    s.append(text_card(3, sid, "Robust overall", "Across tasks, conditioning on a horizon clearly beats leaving it out; trends are visualized as return heatmaps for expert and random data.", GX[1], row_y(1), accent=GREEN, maxc=52))
    s.append(footer("The hindsight relabeling ratio and the horizon are the two tuned knobs; conditioning on a horizon consistently wins."))
    s.append(svg_close())
    return "".join(s)
slides["ablation-study"] = s8()

# ---------- Slide 9: takeaway ----------
def s9():
    sid = "takeaway"
    s = [svg_open(), header(9, "Takeaway", "TAKEAWAY")]
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 178, 570, 380, accent=TEAL))
    s.append(T(82, 226, "The one line", size=18, fill=TEAL, weight="bold"))
    p, _ = para(82, 272, "Reframe goal-conditioned RL as the reverse of a diffusion process — and goal-reaching becomes remarkably simple.", size=20, fill=INK, maxc=40, lh=31)
    s.append(p)
    p2, _ = para(82, 430, "Construct trajectories that walk away from goals, learn to reverse them, and the whole problem collapses to behavior cloning.", size=16, fill=MUTE, maxc=48, lh=25)
    s.append(p2)
    s.append("</g>")
    right = [
        (1, "No value function", "Merlin reduces goal-reaching to plain behavior cloning — nothing to estimate, no instability to fight.", GREEN),
        (2, "Matches or beats SOTA", "Competitive with state-of-the-art across ten tasks, yet an order of magnitude faster than other diffusion methods.", BLUE),
        (3, "A new direction", "Diffusion in the state space is a simple, scalable, practical direction for sequential decision making.", GOLD),
    ]
    yy = 226
    for k, (ci, hd, bd, ac) in enumerate(right):
        c = CMAP[sid]["chunks"][ci]
        s.append(f'<g id="{c["aid"]}"><title>{esc(c["kw"])}</title>')
        s.append(f'<rect x="654" y="{yy-32}" width="570" height="112" rx="10" fill="{PANEL}" stroke="{STROKE}"/>')
        s.append(f'<rect x="654" y="{yy-16}" width="5" height="30" rx="2.5" fill="{ac}"/>')
        s.append(T(680, yy - 4, hd, size=18, fill=INK, weight="bold"))
        p, _ = para(680, yy + 24, bd, size=15, fill=MUTE, maxc=52, lh=22)
        s.append(p)
        s.append("</g>")
        yy += 128
    s.append(footer("Merlin — Learning to Reach Goals via Diffusion  ·  ICML 2024  ·  value-free, single-step, state-space diffusion for GCRL."))
    s.append(svg_close())
    return "".join(s)
slides["takeaway"] = s9()

# ---------- write in narration order ----------
order = ["title", "problem", "motivation", "contribution", "method",
         "dataset-benchmark", "key-result", "ablation-study", "takeaway"]
for i, sid in enumerate(order):
    fn = os.path.join(OUT, f"{i+1:02d}_{sid}.svg")
    open(fn, "w").write(slides[sid])
    print("wrote", fn)
print("done")
