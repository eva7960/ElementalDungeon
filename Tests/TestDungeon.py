import unittest

from Controller.SaveLoad import SaveLoad
from Model.Dungeon import Dungeon
from Model.Element import Element
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Pillar import InheritancePillar, Pillar
from Model.Potion import VisionPotion, HealthPotion
from Model.Room import Room


class TestDungeon(unittest.TestCase):
    def test_dungeon_get_instance_none(self):
        self.assertIsNone(Dungeon.get_instance())
    def test_dungeon_get_instance_dungeon(self):
        Dungeon(False, ["name", Element.EARTH])

        self.assertIsNotNone(Dungeon.get_instance())
        self.assertIsNotNone(Inventory.get_instance())
        self.assertEqual(Hero.get_instance().get_name(), "name")
        self.assertEqual(Hero.get_instance().get_element(), Element.EARTH)

        Dungeon.delete_instance()
    def test_dungeon_delete_instance(self):
        Dungeon(False, ["name", Element.EARTH])

        Dungeon.delete_instance()

        self.assertIsNone(Dungeon.get_instance())
        self.assertIsNone(Hero.get_instance())
        self.assertIsNone(Inventory.get_instance())

    def test_dungeon_constructor_hold_the_pickles(self):
        Dungeon(False, ["name", Element.EARTH])

        self.assertIsNotNone(Dungeon.get_instance())
        self.assertIsNotNone(Inventory.get_instance())
        self.assertEqual(Hero.get_instance().get_name(), "name")
        self.assertEqual(Hero.get_instance().get_element(), Element.EARTH)
        self.assertEqual(Hero.get_instance().get_x(), -100)
        self.assertEqual(Hero.get_instance().get_y(), -100)

        Dungeon.delete_instance()

    def test_dungeon_constructor_extra_pickles(self):
        Dungeon(False, ["name", Element.EARTH])

        SaveLoad.save_game(Dungeon.pickle_dungeon(), "test")
        Dungeon.delete_instance()
        pickle_info = SaveLoad.load_game("test")

        Dungeon(True, pickle_info[0], pickle_info[1], pickle_info[2])

        self.assertIsNotNone(Dungeon.get_instance())
        self.assertIsNotNone(Inventory.get_instance())
        self.assertEqual(Hero.get_instance().get_name(), "name")
        self.assertEqual(Hero.get_instance().get_element(), Element.EARTH)
        self.assertEqual(Hero.get_instance().get_x(), -100)
        self.assertEqual(Hero.get_instance().get_y(), -100)

        Dungeon.delete_instance()

    def test_dungeon_pickle(self):
        Dungeon(False, ["name", Element.EARTH])

        Inventory.get_instance().add(InheritancePillar())
        Inventory.get_instance().add(VisionPotion())
        Inventory.get_instance().add(HealthPotion())

        pickle_info = Dungeon.pickle_dungeon()
        hero_info = pickle_info[0]
        maze_info = pickle_info[1]
        inventory_info = pickle_info[2]

        self.assertEqual(hero_info[0], "name")
        self.assertEqual(hero_info[1], Element.EARTH)
        self.assertEqual(hero_info[2], Hero.get_instance().get_hp())
        self.assertEqual(hero_info[3], Hero.get_instance().get_max_hp())
        self.assertEqual(hero_info[4], -100)
        self.assertEqual(hero_info[5], -100)
        self.assertIsInstance(maze_info[0][0][0], Room)
        self.assertIsInstance(inventory_info[0], Pillar)
        self.assertIsInstance(inventory_info[1], VisionPotion)
        self.assertIsInstance(inventory_info[2], HealthPotion)

        Dungeon.delete_instance()
