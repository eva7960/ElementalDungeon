from random import randint

from Model.CharacterInterface import CharacterInterface
from Model.Potion import HealthPotion, VisionPotion

""""
Monster implements Character interface to create monster
"""
class Monster(CharacterInterface):
    """
    Constructor calls super class for basic information such as name and maxHP,
    monster also has the ability to have a health potion, vision potion, and pillar, this
    is probability is randomly generated.

    @param name
    @param image
    @param hit_image
    @param dead_image
    @param max_hp
    @param agility
    @param element
    """
    def __init__(self, name, image, hit_image, dead_image, max_hp, agility, element):
        super().__init__(name, image, hit_image, dead_image, max_hp, agility, element)
        self.hp = max_hp
        self.pillar = None
        self.health_potion = None
        self.vision_potion = None
        num1 = randint(1,10)
        num2 = randint(1,10)
        if num1 > 4:
            self.health_potion = HealthPotion()
        if num2 > 4:
            self.vision_potion = VisionPotion()

    """
    Calls attack from super class
    @returns tuple with chance to hit and damage
    """
    def attack(self):
        return super().attack()

    """
    Calls special attack from super class
    @returns a tuple with chance to hit and damage
    """
    def special_attack(self):
        return super().special_attack()

    """
    Monster has a 50% chance to heal, random number from 1-20 is generated
    and if that number is greater than 10 the monster regains 10HP.
    
    @return boolean whether monster healed
    """
    def heal(self):
        did_heal = False
        roll = randint(1,20)
        if roll > 10 and self.get_hp() <= (self.get_max_hp() - 5):
            self.set_hp(self.get_hp() + 5)
            did_heal = True
        return did_heal

    """
    Get image for monster
    @return image
    """
    def get_image(self):
        return self.image

    """
    Get current HP for monster
    @return HP
    """
    def get_hp(self):
        return self.hp

    """
    Returns pillar held by monster
    @return pillar
    """
    def get_pillar(self):
        if self.has_pillar():
            return self.pillar
        else:
            raise ValueError("Monster has no pillar!")

    """
    Returns health potion held by monster
    @return health potion
    """
    def get_health_potion(self):
        if self.has_health_potion():
            return self.health_potion
        else:
            raise ValueError("Monster has no health potion!")

    """
    Returns vision potion held by monster
    @return vision potion
    """
    def get_vision_potion(self):
        if self.has_vision_potion():
            return self.vision_potion
        else:
            raise ValueError("Monster has no vision potion!")

    """
    Return whether monster has health potion
    @return boolean if monster has health potion
    """
    def has_health_potion(self):
        return self.health_potion is not None

    """
    Return whether monster has vision potion
    @return boolean if monster has vision potion
    """
    def has_vision_potion(self):
        return self.vision_potion is not None

    """
    Return whether monster has pillar
    @return boolean if monster has pillar
    """
    def has_pillar(self):
        return self.pillar is not None

    """"
    Sets pillar to instance field of monster
    @param pillar
    """
    def set_pillar(self, pillar):
        self.pillar = pillar
