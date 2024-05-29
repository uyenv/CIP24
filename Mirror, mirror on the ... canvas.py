from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
RECT_WIDTH = 100
RECT_HEIGHT = 200

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create mirror line
    canvas.create_line(
        CANVAS_WIDTH / 2, 
        0, 
        CANVAS_WIDTH / 2, 
        CANVAS_HEIGHT)
    
    # Create red rectangle
    red_left_x = 20
    red_left_y = 50
    red_right_x = red_left_x + RECT_WIDTH
    red_right_y = red_left_y + RECT_HEIGHT
    canvas.create_rectangle(
        red_left_x, 
        red_left_y, 
        red_right_x,
        red_right_y,
        'red'
    )

    """
    Idea:
    Begin point:
    right_x(MirroredRect) is WIDTH - right_x(RedRect)
    right_y(MirroredRect) is right_y(RedRect)
    """

    #Create a mirrored rectangle with the color Blue!
    mirrored_right_x = CANVAS_WIDTH - red_left_x
    mirrored_right_y = red_right_y
    mirrored_left_x = mirrored_right_x - RECT_WIDTH
    mirrored_left_y = mirrored_right_y - RECT_HEIGHT
    canvas.create_rectangle(
        mirrored_left_x,
        mirrored_left_y,
        mirrored_right_x,
        mirrored_right_y,
        'blue'
    )

if __name__ == '__main__':
    main()
