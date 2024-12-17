import sqlite3
from Model.Monster import Monster
from Model.Hero import Hero

"""
Factory class that creates monsters and heroes from SQLite database
"""

class CharacterFactory:
    """
    Static method that creates an elemental monster based on element
    passed in, all other data for monster is retrieved from the database
    and used to call constructor in Monster class

    @param element for monster
    @return Monster object of specific element
    """
    @staticmethod
    def create_monster(element):
        element_val = element.value
        con = sqlite3.connect('Assets/character.db')
        cur = con.cursor()
        sql_query = f"SELECT name, image, hit_image, dead_image, max_health, agility FROM monster WHERE element = {element_val}"
        cur.execute(sql_query)
        result = cur.fetchone()
        if result:
            name, image, hit_image, dead_image, max_hp, agility = result
            element = element
            con.close()
            return Monster(name, image, hit_image, dead_image, max_hp, agility, element)
        else:
            con.close()
            raise ValueError(f"No monster found for element {element_val}")

    """
    Static method that constructs a hero using the name and element passed in.
    All other data is retrieved from the database.
    
    @param Hero name and element
    @return Hero object
    """
    @staticmethod
    def create_hero(name, element):
        element_val = element.value
        con = sqlite3.connect('Assets/character.db')
        cur = con.cursor()
        sql_query = f"SELECT image, hit_image, dead_image, max_health, agility FROM hero WHERE element = {element_val}"
        cur.execute(sql_query)
        result = cur.fetchone()
        if result:
            image, hit_image, dead_image, max_hp, agility = result
            element = element
            con.close()
            return Hero(name, image, hit_image, dead_image, max_hp, agility, element)
        else:
            con.close()
            raise ValueError(f"No hero found for element {element_val}")
