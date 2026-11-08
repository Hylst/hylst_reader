# -*- coding: utf-8 -*-
"""Verifie la coherence des couvertures de livres a venir.

La liste FUTURE_BOOKS de LibraryView.jsx et les entrees de APP_SHELL dans
sw.js doivent decrire exactement le meme ensemble de fichiers presents dans
public/covers/. Toute divergence casse le precache hors ligne ou gaspille
de la bande passante.
"""
import argparse
import re
import sys
from pathlib import Path


def fail(messages):
    for message in messages:
        print("KO " + message, file=sys.stderr)
    return 1


def main():
    parser = argparse.ArgumentParser(description="Controle des couvertures a venir.")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent),
                        help="Racine du depot (defaut : dossier parent de scripts/)")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    library_path = root / "js" / "components" / "LibraryView.jsx"
    sw_path = root / "sw.js"
    covers_dir = root / "public" / "covers"

    missing_paths = [str(path) for path in (library_path, sw_path) if not path.is_file()]
    if missing_paths:
        return fail(["fichier introuvable : " + path for path in missing_paths])

    library = library_path.read_text(encoding="utf-8")
    block = re.search(r"const FUTURE_BOOKS\s*=\s*\[(.*?)\n\];", library, re.S)
    if not block:
        return fail(["bloc FUTURE_BOOKS introuvable dans " + str(library_path)])
    future = re.findall(r"cover:\s*'covers/([^']+)'", block.group(1))
    if not future:
        return fail(["aucune couverture dans FUTURE_BOOKS"])
    if len(future) != len(set(future)):
        return fail(["couverture dupliquee dans FUTURE_BOOKS"])

    sw = sw_path.read_text(encoding="utf-8")
    shell = re.search(r"const APP_SHELL\s*=\s*\[(.*?)\n\];", sw, re.S)
    if not shell:
        return fail(["bloc APP_SHELL introuvable dans " + str(sw_path)])
    sw_covers = re.findall(r"'\./public/covers/([^']+)'", shell.group(1))
    if len(sw_covers) != len(set(sw_covers)):
        return fail(["couverture dupliquee dans APP_SHELL"])

    problems = []
    future_set = set(future)
    sw_set = set(sw_covers)
    for name in future:
        if not (covers_dir / name).is_file():
            problems.append("fichier absent : public/covers/" + name)
        if name not in sw_set:
            problems.append("absente de APP_SHELL : " + name)
    for name in sw_covers:
        if name not in future_set:
            problems.append("dans APP_SHELL mais absente de FUTURE_BOOKS : " + name)
        if not (covers_dir / name).is_file():
            problems.append("fichier absent : public/covers/" + name)

    if problems:
        return fail(problems)

    print(f"OK {len(future)} couvertures a venir coherentes entre "
          f"FUTURE_BOOKS, APP_SHELL et public/covers/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
