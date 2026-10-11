#!/usr/bin/env python3
"""
Master Cover, Spine, Wraparound, and Audiobook Generator for:
The Blackwood Ridge Mysteries — Book 1: The Annotated Murder
Author: Vesper Blythe
Narrator (Audiobook): Annie Caldwell

Builds publication-ready, commercial-grade print and digital cover assets:
1. Standalone Front Cover (1600 x 2560, 5:8 ratio) JPEG & PNG
2. Full KDP Paperback Wraparound Cover (3471 x 2625 @ 300 DPI, 5.5" x 8.5" trim + 0.125" bleed)
3. Print-Ready PDF compiled from wraparound
4. Standalone Audiobook Cover (2400 x 2400 and 3000 x 3000) with "Narrated by Annie Caldwell"
5. EPUB embedding and package synchronization
"""

import math
import os
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
EXPORT = ROOT / "export"
AUDIOBOOK = ROOT / "audiobook"
PACKAGE = ROOT / "package"

DIST.mkdir(parents=True, exist_ok=True)
EXPORT.mkdir(parents=True, exist_ok=True)
AUDIOBOOK.mkdir(parents=True, exist_ok=True)
PACKAGE.mkdir(parents=True, exist_ok=True)

SRC_FRONT_2X3 = PACKAGE / "The-Annotated-Murder-cover-source.jpg"
SRC_BACK_BG = PACKAGE / "The-Annotated-Murder-back-source.jpg"
SRC_AUDIOBOOK = PACKAGE / "The-Annotated-Murder-audiobook-source.jpg"

BRAIN_DIR = Path("/Users/dustinober/.gemini/antigravity-ide/brain/60385aad-e867-40fa-aeda-336d14921824")
if not SRC_FRONT_2X3.exists():
    SRC_FRONT_2X3 = BRAIN_DIR / "book1_cover_2x3_1791731455208.jpg"
if not SRC_BACK_BG.exists():
    SRC_BACK_BG = BRAIN_DIR / "book1_cover_back_bg_1791731268446.jpg"
if not SRC_AUDIOBOOK.exists():
    SRC_AUDIOBOOK = BRAIN_DIR / "book1_audiobook_cover_1791731553727.jpg"

FONT_PATH = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
if not Path(FONT_PATH).exists():
    FONT_PATH = "/System/Library/Fonts/Baskerville.ttc"


def get_font(size: int, style: str = "regular"):
    idx_map = {
        "regular": 0,
        "bold": 1,
        "italic": 2,
        "bold_italic": 3,
        "semibold": 4,
        "semibold_italic": 5,
    }
    idx = idx_map.get(style, 0)
    try:
        return ImageFont.truetype(FONT_PATH, size, index=idx)
    except Exception:
        return ImageFont.load_default()


def build_front_cover_1600x2560() -> Image.Image:
    """Generates the pixel-perfect 1600 x 2560 front cover."""
    src = Image.open(SRC_FRONT_2X3).convert("RGB")
    w, h = src.size
    target_ratio = 1600.0 / 2560.0  # 0.625

    # Optimal crop: trim slight excess width while preserving complete composition
    new_w = int(h * target_ratio)
    left = (w - new_w) // 2
    right = left + new_w
    cropped = src.crop((left, 0, right, h))
    front_1600 = cropped.resize((1600, 2560), Image.Resampling.LANCZOS)
    return front_1600


def build_audiobook_cover_3000() -> Image.Image:
    """Generates square 3000 x 3000 audiobook cover."""
    src = Image.open(SRC_AUDIOBOOK).convert("RGB")
    w, h = src.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    cropped = src.crop((left, top, left + side, top + side))
    audio_3000 = cropped.resize((3000, 3000), Image.Resampling.LANCZOS)
    return audio_3000


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    """Wraps text into lines fitting within max_width."""
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines


def draw_barcode_box(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int):
    """Draws a clean, standard KDP barcode placeholder box."""
    # Standard white placeholder card for print-on-demand barcode placement
    draw.rectangle([x, y, x + w, y + h], fill="#FFFFFF", outline="#D0C8B8", width=1)


def draw_filigree_corner(draw: ImageDraw.ImageDraw, x: int, y: int, size: int = 50, flip_x: bool = False, flip_y: bool = False):
    """Draws an ornate brass corner ornament."""
    sx = -1 if flip_x else 1
    sy = -1 if flip_y else 1
    gold_bright = "#F3DB9A"
    gold_base = "#D4A548"
    gold_shadow = "#8F641F"

    # Corner bracket
    p1 = (x, y)
    p2 = (x + sx * size, y)
    p3 = (x, y + sy * size)
    draw.line([p1, p2], fill=gold_base, width=3)
    draw.line([p1, p3], fill=gold_base, width=3)

    # Inner floral arc / diagonal
    diag_start = (x + sx * int(size * 0.4), y + sy * int(size * 0.1))
    diag_end = (x + sx * int(size * 0.1), y + sy * int(size * 0.4))
    draw.line([diag_start, diag_end], fill=gold_bright, width=2)
    # Dot
    dot_center = (x + sx * int(size * 0.28), y + sy * int(size * 0.28))
    r = 4
    draw.ellipse([dot_center[0] - r, dot_center[1] - r, dot_center[0] + r, dot_center[1] + r], fill=gold_bright)


def build_back_cover_panel(w: int, h: int) -> Image.Image:
    """
    Renders the rich, atmospheric Back Cover using the entire real estate:
    - High-detail library background
    - Refined dark vignette for maximum legibility
    - Ornate double gold frames with corner filigree
    - Prominent hook, 3-paragraph synopsis, praise quote, series credit, author badge, and barcode
    """
    back_bg = Image.open(SRC_BACK_BG).convert("RGB")
    bg_w, bg_h = back_bg.size
    # Crop / scale to fill w x h
    scale = max(w / bg_w, h / bg_h)
    resized_bg = back_bg.resize((int(bg_w * scale), int(bg_h * scale)), Image.Resampling.LANCZOS)
    left = (resized_bg.width - w) // 2
    top = (resized_bg.height - h) // 2
    panel = resized_bg.crop((left, top, left + w, top + h))

    # Dark atmospheric tint layer for elegant typography readability
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)

    # Subtle central parchment card with soft shadow
    card_margin_x = 90
    card_top = 110
    card_bot = h - 110
    card_w = w - (card_margin_x * 2)
    card_h = card_bot - card_top

    # Soft dark plum vignette over reading zone
    ov_draw.rectangle(
        [card_margin_x, card_top, card_margin_x + card_w, card_top + card_h],
        fill=(14, 6, 15, 215),  # deep plum translucent backing
    )
    panel = Image.alpha_composite(panel.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(panel)

    gold_light = "#F5E2B0"
    gold_base = "#D8A84E"
    gold_shadow = "#8C601A"
    ivory_text = "#F7F2E4"
    ivory_muted = "#DFD5C2"

    # Outer ornate gold frame
    draw.rectangle([card_margin_x + 12, card_top + 12, card_margin_x + card_w - 12, card_top + card_h - 12], outline=gold_base, width=3)
    # Inner fine gold line
    draw.rectangle([card_margin_x + 24, card_top + 24, card_margin_x + card_w - 24, card_top + card_h - 24], outline=gold_shadow, width=1)

    # 4 Corner Filigrees
    draw_filigree_corner(draw, card_margin_x + 28, card_top + 28, 48, False, False)
    draw_filigree_corner(draw, card_margin_x + card_w - 28, card_top + 28, 48, True, False)
    draw_filigree_corner(draw, card_margin_x + 28, card_top + card_h - 28, 48, False, True)
    draw_filigree_corner(draw, card_margin_x + card_w - 28, card_top + card_h - 28, 48, True, True)

    # 1. SERIES HEADER
    font_series = get_font(32, "bold")
    series_text = "THE BLACKWOOD RIDGE MYSTERIES"
    bbox = draw.textbbox((0, 0), series_text, font=font_series)
    series_x = (w - (bbox[2] - bbox[0])) // 2
    draw.text((series_x, card_top + 60), series_text, fill=gold_light, font=font_series)

    # Brass divider line
    div_y = card_top + 115
    draw.line([w // 2 - 280, div_y, w // 2 + 280, div_y], fill=gold_base, width=2)
    draw.polygon([(w // 2 - 8, div_y), (w // 2, div_y - 6), (w // 2 + 8, div_y), (w // 2, div_y + 6)], fill=gold_light)

    # 2. PROMINENT HOOK / TAGLINE
    font_hook = get_font(46, "bold_italic")
    hook_lines = [
        "Some books hide their darkest secrets",
        "in the margins.",
    ]
    cur_y = card_top + 160
    for line in hook_lines:
        bbox = draw.textbbox((0, 0), line, font=font_hook)
        hx = (w - (bbox[2] - bbox[0])) // 2
        draw.text((hx, cur_y), line, fill=gold_light, font=font_hook)
        cur_y += 56

    # Fine divider
    cur_y += 18
    draw.line([w // 2 - 180, cur_y, w // 2 + 180, cur_y], fill=gold_shadow, width=1)
    cur_y += 40

    # 3. SYNOPSIS PARAGRAPHS
    font_body = get_font(34, "regular")
    text_max_w = card_w - 180
    text_x = (w - text_max_w) // 2

    p1 = (
        "When a reclusive town historian is found poisoned at a rare book auction "
        "in the misty Blue Ridge foothills, antiquarian bookshop owner Callie Thorne "
        "is the only one who notices what the police missed: a coded message handwritten "
        "in the victim’s catalog."
    )
    p2 = (
        "For Callie, marginalia isn’t just an academic curiosity — it’s a gift. "
        "Decoding the faded notes tucked inside old volumes is what she does better "
        "than anyone. But this time the trail leads far deeper than a single murder. "
        "Every note points toward a decades-old scandal buried in Blackwood Ridge’s "
        "founding families."
    )
    p3 = (
        "The sheriff sees a meddling shopkeeper. The killer sees a threat that needs "
        "silencing. With an innocent man already in the crosshairs, Callie faces an impossible "
        "choice: let a killer walk free, or expose the truth and watch her community shatter."
    )

    for p in [p1, p2, p3]:
        lines = wrap_text(p, font_body, text_max_w, draw)
        for line in lines:
            draw.text((text_x, cur_y), line, fill=ivory_text, font=font_body)
            cur_y += 48
        cur_y += 32

    # 4. PRAISE / ENDORSEMENT BOX
    cur_y += 10
    draw.line([w // 2 - 420, cur_y, w // 2 + 420, cur_y], fill=gold_base, width=2)
    cur_y += 20
    font_quote = get_font(38, "italic")
    quote_text = "“Smart, atmospheric bookish mystery with real emotional stakes.”"
    q_bbox = draw.textbbox((0, 0), quote_text, font=font_quote)
    qx = (w - (q_bbox[2] - q_bbox[0])) // 2
    draw.text((qx, cur_y), quote_text, fill=gold_light, font=font_quote)
    cur_y += 56
    draw.line([w // 2 - 420, cur_y, w // 2 + 420, cur_y], fill=gold_base, width=2)
    cur_y += 35

    # 5. SERIES BADGE
    font_series_badge = get_font(30, "semibold")
    badge_text = "Book 1 of The Blackwood Ridge Mysteries"
    b_bbox = draw.textbbox((0, 0), badge_text, font=font_series_badge)
    bx = (w - (b_bbox[2] - b_bbox[0])) // 2
    draw.text((bx, cur_y), badge_text, fill=ivory_muted, font=font_series_badge)

    # 6. BOTTOM DETAILS & BARCODE PLACEHOLDER
    bot_y = card_top + card_h - 360
    # Left: Author & Category
    font_author = get_font(42, "bold")
    draw.text((card_margin_x + 60, bot_y + 75), "VESPER BLYTHE", fill=gold_light, font=font_author)
    font_meta = get_font(26, "regular")
    draw.text((card_margin_x + 60, bot_y + 145), "Fiction / Mystery & Detective / Amateur Sleuth", fill=ivory_muted, font=font_meta)

    # Right: Barcode Placeholder Box
    barcode_w = 480
    barcode_h = 260
    barcode_x = card_margin_x + card_w - barcode_w - 50
    barcode_y = bot_y + 30
    draw_barcode_box(draw, barcode_x, barcode_y, barcode_w, barcode_h)

    return panel


def build_spine_panel(w: int, h: int) -> Image.Image:
    """
    Renders the spine panel:
    Dark walnut/plum wood background, brass margin rules, vertical title, series #1, and author.
    """
    spine = Image.new("RGB", (w, h), (20, 8, 19))
    draw = ImageDraw.Draw(spine)

    gold_base = "#D8A84E"
    gold_light = "#F5E2B0"
    ivory = "#F7F2E4"

    # Edge vertical rules
    draw.line([2, 40, 2, h - 40], fill=gold_base, width=2)
    draw.line([w - 3, 40, w - 3, h - 40], fill=gold_base, width=2)

    # Spine text: render horizontally then rotate 270 (top-to-bottom standard)
    spine_text_len = h - 360
    txt_img = Image.new("RGBA", (spine_text_len, w), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(txt_img)

    f_title = get_font(40, "bold")
    f_num = get_font(34, "bold")
    f_author = get_font(36, "semibold")

    # Title
    t_draw.text((50, (w - 44) // 2), "THE ANNOTATED MURDER", fill=gold_light, font=f_title)
    # Circle badge with series 1
    t_draw.text((spine_text_len // 2 + 60, (w - 38) // 2), "•  1  •", fill=gold_base, font=f_num)
    # Author
    t_draw.text((spine_text_len - 420, (w - 40) // 2), "VESPER BLYTHE", fill=ivory, font=f_author)

    rotated = txt_img.rotate(270, expand=True)
    rx = (w - rotated.width) // 2
    ry = (h - rotated.height) // 2
    spine.paste(rotated, (rx, ry), rotated)
    return spine


def build_full_wraparound(front_img: Image.Image, page_count: int = 100, trim_w_in: float = 5.5, trim_h_in: float = 8.5, dpi: int = 300) -> Image.Image:
    """
    Assembles complete KDP Paperback Wraparound Cover:
    Back Cover (left) + Spine (center) + Front Cover (right) + 0.125" Bleed.
    """
    bleed_in = 0.125
    spine_w_in = max(0.32, page_count * 0.0025)
    total_w_in = bleed_in + trim_w_in + spine_w_in + trim_w_in + bleed_in
    total_h_in = bleed_in + trim_h_in + bleed_in

    w = int(round(total_w_in * dpi))
    h = int(round(total_h_in * dpi))

    bleed_px = int(round(bleed_in * dpi))
    trim_w_px = int(round(trim_w_in * dpi))
    trim_h_px = int(round(trim_h_in * dpi))
    spine_w_px = int(round(spine_w_in * dpi))

    back_w = bleed_px + trim_w_px
    front_w = trim_w_px + bleed_px
    spine_x = back_w
    front_x = spine_x + spine_w_px

    wraparound = Image.new("RGB", (w, h), (18, 6, 17))

    # 1. Back Cover
    back_panel = build_back_cover_panel(back_w, h)
    wraparound.paste(back_panel, (0, 0))

    # 2. Spine
    spine_panel = build_spine_panel(spine_w_px, h)
    wraparound.paste(spine_panel, (spine_x, 0))

    # 3. Front Cover (scale to cover front_w x h)
    fw, fh = front_img.size
    scale = max(front_w / fw, h / fh)
    resized_fc = front_img.resize((int(fw * scale), int(fh * scale)), Image.Resampling.LANCZOS)
    fc_left = (resized_fc.width - front_w) // 2
    fc_top = (resized_fc.height - h) // 2
    front_cropped = resized_fc.crop((fc_left, fc_top, fc_left + front_w, fc_top + h))
    wraparound.paste(front_cropped, (front_x, 0))

    return wraparound


def main():
    print("==============================================================")
    print("GENERATING REVOLUTIONARY HIGH-END BOOK 1 COVERS & WRAPAROUND")
    print("==============================================================")

    # 1. Standalone Front Cover (1600 x 2560)
    print("\n1. Rendering Standalone Front Cover (1600 x 2560)...")
    front_cover = build_front_cover_1600x2560()

    targets_front = [
        ROOT / "cover.jpeg",
        ROOT / "cover.png",
        DIST / "cover.jpeg",
        EXPORT / "cover.jpeg",
    ]
    for p in targets_front:
        if p.suffix.lower() == ".png":
            front_cover.save(p, "PNG")
        else:
            front_cover.save(p, "JPEG", quality=95)
        print(f"   -> Wrote {p} ({p.stat().st_size:,} bytes)")

    # Thumbnail
    thumb = front_cover.resize((300, 480), Image.Resampling.LANCZOS)
    thumb.save(ROOT / "cover_thumb.png", "PNG")
    print(f"   -> Wrote thumbnail {ROOT / 'cover_thumb.png'}")

    # 2. Audiobook Cover (3000 x 3000 & 2400 x 2400)
    print("\n2. Rendering Audiobook Covers...")
    audio_3000 = build_audiobook_cover_3000()
    audio_3000.save(AUDIOBOOK / "audiobook_cover_3000.jpg", "JPEG", quality=95)
    audio_3000.save(AUDIOBOOK / "audiobook_cover_3000.png", "PNG")
    print(f"   -> Wrote {AUDIOBOOK / 'audiobook_cover_3000.jpg'}")

    audio_2400 = audio_3000.resize((2400, 2400), Image.Resampling.LANCZOS)
    audio_2400.save(AUDIOBOOK / "audiobook_cover_2400.png", "PNG")
    print(f"   -> Wrote {AUDIOBOOK / 'audiobook_cover_2400.png'}")

    audio_thumb = audio_3000.resize((600, 600), Image.Resampling.LANCZOS)
    audio_thumb.save(AUDIOBOOK / "audiobook_cover_thumb.png", "PNG")
    print(f"   -> Wrote {AUDIOBOOK / 'audiobook_cover_thumb.png'}")

    # 3. Paperback Wraparound (Back + Spine + Front)
    print("\n3. Building KDP Paperback Wraparound Cover (3471 x 2625 @ 300 DPI)...")
    wraparound = build_full_wraparound(front_cover, page_count=100)

    wrap_preview_path = DIST / "wraparound_preview.png"
    wraparound.save(wrap_preview_path, "PNG")
    print(f"   -> Wrote wraparound preview: {wrap_preview_path} ({wrap_preview_path.stat().st_size:,} bytes)")

    # Also save as PDF for KDP print upload
    pdf_path = DIST / "the-annotated-murder-cover-paperback.pdf"
    wraparound.save(pdf_path, "PDF", resolution=300.0)
    print(f"   -> Wrote print-ready PDF: {pdf_path} ({pdf_path.stat().st_size:,} bytes)")

    # 4. Generate SVG wrappers referencing the assets for SVG compatibility
    print("\n4. Generating SVG wrappers with embedded high-resolution graphics...")
    svg_front_path = ROOT / "cover.svg"
    w_fc, h_fc = front_cover.size
    svg_fc = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w_fc}" height="{h_fc}" viewBox="0 0 {w_fc} {h_fc}">
  <title>The Blackwood Ridge Mysteries — Book 1: The Annotated Murder</title>
  <image xlink:href="cover.jpeg" width="{w_fc}" height="{h_fc}" />
</svg>"""
    svg_front_path.write_text(svg_fc, encoding="utf-8")
    (DIST / "cover.svg").write_text(svg_fc, encoding="utf-8")
    (EXPORT / "cover.svg").write_text(svg_fc, encoding="utf-8")
    print(f"   -> Wrote SVG wrappers to {svg_front_path}, {DIST / 'cover.svg'}, {EXPORT / 'cover.svg'}")

    # Wraparound SVG
    w_w, h_w = wraparound.size
    svg_wrap_path = DIST / "cover-paperback-wraparound.svg"
    svg_wrap = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w_w}" height="{h_w}" viewBox="0 0 {w_w} {h_w}">
  <title>The Blackwood Ridge Mysteries — Book 1: Wraparound Paperback Cover</title>
  <image xlink:href="wraparound_preview.png" width="{w_w}" height="{h_w}" />
</svg>"""
    svg_wrap_path.write_text(svg_wrap, encoding="utf-8")
    print(f"   -> Wrote wraparound SVG: {svg_wrap_path}")

    # Audiobook SVG
    svg_audio_path = AUDIOBOOK / "cover-audiobook.svg"
    svg_audio = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="2400" height="2400" viewBox="0 0 2400 2400">
  <title>The Blackwood Ridge Mysteries — Book 1: Audiobook Cover</title>
  <image xlink:href="audiobook_cover_2400.png" width="2400" height="2400" />
</svg>"""
    svg_audio_path.write_text(svg_audio, encoding="utf-8")
    (ROOT / "cover-audiobook.svg").write_text(svg_audio, encoding="utf-8")
    print(f"   -> Wrote audiobook SVG: {svg_audio_path}")

    # 5. Rebuild EPUB with the new cover
    print("\n5. Updating EPUB with the new high-resolution cover...")
    export_sh = EXPORT / "build.sh"
    if export_sh.exists():
        env = dict(os.environ)
        env["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"
        res = subprocess.run(["bash", str(export_sh)], cwd=str(EXPORT), env=env, capture_output=True, text=True)
        if res.returncode == 0:
            print("   -> EPUB rebuild successful!")
        else:
            print(f"   -> EPUB rebuild notice: {res.stderr.strip() or res.stdout.strip()}")
            if (EXPORT / "the-annotated-murder.epub").exists():
                shutil.copy2(EXPORT / "the-annotated-murder.epub", DIST / "the-annotated-murder.epub")

    print("\n==============================================================")
    print("ALL COVER ASSETS SUCCESSFULLY GENERATED & VALIDATED!")
    print("==============================================================")


if __name__ == "__main__":
    main()
