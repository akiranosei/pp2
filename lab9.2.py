import pygame
import time
import random
pygame.init()
snake_speed = 12
height = 720
width = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((width, height))

fps = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [  [100, 50],
                [100, 50],
                [100, 50],
                 ]
food_position = [random.randrange(1, (height//10)) * 10,
                  random.randrange(1, (width//10)) * 10]
food_spawn = True
food_weight = random.choice([1, 2, 3])
food_spawn_time = time.time()
food_lifetime = 3
direction = 'DOWN'
change_to = direction
score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 40)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (height/2, width/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += food_weight
        food_spawn = False
    else:
        snake_body.pop()

    if time.time() - food_spawn_time > food_lifetime:
        food_spawn = False

    if not food_spawn:
        food_position = [random.randrange(1, (height // 10)) * 10,
        random.randrange(1, (width // 10)) * 10 ]
        food_weight = random.choice([1, 2, 3])
        food_spawn_time = time.time()

    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
        
    if food_weight == 1:
        food_color = red
    elif food_weight == 2:
        food_color = (255, 165, 0)
    elif food_weight == 3:
        food_color = (0, 0, 255)

    pygame.draw.rect(game_window, food_color, pygame.Rect(
        food_position[0], food_position[1], 10, 10))
    font_w = pygame.font.SysFont("times new roman", 20)
    weight_text = font_w.render(str(food_weight), True, white)
    game_window.blit(weight_text, (food_position[0], food_position[1] + 15))

    
    if snake_position[0] < 0 or snake_position[0] > height-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > width-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    show_score(1, white, 'times new roman', 25)
    pygame.display.update()
    fps.tick(snake_speed)
