import pygame
import math

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

def draw_right_triangle(color, position, size):
    x, y = position
    points = [(x, y), (x, y+size), (x+size, y+size)]
    pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(color, position, size):
    x, y = position
    points = [(x, y), (x + size, y), (x + size / 2, y + size * math.sqrt(3) / 2)]
    pygame.draw.polygon(screen, color, points)

def draw_rhombus(color, position, size):
    x, y = position
    points = [(x, y + size / 2), (x + size / 2, y), (x + size, y + size / 2), (x + size / 2, y + size)]
    pygame.draw.polygon(screen, color, points)

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
            # Check if a color button was pressed
            for button in color_buttons:
                if button['rect'].collidepoint(event.pos):
                    brush_color = button['color']
            # Check if the eraser button was pressed
            if eraser_button.collidepoint(event.pos):
                screen.fill(BLACK)
        elif event.type == pygame.MOUSEMOTION:
            # Check if the left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                # Draw a circle with the current brush color and size
                create_circle(brush_color, event.pos)
        elif event.type == pygame.KEYDOWN:
            # Check if the 'T' key was pressed to draw a circle
            if event.key == pygame.K_t:
                create_circle(brush_color, pygame.mouse.get_pos())
            # Check if the 'H' key was pressed to draw a rectangle
            elif event.key == pygame.K_h:
                rect_size = (50, 50)
                rect_pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, brush_color, (rect_pos, rect_size))
                pygame.display.update()
            # Check if the '1' key was pressed to draw a right triangle   
            elif event.key == pygame.K_1:
                draw_right_triangle(brush_color, pygame.mouse.get_pos(), 50)
            # Check if the '2' key was pressed to draw an equilateral triangle
            elif event.key == pygame.K_2:
                draw_equilateral_triangle(brush_color, pygame.mouse.get_pos(), 50)
            # Check if the '3' key was pressed to draw a rhombus
            elif event.key == pygame.K_3:
                draw_rhombus(brush_color, pygame.mouse.get_pos(), 50)

    # Draw the color buttons
    for button in color_buttons:
        pygame.draw.rect(screen, button['color'], button['rect'])

    # Draw the eraser button
    pygame.draw.rect(screen, RED, eraser_button)

    # Draw the "Erase" text on the eraser button
    erase_text = button_font.render("Erase", True, WHITE)
    erase_text_rect = erase_text.get_rect(center=eraser_button.center)
    screen.blit(erase_text, erase_text_rect)

    # Update the display
    pygame.display.update()

# Quit the program
pygame.quit()

