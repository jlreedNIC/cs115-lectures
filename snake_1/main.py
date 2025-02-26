# -----
# Start to the snake game using PyGame
# Only creates a PyGame screen
# -----
import pygame

# init pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# set window title
pygame.display.set_caption("snake")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10
"""game loop"""
running = True
while running:
    """Handle events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """update our game state"""
    """ draw to our screen """
    # clear screen
    screen.fill("white")

    # draw rectangle
    pygame.draw.rect(screen, "green", pygame.Rect((100, 200), (100, 50)))

    # rectangle with parameters specified
    pygame.draw.rect(
        surface=screen,
        color=(200, 128, 50),                # brown color
        rect=pygame.Rect(540, 340, 50, 50)   # create a rectangle at (540,340)
                                             # that has height and width of 50
    )

    # draw circle
    pygame.draw.circle(screen, "blue", (100, 200), 40)

    # circle with parameters specified
    pygame.draw.circle(
        surface=screen, 
        color="black", 
        center=(200, 200),        # put center of circle at point (200, 200)
        radius=100                # give circle a radius of 100
    )

    # draw line
    pygame.draw.line(screen, "red", (450, 100), (200, 200), 5)

    # ellipse with parameters specified
    pygame.draw.ellipse(surface=screen,
                        color="red",
                        rect=pygame.Rect((100, 100),(100, 500)),
                       )

    # update screen
    pygame.display.flip()

    # fps
    dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()
