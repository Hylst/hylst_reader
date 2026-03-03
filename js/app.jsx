// js/app.jsx
import { getBooks, saveBook, deleteBook, getProgress, saveProgress, getSettings, saveSettings, getSignets, saveSignet, removeSignet } from '/js/db.js';
import { importBookFromDirectory } from '/js/importAPI.js';

const { useState, useEffect, useMemo, useRef, useCallback } = React;

// ── SVG Icon Components ─────────────────────────────────────────────────────
const Icon = {
    ArrowLeft: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 12H5M12 19l-7-7 7-7" />
        </svg>
    ),
    ArrowRight: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M5 12h14M12 5l7 7-7 7" />
        </svg>
    ),
    Upload: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /><polyline points="17 8 12 3 7 8" /><line x1="12" y1="3" x2="12" y2="15" />
        </svg>
    ),
    List: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="8" y1="6" x2="21" y2="6" /><line x1="8" y1="12" x2="21" y2="12" /><line x1="8" y1="18" x2="21" y2="18" /><line x1="3" y1="6" x2="3.01" y2="6" /><line x1="3" y1="12" x2="3.01" y2="12" /><line x1="3" y1="18" x2="3.01" y2="18" />
        </svg>
    ),
    Settings: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" />
        </svg>
    ),
    Bookmark: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
        </svg>
    ),
    BookmarkFilled: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
        </svg>
    ),
    Search: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="11" cy="11" r="8" /><line x1="21" y1="21" x2="16.65" y2="16.65" />
        </svg>
    ),
    Sun: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="5" /><line x1="12" y1="1" x2="12" y2="3" /><line x1="12" y1="21" x2="12" y2="23" /><line x1="4.22" y1="4.22" x2="5.64" y2="5.64" /><line x1="18.36" y1="18.36" x2="19.78" y2="19.78" /><line x1="1" y1="12" x2="3" y2="12" /><line x1="21" y1="12" x2="23" y2="12" /><line x1="4.22" y1="19.78" x2="5.64" y2="18.36" /><line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
        </svg>
    ),
    Moon: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
        </svg>
    ),
    Book: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" /><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
    ),
    X: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" />
        </svg>
    ),
    Eye: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" /><circle cx="12" cy="12" r="3" />
        </svg>
    ),
    Clock: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="10" /><polyline points="12 6 12 12 16 14" />
        </svg>
    ),
    ChevronUp: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="18 15 12 9 6 15" />
        </svg>
    ),
    ChevronDown: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="6 9 12 15 18 9" />
        </svg>
    ),
    Info: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" />
        </svg>
    ),
    Lock: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2" /><path d="M7 11V7a5 5 0 0 1 10 0v4" />
        </svg>
    ),
    Mail: () => (
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" /><polyline points="22,6 12,13 2,6" />
        </svg>
    ),
};

const FUTURE_BOOKS = [
    { id: 'f1', title: "L'Odyssée de l'Énergie", subtitle: "Le Carburant Invisible de l'IA", genre: 'Essai SF', cover: 'covers/cover_odyssee_energie.png' },
    { id: 'f2', title: "Les Chroniques d'Étheria", subtitle: "Roman d'Heroic Fantasy", genre: 'Fantasy', cover: 'covers/cover_etheria.png' },
    { id: 'f3', title: 'Scénarios et campagnes pour Nightprowler', subtitle: 'JDR MédFan', genre: 'JDR', cover: 'covers/cover_nightprowler.png' },
    { id: 'f4', title: 'Recueils de proses et poésies fantasques', subtitle: 'Littérature', genre: 'Poésie', cover: 'covers/cover_proses_poesies.png' },
    { id: 'f5', title: 'Considérations existentielles', subtitle: 'Réflexions philosophiques', genre: 'Philosophie', cover: 'covers/cover_existentiel.png' },
    { id: 'f6', title: "Quinte ou Les Harmoniques de l'âme", subtitle: 'Roman', genre: 'Roman', cover: 'covers/cover_quinte.png' },
    { id: 'f7', title: "L'Autre en moi", subtitle: 'Thriller psychologique', genre: 'Thriller', cover: 'covers/cover_autre_en_moi.png' },
    { id: 'f8', title: "L'Élu d'Astrakan", subtitle: "Livre dont vous êtes le héros · Fantasy", genre: 'LDVELH', cover: 'covers/cover_astrakan.png' },
    { id: 'f9', title: '12 Scénarios soirées enquêtes & murder', subtitle: 'Jeu de rôle soirée', genre: 'Jeu', cover: 'covers/cover_murder.png' },
    { id: 'f10', title: 'Approche de la Neurodiversité', subtitle: "Vision d'un non-professionnel", genre: 'Essai', cover: 'covers/cover_neuro.png' },
    { id: 'f11', title: 'Essentiels en Mathématiques', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_maths.png' },
    { id: 'f12', title: 'Essentiels en Physique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_physique.png' },
    { id: 'f12b', title: 'Essentiels en Optique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_optique.png' },
    { id: 'f13', title: 'Essentiels en Électronique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_electronique.png' },
    { id: 'f13b', title: 'Essentiels en Informatique', subtitle: 'Apprentissage', genre: 'Éducation', cover: 'covers/cover_informatique.png' },
    { id: 'f15', title: 'Algorithm for Love', subtitle: 'Recueil de nouvelles SF', genre: 'Nouvelles', cover: 'covers/cover_algorithm_love.png' },
    { id: 'f16', title: 'Chroniques de Godefroi', subtitle: 'Livre de règles · JDR Médiéval', genre: 'JDR', cover: 'covers/cover_godefroi.png' },
    { id: 'f17', title: "Chroniques d'une atrophie programmée", subtitle: 'Roman de Science-Fiction', genre: 'SF', cover: 'covers/cover_atrophie.png' },
    { id: 'f18', title: 'Nouvelles satiriques alsaciennes', subtitle: 'Humour & terroir alsacien', genre: 'Nouvelles', cover: 'covers/cover_nouvelles_alsaciennes.png' },
    { id: 'f19', title: "Solutions d'Automatisation par IA", subtitle: 'Guide pratique entreprise', genre: 'Guide', cover: 'covers/cover_automatisation_ia.png' },
    { id: 'f20', title: "Les Éclats du Corbeau", subtitle: "Livre dont vous êtes le héros · Mystère & Étrange", genre: 'LDVELH', cover: 'covers/cover_eclats_corbeau.png' },
];




// ── App Component ────────────────────────────────────────────────────────────
function App() {
    const [books, setBooks] = useState([]);
    const [currentView, setCurrentView] = useState('library');
    const [activeBookId, setActiveBookId] = useState(null);
    const [settings, setSettingsState] = useState({ theme: 'sepia', fontScale: 1.0, alignment: 'left', focusMode: false });
    const [lastReadSession, setLastReadSession] = useState(null);
    const [showAbout, setShowAbout] = useState(false);

    useEffect(() => {
        const loadData = async () => {
            const loader = document.querySelector('.initial-loader');
            if (loader) loader.style.display = 'none';

            const savedSettings = await getSettings();
            const merged = { theme: 'sepia', fontScale: 1.0, alignment: 'left', focusMode: false, ...savedSettings };
            setSettingsState(merged);

            let localBooks = [];
            try { localBooks = await getBooks(); } catch (e) { console.error(e); }

            try {
                const res = await window.fetch(`public/books.json?t=${Date.now()}`);
                if (res.ok) {
                    const publicBooks = await res.json();
                    const localIds = localBooks.map(b => b.id);
                    for (const pb of publicBooks) {
                        if (!localIds.includes(pb.id)) localBooks.push(pb);
                    }
                }
            } catch (e) { console.error('Could not fetch public/books.json', e); }

            setBooks(localBooks);

            // Find most recent session
            const allProg = await idb.get('hylst-progress') || {};
            let latest = null;
            let latestTime = 0;
            for (const [bid, p] of Object.entries(allProg)) {
                if (p.lastRead > latestTime) {
                    latestTime = p.lastRead;
                    const b = localBooks.find(x => x.id === bid);
                    if (b) latest = { ...p, bookId: bid, bookTitle: b.title };
                }
            }
            setLastReadSession(latest);
        };
        loadData();
    }, []);

    const setSettings = useCallback(async (newSettings) => {
        setSettingsState(newSettings);
        await saveSettings(newSettings);
    }, []);

    // Book CSS variable keys managed by the app
    const BOOK_VAR_KEYS = ['--book-bg', '--book-text', '--book-accent', '--book-accent-dark', '--book-surface', '--book-border', '--book-font-body', '--book-font-heading', '--book-font-title'];

    // Apply global theme + font settings
    // KEY FIX: When switching away from 'sepia', remove inline book vars so [data-theme] wins
    useEffect(() => {
        document.documentElement.setAttribute('data-theme', settings.theme);
        document.documentElement.style.setProperty('--font-size-multiplier', settings.fontScale);
        document.documentElement.style.setProperty('--text-alignment', settings.alignment);
        // Clear book-specific inline vars unless we are in sepia (the book's native palette)
        if (settings.theme !== 'sepia') {
            BOOK_VAR_KEYS.forEach(k => document.documentElement.style.removeProperty(k));
        }
    }, [settings]);

    const activeBook = useMemo(() => books.find(b => b.id === activeBookId), [books, activeBookId]);

    // Apply book-specific CSS variables (only in sepia/default mode)
    useEffect(() => {
        if (settings.theme !== 'sepia') return; // let the theme take over
        if (activeBook?.design?.variables) {
            for (const [k, v] of Object.entries(activeBook.design.variables)) {
                document.documentElement.style.setProperty(k, v);
            }
            const gf = activeBook.design?.fonts?.googleFonts;
            if (gf) {
                const id = 'book-google-fonts';
                let el = document.getElementById(id);
                if (!el) { el = document.createElement('link'); el.id = id; el.rel = 'stylesheet'; document.head.appendChild(el); }
                el.href = `https://fonts.googleapis.com/css2?${gf}&display=swap`;
            }
        } else {
            BOOK_VAR_KEYS.forEach(k => document.documentElement.style.removeProperty(k));
        }
    }, [activeBook, settings.theme]);

    const handleImport = async () => {
        if (!window.showDirectoryPicker) {
            alert("L'API File System Access n'est pas supportée par ce navigateur.");
            return;
        }
        try {
            const dirHandle = await window.showDirectoryPicker();
            const book = await importBookFromDirectory(dirHandle);
            await saveBook(book);
            setBooks(prev => {
                const idx = prev.findIndex(b => b.id === book.id);
                if (idx >= 0) { const n = [...prev]; n[idx] = book; return n; }
                return [...prev, book];
            });
        } catch (err) {
            if (err.name !== 'AbortError') alert("Erreur lors de l'import: " + err.message);
        }
    };

    const openBook = (id) => { setActiveBookId(id); setCurrentView('bookHome'); };
    const startReading = () => setCurrentView('reader');
    const resumeReading = (session) => {
        setActiveBookId(session.bookId);
        setCurrentView('reader');
    };
    const goBack = (to = 'library') => setCurrentView(to);

    return (
        <React.Fragment>
            {showAbout && <AboutModal onClose={() => setShowAbout(false)} />}
            {currentView === 'library' && (
                <LibraryView
                    books={books}
                    onImport={handleImport}
                    onOpenBook={openBook}
                    settings={settings}
                    onUpdateSettings={setSettings}
                    lastSession={lastReadSession}
                    onResume={resumeReading}
                    onShowAbout={() => setShowAbout(true)}
                />
            )}
            {currentView === 'bookHome' && activeBook && (
                <BookHomeView book={activeBook} onBack={() => goBack('library')} onStartReading={startReading} />
            )}
            {currentView === 'reader' && activeBook && (
                <ReaderView
                    book={activeBook}
                    onBack={() => goBack('bookHome')}
                    settings={settings}
                    onUpdateSettings={setSettings}
                />
            )}
        </React.Fragment>
    );
}

// ── About Modal ─────────────────────────────────────────────────────────────
function AboutModal({ onClose }) {
    return (
        <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && onClose()}>
            <div className="modal-content about-modal">
                <div className="modal-header">
                    <h3>Hylst Reader</h3>
                    <button className="btn btn-ghost btn-icon" onClick={onClose}><Icon.X /></button>
                </div>
                <div className="about-body">
                    <p className="about-tagline">Liseuse web elegante, hors-ligne, open source.</p>
                    <div className="about-section">
                        <h4>Fonctionnalites principales</h4>
                        <ul className="about-list">
                            <li>Bibliotheque multi-livres avec couvertures</li>
                            <li>Themes Sepia, Clair et Sombre</li>
                            <li>Signets et reprise de lecture automatique</li>
                            <li>Recherche plein texte dans tous les chapitres</li>
                            <li>PWA : installation et lecture 100% hors-ligne</li>
                            <li>Estimation du temps de lecture par chapitre</li>
                            <li>Slider de navigation et sauts rapides Haut/Bas</li>
                            <li>Import de dossiers (File System Access API)</li>
                        </ul>
                    </div>
                    <div className="about-section">
                        <h4>Mode d'emploi rapide</h4>
                        <ol className="about-list">
                            <li>Les livres integres s'affichent automatiquement.</li>
                            <li>Cliquez <strong>Importer un dossier</strong> pour ajouter vos propres oeuvres.</li>
                            <li>En mode lecture, cliquez pour afficher/masquer la barre d'outils.</li>
                        </ol>
                    </div>
                    <div className="about-creator">
                        <div className="creator-avatar">G</div>
                        <div>
                            <div><strong>Geoffroy Streit</strong> <em>alias Hylst</em></div>
                            <div className="creator-role">Artiste &#233;clectique &middot; D&#233;veloppeur bancal &middot; &#201;crivain &#224; ses heures</div>
                            <a href="mailto:geoffroy.streit@gmail.com" className="creator-mail">
                                <Icon.Mail /> geoffroy.streit@gmail.com
                            </a>
                        </div>
                    </div>
                    <p className="about-wip">Application en cours de developpement actif &mdash; nombreuses evolutions a venir !</p>
                </div>
            </div>
        </div>
    );
}

// ── Library View ─────────────────────────────────────────────────────────────
function LibraryView({ books, onImport, onOpenBook, settings, onUpdateSettings, lastSession, onResume, onShowAbout }) {
    return (
        <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100%' }} className="view-enter">
            <header className="app-header">
                <span className="app-title">Hylst Reader</span>
                <div className="header-actions">
                    <button className="btn btn-ghost btn-icon" title="A propos" onClick={onShowAbout}>
                        <Icon.Info />
                    </button>
                    <button className="btn btn-ghost btn-icon" title="Theme"
                        onClick={() => {
                            const themes = ['sepia', 'light', 'dark'];
                            const next = themes[(themes.indexOf(settings.theme) + 1) % themes.length];
                            onUpdateSettings({ ...settings, theme: next });
                        }}
                    >
                        {settings.theme === 'dark' ? <Icon.Sun /> : settings.theme === 'light' ? <Icon.Moon /> : <Icon.Book />}
                    </button>
                    <button className="btn btn-primary" onClick={onImport}>
                        <Icon.Upload /> Importer un dossier
                    </button>
                </div>
            </header>
            <main className="library-container">
                {lastSession && (
                    <div className="resume-banner">
                        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                            <Icon.Book />
                            <span>Continuer : <strong>{lastSession.bookTitle}</strong> &mdash; Chap. {lastSession.chapterIndex + 1}</span>
                        </div>
                        <button className="resume-btn" onClick={() => onResume(lastSession)}>Reprendre</button>
                    </div>
                )}

                <div className="library-section-label">Ma Bibliotheque</div>
                {books.length === 0 ? (
                    <div className="empty-state">
                        <h2>Votre bibliotheque est vide</h2>
                        <p>Importez un dossier contenant un livre structure pour commencer a lire.</p>
                        <div className="import-zone" onClick={onImport}>
                            <Icon.Upload />
                            <p style={{ marginTop: '0.75rem', fontWeight: 500 }}>Cliquez pour importer un dossier</p>
                        </div>
                    </div>
                ) : (
                    <div className="library-grid">
                        {books.map((book, i) => (
                            <BookCard key={book.id} book={book} onClick={() => onOpenBook(book.id)} delay={i * 60} />
                        ))}
                    </div>
                )}

                <div className="library-section-label future-label">
                    A venir &mdash; Contenus en preparation <span className="wip-badge">En cours</span>
                </div>
                <div className="future-intro">
                    <p>De mes anciens blogs et sites webs, des tiroirs num&#233;riques encombr&#233;s qui n&#8217;ont re&#231;u d&#8217;autres visites que les miennes, j&#8217;aurai mati&#232;re &#224; r&#233;unir bon nombre de mes &#233;crits pass&#233;s en ce lieu, parfois inachev&#233;s ou &#224; revoir, rang&#233;s dans cette biblioth&#232;que num&#233;rique que je travaille &#224; concevoir pour y pr&#233;senter, ouverts &#224; la consultation libre, mes anciennes nouvelles, r&#233;cits d&#8217;aventures HF et SF, livres dont vous &#234;tes le h&#233;ros, sc&#233;narios et campagnes de jeux de r&#244;les, histoires fantasques, r&#233;flexions existentielles, recueils de proses et po&#233;sies, analyses pseudo-scientifiques ou plus s&#233;rieuses, recherche de sens et v&#233;rit&#233;, guides p&#233;dagogiques, frustrastions &amp; passions, divagations &amp; claivoyances, ... issus des m&#233;andres de mon esprit bancal et arborescent au fil des ann&#233;es.</p>
                    <p>Avec le recul &amp; l&#8217;exp&#233;rience, j&#8217;aimerais reprendre bon nombre d&#8217;entre eux pour les am&#233;liorer, corriger ou compl&#233;ter avant de les partager, mais en aurais-je la motivation continue&nbsp;? En prendrai-je le temps&nbsp;? Ne finirais-je pas encore une fois par les laisser choir au fond de mes disques dans l&#8217;obscurit&#233;, si imparfaits soient-ils&nbsp;?</p>
                </div>
                <div className="library-grid">
                    {FUTURE_BOOKS.map((fb, i) => (
                        <FutureBookCard key={fb.id} book={fb} delay={i * 40} />
                    ))}
                </div>
            </main>
            <footer className="app-footer">
                <div className="footer-content">
                    <div className="footer-brand">
                        <span className="app-title" style={{ fontSize: '1.1rem' }}>Hylst Reader</span>
                        <span className="footer-wip">En cours de developpement</span>
                    </div>
                    <div className="footer-creator">
                        Cree par <strong>Geoffroy Streit</strong> alias <em>Hylst</em>
                        &nbsp;&middot;&nbsp; Artiste &#233;clectique, developpeur bancal, &#233;crivain &#224; ses heures
                        &nbsp;&middot;&nbsp;
                        <a href="mailto:geoffroy.streit@gmail.com" className="footer-mail">
                            <Icon.Mail /> geoffroy.streit@gmail.com
                        </a>
                    </div>
                </div>
            </footer>
        </div>
    );
}

// ── Future Book Card ─────────────────────────────────────────────────────────────
function FutureBookCard({ book, delay = 0 }) {
    return (
        <div className="book-card future-card" style={{ animationDelay: `${delay}ms` }} title="Bientot disponible" role="img">
            <div className="book-cover">
                {book.cover
                    ? <img src={`public/${book.cover}`} alt={book.title} loading="lazy" />
                    : <div className="future-cover-placeholder"><Icon.Lock /><span>{book.genre}</span></div>
                }
                <div className="future-badge">Bientot</div>
            </div>
            <div className="book-info">
                <div className="book-title">{book.title}</div>
                <div className="book-author">{book.subtitle}</div>
                <div className="book-genre-tag">{book.genre}</div>
            </div>
        </div>
    );
}

// ── Book Card ─────────────────────────────────────────────────────────────────
function BookCard({ book, onClick, delay = 0 }) {
    const [coverUrl, setCoverUrl] = useState(null);
    const [progress, setProgress] = useState(null);

    useEffect(() => {
        if (book.coverBlob) {
            const url = URL.createObjectURL(book.coverBlob);
            setCoverUrl(url);
            return () => URL.revokeObjectURL(url);
        } else if (book.coverPath) {
            setCoverUrl(`public/${book.coverPath}?t=${Date.now()}`);
        }
    }, [book.coverBlob, book.coverPath]);

    useEffect(() => {
        getProgress(book.id).then(p => { if (p) setProgress(p.scrollRatio || 0); });
    }, [book.id]);

    return (
        <div className="book-card" style={{ animationDelay: `${delay}ms` }} onClick={onClick} role="button" tabIndex={0}
            onKeyDown={e => e.key === 'Enter' && onClick()}>
            <div className="book-cover">
                {coverUrl
                    ? <img src={coverUrl} alt={book.title} loading="lazy" />
                    : <span style={{ opacity: 0.4, fontSize: '0.8rem' }}>Pas de couverture</span>
                }
            </div>
            <div className="book-info">
                <div className="book-title">{book.title}</div>
                <div className="book-author">{book.author}</div>
            </div>
            {progress !== null && progress > 0 && (
                <div className="book-progress-bar" title={`${Math.round(progress * 100)}% lu`}>
                    <div className="book-progress-fill" style={{ width: `${progress * 100}%` }} />
                </div>
            )}
        </div>
    );
}

// ── Book Home View ─────────────────────────────────────────────────────────────
function BookHomeView({ book, onBack, onStartReading }) {
    const [coverUrl, setCoverUrl] = useState(null);
    const [introHtml, setIntroHtml] = useState('');

    useEffect(() => {
        if (book.coverBlob) {
            const url = URL.createObjectURL(book.coverBlob);
            setCoverUrl(url);
            return () => URL.revokeObjectURL(url);
        } else if (book.coverPath) {
            setCoverUrl(`public/${book.coverPath}?t=${Date.now()}`);
        }
    }, [book.coverBlob, book.coverPath]);

    useEffect(() => {
        if (!book.introHtml && book.introPath) {
            window.fetch(`public/${book.introPath}?t=${Date.now()}`)
                .then(r => r.text())
                .then(html => setIntroHtml(html))
                .catch(() => setIntroHtml('<p>Introduction non disponible.</p>'));
        } else {
            setIntroHtml(book.introHtml || '');
        }
    }, [book.id, book.introHtml, book.introPath]);

    return (
        <div className="book-home view-enter">
            <div className="book-home-header">
                <button className="btn btn-ghost" onClick={onBack}><Icon.ArrowLeft /> Bibliothèque</button>
            </div>
            <div className="book-home-content">
                <div className="book-home-cover">
                    {coverUrl && <img src={coverUrl} alt={`Couverture – ${book.title}`} />}
                </div>
                <div className="book-home-meta">
                    <h1 className="book-home-title">{book.title}</h1>
                    <p className="book-home-author">{book.author} {book.year ? `· ${book.year}` : ''}</p>
                    <button className="btn btn-primary" style={{ padding: '0.85rem 2rem', fontSize: '1rem', marginBottom: '2rem' }} onClick={onStartReading}>
                        Commencer la lecture <Icon.ArrowRight />
                    </button>
                    <div className="book-home-intro" dangerouslySetInnerHTML={{ __html: introHtml }} />
                </div>
            </div>
        </div>
    );
}

// ── Reader View ────────────────────────────────────────────────────────────────
function ReaderView({ book, onBack, settings, onUpdateSettings }) {
    const [currentChapterIdx, setCurrentChapterIdx] = useState(0);
    const [chapterHtml, setChapterHtml] = useState('');
    const [showUI, setShowUI] = useState(true);
    const [showSidebar, setShowSidebar] = useState(false);
    const [showSettings, setShowSettings] = useState(false);
    const [showSearch, setShowSearch] = useState(false);
    const [searchQuery, setSearchQuery] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [isSearching, setIsSearching] = useState(false);
    const [signets, setSignets] = useState([]);
    const [scrollProgress, setScrollProgress] = useState(0);

    const containerRef = useRef(null);
    const touchStartRef = useRef(null);
    const uiTimeoutRef = useRef(null);
    const chapter = book.chapters?.[currentChapterIdx];

    // Load signets
    useEffect(() => {
        getSignets(book.id).then(s => setSignets(s || []));
    }, [book.id]);

    // Restore progress
    useEffect(() => {
        getProgress(book.id).then(prog => {
            if (prog) setCurrentChapterIdx(prog.chapterIndex || 0);
        });
    }, [book.id]);

    // Load chapter HTML
    useEffect(() => {
        if (!chapter) return;
        if (chapter.html) {
            setChapterHtml(chapter.html);
        } else if (chapter.path) {
            setChapterHtml('');
            window.fetch(`public/${chapter.path}?t=${Date.now()}`)
                .then(r => r.text())
                .then(html => setChapterHtml(html))
                .catch(() => setChapterHtml('<p>Erreur lors du chargement.</p>'));
        }
        if (containerRef.current) containerRef.current.scrollTop = 0;
        setScrollProgress(0);

        // Auto-restore scroll position after HTML is rendered
        const timer = setTimeout(async () => {
            const prog = await getProgress(book.id);
            if (prog && prog.chapterIndex === currentChapterIdx && prog.scrollRatio > 0 && containerRef.current) {
                const { scrollHeight, clientHeight } = containerRef.current;
                containerRef.current.scrollTop = prog.scrollRatio * (scrollHeight - clientHeight);
                setScrollProgress(prog.scrollRatio);
            }
        }, 100);
        return () => clearTimeout(timer);
    }, [chapter]);

    // Auto show UI on chapter change, then hide it
    useEffect(() => {
        setShowUI(true);
        clearTimeout(uiTimeoutRef.current);
        uiTimeoutRef.current = setTimeout(() => setShowUI(false), 3000);
        return () => clearTimeout(uiTimeoutRef.current);
    }, [currentChapterIdx]);

    const handleContainerClick = () => {
        setShowUI(v => {
            const next = !v;
            if (next) {
                clearTimeout(uiTimeoutRef.current);
                uiTimeoutRef.current = setTimeout(() => setShowUI(false), 3000);
            }
            return next;
        });
    };

    const handleScroll = useCallback(() => {
        if (!containerRef.current) return;
        const { scrollTop, scrollHeight, clientHeight } = containerRef.current;
        const ratio = scrollTop / Math.max(scrollHeight - clientHeight, 1);
        setScrollProgress(ratio);
        saveProgress(book.id, currentChapterIdx, ratio);
    }, [book.id, currentChapterIdx]);

    // Touch swipe
    const handleTouchStart = (e) => { touchStartRef.current = e.changedTouches[0].clientX; };
    const handleTouchEnd = (e) => {
        if (touchStartRef.current === null) return;
        const dx = e.changedTouches[0].clientX - touchStartRef.current;
        touchStartRef.current = null;
        if (Math.abs(dx) < 50) return;
        if (dx < 0) nextChapter();
        else prevChapter();
    };

    const nextChapter = () => {
        if (currentChapterIdx < book.chapters.length - 1) setCurrentChapterIdx(i => i + 1);
    };
    const prevChapter = () => {
        if (currentChapterIdx > 0) setCurrentChapterIdx(i => i - 1);
    };

    const readingTime = useMemo(() => {
        if (!chapterHtml) return '';
        const text = chapterHtml.replace(/<[^>]+>/g, ' ');
        const words = text.split(/\s+/).filter(w => w.length > 0).length;
        const mins = Math.ceil(words / 220);
        return mins > 0 ? `${mins} min de lecture` : "Moins d'une minute";
    }, [chapterHtml]);

    const handleSliderClick = (e) => {
        if (!containerRef.current) return;
        const rect = e.currentTarget.getBoundingClientRect();
        const y = e.clientY - rect.top;
        const ratio = Math.max(0, Math.min(1, y / rect.height));
        const { scrollHeight, clientHeight } = containerRef.current;
        containerRef.current.scrollTop = ratio * (scrollHeight - clientHeight);
    };

    const scrollTo = (target) => {
        if (!containerRef.current) return;
        if (target === 'top') containerRef.current.scrollTo({ top: 0, behavior: 'smooth' });
        else if (target === 'bottom') containerRef.current.scrollTo({ top: containerRef.current.scrollHeight, behavior: 'smooth' });
    };

    const isBookmarked = signets.some(s => s.chapterIdx === currentChapterIdx);

    const toggleBookmark = async () => {
        if (isBookmarked) {
            const updated = signets.filter(s => s.chapterIdx !== currentChapterIdx);
            await removeSignet(book.id, currentChapterIdx);
            setSignets(updated);
        } else {
            const s = { chapterIdx: currentChapterIdx, chapterTitle: chapter?.title || `Chapitre ${currentChapterIdx + 1}`, addedAt: Date.now() };
            await saveSignet(book.id, s);
            setSignets(prev => [...prev, s]);
        }
    };

    const handleSearch = async () => {
        if (!searchQuery.trim()) return;
        setIsSearching(true);
        const results = [];
        for (let i = 0; i < book.chapters.length; i++) {
            let content = book.chapters[i].html;
            if (!content && book.chapters[i].path) {
                try {
                    const r = await window.fetch(`public/${book.chapters[i].path}?t=${Date.now()}`);
                    content = await r.text();
                } catch { continue; }
            }
            if (!content) continue;
            const plain = content.replace(/<[^>]+>/g, ' ');
            const q = searchQuery.toLowerCase();
            let idx = plain.toLowerCase().indexOf(q);
            while (idx !== -1 && results.length < 15) {
                const snippet = plain.substring(Math.max(0, idx - 60), idx + 100);
                results.push({ chapterIdx: i, chapterTitle: book.chapters[i].title, snippet, matchIdx: idx });
                idx = plain.toLowerCase().indexOf(q, idx + 1);
            }
        }
        setSearchResults(results);
        setIsSearching(false);
    };

    const containerClass = `reader-container${showUI ? ' show-ui' : ''}${settings.focusMode ? ' focus-mode' : ''}`;

    return (
        <div className="reader-wrapper view-enter">
            {/* Progress bar */}
            <div className="reader-progress-bar" style={{ width: `${scrollProgress * 100}%` }} />

            {/* Sidebar */}
            <div className={`sidebar-overlay${showSidebar ? ' open' : ''}`} onClick={() => setShowSidebar(false)} />
            <aside className={`sidebar${showSidebar ? ' open' : ''}`}>
                <div className="sidebar-header">
                    <h3>{book.title}</h3>
                    <button className="btn btn-ghost btn-icon" onClick={() => setShowSidebar(false)}><Icon.X /></button>
                </div>
                <div className="sidebar-body">
                    <div className="toc-section-label">Chapitres</div>
                    {book.chapters.map((ch, i) => (
                        <div key={ch.id} className={`toc-item${i === currentChapterIdx ? ' active' : ''}`}
                            onClick={() => { setCurrentChapterIdx(i); setShowSidebar(false); }}>
                            <span className="toc-num">{i + 1}</span>
                            <span>{ch.title}</span>
                        </div>
                    ))}
                    {signets.length > 0 && (
                        <>
                            <div className="toc-section-label" style={{ marginTop: '1rem' }}>Signets</div>
                            {signets.map(s => (
                                <div key={s.chapterIdx} className="toc-item"
                                    onClick={() => { setCurrentChapterIdx(s.chapterIdx); setShowSidebar(false); }}>
                                    <Icon.BookmarkFilled />
                                    <span>{s.chapterTitle}</span>
                                </div>
                            ))}
                        </>
                    )}
                </div>
            </aside>

            {/* Settings Modal */}
            {showSettings && (
                <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && setShowSettings(false)}>
                    <div className="modal-content">
                        <div className="modal-header">
                            <h3>Paramètres de lecture</h3>
                            <button className="btn btn-ghost btn-icon" onClick={() => setShowSettings(false)}><Icon.X /></button>
                        </div>
                        <div className="setting-group">
                            <label>Thème</label>
                            <div className="setting-options">
                                {['sepia', 'light', 'dark'].map(t => (
                                    <button key={t} className={`btn${settings.theme === t ? ' btn-primary' : ''}`}
                                        onClick={() => onUpdateSettings({ ...settings, theme: t })}>
                                        {t === 'sepia' ? 'Sépia' : t === 'light' ? 'Clair' : 'Sombre'}
                                    </button>
                                ))}
                            </div>
                        </div>
                        <div className="setting-group">
                            <label>Taille du texte</label>
                            <div className="setting-options">
                                <button className="btn" onClick={() => onUpdateSettings({ ...settings, fontScale: Math.max(0.7, settings.fontScale - 0.1) })}>A−</button>
                                <span>{Math.round(settings.fontScale * 100)}%</span>
                                <button className="btn" onClick={() => onUpdateSettings({ ...settings, fontScale: Math.min(1.7, settings.fontScale + 0.1) })}>A+</button>
                            </div>
                        </div>
                        <div className="setting-group">
                            <label>Alignement</label>
                            <div className="setting-options">
                                {['left', 'justify'].map(a => (
                                    <button key={a} className={`btn${settings.alignment === a ? ' btn-primary' : ''}`}
                                        onClick={() => onUpdateSettings({ ...settings, alignment: a })}>
                                        {a === 'left' ? 'Gauche' : 'Justifié'}
                                    </button>
                                ))}
                            </div>
                        </div>
                        <div className="setting-group">
                            <label>Mode Concentration</label>
                            <div className="setting-options">
                                <button className={`btn${settings.focusMode ? ' btn-primary' : ''}`}
                                    onClick={() => onUpdateSettings({ ...settings, focusMode: !settings.focusMode })}>
                                    <Icon.Eye /> {settings.focusMode ? 'Actif' : 'Inactif'}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Search Modal */}
            {showSearch && (
                <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && setShowSearch(false)}>
                    <div className="modal-content">
                        <div className="modal-header">
                            <h3>Recherche</h3>
                            <button className="btn btn-ghost btn-icon" onClick={() => setShowSearch(false)}><Icon.X /></button>
                        </div>
                        <div className="search-input-wrapper">
                            <Icon.Search />
                            <input
                                type="text"
                                placeholder="Rechercher dans le livre…"
                                value={searchQuery}
                                onChange={e => setSearchQuery(e.target.value)}
                                onKeyDown={e => e.key === 'Enter' && handleSearch()}
                                autoFocus
                            />
                            <button className="btn btn-primary" onClick={handleSearch} disabled={isSearching}>
                                {isSearching ? '…' : 'OK'}
                            </button>
                        </div>
                        <div style={{ maxHeight: '320px', overflowY: 'auto' }}>
                            {searchResults.map((r, i) => (
                                <div key={i} className="search-result-item" onClick={() => { setCurrentChapterIdx(r.chapterIdx); setShowSearch(false); }}>
                                    <div className="search-result-chapter">{r.chapterTitle}</div>
                                    <div>…{r.snippet.replace(new RegExp(searchQuery, 'gi'), m => `<strong>${m}</strong>`).replace(/<[^>]+>/g, s => s)}{/*simplified*/}…</div>
                                </div>
                            ))}
                            {searchResults.length === 0 && searchQuery && !isSearching && (
                                <p style={{ padding: '1rem', opacity: 0.5, textAlign: 'center' }}>Aucun résultat</p>
                            )}
                        </div>
                    </div>
                </div>
            )}

            {/* Scroll Slider */}
            <div className="reader-slider" onClick={handleSliderClick}>
                <div className="reader-slider-handle" style={{ top: `${scrollProgress * 100}%`, height: '20px' }} />
            </div>

            {/* Jump-to buttons */}
            <div className="jump-controls">
                <button className="jump-btn" onClick={() => scrollTo('top')} title="Haut de page"><Icon.ChevronUp /></button>
                <button className="jump-btn" onClick={() => scrollTo('bottom')} title="Bas de page"><Icon.ChevronDown /></button>
            </div>

            {/* Main reader area */}
            <div
                ref={containerRef}
                className={containerClass}
                onClick={handleContainerClick}
                onScroll={handleScroll}
                onTouchStart={handleTouchStart}
                onTouchEnd={handleTouchEnd}
            >
                {/* Toolbar */}
                <div className="reader-toolbar">
                    <button className="btn btn-icon" onClick={e => { e.stopPropagation(); onBack(); }} title="Retour">
                        <Icon.ArrowLeft />
                    </button>
                    <span className="reader-toolbar-center">{chapter?.title || book.title}</span>
                    <div className="reader-toolbar-actions">
                        <button className="btn btn-icon" title={isBookmarked ? 'Retirer le signet' : 'Ajouter un signet'}
                            onClick={e => { e.stopPropagation(); toggleBookmark(); }}>
                            {isBookmarked ? <Icon.BookmarkFilled /> : <Icon.Bookmark />}
                        </button>
                        <button className="btn btn-icon" title="Rechercher" onClick={e => { e.stopPropagation(); setShowSearch(true); }}>
                            <Icon.Search />
                        </button>
                        <button className="btn btn-icon" title="Table des matières" onClick={e => { e.stopPropagation(); setShowSidebar(true); }}>
                            <Icon.List />
                        </button>
                        <button className="btn btn-icon" title="Paramètres" onClick={e => { e.stopPropagation(); setShowSettings(true); }}>
                            <Icon.Settings />
                        </button>
                    </div>
                </div>

                {/* Content */}
                <article className="reader-content">
                    {readingTime && (
                        <span className="reading-time-badge"><Icon.Clock /> {readingTime}</span>
                    )}
                    {chapterHtml
                        ? <div dangerouslySetInnerHTML={{ __html: chapterHtml }} />
                        : <div style={{ textAlign: 'center', padding: '4rem 0', opacity: 0.4 }}>
                            <div className="spinner" style={{ margin: '0 auto' }} />
                        </div>
                    }
                </article>

                {/* Bottom nav */}
                <div className="chapter-nav">
                    <button className="nav-btn" onClick={e => { e.stopPropagation(); prevChapter(); }}
                        disabled={currentChapterIdx === 0}>
                        <div className="icon-circle"><Icon.ArrowLeft /></div>
                        <span>Précédent</span>
                    </button>
                    <span className="chapter-counter">{currentChapterIdx + 1} / {book.chapters.length}</span>
                    <button className="nav-btn" onClick={e => { e.stopPropagation(); nextChapter(); }}
                        disabled={currentChapterIdx === book.chapters.length - 1}>
                        <span>Suivant</span>
                        <div className="icon-circle"><Icon.ArrowRight /></div>
                    </button>
                </div>
            </div>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
