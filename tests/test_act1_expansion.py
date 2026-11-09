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


class TestAct1Expansion(unittest.TestCase):
    def get_chapter_path(self, num: int) -> Path:
        matches = list(BOOK_DIR.glob(f"{num:02d}-*.html"))
        self.assertEqual(len(matches), 1, f"Fichier pour chapitre {num} introuvable")
        return matches[0]

    def count_words(self, html: str) -> int:
        clean = re.sub(r"<[^>]+>", " ", html)
        return len(re.findall(r"\b\w+\b", clean))

    def test_chapter_files_exist(self):
        for i in range(1, 13):
            self.assertTrue(self.get_chapter_path(i).is_file())
        interlude = BOOK_DIR / "interlude-01-registre-des-mots-interdits.html"
        self.assertTrue(interlude.is_file(), f"Fichier d'interlude manquant : {interlude}")

    def test_word_counts(self):
        ch1_path = self.get_chapter_path(1)
        ch1_words = self.count_words(ch1_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(ch1_words, 2500, f"Le chapitre 1 doit dépasser 2 500 mots (actuel: {ch1_words})")

        total_words = 0
        for i in range(1, 13):
            p = self.get_chapter_path(i)
            words = self.count_words(p.read_text(encoding="utf-8"))
            total_words += words
            self.assertGreaterEqual(words, 750, f"Le chapitre {i} doit dépasser 750 mots (actuel: {words})")

        interlude_path = BOOK_DIR / "interlude-01-registre-des-mots-interdits.html"
        self.assertTrue(interlude_path.is_file(), f"Fichier d'interlude manquant : {interlude_path}")
        i_words = self.count_words(interlude_path.read_text(encoding="utf-8"))
        total_words += i_words
        self.assertGreaterEqual(i_words, 400, f"L'interlude doit dépasser 400 mots (actuel: {i_words})")

        self.assertGreaterEqual(
            total_words, 12000, f"L'Acte 1 complet doit atteindre au moins 12 000 mots (actuel: {total_words})"
        )

    def test_html_structure_and_tags(self):
        for i in range(1, 13):
            content = self.get_chapter_path(i).read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn(f"Chapitre {i} :", content)
            self.assertIn('<p class="chapter-byline">ACTE 1 : Le Plissage et la Fêlure</p>', content)
            self.assertIn(f"chapter-{i:02d}.webp?v=5", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

        interlude_path = BOOK_DIR / "interlude-01-registre-des-mots-interdits.html"
        if interlude_path.is_file():
            content = interlude_path.read_text(encoding="utf-8")
            self.assertIn('<div class="chapter-content">', content)
            self.assertIn("Interlude I", content)
            self.assertIn('<p class="chapter-paragraph">', content)
            self.assertTrue(content.strip().endswith("</div>"))

    def test_canon_concepts_act1(self):
        ch1 = self.get_chapter_path(1).read_text(encoding="utf-8")
        self.assertIn("Écœurement Sémantique", ch1)
        self.assertIn("Tonicité Dégressive", ch1)

        ch3 = self.get_chapter_path(3).read_text(encoding="utf-8")
        self.assertTrue(any(term in ch3.lower() for term in ["lyra", "cadavre", "décharnée", "stase"]))

        ch12 = self.get_chapter_path(12).read_text(encoding="utf-8")
        self.assertTrue(any(term in ch12.lower() for term in ["tuyau", "b-412", "descente", "évacuation"]))

    def test_zero_forbidden_dashes(self):
        found_dashes = []
        for i in range(1, 13):
            p = self.get_chapter_path(i)
            text = p.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((p.name, lineno, name, line))

        interlude_path = BOOK_DIR / "interlude-01-registre-des-mots-interdits.html"
        if interlude_path.is_file():
            text = interlude_path.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), 1):
                for char, name in DASH_CHARS.items():
                    if char in line:
                        found_dashes.append((interlude_path.name, lineno, name, line))

        self.assertEqual(found_dashes, [], f"Tirets interdits détectés : {found_dashes}")


if __name__ == "__main__":
    unittest.main()
