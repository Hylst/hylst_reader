# Structure du Projet · La Bibliothèque de Hylst

Ce document décrit l'organisation physique et logique des répertoires et des fichiers du projet **La Bibliothèque de Hylst**.

## 📁 Arborescence des Répertoires

```
Hylst_Reader/
├── css/                     # Feuilles de style modulaires (Vanilla CSS)
│   ├── base.css             # Raccourcis, fontes de base, réinitialisations
│   ├── book-page.css        # Styles des fiches statiques (généré)
│   ├── components.css       # Styles pour cartes livres, modals, boutons
│   ├── droits.css           # Styles de la page Droits & IA
│   ├── layout.css           # Grilles globales et agencements généraux
│   ├── modals.css           # Structures de fenêtres popups
│   ├── music.css            # Styles dédiés au lecteur de musique et playlists
│   ├── reader.css           # Mise en page littéraire et typographique du Reader
│   ├── responsive.css       # Adaptabilité mobile, tablettes et grands écrans
│   └── variables.css        # Variables CSS, tokens du design system
│
├── js/                      # Logique applicative React
│   ├── components/          # Composants React modularisés et autonomes
│   │   ├── AboutModal.jsx   # Modal À propos (Wattpad, SoundCloud, etc.)
│   │   ├── Ambience.jsx     # Effets animés de fond et nuages de particules
│   │   ├── BookHomeView.jsx # Sommaire et préface du livre sélectionné
│   │   ├── GlobalSettingsModal.jsx # Paramètres de lecture généraux
│   │   ├── Icon.jsx         # Bibliothèque d'icônes SVG optimisées
│   │   ├── ImageLightbox.jsx # Visionneuse plein écran des images
│   │   ├── LibraryView.jsx  # Vue d'accueil et bibliothèque
│   │   ├── MusicPlayerModal.jsx # Lecteur audio complet et tracklist
│   │   └── ReaderView.jsx   # Liseuse interactive premium
│   ├── dist/                # Sortie JSX compilée (générée, servie au runtime)
│   ├── app.jsx              # Orchestrateur général des états de l'application
│   ├── db.js                # Couche IndexedDB pour la persistance locale (idb-keyval)
│   ├── importAPI.js         # API d'importation de fichiers et dossiers HML
│   ├── modalA11y.js         # Piège de focus et fermeture des modales
│   ├── music_data.js        # Catalogue de 282 morceaux de Hylst (tags, cover, src)
│   ├── sanitize.js          # Assainissement des contenus importés (DOMPurify)
│   ├── sw-register.js       # Enregistrement du Service Worker
│   └── theme-boot.js        # Application du thème avant le premier rendu
│
├── livres/                  # 10 fiches statiques indexables (générées)
├── public/                  # Contenus littéraires statiques et images
│   ├── books/               # Ouvrages intégrés d'origine
│   │   ├── l-odyss-e-de-l-ia-2-futurs-un-choix/
│   │   ├── l-odyss-e-de-l-nergie/        # 10 chapitres disponibles
│   │   ├── les-ficelles-du-bonheur/
│   │   ├── quinte-ou-les-harmoniques-de-l-ame/
│   │   ├── nightprowler-carnets-de-samarande/
│   │   ├── recueils-proses-poesies-t1/t2/t3/
│   │   ├── recueils-proses-poesies-t4-carnets-reflexions-partages/
│   │   └── sciences-et-technologie-jeux-videos/
│   ├── covers/              # Couvertures de livres et d'histoires
│   ├── fonts/               # Polices auto-hébergées
│   ├── icons/               # Icônes PWA PNG et apple-touch-icon
│   ├── books.json           # Index général et descriptifs des livres
│   └── social-share.png     # Image de partage Open Graph
│
├── vendor/                  # React, ReactDOM, idb-keyval, JSZip, epub.js, DOMPurify
│   └── LICENSES.md          # Versions, licences et empreintes SHA-256
├── scripts/
│   ├── build_jsx.js         # Précompilation des JSX vers js/dist
│   ├── build_book_pages.py  # Génération des 10 fiches statiques indexables
│   ├── check_dashes.py      # Contrôle zéro tiret cadratin ou demi-cadratin
│   ├── fetch_book_fonts.py  # Récupération des polices de lecture
│   ├── generate_pwa_icons.py # Génération des icônes PWA
│   ├── make_social_share.py # Composition de l'image Open Graph
│   ├── sync-to-platform.ps1 # Synchronisation sûre vers Cours_Memos/Docker/books_reader
│   ├── verify-release.ps1   # Contrôle build, tirets, sitemap, 301, CSP meta et en-tête, fichiers sensibles
│   └── vendor/babel.min.js  # Babel, outil de build uniquement (non servi)
├── livres_pour_import/      # [Ignoré par Git] Sources des livres en local
│
├── .gitignore               # Fichiers et dossiers exclus du versioning Git
├── AGENTS.md                # Consignes agents, pointe vers antigravity.md
├── antigravity.md           # Mémoire projet et consignes agents
├── CHANGELOG.md             # Journal des versions et des modifications
├── README.md                # Guide d'accueil utilisateur et présentation
├── sw.js                    # Service Worker assurant le mode offline complet
├── manifest.json            # Configuration PWA pour installation
├── index.html               # Point d'entrée de l'application statique
├── droits.html              # Droits d'auteur, citation et intelligence artificielle
├── build_books.py           # Compilation des livres bruts vers public/
├── gen_music_data.py        # Génération de js/music_data.js depuis le CSV
└── todo.md                  # Carnet de bord des tâches à accomplir
```

---

## 🛠️ Rôle des Outils & Scripts Spécifiques

- **`build_books.py`** : scanne `livres_pour_import/`, convertit les textes bruts en HTML sémantique, copie les couvertures et actualise `public/books.json`.
- **`scripts/build_jsx.js`** : compile les 10 fichiers JSX vers `js/dist/*.js` avec Babel en mode build. `--check` échoue si la sortie est périmée. Chaque fichier est encapsulé dans une IIFE.
- **`scripts/build_book_pages.py`** : génère les 10 fiches statiques `livres/<id>/` avec métadonnées, JSON-LD, CSP et icônes.
- **`scripts/check_dashes.py`** : refuse tout tiret cadratin ou demi-cadratin dans les fichiers servis.
- **`scripts/sync-to-platform.ps1`** : compile le JSX, génère les fiches, calcule l'empreinte de build, préserve l'index de production et synchronise `Cours_Memos/Docker/books_reader`. Il exclut les sources `.jsx` et `scripts/vendor/babel.min.js` du miroir.
- **`scripts/verify-release.ps1`** : contrôle localement `js/dist` et la règle zéro tiret, puis en production le build, le SW, les 12 URL du sitemap, le 301 des fiches, la CSP meta, l'en-tête CSP Books Reader, l'absence d'en-tête global et les fichiers sensibles.
- **`sw.js`** : précache l'app shell, `public/books.json`, les 91 contenus, les 10 couvertures et les 10 fiches, puis sert le local en Network-First avec repli cache.
- **`index.html`** : charge les styles, le thème avant premier rendu et les fichiers `js/dist/*.js`. Babel n'est plus chargé par le navigateur.
- **`vendor/`** : bibliothèques JS servies localement, sans CDN au runtime. Babel est dans `scripts/vendor/` et reste un outil de build.
- **`js/dist/` et `livres/`** : sorties générées. `js/dist/` est ignoré par Git dans le dépôt source et régénéré avant tout service ou sync. Le miroir de production versionne `js/dist/` pour que Coolify déploie les fichiers compilés.
- **`AGENTS.md`** : consignes courtes lues par les agents, avec renvoi vers `antigravity.md` pour la mémoire complète.
- **`antigravity.md`** : mémoire projet et consignes agents (stack, règles, état courant, prochaines étapes).
- **`gen_music_data.py`** : génère `js/music_data.js` depuis `mp3_online.csv` et `mp3_online.txt`, avec les chemins relatifs `/hml/`.
