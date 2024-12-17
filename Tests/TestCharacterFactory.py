import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero


class TestDungeon(unittest.TestCase):
    def setUp(self):
        Hero.delete_instance()
        self.hero = CharacterFactory.create_hero("hero", Element.WATER)
        self.monster = CharacterFactory.create_monster(Element.WATER)

    def test_create_hero(self):
        self.assertEqual(self.hero.get_name(), "hero")
        self.assertEqual(self.hero.get_image(), 'water_hero.png')
        self.assertEqual(self.hero.get_hit_image(), 'water_hero_hit.png')
        self.assertEqual(self.hero.get_dead_image(), 'water_hero_dead.png')
        self.assertEqual(self.hero.get_max_hp(), 80)
        self.assertEqual(self.hero.get_agility(), 8)
        self.assertEqual(self.hero.get_element(), Element.WATER)

    def test_create_monster(self):
        self.assertEqual(self.monster.get_name(), "Water Monster")
        self.assertEqual(self.monster.get_image(), 'water_monster.png')
        self.assertEqual(self.monster.get_hit_image(), 'water_monster_hit.png')
        self.assertEqual(self.monster.get_dead_image(), 'water_monster_dead.png')
        self.assertEqual(self.monster.get_max_hp(), 30)
        self.assertEqual(self.monster.get_agility(), 8)
        self.assertEqual(self.monster.get_element(), Element.WATER)


