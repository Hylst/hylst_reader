// js/components/Ambience.jsx
const { useMemo } = React;

const DEFAULT_BACKGROUND_ANIMATIONS = { sepia: true, light: true, dark: true };

export const normalizeBackgroundAnimations = (value) => ({
    ...DEFAULT_BACKGROUND_ANIMATIONS,
    ...(value || {})
});

export function Ambience({ theme, enabledByTheme, inReader = false }) {
    const enabled = normalizeBackgroundAnimations(enabledByTheme)[theme];
    const particles = useMemo(() => {
        const count = theme === 'dark' ? 24 : theme === 'sepia' ? 18 : 16;
        return Array.from({ length: count }, (_, i) => ({
            id: i,
            x: Math.random() * 100,
            y: Math.random() * 100,
            size: theme === 'dark' ? 2 + Math.random() * 3 : 2.5 + Math.random() * 4,
            duration: 12 + Math.random() * 20,
            delay: -Math.random() * 20,
            drift: (Math.random() - 0.5) * 40,
            opacity: theme === 'dark' ? 0.3 + Math.random() * 0.4 : theme === 'sepia' ? 0.2 + Math.random() * 0.3 : 0.2 + Math.random() * 0.4
        }));
    }, [theme]);

    if (!enabled) return null;

    return (
        <div className={`ambience-overlay ambience-${theme}${inReader ? ' ambience-reader' : ' ambience-app'}`} aria-hidden="true">
            <div className="ambience-grain" />
            <div className="ambience-gradient" />
            {theme === 'sepia' && <div className="ambience-sepia-wave" />}
            {theme === 'dark' && <div className="ambience-dark-aura" />}
            {theme === 'light' && <div className="ambience-light-haze" />}
            <div className={`ambience-particles ${theme}-particles`}>
                {particles.map(particle => (
                    <span
                        key={particle.id}
                        className={`ambience-particle ${theme}-particle`}
                        style={{
                            '--x': `${particle.x}%`,
                            '--y': `${particle.y}%`,
                            '--size': `${particle.size}px`,
                            '--duration': `${particle.duration}s`,
                            '--delay': `${particle.delay}s`,
                            '--drift': `${particle.drift}px`,
                            '--opacity': particle.opacity
                        }}
                    />
                ))}
            </div>
        </div>
    );
}
