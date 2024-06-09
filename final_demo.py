"""
This is just a plain source for me to look back on in case my laptop shut down mid coding, further explanations 
will be included whenever my project was finished
This mini game is called Karel Dance Audition
**I coded this on Stanford CIP IDE, so if you want to pull down and see the results on your IDE EX VSCode,
you'll have to add something like 'canvas.update()' or 'canvas.mainloop' though. 
"""
from graphics import Canvas
    
CANVAS_WIDTH = 680
CANVAS_HEIGHT = 500

KAREL_SIZE = 100
SPACE = 70 #Relative space amongst static Karels
#Coordinates of static Karels
LEFT.X = SPACE/2
UP.X = (SPACE/2 + KAREL_SIZE + SPACE + 5)
DOWN.X = (SPACE/2 + KAREL_SIZE + SPACE + KAREL_SIZE + SPACE - 5)
RIGHT.X = (CANVAS_WIDTH - KAREL_SIZE - SPACE/2)
STATIC.Y = 20


def main():
    static_draw()


def static_draw():
    """
    Make static images appear on screen
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #import background
    wallpaper = canvas.create_image_with_size(
        0, 0,
        CANVAS_WIDTH, CANVAS_HEIGHT,
        'darkPinkPurple.jpg'
    )
    #import static Karels
    left_static = canvas.create_image_with_size(
        LEFT.X, STATIC.Y,
        KAREL_SIZE, KAREL_SIZE,
        'left.png'
    )
    up_static = canvas.create_image_with_size(
        UP.X, STATIC.Y,
        KAREL_SIZE, KAREL_SIZE,
        'up.png'
    )
    down_static = canvas.create_image_with_size(
        DOWN.X, STATIC.Y,
        KAREL_SIZE, KAREL_SIZE,
        'down.png'
    )
    right_static = canvas.create_image_with_size(
        RIGHT.X, STATIC.Y
        KAREL_SIZE, KAREL_SIZE,
        'right.png'
    )

if __name__ == '__main__':
    main()
