#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 078 (RvS, ICLR 2022).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry."""
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

def poly(pts,fill="none",stroke=ACCENT,sw=2,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{d}/>'

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

def bar(x,y,w,val,vmax,color,label,valtxt,lblcolor=SEC,h=26,lblw=None):
    bw=max(2,int(w*val/vmax))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-12,y+h*0.70,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70,valtxt,14,color,"800"))

def kpi(x,y,num,lbl,col,w=168,h=100):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.56,num,32,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.82,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34,fs=14.5):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+5,text,fs,TEXT,"600"))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2022  ·  OFFLINE RL",14,ACCENT,"800",ls="2.5")
    b+=T(1216,72,"UC Berkeley  ·  CMU",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    # c1: the question = title block
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        T(64,168,"RvS: What is Essential for Offline RL",46,WHITE,"800")+
        T(64,224,"via Supervised Learning?",46,ACCENT,"800"))
    # c2: byline / RvS framing
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,262,1152,64,fill=PANEL,stroke=STROKE)+
        rect(64,262,6,64,fill=TEAL,rx=6,sw=0)+
        T(92,290,"Scott Emmons  ·  Benjamin Eysenbach  ·  Ilya Kostrikov  ·  Sergey Levine",16,TEXT,"700")+
        T(92,314,"RvS = Reinforcement learning via Supervised learning — a unifying view of conditional imitation for offline RL.",14.5,SEC,"500"))
    # c3: surprising finding (left card)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,352,564,190,fill=PANEL,stroke=STROKE)+
        rect(64,352,6,190,fill=GREEN,rx=6,sw=0)+
        T(92,392,"The surprising finding",17,GREEN,"800")+
        para(92,424,"A plain two-layer feedforward network, trained just to maximize likelihood, matches state-of-the-art methods built on temporal-difference learning or Transformer sequence models.",15,SEC,54,24)[0])
    # c4: two levers (right card)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(652,352,564,190,fill=PANEL,stroke=STROKE)+
        rect(652,352,6,190,fill=GOLD,rx=6,sw=0)+
        T(680,392,"Only two things really matter",17,GOLD,"800")+
        chip(680,412,"1  ·  Model capacity  —  tune width & regularization",ACCENT,w=508,h=40,fs=14.5)+
        chip(680,460,"2  ·  What you condition on  —  goals or rewards",TEAL,w=508,h=40,fs=14.5)+
        T(680,524,"Everything else turns out to be optional.",14,TER,"600"))
    b+=line(64,566,1216,566,STROKE,1)
    b+=T(64,600,"A minimal recipe that is competitive with far more complex RL machinery.",16,TEXT,"600")
    b+=T(64,644,"arXiv:2112.10751",14,ACCENT,"700")
    b+=T(320,644,"github.com/scottemmons/rvs",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","What actually makes supervised offline RL work?")
    # c1 headline card (full width)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Plain supervised learning already works — but the picture is muddy",17,TEXT,"800")+
        para(92,228,"Recent work showed supervised learning, with no temporal-difference bootstrapping at all, can be remarkably effective for offline RL. Yet it was unclear why.",15,SEC,96,24)[0])
    # c2 contradictions (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,274,564,166,fill=PANEL,stroke=STROKE)+
        rect(64,274,6,166,fill=GOLD,rx=6,sw=0)+
        T(92,312,"Contradictory conclusions",16,GOLD,"800")+
        para(92,344,"Different papers disagreed about what makes these methods work:",14.5,SEC,58,22)[0]+
        chip(92,372,"Some emphasized advantage weighting",GOLD,w=508,h=28,fs=13.5)+
        chip(92,406,"Others reached for large Transformer models",RED,w=508,h=28,fs=13.5))
    # c3 the core question (right, small)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(652,274,564,166,fill=PANEL,stroke=STROKE)+
        rect(652,274,6,166,fill=TEAL,rx=6,sw=0)+
        T(680,312,"A simple, unanswered question",16,TEAL,"800")+
        para(680,348,"Stripped of the disagreements, one question remains open — and this paper sets out to answer it directly, component by component.",14.5,SEC,56,24)[0])
    # c4 the ask (full-width emphasized)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,460,1152,116,fill="#0F2A2E",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,460,6,116,fill=TEAL,rx=6,sw=0)+
        T(92,498,"The question",15,TEAL,"800",ls="1")+
        para(92,528,"When does supervised learning for offline RL actually work, and which algorithmic components are truly essential versus merely incidental complexity that could be stripped away without cost?",16,TEXT,110,26)[0])
    b+=T(64,632,"The goal is not a new algorithm, but a clear account of what is essential.",14,TER,"600")
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Why look past value-based RL?")
    # c1 value-based dominate (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,564,168,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,168,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Value-based methods dominate",16,ACCENT,"800")+
        para(92,228,"They rule offline and off-policy RL and come with appealing theoretical guarantees on optimality and convergence.",14.5,SEC,56,24)[0]+
        chip(92,286,"Strong theory  ·  well-studied",ACCENT,w=508,h=30,fs=13.5))
    # c2 but hard in practice (right top)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(652,158,564,168,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(652,158,6,168,fill=RED,rx=6,sw=0)+
        T(680,196,"But hard to apply in practice",16,RED,"800")+
        para(680,228,"They need complex tricks to stabilize learning and careful tuning of many interacting hyperparameters.",14.5,TEXT,56,24)[0]+
        chip(680,286,"Fragile training  ·  many knobs",RED,w=508,h=30,fs=13.5))
    # c3 the alternative (full width)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,346,1152,120,fill=PANEL,stroke=STROKE)+
        rect(64,346,6,120,fill=TEAL,rx=6,sw=0)+
        T(92,384,"An attractive alternative: turn RL into conditional imitation",16,TEAL,"800")+
        para(92,416,"Convert the RL problem into a conditional, filtered, or weighted imitation-learning problem — using the insight that experience suboptimal for one task may be optimal for another.",15,SEC,110,24)[0])
    # c4 payoff (full width)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,486,1152,120,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,486,6,120,fill=TEAL,rx=6,sw=0)+
        T(92,524,"Why it is worth doing",15,TEAL,"800",ls="1")+
        para(92,554,"If a minimal supervised recipe can match these complex value-based methods, it gives practitioners a dependable field guide — and reveals exactly where supervised methods still break down.",15,TEXT,110,24)[0])
    b+=T(64,652,"Simplicity that matches the state of the art is itself a finding.",14,TER,"600")
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions")
    # c1 headline
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,66,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,66,fill=ACCENT,rx=6,sw=0)+
        T(92,199,"Not a new algorithm — a unifying framework, a minimal recipe, and an honest map of what matters.",17,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","One unifying framework","Place many existing goal-conditioned and reward-conditioned methods under a single view the authors call RvS: reinforcement learning via supervised learning."),
        (ch[2],GREEN,"2","A minimal recipe","Through extensive experiments, boil these methods down to essentials: a two-layer feedforward network trained to maximize likelihood is competitive with far more complex methods."),
        (ch[3],GOLD,"3","What matters, and the limits","Identify the choices that matter — model capacity, regularization, and what to condition on — and honestly show RvS is comparatively weak on purely random data."),
    ]
    cw=368; gap=24; x0=64; cy=250
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,320,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+68,27,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+78,num,30,col,"800",anchor="middle"))
        yy=cy+132
        for j,ln in enumerate(wrap(ti,24)):
            body+=T(x+28,yy+j*28,ln,19,TEXT,"800")
        yy+=28*len(wrap(ti,24))+10
        body+=para(x+28,yy,tx,14.5,SEC,40,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,624,"A field guide, not a new state-of-the-art claim.",14,TER,"600")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Condition, relabel, and maximize likelihood")
    gx=[64,648]; cw=568
    # c1 setup (top-left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(gx[0],158,cw,192,fill=PANEL,stroke=STROKE)+
        rect(gx[0],158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(gx[0]+28,196,"Condition the policy on an outcome",16.5,ACCENT,"800")+
        para(gx[0]+28,228,"In a Markov decision process, train a policy conditioned on an outcome omega — either a future goal state or an average future return.",14.5,SEC,58,23)[0]+
        chip(gx[0]+28,300,"omega = future goal state",TEAL,w=248,h=34,fs=13.5)+
        chip(gx[0]+296,300,"omega = average return",GOLD,w=248,h=34,fs=13.5))
    # c2 hindsight relabeling (top-right)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(gx[1],158,cw,192,fill=PANEL,stroke=STROKE)+
        rect(gx[1],158,6,192,fill=TEAL,rx=6,sw=0)+
        T(gx[1]+28,196,"Hindsight relabeling",16.5,TEAL,"800")+
        para(gx[1]+28,228,"Given offline trajectories, every observed action becomes a demonstration for whatever outcome actually occurred later in that same trajectory.",14.5,SEC,58,23)[0]+
        T(gx[1]+28,318,"(s, a)  →  demonstration for outcome that followed",14.5,TEXT,"700",ff=MONO))
    # c3 architecture (bottom-left) with mini MLP diagram
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(gx[0],366,cw,214,fill=PANEL,stroke=STROKE)+
        rect(gx[0],366,6,214,fill=GOLD,rx=6,sw=0)+
        T(gx[0]+28,404,"Just a two-layer MLP",16.5,GOLD,"800")+
        para(gx[0]+28,436,"A feedforward network with two fully connected layers; the outcome is fed in simply by concatenating it onto the input state.",14.5,SEC,58,23)[0]+
        _mlp(gx[0]+40,498))
    # c4 objective (bottom-right)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(gx[1],366,cw,214,fill=PANEL,stroke=STROKE)+
        rect(gx[1],366,6,214,fill=GREEN,rx=6,sw=0)+
        T(gx[1]+28,404,"Maximize log-likelihood — nothing else",16,GREEN,"800")+
        rect(gx[1]+28,424,cw-56,46,fill=PANEL2,stroke=STROKE,rx=8)+
        T(gx[1]+cw/2,gx[1]*0+452,"max_theta   E[ log pi_theta( a | s, omega ) ]",17,TEXT,"800",anchor="middle",ff=MONO)+
        _nochip(gx[1]+28,486,"no advantage weighting")+
        _nochip(gx[1]+28,520,"no temporal-difference bootstrapping")+
        _nochip(gx[1]+300,486,"no Transformer")+
        _nochip(gx[1]+300,520,"only max-likelihood"))
    b+=T(64,624,"Relabeled experience turns offline RL into ordinary supervised learning.",14,TER,"600")
    return svg(b)

def _mlp(x,y):
    # tiny 4-layer node diagram: input(concat s,omega) -> hidden -> hidden -> action
    sp=16
    cols=[(x,4,ACCENT,"s | omega"),(x+150,3,TEAL,"FC 1"),(x+300,3,TEAL,"FC 2"),(x+430,2,GOLD,"a")]
    maxn=4; ybase=y+(maxn-1)*sp
    out=""; coords=[]
    for cx,n,col,lbl in cols:
        top=y+(maxn-n)*sp/2.0
        ys=[top+i*sp for i in range(n)]
        coords.append((cx,ys,col))
        out+=T(cx,ybase+24,lbl,12,SEC,"700",anchor="middle")
    for (cx0,ys0,_),(cx1,ys1,_) in zip(coords,coords[1:]):
        for a in ys0:
            for c in ys1:
                out+=line(cx0,a,cx1,c,STROKE,0.7)
    for cx,ys,col in coords:
        for yy in ys:
            out+=circle(cx,yy,5,fill=col)
    return out

def _nochip(x,y,text):
    return (circle(x+8,y+8,7,fill="none",stroke=RED,sw=1.6)+
            line(x+3.5,y+12.5,x+12.5,y+3.5,RED,1.6)+
            T(x+24,y+13,text,13,SEC,"600"))

# ---------- SLIDE 6: DATASET / BENCHMARK ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","A deliberately broad evaluation")
    # c1 headline
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"Two benchmark families spanning navigation, locomotion, and manipulation.",16.5,TEXT,"600"))
    # c2 D4RL card (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,236,564,300,fill=PANEL,stroke=STROKE)+
        rect(64,236,6,300,fill=ACCENT,rx=6,sw=0)+
        T(92,274,"D4RL  ·  three suites",18,ACCENT,"800")+
        _dsrow(92,296,"AntMaze","8-DoF quadruped navigating a maze",ACCENT)+
        _dsrow(92,368,"Gym Locomotion","HalfCheetah · Hopper · Walker  (random / medium / medium-replay / medium-expert)",TEAL)+
        _dsrow(92,458,"Franka Kitchen","9-DoF manipulation from human demonstrations",GOLD))
    # c3 GCSL card (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(652,236,564,300,fill=PANEL,stroke=STROKE)+
        rect(652,236,6,300,fill=TEAL,rx=6,sw=0)+
        T(680,274,"GCSL  ·  goal-conditioned suite",18,TEAL,"800")+
        _dschip(680,300,"2D navigation",TEAL)+_dschip(908,300,"Sawyer arm",TEAL)+
        _dschip(680,344,"Lunar Lander",TEAL)+_dschip(908,344,"Robotic claw",TEAL)+
        para(680,406,"Originally online goal-reaching tasks, adapted for offline RL by collecting data with a random policy.",14.5,SEC,58,23)[0]+
        chip(680,472,"Offline data from a random policy",GOLD,w=508,h=34,fs=13.5))
    # c4 normalization strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,556,1152,66,fill=PANEL2,stroke=STROKE)+
        rect(64,556,6,66,fill=GREEN,rx=6,sw=0)+
        T(92,584,"Common scale",14.5,GREEN,"800")+
        T(92,608,"All scores normalized into a 0–100 range so methods can be compared directly.",15,TEXT,"600")+
        T(1188,596,"0  →  100",22,GREEN,"800",anchor="end",ff=MONO))
    return svg(b)

def _dsrow(x,y,ti,sub,col):
    out=circle(x+7,y+8,6,fill=col)+T(x+24,y+13,ti,16,TEXT,"800")
    pp,_=para(x+24,y+34,sub,13.5,SEC,64,19)
    return out+pp

def _dschip(x,y,text,col):
    return (rect(x,y,206,32,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+16,y+16,5,fill=col)+T(x+30,y+21,text,13.5,TEXT,"600"))

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","A two-layer MLP reaches state of the art")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill="#0F2E2B",stroke=GREEN,rx=12,sw=1.5)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"Nothing but a two-layer network trained with maximum likelihood — state of the art across several suites.",16.5,TEXT,"700"))
    # c2 AntMaze bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,564,182,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,182,fill=ACCENT,rx=6,sw=0)+
        T(92,250,"AntMaze  ·  goal-conditioned",16.5,ACCENT,"800")+
        T(92,278,"Average normalized score (higher is better)",13,SEC,"600")+
        bar(240,296,300,53.5,60,GREEN,"RvS-G","53.5",h=28)+
        bar(240,338,300,50.6,60,GOLD,"best value-based","50.6",h=28)+
        T(92,384,"A plain MLP edges out the strongest value-based baseline.",13,TEAL,"700"))
    # c3 Kitchen + GCSL (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(652,214,564,182,fill=PANEL,stroke=STROKE)+
        rect(652,214,6,182,fill=TEAL,rx=6,sw=0)+
        T(680,250,"Franka Kitchen  &  GCSL suite",16.5,TEAL,"800")+
        kpi(680,266,"54","Kitchen score",GREEN,w=150,h=96)+
        bar(940,300,232,62,70,GREEN,"RvS","62",h=26)+
        bar(940,340,232,58,70,GOLD,"online GCSL","58",h=26)+
        T(848,378,"RvS wins on GCSL using only offline data.",13,TEAL,"700"))
    # c4 Gym Locomotion + stitching (full width)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,412,1152,208,fill=PANEL,stroke=STROKE)+
        rect(64,412,6,208,fill=GOLD,rx=6,sw=0)+
        T(92,450,"Gym Locomotion  &  stitching",16.5,GOLD,"800")+
        rect(92,470,520,132,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,500,"Reward-conditioned RvS  ≈  Decision Transformer",15.5,TEXT,"800")+
        para(112,528,"Matched performance — but with a simple multilayer perceptron instead of a large Transformer sequence model.",14,SEC,56,22)[0]+
        _mono_eq(112,588,"MLP  ==  Transformer   (on locomotion)")+
        rect(640,470,536,132,fill="#0F2E2B",stroke=TEAL,rx=10,sw=1.5)+
        T(660,500,"Even on stitching tasks",15.5,TEAL,"800")+
        para(660,528,"Long thought to demand dynamic programming, yet goal-conditioned RvS keeps pace with value-based methods.",14,TEXT,58,22)[0]+
        T(660,592,"No dynamic programming required to stay competitive.",13,SEC,"600"))
    return svg(b)

def _mono_eq(x,y,text):
    return T(x,y,text,15,TEAL,"800",ff=MONO)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","What actually matters")
    # c1 capacity + saturating curve (left, tall)
    body=(rect(64,158,564,448,fill=PANEL,stroke=STROKE)+
          rect(64,158,6,448,fill=ACCENT,rx=6,sw=0)+
          T(92,196,"1  ·  Capacity: bigger is better",16.5,ACCENT,"800")+
          para(92,228,"The best networks are notably larger than those used in standard online RL or imitation learning. Widening the network up to about a thousand hidden units generally helps.",14.5,SEC,58,23)[0])
    body+=_capacity_curve(112,360)
    body+=T(92,584,"More policy capacity is the single most consistent win.",13.5,TEAL,"700")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],body)
    # c2 dropout mixed (right top)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(652,158,564,190,fill=PANEL,stroke=STROKE)+
        rect(652,158,6,190,fill=GOLD,rx=6,sw=0)+
        T(680,196,"2  ·  Regularization: dropout is not universal",15.5,GOLD,"800")+
        _pmrow(680,222,"+","helps kitchen-complete (small human demos)",GREEN)+
        _pmrow(680,258,"-","hurts hopper-medium-expert",RED)+
        _pmrow(680,294,"-","hurts antmaze-medium-play",RED)+
        T(680,332,"Add a little dropout, and only where it helps.",13,SEC,"600"))
    # c3 categorical output (right middle)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(652,364,564,124,fill=PANEL,stroke=STROKE)+
        rect(652,364,6,124,fill=TEAL,rx=6,sw=0)+
        T(680,400,"3  ·  Output distribution",15.5,TEAL,"800")+
        para(680,430,"A categorical distribution over discretized actions matches or beats a unimodal Gaussian across the GCSL tasks — more capacity again.",14,SEC,58,22)[0])
    # c4 val loss note (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(652,504,564,102,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(652,504,6,102,fill=GOLD,rx=6,sw=0)+
        T(680,540,"4  ·  Validation loss is a weak signal",15.5,GOLD,"800")+
        para(680,570,"It correlates only loosely with final performance — not reliable for tuning on its own.",14,TEXT,58,22)[0])
    return svg(b)

def _capacity_curve(x,y):
    # saturating perf-vs-width curve
    x0,y0=x+40,y+150; ww=430; hh=150
    out=line(x0,y0,x0+ww,y0,SEC,1.5)+line(x0,y0,x0,y0-hh,SEC,1.5)
    out+=T(x0+ww,y0+22,"hidden units",12,TER,"600",anchor="end")
    out+=T(x0-10,y0-hh+4,"perf",12,TER,"600",anchor="end")
    pts=[]
    for i in range(0,ww+1,12):
        t=i/ww
        v=1-math.exp(-3.1*t)   # saturating
        pts.append((x0+i, y0-int(hh*0.90*v)))
    out+=poly(pts,stroke=ACCENT,sw=2.5)
    # marker at ~1000 units (saturation knee)
    kx=x0+int(ww*0.72)
    v=1-math.exp(-3.1*0.72)
    ky=y0-int(hh*0.90*v)
    out+=circle(kx,ky,5,fill=GREEN)+line(kx,ky,kx,y0,GREEN,1,dash="3 3")
    out+=T(kx,ky-12,"~1000 units",12,GREEN,"800",anchor="middle")
    return out

def _pmrow(x,y,sign,text,col):
    return (circle(x+11,y+3,11,fill="none",stroke=col,sw=1.8)+
            T(x+11,y+8,sign,16,col,"800",anchor="middle")+
            T(x+32,y+8,text,13.5,TEXT,"600"))

# ---------- SLIDE 9: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","A practitioner's field guide")
    # c1 headline card
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,72,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,72,fill=GREEN,rx=6,sw=0)+
        T(92,192,"You do not need advantage weighting or a Transformer",17,TEXT,"800")+
        T(92,216,"Plain supervised learning, done right, is competitive with the state of the art for offline RL.",15,SEC,"500"))
    # c2 the two conditions
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,246,564,168,fill=PANEL,stroke=STROKE)+
        rect(64,246,6,168,fill=ACCENT,rx=6,sw=0)+
        T(92,284,"Get two things right",16,ACCENT,"800")+
        chip(92,302,"Tune model capacity & regularization",ACCENT,w=508,h=38,fs=14)+
        chip(92,348,"Choose what to condition on: goals or rewards",TEAL,w=508,h=38,fs=14)+
        T(92,398,"A two-layer MLP trained by max-likelihood does the rest.",13.5,SEC,"600"))
    # c3 the recipe
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(652,246,564,168,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(652,246,6,168,fill=TEAL,rx=6,sw=0)+
        T(680,284,"The concrete recipe",16,TEAL,"800")+
        _step(680,306,"1","Grow network width until performance saturates",TEAL)+
        _step(680,352,"2","Then add a little dropout",TEAL)+
        T(680,402,"Simple, reproducible, and cheap to tune.",13.5,SEC,"600"))
    # c4 caveat strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,434,1152,120,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(64,434,6,120,fill=RED,rx=6,sw=0)+
        T(92,472,"The honest caveat",15,RED,"800",ls="1")+
        para(92,502,"On purely random data, temporal-difference methods still win — which the authors flag as an open problem for future work.",15.5,TEXT,110,26)[0])
    b+=line(64,584,1216,584,STROKE,1)
    b+=T(64,616,"RvS: What is Essential for Offline RL via Supervised Learning?",16,TEXT,"700")
    b+=T(64,644,"ICLR 2022  ·  arXiv:2112.10751  ·  github.com/scottemmons/rvs",13.5,SEC,"600")
    return svg(b)

def _step(x,y,num,text,col):
    return (circle(x+13,y+3,13,fill="none",stroke=col,sw=1.8)+
            T(x+13,y+9,num,14,col,"800",anchor="middle")+
            T(x+36,y+9,text,14.5,TEXT,"700"))

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
