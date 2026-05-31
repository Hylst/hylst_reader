// js/importAPI.js
// Script to handle parsing pure folders using File System Access API

(function() {
    async function importBookFromDirectory(dirHandle) {
        try {
            let config = null;
            let coverBlob = null;
            let introHtml = "";
            let chapters = [];

            // Read config.json
            try {
                const configFileHandle = await dirHandle.getFileHandle('config.json');
                const file = await configFileHandle.getFile();
                const text = await file.text();
                config = JSON.parse(text);
            } catch (e) {
                throw new Error("Le fichier config.json est manquant ou invalide.");
            }

            // Read cover (jpg or png)
            try {
                const coverHandle = await dirHandle.getFileHandle('cover.jpg').catch(() => dirHandle.getFileHandle('cover.png'));
                const file = await coverHandle.getFile();
                coverBlob = file;
            } catch (e) {
                console.warn("Cover image not found");
            }

            // Read intro
            try {
                const introHandle = await dirHandle.getFileHandle('intro.txt').catch(() => dirHandle.getFileHandle('intro.html'));
                const file = await introHandle.getFile();
                const text = await file.text();
                if (file.name.endsWith('.txt')) {
                    introHtml = text.split('\n').map(p => p.trim()).filter(p => p.length > 0).map(p => `<p>${p}</p>`).join('');
                } else {
                    introHtml = text;
                }
            } catch (e) {
                console.warn("Intro file not found");
            }

            // Read Chapters
            const chaptersDirHandle = await dirHandle.getDirectoryHandle('chapitres');
            for await (const entry of chaptersDirHandle.values()) {
                if (entry.kind === 'file' && (entry.name.endsWith('.txt') || entry.name.endsWith('.html'))) {
                    const file = await entry.getFile();
                    const text = await file.text();
                    let html = text;

                    if (entry.name.endsWith('.txt')) {
                        html = text.split('\n')
                            .map(p => p.trim())
                            .filter(p => p.length > 0)
                            .map(p => `<p>${p}</p>`)
                            .join('');
                    }

                    let title = entry.name.replace(/\.[^/.]+$/, "");
                    const match = title.match(/^\d+-(.*)$/);
                    if (match) {
                        title = match[1].replace(/-/g, " ");
                        title = title.charAt(0).toUpperCase() + title.slice(1);
                    }

                    chapters.push({
                        id: entry.name,
                        title: title,
                        html: html,
                        originalName: entry.name
                    });
                }
            }

            chapters.sort((a, b) => a.originalName.localeCompare(b.originalName));

            const bookId = config.title.toLowerCase().replace(/[^a-z0-9]+/g, '-') + '-' + Date.now();

            return {
                id: bookId,
                title: config.title || "Titre inconnu",
                author: config.author || "Auteur inconnu",
                year: config.year,
                language: config.language || "fr",
                design: config.design || {},
                coverBlob: coverBlob,
                introHtml: introHtml,
                chapters: chapters,
                isImported: true
            };

        } catch (err) {
            console.error("Error importing directory", err);
            throw err;
        }
    }

    window.HylstImport = { importBookFromDirectory };
})();
