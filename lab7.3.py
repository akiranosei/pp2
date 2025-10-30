import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
BLUE= (173, 216, 230)
RED = (255, 0, 0)
radius = 30
x, y = WIDTH // 2, HEIGHT // 2
move_step = 20
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - radius - move_step >= 0:
        y -= move_step
    if keys[pygame.K_DOWN] and y + radius + move_step <= HEIGHT:
        y += move_step
    if keys[pygame.K_LEFT] and x - radius - move_step >= 0:
        x -= move_step
    if keys[pygame.K_RIGHT] and x + radius + move_step <= WIDTH:
        x += move_step

    screen.fill(BLUE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()
