# Changelog
Toutes les modifications notables apportées au projet **Hylst Books & Reader** sont documentées dans ce fichier.

## [1.6.0] - 2026-11-03
### Ajouté
- **Les 10 chapitres de *L'Odyssée de l'énergie* sont disponibles** : préambule, introduction, chapitres 1 à 8. La navigation de fin de partie et la pastille `n / 10` fonctionnent sur l'ensemble du livre.
- **Relecture orthographique et grammaticale complète** : accents rétablis, coquilles et accords corrigés, tirets cadratins et demi-cadratins supprimés, ornements `✦` retirés.

### Modifié
- **Données actualisées** : AIE 485 TWh en 2025 et environ 950 TWh en 2030, Irlande 22 % de son électricité en 2024, parc nucléaire français 57 réacteurs et 63 GW pour un âge moyen d'environ 39 ans, CATL environ 39 %, 39 réacteurs chinois en construction, coûts du solaire en baisse d'environ 90 % depuis 2010.
- **Titres de chapitres** : les entrées du sommaire reprennent les titres réels (`I. La faim électrique`, `II. L'inflation des besoins`, etc.).
- **Mention de transparence IA** : encart discret en bas de la dernière de couverture.
- Version 1.6.0, cache Service Worker source `hylst-reader-v48`.

### Corrigé
- Accents manquants dans les chapitres 5 à 8, notamment les passés composés, les prépositions `à` et les adjectifs.
- Coquilles et accords signalés par la relecture : `publie` → `publiées`, `considerabel` → `considérable`, `neglege` → `négligé`, `environmentales` → `environnementales`, `dedicees` → `dédiées`, `incrementales` → `incrémentales`, `confinée` → `confinées`, entre autres.

## [1.5.0] - 2026-11-03
### Ajouté
- **Accès sans slash final** : `https://hylst.fr/books_reader` fonctionne désormais comme `https://hylst.fr/books_reader/`, grâce à une base d'URL explicite dans l'index de production. Le redirect 301 canonique reste recommandé côté Nginx.
- **Transparence IA** : *L'Odyssée de l'énergie* affiche en bas de sa dernière de couverture une mention discrète précisant l'usage d'outils d'intelligence artificielle comme assistants de recherche, de documentation, de vérification des sources, de brainstorming et de rédaction.

### Modifié
- **L'Odyssée de l'énergie** : actualisation des données structurantes (AIE avril 2026 : 485 TWh en 2025, ~950 TWh en 2030 ; Irlande 22 % de son électricité en 2024 ; parc nucléaire français 57 réacteurs / 63 GW, âge moyen ~39 ans ; CATL ~39 % ; 39 réacteurs chinois en construction).
- **Typographie** : suppression de tous les tirets cadratins et demi-cadratins ainsi que des ornements `✦` dans les textes de *L'Odyssée de l'énergie*.
- **Chapitres** : titres et tableaux corrigés (cohérence 57 réacteurs / 63 GW, 39 ans), note de méthode datée au 3 novembre 2026.
- Version 1.5.0, cache Service Worker source `hylst-reader-v47`.

### Corrigé
- `.../books_reader` sans slash ne chargeait plus l'application (CSS et vendor résolus à la racine).

## [1.4.0] - 2026-11-03
### Ajouté
- **Navigation de fin de partie** : un bloc « Fin de la partie » avec le titre de la partie suivante est désormais intégré au flux de lecture, sous le dernier paragraphe. Il est visible même quand la barre d'outils est masquée.
- **Pastille de secours** : en lecture immersive ou plein écran, quand les commandes sont masquées, une pastille discrète `1 / 7 · Suivant` reste visible en bas de l'écran. Elle permet d'afficher les commandes ou de passer directement à la partie suivante.
- **Fin du livre** : dernier chapitre avec bloc « Fin du livre » et retour à la fiche.

### Modifié
- Intro des *Ficelles du bonheur* : byline `2025/26`, mention « Texte intégral ».
- Version 1.4.0, cache Service Worker source `hylst-reader-v46`.

## [1.3.1] - 2026-11-03
### Modifié
- **Corrections de coquilles** dans *Les Ficelles du bonheur*, sélectionnées par l'auteur : « une promesse en quelques années » → « une promesse quelques années », « Imaginez-vous », « pêle-mêle », « dit-on », « nous regarde, Auguste », guillemets fermants, « N'est-ce pas », « ainsi, ne pense-t-elle pas », « compte-t-elle. », « un peu... », « jusqu'au menton, lui faisant », « depuis cette année-là qu'on », « toujours fait... », « aux lèvres », « Je le sais, Odette. », « un hoquet », « moult postillons », « le carton », « suit du regard », « j'ai l'impression que », « touchant chez eux. »
- **Couverture illustrée** : génération locale avec Qwen-Image-2.1 (`qwen-image-21-uc-sdcpp`), format 5:6, sans texte. Elle remplace la couverture typographique de secours pour ce livre.
- L'intro précise désormais « Texte intégral, avec corrections de coquilles. »
- Version 1.3.1, cache Service Worker source `hylst-reader-v45`.
- Note : en production, `scripts/sync-to-platform.ps1` remplace ce nom par l'empreinte de build (`hylst-reader-d9e7b736999a` pour ce build).

## [1.3.0] - 2026-11-03
### Ajouté
- **Les Ficelles du bonheur** : nouvelle pièce de théâtre pour Halloween (29 octobre 2025), intégrée en 7 chapitres (six tableaux et un épilogue). Le texte est conforme au manuscrit DOCX, sans correction ni réécriture.
- **Didascalies bleues** : les passages en bleu du Word sont conservés et stylés via `.scene-description` / `.scene-description-inline`, avec une couleur adaptée aux thèmes Sépia, Clair et Sombre.
- **Mise en page théâtre** : les répliques sont alignées à gauche (`.chapter-paragraph.dialogue`), les didascalies ont un filet bleu discret.
- **Lien direct** : `?book=les-ficelles-du-bonheur` ouvre directement la fiche du livre.
- **Couverture typographique de secours** pour les livres sans image, avec badge `Nouveau`.
- CSS : styles de didascalies, répliques et ligne de crédit (`chapter-byline`).

### Modifié
- `public/books.json` : trois livres intégrés (IA, Énergie, Ficelles du bonheur).
- `LibraryView` et `BookHomeView` : fallback de couverture et badge.
- Version 1.3.0, cache Service Worker `hylst-reader-v44`.

## [1.2.1] - 2026-11-02
### Sécurité
- **Dépendances auto-hébergées** : React 18.3.1, ReactDOM 18.3.1, Babel 8.0.9, idb-keyval 6.3.0, epub.js 0.3.93, JSZip 3.10.2 et DOMPurify 3.4.17 dans `vendor/`. Plus aucun CDN JavaScript au runtime.
- **Assainissement des imports** : DOMPurify filtre les EPUB, dossiers HML et JSON importés (scripts, iframes, gestionnaires d'événements, URL `javascript:`). Les textes TXT/MD sont échappés avant conversion HTML.
- **Défense en profondeur** : `BookHomeView` et `ReaderView` re-filtrent les livres importés déjà présents dans IndexedDB.
- **Liens externes** : `rel="noopener noreferrer"` sur les liens `target="_blank"` du modal À propos.
- **CVE** : vérification OSV du 2026-11-02, aucune vulnérabilité connue pour les versions retenues. JSZip passe de 3.10.1 à 3.10.2.

### Ajouté
- `js/sanitize.js` : helper `HylstSanitize` (`sanitizeHtml`, `sanitizeBook`, `escapeHtml`).
- `vendor/LICENSES.md` : versions, licences et empreintes SHA-256 des dépendances.
- `scripts/sync-to-platform.ps1` : synchronisation sûre vers `Cours_Memos/Docker/books_reader`, cache-busting par empreinte de build, vérifications, suppression du `.env` du miroir, commit local optionnel sans push.

### Corrigé
- `gen_music_data.py` produit désormais `const MUSIC_LIBRARY` + `window.MUSIC_LIBRARY` (au lieu d'un `export` incompatible avec le chargement par balise `<script>`).
- Piste **Dreamlike Embrace** : référence corrigée en `dreamlike_embrace.mp3/.webp` (l'ancien nom `dreamlike_embracemp3` n'existait pas dans `/hml/`).
- **Signets** : `removeSignet` filtre désormais sur `chapterIdx` au lieu d'un `id` inexistant, ce qui supprimait tous les signets du livre.
- Cache Service Worker bumpé : `hylst-reader-v43` en source, empreinte de build en production.

## [1.2.0] - 2026-05-30
### Ajouté
- **Chapitre 5 Intégré** : Intégration officielle du chapitre 5 *« De Spectateur à Architecte »* de l'essai **L'Odyssée de l'IA** (`chapitre-5.html` dans `public/books` et dans `livres_pour_import`).
- **Nettoyage Littéraire** : Réécriture complète des tirets cadratins `—` et retrait des ornements `✦` qui font trop « généré par IA » pour un rendu plus naturel et fluide.
- **Remplacement de « Dualis-IA »** par la dénomination officielle de l'essai : *« L'odyssée de l'IA : 2 futurs, un choix »* (ou tournures de phrases adaptées comme « ce projet », « ce livre »).
- **Couverture Chapitre 5** : Génération de l'illustration manquante `chapitre-5-cover.webp` en WebP dans un style artistique premium sépia/or homogène avec les 4 précédents chapitres.
- **Documentation Technique Complète** : Création de `structure.md` (arborescence), `features.md` (fonctions), `readme-dev.md` (architecture) et `test_build_deploy.md` (guide pas-à-pas pour Windows local et déploiement VPS Hostinger + Coolify + Nginx statique dans `/books_reader/`).

### Modifié
- **Modularisation React Majeure** : Division du fichier unique massif `js/app.jsx` (2000 lignes) en composants ES6 réutilisables chargés par Babel en ligne dans `js/components/` (`Icon.jsx`, `Ambience.jsx`, `AboutModal.jsx`, `GlobalSettingsModal.jsx`, `MusicPlayerModal.jsx`, `LibraryView.jsx`, `BookHomeView.jsx`, `ReaderView.jsx`). `js/app.jsx` est allégé et plus lisible (ramené à 380 lignes).
- **Service Worker Offline** : Optimisation du fichier `sw.js` (Cache v1.2.0) pour mettre en cache les requêtes de CDN externes (`unpkg.com`, `cdn.jsdelivr.net`, etc.) avec une stratégie Cache-First, rendant l'application 100% autonome et résiliente hors-ligne.
- **README.md & about.md** : Actualisation des descriptifs du projet et de la stack.

## [1.1.12] - 2026-03-03
### Corrigé
- **Animations d'ambiance** : Correction définitive de la visibilité des effets en forçant la transparence des conteneurs de texte et en boostant l'opacité et le contraste des calques d'animation. Le z-index a été réorganisé pour garantir que l'ambiance soit toujours visible sous le texte.
- **Temps de lecture** : Déplacé à l'intérieur de la barre de navigation inférieure (au centre, à gauche du compteur de chapitre) pour éviter tout chevauchement avec les boutons de saut de page.
- **Nettoyage UI** : Suppression de l'ancien indicateur flottant et des badges redondants en haut de page.

## [1.1.11] - 2026-03-03
### Corrigé
- **Animations d'ambiance** : Correction du problème de z-index qui rendait les animations invisibles. Elles sont maintenant visibles dans tous les modes (Sépia, Clair, Sombre).
- **Temps de lecture** : Déplacement de l'indicateur en bas à droite de l'écran (visible uniquement au clic/touch) pour plus de discrétion et d'utilité.

### Ajouté
- **Indicateurs paramétrables** : Nouveaux réglages pour activer/désactiver l'affichage du temps restant et du pourcentage de progression dans le slider.
- **Slider pourcentage** : Affichage dynamique du pourcentage de lecture au niveau du curseur de défilement.

## [1.1.10] - 2026-03-03
### Corrigé
- **Lecture (layout)** : Correction du rendu du mode lecture perturbé par la couche d’ambiance (empilement/z-index stabilisé, affichage de contenu restauré).
- **Mode Sombre** : Effet allégé pour éviter le voile trop dense et améliorer le confort visuel.
- **Mode Clair** : Effet rendu visible avec halos très subtils et particules discrètes.

### Modifié
- **Mode Sépia** : Remplacement des bandes trop marquées par des nappes lumineuses douces et lentes, mieux intégrées au style littéraire.
- **Animations ambiantes** : Particules moins nombreuses, plus lentes, plus légères GPU/CPU, dérive réduite pour un mouvement plus naturel.
- **Transitions d’ambiance** : Opacités et amplitudes ajustées pour des animations progressives, qualitatives et non intrusives.

### À faire
- Ajouter un réglage utilisateur “Intensité ambiance” global (faible/moyen/élevé).
- Ajouter un preset “Lecture longue” qui réduit automatiquement l’animation.

## [1.1.9] - 2026-03-03
### Ajouté
- **Animations par thème** : Nouveau réglage dans les modals de paramètres pour activer/désactiver indépendamment les animations de fond en Sépia, Clair et Sombre.
- **Ambiance différenciée** : Trois identités visuelles distinctes selon le thème (onde chaleureuse en Sépia, halo clair en mode Clair, aura + scintillement en mode Sombre).

### Modifié
- **Bloc Continuer/Reprendre** : Refonte complète du composant avec hiérarchie typographique, meilleure lisibilité du titre, troncature élégante et CTA premium.
- **Paramètres UI** : Boutons de thème harmonisés avec icônes du design system (sans emoji), cohérence renforcée avec les tokens existants.
- **Ambiance en lecture** : Les animations de fond sont désormais visibles dans ReaderView et non uniquement dans les écrans bibliothèque/modals.

### Corrigé
- **Visibilité Sépia** : Intensité et contraste ajustés pour rendre l’ambiance perceptible sans nuire au confort de lecture.
- **Persistance settings** : Normalisation des préférences d’animation par thème dans les settings sauvegardés.
- **Cache** : Bump cache-busting vers `v1.1.9` et Service Worker `hylst-reader-v9` pour forcer la prise en compte des nouveaux styles.

### À faire
- Ajuster un slider de densité des effets pour un contrôle fin de l’intensité visuelle.
- Ajouter un preset “Mode minimal” (animations ultra-subtiles) pour les longues sessions de lecture.

## [1.1.0] - 2026-03-03
### Ajouté
- **Bibliothèque Musicale** : Accès direct aux compositions de Geoffroy Streit.
- **Lecteur Audio** : Contrôles avancés (Play/Pause, Loop, Mini-bar header, animations de vagues).
- **Menu Settings** : Personnalisation de l'expérience de lecture (taille police, thèmes, alignement).
- **Import Header** : Bouton d'accès rapide à l'importation de dossiers HML.

### Modifié
- **UI Redesign** : Passage à une largeur de modal de 1100px pour la musique.
- **Organisation** : Séparation claire entre la "Bibliothèque Hylst" et "Vos autres lectures".
- **Documentation** : Mise à jour complète de `README.md`, `resume.md` et `about.md`.

### Corrigé
- Bug de disparition du bouton Settings.
- Problème de filtrage des livres importés (`isImported` property).

## [1.1.1] - 2026-03-03
### Modifié
- **Cartes livres** : Grille élargie pour éviter les cards trop étroites.
- **Modals** : Refonte des styles pour restaurer hiérarchie et lisibilité.
- **Bibliothèque musicale** : Harmonisation des classes CSS avec le rendu réel.

### Corrigé
- Scroll vertical restauré dans la bibliothèque.
- Dégradations visuelles sur About, Settings et Music.
- Bouton pause parasite retiré de la bibliothèque musicale.

### À faire
- Vérifier le responsive sur vieux mobiles après ce correctif.

## [1.1.2] - 2026-03-03
### Modifié
- **Cards livres** : Hauteurs normalisées via conteneur couverture.
- **Layout** : Chaîne de hauteur corrigée pour le scroll bibliothèque.

### Corrigé
- Erreur `idb` non défini lors du chargement.
- État audio stabilisé si un flux distant échoue.

## [1.1.3] - 2026-03-03
### Modifié
- **Cards bibliothèque** : Hauteur réduite et densité visuelle ajustée.
- **Section À venir** : Texte enrichi en deux paragraphes.
- **Mini player** : Ouverture par clic sur la miniature/titre + aperçu au survol.

### Corrigé
- Indicateur loop rendu visuel et durable via alternance d’icônes.

## [1.1.8] - 2026-03-03
### Ajouté
- **Ambiance Visuelle** : Effet de grain de papier animé et poussière flottante discrète dans les modes Sépia et Sombre pour une immersion renforcée.
- **Mode Immersion** : Bouton plein écran dans le lecteur pour masquer l'interface du navigateur.
- **Temps de lecture dynamique** : Affichage du temps restant estimé pour finir le chapitre, mis à jour en temps réel selon votre progression.

### Modifié
- **About Modal** : Refonte complète du design. Le modal est plus large (1100px), mieux structuré et responsive. Correction des problèmes de troncature de texte.
- **Icônes** : Ajout des icônes Maximize/Minimize pour le mode plein écran.

## [1.1.7] - 2026-03-03
### Corrigé
- **Crash AboutModal** : Correction de l'erreur React #130 causée par l'utilisation d'icônes non définies. Ajout de 10 nouvelles icônes au set global.

### Modifié
- **Documentation** : Mise à jour de `about.md` et `README.md` avec les nouvelles fonctionnalités.
- **Git** : Nettoyage du fichier `.gitignore` pour une meilleure gestion du repo.

### Suggestions & À venir (Backlog)
- **Import/Export** : Permettre l'exportation d'un livre (config + chapitres) au format ZIP pour partage.
- **Lecture** : Indicateur de temps de lecture restant pour le chapitre en cours.
- **Ambiance** : Ajout d'animations de fond discrètes (particules, dégradés animés) liées au thème.

## [1.1.6] - 2026-03-03
### Ajouté
- **Raccourcis Clavier** : Support complet pour la navigation (Espace pour scroller, Flèches pour changer de chapitre, Home/End pour sauter en haut/bas).
- **Redesign Modal About** : Nouvelle interface en onglets (À propos, Fonctions, Créateur, Astuces) avec un design plus moderne, interactif et informatif.

### Modifié
- **Recherche** : Suppression de la fonction de recherche intégrée au profit de la recherche native du navigateur (`Ctrl + F`), plus performante et universelle.
- **UI** : Amélioration de la fluidité des animations et des transitions de vue.

## [1.1.5] - 2026-03-03
### Modifié
- **Navigation** : Barre de navigation de chapitre (Précédent/Suivant) désormais fixe en bas de page, fusionnée avec les boutons de saut (Haut/Bas) pour une meilleure accessibilité.
- **Recherche** : Cliquer sur un résultat de recherche dans le chapitre en cours fait défiler la page jusqu'à l'occurrence avec un effet de surbrillance temporaire.

### Corrigé
- **Images chapitres** : Correction des liens brisés vers les couvertures de chapitres (réécriture dynamique des chemins relatifs).

## [1.1.4] - 2026-03-03
### Modifié
- **Settings** : Mise en page recentrée et cartes de réglages stylisées.
- **À venir** : Paragraphes enrichis en blocs avec effets et gradients.
- **Book Home** : Mise en page lisible et scrollable.
- **Typographie** : Normalisation des titres et paragraphes du lecteur.

### Corrigé
- **Lecteur** : Réactivation du scroll et des contrôles au tap.
- **Dropcap** : La capitale initiale n’agrandit plus tout le paragraphe.

## [1.0.0] - 2026-02
- Version initiale : Liseuse PWA, support HML, stockage IndexedDB, Mode Lecteur premium.
