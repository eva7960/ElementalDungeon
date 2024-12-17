from random import choice
import pygame

from Controller import BattleController, HowToPlayController, YouWinController, SaveFileController
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Maze import Maze
from View import DungeonView as View

# Declare new pygame events
EXIT_DUNGEON = pygame.USEREVENT + 3
GET_POTION = pygame.USEREVENT + 1
MONSTER_BATTLE = pygame.USEREVENT + 2


# Declare file variables

_inventory_clicked = False
_map_clicked = False
_monster_defeated = False
_potion_removed = False
_run = True

_potion_time = 0

_array = []
_exit_rect = None
_health_potion_rects = []
_monster_rect = []
_potion_rect = []
_room_rects = []
_toolbar_rects = []
_vision_potion_rects = []

_player = None


"""
A method to run the dungeon screen.

@param screen the pygame screen being passed into controller files
"""
def run(screen):
    global EXIT_DUNGEON
    global GET_POTION
    global MONSTER_BATTLE

    global _inventory_clicked
    global _map_clicked
    global _run

    global _potion_time

    global _array
    global _exit_rect
    global _health_potion_rects
    global _monster_rect
    global _potion_rect
    global _room_rects
    global _toolbar_rects
    global _vision_potion_rects

    global _player

    _potion_time = 0

    # Start dungeon music
    pygame.mixer.init()
    pygame.mixer.music.load('Assets/dungeon music.wav')
    pygame.mixer.music.play(loops=-1)

    # Initialize pygame items
    clock = pygame.time.Clock()
    fps = 60
    GET_POTION = pygame.USEREVENT + 1
    MONSTER_BATTLE = pygame.USEREVENT + 2
    EXIT_DUNGEON = pygame.USEREVENT + 3

    View.set_up(screen)

    _toolbar_rects = View.draw_toolbar(screen)
    _health_potion_rects, _vision_potion_rects = View.draw_inventory(screen)
    _array = Maze.get_instance().get_array()

    """
    A Hero not coming from a pickled file will be placed in a random empty room. 
    Newly generated Heroes start at -100,-100 to avoid immediate collisions.
    """
    if Hero.get_instance().get_x() == -100 and Hero.get_instance().get_y() == -100:
        empty_rooms = []
        for i in range(len(_array)):
            for j in range(len(_array[i])):
                if _array[i][j].get_monster() is None and _array[i][j].get_potion() is None:
                        empty_rooms.append(_array[i][j])
        hero_room = choice(empty_rooms)
        x = hero_room.get_location()[0] * View.ROOM_SIZE + View.ROOM_SIZE * .5
        y = hero_room.get_location()[1] * View.ROOM_SIZE + View.ROOM_SIZE * .5
        Hero.get_instance().set_x(int(x))
        Hero.get_instance().set_y(int(y))

    _player = ControllerHero(View.draw_hero(screen))
    _player.rect.topleft = (Hero.get_instance().get_x() - View.get_camera_offset()[0],
                            Hero.get_instance().get_y() - View.get_camera_offset()[1])
    # main game loop
    while _run:

        # Initialize pygem fps and screen fill
        clock.tick(fps)
        screen.fill(0)

        # Empty the collision lists so they are updated with each redraw
        _room_rects = []
        _monster_rect = []
        _potion_rect = []
        _exit_rect = None

        # Add necessary rectangles for collisions in each room
        for i in range(len(_array)):
            for j in range(len(_array[i])):
                _room_rects.append(View.draw_room(screen, _array[i][j]))
                possible_monster = View.draw_monster(screen, _array[i][j])
                if not possible_monster is None:
                    _monster_rect.append(possible_monster)
                possible_potion = View.draw_potion(screen, _array[i][j])
                if not possible_potion is None:
                    _potion_rect.append(possible_potion)
                possible_exit = View.draw_exit(screen, _array[i][j])
                if not possible_exit is None:
                    _exit_rect = possible_exit

        # Update player based on input
        _player.move()
        View.draw_hero(screen)

        # Add the vision screen unless a vision potion has been used
        if _potion_time == 0:
            View.draw_vision(screen)
        else:
            _potion_time -= 1

        # Open inventory
        if _inventory_clicked:
            View.draw_inventory(screen)
            _health_potion_rects, _vision_potion_rects = View.draw_inventory(screen)

        # Open Map
        if _map_clicked:
            View.draw_mini_map(screen)

        # Draw the toolbar over the dungeon and vision screen
        _toolbar_rects = View.draw_toolbar(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _run = False
            handle_event(screen, event)

        pygame.display.update()
    pygame.quit()

"""
An internal class to handle the Hero's interactions in the maze. Extends pygame Sprite
"""
class ControllerHero(pygame.sprite.Sprite):

    """ Keep track of the direction the player is going, allows for diagonal movement"""
    left = False
    right = False
    up = False
    down = False

    """ 
    Constructor for making a new controller hero
    
    @param rect the rect that is generated by drawing the hero in view
    """
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.rect.topleft = (Hero.get_instance().get_x(), Hero.get_instance().get_y())

    """
    Handles the player's movements by checking for collisions.
    """
    def move(self):
        hero_x = Hero.get_instance().get_x()
        hero_y = Hero.get_instance().get_y()

        for rect in _potion_rect:
            if self.rect.colliderect(rect):
                pygame.event.post(pygame.event.Event(GET_POTION))
                break
        for rect in _monster_rect:
            if self.rect.colliderect(rect):
                pygame.event.post(pygame.event.Event(MONSTER_BATTLE))
                break
        if _exit_rect is not None and self.rect.colliderect(_exit_rect):
            pygame.event.post(pygame.event.Event(EXIT_DUNGEON))
        if self.down and not self.collide_down():
            Hero.get_instance().set_y(hero_y + 5)
        if self.up and not self.collide_up():
            Hero.get_instance().set_y(hero_y - 5)
        if self.right and not self.collide_right():
            Hero.get_instance().set_x(hero_x + 5)
        if self.left and not self.collide_left():
            Hero.get_instance().set_x(hero_x - 5)
        self.rect.topleft = (Hero.get_instance().get_x() - View.get_camera_offset()[0], Hero.get_instance().get_y() - View.get_camera_offset()[1])

    """
    Checks for collisions below the character if the character is trying to move down.
    Returns true of there is a collision.
    """
    def collide_down(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.bottom <= rect.top + 5:
                    return True
        return False
    """
    Checks for collisions above the character if the character is trying to move up.
    Returns true of there is a collision.
    """
    def collide_up(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.top >= rect.bottom - 5:
                    return True
        return False

    """
    Checks for collisions to the right of the character if the character is trying to move right.
    Returns true of there is a collision.
    """
    def collide_right(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.right <= rect.left + 5:
                    return True
        return False
    """
    Checks for collisions to the left of the character if the character is trying to move left.
    Returns true of there is a collision.
    """
    def collide_left(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.left >= rect.right - 5:
                    return True
        return False

"""
Event handler for various keyboard and mouse click events

@param screen the pygame screen which is needed for some events
@param event the type of event that has occurred
"""
def handle_event(screen, event):
    global _run
    global _inventory_clicked
    global _map_clicked
    global _toolbar_rects
    global _potion_time
    room = get_current_room()

    #Check for directional movements using 'awsd' keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            _player.down = True
        if event.key == pygame.K_w:
            _player.up = True
        if event.key == pygame.K_d:
            _player.right = True
        if event.key == pygame.K_a:
            _player.left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s:
            _player.down = False
        if event.key == pygame.K_w:
            _player.up = False
        if event.key == pygame.K_d:
            _player.right = False
        if event.key == pygame.K_a:
            _player.left = False

    #Check if new potion was acquired
    if event.type == GET_POTION:
        Inventory.get_instance().add(room.get_potion())
        room.set_potion(None)

    #Check if collided with a monster
    if event.type == MONSTER_BATTLE:
        _player.down = False
        _player.up = False
        _player.right = False
        _player.left = False
        BattleController.run(room.get_monster())
        room.set_monster(None)

    #Check if found the exit
    if event.type == EXIT_DUNGEON:
        YouWinController.run(screen)

    #Check if the mouse was used to click on items in the toolbar
    if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(len(_toolbar_rects)):
            if _toolbar_rects[i].collidepoint(event.pos):
                if i == 0:
                    if _inventory_clicked:
                        _inventory_clicked = False
                    else:
                        _inventory_clicked = True

                elif i == 1:
                    if _map_clicked:
                        _map_clicked = False
                    else:
                        _map_clicked = True
                        _player.down = False
                        _player.up = False
                        _player.right = False
                        _player.left = False
                elif i == 2:
                    SaveFileController.run()
                elif i == 3:
                    HowToPlayController.run()
                else:
                    _run = False
            # If inventory is open, check for potion actions
            for i in range(len(_health_potion_rects)):
                if _health_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_health_potion()
                    _health_potion_rects.pop(i)
                    break
            for i in range(len(_vision_potion_rects)):
                if _vision_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_vision_potion()
                    _potion_time = 600
                    _vision_potion_rects.pop(i)
                    break
"""
Uses the Hero's coordinates to calculate where in the Room array the Hero currently is.
Returns the Room and marks it has visited by the Hero.
"""
def get_current_room():
    x = Hero.get_instance().get_x()
    y = Hero.get_instance().get_y()
    room_x = x//View.ROOM_SIZE
    room_y = y//View.ROOM_SIZE
    _array[room_x][room_y].set_hero_has_visited(True)
    return _array[room_x][room_y]