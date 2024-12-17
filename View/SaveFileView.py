import pygame
pygame.init()

#Constants
COLOR = (87,57,46)
WHITE = (255,255,255)

FONT = 'Assets/8-bit-pusab.ttf'
HEADER_FONT = pygame.font.Font(FONT, 30)
SMALL_FONT = pygame.font.Font(FONT, 20)

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 300
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

"""
A method for drawing headers.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_header(text, x, y):
    img = HEADER_FONT.render(text, True, COLOR)
    SCREEN.blit(img, (x, y))

"""
A method for drawing text.

@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_text(text, x, y):
    img = SMALL_FONT.render(text, True, COLOR)
    SCREEN.blit(img, (x, y))

"""
A method for drawing scaled images.

@param img the image to draw
@param x the x coordinate of the top left corner of the image
@param y the y coordinate of the top left corner of the image
@param width how wide to make the image
@param height how tall to make the image
"""
def draw_scaled_image(img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    SCREEN.blit(scaled_img, (x, y))

"""
A method for drawing buttons.

@param img the button image
@param text the text to add to the button
@param x the x coordinate of the top left corner of the button
@param y the y coordinate of the top left corner of the button
@param width how wide to make the button
@param height how tall to make the button
"""
def draw_button(img, text, x, y, width, height):
    button_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    text_surface = SMALL_FONT.render(text, True, COLOR)
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
A method for drawing textfields.

@param x the x coordinate of the top left corner of the textfield
@param y the y coordinate of the top left corner of the textfield
@param width how wide to make the textfield
@param height how tall to make the textfield
@param placeholder the placeholder text before the textfield is filled in
@param active whether the textfield is currently writable or not
@param text the text entered into the textfield
"""
def draw_text_field(x, y, width, height, placeholder, active, text):
    pygame.draw.rect(SCREEN, WHITE, (x, y, width, height), border_radius=5)
    pygame.draw.rect(SCREEN, WHITE if active else (200, 200, 200), (x, y, width, height), 2)

    display_text = placeholder if not text and not active else text
    text_surface = SMALL_FONT.render(display_text, True, COLOR if text or active else (150, 150, 150))

    # Center the text
    text_x = x + (width - text_surface.get_width()) // 2
    text_y = y + (height - text_surface.get_height()) // 2
    SCREEN.blit(text_surface, (text_x, text_y))

