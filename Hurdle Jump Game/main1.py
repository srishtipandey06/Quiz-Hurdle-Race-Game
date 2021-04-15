import pygame
from player import Player  # Import our Player class
from hurdle_handler import Hurdle_Handler

WINDOW_SIZE = (720, 360)
GROUND_Y = 280


def event_handler():
    """ Returns all pygame events.
    Checks and handles the QUIT event.
    Returns:
        events (list): pygame events
    """
    events = pygame.event.get()
    for event in events:

        # Has the quit button been pressed?
        if event.type == pygame.QUIT:
            quit()


def show_ground(window, primary_color=(34,139,34), secondary_color=(153, 102, 0), surface_height=15):
    """ Show an orange rectange where the ground is.
    Parameters:
        window (pygame.Surface): Window to show rect on
        primary_color (tuple): Main color of the ground
        secondary_color (tuple): Color of the surface of the ground
        surface_height (int): Height of the surface to display
    """
    pygame.draw.rect(window, primary_color, (0, GROUND_Y, WINDOW_SIZE[0], WINDOW_SIZE[1] - GROUND_Y))
    pygame.draw.rect(window, secondary_color, (0, GROUND_Y, WINDOW_SIZE[0], surface_height))


def has_player_hit_hurdle(player, hurdles, ground_height):
    """ Has the player hit a hurdle?
    Parameters:
         player (Player): player object to check collision for
         hurdles (list): list of hurdles to check
    Returns:
        touching (bool): has the player hit a hurdle?
    """
    player_rect = (player.pos[0] - player.size[0] / 2, player.pos[1] - player.size[1] / 2) + player.size
    for hurdle in hurdles:
        hurdle_rect = (hurdle.x - hurdle.size[0] / 2, ground_height - hurdle.size[1]) + hurdle.size
        if touching(player_rect, hurdle_rect):
            return True
    return False


def touching(rect1, rect2):
    """ Are the two rects touching?

    rects to be in the form (left x, right y, width, height)

    Parameters:
        rect1 (tuple): rect to check for collision with rect2
        rect2 (tuple): rect to check for collision with rect1
    """
    return (rect1[0] + rect1[2] >= rect2[0] and
            rect1[0] <= rect2[0] + rect2[2] and
            rect1[1] + rect1[3] >= rect2[1] and
            rect1[1] <= rect2[1] + rect2[3])


def show_text(window, text, size, pos, color=(0, 0, 0)):
    font = pygame.font.Font("mcFont.ttf", size)
    textSurf = font.render(text, True, color)
    window.blit(textSurf, pos)


def show_all(items, window, score, high_score):
    """ Show all items.
    it's assumed every item in items has a show(window) method. """
    window.fill((200, 236, 254))
    for item in items:
        item.show(window)
    show_ground(window)

    show_text(window, str(score), 60, (10, 10), color=(219, 90, 0))
    show_text(window, str(high_score), 60, (10, 70), color=(100, 40, 0))

    pygame.display.update()


def main():
    """ Main game function.
    Sets up the game and calls the game loop """
    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Antenna Hurdle Race")

    clock = pygame.time.Clock()
    player = Player(GROUND_Y)
    hurdle_handler = Hurdle_Handler(GROUND_Y)

    score = 0
    highscore = 0

    while True:  # Game loop
        event_handler()
        d_time = clock.tick()
        
        score += d_time / 200
        highscore = max(score, highscore)
        if (highscore==score and highscore>41):
          exec(open("quiz3.py").read(), globals())
          break
        # Update game
        player.update(d_time)
        player.stand(GROUND_Y)
        hurdle_handler.update(d_time, WINDOW_SIZE[0], 1 + score / 50)

        # Show everything
        show_all([player, hurdle_handler], window, int(score), int(highscore))

        if has_player_hit_hurdle(player, hurdle_handler.hurdles, GROUND_Y):
            player = Player(GROUND_Y)
            hurdle_handler = Hurdle_Handler(GROUND_Y)
            score = 0      
            

if __name__ == "__main__":  # If this is the file that was opened/run
    main()
    