from Model.CharacterInterface import CharacterInterface

"""
Hero implements Character Interface and Singleton Design
Pattern. Hero and has methods to attack and help navigate 
dungeon in controller code
"""
class Hero(CharacterInterface):
    __instance = None #single instance
    damage_mod = 0
    attack_mod = 0
    x = 0 #coordinates for camera and determining which room hero is in
    y = 0 #coordinates for camera and determining which room here is in
    drank_vision_potion = False #used for vision potions to expand sight radius

    """
    returns single instance of Hero if applicable
    @return Hero
    """
    @staticmethod
    def get_instance():
        return Hero.__instance

    """
    Deletes instance of Hero
    """
    @staticmethod
    def delete_instance():
        Hero.__instance = None

    """
    Constructor for hero checks if hero exists already and if not it calls constructor in 
    CharacterInterface to create Hero
    
    @param name
    @param hit image
    @param dead image
    @param max HP
    @param agility
    @param element
    """
    def __init__(self, name, image, hit_image, dead_image, max_hp, agility, element):
        if Hero.__instance is not None:
            raise Exception("Hero already exists!")
        else:
            super().__init__(name, image, hit_image, dead_image, max_hp, agility, element)
            Hero.__instance = self

    """
    Returns a tuple where the first number is the randomly generated
    number 1-20 from super attack method plus the attack modifer. The second
    number is the amount of damage (5 for a basic attack) plus the damage modifier if
    applicable.
    
    @return attack outcome (chance, damage)
    """
    def attack(self):
        pre_mod = super().attack()
        mod = (pre_mod[0] + self.attack_mod, pre_mod[1] + self.damage_mod)
        return mod

    """
   Returns a tuple where the first number is the randomly generated
   number 1-20 from super special attack method plus the attack modifer. The second
   number is the amount of damage (5 for a basic attack) plus the damage modifier if
   applicable.

   @return special attack outcome (chance, damage)
    """
    def special_attack(self):
        pre_mod = super().special_attack()
        mod = (pre_mod[0] + self.attack_mod, pre_mod[1] + self.damage_mod)
        return mod

    """
    Sets attack mod, used for when encapsulation pillar found
    @param attack mod int
    """

    def set_attack_mod(self, attack_mod):
        if isinstance(attack_mod, int) and attack_mod > 0:
            self.attack_mod = attack_mod
        else:
            raise ValueError("Attack modifier must be an int and cannot be 0 or negative")

    """
    sets damage mod, used for when abstraction pillar found
    @param damage mod int
    """
    def set_damage_mod(self, damage_mod):
        if isinstance(damage_mod, int) and damage_mod > 0:
            self.damage_mod = damage_mod
        else:
            raise ValueError("Damage modifier must be an int and cannot be 0 or negative")

    """
    Checks that x is an int and updates x coordinate
    @param x coordinate
    """
    def set_x(self, x):
        if isinstance(x, int):
            self.x = x
        else:
            raise ValueError(x, "is not an integer")

    """
    Checks that y is an int and updates y coordinate
    @param y coordinate
    """
    def set_y(self, y):
        if isinstance(y, int):
            self.y = y
        else:
            raise ValueError(y, "is not an integer")

    """
    If hero drinks vision potion this setter method is used
    to mark drank_vision_potion to true
    @param value is boolean for if hero drank vision potion
    """
    def set_vision_status(self, value):
        if isinstance(value, bool):
            self.drank_vision_potion = value
        else:
            raise ValueError("Parameter needs to be a boolean")

    """
    Gets damage mod
    @return damage mod
    """
    def get_damage_mod(self):
        return self.damage_mod

    """
    Gets attack mod
    @return attack mod
    """
    def get_attack_mod(self):
        return self.attack_mod

    """
    Gets x coordinate
    @return x coordinate
    """
    def get_x(self):
        return self.x

    """
    Gets y coordinate
    @return y coordinate
    """
    def get_y(self):
        return self.y

    """
    Gets whether hero drank vision potion
    @return boolean of whether hero drank vision potion
    """
    def get_drank_vision_potion(self):
        return self.drank_vision_potion


