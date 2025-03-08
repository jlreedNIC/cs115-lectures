from random import randint
from pygame import draw, Rect

# -----
# Function definitions
# ------
def draw_text(text, coordinate, text_color, my_font, screen):
    """
    this function draws text to the screen
    
    text: variable that holds our text
    coordinate: hold our coordinate values
    text_color: holds the color of text, string or list
    
    """
    text_image = my_font.render(text, True, text_color)
    text_rect = text_image.get_rect()
    text_rect.topleft = coordinate
    screen.blit(text_image, text_rect)

def populate_fruit(min_x=0, max_x=600, min_y=0, max_y=400, block_size=20):
    """
    This function will generate a random x and y position, intended for fruit.
    It will generate a coordinate intended to be a block that the snake will 
    run into. This means it will not generate a position that the snake will
    only cover half of.

    min_x: variable holding min x coordinate of playing field
           defaults to 0 value
    max_x: variable holding max x coordinate of playing field
           defaults to 600 value
    min_y: variable holding min y coordinate of playing field
           defaults to 0 value
    max_y: variable holding max y coordinate of playing field
           defaults to 400 value
    block_size: variable for the size of blocks in the game
                defaults to 20 value
     
    returns: x and y position, integers
    """
    xpos = int(randint(min_x, max_x-block_size)/block_size)*block_size
    ypos = int(randint(min_y, max_y-block_size)/block_size)*block_size

    return [xpos, ypos]

def update_cur_pos(direction, cur_pos, xbound=600, ybound=400):
    """
    This function updates the current position based on the direction.
    It will also check for if we've run into any boundary. If we've
    run into a boundary, the function will return a False value instead
    of the current position.
    
    direction: variable holding string value of direction
    cur_pos: variable holding list of 2 coordinates, x and y
    xbound: maximum x value 
    ybound: maximum y value
    
    returns: coordinate list, or False if error
    """
    still_running = True
    if direction == "up":
        cur_pos[1] -= 20
    if direction == "down":
        cur_pos[1] += 20
    if direction == "left":
        cur_pos[0] -= 20
    if direction == "right":
        cur_pos[0] += 20

    # update bounds
    # check our boundaries after we update our current position
    if cur_pos[0] < 0:  # x direction bounds
        cur_pos[0] = 0
        still_running = False
    if cur_pos[0] > xbound - 20:
        cur_pos[0] = xbound - 20
        still_running = False

    if cur_pos[1] < 0:  # y direction bounds
        cur_pos[1] = 0
        still_running = False
    if cur_pos[1] > ybound - 20:
        cur_pos[1] = ybound - 20
        still_running = False

    if still_running:
        return cur_pos
    else:
        return still_running

def draw_square(screen, color, position, block_size=20):
    """
    This function draws a square to the screen at the specified
    position with the specified color and size.
    
    screen: the screen to draw to
    color: the color to make the square
           can be a string or an RGB value
    position: the coordinates of the square, list format
    block_size: size of the square
                defaults to 20
    """
    draw.rect(screen, color, Rect(position, (block_size,block_size)))

