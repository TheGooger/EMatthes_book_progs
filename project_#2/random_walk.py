from random import choice


class RandomWalk:
    """Class for random walk generation."""

    def __init__(self, num_points=5000):
        """Initialization of walking attributes."""
        self.num_points = num_points
        # All walking starts at (0.0) point.
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Direction and length of movement."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Processes all walking points."""
        # Generation of steps with required length.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Zero movements.
            if x_step == 0 and y_step == 0:
                continue
            # Next values of x and y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)