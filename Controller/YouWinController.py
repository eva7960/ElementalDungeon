import pygame

from Controller import ChooseHeroController
from Model.Dungeon import Dungeon
from View import YouWinView as View

"""
A method for displaying the you won screen.

@param screen the pygame screen being passed around by the controllers
"""
def run(screen):
    is_running = True

    # Main game loop
    while is_running:
        # Draw background
        screen.fill((0, 0, 0))
        View.draw_scaled_image(screen, 'Assets/dungeonBackground.png', 0, 0, 810, 810)
        View.draw_scaled_image(screen, 'Assets/banner.png', 155, 200, 500, 150)
        View.draw_text(screen, "You Win!", 260, 230)
        View.draw_scaled_image(screen, 'Assets/treasure_chest.jpg', 367, 375, 75, 75)

        # Draw buttons
        new_game = View.draw_button(screen, 'Assets/button.png', "Play Again", 300, 500, 200, 75)
        quit_game = View.draw_button(screen, 'Assets/button.png', "Quit", 300, 600, 200, 75)

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
            is_running = False

        # Allow the user to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
