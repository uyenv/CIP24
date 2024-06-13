"""
This is just a plain source for me to look back on in case my laptop shuts down mid coding, further explanations 
will be included whenever my project is finished
This mini-game is called Karel Dance Audition where the player will press AWSD to score
**I coded this on Stanford CIP IDE, so if you want to pull down and see the results on your IDE, for example, VSCode or Pycharm,
you'll have to add something like 'canvas.update()' (every time an object was created) or 'canvas.mainloop' (in the end of the program). 
"""

"""
OBJECTIVES:
    Score count Milestone - Score count system: 
    1. Create a score_count variable
    2. If the key was pressed in the range of 
        current_y = static_y or current_y = static_y +- 2px => perfect_score
        perfect += 1
    3. Print the text "perfect" on the screen whenever the condition is met
    
    TODO: Handle "perfect" condition 
    
    CURRENT MILESTONE: Handle perfect condition
    
    Next's up:
    Make a series of Karel randomly appear on the screen
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

VEL = 7

DELAY = 0.005

#The texts appear during counting the score
PERFECT = 'perfect'
GOOD = 'good'
ALMOST_THERE = 'almost there'
MISS = 'miss :('
FONT_SIZE = 60
TEXT_DELAY = 0.3


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #draw static objects on the screen
    static_draw(canvas)

    #generate a random moving Karel from bellow the screen
    """
    The conditions of generating a moving Karel don't depent on the Karel itself
    but on each specific Xs of them
    """
    current_x = random.choice(MOVING_Xs)
    current_y = CANVAS_HEIGHT - KAREL_SIZE #Karel will move from bellow (for natural purposes lol)

    #Examine which Karel was generated from the random method
    moving_karel = generate_moving_karel(canvas, current_x, current_y) 
    right_key = which_moving_karel(current_x)

    """
    while True:
        #Animation
        current_y -= VEL
        canvas.moveto(moving_karel, current_x, current_y)
        time.sleep(DELAY)



        #handle key press
        key_pressed = canvas.get_last_key_press()

        Player can press multiple keys until it was the right key or current_y < -KAREL_SIZE -> delete current Karel
        If player pressed the right key, delete the moving Karel => Done
        If player misses the whole moving_karel, delete moving Karel when Karel has reached the end of the word => Done

        if key_pressed: #Wait until keys were being pressed before checking the condition
            if press_right_key(key_pressed, right_key): 
                delete_object(canvas, moving_karel)
                break
        #ultimate while loop stop condition even if the key was pressed or not
        if current_y < -KAREL_SIZE:
            delete_object(canvas, moving_karel)
            break


    """

    print_score_condition(canvas, GOOD)

    print("Finish test")




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

def generate_moving_karel(canvas, current_x, current_y):
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

def which_moving_karel(x):
    if x == LEFT_X:
        return 'a'
    if x == UP_X:
        return 'w'
    if x == DOWN_X:
        return 's'
    if x == RIGHT_X:
        return 'd'

def delete_object(canvas, obj):
    canvas.delete(obj)
    canvas.canvas.redraw(obj) #make sure the object is probably deleted

def press_right_key(key_pressed, right_key):
    return key_pressed == right_key

def delete_after_delayed_time(canvas, obj):
    """
    Delete the text after the delayed time
    """
    time.sleep(TEXT_DELAY)
    delete_object(canvas, obj)

def generate_text_perfect(canvas):
    perfect = canvas.create_text(
        (CANVAS_WIDTH * 0.37),
        (CANVAS_HEIGHT * 0.43),
        text = PERFECT,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'yellow'
    )
    return perfect

def generate_text_good(canvas):
    good = canvas.create_text(
        (CANVAS_WIDTH * 0.4),
        (CANVAS_HEIGHT * 0.43),
        text = GOOD,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'orange'
    )
    return good

def generate_text_almostthere(canvas):
    almostthere = canvas.create_text(
        (CANVAS_WIDTH * 0.27),
        (CANVAS_HEIGHT * 0.43),
        text = ALMOST_THERE,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'pink'
    )
    return almostthere

def generate_text_miss(canvas):
    miss = canvas.create_text(
        (CANVAS_WIDTH * 0.38),
        (CANVAS_HEIGHT * 0.43),
        text = MISS,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'turquoise'
    )
    return miss

def print_score_condition (canvas, condition):
    """
    Generate different texts on the screen based on the text that got passed in
    The text will appear in 0.3 seconds
    """
    if condition == PERFECT:
        text = generate_text_perfect(canvas)
        #delete_after_delayed_time(canvas)
    elif condition == GOOD: 
        text = generate_text_good(canvas)
        #delete_after_delayed_time(canvas, text)
    elif condition == ALMOST_THERE:
        text = generate_text_almostthere(canvas)
        #delete_after_delayed_time(canvas, text)
    elif condition == MISS:
        text = generate_text_miss(canvas)
        #delete_after_delayed_time(canvas, text)


if __name__ == '__main__':
    main()
