from View import HowToPlayView as View
import pygame

pygame.init()
"""
A method for displaying the help screen in the main menu and in the dungeon.
"""
def run():
    is_running = True
    while is_running:


        #images
        View.draw_scaled_image('Assets/panel.png', 0, 0, View.SCREEN_WIDTH, View.SCREEN_HEIGHT)
        View.draw_button('Assets/buttonSquare_beige.png', "w", 500, 420, 75, 75)
        View.draw_button('Assets/buttonSquare_beige.png', "s", 500, 500, 75, 75)
        View.draw_button('Assets/buttonSquare_beige.png', "a", 420, 500, 75, 75)
        View.draw_button('Assets/buttonSquare_beige.png', "d", 580, 500, 75, 75)

        #texts
        View.draw_header("HOW TO PLAY", 50, 50)
        pygame.display.set_caption("How To Play")
        View.draw_text("You are a hero trapped in a dungeon.", 50, 120)
        View.draw_text("Navigate through the dungeon maze", 50, 160)
        View.draw_text("to find the four pillars of OO.", 50, 200)
        View.draw_text("Watch out for monsters! They can drop", 50, 240)
        View.draw_text("pillars or potions to help you get", 50, 280)
        View.draw_text("through the maze. Once you find all", 50, 320)
        View.draw_text("four pillars you can find", 50, 360)
        View.draw_text("the Exit and escape!", 50, 400)
        View.draw_text("use wasd keys to move", 350, 600)



        exit_button = View.draw_button('Assets/buttonSquare_beige.png', "x", 710, 50, 50, 50)

        if exit_button:
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
