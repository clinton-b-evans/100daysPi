from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
right_paddle = Paddle((290,0))
left_paddle = Paddle((-290,0))
ball = Ball()
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
    ball.move()
    time.sleep(0.2)

screen.exitonclick()