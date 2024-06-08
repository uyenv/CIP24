from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
VELOCITY = 20

# if DELAY is larger, the game will go slower
DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    """
    set up a direction variable so I can repeatedly
    move player in the old direction before a new key was pressed
    """
    direction = None #This prevents the direction from being reset to None every while iteration.
    
    #1.Set up the goal (red rectangle)
    """
    The red rectangle will appear randomly on the screen
    as long as its x & y are both multiplies of 20
    suppose x & y were called value
        value = 20*k (k: int)
    or x mod 20 = 0
    """
    #1.1. Create a list of numbers that are the multiplies of 20
    goals = []
    for i in range (0, CANVAS_WIDTH):
        if (i % 20 == 0):
            goals.append(i)

    #1.2. Generate a goal from calling a random goal in the list of goals
    generate_goal(canvas, random.choice(goals), random.choice(goals))


    #2. Animation loop:
    #About a count variable to count the goals player ate & player interface
    ate_count = 0
    #ate_count display as text
    ate_text = canvas.create_text(
        0.5*SIZE,
        CANVAS_HEIGHT - 1.5*SIZE,
        font_size = 30,
        text = 'ATE:'
    )
    ate_count_text = canvas.create_text(
        3.8*SIZE,
        CANVAS_HEIGHT - 1.5*SIZE,
        font_size = 30,
        text = str(ate_count),
        color = 'green'
    )
    #Create a start point for player
    left_x = 0
    top_y = 0
    right_x = SIZE
    bottom_y = SIZE

    player = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    while True:
        #Handle key press
        key = canvas.get_last_key_press()

        if key == 'ArrowLeft':
            direction = 'left'
            canvas.move(player, -VELOCITY, 0)
        if key == 'ArrowRight':
            direction = 'right'
            canvas.move(player, VELOCITY, 0)
        if key == 'ArrowUp':
            direction = 'up'
            canvas.move(player, 0, -VELOCITY)
        if key == 'ArrowDown':
            direction = 'down'
            canvas.move(player, 0, VELOCITY)

        """
        In the beginning of the game, if player hasn't press any key
        player's blue square will automatically move in the right direction

        if the key was pressed before (aka direction was set), the snake will proceed to move in the same direction
        """
        if key is None:
            if direction is None or direction == 'right':
                canvas.move(player, VELOCITY, 0)
            if direction == 'down':
                canvas.move(player, 0, VELOCITY)
            if direction == 'up':
                canvas.move(player, 0, -VELOCITY)
            if direction == 'left':
                canvas.move(player, -VELOCITY, 0)

        #Detecting collisions 
        current_x = canvas.get_left_x(player)  #track player's current x
        current_y = canvas.get_top_y(player)    #track player's current y

        #Snake eating goals
        overlapping_objs = canvas.find_overlapping(
            current_x,
            current_y,
            current_x + SIZE,
            current_y + SIZE
        )

        """
        In this example, after printing out the overlapping_objs list
        the player was shape_1
        So anything not shape_1 overlapping with snake will be the goals
        """
        for overlapping_obj in overlapping_objs:
            """
            if the value in the list wasn't player (shape_1) itself
                1. Delete the current goal
                2. Generate a new goal
            """
            #if overlapping_obj != 'shape_1' and overlapping_obj != ate_count_text and overlapping_obj != ate_text:
                #canvas.delete(overlapping_obj)
                #generate_goal(canvas, random.choice(goals), random.choice(goals))

        #Create a point count system


        #End game condition
        if (current_x > CANVAS_WIDTH) or (current_y > CANVAS_HEIGHT) or (current_x < 0) or (current_y < 0):
            return 0  

        #sleep
        time.sleep(DELAY)

def generate_goal(canvas, goal_left_x, goal_top_y):
    goal = canvas.create_rectangle(
        goal_left_x,
        goal_top_y, 
        goal_left_x + SIZE,
        goal_top_y + SIZE,
        'red'
    )

if __name__ == "__main__":
    main()
