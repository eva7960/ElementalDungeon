from Model.CharacterFactory import CharacterFactory
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Maze import Maze

"""
Dungeon follows a Singleton Design pattern and
instantiates the Hero and Maze
"""
class Dungeon:
    __instance = None
    """
    Returns instance of Dungeon if applicable
    """
    @staticmethod
    def get_instance():
        return Dungeon.__instance

    """
    Delete method to delete instance of dungeon,
    this is used when player plays again, effecively
    deleting other single instances such as Hero, Inventory, and Maze
    """
    @staticmethod
    def delete_instance():
        Dungeon.__instance = None
        Hero.delete_instance()
        Inventory.delete_instance()
        Maze.delete_instance()


    """
    Constructor for dungeon instantiates a Maze, Inventory, and Hero. For pickling
    purposes we keep track of Hero state in maze.
    
    @param from_pickle information from saved state
    @param hero_info information about hero 
    @param maze_info information about hero
    @param inventory_info information about inventory
    """
    def __init__(self, from_pickle, hero_info, maze_info=None, inventory_info=None):
        if not Dungeon.__instance is None:
            Dungeon.delete_instance()
        Maze(6)
        Inventory()
        CharacterFactory.create_hero(hero_info[0], hero_info[1])
        Hero.get_instance().set_x(-100)
        Hero.get_instance().set_y(-100)

        if from_pickle:
            Maze.get_instance().set_array(maze_info[0])
            Hero.get_instance().set_max_hp(hero_info[2])
            Hero.get_instance().set_hp(hero_info[3])
            Hero.get_instance().set_x(hero_info[4])
            Hero.get_instance().set_y(hero_info[5])
            for item in inventory_info:
                Inventory.get_instance().add(item)
        Dungeon.__instance = self

    """
    Static method for pickling the dungeon, all current information about
    hero, inventory, and maze are stored in lists
    """
    @staticmethod
    def pickle_dungeon():
        hero_info = [Hero.get_instance().get_name(), Hero.get_instance().get_element(), Hero.get_instance().get_max_hp(),
                     Hero.get_instance().get_hp(),
                     Hero.get_instance().get_x(), Hero.get_instance().get_y()]
        maze_info = [Maze.get_instance().get_array()]
        inventory_info = []
        for item in Inventory.get_instance().get_pillars():
            inventory_info.append(item)
        for item in Inventory.get_instance().get_vision_potions():
            inventory_info.append(item)
        for item in Inventory.get_instance().get_health_potions():
            inventory_info.append(item)
        return hero_info, maze_info, inventory_info