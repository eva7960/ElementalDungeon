import pygame
import os

from Controller import DungeonController
from Controller.SaveLoad import SaveLoad
from Model.Dungeon import Dungeon
from View import LoadView

"""
A method for displaying the load screen from the main menu.

@param screen the pygame screen being passed around by the controllers
"""
def run(screen):
    is_running = True

    # Get the list of pickle files currently in LoadGame
    file_list = [f for f in os.listdir('LoadGame') if f.endswith(".pickle")]
    selected_file = None

    # Main game loop
    while is_running:
        # Set up screen and save button
        LoadView.draw_image(screen, 'Assets/dungeonBackground.png', 0, 0, 810, 810)
        LoadView.draw_image(screen, 'Assets/banner.png', 45, 20, 700, 150)
        LoadView.draw_header(screen, "Load Game", 300, 70)
        confirm_button = LoadView.draw_button(screen,'Assets/buttonSquare_beige.png', "Confirm", 600, 700, 175, 75)

        # Draw buttons for all the files in LoadGame
        for i, file_name in enumerate(file_list):
            button_clicked = LoadView.draw_button(
                screen, 'Assets/button.png', file_name[:-7], 250, 300 + i * 100, 300, 50
            )
            if button_clicked:
                pygame.draw.rect(
                    pygame.display.get_surface(),
                    (0, 255, 0),
                    pygame.Rect(240, 295 + i * 100, 320, 60),
                    2)
                selected_file = file_name

        ''' If a file has been selected and the confirm button is hit, load the saved game'''
        if selected_file and confirm_button:
            dungeon_list = SaveLoad.load_game(selected_file[:-7])  # Load the dungeon data
            Dungeon(True, dungeon_list[0], dungeon_list[1], dungeon_list[2])
            DungeonController.run(screen)
            is_running = False

        #Allow user to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
