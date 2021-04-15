from hurdle import Hurdle
import random

SPEED_MULTIPLIER = 0.2


class Hurdle_Handler:
    """ Class to handle the hurdles. """

    def __init__(self, ground_y):
        self.hurdles = []
        self.spawn_period = 2   # Spawn a hurdle every x seconds
        self.spawn_period_variance = 1
        self.time_until_next = 0    # Seconds
        self.ground_y = ground_y    # Height of ground

    def update(self, d_time, window_width, game_speed):
        """ Update the handler.
        Spawn new hurdles, delete old ones, move existing.
        Parameters:
            d_time (float): Time between this frame and the last (in seconds)
            window_width (int): width of screen
            game_speed (float): game speed multiplier
        """
        self.spawn(d_time, window_width)
        self.move(d_time, game_speed)
        self.delete_old()

    def delete_old(self):
        """ If a hurdle has run off screen, forget it.
        Sets self.hurdles to a new list of the hurdles still on screen. """
        hurdles = []
        for hurdle in self.hurdles:
            if not hurdle.x + hurdle.size[0] / 2 < 0:    # If hurdle not off screen
                hurdles.append(hurdle)
        self.hurdles = hurdles

    def move(self, d_time, game_speed):
        """ Move the hurdles.
        loop through each and call move() """
        for hurdle in self.hurdles:
            hurdle.move(d_time * game_speed * SPEED_MULTIPLIER)

    def spawn(self, d_time, window_width):
        """ Handle hurdle spawning.
        If it's time to spawn a new hurdle, do it and reset the timer. """
        self.time_until_next -= d_time / 1000
        if self.time_until_next <= 0:
            self.time_until_next = self.spawn_period + (random.random() * 2 - 1) * self.spawn_period_variance
            self.spawn_new(window_width)

    def spawn_new(self, window_width):
        """ Spawn a new hurdle """
        self.hurdles.append(Hurdle(window_width))

    def show(self, window):
        """ Show all the hurdles.
        Call the show method of each of the hurdles. """
        for hurdle in self.hurdles:
            hurdle.show(window, self.ground_y)
