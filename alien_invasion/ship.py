import pygame


class Ship:

    def __init__(self, screen):
        """Initialization of the ship and it's started position."""
        self.screen = screen

        # Loading of ship image and getting rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship in current position."""
        self.screen.blit(self.image, self.rect)