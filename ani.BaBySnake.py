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
    #1.2. Generate a goal from calling a random goal in the list of goals
    left_x = random.choice(goals)
    goal = canvas.create_rectangle(
        left_x,
        left_x, 
        left_x + SIZE,
        left_x + SIZE,
        'red'
    )
  
    """
    #TODO: set up the world

    #animation loop
    while True:
        #Update the world

        #sleep
        time.sleep(DELAY)
    """

if __name__ == '__main__':
    main()
