import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from helper.webFilter import isValid
import unittest

class TestFilterMethods(unittest.TestCase):

    def test_true_edu(self):
        self.assertTrue(isValid("https://snir.cs.illinois.edu/"))

    def test_true_org(self):
        self.assertTrue(isValid("https://en.wikipedia.org/wiki/Marc_Snir"))

    def test_true_gov(self):
        self.assertTrue(isValid("https://www.anl.gov/profile/marc-snir"))

    def test_false(self):
        self.assertFalse(isValid("https://www.linkedin.com/in/snirmarc"))
if __name__ == '__main__':
    unittest.main()