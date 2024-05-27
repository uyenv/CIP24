from graphics import Canvas
"""
To draw a chess board with pink and beige

1st Mile Stone: Draw a square

2nd Mile Stone: Draw a row of square

3rd Mile Stone: Draw a chess board
"""
CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_WIDTH
N_ROWS = 8
N_COLS = N_ROWS
SIZE = CANVAS_WIDTH / N_ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for row in range (N_ROWS):
        for col in range (N_COLS):
            draw_square(canvas, row, col)

def draw_square(canvas, r, c):
    #What's the dependence of xs and ys
    #Nếu x thay đổi, thì điều gì khiến nó phụ thuộc vào
    #   mà thay đổi?

    top_x = c * SIZE    #col đổi thì top_x đổi
    top_y = r * SIZE    #row đổi thì top_y đổi
    #botx/y thay đổi chỉ từ tọa độ có sẵn
    #thêm vào một khoảng cách hằng số SIZE
    bot_x = top_x + SIZE 
    bot_y = top_y + SIZE
    
    color = get_color(r, c)

    canvas.create_rectangle(
        top_x,
        top_y,
        bot_x,
        bot_y,
        color,
        'red'
    )

def get_color(row, col):
    if is_even(row, col):   #True by default
        return 'pink'       #Set up a return True function, else would be False
    else:
        return 'beige'

def is_even(r, c):
    return ((r + c) % 2 == 0)

if __name__ == '__main__':
    main()
