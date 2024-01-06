from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x + self.x_move, new_y + self.y_move)
    
    def bounce(self):
        self.y_move *= -1

    def score(self):
        self.goto(0,0)
        self.bounce()
        self.x_move *= -1