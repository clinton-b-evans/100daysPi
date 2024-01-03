from turtle import Turtle, Screen

# Set up the screen and turtle. The colormode needs to be setup to use random 255 colors. 
screen = Screen()
screen.colormode(255)

import random
from random import randint
raphael = Turtle()
raphael.hideturtle()
raphael.pensize(10)
directions = [0,90,180,270]
while True:
    raphael.color(randint(0,255),
                  randint(0,255),
                  randint(0,255),)
    raphael.forward(30)
    print(raphael.pos())
    raphael.setheading(random.choice(directions))
screen.exitonclick()

