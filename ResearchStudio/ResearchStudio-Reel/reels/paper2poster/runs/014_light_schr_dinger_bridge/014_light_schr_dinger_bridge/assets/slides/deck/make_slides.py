#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 014 (Light Schrodinger Bridge / LightSB, ICLR 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass resolves every
anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations only."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1B2B"; PANEL="#12293D"; PANEL2="#16324A"; STROKE="#26455F"
ACCENT="#4C9BE8"; TEAL="#34D3C0"; GOLD="#F2C14E"; RED="#F2685C"; GREEN="#48C78E"; VIOLET="#B08CE8"
TEXT="#EAF2FB"; SEC="#9DB3C8"; TER="#6E869C"; WHITE="#FFFFFF"
SANS="Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO="'DejaVu Sans Mono', Consolas, monospace"

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;"))

def T(x,y,s,size,fill=TEXT,weight="400",anchor="start",ff=SANS,ls=None,opacity=None):
    a=f' letter-spacing="{ls}"' if ls is not None else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{ff}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{a}{o}>{esc(s)}</text>')

def rect(x,y,w,h,fill=PANEL,stroke=None,rx=14,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{o}/>'

def line(x1,y1,x2,y2,stroke=STROKE,sw=1.5,dash=None,cap="round"):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'

def circle(cx,cy,r,fill=ACCENT,stroke=None,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}{o}/>'

def ellipse(cx,cy,rx,ry,fill=ACCENT,opacity=None,stroke=None,sw=1.5):
    o=f' opacity="{opacity}"' if opacity is not None else ""
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"{o}{st}/>'

def path(d,stroke=TEAL,sw=2.5,fill="none",dash=None):
    da=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}/>'

def wrap(text,maxc):
    words=text.split(); lines=[]; cur=""
    for w in words:
        if len(cur)+len(w)+1<=maxc: cur=(cur+" "+w).strip()
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def para(x,y,text,size,fill,maxc,lh,weight="400"):
    ls=wrap(text,maxc); out=[T(x,y+i*lh,l,size,fill,weight) for i,l in enumerate(ls)]
    return "".join(out), y+len(ls)*lh

def anchor(aid,kw,body):
    return f'<g id="{aid}"><title>{esc(" ".join(kw))}</title>{body}</g>'

def eyebrow(label):
    return (rect(64,52,5,26,fill=ACCENT,rx=2,sw=0)+
            T(82,72,label.upper(),15,SEC,"700",ls="2.5"))

def header(label,title,tsize=30):
    return eyebrow(label)+T(64,110,title,tsize,TEXT,"800")

def chunks(slide_id):
    return AM[slide_id]["chunks"]

def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" font-family="{SANS}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
            f'{body}</svg>')

def bar(x,y,w,val,vmax,color,label,valtxt,lblcolor=SEC,h=26):
    bw=max(2,int(w*val/vmax))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-12,y+h*0.72,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.72,valtxt,14,color,"800"))

def kpi(x,y,num,lbl,col,w=168,h=100):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.56,num,30,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.82,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=15,h=42):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# reusable native glyphs -------------------------------------------------------
def blob(cx,cy,col,label,lblcol=SEC):
    # a gaussian-like cluster of dots
    b=ellipse(cx,cy,30,22,fill=col,opacity="0.16")
    import math as _m
    pts=[(0,0),(12,-6),(-11,7),(6,10),(-8,-9),(16,5),(-16,-3),(2,-13),(9,-1),(-4,4)]
    for dx,dy in pts:
        b+=circle(cx+dx,cy+dy,3.2,fill=col)
    b+=T(cx,cy+40,label,12.5,lblcol,"700",anchor="middle")
    return b

def diffusion(x0,x1,cy,col=ACCENT):
    # three wiggly trajectories from source blob to target blob
    b=""
    for i,off in enumerate((-16,0,16)):
        mx=(x0+x1)/2
        d=(f"M {x0} {cy+off} C {x0+60} {cy+off-24} {mx-30} {cy+off+26} {mx} {cy+off} "
           f"S {x1-40} {cy+off-22} {x1} {cy+off}")
        b+=path(d,stroke=col,sw=2,dash="1 7")
    return b

def _traj_panel(x,y,w,h,vol,col,title):
    # mini panel of trajectories from left blob to right; vol in [0,1] sets wiggle amplitude
    b=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    x0=x+22; x1=x+w-22; cy=y+h/2
    b+=ellipse(x0,cy,7,16,fill=col,opacity="0.5")
    b+=ellipse(x1,cy,16,10,fill=GOLD,opacity="0.4")
    for off in (-13,0,13):
        amp=vol*20
        mx=(x0+x1)/2
        d=(f"M {x0} {cy+off*0.4} Q {mx} {cy+off-amp} {x1} {cy+off} ")
        b+=path(d,stroke=col,sw=1.8)
    b+=T(x+w/2,y+h+16,title,11.5,SEC,"700",anchor="middle")
    return b

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Skoltech  ·  AIRI",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,162,"Light Schrödinger Bridge",44,WHITE,"800")
    b+=T(64,206,"A simple, fast, simulation-free Schrödinger Bridge solver",22,ACCENT,"700")
    b+=T(64,242,"Alexander Korotin   ·   Nikita Gushchin   ·   Evgeny Burnaev      —   Skoltech & AIRI",15.5,SEC,"500")
    cw=560; chh=120; gap=32; x0=64; x1=x0+cw+gap; cy0=290; cy1=cy0+chh+22
    data=[
        (ch[0],ACCENT,x0,cy0,"Bridges are useful, but heavy","A Schrödinger Bridge links two distributions by diffusion, yet solvers stack neural nets, use adversarial min-max training, and take GPU-hours."),
        (ch[1],TEAL,x1,cy0,"LightSB","A lightweight Schrödinger Bridge solver, meant to be the simple go-to baseline the field has lacked."),
        (ch[2],GOLD,x0,cy1,"One simple objective","Parameterize the Schrödinger potential as a Gaussian mixture and read its log as an energy; the problem becomes a single non-minimax objective with closed forms."),
        (ch[3],GREEN,x1,cy1,"Minutes on a CPU","Solves bridges in moderate dimensions in minutes on a CPU, needs no painful tuning, and is provably a universal approximator."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,13.5,SEC,66,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,616,1216,616,STROKE,1)
    b+=T(64,650,"arXiv:2310.01174",14,ACCENT,"700")
    b+=T(300,650,"A Schrödinger Bridge solver does not have to be heavy.",14,SEC,"600")
    b+=T(1216,650,"github.com/ngushchin/LightSB",13.5,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","No simple baseline for Schrödinger Bridges")
    # c1 left tall: what the SB problem is + diffusion glyph
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"What the Schrödinger Bridge asks",18,TEXT,"800")+
        para(92,238,"Find the diffusion process carrying one distribution to another that stays as close as possible to a reference Wiener process.",14.5,SEC,50,22)[0]+
        rect(92,336,504,150,fill="#0E2334",stroke=STROKE,rx=10)+
        blob(150,412,ACCENT,"source p0")+
        blob(538,412,GOLD,"target p1")+
        diffusion(190,498,412,col=TEAL)+
        T(344,356,"closest to a Wiener reference",12,TER,"700",anchor="middle")+
        T(92,522,"The dynamic form of entropic optimal transport.",13.5,TEAL,"700"))
    # right: dynamic EOT / apps, the trouble, the gap
    fx=656; fw=560
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,120,fill=TEAL,rx=6,sw=0)+
        T(fx+28,196,"Dynamic entropic optimal transport",16.5,TEAL,"800")+
        para(fx+28,224,"It underpins real applications across science and vision.",14,SEC,70,20)[0]+
        chip(fx+28,242,"single-cell biology   ·   image translation",TEAL,w=504,h=30))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,290,fw,132,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,290,6,132,fill=RED,rx=6,sw=0)+
        T(fx+28,328,"The trouble: solvers are heavy",16,RED,"800")+
        para(fx+28,358,"Almost all existing solvers stack several large neural networks and require complex, often adversarial optimization.",14.5,TEXT,58,22)[0]+
        T(fx+28,414,"several networks  +  min-max training  =  slow, fragile",13.5,RED,"800",ff=MONO))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,434,fw,116,fill=PANEL,stroke=STROKE)+
        rect(fx,434,6,116,fill=GOLD,rx=6,sw=0)+
        T(fx+28,472,"A missing baseline",16,GOLD,"800")+
        para(fx+28,502,"The field has no go-to method the way k-means is for clustering or Sinkhorn is for discrete OT.",14.5,SEC,58,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Heavy machinery for a modest goal")
    # c1 left: the researcher's simple wish
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,200,"A very common wish",18,TEAL,"800")+
        para(92,234,"A researcher simply wants an entropic optimal transport or Schrödinger Bridge between two moderate-dimensional datasets.",14.5,SEC,50,22)[0]+
        rect(92,326,504,90,fill=PANEL2,stroke=STROKE,rx=10)+
        blob(160,371,ACCENT,"dataset A")+
        T(344,376,"want the plan",12.5,GOLD,"700",anchor="middle")+T(344,396,"→",22,GOLD,"800",anchor="middle")+
        blob(528,371,GREEN,"dataset B")+
        rect(92,436,504,96,fill="#0F2E2B",stroke=TEAL,rx=12,sw=1.5)+
        T(112,466,"Often only the endpoints matter",13.5,TEAL,"800")+
        para(112,490,"In many settings the user cares only about the conditional plan pi(x1 | x0).",13.5,SEC,60,20)[0])
    # right: today's options, the cost, the mismatch
    rx=656; rw=560
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,124,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,124,fill=ACCENT,rx=6,sw=0)+
        T(rx+28,196,"Today's only options",16,ACCENT,"800")+
        para(rx+28,224,"Adopt a heavy solver: iterative proportional fitting, min-max optimization, or simulating the process each step.",13.5,SEC,64,21)[0]+
        T(rx+28,272,"IPF   ·   min-max   ·   simulate the SDE each step",13,ACCENT,"700",ff=MONO))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,294,rw,120,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,294,6,120,fill=GOLD,rx=6,sw=0)+
        T(rx+28,332,"They are costly",16,GOLD,"800")+
        para(rx+28,362,"Careful neural-network design, hours on GPUs, and sensitivity to many hyperparameters.",14.5,TEXT,58,22)[0]+
        T(rx+28,404,"hours of GPU   ·   fragile hyperparameters",13,GOLD,"700",ff=MONO))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,426,rw,124,fill=PANEL,stroke=STROKE)+
        rect(rx,426,6,124,fill=GREEN,rx=6,sw=0)+
        T(rx+28,464,"The mismatch LightSB closes",16,GREEN,"800")+
        para(rx+28,494,"Heavy machinery for a modest goal. LightSB returns the conditional plan directly and cheaply.",14.5,SEC,58,22)[0])
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One light solver, three results")
    cards=[
        (ch[0],ACCENT,"1","LightSB, a light solver","Combine two ideas: parameterize the Schrödinger potential with sum-exp quadratic (Gaussian mixture) functions, and view the log-potential as an energy function."),
        (ch[1],TEAL,"2","One clean objective","Together they give a single, non-minimax, simulation-free objective, with closed-form expressions for both the plan and the drift."),
        (ch[2],GOLD,"3","Universal approximator","Prove the Gaussian-mixture solver is a universal approximator of Schrödinger Bridges, the first such result."),
        (ch[3],GREEN,"4","Generalization bound","Analyze the generalization error and show it converges at the standard parametric rate as sample size grows."),
    ]
    cw=272; gap=24; x0=64; cy=176; chh=380
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+70,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+80,num,28,col,"800",anchor="middle"))
        yy=cy+140
        for j,ln in enumerate(wrap(ti,16)):
            body+=T(x+24,yy+j*25,ln,17.5,TEXT,"800")
        yy+=25*len(wrap(ti,16))+14
        body+=para(x+24,yy,tx,13.5,SEC,29,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,590,"Fast and simple, yet backed by a universal-approximation guarantee.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Minimize a KL you can actually compute")
    lx=64; lw=568
    # c1 objective + parameterize the potential
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,196,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,196,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Start from a KL objective",16.5,ACCENT,"800")+
        para(lx+28,226,"Minimize the KL between the true entropic OT plan and a parameterized plan. We cannot see the true plan, so parameterize only the adjusted potential.",13.5,SEC,60,20)[0]+
        eqbox(lx+28,306,lw-56,"KL( pi* || pi_theta )  ->  min over theta",15))
    # c2 Gaussian mixture potential -> closed form
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,370,lw,180,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,370,6,180,fill=TEAL,rx=6,sw=0)+
        T(lx+28,408,"Pick a Gaussian mixture",16,TEAL,"800")+
        para(lx+28,438,"Choose an unnormalized Gaussian mixture for the potential. Then the conditional plan and its normalization become closed-form.",13.5,SEC,60,20)[0]+
        eqbox(lx+28,506,lw-56,"v_theta(x1) = sum_k a_k N(x1 | r_k, eps S_k)",14))
    # c3 Prop 3.1 loss = difference of two expectations
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,196,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,196,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Proposition 3.1: a simple loss",16.5,GOLD,"800")+
        para(rxx+28,226,"The KL becomes a difference of two expectations: log-normalization under the source minus log-potential under the target. Estimate by Monte Carlo, optimize with plain SGD.",13.5,SEC,58,20)[0]+
        eqbox(rxx+28,306,rw-56,"L = E_p0[ log c_theta ] - E_p1[ log v_theta ]",14))
    # c4 no min-max, closed-form drift
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,370,rw,180,fill=PANEL,stroke=STROKE)+
        rect(rxx,370,6,180,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,408,"No min-max, no simulation",16,GREEN,"800")+
        para(rxx+28,438,"No adversarial game, no iterative proportional fitting, no trajectory simulation during training. The trained potential yields a closed-form drift.",13.5,SEC,58,20)[0]+
        chip(rxx+28,506,"closed-form plan  +  closed-form drift g_theta(x, t)",GREEN,w=rw-56,h=30))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Four testbeds of rising difficulty")
    cw=560; chh=176; x0=64; x1=656; y0=158; y1=y0+chh+18
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(x0,y0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,y0,6,chh,fill=ACCENT,rx=6,sw=0)+
        T(x0+28,y0+40,"1 · Gaussian → Swiss-roll toy",17.5,ACCENT,"800")+
        para(x0+28,y0+72,"A two-dimensional toy that visualizes how the noise level epsilon shapes the bridge trajectories.",14,SEC,58,21)[0]+
        _traj_panel(x0+28,y0+112,150,44,0.15,ACCENT,"")+
        chip(x0+196,y0+118,"2-D  ·  visualizes epsilon",ACCENT,w=336,h=34))
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x1,y0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,y0,6,chh,fill=TEAL,rx=6,sw=0)+
        T(x1+28,y0+40,"2 · High-dim EOT benchmark",17.5,TEAL,"800")+
        para(x1+28,y0+72,"A recent benchmark with known ground-truth plans, so accuracy can be measured exactly.",14,SEC,58,21)[0]+
        chip(x1+28,y0+118,"dims 2 → 128    ·    epsilon = 0.1, 1, 10",TEAL,w=504,h=34))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0,y1,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,y1,6,chh,fill=GOLD,rx=6,sw=0)+
        T(x0+28,y1+40,"3 · MSCI single-cell (Kaggle)",17.5,GOLD,"800")+
        para(x0+28,y1+72,"Cells from four human donors at four time points, projected by PCA to increasing dimension.",14,SEC,58,21)[0]+
        chip(x0+28,y1+118,"4 donors · days 2/3/4/7    ·    PCA 50 / 100 / 1000",GOLD,w=504,h=34))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x1,y1,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,y1,6,chh,fill=VIOLET,rx=6,sw=0)+
        T(x1+28,y1+40,"4 · FFHQ face translation",17.5,VIOLET,"800")+
        para(x1+28,y1+72,"Unpaired image translation on FFHQ faces, run in the latent space of a pretrained ALAE autoencoder.",14,SEC,58,21)[0]+
        chip(x1+28,y1+118,"512-dim ALAE latent  ·  unpaired faces",VIOLET,w=504,h=34))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Sharper plans, on a CPU, in minutes")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,48,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,48,fill=GREEN,rx=6,sw=0)+
        T(92,180,"Across the board LightSB delivers both accuracy and speed, without a GPU.",16.5,TEXT,"700"))
    # c2 EOT benchmark error bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,212,560,266,fill=PANEL,stroke=STROKE)+
        rect(64,212,6,266,fill=TEAL,rx=6,sw=0)+
        T(92,248,"EOT benchmark error  ·  lower is better",16,TEAL,"800")+
        T(92,272,"conditional Bures-Wasserstein UVP (%)",12.5,TER,"600")+
        bar(300,292,236,0.3,18,GREEN,"LightSB","≈0.03–0.62%",h=30)+
        bar(300,340,236,18,18,RED,"best baseline","1.04–18.05%",h=30)+
        rect(92,396,504,64,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        para(112,424,"Error well under one percent, often a few hundredths, where the best prior sits between about one and eighteen.",13.5,SEC,64,19)[0])
    # c3 MSCI speed (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,212,560,266,fill=PANEL,stroke=STROKE)+
        rect(656,212,6,266,fill=GOLD,rx=6,sw=0)+
        T(684,248,"MSCI single-cell  ·  same accuracy, far faster",15.5,GOLD,"800")+
        kpi(684,272,"1–2.5 min","LightSB, 4 CPU cores",GREEN,w=250,h=100)+
        kpi(962,272,"10 min – 1 hr+","GPU baselines, V100",RED,w=250,h=100)+
        rect(684,388,528,72,fill=PANEL2,stroke=STROKE,rx=10)+
        para(704,414,"Energy distance comparable to strong GPU solvers, but trained on just four CPU cores.",13.5,SEC,66,20)[0])
    # c4 FFHQ strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,492,6,116,fill=VIOLET,rx=6,sw=0)+
        T(92,526,"FFHQ face translation",16,VIOLET,"800")+
        para(92,556,"Realistic male-to-female and child-to-adult translation in the 512-dimensional ALAE latent space, converging in under a minute on CPU.",14.5,SEC,66,22)[0]+
        chip(760,520,"male ↔ female   ·   child ↔ adult",VIOLET,w=430,h=32)+
        chip(760,560,"512-dim latent   ·   < 1 min on CPU",VIOLET,w=430,h=32))
    b+=T(64,646,"Accurate where it matters, cheap where it counts.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Epsilon controls the bridge's noise")
    # c1 setup strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"Map a 2-D Gaussian to a Swiss roll while sweeping the noise level epsilon across three values.",16,TEXT,"600"))
    # c2 small eps panel (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,196,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,196,fill=TEAL,rx=6,sw=0)+
        T(92,278,"Small epsilon  ·  nearly deterministic",15.5,TEAL,"800")+
        _traj_panel(92,300,220,84,0.08,TEAL,"eps = 2e-3  (straight)")+
        para(340,320,"The learned process is almost deterministic; its trajectories are nearly straight lines.",13.5,SEC,32,21)[0])
    # c3 large eps panel (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,196,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,196,fill=GOLD,rx=6,sw=0)+
        T(684,278,"Large epsilon  ·  volatile, spread out",15.5,GOLD,"800")+
        _traj_panel(684,300,220,84,0.85,GOLD,"eps = 1e-1  (volatile)")+
        para(932,320,"Trajectories grow volatile and the endpoint conditionals spread; epsilon sets the stochasticity.",13.5,SEC,32,21)[0])
    # c4 inductive-bias takeaway
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,452,1152,98,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,452,6,98,fill=GREEN,rx=6,sw=0)+
        T(92,488,"Where LightSB wins most",16,GREEN,"800")+
        para(92,516,"Gains are largest when the target aligns with its sum-exp Gaussian-mixture inductive bias, while accuracy holds across dimensions 2–128 and noise levels 0.1–10.",14.5,TEXT,110,22)[0])
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    # c1 CPU speed strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,168,1152,92,fill=PANEL,stroke=STROKE)+
        rect(64,168,6,92,fill=GREEN,rx=6,sw=0)+
        T(92,204,"Image translation, 512-dim latent",16,GREEN,"800")+
        kpi(700,180,"< 1 min","4 CPU cores, no GPU",GREEN,w=230,h=68)+
        para(92,232,"Converges in under a minute on four CPU cores, with no GPU involved at all.",14.5,SEC,74,20)[0])
    # c2 single-cell CPU vs GPU
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,276,560,274,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,276,6,274,fill=TEAL,rx=6,sw=0)+
        T(92,314,"Single-cell, hardest 1000-dim setting",16,TEAL,"800")+
        kpi(92,334,"1.27","energy dist · LightSB",GREEN,w=250,h=96)+
        kpi(370,334,"1.32","energy dist · minimax GPU",SEC,w=250,h=96)+
        rect(92,442,528,44,fill=PANEL2,stroke=STROKE,rx=8)+
        T(112,470,"146 s on CPU    vs    71 min on a V100",14.5,TEAL,"800",ff=MONO)+
        para(92,516,"Matches a minimax GPU solver at a fraction of the compute.",13.5,SEC,72,20)[0])
    # c3 EOT error
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,276,560,132,fill=PANEL,stroke=STROKE)+
        rect(656,276,6,132,fill=GOLD,rx=6,sw=0)+
        T(684,314,"EOT benchmark error",16,GOLD,"800")+
        kpi(684,330,"0.03%","LightSB, best case",GREEN,w=250,h=64)+
        kpi(962,330,"1–18%","best baseline range",RED,w=250,h=64))
    # c4 guarantee
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,424,560,126,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,424,6,126,fill=GOLD,rx=6,sw=0)+
        T(684,462,"With a theoretical guarantee",16,GOLD,"800")+
        para(684,492,"A universal approximator of Schrödinger Bridges, with generalization error vanishing at the standard parametric rate.",14,TEXT,58,22)[0])
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","A light solver the field was missing")
    cards=[
        (ch[0],ACCENT,"Bridges need not be heavy","A Schrödinger Bridge solver does not have to stack networks or run for GPU-hours."),
        (ch[1],TEAL,"A Gaussian mixture and one objective","Parameterize the transport potential as a Gaussian mixture and optimize a single, straightforward objective, no adversarial training or process simulation."),
        (ch[2],GREEN,"Matches heavy GPU solvers","It matches or outperforms much heavier GPU solvers, carries a universal-approximation guarantee, and is easy to use."),
        (ch[3],GOLD,"The simple, reliable baseline","LightSB is positioned to be the go-to Schrödinger Bridge baseline the field has been missing."),
    ]
    y=170; chh=98; gap=14
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,chh,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,chh,fill=col,rx=6,sw=0)+
              circle(112,y+chh/2,10,fill=col)+
              T(150,y+40,ti,18.5,TEXT,"800"))
        body+=para(150,y+70,tx,14.5,SEC,96,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=chh+gap
    b+=line(64,y+6,1216,y+6,STROKE,1)
    b+=T(64,y+38,"Light Schrödinger Bridge  ·  ICLR 2024  ·  Korotin, Gushchin & Burnaev",15,TEXT,"700")
    b+=T(1216,y+38,"github.com/ngushchin/LightSB",13.5,TEAL,"700",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
