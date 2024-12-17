import pygame

from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Maze import Maze

# Initialize pygame
pygame.init()

# Constants

DEFAULT_SIZE = 0
HEIGHT = 0
ROOM_SIZE = 0
WIDTH = 0
"""
A method for setting up the constants in dungeon view.

@param screen the screen that will be drawn on
"""
def set_up(screen):
    global WIDTH
    global HEIGHT
    global DEFAULT_SIZE
    global ROOM_SIZE

    WIDTH, HEIGHT = screen.get_size()
    #This is the size of one wall block, each wall should need 6
    DEFAULT_SIZE = WIDTH // 18
    ROOM_SIZE = WIDTH // 3

"""
A method for calculating the camera offset based on the Hero's coordinates.
This keeps Hero centered in the middle of the screen.
"""
def get_camera_offset():
    x_min = max(0, Hero.get_instance().get_x() - WIDTH // 2)
    y_min = max(30, Hero.get_instance().get_y() - HEIGHT // 2)
    camera_offset_x = min(ROOM_SIZE*3, x_min)
    camera_offset_y = min(ROOM_SIZE*3 + 30, y_min)
    return camera_offset_x, camera_offset_y

"""
A method for drawing the Hero and their pillar companions.
Returns the rect for Hero

@param screen the screen to draw the Hero on
"""
def draw_hero(screen):
    camera_offset_x, camera_offset_y = get_camera_offset()

    # Draw Hero
    hero_img = pygame.image.load("Assets/" + Hero.get_instance().get_image())
    scaled_hero = pygame.transform.scale(hero_img, (DEFAULT_SIZE, DEFAULT_SIZE))
    img_x = Hero.get_instance().get_x() - camera_offset_x
    img_y = Hero.get_instance().get_y() - camera_offset_y
    screen.blit(scaled_hero, (img_x, img_y))

    # Draws pillars if applicable
    current_pillars = Inventory.get_instance().get_pillars()
    if len(current_pillars) > 0:
        locations = [(img_x -8, img_y- 30),
                     (img_x + 27, img_y -30),
                     (img_x - 30, img_y),
                     (img_x + 50, img_y)
                     ]
        i = 0
        for pillar in current_pillars:
            img = pygame.image.load("Assets/" + pillar.get_image())
            scaled_img = pygame.transform.scale(img, (30,30))
            screen.blit(scaled_img, (locations[i]))
            i+=1
    return scaled_hero.get_rect()

"""
A method for drawing a Room. 
Returns a list of rects that make up a Room for collisions

@param screen the screen to draw the Room on
@room the Room to draw
"""
def draw_room(screen, room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    rect_list = []

    # Calculate where the room should be drawn
    x = room.get_location()[0] * ROOM_SIZE - camera_offset_x
    y = room.get_location()[1] * ROOM_SIZE + DEFAULT_SIZE - camera_offset_y

    # Draw floor and corners, same for every room
    floor = pygame.image.load('Assets/floor.png')
    floor_img = pygame.transform.scale(floor, (ROOM_SIZE, ROOM_SIZE))
    floor_rect = floor_img.get_rect()
    screen.blit(floor_img, (x, y))
    corner = pygame.image.load('Assets/corner.png')
    corner = pygame.transform.scale(corner, (DEFAULT_SIZE, DEFAULT_SIZE))
    screen.blit(corner, (x, y))
    screen.blit(corner, (x + ROOM_SIZE - DEFAULT_SIZE, y))
    screen.blit(corner, (x, y + ROOM_SIZE - DEFAULT_SIZE))
    screen.blit(corner, (x + ROOM_SIZE - DEFAULT_SIZE, y + ROOM_SIZE -DEFAULT_SIZE))

    # Draw partial walls, all rooms have these
    wall = pygame.image.load('Assets/wall.png')
    vert_wall = pygame.transform.scale(wall, (DEFAULT_SIZE, DEFAULT_SIZE))
    horz_wall = pygame.transform.rotate(vert_wall, 90)
    default_vert_walls = [(x, y + DEFAULT_SIZE), #top left corner bottom
                     (x, y + ROOM_SIZE - 2*DEFAULT_SIZE), #bottom left corner top
                     (x + ROOM_SIZE - DEFAULT_SIZE, y + DEFAULT_SIZE),#top right corner bottom
                     (x + ROOM_SIZE - DEFAULT_SIZE, y + ROOM_SIZE- 2*DEFAULT_SIZE), #bottom right corner top
                     ]
    default_horz_walls = [(x + DEFAULT_SIZE, y), #top left corner right
                     (x + ROOM_SIZE - 2*DEFAULT_SIZE, y), #top right corner left
                     (x + DEFAULT_SIZE, y + ROOM_SIZE- DEFAULT_SIZE), #bottom left corner right
                     (x + ROOM_SIZE- 2*DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE) #bottom right corner left
                     ]

    # Add partial walls to rect list
    for location in default_vert_walls:
        rect = pygame.Rect(location[0], location[1], DEFAULT_SIZE, DEFAULT_SIZE)
        screen.blit(vert_wall, location)
        rect_list.append(rect)
    for location in default_horz_walls:
        rect = pygame.Rect(location[0], location[1], DEFAULT_SIZE, DEFAULT_SIZE)
        screen.blit(horz_wall, location)
        rect_list.append(rect)

    # Checks which walls should be completely blocked off
    if room.get_nwall():
        screen.blit(horz_wall, (x + 2*DEFAULT_SIZE, y))
        screen.blit(horz_wall, (x + ROOM_SIZE - 3*DEFAULT_SIZE, y))
        n_wall = pygame.Rect(x + DEFAULT_SIZE, y, ROOM_SIZE- 2*DEFAULT_SIZE, DEFAULT_SIZE)
        rect_list.append(n_wall)

    if room.get_wwall():
        screen.blit(vert_wall, (x, y + 2*DEFAULT_SIZE))
        screen.blit(vert_wall, (x, y + ROOM_SIZE - 3*DEFAULT_SIZE))
        w_wall = pygame.Rect(x, y + DEFAULT_SIZE, DEFAULT_SIZE, ROOM_SIZE - 2*DEFAULT_SIZE)
        rect_list.append(w_wall)

    if room.get_ewall():
        screen.blit(vert_wall, (x + ROOM_SIZE - DEFAULT_SIZE, y + 2*DEFAULT_SIZE))
        screen.blit(vert_wall, (x + ROOM_SIZE - DEFAULT_SIZE, y + ROOM_SIZE - 3*DEFAULT_SIZE))
        e_wall = pygame.Rect(x + ROOM_SIZE - DEFAULT_SIZE, y + DEFAULT_SIZE, DEFAULT_SIZE, ROOM_SIZE - 2*DEFAULT_SIZE)
        rect_list.append(e_wall)

    if room.get_swall():
        screen.blit(horz_wall, (x + 2*DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE))
        screen.blit(horz_wall, (x + ROOM_SIZE - 3*DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE))
        s_wall = pygame.Rect(x + DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE, ROOM_SIZE - 2*DEFAULT_SIZE, DEFAULT_SIZE)
        rect_list.append(s_wall)
    return rect_list


"""
A method for drawing the exit.
Returns the exit's rect or None of the Room does not have an exit

@param screen the screen to draw the exit on
@param room the Room to check for an exit
"""
def draw_exit(screen,room):
    camera_offset_x, camera_offset_y = get_camera_offset()

    #Check if the room has the exit
    if room.has_exit and Inventory.get_instance().has_all_pillars():
        x = room.get_location()[0] * ROOM_SIZE - camera_offset_x
        y = room.get_location()[1] * ROOM_SIZE +DEFAULT_SIZE -camera_offset_y
        door = pygame.image.load('Assets/exit_door.png')
        door_img = pygame.transform.scale(door, (DEFAULT_SIZE*2, DEFAULT_SIZE*2))
        door_rect = door_img.get_rect()
        door_rect.topleft = (x + (ROOM_SIZE/2) -45, y + (ROOM_SIZE/2)-45)
        screen.blit(door_img, (x + (ROOM_SIZE / 2) -45, y + (ROOM_SIZE / 2)-45))
        return door_rect
    else:
        return None

"""
A method for drawing a potion in a Room. 
Returns the potion's rect or None if the Room doesn't have a Potion

@param screen the screen to draw the Potion on
@param room the Room to check for a Potion
"""
def draw_potion(screen, room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    x = room.get_location()[0] * ROOM_SIZE - camera_offset_x
    y = room.get_location()[1] * ROOM_SIZE +DEFAULT_SIZE -camera_offset_y

    #Check if room has a potion
    if room.get_potion() is not None:
        potion = "Assets/" + room.get_potion().get_image()
        potion_img = pygame.image.load(potion)
        potion_rect = (potion_img.get_rect())
        potion_rect.topleft = (x + (ROOM_SIZE/2) -30, y + (ROOM_SIZE/2) -30)
        screen.blit(potion_img, (x + (ROOM_SIZE/2) -30, y + (ROOM_SIZE/2) -30))
        return potion_rect
    else:
        return None

"""
A method for drawing a monster in a Room. 
Returns the monsters rect or None if the Room doesn't have a monster

@param screen the screen to draw the Monster on
@param room the Room to check for a Monster
"""
def draw_monster(screen, room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    x = room.get_location()[0] * ROOM_SIZE - camera_offset_x
    y = room.get_location()[1] * ROOM_SIZE + DEFAULT_SIZE - camera_offset_y

    #Check if room has a monster
    if room.get_monster() is not None:
        monster = room.get_monster()
        monster_img = "Assets/" + monster.get_image()
        img = pygame.image.load(monster_img)
        monster_rect = pygame.Rect((x + (ROOM_SIZE/2) -30), (y + (ROOM_SIZE/2) -30),DEFAULT_SIZE*2, DEFAULT_SIZE*2)
        screen.blit(img, (x + (ROOM_SIZE/2) -30, y + (ROOM_SIZE/2) -30))
        return monster_rect
    else:
        return None

"""
A method for drawing a toolbar at the top of the screen during
the dungeon game.
Returns a list of rects for the toolbar's buttons

@param screen the screen to draw the toolbar on
"""
def draw_toolbar(screen):
    #Draw the toolbar
    font = pygame.font.Font('Assets/8-bit-pusab.ttf', 15)
    image = pygame.Surface((WIDTH, DEFAULT_SIZE / 1.5))
    image.fill((118,59,54))
    rect = image.get_rect()
    rect.topleft = (0, 0)
    screen.blit(image, rect)

    #Draw the buttons
    inventory_button = pygame.Rect(5,0,DEFAULT_SIZE*3, DEFAULT_SIZE)
    map_button = pygame.Rect(DEFAULT_SIZE * 4, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    save_button = pygame.Rect(DEFAULT_SIZE * 6, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    help_button = pygame.Rect(DEFAULT_SIZE * 8, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    quit_button = pygame.Rect(DEFAULT_SIZE * 10, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    rect_list = [inventory_button, map_button, save_button, help_button, quit_button]

    inventory_surface = font.render("Inventory", True, (255,255,255))
    map_surface = font.render("Map", True, (255, 255, 255))
    save_surface = font.render("Save", True, (255, 255, 255))
    help_surface = font.render("Help", True, (255, 255, 255))
    quit_surface = font.render("Quit", True, (255, 255, 255))

    screen.blit(inventory_surface, inventory_button)
    screen.blit(map_surface, map_button)
    screen.blit(save_surface, save_button)
    screen.blit(help_surface, help_button)
    screen.blit(quit_surface, quit_button)

    # Return the button rectangle for external use
    return rect_list

"""
A method for drawing the inventory at the top of the screen below the toolbar during
the dungeon game.
Returns a list of rects for the usable items in inventory

@param screen the screen to draw the inventory on
"""
def draw_inventory(screen):
    #Draw the inventory background
    row_height = 4*DEFAULT_SIZE
    font = pygame.font.Font('Assets/8-bit-pusab.ttf', 15)
    image = pygame.Surface((WIDTH, row_height))
    image.fill((250,197,143))
    rect = image.get_rect()
    rect.topleft = (0, DEFAULT_SIZE/1.5)
    screen.blit(image, rect)
    #Draw the labels
    potion_label = pygame.Rect(5, DEFAULT_SIZE/1.5 + DEFAULT_SIZE, DEFAULT_SIZE*2, DEFAULT_SIZE)
    pillar_label = pygame.Rect(5, DEFAULT_SIZE/1.5 + 3*DEFAULT_SIZE, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    potion_surface = font.render("Potions:", True, (255,255,255))
    pillar_surface = font.render("Pillars:", True, (255, 255, 255))
    screen.blit(potion_surface, potion_label)
    screen.blit(pillar_surface, pillar_label)

    #Draw the pillars in inventory
    current_pillars = Inventory.get_instance().get_pillars()
    i = 3
    for pillar in current_pillars:
        img = pygame.image.load("Assets/" + pillar.get_image())
        scaled_img = pygame.transform.scale(img, (30, 30))
        screen.blit(scaled_img, (DEFAULT_SIZE*i, DEFAULT_SIZE/1.5 + 3*DEFAULT_SIZE))
        i += 2

    #Draw the health potions in inventory
    health_rects = []
    current_health_potions = Inventory.get_instance().get_health_potions()
    i = 3
    for potion in current_health_potions:
        img = pygame.image.load("Assets/" + potion.get_image())
        scaled_img = pygame.transform.scale(img, (30, 30))
        rect = scaled_img.get_rect()
        rect.topleft = (DEFAULT_SIZE * i, DEFAULT_SIZE / 1.5 + DEFAULT_SIZE)
        screen.blit(scaled_img, (DEFAULT_SIZE * i, DEFAULT_SIZE / 1.5 + DEFAULT_SIZE))
        i += 2
        health_rects.append(rect)

    #Draw the vision potions in inventory
    vision_rects = []
    current_vision_potions = Inventory.get_instance().get_vision_potions()
    i = 3
    for potion in current_vision_potions:
        img = pygame.image.load("Assets/" + potion.get_image())
        scaled_img = pygame.transform.scale(img, (30, 30))
        rect = scaled_img.get_rect()
        rect.topleft = (DEFAULT_SIZE * i, DEFAULT_SIZE / 1.5 + 2*DEFAULT_SIZE)
        screen.blit(scaled_img, (DEFAULT_SIZE * i, DEFAULT_SIZE / 1.5 + 2*DEFAULT_SIZE))
        i += 2
        vision_rects.append(rect)

    # Return the button rectangle for external use
    return health_rects, vision_rects

"""
A method for drawing a black screen with a hole in the middle over the dungeon
so that the user can only see the immediate room around the hero.

@param screen the screen to draw the vision blocker on
"""
def draw_vision(screen):
    camera_offset_x, camera_offset_y = get_camera_offset()
    x_center = Hero.get_instance().get_x() - camera_offset_x
    y_center = Hero.get_instance().get_y() - camera_offset_y
    img = pygame.image.load('Assets/vision.png')

    screen.blit(img, (x_center - ROOM_SIZE*2.92,y_center - ROOM_SIZE*2.92))

"""
A method for drawing a a minimap of all the rooms Hero has visited

@param screen the screen to draw the minimap on
"""
def draw_mini_map(screen):
    #set up some variables for adjusting the size of the map vs the dungeon view
    mini_room_size = WIDTH // Maze.get_instance().size
    mini_default_size = mini_room_size//6
    hero_room_x= Hero.get_instance().get_x()//ROOM_SIZE
    hero_room_y = Hero.get_instance().get_y()//ROOM_SIZE
    screen.fill((0,0,0))

    # Draw all visited rooms at absolute position in the maze
    for i in range(len(Maze.get_instance().room_array)):
        for j in range(len(Maze.get_instance().room_array[i])):
            room = Maze.get_instance().room_array[i][j]
            if room.hero_has_visited:
                x = room.get_location()[0] * mini_room_size
                y = room.get_location()[1] * mini_room_size + 15

                # Draw floor and corners
                floor = pygame.image.load('Assets/floor.png')
                floor_img = pygame.transform.scale(floor, (mini_room_size, mini_room_size))
                screen.blit(floor_img, (x, y))
                corner = pygame.image.load('Assets/corner.png')
                corner = pygame.transform.scale(corner, (mini_default_size, mini_default_size))
                screen.blit(corner, (x, y))
                screen.blit(corner, (x + mini_room_size - mini_default_size, y))
                screen.blit(corner, (x, y + mini_room_size - mini_default_size))
                screen.blit(corner, (x + mini_room_size - mini_default_size, y + mini_room_size - mini_default_size))

                # Draw default walls
                wall = pygame.image.load('Assets/wall.png')
                vert_wall = pygame.transform.scale(wall, (mini_default_size, mini_default_size))
                horz_wall = pygame.transform.rotate(vert_wall, 90)
                default_vert_walls = [(x, y + mini_default_size),  # top left corner bottom
                                      (x, y + mini_room_size - 2 * mini_default_size),  # bottom left corner top
                                      (x + mini_room_size - mini_default_size, y + mini_default_size),  # top right corner bottom
                                      (x + mini_room_size - mini_default_size, y + mini_room_size - 2 * mini_default_size),  # bottom right corner top
                                      ]
                default_horz_walls = [(x + mini_default_size, y),  # top left corner right
                                      (x + mini_room_size - 2 * mini_default_size, y),  # top right corner left
                                      (x + mini_default_size, y + mini_room_size - mini_default_size),  # bottom left corner right
                                      (x + mini_room_size - 2 * mini_default_size, y + mini_room_size - mini_default_size)  # bottom right corner left
                                      ]
                for location in default_vert_walls:
                    screen.blit(vert_wall, location)
                for location in default_horz_walls:
                    screen.blit(horz_wall, location)

                # Draw blocked walls
                if room.get_nwall():
                    screen.blit(horz_wall, (x + 2 * mini_default_size, y))
                    screen.blit(horz_wall, (x + mini_room_size - 3 * mini_default_size, y))
                if room.get_wwall():
                    screen.blit(vert_wall, (x, y + 2 * mini_default_size))
                    screen.blit(vert_wall, (x, y + mini_room_size - 3 * mini_default_size))
                if room.get_ewall():
                    screen.blit(vert_wall, (x + mini_room_size - mini_default_size, y + 2 * mini_default_size))
                    screen.blit(vert_wall, (x + mini_room_size - mini_default_size, y + mini_room_size - 3 * mini_default_size))
                if room.get_swall():
                    screen.blit(horz_wall, (x + 2 * mini_default_size, y + mini_room_size - mini_default_size))
                    screen.blit(horz_wall, (x + mini_room_size - 3 * mini_default_size, y + mini_room_size - mini_default_size))

    #Draw Hero in absolute position in the maze
    hero_img = pygame.image.load("Assets/" + Hero.get_instance().get_image())
    scaled_hero = pygame.transform.scale(hero_img, (mini_default_size, mini_default_size))
    screen.blit(scaled_hero, (hero_room_x*mini_room_size + mini_room_size * .5, hero_room_y*mini_room_size + mini_room_size * .5 + 30))