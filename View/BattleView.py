import pygame

# Initialize items to run pygame
pygame.init()
 # Constants
BLACK = (0,0,0)
WHITE = (255,255,255)

FONT = 'Assets/8-bit-pusab.ttf'
BIG_FONT = pygame.font.Font(FONT, 20)
HEADER_FONT = pygame.font.Font(FONT, 30)
REWARD_FONT = pygame.font.Font(FONT, 20)
SMALL_FONT = pygame.font.Font(FONT, 18)
TEXT_FONT = pygame.font.Font(FONT, 25)

SCREEN = pygame.display.set_mode((10, 4))

pygame.display.set_caption("Battle")

"""
A method for drawing text for labels.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_text(text, x, y):
    img = BIG_FONT.render(text, True, WHITE)
    SCREEN.blit(img, (x, y))

"""
A method for writing out the results of battle actions on Hero.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_result(text, x, y):
    img = TEXT_FONT.render(text, True, WHITE)
    SCREEN.blit(img, (x, y))

"""
A method for writing out the results of battle actions on monster.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_monster_result(text, x, y):
    img = TEXT_FONT.render(text, True, (255, 0, 0))
    SCREEN.blit(img, (x, y))

"""
A method for drawing images.

@param img the image to draw
@param x the x coordinate to draw the image at
@param y the y coordinate to draw the image at
@param width how wide to make the image
@param height how tall to make the image
"""
def draw_image(img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    SCREEN.blit(scaled_img, (x, y))

"""
A method for drawing a rotated images.

@param img the image to draw
@param x the x coordinate to draw the image at
@param y the y coordinate to draw the image at
@param width how wide to make the image
@param height how tall to make the image
@param degree how much to rotate the image by
"""
def draw_rotated_image(img, x, y, width, height, degree):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    new_img = pygame.transform.rotate(scaled_img, degree)
    SCREEN.blit(new_img, (x, y))

"""
A method for drawing buttons

@param img the image to use for the button
@param text the text to put on the button
@param x the x coordinate to draw the image at
@param y the y coordinate to draw the image at
@param width how wide to make the image
@param height how tall to make the image
"""
def draw_button(img, text, x, y, width, height):
    button_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    text_surface = BIG_FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)

    SCREEN.blit(scaled_img, button_rect)
    SCREEN.blit(text_surface, text_rect)

    # Check if the button is clicked
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
        return True

    return False


"""
A method for drawing text on the reward window.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def reward_text(text, x, y):
    img = REWARD_FONT.render(text, True, (101, 67, 33))
    SCREEN.blit(img, (x, y))

"""
A method for drawing text for reward header.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def reward_header(text, x, y):
    img = HEADER_FONT.render(text, True, (101, 67, 33))
    SCREEN.blit(img, (x, y))

"""
A method for drawing the rewards window.

@param monster the monster the Hero just defeated
"""
def draw_rewards(monster):
    # Draw reward window
    dim_surface = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()))
    dim_surface.set_alpha(200)  # Set transparency
    dim_surface.fill((0, 0, 0))  # Black
    SCREEN.blit(dim_surface, (0, 0))
    rect = pygame.Rect(205, 205, 400, 400)
    pygame.draw.rect(SCREEN, (245, 222, 179), rect)
    reward_header("Rewards", 293, 220)

    # Get coordinate list depending on how much loot the monster has
    three_items = [(230, 350), (350, 350), (470, 350)]
    two_items = [(300, 350), (400, 350)]
    one_item = (350, 350)

    # Handles the different loot cases
    if monster.has_health_potion() and monster.has_vision_potion() and monster.has_pillar():
        draw_image('Assets/health_potion.png', three_items[0][0], three_items[0][1], 100, 100)
        draw_image('Assets/vision_potion.png', three_items[1][0], three_items[1][1], 100, 100)
        draw_image("Assets/" + monster.get_pillar().get_image(), three_items[2][0], three_items[2][1], 100, 100)
    elif monster.has_health_potion() and monster.has_vision_potion():
        draw_image('Assets/health_potion.png', two_items[0][0], two_items[0][1], 100, 100)
        draw_image('Assets/vision_potion.png', two_items[1][0], two_items[1][1], 100, 100)
    elif monster.has_health_potion() and monster.has_pillar():
        draw_image('Assets/health_potion.png', two_items[0][0], two_items[0][1], 100, 100)
        draw_image("Assets/" + monster.get_pillar().get_image(), two_items[1][0], two_items[1][1], 100, 100)
    elif monster.has_vision_potion() and monster.has_pillar():
        draw_image('Assets/vision_potion.png', two_items[0][0], two_items[0][1], 100, 100)
        draw_image("Assets/" + monster.get_pillar().get_image(), two_items[1][0], two_items[1][1], 100, 100)
    elif monster.has_health_potion():
        draw_image('Assets/health_potion.png', one_item[0], one_item[1], 100, 100)
    elif monster.has_vision_potion():
        draw_image('Assets/vision_potion.png', one_item[0], one_item[1], 100, 100)
    elif monster.has_pillar():
        draw_image("Assets/" + monster.get_pillar().get_image(), one_item[0], one_item[1], 100, 100)

    draw_button('Assets/button.png', "claim", 315, 500, 175, 70)

