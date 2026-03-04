# Hylst Books & Reader

**Hylst Books & Reader** est une application web de lecture (PWA) conçue avec une architecture *Offline-First* et *Pure Frontend*. Elle offre une expérience de lecture premium, une gestion de bibliothèque locale et une intégration musicale unique pour accompagner vos moments de lecture.

## 🌟 Points Forts
- **Expérience Premium** : Design typographique soigné (Cormorant Garamond, Libre Baskerville).
- **Musique Intégrée** : Accès à la bibliothèque musicale de Geoffroy Streit directement dans l'app.
- **Zéro Backend** : Tout tourne dans votre navigateur. Vos données (livres, progression) restent chez vous dans IndexedDB.
- **Import Flexible** : Importez vos propres dossiers HML pour les lire avec le confort du Reader Hylst.
- **Ambiance Visuelle** : Animations d'ambiance subtiles adaptées à chaque thème (Sépia, Clair, Sombre).
- **Temps de Lecture Intelligent** : Calcul dynamique du temps restant et indicateur contextuel.
- **Interface Adaptative** : Navigation fluide avec indicateurs de progression intégrés.

## 🚀 Architecture & Technos
- **Framework** : React 18 (CDN)
- **Stockage** : `idb-keyval` (IndexedDB) pour la persistance locale totale.
- **PWA** : Service Worker (`sw.js`) pour l'installation native.
- **Design** : CSS3 Vanilla (Thèmes dynamiques, animations optimisées).

## ⌨️ Raccourcis Clavier
- `Espace` / `PageDown` : Faire défiler vers le bas.
- `Flèche Droite` / `Gauche` : Chapitre suivant / précédent.
- `Home` / `End` : Haut / Bas de page.
- `Esc` : Fermer les menus et modals.

## 🔮 Suggestions & Évolutions
- **Export ZIP** : Permettre d'exporter ses propres livres importés pour les partager.
- **Mode Plein Écran** : Un bouton dédié pour une immersion totale.
- **Intensité Ambiance** : Contrôle fin de l'intensité des effets visuels (faible/moyen/élevé).
- **Preset Lecture Longue** : Réduction automatique des animations pour les sessions prolongées.

## 🛠️ Utilisation locale
1. Clonez le dépôt.
2. Lancez un serveur statique : `python -m http.server 8000`.
3. Accédez à `http://localhost:8000`.

## 📜 Licence & Crédits
Créé par **Geoffroy Streit**. Développé par **Antigravity**.
Tous les contenus musicaux et littéraires natifs sont la propriété exclusive de Geoffroy Streit (Hylst).
