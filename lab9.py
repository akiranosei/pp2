#import all importnant libraries
import pygame, sys
from pygame.locals import *
import random, time
#initialize pygame library
pygame.init()
#set FPS, used colors and characteristics
FPS = 60
FramePerSec = pygame.time.Clock()
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COINS = 0
#set font style, game over text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
#set background picture and its size (adjust to window size)
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

#enemy class type and how it can appear and move
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#coin class, where set its look and random appearance
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = {
            1: pygame.image.load("coin.png"),
            2: pygame.image.load("coin2.png"),
            3: pygame.image.load("coin3.png"),}

        self.weight = random.choice([1, 2, 3])
        self.image = pygame.transform.scale(self.images[self.weight], (25, 25))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.weight = random.choice([1, 2, 3])
        self.image = pygame.transform.scale(self.images[self.weight], (25, 25))
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(100, SCREEN_HEIGHT - 100))

    def move(self):
        pass

#set player (rocket) sizes, its movement across the screen, speed and borders
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#init classes and add character sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#while game is gaming, ensure the constant speed, sprites/pics updating
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    for coin in coins:
        w_text = font_small.render(str(coin.weight), True, WHITE)
        DISPLAYSURF.blit(w_text, (coin.rect.x, coin.rect.y - 15))

    #if enemies crash wirh rocket, turn on crash sound and show the game over screen
    #If user pushed R, the game restarts with 0 scroing, if user pushed Q game is over and window closes
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crashsound.mp3').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        restart_text = font_small.render("Press R to Restart or Q to Quit", True, BLACK)
        DISPLAYSURF.blit(restart_text, (50, 350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        SPEED = 5
                        COINS = 0
                        P1 = Player()
                        E1 = Enemy()
                        C1 = Coin()
                        enemies.empty()
                        enemies.add(E1)
                        coins.empty()
                        coins.add(C1)
                        all_sprites.empty()
                        all_sprites.add(P1)
                        all_sprites.add(E1)
                        all_sprites.add(C1)
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    #If receive coins, add coin get sound and add +1 to coin scoring, next coin should appear randomly
    hit_coin = pygame.sprite.spritecollideany(P1, coins)
    if hit_coin:
        pygame.mixer.Sound('coinget.mp3').play()
        COINS += hit_coin.weight
        hit_coin.reset_position()
        if COINS % 10 == 0:
            SPEED += 1


    #coins scoring text appears at the right top side of screen
    coins_text = font_small.render("Coins: " + str(COINS), True, WHITE)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))
    pygame.display.update()
    FramePerSec.tick(FPS)