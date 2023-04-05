import pygame

pygame.init()

# Сolours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


button_font = pygame.font.SysFont('calibri', 16)


brush_color = BLACK


brush_size = 10


def create_circle(color, position):
    pygame.draw.circle(screen, color, position, brush_size)

# Create the color buttons
color_buttons = [
    {
        'color': BLUE,
        'rect': pygame.Rect(10, 10, 50, 50)
    },
    {
        'color': RED,
        'rect': pygame.Rect(70, 10, 50, 50)
    },
    {
        'color': BLACK,
        'rect': pygame.Rect(130, 10, 50, 50)
    },
    {
        'color': WHITE,
        'rect': pygame.Rect(190, 10, 50, 50)
    },
    {
        'color': PINK,
        'rect': pygame.Rect(250, 10, 50, 50)
    }
]

# Define the eraser button
eraser_button = pygame.Rect(310, 10, 50, 50)

# Set the program loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
         
            for button in color_buttons:
                if button['rect'].collidepoint(event.pos):
                    brush_color = button['color']
         
            if eraser_button.collidepoint(event.pos):
                screen.fill(BLACK)
        elif event.type == pygame.MOUSEMOTION:
           
            if pygame.mouse.get_pressed()[0]:
                create_circle(brush_color, event.pos)
        elif event.type == pygame.KEYDOWN:
            # Create a circle on key press 'T'
            if event.key == pygame.K_t:
                create_circle(brush_color, pygame.mouse.get_pos())
            # Create a rectangle on key press 'H'
            elif event.key == pygame.K_h:
                rect_size = (50, 50)
                rect_pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, brush_color, (rect_pos, rect_size))
                pygame.display.update()

    for button in color_buttons:
        pygame.draw.rect(screen, button['color'], button['rect'])

    # Draw the eraser button
    pygame.draw.rect(screen, RED, eraser_button)

    # Draw the "Erase" text on the eraser button
    erase_text = button_font.render("Erase", True, WHITE)
    erase_text_rect = erase_text.get_rect(center=eraser_button.center)
    screen.blit(erase_text, erase_text_rect)

    pygame.display.update()

pygame.quit()
