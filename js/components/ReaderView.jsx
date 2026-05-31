// js/components/ReaderView.jsx
// Dépend de : window.Icon, window.Ambience, window.normalizeBackgroundAnimations, window.HylstDB

const { useState: useStateReader, useEffect: useEffectReader, useMemo: useMemoReader, useRef: useRefReader, useCallback: useCallbackReader } = React;

const THEME_KEYS_READER = ['sepia', 'light', 'dark'];

function ReaderView({ book, onBack, settings, onUpdateSettings, currentTrack, isPlaying, isLoop, onTogglePlay, onToggleLoop, onShowMusic, onStop, onToggleFullscreen, isFullscreen }) {
    const Icon = window.Icon;
    const Ambience = window.Ambience;
    const normalizeBackgroundAnimations = window.normalizeBackgroundAnimations;
    const { getProgress, saveProgress, getSignets, saveSignet, removeSignet } = window.HylstDB;

    const [currentChapterIdx, setCurrentChapterIdx] = useStateReader(0);
    const [chapterHtml, setChapterHtml] = useStateReader('');
    const [showUI, setShowUI] = useStateReader(true);
    const [showSidebar, setShowSidebar] = useStateReader(false);
    const [showSettings, setShowSettings] = useStateReader(false);
    const [scrollProgress, setScrollProgress] = useStateReader(0);
    const [signets, setSignets] = useStateReader([]);

    const containerRef = useRefReader(null);
    const touchStartRef = useRefReader(null);
    const uiTimeoutRef = useRefReader(null);
    const chapter = book.chapters?.[currentChapterIdx];

    const transformChapterHTML = useCallbackReader((html) => {
        if (!html) return html;
        let out = html;
        const basePath = `public/books/${book.id}/`;
        out = out.replace(/<img\s+src="([^"]+)"/g, (match, src) => {
            if (src.startsWith('http') || src.startsWith('/') || src.startsWith('data:')) return match;
            return `<img src="${basePath}${src}"`;
        });
        out = out.replace(/<p>\s*PARTIE\s*II\s*<\/p>/i, '<h1>Partie 1 :</h1>');
        out = out.replace(/<p>\s*La\s+Capitulation\s+Silencieuse\s*<\/p>/i, '<h2>La Capitulation Silencieuse</h2>');
        out = out.replace(/<p>\s*Partie\s*I\s*<\/p>/i, '<h1>Partie I</h1>');
        out = out.replace(/<p>\s*Le\s+grand\s+point d'inflexion\s*<\/p>/i, "<h2>Le grand point d'inflexion</h2>");
        return out;
    }, [book.id]);

    useEffectReader(() => {
        getSignets(book.id).then(s => setSignets(s || []));
    }, [book.id]);

    useEffectReader(() => {
        getProgress(book.id).then(prog => {
            if (prog) {
                const idx = prog.chapterIndex || 0;
                if (book.chapters?.[idx] && book.chapters[idx].available !== false) {
                    setCurrentChapterIdx(idx);
                } else {
                    const firstAvail = book.chapters?.findIndex(ch => ch.available !== false);
                    setCurrentChapterIdx(firstAvail >= 0 ? firstAvail : 0);
                }
            }
        });
    }, [book.id]);

    useEffectReader(() => {
        if (!chapter) return;
        if (chapter.html) {
            setChapterHtml(transformChapterHTML(chapter.html));
        } else if (chapter.path) {
            setChapterHtml('');
            window.fetch(`public/${chapter.path}?t=${Date.now()}`)
                .then(r => r.text())
                .then(html => setChapterHtml(transformChapterHTML(html)))
                .catch(() => setChapterHtml('<p>Erreur lors du chargement.</p>'));
        }
        if (containerRef.current) containerRef.current.scrollTop = 0;
        setScrollProgress(0);

        const timer = setTimeout(async () => {
            const prog = await getProgress(book.id);
            if (prog && prog.chapterIndex === currentChapterIdx && prog.scrollRatio > 0 && containerRef.current) {
                const { scrollHeight, clientHeight } = containerRef.current;
                containerRef.current.scrollTop = prog.scrollRatio * (scrollHeight - clientHeight);
                setScrollProgress(prog.scrollRatio);
            }
        }, 200);
        return () => clearTimeout(timer);
    }, [chapter, transformChapterHTML]);

    useEffectReader(() => {
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

    const handleScroll = useCallbackReader(() => {
        if (!containerRef.current) return;
        const { scrollTop, scrollHeight, clientHeight } = containerRef.current;
        const ratio = scrollTop / Math.max(scrollHeight - clientHeight, 1);
        setScrollProgress(ratio);
        saveProgress(book.id, currentChapterIdx, ratio);
    }, [book.id, currentChapterIdx]);

    const handleTouchStart = (e) => { touchStartRef.current = e.changedTouches[0].clientX; };
    const handleTouchEnd = (e) => {
        if (touchStartRef.current === null) return;
        const dx = e.changedTouches[0].clientX - touchStartRef.current;
        touchStartRef.current = null;
        if (Math.abs(dx) < 50) return;
        if (dx < 0) nextChapter();
        else prevChapter();
    };

    const hasNextChapter = useMemoReader(() => {
        if (!book.chapters || currentChapterIdx >= book.chapters.length - 1) return false;
        return book.chapters[currentChapterIdx + 1].available !== false;
    }, [book.chapters, currentChapterIdx]);

    const hasPrevChapter = useMemoReader(() => {
        if (!book.chapters || currentChapterIdx <= 0) return false;
        return book.chapters[currentChapterIdx - 1].available !== false;
    }, [book.chapters, currentChapterIdx]);

    const nextChapter = () => {
        if (hasNextChapter) setCurrentChapterIdx(i => i + 1);
    };
    const prevChapter = () => {
        if (hasPrevChapter) setCurrentChapterIdx(i => i - 1);
    };

    const { readingTime, remainingTime } = useMemoReader(() => {
        if (!chapterHtml) return { readingTime: '', remainingTime: '' };
        const text = chapterHtml.replace(/<[^>]+>/g, ' ');
        const words = text.split(/\s+/).filter(w => w.length > 0).length;
        const mins = Math.ceil(words / 220);
        const remWords = Math.ceil(words * (1 - scrollProgress));
        const remMins = Math.ceil(remWords / 220);
        return {
            readingTime: mins > 0 ? `${mins} min de lecture` : "Moins d'une minute",
            remainingTime: remMins > 0 ? `${remMins} min restantes` : ""
        };
    }, [chapterHtml, scrollProgress]);

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

    useEffectReader(() => {
        const handleKeyDown = (e) => {
            if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
            if (e.key === 'ArrowRight') nextChapter();
            if (e.key === 'ArrowLeft') prevChapter();
            if (e.key === ' ') {
                e.preventDefault();
                if (containerRef.current) {
                    containerRef.current.scrollBy({ top: window.innerHeight * 0.8, behavior: 'smooth' });
                }
            }
            if (e.key === 'Home') scrollTo('top');
            if (e.key === 'End') scrollTo('bottom');
            if (e.key === 'Escape') {
                if (showSidebar) setShowSidebar(false);
                else if (showSettings) setShowSettings(false);
                else {
                    setShowUI(v => {
                        const next = !v;
                        if (next) {
                            clearTimeout(uiTimeoutRef.current);
                            uiTimeoutRef.current = setTimeout(() => setShowUI(false), 3000);
                        }
                        return next;
                    });
                }
            }
        };
        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, [currentChapterIdx, showSidebar, showSettings]);

    const containerClass = `reader-container${showUI ? ' show-ui' : ''}${settings.focusMode ? ' focus-mode' : ''}`;

    return (
        <div className="reader-wrapper view-enter">
            <Ambience theme={settings.theme} enabledByTheme={settings.backgroundAnimations} inReader />
            <div className="reader-progress-bar" style={{ width: `${scrollProgress * 100}%` }} />

            <div className={`sidebar-overlay${showSidebar ? ' open' : ''}`} onClick={() => setShowSidebar(false)} />
            <aside className={`sidebar${showSidebar ? ' open' : ''}`}>
                <div className="sidebar-header">
                    <h3>{book.title}</h3>
                    <button className="btn btn-ghost btn-icon" onClick={() => setShowSidebar(false)}><Icon.X /></button>
                </div>
                <div className="sidebar-body">
                    <div className="toc-section-label">Chapitres</div>
                    {book.chapters.map((ch, i) => {
                        const isAvailable = ch.available !== false;
                        return (
                            <div key={ch.id} className={`toc-item${i === currentChapterIdx ? ' active' : ''}${!isAvailable ? ' disabled' : ''}`}
                                onClick={() => {
                                    if (isAvailable) {
                                        setCurrentChapterIdx(i);
                                        setShowSidebar(false);
                                    }
                                }}
                                style={!isAvailable ? { opacity: 0.5, cursor: 'not-allowed', display: 'flex', alignItems: 'center', justifyContent: 'space-between' } : {}}
                            >
                                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                                    <span className="toc-num">{i + 1}</span>
                                    <span>{ch.title}</span>
                                </div>
                                {!isAvailable && <Icon.Lock />}
                            </div>
                        );
                    })}
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

            {showSettings && (
                <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && setShowSettings(false)}>
                    <div className="modal-content settings-modal">
                        <div className="modal-header">
                            <h3>Paramètres de lecture</h3>
                            <button className="btn btn-ghost btn-icon" onClick={() => setShowSettings(false)}><Icon.X /></button>
                        </div>
                        <div className="settings-body">
                            <div className="setting-group">
                                <label>Thème</label>
                                <div className="setting-options">
                                    {THEME_KEYS_READER.map(t => (
                                        <button key={t} className={`btn${settings.theme === t ? ' btn-primary' : ''}`}
                                            onClick={() => onUpdateSettings({ ...settings, theme: t })}>
                                            {t === 'sepia' ? <Icon.Book /> : t === 'light' ? <Icon.Sun /> : <Icon.Moon />}
                                            {t === 'sepia' ? 'Sépia' : t === 'light' ? 'Clair' : 'Sombre'}
                                        </button>
                                    ))}
                                </div>
                            </div>
                            <div className="setting-group">
                                <label>Animations de fond par thème</label>
                                <div className="theme-animation-grid">
                                    {THEME_KEYS_READER.map(t => {
                                        const label = t === 'sepia' ? 'Sépia' : t === 'light' ? 'Clair' : 'Sombre';
                                        const active = !!normalizeBackgroundAnimations(settings.backgroundAnimations)[t];
                                        return (
                                            <div className="theme-animation-item" key={`reader-anim-${t}`}>
                                                <span className="theme-animation-label">{label}</span>
                                                <button
                                                    className={`btn${active ? ' btn-primary' : ''}`}
                                                    onClick={() => onUpdateSettings({
                                                        ...settings,
                                                        backgroundAnimations: {
                                                            ...normalizeBackgroundAnimations(settings.backgroundAnimations),
                                                            [t]: !active
                                                        }
                                                    })}
                                                >
                                                    {active ? 'Animé' : 'Statique'}
                                                </button>
                                            </div>
                                        );
                                    })}
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
                            <div className="setting-group">
                                <label>Indicateurs</label>
                                <div className="setting-options">
                                    <button className={`btn${settings.showReadingTime ? ' btn-primary' : ''}`}
                                        onClick={() => onUpdateSettings({ ...settings, showReadingTime: !settings.showReadingTime })}>
                                        Temps
                                    </button>
                                    <button className={`btn${settings.showProgressPercent ? ' btn-primary' : ''}`}
                                        onClick={() => onUpdateSettings({ ...settings, showProgressPercent: !settings.showProgressPercent })}>
                                        % Slider
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            <div className="reader-slider" onClick={handleSliderClick}>
                <div className="reader-slider-handle" style={{ top: `${scrollProgress * 100}%`, height: '20px' }}>
                    {settings.showProgressPercent && (
                        <div className="reader-slider-tooltip">{Math.round(scrollProgress * 100)}%</div>
                    )}
                </div>
            </div>

            <div
                ref={containerRef}
                className={containerClass}
                onClick={handleContainerClick}
                onScroll={handleScroll}
                onTouchStart={handleTouchStart}
                onTouchEnd={handleTouchEnd}
            >
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
                        <button className="btn btn-icon" title="Table des matières" onClick={e => { e.stopPropagation(); setShowSidebar(true); }}>
                            <Icon.List />
                        </button>
                        <button className="btn btn-icon" title="Paramètres" onClick={e => { e.stopPropagation(); setShowSettings(true); }}>
                            <Icon.Settings />
                        </button>
                        <button className="btn btn-icon" title="Musique" onClick={e => { e.stopPropagation(); onShowMusic(); }}>
                            <Icon.Music />
                        </button>
                        <button className="btn btn-icon" title={isPlaying ? 'Pause' : 'Lecture'} onClick={e => { e.stopPropagation(); onTogglePlay(); }}>
                            {isPlaying ? <Icon.Pause /> : <Icon.Play />}
                        </button>
                        <button className={`btn btn-icon${isLoop ? ' active-loop' : ''}`} title={isLoop ? 'Boucle active' : 'Boucle inactive'} onClick={e => { e.stopPropagation(); onToggleLoop(); }}>
                            {isLoop ? <Icon.Repeat /> : <Icon.RepeatOff />}
                        </button>
                        <button className="btn btn-icon" title="Arrêter" onClick={e => { e.stopPropagation(); onStop(); }}>
                            <Icon.Square />
                        </button>
                        <button className="btn btn-icon" title="Immersion (Plein écran)" onClick={e => { e.stopPropagation(); onToggleFullscreen(); }}>
                            {isFullscreen ? <Icon.Minimize /> : <Icon.Maximize />}
                        </button>
                    </div>
                </div>

                <article className="reader-content">
                    {chapterHtml
                        ? <div className="reader-article" dangerouslySetInnerHTML={{ __html: chapterHtml }} />
                        : <div style={{ textAlign: 'center', padding: '4rem 0', opacity: 0.4 }}>
                            <div className="spinner" style={{ margin: '0 auto' }} />
                        </div>
                    }
                </article>

                <div className="chapter-nav">
                    <div className="chapter-nav-left">
                        <button className="nav-btn" onClick={e => { e.stopPropagation(); prevChapter(); }}
                            disabled={!hasPrevChapter}>
                            <Icon.ArrowLeft /> <span>Précédent</span>
                        </button>
                    </div>

                    <div className="chapter-nav-center">
                        {settings.showReadingTime && (remainingTime || readingTime) && (
                            <span className="reading-time-inline" style={{ fontSize: '0.8rem', opacity: 0.8, marginRight: '1rem', fontStyle: 'italic' }}>
                                {remainingTime || readingTime}
                            </span>
                        )}
                        <span className="chapter-counter">{currentChapterIdx + 1} / {book.chapters.length}</span>
                    </div>

                    <div className="chapter-nav-right">
                        <button className="nav-btn" onClick={e => { e.stopPropagation(); nextChapter(); }}
                            disabled={!hasNextChapter}>
                            <span>Suivant</span> <Icon.ArrowRight />
                        </button>

                        <div className="jump-controls-inline">
                            <button className="jump-btn-small" onClick={e => { e.stopPropagation(); scrollTo('top'); }} title="Haut"><Icon.ChevronUp /></button>
                            <button className="jump-btn-small" onClick={e => { e.stopPropagation(); scrollTo('bottom'); }} title="Bas"><Icon.ChevronDown /></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

window.ReaderView = ReaderView;
