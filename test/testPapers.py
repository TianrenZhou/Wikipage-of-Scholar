import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from crawler.BaseCrawler import crawlPapers
import unittest

class TestPaperMethods(unittest.TestCase):

    def test_marc(self):
        self.assertEqual(len(crawlPapers("https://scholar.google.com/citations?hl=en&user=HaI6LesAAAAJ",6)),6)

    def test_kevin(self):
        self.assertEqual(len(crawlPapers("https://scholar.google.com/citations?hl=en&user=sugWZ6MAAAAJ",8)),8)

if __name__ == '__main__':
    unittest.main()