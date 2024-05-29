from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24
FONT = 'Courier'

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    """
    Syntax: 
canvas.create_text(
    x, 
    y, 
    text = 'My first text!',
    font = 'Arial', 
    font_size = 50, 
    color ='blue'
)
    """
    #Create first line of text
    canvas.create_text(
        FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y,
        text = 'An old silent pond...',
        font = FONT,
        font_size = FONT_SIZE,
        color = 'blue'
    )
    #Calculate the space amongst lines of text
    space = FONT_SIZE + 4
    #Create second line of text
    canvas.create_text(
        FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + space,
        text = 'A frog jumps into the pond, ',
        font = FONT, 
        font_size = FONT_SIZE,
        color = 'blue'
    )
    #Create third line of text
    canvas.create_text(
        FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + space*2,
        text = 'splash! Silence again.',
        font = FONT, 
        font_size = FONT_SIZE,
        color = 'blue'
    )

#TODO: CREATE A FUNCTION WITH CONST VARS TO OPTIMIZE THE CREATE_TEXT FUNCs

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
