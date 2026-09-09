import sys
sys.path.insert(0, "/home/claude/matchbox")
from birds_icons import BIRDS, BIRD_SYMBOLS
from build_svg import text as T, rect as R, line as L, barcode as BC, esc, C as PAL

MMIN = 25.4  # mm per inch

# ---- label geometry (unchanged product dims) ----
W_FRONT, W_SIDE, W_FLAP, TRIM_H = 30, 10, 30, 50
x_front1, x_sideA1, x_back1, x_sideB1, x_flap1 = 30, 40, 70, 80, 85
TRIM_W = 85

GOLD, CREAM, RICH, CRIM, CHAR = (PAL["gold"]["hex"], PAL["cream"]["hex"], PAL["richblack"]["hex"],
                                  PAL["crimson"]["hex"], PAL["charcoal"]["hex"])
FONT = "Poppins, Arial, sans-serif"

def fit_name(name, max_chars=16):
    if len(name) <= max_chars:
        return [name]
    words = name.split(" ")
    best_split, best_diff = 1, 999
    for i in range(1, len(words)):
        l1 = len(" ".join(words[:i])); l2 = len(" ".join(words[i:]))
        if abs(l1-l2) < best_diff:
            best_diff = abs(l1-l2); best_split = i
    return [" ".join(words[:best_split]), " ".join(words[best_split:])]

def front_symbol(bird):
    fcx = W_FRONT/2
    out = [R(0, 0, W_FRONT, TRIM_H, fill=RICH)]
    out.append(R(2, 2, W_FRONT-4, TRIM_H-4, stroke=GOLD, sw=0.5))
    out.append(f'<g transform="translate({fcx-17},{5}) scale(0.68)">{BIRD_SYMBOLS[bird["key"]]}</g>')
    out.append(T(fcx, 28.3, "EMBER", 4.6, GOLD, weight=700, family=FONT))
    out.append(L(fcx-7.5, 30.8, fcx+7.5, 30.8, GOLD, 0.35))
    lines_ = fit_name(bird["en"])
    fsz = 2.5 if len(lines_) == 1 else 2.15
    yy = 34.3
    for ln in lines_:
        out.append(T(fcx, yy, ln.upper(), fsz, CREAM, weight=600, spacing="0.1"))
        yy += fsz*1.35
    out.append(T(fcx, 44.6, "SAFETY MATCHES", 1.9, GOLD, weight=500, spacing="0.3"))
    return "".join(out)

def side_symbol():
    out = [R(0, 0, W_SIDE, TRIM_H, fill=RICH)]
    out.append(R(0, 7, W_SIDE, 36, fill="#FFFFFF"))  # true blank -- striking compound zone
    out.append(R(0.4, 7.4, W_SIDE-0.8, 35.2, stroke=GOLD, sw=0.3))
    scx = W_SIDE/2
    out.append(f'<g transform="translate({scx-3.5},{1.2}) scale(0.14)">{BIRD_SYMBOLS["peacock"] if False else ""}</g>')
    out.append(f'<circle cx="{scx}" cy="3.4" r="1.5" fill="{CRIM}"/>')
    out.append(f'<circle cx="{scx}" cy="46.6" r="1.5" fill="{CRIM}"/>')
    return "".join(out)

def back_symbol():
    bcx = W_FRONT/2
    out = [R(0, 0, W_FRONT, TRIM_H, fill=CREAM)]
    out.append(f'<circle cx="6" cy="6.5" r="2.6" fill="{CRIM}"/>')
    out.append(T(11, 7.5, "EMBER", 3.6, RICH, weight=700, anchor="start"))
    out.append(T(11, 10.6, "INDIAN BIRDS SERIES", 1.4, CHAR, weight=500, anchor="start", spacing="0.2"))
    out.append(L(2, 13, W_FRONT-2, 13, GOLD, 0.35))
    body = [("Mfd. & Mktd. by:", 500), ("EMBER MATCH WORKS", 700), ("Sivakasi, TN 626123", 400),
            ("Net Wt: 40 Matches", 500), ("Safety Info:", 600), ("Keep away from children", 400),
            ("Store cool & dry place", 400), ("Keep away from flame", 400), ("Close box after use", 400),
            ("Collect all 25 birds!", 600)]
    yy = 17.0
    for s, wgt in body:
        out.append(T(2, yy, s, 1.75, CHAR, weight=wgt, anchor="start"))
        yy += 2.55
    out.append(BC(3, yy+0.8, W_FRONT-6, 4.0, RICH))
    out.append(T(bcx, yy+6.6, "9 800000 123456", 1.5, CHAR, weight=400, spacing="0.2"))
    return "".join(out)

def flap_symbol():
    return L(1, 3, 1, TRIM_H-3, GOLD, 0.2, dash="1,1.2")

# ============================================================
# SHEET
# ============================================================
SHEET_W_IN, SHEET_H_IN = 25, 36
MARGIN_IN = 1
SHEET_W, SHEET_H = SHEET_W_IN*MMIN, SHEET_H_IN*MMIN
MARGIN = MARGIN_IN*MMIN
USABLE_W, USABLE_H = SHEET_W-2*MARGIN, SHEET_H-2*MARGIN

COLS, ROWS = 11, 10
CELL_W, CELL_H = TRIM_H, TRIM_W  # rotated: 50 x 85
GRID_W, GRID_H = COLS*CELL_W, ROWS*CELL_H
GX0 = MARGIN + (USABLE_W-GRID_W)/2
GY0 = MARGIN + (USABLE_H-GRID_H)/2
TOTAL = COLS*ROWS

defs = ['<defs>']
for b in BIRDS:
    defs.append(f'<symbol id="f-{b["key"]}" viewBox="0 0 {W_FRONT} {TRIM_H}">{front_symbol(b)}</symbol>')
defs.append(f'<symbol id="side" viewBox="0 0 {W_SIDE} {TRIM_H}">{side_symbol()}</symbol>')
defs.append(f'<symbol id="back" viewBox="0 0 {W_FRONT} {TRIM_H}">{back_symbol()}</symbol>')
defs.append(f'<symbol id="flap" viewBox="0 0 {W_FLAP} {TRIM_H}">{flap_symbol()}</symbol>')
defs.append('</defs>')

body_layer = []
for r in range(ROWS):
    for c in range(COLS):
        idx = r*COLS + c
        bird = BIRDS[idx % 25]
        cx, cy = GX0 + c*CELL_W, GY0 + r*CELL_H
        tform = f"translate({cx+CELL_W},{cy}) rotate(90)"
        g = [f'<g transform="{tform}">']
        g.append(f'<use href="#f-{bird["key"]}" x="0" y="0" width="{W_FRONT}" height="{TRIM_H}"/>')
        g.append(f'<use href="#side" x="{x_front1}" y="0" width="{W_SIDE}" height="{TRIM_H}"/>')
        g.append(f'<use href="#back" x="{x_sideA1}" y="0" width="{W_FRONT}" height="{TRIM_H}"/>')
        g.append(f'<use href="#side" x="{x_back1}" y="0" width="{W_SIDE}" height="{TRIM_H}"/>')
        g.append(f'<use href="#flap" x="{x_sideB1}" y="0" width="{W_FLAP}" height="{TRIM_H}"/>')
        g.append("</g>")
        body_layer.append("".join(g))

# ---- dieline: grid cut lines + per-row fold lines (all full-span, cheap) ----
diel = []
for c in range(COLS+1):
    x = GX0 + c*CELL_W
    diel.append(L(x, GY0, x, GY0+GRID_H, RICH, 0.3))
for r in range(ROWS+1):
    y = GY0 + r*CELL_H
    diel.append(L(GX0, y, GX0+GRID_W, y, RICH, 0.3))
for r in range(ROWS):
    rowY = GY0 + r*CELL_H
    for off in (x_front1, x_sideA1, x_back1, x_sideB1):
        y = rowY + off
        diel.append(L(GX0, y, GX0+GRID_W, y, RICH, 0.18, dash="1.4,1"))

# ---- corner crop marks + compact footer note ----
crops = []
for (cx_, cy_, dx, dy) in [(GX0, GY0, -1, -1), (GX0+GRID_W, GY0, 1, -1),
                           (GX0, GY0+GRID_H, -1, 1), (GX0+GRID_W, GY0+GRID_H, 1, 1)]:
    crops.append(L(cx_, cy_+dy*2, cx_, cy_+dy*8, RICH, 0.25))
    crops.append(L(cx_+dx*2, cy_, cx_+dx*8, cy_, RICH, 0.25))

note_y = SHEET_H - MARGIN + 8
footer = T(SHEET_W/2, note_y,
           f"EMBER Safety Matches \u2014 Indian Birds Series | Sheet {SHEET_W_IN}x{SHEET_H_IN}in | {COLS}x{ROWS} = {TOTAL} labels | 1in margin | Label 85x50mm | Striking zone = true unprinted white",
           2.6, RICH, weight=500, spacing="0.05")

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{SHEET_W}mm" height="{SHEET_H}mm" viewBox="0 0 {SHEET_W} {SHEET_H}">
<rect width="{SHEET_W}" height="{SHEET_H}" fill="#FFFFFF"/>
{"".join(defs)}
<g id="labels">{"".join(body_layer)}</g>
<g id="dieline">{"".join(diel)}{"".join(crops)}</g>
<g id="notes">{footer}</g>
</svg>'''

with open("/home/claude/matchbox/bird_sheet.svg", "w") as f:
    f.write(svg)
print(f"Sheet: {SHEET_W_IN}x{SHEET_H_IN}in ({SHEET_W:.1f}x{SHEET_H:.1f}mm), grid {COLS}x{ROWS}={TOTAL} labels")
