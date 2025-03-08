# -----
# Snake game using PyGame
# -----
import pygame
from pygame.constants import KEYDOWN
import helper_functions

# ---
# main game
# ----
# init pygame
pygame.init()

# create font
system_fonts = pygame.font.get_fonts()
print(system_fonts)

my_font = pygame.font.SysFont(system_fonts[0], size=48, bold=True, italic=False)

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

# snake current position
cur_pos = [300, 200]
direction = "down"  # direction of snake traveling
snake_body = [  # snake body pieces
    [300, 200], 
    [300, 180], 
    [300, 160], 
    [300, 140]
]
score = 0        # to keep track of score

# generate random fruit position
fruit_pos = helper_functions.populate_fruit(min_y=100)
add_body = False

"""game loop"""
running = True
while running:
    """Handle events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # escape key
                running = False

            if event.key == pygame.K_w and direction != "down":  # up direction
                direction = "up"
            if event.key == pygame.K_s and direction != "up":  # down direction
                direction = "down"
            if event.key == pygame.K_a and direction != "right":  # left direction
                direction = "left"
            if event.key == pygame.K_d and direction != "left":  # right direction
                direction = "right"
    
    """update our game state"""
    # update current position
    # this allows for continuous movement
    # because we always update the current position
    # check function in helper file
    cur_pos = helper_functions.update_cur_pos(direction, cur_pos)
    if cur_pos == False:
        running = False

    # check if our snake has collided with its own body
    # this is done with Python functions
    if cur_pos in snake_body:
        print("You lose.")
        running = False

    # check if snake collided with fruit
    if cur_pos == fruit_pos:
        score += 10
        fruit_pos = helper_functions.populate_fruit(min_y=100)
        add_body = True
        
    # snake movement
    snake_body.insert(0, list(cur_pos))
    if add_body:
        add_body = False
    else:
        snake_body.pop()
   
    
    """ draw to our screen """
    # clear screen
    screen.fill("white")

    # draw text to screen
    helper_functions.draw_text(f'Score: {score}', (20,20), "red", my_font, screen)
    helper_functions.draw_text(f'Snake!', (300,20), "blue", my_font, screen)

    # draw fruit
    helper_functions.draw_square(screen, "red", fruit_pos)
    
    # draw snake
    for body in snake_body:
        helper_functions.draw_square(screen, "green", body)

    # update screen
    pygame.display.flip()

    # fps
    dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()
