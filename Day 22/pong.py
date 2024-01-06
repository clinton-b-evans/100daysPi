from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
player1 = Paddle((290,0))
player2 = Paddle((-290,0))
screen.tracer(0) # Turns off animation.
game_is_on = True


screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

# Main game loop
while game_is_on:
    screen.update()
screen.exitonclick()