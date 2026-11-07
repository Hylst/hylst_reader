# Conception Technique · La Bibliothèque de Hylst

Ce guide technique explique les choix d'architecture et de conception pour les développeurs souhaitant comprendre ou modifier l'application **La Bibliothèque de Hylst**.

---

## 🏗️ 1. Architecture globale : statique, avec précompilation JSX

L'application se sert comme un site statique : aucun serveur applicatif, aucun framework côté serveur. Les sources JSX sont compilées **avant le déploiement** par `scripts/build_jsx.js`, puis le navigateur ne charge que du JavaScript classique depuis `js/dist/`.

### 🌟 Avantages de cette stack :
1. **Runtime léger** : plus de Babel ni de transpilation dans le navigateur, donc environ 2,3 Mo et 53 % du premier chargement en moins.
2. **Déploiement simple** : le miroir ne contient que des fichiers statiques. La compilation est une étape de build, pas une dépendance de production.
3. **Contrôle** : `node scripts/build_jsx.js --check` échoue si `js/dist/` n'est pas à jour, et `sync-to-platform.ps1` l'exécute avant de calculer l'empreinte.

---

## 📦 2. Précompilation JSX et dépendances locales

Les dépendances critiques sont servies localement depuis `vendor/` : React 18.3.1, ReactDOM 18.3.1, idb-keyval 6.3.0, JSZip 3.10.2, epub.js 0.3.93 et DOMPurify 3.4.17. Aucun CDN n'est appelé au runtime.

Les sources JSX de `js/` et `js/components/` sont compilées avec le runtime React classique (`React.createElement`) vers `js/dist/` :

```powershell
node scripts/build_jsx.js           # régénère js/dist/
node scripts/build_jsx.js --check   # vérifie que js/dist/ est à jour
```

Babel reste un outil de build dans `scripts/vendor/babel.min.js`. Il n'est ni copié dans le miroir, ni chargé par `index.html`. Chaque fichier compilé est encapsulé dans une IIFE pour éviter les collisions de portée globale, et expose son API via `window.*`. L'ordre de chargement des scripts reste donc important : composants d'abord, `js/dist/app.js` en dernier.

---

## 📂 3. Modularisation React par Composants Réels

L'application est structurée de manière modulaire au sein de `js/components/`. Chaque fichier est un script classique, encapsulé dans une IIFE par `scripts/build_jsx.js`. Il n'utilise pas `import`/`export` ES6 : il expose ses fonctions via `window.*`, et l'ordre de chargement reste explicite dans `index.html`.
- **`js/components/Icon.jsx`** : Fournit le set complet des icônes SVG.
- **`js/components/Ambience.jsx`** : Gère l'arrière-plan interactif et les particules.
- **`js/components/LibraryView.jsx`, `BookHomeView.jsx`, `ReaderView.jsx`** : Bibliothèque, fiche de livre et liseuse.
- **`js/app.jsx`** : Sert de chef d'orchestre global, gérant la machine à états de l'application (vue active, livre en cours, progression) et la lecture audio persistante.

---

## 💾 4. Base de Données Locale IndexedDB (`db.js`)

Pour persister les données de progression sans serveur backend, nous utilisons `idb-keyval`, une abstraction ultra-légère au-dessus de l'API complexe IndexedDB du navigateur :
- **`getBooks()` / `saveBook(book)`** : Sauvegarde des livres importés au format HML, TXT, EPUB ou JSON.
- **`getProgress(bookId)` / `saveProgress(bookId, chapterIdx, ratio)`** : Sauvegarde permanente du dernier chapitre lu et du pourcentage de défilement pour un effet "continuer la lecture" transparent.
- **`getSignets(bookId)` / `saveSignet(bookId, bookmark)`** : Enregistrement de signets posés par le lecteur.

---

## 🌐 5. Cache PWA offline complet (`sw.js`)

À l'installation, le Service Worker précache :
1. **L'app shell** : `index.html`, CSS, JS compilés, vendors, manifeste, icônes et `droits.html`.
2. **Les contenus** : `public/books.json`, les 84 fichiers de contenu (10 introductions et 74 chapitres), les 10 couvertures actives et les 10 fiches statiques `livres/<id>/`.

La stratégie réseau reste Network-First pour les fichiers locaux, avec repli sur le cache hors ligne. Une navigation sans correspondance retombe sur l'app shell déjà précaché. L'activation ne supprime que les caches préfixés `hylst-reader-` : les caches des autres applications de l'origine `hylst.fr` sont préservés.

---

## 🔒 6. Dépendances auto-hébergées (`vendor/`)

Les bibliothèques servies au runtime sont React 18.3.1, ReactDOM 18.3.1, idb-keyval 6.3.0, JSZip 3.10.2, epub.js 0.3.93 et DOMPurify 3.4.17. Les versions, licences et empreintes SHA-256 sont documentées dans `vendor/LICENSES.md`. Babel 8.0.9 figure à part, dans `scripts/vendor/`, comme outil de build non servi.

Le chargement via CDN a été supprimé de `index.html` pour éviter les dépendances runtime externes et les risques de supply chain.

---

## 🛡️ 7. Sécurité des contenus importés (`sanitize.js`)

Les livres intégrés au dépôt sont considérés comme sûrs. En revanche, les contenus choisis par l'utilisateur (EPUB, dossiers HML, JSON) sont traités comme non fiables :

- `HylstSanitize.sanitizeHtml()` applique DOMPurify avec le profil HTML, interdit les balises actives (`script`, `iframe`, `object`, `embed`, `form`, etc.) et les attributs dangereux (`srcdoc`, `formaction`, `xlink:href`).
- `HylstSanitize.sanitizeBook()` filtre `introHtml` et tous les `chapters[].html` d'un livre importé.
- Les fichiers TXT/MD sont échappés avant d'être transformés en paragraphes.
- `BookHomeView` et `ReaderView` re-filtrent les livres importés au rendu, ce qui protège aussi les livres déjà stockés dans IndexedDB avant cette version.

---

## 🚀 8. Déploiement

Le déploiement réel ne se fait pas depuis ce dépôt seul. Le miroir de production est :

```text
D:\0CODE\AntiGravity\Cours_Memos\Docker\books_reader
```

Il appartient au dépôt `Hylst/cours_info`, déployé par Coolify (`hylst-cours`) sur `https://hylst.fr/books_reader/`.

Utiliser `scripts/sync-to-platform.ps1` : il compile le JSX, génère les fiches statiques, copie uniquement les fichiers runtime, préserve l'`index.html` de production (vendor, polices de la plateforme, canonical), calcule une empreinte de build, met à jour `sw.js` et les `?v=`, puis vérifie les empreintes. Les sources `.jsx` et Babel ne sont pas copiés. `-Commit` crée un commit local ; le script ne pousse jamais.

Le 301 `/books_reader/livres/<id>` vers `/books_reader/livres/<id>/` est décrit dans `Cours_Memos/Docker/nginx-coolify-reference.conf` et appliqué dans Coolify.
