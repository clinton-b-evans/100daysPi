from turtle import Turtle, Screen

# Set up the screen and turtle. The colormode needs to be setup to use random 255 colors. 
screen = Screen()
screen.colormode(255)

from random import randint
raphael = Turtle()
raphael.shape("arrow")
count = 0
for _ in range(3,11,1):
    angle = int(360 / _)
    raphael.color(randint(0,255),
                  randint(0,255),
                  randint(0,255),)
    for shape in range(_):
        raphael.forward(100)
        raphael.left(angle)


screen.exitonclick()