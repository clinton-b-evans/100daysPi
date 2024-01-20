from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
with open("high_score.txt") as file:
    HIGH_SCORE = file.read()





class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.setposition(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        with open("high_score.txt",mode="w") as file:
           file.write(str(self.high_score))
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)