from Model.Potion import HealthPotion, VisionPotion
from Model.Pillar import PolymorphismPillar, EncapsulationPillar, InheritancePillar, AbstractionPillar

"""
Inventory follows Singleton Design Pattern and handles
adding and deleting potions and pillars as hero navigates dungeon
"""
class Inventory:
    __instance = None

    """
    Returns instance of inventory
    @return inventory
    """
    @staticmethod
    def get_instance():
        return Inventory.__instance

    """
    Deletes instance of inventory
    """
    @staticmethod
    def delete_instance():
        Inventory.__instance = None

    """
    Constructs inventory object and instantiates 3 empty lists to hold
    health potions, vision potions, and pillars. Constructor also checks 
    that inventory does not already exist.
    """
    def __init__(self):
        if Inventory.__instance is not None:
            raise Exception("Inventory already exists!")
        else:
            self.health_potions = []
            self.vision_potions = []
            self.pillars = []
            Inventory.__instance = self

    """
    Adds potions and pillars to inventory by checking what type of
    object is being added and adding it to the right list. If the object
    is a pillar it calls the enhance method to give the hero a specific perk.
    
    @param object is a pillar, health, or vision potion
    """
    def add(self, object):
        if object is not None:
            if (isinstance(object, PolymorphismPillar)
                    or isinstance(object, EncapsulationPillar)
                    or isinstance(object, InheritancePillar)
                    or isinstance(object, AbstractionPillar)):
                self.pillars.append(object)
                object.enhance()
            elif isinstance(object, HealthPotion) or isinstance(object, VisionPotion):
                if object.get_name() == "health":
                    self.health_potions.append(object)
                else:
                    self.vision_potions.append(object)
        else:
            raise ValueError("Cannot add null object to inventory")

    """
    returns if inventory has health potions
    @return boolean if there are health potions
    """
    def has_health_potion(self):
        return len(self.health_potions) > 0

    """
    returns number of health potions in inventory
    @return number of health potions
    """
    def number_of_health_potions(self):
        return len(self.health_potions)

    """
    Returns whether there are vision potions in inventory
    @return boolean of whether there are vision potions
    """
    def has_vision_potion(self):
        return len(self.vision_potions) > 0

    """
    Checks to see if there are any health potions and if so, uses
    health potion and deletes from the list of health potions.
    """
    def drink_health_potion(self):
        if self.has_health_potion():
            self.health_potions[-1].drink()
            self.health_potions.pop()

    """
    Checks for vision potions in list, if so it uses up a vision potion
    and discards from list.
    """
    def drink_vision_potion(self):
        if len(self.vision_potions) > 0:
            self.vision_potions[-1].drink()
            self.vision_potions.pop()

    """
    Returns whether hero has all 4 pillars
    @return boolean hero has 4 pillars
    """
    def has_all_pillars(self):
        return len(self.pillars) == 4

    """
    Returns pillar list
    @return pillar list
    """
    def get_pillars(self):
        return self.pillars
    """
    Returns health potion lists
    @return health potion lists
    """
    def get_health_potions(self):
        return self.health_potions

    """
    Returns vision potion lists
    @return vision potion list
    """
    def get_vision_potions(self):
        return self.vision_potions
