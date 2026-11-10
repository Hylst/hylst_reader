---
description: Compile, synchronise et vérifie le miroir de production
agent: bibliothecaire
---

Vérifie le miroir de production de La Bibliothèque de Hylst.

1. Lis `AGENTS.md`, `antigravity.md` et `test_build_deploy.md`.
2. Compile : `node scripts/build_jsx.js`, puis `node scripts/build_jsx.js --check`.
3. Vérifie les tirets : `python scripts/check_dashes.py --root .`.
4. Synchronise : `powershell -ExecutionPolicy Bypass -File .\scripts\sync-to-platform.ps1`.
5. Sers `D:\0CODE\AntiGravity\Cours_Memos\Docker` sur `http://127.0.0.1:8765/books_reader/`.
6. Contrôle : le catalogue contient 12 entrées, chaque entrée a une couverture, une introduction et ses chapitres, aucune URL externe n'est chargée, aucun script inline n'est présent.
7. Rends un rapport avec les commandes, les résultats et les écarts. Ne pousse pas sur GitHub.
