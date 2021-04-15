import pygame


class Hurdle:
    """ Class for the hurdle. """

    def __init__(self, x=0):
        self.size = (30, 60)    # Display and hit box size (in pixels)
        self.x = x + self.size[0] / 2    # x pos of centre of hurdle

        self.image = None
        self.load_image()

    def move(self, change):
        """ Move the hurdle. """
        self.x -= change

    def load_image(self):
        """ Load the image at "images/hurdle.png" into self.image """
        self.image = pygame.image.load("images/hurdle.png")

    def show(self, window, ground_height):
        """ Show the hurdle on window at ground_height.
        Parameters:
            window (pygame.Surface): surface to show image to
            ground_height (int): height of ground
        """
        # Get the position to display sprite at (self.pos is center position)
        top_left_pos = (self.x - self.size[0] / 2, ground_height - self.size[1])
        # pygame.draw.rect(window, (0, 0, 0), (top_left_pos[0], top_left_pos[1], self.size[0], self.size[1]))

        scaled_image = pygame.transform.scale(self.image, self.size)
        window.blit(scaled_image, top_left_pos)
