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
    for i in range (0, 400):
        if (i % 20 == 0):
            goals.append(i)

    #1.2. Generate a goal from calling a random goal in the list of goals
    generate_goal(canvas, random.choice(goals))


    #2. Animation loop:
    #Create a start point for player
    left_x = 0
    top_y = 0
    right_x = SIZE
    bottom_y = SIZE

    player = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    """
    idk if this is right or wrong so just keeping it there

    #Set up an auto start up point for player
    In the beginning of the game, if player hasn't press any key
    player's blue square will automatically move in the right direction
    while canvas.get_last_key_press() is None:
        canvas.move(player, VELOCITY, 0)
        time.sleep(DELAY)
        if canvas.get_last_key_press():
            break
    """

    while True:
        #Handle key press
        key = canvas.get_last_key_press()
        if key is None:
            if direction is None or direction == 'right':
                canvas.move(player, VELOCITY, 0)
            if direction == 'down':
                canvas.move(player, 0, VELOCITY)
            if direction == 'up':
                canvas.move(player, 0, -VELOCITY)
            if direction == 'left':
                canvas.move(player, -VELOCITY, 0)
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
            
        #Detecting collisions
        current_x = canvas.get_left_x(player)   #track player's x
        current_y = canvas.get_top_y(player)    #track player's y
        if (current_x == CANVAS_WIDTH) or (current_y == CANVAS_HEIGHT):
            return 0    #end program

        #sleep
        time.sleep(DELAY)

def generate_goal(canvas, goal_left_x):
    goal = canvas.create_rectangle(
        goal_left_x,
        goal_left_x, 
        goal_left_x + SIZE,
        goal_left_x + SIZE,
        'red'
    )

if __name__ == "__main__":
    main()
