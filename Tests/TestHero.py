import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Hero import Hero
from Model.Element import Element

class TestHero(unittest.TestCase):
    def setUp(self):
        Hero.delete_instance()  # Ensure fresh singleton instance
        self.hero = CharacterFactory.create_hero("hero", Element.WATER)

    def tearDown(self):
        Hero.delete_instance()  # Clean up singleton instance after tests

    def test_singleton_enforcement(self):
        # Ensure only one instance can exist
        with self.assertRaises(Exception) as context:
            Hero("another_hero", "hero.png", "hero_hit.png", "hero_dead.png", 50, 5, Element.WATER)
        self.assertEqual(str(context.exception), "Hero already exists!")

    def test_get_instance(self):
        # Test that get_instance returns the singleton
        self.assertEqual(Hero.get_instance(), self.hero)

    def test_delete_instance(self):
        # Test that deleting the instance allows recreation
        Hero.delete_instance()
        new_hero = Hero("new_hero", "hero.png", "hero_hit.png", "hero_dead.png", 80, 8, Element.EARTH)
        self.assertNotEqual(self.hero, new_hero)

    def test_attack(self):
        chance, damage = self.hero.attack()
        self.assertGreaterEqual(chance, 1)
        self.assertLessEqual(chance, 20)
        self.assertEqual(damage, 5)

    def test_special_attack(self):
        chance, damage = self.hero.special_attack()
        self.assertGreaterEqual(chance, -3)
        self.assertLessEqual(chance, 20)
        self.assertEqual(damage, 10)

    def test_set_attack_mod_valid(self):
        self.hero.set_attack_mod(5)
        self.assertEqual(self.hero.get_attack_mod(), 5)

    def test_set_attack_mod_invalid(self):
        with self.assertRaises(ValueError):
            self.hero.set_attack_mod(-1)  # Negative value
        with self.assertRaises(ValueError):
            self.hero.set_attack_mod("string")  # Non-integer

    def test_set_damage_mod_valid(self):
        self.hero.set_damage_mod(4)
        self.assertEqual(self.hero.get_damage_mod(), 4)

    def test_set_damage_mod_invalid(self):
        with self.assertRaises(ValueError):
            self.hero.set_damage_mod(0)  # Zero
        with self.assertRaises(ValueError):
            self.hero.set_damage_mod(None)  # Non-integer

    def test_set_x_valid(self):
        self.hero.set_x(10)
        self.assertEqual(self.hero.get_x(), 10)

    def test_set_x_invalid(self):
        with self.assertRaises(ValueError):
            self.hero.set_x("invalid")  # Non-integer
        with self.assertRaises(ValueError):
            self.hero.set_x(3.5)  # Float

    def test_set_y_valid(self):
        self.hero.set_y(20)
        self.assertEqual(self.hero.get_y(), 20)

    def test_set_y_invalid(self):
        with self.assertRaises(ValueError):
            self.hero.set_y("invalid")  # Non-integer
        with self.assertRaises(ValueError):
            self.hero.set_y(None)  # None

    def test_set_vision_status_valid(self):
        self.hero.set_vision_status(True)
        self.assertTrue(self.hero.get_drank_vision_potion())
        self.hero.set_vision_status(False)
        self.assertFalse(self.hero.get_drank_vision_potion())

    def test_set_vision_status_invalid(self):
        with self.assertRaises(ValueError):
            self.hero.set_vision_status("not_boolean")  # Non-boolean
        with self.assertRaises(ValueError):
            self.hero.set_vision_status(None)  # None

    def test_get_damage_mod(self):
        self.hero.set_damage_mod(7)
        self.assertEqual(self.hero.get_damage_mod(), 7)

    def test_get_attack_mod(self):
        self.hero.set_attack_mod(6)
        self.assertEqual(self.hero.get_attack_mod(), 6)

    def test_get_coordinates(self):
        self.hero.set_x(15)
        self.hero.set_y(25)
        self.assertEqual(self.hero.get_x(), 15)
        self.assertEqual(self.hero.get_y(), 25)

    def test_vision_status(self):
        self.hero.set_vision_status(True)
        self.assertTrue(self.hero.get_drank_vision_potion())
        self.hero.set_vision_status(False)
        self.assertFalse(self.hero.get_drank_vision_potion())

if __name__ == '__main__':
    unittest.main()
