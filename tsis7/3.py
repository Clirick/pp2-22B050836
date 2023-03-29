import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

ball_pos = [250, 250]
ball_radius = 25

move_vector = [0, 0]

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_vector[1] = -20

            elif event.key == pygame.K_DOWN:
                move_vector[1] = 20

            elif event.key == pygame.K_LEFT:
                move_vector[0] = -20

            elif event.key == pygame.K_RIGHT:
                move_vector[0] = 20

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                move_vector[1] = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                move_vector[0] = 0
    

    ball_pos[0] += move_vector[0]
    ball_pos[1] += move_vector[1]
    
    if ball_pos[0] - ball_radius < 0:
        ball_pos[0] = ball_radius
    elif ball_pos[0] + ball_radius > size[0]:
        ball_pos[0] = size[0] - ball_radius
    if ball_pos[1] - ball_radius < 0:
        ball_pos[1] = ball_radius
    elif ball_pos[1] + ball_radius > size[1]:
        ball_pos[1] = size[1] - ball_radius
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
