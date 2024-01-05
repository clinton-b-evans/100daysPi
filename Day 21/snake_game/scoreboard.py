from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("Score: 0", align="center", font=("Arial", 24, "normal"))

    
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))