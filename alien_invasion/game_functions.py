import sys
import pygame


def check_events():
    """Processes keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Updates images on the screen and shows new screen."""
    # Draw screen.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Shows last printed screen.
    pygame.display.flip()