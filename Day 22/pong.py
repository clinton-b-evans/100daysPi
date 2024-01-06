from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turns off animation.
game_is_on = True

# Create and move paddle before moving to pong.py file
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)
screen.update() # Refreshes screen after moving paddle.


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    screen.update() # Refreshes the screen after each movement.


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    screen.update()

# Main game loop
while game_is_on:
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")

    screen.exitonclick()