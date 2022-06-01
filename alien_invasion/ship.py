import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialization of the ship and it's started position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading of ship image and getting rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving floating coordinate of ship center.
        self.center = float(self.rect.centerx)
        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draws the ship in current position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updating ship position using flag."""
        # Updating center attribute.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Updating rect attribute with self.center.
        self.rect.centerx = self.center
