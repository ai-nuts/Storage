#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 074
(Deep Demonstration Tracing: Learning Generalizable Imitator Policy for Runtime
Imitation from a Single Demonstration / DDT - ICML 2024, Nanjing University et al.).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: an imitator that TRACES a single demonstration - identify the
relevant demonstrated states, analyze the expert there, and trace back onto the
path after detouring around an unforeseen obstacle."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1A2B"; PANEL="#122A42"; PANEL2="#173453"; STROKE="#2A4D6E"
ACCENT="#3E9BFF"; TEAL="#33D6C0"; GOLD="#F4C24C"; RED="#F2685C"; GREEN="#46C98B"
VIOLET="#9C86F0"
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

def polygon(pts,fill=ACCENT,stroke=None,sw=1.0):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polygon points="{p}" fill="{fill}"{st}/>'

def arrow(x1,y1,x2,y2,color=STROKE,sw=1.5,head=6):
    ang=math.atan2(y2-y1,x2-x1)
    hx,hy=x2-head*math.cos(ang),y2-head*math.sin(ang)
    p1=(hx-head*math.cos(ang-0.5),hy-head*math.sin(ang-0.5))
    p2=(hx-head*math.cos(ang+0.5),hy-head*math.sin(ang+0.5))
    return (line(x1,y1,x2,y2,color,sw)+
            polygon([(x2,y2),p1,p2],fill=color))

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

def stat(x,y,w,h,num,lbl,col):
    ns=min(30,h*0.34)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44,col=TEXT):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,col,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
def mazefig(x,y,s=1.0,detour=True):
    """The VPAM signature: a demonstrated route (teal dashed) from start to goal,
    an unforeseen rectangular obstacle (red) dropped on the path, and the DDT
    agent tracing a detour (accent) that rejoins the demonstration."""
    w=int(232*s); h=int(180*s)
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    # faint maze grid
    for gx in range(1,6):
        out+=line(x+gx*w/6,y+8,x+gx*w/6,y+h-8,STROKE,0.5)
    for gy in range(1,4):
        out+=line(x+8,y+gy*h/4,x+w-8,y+gy*h/4,STROKE,0.5)
    sx,sy=x+int(24*s),y+h-int(30*s)          # start (blue)
    gx2,gy2=x+w-int(26*s),y+int(30*s)        # goal (green)
    # demonstrated route (teal dashed) via a mid waypoint
    mx,my=x+w*0.44,y+h*0.44
    demo=[(sx,sy),(x+w*0.30,y+h*0.62),(mx,my),(x+w*0.66,y+h*0.30),(gx2,gy2)]
    out+=poly(demo,stroke=TEAL,sw=2.2,dash="6 5")
    # obstacle on the path
    ox,oy=int(mx-14*s),int(my-2*s)
    out+=rect(ox,oy,int(30*s),int(20*s),fill=RED,rx=3,sw=0)
    if detour:
        det=[(mx-6,my+16),(mx-22,my+2),(mx-14,my-20),(mx+18,my-20),(mx+22,my-2)]
        out+=poly([(x+w*0.30,y+h*0.62)]+det+[(x+w*0.66,y+h*0.30)],stroke=ACCENT,sw=2.6)
    out+=circle(sx,sy,6,fill=ACCENT)
    out+=rect(gx2-6,gy2-6,12,12,fill=GREEN,rx=2,sw=0)
    out+=T(sx+2,sy+16,"start",9,SEC,"700",anchor="middle")
    out+=T(gx2,gy2-12,"goal",9,GREEN,"800",anchor="middle")
    out+=T(x+w/2,y+h+0,"",9,SEC,"600",anchor="middle")
    return out

def tracestages(x,y,w,h):
    """The human three-stage decision process DDT imitates: identify the relevant
    demonstrated states, analyze how the expert behaved, then trace back on."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    stages=[("Identify","relevant demo states",ACCENT),
            ("Analyze","expert behavior there",GOLD),
            ("Trace","back onto the path",GREEN)]
    gap=10; bw=(w-28-2*gap)/3.0; cy=y+h/2
    cx=x+14
    for i,(nm,sub,col) in enumerate(stages):
        out+=rect(cx,y+18,bw,h-34,fill=PANEL2,stroke=col,rx=8,sw=1.4)
        out+=circle(cx+bw/2,y+42,10,fill="none",stroke=col,sw=2.2)
        out+=T(cx+bw/2,y+47,str(i+1),12,col,"800",anchor="middle")
        out+=T(cx+bw/2,y+74,nm,13,TEXT,"800",anchor="middle")
        for j,ln in enumerate(wrap(sub,15)):
            out+=T(cx+bw/2,y+92+j*13,ln,10,SEC,"600",anchor="middle")
        if i<2:
            out+=arrow(cx+bw+1,cy,cx+bw+gap-1,cy,col,1.8,6)
        cx+=bw+gap
    return out

def stagebar(x,y,w,h=42):
    """Compact one-line identify -> analyze -> trace strip (used where a full
    tracestages card does not fit)."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    stages=[("1","Identify",ACCENT),("2","Analyze",GOLD),("3","Trace",GREEN)]
    seg=w/3.0
    for i,(n,nm,col) in enumerate(stages):
        cx=x+i*seg
        out+=circle(cx+20,y+h/2,9,fill="none",stroke=col,sw=2)
        out+=T(cx+20,y+h/2+4,n,11,col,"800",anchor="middle")
        out+=T(cx+36,y+h/2+5,nm,13,TEXT,"700")
        if i<2: out+=T(cx+seg-6,y+h/2+5,"->",12,SEC,"800",anchor="middle")
    return out

def demotransformer(x,y,w,h):
    """The demonstration transformer (Fig 3): the agent's current state is the
    query; the demonstration's states/actions are keys and values. Attention
    weighting identifies relevant demo states, a point-wise product analyzes the
    expert, and the result is combined with the current state to trace an action."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    # query (current state) at far left
    qcx=x+34; qcy=y+h/2
    out+=circle(qcx,qcy,15,fill=ACCENT)
    out+=T(qcx,qcy+5,"q",13,BG,"800",anchor="middle",ff=MONO)
    out+=T(qcx,qcy-24,"query",9.5,SEC,"700",anchor="middle")
    out+=T(qcx,qcy+30,"state s_t",9.5,SEC,"700",anchor="middle")
    # demonstration states as keys/values (stacked)
    kx=x+w*0.30
    keys=[("se_0",TEAL),("se_i",GOLD),("se_t",RED)]
    kcen=[]
    for i,(nm,col) in enumerate(keys):
        ky=y+22+i*((h-44)/2.0)
        kcen.append(ky+10)
        out+=line(qcx+16,qcy,kx-6,ky+10,STROKE,1.2)
        out+=T(kx-16,ky+15,"·",15,SEC,"800",anchor="middle")
        out+=rect(kx,ky,60,20,fill=PANEL2,stroke=col,rx=5,sw=1.3)
        out+=T(kx+30,ky+14,nm,10.5,col,"800",anchor="middle",ff=MONO)
    out+=T(kx+30,y+12,"demo keys/values",9,SEC,"700",anchor="middle")
    # attention weights (identify) then point-wise (analyze)
    wx=x+w*0.565
    out+=T(wx+40,y+13,"attn w (identify)",9.5,ACCENT,"800",anchor="middle")
    ww=[(0.20,TEAL),(0.58,GOLD),(0.22,RED)]
    for i,((val,col),kcy) in enumerate(zip(ww,kcen)):
        by=y+24+i*((h-46)/2.0)
        bw=int(92*val)+8
        out+=line(kx+60,kcy,wx-4,by+8,STROKE,1.0)
        out+=rect(wx,by,bw,16,fill=col,rx=4,sw=0)
    # trace: combine -> action
    px=x+w-46
    out+=arrow(wx+108,qcy,px-20,qcy,STROKE,1.4,7)
    out+=T((wx+108+px)/2,qcy-8,"trace",9,GREEN,"800",anchor="middle")
    out+=circle(px,qcy,20,fill="none",stroke=GREEN,sw=2.4)
    out+=T(px,qcy+6,"a",15,GREEN,"800",anchor="middle",ff=MONO)
    out+=T(px,qcy-28,"action",9.5,GREEN,"800",anchor="middle")
    return out

def raysfig(cx,cy,s=1.0):
    """The VPAM local observation: eight rays cast from the point agent give
    short-range local views of nearby walls/obstacles."""
    r=int(46*s); out=""
    for k in range(8):
        ang=k*math.pi/4.0
        ex,ey=cx+r*math.cos(ang),cy+r*math.sin(ang)
        out+=line(cx,cy,ex,ey,GOLD,1.3,dash="3 3")
        out+=circle(ex,ey,2.4,fill=GOLD)
    out+=circle(cx,cy,7,fill=ACCENT)
    out+=T(cx,cy+r+16,"8 rays",10,SEC,"700",anchor="middle")
    return out

def groupbars(x,y,w,h,title=""):
    """VPAM success rate under three settings for the three headline methods:
    DDT stays high and degrades little; baselines collapse under obstacles."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    if title: out+=T(x+14,y+20,title,11.5,TEXT,"800")
    groups=[("seen",[("DDT",0.86,GREEN)]),
            ("no-obst",[("DDT",0.84,GREEN)]),
            ("obstacle",[("DDT",0.73,GREEN),("DCRL",0.57,GOLD),("Trans4OSIL",0.16,RED)])]
    ax0=x+40; ax1=x+w-14; ay0=y+h-30; ay1=y+30
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    # simple: three clusters
    gslot=(ax1-ax0)/3.0
    for gi,(gname,bars) in enumerate(groups):
        gx0=ax0+gi*gslot+10
        bw=(gslot-24)/max(1,len(bars))
        for bi,(nm,v,col) in enumerate(bars):
            bx=gx0+bi*bw
            bh=(ay0-ay1)*v
            out+=rect(bx,ay0-bh,bw-4,bh,fill=col,rx=3,sw=0)
            out+=T(bx+(bw-4)/2,ay0-bh-5,f"{v:.2f}",9.5,col,"800",anchor="middle")
            if len(bars)>1:
                out+=T(bx+(bw-4)/2,ay0+12,nm,8.5,SEC,"600",anchor="middle")
        out+=T(gx0+(gslot-24)/2,ay0+24,gname,10,TER,"700",anchor="middle")
    return out

def degradebars(x,y,w,h):
    """Robustness: performance retention from training to unforeseen obstacles.
    DDT drops only 15%, far less than the 20/33/52% of the baselines."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    vals=[("DDT",15,GREEN),("b1",20,ACCENT),("b2",33,GOLD),("b3",52,RED)]
    ax0=x+18; ax1=x+w-14; ay0=y+h-26; top=y+28
    slot=(ax1-ax0)/len(vals)
    for i,(nm,v,col) in enumerate(vals):
        cx=ax0+i*slot+slot/2
        bh=(ay0-top)*(v/60.0)
        out+=rect(cx-slot*0.3,ay0-bh,slot*0.6,bh,fill=col,rx=3,sw=0)
        out+=T(cx,ay0-bh-6,f"-{v}%",10.5,col,"800",anchor="middle")
        out+=T(cx,ay0+14,nm,9,SEC,"600",anchor="middle")
    out+=T(x+14,y+18,"drop: train -> obstacles",10.5,SEC,"800")
    return out

def vsbars(x,y,w,h,title,ddt,base,baselab,fmt="{:.2f}"):
    """Two-bar comparison: DDT vs the strongest baseline on one benchmark."""
    out=rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=10)
    ay0=y+h-24; top=y+30; span=ay0-top
    mx=max(ddt,base,0.01)
    pairs=[("DDT",ddt,GREEN),(baselab,base,SEC)]
    slot=(w-40)/2.0
    for i,(lb,v,c) in enumerate(pairs):
        cx=x+20+slot*i+slot/2
        bh=max(6,span*(v/mx))
        out+=rect(cx-36,ay0-bh,72,bh,fill=c,rx=5,sw=0)
        out+=T(cx,ay0-bh-8,fmt.format(v),14,c,"800",anchor="middle")
        out+=T(cx,ay0+16,lb,11,SEC,"700",anchor="middle")
    return out

def ablbars(x,y,w,h):
    """Ablation: full DDT vs a standard transformer vs no OSIL reward - each
    removal drops asymptotic performance, showing both parts are necessary."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    vals=[("DDT",0.84,GREEN),("std. Trans.",0.55,GOLD),("no OSIL rew.",0.34,RED)]
    ax0=x+18; ax1=x+w-14; ay0=y+h-28; top=y+34
    slot=(ax1-ax0)/len(vals)
    for i,(nm,v,col) in enumerate(vals):
        cx=ax0+i*slot+slot/2
        bh=(ay0-top)*v
        out+=rect(cx-slot*0.28,ay0-bh,slot*0.56,bh,fill=col,rx=3,sw=0)
        out+=T(cx,ay0-bh-6,f"{v:.2f}",10,col,"800",anchor="middle")
        for j,ln in enumerate(wrap(nm,11)):
            out+=T(cx,ay0+12+j*11,ln,8.5,SEC,"600",anchor="middle")
    out+=T(x+14,y+18,"asymptotic performance",10.5,SEC,"800")
    return out

def slowcurve(x,y,w,h):
    """Removing the dense OSIL reward leaves only a sparse ending reward, so
    learning is much slower than the full DDT reward shaping."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    ax0=x+30; ax1=x+w-14; ay0=y+h-22; ay1=y+18
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    def curve(final,k):
        return [(ax0+(t/100.0)*(ax1-ax0), ay0-final*(1-math.exp(-k*t/100.0))*(ay0-ay1))
                for t in range(0,101,5)]
    out+=poly(curve(0.40,1.4),stroke=RED,sw=2.4,dash="6 5")
    out+=poly(curve(0.86,4.2),stroke=GREEN,sw=2.8)
    out+=T(ax1,ay0-0.86*(ay0-ay1)-6,"full OSIL",9.5,GREEN,"800",anchor="end")
    out+=T(ax1,ay0-4,"sparse only",9.5,RED,"800",anchor="end")
    out+=T(ax0-2,ay1+2,"success",9,TER,"600",anchor="end")
    out+=T(ax1,ay0+14,"steps ->",9,TER,"600",anchor="end")
    return out

def scalecurve(x,y,w,h):
    """Scaling up: DDT's asymptotic performance grows roughly log-linearly with
    both data volume and model size, hinting at a generalist backbone."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    ax0=x+34; ax1=x+w-16; ay0=y+h-24; ay1=y+18
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    pts=[(ax0+i*(ax1-ax0)/5, ay0-(0.18+0.15*i)*(ay0-ay1)) for i in range(6)]
    out+=poly(pts,stroke=TEAL,sw=2.8)
    for px,py in pts: out+=circle(px,py,3,fill=TEAL)
    out+=T(ax0-2,ay1+2,"perf",9,TER,"600",anchor="end")
    out+=T(ax1,ay0+14,"log(params / data) ->",9,TER,"600",anchor="end")
    return out

def envrow(x,y,w,items):
    gap=14; bw=(w-(len(items)-1)*gap)/len(items); out=""
    for i,(nm,col,sub) in enumerate(items):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,60,fill=PANEL2,stroke=col,rx=10,sw=1.5)
        out+=rect(bx,y,bw,5,fill=col,rx=3,sw=0)
        out+=T(bx+bw/2,y+32,nm,14.5,TEXT,"800",anchor="middle")
        out+=T(bx+bw/2,y+50,sub,11,SEC,"600",anchor="middle")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2024",14,ACCENT,"800",ls="2")
    b+=T(1216,72,"One-Shot Imitation  ·  Runtime Robustness  ·  Meta-RL",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"DDT",44,WHITE,"800")
    b+=T(64,196,"Deep Demonstration Tracing",23,ACCENT,"800")
    b+=T(64,224,"Generalizable One-Shot Imitation under Runtime Change",23,ACCENT,"800")
    b+=mazefig(1044,120,1.0)
    b+=T(64,258,"Xiong-Hui Chen, Junyin Ye, Yang Yu, Zongzhang Zhang, et al.",13.5,SEC,"500")
    b+=T(64,280,"Nanjing University   ·   Polixir Technologies   ·   NUDT",12.5,TER,"600")
    cw=368; gap=24; x0=64; cy=306; chh=224
    data=[
        (ch[0],ACCENT,x0,"The world changes after the demo",
         "One-shot imitation learning must act from a single demonstration, but the real world is dynamic: after the demo is given, the environment can change at runtime."),
        (ch[1],TEAL,x0+cw+gap,"Trace, do not replay",
         "Deep Demonstration Tracing, DDT, lets an imitator adaptively trace the right states in a single demonstration while recovering from unforeseen obstacles."),
        (ch[2],GREEN,x0+2*(cw+gap),"Transformer + meta-RL",
         "A purpose-built demonstration transformer trained by meta-reinforcement learning beats prior one-shot imitation on a new maze benchmark and robotics tasks."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+44,7,fill=col))
        body+=para(x+46,cy+50,ti,17.5,TEXT,26,22,"800")[0]
        body+=para(x+26,cy+100,tx,13.5,SEC,42,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,556,1216,556,STROKE,1)
    b+=T(64,592,"arXiv:2408.05285",14,ACCENT,"700")
    b+=T(320,592,"github.com/xionghuichen/Deep-Demonstration-Tracing",13.5,SEC,"600")
    b+=T(1216,592,"Robust one-shot imitation from a single demonstration.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","One demo, then the world moves")
    # c1 left tall: the one-shot setting
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Act from a single demo",17.5,TEXT,"800")+
        para(92,238,"One-shot imitation learning asks an agent to carry out a task after seeing just a single demonstration. It works well when deployment looks like the demonstration.",14,SEC,42,22)[0]+
        rect(92,360,344,138,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,390,"the hidden assumption",12.5,TER,"700")+
        eqbox(112,406,304,"deploy  ==  demonstration",12.5,h=40,col=ACCENT)+
        T(112,486,"but the real world is dynamic",12,SEC,"600"))
    fx=500; fw=716
    # c2 runtime change breaks replay
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=TEAL,rx=6,sw=0)+
        T(fx+28,196,"Runtime change breaks blind replay",16.5,TEAL,"800")+
        para(fx+28,226,"After the demonstration is provided, an unexpected obstacle can appear, or a grasped object can slip, pushing the agent into states the demo never covered.",14,SEC,50,21)[0]+
        mazefig(fx+fw-214,168,0.72))
    # c3 prior methods rigid to change
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"Prior methods excel only when stationary",16,GOLD,"800")+
        para(fx+28,392,"Traditional one-shot imitation methods shine in stationary settings, yet their ability to handle these unforeseen runtime changes is limited and rarely studied.",14.5,TEXT,88,24)[0])
    # c4 the gap this paper attacks
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=GREEN,rx=6,sw=0)+
        T(fx+28,482,"The gap: robust OSIL at runtime",16,GREEN,"800")+
        para(fx+28,512,"This paper focuses squarely on that gap - making one-shot imitation robust when the environment changes unexpectedly at deployment time.",14.5,SEC,88,24)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","How a human handles a detour")
    # c1 left top: the parked-truck story with maze glyph
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"A demonstrated route, blocked",16,ACCENT,"800")+
        para(92,224,"Consider following a demonstrated route from a start to a destination. Partway there, a truck is parked where the demonstration had none.",13.5,SEC,40,20)[0]+
        mazefig(384,178,0.98))
    # c2 left bottom: human detours and rejoins
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,378,560,172,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(92,414,"People detour, then rejoin",15,GREEN,"800")+
        para(92,442,"A human simply detours around the obstacle and then rejoins the original demonstrated path at a convenient point - effortless for people.",13.5,TEXT,58,20)[0])
    # c3 right top: current OSIL just clones
    rxx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,204,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,158,6,204,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"But current OSIL just clones",16,GOLD,"800")+
        para(rxx+28,226,"This is hard for current one-shot imitation techniques, which mostly clone demonstrated actions and have no principled way to behave in states the demonstration never showed.",13.5,TEXT,60,20)[0]+
        eqbox(rxx+28,312,rw-56,"unseen state  =>  no principled action",13.5,h=40,col=RED))
    # c4 right bottom: the three-stage blueprint
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,378,rw,172,fill=PANEL,stroke=STROKE)+
        rect(rxx,378,6,172,fill=TEAL,rx=6,sw=0)+
        T(rxx+28,414,"Blueprint: identify, analyze, trace",15.5,TEAL,"800")+
        tracestages(rxx+28,428,rw-56,110))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","A setting, an architecture, a theory")
    cards=[
        (ch[0],VIOLET,"≡","Three contributions","The paper advances one-shot imitation on three fronts: a harder setting, a tracing architecture, and a meta-RL formulation with theory."),
        (ch[1],ACCENT,"1","Harder OSIL + VPAM","Deliberately introduces a large gap between when the demonstration is collected and when the policy is deployed, backed by a new demonstration-navigation benchmark."),
        (ch[2],TEAL,"2","Demonstration transformer","A demonstration transformer architecture that encourages the policy to trace the demonstration, following the identify, analyze, and trace process."),
        (ch[3],GREEN,"3","Meta-RL + theory","Casts one-shot imitation as context-based meta-reinforcement learning, and analyzes the conditions under which an imitator can succeed from a single trajectory."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,tag,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+75,tag,26,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,13.5,SEC,29,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"One trained imitator that traces a single demonstration and stays robust when the world changes.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Trace the demo, train with meta-RL")
    # c1 full-width top: the demonstration transformer + eq
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,182,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,182,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"Demonstration transformer: state is the query",16.5,TEXT,"800")+
        para(92,220,"The first core piece turns the human three-stage process into a network: the agent's current state is the query, and the demonstration's states and actions are the keys and values.",13,SEC,58,19)[0]+
        eqbox(92,286,536,"q = s_t   ;   K,V = demo   ;   a = trace(attn(q,K)*V, s_t)",12,h=40)+
        demotransformer(652,196,564,128))
    # c2 identify / analyze / trace
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,356,560,194,fill=PANEL,stroke=STROKE)+
        rect(64,356,6,194,fill=TEAL,rx=6,sw=0)+
        T(92,394,"Identify, analyze, then trace",16.5,TEAL,"800")+
        para(92,424,"An attention-weighting module identifies which demonstrated states to follow, a point-wise product analyzes how the expert behaved, and the result combines with the current state to give the action.",13,TEXT,64,19)[0]+
        stagebar(92,504,504,42))
    # c3 right top: training is meta-RL, not BC
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,356,rw,90,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,356,6,90,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,388,"Training: meta-RL, not cloning",15.5,GOLD,"800")+
        para(rxx+28,414,"Rather than behavior cloning, DDT frames one-shot imitation as context-based meta-RL, so the agent explores and learns to act in states the demo never visited.",12.5,SEC,82,18)[0])
    # c4 right bottom: OSIL reward + SAC
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,462,rw,88,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rxx,462,6,88,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,494,"OSIL reward + task reward, via SAC",15,GREEN,"800")+
        para(rxx+28,520,"A stationary OSIL reward rewards following the demo while a large task reward keeps the focus on finishing; all optimized by Soft Actor-Critic.",12.5,SEC,82,18)[0])
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","VPAM maze plus robotics tasks")
    # c1 full-width top: VPAM introduced
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"VPAM: Valet Parking Assist in Maze",16,TEXT,"800")+
        para(92,220,"To test one-shot imitation under unforeseen change, the authors built VPAM, a maze navigation benchmark inspired by real-world valet parking - the setting where DDT's runtime robustness matters most.",13,SEC,66,20)[0]+
        mazefig(1032,174,0.68))
    # c2 left: point agent, local ray views
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,140,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,140,fill=TEAL,rx=6,sw=0)+
        T(92,360,"Point agent, local ray views",15,TEAL,"800")+
        para(92,388,"A point agent must reach a target in a maze it has never seen globally, relying only on short local views computed from eight rays.",13,SEC,44,19)[0]+
        raysfig(536,394,1.0))
    # c3 right: random obstacles + variants
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,324,560,140,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,324,6,140,fill=GOLD,rx=6,sw=0)+
        T(684,360,"Random obstacles, 8 variants",15.5,GOLD,"800")+
        para(684,388,"Rectangular obstacles are randomly dropped on the path and often absent from the demo, so blind replay fails. Eight variants vary single vs many maps, obstacles, and coordinates.",13,TEXT,62,19)[0])
    # c4 full-width green: robotics suites
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,480,6,70,fill=GREEN,rx=6,sw=0)+
        T(92,512,"Beyond VPAM: robotics",15.5,GREEN,"800")+
        envrow(360,486,856,[("Meta-World",ACCENT,"+ disturbance"),("Reacher",TEAL,"Gymnasium"),
                            ("Pusher",GOLD,"Gymnasium"),("MuJoCo manip.",RED,"grasp/stack")]))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","DDT leads, and stays robust")
    # c1 headline strip with grouped bars
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,162,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,162,fill=GREEN,rx=6,sw=0)+
        T(92,196,"Across VPAM, DDT consistently leads",16.5,GREEN,"800")+
        rect(92,214,430,90,fill=PANEL2,stroke=STROKE,rx=12)+
        para(112,244,"On every VPAM setting DDT tops the table, and its margin over the baselines grows precisely where it matters most - under unforeseen obstacles.",13,SEC,48,20)[0]+
        groupbars(548,210,668,98,title="VPAM success rate by setting"))
    # c2 success rates
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,336,368,214,fill=PANEL,stroke=STROKE)+
        rect(64,336,6,214,fill=ACCENT,rx=6,sw=0)+
        T(92,372,"High success everywhere",15.5,ACCENT,"800")+
        para(92,400,"DDT reaches 0.86 on the training set and 0.84 without obstacles; even under obstacles it holds 0.73, versus DCRL 0.57 and Trans4OSIL 0.16.",13,SEC,42,19)[0]+
        vsbars(92,470,312,72,"obstacle",0.73,0.16,"Trans4OSIL"))
    # c3 stability / degradation
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,336,368,214,fill=PANEL,stroke=STROKE)+
        rect(456,336,6,214,fill=TEAL,rx=6,sw=0)+
        T(484,372,"Robust: it barely degrades",15.5,TEAL,"800")+
        para(484,400,"From training to unforeseen obstacles DDT drops only 15%, while baselines drop 20, 33, and 52%.",13,SEC,40,19)[0]+
        degradebars(484,452,312,90))
    # c4 meta-world disturbance
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,336,368,214,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(848,336,6,214,fill=GOLD,rx=6,sw=0)+
        T(876,372,"Robotics: 61% vs 12%",15.5,GOLD,"800")+
        para(876,400,"On disturbed Meta-World tasks DDT still succeeds 61% on unseen demonstrations; the strongest baseline manages about 12%.",13,TEXT,42,19)[0]+
        vsbars(876,470,312,72,"unseen",0.61,0.12,"best base",fmt="{:.0%}"))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Both parts are necessary")
    # c1 left top: what is ablated + bars
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Two components ablated",16,ACCENT,"800")+
        para(92,224,"To confirm each component matters, the authors ablate two pieces of DDT and measure the effect on final performance.",13,SEC,40,19)[0]+
        ablbars(340,206,262,140))
    # c2 left bottom: swap transformer
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,378,560,172,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,378,6,172,fill=GOLD,rx=6,sw=0)+
        T(92,414,"Standard transformer hurts",15,GOLD,"800")+
        para(92,442,"Swapping the demonstration transformer for a standard transformer significantly reduces asymptotic performance - the tailored architecture, not attention in general, drives DDT.",13.5,TEXT,58,20)[0])
    # c3 right top: remove OSIL reward
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,204,fill=RED,rx=6,sw=0)+
        T(684,196,"Remove OSIL reward: slow",16,RED,"800")+
        para(684,224,"Training with only the sparse ending reward sharply slows learning; the OSIL reward supplies a dense signal to follow the demo early.",13,SEC,44,19)[0]+
        slowcurve(972,206,232,140))
    # c4 right bottom: distinct necessary roles
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,378,560,172,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(684,414,"Each plays a distinct role",15.5,GREEN,"800")+
        para(684,442,"Together the ablations show the demonstration transformer and the OSIL reward each play a distinct and necessary role in DDT's imitation ability.",13.5,TEXT,58,20)[0])
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","Four numbers that capture DDT")
    # c1 full-width strip: obstacle 73 vs 57
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,120,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,166,6,120,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Under unforeseen obstacles, DDT wins clearly",16.5,GREEN,"800")+
        stat(92,214,300,60,"73% vs 57%","DDT vs best baseline",GREEN)+
        rect(410,214,806,60,fill=PANEL2,stroke=STROKE,rx=12)+
        para(430,240,"On the hardest VPAM setting DDT succeeds 73% of the time, against 57% for the strongest competitor - the gap widens exactly where robustness is tested.",13.5,SEC,96,20)[0])
    # c2 degradation 15%
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,302,368,162,fill=PANEL,stroke=STROKE)+
        rect(64,302,6,162,fill=ACCENT,rx=6,sw=0)+
        T(92,334,"Degradation just -15%",14.5,ACCENT,"800")+
        T(92,356,"train -> unforeseen obstacles",11.5,SEC,"600")+
        vsbars(92,366,312,90,"drop",15,20,"best base",fmt="-{:.0f}%"))
    # c3 meta-world 61 vs 12
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,302,368,162,fill=PANEL,stroke=STROKE)+
        rect(456,302,6,162,fill=GOLD,rx=6,sw=0)+
        T(484,334,"Meta-World, unseen demos",14.5,GOLD,"800")+
        T(484,356,"with added disturbance",11.5,SEC,"600")+
        vsbars(484,366,312,90,"success",0.61,0.12,"best base",fmt="{:.0%}"))
    # c4 scaling
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,302,368,162,fill=PANEL,stroke=STROKE)+
        rect(848,302,6,162,fill=TEAL,rx=6,sw=0)+
        T(876,334,"Scales log-linearly",14.5,TEAL,"800")+
        T(876,356,"~2x with more parameters",11.5,SEC,"600")+
        scalecurve(876,366,312,90))
    # footer scope strip (shared, not an anchor)
    b+=rect(64,480,1152,70,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,510,"Across",13.5,SEC,"600")
    b+=T(180,510,"VPAM (8 variants)  ·  Meta-World  ·  Reacher / Pusher  ·  MuJoCo manip.",14,TEXT,"800",ff=MONO)
    b+=T(1192,510,"robust where prior methods fail",13.5,GREEN,"800",anchor="end")
    b+=T(1192,534,"higher success / lower drop is better",12,TER,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Trace it, don't replay it")
    # c1 thin full-width banner (short chunk)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,58,fill=PANEL2,stroke=STROKE,rx=12)+
        rect(64,166,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"The takeaway is simple: an imitator should trace a demonstration, not blindly replay it.",16,TEXT,"800"))
    cards=[
        (ch[1],ACCENT,"Trace, don't replay","Instead of blindly replaying a demo, an agent should identify which demonstrated states matter right now, read what the expert did, and steer back onto the path after a detour."),
        (ch[2],TEAL,"Transformer + meta-RL","DDT operationalizes tracing with a demonstration transformer trained by meta-RL, giving one-shot imitation that stays robust when the environment changes - where earlier methods fail."),
        (ch[3],GREEN,"A generalist backbone","Its clean log-linear scaling behavior even suggests DDT could become a building block for larger, more general decision-making agents."),
    ]
    cw=368; gap=24; x0=64; cy=240; chh=302
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+34,cy+50,11,fill=col))
        yy=cy+92
        for j,ln in enumerate(wrap(ti,24)):
            body+=T(x+28,yy+j*26,ln,19,TEXT,"800")
        yy+=26*len(wrap(ti,24))+16
        body+=para(x+28,yy,tx,13.5,SEC,34,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,556,1216,556,STROKE,1)
    b+=mazefig(92,566,0.42)
    b+=T(1216,614,"DDT  ·  Deep Demonstration Tracing  ·  ICML 2024",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
