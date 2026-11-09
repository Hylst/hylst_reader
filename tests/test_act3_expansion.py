from pathlib import Path
import re
import unittest

BOOK_DIR = Path("public/books/chronique-une-atrophie-programmee")

DASH_CHARS = {
    "\u2012": "FIGURE DASH",
    "\u2013": "EN DASH",
    "\u2014": "EM DASH",
    "\u2015": "HORIZONTAL BAR",
    "\ufe58": "SMALL EM DASH",
}


class TestAct3Expansion(unittest.TestCase):
    def get_chapter_path(self, num: int) -> Path:
        matches = list(BOOK_DIR.glob(f"{num:02d}-*.html"))
        self.assertEqual(len(matches), 1, f"Fichier pour chapitre {num} introuvable")
        return matches[0]

    def count_words(self, html: str) -> int:
        clean = re.sub(r"<[^>]+>", " ", html)
        return len(re.findall(r"\b\w+\b", clean))

    def test_chapter_files_exist(self):
        for i in range(25, 37):
            self.assertTrue(self.get_chapter_path(i).is_file())
        interlude = BOOK_DIR / "interlude-03-dossier-tristan-syndic.html"
        self.assertTrue(interlude.is_file(), f"Fichier d'interlude manquant : {interlude}")

    def test_word_counts(self):
        ch32_path = self.get_chapter_path(32)
        ch32_words = self.count_words(ch32_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(
            ch32_words, 2500, f"Le chapitre 32 (Chapitre-Pilier) doit dépasser 2 500 mots (actuel: {ch32_words})"
        )

        total_words = 0
        for i in range(25, 37):
            p = self.get_chapter_path(i)
            words = self.count_words(p.read_text(encoding="utf-8"))
            total_words += words
            self.assertGreaterEqual(words, 750, f"Le chapitre {i} doit dépasser 750 mots (actuel: {words})")

        interlude_path = BOOK_DIR / "interlude-03-dossier-tristan-syndic.html"
        self.assertTrue(interlude_path.is_file(), f"Fichier d'interlude manquant : {interlude_path}")
        i_words = self.count_words(interlude_path.read_text(encoding="utf-8"))
        total_words += i_words
        self.assertGreaterEqual(i_words, 400, f"L'interlude 03 doit dépasser 400 mots (actuel: {i_words})")

        self.assertGreaterEqual(
            total_words, 12000, f"L'Acte 3 complet doit atteindre au moins 12 000 mots (actuel: {total_words})"
        )

    def test_html_structure_and_tags(self):
        for i in range(25, 37):
            content = self.get_chapter_path(i).read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn(f"Chapitre {i} :", content)
            self.assertIn('<p class="chapter-byline">ACTE 3 : L\'Ombre et le Doute</p>', content)
            self.assertIn(f"chapter-{i:02d}.webp?v=5", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

        interlude_path = BOOK_DIR / "interlude-03-dossier-tristan-syndic.html"
        if interlude_path.is_file():
            content = interlude_path.read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn("Interlude III", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

    def test_canon_concepts_act3(self):
        ch26 = self.get_chapter_path(26).read_text(encoding="utf-8").lower()
        self.assertTrue("barnabé" in ch26)
        self.assertTrue("agronome" in ch26 or "agronomie" in ch26 or "semence" in ch26)
        self.assertTrue("complicité" in ch26 or "responsable" in ch26 or "faute" in ch26 or "culpabilité" in ch26)

        ch32 = self.get_chapter_path(32).read_text(encoding="utf-8").lower()
        self.assertTrue("poêle" in ch32 or "fourneau" in ch32)
        self.assertTrue("élise" in ch32)
        self.assertTrue("cliquet" in ch32)
        self.assertTrue("marthe" in ch32)

        ch35 = self.get_chapter_path(35).read_text(encoding="utf-8").lower()
        self.assertIn("julien vasseur", ch35)
        self.assertIn("2080-ménilmontant-0348", ch35)
        self.assertTrue("émeraude" in ch35)

        ch36 = self.get_chapter_path(36).read_text(encoding="utf-8").lower()
        self.assertTrue("schisme" in ch36 or "scission" in ch36 or "séparation" in ch36)
        self.assertTrue("60 000" in ch36 or "soixante mille" in ch36)
        self.assertTrue("antihistaminique" in ch36)

        interlude_path = BOOK_DIR / "interlude-03-dossier-tristan-syndic.html"
        if interlude_path.is_file():
            i3 = interlude_path.read_text(encoding="utf-8").lower()
            self.assertIn("s.y.n.d.i.c.", i3)
            self.assertIn("tristan vasseur", i3)
            self.assertIn("julien vasseur", i3)
            self.assertIn("lina", i3)

    def test_zero_forbidden_dashes(self):
        found_dashes = []
        for i in range(25, 37):
            p = self.get_chapter_path(i)
            text = p.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((p.name, lineno, name, line))

        interlude_path = BOOK_DIR / "interlude-03-dossier-tristan-syndic.html"
        if interlude_path.is_file():
            text = interlude_path.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((interlude_path.name, lineno, name, line))

        self.assertEqual(found_dashes, [], f"Tirets interdits détectés : {found_dashes}")


if __name__ == "__main__":
    unittest.main()
