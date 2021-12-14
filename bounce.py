#How to change the speed of the ball and the padde
from tkinter import *
import time
import random
from tkinter import messagebox

root = Tk()
root.resizable(0, 0)    #it is not resizable             #The binding function is used to deal    with the events. We can bind Python’s
# Functions and methods to an event as well as we can bind these functions to any particular widget.
root.title("!Bounce Game!")
canvas = Canvas(root, height=500, width=500, bd=0, highlightthickness=0,bg="#ffeaee")
l= Label(root, text="Score: ", font=("arial", 12, "bold"), bg="black", fg="white")
l.pack(fill=X)
canvas.pack()                 # The pack() fill option is used to make a widget fill the entire frame. The pack()
# expand option is used to expand the widget if the user expands the frame.

root.update()
score = 0


def update(score):
    l.configure(text="score: " + str(score))


class Ball:    #bluprint of the code
    score=0

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 240, 250)
        start = [-2, -1, 1, 2]
        random.shuffle(start)
        self.x=start[1]
        self.y = -6
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        global score
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                score += 1
                update(score)
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # this will give us [x1, y1, x2, y2]
        if pos[0] <= 0:
            self.x=4
        if pos[1] <= 0:
            self.y=4
        if pos[2] >= self.canvas_width:
            self.x= -4
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(245, 100, font=("arial", 15, "bold"), text="Game Over")
        if self.hit_paddle(pos) ==True:
            self.y =-4


class Paddle:

    def rightbutt(self, event):
        self.x = 6

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 360)
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0
        self.canvas.bind_all("<Left>", self.leftbutt)
        self.canvas.bind_all("<Right>", self.rightbutt)
        #The binding function is used to deal with the events.
        # We can bind Python’s Functions and methods to an event as well as we can bind these functions to any
        # particular widget.



    def leftbutt(self, event):
        self.x = -6


    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0



paddle = Paddle(canvas,'blue')
ball = Ball(canvas, paddle, 'red')
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    root.update_idletasks()
    root.update()
    time.sleep(0.013)       # sleep() is defined in time() module of python 3. Sometimes, there is a need to halt
                            # the flow of the program so that several other executions can take place or simply due to the utility required.
                            # sleep() can come handy in such a situation which provides an accurate and flexible way to halt the flow of code
                            # for any period of time. This function discusses the insight of this function.



score = "your score is: " + str(score)
messagebox.showinfo("Score", score)