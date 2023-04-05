import random
import pygame
import time

pygame.init()
#COLOURS
SCORE = 0
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#Setting images
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
background_image = pygame.image.load('AnimatedStreet.png')
enemy_image = pygame.image.load('Enemy.png')
player_image = pygame.image.load('Player.png')
coin_image = pygame.image.load('coin2.jpg')

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#setting up fonts
font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

clock = pygame.time.Clock()
coin_image = pygame.image.load('coin2.jpg')
coin_image = pygame.transform.scale(coin_image, (coin_image.get_width() // 4, coin_image.get_height() // 4))



#Creating classes
class Enemy():
    def __init__(self):
        self.speed = 10
        self.image = enemy_image
        self.rect = self.image.get_rect()

        #choosing random point in x-axis to spawn enemy
        random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.center = (random_width, 0)


    def update(self):
        global SCORE
        self.rect.y += self.speed // 1

        if self.rect.y > HEIGHT:
            SCORE += 1
            if self.speed < 20: 
                self.speed += 0.25 

           #respawn
            random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
            self.rect.center = (random_width, 0)


    def draw(self):
        SCREEN.blit(self.image, self.rect)





class Player():
    def __init__(self):
        self.speed = 5
        self.image = player_image
        self.rect = self.image.get_rect()
     
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)


    def update(self):
        pressed = pygame.key.get_pressed()
        #checking if player is still on screen
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.x += self.speed
    
    
    def draw(self):
        SCREEN.blit(self.image, self.rect)




class Background():
    def __init__(self, start_y):
        self.image = background_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 + start_y)


    def draw(self):
        SCREEN.blit(self.image, self.rect)


    def update(self, speed):
      
        if self.rect.y >= HEIGHT + 10:
            self.rect.y = -HEIGHT - 10
        self.rect.y += speed





class Coin():
    def __init__(self, x, y):
        #getting coordinates
        self.x = x
        self.y = y
        
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self, speed):
        self.rect.y += speed

    
    def draw(self):
        SCREEN.blit(self.image, self.rect)




def add_coins(coins):
    for i in range(5):
    
        random_width = random.randint(40, WIDTH - 40)
        coins.append(Coin(random_width, -(i) * HEIGHT * 0.15))
    return coins




def main():
    COLLECTED = 0
    enemy = Enemy()
    player = Player()
    background_1 = Background(0)
    background_2 = Background(-HEIGHT)
    coins = []
    running = True

    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        if len(coins) < 2:
            add_coins(coins)
        
        

        #updating states of entities exept coins
        background_1.update(enemy.speed // 3)
        background_2.update(enemy.speed // 3)
        player.update()
        enemy.update()
     
        background_1.draw()
        background_2.draw()
        player.draw()
        enemy.draw()

        #showing score and number of coins
        score = font_small.render("Your score: " + str(SCORE), True, BLACK)
        coins_text = font_small.render("Coins collected: " + str(COLLECTED), True, BLACK)
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coins_text, (WIDTH // 2, 0))

        #collision between player and enemy
        if player.rect.colliderect(enemy):
            SCREEN.blit(game_over, (30, 250))
            pygame.display.flip() 
            time.sleep(1)
            running = False 

        i = 0
        while i < len(coins):
            #collision between player and coin
            if player.rect.colliderect(coins[i]):
                COLLECTED += 1
                coins.pop(i)
                i -= 1
            #returning coin to start
            if coins[i].rect.y >= HEIGHT:
                coins[i].rect.y = -20
            i += 1

        for coin in coins:
            coin.update(enemy.speed // 3)
            coin.draw()

        pygame.display.flip()
        clock.tick(60)






if __name__ == '__main__':
    main()