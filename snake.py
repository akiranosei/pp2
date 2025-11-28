import pygame
import time
import random
from database import user_login, save_game_state, get_all_user_scores
pygame.init()

height = 720
width = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((height, width))
font = pygame.font.SysFont('times new roman', 40)
score_font = pygame.font.SysFont('times new roman', 25)
fps = pygame.time.Clock()

def set_game_level(level):
    if level == 1:
        return 12, False
    elif level == 2:
        return 15, True
    elif level == 3:
        return 18, True
    return 12, False

def show_score(score):
    score_surface = score_font.render('Score: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 2, 15)
    game_window.blit(score_surface, score_rect)

def game_over(score):
    game_over_surface = font.render('Game Over! Score: ' + str(score), True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (height / 2, width / 2)
    game_window.blit(game_over_surface, game_over_rect)

    all_scores = get_all_user_scores()
    y_offset = 100

    for username, user_score, timestamp in all_scores[:5]:
        score_surface = font.render(f"{username}: {user_score}", True, white)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (width / 2, y_offset)
        game_window.blit(score_surface, score_rect)
        y_offset += 40

    pygame.display.update()
    time.sleep(100)

def game_loop(user_id, username, level, score):
    snake_speed, wall_mode = set_game_level(level)
    snake_position = [100, 50]
    snake_body = [[100, 50], [100, 50], [100, 50], [100, 50]]
    food_position = [random.randrange(1, (height // 10)) * 10,
                     random.randrange(1, (width // 10)) * 10]
    food_spawn = True
    direction = 'DOWN'
    change_to = direction
    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_s:
                    save_game_state(user_id, score, level)

        if paused:
            pause_surface = font.render('Game Paused. Press P to Resume', True, white)
            pause_rect = pause_surface.get_rect()
            pause_rect.midtop = (height / 2, width / 2)
            game_window.blit(pause_surface, pause_rect)
            pygame.display.update()
            continue

        direction = change_to

        if direction == 'UP':
            snake_position[1] -= 10
        elif direction == 'DOWN':
            snake_position[1] += 10
        elif direction == 'LEFT':
            snake_position[0] -= 10
        elif direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))

        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [random.randrange(1, (height // 10)) * 10,
                             random.randrange(1, (width // 10)) * 10]

        food_spawn = True
        game_window.fill(black)

        for block in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(block[0], block[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1], 12, 12))

        if snake_position[0] < 0 or snake_position[0] > height - 10 or snake_position[1] < 0 or snake_position[1] > width - 10:
            game_over(score)
            break

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(score)
                break

        show_score(score)

        pygame.display.update()
        fps.tick(snake_speed)

if __name__ == "__main__":
    user_id, username, level, score = user_login()
    game_loop(user_id, username, level, score)
