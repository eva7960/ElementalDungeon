import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from Model.Pillar import AbstractionPillar, PolymorphismPillar, InheritancePillar, EncapsulationPillar

class TestPillars(unittest.TestCase):
    CharacterFactory.create_hero("hero", Element.EARTH)
    def setUp(self):
        # Singleton Hero instance
        self.hero = Hero.get_instance()
        self.hero.set_hp(50)
        self.hero.set_max_hp(100)
        self.hero.set_vision_status(False)

    def test_abstraction_pillar_initialization(self):
        pillar = AbstractionPillar()
        self.assertEqual(pillar.get_name(), "abstraction")
        self.assertEqual(pillar.get_image(), "abstraction_pillar.png")

    def test_polymorphism_pillar_initialization(self):
        pillar = PolymorphismPillar()
        self.assertEqual(pillar.get_name(), "polymorphism")
        self.assertEqual(pillar.get_image(), "polymorphism_pillar.png")

    def test_inheritance_pillar_initialization(self):
        pillar = InheritancePillar()
        self.assertEqual(pillar.get_name(), "inheritance")
        self.assertEqual(pillar.get_image(), "inheritance_pillar.png")

    def test_encapsulation_pillar_initialization(self):
        pillar = EncapsulationPillar()
        self.assertEqual(pillar.get_name(), "encapsulation")
        self.assertEqual(pillar.get_image(), "encapsulation_pillar.png")

    def test_restore_health(self):
        abstraction_pillar = AbstractionPillar()
        abstraction_pillar.restore_health()
        self.assertEqual(self.hero.get_hp(), self.hero.get_max_hp())

    def test_enhance_abstraction_pillar(self):
        pillar = AbstractionPillar()
        original_damage_mod = self.hero.get_damage_mod()
        pillar.enhance()
        self.assertEqual(self.hero.get_damage_mod(), original_damage_mod + 5)

    def test_enhance_polymorphism_pillar(self):
        pillar = PolymorphismPillar()
        original_max_hp = self.hero.get_max_hp()
        pillar.enhance()
        self.assertEqual(self.hero.get_max_hp(), original_max_hp + 10)

    def test_enhance_inheritance_pillar(self):
        pillar = InheritancePillar()
        original_attack_mod = self.hero.get_attack_mod()
        pillar.enhance()
        self.assertEqual(self.hero.get_attack_mod(), original_attack_mod + 2)

    def test_enhance_encapsulation_pillar(self):
        pillar = EncapsulationPillar()
        original_agility = self.hero.get_agility()
        pillar.enhance()
        self.assertEqual(self.hero.get_agility(), original_agility + 4)