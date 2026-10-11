#!/usr/bin/env python3
"""Deterministic SVG art for Blackwood Ridge social cards.

Styles: valley-dusk, gaslight, window, garden. Colors mirror
marketing/brand.yaml (ink / ivory / gold families) — if you change brand
colors, change them here too.

Used by generate.py; can also run standalone:
    python3 ridge_art.py valley-dusk 7 out.svg
"""
import random
import sys

INK = "#0E060F"
INK_WARM = "#241019"
WALNUT = "#3A2418"
IVORY = "#F7F2E4"
IVORY_MUTED = "#DFD5C2"
GOLD = "#D8A84E"
GOLD_LIGHT = "#F5E2B0"
GOLD_SHADOW = "#8C601A"

FOG_OPACITY = {"valley-dusk": 0.08, "gaslight": 0.12, "window": 0.0, "garden": 0.10}


def defs(fog_op):
    return f"""<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{INK}"/>
    <stop offset="0.55" stop-color="{INK_WARM}"/>
    <stop offset="0.85" stop-color="{GOLD_SHADOW}"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{GOLD_SHADOW}" stop-opacity="0.5"/>
    <stop offset="1" stop-color="{GOLD_SHADOW}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="night" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{INK}"/>
    <stop offset="1" stop-color="{INK_WARM}"/>
  </linearGradient>
  <radialGradient id="warm" cx="0.5" cy="0.42" r="0.75">
    <stop offset="0" stop-color="{GOLD_LIGHT}" stop-opacity="0.95"/>
    <stop offset="0.55" stop-color="{GOLD}" stop-opacity="0.55"/>
    <stop offset="1" stop-color="{GOLD_SHADOW}" stop-opacity="0.2"/>
  </radialGradient>
  <radialGradient id="lamp" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{GOLD_LIGHT}" stop-opacity="0.9"/>
    <stop offset="0.35" stop-color="{GOLD}" stop-opacity="0.4"/>
    <stop offset="1" stop-color="{GOLD}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="fog" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{IVORY}" stop-opacity="0"/>
    <stop offset="0.5" stop-color="{IVORY}" stop-opacity="{fog_op}"/>
    <stop offset="1" stop-color="{IVORY}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="facade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{WALNUT}" stop-opacity="0"/>
    <stop offset="0.35" stop-color="{WALNUT}" stop-opacity="0.35"/>
  </linearGradient>
  <radialGradient id="vignette" cx="0.5" cy="0.5" r="0.72">
    <stop offset="0.55" stop-color="{INK}" stop-opacity="0"/>
    <stop offset="1" stop-color="{INK}" stop-opacity="0.55"/>
  </radialGradient>
</defs>"""


def ridge(rng, w, h, base_y, amp, steps):
    pts = []
    y = base_y
    for i in range(steps + 1):
        x = w * i / steps
        pts.append((x, y))
        y += rng.uniform(-amp, amp)
        y = max(h * 0.30, min(h * 0.88, y))
    return pts


def poly(pts, h, fill):
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d += f" L {pts[-1][0]:.1f},{h} L 0,{h} Z"
    return f'<path d="{d}" fill="{fill}"/>'


def valley_dusk(rng, w, h):
    parts = [f'<rect width="{w}" height="{h}" fill="url(#sky)"/>']
    for _ in range(46):
        x, y = rng.uniform(0, w), rng.uniform(0, h * 0.42)
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rng.uniform(0.4, 1.2):.2f}"'
            f' fill="{IVORY}" fill-opacity="{rng.uniform(0.12, 0.45):.2f}"/>'
        )
    parts.append(f'<ellipse cx="{w * 0.5:.0f}" cy="{h * 0.74:.0f}" rx="{w * 0.52:.0f}" ry="{h * 0.20:.0f}" fill="url(#glow)"/>')
    parts.append(poly(ridge(rng, w, h, h * 0.62, 16, 9), h, "#2E1620"))
    parts.append(f'<rect x="0" y="{h * 0.60:.0f}" width="{w}" height="{h * 0.16:.0f}" fill="url(#fog)"/>')
    parts.append(poly(ridge(rng, w, h, h * 0.72, 20, 8), h, "#1B0D14"))
    parts.append(f'<rect x="0" y="{h * 0.71:.0f}" width="{w}" height="{h * 0.17:.0f}" fill="url(#fog)"/>')
    parts.append(poly(ridge(rng, w, h, h * 0.84, 24, 7), h, INK))
    for _ in range(6):
        x, y = rng.uniform(w * 0.12, w * 0.88), rng.uniform(h * 0.87, h * 0.93)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rng.uniform(9, 18):.1f}" fill="url(#lamp)"/>')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.3" fill="{GOLD_LIGHT}" fill-opacity="0.95"/>')
    parts.append(f'<rect width="{w}" height="{h}" fill="url(#vignette)"/>')
    return parts


def gaslight(rng, w, h):
    parts = [f'<rect width="{w}" height="{h}" fill="url(#night)"/>']
    parts.append(f'<rect x="0" y="{h * 0.30:.0f}" width="{w}" height="{h * 0.50:.0f}" fill="url(#facade)"/>')
    parts.append(f'<rect x="0" y="{h * 0.52:.0f}" width="{w}" height="{h * 0.30:.0f}" fill="url(#fog)"/>')
    parts.append(f'<rect x="0" y="{h * 0.70:.0f}" width="{w}" height="{h * 0.26:.0f}" fill="url(#fog)"/>')
    parts.append(poly(ridge(rng, w, h, h * 0.86, 8, 6), h, "#0A040B"))
    for fx, fy in ((0.26, 0.40), (0.5, 0.34), (0.74, 0.44)):
        x, y, base = w * fx, h * fy, h * 0.84
        parts.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x:.0f}" y2="{base:.0f}" stroke="{IVORY_MUTED}" stroke-opacity="0.28" stroke-width="2.4"/>')
        parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{w * 0.20:.0f}" fill="url(#lamp)"/>')
        parts.append(f'<rect x="{x - 5:.0f}" y="{y - 9:.0f}" width="10" height="13" fill="none" stroke="{GOLD}" stroke-opacity="0.7" stroke-width="1.6"/>')
        parts.append(f'<circle cx="{x:.0f}" cy="{y - 2:.0f}" r="3.4" fill="{GOLD_LIGHT}" fill-opacity="0.95"/>')
        parts.append(f'<rect x="{x - 7:.0f}" y="{y - 13:.0f}" width="14" height="4" fill="{INK}"/>')
    parts.append(f'<rect width="{w}" height="{h}" fill="url(#vignette)"/>')
    return parts


def window(rng, w, h):
    parts = [f'<rect width="{w}" height="{h}" fill="url(#night)"/>']
    parts.append(f'<rect x="{w * 0.07:.0f}" y="{h * 0.05:.0f}" width="{w * 0.86:.0f}" height="{h * 0.90:.0f}" fill="#1A0C13"/>')
    wx0, wy0, wx1, wy1 = w * 0.27, h * 0.14, w * 0.73, h * 0.58
    parts.append(f'<rect x="{wx0:.0f}" y="{wy0:.0f}" width="{wx1 - wx0:.0f}" height="{wy1 - wy0:.0f}" rx="4" fill="url(#warm)"/>')
    sill = wy1 - h * 0.045
    x = wx0 + 8
    while x < wx1 - 10:
        bw = rng.uniform(5, 9)
        bh = rng.uniform(h * 0.045, h * 0.10)
        marked = rng.random() < 0.12
        parts.append(
            f'<rect x="{x:.0f}" y="{sill - bh:.0f}" width="{bw:.1f}" height="{bh:.0f}"'
            f' fill="{GOLD if marked else INK}" fill-opacity="{0.85 if marked else 0.6}"/>'
        )
        x += bw + rng.uniform(1.5, 4)
    mids = (wx0 + wx1) / 2
    parts.append(f'<rect x="{mids - 2:.0f}" y="{wy0:.0f}" width="4" height="{wy1 - wy0:.0f}" fill="{INK}"/>')
    for fy in (0.36, 0.50):
        y = h * fy
        parts.append(f'<rect x="{wx0:.0f}" y="{y - 2:.0f}" width="{wx1 - wx0:.0f}" height="4" fill="{INK}"/>')
    parts.append(f'<rect x="{wx0 - 10:.0f}" y="{wy1:.0f}" width="{wx1 - wx0 + 20:.0f}" height="{h * 0.02:.0f}" fill="#120709"/>')
    lx = w * 0.86
    parts.append(f'<line x1="{lx:.0f}" y1="{h * 0.30:.0f}" x2="{lx:.0f}" y2="{h * 0.52:.0f}" stroke="{IVORY_MUTED}" stroke-opacity="0.25" stroke-width="2"/>')
    parts.append(f'<circle cx="{lx:.0f}" cy="{h * 0.29:.0f}" r="{w * 0.11:.0f}" fill="url(#lamp)"/>')
    parts.append(f'<circle cx="{lx:.0f}" cy="{h * 0.29:.0f}" r="3" fill="{GOLD_LIGHT}" fill-opacity="0.95"/>')
    parts.append(f'<rect width="{w}" height="{h}" fill="url(#vignette)"/>')
    return parts


def garden(rng, w, h):
    parts = [f'<rect width="{w}" height="{h}" fill="url(#night)"/>']
    parts.append(f'<circle cx="{w * 0.78:.0f}" cy="{h * 0.18:.0f}" r="{w * 0.075:.0f}" fill="url(#lamp)"/>')
    parts.append(f'<circle cx="{w * 0.78:.0f}" cy="{h * 0.18:.0f}" r="{w * 0.05:.0f}" fill="{GOLD_LIGHT}" fill-opacity="0.55"/>')
    parts.append(f'<rect x="0" y="{h * 0.82:.0f}" width="{w}" height="{h * 0.18:.0f}" fill="#100709"/>')
    spots = []
    y = h * 0.34
    while y < h * 0.80:
        x = w * rng.uniform(0.05, 0.10)
        while x < w * 0.94:
            spots.append((x, y))
            x += w * 0.072 * rng.uniform(0.85, 1.18)
        y += h * 0.088 * rng.uniform(0.9, 1.1)
    gold_spots = set(rng.sample(range(len(spots)), min(9, len(spots))))
    for i, (x, y) in enumerate(spots):
        jx, jy = x + rng.uniform(-4, 4), y + rng.uniform(-3, 3)
        stem = rng.uniform(h * 0.035, h * 0.06)
        parts.append(f'<line x1="{jx:.1f}" y1="{jy:.1f}" x2="{jx:.1f}" y2="{jy + stem:.1f}" stroke="#3D2A1E" stroke-width="1.2"/>')
        if i in gold_spots:
            parts.append(f'<circle cx="{jx:.1f}" cy="{jy:.1f}" r="{rng.uniform(4.5, 6):.1f}" fill="{GOLD}" fill-opacity="0.95"/>')
            parts.append(f'<circle cx="{jx:.1f}" cy="{jy:.1f}" r="1.6" fill="{GOLD_LIGHT}"/>')
        else:
            parts.append(
                f'<circle cx="{jx:.1f}" cy="{jy:.1f}" r="{rng.uniform(2.8, 4.2):.1f}"'
                f' fill="{IVORY_MUTED}" fill-opacity="{rng.uniform(0.22, 0.38):.2f}"/>'
            )
    parts.append(f'<rect x="0" y="{h * 0.70:.0f}" width="{w}" height="{h * 0.30:.0f}" fill="url(#fog)"/>')
    parts.append(f'<rect width="{w}" height="{h}" fill="url(#vignette)"/>')
    return parts


STYLES = {"valley-dusk": valley_dusk, "gaslight": gaslight, "window": window, "garden": garden}


def render(style, seed, w=540, h=540):
    if style not in STYLES:
        raise SystemExit(f"unknown art style: {style} (known: {', '.join(STYLES)})")
    rng = random.Random(f"{style}:{seed}")
    body = "".join(STYLES[style](rng, w, h))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"'
        f' viewBox="0 0 {w} {h}">{defs(FOG_OPACITY[style])}{body}</svg>'
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    with open(sys.argv[3], "w", encoding="utf-8") as f:
        f.write(render(sys.argv[1], int(sys.argv[2])))
