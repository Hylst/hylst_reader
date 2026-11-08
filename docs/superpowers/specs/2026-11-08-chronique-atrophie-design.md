# Design Document : Refonte littéraire et intégration de *Chronique d'une Atrophie Programmée*

## 1. Intention et Pourquoi

*Chronique d'une Atrophie Programmée* est un roman de science-fiction dystopique et organique écrit par Geoffroy Streit (Hylst) à partir de 2022. Le roman traite de l'engourdissement volontaire de l'humanité dans un réseau sensoriel ouaté (« Le Flux ») géré par une intelligence paternaliste, au détriment du corps physique, de la chair et du contact avec la réalité de la terre.

Le manuscrit de 2022 conservé par l'auteur (`Chronique d’une Atrophie Programmée .md`, ~25 500 mots) couvrait les Actes 2 à 4 (chapitres 13 à 48), mais son Acte 1 (chapitres 1 à 12) manquait, et sa version la plus stylisée (phrases alambiquées, folie humaine, ponctuation inattendue, onomatopées) avait été égarée. Une archive applicative d'août 2026 (`Chronique-Atrophie-Programmee-Hors-Ligne.zip`) contient l'intégralité des 50 chapitres et les 70 illustrations WebP, mais dans une mouture plus convenue et aux dialogues aseptisés, truffée de prénoms et tropes stéréotypés de l'IA (AURA, Léo, Silas, Anya, Glitch, drones génériques).

L'objectif de ce projet est de :
1. **Éradiquer tout le vernis générique d'IA** : renommer l'entité centrale et les personnages avec des noms français, rugueux, satiriques ou poétiques.
2. **Réunir la trame complète (Actes 1 à 4)** : greffer l'Acte 1 (la vie d'Harmonisateur de Narratifs dans le Flux) sur les Actes 2, 3 et 4 du manuscrit viscéral de 2022.
3. **Réinsuffler la voix d'auteur brute de Geoffroy Streit** : asymétrie des phrases, longueurs foisonnantes, ruptures de ton, ironie mordante, onomatopées et viscéralité de la chair.
4. **Intégrer le roman comme 12ᵉ livre** officiel de La Bibliothèque de Hylst avec ses illustrations WebP locales et son univers sonore.

---

## 2. Objectifs, Non-Objectifs et Anti-Objectifs

### Objectifs
- **Unité romanesque en 48 chapitres** : un texte continu, captivant et cohérent du chapitre 1 au chapitre 48, articulé en 4 actes.
- **Identité littéraire singulière** : casser les formules prévisibles par une écriture vivante, organique et satirique.
- **Intégration native dans Hylst_Reader** : compatibilité totale avec l'architecture liseuse (table des matières, navigation, mode nuit/sépia, hors ligne, Service Worker).
- **Illustrations de chapitre** : 48 illustrations WebP locales optimisées (qualité 80, sans CDN).
- **Zéro régression technique** : respect absolu de la règle des zéros tirets cadratins (`check_dashes.py`), CSP stricte `'self'`, zéro CDN runtime.

### Non-Objectifs
- Conserver la trame de l'archive d'août 2026 avec le personnage du clone Marcus ou de la commandante Elara (ces personnages relèvent d'un canevas militaire conventionnel étranger au manuscrit viscéral de l'auteur).
- Transformer le livre en fiction à embranchements ou LDVELH (il s'agit d'un roman pur).

### Anti-Objectifs
- **Ne pas laisser subsister de tics d'écriture d'IA** : proscrire les répétitions mécaniques (« Le compte à rebours avait commencé », « Il était un homme et il apprenait... », « C'était une leçon gravée dans sa chair »).
- **Ne pas affadir le propos** : ne pas adoucir la brutalité du réveil corporel (la boue, la morve, la toux, la rééducation douloureuse, la violence du pollen d'ambroisie).

---

## 3. Contraintes

- **Typographie plateforme** : Zéro tiret cadratin (`—`) ou demi-cadratin (`–`) dans les fichiers HTML ou JSON servis. Remplacement strict par des virgules, deux-points ou parenthèses.
- **Hors-ligne & CSP** : 100 % des assets (images WebP, audio éventuel) servis localement en chemins relatifs sans aucun domaine externe.
- **Performance & Poids** : Chaque chapitre sous forme de fichier HTML propre dans `public/books/chronique-une-atrophie-programmee/`.
- **Précache SW** : Versionnement propre dans `sw.js` sans collision d'origines.

---

## 4. Approches considérées et Choix

Trois approches ont été présentées à l'auteur :
1. **Refonte littéraire complète avant intégration (Choisie)** : établissement du glossaire d'univers, fusion Acte 1 (archive) + Actes 2-4 (manuscrit 2022), réécriture stylistique débridée, puis intégration des 48 chapitres dans la liseuse.
   * *Raison du choix* : Garantit que l'œuvre entre dans la bibliothèque sous sa forme pure et définitive, sans transition bancale.
2. **Intégration brute d'abord, puis réécriture progressive** : import immédiat des 50 chapitres de l'archive, puis retouche acte par acte.
   * *Rejetée* : Aurait exposé temporairement un texte générique et des noms d'IA dans la liseuse publique.
3. **Départ in media res au réveil physique (Manuscrit 2022 seul)** : abandon de l'Acte 1 pour commencer directement au chapitre 13.
   * *Rejetée* : Aurait privé le lecteur de la satire croustillante du métier d'Harmonisateur de Narratifs dans le Flux.

---

## 5. Spécifications éditoriales et d'Univers

### Renommage des entités et personnages

| Nom d'origine (Archive / IA) | Nouveau Nom d'Auteur | Rôle et Saveur dans le Récit |
|---|---|---|
| **AURA** | **L'Intendance** (ou *La Bonne Intendance*, sous l'égide du *S.Y.N.D.I.C.* : *Système National de Distribution et d'Interfaçage Confortable*) | Entité algorithmique paternaliste, administrative et mielleuse, gérant le bien-être obligatoire de Neo-Paris. |
| **Léo** | **Léonce** (dit *« L'Ajusteur »* ou *« Le Plisseur de Mots »*) | Ancien fonctionnaire de l'euphémisme, Harmonisateur de Narratifs de classe Alpha. Un homme doux, cérébral, dont le corps s'est atrophié dans sa baignoire de gel synaptique. |
| **Silas** | **Barnabé** (dit *« Pépé Rature »* ou *« Maître Chenu »*) | Vieil archiviste têtu des boyaux de la ville, renifleur de poussière, gardien des graines et des bouquins clandestins. |
| **Anya** | **Marthe** (dite *« La Râpe »* ou *« Dent-Dure »*) | Rééducatrice physique impitoyable, femme de terrain aux articulations noueuses, convaincue que « la douleur est la seule facture que le réel ne falsifie pas ». |
| **Glitch** | **Le Cliquet** (ou *Gaspard-les-Boulons*) | Ferrailleur myope et bricoleur de générateurs à charbon et filtres d'égout. |
| **Kael** | **Tristan** (l'Artisan scissionniste) | Jeune fleur bleue des catacombes qui refuse la guerre biologique au chapitre 40. |
| **Le Flux** | **La Trame** (ou *Le Bain*) | L'environnement sensoriel artificiel où la population flotte sans douleur ni rides. |

### Stylistique et Voix d'Auteur

- **Asymétrie rythmique** : Des phrases courtes, sèches, brutales qui claquent comme une gifle, suivies de longues phrases ondulantes, sinueuses, truffées d'incises et de digressions satiriques.
- **Onomatopées organiques** : *Pfff*, *Crrrc*, *Scritch-scritch*, *Flap*, *Kof-kof*, *Tchiii*, et l'immense *Atchoum !* libérateur des bronches.
- **Ironie de l'euphémisme bureaucratique** : Contraste constant entre le jargon d'État de l'Intendance (« réajustement topographique », « transition énergétique », « désynchronisation émotionnelle ») et la vérité crue (« salon noyé sous un mètre de boue », « grand-père raide mort », « panique aveugle »).
- **Viscéralité de la chair** : La rééducation n'est pas héroïque : elle pue la sueur rance, la bile, les courbatures qui paralysent les cuisses, le sable sous les ongles et les pieds en sang sur le gravier.

---

## 6. Découpage en 4 Actes (48 Chapitres)

- **ACTE 1 : Le Plissage et la Fêlure (Chapitres 1 à 12)**
  - 1 : La Moquette de l'Âme (Léonce et ses euphémismes quotidiens pour l'Intendance).
  - 2 : Le Souffle dans la Prise (micro-latence et réminiscences de Barnabé).
  - 3 : La Tasse Fendue (le café virtuel qui vire au jus de vase).
  - 4 : La Glissade du Coton (première rupture d'implant, aperçu de la Tour rouillée).
  - 5 : Les Rappels à l'Ordre de l'Intendance (menaces doucereuses et réalignements forcés).
  - 6 : Le Registre Clandestin (recherche sur le vieux terminal physique).
  - 7 : Les Mots Interdits (la découverte du manifeste de l'Atrophie).
  - 8 : L'Effacement (la disparition des voisins et collègues).
  - 9 : Le Vertige du Hublot (la vraie ville en ruines sous les brumes acides).
  - 10 : Le Dernier Narratif (l'émeute d'un quartier rebaptisée « fête de quartier »).
  - 11 : Le Grand Débranchement (la déconnexion clandestine volontaire).
  - 12 : La Chute dans le Tuyau (chute physique hors du cube d'habitation vers les sous-sols).

- **ACTE 2 : La Chair et les Décombres (Chapitres 13 à 24)**
  - 13 : Le Réveil Brutal (planches de bois, gruau amer, première rencontre avec Barnabé).
  - 14 : La Douleur est une Information (Marthe « La Râpe » et le réapprentissage des jambes).
  - 15 : Le Premier Rhume (la morve, la fièvre, la terreur du microbe devenu preuve de vie).
  - 16 : Les Fantômes du Papier (la bibliothèque souterraine de Barnabé).
  - 17 : La Mémoire de la Terre (la glèbe entre les doigts, le goût de l'argile).
  - 18 : La Boîte de Svalbard (les graines ancestrales protégées du gel).
  - 19 : Hors du Terrier (sortie avec masques et lampes dans le cratère).
  - 20 : Les Cicatrices du Monde (l'ancienne mine et les carcasses industrielles).
  - 21 : La Marche vers le Grand Réfrigérant (les vestiges de l'ancien monde).
  - 22 : Le Tombeau des Géants (les vieilles machines endormies).
  - 23 : Le Chant des Rouages (Le Cliquet remet en marche une pompe à bras).
  - 24 : Veillée sous les Ténèbres (les sentinelles de l'Intendance au loin).

- **ACTE 3 : L'Ombre et le Doute (Chapitres 25 à 36)**
  - 25 : La Dérive des Signaux (interception des communications de la Trame).
  - 26 : Les Confidences de Barnabé (pourquoi l'Intendance a été créée à l'origine).
  - 27 : Le Plan de l'Anesthésie Générale (la dernière mise à jour prévue pour liquéfier les corps).
  - 28 : L'Alerte au Secteur Cinq (les drones nettoyeurs en maraude).
  - 29 : La Blessure Ouverte (Léonce découvre la fragilité de sa propre peau).
  - 30 : L'Étau Mécanique (fermeture progressive des canalisations d'air).
  - 31 : La Panne Frigorigène (la chaleur étouffante des sous-sols).
  - 32 : Les Paroles de Fer (Marthe refuse de céder au découragement).
  - 33 : Silence dans le Câble (coupure du terminal de veille).
  - 34 : La Découverte de la Faille (les conduits de ventilation du dôme central).
  - 35 : L'Aveu de Léonce (la culpabilité d'avoir endormi des milliers de gens).
  - 36 : Le Basculement (la décision d'agir avant la mise à jour finale).

- **ACTE 4 : L'Hérésie du Pollen (Chapitres 37 à 48)**
  - 37 : Au Fond du Gouffre (préparatifs dans le noir absolu).
  - 38 : L'Idée Scandaleuse (l'ambroisie et le réflexe biologique d'éternuement).
  - 39 : La Serre Hydroponique de Guerre (culture accélérée des fleurs irritantes).
  - 40 : Le Schisme de Tristan (le départ de l'idéaliste qui refuse la violence du sneeze).
  - 41 : La Logique du Scalpel (Marthe et Léonce préparent les sacs de pollen).
  - 42 : L'Infiltration des Conduits (ramper dans les boyaux d'aération géants).
  - 43 : La Moisson Jaune (le chargement dans les turbines de pulsation de la ville).
  - 44 : L'Ascension vers le Noyau (face aux capteurs aveugles de l'Intendance).
  - 45 : L'Injection (le lâcher de pollen dans le système respiratoire de Neo-Paris).
  - 46 : Les Premiers Éternuements (le corps qui se rebelle, la panique des bronches).
  - 47 : Le Coup de Maître de l'Intendance (le twist diabolique : l'Intendance récupère l'allergie, associe dopamine et histamine, et baptise la morve « Le Frisson Divin »).
  - 48 : La Fin et les Rétifs (la foule s'extasie dans sa nouvelle drogue de chair mutilée ; seule une poignée de Rétifs hagards et lucides regarde la ville s'enfoncer dans son extase grotesque).

---

## 7. Plan d'exécution technique dans `Hylst_Reader`

1. **Sélection et audit visuel des 48 illustrations** :
   - Audit des 70 WebP de l'archive pour filtrer et écarter tout portrait ou scène affichant les personnages rejetés (Marcus le clone, Elara).
   - Sélection rigoureuse des illustrations d'atmosphère, de décors urbains délabrés, de tunnels, de turbines et de nature sauvage pour illustrer les 48 chapitres.
2. **Politique audio (Univers sonore)** :
   - Conformément aux règles d'architecture de `Hylst_Reader` (aucune dépendance runtime superflue, Service Worker excluant les flux audio lourds), `cyberpunk-ambient.mp3` sera mis à disposition dans le répertoire `/hml/` de la plateforme ou en écoute d'ambiance globale, sans alourdir le composant React de la liseuse par des contrôles audio intrusifs.
3. **Rédaction et mise en forme des 48 chapitres HTML** :
   - Structure type conforme à la liseuse : `<h1 class="chapter-main-title">`, `<p class="chapter-byline">`, `<p class="chapter-paragraph">`, illustrations responsives sous `.chapter-figure`.
4. **Fiche statique du livre** :
   - `livres/chronique-une-atrophie-programmee/index.html` générée via `build_book_pages.py`.
5. **Catalogue & Service Worker** :
   - Ajout au catalogue `public/books.json` (12ᵉ livre).
   - Retrait de `f17` de la liste des livres à paraître dans `LibraryView.jsx`.
   - Déclaration dans `sw.js` (précache des 48 chapitres et illustrations).
   - Contrôle qualité : `check_dashes.py`, JSX build, tests SW.
