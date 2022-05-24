import sys
import pygame
from settings import Settings


def run_game():
    # Initialization of pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Starting of main game cycle.
    while True:
        # Checking mouse and keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Draw screen.
        screen.fill(ai_settings.bg_color)
        # Shows last printed screen.
        pygame.display.flip()


run_game()
