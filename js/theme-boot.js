// Thème appliqué avant le premier rendu : sombre par défaut, choix mémorisé respecté.
(function () {
    var THEME_COLORS = { sepia: '#faf4e8', light: '#fafaf8', dark: '#0f0e0c' };
    var theme = 'dark';
    try {
        var saved = JSON.parse(localStorage.getItem('hylst_settings') || 'null');
        if (saved && Object.prototype.hasOwnProperty.call(THEME_COLORS, saved.theme)) {
            theme = saved.theme;
        }
    } catch (e) {
        /* Stockage indisponible : on garde le mode sombre. */
    }
    document.documentElement.setAttribute('data-theme', theme);
    var meta = document.getElementById('theme-color-meta');
    if (meta) meta.setAttribute('content', THEME_COLORS[theme]);
})();
