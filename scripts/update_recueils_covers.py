# -*- coding: utf-8 -*-
"""Met a jour la ligne de compteur des couvertures des Tomes I et II.

Les couvertures d'origine ont ete composees en 2021 avec la mention
« ONZE TEXTES · 2021-2024 » et « HUIT TEXTES · 2021-2024 ». L'ajout des
textes retrouves change ces compteurs. Le script efface la ligne par un
flou local, puis la redessine avec la meme typographie et le meme alignement.

Usage : python scripts/update_recueils_covers.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "covers"
W, H = 600, 900

SANS_SEMI = "C:/Windows/Fonts/seguisb.ttf"

COVERS = {
    "recueils-proses-poesies-t1-saisons-nature.webp": "SEIZE TEXTES · 1995-2024",
    "recueils-proses-poesies-t2-fantasque-merveilleux.webp": "DIX TEXTES · 1999-2024",
}

# Zone de la ligne de compteur, au-dessus des trois vignettes.
TEXT_BOX = (80, 510, 520, 545)
BASELINE_Y = 519


def draw_spaced(draw, y, text, fnt, fill, spacing):
    total = sum(draw.textlength(c, font=fnt) + spacing for c in text) - spacing
    x = (W - total) / 2
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + spacing


def patch(path: Path, label: str):
    im = Image.open(path).convert("RGB")
    box = TEXT_BOX
    region = im.crop(box).filter(ImageFilter.GaussianBlur(9))
    im.paste(region, box)

    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype(SANS_SEMI, 15)
    # Ombre legere, puis texte creme, comme sur les couvertures d'origine.
    draw_spaced(draw, BASELINE_Y + 1, label, fnt, (18, 20, 16), 2.6)
    draw_spaced(draw, BASELINE_Y, label, fnt, (235, 228, 210), 2.6)

    im.save(path, "WEBP", quality=90, method=6)
    print(f"{path.relative_to(ROOT)} {im.size} {path.stat().st_size} octets")


def main():
    for name, label in COVERS.items():
        patch(OUT / name, label)


if __name__ == "__main__":
    main()
