# -*- coding: utf-8 -*-
"""Construit le dossier servi pour La Bibliothèque de Hylst sur art.hylst.fr.

Usage :
    python scripts/construire_hylst_biblio.py

Le script copie uniquement les fichiers utiles au runtime (pas les documents,
les scripts de génération ni les sources JSX déjà compilées dans js/dist),
puis vérifie qu'aucune URL de l'ancienne adresse ne subsiste.
"""
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SITE_PATH = "/hylst_biblio/"

DOSSIERS = ["css", "js", "vendor", "livres", "public"]
FICHIERS = ["index.html", "droits.html", "manifest.json", "sw.js", "sitemap.xml"]


def copier(rel: str) -> None:
    source = ROOT / rel
    cible = DIST / rel
    if source.is_dir():
        shutil.copytree(source, cible)
    else:
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, cible)


def main() -> None:
    # js/dist est ignore par Git : il est regenere avant chaque empaquetage.
    subprocess.run(["node", "scripts/build_jsx.js"], cwd=ROOT, check=True)
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for dossier in DOSSIERS:
        copier(dossier)
    for fichier in FICHIERS:
        copier(fichier)

    restes = []
    for p in DIST.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".html", ".js", ".json", ".css", ".xml", ".webmanifest"}:
            continue
        texte = p.read_text(encoding="utf-8", errors="ignore")
        if "books_reader" in texte:
            restes.append(str(p.relative_to(DIST)))
    if restes:
        raise SystemExit("Ancienne adresse encore presente : " + ", ".join(restes[:8]))

    index = (DIST / "index.html").read_text(encoding="utf-8")
    if f'href="https://art.hylst.fr{SITE_PATH}"' not in index:
        raise SystemExit("canonical art absent de index.html")
    if f'href="{SITE_PATH}"' not in (DIST / "droits.html").read_text(encoding="utf-8"):
        raise SystemExit("base /hylst_biblio/ absente de droits.html")

    fichiers = [p for p in DIST.rglob("*") if p.is_file()]
    octets = sum(p.stat().st_size for p in fichiers)
    print(f"{len(fichiers)} fichiers, {octets / 1024 / 1024:.1f} Mo")
    print(f"entree : {DIST / 'index.html'}")


if __name__ == "__main__":
    main()
