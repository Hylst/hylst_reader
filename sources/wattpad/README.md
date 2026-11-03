# Sources Wattpad

Ce dossier conserve les **métadonnées de provenance** des textes importés depuis le compte Wattpad de l'auteur. Les textes bruts et les couvertures originales ne sont pas versionnés ici : le manifeste contient les identifiants, les dates et les URL nécessaires à une nouvelle récupération.

## Compte source

- Profil : <https://www.wattpad.com/user/GeoffroyStreit>
- 29 histoires publiées, une seule partie chacune.
- Période : mars 2021 à février 2024.
- Import dans la bibliothèque : 3 novembre 2026.

## Répartition éditoriale

| Recueil | Textes | Période |
|---|---:|---|
| `recueils-proses-poesies-t1-saisons-nature` | 11 | mars 2021 à février 2024 |
| `recueils-proses-poesies-t2-fantasque-merveilleux` | 8 | mars 2021 à février 2024 |
| `recueils-proses-poesies-t3-coeurs-chaos-quotidien` | 10 | mars à septembre 2021 |

Le détail des textes, leur titre d'origine, leur date de publication, leur identifiant de partie et leur URL Wattpad se trouvent dans `manifest.json`.

## API utilisée

- Inventaire : `https://www.wattpad.com/api/v3/users/GeoffroyStreit/stories?limit=50&fields=stories(id,title,description,cover,createDate,modifyDate,parts(id,title,length),tags,language,categories)`
- Texte d'une partie : `https://www.wattpad.com/apiv2/storytext?id=<partId>` (réponse HTML, éventuellement compressée en gzip).

Ces endpoints sont des API internes, non officielles : elles peuvent changer sans préavis. Le manifeste et une sauvegarde locale des textes doivent être conservés avant toute nouvelle importation.

## Conversion vers la liseuse

Les textes ont été convertis en HTML avec les classes de la liseuse :

- `chapter-main-title` pour le titre ;
- `chapter-byline` pour la date de publication ;
- `chapter-paragraph` pour les paragraphes ;
- `poem-stanza` pour les poèmes, avec les lignes séparées par `<br>` ;
- `chapter-source-note` pour le lien vers la version originale.

Les titres décoratifs ont été normalisés pour le sommaire, mais le titre d'origine reste conservé dans `originalTitle`. Le corps des textes n'a pas été réécrit : seuls la conversion, la mise en page et les corrections typographiques évidentes des titres ont été appliquées.

Les textes sont intégralement écrits par Geoffroy Streit (Hylst), sans assistance d'intelligence artificielle. La conversion au format de la liseuse, la mise en page et les ajustements typographiques ont été réalisés avec des outils techniques.

## Droits

Les textes restent la propriété de leur auteur, Geoffroy Streit (Hylst). Les fichiers de couvertures Wattpad d'origine ne sont pas redistribués séparément dans le dépôt ; les couvertures des recueils sont des compositions réalisées pour cette édition à partir de ces illustrations.
