from turtle import Turtle, Screen
import random

# Variables created
screen = Screen()
screen.colormode(255)
raphael = Turtle()
raphael.speed(0)
raphael.pensize(5)


# Functions created
def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        raphael.color(random_color())
        raphael.circle(100)
        raphael.setheading(raphael.heading() + size_of_gap)
    screen.exitonclick()

# Main program
draw_spirograph(5)
