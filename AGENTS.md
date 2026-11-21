# Consignes agents : La Bibliothèque de Hylst

La mémoire projet complète est dans [`antigravity.md`](antigravity.md). La lire avant toute modification.

## Configuration OpenCode

- `opencode.jsonc` définit l'agent `bibliothecaire` et les permissions du projet.
- `.opencode/agents/bibliothecaire.md` : gardien du catalogue, du build et du miroir.
- `.opencode/commands/publier.md` : publication d'un livre depuis un export validé.
- `.opencode/commands/verifier-miroir.md` : compilation, synchronisation et test du miroir.
- `build_books.py` est interdit. `public/books/` n'est jamais régénéré.

## Règles courtes

- Ne jamais régénérer automatiquement les HTML de `public/books/` : les corriger manuellement.
- Zéro tiret cadratin ou demi-cadratin dans les contenus servis. Lancer `python scripts/check_dashes.py --root .`.
- Adresse de contact unique : `geoffroy.streit@ik.me`. L'ancienne adresse Gmail ne doit jamais revenir, ni dans la source ni dans le miroir : après chaque synchronisation, lancer `python scripts/verifier-integrite.py` à la racine du hub, qui échoue sinon.
- `frame-ancestors` est une directive d'en-tête : ne jamais la mettre dans une CSP en balise meta (ignorée, erreur console). L'en-tête Nginx de `/hylst_biblio/` la sert déjà.
- Aucun CDN au runtime. Les dépendances sont dans `vendor/`, les polices sur `/assets/fonts/`, la musique sur `/hml/`.
- CSP : `script-src 'self'`. Ne jamais ajouter de script inline. Externaliser dans `js/` et déclarer le fichier dans le précache de `sw.js`.
- Le Service Worker ne supprime que les caches préfixés `hylst-reader-`.
- Compiler le JSX avec `node scripts/build_jsx.js`, puis vérifier avec `--check`.
- Synchroniser avec `scripts/sync-to-platform.ps1`. Il préserve l'`index.html` de production et exclut les sources `.jsx` et Babel.
- Le miroir de production est `D:\0CODE\hylst.fr.platforms\it.hylst.fr\books_reader`.
- Tester le miroir via `http://127.0.0.1:8765/hylst_biblio/`, pas la racine source.
- Après chaque version : `CHANGELOG.md`, `todo.md`, `antigravity.md`, puis les docs plateforme (`changelog.md`, `securite.md`, `todo.md`, `hylst_IT_platform_content.md`).
