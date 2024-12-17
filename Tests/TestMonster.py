import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Monster import Monster
from Model.Element import Element
from Model.Pillar import AbstractionPillar


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.monster = CharacterFactory.create_monster(Element.AIR)
        self.monster.set_pillar(AbstractionPillar())

    def test_monster_constructor(self):
        self.assertEqual(self.monster.get_hp(), 20)
        self.assertEqual(self.monster.get_image(), "air_monster.png")
        self.assertEqual(self.monster.get_max_hp(), 20)
        self.assertEqual(self.monster.get_agility(), 16)
        self.assertEqual(self.monster.get_element(), Element.AIR)

    def test_heal_if_not_at_full_health(self):
        self.monster.set_hp(5)
        if self.monster.heal():
            self.assertEqual(self.monster.get_hp(), 10)
        else:
            self.assertEqual(self.monster.get_hp(), 5)

    def test_heal_if_at_full_health(self):
        self.monster.set_hp(self.monster.get_max_hp())
        self.assertEqual(self.monster.heal(), False)

    def test_get_pillar(self):
        if self.monster.has_pillar():
            self.assertIsNotNone(self.monster.get_pillar())
        else:
            with self.assertRaises(ValueError):
                self.monster.get_pillar()

    def test_has_pillar(self):
        self.assertEqual(self.monster.has_pillar(), self.monster.pillar is not None)

    def test_attack(self):
        chance, damage = self.monster.attack()
        self.assertGreaterEqual(chance, 1)
        self.assertLessEqual(chance, 20)
        self.assertEqual(damage, 5)

    def test_special_attack(self):
        chance, damage = self.monster.special_attack()
        self.assertGreaterEqual(chance, -3)
        self.assertLessEqual(chance, 20)
        self.assertEqual(damage, 10)

    def test_opposite_element(self):
        self.assertEqual(self.monster.get_opposite_element(), Element.EARTH)

    def test_random_potion_assignment(self):
        potion_count = sum([self.monster.has_health_potion(), self.monster.has_vision_potion()])
        self.assertIn(potion_count, [0, 1, 2])

    def test_potion_healing_logic(self):
        # Test healing behavior when monster is at different health levels
        self.monster.set_hp(50)
        self.assertFalse(self.monster.heal())
        self.monster.set_hp(5)
        heal = self.monster.heal()
        if heal:
            self.assertEqual(self.monster.get_hp(), 10)
        else:
            self.assertEqual(self.monster.get_hp(), 5)