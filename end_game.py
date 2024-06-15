#TODO2: DELETE THE WHOLE CANVAS AFTER GAME_BODY to free memory

from graphics import Canvas
import time
#import game_body

CANVAS_WIDTH = 680
CANVAS_HEIGHT = 500

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #score_dict = game_body.main()
    static_draw(canvas)

def static_draw(canvas):
    canvas.create_image_with_size(
        0, 0,
        CANVAS_WIDTH, 
        CANVAS_HEIGHT,
        'lightPinkPurple.jpg'
    )
    #CREATE A TEST BORDER
    canvas.create_line(
        CANVAS_WIDTH/2, 0,
        CANVAS_WIDTH/2, CANVAS_HEIGHT
    )
    """
    top_line = canvas.create_line(
        CANVAS_WIDTH/2, CANVAS_HEIGHT/3.5, 
        CANVAS_WIDTH, CANVAS_HEIGHT/3.5, 
    )
    """
    canvas.create_oval(
        ((CANVAS_WIDTH*0.672) - 7), (((CANVAS_HEIGHT/3.5)/1.6) - 15),
        (CANVAS_WIDTH), ((CANVAS_HEIGHT/3.5) + 15),
        'purple',
        'white'
    )
    your_result_text =  canvas.create_text(
        CANVAS_WIDTH*0.69, ((CANVAS_HEIGHT/3.5)/1.6),
        text = 'your result',
        font = 'Aptos Display',
        font_size = 45,
        color = 'white'
    )
    wiggle(canvas, your_result_text)

#BUGGY
def wiggle(canvas, text):
    #make the text wiggle up and down lol
    #set up
    text_x = canvas.get_left_x(text)
    text_y = canvas.get_top_y(text)

    vel = 0.05 #change by
    
    while text_y >  (((CANVAS_HEIGHT/3.5)/1.6) - 5 ):
        text_y -= vel #update to new coordinate
        canvas.moveto(text, text_x, text_y) #demonstrate
        time.sleep(0.05) #make the update visible in real time



if __name__ == '__main__':
    main()
