from graphics import Canvas
import time
import game_body #obtain the score_dict after game_body was done executing

CANVAS_WIDTH = 680
CANVAS_HEIGHT = 500

#The texts appear during counting the score
PERFECT = 'perfect'
GOOD = 'good'
ALMOST_THERE = 'almost there'
MISS = 'miss :('

FONT_SIZE = 35
TEXT_GAP = 40

MISS_X = 310
MISS_Y = 172

AL_THR_X = (310 + TEXT_GAP*1.2)
AL_THR_Y = (172 + TEXT_GAP)

GOOD_X = (314 + TEXT_GAP*2.4)
GOOD_Y = (171 + TEXT_GAP*2)

PERFECT_X = (290 + TEXT_GAP*3.6)
PERFECT_Y = (171 + TEXT_GAP*3)

score_dict= {'perfect':12, 'good':0, 'almost there':10, 'miss :(':0}

#About the yes/ no boxes
#Save the x, y ranges of the yes and no coords
YES_LEFT_X = 235
YES_TOP_Y = 357
YES_RIGHT_X = 298
YES_BOTTOM_Y = 392

NO_LEFT_X = 333
NO_TOP_Y = 357
NO_RIGHT_X = 396
NO_BOTTOM_Y = 392

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #score_dict = game_body.main()
    static_draw(canvas)

    #create two boxes for YES an NO
    yes_box = canvas.create_rectangle(
        YES_LEFT_X, YES_TOP_Y,
        YES_RIGHT_X, YES_BOTTOM_Y,
        'pink'
    )
    no_box = canvas.create_rectangle(
        NO_LEFT_X, NO_TOP_Y, 
        NO_RIGHT_X, NO_BOTTOM_Y,
        'turquoise'
    )
    #handle mouse click -> yes or no box
    click = canvas.wait_for_click()
    click_x = canvas.get_mouse_x()
    click_y = canvas.get_mouse_y()
    #in the yes box range
    if click == yes_box: #not done yet
        print('yay')

def generate_text_perfect(canvas):
    canvas.create_text(
        PERFECT_X, PERFECT_Y,
        text = PERFECT,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'yellow'
    )

def generate_text_good(canvas):
    canvas.create_text(
        GOOD_X, GOOD_Y,
        text = GOOD,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'orange'
    )

def generate_text_almostthere(canvas):
    canvas.create_text(
        AL_THR_X, AL_THR_Y,
        text = ALMOST_THERE,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'pink'
    )

def generate_text_miss(canvas):
    canvas.create_text(
        MISS_X, MISS_Y,
        text = MISS,
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'turquoise'
    )

def generate_text(canvas, text_ ,text_x , text_y):
    canvas.create_text(
        text_x,
        text_y,
        text = str(text_),
        font = 'Calibri',
        font_size = FONT_SIZE,
        color = 'purple'
    )

def print_score_times(canvas, score_dict):
    for score, times in score_dict.items():
        if score == MISS:
            generate_text(canvas, times, MISS_X + 115, MISS_Y)
        if score == ALMOST_THERE:
            generate_text(canvas, times, AL_THR_X + 200, AL_THR_Y)
        if score == GOOD:
            generate_text(canvas, times, GOOD_X + 100, GOOD_Y)            
        if score == PERFECT:
            generate_text(canvas, times, PERFECT_X + 125, PERFECT_Y)

def print_score_names(canvas):
    generate_text_perfect(canvas)
    generate_text_good(canvas)
    generate_text_almostthere(canvas)
    generate_text_miss(canvas)

def calculate_total_score(score_dict):
    res = 0
    for score, times_appear in score_dict.items():
        if score == PERFECT:
            res += 100*times_appear
        if score == GOOD:
            res += 50*times_appear
        if score == ALMOST_THERE:
            res += 25*times_appear
        #of course if you miss, there's no cake for you, sadly :(
    return res

def static_draw(canvas):
    #Set up the wallpaper
    canvas.create_image_with_size(
        0, 0,
        CANVAS_WIDTH, 
        CANVAS_HEIGHT,
        'end_wall.png'
    )
    #print scores player obtained
    print_score_names(canvas)
    print_score_times(canvas, score_dict)
    #print total score
    total_score = calculate_total_score(score_dict)
    generate_text(canvas, total_score, 502, 410)

    generate_text(canvas, 'yes', 244, 356)
    generate_text(canvas, 'nah', 338, 360)


if __name__ == '__main__':
    main()
