# Dépendances JavaScript auto-hébergées

Ces fichiers sont servis localement par l'application, sans CDN au runtime.
Dernière vérification CVE : 2026-11-02 (OSV.dev, aucune vulnérabilité connue pour ces versions).

| Fichier | Version | Licence | SHA-256 |
|---|---|---|---|
| `react.production.min.js` | React 18.3.1 | MIT | `d949f1c3687aedadcedac85261865f29b17cd273997e7f6b2bfc53b2f9d4c4dd` |
| `react-dom.production.min.js` | React DOM 18.3.1 | MIT | `35f4f974f4b2bcd44da73963347f8952e341f83909e4498227d4e26b98f66f0d` |
| `idb-keyval.js` | idb-keyval 6.3.0 | Apache-2.0 | `1d5aefa0c1cc78962ef116f11b7608dafeabf4950f71cb99fdab410422921d52` |
| `jszip.min.js` | JSZip 3.10.2 | MIT ou GPL-3.0-or-later | `7f839b2d4688b845c105ebf5d2f9803075f91ea0fe72bdaac176c3a04dd3d2c1` |
| `epub.min.js` | epub.js 0.3.93 | BSD-2-Clause | `06eae15745107b4aa508c95538275251f69bfb9f1175621fc458d9f42ed082d4` |
| `purify.min.js` | DOMPurify 3.4.17 | MPL-2.0 ou Apache-2.0 | `cd37898f9782adf54820c413191b5691803f0f137c799d6edcfd38523b4c2c31` |

## Outil de build (non servi)

| Fichier | Version | Licence | SHA-256 |
|---|---|---|---|
| `scripts/vendor/babel.min.js` | @babel/standalone 8.0.9 | MIT | `111f486263ad78ecf27322c26e4e219695b9ace603b5952b4b2bbe4f9ebf7919` |

Babel sert uniquement à précompiler `js/*.jsx` vers `js/dist/*.js` avec `scripts/build_jsx.js`. Il n'est plus chargé par la liseuse et n'est pas copié dans le miroir de production.

## Notes de mise à jour

- **JSZip 3.10.2** : correctifs de détection de type binaire cross-realm et de support Blob.
- **DOMPurify 3.4.17** : utilisé uniquement pour assainir les contenus importés (EPUB, dossiers HML, JSON). Les livres intégrés au dépôt ne sont pas filtrés.
- **Babel 8.0.9** : version volontairement figée. Babel 8.1.1 est sorti le 2026-11-02 et n'a pas encore été validé avec cette application.
- **React 18.3.1** : pas de CVE connue pour l'usage client UMD de cette application. Les CVE React Server Components ne s'appliquent pas ici (aucun rendu serveur, aucun RSC).

## Vérification

Les empreintes ci-dessus peuvent être contrôlées avec :

```powershell
Get-FileHash -Algorithm SHA256 vendor\*.js
```

Pour rechercher des CVE :

```powershell
# Exemple avec OSV.dev
curl -X POST https://api.osv.dev/v1/query -H "Content-Type: application/json" -d "{\"package\":{\"name\":\"jszip\",\"ecosystem\":\"npm\"},\"version\":\"3.10.2\"}"
```
