from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
scoreboard = Scoreboard()
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
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
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.score()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.score()
        scoreboard.right_point()



screen.exitonclick()