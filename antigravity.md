# Hylst Reader - Project & Context Memory

## Technical Stack & Constraints
- **Core**: HTML, JavaScript (React components inside `js/`), custom CSS (`css/reader.css`).
- **Offline & Storage**: PWA active using `vite-plugin-pwa` with local offline state management (`Dexie`/`localForage`).
- **Development Server**: Python HTTP server running on port `8000`.

---

## ⚠️ CRITICAL RULES & INSTRUCTIONS FOR AGENTS

### 1. Source of Truth for Books
- **L'Odyssée de l'IA**: The absolute source of truth is the `.html` files located in `public/books/l-odyss-e-de-l-ia-2-futurs-un-choix/`.
- **NO AUTOMATIC REGENERATION**: Under no circumstances should these HTML files be overwritten by automated scripts, conversion tools, or external sources (like PDF or Docx). 
- **MANUAL EDITS ONLY**: All additions, styling corrections, hook replacements, and cover inclusions must be edited **manually** file-by-file, matching the user's design choices (dropcaps, italic paragraphs, title layouts, custom styles).

### 2. General Workspace Guidelines
- **Non-Interactive First**: Always use non-interactive flags (`-y`, `--yes`, etc.) for any terminal initializations.
- **Workspace Cleanliness**: Keep the root clean. If temporary folders are needed, clean them up.

---

## CURRENT STATUS & RECENT CHANGES

### ✅ L'Odyssée de l'IA (IA Odyssey)
- **Hooks & Cover Illustrations**:
  - **Chapitre 1**: Added cover `chapitre-1-cover.webp` at the very beginning. Restored original title structures (`<h1>Partie I</h1>`, `<h2>Le grand point d'inflexion</h2>`).
  - **Chapitre 2**: Replaced the bullet points with the Hook `« Imaginez… Un avenir à mon sens très probable… »`. Placed cover `chapitre-2-cover.webp` underneath. Restored original titles (`<h1>Partie II</h1>`, `<h2>La Capitulation Silencieuse</h2>`, `<h2><em>La Dystopie High-Tech (2034)</em></h2>`).
  - **Chapitre 3**: Cover `chapitre-3-cover.webp` and Hook `« L'IA ne nous remplace pas. Elle nous rend à nous-mêmes. »` aligned.
  - **Chapitre 4**: Cover `chapitre-4-cover.webp` and Hook `« Ce n'est pas l'IA qui choisira. Ce sont nos actes d'aujourd'hui. »` aligned.
  - **Chapitre 5**: Cover `chapitre-5-cover.webp` and Hook `« Chaque génération a sa fenêtre. La nôtre s'appelle 2026. »` aligned.
- **Sync Files**: Updated `livre-complet.html` and `livre-imprimable.html` to reflect the updated Partie II hook.

### ✅ L'Odyssée de l'Énergie (Energy Odyssey)
- Imported and styled all 8 chapters in `public/books/l-odyss-e-de-l-energie/` using custom layout classes:
  - `.chapter-pullquote` for highlighted citation blocks.
  - `.chapter-divider` for elegant gradients instead of the raw `✦ ✦ ✦` dividers.
  - `.chapter-stats-table` for beautifully styled tables representing raw statistical data.
  - `.chapter-section-title` for inner section boundaries.
- **Cover Images**:
  - Chapters 1, 2, 3, 4, 6: Have their unique custom-generated Solarpunk illustration covers.
  - Chapters 5, 7, 8: Temporarily reuse existing covers due to generation quotas. To be updated once image generation quotas reset.

---

## NEXT STEPS
1. Double-check all manual file structures to verify no styling details are broken.
2. Update the cover illustrations for Chapters 5, 7, and 8 of the Energy Odyssey when the image generation quota is reset (around June 6th, 2026).
