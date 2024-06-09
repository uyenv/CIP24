"""
This is just a plain source for me to look back on in case my laptop shut down mid coding, further explanations 
will be included whenever my project was finished
This mini game is called Karel Dance Audition
**I coded this on Stanford CIP IDE, so if you want to pull down and see the results on your IDE for example VSCode or Pycharm,
you'll have to add something like 'canvas.update()' or 'canvas.mainloop' though. 
"""
from graphics import Canvas
import random
import time

CANVAS_WIDTH = 680
CANVAS_HEIGHT = 500

KAREL_SIZE = 100
SPACE = 70 #Relative space amongst static Karels
#Coordinates of static Karels
LEFT_X = SPACE/2
UP_X = (SPACE/2 + KAREL_SIZE + SPACE + 5)
DOWN_X = (SPACE/2 + KAREL_SIZE + SPACE + KAREL_SIZE + SPACE - 5)
RIGHT_X = (CANVAS_WIDTH - KAREL_SIZE - SPACE/2)
STATIC_Y = 20
#Coordinates of moving Karels
MOVING_Xs= [LEFT_X, UP_X, DOWN_X, RIGHT_X] 
MOVING_Y = CANVAS_HEIGHT - KAREL_SIZE #Karel will move from bellow the screen (for natural purposes lol)
VEL = 6
DELAY = 1/(10**2)

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    static_draw(canvas)

    #generate a random moving Karel from bellow
    """
    The conditions of generating a moving Karel don't depent on the Karel itself
    but on each specific Xs of them
    """
    current_x = random.choice(MOVING_Xs)
    current_y = CANVAS_HEIGHT - KAREL_SIZE #Karel will move from bellow (for natural purposes lol)
    #Examine which Karel was generated from the random method
    moving_karel = which_moving_karel(current_x, current_y)

    while (current_y > 0):
        """
        current_y -= VEL
        canvas.moveto(moving_karel, current_x, current_y)
        key_pressed = canvas.get_last_key_press()
        if key_pressed == 'a':
            canvas.delete(moving_karel)
        """
        time.sleep(DELAY)



def static_draw(canvas):
    """
    Make static images appear on screen
    """
    #import background
    wallpaper = canvas.create_image_with_size(
        0, 0,
        CANVAS_WIDTH, CANVAS_HEIGHT,
        'darkPinkPurple.jpg'
    )
    #import static Karels
    left_static = canvas.create_image_with_size(
        LEFT_X, STATIC_Y,
        KAREL_SIZE, KAREL_SIZE,
        'left.png'
    )
    up_static = canvas.create_image_with_size(
        UP_X, STATIC_Y,
        KAREL_SIZE, KAREL_SIZE,
        'up.png'
    )
    down_static = canvas.create_image_with_size(
        DOWN_X, STATIC_Y,
        KAREL_SIZE, KAREL_SIZE,
        'down.png'
    )
    right_static = canvas.create_image_with_size(
        RIGHT_X, STATIC_Y,
        KAREL_SIZE, KAREL_SIZE,
        'right.png'
    )

def which_moving_karel(current_x, current_y):
    if current_x == LEFT_X:
        moving_karel = canvas.create_image_with_size(
            current_x, current_y,
            KAREL_SIZE, KAREL_SIZE,
            'left.png'
        )
    if current_x == UP_X:
        moving_karel = canvas.create_image_with_size(
            current_x, current_y,
            KAREL_SIZE, KAREL_SIZE,
            'up.png'
        )
    if current_x == DOWN_X:
        moving_karel = canvas.create_image_with_size(
            current_x, current_y,
            KAREL_SIZE, KAREL_SIZE,
            'down.png'
        )
    if current_x == RIGHT_X:
        moving_karel = canvas.create_image_with_size(
            current_x, current_y,
            KAREL_SIZE, KAREL_SIZE,
            'right.png'
        )
    return moving_karel

if __name__ == '__main__':
    main()
