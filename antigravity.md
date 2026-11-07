# La Bibliothèque de Hylst - Mémoire projet et consignes agents

## Stack réelle (04/11/2026)

- **Frontend** : HTML, CSS Vanilla, React 18.3.1 et ReactDOM 18.3.1 servis depuis `vendor/`. Les sources JSX de `js/` sont précompilées vers `js/dist/` par `scripts/build_jsx.js` avec le runtime React classique.
- **Babel** : outil de build uniquement, dans `scripts/vendor/babel.min.js`. Il n'est ni chargé par `index.html`, ni copié dans le miroir de production.
- **Hors ligne** : Service Worker maison `sw.js`, précache de l'app shell, de `public/books.json`, de 10 introductions et 82 chapitres (92 fichiers de contenu), des 10 couvertures actives et des 10 fiches statiques. Stockage local via `idb-keyval` et IndexedDB. Pas de Vite, pas de Dexie, pas de localForage.
- **Polices** : `/assets/fonts/fonts.css` sur la plateforme. **Musique** : `/hml/` en chemins relatifs.
- **Test local** : compiler, synchroniser, puis servir `D:\0CODE\AntiGravity\Cours_Memos\Docker` sur `http://127.0.0.1:8765/books_reader/`.

## Règles critiques

1. **Sources des livres** : les fichiers HTML de `public/books/l-odyss-e-de-l-ia-2-futurs-un-choix/` sont la source de vérité. Ne jamais les régénérer automatiquement. Les corrections se font manuellement, fichier par fichier.
2. **Zéro tiret long** : aucun tiret cadratin ou demi-cadratin dans les contenus servis. Contrôle obligatoire avec `python scripts/check_dashes.py --root .`.
3. **Aucun CDN au runtime** : React, JSZip, epub.js, DOMPurify et idb-keyval sont locaux. Les polices et la musique sont servies par la plateforme, en same-origin.
4. **CSP** : `script-src 'self'`. Ne jamais ajouter de script inline dans `index.html`, `droits.html` ou les fiches. Externaliser dans `js/` et déclarer le fichier dans `sw.js`.
5. **Service Worker** : ne supprimer que les caches préfixés `hylst-reader-`. Le stockage `caches` est partagé par toute l'origine `hylst.fr`.
6. **Miroir de production** : `scripts/sync-to-platform.ps1` préserve l'`index.html` de production et régénère `js/dist`. Ne jamais écraser l'index de production avec l'index source.
7. **Build JSX** : `node scripts/build_jsx.js` puis `node scripts/build_jsx.js --check`. Le sync exécute les deux et refuse une sortie périmée.
8. **301** : `/books_reader/livres/<id>` redirige vers `/books_reader/livres/<id>/` avec query conservée. Configuration dans `Cours_Memos/Docker/nginx-coolify-reference.conf`, base Coolify et conteneur `hylst-cours`.
9. **Documentation** : après chaque version, mettre à jour `CHANGELOG.md`, `todo.md`, ce fichier, et côté plateforme `changelog.md`, `securite.md`, `todo.md` et `hylst_IT_platform_content.md`.
10. **Textes de tiers (corpus Nightprowler)** : ne jamais reproduire l'Atlas de Bejofa (Letorve), le texte original des règles de combat de Mathieu Mazzoni ni l'aide à la description (Hirrinkaël). Le chapitre VI publie la version personnelle de l'auteur, inspirée de Mazzoni, pas une reproduction ; le chapitre VII suit la même règle. L'aide à la description est réécrite sous le nom de l'auteur et signalée comme provisoire par une note `chapter-source-note`. Les sources sont dans `D:\0HYLST\0 HYLST ART 2024\ecrits\`, encodage cp1252, balisage très dégradé : extraire un texte UTF-8 propre avant toute rédaction et vérifier chaque liste mot par mot, jamais depuis une sortie de console tronquée.
11. **Sitemap** : il vit uniquement dans le miroir, `D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader\sitemap.xml`. `sync-to-platform.ps1` met à jour les `lastmod` et complète automatiquement les fiches de livres déclarées dans `public/books.json` ; toute nouvelle fiche doit quand même être vérifiée après synchronisation.
12. **Illustrations de chapitre** : les images vivent dans le dossier du livre, référencées en chemin relatif, et s'affichent via `<figure class="chapter-cover">`. La génération se fait sur le GPU local avec `D:/0CODE/ClaudeCode/wainsfw/main.py` (modèle `z-image-turbo-sdcpp`, sorties WebP 1216×832), jamais via OpenRouter, dont les crédits image sont épuisés.

## État actuel

- Version **1.8.19** déployée le 07/11, cache Service Worker source `hylst-reader-v75`, build `18c6aef2b4f1`, SW `hylst-reader-18c6aef2b4f1`, commit plateforme `0e29f9cb`. `verify-release.ps1` entièrement vert.
- Catalogue à **10 livres et 88 chapitres** : les huit livres existants, le Tome IV *Carnets, réflexions & partages* (4 chapitres, textes de 2003 à 2024) et le livre *Sciences et technologie* (préface 2026 et quatre parties, étude de 2001-2002). Le Tome I passe à 16 textes avec quatre escapades de 1995 et *Un brin d'écrit* (1996) ; le Tome II passe à 10 textes avec *Farouches apparitions* (1999) et *La tanière du mage* (2020).
- Livre ***Nightprowler, carnets de Samarande*** complet : 13 chapitres publiés (I à XIII), introduction réécrite dans un ton d'hommage avec le lien Grog et les romans de Pierre Pevel, treize illustrations de chapitre dans le style de la couverture, sommaire complet à treize entrées sur la page du livre, fiche statique présente, `f3` retiré des contenus en préparation. Le chapitre VII réunit six fiches normalisées : Albert Degreffion et les cinq prétirés de la convention des Alchimistes de 2011. Le chapitre VIII est le scénario du squelette enfoui d'Azefhfkrijiiir, écrit vers 1999, restructuré en six actes et complété par la rencontre finale. Le chapitre IX est l'esclavage gouri, écrit en 1999-2000 et retapé en 2001, restructuré en cinq actes, avec un plan du camp en SVG et six issues d'évasion. Le chapitre X est Vapeur et boulons, écrit pour la convention des Alchimistes de 2011, restructuré en cinq actes, avec un plan du moulin en SVG, la machine et la pierre de rosette. Le chapitre XI est la reconquête du trône des Rodallois, écrit en 1999 pour un autre jeu et clairement séparé de Nightprowler. Le chapitre XII rassemble trois pistes inachevées de 1999 : le camp barbare du prince démon, le contrôle d'entrée et Kalaar. Le chapitre XIII rassemble les annexes : feuille de personnage vierge normalisée, lexique de 23 termes et chronologie documentée. Référence de reprise : `continue.md`.
- **Rubrique Sciences et technologie** : format hybride. La liseuse sert une préface de 2026, des résumés et les sommaires d'origine ; les quatre PDF exportés depuis les `.docx` conservent le texte, les images et la mise en page de 2001-2002. Les PDF ne sont pas précachés. Les liens utilisent le chemin absolu `/books_reader/public/books/sciences-et-technologie-jeux-videos/pdf/...` pour fonctionner dans la liseuse et dans les fiches statiques.
- CSP meta stricte : `style-src 'self'` et `style-src-attr 'unsafe-inline'`. Les CSS des droits et des fiches sont externalisés.
- Production 1.8.19 (dernière vérifiée) : `verify-release.ps1` entièrement vert, sitemap à 12 URL, 10 livres, 88 chapitres, 268 fichiers runtime et 10 fiches. Le chapitre XIII et son illustration répondent en 200. Le livre *Nightprowler, carnets de Samarande* est complet avec ses 13 chapitres.
- Hors ligne vérifié sur la bibliothèque, une fiche et une page statique, y compris `/livres/<id>` sans slash.
- 301 des fiches sans slash actif (regex sur `/books_reader/livres/<id>`), query conservée, persistance confirmée après redéploiement.
- En-tête CSP Nginx actif, limité à `/books_reader/` : configuration `28f5c867...`, base64 Coolify `375eebfe...`, sauvegarde `/root/hylst-nginx-backup-20261104-booksreader-csp/`, `nginx -t` OK, persistance après deux redéploiements.
- Lighthouse production : mobile 91/100/100/100, desktop 97/100/100/100.

## Prochaines étapes possibles

- Refactorisation CSS et allègement de `base.css`.
- Export `.json` de la bibliothèque importée.
- Preset de lecture longue avec réduction automatique des animations.
- Normalisation hors ligne de `/livres/<id>` vers `/livres/<id>/` dans le Service Worker.
