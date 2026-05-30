// js/app.jsx
import { getBooks, saveBook, getSettings, saveSettings, getSignetsAll } from './db.js';
import { importBookFromDirectory } from './importAPI.js';
import { Icon } from './components/Icon.jsx';
import { Ambience, normalizeBackgroundAnimations } from './components/Ambience.jsx';
import { AboutModal } from './components/AboutModal.jsx';
import { GlobalSettingsModal } from './components/GlobalSettingsModal.jsx';
import { MusicPlayerModal } from './components/MusicPlayerModal.jsx';
import { LibraryView } from './components/LibraryView.jsx';
import { BookHomeView } from './components/BookHomeView.jsx';
import { ReaderView } from './components/ReaderView.jsx';

const { useState, useEffect, useMemo, useRef, useCallback } = React;

const THEME_KEYS = ['sepia', 'light', 'dark'];
const DEFAULT_BACKGROUND_ANIMATIONS = { sepia: true, light: true, dark: true };
const DEFAULT_SETTINGS = {
    theme: 'dark',
    fontScale: 1.0,
    alignment: 'left',
    focusMode: false,
    contentWidth: 'medium',
    showReadingTime: true,
    showProgressPercent: true,
    backgroundAnimations: DEFAULT_BACKGROUND_ANIMATIONS
};

// Book CSS variable keys managed by the app
const BOOK_VAR_KEYS = [
    '--book-bg',
    '--book-text',
    '--book-accent',
    '--book-accent-dark',
    '--book-surface',
    '--book-border',
    '--book-font-body',
    '--book-font-heading',
    '--book-font-title'
];

function App() {
    const [books, setBooks] = useState([]);
    const [currentView, setCurrentView] = useState('library');
    const [activeBookId, setActiveBookId] = useState(null);
    const [settings, setSettingsState] = useState(() => {
        try {
            const saved = localStorage.getItem('hylst_settings');
            if (saved) {
                return { ...DEFAULT_SETTINGS, ...JSON.parse(saved) };
            }
        } catch (e) {
            console.error("Failed to parse settings from localStorage", e);
        }
        return DEFAULT_SETTINGS;
    });

    useEffect(() => {
        localStorage.setItem('hylst_settings', JSON.stringify(settings));
    }, [settings]);

    const [lastReadSession, setLastReadSession] = useState(null);
    const [showAbout, setShowAbout] = useState(false);
    const [showMusic, setShowMusic] = useState(false);
    const [showSettings, setShowSettings] = useState(false);

    // ── Global Audio State ──────────────────────────────────────────────────
    const audioRef = useRef(new Audio());
    const [currentTrack, setCurrentTrack] = useState(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const [isLoop, setIsLoop] = useState(false);
    const [isFullscreen, setIsFullscreen] = useState(false);

    const toggleFullscreen = useCallback(() => {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().then(() => setIsFullscreen(true)).catch(err => {
                console.error(`Error attempting to enable full-screen mode: ${err.message}`);
            });
        } else {
            document.exitFullscreen().then(() => setIsFullscreen(false));
        }
    }, []);

    useEffect(() => {
        const handleFsChange = () => setIsFullscreen(!!document.fullscreenElement);
        document.addEventListener('fullscreenchange', handleFsChange);
        return () => document.removeEventListener('fullscreenchange', handleFsChange);
    }, []);

    useEffect(() => {
        const audio = audioRef.current;
        audio.loop = isLoop;
    }, [isLoop]);

    useEffect(() => {
        const audio = audioRef.current;
        const handleError = () => {
            setIsPlaying(false);
            setCurrentTrack(null);
        };
        audio.addEventListener('error', handleError);
        return () => audio.removeEventListener('error', handleError);
    }, []);

    useEffect(() => {
        const audio = audioRef.current;
        const handleEnded = () => { if (!isLoop) setIsPlaying(false); };
        audio.addEventListener('ended', handleEnded);
        return () => audio.removeEventListener('ended', handleEnded);
    }, [isLoop]);

    // Keep audio alive through orientation change / tab visibility change
    useEffect(() => {
        let wasPlayingBeforeHide = false;
        const handleVisibility = () => {
            if (document.hidden) {
                wasPlayingBeforeHide = isPlaying;
            } else {
                if (wasPlayingBeforeHide && currentTrack && audioRef.current) {
                    audioRef.current.play().catch(() => { });
                    setIsPlaying(true);
                }
            }
        };
        document.addEventListener('visibilitychange', handleVisibility);
        return () => document.removeEventListener('visibilitychange', handleVisibility);
    }, [isPlaying, currentTrack]);

    const playTrack = useCallback((track) => {
        if (currentTrack?.id === track.id) {
            if (isPlaying) { audioRef.current.pause(); setIsPlaying(false); }
            else { audioRef.current.play(); setIsPlaying(true); }
            return;
        }
        audioRef.current.src = track.src;
        setCurrentTrack(track);
        audioRef.current.play().then(() => setIsPlaying(true)).catch(() => setIsPlaying(false));
    }, [currentTrack, isPlaying]);

    const togglePlay = useCallback(() => {
        if (!currentTrack) return;
        if (isPlaying) { audioRef.current.pause(); setIsPlaying(false); }
        else {
            audioRef.current.play().then(() => setIsPlaying(true)).catch(() => setIsPlaying(false));
        }
    }, [currentTrack, isPlaying]);

    const stopPlay = useCallback(() => {
        audioRef.current.pause();
        audioRef.current.currentTime = 0;
        setIsPlaying(false);
        setCurrentTrack(null);
    }, []);

    const toggleLoop = useCallback(() => setIsLoop(v => !v), []);

    useEffect(() => {
        const loadData = async () => {
            const loader = document.querySelector('.initial-loader');
            if (loader) loader.style.display = 'none';

            const savedSettings = await getSettings();
            const merged = {
                ...DEFAULT_SETTINGS,
                ...savedSettings,
                theme: THEME_KEYS.includes(savedSettings?.theme) ? savedSettings.theme : 'sepia',
                backgroundAnimations: normalizeBackgroundAnimations(savedSettings?.backgroundAnimations)
            };
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

            // Find most recent session from SIGNETS
            const allSignets = await getSignetsAll();
            let latest = null;
            let latestTime = 0;
            for (const [bid, signetsList] of Object.entries(allSignets)) {
                if (!signetsList || signetsList.length === 0) continue;
                for (const s of signetsList) {
                    if (s.addedAt > latestTime) {
                        latestTime = s.addedAt;
                        const b = localBooks.find(x => x.id === bid);
                        if (b) {
                            latest = {
                                bookId: bid,
                                bookTitle: b.title,
                                chapterIndex: s.chapterIdx || 0,
                                addedAt: s.addedAt
                            };
                        }
                    }
                }
            }
            setLastReadSession(latest);
        };
        loadData();
    }, []);

    const setSettings = useCallback(async (newSettings) => {
        const normalized = {
            ...DEFAULT_SETTINGS,
            ...newSettings,
            theme: THEME_KEYS.includes(newSettings?.theme) ? newSettings.theme : 'sepia',
            backgroundAnimations: normalizeBackgroundAnimations(newSettings?.backgroundAnimations)
        };
        setSettingsState(normalized);
        await saveSettings(normalized);
    }, []);

    // Apply global theme + font settings
    useEffect(() => {
        document.documentElement.setAttribute('data-theme', settings.theme);
        document.documentElement.style.setProperty('--font-size-multiplier', settings.fontScale);
        document.documentElement.style.setProperty('--text-alignment', settings.alignment);
        const widthMap = { small: '640px', medium: '760px', large: '980px' };
        document.documentElement.style.setProperty('--book-content-max', widthMap[settings.contentWidth] || widthMap.medium);
        if (settings.theme !== 'sepia') {
            BOOK_VAR_KEYS.forEach(k => document.documentElement.style.removeProperty(k));
        }
    }, [settings]);

    const activeBook = useMemo(() => books.find(b => b.id === activeBookId), [books, activeBookId]);

    // Apply book-specific CSS variables (only in sepia mode)
    useEffect(() => {
        if (settings.theme !== 'sepia') return;
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
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '.json,.txt,.md,.epub';

        input.onchange = async (e) => {
            const file = e.target.files[0];
            if (!file) return;

            const isEpub = file.name.endsWith('.epub');
            const reader = new FileReader();

            reader.onload = async (event) => {
                const content = event.target.result;
                let book = null;

                if (file.name.endsWith('.json')) {
                    try {
                        book = JSON.parse(content);
                        book.isImported = true;
                    } catch (err) {
                        alert("Erreur de lecture du JSON: " + err.message);
                        return;
                    }
                } else if (isEpub) {
                    try {
                        const epub = ePub(content);
                        const metadata = await epub.loaded.metadata;
                        const spine = await epub.loaded.spine;

                        const chapters = [];
                        const requestFn = epub.load.bind(epub);
                        for (const item of spine.items) {
                            try {
                                const section = epub.spine.get(item.idref);
                                if (!section) continue;
                                const doc = await section.load(requestFn);
                                const body = doc.querySelector("body");
                                let html = body ? body.innerHTML : "";
                                html = html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');

                                chapters.push({
                                    id: item.idref,
                                    title: section.label || item.idref,
                                    html: html
                                });
                                section.unload();
                            } catch (e) {
                                console.warn(`Could not load section ${item.idref}`, e);
                            }
                        }

                        book = {
                            id: 'epub-' + Date.now(),
                            title: metadata.title || file.name,
                            author: metadata.creator || "Auteur inconnu",
                            year: new Date().getFullYear(),
                            isImported: true,
                            design: { variables: { "--book-font-size": "1.05rem", "--book-line-height": "1.7" } },
                            introHtml: `<h1>${metadata.title || file.name}</h1><p class="dropcap">EPUB importé : ${file.name}</p>`,
                            chapters: chapters.length > 0 ? chapters : [{
                                id: 'ch-error',
                                title: 'Erreur',
                                html: '<p>Impossible d\'extraire les chapitres de cet EPUB.</p>'
                            }]
                        };
                    } catch (err) {
                        alert("Erreur de lecture de l'EPUB: " + err.message);
                        console.error(err);
                        return;
                    }
                } else {
                    const title = file.name.replace(/\.[^/.]+$/, "").replace(/[_-]/g, " ");
                    book = {
                        id: 'import-' + Date.now(),
                        title: title.charAt(0).toUpperCase() + title.slice(1),
                        author: "Import Local",
                        year: new Date().getFullYear(),
                        isImported: true,
                        design: { variables: { "--book-font-size": "1.05rem", "--book-line-height": "1.8" } },
                        introHtml: `<h1>${title}</h1><p class="dropcap">Fichier importé : ${file.name}</p>`,
                        chapters: [{
                            id: 'ch-1',
                            title: 'Texte complet',
                            html: parseImportedText(content)
                        }]
                    };
                }

                if (book) {
                    await saveBook(book);
                    setBooks(prev => {
                        const idx = prev.findIndex(b => b.id === book.id);
                        if (idx >= 0) { const n = [...prev]; n[idx] = book; return n; }
                        return [...prev, book];
                    });
                    alert(`"${book.title}" a été ajouté à votre bibliothèque !`);
                }
            };

            if (isEpub) {
                reader.readAsArrayBuffer(file);
            } else {
                reader.readAsText(file);
            }
        };
        input.click();
    };

    const parseImportedText = (text) => {
        const lines = text.split(/\r?\n/);
        let html = '';
        let firstPara = true;

        lines.forEach(line => {
            const trimmed = line.trim();
            if (!trimmed) {
                html += '<br/>';
                return;
            }

            let content = trimmed;
            let className = 'chapter-paragraph';

            if (firstPara && trimmed.length > 50) {
                className = 'dropcap';
                firstPara = false;
            }

            content = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            content = content.replace(/\*(.*?)\*/g, '<em>$1</em>');

            if (trimmed.startsWith('# ')) {
                html += `<h1 class="chapter-main-title">${content.replace('# ', '')}</h1>`;
            } else if (trimmed.startsWith('## ')) {
                html += `<h2 class="chapter-subtitle">${content.replace('## ', '')}</h2>`;
            } else {
                html += `<p class="${className}">${content}</p>`;
            }
        });
        return html;
    };

    const handleImportDirectory = async () => {
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
    const goBack = (to = 'library') => setCurrentView(to);

    const renderView = () => {
        if (currentView === 'library') {
            return (
                <LibraryView
                    books={books}
                    onImport={handleImport}
                    onImportDirectory={handleImportDirectory}
                    onOpenBook={openBook}
                    settings={settings}
                    onUpdateSettings={setSettings}
                    lastSession={lastReadSession}
                    onResume={(session) => {
                        setActiveBookId(session.bookId);
                        setCurrentView('reader');
                    }}
                    onShowAbout={() => setShowAbout(true)}
                    onShowMusic={() => setShowMusic(true)}
                    onShowSettings={() => setShowSettings(true)}
                    currentTrack={currentTrack}
                    isPlaying={isPlaying}
                    isLoop={isLoop}
                    onTogglePlay={togglePlay}
                    onToggleLoop={toggleLoop}
                    onStop={stopPlay}
                />
            );
        }
        if (currentView === 'bookHome' && activeBook) {
            return (
                <BookHomeView book={activeBook} onBack={() => goBack('library')} onStartReading={startReading} />
            );
        }
        if (currentView === 'reader' && activeBook) {
            return (
                <ReaderView
                    book={activeBook}
                    onBack={() => goBack('bookHome')}
                    settings={settings}
                    onUpdateSettings={setSettings}
                    backgroundAnimations={settings.backgroundAnimations}
                    currentTrack={currentTrack}
                    isPlaying={isPlaying}
                    isLoop={isLoop}
                    onTogglePlay={togglePlay}
                    onToggleLoop={toggleLoop}
                    onShowMusic={() => setShowMusic(true)}
                    onStop={stopPlay}
                    onToggleFullscreen={toggleFullscreen}
                    isFullscreen={isFullscreen}
                />
            );
        }
        return null;
    };

    return (
        <div className={`app-root theme-${settings.theme}`}>
            {currentView !== 'reader' && <Ambience theme={settings.theme} enabledByTheme={settings.backgroundAnimations} />}
            {renderView()}
            {showAbout && <AboutModal onClose={() => setShowAbout(false)} />}
            {showSettings && (
                <GlobalSettingsModal
                    settings={settings}
                    onUpdateSettings={setSettings}
                    onClose={() => setShowSettings(false)}
                />
            )}
            <MusicPlayerModal
                isOpen={showMusic}
                onClose={() => setShowMusic(false)}
                currentTrack={currentTrack}
                isPlaying={isPlaying}
                isLoop={isLoop}
                onPlayTrack={playTrack}
                onTogglePlay={togglePlay}
                onToggleLoop={toggleLoop}
            />
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
