
"""
Room object used in maze, a room can have up to 4 walls,
a monster, a potion, and a location.
"""
class Room:
    """
    constructor for the room class takes in booleans for each of the walls,
    a potion, a monster, and a location. Additionally, it sets fields for has_visited,
    hero_has_visited, and has_exit to false, this is for when the hero finds all pillars and
    for minimap feature.

    @param northWall
    @param southWall
    @param eastWall
    @param westWall
    @param location
    @param potion
    @param monster
    """
    def __init__(self,northWall,southWall,eastWall,westWall,location,potion,monster):
        #boolean values for if a wall exists
        self.set_nwall(northWall)
        self.set_ewall(eastWall)
        self.set_swall(southWall)
        self.set_wwall(westWall)
        self.set_potion(potion)
        self.set_monster(monster)
        self.set_location(location)
        self.has_visited = False
        self.hero_has_visited = False
        self.has_exit = False

        """
    Sets the value of the north wall.

    @param wall boolean indicating whether the north wall exists.
    """
    def set_nwall(self, wall):
        if wall is not None:
            self.northWall = wall
        else:
            print("Wall value is null.")

    """
    Sets the value of the south wall.

    @param wall boolean indicating whether the south wall exists.
    """
    def set_swall(self, wall):
        if wall is not None:
            self.southWall = wall
        else:
            print("Wall value is null.")

    """
    Sets the value of the east wall.

    @param wall boolean indicating whether the east wall exists.
    """
    def set_ewall(self, wall):
        if wall is not None:
            self.eastWall = wall
        else:
            print("Wall value is null.")

    """
    Sets the value of the west wall.

    @param wall boolean indicating whether the west wall exists.
    """
    def set_wwall(self, wall):
        if wall is not None:
            self.westWall = wall
        else:
            print("Wall value is null.")

    """
    Sets the monster present in the room.

    @param monster the Monster object to be placed in the room.
    """
    def set_monster(self, monster):
        self.monster = monster

    """
    Sets the potion present in the room.

    @param potion the Potion object to be placed in the room.
    """
    def set_potion(self, potion):
        self.potion = potion

    """
    Sets the location of the room.

    @param location a tuple (col, row) representing the room's coordinates.
    """
    def set_location(self, location):
        if location is not None:
            self.location = location
        else:
            print("Location value is null.")

    """
    Sets the visitation status of the room.

    @param visited a boolean indicating whether the room has been visited.
    """
    def set_has_visited(self, visited):
        if isinstance(visited, bool) and visited is not None:
            self.has_visited = visited
        else:
            print("Visited status needs to be a boolean.")

    """
    Sets whether the hero has visited the room.

    @param visited a boolean indicating whether the hero has visited the room.
    """
    def set_hero_has_visited(self, visited):
        if isinstance(visited, bool) and visited is not None:
            self.hero_has_visited = visited
        else:
            print("Visited status needs to be a boolean.")

    """
    Sets whether the room has an exit.

    @param exit_door a boolean indicating whether the room has an exit.
    """
    def set_has_exit(self, exit_door):
        if isinstance(exit_door, bool) and exit_door is not None:
            self.has_exit = exit_door
        else:
            print("Exit status needs to be a boolean.")

    """
    Retrieves the status of the north wall.

    @return boolean True if the north wall exists, False otherwise.
    """
    def get_nwall(self):
        return self.northWall

    """
    Retrieves the status of the south wall.

    @return boolean True if the south wall exists, False otherwise.
    """
    def get_swall(self):
        return self.southWall

    """
    Retrieves the status of the east wall.

    @return boolean True if the east wall exists, False otherwise.
    """
    def get_ewall(self):
        return self.eastWall

    """
    Retrieves the status of the west wall.

    @return boolean True if the west wall exists, False otherwise.
    """
    def get_wwall(self):
        return self.westWall

    """
    Retrieves the location of the room.

    @return tuple the (col, row) coordinates of the room.
    """
    def get_location(self):
        return self.location

    """
    Retrieves the potion in the room.

    @return Potion the potion object in the room.
    """
    def get_potion(self):
        return self.potion

    """
    Retrieves the monster in the room.

    @return Monster the monster object in the room.
    """
    def get_monster(self):
        return self.monster

    """
    Checks if the room has been visited.

    @return boolean True if the room has been visited, False otherwise.
    """
    def get_has_visited(self):
        return self.has_visited

    """
    Checks if the hero has visited the room.

    @return boolean True if the hero has visited the room, False otherwise.
    """
    def get_hero_has_visited(self):
        return self.hero_has_visited
