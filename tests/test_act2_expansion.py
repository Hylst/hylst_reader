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


class TestAct2Expansion(unittest.TestCase):
    def get_chapter_path(self, num: int) -> Path:
        matches = list(BOOK_DIR.glob(f"{num:02d}-*.html"))
        self.assertEqual(len(matches), 1, f"Fichier pour chapitre {num} introuvable")
        return matches[0]

    def count_words(self, html: str) -> int:
        clean = re.sub(r"<[^>]+>", " ", html)
        return len(re.findall(r"\b\w+\b", clean))

    def test_chapter_files_exist(self):
        for i in range(13, 25):
            self.assertTrue(self.get_chapter_path(i).is_file())
        interlude = BOOK_DIR / "interlude-02-rapport-voirie-b412.html"
        self.assertTrue(interlude.is_file(), f"Fichier d'interlude manquant : {interlude}")

    def test_word_counts(self):
        ch14_path = self.get_chapter_path(14)
        ch14_words = self.count_words(ch14_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(ch14_words, 2200, f"Le chapitre 14 (Chapitre-Pilier) doit dépasser 2 200 mots (actuel: {ch14_words})")

        total_words = 0
        for i in range(13, 25):
            p = self.get_chapter_path(i)
            words = self.count_words(p.read_text(encoding="utf-8"))
            total_words += words
            self.assertGreaterEqual(words, 750, f"Le chapitre {i} doit dépasser 750 mots (actuel: {words})")

        interlude_path = BOOK_DIR / "interlude-02-rapport-voirie-b412.html"
        self.assertTrue(interlude_path.is_file(), f"Fichier d'interlude manquant : {interlude_path}")
        i_words = self.count_words(interlude_path.read_text(encoding="utf-8"))
        total_words += i_words
        self.assertGreaterEqual(i_words, 400, f"L'interlude 02 doit dépasser 400 mots (actuel: {i_words})")

        self.assertGreaterEqual(
            total_words, 12000, f"L'Acte 2 complet doit atteindre au moins 12 000 mots (actuel: {total_words})"
        )

    def test_html_structure_and_tags(self):
        for i in range(13, 25):
            content = self.get_chapter_path(i).read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn(f"Chapitre {i} :", content)
            self.assertIn('<p class="chapter-byline">ACTE 2 : La Chair et les Décombres</p>', content)
            self.assertIn(f"chapter-{i:02d}.webp?v=5", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

        interlude_path = BOOK_DIR / "interlude-02-rapport-voirie-b412.html"
        if interlude_path.is_file():
            content = interlude_path.read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn("Interlude II", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

    def test_canon_concepts_act2(self):
        ch14 = self.get_chapter_path(14).read_text(encoding="utf-8").lower()
        self.assertIn("fers de marche", ch14)
        self.assertTrue("otolithe" in ch14 or "vestibulaire" in ch14)
        self.assertTrue("bile" in ch14 or "vomis" in ch14)
        self.assertTrue("cliquet" in ch14)
        self.assertTrue("marthe" in ch14)

        ch16 = self.get_chapter_path(16).read_text(encoding="utf-8").lower()
        self.assertIn("bibliothèque", ch16)
        self.assertIn("barnabé", ch16)

        ch21 = self.get_chapter_path(21).read_text(encoding="utf-8").lower()
        ch22 = self.get_chapter_path(22).read_text(encoding="utf-8").lower()
        ch23 = self.get_chapter_path(23).read_text(encoding="utf-8").lower()
        combined_turbines = f"{ch21} {ch22} {ch23}"
        self.assertIn("grand réfrigérant", combined_turbines)
        self.assertIn("turbine", combined_turbines)
        self.assertIn("saint-denis", combined_turbines)

        interlude_path = BOOK_DIR / "interlude-02-rapport-voirie-b412.html"
        if interlude_path.is_file():
            i2 = interlude_path.read_text(encoding="utf-8")
            self.assertIn("B-412", i2)
            self.assertIn("S.Y.N.D.I.C.", i2)

    def test_zero_forbidden_dashes(self):
        found_dashes = []
        for i in range(13, 25):
            p = self.get_chapter_path(i)
            text = p.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((p.name, lineno, name, line))

        interlude_path = BOOK_DIR / "interlude-02-rapport-voirie-b412.html"
        if interlude_path.is_file():
            text = interlude_path.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((interlude_path.name, lineno, name, line))

        self.assertEqual(found_dashes, [], f"Tirets interdits détectés : {found_dashes}")


if __name__ == "__main__":
    unittest.main()
