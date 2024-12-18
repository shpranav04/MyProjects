import pygame
import sys
from pygame.locals import QUIT

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
RED_COLOR = (229, 9, 20)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 120
ANIMATION_DURATION = 2000  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Netflix Intro Animation')

font = pygame.font.Font(None, FONT_SIZE)

text_surface = font.render('NETFLIX', True, TEXT_COLOR)
text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    elapsed_time = pygame.time.get_ticks() - start_time

    if elapsed_time < ANIMATION_DURATION:
        scale_factor = 1 + elapsed_time / ANIMATION_DURATION
    else:
        scale_factor = 2  

    scaled_surface = pygame.transform.scale(
        text_surface, (int(text_rect.width * scale_factor), int(text_rect.height * scale_factor))
    )
    scaled_rect = scaled_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    pygame.draw.rect(screen, RED_COLOR, scaled_rect.inflate(20, 20))

    screen.blit(scaled_surface, scaled_rect)

    pygame.display.flip()

    clock.tick(60)

    if elapsed_time >= ANIMATION_DURATION:
        pygame.time.wait(1000)
        running = False

pygame.quit()
