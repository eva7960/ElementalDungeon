from abc import ABC

import pygame

from Model.Element import Element
from random import randint

"""
Character Interface for all state and behavior that
both heroes and monsters have such as attacks, HP, images,
agility, etc.
"""

class CharacterInterface(ABC):
    """
    Static fields for all characters. Both monsters and heroes
    deal 5 points damage for a basic attack and 10 for a special
    attack, not including modifiers the hero can add from finding pillars.
    """
    BASIC_DAMAGE = 5
    SPECIAL_DAMAGE = 10

    """
    Constructor for abstract base class for character object,
    passes incoming parameters to a setter method to check that
    incoming data is valid.
    
    @param name of the character
    @param image for the character (GUI)
    @param hit image for character (Battle GUI)
    @param dead image for character (Battle GUI)
    @param max hit points(hp) the character can have
    @param agility score of the character, determines if an attack hits
    @param element of the character, enumerated element type
    """
    def __init__(self, name, image, hit_image, dead_image, max_hp, agility, element):
        self.set_name(name)
        self.set_image(image)
        self.set_hit_image(hit_image)
        self.set_dead_image(dead_image)
        self.set_max_hp(max_hp)
        self.set_agility(agility)
        self.set_element(element)


    """
    Checks that name string is not null and sets field to name
    @param name
    """
    def set_name(self, name):
        if name is not None:
            self.name = name
        else:
            print("Name string is null")

    """
    Checks that image is not null and sets field to image
    @param image string format
    """
    def set_image(self, image):
        if image is not None:
            self.image = image
        else:
            print("Image string is null")

    """
    Checks that hit image is not null and sets field to image
    @param image string format
    """
    def set_hit_image(self, image):
        if image is not None:
            self.hit_image = image
        else:
            print("Image string is null")

    """
    Checks that dead image is not null and sets field to image
    @param image string format
    """
    def set_dead_image(self, image):
        if image is not None:
            self.dead_image = image
        else:
            print("Image string is null")

    """
    Checks that number for maxHP passed in is a number greater than 0
    and sets character's max HP to that number
    @param number for max HP
    """
    def set_max_hp(self, max_hp):
        if isinstance(max_hp,int) and max_hp > 0:
            self.max_hp = max_hp
            self.set_hp(max_hp)
        else:
            print("Max HP must be an int and cannot be 0 or negative")


    """
    Checks that number passed in is greater than or equal to 0 and less
    than or equal to max HP
    @param number for HP
    """
    def set_hp(self, hp):
        if isinstance(hp,int) and 0 <= hp <= self.max_hp:
            self.hp = hp
        else:
            print("HP must be an int and cannot be 0 or negative or higher than MaxHP")


    """
    Checks that agility is greater than 0 and sets agility field to that number
    @param agility for character
    """
    def set_agility(self, agility):
        if isinstance(agility,int) and agility > 0:
            self.agility = agility
        else:
            print("Agility must be an int and cannot be 0 or negative")

    """
    Checks that element passed in is one of the Enums specified in Element
    class and makes it character's element
    @param Element as Enum (e.g. Element.EARTH)
    """
    def set_element(self, element):
        if isinstance(element, Element):
            self.element = element
        else:
            print(f"{element} is not an Element.")


    """
    Gets name of character
    @return name
    """
    def get_name(self):
        return self.name

    """
    Gets character image
    @return idle image for character
    """
    def get_image(self):
        return self.image

    """
    Gets hit image for character
    @return hit image
    """
    def get_hit_image(self):
        return self.hit_image

    """
    Gets dead image for character
    @return dead image
    """
    def get_dead_image(self):
        return self.dead_image

    """
    Gets max HP of character
    @return max HP
    """
    def get_max_hp(self):
        return self.max_hp

    """
    Gets HP for character
    @return current HP
    """
    def get_hp(self):
        return self.hp

    """
    Gets agility of character
    @return agility
    """
    def get_agility(self):
        return self.agility

    """
    Gets character's element
    @return element as Enum
    """
    def get_element(self):
        return self.element

    """
    Returns opposite of character's element (e.g. Earth and Air, Fire and Water)
    @return opposite element as Enum
    """
    def get_opposite_element(self):
        return self.element.get_opposite()


    """
    When a character uses its basic attack, it sends the character
    it is attacking a tuple containing the value of the attack so 
    the other player can determine if they can dodge the attack
    and the amount of damage (5) the attack will do if it lands.
    """
    def attack(self):
        return randint(1, 20), 5

    """
    When a character uses its special attack, it sends the character
    it is attacking a tuple containing the value of the attack (which
    is decreased by 3 because it is less likely to hit) so 
    the other player can determine if they can dodge the attack
    and the amount of damage (10) the attack will do if it lands.
    """
    def special_attack(self):
        return (randint(1, 20) - 3), 10
