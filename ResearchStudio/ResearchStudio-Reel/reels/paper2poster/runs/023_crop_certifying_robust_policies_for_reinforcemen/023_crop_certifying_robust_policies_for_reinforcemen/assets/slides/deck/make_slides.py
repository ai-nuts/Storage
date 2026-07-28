#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 023
(CROP: Certifying Robust Policies for Reinforcement Learning through Functional
Smoothing - ICLR 2022, UIUC / WashU / CMU).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: a state point ringed by a certified radius r, a Gaussian
smoothing bell over the Q-function, and three reward bounds JE < Jp < J
climbing toward the empirical PGD line."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0C1826"; PANEL="#122539"; PANEL2="#173049"; STROKE="#284A66"
ACCENT="#3E9BFF"; TEAL="#33D6C0"; GOLD="#F4C24C"; RED="#F2685C"; GREEN="#46C98B"
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

def poly(pts,fill="none",stroke=ACCENT,sw=2.5,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{d}/>'

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
            T(x-12,y+h*0.70+2,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70+2,valtxt,14,color,"800"))

def stat(x,y,w,h,num,lbl,col):
    ns=min(32,h*0.34)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
def radiusfig(cx,cy,scale=1.0):
    """A state point s ringed by its certified radius r: inside the ring the
    smoothed policy's action cannot change."""
    R=int(46*scale)
    out=circle(cx,cy,R,fill="none",stroke=ACCENT,sw=2.2)
    out+=circle(cx,cy,R+10,fill="none",stroke=ACCENT,sw=1.0,opacity=0.35)
    out+=circle(cx,cy,5,fill=GOLD)
    out+=line(cx,cy,cx+R,cy,GOLD,1.6,dash="5 4")
    out+=T(cx+R/2,cy-8,"r",14,GOLD,"800",anchor="middle",ff=MONO)
    out+=T(cx,cy-R-16,"action fixed",11.5,TEAL,"800",anchor="middle")
    out+=T(cx,cy+R+22,"state  s",11.5,SEC,"700",anchor="middle")
    return out

def gaussbell(x,y,w,h):
    """Gaussian smoothing of the Q-function: noisy samples s+Delta averaged into
    a smooth (Lipschitz) value function - a bell curve over the axis."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+16; ax1=x+w-14; ay0=y+h-20
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    n=40
    def g(t):
        u=(t-0.5)*6.0
        return math.exp(-u*u/2.0)
    pts=[(ax0+i/n*(ax1-ax0), ay0-(h-40)*g(i/n)) for i in range(n+1)]
    out+=poly(pts,stroke=ACCENT,sw=2.6)
    for i in range(-2,3):
        sx=(ax0+ax1)/2 + i*(ax1-ax0)*0.10
        out+=circle(sx,ay0-6,3,fill=TEAL,opacity=0.8)
    out+=circle((ax0+ax1)/2,ay0-(h-40),4.5,fill=GOLD)
    out+=T((ax0+ax1)/2,y+18,"E[ Q(s+D) ]",11.5,GOLD,"800",anchor="middle",ff=MONO)
    out+=T(ax1,ay0-4,"s + Delta",9.5,TER,"600",anchor="end")
    return out

def envrow(x,y,w):
    """Four benchmark environments spanning very different regimes."""
    items=[("Pong",ACCENT,"Atari"),("Freeway",TEAL,"Atari"),
           ("CartPole",GOLD,"control"),("Highway",RED,"driving")]
    gap=14; bw=(w-3*gap)/4; out=""
    for i,(nm,col,sub) in enumerate(items):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,64,fill=PANEL2,stroke=col,rx=10,sw=1.6)
        out+=rect(bx,y,bw,5,fill=col,rx=3,sw=0)
        out+=T(bx+bw/2,y+34,nm,15.5,TEXT,"800",anchor="middle")
        out+=T(bx+bw/2,y+52,sub,11.5,SEC,"600",anchor="middle")
    return out

def rewardbounds(x,y,w,h):
    """Three certified reward bounds climbing toward the empirical PGD line:
    loose expectation JE < percentile Jp < tight absolute lower bound J."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+42; ax1=x+w-16; ay0=y+h-22; ay1=y+18
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    # empirical PGD reference (dashed, near the top)
    emp=ay1+0.10*(ay0-ay1)
    out+=line(ax0,emp,ax1,emp,TER,1.3,dash="6 5")
    out+=T(ax1,emp-5,"empirical PGD",9.5,TER,"700",anchor="end")
    bars=[("JE",0.34,RED),("Jp",0.62,GOLD),("J",0.88,GREEN)]
    bw=34; gap=(ax1-ax0-3*bw)/4
    for i,(lb,val,col) in enumerate(bars):
        bx=ax0+gap*(i+1)+bw*i
        top=ay0-val*(ay0-ay1)
        out+=rect(bx,top,bw,ay0-top,fill=col,rx=4,sw=0,opacity=0.9)
        out+=T(bx+bw/2,ay0+14,lb,11,col,"800",anchor="middle",ff=MONO)
    out+=T(ax0-6,ay1+2,"reward",9.5,TER,"600",anchor="end")
    return out

def sigmacurve(x,y,w,h):
    """Certified radius vs smoothing variance sigma: Freeway keeps rising to
    sigma ~ 1.0, while Pong peaks at a moderate sigma then falls."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+30; ax1=x+w-14; ay0=y+h-22; ay1=y+16
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    # Freeway: monotonic rising
    fw=[(ax0+t/100*(ax1-ax0), ay0-(0.20+0.68*(t/100)**0.7)*(ay0-ay1)) for t in range(0,101,5)]
    out+=poly(fw,stroke=TEAL,sw=2.6)
    # Pong: peak near sigma ~ 0.02 then decline
    def pv(t):
        return max(0.10,0.86*math.exp(-((t-0.20))**2/0.10))
    pg=[(ax0+t/100*(ax1-ax0), ay0-pv(t/100)*(ay0-ay1)) for t in range(0,101,5)]
    out+=poly(pg,stroke=ACCENT,sw=2.6,dash="6 5")
    px=ax0+0.20*(ax1-ax0); py=ay0-pv(0.20)*(ay0-ay1)
    out+=circle(px,py,4.5,fill=ACCENT)
    out+=T(px+6,py-6,"Pong best",9.5,ACCENT,"800")
    out+=T(ax1,fw[-1][1]-6,"Freeway",9.5,TEAL,"800",anchor="end")
    out+=T(ax0-4,ay1+4,"cert. r",9.5,TER,"600",anchor="end")
    out+=T(ax1,ay0+14,"sigma ->",9.5,TER,"600",anchor="end")
    return out

def certtree(x,y,w,h):
    """CROP-LoRe grows a trajectory tree to certify a tight absolute lower
    bound on cumulative reward."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    root=(x+26,y+h/2)
    out+=circle(root[0],root[1],6,fill=GOLD)
    lvl1=[(x+w*0.46,y+h*0.28),(x+w*0.46,y+h*0.72)]
    for p in lvl1:
        out+=line(root[0],root[1],p[0],p[1],ACCENT,1.6)
        out+=circle(p[0],p[1],5,fill=ACCENT)
    leaves=[(x+w-30,y+h*0.16),(x+w-30,y+h*0.40),(x+w-30,y+h*0.60),(x+w-30,y+h*0.84)]
    for i,p in enumerate(lvl1):
        for lf in leaves[2*i:2*i+2]:
            out+=line(p[0],p[1],lf[0],lf[1],TEAL,1.4)
            out+=circle(lf[0],lf[1],4,fill=TEAL)
    out+=T(x+14,y+16,"trajectory tree",10.5,SEC,"700")
    out+=T(x+w-14,y+h-8,"absolute lower bound J",10,GREEN,"800",anchor="end")
    return out

def attackfig(x,y,w,h):
    """A clean state observation is nudged by a bounded adversarial
    perturbation, flipping the agent's chosen action."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    cy=y+h/2
    out+=circle(x+40,cy,7,fill=TEAL)
    out+=T(x+40,cy-16,"state s",10.5,TEAL,"800",anchor="middle")
    out+=line(x+56,cy,x+w*0.52,cy,RED,2.2)
    out+=poly([(x+w*0.52-9,cy-5),(x+w*0.52,cy),(x+w*0.52-9,cy+5)],fill=RED,stroke=RED,sw=1)
    out+=T((x+56+x+w*0.52)/2,cy+18,"|| delta || <= eps",10,RED,"800",anchor="middle",ff=MONO)
    out+=circle(x+w*0.62,cy,7,fill=RED,stroke=GOLD,sw=1.5)
    out+=T(x+w*0.62,cy-16,"s + delta",10.5,RED,"800",anchor="middle")
    out+=T(x+w-14,cy+4,"action flips",10.5,GOLD,"800",anchor="end")
    out+=T(x+w-14,cy+22,"empirical defense breaks",9.5,SEC,"600",anchor="end")
    return out

def rangecmp(x,y,w,h):
    """Why RL breaks smoothing: classifier confidence lives in [0,1] and acts
    like a probability; a Q-value has an unknown, unbounded range."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    midx=x+w/2
    out+=line(midx,y+12,midx,y+h-12,STROKE,1.1,dash="4 4")
    # left: classifier [0,1]
    out+=T(x+18,y+26,"classifier",11.5,ACCENT,"800")
    out+=rect(x+18,y+40,w/2-40,20,fill=PANEL2,stroke=ACCENT,rx=5,sw=1.2)
    out+=T(x+18,y+80,"prob in [0, 1]",11,SEC,"700",ff=MONO)
    # right: Q-value unknown range
    out+=T(midx+18,y+26,"Q-value",11.5,RED,"800")
    out+=rect(midx+18,y+40,w/2-40,20,fill=PANEL2,stroke=RED,rx=5,sw=1.2)
    out+=T(midx+18,y+80,"range [Vmin, Vmax] ?",11,SEC,"700",ff=MONO)
    out+=T(midx+18,y+h-12,"not a probability",10,GOLD,"700")
    return out

def algos3(x,y,w,h):
    """The three CROP algorithms: LoAct for actions, GRe and LoRe for reward."""
    gap=20; bw=(w-2*gap)/3
    data=[("CROP-LoAct",ACCENT,"local smoothing","certified action radius"),
          ("CROP-GRe",TEAL,"global smoothing","expected & percentile reward"),
          ("CROP-LoRe",GREEN,"adaptive tree search","tight lower-bound reward")]
    out=""
    for i,(nm,col,l1,l2) in enumerate(data):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,h,fill=PANEL2,stroke=col,rx=10,sw=1.6)
        out+=rect(bx,y,bw,5,fill=col,rx=3,sw=0)
        out+=T(bx+bw/2,y+30,nm,15,col,"800",anchor="middle",ff=MONO)
        out+=T(bx+bw/2,y+52,l1,12,TEXT,"700",anchor="middle")
        for j,ln in enumerate(wrap(l2,26)):
            out+=T(bx+bw/2,y+72+j*15,ln,11.5,SEC,"600",anchor="middle")
    return out

def rankrows(x,y,w):
    """Certified-robustness ranking rows for two environments."""
    rows=[("Freeway",TEAL,"RadialRL","highest r at every sigma"),
          ("Pong",ACCENT,"SA-MDP (CVX)","most certifiably robust")]
    out=""
    for i,(env,col,win,note) in enumerate(rows):
        ry=y+i*46
        out+=rect(x,ry,w,38,fill=PANEL2,stroke=STROKE,rx=8)
        out+=rect(x,ry,5,38,fill=col,rx=3,sw=0)
        out+=T(x+20,ry+24,env,14,col,"800")
        out+=T(x+120,ry+24,win,14,TEXT,"800")
        out+=T(x+w-16,ry+24,note,12,SEC,"600",anchor="end")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2022",14,ACCENT,"800",ls="2")
    b+=T(1216,72,"Certified Robustness  ·  Reinforcement Learning",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"CROP",44,WHITE,"800")
    b+=T(64,196,"Certifying Robust Policies for Reinforcement Learning",23,ACCENT,"800")
    b+=T(64,224,"through Functional Smoothing",23,ACCENT,"800")
    b+=radiusfig(1116,176,1.0)
    b+=T(64,258,"Fan Wu · Linyi Li · Zijian Huang · Yevgeniy Vorobeychik · Ding Zhao · Bo Li",13.5,SEC,"500")
    b+=T(64,280,"UIUC   ·   Washington University in St. Louis   ·   Carnegie Mellon University",12.5,TER,"600")
    cw=276; gap=16; x0=64; cy=306; chh=224
    data=[
        (ch[0],ACCENT,x0,"RL in safety-critical systems",
         "Reinforcement learning now drives systems like autonomous vehicles, where adversarial perturbations to a policy's input states can quietly steer it toward disaster."),
        (ch[1],RED,x0+cw+gap,"Empirical is not enough",
         "Many defenses improve robustness empirically, yet almost none can certify it with theoretical guarantees against every bounded attack."),
        (ch[2],TEAL,x0+2*(cw+gap),"Certify at two levels",
         "CROP is the first unified framework to certify RL robustness at two levels: the per-state action, and a lower bound on cumulative reward."),
        (ch[3],GREEN,x0+3*(cw+gap),"9 methods, 4 environments",
         "The authors benchmark nine existing robust RL algorithms across four environments and show their certificates are often tight."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+26,cy+42,7,fill=col))
        body+=para(x+44,cy+48,ti,17,TEXT,22,22,"800")[0]
        body+=para(x+24,cy+96,tx,13,SEC,34,19)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,556,1216,556,STROKE,1)
    b+=T(64,592,"arXiv:2106.09292",14,ACCENT,"700")
    b+=T(300,592,"crop-leaderboard.github.io",13.5,SEC,"600")
    b+=T(1216,592,"Prove robustness, don't just observe it.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Certify robustness, don't just observe it")
    # c1 left tall: RL moved into costly-failure domains
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"RL where failure is costly",17.5,TEXT,"800")+
        para(92,238,"Reinforcement learning has moved into domains such as autonomous driving and trading, where a single wrong decision can be catastrophic.",14,SEC,42,22)[0]+
        rect(92,352,344,146,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,382,"the deployed decision loop",12.5,TER,"700")+
        eqbox(112,398,304,"observe s -> pick action a",13,h=40)+
        T(112,478,"one bad action can cascade",12,SEC,"600"))
    fx=500; fw=716
    # c2 adversary perturbs states, defenses break
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"A small perturbation flips the action",16.5,RED,"800")+
        para(fx+28,226,"An adversary who slightly perturbs the state observations fed to an agent can reliably change its decisions; empirical defenses keep falling to newer adaptive attacks.",14,SEC,50,21)[0]+
        attackfig(fx+430,220,272,74))
    # c3 what is missing: certification
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"What is missing: certification",16,GOLD,"800")+
        para(fx+28,392,"A way to prove, not just observe, that a trained policy stays reliable under every perturbation within a bounded budget.",14.5,TEXT,74,22)[0])
    # c4 this paper tackles the gap
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=GREEN,rx=6,sw=0)+
        T(fx+28,482,"CROP tackles exactly this gap",16,GREEN,"800")+
        para(fx+28,512,"This paper delivers the first certification of robustness for reinforcement learning, turning a hope into a provable guarantee.",14.5,SEC,74,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Why RL breaks randomized smoothing")
    # c1 left top: trust
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"The core motivation is trust",16.5,ACCENT,"800")+
        para(92,226,"If you cannot prove a policy is robust, then passing today's attacks tells you little about tomorrow's stronger, unseen adversary.",14,SEC,58,21)[0]+
        eqbox(92,300,504,"pass known attacks  =/=  robust",13.5))
    # c2 left bottom: smoothing works for classifiers
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill=PANEL,stroke=STROKE)+
        rect(64,366,6,184,fill=TEAL,rx=6,sw=0)+
        T(92,404,"Smoothing certifies classifiers",16,TEAL,"800")+
        para(92,434,"Randomized smoothing has become a leading tool for certified robustness in image classification, but reinforcement learning does not fit its mold.",14,SEC,58,21)[0]+
        chip(92,516,"add noise  ·  average outputs  ·  certified radius",TEAL,w=468,h=28))
    # c3 right top: the two mismatches
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,158,6,192,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"Q-values are not probabilities",16.5,GOLD,"800")+
        para(rx+28,226,"Classifier confidence lives in a known 0-1 range and acts like a probability; a Q-value's range is unknown, and it is not a probability.",14,TEXT,64,21)[0]+
        rect(rx+28,282,(rw-72)/2,52,fill=PANEL2,stroke=ACCENT,rx=8,sw=1.2)+
        T(rx+44,306,"classifier",11.5,ACCENT,"800")+
        T(rx+44,326,"prob in [0, 1]",11.5,SEC,"700",ff=MONO)+
        rect(rx+28+(rw-72)/2+16,282,(rw-72)/2,52,fill=PANEL2,stroke=RED,rx=8,sw=1.2)+
        T(rx+44+(rw-72)/2+16,306,"Q-value",11.5,RED,"800")+
        T(rx+44+(rw-72)/2+16,326,"range [Vmin, Vmax] ?",11.5,SEC,"700",ff=MONO))
    # c4 right bottom: reward, not one action
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(rx+28,404,"Reward, not a single action",16,GREEN,"800")+
        para(rx+28,434,"A single action decision is not the whole story: what ultimately matters is the reward accumulated along an entire trajectory. CROP overcomes both obstacles.",14,TEXT,58,21)[0]+
        T(rx+28,524,"certify action AND cumulative reward",13.5,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Two criteria, three algorithms")
    cards=[
        (ch[0],ACCENT,"Two certification criteria","CROP defines two criteria for RL: robustness of the per-state action, and a lower bound on the cumulative reward."),
        (ch[1],TEAL,"1  CROP-LoAct","Local randomized smoothing certifies a radius around each state within which the chosen action cannot change."),
        (ch[2],GREEN,"2  CROP-GRe & LoRe","Global smoothing bounds expected and percentile reward; an adaptive tree search gives a much tighter absolute lower bound."),
        (ch[3],GOLD,"3  Benchmark & leaderboard","The tools certify nine existing robust RL algorithms across four environments, released as an open leaderboard."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["2","1","2","9"]
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+74,tags[i],26,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"The first unified framework to certify RL robustness at both the action and the cumulative-reward level.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Functional smoothing of the Q-function")
    # c1 full-width top: the smoothing engine + key eq
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,168,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,168,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"The engine: functional smoothing",16.5,TEXT,"800")+
        para(92,220,"At each state and action, add Gaussian noise to the state and average the trained Q-network's output, producing a smoothed value function.",13.5,SEC,64,20)[0]+
        eqbox(92,272,560,"Q~(s,a) = E[ Q(s+D, a) ],  D ~ N(0, s^2 I)",13.5,h=40)+
        gaussbell(676,200,540,110))
    # c2 Lipschitz lemma -> certified radius
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,342,560,208,fill=PANEL,stroke=STROKE)+
        rect(64,342,6,208,fill=TEAL,rx=6,sw=0)+
        T(92,380,"Smoothed => Lipschitz => radius",16.5,TEAL,"800")+
        para(92,410,"A key lemma shows the smoothed function is Lipschitz continuous, with a constant that shrinks as the variance grows. Theorem 1 turns this into a certified radius on the action.",13.5,TEXT,58,20)[0]+
        eqbox(92,508,504,"|delta| < r  =>  action unchanged",13.5))
    # c3 the radius trade-off
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,342,rw,102,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,342,6,102,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,376,"Radius = margin trade-off",16,GOLD,"800")+
        para(rxx+28,404,"The radius grows with the gap between the top-two smoothed values; more smoothing narrows that margin.",13,TEXT,64,19)[0])
    # c4 reward: global smoothing + LoRe tree
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,460,rw,90,fill=PANEL,stroke=STROKE)+
        rect(rxx,460,6,90,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,492,"Reward: global smoothing + tree",15.5,GREEN,"800")+
        para(rxx+28,518,"Global smoothing bounds expected and percentile reward, while CROP-LoRe grows a trajectory tree for a tight absolute lower bound.",12.5,SEC,74,17)[0])
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Four environments, nine methods")
    # c1 full-width top: four environments
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"Four environments across regimes",16,TEXT,"800")+
        para(92,222,"The authors test the framework broadly, on four environments spanning very different regimes.",14,SEC,120,21)[0]+
        envrow(92,244,1096))
    # c2 the regimes
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,124,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,124,fill=TEAL,rx=6,sw=0)+
        T(92,360,"High-dim games to control & driving",15,TEAL,"800")+
        para(92,388,"Pong and Freeway are high-dimensional Atari games; CartPole is classic low-dimensional control; Highway simulates autonomous driving.",13.5,SEC,60,20)[0])
    # c3 nine methods
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,324,560,124,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,124,fill=RED,rx=6,sw=0)+
        T(684,360,"Nine robust RL methods certified",15.5,RED,"800")+
        para(684,388,"StdTrain, GaussAug, AdvTrain, SA-MDP (PGD), SA-MDP (CVX), RadialRL, CARRL, NoisyNet, and GradDQN.",13.5,SEC,60,20)[0])
    # c4 full-width callout: common footing
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,464,1152,86,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,464,6,86,fill=GREEN,rx=6,sw=0)+
        T(92,496,"Not one certificate, but a benchmark",15.5,GREEN,"800")+
        stat(640,472,168,68,"4","environments",ACCENT)+
        stat(822,472,168,68,"9","methods",TEAL)+
        stat(1004,472,168,68,"3","algorithms",GOLD)+
        T(92,524,"many robust RL methods on a common, provable footing",13,SEC,"600"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Consistent, certified winners")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,196,"The certifications reveal clear, consistent winners",16.5,GREEN,"800")+
        rect(92,214,470,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(112,244,"Certified rankings place many methods on one provable scale, with a clear leader in each environment.",13,SEC,52,20)[0]+
        rankrows(584,214,632))
    # c2 Freeway -> RadialRL
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,368,224,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,224,fill=TEAL,rx=6,sw=0)+
        T(92,360,"Freeway",16,TEAL,"800")+
        para(92,388,"RadialRL achieves the highest certified radius across every smoothing level.",13.5,SEC,42,20)[0]+
        rect(92,448,312,88,fill=PANEL2,stroke=TEAL,rx=10,sw=1.4)+
        T(110,482,"RadialRL",21,TEAL,"800")+
        para(110,506,"optimizes against worst-case perturbations",11.5,SEC,44,15)[0])
    # c3 Pong -> SA-MDP (CVX)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,324,368,224,fill=PANEL,stroke=STROKE)+
        rect(456,324,6,224,fill=ACCENT,rx=6,sw=0)+
        T(484,360,"Pong",16,ACCENT,"800")+
        para(484,388,"SA-MDP with the convex relaxation is the most certifiably robust.",13.5,SEC,42,20)[0]+
        rect(484,448,312,88,fill=PANEL2,stroke=ACCENT,rx=10,sw=1.4)+
        T(502,482,"SA-MDP (CVX)",19,ACCENT,"800")+
        para(502,506,"certified ranking matches empirical results",11.5,SEC,44,15)[0])
    # c4 new structure: periodic radius
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,324,368,224,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(848,324,6,224,fill=GOLD,rx=6,sw=0)+
        T(876,360,"A periodic pattern on Pong",15.5,GOLD,"800")+
        para(876,390,"Every method shows a periodic certified radius over time, peaking at confident states such as when the ball flies toward the paddle.",13.5,TEXT,42,20)[0]+
        chip(876,502,"an insight to guide robust training",GOLD,w=316,h=32))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Tuning sigma and the tightness of bounds")
    # c1 left top: sigma on Freeway
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Freeway: bigger sigma keeps helping",16,ACCENT,"800")+
        para(92,224,"A central ablation studies the smoothing variance sigma. On Freeway, robustness for SA-MDP and RadialRL keeps rising all the way to sigma = 1.0.",13.5,SEC,44,20)[0]+
        sigmacurve(392,206,212,140))
    # c2 left bottom: Pong prefers moderate sigma
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,378,560,172,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,378,6,172,fill=GOLD,rx=6,sw=0)+
        T(92,414,"Pong prefers a moderate sigma",15,GOLD,"800")+
        para(92,442,"On Pong the story differs: too much smoothing hurts, and a moderate sigma between about 0.01 and 0.03 works best for nearly all methods.",13.5,TEXT,58,20)[0]+
        chip(92,512,"sigma ~ 0.01 - 0.03  best on Pong",GOLD,w=468,h=28))
    # c3 right top: three reward bounds
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,204,fill=TEAL,rx=6,sw=0)+
        T(684,196,"Three reward bounds compared",16,TEAL,"800")+
        para(684,224,"The percentile bound Jp is far tighter than the loose expectation bound JE, sharpening the certified reward.",13.5,SEC,40,20)[0]+
        rewardbounds(984,206,220,146))
    # c4 right bottom: absolute lower bound is tight
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,378,560,172,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(684,414,"Absolute lower bound is tight",15.5,GREEN,"800")+
        para(684,442,"The absolute lower bound from CROP-LoRe often matches the empirical reward under PGD exactly, a zero gap over a wide range of attacks.",13.5,TEXT,58,20)[0]+
        chip(684,512,"zero gap to empirical PGD  ->  certificates are tight",GREEN,w=508,h=28))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The scope in one place")
    # c1 full-width strip: first unified framework
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,132,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,166,6,132,fill=GREEN,rx=6,sw=0)+
        T(92,202,"First unified robustness certification for RL",16.5,GREEN,"800")+
        stat(92,220,300,66,"action + reward","two certified levels",GREEN)+
        rect(410,220,806,66,fill=PANEL2,stroke=STROKE,rx=12)+
        para(430,248,"CROP works at both the per-state action level and the cumulative-reward level, the first framework to do so.",13.5,SEC,96,20)[0])
    # c2 methods & environments
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,314,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,352,"Methods & environments",16.5,ACCENT,"800")+
        stat(92,368,236,80,"9","robust RL methods",ACCENT)+
        stat(346,368,236,80,"4","environments",TEAL)+
        T(112,458,"Pong · Freeway · CartPole · Highway",12,SEC,"600"))
    # c3 algorithms & sigma
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,314,560,150,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,314,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,352,"Algorithms & smoothing",16,GOLD,"800")+
        stat(684,368,236,80,"3","CROP algorithms",GOLD)+
        stat(938,368,236,80,"sigma <= 1.0","on Freeway",TEAL)+
        T(704,458,"CROP-LoAct · CROP-GRe · CROP-LoRe",12,SEC,"600"))
    # c4 full-width bottom strip: reward bounds
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill=PANEL,stroke=STROKE)+
        rect(64,480,6,70,fill=GREEN,rx=6,sw=0)+
        T(92,510,"Three reward bounds",15.5,GREEN,"800")+
        T(92,534,"expectation JE  ·  percentile Jp (p = 50%)  ·  absolute lower bound J",13.5,SEC,"600")+
        eqbox(864,492,352,"J = sum gamma^t R(s_t)",14,h=46))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Provable robustness for RL")
    cards=[
        (ch[0],ACCENT,"Robustness need not be hope","By smoothing the value function, you can prove an agent's action stays fixed within a certified radius, not merely hope it does."),
        (ch[1],TEAL,"A provable reward floor","You can also prove a lower bound on the reward the agent will collect under any bounded attack, across a whole trajectory."),
        (ch[2],GREEN,"Correct, and often tight","Applied to nine methods across four environments, these certificates are not only correct but often tight, matching what attacks achieve."),
        (ch[3],GOLD,"A common, provable leaderboard","CROP turns robust RL into something you can measure and compare, inviting the community to certify more methods and environments."),
    ]
    cw=560; gap=32; x0=64; cy=176; chh=180
    pos=[(x0,cy),(x0+cw+gap,cy),(x0,cy+chh+18),(x0+cw+gap,cy+chh+18)]
    for (c,col,ti,tx),(x,y) in zip(cards,pos):
        body=(rect(x,y,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,y,6,chh,fill=col,rx=6,sw=0)+
              circle(x+34,y+40,10,fill=col))
        for j,ln in enumerate(wrap(ti,40)):
            body+=T(x+58,y+34+j*24,ln,17,TEXT,"800")
        body+=para(x+28,y+94,tx,14,SEC,62,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,584,1216,584,STROKE,1)
    b+=radiusfig(112,628,0.42)
    b+=T(1216,632,"CROP  ·  Certified Robust RL via Functional Smoothing  ·  ICLR 2022",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
