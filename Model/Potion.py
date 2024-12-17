from abc import ABC, abstractmethod
from Model.Hero import Hero

"""
The abstract potion class for both the health and 
vision potions.
"""


class Potion(ABC):
    """
    Constructor for abstract base class of potion
    @param image is the image for the potion
    """

    def __init__(self, name, image):
        self.name = name
        self.image = image
    """
    return name of potion i.e health or vision
    """
    def get_name(self):
        return self.name

    """
    gets image for the potion
    @return image returns the image
    """
    def get_image(self):
        return self.image

    """
    the drink method used to determine when to remove the potion 
    from the inventory
    """
    @abstractmethod
    def drink(self):
        pass


"""
The healthPotion child class of the Potion ABC
"""

class HealthPotion(Potion):
    """
    Constructs health potion calling super class and passes
    health name and health potion image to constructor since
    all health potions have the same name and image
    """
    def __init__(self):
        super().__init__("health", "health_potion.png")

    """
    Checks to see if hero's HP plus 10 is greater than the max HP in which case
    it will set the hero's HP to max HP since the current HP cannot exceed max HP.
    Otherwise it just restores 10 HP to hero.
    """
    def drink(self):
        if Hero.get_instance().get_hp() + 10 > Hero.get_instance().get_max_hp():
            Hero.get_instance().set_hp(Hero.get_instance().get_max_hp())
        else:
            Hero.get_instance().set_hp(Hero.get_instance().get_hp() + 10)

"""
the vision potion child class of the Potion ABC
"""

class VisionPotion(Potion):
    """
    Constructor for Vision potion calls parent class and passes in
    name and image since all vision potions will have the same name and image
    """
    def __init__(self):
        super().__init__("vision", "vision_potion.png")

    """
    Drinking a vision potion sets the hero field indicating if they drank a 
    vision potion to true.
    """
    def drink(self):
        Hero.get_instance().set_vision_status(True)
