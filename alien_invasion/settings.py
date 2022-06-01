class Settings:
    """Class for all game settings."""

    def __init__(self):
        """Initialization of game settings."""
        # Screen parameters.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # Ship settings.
        self.ship_speed_factor = 1.5
