# -*- coding: utf-8 -*-
"""Telecharge les polices de livres et genere css/book-fonts.css.

Polices utilisees par les designs de livres en theme sepia :
Outfit (titres) et Merriweather (corps). Les fichiers sont auto-heberges
dans public/fonts/ pour supprimer tout appel a Google Fonts au runtime.
"""
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "public" / "fonts"
OUT_CSS = ROOT / "css" / "book-fonts.css"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
URL = ("https://fonts.googleapis.com/css2?"
       "family=Outfit:wght@300;400;500;600;700&"
       "family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap")

BLOCK_RE = re.compile(r"/\*\s*([a-z-]+)\s*\*/\s*@font-face\s*\{(.*?)\}", re.S)
FAMILY_RE = re.compile(r"font-family:\s*'([^']+)'")
STYLE_RE = re.compile(r"font-style:\s*(\w+)")
WEIGHT_RE = re.compile(r"font-weight:\s*(\d+)")
SRC_RE = re.compile(r"src:\s*url\((https://[^)]+)\)")
RANGE_RE = re.compile(r"unicode-range:\s*([^;]+);")


def main() -> None:
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    css = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")

    latin = {}
    for subset, body in BLOCK_RE.findall(css):
        if subset != "latin":
            continue
        family = FAMILY_RE.search(body).group(1)
        style = STYLE_RE.search(body).group(1)
        weight = WEIGHT_RE.search(body).group(1)
        src = SRC_RE.search(body).group(1)
        rng = RANGE_RE.search(body)
        latin[(family, style, weight)] = (src, rng.group(1).strip() if rng else "")

    if not latin:
        raise SystemExit("Aucune police latine trouvee dans la reponse Google Fonts.")

    FONT_DIR.mkdir(parents=True, exist_ok=True)
    rules = [
        "/* Polices auto-hebergees des livres (theme sepia).",
        "   Genere par scripts/fetch_book_fonts.py, ne pas editer a la main. */",
        "",
    ]
    for (family, style, weight), (src, rng) in sorted(latin.items()):
        slug = f"{family.lower().replace(' ', '-')}-{weight}-{style}.woff2"
        dest = FONT_DIR / slug
        if not dest.exists():
            data = urllib.request.urlopen(
                urllib.request.Request(src, headers={"User-Agent": UA}), timeout=60
            ).read()
            dest.write_bytes(data)
        rules.append("@font-face {")
        rules.append(f"    font-family: '{family}';")
        rules.append(f"    font-style: {style};")
        rules.append(f"    font-weight: {weight};")
        rules.append("    font-display: swap;")
        rules.append(f"    src: url('../public/fonts/{slug}') format('woff2');")
        if rng:
            rules.append(f"    unicode-range: {rng};")
        rules.append("}")
        rules.append("")

    OUT_CSS.write_text("\n".join(rules), encoding="utf-8", newline="\n")
    total = sum((FONT_DIR / f).stat().st_size for f in [d.name for d in FONT_DIR.glob("*.woff2")])
    print(f"{len(latin)} fontes latines, {len(list(FONT_DIR.glob('*.woff2')))} fichiers, {total / 1024:.0f} Ko")
    print(f"CSS : {OUT_CSS}")


if __name__ == "__main__":
    main()
