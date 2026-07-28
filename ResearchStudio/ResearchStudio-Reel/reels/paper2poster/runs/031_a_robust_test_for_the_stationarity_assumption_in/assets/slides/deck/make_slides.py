#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 031
(A Robust Test for the Stationarity Assumption in Sequential Decision Making).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict --require-pptx-anchors
cue pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients,
ASCII mono equations only."""
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

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"University of Michigan  ·  LSE",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"A Robust Test for the Stationarity",40,WHITE,"800")
    b+=T(64,198,"Assumption in Sequential Decision Making",40,ACCENT,"800")
    b+=T(64,238,"A doubly robust change-point test for offline reinforcement learning",21,TEAL,"700")
    b+=T(64,276,"Jitao Wang   ·   Chengchun Shi   ·   Zhenke Wu      —   U-M Biostatistics  &  LSE Statistics",15,SEC,"500")
    # four concept cards (2x2) = anchors
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=312; cy1=cy0+chh+22
    data=[
        (ch[0],ACCENT,x0,cy0,"The hidden assumption","Almost every RL algorithm assumes the world never changes. In mobile health, traffic, and robotics that stationarity quietly breaks and poisons the policy."),
        (ch[1],TEAL,x1,cy0,"A doubly robust test","A statistical test checks whether an offline Markov decision process is actually stationary, and pinpoints where the dynamics change."),
        (ch[2],GOLD,x0,cy1,"ML meets semiparametrics","It pairs flexible ML estimators with semiparametric statistics, so it controls false alarms yet stays powerful even in high dimensions."),
        (ch[3],GREEN,x1,cy1,"Detect, then recover","Across four simulations and a real intern health study, it finds change points others miss and lets policies recover lost reward."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,13.5,SEC,72,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,606,1216,606,STROKE,1)
    b+=T(64,642,"github.com/jtwang95/Double_CUSUM_RL",14,ACCENT,"700")
    b+=T(560,642,"Is your offline MDP really stationary?  Test it before you trust the policy.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","One fragile assumption under every policy")
    # c1 left tall card: RL optimizes but leans on a fragile assumption
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"RL chases the optimal policy",18,TEXT,"800")+
        para(92,240,"Agents are trained to find the best possible policy, but nearly every algorithm leans on one fragile premise.",15,SEC,42,24)[0]+
        # stationary MDP glyph: fixed transition arrows
        rect(92,336,344,120,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,362,"Assumed: a frozen MDP",12.5,TER,"700")+
        circle(140,412,12,fill=ACCENT)+T(140,417,"s",13,BG,"800",anchor="middle")+
        line(156,412,232,412,ACCENT,2)+T(194,402,"P, R fixed",11.5,SEC,"600",anchor="middle")+
        circle(252,412,12,fill=ACCENT)+T(252,417,"s'",12,BG,"800",anchor="middle")+
        line(268,412,344,412,ACCENT,2)+
        circle(364,412,12,fill=ACCENT)+
        T(92,502,"Transition P and reward R never change with time.",13.5,ACCENT,"700"))
    # right column
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,124,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,124,fill=GOLD,rx=6,sw=0)+
        T(fx+28,196,"The stationarity assumption",17,GOLD,"800")+
        para(fx+28,226,"It requires the state-transition function and the reward function to stay exactly the same at every time step over the whole horizon.",14.5,SEC,72,22)[0]+
        T(fx+28,272,"P_t = P  and  R_t = R   for all t",14.5,GOLD,"800",ff=MONO))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,294,fw,110,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,294,6,110,fill=RED,rx=6,sw=0)+
        T(fx+28,332,"In the real world it rarely holds",16,RED,"800")+
        para(fx+28,362,"Robotics, healthcare, and digital marketing all drift over long horizons, so a frozen policy turns suboptimal, even harmful.",14.5,TEXT,74,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,416,fw,134,fill=PANEL,stroke=STROKE)+
        rect(fx,416,6,134,fill=ACCENT,rx=6,sw=0)+
        T(fx+28,454,"The question this paper answers",16,ACCENT,"800")+
        para(fx+28,484,"Before you trust the policy an offline system produced, can you reliably tell whether that system was actually stationary in the first place?",14.5,SEC,74,22)[0]+
        T(fx+28,540,"Test stationarity  ->  then trust (or relearn) the policy",14,ACCENT,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Why non-stationarity matters now")
    # c1 left: Intern Health Study + waning-effect timeline
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,198,"The Intern Health Study",18,TEAL,"800")+
        para(92,230,"A year-long mobile-health trial that nudges first-year physicians toward healthier habits with push notifications.",14.5,SEC,50,22)[0]+
        _waning(92,318,504,150)+
        T(92,502,"A textbook case of drift over a long horizon.",13.5,TEAL,"700"))
    # right column
    rx=648; rw=568
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,120,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,120,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"The effect wanes over time",16,GOLD,"800")+
        para(rx+28,226,"Nudge effectiveness fades as the year goes on. Traffic-signal control shows the same drift, swinging between peak and off-peak flow.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,290,rw,116,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(rx,290,6,116,fill=RED,rx=6,sw=0)+
        T(rx+28,328,"Ignoring the shift is costly",16,RED,"800")+
        para(rx+28,358,"A stationary policy sends prompts at the wrong moments and steadily erodes the long-term reward it was meant to raise.",14.5,TEXT,60,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,418,rw,132,fill=PANEL,stroke=STROKE)+
        rect(rx,418,6,132,fill=ACCENT,rx=6,sw=0)+
        T(rx+28,456,"Prior tests leave a gap",16,ACCENT,"800")+
        para(rx+28,486,"Prior tests either need a fully known model, or lean on linear approximations that break in high dimensions.",14.5,SEC,64,22)[0]+
        T(rx+28,540,"known model  X      linear approx  X  (high-dim)",13.5,ACCENT,"800",ff=MONO))
    return svg(b)

def _waning(x,y,w,h):
    # decaying nudge-effect curve with change marker
    box=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    axis=line(x+16,y+h-20,x+w-12,y+h-20,STROKE,1.5)+line(x+16,y+14,x+16,y+h-20,STROKE,1.5)
    pts=[]
    for i in range(0,w-40,10):
        t=i/(w-44)
        v=math.exp(-2.2*t)
        pts.append((x+22+i, (y+h-24)-v*(h-46)))
    poly=f'<polyline points="{" ".join(f"{px:.1f},{py:.1f}" for px,py in pts)}" fill="none" stroke="{GOLD}" stroke-width="2.6"/>'
    # change marker
    mx=x+22+int((w-44)*0.55)
    mark=line(mx,y+16,mx,y+h-20,RED,1.6,dash="4 4")+T(mx,y+12,"change",11,RED,"700",anchor="middle")
    lbl=T(x+22,y+30,"nudge effect",11.5,GOLD,"700")+T(x+w-14,y+h-6,"weeks ->",11,TER,"600",anchor="end")
    return box+axis+poly+mark+lbl

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","A doubly robust stationarity test")
    cards=[
        (ch[0],ACCENT,"1","Test and detect","A model-based, doubly robust procedure that tests the stationarity assumption and locates change points in offline reinforcement learning."),
        (ch[1],TEAL,"2","Double robustness","Type-I error stays controlled as long as either the transition function or the marginal state-action distribution is correctly specified."),
        (ch[2],GOLD,"3","Theory + p-values","Size control and double robustness under a bidirectional asymptotic framework (N or T may diverge), with a Gaussian multiplier bootstrap for honest p-values."),
    ]
    cw=368; gap=24; x0=64; cy=180; chh=360
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+52,cy+70,26,fill="none",stroke=col,sw=2.5)+
              T(x+52,cy+80,num,28,col,"800",anchor="middle"))
        yy=cy+142
        for j,ln in enumerate(wrap(ti,22)):
            body+=T(x+28,yy+j*28,ln,20,TEXT,"800")
        yy+=28*len(wrap(ti,22))+16
        body+=para(x+28,yy,tx,15,SEC,40,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,584,"Valid inference even when one nuisance model is wrong  —  that is what doubly robust buys you.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","CUSUM comparison, made doubly robust")
    # LEFT column: c1 + c2
    lx=64; lw=568
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,196,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,196,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Step 1  ·  compare before vs after",16.5,ACCENT,"800")+
        para(lx+28,226,"At each candidate change point t, compare the pooled transition dynamics before and after t with a CUSUM-style statistic.",14,SEC,58,21)[0]+
        _prepost(lx+28,300,lw-56,40))
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,370,lw,180,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(lx,370,6,180,fill=RED,rx=6,sw=0)+
        T(lx+28,408,"Step 2  ·  kill the plug-in bias",16,RED,"800")+
        para(lx+28,438,"Naively plugging ML estimators into the comparison introduces heavy bias, so add a mean-zero augmentation term to get a doubly robust estimating function psi.",14,SEC,58,21)[0]+
        eqbox(lx+28,506,lw-56,"psi = naive  +  mean-zero correction   (E psi = 0 under H0)",13))
    # RIGHT column: c3 + c4 + key equation
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,150,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,150,fill=TEAL,rx=6,sw=0)+
        T(rxx+28,196,"Step 3  ·  plug in flexible ML",16,TEAL,"800")+
        para(rxx+28,226,"The correction lets neural nets, random forests, or lasso estimate the transition and state-action distributions without spoiling the inference.",14,SEC,56,21)[0]+
        chip(rxx+28,282,"neural nets  ·  random forests  ·  lasso",TEAL,w=rw-56,h=30))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,324,rw,130,fill=PANEL,stroke=STROKE)+
        rect(rxx,324,6,130,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,362,"Step 4  ·  normalize, then bootstrap",16,GOLD,"800")+
        para(rxx+28,392,"Sample splitting and cross-fitting normalize the statistic across candidate points and test functions; a Gaussian multiplier bootstrap gives the p-value.",14,SEC,56,21)[0])
    # key equation strip (full width bottom-right area)
    b+=(rect(rxx,470,rw,80,fill=PANEL2,stroke=ACCENT,rx=12,sw=1.5)+
        rect(rxx,470,6,80,fill=ACCENT,rx=6,sw=0)+
        T(rxx+28,496,"Test statistic",12.5,ACCENT,"800")+
        T(rxx+rw/2,528,"Gamma = max_t max_h  sqrt( t(T-t)/T^2 )  S(t,h)",15,TEXT,"800",anchor="middle",ff=MONO))
    return svg(b)

def _prepost(x,y,w,h):
    seg=w-120
    mid=x+int(seg*0.55)
    base=y+h-6
    l=line(x,base,x+seg,base,STROKE,3)
    before=line(x,base,mid,base,ACCENT,4)
    after=line(mid,base,x+seg,base,GOLD,4)
    mk=line(mid,y-2,mid,base+6,RED,1.8,dash="4 4")+circle(mid,base,5,fill=RED)
    lbls=(T(x+seg*0.27,y+12,"P before",12,ACCENT,"800",anchor="middle")+
          T(x+seg*0.78,y+12,"P after",12,GOLD,"800",anchor="middle")+
          T(mid,base+22,"candidate t",11,RED,"700",anchor="middle")+
          T(x+seg+16,base+4,"same?",13,TEXT,"800"))
    return l+before+after+mk+lbls

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Four simulations and one real trial")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"The method is stress-tested across four numerical studies of rising difficulty, plus one real mobile-health dataset.",16,TEXT,"600"))
    # c2 discrete toy + high-dim synthetic (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,150,fill=TEAL,rx=6,sw=0)+
        T(92,280,"Toy example + high-dim synthetic",17,TEAL,"800")+
        para(92,312,"A discrete-state toy shows double robustness; synthetic data pushes the state dimension from 1 up to 30.",14,SEC,60,21)[0]+
        chip(92,352,"vs ODCP   ·   vs CUSUM-RL     state dim 1 -> 30",TEAL,w=468,h=30))
    # c3 grid world + batch-online (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,280,"Grid world + batch-online",17,GOLD,"800")+
        para(684,312,"A 4x4 grid world shows change detection improving policy learning; a batch-online study mimics the real trial.",14,SEC,60,21)[0]+
        chip(684,352,"4x4 grid world   ·   semi-synthetic online study",GOLD,w=468,h=30))
    # c4 IHS real (full width)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,410,1152,140,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,410,6,140,fill=GREEN,rx=6,sw=0)+
        T(92,448,"Real data  ·  the Intern Health Study (IHS)",17,GREEN,"800")+
        para(92,480,"A 21-week micro-randomized mobile-health trial of first-year medical interns in the United States, the study that motivated the whole method.",14.5,TEXT,110,23)[0]+
        T(92,536,"21 weeks   ·   micro-randomized trial   ·   Internal Medicine & Family Practice",13.5,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Robust where baselines break: high dimensions")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,50,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,50,fill=GREEN,rx=6,sw=0)+
        T(92,182,"The headline finding is robustness to dimensionality: the test keeps working as the state grows.",16.5,TEXT,"700"))
    # c2 detection-by-dimension matrix (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,214,6,264,fill=TEAL,rx=6,sw=0)+
        T(92,250,"Correct change-point detection by state dim",15.5,TEAL,"800")+
        _detgrid(92,272))
    # c3 baselines fail (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,214,560,264,fill=PANEL,stroke=STROKE)+
        rect(656,214,6,264,fill=RED,rx=6,sw=0)+
        T(684,250,"Where the baselines break",16,RED,"800")+
        para(684,282,"CUSUM-RL recovers the change point only when the state is one-dimensional. ODCP fails to control the type-I error at all in high dimensions.",14,SEC,56,21)[0]+
        rect(684,352,504,50,fill=PANEL2,stroke=STROKE,rx=10)+circle(710,377,6,fill=GOLD)+T(726,382,"CUSUM-RL: works only at dim = 1",14,TEXT,"700")+
        rect(684,410,504,50,fill=PANEL2,stroke=STROKE,rx=10)+circle(710,435,6,fill=RED)+T(726,440,"ODCP: type-I error uncontrolled in high dim",14,TEXT,"700"))
    # c4 toy double robustness strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,492,6,116,fill=GREEN,rx=6,sw=0)+
        T(92,526,"Toy example  ·  double robustness in action",16,GREEN,"800")+
        para(92,556,"Size and power hold as long as at least one of the two nuisance models is correctly specified, with the strongest power when both are right.",14.5,TEXT,74,22)[0]+
        _drpills(880,512))
    b+=T(64,646,"Detection survives to state dimension 30, where the closest competitor only works at dimension one.",14,SEC,"600")
    return svg(b)

def _detgrid(x,y):
    # rows: Proposed / CUSUM-RL / ODCP ; cols: dim 1,10,20,30
    dims=["dS=1","dS=10","dS=20","dS=30"]
    rows=[("Proposed",[1,1,1,1],TEAL),("CUSUM-RL",[1,0,0,0],GOLD),("ODCP",[0,0,0,0],RED)]
    out=""
    cx0=x+120; cw=96; ch=44; gap=8
    for j,d in enumerate(dims):
        out+=T(cx0+j*(cw+gap)+cw/2,y+16,d,13,SEC,"700",anchor="middle")
    for i,(name,cells,col) in enumerate(rows):
        ry=y+30+i*(ch+gap)
        out+=T(x+8,ry+ch*0.62,name,13.5,TEXT,"800")
        for j,v in enumerate(cells):
            bx=cx0+j*(cw+gap)
            fill= "#0F2E2B" if v else "#2A1720"
            edge= GREEN if v else RED
            out+=rect(bx,ry,cw,ch,fill=fill,stroke=edge,rx=8,sw=1.4)
            mark="check" if v else "X"
            out+=T(bx+cw/2,ry+ch*0.66,("OK" if v else "fail"),14,edge,"800",anchor="middle")
    return out

def _drpills(x,y):
    # 2x2 double-robustness mini legend
    return (T(x,y,"M1 / M2 spec",11,TER,"700")+
            rect(x,y+8,150,30,fill="#0F2E2B",stroke=GREEN,rx=7,sw=1.2)+T(x+75,y+28,"either correct = valid",11.5,GREEN,"800",anchor="middle")+
            rect(x,y+44,150,30,fill=PANEL2,stroke=ACCENT,rx=7,sw=1.2)+T(x+75,y+64,"both correct = best power",11.5,ACCENT,"800",anchor="middle"))

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Double robustness, sweep by sweep")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,120,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,120,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Sweep 1  ·  vary misspecification",16.5,ACCENT,"800")+
        para(92,226,"Vary the model misspecification level lambda from mild to severe across five hundred replications.",14.5,SEC,54,22)[0]+
        T(92,268,"lambda in {0.1, 0.3, 0.5, 0.7, 0.9}   ·   500 reps",13.5,ACCENT,"800",ff=MONO))
    # c2 double-robustness 2x2 matrix (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,294,560,256,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,294,6,256,fill=GREEN,rx=6,sw=0)+
        T(92,330,"Empirical size stays at nominal if either model is right",14,TEXT,"800")+
        _drmatrix(178,352))
    # c3 kappa sweep (right, tall)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,392,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Sweep 2  ·  locate the change point",16.5,GOLD,"800")+
        para(684,226,"Sweep kappa, the length of the tested interval. The test holds its size while the null is true, then its power climbs once the interval crosses the true change point at 25.",14.5,SEC,58,22)[0]+
        _powercurve(684,318,504,180)+
        T(684,528,"Correct size for kappa <= 25  ·  rising power for kappa > 25",13.5,GOLD,"800"))
    return svg(b)

def _drmatrix(x,y):
    # 2x2: rows M1 correct/wrong, cols M2 correct/wrong
    cw=170; ch=64; gap=8
    out=T(x-16,y+ch*0.6,"M1 ok",11.5,SEC,"700",anchor="end")+T(x-16,y+ch+gap+ch*0.6,"M1 wrong",11.5,SEC,"700",anchor="end")
    out+=T(x+cw/2,y-8,"M2 ok",11.5,SEC,"700",anchor="middle")+T(x+cw+gap+cw/2,y-8,"M2 wrong",11.5,SEC,"700",anchor="middle")
    cells=[[(GREEN,"valid+ (best)"),(GREEN,"valid")],
           [(GREEN,"valid"),(RED,"invalid")]]
    for i in range(2):
        for j in range(2):
            col,lab=cells[i][j]
            bx=x+j*(cw+gap); by=y+i*(ch+gap)
            fill="#0F2E2B" if col==GREEN else "#2A1720"
            out+=rect(bx,by,cw,ch,fill=fill,stroke=col,rx=9,sw=1.4)
            out+=T(bx+cw/2,by+ch*0.62,lab,14,col,"800",anchor="middle")
    return out

def _powercurve(x,y,w,h):
    box=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax=line(x+24,y+h-22,x+w-12,y+h-22,STROKE,1.5)+line(x+24,y+12,x+24,y+h-22,STROKE,1.5)
    # true change point at kappa=25 -> fraction 0.5
    cpx=x+24+int((w-40)*0.5)
    # nominal size line (flat low), then power rising after cpt
    pts=[]
    for i in range(0,w-40,8):
        t=i/(w-44)
        if t<=0.5:
            v=0.05
        else:
            v=0.05+0.9*(1-math.exp(-6*(t-0.5)))
        pts.append((x+24+i,(y+h-24)-v*(h-40)))
    poly=f'<polyline points="{" ".join(f"{px:.1f},{py:.1f}" for px,py in pts)}" fill="none" stroke="{GOLD}" stroke-width="2.8"/>'
    nom=line(x+24,(y+h-24)-0.05*(h-40),x+w-12,(y+h-24)-0.05*(h-40),ACCENT,1.4,dash="5 4")
    mk=line(cpx,y+14,cpx,y+h-22,RED,1.6,dash="4 4")+T(cpx,y+10,"kappa=25",11,RED,"700",anchor="middle")
    lbl=T(x+30,y+26,"rejection rate",11.5,GOLD,"700")+T(x+w-14,y+h-8,"kappa ->",11,TER,"600",anchor="end")+T(x+w-14,(y+h-24)-0.05*(h-40)-4,"alpha=0.05",10.5,ACCENT,"700",anchor="end")
    return box+ax+nom+poly+mk+lbl

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    # c1 dimension reach big strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,164,1152,142,fill=PANEL,stroke=STROKE)+
        rect(64,164,6,142,fill=TEAL,rx=6,sw=0)+
        T(92,202,"Change-point detection reaches far higher dimensions",16.5,TEAL,"800")+
        kpi(92,220,"dS = 30","proposed still detects",TEAL,w=250,h=74)+
        T(360,264,"vs",26,SEC,"800",anchor="middle")+
        kpi(400,220,"dS = 1","CUSUM-RL ceiling",GOLD,w=250,h=74)+
        rect(672,220,544,74,fill=PANEL2,stroke=STROKE,rx=12)+
        para(692,248,"Correct detection sustained all the way to a 30-dimensional state, where the closest competitor works only at dimension one.",13.5,SEC,64,20)[0])
    # c2 nominal significance (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,322,560,196,fill=PANEL,stroke=STROKE)+
        rect(64,322,6,196,fill=ACCENT,rx=6,sw=0)+
        T(92,358,"Size control everywhere",16.5,ACCENT,"800")+
        kpi(92,378,"0.05","nominal alpha held",ACCENT,w=250,h=96)+
        kpi(370,378,"4 + 2","sims + real specialties",TEAL,w=250,h=96)+
        T(92,502,"Type-I error stays at the nominal level in every setting.",13.5,SEC,"600"))
    # c3 real IHS finding (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,322,560,196,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,322,6,196,fill=GREEN,rx=6,sw=0)+
        T(684,358,"On the real Intern Health Study",16.5,GREEN,"800")+
        kpi(684,378,"week 16","Internal Medicine: change",GREEN,w=250,h=96)+
        kpi(966,378,"none","Family Practice: no change",SEC,w=250,h=96)+
        T(684,502,"A genuine change point for one specialty, none for the other.",13.5,SEC,"600"))
    # c4 evidence base footer
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,534,1152,70,fill=PANEL2,stroke=STROKE,rx=12)+
        rect(64,534,6,70,fill=GOLD,rx=6,sw=0)+
        T(92,566,"Evidence base",13,GOLD,"800")+
        T(92,588,"Every number rests on thousands of bootstrap samples and hundreds of replications per setting.",14.5,TEXT,"600")+
        T(1188,576,"5000 bootstrap  ·  100-500 reps",13.5,GOLD,"800",anchor="end",ff=MONO))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Test stationarity, then trust the policy")
    cards=[
        (ch[0],ACCENT,"The idea in one line","A doubly robust CUSUM test tells you, reliably, when an offline RL environment has stopped being stationary."),
        (ch[1],TEAL,"ML flexibility, valid inference","It marries flexible machine-learning estimators with semiparametric rigor, so it stays valid even in high dimensions, and policies can be relearned on the correct, stationary segment of data."),
        (ch[2],GREEN,"Recover the reward left on the table","When some homogeneity is present, detecting and adapting to change points recovers near-oracle reward that stationary or sliding-window strategies simply give up."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,92,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"A Robust Test for the Stationarity Assumption in Sequential Decision Making",15.5,TEXT,"700")
    b+=T(64,660,"ICML 2023  ·  Wang, Shi & Wu  ·  github.com/jtwang95/Double_CUSUM_RL",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
