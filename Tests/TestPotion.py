import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from Model.Potion import HealthPotion, VisionPotion

class TestPotions(unittest.TestCase):
    CharacterFactory.create_hero("hero", Element.EARTH)
    def setUp(self):
        # Singleton Hero instance
        self.hero = Hero.get_instance()
        self.hero.set_max_hp(100)
        self.hero.set_hp(50)
        self.hero.set_vision_status(False)

    def test_potion_initialization(self):
        health_potion = HealthPotion()
        vision_potion = VisionPotion()

        # Test Potion initialization for HealthPotion
        self.assertEqual(health_potion.get_name(), "health")
        self.assertEqual(health_potion.get_image(), "health_potion.png")

        # Test Potion initialization for VisionPotion
        self.assertEqual(vision_potion.get_name(), "vision")
        self.assertEqual(vision_potion.get_image(), "vision_potion.png")

    def test_drink_health_potion(self):
        potion = HealthPotion()
        potion.drink()
        self.assertEqual(self.hero.get_hp(), 60)

    def test_drink_health_potion_when_full_hp(self):
        self.hero.set_hp(100)
        potion = HealthPotion()
        potion.drink()
        self.assertEqual(self.hero.get_hp(), 100)  # HP should not exceed max

    def test_drink_vision_potion(self):
        potion = VisionPotion()
        potion.drink()
        self.assertTrue(self.hero.get_drank_vision_potion())  # Hero should gain vision status