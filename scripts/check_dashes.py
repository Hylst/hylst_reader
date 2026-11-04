#!/usr/bin/env python3
"""Vérifie l'absence de tirets cadratins et demi-cadratins dans la bibliothèque.

Usage :
    python scripts/check_dashes.py
    python scripts/check_dashes.py --all
    python scripts/check_dashes.py --root D:/chemin/vers/books_reader

Par défaut, seuls les contenus servis et les chaînes d'interface sont contrôlés.
Avec --all, les documents et les commentaires sont aussi contrôlés, mais les
sources brutes (livres_pour_import, sources/), les dépendances (vendor,
node_modules) et les fichiers générés exclus sont ignorés.

Caractères contrôlés : U+2012, U+2013, U+2014, U+2015, U+FE58.
Le signe moins mathématique U+2212 n'est pas concerné.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DASHES = {
    "\u2012": "FIGURE DASH",
    "\u2013": "EN DASH",
    "\u2014": "EM DASH",
    "\u2015": "HORIZONTAL BAR",
    "\ufe58": "SMALL EM DASH",
}

SKIP_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    "vendor",
    "livres_pour_import",
    "sources",
}

TEXT_EXTS = {".html", ".jsx", ".js", ".css", ".json", ".md", ".py", ".txt"}

DEFAULT_FILES = [
    "index.html",
    "manifest.json",
    "sw.js",
    "public/books.json",
]

DEFAULT_GLOBS = [
    "public/books/**/*.html",
    "js/components/*.jsx",
    "js/app.jsx",
]


def iter_default_files(root: Path):
    for rel in DEFAULT_FILES:
        p = root / rel
        if p.is_file():
            yield p
    for pattern in DEFAULT_GLOBS:
        yield from root.glob(pattern)


def iter_all_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXTS:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def scan(root: Path, all_files: bool):
    files = sorted(set(iter_all_files(root) if all_files else iter_default_files(root)))
    findings = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for char, name in DASHES.items():
                if char in line:
                    findings.append((path, lineno, name, line.strip()))
    return findings, len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Racine à contrôler")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Contrôler aussi les documents et commentaires (hors sources brutes)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERREUR] Racine introuvable : {root}", file=sys.stderr)
        return 2

    findings, count = scan(root, args.all)
    if findings:
        print(
            f"[ECHEC] {len(findings)} tiret(s) cadratin(s)/demi-cadratin(s) "
            f"dans {count} fichier(s) contrôlé(s) :"
        )
        for path, lineno, name, line in findings:
            rel = path.relative_to(root)
            print(f"  {rel}:{lineno}: {name}: {line[:160]}")
        return 1

    print(
        f"[OK] Aucun tiret cadratin ou demi-cadratin dans {count} fichier(s) "
        f"contrôlé(s) ({root})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
