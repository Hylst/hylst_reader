# -*- coding: utf-8 -*-
"""Compose l'image sociale 1200x630 de La Bibliothèque de Hylst.

Fond sombre, titre, signature et quatre couvertures en éventail.
Usage : python scripts/make_social_share.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
COVERS = ROOT / "public" / "covers"
OUT = ROOT / "public" / "social-share.png"

W, H = 1200, 630
BG = (15, 14, 12)
TEXT = (246, 239, 228)
MUTED = (160, 144, 128)
ACCENT = (212, 149, 90)

SERIF_BOLD = "C:/Windows/Fonts/georgiab.ttf"
SERIF_ITALIC = "C:/Windows/Fonts/georgiai.ttf"
SANS = "C:/Windows/Fonts/segoeui.ttf"
SANS_SEMI = "C:/Windows/Fonts/seguisb.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def text(draw, xy, value, fnt, fill, spacing=0):
    x, y = xy
    if not spacing:
        draw.text((x, y), value, font=fnt, fill=fill)
        return
    for char in value:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + spacing


def cover(path: Path, height: int) -> Image.Image:
    im = Image.open(path).convert("RGBA")
    width = round(im.width * height / im.height)
    im = im.resize((width, height), Image.LANCZOS)
    radius = 10
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.width, im.height), radius=radius, fill=255)
    im.putalpha(mask)
    return im


def paste_rotated(base, im, center, angle, shadow=True):
    rotated = im.rotate(angle, expand=True, resample=Image.BICUBIC)
    x = round(center[0] - rotated.width / 2)
    y = round(center[1] - rotated.height / 2)
    if shadow:
        alpha = rotated.split()[3].point(lambda v: int(v * 0.55))
        shadow_im = Image.new("RGBA", rotated.size, (0, 0, 0, 255))
        shadow_im.putalpha(alpha)
        shadow_im = shadow_im.filter(ImageFilter.GaussianBlur(18))
        base.alpha_composite(shadow_im, (x + 8, y + 16))
    base.alpha_composite(rotated, (x, y))


# --- Fond : dégradé radial chaud + vignettage -------------------------------
base = Image.new("RGBA", (W, H), BG + (255,))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse((-260, 60, 620, 760), fill=(120, 74, 38, 90))
gdraw.ellipse((520, -180, 1400, 520), fill=(70, 52, 88, 70))
glow = glow.filter(ImageFilter.GaussianBlur(150))
base.alpha_composite(glow)

vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vdraw = ImageDraw.Draw(vignette)
vdraw.rectangle((0, 0, W, H), fill=(0, 0, 0, 40))
vignette = vignette.filter(ImageFilter.GaussianBlur(120))
base.alpha_composite(vignette)

draw = ImageDraw.Draw(base)

# --- Couvertures en éventail, à droite -------------------------------------
fan = [
    ("cover_quinte.webp", 430, (770, 318), -11),
    ("l-odyss-e-de-l-nergie.webp", 468, (925, 300), -2),
    ("les-ficelles-du-bonheur.webp", 440, (1082, 312), 9),
]
for name, height, center, angle in fan:
    image = cover(COVERS / name, height)
    paste_rotated(base, image, center, angle)

# --- Texte ------------------------------------------------------------------
kicker_font = font(SANS_SEMI, 19)
title_font = font(SERIF_BOLD, 68)
subtitle_font = font(SERIF_ITALIC, 27)
body_font = font(SANS, 21)
small_font = font(SANS, 16)

text(draw, (80, 118), "GEOFFROY STREIT  ·  HYLST", kicker_font, ACCENT, spacing=2.2)
draw.text((80, 160), "La Bibliothèque", font=title_font, fill=TEXT)
draw.text((80, 240), "de Hylst", font=title_font, fill=TEXT)

draw.line((82, 360, 182, 360), fill=ACCENT, width=3)

draw.text((80, 384), "Livres, proses, poésies et récits", font=subtitle_font, fill=TEXT)
draw.text((80, 424), "Une liseuse web hors-ligne, sans compte.", font=body_font, fill=MUTED)

draw.text((80, 556), "hylst.fr/books_reader", font=small_font, fill=ACCENT)
draw.text((278, 556), "© 2026 Geoffroy Streit  ·  Tous droits réservés", font=small_font, fill=MUTED)

# Filet lumineux en bas, rappel du bandeau de la liseuse.
for i in range(3):
    draw.line((0, H - 5 + i, W, H - 5 + i), fill=(212, 149, 90, 26 - i * 8))

OUT.parent.mkdir(parents=True, exist_ok=True)
base.convert("RGB").save(OUT, "PNG", optimize=True)
print(f"{OUT} : {base.width}x{base.height}, {OUT.stat().st_size / 1024:.0f} Ko")
