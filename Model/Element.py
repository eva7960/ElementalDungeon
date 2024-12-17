from enum import Enum
"""
Class represents Elements as Enumerated Types
"""
class Element(Enum):
    EARTH = 1
    FIRE = 2
    AIR = 3
    WATER = 4

    """
    Method that returns the opposite element of 
    object's element passed in.
    
    @return opposite element
    """
    def get_opposite(self):
        return opposites[self]
opposites = {
             Element.EARTH: Element.AIR,
             Element.FIRE: Element.WATER,
             Element.AIR: Element.EARTH,
             Element.WATER:Element.FIRE
            }