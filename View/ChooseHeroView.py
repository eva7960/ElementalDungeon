import pygame
pygame.init()

# Constants
BLACK = (0,0,0)
WHITE = (255,255,255)

FONT = 'Assets/8-bit-pusab.ttf'
HEADER_FONT = pygame.font.Font(FONT, 40)
SMALL_FONT = pygame.font.Font(FONT, 20)

pygame.display.set_caption("Choose Your Hero")

"""
A method for drawing headers.

@param screen the screen to draw the header on
@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_header(screen, text, x, y):
    img = HEADER_FONT.render(text, True, WHITE)
    screen.blit(img,(x,y))

"""
A method for drawing text.

@param screen the screen to draw the text on
@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_text(screen, text, x, y):
    img = SMALL_FONT.render(text, True, WHITE)
    screen.blit(img, (x,y))

"""
A method for drawing images.

@param screen the screen to draw the image on
@param img the image to draw
@param x the x coordinate of the top left corner of the image
@param y the y coordinate of the top left corner of the image
@param width how wide to make the image
@param height how tall to make the image
"""
def draw_image(screen, img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    screen.blit(scaled_img, (x, y))

"""
A method for drawing buttons.

@param screen the screen to draw the button on
@param img_path the path to get the button image
@param text the text to add to the button
@param x the x coordinate of the top left corner of the button
@param y the y coordinate of the top left corner of the button
@param width how wide to make the button
@param height how tall to make the button
"""
def draw_button(screen, img_path, text, x, y, width, height):
    button_img = pygame.image.load(img_path).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    text_surface = SMALL_FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(scaled_img, button_rect)
    screen.blit(text_surface, text_rect)

    return button_rect

"""
A method for drawing textfields.

@param screen the screen to draw the textfield on
@param x the x coordinate of the top left corner of the textfield
@param y the y coordinate of the top left corner of the textfield
@param width how wide to make the textfield
@param height how tall to make the textfield
@param placeholder the placeholder text before the textfield is filled in
@param active whether the textfield is currently writable or not
@param text the text entered into the textfield
"""
def draw_text_field(screen, x, y, width, height, placeholder, active, text):
    pygame.draw.rect(screen, WHITE, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, WHITE if active else (200, 200, 200), (x, y, width, height), 2)
    display_text = placeholder if not text and not active else text
    text_surface = SMALL_FONT.render(display_text, True, BLACK if text or active else (150, 150, 150))

    # Center the text
    text_x = x + (width - text_surface.get_width()) // 2
    text_y = y + (height - text_surface.get_height()) // 2
    screen.blit(text_surface, (text_x, text_y))



