import pygame
pygame.init()

#Constants
RED = (255,0,0)
BLACK = (0,0,0)

FONT = 'Assets/8-bit-pusab.ttf'
BIG_FONT = pygame.font.Font(FONT, 50)
SMALL_FONT = pygame.font.Font(FONT, 20)


"""
A method for drawing text.

@param screen the screen to draw the text on
@param text the text to write out
@param x the x coordinate of the top left corner of the text
@param y the y coordinate of the top left corner of the text
"""
def draw_text(screen, text, x, y):
    img = BIG_FONT.render(text, True, RED)
    screen.blit(img, (x,y))

"""
A method for drawing images.

@param screen the screen to draw the image on
@param img the image to draw
@param x the x coordinate of the top left corner of the image
@param y the y coordinate of the top left corner of the image
"""
def draw_image(screen, img, x, y):
    screen.blit((pygame.image.load(img).convert()), (x,y))

"""
A method for drawing rotated images.

@param screen the screen to draw the image on
@param img the image to draw
@param x the x coordinate of the top left corner of the image
@param y the y coordinate of the top left corner of the image
@param width how wide to make the image
@param height how tall to make the image
@param degree how much to rotate the image by
"""
def draw_rotated_image(screen, img, x, y, width, height, degree):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    new_img = pygame.transform.rotate(scaled_img, degree)
    screen.blit(new_img, (x, y))

"""
A method for drawing scaled images.

@param screen the screen to draw the image on
@param img the image to draw
@param x the x coordinate of the top left corner of the image
@param y the y coordinate of the top left corner of the image
@param width how wide to make the image
@param height how tall to make the image
"""
def draw_scaled_image(screen, img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    screen.blit(scaled_img, (x, y))

"""
A method for drawing buttons.

@param screen the screen to draw the button on
@param img the button image
@param text the text to add to the button
@param x the x coordinate of the top left corner of the button
@param y the y coordinate of the top left corner of the button
@param width how wide to make the button
@param height how tall to make the button
"""
def draw_button(screen, img, text, x, y, width, height):
    button_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    text_surface = SMALL_FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)

    screen.blit(scaled_img, button_rect)
    screen.blit(text_surface, text_rect)

    # Check if the button is clicked
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
        return True

    return False


