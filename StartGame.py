import pygame
from Controller import MainMenuController

"""
A class for starting the dungeon adventure game.
"""
class StartGame:
    pygame.init()
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    MainMenuController.run(screen)
    #yippie