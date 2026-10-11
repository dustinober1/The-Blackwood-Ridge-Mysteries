#!/usr/bin/env python3
"""
Vector Cover, Spine, Wraparound, and Audiobook Cover Generator for:
The Blackwood Ridge Mysteries — Book 1: The Annotated Murder
Author: Vesper Blythe
Narrator (Audiobook): Annie Caldwell

Generates publication-ready SVG vector artwork and crisp raster exports:
1. Standalone Front / eBook Cover SVG (1600 x 2560, 5:8 ratio)
2. Standalone Print Spine SVG (calibrated for print trim and page count)
3. Full KDP Paperback Wraparound Cover SVG + Print-ready PDF (5.5" x 8.5" trim)
4. Standalone Audiobook Cover SVG (2400 x 2400 square) with "Narrated by Annie Caldwell"
5. High-resolution raster renders:
   - books/book-01/cover.jpeg (1600 x 2560, quality 95)
   - books/book-01/cover.png
   - books/book-01/export/cover.jpeg
   - books/book-01/dist/cover.jpeg
   - books/book-01/audiobook/audiobook_cover_2400.png
   - books/book-01/audiobook/audiobook_cover_3000.jpg
   - books/book-01/audiobook/audiobook_cover_3000.png
   - books/book-01/audiobook/audiobook_cover_thumb.png
6. EPUB compilation with embedded cover image via Pandoc.
"""

import argparse
import math
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Self-bootstrap using uv if cairosvg or PIL is missing or needs brew dynamic libraries
try:
    import cairosvg
    from PIL import Image
except ImportError:
    uv_bin = shutil.which("uv")
    if uv_bin and not os.environ.get("_BUILD_COVERS_BOOTSTRAPPED"):
        env = dict(os.environ)
        env["_BUILD_COVERS_BOOTSTRAPPED"] = "1"
        env["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"
        cmd = [
            uv_bin,
            "run",
            "--with",
            "cairosvg",
            "--with",
            "pillow",
            "python3",
            str(Path(__file__).resolve()),
        ] + sys.argv[1:]
        result = subprocess.run(cmd, env=env)
        sys.exit(result.returncode)
    else:
        sys.exit("Error: cairosvg and pillow are required. Run with uv or set DYLD_FALLBACK_LIBRARY_PATH.")

ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ROOT.parent.parent
DIST = ROOT / "dist"
EXPORT = ROOT / "export"
AUDIOBOOK = ROOT / "audiobook"

# Palette Tokens (Series Standard: dark plum / aubergine, near-black ink, brass, ivory)
COLOR_PLUM_TOP = "#190818"
COLOR_PLUM_MID = "#230C21"
COLOR_PLUM_LOW = "#140613"
COLOR_INK_DARK = "#090408"
COLOR_WOOD_DARK = "#120810"

COLOR_BRASS_LIGHT = "#F2D898"
COLOR_BRASS_BASE = "#CC9E40"
COLOR_BRASS_SHADOW = "#8C631B"
COLOR_BRASS_DARK = "#52370A"

COLOR_IVORY = "#F7F1E1"
COLOR_IVORY_MUTED = "#DCD2BC"

COLOR_PARCHMENT = "#F4ECE1"
COLOR_PARCHMENT_SHADOW = "#D8C7AD"
COLOR_SEPIA_INK = "#3B2215"
COLOR_TEA_STAIN = "#7A431E"
COLOR_CRIMSON_RIBBON = "#8A1C24"

FONT_SERIF = "Baskerville, 'Playfair Display', Georgia, 'Times New Roman', serif"
FONT_ITALIC = "Baskerville, Georgia, serif"


def get_shared_defs() -> str:
    """Returns SVG defs (gradients, filters, markers)."""
    return f"""
  <defs>
    <!-- Background Vignette Gradient -->
    <radialGradient id="vignetteGrad" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="{COLOR_PLUM_MID}" stop-opacity="0.9" />
      <stop offset="65%" stop-color="{COLOR_PLUM_TOP}" stop-opacity="1.0" />
      <stop offset="100%" stop-color="{COLOR_INK_DARK}" stop-opacity="1.0" />
    </radialGradient>

    <!-- Brass Gradient -->
    <linearGradient id="brassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_BRASS_LIGHT}" />
      <stop offset="35%" stop-color="{COLOR_BRASS_BASE}" />
      <stop offset="70%" stop-color="{COLOR_BRASS_LIGHT}" />
      <stop offset="100%" stop-color="{COLOR_BRASS_SHADOW}" />
    </linearGradient>

    <!-- Horizontal Brass Rule Gradient -->
    <linearGradient id="brassHGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{COLOR_BRASS_BASE}" stop-opacity="0.1" />
      <stop offset="25%" stop-color="{COLOR_BRASS_LIGHT}" stop-opacity="0.95" />
      <stop offset="50%" stop-color="{COLOR_BRASS_BASE}" stop-opacity="1.0" />
      <stop offset="75%" stop-color="{COLOR_BRASS_LIGHT}" stop-opacity="0.95" />
      <stop offset="100%" stop-color="{COLOR_BRASS_BASE}" stop-opacity="0.1" />
    </linearGradient>

    <!-- Open Book Left Page Gradient -->
    <linearGradient id="pageLeftGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{COLOR_PARCHMENT_SHADOW}" />
      <stop offset="12%" stop-color="{COLOR_PARCHMENT}" />
      <stop offset="85%" stop-color="{COLOR_PARCHMENT}" />
      <stop offset="100%" stop-color="{COLOR_PARCHMENT_SHADOW}" stop-opacity="0.8" />
    </linearGradient>

    <!-- Open Book Right Page Gradient -->
    <linearGradient id="pageRightGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{COLOR_PARCHMENT_SHADOW}" stop-opacity="0.9" />
      <stop offset="15%" stop-color="{COLOR_PARCHMENT}" />
      <stop offset="88%" stop-color="{COLOR_PARCHMENT}" />
      <stop offset="100%" stop-color="{COLOR_PARCHMENT_SHADOW}" />
    </linearGradient>

    <!-- Magnifying Glass Bezel Metallic Gradient -->
    <linearGradient id="bezelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_BRASS_LIGHT}" />
      <stop offset="30%" stop-color="{COLOR_BRASS_BASE}" />
      <stop offset="55%" stop-color="#FFF2BD" />
      <stop offset="80%" stop-color="{COLOR_BRASS_SHADOW}" />
      <stop offset="100%" stop-color="{COLOR_BRASS_DARK}" />
    </linearGradient>

    <!-- Wooden Handle Gradient -->
    <linearGradient id="handleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2D170B" />
      <stop offset="45%" stop-color="#6B3718" />
      <stop offset="75%" stop-color="#4A2610" />
      <stop offset="100%" stop-color="#1B0C05" />
    </linearGradient>

    <!-- Lens Glass Reflection Gradient -->
    <linearGradient id="lensReflection" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.45" />
      <stop offset="40%" stop-color="#FFFFFF" stop-opacity="0.05" />
      <stop offset="70%" stop-color="#C2DCF2" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.25" />
    </linearGradient>

    <!-- Warm Amber Glow from Unseen Lantern -->
    <radialGradient id="lampGlow" cx="60%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#FFA834" stop-opacity="0.22" />
      <stop offset="45%" stop-color="#D97706" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0.0" />
    </radialGradient>

    <!-- Drop Shadows -->
    <filter id="shadowFilter" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="8" dy="16" stdDeviation="14" flood-color="#000000" flood-opacity="0.75" />
    </filter>
    <filter id="glassShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="14" dy="22" stdDeviation="16" flood-color="#000000" flood-opacity="0.8" />
    </filter>
  </defs>
"""


def generate_corner_ornament(x: float, y: float, size: float = 64, flip_x: bool = False, flip_y: bool = False) -> str:
    """Generates Victorian brass corner filigree."""
    sx = -1 if flip_x else 1
    sy = -1 if flip_y else 1
    return f"""
    <g transform="translate({x}, {y}) scale({sx}, {sy})">
      <path d="M 0,0 L {size},0 C {size*0.5},0 {size*0.3},{size*0.2} {size*0.2},{size*0.3} C {size*0.2},{size*0.5} 0,{size*0.5} 0,{size} Z" fill="url(#brassGrad)" opacity="0.85" />
      <circle cx="{size*0.35}" cy="{size*0.35}" r="{size*0.08}" fill="{COLOR_BRASS_LIGHT}" />
      <path d="M 6,6 L {size*0.7},6 C {size*0.4},6 {size*0.25},{size*0.15} {size*0.15},{size*0.25} C {size*0.15},{size*0.4} 6,{size*0.4} 6,{size*0.7} Z" fill="none" stroke="{COLOR_BRASS_BASE}" stroke-width="1.5" />
    </g>
    """


def generate_book_and_magnifier_illustration(cx: float, cy: float, scale: float = 1.0) -> str:
    """
    Renders the signature archival mystery scene:
    Antique open ledger with Latin marginalia + brass magnifying glass.
    """
    return f"""
  <g id="illustration-group" transform="translate({cx}, {cy}) scale({scale})">
    <!-- Ambient Warm Lantern Glow -->
    <ellipse cx="60" cy="-20" rx="640" ry="460" fill="url(#lampGlow)" />

    <!-- Open Book Shadow -->
    <ellipse cx="0" cy="220" rx="540" ry="60" fill="#000000" opacity="0.6" filter="url(#shadowFilter)" />

    <!-- Outer Leather Binding / Book Cover Edges -->
    <rect x="-530" y="-210" width="1060" height="420" rx="16" fill="#2E180E" stroke="#4A2616" stroke-width="4" />
    <rect x="-525" y="-205" width="1050" height="410" rx="12" fill="#1C0D07" />

    <!-- Gilded Edge Trim -->
    <path d="M -520,-200 L 520,-200 L 526,200 L -526,200 Z" fill="#6B4B1B" opacity="0.5" />

    <!-- Left Open Page -->
    <path d="M -505,-190 C -360,-200 -180,-195 -10,-182 L -10,188 C -180,180 -360,182 -505,195 Z"
          fill="url(#pageLeftGrad)" stroke="#C7B295" stroke-width="1.5" filter="url(#shadowFilter)" />

    <!-- Right Open Page -->
    <path d="M 10,-182 C 180,-195 360,-200 505,-190 L 505,195 C 360,182 180,180 10,188 Z"
          fill="url(#pageRightGrad)" stroke="#C7B295" stroke-width="1.5" filter="url(#shadowFilter)" />

    <!-- Book Gutter Shadow -->
    <rect x="-14" y="-185" width="28" height="375" fill="#000000" opacity="0.32" />
    <line x1="0" y1="-185" x2="0" y2="190" stroke="#8C6E4A" stroke-width="2.5" />

    <!-- Left Page: Faint Historical Ledger Lines and Entries -->
    <g opacity="0.75">
      <!-- Ledger Header -->
      <text x="-480" y="-155" font-family="{FONT_SERIF}" font-size="14" font-weight="bold" fill="{COLOR_SEPIA_INK}" letter-spacing="2px">BLACKWOOD RIDGE HISTORICAL REGISTER • 1842</text>
      <line x1="-480" y1="-146" x2="-40" y2="-146" stroke="{COLOR_SEPIA_INK}" stroke-width="1" opacity="0.6" />
      <line x1="-480" y1="-142" x2="-40" y2="-142" stroke="{COLOR_SEPIA_INK}" stroke-width="0.5" opacity="0.4" />

      <!-- Columns -->
      <line x1="-390" y1="-142" x2="-390" y2="160" stroke="#CBB99E" stroke-width="0.8" />
      <line x1="-220" y1="-142" x2="-220" y2="160" stroke="#CBB99E" stroke-width="0.8" />

      <!-- Sample Handwritten Ledger Rows -->
      <text x="-475" y="-115" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Oct 4</text>
      <text x="-375" y="-115" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Lot 14: Ridge Parcel</text>
      <text x="-205" y="-115" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">140 Acres / Survey Sealed</text>

      <text x="-475" y="-80" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Oct 9</text>
      <text x="-375" y="-80" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Minister E. Townsend</text>
      <text x="-205" y="-80" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Non casus. Equus, via nota.</text>

      <text x="-475" y="-45" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Oct 16</text>
      <text x="-375" y="-45" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Pike Inquiry Rec.</text>
      <text x="-205" y="-45" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}" opacity="0.85">Iudex emptus. S.R. iussit.</text>

      <!-- Faded Hand-drawn Margin Note (Eleanor's / Callie's finding) -->
      <g transform="translate(-485, 30) rotate(-4)">
        <path d="M 0,0 C 30,-8 90,-4 130,-12" fill="none" stroke="{COLOR_SEPIA_INK}" stroke-width="1.8" opacity="0.6" />
        <text x="10" y="-16" font-family="{FONT_ITALIC}" font-style="italic" font-weight="bold" font-size="16" fill="#6B2814">
          † Linea vera abest tres gradus...
        </text>
        <text x="12" y="16" font-family="{FONT_ITALIC}" font-size="13" fill="#6B2814" opacity="0.9">
          (the true line lies three degrees off)
        </text>
      </g>
    </g>

    <!-- Right Page: Margin Annotation with Tea Stain -->
    <g>
      <!-- Subtle Text Columns on Right Page -->
      <g opacity="0.65">
        <text x="40" y="-155" font-family="{FONT_SERIF}" font-size="14" font-weight="bold" fill="{COLOR_SEPIA_INK}" letter-spacing="2px">CATALOGUE OF COUNTY ACQUISITIONS</text>
        <line x1="40" y1="-146" x2="480" y2="-146" stroke="{COLOR_SEPIA_INK}" stroke-width="1" opacity="0.6" />
        <text x="45" y="-115" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}">Folio 82: Keystone transcriptions by J. Wren.</text>
        <text x="45" y="-80" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}">Surveyor's Prayer inscribed at north lintel.</text>
        <text x="45" y="-45" font-family="{FONT_ITALIC}" font-size="13" fill="{COLOR_SEPIA_INK}">The Ralston lot (1962 donation) remains intact.</text>
      </g>

      <!-- The Bergamot Tea Stain (Tannin Ring on Lower Corner) -->
      <g transform="translate(390, 85)">
        <ellipse cx="0" cy="0" rx="55" ry="46" fill="none" stroke="{COLOR_TEA_STAIN}" stroke-width="5" opacity="0.32" />
        <ellipse cx="0" cy="0" rx="49" ry="41" fill="{COLOR_TEA_STAIN}" opacity="0.14" />
        <ellipse cx="3" cy="-2" rx="42" ry="34" fill="{COLOR_TEA_STAIN}" opacity="0.08" />
        <circle cx="58" cy="18" r="4" fill="{COLOR_TEA_STAIN}" opacity="0.25" />
        <circle cx="68" cy="28" r="2.5" fill="{COLOR_TEA_STAIN}" opacity="0.2" />
      </g>

      <!-- Crimson Silk Bookmark Ribbon flowing across right page -->
      <path d="M 0,-185 C 30,-80 80,40 140,195 C 155,200 170,192 180,185 C 130,50 80,-70 20,-185 Z"
            fill="{COLOR_CRIMSON_RIBBON}" opacity="0.9" />
      <path d="M 12,-180 C 40,-75 90,45 150,190" stroke="#B8444E" stroke-width="1.5" fill="none" opacity="0.7" />
    </g>

    <!-- The Brass Magnifying Glass (Angled over crucial text) -->
    <g transform="translate(180, 20) rotate(-32)" filter="url(#glassShadow)">
      <!-- Turned Hardwood Handle -->
      <g transform="translate(0, 140)">
        <path d="M -16,0 L 16,0 L 22,220 C 22,250 14,270 0,270 C -14,270 -22,250 -22,220 Z" fill="url(#handleGrad)" />
        <!-- Brass Rings & Collars on Handle -->
        <rect x="-18" y="0" width="36" height="14" rx="3" fill="url(#bezelGrad)" />
        <rect x="-20" y="30" width="40" height="8" rx="2" fill="url(#bezelGrad)" />
        <rect x="-22" y="120" width="44" height="10" rx="3" fill="url(#bezelGrad)" />
        <circle cx="0" cy="270" r="14" fill="url(#bezelGrad)" />
      </g>

      <!-- Outer Heavy Brass Bezel Rim -->
      <circle cx="0" cy="0" r="146" fill="url(#bezelGrad)" stroke="{COLOR_BRASS_DARK}" stroke-width="3" />
      <circle cx="0" cy="0" r="132" fill="{COLOR_BRASS_LIGHT}" opacity="0.8" />
      <circle cx="0" cy="0" r="126" fill="{COLOR_BRASS_DARK}" />

      <!-- Inner Magnified View Area -->
      <circle cx="0" cy="0" r="124" fill="{COLOR_PARCHMENT}" />

      <!-- Magnified Text Under Lens -->
      <g transform="translate(-108, -35)">
        <rect x="0" y="-18" width="216" height="74" fill="#FFF8EA" opacity="0.6" rx="4" />
        <text x="108" y="0" font-family="{FONT_SERIF}" font-size="21" font-weight="bold" fill="#1C0D05" text-anchor="middle">
          LINEA VERA ABEST
        </text>
        <text x="108" y="26" font-family="{FONT_SERIF}" font-size="18" font-style="italic" fill="#752912" text-anchor="middle">
          tres gradus ab inscripta
        </text>
        <line x1="20" y1="36" x2="196" y2="36" stroke="#9E3B1D" stroke-width="1.8" />
      </g>

      <!-- Glass Convex Lens Shimmer / Refraction Overlay -->
      <circle cx="0" cy="0" r="124" fill="url(#lensReflection)" />

      <!-- Optical Glare Arc -->
      <path d="M -90,-80 A 120,120 0 0,1 80,-90 A 108,108 0 0,0 -80,-60 Z" fill="#FFFFFF" opacity="0.55" />
    </g>
  </g>
"""


def generate_front_cover_svg() -> str:
    """Generates the 1600 x 2560 standalone front/ebook cover SVG."""
    w, h = 1600, 2560
    cx = w // 2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{get_shared_defs()}

  <!-- Canvas Background -->
  <rect width="{w}" height="{h}" fill="url(#vignetteGrad)" />

  <!-- Top Title Panel Tint -->
  <rect x="0" y="70" width="{w}" height="910" fill="{COLOR_PLUM_TOP}" opacity="0.85" />

  <!-- Bottom Author Panel Tint -->
  <rect x="0" y="2180" width="{w}" height="380" fill="{COLOR_INK_DARK}" opacity="0.95" />

  <!-- Central Archival Illustration -->
  {generate_book_and_magnifier_illustration(cx=800, cy=1540, scale=1.28)}

  <!-- Signature Double Brass Keylines -->
  <!-- Outer Keyline (54px inset, 5px stroke) -->
  <rect x="54" y="54" width="1492" height="2452" fill="none" stroke="url(#brassGrad)" stroke-width="5" />
  <!-- Inner Keyline (76px inset, 1.5px stroke) -->
  <rect x="76" y="76" width="1448" height="2408" fill="none" stroke="url(#brassGrad)" stroke-width="1.8" opacity="0.9" />

  <!-- Victorian Corner Filigree -->
  {generate_corner_ornament(82, 82, 70, flip_x=False, flip_y=False)}
  {generate_corner_ornament(1518, 82, 70, flip_x=True, flip_y=False)}
  {generate_corner_ornament(82, 2478, 70, flip_x=False, flip_y=True)}
  {generate_corner_ornament(1518, 2478, 70, flip_x=True, flip_y=True)}

  <!-- Series Header -->
  <g id="series-header">
    <text x="{cx}" y="152" font-family="{FONT_SERIF}" font-size="32" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="4px">
      THE BLACKWOOD RIDGE MYSTERIES  •  BOOK 1
    </text>
    <!-- Brass Rule Under Series Header -->
    <line x1="280" y1="214" x2="1320" y2="214" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="{cx-6},214 {cx},208 {cx+6},214 {cx},220" fill="{COLOR_BRASS_LIGHT}" />
  </g>

  <!-- Main Title -->
  <g id="title-group">
    <!-- Line 1: The -->
    <text x="{cx}" y="380" font-family="{FONT_ITALIC}" font-style="italic" font-size="132" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="3px">
      The
    </text>
    <!-- Line 2: Annotated -->
    <text x="{cx}" y="570" font-family="{FONT_SERIF}" font-size="182" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="4px">
      ANNOTATED
    </text>
    <!-- Line 3: Murder -->
    <text x="{cx}" y="770" font-family="{FONT_SERIF}" font-size="182" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="5px">
      MURDER
    </text>

    <!-- Brass Rule Under Title -->
    <line x1="380" y1="880" x2="1220" y2="880" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="{cx-8},880 {cx},872 {cx+8},880 {cx},888" fill="{COLOR_BRASS_LIGHT}" />
  </g>

  <!-- Author Lockup -->
  <g id="author-group">
    <line x1="480" y1="2230" x2="1120" y2="2230" stroke="url(#brassHGrad)" stroke-width="2" />
    <polygon points="{cx-6},2230 {cx},2225 {cx+6},2230 {cx},2235" fill="{COLOR_BRASS_LIGHT}" />

    <text x="{cx}" y="2330" font-family="{FONT_SERIF}" font-size="56" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="10px">
      VESPER BLYTHE
    </text>

    <line x1="520" y1="2390" x2="1080" y2="2390" stroke="url(#brassHGrad)" stroke-width="1.5" />
  </g>
</svg>
"""
    return svg


def generate_spine_svg(spine_width_in: float = 0.35, height_in: float = 8.5, dpi: int = 300) -> str:
    """Generates the standalone print spine SVG."""
    sw = int(spine_width_in * dpi)
    sh = int(height_in * dpi)
    cx = sw // 2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{sw}" height="{sh}" viewBox="0 0 {sw} {sh}">
{get_shared_defs()}

  <!-- Spine Background -->
  <rect width="{sw}" height="{sh}" fill="{COLOR_PLUM_TOP}" />
  <rect x="0" y="0" width="{sw}" height="{sh}" fill="url(#vignetteGrad)" opacity="0.6" />

  <!-- Vertical Keylines on Left & Right edge -->
  <line x1="4" y1="12" x2="4" y2="{sh-12}" stroke="url(#brassGrad)" stroke-width="1" opacity="0.5" />
  <line x1="{sw-4}" y1="12" x2="{sw-4}" y2="{sh-12}" stroke="url(#brassGrad)" stroke-width="1" opacity="0.5" />

  <!-- Top Series Numeral Badge -->
  <g transform="translate({cx}, 140)">
    <circle cx="0" cy="0" r="28" fill="{COLOR_INK_DARK}" stroke="url(#brassGrad)" stroke-width="2" />
    <text x="0" y="8" font-family="{FONT_SERIF}" font-size="24" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle">
      1
    </text>
  </g>

  <!-- Rotated Title Text -->
  <g transform="translate({cx}, {sh // 2 - 120}) rotate(90)">
    <text x="0" y="9" font-family="{FONT_SERIF}" font-size="28" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="5px">
      THE ANNOTATED MURDER
    </text>
  </g>

  <!-- Rotated Author Text -->
  <g transform="translate({cx}, {sh - 340}) rotate(90)">
    <text x="0" y="6" font-family="{FONT_SERIF}" font-size="20" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="4px">
      VESPER BLYTHE
    </text>
  </g>

  <!-- Bottom Publisher Colophon Symbol -->
  <g transform="translate({cx}, {sh - 90})">
    <path d="M -12,-8 C -4,-12 4,-12 12,-8 L 12,8 C 4,5 -4,5 -12,8 Z" fill="none" stroke="url(#brassGrad)" stroke-width="2" />
    <line x1="0" y1="-10" x2="0" y2="7" stroke="url(#brassGrad)" stroke-width="1.5" />
  </g>
</svg>
"""
    return svg


def generate_audiobook_cover_svg() -> str:
    """
    Generates the square 2400 x 2400 Audiobook Cover SVG with:
    - Series mark: THE BLACKWOOD RIDGE MYSTERIES • BOOK 1
    - Title: THE ANNOTATED MURDER
    - Signature open ledger & brass magnifier illustration
    - Author: VESPER BLYTHE
    - Narrator: Narrated by Annie Caldwell
    """
    size = 2400
    cx = size // 2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">
{get_shared_defs()}

  <!-- Background -->
  <rect width="{size}" height="{size}" fill="url(#vignetteGrad)" />

  <!-- Top Title Panel -->
  <rect x="0" y="60" width="{size}" height="760" fill="{COLOR_PLUM_TOP}" opacity="0.88" />

  <!-- Bottom Author/Narrator Panel -->
  <rect x="0" y="1960" width="{size}" height="440" fill="{COLOR_INK_DARK}" opacity="0.95" />

  <!-- Central Archival Illustration (Optimized for Square Canvas) -->
  {generate_book_and_magnifier_illustration(cx=cx, cy=1380, scale=1.35)}

  <!-- Signature Double Brass Keylines -->
  <!-- Outer Keyline (50px inset, 5px stroke) -->
  <rect x="50" y="50" width="2300" height="2300" fill="none" stroke="url(#brassGrad)" stroke-width="5" />
  <!-- Inner Keyline (72px inset, 1.8px stroke) -->
  <rect x="72" y="72" width="2256" height="2256" fill="none" stroke="url(#brassGrad)" stroke-width="1.8" opacity="0.9" />

  <!-- Corner Filigree -->
  {generate_corner_ornament(78, 78, 76, flip_x=False, flip_y=False)}
  {generate_corner_ornament(2322, 78, 76, flip_x=True, flip_y=False)}
  {generate_corner_ornament(78, 2322, 76, flip_x=False, flip_y=True)}
  {generate_corner_ornament(2322, 2322, 76, flip_x=True, flip_y=True)}

  <!-- Series Header -->
  <g id="series-header">
    <text x="{cx}" y="148" font-family="{FONT_SERIF}" font-size="34" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="5px">
      THE BLACKWOOD RIDGE MYSTERIES  •  BOOK 1
    </text>
    <line x1="420" y1="205" x2="1980" y2="205" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="{cx-7},205 {cx},198 {cx+7},205 {cx},212" fill="{COLOR_BRASS_LIGHT}" />
  </g>

  <!-- Title Lockup -->
  <g id="title-group">
    <!-- Line 1: The -->
    <text x="{cx}" y="340" font-family="{FONT_ITALIC}" font-style="italic" font-size="124" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="3px">
      The
    </text>
    <!-- Line 2: Annotated -->
    <text x="{cx}" y="520" font-family="{FONT_SERIF}" font-size="172" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="5px">
      ANNOTATED
    </text>
    <!-- Line 3: Murder -->
    <text x="{cx}" y="705" font-family="{FONT_SERIF}" font-size="172" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="5px">
      MURDER
    </text>

    <!-- Brass Rule Under Title -->
    <line x1="560" y1="785" x2="1840" y2="785" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="{cx-8},785 {cx},777 {cx+8},785 {cx},793" fill="{COLOR_BRASS_LIGHT}" />
  </g>

  <!-- Bottom Lockup: Author and Narrator Annie Caldwell -->
  <g id="bottom-credits">
    <!-- Top Divider -->
    <line x1="580" y1="2010" x2="1820" y2="2010" stroke="url(#brassHGrad)" stroke-width="2.2" />
    <polygon points="{cx-6},2010 {cx},2004 {cx+6},2010 {cx},2016" fill="{COLOR_BRASS_LIGHT}" />

    <!-- Author Byline -->
    <text x="{cx}" y="2100" font-family="{FONT_SERIF}" font-size="62" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="10px">
      VESPER BLYTHE
    </text>

    <!-- Mid Divider with Small Lozenge -->
    <line x1="720" y1="2155" x2="1680" y2="2155" stroke="url(#brassHGrad)" stroke-width="1.5" />
    <circle cx="{cx}" cy="2155" r="5" fill="{COLOR_BRASS_LIGHT}" />

    <!-- Narrator Byline: Narrated by Annie Caldwell -->
    <text x="{cx}" y="2245" font-family="{FONT_ITALIC}" font-style="italic" font-size="48" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="3px">
      Narrated by Annie Caldwell
    </text>

    <!-- Base Fine Rule -->
    <line x1="840" y1="2295" x2="1560" y2="2295" stroke="url(#brassHGrad)" stroke-width="1.2" opacity="0.8" />
  </g>
</svg>
"""
    return svg


def generate_wraparound_svg(page_count: int = 100, trim_w_in: float = 5.5, trim_h_in: float = 8.5, dpi: int = 300) -> str:
    """
    Generates the complete KDP Paperback Wraparound Cover SVG:
    Back Cover (left) + Spine (center) + Front Cover (right) + 0.125" Bleed.
    """
    bleed_in = 0.125
    spine_w_in = max(0.32, page_count * 0.0025)  # minimum 0.32" for legible spine text
    total_w_in = bleed_in + trim_w_in + spine_w_in + trim_w_in + bleed_in
    total_h_in = bleed_in + trim_h_in + bleed_in

    w = int(total_w_in * dpi)
    h = int(total_h_in * dpi)

    bleed_px = int(bleed_in * dpi)
    trim_w_px = int(trim_w_in * dpi)
    trim_h_px = int(trim_h_in * dpi)
    spine_w_px = int(spine_w_in * dpi)

    back_x = bleed_px
    spine_x = back_x + trim_w_px
    front_x = spine_x + spine_w_px

    back_cx = back_x + trim_w_px // 2
    front_cx = front_x + trim_w_px // 2
    spine_cx = spine_x + spine_w_px // 2

    # Scale factor for front cover inside wraparound
    scale_fc_x = trim_w_px / 1600.0
    scale_fc_y = trim_h_px / 2560.0

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{get_shared_defs()}

  <!-- Background for Entire Wraparound -->
  <rect width="{w}" height="{h}" fill="url(#vignetteGrad)" />

  <!-- ==================== BACK COVER (LEFT) ==================== -->
  <g id="back-cover" transform="translate({back_x}, {bleed_px})">
    <!-- Back Cover Keyline Frame -->
    <rect x="54" y="54" width="{trim_w_px - 108}" height="{trim_h_px - 108}" fill="none" stroke="url(#brassGrad)" stroke-width="4.5" />
    <rect x="74" y="74" width="{trim_w_px - 148}" height="{trim_h_px - 148}" fill="none" stroke="url(#brassGrad)" stroke-width="1.8" opacity="0.85" />

    <!-- Corner Filigree -->
    {generate_corner_ornament(78, 78, 64, flip_x=False, flip_y=False)}
    {generate_corner_ornament(trim_w_px - 78, 78, 64, flip_x=True, flip_y=False)}
    {generate_corner_ornament(78, trim_h_px - 78, 64, flip_x=False, flip_y=True)}
    {generate_corner_ornament(trim_w_px - 78, trim_h_px - 78, 64, flip_x=True, flip_y=True)}

    <!-- Series Heading -->
    <text x="{trim_w_px // 2}" y="150" font-family="{FONT_SERIF}" font-size="28" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="4px">
      THE BLACKWOOD RIDGE MYSTERIES
    </text>
    <line x1="240" y1="195" x2="{trim_w_px - 240}" y2="195" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="{trim_w_px // 2 - 6},195 {trim_w_px // 2},190 {trim_w_px // 2 + 6},195 {trim_w_px // 2},200" fill="{COLOR_BRASS_LIGHT}" />

    <!-- Hook / Tagline -->
    <text x="{trim_w_px // 2}" y="280" font-family="{FONT_ITALIC}" font-style="italic" font-weight="bold" font-size="38" fill="{COLOR_IVORY}" text-anchor="middle">
      Some books hide their darkest secrets in the margins.
    </text>

    <!-- Synopsis Blurb Paragraphs with enhanced typography & spread -->
    <g transform="translate(130, 360)">
      <text font-family="{FONT_SERIF}" font-size="27" fill="{COLOR_IVORY}">
        <tspan x="0" dy="0">When a reclusive town historian is found poisoned at a rare book</tspan>
        <tspan x="0" dy="46">auction in the misty Blue Ridge foothills, antiquarian bookshop owner</tspan>
        <tspan x="0" dy="46">Callie Thorne is the only one who notices what the police missed:</tspan>
        <tspan x="0" dy="46">a coded message handwritten in the victim’s catalog.</tspan>

        <tspan x="0" dy="68">For Callie, marginalia isn’t just an academic curiosity — it’s a gift.</tspan>
        <tspan x="0" dy="46">Decoding the faded notes tucked inside old volumes is what she does</tspan>
        <tspan x="0" dy="46">better than anyone. But this time the trail leads far deeper than a</tspan>
        <tspan x="0" dy="46">single murder. Every note points toward a decades-old scandal buried</tspan>
        <tspan x="0" dy="46">in Blackwood Ridge’s founding families.</tspan>

        <tspan x="0" dy="68">The sheriff sees a meddling shopkeeper. The killer sees a threat that</tspan>
        <tspan x="0" dy="46">needs silencing. With an innocent man already in the crosshairs,</tspan>
        <tspan x="0" dy="46">Callie faces an impossible choice: let a killer walk free, or expose the</tspan>
        <tspan x="0" dy="46">truth and watch her community shatter.</tspan>
      </text>
    </g>

    <!-- Praise / Endorsement Box -->
    <g transform="translate({trim_w_px // 2}, 1320)">
      <line x1="-420" y1="0" x2="420" y2="0" stroke="url(#brassHGrad)" stroke-width="2" />
      <text x="0" y="58" font-family="{FONT_ITALIC}" font-style="italic" font-size="28" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle">
        "Smart, atmospheric bookish mystery with real emotional stakes."
      </text>
      <line x1="-420" y1="102" x2="420" y2="102" stroke="url(#brassHGrad)" stroke-width="2" />
    </g>

    <!-- Clean Barcode Reserved Box (Lower Right, 480 x 280 px) -->
    <g transform="translate({trim_w_px - 580}, {trim_h_px - 440})">
      <rect width="480" height="290" fill="#FFFFFF" rx="4" stroke="#D0D0D0" stroke-width="1.2" />
    </g>
  </g>

  <!-- ==================== SPINE (CENTER) ==================== -->
  <g id="spine" transform="translate({spine_x}, {bleed_px})">
    <rect width="{spine_w_px}" height="{trim_h_px}" fill="{COLOR_PLUM_TOP}" />
    <!-- Spine Vertical Rules -->
    <line x1="2" y1="20" x2="2" y2="{trim_h_px - 20}" stroke="url(#brassGrad)" stroke-width="1" opacity="0.6" />
    <line x1="{spine_w_px - 2}" y1="20" x2="{spine_w_px - 2}" y2="{trim_h_px - 20}" stroke="url(#brassGrad)" stroke-width="1" opacity="0.6" />

    <!-- Top Number 1 -->
    <g transform="translate({spine_w_px // 2}, 160)">
      <circle cx="0" cy="0" r="26" fill="{COLOR_INK_DARK}" stroke="url(#brassGrad)" stroke-width="2" />
      <text x="0" y="8" font-family="{FONT_SERIF}" font-size="22" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle">1</text>
    </g>

    <!-- Rotated Spine Title -->
    <g transform="translate({spine_w_px // 2}, {trim_h_px // 2 - 80}) rotate(90)">
      <text x="0" y="9" font-family="{FONT_SERIF}" font-size="26" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="4px">
        THE ANNOTATED MURDER
      </text>
    </g>

    <!-- Rotated Author -->
    <g transform="translate({spine_w_px // 2}, {trim_h_px - 380}) rotate(90)">
      <text x="0" y="6" font-family="{FONT_SERIF}" font-size="20" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="3px">
        VESPER BLYTHE
      </text>
    </g>
  </g>

  <!-- ==================== FRONT COVER (RIGHT) ==================== -->
  <g id="front-cover-wrap" transform="translate({front_x}, {bleed_px}) scale({scale_fc_x}, {scale_fc_y})">
    <!-- Outer Keyline -->
    <rect x="54" y="54" width="1492" height="2452" fill="none" stroke="url(#brassGrad)" stroke-width="5" />
    <!-- Inner Keyline -->
    <rect x="76" y="76" width="1448" height="2408" fill="none" stroke="url(#brassGrad)" stroke-width="1.8" opacity="0.9" />

    <!-- Corner Filigree -->
    {generate_corner_ornament(82, 82, 70, flip_x=False, flip_y=False)}
    {generate_corner_ornament(1518, 82, 70, flip_x=True, flip_y=False)}
    {generate_corner_ornament(82, 2478, 70, flip_x=False, flip_y=True)}
    {generate_corner_ornament(1518, 2478, 70, flip_x=True, flip_y=True)}

    <!-- Series Header -->
    <text x="800" y="152" font-family="{FONT_SERIF}" font-size="32" font-weight="bold" fill="{COLOR_BRASS_LIGHT}" text-anchor="middle" letter-spacing="4px">
      THE BLACKWOOD RIDGE MYSTERIES  •  BOOK 1
    </text>
    <line x1="280" y1="214" x2="1320" y2="214" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="794,214 800,208 806,214 800,220" fill="{COLOR_BRASS_LIGHT}" />

    <!-- Main Title -->
    <text x="800" y="380" font-family="{FONT_ITALIC}" font-style="italic" font-size="132" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="3px">
      The
    </text>
    <text x="800" y="570" font-family="{FONT_SERIF}" font-size="182" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="4px">
      ANNOTATED
    </text>
    <text x="800" y="770" font-family="{FONT_SERIF}" font-size="182" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="5px">
      MURDER
    </text>
    <line x1="380" y1="880" x2="1220" y2="880" stroke="url(#brassHGrad)" stroke-width="2.5" />
    <polygon points="792,880 800,872 808,880 800,888" fill="{COLOR_BRASS_LIGHT}" />

    <!-- Illustration -->
    {generate_book_and_magnifier_illustration(cx=800, cy=1540, scale=1.28)}

    <!-- Author -->
    <line x1="480" y1="2230" x2="1120" y2="2230" stroke="url(#brassHGrad)" stroke-width="2" />
    <polygon points="794,2230 800,2225 806,2230 800,2235" fill="{COLOR_BRASS_LIGHT}" />
    <text x="800" y="2330" font-family="{FONT_SERIF}" font-size="56" font-weight="bold" fill="{COLOR_IVORY}" text-anchor="middle" letter-spacing="10px">
      VESPER BLYTHE
    </text>
    <line x1="520" y1="2390" x2="1080" y2="2390" stroke="url(#brassHGrad)" stroke-width="1.5" />
  </g>
</svg>
"""
    return svg


def main():
    parser = argparse.ArgumentParser(description="Build SVGs, Covers, Spine, Audiobook, and EPUB for Book 1.")
    parser.add_argument("--page-count", type=int, default=100, help="Page count for spine thickness (default: 100)")
    args = parser.parse_args()

    print("======================================================================")
    print(" The Blackwood Ridge Mysteries — Book 1: The Annotated Murder")
    print(" Vector SVG Cover, Spine, Wraparound, and Audiobook Pipeline")
    print("======================================================================")

    DIST.mkdir(parents=True, exist_ok=True)
    EXPORT.mkdir(parents=True, exist_ok=True)
    AUDIOBOOK.mkdir(parents=True, exist_ok=True)

    # 1. Front Cover SVG
    print("\n1. Generating Standalone Front / eBook Cover SVG (1600 x 2560)...")
    front_svg = generate_front_cover_svg()
    front_svg_root = ROOT / "cover.svg"
    front_svg_dist = DIST / "cover.svg"
    front_svg_export = EXPORT / "cover.svg"

    front_svg_root.write_text(front_svg, encoding="utf-8")
    front_svg_dist.write_text(front_svg, encoding="utf-8")
    front_svg_export.write_text(front_svg, encoding="utf-8")
    print(f"   [OK] Wrote {front_svg_root} ({len(front_svg):,} bytes)")
    print(f"   [OK] Synced {front_svg_dist} and {front_svg_export}")

    # 2. Standalone Spine SVG
    print(f"\n2. Generating Standalone Spine SVG ({args.page_count} pages)...")
    spine_svg = generate_spine_svg()
    spine_svg_root = ROOT / "spine.svg"
    spine_svg_dist = DIST / "spine.svg"

    spine_svg_root.write_text(spine_svg, encoding="utf-8")
    spine_svg_dist.write_text(spine_svg, encoding="utf-8")
    print(f"   [OK] Wrote {spine_svg_root} ({len(spine_svg):,} bytes)")
    print(f"   [OK] Synced {spine_svg_dist}")

    # 3. Audiobook Cover SVG with Narrated by Annie Caldwell
    print("\n3. Generating Audiobook Cover SVG (2400 x 2400) with Narrated by Annie Caldwell...")
    audio_svg = generate_audiobook_cover_svg()
    audio_svg_path = AUDIOBOOK / "cover-audiobook.svg"
    audio_svg_root = ROOT / "cover-audiobook.svg"

    audio_svg_path.write_text(audio_svg, encoding="utf-8")
    audio_svg_root.write_text(audio_svg, encoding="utf-8")
    print(f"   [OK] Wrote {audio_svg_path} ({len(audio_svg):,} bytes)")
    print(f"   [OK] Synced {audio_svg_root}")

    # 4. Paperback Wraparound Cover SVG & Print PDF
    print(f"\n4. Generating Paperback Wraparound Cover SVG ({args.page_count} pages, 5.5x8.5 trim)...")
    wrap_svg = generate_wraparound_svg(page_count=args.page_count)
    wrap_svg_path = DIST / "cover-paperback-wraparound.svg"
    wrap_svg_path.write_text(wrap_svg, encoding="utf-8")
    print(f"   [OK] Wrote {wrap_svg_path} ({len(wrap_svg):,} bytes)")

    print("   Compiling Print-Ready PDF from Wraparound SVG via CairoSVG...")
    wrap_pdf_path = DIST / "the-annotated-murder-cover-paperback.pdf"
    cairosvg.svg2pdf(bytestring=wrap_svg.encode("utf-8"), write_to=str(wrap_pdf_path))
    print(f"   [OK] Wrote {wrap_pdf_path} ({wrap_pdf_path.stat().st_size:,} bytes)")

    # 5. Render High-Resolution Raster Outputs
    print("\n5. Rendering High-Resolution Raster Covers...")
    # Front Cover 1600 x 2560
    cover_png_path = ROOT / "cover.png"
    cover_jpeg_path = ROOT / "cover.jpeg"
    cover_export_jpeg = EXPORT / "cover.jpeg"
    cover_dist_jpeg = DIST / "cover.jpeg"

    print("   Rendering Front Cover PNG (1600 x 2560)...")
    cairosvg.svg2png(
        bytestring=front_svg.encode("utf-8"),
        write_to=str(cover_png_path),
        output_width=1600,
        output_height=2560,
    )
    print(f"   [OK] Wrote {cover_png_path} ({cover_png_path.stat().st_size:,} bytes)")

    # Convert to High Quality RGB JPEG (Quality 95)
    with Image.open(cover_png_path) as im:
        rgb_im = im.convert("RGB")
        rgb_im.save(cover_jpeg_path, format="JPEG", quality=95, subsampling=0)
        shutil.copyfile(cover_jpeg_path, cover_export_jpeg)
        shutil.copyfile(cover_jpeg_path, cover_dist_jpeg)
    print(f"   [OK] Wrote {cover_jpeg_path} ({cover_jpeg_path.stat().st_size:,} bytes)")
    print(f"   [OK] Synced {cover_export_jpeg} and {cover_dist_jpeg}")

    # Audiobook Cover 2400 x 2400 and 3000 x 3000
    print("\n   Rendering Audiobook Cover Raster Assets...")
    audio_png_2400 = AUDIOBOOK / "audiobook_cover_2400.png"
    audio_png_3000 = AUDIOBOOK / "audiobook_cover_3000.png"
    audio_jpg_3000 = AUDIOBOOK / "audiobook_cover_3000.jpg"
    audio_png_thumb = AUDIOBOOK / "audiobook_cover_thumb.png"

    cairosvg.svg2png(
        bytestring=audio_svg.encode("utf-8"),
        write_to=str(audio_png_2400),
        output_width=2400,
        output_height=2400,
    )
    print(f"   [OK] Wrote {audio_png_2400} ({audio_png_2400.stat().st_size:,} bytes)")

    cairosvg.svg2png(
        bytestring=audio_svg.encode("utf-8"),
        write_to=str(audio_png_3000),
        output_width=3000,
        output_height=3000,
    )
    print(f"   [OK] Wrote {audio_png_3000} ({audio_png_3000.stat().st_size:,} bytes)")

    with Image.open(audio_png_3000) as im:
        rgb_audio = im.convert("RGB")
        rgb_audio.save(audio_jpg_3000, format="JPEG", quality=95, subsampling=0)
        thumb = rgb_audio.resize((500, 500), Image.Resampling.LANCZOS)
        thumb.save(audio_png_thumb, format="PNG")
    print(f"   [OK] Wrote {audio_jpg_3000} ({audio_jpg_3000.stat().st_size:,} bytes)")
    print(f"   [OK] Wrote {audio_png_thumb}")

    # 6. Rebuild EPUB with Embedded Cover Image
    print("\n6. Rebuilding EPUB with the new vector-rendered cover...")
    build_sh = EXPORT / "build.sh"
    build_sh_content = f"""#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc is not installed."
  exit 1
fi

pandoc manuscript-combined.md \\
  -f markdown \\
  -t epub3 \\
  --toc --toc-depth=1 \\
  --metadata title="The Annotated Murder" \\
  --metadata author="Vesper Blythe" \\
  --metadata lang="en" \\
  --epub-cover-image cover.jpeg \\
  -o "the-annotated-murder.epub"

echo "Built the-annotated-murder.epub with embedded cover image"
"""
    build_sh.write_text(build_sh_content, encoding="utf-8")
    build_sh.chmod(0o755)

    res = subprocess.run([str(build_sh)], capture_output=True, text=True, cwd=EXPORT)
    if res.returncode == 0:
        print(f"   {res.stdout.strip()}")
    else:
        print(f"   EPUB build error: {res.stderr}")
        sys.exit(res.returncode)

    epub_path = EXPORT / "the-annotated-murder.epub"
    dist_epub_path = DIST / "the-annotated-murder.epub"
    shutil.copyfile(epub_path, dist_epub_path)
    print(f"   [OK] Verified {epub_path} ({epub_path.stat().st_size:,} bytes)")
    print(f"   [OK] Synced {dist_epub_path}")

    print("\nAll assets successfully generated, verified, and synchronized!")


if __name__ == "__main__":
    main()
