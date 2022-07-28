# tests/test_colorful.py
from operator import is_
import unittest

from colorful import is_colorful

class ColorfulTest(unittest.TestCase):
    # check 23 is colorful
    def test_23(self):
        self.assertTrue(is_colorful(23))

    # test - doublon
    def test_doublon(self):
        self.assertFalse(is_colorful(11))

    # test - renvoie erreur si type n'est pas un integer
    def test_type(self):
        self.assertEqual(is_colorful("string"), None)

    # test - zero in number
    def test_zero(self):
        self.assertFalse(is_colorful(309))

    # test - numbers < 10 are colorful
    def test_chiffre(self):
        for i in range(10):
            self.assertTrue(is_colorful(i))

    # test - 1 in number
    def test_chiffre(self):
        self.assertFalse(is_colorful(819))





