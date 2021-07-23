'''

Bouncing Ball Game

- This script is final project of Code In Place 2020(Harvard).
- This script uses only Tkinter for GUI, not pygame.

'''

# import modules
import tkinter
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# define constants
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels

PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 100

BALL_SIZE = 50
N_ROWS = 8
N_COLS = 10
rowsize = 20
colsize = 60


def main():
    score=0

    #Start Screen
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Break Brick')
    draw_square(canvas)

    # count down
    a=canvas.create_text(250, 350, anchor='w', font='TkMenuFont 80', text="3",fill='gold')
    canvas.update()
    time.sleep(1)
    canvas.delete(a)

    b = canvas.create_text(250, 350, anchor='w', font='TkMenuFont 80', text="2", fill='gold')
    canvas.update()
    time.sleep(1)
    canvas.delete(b)

    c = canvas.create_text(250, 350, anchor='w', font='TkMenuFont 80', text="1", fill='gold')
    canvas.update()
    time.sleep(1)
    canvas.delete("all")

    #game screen
    block_list=draw_square(canvas)
    ball = canvas.create_oval(300, 200, 300+BALL_SIZE, 200+BALL_SIZE, fill='red', outline='yellow4')
    
    # make a paddle
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT-25 , fill="dodger blue")  #dodger blue

    # set ball's velocity
    dx = 14
    dy = 10

    # loop until game or game over
    while True:

        # get the mouse location and react to it
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)

        # hit wall and bounce to another direction
        canvas.move(ball, dx, dy)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
        if hit_top_wall(canvas, ball):
            dy *= -1

        # check if the ball hits the paddle and bounce to another direction
        if hit_paddle(canvas, paddle):
            dy *= -1
            canvas.update()

        if hit_block(canvas,block_list):
            score=score+1
            dy*=-1

        # miss ball
        if hit_bottom_wall(canvas,ball):
            break

        # break all blocks
        if len(block_list)<1:
            break

        canvas.update()
        time.sleep(1/50.)


    #score screen
    canvas.delete("all")
    draw_square(canvas)
    total_score='Score:' + str(score)

    # win
    if len(block_list)<1:
        canvas.create_text(200, 250, anchor='w', font='TkMenuFont 35', text='You Win !', fill='gold')

    # game over
    else :
        canvas.create_text(200, 250, anchor='w', font='TkMenuFont 35', text='Game Over!',fill='gold')
    canvas.create_text(250, 350, anchor='w', font='TkMenuFont 35', text=total_score,fill='gold')
    canvas.mainloop()











def draw_square(canvas):
    block_list=[]
    for row in range(N_ROWS):
        for col in range(N_COLS):
            x = col*colsize
            y = row*rowsize
            color = get_color(row,col)
            block=canvas.create_rectangle(x+2, y+2, x + colsize, y + rowsize, fill=color,outline='white')
            block_list.append(block)
    return block_list


# create color blocks
def get_color(row,col):
    
    if row<1:
        color='orange'
    elif row<2:
        color='black'

    elif row<3:
        color='gold'
    elif row<4:
        color='aquamarine'
    elif row<5:
        color='RosyBrown'
    elif row<6:
        color='light green'
    elif row<7:
        color='YellowGreen'
    elif row<8:
        color='tan'
    return color


# check whether the ball hit the paddle
def hit_paddle(canvas, paddle):
    
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    y1 = paddle_coords[1]
    x2 = paddle_coords[2]
    y2 = paddle_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)

    return len(results) > 1

# check whether the ball hit the block
def hit_block(canvas,block_list):

    for num in block_list:
        paddle_coords = canvas.coords(num)
        x1 = paddle_coords[0]
        y1 = paddle_coords[1]
        x2 = paddle_coords[2]
        y2 = paddle_coords[3]
        results = canvas.find_overlapping(x1, y1, x2, y2)
        if len(results) > 1:
            canvas.delete(num)
            block_list.remove(num)

            return True


# check whether the ball hit the left wall
def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

# check whether the ball hit the top wall
def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

# check whether the ball hit the right wall
def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

# check whether the ball hit the bottom wall
def hit_bottom_wall( canvas, object ):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT

# get coordinates
def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


# create canvas of given width, height and title
def make_canvas(width, height, title):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas




if __name__ == '__main__':
    main()
