#!/usr/bin/env python3
"""Generate the final ebook cover for The Challenger.

The design follows the established Blackwood Ridge series language:
deep-plum field, tarnished-gold frame and serif typography, archival paper,
red/blue evidence overlays, and Callie Thorne's brass magnifying glass.
"""
from __future__ import annotations

import argparse
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

WIDTH = 1600
HEIGHT = 2560
DPI = 72

PLUM = (47, 20, 55)
PLUM_LIGHT = (89, 44, 102)
PLUM_DARK = (25, 10, 31)
GOLD = (184, 134, 11)
GOLD_LIGHT = (225, 192, 102)
IVORY = (244, 236, 213)
PAPER_SHADOW = (82, 53, 48)
ARCHIVE_GREEN = (75, 96, 67)
BLUE = (63, 95, 138)
RED = (143, 58, 58)
MARBLE = (205, 206, 198)
INK = (48, 37, 34)

FONT_REGULAR = Path('/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf')
FONT_BOLD = Path('/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Bold.ttf')
FONT_SMALLCAPS = Path('/usr/share/fonts/truetype/ebgaramond/EBGaramond12-AllSC.ttf')
FONT_ITALIC = Path('/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Italic.ttf')
FALLBACK = Path('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf')
FALLBACK_BOLD = Path('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf')


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    selected = path if path.exists() else (FALLBACK_BOLD if 'Bold' in path.name else FALLBACK)
    return ImageFont.truetype(str(selected), size=size)


def add_tracking(draw: ImageDraw.ImageDraw, text: str, xy: tuple[float, float], face: ImageFont.FreeTypeFont,
                 fill: tuple[int, int, int], tracking: float, anchor: str = 'mm') -> None:
    widths = [draw.textlength(ch, font=face) for ch in text]
    total = sum(widths) + tracking * max(0, len(text) - 1)
    x, y = xy
    if anchor.startswith('m'):
        x -= total / 2
    elif anchor.startswith('r'):
        x -= total
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=face, fill=fill, anchor='lm')
        x += w + tracking


def centered(draw: ImageDraw.ImageDraw, text: str, y: int, face: ImageFont.FreeTypeFont,
             fill: tuple[int, int, int], stroke_width: int = 0,
             stroke_fill: tuple[int, int, int] | None = None) -> None:
    draw.text((WIDTH // 2, y), text, font=face, fill=fill, anchor='mm',
              stroke_width=stroke_width, stroke_fill=stroke_fill or fill)


def make_background() -> Image.Image:
    rng = random.Random(3103)
    img = Image.new('RGB', (WIDTH, HEIGHT), PLUM_DARK)
    px = img.load()
    cx, cy = WIDTH * 0.48, HEIGHT * 0.45
    max_d = math.hypot(max(cx, WIDTH-cx), max(cy, HEIGHT-cy))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            d = math.hypot(x-cx, y-cy) / max_d
            light = max(0.0, 1.0 - d)
            grain = rng.uniform(-4.0, 4.0)
            r = int(PLUM_DARK[0] + (PLUM_LIGHT[0]-PLUM_DARK[0]) * light * 0.82 + grain)
            g = int(PLUM_DARK[1] + (PLUM_LIGHT[1]-PLUM_DARK[1]) * light * 0.72 + grain * 0.35)
            b = int(PLUM_DARK[2] + (PLUM_LIGHT[2]-PLUM_DARK[2]) * light * 0.88 + grain)
            px[x, y] = (max(0,min(255,r)), max(0,min(255,g)), max(0,min(255,b)))
    glow = Image.new('RGBA', (WIDTH, HEIGHT), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((110, 600, 1490, 2200), fill=(214, 169, 78, 34))
    glow = glow.filter(ImageFilter.GaussianBlur(180))
    return Image.alpha_composite(img.convert('RGBA'), glow).convert('RGB')


def paper_texture(size: tuple[int, int], seed: int) -> Image.Image:
    rng = random.Random(seed)
    w, h = size
    p = Image.new('RGB', size, IVORY)
    px = p.load()
    for y in range(h):
        for x in range(w):
            v = rng.randint(-7, 7)
            px[x, y] = tuple(max(0, min(255, c + v)) for c in IVORY)
    d = ImageDraw.Draw(p, 'RGBA')
    for _ in range(30):
        x = rng.randrange(0, w)
        y = rng.randrange(0, h)
        rw = rng.randrange(20, 130)
        rh = rng.randrange(10, 70)
        d.ellipse((x-rw, y-rh, x+rw, y+rh), fill=(120, 85, 50, rng.randrange(2, 8)))
    return p.filter(ImageFilter.GaussianBlur(0.2))


def draw_document(layer: Image.Image, center: tuple[int, int], size: tuple[int, int], angle: float,
                  seed: int, accent: str) -> None:
    w, h = size
    sheet = paper_texture(size, seed).convert('RGBA')
    d = ImageDraw.Draw(sheet, 'RGBA')
    margin = 75
    rng = random.Random(seed + 9)
    for row in range(15):
        y = 95 + row * 55
        length = rng.randint(int(w*0.47), int(w*0.78))
        d.line((margin, y, margin+length, y), fill=(INK[0], INK[1], INK[2], 95), width=3)
    num_face = font(FONT_REGULAR, 34)
    d.text((w-90, 38), str(40 + seed % 9), font=num_face, fill=(70,54,48,130), anchor='ra')
    if accent in {'blue','both'}:
        for row in (2, 4, 7, 11):
            y = 95 + row*55
            d.rectangle((margin-8, y-10, w-margin+5, y+13), fill=(*BLUE, 45))
            d.line((margin-5, y+18, w-margin-30, y+18), fill=(*BLUE, 210), width=5)
    if accent in {'red','both'}:
        for row in (1, 5, 8, 12):
            y = 95 + row*55
            d.rectangle((margin-8, y-10, w-margin+5, y+13), fill=(*RED, 42))
            d.line((margin+30, y+18, w-margin+10, y+18), fill=(*RED, 210), width=5)
    for i in range(7):
        x = rng.randint(120, w-150)
        y = rng.randint(130, h-120)
        color = (*BLUE, 210) if i % 2 == 0 else (*RED, 210)
        d.ellipse((x-32, y-16, x+34, y+16), outline=color, width=4)
    shadow = Image.new('RGBA', (w+100, h+100), (0,0,0,0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((48, 55, w+48, h+55), radius=14, fill=(10,5,8,125))
    shadow = shadow.filter(ImageFilter.GaussianBlur(23))
    shadow = shadow.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    sheet = sheet.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    sx = int(center[0]-shadow.width/2+10)
    sy = int(center[1]-shadow.height/2+18)
    layer.alpha_composite(shadow, (sx, sy))
    x = int(center[0]-sheet.width/2)
    y = int(center[1]-sheet.height/2)
    layer.alpha_composite(sheet, (x, y))


def draw_bookend(layer: Image.Image) -> None:
    art = Image.new('RGBA', (430, 610), (0,0,0,0))
    d = ImageDraw.Draw(art, 'RGBA')
    d.rounded_rectangle((72, 96, 366, 545), radius=34, fill=(0,0,0,95))
    d.rectangle((48, 474, 390, 565), fill=(0,0,0,105))
    d.rounded_rectangle((62, 56, 350, 518), radius=28, fill=(*MARBLE,255), outline=(236,230,209,235), width=7)
    d.rectangle((34, 465, 383, 555), fill=(183,184,177,255), outline=(232,226,205,235), width=6)
    rng = random.Random(33)
    for _ in range(15):
        x = rng.randint(75, 330)
        y = rng.randint(70, 490)
        pts = [(x,y)]
        for _ in range(4):
            x += rng.randint(-35,35)
            y += rng.randint(28,70)
            pts.append((x,y))
        d.line(pts, fill=(120,125,124,80), width=rng.randint(2,5))
    d.arc((85,78,320,390), 195, 295, fill=(255,255,247,100), width=10)
    art = art.rotate(-2.0, resample=Image.Resampling.BICUBIC, expand=True)
    layer.alpha_composite(art, (1050, 1310))


def draw_magnifying_glass(layer: Image.Image) -> None:
    art = Image.new('RGBA', (760, 760), (0,0,0,0))
    d = ImageDraw.Draw(art, 'RGBA')
    d.ellipse((98, 80, 558, 540), outline=(0,0,0,100), width=48)
    d.line((490, 495, 680, 685), fill=(0,0,0,100), width=72)
    d.ellipse((76, 58, 536, 518), fill=(205,225,230,34), outline=(*GOLD_LIGHT,255), width=36)
    d.ellipse((108, 90, 504, 486), outline=(*GOLD,250), width=18)
    d.arc((130,112,485,470), 196, 292, fill=(255,248,218,125), width=17)
    d.arc((165,148,450,430), 203, 268, fill=(255,255,255,80), width=8)
    d.line((475, 475, 672, 672), fill=(*GOLD,255), width=62)
    d.line((482, 482, 666, 666), fill=(*GOLD_LIGHT,210), width=18)
    d.ellipse((627,627,704,704), fill=(*GOLD,255), outline=(*GOLD_LIGHT,255), width=8)
    art = art.rotate(11, resample=Image.Resampling.BICUBIC, expand=True)
    layer.alpha_composite(art, (265, 1235))


def draw_cover(output: Path) -> None:
    img = make_background().convert('RGBA')
    panel = Image.new('RGBA', (WIDTH, HEIGHT), (0,0,0,0))
    pd = ImageDraw.Draw(panel, 'RGBA')
    pd.rounded_rectangle((92, 92, WIDTH-92, HEIGHT-92), radius=12, outline=(*GOLD,235), width=5)
    pd.rounded_rectangle((112, 112, WIDTH-112, HEIGHT-112), radius=9, outline=(*GOLD_LIGHT,90), width=2)
    for xsign in (-1,1):
        for ysign in (-1,1):
            cx = 150 if xsign < 0 else WIDTH-150
            cy = 150 if ysign < 0 else HEIGHT-150
            pd.arc((cx-45,cy-45,cx+45,cy+45), 0, 360, fill=(*GOLD_LIGHT,145), width=3)
            pd.line((cx, cy-65*ysign, cx, cy-22*ysign), fill=(*GOLD,155), width=3)
            pd.line((cx-65*xsign, cy, cx-22*xsign, cy), fill=(*GOLD,155), width=3)
    img = Image.alpha_composite(img, panel)

    art = Image.new('RGBA', (WIDTH, HEIGHT), (0,0,0,0))
    ad = ImageDraw.Draw(art, 'RGBA')
    ad.polygon([(120,1390),(1480,1340),(1510,2080),(90,2140)], fill=(50,30,31,230))
    for y in range(1410, 2110, 35):
        ad.line((110,y,1490,y-45), fill=(95,54,38,55), width=3)
    draw_document(art, (640, 1585), (760, 950), -6.0, 43, 'blue')
    draw_document(art, (920, 1580), (760, 950), 5.0, 44, 'red')
    ad.rectangle((775, 1190, 835, 1970), fill=(18,10,18,115))
    ad.line((805,1190,805,1970), fill=(239,214,154,80), width=3)
    draw_bookend(art)
    draw_magnifying_glass(art)
    art = art.filter(ImageFilter.GaussianBlur(0.15))
    img = Image.alpha_composite(img, art)

    d = ImageDraw.Draw(img)
    series_face = font(FONT_SMALLCAPS, 44)
    title_face = font(FONT_BOLD, 172)
    author_face = font(FONT_SMALLCAPS, 72)
    subtitle_face = font(FONT_ITALIC, 40)

    add_tracking(d, 'THE BLACKWOOD RIDGE MYSTERIES · BOOK 3', (WIDTH/2, 215), series_face, GOLD_LIGHT, 3.0)
    d.line((280, 278, 1320, 278), fill=(*GOLD, 180), width=3)
    d.ellipse((792,267,808,283), fill=GOLD_LIGHT)
    centered(d, 'THE', 410, font(FONT_SMALLCAPS, 74), GOLD_LIGHT)
    centered(d, 'CHALLENGER', 585, title_face, IVORY, stroke_width=3, stroke_fill=PLUM_DARK)
    centered(d, 'A BLACKWOOD RIDGE MYSTERY', 745, subtitle_face, GOLD_LIGHT)
    d.line((400, 805, 1200, 805), fill=(*GOLD, 145), width=3)

    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0,0,0,0))
    od = ImageDraw.Draw(overlay, 'RGBA')
    od.rectangle((125, 2180, 1475, 2400), fill=(22, 9, 28, 176))
    overlay = overlay.filter(ImageFilter.GaussianBlur(12))
    img = Image.alpha_composite(img, overlay)
    d = ImageDraw.Draw(img)
    add_tracking(d, 'VESPER BLYTHE', (WIDTH/2, 2285), author_face, GOLD_LIGHT, 5.0)
    centered(d, 'An atmospheric archival mystery', 2380, font(FONT_ITALIC, 36), IVORY)

    img = img.convert('RGB').filter(ImageFilter.UnsharpMask(radius=1.4, percent=115, threshold=3))
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, 'JPEG', quality=96, subsampling=0, dpi=(DPI,DPI), optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('dist/The-Challenger-cover.jpg'))
    args = parser.parse_args()
    draw_cover(args.output)
    with Image.open(args.output) as im:
        if im.size != (WIDTH, HEIGHT) or im.mode != 'RGB' or im.format != 'JPEG':
            raise SystemExit(f'cover validation failed: {im.format=} {im.mode=} {im.size=}')
    print(args.output)


if __name__ == '__main__':
    main()
