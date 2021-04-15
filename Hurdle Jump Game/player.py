import pygame
import time

GRAVITY = 0.001     # Gravity constant. Not 9.8 as everything is measured in pixels


class Player:
    """ Player class """

    def __init__(self, start_y=0):
        """ Initialize the player
        Sets the position to (0, 0) """
        self.pos = (150, start_y)       # Center position of player (in pixels)
        self.velocity_y = 0
        self.size = (60, 90)   # Size of hit box (in pixels)

        self.jump_power = 0.5
        self.on_ground = False

        self.images = None  # Will be initialized by load_images
        self.image_change_period = 0.1  # Seconds
        self.load_images()

    def update(self, d_time):
        """ Update the player.
        Do all the physics and input things - everything the player does minus display stuff.
        Parameters:
            d_time (float): Time between this frame and the last (in seconds)
        """
        self.handle_input()
        self.update_physics(d_time)

    def update_physics(self, d_time):
        """ Update the physics of the player.
        apply gravity and velocity. """
        self.apply_gravity(d_time)
        self.apply_velocity(d_time)

    def handle_input(self):
        """ Handle the player input.
        If the player pressed space and the player is on ground, call jump(). """
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):
        """ Increase the players' y velocity to make them jump. """
        self.velocity_y = -self.jump_power

    def apply_gravity(self, d_time):
        """ Apply gravity - decrease the velocity by x so player falls
        Parameters:
            d_time (float): Time between this frame and the last (in seconds)
        """
        self.velocity_y += d_time * GRAVITY

    def apply_velocity(self, d_time):
        """ Apply the velocity of the player to the y position.
        Parameters:
            d_time (float): Time between this frame and the last (in seconds)
        """
        self.pos = (self.pos[0], self.pos[1] + self.velocity_y * d_time)

    def stand(self, ground_y):
        """ Stop the player from falling below the floor (at y = ground y) """
        if self.pos[1] + self.size[1] / 2 >= ground_y:   # Is the player below or on the ground?
            self.pos = (self.pos[0], ground_y - self.size[1] / 2)   # Set the player to be standing
            self.velocity_y = min(self.velocity_y, 0)
            self.on_ground = True
        else:
            self.on_ground = False

    def load_images(self):
        """ Set/load the self.images list.
        Looks for the 6 images with names in the form images/player/runX.png where X is between 0 and 5 (inclusive) """
        self.images = []
        for i in range(6):
            self.images.append(pygame.image.load("images/player/run{}.png".format(str(i))))

    def show(self, window):
        """ Show the player animation.
        Animation speed can be changed by changing self.image_change_period
        Scale the image up to self.size.
        Parameters:
            window (pygame.Surface): Window to show image on
        """
        # Get the position to display sprite at (self.pos is center position)
        top_left_pos = (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2)

        # Background block to see hitbox (Temporary)
        # pygame.draw.rect(window, (0, 0, 0), top_left_pos + self.size)

        image_index = int((time.time() / self.image_change_period) % 6)
        image = self.images[image_index]
        scaled_image = pygame.transform.scale(image, self.size)
        window.blit(scaled_image, top_left_pos)
