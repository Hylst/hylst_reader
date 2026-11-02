// js/sanitize.js
// Assainissement des contenus importés (EPUB, HML, JSON).
// Les livres intégrés au dépôt restent considérés comme sûrs et ne passent pas par ici.
// Dépend de : vendor/purify.min.js (DOMPurify), chargé avant ce fichier.

(function () {
    'use strict';

    const FORBID_TAGS = [
        'script', 'style', 'iframe', 'object', 'embed', 'form', 'input',
        'button', 'textarea', 'select', 'option', 'link', 'meta', 'base',
        'noscript', 'template'
    ];

    const FORBID_ATTR = [
        'srcdoc', 'formaction', 'action', 'method', 'xlink:href'
    ];

    function sanitizeHtml(html) {
        if (typeof html !== 'string' || html.length === 0) return '';

        if (!window.DOMPurify || typeof window.DOMPurify.sanitize !== 'function') {
            console.error('[HylstSanitize] DOMPurify indisponible : contenu importé bloqué.');
            return '<p>Contenu importé bloqué : le module de sécurité DOMPurify n\'est pas chargé.</p>';
        }

        return window.DOMPurify.sanitize(html, {
            USE_PROFILES: { html: true },
            FORBID_TAGS: FORBID_TAGS,
            FORBID_ATTR: FORBID_ATTR,
            ALLOW_DATA_ATTR: false,
            ALLOW_ARIA_ATTR: true
        });
    }

    function escapeHtml(value) {
        return String(value == null ? '' : value)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function sanitizeBook(book) {
        if (!book || typeof book !== 'object') return book;

        const copy = Object.assign({}, book);

        if (typeof copy.introHtml === 'string') {
            copy.introHtml = sanitizeHtml(copy.introHtml);
        }

        if (Array.isArray(copy.chapters)) {
            copy.chapters = copy.chapters.map(function (chapter) {
                if (!chapter || typeof chapter !== 'object') return chapter;
                if (typeof chapter.html !== 'string') return chapter;
                return Object.assign({}, chapter, { html: sanitizeHtml(chapter.html) });
            });
        }

        return copy;
    }

    window.HylstSanitize = {
        sanitizeHtml: sanitizeHtml,
        sanitizeBook: sanitizeBook,
        escapeHtml: escapeHtml
    };
})();
