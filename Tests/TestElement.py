import unittest

from Model.Element import Element


class TestHero(unittest.TestCase):
    def test_Enum(self):
        self.assertEqual(Element(1), Element.EARTH)
        self.assertEqual(Element(2), Element.FIRE)
        self.assertEqual(Element(3), Element.AIR)
        self.assertEqual(Element(4), Element.WATER)
    def test_opposite(self):
        self.assertEqual(Element.EARTH.get_opposite(), Element.AIR)
        self.assertEqual(Element.AIR.get_opposite(), Element.EARTH)
        self.assertEqual(Element.WATER.get_opposite(), Element.FIRE)
        self.assertEqual(Element.FIRE.get_opposite(), Element.WATER)