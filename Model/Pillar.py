from abc import ABC, abstractmethod
from Model.Hero import Hero


class Pillar(ABC):

    """
    Construction for abstract base class for pillar object,
    passes incoming parameters to a setter method to check that
    incoming data is valid.

    @param name of OO pillar
    @param image for that pillar (GUI)
    @param hero reference so pillars can give hero perks
    """
    def __init__(self, name, image):
        self.name = name
        self.image = image

    """
    Returns name of pillar
    @return name
    """
    def get_name(self):
        return self.name

    """
    Returns image of pillar
    @return image
    """
    def get_image(self):
        return self.image

    """
    Every time hero finds pillar it fully heals the hero
    """
    def restore_health(self):
        Hero.get_instance().set_hp(Hero.get_instance().get_max_hp())

    """
    Abstract method that all subclasses have to implement,
    each pillar gives the hero a different perk
    """
    @abstractmethod
    def enhance(self):
        pass



"""
Abstraction pillar adds +5 damage to basic and special attack
"""
class AbstractionPillar(Pillar):
    def __init__(self):
        super().__init__("abstraction", "abstraction_pillar.png")
    def enhance(self):
        self.restore_health()
        Hero.get_instance().set_damage_mod(Hero.get_instance().get_damage_mod() + 5)


"""
Polymorphism pillar increases hero's max health by 10
"""
class PolymorphismPillar(Pillar):
    def __init__(self):
        super().__init__("polymorphism", "polymorphism_pillar.png")
    def enhance(self):
        self.restore_health()
        Hero.get_instance().set_max_hp(Hero.get_instance().get_max_hp() + 10)


"""
Inheritance pillar does +2 hit chance
"""
class InheritancePillar(Pillar):
    def __init__(self):
        super().__init__("inheritance", "inheritance_pillar.png")
    def enhance(self):
        self.restore_health()
        Hero.get_instance().set_attack_mod(Hero.get_instance().get_attack_mod() + 2)

"""
Encapsulation pillar adds +4 to hero's agility stat
"""
class EncapsulationPillar(Pillar):
    def __init__(self):
        super().__init__("encapsulation", "encapsulation_pillar.png")
    def enhance(self):
        self.restore_health()
        Hero.get_instance().set_agility(Hero.get_instance().get_agility() + 4)

