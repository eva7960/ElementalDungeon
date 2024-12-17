import pygame

from Controller import ChooseHeroController, YouWinController, LoadController
from Controller import HowToPlayController
from View import MainMenuView as View

# Start main menu music
pygame.mixer.init()
pygame.mixer.music.load('Assets/menu music.wav')
pygame.mixer.music.play(loops=-1)

"""
A method for displaying the main menu.

@param screen the pygame screen being passed around the controllers
"""
def run(screen):
    is_running = True
    while is_running:
        # Draw the background
        screen.fill((234, 165, 108))
        View.draw_scaled_image(screen,'Assets/dungeonBackground.png', 0, 0, 810, 810)
        View.draw_scaled_image(screen,'Assets/banner.png', 155, 80, 500, 150)
        View.draw_header(screen,"Dungeon Adventure", 197, 120)

        # Draw the buttons
        new_game = View.draw_button(screen,'Assets/button.png', "New Game", 300, 300, 210, 50)
        load_game = View.draw_button(screen,'Assets/button.png', "Load Game", 300, 370, 210, 50)
        rules = View.draw_button(screen,'Assets/button.png', "How to play", 300, 440, 210, 50)
        quit_game = View.draw_button(screen,'Assets/button.png', "Quit", 300, 510, 210, 50)

        # Handle button clicks
        if(quit_game):
            is_running = False

        if(new_game):
            ChooseHeroController.run(screen)

        if(rules):
            HowToPlayController.run()

        if(load_game):
            LoadController.run(screen)

        # Allow the user to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

