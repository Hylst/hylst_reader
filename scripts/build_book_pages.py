# -*- coding: utf-8 -*-
"""Genere une fiche statique et indexable pour chaque livre.

Sortie : livres/<id>/index.html
Ces pages servent de point d'entree SEO et de secours sans JavaScript.
Elles renvoient vers la liseuse pour la lecture complete.
"""
import html
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "livres"
BASE = "https://hylst.fr/books_reader/"
SITE = "La Bibliothèque de Hylst"


def strip_html(value: str) -> str:
    value = re.sub(r"<script.*?</script>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<style.*?</style>", " ", value, flags=re.S | re.I)
    value = re.sub(r"</(?:p|h[1-6]|div|li|blockquote)>", ". ", value, flags=re.I)
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"[🀀-🫿☀-➿️]", "", value)
    value = re.sub(r"(\s*\.\s*){2,}", ". ", value)
    return re.sub(r"\s+", " ", value).strip()


def shorten(value: str, limit: int = 155) -> str:
    if len(value) <= limit:
        return value
    cut = value[:limit]
    sentences = re.split(r"(?<=[.!?])\s+", cut)
    if len(sentences) > 1 and len(sentences[0]) >= 90:
        return sentences[0].strip()
    cut = cut.rsplit(" ", 1)[0].rstrip(" ,;:.")
    return cut + "…"


def xml_escape(value: str) -> str:
    return html.escape(value, quote=True)


STYLE = """
:root {
    --bg: #0f0e0c;
    --surface: #1c1917;
    --text: #e8e2d9;
    --muted: #a09080;
    --accent: #d4955a;
    --border: rgba(255, 255, 255, 0.1);
}
* { box-sizing: border-box; }
body {
    margin: 0;
    background:
        radial-gradient(1000px 600px at 12% -10%, rgba(212, 149, 90, 0.13), transparent 65%),
        var(--bg);
    color: var(--text);
    font-family: Georgia, 'Iowan Old Style', 'Times New Roman', serif;
    line-height: 1.75;
    font-size: 17px;
}
a { color: var(--accent); }
.wrap { max-width: 980px; margin: 0 auto; padding: 2.5rem 1.5rem 5rem; }
.topbar {
    display: flex; justify-content: space-between; align-items: center; gap: 1rem;
    padding-bottom: 1.25rem; margin-bottom: 2.5rem;
    border-bottom: 1px solid var(--border);
    font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
    font-size: 0.82rem; letter-spacing: 0.03em;
}
.topbar a { text-decoration: none; }
.topbar .brand { color: var(--text); font-weight: 600; }
.hero { display: grid; grid-template-columns: 260px 1fr; gap: 2.5rem; align-items: start; }
.cover {
    width: 100%; aspect-ratio: 5 / 8; border-radius: 10px; overflow: hidden;
    border: 1px solid var(--border); box-shadow: 0 24px 50px -18px rgba(0, 0, 0, 0.8);
    background: var(--surface);
}
.cover img { width: 100%; height: 100%; object-fit: cover; display: block; }
.kicker {
    font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
    font-size: 0.7rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--muted); margin: 0 0 0.6rem;
}
h1 { font-size: clamp(2rem, 4.5vw, 3rem); line-height: 1.15; margin: 0 0 0.4rem; font-weight: 600; }
.subtitle { color: var(--muted); font-style: italic; font-size: 1.1rem; margin: 0 0 0.9rem; }
.author { color: var(--text); margin: 0 0 0.35rem; }
.year { color: var(--muted); font-size: 0.9rem; margin: 0 0 1.1rem; }
.rights { color: var(--muted); font-size: 0.78rem; margin: 0 0 1.4rem; }
.rights a { text-decoration: none; border-bottom: 1px dotted rgba(212, 149, 90, 0.5); }
.badge {
    display: inline-block; margin-bottom: 0.8rem; padding: 0.15rem 0.6rem;
    border: 1px solid rgba(212, 149, 90, 0.45); border-radius: 999px;
    color: var(--accent); font-size: 0.68rem; letter-spacing: 0.08em;
    text-transform: uppercase; font-family: system-ui, sans-serif;
}
.cta {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: linear-gradient(135deg, #d4955a, #b87c45);
    color: #1a1208; text-decoration: none; font-weight: 700;
    padding: 0.85rem 1.6rem; border-radius: 8px;
    font-family: system-ui, -apple-system, 'Segoe UI', sans-serif; font-size: 0.92rem;
    box-shadow: 0 14px 28px -12px rgba(212, 149, 90, 0.6);
}
.cta:hover { filter: brightness(1.06); }
.section { margin-top: 3rem; }
.section h2 {
    font-size: 0.82rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--accent); font-family: system-ui, sans-serif; font-weight: 600;
    margin: 0 0 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border);
}
.intro { font-size: 1.02rem; color: var(--text); }
.intro :is(h1, h2, h3) { font-size: 1.25rem; color: var(--text); margin: 1.6rem 0 0.7rem; }
.intro p { margin: 0 0 1rem; }
.intro hr.ornament { width: 70px; margin: 1.2rem auto; border: 0; border-top: 1px solid var(--accent); opacity: 0.6; }
.intro .chapter-byline, .intro .chapter-continuation { color: var(--muted); font-style: italic; font-size: 0.88rem; }
.intro a { color: var(--accent); }
ol.chapters { margin: 0; padding-left: 1.3rem; color: var(--muted); }
ol.chapters li { margin-bottom: 0.35rem; }
footer {
    margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border);
    color: var(--muted); font-size: 0.8rem; font-family: system-ui, sans-serif;
}
footer a { color: var(--accent); text-decoration: none; }
@media (max-width: 720px) {
    .wrap { padding: 1.75rem 1.1rem 3.5rem; }
    .hero { grid-template-columns: 1fr; gap: 1.5rem; }
    .cover { max-width: 220px; }
}
"""


def chapter_items(chapters):
    items = []
    for i, chapter in enumerate(chapters, 1):
        title = html.escape(chapter.get("title", f"Chapitre {i}"))
        items.append(f"                <li>{title}</li>")
    return "\n".join(items)


def build_book(book: dict) -> str:
    book_id = book["id"]
    title = book["title"]
    subtitle = (book.get("subtitle") or "").strip()
    author = book.get("author") or "Geoffroy Streit (Hylst)"
    year = str(book.get("year") or "").strip()
    year_start = year.split("-")[0] if year else ""
    cover = f"{BASE}public/{book['coverPath']}"
    url = f"{BASE}livres/{book_id}/"
    intro_path = ROOT / "public" / "books" / book_id / "intro.html"
    intro_html = intro_path.read_text(encoding="utf-8") if intro_path.exists() else ""
    # Le premier h2 qui repete le titre de la page est retire de l'encart.
    first_h2 = re.search(r"<h2[^>]*>(.*?)</h2>", intro_html, flags=re.S | re.I)
    if first_h2 and strip_html(first_h2.group(1)).lower() == title.lower():
        intro_html = intro_html[:first_h2.start()] + intro_html[first_h2.end():]
    # Le sous-titre est deja affiche dans l'entete : on retire la ligne redondante.
    intro_html = re.sub(r'<p[^>]*class="[^"]*chapter-byline[^"]*"[^>]*>.*?</p>', '', intro_html, count=1, flags=re.S | re.I)
    intro_desc_html = re.sub(r"<h[1-3][^>]*>.*?</h[1-3]>", " ", intro_html, flags=re.S | re.I)
    intro_desc_html = re.sub(
        r'<(?:p|div)[^>]*class="[^"]*(?:chapter-byline|chapter-epigraph|chapter-continuation|chapter-tags|provenance-note)[^"]*"[^>]*>.*?</(?:p|div)>',
        " ", intro_desc_html, flags=re.S | re.I)
    intro_text = strip_html(intro_desc_html)
    for prefix in (title, subtitle):
        if prefix and intro_text.lower().startswith(prefix.lower()):
            intro_text = intro_text[len(prefix):].lstrip(" :·,.-")
    fallback = f"{title}{', ' + subtitle if subtitle else ''}, un texte de Geoffroy Streit (Hylst) à lire dans La Bibliothèque de Hylst."
    if not intro_text or len(intro_text) < 40 or intro_text.lower().startswith(("cet ouvrage", "préface")):
        description = fallback
    else:
        description = shorten(intro_text)

    og_dir = ROOT / "public" / "covers" / "og"
    og_dir.mkdir(parents=True, exist_ok=True)
    cover_src = ROOT / "public" / book["coverPath"]
    og_path = og_dir / f"{book_id}.jpg"
    if cover_src.exists():
        Image.open(cover_src).convert("RGB").save(og_path, "JPEG", quality=88, optimize=True, progressive=True)
    if og_path.exists():
        og_w, og_h = Image.open(og_path).size
        og_image = f"{BASE}public/covers/og/{book_id}.jpg"
        og_type = "image/jpeg"
    else:
        og_w, og_h = 1200, 630
        og_image = f"{BASE}public/social-share.png"
        og_type = "image/png"

    badge = ""
    if book.get("badge"):
        badge = f'                <span class="badge">{html.escape(book["badge"])}</span>\n'

    subtitle_html = ""
    if subtitle:
        subtitle_html = f'                <p class="subtitle">{html.escape(subtitle)}</p>\n'

    chapters = book.get("chapters") or []
    chapter_blocks = []
    for i, chapter in enumerate(chapters, 1):
        chapter_blocks.append({
            "@type": "Chapter",
            "name": chapter.get("title", f"Chapitre {i}"),
            "position": i,
        })

    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Book",
                "@id": f"{url}#book",
                "name": title,
                "url": url,
                "author": {"@type": "Person", "name": "Geoffroy Streit", "alternateName": "Hylst"},
                "publisher": {"@type": "Person", "name": "Geoffroy Streit"},
                "inLanguage": "fr",
                "bookFormat": "https://schema.org/EBook",
                "isAccessibleForFree": True,
                "image": og_image,
                "datePublished": year_start,
                "description": description,
                "copyrightHolder": {"@type": "Person", "name": "Geoffroy Streit"},
                "license": f"{BASE}droits.html",
                "hasPart": chapter_blocks,
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "La Bibliothèque de Hylst", "item": BASE},
                    {"@type": "ListItem", "position": 2, "name": title, "item": url},
                ],
            },
        ],
    }

    page_title = f"{title} · {SITE}"

    return f"""<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <meta name="description" content="{html.escape(description)}">
    <meta name="author" content="Geoffroy Streit (Hylst)">
    <meta name="robots" content="index, follow, max-image-preview:large, noai, noimageai">
    <meta name="copyright" content="© 2026 Geoffroy Streit">
    <meta name="rights" content="Tous droits réservés. Reproduction et entraînement de modèles d'intelligence artificielle interdits sans autorisation écrite.">
    <meta name="tdm-reservation" content="1">
    <meta name="tdm-policy" content="{BASE}droits.html">
    <link rel="canonical" href="{url}">
    <link rel="license" href="{BASE}droits.html">
    <meta name="theme-color" content="#0f0e0c">

    <meta property="og:site_name" content="{SITE}">
    <meta property="og:locale" content="fr_FR">
    <meta property="og:type" content="book">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:image:type" content="{og_type}">
    <meta property="og:image:width" content="{og_w}">
    <meta property="og:image:height" content="{og_h}">
    <meta property="og:image:alt" content="Couverture de {html.escape(title)}">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{page_title}">
    <meta name="twitter:description" content="{html.escape(description)}">
    <meta name="twitter:image" content="{og_image}">

    <script type="application/ld+json">
{json.dumps(jsonld, ensure_ascii=False, indent=2)}
    </script>

    <style>{STYLE}</style>
</head>
<body>
    <div class="wrap">
        <nav class="topbar">
            <a class="brand" href="../../">La Bibliothèque de Hylst</a>
            <a href="../../droits.html">Droits &amp; IA</a>
        </nav>

        <main>
            <div class="hero">
                <div class="cover">
                    <img src="../../public/{html.escape(book['coverPath'])}" alt="Couverture de {html.escape(title)}" width="512" height="800">
                </div>
                <div>
{badge}                    <p class="kicker">La Bibliothèque de Hylst</p>
                    <h1>{html.escape(title)}</h1>
{subtitle_html}                    <p class="author">{html.escape(author)}</p>
                    <p class="year">{html.escape(year)}</p>
                    <p class="rights">Texte de <strong>Geoffroy Streit</strong> · © Tous droits réservés · <a href="../../droits.html">Citation &amp; IA</a></p>
                    <a class="cta" href="../../?book={book_id}">Lire dans la liseuse</a>
                </div>
            </div>

            <section class="section intro">
                <h2>Présentation</h2>
                {intro_html or f"<p>{html.escape(description)}</p>"}
            </section>

            <section class="section">
                <h2>Sommaire</h2>
                <ol class="chapters">
{chapter_items(chapters)}
                </ol>
            </section>
        </main>

        <footer>
            {SITE} · Livres, proses, poésies et récits de Geoffroy Streit.
            <br>
            <a href="../../">Retour à la bibliothèque</a> ·
            <a href="../../droits.html">Droits d'auteur &amp; intelligence artificielle</a>
        </footer>
    </div>
</body>
</html>
"""


def main() -> None:
    books = json.loads((ROOT / "public" / "books.json").read_text(encoding="utf-8"))
    OUT_DIR.mkdir(exist_ok=True)
    for book in books:
        dest = OUT_DIR / book["id"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(build_book(book), encoding="utf-8", newline="\n")
        print(f"{dest.relative_to(ROOT)}")
    print(f"{len(books)} fiches generees.")


if __name__ == "__main__":
    main()
