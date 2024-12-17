import pygame

from Controller import ChooseHeroController
from Model.Dungeon import Dungeon
from Model.Hero import Hero
from View import YouDiedView as View

"""
A method to display the you died screen.

@param screen the pygame screen being passed around by the controllers
"""
def run(screen):
    hero = Hero.get_instance()
    is_running = True

    # Main game loop
    while is_running:
        # Draw background
        screen.fill((0, 0, 0))
        View.draw_text(screen, "You Died :(", 175, 100)

        # Draw buttons
        new_game = View.draw_button(screen, 'Assets/button.png', "New Game", 300, 500, 200, 75)
        quit_game = View.draw_button(screen, 'Assets/button.png', "Quit", 300, 600, 200, 75)

        # Draw dead Hero
        View.draw_rotated_image(screen, "Assets/" + hero.get_dead_image(), 350, 300, 100, 100, 90)

        # Clear dungeon data
        Dungeon.delete_instance()

        # Handle button clicks
        if quit_game:
            is_running = False
            pygame.quit()
            exit()

        if new_game:
            pygame.mixer.init()
            pygame.mixer.music.load('Assets/menu music.wav')
            pygame.mixer.music.play(loops=-1)
            ChooseHeroController.run(screen)

        # Allow the user to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
