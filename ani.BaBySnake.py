from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if DELAY is larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
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
    #1.2. Generate a goal by calling a random goal in the list of goals
    left_x = random.choice(goals)
    goal = canvas.create_rectangle(
        left_x,
        left_x, 
        left_x + SIZE,
        left_x + SIZE,
        'red'
    )
  
    #animation loop:
    #Create a starting point for player
    left_x = 0
    top_y = 0
    right_x = SIZE
    bottom_y = SIZE

    player = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    while True:
        #update the world
        current_x = canvas.get_left_x(player)   #track player's x
        current_y = canvas.get_top_y(player)    #track player's y

        #Handle key press
        key = canvas.get_last_key_press()
        if key is None:
            canvas.move(player, VELOCITY, 0) #player will move with the velocity = 20 px each time

        #if key == 'ArrowLeft':

        #if key == 'ArrowRight':

        #if key == 'ArrowUp':

        #if key == 'ArrowDown':
            #canvas.move(player, 0, VELOCITY)

        #Detecting collisions
        if (current_x == CANVAS_WIDTH) or (current_y == CANVAS_HEIGHT):
            return 0    #end program

        #sleep
        time.sleep(DELAY)


if __name__ == '__main__':
    main()
