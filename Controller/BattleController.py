import pygame
import random

from Controller import YouDiedController
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Monster import Monster
from View import BattleView as View

# Initialize pygame
pygame.init()

"""
A method for running the battle screen.

@param monster is the monster the hero is currently fighting
"""

def run(monster):
    # Starts battle music
    pygame.mixer.init()
    pygame.mixer.music.load('Assets/battle music.wav')
    pygame.mixer.music.play(loops=-1)

    # Pygame set up
    screen = pygame.display.set_mode((810, 810))
    is_running = True
    clock = pygame.time.Clock()
    hero = Hero.get_instance()
    inventory = Inventory.get_instance()
    in_battle = True
    action_delay = 400  # Delay in milliseconds between turns

    black_rect = pygame.Rect(25, 475, 760, 190)
    white_rect = pygame.Rect(20, 470, 770, 200)

    """
    Updates the screen
    """
    def redraw_screen():
        """Redraw the screen elements."""
        screen.fill((0, 0, 0))
        View.draw_image('Assets/battle_background.jpg', 0, 0, 810, 450)
        pygame.draw.rect(screen, (0, 0, 0), black_rect)
        pygame.draw.rect(screen, (255, 255, 255), white_rect, 5)
        View.draw_text(f"Health Potions: {inventory.number_of_health_potions()}", 470, 625)
        display_health_bars()

    """
    Updates the sprites, checks for damage and death scenarios
    """
    def redraw_sprites(character, action):
        if action == "hit":
            if isinstance(character, Monster):
                View.draw_image("Assets/" + monster.get_hit_image(), 400, 330, 90, 90)
                View.draw_image("Assets/" + hero.get_image(), 75, 330, 90, 90)
            else:
                View.draw_image("Assets/" + hero.get_hit_image(), 75, 330, 90, 90)
                View.draw_image("Assets/" + monster.get_image(), 400, 330, 90, 90)
        elif action == "dead":
            if isinstance(character, Monster):
                View.draw_rotated_image("Assets/" + monster.get_dead_image(), 400, 350, 90, 90,270)
                View.draw_image("Assets/" + hero.get_image(), 75, 330, 90, 90)
            else:
                View.draw_rotated_image("Assets/" + hero.get_dead_image(), 75, 350, 90, 90, 90)
                View.draw_image("Assets/" + monster.get_image(), 400, 330, 90, 90)
        elif action == "idle":
            View.draw_image("Assets/" + hero.get_image(), 75, 330, 90, 90)
            View.draw_image("Assets/" + monster.get_image(), 400, 330, 90, 90)
    """
    Updates the screen based on damage and attack results
    
    @param character doing the action
    @param text name of character being acted against
    @param damage amount of damage done
    """
    def update(character, text, damage):
        """Update health bars and display results."""
        result = character.get_hp() + damage
        redraw_screen()
        redraw_sprites(character, "idle")
        if damage == 0:
            if character.get_name() == hero.get_name():
                View.draw_monster_result(text, 40, 500)
            else:
                View.draw_result(text,40,500)
        elif result <= 0:
            character.set_hp(0)
            display_health_bars()
            redraw_screen()
            if character.get_name() == hero.get_name():
                View.draw_monster_result(hero.get_name() + " was defeated", 40, 500)
                redraw_sprites(hero, "dead")
                YouDiedController.run(screen)
            else:
                View.draw_result(hero.get_name() + " won!", 40, 500)
                redraw_sprites(monster, "dead")
                pygame.display.update()
                pygame.time.wait(2000)
                View.draw_rewards(monster)
                clicked = False  # Initialize claim flag as False
                while not clicked:  # Keep checking for the claim button click
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            claim = View.draw_button('Assets/button.png', "claim", 315, 500, 175, 70)
                            if claim:  # If the claim button was clicked
                                if monster.has_health_potion():
                                    inventory.add(monster.health_potion)
                                if monster.has_vision_potion():
                                    inventory.add(monster.vision_potion)
                                if monster.has_pillar():
                                    inventory.add(monster.get_pillar())
                                clicked = True  # Set clicked to True to exit the loop
                                pygame.mixer.init()
                                pygame.mixer.music.load('Assets/dungeon music.wav')
                                pygame.mixer.music.play(loops=-1)
                    pygame.display.update()
            return False
        else:
            character.set_hp(result)
            redraw_screen()
            if character.get_name() == hero.get_name():
                View.draw_monster_result(text, 40, 500)
                if damage < 0:
                    redraw_sprites(hero, "hit")
                else:
                    redraw_sprites(hero, "idle")
            else:
                View.draw_result(text, 40, 500)
                if damage < 0:
                    redraw_sprites(monster, "hit")
                else:
                    redraw_sprites(hero, "idle")
        pygame.display.update()
        pygame.time.wait(action_delay)
        return True
    """
    Updates health bar
    """
    def display_health_bars():
        """Draw health bars for the hero and monster."""
        # Hero health bar
        if hero.get_hp() == 0:
            hero_health_width = 0 # If hero is defeated, set width to 0
        else:
            hero_health_width = (hero.get_hp() / hero.get_max_hp()) * 150
        pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(80, 20, hero_health_width, 25))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(80, 20, 150, 25), 3)
        View.draw_text("HP", 20, 15)
        View.draw_text(f"{hero.get_hp()}/{hero.get_max_hp()}", 250, 15)

        # Monster health bar
        if monster.get_hp() == 0:
            monster_health_width = 0  # If monster is defeated, set width to 0
        else:
            monster_health_width = (monster.get_hp() / monster.get_max_hp()) * 150
        pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(370, 270, monster_health_width, 25))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(370, 270, 150, 25), 3)
        View.draw_text(f"{monster.get_hp()}/{monster.get_max_hp()}", 530, 263)

    """
    Handles the monsters turn by determining if the monster will use its basic attack, special attack, or heal
    """
    def monsters_turn():
        """Monster's actions during its turn."""
        num = random.randint(1, 3)
        pygame.time.wait(action_delay)
        if num == 1:
            result = monster.attack()
            if result[0] > hero.get_agility():
                return update(hero, f" {monster.get_name()} dealt {result[1]} damage!", -result[1])
            else:
                return update(hero, f"{monster.get_name()} missed!", 0)
        elif num == 2:
            result = monster.special_attack()
            if result[0] > hero.get_agility():
                return update(hero, f"{monster.get_name()} dealt {result[1]} damage!", -result[1])
            else:
                return update(hero, f"{monster.get_name()} missed!", 0)
        else:
            healed = monster.heal()
            if not healed:
                result = monster.attack()
                if result[0] > hero.get_agility():
                    return update(hero, f"{monster.get_name()} dealt {result[1]} damage!", -result[1])
                else:
                    return update(hero, f"{monster.get_name()} missed!", 0)
            return update(hero, f" {monster.get_name()} healed!", 0)
    """
    Handles the Hero's action based on the user's input. Available actions include basic attack, special attack,
    use health potion, and skip. Skip is a cheat for testing/educational purposes.
    """
    def hero_turn(action):
        """Handle hero's actions based on input."""
        monster_agility = monster.get_agility()
        if action == "attack":
            result = hero.attack()
            if result[0] > monster.get_agility() and monster.get_element() == hero.get_opposite_element():
                return update(monster, f"{hero.get_name()} did {2 * result[1]} damage!", 2 * -result[1])
            elif result[0] > monster_agility:
                return update(monster, f"{hero.get_name()} did {result[1]} damage!", -result[1])
            else:
                return update(monster, f"{hero.get_name()} missed!", 0)

        elif action == "special":
            result = hero.special_attack()
            if result[0] > monster.get_agility():
                return update(monster, f"{hero.get_name()} did {result[1]} damage!", -result[1])
            else:
                return update(monster, f"{hero.get_name()} missed!", 0)
        elif action == "potion":
            inventory.drink_health_potion()
            return update(monster, f"{hero.get_name()} used a health potion!", 0)

    """ Main game loop"""
    while is_running and in_battle:
        redraw_screen()
        display_health_bars()
        redraw_sprites(hero, "idle")

        #draw option buttons
        View.draw_button('Assets/battle_button.png', "Attack", 20, 700, 185, 75)
        View.draw_button('Assets/battle_button.png', "Special", 215, 700, 185, 75)
        View.draw_button('Assets/battle_button.png', "Potion", 410, 700, 185, 75)
        View.draw_button('Assets/battle_button.png', "Skip", 605, 700, 185, 75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.mixer.music.stop()
                pygame.quit()
                exit()

            # determine user's input for Hero action
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos

                if 20 <= mx <= 205 and 700 <= my <= 775:
                    in_battle = hero_turn("attack")
                    if in_battle:
                        clock.tick(10)
                        in_battle = monsters_turn()

                elif 215 <= mx <= 400 and 700 <= my <= 775:
                    in_battle = hero_turn("special")
                    if in_battle:
                        clock.tick(10)
                        in_battle = monsters_turn()

                elif 410 <= mx <= 595 and 700 <= my <= 775:
                    if inventory.has_health_potion() and hero.get_hp() + 10 <= hero.get_max_hp():
                        in_battle = hero_turn("potion")
                        clock.tick(10)
                        in_battle = monsters_turn()
                    else:
                        View.draw_result("You can't use that", 40, 500)

                elif 605 <= mx <= 790 and 700 <= my <= 775:
                    is_running = False
                    if monster.has_health_potion():
                        inventory.add(monster.health_potion)
                    if monster.has_vision_potion():
                        inventory.add(monster.vision_potion)
                    if monster.has_pillar():
                        inventory.add(monster.get_pillar())
                    pygame.mixer.init()
                    pygame.mixer.music.load('Assets/dungeon music.wav')
                    pygame.mixer.music.play(loops=-1)

        pygame.display.update()
        clock.tick(60)
