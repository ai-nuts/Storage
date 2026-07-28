#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 096.
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1B2B"; PANEL="#12293D"; PANEL2="#16324A"; STROKE="#26455F"
ACCENT="#4C9BE8"; TEAL="#34D3C0"; GOLD="#F2C14E"; RED="#F2685C"; GREEN="#48C78E"
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

def header(label,title,tsize=30,tw=None):
    out=eyebrow(label)
    if tw is None:
        out+=T(64,110,title,tsize,TEXT,"800")
    else:
        for i,l in enumerate(tw):
            out+=T(64,110+i*38,l,tsize,TEXT,"800")
    return out

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

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NEURIPS 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Purdue University",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,168,"Truly Scale-Equivariant Deep Nets",44,WHITE,"800")
    b+=T(64,220,"with Fourier Layers",44,ACCENT,"800")
    b+=T(64,262,"Md Ashiqur Rahman   ·   Raymond A. Yeh      —   Dept. of Computer Science, Purdue University",17,SEC,"500")
    # three concept cards = anchors
    cy=310; cw=368; gap=20; cx=64
    data=[
        (ACCENT,"Scale-Equivariance","Resize an object and the network's features transform consistently while its label stays the same."),
        (RED,"The gap","Prior scale-equivariant CNNs are only approximately equivariant: derived in the continuous domain, blind to anti-aliasing."),
        (TEAL,"This work","Formulate down-scaling in the discrete domain with anti-aliasing, via Fourier layers → absolute zero equivariance error."),
    ]
    for i,(col,ti,tx) in enumerate(data):
        x=cx+i*(cw+gap)
        body=(rect(x,cy,cw,196,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+44,7,fill=col)+
              T(x+48,cy+50,ti,20,TEXT,"800"))
        pp,_=para(x+24,cy+92,tx,15,SEC,42,25)
        body+=pp
        b+=anchor(ch[i]["aid"],ch[i]["kw"],body)
    b+=line(64,548,1216,548,STROKE,1)
    b+=T(64,584,"Zero equivariance error — in theory and in practice — while staying competitive on classification accuracy.",17,TEXT,"600")
    b+=T(64,632,"arXiv:2311.02922",14,ACCENT,"700")
    b+=T(300,632,"github.com/ashiq24/Scale_Equivarinat_Fourier_Layer",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Approximately equivariant, not truly so")
    # c1 definition card (left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,404,6,fill=ACCENT,rx=6,sw=0)+
        T(92,206,"What is scale-equivariance?",19,TEXT,"800")+
        para(92,246,"When an object in an image is resized, the network's features should transform consistently — and its predicted label should not change.",16,SEC,40,26)[0]+
        # mini glyph: small vs large digit -> same label
        rect(92,352,120,120,fill=PANEL2,stroke=STROKE,rx=10)+T(152,422,"8",54,ACCENT,"800",anchor="middle")+
        T(230,392,"resize",13,TER,"600")+line(224,404,320,404,ACCENT,2,dash="4 4")+T(320,410,"→",20,ACCENT,"800")+
        rect(336,376,72,72,fill=PANEL2,stroke=STROKE,rx=10)+T(372,424,"8",32,ACCENT,"800",anchor="middle")+
        T(92,508,"features transform consistently  ·  label stays “8”",14,TEAL,"700"))
    # right column: how prior methods work -> fail (c2,c3,c4 vertical flow)
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,108,fill=PANEL,stroke=STROKE)+
        T(fx+28,196,"1  ·  How prior scale-equivariant CNNs work",17,ACCENT,"800")+
        para(fx+28,228,"They share weights and resize the same kernel across scales — one kernel, re-scaled for every resolution.",15,SEC,72,24)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,278,fw,108,fill=PANEL,stroke=STROKE)+
        T(fx+28,316,"2  ·  Where it breaks",17,GOLD,"800")+
        para(fx+28,348,"The resizing is derived in the continuous domain, then discretized when it is actually implemented in code.",15,SEC,72,24)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,398,fw,152,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,398,6,152,fill=RED,rx=6,sw=0)+
        T(fx+28,438,"3  ·  The cost: a non-negligible equivariance error",17,RED,"800")+
        para(fx+28,470,"That discretization step injects a residual error, so the networks are only approximately scale-equivariant — never truly so.",15,TEXT,72,24)[0]+
        T(fx+28,536,"Equivariance error  >  0",16,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Down-scaling is a signal-processing problem")
    # c1 headline card full width
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,84,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,84,fill=TEAL,rx=6,sw=0)+
        T(92,196,"Key insight",15,TEAL,"800",ls="1.5")+
        T(92,224,"Down-scaling a discrete signal is fundamentally a signal-processing operation — not a continuous re-parameterization.",17,TEXT,"600"))
    # c2 Nyquist diagram (left)
    dx=64; dw=560
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(dx,258,dw,292,fill=PANEL,stroke=STROKE)+
        T(dx+28,296,"Nyquist: filter before you subsample",17,TEXT,"800")+
        # spectrum axes
        line(dx+40,470,dx+520,470,SEC,2)+T(dx+520,492,"freq",12,TER,"600",anchor="end")+
        # full spectrum (light) with high-freq region
        _spectrum(dx+40,470)+
        # cutoff line
        line(dx+300,330,dx+300,470,GOLD,2,dash="5 4")+T(dx+300,322,"Nyquist limit",12,GOLD,"700",anchor="middle")+
        rect(dx+300,332,220,138,fill=RED,rx=0,sw=0,opacity="0.10")+
        T(dx+410,356,"zeroed by",12,RED,"700",anchor="middle")+T(dx+410,372,"low-pass",12,RED,"700",anchor="middle")+
        para(dx+28,516,"Skip the filter and high frequencies fold into low ones — aliasing (the wagon-wheel effect).",13,SEC,60,18)[0])
    # c3 prior gap + c4 fix (right stacked)
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,258,rw,138,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(rx,258,6,138,fill=RED,rx=6,sw=0)+
        T(rx+28,296,"Why prior methods have no filter",16,RED,"800")+
        para(rx+28,328,"Formulated in the continuous domain, prior scale-equivariant networks simply have no place to put an anti-aliasing filter.",14.5,TEXT,60,23)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,412,rw,138,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rx,412,6,138,fill=TEAL,rx=6,sw=0)+
        T(rx+28,450,"The fix",16,TEAL,"800")+
        para(rx+28,482,"To be truly scale-equivariant, formulate down-scaling directly in the discrete domain, with anti-aliasing built in from the start.",14.5,TEXT,60,23)[0])
    return svg(b)

def _spectrum(x0,y0):
    # a triangular-ish spectrum envelope
    pts=[]
    import math
    for i in range(0,481,10):
        v=math.exp(-((i-0)/230.0)**2)  # decaying from left
        pts.append((x0+i, y0-8-int(120*v)))
    poly=" ".join(f"{px},{py}" for px,py in pts)
    poly=f"{x0},{y0} "+poly+f" {x0+480},{y0}"
    return f'<polygon points="{poly}" fill="{ACCENT}" opacity="0.35"/><polyline points="{" ".join(f"{px},{py}" for px,py in pts)}" fill="none" stroke="{ACCENT}" stroke-width="2"/>'

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,66,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,66,fill=ACCENT,rx=6,sw=0)+
        T(92,199,"A new formulation, a new family of layers, and experiments that prove exact scale-equivariance at no accuracy cost.",17,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","Discrete-domain down-scaling","Define down-scaling as ideal downsampling — an ideal low-pass (anti-aliasing) filter, then subsampling — directly in the discrete domain."),
        (ch[2],TEAL,"2","A family of Fourier layers","Rethink every component — convolution, non-linearity, pooling — as Fourier layers obeying one simple frequency-dependency rule."),
        (ch[3],GOLD,"3","Zero error, competitive accuracy","On MNIST-scale and STL-10: absolute zero end-to-end equivariance error, competitive accuracy, and better data efficiency."),
    ]
    cw=368; gap=24; x0=64; cy=250
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,300,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2)+
              T(x+50,cy+76,num,30,col,"800",anchor="middle")+
              T(x+28,cy+140,ti,19,TEXT,"800") if False else "")
        body=(rect(x,cy,cw,300,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+68,27,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+78,num,30,col,"800",anchor="middle"))
        yy=cy+130
        for j,ln in enumerate(wrap(ti,22)):
            body+=T(x+28,yy+j*28,ln,19,TEXT,"800")
        yy+=28*len(wrap(ti,22))+8
        body+=para(x+28,yy,tx,15,SEC,40,25)[0]
        b+=anchor(c["aid"],c["kw"],body)
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","One frequency rule, every layer redesigned")
    # 2x2 grid
    gx=[64,648]; gy=[158,360]; cw=568; chh=190
    # c1 ideal downsampling
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[0],6,chh,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,gy[0]+38,"Ideal downsampling",17,ACCENT,"800")+
        para(gx[0]+28,gy[0]+68,"First an ideal low-pass filter zeros every frequency above the new Nyquist limit, then subsample.",14.5,SEC,58,22)[0]+
        rect(gx[0]+28,gy[0]+124,cw-56,44,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[0]+cw/2,gy[0]+152,"D_R(x) = Sub_R( h * x )",18,TEXT,"800",anchor="middle",ff=MONO))
    # c2 Claim 1
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],gy[0],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[0],6,chh,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,gy[0]+38,"Claim 1  ·  the equivariance condition",17,TEAL,"800")+
        para(gx[1]+28,gy[0]+68,"Truly scale-equivariant iff every output frequency depends only on equal-or-lower input frequencies.",14.5,SEC,58,22)[0]+
        rect(gx[1]+28,gy[0]+124,cw-56,44,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[0]+152,"Y[k] = G_k( X[-k : k] )   for all k",17,TEXT,"800",anchor="middle",ff=MONO))
    # c3 redesigned modules
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[0],gy[1],6,chh,fill=GOLD,rx=6,sw=0)+
        T(gx[0]+28,gy[1]+38,"Every module obeys the rule",17,GOLD,"800")+
        _chip(gx[0]+28,gy[1]+64,"Spatially-local Fourier conv",ACCENT)+
        _chip(gx[0]+28,gy[1]+110,"Frequency-band ReLU non-linearity",TEAL)+
        _chip(gx[0]+28,gy[1]+156,"Fourier pooling (same dependency)",GOLD))
    # c4 classifier + loss
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],gy[1],cw,chh,fill=PANEL,stroke=STROKE)+
        rect(gx[1],gy[1],6,chh,fill=RED,rx=6,sw=0)+
        T(gx[1]+28,gy[1]+38,"Per-scale classifier + consistency loss",16.5,RED,"800")+
        para(gx[1]+28,gy[1]+68,"One MLP shared across scales via Fourier padding; a hinge loss penalizes a high-res prediction that is worse than its low-res one.",14,SEC,60,21)[0]+
        rect(gx[1]+28,gy[1]+132,cw-56,40,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gy[1]+158,"sum  max( L(y[k]) - L(y[k-1]), 0 )",15,TEXT,"800",anchor="middle",ff=MONO))
    return svg(b)

def _chip(x,y,text,col):
    return (rect(x,y,512,34,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+17,5,fill=col)+
            T(x+34,y+23,text,14.5,TEXT,"600"))

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Two standard scale benchmarks")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,60,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,60,fill=ACCENT,rx=6,sw=0)+
        T(92,195,"Following prior work, the model is evaluated on two benchmarks built by randomly downsampling images across scales.",16.5,TEXT,"600"))
    # two dataset cards
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,282,"MNIST-scale",20,ACCENT,"800")+
        para(92,316,"Randomly downsampled MNIST digits, with every resolution equally represented.",14.5,SEC,58,22)[0]+
        _rangebadge(92,352,"8×8","28×28",ACCENT))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,150,fill=TEAL,rx=6,sw=0)+
        T(684,282,"STL10-scale",20,TEAL,"800")+
        para(684,316,"The same construction applied to natural color images.",14.5,SEC,58,22)[0]+
        _rangebadge(684,352,"48","97",TEAL))
    # c4 evaluation settings
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,410,1152,140,fill=PANEL,stroke=STROKE)+
        rect(64,410,6,140,fill=GOLD,rx=6,sw=0)+
        T(92,448,"Four evaluation settings",17,GOLD,"800")+
        _evchip(92,470,"Ideal downsampling","theory = practice",ACCENT)+
        _evchip(376,470,"Unseen scales","generalization",TEAL)+
        _evchip(660,470,"Data efficiency","5k · 2.5k · 1k samples",GOLD)+
        _evchip(944,470,"Non-ideal downsampling","imperfect filter",RED))
    return svg(b)

def _rangebadge(x,y,lo,hi,col):
    return (rect(x,y,150,26,fill=PANEL2,stroke=STROKE,rx=13)+
            T(x+16,y+18,lo,14,col,"800")+T(x+58,y+18,"→",14,TER,"700")+T(x+82,y+18,hi,14,col,"800")+
            T(x+170,y+18,"resolutions",13,TER,"600"))

def _evchip(x,y,ti,sub,col):
    return (rect(x,y,260,58,fill=PANEL2,stroke=STROKE,rx=10)+
            rect(x,y,5,58,fill=col,rx=2,sw=0)+
            T(x+20,y+26,ti,14.5,TEXT,"800")+T(x+20,y+46,sub,12.5,SEC,"600"))

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Best accuracy, zero equivariance error")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"Best on every metric — and, by construction, an absolute zero equivariance error.",16.5,TEXT,"700"))
    # c2 MNIST card: KPI tiles + equi-err bars
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,336,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,336,fill=ACCENT,rx=6,sw=0)+
        T(92,250,"MNIST-scale  ·  ideal downsampling",16.5,ACCENT,"800")+
        _kpi(92,268,"98.9%","accuracy",GREEN)+_kpi(272,268,"97.0%","scale-consistency",GREEN)+_kpi(452,268,"0.00","equi-error",TEAL)+
        T(92,388,"End-to-end equivariance error (lower is better)",13.5,SEC,"700")+
        bar(240,404,320,0.00,0.50,TEAL,"Ours","0.00",h=22)+
        bar(240,436,320,0.28,0.50,GOLD,"Fourier CNN","0.28",h=22)+
        bar(240,468,320,0.44,0.50,RED,"DISCO","0.44",h=22)+
        T(92,522,"Ours drives the residual error to exactly zero.",13.5,TEAL,"700"))
    # c3 STL10 bars
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,336,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,336,fill=TEAL,rx=6,sw=0)+
        T(684,250,"STL10-scale  ·  natural images",16.5,TEAL,"800")+
        T(684,282,"Accuracy (higher is better)",13.5,SEC,"700")+
        bar(860,300,300,73.3,80,GREEN,"Ours","73.3%",h=26)+
        bar(860,340,300,58.4,80,GOLD,"Fourier CNN","58.4%",h=26)+
        bar(860,380,300,56.0,80,SEC,"Wide ResNet","56.0%",h=26)+
        rect(684,424,532,44,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(700,452,"≈ +15 points over the strongest baseline · equi-error 0.00",15,TEAL,"800")+
        T(684,506,"The gain is largest on the harder natural-image benchmark.",13.5,SEC,"600"))
    # c4 graceful degradation strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,564,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,564,6,116,fill=GOLD,rx=6,sw=0)+
        T(92,598,"Degrades gracefully",16,GOLD,"800")+
        _evchip(92,616,"Non-ideal downsampling","still best: 98.8% acc · err 0.05",ACCENT)+
        _evchip(452,616,"Low-data regime","most data-efficient of all methods",TEAL)+
        _evchip(812,616,"1k training samples","96.06% vs DISCO 94.57%",GOLD))
    return svg(b)

def _kpi(x,y,num,lbl,col):
    return (rect(x,y,168,100,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+84,y+56,num,32,col,"800",anchor="middle")+
            T(x+84,y+82,lbl,12.5,SEC,"600",anchor="middle"))

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","The consistency loss earns its place")
    # c1 setup + grouped bar chart (left)
    cx=64; cw=680
    body=(rect(cx,158,cw,392,fill=PANEL,stroke=STROKE)+
          rect(cx,158,6,392,fill=ACCENT,rx=6,sw=0)+
          T(cx+28,196,"Scale-consistency:  with vs. without consistency loss",16,TEXT,"800"))
    # grouped bars for 5k/2.5k/1k
    groups=[("5000",0.9150,0.9296),("2500",0.8633,0.8906),("1000",0.8144,0.8183)]
    baseY=490; maxh=210; vmin=0.78; vmax=0.95
    gxs=[cx+120,cx+340,cx+560]
    for (lbl,wo,wi),gxc in zip(groups,gxs):
        def hh(v): return int(maxh*(v-vmin)/(vmax-vmin))
        h1=hh(wo); h2=hh(wi)
        body+=rect(gxc-56,baseY-h1,48,h1,fill=SEC,rx=4,sw=0)+T(gxc-32,baseY-h1-8,f"{wo*100:.1f}",12,SEC,"700",anchor="middle")
        body+=rect(gxc+8,baseY-h2,48,h2,fill=GREEN,rx=4,sw=0)+T(gxc+32,baseY-h2-8,f"{wi*100:.1f}",12,GREEN,"800",anchor="middle")
        body+=T(gxc,baseY+22,f"{lbl} samples",13,SEC,"700",anchor="middle")
    body+=line(cx+40,baseY,cx+640,baseY,STROKE,1.5)
    # legend
    body+=rect(cx+28,224,14,14,fill=SEC,rx=3,sw=0)+T(cx+50,236,"without consistency",13,SEC,"600")
    body+=rect(cx+220,224,14,14,fill=GREEN,rx=3,sw=0)+T(cx+242,236,"with consistency",13,GREEN,"700")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],body)
    # c2 highlight 5k
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(764,158,452,120,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(764,158,6,120,fill=TEAL,rx=6,sw=0)+
        T(792,194,"At 5,000 samples",15,TEAL,"800")+
        T(792,244,"91.5%  →  93.0%",30,TEXT,"800")+
        T(792,268,"scale-consistency",13,SEC,"600"))
    # c3 confirms
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(764,294,452,120,fill=PANEL,stroke=STROKE)+
        rect(764,294,6,120,fill=GREEN,rx=6,sw=0)+
        T(792,330,"The loss does real work",15,GREEN,"800")+
        para(792,362,"It improves both accuracy and scale-consistency at every training-set size.",14,SEC,44,22)[0])
    # c4 freq-domain note
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(764,430,452,120,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(764,430,6,120,fill=GOLD,rx=6,sw=0)+
        T(792,466,"A design lesson",15,GOLD,"800")+
        para(792,498,"A frequency-domain non-linearity is equivariant but hurt accuracy — hence the spatial-domain non-linearity.",14,SEC,44,22)[0])
    return svg(b)

# ---------- SLIDE 9: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Get the signal processing right")
    cards=[
        (ch[0],ACCENT,"Reframe the problem","Treat scale-equivariance as a signal-processing problem — down-scaling is ideal, anti-aliased downsampling of a discrete signal."),
        (ch[1],TEAL,"Provably zero error","Require every output frequency to depend only on equal-or-lower input frequencies, and Fourier layers become exactly scale-equivariant — zero error, not a small residual."),
        (ch[2],GREEN,"No practical cost","The guarantee is free: the model matches or beats prior scale-equivariant CNNs on accuracy and is more data-efficient, especially on natural images."),
    ]
    y=170
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,88,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=136
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"Truly Scale-Equivariant Deep Nets with Fourier Layers",16,TEXT,"700")
    b+=T(64,660,"NeurIPS 2023  ·  arXiv:2311.02922  ·  github.com/ashiq24/Scale_Equivarinat_Fourier_Layer",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
