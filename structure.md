# Structure du Projet — Hylst Books & Reader

Ce document décrit l'organisation physique et logique des répertoires et des fichiers du projet **Hylst Books & Reader**.

## 📁 Arborescence des Répertoires

```
Hylst_Reader/
├── css/                     # Feuilles de style modulaires (Vanilla CSS)
│   ├── base.css             # Raccourcis, fontes de base, réinitialisations
│   ├── components.css       # Styles pour cartes livres, modals, boutons
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
│   │   ├── LibraryView.jsx  # Vue d'accueil et bibliothèque
│   │   ├── MusicPlayerModal.jsx # Lecteur audio complet et tracklist
│   │   └── ReaderView.jsx   # Liseuse interactive premium
│   │
│   ├── app.jsx              # Orchestrateur général des états de l'application
│   ├── db.js                # Couche IndexedDB pour la persistance locale (idb-keyval)
│   ├── importAPI.js         # API d'importation de fichiers et dossiers HML
│   └── music_data.js        # Catalogue de 280+ morceaux de Hylst (tags, cover, src)
│
├── public/                  # Contenus littéraires statiques et images
│   ├── books/               # Ouvrages intégrés d'origine
│   │   └── l-odyss-e-de-l-ia-2-futurs-un-choix/ # Dossier de l'ouvrage IA
│   │       ├── chapitre-1-cover.webp
│   │       ├── chapitre-1.html
│   │       ├── ...
│   │       ├── chapitre-5-cover.webp # Couverture du chapitre 5 générée
│   │       └── chapitre-5.html       # Chapitre final nettoyé
│   ├── covers/              # Emplacement des couvertures de livres
│   ├── books.json           # Index général et descriptifs des livres
│   └── social-share.png     # Image de partage Open Graph
│
├── livres_pour_import/      # [Ignoré par Git] Sources des livres en local
│   └── 2 futurs un choix/   # Fichiers originaux non-compilés
│
├── .gitignore               # Fichiers et dossiers exclus du versioning Git
├── CHANGELOG.md             # Journal des versions et des modifications
├── README.md                # Guide d'accueil utilisateur et présentation
├── sw.js                    # Service Worker assurant le mode offline complet
├── manifest.json            # Configuration PWA pour installation
├── index.html               # Point d'entrée de l'application statique
├── build_books.py           # Script Python de compilation automatique des livres
└── todo.md                  # Carnet de bord des tâches à accomplir
```

---

## 🛠️ Rôle des Outils & Scripts Spécifiques

- **`build_books.py`** : Script Python qui scanne le dossier `livres_pour_import/`, convertit les fichiers textuels bruts en structures HTML sémantiques compatibles avec notre liseuse, copie les couvertures et génère l'index global dans `public/books.json`.
- **`sw.js`** : Service Worker implémentant une stratégie de cache hybride (Network-First pour les fichiers locaux et Cache-First pour les CDN externes) garantissant l'accès complet hors-ligne.
- **`index.html`** : Point d'entrée unique. Il charge les styles CSS Vanilla et transpile à la volée le code JSX en JavaScript compréhensible par le navigateur grâce à Babel CDN.
