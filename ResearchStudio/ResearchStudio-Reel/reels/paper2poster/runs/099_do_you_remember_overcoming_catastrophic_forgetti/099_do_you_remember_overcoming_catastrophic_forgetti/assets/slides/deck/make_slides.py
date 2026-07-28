#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 099
(Do You Remember? Overcoming Catastrophic Forgetting for Fake Audio Detection - RAWM, ICML 2023).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass resolves every
anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: paired audio waveforms - a steady TEAL genuine wave vs a jagged RED fake wave -
plus a small retention/forgetting curve, echoing 'remember the old while learning the new'."""
import json, os, math

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
def wave(x,y,w,n,color,amp,jag=0.0,sw=3.0):
    """A small centered audio waveform of n vertical bars. jag adds fake-style
    irregularity; amp is max half-height. Genuine = low jag, fake = high jag."""
    out=""; bw=3; gap=(w-n*bw)/(n-1)
    for i in range(n):
        t=i/(n-1)
        base=math.sin(t*math.pi*3.0)
        wobble=math.sin(t*math.pi*11.0+1.3)*jag + math.sin(t*math.pi*23.0)*jag*0.6
        v=abs(base*(1-jag*0.4)+wobble)
        hh=max(3,amp*(0.28+0.72*min(1.0,v)))
        cx=x+i*(bw+gap)
        out+=f'<line x1="{cx}" y1="{y-hh}" x2="{cx}" y2="{y+hh}" stroke="{color}" stroke-width="{bw}" stroke-linecap="round"/>'
    return out

def forgetcurve(x,y,w,h):
    """Two retention curves over a task sequence: RAWM stays high (green),
    fine-tuning forgets (red decay). Small inset chart."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+14; ax1=x+w-12; ay0=y+h-16; ay1=y+14
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    good=[]; bad=[]
    for i in range(0,101,5):
        t=i/100.0
        gv=0.90-0.06*t
        bv=0.90*math.exp(-2.6*t)+0.05
        good.append((ax0+t*(ax1-ax0), ay0-gv*(ay0-ay1)))
        bad.append((ax0+t*(ax1-ax0), ay0-bv*(ay0-ay1)))
    out+=poly(good,stroke=GREEN,sw=2.6)
    out+=poly(bad,stroke=RED,sw=2.6,dash="5 4")
    out+=T(ax1-2,ay1+2,"RAWM",10.5,GREEN,"800",anchor="end")
    out+=T(ax1-2,ay0-3,"fine-tune",10.5,RED,"700",anchor="end")
    out+=T(ax0,ay0+13,"tasks ->",10,TER,"600")
    return out

def projglyph(x,y,color=ACCENT):
    """Small orthogonal-projector schematic: an update vector projected off a
    subspace line, plus a second projector Q."""
    out=""
    ox,oy=x,y+70
    out+=line(ox,oy,ox+150,oy,STROKE,2.0)            # subspace of previous inputs
    out+=T(ox,oy+18,"prev-input subspace",11,TER,"600")
    out+=line(ox+20,oy,ox+92,oy-58,SEC,2.4)          # raw gradient g
    out+=T(ox+96,oy-58,"g",13,SEC,"800")
    out+=line(ox+20,oy,ox+20,oy-58,color,3.0)        # P g (orthogonal)
    out+=T(ox+2,oy-40,"Pg",12.5,color,"800",anchor="end")
    out+=f'<path d="M {ox+34} {oy-40} q 10 6 0 18" fill="none" stroke="{TEAL}" stroke-width="2.4"/>'
    out+=T(ox+58,oy-24,"beta.Q",12,TEAL,"800")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Institute of Automation, CAS  ·  Continual Learning for Fake Audio Detection",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"Do You Remember?",42,WHITE,"800")
    b+=T(64,198,"Overcoming Catastrophic Forgetting for Fake Audio Detection",26,ACCENT,"800")
    # genuine vs fake waveform motif near the title
    b+=wave(940,150,150,34,TEAL,20,jag=0.05)
    b+=wave(940,196,150,34,RED,20,jag=0.85)
    b+=T(1015,232,"genuine  vs  fake",12,TER,"600",anchor="middle")
    b+=T(64,236,"Xiaohui Zhang  ·  Jiangyan Yi  ·  Jianhua Tao  ·  Chenglong Wang  ·  Chuyuan Zhang     —   RAWM",14.5,SEC,"500")
    # four concept cards in a row = anchors
    cw=276; gap=16; x0=64; cy=296; chh=236
    data=[
        (ch[0],RED,x0,"Detectors don't transfer",
         "Fake audio detectors work well on their own data, but accuracy collapses on audio from a new dataset."),
        (ch[1],GOLD,x0+cw+gap,"Fine-tuning forgets",
         "Fine-tuning on the new data makes the model forget the old, the classic catastrophic forgetting problem."),
        (ch[2],ACCENT,x0+2*(cw+gap),"RAWM",
         "Regularized Adaptive Weight Modification adapts updates by the genuine-to-fake ratio and adds a memory regularizer."),
        (ch[3],GREEN,x0+3*(cw+gap),"No replay, 10x less",
         "Without replaying any past samples, forgetting drops to about one tenth, and it even generalizes beyond audio."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              wave(x+26,cy+42,120,20,col,13,jag=(0.85 if col==RED else 0.1))+
              para(x+24,cy+96,ti,17.5,TEXT,26,23,"800")[0])
        body+=para(x+24,cy+150,tx,13,SEC,34,19)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,562,1216,562,STROKE,1)
    b+=T(64,598,"arXiv:2308.03300",14,ACCENT,"700")
    b+=T(300,598,"github.com/Cecile-hi/Regularized-Adaptive-Weight-Modification",13.5,SEC,"600")
    b+=T(1216,598,"Learn the new dataset without forgetting the old.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Detectors don't cross datasets, fixes forget")
    # c1 left tall: fake audio is a rising threat
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Fake speech is now human-like",18,TEXT,"800")+
        para(92,240,"Speech synthesis and voice conversion produce human-like speech, so reliable fake audio detection has become critical.",14.5,SEC,42,23)[0]+
        rect(92,352,344,146,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,382,"real vs synthesized waveform",12.5,TER,"700")+
        wave(112,428,320,18,TEAL,14,jag=0.05)+
        wave(112,470,320,18,RED,14,jag=0.85))
    # right column, three stacked
    fx=500; fw=716
    # c2 EER rises across datasets
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"Great on its own set, poor on the next",16.5,RED,"800")+
        para(fx+28,226,"A detector performs well on its own dataset, but its Equal Error Rate rises dramatically on audio from another dataset.",14,SEC,58,21)[0]+
        bar(fx+250,270,200,3.0,40,TEAL,"own set EER","low",h=24)+
        bar(fx+250,300,200,34.0,40,RED,"new set EER","high",h=24))
    # c3 obvious fix forgets
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"The obvious fix backfires",16,GOLD,"800")+
        para(fx+28,392,"Fine-tuning on the new data causes the network to forget what it had learned before.",14.5,TEXT,74,22)[0])
    # c4 replay is impractical (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill=PANEL,stroke=STROKE)+
        rect(fx,444,6,106,fill=TEAL,rx=6,sw=0)+
        T(fx+28,482,"And you can't just replay old data",16,TEAL,"800")+
        para(fx+28,512,"Earlier remedies replay old samples, which is impractical when the original data is inaccessible.",14.5,SEC,74,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Genuine speech is a regularity to exploit")
    # c1 left top: OWM treats every input the same
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"OWM treats every input alike",16.5,ACCENT,"800")+
        para(92,226,"Existing weight-modification methods such as OWM constrain every update the same way, ignoring which class an input belongs to.",14,SEC,58,21)[0]+
        eqbox(92,300,504,"OWM:  W <- W - lr * P * g   (same P for all)",13.5))
    # c2 left bottom: genuine similar, fake varies
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,366,6,184,fill=TEAL,rx=6,sw=0)+
        T(92,404,"Genuine looks alike; fake drifts",16,TEAL,"800")+
        para(92,434,"In fake audio detection genuine speech stays similar from one dataset to the next, while the fake speech varies a lot.",14,TEXT,58,21)[0]+
        wave(92,516,230,16,TEAL,12,jag=0.05)+T(92,540,"genuine: stable",11.5,TER,"600")+
        wave(360,516,230,16,RED,12,jag=0.9)+T(360,540,"fake: varies",11.5,TER,"600"))
    # c3 right top: adapt the update direction
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,192,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"Let the update direction adapt",16.5,GOLD,"800")+
        para(rx+28,226,"That regularity is an opportunity: the direction of a weight update should adapt to how genuine-heavy versus fake-heavy each batch is.",14,SEC,56,21)[0]+
        eqbox(rx+28,300,rw-56,"beta = #genuine / #fake  in the batch",13.5))
    # c4 right bottom: acoustic conditions can backfire (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=GOLD,rx=6,sw=0)+
        T(rx+28,404,"Some sets need a safeguard",16,GOLD,"800")+
        para(rx+28,434,"Some datasets record genuine audio under acoustic conditions so different that a naive rule backfires, motivating an extra safeguard.",14,TEXT,58,21)[0]+
        T(rx+28,522,"very different conditions  ->  add regularization",13.5,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One method, two essential steps")
    cards=[
        (ch[0],ACCENT,"RAWM","Regularized Adaptive Weight Modification: a replay-free continual learning method built from two essential steps."),
        (ch[1],TEAL,"1  Adaptive weights","An extra projector adjusts the update direction by the ratio of similar-distribution classes, such as genuine utterances, to the rest."),
        (ch[2],GOLD,"2  Regularization","A term inspired by learning without forgetting keeps the new inference distribution close to the old one."),
        (ch[3],GREEN,"Replay-free, general","No previous samples are needed, and the authors show it transfers to speech emotion and image recognition."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["RAWM","1","2","+"]
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+74,tags[i],(18 if i==0 else 26),col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"Adapt the weights to the batch, and regularize the model to remember, with no stored data.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Two projectors that balance old and new")
    lx=64; lw=568
    # c1 start from OWM projector P, add Q scaled by beta
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,204,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Start from OWM's projector P",16.5,ACCENT,"800")+
        para(lx+28,224,"P points the update away from the subspace of previous inputs. RAWM adds a second projector Q, orthogonal to P and scaled by the genuine/fake ratio beta.",13.5,SEC,60,20)[0]+
        eqbox(lx+28,304,lw-56,"P g _|_ span(prev inputs);   Q _|_ P,  scale beta",13))
    # c2 combine into modified direction R
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,378,lw,172,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,378,6,172,fill=TEAL,rx=6,sw=0)+
        T(lx+28,416,"Combine into direction R",16,TEAL,"800")+
        para(lx+28,444,"Normalized and combined, a mostly-genuine batch leans toward preserving old knowledge; otherwise it leans toward learning the new data.",13.5,TEXT,60,20)[0]+
        eqbox(lx+28,506,lw-56,"R = norm(P) + beta * norm(Q),   Q _|_ P",13.5))
    rxx=656; rw=560
    # c3 regularization: teacher-student
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,204,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,204,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Regularize with a frozen teacher",16.5,GOLD,"800")+
        para(rxx+28,224,"For datasets recorded under very different conditions, the frozen pre-trained model acts as a teacher; the fine-tuned student matches its softened outputs to remember the old inference distribution.",13.5,SEC,58,20)[0]+
        eqbox(rxx+28,318,rw-56,"L = L_ce + lambda * KD(student || teacher)",13))
    # c4 no replay (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,378,rw,172,fill=PANEL,stroke=STROKE)+
        rect(rxx,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,416,"Crucially: no replay",16,GREEN,"800")+
        para(rxx+28,444,"None of this stores or replays past samples. Old knowledge is kept purely through the projector and the regularizer.",13.5,TEXT,58,20)[0]+
        T(rxx+28,528,"memory kept in the weights, not a buffer",13.5,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Four fake-audio sets, plus two transfers")
    # c1 four-dataset sequence strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,132,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"A continual-learning sequence of four datasets",16,TEXT,"800")+
        _seqchip(112,222,"ASVspoof 2019 LA","source",ACCENT)+
        T(320,250,"->",22,SEC,"800",anchor="middle")+
        _seqchip(348,222,"ASVspoof 2015","t2",TEAL)+
        T(556,250,"->",22,SEC,"800",anchor="middle")+
        _seqchip(584,222,"VCC 2020","t3",GOLD)+
        T(792,250,"->",22,SEC,"800",anchor="middle")+
        _seqchip(820,222,"In-the-Wild","t4",RED))
    # c2 distinct conditions / in-the-wild deepfakes
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,306,560,140,fill=PANEL,stroke=STROKE)+
        rect(64,306,6,140,fill=RED,rx=6,sw=0)+
        T(92,342,"Each a distinct condition",16.5,RED,"800")+
        para(92,372,"Every set has its own acoustic and linguistic condition; In-the-Wild is real-world deepfakes of public figures.",14,SEC,58,21)[0])
    # c3 EER metric
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,306,560,140,fill=PANEL,stroke=STROKE)+
        rect(656,306,6,140,fill=TEAL,rx=6,sw=0)+
        T(684,342,"Measured by Equal Error Rate",16.5,TEAL,"800")+
        para(684,372,"Detection quality on every dataset is reported as the Equal Error Rate, or EER.",14,SEC,58,21)[0]+
        eqbox(684,404,504,"lower EER  =  better detection",13,h=30))
    # c4 breadth: SER + image (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,462,1152,88,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,462,6,88,fill=GOLD,rx=6,sw=0)+
        T(92,498,"Beyond audio",16,GOLD,"800")+
        para(210,492,"To show breadth, RAWM is also evaluated on speech emotion recognition and on the CLEAR-10 image recognition benchmark.",14,TEXT,92,22)[0])
    return svg(b)

def _seqchip(x,y,name,tag,col,w=196,h=52):
    return (rect(x,y,w,h,fill=PANEL2,stroke=col,rx=10,sw=1.5)+
            rect(x,y,5,h,fill=col,rx=2,sw=0)+
            T(x+16,y+24,name,13.5,TEXT,"800")+
            T(x+16,y+42,tag,11.5,TER,"600"))

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Ten times less forgetting, best on both")
    # c1 headline strip: forgetting 1/10, new error halved
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,196,"RAWM cuts forgetting to about one tenth of fine-tuning",16.5,GREEN,"800")+
        stat(92,214,220,80,"~1/10","forgetting vs fine-tune",GREEN)+
        stat(332,214,220,80,"~1/2","error on the new set",TEAL)+
        forgetcurve(576,214,300,80)+
        rect(900,214,300,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(920,244,"Old knowledge is retained while the new dataset is still learned.",13,SEC,42,20)[0])
    # c2 lowest EER vs mainstream CL methods (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,224,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,224,fill=ACCENT,rx=6,sw=0)+
        T(92,360,"Lowest EER on old and new",16,ACCENT,"800")+
        para(92,388,"Across two- and four-dataset sequences, RAWM beats mainstream continual learning methods on both old and new data.",13.5,SEC,58,20)[0]+
        bar(300,452,250,8.0,20,RED,"fine-tune","high",h=22)+
        bar(300,480,250,5.5,20,GOLD,"EWC / LwF / OWM","mid",h=22)+
        bar(300,508,250,1.6,20,GREEN,"RAWM","lowest",h=22)+
        T(300,540,"vs EWC · LwF · OWM · DFWF",12,TER,"600"))
    # c3 coefficient 1/2 keeps error low (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,324,560,224,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,224,fill=GOLD,rx=6,sw=0)+
        T(684,360,"Coefficient one half is best",16,GOLD,"800")+
        para(684,388,"With the regularization coefficient at one half, giving equal attention to old and new, error stays low across all four datasets even as a baseline collapses.",13.5,SEC,58,20)[0]+
        eqbox(684,486,504,"lambda = 1/2  ->  equal old / new attention",13,h=40))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Which component carries the weight")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Two components, separated",16.5,ACCENT,"800")+
        para(92,226,"The ablation isolates the two ingredients of RAWM: adaptive weight modification and the memory regularization term.",14,SEC,56,21)[0]+
        chip(92,268,"AWM  +  regularization",ACCENT,w=468,h=28))
    # c2 similar distribution -> AWM does the work (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(92,362,"Similar sets: AWM carries it",16.5,GREEN,"800")+
        para(92,392,"When old and new datasets share a similar feature distribution, adaptive weight modification does most of the work; removing it sharply raises error.",14,TEXT,56,21)[0]+
        bar(300,472,250,3.0,20,GREEN,"with AWM","low",h=24)+
        bar(300,506,250,14.0,20,RED,"AWM removed","high",h=24))
    # c3 different conditions -> regularization is key (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Different sets: regularization is key",16,GOLD,"800")+
        para(684,226,"When datasets are recorded under very different conditions, the regularization term becomes the key to overcoming forgetting.",14,SEC,56,21)[0])
    # c4 primary driver (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(684,362,"AWM is the primary driver",16.5,TEAL,"800")+
        para(684,392,"Across the full four-dataset sequence, removing adaptive weight modification hurts more than removing regularization.",14,SEC,56,21)[0]+
        chip(684,468,"remove AWM  ->  larger error jump",RED,w=504,h=30)+
        chip(684,506,"regularization: valuable complement",TEAL,w=504,h=30))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 forgetting 1/10, new error 1/2 (big strip)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,132,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Forgetting and new-set error, both slashed",16.5,GREEN,"800")+
        stat(92,220,250,66,"~1/10","forgetting vs fine-tune",GREEN)+
        stat(360,220,250,66,"~1/2","error on the new set",TEAL)+
        rect(630,220,586,66,fill=PANEL2,stroke=STROKE,rx=12)+
        para(650,248,"Old datasets stay accurate while the new one is learned, with no replay buffer.",13.5,SEC,74,20)[0])
    # c2 few-sample regime (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,314,560,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,314,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,352,"Only 100 new samples",16.5,GREEN,"800")+
        stat(92,368,158,80,"0.92","EER old set",GREEN)+
        stat(262,368,158,80,"0.31","EER new set",TEAL)+
        stat(432,368,158,80,"~8","fine-tune EER",RED))
    # c3 SER transfer (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,314,6,150,fill=ACCENT,rx=6,sw=0)+
        T(684,352,"Speech emotion recognition",16.5,ACCENT,"800")+
        stat(684,368,250,80,"~42%","MSP-Podcast acc",ACCENT)+
        stat(958,368,250,80,"54%","IEMOCAP acc",TEAL)+
        T(684,456,"best of all continual learning methods tested",12.5,TER,"600"))
    # c4 optimal lambda (bottom strip)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,480,6,70,fill=GOLD,rx=6,sw=0)+
        T(92,510,"Optimal regularization weight",15.5,GOLD,"800")+
        T(92,534,"Equal attention to old and new data works best.",13.5,SEC,"600")+
        eqbox(864,492,352,"lambda = 1/2",15,h=46))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Learn the new, keep the old, store nothing")
    cards=[
        (ch[0],ACCENT,"Teach new sets without forgetting","You can teach a fake audio detector new datasets without it forgetting the old, and without keeping any of the old data around."),
        (ch[1],TEAL,"Adapt the update, regularize the memory","RAWM makes the weight update adapt to how genuine-heavy each batch is, and regularizes the model to remember its previous behavior."),
        (ch[2],GREEN,"A regularity that generalizes","Because some classes stay similar across datasets in many problems, the same recipe extends to speech emotion and image recognition."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,88,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=wave(64,624,150,18,TEAL,13,jag=0.05)
    b+=wave(232,624,150,18,RED,13,jag=0.85)
    b+=T(1216,632,"RAWM  ·  Overcoming Catastrophic Forgetting for Fake Audio Detection  ·  ICML 2023",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
