import pygame

from Controller import DungeonController
from Model.Dungeon import Dungeon
from Model.Element import Element
from View import ChooseHeroView as View

"""
A method for running the choose character screen.

@param the pygame screen being passed into each controller window
"""
def run(screen):

    # Initialize pygame items
    is_running = True
    clock = pygame.time.Clock()
    hero_name = ""
    text_field_active = False
    text_field_rect = pygame.Rect(200, 180, 400, 50)

    # Hero button definitions
    heroes = {
        "fire": {"rect": pygame.Rect(150, 675, 100, 100), "element": "Fire", "health": "60", "agility": "12"},
        "water": {"rect": pygame.Rect(450, 550, 100, 100), "element": "Water", "health": "80", "agility": "8"},
        "air": {"rect": pygame.Rect(250, 550, 100, 100), "element": "Air", "health": "40", "agility": "16"},
        "earth": {"rect": pygame.Rect(550, 675, 100, 100), "element": "Earth", "health": "100", "agility": "4"},
    }
    # Default stats (updated on hover or selection)
    current_stats = {"element": "---", "health": "---", "agility": "---"}
    selected_stats = {"element": "---", "health": "---", "agility": "---"}
    selected_hero = None
    confirm_button_visible = False
    confirmation_prompt = False
    # Confirmation state
    confirmation_result = False

    #main game loop
    while is_running:
        mouse_pos = pygame.mouse.get_pos()
        # Draw the background and UI
        View.draw_image(screen, 'Assets/dungeonBackground.png', 0, 0, 810, 810)
        View.draw_image(screen, 'Assets/banner.png', 45, 20, 700, 150)
        View.draw_header(screen, "Choose Your Hero", 90, 50)

        # Draw elements only if the confirmation prompt is NOT active
        if not confirmation_prompt:
            # Draw the text field with active indicator
            border_color = (0, 255, 0) if text_field_active else (255, 255, 255)
            pygame.draw.rect(pygame.display.get_surface(), border_color, text_field_rect, 2)
            View.draw_text_field(
                screen,
                text_field_rect.x, text_field_rect.y,
                text_field_rect.width, text_field_rect.height,
                "Name Your Hero", text_field_active, hero_name
            )

            # Draw current stats
            View.draw_text(screen, f"Element: {current_stats['element']}", 283, 260)
            View.draw_text(screen, f"Health: {current_stats['health']}", 305, 320)
            View.draw_text(screen,f"Agility: {current_stats['agility']}", 297, 380)

            # Draw hero buttons
            for hero, data in heroes.items():
                if data["rect"].collidepoint(mouse_pos):
                    # Highlight hovered hero and update stats
                    current_stats = {
                        "element": data["element"],
                        "health": data["health"],
                        "agility": data["agility"],
                    }
                    pygame.draw.rect(
                        pygame.display.get_surface(),
                        (255, 255, 0),
                        data["rect"].inflate(10, 10),
                        2
                    )
                if selected_hero == hero:
                    # Highlight the selected hero
                    pygame.draw.rect(
                        pygame.display.get_surface(),
                        (0, 255, 0),
                        data["rect"].inflate(10, 10),
                        2
                    )
                View.draw_button(screen, f'Assets/{hero}_hero.png', "", data["rect"].x, data["rect"].y, data["rect"].width,
                                 data["rect"].height)

            # Draw the Confirm button (at new position)
            if confirm_button_visible:
                View.draw_button(screen, 'Assets/button.png', "confirm", 302, 450, 200, 50)

        # Draw the confirmation prompt
        if confirmation_prompt:
            pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), (200, 300, 400, 200))  # Background box
            View.draw_text(screen,"Are you sure?", 280, 325)
            # Ensure confirmation prompt buttons have the correct positions
            View.draw_button(screen, 'Assets/button.png', "Yes", 250, 400, 100, 50)
            View.draw_button(screen, 'Assets/button.png', "No", 450, 400, 100, 50)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
                exit()

            if not confirmation_prompt:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a hero is clicked
                    for hero, data in heroes.items():
                        if data["rect"].collidepoint(event.pos):
                            selected_hero = hero  # Set selected hero only on click
                            selected_stats = {  # Use selected_stats to store selected hero's stats
                                "element": data["element"],
                                "health": data["health"],
                                "agility": data["agility"],
                            }
                            confirm_button_visible = bool(hero_name)  # Show confirm button only if a hero is selected
                            break  # Break after the first hero is clicked

                    # Activate or deactivate text field
                    if text_field_rect.collidepoint(event.pos):
                        text_field_active = True
                    else:
                        text_field_active = False

                    # Confirm button click (use updated position)
                    if confirm_button_visible and pygame.Rect(302, 450, 200, 50).collidepoint(event.pos):
                        confirmation_prompt = True
                        confirm_button_visible = False

                # Handle text input
                if event.type == pygame.KEYDOWN and text_field_active:
                    if event.key == pygame.K_BACKSPACE:
                        hero_name = hero_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        print(f"Hero Name Confirmed: {hero_name}")
                    elif len(hero_name) < 20:  # Limit text length
                        hero_name += event.unicode
                    confirm_button_visible = bool(hero_name and selected_hero)

            else:  # Handle confirmation prompt
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check for Yes button click
                    if pygame.Rect(250, 400, 100, 50).collidepoint(event.pos):  # Yes button
                        confirmation_result = True
                        if selected_stats["element"] == "Fire":
                            element = Element.FIRE
                            #CharacterFactory.create_hero(hero_name, Element.FIRE)
                        elif selected_stats["element"] == "Water":
                            element = Element.WATER
                            #CharacterFactory.create_hero(hero_name, Element.WATER)
                        elif selected_stats["element"] == "Air":
                            element = Element.AIR
                            #CharacterFactory.create_hero(hero_name, Element.AIR)
                        else:
                            element = Element.EARTH
                            #CharacterFactory.create_hero(hero_name, Element.EARTH)
                        Dungeon(False, [hero_name, element])
                        DungeonController.run(screen)
                    # Check for No button click
                    elif pygame.Rect(450, 400, 100, 50).collidepoint(event.pos):  # No button
                        confirmation_prompt = False
                        confirm_button_visible = True

            # Draw the background and UI
            View.draw_image(screen,'Assets/dungeonBackground.png', 0, 0, 810, 810)
            View.draw_image(screen,'Assets/banner.png', 45, 20, 700, 150)
            View.draw_header(screen,"Choose Your Hero", 90, 50)

            # Draw elements only if the confirmation prompt is NOT active
            if not confirmation_prompt:
                # Draw the text field with active indicator
                border_color = (0, 255, 0) if text_field_active else (255, 255, 255)
                pygame.draw.rect(pygame.display.get_surface(), border_color, text_field_rect, 2)
                View.draw_text_field(
                    screen,
                    text_field_rect.x, text_field_rect.y,
                    text_field_rect.width, text_field_rect.height,
                    "Name Your Hero", text_field_active, hero_name
                )

                # Draw current stats
                View.draw_text(screen,f"Element: {current_stats['element']}", 283, 260)
                View.draw_text(screen,f"Health: {current_stats['health']}", 305, 320)
                View.draw_text(screen,f"Agility: {current_stats['agility']}", 297, 380)

                # Draw hero buttons
                for hero, data in heroes.items():
                    if selected_hero == hero:
                        # Highlight the selected hero with a green border
                        pygame.draw.rect(
                            pygame.display.get_surface(),
                            (0, 255, 0),
                            data["rect"].inflate(10, 10),
                            2
                        )
                    else:
                        # Highlight hovered hero with yellow border (only during hover, not on click)
                        if data["rect"].collidepoint(mouse_pos):
                            pygame.draw.rect(
                                pygame.display.get_surface(),
                                (255, 255, 0),
                                data["rect"].inflate(10, 10),
                                2
                            )
                    View.draw_button(screen, f'Assets/{hero}_hero.png', "", data["rect"].x, data["rect"].y, data["rect"].width,
                                     data["rect"].height)

                # Draw the Confirm button (at new position)
                if confirm_button_visible:
                    View.draw_button(screen, 'Assets/button.png', "confirm", 302, 450, 200, 50)

            # Draw the confirmation prompt
            if confirmation_prompt:
                pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), (200, 300, 400, 200))  # Background box
                View.draw_text(screen,"Are you sure?", 280, 325)
                # Ensure confirmation prompt buttons have the correct positions
                View.draw_button(screen, 'Assets/button.png', "Yes", 250, 400, 100, 50)
                View.draw_button(screen, 'Assets/button.png', "No", 450, 400, 100, 50)

            # Update the display
            pygame.display.update()
            clock.tick(60)



