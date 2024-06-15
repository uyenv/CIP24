"""
This is just a plain source for me to look back on in case my laptop shuts down mid coding, further explanations 
will be included whenever my project is finished
This mini-game is called Karel Dance Audition where the player will press AWSD to score
**I coded this on Stanford CIP IDE, so if you want to pull down and see the results on your IDE, for example, VSCode or Pycharm,
you'll have to add something like 'canvas.update()' (every time an object was created) or 'canvas.mainloop' (in the end of the program). 
"""

"""
OBJECTIVES:
    Score count Milestone - Score count system
    
    CURRENT MILESTONE: Test one_time_game function, make sure it runs smoothly => Done
    
    TODO: 
    1. Make a series of Karel randomly appear on the screen => Done
        1.1. Make the while True (animation loop) nested inside of the for loop
        1.2. The begin and end conditions of the one_time_game loop. 
            1.2.1. The helper function begins with what? => Canvas (parameter)
            1.2.2. The helper function ends with what? => Return value = PERFECT, GOOD, ALMOST THERE or MISS,
                    append the value into the list called score_lst
                    
    2. Think about the way to implement the dictionary to store PERFECT, GOOD, ALMOST THERE and MISS scores.
     2.1. The value which is returned from one_time_game after each and every time the game begins
     2.2. Make another helper function to count the times each unique value appeared on the screen,    
             resulting in the dictionary called score_dict to store the full wanted values
             with the key as each unique value and the key value as the score counts
"""
#TODO: Finish Score Count System
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

VEL = 10

DELAY = 0.005


#PERFECT score range in pixel: from left to right
"""
For easier interpretation: 
The y axist falls down, so the point from the top will 
have a smaller value than the point from further down
so the range will vary from top -> bottom
"""
#The range where player would have the perfect score
PERFECT_TOP = STATIC_Y
PERFECT_BOTTOM = STATIC_Y + int(KAREL_SIZE/3)

GOOD_TOP = PERFECT_BOTTOM
GOOD_BOTTOM = PERFECT_BOTTOM + int(KAREL_SIZE/2)

ALMOST_THERE_TOP = GOOD_BOTTOM
ALMOST_THERE_BOTTOM = int(CANVAS_HEIGHT/2)

#The texts appear during counting the score
PERFECT = 'perfect'
GOOD = 'good'
ALMOST_THERE = 'almost there'
MISS = 'miss :('
FONT_SIZE = 60
TEXT_DELAY = 0.3

#A list to store the values that will be returned after game_on()
score_lst = []


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #draw static objects on the screen
    static_draw(canvas)

    #TODO: GENERATE A SERIES OF 3 MOVING KARELS ONE BY ONE APPEAR ON THE SCREEN: => Finished
    for i in range (3):
        score = game_on(canvas)
        score_lst.append(score)
    print("Finish test")
    print("Here's a list of score: ", score_lst)




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
        delete_after_delayed_time(canvas, text)
    elif condition == GOOD: 
        text = generate_text_good(canvas)
        delete_after_delayed_time(canvas, text)
    elif condition == ALMOST_THERE:
        text = generate_text_almostthere(canvas)
        delete_after_delayed_time(canvas, text)
    elif condition == MISS:
        text = generate_text_miss(canvas)
        delete_after_delayed_time(canvas, text)

def was_in_range_of(y, range_left, range_right):
    for pos in range (range_left, range_right):
        if (y == pos):
            return True

def game_on(canvas):
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


    while True:
        """
        This loop began with a new random moving Karel accelerating from below the screen
        This loop ended with a value in return: 
                                                Perfect, Good, Almost There or Miss

        So in the end credit: 
        How many times one of four of these will be counted and print out the screen
        Data structure: Dictionary with key as score condition and value as times appear during the game
        """

        #Animation
        current_y -= VEL
        canvas.moveto(moving_karel, current_x, current_y)
        time.sleep(DELAY)

        #handle key press
        key_pressed = canvas.get_last_key_press()

        """
        Player can press multiple keys until it was the right key or current_y < -KAREL_SIZE -> delete current Karel
        If player pressed the right key, delete the moving Karel => Done
        If player misses the whole moving_karel, delete moving Karel when Karel has reached the end of the word => Done
        """

        if key_pressed: #Wait until keys were being pressed before checking the condition
            print("current_y:", current_y, "vs STATIC_Y:", STATIC_Y) #for testing cases
            #Handle the PERFECT score
            if press_right_key(key_pressed, right_key) and was_in_range_of(current_y, PERFECT_TOP, PERFECT_BOTTOM):
                print("Perfect Score: ", current_y)
                delete_object(canvas, moving_karel)
                print_score_condition(canvas, PERFECT)
                return PERFECT
            #Handle the GOOD score
            if press_right_key(key_pressed, right_key) and was_in_range_of(current_y, GOOD_TOP, GOOD_BOTTOM ):
                print("Good Score: ", current_y)
                delete_object(canvas, moving_karel)
                print_score_condition(canvas, GOOD)
                return GOOD
            #Handle the ALMOST_THERE score
            if press_right_key(key_pressed, right_key) and was_in_range_of(current_y, ALMOST_THERE_TOP , ALMOST_THERE_BOTTOM ):
                print("Almost there Score: ", current_y)
                delete_object(canvas, moving_karel)
                print_score_condition(canvas, ALMOST_THERE)
                return ALMOST_THERE
            #MISS if player pressed the right key but too soon
            if press_right_key(key_pressed, right_key) and was_in_range_of(current_y, ALMOST_THERE_BOTTOM, CANVAS_HEIGHT ):
                print("Miss Score: ", current_y)
                delete_object(canvas, moving_karel)
                print_score_condition(canvas, MISS)
                return MISS

        """
        If moving Karel has surpassed static Karel 
        and the last pressed key is still not right 
        (even if the key wasn't pressed, the condition of press_right_key() would be automatically false at first)
        -> print 'miss', delete moving karel
        """
        if current_y < -50 and ( press_right_key(key_pressed, right_key) == False ): 
            delete_object(canvas, moving_karel)
            print_score_condition(canvas, MISS)
            return MISS


if __name__ == '__main__':
    main()

