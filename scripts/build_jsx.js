// scripts/build_jsx.js
// Précompile les fichiers JSX de l'application en JavaScript classique.
// Le runtime ne charge plus Babel : les fichiers servis sont js/dist/*.js.
//
// Usage :
//   node scripts/build_jsx.js           (génère js/dist)
//   node scripts/build_jsx.js --check   (vérifie que js/dist est à jour, code 1 sinon)

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const JS_DIR = path.join(ROOT, 'js');
const OUT_DIR = path.join(JS_DIR, 'dist');
const CHECK = process.argv.includes('--check');
const Babel = require('./vendor/babel.min.js');

const BANNER = (rel) => `// Fichier généré depuis ${rel} par scripts/build_jsx.js. Ne pas modifier à la main.\n`;

function walk(dir) {
    const out = [];
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            if (entry.name === 'dist' || entry.name === 'vendor') continue;
            out.push(...walk(full));
        } else if (entry.name.endsWith('.jsx')) {
            out.push(full);
        }
    }
    return out;
}

function targetFor(source) {
    const rel = path.relative(JS_DIR, source).replace(/\\/g, '/');
    return path.join(OUT_DIR, rel.replace(/\.jsx$/, '.js'));
}

function compile(source) {
    const rel = path.relative(ROOT, source).replace(/\\/g, '/');
    const code = fs.readFileSync(source, 'utf8');
    const result = Babel.transform(code, {
        presets: [['react', { runtime: 'classic' }]],
        sourceType: 'script',
        filename: rel,
        compact: false,
        comments: true
    });
    // Chaque fichier etait isole par Babel au runtime. Les scripts classiques
    // partagent sinon la portee globale (collision des const/let). On conserve
    // l'isolation avec une IIFE : seuls les exports window.* restent visibles.
    const body = result.code.replace(/\r\n/g, '\n');
    return BANNER(rel) + '(function () {\n' + body + '\n})();\n';
}

const sources = walk(JS_DIR).sort();
if (sources.length === 0) {
    console.error('[ERREUR] Aucun fichier JSX trouvé dans js/.');
    process.exit(1);
}

const expected = new Map();
for (const source of sources) {
    expected.set(targetFor(source), compile(source));
}

if (CHECK) {
    let stale = 0;
    for (const [target, content] of expected) {
        const rel = path.relative(ROOT, target).replace(/\\/g, '/');
        if (!fs.existsSync(target)) {
            console.error('[KO] manquant : ' + rel);
            stale++;
            continue;
        }
        const current = fs.readFileSync(target, 'utf8').replace(/\r\n/g, '\n');
        if (current !== content) {
            console.error('[KO] désynchronisé : ' + rel);
            stale++;
        }
    }
    if (fs.existsSync(OUT_DIR)) {
        for (const entry of fs.readdirSync(OUT_DIR, { recursive: true, withFileTypes: true })) {
            if (!entry.isFile() || !entry.name.endsWith('.js')) continue;
            const full = path.join(entry.parentPath || entry.path, entry.name);
            if (!expected.has(full)) {
                console.error('[KO] orphelin : ' + path.relative(ROOT, full).replace(/\\/g, '/'));
                stale++;
            }
        }
    }
    if (stale > 0) {
        console.error(`[ERREUR] ${stale} fichier(s) compilé(s) à régénérer : node scripts/build_jsx.js`);
        process.exit(1);
    }
    console.log(`[OK] ${expected.size} fichier(s) compilé(s) à jour.`);
    process.exit(0);
}

// Écriture atomique et nettoyage des sorties orphelines.
fs.mkdirSync(OUT_DIR, { recursive: true });
for (const [target, content] of expected) {
    fs.mkdirSync(path.dirname(target), { recursive: true });
    const tmp = target + '.tmp';
    fs.writeFileSync(tmp, content, 'utf8');
    fs.renameSync(tmp, target);
}

let removed = 0;
for (const entry of fs.readdirSync(OUT_DIR, { recursive: true, withFileTypes: true })) {
    if (!entry.isFile() || !entry.name.endsWith('.js')) continue;
    const full = path.join(entry.parentPath || entry.path, entry.name);
    if (!expected.has(full)) {
        fs.unlinkSync(full);
        removed++;
    }
}

const bytes = [...expected.values()].reduce((sum, content) => sum + Buffer.byteLength(content), 0);
console.log(`[OK] ${expected.size} fichier(s) JSX compilé(s) vers js/dist (${bytes} octets)` + (removed ? `, ${removed} orphelin(s) supprimé(s)` : '.'));
