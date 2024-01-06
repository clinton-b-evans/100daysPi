from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
right_paddle = Paddle((290,0))
left_paddle = Paddle((-290,0))
screen.tracer(0) # Turns off animation.
game_is_on = True


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Main game loop
while game_is_on:
    screen.update()
screen.exitonclick()