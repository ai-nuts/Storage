#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 004
(CW-ERM: Improving Autonomous Driving Planning with Closed-loop Weighted
Empirical Risk Minimization - NeurIPS 2022, Woven Planet).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: a top-down ego vehicle with front / side / rear collision zones,
an open-loop-expert vs closed-loop-drift lane, and a three-stage
train -> simulate -> upsample recipe."""
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
def car(cx,cy,color=ACCENT,w=38,h=68):
    """Top-down ego vehicle pointing up."""
    out=rect(cx-w/2,cy-h/2,w,h,fill=PANEL2,stroke=color,rx=12,sw=2.2)
    out+=rect(cx-w/2+6,cy-h/2+9,w-12,15,fill=color,rx=4,sw=0,opacity=0.6)   # windshield
    out+=rect(cx-w/2+6,cy+h/2-20,w-12,11,fill=color,rx=4,sw=0,opacity=0.32) # rear window
    out+=line(cx-w/2+3,cy-2,cx+w/2-3,cy-2,color,1.2,cap="butt")
    return out

def scene(cx,cy,scale=1.0):
    """Ego car with front / side / rear collision zone chips."""
    out=car(cx,cy,ACCENT)
    z=[( 0,-64,RED,"front"),(-64,6,GOLD,"side"),(64,6,GOLD,"side"),(0,72,TEAL,"rear")]
    for dx,dy,col,lb in z:
        out+=circle(cx+dx,cy+dy,7,fill=col)
    out+=T(cx,cy-78,"front",11,RED,"800",anchor="middle")
    out+=T(cx-64,cy+30,"side",11,GOLD,"800",anchor="middle")
    out+=T(cx+64,cy+30,"side",11,GOLD,"800",anchor="middle")
    out+=T(cx,cy+94,"rear",11,TEAL,"800",anchor="middle")
    return out

def driftlane(x,y,w,h):
    """Open-loop expert path (green, stays on lane) vs closed-loop policy drift
    (red, compounding error off the lane / out of distribution)."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    midy=y+h*0.60
    out+=line(x+12,y+14,x+w-12,y+14,STROKE,1.1)
    out+=line(x+12,y+h-12,x+w-12,y+h-12,STROKE,1.1)
    out+=line(x+12,midy,x+w-12,midy,TER,1.3,dash="9 9")
    exp=[(x+14+t/10*(w-28), midy) for t in range(11)]
    out+=poly(exp,stroke=GREEN,sw=2.6)
    pol=[(x+14+t/10*(w-28), midy-(h*0.42)*((t/10)**2)) for t in range(11)]
    out+=poly(pol,stroke=RED,sw=2.6,dash="6 5")
    out+=circle(pol[-1][0],pol[-1][1],4.5,fill=RED)
    out+=T(x+w-14,midy+16,"expert (open-loop)",10.5,GREEN,"800",anchor="end")
    out+=T(x+w-14,y+22,"policy drift -> OOD",10.5,RED,"800",anchor="end")
    return out

def pipeline3(x,y,w,h):
    """Three-stage recipe: train ID policy -> roll out in simulator -> retrain
    with failing scenes upsampled."""
    gap=52; bw=(w-2*gap)/3
    stages=[("1","Train identification policy","standard ERM behavioral cloning",ACCENT),
            ("2","Roll out in the simulator","collect closed-loop costs (collisions)",GOLD),
            ("3","Retrain, upsample failures","weighted ERM on the error set",GREEN)]
    out=""
    for i,(nu,ti,su,col) in enumerate(stages):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,h,fill=PANEL2,stroke=col,rx=10,sw=1.6)
        out+=rect(bx,y,bw,5,fill=col,rx=3,sw=0)
        out+=circle(bx+30,y+38,15,fill="none",stroke=col,sw=2.2)
        out+=T(bx+30,y+44,nu,17,col,"800",anchor="middle")
        for j,ln in enumerate(wrap(ti,22)):
            out+=T(bx+56,y+34+j*19,ln,14,TEXT,"800")
        for j,ln in enumerate(wrap(su,30)):
            out+=T(bx+16,y+h-30+j*15,ln,12,SEC,"600")
        if i<2:
            ax=bx+bw+gap/2
            out+=T(ax,y+h/2+7,">",26,SEC,"800",anchor="middle")
    return out

def pareto(x,y,w,h):
    """Scatter of metric-targeting configs tracing a Pareto front of trade-offs."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+30; ax1=x+w-14; ay0=y+h-24; ay1=y+16
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    out+=T(ax0-6,ay1+2,"side",9.5,TER,"600",anchor="end")
    out+=T(ax1,ay0+14,"front ->",9.5,TER,"600",anchor="end")
    # pareto frontier points (front vs side collisions)
    fr=[(ax0+0.12*(ax1-ax0),ay1+0.10*(ay0-ay1)),
        (ax0+0.34*(ax1-ax0),ay1+0.30*(ay0-ay1)),
        (ax0+0.60*(ax1-ax0),ay1+0.52*(ay0-ay1)),
        (ax0+0.86*(ax1-ax0),ay1+0.80*(ay0-ay1))]
    out+=poly(fr,stroke=GREEN,sw=2.0,dash="5 4")
    for px,py in fr:
        out+=circle(px,py,4.5,fill=GREEN)
    # a dominated (combine-with-rear) point above the front
    out+=circle(ax0+0.55*(ax1-ax0),ay1+0.24*(ay0-ay1),5,fill=RED)
    out+=T(ax0+0.55*(ax1-ax0)+9,ay1+0.24*(ay0-ay1)+3,"+rear",9.5,RED,"800")
    return out

def wcurve(x,y,w,h):
    """Side collisions vs upsampling factor w: a valley reaching its minimum
    near w~50 (best), then rising again (saturation). Lower is better."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+30; ax1=x+w-14; ay0=y+h-22; ay1=y+16
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    def val(t): return max(0.10,min(0.92,0.15+2.6*(t-0.55)**2))
    pts=[(ax0+t/100*(ax1-ax0), ay0-val(t/100)*(ay0-ay1)) for t in range(0,101,4)]
    out+=poly(pts,stroke=ACCENT,sw=2.6)
    mx=ax0+0.55*(ax1-ax0); my=ay0-val(0.55)*(ay0-ay1)
    out+=line(mx,my,mx,ay0,GOLD,1.1,dash="4 4")
    out+=circle(mx,my,5,fill=GOLD)
    out+=T(mx,my-9,"w ~ 50",11,GOLD,"800",anchor="middle")
    out+=T(ax0-4,ay1+4,"side coll.",9.5,TER,"600",anchor="end")
    out+=T(ax1,ay0+14,"upsampling w ->",9.5,TER,"600",anchor="end")
    return out

def minicar(cx,cy):
    return car(cx,cy,ACCENT,w=28,h=50)

def colllegend(x,y):
    items=[(RED,"front"),(GOLD,"side"),(TEAL,"rear")]
    out=""
    for i,(col,lb) in enumerate(items):
        cx=x+i*96
        out+=circle(cx,y,6,fill=col)+T(cx+13,y+5,lb,12.5,SEC,"700")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2022  ·  ML4AD Workshop",14,ACCENT,"800",ls="2")
    b+=T(1216,72,"Woven Planet  ·  Autonomous Driving Planning",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"CW-ERM",44,WHITE,"800")
    b+=T(64,196,"Improving Autonomous Driving Planning with Closed-loop",23,ACCENT,"800")
    b+=T(64,224,"Weighted Empirical Risk Minimization",23,ACCENT,"800")
    b+=scene(1110,176,1.0)
    b+=T(64,258,"Eesha Kumar · Yiming Zhang · Stefano Pini · Simon Stent · Ana Ferreira · Sergey Zagoruyko · Christian S. Perone",13.5,SEC,"500")
    cw=276; gap=16; x0=64; cy=290; chh=244
    data=[
        (ch[0],ACCENT,x0,"Trained open, driven closed",
         "Behavioral cloning matches expert actions one step at a time, yet the policy is deployed closed-loop where every action shapes future states."),
        (ch[1],RED,x0+cw+gap,"The mismatch hurts safety",
         "This open-loop versus closed-loop gap quietly hurts real-world driving safety."),
        (ch[2],GOLD,x0+2*(cw+gap),"A two-stage recipe",
         "Run a policy in a simulator to find the scenes where it fails, then upsample exactly those scenes when training the final policy."),
        (ch[3],GREEN,x0+3*(cw+gap),"~35% fewer collisions",
         "On a challenging urban dataset it cuts collisions substantially, with no differentiable simulator or costly closed-loop training."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+26,cy+42,7,fill=col))
        body+=para(x+44,cy+48,ti,17,TEXT,22,22,"800")[0]
        body+=para(x+24,cy+104,tx,13,SEC,34,19)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,556,1216,556,STROKE,1)
    b+=T(64,592,"arXiv:2210.02174",14,ACCENT,"700")
    b+=T(300,592,"github.com/wp-research-uk/cw-erm",13.5,SEC,"600")
    b+=T(1216,592,"Closed-loop benefits, without closed-loop training.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Trained open-loop, deployed closed-loop")
    # c1 left tall: behavioral cloning copies the next action
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Cloning the expert's next action",17.5,TEXT,"800")+
        para(92,238,"Imitation learning for self-driving is usually behavioral cloning: the network is trained to reproduce an expert's next action.",14,SEC,42,22)[0]+
        rect(92,346,344,152,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,376,"one-step supervised matching",12.5,TER,"700")+
        eqbox(112,392,304,"min  E || pi(s) - a_expert ||",13,h=40)+
        T(112,472,"open-loop: no feedback from its own acts",12,SEC,"600"))
    fx=500; fw=716
    # c2 open-loop never sees consequences
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"It never sees its own consequences",16.5,RED,"800")+
        para(fx+28,226,"Training is open-loop, so the model never sees the effects of its actions. But when it drives, every action changes the future state it will see.",14,SEC,58,21)[0]+
        driftlane(fx+430,220,272,74))
    # c3 errors compound into OOD
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill=PANEL,stroke=STROKE)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"Small errors compound into OOD",16,GOLD,"800")+
        para(fx+28,392,"Small prediction errors accumulate, pushing the car into out-of-distribution situations it was never trained on.",14.5,TEXT,74,22)[0])
    # c4 metrics that matter are invisible
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=RED,rx=6,sw=0)+
        T(fx+28,482,"The metrics that matter are invisible",16,RED,"800")+
        para(fx+28,512,"Collisions are non-differentiable, invisible to the loss, so the policy looks great open-loop but drives poorly closed-loop.",14.5,SEC,74,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Closed-loop benefits, without the cost")
    # c1 left top: Urban Driver puts a sim in the loop
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Prior work puts the sim in the loop",16.5,ACCENT,"800")+
        para(92,226,"Methods like Urban Driver run a differentiable simulator directly inside the training loop, using backpropagation through time.",14,SEC,58,21)[0]+
        eqbox(92,300,504,"grad flows through unrolled sim  (BPTT)",13.5))
    # c2 left bottom: but it is expensive
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,366,6,184,fill=GOLD,rx=6,sw=0)+
        T(92,404,"But it is expensive",16,GOLD,"800")+
        para(92,434,"It needs a differentiable simulator, it does not scale well, and it carries the heavy memory cost of unrolling policies during training.",14,TEXT,58,21)[0]+
        chip(92,516,"differentiable sim  ·  poor scaling  ·  memory heavy",GOLD,w=468,h=28))
    # c3 right top: on-policy / oracles are costly
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,192,fill=RED,rx=6,sw=0)+
        T(rx+28,196,"On-policy data and oracles cost more",16.5,RED,"800")+
        para(rx+28,226,"Other approaches collect on-policy data or add extra human oracles to label behavior, which are slow and costly to run.",14,SEC,56,21)[0]+
        chip(rx+28,300,"on-policy rollouts  ·  human oracles  ·  slow",RED,w=rw-56,h=30))
    # c4 right bottom: a simpler question
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(rx+28,404,"A simpler question -> CW-ERM",16,GREEN,"800")+
        para(rx+28,434,"Can we get closed-loop benefits by using a simulator only to decide which training scenes matter, with no loss change and no differentiability?",14,TEXT,58,21)[0]+
        T(rx+28,524,"simulator picks scenes, not gradients",13.5,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions, one simple idea")
    cards=[
        (ch[0],ACCENT,"Three contributions","A method, an empirical study, and a theoretical connection tie the paper together."),
        (ch[1],TEAL,"1  CW-ERM","Closed-loop Weighted ERM leverages metrics from policy rollouts to debias the network and shrink the open-loop to closed-loop gap."),
        (ch[2],GREEN,"2  Real gains, cheaply","Evaluated on a challenging urban driving dataset, it shows significant closed-loop improvements with no expensive closed-loop training."),
        (ch[3],GOLD,"3  A theoretical link","It connects this reweighting to the classic family that corrects covariate shift through density-ratio estimation."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["3","1","2","3"]
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
    b+=T(64,586,"Use the simulator to reweight the training data, and leave the loss and the network untouched.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Train, simulate, then upsample failures")
    # c1 full-width top: three-stage pipeline
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,168,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,168,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"Three stages, and strikingly simple",16.5,TEXT,"800")+
        pipeline3(96,206,1092,102))
    # c2 error set + upsample
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,342,560,208,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,342,6,208,fill=GREEN,rx=6,sw=0)+
        T(92,380,"Failing scenes -> upsample by w",16.5,GREEN,"800")+
        para(92,410,"Every scene with a positive cost, meaning the policy failed, goes into an error set. The final policy is retrained with weighted ERM, upsampling those scenes by a factor w.",13.5,TEXT,58,20)[0]+
        eqbox(92,508,504,"cost(scene) > 0  ->  error set,  x w",13.5))
    # c3 almost the same objective
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,342,rw,102,fill=PANEL,stroke=STROKE)+
        rect(rxx,342,6,102,fill=TEAL,rx=6,sw=0)+
        T(rxx+28,378,"Almost the same objective",16,TEAL,"800")+
        para(rxx+28,406,"Nearly identical to behavioral cloning, with a single weighting term driven by closed-loop failures.",13.5,SEC,60,20)[0])
    # c4 two tricks + no differentiable sim
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,460,rw,90,fill=PANEL,stroke=STROKE)+
        rect(rxx,460,6,90,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,492,"Two tricks, no differentiable sim",15.5,GOLD,"800")+
        para(rxx+28,518,"Early-stop the ID policy so the error set is not depleted; upsample (not reweight) for stability; any non-differentiable metric works.",12.5,SEC,72,17)[0])
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Real urban driving, at fleet scale")
    # c1 full-width top: proprietary SF & Palo Alto fleet
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,132,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"A proprietary real-world fleet dataset",16,TEXT,"800")+
        para(92,224,"Collected from the company's self-driving vehicles on challenging urban missions in San Francisco and Palo Alto.",14,SEC,72,21)[0]+
        chip(700,214,"San Francisco",ACCENT,w=230,h=32)+
        chip(946,214,"Palo Alto",TEAL,w=200,h=32))
    # c2 trajectories + HD maps
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,306,560,140,fill=PANEL,stroke=STROKE)+
        rect(64,306,6,140,fill=TEAL,rx=6,sw=0)+
        T(92,342,"Trajectories plus HD maps",16.5,TEAL,"800")+
        para(92,372,"Recorded trajectories of the ego vehicle and surrounding agents, together with high-definition maps.",14,SEC,58,21)[0])
    # c3 diverse difficult scenarios
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,306,560,140,fill=PANEL,stroke=STROKE)+
        rect(656,306,6,140,fill=RED,rx=6,sw=0)+
        T(684,342,"Diverse, difficult scenarios",16.5,RED,"800")+
        para(684,368,"Stopping behind a lead car, intersections, dense traffic with pedestrians and cyclists; most scenes 11-13 s, up to 30 s.",13.5,SEC,60,20)[0])
    # c4 full-width callout: hours + open source
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,462,1152,88,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,462,6,88,fill=GREEN,rx=6,sw=0)+
        T(92,494,"Trained at scale, simulator open-sourced",15.5,GREEN,"800")+
        stat(560,472,168,68,"180 h","training",GREEN)+
        stat(742,472,168,68,"60 h","validation",TEAL)+
        stat(924,472,168,68,"60 h","test",ACCENT)+
        T(92,522,"closed-loop sim + metrics released",13,SEC,"600"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Fewer collisions across the board")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,196,"Up to ~35% fewer collisions vs the best baseline",16.5,GREEN,"800")+
        stat(92,214,236,80,"~35%","fewer on some metrics",GREEN)+
        rect(348,214,410,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(368,244,"Beats behavioral cloning with ERM and perturbation, the strongest baseline.",13,SEC,48,20)[0]+
        rect(776,214,440,80,fill=PANEL2,stroke=STROKE,rx=12)+
        T(796,242,"Collisions cut across all zones at once:",12.5,SEC,"600")+
        colllegend(796,270))
    # c2 front collisions 14 -> 9
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,368,224,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,224,fill=RED,rx=6,sw=0)+
        T(92,360,"Front collisions",16,RED,"800")+
        para(92,388,"Upsampling front-collision scenes.",13.5,SEC,40,20)[0]+
        stat(92,420,150,104,"14","baseline",SEC)+
        T(258,476,">",26,GREEN,"800",anchor="middle")+
        stat(282,420,120,104,"9","CW-ERM",GREEN))
    # c3 side collisions 55 -> 47
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,324,368,224,fill=PANEL,stroke=STROKE)+
        rect(456,324,6,224,fill=GOLD,rx=6,sw=0)+
        T(484,360,"Side collisions",16,GOLD,"800")+
        para(484,388,"Upsampling side-collision scenes.",13.5,SEC,40,20)[0]+
        stat(484,420,150,104,"55","baseline",SEC)+
        T(650,476,">",26,GREEN,"800",anchor="middle")+
        stat(674,420,120,104,"47","CW-ERM",GREEN))
    # c4 less passive, lower variance
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,324,368,224,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(848,324,6,224,fill=GREEN,rx=6,sw=0)+
        T(876,360,"Less passive, more stable",15.5,GREEN,"800")+
        para(876,390,"Upsampling side collisions also reduces rear collisions: the policy becomes less passive, not gaming one number.",13.5,TEXT,42,20)[0]+
        chip(876,486,"variance lower than baseline",GREEN,w=316,h=32))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","How to target the right scenes")
    # c1 left top: single vs combined -> Pareto
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Single metric vs a Pareto balance",16,ACCENT,"800")+
        para(92,224,"Targeting one metric alone gives the biggest gain on it; combining metrics trades off, tracing a Pareto front.",13.5,SEC,42,20)[0]+
        pareto(400,206,204,140))
    # c2 left bottom: +rear regresses
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,378,560,172,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,378,6,172,fill=GOLD,rx=6,sw=0)+
        T(92,414,"Front + side + distance works; +rear hurts",15,GOLD,"800")+
        para(92,442,"Adding rear collisions causes a clear regression, traced to false positives from log-replayed agents that do not react in the sim.",13.5,TEXT,58,20)[0]+
        chip(92,512,"rear metric -> non-reacting replay agents",RED,w=468,h=28))
    # c3 right top: early-stop budget K
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,204,fill=TEAL,rx=6,sw=0)+
        T(684,196,"Early-stopping budget K",16,TEAL,"800")+
        para(684,224,"The identification policy is stopped early. The budget K controls how full the error set stays.",13.5,SEC,58,20)[0]+
        stat(684,286,250,60,"K = 10","best, single metric",TEAL)+
        stat(958,286,250,60,"K = 20","best, multi-metric",ACCENT))
    # c4 right bottom: upsampling factor peaks ~50
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,378,560,172,fill=PANEL,stroke=STROKE)+
        rect(656,378,6,172,fill=GOLD,rx=6,sw=0)+
        T(684,414,"Upsampling factor peaks near 50",15.5,GOLD,"800")+
        para(684,442,"Gains improve up to w around fifty, then side collisions rise again, echoing saturation in Just Train Twice.",13.5,SEC,40,20)[0]+
        wcurve(984,392,220,146))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 full-width strip: front collisions 14 -> 9
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,132,fill=RED,rx=6,sw=0)+
        T(92,202,"Front collisions, against the strongest baseline",16.5,RED,"800")+
        stat(92,220,236,66,"14 -> 9","front collisions",RED)+
        stat(346,220,236,66,"~36%","reduction",GREEN)+
        rect(600,220,616,66,fill=PANEL2,stroke=STROKE,rx=12)+
        para(620,248,"Upsampling front-collision scenes drives the largest single-metric drop.",13.5,SEC,78,20)[0])
    # c2 distance-to-reference
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,314,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,352,"Distance-to-reference & side",16.5,ACCENT,"800")+
        stat(92,368,236,80,"35 -> 28","dist-to-ref (~20%)",ACCENT)+
        stat(346,368,236,80,"55 -> 47","side collisions",GOLD))
    # c3 overall + best w
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,314,560,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,314,6,150,fill=GREEN,rx=6,sw=0)+
        T(684,352,"Overall improvement & best factor",16,GREEN,"800")+
        stat(684,368,236,80,"~35%","on some metrics",GREEN)+
        stat(938,368,236,80,"w ~ 50","best upsampling",GOLD))
    # c4 full-width bottom strip: training budget
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill=PANEL,stroke=STROKE)+
        rect(64,480,6,70,fill=TEAL,rx=6,sw=0)+
        T(92,510,"Training budget",15.5,TEAL,"800")+
        T(92,534,"180 h train  ·  60 h validation  ·  60 h test",13.5,SEC,"600")+
        eqbox(864,492,352,"final policy: 40 epochs",14,h=46))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Simpler, and safer, planners")
    cards=[
        (ch[0],ACCENT,"No diff sim, no human, no CL training","You do not need a differentiable simulator, a human in the loop, or expensive closed-loop training to get closed-loop benefits."),
        (ch[1],GOLD,"Run once, note failures, upsample, retrain","Just run the policy once in a simulator, mark the scenes where it fails, upsample those scenes, and retrain the final policy."),
        (ch[2],GREEN,"Significant, latency-free, any metric","The recipe delivers significant collision reductions, works with any closed-loop metric, and adds no inference latency."),
        (ch[3],TEAL,"A clean theoretical story","Weighting scenes by failure is closely connected to correcting covariate shift through density-ratio estimation."),
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
    b+=minicar(96,632)
    b+=colllegend(126,632)
    b+=T(1216,632,"CW-ERM  ·  Closed-loop Weighted ERM  ·  Woven Planet  ·  NeurIPS 2022",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
