# -*- coding: utf-8 -*-
"""Compose les couvertures du Tome IV et du livre Sciences et technologie.

Les fonds sont des textures generees localement (GPU) et conservees dans
scripts/assets/covers/. La typographie est composee avec PIL : le texte reste
net, lisible en vignette et reproductible.

Usage : python scripts/make_book_covers.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "scripts" / "assets" / "covers"
OUT = ROOT / "public" / "covers"
W, H = 600, 900

SERIF_BOLD = "C:/Windows/Fonts/georgiab.ttf"
SERIF = "C:/Windows/Fonts/georgia.ttf"
SERIF_ITALIC = "C:/Windows/Fonts/georgiai.ttf"
SANS = "C:/Windows/Fonts/segoeui.ttf"
SANS_SEMI = "C:/Windows/Fonts/seguisb.ttf"
SANS_BOLD = "C:/Windows/Fonts/segoeuib.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def centered(draw, y, text, fnt, fill, spacing=0.0):
    if spacing:
        total = sum(draw.textlength(c, font=fnt) + spacing for c in text) - spacing
        x = (W - total) / 2
        for c in text:
            draw.text((x, y), c, font=fnt, fill=fill)
            x += draw.textlength(c, font=fnt) + spacing
        return
    width = draw.textlength(text, font=fnt)
    draw.text(((W - width) / 2, y), text, font=fnt, fill=fill)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def background(name: str, tint, tint_alpha: float, blur: float = 0.0) -> Image.Image:
    im = Image.open(ASSETS / name).convert("RGB")
    im = im.resize((W, H), Image.LANCZOS)
    if tint:
        overlay = Image.new("RGB", (W, H), tint)
        im = Image.blend(im, overlay, tint_alpha)
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    return im


def ornament(draw, cx, cy, color, size=26):
    """Petit losange double, dessine au trait."""
    for factor in (1.0, 0.55):
        half = size * factor
        draw.polygon(
            [(cx, cy - half), (cx + half, cy), (cx, cy + half), (cx - half, cy)],
            outline=color,
        )


def cover_tome4() -> Image.Image:
    im = background("tome4-paper.webp", (243, 236, 223), 0.18, blur=0.3)
    draw = ImageDraw.Draw(im)
    ink = (42, 36, 29)
    copper = (180, 104, 47)
    muted = (122, 74, 43)

    # Double filet de cadre.
    draw.rectangle([36, 36, W - 37, H - 37], outline=copper, width=2)
    draw.rectangle([46, 46, W - 47, H - 47], outline=(180, 104, 47, 90), width=1)

    centered(draw, 80, "RECUEILS DE PROSES ET POÉSIES FANTASQUES", font(SANS_SEMI, 13), muted, spacing=2.2)
    centered(draw, 106, "TOME IV", font(SANS_SEMI, 15), copper, spacing=5.0)

    ornament(draw, W // 2, 152, copper, 14)

    centered(draw, 220, "Carnets,", font(SERIF_BOLD, 78), ink)
    centered(draw, 320, "réflexions", font(SERIF_BOLD, 72), ink)
    centered(draw, 410, "& partages", font(SERIF_BOLD, 62), ink)

    draw.line([(W // 2 - 70, 516), (W // 2 + 70, 516)], fill=copper, width=2)
    ornament(draw, W // 2, 552, copper, 10)

    centered(draw, 605, "Hylst", font(SERIF_ITALIC, 44), ink)
    centered(draw, 668, "GEOFFROY STREIT", font(SANS, 14), muted, spacing=3.0)

    centered(draw, 790, "Textes retrouvés · 2003-2024", font(SERIF_ITALIC, 17), muted)
    return im


def cover_sciences() -> Image.Image:
    im = background("sciences-grid.webp", (237, 241, 243), 0.62, blur=0.4)
    draw = ImageDraw.Draw(im)
    ink = (26, 40, 48)
    blue = (31, 75, 99)
    amber = (181, 115, 43)

    # Bandeau technique.
    draw.rectangle([0, 0, W, 176], fill=blue)
    draw.rectangle([0, 176, W, 182], fill=amber)
    centered(draw, 62, "SCIENCES & TECHNOLOGIE", font(SANS_BOLD, 25), (255, 255, 255), spacing=3.4)
    centered(draw, 112, "ÉTUDE TECHNIQUE BIBLIOGRAPHIQUE", font(SANS, 12), (223, 232, 236), spacing=2.6)

    # Quadrillage discret sur le bandeau.
    for x in range(0, W, 20):
        draw.line([(x, 0), (x, 176)], fill=(255, 255, 255, 10), width=1)

    title_font = font(SERIF_BOLD, 38)
    lines = ["Analyse des solutions", "techniques mises en œuvre", "dans les jeux vidéos"]
    y = 284
    for line in lines:
        centered(draw, y, line, title_font, ink)
        y += 58

    draw.line([(W // 2 - 80, y + 30), (W // 2 + 80, y + 30)], fill=amber, width=2)

    centered(draw, y + 86, "Étude technique bibliographique", font(SANS, 17), blue, spacing=0.6)
    centered(draw, y + 122, "2001-2002", font(SANS_BOLD, 30), amber, spacing=2.5)

    # Cartouche de bas de couverture.
    draw.rectangle([64, 700, W - 65, 812], outline=blue, width=1)
    centered(draw, 724, "NFIO · PROMOTION 7 · 5e ANNÉE", font(SANS, 12), blue, spacing=2.0)
    centered(draw, 758, "Hylst (Geoffroy Streit)", font(SERIF_ITALIC, 24), ink)
    centered(draw, 838, "Édition numérique 2026", font(SANS, 15), blue, spacing=1.4)
    return im


def save(im: Image.Image, name: str):
    dest = OUT / name
    im.convert("RGB").save(dest, "WEBP", quality=90, method=6)
    print(f"{dest.relative_to(ROOT)} {im.size} {dest.stat().st_size} octets")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    save(cover_tome4(), "recueils-proses-poesies-t4-carnets-reflexions-partages.webp")
    save(cover_sciences(), "sciences-et-technologie-jeux-videos.webp")


if __name__ == "__main__":
    main()
