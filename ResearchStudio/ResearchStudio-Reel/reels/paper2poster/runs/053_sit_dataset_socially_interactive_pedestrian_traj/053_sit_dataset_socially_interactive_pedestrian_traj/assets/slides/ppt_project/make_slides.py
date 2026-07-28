#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the SiT Dataset paper2video deck: 10 all-native SVG slides (1280x720, dark).

Each narration chunk from visual_anchor_contract.json becomes its own
<g id="cue_sXX_cN_..."> card whose <title> carries the narration keywords, so
the strict --require-pptx-anchors cue pass resolves every anchor from geometry.
Only ONE <image> exists deck-wide (code QR on the cover), sized to clear the
ppt_visuals_too_small gate.
"""
import base64
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = os.path.join(HERE, "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
IMG = os.path.join(HERE, "images")
os.makedirs(OUT, exist_ok=True)

# ---- palette -------------------------------------------------------------
BG="#0B1220"; PANEL="#152238"; PANEL2="#1B2B47"; BORDER="#2A3B5C"
INK="#EAF1FF"; SUB="#9DB0D0"; MUTED="#6E82A6"
BLUE="#4F8CFF"; BLUE_SOFT="#2A4A8A"; GREEN="#34D399"; GREEN_SOFT="#14532D"
RED="#F87171"; RED_SOFT="#5A2130"; AMBER="#FBBF24"; VIOLET="#A78BFA"
TRACK="#24344F"; WHITE="#FFFFFF"
SANS="Arial, Helvetica, sans-serif"
SERIF="Georgia, serif"
MONO="Consolas, monospace"

# ---- load anchor contract -----------------------------------------------
with open(CONTRACT, encoding="utf-8") as f:
    CONTRACT_DATA = json.load(f)
SLIDE_CHUNKS = {}          # slide_id -> [(anchor_id, [keywords]), ...]
ORDER = []                 # narration order of slide ids
for s in CONTRACT_DATA["slides"]:
    SLIDE_CHUNKS[s["id"]] = [(c["anchor_id"], c.get("cue_keywords") or []) for c in s["chunks"]]
    ORDER.append(s["id"])
PREFIX = {sid: f"{i+1:02d}" for i, sid in enumerate(ORDER)}

def esc(t):
    return (str(t).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;").replace("'","&apos;"))

class Slide:
    def __init__(self, sid):
        self.sid = sid
        self.body = []
        self.chunks = list(SLIDE_CHUNKS[sid])
        self.ci = 0
    def raw(self, s): self.body.append(s)
    def rect(self, x,y,w,h, fill, rx=0, stroke=None, sw=1, opacity=None):
        o = f' fill-opacity="{opacity}"' if opacity is not None else ""
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{o}/>')
    def line(self,x1,y1,x2,y2,stroke,sw=2,dash=None,cap="round"):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')
    def circle(self,cx,cy,r,fill,stroke=None,sw=1):
        st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.body.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>')
    def poly(self, pts, fill="none", stroke=None, sw=2):
        st=f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"' if stroke else ""
        p=" ".join(f"{x},{y}" for x,y in pts)
        self.body.append(f'<polyline points="{p}" fill="{fill}"{st}/>')
    def text(self,x,y,s,size,fill=INK,weight=400,family=SANS,anchor="start",ls=None,italic=False):
        a=f' text-anchor="{anchor}"' if anchor!="start" else ""
        l=f' letter-spacing="{ls}"' if ls is not None else ""
        it=' font-style="italic"' if italic else ""
        self.body.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}"{a}{l}{it}>{esc(s)}</text>')
    # cue wrapper: pulls next contract anchor for this slide
    def cue_open(self, human):
        aid, kw = self.chunks[self.ci]; self.ci += 1
        title = human + " — " + " ".join(kw)
        self.body.append(f'<g id="{aid}">')
        self.body.append(f'<title>{esc(title)}</title>')
        return aid
    def cue_close(self):
        self.body.append('</g>')
    def save(self):
        assert self.ci == len(self.chunks), f"{self.sid}: used {self.ci}/{len(self.chunks)} cues"
        svg = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
               f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">\n'
               f'<g id="bg"><rect x="0" y="0" width="1280" height="720" fill="{BG}"/>'
               f'<rect x="0" y="0" width="1280" height="6" fill="{BLUE}"/></g>\n'
               + "\n".join(self.body) + "\n</svg>\n")
        with open(os.path.join(OUT, PREFIX[self.sid]+"_"+self.sid+".svg"), "w", encoding="utf-8") as f:
            f.write(svg)

def header(sl, kicker, title, num):
    sl.text(64, 62, kicker, 13, fill=BLUE, weight=700, ls=3)
    sl.text(64, 104, title, 34, fill=INK, weight=700, family=SERIF)
    sl.line(64, 122, 64+300, 122, BORDER, 2)
    sl.text(1216, 62, num, 12, fill=MUTED, weight=600, anchor="end", ls=2)

def card(sl, x, y, w, h, fill=PANEL, stroke=BORDER, rx=14, accent=None):
    sl.rect(x,y,w,h, fill, rx=rx, stroke=stroke, sw=1)
    if accent:
        sl.rect(x, y+16, 5, h-32, accent, rx=2)

def tag(sl, x, y, label, color):
    w = 16 + len(label)*7.6
    sl.rect(x, y-15, w, 22, PANEL2, rx=6, stroke=color, sw=1)
    sl.text(x+8, y, label, 12, fill=color, weight=700, ls=1)
    return w

def wrap(sl, x, y, s, size, fill, weight, maxchars, lh, family=SANS):
    words=s.split(); line=""; yy=y
    for wd in words:
        t=(line+" "+wd).strip()
        if len(t)>maxchars and line:
            sl.text(x,yy,line,size,fill=fill,weight=weight,family=family); line=wd; yy+=lh
        else: line=t
    if line: sl.text(x,yy,line,size,fill=fill,weight=weight,family=family); yy+=lh
    return yy

# =========================================================================
# SLIDE 01 - TITLE / COVER
# =========================================================================
def s01():
    sl = Slide("title")
    # left column
    sl.text(64, 96, "HANYANG UNIVERSITY", 13, fill=BLUE, weight=700, ls=3)
    sl.text(64, 118, "NeurIPS 2023 · Datasets & Benchmarks", 12, fill=MUTED, weight=600, ls=1)
    sl.cue_open("SiT title and social-navigation framing")
    sl.text(64, 196, "SiT Dataset", 52, fill=INK, weight=700, family=SERIF)
    sl.text(64, 240, "Socially Interactive Pedestrian Trajectory", 22, fill=SUB, weight=600)
    sl.text(64, 268, "for Social Navigation Robots", 22, fill=SUB, weight=600)
    sl.rect(64, 286, 90, 5, BLUE, rx=2)
    sl.text(64, 330, "Trajectories recorded by a robot moving through real crowds —", 15, fill=INK, weight=500)
    sl.text(64, 352, "perceiving and predicting the people around it, up close.", 15, fill=INK, weight=500)
    sl.text(64, 384, "Bae, Kim, Yun, Kang, Choi, Kim, Lee, Choi, Choi", 13, fill=MUTED, weight=500)
    sl.cue_close()
    # QR (only image in deck), lower left — sized to clear ppt_visuals_too_small
    with open(os.path.join(IMG,"code_qr.png"),"rb") as f:
        qr=base64.b64encode(f.read()).decode()
    sl.rect(64, 432, 212, 212, WHITE, rx=12)
    sl.body.append(f'<image href="data:image/png;base64,{qr}" x="72" y="440" width="196" height="196" preserveAspectRatio="xMidYMid meet"/>')
    sl.text(300, 500, "SCAN FOR CODE", 12, fill=SUB, weight=700, ls=2)
    sl.text(300, 526, "github.com/SPALaboratory/SiT-Dataset", 13, fill=BLUE, weight=600)
    sl.text(300, 580, "Dataset · dev-kit · baselines", 14, fill=MUTED, weight=500, italic=True)
    sl.text(300, 602, "released publicly.", 14, fill=MUTED, weight=500, italic=True)
    # right column: 3 highlight cards for chunks c2,c3,c4
    RX=676; RW=540; ry=150; rh=150; gap=18
    cards=[
        ("WHAT IT IS", BLUE, "The SiT dataset — Socially Interactive Pedestrian Trajectory — captures genuine human-robot interaction as a robot navigates crowds.",
         "SiT dataset introduced short socially interactive"),
        ("WHY IT IS NEW", GREEN, "Unlike fixed rooftop cameras or cars on separate roads, SiT was recorded by a mobile robot in densely populated indoor and outdoor Seoul.",
         "Unlike earlier trajectory datasets mobile robot Seoul"),
        ("WHAT IT SHIPS", AMBER, "Synchronized LiDAR, camera, IMU and RTK, 2D and 3D annotations, semantic maps, and a benchmark from detection to end-to-end forecasting.",
         "Ships synchronized LiDAR camera IMU RTK benchmark"),
    ]
    for i,(lab,col,txt,hu) in enumerate(cards):
        y=ry+i*(rh+gap)
        sl.cue_open(hu)
        card(sl, RX, y, RW, rh, fill=PANEL, accent=col)
        sl.text(RX+26, y+36, lab, 13, fill=col, weight=700, ls=2)
        wrap(sl, RX+26, y+66, txt, 16, INK, 500, 50, 24)
        sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 02 - PROBLEM
# =========================================================================
def s02():
    sl=Slide("problem")
    header(sl,"THE PROBLEM","Training Data That Never Sees the Robot","01 / 10")
    # c1 intro card (full width) - perceive & predict
    sl.cue_open("Robot must perceive and predict nearby pedestrians in 3D")
    card(sl,64,150,1152,60,fill=PANEL,accent=BLUE)
    sl.text(90,186,"To move safely among people, a robot must perceive nearby pedestrians as individual 3D entities — and predict where they go next.",18,fill=INK,weight=500)
    sl.cue_close()
    # c2 problem statement strip
    sl.cue_open("Datasets used to train these models do not reflect the robot's real situation")
    card(sl,64,222,1152,48,fill=RED_SOFT,stroke=RED)
    sl.text(90,252,"The problem: the datasets used to train these models don't reflect the robot's real situation.",17,fill=INK,weight=600)
    sl.cue_close()
    # c3 fixed-camera datasets (left)
    sl.cue_open("ETH UCY SDD fixed rooftop cameras never see interaction")
    card(sl,64,288,560,242,fill=PANEL,accent=VIOLET)
    sl.text(92,324,"Fixed top-view cameras",17,fill=VIOLET,weight=700)
    sl.text(92,350,"ETH · UCY · SDD",14,fill=SUB,weight=600)
    for i,t in enumerate(["Mounted high on rooftops or drones",
                          "A bird's-eye view of a plaza or street",
                          "The device never enters the scene",
                          "So they never see human-robot interaction"]):
        yy=384+i*34; sl.circle(104,yy-4,4,VIOLET); sl.text(118,yy,t,14,fill=INK,weight=500)
    sl.cue_close()
    # c4 autonomous-driving datasets (right)
    sl.cue_open("Autonomous-driving datasets separate roads rarely close contact")
    card(sl,644,288,572,242,fill=PANEL,accent=AMBER)
    sl.text(672,324,"Autonomous-driving data",17,fill=AMBER,weight=700)
    sl.text(672,350,"nuScenes · Waymo · Argoverse",14,fill=SUB,weight=600)
    for i,t in enumerate(["Rich multi-sensor data from a moving car",
                          "But car and pedestrians use separate roads",
                          "They rarely come into close contact",
                          "Neither setting matches a robot in a crowd"]):
        yy=384+i*34; sl.circle(684,yy-4,4,AMBER); sl.text(698,yy,t,14,fill=INK,weight=500)
    sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 03 - MOTIVATION
# =========================================================================
def s03():
    sl=Slide("motivation")
    header(sl,"MOTIVATION","Interaction Only Appears Up Close","02 / 10")
    # c1 HRI finding (left top)
    sl.cue_open("Studies show robot motion changes how nearby people walk")
    card(sl,64,150,560,190,fill=PANEL,accent=GREEN)
    sl.text(92,186,"Interaction is real",16,fill=GREEN,weight=700)
    wrap(sl,92,216,"Human-robot interaction studies show a robot's motion changes how nearby people walk — and the effect is strongest when robot and pedestrians share the same space, up close.",16,INK,500,48,24)
    sl.cue_close()
    # c2 what data is needed (right top)
    sl.cue_open("Need data collected from a moving robot inside real crowds")
    card(sl,644,150,572,190,fill=BLUE_SOFT,stroke=BLUE)
    sl.text(672,186,"WHAT WE NEED",13,fill=BLUE,weight=700,ls=2)
    wrap(sl,672,216,"To study and model that behavior, we need data collected while a robot actually moves through crowds — not from a camera bolted to a building.",17,INK,600,50,25)
    sl.cue_close()
    # c3 prior robot datasets gaps (left bottom, wide)
    sl.cue_open("STCrowd fixed position and JRDB no trajectories not synced")
    card(sl,64,364,772,150,fill=PANEL,accent=RED)
    sl.text(92,400,"Prior robot datasets came close — but each had a gap",16,fill=RED,weight=700)
    sl.text(92,438,"STCrowd",15,fill=INK,weight=700)
    sl.text(92,462,"Sensors kept at a fixed position →",13,fill=SUB,weight=500)
    sl.text(92,484,"scenes barely varied.",13,fill=SUB,weight=500)
    sl.line(452,428,452,500,BORDER,1)
    sl.text(474,438,"JRDB",15,fill=INK,weight=700)
    sl.text(474,462,"Not organized into trajectories; sensors",13,fill=SUB,weight=500)
    sl.text(474,484,"not fully time-synchronized → limits fusion.",13,fill=SUB,weight=500)
    sl.cue_close()
    # c4 SiT fills the gaps (right bottom)
    sl.cue_open("SiT designed specifically to fill these gaps")
    card(sl,856,364,360,150,fill=GREEN_SOFT,stroke=GREEN)
    sl.text(880,404,"SiT",34,fill=GREEN,weight=700,family=SERIF)
    wrap(sl,880,440,"is designed specifically to fill these gaps.",17,INK,600,30,24)
    sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 04 - CONTRIBUTIONS (2x2)
# =========================================================================
def s04():
    sl=Slide("contribution")
    header(sl,"CONTRIBUTIONS","What SiT Delivers","03 / 10")
    data=[
        ("01","Real crowd trajectories",BLUE,"Large-scale real-world pedestrian trajectories gathered as a robot navigated crowded indoor and outdoor scenes — interiors, campuses, crosswalks, walkways.",
         "Large-scale real-world pedestrian trajectories indoor outdoor"),
        ("02","Rich prediction context",GREEN,"Enables prediction with rich context: appearance features, the robot's own ego-motion, and semantic map data around each pedestrian.",
         "Rich context appearance ego-motion semantic map"),
        ("03","Synchronized + mapped",VIOLET,"Precise time synchronization across all sensors via centralized triggering makes fusion practical, plus multi-layered semantic maps for indoor and outdoor scenes.",
         "Precise time synchronization centralized triggering semantic maps"),
        ("04","Unified benchmark",AMBER,"A curated benchmark spanning 3D detection, 3D multi-object tracking, trajectory prediction, and end-to-end motion forecasting — all released publicly.",
         "Curated benchmark detection tracking prediction end-to-end"),
    ]
    X=[64,644]; Y=[150,352]; W=552; H=178
    for i,(n,t,c,txt,hu) in enumerate(data):
        x=X[i%2]; y=Y[i//2]
        sl.cue_open(hu)
        card(sl,x,y,W,H,fill=PANEL,accent=c)
        sl.text(x+30,y+58,n,40,fill=c,weight=700,family=SERIF)
        sl.text(x+96,y+50,t,20,fill=INK,weight=700)
        sl.line(x+96,y+62,x+W-30,y+62,BORDER,1)
        wrap(sl,x+96,y+92,txt,15,SUB,500,52,22)
        sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 05 - METHOD
# =========================================================================
def s05():
    sl=Slide("method")
    header(sl,"DATA COLLECTION","A Sensor-Rich Robot in the Crowd","04 / 10")
    # c1: platform + sensor suite (left top)
    sl.cue_open("Clearpath Husky UGV with LiDARs cameras IMUs RTK")
    card(sl,64,150,720,168)
    sl.text(90,184,"Clearpath Husky UGV — remotely operated through downtown Seoul",16,fill=INK,weight=700)
    sensors=[("2×","Velodyne\n16-ch LiDAR",BLUE),
             ("5×","Basler cameras\n360° view",GREEN),
             ("2×","IMU",VIOLET),
             ("RTK","positioning",AMBER)]
    sx=90
    for i,(a,b,c) in enumerate(sensors):
        x=sx+i*168
        sl.rect(x,214,150,80,PANEL2,rx=10,stroke=c,sw=1)
        sl.text(x+75,246,a,22,fill=c,weight=700,anchor="middle",family=SERIF)
        for j,ln in enumerate(b.split("\n")):
            sl.text(x+75,266+j*15,ln,11,fill=SUB,weight=500,anchor="middle")
    sl.cue_close()
    # c2: PPS time sync (left bottom)
    sl.cue_open("Pulse-per-second signal generator triggers all sensors in time")
    card(sl,64,332,720,150,fill=PANEL,accent=BLUE)
    sl.text(90,366,"Precise time synchronization",16,fill=BLUE,weight=700)
    sl.rect(90,384,140,48,GREEN_SOFT,rx=8,stroke=GREEN,sw=1)
    sl.text(160,414,"PPS generator",13,fill=GREEN,weight=700,anchor="middle")
    for i,(lab) in enumerate(["LiDAR","cameras","IMU"]):
        x=300+i*150
        sl.line(230,408,x,408,GREEN,2)
        sl.rect(x,392,120,32,PANEL2,rx=8,stroke=BORDER,sw=1)
        sl.text(x+60,413,lab,13,fill=INK,weight=600,anchor="middle")
    sl.text(90,468,"A pulse-per-second trigger aligns every sensor in time, making camera–LiDAR fusion reliable.",13,fill=SUB,weight=500)
    sl.cue_close()
    # c3: pose recovery (right top)
    sl.cue_open("Robot pose from RTK outdoors and LiDAR-inertial SLAM indoors")
    card(sl,804,150,412,168,fill=PANEL,accent=VIOLET)
    sl.text(828,186,"Robot ego-motion",16,fill=VIOLET,weight=700)
    wrap(sl,828,214,"Pose from RTK outdoors and LiDAR-inertial SLAM indoors — needed to compensate ego-motion when forming trajectories and to align the maps.",15,INK,500,34,22)
    sl.cue_close()
    # c4: annotation + maps (right bottom)
    sl.cue_open("Twelve-layer semantic maps 3D cuboids 5Hz to 10Hz privacy blur")
    card(sl,804,332,412,150,fill=PANEL,accent=AMBER)
    sl.text(828,366,"Maps & annotations",16,fill=AMBER,weight=700)
    wrap(sl,828,394,"12-layer semantic maps from point clouds. 3D cuboids labeled at 5 Hz, interpolated to 10 Hz; 2D boxes share IDs. Faces & plates blurred.",14,INK,500,36,21)
    sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 06 - DATASET / BENCHMARK
# =========================================================================
def s06():
    sl=Slide("dataset-benchmark")
    header(sl,"DATASET & BENCHMARK","Sixty Scenes, Four Benchmarks","05 / 10")
    # c1 dataset scale (left top) - KPI row inside
    sl.cue_open("SiT contains 60 scenes 60K images 12K point clouds annotations")
    card(sl,64,150,560,168)
    sl.text(90,184,"Dataset scale",16,fill=INK,weight=700)
    kpis=[("60","scenes",BLUE),("60K","images",GREEN),("12K","point clouds",VIOLET)]
    for i,(n,l,c) in enumerate(kpis):
        x=104+i*168
        sl.text(x,236,n,34,fill=c,weight=700,family=SERIF)
        sl.text(x,258,l,13,fill=SUB,weight=600)
    sl.text(90,296,"≈ 470K 2D annotations  ·  ≈ 320K 3D annotations",15,fill=INK,weight=600)
    sl.cue_close()
    # c2 clip structure (right top)
    sl.cue_open("Twenty-second clips at ten hertz yield nine-second trajectories")
    card(sl,644,150,572,168,fill=PANEL,accent=GREEN)
    sl.text(672,184,"Clip structure",16,fill=GREEN,weight=700)
    sl.text(672,232,"20 s",34,fill=GREEN,weight=700,family=SERIF)
    sl.text(760,232,"of sequential data at 10 Hz",16,fill=INK,weight=600)
    sl.text(672,272,"→  9 s of trajectory, represented as pose vectors.",15,fill=SUB,weight=500)
    sl.text(672,300,"On top of this data, the paper defines four benchmarks.",14,fill=MUTED,weight=500,italic=True)
    sl.cue_close()
    # c3 detection + tracking (left bottom)
    sl.cue_open("3D detection distance-based AP and 3D multi-object tracking")
    card(sl,64,338,560,192,fill=PANEL,accent=BLUE)
    sl.text(92,374,"Perception benchmarks",16,fill=BLUE,weight=700)
    sl.text(92,410,"1 · 3D pedestrian detection",15,fill=INK,weight=700)
    sl.text(110,432,"AP on center distance @ 0.25 / 0.5 / 1 / 2 m",13,fill=SUB,weight=500)
    sl.text(92,472,"2 · 3D multi-object tracking",15,fill=INK,weight=700)
    sl.text(110,494,"Standard MOT metrics (sAMOTA, AMOTA, MOTA…)",13,fill=SUB,weight=500)
    sl.cue_close()
    # c4 prediction + end-to-end (right bottom)
    sl.cue_open("Trajectory prediction two seconds past seven ahead end-to-end")
    card(sl,644,338,572,192,fill=PANEL,accent=VIOLET)
    sl.text(672,374,"Forecasting benchmarks",16,fill=VIOLET,weight=700)
    sl.text(672,410,"3 · Trajectory prediction",15,fill=INK,weight=700)
    sl.text(690,432,"2 s of past → 7 s ahead, ADE / FDE over best-of-K",13,fill=SUB,weight=500)
    sl.text(672,472,"4 · End-to-end",15,fill=INK,weight=700)
    sl.text(690,494,"Raw sensors → future bounding boxes & trajectories",13,fill=SUB,weight=500)
    sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 07 - KEY RESULT
# =========================================================================
def s07():
    sl=Slide("key-result")
    header(sl,"KEY RESULT","It Captures the Interaction — and Maps Help","06 / 10")
    # c1 headline banner
    sl.cue_open("Analysis confirms SiT captures the interactions it targeted")
    card(sl,64,150,1152,58,fill=PANEL,accent=GREEN)
    sl.text(90,186,"The data analysis confirms SiT captures exactly the close human-robot interaction it set out to.",18,fill=INK,weight=600)
    sl.cue_close()
    # c2 proximity scatter (left) - SiT clusters close vs AD off-side
    sl.cue_open("Pedestrians cluster close from all directions vs Waymo nuScenes off-side")
    card(sl,64,230,560,300)
    sl.text(90,264,"Where pedestrians appear (relative to ego)",15,fill=INK,weight=700)
    # two mini polar plots
    import math
    def polar(cx,cy,r,col,close):
        sl.circle(cx,cy,r,PANEL2,stroke=BORDER,sw=1)
        sl.circle(cx,cy,3,col)
        pts = [(0.30,20),(0.42,80),(0.28,140),(0.5,200),(0.33,260),(0.45,320),(0.25,10),(0.38,170)] if close \
              else [(0.9,15),(0.95,340),(0.85,20),(0.92,350),(0.8,10),(0.9,5)]
        for rr,ang in pts:
            a=math.radians(ang)
            sl.circle(cx+r*rr*math.cos(a), cy-r*rr*math.sin(a), 3.5, col)
    polar(200,400,78,GREEN,True)
    sl.text(200,502,"SiT — close, all directions",12,fill=GREEN,weight=700,anchor="middle")
    polar(470,400,78,AMBER,False)
    sl.text(470,502,"Waymo / nuScenes — off to the side",11,fill=AMBER,weight=700,anchor="middle")
    sl.cue_close()
    # c3 interaction-instance count (right top)
    sl.cue_open("SiT has dramatically more space-sharing within-two-meter instances")
    card(sl,644,230,572,142,fill=PANEL,accent=BLUE)
    sl.text(672,266,"Space-sharing + within-2 m instances",15,fill=BLUE,weight=700)
    bx=672; bw=380; by=300
    sl.rect(bx,by,bw,24,GREEN,rx=5); sl.text(bx+12,by+17,"SiT",13,fill="#062012",weight=700)
    sl.text(bx+bw+12,by+17,"far more",13,fill=GREEN,weight=700)
    sl.rect(bx,by+34,bw*0.18,24,AMBER,rx=5)
    sl.text(bx+bw*0.18+12,by+51,"nuScenes / Waymo / Argoverse",12,fill=SUB,weight=600)
    sl.cue_close()
    # c4 semantic map improves prediction (right bottom)
    sl.cue_open("Semantic map improves prediction NSP-SFM ADE20 0.52 FDE20 0.93")
    card(sl,644,388,572,142,fill=GREEN_SOFT,stroke=GREEN)
    sl.text(672,424,"Semantic map improves prediction",15,fill=GREEN,weight=700)
    sl.text(672,474,"0.52",40,fill=GREEN,weight=700,family=SERIF)
    sl.text(752,474,"ADE₂₀",15,fill=INK,weight=600)
    sl.text(852,474,"0.93",40,fill=GREEN,weight=700,family=SERIF)
    sl.text(932,474,"FDE₂₀",15,fill=INK,weight=600)
    sl.text(672,506,"Best model NSP-SFM with the map — clearly better than without.",13,fill=SUB,weight=500)
    sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 08 - ABLATION
# =========================================================================
def s08():
    sl=Slide("ablation-study")
    header(sl,"ABLATION","The Map Helps — Fusion Wins","07 / 10")
    # c1 banner
    sl.cue_open("Most informative comparison map on off for trajectory prediction")
    card(sl,64,150,1152,56,fill=BLUE_SOFT,stroke=BLUE)
    sl.text(90,186,"The most informative comparison: turning the semantic map on and off for trajectory prediction.",18,fill=INK,weight=600)
    sl.cue_close()
    # c2 Y-Net (left) - before/after bars
    sl.cue_open("Y-Net map lowers ADE20 0.84 to 0.68 FDE20 1.88 to 1.55")
    card(sl,64,230,560,300,fill=PANEL,accent=VIOLET)
    sl.text(92,266,"Y-Net · with vs without map",16,fill=VIOLET,weight=700)
    def metric_pair(x0,y0,label,no,yes,mx):
        sl.text(x0,y0,label,14,fill=SUB,weight=700)
        bw=300
        sl.rect(x0,y0+14,bw*no/mx,20,RED,rx=4); sl.text(x0+bw*no/mx+10,y0+30,f"{no:.2f}",13,fill=RED,weight=700)
        sl.text(x0+bw+70,y0+30,"no map",11,fill=MUTED,weight=600)
        sl.rect(x0,y0+40,bw*yes/mx,20,GREEN,rx=4); sl.text(x0+bw*yes/mx+10,y0+56,f"{yes:.2f}",13,fill=GREEN,weight=700)
        sl.text(x0+bw+70,y0+56,"+ map",11,fill=GREEN,weight=600)
    metric_pair(92,306,"ADE₂₀",0.84,0.68,2.0)
    metric_pair(92,392,"FDE₂₀",1.88,1.55,2.0)
    sl.text(92,500,"Adding the map lowers both errors.",13,fill=SUB,weight=500,italic=True)
    sl.cue_close()
    # c3 NSP-SFM (right top)
    sl.cue_open("NSP-SFM map brings ADE20 0.63 to 0.52 FDE20 1.09 to 0.93 helps both")
    card(sl,644,230,572,142,fill=PANEL,accent=GREEN)
    sl.text(672,266,"NSP-SFM · with vs without map",16,fill=GREEN,weight=700)
    sl.text(672,306,"ADE₂₀  0.63 → 0.52",18,fill=INK,weight=700)
    sl.text(672,336,"FDE₂₀  1.09 → 0.93",18,fill=INK,weight=700)
    sl.text(960,306,"↓",20,fill=GREEN,weight=700); sl.text(960,336,"↓",20,fill=GREEN,weight=700)
    sl.text(984,321,"map helps in both cases",13,fill=GREEN,weight=600)
    sl.cue_close()
    # c4 detection (right bottom)
    sl.cue_open("Fusion beats single-sensor voxel beats pillar TransFusion best")
    card(sl,644,388,572,142,fill=PANEL,accent=AMBER)
    sl.text(672,424,"Detection findings",16,fill=AMBER,weight=700)
    for i,t in enumerate(["Camera + LiDAR fusion beats single-sensor models",
                          "Voxel backbones beat pillar-based ones",
                          "TransFusion (voxel) gives the best detection score"]):
        yy=452+i*26; sl.circle(684,yy-4,4,AMBER); sl.text(698,yy,t,14,fill=INK,weight=500)
    sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 09 - HEADLINE NUMBERS
# =========================================================================
def s09():
    sl=Slide("headline-numbers")
    header(sl,"BY THE NUMBERS","Numbers Worth Remembering","08 / 10")
    # c1 banner
    sl.cue_open("A few numbers capture what SiT provides")
    card(sl,64,150,1152,54,fill=BLUE_SOFT,stroke=BLUE)
    sl.text(90,185,"A few numbers worth remembering from the SiT dataset and its benchmark.",18,fill=INK,weight=600)
    sl.cue_close()
    kpis=[
        ("60 scenes",BLUE,"about 60K images and 12K point cloud frames, with ≈470K 2D and ≈320K 3D annotations.",
         "Sixty scenes sixty thousand images twelve thousand point clouds annotations"),
        ("0.52 / 0.93",VIOLET,"best trajectory prediction with the semantic map: ADE₂₀ and FDE₂₀ (NSP-SFM).",
         "Trajectory benchmark best semantic map ADE20 0.52 FDE20 0.93"),
        ("0.53 · 0.61",GREEN,"best camera+LiDAR detection mAP, and CenterPoint tracking sAMOTA — leading the benchmark.",
         "Detection fusion mAP 0.53 tracking CenterPoint sAMOTA 0.61"),
    ]
    X=[64,458,852]; W=364; y=234; H=290
    for i,(num,c,txt,hu) in enumerate(kpis):
        x=X[i]
        sl.cue_open(hu)
        card(sl,x,y,W,H,fill=PANEL,accent=None,stroke=BORDER)
        sl.rect(x,y,W,6,c,rx=3)
        sl.text(x+W/2,y+130,num,44,fill=c,weight=700,anchor="middle",family=SERIF)
        sl.line(x+50,y+160,x+W-50,y+160,BORDER,1)
        wrap(sl,x+30,y+196,txt,15,SUB,500,38,23)
        sl.cue_close()
    sl.save()

# =========================================================================
# SLIDE 10 - TAKEAWAY
# =========================================================================
def s10():
    sl=Slide("takeaway")
    header(sl,"TAKEAWAY","Data From the Crowd, Not the Rooftop","09 / 10")
    cards=[
        ("The takeaway is simple",BLUE,"Social navigation needs data that shows the robot up close in the crowd — not a camera bolted to a building.",
         "Takeaway is simple"),
        ("What such data must have",GREEN,"To build robots that move safely and gracefully among people, you need close-crowd trajectories, sensors aligned in time, and the surrounding scene captured as a map.",
         "Robots move safely close crowd sensors aligned scene map"),
        ("SiT is the first to deliver it",VIOLET,"SiT is the first dataset to combine all three, with a benchmark spanning detection, tracking, prediction, and end-to-end forecasting — all publicly released.",
         "SiT first dataset deliver combination benchmark publicly released"),
    ]
    y=150; H=112; gap=14
    for i,(t,c,txt,hu) in enumerate(cards):
        yy=y+i*(H+gap)
        sl.cue_open(hu)
        card(sl,64,yy,820,H,fill=PANEL,accent=c)
        sl.text(92,yy+40,t,19,fill=c,weight=700)
        wrap(sl,92,yy+70,txt,15,SUB,500,74,22)
        sl.cue_close()
    # right rail summary (decorative)
    card(sl,908,150,308,376,fill=PANEL2,stroke=BORDER)
    sl.text(1062,196,"SiT",34,fill=INK,weight=700,anchor="middle",family=SERIF)
    sl.text(1062,222,"robot in the crowd",14,fill=SUB,weight=500,anchor="middle")
    sl.line(958,244,1166,244,BORDER,1)
    for i,(k,v,c) in enumerate([("scenes","60",BLUE),("sensors","LiDAR+cam+RTK",GREEN),("maps","12 layers",VIOLET),("benchmark","4 tasks",AMBER)]):
        yy=290+i*54
        sl.text(958,yy,k,14,fill=MUTED,weight=600)
        sl.text(1166,yy,v,15,fill=c,weight=700,anchor="end")
        sl.line(958,yy+16,1166,yy+16,BORDER,1)
    sl.text(1062,516,"github.com/SPALaboratory/SiT-Dataset",11,fill=MUTED,weight=500,anchor="middle")
    sl.save()

for fn in (s01,s02,s03,s04,s05,s06,s07,s08,s09,s10):
    fn()
print("wrote 10 slides to", OUT)
