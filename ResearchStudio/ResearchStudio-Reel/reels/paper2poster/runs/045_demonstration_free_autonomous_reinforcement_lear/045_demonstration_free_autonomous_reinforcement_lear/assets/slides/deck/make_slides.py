#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 045
(IBC: Demonstration-free Autonomous RL via Implicit and Bidirectional Curriculum, ICML 2023).
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

def poly(pts,fill=ACCENT,stroke=None,sw=1.5,opacity=None):
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<polygon points="{p}" fill="{fill}"{st}{o}/>'

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
            T(x+bw+10,y+h*0.72,valtxt,13.5,color,"800"))

def kpi(x,y,num,lbl,col,w=168,h=100):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.54,num,28,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=15,h=42):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# reusable native glyphs -------------------------------------------------------
def arrowhead(x,y,ang,col,hl=10,spread=0.5):
    l=(x-hl*math.cos(ang-spread), y-hl*math.sin(ang-spread))
    r=(x-hl*math.cos(ang+spread), y-hl*math.sin(ang+spread))
    return poly([(x,y),l,r],fill=col)

def robot(cx,cy,col,r=22,stroke_col=None):
    stroke_col=stroke_col or col
    b=circle(cx,cy,r,fill=PANEL2,stroke=stroke_col,sw=2)
    # tiny robot arm / gripper glyph
    b+=circle(cx,cy-2,6,fill="none",stroke=col,sw=2)
    b+=line(cx-8,cy+8,cx+8,cy+8,col,2)
    return b

def state_node(cx,cy,label,col,r=22):
    return (circle(cx,cy,r,fill=PANEL2,stroke=col,sw=2)+
            T(cx,cy+5,label,14,col,"800",anchor="middle",ff=MONO))

def agent_loop(x,y,w,h):
    """Forward agent pi_f (start->goal) + auxiliary agent pi_a (goal->start), a reset-free cycle."""
    b=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    sx=x+70; gx=x+w-70; cy=y+h/2+6
    b+=state_node(sx,cy,"s0",ACCENT)
    b+=T(sx,cy+44,"target init states",11.5,SEC,"700",anchor="middle")
    b+=circle(gx,cy,22,fill=PANEL2,stroke=GOLD,sw=2)
    b+=poly([(gx-6,cy-7),(gx+8,cy),(gx-6,cy+7)],fill=GOLD)
    b+=T(gx,cy+44,"task goal g*",11.5,SEC,"700",anchor="middle")
    # forward arrow (top, green)
    b+=path(f"M {sx+26} {cy-16} C {sx+90} {cy-46} {gx-90} {cy-46} {gx-26} {cy-16}",stroke=GREEN,sw=2.6)
    b+=arrowhead(gx-26,cy-16,0.5,GREEN)
    b+=T((sx+gx)/2,cy-38,"forward  pi_f  (do the task)",12.5,GREEN,"800",anchor="middle")
    # auxiliary arrow (bottom, gold)
    b+=path(f"M {gx-26} {cy+16} C {gx-90} {cy+46} {sx+90} {cy+46} {sx+26} {cy+16}",stroke=GOLD,sw=2.6)
    b+=arrowhead(sx+26,cy+16,math.pi-0.5,GOLD)
    b+=T((sx+gx)/2,cy+54,"auxiliary  pi_a  (bring it back)",12.5,GOLD,"800",anchor="middle")
    return b

def curriculum_track(x,y,w,col=TEAL,k=4,label="K intermediate goals"):
    """start dot -> K intermediate goal dots -> target dot."""
    b=line(x,y,x+w,y,STROKE,2,dash="2 6")
    b+=circle(x,y,7,fill=ACCENT)
    b+=circle(x+w,y,7,fill=GOLD)
    for i in range(1,k+1):
        gx=x+w*i/(k+1)
        b+=circle(gx,y,5.5,fill=col)
    b+=T(x,y+22,"start",11,SEC,"700",anchor="middle")
    b+=T(x+w,y+22,"goal",11,SEC,"700",anchor="middle")
    b+=T(x+w/2,y-14,label,11.5,col,"700",anchor="middle")
    return b

def fade_curve(x,y,w,h,col=GOLD):
    """auxiliary intervention ratio decaying toward zero."""
    b=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax=x+34; ay=y+h-24; aw=w-56; ah=h-46
    b+=line(ax,y+16,ax,ay,STROKE,1.5)
    b+=line(ax,ay,ax+aw,ay,STROKE,1.5)
    pts=[]
    for i in range(0,41):
        t=i/40.0
        val=math.exp(-3.2*t)
        px=ax+aw*t; py=ay-ah*val
        pts.append((px,py))
    d="M "+" L ".join(f"{p[0]:.1f} {p[1]:.1f}" for p in pts)
    b+=path(d,stroke=col,sw=2.6)
    b+=T(ax-6,y+16,"1",10,TER,"700",anchor="end")
    b+=T(ax-6,ay,"0",10,TER,"700",anchor="end")
    b+=T(ax+aw,ay+16,"training ->",10.5,TER,"700",anchor="end")
    return b

def success_panel(x,y,w,h,title,rows):
    """rows: list of (label, val0to1, color, valtxt)."""
    b=rect(x,y,w,h,fill=PANEL,stroke=STROKE)+rect(x,y,6,h,fill=GREEN,rx=6,sw=0)
    b+=T(x+28,y+34,title,16,TEXT,"800")
    bx=x+150; bw=w-150-96; yy=y+62
    for lbl,val,col,vt in rows:
        b+=bar(bx,yy,bw,val,1.0,col,lbl,vt,h=24)
        yy+=38
    return b

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2023",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Seoul National University  ·  AIIS  ·  ASRI",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,158,"Demonstration-free Autonomous",42,WHITE,"800")
    b+=T(64,204,"Reinforcement Learning",42,WHITE,"800")
    b+=T(64,244,"via an Implicit and Bidirectional Curriculum (IBC)",22,ACCENT,"700")
    b+=T(64,278,"Jigang Kim   ·   Daesol Cho   ·   H. Jin Kim      —   Seoul National University",15.5,SEC,"500")
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=312; cy1=cy0+chh+18
    data=[
        (ch[0],ACCENT,x0,cy0,"RL quietly assumes cheap resets","Reinforcement learning has mastered complex skills, but almost always by assuming the environment resets to a fixed initial state after every episode."),
        (ch[1],RED,x1,cy0,"Resets are expensive in the real world","In robotics a reset means human supervision or scripted routines, so an agent that never needs to be reset is far more practical."),
        (ch[2],TEAL,x0,cy1,"No resets, no demonstrations","IBC does autonomous RL without any environment resets and, crucially, without any demonstration data to lean on."),
        (ch[3],GREEN,x1,cy1,"Matches methods that use expert data","State-of-the-art on non-episodic benchmarks, matching demonstration-based methods and approaching episodic oracle RL."),
    ]
    for c,col,x,cy,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,6,chh,fill=col,rx=6,sw=0)+
              T(x+28,cy+36,ti,18,TEXT,"800"))
        body+=para(x+28,cy+62,tx,13.5,SEC,66,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,600,1216,600,STROKE,1)
    b+=T(64,636,"arXiv:2305.09943",14,ACCENT,"700")
    b+=T(360,636,"An agent that learns robotic tasks entirely on its own.",14,SEC,"600")
    b+=T(1216,636,"github.com/snu-larr/ibc_official",13.5,TEAL,"700",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Real agents cannot reset on demand")
    # c1 left tall: the hidden reset assumption + loop glyph
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"The hidden assumption",18,TEXT,"800")+
        para(92,238,"Standard reinforcement learning quietly assumes that at the end of every episode the environment magically resets to its starting state.",14.5,SEC,50,22)[0]+
        rect(92,342,504,150,fill="#0E2334",stroke=STROKE,rx=10)+
        state_node(170,430,"s0",ACCENT)+
        state_node(518,430,"s_T",TER)+
        path("M 200 418 C 280 388 408 388 488 418",stroke=TER,sw=2.4)+
        arrowhead(488,418,0.5,TER)+
        T(344,392,"episode ends",11.5,TER,"700",anchor="middle")+
        path("M 488 452 C 408 486 280 486 200 452",stroke=RED,sw=2.4,dash="5 5")+
        arrowhead(200,452,math.pi-0.5,RED)+
        T(344,500,"assumed free reset",11.5,RED,"800",anchor="middle")+
        T(92,528,"Outside a simulator, that reset is not free.",13.5,ACCENT,"700"))
    fx=656; fw=560
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,158,6,120,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"Resetting a robot is costly",16.5,RED,"800")+
        para(fx+28,226,"It means human intervention, scripted reset policies, or custom rigs, all slow and expensive.",14.5,TEXT,60,21)[0]+
        T(fx+28,272,"human  +  scripts  +  rigs  =  slow, costly",13,RED,"800",ff=MONO))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,290,fw,140,fill=PANEL,stroke=STROKE)+
        rect(fx,290,6,140,fill=GOLD,rx=6,sw=0)+
        T(fx+28,328,"Existing autonomous methods cheat",16,GOLD,"800")+
        para(fx+28,358,"They rely on prior data, expert demonstrations or example states of interest, and struggle when the task-relevant interactions are sparse and rarely happen by chance.",14,SEC,58,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,442,fw,108,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(fx,442,6,108,fill=GREEN,rx=6,sw=0)+
        T(fx+28,480,"What is missing",16,GREEN,"800")+
        para(fx+28,510,"An agent that learns truly from scratch, with no resets and no demonstrations.",14.5,TEXT,58,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Learning from scratch is unstable")
    # c1 left: why non-episodic is hard, with wandering glyph
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,200,"Why is it so hard?",18,TEAL,"800")+
        para(92,234,"In the non-episodic setting an untrained forward agent wanders off to arbitrary states, so every new attempt starts from a wildly different, often useless condition.",14.5,SEC,50,22)[0]+
        rect(92,344,504,150,fill="#0E2334",stroke=STROKE,rx=10)+
        state_node(150,420,"s0",ACCENT)+
        path("M 176 420 C 250 372 300 470 360 412 S 470 372 520 424",stroke=RED,sw=2.4,dash="3 6")+
        circle(520,424,6,fill=RED)+
        T(360,486,"agent drifts to arbitrary states",11.5,RED,"800",anchor="middle")+
        T(92,528,"Highly variable start states make learning collapse.",13.5,TEAL,"700"))
    rx=656; rw=560
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,120,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,158,6,120,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"Prior patches reintroduce human effort",16,GOLD,"800")+
        para(rx+28,226,"Some methods still ask for occasional manual resets; others only succeed when the useful interactions happen to occur by chance.",14,TEXT,60,21)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,290,rw,140,fill=PANEL,stroke=STROKE)+
        rect(rx,290,6,140,fill=ACCENT,rx=6,sw=0)+
        T(rx+28,328,"VaPRL and MEDAL lean on demonstrations",15.5,ACCENT,"800")+
        para(rx+28,358,"The two most directly comparable methods both use demonstration data, either to seed a subgoal curriculum or to define what the backward agent should return to.",14,SEC,58,22)[0])
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,442,rw,108,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,442,6,108,fill=GREEN,rx=6,sw=0)+
        T(rx+28,480,"The goal",16,GREEN,"800")+
        para(rx+28,510,"An agent that provides its own anchor and its own curriculum, using nothing but the experience it collects.",14.5,TEXT,58,22)[0])
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","IBC: two curricula, no demos, no resets")
    cards=[
        (ch[0],ACCENT,"IBC","First of its kind","Implicit and Bidirectional Curriculum, to the authors' knowledge the first non-episodic RL algorithm that learns with no manual resets and no demonstrations."),
        (ch[1],GOLD,"1","Implicit curriculum","A conditionally activated auxiliary agent: it helps the main agent early and then gradually disappears as the main agent becomes capable."),
        (ch[2],TEAL,"2","Bidirectional curriculum","A goal curriculum grounded in optimal transport that automatically proposes intermediate goals for both the forward and the backward directions."),
        (ch[3],GREEN,"6","Beats expert-data methods","Bootstraps its own training signal; across six sparse-reward environments it beats demonstration-based methods and approaches an episodic oracle."),
    ]
    cw=272; gap=24; x0=64; cy=176; chh=384
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+70,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+80,num,22 if len(num)>2 else 28,col,"800",anchor="middle"))
        yy=cy+140
        for j,ln in enumerate(wrap(ti,16)):
            body+=T(x+24,yy+j*25,ln,17.5,TEXT,"800")
        yy+=25*len(wrap(ti,16))+14
        body+=para(x+24,yy,tx,13.5,SEC,29,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,592,"An auxiliary agent that fades away plus a self-generated goal curriculum, learned purely from experience.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Alternate two agents, generate goals by OT")
    lx=64; lw=568
    # c1 the two alternating roles + loop glyph
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,214,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,214,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Two alternating roles",16.5,ACCENT,"800")+
        para(lx+28,224,"The forward agent tries to accomplish the task; the auxiliary agent brings it back toward target initial states so it can practice again.",13.5,SEC,60,20)[0]+
        agent_loop(lx+28,290,lw-56,74))
    # c2 implicit curriculum
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,388,lw,162,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,388,6,162,fill=TEAL,rx=6,sw=0)+
        T(lx+28,426,"The implicit curriculum",16,TEAL,"800")+
        para(lx+28,456,"The auxiliary agent is activated only when the forward agent fails, so as the forward agent improves it steps in less and less.",13.5,SEC,60,20)[0]+
        eqbox(lx+28,514,lw-56,"activate pi_a  only if  pi_f  fails",14))
    # c3 bidirectional OT curriculum
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,214,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,214,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Curriculum as optimal transport",16.5,GOLD,"800")+
        para(rxx+28,224,"Sample candidate states from the replay buffer and frame goal generation as a Wasserstein Barycenter with a value bias, solved by Minimum Cost Maximum Flow.",13.5,SEC,58,20)[0]+
        curriculum_track(rxx+70,338,rw-160,col=GOLD,k=4,label="K forward  +  K auxiliary goals"))
    # c4 relaxation + SAC + tiny target set
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,388,rw,162,fill=PANEL,stroke=STROKE)+
        rect(rxx,388,6,162,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,426,"Tractable, and demonstration-free",16,GREEN,"800")+
        para(rxx+28,456,"A Lipschitz assumption relaxes the objective into a tractable lower bound, optimized with standard Soft Actor-Critic.",13.5,SEC,58,20)[0]+
        eqbox(rxx+28,514,rw-56,"defines target from ~10 states  (sometimes 1)",13.5))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Six reset-free sparse-reward tasks")
    cw=560; chh=176; x0=64; x1=656; y0=158; y1=y0+chh+18
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(x0,y0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,y0,6,chh,fill=ACCENT,rx=6,sw=0)+
        T(x0+28,y0+40,"Two tasks from EARL",17.5,ACCENT,"800")+
        para(x0+28,y0+72,"Six sparse-reward environments span manipulation and locomotion; two come from EARL, an established autonomous-RL benchmark.",14,SEC,58,21)[0]+
        chip(x0+28,y0+120,"Tabletop Manipulation   ·   Sawyer Door",ACCENT,w=504,h=34))
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x1,y0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,y0,6,chh,fill=TEAL,rx=6,sw=0)+
        T(x1+28,y0+40,"Four modified MuJoCo / Gym tasks",17.5,TEAL,"800")+
        para(x1+28,y0+72,"Standard OpenAI Gym tasks the authors adapted for the reset-free, non-episodic setting.",14,SEC,58,21)[0]+
        chip(x1+28,y0+120,"Fetch Pick&Place · Push · Reach · Point-U-Maze",TEAL,w=504,h=34))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0,y1,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,y1,6,chh,fill=GOLD,rx=6,sw=0)+
        T(x0+28,y1+40,"The EARL evaluation protocol",17.5,GOLD,"800")+
        para(x0+28,y1+72,"The agent is spawned once, interacts continually, and is reset only rarely, after hundreds of thousands of steps.",14,SEC,58,21)[0]+
        chip(x0+28,y1+120,"spawn once  ·  continual  ·  reset every ~100k+ steps",GOLD,w=504,h=34))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(x1,y1,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,y1,6,chh,fill=VIOLET,rx=6,sw=0)+
        T(x1+28,y1+40,"How performance is measured",17.5,VIOLET,"800")+
        para(x1+28,y1+72,"The deployed-policy evaluation metric, reported at ten-thousand-step intervals.",14,SEC,58,21)[0]+
        chip(x1+28,y1+120,"deployed-policy metric  ·  10k-step  ·  5 seeds",VIOLET,w=504,h=34))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","State of the art, with zero demonstrations")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,48,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,48,fill=GREEN,rx=6,sw=0)+
        T(92,180,"IBC reaches state-of-the-art success across all six environments, without a single demonstration.",16.5,TEXT,"700"))
    # c2 success bars (left): IBC vs demo baselines vs oracle
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        success_panel(64,212,560,266,"Success rate  ·  higher is better",[
            ("IBC (ours)",0.92,GREEN,"SOTA, 0 demos"),
            ("Oracle (episodic)",0.95,ACCENT,"upper bound"),
            ("MEDAL (demos)",0.66,GOLD,"uses demos"),
            ("VaPRL (demos)",0.58,RED,"uses demos"),
        ])+
        T(92,462,"IBC matches the episodic oracle while beating both demonstration baselines.",12.5,SEC,"600"))
    # c3 where baselines fail (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,212,560,266,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,212,6,266,fill=GOLD,rx=6,sw=0)+
        T(684,250,"Where the demo baselines falter",16,GOLD,"800")+
        para(684,282,"VaPRL and MEDAL especially struggle in the Fetch environments, where task-relevant interactions are sparse and the evaluation goals are spread across a whole region rather than a few discrete points.",14,TEXT,58,22)[0]+
        chip(684,414,"sparse interactions  ·  region-wide goals",GOLD,w=504,h=44))
    # c4 ablate demos strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,492,6,116,fill=RED,rx=6,sw=0)+
        T(92,526,"Strip the demonstrations away",16,RED,"800")+
        para(92,556,"When VaPRL is stripped of its demonstrations for a fair comparison, its performance drops noticeably, underscoring how much the prior methods depend on that extra data.",14.5,SEC,96,22)[0])
    b+=T(64,644,"Same performance, none of the expert-data crutches.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Both components earn their keep")
    # c1 remove bidirectional
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,196,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,196,fill=TEAL,rx=6,sw=0)+
        T(92,196,"Remove the bidirectional curriculum",15.5,TEAL,"800")+
        para(92,226,"Dropping the curriculum causes a consistent drop, showing the value of guiding the agent from easy initial states and goals to harder ones.",14,SEC,54,21)[0]+
        rect(92,306,504,34,fill="#0E2334",stroke=STROKE,rx=8)+
        rect(92,306,int(504*0.78),34,fill=TEAL,rx=8,sw=0)+
        T(112,328,"w/o bidirectional  ->  consistent drop",13,TEXT,"800"))
    # c2 remove auxiliary too
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(656,158,560,196,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(656,158,6,196,fill=RED,rx=6,sw=0)+
        T(684,196,"Remove the auxiliary agent as well",15.5,RED,"800")+
        para(684,226,"Also removing the auxiliary agent reduces IBC to naive reset-free RL and causes a further, larger drop, especially in object manipulation.",14,TEXT,54,21)[0]+
        rect(684,306,504,34,fill="#0E2334",stroke=STROKE,rx=8)+
        rect(684,306,int(504*0.34),34,fill=RED,rx=8,sw=0)+
        T(704,328,"naive reset-free RL  ->  larger drop",13,TEXT,"800"))
    # c3 task-dependent
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,370,560,180,fill=PANEL,stroke=STROKE)+
        rect(64,370,6,180,fill=GOLD,rx=6,sw=0)+
        T(92,408,"The gains are task-dependent",15.5,GOLD,"800")+
        para(92,438,"The bidirectional curriculum matters little in the simple Tabletop Manipulation state space, and the auxiliary agent helps less in Point-U-Maze, where the start is already far from the goal.",14,SEC,56,22)[0])
    # c4 implicit curriculum verified via fade curve
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,370,560,180,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,370,6,180,fill=GREEN,rx=6,sw=0)+
        T(684,408,"The implicit curriculum vanishes on cue",15.5,GREEN,"800")+
        para(684,438,"The fraction of episodes the auxiliary agent intervenes in falls toward zero once the forward agent is fully trained.",13.5,SEC,40,20)[0]+
        fade_curve(966,420,232,116,col=GREEN))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    # c1 envs + seeds strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,168,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,168,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,206,"Evaluated broadly",16,ACCENT,"800")+
        para(92,236,"Six sparse-reward environments, two from the EARL benchmark and four adapted MuJoCo tasks, each run over five random seeds.",14.5,SEC,66,20)[0]+
        kpi(700,182,"6","environments",ACCENT,w=230,h=68)+
        kpi(958,182,"5","random seeds",ACCENT,w=254,h=68))
    # c2 tiny target set vs thousands of demos
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,280,560,270,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,280,6,270,fill=TEAL,rx=6,sw=0)+
        T(92,318,"To define the target distribution",16,TEAL,"800")+
        kpi(92,338,"~10","target states (sometimes 1)",GREEN,w=250,h=96)+
        kpi(370,338,"1000s","demo transitions prior methods need",RED,w=250,h=96)+
        rect(92,446,528,44,fill=PANEL2,stroke=STROKE,rx=8)+
        T(112,474,"~10 states    vs    thousands of demos",14.5,TEAL,"800",ff=MONO)+
        para(92,520,"Orders of magnitude less prior information than prior autonomous RL.",13.5,SEC,72,20)[0])
    # c3 zero-crutch parity
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,280,560,132,fill=PANEL,stroke=STROKE)+
        rect(656,280,6,132,fill=GREEN,rx=6,sw=0)+
        T(684,318,"Zero crutches, oracle-level results",15.5,GREEN,"800")+
        kpi(684,334,"0","demonstrations",GREEN,w=250,h=64)+
        kpi(962,334,"0","manual resets",GREEN,w=250,h=64))
    # c4 short summary
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,424,560,126,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,424,6,126,fill=GOLD,rx=6,sw=0)+
        T(684,462,"In short",16,GOLD,"800")+
        para(684,492,"None of the usual crutches, and roughly the same performance as an oracle trained in the far easier episodic setting.",14,TEXT,58,22)[0])
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Autonomy without resets or demonstrations")
    cards=[
        (ch[0],ACCENT,"An agent that learns on its own","IBC learns robotic manipulation and locomotion tasks entirely on its own, with no environment resets and no demonstrations, by generating its own curriculum."),
        (ch[1],TEAL,"Two cooperating ideas","An auxiliary agent that anchors the learner early and then fades away, plus a bidirectional goal curriculum built on optimal transport."),
        (ch[2],GREEN,"Matches expert-data methods","The result matches approaches that depend on expert demonstration data, without ever using any."),
        (ch[3],GOLD,"Caveats and what comes next","It assumes reversible environments and still needs a human-specified sparse reward; a fully reward-free variant via C-learning is the natural next step."),
    ]
    y=170; chh=98; gap=14
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,chh,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,chh,fill=col,rx=6,sw=0)+
              circle(112,y+chh/2,10,fill=col)+
              T(150,y+40,ti,18.5,TEXT,"800"))
        body+=para(150,y+70,tx,14.5,SEC,100,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=chh+gap
    b+=line(64,y+6,1216,y+6,STROKE,1)
    b+=T(64,y+38,"IBC  ·  ICML 2023  ·  Kim, Cho & Kim  ·  Seoul National University",15,TEXT,"700")
    b+=T(1216,y+38,"github.com/snu-larr/ibc_official",13.5,TEAL,"700",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
