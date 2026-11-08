# Le pantin et la poupée de cire : fiche de conception

Date : 8 novembre 2026  
Statut : validé par l'auteur, prêt pour le plan d'implémentation  
Portée : ajout d'une nouvelle poétique inédite dans *Recueils de proses et poésies fantasques · Tome II (Fantasque & merveilleux)* au sein de La Bibliothèque de Hylst.

---

## 1. Intention et genèse

Le texte *Le pantin et la poupée de cire* a été rédigé en novembre 2021 dans le cadre d'un défi littéraire d'écriture (*Nouvember 2021*), avec contraintes de mots imposés au fil des jours (*cire, spasme, vérité, coquelicot, patience, solidaritéfantasques*).

Il constitue le pendant nocturne, magique et intime du conte *Le précieux pantin de bois* (publié sur Wattpad en avril 2021, actuellement chapitre 4 du Tome II). Dans le texte d'avril, le pantin subit l'abandon et la dureté du monde moderne après le départ du vieil artisan, avec le constat amer : *« Nulle fée ne vint lui donner vie... »*. Dans ce texte de novembre, au contraire, une poussière de fée éveille le pantin au cœur de la nuit dans l'échoppe de l'ancienne ruelle des Jouvenceaux. Il allume une bougie et traverse courageusement l'atelier pour rejoindre la poupée de cire endormie dans son écrin de satin.

Le manuscrit retrouvé comprend :
1. Une première partie en prose poétique versifiée (l'éveil, l'ascension téméraire, l'allumette frottée, la bougie coquelicot, la traversée acrobatique des jouets et l'arrivée devant la poupée).
2. Une série de notes de continuation (*A suivre... encre pas, allumette se brûler, 12 coups de minuit, jeu d'ombre, danse, boîte à musique, marelle, baiser, larme, frénétique, flamboiement, impétuosité, pantin allumette poupée fond*).
3. Un poème final complet de 5 strophes d'alexandrins et décasyllabes (*L'aube ouvre son regard, lisse sa chevelure... Un sanglot de cire se suspend à la lune / Une larme volée au cœur d'une poupée*).

L'objectif est d'intégrer ce conte inédit dans la bibliothèque en préservant scrupuleusement le style et le texte de l'auteur, en complétant la scène médiane à partir de ses notes préparatoires, et en reliant la narration au poème dans un ensemble harmonieux et présentable.

---

## 2. Décisions d'architecture et de contenu

- **Titre retenu** : *Le pantin et la poupée de cire*.
- **Emplacement** : **Chapitre 05** du Tome II (*Recueils de proses et poésies fantasques · Tome II : Fantasque & merveilleux*), inséré immédiatement après *Le précieux pantin de bois* (chapitre 04) pour former un diptyque narratif direct.
- **Numérotation du Tome II** : les chapitres existants 05 à 10 sont décalés de 06 à 11. Le recueil passe de 10 à **11 textes**.
- **Introduction du recueil (`intro.html`)** : mise à jour pour présenter 11 textes (de 1999 à 2024/2026) et mentionner le diptyque des pantins de l'artisan.
- **Complétion de la scène médiane** :
  - Style : prose poétique cadencée en vers libres, épousant le souffle, le rythme ternaire et la délicatesse d'époque du manuscrit.
  - Éléments narratifs développés à partir des notes :
    1. *Les douze coups de minuit* qui résonnent au grand pendule d'argent.
    2. *L'éveil musical* : la vieille boîte à musique en fer blanc remontée sur le guéridon, libérant une mélodie cristalline.
    3. *Le jeu d'ombres et la danse* : le pantin enlace la taille de chiffon de la poupée inerte, leurs silhouettes géantes dansant sur les lambris, un pas de marelle enfantin.
    4. *L'impétuosité et le drame du feu* : voulant contempler de plus près son visage et lui dérober un baiser, le pantin approche la flamme ardente de la bougie ; la chaleur adoucit la joue de cire virginale et fait couler une première larme tiède.
    5. *L'agonie de la flamme et l'approche de l'aube* : transition naturelle vers le poème de clôture.
- **Poème de clôture** : conservé **mot à mot** dans son intégralité (5 strophes de 4 vers).
- **Mention de source** : *Texte composé à l'occasion d'un défi littéraire d'écriture (Nouvember 2021), relu et complété pour cette édition numérique*.
- **Typographie** : zéro tiret cadratin ou demi-cadratin. Guillemets français avec espaces insécables.

---

## 3. Objectifs, non-objectifs et anti-objectifs

### Objectifs
- Offrir une lecture poétique, immersive et sensible, fidèle à l'imaginaire de Geoffroy Streit (Hylst).
- Assurer une continuité stylistique indétectable entre le texte original, la scène médiane complétée et le poème final.
- Garantir une intégration parfaite dans la PWA : catalogue `books.json`, sommaire du livre, fiches statiques, précache Service Worker, accessibilité mobile.

### Non-objectifs
- Ne pas modifier le poème de 5 strophes.
- Ne pas altérer le texte préexistant du chapitre 04 (*Le précieux pantin de bois*).
- Ne pas introduire de cadre narratif extérieur au monde de l'artisan et de sa boutique de jouets traditionnels.

### Anti-objectifs
- Proscrire tout remplissage froid ou générique.
- Proscrire tout tiret long dans les fichiers servis.
- Ne pas casser les métadonnées de lecture ou les signets existants des lecteurs.

---

## 4. Contraintes techniques

- Fichier HTML : `public/books/recueils-proses-poesies-t2-fantasque-merveilleux/05-le-pantin-et-la-poupee-de-cire.html`.
- Décalage des fichiers existants :
  - `05-ondes-positives.html` → `06-ondes-positives.html`
  - `06-intermede-feerique.html` → `07-intermede-feerique.html`
  - `07-dangaord.html` → `08-dangaord.html`
  - `08-metro-fantasque.html` → `09-metro-fantasque.html`
  - `09-farouches-apparitions.html` → `10-farouches-apparitions.html`
  - `10-la-taniere-du-mage.html` → `11-la-taniere-du-mage.html`
- Mise à jour de `public/books.json` pour refléter les 11 chapitres, leurs titres, résumés et chemins.
- Regénération de la fiche statique de livre via `python scripts/build_book_pages.py`.
- Validation stricte avec `scripts/check_dashes.py --root .`, `scripts/build_jsx.js --check` et `scripts/test-sw-policy.js`.
- Mise à jour du Service Worker `sw.js` (bump de cache) et synchronisation vers la plateforme.

---

## 5. Approches examinées et arbitrage

### 5.1 Emplacement dans le recueil
1. **Chapitre 05 en diptyque immédiat (Retenu)** : permet une résonance poétique instantanée avec *Le précieux pantin de bois*. Le lecteur découvre la face cachée de l'atelier de l'artisan.
2. **Chapitre 11 en clôture (Écarté)** : séparait artificiellement deux récits situés dans le même univers de jouets d'antan.
3. **Fusion dans le chapitre 04 (Écartée)** : créait un texte hybride bancal mêlant prose classique de conte réaliste et prose poétique versifiée féerique.

### 5.2 Traitement de la scène médiane
1. **Prose poétique cadencée en vers libres (Retenue)** : épouse les retours à la ligne du brouillon, conserve la ponctuation expressive (points de suspension, exclamations) et développe minutieusement les notes de l'auteur.
2. **Paragraphes de prose continue classique (Écartée)** : rompait le rythme lyrique initié dès le premier vers.

---

## 6. Ce qui reste au constructeur

1. Renommer les fichiers de chapitres 05 à 10 vers 06 à 11 dans `recueils-proses-poesies-t2-fantasque-merveilleux`.
2. Rédiger le fichier `05-le-pantin-et-la-poupee-de-cire.html` avec la narration initiale intégrale, la scène médiane harmonisée et le poème de clôture.
3. Mettre à jour `intro.html` et `public/books.json`.
4. Mettre à jour `sw.js` et relancer la chaîne de validation.
5. Regénérer les fiches statiques et contrôler le rendu visuel.
