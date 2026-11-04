# -*- coding: utf-8 -*-
"""Genere les icones PNG de la PWA et de l'ecran d'accueil iOS.

Les icones data: SVG du manifeste fonctionnaient dans Chrome, mais iOS
ignore les apple-touch-icon SVG. On produit donc de vrais PNG, dont une
variante maskable avec une zone de securite respectee.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "public" / "icons"
FONT_PATH = Path("C:/Windows/Fonts/georgiab.ttf")
BACKGROUND = "#8b5a2b"
BORDER = "#a9713f"
TEXT = "#f6efe4"


def draw_icon(size: int, text_ratio: float, name: str) -> None:
    image = Image.new("RGB", (size, size), BACKGROUND)
    draw = ImageDraw.Draw(image)

    if size >= 64:
        margin = int(size * 0.08)
        draw.rounded_rectangle(
            [margin, margin, size - margin - 1, size - margin - 1],
            radius=max(2, int(size * 0.04)),
            outline=BORDER,
            width=max(1, size // 128),
        )

    font = ImageFont.truetype(str(FONT_PATH), int(size * text_ratio))
    text = "BH"
    box = draw.textbbox((0, 0), text, font=font)
    width = box[2] - box[0]
    height = box[3] - box[1]
    x = (size - width) / 2 - box[0]
    y = (size - height) / 2 - box[1]
    draw.text((x, y), text, font=font, fill=TEXT)

    image.save(OUT_DIR / name, "PNG", optimize=True)
    print(f"{name} : {size}x{size}")


def main() -> None:
    if not FONT_PATH.exists():
        raise SystemExit(f"Police introuvable : {FONT_PATH}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    draw_icon(32, 0.46, "icon-32.png")
    draw_icon(180, 0.40, "apple-touch-icon.png")
    draw_icon(192, 0.42, "icon-192.png")
    draw_icon(512, 0.42, "icon-512.png")
    # Zone de securite maskable : le monogramme reste dans le cercle central.
    draw_icon(512, 0.32, "icon-512-maskable.png")


if __name__ == "__main__":
    main()
