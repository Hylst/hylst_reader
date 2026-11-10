---
description: Publie un livre dans la Bibliothèque de Hylst sans écraser le catalogue
agent: bibliothecaire
---

Publie `$ARGUMENTS` dans La Bibliothèque de Hylst.

1. Lis `AGENTS.md`, `antigravity.md`, `structure.md` et `test_build_deploy.md`.
2. Vérifie la source : `livres_pour_import/$ARGUMENTS/` ou l'export validé fourni. Contrôle le titre, l'auteur, l'année, la couverture, l'introduction et les chapitres.
3. Vérifie que l'identifiant `$ARGUMENTS` n'existe pas déjà dans `public/books.json`.
4. Copie les fichiers dans `public/books/$ARGUMENTS/` et la couverture dans `public/covers/`. Ne touche à aucun autre livre.
5. Ajoute une seule entrée dans `public/books.json`, en conservant les 12 entrées existantes et leur ordre. Demande l'accord avant d'écrire ce fichier.
6. Lance `node scripts/build_jsx.js`, puis `--check`, puis `python scripts/check_dashes.py --root .`.
7. Synchronise avec `.\scripts\sync-to-platform.ps1`, sers `D:\0CODE\AntiGravity\Cours_Memos\Docker` sur `http://127.0.0.1:8765/books_reader/` et teste l'entrée ajoutée.
8. Rends un rapport : fichiers créés, entrée de catalogue, nombre d'entrées avant et après, résultats des tests, problèmes, décision humaine restante.

Ne lance jamais `build_books.py`. Ne pousse pas sur GitHub. Si une étape échoue, arrête-toi et explique.
