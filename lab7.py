import pygame
import sys
from datetime import datetime
pygame.init()

WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey = pygame.image.load("mickey-pic.png").convert_alpha()
minute_hand = pygame.image.load("minute.png").convert_alpha()
second_hand = pygame.image.load("second.png").convert_alpha()

mickey = pygame.transform.smoothscale(mickey, (WIDTH, HEIGHT))

minute_scale = 0.8
second_scale = 0.7

minute_size = (int(minute_hand.get_width() * minute_scale),
               int(minute_hand.get_height() * minute_scale))
second_size = (int(second_hand.get_width() * second_scale),
               int(second_hand.get_height() * second_scale))

minute_hand = pygame.transform.smoothscale(minute_hand, minute_size)
second_hand = pygame.transform.smoothscale(second_hand, second_size)

center = (WIDTH // 2, HEIGHT // 2)

def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=pos).center)
    surf.blit(rotated_image, new_rect.topleft)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = -((minute / 60) * 360) + 90
    second_angle = -((second / 60) * 360) + 90

    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))

    blit_rotate_center(screen, minute_hand, center, minute_angle)
    blit_rotate_center(screen, second_hand, center, second_angle)

    pygame.display.flip()
    clock.tick(60)
