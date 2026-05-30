# Hylst Books & Reader

**Hylst Books & Reader** est une application web de lecture (PWA) conçue avec une architecture *Offline-First* et *Pure Frontend*. Elle offre une expérience de lecture premium, une gestion de bibliothèque locale souveraine, et une intégration musicale unique pour accompagner vos moments de lecture.

Cette application est l'écrin officiel des récits littéraires et musicaux de **Geoffroy Streit (alias Hylst)**.

---

## 🌟 Points Forts

- **Expérience Premium** : Design typographique soigné (*Cormorant Garamond*, *Libre Baskerville*).
- **Musique Intégrée** : Accès à plus de 280 compositions originales de Geoffroy Streit directement dans l'app, filtrables par mood/BPM.
- **Partie V Intégrée** : Intégration du chapitre final *« De Spectateur à Architecte »* de l'essai **L'Odyssée de l'IA** (version nettoyée de ses tics typographiques d'IA).
- **Zéro Backend** : Tout tourne dans votre navigateur. Vos données (livres, progression, signets) restent chez vous dans IndexedDB.
- **Import Flexible** : Importez vos propres textes (EPUB, TXT, MD, JSON) ou dossiers HML complets, lus confortablement dans le Reader.
- **Ambiance Visuelle** : Animations d'ambiance subtiles adaptées à chaque thème (grain de papier, ondes sépia, lueurs blanches, poussières stellaires).
- **Temps de Lecture Intelligent** : Calcul dynamique du temps restant et indicateur contextuel.
- **Interface Adaptative** : Navigation fluide avec indicateurs de progression intégrés.

---

## 🚀 Architecture & Technos

- **Framework** : React 18 (Babel, et dépendances chargés via CDN) - sans étape de build obligatoire !
- **Modularité** : Composants React isolés et autonomes au sein de `js/components/`.
- **Stockage** : `idb-keyval` (IndexedDB) pour la persistance locale totale de vos bibliothèques.
- **PWA & Offline** : Service Worker (`sw.js`) pour l'installation native et cache-first des CDNs. Le mode hors-ligne est donc pleinement fonctionnel une fois l'application ouverte une première fois.
- **Design** : CSS3 Vanilla modulaire.

---

## 📚 En Savoir Plus (Documentation Technique)

Pour comprendre en profondeur le fonctionnement de l'application, consultez nos guides dédiés :
1. 📁 **[Structure du Projet](structure.md)** : Cartographie des dossiers et fichiers.
2. 🛠️ **[Fonctionnalités Détaillées](features.md)** : Descriptif des outils de la liseuse.
3. 🧠 **[Conception Technique](readme-dev.md)** : Explications sur React CDN, Babel Standalone et IndexedDB.
4. 🚀 **[Guide de Test et Déploiement](test_build_deploy.md)** : Guide Windows local + déploiement Hostinger & Coolify (sous-dossier `/books_reader/` avec URL statique Nginx).

---

## ⌨️ Raccourcis Clavier

- `Espace` / `PageDown` : Faire défiler vers le bas d'environ 80%.
- `Flèche Droite` / `Gauche` : Chapitre suivant / précédent.
- `Home` / `End` : Haut / Bas de page.
- `Esc` : Fermer les menus, modals et barres d'outils.

---

## 📜 Licence & Crédits

Créé par **Geoffroy Streit (Hylst)** - Mail : geoffroy.streit@gmail.com  
Développé par **Antigravity**.  
Tous les contenus musicaux et littéraires natifs sont la propriété exclusive de Geoffroy Streit (Hylst).
