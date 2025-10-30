import pygame
import os
import sys
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player")
LAVANDA = (230, 230, 250)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("timesnewroman", 25, italic=True, bold=True)

_songs = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3",
    "song4.mp3" ]

_current_index = 0
_is_playing = False
load_image = lambda n, s=(60, 60): pygame.transform.smoothscale(pygame.image.load(n).convert_alpha(), s)
img_prev = load_image("previous.png")
img_next = load_image("next.png")
img_play = load_image("play.png")
img_stop = load_image("stop.png")

buttons = {
    "prev": img_prev.get_rect(center=(100, 150)),
    "play": img_play.get_rect(center=(200, 150)),
    "next": img_next.get_rect(center=(300, 150)), }

def load_and_play(song_path):
    global _is_playing
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    _is_playing = True

def play_next():
    global _current_index
    _current_index = (_current_index + 1) % len(_songs)
    load_and_play(_songs[_current_index])

def play_prev():
    global _current_index
    _current_index = (_current_index - 1) % len(_songs)
    load_and_play(_songs[_current_index])

def toggle_play():
    global _is_playing
    if _is_playing:
        pygame.mixer.music.stop()
        _is_playing = False
    else:
        load_and_play(_songs[_current_index])

def draw():
    screen.fill(LAVANDA)
    song_text = font.render(f"{_songs[_current_index]}", True, BLACK)
    song_rect = song_text.get_rect(center=(WIDTH / 2, 60))
    screen.blit(song_text, song_rect)
    screen.blit(img_prev, buttons["prev"])
    screen.blit(img_next, buttons["next"])
    screen.blit(img_stop if _is_playing else img_play, buttons["play"])


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["prev"].collidepoint(event.pos):
                    play_prev()
                elif buttons["next"].collidepoint(event.pos):
                    play_next()
                elif buttons["play"].collidepoint(event.pos):
                    toggle_play()

        draw()
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()